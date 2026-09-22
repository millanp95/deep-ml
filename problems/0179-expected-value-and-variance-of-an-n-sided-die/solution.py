def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	mean = 1 / n * sum([x for x in range(1, n+1)])
	variance = 1 / n * sum([(x - mean)**2 for x in range(1, n+1)])
	return (mean, variance )