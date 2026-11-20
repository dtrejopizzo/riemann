# Una media positiva del saldo completo mantiene el techo de raíz tras cribar los divisores

Sea B_t(v)=Σ_(m≤v)b_t(m) la suma completa de 292. Para cualquier conjunto finito P de primos, incluso elegido según x, poner

    T_P(x,t)=Σ_(n≤x; p∤n para todo p∈P) τ(n) B_t(x/n),

donde τ cuenta divisores. Para todo σ∈(1/2,1) se tiene incondicionalmente

    |T_P(x,t)| ≤ C_σ x^σ ∏_(p∈P)(1+p^(−σ))²,

uniformemente en 0≤t≤2, x≥2 y P. En particular, aun retirando todos los divisores que contengan algún primo ≤Y, con Y=(log x)^(2+o(1)), el saldo integrado con estos pesos discretos satisface O_ε(x^(1/2+ε)). Se mantiene con coeficiente uno la contribución individual B_t(x).

**Primero, la media sin cribar.** Su serie de coeficientes es D_t(s)ζ(s)²=G_t(s)² L(s−it,χ)L(s+it,χ) por 292. Los coeficientes de cada L tienen sumas parciales O(log(2v)) uniformes en la banda por sumación parcial del carácter no principal. La hipérbola de Dirichlet divide el producto en dos sumas cortas de longitud √v y el rectángulo de intersección. Por tanto el sumatorio de los coeficientes del producto de las dos L es O(√v log(2v)+log²(2v)). Convolucionar con los coeficientes de G_t² cuesta su norma absoluta con peso n^(−σ), uniformemente finita por 294. Se deduce |T_∅(v,t)|≤C_σ v^σ para v≥1.

**Después, los divisores admitidos.** La serie de sus pesos es ζ(s)²∏_(p∈P)(1−p^(−s))². El polinomio finito que multiplica a la media anterior tiene norma absoluta ponderada exactamente ∏_(p∈P)(1+p^(−σ))², lo que da el techo afirmado por convolución. Incluso es posible reducir parcialmente el peso de cada primo: reemplazar el factor finito por (1−a_p p^(−s))², con 0≤a_p≤1. Los pesos finales siguen siendo positivos o nulos ya que cada factor local se obtiene al cuadrar 1+(1−a_p)Σ_(e≥1)p^(−es). Se obtiene el mismo techo con a_p p^(−σ) en el producto de normas. Las constantes no dependen de cuántos primos ni de qué niveles de reducción se hayan elegido.

**Escala de la criba.** Para P contenido en [2,Y], el logaritmo del coste es O_σ(Y^(1−σ)/log(2Y)) por Chebyshev y sumación parcial. Dado ε>0 pequeño tomar σ=1/2+ε/2. Si Y=(log x)^(2+o(1)), el logaritmo del coste es o(log x), de modo que el techo es O_ε(x^(1/2+ε)). Más generalmente, para Y=(log x)^A, A>0 fijo, se obtiene O_(A,ε)(x^(max(1/2,1−1/A)+ε)). Para A>2 la propia norma absoluta con todos los primos retirados tiene logaritmo comparable a Y^(1−σ)/log Y, por el PNT, así que esta estimación por módulos no alcanza la raíz para σ suficientemente cercano a 1/2. Esto limita el argumento empleado y no la cancelación real del polinomio.

**Diferencia con la meta.** T_P es una suma firmada con pesos no negativos, no una suma de partes positivas. Para P=[2,Y]∩primos la identidad deja B_t(x) más las dilataciones B_t(x/n) con todos los primos de n mayores que Y. El techo probado ya paga la suma entera a escala de raíz; falta un piso para esas dilataciones si se quiere extraer el techo unilateral para B_t(x). La cancelación formal por ζ² figuraba en 292 y 294. El enunciado aquí es una estimación uniforme para la familia de medias aritméticas después de retirar divisores.
