# III + IV.1 — Veredicto consolidado del tribunal (· ·) Los tres atacaron **III (estabilidad relativa /ε₀)** y **IV.1 (operador límite)** con matemática
pura, en paralelo, y **convergieron**. Resultado honesto y con dos wins reales de demostración. --- ## RESULTADO CENTRAL (consenso): III y IV.1 son el MISMO hueco + el muro Los tres separan limpiamente, y coinciden, en tres objetos que el documento maestro mezclaba: | Objeto | Estado demostrado |
|---|---|
| `γ(λ)>0` a cada λ **finito** | **PROBADO** (simplicidad H1; B.3) — incondicional |
| **tamaño** \|ε₀\| (cuán chico es el menor autovalor) | **ANÁLISIS** — cota incondicional probada |
| **signo** de ε₀ (=Weil-pos=RH-hasta-T*) | **= RH** — irreductible, probado fuera de alcance del análisis |
| **uniformidad** `liminf_λ γ(λ)>0` | se **factoriza** en (tamaño, análisis) × (signo, RH) | **Teorema del tribunal (III.3 / III.4 / III.5):**
> `liminf_λ γ(λ)>0` ⟹ `ε₀>0` para todo λ grande ⟹ RH-hasta-T*.
> Por tanto **una prueba incondicional de la uniformidad probaría RH**: la arquitectura `/ε₀`
> presupone régimen RH-true. Ahora es **teorema, no sospecha** (confirma C.3/-agrava). --- ## WIN 1 — Cota de tamaño incondicional de ε₀ (III.3) [SÓLIDO] Por Rayleigh con el test `Ξ_T` y `‖Ξ_T‖²≍logλ`:
> **`|ε₀| = O(1/logλ)`** — incondicional (Plancherel–Pólya/Nikolskii), RH-neutral. **Corrección dura al documento maestro:** se **retira `ε₀ ~ C/λ²`** (era la conflación C.2 del
gap-de-frame `λ_min(S_λ)=0`, que tiene `O(λ²)` direcciones nulas, con el autovalor de `QW`).
El tamaño correcto probado es `O(1/logλ)`, y el **signo** sigue siendo RH. ## WIN 2 — (H-lim) deja de ser hipótesis: probado bajo tightness (III.3) [SÓLIDO] > Bajo **tightness uniforme (T)** de la familia `{Â_λ}` (condición RH-neutral, tipo Landau–Widom),
> `(H-lim)` (existencia del límite de escala) se prueba **incondicionalmente** por
> Prokhorov + convergencia fuerte de resolvente (Reed–Simon VIII.21/24). ⟹ `(H-gap)` y `(H-lim)` **colapsan en una sola** hipótesis RH-neutral (T★): *"existe escala de
borde logarítmica no degenerada"*. Antes eran dos huecos numéricos; ahora es **un** enunciado de
análisis citable. --- ## IV.1 — operador límite: tres avances + un hueco honesto **A. Obstrucción de compacidad, resuelta (IV.1) [SÓLIDO].**
La paradoja "Loewner compacto vs. operador diferencial" se resuelve: el SL de 2º orden es el
**inverso de Green** del compacto de borde. Green del Laplaciano-Dirichlet = `min(x,y)(1−max(x,y))`;
los `ε_k` medidos son autovalores del **inverso**, no del compacto ordenado. La compacidad NO
obstruye — sólo había que invertir. (Esto reconcilia E12–E18: las IDs de coef. constante fallaron
porque el potencial `V(x)` es **variable**.) **B. Cadena Sturm → Weyl, condicional pero rigurosa (IV.5–IV.6).**
La paridad alternante `(−1)^k` + `k` nodos **fuerza** (Sturm) que `Â_∞` sea un SL regular de 2º
orden con potencial par; **bajo** esa forma, la ley de Weyl + conteo de nodos (`n=k+1`) dan
`μ_k/μ_0→(k+1)²=n²` y `γ→3`. **C. `n² ⟺ (T★)` por invarianza de escala (IV.3) [SÓLIDO].**
Fijada la escala de borde **logarítmica**, el patrón `n²` está **forzado**: sub-log ⟹ espectro
continuo; super-log ⟹ degenerado. `n²` es **equivalente** a la hipótesis (T★). **D. Candidato Airy/Bessel REFUTADO para n² (IV.4) [hallazgo severo].**
El operador de concentración natural (prolato `P_c`, Landau–Widom) tiene borde **Airy** (`≍k^{2/3}`)
o **Bessel** (`≍k`) — **ninguno es `n²`**. El `n²` pertenece a un SL regular en intervalo finito,
otro operador. Mata la esperanza fácil "límite de prolato = n²". **Hueco honesto de IV.1 (los tres):** pinear el **potencial variable `V(x)`** (equivalentemente, la
tasa exacta del carrier `h(λ)=π−ω*(λ)`) por convergencia de resolvente. Es **análisis de capa de
borde duro, NO RH-hard**. `γ=3` sigue **sin derivarse** hasta identificar `V` (confirma C.4). --- ## SÍNTESIS UNÁNIME — la compresión > Los **cuatro** residuos analíticos abiertos del documento — `(H-gap)` uniforme, `(H-lim)`, la
> identificación del operador IV.1, y `γ=3` — **se comprimen en UN solo enunciado RH-neutral**:
> **(T★) = la familia `Â_λ` tiene escala de borde logarítmica no degenerada `h(λ)=π−ω*(λ)`**,
> del tipo asintótica de Landau–Widom. Probarlo cierra III (módulo signo) e IV.1 a la vez.
> El **muro RH** intacto y aislado: el **signo de ε₀** (= (H-pos) = IV.2≡§V). No se movió un mm. ## Lo asentado como demostración (resiste a los tres)
- **III.3-tamaño:** `|ε₀|=O(1/logλ)` incondicional [retira `ε₀~C/λ²` del maestro].
- **(H-lim) bajo tightness** incondicional (Prokhorov + resolvente).
- **III es RH-hard, como teorema:** uniformidad del gap ⟹ RH.
- **IV.1 inverso-de-Green:** la compacidad no obstruye; el límite es SL 2º orden, potencial `V` variable.
- **`n² ⟺ (T★)`** y **Airy/Bessel ≠ n²** (refuta candidato prolato).
- **Compresión:** 4 huecos → 1 hipótesis RH-neutral (T★, Landau–Widom). ## Lo que queda
- **Abierto no-RH-hard:** (T★) — identificar `V(x)` / la tasa `h(λ)` por capa de borde Landau–Widom. Cierra III (módulo signo), IV.1, `(H-gap)+(H-lim)` y `γ=3` de un golpe.
- **RH-hard (el muro):** signo de ε₀ = (H-pos) = IV.2≡§V. Irreductible, probado fuera del análisis. — A. · C. · H. (tribunal)
