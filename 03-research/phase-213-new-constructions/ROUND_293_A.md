# Qué cofactores pueden retirarse a coste de raíz de la autoconvolución

Para b_t de 292, fijar A>1, 0≤δ<1 e y=(log x)^A. Sea r_y(n) el producto, con multiplicidades, de las potencias primas de n cuyos primos son mayores que y (producto vacío 1). En la región n≤x, r_y(n)≤x^δ, las masas positiva y negativa en magnitud de b_t satisfacen, cada una,

    Σ max(±b_t(n),0) = x^(1−(1−δ)/A+o(1)),

uniformemente para 1≤t≤2. Así, para 1<A≤2 y δ≤1−A/2 toda esa región se puede descartar de la suma ANTES de tomar su parte positiva en el criterio de 292. Para A=3/2 esto elimina todos los n cuyo cofactor por encima de (log x)^(3/2) sea a lo sumo x^(1/4). Para A=2 incluye todos los n construidos exclusivamente con primos hasta (log x)². Por encima de la frontera indicada cada signo por separado supera el presupuesto de raíz.

**Agrupamiento y techo.** Con u_p=1−Re(χ(p)p^(it))∈[0,2], los coeficientes locales de b_t en los niveles 0,1,2 son 1,−2u_p,u_p², y valen cero en los niveles superiores. Un paquete completo sin pesos suma (1−u_p)², pero un corte en x puede excluir sus niveles 1 ó 2. Para incluir todos esos bordes, factorizar n=d r con d formado por primos ≤y y r=r_y(n). Tomar σ=1−1/A>0. Entonces

    Σ |b_t(n)| ≤ x^σ ∏_(p≤y)(1+2p^(−σ))² · Σ_(r≤x^δ)|b_t(r)|r^(−σ).

Por Chebyshev y sumación parcial, el logaritmo del producto es O_A(y^(1−σ)/log y)=O_A(log x/log log x). Para el último factor basta |b_t(r)|≤4^ω(r)≤τ(r)²=r^o(1) en su soporte, uniformemente en t. Resulta el exponente σ+δ(1−σ) anunciado, también para δ=0.

**Piso para cada signo.** Para Z grande y cada t∈[1,2] hay ≫Z/log Z primos p en [.9 Z,Z] con u_p≥3/4, uniformemente. En efecto, elegir la clase no nula módulo 3 con signo χ opuesto al de cos(t log Z). A lo largo del intervalo el coseno varía a lo sumo 2log(10/9)<1/4. El teorema de los números primos en las dos clases fijas da el conteo. El primo excepcional 3 no interviene a escala grande.

Tomar k primos distintos de ese conjunto con Z=y, con k igual a la parte entera de (1−δ)log x/log y o un entero contiguo por debajo para ajustar la paridad. Si δ>0, multiplicar por un primo q de la misma construcción con Z=x^δ. Para δ=0 no usar q. Los productos quedan ≤x y tienen el cofactor exigido; diferentes elecciones dan enteros distintos. Cada coeficiente tiene el signo fijado por la paridad y módulo ≥1. Si M≫y/log y es el número de candidatos pequeños, M/k≫(log x)^(A−1); por tanto binom(M,k)≥(M/k)^k aporta x^((1−δ)(1−1/A)+o(1)) como piso de exponente. El primo grande, cuando corresponde, aporta además x^(δ+o(1)) elecciones. Hacer la construcción para las dos paridades prueba los dos pisos.

**Alcance.** La parte positiva es una función 1-Lipschitz: al borrar esta región en el rango admisible, su integral en t cambia a lo sumo x^(1/2+o(1)). El carácter sigue siendo el fijo módulo 3, sin hipótesis sobre ceros auxiliares. Los pisos por encima de la frontera descartan sólo pagar el borrado por suma de módulos; no descartan un ahorro por compensación entre ambas paridades. Falta la cota unilateral para los enteros restantes. El recuento de números lisos por Rankin es clásico; aquí se aplica con un cofactor permitido y se obtiene el exponente inferior de cada signo para los coeficientes reales del criterio, uniforme en frecuencia.
