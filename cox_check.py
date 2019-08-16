from scipy import (
    fftpack,
)  # модуль позволяет выполнить ДКП - реализация функций в открытом доступе (англ.)


def algorithm_check(modified_elements, empty_container, full_container, omega):
    """Проверяем встроенную ЦВЗ

    Данная функция позволяет проверить работу алгоритма.
    Сначала находим ДКП для заполненного контейнера-изображения, а затем 1000 наибольших спектральных элементов.
    После этого повторяем данные действия для пустого контенера. Затем вычитаем из модифицированных значений
    заполненного контейнера модифицированные значения незаполненного контейнера.
    Полученный результат сравниваем с последовательностью Omega, которую встраивали ранее.
    При совпадении значений функция выведет в консоль True.
    modified_elements[n][0] - индекс-строка n-го элемента
    modified_elements[n][1] - индекс-столбец n-го элемента
    """

    # производим прямое косинусное преобразование full_container
    full_container_dct = fftpack.dct(
        fftpack.dct(full_container.T, norm="ortho").T, norm="ortho"
    )
    # создаем массив и записываем туда значения наибольших элементов при встроенной ЦВЗ
    full_container_max_elements = []
    for i in modified_elements:
        full_container_max_elements.append((full_container_dct[i[0]][i[1]]))
    # производим прямое косинусное преобразование full_container
    empty_container_dct = fftpack.dct(
        fftpack.dct(empty_container.T, norm="ortho").T, norm="ortho"
    )
    # создаем массив и записываем туда значения наибольших элементов без встроенной ЦВЗ
    empty_container_max_elements = []
    for i in modified_elements:
        empty_container_max_elements.append((empty_container_dct[i[0]][i[1]]))

    # теперь вычтем из full_container_max_elements значения  empty_container_max_elements
    # результаты запишем в check_arr
    check_arr = []
    for idx in range(len(full_container_max_elements)):
        check_arr.append(
            (full_container_max_elements[idx] - empty_container_max_elements[idx])
        )

    print("Результат проверки:", check_arr in omega)
