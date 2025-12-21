# src/main.py

import cv2
from src.detector.yolo_detector import YOLODetector
from src.tracker.object_tracker import ObjectTracker
from src.counter.object_counter import ObjectCounter
from src.utils.video import get_video_stream, read_frame, release_stream
from src.utils.drawing import draw_boxes, draw_count


def main():

    # ----------------------------------------
    # 1. Initialize components
    # ----------------------------------------
    detector = YOLODetector()
    tracker = ObjectTracker(max_lost=10)
    counter = ObjectCounter()

    cap = get_video_stream()

    print("🚀 Starting Real-Time Object Counter... Press 'q' to quit.")

    # ----------------------------------------
    # 2. Main loop: runs once per frame
    # ----------------------------------------
    while True:

        # Read frame from webcam
        success, frame = read_frame(cap)
        if not success:
            break

        # 2A. YOLO detection
        detections = detector.detect(frame)

        # 2B. Tracking of detections
        tracked_objects = tracker.update(detections)

        # 2C. Counting logic
        total_count = counter.update(tracked_objects)

        # 2D. Draw bounding boxes + IDs
        frame = draw_boxes(frame, tracked_objects)

        # 2E. Draw count on screen
        frame = draw_count(frame, total_count)

        # 2F. Display the frame
        cv2.imshow("Real-Time Object Counter", frame)

        # Quit when pressing 'q'
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # ----------------------------------------
    # 3. Clean up
    # ----------------------------------------
    release_stream(cap)


if __name__ == "__main__":
    main()
