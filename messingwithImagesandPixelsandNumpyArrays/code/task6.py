import cv2  # Import OpenCV package
import numpy as np  # Imports numpy package
import os  # Import a python library

''' You need to complete following function for task 6 '''


def binary_threshold(image, rows, cols, channels):  # This function will binary threshold the image

    ''' Enter your code here'''
    for k in range(channels):  # Iterate through all channels
        for r in range(rows):  # Iterate through all pixel rows/height of the image
            for c in range(cols):  # Iterate through all pixel columns of the image
                if image[r][c][k] > 125:
                    image[r][c][k] = 255
                elif image[r][c][k] <= 125:
                    image[r][c][k] = 0
    return image  # return the image


def read_image(imagepath):  # This function will read the image from imagepath
    im = cv2.imread(imagepath)  # OpenCV function to read the image as RGB
    im = np.expand_dims(im[:, :, 0], axis=2)  # Use only first (blue) channel of the image and reshape the array to have one channel (rows x columns x 1)
    return im, im.shape


def write_image(imagename, im):  # This function will store image array (im) with name "imagename"
    if not os.path.exists('outputs'):  # Create output directory if it doesn't exist already
        os.mkdir('outputs')

    cv2.imwrite(os.path.join('outputs', imagename), im)  # Store the image in the path with the name "imagename"


im, shape = read_image('circle.png')  # Read circle.png image provided in the current directory
(rows, cols, channels) = shape

imcopy = binary_threshold(im.copy(), rows, cols,
                          channels)  # Make a copy of the original array and pass it to the function

write_image('thresh_125.jpg',
            imcopy)  # Store the thresholded image. You can change the name of the image to run the code for different threshold values
