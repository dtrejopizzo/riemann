# Cota puntual para todos los cocientes reducidos de altura pequeña en 338

En 338 usar la versión con de>X^(1−δ−ε), ε=δ/4, y fijar 0<δ≤1/10. Sea R=X^(δ/4). Para x∈[X,2X], el aporte conjunto de todos los pares cuyo cociente reducido r/s=d/e cumple max(r,s)≤R tiene módulo

    ≪ h√X R + X^(1/4+7δ/4+o(1)) = o(√(Xh)).

En particular, la diagonal y un conjunto creciente de direcciones racionales pueden retirarse con error cuadrático medio o(Xh), sin hipótesis sobre los ceros. El rango δ=1/j con j≥10 basta en la equivalencia de 337.

**Prueba.** Combinar los dos pulsos como Σ_k (−1)^(k+1)W_x(kde) ya que la segunda copia retira dos veces los múltiplos pares. Basta k≤K=⌈2X^(δ+ε)⌉. Escribir d=gr, e=gs, (r,s)=1. Los cortes de 338 y el del producto equivalen a g en un intervalo J dentro de (0,D], independiente de k. El coeficiente en g es μ(r)μ(s)μ²(g)1_{(g,rs)=1}. Para Q=rs la suma de μ²(g)1_{(g,Q)=1} hasta z es c_Q z+O(τ(Q)√z) con 0≤c_Q≤1. En efecto se expande μ² con los divisores cuadrados: para (l,Q)=1 el recuento coprimo hasta z/l² es (φ(Q)/Q)z/l²+O(τ(Q)); la cola al completar la serie principal cuesta O(√z).

Para cada k la variación total en g del pulso cortado por J es O_η(1), por monotonía del argumento logarítmico. Sustituir la suma en g por c_Q veces la integral cuesta O_η(τ(Q)√D). Sumando los errores en módulo sobre los k y los pares r,s se obtiene O(K R² X^(1/4+o(1))) por la cota elemental de divisores.

En la integral cambiar g=√(x/(krs))exp(−hv/2). Para cada v del soporte de η, la condición g∈J delimita un intervalo en k, incluso después del corte k≤K. La suma alternada de k^(−1/2) en cualquier intervalo cuesta a lo sumo uno. El jacobiano da entonces un techo O_η(h√(X/(rs))) para el término principal de cada cociente. Sumando (rs)^(−1/2) hasta R en ambos índices se obtiene O(R). Para el primer coste el exponente es 1/2−3δ/4; para el segundo es 1/4+7δ/4+o(1). Ambos son estrictamente inferiores a 1/2−δ/2 en el rango enunciado.

**Qué aporta al criterio.** La estimación aprovecha simultáneamente los múltiplos pares e impares del mismo producto. Los signos verdaderos en cada cociente se reducen a un recuento de libres de cuadrados y el término de densidad se cancela en k. 331 identifica la constancia de signo a cociente fijo para otra energía de pares; aquí se demuestra una cota al tamaño requerido en el observable de 338. Quedan los cocientes de altura mayor que R, incluido el caso de dos factores coprimos grandes.
