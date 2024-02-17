import os
import random

# 设置图片文件夹和文本文件夹的路径
image_folder = r"C:\Users\H2250\Desktop\1\img\IMG"
text_folder = r"C:\Users\H2250\Desktop\1\img\LABEL"

# 获取图片文件夹中所有文件的列表
images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# 计算要保留的图片数量（40%）
num_to_keep = int(len(images) * 0.4)

# 随机选择要保留的图片
images_to_keep = random.sample(images, num_to_keep)

# 删除未被选中保留的图片
for image in images:
    if image not in images_to_keep:
        image_path = os.path.join(image_folder, image)
        os.remove(image_path)  # 删除图片文件

        # 构建对应的文本文件名和路径
        txt_filename = os.path.splitext(image)[0] + '.txt'
        txt_path = os.path.join(text_folder, txt_filename)

        # 如果对应的文本文件存在，则删除
        if os.path.exists(txt_path):
            os.remove(txt_path)

print("finished!")
