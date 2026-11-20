# Ronda 23, memo A: positividad por reflexión a través de log m = log(kn)

Puerta de selección. No se deriva, no se computa, no se tocan papers ni el índice.

Operación examinada: tomar las casi-coincidencias m ≈ kn (h = m − kn ≠ 0) como pares reflejados
h ↔ −h respecto de la coincidencia exacta h = 0 (Div), para escribir Div_M + Near_M = ⟨θF, F⟩ con una
reflexión θ, y que Arch_M aporte la medida reflexión-positiva.

Cotejo hecho: `ROUTES-MASTER-INDEX.md` (grep «reflexi», «reflection», «Osterwalder», «INV_V_002»: l.1918,
2087, 3016–3020, 4804–4820, 5041, 5828, 5875, 6050), `RULES_AVOID.md` §Z (Z3), `NEAR_DOSSIER.md` l.205,
`phase-200-sign-object/LEDGER_L1_RH1-9_PH000-099.md` l.95–102 y l.140–146, `AUDIT_200_SPEC_002.md`
(final de §5), `phase-193-creation-campaign/CA_A_007_SEED_TRIAGE_HOMOTOPY_TRIPLES_RP.md` (Lema 1,
Teorema 2, l.36–62), `phase-200-sign-object/K1_OSG_001.md`, `phase-196-global-object/INV_V_002_*.md`
(V2.2, V2.4), `ROUND_016_C.md` §§0–3, `phase-6-osterwalder-schrader-reflection/` (M-OS-2, Prop. S2.1).

## (1) Antecedente más cercano

- **CA_A_007 §3** (fase 193). Lema 1: para F = f + Θf con f soportada en un semieje,
  𝔞(F) = 2𝔞(f) + 2H_K(f), con H_K(f) = ∬ f(t)f(s)K(t+s); «RP es la mitad Hankel de la forma
  Toeplitz». **Teorema 2 (PROVED):** si K = K_c − Σ_n (v_n/2)δ_{±log n} tiene un solo átomo en el rango,
  H_K no es ≥ 0 (f_ε concentrada en ½ log n_0 da H_K → −v_{n_0}/2). La l.62 del mismo memo cierra
  explícitamente la versión «cross-place» de NG-E1, que es la que propone LEDGER_L1 S1.
- **K1_OSG_001** (fase 200): reflexión en el borde; el Teorema 2 conjugado por traslación; R-K1 «no
  reintentar reflexiones de borde ni núcleos CM».
- **ROUND_016_C** (fase 212, RULES_AVOID Z3): las tres variantes de elección de θ (traslación del centro,
  n ↦ 1/n, reflexiones por primo θ_p = tablero de CA_J_001) ya descartadas; «Arch es completamente
  monótona» (K(u) = 2Σ_j e^{−(2j+½)u}) probado y ciego.
- **INV_V_002** (fase 196): forma afín de casi-coincidencias 𝔄ff_T; Thm V2.4 (rigidez de Chebyshev, PROVED).

## (2) Objeto u operación nuevos

La candidata nominalmente nueva sería: θ actuando sobre el índice de casi-coincidencia h = m − kn,
θ: h ↦ −h, con Div en el «hiperplano» h = 0. Escrita en las variables reales de la forma no existe:
𝔸_M es una forma en vectores x = (x_m)_{m≤M}; h es un índice de suma interno al núcleo
Near_M(m,k) = ½ Σ_{n≥2, kn≠m} v_n c_0(log(kn/m)), no una coordenada del espacio de Hilbert. Para que
«Div + Near = ⟨θF,F⟩» tenga sentido hay que llevar h a la variable logarítmica t = log(kn/m), y entonces
θ es t ↦ −t, que es (i) la paridad de c_0 (identidad, ciega al peso) o (ii) la reflexión de la mitad Hankel
de CA_A_007 trasladada al punto log m (K1_OSG_001). La versión «pares (p^a, q^b) con θ en
log p^a − log q^b» de LEDGER_L1 S1 es exactamente la cross-place que CA_A_007 l.62 cerró.
**No se puede escribir una fórmula de θ distinta de esas dos.** Además, en la variable h la reflexión no es
exacta: log((m+h)/m) ≠ −log((m−h)/m) a orden h²/m², de modo que ni siquiera la identidad de paridad sobrevive
en h; el «test de asimetría 𝔖_2(h) vs 𝔖_2(−h)» de AUDIT_200_SPEC_002 fue calificado allí de dato, no de ruta,
y además 𝔖_n no depende del peso (falsificador cΛ, c>1, en el mismo memo).

## (3) ¿Evita el motivo exacto de fracaso?

No. El motivo exacto es el Teorema 2: en el esquema OS la parte reflejada R = 2H_K(f) recibe el peine con
signo negativo, y un núcleo de Hankel h(t+s) es ≥ 0 en un semieje sólo si h es transformada de Laplace de
una medida positiva (Widom–Bernstein, CITED); un peine de átomos negativos no lo es. Poner Div en el
hiperplano no cambia nada: Div son los átomos en t = 0 (la diagonal de θ), Near los átomos en t ≠ 0, y ambos
entran con signo −. «Arch aporta la medida reflexión-positiva» es la Observación 1 de ROUND_016_C (ciega).
La diferencia frente a INV_V_002 que LEDGER_L1 dejó pendiente («RP no es un levantamiento hermitiano sino
positividad de semiespacio») es real como enunciado, pero el semiespacio cae entonces bajo el Teorema 2: se
esquiva V2.4 sólo para entrar en CA_A_007 §3.

## (4) Enlace con 𝔸_M ⪰ 0 y controles

El único enlace escribible es Cauchy–Schwarz OS: 𝔞(f) ≥ |H_K(f)| en ambos sectores de paridad, que es la
positividad de la forma restringida a pares e impares (J3, thm:parityschur): reformulación, no mecanismo.
Bajo los tres controles (peso cΛ con c≠2; borrado de una potencia de primo; peso tipo Beurling) el paso con
nombre que debería romperse no existe: RP falla en los cuatro casos por el mismo Teorema 2 (cualquier átomo
basta), y la parte que sí es positiva (Arch, CM) vale en los cuatro casos. Viola (F1) y (F3) (paridad /
cambio de operador de referencia); Arch y el peso no entran en el mismo paso (F2).

## Veredicto

**NO PASA (repetición).** Es la reflexión cross-place de NG-E1 / LEDGER_L1 S1, cerrada por CA_A_007
Teorema 2 (PROVED) y l.62; las variantes de θ están en K1_OSG_001 y ROUND_016_C (RULES_AVOID Z3). La
pendiente «diferencia frente a INV_V_002» queda resuelta: existe, pero desemboca en el Teorema 2. Reabrir
exigiría un θ no expresable como paridad de c_0 ni como reflexión de semieje en t, con fórmula explícita y
con el peine entrando con signo positivo en la parte reflejada; no se identificó ninguno.
