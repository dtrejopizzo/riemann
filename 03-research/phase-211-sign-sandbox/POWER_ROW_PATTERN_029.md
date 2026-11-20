# POWER_ROW_PATTERN_029 — Región uniforme u²>=256N, k>=1

Estado: **PROVED**, revisión independiente por mapa aprobada y verificador PASS reproducido. Para TODOS enteros N>=2,k>=1 y TODA tasa real positiva u con u²>=256N,

    W[f_(N,k)]>(7/10)||f_(N,k)||²,
    F_(N,k)(s)=s^k/(s+u)^(N+k).                            (REGION)

Se conserva el peine COMPLETO y el polar. Sin campaña de N, papers intactos. El borde k0 se trata separadamente en BOUNDARY_WEDGE029 con una condición más fuerte sobre u.

## 1. Corpus y diferencia precisa

Leídos las reglas del proyecto, JOINT_SCALE016 y su auditoría (fracaso de pesos exponenciales uniformes con u fijo,N/u² grande), INTERIOR017 (WRN), TABLE_DESCENT018, ROW_FOUR028 y ROW_SPLIT028; consultados índice/grid/crucigrama sobre pesos centrados, cotas de filas y momentos beta. No se atribuye una prueba de signo a las identidades de filtros.

La diferencia frente016 y018 es doble: usar AMBOS pesos opuestos en Cauchy–Schwarz, cancelando el coste lineal Neta/u; y permitir u crecer como sqrt(N), conservando un coste uniforme en Neta²/u². El contraejemplo016 a uniformizar pesos con u fijo y N/u² sin cota NO pertenece a esta región. No se presenta la condición variable como un puente hacia la tabla completa de tasa FIJA u31.5. La nueva conclusión es una región explícita de W real en infinitos órdenes, sin certificados individuales por N.

## 2. Ganancia de la primera columna y fórmula arquimediana inferior

Si A_(N,k)(u)=ARCH_(N,k)/norm², la recurrencia Poisson de018 y las normas beta dan exactamente

    A_(N,1)=A_(N,0)+u A_(N,0)'.                            (GAIN)

La derivación usa I_(N+1)=−I_N'/[2Nu] y norm_(N,1)²=norm_(N,0)²/(2N). La ganancia es no negativa: al reescalar tau=u xi, el término uA0' es la media de tau m'(tau)>=0. GAIN no implica por sí sola un margen y no se extrapola a la forma completa.

Para obtener un bound CUANTITATIVO válido a órdenes variables probamos primero, para todo t real no nulo,

    Re psi(1/4+it)>=log|t|−9/(8t²).                       (PSI)

Prueba elemental: la fórmula de sumación de Euler, integrada una vez más mediante el polinomio periódico B2, es

    psi(z)=logz−1/(2z)−1/(12z²)
            +int_0^infty B2({x})/(z+x)^3 dx,
    |B2({x})|<=1/6,  Re z>0.

Para z=a+it, el módulo de los términos tras logz−1/(2z) es <=1/(4t²), pues |z|>=|t| y int_0^infty |z+x|^(−3)dx<=1/t². Aplicar en a5/4, usar log|z|>=log|t| y Re(1/(2z))<=5/(8t²), y restar Re[1/(1/4+it)]<=1/(4t²) por la recurrencia de psi, prueba PSI.

La probabilidad de q=tau²/(u²+tau²) es Beta(k+1/2,N−1/2). Por tanto

    Elog|tau|=logu+(1/2)[psi(k+1/2)−psi(N−1/2)],
    E tau^(−2)=(N−1/2)/[u²(k−1/2)]       (k>=1).

PSI con t=tau/2 da la desigualdad uniforme

    A_(N,k)>=log(u/(2pi))+(1/2)[psi(k+1/2)−psi(N−1/2)]
                       −9(N−1/2)/[2u²(k−1/2)].           (ARCH-GENERAL)

Este bound conserva una ganancia que no era accesible usando sólo el mínimo k0; el momento inverso necesario es finito desde k1. Para k>=1 el lado derecho crece con k. Usar psi(N−1/2)<=logN, psi(3/2)=2−gamma−2log2 y u²>=256N prueba

    A_(N,k)>=2log2−logpi+1−gamma/2−9/256>9/10.             (ARCH)

La última comparación se verifica con intervalos racionales003, sin evaluar otro N.

## 3. Cauchy–Schwarz con AMBOS pesos y simplificación uniforme

Para eta>0, la autocorrelación causal satisface

    |c_f(t)|<=e^(−eta t)||e^(eta y)f||·||e^(−eta y)f||.

WRN017 es válido en ambos signos del peso (la expresión sólo usa el cuadrado del segundo parámetro). Con rho_+=eta²/(u−eta)² y rho_−=eta²/(u+eta)²,

    ||e^(eta y)f||·||e^(−eta y)f||/norm²
      <=[u²/(u²−eta²)]^(N−1/2) sqrt(S_N(rho_+)S_N(rho_−)),
    S_N(r)=sum_(l>=0)B_l^(N)r^l,
    B_l^(N)=(N−1/2)_l/(1/2)_l.

El límite por coeficientes es elemental:

    B_l^(N)<=(2N−1)_l/l!,
    S_N(r)<=(1−r)^(−2N+1).

En efecto los cocientes sucesivos se comparan al multiplicar en cruz; la diferencia es (N−1)l>=0. De aquí, para u>2eta,

    |c_f(t)|/norm²<=e^(−eta t)
            [(u²−eta²)/(u²−4eta²)]^(N−1/2).              (CENTERED)

Ésta es una desigualdad del kernel real para TODO k, no una afirmación de positividad desde identidades. El producto elimina el término lineal de coste que aparecía en la cota de un solo peso.

## 4. Peine completo uniforme en la región

Fije eta4. Como u²>=256N,N>=2, el factor CENTERED es

    [1+48/(u²−64)]^(N−1/2)
       <=exp(48N/(224N))=exp(3/14)<14/11.

Así, usando TODOS los contactos,

    |PRIME|/norm²
      <(28/11)sum_(q>=2)Lambda(q)q^(−9/2)
      <=(28/11)(5/7)2^(−4)[log2+2log2/3+2/9]
      <4/25.                                            (PRIME)

Se usaron Lambda(q)<=logq, q^(−1/2)<=2^(−1/2)<5/7 y la integral decreciente de x^(−4)logx desde2. Las comparaciones finales son Fraction. No hay truncamiento aritmético ni hipótesis sobre el signo individual de contactos.

## 5. Polar alternado en N variable

Sea c_k=binom(2k,k)/4^k. Las fórmulas beta exactas son

    norm_(N,0)²=Gamma(N−1/2)/[2sqrt(pi)Gamma(N)u^(2N−1)],
    norm_(N,k)²/norm_(N,0)²=c_k/binom(k+N−1,N−1),
    POLAR_(N,k)=2(−1/4)^k/(u²−1/4)^(N+k).

Jensen para X de ley Gamma(N−1/2) da Gamma(N)/Gamma(N−1/2)=E sqrt(X)<=sqrt(N−1/2)<sqrtN. Por Bernoulli y u²>=256N,

    p_(N,0):=POLAR_(N,0)/norm_(N,0)²
      <=(4sqrt(pi)sqrtN/u)(1−1/(4u²))^(−N)
      <(9/20)(1024/1023).

Se usó sqrt(pi)<9/5. Como binom(k+N−1,N−1)<=N^k y c_k>=2^(−k),

    |POLAR_(N,k)|/norm²<=p_(N,0)[2N/(4u²−1)]^k,
    2N/(4u²−1)<=4/2047<1/500.

Para k PAR el polar es positivo. Para k IMPAR>=1, los dos bounds racionales prueban

    |POLAR_(N,k)|/norm²<1/1000.                            (POLAR)

No se resta la contribución positiva de los k pares ni se usa una constante que crezca sin control con N.

## 6. Forma real, frontera del patrón y coordinación del borde

ARCH, PRIME y POLAR dan para TODOS los parámetros de REGION,

    W[f_(N,k)]/norm²>9/10−4/25−1/1000
                    =739/1000>7/10.

Ésta es nueva cobertura real de W en un conjunto infinito de órdenes y tasas. No es una campaña por dimensiones ni un nuevo argumento de descenso formal.

La condición u²>=256N NO cubre todos los órdenes a u fijo: allí sólo garantiza N<=u²/256. En particular no cierra la tabla suficiente de u31.5. El momento E tau^(−2) usado en ARCH-GENERAL diverge en k0; eso limita esta prueba, no refuta el signo del borde. El constructor paralelo trata k0 por un bound real específico y una cuña más fuerte u>=64sqrtN, con el polar conservado, en POWER_BOUNDARY_WEDGE_029.md. Su resultado se combina sólo tras su propia prueba y revisión; no se presupone desde REGION.

No se afirma una nueva ventanaT ni el signo global del Paper47. El avance es la escala cuadrática explícita, manteniendo la forma gamma y el peine completo.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_row_pattern_029_verify.py

El verificador sólo compara constantes universales Fraction/intervalos; PASS. La uniformidad en N,k,u reside en las demostraciones anteriores, no en un barrido.
