# Explanation
El código implementa la cuadratura de Gaussiana  para aproximar integrales definidas.

Se usa la función sin(x²) y se integra en el intervalo de 0 a pi.

Se calcula la integral usando diferentes grados del polinomio de Legendre, desde 1 hasta 10.

La función gaussxw da los puntos y pesos originales.

La función gaussxwab ajusta esos puntos y pesos al intervalo deseado.

La función integrar evalúa la aproximación de la integral con los valores dados.

La función iterar repite el cálculo para varios valores de N y devuelve los resultados.

Al final se grafica cómo cambia la aproximación con N.
