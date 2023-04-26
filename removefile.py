import os

folder_path = 'D:/YOLO/runs/pose/predict/labels'

# Duyệt qua tất cả các file trong folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Kiểm tra file có phải là file văn bản không
        file_path = os.path.join(folder_path, filename)
        # Kiểm tra xem file có trống không
        if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
            os.remove(file_path)
            print(f'Đã xóa file {filename} trống')
        else:
            print(f'File {filename} không trống hoặc không tồn tại')
