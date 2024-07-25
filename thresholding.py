from __future__ import print_function
import cv2 as cv
import argparse

# Constants
max_value = 255
max_type = 4
max_binary_value = 255
trackbar_type = 'Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted'
trackbar_value = 'Value'
window_name = 'Threshold Demo'

# Function for thresholding demo
def Threshold_Demo(val):
    # Get the current positions of the trackbars
    threshold_type = cv.getTrackbarPos(trackbar_type, window_name)
    threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
    
    # Apply the thresholding
    _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, threshold_type)
    cv.imshow(window_name, dst)

# Argument parser to get input image
parser = argparse.ArgumentParser(description='Code for Basic Thresholding Operations tutorial.')
parser.add_argument('--input', help='Path to input image.', default='antony.jpg')
args = parser.parse_args()

# Read the input image
src = cv.imread(args.input)
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)

# Convert the image to gray
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Create a window and trackbars
cv.namedWindow(window_name)
cv.createTrackbar(trackbar_type, window_name, 3, max_type, Threshold_Demo)
cv.createTrackbar(trackbar_value, window_name, 0, max_value, Threshold_Demo)

# Initialize
Threshold_Demo(0)

# Wait until the user finishes the program
cv.waitKey()
