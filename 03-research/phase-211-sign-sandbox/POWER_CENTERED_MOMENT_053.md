# POWER_CENTERED_MOMENT_053 — Un momento matricial exacto reduce el corte a96

Estado: **PROVED con certificado racional; auditoría independiente aprobada en POWER_CENTERED_MOMENT_AUDIT_053.md.** Sólo dimensión13, TODOS los numeradores y TODOS j>=96. Papers intactos.

## 1. Corpus, elección previa y diferencia

Consultados ROUTES-TRIED-INDEX/README, grid maestro, CROSSWORD-TO-D, HIGHPASS015, CENTERED_CUTOFF049 y DIMENSIONAL_CUTOFF051 con su corrección auditada. El bound uniforme051 permite pagar dos contactos mediante un corte mayor (por ejemplo128). La diferencia aquí es certificar el momento inverso EXACTO de todo un bloque de dimensión13, en vez de reutilizar como nuevo el majorante IBP051.

Se fijaron ANTES del cálculo J=96 y b=1/5: un único ensayo racional para reducir en un cuarto ese corte128 y obtener ARCH>12/5. Se comunicó previamente al constructor principal. No se ensayó otro J, ningún numerador ni una malla de parámetros. La matriz tiene dimensión13, aunque el orden highpass sea96. El script `tools/power_centered_moment_053_verify.py` ejecuta solamente ese certificado y constantes racionales.

## 2. Gram binomial exacta y positividad del momento

Sobre el círculo z=exp(i theta), q=(2+z+zbar)/4=|1+z|²/4. Si A(z)=sum_(a=0)^12 A_a z^a, la correspondencia ortonormal Laguerre da exactamente la probabilidad espectral de Q^j F0 como q^j|A(z)|² dtheta, normalizada. Aquí F0 recorre TODO V13.

La matriz de la integral contra dtheta/(2pi) es

    (T_j)_(a,b)=4^(-j) binom(2j,j+a-b), 0<=a,b<=12,

entendiendo cero si el índice está fuera de0,...,2j. Prueba: expandir

    q^j=4^(-j)z^(-j)(1+z)^(2j)

y tomar el coeficiente constante después de multiplicar por z^(a-b). La simetría binomial hace irrelevante intercambiar a-b con b-a. T_j es definida positiva: q^j>0 salvo en un punto del círculo y un polinomio no nulo tiene sólo un número finito de raíces.

La razón r_j=E[(1-q)/q] verifica

    r_j = A* (T_(j-1)-T_j) A / (A*T_j A).

Por tanto r_96<1/5 para TODOS A!=0 equivale a que (6/5)T_96-T_95 sea definida positiva. Multiplicar por4^96 da la matriz racional FINITA

    M_(a,b)=(6/5)binom(192,96+a-b)
                         -4binom(190,95+a-b).

El verificador comprueba los TRECE pivotes LDL estrictamente positivos por aritmética Fraction, sin autovalores flotantes. El certificado es válido también para coeficientes complejos porque la matriz es real simétrica.

## 3. Todos los j posteriores, sin otros certificados

Para cada A fijo, pasar de j a j+1 repondera por q. Como (1-q)/q decrece en q, la covarianza es no positiva. Por ello r_(j+1)<=r_j. Todas las integrales son finitas para j>=1. Se obtiene simultáneamente para TODOS j>=96 y TODOS F0!=0 en V13,

    r_j<1/5,
    E_(Q^jF0)[tau^-2] < 1/(5u²)=4/19845, u=63/2.       (MOMENT)

No se requiere que el mismo A minimice cada índice; la monotonía vale para CADA A y el certificado inicial cubre TODOS A.

## 4. ARCH y dos contactos con constantes exactas

Por Jensen, Cauchy y el bound de digamma de017/051,

    ARCH/||G||²
      > log[u sqrt5/(2pi)] - 2/sqrt19845 - 2/19845.

Se tiene sqrt5>559/250 y pi<22/7, de donde u sqrt5/(2pi)>56/5. Además2/sqrt19845<1/70 y2/19845<1/9800. Finalmente

    log(56/5)>12/5+1/70+1/9800

se verifica con los32 primeros términos POSITIVOS de la serie atanh, de argumento51/61. No se necesitan un resto ni una evaluación decimal: un prefijo positivo inferior ya supera el racional indicado. En consecuencia

    ARCH[Q^jF0] > (12/5)||Q^jF0||², j>=96.             (ARCH)

Los coeficientes reales de los contactos satisfacen v2=sqrt2 log2<1 y v3=2log3/sqrt3<77/60<13/10. Se usan log2<7/10, sqrt2<10/7, log3<11/10 y sqrt3>12/7. El valor absoluto de cada correlación está acotado por la norma al cuadrado, así que

    (ARCH+contacto2+contacto3)[G] > (7/60)||G||².

No se presume signo favorable de los contactos.

## 5. Polar y alcance E23

En V13, las bandas polares exactas son

    p_k=(63/992)(-1)^k[(32/31)^k+(31/32)^k], 0<=k<=12.

El verificador comprueba |p_k|<1/5. La norma de la matriz polar es menor que13/5<3 por suma de filas. La prueba elemental de ENDPOINT048 para dimensión13 da <qF,F>>=||F||²/(4·13²)=||F||²/676. La logconvexidad de los momentos q^j implica ||Q^jF||²>=676^(-j)||F||². Por ello

    |Polar[Q^jF]|/||Q^jF||²
       <3(676/3968)^j=3(169/992)^j<3·5^(-j)<1/1000

para todos j>=96. Definiendo E23=ARCH+POLAR+contactos2,3, queda

    E23[Q^jF]>(1/10)||Q^jF||²,
    TODOS j>=96, TODOS F!=0 enV13.                      (TAIL-E23)

El bound usa7/60-1/1000>1/10. No contiene los contactos n>=4. Para una afirmación sobre W completo faltan pagar esa cola y tratar el segmento j=1,...,95; la positividad de V13 base y cualquier transporte posterior son obligaciones separadas. No se ha certificado aquí ese segmento ni se concluye signo global.
