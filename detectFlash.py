
import numpy as np
import cv2

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
        print type(img)
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

    def reset():
        self.lastpix=0
        self.flashNum=0

def main():
    flash_detect = detectFlash();
    img = cv2.imread("/Users/Simeon/Documents/darkimg.jpeg");
    print "in main: "
    print type(img)
    count = 0
    while True:
        if (flash_detect.detect_img(img)):
            print("FLASH")
        print(count)
        if (count >= 20):
            img = cv2.imread("/Users/Simeon/Documents/lightimg.jpeg");
        count += 1

main()








#######video or frames or input
    
        
        ##output for some light in the first flash
        
        
            
            
            
    
