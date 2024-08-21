## Librerias

import numpy as np
    
    '''
    Para el primer y segundo problema se generara una funcion que posea tres parameters, el
    primero funciona para saber la dimensionalidad de la matriz deseada, el segundo es el 
    valor inicial para generar la matriz y el ultimo es una dupla que contiene la posicion
    inicial del valor inicial. 
    '''

def matrix_prob(dimension = 10, initial_value = 1, position_initial = (1, 1)):
  """
    Generadora de matrices que poseen cada elemento posee la siguiente condicion
    vx_i,j+1 = x_i,j + 1 y x_i+1,j = x_i,h - 1
      
    
    Parametros:
    
    dimension (int, float): Es la dimensionalidad de la matriz.
    initial_value (int, float): Valor que inicial que se asignara.
    position_initial (int, float): Posicion de la matriz donde se asignara el valor inicial.
  
    Retorna:
    int, float: Una matriz de n dimension.
  """
        
  # Primer paso. Se genera una matriz de ceros.
  data_matrix = np.zeros((dimension, dimension))
    
  # Segundo paso. Se ajustan los indices de la posicion inicial.
  # Nota se puede resta una unidad ya que python se comienza del 0 y no del 1.
  x_initial = position_initial[0] - 1
  y_initial = position_initial[1] - 1
      
  # Tercer paso. Asigna el valor inicial en la posicion deseada.
  data_matrix[x_initial, y_initial] = data_initial
      
  # Cuarto paso. Comienza a generar los elementos de la matriz, desde la posicion incial hacia la derecha.
  for j in range(y_initial + 1, dimension):
    data_matrix[x_initial, j] = data_matrix[x_initial, j - 1] + 1
      
  # Quinto paso. Si la posicion inicial es diferente a (1, 1) de la matriz, 
  # entonces se generaran los elementos del lado izquierdo de la posicion incial.
  if y_initial > 0:
    for j in range(y_initial - 1, -1, -1):
      data_matrix[x_initial, j] = data_matrix[x_initial, j + 1] - 1

  # Sexto paso. Comienza a generar los elementos de la matriz por columna, desde la posicion incial hacia abajo.
  for i in range(x_initial + 1, dimension):
    data_matrix[i, y_initial] = data_matrix[i - 1, y_initial] - 1

  # Septimo paso. Si la posicion es diferente a (1 , 1) de la matriz,
  # entonces se generaran los elementos del arriba de la posicion incial.
  if x_initial > 0:
        for i in range(x_initial - 1, -1, -1):
            data_matrix[i, y_initial] = data_matrix[i + 1, y_initial] + 1

  # Octavo paso. Llenar el resto de la matriz, incluyendo los valores menores solo si la condición se cumple
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
