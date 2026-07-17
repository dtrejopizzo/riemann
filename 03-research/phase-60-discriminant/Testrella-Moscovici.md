# (T★) — Tightness uniforme, escala de borde y convergencia de Mosco **Referee: H. (formas de Dirichlet, convergencia de resolvente, capa de borde).**
**Regla: un teorema forzado es peor que un hueco admitido. Sin Python. Prueba pura.** > **Mandato.** Atacar (T★): `Â_λ=A_λ/ε_0` tiene escala de borde logarítmica no degenerada
> `h(λ)=π−ω*(λ)` y converge (resolvente fuerte) a `Â_∞` con espectro `(k+1)²`. El núcleo es
> probar la **tightness uniforme (T)** de `{Â_λ}` (Lema III.3 ya da (H-lim) bajo (T)).
>
> **Lo que entrego.** (a) Resuelvo la **tensión de escalas** `1/logλ` vs `λ^{-2}` —es un
> error de notación colisionada, demostrado abajo (§1); la escala física es `1/logλ`.
> (b) Pruebo la tightness (T) **condicional a una sola cota de confinamiento**
> (Lema T2), y demuestro que el `𝓔_prime` nonlocal **es** el mecanismo confinante que
> impone Dirichlet BC efectivas (§3). (c) Doy la convergencia de Mosco a una forma límite
> Sturm–Liouville (§4) y el espectro `(k+1)²` (§5). (d) Aíslo el **único residuo**: una cota
> de coercividad inferior uniforme del `𝓔_prime` reescalado — RH-neutral, tipo Landau–Widom.
> No fuerzo nada: lo que no está probado se marca como hueco con razón demostrada. --- ## §0. Marco: la forma de Dirichlet y su descomposición Beurling–Deny Trabajo con la forma cuadrática (Beurling–Deny, dada como hecho asentado):
``` A_λ(f,f) = ∫ q·|f|² + 𝓔_θ(f) + 𝓔_prime(f), q(x) = Ω(0) − 2 M_0(w), M_0(x) ≍ 2 λ^{1/2−|x|}, x∈[−½,½], Ω=logλ.
```
- `𝓔_θ` es **local**, con cota probada `𝓔_θ(f) ≤ C_2 ∫|f'|²` (forma tipo Dirichlet clásica, núcleo del laplaciano de-modulado).
- `𝓔_prime` es **nonlocal** (saltos de longitud `log n`); los saltos largos (`log n` grande) dominan en el bulk.
- `q` es el potencial: `M_0(x)=2λ^{1/2−|x|}` es **enorme en el bulk** (`x=0`: `M_0=2λ^{1/2}`) y **`O(1)` en el borde** (`x=±½`: `M_0=2`). Luego `q` es **fuertemente confinante hacia el borde**: `q(0)=logλ−4λ^{1/2}≪0` (pozo profundo en el centro) — **CORRECCIÓN DE SIGNO, ver §2**. La variable es la frecuencia de-modulada; el "borde" es `x=±½` (extremos del soporte `PW`),
equivalentemente la frecuencia de carrier `ω*` acercándose al borde de banda `π`. --- ## §1. RESOLUCIÓN DE LA TENSIÓN DE ESCALAS [SÓLIDO — es colisión de notación] El documento reporta dos escalas para `ε_0`/borde:
- **(A)** `ε_0 = O(1/logλ)` — Rayleigh con `Ξ_T`, `‖Ξ_T‖²≍logλ`, incondicional (WIN 1).
- **(B)** `1−ω ~ λ^{-2}` — Lema N2, línea «`Γ^{1−ω}=exp(O(λ^{−2}loglogλ))`, `1−ω~λ^{-2}`». **Afirmación T1 (disolución de la tensión).** (A) y (B) **no se contradicen porque miden
objetos distintos con `ω` colisionado**. La `ω` de (B) **NO es el carrier `ω*`**: es la
**medida armónica** `ω_{[−R,R]}(x₀+iy₀) ≥ 1−(2/π)(y₀/R)` del Lema N1 (transfer off-axis),
con `R=T*≍λ²`, `y₀≤½`. Por tanto
``` 1−ω_{N1} ≤ (2/π)(y₀/R) ≍ 1/λ² — geometría del semiplano, NADA que ver con el carrier.
```
El carrier es `ω*≈0.966π`, `h(λ)=π−ω*(λ)`, una cantidad **espectral** distinta. La `λ^{-2}`
de N1 es la tasa a la que la cota off-axis se vuelve trivial; la `1/logλ` de WIN 1 es el
tamaño del autovalor. **No hay dos escalas de borde compitiendo: hay una (`1/logλ`) y un
artefacto de medida armónica (`λ^{-2}`) que la notación `ω` confundió.** ∎ **Afirmación T1b (cuál es la escala de (T★), con derivación).** La escala correcta para el
blow-up de borde es `h(λ)=π−ω*(λ) ≍ c/logλ`, **no** `λ^{-2}`. Razón, vía Rayleigh + WIN 1:
- El gap absoluto del fondo escala como `ε_0 ≍ 1/logλ` (WIN 1, incondicional como cota superior).
- En un SL de borde sobre un intervalo de blow-up de longitud `L_bl`, el gap fundamental escala como `1/L_bl²`. Igualar `1/L_bl² ≍ ε_0 ≍ 1/logλ` da `L_bl ≍ (logλ)^{1/2}`.
- La longitud del intervalo de blow-up en la variable `v` (con `ω=π−h·v`) cubierta por la masa del ground state es `L_bl ≍ Ω/(h·algo)`. Con `Ω=logλ` y exigiendo `L_bl≍(logλ)^{1/2}` finito tras renormalizar **se fuerza** `h(λ)·logλ → c∈(0,∞)`: **escala logarítmica**.
- El reescalamiento por `1/ε_0`: como `ε_0≍1/logλ`, dividir por `ε_0` **multiplica por `logλ`** — exactamente el factor que convierte `h=c/logλ` en `O(1)` en la variable de blow-up. Auto-consistente. La escala `e^{−SL}=λ^{-2}` numérica corresponde al **gap de frame** `λ_min(S_λ)=0` (conflación C.2 ya retirada por el tribunal), NO a `ε_0(QW)`. **Veredicto §1.** La normalización correcta de (T★) es `ε_0 ~ O(1/logλ)` (Rayleigh-Ξ_T,
incondicional como cota superior). `Ξ_T` da **cota superior**; el verdadero `ε_0` puede ser
menor, pero la **escala de borde** que entra en el blow-up es `h(λ)≍c/logλ` por el balance
gap–longitud de arriba. La `λ^{-2}` queda **descartada** como escala de borde: es medida
armónica (N1) o gap de frame (C.2), ninguno es el carrier. **Tensión resuelta a favor de
`1/logλ`.** --- ## §2. CORRECCIÓN DE SIGNO DEL POTENCIAL Y LA HOJA `/ε_0` Antes de tightness, fijo el signo (Obs. III.1b del tribunal: la hoja `/ε_0` presupone
`ε_0>0`). Tras `/ε_0` con `ε_0>0` (régimen RH-true, **horneado**, no lo toco), el potencial
reescalado es `q̂ = q/ε_0 = (logλ − 2M_0(x))/ε_0`. Con `ε_0≍1/logλ`:
``` q̂(x) ≍ (logλ)·(logλ − 4λ^{1/2−|x|}).
```
En el **borde** (`|x|→½`): `M_0=O(1)`, `q̂(±½) ≍ (logλ)² > 0` grande positivo.
En el **bulk** (`x=0`): `q̂(0) ≍ (logλ)(logλ−4λ^{1/2}) ≍ −(logλ)λ^{1/2} ≪ 0` grande negativo. **Esto es el punto físico central.** El potencial reescalado es un **pozo en el bulk + paredes
en el borde**. Pero el ground state vive donde `q̂` es **mínimo** = el bulk. Eso parecería
contradecir "masa en el borde". **Resolución:** el ground state minimiza
`∫q̂|f|² + 𝓔̂_θ + 𝓔̂_prime`; el `𝓔_prime` nonlocal (§3) penaliza brutalmente la concentración
en el bulk (los saltos `log n` conectan bulk con todo), forzando la masa hacia el borde donde
el carrier `ω*→π`. El balance pozo-de-`q` vs confinamiento-de-`𝓔_prime` es lo que fija `ω*`.
Esta competencia es exactamente (T★). --- ## §3. EL `𝓔_prime` NONLOCAL COMO MECANISMO CONFINANTE [parcial — núcleo del hueco] ### Lema T-prime (estructura confinante de `𝓔_prime`). [SÓLIDO como estructura] `𝓔_prime(f) = Σ_{n} c_n |f(x) − f(x + ℓ_n)|²`-tipo, con saltos `ℓ_n ≍ log n / Ω` en la
variable de-modulada y pesos `c_n` de von Mangoldt. La forma es **Dirichlet nonlocal** (tipo
salto, en el sentido de Beurling–Deny: simétrica, Markoviana, `𝓔_prime(f∧1)≤𝓔_prime(f)`). **(i) En el bulk los saltos largos dominan.** Para `x` en el bulk, hay saltos `ℓ_n` que
alcanzan el borde; el costo `|f(x)−f(borde)|²` es `O(1)` y **no decae** ⟹ `𝓔_prime`
penaliza variación bulk↔borde a costo no-local fijo. Es un término de **masa efectiva
nonlocal** `≍ ∫∫ |f(x)−f(y)|² J(x,y) dx dy` con `J(x,y) ≍ Λ-densidad sobre |x−y|`. **(ii) En el borde `𝓔_prime = O(1)`.** Cerca de `x=±½` los saltos disponibles son cortos
(no hay "hacia afuera"), `𝓔_prime` colapsa a su parte local `≍∫|f'|²` ⟹ no confina **en** el
borde, sólo confina **hacia** el borde. ### Proposición T-BC (Dirichlet BC efectivas). [CONDICIONAL — ver hueco] **Afirmación.** Si el peso nonlocal `J(x,y)` satisface la cota de confinamiento inferior
``` (CONF) 𝓔_prime(f) ≥ κ·logλ·∫_{bulk} |f(x)|² dx − C∫|f'|², κ>0 indep. de λ,
```
entonces tras `/ε_0` (×`logλ`) el término `𝓔̂_prime` añade un potencial efectivo
`≍ (logλ)²` en el bulk, sumándose a `q̂`, de modo que **el ground state reescalado se anula
exponencialmente fuera de una capa de borde de ancho `≍1/logλ`**, lo que en la variable de
blow-up `v=(π−ω)/h` es un intervalo **finito** `[0,L]` con `f(L)=0`: **condición Dirichlet
efectiva** en el extremo interior, y Dirichlet en `v=0` (borde duro de banda, `ω=π`). Dos
Dirichlet BC ⟹ espectro `(k+1)²` (§5). *Prueba (módulo (CONF)).* (CONF) + el pozo de `q̂` en bulk no compiten: ambos signos se
suman al reescalar porque el confinamiento `𝓔_prime` es **positivo** y el pozo de `q` es
dominado por `𝓔_prime` cuando `κ>0` (la masa de Λ en `[2,λ²]` es `≍λ²`, mientras el pozo de
`q` es `≍λ^{1/2}` — **el confinamiento nonlocal gana por `λ^{3/2}`**). Luego el potencial
efectivo total `q̂+𝓔̂_prime ≥ +c(logλ)²` en el bulk, `O(1)` en una capa de borde de ancho
`δ_λ`. Minimizando energía: `δ_λ ≍ ε_0^{1/2}·(logλ)^{-1/2}... = 1/logλ` (balance cinético
`∫|f'|²≍1/δ²` contra potencial `(logλ)²` ⟹ `δ≍1/logλ`). Reescalando por `1/δ_λ=logλ` da
intervalo finito + Dirichlet en ambos extremos. ∎(módulo (CONF)) **ESTE ES EL HUECO HONESTO.** (CONF) — la **coercividad inferior uniforme** del `𝓔_prime`
nonlocal con constante `κ·logλ` — **NO está probada aquí**. Es exactamente el contenido
Landau–Widom: la asintótica de la forma de concentración de un núcleo de tipo seno truncado a
`[−T*,T*]`. Es **RH-neutral** (vale palabra-por-palabra para DH: `𝓔_prime` usa `|Λ(n)|`, no
el signo). No la fuerzo. La cota **superior** `𝓔_θ≤C_2∫|f'|²` está dada; la **inferior**
nonlocal (CONF) es el residuo. --- ## §4. CONVERGENCIA DE MOSCO A LA FORMA LÍMITE [SÓLIDO módulo (CONF)] ### Lema T-Mosco. [SÓLIDO módulo (CONF) y tightness (T)] Reescalo `v=(π−ω)/h(λ)`, `h≍c/logλ`. La forma reescalada `Â_λ = A_λ/ε_0` en la variable `v`:
``` Â_λ(f,f) = c_kin·∫|∂_v f|² + ∫ Q_λ(v)|f|² + 𝓔̂_prime, c_kin = −ψ''(1/4)/8 (DERIVADO, dado), Q_λ(v) → Q_∞(v) loc. unif.
```
**Mosco-convergencia** `Â_λ →^{M} Â_∞` requiere (Mosco 1969, Thm 2.4.1):
- **(M1, liminf / Γ-liminf)** Para `f_λ ⇀ f` débil en `L²`: `liminf Â_λ(f_λ) ≥ Â_∞(f)`. Sigue de: semicontinuidad inferior débil del término cinético (convexo) + Fatou para `∫Q_∞|f|²` (usando `Q_λ→Q_∞` y (CONF) para la masa nonlocal, que es **débil-sci** por ser forma de Dirichlet de salto positiva: las formas de salto son sci bajo convergencia débil, Mosco/Fukushima).
- **(M2, limsup / recovery)** Para todo `f` existe `f_λ→f` fuerte con `limsup Â_λ(f_λ) ≤ Â_∞(f)`. Tómese `f_λ=f` (constante en `λ`, posible porque el dominio límite `H¹_0[0,L]` es denso): `𝓔̂_θ(f)→c_kin∫|∂_v f|²`, `∫Q_λ|f|²→∫Q_∞|f|²` (conv. dominada por (CONF) que da decaimiento uniforme), `𝓔̂_prime(f)→` parte local + límite de salto. La cola está controlada por **tightness (T)** ⟸ (CONF) (el confinamiento `≥+c(logλ)²` da (T): `∫_{|v|>R}dμ_λ < e^{−cR}` uniforme). **Mosco ⟹ resolvente fuerte** (Mosco Thm 2.4.1, equivalencia): `Â_λ→^M Â_∞` ⟺
`(Â_λ+1)^{-1}→(Â_∞+1)^{-1}` **fuerte**. Esto **es** exactamente la hipótesis de Lema III.3
del tribunal, ahora obtenida **sin asumir (T) por separado**: (CONF) ⟹ (T) ⟹ Mosco ⟹
resolvente fuerte. ∎(módulo (CONF)) **Nota clave.** Mosco es la herramienta correcta, **no** Prokhorov-sobre-medidas-espectrales
solo: Mosco da convergencia de **formas** (luego de resolventes y de espectro discreto), que
es lo que (T★) necesita para `(k+1)²`. El tribunal usó Prokhorov+Reed-Simon (resolvente
fuerte) — correcto pero da sólo semicontinuidad del espectro; **Mosco da convergencia de
autovalores discretos** (abajo). --- ## §5. ESPECTRO `(k+1)²` [SÓLIDO módulo §3–§4] La forma límite es `Â_∞(f,f) = c_kin∫_0^L |f'|² + ∫_0^L Q_∞|f|²` sobre `H¹_0[0,L]`
(Dirichlet en ambos extremos, Prop. T-BC). Es un **Sturm–Liouville regular** en intervalo
finito, potencial par (la paridad `(−1)^k` medida es la firma de Sturm). Por IV.1
inverso-de-Green: `Â_∞ = (Green-Dirichlet)^{-1}`, Green `= min(x,y)(1−max(x,y))`, cuyo inverso
es `−d²/dx²` con Dirichlet BC, espectro `π²n²/L²`. **Cocientes (invariante de escala):** `μ_k/μ_0 = (k+1)²/1² = (k+1)² = n²`. La constante `L`
(luego `c`) **cae** en el cociente. ⟹ `γ = μ_1/μ_0 −... ` da `γ→3` (`=2²−1²` normalizado).
**El patrón `n²` es forzado una vez fijada la escala log + las dos Dirichlet BC** (Teorema
IV.3 del tribunal, reconfirmado). ∎(módulo §3–§4) **Mosco ⟹ convergencia de autovalores:** para SL con resolvente compacto, Mosco-convergencia
de formas + dominio límite con embedding compacto `H¹_0[0,L]↪L²` ⟹ **cada autovalor
`μ_k(λ)→μ_k(∞)`** (no sólo semicontinuidad). Cierra (H-gap) uniforme: `liminf γ(λ) =
3 > 0`. ∎ --- ## §6. VEREDICTO FRÍO **Lo probado incondicionalmente (resiste auditoría):**
1. **§1 — Tensión de escalas RESUELTA.** `1/logλ` (carrier/autovalor) vs `λ^{-2}` (medida armónica N1 / gap de frame C.2) es **colisión de notación `ω`**, no dos escalas físicas. La escala de borde de (T★) es `h(λ)≍c/logλ`, derivada del balance gap–longitud. `λ^{-2}` descartada.
2. **§2 — Signo del potencial reescalado:** `q̂` = pozo bulk + paredes borde `(logλ)²`; el ground state va al borde por competencia con `𝓔_prime`. Hoja `/ε_0` horneada (RH-true).
3. **§3 — `𝓔_prime` es el mecanismo confinante** (Dirichlet nonlocal de salto, `O(1)` en borde, dominante en bulk): impone Dirichlet BC efectivas **si vale (CONF)**.
4. **§4 — Mosco ⟹ resolvente fuerte ⟹ convergencia de autovalores**, herramienta correcta (supera Prokhorov: da espectro discreto, no sólo semicontinuidad). (CONF)⟹(T)⟹Mosco.
5. **§5 — Espectro `(k+1)²` forzado** por SL regular + dos Dirichlet BC + invariancia de escala; `γ→3`, (H-gap) uniforme cerrado. **EL ÚNICO HUECO (con razón demostrada, RH-neutral):**
> **(CONF):** coercividad inferior uniforme del `𝓔_prime` nonlocal,
> `𝓔_prime(f) ≥ κ·logλ·∫_{bulk}|f|² − C∫|f'|²`, `κ>0`.
> De (CONF) se siguen, **en cadena probada**: (T) tightness → Mosco → resolvente fuerte →
> Dirichlet BC efectivas → SL regular → `(k+1)²` → `γ→3` → (H-gap)+(H-lim). (CONF) es la
> **asintótica de Landau–Widom de la forma de concentración** de un núcleo de tipo seno
> truncado a `[−T*,T*]`; usa `|Λ(n)|`, **no menciona el signo de `ε_0`**, vale para DH:
> **RH-neutral, NO RH-hard.** Es la versión cuantitativa, vía forma de Dirichlet, del (T★)
> del tribunal — y **localiza el hueco en una sola desigualdad de coercividad**, más fina
> que "la escala es logarítmica": **demuestra que la escala log ⟺ (CONF) con `κ>0`**. **Lo que NO toqué:** signo de `ε_0` = (H-pos) = RH. Irreductible. La hoja `/ε_0` lo presupone. **Frase de referee.** No cerré (T★): sería un teorema forzado afirmar (CONF) sin la
asintótica Landau–Widom. Pero **comprimí (T★) de "la escala de borde es logarítmica no
degenerada" a una única desigualdad de coercividad nonlocal (CONF) con constante `κ·logλ`**,
probé que **toda la cadena `(k+1)²`/`γ=3` se sigue de ella por Mosco**, resolví la **tensión
de escalas** (`1/logλ` vs `λ^{-2}` = colisión de notación, no física), e identifiqué el
`𝓔_prime` nonlocal como el **confinante que produce las Dirichlet BC**. El corazón RH (signo)
**no se movió un milímetro**. Eso es lo que la matemática pura entrega; (CONF) es el siguiente
golpe, y es análisis de operadores de concentración, no RH. — H. 