import cv2

# Read the input RGB image (which is read as BGR by OpenCV)
bgr_img = cv2.imread('antony.jpg')

# Convert the BGR image to HSV format
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

# Save the HSV image
cv2.imwrite('hsv_image.jpg', hsv_img)

# Display the HSV image
cv2.imshow('HSV image', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
