# -*- coding: utf-8 -*-
"""PLV_MODULE1_PIPELEINE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vHs5S8M8Siu6Vdqa2T74fzWEpjaL8ZN7
"""

"""YOUTUBE STREAM IMAGE FETCHER"""

import cv2
import pafy
import time
import os
import subprocess
import string
import random
import boto3
import pathlib
import json
import argparse
import platform
import shutil
import time
import torch
import torch.backends.cudnn as cudnn
import configparser
import my_utils
from my_utils.image_fetcher import image_fetcher
from my_utils.preprocess import pre_process
from numpy import random
from pathlib import Path
from datetime import datetime
from pymongo import MongoClient, errors
from subprocess import PIPE, run





def process2_pipeline(MODEL, MONGO, AWS_CREDENTIALS, AWS_ENV,PREPROCESSING_CONFIG):
    # IMAGE FETCHER SCRIPT
    url = "https://www.youtube.com/watch?v=e9LYewJGQlk"

    fetched_image, filename_string, str_date = image_fetcher(url)

    # etting the path for saving the fetched and preprocessed images.
    preprocess_image_dir_path = PREPROCESSING_CONFIG["preprocessed-image-dir-save-path"]
    
    # Sending the image to preprocessing script 
    pre_processed_image = pre_process(fetched_image, preprocess_image_dir_path, filename_string) 
  
    # Setting the directory path to fetch the image for detection 
    source = PREPROCESSING_CONFIG["preprocessed-image-dir-save-path"] + filename_string


    # DETECTION/ PREDICT part of the process pipeline
    command = [
            'python3',
            '/home/ubuntu/urban-detection/yolov5/detect.py',  
            '--weights',
            MODEL["weights"],
            '--source',
            source,
            '--img-size',
            MODEL["img-size"]]
   
   # Running the detection script
    sp = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, _ = sp.communicate()
    # printing the output from the detection script.
    print(output)


    

if __name__ == "__main__":
#Read config.ini file
    config_obj = configparser.ConfigParser()
    config_obj.read("config.ini")
    MODEL = config_obj["MODEL_INPUTS"]
    MONGO = config_obj["MONGODB_ENV"]
    AWS_CREDENTIALS = config_obj["AWS_CREDS"]
    AWS_ENV = config_obj["AWS_ENV"]
    PREPROCESSING_CONFIG = config_obj["PRE_PROCESSING_BOUNDS"]
    iteration = 0
    while True:
        print(f"iteration {iteration}")
        start = time.time()
        
        process2_pipeline(MODEL, MONGO, AWS_CREDENTIALS, AWS_ENV,PREPROCESSING_CONFIG)

        end = time.time()
        diff = end - start
        print(diff)
        time.sleep(40)
        iteration += 1 













