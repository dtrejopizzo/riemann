# Plan de cierre de A y selección de la ruta hacia RH

Fecha: 2026-09-08. Documento de planificación para ejecutar después con otro modelo. No demuestra A ni RH y no modifica los papers.

## 1. Decisión recomendada

Para **cerrar A**, concentrar la siguiente campaña en el enlace entre geometría integral, dualidad y determinante metrizado. Suspender la expansión de perfiles de frontera como línea autónoma: retomarla únicamente si una prueba concreta de ese enlace necesita una estimación que todavía falta.

Para **demostrar RH**, no imponer previamente el cierre de toda A. La ruta analítica de primer contacto permite formular un ataque más corto en dependencias, apoyado en fases 118–122. Su ley aritmética central sigue sin probarse. Tener menos dependencias no permite afirmar que sea matemáticamente más fácil.

La primera ejecución hará dos estudios acotados de viabilidad: uno de A, otro de la ley de primer contacto. Elegirá el trabajo posterior por el mecanismo matemático obtenido, no por el número de lemas, sesiones o reformulaciones. Si el objetivo de esa ejecución permanece exclusivamente en A, el estudio directo se conserva como referencia y no desplaza su construcción.

No hay fundamento para prometer un cierre rápido. Sí hay fundamento para eliminar trabajo redundante y atacar antes los obstáculos que pueden invalidar toda una construcción.

## 2. Base documental y precedencia

Se comprobaron 123 directorios `phase-*` y 42 directorios numerados de papers. Esta planificación utilizó los índices generales, la cobertura anterior, búsquedas dirigidas por tres agentes GPT-5.5 y lectura de fuentes decisivas. No constituye una lectura integral ni una nueva auditoría de las pruebas de todos los archivos.

El contrato que gobierna A es [P123_A_ACCEPTANCE_SPECIFICATION.md](../../03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md). El rótulo histórico «A cerrado» en contratos restringidos no satisface ese contrato. Sus diez cláusulas no se reducen en este plan.

Fuentes de trabajo que el ejecutor debe cargar, sin releer todo el corpus:

| Tema | Fuente y uso |
|---|---|
| Alcance real de A/B/C | [Auditoría de referencias](../../03-research/phase-122-row-d-integrity-and-construction/P122_ROWS_ABC_REFERENCE_AUDIT.md): distingue objetos decorados, carácter de Meyer e intersección geométrica. |
| Coeficientes y localización | [P123.121](../../03-research/phase-123-weil-strength-abc/P123_121_COMMON_SMOOTH_ZERO_STRATIFIED_SOURCE.md), [122](../../03-research/phase-123-weil-strength-abc/P123_122_DERIVED_COMMON_SOURCE_COMPOSITION.md), [123](../../03-research/phase-123-weil-strength-abc/P123_123_EQUIVARIANT_SEMILOCAL_COMPOSITION.md), [124](../../03-research/phase-123-weil-strength-abc/P123_124_COMMON_SOURCE_LOCALIZED_DERIVED_TENSORS.md), [125](../../03-research/phase-123-weil-strength-abc/P123_125_ZERO_STRATUM_DERIVED_QUOTIENTS.md): reutilizar sus dominios exactos, no importar una monoidalidad más fuerte. |
| Dualidad y contactos | [A_DUALITY_WORK.md](../../03-research/phase-123-weil-strength-abc/A_DUALITY_WORK.md): leer los encabezados pertinentes y las correcciones posteriores. Contiene contactos derivados, transporte de la unidad, obstrucción del dual fuerte y perfiles. |
| Métrica | [A_MIXED_METRIC_WORK.md](../../03-research/phase-123-weil-strength-abc/A_MIXED_METRIC_WORK.md): determinantes analíticos disponibles; falta el mapa geométrico y la comparación con rulings. |
| Ley de signo | [Cierre 120](../../03-research/phase-120-global-polarization/PHASE_120_CLOSURE.md), [P122.008](../../03-research/phase-122-row-d-integrity-and-construction/P122_008_PHASE121_LOAD_BEARING_AUDIT.md), [P122.028](../../03-research/phase-122-row-d-integrity-and-construction/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md): identidad firmada, detectores y flecha todavía abierta. |
| Alternativa Li | [Frente de reinicio](../RH-MASTER-CONTEXT/LIVE_FRONTIER_AND_RESTART_PLAN.md), papers [37](../../04-papers/37-death-of-the-positivity-family/main.tex) y [38](../../04-papers/38-li-fir-stability/main.tex): blanco unilateral y límites de los filtros. |

Los índices antiguos orientan búsquedas; una corrección específica posterior prevalece sobre sus etiquetas. No repetir los certificados ni los cálculos de contactos existentes salvo que cambien sus entradas, su categoría o la hipótesis que se pretende utilizar.

## 3. ¿Existe A en la bibliografía?

**No se encontró una construcción que satisfaga conjuntamente A.1–A.10.** Es el resultado de esta búsqueda dirigida, no un teorema de inexistencia. Se encontraron componentes importantes y una oportunidad concreta de importación:

| Fuente primaria | Qué ofrece | Qué falta para nuestra A |
|---|---|---|
| Connes–Consani, [On the Jacobian of Spec Z, 2602.15941](https://arxiv.org/html/2602.15941) | Monoide de divisores aritméticos de rango uno con seminorma, interpretación adélica y haces asociados; en infinito, condición de bola unidad sobre secciones. | Categoría estable de correspondencias mixtas sobre el cuadrado y su RR. Es el primer candidato para conservar el dato integral/métrico que el modelo puramente complejo pierde. |
| Connes–Consani, [Absolute Geometry, 2606.06604](https://arxiv.org/html/2606.06604) | Haz absoluto, descripción de stalks, puntos perfectoid y relación con curvas de Tate y Fargues–Fontaine. | Una identificación de puntos o simetrías no importa composición de kernels, dualidad global ni intersección. |
| Connes–Consani, [Riemann–Roch for the ring Z, 2306.00456](https://arxiv.org/abs/2306.00456) y [Scaling Site, 1603.03191](https://arxiv.org/abs/1603.03191) | RR en sus respectivos ámbitos: divisores de la curva aritmética y órbitas periódicas. | RR mixto sobre el cuadrado. No sustituir un resultado de dimensión uno por el resultado requerido. |
| Connes–Consani, [Riemann–Roch strategy, 1805.10501](https://arxiv.org/html/1805.10501) | Levantamiento complejo adélico, descenso tropical y estrategia de existencia de secciones. La introducción identifica la dificultad de la cohomología del cuadrado. | Es una ruta para investigar A.7/A.8, no el teorema completo que buscamos. |
| Cisinski–Tabuada, [1111.0257](https://arxiv.org/html/1111.0257), teoremas 1.7 y 1.11 | Lefschetz y HRR no conmutativos; hipótesis explícitas de suavidad/properness según el resultado. | Probar que el dominio aritmético pertinente satisface las hipótesis; además construir la comparación métrica. Nuclearidad de Fréchet no implica properness dg. |
| Marcolli–Tabuada, [1105.2950](https://arxiv.org/abs/1105.2950) | Intersecciones vía Hochschild y equivalencia numérica en motivos no conmutativos. | Realización de nuestra fuente, topología del cociente completado y conservación del sector mixto. No importa automáticamente la teoría de rango infinito. |
| Deninger, [2508.05329](https://arxiv.org/abs/2508.05329), §5 | Vectores de Witt racionales como correspondencias relativas finitas bajo hipótesis algebraicas precisas. | Functor hacia el cuadrado de A y contacto diagonal derivado. Ayuda a B; no define A mediante valores de Lambda. |
| Meyer, [math/0412277v3](https://arxiv.org/abs/math/0412277v3) | Realización nuclear y fórmula de carácter. | Identificar ese carácter con la sombra geométrica de A. Se importa en C. |
| Connes–Consani–Moscovici, [Zeta Spectral Triples, 2511.22755](https://arxiv.org/html/2511.22755#S8) | Aproximantes espectrales; §8 declara pendientes simplicidad/paridad del mínimo y aproximación del autovector que permita la convergencia. | No proporciona la positividad o identificación límite que cerrarían RH. |

Se revisaron además las fuentes locales `2510.08033` y `2512.01811` de `00-references/papers-nuevos/D`: sus resultados de superficies aritméticas ordinarias requieren una geometría cuya identificación con nuestro cuadrado no está construida. El puente [Morishita, 2508.15971](https://arxiv.org/abs/2508.15971), teorema 3.6 de la versión local v5, da mapas compatibles de flujos/órbitas; no una equivalencia de cohomologías con polarización.

**Importación prioritaria propuesta:** geometría de divisores y secciones de 2602.15941 + fuente común P123.121–125 + cálculo relativo de kernels. La realización que los una es un problema nuevo y explícito; no se afirma que exista por juntar estas referencias.

## 4. Primera campaña de A: dos pruebas de viabilidad decisivas

### A-V1. Realización geométrica y dualidad de la misma categoría

**Entradas:** fuente común P123.121–125; haces de divisores del Jacobian; dualidad clásica y triángulo de frontera de `A_DUALITY_WORK.md`.

**Candidata:** correspondencias geométricamente localizadas, con condiciones relativas de soporte/perfección que permitan composición, y una realización en bimódulos de la fuente común. La diagonal debe seguir siendo la unidad completa. Mantener separados el dominio de correspondencias y el ideal trazable.

Trabajo concreto:

1. Definir el functor de realización sobre haces de divisores y correspondencias finitas generales, antes de elegir la familia aritmética de B. Precisar qué categoría conserva las restricciones métricas al pasar a un contexto estable. Una envolvente estable por sí sola no demuestra esa conservación.
2. Exigir en un único dominio la diagonal, ambos rulings y contactos mixtos no nulos, junto con sus conos y composiciones. Los contactos analíticos ya construidos sirven para detectar pérdidas de información; no son automáticamente los contactos aritméticos de B.
3. Buscar la dualidad mediante adjuntos relativos y el objeto dualizante. Calcular su cuadrado, incluyendo el posible giro de Serre. Si se propone una media raíz dualizante, construirla o explicar su descenso; no elegirla tácitamente.
4. Aplicar la candidata al triángulo fuente `I -> B -> B/I`. Calcular las imágenes de sus flechas, el bidual y la evaluación. Este test debe superar la pérdida de frontera del cociente de Hom fuerte ya documentada.
5. Probar reversión de composición, unidad fija y compatibilidad semilocal. Cambiar a categorías condensadas/bornológicas solo si se exhibe cómo resuelven este test; el nombre del formalismo no es una prueba.

**Salida que justifica continuar:** functor y dualidad reales en un dominio que contiene los objetos anteriores, con una lista precisa de las extensiones aún necesarias. **Salida de descarte:** un contraejemplo de bidualidad, pérdida del contacto o giro inevitable incompatible con A.4. Un resultado local no se etiqueta como A.4 global.

### A-V2. Extensión del determinante intrínseco, antes de ampliar completaciones

**Entradas:** misma candidata A-V1; rulings y su norma intrínseca; determinantes de contactos y sus leyes de cambio de ecuación; `A_MIXED_METRIC_WORK.md`.

Trabajo concreto:

1. Construir desde las secciones de la fuente el dato determinante que se pretende extender. Distinguir complejos perfectos absolutos, determinantes relativos con cono perfecto y determinantes nucleares. No tomar el determinante ordinario de un complejo infinito.
2. Comparar objetos y trivializaciones en los sectores ruling–ruling, ruling–mixto y mixto–mixto. El primer sector debe recuperar la norma `exp(-d1*d2)`, con la convención correcta entre norma y norma al cuadrado.
3. Calcular los cambios bajo sustitución de ecuación local por una unidad, adición de divisores y cambio semilocal. Usar los resultantes y normas de unidades ya obtenidos para contactos; calcular el cociclo de discrepancia que aún separa ambas realizaciones.
4. Probar que ese cociclo admite la trivialización canónica requerida por la geometría y que esta preserva la métrica. Una igualdad de curvaturas en cero, o ajustar una constante para que coincidan números, no da esa trivialización.
5. Declarar una clase efectiva desde secciones/ciclos de la fuente. No tomar como efectivos todos los objetos de una categoría estable, pues sus desplazamientos cambian el signo en K0. Tampoco identificarla con sumas de cuadrados de operadores.

**Salida que justifica continuar:** comparación natural de líneas metrizadas en un sector genuinamente mixto, con invariancia principal y un mecanismo explícito para extenderla. **Salida de descarte:** la realización borra el dato integral de secciones, la métrica no desciende o la comparación exige asumir la forma de Weil/signo deseados.

Ambas pruebas son filtros de la arquitectura, no una promesa de que la candidata pasará. Si una falla, la siguiente tarea es su obstrucción matemática concreta o una candidata que la cambie; no más perfiles de frontera sin relación con ella.

## 5. Programa completo de A una vez elegida una candidata viable

| Paquete | Trabajo de construcción | Criterio de cierre y cláusulas |
|---|---|---|
| A-I: fuente y geometría | Extender la realización a todas las cartas declaradas; localizar en el cuadrado; descenso y coherencia triple. Reutilizar los tensores derivados relativos existentes. | Un único carrier y dominio geométrico estable: A.1, A.2. |
| A-II: operaciones | Extender composición y dualidad de A-V1; demostrar estabilidad bajo la completación elegida, continuidad y unidad completa. | Fórmulas de composición, bidualidad y reversión válidas en el mismo dominio: A.3, A.4. |
| A-III: sombra | Construir sombra diagonal cíclica antes de scalarizar, distinguir contactos de exceso y probar localización. Compararla con el determinante en su dominio permitido. | A.5 con target y límites explícitos. La unidad no necesita traza escalar finita. |
| A-IV: numérico | Definir radical contra TODOS los tests trazables. Probar ideal, estabilidad por dagger, cerradura, cociente Hausdorff y continuidad de operaciones. | A.6 con ruling plane y sector mixto no nulo de rango compatible con el kernel completo; no basta inyectividad de un sector local. |
| A-V: efectividad y RR | Extender A-V2: invariancia principal, biextensión, restricción, convergencia e igualdad RR; probar el descenso de efectividad realmente utilizado. | A.7, A.8. Si la posterior ruta Hodge usa crecimiento de secciones, demostrar además la desigualdad de existencia necesaria; un grado de determinante no la sustituye. |
| A-VI: comparación y cierre | Control clásico por un functor tipado: curvas finitas, grafos finitos no invertibles, diagonal, transposición, intersección y efecto. Revisar independencia de B/C/D. | A.9, A.10 y auditoría conjunta de A.1–A.10. |

El control clásico se utiliza desde A-V1 para descartar errores; A-VI comprueba su compatibilidad con la construcción final. Los paquetes no son seis teoremas conocidos pendientes de transcribir: A-I, A-II y A-V contienen problemas de investigación genuinos.

**Cierre de A:** todas las cláusulas satisfechas en la misma teoría, sin flechas condicionales. Si solo se cierra un sector, informar cuál y qué clausula global sigue pendiente.

## 6. B/C/D si se continúa la prueba tipo Weil

**B — pasar de etiquetas a contactos geométricos.** Realizar las correspondencias de Witt mediante el functor compatible con A. Derivar el contacto diagonal que produce el complejo ciclotómico, en vez de adjuntarlo como decoración. Demostrar el resultado para la familia general; la comparación entre un primo, su cuadrado y un producto de primos detecta si se obtuvo un contacto lineal incorrecto. No repetir pruebas pequeñas ya existentes sin un cambio de construcción. Unidad/exceso se trata aparte. La masa `log|Phi_n(1)|` se deduce al final.

**C — un solo teorema de comparación.** Construir una realización de la sombra de A en el complejo de Poisson de Meyer que conserve acción, dualidad y términos Tate. Probar que contacto finito, término Gamma y exceso identidad dan conjuntamente la fórmula explícita, primero en un núcleo común y luego en el dominio suficiente para Weil. Una coincidencia de listas de coeficientes no sustituye ese functor. Declarar órdenes de límites; no imponer uniformidad en todas las ventanas si basta controlar cada soporte compacto.

**D — elegir una de dos demostraciones.** O bien índice de Hodge mediante la geometría/efectividad y RR ya construidos, o bien ley aritmética de primer contacto del apartado siguiente. No exigir resolver las dos. En ambas se debe demostrar el signo primitivo, sin incorporarlo a la definición de la métrica o del cono. La semidefinitud basta si cubre el criterio usado; no añadir una clasificación global de igualdad innecesaria.

Una prueba directa de RH no rellena retroactivamente los funtores de A/B/C ni toda una versión geométrica de D.

## 7. Ruta más directa: signo mediante primer contacto

Esta es la alternativa prioritaria para un intento de RH con menos construcción previa. Reutiliza [P122.002](../../03-research/phase-122-row-d-integrity-and-construction/P122_002_FIRST_CONTACT_COMPACTNESS_THEOREM.md), el certificado inicial existente y las correcciones de [P122.008](../../03-research/phase-122-row-d-integrity-and-construction/P122_008_PHASE121_LOAD_BEARING_AUDIT.md).

El objetivo analítico es demostrar `q_T(F)=-B_nuc,T(F,F)>=0` para cada ventana y todo test primitivo de su dominio. Una falla posterior a la ventana certificada proporciona, bajo las hipótesis del teorema de primer contacto, un estado nulo no trivial. Falta excluirlo mediante aritmética.

El cálculo disponible es

```
E_eff(F) = ||(E_q,T - E_p,T) h_F||^2 / log(q/p).
```

La ecuación armónica solo fuerza flujo constante. No fuerza energía cero. La tarea nueva es obtener de la fuente aritmética, para el estado de primer contacto, la transmisión crítica y el pegado que anulan el defecto. La especificación exacta de las dos condiciones está en [P122_D_SPECIFICATION.md, §8](../../03-research/phase-122-row-d-integrity-and-construction/P122_D_SPECIFICATION.md) y su condición de borde en [P122.029](../../03-research/phase-122-row-d-integrity-and-construction/P122_029_LIONS_MAGENES_TRANSMISSION_AUDIT.md).

Orden de ataque:

1. Trabajar sobre la fuente entera con sucesor aditivo, isometrías multiplicativas y Gamma ya construida; escribir una relación global candidata con todos sus términos de borde.
2. Derivar una identidad de Green/reciprocidad para esa relación. Identificar el paso que selecciona datos aritméticos reales y las dos orientaciones antes de perderlas en la traza.
3. Probar la condición crítica de transmisión y la anulación del flujo requeridas. Deben ser consecuencias; no condiciones añadidas a la definición del estado.
4. Aplicar la rigidez ya disponible, con TODAS sus hipótesis, para excluir el primer contacto. Pasar por exhaustión al dominio de Weil.

**Primer entregable:** una identidad global con un término nuevo controlado, o una refutación de la relación candidata. No otro detector equivalente de flujo cero.

La factorización `q=||X F||^2-||Y F||^2` y una contracción que implicaría el signo son coordenadas legítimas del problema. Su equivalencia con RH no las descarta; obliga a demostrar la contracción desde propiedades aritméticas nuevas. Los no-go del corpus se usan únicamente con su clase exacta de hipótesis.

## 8. Otras rutas y criterio para cambiar de prioridad

| Ruta | Objetivo restante útil | Cuándo activarla |
|---|---|---|
| Primer contacto | Ley global que impide un estado nulo no trivial en la primera pérdida de signo. | Primera alternativa directa, por disponer ya del detector, regularidad y reducción. |
| Connes–CCM espectral | Simplicidad/paridad necesarias y estimación que identifique los aproximantes de espectro real con Xi en una topología holomorfa suficiente. | Solo si aparece un nuevo control de gap/residuo y normalización que sobreviva al límite. Cercanía numérica o autoadjunción finita no bastan. |
| Li–Laguerre | Cota unilateral firmada para todos los índices, con continuación primo–polo pareada. | Si aparece una identidad aritmética de compensación o una estimación uniforme que preserve el signo. |
| Weil completo | A fuerte, realización B, comparación C y signo D. | Prioritario para cerrar A como teoría, o si la nueva geometría produce el mecanismo de signo que falta en las rutas directas. |

Blanco exacto alternativo de Li, en las convenciones del frente de reinicio:

```
f_(n,eps)(y) = y^(-1-eps) L_(n-1)^(1)(log y),
lambda_n^prime
 = lim_(eps down to 0) integral_1^infinity (psi(y)-y+1) f'_(n,eps)(y) dy,
lambda_n^prime >= -lambda_n^arch  para n>=8.
```

El rango 1–7 tiene certificado separado en ese frente. El límite pareado, la dependencia en n y las colas son obligaciones del teorema; ninguna manipulación de sumas divergentes separadas es admisible. Los filtros de paper 38 no prueban esta cota.

En la variante espectral, fijar primero un normalizador no nulo y el dominio complejo de convergencia. Una convergencia holomorfa local uniforme hacia una función no idénticamente nula permitiría usar Hurwitz para excluir ceros fuera de la línea en ese dominio. Justificar precisamente esa convergencia, y su cobertura de los posibles ceros, es el problema; no se presupone.

## 9. Ejecución económica y entregables

Usar GPT-5.5 para extracción de fuentes, cotejo de hipótesis y una primera construcción por paquete. Una revisión independiente debe concentrarse en la nueva flecha decisiva, no volver a leer cada lema heredado. GPT-5.4 es una opción del usuario si está disponible en su sesión; no es necesario para este plan.

Primera ronda, como máximo dos trabajos matemáticos independientes:

1. **Trabajo A:** resolver A-V1 y formular el cociclo/obligación concreta de A-V2 sobre esa misma candidata. Si la dualidad falla, entregar la obstrucción antes de construir más completaciones.
2. **Trabajo directo:** proponer y analizar una sola ley global de primer contacto con los datos de fases 120–122. Si el encargo es exclusivamente cerrar A, sustituirlo por A-V2 a partir de una interfaz de fuente común explícita.

Después se elige una línea principal. No lanzar simultáneamente proyectos separados de Hodge, KYP, de Branges, Fock, entropía y positividad si terminan en la misma contracción sin un mecanismo nuevo.

Cada entrega debe contener únicamente:

- enunciado nuevo con cuantificadores y dominio;
- prueba, o el paso preciso que sigue abierto;
- referencias importadas con sus hipótesis verificadas;
- cláusula de A o flecha hacia RH que cambió;
- siguiente tarea concreta, si existe progreso que la justifique.

Una tentativa refutada descarta esa tentativa. Un teorema difícil todavía abierto no se declara imposible ni cerrado. No se cambia de notación para simular avance.

**No crear nuevas fases, ampliar memorias ni editar papers durante esta primera campaña.** Conservar solo el entregable matemático necesario para evaluar la ruta. No regenerar certificados ya aceptados por rutina.

## 10. Prompt de traspaso

> Ejecutá el plan PLAN_PRIORITARIO_2026-09-08.md, empezando por A-V1. El objetivo de esta ejecución es producir un functor de realización y una dualidad contravariante en la misma categoría que contiene la unidad, rulings y un contacto mixto, o aislar su obstrucción concreta. Usá P123.121–125 y las correcciones de A_DUALITY_WORK; no repitas las construcciones locales ya registradas. Investigá la importación de los haces de divisores de Connes–Consani 2602.15941 conservando sus datos integrales y métricos. Probá temprano el triángulo I→B→B/I y el giro del bidual. No confundas una involución covariante con dagger, una categoría de contactos con la unidad global, ni nuclearidad con properness. Si esa arquitectura funciona, pasá a A-V2 antes de ampliar las completaciones. No edites ningún paper. Reportá la nueva flecha demostrada, las hipótesis que permanecen abiertas y el alcance exacto. No declares A cerrada hasta satisfacer A.1–A.10.

Para priorizar RH en lugar de A, reemplazar la primera tarea del prompt por el apartado 7. Ese cambio conserva los resultados de A como recursos, pero no exige completar una teoría geométrica entera antes de atacar el signo.
