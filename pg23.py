import cv2
import numpy as np

# Load the image
image = cv2.imread("images.jpeg", cv2.IMREAD_GRAYSCALE)

# Define kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply Top-Hat transformation
tophat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Image", tophat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
