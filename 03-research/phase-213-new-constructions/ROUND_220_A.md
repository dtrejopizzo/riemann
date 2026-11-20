# Balance incondicional y frecuencia condicional de las excursiones de signo

Usar la muestra aritmética compleja C_k de 217. Fijar un ángulo real φ, un umbral λ>0 y una progresión k=qn+b, q entero positivo. En cada bloque M<n≤M+H con H≤M, H/√M→∞, contar por separado

    P: Re(exp(−iφ) C_k)>λ,      D: Re(exp(−iφ) C_k)<−λ.

Incondicionalmente (#P−#D)/H→0. Más precisamente, bajo RH ambas fracciones son eventualmente cero; si falla RH, cada una tiende a 1/2. En particular es suficiente demostrar para UNA dirección, UNA progresión y UNA sucesión de tales bloques que la frecuencia de excursiones negativas tiene liminf inferior a 1/2. No hace falta una estimación sobre el tamaño de los valores extremos. Demostrar únicamente que los excesos positivos y negativos se equilibran NO discrimina el signo global: ese balance se cumple en ambos casos.

**Prueba.** Bajo RH, 217 da C_k→0. Fuera de RH, su equivalencia compleja y la fase del factor beta dan, módulo 2π,

    arg C_k=π + k log r₀ + Θ√k + o(1),      |C_k|→∞,

pues w₀ tiene argumento −Θ y K_(k²)(s_k) tiene fase o(1). En cada progresión esta fase se equidistribuye en el círculo, incluso si log r₀/(2π) es racional. Para verificarlo en los bloques indicados, fijar un armónico entero m≠0 y poner f(n)=m[(qn+b)log r₀+Θ√(qn+b)]. El incremento Δf(n) es monótono y tiende a mq log r₀. Si el límite no es múltiplo de 2π, Σ exp(if(n))=O_m(1) en el bloque. Si es múltiplo de 2π, la distancia de Δf al múltiplo es comparable a 1/√M en todo el bloque por Θ>0, q fijo y H≤M. Entonces la suma es O_m(√M). Las constantes pueden depender de Θ,q,b,r₀. Ambos techos salen directamente de sumar por partes la identidad exp(if(n))=(exp(if(n+1))−exp(if(n)))/(exp(iΔf(n))−1): el recíproco tiene parte real constante −1/2 y parte imaginaria monótona mientras los incrementos permanecen entre múltiplos consecutivos de 2π. Por tanto su variación es O(1) u O(√M), respectivamente. El o(1) de fase en 217 altera el promedio normalizado en o(1). Dividir por H y aplicar el criterio de Weyl prueba la equidistribución.

La fase de C_k distribuye así la mitad de los índices en cada semicírculo. Para imponer λ>0 y rotar por φ, excluir primero un entorno fijo de los dos extremos del semicírculo, usar |C_k|→∞ uniformemente en la cola, y hacer tender a cero el tamaño del entorno excluido. Esto da los límites afirmados. También se obtiene la dicotomía para densidad natural por bloques diádicos, aplicando el mismo argumento de sumas exponenciales a [1,M] o sumando los límites de bloques.

**Lectura aritmética.** 207 obtenía signos negativos infinitas veces para una tasa racional dependiente del hipotético cero, mediante una rotación que podía ser periódica. Aquí se observa la misma muestra prima fijada de antemano en cada orden y se obtiene una frecuencia exacta de excursiones por encima de un umbral fijo en ambas direcciones. La curvatura Θ√k que resulta del peso de 217 elimina la posible resonancia. La estimación incondicional de la diferencia de conteos es una consecuencia de la dicotomía espectral; no constituye evidencia a favor de ninguna de sus ramas. Se mantiene pendiente una estimación prima que distinga la frecuencia cero de la frecuencia un medio.
