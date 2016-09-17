
from __future__ import print_function
from dronekit import connect, VehicleMode
import numpy as np
import cv2
import sys
import time

class detectFlash:
    lastpix=0
    flashNum=0
        

    def detect_img(self, img):
        totalR=0
        totalB=0
        totalG=0
        avgG=0
        avgB=0
        avgR=0
        height, width, channels = img.shape
        imgsize= height*width

        totalpix=0
        for row in range(0,width):
            for column in range(0,height):


                px = img[column, row]
                totalR+=px[2]
                totalB+=px[0]
                totalG+=px[1]

        avgR=totalR/imgsize
        avgB=totalB/imgsize
        avgG=totalG/imgsize
        
        avgpix=(avgR+avgG+avgB)/3
        
                
                
        returnVal=False     
        if self.lastpix==0:
            self.lastpix=avgpix
            return returnVal
        elif avgpix-self.lastpix>=50:
            self.flashNum+=1
            returnVal=True
            self.lastpix=avgpix
            return returnVal
        else:
            self.lastpix=avgpix
            return returnVal

    def reset(self):
        self.lastpix=0
        self.flashNum=0

def react(int):
    return 0

def main():
    flash_detect = detectFlash()

    # Open /dev/video0
    vc = cv2.VideoCapture()
    vc.open(0)

    interval = .5
    last = time.time()
    while True:
        vc.grab()
        ret, buf = vc.retrieve()
        if not ret:
            SystemExit('Could not retrieve image.')
        if flash_detect.detect_img(buf):
            print("FLASH")
            react(1)

main()
