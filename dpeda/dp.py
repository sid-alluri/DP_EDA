import numpy as np

dp_results = []
def AddNoise(data, epsilon=0.5):
    for i in range(len(data)):
        dp_results.append(data[i] + np.random.laplace(0,1.0/epsilon))
    return dp_results