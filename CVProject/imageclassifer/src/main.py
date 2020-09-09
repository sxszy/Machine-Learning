# -*- coding=utf-8 -*-
"""
main.py: Main function
Author: Shi Zheyang
Date: 2020/08/17
"""
import tensorflow as tf
import time
import os
import math
import tensorflow_datasets as tfds

from matplotlib import pyplot as plt
from model.resnet import resnet_18, resnet_34
from tensorflow.keras import optimizers, datasets, Sequential, layers

tf.random.set_seed(2345)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
BATCH_SIZE = 256
EPOCHS = 30
LEARNING_RATE = 1e-3
NUM_CLASSES = 10
AUTOTUNE = tf.data.experimental.AUTOTUNE
IMAGE_SIZE = 32
MODEL_PATH = "../model_weight/result"
SAVE_MODEL_DIR = "../save_model"
SAVE_TFLITE = "../tflite_model/model.tflite"

# GPU settings
gpus = tf.config.experimental.list_physical_devices('GPU')
print(gpus)
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)


# Date pre-process and argumentation
def preprocess(x, y, augment=False):
    """Pre-process: Normalization, random data argumentation
    Args:
        x: Image
        y: Label
    Returns:
        augment: If true, including augmentation. Default False.
    """
    # img_mean = tf.constant([0.4914, 0.4822, 0.4465])
    # img_std = tf.constant([0.2023, 0.1994, 0.2010])
    x = tf.cast(x, dtype=tf.float32) / 255
    if augment:
        x = tf.image.random_flip_left_right(x)
        x = tf.image.random_flip_up_down(x)
        x = tf.image.random_brightness(x, max_delta=0.5)
        x = tf.image.random_crop(x, size=[IMAGE_SIZE, IMAGE_SIZE, 3])
    # x = (x - img_mean) / img_std
    y = tf.cast(y, dtype=tf.int32)
    return x, y


print(tf.__version__)

# Create Dataset
(train_x, train_y), (test_x, test_y) = datasets.cifar10.load_data()

train_y = tf.squeeze(train_y, axis=1)
test_y = tf.squeeze(test_y, axis=1)

print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)

train_db = tf.data.Dataset.from_tensor_slices((train_x, train_y))
train_db = train_db.shuffle(1000).map(lambda x, y: preprocess(x, y, True),num_parallel_calls=4).batch(BATCH_SIZE).prefetch(buffer_size=AUTOTUNE)
test_db = tf.data.Dataset.from_tensor_slices((test_x, test_y))
test_db = test_db.map(lambda x, y: preprocess(x, y), num_parallel_calls=4).batch(BATCH_SIZE).prefetch(buffer_size=AUTOTUNE)
sample = next(iter(test_db))
test_image = sample[0][1]
label = sample[1][1]
# [b, 32, 32, 3]
# strategy = tf.distribute.MirroredStrategy()
# with strategy.scope():
model = resnet_18(NUM_CLASSES)
model.build(input_shape=(None, 32, 32, 3))
model.summary()

# Define optimizer and loss
optimizer = optimizers.Adam(LEARNING_RATE, decay=1e-2/EPOCHS)
# optimizer = optimizers.SGD(LEARNING_RATE, momentum=0.9, decay=5e-4)
# loss_object = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
loss_object = tf.keras.losses.CategoricalCrossentropy(from_logits=False)

train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.CategoricalAccuracy(name='train_accuracy')

valid_loss = tf.keras.metrics.Mean(name='valid_loss')
valid_accuracy = tf.keras.metrics.CategoricalAccuracy(name='valid_accuracy')


@tf.function
def train_step(x, y):
    """One train step"""
    with tf.GradientTape() as tape:
        # [b, 32, 32, 3] => [b, num_classes]
        logits = model(x, training=True)
        # [b] => [b, num_classes]
        y_onehot = tf.one_hot(y, depth=NUM_CLASSES)
        # compute losses
        loss = loss_object(y_true=y_onehot, y_pred=logits)

    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

    train_loss(loss)
    train_accuracy(y_onehot, logits)


@tf.function
def valid_step(x, y):
    """One valid step"""
    with tf.GradientTape() as tape:
        # [b, 32, 32, 3] => [b, num_classes]
        logits = model(x, training=False)
        # [b] => [b, num_classes]
        y_onehot = tf.one_hot(y, depth=NUM_CLASSES)
        # compute losses
        v_loss = loss_object(y_true=y_onehot, y_pred=logits)

    valid_loss(v_loss)
    valid_accuracy(y_onehot, logits)


def plot_result(train_acc, valid_acc, train_loss, valid_loss):
    """Plot train and valid result"""
    fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
    fig.suptitle('Training & Valid Metrics')

    axes[0].set_ylabel("Accuracy", fontsize=14)
    axes[0].set_xlabel("Epoch", fontsize=14)
    l1, = axes[0].plot(train_acc)
    l2, = axes[0].plot(valid_acc)
    axes[0].legend(handles=[l1, l2], labels=['train_acc', 'vaild_acc'], loc='best')

    axes[1].set_ylabel("Loss", fontsize=14)
    l3, = axes[1].plot(train_loss)
    l4, = axes[1].plot(valid_loss)

    axes[1].legend(handles=[l3, l4], labels=['train_loss', 'vaild_loss'], loc='best')
    fig.savefig(str(len(train_acc))+"_result.png")
    plt.show()


def learning_fn(epoch):
    """Return learning rate according epoch
    Args:
        epoch: The current epoch
    Returns:
        learning_rate
    """
    if epoch < 30:
        learning_rate = 1e-2
    elif epoch < 60:
        learning_rate = 1e-3
    else:
        learning_rate = 4e-4
    return learning_rate


def train(save_method="weights"):
    """Train process"""
    train_loss_list, train_accuracy_list, valid_accuracy_list, valid_loss_list = [], [], [], []
    max_acc = 0
    for epoch in range(EPOCHS):
        train_loss.reset_states()
        train_accuracy.reset_states()
        valid_loss.reset_states()
        valid_accuracy.reset_states()
        for step, (x, y) in enumerate(train_db):

            train_step(x, y)

            # optimizer.learning_rate = learning_fn(epoch)
            if step % 50 == 0:
                print("Epoch: {}/{}, step: {}/{}, loss: {:.5f}, accuracy: {:.3%}".format(epoch+1,
                                                                                         EPOCHS,
                                                                                         step,
                                                                                         math.ceil(train_x.shape[0] / BATCH_SIZE),
                                                                                         train_loss.result(),
                                                                                         train_accuracy.result()))

        for x, y in test_db:
            valid_step(x, y)

        print("Epoch: {}/{}, train loss: {:.5f}, train accuracy: {:.3%}, "
              "valid loss: {:.5f}, valid accuracy: {:.3%}, ".format(epoch + 1,
                                                                    EPOCHS,
                                                                    train_loss.result(),
                                                                    train_accuracy.result(),
                                                                    valid_loss.result(),
                                                                    valid_accuracy.result()))
        train_loss_list.append(train_loss.result())
        train_accuracy_list.append(train_accuracy.result())
        valid_loss_list.append(valid_loss.result())
        valid_accuracy_list.append(valid_accuracy.result())

        if valid_accuracy.result() > max_acc:
            print("save model, test accuracy is {:.3%}".format(valid_accuracy.result()))
            if save_method == "weights":
                model.save_weights(MODEL_PATH)

    plot_result(train_accuracy_list, valid_accuracy_list, train_loss_list, valid_loss_list)

    return model


def predict(model_path):
    """Classify a test image by using trained model"""
    test_model = resnet_18(NUM_CLASSES)
    test_model.build(input_shape=(None, 32, 32, 3))
    test_model.load_weights(model_path)
    input_image = tf.expand_dims(test_image, 0)
    predictions = test_model(input_image)
    print(tf.argmax(predictions, axis=1)[0])
    print(label)


if __name__ == '__main__':
    start = time.time()
    model = train()
    print("Time: ", time.time() - start)
    predict(MODEL_PATH)
    tf.saved_model.save(model, SAVE_MODEL_DIR)

    converter = tf.lite.TFLiteConverter.from_saved_model(SAVE_MODEL_DIR)
    converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
    tflite_model = converter.convert()

    with open(SAVE_TFLITE, "wb") as f:
        f.write(tflite_model)

