from math import sqrt
from informations_to_image import informations_to_image


def get_pixels_in_circle(image, percentage_radius):
    width, height, dimensions, pixel_values = informations_to_image(image)
    x0 = int(width/2)
    y0 = int(height/2)
    radius = ((width+height) / 4) * percentage_radius/100
    circle_indices = []
    for x in range(width):
        for y in range(height):
            dx = x - x0
            dy = y - y0
            distance = sqrt((dx ** 2) + (dy ** 2))
            if distance <= radius:
                circle_indices.append((x, y))
    return circle_indices