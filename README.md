Реализация алгоритма И. Кокса для встраивания ЦВЗ в полутоновое растровое изображение

При реализации использована версия Python 3.7 (реализация интерпретатора CPython).
Дополнительно были задейстованы модули:
os  # взаимодействие с системой для указания пути к файлам, их загрузке и выгрузке
matplotlib.image  # модуль для загрузки исходного файла с изображением
matplotlib.pyplot as plt  # модуль для отрисовки полотна с изображением
numpy   # модуль использован для проведения операций над матрицами полотна с изображение
scipy # модуль позволяет выполнить ДКП - реализация функций в открытом доступе (англ.)

Установка модулей через pip:
pip install numpy matplotlib scipy scikit-image

Даны подробные комментарии. Для ознакомления с реализацией сторонних модулей можно 
использовать документацию по соответствующему модулю, либо смотреть исходный код.

Запуск производится из main.py, где также можно заменить образец изображения sample_image.png. 