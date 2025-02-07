import cv2
import numpy as np

# Load the original image and watermark
image = cv2.imread("images.jpeg")
watermark = cv2.imread("watermark.png", cv2.IMREAD_UNCHANGED)

# Resize watermark to fit on the image
wm_h, wm_w = watermark.shape[:2]
img_h, img_w = image.shape[:2]
scale = 0.3
watermark = cv2.resize(watermark, (int(img_w * scale), int(img_h * scale)))

# Define watermark position (bottom right corner)
wm_h, wm_w = watermark.shape[:2]
x_offset, y_offset = img_w - wm_w, img_h - wm_h

# Blend watermark into the original image
overlay = image.copy()
overlay[y_offset:y_offset + wm_h, x_offset:x_offset + wm_w] = watermark

# Display the watermarked image
cv2.imshow("Watermarked Image", overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()
