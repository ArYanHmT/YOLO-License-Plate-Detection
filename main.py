from ultralytics import YOLO
from pathlib import Path

model = YOLO("models/best.pt")

image_folder = Path("images")

image_files = (
    list(image_folder.glob("*.jpg")) +
    list(image_folder.glob("*.png")) +
    list(image_folder.glob("*.jpeg"))
)

for image_path in image_files:

    print(f"\nProcessing: {image_path.name}")

    results = model.predict(
    source=str(image_path),
    conf=0.60,
    save=True,
    project="output",
    name="detections",
    exist_ok=True
)

    for result in results:
        if result.boxes is None or len(result.boxes) == 0:
            print("No license plate detected!")
            continue

        for box in result.boxes:
            confidence = float(box.conf[0])
            print(f"License Plate: {confidence:.2%}")

print("\nAll images processed!")