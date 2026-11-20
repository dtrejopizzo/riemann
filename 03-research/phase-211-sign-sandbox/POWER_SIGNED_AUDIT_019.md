# POWER SIGNED AUDIT 019

Estado: APROBADOS ambos memos de construcción, con alcance local explícito; no certificado global nuevo. Papers intactos.

## Antecedentes y restricción de novedad

La búsqueda dirigida del corpus sitúa la identidad de Euler/Möbius en los antecedentes ya citados por `POWER_TATE_CHAIN_009` §0: `PROOF_L_SHARP_E/J` (Λ*1=log y momentos), `A_MU_FACTORIZATION/AUDIT200` y `N_018`. La negatividad de una suma divisor acumulada no constituye por sí sola una nueva ruta de signo. El paso distinto que requeriría prueba es la desigualdad del kernel adjunto específico y completo, con sus signos de Möbius.

Descartes ya aparece en `phase-162-row-d-first-contact-closure/R162_1501_TARGET_AUDIT.md`, Lemma D, y en el inventario de `phase-200-sign-object/SPEC_SIGN_OBJECT_011.md`. Su aplicación a una autocorrelación racional concreta puede proporcionar un lema nuevo y local; no se presenta como nueva ruta nodal general.

## Identidad acumulada: chequeo independiente inicial

Si B(x)=log(n!)−xH_n+n, n=floor x, entonces B(1)=0, B tiene pendiente −H_n en cada intervalo [n,n+1) y sus máximos enteros satisfacen B(n+1)−B(n)=log(n+1)−H_n<0, por comparación suma/integral. Así B(x)<0 para x>1. La identificación con la suma divisor de E0 debe mantener la convención E0(1)=0 y los saltos log n.

Este signo escalar no certifica el signo del kernel adjunto. En particular, una truncación de sus sumandos m=1,2,3 negativa no implica negatividad de la suma infinita restante. Las revisiones completas de los memos entregados se registran a continuación.

## Revisión completa de SIGNED_MEAN019 — APROBADO

Leído `POWER_SIGNED_MEAN_019.md`. La suma divisor, la cota B(x)≤−(1−log2)(x−1), y la integración positiva MEAN son correctas. La monotonía de H_n−log(n+1) da la cota en enteros y la pendiente −H_n la prolonga entre ellos. La identidad ∫H_N(x)(x−1)dx=J_N(1/2) conserva los extremos. Así la media de TODAS las dilataciones es estrictamente negativa.

El adjunto h_N(x)=Σμ(m)mH_N(mx) contiene correctamente el jacobiano. La identidad Σd h_N(dy)=H_N(y) sale agrupando divisores; el emparejamiento F_N=2∫h_N B es correcto. Las permutaciones son absolutamente convergentes: H_N(x)=O_N(x^−33 polylog x), mientras |E0(x)|=O(x log x) basta. La condición SIGNED equivale exactamente a −F_N≥−Arch_sharp/c0; no se ha probado.

FAIL3 es correcto para N≥2^17: M2=u²/(2N−3)<1/128, rho(log m)≥1−2M2, rho′≤0 y 1/√2+1/√3>7/6 dan h_N^[3](1)<−19/256. Refuta positividad de cada prefijo inverso en el kernel real. No determina el signo de h_N completo, ni de F_N, ni de W. Resultado nuevo local: signo MEAN y fallo explícito de la preservación por prefijos; la identidad de Möbius por sí misma pertenece a los antecedentes.

Root revisó independientemente SIGNED_MEAN019 y coincide en la aprobación de normalización ERR, saltos/extremos B, constante MEAN, adjunto absolutamente sumable y FAIL3 con su alcance parcial.


## Revisión ARITHMETIC_DIFFERENCES019 — APROBADO

Leídos `POWER_ARITHMETIC_DIFFERENCES_019.md` y su verificador `tools/power_arithmetic_differences_019_verify.py`; ejecución independiente PASS. La fórmula de C_M conserva la norma en t=0 y la identidad c_(N,1)=−C_(N+1)″ es legítima también para N=1: la densidad de la segunda derivada es integrable.

Para N≥2, el cociente exacto de coeficientes de r_N=p_N−2p_N′+p_N″ tiene denominador positivo y numerador j(j+1)−2N estrictamente creciente. Ignorando ceros, tiene una variación. El signo constante negativo y el principal positivo dan existencia; Descartes da unicidad y simplicidad. El extremo N=1 es r_1=x−1. El extremo N=2 da x²−x−1. La recurrencia y p_j>x p_(j−1), probada por comparación de coeficientes, dan los límites declarados de la única raíz para N≥3. No falta un extremo pequeño.

El umbral aritmético es correcto: u log2>21 y 21²−21−(2N−3)≥1 para N≤211. Así TODOS los contactos de la columna k=1 tienen autocorrelación negativa y el peine completo es estrictamente positivo. La suma es absolutamente convergente para u>1/2. No se ha omitido ningún contacto ni se ha inferido el signo de W a partir de este sumando.

La identidad de diferencias del peine aislado es exacta por la misma identidad racional complementaria. C_N>0 da P_(N,0)<0, por lo que todas las diferencias (−Δ)^rP_(1,0) son negativas. Esto refuta sólo la atribución de diferencias positivas al peine por Λ≥0; no refuta las diferencias de la forma completa. La novedad relativa al corpus es la frontera única específica, sus límites y la consecuencia firmada de los 211 órdenes, no el uso general de Descartes.

## Cierre de alcance de la ronda

Se aprueban MEAN y FAIL3, y la transición única de toda la columna k=1 con peine completo positivo para N≤211. Las dos construcciones conservan sus portadores: media de dilataciones frente a residuo original, y peine frente a W completo. El kernel inverso completo y el signo global de la tabla siguen abiertos. No hay nueva ventana T certificada ni modificación de papers.
