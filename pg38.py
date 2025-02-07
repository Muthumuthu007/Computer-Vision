import cv2

def count_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

    print(f"Number of faces detected: {len(faces)}")

    cv2.imshow("Faces Detected", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
count_faces("images.jpeg")
