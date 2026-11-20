# Interpolación del peine primo en los nodos cuartos

En la reducción 121–122 se pueden sustituir todos los datos primos por dos momentos de cada intervalo entre cuartas potencias consecutivas. La sustitución es simultánea para los vectores del espacio de prueba. No necesita una estimación de primos en intervalos cortos.

Sea X=exp(2T), F real normalizado de soporte en [−T,T] con extensión por cero en H¹ y ||F'||₂≤B. Sean c su autocorrelación y f(v)=v^(−1/2)c(log v). Para v≥1 se tiene |f''(v)|≤C(1+B²)v^(−5/2): el factor entre paréntesis en la derivada segunda es c''−2c'+3c/4, y las cotas respectivas son B², B y 1 por Cauchy–Schwarz. En particular c'' es la autocorrelación negativa de F', continua, también donde termina el soporte. Así f y su interpolación se pueden considerar sobre toda la semirrecta sin crear un salto artificial en X.

En cada celda [m⁴,(m+1)⁴] sea If la interpolante lineal por los extremos. La longitud es O(m³), luego |f−If|≤C(1+B²)/v allí. Fuera de las celdas que tocan [1,X] ambas funciones valen cero. Para la medida firmada dD=Σ_p(log p)δ_p−dv resulta

    |∫(f−If)dD| ≤ C(1+B²)(1+log X).

En efecto cada banda diádica aporta O(1+B²) por Chebyshev para la masa prima y por integración para la masa continua. El extremo superior de la última celda es O(X). La misma prueba vale para dD restringida al bloque (X^a,X], tomando los momentos sólo de la porción de celda incluida. Por afinidad, ∫If dD en cada celda sólo usa ∫dD y ∫v dD, con los bordes asignados una vez. Equivalentemente se distribuye la masa en sus dos nodos con pesos baricéntricos. Al tratarse de una cota uniforme de cuadráticas, es una cota de norma de la diferencia de las matrices simétricas, con factor 2 para la convención de 121.

Por 121 y 122, tomando N=ceil(T log log(T+4)), B=πN/T, el mayor autovalor positivo del bloque así interpolado conserva la tasa del bloque original (usar log(1+parte positiva)). Basta acotar ese exceso por exp(o(T)) sobre alguna sucesión no acotada. El beneficio concreto es la libertad de redistribuir los primos dentro de cada celda conservando los dos momentos; todo el detalle restante de sus posiciones cuesta a lo sumo O((1+B²)(1+T)). Falta la comparación unilateral para los momentos efectivamente producidos por los primos. El número de celdas crece como X^(1/4).

Cotejo: 039 y 044 ya usan cuartas potencias e interpolación para una discrepancia escalar; aquí se interpola la función de prueba de cada vector y se controla el error en norma. R166_702 ya desplaza primos para estudiar sistemas de Beurling. No se afirma novedad de la interpolación lineal ni de la idea de desplazar primos.
