import cv2
from PIL import Image
import numpy as np
from find_pixel_position import find_pixel_position
from image_circle import image_circle
from otimize_img import otimize_img


img_base = cv2.imread('Alg/data/disc/test/image/BINRUSHED1_image2.jpg', cv2.IMREAD_UNCHANGED)
image_blurred = cv2.GaussianBlur(img_base, (0, 0), 15)
cv2.imwrite('Alg/results/img-blurred.jpg', image_blurred)
image_pre_processed = cv2.addWeighted(img_base, 4, image_blurred, -4, 128)
cv2.imwrite('Alg/results/img-pre-processed.jpg', image_pre_processed)
image_pre_processed = cv2.imread('Alg/results/img-pre-processed.jpg', cv2.IMREAD_UNCHANGED)
img_base = Image.fromarray(img_base)
image_pre_processed = Image.fromarray(image_pre_processed)
positions = find_pixel_position([(50, 20, 60), (0, 0, 0)], 80, image_pre_processed)
image_res = otimize_img(positions, img_base, 300, 0)
image_array = np.array(image_res, dtype=np.uint8)
image_res = Image.fromarray(image_array)
image_res = image_circle(image_res, 98)
positions = find_pixel_position([(50, 20, 60), (0, 0, 0)], 80, image_pre_processed)
image_pre_processed_black = otimize_img(positions, img_base, 30, 300)
cv2.imwrite('Alg/results/img-pre-processed-black.jpg', image_pre_processed_black)
cv2.imwrite('Alg/results/img-res.jpg', image_res)
cv2.imwrite('Alg/results/img-final.jpg', np.concatenate([img_base, image_blurred, image_pre_processed, image_pre_processed_black, image_res], axis=1))
cv2.imshow("img final", cv2.imread('Alg/results/img-final.jpg', cv2.IMREAD_UNCHANGED))
cv2.waitKey(0); 
cv2.destroyAllWindows();