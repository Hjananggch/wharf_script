'''
Author: AI_Widsom
date: 2024-02-15
Description: 从视频文件中提取图像
'''
import cv2
import os

# 视频文件所在的目录
video_dir = 'path/to/your/video/directory'
# 保存图像的目录
image_dir = 'path/to/your/image/directory'
# 确保保存图像的目录存在
os.makedirs(image_dir, exist_ok=True)

# 遍历视频目录下的所有文件
for filename in os.listdir(video_dir):
    if filename.endswith(('.mp4', '.avi', '.mov')):  # 检查文件扩展名
        video_path = os.path.join(video_dir, filename)
        cap = cv2.VideoCapture(video_path)

        frame_count = 0
        num = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 每隔10帧保存一次图像
            if frame_count % 10 == 0:
                image_path = os.path.join(image_dir, f'{filename}_frame{frame_count}.jpg')
                cv2.imwrite(image_path, frame)
                print(f'Saved {num}')
                num += 1

            frame_count += 1

        cap.release()

print('Completed!')

