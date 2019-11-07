import cv2  # Imports OpenCV package
import numpy as np  # Imports Numpy package
import os  # Imports python library


def generate_image():  # This function will generate an image for first 5 tasks
    im = np.ones(shape=(700, 700, 3)) * 255  # Initialize a numpy array of size (700 x 700 x 3) filled with value = 255
    im[100:300, 400:500, 1:] = 0  # For blue rectangle, set corresponding pixel values in red and green channels to zero
    im[30:400, 100:250, 0] = 0  # For green rectangle, set corresponding pixel values in blue and red channels to zero
    im[30:400, 100:250, 2] = 0
    im[500:600, 300:600, 0:2] = 0  # For red rectangle, set corresponding pixel values in blue and green channels to
    # zero
    return im, im.shape  # return image as numpy array and its shape


def write_image(imagename, im):  # This function will write image to the disk in output/[IMAGE_NAME]
    if not os.path.exists('outputs'):
        os.mkdir('outputs')
    cv2.imwrite(os.path.join('outputs', imagename), im)  # OpenCV function to write the image


''' You need to complete following function for task 1 '''


def count_pixels(image, rows, cols, channels):  # First task is to count the number of white, red, blue and total
    # number of pixels in
    # the image
    whitecount = 0  # Set white pixel counter to zero
    redcount = 0  # Set red pixel counter to zero
    bluecount = 0  # Set blue pixel counter to zero
    totalcount = 0  # Set counter of total number of pixels to zero
    for k in range(channels):  # Iterate through all channels
        for r in range(rows):  # Iterate through all pixel rows/height of the image
            for c in range(cols):  # Iterate through all pixel columns of the image
                ''' Write your code here'''
                if k == 0:
                    totalcount += 1
                    if image[r][c][0] == 255 and image[r][c][1] == 255 and image[r][c][2] == 255:
                        whitecount += 1
                    elif image[r][c][0] == 255:
                        bluecount += 1
                    elif image[r][c][2] == 255:
                        redcount += 1
    print('White pixels:', whitecount)  # Print final counts
    print('Red Pixels:', redcount)
    print('Blue Pixels:', bluecount)
    print('Total Pixels:', totalcount)


''' You need to complete following function for task 2 '''


def red_to_blue(image, rows, cols, channels):
    ''' Write your code here '''
    image[100:300, 400:500, 0] = 0
    image[100:300, 400:500, 2] = 255
    image[500:600, 300:600, 2] = 0
    image[500:600, 300:600, 0] = 255
    return image


''' You need to complete following function for task 3 '''


def remove_blue(image, rows, cols, channels):
    ''' Write your code here '''
    image[100:300, 400:500, 0:3] = 255
    return image


''' You need to complete following function for task 4 '''


def green_to_black(image, rows, cols, channels):
    ''' Write your code here '''
    image[30:400, 100:250, 0:3] = 0
    return image


''' You need to complete following function for task 5 '''


def reduce_brightness(image, rows, cols, channels):
    ''' Write your code here '''
    image[:, :, :] /= 2
    return image


im, shape = generate_image()  # Generate the image
(rows, cols, channels) = shape  # Assign shape values to proper variables

''' Call function for task 1 '''
count_pixels(im.copy(), rows, cols, channels)  # For task 1, this function will be called

''' Call function for task 2 '''
imcopy = red_to_blue(im.copy(), rows, cols, channels)  # This function will be called for task 2. The function should return the output image
write_image('red_blue.jpg', imcopy)  # Store the image returned by the function

''' Call function for task 3 '''
imcopy = remove_blue(im.copy(), rows, cols, channels)  # This function will be called for task 3. The function should return the output image
write_image('blue_removed.jpg', imcopy)  # Store the image returned by the function

''' Call function for task 4 '''
imcopy = green_to_black(im.copy(), rows, cols, channels)  # This function will be called for task 4. The function should return the output # image
write_image('green_black.jpg', imcopy)  # Store the image returned by the function

''' Call function for task 5 '''
imcopy = reduce_brightness(im.copy(), rows, cols, channels)  # This function will be called for task 5. The function should return the output image
write_image('low.jpg', imcopy)  # Store the image returned by the function
