import os
from PIL import Image
import cv2
import numpy as np
from find_pixel_position import find_pixel_position
from image_circle import image_circle
from otimize_img import otimize_img


dir = 'Alg/data/disc/test/image'
#dir = 'Alg/data/disc/train/image'

for i, path in enumerate(os.listdir(dir)):
    print("imagem" + str(i))
    
    if os.path.isfile(os.path.join(dir, path)):
        image = cv2.imread(os.path.join(dir, path), cv2.IMREAD_UNCHANGED)
        image_blurred = cv2.GaussianBlur(image, (0, 0), 15)
        image_processed = cv2.addWeighted(image, 4, image_blurred, -4, 128)

        image = Image.fromarray(image)
        image_processed = Image.fromarray(image_processed)

        positions = find_pixel_position([(50, 20, 60), (0, 0, 0)], 80, image_processed)
        res = otimize_img(positions, image, 300, 0)

        image_array = np.array(res, dtype=np.uint8)
        res = Image.fromarray(image_array)

        res = image_circle(res, 98)
        cv2.imwrite('Alg/results/process_test/' + path, res)
        #cv2.imwrite('results/process/' + path, res)