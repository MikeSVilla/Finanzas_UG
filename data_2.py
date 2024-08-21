import numpy as np

def mp1(dimension=10, data_initial=1, position_initial=(1, 1)):
    # Crear la matriz con la dimensión correcta
    data_matrix = np.zeros((dimension, dimension))

    # Ajustar los índices de la posición inicial para ser cero-indexados
    x_initial = position_initial[0] - 1
    y_initial = position_initial[1] - 1

    # Asignar el valor inicial en la posición indicada
    data_matrix[x_initial, y_initial] = data_initial

    # Llenar hacia la derecha desde la posición inicial
    for j in range(y_initial + 1, dimension):
        data_matrix[x_initial, j] = data_matrix[x_initial, j - 1] + 1

    # Llenar hacia la izquierda desde la posición inicial, si se cumple la condición
    if y_initial > 0:
        for j in range(y_initial - 1, -1, -1):
            data_matrix[x_initial, j] = data_matrix[x_initial, j + 1] - 1

    # Llenar hacia abajo desde la posición inicial
    for i in range(x_initial + 1, dimension):
        data_matrix[i, y_initial] = data_matrix[i - 1, y_initial] - 1

    # Llenar hacia arriba desde la posición inicial, si se cumple la condición
    if x_initial > 0:
        for i in range(x_initial - 1, -1, -1):
            data_matrix[i, y_initial] = data_matrix[i + 1, y_initial] + 1

    # Llenar el resto de la matriz, incluyendo los valores menores solo si la condición se cumple
    for i in range(dimension):
        for j in range(dimension):
            if data_matrix[i, j] == 0:
                if i > x_initial:
                    data_matrix[i, j] = data_matrix[i - 1, j - 1]
                elif j > y_initial:
                    data_matrix[i, j] = data_matrix[i - 1, j - 1]
                elif (i < x_initial or j < y_initial) and (x_initial > 0 or y_initial > 0):
                    data_matrix[i, j] = data_matrix[x_initial, y_initial] - abs(x_initial - i) - abs(y_initial - j)

    return data_matrix
