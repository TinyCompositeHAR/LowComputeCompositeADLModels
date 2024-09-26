import tensorflow as tf
import tensorrt
import keras as k

print(tf.reduce_sum(tf.random.normal([1000, 1000])))
print(tf.config.list_physical_devices('GPU'))
print(tensorrt.__version__)
print(tf.__version__)
print(k.__version__)
