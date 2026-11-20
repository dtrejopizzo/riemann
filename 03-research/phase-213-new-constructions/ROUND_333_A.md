# Cancelación simultánea en las clases de máximo común divisor exacto

Sea S_q la contribución firmada de los pares n≠d con (n,d)=q a la energía de 325. En el mismo rango de 329, h=exp(−am)m^b, 0<a≤log 4 y b fijo, para todo A>0 fijo se tiene

    Σ_q |S_q| ≪_(a,b,A,η) h binom(2m,m) m^(−A).

**Prueba.** Basta acotar Σ b_q S_q uniformemente para |b_q|≤1, pues se puede elegir el signo de cada clase. Por inversión, b_(n,d) es la suma de c_g=(μ*b)(g) sobre los divisores comunes; |c_g|≤τ(g). Para cada g, el argumento de 331 antes de sumar los divisores da un techo absoluto fuera de diagonal O(h binom(2m,m)/g²) para los pares de múltiplos de g. Esto justifica el intercambio de sumas y limita la cola g>G a O(h binom(2m,m)(1+log G)/G), por Σ_{g≤t}τ(g)≤t(1+log t) y sumación parcial.

Para g≤G usar 329 con coeficientes μ(n)1_{g|n}. El máximo para la sumación parcial en el intervalo corto se toma ahora sobre subintervalos intersectados con gℤ; cada intersección es una progresión. La definición (1.3) de la estimación maximal incluye todas estas progresiones con el mismo conjunto excepcional; se emplea el insumo escalar de §1.1, (1.5) y el párrafo siguiente, tal como en 329. Por tanto la cota de la integral central de Gram conserva cualquier ahorro m^(−D) con constante uniforme en g. El tratamiento absoluto de los bordes, la diagonal central y la cola gamma de los pares distintos también pasa uniformemente pues se retiraron términos al estimar en módulo. Al separar la diagonal se obtiene O_D(h binom(2m,m)m^(−D)) para la contribución firmada fuera de diagonal de todos los múltiplos de g. [Artículo, definición del máximo y estimación escalar](https://arxiv.org/html/2411.05770v1)

Tomar G=m^(A+2) y D=3A+6. La suma de |c_g| hasta G es ≤G(1+log G); con estos parámetros ambos errores satisfacen la cota enunciada.

**Consecuencia.** La clase q=1 de 332 tiene masa absoluta exponencial para 0<a<log 4. Su desequilibrio entre aportes positivos y negativos, como fracción de esa masa, decae más deprisa que cada potencia fija de 1/m (usar el piso h4^m/m y aumentar D). Por tanto ambas masas son asintóticamente iguales ya entre pares coprimos. La prueba permite elegir signos independientes para todas las clases antes de sumarlas. Queda abierta la mejora exponencial que exige 326.
