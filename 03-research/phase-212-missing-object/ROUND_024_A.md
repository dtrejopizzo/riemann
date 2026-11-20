# Ronda 24, memo A — Término principal del defecto de truncación: ROUND_019_A §§2–4 frente a ROUND_021_A §3

Nota de control. No es un intento de signo. Notación de P47 y de la ronda 7: `a_T(F) = Arch(F) − Σ v_n c_F(log n)`,
`v_n = 2Λ(n)/√n`, `P_T = {∫F e^{±t/2} = 0}`, `W_*` la forma global, `M = (−∂² + ¼)K_Pó`, `K_Pó = S_ζ g_0`,
`g_0(t) = (2π²e^{9t/2} − 3πe^{5t/2})e^{−πe^{2t}}`, `W_*(M∗φ, ·) ≡ 0` (CITED: R160_M4_R1 Lema 2(a); P46 Thm 11.11).

**Archivos abiertos:** ROUND_019_A.md, ROUND_021_A.md (íntegros); ROUTES-MASTER-INDEX.md por grep (entradas P211-17A,
l.6457 y l.9833; registro de ROUND_021_A, l.31200–31204); P2_SCHUR_001.md por grep (Lemas P2-S.2, P2-S.3).
**No abiertos:** R160_M4_R1.md, 106_09, ROUND_017_A de la 211, P47 main.tex, BRIEF_CONSTRUCTOR.md, RULES_AVOID.md
(la tarea es de cuenta, no de construcción). Sin cómputo.

## §0 Cotejo
La pregunta (quién domina y por qué difieren los dos memos) no está respondida en el corpus: el índice registra la
afirmación de ROUND_021_A (l.31204) y la de ROUND_019_A, sin conciliación. La parte de acople es P211-17A (ver §4).

## §1 Corrección de la premisa: los dos cortes son lisos
ROUND_019_A l.52: «`χ_T` corte liso, `= 1` en `[−T+θ, T−θ]`, `θ = e^{−2T}`». No es un corte abrupto. El vector
de ROUND_019_A es el caso particular de ROUND_021_A con `φ = δ_0` (`δ = T`), transición de anchura `η = θ = e^{−2T}`
y una sola corrección par `u_ev` (en vez de `u_±`). La diferencia relevante NO es el tipo de corte sino (i) la distancia
`D := δ − η` entre el soporte de `φ` y el inicio de la transición y (ii) que ROUND_019_A comparó exponentes y ROUND_021_A
constantes.

## §2 Rederivación del término principal (general, `R = (1−χ)(M∗φ)`, `D = δ − η`)
**(a) Perfil.** Para `t → +∞`, `M(t) = −16π⁴e^{17t/2}e^{−πe^{2t}}(1 + O(e^{−2t}))` (término `n = 1` de `S_ζ`, dos
derivadas de la gaussiana doble exponencial). `M∗φ` en `t ≥ T − η` es `≍ ‖φ‖_{L¹}·e^{cT}e^{−πe^{2(t−(T−δ))}}`, con
tasa local de decaimiento `A := 2πe^{2D}`. `R` es el producto de esa caída por `1−χ`, que crece desde `0` en `T−η`.
La masa de `R` está en una capa de anchura `w`:
- si `1−χ` se anula a orden finito `r` en `T−η`: `w ≍ 1/A ≍ e^{−2D}`;
- si `χ ∈ C_c^∞` (anulación plana, perfil tipo `e^{−η/x}`): `w ≍ (η/A)^{1/2}` en la escala `η` y, para `η` fijo,
  `w ≍ A^{−3/4}`. (ARGUED, Laplace.)
En ROUND_019_A (`η = θ = 1/N`, `N = e^{2T}`, `A = 2πN`) ambos casos dan `w ≍ 1/N`. En ROUND_021_A con `η` fijo y
`χ` liso, el «orden finito» de l.103 no es compatible con `χ ∈ C_c^∞`; da `w ≍ e^{−3D/2}`, no `e^{−2D}`.

**(b) Diagonal arquimediana, signo +.** `Arch_*(R) = (1/2π)∫m(τ)|R̂(τ)|²dτ`, `m(τ) = log|τ| + O(1)` para `|τ| ≥ 1`.
`|R̂|²` está repartido hasta `|τ| ≍ 1/w`; la parte `|τ| ≤ C` pesa `≤ C‖R‖²_{L¹} ≤ Cw‖R‖²`. Así
`Arch_*(R) = (log(1/w) + O(1))‖R‖² = (κD + O(1))‖R‖²`, `κ = 2` (orden finito) o `κ = 3/2` (plano, `η` fijo); `κD = 2T + O(1)`
en ROUND_019_A. **Positivo.** (ARGUED.)

**(c) Primos, signo −.** Autodesplazamientos: `c_R(log n)` con ambos factores en la misma capa exige `log n ≤ w`:
imposible. Cruces `+`/`−` (o `R` con la cola de `M` más allá de `T` en ROUND_019_A): `log n ∈ 2(T−η) ± O(w)`, es decir
`≍ e^{2(T−η)}w` enteros, cada uno con `v_n ≤ 4Te^{−(T−η)}` y `|c_R(log n)| ≤ C‖R‖²` (Cauchy–Schwarz), y la suma sobre la ventana se
controla por `∫|c_R(u)|e^{u}du ≤ Ce^{2T}‖R‖²_{L¹} ≤ Ce^{2T}w‖R‖²`. Cota uniforme (sin cancelación ni distribución de primos):

    |Σ_n v_n c_R(log n)| ≤ C·T·e^{−T}·max(1, e^{2T}w)·‖R‖².                                               (2.1)

Para `e^{2T}w ≥ 1` (muchos enteros) el factor es `C·T·e^{3T}w²`; para `e^{2T}w < 1` (a lo sumo `O(1)` enteros), `C·T·e^{T}w`.
Signo: si `φ` es par y de un signo, `R ≤ 0` en ambas capas (`M < 0` para `t` grande), `c_R(log n) > 0` y el término entra
con **−** (coincide con ROUND_019_A l.96–101). (ARGUED.)

**(d) Corrección de momentos.** `|A(R)|, |B(R)| ≤ e^{T/2}‖R‖_{L¹} ≤ e^{T/2}w^{1/2}‖R‖`. `W_*(u, R)` (contactos `log n ≈ T`,
densidad de primos `≈ e^{T}`, peso `2Te^{−T/2}`) es `O(Te^{T/2}‖R‖_{L¹})`. Aporte total `O(Te^{T}w)‖R‖²`, sin signo fijo. (ARGUED.)

**(e) Cociente primos/arquimediana.** `𝔡_T = (κD + O(1))‖R‖²·(1 + O(ρ))`, `ρ := [Te^{−T}max(1, e^{2T}w) + Te^{T}w]/(κD)`.
- ROUND_019_A (`D ≈ T`, `w ≍ e^{−2T}`): `ρ ≍ e^{−T}`. **La arquimediana domina por `≍ e^{T}`.** Primos `n ∈ [N−2, N+2]`
  y corrección `u_ev`: ambas `O(Te^{−T})‖R‖²`.
- ROUND_021_A con `δ = T − ½`, orden finito: `ρ ≍ e^{−T}`; con `χ` plano y `η` fijo: `ρ ≍ e^{−T/2}` (aquí sale el
  `e^{T/2}` de l.112, por otra vía que la allí escrita).
- Familia general: la cota (2.1) asegura dominancia sólo si `w ≪ e^{−T}`, i.e. `D ≥ T/2 + O(1)` (orden finito)
  o `D ≥ 2T/3 + O(1)` (plano). Para `φ` anchos (`D` menor) la cota uniforme deja de bastar; la parte media de
  la suma de primos es `≈ 2∫c_R(u)cosh(u/2)du`, que es momento × momento y queda absorbida en (d); el resto depende de la
  distribución de primos en intervalos cortos de longitud `≍ e^{2T}w`. **OPEN** fuera de ese rango.

## §3 Veredicto sobre la discrepancia
1. **Exponente** (ROUND_019_A §2): correcto. Las tres fuentes llevan `e^{−2πN'}`, `N' = e^{2(T−θ)} = N − 2 + O(1/N)`:
   `‖E‖² ∝ e^{−2πN'}/N`, los cruces en `n = N' + k` llevan `e^{−2π(N'+k)}` (mínimo de `e^{2t} + n²e^{−2t}` en `2n`).
   PROVED como lectura (Laplace estándar), ARGUED en constantes.
2. **Constante** (ROUND_021_A §3): correcta en el resultado. «Comparten orden» de ROUND_019_A §2–§4(1) es cierto sólo
   módulo `e^{cT}`; dentro de ese factor, el primo cuesta `v_n ≍ 4Te^{−T}` y la diagonal `log(1/w) ≍ 2T`: la arquimediana
   domina por `≍ e^{T}`. ROUND_019_A no escribió el `e^{−T}` de `v_n` (lo absorbió en `e^{cT}`). Su conclusión (ii) («la
   cola reticular es negativa y la compensa la energía arquimediana de alta frecuencia») es compatible y queda reforzada.
3. **¿Sólo el corte?** No. Los dos cortes son lisos. Difieren en (i) nivel de lectura (exponente vs constante), (ii) `D`:
   `D = T` en ROUND_019_A, `D` libre en ROUND_021_A; (iii) el perfil de `1−χ` cambia `κ ∈ {3/2, 2}` y el margen
   (`e^{T}` vs `e^{T/2}`), no el signo. ROUND_021_A tiene dos imprecisiones: «orden finito» con `χ` liso y la afirmación
   para `φ` general, que sólo vale para `D ≥ T/2 + O(1)` (§2(e)).
4. Signos: diagonal +, primos −, corrección sin signo; término principal `𝔡_T ≈ κD‖R‖² > 0`, ciego a `Λ`. ARGUED.

## §4 Acople con el complemento
Para `G ∈ P_T`, `F = M∗φ`: `χF + G = F + (G − R)`, y `W_*(F, ·) ≡ 0` da `a_T(χF + G) = W_*(G − R)` (PROVED, una línea).
En `span{G, χF}`, con `s ∈ ℝ`:

    a_T(G + sχF) = W_*(G) − 2s W_*(G, R) + s² W_*(R),

y como `W_*(R) > 0` (§2, ARGUED en el rango de dominancia), `min_s = W_*(G) − W_*(G,R)²/W_*(R)`. Es la forma secular /
Schur de P211-17A (PROVED allí: `(★) ⟺ C ⪰ 0` y `ρ ≥ sup b²/a_T`) con bloque escalar `W_*(R)` y vector `b = W_*(G,R)`;
a `T = ∞` (`R = 0`) es `𝒲_AB ≡ 0` de P2_SCHUR_001 (Lema P2-S.2: Schur = la forma en el cociente).

Lo que añade el cálculo de §2 (ARGUED): `|W_*(G, R)| ≤ ` energía de `G` en la capa `|t| ∈ [T−η, T]` a frecuencias `≍ 1/w`
(arquimediana local) + contactos de primos `log n ≈ 2T` y `≈ T` con pesos `e^{−T}`, `e^{−T/2}`. Así la corrección de Schur
`W_*(G,R)²/W_*(R)` está acotada por `(κD)^{−1}`·(energía de alta frecuencia de `G` en la capa)² más términos
`O(e^{−T/2})`. Lectura: la familia casi radical sólo puede bajar `a_T` por debajo de `W_*(G)` a través del contenido de
`G` en la capa de borde a frecuencia `≍ e^{2D}`.

**¿Enunciado de signo nuevo?** No. (i) `W_*(R) > 0` es positividad de la diagonal del bloque, ya registrada como «no
fija `λ_A`» (ROUND_021_A §3; índice l.31204). (ii) La desigualdad `W_*(G)W_*(R) ≥ W_*(G,R)²` es exactamente la
positividad de `W_*` en `span{G, R}`, o sea el problema original sobre un plano; reescribirla como Schur es P211-17A.
(iii) La cota del vector de acople por la capa de borde es una localización de `b`, no un signo; P211-17A ya mostró
(NUMÉRICO) que la cuota de Schur no es atribuible a arch/peine/Tate por separado, y esta localización no lo contradice
ni lo resuelve. NO-GO como fuente de signo (ARGUED); ninguna operación nueva.

## Etiquetas
- Premisa «corte abrupto» de la pregunta: incorrecta (ROUND_019_A l.52). CITED.
- Exponente común `e^{−2πe^{2T}}` (019 §2): PROVED como lectura; constantes ARGUED.
- Dominancia arquimediana por `≍ e^{T}` en `X_T` y por `≍ e^{T}`/`e^{T/2}` (orden finito/plano) con `δ = T − ½`: ARGUED.
- ROUND_021_A §3 para `φ` general: ARGUED sólo si `D ≥ T/2 + O(1)` (`2T/3` con `χ` plano); OPEN en el resto.
- Identidad `a_T(χF + G) = W_*(G − R)` y forma 2×2: PROVED (elemental); equivalente a P211-17A / P2_SCHUR_001: CITED.
- Enunciado de signo nuevo: ninguno.
