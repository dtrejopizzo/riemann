# Conservar momentos exactos de cada celda no basta si su número crece sin tasa

Para el modelo de 225 surge una pregunta previa a usar identidades de divisores: ¿basta controlar exactamente cualquier lista fija de momentos bajos por celda? En el orden lineal más corto, N=k (j=1), la respuesta es negativa incluso si se conserva un número de momentos que tiende a infinito sin tasa prefijada.

Existen pesos positivos λ_p→1 sobre los mismos primos y enteros M_n→∞ tales que en TODA celda n≤log p<n+1 los momentos sin redondear de órdenes 0,…,M_n son idénticos a los auténticos. Sin embargo,

    limsup log(1+|C_(k,1)(λ)−C_(k,1)(1)|)/k = log M_(1/2)(3)>0.

La muestra auténtica tiene tasa cero aquí por 224: d₁=arctan(1/2)−log(5/4)>arctan(1/28)≥Θ. El sistema modificado da por tanto tasa superior estrictamente positiva. No se programa la muestra en toda subsucesión ni se preserva el producto de Euler de ζ.

**Bloque que distingue los modelos.** Poner a=1/2, m=log M_a(3), v=∂_a log M_a(3), x=x_a(3) de 212. Fijar el orden k, N=k, n=ceil(Nv), e=n−Nv, d=log p−n. Usar I_k(L) de 218 con el orden cambiado a N=k y s=−√k+ik. Normalizar I_k(n+d) por el factor complejo

    F=3^(s−1) exp(Nm−an) N^(−3/2).

En d∈[0,1], I_k(n+d)/F difiere en o(1) uniforme del perfil

    g_φ(d)=exp(−ad)[K exp(iφ+ixd)J₊ + conjugado(K)exp(−iφ−ixd)J₋]/2,
    J₊=3/[v(a−ix)−i],   J₋=3/[v(a+ix)−i],   φ=Nθ+xe,

con K y θ de 212. En efecto el cambio u=3+r/N en la prueba de 216 conserva ahora el factor exp(ir/3) pues k/N=1. La escala de 216 y 212 dan el perfil real con corrimiento e+d+rv/3. La integración de cada rama con exp(ir/3−avr/3) produce J₊ y J₋. El corrimiento e queda en la fase y el factor exp(−a(e+d)) se ha normalizado en n. La envolvente del contorno domina por C exp(−cr); el indicador del corte converge a uno para cada r fijo ya que v<2 log M₁(3). Esta prueba no supone que el perfil complejo antes de la proyección sea real.

**Un momento que los datos elegidos no ven.** Fijar temporalmente un entero M. Usar en [0,1] la medida positiva empírica ν_n que asigna a cada d la masa exp(−n/2)(log p)/√p. Por PNT converge débilmente a exp(d/2)dd. En la norma compleja de esta medida proyectar I_k/F sobre el espacio de polinomios de grado ≤M. La norma del residuo queda separada de cero para todo k grande (con constante dependiente de M). En efecto las matrices de Gram convergen a una definida positiva. Ninguna g_φ es polinomio: es una combinación con coeficientes no nulos de dos exponenciales de exponentes distintos y no nulos; al derivar M+1 veces no se anula idénticamente. Por compacidad de la fase la distancia mínima al espacio es positiva. Esto se transfiere a ν_n por convergencia de todos los productos de los perfiles y los monomios, uniforme en φ (sólo aparecen finitos armónicos). Los polinomios proyectados y sus residuos tienen además supremo acotado uniformemente para M fijo, por acotación de las inversas de Gram y del perfil.

Tomar la parte real o imaginaria del residuo cuya norma L² sea mayor y llamarla R. Es real y ortogonal a todos los monomios hasta M. Perturbar los pesos de esa celda por λ_p−1=R(d)/(k(1+||R||∞)). Esto conserva exactamente los momentos de 225 hasta M, sin usar PNT para esa igualdad. El módulo del cambio de muestra en la celda es al menos c_M |F| exp(n/2)/k: la coordenada correspondiente del producto integrado de R con I_k/F es ∫R²dν_n. Como a=1/2 el factor exp(n/2) cancela exp(−an). Queda un piso exp(km−O(√k+log k)) por c_M. Para cualquier perturbación relativa uniformemente acotada el techo del limsup es m por el contorno de altura 1/2 y Chebyshev, como en 216; este techo absoluto no requiere t=o(N).

**Un único sistema de pesos.** En la etapa ℓ tomar M=ℓ y escoger k tan grande que la pérdida por c_M sea exp(o(k)), por ejemplo |log c_M|≤k/ℓ. Elegir la celda por encima del corte de todos los órdenes ya tratados. El efecto de los cambios anteriores, en un conjunto finito de primos, tiende a cero con k por 211. Los cambios posteriores no entran en los órdenes ya fijados. En las celdas alteradas poner M_n=ℓ y en las restantes M_n=n. Esto da M_n→∞, λ_p→1 y el limsup afirmado. No se demuestra aquí necesidad de la tasa específica n/log n suficiente en 225.

**Antecedentes y decisión.** 155–156 ya explican la pérdida de detección al usar identidades factoriales o un número fijo de derivadas de un peso de divisor. Aquí los momentos están en las posiciones de primos de cada celda y la obstrucción viene de una distancia estricta a un espacio de polinomios en una medida prima positiva. A diferencia de 221 y 223 se conservan todos los momentos bajos de cada celda y se cambia el orden cuadrático por lineal. Este ejemplo descarta obtener el techo mediante positividad de la medida y esos momentos solamente. No descarta las identidades aritméticas que relacionan momentos altos de distintas celdas.
