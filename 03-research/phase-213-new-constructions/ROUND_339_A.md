# Una fase logarítmica compartida sobrevive al cuadrado del bloque

Para 0<δ<1/4 y h=X^(−δ), la cota de 338 para dos copias no se deduce de soporte libre de cuadrados, coeficientes reales acotados y ahorro de una potencia en las sumas de cada copia sobre **todos** los subintervalos (respecto de la longitud del bloque completo). Hay copias idénticas que cumplen esas propiedades y cuyo segundo momento en 338 es ≫(hX)². El criterio pide O_ε(hX·X^ε).

**Construcción.** Y=√X, I=[1.05Y,1.1Y], t=c/h con c>0 fijo suficientemente pequeño para que la transformada de Fourier de η no se anule en c. Poner b(n)=μ²(n) signo cos(t log(n/Y)) en I y cero fuera, con signo +1 en los ceros del coseno. Este intervalo cabe en el bloque de 338 para X grande. Para cualquier subintervalo J de I,

    |Σ_{n∈J} b(n)| ≪ Y/t + (1+t)√Y.

En efecto el recuento hasta v de libres de cuadrados es v/ζ(2)+O(√v). La función de signo tiene O(1+t) saltos, por lo que sustituir el recuento por su integral cuesta O((1+t)√Y). En la integral cambiar a u=log(v/Y); el signo periódico tiene media cero y primitiva O(1/t), y la variación del peso Ye^u es O(Y). Ambos términos de la cota dan un ahorro de potencia respecto de Y para cada δ fijo del rango indicado.

**Medición de la resonancia.** En [X,2X] el producto de dos miembros de I sólo activa el primer peine en k=1. Todos los pulsos W_x(de) están enteramente dentro de esa ventana para X grande, pues de/X está entre 1.05² y 1.1². Sea B(x)=Σ b(d)b(e) W_x(de). Integrando contra exp(−it log(x/X)) en dx/x se obtiene exactamente

    h hatη(c) [Σ_{n∈I} b(n)(n/Y)^(−it)]².

La parte real de la suma entre corchetes es Σ μ²(n)|cos(t log(n/Y))| ≫ Y. Para verlo, el error al pasar a la integral es O((1+t)√Y)=o(Y) por variación total; la función |cos| tiene media 2/π y el error de promediado en la integral es O(Y/t). Por Cauchy–Schwarz, ∫_[X,2X]|B|²dx/x ≫ h²Y⁴. Así hay un desequilibrio macroscópico incluso con ahorro en todos los intervalos ordinarios de las dos copias.

**Qué excluye.** Una prueba uniforme para coeficientes de bloque tratables sólo mediante esos límites de sumas parciales daría una estimación falsa. El ejemplo selecciona sus coeficientes según X; no es una función multiplicativa fija y no afirma resonancia de este tamaño para μ. Hace explícita la frecuencia t de orden 1/h que las dos copias pueden reforzar simultáneamente. El antecedente aritmético de bloque es 338; el ingrediente de fases n^(it) es el habitual de Mellin.
