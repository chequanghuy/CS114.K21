import cv2
import numpy as np
import glob

i = 0 

for img in glob.glob('n/*.*'):
    try:
        img_abc = cv2.imread(img)
        img_abc = cv2.resize(img_abc, (int(img_abc.shape[1] * 0.1), int(img_abc.shape[0] * 0.1)))
        print(img)
        file_name = 'nb/' + str(i) + '.png'
        cv2.imwrite(file_name, img_abc)
        i += 1
    except:
        pass