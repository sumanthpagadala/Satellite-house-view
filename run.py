from ultralytics import YOLO
import os

model = YOLO("best.pt")

image_directory = "/Users/sumanthpagadala/Desktop/House_Satt_Dataset/YOLODataset/images/val"

image_files = [os.path.join(image_directory, file) for file in os.listdir(image_directory) if file.endswith(('.png', '.jpg', '.jpeg'))]

# Run prediction on each image
for image_path in image_files:
    model.predict(
        source=image_path,
        show=True,
        save=True,
        hide_labels=False,
        hide_conf=False,
        box=False,
        conf=0.5,
        save_crop=False
    )
