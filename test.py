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
# выводим полный путь к изображению в консоль
print(IMAGE_FILE)
# считываем изображение
CONTAINER = imread(IMAGE_FILE)
# выведем информацию об изображении
# выводится кортеж, в котором
# первое значение - высота изображения в пикселях - image.shape[0]
# второе значение - ширина изображения в пикселях - image.shape[1]
# третье значение - глубина цвета (цветность - количество байт на один пиксель) - image.shape[2]
print(CONTAINER.shape)
# выведем количество пикселей в изображении
print(CONTAINER.shape[0] * CONTAINER.shape[1], "пикселей")
# выведем объем изображения в битах
print(CONTAINER.shape[0] * CONTAINER.shape[1] * CONTAINER.shape[2], "байт")

# преобразуем изображение в матрицу значений
arr = np.asarray(CONTAINER)

# отобразим изображение
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
plt.show()
