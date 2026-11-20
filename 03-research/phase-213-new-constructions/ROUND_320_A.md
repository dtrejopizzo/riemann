# Banda polilogarítmica con promedios locales positivos recombinables

En cada bloque X=2^k grande poner L=log X, D=⌊L⌋, j₀=⌈L⌉ y N=C₀ D L² para una constante absoluta suficientemente grande. Sea ν la ley de las uniformes independientes de 047, con longitudes l_i=1/[i(i+1)], y ν_> la ley de la suma de las de índices i>j₀. Es una probabilidad en [0,1/(j₀+1)]. Para X≤x≤8X definir

    T_X(x,t)=∫ C_t(x exp(u)) dν_>(u).

Existen pesos firmados explícitos g(n)(1−ψ(n/N)) para los que, uniformemente en esa banda y 0≤t≤2,

    T_X(x,t)+J_X(x,t)=O_ε(X^(1/2+ε)),
    J_X(x,t)=Σ_(D<n<2N)g(n)(1−ψ(n/N)) T_X(x/n,t).

En esta fórmula el mismo núcleo congelado define T_X también a argumentos menores. RH equivale al techo O_ε(X^(1/2+ε)) para ∫₁²(−J_X(x,t))₊dt en todos estos bloques. Se necesitan sólo índices entre ⌊log X⌋ y O((log X)³). El promedio local de la muestra principal es positivo en sus pesos y su ventana tiene ancho relativo O(1/log X). El signo de los coeficientes de la suma intermedia sigue siendo libre.

**La criba.** Poner a(d)=μ(d) para d≤D, a(2D)=−2D Σ_(d≤D)μ(d)/d y cero en el resto. Entonces Σ a(d)/d=0, Σ|a(d)|=O(D log(2D)) y g=1*a tiene g(1)=1, g(2)=…=g(D)=0. La media completa contra T_X tiene techo de raíz por 309, pues el sumatorio de 1*c_t es U de 317 y los a(d) cuestan sólo potencias de L. Para ψ tomar la función de distribución de ν evaluada en v−1: vale cero hasta 1 y uno desde 2.

**Una cota con el orden de derivación creciente.** Escribir S_J(w)=ν_>((w,∞)) con J=j₀. Su derivada de orden k tiene norma suprema ≤[2(J+k+1)²]^k. Basta derivar k de las uniformes conservando la función de supervivencia de las demás: cada derivada es una diferencia de dos masas de norma total 2/l_i. Quedan infinitas uniformes y la derivación distribucional da la cota clásica. La misma prueba con J=0 sirve para ψ. Para cada m≤8eX/N definir F_m(v)=ψ(v/N)S_J(log(mv/x)) en v>0, extendida por cero a la izquierda. Su soporte está en [N,8eX/m]. Para j≥1,

    ||F_m^(j)||₁ ≤ O(X) [C(J+j+1)²/N]^j.

En efecto, en v≥N la derivada de orden b de S_J(log(mv/x)) es v^(−b) por una combinación de las primeras b derivadas con coeficientes de Stirling de primera especie. El polinomio de sus módulos es z(z+1)…(z+b−1), que en z=2(J+j+1)² vale ≤(z+j)^b. Leibniz, las cotas de ψ y la longitud del soporte prueban la desigualdad con C absoluto.

En la cola con ψ intercambiar los coeficientes c_t(m). Poisson aplicado a cada Σ_l F_m(dl) elimina el modo integral al sumar en d. La suma de los demás modos está acotada por O(||F_m^(j)||₁) Σ_d |a(d)|d^(j−1) para j≥2. Tomar j=⌈L⌉. Como d≤2D, al sumar en m el error total queda ≤O(X³)(C' D L²/N)^j, usando |c_t(m)|≪_ε m^ε y absorbiendo las potencias logarítmicas. Elegir C₀ con C'/C₀<exp(−6). Queda O(X^(−2)), margen suficiente para la identidad. Esto controla el orden creciente en lugar de sustituir formalmente δ por cero en 319.

**Por qué el promedio positivo corto sigue detectando ceros.** Bajo RH rige el techo en módulo de 317. Para la recíproca tomar x∈[X,2X] y promediar T_X(x exp(v),t) respecto de la ley de la cabeza i≤j₀. Todos los centros caen en [X,8X]. Por independencia se recupera exactamente ∫ C_t(x exp(w))dν(w), con la misma ley fija en todos los bloques. La convexidad de la parte positiva transfiere el techo a este promedio fijo sin multiplicar la constante. Su Mellin es el de C_t multiplicado por ∫exp(sw)dν(w), salvo una función entera por el extremo inferior. Ese factor no se anula en Re s>0: es el producto convergente de (exp(s l_i)−1)/(s l_i), y Σ l_i<∞. La localización en t y Landau de 317 detectan por tanto cualquier polo exterior. Esta prueba sólo usa pesos no negativos en la observación local y en la recombinación.

**Antecedentes y límite.** El núcleo y su producto ya aparecen en 047; 049 también usa cancelación del modo integral y corrección de la densidad. El paso adicional es separar cabeza y cola dependientes del bloque para conservar exactamente el detector de polos mientras se reduce la ventana observada, con el sumatorio ordinario C_t de 317. Falta la estimación unilateral de J_X. Reducir a un número polilogarítmico de índices no demuestra esa estimación.
