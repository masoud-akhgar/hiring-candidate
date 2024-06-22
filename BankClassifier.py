import io
import requests
from PIL import Image
import torch
import pickle
import numpy
from transformers import AutoImageProcessor, DetrForSegmentation
from transformers.image_transforms import rgb_to_id
import os.path
import gc
import cv2
class BankDocPredictor():
    def __init__(self):
        self.__classifier = DetrForSegmentation.from_pretrained("facebook/detr-resnet-50-panoptic")
        self.__image_processor = AutoImageProcessor.from_pretrained("facebook/detr-resnet-50-panoptic")

    def predict(self,img_dir):
        try:
            image = cv2.imread(img_dir)
            inputs = self.__image_processor(images=cv2.cvtColor(image, cv2.COLOR_BGR2RGB), return_tensors="pt")
        except:
            return "Error: Not a Valid Image"
        outputs = self.__classifier(**inputs)

        target_sizes = torch.tensor([image.shape[1::-1]])
        result = self.__image_processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.8)[0]
        retrievedList=[]
        if len(result["scores"])==0:
            return "Error: No Table Invoice Was Detected"
        else: # return the first detected
            for score, label, box in zip(result["scores"], result["labels"], result["boxes"]):
                box = [round(i, 2) for i in box.tolist()]
                retrievedList.append(""+f"Detected {self.__classifier.config.id2label[label.item()]} with confidence " + f"{round(score.item(), 3)} at location {box}")
        
        del inputs
        del outputs
        del result
        gc.collect()
        return retrievedList   # unrelated
    def __str__(self):
        return "BankDocPredictor model is designed to detect bank table documents"