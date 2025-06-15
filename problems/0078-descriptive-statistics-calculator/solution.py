import numpy as np 
from collections import Counter
def descriptive_statistics(data):
	# Your code here
    c = Counter(data)
    data = np.array(data)
    mean = data.mean()
    median = np.median(data)
    std_dev = np.std(data)
    variance = std_dev**2
    percentiles = np.percentile(data, [25, 50, 75,])
    iqr = percentiles[2] - percentiles[0]
    
    mode = Counter(data).most_common(1)[0][0]


	stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
	return stats_dict