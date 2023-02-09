import json
import os

path = 'C:\\Git\\Traffic-Sign-Yolov5-Mapillary\\dataset\\organized_mapilary_dataset\\fully\\annotations'


print(os.listdir(path))
for image_file in os.listdir(path):
    print(image_file)
    with open(os.path.join(path,image_file), "r") as f: #has only one annotation
        annotations = json.load(f)
    print (annotations)
    
    if not os.path.exists ("yolov7_dataset"):
        os.makedirs ("yolov7_dataset")
    
    for obj in annotations["objects"]:
        print(obj["key"])
        print(obj["label"])
        class_label = obj["label"]
        x = 0         
        complementary = "complementary"
        if complementary in class_label:
            x = 0
        information = "information"
        if information in class_label:
            x = 1
        regulatory = "regulatory"
        if regulatory in class_label:
            x = 2
        warning = "warning"
        if warning in class_label:
            x = 3
        other = "other-sign"
        if other in class_label:
            x = 4
        bbox = obj["bbox"]
        xcenter = ((bbox["xmin"]) + (bbox["xmax"])) / 2 / (annotations["width"])
        ycenter = ((bbox["ymin"]) + (bbox["ymax"])) / 2 / (annotations["height"])
        bbox_width = ((bbox["xmax"]) - (bbox["xmin"])) / (annotations["width"])
        bbox_height = ((bbox["ymax"]) - (bbox["ymin"])) / (annotations["height"])
        # Create a new file to store the YOLOv7 annotation
        yolov7_annotation_file = open(f"yolov7_dataset/{os.path.splitext(image_file)[0]}.txt", "a")
        print (yolov7_annotation_file)
        # Write the annotation to the file
        yolov7_annotation_file.write(f"{x} {xcenter} {ycenter} {bbox_width} {bbox_height}\n")
        # Close the annotation file
        yolov7_annotation_file.close()