# POWER_DIVISOR_COMPARISON_034 — Un comparador completo positivo uniforme

Estado: **PROVED; revisión independiente APROBADA en POWER_COMPARISON_AUDIT_034.md**. Para TODOS enteros N>=3,k>=1 y TODAS tasas reales u tales que

    u>=63/2,   u²>=225N/4,
    W[f_(N,k)]>(1/40)||f_(N,k)||².                       (NEW-REGION)

Además, PARA k=1, el comparador inferior normalizado B_N+S_K de033 es >1/40 para CADA K impar. En la tasa FIJA u31.5 se cubren simultáneamente N3,...,17 en TODAS las columnas k>=1; N6,...,17 eran el segmento no cubierto por las filas completas1,...,5. Para k>=2 el margen mejora a3/20 mediante§7. No se afirma toda la tabla ni una nueva ventanaT. Papers intactos.

## 1. Corpus y razón nueva

Consultados ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D sobre contactos, cotas beta y límites de identidades Euler; leídos ROW_PATTERN029, CONTACT_DECISION032 y PRIME_BALANCE033 con sus auditorías. No se presenta la fórmula beta, la monotonía arquimediana ni Euler como nuevas.

La diferencia es que el peine FIRMADO de019/033 permite retirar el costo absoluto aritmético que limitaba la región029 u>=16sqrtN. El comparador completo de033 obtiene ahora un margen POSITIVO en un rango infinito nuevo, con constantes universales y sin certificar órdenes separados. La mejora procede aquí de ARCH−|POLAR|>0 más el peine favorable, NO de que Neumann compense un ARCH negativo como en el punto211. No se atribuye a esta región el mecanismo crítico de032.

## 2. La región satisface todas las hipótesis aritméticas

Puesto que N<=4u²/225,

    2u²/9−u/3+3/2−N
      >=46u²/225−u/3+3/2>0,  u>=63/2.

Así NEW-REGION está dentro de REGION033. TODOS los contactos son positivos por019 y las desigualdades033 son válidas: S_K>0 para cada K impar. Los tres contactos q2,3,4 que forman parte de B_N también son positivos. No se omite una cola de signo desconocido.

## 3. Margen arquimediano uniforme

ARCH-GENERAL029 prueba, por Euler periódico B2 y los momentos beta exactos, para todo N>=2,

    ARCH_(N,1)/norm²
      >=log(u/(2pi))+(1/2)[psi(3/2)−psi(N−1/2)]
                        −9(N−1/2)/u².                  (A)

La cota psi(x)<=logx se sigue, por ejemplo, de Jensen sobre la ley Gamma(x): psi(x)=ElogX<=logEX. Como psi(3/2)=2−gamma−2log2 y u/sqrtN>=15/2, se obtiene

    ARCH_(N,1)/norm²
      >log(15/2)−log(4pi)+1−gamma/2−4/25
      >7/200.                                          (ARCH)

La última comparación es racional con las constantes auditadas003. Es una sola desigualdad de constantes; no un barrido de N ni una aproximación de ARCH en N concretos.

## 4. Polar exacto y pérdida uniforme

Las fórmulas beta029 dan

    p_(N,0)=POLAR_(N,0)/norm_(N,0)²
      <=4sqrt(pi)sqrtN/u ·(1−1/(4u²))^(−N),
    |POLAR_(N,1)|/norm_(N,1)²
      =p_(N,0)·2N/(4u²−1).

Como sqrt(pi)<9/5 y sqrtN/u<=2/15, el primer factor es <24/25. Bernoulli entero y N/(4u²)<=1/225 dan

    (1−1/(4u²))^N>=1−N/(4u²)>=224/225,
    p_(N,0)<(24/25)(225/224)=27/28.

Además N>=3 implica

    2N/(4u²−1)<=2N/(225N−1)<=3/337.

Por tanto el polar de k1, que es NEGATIVO, satisface

    |POLAR_(N,1)|/norm² <81/9436<9/1000.                  (POLAR)

No se descarta su signo ni se uniformiza con una constante creciente en N.

## 5. Comparador033 positivo y forma completa

Por definición033 y la positividad aritmética,

    B_N+S_K
      =ARCH/norm²+POLAR/norm²
         +log2 w(2)+log3 w(3)+log2 w(4)+S_K
      >7/200−9/1000=13/500>1/40                         (COMPARATOR)

para CADA K impar. FULL033 conserva TODA la cola y da

    W[f_(N,1)]/norm²>=B_N+S_K>1/40.

Esto prueba NEW-REGION en k1. También puede probarse directamente ignorando el peine favorable; explicitar COMPARATOR muestra que el criterio033 ya no queda únicamente en una obligación formal. La contracción no es necesaria para el margen de esta región y no se afirma lo contrario.

## 6. Alcance

La condición u²>=225N/4 mejora la condición029 u²>=256N para TODAS las columnas k>=1, usando el signo aritmético en k1 y el margen mayor en las columnas restantes. En u31.5, 4u²/225=441/25=17.64; de ahí el segmento entero N<=17 sin verificaciones individuales.

No se ha reparado aquí un ARCH negativo ni se ha decidido todo el rango033 N/u² cercano a2/9. La cancelación casi exacta de211 sigue siendo un certificado puntual032. El borde k0 no se incluye. Las columnas k>=2 se prueban aparte en§7, sin extrapolarles el signo aritmético de k1.

Reproducción:

    python3 03-research/phase-211-sign-sandbox/tools/power_divisor_comparison_034_verify.py

PASS; sólo constantes universales Fraction/intervalos. La uniformidad de N,u reside en las desigualdades escritas.


## 7. Extensión uniforme a TODAS las columnas k>=2

La misma ARCH-GENERAL029, ahora con psi(k+1/2)>=psi(5/2)=psi(3/2)+2/3 y k−1/2>=3/2, da

    ARCH_(N,k)/norm²
      >log(15/2)−log(4pi)+1−gamma/2+1/3−4/75
      >19/40,  k>=2.                                    (ARCH2)

En efecto el margen respecto al bound arquimediano de k1 es1/3+8/75=11/25. No se evalúa ninguna columna por separado.

Aquí el peine no tiene signo supuesto. CENTERED029, válido para TODO k, con eta4 da

    |c_f(t)|/norm²<=e^(-4t)R,
    R=[(u²−16)/(u²−64)]^(N−1/2)
      <=exp[48(N−1/2)/(u²−64)]
      <exp(9/10)<5/2.                                    (CENTER)

Para el exponente, 48(N−1/2)/(u²−64)<9/10 equivale a48N+168/5<(9/10)u². Como 48N<=(64/75)u² y 9/10−64/75=7/150, basta u²>720, garantizado por u>=63/2. La última comparación usa el intervalo racional log(5/2)>9/10; no se reemplaza exp por un decimal.

Usando TODOS los contactos, Lambda(q)<=logq y la integral decreciente de x^-4 logx,

    sum_(q>=2)Lambda(q)q^(-9/2)
      <(5/7)2^-4[(5/3)log2+2/9]<31/500.

Se utilizó q^-1/2<=2^-1/2<5/7. Por tanto

    |PRIME|/norm²<2R(31/500)<31/100.                     (PRIME2)

Las fórmulas beta029 y binom(k+N−1,N−1)<=N^k, c_k>=2^-k prueban para CUALQUIER k

    |POLAR_(N,k)|/norm²<=p_(N,0)[2N/(4u²−1)]^k.

Como 2N/(4u²−1)<=3/337<1 y p_(N,0)<27/28, el polar impar es <9/1000; el par es favorable. No se asume que el peine de estas columnas sea favorable.

Juntando las tres desigualdades,

    W[f_(N,k)]/norm²>19/40−31/100−9/1000
                         =39/250>3/20,  k>=2.           (HIGHER)

Así se completa NEW-REGION para TODOS k>=1. La prueba usa dos regímenes: el pequeño margen arquimediano de k1 necesita el signo real del peine019/033; desde k2, la ganancia beta permite un costo absoluto uniforme. El borde k0 permanece fuera de la afirmación.

## 8. Corolarios de cobertura al combinar certificados ya auditados

En u FIJO63/2, ARITHMETIC_BLOCK007§1 prueba W>10^-4 norm² en TODO V12=e^(-uy)·{polinomios de grado<=11}. Para N<=12, g_N(y)=y^(N−1)e^(-uy)/(N−1)! pertenece a V12. Combinándolo con NEW-REGION (N<=17 en esta tasa), se completan las filas3<=N<=12 para TODOS k>=0, con margen>10^-4. Las filas1,2 ya estaban probadas. Para N13,...,17, este corolario deja únicamente k0 abierto; no extiende V12 a órdenes superiores.

Para TODA tasa u>=63/2, SIGNED_TRANSFER014§1 permite ocho polos con multiplicidades y prueba W>10^-3 norm². El átomo g_N con N<=8 se representa en el espacio de denominador(s+u)^8 mediante numerador(s+u)^(8−N), de grado<8. Por tanto k0 está cubierto uniformemente hasta N8. NEW-REGION cubre k>=1 hasta N17 para todas esas tasas (pues u²>=u0²>225·17/4). Así se completan uniformemente las filas3<=N<=8, con margen>10^-3. No se afirma k0 uniforme en u para N9,...,12: el certificadoV12 sólo usa la tasa fija63/2.

Estas inclusiones de espacios no alteran los certificados007/014 ni convierten la nueva región en una prueba de toda la tabla. El resto a tasa fija incluye k0 paraN>=13 y el interior no cubierto paraN>=18.
