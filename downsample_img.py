import cv2
import numpy as np
import os
img_path = r'C:\Users\lyuyz\Desktop\workspace\ResGS\resgs.github.io\static\images\Teaser_readme.png'
img = cv2.imread(img_path)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
save_path = r"C:\Users\lyuyz\Desktop\workspace\ResGS\resgs.github.io\static\images\Teaser_readme_downsampled.png"
cv2.imwrite(save_path, img)
print('Downsampled image saved at:', img_path)
