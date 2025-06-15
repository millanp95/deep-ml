import numpy as np

def distance(x, y):
	diff = np.array(x) - np.array(y)
    return np.dot(diff, diff)

def assign(points, centroids):
    assignments = []
    for x in points:
        distances = [distance(x, c) for c in centroids]
        assignments.append(np.argmin(distances))
    return assignments

def update_centroids(points, assignments, centroids):
	k = len(centroids)
    sums = np.zeros((k, len(points[0])))
    counts = np.zeros(k)
    
    for point, cluster_id in zip(points, assignments):
        sums[cluster_id] += np.array(point)
        counts[cluster_id] += 1
    
    for i in range(k):
        if counts[i] != 0:
        	centroids[i] = (tuple(sums[i] / counts[i]))

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    centroids = initial_centroids
    for _ in range(max_iterations):
        assignments = assign(points, centroids)
        update_centroids(po