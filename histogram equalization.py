import cv2
import numpy as np

image = cv2.imread('images.jpeg')  
if image is None:
    print("Error: Could not read the image.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    equalized_image = cv2.equalizeHist(gray_image)

    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])  
    color_equalized_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

    cv2.imwrite('equalized_gray_image.jpg', equalized_image)
    cv2.imwrite('color_equalized_image.jpg', color_equalized_image)

    cv2.imshow('Original Image', image)
    cv2.imshow('Equalized Grayscale Image', equalized_image)
    cv2.imshow('Equalized Color Image', color_equalized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
