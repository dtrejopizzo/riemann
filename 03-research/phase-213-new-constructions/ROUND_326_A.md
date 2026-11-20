# Cuándo la proximidad de los pares paga por sí sola el presupuesto

Mantener η,K,l_m de 325. Para a>0 fijo usar ahora h=exp(−am), escribir E_m(a) para la energía firmada, P_m(a) para la suma con |μ(n)μ(d)| y R(a)=limsup E_m(a)^(1/(2m)). Entonces

    RH ⇔ R(1/j)≤1 para todos los enteros j≥1,
    lim P_m(a)^(1/(2m)) = max(1,2 exp(−a/2)).

En a≥log 4 el techo subexponencial ya vale incondicionalmente, incluso en módulo término a término. En a>log 4 la energía firmada es asintótica a la diagonal. En 0<a<log 4 la masa absoluta crece exponencialmente: el mero recuento de pares no alcanza. La frontera log 4 es la de la estimación por módulos, no un umbral demostrado para la energía firmada.

**Detección con ventanas exponenciales.** Se conserva la representación de 325 como integral positiva de |A_m(t)|². En un intervalo fijo de alturas, la densidad W_m es ≥c exp(−am) para todo m grande. El argumento local de convergencia de Taylor de 325 da ahora

    R(a) ≥ exp(−a/2)/(3/2−Θ).

En efecto, el paso de la norma ponderada a la integral local de |A_m| pierde como máximo exp(am/2) por Cauchy–Schwarz. Si Θ>1/2, algún a=1/j suficientemente pequeño da R(a)>1. Bajo RH, para todo r<1 y todo η₀>0 se tiene |A_m(t)|≪_(r,η₀)r^(−m)(2+|t|)^η₀ por Cauchy y la cota clásica para 1/ζ en cada semiplano cerrado estrictamente a la derecha de 1/2 bajo RH (la misma empleada en 292). La norma cuadrática ponderada de esa potencia cuesta O(h^(−2η₀)); por tanto R(a)≤r^(−1) exp(aη₀). Tomar primero η₀→0 y luego r→1 prueba la dirección directa. A una sola anchura fija, el piso mostrado sólo garantiza detección para Θ>3/2−exp(−a/2).

**Cota por módulos.** Para cada n el número de d distintos con 0<|log(d/n)|<h es ≤C h n: a cada lado se cuentan enteros a distancia positiva ≤(exp(h)−1)n. Usar 2l_m(n)l_m(d)≤l_m(n)²+l_m(d)² y simetría. El coste absoluto fuera de la diagonal queda ≤C h Σ_n n l_m(n)²≪h 4^m/√m. En la última estimación, la integral correspondiente a Σ(log n)^(2m)/n² es (2m)! y el error por unimodalidad se acota por una constante por el máximo. La diagonal Δ_m es comparable a 1/√m: más precisamente al usar Σ_(n≤v)μ(n)²=v/ζ(2)+O(√v) por inversión de cuadrados, se obtiene

    Δ_m ∼ (2m)! / [ζ(2) 2^(2m+1)(m!)²].

El error tras sumación parcial se acota integrando √v por el módulo de la derivada de (log v)^(2m)v^(−3): después de dividir por (m!)² se gana exponencialmente, por las integrales gamma con parámetro 5/2 en lugar de 2. Así para a>log 4 la cola absoluta es o(Δ_m), y en el extremo a=log 4 se obtiene O(1/√m) para toda la energía.

**Piso por ocupación.** Para 0<a<log 4, poner Y=exp(2m). En [Y,2Y] hay ≫Y enteros libres de cuadrados. Partir ese intervalo en O(1/h) celdas de largo logarítmico ≤c₀h, eligiendo c₀>0 con K≥1/2 en [−c₀,c₀]. Cauchy–Schwarz aplicado a la ocupación de las celdas da ≫hY² pares ordenados en la misma celda. Borrar la diagonal cuesta O(Y), despreciable ya que a<log 4<2. En esa banda l_m(n)≥(2m)^m/[m!(2Y)^(3/2)]. Por Stirling el aporte absoluto es ≫ h 4^m/m. Junto con el techo anterior y la diagonal esto prueba el límite anunciado. El razonamiento sólo requiere densidad de libres de cuadrados en [Y,2Y], sin asumir que estén distribuidos en cada intervalo corto.

En particular, en el bloque que genera el piso, la distancia ordinaria de los pares es O(Y^(1−a/2)): para cada a fijo se ha retirado una potencia real respecto de Y. El paso abierto consiste en acotar la suma con los signos de Möbius antes de tomar módulos, para a arbitrariamente pequeño y fijo.
