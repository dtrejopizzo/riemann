# POWER_RENORMALIZED_TAIL_042 — Cancelación global del afín y cola en escala absoluta

Estado: **PROVED**, revisión independiente aprobada en [POWER_RENORMALIZED_AUDIT_042.md](POWER_RENORMALIZED_AUDIT_042.md); verificador exacto PASS. u=63/2 fijo. Papers intactos. Signo W global OPEN.

## 1. Corpus y diferencia

Consultados ROUTES-TRIED-INDEX/README, grid maestro y CROSSWORD-TO-D; releídos MASS022, ARCH_CELL026, INTERIOR_SCALE030, GAMMA_WEIGHT031, CRITICAL_BALANCE040 y ENERGY_BAND041§7. La masa exacta y la sumación Euler por celdas ya existen; no se ofrecen como otra prueba de signo.

La diferencia cuantitativa frente041 es eliminar GLOBALMENTE el afín−gamma x mediante MASS antes de acotar el complemento. Se prueba que la cola del residuo renormalizado, desde el MISMO corte cercano a la energía de040, es exponencialmente pequeña en escala ABSOLUTA. El beneficio041 era relativo a una energía C_N posiblemente exponencial; no se suma ese beneficio aquí sin su contabilidad de bordes.

## 2. Normalización global sin Fubini crítico

Conserve J_N,h_N de022, J'=−h, sum_(n>=1)J(n)=1 y J(x)->0. Todos los integrales y sumas siguientes son absolutos para N fijo por022; no se integra una serie Euler en sigma1. Sea B1({x})={x}−1/2 fuera de enteros y conserve SAWTOOTH041

    B(x)=−gamma x−B1({x})logx+kappa+E(x),
    kappa=(1/2)log(2pi)−1/2, |E(x)|<=1/x.

La sumación Euler CELULAR con su borde1 da

    int_1^infty J(x)dx=1−J(1)/2+int_1^infty B1({x})h(x)dx.

Se puede probar sin fórmula de sumación externa: en cada(n,n+1), integrar B1 J'; los bordes son[J(n)+J(n+1)]/2 y el integral−int J. Sumar hasta un entero y pasar al límite. Los saltos de B1 quedan exactamente incluidos.

Integrando−xJ' y usando xJ(x)->0,

    int_1^infty xh(x)dx
      =1+J(1)/2+int_1^infty B1({x})h(x)dx.

En consecuencia, con F_N=2int hB,

    F_N/2=−gamma+(kappa−gamma/2)J_N(1)+R_N,
    R_N=−int_1^infty h_N(x)B1({x})(logx+gamma)dx
                            +int_1^infty h_N(x)E(x)dx. (RENORMALIZED)

Esta identidad por sí sola no prescribe signo. A continuación se controla una parte de R_N con precisión absoluta.

## 3. Resultado cuantitativo

Para TODOS N>=2^80, sea

    T=(N−1)/992+5, X=exp(T),
    R_N^tail=−int_X^infty h_N B1({x})(logx+gamma)dx
                                  +int_X^infty h_N E dx.

Entonces

    |R_N^tail|<=N(T+2)exp(−3T/2)<exp(−N/1000).       (ABS-TAIL)

El complemento completo es, por tanto, interior en la fórmula exacta

    W[g_N]/norm²
      =ARCH_sharp+2gamma−(2kappa−gamma)J_N(1)
                 −2R_N^inside+epsilon_N,
    |epsilon_N|<2exp(−N/1000),

con inside integrado de1 aX y con el mismo E REAL041. No se afirma signo de esa expresión interior ni que su margen sea mayor que el error.

## 4. Dilatación real y derivada completa del inverso

Ponga delta0=2000/N, v0=1/2+delta0 y t0=2(N−1)v0/(u²−v0²). El corolario040 prueba t0<T y q(t0)>v0. La monotonía de q da, para t>=T,

    q(t)>1/2+2000/N,
    rho(t+logm)<=rho(t)m^(−q(t)).

Por el integral elemental de una serie decreciente,

    sum_(m>=1)m^(−1/2)rho(t+logm)
       <=rho(t)[1+N/2000]<N rho(t)/1000.              (DILATION)

No se invoca cancelación de Möbius para este estimate. Es válido DESPUÉS de eliminar el afín; el peso residual permite aprovechar su ganancia adicional1/x.

Escriba g=rho/2−rho'=(1/2+q)rho, H=x^(−3/2)g(logx). Se tienen0<q<u,0<q'<M=u²/(2N−3)<1 y rho<=1. Por tanto

    |g|<=32rho,
    |g'−(3/2)g|
      =rho |q'−q(1/2+q)−(3/2)(1/2+q)|
      <=rho[1+(u+3/2)(u+1/2)]=1057rho<1100rho.

Derivar la serie absoluta022 h(x)=sum mu(m)mH(mx) es legítimo en la cola; el mismo mayorante domina sus derivadas. DILATION produce

    |h_N(x)|<=N x^(−3/2),
    |h_N'(x)|<=2N x^(−5/2), x>=X.                    (REAL-DECAY)

Estos bounds conservan TODOS los divisores. No se presupone h' negativo ni se deduce una monotonía no probada de h.

## 5. Primitiva periódica y borde inferior contado

Use Q2 de041, continua y periódica, Q2'=B1 casi por todas partes y||Q2||_infty=1/16. Si V(x)=logx+gamma, integración por partes da EXACTAMENTE

    R_N^tail=h_N(X)V(X)Q2(X)
       +int_X^infty Q2(x)[h_N'(x)V(x)+h_N(x)/x]dx
       +int_X^infty h_N(x)E(x)dx.                    (TAIL-BOUNDARY)

El borde infinito se anula por REAL-DECAY. Q2 no tiene saltos y los valores de B1 en enteros no cambian los integrales. El borde X se conserva, incluso cuando X fuese entero. No se supone que el error E tenga signo favorable.

Con0<gamma<1, REAL-DECAY y |E|<=1/x,

    |R_N^tail| <= (N X^(−3/2)/16)(T+1)
      +(N/16) int_X^infty x^(−5/2)[2(logx+1)+1]dx
      +N int_X^infty x^(−5/2)dx
    =N X^(−3/2)[(7/48)(T+1)+55/72]
    <N(T+2)exp(−3T/2).

Aquí se han contado todos los bordes y variaciones, incluidos los de la corrección periódica real.

## 6. Constante exponencial absoluta y alcance

T>N/992 y T+2<N para N>=2^80; por ello el último bound es menor que N²exp(−3N/1984). La desigualdad positiva de la exponencial

    exp(N/4000)> (N/4000)²/2>N

vale ya para N>32000000. Así N²<exp(N/2000), y

    3/1984−1/2000>1/1000

prueba ABS-TAIL sin evaluar un N ni una suma prima.

La obligación restante es el interior RENORMALIZADO y su balance con ARCH_sharp y J_N(1). A diferencia del coste energético041, el error aquí es absoluto y exponencialmente decreciente; no se identifica con un margen global ni se declara el interior favorable. La cancelación del afín se efectuó mediante MASS exacta, no por un Fubini crítico sum|mu|/m. No hay campaña de órdenes, contactos o precisiones.
