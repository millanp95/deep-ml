import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	answer = {"magnitude":0.0, "direction":[0.0]*len(gradient), 'descent_direction':[0.0]*len(gradient)}

	l2 = sum([x**2 for x in gradient]) ** 0.5
	answer["magnitude"] = l2
	if l2 != 0:
		normalized = [x/l2 for x in gradient]
		descent = [-x for x in normalized]
		answer["direction"] = normalized
		answer["descent_direction"] = descent
	return answer