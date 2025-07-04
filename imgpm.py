﻿# pm_data_extraction
import cv2
import os
from datetime import datetime, timedelta

stream_url = 'enter your url here'

save_path = "C:/Users/KIIT0001/Desktop/PM/root/v2/imgpm"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Cannot open stream")
    exit()

# Set the next capture time
next_capture = datetime.now()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        continue

    now = datetime.now()

    # If it's time to capture a new image
    if now >= next_capture:
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(save_path, f'snapshot_{timestamp}.jpg')
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")

        # Set time for next capture
        next_capture = now + timedelta(minutes=1)

cap.release()
