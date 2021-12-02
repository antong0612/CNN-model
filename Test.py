import cv2

def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    crop_img = img[200:, :]
    img = crop_img
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

img = cv2.imread('AAA.jpg')
img = preProcess(img)
cv2.imshow('Cropped', img)
cv2.waitKey(0)