# src/utils/config.py

# -----------------------------
# YOLO MODEL CONFIG
# -----------------------------
YOLO_MODEL_PATH = "models/yolov8n.pt"   # Path to YOLOv8 model weights
CONFIDENCE_THRESHOLD = 0.4              # Ignores predictions below 40% confidence
IOU_THRESHOLD = 0.5                     # IOU threshold for non-max suppression (overlap removal)

# -----------------------------
# TRACKER CONFIG
# -----------------------------
MAX_AGE = 30        # How many frames a tracked object can disappear before removed
MIN_HITS = 5        # Minimum detections before a track is considered valid

# -----------------------------
# COUNTING CONFIG
# -----------------------------
COUNTING_MODE = "unique"   # "unique" or "line_crossing"
LINE_POSITION = 300        # y-position of line crossing count (if enabled)

# -----------------------------
# DISPLAY CONFIG
# -----------------------------
FONT_SCALE = 0.7
FONT_THICKNESS = 2
BOX_THICKNESS = 2

# -----------------------------
# VIDEO CONFIG
# -----------------------------
VIDEO_SOURCE = "videos/traffic.mp4"
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
