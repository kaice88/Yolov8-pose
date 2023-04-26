from ultralytics import YOLO
import os

# Load a model
# load an official model
# model = YOLO('C:/Users/Lenovo/Desktop/Yolov8/runs/pose/train14/weights/best.pt')
model = YOLO('D:/YOLO/runs/pose/train7/weights/best.pt')

# files_path = ["C:/Users/Lenovo/Desktop/DT/111/CR_1_0011.jpg", "C:/Users/Lenovo/Desktop/DT/111/CR_1_0014.jpg",
#               "C:/Users/Lenovo/Dytesktop/DT/111/CR_1_0012.jpg", "C:/Users/Lenovo/Desktop/DT/111/CR_1_0013.jpg"]
# Specify the path to the parent directory containing the subfolders
parent_dir = 'C:/Users/Lenovo/Desktop/DT'
folder_name = ['010', '011', '110', '111', '120', '121', '130', '131']
# Create an empty list to store the file paths
file_paths = []

# Loop through each subfolder specified in the arr list
for subfolder in folder_name:
    # Construct the full path to the subfolder
    subfolder_path = os.path.join(parent_dir, subfolder)
    # Loop through each file in the subfolder
    for filename in os.listdir(subfolder_path):
        # Check if the file is a .jpg file
        if filename.endswith('.jpg'):
            # Construct the full path to the file and add it to the list
            file_path = os.path.join(subfolder_path, filename)
            file_paths.append(file_path)


for i in file_paths:
    model.predict(i, save=True, save_txt=True, conf=0.6)


# Predict with the model
# model.predict("C:/Users/Lenovo/Desktop/DT/111/CR_1_0002.jpg",
#               save=True, save_txt=True, conf=0.5)
# dir = "C:/Users/Lenovo/Desktop/DT/110"
# # Get a list of all file names in Folder A
# file_names = os.listdir(dir)

# # Create a list of file paths by joining the file names with the folder path
# file_paths = [os.path.join(dir, file_name) for file_name in file_names]

# arr = ["C:/Users/Lenovo/Desktop/DT/110/WL_1_0009.jpg", "C:/Users/Lenovo/Desktop/DT/110/WL_1_0002.jpg", "C:/Users/Lenovo/Desktop/DT/110/WL_1_0003.jpg",
#        "C:/Users/Lenovo/Desktop/DT/110/WL_1_0010.jpg", "C:/Users/Lenovo/Desktop/DT/110/WL_1_0005.jpg", "C:/Users/Lenovo/Desktop/DT/110/WL_1_0006.jpg"]

# rs = model.predict("C:/Users/Lenovo/Desktop/DT/110/110_27.jpg",
#                    save=True, save_txt=True, conf=0.5)
# print(rs)
