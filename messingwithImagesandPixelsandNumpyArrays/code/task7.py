import cv2
import numpy as np

im = cv2.imread('uh.png')  # Reads image from current folder
height, width, channels = im.shape  # Gets the shape of the image
print('Original Image Dimensions:', im.shape)
maxpooled = np.empty(shape=(height // 4, width // 4, 3))  # Initializing an empty array with half the dimensions of the input image

'''Write your code here'''


def maxVal(im, s1, s2, r, c, ch):
    arr = []
    for r1 in range(s1, r):
        for c1 in range(s2, c):
            arr.append(im[r1][c1][ch])
    return max(arr)


row = 0
col = 0
for x in range(channels):
    for y in range(0, height, 4):
        for z in range(0, width, 4):
            # with max pooling
            maxpooled[row][col][x] = maxVal(im, y, z, y+4, z+4, x)
            # without max pooling
            # maxpooled[row][col][x] = im[y][z][x]
            if col < 255:
                col += 1
        col = 0
        if row < 255:
            row += 1
    row = 0
    col = 0

print('Max-pooled Image Dimensions:', maxpooled.shape)  # Prints dimensions of the maxpooled image
cv2.imwrite('maxpooled.png', maxpooled)  # Stores image
