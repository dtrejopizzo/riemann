# R9 — Fase 2.3.F-CLOSE-II: tres frentes nuevos (N1 Lanczos · N2 trazas · N3 Liouville-Green)

**Fecha:** 2026-06-25.  **Engine:** `engine_cache.py` (cache a 50 díg. de `build` de E70), dps=40,
falsador DH en los tres.  **Objetivo:** atacar 2.3.F-Loc con herramientas **intrínsecas y robustas**
que NO repiten los 8 atajos muertos (R3–R8). λ ∈ {7,9,11,13,15(,17,19,21)}.

## N1 — Jacobi intrínseca vía Lanczos exacto sobre `A` de Weil (`E79_lanczos_intrinsic.py`)

**RESULTADO POSITIVO (ganancia metodológica real).** Lanczos exacto (mpmath, reortogonalización
completa) sobre la matriz de Weil `A`, arrancando de un vector cíclico de **ambas paridades**:

- **Reproduce la escalera EXACTAMENTE en el residuo `e^{−cL}`**: a λ=9, espectro de la tridiagonal
  de Lanczos = `[1, 3.998, 9.026, 16.056, 25.22, 36.386]` ≈ `(k+1)²`, con `rep_err = 0` (exacto).
  **Esto DERROTA el obstáculo de E76**: E76 inyectó base seno externa (error O(1), 19 órdenes por
  encima del residuo) y se rompió; Lanczos es una reducción ortogonal *interna* → estable, alcanza
  el residuo sin base externa.
- **Sub-sector de paridad:** un vector de arranque par sólo excita el sector par → escalera
  `1, 9.05, 25.4, 50.7 ≈ (2k+1)²` (consistente, confirma la estructura).
- **Insight estructural (mecanismo, medido):** la Jacobi intrínseca tiene coeficientes
  `αₙ, βₙ = O(1)`, **acotados** y **alternados por paridad** (`α≈[0.79, 3.69, 0.85, 3.68, 0.88,…]`).
  NO crecen como la Jacobi prolata **desnuda** de Connes (Prop 3.5, `bₙ ≈ 2πλ²·8n`, crecimiento
  lineal `~n¹`). **La balanza de Weil + Doob ELIMINA la escala `2πλ²`**, dejando una Jacobi de
  coeficientes acotados cuyo espectro bajo es la escalera `(k+1)²`. Reframe de la ruta A: probar que
  la Jacobi intrínseca **acotada** → Dirichlet `(k+1)²` asintóticamente.
- **Falsador DH:** ratios `[1, 0.67, 0.62, 0.54, …]` (basura), `αₙ` con signo cambiado. Falla limpio.

## N2 — Zeta espectral / traza de calor (`E80_spectral_zeta.py`)

**RESULTADO POSITIVO (robustez) + NEGATIVO (sin ley de tasa limpia).** `μ_k = eps_k/eps_0`:

| λ | μ (target 1,4,9,16,25) | ladder_err | Z(1) err | Θ(0.7) err |
|---|---|---|---|---|
| 7  | 1, 4.07, 9.05, 16.40, 25.40 | 0.025 | 0.0048 | 0.0053 |
| 9  | 1, 4.00, 9.03, 16.06, 25.22 | 0.009 | 0.0005 | 0.0001 |
| 11 | 1, 3.90, 9.02, 15.65, 25.14 | 0.024 | 0.0048 | 0.0075 |
| 13 | 1, 4.04, 9.01, 16.20, 25.12 | 0.013 | 0.0025 | 0.0031 |
| 15 | 1, 3.93, 9.01, 15.76, 25.08 | 0.017 | 0.0033 | 0.0051 |

- **Las trazas reproducen los invariantes Dirichlet a <0.5%** (agregado), mucho más robusto que
  cualquier eigenvalor individual `e^{−cL}`. Confirma 2.3.F-Loc a nivel de invariante espectral.
- **Falsador DH CATASTRÓFICO** (instrumento limpio): `ladder_err=0.98`, `Z(s) err = 4.3, 10.8, 19.9`.
- **PERO la dependencia en λ es OSCILATORIA, no monótona**: `μ_1` rebota alrededor de 4
  (4.07→4.00→3.90→4.04→3.93), `μ_3` alrededor de 16. Las tasas de Richardson salen **inconsistentes**
  entre observables (ladder_err `p=+0.80` converge, pero `Z(s=2) p=−2.85`). ⟹ **NO hay ley de
  potencia limpia**: el residuo respecto de `(k+1)²` **fluctúa aritméticamente en λ** (eco de la
  oscilación de primos en la banda `L=2logλ`). La escalera es exacta **en media**; la convergencia es
  Cesàro/promediada, no puntual-suave.

### Envelope a λ alto (`E82_envelope.py`, λ hasta 21)

| λ | L | μ_1 | μ_3 | \|dev μ1\| | \|dev μ3\| | ladder_err |
|---|---|---|---|---|---|---|
| 7  | 3.89 | 4.070 | 16.40 | 0.070 | 0.404 | 0.025 |
| 9  | 4.39 | 3.998 | 16.06 | 0.002 | 0.056 | 0.009 |
| 11 | 4.80 | 3.904 | 15.65 | 0.096 | 0.346 | 0.024 |
| 13 | 5.13 | 4.041 | 16.20 | 0.041 | 0.202 | 0.013 |
| 15 | 5.42 | 3.934 | 15.76 | 0.066 | 0.240 | 0.017 |
| 17 | 5.67 | 4.034 | 16.16 | 0.034 | 0.160 | 0.010 |
| 19 | 5.89 | 3.978 | 15.93 | 0.022 | 0.071 | 0.006 |
| 21 | 6.09 | 3.928 | 15.73 | 0.072 | 0.271 | 0.018 |

**El envelope NO decae limpio:** la desviación de `(k+1)²` **oscila en una banda ~estable** (ladder_err
rebota 0.025, 0.009, 0.024, 0.013, 0.017, 0.010, 0.006, **0.018**). Los ajustes "decae" (`p≈1.45,
0.85`) están dominados por los λ bajos y un λ=19 afortunado; λ=21 vuelve a 0.018. Conclusión:
**escalera exacta EN MEDIA + fluctuación aritmética irreducible ~1–2% que no se desvanece a λ
alcanzable.** Eso es el obstáculo, preciso.

## N3 — Portadora `θ(y)` vía Liouville–Green + tasa 1/L (`E81_liouville_green.py`)

**RESULTADO NEGATIVO (sin ley derivable).** Dos vías: (a) `cosθ=(f_1/u_0)/2` de modos medidos;
(b) Liouville–Green `θ=∫√(w/C)dy` con `C` medido.

- Residuo de afinidad **pequeño** (modos 0.5–1%, LG ~2.3–2.6%) pero **plano**: la tasa LG en `1/L`
  sale `≈ 0` (no converge limpio); la de modos es ruidosa (`p≈0.55` dominada por un punto).
- **Falsador DH:** modos 17.4%, LG 6.0% (mucho peor). Falla.
- Veredicto: consistente con la oscilación de N2 — la afinidad es buena (~2%) pero su tendencia con λ
  está dominada por la fluctuación aritmética, no por una ley `1/L^p` extraíble.

## Veredicto consolidado R9

**Las tres herramientas nuevas SON un avance real, pero NO cierran 2.3.F:**

1. **Ganancia firme (N1):** Lanczos da una **tridiagonalización intrínseca ESTABLE** que alcanza la
   escalera `(k+1)²` en el residuo `e^{−cL}` (donde E76 fallaba) — herramienta nueva utilizable.
2. **Insight estructural nuevo (N1):** en el marco intrínseco el operador es una **Jacobi de
   coeficientes acotados O(1)** (la balanza de Weil borra la escala `2πλ²` de la prolata desnuda).
   Reframe limpio de la ruta A: "Jacobi acotada intrínseca → Dirichlet `(k+1)²`".
3. **Triple confirmación robusta de 2.3.F-Loc** (Lanczos, trazas, portadora) + **falsación DH limpia
   en los tres** (instrumento fiel).
4. **Obstrucción precisada (N2/N3):** el residuo de `(k+1)²` **oscila aritméticamente en λ** (no hay
   ley de potencia `1/L^p`); la convergencia a la escalera es **en media**, no puntual. Por eso ningún
   ajuste de tasa cierra: el contenido restante es una **asintótica promediada** (Cesàro) de la
   deformación prolato/Sonin = exactamente la maquinaria de Connes/Consani.

**Estado de 2.3.F sin cambios en el TEOREMA, pero con mejor mapa:** sigue REDUCIDO a 2.3.F-Loc; ahora
con (i) una ruta computacional estable (Lanczos), (ii) un enunciado más nítido del crux (Jacobi
acotada → Dirichlet, en media sobre λ), y (iii) la confirmación de que la obstrucción es la
**fluctuación aritmética** del residuo, no un atajo faltante.
