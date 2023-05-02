from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from addlabels import addlabels
from calc_rgb import calc_rgb
from informations_to_image import informations_to_image


def generate_graph(img, name):
    if(type(img) == np.ndarray):
        img = Image.fromarray(img)

    width, height, dimensions, pixel_values = informations_to_image(img)
    r, g, b = calc_rgb(width, height, pixel_values)

    x = ["Vermelho(R)", "Verde(G)", "Azul(B)"]
    y = [round(r, 3), round(g, 3), round(b, 3)]
    plt.bar(x, y, color=['red', 'green', 'blue'])
    addlabels(x, y)
    plt.ylabel("Quantidade de Cor")
    plt.title("Dominancia de Cor")
    plt.savefig(name + '.png', format='png')
    plt.close()