# E2.núcleo — toda la matemática pura posible Ataque al único nudo RH-hard restante, vía el reencuadre de aproximación
(-style): no atacar `R_λ` ni `δV` (probado RH-equivalente, `(λ²)^{Θ−½}`),
sino la diferencia con la **truncación canónica de Fourier** de Ξ. Marcadores: **[P]** probado (matemática pura) · **[GAP]** módulo resultado clásico
estándar · **[!]** hallazgo/frontera. --- ## 0. Objeto y meta `ξ̂_{λ,N}` = función entera band-limited de tipo `T = L/2 = log λ` (PW_{T}) cuyos
ceros reales son los `ρ̂_n`, **real-rooted por Eslabón 1** (Perron–Frobenius, Λ(n)≥0,
**probado**). `Ξ(z)` = función xi de Riemann (entera, orden 1, par, real en ℝ),
real-rooted `⟺` RH. Vía Hurwitz, RH se sigue si `ξ̂_{λ,N} → Ξ` **uniformemente en una franja compleja de
ancho fijo** que contenga los ceros. Todos los ceros de Ξ viven en `|Im z| ≤ ½`
(porque `ρ = ½+it` con `Re ρ ∈ (0,1)` ⟹ `Im z = ½−Re ρ ∈ (−½,½)`). Meta: convergencia
uniforme en `|Im z| ≤ ½`. --- ## 1. Truncación canónica de Fourier `Ξ_T` — Paso 1 [P] ### 1.1 Representación de Riemann Clásico (Riemann 1859 / Pólya):
``` Ξ(z) = ∫_{-∞}^{∞} Φ(u) e^{izu} du, Φ(u) = Σ_{n≥1} (2π²n⁴ e^{9u/2} − 3πn² e^{5u/2}) · exp(−πn² e^{2u}).
```
`Φ` es **par** (`Φ(−u)=Φ(u)`, contenido de la ecuación funcional), suave, y
``` Φ(u) ≤ C · e^{9u/2} · exp(−π e^{2u}) (u ≥ 0) (★)
```
con `C` absoluta. (Para `u≥0`, `Σ_n n⁴ e^{−πn²e^{2u}} ≤ e^{−πe^{2u}} Σ_n n⁴ e^{−π(n²−1)e^{2u}} ≤ C e^{−πe^{2u}}`.)
**Decaimiento DOBLE-exponencial.** Eso es todo lo que se usa. ### 1.2 Definición y tipo ``` Ξ_T(z):= ∫_{-T}^{T} Φ(u) e^{izu} du.
```
`Ξ_T` es entera de **tipo exponencial `T`** (Paley–Wiener: soporte de la transformada
en `[−T,T]`), con `|Ξ_T(x+iy)| ≤ (∫Φ) e^{T|y|}`. **[P]** ### 1.3 Teorema 1 (convergencia strip-uniforme, incondicional) > Para todo `δ ≥ 0` y `T = log λ`:
> ```
> sup_{|Im z| ≤ δ} |Ξ(z) − Ξ_T(z)| ≤ C_δ · λ^{5/2+δ} · e^{−π λ²}.
> ``` **Demostración [P].** Por evenness,
``` |Ξ(z) − Ξ_T(z)| = |∫_{|u|>T} Φ(u) e^{izu} du| ≤ 2∫_T^∞ Φ(u) e^{δu} du.
```
Por (★),
``` 2∫_T^∞ Φ(u) e^{δu} du ≤ 2C ∫_T^∞ e^{(9/2+δ)u} e^{−π e^{2u}} du.
```
Sustituyendo `v = e^{2u}` (`du = dv/2v`):
``` = C ∫_{e^{2T}}^∞ v^{5/4+δ/2} e^{−πv} dv = C · Γ(7/4+δ/2, π e^{2T}).
```
Para la Gamma incompleta con argumento grande `X=e^{2T}`:
`∫_X^∞ v^a e^{−πv} dv ≤ 2 X^a e^{−πX}/π` (`X` grande). Con `a=5/4+δ/2`, `X=e^{2T}=λ²`:
``` ≤ C' · (λ²)^{5/4+δ/2} · e^{−πλ²} = C' · λ^{5/2+δ} · e^{−πλ²}. ∎
``` **[!] Corolario fuerte.** El prefactor `λ^{5/2+δ}` es **polinomial**; lo aplasta
`e^{−πλ²}`. La cota tiende a 0 incluso si `δ = δ(λ) → ∞`, mientras
`(5/2+δ)log λ < π λ²`, i.e. **`δ(λ) = o(λ²/log λ)`**. La truncación de Fourier
converge a Ξ uniformemente en franjas cuyo ancho **crece** hasta `~ λ²/log λ`.
En particular, trivialmente, en `|Im z| ≤ ½`. ### 1.4 Qué establece (y qué NO) el Paso 1 **Establece [P]:** existe un aproximante band-limited de tipo `log λ`, canónico y
explícito, que converge a Ξ **uniformemente en la franja de TODOS los ceros**, a tasa
super-exponencial `e^{−πλ²}`, **sin condición y sin mencionar la posición de ningún
cero** (sólo `Φ` doble-exponencial). **Refuta** mi objeción previa (eslabon2-soft-theorem §3): "tipo `log λ` ⟹ franja
`~1/log λ → 0`". **Falso para la truncación de Fourier.** La franja de Paley–Wiener-L²
se angosta, pero la diferencia `Ξ−Ξ_T` se controla por la **cola de `Φ`**, que es
doble-exponencial y gana en cualquier franja fija. **La truncación de Fourier de Ξ no
es el obstáculo.** (Frase ajustada según el referee: no decimos "band-limiting no es el
obstáculo" — eso aún depende del Paso 2.) **NO establece:** que `Ξ_T` sea real-rooted (no lo es, es una truncación cualquiera).
Por eso `Ξ_T` solo no da RH. El real-rootedness lo aporta el objeto CCM `ξ̂`. → Paso 2. --- ## 2. Descomposición y localización — Paso 2 ### 2.1 La descomposición limpia ``` ξ̂_{λ,N} − Ξ = (ξ̂_{λ,N} − Ξ_T) + (Ξ_T − Ξ). └──── δ̂ ────┘ └─ Teorema 1: ≤ λ³ e^{−πλ²} en |Im z|≤½ ─┘
```
El segundo término está **completamente controlado** (Teorema 1, `δ=½`). **Todo el
contenido RH restante está en `δ̂:= ξ̂_{λ,N} − Ξ_T`**, que es entera de tipo `≤ T = log λ`
(diferencia de dos funciones de tipo `T`). **[P]** ### 2.2 Lema de continuación off-axis (PL + medida armónica) [P] > **Lema 2.** Sea `F` entera de tipo exponencial `τ`, con `|F(x)| ≤ Γ` para todo `x∈ℝ`
> y `|F(x)| ≤ ε` para `|x| ≤ R`. Entonces para `|x₀| ≤ R/2`, `0 < y₀ ≤ δ`:
> ```
> |F(x₀+iy₀)| ≤ e^{τ y₀} · ε^{ω} · Γ^{1−ω}, ω = ω_{[−R,R]}(x₀+iy₀),
> ```
> con `ω` la medida armónica del segmento `[−R,R]` vista desde `x₀+iy₀` en el semiplano
> superior. Para `y₀ ≪ R`: `1−ω ≤ (2/π)(y₀/R)`. **Demostración [P].** En `H={Im z>0}` pongo `w(z)=log|F(z)| − τ·Im z`. `log|F|` es
subarmónica, `τ Im z` armónica ⟹ `w` subarmónica en `H`. En la frontera `ℝ`:
`w(x)=log|F(x)| ≤ log Γ`, y `≤ log ε` en `[−R,R]`. `F` de tipo `τ` y acotada en `ℝ`
satisface `|F(z)| ≤ Γ e^{τ|Im z|}` (Boas, *Entire Functions*, Thm 6.2.4), luego `w` está
acotada superiormente en `H` y vale Phragmén–Lindelöf: `w` está por debajo de su
mayorante armónica de los datos de frontera,
``` w(z) ≤ ω_{[−R,R]}(z)·log ε + (1−ω_{[−R,R]}(z))·log Γ.
```
Exponenciando y reponiendo `τ y₀`: `|F(z)| ≤ e^{τ y₀} ε^{ω} Γ^{1−ω}`. La cota de
medida armónica del segmento desde `iy₀`: `ω_{[−R,R]}(iy₀) = (2/π)arctan(R/y₀) ≥ 1−(2/π)(y₀/R)`. ∎ ### 2.3 Aplicación a `δ̂` `δ̂` es de tipo `τ = log λ`. Sea
``` ε_loc(λ):= sup_{|t| ≤ T*} |ξ̂_{λ,N}(t) − Ξ(t)|, T* = 2π λ² (horizonte, Lema 2/CCM),
```
la tasa de aproximación **en el eje real, sobre el segmento del horizonte**. En el
segmento, `|δ̂| ≤ ε_loc + |Ξ_T−Ξ| ≤ ε_loc + λ^{5/2}e^{−πλ²} ≈ ε_loc`. Globalmente en ℝ,
`Γ:= sup_ℝ|δ̂| = poly(λ)` (ambas band-limited acotadas; `Ξ` decae exponencial en ℝ por
el factor Γ de Euler). Aplico el Lema 2 con `R=T*~λ²`, `δ=½`, `τ=log λ`, en `|x₀|≤T*/2`:
``` |δ̂(x₀+iy₀)| ≤ e^{(log λ)·½} · ε_loc^{ω} · Γ^{1−ω} ≤ λ^{1/2} · ε_loc · poly(λ)^{(2/π)(1/2)/(2πλ²)} ≈ λ^{1/2} · ε_loc. (∗)
```
**[!] La corrección de medida armónica `Γ^{1−ω}` es despreciable** porque el horizonte
`R=T*~λ²` es enorme: `1−ω ~ 1/λ²`, luego `Γ^{1−ω}=poly(λ)^{1/λ²}→1`. **El horizonte
gigante mata la cola lejana.** Solo sobrevive la amplificación de tipo `λ^{1/2}` (de
`δ=½`, la profundidad de los ceros). ### 2.4 Teorema 2 (reducción final, incondicional) > ```
> sup_{|Im z| ≤ ½} |ξ̂_{λ,N}(z) − Ξ(z)| ≤ C · λ^{1/2} · ε_loc(λ) + C λ³ e^{−πλ²}.
> ```
> **Corolario (criterio para RH):** si
> ```
> ε_loc(λ) = sup_{|t|≤2πλ²} |ξ̂_{λ,N}(t) − Ξ(t)| = o(λ^{−1/2}) (λ→∞),
> ```
> entonces `ξ̂_{λ,N} → Ξ` uniformemente en `|Im z| ≤ ½`, y por **Hurwitz** Ξ hereda el
> real-rootedness de `ξ̂_{λ,N}` (Eslabón 1) ⟹ **RH**. **Demostración [P].** Suma de §2.1 (Teorema 1, `δ=½`: `λ³e^{−πλ²}`) y (∗)
(`λ^{1/2}ε_loc`). Si `ε_loc=o(λ^{−1/2})`, el sup en la franja `→0`; los ceros de `ξ̂`
(reales, Eslabón 1) convergen a los de Ξ y, por Hurwitz en la franja abierta `|Im z|<½`,
ningún cero de Ξ puede estar fuera del eje. ∎ --- ## 3. Dónde quedó el muro — frontera exacta [!] Todo RH (en este programa) está ahora en **un único número real medible**:
``` ε_loc(λ) = sup-norma de (ξ̂_{λ,N} − Ξ) sobre el segmento real [−2πλ², 2πλ²]. ¿Es o(λ^{−1/2})?
``` Esto es **mucho más fino** que `(λ²)^{Θ−½}`. Análisis honesto de si es RH-equivalente o
más débil: - **A favor de que se cierre (no-circular):** `ε_loc` es un **residuo de interpolación band-limited a densidad crítica** (Beurling–Selberg/Plancherel–Pólya). El conteo encaja: Ξ tiene `~N(T*)~(T*/2π)log T* ~ λ²·2log λ` ceros bajo el horizonte; `ξ̂` de tipo `log λ` tiene `~(log λ/π)·2T* ~ (2/π)λ²log λ` grados de libertad reales — **comparables** (esto ES el Lema del horizonte). Hay apenas suficientes DOF para interpolar. La tasa puntual medida fue `e^{−cλ²}` (c≈11) — **si esa tasa vale en sup-norma sobre TODO el segmento**, entonces `ε_loc ~ e^{−cλ²} ≪ λ^{−1/2}` y **RH se sigue**. El factor `λ^{1/2}` de amplificación off-axis es ridículamente pequeño contra `e^{−cλ²}`. - **El riesgo real (dónde re-entran los ceros):** `ε_loc` es un **sup sobre un intervalo que CRECE** como `λ²`. La aproximación band-limited se **degrada cerca del borde del horizonte** `|t|~T*`, donde el residuo de interpolación depende del espaciamiento real de los nodos `= los γ_n`. El peor caso sobre el segmento podría ser `O(1)`, no `e^{−cλ²}`. **Ahí, y solo ahí, puede reaparecer la información de los ceros.** Pero nótese: lo que importa cerca del borde es la **regularidad del espaciamiento** de los γ_n (Riemann–von Mangoldt, densidad — incondicional), no su **parte real** (posición). Plausiblemente **más débil que RH completa**. Esa es la apuesta, ahora afilada. ### El blanco matemático preciso (sustituye al muro difuso)
``` ¿ sup_{|t|≤2πλ²} |ξ̂_{λ,N}(t) − Ξ(t)| = o(λ^{−1/2}) ?
```
Un objeto de **teoría de aproximación pura** (residuo de interpolación a densidad
crítica cerca del borde del horizonte), medible numéricamente, sin nombrar a Weil ni la
positividad. Es la localización más limpia del programa: de `(λ²)^{Θ−½}` (RH-equivalente
manifiesto) a "sup-norma del residuo sobre el horizonte vs `λ^{−1/2}`". --- ## 4. Estado | Pieza | Estado |
|---|---|
| **Teorema 1** — `Ξ_T→Ξ` strip-uniforme `λ^{5/2+δ}e^{−πλ²}` | **[P] probado, incondicional, sin ceros** |
| **Lema 2** — continuación off-axis PL + medida armónica | **[P] (módulo Boas Thm 6.2.4, clásico)** |
| **Teorema 2** — reducción: RH ⟸ `ε_loc=o(λ^{−1/2})` | **[P] probado** |
| El horizonte `λ²` mata la cola lejana (`Γ^{1−ω}→1`) | **[P]** |
| `ξ̂` real-rooted (Eslabón 1) | **[P] (previo)** |
| **`ε_loc(λ) = o(λ^{−1/2})`** — el blanco | **[GAP] — único nudo; medible** | **Conclusión.** Se hizo toda la matemática pura posible sin tocar el nudo: el Paso 1 es
un **teorema limpio e incondicional**, y la maquinaria de continuación reduce RH a una
**única cota de sup-norma sobre el horizonte**, `ε_loc = o(λ^{−1/2})`. No prueba RH —
pero transforma el muro difuso `(λ²)^{Θ−½}` en un blanco de aproximación preciso y
medible. Próximo paso natural (numérico): medir `ε_loc(λ)` como sup sobre `[−T*,T*]`
(no en puntos/ceros sueltos) y ver su ley en `λ`, en particular cerca del borde `|t|~T*`.
