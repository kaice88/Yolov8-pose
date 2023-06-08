from ultralytics import YOLO
import os


model = YOLO('D:/YOLO/best.pt')

# Specify the path to the parent directory containing the subfolders
# parent_dir = 'C:/Users/Lenovo/Desktop/Processed'
folder_name = ['Wrong_Head', 'Correct_Head']
#  Create an empty list to store the file paths
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
    model.predict(i, save=True, save_txt=True, conf=0.01)
