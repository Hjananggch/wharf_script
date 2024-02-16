import os

# 图片路径和标签路径
image_dir = r"C:\Users\H2250\Desktop\DATA\temporary\no\imgs"
label_dir = r"C:\Users\H2250\Desktop\DATA\temporary\no\label"

# 获取图片和标签文件列表
image_files = os.listdir(image_dir)
label_files = os.listdir(label_dir)

# 遍历标签目录
for label_file in label_files:
    # 排除classes.txt文件
    if label_file == 'classes.txt':
        continue
    # 构建对应的图片文件名
    image_file = os.path.splitext(label_file)[0] + ".jpg"

    # 构建完整的图片路径
    image_path = os.path.join(image_dir, image_file)

    # 检查对应的图片文件是否存在
    if image_file not in image_files or not os.path.exists(image_path):
        # 构建完整的标签路径
        label_path = os.path.join(label_dir, label_file)

        # 删除标签文件
        os.remove(label_path)

        print(f"删除标签: {label_file}")
