from calc_pixel_values import calc_pixel_values


def informations_to_image(img):
    width, height = img.size
    pixel_values = calc_pixel_values(img)
    qtd_pixels = len(pixel_values)
    dimensions = len(pixel_values[0])
    return width, height, dimensions, pixel_values