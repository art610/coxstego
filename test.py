import os

import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread

# изображение в формате png помещаем в директорию с данным скриптом
IMAGE_NAME = "sample_image.png"  # указываем здесь наименование изображения

# получаем путь к текущей директории (где находится скрипт)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# получаем полный путь к изображению (включая его название)
IMAGE_FILE = os.path.join(CURRENT_DIR, IMAGE_NAME)
print(IMAGE_FILE)
# считываем изображение
CONTAINER = imread(IMAGE_FILE)
# преобразуем изображение в матрицу значений
arr = np.asarray(CONTAINER)
print(arr)
# отобразим изображение
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
plt.show()
