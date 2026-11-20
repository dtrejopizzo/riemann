# Una criba positiva aísla la escala principal hasta cualquier umbral subpotencial

Para B_t de 309, x≥2 y 2≤D≤x, definir

    w_D(n)=τ(n)(Σ_(d|n, d≤D) μ(d))²,    S_D(x,t)=Σ_(n≤x) w_D(n) B_t(x/n).

Los pesos son no negativos, w_D(1)=1 y w_D(n)=0 para todo 2≤n≤D por inversión de Möbius. Para 1/2<σ<1 y η>0,

    |S_D(x,t)| ≪_(σ,η) x^σ D^(2(1−σ)+η),    0≤t≤2.

En particular D puede ser cualquier x^o(1), incluso exp(√log x), conservando el techo de raíz con pérdida arbitraria. Las dilataciones restantes sólo usan argumentos x/n<x/D. A diferencia de la criba por primos de 309, al superar D pueden reaparecer enteros con primos pequeños. Por ejemplo, en D<n≤2D todos los divisores propios son ≤D, y el peso es exactamente τ(n)μ(n)².

**Coste de la construcción.** Abrir el cuadrado y poner l=mcm(d,e). Para d,e libres de cuadrados, la serie de los pesos τ(n) con l|n es ζ(s)² por el polinomio ∏_(p|l)p^(−s)(2−p^(−s)); esto se comprueba sumando el factor local de τ sobre los exponentes positivos. Por tanto w_D=τ*h_D con h_D un polinomio de Dirichlet. En la norma absoluta de coeficientes con peso n^(−σ),

    ||h_D||_σ ≤ Σ_(d,e≤D; μ(d)μ(e)≠0) l^(−σ) ∏_(p|l)(2+p^(−σ)).

El producto es ≪_η D^η (l≤D² y 3^ω(l)≪_ν l^ν para todo ν>0). Descomponiendo d=gu,e=gv con g su mcd, la suma sin ese producto es ≤Σ_(g≤D)g^(−σ)(Σ_(u≤D/g)u^(−σ))² ≪_σ D^(2−2σ), pues Σ g^(σ−2) converge. Convolucionar h_D con la media sin cribar de 309 prueba el techo. La idea clásica usada es el cuadrado de una suma de divisores; aquí se evalúa cuánto cuesta, y cuánto debe costar, abrir una brecha en esta media del saldo.

**Optimalidad del exponente de la norma.** Supóngase que w=τ*h es cualquier otro sistema de pesos reales con w(1)=1, w(n)=0 en 2≤n≤D y w(n)≥0 en todo n. Se fuerza h(p)=−2 en p≤D. Para dos primos distintos p,q∈(D/2,D], se tiene w(pq)=4−4−4+h(pq)≥0, de donde h(pq)≥4. Hay ≫D²/log²D pares para D grande, de productos distintos salvo el orden. Por tanto

    ||h||_σ ≥ c_σ D^(2−2σ)/log²D.

La misma barrera vale para una norma truncada en x si D²≤x. En particular, para un hueco D=x^δ con 0<δ<1/2, todo argumento que sólo multiplique la cota x^σ de 309 por esa norma paga al menos x^(σ+2δ(1−σ)−o(1)). Al acercar σ a 1/2 la pérdida es una potencia x^δ. Así, optimizar los pesos dentro de esta clase sin explotar cancelación entre los coeficientes de h no lleva ese método a una brecha de potencia con error de raíz. Esto no impone un límite inferior al saldo aritmético S_D.

**Obligación restante.** Para D subpotencial el techo anterior ya controla B_t(x)+Σ_(D<n≤x)w_D(n)B_t(x/n) en módulo. Un piso de orden −x^(1/2+ε) para la cola, uniformemente o en la versión integrada pertinente, cerraría el techo unilateral de 292. Los pesos positivos y el hueco dejan abierta esa desigualdad.
