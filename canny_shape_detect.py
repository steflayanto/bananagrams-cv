import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Stefa\Desktop\Bananagram Solver\bananagrams-cv\imgs/2.jpg", cv2.IMREAD_COLOR)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# namedWindow('image2', WINDOW_NORMAL)
# resizeWindow("image", 600,600)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, gray = cv2.threshold(gray,230,255, cv2.THRESH_BINARY)
edges1 = cv2.Canny(gray,80,230)

# imshow("image", thresh1)
# imshow("image2", edges)
cv2.imwrite("canny.png", edges1)

def get_contour(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (7, 7), 0)
    edges = cv2.Canny(blur, 50, 100, apertureSize=3)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(edges, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(
        dilation,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)
    print(type(contours))
    max_cnt = max(contours, key=cv2.contourArea)
    # cnt = contours[0]
    # print(type(cnt))
    contour_img = img.copy()
    contour_img = np.zeros(img.shape)
    # print(len(cnt))
    cv2.drawContours(contour_img, [max_cnt], 0, (0, 255, 0))
    # for i in range(len(contours)):
    #     cv2.drawContours(contour_img, contours, i, (0, 255, 0))
    return contour_img, None

# cnt_img, cnt = get_contour(img)
cv2.imshow("image", cnt_img)
cv2.waitKey(0)
# imwrite("thresh.png", thresh1)
# waitKey(0)
# destroyAllWindows()

# contours, hierarchy = findContours(gray, RETR_LIST, CHAIN_APPROX_SIMPLE)
"""
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
"""