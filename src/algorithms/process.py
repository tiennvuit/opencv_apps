import sys
import os
import argparse
import cv2
from defaults import *

# Imort all functions we have
from algorithm import Algorithm

def process(image, name_algorithm: str, *arg):
    """
    @day: 11-03-2020
    @author: Tien Nguyen
    @parameters:
        - image(image object).
        - name_algorithm (string): The name of alogorithm apply on the image.
        - *arg: some optional arguments.
    @return value:
        - An image object applied the alogithms/operation
    """
    if not name_algorithm in VALID_ALGORITHMS:
        print("The name algorithm is not valid !")
        exit(2)

    if name_algorithm == 'Convolution2D':
        output = Algorithm.Convolution2D(image)
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="the path of image", default="test.png")
    parser.add_argument("--operation", help="operation apply in image", default="Convolution2D")
    args = parser.parse_args()
    path_image = args.path
    operation = args.operation

    # If the path of image and operation is valid
    if not os.path.isfile(path_image):
        print("The path of image is not exist !")
        sys.exit(1)

    # otherwise
    image = cv2.imread(path_image)
    output = process(image=image, name_algorithm=operation)
    while True:
        cv2.imshow('Origin', image)
        cv2.imshow('Output', output)
        c = cv2.waitKey()
        if c == 27:
            break
    cv2.destroyAllWindows()
    print("Thank you for your using !")

if __name__ == "__main__":
    main()
