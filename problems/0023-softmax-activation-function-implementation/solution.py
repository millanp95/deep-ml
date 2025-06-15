import math

def softmax(scores: list[float]) -> list[float]:
	denominator = sum([math.exp(z) for z in scores])
	probabilities = [round(math.exp(z) / denominator, 4) for z in scores]
	return probabilities