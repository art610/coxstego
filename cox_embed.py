import numpy as np  # модуль для обработки и вычислений
from scipy import (
    fftpack,
)  # модуль позволяет выполнить ДКП - реализация функций в открытом доступе (англ.)

# некоторые функции были  вынесены в отдельные файлы, которые необходимо импортировать как модули
import zigzag_scan  # импортируем скрипт для развертки исходной матрицы ДКП в змеевидном порядке


def cox_embed(container, omega, alpha):
    """Функция производит встраивание последовательности omega с учетом коэффициентов alpha в container

    Данная функция позволяет встроить информацию (последовательность omega) в изображение-контейнер container,
    коэффициент alpha позволяет снизить искажения при встраивании (выбирается либо случайным образом, либо
    при помощи отдельного алгоритма)
    Над контейнером производим ДКП (функция dct модуля fftpack) и получаем матрицу для модификации
    Алгоритм И.Кокса подразумевает модификацию спектральных компонент (уширение), в частности, к каждому
    из выбранных компонент необходимо прибавить соответствующее значение omega(i), умноженное на коэффициент alpha
    """

    # производим прямое косинусное преобразование изображения-контейнера
    # реализация функции dct доступна в модуле fftpack (в документации даются доп. пояснения по реализации)
    dct = fftpack.dct(fftpack.dct(container.T, norm="ortho").T, norm="ortho")

    # проходим по матрице элементов ДКП зигзагом и на основе этого создаем новую матрицу
    # матрица zigzagmatrix содержит индексы и значения элементов,
    # элементы расположены в соответствие с порядком "змеевидного" прохода по исходной матрице
    zigzagmatrix = zigzag_scan.zigzagscan(dct)

    def get_thousand_max_elements(matrix):
        """Функция производит поиск 1000 наибольших элементов в матрице matrix

        Данная функция принимает в качестве аргумента матрицу matrix (двумерный массив/список)
        Функция возвращает матрицу из значений и индексов 1000 наибольших элементов исходной матрицы
        Сохраняется порядок элементов, который был получен при "змеевидном" (или другом) проходе по исходной матрице
        """
        elements_values = (
            []
        )  # здесь храним только значения элементов исходной матрицы (последний столбец)
        for i in range(
            len(matrix)  # количество элементов в исходной матрице
        ):  # в данном цикле мы переписываем значения из матрицы в массив elements_values
            elements_values.append(zigzagmatrix[i][2])
        # отбираем индексы у 1000 наибольших значений из elements_values
        N = 1000  # количество элементов для отбора
        max_elements_idx = np.argsort(elements_values)[
                           -N:
                           ]  # создаем массив с индексами наибольших элементов
        # значения 1000 наибольших элементов запишем в отдельный массив (список / list) max_elements
        max_elements = (
            []
        )  # здесь храним выбранную для модификации 1000 наибольших значений массива elements_values
        for idx in max_elements_idx:  # данный цикл заполняет массив max_elements
            max_elements.append(elements_values[idx])
        # в матрицу result_matrix сохраним 1000 наибольших значений и их индексы в исходной матрице ДКП
        # элементы сохраняем в порядке изначального (змейкой/зигзагом) обхода матрицы ДКП
        result_matrix = []
        for row in matrix:
            if (
                row[2] in max_elements
            ):  # данный столбец (последний) хранит значения, предыдущие два столбца хранят индексы
                result_matrix.append(row)
        # возвращаем результирующую матрицу с 1000 наибольших элементов исходной матрицы
        return result_matrix

    max_elements_in_matrix = get_thousand_max_elements(zigzagmatrix)

    # ====================================================================================

    def cox_mod(source_dct_matrix, elements_in_matrix):
        """Функция производит модификацию спектральных компонент в матрице ДКП

        Данная функция принимает в качестве аргумента матрицу matrix (двумерный массив/список)
        Функция возвращает матрицу из значений и индексов 1000 наибольших элементов исходной матрицы
        Сохраняется порядок элементов, который был получен при "змеевидном" (или другом) проходе по исходной матрице
        """
        # модифицируем значения элементов в конечной матрице,
        # которая представляет собой пространство признаков
        # увеличиваем значения в третьем столбце в матрице

        # умножим omega на alpha в соотвествие с формулой алгоритма И. Кокса
        for el in omega:
            el *= alpha

        # встроим значения из переданной последовательности Omega
        for el_idx in range(1000):
            elements_in_matrix[el_idx][2] += omega[el_idx]
        # весовой коэффициент alpha используем для снижения искажений от встраивания omega
        # вставим модифицированные значения в матрицу ДКП в соответствие с их индексами
        for row in elements_in_matrix:
            source_dct_matrix[row[0]][row[1]] = row[2]

    cox_mod(dct, max_elements_in_matrix)

    # ====================================================================================

    # запишем найденные максимальные значения в отдельный файл max_elements.txt

    with open('max_elements.txt', 'w') as ouf2:
        for el1 in max_elements_in_matrix:
            ouf2.write(str(el1) + '\n')

    # ====================================================================================
    # проводим обратное ДКП и формируем заполненный контейнер
    # обратное косинусное преобразование
    full_container = fftpack.idct(fftpack.idct(dct.T, norm="ortho").T, norm="ortho")

    return full_container
