import cv2
import numpy as np

# Load the image
img = cv2.imread('antony.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges using Canny method
edges = cv2.Canny(gray, 150, 300)

# Highlight the edges on the original image
img[edges == 255] = (255, 0, 0)  # Color the edges in red

# Display the image with edges highlighted
cv2.imshow('Canny Edges', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
