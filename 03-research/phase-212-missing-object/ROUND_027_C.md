# Ronda 27, memo C — Estructura de la forma atenuada `a^{(ω)}_T`

Notación de P47 (eq:symbol, eq:form, eq:W, eq:Aform, lem:K, lem:polar): `c_F(u) = ∫F(t)F̄(t−u)dt`, `m`, `s_T`,
`v_n = 2Λ(n)/√n`, `N_T = {n ≥ 2 : log n < 2T}`, `A(F) = ∫Fe^{t/2}`, `B(F) = ∫Fe^{−t/2}`, `W_T = a_T + 2Re(AB̄)`,
`K(u) = 2e^{3u/2}/(e^{2u}−1)`. Forma atenuada: `a^{(ω)}_T(F) = Arch(F) − Σ_{N_T} v_n cos(ω log n) c_F(log n)` en `P_T ∩ D_T`.
Peso de prueba general: `a^w_T`. Antecedentes cotejados: 212-26-A (el óptimo con `w ≥ 0` se parece a `v` atenuado),
212-25 (`K_T`, Tychonoff), ROUND_019_A (3.1), ROUND_021_A §4, ROUND_024_A, P211-9A («taper» de prolatas: otro objeto),
212-24-C(c) (medias de Fejér sobre el toro: otro objeto). Nada de este memo reintenta esas entradas: el objeto nuevo
es el peso modulado `v_n cos(ω log n)` como familia de relajaciones con margen.

## §1 Hechos (i) y (ii)

**Lema 1.1 (dominios y tests complejos).** PROVED. (a) `D_T` es invariante por modulación: `Ĝ(τ) = F̂(τ+ω)` y
`log(2+|τ−ω|) ≤ log(2+|τ|) + log(1+|ω|)`. (b) Para un símbolo real par, `a(U+iV) = a(U) + a(V)` (U, V reales): el
término cruzado es `∫ s·Im(ÛV̄̂)`, integrando impar. Como `e^{±t/2}` son reales, `P_T` se parte igual; los ínfimos
real y complejo coinciden. (c) Para `F` real, `c_{Fe^{iωt}}(u) = e^{iωu}c_F(u)`, luego `cos(ωu)c_F(u) = Re c_G(u)`.
**Lema 1.2 (extensión por cero y cerradura).** PROVED. `K_T = {w ∈ ℝ^{N_T} : a^w_T ≥ 0 en P_T ∩ D_T}` es intersección
de semiespacios cerrados `{w : Arch(F) ≥ Σ w_n c_F(log n)}`, luego cerrado y convexo en dimensión finita (`a^w` es
afín en `w`). Si `T < T′` y `F ∈ P_T`, su extensión por cero está en `P_{T′} ∩ D_{T′}` con el mismo `F̂`, y `c_F`
(continua, soporte `[−2T,2T]`) se anula en `log n ≥ 2T`; así `a^w_{T′}(F) = a^{w|N_T}_T(F)` y `w ∈ K_{T′} ⟹ w|N_T ∈ K_T`.
**Lema 1.3 (paso al límite).** PROVED. Sean `T_j → ∞` y `ω_j` con `ω_j log n → 0` para cada `n` fijo (basta
`ω_j → 0`). Si `a^{(ω_j)}_{T_j} ≥ 0` en `P_{T_j}` para todo `j`, entonces `λ_A(T) ≥ 0` para todo `T`.
*Prueba.* Fijado `T`, para `T_j ≥ T` el vector `(v_n cos(ω_j log n))_{n∈N_T}` está en `K_T` (Lema 1.2) y converge
a `v|N_T` en `ℝ^{N_T}`; `K_T` es cerrado. ∎ No hace falta uniformidad en `T` ni signo de `cos`.
**Corolario 1.4 (clase convexa).** PROVED. Si `g(u) = ∫cos(ωu)dμ(ω)`, `μ ≥ 0` probabilidad, entonces
`a^{v·g}_T = ∫ a^{(ω)}_T dμ(ω)`. Por convexidad de `K_T`: si `a^{(ω)}_T ≥ 0` para `ω ∈ supp μ`, también `a^{v·g}_T ≥ 0`.

## §2 La forma atenuada en términos de la forma completa
**Proposición 2.1 (identidad exacta).** PROVED. Para `F ∈ P_T` real y `G = Fe^{iωt}`:
```
a^{(ω)}_T(F) = a_T(G) − ∫_0^∞ (1−cos ωu) K(u) c_F(u) du                                   (2.1)
             = W_T(G) + ∫_0^∞ (1−cos ωu) [4cosh(u/2) − K(u)] c_F(u) du.                   (2.2)
```
*Prueba.* (2.1): `Arch(G) = C_0‖F‖² + ∫(c_F(0) − cos(ωu)c_F(u))K`, y `Arch(F) − Arch(G) = −∫(1−cos ωu)Kc_F`; la
parte de primos de `a_T(G)` es `Σv_n Re c_G(log n)` (Lema 1.1c). En símbolo: `m(τ) − ½m(τ−ω) − ½m(τ+ω) =
−∫_0^∞ cos(τu)(1−cos ωu)K(u)du`. (2.2): `2Re(A(G)B̄(G)) = ∫_ℝ c_G(u)·2cosh(u/2)du = ∫ cos(ωu)c_F 2cosh(u/2)`, y
`∫c_F 2cosh(u/2) = 2Re(AB̄)(F) = 0` en `P_T`; restar da `−2∫_0^∞(1−cos ωu)c_F·2cosh(u/2)`. ∎
**Término polar.** `G` no anula los polos: `A(G) = ∫F e^{t/2}(e^{iωt}−1)`, `B(G) = ∫Fe^{−t/2}(e^{iωt}−1)`.
El término polar que aparece en (2.2) es `−2Re(A(G)B̄(G)) = −2ω²A′(F)B′(F) + O(ω³)`, con `A′ = ∫tFe^{t/2}`,
`B′ = ∫tFe^{−t/2}` (comprobado por las dos vías: `∫u²c_F 2cosh(u/2) = −4A′B′` en `P_T`). Signo: indefinido; es la
forma de rango 2 y signatura (1,1) de lem:polar evaluada en las direcciones de primer momento. Tamaño:
`|A′B′| ≤ ‖F‖²·∫_{−T}^{T}t²e^{t}dt ≲ T²e^{T}‖F‖²`, es decir `≲ ω²T²e^{T}` — grande frente al margen medido.
La corrección arquimediana es `−(ω²/2)∫_0^∞u²Kc_F + O(ω⁴)`, acotada por `(ω²/2)‖F‖²∫u²K` (`∫u²K < ∞`): `O(ω²)`.
Lectura: la atenuación es la forma completa en el test modulado más una corrección cuyo núcleo `(1−cos ωu)
(4cosh(u/2) − K)` es negativo cerca de 0 y crece como `ω²u²e^{u/2}`: el polo domina. Desarrollo directo
equivalente: `a^{(ω)}_T(F) = a^v_T(F) + (ω²/2)Q(F) + O(ω⁴Σv_n(log n)⁴|c_F|)`, `Q(F) = Σv_n(log n)²c_F(log n)`.

## §3 Evaluación en la familia casi nula `X_φ = Π_T(M∗φ)`
Por ROUND_019_A (3.1) con `w = v cos(ω log ·)` (exacto salvo `O(e^{cT}e^{−πN})` y la capa de ROUND_024_A):
```
a^{(ω)}_T(X_φ) = Σ_{N_T} v_n (1 − cos(ω log n)) c_{X_φ}(log n) = (1/2π)∫ |M̂(τ)|²|φ̂(τ)|² q_ω(τ) dτ,   (3.1)
q_ω(τ) = Σ_{N_T} v_n (1 − cos(ω log n)) cos(τ log n) = p(τ) − ½p(τ−ω) − ½p(τ+ω),  p = Σ_{N_T} v_n cos(τ log n).
```
(PROVED la reescritura: `c_{M∗φ} = c_M ∗ c_φ`, Plancherel.) **φ = δ:** sólo `n ≤ 6` cuentan (`c_M(log 7) ≈ 3·10⁻⁷`):
`(ω²/2)[0.9803·0.4805·(−9.753) + 1.2685·1.2069·6.066 + 0.6931·1.9218·0.235] = (ω²/2)(−4.594 + 9.287 + 0.313)
≈ +2.50·ω²` (NUMÉRICO con los valores citados): **positivo**, el `3` vence al `2` por el factor `(log 3/log 2)²`.
Cociente `≈ 2.50ω²/97.47 = 0.026ω²`; en `T = 2`, `k = 1` da `0.004` frente a `λ_min ≈ 10⁻⁴`: `X_δ` no es el
minimizador. La ley `∝ ω²` sí coincide con la medida.
**φ general:** el signo es el de la media de `q_ω` bajo `|M̂φ̂|²`. `q_ω` no tiene término constante y no es
idénticamente nulo, luego toma valores negativos; por PNT su parte lisa es `≈ Re[2e^{(½+iτ)2T}h(τ)/(½+iτ)]`,
oscila en `τ` con período `≈ π/T` y amplitud `≍ e^{T}`. Para hacer negativa (3.1) hay que concentrar `φ̂` en una
zona negativa de anchura `≍ π/(2T)` con `φ` de soporte `≤ 2T`: producto tiempo–banda `O(1)`, marginal, y
`|M̂|²` (decaimiento `e^{−πτ/2}`) premia la fuga hacia `τ ≈ 0` donde `q_ω > 0`. Conclusión: positivo para `φ = δ`
(NUMÉRICO); para toda `φ`: OPEN, sin prueba y sin contraejemplo; el riesgo es real (ARGUED). Cómputo barato que
decide: minimizar (3.1) en `φ` sobre una base prolata del soporte, `T = 1.6, 2.0, 2.4`.

## §4 Por qué Fejér falla y el coseno no
La triangular `g(u) = (1 − |u|/2T)_+` **es** definida positiva: `μ_F(dω) ∝ sinc²(ωT)dω`. Por el Cor. 1.4,
`a^{Fejér} = ∫a^{(ω)}dμ_F`, y `μ_F` tiene cola `∝ ω⁻²` sin soporte acotado. Que la media dé `−0.04…−0.15` obliga
(PROVED, lógica) a `a^{(ω)}_T < 0` para algún `ω` en el soporte, necesariamente grande (para `k ≤ 1` es `> 0`
numéricamente). Mecanismo (ARGUED): con `ω log 2`, `ω log 3` lejos de 0 los pesos de `2` y `3` caen o cambian de
signo y reaparecen las direcciones negativas de `Arch` en `P_T` (thm:index: `n_− ≥ 1` desde `T = 0.60`), que sólo
los primos bajos a peso casi pleno compensan. Sobre `X_δ` Fejér da `(1/2T)(−6.63 + 8.45 + 0.23) > 0`: el fallo está
en otra dirección. Lo que decide **no** es `g″(0) < 0` ni ser definida positiva por sí solos, sino
`1 − g(log p) = O(ω²)` para los primos bajos, es decir **soporte espectral acotado y pequeño** de `μ`.
**Clase propuesta (CONDITIONAL a `a^{(ω)}_T ≥ 0` en `[0, ω_*(T)]`):** `g = ∫cos(ωu)dμ`, `μ ≥ 0`,
`supp μ ⊂ [0, ω_*(T)]`, `ω_*(T) ≈ π/(4T)` según la tabla. Toda la clase se reduce a los cosenos (Cor. 1.4): no
hay ganancia en buscar otras atenuaciones; el núcleo del asunto es `ω ↦ a^{(ω)}_T` en ese intervalo.

## §5 ¿Hay un camino para probar `a^{(ω)}_T ≥ 0`?
**Circularidad, sin adornos.** (1) `a^{(ω)} ≥ 0` a lo largo de `T_j → ∞`, `ω_j → 0` **implica** el objetivo
(Lema 1.3). (2) El objetivo **no** implica `a^{(ω)} ≥ 0`: por (2.2) incluso la positividad de `W_T` en todos los
tests deja el resto `∫(1−cos ωu)(4cosh(u/2)−K)c_F`, sin signo y de tamaño `ω²T²e^{T}` ≫ margen. (3) Es un enunciado
**más fuerte** que el objetivo en las direcciones con `Q(F) < 0` y más débil donde `Q(F) > 0`; el margen medido
existe porque `Q > 0` en las direcciones casi nulas. No es circular, pero tampoco es más débil: es un
fortalecimiento con holgura polinómica. La desigualdad concreta a probar es
`Σ_{N_T} v_n cos(π log n/4T) c_F(log n) ≤ Arch(F)  ∀F ∈ P_T`, con constante de pérdida admisible `≲ c(T)ω²`.
**(a) T pequeño.** PROVED: para `T ≤ ½log 2` no hay contactos y `a^{(ω)} = Arch ≥ 0` (thm:index, `T ≤ 0.58`).
Para `T ≤ ½log 3` (sólo `n = 2`): `0 ∈ K_T` (thm:index) y `v ∈ K_T` (Teorema A en `½log3` más Lema 1.2), luego
`[0, v_2] ⊂ K_T` por convexidad y `a^{(ω)}_T ≥ 0` si `cos(ω log 2) ≥ 0`. Más allá: nada, porque `0 ∉ K_T` para
`T > T*_ev` y `w` no es múltiplo de `v` con dos o más contactos. «ω grande» no ayuda: va en contra de `ω → 0`.
**(b) Inducción en T.** Con `ω = π/4T` el entero nuevo entra con peso `v_n cos(π log n/4T) ≈ 0` en el borde:
costo de los enteros nuevos en `[2T, 2T+2dT)` es `O(e^{T}T·dT²)‖F‖²` (PROVED, elemental): gratis a primer orden.
Lo que no es gratis: (b1) el corrimiento de todos los pesos viejos, `∂_T w_n = v_n(ω log n/T)sin(ω log n)`, de
tamaño genérico `≲ (ω/T)Σ v_n log n|c_F(log n)| ≲ ω e^{T}‖F‖²` frente al presupuesto `ω²c(T)`: déficit por factor
`≍ e^{(1+β)T}/ω` salvo cancelación en `Σv_n log n sin(ω log n)c_{F_*}(log n)`, no disponible; (b2) el crecimiento
del dominio (tests nuevos), cuya derivada tipo Hadamard no está acotada en el corpus. NO-GO (ARGUED) como
inducción con presupuesto de margen; reabrir pide una cota de (b1) en el minimizador.
**(c) Pérdidas conocidas.** Margen medido: `0.01269, 0.00229, 0.00040, 0.00010` en `T = 0.8…2.0` (`k = 1`),
es decir `≈ e^{−4.3T}…e^{−3.5T}` con el `ω²` incluido: `N^{−2}…N^{−1.7}`. En el corpus sólo hay cotas **superiores**
con pérdida polinómica (P211-9A, `N^{16.5}e^{−2πN}`); la mitad inferior (prob:ext-L) está OPEN. Ninguna cota
inferior conocida tiene pérdida `≤ N^{−2}`: compatible en escala, inexistente en contenido.
**Qué se necesitaría.** Sobre la familia, (3.1) ≥ 0 para toda `φ`: un enunciado sobre la media de la segunda
diferencia `q_ω` de la suma de primos bajo `|M̂|²` (que contiene `Λ` exacta por `W_*(M,·) ≡ 0`). Fuera de la
familia, la desigualdad anterior. Ninguna de las dos se deduce de herramientas del corpus.

## §6 Controles
No hay prueba cuyo paso pueda fallar; lo que se rompe es la positividad medida, en la familia `X_δ` y en el paso
con nombre «radicalidad: `W_*(M,·) ≡ 0`» (Lema 2(a) de R160_M4_R1), del que depende (3.1):
- **`cΛ`:** `a(X_δ) = (1−c)P(M) + c·2.50ω² = −1.698(1−c) + 2.50cω²`; con `c < 1` y `ω² < 0.68(1−c)/c` es negativo:
  falla en el término `Arch_*(M∗φ)` de ROUND_021_A §4 (con `c > 1`, por la indefinición en `φ` de ese término).
- **Borrar `2`:** `a(X_δ) ≈ v_2cos(ω log 2)c_M(log 2) ≈ −9.56cos(ω log 2) < 0`: falla en la radicalidad.
- **Beurling:** `−Σ(w_n−v_n)c_M(log n) = O(1)` con signo del perfil de `c_M`: falla en la radicalidad.
Las violaciones son `O(1)` y el margen `O(ω²e^{−βT})`: los tres controles rompen con holgura.

## Balance
PROVED: Lemas 1.1–1.3, Cor. 1.4, Prop. 2.1 (con término polar `−2ω²A′B′`), (3.1), §5(a) para `T ≤ ½log 3`.
NUMÉRICO: `X_δ` da `+2.50ω²`. ARGUED: Fejér falla por frecuencias altas de su medida; (b) NO-GO.
OPEN: (3.1) ≥ 0 para toda `φ` (cómputo barato propuesto); `a^{(ω)}_T ≥ 0` para `T` grande; cota inferior con
pérdida polinómica. Abierto en este memo: la reducción de toda atenuación definida positiva a cosenos y la
identidad (2.2). No abierto: ningún camino de prueba de §5.
