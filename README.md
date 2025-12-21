project:
  name: "Real-Time Object Counter (YOLOv8 + SORT Tracking)"
  description: >
    A real-time object counting system built using YOLOv8, OpenCV, and a lightweight SORT-style tracker.
    The system detects objects in webcam footage, assigns each object a unique ID, and counts them
    without double-counting. This is a clean, modular, and professional computer vision project suitable
    for resumes, portfolios, and interview discussions.

features:
  - "Real-time object detection using YOLOv8"
  - "Object tracking with unique ID assignment"
  - "Accurate unique object counting"
  - "Modular architecture (detector, tracker, counter, utils)"
  - "Easily extendable for line-crossing counting"
  - "Class-specific counting (e.g., count only people)"
  - "Region-based analytics"
  - "FastAPI/React deployment support"

architecture: |
  src/
  │
  ├── counter/
  │   └── object_counter.py        # Unique ID counting logic
  │
  ├── detector/
  │   └── yolo_detector.py         # YOLOv8 detection wrapper
  │
  ├── tracker/
  │   └── object_tracker.py        # Lightweight SORT-style tracker
  │
  ├── utils/
  │   ├── config.py                # Global configuration values
  │   ├── drawing.py               # Drawing bounding boxes, IDs, count
  │   └── video.py                 # Webcam/video input handling
  │
  └── main.py                      # Orchestrates full pipeline

installation:
  steps:
    - "Clone the repository:"
    - |
      git clone <your-repo-url>
      cd object-counter
    - "Install dependencies:"
    - |
      pip install -r requirements.txt
    - "Download YOLOv8 model weights:"
    - |
      yolo predict model=yolov8n.pt source=0
    - "Move yolov8n.pt into the /models directory."

running:
  command: |
    cd src
    python main.py
  quit_instruction: "Press 'q' to quit the application."

pipeline_description:
  - step: "YOLO Detection"
    detail: "Each frame is passed into a pretrained YOLOv8 model, producing bounding boxes and class predictions."
  - step: "Object Tracking"
    detail: "A lightweight SORT-style tracker assigns consistent IDs to objects across frames."
  - step: "Unique Counting"
    detail: "The counter increments only when a new ID is observed."
  - step: "Drawing"
    detail: "OpenCV overlays bounding boxes, object IDs, and total count."

technologies_used:
  - "Python 3.9+"
  - "YOLOv8 (Ultralytics)"
  - "OpenCV"
  - "NumPy"
  - "SORT-inspired object tracking"

future_improvements:
  - "Line-crossing counting with direction"
  - "Class-specific counting (people-only, car-only, etc.)"
  - "Region-based analytics"
  - "Logging count data to CSV or database"
  - "FastAPI backend + React dashboard"
  - "Docker container for deployment"
  - "Performance optimization using GPU acceleration"

example_output:
  placeholder: "Add screenshot or GIF here (images/sample.png)"

author:
  name: "Arjun Bharadwaj"
  title: "Computer Science @ University of Maryland"
  concentration: "Machine Learning Concentration"

license:
  type: "MIT"
  recommended: true
