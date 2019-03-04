# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:25:28 2019

@author: Shishir
"""
import win32api, win32con
import pyscreenshot as ImageGrab
import sys
import cv2
import numpy as np

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#click(15,15)
#bot image to find
template = cv2.imread('bot.png')
w, h = template.shape[:-1]

try:
    #Screengrab of specific area
    while True:
        if __name__ == "__main__":
            # part of the screen
            im=ImageGrab.grab(bbox=(230,440,750,580)) # X1,Y1,X2,Y2
#            im.show()
            im.save("screenTest.png")
            
            img_org = cv2.imread('screenTest.png')
            res = cv2.matchTemplate(img_org, template, cv2.TM_CCOEFF_NORMED)
            threshold = .80
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):  # Switch collumns and rows
                cv2.circle(img_org, (pt[0]+3, pt[1]), 1, (0, 0, 255), 2)
                click(pt[0]+3+230,pt[1]+400)
#            cv2.imshow("marked",img_org)
except KeyboardInterrupt:
    sys.exit()