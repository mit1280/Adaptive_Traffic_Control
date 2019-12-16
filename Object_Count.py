import time
from PIL import Image   
from imageai.Detection import ObjectDetection
import os

execution_path=os.getcwd()
detector=ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path,"yolo.h5"))
detector.loadModel()

x=time.time()
file_name=os.listdir("/Users/mit/Downloads/Yolo")
file_name=file_name[2]
image_obj =Image.open(execution_path+"/"+file_name)
width,height = image_obj.size
cropped_image_V_1 = image_obj.crop((0, 0, width/2, height))
cropped_image_V_2 = image_obj.crop((width/2, 0, width, height))
cropped_image_V_1.save('cropped3.jpg')
cropped_image_V_2.save('cropped4.jpg')	
detectionsv1=detector.detectObjectsFromImage(os.path.join(execution_path,"cropped3.JPG"),execution_path+"/h1_"+file_name)
detectionsv2=detector.detectObjectsFromImage(os.path.join(execution_path,"cropped4.JPG"),execution_path+"/h2_"+file_name)
sum0=0
for i in range(len(detectionsv1)):
    if(detectionsv1[i]['name']== 'truck' or detectionsv1[i]['name']== 'bus' or detectionsv1[i]['name']== 'bicycle' or detectionsv1[i]['name']== 'motorbike' or detectionsv1[i]['name']== 'car'):
        sum0=sum0+1
sum1=0
for i in range(len(detectionsv2)):
    if(detectionsv2[i]['name']== 'truck' or detectionsv2[i]['name']== 'bus' or detectionsv2[i]['name']== 'bicycle' or detectionsv2[i]['name']== 'motorbike' or detectionsv2[i]['name']== 'car'):
        sum1=sum1+1
print(sum0+sum1)
y=time.time()
print(y-x)