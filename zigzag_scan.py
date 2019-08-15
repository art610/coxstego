def zigzagscan(matrix):
    # zigzag - представляет собой матрицу, где в каждой строке определены соответствующие значения
    zigzag = []
    n = len(matrix)
    m = len(matrix)
    i = 0

    # ====================================================================================================================
    # ====================================================================================================================
    # КВАДРАТНАЯ МАТРИЦА
    if m == n:
        for j in range(1, m):  # идем по первой строке зигзагами до поворота
            # первая часть исходной матрицы (до конца центральной диагонали)
            if j != m and i != n:
                if j % 2 == 0:  # если первый столбец четный
                    k1 = j
                    k2 = 0
                    while k1 >= 0 and k2 <= j:
                        if k1 <= m and k2 <= n:
                            zigzag.append(
                                [k1, k2, matrix[k1][k2]]
                            )  # добавляем соответствующие значения в матрицу
                        k1 -= 1
                        k2 += 1
                else:  # если первый столбец нечетный
                    k1 = j
                    k2 = 0
                    while k1 >= 0 and k2 <= j:
                        if k1 <= m and k2 <= n:
                            zigzag.append([k2, k1, matrix[k2][k1]])
                        k1 -= 1
                        k2 += 1

                i += 1

        # ==================================================================
        # вторая часть исходной матрицы
        col = m - 1
        for row in range(1, n):  # делаем поворот и проходим оставшуюся часть
            if row % 2 != 0:  # нечетные строки в матрице
                k1 = row
                k2 = col
                while k1 < n and k2 > 0:
                    zigzag.append([k1, k2, matrix[k1][k2]])
                    k1 += 1
                    k2 -= 1
            else:  # четные строки в матрице
                k1 = row
                k2 = col
                while k1 < n and k2 > 0:
                    zigzag.append([k2, k1, matrix[k2][k1]])
                    k1 += 1
                    k2 -= 1
            row += 1

    # ====================================================================================================================
    # ПРЯМОУГОЛЬНАЯ МАТРИЦА
    if m != n:
        row = 0
        # первая часть матрицы
        for col in range(1, m):  # идем по первой строке зигзагами до поворота
            # сделать проверку на нулевой индекс для первого значения
            # 1 диагональ ===========================
            # идем по стандартным диагоналям
            if col != m and row != n:
                if col % 2 == 0:  # нечетные столбцы в матрице
                    k1 = col
                    k2 = 0
                    while k1 >= 0 and k2 <= col:
                        if k1 <= m and k2 <= n:
                            zigzag.append([k1, k2, matrix[k1][k2]])
                        k1 -= 1
                        k2 += 1
                else:  # четные столбцы в матрице
                    k1 = col
                    k2 = 0
                    while k1 >= 0 and k2 <= col:
                        if k1 < m and k2 < n:
                            zigzag.append([k2, k1, matrix[k2][k1]])
                        k1 -= 1
                        k2 += 1

                row += 1

        # ==================================================================
        # вторая часть при нечетном общем количестве столбцов в исходной матрице
        if n < m and (m % 2 != 0):
            row = n - 1
            for col in range(2, m - 2):
                if col % 2 == 0:
                    k1 = row
                    k2 = col
                    while k1 >= 0:
                        if k1 < n and k2 < m:
                            zigzag.append([k1, k2, matrix[k1][k2]])
                        k1 -= 1
                        k2 += 1
                else:
                    k2 = col
                    i = 0
                    j = col + (n - 1)
                    while i < n and j >= k2:
                        zigzag.append([i, j, matrix[i][j]])
                        i += 1
                        j -= 1
            zigzag.append([n - 1, m - 2, matrix[n - 1][m - 2]])
            zigzag.append([n - 2, m - 1, matrix[n - 2][m - 1]])
            zigzag.append([n - 1, m - 1, matrix[n - 1][m - 1]])

        # ====================================================================================================================
        # вторая часть при четном общем количестве столбцов в исходной матрице
        if n < m and (m % 2 == 0):
            row = n - 1
            for col in range(2, m - 2):
                if col % 2 == 0:
                    k1 = row
                    k2 = col
                    while k1 >= 0:
                        if k1 < n and k2 < m:
                            zigzag.append([k1, k2, matrix[k1][k2]])
                        k1 -= 1
                        k2 += 1
                else:
                    k2 = col
                    i = 0
                    j = col + (n - 1)
                    while i < n and j >= k2:
                        zigzag.append([i, j, matrix[i][j]])
                        i += 1
                        j -= 1
            zigzag.append([n - 1, m - 2, matrix[n - 1][m - 2]])
            zigzag.append([n - 2, m - 1, matrix[n - 2][m - 1]])
            zigzag.append([n - 1, m - 1, matrix[n - 1][m - 1]])
    # ====================================================================================================================
    # возвращаем полученную матрицу
    return zigzag