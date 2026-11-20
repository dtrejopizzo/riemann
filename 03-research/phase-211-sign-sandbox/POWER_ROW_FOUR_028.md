# POWER_ROW_FOUR_028 — Cuarta fila completa de la tabla escalar

Estado: **PROVED**, revisión independiente por mapa aprobada y verificador PASS reproducido. Para TODOS k>=0 y TODOS u>=63/2,

    W[f_(4,k)]>(1/50)||f_(4,k)||²,
    F_(4,k)(s)=s^k/(s+u)^(4+k).                           (ROW4)

Se conserva TODO el peine y el polar. Papers intactos. No se extrapola a otras filas ni al signo global.

## 1. Corpus y razón nueva

Leídos las reglas del proyecto, INTERIOR017 (WRN), TABLE_DESCENT018 (filas2/3), sus auditorías y STATE027; consultados índice de rutas, grid maestro y CROSSWORD-TO-D.md sobre filas, derivadas gamma y pesos. La prohibición018 de sustituir una prueba universal por una campaña de filas se conserva: esta fila es el objetivo concreto autorizado028 y no se presenta como cierre. Las recurrencias solas no dan signo, como prueba el falsificador018.

La diferencia matemática frente018 es conservar la fórmula EXACTA de ARCH4, cuyo margen resulta pequeño pero positivo, y usar el peso racional eta12 en WR4 en lugar de fijar eta15. No es un barrido ni una búsqueda de otro N: una fórmula gamma y una elección analítica del peso producen un bound uniforme de la forma REAL para todo k y u. El signo alternado del polar se conserva; no se resta el polar positivo de los k pares.

## 2. Monotonías arquimedianas legítimas y fórmula exacta

Sea m(tau)=Re psi(1/4+i tau/2)−logpi. Por la serie de psi, m crece con |tau|. Para N fijo, normalizar la densidad tau^(2k)/(u²+tau²)^(N+k) y reescalar tau=u xi da una probabilidad en xi independiente de u. Luego ARCH_(N,k)/norm² crece con u por comparación punto a punto de m(u xi).

Al aumentar k, la probabilidad se repondera por xi²/(1+xi²), creciente en |xi|. La covarianza con m(u xi) es no negativa. Así para todo u>=u0=63/2 y k>=0,

    ARCH_(4,k)(u)/norm²>=ARCH_(4,0)(u0)/norm².             (MON)

Esto sólo usa ARCH, no movimiento de polos de la forma completa ni el lema global refutado007.

Ponga d(u)=psi((u+1/2)/2)−logpi. La integral de Poisson da I1=d(u)/(2u), y la recurrencia exacta I_(r+1)=−I_r'/[2ur] para el denominador (u²+tau²)^r permite calcular

    ARCH_(4,0)/norm²=d−u d'+(2u²/5)d''−(u³/15)d'''.       (A4)

La norma base es5/(32u^7). En u0, el argumento de psi es16. Usando psi^(r)(16) por sus series ABSOLUTAS,

    A4(u0)=H15−gamma−logpi−(u0/2)S2−(u0²/5)S3−(u0³/20)S4,
    Sp=sum_(j=16)^infty j^(−p).

Todos los Sp se restan. Por monotonía elemental,

    Sp<=sum_(j=16)^115 j^(−p)+115^(1−p)/(p−1).

El verificador Fraction y los intervalos explícitos003 de gamma/logpi prueban

    A4(u0)>11/400.                                       (ARCH)

El extremo115 es un corte de las tres series de funciones especiales con resto integral, no una muestra de parámetros k o u. MON extiende ARCH a TODOS los parámetros declarados sin calcular otra matriz ni otro átomo.

## 3. Peso eta12 y peine COMPLETO

El lema WRN017, válido para eta<u/2, prueba para toda k la cota

    ||e^(eta y)f_(4,k)||²/||f_(4,k)||²<=R4(u,eta),
    R4=(u/(u−eta))^7 S4(rho), rho=(eta/(u−eta))²,
    S4(rho)=(1+3rho−rho²+rho³/5)/(1−rho)^4.

La expresión se obtiene del producto diferencial017; equivalentemente,

    S4(rho)=sum_(l>=0)[(2l+1)(2l+3)(2l+5)/15]rho^l.

Esta última serie tiene coeficientes positivos, luego S4 crece con rho. Para eta12 fijo, u/(u−eta) y rho decrecen con u. Así R4(u,12)<=R4(u0,12)<400, comparación racional exacta con rho=64/169 y u0/(u0−12)=21/13.

Por Cauchy–Schwarz ponderado,

    |c_f(t)|<=sqrt(R4)e^(−12t)||f||².

Se controla TODA la contribución del peine por

    |PRIME|/norm²<40sum_(q>=2)Lambda(q)q^(−25/2).

Usar Lambda(q)<=logq y q^(−1/2)<=2^(−1/2)<5/7 permite comparar con una sola integral decreciente:

    |PRIME|/norm²
      <(200/7)2^(−12)[log2+2log2/11+2/121]
      <3/500.                                           (PRIME)

La última comparación usa log2<7/10 y Fraction. No se trunca Λ ni se descartan contactos adversos. La desigualdad f'(q)<0 para f(q)=q^(−12)logq,q>=2 se sigue ya de log2>2/3.

## 4. Polar alternado, uniforme en TODO k

Escriba c_k=binom(2k,k)/4^k. La integral beta da

    norm_(4,k)²=[5/(32u^7)] c_k/binom(k+3,3),
    POLAR_(4,k)=2(−1/4)^k/(u²−1/4)^(4+k).

Ponga q_u=1/(4u²−1) y p_40(u)=64u^7/[5(u²−1/4)^4]. Entonces

    |POLAR|/norm²=p_40(u) q_u^k binom(k+3,3)/c_k
                 <=p_40(u)(8q_u)^k.                      (P)

En efecto c_k>=2^(−k) por Vandermonde y binom(k+3,3)<=4^k por contar los histogramas de palabras de longitud k en cuatro letras. Ambos p_40(u) y q_u decrecen con u>1/2: la derivada logarítmica de p_40 tiene numerador−u²−7/4<0.

Para k PAR, el polar es positivo y no causa pérdida. Para k IMPAR>=1,8q_(u0)<1 y el verificador prueba

    |POLAR|/norm²<=p_40(u0)8q_(u0)<1/1000.                (POLAR)

Este bound no resta el polar de k0 ni lo sustituye por su máximo de todo k, que sería demasiado grande.

## 5. Forma completa y región nueva

Para toda k y u declarados, combinando ARCH, PRIME y POLAR,

    W[f_(4,k)]/norm²
      >11/400−3/500−1/1000
      =41/2000>1/50.

Así queda probado ROW4 con margen uniforme y con TODOS los términos de la forma explícita. El resultado cubre una fila completa adicional; no es una consecuencia formal de las otras filas ni de las identidades de filtros. Tampoco cierra la tabla de TODOS N,k requerida por SCALAR_BRIDGE017. No se afirma una nueva ventanaT por este resultado aislado.

Por la recurrencia completa018, en particular la TERCERA diferencia de la fila1 es estrictamente positiva para todo k, con el factor u^6 correspondiente. Más precisamente, si a_(N,k)=W[f_(N,k)],

    (−Delta)^3 a_(1,k)=u^6 a_(4,k)
      >3c_k/[160u(k+1)(k+2)(k+3)].

No se afirma completa monotonía de orden arbitrario.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_row_four_028_verify.py

El script ejecuta sólo comparaciones Fraction e intervalos de constantes elementales; PASS. La uniformidad en k y u pertenece a las demostraciones MON/WRN/P, no a un barrido numérico.
