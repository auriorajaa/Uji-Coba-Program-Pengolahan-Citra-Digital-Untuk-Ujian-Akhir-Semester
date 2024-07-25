import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the image
sample_image = cv2.imread('antony.jpg')
img = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

# Reshape the image to a 2D array of pixels
twoDimage = img.reshape((-1, 3))
twoDimage = np.float32(twoDimage)

# Create a figure with 4 subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

# Perform K-Means clustering with different K values
for i, k in enumerate([3, 4, 5, 6]):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    attempts = 10
    ret, label, center = cv2.kmeans(twoDimage, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    result_image = res.reshape((img.shape))
    
    # Plot the results
    row = i // 2
    col = i % 2
    axs[row, col].imshow(result_image)
    axs[row, col].set_title(f'K={k}')
    axs[row, col].axis('off')

# Show the figure
plt.show()
