import cv2
import numpy as np

# Load the image
image = cv2.imread("images.jpeg")

# Get image dimensions
h, w = image.shape[:2]

# Define source and destination points for Affine Transformation
src_pts = np.float32([[50, 50], [200, 50], [50, 200]])
dst_pts = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the Affine Transformation matrix
affine_matrix = cv2.getAffineTransform(src_pts, dst_pts)

# Apply the transformation
affine_img = cv2.warpAffine(image, affine_matrix, (w, h))

# Display the result
cv2.imshow("Affine Transformation", affine_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
