import numpy as np
from informations_to_image import informations_to_image
from get_pixels_in_circle import get_pixels_in_circle

def image_circle(image, percentage_radius):
    pos = get_pixels_in_circle(image, percentage_radius)
    width, height, dimensions, pixel_values = informations_to_image(image)
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)
    for i in pos:
      pixel = list(pixel_values[width*i[0] + i[1]])
      img_process[i[0], i[1]] = tuple(pixel)
    return img_process