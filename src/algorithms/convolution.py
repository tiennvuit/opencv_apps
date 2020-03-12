from defaults import *

def convolution2D(image, ddepth=DEFAULT_DDEPTH, kernel=DEFAULT_FILTER):
    """
        @day: 11-03-2020
        @author: Tien Nguyen
        @parameters:
            - image (image object): input image
            - ddepth (int): the desred depth of the destination image.
            - kernel (numpy.array): convolution kernel.
    """

    output = cv2.filter2D(src=image, ddepth=ddepth, kernel=kernel)
    return output
