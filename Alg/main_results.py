import matplotlib.pyplot as plt
import cv2
from PIL import Image
from image_circle import image_circle
from informations_to_image import informations_to_image


img_base = cv2.imread("Alg/data/disc/test/image/BINRUSHED1_image2.jpg")
img_base = image_circle(Image.fromarray(img_base), 98)
img_res = cv2.imread("Alg/results/process_test/BINRUSHED1_image2.jpg")
img_res = image_circle(Image.fromarray(img_res), 98)

"""
test =  img_res - img_base
cv2.imwrite('test.jpg', test)
"""
colors = ("b", "g", "r")        
channels = cv2.split(img_base)  
channels1 = cv2.split(img_res)      
#channels2 = cv2.split(test)

hist = []
for (i, col) in zip(channels, colors):       
    hist.append(cv2.calcHist([i], [0], None, [256], [1, 256]))  

hist1 = []
for (i, col) in zip(channels1, colors):     
    hist1.append(cv2.calcHist([i], [0], None, [256], [1, 256]))  

"""
hist2 = []
for (i, col) in zip(channels2, colors):       
    hist2.append(cv2.calcHist([i], [0], None, [256], [1, 256]))  

for (i) in range(3):       
    plt.plot(hist[i], color = colors[i])   
    plt.xlim([1, 256])
plt.show()

for (i) in range(3):       
    plt.plot(hist1[i], color = colors[i])   
    plt.xlim([1, 256])
plt.show()

for (i) in range(3):       
    plt.plot(hist1[i] - hist[i], color = colors[i])   
    plt.xlim([1, 256])
plt.show()
"""

plt.figure()    
plt.xlabel("Saturação",fontname="Times New Roman", fontsize=24)
plt.ylabel("Numero de Pixeis",fontname="Times New Roman", fontsize=24)
plt.yscale('log')
plt.grid()

for (i) in range(3):       
    plt.plot(hist[i], color = colors[i], linestyle='dotted') 
    plt.plot(hist1[i], color = colors[i])     
    plt.xlim([1, 256])
plt.savefig("Alg/results/histogram.jpg")
plt.show()
"""
for (i) in range(3):       
    plt.plot(hist2[i], color = colors[i])   
    plt.xlim([1, 256])
plt.show()
"""