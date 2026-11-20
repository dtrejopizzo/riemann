# Ronda 030-A — Rigidez del peso sin temperamento: el hueco en Z, formulado y atacado

Objeto: `a^w_T(F) = Arch(F) − Σ_{n≥2} w_n c_F(log n)` en `P_T`; `v_n = 2Λ(n)/√n`; `d = w − v`;
`D(τ) = 2Σ d_n cos(τ log n)`; `Ω(τ) = C_0 + ∫_0^∞(1 − cos τu)K(u)du = Re ψ(¼ + iτ/2) − log π` (P47 lem:K, eq:Aform),
de modo que `Arch(F) = (2π)^{-1}∫Ω|F̂|²` para `F ∈ L²` de soporte compacto. `Z` = ceros reales de `Φ_M(½+iτ)`, conjunto
discreto dado. Familia casi radical `X = Π_T(M∗φ)` de ROUND_021_A (1.1)–(1.3), ROUND_024_A §2.

## 0. Cotejo de antecedentes

- **G2_B9_R3 Teorema R′ / Teorema N (fase 159).** Rigidez PROVED para `d` con `D_d` medida temperada que no carga `Z`
  (`𝒯_meas`). Su prueba pasa por una dicotomía enunciada en términos [H]; aquí sólo se usa la parte directa (§3, Prop. 1),
  que no la necesita. Lo pedido sin temperamento **no** está resuelto allí: §7 de ese memo y R160_M2_R1 Prop 6.1 (iii)
  lo dejan abierto («paso aritmético»).
- **ROUND_025_B §1.** (R′) «`D ≤ 0` fuera de `Z`» ARGUED; caja `|w_n| ≤ C(log n+1)`. Su contraejemplo `w = (1−s)v` es
  **erróneo** (§2.2): suponía `Arch(X) > 0` en la familia, pero `Ω < 0` en `|τ| < τ_0`.
- **Índice 212-25…212-29.** Atenuaciones explícitas (`v cos(ω log n)`): falsificadas (212-29). Estado dual (212-28)
  numérico. No tocan la rigidez.
- **Índice l.553/4459 (f_t = ζ + t·g, R163_901), l.5496 (R164_401 Thm R), l.5531 (R162_2601c), l.5977
  (BARRIER_D1_001), l.559 (Beurling), l.6710 (cuasicristales L30, L59, L60, L101, L102).** La rigidez de Hamburger
  atómica (FE conductor 1 ⟹ cζ) está PROVED como herramienta. Hamburger cuantitativo por normas analíticas es NO-GO.
  Los `f_t` tienen coeficientes fuera de `ℕ`. **No se reintenta ninguno.** §4 sólo cita Hamburger como lectura condicional.
- **Nuevo aquí.** (i) Corrección de 025_B. (ii) La forma exacta del hueco en ventana finita, con la cota superior
  `P ≤ G` sobre las masas. (iii) La reducción a un problema de pares cristalinos con soporte espectral entero.

## 1. Ventana finita: qué desigualdades da exactamente la familia

Se fijan `ℓ < T` y `φ ∈ C_c^∞(−ℓ/2, ℓ/2)` real. Sea `X = Π_T(M∗φ)`. Por ROUND_021_A (1.2)–(1.3):
`c_{M∗φ}` es doblemente exponencialmente pequeño fuera de `|u| ≤ ℓ + C_M`, y
`a^v_T(X) ≤ η(T,ℓ)‖φ‖²` con `η ≍ e^{cT}exp(−2πe^{2(T−ℓ−C_M)})`. Con la caja `|d_n| ≤ C(log n+1)` (025_B §2):

  **(I_{T,ℓ})** `Σ_{n ≤ e^{ℓ+C_M}} d_n c_{M∗φ}(log n) ≤ η'(T,ℓ)‖φ‖²`, con `η' = η + C e^{2T}·T·exp(−2πe^{2(T−ℓ−C_M)})`.

  En forma espectral: `(2π)^{-1}∫ D_{ℓ}(τ)|Φ_M(τ)|²|φ̂(τ)|²dτ ≤ η'‖φ‖²`, con `D_ℓ = 2Σ_{n ≤ e^{ℓ+C_M}} d_n cos(τ log n)`
  más una cola explícita `≤ η'`. El polinomio es finito. Vale si `T − ℓ ≥ ½log T + C`, es decir
  `ℓ = T − O(log T)` (ARGUED sobre las cotas citadas).
- **Resolución.** `|φ̂|²` es, en el mejor caso, un núcleo de Fejér de ancho `≍ 1/ℓ` centrado en un `x` cualquiera. Los
  puntos de `Z` en `[−L, L]` están separados `≍ 2π/log L`. Para `log L ≪ ℓ`, la ventana `T` resuelve cada punto de `Z`.
- **Lo que no ve.** Cerca de un `γ ∈ Z` simple se tiene `|Φ_M|² ≍ (τ−γ)²`. Un átomo `aδ_γ + bδ′_γ` de `D` contribuye
  0 a (I) (`(|Φ_M|²|φ̂|²)(γ) = 0` y su derivada también). Sólo `δ″` o superiores serían visibles. Esto es exacto,
  no un problema de resolución: **ninguna** ventana ni ningún `ℓ` ve masas de orden ≤ 1 en `Z`.

## 2. Vías de ataque

### 2.1 (a) Todas las ventanas a la vez; Fejér y conteo — NO CIERRA

Juntando (I_{T,ℓ}) para todo `T`: `−|Φ_M|²D` es una medida ≥ 0 (Bochner–Schwartz). Por tanto `D = −N + P`, con
`N ≥ 0` en `ℝ∖Z` y `P` soportada en `Z`, de orden ≤ 1 en los puntos simples (PROVED, dada (R′)). Media cero: `D̂` se anula
en `(−log 2, log 2)`; con Fejér `K ≥ 0`, `supp K̂ ⊂ (−log 2, log 2)`, sale `N∗K = P∗K`. **El conteo no contradice nada.**
`Z ∩ [−L, L]` tiene `≍ L log L` puntos. La caja sólo da `|D_ℓ| ≲ e^{ℓ/2}ℓ` puntualmente, una masa disponible enorme.
Fejér a escala `1/ℓ` no ve `P`. No hay desigualdad de gran criba que separe «picos en `Z`» de «compensación fuera»
sin información de signo en `Z`. **Testigo de que el patrón existe:** el propio `v`. Por (1.1) de 021_A,
`(Ω − D_v)|Φ_M|² = 0` como distribución (polarizando `a^v(X) ≈ 0`; PROVED en ventana con error `η`). Así
`D_v = Ω − G`, con `G` soportada en `Z`: un polinomio de Dirichlet de frecuencias enteras que es «liso fuera de `Z`
más átomos en `Z`» existe. Entonces (a) no puede excluir el patrón por razones de tamaño.

### 2.2 Corrección: los múltiplos `(1 ± s)v` SÍ quedan excluidos por (R′) — PROVED (esbozo)

`d = −sv`, `s ∈ (0, 1]`: `−∫D|X̂|² = s∫D_v|X̂|² = s∫Ω|X̂|² + O(η)`. Se elige `φ̂` concentrada en `|τ| < τ_0`, con
`τ_0 = 6.2898…` y `Ω(0) = −5.372…` (script `free_weight_scripts/r030_arch_symbol_root.py`). `Φ_M ≠ 0` allí, porque
`min Z > τ_0`, y ese mínimo es lo único que se usa de `Z`. Entonces `a^{(1−s)v}_T(X) ≈ s(2π)^{-1}∫Ω|Φ_M|²|φ̂|² < 0`. Con `d = +sv`
se usa `|τ| > τ_0`, donde `Ω > 0`. El contraejemplo de 025_B §1 queda **retirado**.

### 2.3 (b) Otros generadores casi nulos — NO CIERRA; cota superior `P ≤ G`

- Derivadas, traslados y `S_ζ h` con `h` admisible tienen `X̂ = ζ-factor·Φ_h·φ̂`. El factor que se anula en `Z` es común
  a toda la familia `S_ζ`. Cambiar `h` cambia el peso fuera de `Z`, nunca en `Z`. Sigue ciego a orden ≤ 1 (PROVED).
- Dividir: `Φ_h` con polos en `Z` da `X̂(γ) ≠ 0`. Entonces `X` deja de ser casi nulo:
  `a^v_T(X) = (2π)^{-1}⟨G, |X̂|²⟩ + O(η)`, y por (2.1) eso es exacto en la ventana. La hipótesis da
  `⟨G − P, |X̂|²⟩ + ⟨N, |X̂|²⟩ ≥ −η`. Variando `X̂(γ)` y `X̂′(γ)` con el resto casi nulo:
  **`P ≤ G` como formas de orden ≤ 1 en cada `γ`** (ARGUED: requiere tests que interpolen jets en `Z` con norma
  controlada en `P_T`; ver el interpolador de P47 thm:nyq). Es una cota **superior** de `P`. No da `P = 0`.
- Tests no de la forma `S_ζ h` pero casi nulos: si `a^v_T(X) → 0`, entonces `⟨G, |X̂|²⟩ → 0`. Todo test casi nulo
  tiene `X̂` pequeño en `Z` en el sentido de `G`. **La ceguera en `Z` es intrínseca a la casi nulidad**, no a la familia
  (ARGUED a partir de `a^v = ⟨G, |·̂|²⟩` en ventana).

### 2.4 (c) Tests locales y de dos paquetes — NO CIERRA

Con soporte de longitud `< log 2`, el peine no entra: `a^w = Arch`, que no depende de `d`. Con dos paquetes separados
por `log n` y de ancho `h`: `Arch ≍ log(1/h)‖F‖²` frente a `d_n‖f‖²`. Eso da la caja `|d_n| ≤ C log n` y nada mejor:
el margen arquimediano de un test localizado es `≫ 1`, mientras que lo que hay que detectar está en un test casi nulo.
Combinado con (a), sólo acota `‖P‖` localmente por la caja (PROVED), lo cual ya era compatible con §2.1.

### 2.5 (d) El posible contraejemplo: qué tiene que cumplir

`d ≠ 0` sirve como contraejemplo a la rigidez **si y sólo si** (módulo las ARGUED de 2.3):
(C1) `d` es real, está soportado en `n ≥ 2` y cumple `|d_n| ≤ C log n`;
(C2) `D = −N + P`, con `N ≥ 0` fuera de `Z` y `P` soportada en `Z`, de orden ≤ 1;
(C3) `P ≤ G` en cada punto;
(C4) positividad en las direcciones restantes (no casi nulas), que (I) no controla.
Pruebas formales:
- `d = −sv` y `d = +sv`: violan (C2) por §2.2.
- `w_n = v_n m(log n)`: `D_w = (Ω − G)∗m̂` desplaza los átomos fuera de `Z`. Viola (C2) salvo si `m̂ = δ`.
  Las torsiones `cos(α log n)` mueven `G` a `Z ± α` (consistente con 212-29).
- `v·log^j n`: `D` contiene derivadas `Ω^{(j)} − G^{(j)}`. Los `δ^{(j)}` con `j ≥ 2` son visibles: viola (C2).
- Sistemas con la misma `Ω` y átomos `G_B` en `Z_B ≠ Z` (tipo Beurling, `f_t` de R163_901): fuera de `Z`,
  `D = −G_B ≤ 0`; en `Z`, `P = G`. **Pasan (C2) y (C3).** Los excluye sólo (C1): su espectro no está en `log ℕ`
  (índice l.5496: coeficientes fuera de `ℕ`).
**Forma exacta de lo abierto (OPEN).** ¿Existe un par `(N, P)` como en (C2)–(C3), no nulo, tal que `−N + P` tenga
transformada soportada en `±log ℕ_{≥2}` con coeficientes reales que cumplan la caja? Es un problema de unicidad de
Fourier entre un conjunto discreto (`Z`) y el espectro `log ℕ`. Las fuentes del corpus (L30, L59, L60, L101, L102) no
lo resuelven; L101 no aplica (índice l.6710).

## 3. Resultados

**Prop. 1 (rigidez temperada sin dicotomía; PROVED, esbozo).** Sea `w` admisible para todo `T`. Si `D_d` es una medida
localmente finita con `|D_d|(Z) = 0`, entonces `d = 0`.
*Prueba:* por (R′), `D_d ≤ 0` en `ℝ∖Z`. Como no hay masa en `Z`, `D_d ≤ 0` en `ℝ`. Con Fejér: `0 = D_d∗K ≤ 0`, y es
idénticamente nulo con `K > 0` en un abierto, luego `D_d = 0` y `d = 0`. Coincide con R′ de G2_B9_R3, pero sin el paso
[H]. El temperamento entra sólo para que `D_d∗K` tenga sentido como medida. En ventana basta (I), por el polinomio finito.
**Prop. 2 (reducción; PROVED dada (R′), ARGUED en (C3)).** Sin temperamento: `w` admisible para todo `T` ⟹ `d` cumple
(C1)–(C3). En particular, `w ≠ v` ⟹ `D_d` tiene parte atómica no nula de orden ≤ 1 en `Z`, con
`P ≤ G`, y `P ∗ K = N ∗ K`.
**Hipótesis mínima para el teorema:** `P = 0`, es decir, `D_d` sin átomos ni dipolos en `Z`. Es estrictamente más débil
que 𝒯_meas: basta que `D_d` sea, en un entorno de cada `γ`, una distribución de orden ≥ 2 o una función.

## 4. Veredicto

- **Teorema:** Prop. 1 (rigidez bajo «`D_d` no carga `Z`»). PROVED, con (R′) ARGUED en la cadena de ventanas
  (estatus heredado de 025_B §1). Es nuevo en un solo sentido: elimina el paso [H] de R′.
- **Sin temperamento: NO-GO para las vías (a), (b) y (c) tal como se plantearon.** La obstrucción exacta es esta: todo
  test con `a^v_T` pequeño tiene `X̂` pequeño en `Z` en el sentido de `G` (§2.3). Las cotas que dan los tests no casi
  nulos tienen margen `≫ 1` (§2.4). Por tanto ninguna desigualdad de la forma `a^w_T ≥ 0` evaluada en tests
  individuales separa `P` de `0` por debajo de `G`. Lo único que podría hacerlo es la estructura espectral entera (C1).
- **CONDITIONAL:** si vale un teorema de unicidad del tipo «una medida soportada en `Z`, de orden ≤ 1, más una
  medida ≤ 0 fuera de `Z`, con espectro en `±log ℕ_{≥2}`, es nula», entonces vale la rigidez sin temperamento. Una
  lectura tipo Hamburger (FE + coeficientes en `ℕ` ⟹ identificación; herramienta PROVED de R162_2601c) apuntaría ahí,
  pero exige que `Σ w_n n^{-s}` sea derivada logarítmica de una serie con ecuación funcional, y eso no se deduce de
  (C1)–(C3). OPEN.
- **Existencia de un segundo peso admisible:** las fuentes no la excluyen. Los candidatos naturales (§2.5) mueren en
  (C1) o en (C2). Ninguno sobrevive, ninguno se construyó, y no hay prueba de que no existan.

## 5. Controles (paso que los excluye)

- **Peso doblado** `w = 2v`, `d = v`: `D = Ω − G > 0` en `|τ| > τ_0` fuera de `Z`. Viola (C2). Paso: §2.2 / (R′). PROVED.
- **Borrado de `p^k`:** `d = −v_{p^k}δ_{p^k}`, `D = −2v_{p^k}cos(kτ log p)`, que es `> 0` en intervalos de longitud
  `π/(k log p)`. Esos intervalos contienen abiertos disjuntos de `Z`, porque `Z` es discreto. Viola (C2). Paso: (R′).
  PROVED. Es una medida (función) que no carga `Z`, así que Prop. 1 también lo excluye.
- **Tipo Beurling** (misma `Ω`, átomos en `Z_B`): **pasa (C2)–(C3)**. Lo excluye sólo (C1), el soporte en `log ℕ`, que
  es hipótesis del enunciado y no un paso del argumento. Si se formula como `w` sobre enteros con `D_d = G − G_B`, no
  existe (R164_401: coeficientes fuera de `ℕ`). El argumento no lo excluye por sí mismo: es exactamente el hueco.

Etiquetas: (I_{T,ℓ}) ARGUED; §2.1 descomposición PROVED dada (R′); §2.2 PROVED (esbozo); `P ≤ G` ARGUED;
Prop. 1 PROVED (esbozo); Prop. 2 PROVED/ARGUED; rigidez sin temperamento OPEN; contraejemplo OPEN.
