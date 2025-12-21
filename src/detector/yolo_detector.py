# src/detector/yolo_detector.py

from ultralytics import YOLO
import numpy as np
from ..utils.config import YOLO_MODEL_PATH, CONFIDENCE_THRESHOLD


class YOLODetector:
    """
    Loads a YOLOv8 model and performs object detection on each frame.
    """

    def __init__(self):
        # Load the YOLOv8 model from the provided path
        self.model = YOLO(YOLO_MODEL_PATH)
        print(f"🧠 Loaded YOLO model from: {YOLO_MODEL_PATH}")

    def detect(self, frame):
        """
        Runs YOLO inference on a frame.
        Returns a list of detections, each formatted as:
        [x1, y1, x2, y2, confidence, class_id]
        """

        # Run YOLO inference (returns Results object)
        results = self.model(frame, verbose=False)

        detections = []

        # Loop through the results (YOLO may return batch results)
        for result in results:
            boxes = result.boxes  # YOLO bounding boxes

            for box in boxes:
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                # Filter out low confidence detections
                if conf < CONFIDENCE_THRESHOLD:
                    continue

                # YOLO gives x1, y1, x2, y2; convert to ints
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append([x1, y1, x2, y2, conf, cls])

        return detections
