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
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def save_image(image, output_path):
    """Save the image"""
    cv2.imwrite(output_path, image)


def show_images():
    """Show the image"""
    pass


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
        h = (h / scale) * scale
        w = (w / scale) * scale
        image = image[0:h, 0:w, :]
    else:
        h, w = image.shape
        h = (h / scale) * scale
        w = (w / scale) * scale
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

    label_ = modcrop(image, scale)

    bicbuic_img = cv2.resize(label_, None, fx=1/scale, fy=1/scale, interpolation=cv2.INTER_CUBIC)
    input_ = cv2.resize(bicbuic_img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    return input_, label_


def prepare_data(dataset="Train"):
    """Prepare data
    Args:
        dataset: Choose train or test dataset,
        For train dataset, output would be a list storing the path of images
    """
    if dataset == "Train":
        data = pathlib.Path("/home/qzszy/github/Machine-Learning-and-Data-Mining/super-resolution/dataset/Train")

    pass


def load_data():
    """Load train data or test data"""
    pass


def make_sub_data():
    """Make the sub_data set"""
    pass


def merge(images, size, c_dim):
    """
        images is the sub image set, merge it
    """
    h, w = images.shape[1], images.shape[2]

    img = np.zeros((h * size[0], w * size[1], c_dim))
    for idx, image in enumerate(images):
        i = idx % size[1]
        j = idx // size[1]
        img[j * h: j * h + h, i * w: i * w + w, :] = image
        # cv2.imshow("srimg",img)
        # cv2.waitKey(0)

    return img


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
    if not os.path.isdir(os.path.join(os.getcwd(),config.checkpoint_dir)):
        os.makedirs(os.path.join(os.getcwd(),config.checkpoint_dir))

    if config.is_train:
        savepath = os.path.join(os.getcwd(), config.checkpoint_dir + '/train.h5')
    else:
        savepath = os.path.join(os.getcwd(), config.checkpoint_dir + '/test.h5')

    with h5py.File(savepath, 'w') as hf:
        hf.create_dataset('input', data=input_)
        hf.create_dataset('label', data=label_)


def input_setup(config):
    """
        Read image files and make their sub-images and saved them as a h5 file format
    """

    # Load data path, if is_train False, get test data
    data = load_data(config.is_train, config.test_img)

    padding = abs(config.image_size - config.label_size) / 2

    # Make sub_input and sub_label, if is_train false more return nx, ny
    sub_input_sequence, sub_label_sequence, nx, ny = make_sub_data(data, padding, config)


    # Make list to numpy array. With this transform
    arrinput = np.asarray(sub_input_sequence) # [?, 33, 33, 3]
    arrlabel = np.asarray(sub_label_sequence) # [?, 21, 21, 3]

    make_data_hf(arrinput, arrlabel, config)

    return nx, ny