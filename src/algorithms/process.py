import sys
import os
import argparse
import cv2
from defaults import *

# Imort all functions we have
from algorithm import Algorithm

def process(image, name_algorithm: str, args):
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

    if name_algorithm == 'Bluring':
        size_bluring = int(args.size_bluring)
        output = Algorithm.Bluring(image=image, size=size_bluring)

    if name_algorithm == 'Sharpening':
        kernel_sharpen = str(args.kernel_sharpen)
        output = Algorithm.Sharpening(image=image, selected_kernel_sharpen=kernel_sharpen)

    if name_algorithm == 'Embossing':
        kernel_emboss = str(args.kernel_emboss)
        output = Algorithm.Embossing(image=image, selected_kernel_emboss=kernel_emboss)

    if name_algorithm == 'Embossing_advance':
        kernel_emboss_adv = str(args.kernel_emboss_adv)
        ksize = int(args.ksize)
        print(kernel_emboss_adv)
        output = Algorithm.Embossing_advance(image=image, selected_kernel_emboss=kernel_emboss_adv, ksize=ksize)

    if name_algorithm == 'Color_space_convert':
        source_cs = args.source_cs
        destination_cs = args.destination_cs
        output = Algorithm.Color_space_convert(image=image, src_cs=source_cs, dst_cs=destination_cs)

    if name_algorithm == 'Erosion':
        ksize = int(args.ksize)
        iterations = int(args.iterations)
        output = Algorithm.Erosion(image, ksize=ksize, iterations=iterations)

    if name_algorithm == 'Dilation':
        ksize = int(args.ksize)
        iterations = int(args.iterations)
        output = Algorithm.Dilation(image, ksize=ksize, iterations=iterations)

    if name_algorithm == 'Vignette_filter':
        output = Algorithm.Vignette_filter(image)

    if name_algorithm == 'Enhancing_contrast':
        option = args.option_contrast
        output = Algorithm.Enhancing_contrast(image=image, option=option)

    if name_algorithm == 'Translation':
        dx = int(args.dx)
        dy = int(args.dy)
        output = Algorithm.Translation(img=image,dx=dx,dy=dy)

    if name_algorithm == 'Rotation':
        angle = int(args.angle)
        output = Algorithm.Rotation(img=image,angle=angle)

    if name_algorithm == 'Scale':
        fx = float(args.fx)
        fy = float(args.fy)
        output = Algorithm.Scaling(img=image,fx=fx,fy=fy)

    if name_algorithm == 'Vertical_wave':
        dx = int(args.dx)
        output = Algorithm.Vertical_wave(img=image,dx=dx)

    if name_algorithm == 'Horizontal_wave':
        dy = int(args.dy)
        output = Algorithm.Horizontal_wave(img=image,dy=dy)

    if name_algorithm == 'Double_wave':
        dx = int(args.dx)
        dy = int(args.dy)
        output = Algorithm.Double_wave(img=image,dx=dx,dy=dy)

    if name_algorithm == 'Concave_effect':
        output = Algorithm.Concave_effect(img=image)


    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="the path of image", default="test.png")
    parser.add_argument("--source_cs", help="color space source", default='RGB')
    parser.add_argument("--destination_cs", help="color space destination", default='GRAY')
    parser.add_argument("--operation", help="operation apply in image", default="Convolution2D")
    parser.add_argument("--size_bluring", help="size of kernel bluring", default=SIZE_BLURING)
    parser.add_argument("--kernel_sharpen", help="the kernel sharpening", default=1)
    parser.add_argument("--dx", help= "distance along x-axis", default =0)
    parser.add_argument("--dy", help = "distance along y-axis", default =0)
    parser.add_argument("--fx", help= "ratio along x-axis", default =0)
    parser.add_argument("--fy", help = "ratio along y-axis", default =0)
    parser.add_argument("--angle", help = "angle", default = 0)
    parser.add_argument("--kernel_emboss", help="the kernel embossing", default=1)
    parser.add_argument("--kernel_emboss_adv", help="the kernel embossing advance", default='sobel_horizontal')
    parser.add_argument("--ksize", help="kernel size value in Sobel filter", default=5)
    parser.add_argument("--iterations", help="Iteration in erosion/dilate", default=1)
    parser.add_argument("--option_contrast", help="Choose the way enhance contrast", default=None)

    args = parser.parse_args()
    path_image = args.path
    operation = args.operation

    # If the path of image and operation is valid
    if not os.path.isfile(path_image):
        print("The path of image is not exist !")
        sys.exit(1)

    # otherwise
    image = cv2.imread(path_image)
    output = process(image=image, name_algorithm=operation, args=args)
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
