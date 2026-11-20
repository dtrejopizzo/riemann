# Ronda 029-A — Peso atenuado `w_n = v_n cos(kπ log n/(4T))` con base de elementos finitos hp

Etiqueta global: **NUMÉRICO**. Continúa 212-27 (ROUND_027_A/B/C). No se tocó ningún paper ni el índice.

## 1. Método
- Forma `a^w_T(F) = C_0‖F‖² + ∫_0^∞(c_F(0) − c_F(u))K(u)du − Σ w_n c_F(log n)` sobre `P_T`
  (P47 eq:Aform, lem:K; cola `G(s) = ∫_s^∞K = log coth(s/4) + π − 2 arctan e^{s/2}`, que en `s = 2T`
  da la fórmula de thm:S(iii)). Sólo entran `n` con `Λ(n) > 0`, `log n < 2T`.
- Base: Legendre ortonormal de grado `p − 1` por elemento, discontinua (conforme: la forma es finita
  para funciones a trozos, pues `c_F(0) − c_F(u) = O(u)`), malla con interior uniforme de paso `≤ H`
  y capas geométricas de razón `σ` hacia `±T` hasta `h_min = c·e^{−2T}`.
- Parte arquimediana por pares de elementos `(e,f)`: `∫(δ − C_ef(u))K(u)du` partido en los quiebres
  `{a_f − b_e, a_f − a_e, b_f − b_e, b_f − a_e}`; en cada trozo el integrando es analítico (cerca de
  `u = 0` el factor `I − C_ee(u)` se anula linealmente); Gauss en `u` (`2p + 16` nodos) y Gauss exacto
  en `t`. Diagonal: `∫_0^{h_e}(I − C_ee)K + G(h_e)I`. Aritmética: `C(log n)` exacta. `P_T` por SVD.
- Niveles `L = (H, p, σ, c)`: 1 `(0.5,6,.3,.3)`, 2 `(.35,8,.25,.1)`, 3 `(.25,10,.2,.03)`, 4 `(.2,12,.18,.01)`,
  5 `(.15,14,.15,3e−3)`, 6 `(.12,16,.15,1e−3)`, 7 `(.1,18,.15,3e−4)`. Galerkin ⇒ cotas SUPERIORES.
- Scripts y salidas: `free_weight_scripts/hp.py`, `run_hp.py`, `val_hp.py`, `qcheck.py`, `indep.py`,
  `profile.py`, `scanH.py`; salidas y vectores en `free_weight_scripts/hp_out/`.

## 2. Validación
- `λ_A(½log3)`: `9.66e−4, 9.488e−4, 9.479e−4` (p = 6, 8, 10). `λ_A(log 2)`: `3.4e−6, 1.04e−7, 9.90e−8`.
- `k = 1`, comparación con valores convergidos previos: `T = 0.8`: `+0.012689`; `1.2`: `+0.002291`;
  `1.6`: `+3.96e−4`; `2.0`: `+9.84e−5` (L4); `2.4`: `+2.562e−5` (L4–L7 iguales a 4 cifras). Coinciden.
- Control del peso verdadero `v` (paso 5): `|λ_min| ≤ 1.2e−13` en todos los `T` (0.8–3.6) y niveles;
  crece con `N` como redondeo. No aparece ningún valor apreciablemente negativo.
- Cuadratura: `T = 3.6`, L1, `u`-nodos 28 → 60: `max|ΔA| = 1.9e−11`, `λ_min` igual a 12 cifras.
- Evaluación independiente del minimizador de `T = 3.6` (L1, `k = 1`) con `c_F(u)` directo y
  cuadratura adaptativa en `u`: `a = −2.440775e−4`, idéntico; `‖F‖ = 1`, restricciones `≈ 1e−14`.
  Igual en `T = 3.35` (L4): `a = −1.137518e−5`, idéntico al autovalor guardado.
- Código independiente (Legendre global, `taper.py`) en `T = 3.6`, `k = 1`: `−2.93e−4` (N=80),
  `−4.72e−4` (N=120). Confirma el signo.

## 3. Hallazgo sobre la resolución
El diagnóstico previo («la base no resuelve el borde `e^{−2T}`») NO es lo que limita: con `H` fijo,
refinar sólo el borde (`c` 1e−2 → 1e−4) no cambia el valor; refinar el INTERIOR sí
(`T = 3.2`, `p = 10`: `H = .25, .12, .06, .03` → `1.88e−5, 6.12e−6, 2.138e−6, 2.053e−6`).
Los minimizadores positivos son paquetes de alta frecuencia que llenan la ventana:
`T = 2.8`: par, `ω ≈ 74`, 71 % de la masa a distancia `> 1.5` del borde; `T = 3.2`: impar, `ω ≈ 126`.
Una base global de 240 cosenos no alcanza esas frecuencias con el soporte completo.

## 4. Tablas (λ_min, `‖F‖ = 1`)
`k = 1` por nivel:

| T | L1 | L2 | L3 | L4 | L5 | L6 | L7 | estado |
|---|---|---|---|---|---|---|---|---|
| 2.4 | 4.68e−4 | 1.07e−4 | 4.34e−5 | 2.564e−5 | 2.562e−5 | 2.562e−5 | 2.562e−5 | POSITIVO convergido |
| 2.8 | 2.79e−4 | 6.05e−5 | 2.78e−5 | 1.15e−5 | 6.955e−6 | 6.932e−6 | 6.927e−6 | POSITIVO convergido (~0.1 %) |
| 3.2 | 1.89e−4 | 4.19e−5 | 1.88e−5 | 7.70e−6 | 3.71e−6 | 2.080e−6 | 2.060e−6 | POSITIVO convergido (~1 %; H=.03: 2.053e−6) |
| 3.3 | — | — | 1.73e−5 | 8.06e−6 | 3.33e−6 | 8.11e−7 | 4.10e−7 | NO DECIDIDO (baja ×2 por nivel) |
| 3.35 | — | — | 1.36e−5 | −1.14e−5 | −3.33e−5 | −4.06e−5 | — | NEGATIVO |
| 3.4 | 1.87e−4 | 3.66e−5 | −4.72e−5 | −9.96e−5 | −1.287e−4 | −1.403e−4 | — | NEGATIVO |
| 3.6 | −2.44e−4 | −5.08e−4 | −7.63e−4 | −8.78e−4 | −9.73e−4 | −1.006e−3 | — | NEGATIVO |

Como son cotas superiores, cada valor negativo ya decide «cruza»; la sucesión sólo afina la magnitud.
Extrapolación (`T = 3.6`, diferencias 1.15e−4, 9.5e−5, 3.3e−5): `λ ≈ −1.03e−3 ± 3e−5`.

`k = 0.9, 1.1` (mejor nivel; «c» = convergido, «nc» = no convergido):

| T | k = 0.9 | k = 1.0 | k = 1.1 |
|---|---|---|---|
| 2.4 | +2.076e−5 c | +2.562e−5 c | +3.099e−5 c |
| 2.8 | +5.623e−6 c | +6.927e−6 c | +8.357e−6 c |
| 3.2 | +1.676e−6 c (~1 %) | +2.060e−6 c | −5.68e−4 NEG |
| 3.3 | +1.30e−6 nc | +4.1e−7 nc | −1.08e−3 NEG |
| 3.35 | +1.29e−6 nc | −4.06e−5 NEG | −1.49e−3 NEG |
| 3.4 | +1.23e−6 nc | −1.40e−4 NEG | −2.09e−3 NEG |
| 3.6 | −4.82e−3 NEG | −1.006e−3 NEG | −4.81e−3 NEG |

## 5. Veredicto por T (pregunta: `k = 1`)
- `T = 2.4`: POSITIVO convergido, `+2.562e−5`.
- `T = 2.8`: POSITIVO convergido, `+6.93e−6` (el `+7.0e−6` de 240 cosenos estaba cerca;
  el `+2.8e−5` de la base 130 no).
- `T = 3.2`: POSITIVO convergido, `+2.05e−6 … +2.06e−6`.
- `T = 3.3`: NO DECIDIDO (`+4.1e−7` en L7, sin convergencia).
- `T = 3.35, 3.4, 3.6`: NEGATIVO (decidido por cota superior; verificado con evaluador y código
  independientes en 3.6). **La atenuación `k = 1` cruza cero entre `T = 3.2` y `T = 3.35`**,
  probablemente cerca de `T ≈ 3.3`.
- Ley de caída en el tramo positivo: `2.4 → 2.8 → 3.2` da tasas locales `e^{−3.27T}`, `e^{−3.04T}`
  (consistente con `≈ e^{−3.4T}` de 212-27 para `T ≤ 2.4`); el cruce NO sigue esa ley: lo produce
  otra rama de autovectores que baja bruscamente (abajo).

## 6. Vector minimizante negativo (paso 3)
- `T = 3.6`, L6, `k = 1`: `λ = −1.006e−3`; `Arch = 0.12713`, suma atenuada `= 0.12814`
  (`‖F‖ = 1`). PAR (masa impar `1.3e−5`); 35 % de la masa a distancia `0.01–0.1` del borde, 20 % en
  `0.1–0.5`, 34 % en `0.5–1.5`, 12 % más adentro; frecuencia interior dominante `ω ≈ 0.95` (más
  componentes en `ω ≈ 14–25`). Capa de borde de ancho `≍ 0.01–0.1`, no `e^{−2T} ≈ 7e−4`.
- `T = 3.35`, L6: `λ = −4.06e−5`, `Arch = 1.29781`, suma `= 1.29786`; par, 40 % en `0.01–0.1` del
  borde, `ω ≈ 31–42`. Mismo tipo (par, capa de borde + baja frecuencia).
- `T = 3.2`, `k = 1.1` (negativo): par, 43 % en `0.01–0.1` del borde, `ω ≈ 1.1`. La misma rama aparece
  antes para `k > 1`.
- Perfiles guardados: `hp_out/vec_T*_L*_k*.npz` (coeficientes, malla, `λ`, Arch, suma) y
  `*_profile.txt` (`t`, `F(t)`).

## 7. Ventana de `k` (paso 4)
Hasta `T = 2.8` los tres `k` son positivos y `λ` crece con `k` (rama de alta frecuencia). Desde
`T = 3.2` la rama par de borde vuelve negativo primero a `k = 1.1`, luego (`T ≈ 3.3`) a `k = 1`; en
`3.4` sólo `k = 0.9` sigue positivo (no convergido); en `3.6` los tres son negativos de orden `1e−3`.
`k = 1` no es punto aislado en `T ≤ 3.2`; el intervalo admisible se corre hacia `k < 1` y se
estrecha; en `T = 3.6` no contiene a `0.9, 1, 1.1` (no se probaron otros `k` allí).

## 8. Límites
- Los NEGATIVOS son cotas superiores con verificación independiente; los POSITIVOS «convergidos»
  lo son empíricamente (estabilidad entre niveles y entre refinamiento en `H` y en `p`), no hay
  cota inferior rigurosa ni aritmética de intervalos.
- La frecuencia del minimizador positivo crece con `T` (`ω ≈ 74 → 126`); a `T` mayor hace falta
  `H` menor. `T = 3.3` y `k = 0.9` en `3.3–3.4` quedan sin convergencia.
- No se exploró `k` fuera de `{0.9, 1, 1.1}` ni otras formas de atenuación.
