import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load and preprocess the image
sample_image = cv2.imread('antony.jpg')
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (256, 256))

# Create a figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

# Image Thresholding
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)
axes[0, 0].imshow(thresh, cmap='gray')
axes[0, 0].set_title('Image Thresholding')
axes[0, 0].axis('off')

# Detecting Edges
edges = cv2.dilate(cv2.Canny(thresh, 0, 255), None)
axes[0, 1].imshow(edges, cmap='gray')
axes[0, 1].set_title('Detecting Edges')
axes[0, 1].axis('off')

# Detecting Contours To Create Mask
cnt = sorted(cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2], key=cv2.contourArea)[-1]
mask = np.zeros((256, 256), np.uint8)
masked = cv2.drawContours(mask, [cnt], -1, 255, -1)
axes[1, 0].imshow(masked, cmap='gray')
axes[1, 0].set_title('Detecting Contours To Create Mask')
axes[1, 0].axis('off')

# Segmenting Region
dst = cv2.bitwise_and(img, img, mask=mask)
segmented = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
axes[1, 1].imshow(segmented)
axes[1, 1].set_title('Segmenting Region')
axes[1, 1].axis('off')

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
