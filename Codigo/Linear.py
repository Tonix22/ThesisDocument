import numpy as np
from layer import Layer

class Linear(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size)
        self.bias = np.random.randn(output_size, 1)

    def forward(self, input):
        self.input = input
        return  self.weights@self.input + self.bias

    def backward(self, output_gradient, learning_rate):
        weights_gradient = output_gradient @ self.input.T
        input_gradient   = self.weights.T  @ output_gradient
        self.weights    -= learning_rate * weights_gradient
        self.bias       -= learning_rate * output_gradient
        return input_gradient
      