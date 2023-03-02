# Converting-annotation-from-JSON-to-YOLO-format
## Project Description
As we are developing the roadscanner application that can detect damages, traffic signs and other necessary information on the roads, we came across several dataset. For Traffic Sign, the most sutiable dataset found for training was the [Mapillary Traffic Sign Dataset](https://www.mapillary.com/dataset/trafficsign). Howwver, the obstacle we encountered in the beginning is the annotation format of the labels. We are training machine on YOLOv7, which does not recognise the json annotation format. This repository contribute in conversion of these annotations (and also any similar type of annotations) to txt format to make it ready for training in YOLO and provide a step-by-step guideline for using the files.

## Dataset
The annotations are stored as JSON with the following keys:
 - `width`: the width of the corresponding image
 - `height`: the height of the corresponding image
 - `ispano`: a boolean indicating if the image is a 360° panorama image
 - `objects`: a list of traffic signs in the image

 Each object is itself a dictionary with the following keys:
  - `bbox`: defining the bounding box of the traffic sign within the image.
  - `key`: a unique identifier of the traffic sign.
  - `label`: the class of the traffic sign
  - `properties`: a dictionary defining special properties of the sign.

Panoramas are stored as standard images with equirectangular projection and can be loaded as any image.

For the special case of traffic signs that extend across the image boundary of a panorama (`xmin > xmax`),
we include a dictionary `cross_boundary` in the `bbox` defnition containing the `left` and the `right` crop of the bounding box. In order to extract the full image crop of the traffic sign, one can crop `left` and `right` separately and stitch them together.
In addition to the bounding boxes and the matching traffic sign templates, the annotators were asked to provide additional attributes for each sign: 
-	occluded if the sign is partly occluded
-	Ambiguous if the sign is not classifiable at all (e.g. too small, bad quality, heavy occlusion etc.)
-	Dummy if it looks like a sign but isn’t (e.g. car stickers, reflections, etc.)
-	out-of-frame if the sign is cut off by the image border
-	included if the sign is part of another bigger sign 
-	Exterior if the sign includes other signs.

Furthermore, the dataset includes 52.000 images that are fully annotated, and 48.000 images that are partially annotated. Detailed description of each of the labels can be found in the repository. 

From the annotations, it is observed that the annotations are classfied into 401 classes, in 5 main categories: `complementary`, `information`,`regulatory`,`warning` and `other-sign`. For the convenience of the conversions, I have limited the labelling into these 5 classes.

## Conversion of the json annotation to YOLO txt format
Download and open the [json2yolo_mapillaryfull.py](https://github.com/TahmidTowsifAhmed/Converting-annotation-from-JSON-to-YOLO-format/blob/main/json2yolo_mapillaryfull.py) file. On line 4, direct the `path`to the annotation files saved on the local machine. The script will generate a folder under the working directory naming `yolov7_dataset`where it will save all the converted annotation files. You can change the name according to your requirements. As mentioned earlier, the script will look for the category names inside the `class_label`of json annotation format and based on that classify the labels for YOLO format. 

## Looking for images missing annotations
There can be cases while converting annotations is that YOLO annotation is not generated, since in some of the images there is no annotation. Too detect these images, you can look [find_missing_images.py](https://github.com/TahmidTowsifAhmed/Converting-annotation-from-JSON-to-YOLO-format/blob/main/find_missing_images.py), where in line 9, you direct the `path`wehre you have the images saved and in line 10, you direct the `path`where you have the respective annotations saved. The output will give you the list of the images that does not contain annotation files.

## Deleting images missing annotations
As we have identified the images that do not have annotaions, we can do two things: annotate the images or delete them. If you think you do not need these images, you can delete them with [delete_missing_images.py](https://github.com/TahmidTowsifAhmed/Converting-annotation-from-JSON-to-YOLO-format/blob/main/delete_missing_images.py). Same as before, just direct the path to the images and annotations folders in line 4 and 5 and run the script. This will delete the images that do have annotations missing.
