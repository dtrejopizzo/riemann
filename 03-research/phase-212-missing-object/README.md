# Phase 212 — Building the object that carries the sign

Working memos in this folder are written in Spanish.

## Aim

Target (★): λ_A(T) ≥ 0 for every T > 0, with the definitions of
`../phase-211-sign-sandbox/STATEMENT_001.md` (window form a_T on the primitive subspace P_T).
The problem is treated purely as the sign of an explicit quadratic form; no equivalence with any other
statement is used, named or reasoned from. Pure mathematics; computations only to validate concrete
points. No paper is modified until the sign is proved.

Phase 211 is kept as a record. This phase does not continue its towers: it starts from what was PROVED
there and in Papers 47–48 about the shape the object must have, and builds only candidates that pass the
filter of `RULES_AVOID.md`. The object sought is specified in `OBJECT_SPEC.md`: in one line, a family of
exact Gram realisations a_T(F) = ‖V_T F‖²_{ℋ_T} + (manifestly ≥ 0 remainder) on P_T, with V_T built
non-linearly from the exact values Λ(n), n < e^{2T}, whose identity breaks (not merely "loses margin")
under every falsifier.

## What is established and fixes the design

1. **Zero slack.** λ_A(T) ≤ 4·10⁹ T e^{−15.449T} for T ≥ 1 (P47 cor:margin1); the window of positive
   weights closes on c = 1 from both sides (211 LEDGER C43). The sign step cannot be an estimate with
   remainder (P47 thm:shape (B′)); it must be an exact identity "form = manifestly non-negative expression".
2. **Not generic.** An identity valid for every weight vector carries no sign (P47 lem:shape-ident). The
   sign-step identity must fail for cΛ (c ≠ 1), a_P, finite deletion and amplification, and the models of
   the battery (`RULES_AVOID.md` §E).
3. **Conjunction without a common falsifier.** Euler product over ℕ (E), functional equation with
   Γ(s/2) at conductor 1 (F) and integrality (I) used together have no common falsifier
   (P47 rem:conjunctions). What was never built is a **non-linear** sign step in which all three enter
   together. The elementary exact separator is Σ_{d|n} a(d) = log n (P48, scope note after req:spec): it
   identifies Λ, but turning identification into a quadratic bound is OPEN.
4. **The sign lives in the cross terms.** Every line of phase 211 stopped at a joint remainder without
   sign. The existing positive pieces are correct and do not suffice separately.
5. **Grid row 6 used only linearly.** The exact values of Λ (Λ ∗ 1 = log as an identity) never entered a
   sign step non-linearly (P48 §Coordinates).

Available PROVED pieces (not re-derived here): exact reductions (L2) P47 thm:coer-schur, (S) P47 prop:AM,
one profile P47 thm:oneprofile, Nyquist mesh P47 thm:nyq, power ladder 211 POWER_BRIDGE_002 §6, thermal
polynomial kernel 211 GRAM_SLICES §§19.8, 19.10, integer blocks ⟺ real nodes 211 GRAM_SLICES §18; partial
positivities (prop:nearfree; resonant sum of squares with uniform margin, 211 GRAM_SLICES §17; reciprocal
endpoint C_0 of all orders; all-order Gram of the hyperbolic model, 211 HYPERBOLIC §§4–5; certified plane
{E₁,E₂}, 211 GRAM_SLICES §19.9; certified range T ≤ ½log5); identities with the three inputs (finite
Poisson–Chebyshev identity P47 thm:PCfinite and contraction prop:GEgap; theta operator realisation 211
HYPERBOLIC §12.6, without metric).

## Status

- **(★) is OPEN. No construction meeting `OBJECT_SPEC.md` has been obtained.**
- `LEDGER.md` records rounds 1–18 candidate by candidate: closed with NO-GO with class (L-comp, K3),
  accepted without a new mechanism (K1, K2, K4, K1′, K2′, K5), or no candidate passing the selection gate
  (rounds 3–5 and 7–18); round 6 (per-prime window split) is NUMERICAL, reaching the ceiling up to
  T ≈ 0.69 and failing from 0.70.
- Later rounds (`ROUND_019_*` … `ROUND_095_*`) and constructions `BUILD_079`–`BUILD_084` carry their own
  status lines: the builds have sign OPEN (079–083: formulas reviewed, global sign not established);
  `ROUND_095_A/B` are PROVED results about an auxiliary form (negative sign of the cyclotomic finite part;
  no self-energy constant repairs it) and do not decide the sign of the full form.
- Every attempt is registered in `05-meta-and-planning/ROUTES-MASTER-INDEX.md` (Part III.0 and Part V).

Labels used: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL (NUMÉRICO).

## Method

- **Selection gate before building.** Each candidate states the four points of the novelty filter
  (closest antecedent with file/section; the genuinely new object or claim; why the change avoids the
  concrete difficulty of the antecedent; which identity or inequality connects it with global positivity of
  the full form). An independent review checks the difference against the index, the grid, the crossword,
  Paper 48 and `RULES_AVOID.md` before any derivation.
- If no candidate passes, this is recorded and the search continues; novelty is not manufactured.

## Contents

**Core documents**
- `OBJECT_SPEC.md` — specification of the object to build.
- `RULES_AVOID.md` — hard rules, failure patterns, closed families, battery of falsifiers, non-excluded
  ground.
- `BRIEF_CONSTRUCTOR.md` — reading brief for every memo of the phase.
- `LEDGER.md` — one line per candidate, rounds 1–18.
- `NEAR_DOSSIER.md` — compilation of what the corpus knows about the near-coincidence term Near_M.
- `TRIAGE_D_1.md` … `TRIAGE_D_5.md` — triage of row-D ideas recorded but never carried through.

**Series**
- `ROUND_nnn_X.md` — designs and constructions, rounds 001–095 (full list below).
- `REVIEW_*.md` — independent reviews of the rounds.
- `BUILD_079_*` … `BUILD_084_*` — explicit constructions with their data folders.
- `ANNEX_*.md` — complete readings of the index, of phases 114, 161, 170, 193 and 211, comparisons and
  literature.

**Data and scripts**
- `build_079_data/` — scripts (Arb certification, residual and source evaluations) and data for BUILD_079.
- `build_084_data/` — certification scripts and JSON certificates for BUILD_084.
- `free_weight_scripts/` — scripts and outputs for rounds 017–033 (free-weight / window-split numerics);
  subfolders `hp_out/`, `out_032A/`, `out_033/` hold outputs.
- `verify_window_split.py`, `verify_window_split_canonical.py` — numerical checks of the per-prime window
  split (rounds 6 and 17).

## Suggested reading order

1. This README, `OBJECT_SPEC.md`, `RULES_AVOID.md`, `BRIEF_CONSTRUCTOR.md`.
2. `LEDGER.md` for rounds 1–18.
3. `NEAR_DOSSIER.md` and the `TRIAGE_D_*` files.
4. The `BUILD_*` memos and the latest rounds (`ROUND_09*`).
5. `ANNEX_*` files as reference when a round cites them.

## Running the scripts

Python 3 with `numpy`, `scipy`, `mpmath` and `python-flint` (Arb). Scripts import sibling modules, so run
them from their own folder, e.g. `cd build_084_data && python3 certify_three_cells.py`. They are
validation tools for specific memos; a numerical output is not a proof.

## Full index of rounds, reviews, annexes and triage files

- `ROUND_001_A.md` — Ronda 1, memo A — Candidata K1: realización de Gram desde el separador exacto con Poisson y el factor arquimediano
- `ROUND_001_B.md` — Ronda 1 B — Candidata K2: pivotes de Schur a lo largo de un anidamiento multiplicativo de los enteros (memo de selección)
- `ROUND_001_C.md` — Ronda 1 — Candidata K3: sistema ampliado de cuadrados para los cruces no resonantes
- `ROUND_001_D.md` — Ronda 1, candidata K4 — desigualdad multiescala no lineal con Λ más allá de la ventana
- `ROUND_001_L.md` — ROUND_001_L — Rigidez de comparadores de tipo Carathéodory en la escalera de potencias
- `ROUND_002_A.md` — Ronda 2, candidata A — La cola exterior de la hipérbola como suma de cuadrados: memo de selección
- `ROUND_002_B.md` — Ronda 2 B — La factorización de incidencia [log mcd] = E diag(Λ) Eᵀ actuando sobre F (memo de selección)
- `ROUND_002_C.md` — Ronda 002 C — El canal de dos bases primas: memo de selección
- `ROUND_003_1.md` — Ronda 3, opción 1 — Familias de funcionales que ven la ventana y no son la modal theta (memo de selección)
- `ROUND_003_2.md` — Ronda 3, opción 2 — Funcionales y factores que dependen de Λ (memo de selección)
- `ROUND_003_3.md` — Ronda 3, opción 3 — el sector de paridad: productos mn mediante la reflexión J
- `ROUND_003_4.md` — ROUND_003_4 — Selección: coordenada de borde y ancla nula con borde dentro de (G)
- `ROUND_003_5.md` — Ronda 3, opción 5 — el par virial: selección
- `ROUND_003_6.md` — Ronda 3, opción 6 — Conversión conjunta de la identidad finita de Poisson–Chebyshev sin recombinar (memo de selección)
- `ROUND_003_7.md` — Ronda 3, opción 7 — La formulación (S): incidencia de divisores sobre 𝔸_M (memo de selección)
- `ROUND_003_8.md` — Ronda 3, opción 8 — el objeto cuadrático en el peso y la factorización tipo Riccati
- `ROUND_003_9.md` — ROUND_003_9 — Selección: métrica no local de la realización theta
- `ROUND_004_A.md` — Ronda 4, candidata A — La meta SP-161 / L161.1 con pesos con signo y pesos de criba (memo de selección)
- `ROUND_004_B.md` — Ronda 4, zona 1 — Defecto de divisores cuadrático que entra sumando (memo de selección)
- `ROUND_004_C.md` — Ronda 4, zona 3: el resto R(F) del test de Möbius truncado (memo de selección)
- `ROUND_004_D.md` — Ronda 4, zona D — Factorización de 𝔸_M con soporte en las casi-coincidencias m ≈ kn (memo de selección)
- `ROUND_004_E.md` — ROUND_004_E — Selección: formas indefinidas (Kreĭn/Pontryagin) con vector neutro no radical
- `ROUND_005_G1.md` — Ronda 5, semilla G1: objeto de grado ≥ 3 cuya hessiana sea la forma
- `ROUND_005_G2.md` — Ronda 5, semilla G2 — cierre bajo producto de factores de Euler aplicado a la signatura
- `ROUND_005_G3.md` — Ronda 5, semilla G3 — una medida construida desde la forma cuyo cierre dé el signo
- `ROUND_005_G4.md` — Ronda 5, semilla G4: inducción que alarga la ventana con la identidad de divisores en el paso
- `ROUND_005_G5.md` — Ronda 5, memo G5: invención libre desde A1–A6 (deducción hacia atrás de los tipos de objeto)
- `ROUND_006_WINDOW_SPLIT_NUMERIC.md` — Ronda 6 — Reparto local dependiente de la ventana en T = 0.5925 (NUMÉRICO)
- `ROUND_007_A.md` — Ronda 7, memo A: el cuadrado del déficit, la representación de estado fundamental de los contactos y las condiciones de optimalidad del re
- `ROUND_007_B.md` — Ronda 7, B — predicado de etapa para la inducción por primos
- `ROUND_007_C.md` — Ronda 7, encargo C — relación no lineal en el peso entre convolución y ventana
- `ROUND_008_A.md` — Ronda 8, encargo A — el concomitante de borde que convertiría el canal de producto en el de cocientes
- `ROUND_009_G1.md` — Ronda 9, encargo G1 — objeto con papeles invertidos: la aritmética como fuente de signo
- `ROUND_009_G2.md` — Ronda 9, G2: recursión con dato de etapa dependiente de la historia
- `ROUND_009_G3.md` — Ronda 9, encargo G3 — dónde el mapa no tiene marcas
- `ROUND_010_A.md` — Ronda 10, A: covariancia aditiva como mecanismo del signo
- `ROUND_011_A.md` — Ronda 11, A: los residuos abiertos de (PC) y la discrepancia reticular unilateral
- `ROUND_012_A.md` — Ronda 12, A: el residuo L161.4 y su paso a todo P_T
- `ROUND_013_A.md` — Ronda 13 A — Ingeniería inversa en pequeño: la ventana ½log 4 < T < ½log 5
- `ROUND_013_B.md` — Ronda 13, memo B: el peso como caso de igualdad de una positividad (Gram, Schur, cuadrado completado)
- `ROUND_013_C.md` — Ronda 13, C — mapa de operaciones de combinación entre objetos con signo y objetos que ven el peso
- `ROUND_014_A.md` — Ronda 14, A — linealizar el canal de cocientes: independencia de los primos, polarización y transporte desde el canal de productos
- `ROUND_014_B.md` — Ronda 14, memo B: positividad de Schur–Schoenberg sobre el producto de Euler como fuente propia de un bloque no Gram
- `ROUND_014_C.md` — Ronda 14, memo C: transición entre ventanas que no es la inclusión
- `ROUND_015_A.md` — Ronda 15, memo A — Transporte de retardos no afín: cotejo y cierre por repetición
- `ROUND_015_B.md` — Ronda 15, memo B: acoplar primos distintos en el reparto por bloques, y matrices GCD como acople
- `ROUND_015_C.md` — Ronda 15, memo C — Funcional convexo con hessiano a_T (O14) y emparejamiento impar no lineal en A_M (O-odd)
- `ROUND_015_D.md` — Ronda 15 — D. Umbral del reparto DIR, vector de transferencia y cuenta de cuadrados faltantes
- `ROUND_016_A.md` — Ronda 16, memo A — Curvatura (Γ₂, Bakry–Émery, Lichnerowicz) como fuente del signo
- `ROUND_016_B.md` — Ronda 16, memo B — estados KMS sobre álgebras donde actúan juntas la suma y el producto de ℕ
- `ROUND_016_C.md` — Ronda 16, memo C: positividad por reflexión, desigualdades de correlación y dominación gaussiana como fuente del signo
- `ROUND_017_A.md` — Ronda 17, memo A: el muro de log 2, el muro del reparto DIR y el reparto de los átomos
- `ROUND_018_A.md` — Ronda 18, memo A: representación de estado fundamental con `φ` de signo variable para el reparto local en `T ∈ (0.60, 0.69)`
- `ROUND_019_A.md` — Ronda 19, memo A — Control de escala: ¿es el margen `e^{−2πe^{2T}}` la cola reticular más allá de `N = e^{2T}`?
- `ROUND_020_A.md` — Ronda 20, nota A — índice negativo de la forma arquimediana en P_T para todo T
- `ROUND_020_B.md` — Ronda 20, memo B — La identidad de radical de `M` como una sola relación lineal entre el símbolo y los pesos
- `ROUND_021_A.md` — Ronda 21, memo A — La familia casi radical `{Π_T(M∗φ)}`: cuenta y enunciado estructural
- `ROUND_022_A.md` — Ronda 22, memo A — «Deshacer la suma»: ¿un solo objeto?, y la congruencia de Möbius sobre 𝔸_M
- `ROUND_022_B.md` — Ronda 22, memo B — la reformulación «blanda» con una norma fuerte
- `ROUND_022_C.md` — Ronda 22, memo C — Postura «primer contacto»: inventario del vector nulo y cotejo de dos ideas
- `ROUND_023_A.md` — Ronda 23, memo A: positividad por reflexión a través de log m = log(kn)
- `ROUND_023_B.md` — ROUND_023_B — Puerta: (PC) comprimida antes de emparejar y orientación del salto terminal
- `ROUND_023_C.md` — Ronda 23, memo C — Bloque interior I^λ con pesos de criba y lema 𝒩_k(ν): puerta de selección
- `ROUND_023_D.md` — Ronda 23, memo D — ¿identidad exacta de la cancelación por átomo para vectores generales?
- `ROUND_024_A.md` — Ronda 24, memo A — Término principal del defecto de truncación: ROUND_019_A §§2–4 frente a ROUND_021_A §3
- `ROUND_024_B.md` — Ronda 24, memo B — ¿Bloque casi nulo de la 211 = familia casi radical `{Π_T(M∗φ)}`?
- `ROUND_024_C.md` — ROUND 024 C — Las tres comprobaciones baratas que dejó el triage de la fila D
- `ROUND_024_D.md` — ROUND_024_D — Puerta: objeto de grado ≥ 2 con el Möbius del sistema μ_a y la fuga de borde
- `ROUND_025_A.md` — ROUND_025_A — Cotejo de antecedentes: esquema «existencia + rigidez» (WF)/(R)/(E) contra Paper 47 y fases 153–160, 197
- `ROUND_025_B.md` — Ronda 25, memo B — Ataque lógico al esquema «existencia + rigidez» (R)/(E)/(WF)
- `ROUND_026_A.md` — ROUND_026_A — Cómputo del valor cóncavo V*_T frente a λ_A(T)
- `ROUND_026_B.md` — Ronda 026 B — (PBP_T) como problema extremal exacto; argumento de Kreĭn y densidad; puerta de cuatro puntos
- `ROUND_027_A.md` — Ronda 027-A — Verificación numérica hostil del peso atenuado `v_n cos(ω log n)`
- `ROUND_027_B.md` — ROUND_027_B — Cotejo hostil de antecedentes: peso atenuado v_n·cos(ω log n) y clausura por K_T cerrado
- `ROUND_027_C.md` — Ronda 27, memo C — Estructura de la forma atenuada `a^{(ω)}_T`
- `ROUND_028_A.md` — Ronda 28, memo A — Estado extremal del problema de peso libre no negativo
- `ROUND_029_A.md` — Ronda 029-A — Peso atenuado `w_n = v_n cos(kπ log n/(4T))` con base de elementos finitos hp
- `ROUND_030_A.md` — Ronda 030-A — Rigidez del peso sin temperamento: el hueco en Z, formulado y atacado
- `ROUND_030_B.md` — Ronda 030 B — Cadenas de divisores, masa espectral en baja frecuencia y primitividad en (PBP_T)
- `ROUND_031_A.md` — Ronda 031 A — Cotejo de antecedentes: desigualdad de funciones enteras con ceros en ±i/2 para (PBP_T)
- `ROUND_031_B.md` — Ronda 031 B — Primitividad como cota cuantitativa y generación del bloque negativo por traslaciones en log ℕ
- `ROUND_032_A.md` — Ronda 032-A — ¿Es la existencia de pesos con margen una propiedad de los enteros? (NUMÉRICO)
- `ROUND_032_B.md` — ROUND 032 B — Puerta de selección: (PBP_T) como problema de medidas representantes del origen en el polidisco infinito
- `ROUND_095_A.md` — Dilataciones primas: signo negativo de la parte finita ciclotómica
- `ROUND_095_B.md` — Ninguna constante de autoenergía repara la parte finita ciclotómica
- `REVIEW_001_ABD.md` — Revisión de las memos de selección ROUND_001_A, ROUND_001_B y ROUND_001_D
- `REVIEW_001_LC.md` — REVIEW_001_LC — Revisión hostil de ROUND_001_L y ROUND_001_C
- `REVIEW_002_A.md` — REVIEW_002_A — Revisión hostil de ROUND_002_A (cola exterior de la hipérbola como suma de cuadrados)
- `REVIEW_002_BC.md` — REVIEW_002_BC — Revisión hostil de ROUND_002_B y ROUND_002_C
- `REVIEW_003.md` — Revisión de la ronda 3 (selección sobre nueve zonas no excluidas)
- `REVIEW_004.md` — Revisión de la ronda 4 (meta SP-161 con pesos con signo y cuatro zonas no excluidas)
- `REVIEW_005.md` — Revisión de la ronda 5 (generativa: escribir un objeto desde la especificación A1–A6)
- `REVIEW_006.md` — Revisión de la puerta de selección tras la ronda 6 (reparto por reglas: bandas de distancia y potenciales por primo)
- `REVIEW_007.md` — Revisión de la ronda 7 (`ROUND_007_A.md`, `ROUND_007_B.md`, `ROUND_007_C.md`)
- `REVIEW_009.md` — Revisión de la ronda 9 (`ROUND_009_G1.md`, `ROUND_009_G2.md`, `ROUND_009_G3.md`)
- `REVIEW_022_027.md` — Revisión hostil de ROUND_022_A, 024_A, 024_B, 025_B y 027_C
- `REVIEW_030_031.md` — Revisión hostil de ROUND_030_A, ROUND_030_B y ROUND_031_B
- `ANNEX_114_D163_D135.md` — Anexo — Los objetos D.163 y D.134/D.135 de la fase 114: enunciados, estatuto y relación con la fase 212
- `ANNEX_161_FILES_1.md` — Anexo: lectura por archivo de la fase 161, tramo 1 (README y R161_000 a R161_027)
- `ANNEX_161_FILES_2.md` — Anexo: lectura por archivo de la fase 161, tramo R161_028 – R161_055
- `ANNEX_161_FILES_3.md` — Anexo: lectura por archivo de la fase 161, tramo 3 (R161_056 a R161_099)
- `ANNEX_170_FILES_1.md` — Anexo 170 — archivos, tramo 1 (R170_000 a R170_822)
- `ANNEX_170_FILES_2.md` — Anexo: fase 170, archivos R170_823 a R170_840
- `ANNEX_170_FILES_3.md` — Anexo 170 — tramo 3: archivos R170_841 a R170_862
- `ANNEX_170_FILES_4.md` — Anexo 170 — tramo 4: archivos R170_863 a R170_900
- `ANNEX_211_FILES_1.md` — Anexo 211 — Archivos AUDIT_001 … POWER_DEFICIT_LIMIT_013 (61 archivos)
- `ANNEX_211_FILES_2.md` — Anexo 211 — Archivos, segunda tanda (POWER_DESCENT_016 … POWER_INVERSE_INTERIOR_022)
- `ANNEX_211_FILES_3.md` — Anexo 211 — tercer tramo de archivos (POWER_INVERSE_INTERIOR_AUDIT_022 … POWER_RECURRENCE_BOUNDARY_036)
- `ANNEX_211_FILES_4.md` — Anexo 211 — Archivos POWER_REDUCTION_AUDIT_044 … POWER_THETA_DENSITY_ORIGIN_087 (106 archivos)
- `ANNEX_211_FILES_5.md` — Anexo 211, bloque 5 — lectura completa de `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md` … `ROUND_001_A.md`
- `ANNEX_211_FILES_6.md` — Anexo 211 — archivos ROUND_001_B a ROUND_007_B (lectura completa)
- `ANNEX_211_FILES_7.md` — Anexo 211 — archivos ROUND_007_C a ROUND_016_A (lectura completa)
- `ANNEX_211_FILES_8.md` — Fase 212 — Anexo de lectura completa: archivos de la fase 211, bloque 8
- `ANNEX_211_GLOBAL_REVIEW.md` — Anexo — Lectura completa de `phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`
- `ANNEX_211_GRAM_HYPERBOLIC.md` — Anexo 211 — Kernel Gram por traslación, modelo hiperbólico y auditoría
- `ANNEX_COTEJO_LORENTZ_1.md` — Anexo — Cotejo dirigido: Hodge, Lorentz, Alexandrov–Fenchel, log-concavidad
- `ANNEX_COTEJO_LORENTZ_2.md` — Anexo de cotejo — signatura de tipo Lorentz y mecanismos con reglas de cierre (tramo 2: estabilidad, Lee–Yang, Laguerre–Pólya, positi
- `ANNEX_COTEJO_NULLDIR.md` — Anexo de cotejo — direcciones casi nulas de a_T sobre P_T y ventana en c
- `ANNEX_INDEX_04.md` — Fase 212 — Anexo al consolidado: índice de rutas, fases 100–189 (archivo 04)
- `ANNEX_INDEX_README.md` — Anexo a RULES_AVOID — índice de rutas, README líneas 366–2396
- `ANNEX_LITERATURE_CONCENTRATION.md` — Anexo — literatura: mecanismos de positividad de tipo concentración
- `ANNEX_MARGIN_CONFLICT.md` — Anexo: el conflicto sobre el margen de λ_A(T)
- `ANNEX_PHASE_193_LABELS.md` — Anexo — Re-etiquetado de las candidatas de la fase 193
- `ANNEX_PHASE_193_PRIMARY.md` — Anexo — Lectura primaria completa de la fase 193 y contraste con ANNEX_PHASE_193_LABELS.md
- `ANNEX_SONIN_READING.md` — Anexo — Lectura en primaria de la cadena de Sonin semilocal
- `TRIAGE_D_1.md` — Triage D-1: ideas de la fila D registradas y nunca llevadas a término (lista 1, ítems 1–41)
- `TRIAGE_D_2.md` — Triage D-2: ideas de la fila D escritas y nunca ejecutadas (ítems 42–82)
- `TRIAGE_D_3.md` — Triage D, lista 3: ideas de la fila D registradas y no llevadas a término (ítems 83–123)
- `TRIAGE_D_4.md` — Triage D — lista 4 (ítems 124–164, fases 170–211)
- `TRIAGE_D_5.md` — Triage D, lista 5 (ítems 165–201)
