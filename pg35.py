import cv2

def add_text(image_path, text):
    img = cv2.imread(image_path)

    # Define text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (50, 50)
    font_scale = 1
    font_color = (0, 0, 255)
    thickness = 2

    # Put text on image
    cv2.putText(img, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

    # Display image
    cv2.imshow("Text on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
add_text("images.jpeg", "Hello, OpenCV!")
