# Auditoría RH7–RH9: detector local, estabilidad y geometría

## Alcance y leyenda

Se revisaron los tres README, todos los `OVERVIEW.md` y, cuando aportaban evidencia material, los CSV, cuadernos y especificaciones asociados. La etiqueta expresa el alcance exacto de la afirmación, no su aspiración.

| Etiqueta | Significado operativo |
|---|---|
| **PROBADO** | Identidad, reducción o cota demostrada en el espacio finito y con hipótesis explícitas. |
| **CONDICIONAL** | Depende de una hipótesis matemática, de una identificación no construida o de una especificación externa completa. |
| **NUMÉRICO** | Reproducido en datos, una malla finita o una implementación; no es un teorema asintótico. |
| **CONJETURAL** | Arquitectura, extrapolación o ruta de investigación. |
| **REFUTADO** | La formulación ensayada falla, es inconsistente o no tiene datos suficientes para el uso reclamado. |
| **REFORMULACIÓN-EQUIVALENTE-A-RH** | Cambia RH por una condición que, de ser cierta, ya contiene la positividad o el paso uniforme que decide RH. No aporta una demostración independiente. |

## RH7 — Detector local de la forma cuadrática de Weil

**Objetivo y método.** Construir una forma localizada
\(Q=M_{\rm zeros}-M_{\rm arith}\) en una base Hermite--Gauss, validarla en \(\zeta\), \(L(\chi_4\bmod 5)\) y \(L(\Delta)\), inyectar cuartetos de ceros desplazados, medir \(\lambda_{\min}\), y separar la señal de un cero fuera de recta del error de cortar primos y ceros. La dependencia correcta es de \((T_0,\sigma,J,X,H)\); toda lectura que la suprima queda fuera de alcance.

### Resultados cerrados y evidencia

- **[PROBADO, finito]** La expansión de Taylor del modelo sintético de cuartetos da un término de orden \(\delta^2\) y un operador real simétrico de bajo rango construido con \(\phi,\phi',\phi''\). La parte algebraica de esta afirmación es finita-dimensional, una vez fijadas convención de cuarteto, base y lista de ceros.
- **[NUMÉRICO]** `task32` compara el mínimo del operador suma con la superficie simulada en 60 celdas y registra \(R^2\) redondeado a uno; `task31` lo contrasta en otro centro. Es evidencia muy fuerte de que el código y la expansión usan la misma convención, no una prueba sobre un cero real desconocido ni sobre el funcional infinito.
- **[NUMÉRICO]** El motor pasa trazas de controles en los regímenes que se declaran resueltos; `task20` da para \(L(\Delta)\) un residual de traza cercano a precisión de máquina tras elevar el corte y reparar los datos de ceros. `task40` aporta el control de \(\zeta\). Esto valida instancias concretas de ensamblaje, no una implementación independiente ni una identidad uniforme en la familia.
- **[PROBADO con alcance finito / NUMÉRICO en la calibración]** La transformada de productos Hermite--Gauss tiene cola gaussiana y permite acotar la cola aritmética por valores absolutos usando una cota explícita para \(\psi(x)\). `task34` y el README comparan esa envolvente con siete valores de \(X\). La correlación y el factor de holgura observado son **NUMÉRICOS**; para llamar a la integral una cota se debe sustituir la densidad PNT aproximada por una desigualdad explícita y conservar todas las constantes.
- **[NUMÉRICO]** Las tablas de detectabilidad (`task15`, `task18`, `task21`) estiman cuándo \(c\delta^2\) supera un suelo observado. Interpolan en \(J\), toman siete cortes de primos y, en un punto, alcanzan el suelo de coma flotante: son reglas de diseño, no umbrales matemáticos certificados.

### Dependencias, puntos abiertos y estado lógico

| Afirmación | Estado | Auditoría |
|---|---|---|
| Paso de una perturbación sintética a negatividad del modelo finito | **PROBADO** | Válido sólo tras fijar la convención de cuarteto y el operador de la base. |
| \(\delta^2\), localidad y amplificación en \(J\) para las mallas ejecutadas | **NUMÉRICO** | Los ceros movidos son datos fabricados; no hay control uniforme al crecer \(J\). |
| Validación de \(Q\) para \(\zeta\), carácter complejo y \(\Delta\) en puntos de control | **NUMÉRICO** | Una coincidencia de traza no certifica por sí sola cada entrada ni otras normalizaciones. |
| Cola de primos con base Hermite--Gauss | **PROBADO** si se formula con una cota explícita de Chebyshev/PNT; **NUMÉRICO** para la constante ajustada | La sustitución de la suma discreta por una densidad no es, por sí sola, una demostración de cota. |
| Cola de ceros y convergencia uniforme de \(Q_X\) a \(Q_\infty\) en el régimen decisivo | **REFORMULACIÓN-EQUIVALENTE-A-RH** | Es precisamente el paso que permitiría trasladar la negatividad finita a la positividad de Weil global. No quedó demostrado. |
| “El detector prueba RH si nunca ve negatividad” | **REFUTADO** | Una búsqueda finita no cubre todos los centros, anchos, órdenes, alturas ni desplazamientos. |

### Errores, retiros y no-go

- **Davenport--Heilbronn:** el valor de referencia absoluto no es reproducible con la información disponible. Falta una definición única de la secuencia aritmética análoga a \(\Lambda\), y una combinación lineal de funciones \(L\) no permite combinar término a término logaritmos derivados. `task11`, `task24` y `task41` obligan a retirarlo como control cuantitativo. Queda sólo como contraste cualitativo: **REFUTADO** para calibración numérica.
- **Normalizaciones de \(L(\Delta)\):** `task2`, `task12` y `task17` descartan las correcciones de factor dos ensayadas. Los primeros fallos de traza y listas de ceros (`task4`, `task5`, `task8`, `task23`, `task36`, `task37`) fueron superados en parte por `task20`, pero no deben mezclarse con el resultado final.
- **Ceros de \(\Delta\):** el integrador con corte fijo perdió ceros; algunas listas iniciales contienen entradas dudosas. Sólo las listas verificadas y el protocolo de refinamiento posterior pueden alimentar una afirmación cuantitativa.
- **Carácter no autodual:** la fórmula inicial tenía un sesgo de fase. RH7 usa una corrección con parte real; RH8 adopta una formulación simetrizada. No se debe transferir números entre ambas sin fijar exactamente lado de ceros, conductor, términos gamma y convención de conjugación.
- **Inconsistencia documental:** la fórmula del operador perturbativo escrita en la síntesis de RH7 no coincide literalmente con la derivada en `task32`. La fórmula canónica debe reconstruirse desde la expansión y verificarse contra el CSV antes de ser citada como teorema.
- **Ajustes de leyes:** siete puntos de \(X\) no identifican un “régimen de densidad cero”. `task9` reconoce sobreajuste; por tanto su inferencia sobre la hipótesis más débil es **REFUTADA** como deducción lógica, aunque el ajuste sea un dato útil.

### Herencia y ruta que no repetir

Hereda a RH8 un motor que debe ser trazado con especificación, lista de ceros validada y corte dependiente de \(\sigma,J\). Deja para cualquier continuación una única tarea analítica: una desigualdad de norma que controle simultáneamente colas de primos, ceros y error numérico en una clase explícita de parámetros. No repetir: convertir ajustes empíricos en hipótesis aritméticas, usar Davenport--Heilbronn cuantitativamente, ni confundir \(\Delta Q\) sintético con una prueba sobre \(Q_\infty\).

## RH8 — Estabilidad en base y monotonicidad de localización

**Objetivo y método.** Estudiar en los tres controles la estabilidad de \(\lambda_{\min}(Q(T_0,\sigma,J))\) al aumentar \(J\) (H1) y su respuesta a \(\sigma\) y a ventanas anidadas de ceros (H2). El programa reutiliza el motor de RH7, impone una puerta de traza antes de interpretar un autovalor y excluye cuantitativamente a Davenport--Heilbronn.

### Resultado auditado

- **[NUMÉRICO]** En los dominios donde la traza pasa la puerta, las curvas disponibles para \(\zeta\), \(L(\chi_4\bmod5)\) y \(L(\Delta)\) se acercan al suelo numérico al ampliar \(J\), \(\sigma\) o la ventana de ceros. `task4`, `task9`, `task14` y `task17` son controles puntuales; `task1`, `task16`, `task19`, `task25` y `task27` dan las mallas de H1.
- **[NUMÉRICO]** H2 es apoyada en el régimen resuelto: `task2`, `task20`, `task21` y `task26` no encuentran el patrón de obstrucción buscado bajo ensanchamiento de ventana. Esto es ausencia de contraejemplo en malla finita, no una monotonía variacional demostrada.
- **[NUMÉRICO / corrección de implementación]** `task3` sustituye la fórmula no autodual por la forma simetrizada que combina carácter y conjugado, y elimina el residual independiente de \(X\). Es una corrección necesaria para esta implementación; no prueba que toda generalización de Weil de carácter complejo haya quedado normalizada de manera única.
- **[REFUTADO en el dominio computado]** A \(\sigma=0.5\) y cortes accesibles, la puerta de traza no se cierra; `task6` observa incluso crecimiento del defecto. Las curvas de H1/H2 allí no son evidencia espectral.

| Afirmación | Estado | Límite |
|---|---|---|
| H1 para \(J\) finitos, \(\sigma\) y \(X\) resueltos | **NUMÉRICO** | No prueba el límite \(J\to\infty\), ni uniformidad fuera de los centros muestreados. |
| H2 en ventanas anidadas y anchos resueltos | **NUMÉRICO** | No hay teorema de orden de formas ni monotonicidad para todos los test. |
| H1/H2 a \(\sigma=0.5\) con los cortes disponibles | **REFUTADO** como lectura del espectro | Predomina truncación aritmética. |
| “Estabilidad o monotonicidad finita implica RH” | **REFUTADO** | El propio diseño lo prohíbe; también depende de la transición al funcional completo. |
| Escalado suficiente de \(X\) para toda la familia \((T_0,\sigma,J)\) | **CONDICIONAL** | Se midieron fronteras prácticas, no una ley uniforme demostrada. |

**Dependencias y herencia.** RH8 depende directamente de la validez local de RH7; su contribución durable es metodológica: no interpretar \(\lambda_{\min}\) sin residual de traza, y separar tres regímenes: validado, recuperable elevando \(X\), e inaccesible con el corte actual. Hereda hacia adelante una condición de admisión para toda exploración numérica, pero ninguna vía nueva hacia RH.

**No-go y correcciones.** No reutilizar los resultados de `task8`, `task10`, `task12`, `task13`, `task22` y `task23` como validaciones: registran implementación incompleta, datos ausentes o límites de cómputo. Tampoco presentar la corrección simetrizada como si reconciliara automáticamente las convenciones anteriores de RH7. La ruta correcta es fijar una única especificación matemática, añadir una verificación independiente de entradas de matriz y demostrar una cota de cola antes de reclamar H1/H2 asintóticas.

## RH9 — Superficie aritmética y estructura de Lefschetz

**Objetivo y método.** Buscar una geometría independiente del espectro que produzca una superficie absoluta \(S\), diagonal \([\Delta]\), un triple de Lefschetz y una forma de Hodge--Riemann vinculados al criterio de Weil. Se investigan tres rutas: Arakelov/\(\lambda\)-anillos, prismática/TC y geometría no conmutativa de escala; además se usan estadísticas espectrales como restricción de diseño.

### Veredicto global

No se construyó \(S\), \([\Delta]\), una cohomología con \(H^1\) espectral, ni un triple \((L,\Lambda,H)\) que pase G1--G4. El programa es valioso como mapa de incompatibilidades y requisitos, pero no como avance demostrativo hacia RH. La reducción inicial que declara que la existencia de G1--G4 equivale a RH debe catalogarse **REFORMULACIÓN-EQUIVALENTE-A-RH** hasta que se aporte una prueba independiente de la reducción y, sobre todo, una construcción que no codifique los ceros.

### Rutas, resultados y dependencias

| Ruta | Lo que queda | Estado auditado |
|---|---|---|
| Arakelov y \(\lambda\)-anillos | Hay clases de Chern, intersecciones, índices de Hodge aritméticos y gradaciones Adams en contextos existentes. La variación de métrica sugiere independencia respecto de un operador definido por ceros. | **CONDICIONAL / CONJETURAL.** Falta el objeto absoluto, el mapa a \(\Pi^\perp\), la diagonal, \(\Lambda\), un espacio común donde demostrar \(L\notin W^*(T)\), y la identificación de la positividad aritmética con la forma requerida. |
| Prismática, TC y Sen | Frobenios locales, filtraciones Nygaard y comparaciones locales son herramientas reales; la bibliografía no aporta un generador global con espectro de ceros. | **CONJETURAL** como andamiaje; la ausencia de un objeto en la consulta no es una refutación universal. G1, G3 y G4 siguen abiertos. |
| Escala, adeles y prolate/Sonin | La dinámica de escala produce la estructura de traza y pesos \(\log p\) de órbitas primitivas. El generador relevante es no compacto y sus realizaciones examinadas no dan la gradación entera de peso mínimo requerida. | **CONDICIONAL** como obstrucción: es sólida para las representaciones y dominios especificados, pero no prueba un no-go de toda geometría no conmutativa. |
| Estadística \(\Delta_3\) | CSV y cuadernos registran un plateau cercano a \(0.1908\) para una muestra de ceros y su diferencia respecto de GUE finito/infinito. | **NUMÉRICO.** Es una restricción fenoménica para un modelo futuro, no una identidad cohomológica. |

### Puntos abiertos, circularidades y retiradas

- **G1:** no hay una identificación demostrada entre cohomología geométrica y \(\Pi^\perp\), ni un Frobenius con espectro \(\gamma_\rho\). Métrica variable frente a espectro fijo es evidencia heurística de independencia, no un certificado de pertenencia a un álgebra de von Neumann sin una representación común.
- **G2:** Adams da pesos enteros racionalizados, pero no el operador de Cartan de un \(\mathfrak{sl}_2\) de Lefschetz. Los casos de variedades abelianas usan dualidad y núcleo de Poincaré ausentes para \(\mathrm{Spec}\,\mathbb Z\). Un triple prolate con generador de escala continuo no satisface el requisito.
- **G3:** imponer \([T,L]=cL\) dentro de la base de ceros vuelve a pedir traslaciones aritméticas del espectro. El argumento es concluyente para operadores acotados con hipótesis de dominio adecuadas; para operadores no acotados los cuadernos y revisiones sólo dan una advertencia de dominio, no un teorema general.
- **G4:** el índice de Hodge aritmético es una fuente de positividad en su propio contexto, pero no se ha identificado su parte primitiva con la del criterio de Weil. Si la positividad se define usando los signos de ceros fuera de recta o equivale a \(Q\succeq0\), es circular y queda **REFORMULACIÓN-EQUIVALENTE-A-RH**.
- La fórmula de suma prima propuesta para explicar el plateau que contiene \(\sum_{p,k}(\log p)^2/p^k\) diverge; `task14` la descarta. Sólo una fórmula con corte dinámico y derivación completa puede usarse: la fórmula literal está **REFUTADA**.
- Los cálculos de `task14`, `task36`, `task46`, `task59` y `task70` son exploratorios y contienen aproximaciones de unfolding, GUE y fórmulas semiclasicas. No pueden transformarse en un teorema de ausencia de escalas, de independencia lineal ni de existencia de una constante geométrica.
- La bibliografía de los `OVERVIEW.md` es evidencia de orientación. Antes de convertir cualquiera de sus afirmaciones en dependencia matemática se deben verificar las fuentes primarias, hipótesis y notación; los resúmenes no sustituyen esa verificación.

### Herencia y ruta que no repetir

La herencia útil es un conjunto de puertas: independencia de \(W^*(T)\), gradación entera genuina, operador global con espectro correcto, y positividad que no replantee RH. Ninguna ruta debe empezar definiendo \(L\) a partir de momentos o ceros, invocar una superficie sobre \(\mathbb F_1\) como existente, confundir Frobenios locales con el espectro global, ni inferir un triple de Lefschetz de estadísticas de espaciados. El próximo paso legítimo es escoger una única categoría geométrica ya construida y demostrar una pieza concreta de G1--G4 sin identificarla anticipadamente con RH.

## Cobertura de directorios

| Programa | Directorios cubiertos | Tipo de evidencia y destino |
|---|---|---|
| RH7 | `task1, task3, task7, task13, task14, task27, task30, task33, task38, task39, task43` | Sin respuesta sustantiva; no sostienen conclusiones. |
| RH7 | `task2, task4, task5, task6, task8, task11, task12, task17, task23, task24, task25, task26, task28, task35, task36, task37, task40, task41, task42` | Diagnóstico de motor, normalización, datos y límites; varios son retirados o sustituidos por validaciones posteriores. |
| RH7 | `task9, task10, task15, task16, task18, task19, task20, task21, task22, task29, task31, task32, task34` | Señal \(\delta^2\), colas, detectabilidad y validaciones finales; mezcla de resultados finitos y numéricos, según la tabla anterior. |
| RH8 | `task7, task8, task10, task12, task13, task15, task22, task23, task24` | Sin cierre o implementación/datos insuficientes; excluidos como evidencia de H1/H2. |
| RH8 | `task4, task9, task14, task17` | Puertas de traza y controles puntuales: evidencia numérica de ensamblaje en régimen resuelto. |
| RH8 | `task1, task2, task3, task5, task6, task11, task16, task18, task19, task20, task21, task25, task26, task27` | Curvas H1/H2, barridos de corte y corrección no autodual; evidencia exclusivamente numérica y dependiente de régimen. |
| RH9 | `task1–task13` | Revisión de rutas Arakelov, escala, prismática y correspondencias; evidencia bibliográfica, mayoritariamente condicional. |
| RH9 | `task14` | Cuaderno de \(\Delta_3\), fórmula divergente retirada y comparación semiclasica: numérico/exploratorio. |
| RH9 | `task15–task35` | Gradaciones, Lefschetz, independencia, traza y prismática: mapa de dependencias y vacíos, no construcción. |
| RH9 | `task36` | Estadística de pares de ceros: numérica; no prueba una obstrucción espectral general. |
| RH9 | `task37–task45` | Positividad aritmética, operadores, \(\lambda\)-anillos y no-go parciales: condicionales. |
| RH9 | `task46` | Réplica de \(\Delta_3\): numérica y no independiente de la misma tubería de datos. |
| RH9 | `task47–task54` | \(\Lambda\), correspondencias, Frobenio/Sen y cohomología absoluta: vacíos identificados, no piezas G1--G4 cerradas. |
| RH9 | `task55` | Cuaderno de construcción de conmutador; artefacto exploratorio sin certificación de una ruta geométrica. |
| RH9 | `task56–task62` | Transformadas por núcleos, Adams, trazas y estadística: propuestas y restricciones, no demostraciones globales. |
| RH9 | `task63` | Síntesis extensa de literatura; útil como inventario, no como prueba de la reducción ni de una construcción. |
| RH9 | `task64–task66` | Compatibilidad, operador de Weil y estrella aritmética: condicionales; faltan los objetos globales. |
| RH9 | `task67` | Preprocesamiento incompleto; sin evidencia utilizable. |
| RH9 | `task68–task69` | Pesos \(\log p\) y deformación cuántica: mecanismos parciales/conjeturales. |
| RH9 | `task70` | Comparación Riemann--GUE de \(\Delta_3\): numérica, con normalizaciones y aproximaciones a controlar. |
| RH9 | `task71–task79` | Prolate, estrella, Hecke, operadores no acotados y álgebra de von Neumann: restricciones condicionales y revisión de literatura. |

## Síntesis para el replanteo global

1. RH7 aporta un detector y una cota de cola para una base finita; RH8 muestra qué regímenes numéricos son admisibles. Ninguno resuelve el salto al funcional infinito: ése es el cuello de botella lógico y es **REFORMULACIÓN-EQUIVALENTE-A-RH**.
2. RH9 no entrega geometría absoluta; entrega filtros que una geometría tendría que satisfacer sin circularidad. Sus mejores activos son los no-go condicionados y la lista G1--G4, no una vía demostrativa ya abierta.
3. La continuación debe separar tres capas: identidad finita demostrada, cota analítica explícita y afirmación global. No se debe permitir que una misma calibración numérica ocupe dos de esas capas.
