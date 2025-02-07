import cv2

# Read the image
image = cv2.imread('images.jpeg')

if image is None:
    print("Error: Image not loaded.")
else:
    # Resize the image to half of its original size (smaller)
    small_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    # Resize the image to twice its original size (bigger)
    big_image = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)

    # Display the images
    cv2.imshow('Original Image', image)
    cv2.imshow('Smaller Image', small_image)
    cv2.imshow('Bigger Image', big_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
