# Author:Fuhong Gao
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img = np.array(Image.open("cat0.jpg"))

# 随机生成500个椒盐
rows, cols, dims = img.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

plt.figure("Mona Lisa")
plt.imshow(img)
plt.axis('off')
plt.show()