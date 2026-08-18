# Auditoría de fases 000–025

## Criterio y alcance

Esta auditoría cubre cada directorio de `03-research` cuya fase numérica está entre 000 y 025. Las fases **001** y **002 no existen en el árbol**; se registra la ausencia, no se les atribuye trabajo ni resultado. Se leyeron los documentos Markdown sustantivos, incluidos planes, informes, veredictos, cierres, auditorías y bitácoras de prueba; los programas y datos se contrastaron sólo cuando el texto apoyaba un hecho numérico o reproducible. Los artefactos técnicos auxiliares (código, CSV, imagen, PDF/TeX, copia de seguridad y `.DS_Store`) no se cuentan como documentos matemáticos, salvo que su resultado estuviera incorporado y discutido en un Markdown.

Leyenda: **PROBADO** = derivación interna completa o identidad clásica correctamente usada; **CONDICIONAL** = depende de una hipótesis declarada; **NUMÉRICO** = experimento, aunque sea reproducible; **CONJETURAL** = programa o implicación no demostrada; **REFUTADO** = el propio expediente invalida la vía; **EQUIVALENTE-A-RH** = la meta es otra formulación de RH; **INCOMPLETO** = falta un enlace necesario. “Probado” significa probado en el expediente y no certificación externa de todas las referencias o de cada paso largo.

## Cobertura documental

| Fase | Cobertura de documentos sustantivos | Estado de cobertura |
|---|---|---|
| 000 | `0A1-weil-guinand-translation`; `0A2-connes-compression`; `0A3-debranges-structure-function`; `0B-cartography-first-pass`; `phase0-plan` | Completa: 5/5 |
| 001 | Directorio ausente | Ausencia registrada |
| 002 | Directorio ausente | Ausencia registrada |
| 003 | `engine-spec`; `phase3-plan` | Completa: 2/2 |
| 004 | `B2-THEOREM`; `B3-KREIN-STRUCTURE`; `PAPER-A`; `PHASE4-WORK-PROGRAM`; `RH-ENDGAME`; y en `proofs/`: `00-PROOF-LOG`, `A1-operator-and-compression`, `B2-semiboundedness`, `B2.4a-break-attempt`, `B2.4a-closability`, `B2.4a-de-branges-norm`, `CLOS1-audit-and-RFB`, `Day10-kernel-audit`, `Day11-theorem-audit`, `Day12-density-scaling-law`, `Day13-DENS1-audit`, `Day14-reduction-audit`, `Day15-K5-audit`, `Day16-carleson-and-RFB`, `Day17-verification`, `Day18-quadrature`, `Day19-pair-correlation-input`, `Day20-threshold-correction`, `Day21-offline-and-coercivity`, `Day22-coercivity`, `EF-identity-audit`, `closure-in-HEgamma`, `space-correction-strip-hardy` | Completa: 28/28; manual LaTeX excluido por no ser documento matemático independiente |
| 005 | `B2-semilocal-residual`; `B3.1-connes-comparison`; `B3.2-de-branges-comparison`; `M5-T1-T2-proofs`; `M5-classification-pure-theory`; `Phase2-Rp-Euler`; `T3-anatomy`; `T4-seed`; `experiments/M4-D2-results`; `experiments/Phase3-results` | Completa: 10/10 |
| 006 | `M-OS-1-S1-setup`; `M-OS-2-S2-local-REFUTATION`; `S2-followup-incoherence`; `S2f-PROGRESS-CANDID` | Completa: 4/4 |
| 007 | `P7-OPEN-CORE-carleson-saturation`; `P7b-second-order-sinekernel-bridge`; `connes/P7c-connes-core-same-wall` | Completa: 3/3 |
| 008 | `GATE-B-verdict-sixth-language`; `PLAN-RH-PHASE8-heat-flow`; `RT-coupled-verdict`; `SEED-results-and-candid-caveat`; `UPPER-TAIL-verdict` | Completa: 5/5 |
| 009 | `M9.1-N6-spearhead-verdict`; `PLAN-RH-PHASE9-unconditional-universality`; `T9A-verdict-wrong-sign`; `T9cal-DELIVERABLE-exchange-rate` | Completa: 4/4 |
| 010 | `DEEPRUN-analysis-M10.1-M10.3`; `M10.1-verdict-degenerate-hodge`; `M10.2-verdict-regularized-gap-survives`; `M10.3-verdict-uniform-frame-S(T)`; `M10.4-verdict-route-priced-capstone-holds`; `PHASE-10-NEW-MATHEMATICS-the-cohomological-turn`; `REPORT-M10.1-to-M10.3-cohomological-turn` | Completa: 7/7 |
| 011 | `PLAN-RH-PHASE11-hyperbolicity-route`; `M11.2-verdict-interlacing-total-positivity`; `M11.3-verdict-preserver-blind-MSS-pivot`; `M11.4-5-verdict-capstone-holds-richest-positivity` | Completa: 4/4 |
| 012 | `PLAN-RH-PHASE12-log-correlated-upper-bounds`; `M12-VERDICT-capstone-escaped-new-barrier`; `M12.8-verdict-freezing-live-frontier`; `M12.9-verdict-moment-problem-candid-status`; `M12.10-the-meta-obstruction`; `M12.11-N7-closure-attempt-littlewood` | Completa: 6/6 |
| 013 | `RESULT-omega-class-structure-of-chaos` | Completa: 1/1 |
| 014 | `ANCHOR-framework-a-classification-of-zero-absence`; `AUDIT-P7-structural-line-collapse`; `BREAK-N8-the-anchor-asymmetry`; `M14.1-verdict-additive-divisor-motohashi`; `M14.2-verdict-nontrivial-spectral-modification`; `M14.3-VERDICT-self-referential-close-the-line`; `N8-the-density-to-absence-gap`; `STAGE1-2-anchor-vs-definiteness-the-verdict`; `STRATEGIC-where-omega-touches-the-zeros` | Completa: 9/9 |
| 015 | `00-PHASE-15-overview`; `M1-arithmetic-intersection-pairing`; `M2-ample-cone-edge-positivity`; `M3-arithmetic-hodge-index`; `M3-attempt5-arithmetic-hodge-index-exists`; `M3-attempt6-elliptic-control-heights-vs-zeros`; `M3-attempt7-constructing-the-zero-cohomology`; `M3-attempt8-the-kahler-form`; `M3-genuine-attempts-on-the-core`; `M4-the-chosen-direction-archimedean-modular-omega`; `M5-the-lefschetz-dichotomy-closure`; `M6-the-prismatic-route-assessment`; `M7-advisor-incompleteness-theorem-audit`; `M8-front1-proof-audit-REFUTED`; `M9-kosmos-run-1-assessment`; `M10-arakelov-equivalence-audit`; `SYNTHESIS-M1-to-M3-and-the-precise-gap` | Completa: 17/17 |
| 016 | `00-SURF-SPEC-SHEET`; `01-pillar1-triage-three-routes`; `02-pillar2-prototype-resonance-wall`; `03-residue-pairing-nontrivial`; `04-MSZ-pairing-hits-CAP`; `05-resonance-pairing-definite-THEOREM`; `06-hunt-indefinite-object`; `07-pontryagin-the-indefinite-object`; `08-debranges-herglotz-clean-criterion`; `09-self-adjoint-construction` | Completa: 10/10 |
| 017 | `00-SURF-2.0-design`; `01-SURF-A-triage`; `02-involution`; `03-route2-testbed`; `04-SURF-B-resolvent` | Completa: 5/5 |
| 018 | `01-negative-directions-portrait`; `02-explicit-formula-coupling` | Completa: 2/2 |
| 019 | `00-PHASE19-CLOSURE`; `01-camino3-forward-flow`; `02-omega-rate-freezing`; `03-bsmooth-freezing`; `04-random-mult-maximum`; `05-k2-from-erdjoskac` | Completa: 6/6 |
| 020 | `00-PHASE20-DESIGN`; `00b-PASO0-analisis-dirichlet`; `01-proof-explicit-formula-omega`; `02-proof-error-correlation` | Completa: 4/4 |
| 021 | `00-setup`; `01-parity-and-geometry`; `02-exclusion-principle` | Completa: 3/3 |
| 022 | `00-setup`; `01-modified-explicit-formula`; `02-invariants`; `03-spectral-rigidity` | Completa: 4/4 |
| 023 | `00-setup`; `01-exact-hadamard-effect`; `02-structure-function-analysis`; `03-barrier-formulation` | Completa: 4/4 |
| 024 | `00-setup`; `01-lower-bounds-bj`; `02-local-profile`; `03-rigorous-chaos` | Completa: 4/4 |
| 025 | `00-setup`; `01-audit-classical`; `02-deBruijn-Newman`; `03-krein-lp`; `04-verdict` | Completa: 5/5 |

## Reconstrucción por fase

### 000 — Traducción de Weil y cartografía

**Objetivo.** Identificar el detector localizado como forma de Weil, y separar el error técnico de truncación de la positividad global.

**PROBADO / heredado clásico.** La fórmula explícita y el criterio de Weil dan `B ⪰ 0 ⇔ RH`; `Q` se interpreta como compresión localizada, no como objeto nuevo. La cartografía separa la estimación de colas, plausiblemente armónica e incondicional, de la positividad total.

**CONDICIONAL / CONJETURAL.** La identidad exacta con el operador de Connes, el dominio de formas, la completitud y ausencia de contaminación espectral siguen abiertos. La traducción de de Branges exige verificación especializada y supera el obstáculo Conrey–Li sólo si identifica una cadena nueva.

**Dependencia y herencia.** Funda 003–004; transmite el test decisivo: fidelidad no implica positividad, y positividad global es **EQUIVALENTE-A-RH**.

**Reauditoría.** `0A1` usa alternativamente `Q=M_zeros-M_arith` y la forma de Weil; para la fórmula completa la diferencia es cero. Debe fijarse una sola convención, truncación y signo, antes de atribuir una matriz espectral al objeto de Connes.

### 003 — Desigualdad uniforme y especificación empírica

**Objetivo.** Calibrar el detector y formular la desigualdad límite (LB).

**NUMÉRICO.** Los controles, la localidad, la ley aproximada en `δ²` y la amplificación en `J` son referencias de implementación, no teoremas sobre zeta. La especificación además documenta rutas ciegas: Li, Mercer/PSD construido, TDA y Gram sólo de ceros.

**PROBADO en el expediente / límite.** La reducción de (LB) a positividad de Weil es correcta: **EQUIVALENTE-A-RH**. El plan declara que computación finita no puede resolver el paso uniforme.

**Herencia.** Provee el instrumento para 004 y la taxonomía de falsificadores. No demuestra RH ni fidelidad de compresión.

### 004 — Operador semibounded, Kreĭn y cierre de la rama

**Objetivo.** Construir una realización operatorial de la forma de Weil, aislar coercividad, y atacar el signo mediante geometría de Kreĭn.

**PROBADO en el dossier.** Integración por partes, estimaciones verticales, cuadratura, separación profundo/somero, realización con simetría fundamental y el no-go de la dependencia en profundidades se presentan como incondicionales. El no-go es el resultado más robusto: acotar `||K||≤1` desde ceros equivale a positividad aritmética, por tanto a RH.

**CONDICIONAL.** La coercividad uniforme usa (H), una densidad de ceros en intervalos cortos uniforme; el expediente reconoce que no está establecida incondicionalmente. Bajo (H), la equivalencia entre RH y el signo del fondo espectral es una reformulación.

**REFUTADO / no-go.** La esperanza de extraer palanca de las profundidades fuera de línea queda cerrada por el teorema de no-go. Magnitud, muestreo y densidad no fuerzan el signo.

**Herencia.** Entrega a 005–018 el muro CAP/SURF/de Branges: construir la realización es distinto de demostrar positividad. `RH-ENDGAME` deja como única ruta estructural una factorización positiva, que es **EQUIVALENTE-A-RH**.

**Reauditoría crítica.** `B2-THEOREM` llama a partes “incondicionales” y a la vez hace depender la coercividad central de (H); `PAPER-A` corrige el alcance, pero todo enunciado de “realización semibounded fiel” debe etiquetarse **CONDICIONAL en (H)** hasta revisión independiente. La bitácora muy extensa contiene correcciones sucesivas: se requiere revisión lineal de dominios, normalizaciones y la transición de formularios a operadores antes de convertirla en teorema externo.

### 005–009 — Ramas estructurales, residuos, Carleson, calor y universalidad

**Objetivo conjunto.** Buscar un mecanismo unilateral o geométrico que transforme información local/estadística en positividad uniforme.

**PROBADO / diagnóstico.** 005 clasifica formas residuales y compara Connes/de Branges; 006 **REFUTA** localmente S2 y documenta incoherencia; 007 identifica saturación Carleson y que el puente de segundo orden vuelve al mismo núcleo; 008 produce veredictos numéricos de flujo de calor, colas y acoplamiento; 009 formaliza la tasa de intercambio y el signo incorrecto de la correlación.

**NUMÉRICO y CONJETURAL.** Los experimentos de 005, 007–009 ilustran escalas y controles; no prueban cotas uniformes. Los puentes Connes/de Branges y la universalidad requerida permanecen **INCOMPLETOS**.

**No-go y herencia.** La salida es el “wrong-sign capstone”: las herramientas disponibles dan cotas en la dirección equivocada. Se hereda a 010–014 como `U`, el control uniforme de clustering/correlación, no como avance hacia una prueba.

### 010 — Giro cohomológico y marco de Riesz

**Objetivo.** Reinterpretar la forma como índice de Hodge regularizado y hallar una herramienta bidireccional mediante marcos de Riesz, `A₂` y regularidad extremal de `S(T)`.

**NUMÉRICO.** La envolvente lorentziana finita, su degeneración, el hueco regularizado y la ley `λ_min(G)=π² β_min²/6` se reportan como medidas. El análisis profundo corrige la lectura optimista de M10.3: los datos no alcanzan pares de Lehmer extremos.

**CONDICIONAL / EQUIVALENTE-A-RH.** `RH ⇔` hueco de marco uniforme `⇔ A₂` uniforme, bajo el diccionario funcional invocado; la uniformidad de `A₂` es abierta. Selberg controla comportamiento típico, no el extremo necesario.

**Resultado franco.** El giro no cruza el muro: vuelve a `U` y sufre el mismo coste de resolución. Hereda a 011–012 una descripción más natural, no una prueba.

### 011 — Hiperbolicidad, Jensen y MSS

**Objetivo.** Evitar la positividad cuadrática usando entrelazamiento, preservadores y familias MSS.

**PROBADO / NUMÉRICO.** Se observa entrelazamiento en el rango ensayado y se identifica el desplazamiento como derivación; el preservador es ciego a la aritmética. La equivalencia algebraica “raíces reales de un polinomio real ⇔ forma de Hermite semidefinida positiva” es clásica.

**REFUTADO como escape.** La ruta termina de nuevo en positividad total/Hermite y en `U`; la promesa de un mecanismo ajeno a positividad queda invalidada en el propio veredicto. Una realización MSS aritmética es sólo **CONJETURAL**.

### 012–013 — Caos log-correlacionado y clase omega

**Objetivo.** Atacar extremos mediante cotas superiores deterministas, teoría de momentos y congelamiento; 013 aísla la estructura de la clase omega.

**PROBADO / aportación independiente.** La identificación del exponente diagonal `k²` a partir de la estructura multiplicativa/Poisson y parte de la taxonomía omega es independiente de posiciones de ceros.

**CONDICIONAL / CONJETURAL.** El paso que convertiría control estadístico de extremos en exclusión de ceros fuera de línea es N7 y está declarado heurístico. El problema supercrítico de momentos para órdenes altos y el congelamiento fino permanecen abiertos.

**Resultado.** La fase evita formalmente el capstone de signo, pero no alcanza RH: es **INCOMPLETA**, con un segundo muro probabilístico–determinista. 014 cierra la pretensión de que omega por sí sola vea los ceros.

### 014 — Anclas y cierre de omega→ceros

**Objetivo.** Distinguir densidad de ausencia y preguntar por un ancla de positividad en la línea crítica.

**PROBADO / diagnóstico.** Motohashi y las identidades espectrales dan densidad, no ausencia. El peso omega resulta autorreferencial al expresarse por potencias de zeta; la línea omega→ceros queda **REFUTADA** para el objetivo de RH.

**CONJETURAL.** La clasificación de anclas (ACC) es evidencia metodológica, no teorema. El ancla central/Hodge global es una pregunta abierta.

**EQUIVALENTE-A-RH.** La ausencia uniforme y la positividad de Weil reaparecen como la misma barrera; se transmite a 015 como búsqueda de una superficie aritmética.

### 015 — Hodge aritmético, Lefschetz y superficie ausente

**Objetivo.** Construir emparejamiento, cono amplio y parte primitiva que imiten el índice de Hodge de cuerpos de funciones.

**PROBADO en el expediente.** M1–M2 construyen identidad de traza, efectividad y positividad del cono amplio; la síntesis afirma una reducción precisa de RH a positividad de la parte primitiva. Se corrige explícitamente una falsa bicondicional Arakelov–RH y se **REFUTA** el supuesto “Frente 1” de prueba.

**EQUIVALENTE-A-RH / INCOMPLETO.** M3, el índice de Hodge aritmético, es RH en otra forma. Falta la superficie global que porte cohomología de ceros, Lefschetz y la relación alturas–ceros. La ruta prismática sólo da estructura local; no sustituye la realización global.

**Reauditoría.** Hay una tensión terminológica: “cohomología cero-portadora construida” no equivale a objeto geométrico con correspondencias y positividad. Deben separarse con rigor construcción funcional, interpretación geométrica y teorema de Hodge antes de reclamar una realización.

### 016–018 — SURF, resonancias e imagen de direcciones negativas

**Objetivo.** Realizar geométricamente el espacio indefinido y entender qué aspecto tendría un cero fuera de línea.

**PROBADO / diagnóstico.** 016 muestra que el emparejamiento natural Maass–Selberg–Zagier es definido/no diagonal para el fin deseado; se **REFUTA** como detector de índice negativo. También se registra que la condición específica de de Branges fue **REFUTADA** por Conrey–Li. 017 separa simetría de positividad y el testbed de Ruta 2 resulta ciego a `γ`; 018 demuestra que el perfil local de una dirección negativa no tiene protección local y vuelve a requerir correlación uniforme.

**INCOMPLETO / EQUIVALENTE-A-RH.** Una realización de resonancias con el emparejamiento correcto implicaría RH, pero no está construida; el criterio Herglotz de `ξ'/ξ` es RH bajo otro nombre. Herencia: se abandona la obtención espectral directa y se abre el flujo directo omega de 019.

### 019–020 — Flujo directo omega y barrera de información

**Objetivo.** Obtener matemáticas independientes desde primos hacia omega, momentos y caos, y medir si puede volver a los ceros.

**PROBADO / NUMÉRICO.** Selberg–Delange respalda los promedios y la derivación de `k²`; los ensayos B-smooth y de máximos muestran regímenes preasintóticos, no congelamiento límite. 020 corrige el diseño inicial: `F_q=ζ^qG_q` hace que la información de ceros no entre como se suponía; establece identidades y separaciones de información dentro del marco declarado.

**EQUIVALENTE-A-RH / INCOMPLETO.** La tasa de convergencia relevante de correlaciones es RH-equivalente; no hay puente inverso. El posible refinamiento cuantitativo de pesos multiplicativos queda abierto pero no es una prueba de RH.

### 021–023 — Defecto finito de Pontryagin y barrera explícita

**Objetivo.** Suponer finitamente muchos paquetes fuera de línea, deducir su geometría y buscar una contradicción aritmética.

**PROBADO en el expediente.** 021 obtiene paridad: una falla de RH cuesta pares de direcciones negativas, y formaliza el régimen de Pontryagin bajo finitud. 022 deduce la fórmula explícita modificada, oscilaciones y energía del defecto bajo Hipótesis D; identifica el límite Paley–Wiener. 023 calcula el efecto Hadamard y formula con precisión por qué las cotas incondicionales no contradicen el defecto.

**CONDICIONAL.** Todo lo que usa Hipótesis D (finitud de las órbitas fuera de línea) sólo vale bajo ella; no puede concluir RH sin excluir también infinitud.

**CONJETURAL / INCOMPLETO.** EX/W4-RSRP y la rigidez espectral caos–defecto son candidatos, no teoremas. La barrera final exige F1, F2 o F3; F1 es esencialmente RH y F2/F3 están abiertos. La herencia a 024 es buscar una cota inferior para la distancia `b_j`.

### 024 — Cotas para `b_j`, perfil local y caos riguroso

**Objetivo.** Excluir defectos minúsculos mediante una cota inferior incondicional de la distancia a la línea.

**PROBADO / negativo.** La auditoría muestra que los métodos disponibles no producen tal cota para un cero individual. El perfil local inducido por una órbita se deriva formalmente; las cotas y modelos conocidos no dominan la interferencia de ceros en línea en el punto requerido.

**CONDICIONAL.** Una cota de tipo polinómico se obtiene sólo bajo control puntual de `log|ζ|`/CLT de Selberg en alturas especiales. La compatibilidad con caos es no-excluyente incondicionalmente.

**Herencia.** 025 audita mecanismos clásicos restantes. El resultado es un no-go metodológico, no prueba de inexistencia de toda cota futura.

### 025 — Auditoría final de mecanismos para `b_j`

**Objetivo.** Examinar mecanismos clásicos, de Bruijn–Newman y Laguerre–Pólya/Kreĭn para forzar una cota no trivial de `b_j`.

**PROBADO / diagnóstico.** La auditoría descarta las familias examinadas como fuente de una cota de ese tipo. La relación de Bruijn–Newman da un vínculo cuantitativo bajo Hipótesis D; el análisis LP/Turán identifica circularidad al dividir por factores asociados a ceros fuera de línea.

**EQUIVALENTE-A-RH.** `Λ=0`, la pertenencia LP de xi y la desigualdad (LB) son reformulaciones de RH, no mecanismos independientes. El veredicto concluye correctamente que ningún mecanismo auditado fuerza el lower bound solicitado sin reintroducir RH.

## Dependencias y mapa de herencia

`000 → 003 → 004` fija Weil, truncación y la realización condicional. `004 → 005–011` produce el capstone de signo y pruebas de que localización, calor, correlación, marcos e hiperbolicidad no lo evitan. `012–014 → 019–020` conserva omega como matemática independiente pero cierra su uso inverso para localizar ceros. `015–018` buscan una realización geométrica; el resultado es SURF/CAP, no una realización. `021–025` adopta Hipótesis D para obtener consecuencias y termina en la imposibilidad actual de excluir distancias arbitrariamente pequeñas.

El único cuello de botella que sobrevive a todas las traducciones es uno de estos dos, según la rama: (i) positividad global de Weil/operador/índice de Hodge, **EQUIVALENTE-A-RH**; o (ii) un principio nuevo de rigidez que excluya un defecto finito o infinitesimal, **CONJETURAL** y todavía sin puente incondicional.

## Hallazgos críticos que requieren reauditoría

1. **Convención del objeto central.** Debe resolverse si `Q` es la forma aritmética, una compresión de ella, o el residuo entre lados truncados de la fórmula explícita. La igualdad completa de ambos lados impide tratarlos sin distinción.
2. **Fase 004 y (H).** La presentación final es cuidadosa, pero versiones de “semiboundedness” y “fidelidad” deben auditarse contra la hipótesis de densidad uniforme y los dominios de operadores. Sin (H) no corresponde etiqueta incondicional.
3. **Etiquetas numéricas.** Las leyes de escalamiento, estabilidad de `J`, huecos de Hodge y entrelazamiento explorado no son pruebas uniformes ni sustituyen un límite. Deben conservarse como **NUMÉRICO**.
4. **Equivalencias geométricas.** Las fases 010, 015 y 016 mezclan a veces un diccionario/realización formal con una equivalencia funcional. Cada equivalencia debe separar: identidad algebraica, hipótesis de dominio/completitud, y positividad global.
5. **Hipótesis D.** Las fases 021–025 aportan consecuencias nítidas bajo finitud, pero no justifican que el complemento de RH caiga en ese régimen. Los resultados no excluyen infinitas órbitas fuera de línea.
6. **No-go no es imposibilidad absoluta.** Los cierres de 006, 011, 014, 016–018 y 025 descartan el mecanismo especificado; no demuestran que toda futura teoría en ese lenguaje sea imposible. Esta distinción es esencial para evitar sobreventa.

## Veredicto global

El tramo 000–025 no contiene una prueba de RH. Sí contiene una cartografía amplia y, en varios casos, resultados internos útiles: reducciones explícitas, identidades de defecto, una paridad del índice negativo, diagnósticos de circularidad y no-go de rutas concretas. Las afirmaciones que pretenden cruzar de esas reducciones a positividad uniforme, exclusión de defectos o cotas de distancia son **CONDICIONALES**, **CONJETURALES**, **EQUIVALENTES-A-RH** o **INCOMPLETAS** según se indica arriba.
