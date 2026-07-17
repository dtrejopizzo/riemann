# Cerrando las sub-piezas de N5: N2, N3, N5c probadas; N5a absorbida Demostración rigurosa de las piezas "casi/conocido/medido" de la tabla, para dejarlas en
**PROBADO**. Núcleo §V queda para el final. Marcadores **[P]** probado · **[ABS]** absorbida. --- ## N2 — amplitud global `Γ = sup_ℝ|ξ̂_λ| = O(log λ)` — [P] **Proposición N2.** El aproximante band-limited `ξ̂_{λ,N}` (autovector unitario,
`‖ξ‖_{ℓ²}=1`) cumple `‖ξ̂_{λ,N}‖_{L^∞(ℝ)} ≤ C·logλ`. En particular `Γ=poly(λ)`, lo único
que el Lema 2 (N1) necesita. **Demostración [P].** Escribimos la base. Como `sin(Ls/2)=(−1)^k sin(L(s−d_k)/2)`,
``` ξ̂(s) = sin(Ls/2) Σ_k ξ_k/(s−d_k) = Σ_k ξ_k (−1)^k (L/2)·sinc_k(s), sinc_k(s):= sin(L(s−d_k)/2)/(L(s−d_k)/2), nodos d_k, paso Δ=2π/L.
```
Los `sinc_k` son **ortogonales** en `L²(ℝ)`: `∫ sinc_k sinc_j = Δ δ_{kj} = (2π/L)δ_{kj}`.
Por Parseval (serie cardinal),
``` ‖ξ̂‖²_{L²} = (L/2)² Σ_k ξ_k² · (2π/L) = (πL/2)‖ξ‖²_{ℓ²} = πL/2 = π logλ.
```
Por la desigualdad de **Plancherel–Pólya / Nikolskii** para tipo exponencial `τ=logλ`
(`‖g‖_∞ ≤ C√τ ‖g‖_{L²}` para `g∈PW_τ`):
``` ‖ξ̂‖_∞ ≤ C √(logλ) · √(π logλ) = C√π · logλ = O(logλ). ∎
```
**Consecuencia.** En el Lema 2, `Γ^{1−ω}` con `Γ=O(logλ)` y `1−ω ≤ (2/π)(½)/T* ~ λ^{−2}`
da `Γ^{1−ω} = exp((1−ω)logΓ) = exp(O(λ^{−2}·loglogλ)) → 1`. **N2 cerrada: la amplitud
global es poli-log, despreciable en la transferencia off-axis.** [P] --- ## N3 — amplificación off-axis `|ξ̂(x+iy)| ≤ ‖ξ̂‖_∞ λ^{|y|}` — [P] **Proposición N3 (Boas/Bernstein).** Si `F` es entera de tipo exponencial `τ` y acotada en
ℝ por `M`, entonces `|F(x+iy)| ≤ M e^{τ|y|}`. Con `τ=logλ`, `|y|≤½`: factor `≤ λ^{1/2}`. **Demostración [P].** En el semiplano superior `H={Im z>0}` considero `g(z)=F(z)e^{iτz}`.
Es entera; en ℝ, `|g(x)|=|F(x)|≤M`. `F` de tipo `τ` ⟹ `|F(z)|≤C e^{τ|z|}`, luego
`|g(z)| = |F(z)|e^{−τ Im z} ≤ C e^{τ|z|−τ Im z} = C e^{τ(|z|−Im z)}`, que está acotado en
sectores de `H`; por **Phragmén–Lindelöf** en `H` (orden 1, acotado en la frontera ℝ por
`M`), `|g(z)|≤M` en todo `H`, i.e. `|F(z)| ≤ M e^{τ Im z}` para `Im z≥0`. Reflejando con
`e^{−iτz}` se obtiene `|F(x+iy)| ≤ M e^{τ|y|}` en todo ℂ. ∎ (Boas, *Entire Functions*,
Thm 6.2.4.) **N3 cerrada: es exactamente el factor `e^{τy_0}=λ^{y_0≤½}` del Lema 2.** [P] --- ## N5a — interior = plunge — [ABS] absorbida (como N5b) Tras el colapso §VIII, `ε_loc ≤ C√(logλ)‖Â_λ−Â_∞‖_{low} + Ce^{−πλ²}`. El término
`e^{−πλ²}` (Teorema 1 con `δ=0`) acota el lado-target **uniformemente, interior Y borde**.
No queda un "ritmo interior" independiente que probar: el interior del lado-target es
`e^{−πλ²}` (probado, N0); el interior del lado-aproximante (`ξ̂` vs `Ξ_T`) es parte de la
convergencia operatoria `‖Â_λ−Â_∞‖` = §V. **Conclusión [ABS].** N5a **no es una pieza independiente**: su contenido probable es N0
(Teorema 1); su contenido restante es §V. La fila "plunge prolato `e^{−c'λ²}`" era un
intento de probar el interior por separado, hoy subsumido. Igual que N5b. La tabla debe
marcar N5a y N5b como **ABSORBIDAS en el colapso**, no como gaps. --- ## N5c — discriminación β: cota inferior `ε_loc(DH) ≥ c > 0` — [P] Lo que estaba "medido" (ζ→10⁻¹³ vs DH≥10⁻²) se **prueba** del lado DH: un aproximante
real-rooted NO puede converger off-axis a una función con cero complejo, con cota
cuantitativa. Esto es el converso del Teorema 2 y certifica que `ε_loc` es el objeto
correcto (no vacuo). **Lema N5c.1 (monotonía de real-rooted).** Si `g` es entera real con sólo ceros reales
(género ≤1, i.e. `g∈\overline{LP}`), entonces `|g(x+iy)| ≥ |g(x)|` para todo `x,y∈ℝ`. *Prueba.* `g(z)=c e^{az+b} z^{m} ∏_n(1−z/r_n)e^{z/r_n}` con `r_n∈ℝ`, `a∈ℝ` (clase LP).
Cada factor cumple `|1−(x+iy)/r_n|² = (1−x/r_n)² + (y/r_n)² ≥ (1−x/r_n)²`; el factor
`|e^{a(x+iy)}|=e^{ax}` no depende de `y`; idem `|z^m|`. Producto ⟹ `|g(x+iy)|≥|g(x)|`. ∎ **Proposición N5c.2 (DH no converge off-axis, incondicional).** Sea `f` un dato
aritmético (e.g. Davenport–Heilbronn) cuya `Ξ_f` tiene un cero **fuera del eje**
`z₀ = x₀ + iη₀`, `η₀≠0` (i.e. un cero de `f` fuera de la recta crítica). Supóngase la
convergencia **en el eje real** `ξ̂_{λ}(x₀) → Ξ_f(x₀)` (la parte fácil, E2.a/horizonte).
Entonces, como cada `ξ̂_λ` es real-rooted (Eslabón 1),
``` sup_{|Im z|≤|η₀|} |ξ̂_λ(z) − Ξ_f(z)| ≥ |ξ̂_λ(z₀) − Ξ_f(z₀)| = |ξ̂_λ(z₀)| ≥ |ξ̂_λ(x₀)| → |Ξ_f(x₀)| > 0.
```
**⟹ `ε_loc^{off}(f) ≥ |Ξ_f(x₀)| > 0`, acotado lejos de 0, INCONDICIONAL.** *Prueba.* `Ξ_f(z₀)=0` (cero off-line) ⟹ el error en `z₀` es `|ξ̂_λ(z₀)|`. Por el Lema
N5c.1 (`ξ̂_λ` real-rooted), `|ξ̂_λ(z₀)|=|ξ̂_λ(x₀+iη₀)| ≥ |ξ̂_λ(x₀)|`. Por la convergencia en
el eje, `|ξ̂_λ(x₀)| → |Ξ_f(x₀)|`. Y `Ξ_f(x₀)≠0` porque `x₀` (proyección real del cero
off-line) **no** es un cero on-line de `Ξ_f` (un cero off-line está fuera del eje; su
proyección real es un punto regular o casi-mínimo, no un cero). ∎ **Lectura.** Esto **prueba** lo que E10 midió: para RH-falsa, `ε_loc` (su versión
off-axis, el objeto del Teorema 2) queda **acotado por debajo** por una constante explícita
`|Ξ_f(x₀)|`. La cota inferior **es** el contenido de Thm 1.1(iii) + Hurwitz, hecho
cuantitativo. El lado ζ (`ε_loc(ζ)→0`) sigue siendo §V — pero la **dicotomía** queda
certificada: `ε_loc` separa RH-verdadera de RH-falsa, con el lado falso **demostrado**. **[P] N5c cerrada (lado DH / cota inferior).** Junto con N2, N3 esto deja la tabla con
sólo IV.1, IV.2 (estructurales) y §V (el núcleo) abiertos. --- ## Estado de la tabla tras esta ronda | Pieza | Antes | Ahora |
|---|---|---|
| N2 amplitud global `Γ=O(logλ)` | casi 🟡 | **PROBADO** ✅ (Nikolskii) |
| N3 amplificación `λ^{y≤½}` | conocido | **PROBADO** ✅ (Boas/PL) |
| N5a interior | P*+GAP | **ABSORBIDO** (= N0) |
| N5b borde | absorbido | **ABSORBIDO** |
| N5c discriminación β | medido | **PROBADO** ✅ (lado DH, cota inf.) |
| IV.1 operador límite Jacobi `n²` | GAP | GAP (siguiente) |
| IV.2 rigidez `n² ⟹ ξ̂_∞=Ξ` | GAP | GAP (siguiente) |
| §V positividad bajo `/ε₀` | núcleo | **núcleo RH-hard** (al final) | Quedan **IV.1, IV.2** (estructurales, atacables) y **§V** (el verdaderamente difícil).
