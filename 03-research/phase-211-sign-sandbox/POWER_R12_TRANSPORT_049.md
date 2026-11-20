# POWER_R12_TRANSPORT_049 — Transporte aritmético R12 para el primer movimiento desde V12

Estado: PROVED; revisión independiente APROBADA en POWER_R12_AUDIT_049.md. Constructor, auditor y root reprodujeron el certificado exhaustivo finito PASS. R12 queda resuelto en su clase declarada, no el signo completo de W. Papers intactos.

## 1. Corpus, diferencia y objetivo

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID, CROSSWORD-TO-D y PRIME_TRANSFER014, GEOMETRIC_TRANSFER015, ARITHMETIC_BLOCK007, R12_ENDPOINT048 y CENTERED_CUTOFF049. El falsificador universal014 no pertenece a V12. La eventualidad015 no daba un corte efectivo. La diferencia actual es combinar el corte analítico J=14, uniforme en TODOS los numeradores de V12, con un certificado exhaustivo del único segmento restante j=1,...,13. Los índices se fijan por la prueba del corte, no mediante una búsqueda de casos favorables.

Sea u=63/2, Q(s)=s/(s+u), y E2=ARCH+POLAR−sqrt(2)log2·c(log2). El objetivo es exactamente R12 de PRIME_TRANSFER014§5, con c=1/2500.

## 2. Segmento finito: matrices y error relativo a la Gram

El verificador tools/power_r12_finite_segment_049_verify.py reproduce las fórmulas intervalares auditadas007 y048 para las25 primeras bandas de la matriz Toeplitz E2 en la base Laguerre ortonormal. Conserva ARCH, contacto2 y polar exactos en sus normalizaciones originales. La ARCH usa sumas de potencias a partir de16 con Euler y restos explícitos, el polar es racional y log2 tiene resto de atanh positivo. Los centros racionales tienen denominador10^18. La suma de errores por fila es menor que10^−8.

Sobre el círculo z=(s−u)/(s+u), Q=(1+z)/2. Para cada j=1,...,13 la imagen Q^jV12 tiene matriz de coeficientes

    C_j[a,i]=binom(j,a−i), 0≤i≤11, 0≤a≤11+j,

entendiendo cero fuera de0≤a−i≤j. Se omite el factor común2^−j: cancela del signo de la desigualdad. La Gram exacta es C_jᵀC_j. Si T es la matriz E2 y Tc su centro intervalar, entonces

    |xᵀ C_jᵀ(T−Tc) C_j x| ≤ 10^−8 xᵀ C_jᵀC_j x.

No se paga el error contra una identidad de coordenadas mal condicionadas. El LDL racional de dimensión12 verifica, para TODOS los trece índices,

    C_jᵀ Tc C_j − (1/2500+10^−8)C_jᵀC_j > 0.

La ejecución única terminó exit0, con trece mensajes PASS y la conclusión

    E2[Q^jF] > ||Q^jF||²/2500,
    F∈V12 no nulo, j=1,...,13.                          (FINITE)

La comprobación no usa autovalores flotantes ni discretización de tasas, y no deja índices sin verificar en ese segmento.

## 3. Cola analítica y toda la órbita

CENTERED_CUTOFF049 demuestra para TODO j≥14 y TODO F∈V12,

    E_(Q^jF) τ^−2 < 1/405,
    ARCH[Q^jF]/||Q^jF||² > 859/800.

El contacto2 tiene módulo menor que la norma². R12_ENDPOINT048 da

    |POLAR[Q^jF]|/||Q^jF||² ≤ (9/62)^j PB12,

con PB12<3: las bandas polares tienen módulo<1/5 y la suma de fila es<12/5. Así, para j≥14,

    E2[Q^jF]/||Q^jF||²
       > 859/800 − 1 − 3(9/62)^14 > 1/2500.             (TAIL)

Juntando FINITE y TAIL, E2−c norma² es estrictamente positiva en TODA Q^jV12, para todos los enteros j≥1.

## 4. Ensamblaje exacto y resolución de R12

Para v≥u ponga r=1−u²/v²∈[0,1). Sea G_v(s)=sF(s)/(s+v). La identidad geométrica015, aplicada a QF, da

    E2[G_v]=(1−r)Σ_(j≥0) r^j E2[Q^(j+1)F],
    ||G_v||²=(1−r)Σ_(j≥0)r^j ||Q^(j+1)F||².           (MIX)

Es una identidad de formas cuadráticas, no de funciones. El polar se conserva porque Q(−1/2)Q(1/2)=−1/3968 y

    (1−r)Σ r^j (−1/3968)^(j+1)=−1/(4v²−1).

Las series convergen absolutamente por un argumento directo. En el eje real |Q(iτ)|<=1 y la integral de |m(τ)||F(iτ)|² es finita para todo F en V12, por su decaimiento racional. Esto domina uniformemente las integrales arquimedianas de Q^jF. El contacto2 está acotado por sqrt(2)log2·||F||², y el polar es la sucesión geométrica explícita anterior. Así cada E2[Q^jF] queda uniformemente acotada en j; la suma geométrica y la convergencia dominada justifican MIX para cada v finito. La misma dominación con multiplicador1 prueba la identidad de normas y permite restar c. El caso v=u es r=0 y queda incluido.

Por FINITE+TAIL y MIX,

    E2[G_v] > (1/2500)||G_v||²,
    F∈V12\{0}, TODOS v≥u.                              (R12-PROVED)

Esta es exactamente la obligación R12: |G_v(iτ)|²=τ²|F(iτ)|²/(v²+τ²) y POLAR[G_v]=−POLAR[F]/[4(v²−1/4)].

Si f_v=(s+u)F/(s+v), T2 de014 implica

    (E2−c norma²)[f_v] ≥ (u²/v²)(E2−c norma²)[F].

007 certifica E2[F]>(1/1250−10^−8)||F||²; como ese margen es mayor que c, la base también es coerciva a la misma constante.

## 5. Alcance

Se resuelve la obligación restringida R12 y el primer movimiento desde V12. No se han acotado aquí los contactos restantes sobre el espacio desplazado: la cola pequeña de007 fue certificada sólo sobre la base confluyente V12. Por tanto no se infiere una desigualdad para W completo en esos nuevos espacios. Tampoco se aplica R12 recursivamente a una base intermedia distinta de V12 sin una prueba adicional. No se afirma signo global ni nueva ventana temporal.
