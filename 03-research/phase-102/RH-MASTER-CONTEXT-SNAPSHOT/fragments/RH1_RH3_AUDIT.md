# Auditoría de RH1–RH3: utilidad, límites y reinicio

## Dictamen ejecutivo

Los tres programas no contienen una demostración de RH ni una reducción nueva que la acerque de forma demostrable. Su rendimiento útil es diagnóstico: fijan varios controles numéricos, muestran que la multiplicatividad por sí sola no clasifica la geometría finita de polinomios de Dirichlet y localizan fallos que un replanteo debe bloquear desde el inicio. La tesis rectora de RH1 —«producto de Euler/multiplicatividad suprime la resonancia que permitiría ceros fuera de la recta»— queda **REFUTADA** como explicación general por las familias multiplicativas aleatorias y, de modo decisivo, por Liouville. RH2 elimina además las flechas empíricas que pretendían convertir esos observables en una prueba. RH3 conserva una fenomenología de clases \(\omega(n)\), pero sólo a escala finita y con sensibilidad marcada a la definición, la selección de picos y la implementación.

**Regla de lectura.** PROBADO significa identidad matemática o teorema externo correctamente invocado, no una gráfica. CONDICIONAL significa una implicación que requeriría una cota nueva. NUMÉRICO significa cálculo finito reproducible dentro de una implementación identificada. CONJETURAL significa interpretación o extrapolación. REFUTADO significa que el propio programa aportó un contraejemplo, un ensayo negativo o una imposibilidad metodológica. REFORMULACIÓN-EQUIVALENTE-A-RH señala una frase que, si fuera cierta en todo el dominio pertinente, ya sería RH y no una vía independiente.

## Cobertura documental

Se leyeron los tres README, los 266 `OVERVIEW.md` y los documentos matemáticos o de validación necesarios para resolver conflictos: en particular los informes de validación de Davenport–Heilbronn, las descomposiciones de momentos, los informes canónicos de \(r\), el código o informe de la función aleatoria canónica y el manuscrito de redes de barrido. La cobertura es exhaustiva por intervalos contiguos; no queda ningún directorio de tarea fuera de la tabla.

| Programa | Directorios revisados | Cobertura | Foco dominante |
|---|---|---:|---|
| RH1 | `task1`–`task89` | 89/89 | detector de resonancia, fases, GEV, clasificación y crisis DH |
| RH2 | `task1`–`task94` | 94/94 | intento de cadena prueba–diagnóstico, perturbaciones y controles |
| RH3 | `task1`–`task83` | 83/83 | geometría de clases \(\omega\), momentos, causalidad finita e infraestructura |
| **Total** | `RH1/task1`–`task89`; `RH2/task1`–`task94`; `RH3/task1`–`task83` | **266/266** | — |

## Inventario de estatus matemático

| Afirmación | Estatus | Alcance correcto |
|---|---|---|
| La función clásica de Davenport–Heilbronn carece de producto de Euler y posee ceros fuera de la recta crítica. | **PROBADO** | Hecho de calibración externo; sirve para descartar detectores, no para inferir RH. |
| \(\lambda\) es completamente multiplicativa y su serie es \(\zeta(2s)/\zeta(s)\). | **PROBADO** | Contraejemplo conceptual a «multiplicativo implica supresión». |
| \(\mu(n)^2(-1)^{\omega(n)}=\mu(n)\), por lo que la serie correspondiente es \(1/\zeta(s)\). | **PROBADO** | Corrige la falsa presentación de ese objeto como una función nueva independiente. |
| \(|D|^2=\sum_k|S_k|^2+\sum_{j\ne k}\Re(S_j\overline{S_k})\). | **PROBADO** | Identidad algebraica. El cociente \(r\) es una parametrización de esos términos cruzados, no una cota sobre ceros. |
| Ortogonalidad media de polinomios de Dirichlet y el paradigma Montgomery–Vaughan para segundos momentos. | **PROBADO** | No convierte la descomposición por \(\omega\) en información sobre \(\zeta(\rho)=0\). Los ensayos finitos sólo son consistentes con el teorema. |
| Vinogradov–Korobov y Selberg CLT. | **PROBADO** como teoremas externos; **NUMÉRICO** como comprobaciones de escala finita en RH2. | Equidistribución o gaussianidad de promedios no da una exclusión uniforme de ceros fuera de la recta. |
| Deformar \(S_k\mapsto -S_k\) reduce picos de un polinomio de Dirichlet seleccionado. | **NUMÉRICO** | Es causal sólo para esa variable finita, esa malla, esos picos y esa partición; no es causalidad sobre los ceros de una función \(L\). |
| Separación SVM/LDA por CAS, \(M_{\rm coh}\), \(R_{\rm comp}\), entropía o ACF. | **NUMÉRICO** | Clasifica las muestras y generadores usados. Una separación incluso perfecta no es caracterización analítica ni criterio de RH. |
| Anomalía de \(M_4\) cerca de \(N\approx10^5\). | **NUMÉRICO**, parcialmente **REFUTADO** como universal. | Aparece en varias familias reales y aritméticas, falta en el nulo i.i.d. y en la función multiplicativa aleatoria compleja; depende también de la descomposición. |
| «La arquitectura de fases o de clases \(\omega\) es la causa profunda de RH». | **CONJETURAL** | Los datos sólo describen polinomios truncados y admiten contraejemplos entre las familias comparadas. |
| «Una raíz \(\beta+i\gamma\), \(\beta>1/2\), fuerza \(|D(\gamma;N)|\asymp N^{\beta-1/2}\)». | **CONDICIONAL** sin demostración presentada; **REFUTADO** como firma operacional de DH. | No se derivó un teorema para ese observable truncado. En DH la pendiente observada fue compatible con cero hasta escalas grandes. |
| \(R_{\rm comp}\) pequeño \(\Rightarrow\xi<0\Rightarrow\) ausencia de crecimiento \(\Rightarrow\) no hay cero fuera de la recta. | **REFUTADO** | RH2 encuentra que la relación \(R_{\rm comp}\)-\(\xi\) no es universal y que los ajustes GEV cambian con observable, bloques y selección. |
| Cota uniforme de decoherencia para \(D_\zeta\), deducida de sumas exponenciales de primos. | **CONDICIONAL** | Es la única forma reconocible de puente hacia RH, pero falta precisamente la cota uniforme de clases compuestas y el paso de extremos finitos a no-anulación. |
| «Las regiones de barrido cubren el semiplano crítico y allí \(\zeta\ne0\)». | **REFORMULACIÓN-EQUIVALENTE-A-RH** y **REFUTADO como prueba** | Cubrir toda la banda y excluir ceros ya equivale a RH. El manuscrito usa que \(\zeta\) queda lejos de cero y controla \(\zeta'/\zeta\) atravesando posibles polos: son las conclusiones buscadas. |

## RH1 — detector de resonancia y resultado real

**Objetivo y método.** RH1 compara \(\zeta\), caracteres de Dirichlet, una función multiplicativa aleatoria, DH y perturbaciones de DH mediante sumas truncadas
\[
D_F(t;N)=\sum_{n\le N}a_n n^{-1/2-it}.
\]
Mide extremos, colas, coherencia entre escalas, fases de primos y compuestos, \(M_{\rm coh}\), \(R_{\rm comp}\), CAS y GEV. Usa compensación de Kahan y contrastes puntuales de precisión alta. El diseño correcto era falsable: un detector serio debía distinguir una DH validada de familias con producto de Euler.

**Resultados cerrados.**

- **NUMÉRICO / REFUTADO:** la firma asesina no apareció. En el supuesto primer cero de DH, la pendiente ajustada hasta \(N=10^9\) fue aproximadamente \(0.00044\pm0.00045\), no \(0.3085\); seguir el máximo desplazado tampoco la recuperó. Es un resultado negativo del detector, no evidencia de que el hecho clásico sobre DH sea falso.
- **NUMÉRICO / REFUTADO:** las colas, el puntaje de resonancia y la coherencia no ordenan las clases como «multiplicativa frente a no multiplicativa». La función multiplicativa aleatoria y Liouville pueden ser más extremas o más coherentes que DH.
- **NUMÉRICO:** en versiones concretas, los picos de \(\zeta\) muestran sesgo de fases primas y DH puede mostrar estructura en compuestos; la desfasación por clases cambia los picos. Es una descripción de los polinomios calculados, no de sus ceros.
- **NUMÉRICO:** CAS, periodicidad y entropía separan muy bien los conjuntos generados. El hallazgo útil es inverso al programa inicial: las métricas capturan organización de coeficientes, no multiplicatividad ni validez de RH.

**Dependencias y herencia válida.** Se heredan la evaluación compensada, comparación contra precisión alta, controles aleatorios reproducibles, el registro de selección de picos y la identidad de energía por clases. También queda el contraejemplo Liouville como prueba de estrés obligatoria.

**Retiro, no-go y circularidad.**

- El crecimiento \(N^{\beta-1/2}\) se trató como consecuencia automática de una raíz fuera de la recta sin una derivación que conecte la serie truncada sobre \(\Re s=1/2\) con esa raíz. No debe volver a usarse como lema.
- El éxito de un clasificador entrenado y evaluado sobre coeficientes o variantes hermanas no puede certificar una propiedad de cero. Es sobreajuste de la pregunta analítica aunque la validación cruzada interna sea impecable.
- DH fue implementada de formas incompatibles: combinación de caracteres periódica, restricción artificial a cuadrados libres y datos de referencia de procedencia distinta. Las coordenadas de «cero» y \(\kappa\) también varían. Toda conclusión comparativa que mezcle esas variantes queda **REFUTADA por falta de identidad del objeto**.
- La variante periódica sin la restricción a cuadrados libres es la única candidata que pasó la puerta numérica interna en los cuatro puntos refinados; aun así, una suma truncada pequeña sólo es **NUMÉRICA**, no certificación de los ceros de la función completa. Hay que fijar definición, normalización, coordenadas y prueba de convergencia antes de reutilizarla.

## RH2 — de la intuición a una cadena de prueba que no cerró

**Objetivo y método.** RH2 intenta normalizar un motor único, validar DH antes de analizar y convertir tres blancos empíricos en una cadena: decoherencia compuesta \(\to\) forma GEV \(\to\) no crecimiento \(\to\) ausencia de ceros. Añade perturbaciones de clases \(\omega\), distancia pretenciosa, ajustes de \(\xi\), regresiones y verificaciones numéricas de teoremas conocidos.

**Resultados cerrados.**

- **NUMÉRICO / REFUTADO:** \(R_{\rm comp}\) bajo no predice universalmente \(\xi<0\); la correlación cambia de signo, familia y protocolo. Por tanto se rompe el segundo eslabón de la cadena.
- **NUMÉRICO / REFUTADO:** los ajustes de GEV no ofrecen clasificador robusto ni tendencia asintótica fiable. Hay informes con signo opuesto de \(\xi\), y la convención de SciPy \(c=-\xi\), el uso de \(|D|\) frente a \(\log|D|\), la ventana y el tamaño de bloque alteran la lectura.
- **NUMÉRICO:** invertir \(S_2\) o clases compuestas altera covarianzas y picos de \(\zeta\) en las muestras; es una sensibilidad finita interesante, no una desigualdad uniforme.
- **NUMÉRICO / REFUTADO:** la distancia pretenciosa, los momentos globales y los modelos de regresión no sostienen un predictor generalizable de cola o coherencia. Los buenos \(R^2\) internos fallan en validación cruzada.
- **PROBADO / NUMÉRICO:** el motor y los controles de precisión son una mejora operativa, y las verificaciones de resultados clásicos son controles de cordura, no pruebas nuevas.

**Dependencias.** RH2 depende de una única DH validada, de definición fija de \(S_k\), del mismo criterio de pico y de un protocolo GEV congelado. Esas condiciones no se mantuvieron de forma global: el propio repositorio conserva validaciones fallidas, coordenadas distintas y tareas detenidas por la precondición.

**No repetir.** No encadenar correlaciones de escala finita como implicaciones lógicas; no interpretar \(\xi\) penúltimo como tipo de cola asintótico; no usar evidencia de Vinogradov–Korobov o Selberg para suplir la cota uniforme ausente; no aceptar resultados DH si la puerta de validación no está documentada para exactamente la misma función.

## RH3 — geometría \(\omega\), momentos y límites computacionales

**Objetivo y método.** RH3 estudia \(S_k=\sum_{\omega(n)=k}a_n n^{-1/2-it}\), el cociente canónico \(r\), inversión de fase de una clase, segundo y cuarto momento y su evolución con \(N\). Compara \(\zeta\), Liouville, Möbius, caracteres, funciones aleatorias y DH; añade una función multiplicativa aleatoria de semilla fija y aceleración compilada.

**Resultados cerrados.**

- **PROBADO:** la identidad de energía que define \(r\) y la reproducibilidad de la función aleatoria canónica de semilla fija. Son infraestructura, no contenido sobre RH.
- **NUMÉRICO:** en picos seleccionados \(r\) suele ser positivo y en valles puede ser negativo; la inversión de \(S_2\) o \(S_3\) reduce picos. La interpretación correcta es interferencia de vectores condicionada por selección.
- **NUMÉRICO:** los segundos momentos transversales disminuyen en los ensayos y son compatibles con la ortogonalidad media; el cuarto momento y sus categorías muestran cambios finitos no monótonos en varias familias.
- **NUMÉRICO / REFUTADO:** la anomalía \(M_4\) no es universal de la multiplicatividad: falla en el nulo complejo y aparece en familias no multiplicativas. Tampoco queda establecida como propiedad de «coeficientes reales»: algunas tareas fijan partes de la descomposición por proporciones preasignadas.
- **REFUTADO:** las narrativas de evolución monótona de \(r\), de dominancia de pares adyacentes o de una resonancia fina en \(\kappa\) caen al igualar el criterio de selección de picos o al ampliar el barrido.

**Errores y límites decisivos.**

- Comparar picos elegidos por \(r\) en una escala con picos elegidos por magnitud en otra introdujo sesgo; el reanálisis homogéneo lo deshace.
- Varias tareas no alcanzan \(N=10^7\); por ello no hay evidencia de límite ni de monotonicidad. «No computable dentro del presupuesto» no es resultado negativo sobre la hipótesis matemática.
- En una descomposición de \(M_4\) se calcularon sólo términos iniciales y se impusieron proporciones fijas para el resto. Sus porcentajes no son evidencia y deben marcarse **REFUTADOS como descomposición**.
- Un manuscrito de redes de barrido sostiene ausencia de ceros mediante cotas y convergencias que presuponen evitar los polos de \(\zeta'/\zeta\). Es circular y no debe heredarse como demostración.
- La validación DH que prueba puntos \(1/2+it\) con sólo alturas de presuntos ceros fuera de la recta es un control mal planteado: faltan las partes reales. Su fallo no valida ni invalida DH; sólo invalida ese protocolo.

## Qué debe heredar el replanteo global

1. **PROBADO / reutilizable:** identidades algebraicas explícitas, teoremas externos con hipótesis escritas, aritmética de coeficientes, compensación numérica, precisión alta y hashes o semillas para nulos.
2. **NUMÉRICO / reutilizable como exploración:** perturbaciones \(S_k\), mapas de fases, \(r\), CAS y momentos, siempre con definición única, datos versionados, selección idéntica y barras de incertidumbre.
3. **CONDICIONAL / frontera auténtica:** una cota uniforme, explícita y demostrada que conecte estructura aritmética de coeficientes con no-anulación de \(\zeta\) fuera de la recta. Debe ser independiente de RH y estable al pasar de polinomios truncados a la continuación analítica.
4. **REFUTADO / prohibido:** multiplicatividad como criterio suficiente; clasificación estadística como certificado; GEV o correlaciones como eslabones de prueba; la firma de crecimiento DH sin teorema; combinar implementaciones DH; extrapolar desde \(N\le10^7\); y argumentar a partir de picos definidos de manera distinta.
5. **REFORMULACIÓN-EQUIVALENTE-A-RH / prohibido como avance:** afirmar directamente no-anulación en una familia de regiones que cubre la banda crítica, o introducir una cota de \(\zeta'/\zeta\) válida sólo si no hay ceros. Tales enunciados deben etiquetarse como meta, no como lemas disponibles.

## Puerta mínima antes de cualquier nuevo programa

Fijar una sola definición de cada función, en especial DH; acompañarla de una prueba de identidad de coeficientes, de valores de referencia de precisión alta y de coordenadas completas de calibración. Separar en el repositorio teoremas, lemas condicionales, observaciones numéricas y conjeturas. Para cada afirmación de transferencia \(N\to\infty\), exigir una desigualdad explícita con constantes y un paso analítico hacia la función completa. Si ese paso no existe, el resultado debe permanecer NUMÉRICO aunque todas las pruebas de software pasen.
