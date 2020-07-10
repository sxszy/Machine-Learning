#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
The simple implement of SRCNN
Author: Shi Zheyang
Date: 2020/07/09
"""
from tensorflow import keras
from tensorflow.keras import Sequential, datasets, layers, optimizers, metrics
from super_resolution.srcnn.utils import *
from super_resolution.srcnn import config
from super_resolution.srcnn.model import SRCNN

import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
import pathlib
import glob
import random


print(tf.__version__)

# Load pre-process data
model_path = os.path.join(config.checkpoint_dir, "srcnn.h5")
if config.is_train == True:
    nx, ny = input_setup(config=config)

    data_dir = checkpoint_dir(config)

    input_, label_ = read_data(data_dir)

    train_dataset = tf.data.Dataset.from_tensor_slices((input_, label_))
    train_dataset = train_dataset.shuffle(1000).batch(32)

    # Build the model
    model = SRCNN(config)
    model.compile(optimizer=optimizers.Adam(config.learning_rate),
                  loss='mse',
                  metrics=['mae'])

    # Train the mode
    history = model.fit(train_dataset, epochs=config.epoch)
    model.save(model_path)
else:
    model = keras.models.load_model(model_path)
    # Test
    result = model.predict
