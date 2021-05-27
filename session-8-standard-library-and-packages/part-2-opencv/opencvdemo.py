# Import libraries
import cv2 as cv
import numpy as np

# Read in our image
src_img = cv.imread('bruhmoment.jpeg')

# Sharpen image
img = src_img.copy()
for i in range(10):
  frame = cv.GaussianBlur(img, (3,3), 13)
  img = cv.addWeighted(img, 1.5, frame, -0.5, 0)

# Increased the red contrast
contrast = 2.2
brightness = 50
b, g, r = cv.split(img)
r = r*contrast + brightness
r = r.astype(np.uint8)
r = np.clip(r, 0, 255)
img = cv.merge((b, g, r))

# Bold the edges
edges = cv.Canny(src_img, 50, 50)
red_edges = np.zeros(img.shape)
red_edges[:, :, 2] = edges
red_edges = red_edges.astype(np.uint8)
img = cv.addWeighted(img, 0.5, red_edges, 0.5, 0)

# Increase overall brightness
img = img*1.5 + 50
img = img.astype(np.uint8)

# Display our creation
cv.imshow('img sharp', img)
cv.waitKey(0)
cv.destroyAllWindows()
