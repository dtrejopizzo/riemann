# POWER_ARCH_TRIPLE_004 — Cota de dimensión tres y límite exacto del método

Estado: PROVED cota de densidad; NUMERICAL diagnóstico de su insuficiencia; OPEN positividad arquimediana para todas las ternas de tasas >=31.5. No se obtiene falsificador de esa positividad.

Diferencia respecto del registro exterior/Pick: se ensaya una desigualdad de incertidumbre para una dimensión FIJA igual a tres, explotando polos reales con tasas inferiores acotadas. No se propone extrapolar casos finitos. Antecedentes consultados en POWER_BRIDGE_002 y POWER_POLYNOMIAL_003; no se toca ningún paper.

Para tasas u_j>=a, sea V=span{exp(-u_j y)1_(y>0)} de dimensión n<=3. La base ortonormal racional de Malmquist da exactamente el kernel evaluador sobre la recta de Fourier:

    Σ_j |phi_j(tau)|²=Σ_j 2u_j/(u_j²+tau²).

Los factores anteriores de Blaschke tienen módulo uno, de donde el resultado por suma. Cauchy–Schwarz aplicado a los coeficientes normalizados da

    |hhat(tau)|²/(2pi ||h||²) <= Σ_j u_j/[pi(u_j²+tau²)].

Para |tau|<=a, u/(u²+tau²) decrece en u>=a. Así la densidad es <=n a/[pi(a²+tau²)] en ese intervalo. La desigualdad persiste por continuidad en los límites confluentes, interpretados como y^k exp(-uy).

El símbolo m(tau) es par y estrictamente creciente en |tau|; esto se obtiene de la serie de digamma (cada término real tiene derivada positiva para tau>0). El principio de llenar desde frecuencias menores da por tanto

    arch[h]/||h||² >= (2n/pi)∫_0^R m(tau) a/(a²+tau²) dtau,
    R=a tan(pi/(2n)),

si R<=a, como ocurre para n=3. Basta observar que la densidad candidata satura su cap en [-R,R] y tiene masa total uno; en el exterior toda masa paga m>=m(R), y en el interior se usa el cap. No se necesita una cota exterior adicional.

Para a=31.5,n=3, cuadratura diagnóstica de esta integral con scipy da R=18.186533479473212 y cota -0.05064542812409753. No se presenta como certificado exacto: sirve para decidir que esta cota no da la positividad requerida. Mejorar discretización o aritmética no resolvería esa pérdida. Es más ajustada que reemplazar la densidad por la constante n/(pi a), pero todavía olvida la imposibilidad de saturar simultáneamente evaluadores en todo un intervalo.

Un ensayo numérico limitado a tasas log-separadas por >=.04 encontró el mínimo en el extremo de separaciones pequeñas, sin negatividad (valor aproximado .1932). Esto no demuestra monotonía ni cubre tasas confluentes. Una corrida sin separación mínima produjo un negativo espurio por mal condicionamiento de la Gram Cauchy; se descartó, y NO se usa como falsificador.

Residuo preciso: obtener una desigualdad colectiva que mejore el cap escalar al menos .051 en la peor terna, o demostrar que la menor eigenenergía arquimediana aumenta al separar tasas desde el límite confluente. Ninguno de ambos enunciados se ha probado aquí. El certificado de escalera fija de grados hasta cinco es otra tarea y no implica esa monotonía.
