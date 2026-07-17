# El muro vía la estructura cuaterniónica — enunciado preciso para evaluación

**Fecha:** 2026-06-25. **Para:** evaluación con A. Connes / C. Consani. **Honestidad:** todo lo
marcado MEDIDO es numérico (engine fiel `engine_cache.py`, forma de Weil semilocal, dps≥40, falsador
Davenport–Heilbronn = DH); lo marcado PROBADO remite a la cadena (Teoremas 2.2, 12.2); las
CONJETURAS son lo que habría que demostrar. Ningún paso usa la posición de los ceros como input.

---

## 0. El lever (PROBADO) — el muro es un escalar

Por el **Teorema 2.2** (Perron–Frobenius, incondicional a λ finito: `Λ(n) ≥ 0` ⟹ semigrupo
positividad-preservante ⟹ estado base `u₀ > 0` simple = minimizador global de `A_λ`), el muro
`μ_λ = inf spec A_λ ≥ 0 ⟺ RH` (CCM Cor. 2.17) es la **desigualdad escalar**

$$\boxed{\;\varepsilon_0(\lambda) \;=\; \frac{\langle u_0,\,A_\lambda\,u_0\rangle}{\|u_0\|^2}\;\ge\;0\;}$$

sobre la función positiva explícita `u₀`. Con `ε₀(λ) → 0` (**marginalidad**, Teorema 12.2 PROBADO),
el muro es: **¿`ε₀` llega a 0 por arriba (RH) o por abajo (¬RH)?** MEDIDO: `ε₀(λ) = +5.8, 4.2, 3.6,
2.9, 2.7, 2.2, 2.1, 2.0 × 10⁻²¹` para λ=7…21 (positivo, decreciente); DH: `ε₀ = −6.54`.

## 1. La estructura cuaterniónica aritmética (MEDIDO, RH-neutral)

En la base de Fourier `V_n = e^{2πi n u/L}` sobre `[0,L]`, `L = 2log λ`, el operador `∗` de Deninger
construido **desde el flujo de escala** (E52, NO desde los ceros) es `∗ = Σ·K` (`K` = conjugación),
con parte lineal `Σ V_n = i·sgn(n)·V_{−n}`. MEDIDO exacto: `∗² = −1` (en `n≠0`), `[∗, θ] = 0`
(`θ = d/du`). El modo `n=0` (polo) es el `H⁰` real, núcleo de `∗`.

**Caracterización algebraica de la ∗-compatibilidad (DERIVADA y VERIFICADA hoy):** como el núcleo
`q_{mn}(u)` cumple `q_{−m,−n} = q_{mn}` y los pesos son funciones de `u` solo, se tiene
`A_{−m,−n} = A_{mn}`, de donde `(Σ^H A_λ Σ)_{mn} = \operatorname{sgn}(m)\operatorname{sgn}(n)\,A_{mn}`
y por tanto

$$\boxed{\;\delta_\lambda \;:=\; \max_{m,n}\big|(\Sigma^H A_\lambda \Sigma - A_\lambda)_{mn}\big|
\;=\; 2\,\max_{\operatorname{sgn} m \ne \operatorname{sgn} n}\big|A_{mn}\big|\;}$$

VERIFICADO a máquina (`δ = 2·max|A_opp-sign|` exacto, λ=7,11,15). Es decir: **la ∗-incompatibilidad
de `A_λ` es exactamente su bloque de acoplamiento entre frecuencias positivas y negativas.**
`δ_λ = 0 ⟺ A_λ es bloque-diagonal en la descomposición `±`-frecuencia` (los modos `+` y `−`
desacoplan, salvo por el polo `n=0`) ⟺ `A_λ` es estrictamente cuaterniónica ⟹ positividad
estructural vía `∗² = −1` (mecanismo E51: Gram `Ω(·,∗·)` definida).

El elemento cruzado, explícitamente, con `m, n' > 0`:
$$A_{m,-n'} \;=\; \mathrm{ARCH}_{m,-n'} \;-\; \sum_{n\le\lambda^2}\Lambda(n)\,n^{-1/2}\,q_{m,-n'}(\log n),
\qquad q_{m,-n'}(u) = -\frac{\sin\frac{2\pi m u}{L} + \sin\frac{2\pi n' u}{L}}{\pi(m+n')}.$$
(Núcleo **suma** de senos, vs. el núcleo **diferencia** del bloque mismo-signo.)

## 2. Estado honesto: `δ_λ ↛ 0` — la compatibilidad EXACTA FALLA

MEDIDO: `δ_λ = 0.133, 0.135, 0.181, 0.216` para λ=7,11,15,19 (**crece**). Falsador DH:
`δ = 4.51` (35× mayor). ⟹ **El `∗` aritmético hace a ζ *casi* cuaterniónica y a DH no en absoluto,
pero NO exactamente: `A_λ` no es bloque-diagonal `±`.** Por tanto el objetivo ingenuo *"la
multiplicatividad fuerza `δ_λ = 0`"* es **FALSO** (y empeora con λ). Esto hay que decirlo claro: no
existe un "lema de Euler ⟹ `δ=0`"; la cancelación cruzada `±` no es exacta.

## 3. Lo que SÍ es estructural (MEDIDO) y el blanco correcto

Sea `Â_λ = ½(A_λ + Σ^H A_λ Σ)` la **parte ∗-simétrica** (cuaterniónica) y `Ǎ_λ = A_λ − Â_λ` el resto.
MEDIDO (λ=7…19):
- `inf spec Â_λ = +1.7, +0.83, +0.59, +0.45 × 10⁻¹⁹ > 0` (**`Â_λ` es PSD para ζ**); DH:
  `inf spec Â = −4.92 < 0` (**indefinida**). ⟹ `Â_λ ⪰ 0 ⟺ RH` (otra reformulación fiel).
- `inf spec Ǎ_λ = −0.38, −0.32, −0.58, −0.63` (O(1) indefinida, no decae).
- Sobre el estado base: `⟨u_0, Â_λ u_0⟩ = +1.3·10⁻⁵`, `⟨u_0, Ǎ_λ u_0⟩ = −1.3·10⁻⁵`; **suman al
  residuo `ε₀ ≈ 10⁻²¹`** (`u_0 ⊥ Σu_0`, overlap = 0, así que `u_0` NO es `∗`-simétrico).

**Consecuencia crucial (honesta):** `Â_λ ⪰ 0` por sí solo **NO** da `ε₀ ≥ 0`, porque el término
cruzado `⟨u_0, Ǎ_λ u_0⟩` es negativo y **casi cancela** a `⟨u_0, Â_λ u_0⟩`. El muro es que la parte
cuaterniónica **domine** a la incompatible *sobre el estado base*:
$$\boxed{\;\langle u_0, \hat A_\lambda u_0\rangle \;\ge\; \big|\langle u_0, \check A_\lambda u_0\rangle\big|\;}$$
y esto es **knife-edge** (ambos lados `≈ 1.3·10⁻⁵`, diferencia `≈ 10⁻²¹`). Aquí vuelve a vivir RH.

## 4. El enunciado preciso a evaluar (las dos CONJETURAS, y dónde entra Euler)

> **Conjetura A (positividad cuaterniónica).** La parte `∗`-simétrica `Â_λ ⪰ 0` para todo λ.
> Equivalente a `Â_λ = B_λ^* B_λ` (suma de cuadrados). **Rol de Euler:** `Â_λ` mezcla, vía
> `Σ^H A Σ`, los elementos `A_{−m,−n}`; la factorización `B^*B` debería reflejar el producto de
> Euler `−ζ'/ζ(s) = Σ Λ(n)n^{−s}` como producto sobre primos (DH, sin producto de Euler, da
> `Â` indefinida). **Honestidad:** Conj. A es RH-equivalente (MEDIDO: falla para DH); su prueba
> NO es más débil que RH, pero su forma (SOS sobre la parte simétrica) es donde la
> multiplicatividad podría dar un certificado que el Cholesky directo de `A` (E42) no dio.

> **Conjetura B (dominancia sobre el estado base).** `⟨u_0, Â_λ u_0⟩ ≥ |⟨u_0, Ǎ_λ u_0⟩|`. Esto,
> con `u_0 > 0` (PF, PROBADO), da el muro. **Rol de Euler / lo que hay que probar sobre `Σ Λ(n)`:**
> el término incompatible es la suma de primos contra el núcleo-**suma**
> `Ǎ`-parte `= −Σ_{n}Λ(n)n^{−1/2}\,\tfrac12[q_{m,-n'} + \text{sgn-conjugado}]`; hay que demostrar
> que la contribución de `Σ Λ(n)n^{−1/2}` al bloque `±`-cruzado está **acotada por** su
> contribución al bloque cuaterniónico, con el producto de Euler como la estructura que lo fuerza.

**Dónde está exactamente el contenido de Euler / `Σ Λ(n)`:** la diferencia entre el bloque
mismo-signo (núcleo **diferencia** de senos, da la energía cuaterniónica `Â`) y el bloque cruzado
(núcleo **suma** de senos, da `Ǎ`). La multiplicatividad `Λ = \log * \mathbf 1` (von Mangoldt como
convolución) y `−ζ'/ζ = Σ_p \sum_k \log p\, p^{−ks}` debe controlar la razón
`\text{(bloque suma)} / \text{(bloque diferencia)}` de la suma de primos. DH rompe esto porque su
serie carece de producto de Euler (sus "primos" tienen coeficientes con signo `χ mod 5`).

## 5. Caveats de no-circularidad (para la evaluación)

- Conjeturas A y B son **RH-equivalentes** (MEDIDO: ambas fallan para DH exactamente cuando RH
  falla). No son atajos *lógicos*; son reformulaciones **estructuradas** (SOS / dominancia) donde la
  multiplicatividad entra explícitamente — a diferencia de la positividad global `∀f` (Cholesky
  E42, Hodge–Riemann E63, Herglotz E61, todos sin certificado).
- El `∗` es RH-neutral (flujo de escala, ceros = output). Pero `A_λ` **no** es `∗`-compatible
  (`δ ↛ 0`): la estructura cuaterniónica es **aproximada** para ζ, exacta solo en el límite si y
  solo si las Conjeturas se cumplen.
- **Pregunta para Connes/Consani:** ¿la factorización `Â_λ = B^*B` (Conj. A) o la dominancia
  (Conj. B) admiten un certificado que use el producto de Euler de forma esencial (no disponible
  para DH), o ambas se reducen, como todos nuestros intentos aditivos, al residuo `e^{−cL}` del
  balance exacto `P = WR + PRIME` (MEDIDO: ratio `P/(WR+PRIME) = 1.000000`)? Si es lo segundo, el
  muro es irreduciblemente el signo de ese residuo y el aporte de este documento es el **mapa
  preciso** de por qué cada estructura (`∗`-simetría incluida) aterriza ahí.

---

### Apéndice — hechos MEDIDOS hoy (reproducibles)
`E87/E87b` (ε₀ monótona, primos suben ε₀ de −6 a 0), `E88` (`P=WR+PRIME` exacto), `E90`
(`δ` = bloque `±`, no decae), `E91` (`Â` PSD ζ / indef DH), verificación `δ = 2·max|A_opp-sign|`.
Cache: `engine_cache.py`. venv: `propuestas-de-investigacion/99-archive/05-lise-science-v6/.../investigacion-2/venv`.
