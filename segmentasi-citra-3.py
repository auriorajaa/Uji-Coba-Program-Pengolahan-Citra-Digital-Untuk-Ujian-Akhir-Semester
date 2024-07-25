import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import cv2

# Load and preprocess the image
sample_image = cv2.imread('antony.jpg')
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

# Create a figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original image
axes[0].imshow(img)
axes[0].set_title('Original Image')
axes[0].axis('off')

# Thresholded image
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = threshold_otsu(img_gray)
img_otsu = img_gray < thresh
axes[1].imshow(img_otsu, cmap='gray')
axes[1].set_title('Thresholded Image')
axes[1].axis('off')

# Filtered image
def filter_image(image, mask):
    r = image[:, :, 0] * mask
    g = image[:, :, 1] * mask
    b = image[:, :, 2] * mask
    return np.dstack([r, g, b])

filtered = filter_image(img, img_otsu)
axes[2].imshow(filtered)
axes[2].set_title('Filtered Image')
axes[2].axis('off')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
