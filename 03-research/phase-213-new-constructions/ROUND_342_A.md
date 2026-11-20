# Una segunda dilatación cancela la densidad de cada cociente por separado

Escribir A_h(x)=S_h(x)−2S_h(x/2) como en 338. Usar ahora C_h(x)=A_h(x)−2A_h(x/4), siempre con el mismo h=X^(−δ). Para δ=1/j, j≥16, su criterio de segundo momento sigue siendo equivalente a RH: el factor adicional de Mellin 1−2·4^(−s) tiene todos sus ceros en Re s=1/2, y permanece acotado en las franjas de 337. El argumento inverso de 337 funciona con los nuevos coeficientes acotados y preserva todos los polos a la derecha de 1/2.

En C_h se puede retirar con error puntual o(√(Xh)) el conjunto entero de cocientes de altura hasta X^ρ, para cada

    0<ρ<1/6−7δ/6.

En particular ρ=1/12 funciona simultáneamente como elección de exponente para cada δ=1/j, j≥16 (las constantes pueden depender de j). A diferencia del exponente δ/4 de 341, este exponente permanece positivo al tender δ a cero.

**Cortes coordinados.** En A_h(x) usar la versión corta de 338 con D=2√X real, P=X^(1−5δ/4) y L=P/D, es decir L<d,e≤D, de>P. En A_h(x/4) usar D/2, L/2, P/4. Para ambos sigue siendo válida la identidad truncada pues D²≥2X y (D/2)²≥2X/4. Los peines borrados tienen longitud al menos constante por X^(δ/4) en ambos casos y el error de Poisson es O_B(X^(−B)). El corte k≤K=⌈2X/P⌉ sirve para ambos. Los cortes reales resuelven exactamente la correspondencia de intervalos de integración sin requerir igualdad de extremos enteros.

**Cancelación previa a la suma.** Fijar r,s coprimos y d=gr, e=gs. Si en el primer término el intervalo continuo de g es J, en el segundo es exactamente J/2. Para cada k, el cambio g'=g/2 da

    ∫_J W_x(kg²rs) dg = 2 ∫_(J/2) W_(x/4)(k(g')²rs) dg'.

La densidad aritmética c_(rs) de 341 es la misma a ambas escalas. Por tanto su contribución desaparece para cada k,r,s individual, antes incluso de usar el signo alternado de k. El error de reemplazar cada recuento por su integral cuesta O(τ(rs)√(D/max(r,s))) por 341, porque el extremo superior de J es a lo sumo D/max(r,s). Los intervalos vacíos no contribuyen. Para R=X^ρ hay a lo sumo 2v pares de altura v, luego la suma de v^(−1/2) con esas multiplicidades es O(R^(3/2)). Tras sumar k y usar τ(rs)=X^o(1), el coste es

    O(X^(1/4+5δ/4+3ρ/2+o(1))).

El exponente es estrictamente menor que (1−δ)/2 bajo la condición anunciada. Esto prueba la cota incluso si se toman módulos de los errores por r,s,k.

**Límite actual.** La resta cuadrática aprovecha que la variable común g entra por g² y conserva los posibles polos relevantes. Se controla una franja incondicionalmente mayor de cocientes; siguen pendientes aquellos donde los dos factores reducidos pueden ser de tamaño próximo a √X.
