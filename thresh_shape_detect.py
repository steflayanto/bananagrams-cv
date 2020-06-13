from cv2 import *
import numpy as np

img = imread(r"C:\Users\Stefa\Desktop\Bananagram Solver\bananagrams-cv\imgs/2.jpg", IMREAD_COLOR)

namedWindow('image', WINDOW_NORMAL)
namedWindow('image2', WINDOW_NORMAL)
# resizeWindow("image", 600,600)
gray = cv2.cvtColor(img, COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,230,255,THRESH_BINARY)
# edges = cv2.Canny(img,100,200)
imshow("image", thresh1)
imshow("image2", gray)
# imwrite("canny.png", edges)
# imwrite("thresh.png", thresh1)
waitKey(0)
destroyAllWindows()
# exit()
# contours, hierarchy = findContours(gray, RETR_LIST, CHAIN_APPROX_SIMPLE)

h, w = img.shape[:2]

contours0, hierarchy = findContours( thresh1.copy(), RETR_TREE, CHAIN_APPROX_SIMPLE)
contours = [approxPolyDP(cnt, 3, True) for cnt in contours0]
namedWindow('contours', WINDOW_NORMAL)
def update(levels):
    vis = np.zeros((h, w, 3), np.uint8)
    levels = levels - 3
    drawContours( vis, contours, (-1, 2)[levels <= 0], (128,255,255),
        3, LINE_AA, hierarchy, abs(levels) )

    imshow('contours', vis)

update(3)
namedWindow('image', WINDOW_NORMAL)
createTrackbar( "levels+3", "contours", 3, 7, update )
imshow('image', img)
waitKey()
print('Done')
