# POWER_BOUNDARY_BALANCE_035 — Dato terminal y descenso real hasta la fila17

Estado: **PROVED; revisión independiente APROBADA en POWER_BOUNDARY_AUDIT_035.md**. A tasa FIJA u=63/2,

    W[f_(N,k)]>(1/40)||f_(N,k)||²,
    TODOS enteros1<=N<=17, TODOS k>=0.                  (ROWS17)

El dato terminal NUEVO es W[f_(17,0)]>(1/25)||f_(17,0)||². Una sola evaluación terminal, ninguna campaña N13,14,...,17. Papers intactos; no nueva ventanaT ni signo de mezclas arbitrarias.

## 1. Corpus y diferencia precisa

Consultados ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D sobre descenso, recurrencias, datos terminales y contactos; leídos DESCENT016, TABLE_DESCENT018 y su falsificador estructural, ARITHMETIC_DIFFERENCES019, ARCH_EXACT032, DIVISOR_COMPARISON034 y auditorías respectivas. No se atribuye signo a una recurrencia aislada ni se supone monotonía general de ARCH+POLAR, ya inadecuada en007.

La diferencia nueva es combinar DOS datos de signo REAL: la columna k1 uniforme034 y un único extremo k0 certificado aquí con TODO el peine adverso. Esa información adicional permite descenso finito legítimo. N17 se elige como el extremo entero de034 a tasa fija: 4u²/225=17.64. No se prueban cinco entradas k0 independientes ni se selecciona un extremo por un barrido de signos.

En018, recurrencia y eventualidad por sí solas dejaban datos terminales desconocidos, y el falsificador conservaba precisamente esa falta de signo. Aquí el dato terminal es real y rigurosamente positivo, y sólo se propaga dentro del rango donde034 ya prueba la columna requerida. No se extrapola el descenso a N>=18.

## 2. TerminalN17: normalización y ARCH exacta

Fije N17,d16,u63/2. La norma del borde es

    n_N=||f_(N,0)||²
       =binom(2N−2,N−1)/[2^(2N−1)u^(2N−1)].

ARCH_EXACT032 da la fórmula POSITIVA finita para A_N=ARCH/n_N,

    A_N=H15−gamma−logpi−sum_(j=1)^(N−1)b_j S_(j+1),
    b0=1, b_(j+1)=b_j u(d−j)/(2d−j),
    S_p=sum_(n>=16)n^(-p).

Para este extremo de grado16 basta Euler–Maclaurin hasta B4 en M32. El centro es

    Z_p=sum_(n=16)^31 n^(-p)+32^(1−p)/(p−1)+(1/2)32^-p
                  +(p/12)32^(-p−1)
                  −[p(p+1)(p+2)/720]32^(-p−3),
    |S_p−Z_p|<=E_p=p(p+1)(p+2)/(720·32^(p+3)).          (EM2)

El resto es el integral del Bernoulli periódico4; sup|B4({x})|<=|B4|=1/30. No se supone que el signo del siguiente término determine el resto. Es el mismo argumento absoluto032 con sólo DOS términos Bernoulli, suficiente para este margen.

Multiplicando los extremos racionales por b_j ANTES de redondear y sumando todos los j1,...,16, el verificador prueba

    A_17>−217/250=−.868.                                 (ARCH17)

Se usa sólo gamma y logpi de003 con restos auditados; no hay cuadratura ni funciones especiales numéricas en el certificado.

## 3. Polar17 exacto y favorable

La expresión beta exacta es

    p_N=POLAR/n_N
       =[4^N/(u binom(2N−2,N−1))]
                       [u²/(u²−1/4)]^N.

Para N17 esta fracción positiva satisface

    p_17>911/1000.                                      (POLAR17)

No se reemplaza el polar por cero ni se supone monotonía de su suma con ARCH.

## 4. TODO el peine adverso desde una cota de pendiente real

Sea rho_17(t)=C_17(t)/C_17(0)>0, q=−rho'/rho. En k0 el peine normalizado es NEGATIVO,

    PRIME/n_17=−2sum_(n>=2)Lambda(n)n^-1/2 rho_17(logn).

Por ROOT/CURV026, con d16,

    q(t)>sqrt[(d/t)²+u²]−d/t,  q'(t)>0.

Como log2>2/3 y

    u²=3969/4 >15²+2·16·15/(2/3)=945,

se obtiene q(log2)>15. Por monotonía de q, para TODOS n>=2,

    rho_17(logn)<=rho_17(log2)(n/2)^(-15).               (TAIL-SLOPE)

Esto no es una extrapolación de pocos contactos: integra una cota diferencial válida para toda la semirrecta.

El polinomio normalizado rho=e^(-ut)P_17(t) tiene coeficientes POSITIVOS p_j=b_j2^j/j!. Por tanto Horner con el extremo superior racional de log2, usando

    2^(-u)=2^-31/sqrt2 < (5/7)2^-31,

prueba

    rho_17(log2)<1/600.                                 (RHO2)

Ahora Lambda(n)<=logn, n^-1/2<5/7 y la integral decreciente de x^-15logx dan

    2sum_(n>=2)Lambda(n)n^-1/2 rho_17(logn)
      <=(10/7)rho_17(log2)[(8/7)log2+1/98]
      <(6/5)rho_17(log2)<1/500.                         (PRIME17)

Se han incluido TODAS las potencias primas y todo el resto infinito, sin una enumeración ni una cuadratura de cola. El paso a TODOS los enteros es una cota superior del módulo de este peine adverso, por lo que su dirección en el bound inferior de W es correcta.

## 5. Signo real del extremo y descenso normalizado

ARCH17, POLAR17 y PRIME17 prueban

    W[f_(17,0)]/n_17
      >−217/250+911/1000−1/500
       =41/1000>1/25.                                  (TERMINAL)

Use ahora la recurrencia COMPLETA sin normalizar, con a_(N,k)=W[f_(N,k)]:

    a_(N,0)=a_(N,1)+u²a_(N+1,0).                       (REC)

Se verifica tanto para la densidad tau²/(u²+tau²)^(N+1)+u²/(u²+tau²)^(N+1)=(u²+tau²)^(-N), como para el polar exacto; no se omite ningún término aritmético.

Las normas beta dan

    ||f_(N,1)||²/n_N=1/(2N),
    u²n_(N+1)/n_N=(2N−1)/(2N).

Por ello la identidad NORMALIZADA es una combinación convexa:

    W[f_(N,0)]/n_N
      =[1/(2N)] W[f_(N,1)]/||f_(N,1)||²
        +[(2N−1)/(2N)] W[f_(N+1,0)]/n_(N+1).            (CONVEX)

DIVISOR_COMPARISON034 prueba el primer término normalizado>1/40 para TODOS3<=N<=17, en esta tasa. TERMINAL es>1/25>1/40. Descendiendo N16,...,3 mediante CONVEX se obtiene W[f_(N,0)]/n_N>1/40 en TODO ese rango. No se certifica cada entrada: la propagación es simbólica y usa exclusivamente signos reales ya probados.

Con034 para todas las columnas k>=1, se completan las filas3,...,17. INTERIOR017 ya prueba la fila1 con margen4/3 y TABLE_DESCENT018 las filas2,3 con margen1/8, en todos los k y u>=63/2; por tanto también las filas1,2 cumplen el margen1/40 a la tasa fijada. Esto prueba ROWS17.

## 6. Patrón y alcance exacto

El patrón reutilizable es un principio FINITO: una columna k1 realmente positiva en1<=N<M y un borde terminal k0 realmente positivo en M fuerzan hacia atrás los bordes anteriores por REC. Los márgenes normalizados se propagan por convexidad de normas. Una identidad sin esos dos datos de signo no lo permite, tal como mostraban016/018.

Este memo proporciona ambos datos hasta M17 y mantiene todo el peine. No controla ningún terminal M>=18 ni el borde de todas las tasas u variables; TERMINAL usa u=63/2 exactamente. Tampoco demuestra positividad de mezclas arbitrarias de todos estos átomos. La tabla suficiente de todos los órdenes y las nuevas ventanasT permanecen abiertas.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_boundary_balance_035_verify.py

PASS. Una sola evaluación terminal N17 y constantes racionales; ningún barrido N13,...,17. La prueba de todas las filas reside en CONVEX y034.
