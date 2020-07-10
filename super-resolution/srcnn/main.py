#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
The simple implement of SRCNN
Author: Shi Zheyang
Date: 2020/07/09
"""
from tensorflow import keras
from tensorflow.keras import Sequential, datasets, layers, optimizers, metrics
import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
import pathlib
import glob
import random


print(tf.__version__)

# Load data
data_root = pathlib.Path("/home/qzszy/github/Machine-Learning-and-Data-Mining/super-resolution/dataset/Train")
for item in data_root.iterdir():
    print(item)
all_image_paths = list(data_root.glob("*")) # pathlib can easily used in joining path
all_image_paths = [str(item) for item in all_image_paths]
random.shuffle(all_image_paths)
print(all_image_paths)
train_dataset = tf.data.Dataset.from_tensor_slices((all_image_paths, all_image_paths))
train_dataset = train_dataset.map().shuffle(60).batch()

sample = next(iter(train_dataset))
print(sample[0].shape)
# Pre-process of the Input

pass

# Build the model

pass

# Train the model

pass

# Test model and evaluation

pass
