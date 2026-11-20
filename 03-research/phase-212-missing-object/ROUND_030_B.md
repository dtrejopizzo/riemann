# Ronda 030 B — Cadenas de divisores, masa espectral en baja frecuencia y primitividad en (PBP_T)

Objeto: `𝔈(Φ) = C_0 + ∫_0^∞ (1 − Φ)K` sobre `Φ` definida positiva, `Φ(0) = 1`, `sop Φ ⊂ [−2T, 2T]`,
`Φ(log n) = 0` (`2 ≤ n < e^{2T}`), con las dos condiciones de `eq:Kprim` (P47, l. 453–476, cotejado:
`∫Φ cosh(u/2) = 0`, `∫Φ u sinh(u/2) = 0`). Con `Φ = μ̂`, `μ ≥ 0` de masa 1: `𝔈 = ∫ m dμ`,
`m(τ) = Re ψ(¼ + iτ/2) − log π` (identidad comprobada en `τ = 3` a 1e−13; script abajo).

## Cotejo

1. **Antecedente más cercano.** ROUND_026_B §§2–4 (Kreĭn + huecos; techo 3.0–3.4; en §4 «Controles» ya se
   registra la ortogonalidad `ξ_{log m} ⊥ ξ_{log n}` si `n | m` como «no explotada, la comparte todo sistema
   de Beurling»); R160_M2_R1 D4–D5, Thm 4.1 (dualidad: el dual de `Z^prim_T` es el problema de pesos libres
   `K_T`); R155_033 §2.2 («τ = 0 cap»); P47 `rem:Kprim` (primitividad en términos de `Φ̂(±i/2)`); 212-26-A.
2. **Qué sería nuevo.** (i) Ver si las cadenas de divisibilidad dan restricciones *más allá* de las lineales
   `Φ(log n) = 0`; (ii) una cota explícita de la masa de `μ` en `|τ| ≤ τ_0` y de `𝔈` por empuje al círculo;
   (iii) la lectura de la primitividad sobre `μ`.
3. **Por qué evitaría el antecedente.** ROUND_026_B usa (K1)–(K2) en el lado `u`; aquí se trabaja en el lado
   `τ`, donde la singularidad `K ~ 1/u` es el crecimiento `m ~ log|τ|`, y la multiplicatividad entra por
   periodicidad.
4. **Conexión global.** `𝔈 ≥ −δ` uniforme sería un paso hacia (PBP_T); (PBP_T) ∀T → `K_T ≠ ∅` ∀T, y de ahí al
   peso verdadero sólo CONDITIONAL (212-25).

Grep previo («divisib», «cadena», «ortonormal», «Selberg», «empuje») en el índice: sólo NG-110, P74–P75,
INV_H_001, la proyección `Π_m` (Parte V, 2026-11-07) y la nota de ROUND_026_B; ninguno es este cálculo.
Conclusión adelantada: (i) es repetición exacta del dual lineal (§1); (ii) es nuevo como cuenta y da una
cota PROVED pero negativa con techo PROVED (§2); (iii) ya está en P47 (§3).

## 1. Las cadenas de divisores no añaden restricciones (PROVED)

En el espacio GNS, `⟨ξ_{log m}, ξ_{log k}⟩ = Φ(log(k/m))`. La ortogonalidad para `m | k`, `m ≠ k`, es
*literalmente* `Φ(log(k/m)) = 0` con `k/m ∈ ℕ_{≥2}`: el grafo de divisibilidad es la lista de restricciones
de contacto, nada más. Para multiplicadores `f = |Σ_{n∈C} a_n n^{−iτ}|²` sobre una cadena `C`:
`∫ f dμ = Σ|a_n|²` y la cota `𝔈 ≥ ínf_τ [m + λ(f − ‖a‖²)]` usa
`f − ‖a‖² = Σ_{j≠k} a_j ā_k (n_k/n_j)^{iτ}`. Sumando varios `(λ_i, a_i)`, lo que aparece es la parte fuera de
la diagonal de una matriz semidefinida `G`; como toda hermitiana `H` con diagonal nula es parte fuera de la
diagonal de `H + cI ⪰ 0`, la clase resultante es **exactamente** `m(τ) − Σ_d w_d cos(τ log d)` con `w` real
de signo libre soportado en los cocientes de la cadena, es decir, un certificado de peso libre (dual de
R160 Thm 4.1), además puntual en `τ` (sin usar el soporte `[−2T,2T]`). Así que la positividad de `|·|²` se
pierde en la clausura y la vía (a) **está contenida en `K_T`**: repetición. Lo que la GNS no fija son los
productos `⟨ξ_{log 2}, ξ_{log 3}⟩ = Φ(log 3/2)`, libres; la estructura semigrupo (no grupo) de `log ℕ`
aparece sólo como «restricciones en el cuadrante positivo» (§2.3).

## 2. Empuje al círculo por un generador: cota explícita

**2.1 Monotonía (PROVED).** `Re ψ(a+iy) − ψ(a) = Σ_{k≥0} y²/((k+a)((k+a)²+y²))`, cada término creciente en
`|y|`; luego `m` es par, creciente en `|τ|`, con raíz `τ_* = 6.28984` (NUMÉRICO). Por tanto
`𝔈 = C_0 + ∫_0^∞ m′(s) μ(|τ| > s) ds`, `m′ ≥ 0`.

**2.2 Teorema (PROVED, con Selberg CITED).** Sea `J = ⌈2T/log 2⌉ − 1` (número de `j ≥ 1` con `2^j < e^{2T}`),
`L := π/log 2 = 4.5324`. Si `Φ(j log 2) = 0` para `1 ≤ j ≤ J`, entonces
```
𝔈(Φ) ≥ M_2 − (m(L) − C_0)/(J+1),   M_2 := (1/L)∫_0^L m(τ)dτ = −1.4979,   m(L) − C_0 = 5.0434.
```
Prueba. El empuje `ν` de `μ` por `τ ↦ τ log 2 mod 2π` tiene coeficientes de Fourier `ν̂(j) = Φ(j log 2) = 0`
para `1 ≤ |j| ≤ J`. El mayorante de Selberg de grado `J` de un arco de longitud `ℓ` tiene media
`ℓ/2π + 1/(J+1)` (CITED), luego `μ(|τ| ≤ s) ≤ ν(arco 2s log 2) ≤ s/L + 1/(J+1)` para `s ≤ L`. Con `m′ ≥ 0`:
`𝔈 ≥ C_0 + ∫_0^L m′(s)(1 − s/L − 1/(J+1)) ds`, e integrando por partes `= M_2 − (m(L) − C_0)/(J+1)`. ∎
Con `T → ∞`: `𝔈 ≥ −1.4979`. Igual con el generador `n`: `M_3 = −2.057`, `M_4 = −2.358`, `M_5 = −2.559`
(NUMÉRICO); el mejor es `n = 2`.

**2.3 Techo del método (PROVED).** La medida uniforme en `[−L, L]` tiene `Φ(u) = sin(πu/log 2)/(πu/log 2)`,
que se anula en todo `j log 2` y da `𝔈 = M_2` exactamente: la cota es óptima para los datos de un solo
generador. Combinar generadores por el empuje al toro `(τ log 2, τ log 3)` sólo anula coeficientes en
`ℤ²_{≥0} ∪ ℤ²_{≤0}`; los mixtos `(j, −k)` (cocientes `2^j/3^k ∉ ℕ`) quedan libres y una medida concentrada
cerca de `θ_1 = θ_2` los respeta. Además `|τ| ≤ τ_*` cubre más de un período `2π/log p` para todo primo
`p` (`log p ≥ 0.5 > π/τ_*`), así que **ningún empuje por un solo generador acota la masa en todo
`|τ| ≤ τ_*`**: la masa sólo se controla en `|τ| ≤ π/log 2`. Lo que falta (`1.498`) tiene que venir de la
interacción de generadores distintos, que es el problema lineal completo `K_T` (§1). ARGUED: no hay una
versión «toro» que mejore §2.2 sin rehacer ese dual.

## 3. Primitividad sobre μ

`μ` tiene densidad `μ′ = Φ̂/2π`, entera de tipo `2T`. Las dos condiciones son
`Re Φ̂(i/2) = 0` y `Re[i(Φ̂′(i/2) − Φ̂′(−i/2))] = 0` (P47, l. 472–476, CITED; con `F ∈ P_T`, `Φ̂` se anula a
orden 2 en `±i/2`). No son funcionales `∫ g dμ` con `g` acotada: actúan sobre la continuación analítica de
la densidad y sólo tienen sentido junto con la restricción de tipo (soporte `[−2T, 2T]`). La cota de §2.2 no
usa ni el tipo ni la primitividad; sólo las cumple el ejemplo de §2.3 si se le añade una corrección (la
uniforme no es de tipo finito). En el dual, ambas son los términos de polo de P47 `thm:A`/`eq:Kprim`: ya
están (repetición). No encontré cómo convertirlas en cota de masa de baja frecuencia: OPEN.

## 4. Banco de pruebas (estado extremal de ROUND_028_A)

Frecuencia `≈ 6.7`: `m(6.7) = +0.063` (NUMÉRICO), justo por encima de `τ_*`. Su `μ` está fuera de
`|τ| ≤ L`, de modo que §2.2 no lo restringe y tampoco lo prohíbe (la cota es negativa). Compatible. Muestra
además dónde está la dificultad real: el estado extremal evita la zona controlada por el generador 2 y vive
en `L < |τ| < τ_*`-ish, donde `m ∈ (−0.33, 0)`; su `Φ` cambia de signo en `log n` (`n ≤ 13`) en vez de
anularse en una red aritmética simple.

## 5. Controles

- Enteros coprimos con 2: el mejor generador pasa a 3 y la cota baja a `M_3 = −2.057`; el argumento no
  cambia de forma. Sistema de Beurling con un generador `g`: misma cota con `L = π/log g`.
- Paso con nombre que usa `log ℕ`: sólo «existe un generador `g` con todas sus potencias en el conjunto»
  (§2.2). Lo comparte todo semigrupo multiplicativo; la exactitud de `log ℕ` **no se usa**. §1 tampoco la
  usa (el grafo de divisibilidad es el de cualquier semigrupo). Por la regla del filtro: NO-GO de selección
  para (a) como mecanismo del signo.
- Falsificadores con peso (`cΛ`, `a_P`, borrados, Davenport–Heilbronn, …): (PBP_T) no lleva peso; §2 no
  distingue ninguno porque no contiene peso.

## Resultado

**Pieza PROVED pequeña + NO-GO de selección.** (a) las cadenas de divisores son exactamente restricciones
lineales ya contenidas en el dual de pesos libres (R160 Thm 4.1): repetición. (b) primitividad = P47
`rem:Kprim`, no convertida en cota de masa: OPEN. Cota nueva: `𝔈 ≥ −1.4979 − 5.0434/(J+1)` con `J` el número
de potencias de 2 en la ventana, óptima para datos de un generador (techo `−1.4979`).

## Qué se probó

Monotonía de `m`; la cota de §2.2 y su optimalidad §2.3; la reducción §1 (clausura = peso libre).

## Qué falló y por qué

Faltan `1.498` (techo de un generador) frente a 0; el déficit de ROUND_026_B (≈ 2 respecto de 5.372) y este
son la misma pared vista desde los dos lados: la masa en `π/log 2 < |τ| < 6.29`, donde ningún generador
aislado controla nada y la información está en la interacción de cocientes no enteros (libres).

## Siguiente paso concreto

Usar el tipo `2T` (densidad entera) junto con la primitividad de orden 2 en `±i/2` para acotar
`μ(L < |τ| < τ_*)`: una desigualdad de tipo Paley–Wiener con ceros prescritos en `±i/2`. Antes, grep en
fases 155/160 por «Paley–Wiener» y «prescribed zeros».

Script: `free_weight_scripts/chain_mean_030B.py` (raíz de `m`, medias `M_n`, comprobación de `m`).
