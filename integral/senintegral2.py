from scipy.special import legendre
import matplotlib.pyplot as plt
import numpy as np

def gaussxw(N):
    """Usa numpy para extraer los pesos y los puntos de muestreo de la cuadratura gaussiana.

    Examples:
        >>> print(gaussxw(3))
        [-0.77459667  0.          0.77459667] [0.55555556 0.88888889 0.55555556]

    Args:
        N (int): Primer argumento, da el grado del polinomio de Legendre. 

    Returns:
        list: (1) Devuelve los puntos de muestreo.
        list: (2) Devuelve los pesos respectivos de los puntos de muestreo.

    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """Aplica la rutina vista en clase para escalar el intervalo de integración y devuele los puntos de muestreo y los pesos adaptados.

    Examples:
        >>> print(gaussxwab(0,np.pi,[-0.77459667  0.          0.77459667],[0.55555556 0.88888889 0.55555556]))
        [0.35406272 1.57079633 2.78752993] [0.87266463 1.3962634  0.87266463]

    Args:
        a (float): Límite inferior de la integral.
        b (float): Límite superior de la integral.
        x (list): Puntos de muestreo no escalados.
        w (list): Pesos no escaladod

    Returns:
        list: (1) Devuelve los puntos de muestreo escalados.
        list: (2) Devuelve los pesos escalados respectivos de los puntos de muestreo.

    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def func(varInd):
    """Evalua la función a integral en un punto dado.

    Examples:
        >>> print(func((np.pi/2)**(1/2)))
        1

    Args:
        varInd (float): Valor de x en el que se va a evaluar la función. 

    Returns:
       a (float): Función evaluada en el punto dado.

    """
    return np.sin(varInd**2)

def integrar(func,x,w):
    """Aplica cuadratura gaussiana a una función con puntos de muestreo y pesos dados.

    Examples:
        >>> print(integrar(func,[0.35406272 1.57079633 2.78752993], [0.87266463 1.3962634  0.87266463]))
        1.8503636166558148

    Args:
        varInd (float): Valor de x en el que se va a evaluar la función. 
        func (function): Función a integrar.
        x (list): Puntos de muestreo de la cuadratura gaussiana.
        w (list): Pesos respectivos a los puntos de muestreo de la cuadratura gaussiana

    Returns:
        float: Función evaluada en el punto dado.

    """
    return np.sum(func(x)*w)

def iterar(funcGen):
    """Calcula el resultado de la cuadratura gaussiana de una función dada para polinomios de Lagendre de grados entre 1 y 10.

    Examples:
        >>> print(iterar(func))
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1.9611893306991126, 0.4444055098839264, 1.8503636166558148, 0.3635354764094303, 0.7858090342523546, 0.7886218902294921, 0.7702887018119796, 0.7725895134091216, 0.7726873847372616, 0.7726500262612431])

    Args:
        funGen (function): Función para la que se integra. 

    Returns:
        list: Lista que tiene en su primer índice los valores de N y en su segundo índice los resultados de la cuadratura gaussiana para el valor de N respectivo.

    """
    x=[1,2,3,4,5,6,7,8,9,10]
    y=[0]*10
    for i in range(1,11):
        x_4,w_4=gaussxw(i)
        x_4,w_4=gaussxwab(0,np.pi,x_4,w_4)
        y[i-1]=integrar(func,x_4,w_4)
    return x,y

datos= iterar(func)
print(datos[1])

plt.plot(datos[0], datos[1], 'o')
plt.xlabel("Valores N")
plt.ylabel("Valores I")
plt.show()
