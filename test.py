import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('screens/hs07.png',0)
img2 = img.copy()
img2 = cv2.resize(img2, (0, 0), fx=0.4628, fy=0.4628)
template = cv2.imread('hs-images/348.png',0)
w, h = template.shape[::-1]
threshold = 1

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    loc = np.where( res >= threshold )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    res = np.where( res >= threshold)
    print res
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()