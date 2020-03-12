import sys
import argparse
import cv2
# Imort all functions we have
from convolution import convolution2D


def process(image, name_algorithm: str, *arg):
    """
    @day: 11-03-2020
    @author: Tien Nguyen
    @parameters:
        - image(image object).
        - name_algorithm (string): The name of alogorithm apply on the image.
        - *arg: some optional arguments.
    @return value:
        - An image object applied the alogithms
    """
    name_function = ALGORITHMS[name_algorithm]

    if name_function == 'convolution2D':
        output = convolution2D(image=image)

    return output

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="the path of image")
    parser.add_argument("--operation", help="operation apply in image")


if __name__ == "__main__":
    main(sys.argv[1:])
