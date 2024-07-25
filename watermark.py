# import required libraries
import cv2

# Read the image on which we are going to apply watermark
img = cv2.imread("antony.jpg")

# Read the watermark image
wm = cv2.imread("wm-2.jpg")

# height and width of the watermark image
h_wm, w_wm = wm.shape[:2]

# height and width of the image
h_img, w_img = img.shape[:2]

# calculate coordinates of center of image
center_x = int(w_img / 2)
center_y = int(h_img / 2)

# calculate region of interest (ROI) from top, bottom, right, and left
top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

# add watermark to the image
roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result

# display watermarked image
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
