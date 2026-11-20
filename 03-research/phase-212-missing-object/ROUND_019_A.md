# Ronda 19, memo A — Control de escala: ¿es el margen `e^{−2πe^{2T}}` la cola reticular más allá de `N = e^{2T}`?

Nota de control, deliberadamente modesta. No es una prueba de signo ni se presenta como tal. Notación de
P47 y de la ronda 7: `a_T(F) = Arch(F) − Σ_n v_n c_F(log n)`, `v_n = 2Λ(n)/√n`, `c_F(u) = ∫F(t)F(t−u)dt`,
`P_T = {∫F e^{±t/2} = 0}`, `N := e^{2T}`. `W_*` = forma de la fórmula explícita en la clase de Weil
`D^W` (suma de primos sobre todo `n`), como en `phase-160-row-d-infinite-T/R160_M4_R1.md`.

## Filtro de cuatro puntos

1. **Antecedente más cercano.** `R160_M4_R1.md` §4 (Teorema B(i), l.334–351), Remark C1 (l.427–431:
   «`2π` es el exponente natural del truncado de un solo radical») y O-5 (l.555–557: constante aguda
   abierta); re-controlado en `ANNEX_MARGIN_CONFLICT.md` §3. Para la cola de (PC):
   `phase-161-row-d-sum-product-square/R161_001_MUNTZ_CHEBYSHEV_ANOMALY.md` Teor. 2.1 y 3.1, §5;
   `ROUND_002_A.md` (Lema y §(4)). Lado «colas de Poisson»: `phase-211-sign-sandbox/ROUND_015_A.md`
   (peine sobre colas de Poisson = `2⟨𝒯_log u, 𝒯u⟩`) y `ROUND_019_B.md` (reducción a colas
   admisibles; índice maestro P211-15A, P211-19B).
2. **Lo nuevo.** Sólo una afirmación de control: la descomposición del valor `a_T(X_T)` por fuentes
   (diagonal arquimediana, corrección `a·u_ev`, primos `n ≥ N−2`), con el signo de la cola reticular
   `n > N`, y el comportamiento de `a_T(X_T)` bajo los tres controles. No se propone objeto.
3. **Por qué no repite.** Ninguna fuente localizada evalúa por fuentes `a_T(X_T)` ni compara su
   exponente con una cola reticular; B(i) sólo acota `|W_*(E)|` en bloque. No hay mecanismo de signo
   nuevo: la nota no pretende pasar el filtro como constructora.
4. **Conexión con la positividad global.** Ninguna directa. Lo único que podría dar es una restricción
   sobre el resto `ρ_T` de una identidad `a_T = ‖V_TF‖² + ρ_T` evaluada en `X_T`.

## §1 Cotejo de antecedentes

- `grep` en `05-meta-and-planning/ROUTES-MASTER-INDEX.md` por `2πe^{2T}`, `near-radical`, `X_T`,
  `Poisson tail`, `first omitted`: las únicas apariciones de `X_T` como vector casi nulo son l.31144–31146
  (registro de R160_M4_R1: «el objeto debe llevar `X_T` casi a cero a esa escala»); `X_T` de
  G1C-R161_020-021 (l.5235, l.12338) y de 16_03 (l.21265, l.30658) son **otros** objetos (un escalar de
  dispersión y un operador). Q-P2.2 (l.9305) pide un bloque casi radical con Guo cuantitativo, sin
  evaluación. Ninguna entrada enuncia «margen = primer término reticular omitido en `N = e^{2T}`».
- En el corpus, «first omitted / primer término omitido» no aparece con este sentido. R160_M4_R1
  Remark C1 dice lo más cercano: `2π` = dos veces la tasa `π` de decaimiento de `K_Pó`, que por el
  Teorema C es la máxima posible en el radical ξ-divisible. 106_09 (cota `Cλ^Me^{−cλ²}`, `λ = e^T`, `c`
  no especificado) tiene el mismo origen (cortes de `K, K′, K″`), sin evaluar la cola de (PC).
- **La cola de (PC) nunca se evaluó en `X_T`.** Además no puede evaluarse tal cual: (PC) es una
  identidad de operadores `S_N A_{M_0} 𝓕 = …`, y para leer `a_T(F)` en ella hace falta un test
  `z = S_N𝓕g = F` con `g` en la ventana, que no tiene solución (`ROUND_002_A` §(4), `REVIEW_001_ABD`
  §4.1). Lo que sí aparece en `a_T(X_T)` es la suma de primos de `W_*` sobre `n > N` (§2).
- **Qué cerró `ROUND_002_A`.** NO-GO de clase (Lema, PROVED): formas `C^w − ⟨α, Bα⟩` con test de momentos
  `Σ_L`, `L` finito, cualquier peso `w ≥ 0` en `k > N`: ninguna es semidefinida sobre `P_T`; la cola no
  es `±(Σ_k h(k)|ℓ_k|² + ρ)` con `ℓ_k` en momentos de orden `≤ L`. Una evaluación sobre **un** vector
  explícito no es una forma sobre `P_T` y queda fuera de esa clase; pero tampoco puede dar signo: sólo
  restricciones. Así se trata aquí.

## §2 El cómputo

**Vector** (R160_M4_R1 l.346–351; ANNEX §3). `K_Pó(t) = Σ_{n≥1}(4π²n⁴e^{9t/2} − 6πn²e^{5t/2})e^{−πn²e^{2t}}`,
par, `Φ_{K_Pó} = ξ`; `M = −K_Pó″ + ¼K_Pó`, `Φ_M(s) = s(1−s)ξ(s)`, `M ∈ P_T`-tipo (`A(M) = B(M) = 0`).
`χ_T` corte liso, `= 1` en `[−T+θ, T−θ]`, `θ = e^{−2T}`; `E = M(1−χ_T)`; `a = −ℓ_ev(E)`;
`X_T = Mχ_T − a u_ev ∈ P_T`. Con `Y = E + a u_ev`:

    a_T(X_T) = W_*(Y) = W_*(E) + 2a W_*(u_ev, E) + a² W_*(u_ev).                          (2.1)

(PROVED en la memoria; aquí CITED, re-controlado en ANNEX §3.)

**De dónde sale `e^{−2πe^{2T}}` en la prueba.** No hay contorno ni Bessel: es la cola gaussiana del
término `n = 1` de la serie theta, `|K_Pó^{(j)}(t)| ≤ c_j e^{(9/2+2j)|t|} e^{−πe^{2|t|}}` (Lema 3), evaluada en
el borde del soporte de `E`, `e^{2(T−θ)} = N − 2 + O(e^{−2T})`. Cada factor (`‖E‖`, `a`, `𝔪_T(E)`) es
`e^{cT}e^{−πN}`; `2π` sale de que (2.1) es **cuadrática** en la cola. Es decir
`e^{−2πN} = (e^{−π·1²·x})²|_{x=N}`: punto reticular `n = 1` de `ℤ` en la gaussiana de theta, al cuadrado;
no un término `e^{−2πky}` en `k = N`. (PROVED como lectura de la prueba.)

**Descomposición por fuentes** (ARGUED: estimaciones de Laplace sobre `e^{−π(e^{2t}+e^{2s})}`, sin
constantes escritas). Sea `ε_N := e^{−2πN}`.

(a) *Diagonal arquimediana.* `Arch_*(E) ≈ ∫ m(τ)|Ê(τ)|²dτ`; `E` vive en frecuencias `|τ| ≳ e^{2T}`
(colapso del corte en anchura `θ` y oscilación de la gaussiana), donde `m(τ) ~ log|τ| > 0`. Tamaño
`e^{cT}ε_N`, **positivo**.

(b) *Primos `n < N − 2`.* Para que `E(t)E(t−log n) ≠ 0` con ambos puntos en `|·| ≥ T−θ` hace falta
`log n ≥ 2T−2θ` (lados opuestos) o ambos del mismo lado, con exponente `−π(N−2)(1+n²) ≤ −5π(N−2)`.
Despreciables.

(c) *Primos `n ≥ N − 2` (la «cola reticular más allá de `N`»).* Lados opuestos: `c_E(log n) ≈
∫E(t)E(log n − t)dt` (paridad de `E`), exponente `−π(e^{2t} + n²e^{−2t})`, mínimo `−2πn` en `e^{2t} = n`,
admisible exactamente cuando `n ≥ N − 2`. Así `c_E(log n) = e^{cT}e^{−2πn}`·(factor de forma), y
`−Σ_{n≥N−2} v_n c_E(log n)` tiene el **mismo exponente** `2πN`, dominado por los dos o tres enteros
`n ∈ [N−2, N+2]` y decreciente como `e^{−2πn}` después. Coincidencia de escala: **sí**, pero por la
misma gaussiana (desigualdad `e^{2t} + n²e^{−2t} ≥ 2n`), no por una retícula de Poisson.

(d) *Corrección `a·u_ev`.* `2aW_*(u_ev,E)`: `a = e^{cT}e^{−πN}`, y `W_*(u_ev, E)` contiene primos con
`log n ≈ T`, es decir `n ≈ √N = e^T` (contactos de `u_ev ⊂ (−½,½)` con la cola en `±T`), de tamaño
`e^{cT}e^{−πN}`. Producto: otra vez `e^{cT}ε_N`, con aritmética en `n ≈ e^T`, no en `n ≈ e^{2T}`.

**Conclusión del cómputo.** El exponente `2πe^{2T}` es común a (a), (c) y (d); el corte natural para
(c) es `N = e^{2T}` (no `e^T`), pero (d) introduce `e^T`. La constante delante de `ε_N` depende de
`χ_T`, `θ`, `u_ev` y de `Λ` en unos pocos enteros cerca de `N` y cerca de `√N`: no es canónica (es
O-5, constante aguda, abierta). El término `H_{M,N}` de (PC) no aparece: lo que aparece es la suma de
primos de `W_*` restringida a `n ≥ N − 2`.

## §3 Signo y controles

**Signo de la cola `n > N` en `X_T`** (ARGUED, verificable por asintótica del término `n = 1`). Para `t`
grande, `K_Pó″ ≈ 16π⁴ e^{17t/2}e^{−πe^{2t}} > 0`, luego `M < 0` en `t ≥ T−1` (`M(1.5) ≈ −1.9·10^{−19}`,
NUMÉRICO) y `E ≤ 0` en `t ≥ 0`. Entonces `E(t)E(log n − t) ≥ 0` y `c_E(log n) > 0` en primer orden para
`n ≥ N − 2`: la cola reticular entra en `a_T(X_T)` como `−Σ_{n≥N−2} v_n c_E(log n) < 0`. Es una suma con
coeficientes `v_n ≥ 0` de productos positivos (no cuadrados), **con signo menos**. Lo positivo a esa
escala es (a), la energía arquimediana de alta frecuencia de la cola del corte. La lectura «`ρ_T` = cola
reticular más allá de `N`» tiene el signo equivocado.

**Qué cancelación hace casi nulo a `X_T`.** `W_*(M, ·) ≡ 0` (Lema 2(a) de la memoria): `Φ_M = s(1−s)ξ`
se anula en todos los ceros, por la ecuación funcional de theta (Poisson sobre `ℤ`: `θ(1/x) = √x θ(x)`,
espaciado entero) **junto con** el producto de Euler (suma de primos con `Λ` exacta). Usa el espaciado de
los enteros dos veces: en el radical y en la tasa `π` de la cola (primer punto no nulo `n = 1`).

**Controles.** Para un peso `w`, `W^w_* = W_* − Σ_n (w_n − v_n) c(log n)`, y `c_{X_T}(log n) = c_M(log n)
+ O(e^{cT}e^{−πN})`. Luego

    a^w_T(X_T) = −Σ_n (w_n − v_n) c_M(log n) + O(e^{cT}e^{−πN}).                         (3.1)

El paso que falla es el Lema 2(a): `M` deja de estar en el radical de `W^w_*`. Valores (NUMÉRICO,
cuadratura en `[−6,6]`, paso `5·10^{−5}`, `n < 2·10⁴`): `c_M(log 2) ≈ −9.753`, `c_M(log 3) ≈ +6.066`,
`c_M(log 4) ≈ +0.235`, `P(M) := Σ v_n c_M(log n) ≈ −1.698`, `‖M‖² ≈ 97.47`.

- `2Λ`: `a^{(2)}_T(X_T) → −P(M) ≈ +1.70 > 0`. El casi-nulo se rompe a `O(1)` pero hacia **positivo**:
  `X_T` no es testigo para `c = 2`. (Para `c < 1` da `(1−c)P(M) < 0`; en particular `Arch(X_T) ≈ P(M) < 0`,
  coherente con F2.)
- Borrar `p^k`: `a^{del}_T(X_T) → v_{p^k} c_M(k log p)`. Borrar `2`: `√2 log 2·(−9.753) ≈ −9.56 < 0`,
  `X_T` es testigo negativo a `O(1)`. Borrar `3`: `≈ +7.70 > 0`.
- Beurling: `−Σ(w_n − v_n)c_M(log n)`, `O(1)` y de signo determinado por el perfil `c_M`, que alterna
  en `n = 2, 3` y es despreciable para `n ≥ 7` (`c_M(log 7) ≈ 3·10^{−7}`).

Lectura: el casi-nulo de `X_T` es una propiedad del radical, no del signo; bajo control se pierde en el
primer orden, con un signo fijado por `c_M` en `n = 2, 3`. La cola `n > N` no interviene en ninguno de
los tres controles a primer orden.

## §4 Veredicto

1. (i) **Refutada como lectura** (ARGUED para órdenes y signo; PROVED el origen del exponente): el
   exponente `2πe^{2T}` es `(e^{−π·1²·e^{2T}})²`, cola gaussiana del término `n = 1` de theta al cuadrado.
   La suma de primos sobre `n ≥ N − 2` reproduce el mismo exponente (misma gaussiana, `e^{2t}+n²e^{−2t} ≥ 2n`),
   pero entra con signo **negativo**, y comparte orden con la diagonal arquimediana (positiva) y con la
   corrección `a·u_ev` (primos `n ≈ e^T`). Sin constante canónica (O-5 sigue OPEN).
2. La cola `H_{M,N}` de (PC) no se puede evaluar en `X_T`: (PC) no contiene `a_T(X_T)` sin `z = F`
   (ROUND_002_A §(4)); no se computó, por imposibilidad de formulación, no por coste.
3. (ii) Implicación para el objeto: sólo una **restricción** (ARGUED): `ρ_T` no puede ser una cola
   reticular `Σ_{k>N}(pesos ≥ 0)·(productos de la cola)`, porque en `X_T` esa cola es negativa y la
   compensa la energía arquimediana de alta frecuencia. No hay candidata `ρ_T` con fórmula.
4. Controles (NUMÉRICO + identidad (3.1) PROVED a primer orden): `2Λ` da `X_T` positivo (`≈ +1.70`);
   borrar `2` da `≈ −9.56`; la ruptura está en el Lema 2(a) (radical) y depende de `c_M` en `n = 2, 3`,
   no de la cola.
5. (iii) Siguiente operación: **ninguna** en esta dirección. Calcular la constante de `ε_N` sería LOCAL
   y no decide nada (depende de `χ_T`, `u_ev`).

Cálculo auxiliar descartable (no forma parte del registro): script de cuadratura de `c_M(log n)`.
