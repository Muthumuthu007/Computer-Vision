import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    image = cv2.imread('images.jpeg')

    if image is None:
        print("Error: Could not read the image.")
        return

    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    for channel, color, name in zip(channels, colors, channel_names):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(hist, color=color, label=f'{name} Channel')

    plt.legend()

    plt.show()

analyze_histogram('images.jpeg')  
