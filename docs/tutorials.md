Este proyecto implementa la cuadratura Gaussiana para aproximar integrales definidas en el intervalo `[0, π]`.

## ¿Qué hace el código?

- Usa polinomios de Legendre de grado 1 a 10.
- Evalúa la integral de `sin(x**2)` usando la cuadratura gaussiana.
- Muestra cómo cambia la aproximación a medida que se incrementa el grado del polinomio.

## Estructura del código

El archivo contiene las siguientes funciones:

- `gaussxw(N)`: Obtiene los puntos de muestreo y pesos para un polinomio de Legendre de grado `N`.
- `gaussxwab(a, b, x, w)`: Escala los puntos y pesos al intervalo `[a, b]`.
- `func(varInd)`: Define la función `sin(x²)` a integrar.
- `integrar(func, x, w)`: Aplica la cuadratura gaussiana.
- `iterar(func)`: Evalúa la integral para valores de `N` de 1 a 10.

## Ejemplo

```{python}
from integral.senintegral2 import gaussxw, gaussxwab, func, integrar, iterar

def func(varInd):
    return np.sin(varInd**2)

datos = iterar(func)

print(datos[1])

import matplotlib.pyplot as plt

plt.plot(datos[0], datos[1], 'o')
plt.xlabel("Valores N")
plt.ylabel("Valores de la integral")
plt.show()

```
