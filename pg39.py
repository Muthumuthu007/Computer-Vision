import cv2

def play_video_reverse_slow(video_path):
    cap = cv2.VideoCapture(video_path)

    frames = []
    fps = cap.get(cv2.CAP_PROP_FPS)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)
        if cv2.waitKey(int(1000 / (fps / 2))) & 0xFF == ord('q'):  # Slow motion (double delay)
            break

    cv2.destroyAllWindows()

# Example usage
play_video_reverse_slow("video.mp4")
