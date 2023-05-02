from calc_pixel_values import calc_pixel_values


def find_pixel_position(vector_color, range, img):
    img = calc_pixel_values(img)
    positions = []
    for color in vector_color:
        for i, position in enumerate(img):
            if ((position[0] >= color[0] and position[0] <= color[0] + range) 
            and (position[1] >= color[1] and position[1] <= color[1] + range) 
            and (position[2] >= color[2] and position[2] <= color[2] + range)):
                positions.append(i)
    return set(positions)