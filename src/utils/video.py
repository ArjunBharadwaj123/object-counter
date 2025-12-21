# src/utils/video.py

import cv2
from .config import VIDEO_SOURCE, FRAME_WIDTH, FRAME_HEIGHT


def get_video_stream():
    """
    Opens the video source (webcam or file) and configures resolution.
    Returns a cv2.VideoCapture object.
    """

    cap = cv2.VideoCapture(VIDEO_SOURCE)

    if not cap.isOpened():
        raise ValueError(f"❌ Could not open video source: {VIDEO_SOURCE}")

    # Set resolution (if supported by camera)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    print(f"🎥 Video stream opened: {VIDEO_SOURCE} ({FRAME_WIDTH}x{FRAME_HEIGHT})")

    return cap


def read_frame(cap):
    """
    Reads a single frame from the video stream.
    Returns (success, frame).
    """

    ret, frame = cap.read()

    if not ret:
        print("⚠️ Warning: Failed to read frame from stream.")
        return False, None

    return True, frame


def release_stream(cap):
    """
    Safely releases the video stream and closes all OpenCV windows.
    """

    cap.release()
    cv2.destroyAllWindows()
    print("🔚 Video stream closed.")
