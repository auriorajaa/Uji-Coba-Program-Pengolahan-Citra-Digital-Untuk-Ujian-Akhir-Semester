import cv2 as cv
import numpy as np

# Read the input image in grayscale
img = cv.imread('antony.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File could not be read, check with os.path.exists()"

# Define a 5x5 kernel of ones
kernel = np.ones((5,5),np.uint8)

# Perform various morphological operations
erosion = cv.erode(img, kernel, iterations=1)           # Erosion
dilation = cv.dilate(img, kernel, iterations=1)         # Dilation
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)   # Opening
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # Closing
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel) # Morphological Gradient
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)     # Top Hat
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel) # Black Hat

# Create different types of kernels
rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))      # Rectangular Kernel
ellipse_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5)) # Elliptical Kernel
cross_kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))     # Cross-shaped Kernel

# Display the results
cv.imshow("Original", img)
cv.imshow("Erosion", erosion)
cv.imshow("Dilation", dilation)
cv.imshow("Opening", opening)
cv.imshow("Closing", closing)
cv.imshow("Gradient", gradient)
cv.imshow("Top Hat", tophat)
cv.imshow("Black Hat", blackhat)

# Print the kernels
print("Rectangular Kernel:")
print(rect_kernel)
print("Elliptical Kernel:")
print(ellipse_kernel)
print("Cross-shaped Kernel:")
print(cross_kernel)

cv.waitKey(0)
cv.destroyAllWindows()
