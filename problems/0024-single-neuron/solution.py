import math
import numpy as np

def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = [round(sigmoid(np.dot(x, weights) + bias), 4) for x in features]
    mse = round(sum([(p - l)**2 for p, l in zip(probabilities, labels)])/len(labels), 4)
	return probabilities, mse