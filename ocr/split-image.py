import cv2
import numpy as np

img = cv2.imread('ocr/img/safeway2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('ocr/res/gray.png', gray)

# threshold
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

# minAreaRect on the nozeros
pts = cv2.findNonZero(threshed)
ret = cv2.minAreaRect(pts)

(cx,cy), (w,h), ang = ret

# empiric fix of image being upside down
ang -= 180
print(ang)

if w > h:
    print('width greater than height')
    w,h = h,w
    ang += 90

print('angle', ang)

# find rotated matrix, do rotation
M = cv2.getRotationMatrix2D((cx,cy), ang, 1.0)
rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))
cv2.imwrite('ocr/res/rotated.png', rotated)

# find and draw the upper and lower boundary of each lines
hist = cv2.reduce(rotated,1, cv2.REDUCE_AVG).reshape(-1)

th = 2
H,W = img.shape[:2]
uppers = [y for y in range(H-1) if hist[y]<=th and hist[y+1]>th]
lowers = [y for y in range(H-1) if hist[y]>th and hist[y+1]<=th]

rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
for y in uppers:
    cv2.line(rotated, (0,y), (W, y), (255,0,0), 1)

for y in lowers:
    cv2.line(rotated, (0,y), (W, y), (0,255,0), 1)

cv2.imwrite('ocr/res/result.png', rotated)
