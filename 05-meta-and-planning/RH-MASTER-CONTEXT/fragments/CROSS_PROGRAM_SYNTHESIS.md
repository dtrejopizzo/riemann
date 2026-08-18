# Síntesis transversal de programas RH y fases 000–101

## Dictamen de lectura

El corpus deja instrumentos, identidades finitas, controles adversariales y una cartografía bastante precisa del obstáculo. No deja una demostración de RH ni una cadena deductiva cerrada hacia ella. La conclusión transversal es más estrecha y más útil: las rutas de detectores finitos, clasificaciones, positividad construida, promedios, geometrías aún no construidas y cambios de coordenadas no sustituyen las cargas pendientes, entre ellas una convergencia firmada build-neutral y una identificación aritmética independiente con control uniforme. Tampoco está demostrado que una de esas cargas sea el único paso de fuerza-RH. La auditoría de paper 36 añade que el blanco primo mínimo es unilateral, \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\); por ello los no-go basados en valores absolutos no cierran toda posible ruta directa a Li.

Se usan cinco etiquetas sin intercambio de alcance:

| Etiqueta | Uso estricto |
|---|---|
| **DEMOSTRADO** | Identidad, desigualdad o implicación con hipótesis expuestas; puede ser finita o abstracta y no hereda automáticamente un límite. |
| **CONDICIONAL** | Depende de una hipótesis no construida, de una separación, de una cota uniforme, de una geometría o de una transferencia declarada. |
| **NUMÉRICO** | Reproducible sólo para datos, mallas, cortes, normalizaciones e implementación fijados. |
| **REFUTADO** | Falla el mecanismo, la inferencia o la implementación concreta auditada. No afirma imposibilidad de toda idea relacionada. |
| **FUERZA-RH** | Enunciado cuya prueba resolvería RH bajo las transferencias indicadas, o que ya es una equivalencia de RH con otro lenguaje. No es un lema auxiliar disponible. |

En particular, una identidad de sección finita puede ser **DEMOSTRADA** y seguir sin tener fuerza sobre el divisor límite; una calibración puede ser **NUMÉRICA** y muy valiosa sin ser asintótica; y un no-go sólo se aplica a la clase, normalización y mecanismo que efectivamente examina.

## Taxonomía consolidada de no-go

| Familia cerrada | Resultado | Alcance exacto; lo que no autoriza a concluir |
|---|---|---|
| Multiplicatividad, fases y clases \(\omega\) | **REFUTADO** que multiplicatividad, decoherencia compuesta, \(r\), anomalías de momentos, \(\omega=2\), entropías o picos clasifiquen una propiedad de ceros. Liouville, nulos multiplicativos y controles sin producto de Euler rompen las lecturas propuestas. | No prueba que toda identidad aritmética sea inútil. Las descomposiciones por \(\omega\) siguen siendo contabilidad de energía y banco de confusores. |
| Clasificación estadística y extremos | **REFUTADO** que SVM/LDA, GEV, CAS, TDA, regresiones, correlaciones o validación interna certifiquen no-anulación. | No invalida su uso diagnóstico con familias, ventanas y variables de fuga declaradas. No produce una ley universal de colas. |
| Gram, Mercer y cero-sólo | **DEMOSTRADO / REFUTADO**: una Gram hecha sólo con evaluaciones de ceros es PSD por construcción; su positividad no detecta desplazamiento horizontal. | No descarta una forma que incorpore de modo no tautológico el lado aritmético completo y una desigualdad independiente. |
| Truncación, mallas y búsqueda negativa | **REFUTADO** que positividad localizada, coeficientes de Li finitos, ventanas estables, catálogos parciales o ausencia de señal en una búsqueda finita excluyan todos los ceros fuera de recta. | No cuestiona una certificación numérica de la sección concreta, ni una calibración contra una perturbación sintética. |
| Detectores locales de Weil | **REFUTADO** que H0, \(\lambda_{\min}\), respuesta \(\delta^2\), estabilidad H1/H2, o una cola ajustada pasen por sí mismos al funcional completo. | No niega el detector finito: la expansión de cuartetos y ciertas cotas de cola con constantes explícitas sobreviven en su dominio. El no-go no es contra toda futura cota uniforme. |
| LP, energía BTG y `GAP-Z` | **REFUTADO** el núcleo trivial de la formulación LP antigua y la suma absoluta de capas como cota de `ZERO`. La neutralidad LP/Outcome A no está demostrada: usa secciones finitas y un `mu_ref`, no el verdadero \(\mu_L\). | No refuta LP corregido. `BTG-DIV` en \(\mu_L\), completitud mu-libre y la convergencia firmada build-neutral de `ZERO` siguen **INCOMPLETOS**. |
| Discriminantes de nubes | **REFUTADO** elevar cruces, deriva monótona, outliers o proxies de dos escalas a una identificación Euler–Gamma. `E79.6` y las firmas afines son **NUMÉRICAS/CONJETURALES**. | No prueba que `DISCRIMINANT` sea necesario, suficiente ni el único paso de fuerza-RH. Sólo lo deja como separador propuesto dentro de un corte concreto. |
| Promedio, momentos y continuidad débil | **REFUTADO** que promedio, momentos holomorfos, convergencia subsecuencial, productos de trazas, información de nivel único o densidad recuperen soporte transversal, un cero individual o multiplicidad lineal. | No excluye una convergencia de divisor sensible a soporte y multiplicidad; esa condición sería de **FUERZA-RH**. |
| Índice, Stone, Kreĭn, Hodge y geometría importada | **REFUTADO** que unitariedad formal, homotopía sola, símbolo GLT, índice finito postulado, transferencia directa desde cuerpos de funciones o positividad geométrica no identificada suministren el signo de Weil. | No descarta construir una geometría externa real. Exige una categoría, polarización, diagonal y lector espectral construidos sin codificar ceros. |
| Resolventes, cocientes y cierres algebraicos | **REFUTADO** usar pseudoinversa en la curva singular, matching término a término, un solo gap, dos jets, cotas absolutas de cola, smoothing o un \(q\)-resolvente como forzador independiente. | Las identidades de Feshbach, shorting, Cauchy, adjugado y cofactores permanecen **DEMOSTRADAS** con sus hipótesis y preservando los términos acoplados. |
| Abstracciones locales tauberianas y diofánticas | **REFUTADO** que las clases locales examinadas, la transversalidad de fases o densidad Beurling–Malliavin transporten por sí solas fase a inercia. | No es un teorema de inexistencia de toda entrada diofántica no local; queda abierta una condición nueva que haga ese transporte. |

La regla común es: ningún no-go se eleva a imposibilidad universal si sólo se estableció para un observable, una familia de controles, una representación o una clase axiomática concreta.

## Resultados durables que sí sobreviven

### Demostrado y reutilizable

- Identidades de energía y de producto cruzado para \(D=\sum_k S_k\), incluida la lectura de \(r\) como parametrización de interferencia; Cauchy–Schwarz da cotas de conteo de clases, no información de ceros.
- Identidades finitas de determinante bordeado, adjugado, cofactores, Jacobianos característicos, shorting/Feshbach, Cauchy/Hilbert, conmutadores y separación exacta interior/cáscara. La continuación polinómica que evita invertir en una curva singular es válida.
- Para LP corregido: resolvente compacto, existencia del autovalor inferior de multiplicidad finita y equivalencia finita entre energía BTG y contracción del disco de Weyl. No se incluye aquí la divergencia límite en el verdadero \(\mu_L\).
- La descomposición exacta `g_(N+2)-g_N=ZERO+MESH+BND`, con `MESH=O(\sigma/N^2)` y `BND=O(\sigma/N^3)`. El término aritmético `ZERO` no comparte aún esas cotas.
- Del split exacto de Li, la condición mínima es \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\). La dominación de \(|\lambda_n^{\rm prime}|\) es más fuerte y no es equivalente a \(\Omega_7\).
- En el semiplano de convergencia absoluta, el producto Euler–Gamma, la ausencia de ceros del aproximante y su derivada logarítmica; también las identidades seculares, Stieltjes, Abel, Feshbach y de rotación de perfil de las fases 80–89. Son coordenadas exactas, no la identificación del límite.
- La positividad tautológica de formas cero-sólo, la respuesta cuadrática de H0 para el modelo de nube vertical y los no-go de Stone–Kreĭn, Cesàro en el mecanismo examinado, filtros circulares y pérdida de multiplicidad lineal.
- Teoremas externos correctamente usados como marco: criterio de Weil, criterio de Li, Hurwitz en la transferencia apropiada, ortogonalidad media y resultados clásicos de promedios. Su reutilización exige conservar todas las hipótesis.
- Infraestructura: suma compensada y contraste de precisión alta, semillas y hashes para nulos, falsadores plantados o de Davenport–Heilbronn bien definidos, puertas de traza, separación de error de datos frente a error de fórmula y catálogos versionados con cobertura explícita.

### Condicional y útil sólo con hipótesis visibles

- Cierres por convergencia local uniforme, Fredholmicidad, rama simple, Gram uniforme, separación, no anulación de carta, even-simple cofinal, compactidad y cotas de colas conjuntas.
- Torres de índice, confinamiento, coercividad, puentes Pontryagin/Hodge/Fredholm, `D8.5`, `LP-134∞`, `178.C`, `TW_y` y transferencias Cauchy/CCM: son programas condicionales, no piezas ya disponibles.
- LP corregido requiere `BTG-DIV` en el verdadero \(\mu_L\); Outcome A y la neutralidad frente al control son **NUMÉRICOS/CONDICIONALES**, no consecuencias del resolvente compacto. `GAP-Z`, `RDI-CONV`, `RDI-ANCHOR`, `RDP-SHELL`, PROLATE, WEIL-TAIL y las continuidades direccionales siguen siendo obligaciones independientes.
- Una cota Hermite–Gauss para parámetros fijos puede ser demostrable con desigualdades explícitas; la cota conjunta en centro, ancho, dimensión, corte primo, cola de ceros y normalización sigue abierta.

### Numérico, conservable como exploración

- Calibraciones de perturbaciones sintéticas, anomalías locales conocidas, trazas y ensamblajes de matrices, perfiles de calor/Jacobi/Abel, momentos, mapas de fase, H0, H1/H2 y falsadores de secciones finitas.
- Las nubes, defectos de cierre, escapes de rango uno, proxies y `E79.6` son firmas **NUMÉRICAS/CONJETURALES**. No constituyen una ley asintótica ni `DISCRIMINANT`.
- Estas salidas son controles de motor o de detectabilidad. Requieren siempre objeto, normalización, lista, corte, ventana, criterio de selección y barras de error idénticos antes de comparar.

## Equivalencias y condiciones de fuerza-RH bajo nombres distintos

No son avances independientes; son coordenadas de la misma barrera, salvo que se aporte una implicación nueva que no reutilice el objetivo.

| Familia | Nombres usados | Estatus correcto |
|---|---|---|
| Positividad global | Criterio de Weil, positividad de todas las pruebas admisibles, Li para todos los índices, forma de intersección identificada con Weil | **FUERZA-RH**, en varios casos equivalencia clásica. |
| Real-rootedness y pasividad | Hilbert–Pólya útil, \(\xi\in LP\), Herglotz/pasividad de \(\Xi\), \(\mathrm{Im}(-\Xi'/\Xi)\ge0\), \(\Lambda\le0\) en la transferencia declarada | **FUERZA-RH**. |
| Convergencia de aproximantes | Aproximantes enteros con ceros reales que convergen localmente a \(\Xi\), continuidad de signatura, convergencia de resolvente/divisor, Gram primitivo en el extremo | **FUERZA-RH** cuando la convergencia preserva los ceros o el signo necesarios. |
| Índice y defecto | `Omega7`, índice negativo global nulo, `L1`, AHM, pasividad límite, margen uniforme localizado | **FUERZA-RH**; las versiones finitas son sólo certificados o detectores. |
| Cierre Cauchy–Feshbach | `PW-Cauchy`, `HPR-DIV`, `K-DIAGOFF`, `EG_LOCK`, `ADJ-ARITH-LOCK`, `TPW`, `scalar-WRL` | Distintas caras de una cancelación/divisibilidad aritmética firmada pendiente; su cierre tiene **FUERZA-RH** bajo las transferencias ya declaradas. |
| Ruta LP/IDENT | `LP`, `BTG-DIV`, `GAP-Z`, `RDI-CONV`, `RDI-ANCHOR`/`IDENT`, `RDP-SHELL`, PROLATE y WEIL-TAIL | La conjunción declarada implica `Omega7` sólo **CONDICIONALMENTE**. Sus miembros abiertos no se reducen de manera demostrada a un único hito. |
| Ancla bordeada y corrientes | `RDI-ANCHOR`, `DIRECT-BORDERED-ANCHOR`, `CLUSTER-RDI-ANCHOR`, `COFACTOR-CELL-ANCHOR`, `CHARACTERISTIC-JACOBIAN-ANCHOR`, `BASE+SUMDEF→0`, `SENSITIVITY-BOUNDARY-SHELL` | Reparametrizaciones del mismo ancla Gamma–Euler; **FUERZA-RH**. |
| Atlas de divisor y transformadas | `LOCAL-COVARIANT-IDENT`, `STIELTJES-IDENT`, `SR-LOG`, `C_core→0` en intervalo seguro, `XI-PARITY-CURRENT-NULL` | La identificación en intervalo seguro propaga al objetivo; **FUERZA-RH**. |
| Divisor sensible | `TRUE-DIVISOR-IDENT`, convergencia Radon/distribucional que conserve soporte real y multiplicidad lineal | Condición suficiente más fuerte; también de **FUERZA-RH**. |

## Contradicciones, retiros y precedencia documental

La precedencia debe ser: corrección o auditoría que identifica un fallo > ledger final de la fase > cierre explícito del programa > borrador, gráfica, README o rótulo promocional anterior. Si dos textos discrepan y no existe corrección demostrada, el estado conservador es **CONDICIONAL** o **INCOMPLETO**, nunca **DEMOSTRADO**.

| Conflicto | Resolución vinculante |
|---|---|
| Davenport–Heilbronn | Variantes de coeficientes, restricción a cuadrados libres, \(\kappa\), coordenadas de ceros y catálogos no son intercambiables. Sólo una definición fijada y validada sirve de control interno; el uso cuantitativo posterior sin secuencia aritmética única queda **REFUTADO**. |
| Forma de Weil frente a residuo truncado | La forma completa y la discrepancia numérica de lados truncados son objetos distintos. La segunda no hereda positividad de la primera. |
| H0 lineal frente a cuadrático | No hay ley universal: dependen de paridad, cuarteto desplazado, matriz y normalización. La divergencia es alarma de especificación, no nuevo efecto asintótico. |
| Fase 54 | Las versiones incondicionales de los corolarios que mezclaban normalizaciones o omitían \(I<\infty,\kappa=\infty\) están retiradas; sobrevive sólo la forma condicionada. |
| Fase 64 | El argumento `det Y≡1` que pretendía cerrar la convergencia HB fue retirado por non sequitur. No puede citarse ni como prueba ni como no-go. |
| Fase 65 | Todo rótulo de QED queda subordinado a las correcciones que reconocen `D8.5` como punto abierto de fuerza-RH. |
| LP antiguo frente a LP corregido | `ker_l2(H_L-mu_L)=0` queda **REFUTADO**: el resolvente compacto produce un autovalor inferior con núcleo no nulo. La formulación admisible es `BTG-DIV` y contracción de discos, pero falta probar la divergencia en \(\mu_L\). |
| Outcome A y neutralidad LP | La atribución desde secciones finitas y `mu_ref` no controla el objeto límite. La cuarentena build-neutral es una regla prudente, no una demostración de neutralidad del control. |
| `GAP-Z` | Sólo `MESH` y `BND` tienen las cotas declaradas. `ZERO` queda abierto; no se permite reemplazar la cancelación firmada por suma de valores absolutos ni convertir `GAP-Z` en discriminante. |
| Dominación absoluta de la parte prima | \(|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}\) no es la desigualdad exacta de Li; el fallo como equivalencia ya aparece en \(n=1\). Los no-go absolutos no se transfieren a un lower bound unilateral. |
| Integración por partes Laguerre | La fórmula impresa \(-\int(\psi-y)f'\) tiene signo y borde incorrectos. Debe usarse \(-n+\int(\psi-y)f'=\int(\psi-y+1)f'\) antes de cualquier estimación firmada. |
| Asintótica de la envolvente | Debe conservarse \(\frac{\gamma-1}{2}n\); no cabe dentro de \(O(\sqrt n\log n)\). La cota de la parte prima con \(\log n\) empieza en \(n\ge2\). |
| Proxies E79 | El avatar estable, el conteo de cruces y la deriva monótona fueron retirados por controles posteriores; una cola de precisión insuficiente fue anulada. `mean(d)` cambió silenciosamente a una escala de malla distinta, por lo que toda reutilización exige fijar la definición. `E79.6` permanece **NUMÉRICO/CONJETURAL**. |
| Adjugado y corrección característica | `adj(K)[Z,H]adj(K)=0` es compatibilidad, no fórmula para \([Z,adj(K)]\). `Gamma_t dot mu_t` es regla de la cadena, no una fuente aritmética adicional. |
| Objetos raw/core | La fuente correcta es `C_core` tras extraer exactamente el factor exterior. No se sustituye por un borde aislado, una antisimetrización diferente ni un producto bilateral sin arrastrar el defecto de fase. |
| Realización geométrica | Construcciones abstractas, juguetes y categorías locales no constituyen una superficie absoluta ni una cohomología que transporte los ceros. La lectura geométrica permanece **CONDICIONAL**. |

## Duplicaciones por reparametrización

Se debe contar una sola vez cada avance si sólo cambia representación.

1. Las cadenas índice–Herglotz–Lee–Yang–`Omega7` vuelven al mismo requisito de positividad global.
2. Connes/CCM, estado base, prolate, fuga Feshbach, interpolación Cauchy, divisibilidad y adjugado reducen al mismo residual firmado; no son cierres acumulativos.
3. Kato, cociclo Euler, determinante bordeado, cofactores, Jacobiano, von Mangoldt, conmutador, cáscara Fourier y corrientes Stieltjes/calor son cambios de coordenadas del ancla Gamma–Euler, no pruebas independientes.
4. Li, Weil, LP, Herglotz, Hilbert–Pólya y convergencia de aproximantes reales no se suman como evidencia: son equivalencias o condiciones de fuerza-RH tras la transferencia correspondiente.
5. Una gram positiva, una forma cero-sólo PSD y una matriz de ventana estable pueden coincidir en una sección finita sin aportar la identificación del divisor límite.
6. Las fases 80–89 no forman una escalera de cierres. Las rutas secular/generadora, distribucional/coborde y deformación/Feshbach/rotación regresan a `RDI-ANCHOR`/`IDENT`; reescriben el mismo cuello de botella.
7. `DISCRIMINANT` es un candidato de separación dentro del corte RDI, no un teorema de unicidad. `RDI-CONV`, LP/`BTG-DIV`, completitud mu-libre, `GAP-Z`, `RDP-SHELL` y continuidades direccionales conservan cargas propias.

## Puerta H0 operativa para ideas futuras

Una propuesta no entra en la línea de prueba hasta superar todos los puntos siguientes. Fallar uno la mantiene como **NUMÉRICA**, **CONDICIONAL** o exploratoria según corresponda.

1. **Objeto único.** Especificar coeficientes, dominio, normalización, signo, transformada, simetrización, términos polares/arquimedianos, orden de límites y el objeto completo distinto de todo residuo truncado.
2. **Afirmación etiquetada.** Declarar antes de calcular si se pretende una identidad demostrada, una cota condicional, una medición numérica o una condición de fuerza-RH. Prohibido llamar puente a una equivalencia.
3. **Mecanismo independiente.** Identificar la desigualdad, identidad firmada o construcción externa que no use positividad de Weil, posiciones de ceros, filtro de ceros, divisor ya real ni una métrica adaptada a raíces.
4. **Control adversarial.** Exigir un falsador con cuarteto fuera de línea o análogo plantado, además de controles de coeficientes, conductor, soporte y normalización. Debe poder fallar precisamente donde falla el objetivo.
5. **Objeto límite correcto.** Una medición en `mu_ref`, un autovalor de sección o una malla no puede sustituir \(\mu_L\). Toda proclamación de neutralidad debe demostrarse para las dos construcciones en el objeto límite que usa el teorema.
6. **Uniformidad explícita.** Dar constantes y dependencia simultánea de todas las escalas relevantes: dimensión, centro, ancho, corte primo, cola de ceros, precisión y orden de límites. Una malla o un ajuste no sustituye este punto.
7. **Preservación de información.** Verificar conjugación, soporte transversal, multiplicidad lineal, acoplamiento firmado y términos de borde antes de contraer, promediar, tomar trazas o aplicar una inversa.
8. **Transferencia auditada.** Probar separadamente el paso desde el objeto finito al completo. Si éste produce positividad global, no-anulación o identificación de divisor, registrar **FUERZA-RH** y no descontarlo como detalle técnico. Si se afirma que es el único paso de esa fuerza, demostrar además esa unicidad respecto de las demás obligaciones.
9. **Reproducibilidad.** Congelar datos y versiones; documentar cobertura, precisión, selección de picos, semillas y pruebas de entrada. Ninguna validación posterior puede mezclar variantes sin volver a pasar la puerta.

## Matemática realmente nueva que falta

Falta al menos una aportación de fuerza-RH, y ninguna se obtiene reetiquetando un detector existente. La corrección del blanco de Li abre una opción directa que debe examinarse antes de asumir que toda prueba pasa por LP+IDENT.

1. **Desigualdad unilateral directa para Li.** Debe probar \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\) sin reemplazar el kernel Laguerre por su módulo. Cuando la parte arquimediana es no negativa, esto controla la excursión negativa; en los índices restantes debe conservar el lower bound completo. Ha de mantener juntos los términos de polo, Gamma, borde y primos, no usar una cota de PNT ya equivalente a RH y, si se invoca un control aritmético fuera de línea, definir primero una clase Euler–Gamma comparable que lo contenga.
2. **Convergencia firmada y ancla aritmética.** Debe resolver `GAP-Z` mediante control build-neutral de `ZERO` y, separadamente o mediante una implicación demostrada, identificar el residual Gamma–Euler completo como `RDI-ANCHOR`/`PROFILE-ROTATION-RDI`. Ha de conservar conjugación, soporte transversal y multiplicidad lineal, sobrevivir a un control plantado fuera de línea y producir `ADJ-ARITH-LOCK`/`DIRECTIONAL-IDENT` sin usar el divisor buscado. Una cota absoluta, un promedio, un producto de trazas o una firma finita no bastan. No se presupone que `DISCRIMINANT` sea la única forma posible de aportar esta matemática.
3. **Geometría externa construida.** Debe producir efectivamente categoría, objeto global, diagonal, polarización, lector espectral y triple de Lefschetz con independencia demostrable respecto del operador de ceros. Sólo después podría conectar una positividad geométrica nueva con la forma de Weil sin circularidad.

Una posibilidad adicional sería una teoría no local de transporte fase→inercia que exceda las clases tauberianas y diofánticas ya cerradas, con una desigualdad firmada que pase los mismos falsadores. Mientras no exista una de estas piezas, el estado transversal es **INCOMPLETO**: quedan matemáticas y diagnósticos aprovechables, pero no un cierre lógico.
