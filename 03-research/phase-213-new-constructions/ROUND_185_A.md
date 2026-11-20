# Qué tamaño debe tener una muestra que detecte desalineación en toda la banda

En la escala crítica de 184, N=exp(2T−2D), G=exp(exp T), D fijo. Consideramos el módulo del promedio ponderado de p^{it} para N≤p≤eN. Se trata exclusivamente de certificados que reemplazan el promedio por una sola muestra fija con pesos no negativos independientes de t.

**Obstrucción para muestras pequeñas.** Sean p_1,…,p_m primos distintos de ese intervalo, con pesos arbitrarios w_j≥0 de suma uno. Para K≥2 fijo, si

    m[K log(eN)+log K] ≤ (log G)/2,

existe t∈[2G,3G] con Re Σ w_j p_j^{it} ≥ cos(π/(K+1))−o(1), uniformemente en la selección y los pesos. Para una brecha ε fija puede tomarse K de orden 1/√ε, con 1−cos(π/(K+1))<ε/2. En particular toda muestra de tamaño ≤c_ε exp(T)/T admite una frecuencia con módulo >1−ε. La frecuencia puede cambiar al cambiar la muestra.

**Prueba en la banda prescrita.** Tomar b_r proporcional a sin((r+1)π/(K+1)) para 0≤r<K, normalizando Σb_r²=1. Formar R(t)=∏_j Σ_r b_r p_j^{irt}. Por factorización única, la media diagonal de |R|² es uno. La de p_j^{it}|R|² es Σ_{r<K−1}b_r b_{r+1}=cos(π/(K+1)), por la recurrencia del seno con extremos cero. En ambas expansiones la suma de módulos de coeficientes es ≤K^m por Cauchy–Schwarz. Los cocientes de enteros que representan frecuencias no nulas tienen numerador y denominador ≤(eN)^{mK+1}; por tanto el módulo del promedio de cada oscilación en un intervalo de longitud G es ≤2(eN)^{mK+1}/G. El error conjunto es ≤2(eN)G^(−1/2)=o(1). Promediar con la densidad |R|² y tomar un punto al menos tan grande como el promedio demuestra la obstrucción.

**Cuándo una muestra sí reproduce todo el promedio.** Para 0<ε<1/2 existe una muestra con repetición de O(ε^(−2)log(2+G/ε)) primos que aproxima uniformemente en error absoluto ε el promedio complejo de 184 en la banda [G,4G]. Esto incluye las correcciones de frecuencia de 184 para T grande. Muestrear independientemente con probabilidades proporcionales a log p; quitar la fase común N^{it} deja exponentes log(p/N)∈[0,1]. Tanto el promedio verdadero como el empírico tienen derivada de módulo ≤1. En una red de paso ε/8, Hoeffding aplicado a las partes real e imaginaria da probabilidad ≤4 exp(−c m ε²) de error >ε/2 en cada nodo. La unión sobre O(1+G/ε) nodos tiene probabilidad <1 con la constante indicada, y la derivada extiende el control a la banda. Es un resultado de existencia de muestra, sin cota nueva para el valor del promedio original.

La recurrencia del peine en 081 permite alturas arbitrarias. El argumento aquí impone [2G,3G] y admite que el número de primos crezca con la ventana. La coherencia de P47 prop:wit-coh y los momentos de 181 no dan un certificado puntual de desalineación de estas muestras. El resultado acota el alcance de sustituir el bloque de 184 por pocos primos. Sigue abierta la desalineación del bloque completo.
