# -*- coding=utf-8 -*-
"""
classifer_server_flask.py: Use trained model to provide service
Author: Shi Zheyang
Date: 2020/08/17
"""
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
from gevent.pywsgi import WSGIServer
from urllib import request as u_request
from flask import Flask, jsonify, make_response, abort, request as f_request
from model.resnet import resnet_18, resnet_34

app = Flask(__name__)

NUM_CLASSES = 10
MODEL_PATH = "./model_weight/result"
test_model = resnet_18(NUM_CLASSES)
test_model.build(input_shape=(None, 32, 32, 3))
test_model.load_weights(MODEL_PATH)
label = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
print("===>Environment Init!!")


def image_url_input(image_url):
    """Get image from specified url
    Args:
        image_url: The url of image
    Returns:
        image
    """
    try:
        req = u_request.urlopen(image_url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, -1)  # 'load it as it is'
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
    except Exception as e:
        print(e)
        return None
    return image


def process_image(image):
    """Do pre-process for image: 1.resize image to (32, 32) 2.image/255"""
    image = image.resize((32, 32))
    image = tf.convert_to_tensor(np.array(image))
    image = (image / 255)
    # image = (image - img_mean) / img_std
    image = tf.expand_dims(tf.cast(image, dtype=tf.float32), 0)
    return image


@app.errorhandler(404)
def not_found(error):
    """Error handler"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/file_classifier", methods=['GET', 'POST'])
def file_server():
    """Server for image classifier for file"""
    # Receive a original image
    image = f_request.files['file']
    if image:
        image = Image.open(image)
        image = process_image(image)
        predictions = tf.argmax(test_model(image), axis=1)
        return str(predictions)
    abort(400)


@app.route("/url_classifier", methods=["GET", "POST"])
def url_server():
    """Server for image classifier for url"""
    if f_request.method == "POST":
        try:
            url_json = f_request.get_json()
            image = image_url_input(url_json['url'])
            image = process_image(image)
            result = test_model(image)
            output = np.argmax(result, axis=1)
            predictions = label[output[0]]
            return jsonify({predictions: float(result[0][output[0]])})
        except Exception as e:
            print(e)
    else:
        params = f_request.args
        if 'url' in params:
            image = image_url_input(params["url"])
            image = process_image(image)
            result = test_model(image)
            output = np.argmax(result, axis=1)
            predictions = label[output[0]]
            return jsonify({predictions: float(result[0][output[0]])})
        abort(400)


if __name__ == '__main__':
    WSGIServer(('0.0.0.0', 8001), app).serve_forever()
    #http://127.0.0.1:8000/url_classifier?url=https://img0.sc115.com/uploads3/sc/jpgs/1904/bpic11184_sc115.com.jpg
    #ab -n 1000 -c 200 10.15.121.165:8000/url_classifier?url=https://media.bnextmedia.com.tw/image/album/2018-01/img-1515398565-99051.jpg
    # -n 请求次数 -c 代表并发数
    # gunicorn -k gevent -c ../conf/gun.conf classifer_server_flask:app












