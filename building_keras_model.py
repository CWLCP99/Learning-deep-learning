# Sequential model 
import keras 
from keras import layers 

# Simplest way to create a Keras model is the sequential model: 

"""
model = keras.Sequential(
    [
        layers.Dense(64, activation= "relu"),
        layers.Dense(10, activation= "softmax")
    ]
    
)

"""