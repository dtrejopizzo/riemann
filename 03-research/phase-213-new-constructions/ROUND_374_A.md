# Coste de las capas de alta multiplicidad en el corte exacto

**Estado: PROVED, revisado independientemente, incluidos el empacado y los redondeos.**

Sea A_K(x) la masa gaussiana positiva de 368 sobre enteros libres de cuadrados sin primos ≤L² que tienen al menos K factores primos, L=log x, h=log L. Para 0<c<1/2 fijo y K=ceil(cL/h),

    limsup log(1+A_K(x))/L = 1−c.

Para cualquier K=(1/2+o(1))L/h se tiene A_K(x)≤x^(1/2+o(1)). Por tanto estas últimas capas pueden retirarse de S sin afectar el criterio unilateral de exponente de 372.

**Techo uniforme.** Para s=1+1/L se cumple g(u)≤C exp(su), por completación del cuadrado con C absoluto para L≥1. Si H=Σ_p p^(−s)≤log ζ(s)≤log(1+L), el producto sobre k primos distintos tiene masa de Dirichlet ≤H^k/k! por ordenación. Luego A_K≤Cx^s Σ_{k≥K} H^k/k!≤2Cx^s(eH/K)^K cuando K≥2eH. Al tomar logaritmos, el término factorial ahorra (c+o(1))L para K=(c+o(1))L/h.

**Piso aun para cualquiera de las dos paridades.** Elegir enteros k→∞ de la paridad deseada, P=k^(1/c), y formar productos de k primos distintos de [P,2P]. Por el PNT hay N≫P/log P candidatos. Los logaritmos de los productos están en un intervalo de longitud k log 2; alguna celda de longitud ≤1 contiene ≥binom(N,k)/O(k) productos diferentes. Sea L el punto medio de esa celda y x=exp L. Tenemos L=(k/c)log k+O(k), de donde log L=log k+log log k+O_c(1). Más precisamente,

    k−cL/log L = (1+o(1)) k log log k/log k →∞,
    P/L² ≍_c k^(1/c−2)/(log k)² →∞.

Así k≥ceil(cL/log L) y todos los primos elegidos superan L² eventualmente. No se requiere redondear P ni x a enteros. Cada producto cobra un peso acotado por debajo por una constante positiva, pues |log(x/n)|≤1/2. Como binom(N,k)≥(N/k)^k, el logaritmo del aporte es ≥(1/c−1)k log k−O_c(k log log k)=(1−c−o(1))L. Esto prueba el limsup. Las escalas para las dos paridades pueden diferir; no se deduce un piso para su diferencia.

**Uso.** Tomando por ejemplo K=floor(L/(2h)−L/h^(3/2)), la contribución firmada de k≥K cuesta a lo sumo x^(1/2+o(1)) en módulo. Por tanto, para cada σ>1/2 y cada signo, el techo unilateral O(x^σ) es equivalente antes y después de retirarla; no se afirma que se conserve un signo puntual. Bajar el umbral a cL/h con c fijo menor que 1/2 e intentar pagar todas esas capas en módulo ya cuesta x^(1−c−o(1)) en una subsucesión. La estimación deja sin controlar la cancelación en k<K.

**Cotejo.** 369 trata cortes grandes mediante una comparación firmada de capas; aquí se usa el corte exacto y se cuantifica el límite de pagar en módulo. Los antecedentes internos más próximos para el piso son 293, «Piso para cada signo», y 356, «Optimalidad del exponente»: ambos seleccionan productos de primos distintos y usan binom(N,k)≥(N/k)^k. Es el mismo mecanismo combinatorio básico, aplicado aquí a primos por encima del corte y seguido por un empacado en una celda logarítmica para mantener el peso gaussiano. La búsqueda en las notas de investigación y el índice no encontró un antecedente exacto del enunciado limsup de esta cola; no se afirma novedad histórica. La revisión independiente confirmó la inyectividad por factorización única, el factor O(k) de celdas y que el margen en el redondeo del umbral tiende a infinito.
