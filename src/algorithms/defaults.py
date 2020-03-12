import numpy as np
import cv2

DEFAULT_DDEPTH = -1

DEFAULT_FILTER = np.ones((3,3), np.float32) / 9.0

KERNEL_ITENSITY = np.array([[0,0,0], [0,1,0], [0,0,0]])

KERNEL_3x3 = np.ones((3,3), np.float32) / 9.0

KERNEL_5x5 = np.ones((5,5), np.float32) / 25.0

# DEFAULT_DIM = (600,400)

DEFAULT_INTERPOLATION = cv2.INTER_AREA

VALID_ALGORITHMS = {'Convolution2D'}
