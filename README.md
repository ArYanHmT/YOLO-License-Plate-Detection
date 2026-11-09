YOLO License Plate Detection

A simple vehicle license plate detection project using YOLOv8 and Python.

Overview

This project uses a pre-trained YOLOv8 model to detect vehicle license plates in images.

It identifies license plates, draws bounding boxes around detected regions, and saves the processed images.

Features

- License plate detection using YOLOv8
- Multiple image processing
- Confidence score filtering
- Automatic image saving
- Simple and easy-to-use Python code

Technologies

- Python
- YOLOv8
- Ultralytics
- OpenCV

Project Structure

YOLO-License-Plate-Detection/
├── models/
│   └── best.pt
├── images/
├── output/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

Installation

Install the required libraries:

pip install -r requirements.txt

Usage

1. Place your vehicle images inside the "images" folder.
2. Run the following command:

python main.py

3. Find the detected license plates in the "output/detections" folder.

Confidence Threshold

The model uses a confidence threshold of "0.60" to filter low-confidence detections.

License

See the original model repository for model weight licensing and attribution.

## Credits

Pre-trained YOLOv8 license plate detection model:

https://huggingface.co/Koushim/yolov8-license-plate-detection

The original model is credited to its author.