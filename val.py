from ultralytics import YOLO


from ultralytics import YOLO

# Load a model

model = YOLO('D:/YOLO/best.pt')

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category
