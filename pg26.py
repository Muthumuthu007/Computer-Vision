import cv2

def reverse_video(input_path, output_path):
    # Open the video file
    cap = cv2.VideoCapture(input_path)
    frames = []

    # Read all frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Reverse the frames
    frames.reverse()

    # Get video properties
    height, width, channels = frames[0].shape
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Write reversed frames
    for frame in frames:
        out.write(frame)

    out.release()
    print("Reversed video saved as", output_path)

# Example usage
reverse_video("video.mp4", "reversed_video.avi")
