# Ronda 027-A — Verificación numérica hostil del peso atenuado `v_n cos(ω log n)`

Todo lo de este memo es NUMÉRICO salvo donde se indica. Scripts y salidas: carpeta temporal
`pbp_verify/` (trig.py, sweep.py, leg.py, hi.py; s1.log, s2.log, hi.log).

## 1. Auditoría de la implementación original (forms.py)

Cotejada con el Paper 47 (eq:symbol, eq:form, lem:K, thm:S(iii), thm:A eq:Aform):
- `K(u) = 2e^{-u/2}/(1−e^{-2u}) = 2e^{3u/2}/(e^{2u}−1)`: correcto. `C_0 = ψ(1/4) − log π`: correcto.
- Lévy sobre `[0,2T]` más cola `c_F(0)∫_{2T}^∞K = log coth(T/2) + π − 2 arctan e^T`: coincide con thm:S(iii).
- `c_F(u) = ∫F(t)F(t+u)dt` simetrizada; contactos `log n < 2T`; `v_n = 2Λ(n)/√n`: correcto.
- `P_T` = núcleo de `A, B` con `e^{±t/2}`: correcto. Cuadratura de Gauss en `u`: el integrando
  `K(u)(c(0)−c(u))` es polinomio por función analítica, sin singularidad; adecuada.
- Atenuación de taper2: `cos(kπ x/2)`, `x = log n/2T`, es `cos(ω log n)` con `ω = kπ/(4T)`: correcto.
No encontré error que fabrique el efecto.

## 2. Reimplementación independiente

Base de cosenos de Neumann `cos(kπ(t+T)/2T)` (no polinómica), autocorrelaciones y momentos de Tate en
forma cerrada, cuadratura tanh-sinh en `u`, extrapolación de Richardson (convergencia `O(N^{-2})`).

| T | N=40 | 80 | 160 | 320 | Richardson | Paper 47 |
|---|---|---|---|---|---|---|
| ½log3 | 1.0028e-3 | 9.5688e-4 | 9.4769e-4 | 9.4557e-4 | 9.449e-4 | 9.448e-4 |
| log 2 | 1.497e-7 | 1.096e-7 | 1.006e-7 | 9.878e-8 | 9.82e-8 | 9.83e-8 |

Advertencia técnica: con N = 320 y T ≥ 2 el paso tanh-sinh h = 0.01 no resuelve la oscilación de
`c_ij(u)` y produce `λ_A ≈ −0.07 … −0.27` espurios (artefacto: con h = 0.003, N = 240, `λ_A ≈ −1e−12`,
nivel de redondeo). Esas filas se descartan.

## 3. Valores k = 1.0 y k = 0.6 (base trig; entre paréntesis Legendre de forms.py)

Margen `μ(T) = λ_min(a^{w(ω)}_T)`, ω = kπ/(4T):

| T | k=1.0, N=80 / 160 / 240–320 | estado | k=0.6 (N mayor) | cociente 0.6/1.0 |
|---|---|---|---|---|
| 0.8 | 0.01269 / 0.01269 / 0.01269 | convergido | 0.004495 | 0.354 |
| 1.2 | 0.002296 / 0.002292 / 0.002291 | convergido | 0.000820 | 0.358 |
| 1.6 | 3.967e-4 / 3.960e-4 | convergido | 1.427e-4 | 0.360 |
| 2.0 | 9.96e-5 / 9.86e-5 / 9.84e-5 | convergido | 3.557e-5 | 0.361 |
| 2.4 | 4.00e-5 / 2.565e-5 / 2.563e-5 (Leg 60/100/140: 1.55e-4, 4.8e-5, 2.9e-5) | convergido trig, Leg no | 9.24e-6 | 0.360 |
| 2.8 | 2.99e-5 / 9.6e-6 / 7.0e-6 (Leg: 1.2e-4, 4.9e-5, 2.2e-5) | NO convergido, decreciente | **−0.00132** | — |
| 3.2 | 2.42e-5 / 6.2e-6 / 3.2e-6 | NO convergido, decreciente | **−0.0137** | — |

- Los cuatro valores del hallazgo (T = 0.8…2.0, k = 1.0 y k = 0.6) se reproducen en otra base a 3–4 cifras.
- Ley de caída para k = 1 (T ≤ 2.4, convergidos): cocientes por ΔT = 0.4 de 5.5, 5.8, 4.0, 3.8. Exponencial
  simple que se frena: `μ ≈ e^{−3.4T}` al final, es decir `≈ N^{−1.7}` con N = e^{2T}. No es doble exponencial.
- **k = 0.6 cruza cero entre T = 2.4 y T = 2.8** (negativo y convergido en las dos bases: trig −0.00127/−0.00132,
  Legendre −0.00102/−0.00114). La ley `μ ∝ k²` vale hasta T = 2.4 (cociente 0.36 = 0.6²) y se rompe después.
- k = 1.0 en T ≥ 2.8: positivo en toda base probada, pero el margen baja al subir N sin estabilizarse
  (T = 3.2: 2.4e-5 → 6.2e-6 → 3.2e-6). **No se puede afirmar positividad para T ≥ 2.8**: es compatible con
  un límite pequeño positivo y con un límite ≤ 0. Queda OPEN y NUMÉRICO no convergido.

## 4. ω fijo

| T | ω=0.2 | ω=0.4 |
|---|---|---|
| 0.8 | 5.29e-4 | 2.08e-3 |
| 1.2 | 2.15e-4 | 8.51e-4 |
| 1.6 | 6.59e-5 | 2.63e-4 |
| 2.4 | 9.58e-6 (conv.) | 3.82e-5 (conv.) |
| 2.8 | 4.9e-6 → 3.6e-6 (no conv.) | **−0.0119** (conv.) |
| 3.2 | 4.2e-6 → 2.1e-6 (no conv.) | **−0.12** |

ω = 0.4 cruza cero entre 2.4 y 2.8; coincide con el umbral `ω·2T > π/2` en el que pesos con `log n > π/(2ω)`
se vuelven negativos (n > 51), pero k = 0.6 cruza con todos los pesos positivos, así que el signo del peso no
es la única causa. ω = 0.2: margen positivo que decae y no converge en N para T ≥ 2.8.
Conclusión: con ω fijo **no** se mantiene el margen; la premisa «margen ∝ ω² uniforme en T» es falsa.

## 5. Predicción de primer orden `μ ≈ λ_A + (ω²/2) Q(F_*)`

- T = 0.5 (λ_A = 0.01187, autovalor aislado): ω = 0.2 medido 0.013654, predicho 0.013655; ω = 0.4: 0.01893
  frente a 0.01900. **Correcta** donde λ_A está separado.
- T = 0.8: predicción ≈ 2× el valor medido (ω=0.2: 1.005e-3 vs 5.29e-4). T ≥ 1.2: predicción 50× a 10⁴× por
  encima y `Q(F_*)` no converge en N (T = 1.6: 3.97 → 7.0). Motivo: `a^v_T` tiene un subespacio casi nulo de
  dimensión creciente (`λ_A` está a nivel de redondeo, 1e−13), el minimizador `F_*` no está determinado y la
  perturbación es degenerada: el margen lo fija `min` de Q sobre ese subespacio, no Q en un vector. La fórmula
  (iii) del hallazgo, evaluada en un minimizador, no es informativa para T ≥ 0.8.

## 6. Controles (k = 1.0; entre paréntesis sin atenuar)

| T | sin n=2 | 2v | Beurling (2 → 2.2) |
|---|---|---|---|
| 0.8 | −0.403 (−0.568) | −0.293 | −0.210 (−0.380) |
| 1.2 | −0.642 (−0.735) | −0.942 | −0.550 (−1.103) |
| 1.6 | −0.775 | −1.67 | −1.09 |
| 2.4 | −0.873 | −1.98 … −2.8 | −1.92 |
| 3.2 | −0.92 | −2.46 | −2.35 |

Los tres controles dan forma atenuada **negativa** y de orden 1 en todo T ≥ 0.8, convergidos. (En T = 0.5
sólo hay un contacto y los controles son triviales.) La atenuación no crea positividad por sí sola: el efecto
depende de los valores exactos de v. Esto es coherente con la exigencia de no linealidad en Λ.

## 7. Balance

- PROVED (elemental, ya en el hallazgo): (i) modulación y (ii) monotonía de K_T bajo extensión por cero.
- NUMÉRICO convergido: reproducción de λ_A(½log3), λ_A(log 2) y de los valores k = 1, 0.6 hasta T = 2.4;
  controles negativos; k = 0.6 y ω = 0.4 negativos en T = 2.8, 3.2.
- NUMÉRICO no convergido: k = 1 y ω = 0.2 en T ≥ 2.8 (positivos en las bases probadas, a la baja con N).
- Consecuencia para el uso (ii): una sucesión `ω_j → 0` con margen positivo exige `ω_j ≳ π/(4T_j)` o más
  (k ≥ 1 con k = 0.6 ya fallando); qué ocurre en k = 1 para T grande es exactamente lo no resuelto. OPEN.
- Lo que no se abrió: precisión extendida (mpmath) — no fue necesaria para los valores reproducidos y no
  resolvería la no convergencia en N, que es de base, no de redondeo; T = 3.2 con N > 240.
