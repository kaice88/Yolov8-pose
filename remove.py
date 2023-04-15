
import os


# Set the paths for the folders
folder_a_path = "C:/Users/Lenovo/Desktop/Yolov8/datasets/custom_datasets2/images/train"
folder_b_path = "C:/Users/Lenovo/Desktop/DT/train1"

# Get the list of files in folder A with extension .py
folder_a_files = [f for f in os.listdir(folder_a_path) if f.endswith('.jpg')]

# Get the list of files in folder B with extension .txt
folder_b_files = [f for f in os.listdir(folder_b_path) if f.endswith('.jpg')]

# Get the list of file names without extensions in folder A
folder_a_filenames = [os.path.splitext(f)[0] for f in folder_a_files]

# Get the list of file names without extensions in folder B
folder_b_filenames = [os.path.splitext(f)[0] for f in folder_b_files]

# Get the list of file names in folder A that are not in folder B
files_to_delete = [
    f + '.jpg' for f in folder_b_filenames if f not in folder_a_filenames]

# Delete the files in folder B that match the files to delete
for f in files_to_delete:
    file_path = os.path.join(folder_b_path, f)
    if os.path.isfile(file_path):
        os.remove(file_path)
