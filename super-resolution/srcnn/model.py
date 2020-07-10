#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
model.py: Define SRCNN model
Author: Shi Zheyang
Date: 2020/07/09
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from tensorflow.keras import Sequential, datasets, layers, optimizers, metrics, Model
import tensorflow as tf
import os


class SRCNN(Model):

    def __init__(self):
        super(SRCNN, self).__init__()
        """Input parameter"""
        self.conv1 = layers.Conv2D(filters=64, kernel_size=9, activation=tf.nn.relu)
        self.conv2 = layers.Conv2D(filters=64, kernel_size=9, activation=tf.nn.relu)
        self.conv3 = layers.Conv2D()
        pass

    def call(self):
        pass
