import os

# define the directory paths where the images and annotations are located
images = "path\to\images"
annotations = "path\to\labels"

def find_images_without_annotations(images, annotations):
    images = [f.split('.')[0] for f in os.listdir(images)]
    annotations = [f.split('.')[0] for f in os.listdir(annotations)]
    missing_annotations = [img for img in images if img not in annotations]
    return missing_annotations

# the list of the images that do not have annotations
missing_annotations = find_images_without_annotations(images, annotations)
print("Images without annotations: ", missing_annotations)

# loop through the image files in the image directory
for filename in os.listdir(images):
    # check if the file is an image file
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # check if there is an annotation file for this image
        annotation_filename = os.path.join(annotations, os.path.splitext(filename)[0] + ".txt")
        if not os.path.exists(annotation_filename):
            # delete the image file if there is no corresponding annotation file
            os.remove(os.path.join(images, filename))
            print(f"Deleted {filename}")