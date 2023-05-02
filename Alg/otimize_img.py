import numpy as np
from informations_to_image import informations_to_image


def otimize_img(positions, img_base, increment, decrement):
    width, height, dimensions, pixel_values = informations_to_image(img_base)
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)
    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])
            if width*h + w in positions:
                  pixel[0] = pixel[0] + increment
                  pixel[1] = pixel[1] + increment
                  pixel[2] = pixel[2] + increment

                  if(pixel[0] > 255):
                    pixel[0] = 255 
                  if(pixel[1] > 255):
                    pixel[1] = 255
                  if(pixel[2] > 255):
                    pixel[2] = 255    
            else:
                  pixel[0] = pixel[0] - decrement
                  pixel[1] = pixel[1] - decrement
                  pixel[2] = pixel[2] - decrement

                  if(pixel[0] < 0):
                    pixel[0] = 0 
                  if(pixel[1] < 0):
                    pixel[1] = 0
                  if(pixel[2] < 0):
                    pixel[2] = 0
            
            img_process[h, w] = tuple(pixel)
    return img_process