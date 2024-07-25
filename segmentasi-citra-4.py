import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import cv2

# Load and preprocess the image
sample_image = cv2.imread('antony.jpg')
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

# Define the color mask
low = np.array([0, 0, 0])
high = np.array([100, 255, 100])
mask = cv2.inRange(img, low, high)

# Apply color masking
result = cv2.bitwise_and(img, img, mask=mask)

# Create a figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot the original image
ax1.imshow(img)
ax1.set_title('Original Image')
ax1.axis('off')

# Plot the applied mask
ax2.imshow(mask, cmap='gray')
ax2.set_title('Applied Mask')
ax2.axis('off')

# Plot the color-masked image
ax3.imshow(result)
ax3.set_title('Color-Masked Image')
ax3.axis('off')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
