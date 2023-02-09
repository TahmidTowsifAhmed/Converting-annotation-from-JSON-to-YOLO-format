import os

def find_images_without_annotations(images_folder, annotations_folder):
    images = [f.split('.')[0] for f in os.listdir(images_folder)]
    annotations = [f.split('.')[0] for f in os.listdir(annotations_folder)]
    missing_annotations = [img for img in images if img not in annotations]
    return missing_annotations

images_folder = "C:\\Git\Traffic-Sign-Yolov5-Mapillary\\dataset\\organized_mapilary_dataset\\partially\\img"
annotations_folder = "C:\\Git\Traffic-Sign-Yolov5-Mapillary\\dataset\\yolov7_dataset_partially"
missing_annotations = find_images_without_annotations(images_folder, annotations_folder)
print("Images without annotations: ", missing_annotations)