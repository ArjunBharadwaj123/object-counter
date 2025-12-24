# 🚀 Real-Time Object Counter  
## YOLOv8 + SORT Tracking

> A **real-time object counting system** built using **YOLOv8**, **OpenCV**, and a lightweight **SORT-style tracker**.  
> The system detects objects in live video or webcam footage, assigns each object a **unique ID**, and counts them **without double-counting**.

This project is designed with a **clean, modular codebase** and is suitable for **resumes, portfolios, and technical interviews**.

---

## ✨ Features

* Real-time object detection using **YOLOv8**
* Object tracking with **unique ID assignment**
* Accurate **unique object counting**
* Modular and extensible design
* Easily extendable for **line-crossing counting**
* Class-specific counting (e.g., *people-only*)
* Region-based analytics
* Ready for **FastAPI + React** deployment

---

## 🛠️ Installation

### 1. Clone the repository
git clone https://github.com/ArjunBharadwaj123/object-counter.git
cd object-counter


### 2. Install dependencies
pip install -r requirements.txt


### 3. Download YOLOv8 model weights
yolo predict model=yolov8n.pt source=0



### 4. Move the model file

Move `yolov8n.pt` into the `/models` directory.

---

## ▶️ Running the Project

python -m src.main


**Controls**

* Press `q` to quit the application.

---

## 🔄 Processing Pipeline

### 1. YOLO Detection
Each video frame is passed into a pretrained YOLOv8 model, producing bounding boxes and class predictions.

### 2. Object Tracking
A lightweight SORT-style tracker assigns **consistent IDs** to objects across frames.

### 3. Unique Counting
The counter increments **only when a new object ID appears**, preventing double-counting.

### 4. Drawing & Visualization
OpenCV overlays bounding boxes, object IDs, and the total object count on each frame.

---

## 🧠 Technologies Used

* Python 3.9+
* YOLOv8 (Ultralytics)
* OpenCV
* NumPy
* SORT-inspired object tracking

---

## 🚧 Future Improvements

1. Line-crossing counting with direction detection
2. Class-specific counting (people-only, vehicle-only, etc.)
3. Region-based analytics
4. Logging count data to CSV or database
5. FastAPI backend with React dashboard
6. Docker container for deployment
7. GPU acceleration for improved performance

---

## 🖼️ Example Output

![Sample output](images/output.png)

---

## 👤 Author

**Arjun Bharadwaj**  
Computer Science @ University of Maryland  
Machine Learning Concentration

---

## 📄 License

This project is licensed under the **MIT License**.
