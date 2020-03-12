from defaults import *


class Algorithm():
    number_algorithm = 1

    def Convolution2D(image, ddepth=DEFAULT_DDEPTH, kernel=DEFAULT_FILTER):
        output = cv2.filter2D(src=image, ddepth=ddepth, kernel=kernel)
        return output
