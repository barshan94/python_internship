import cv2

'''
#Displaying a image
img=cv2.imread('ai.jpg')
cv2.imshow('OUTPUT1',img)
cv2.waitKey(0) #holds miliseconds but while using it permanents the image
cv2.destroyAllWindows()

'''

'''
#Duplicating a image
img=cv2.imread('2.jpg')
cv2.imshow('OUTPUT1',img)
cv2.imwrite('Reyna.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#Properties about img
img=cv2.imread('4.jpg')
print(img.shape)
'''

'''
#Converts a image into grayscale image
img=cv2.imread('4.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Orginal Image',img)
cv2.imshow('Grayscale Image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#Converts a image to gracscale
img=cv2.imread('3.jpg',0)
cv2.imshow('Grayscale Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#Convert a image into Binary
img=cv2.imread('ai.jpg')
ret,binary=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Image',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#White background
import numpy as np
img=np.ones((1000,800,3))
cv2.imshow('White Background',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
#Black Background
import numpy as np
img=np.zeros((1000,800,3))
cv2.imshow('Black Background',img)
cv2.waitKey()
cv2.destroyAllWindows()
'''

