import os
import xml.etree.ElementTree as ET


def xml_to_yolo(xml_path, output_folder):
    # Parse XML content
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Extract image dimensions
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)

    # Initialize a list to hold YOLO format lines
    yolo_lines = []

    # Iterate through each object in the XML
    for obj in root.iter('object'):
        # Extract object class (assuming 'fire' class is indexed as 0)
        obj_class = 0  # Placeholder for actual class index if multiple classes exist

        # Extract bounding box coordinates
        xmin = int(obj.find('bndbox/xmin').text)
        ymin = int(obj.find('bndbox/ymin').text)
        xmax = int(obj.find('bndbox/xmax').text)
        ymax = int(obj.find('bndbox/ymax').text)

        # Calculate YOLO format values
        x_center = ((xmin + xmax) / 2) / width
        y_center = ((ymin + ymax) / 2) / height
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        # Create YOLO format line and add to the list
        yolo_line = f"{obj_class} {x_center} {y_center} {bbox_width} {bbox_height}"
        yolo_lines.append(yolo_line)

    # Construct output filename and save YOLO formatted annotations
    base_filename = os.path.splitext(os.path.basename(xml_path))[0]
    output_path = os.path.join(output_folder, f"{base_filename}.txt")

    with open(output_path, 'w') as file:
        file.write('\n'.join(yolo_lines))


def convert_folder(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all XML files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.xml'):
            xml_path = os.path.join(input_folder, filename)
            xml_to_yolo(xml_path, output_folder)
            print(f"Converted {filename} to YOLO format.")


# Specify your input and output folders here
input_folder = r'C:\Users\H2250\Desktop\fire\fire_smoke\fire_smoke\annotations'
output_folder = r'C:\Users\H2250\Desktop\fire\fire_smoke\fire_smoke\txt'

convert_folder(input_folder, output_folder)

