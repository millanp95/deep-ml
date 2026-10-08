def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	trace = sum([matrix[i][i] for i in range(len(matrix))])

	def det(matrix):

		if len(matrix) == 2:
			return matrix[0][0]* matrix[1][1] - matrix[0][1] *  matrix[1][0]
		else:
			idx = list(range(len(matrix)))
			return sum((-1)**J * matrix[0][J]*det([[matrix[i][j] for j in (idx[:J]+idx[J+1:])] for i in idx[1:]]) for J in idx)

	return det(matrix), trace