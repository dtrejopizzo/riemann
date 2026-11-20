# Separación necesaria de los extremos binomiales en un ajuste de coste de raíz

Sea x entero, N=2x y g el peso de 267. Agrupar coeficientes reales a_(n,k) por extremo n≤N, con 1≤k≤n/2 por simetría. Escribir V_n=Σ_k |a_(n,k)|. Si la respuesta R coincide con g(p/x) en todos los primos p≤N, entonces para todo ε fijo en (0,1/3), con H=x^(1/6+ε), se tiene para x suficientemente grande

    Σ_n (H+N−n)V_n ≫ x.

En particular, con un único extremo N se requieren ≫ x^(5/6−ε) unidades de variación, aun permitiendo coeficientes arbitrarios. Si todos los extremos están en [N−D,N], el coste es ≫ x/(H+D). Esto descarta un coste x^(1/2+o(1)) para D≤x^(1/2−η), con cualquier η>0 fijo.

**Tres primos próximos a tres posiciones.** Por 267 hay un intervalo cerrado I de longitud positiva, interior a (2/3,1), y c>0 con |g(2r)−g(2−r)|≥2c en I. Para todo t∈xI salvo un conjunto de medida o(x) elegir primos p,q,s en los intervalos de longitud H que empiezan respectivamente en t, 2t y N+1−t. Esto usa el teorema de los números primos en casi todos los intervalos cortos de longitud X^(1/6+δ); se puede tomar δ=ε/2 y cubrir las tres regiones mediante un número fijo de tramos diádicos. Cada cambio afín de variable conserva la estimación o(x) para la medida excepcional. Por continuidad, |R(q)−R(s)−R(p)|≥c: p queda debajo de x, q y s encima.

**Efecto de cada extremo.** Sea A_n(u)=Σ_(k≥u) a_(n,k) para argumentos enteros positivos. Por compacidad de I elegir η₀>0 pequeño y fijo. Para n≥N−η₀x, las fórmulas de conteo de 267, aplicadas con extremo n, dan exactamente

    R_n(q)=A_n(n+1−q),     R_n(s)=A_n(n+1−s),
    R_n(p)=A_n(n+1−2p)−A_n(p).

En efecto q,s están entre n/2 y n, y p está entre n/3 y n/2 con margen proporcional a x. Para los tres primos y n en ese rango, todos los argumentos de las colas mostradas son positivos y ≤⌊n/2⌋+1. Las dos diferencias de colas se acotan por suma de |a_(n,k)| en dos intervalos. El primero está centrado en n+1−2t con radio 3H; el segundo en t con radio N−n+2H. Al integrar en t, cada k cuenta en un conjunto de medida O(H+N−n), por las pendientes −2 y 1 de los centros. Estas mayoraciones sólo dependen de t y H; la elección de los primos no exige independencia. Para extremos n<N−η₀x se usa |R_n(q)−R_n(s)−R_n(p)|≤3V_n porque los acarreos valen cero o uno; al integrar cuesta O(x V_n)=O((N−n)V_n). Sumando las mayoraciones e integrando sobre los t buenos se obtiene la desigualdad anunciada.

**Alcance.** La prueba también tolera un error uniforme menor que c/6 por primo tomando c para la separación exacta. No usa ajuste en compuestos, condición escalar de entropía, ni restricciones de signo o de suma de coeficientes. Para familias con extremos suficientemente separados la desigualdad deja abierta la construcción de 262. La entrada externa se limita a la existencia de primos en casi todos los intervalos; la deducción sobre los extremos es una comparación de tres respuestas del acarreo. [Enunciado del resultado sobre intervalos cortos en las notas de K. Matomäki](https://math.mit.edu/~drew/MITNT/KaisaMatomakiSlides.pdf).
