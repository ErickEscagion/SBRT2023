import numpy as np
from PIL import Image


def create_image():
    img = [

        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],
 
        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [10, 40, 120], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[10, 40, 120], [10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [10, 40, 120], [10, 40, 120], [10, 40, 120],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [190, 190, 190], [190, 190, 190], [10, 40, 120],[10, 40, 120], [10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 220, 50], [190, 220, 50],[190, 220, 50] 
        ],

        [
            [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [10, 40, 120], [10, 40, 120], [10, 40, 120], [10, 40, 120],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 220, 50], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [10, 40, 120], [10, 40, 120], [10, 40, 120],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [10, 40, 120], [10, 40, 120], [10, 40, 120],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [10, 40, 120], [10, 40, 120], [10, 40, 120],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [190, 190, 190], [190, 190, 190], [10, 40, 120],[10, 40, 120], [10, 40, 120], [10, 40, 120], [190, 190, 190], [190, 190, 190],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [10, 40, 120], [10, 40, 120], [10, 40, 120],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[10, 40, 120], [10, 40, 120], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ],

        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190], [190, 190, 190],[190, 190, 190], [190, 190, 190], [10, 40, 120], [190, 190, 190], [190, 190, 190],[190, 190, 190] 
        ]
    ]
    image_array = np.array(img, dtype=np.uint8)
    img_base = Image.fromarray(image_array)
    return img_base


def create_image_mini():
    img = [

        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190]
        ],
        [
            [190, 190, 190], [10, 40, 120], [190, 190, 190]
        ],
        [
            [190, 190, 190], [190, 190, 190], [2, 5, 10]
        ]
    ]
    image_array = np.array(img, dtype=np.uint8)
    img_base = Image.fromarray(image_array)
    return img_base
