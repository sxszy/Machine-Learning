#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
The simple implement of SRCNN
Author: Shi Zheyang
Date: 2020/07/09
Reference: https://github.com/kweisamx/TensorFlow-SRCNN
"""
from tensorflow import keras
from tensorflow.keras import Sequential, datasets, layers, optimizers, metrics
from super_resolution.srcnn.utils import *
from super_resolution.srcnn import config
from super_resolution.srcnn.model import SRCNN

import tensorflow as tf


print(tf.__version__)

# Load pre-process data
model_path = os.path.join(config.checkpoint_dir, "model_weight")
if config.is_train:
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
    model.save_weights(model_path)
else:
    nx, ny = input_setup(config=config)

    data_dir = checkpoint_dir(config)

    input_, label_ = read_data(data_dir)

    model = SRCNN(config)
    model.compile(optimizer=optimizers.Adam(config.learning_rate),
                  loss='mse',
                  metrics=['mae'])
    model.load_weights(model_path)
    result = model.predict(input_)
    image = merge(result, [nx, ny], config.c_dim)
    save_image(image, "result.png")
