# POWER_CONFLUENT_THIRTEEN_052 — Pivote real de V13 y contactos adversos en la dirección complementaria

Estado: PROVED, certificado racional PASS y revisión independiente aprobada en POWER_CONFLUENT_THIRTEEN_AUDIT_052.md. Sólo V13 confluyente de tasa63/2; no trece polos arbitrarios. Papers intactos.

## 1. Resultado y diferencia respecto a051

Sea u=63/2 y V13={P(s)/(s+u)^13:gradoP<13}, con funciones causales y coeficientes reales. Conservando ARCH, POLAR y TODOS los contactos,

    W[f] > ||f||²/4000,   f∈V13 no nulo.                (FULL13)

La información adicional no es sólo otro bloque positivo: se cuantifica el pivote complementario a ZERO13 y se identifica el signo real de sus contactos2 y3. En una dirección racional que minimiza el Schur de E2 hasta el error intervalar certificado, ARCH+POLAR es positivo, mientras ambos contactos son adversos. El contacto2 consume casi todo ese beneficio: no es un contacto reparador en esta dirección.

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D, con las entradas Schur/W-lin y STATE051. Revisados ARITHMETIC_BLOCK007, R12_ENDPOINT048, FULL_TWELVE050 y su auditoría.051 ya deduplicó la fórmula abstracta de Schur y mostró que positividad en codimensión1 no basta. La diferencia actual es evaluar el acoplamiento de ESTA forma real y sus contactos, en el ÚNICO bloque siguiente V13, sin barrer dimensiones o tasas.

## 2. E2 ya positiva, pero el majorante de cola007 no cabe

En la base Laguerre ortonormal e_0,...,e_12 de048, E2=ARCH+POLAR+contacto2 tiene matriz Toeplitz real T2. El certificado exacto demuestra

    E2[f] > (3/10000)||f||².                             (E2)

El menor autovalor flotante, utilizado sólo para diagnosticar este bloque único antes de certificarlo, fue aproximadamente0.000305571086. No se utiliza ese valor en la prueba.

La adaptación directa a dimensión13 del majorante de cola desde3 de007 da aproximadamente0.002331781986, mayor que el margen anterior. El nuevo grado12 requiere justificar monotonía con log3>16/15, en lugar del bound log3>1 que bastaba para grado11: para 0≤r≤12,

    1/log3 +63r/(63log3−40) < 32.

El bound16/15 se obtiene de los primeros términos positivos de atanh para log3. Esta insuficiencia del majorante no afirma que la cola real tenga ese tamaño ni que E2 sea insuficiente en la forma completa.

Se retuvo entonces EXACTAMENTE el siguiente contacto3, según la instrucción de la tarea; no se buscaron otros contactos.

## 3. E23 y cola completa desde4

Escribir E23=E2−(2log3/sqrt3)c(log3). Las bandas del contacto n son

    diagonal: −2(logn)n^−32,
    banda k≥1: −(logn)n^−32 [L_k(63logn)−L_(k−1)(63logn)],

para n=2,3; el factor sqrt(n) ya está absorbido exactamente junto con exp(−u logn). El logaritmo de3 se encierra por atanh con argumento1/2 y resto positivo, sin exponenciales flotantes.

El verificador tools/power_confluent_thirteen_052_verify.py extiende007 a trece bandas. ARCH usa las mismas sumas de potencias a partir de16 y colas Euler con resto explícito; POLAR es racional exacto. Los centros de T2 y T23 tienen denominador10^15 y su error de operador es<ε=10^−10, por suma de filas. Dos LDL racionales verifican

    Tc2−(3/10000+ε)I>0,
    Tc23−(7/25000+ε)I>0.

Así E23[f]>(7/25000)||f||²=0.00028||f||².

Para la cola n≥4 se conserva la cancelación polinómica de007: todos los coeficientes de

    (−1)^k [L_k(40+y)−L_(k−1)(40+y)], 0≤k≤12,

son no negativos (L_−1=0). Cada término se limita usando Λ(n)≤logn y el primer término más la integral de

    (logx)(63logx−40)^r x^−32, x≥4, 0≤r≤12.

La derivada logarítmica tiene signo negativo porque log4>4/3 y

    1/(4/3)+63·12/(63·4/3−40)<32.

Con log4<7/5, las integrales se evalúan exactamente mediante el cambio x=4exp(t) y los momentos ∫_0∞t^r exp(−31t)dt=r!/31^(r+1). El resultado es una cota racional por banda; la suma de filas certificada es

    ||cola_(n≥4)|| <1/100000=0.00001.                    (TAIL)

La evaluación decimal de ese majorante es aproximadamente0.0000090179619783; la prueba usa sólo fracciones. La cola incluye TODOS los primos y potencias primas restantes. De E23 y TAIL,

    W[f]>(7/25000−1/100000)||f||²
         >||f||²/4000,

probando FULL13.

## 4. Pivote complementario real y error de sus cruces

Sea ell_j=(−1)^j y h=ell, con ||h||²=13. La restricción ZERO13 es H=ell⊥, pues la evaluación de Laplace en0 es un múltiplo de Σ(−1)^jz_j. Sus columnas racionales son

    C_i=e_i−(−1)^i e_12, i=0,...,11.

Para una matriz T, definir

    A=CᵀTC, g=CᵀTh, d=hᵀTh,
    sigma(T)=(d−gᵀA^−1g)/13.

Es el mínimo de la forma sobre h/√13+H. No es el menor autovalor de T. El subbloque A es positivo por los resultados anteriores; los cálculos aquí también comprueban sus pivotes al resolverlo. Para T2 central:

    d/13 ∈(0.12337,0.12338),
    gᵀA^−1g/13 ∈(0.12296,0.12298).

La cancelación de ambos términos deja un margen pequeño. Para encerrar el pivote de la matriz exacta se calcula sigma(Tc−εI) y sigma(Tc+εI). La orientación es válida porque sigma es el ínfimo de formas evaluadas sobre el MISMO espacio afín, y la restricción sigue positiva. El certificado obtiene

    0.0004054 <sigma(E2)<0.0004055,
    0.0003834 <sigma(E23)<0.0003836.                     (PIVOTS)

El contacto3 reduce el pivote; no lo repara.

Para la forma completa, TAIL implica Tc23−(ε+0.00001)I≤TW≤Tc23+(ε+0.00001)I. Aplicar el mismo principio del ínfimo da

    0.0003 <sigma(W)<0.0005.                             (FULL-PIVOT)

Éste es un control real del cruce con TODOS los contactos, no una conclusión extraída sólo de la positividad codimensional de050.

## 5. Qué términos sostienen y consumen este margen

Sea x=h−CA^−1g el vector RACIONAL definido por el centro Tc2, sin redondear sus coordenadas. Su componente sobre ell es h, y el mínimo anterior es xᵀTc2x/13. Evaluando los componentes intervalares originales sobre este MISMO vector, el verificador demuestra

    ARCH[x]/13+POLAR[x]/13 ∈(0.01839,0.01841),
    contacto2[x]/13 ∈(−0.01800,−0.01798),
    contacto3[x]/13 <0.                                 (COMPONENTS)

Estas cifras son energías de y=x/√13, cuyo coeficiente sobre el complemento unitario h/√13 es1; y NO tiene norma1. No son cocientes de Rayleigh divididos por ||x||². No se mezclan minimizadores de componentes distintos. Las fracciones y sus productos se mantienen exactos. El vector minimiza el Schur del CENTRO, mientras PIVOTS encierra el mínimo de la forma exacta; no se atribuye a x una optimalidad exacta no probada.

El dato revela dos funciones diferentes del contacto2. ARCH+POLAR es indefinida en V12 por el test auditado006, luego también en V13 por inclusión; allí la aritmética2 repara otras direcciones. Sin embargo, en la dirección complementaria de este Schur,2 es adverso y casi cancela el AP positivo.3 también es adverso. Conservar3 exactamente mejora el certificado al evitar el exceso del majorante absoluto de cola007, NO porque3 aporte energía positiva.

Esto exige controlar los cruces y la dirección de cada contacto, en lugar de asumir que un mismo primo es reparador en todas las direcciones. El margen full queda positivo gracias al balance cuantificado y a la pequeña cola desde4.

## 6. Alcance

Se decide el signo de V13 CONFLUYENTE y su pivote respecto a ZERO13, con toda la aritmética. La cobertura050 para doce polos arbitrarios se conserva. No se infiere positividad para trece polos arbitrarios: faltaría una ganancia completa apropiada de catorce polos o una extensión de órbita que no se prueba aquí. No se continuó con V14,V15,... ni se realizó una campaña de contactos.
