# Triage D, lista 5 (ítems 165–201)

Ámbito: ideas de la fila D registradas en las fases 124–211 como propuestas y no ejecutadas, o abiertas con condición de reapertura escrita. Filtros F1–F5 tal como se fijaron en la fase 212. Este documento clasifica; no se construye, deriva ni calcula nada.

Abreviaturas (rutas bajo `03-research/`): GLOBAL = `phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`; HY = `phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`; GRAM = `phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md`; IDX = `05-meta-and-planning/ROUTES-MASTER-INDEX.md`.

## §1 Tabla

| nº | Idea | Fuente (pasaje abierto) | Clase | Razón y cita |
|---|---|---|---|---|
| 165 | Pasada de verificación: ¿la identidad 𝔊_T = S^Sch_T + J afina el término ‖K‖ no controlado? | `phase-211-sign-sandbox/AUDIT_002.md` §Hits, l.144–152 | LOCAL/NUMÉRICA — no decide nada | La fuente pide una pasada de verificación de coherencia. Una partición tipo Schur de vectores construidos desde F vale para todo peso (F3), y afinar ‖K‖ es mejorar una cota con holgura (F4). |
| 166 | C4 lente corona/símbolo; C6 defecto de transporte M→M+1 / coercividad de ventanas adyacentes; C7 Carathéodory–Fejér | `phase-211-sign-sandbox/LEDGER.md` l.8–11 | REF (C4, C7) / REP212 (C6) | C7 trae su condición escrita: «"dies at the limit" (phase 35) must be answered». No se aporta respuesta, y la extensión CF de ventana finita reformula la positividad de Toeplitz (F5). C4 tampoco tiene un lado independiente. C6 es compensación entre escalas: memoria de selecciones de las reglas del proyecto (POWER_DESCENT_016 §§2–4). |
| 167 | SURVEY_001, Top 10 restantes (Papers 07, 15, 24, 09, 36, 35, 12, 16) | `phase-211-sign-sandbox/SURVEY_001.md` l.371–382 | REF / CIEGA / CERRADA (Paper 35) | La fuente da una razón de novedad por objeto (aplicación a S_{T,k} finito), pero no aporta mecanismo de signo. Paper 35 (Bakry–Émery de primos): cerrado por ROUND_005_D, INV_N_001 y ROUND_016_A. Paper 09 (concavidad en caja de Λ(n)): la caja contiene c = 2 y los borrados (F1). Papers 07, 15 y 36 son criterios sobre S_{T,k} (F5). Paper 24 es analogía; 12 y 16 no tienen promoción escrita. |
| 168 | k=0: probar B_N ≤ 2N·A_N, o B_N ≥ A_N con liminf A_N ≥ 0 | `POWER_STATE_064.md` l.28–38; `POWER_STATE_065.md` l.13 | REP212 / CIEGA | 065: sin prueba ni contraejemplo. Cerca de u = ½ la cancelación polar/continuo impide dominancia, y sólo se obtiene B_N − A_N → 1 eventual. 064 reconoce que reproduce 016/036/Bessel019. Cubre sólo k = 0. |
| 169 | «Dos medias»: comparar firmadamente E_{ν+}D y E_{ν−}D | `POWER_STATE_065.md` §Consulta066, l.15–18 | CIEGA | La fuente: «el conteo 065 no proporciona por sí solo una estimación de compensación». Comparar medias de D(x) = ψ_Λ(x) − x + 1 bajo una medida firmada no aporta operación de signo (cf. GLOBAL «presupuesto022»: la medida firmada no admite reglas de probabilidad). |
| 170 | Probar G_W(v) ≥ 0 ∀v > 0 (fila k=0 por mezcla gamma) | `POWER_STATE_067.md` l.21–23 | CERRADA (ARGUED) | GLOBAL, «Transferencia comprobada a los inversos gaussianos»: 128/129 fuerzan una gaussiana con h_a(1) < 0 y «la positividad inversa universal gaussiana no puede servir de premisa». G_W″ < 0 para a ≥ 65536 (IDX l.7497, l.8158). Falta confirmar que h_a coincide con G_W. |
| 171 | Criterio Wronskiano J′Φ_u − JΦ_u′ > 0 | `POWER_STATE_075.md` §Consulta076, l.19–41 | CERRADA (superada) | La fuente: no demostrado para Φ real, y aunque se demostrara no daría el kernel de dos nodos. La torre de Wronskianos 087–089 quedó PARCIAL, sin S4 global (IDX l.7558–7564). |
| 172 | Turán a_{N,k}a_{N+2,k} − a_{N+1,k}² | `POWER_STATE_055.md` l.35–37 | REP (interna de la 211) | 055 detiene la consulta porque el registro 046 ya vuelve a momentos/determinantes (IDX l.7429, l.8134). La herencia escalar está falsificada en FOUR_TURAN_084 (IDX l.7368). |
| 173 | Numérico anunciado e inexistente de ROUND_008_A §4 (c = 1.01, r, K*) | `phase-211-sign-sandbox/ROUND_008_A.md`; `ROUND_008_D.md` l.129–190 | LOCAL/NUMÉRICA — no decide nada | ROUND_008_D ya da K* ≈ 25–30 (T = 1.0) y ≈ 105–125 (T = 1.2), con el test cΛ en c = 1.01 y c = 1.1. Rellenar 008_A sólo daría un grado a un T fijo (F4). |
| 174 | Del modelo cosh genérico a la aritmética real en escala √N | `POWER_SIGNED_TRANSFORM_035.md` §§5, 7–8 | CIEGA | §7 muestra que el modelo cosh positivo da A_2,model < 0: la simetría no fuerza el signo. §8 deja como paso siguiente «estimar el promedio aritmético en escala √N», sin mecanismo. El pedido es la propia obligación aritmética. |
| 175 | GRAM: desplazamiento A − a, «no se ha construido tal compensación» | GRAM l.989–991 y §8.11 l.1038–1060 | CERRADA (PROVED, en su clase) | GRAM §8.11 PROVED: para todo c > 0 y todo intervalo, K_M − cG no es PSD. No existe un margen de Cauchy positivo uniforme en todos los órdenes, así que el desplazamiento por una constante no puede llevar el signo. Coincide con F4. |
| 176 | presupuesto022: desigualdad independiente que pague ARCH_sharp | GLOBAL l.150–162 | REF / REP212 | GLOBAL: la obligación es A_N + 2∫K_N C_B ≥ 0, con A_N de límite negativo (LOW_TABLE018). La parte afín vuelve a RENORMALIZED_TAIL042 y 062 tiene déficit. Antecedente: `phase-188-closing-D/N_BUILD_022_MATRIX_IDENTITY_FOR_X_M.md` §1. F2. |
| 177 | Interpolación geométrica φ_s = φ_0 e^{sh} | GLOBAL l.310–320 | CERRADA (aplicación de un falsificador) | h = a cosh(2t): kernels PSD (HY §5), derivada no PSD (HY §9). Exigir PSD de la derivada es más fuerte que exigirlo de la integral. |
| 178 | Cuatro propuestas detenidas: testigo nodal; tasas antes de T; Jensen para operadores; BPY par/impar en escala ¼ | GLOBAL l.2276–2290 | REP212 | Cada una tiene antecedente nombrado en la fuente: P121_FIVE §5, L2_BUILD_004 §§1–4; 106_51 §§1–5; 106_99 §6, R186_033 §1; «Autodescomposición BPY por escala». Para reabrir se exige una afirmación adicional; no se aporta. |
| 179 | Acoplamiento f_{N+1} = f_N * Gamma(2, π(N+1)²) / símplex Dirichlet | GLOBAL l.2340–2350 | REP212 / CIEGA | La fuente dice que el símplex ya aparece en la expansión de los aproximantes y que la renovación plegada conserva los cruces. La convolución positiva sirve para todo peso (F1). |
| 180 | Corte de puente gaussiano BPY | GLOBAL l.2360–2370 | REF | La condición de reapertura, «A completa con medida positiva y sin resto», es el objetivo reescrito (F5). Antecedente: autodescomposición BPY por escala. |
| 181 | Transferencia triangular (Volterra) T h = h + ∫k h, A[G_2] = T A[G_1] T* + R | GLOBAL l.2525–2545 | CIEGA / REP | No hay k ni entrelazamiento; R definido por diferencia deja el signo pendiente (fuente). El formato congruencia + Gram vale para todo peso (F3). Antecedentes: phase-114 `114_d_78` §7, Volterra relativo REF-D (IDX l.4672), Volterra bruto FALSIFIED (IDX l.6563, l.7583). |
| 182 | Variación compensada de dos tasas; operador de etiquetas SF | GLOBAL l.2354–2375 | REP212 | La fuente: «no se encontró la diferencia matemática exigida»; la rigidez BPY de tasas lo impide. GRAPH ya realiza el operador de etiquetas. |
| 183 | HY §12.7: métricas no locales, no acotadas, conexiones nuevas, otras realizaciones | HY l.860–875 | REP212 | Memoria de selecciones de las reglas del proyecto, «Reserva de métricas no locales». Reabrir requiere un kernel no local positivo con identidad Green; no se aporta. |
| 184 | HY §12.5: escape operatorial | HY l.670–685 | CERRADA (parcial) / REP | §12.5 está PROVED en la clase regular declarada: la deriva determina un kernel de ondas. Lo que queda abierto es otra realización, igual que en 183. F3 / D.186. |
| 185 | Selberg completo vs compensado | GLOBAL l.262–270 | REP / CIEGA | P1_BBSTAR_001 §§2.6–2.8 y ROUND005C §5.3(i) ya conservan el cuadrado negativo. Sólo hay un diagnóstico NUMÉRICO sin falsificador. Los cuadrados de primos son ciegos al peso (F1). |
| 186 | Fase 154: corrida «--offlat», ansatz de Lemma W, parametrización de 𝒫_T, cota de clase, r6ub.py M = 24…96, ids arXiv | `phase-154-row-d-law-of-the-body/R154_017_ROUND6.md` l.39; `R154_029_AUDIT_R10.md` l.12–15; `R154_030_CLOSING_DECISION_R5_R10.md` l.31; `R154_018_ROUND7_BLUEPRINT.md` | LOCAL/NUMÉRICA — no decide nada | «--offlat» está implementado y nunca corrido. Todo es LP a T fijo (T = 0.58, M ≤ 96). La cota de clase es «No idea in hand» según la propia fuente. Los ids arXiv son higiene bibliográfica. |
| 187 | Fase 153: P153.1, .3, .7, .8, .9, .15 | `phase-153-row-d-sign-carrying-endpoint/R153_005_CLOSING_DECISION.md` l.47–49; `R153_007_TRACK1_SINGLE_PAIR.md` l.275–277; `R153_008_TRACK2_NEEDLE.md` l.207; `R153_017_ROUND5_CLOSING_DECISION.md` l.17, 33; `R153_019_ROUND6_BODY.md` l.238, 321 | LOCAL/NUMÉRICA (P153.1, .3, .7, .9 y .15) / OTRO OBJETO (P153.8) | P153.3 a ½log5: λ_min ≤ 3.2·10⁻¹² (Galerkin), «not answered»; está a T fijo y por debajo de la frontera ½log15. P153.8 trata versiones con pares fuera de la línea en el lado de ceros, no la forma a_T. P153.15 es una coincidencia numérica. |
| 188 | PRECHECK_T1_001: correr μ = 50 y 80; reformular T1 con Π | `phase-199-frontier-pattern/proof-L-sharp/PRECHECK_T1_001.md` l.9–11 | LOCAL/NUMÉRICA — no decide nada | La fuente ya confirma el orden principal de M3 al 2–3 %, con signo positivo en todos los casos. Más μ sólo afinaría el desfase. Reformular T1 con Π es REF. |
| 189 | JJ_001: residuos R1 (símbolo→operador, Fresnel), R3, R4 | `phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_JJ_001_REOPEN_7_3.md` l.17–26, 93, §6 | CERRADA (reapertura negativa) / REF | Veredicto de la fuente: «neither reopening reaches the real extremal. L′♯ OPEN». R1 es el error de sustitución n^{3/2}c^{−½}, de naturaleza técnica. El objetivo L′♯ es una reformulación de la fila D. |
| 190 | P124_011, rango ρ_{+,T} ∈ Ran L_T^{1/2}; P124_012, estimación (3.3) sin supertraza | `phase-124-direct-first-contact/P124_011_SCHUR_COLLAR_REDUCTION.md` l.5–20; `P124_012_CAUSAL_STORAGE_SCALAR_SEAM_GATE.md` l.143–157 | REF | La fuente: «missing range condition is precisely the desired collar cancellation». Es una condición de Douglas equivalente al objetivo (F5). (3.3) es la desigualdad unilateral misma. |
| 191 | Fase 143: O-28, O-24, O-26, O-27, O-29, O-19′; s_* de cono | `phase-143-row-d-trace-positive-cone/R143_001_ROUND1.md` l.53–68; `R143_003_ROUND2.md` l.162–166; `R143_005_CLOSING_DECISION.md` l.21, 40 | OTRO OBJETO / REF | s_* está definido sobre los ceros (lado espectral). O-28 es la interpolación de un CLAIM rebajado. El cono traza-positivo B4 dio (T1) NO y (T2) falso. Nada de esto actúa sobre a_T en P_T. |
| 192 | Fase 146: O-46.1 «DO NOT ATTEMPT»; O-46.2; O-46.4; O-46.5 | `phase-146-row-d-coupled-pairing/R146_001_ROUND1.md` l.661–687; `R146_003_ROUND2.md` l.28–32, 346 | REF | La fuente rotula O-46.1 «suspected equivalent» y mantiene la prohibición. O-46.2 es una inconsistencia de constante, ya corregida por M8 (R146_004 l.45). |
| 193 | Fase 150: O-150.2, O-150.3 | `phase-150-row-d-method-theorems/R150_001_ROUND1.md` l.875; `R150_005_CLOSING_DECISION.md` l.56–58; `R150_002_AUDIT.md` l.83 | LOCAL (bibliográfica) / OTRO OBJETO | O-150.2 es literalmente una consulta de literatura (regiones tipo Vinogradov–Korobov en clases de Beurling). O-150.3 pide celdas de puerta para los modelos ζ_𝒫 y Ξ_Q. Ninguna trata el signo de a_T. |
| 194 | Fase 149: (C) OPEN para c ≥ ½ | `phase-149-row-d-additive-pencil/R149_003_REPAIRS.md` §1, l.45–98 | CERRADA (superada) | La reparación degrada (C)/(C′): (E) sola cubre todo c < 1, y el umbral c = ½ sólo aparece en (C) con q_0 > 1. Ya no se necesita. |
| 195 | Fase 137: (23d); puerta D.14 | `phase-137-row-d-canonical-coupling/R137_003_ROUND2.md` l.564–577; `R137_005_ROUND3.md` l.286–292; `R137_007_CLOSING_DECISION.md` l.16 | OTRO OBJETO | (23d) pide cotas sobre Λ_W en Re s = 1. D.14 queda cerrada mientras no se resuelva (23c) (si h⁰_Z(mK) es siquiera finito). Es el bloque geométrico de h⁰. |
| 196 | Fase 138: D.17-α, D.15-β, D.16-α, D.16-β | `phase-138-row-d-detecting-cones/R138_003_ROUND2.md` l.27–29, 66–67; `R138_005_CLOSING_DECISION.md` l.29, 80–81 | LOCAL (bibliográfica, D.17-α) / REF | D.17-α es una búsqueda de atribución. D.15-β pide una descripción del cono amplio sin I_∞, que es una reformulación. La fuente: «never as a sign». |
| 197 | Fase 140: candidato (β) de h⁰ con (U1)/(U2); O-15′ | `phase-140-row-d-frobenius-square/R140_001_ROUND1.md` l.720, 817–825; `R140_005_CLOSING_DECISION.md` l.21 | OTRO OBJETO | (U1) y (U2) son problemas de unidades y de diccionario de grado. O-15′ es la mitad de necesidad del lado de ceros. |
| 198 | Fase 136: teorema de ausencia de margen; E67.8; S7 | `phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md` l.76–77, 124 | CERRADA (ausencia de margen) / OTRO OBJETO | El margen ya está acotado: λ_A ≤ C e^{cT} e^{−2πe^{2T}} (R160_M4_R1 B(i), F4); además, GRAM §8.11. E67.8 trata de estados sobre un álgebra de semigrupo. S7 es «Deninger sin Hasse». |
| 199 | Fase 135: (22) convexidad de h⁰ = Φ(H⁰); (21) | `phase-135-row-d-canonical-class` (búsqueda sin coincidencia de la etiqueta) | OTRO OBJETO | Bloque de h⁰ y transferencia de Hodge condicional; no se localizó el pasaje (§4). |
| 200 | Fase 134: temperancia de 𝔏 (Rem 3.6b) | `phase-134-row-d-opening/R134_007_CLOSING_DECISION.md` l.40; `R134_006_ROUND3.md` l.83 | REF / OTRO OBJETO | La fuente: «equivalent to a PNT-type growth bound, not decided». Es una propiedad de un objeto auxiliar. |
| 201 | Fase 154: ϑ(μ) → π/4 y constante O(1/n) | `phase-154-row-d-law-of-the-body/R154_004_ROUND2.md` l.10, 196, 307 | OTRO OBJETO | La fuente lo da como ley de Kwaśnicki, «sin vínculo con el signo». |

Recuento por clase principal:
- **CERRADA (7):** 170, 171, 175, 177, 189, 194, 198.
- **REF (8):** 166, 167, 176, 180, 190, 192, 196, 200.
- **REP212 (8):** 168, 172, 178, 179, 182, 183, 184, 185.
- **CIEGA (3):** 169, 174, 181.
- **LOCAL/NUMÉRICA (7):** 165, 173, 186, 187, 188, 193 y la parte bibliográfica de 196; ninguna decide nada.
- **OTRO OBJETO (5):** 191, 195, 197, 199, 201.
- **VIVA (0).**

Varios ítems tienen clase mixta, indicada en la tabla. Un ítem cuenta una sola vez, por su primera clase.

## §2 Entradas VIVA

Ninguna. La lectura de los primarios no promovió ningún ítem y endureció tres:
- 175 pasa a CERRADA por GRAM §8.11 (PROVED: no existe un margen de Cauchy uniforme).
- 194 pasa a CERRADA porque la reparación R149_003 ya no necesita (C).
- 189 pasa a CERRADA porque la propia reapertura concluyó negativa.

El candidato más fuerte, la transferencia triangular de 181, sigue sin k explícito ni ley de entrelazamiento. Su formato congruencia + Gram sobrevive a los tres controles (c = 2, borrado de una potencia de primo, peso de tipo Beurling) sin fallar en ningún paso nombrado (F3).

## §3 Ítems LOCAL/NUMÉRICA que deciden algo

Ninguno. Todo es certificación a T fijo (186, 187, 173), un ajuste de discrepancia ya confirmado al 2–3 % (188), una verificación de coherencia (165) o higiene bibliográfica (186: ids arXiv; 193: O-150.2; 196: D.17-α). Por F4, nada de esto se extiende a todo T.

## §4 Fuentes abiertas y no encontradas

Fuente primaria abierta (pasaje citado en la tabla): 165, 166, 167, 168, 169, 170, 171, 172, 173 (vía ROUND_008_D), 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 200, 201.

No encontrado o abierto sólo en parte:
- **199:** la búsqueda de «(22)», «(21)» y «convex» en `phase-135-row-d-canonical-class` (README y cierre) no dio el pasaje. Queda clasificado por el estado registrado de la fase.
- **173:** el §4 de `ROUND_008_A.md` se trató a través de ROUND_008_D, sin releer 008_A.
- **170:** clasificación ARGUED. Falta confirmar que el h_a(1) < 0 forzado en GLOBAL corresponde exactamente al funcional G_W(v) de 067.
