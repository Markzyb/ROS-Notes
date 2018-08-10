# --coding: utf-8--
import numpy as np
import cv2


img = cv2.imread('/home/intel/Desktop/img.jpg',0)


cv2.imshow('gaiminzi',img)


img2 = cv2.imread('/home/intel/Desktop/img2.jpg')


cv2.imshow('gaiminzi2',img2)

cv2.waitKey (0)

cv2.destroyAllWindows()

#中文注释实验 
