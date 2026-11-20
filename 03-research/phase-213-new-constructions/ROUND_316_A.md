# Tres dilataciones cancelan el tramo de argumentos hasta una potencia fija

Sea D=x^o(1), D≥2, q=⌊D⌋+1 y w_D la criba de 310. Congelar D,q al evaluar en escalas distintas y formar los pesos firmados

    g(n)=w_D(n)−2q w_D(n/q)+q²w_D(n/q²),

interpretando los argumentos no enteros como peso cero. Con κ=77/285, para todo x suficientemente grande y uniformemente en 0≤t≤2,

    B_t(x) + Σ_(D<n≤x^(1−κ)) g(n) B_t(x/n) = O_ε(x^(1/2+ε)).

La muestra principal entra con coeficiente uno. La suma conservada evalúa B_t sólo en argumentos entre x^κ y x/D. Eliminar todos los argumentos menores que x^κ cuesta en total O_ε(x^(1/2+ε)), sin localizar cruces ni escoger el extremo según t. El resultado corresponde a una combinación firmada de las medias de 310; no conserva la positividad de sus pesos.

**Techo de la media completa.** El polinomio que modifica la criba es (1−q^(1−s))². El sumatorio ponderado en todas las dilataciones es S_D(x,t)−2q S_D(x/q,t)+q² S_D(x/q²,t). Por 310 en cualquier recta fija σ>1/2 la modificación multiplica el techo por (1+q^(1−σ))²=x^o(1). Resulta el techo de raíz con pérdida arbitraria. Como q>D, g(1)=1 y g(n)=0 en 2≤n≤D.

**Qué cancela la diferencia.** La serie de g es ζ(s)²k(s) con k=h_D(s)(1−q^(1−s))². Su polinomio finito está soportado hasta D⁴q²=x^o(1), tiene norma absoluta x^o(1) en cada abscisa fija no negativa (por 310 o su expansión por pares) y satisface k(1)=k'(1)=0 exactamente. Poner G(v)=Σ_(n≤v)g(n) y β=131/416. Para v≥D⁴q², convolucionar el asintótico del divisor con k anula por completo v log v y v: los coeficientes son k(1) y (2γ−1)k(1)+k'(1). Por tanto |G(v)|≪_η x^o(1) v^(β+η) para todo η>0. El único insumo externo adicional es la cota publicada para el error en el sumatorio de τ; los factores logarítmicos se absorben en η. [Huxley, Exponential sums and lattice points III](https://doi.org/10.1112/S0024611503014485)

**Transferencia a la cola firmada.** Para V=x^κ el intercambio de sumas da exactamente

    Σ_(x/V<n≤x) g(n)B_t(x/n)
        = Σ_(m≤V)b_t(m)[G(x/m)−G(x/V)].

Todos los argumentos de G superan su umbral de soporte para x grande. Los coeficientes |b_t(m)|≪_η m^η uniformemente, por los factores locales acotados y el soporte libre de cubos. Estimando ambos términos queda O_η(x^(β+O(η)+o(1)) V^(1−β)). Como β+κ(1−β)=1/2, la cola cabe en el presupuesto para cualquier ε>0. La misma prueba con cualquier exponente β<1/2 del problema del divisor permite κ=(1/2−β)/(1−β). La estimación para g se hace después de compensar entre las tres dilataciones: acotar las tres masas en módulo por separado perdería los dos ceros en 1.

**Lo pendiente.** Por 292, controlar la integral en t∈[1,2] de la parte negativa de la suma intermedia en el enunciado a escala x^(1/2+ε) equivale al signo global, ya que su opuesto difiere de B_t(x) en un error uniforme de ese orden. El recorte de 311 era positivo con un extremo adaptado, y el filtro diádico de 300 actuaba sobre la primera fila. Aquí q>D preserva la brecha inicial mientras elimina el tramo de potencia para todas las frecuencias. Falta pagar el intervalo intermedio.
