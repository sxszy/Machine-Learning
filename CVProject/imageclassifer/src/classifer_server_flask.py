# -*- coding=utf-8 -*-
"""
classifer_server_flask.py: Use trained model to provide service
Author: Shi Zheyang
Date: 2020/08/17
"""
import tensorflow as tf
import os
import sys
import requests
import numpy as np
import json
import logging
from io import BytesIO
from gevent.pywsgi import WSGIServer
from flask import Flask, request, jsonify, make_response
from model.resnet import resnet_18, resnet_34


app = Flask(__name__)


def test_image(image_path):
    img_mean = tf.constant([0.4914, 0.4822, 0.4465])
    img_std = tf.constant([0.2023, 0.1994, 0.2010])
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.resize(image, [32, 32])
    image = (image / 255)
    image = (image - img_mean) / img_std
    image = tf.expand_dims(tf.cast(image, dtype=tf.float32), 0)
    return image


@app.before_first_request
def get_model():
    """Load trained model"""
    pass


@app.errorhandler(404)
def not_found(error):
    """Error handler"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/image_classifier", methods=['GET', 'POST'])
def server():
    """Server for image classifier"""
    pass


if __name__ == '__main__':
    WSGIServer(('0.0.0.0', 8001), app).serve_forever()
    #http://127.0.0.1:8001/judge?text="公会拉人加微信456789"
    #ab -n 1000 -c 200 http://127.0.0.1:8001/judge?text="公会拉人加微信456789"
    # -n 请求次数 -c 代表并发数