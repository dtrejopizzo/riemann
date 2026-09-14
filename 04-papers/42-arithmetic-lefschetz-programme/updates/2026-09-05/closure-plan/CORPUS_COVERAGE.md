# Cobertura del corpus para el plan A–B–C–D

Fecha del inventario: 2026-09-05, antes de crear estos documentos. Estado: **inventario y revisión estratégica; no certificado de validez matemática**.

## Método y límites

- Se enumeraron todos los directorios `phase-*` en `03-research` y los 42 directorios numerados de `04-papers`.
- Se leyeron mecánicamente los 5.359 textos con extensiones `.md`, `.tex`, `.txt` de `01-context`, `02-foundations`, `03-research`, `04-papers` y `05-meta-and-planning` para localizar vocabulario de estados y obstrucciones. Leerlos mediante un script no equivale a revisar sus pruebas.
- Se extrajeron encabezados de documentos de fase y abstracts/encabezados de las fuentes principales de los papers. Los extractos y el índice general orientaron la selección; no se afirma haber leído íntegros los 42 fuentes.
- La lectura detallada de esta campaña de planificación se concentró en P123.006, .010, .011, .014–.018, contrato/plan de fase 123; P122.002, .008, .020, .028, .029, especificación D, índice y auditoría de fuentes A/B/C; cierre de fase 120; índice de fase 121; resultados de fase 119; pasajes pertinentes del paper 42 y documentación de certificados. Se consultaron además los mapas raíz, OPTIONS, índice de papers y dossier histórico de auditorías.
- Los binarios, notebooks no extraídos y salidas masivas no se trataron como pruebas. No se regeneraron certificados numéricos durante la elaboración de este plan.
- Los hashes de fuentes fijan el material inventariado, no validan su contenido. Los recuentos incluyen duplicados históricos dentro de cada fase.

Hay 123 directorios de fases: la numeración llega a 123, faltan las etiquetas 1 y 2 y existen dos directorios con la etiqueta 44. No confundir número máximo con número de directorios.

## Reutilización transversal

| Sector | Uso propuesto | Condición |
|---|---|---|
| RH1–RH9 | Controles empíricos, historia omega y falsadores | Auditar datos concretos sólo si se usan en un argumento. |
| Fases 0–28 | Detectores, signos, truncación e inercia | Verificar hipótesis; no trasladar positividad auxiliar. |
| Fases 29–61 | CCM, correspondencias, Hodge, recurrencia y barreras | No reabrir una clase refutada sin cambiar una hipótesis relevante. |
| Fases 62–76 | Índice, Feshbach y Pick | Reutilizar identidades; no hacer de LP+IDENT una obligación extra de A–D. |
| Fases 77–101 | Anclajes, transporte y defectos | Separar identidad exacta de control del límite o de signo. |
| Fases 102–106 | Li firmado, análisis primo–Gamma y falsadores | Reserva analítica y controles de completación. |
| Fases 107–118 | Desarrollo histórico de los cuatro rows | Leer con las auditorías posteriores; Schur logarítmico retractado. |
| Fase 119 | Separadores aritméticos y pérdida por agrupación de normas | Mantener etiquetas de lugares. |
| Fases 120–122 | Identidades de Green, rigidez, primer contacto y transmisión | Los detectores no prueban su propia anulación. |
| Fase 123 | Portador de correspondencias candidato | Corregir P123.018 antes de completar A. |

## Los 42 papers

Las funciones asignadas son decisiones de planificación basadas en índices y extractos, no juicios definitivos de validez o novedad. Cada uso como lema exige lectura de su prueba y dependencias.

| Paper / fuente | Líneas del fuente | Papel en el plan | SHA-256 (prefijo) |
|---|---:|---|---|
| [01-critical-line-survey](../../04-papers/01-critical-line-survey/main.tex) | 1245 | Mapa bibliográfico histórico; verificar fechas y fuentes antes de reutilizar. | `b94222f7f1c3b81d` |
| [02-omega-class-decomposition](../../04-papers/02-omega-class-decomposition/main.tex) | 1073 | Descomposición omega; recurso lateral, sin puente automático a D. | `bdf6445d69f012f2` |
| [03-sign-interclass-interference](../../04-papers/03-sign-interclass-interference/main.tex) | 351 | Corrección de signos en interferencia; disciplina de controles. | `5531de3b7822f524` |
| [04-davenport-heilbronn-null](../../04-papers/04-davenport-heilbronn-null/main.tex) | 1198 | Control Davenport–Heilbronn y límites de observación finita. | `0af3a3ad82321c33` |
| [05-omega-hierarchy-chaos](../../04-papers/05-omega-hierarchy-chaos/main.tex) | 491 | Diccionario de caos/omega; recurso independiente, no premisa de cierre. | `f20a9c6938f60a84` |
| [06-why-rh-resists](../../04-papers/06-why-rh-resists/main.tex) | 335 | Clasificador de mecanismos; usar como heurística, no veto universal. | `b9662b45ae5ec64b` |
| [07-localized-weil-detector](../../04-papers/07-localized-weil-detector/main.tex) | 522 | Detector localizado y truncación; auditar antes de reutilizar en C/D. | `f9ac5ced085f1a47` |
| [08-weil-krein-realization](../../04-papers/08-weil-krein-realization/main.tex) | 628 | Realización de Krein; comprobar hipótesis de semiboundedness y dominios. | `3bef955560eee14e` |
| [09-stable-arithmetic-fingerprints](../../04-papers/09-stable-arithmetic-fingerprints/main.tex) | 226 | Estabilidad de datos locales; útil para errores y controles. | `6d194087696b6924` |
| [10-anatomy-local-invariant](../../04-papers/10-anatomy-local-invariant/main.tex) | 500 | Información aritmética recuperable; posible control de fidelidad en B/C. | `379f2d4d9502c7d1` |
| [11-pontryagin-index-finite-defect](../../04-papers/11-pontryagin-index-finite-defect/main.tex) | 205 | Defecto finito; archivo de límites de esta estrategia. | `da93c84eda388333` |
| [12-band-limited-weil-carleson](../../04-papers/12-band-limited-weil-carleson/main.tex) | 318 | Puente finito–global y saturación; control de cuantificadores en D. | `d74d4064491811c5` |
| [13-heat-flow-lyapunov](../../04-papers/13-heat-flow-lyapunov/main.tex) | 247 | Flujo de calor; no importar monotonicidad como signo inicial. | `5c0da9f55c2039d4` |
| [14-modern-routes-wrong-sign](../../04-papers/14-modern-routes-wrong-sign/main.tex) | 252 | Reformulaciones Hodge/hiperbolicidad; revisar alcance exacto. | `26c117fef0b0eacb` |
| [15-finite-to-full-uniformity](../../04-papers/15-finite-to-full-uniformity/main.tex) | 383 | Uniformidad de torres; herramientas candidatas para límites, bajo hipótesis. | `5898b0f6da7b0ad4` |
| [16-unconditional-finite-bottom](../../04-papers/16-unconditional-finite-bottom/main.tex) | 369 | Cotas parciales incondicionales; no sustituyen el signo de D. | `54adc4cfea9416b4` |
| [17-lefschetz-dichotomy](../../04-papers/17-lefschetz-dichotomy/main.tex) | 482 | Obstrucción Lefschetz en clase declarada; comprobar antes del control clásico. | `de5bb79557f29e55` |
| [18-localized-weil-krein-index](../../04-papers/18-localized-weil-krein-index/main.tex) | 794 | Índice de Krein y detectores; recurso para diagnóstico de D. | `e5c7e11fb42314b0` |
| [19-arithmetic-defect-offline-zeros](../../04-papers/19-arithmetic-defect-offline-zeros/main.tex) | 515 | Inercia y defecto fuera de línea; conservar normalización de cuádruplos. | `f0fcd9cc8f949fe2` |
| [20-herglotz-criterion](../../04-papers/20-herglotz-criterion/main.tex) | 267 | Criterio Herglotz; blanco alternativo, no teorema de positividad. | `1e8864ee41f45273` |
| [21-omega-information-barrier](../../04-papers/21-omega-information-barrier/main.tex) | 530 | Barrera de información omega; no confundir estadística y signo. | `096243c5fb3d6b73` |
| [22-moment-rigidity-criterion](../../04-papers/22-moment-rigidity-criterion/main.tex) | 753 | Rigidez de momentos; criterio alternativo sujeto a hipótesis. | `57fb968fc6e801ae` |
| [23-ccm-jacobi-incidence-equivalence](../../04-papers/23-ccm-jacobi-incidence-equivalence/main.tex) | 471 | Incidencia/Jacobi; recurso de realización, requiere identificación correcta. | `95e65e08cffbb03d` |
| [24-trace-measure-criterion](../../04-papers/24-trace-measure-criterion/main.tex) | 359 | Medida/traza; revisar qué afirmaciones son criterios y cuáles pruebas. | `981064569bfcc267` |
| [25-bridge-theorem](../../04-papers/25-bridge-theorem/main.tex) | 558 | Puente entre índices; importar sólo después de revalidar dominios. | `1bd61b908ef83350` |
| [26-weil-toeplitz-logistic-criterion](../../04-papers/26-weil-toeplitz-logistic-criterion/main.tex) | 1715 | Geometría Weil–Toeplitz; revisar sentidos de las equivalencias. | `5c77f78b97a1dcef` |
| [27-exhaustion-1d-propagation](../../04-papers/27-exhaustion-1d-propagation/main.tex) | 544 | Propagación unidimensional; no-go con alcance limitado a sus mecanismos. | `241b63d011ae726d` |
| [28-amplification-survivor](../../04-papers/28-amplification-survivor/main.tex) | 541 | Amplificación; archivo de rutas y sus estimaciones pendientes. | `89b18d73b4b4a304` |
| [29-master-quantifier](../../04-papers/29-master-quantifier/main.tex) | 451 | Cuantificadores promedio/uniforme; control permanente del cierre. | `b8585cfb13c8709f` |
| [30-two-lemma-architecture](../../04-papers/30-two-lemma-architecture/main.tex) | 438 | Finitud más rigidez; alternativa, no dependencia obligatoria A–D. | `02085b96bfd65d86` |
| [31-curvature-lp-synthesis](../../04-papers/31-curvature-lp-synthesis/main.tex) | 570 | Curvatura/LP; otras coordenadas del signo. | `ab747ebbca01fee5` |
| [32-stepanov-band](../../04-papers/32-stepanov-band/main.tex) | 527 | Resultado Stepanov; no extender a la versión en una sola recta sin prueba. | `f601e6a54d634fc0` |
| [33-energy-decomposition](../../04-papers/33-energy-decomposition/main.tex) | 1077 | Energía fuera de línea; alternativa parcial, no puente construido a A. | `c3ba9e2189751b73` |
| [34-architecture-of-obstruction](../../04-papers/34-architecture-of-obstruction/main.tex) | 1476 | Mapa histórico de obstrucciones; contrastar con correcciones posteriores. | `7ccb775a7ecf59df` |
| [35-colligation-route](../../04-papers/35-colligation-route/main.tex) | 527 | Coligación y Doob; distinguir curvatura local y constante global. | `886bc32b19b3dab7` |
| [36-obstruction-ledger](../../04-papers/36-obstruction-ledger/main.tex) | 11996 | Li–Keiper/Pick; reserva de prueba firmada y registro de obstrucciones. | `5bd49289e2ec42ac` |
| [37-death-of-the-positivity-family](../../04-papers/37-death-of-the-positivity-family/main.tex) | 3812 | Falsadores de transferencias positivas; conservar corrección del cutoff. | `a6ae79080e4a8854` |
| [38-li-fir-stability](../../04-papers/38-li-fir-stability/main.tex) | 1131 | Filtros FIR y Li; blanco alternativo, no resolverlo además de D obligatoriamente. | `f3934f5dcf8a33f8` |
| [39-cofinal-weil-summability](../../04-papers/39-cofinal-weil-summability/main.tex) | 3156 | Sumabilidad y defectos de transporte; posible infraestructura C/D. | `f7263cafdce1310e` |
| [40-connes-proof-skeleton](../../04-papers/40-connes-proof-skeleton/main.tex) | 3674 | Fuentes primo–Gamma e inercia; reutilizar identidades verificadas. | `bddf2b4e6861eed4` |
| [41-obstruction-catalogue](../../04-papers/41-obstruction-catalogue/main.tex) | 1490 | Catálogo de 31 mecanismos; clasificar no-go, falsador y contramodelo. | `cf15e600e3affc9d` |
| [42-arithmetic-lefschetz-programme](../../04-papers/42-arithmetic-lefschetz-programme/main.tex) | 7270 | Programa A/B/C/D principal; contrato restringido sujeto a P122 y P123.018. | `c12c1584e68245f1` |

## Inventario completo de fases

Cada fila acredita presencia y recuento. El enlace lleva al directorio; la clasificación estratégica por intervalos está arriba. No se promueve la etiqueta histórica `closure` a teorema revisado.

| Fase | Archivos de texto | Archivos totales |
|---|---:|---:|
| [phase-0-foundations](../../03-research/phase-0-foundations/) | 5 | 5 |
| [phase-3-uniform-inequality](../../03-research/phase-3-uniform-inequality/) | 2 | 2 |
| [phase-4-handoff](../../03-research/phase-4-handoff/) | 30 | 32 |
| [phase-5-structural](../../03-research/phase-5-structural/) | 10 | 16 |
| [phase-6](../../03-research/phase-6/) | 4 | 4 |
| [phase-7](../../03-research/phase-7/) | 3 | 7 |
| [phase-8](../../03-research/phase-8/) | 5 | 9 |
| [phase-9](../../03-research/phase-9/) | 4 | 7 |
| [phase-10](../../03-research/phase-10/) | 7 | 13 |
| [phase-11](../../03-research/phase-11/) | 4 | 8 |
| [phase-12](../../03-research/phase-12/) | 6 | 13 |
| [phase-13](../../03-research/phase-13/) | 1 | 4 |
| [phase-14](../../03-research/phase-14/) | 9 | 17 |
| [phase-15](../../03-research/phase-15/) | 17 | 33 |
| [phase-16](../../03-research/phase-16/) | 10 | 26 |
| [phase-17](../../03-research/phase-17/) | 5 | 9 |
| [phase-18](../../03-research/phase-18/) | 2 | 4 |
| [phase-19](../../03-research/phase-19/) | 6 | 11 |
| [phase-20](../../03-research/phase-20/) | 4 | 5 |
| [phase-21](../../03-research/phase-21/) | 3 | 3 |
| [phase-22](../../03-research/phase-22/) | 4 | 4 |
| [phase-23](../../03-research/phase-23/) | 4 | 4 |
| [phase-24](../../03-research/phase-24/) | 4 | 4 |
| [phase-25](../../03-research/phase-25/) | 5 | 5 |
| [phase-26](../../03-research/phase-26/) | 2 | 2 |
| [phase-27](../../03-research/phase-27/) | 4 | 4 |
| [phase-28](../../03-research/phase-28/) | 9 | 9 |
| [phase-29](../../03-research/phase-29/) | 55 | 55 |
| [phase-30](../../03-research/phase-30/) | 3 | 3 |
| [phase-31](../../03-research/phase-31/) | 1 | 1 |
| [phase-32-ccm](../../03-research/phase-32-ccm/) | 11 | 11 |
| [phase-33-dbn](../../03-research/phase-33-dbn/) | 20 | 20 |
| [phase-34-new-directions](../../03-research/phase-34-new-directions/) | 8 | 8 |
| [phase-35-five-fronts](../../03-research/phase-35-five-fronts/) | 6 | 6 |
| [phase-36-ABC-forms](../../03-research/phase-36-ABC-forms/) | 5 | 5 |
| [phase-37-physics](../../03-research/phase-37-physics/) | 5 | 5 |
| [phase-38-final-audit](../../03-research/phase-38-final-audit/) | 5 | 5 |
| [phase-39-G1G2-interface](../../03-research/phase-39-G1G2-interface/) | 3 | 3 |
| [phase-40-close-G1](../../03-research/phase-40-close-G1/) | 3 | 3 |
| [phase-41-build-G2](../../03-research/phase-41-build-G2/) | 2 | 2 |
| [phase-42-hodge-dynamics](../../03-research/phase-42-hodge-dynamics/) | 2 | 2 |
| [phase-43-hodge-foliated-specZ](../../03-research/phase-43-hodge-foliated-specZ/) | 2 | 2 |
| [phase-44-creative-breakthrough](../../03-research/phase-44-creative-breakthrough/) | 1 | 1 |
| [phase-44-new-mathematics](../../03-research/phase-44-new-mathematics/) | 3 | 3 |
| [phase-45-fredholm](../../03-research/phase-45-fredholm/) | 3 | 3 |
| [phase-46-audit-and-attacks](../../03-research/phase-46-audit-and-attacks/) | 7 | 7 |
| [phase-47-live-fronts](../../03-research/phase-47-live-fronts/) | 5 | 5 |
| [phase-48-audit-and-purity](../../03-research/phase-48-audit-and-purity/) | 5 | 5 |
| [phase-49-cross-the-wall](../../03-research/phase-49-cross-the-wall/) | 4 | 4 |
| [phase-50-diophantine-thread](../../03-research/phase-50-diophantine-thread/) | 2 | 2 |
| [phase-51-functor-construction](../../03-research/phase-51-functor-construction/) | 2 | 2 |
| [phase-52-homotopy-inertia](../../03-research/phase-52-homotopy-inertia/) | 2 | 2 |
| [phase-53-quantum-import](../../03-research/phase-53-quantum-import/) | 2 | 2 |
| [phase-54-index-dynamics](../../03-research/phase-54-index-dynamics/) | 7 | 7 |
| [phase-55-two-arrows](../../03-research/phase-55-two-arrows/) | 5 | 5 |
| [phase-56-two-towers](../../03-research/phase-56-two-towers/) | 4 | 4 |
| [phase-57-brick-A](../../03-research/phase-57-brick-A/) | 1 | 1 |
| [phase-58-full-audit](../../03-research/phase-58-full-audit/) | 9 | 9 |
| [phase-59-full-closure](../../03-research/phase-59-full-closure/) | 7 | 7 |
| [phase-60-discriminant](../../03-research/phase-60-discriminant/) | 63 | 99 |
| [phase-61-open-problems](../../03-research/phase-61-open-problems/) | 10 | 132 |
| [phase-62-cesaro-closure](../../03-research/phase-62-cesaro-closure/) | 6 | 14 |
| [phase-63-lefschetz-realization](../../03-research/phase-63-lefschetz-realization/) | 6 | 9 |
| [phase-64-connes-route](../../03-research/phase-64-connes-route/) | 33 | 46 |
| [phase-65-signature-continuity](../../03-research/phase-65-signature-continuity/) | 31 | 31 |
| [phase-66-rank-one-escape](../../03-research/phase-66-rank-one-escape/) | 9 | 13 |
| [phase-67-quantum-q-index](../../03-research/phase-67-quantum-q-index/) | 23 | 39 |
| [phase-68-glt-symbol](../../03-research/phase-68-glt-symbol/) | 6 | 12 |
| [phase-69-exact-signed-index](../../03-research/phase-69-exact-signed-index/) | 3 | 6 |
| [phase-70-lee-yang-dbn](../../03-research/phase-70-lee-yang-dbn/) | 14 | 18 |
| [phase-71-cand1-convergence](../../03-research/phase-71-cand1-convergence/) | 26 | 40 |
| [phase-72-feshbach-leakage-calculus](../../03-research/phase-72-feshbach-leakage-calculus/) | 437 | 782 |
| [phase-73-cauchy-projection](../../03-research/phase-73-cauchy-projection/) | 463 | 787 |
| [phase-74-hilbert-eigenline-cancellation](../../03-research/phase-74-hilbert-eigenline-cancellation/) | 37 | 68 |
| [phase-75-arithmetic-numerator-divisibility](../../03-research/phase-75-arithmetic-numerator-divisibility/) | 12 | 15 |
| [phase-76-normalized-adjugate-arithmetic-lock](../../03-research/phase-76-normalized-adjugate-arithmetic-lock/) | 61 | 166 |
| [phase-77-weyl-limit-point](../../03-research/phase-77-weyl-limit-point/) | 113 | 382 |
| [phase-78-build-neutral-lp-and-ident](../../03-research/phase-78-build-neutral-lp-and-ident/) | 159 | 405 |
| [phase-79-shared-convergence-and-ident-discriminant](../../03-research/phase-79-shared-convergence-and-ident-discriminant/) | 107 | 270 |
| [phase-80-relative-determinant-identification](../../03-research/phase-80-relative-determinant-identification/) | 11 | 11 |
| [phase-81-secular-arithmetic-anchor](../../03-research/phase-81-secular-arithmetic-anchor/) | 6 | 6 |
| [phase-82-coupled-generator-continuum](../../03-research/phase-82-coupled-generator-continuum/) | 7 | 7 |
| [phase-83-gamma-euler-coboundary](../../03-research/phase-83-gamma-euler-coboundary/) | 10 | 10 |
| [phase-84-distributional-endpoint-module](../../03-research/phase-84-distributional-endpoint-module/) | 7 | 7 |
| [phase-85-parity-weyl-defect](../../03-research/phase-85-parity-weyl-defect/) | 7 | 7 |
| [phase-86-signed-spectral-abel](../../03-research/phase-86-signed-spectral-abel/) | 6 | 6 |
| [phase-87-euler-deformation-discriminant](../../03-research/phase-87-euler-deformation-discriminant/) | 7 | 7 |
| [phase-88-endpoint-layer-pencil](../../03-research/phase-88-endpoint-layer-pencil/) | 6 | 6 |
| [phase-89-projective-layer-rotation](../../03-research/phase-89-projective-layer-rotation/) | 7 | 7 |
| [phase-90-projective-kato-euler-current](../../03-research/phase-90-projective-kato-euler-current/) | 7 | 7 |
| [phase-91-kato-coboundary-equivalence](../../03-research/phase-91-kato-coboundary-equivalence/) | 6 | 6 |
| [phase-92-cluster-adjugate-projectivization](../../03-research/phase-92-cluster-adjugate-projectivization/) | 9 | 9 |
| [phase-93-direct-bordered-anchor](../../03-research/phase-93-direct-bordered-anchor/) | 7 | 7 |
| [phase-94-global-cofactor-cell-current](../../03-research/phase-94-global-cofactor-cell-current/) | 8 | 8 |
| [phase-95-characteristic-jacobian-current](../../03-research/phase-95-characteristic-jacobian-current/) | 7 | 7 |
| [phase-96-determinantal-prime-response](../../03-research/phase-96-determinantal-prime-response/) | 7 | 7 |
| [phase-97-euler-sensitivity-commutator](../../03-research/phase-97-euler-sensitivity-commutator/) | 8 | 8 |
| [phase-98-sensitivity-shell-split](../../03-research/phase-98-sensitivity-shell-split/) | 7 | 7 |
| [phase-99-adjugate-boundary-sandwich](../../03-research/phase-99-adjugate-boundary-sandwich/) | 8 | 8 |
| [phase-100-characteristic-cofactor-factorization](../../03-research/phase-100-characteristic-cofactor-factorization/) | 7 | 7 |
| [phase-101-covariant-bordered-current](../../03-research/phase-101-covariant-bordered-current/) | 98 | 101 |
| [phase-102-omega7-closure-campaign](../../03-research/phase-102-omega7-closure-campaign/) | 266 | 269 |
| [phase-103-direct-a1-closure](../../03-research/phase-103-direct-a1-closure/) | 72 | 96 |
| [phase-104-unconditional-a1-closure](../../03-research/phase-104-unconditional-a1-closure/) | 116 | 307 |
| [phase-105-a1-geometry-and-deep-limit](../../03-research/phase-105-a1-geometry-and-deep-limit/) | 7 | 20 |
| [phase-106-global-modular-star-audit](../../03-research/phase-106-global-modular-star-audit/) | 212 | 277 |
| [phase-107-arithmetic-lefschetz-reconstruction](../../03-research/phase-107-arithmetic-lefschetz-reconstruction/) | 248 | 542 |
| [phase-108-row-a-construction](../../03-research/phase-108-row-a-construction/) | 53 | 104 |
| [phase-109-one-sided-pairing](../../03-research/phase-109-one-sided-pairing/) | 6 | 10 |
| [phase-110-principal-xi-divisibility](../../03-research/phase-110-principal-xi-divisibility/) | 5 | 9 |
| [phase-111-schwartz-admissibility](../../03-research/phase-111-schwartz-admissibility/) | 5 | 8 |
| [phase-112-effective-cone](../../03-research/phase-112-effective-cone/) | 5 | 8 |
| [phase-113-the-trace-on-schwartz-data](../../03-research/phase-113-the-trace-on-schwartz-data/) | 17 | 33 |
| [phase-114-closing-the-four-rows](../../03-research/phase-114-closing-the-four-rows/) | 465 | 1108 |
| [phase-115-the-mixed-class-and-the-green-extension](../../03-research/phase-115-the-mixed-class-and-the-green-extension/) | 18 | 33 |
| [phase-116-the-logarithmic-schur-angle-conjecture](../../03-research/phase-116-the-logarithmic-schur-angle-conjecture/) | 468 | 903 |
| [phase-117-the-transfer-comparison-measured](../../03-research/phase-117-the-transfer-comparison-measured/) | 1 | 10 |
| [phase-118-the-exact-threshold-inequality](../../03-research/phase-118-the-exact-threshold-inequality/) | 7 | 219 |
| [phase-119-what-a-finite-compression-certifies](../../03-research/phase-119-what-a-finite-compression-certifies/) | 3 | 7 |
| [phase-120-global-polarization](../../03-research/phase-120-global-polarization/) | 42 | 56 |
| [phase-121-negative-witness-rigidity](../../03-research/phase-121-negative-witness-rigidity/) | 54 | 54 |
| [phase-122-row-d-integrity-and-construction](../../03-research/phase-122-row-d-integrity-and-construction/) | 35 | 37 |
| [phase-123-weil-strength-abc](../../03-research/phase-123-weil-strength-abc/) | 21 | 33 |

## Discrepancias materiales detectadas

1. Los índices raíz todavía describen principalmente el estado hasta fase 119; el presente inventario llega a 123.
2. El dossier RH-MASTER-CONTEXT conserva un inventario histórico hasta fase 101. Se usa como auditoría de ese corte, no como censo actual.
3. El traspaso proponía realizar el modelo finito de dos primos, pero P122.028 ya contiene su cálculo y resultado negativo para la inferencia harmonicidad → flujo cero.
4. `OPTIONS.md` desaconseja trabajar en Weil por ser equivalente a RH; el reinicio histórico corrige expresamente ese veto. Se adopta la corrección lógica.
5. P123.018 invalida dos mapas explícitos y reabre otras obligaciones: prevalece sobre las etiquetas anteriores de aceptación global.
6. El control clásico P123.011 requiere revisión del puente de categorías y de la relación entre cuadrados y ciclos efectivos; no se certifica nuevamente aquí.

## Fuentes externas contrastadas para orientar el plan

- [Connes–Consani, Knots, primes and class field theory](https://arxiv.org/html/2501.06560v1), §5: haz algebraico y mapas de coeficientes. Se contrastaron los enunciados relevantes; no se auditó toda la demostración.
- [Deninger, Rational Witt vectors and associated sheaves](https://arxiv.org/html/2508.05329v1), Teorema 5.1 y Proposición 5.2: punto de entrada a ciclos finitos, con sus hipótesis. No es un puente ya construido hacia Corr_A.
- [Meyer, A spectral interpretation for the zeros of the Riemann zeta function](https://arxiv.org/abs/math/0412277v3): título y versión corregidos. La atribución más amplia del documento de traspaso no es el título de este identificador.
- [Connes–Consani, On the Jacobian of Spec Z compactificado](https://arxiv.org/abs/2602.15941): ficha y abstract contrastados; recurso geométrico, sin importar un Hodge mixto.
- [Grubb, teoría de mu-transmisión](https://arxiv.org/abs/1310.0951): referencia contrastada; su aplicabilidad a los saltos concretos se rige por P122.029.

## Qué queda por auditar al ejecutar

El cierre de dependencias de cada lema elegido, los teoremas externos completos y su mapa de hipótesis, los funtores no construidos, las estimaciones globales y los certificados realmente utilizados. No hace falta volver a demostrar resultados que se importen correctamente, pero sí comprobar que dicen lo que la prueba necesita.
