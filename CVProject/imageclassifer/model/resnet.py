# -*- coding=utf-8 -*-
"""
resnet.py: Define resnet
Author: Shi Zheyang
Date: 2020/08/18
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential


class BasicBlock(layers.Layer):

    def __init__(self, filter_num, strides=1):
        super(BasicBlock, self).__init__()

        self.conv1 = layers.Conv2D(filter_num, (3, 3), strides=strides, padding='same')
        self.bn1 = layers.BatchNormalization(momentum=0.9, epsilon=1e-5)
        self.relu1 = layers.Activation('relu')

        self.conv2 = layers.Conv2D(filter_num, (3, 3), strides=1, padding='same')
        self.bn2 = layers.BatchNormalization(momentum=0.9, epsilon=1e-5)

        if strides != 1:
            self.downsample = layers.Conv2D(filter_num, (1, 1), strides=strides)
        else:
            self.downsample = lambda x: x

        self.relu2 = layers.Activation('relu')

    def call(self, inputs, training=None):
        out = self.conv1(inputs)
        out = self.bn1(out, training=training)
        out = self.relu1(out)

        out = self.conv2(out)
        out = self.bn2(out, training=training)

        indentity = self.downsample(inputs)

        output = layers.add([out, indentity])
        # change2
        output = self.relu2(output)

        return output


class ResNet(keras.Model):

    def __init__(self, layer_dim, num_classes=100):
        super(ResNet, self).__init__()
        # Input [b, h, w, c]
        self.stem = Sequential([
            layers.Conv2D(64, (3, 3), strides=(1, 1)),
            layers.BatchNormalization(momentum=0.9, epsilon=1e-5),
            layers.Activation('relu'),
            layers.MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding='same')
        ])

        self.layer1 = self.build_block(64, layer_dim[0])
        self.layer2 = self.build_block(128, layer_dim[1], strides=2)
        self.layer3 = self.build_block(256, layer_dim[2], strides=2)
        self.layer4 = self.build_block(512, layer_dim[3], strides=2)

        self.gap = layers.GlobalAveragePooling2D()
        self.fc = layers.Dense(num_classes)

    def call(self, inputs, training=None):
        out = self.stem(inputs, training=training)

        out = self.layer1(out, training=training)
        out = self.layer2(out, training=training)
        out = self.layer3(out, training=training)
        out = self.layer4(out, training=training)

        # [b, c]
        out = self.gap(out)
        # [b, num_classes]
        out = self.fc(out)

        return out

    def build_block(self, filter_num, blocks, strides=1):
        res_block = Sequential()
        res_block.add(BasicBlock(filter_num, strides))

        for _ in range(1, blocks):
            res_block.add(BasicBlock(filter_num, strides=1))

        return res_block


def resnet_18(num_classes=100):
    return ResNet([2, 2, 2, 2], num_classes)


def resnet_34(num_classes=100):
    return ResNet([3, 4, 6, 3], num_classes)

