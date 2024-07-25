import cv2
import os

# Read the input image
img = cv2.imread('antony.jpg')

# Save the image as a lossless PNG
cv2.imwrite('lossless_compressed_image.png', img)

# Set JPEG quality (0-100, higher means better quality but larger file size)
jpeg_quality = 90

# Save the image as a lossy JPEG
cv2.imwrite('lossy_compressed_image.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])

# Get the file sizes of the original, lossless, and lossy compressed images
original_size = os.path.getsize('antony.jpg')
lossless_size = os.path.getsize('lossless_compressed_image.png')
lossy_size = os.path.getsize('lossy_compressed_image.jpg')

# Print the file sizes
print(f'Original image size: {original_size} bytes')
print(f'Lossless compressed image size: {lossless_size} bytes')
print(f'Lossy compressed image size: {lossy_size} bytes')

# Read the compressed images
lossless_img = cv2.imread('lossless_compressed_image.png')
lossy_img = cv2.imread('lossy_compressed_image.jpg')

# Display the original and compressed images
cv2.imshow('Original Image', img)
cv2.imshow('Lossless Compressed Image', lossless_img)
cv2.imshow('Lossy Compressed Image', lossy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
