# (T★) — Veredicto del tribunal (· ·) Los tres atacaron (T★) — el único pendiente declarado no-RH-hard. **No convergieron.** Hay
acuerdo total en varios wins reales, y **un desacuerdo agudo en el último paso** que es,
honestamente, el resultado del día: revela que (T★) **no era un solo enunciado RH-neutral**. --- ## ACUERDO UNÁNIME — wins reales, RH-neutrales, demostrados **W1 — La escala de borde es logarítmica no degenerada [PROBADO, RH-neutral].**
`h(λ)=π−ω*=π/(2N+1)` exacto; `2N+1≍2logλ`; por tanto `(logλ)·h(λ)→π/2 ∈(0,∞)` (Thm 2.3).
Ni colapsa (sub-log⟹espectro continuo) ni diverge (super-log⟹degenera). **La escala está cerrada.** **W2 — Capa de Landau–Widom, ancho `Θ(logλ)` [PROBADO vía teorema LW, ].**
El ancho de rampa del prolato `P_c` (`c=2πλ²logλ`) es `W(λ)=Θ(logλ)`, y coincide con `Γ` de N2 y
con `‖Ξ_T‖²` — **los tres son la MISMA capa logarítmica**. Confirma la predicción IV.1.4. **W3 — Reconciliación Airy/Bessel ↦ n² [RESUELTO, era una conflación].**
El borde Airy/Bessel es del **concentrador** `P_c`; el `(k+1)²` es del **inverso-de-Green** (el SL).
Miran porciones espectrales distintas (`μ→½` rampa vs `ν→∞` cola de Weyl). Green explícito
`min(x,y)(1−max)` tiene autovalores `(kπ)^{−2}↓`, su inverso crece como `(k+1)²`. La objeción
-IV.4 **NO** refutaba (T★): era conflación concentrador↔inverso (versión espectral de C.2). **W4 — Tensión de escalas `1/logλ` vs `λ^{−2}` [RESUELTA, ].**
Era **colisión de notación `ω`**, no dos escalas físicas: la `λ^{−2}` del Lema N2 es la **medida
armónica** `ω_{[−R,R]}` (R≍λ²), no el carrier `ω*`; la `λ^{−2}` numérica era el **gap de frame**
(conflación C.2, ya retirada). **La escala física es `1/logλ`**, por balance gap–longitud. **W5 — Espectro `n²` FORZADO bajo (T) [PROBADO condicionalmente].**
Si la familia es tight (T), Mosco ⟹ límite discreto; el blow-up `y=(x−½)/h` con `h≍1/logλ` acota
el potencial residual a `O(1)`, Sturm fija SL regular con Dirichlet BC, Weyl da `μ_k/μ_0→(k+1)²`,
`γ→3`. **Sin input extra.** El `n²` ya no es un misterio: es consecuencia de (T). --- ## EL DESACUERDO (el resultado del día): ¿la tightness (T) es RH-neutral o RH-hard? Tras W1–W5, todo (T★) se reduce a **probar la tightness uniforme (T)** = una **cota inferior de
Dirichlet** `c₁·𝓔_D ≤ Â_λ` con `c₁>0` uniforme. Aquí los tres se parten: **🔴 (Thm 1.3): la cota inferior ES RH.**
> `c₁𝓔_D ≤ Â_λ=A_λ/ε₀` uniforme `⟺ ε₀>0 ⟺` Weil-positividad-local `⟺` RH-local.
Razón: el potencial de Beurling–Deny `q(w)=Ω−2M₀` tiene **pozo central `q(0)≍−λ^{1/2}<0`** — el
mismo objeto cuyo signo es ε₀. Dividir por ε₀ lo profundiza, no lo cura. **Veredicto: (T★)
es ~⅔ análisis puro (W1–W5) + ⅓ muro RH (la cota inferior). (T★) NO cierra III incondicionalmente.**
"El hueco no-RH-hard del tribunal era ilusión de contabilidad: la mitad de (T) es el muro,
escondida en la cota inferior." **🟢 (CONF): la cota inferior es RH-NEUTRAL.**
> `𝓔_prime(f) ≥ κ·logλ·∫_bulk|f|² − C∫|f'|²`, `κ>0`.
Razón: usa `|Λ(n)|` (no el signo), **vale para DH**, es asintótica de Landau–Widom. El término de
primos nonlocal **confina** (masa `≍λ²` en bulk vence al pozo `≍λ^{1/2}` por `λ^{3/2}`) ⟹ impone
**Dirichlet BC efectivas** en capa `1/logλ` ⟹ tightness ⟹ Mosco ⟹ (k+1)². **Veredicto:
(T★) se comprime a UNA desigualdad (CONF) RH-neutral; NO RH-hard.** **🟡: reducible a 3 constantes de capa de borde, no-RH-hard — pero marca el riesgo.**
La no-degeneración y la tightness las prueba **por conteo + Landau–Widom**; lo que falta son tres
constantes analíticas (la constante de matcheo `2N+1=W(λ)`, la **cota inferior de ε₀**, el potencial
`V`). Explícitamente: *"la tightness descansa en la cota inferior de ε₀; sin circularidad si ε₀ se
prueba por inverso-de-Green, con circularidad si se intenta al revés. Lo marco."* --- ## DÓNDE ESTÁ EXACTAMENTE EL CHOQUE y miran **objetos distintos** y por eso difieren:
- acota `𝓔_prime` SOLA (la forma de primos, con `|Λ(n)|`) ⟹ confinamiento del **bulk**, genuinamente RH-neutral. **Esto es correcto** y es un win.
- acota `Â_λ=A_λ/ε₀` COMPLETA (primos **menos** arquimedeano `q`, dividido por `ε₀`) ⟹ la positividad global, que **es** el signo de ε₀. **Esto también es correcto.** La pregunta no resuelta: **¿el confinamiento del bulk (CONF, RH-neutral) basta para la tightness
de la familia, o la tightness exige además controlar el pozo negativo `q` (= signo de ε₀ = RH)?**
- Si la EXISTENCIA del límite (posiblemente con masa escapando a 0) sólo necesita CONF ⟹ gana: el operador límite y su espectro RELATIVO `(k+1)²` son RH-neutrales.
- Si la NO-DEGENERACIÓN del límite (que no se escape masa) necesita `q` controlado ⟹ gana: esa pieza es RH. ya lo formuló como dicotomía (su punto 5): **existencia del límite = RH-neutral;
no-degeneración del límite = RH.** afirma que CONF da AMBAS. **Ese es el punto abierto.** --- ## ESTADO HONESTO DE (T★) **Probado RH-neutral (los tres):** escala log (W1), capa LW `Θ(logλ)` (W2), reconciliación Airy↦n²
(W3), resolución de la tensión de escalas (W4), espectro `n²` forzado bajo (T) (W5). El **espectro
RELATIVO** `(k+1)²` y la **existencia** del operador límite están esencialmente cerrados. **El punto de choque (no resuelto):** ¿la tightness/cota-inferior es CONF (RH-neutral,)
o es ε₀>0 (RH,)? la marca como riesgo de circularidad. **El muro RH (intacto, los tres coinciden):** el **signo de ε₀** = (H-pos) = Weil-positividad =
IV.2≡§V. No se movió un milímetro. La hoja `/ε₀` lo presupone. ## Corrección importante al mapa
El veredicto previo decía *"los 4 huecos se comprimen a UN enunciado RH-neutral (T★)"*. **Eso era
demasiado optimista** (lo refuta): (T★) **no es enteramente RH-neutral** — contiene una cota
inferior de Dirichlet cuyo status (RH-neutral vs RH) es **el punto en disputa**. Lo no-RH-neutral
de (T★), si tiene razón, es el mismo muro de siempre (signo de ε₀), no algo nuevo. — A. · C. · H. (tribunal, en desacuerdo)
