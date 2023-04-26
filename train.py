from ultralytics import YOLO


# load a pretrained model (recommended for training)
model = YOLO('D:/YOLO/runs/pose/train7/weights/best.pt')


# Train the model
model.train(data='custom_datasets.yaml', epochs=20)
