def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	n,m = len(a), len(a[0])
	transpose = [[0]*n for i in range(m)]
	for i in range(n):
		for j in range(m):
			transpose[j][i] = a[i][j]
	return transpose