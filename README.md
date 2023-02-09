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

Furthermore, the dataset includes 52.000 images that are fully annotated, and 48.000 images that are partially annotated.




**NEED TO REMEMBER HERE TO EXPLAIN THE CLASSES DETAILS**

**ALSO NEED TO ADD THE TXT FILE THAT EXPLAINS ALL THE ANNOTATION VALUES AND THEIR NUMBERS**
## Conversion of the json annotation to YOLO txt format
