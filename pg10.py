import cv2

# Read the image
image = cv2.imread('images.jpeg')

if image is None:
    print("Error: Image not loaded.")
else:
    # Rotate the image 90 degrees clockwise along the y-axis
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
