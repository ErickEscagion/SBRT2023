import cv2
import numpy as np


image = cv2.imread('Alg/data/disc/test/image/BINRUSHED1_image2.jpg', cv2.IMREAD_UNCHANGED)

image_blurred = cv2.GaussianBlur(image, (0, 0), 15)
image_processed = cv2.addWeighted(image, 4, image_blurred, -4, 128)
cv2.imwrite('Alg/results/tests/pre-processed.jpg', np.concatenate([image_blurred, image_processed], axis=1))

image_blurred2 = cv2.GaussianBlur(image, (0, 0), 15)
image_processed2 = cv2.addWeighted(image, 5, image_blurred2, -4, 128)
cv2.imwrite('Alg/results/tests/pre-processed2.jpg', np.concatenate([image_blurred2, image_processed2], axis=1))

image_blurred3 = cv2.GaussianBlur(image, (0, 0), 15)
image_processed3 = cv2.addWeighted(image, 4, image_blurred3, -5, 128)
cv2.imwrite('Alg/results/tests/pre-processed3.jpg', np.concatenate([image_blurred3, image_processed3], axis=1))

image_blurred4 = cv2.GaussianBlur(image, (0, 0), 15)
image_processed4 = cv2.addWeighted(image, -500, image_blurred4, 500, 128)
cv2.imwrite('Alg/results/tests/pre-processed4.jpg', np.concatenate([image_blurred4, image_processed4], axis=1))

image_blurred5 = cv2.GaussianBlur(image, (0, 0), 100)
image_processed5 = cv2.addWeighted(image, 4, image_blurred5, -4, 128)
cv2.imwrite('Alg/results/tests/pre-processed5.jpg', np.concatenate([image_blurred5, image_processed5], axis=1))

image_blurred6 = cv2.GaussianBlur(image, (0, 0), 100)
image_processed6 = cv2.addWeighted(image, 5, image_blurred6, -4, 128)
cv2.imwrite('Alg/results/tests/pre-processed6.jpg', np.concatenate([image_blurred6, image_processed6], axis=1))

image_blurred7 = cv2.GaussianBlur(image, (0, 0), 100)
image_processed7 = cv2.addWeighted(image, 4, image_blurred7, -5, 128)
cv2.imwrite('Alg/results/tests/pre-processed7.jpg', np.concatenate([image_blurred7, image_processed7], axis=1))

image_blurred8 = cv2.GaussianBlur(image, (0, 0), 100)
image_processed8 = cv2.addWeighted(image, -500, image_blurred8, 500, 128)
cv2.imwrite('Alg/results/tests/pre-processed8.jpg', np.concatenate([image_blurred8, image_processed8], axis=1))

cv2.imwrite('Alg/results/tests/concat.jpg', np.concatenate(
    [
        cv2.imread('Alg/results/tests/pre-processed.jpg', cv2.IMREAD_UNCHANGED),
        cv2.imread('Alg/results/tests/pre-processed2.jpg', cv2.IMREAD_UNCHANGED),
        cv2.imread('Alg/results/tests/pre-processed3.jpg', cv2.IMREAD_UNCHANGED),
        cv2.imread('Alg/results/tests/pre-processed4.jpg', cv2.IMREAD_UNCHANGED),
        cv2.imread('Alg/results/tests/pre-processed5.jpg', cv2.IMREAD_UNCHANGED),
        cv2.imread('Alg/results/tests/pre-processed6.jpg', cv2.IMREAD_UNCHANGED),
        cv2.imread('Alg/results/tests/pre-processed7.jpg', cv2.IMREAD_UNCHANGED),
        cv2.imread('Alg/results/tests/pre-processed8.jpg', cv2.IMREAD_UNCHANGED),
    ], axis=0))

cv2.imshow("img final", cv2.imread('Alg/results/tests/concat.jpg', cv2.IMREAD_UNCHANGED))
cv2.waitKey(0); 