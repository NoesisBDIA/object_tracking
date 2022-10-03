# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:46:16 2022

@author: tlambart
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Open a test image
image = cv2.imread("../Data/Capture.png")
# Reorder RGB channels
# NOT WORKING !!!
#image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Separate RGB channels
blue, green, red = image[:,:,0], image[:,:,1], image[:,:,2]

image_red = image.copy()
image_red[:,:,0] = 0
image_red[:,:,1] = 0
image_green = image.copy()
image_green[:,:,0] = 0
image_green[:,:,2] = 0
image_blue = image.copy()
image_blue[:,:,1] = 0
image_blue[:,:,2] = 0
cv2.imwrite('../Data/Capture_red.png', image_red)
cv2.imwrite('../Data/Capture_green.png', image_green)
cv2.imwrite('../Data/Capture_blue.png', image_blue)


# Grayscale iamge
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# create figure
fig = plt.figure(figsize=(20, 14))
  
# setting values to rows and column variables
rows = 3
columns = 2

fig.add_subplot(rows, columns, 1)

# Display the image
plt.imshow(image)
plt.axis('off')
plt.title("Original")

fig.add_subplot(rows, columns, 2)

plt.imshow(image_gray)
plt.axis('off')
plt.title("Gray")
# Write the image into a new file
cv2.imwrite('../Data/Capture_gray.png', image_gray)

fig.add_subplot(rows, columns, 3)

# flip 180° image
im_flip = cv2.flip(image, 0)

plt.imshow(im_flip)
plt.axis('off')
plt.title("Upside Down")

fig.add_subplot(rows, columns, 4)

# rotate image 90° clockwise, same method for other rotations
im_flip2 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

plt.imshow(im_flip2)
plt.axis('off')
plt.title("90° clockwise")

upper, left, lower, right = 150, 150, 400, 400

fig.add_subplot(rows, columns, 5)

crop_image=image.crop((left, upper, right, lower))

plt.imshow(crop_image)
plt.axis('off')
plt.title("cropped image")
