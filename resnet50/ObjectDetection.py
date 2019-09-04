from imageai.Detection import ObjectDetection
import os
execution_path=os.getcwd()
detector=ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path,"resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections=detector.detectObjectsFromImage(input_image=os.path.join(execution_path,"2.jpg"),output_image_path=os.path.join(execution_path,"imagenew.jpg"))


for each in range(len(detections)):
    print(each["name"], " : ",each["percentage_probability"])
