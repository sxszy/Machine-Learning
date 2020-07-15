#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
utils.py: Functions used in srcnn
Author: Shi Zheyang
Date: 2020/07/09
"""
import cv2
import numpy as np
import os
import h5py
import pathlib
import glob


def read_image(image_path):
    """Read the image
    Args:
        image_path: The path of image
    Returns:
        image: cv2-image(RGB)
    """
    # OpenCV is BGR, Pillow is RGB
    image = cv2.imread(image_path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def save_image(image, output_path):
    """Save the image
    Args:
        image: Input image
        output_path: The path of output image
    """
    cv2.imwrite(output_path, image*255)


def checkpoint_dir(config):
    if config.is_train:
        return os.path.join('./{}'.format(config.checkpoint_dir), "train.h5")
    else:
        return os.path.join('./{}'.format(config.checkpoint_dir), "test.h5")


def modcrop(image, scale):
    """Adjust the image size according to scale
    Args:
        image: Input image
        scale: The scaling factor
    Returns:
        image: Image after modcrop
    """
    if len(image.shape) == 3:
        h, w, _ = image.shape
        h = (h // scale) * scale
        w = (w // scale) * scale
        image = image[0:h, 0:w, :]
    else:
        h, w = image.shape
        h = (h // scale) * scale
        w = (w // scale) * scale
        image = image[0:h, 0:w]
    return image


def preprocess_data(image_path, scale=3):
    """Do pre-process on data, read->modcrop->scale
    Args:
        image_path: The path of image
        scale: Scaling factor, default 3
    Returns:
        input_: inputX after pre-process
        label_: inputY after pre-process
    """
    image = read_image(image_path)
    cv2.imwrite("origin.png", image)
    label_ = modcrop(image, scale)

    bicbuic_img = cv2.resize(label_, None, fx=1.0 / scale, fy=1.0 / scale, interpolation=cv2.INTER_CUBIC)
    input_ = cv2.resize(bicbuic_img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("input.png", input_)

    return input_, label_


def prepare_data(dataset="Train"):
    """Prepare data
    Args:
        dataset: Choose train or test dataset,
        For train dataset, output would be a list storing the path of images
    Returns:
        all_image_paths: The list of image paths
    """
    if dataset == "Train":
        data = pathlib.Path("/home/qzszy/github/Machine-Learning-and-Data-Mining/super_resolution/dataset/Train")
        all_image_paths = list(data.glob("*"))  # pathlib can easily used in joining path
    else:
        data = pathlib.Path("/home/qzszy/github/Machine-Learning-and-Data-Mining/super_resolution/dataset/Test/Set5")
        all_image_paths = list(data.glob("*"))  # pathlib can easily used in joining path
    all_image_paths = [str(image) for image in all_image_paths]
    print(all_image_paths)
    return all_image_paths


def load_data(is_train):
    """Load train data or test data
    Args:
        is_train: The flag stands for train or test.
    Returns:
        data: Return
    """
    if is_train:
        data = prepare_data("Train")
    else:
        data = prepare_data("Test")
    return data


def make_sub_data(data, padding, config):
    """Make the sub_data set
    Args:
        data: The list of image paths
        padding: The image padding of input to label
        config: The configuration
    Returns:
        sub_input_sequence: The list of sub input data
        sub_label_sequence: The list of sub label data
        nx: Number of x
        ny: Number of y
    """
    sub_input_sequence = []
    sub_label_sequence = []
    # For every image data
    for i in range(len(data)):
        # Do pre-process on image
        input_, label_ = preprocess_data(data[i], config.scale)

        if len(input_.shape) == 3:
            h, w, c = input_.shape
        else:
            h, w = input_.shape

        nx, ny = 0, 0
        for x in range(0, h - config.image_size + 1, config.stride):
            nx += 1
            ny = 0
            for y in range(0, w - config.image_size + 1, config.stride):
                ny += 1
                # Cut the image
                sub_input = input_[x: x + config.image_size, y: y + config.image_size]  # 33 * 33
                sub_label = label_[x + padding: x + padding + config.label_size, y + padding: y + padding + config.label_size]  # 21 * 21

                # Reshape subinput and sublabel
                sub_input = sub_input.reshape([config.image_size, config.image_size, config.c_dim])
                sub_label = sub_label.reshape([config.label_size, config.label_size, config.c_dim])

                # Normalize
                sub_input = sub_input / 255.0
                sub_label = sub_label / 255.0

                # Add to sequence
                sub_input_sequence.append(sub_input)
                sub_label_sequence.append(sub_label)

    return sub_input_sequence, sub_label_sequence, nx, ny


def read_data(path):
    """
        Read h5 format data file
        Args:
            path: file path of desired file
            data: '.h5' file format that contains  input values
            label: '.h5' file format that contains label values
    """
    with h5py.File(path, 'r') as hf:
        input_ = np.array(hf.get('input'))
        label_ = np.array(hf.get('label'))
        return input_, label_


def make_data_hf(input_, label_, config):
    """
        Make input data as h5 file format
        Depending on "is_train" (flag value), savepath would be change.
    """
    # Check the check dir, if not, create one
    if not os.path.isdir(os.path.join(os.getcwd(), config.checkpoint_dir)):
        os.makedirs(os.path.join(os.getcwd(), config.checkpoint_dir))

    if config.is_train:
        savepath = os.path.join(os.getcwd(), config.checkpoint_dir + '/train.h5')
    else:
        savepath = os.path.join(os.getcwd(), config.checkpoint_dir + '/test.h5')

    with h5py.File(savepath, 'w') as hf:
        hf.create_dataset('input', data=input_)
        hf.create_dataset('label', data=label_)


def merge(images, size, c_dim):
    """
        images is the sub image set, merge it
    """
    h, w = images.shape[1], images.shape[2]

    img = np.zeros((h * size[0], w * size[1], c_dim))
    for idx, image in enumerate(images):
        i = idx % size[1]  # return modulo
        j = idx // size[1]  # return reminder
        img[j * h: j * h + h, i * w: i * w + w, :] = image
        # cv2.imshow("srimg",img)
        # cv2.waitKey(0)

    return img


def input_setup(config):
    """
        Read image files and make their sub-images and saved them as a h5 file format
    """

    # Load data path, if is_train False, get test data
    data = load_data(config.is_train)

    padding = abs(config.image_size - config.label_size) // 2

    # Make sub_input and sub_label, if is_train false more return nx, ny
    sub_input_sequence, sub_label_sequence, nx, ny = make_sub_data(data, padding, config)
    print(len(sub_label_sequence))
    # Make list to numpy array. With this transform
    arrinput = np.asarray(sub_input_sequence)  # [?, 33, 33, 3]
    arrlabel = np.asarray(sub_label_sequence)  # [?, 21, 21, 3]
    print("input", arrinput.shape)
    make_data_hf(arrinput, arrlabel, config)
    return nx, ny


def compute_psnr(image1, image2):
    """Compute psnr
    Args:
        image1: result image
        image2: ground truth image
    Returns:
        psnr: Peak signal-to-noise ratio - PSNR = 20*log10(MAXI/sqrt(MSE))
    """
    diff = np.abs(image1 - image2)
    mse = np.square(diff).mean()
    psnr = 20*np.log10(255 / np.sqrt(mse))
    return psnr


def read_test_data(config):
    """Read test data
    Args:
        config: Configuration of project
    Returns:
        arrinput: The test data
    """
    data = load_data(config.is_train)

    test_data, test_label = preprocess_data(data[0], scale=3)
    test_data = test_data / 255
    test_label = test_label / 255
    arrinput = np.asarray(test_data)
    arrlabel = np.asarray(test_label)
    print("arrinput.shape", arrinput.shape)
    print("arrlabel.shape", arrlabel.shape)
    print("bibucic psnr:", compute_psnr(image1=(arrinput * 255), image2=(arrlabel * 255)))
    return arrinput, arrlabel
