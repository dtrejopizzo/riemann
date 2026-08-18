# Auditoría de los programas RH1–RH9

## Balance global

Los nueve programas no producen una demostración de RH ni una reducción con menor fuerza demostrada. Su valor es otro: construyen falsadores, calibran detectores, identifican errores de normalización y cierran varias explicaciones tentadoras pero falsas. El recorrido va desde estadísticas de coeficientes hasta geometría cohomológica:

\[
\text{fases de coeficientes}
\to
\text{clases }\omega
\to
\text{reconstrucción por ceros}
\to
\text{forma localizada de Weil}
\to
\text{estabilidad finita}
\to
\text{geometría de Lefschetz}.
\]

En cada transición reaparece el mismo corte: los objetos finitos describen o detectan, pero no fuerzan la positividad global ni construyen el divisor real.

## Tabla canónica

| Programa | Objetivo | Resultado durable | Ruta cerrada o carga pendiente |
|---|---|---|---|
| RH1 | Detectar resonancia mediante sumas de Dirichlet, fases, coherencia y extremos | Instrumentación numérica, controles de precisión y contraejemplo Liouville | Multiplicatividad no suprime por sí sola la resonancia; la firma de crecimiento atribuida a un cero fuera de línea no fue derivada ni observada de modo operativo. |
| RH2 | Convertir decoherencia, GEV y no crecimiento en una cadena de no-anulación | Protocolo más estricto de validación y perturbaciones por clase | Las correlaciones y parámetros GEV no son universales; el paso uniforme a no-anulación falta y tiene fuerza al menos comparable a la meta. |
| RH3 | Estudiar geometría de clases \(\omega(n)\), momentos y causalidad finita | Identidades de energía, reproducibilidad y banco de confusores | Las anomalías dependen de selección, escala e implementación; no hay transferencia desde picos truncados a ceros de la función completa. |
| RH4 | Reconstruir información de ceros desde matrices de picos y covarianzas | Cotas elementales, ablation aritmética y diagnóstico de fugas | Covarianza interclase negativa y singularidad de \(\omega=2\) fueron refutadas; las matrices codifican sobre todo coeficientes, conductor y soporte. |
| RH5 | Usar Jacobi, Mercer, Li, TDA y listas de ceros | Calibración de potencia mediante desplazamientos sintéticos | Gram cero-sólo es PSD tautológica; positividad finita de Li o Mercer no excluye un cero desconocido; forma completa y residuo truncado no son el mismo objeto. |
| RH6 | Localizar la forma de Weil con base Hermite–Gauss | Detector calibrado, respuesta de cuartetos y separación de errores | Falta una cota uniforme conjunta en dimensión, centro, ancho, corte primo, cola de ceros y normalización. Las leyes lineal y cuadrática no pueden mezclarse. |
| RH7 | Construir un detector local con cola controlada | Expansión finita de bajo rango y controles de ensamblaje | La calibración es numérica; el paso al funcional infinito es la positividad de Weil global en otra coordenada. |
| RH8 | Estudiar estabilidad al crecer base, ancho y ventana | Puerta de traza y división de regímenes computacionales | H1/H2 son evidencia de malla; no hay monotonía variacional ni uniformidad al crecer todos los parámetros. |
| RH9 | Construir superficie aritmética, diagonal, Frobenius y triple de Lefschetz | Lista G1–G4 de condiciones y no-go condicionados | No se construyó la superficie, la cohomología, el lector espectral ni la polarización; imponer su positividad a partir de los ceros sería circular. |

## RH1–RH3: por qué falló la explicación por multiplicatividad

Los programas parten de

\[
D_F(t;N)=\sum_{n\le N}a_n n^{-1/2-it},
\qquad
D_F=\sum_k S_k,
\quad
S_k=\sum_{\substack{n\le N\\\omega(n)=k}}a_n n^{-1/2-it}.
\]

La identidad

\[
|D_F|^2
=
\sum_k|S_k|^2
+
\sum_{j\ne k}\Re(S_j\overline{S_k})
\]

es demostrada y útil como contabilidad. No relaciona por sí misma los términos cruzados con ausencia de ceros. Liouville ofrece el falsador conceptual decisivo: es completamente multiplicativa y su serie es \(\zeta(2s)/\zeta(s)\), de modo que “multiplicativo” no implica la geometría de ceros pretendida. Las funciones multiplicativas aleatorias rompen también la identificación entre producto de Euler, coherencia pequeña y colas benignas.

El supuesto puente

\[
\rho=\beta+i\gamma,\ \beta>\tfrac12
\quad\Longrightarrow\quad
|D_F(\gamma;N)|\asymp N^{\beta-1/2}
\]

no fue demostrado para el observable truncado. En el control Davenport–Heilbronn no apareció la pendiente predicha. Esto refuta el detector propuesto, no el hecho clásico de que esa función posee ceros fuera de la recta.

Los clasificadores SVM/LDA, CAS, entropía, ACF, momentos y GEV separan generadores concretos, pero no caracterizan una propiedad analítica. Sus resultados cambian con el observable, la ventana, el bloque, la selección de picos y la convención de signo. RH2 rompe explícitamente las flechas

\[
R_{\rm comp}\text{ pequeño}
\not\Rightarrow
\xi_{\rm GEV}<0
\not\Rightarrow
\text{no crecimiento}
\not\Rightarrow
\text{no ceros fuera de línea}.
\]

La herencia válida de RH1–RH3 es instrumental: suma compensada, precisión alta, semillas y hashes, criterio idéntico de selección, perturbaciones por clase y controles Liouville/aleatorios. La hipótesis causal por clases \(\omega\) queda retirada.

## RH4–RH6: del observable de picos al detector de Weil

RH4 comprueba que las matrices

\[
M_{jk}=\mathbb E\,\Re(S_j\overline{S_k})
\]

responden con fuerza a masa de coeficientes, conductor, soporte y condicionamiento por picos. La inyección de ceros no reproduce las diferencias entre familias, mientras ciertas ablaciones por primos ramificados sí lo hacen. Por eso queda cerrado el puente inverso propuesto desde \(M_{jk}\) a la parte real de un cero. También quedan refutadas la cifra heredada de covarianza negativa y la excepcionalidad causal de \(\omega=2\).

RH5 descubre un no-go esencial: si

\[
G_{ij}=\sum_{\rho}v_i(\rho)\overline{v_j(\rho)},
\]

entonces \(G\succeq0\) por construcción, incluso cuando el diseño ha descartado la coordenada horizontal que debía detectar. Esa PSD no dice RH. Del mismo modo, comprobar \(\lambda_n>0\) para un conjunto finito de índices o una lista finita de ceros no controla los índices restantes.

Debe distinguirse siempre:

\[
\text{forma completa de Weil}
\qquad\text{frente a}\qquad
\text{diferencia entre dos truncaciones de la fórmula explícita}.
\]

La primera tiene positividad universal equivalente a RH. La segunda mide corte, datos y normalización; no hereda un signo.

RH6 mejora el detector localizado, pero conserva una inconsistencia que funciona como alarma: un montaje produce respuesta cuadrática en el desplazamiento y otro informa respuesta lineal. Antes de comparar deben fijarse paridad, cuarteto desplazado, transformada, términos polar/arquimediano y definición exacta de la matriz. La caída gaussiana de Hermite–Gauss controla colas para parámetros fijos; no proporciona por sí sola la desigualdad uniforme necesaria para toda prueba.

## RH7–RH8: detector válido, inferencia global inválida

La expansión finita de un cuarteto perturbado produce un operador simétrico de bajo rango con dependencia cuadrática en \(\delta\) para el montaje especificado. Los controles de traza, listas verificadas y colas Hermite–Gauss son activos reales. Su estado se divide así:

- identidad algebraica de la expansión: **DEMOSTRADO** para la sección fijada;
- coincidencia con mallas, trazas y umbrales: **NUMÉRICO**;
- paso uniforme al funcional completo: **FUERZA-RH**.

RH8 añade una regla metodológica fuerte: no interpretar \(\lambda_{\min}\) si el residual de traza no cierra. A ancho estrecho o corte primo insuficiente, la truncación domina y la aparente inestabilidad no es información espectral. Las curvas H1/H2 observadas no demuestran

\[
Q_{J,\sigma,X,H}\longrightarrow Q_\infty
\]

uniformemente en centro, dimensión, ancho y ventanas. Precisamente esa convergencia, combinada con detección de una perturbación, excluiría ceros fuera de línea y no puede ser tratada como detalle numérico.

## RH9: la geometría todavía no existe

El programa exige una construcción que entregue simultáneamente:

1. un objeto global \(S\) y una diagonal \([\Delta]\);
2. una cohomología cuyo grado uno porte el espectro pertinente;
3. un triple \((L,\Lambda,H)\) de Lefschetz con dominios bien definidos;
4. una polarización positiva que se identifique con la forma de Weil sin haber usado los ceros.

Arakelov, \(\lambda\)-anillos, TC/prismática, dinámica de escala, prolate/Sonin y geometría no conmutativa aportan piezas o analogías, pero no esa construcción conjunta. Frobenios locales no son automáticamente un Frobenius global con espectro de ceros; pesos Adams no son el operador de Cartan requerido; una métrica que se fabrica desde las raíces interpola el divisor en vez de explicarlo.

La estadística \(\Delta_3\) y las comparaciones con GUE son numéricas. Una fórmula prima propuesta para el plateau incluye una serie divergente y queda retirada en su forma literal. RH9 sobrevive como filtro G1–G4, no como ruta activa ya construida.

## Incompatibilidades que bloquean la reutilización automática

1. **Davenport–Heilbronn.** Se mezclaron combinación periódica, restricción a cuadrados libres, constantes, coordenadas y catálogos distintos. Ningún número pasa de una variante a otra sin reconstruir la definición.
2. **Ley de perturbación.** “Lineal” y “cuadrática” corresponden a montajes distintos o a una inconsistencia; no hay ley universal auditada.
3. **Forma y residuo.** La igualdad de la fórmula explícita completa no convierte el error truncado en forma positiva.
4. **Ceros y aritmética.** Una Gram hecha sólo con ceros no es un control independiente del lado primo.
5. **Promedio y universalidad.** Una separación estadística de familias construidas no cuantifica sobre la clase de todas las alternativas a RH.
6. **Catálogos parciales.** Listas incompletas o con precisión distinta no se combinan como una sola muestra.

## Resultado del recorrido

Los programas quedan divididos en tres bancos:

- **banco de instrumentos:** precisión, colas, trazas, falsadores, perturbaciones y control de datos;
- **banco de no-go:** multiplicatividad, clases \(\omega\), Gram cero-sólo, clasificación, TDA, extrapolación finita y geometría meramente postulada;
- **banco de objetivos de fuerza-RH:** positividad completa de Weil, convergencia uniforme del detector, divisor real y polarización identificada.

La continuación no debe abrir un décimo programa exploratorio del mismo tipo. Debe partir de una afirmación aritmética firmada que falle ante un cuarteto plantado y cuya demostración no dependa de la posición de los ceros.

Las auditorías de tarea que sostienen este balance están en:

- [`fragments/RH1_RH3_AUDIT.md`](fragments/RH1_RH3_AUDIT.md)
- [`fragments/RH4_RH6_AUDIT.md`](fragments/RH4_RH6_AUDIT.md)
- [`fragments/RH7_RH9_AUDIT.md`](fragments/RH7_RH9_AUDIT.md)
