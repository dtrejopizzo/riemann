# Ronda 026 B — (PBP_T) como problema extremal exacto; argumento de Kreĭn y densidad; puerta de cuatro puntos

Objeto: la forma `a^w_T` sobre `P_T` (Paper 47, `04-papers/47-row-d-dual-certificates/main.tex`). Sin derivaciones
largas. Abiertos: R160_M2_R1 completo; G2_B9_R3 §3; P47 `eq:m`, `eq:Aform`, `eq:Kprim`, `prop:finite`, `lem:degen`,
`rem:resweights`; R155_033 §0, §2.1–2.3; índice, entrada 212-25; ROUND_025_A (grep). No abiertos: R155_023/024/027
(umbrales y Theorem N′, sólo por su resumen en README de la fase 155), R155_049, ROUND_025_B, G2_B6_R2.

## 1. Formulación exacta (ya hecha en el corpus)

Literal del paper (`eq:m`, `eq:Aform`, `eq:Kprim`): para `F` real, `‖F‖=1`, `c=c_F`,
```
𝔞^{(w)}_T(F) = C_0·c(0) + 𝔈(c) − Σ_{n∈N_T} w_n c(log n),   𝔈(c) = ∫_0^∞ (c(0) − c(u)) K(u) du ≥ 0,
C_0 = ψ(1/4) − log π = −5.3721834…,   K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)),
K(u) = 1/u + O(1) (u↓0),   K(u) = 2e^{−u/2}(1+O(e^{−u})) (u→∞).
```
Términos de polo: en la forma completa se suma `2A(F)B(F) = 2∫c(u)cosh(u/2)du` (R160_M2_R1 Rem. 2.5). En `P_T`
desaparecen y la primitividad pasa a dos restricciones lineales sobre `c` (`eq:Kprim`):
`∫ c(u) cosh(u/2) du = 0`, `∫ c(u) u sinh(u/2) du = 0`. Como `c` se anula en `|u| ≥ 2T`,
`𝔈(c) = ∫_0^{2T} (1 − c)K + ∫_{2T}^∞ K`, y el último sumando es `≈ 4e^{−T}`.

Problema extremal (relajado a estados mixtos, convexo):
```
Z^prim_T = ínf { C_0 + 𝔈(Φ) :  Φ par, definida positiva, Φ(0)=1, sop Φ ⊂ [−2T,2T],
                 ∫Φ cosh(u/2) = ∫Φ u sinh(u/2) = 0,  Φ(log n) = 0  ∀ 2 ≤ n < e^{2T} } ;
(PBP_T):  Z^prim_T ≥ 0  (equivalentemente K_T = 𝒱^prim_T ≠ ∅).
```
**Ya hecho (CITED, PROVED allí):** es literalmente R160_M2_R1 D4–D5, Thm 4.1 (dualidad fuerte; el peso óptimo es el
multiplicador de Lagrange de las restricciones `Φ(log n)=0`), Thm 4.3(a) (`𝒱^prim_T ≠ ∅ ⟺ Z^prim_T ≥ 0`), Rem. 4.4
(versión `T→∞`) y §7.1. Sin las restricciones de contacto es el programa `(P_∞)` de R155_033 §2.1–2.2. Nada nuevo en (1).

## 2. El argumento de Kreĭn más densidad de `log ℕ`: qué da

Herramienta (CITED, estándar): para `Φ` definida positiva con `Φ(0)=1` existe un espacio de Hilbert con vectores
unitarios `ξ_u`, `⟨ξ_u, ξ_{u′}⟩ = Φ(u − u′)`. Con `ω := 1 − Φ ∈ [0,2]` y `d(h) := ‖ξ_h − ξ_0‖ = √(2ω(h))`:
(K1) `|Φ(u) − Φ(u′)| ≤ d(u − u′)` (Kreĭn); (K2) `d` es subaditiva, luego `ω(s) + ω(h−s) ≥ ω(h)/2` para `0 ≤ s ≤ h`.

Consecuencias (PROVED, una línea cada una; `K` decreciente):
- **Campo lejano.** Si `g(u) := dist(u, {log n: n≥2})`, entonces `|Φ(u)| ≤ D(g(u))`, `D(r) := sup_{|h|≤r} d(h)`, y
  `ω(u) ≥ 1 − D(g(u))`. En `[log N, ∞)` es `g ≤ ½ log(1+1/N)`, así que
  `∫_{log N}^∞ ωK ≥ (1 − D_N) ∫_{log N}^∞ K`, `D_N := D(½log(1+1/N))`.
- **Cerca de 0.** Por (K2), `∫_0^h ωK ≥ (ω(h)/2) ∫_{h/2}^h K ≈ (log 2/2) ω(h)`; con `ω(h) = D²/2` en el punto donde se
  alcanza `D_N`, el aporte es `≥ (log 2/4) D_N² ≈ 0.173 D_N²` (≤ 0.69).
- **Primer contacto.** `ω(log 2) = 1` y (K2) dan `∫_0^{log 2} ωK ≥ ½∫_{½log2}^{log 2} K = 0.4266`.

Cota resultante (PROVED como desigualdad, salvo el solapamiento de las dos cotas sobre `[0, log 2]`, que sólo puede
bajarla): `𝔈(Φ) ≥ mín_{D∈[0,2]} [ (1−D)_+ ∫_{log 2}^∞ K + máx(0.4266, 0.173 D²) ]`. Valores (NUMÉRICO, mpmath):
`∫_{log 2}^∞ K = 2.9937`, `∫_{log 7}^∞ K = 1.5181` (la cifra 1.5 de H1), `∫_{log 3}^∞ K = 2.3642`.
**Techo del método: `𝔈 ≥ ~3.0–3.4` (en el mejor caso `D=0`), contra `−C_0 = 5.372`. Faltan `≈ 2.0` (al menos 1.7 aun
sumando las dos cotas sin solapamiento, ≤ 3.7).** NO alcanza; no se fuerza.

De dónde tendría que salir lo que falta (ARGUED). La positividad arquimediana en ventanas cortas (`T*_{∞,P} ≈ 0.58–0.60`)
viene de la singularidad `K ~ 1/u`: un `Φ` que cae de 1 a 0 en escala `h` paga `≈ log(1/h)` por *todas* las escalas
diádicas entre `h` y 1. (K2) sólo cobra una escala (un factor `log 2`), no la suma diádica. Lo que falta es un
**principio de incertidumbre multiescala para funciones definidas positivas que se anulan en `log ℕ`**: una cota
inferior de `∫_0^1 ωK` que crezca como `log(1/g)` cuando las anulaciones fuerzan variación a escala `g ≍ e^{−u}`. Es la
pared «del borde» de R155_033 §0 (`thm:O`, presente ya con `v=0`), ahora en el lado primal. Sin ella el argumento sólo
cobra la cola de `K`, que es `O(1)` y acotada por `∫_{log 2}^∞ K < 3`.

Primitividad. En el argumento de (2) **no entra**: (K1)–(K2) valen para toda `Φ` definida positiva. Su único papel
posible es obligar a `Φ` a tener masa negativa ponderada por `cosh(u/2)` lejos de 0, lo que choca con `|Φ| ≤ D(g)`. Pero
el peso llega a `e^{T}`, así que basta amplitud `≍ e^{−T}` lejos, que (K1) permite con `D ≍ e^{−T}`: aporte asintótico
nulo por esta vía (ARGUED, no cuantificado con mezclas). Cuantificarlo: OPEN.

## 3. Antecedentes y qué de (1)–(2) ya está

- R160_M2_R1: (1) completo (D4–D5, Thm 4.1–4.5, Rem. 4.4, §7.1–7.2); §6 H1 es la versión heurística de (2) con
  `|c′| ≤ Ω` en vez de (K1), y ya concluye «≈1.5, not enough against 5.37 by crude bounds». (2) es H1 rigorizado y
  apenas mejorado (de 1.5 a ≤ 3.4 al usar todo `[log 2, ∞)` y (K2)); el déficit sigue.
- R155_033 §2.2: la misma cuenta en el lado dual («`τ=0` cap»): un certificado necesita `∫_{2T}^∞(1−w)K ≥ 𝔈(c_{F⋆})`,
  y la cola de `K` sola no basta (factores 2.3–2.6). Es la versión dual del techo de (2).
- R155_033 §0, Thm AL (sólo `(D_∞)`; corregida por R155_049 a `Θ(1/M)` en el programa completo): la pared es el borde
  de la ventana, no el retículo. Coincide con el diagnóstico de §2.
- P47 `lem:degen`, `rem:resweights`: definen `μ_T` cóncava y el caso degenerado; `prop:finite`(ii)–(iii): `𝒱_T`
  cerrado convexo, `0 ∉ 𝒱_T` para `T ≥ 0.60`.
- G2_B9_R3 §3 (Thm N, R′): rigidez sólo para `w − v ∈ 𝒯_meas`; para pesos no temperados, hueco registrado en 212-25.
- Grep «Kreĭn inequality / 1 − Re»: no hay uso de (K1)–(K2) sobre `Z^prim_T` en el corpus (las coincidencias de 211
  ROUND_012_B/016_A/024_A, 212 ROUND_018_A y R162_1301 son otros objetos: espacios de Kreĭn/Pontryagin, función Q).
  Una búsqueda sin coincidencias no prueba novedad conceptual: (K1) es exactamente el control de H1.

## 4. Puerta de cuatro puntos

1. **Antecedente más cercano:** R160_M2_R1 §6 H1 y §7.1 (más D5, Thm 4.1/4.3); en el lado dual R155_033 §2.2.
2. **Qué es nuevo:** sustituir la hipótesis de banda `|c′| ≤ Ω` de H1 por (K1)–(K2), válidas para toda `Φ` de la clase
   mixta, y el cálculo exacto del techo (≈ 3.0–3.4 frente a 5.372). Es una precisión de una heurística, no un objeto.
3. **¿Evita la dificultad del antecedente?** No. La dificultad de H1 era que la cola de `K` sólo da `O(1)`; (K1)–(K2)
   cobran la misma cola y una sola escala cerca de 0. El déficit `≈ 2` está en la suma diádica de la singularidad,
   que ninguna desigualdad de tres puntos ve.
4. **Conexión con el objetivo global:** (PBP_T) ∀T ⟹ `K_T ≠ ∅` ∀T ⟹ (Tychonoff, 212-25) un `w` con `a^w_T ≥ 0` ∀T;
   pasar de ese `w` al peso verdadero exige rigidez para pesos con `|w_n| ≲ log n`: **CONDITIONAL** (212-25).
   (PBP_T) ∀T por sí sola **sí sería un teorema nuevo respecto del corpus** (OPEN en R160 §7.1 para `T > log 2` puro y
   `T > 0.8` relajado; ningún falsificador ni prueba de imposibilidad): diría que *ningún estado primitivo cuya
   autocorrelación se anula en todo `log n` tiene energía arquimediana negativa*, con todo el contenido en las
   posiciones `log n` y ninguno en valores de pesos. No da el signo del objetivo sin la rigidez.

Controles. (PBP) no tiene peso; el control es el retículo. En (2) el retículo entra **sólo** en dos datos: la función
de huecos `g(u) ≤ ½log(1+1/⌊e^u⌋)` y la posición del primer contacto `log 2`. Ningún paso usa que el conjunto sea
exactamente `log ℕ`: para los enteros coprimos con `p` los huecos crecen a lo sumo por un factor `p/(p−1)` y el
primer contacto pasa a `log 3` (`p=2`), con techo `∫_{log 3}^∞ K = 2.36`, menor; un sistema de Beurling con el mismo
perfil de huecos da la misma cota. El argumento varía continuamente y no separa `log ℕ` de sus vecinos (si (PBP)
fallara para alguno, este método no lo vería). El único lugar donde la estructura entera podría entrar y no se usa:
en el espacio GNS, `ξ_{log m} ⊥ ξ_{log n}` cuando `n | m` (pues `Φ(log(m/n)) = 0`); pero esa relación de divisibilidad
la comparte todo sistema multiplicativamente cerrado (Beurling incluido), así que tampoco separa. Registrado, no
explotado.

## Veredicto

**NO PASA (repetición, y sin mecanismo).** (1) está hecho (R160_M2_R1 D4–D5, Thm 4.1/4.3). (2) es H1 de R160 §6 con
(K1)–(K2) en lugar de banda limitada: techo PROVED-como-cota `𝔈 ≳ 3.0–3.4 < 5.372`, déficit `≈ 2`; la primitividad no
entra en el argumento (aporte ARGUED nulo asintóticamente). Lo que falta es una cota multiescala de la singularidad
`K ~ 1/u` forzada por las anulaciones (pared del borde de R155_033), no la cola de `K`. (PBP_T) ∀T sigue OPEN y sería
nuevo; su conexión con el objetivo es CONDITIONAL en la rigidez para pesos no temperados (212-25). Reapertura: un
principio de incertidumbre para `Φ` definida positiva anulada en `log ℕ` que cobre `≳ log(1/g)` por escalas.
