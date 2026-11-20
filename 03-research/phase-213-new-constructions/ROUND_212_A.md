# Umbral de estabilidad del corte primo a escala lineal

En 208 el contorno de altura 1 da el corte log X=2N log M₁. En 211 la obstrucción de borde a escala √N era subexponencial, invisible en la raíz N-ésima de 210. Aquí, incluso en las tasas verificadas 3≤u≤4, ciertos cortes producen un falso crecimiento EXPONENCIAL en N. Se identifica el umbral de estabilidad frente a corrimientos acotados del extremo. Las afirmaciones siguientes son a tasa u fija.

Escribir l(a)=log M_a(u), v(a)=l'(a), F(a)=l(a)−(a−1/2)v(a). Hay una única a* en (1/2,1) con F(a*)=0. En efecto l es estrictamente convexa y su serie en a² tiene coeficientes positivos en todos los grados positivos: l'(a)=(1/√(1−4a²/u²)−1)/a. Así F(1/2)>0, F(1)<0 (cada monomio a^(2k) contribuye en 1 con factor 1−k), y F'=(1/2−a)l''. Poner v*=v(a*). Es el mínimo de l(a)/(a−1/2) sobre 1/2<a≤1 y es estrictamente menor que 2 log M₁. Para cualquier u≥3 el corte Nv*+O_u(1) conserva toda la suma prima infinita con error O_u(1/√N); para pendientes mayores el error es exponencialmente pequeño. Esto mejora el corte a tasa fija del criterio 208–209.

**Perfil en la frontera.** Para 0<a≤1 sea x_a>0 el punto máximo positivo de |H(x+ia)| dado por 208. Los dos máximos ±x_a son estrictamente cuadráticos: el máximo en q de la fracción racional de 208 tiene segunda derivada negativa y dq/dx=2x_a≠0. Escribir h=log H localmente en x_a+ia. Por Cauchy–Riemann y la ecuación de punto máximo, h'=−i v(a); Re h''<0. Para cada d real fijo, inversión sobre el contorno y expansión en (x−x_a)√N dan

    √N exp(−Nl(a)+a(Nv+d)) c_N(Nv+d;u)
        = Re[K exp(iNθ+ix_a d)] + o(1),
    K=√(2/π)/√(−h''),   θ=arg H(x_a+ia)+x_a v.

Se toma la raíz de parte real positiva. En cada vecindad domina una gaussiana tras reescalar y los términos lineales de orden √N se cancelan. El otro pico aporta el conjugado por simetría; el complemento es exponencialmente menor por integrabilidad y separación de ambos máximos. La misma cota absoluta de contorno con factor 1+|x+ia| da, para N≥3 y t≥0,

    |c_N(t;u)|+|c'_N(t;u)| ≤ C_(a,u) exp(Nl(a)−at)/√N.

En particular Chebyshev y sumación parcial en la cola con a=a*>1/2 prueban la afirmación de corte anterior.

**El extremo genera una señal prima.** Fijar L=Nv(a)+c con c constante. Para a<1/2 tomar B la suma prima hasta exp L; para a>1/2 tomar B la cola estrictamente posterior. Sustituir dθₚ(x) por dx (θₚ es la función de Chebyshev) en el peso x^(−1/2)c_N(log x;u). Después de multiplicar por √N exp(−Nl(a)−(1/2−a)L), el error de borde es o(1) por PNT y la cota de contorno. La integral del error por partes queda dominada en r=|log x−L| por C exp(−|a−1/2|r)|θₚ(x)/x−1|, con x≥1; converge a cero por dominación. Para dx usar el perfil anterior con d=c±r y el mismo mayorante sin el error de PNT. Resulta

    √N exp(−Nl(a)−(1/2−a)L) B
      = Re[K exp(iNθ+ix_a c) J]+o(1),

con J=1/(1/2−a+ix_a) para la suma inicial y J=1/(a−1/2−ix_a) para la cola. KJ≠0. Entre los dos extremos c=0 y c=π/(2x_a), al menos uno da para cada N suficientemente grande un módulo ≥C exp(NF(a))/√N, por las dos fases en cuadratura.

**Consecuencia y salvedad.** En 3≤u≤4 la suma completa es o(1) por 209 y su prueba de cola. Luego, para cada pendiente v en (0,v*) excepto v(1/2), al menos uno de esos dos cortes iniciales tiene módulo exponencial en N, con exponente F(a)>0, donde v=l'(a). Para a>1/2 se resta la cola al total. Por tanto ninguna pendiente estrictamente inferior a v* garantiza estabilidad para TODOS los cortes de pendiente a lo sumo v* que estén por encima de ella: siempre hay pendientes intermedias que fallan. Para la pendiente exacta v(1/2) el argumento de dominación pierde el decaimiento en r y no decide. Tampoco se deduce una cota inferior para cada fase individual. El crecimiento espurio ya aparece con los ceros locales verificados; no puede usarse como indicador de fallo del signo. Queda abierta la estimación superior de la suma completa.
