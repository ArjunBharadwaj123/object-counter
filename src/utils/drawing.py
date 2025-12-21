# src/utils/drawing.py

import cv2
from .config import FONT_SCALE, FONT_THICKNESS, BOX_THICKNESS, LINE_POSITION


def draw_boxes(frame, tracked_objects):
    """
    Draw bounding boxes and object IDs on the frame.
    tracked_objects format:
    [id, x1, y1, x2, y2, conf, cls]
    """
    for obj in tracked_objects:
        obj_id, x1, y1, x2, y2, conf, cls = obj

        # Draw box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), BOX_THICKNESS)

        # Draw label text: "ID 3"
        label = f"ID {obj_id}"
        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            FONT_SCALE,
            (255, 255, 255),
            FONT_THICKNESS
        )

    return frame


def draw_count(frame, count):
    """
    Draws the total object count in the top-left corner.
    """
    text = f"Count: {count}"
    cv2.putText(
        frame,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE + 0.3,
        (0, 255, 255),
        FONT_THICKNESS + 1
    )

    return frame


def draw_counting_line(frame):
    """
    Optional: Draws a horizontal line across the frame for line-crossing logic.
    """
    cv2.line(frame, (0, LINE_POSITION), (frame.shape[1], LINE_POSITION),
             (0, 0, 255), 2)

    return frame
