# Cancelación relativa demostrada en la banda de pares que aún exige cancelación exponencial

Para cada 0<a<log 4 fijo, con la notación de 325–326 y h=exp(−am), se tiene incondicionalmente

    P_m(a) ∼ h binom(2m,m) (∫η)²/[ζ(2)²∫η²],       E_m(a)=o(P_m(a)).

Por tanto las masas de los pares con producto de Möbius positivo y negativo (ésta en módulo) son cada una asintóticas a P_m(a)/2. El o(1) es para a fijo. Es una aplicación al peso de 325 del teorema de Matomäki y Radziwiłł sobre funciones multiplicativas reales acotadas en casi todos los intervalos cortos. [Artículo original, Annals of Mathematics](https://annals.math.princeton.edu/2016/183-3/p06)

**Transferir el teorema a esta ventana.** Para f=μ o μ² sea c_f respectivamente 0 o 1/ζ(2), por el PNT o por el recuento de libres de cuadrados. Para b,B fijos con a<b<2<B, uniformemente sobre bloques [Y,2Y] con log Y entre bm−O(1) y Bm+O(1), el promedio cuadrático de

    (hx)^(−1) Σ_n f(n) η(log(x/n)/h) − c_f∫η

tiende a cero. En efecto hY→∞ uniformemente. El teorema citado, el límite de la media larga de f y la acotación |f|≤1 dan convergencia en media cuadrática para los promedios aditivos hacia atrás de cada longitud fija en el bloque comparable a hY (la misma conclusión hacia atrás se obtiene por traslación de la variable y error de bordes O(h)). Para detallar el paso a longitud dependiente de x, aproximar η uniformemente por una función escalonada a precisión ε. Cada extremo de sus intervalos en n se escribe x−x(1−exp(−hu)) con u fijo. Redondear cada longitud a una malla de paso ε' hY; sólo hay O(1/ε') longitudes para todo el bloque y el error de cada extremo normalizado es O(ε'+1/(hY)). Para un número fijo de pasos primero tomar m→∞, luego ε'→0 y por último ε→0. Aplicando el mismo recuento a f=1 se obtiene el factor ∫η (el jacobiano local es exp(−hu)). La uniformidad en los bloques se deduce también por el criterio secuencial del teorema, ya que tanto Y como cada longitud positiva de la malla crecen uniformemente.

**Integrar los bloques con el peso correcto.** Para cualquiera de las dos energías, la expresión exacta es

    (h∫η²)^(−1) ∫ |Σ_n f(n) l_m(n) η(log(x/n)/h)|² dx/x.

En la región central bm≤log x≤Bm, l_m(n)/l_m(x)=1+O_b(h) para n en el soporte, por derivación logarítmica. El peso de integración después de normalizar el promedio es h x l_m(x)² dx/∫η². En cada bloque diádico central x l_m(x)² varía por un factor acotado independientemente de m, también por derivación logarítmica. El error cuadrático medio uniforme del párrafo anterior se suma, por tanto, como o(1) de la integral total de ese peso. Para los bloques extremos se puede usar el bloque entero y la misma cota. Los promedios normalizados están uniformemente acotados, de modo que esto controla también la diferencia de sus cuadrados.

Fuera de esa región usar |f|≤1, la diagonal de 326 y la desigualdad entre producto y media de cuadrados usada allí. El coste está acotado por O(Δ_m) (o por la misma diagonal sin μ²) más O(h Σ n l_m(n)²) restringida a log n fuera de [bm+O(h),Bm−O(h)]. La diagonal es despreciable porque a<log 4. La suma restringida es exponencialmente menor que binom(2m,m): por comparación integral y unimodalidad su integral en u=log n es la cola de u^(2m)exp(−u)/(m!)² fuera de un intervalo que contiene 2m con margen proporcional a m. La cota de Chernoff para esa densidad gamma basta; el error de discretización por el máximo es también exponencialmente menor. La integral completa de x l_m(x)² dx es binom(2m,m). Esto prueba ambas afirmaciones.

**Una distinción cuantitativa.** Un cociente E_m/P_m que tiende a cero aún puede tener raíz de orden 2m tendente a uno. En cambio, si para un solo a fijo en este tramo se demostrara R(a)≤2 exp(−a/2−δ) con δ>0, el piso de 326 obligaría a Θ≤3/2−exp(δ)/2<1. Incluso esa mejora parcial implicaría una franja fija sin ceros, uniformemente a todas las alturas. Para RH sigue pendiente R(1/j)≤1 para todo j. El teorema de intervalos cortos da cancelación relativa genuina y no suministra por este argumento una ganancia en el exponente.
