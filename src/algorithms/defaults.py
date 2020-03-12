import numpy as np

DEFAULT_DDEPTH = -1

DEFAULT_FILTER = np.ones((3,3), np.float32) / 9.0

KERNEL_ITENSITY = np.array([[0,0,0], [0,1,0], [0,0,0]])

KERNEL_3x3 = np.ones((3,3), np.float32) / 9.0

KERNEL_5x5 = np.ones((5,5), np.float32) / 25.0

ALGORITHMS = {'Convolution': 'convolution2D'}
