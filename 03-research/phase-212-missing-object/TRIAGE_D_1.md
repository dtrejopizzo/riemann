# Triage D-1: ideas de la fila D registradas y nunca llevadas a término (lista 1, ítems 1–41)

Filtro: F1 (Lema T, con los controles c = 2, borrado de una potencia prima y peso tipo Beurling), F2 (arquimediano y peso del mismo objeto en el mismo paso), F3 (formatos afines en el peso; Gram/Schur; piezas por primo; cambio de operador de referencia), F4 (margen doblemente exponencial: ninguna cota con holgura), F5 (REF sin lado independiente). «MI l.N» = línea de `05-meta-and-planning/ROUTES-MASTER-INDEX.md`. Donde una fuente nombra el enunciado clásico se escribe [H]. Las rutas de las fuentes se dan relativas a `03-research/` o `01-context/`. Es una clasificación: no se construye ni se calcula nada.

Para cada ítem se abrió el pasaje de la fuente primaria. La lista exacta está en §4. El índice se usó sólo para buscar cierres posteriores.

## §1 Tabla

| nº | idea | fuente (pasaje leído) | clase | razón |
|---|---|---|---|---|
| 1 | (♦): ‖G^{1/2}(W^prime_λ − p_λ)^− G^{1/2}‖ ≤ 1; comparación «Σ traza prima − masa del polo < 1» | phase-64/POLE-DEFECT-estimate.md l.18–211 | REF | l.98: «(♦) is ε₀≥0 = [H]». La versión de traza de §6 la retira el propio memo por «too strong and the wrong tool» (l.158–163): pierde exactamente el caso marginal. La forma aguda (♦′)/(♦″) (l.179–203) es otra vez ⟺ meta. Dependencia en el peso: p_λ ≥ 0 es la barrera del polo, de masa fija π_res, e independiente del peso; W^prime_λ es lineal en Λ (l.25, 42). El arquimediano no entra en (♦) (l.94), y en §6 se evalúa aparte con PNT (l.141). Por lo tanto no satisface F2: el arquimediano y el peso no salen del mismo paso. La comparación de traza es afín en el peso (F3). La «next computation» (signo puntual de W^prime − p_λ, l.210) decide sólo si el núcleo BS es positivo-mejorante, no el signo de la forma. |
| 2 | Discrepancia de {log n} con pesos Λ(n)/√n | phase-64/FACE-C-spectral-shift-monotonicity.md l.115–130 | CERRADA (class result, ARGUED) | Es una cota «a priori» de equidistribución, es decir de tamaño (F4). La clase «cotas que usan sólo \|Λ(n)\| (large sieve, mean-value)» está cerrada por el METHOD OBSTRUCTION THEOREM con control DH (phase-60/0-triangulation-of-the-wall-from-three.md l.16, RIGOROUS en el memo). Además, el puente arg D_P = πξ_K está invalidado por la errata de la fase 106. |
| 3 | Entrelazado decidido por el signo del polo + HB finito | phase-64/FACE-C-rigidity-attack.md l.129–170 | CIEGA | La propuesta decide el entrelazado «by the sign of the pole alone» (l.141–142), y cada truncación finita es HB. El signo del polo y la propiedad HB finita son idénticos con c = 2, con el borrado de una potencia prima y con el peso Beurling, así que la relación usada vale en los tres controles (F1). Antes de ese paso hay que tomar el límite de la renormalización, que es REF (Thm hbstab). |
| 4 | Isometría de la J-reflexión del núcleo canónico primitivo | phase-64/FACE-C-simple-crossings-audit.md l.180–201 | REF | El memo dice textualmente «[H] = the s↔1−s reflection acts isometrically on the primitive canonical kernel» (l.187–188) y la llama «new, clean equivalent». |
| 5 | (CONF) Landau–Widom: compresión de Wiener–Hopf → caja de Dirichlet | phase-60/cierre-1-CONF-landau-widom.md l.12–28 | OTRO OBJETO | Es la convergencia del espectro bajo renormalizado a (k+1)², «RH-neutral … closable by established machinery». No contiene el signo: el memo separa «existencia del límite = neutral» del signo de ε₀. |
| 6 | Cota de la cola de Fourier del símbolo completo | phase-60/weil-remainder-attack.tex l.227–272 | CIEGA | Prop noncirc la plantea como cota de una cola suave, es decir una estimación de tamaño (F4). No nombra ninguna operación de signo. |
| 7 | Funcional de δV insensible a ceros individuales | phase-60/attack-deltaV-analysis.md l.35–45 | CERRADA (ARGUED) | Un funcional insensible a ceros individuales sólo usa densidad. Cae en la clase cerrada por el METHOD OBSTRUCTION THEOREM (0-triangulation l.16). El memo lo juzga improbable. |
| 8 | ε₀(λ) ≥ c/λ² sólo con datos primos (densidad, PNT) | phase-60/spectral-gap-analysis.tex l.150–183 | CERRADA (ARGUED) | La pregunta es «¿basta la densidad?», y el METHOD OBSTRUCTION THEOREM responde para esa clase: el control DH tiene magnitudes comparables y ε₀ < 0. |
| 9 | Diseño de ventana: resolución(φ) ≫ 1/log λ | phase-60/0-triangulation-of-the-wall-from-three.md l.23–35 | CERRADA | «Computation in progress … recorded to continue» sin resultado. Cerrada después por «structural marginality» (REDUCCION §9.2; MI l.27202). El mismo memo prueba la obstrucción de método. |
| 10 | Hardy aguda c = 2 / positividad de la forma finita desde PNT | phase-60/A_intento_demostracion.md l.13–27 | CERRADA (ARGUED) | «c = 2 = [H]» (l.23) es REF. El [GAP] del paso 4 es «positividad de la forma finita desde PNT, sin posición de ceros» (l.24), que es la clase de densidad cerrada por la obstrucción de método. |
| 11 | Hessiano arch↔arith; dirección curvada = reescalado global | phase-60/CONSOLIDACION_L_y_eslabones.md §4 l.38–58 | LOCAL/NUMÉRICA, no decide nada | Resultado [N] en mpmath: la única dirección curvada es Λ → Λ(1+δ), justamente la dirección del control c. Es información de segundo orden en torno al peso real. No da signo para todo T (F4), y el arquimediano queda como esqueleto fijo (F2). |
| 12 | Identificación de V(x) / tasa h(λ) | phase-60/IV1-operator-identification.md l.26–89 | CERRADA | Las identificaciones de Â_∞ fueron REFUTED y Airy/Bessel FALSIFIED (MI l.11534). El resto («IV.1 y IV.1★ cierran juntos módulo un residual») es la convergencia del caso 5. |
| 13 | Persistencia de la positividad PF bajo renormalización | phase-60/rh-proof.tex l.35–81 | REF | «[H] reduced to a single positivity-under-renormalization lemma» (l.35–45): el lema es la meta. Cae bajo el NO-GO de topología T1–T2 (MI l.27655). |
| 14 | Lema 2.3.F (Doob–Feshbach–Mosco) | phase-61/R9_three_new_fronts_RESULTS.md l.81–95 | REF | «Status of 2.3.F unchanged … remains REDUCED to» 2.3.F-Loc, confirmado como invariante espectral de escala e^{−cL}. «PSC con fuente uniforme = Lemma 2.3.F/L1 wall» (MI l.26192). (respuesta4.md no contiene la cadena «2.3.F».) |
| 15 | (★) CD(0,∞) por primo + tensorización | phase-64/CONSTRUCTION-spectral-surface.md l.104–180 | CIEGA | Pide curvatura con signo por primo (l.174–177). CD(0,∞) es invariante por escala del núcleo, así que (★) vale igual con c = 2 y con el borrado de una potencia prima (F1/F3). El memo nota además que Γ₂ es marginal (l.157). |
| 16 | R > 0 para toda configuración | phase-64/E107_RESULTS.md l.19–48 | OTRO OBJETO | Margen de la colligación con conjuntos de puntos plantados. «R is configuration-dependent»; probarlo para todas las configuraciones «is [H]». No es a_T en P_T. |
| 17 | Renormalización de rango uno continua en resolvente fuerte | phase-65/D8.5b-i-SELF-ADJOINT-COMPLETION.md l.21, 141–159 | REF | Dentro de la franja, la convergencia «is exactly what is in question» (l.74). Es el NO-GO T1–T2: el índice debe salir del signo y no de la topología. |
| 18 | M3: divergencia positiva de rango uno ⇒ sin cuadrado negativo | phase-65/M2-pole-relative-completion.md l.9–102 | CIEGA | El dato que M3 debe explotar es el «definite-signed rank-one defect» del polo (l.9). Ese signo es el mismo con c = 2, con el borrado y con Beurling (F1), y el memo no nombra ningún paso aritmético que falle en un control. |
| 19 | sup_P ‖P_prim K_P P_prim‖ < ∞ | phase-66/MAXIMAL-CLOSURE-omega7.md l.97–156 | REF | La cota da el índice de Kreĭn–Langer cero, es decir la meta (l.138). Es la cota superior de Thm onefence. |
| 20 | Estado del semigrupo que produzca log b − log a | phase-67/E67_8_RESULTS.md l.28–66 | OTRO OBJETO | Coherencia del modelo QSC fuera de la diagonal, no a_T. Un estado es además lineal (F3). |
| 21 | Torsión fuera de la diagonal; tilting | phase-67/E67_13_RESULTS.md l.43–44 | CERRADA | Auditoría E67.13: «contamination AND fabrication … structural» (MI l.26319). |
| 22 | RCOER C_actual ≥ θ_H C_model; MCOER2 | phase-72/E72_134 l.17–70; E72_148 l.81; E72_267 l.91–95 | CIEGA | Es una comparación con holgura θ_H respecto de un modelo (F4). Cambiar el operador de referencia no cambia el signo (F3). MCOER2 es «purely archimedean … no primes» (F2). |
| 23 | Atacar R_x(s) directamente | phase-72/E72_15_ACD_RESONANCE_BARRIER.md l.34–50 | REF | Thm 72.15: ACD ⟺ aniquilación de las resonancias fuera de la recta. R_x(s) es la respuesta del núcleo acumulado, del lado de los ceros. |
| 24 | Identidad de vector nulo en bloques de resonancia maximal | phase-72/E72_17_MAXIMAL_RESONANCE_BLOCK.md l.148 | REF | Se pide anular los bloques «off-line resonance Gram»: es la meta del lado de los ceros. Las simetrías ya están descartadas en el mismo memo. |
| 25 | HOC3 uniforme (LOW1, LOW2, TAIL) | phase-72/E72_242_HYBRID_HOC3_CERTIFICATE.md l.5–27 | LOCAL/NUMÉRICA, no decide nada | Certificados de la cola del modelo Feshbach de la fase 72 (λ = 32 delicado). No es a_T en P_T, y la versión uniforme es una cota con holgura (F4). |
| 26 | Pila GAP/DCB; DCB en la fuente | phase-72/E72_296_DIRECTIONAL_COMMUTATOR_REPLACEMENT.md l.29–141 | REF | DCB se parte en DCB-model + DCB-arith. Cada paso es una reformulación exacta y el residuo es la anulación de paquetes fuera de línea (MI l.26063). |
| 27 | ELR2/ELR3, XNEG, HOC3 polo-par | phase-72/E72_270 l.1–21; E72_211 | CIEGA | Son envolventes de energía y signos medidos («Negative supports XNEG»), es decir cotas de tamaño (F4). |
| 28 | DSF-O2 | phase-72/E72_288_DSF_STRENGTH_AUDIT.md l.60 | REF | «should be treated as an [H]-strength arithmetic theorem». |
| 29 | GAP-151.A/B/C | phase-48/151-adversarial-audit-of-docs-145-and-148.md l.61–173 | OTRO OBJETO | Huecos de marco de la forma semilocal de dos primos puros y completitud de pruebas de los documentos 145/148. No es la forma completa a_T. |
| 30 | Cota superior ⟨Γ,H⟩² > ⟨H,H⟩⟨Γ,Γ⟩ fuera de efectividad/Bochner/relajación/Satake | phase-15/M3-genuine-attempts-on-the-core.md l.45–58 | REF | «The upper bound (the Hodge index) is genuinely a different, one-sided statement»: es el índice de Hodge, es decir la meta. La reapertura sólo excluye fuentes. |
| 31 | Siete lemas del Bottleneck Ledger | RH8/task1/bottleneck_ledger*.md; RH8/task11/bottleneck_ledger_v3.md | OTRO OBJETO | Regularidades numéricas de Q_σ y lemas del lado de los ceros. No es a_T. |
| 32 | Forma de Weil localizada en ordenadas fuera de la recta | RH5/task37/weil_positivity_results.txt l.7; OVERVIEW.md l.16 | OTRO OBJETO | «MISSING LEMMA» de detección de violaciones mediante funciones de prueba. No es un mecanismo de signo. |
| 33 | Perturbación por desplazamiento, \|λ\| ∝ β² | RH6/task10/OVERVIEW.md l.17–20 | OTRO OBJETO | Sensibilidad a ceros desplazados (calibración). |
| 34 | Hardy-prime cancellation | phase-70/E70_6_PARTIAL_SUMMATION_BARRIER.md l.128–176 | REF | «⟺ Hardy-prime cancellation estimate», declarada de fuerza completa. |
| 35 | (C) coborde de Mellin / (D) corriente de Euler orlada | .phase-102-discard/phase-102-omega7-closure/102_A1_SIGNED_COMPENSATION_CANDIDATES.md l.50–110 | CERRADA (D) / OTRO OBJETO (C) | Ambas apuntan a la desigualdad de Li C_n + ¾λ_n^arch ≥ 0, no a a_T en P_T. (D) figura DEAD en el grid (fila G4B-phase-102/119; ANNEX_INDEX_04 l.283, l.658). (C) es un esquema con resto R_{n,T} ≥ 0 sin especificar y no fue retomado en ningún otro lugar del corpus. |
| 36 | Índice de Pontryagin exactamente dos de la colligación fuente | phase-114/114_d_99_MATRIX_PICONE_TOTAL_POSITIVITY_AUDIT.md l.236–245 | REF | Índice negativo dos, con las dos direcciones agotadas por los residuos de Tate. Por Haynsworth equivale a la positividad restringida, es decir la misma condición (6.3) de D.53. El propio memo exige probarlo «from the source colligation» sin indicar con qué operación. |
| 37 | n₊(A_T) = 1 uniforme | phase-114/114_d_47_TWO_JET_PONTRYAGIN_SCHUR_GATE.md l.160–180 | REF | Las tres estimaciones uniformes (índice, signatura (1,1), ausencia de modo cero) son la puerta de Haynsworth de la meta. Los NO-GO estructurales de D.56 (PROVED) excluyen las fuentes naturales. |
| 38 | Oscilación de dos modos (6.7): n₋(A_{T,P}) ≤ 2 y n₋(𝒢_{T,P}) = n₋(A_{T,P}) | phase-114/114_d_53_THRESHOLD_FLOW_FAILURE_AND_TWO_MODE_OSCILLATION_GATE.md §6 l.166–245 | REF (con falsificador LOCAL en §3) | La igualdad de índices es, por (6.5), la positividad restringida misma. La versión anterior de este triage la daba por CERRADA vía D.135; la lectura de D.135 §6 no lo sostiene, porque D.135 trata el índice positivo del contacto y no n₋(A_T). La mitad «n₋ ≤ 2 para toda partición» sí es falsable a T fijo (§3). |
| 39 | Meta (9.1)/(4.3): ⟨u_o,(H_o − E)^{-1}u_o⟩ < 1 | phase-114/114_d_50_PARITY_BIRMAN_SCHWINGER_AND_DISPLACEMENT_AUDIT.md l.133–150, 263–267; 114_d_51_EXPLICIT_EVEN_LEVEL_AND_ODD_GREEN_GATE.md | REF | «μ_e < μ_o ⟺ m_o(μ_e) < 1»: reduce la meta a orden de canales más nivel par ≥ 0, y ninguna de las dos partes tiene prueba independiente. El contraejemplo de D.50 (PROVED) muestra que el entrelazado de rango uno puede invertir el orden. |
| 40 | λ_max(K_T) ≤ 1 ∀T | phase-114/114_d_135_CENTERED_BIRMAN_SCHWINGER_SPECTRUM.md §6 l.245–260 | REF | D.134 (0.4): ‖W_T R_T^{-1/2}‖ ≤ 1 ⟺ forma ≥ 0. Las reaperturas propuestas («relative screw-kernel factorization or a directed shorted-capacity estimate») no se enuncian, y el memo dice: «No such uniform bound is asserted». |
| 41 | Capacidad de Schur no perturbativa con cancelación conjunta Gamma + contactos | phase-114/114_d_133_THRESHOLD_HADAMARD_CAPACITY_AUDIT.md l.47, 432–445 | REF | La capacidad por celda es «assuming row D» (D.133 Tate–Chebyshev (5.1)/(5.2)). La versión no perturbativa no nombra ninguna operación de signo, y una capacidad es una cota (F4). |

Recuento:
- CERRADA = {2, 7, 8, 9, 10, 12, 21, 35} = 8;
- REF = {1, 4, 13, 14, 17, 19, 23, 24, 26, 28, 30, 34, 36, 37, 38, 39, 40, 41} = 18;
- CIEGA = {3, 6, 15, 18, 22, 27} = 6;
- LOCAL/NUMÉRICA = {11, 25} = 2;
- OTRO OBJETO = {5, 16, 20, 29, 31, 32, 33} = 7;
- VIVA = 0.

Total 41. El ítem 35 se cuenta como CERRADA por su parte (D).

Cambios respecto de la versión anterior (hecha desde las fichas del índice):
- 1 pasa de CIEGA a REF;
- 3 pasa de REF a CIEGA;
- 5 pasa de REF a OTRO OBJETO;
- 8 y 10 pasan de REF a CERRADA;
- 11 pasa de CIEGA a LOCAL;
- 18 pasa de REF a CIEGA;
- 29 pasa de CIEGA a OTRO OBJETO;
- 35 se reparte entre CERRADA (D) y OTRO OBJETO (C);
- 38 pasa de CERRADA a REF.

## §2 Ítems VIVA

Ninguno. Los menos excluidos son:

- Ítem 38: la parte de cota de índice es falsable, pero la igualdad de índices es la meta.
- Ítem 35 (C): esquema sin resto especificado y dirigido a otra desigualdad.

## §3 LOCAL/NUMÉRICA que deciden algo

- **Ítem 38, cota (6.7) n₋(A_{T,P}) ≤ 2.**
  - Qué se calcula: el número de autovalores negativos de la matriz de promedios por celda de K_g (D.52 (2.1)) en el hiperplano de masa cero, para particiones finas de [−T, T].
  - Dónde: en un par de valores de T dentro y por encima de la zona T* ∈ [0.58, 0.60], donde el arquimediano ya tiene direcciones negativas.
  - Costo: diagonalización de matrices de 10²–10³ con aritmética de intervalos.
  - Qué decide: si n₋ > 2 en algún T, la puerta (6.3)/(6.7) queda falsada como formulada, y con ella la ruta 36–38. Si n₋ ≤ 2, no prueba nada uniforme.
  - Antes de lanzarlo hay que cotejar con Thm P (n₋ ≤ 5/7/8, «cuenta 5 en log 2»; MI l.5150, l.12268): si ese conteo es del mismo operador A_T restringido a la masa cero, el falsificador ya existe y el ítem 38 pasa a CERRADA. [Corrección, ROUND_024_C: no es el mismo operador; Thm P cuenta la parte arquimediana sola y (6.7) el núcleo completo con el peine. El ítem queda como reformulación; (6.7) OPEN.]

## §4 Fuentes abiertas y no encontradas

Abiertas (pasaje citado en la tabla):
- **phase-64-connes-route:** POLE-DEFECT-estimate.md, FACE-C-spectral-shift-monotonicity.md, FACE-C-rigidity-attack.md, FACE-C-simple-crossings-audit.md, CONSTRUCTION-spectral-surface.md, E107_RESULTS.md.
- **phase-60-discriminant:** cierre-1-CONF-landau-widom.md, weil-remainder-attack.tex, attack-deltaV-analysis.md, spectral-gap-analysis.tex, 0-triangulation-of-the-wall-from-three.md, A_intento_demostracion.md, CONSOLIDACION_L_y_eslabones.md, IV1-operator-identification.md, rh-proof.tex.
- **phase-61-open-problems:** R9_three_new_fronts_RESULTS.md; respuesta4.md (grep sin la cadena «2.3.F»).
- **phase-65-signature-continuity:** D8.5b-i-SELF-ADJOINT-COMPLETION.md, M2-pole-relative-completion.md.
- **phase-66-rank-one-escape:** MAXIMAL-CLOSURE-omega7.md.
- **phase-67-quantum-q-index:** E67_8_RESULTS.md, E67_13_RESULTS.md.
- **phase-72-feshbach-leakage-calculus:** E72_134, E72_148, E72_267, E72_15, E72_17, E72_242, E72_296, E72_270, E72_288.
- **phase-48-audit-and-purity:** 151-adversarial-audit-of-docs-145-and-148.md.
- **phase-15-arithmetic-hodge-index:** M3-genuine-attempts-on-the-core.md.
- **phase-70-lee-yang-dbn:** E70_6_PARTIAL_SUMMATION_BARRIER.md.
- **.phase-102-discard/phase-102-omega7-closure:** 102_A1_SIGNED_COMPENSATION_CANDIDATES.md (más phase-102-omega7-closure-campaign/102_A1_SIGNED_COMPENSATION_MECHANISMS.md).
- **phase-114-closing-the-four-rows:** 114_d_99, 114_d_47, 114_d_53, 114_d_50, 114_d_135, 114_d_133_THRESHOLD; 114_d_51 sólo por nombre y por su script.
- **01-context:**
  - RH5/task37 (weil_positivity_results.txt, OVERVIEW.md);
  - RH6/task10/OVERVIEW.md;
  - RH8/task1 (listado: bottleneck_ledger.md, bottleneck_ledger_v2.md) y RH8/task11/bottleneck_ledger_v3.md, ambos sólo localizados, no leídos en detalle.

No abiertas o sólo parcialmente:
- Testrella-*.md (ítem 5): se leyó cierre-1-CONF en su lugar.
- 2b_*.md (ítem 12).
- E104_RESULTS.md (ítem 16): sólo E107.
- E67_12_RESULTS.md (ítem 21): sólo E67_13.
- E72_132, E72_286 (ítem 22).
- E72_240 (ítem 25).
- E72_293 §5 (ítem 26): sólo E72_296.
- E72_211–223 salvo 211 y 270–272 (ítem 27).
- RH8/task14 (ítem 31).
- 114_d_52 y 114_d_56 (ítem 37).
- Cuerpo de 114_d_51 (ítem 39).
- Doc 151 original del tramo 02_02 (ítem 29): se usó la auditoría de la fase 48 que define GAP-151.

Ninguna fuente quedó sin localizar.
