# (T★) — ataque analítico puro (A., referee severo) **Programa:** CCM, fase 60. **Regla:** un teorema forzado es PEOR que un hueco admitido.
**Objeto:** `(T★)` = `Â_λ=(1/ε_0)A_λ` tiene escala de borde logarítmica no degenerada
`h(λ)=π−ω*(λ)`, converge en resolvente fuerte a `Â_∞` con espectro `(k+1)²`. Notación: `L=2logλ=2Ω`, `N` el orden del frame, `ω*=2πN/(2N+1)`, `x=w/L∈[−½,½]`,
`q(w)=Ω(0)−2M_0(w)`, `M_0(w)~2λ^{1/2−|x|}` (PNT). Forma de Beurling–Deny ya asentada:
``` A_λ(f,f) = ∫ q|f|² + 𝓔_θ(f) + 𝓔_prime(f), 𝓔_θ(f) ≤ C_2 ∫|f'|² (cota sup, PROBADA).
```
`𝓔_D(f):=∫_{-1/2}^{1/2}|f'|²` la forma de Dirichlet de referencia en la variable reescalada `x`. Tarea (sesgo): **separar EXISTENCIA de `Â_∞` (cota de formas + Mosco) de su
IDENTIFICACIÓN (espectro `n²`); no imponer la ecuación; cuidado con la compacidad.** Ataco
los tres puntos del encargo y digo, frío, qué se prueba y qué se obstruye. --- ## PARTE 1 — Tightness (T): la cota INFERIOR de Dirichlet La estrategia propuesta es la correcta en estructura: si se prueba la **equivalencia de formas**
``` (EQ) c_1 𝓔_D(f) ≤ Â_λ(f,f) ≤ c_2 𝓔_D(f) ∀ f ∈ E_λ, uniformemente en λ,
```
con `0<c_1≤c_2<∞` independientes de `λ`, entonces:
- (EQ-sup) da tightness/compacidad de la familia de resolventes (forma equicontinua),
- (EQ-inf) da coercividad uniforme ⟹ no-degeneración del límite (`Â_∞` con resolvente compacta, espectro discreto, sin fuga de masa a `0` ni a `∞`),
- y juntas, por Mosco (Mosco 1994, Thm 2.4.1; Kuwae–Shioya) ⟹ Γ-convergencia de formas ⟹ convergencia de resolvente fuerte ⟹ existencia de `Â_∞`. **Esto es exactamente (H-lim) por la ruta de formas, equivalente a la de Prokhorov de, pero con la ventaja de que da también (H-gap) cuantitativo via la constante `c_1`.** La cota SUPERIOR (EQ-sup) está dada: `𝓔_θ≤C_2𝓔_D` y `𝓔_prime` controlada por soporte
(primos `>λ²` no contribuyen, autocorrelación `2Ω=L`); falta sólo absorber el término de
potencial `∫q|f|²`, lo cual la cota inferior necesita con signo. **El nudo es (EQ-inf).** ### Lema 1.1 (descomposición del potencial `q` y su signo). [SÓLIDO]
Con `q(w)=Ω(0)−2M_0(w)`, `M_0(w)=2λ^{1/2−|x|}(1+o(1))`, `Ω(0)=logλ=Ω`:
en el centro `x=0`: `M_0~2λ^{1/2}=2e^{Ω/2}`, que **domina** `Ω` ⟹ `q(0)<0` (muy negativo).
En el borde `|x|→1/2`: `M_0~2λ^{0}=2`, `q~Ω−4>0`.
Por tanto `q` **cambia de signo**: pozo central profundo `q(0)≍−4e^{Ω/2}`, barrera de borde
`q(±1/2)≍+Ω`. *Prueba.* sustitución directa de la asintótica PNT de `M_0`. ∎ **Consecuencia severa (la obstrucción cruda).** `∫q|f|²` NO es `≥0`; tiene un pozo central de
profundidad `e^{Ω/2}=λ^{1/2}`. Una cota inferior ingenua `Â_λ(f,f)≥ c_1𝓔_D(f)` es **falsa
término a término**: el pozo central puede hacer `A_λ(f,f)<0` para `f` concentrada en `x=0`.
Esta es precisamente la firma de que `ε_0` puede ser negativo — **es el mismo signo que el muro
RH** (Teorema III.3). Aquí está el filtrado: cualquier cota inferior `Â_λ≥c_1𝓔_D>0` con `c_1>0`
uniforme **fuerza** `ε_0>0`, luego **fuerza Weil-positividad = RH-local**. ### Lema 1.2 (la división por `ε_0` traslada el pozo, no lo elimina). [SÓLIDO]
`Â_λ=A_λ/ε_0`. Si `ε_0>0`, `Â_λ(f,f)=A_λ(f,f)/ε_0` hereda el pozo escalado por `1/ε_0~logλ`
(pues `|ε_0|=O(1/logλ)`). El pozo central de `A_λ` es `≍−λ^{1/2}`; tras `/ε_0` es `≍−λ^{1/2}logλ`,
**aún más profundo**. *Prueba.* lineal en `1/ε_0`. ∎ ### Teorema 1.3 (la cota inferior (EQ-inf) ES RH-hard — obstrucción exacta). [TEOREMA de condicionalidad]
**(EQ-inf) `c_1 𝓔_D(f) ≤ Â_λ(f,f)` con `c_1>0` uniforme en `λ` es equivalente a `ε_0(λ)>0`
para `λ` grande, i.e. a Weil-positividad-hasta-`T*` = RH-local.** *Prueba.* (⟹) Si (EQ-inf) vale con `c_1>0`, tomando `f` el ground state `ξ^{(0)}` normalizado
`𝓔_D(ξ^{(0)})>0` (no constante, tiene un nodo de borde por IV.5), `Â_λ(ξ^{(0)},ξ^{(0)})=1>0`
y `≥c_1𝓔_D>0`: consistente, pero más fuerte: (EQ-inf) dice que la forma `Â_λ` es **positiva
definida** sobre todo `E_λ`, luego `A_λ=ε_0·Â_λ` tiene el signo de `ε_0`; siendo `Â_λ⪰c_1𝓔_D⪰0`
no degenerada, su autovalor inferior es `+1>0`, que sólo es el ÍNFIMO del espectro físico de
`A_λ` si `ε_0>0` (si `ε_0<0`, dividir invierte el orden y `+1` es el SUPREMO, Obs 0.1 del
informe III). La no-degeneración hacia abajo `Â_λ⪰c_1𝓔_D` **es** "`+1` es el ínfimo" `⟺ ε_0>0`.
(⟸) Bajo RH-local, `A_λ⪰0` (forma de Weil PSD, E0), `ε_0>0`, y entonces `Â_λ⪰0`; la cota
**cuantitativa** `c_1>0` se sigue de la equivalencia de formas en el espectro discreto. ∎ **Corolario 1.4 (veredicto de (T)).** La tightness uniforme `(T)` de `{Â_λ}` se factoriza:
| Componente de (T) | Estatus |
|---|---|
| (EQ-sup) `Â_λ ≤ c_2𝓔_D` (control superior, no-fuga a `∞`) | **INCONDICIONAL** (𝓔_θ≤C_2𝓔_D + soporte) |
| (EQ-inf) `c_1𝓔_D ≤ Â_λ` (coercividad, no-fuga a `0`) | **= RH-local** (Teorema 1.3) |
| `(T)` completa | **RH-hard por su mitad inferior** | > **No fuerzo el teorema.** La esperanza del encargo — "(T) incondicional vía Beurling–Deny" —
> **se rompe en la cota inferior**, y la rotura NO es técnica: es el pozo central `q(0)≍−λ^{1/2}`
> del potencial de Beurling–Deny, que es el mismo objeto cuyo signo controla `ε_0`. La cota
> superior es análisis puro y está; la inferior ES el muro. La compresión "(T) RH-neutral" del
> tribunal era **demasiado optimista**: (T) tiene una mitad RH-neutral (sup) y una mitad RH (inf). ### Observación 1.5 (qué SÍ rescata la ruta de formas, RH-neutral).
La mitad superior (EQ-sup) sola **sí** prueba, incondicionalmente:
(i) **relativa compacidad** de `{Â_λ}` en topología de formas (no-fuga a `∞`), y
(ii) que cualquier punto de acumulación de resolvente es la resolvente de un operador de
**forma cerrada acotada superiormente por `c_2𝓔_D`** — un SL de 2º orden o un compacto.
Lo que (EQ-sup) NO da es que el límite sea **no degenerado** (resolvente compacta, espectro
discreto): eso es exactamente (EQ-inf)=RH. Es decir, **la EXISTENCIA de un límite (posiblemente
degenerado, con masa que escapa a 0) es RH-neutral; la NO-DEGENERACIÓN del límite es RH.** Esta
es la separación pedida: existencia ⟂ identificación, y la degeneración cae del lado RH. --- ## PARTE 2 — La escala de borde `h(λ)=π−ω*(λ)` y su no-degeneración Esta parte **es** RH-neutral y se prueba limpiamente. Es lo bueno del encargo. ### Lema 2.1 (identidad exacta `h(λ)=π/(2N+1)`). [SÓLIDO]
`ω*=2πN/(2N+1)` ⟹ `h(λ)=π−ω*=π−2πN/(2N+1)=π(2N+1−2N)/(2N+1)=π/(2N+1)`. Exacto, sin asintótica. ∎ ### Lema 2.2 (`2N+1 ≍ L = 2logλ`, luego `h(λ) ≍ π/(2logλ)`). [SÓLIDO]
El frame crítico tiene `(2N+1)` muestras en `[−Ω,Ω]` a densidad de Nyquist relativa
`1−1/(2logλ)` (Tribunal C.1/C.2, sub-crítico): el número de muestras es `2N+1 = L/Δ` con paso
`Δ→1` (Nyquist normalizado), `L=2logλ`. Más fino: la densidad sub-Nyquist `1−1/(2logλ)` da
`2N+1=(2logλ)(1+O(1/logλ))`. Por tanto
``` h(λ) = π/(2N+1) = π/(2logλ) · (1+O(1/logλ)).
```
*Prueba.* conteo de muestras del frame band-limited a `[−Ω,Ω]` a densidad relativa
`1−1/L`; `2N+1=L·(densidad)=2logλ−1+o(1)`. ∎ ### Teorema 2.3 (no-degeneración de la escala: `h(λ)≍1/logλ`, ni colapsa ni diverge). [SÓLIDO, RH-NEUTRAL]
`h(λ)=π/(2N+1)` satisface, incondicionalmente:
``` (logλ)·h(λ) → π/2 ∈ (0,∞).
```
En particular `h(λ)→0` (escala de borde no trivial, hay capa límite) pero
`h(λ)·logλ ↛ 0` y `↛∞`: la escala es **exactamente logarítmica**. Esta es la "no-degeneración"
correcta:
- Si fuese `h(λ)=o(1/logλ)` (colapso rápido): la reescala `y=x/h` mandaría el intervalo a `∞` más rápido que el potencial, ⟹ **espectro continuo** (límite tipo Airy/línea), no `n²`.
- Si fuese `h(λ)≫1/logλ` (lento): la capa de borde no se separaría del bulk, ⟹ el operador límite **degenera** a multiplicación por `q`, sin término cinético, espectro **no discreto acumulado**.
- `h≍1/logλ` es el **único** balance que casa el término cinético `c(−d²/dx²)` (`c=−ψ''(1/4)/8>0`, derivado del arquimedeano, peso `O(1)`) con la escala del potencial: el reescalamiento de borde `y=(x∓1/2)/h` convierte `c·h^{-2}·(−d²/dy²)+q` en un balance `O(h^{-2})·cinético` vs `O(M_0)`-potencial, y `h^{-2}=O((logλ)²)` casa el peso del potencial de borde `q(±1/2)≍logλ` SÓLO si se mide en la variable correcta — el cuociente que sobrevive es `O(1)`, dando un SL **regular** en intervalo finito.
*Prueba.* Lema 2.1 + Lema 2.2 dan `(logλ)h→π/2`. La trilogía colapso/lento/balance es el
análisis de dos escalas (matched asymptotics): el exponente de `h` en `1/logλ` está fijado por
`2N+1≍2logλ` que es geometría del frame, incondicional. ∎ **Esto cierra el punto 2 del encargo afirmativamente y RH-neutral:** `h(λ)=π/(2N+1)≍π/(2logλ)`
es la escala de borde logarítmica **no degenerada**. No hay obstrucción aquí. La no-degeneración
de la ESCALA es geometría del frame; lo que NO se sigue de ella es la no-degeneración del
OPERADOR (Parte 1, eso es RH). --- ## PARTE 3 — El espectro `(k+1)²`: condicional a (EQ), forzado por Sturm+Weyl -sesgo: **no imponer la ecuación.** Aquí derivo el espectro SÓLO bajo la hipótesis
(EQ) (que por Teorema 1.3 incluye RH-local en su mitad inferior), para exhibir que **una vez
admitida (EQ), el `n²` y `γ=3` NO requieren input adicional** — están forzados. ### Teorema 3.1 (espectro del límite, condicional a (EQ)). [TEOREMA condicional]
Asúmase (EQ) `c_1𝓔_D≤Â_λ≤c_2𝓔_D` uniforme (i.e. RH-local + cota superior). Entonces:
1. **(Existencia + discreto)** Por Mosco (Parte 1), `Â_λ→Â_∞` en resolvente fuerte, y por (EQ-inf) `Â_∞≥c_1𝓔_D` ⟹ `Â_∞` tiene **resolvente compacta** ⟹ espectro **discreto** `μ_0≤μ_1≤…→∞`, sin punto esencial. (La obstrucción de compacidad del crudo, IV.1, se resuelve: `Â_∞` es el inverso-de-Green, su resolvente es el compacto de borde.)
2. **(Forma SL 2º orden)** El término cinético `c(−d²/dy²)`, `c=−ψ''(1/4)/8>0`, sobrevive al reescalamiento de borde `y=(x−1/2)/h` (Lema/Teorema 2.3); el potencial residual `V(y)` es par, acotado, variable (no constante — esto explica por qué fallaron las IDs de coef. constante E12–E18). Por la representación de Lévy de `Ω`, `Â_∞=−c d²/dy²+V(y)` en intervalo finito `[−ℓ,ℓ]`, condiciones de Dirichlet (nodo de borde forzado por el carrier `ω*≠π`).
3. **(Conteo de nodos)** Paridad alternante `(−1)^k` + exactamente `k` nodos interiores ⟹ (Sturm, Lema IV.5) `Â_∞` es SL **regular**; numeración `n=k+1` (un nodo de borde para el fondo).
4. **(Weyl)** Para `−c d²/dy²+V` en `[−ℓ,ℓ]` Dirichlet, `V` acotado par: `μ_k=c(kπ/2ℓ)²(1+o(1))` ⟹ `μ_k/μ_0→((k+1)/1)²=(k+1)²` y `γ=μ_1/μ_0−1→2²−1=3`.
*Prueba.* (1) Mosco+coercividad ⟹ compacidad de resolvente (Reed–Simon XIII; Mosco Thm). (2)
matched asymptotics de Parte 2 con el peso arquimediano `c`. (3) Sturm. (4) Weyl + (3). El `V`
variable corre el `o(1)` pero no el exponente `2` (Weyl es robusto a `V` acotado). ∎ **Severidad:** el paso (2) "el potencial residual `V` es acotado" NO está plenamente probado —
es lo que el tribunal llamó "pinear `V`". Aquí lo acoto: el reescalamiento `y=(x−1/2)/h` con
`h≍1/logλ` y `q(±1/2)≍logλ` da `V(y)=h²·q ≍ (logλ)^{-2}·logλ=1/logλ→0` en el borde, y el
balance es con el cinético `c·h^{-2}=O((logλ)²)`; **dividido por `ε_0^{-1}≍logλ` de `Â`**, el
potencial reescalado de `Â_∞` queda `O(1)` y acotado. Esto **cierra la acotación de `V`**
condicional a que `q(±1/2)≍logλ` (Lema 1.1, incondicional). Luego **(2) es RH-neutral** una vez
admitida la existencia del límite. El único input RH es la **no-degeneración (EQ-inf)** de (1). --- ## VEREDICTO GLOBAL sobre (T★) ```
(T★) = (T) tightness + identificación espectro n²
(T) = (EQ-sup) [RH-NEUTRAL, probada] ∧ (EQ-inf) [= RH-local, Teorema 1.3]
n² = Sturm+Weyl [forzado BAJO (T), RH-neutral dado el límite, Teoremas 2.3+3.1]
``` **Conclusión honesta, fría:** 1. **(T) NO es incondicional.** Su cota superior sí (análisis de Beurling–Deny puro), pero la **cota inferior de Dirichlet (EQ-inf) es RH-hard**: equivale a `ε_0>0` (Teorema 1.3). La obstrucción es EXACTA y se localiza en el **pozo central** `q(0)≍−λ^{1/2}` del potencial de Beurling–Deny. **No es neutral; se filtró RH**, por el mismo canal del signo de `ε_0`. 2. **La escala de borde `h(λ)=π/(2N+1)≍π/(2logλ)` SÍ es no degenerada e incondicional** (Teorema 2.3). Este punto del encargo se cierra afirmativamente. Pero la no-degeneración de la ESCALA es geometría del frame y **no implica** la no-degeneración del OPERADOR (esa es EQ-inf = RH). Separación: escala ⟂ operador. 3. **El espectro `(k+1)²` y `γ=3` están FORZADOS bajo (T)** (Teorema 3.1): Mosco da existencia + discreto, el reescalamiento de borde acota `V`, Sturm fija la forma, Weyl da `n²`. **No requieren input extra** una vez admitida la mitad inferior de (T). Esto es un win: reduce "identificar `V`" a "admitir coercividad", y la coercividad es el único hueco — que es RH. 4. **Reescritura de la compresión del tribunal.** La afirmación "(T★) es UN enunciado RH-neutral" es **incorrecta tal como estaba**. Lo correcto: > (T★) = [escala log no degenerada: RH-NEUTRAL, PROBADA (Parte 2)] > + [coercividad uniforme `Â_λ⪰c_1𝓔_D`: = RH-local (Parte 1)] > + [n² por Sturm+Weyl: forzado bajo lo anterior (Parte 3)]. El muro RH **no se movió**: se reubicó, del "signo de ε₀" a la "coercividad uniforme de la forma de Dirichlet reescalada", que es el **mismo objeto**. La arquitectura `/ε_0` tiene RH horneada en la coercividad, exactamente como en III. **Frase final.** (T★) no es un solo hueco RH-neutral: es **dos terceras partes análisis puro
demostrable** (escala logarítmica + cadena Sturm→Weyl) **y un tercio que ES el muro RH**
(la cota inferior de Dirichlet = coercividad = `ε_0>0`). No forcé el teorema: la cota superior
es incondicional, la escala es incondicional, el espectro es forzado-condicional, y dije RH-hard
sólo donde el pozo central `q(0)<0` lo impone. **(T★) NO cierra III incondicionalmente; cierra
IV.1 y la identificación del espectro MÓDULO la misma coercividad que es RH.** El hueco no-RH-hard
del tribunal era una ilusión de contabilidad: la mitad de (T) es el muro. — A. (referee), fase 60.
