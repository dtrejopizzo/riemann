# III y IV.1 — Análisis de perturbación y operador de borde **Referee: H. (operadores, perturbación, de Branges / Hermite–Biehler).**
**Regla:** un teorema forzado es peor que un hueco admitido. Sin Python. Prueba pura. > **Tesis del documento.** III pide un análisis de perturbación (Davis–Kahan en `Â=A/ε_0`)
> que necesita (H-gap), (H-lim), (H-pos). IV.1 pide identificar el operador límite `Â_∞`
> con espectro `(k+1)²=n²`, sabiendo que el Loewner crudo es **compacto**.
>
> **Lo que entrego abajo:** (a) la teoría de perturbación se rehace correctamente; (b) se
> **prueba incondicionalmente** la existencia del límite de escala (H-lim) **bajo una
> hipótesis de tightness explícita y RH-neutral** (Lema III.3), separando limpiamente
> "existe límite" de "el signo de ε_0"; (c) se demuestra que **sin tightness uniforme el
> límite puede no existir**, y que la tightness uniforme es exactamente lo que falta;
> (d) para IV.1 se **formaliza el blow-up de borde** y se demuestra el **teorema de
> obstrucción exacto**: el reescalamiento singular que convertiría el compacto en
> diferencial existe formalmente, pero la potencia de blow-up que produce `n²` **no es
> derivable de la estructura finita** sin un input de tipo Landau–Widom que es justo el
> hueco. Doy la razón demostrada, no fenomenología. --- ## Parte 0 — Marco preciso de la perturbación Fijo notación de operadores. `Q_λ:= QW(λ,N)` con `N=N(λ)→∞` ya tomado (el límite `N`
está probado, E2.a). `Q_λ` es real simétrica sobre `H_λ:= ℝ^{2N+1}≅PW_Ω` con la norma
`L²` band-limited. Autovalores `ε_0(λ)≤ε_1(λ)≤…`, autovectores `ξ^{(0)},ξ^{(1)},…`
ortonormales. `ε_0=ε_0(λ)` es el fondo; `ξ:=ξ^{(0)}` el ground state; `ξ̂` su transformada
secular. **Hechos asentados (no re-derivo):**
- (F1) `Q_λ` = forma de Weil restringida a `PW_Ω` (identidad variacional, tribunal B.4).
- (F2) `ε_0>0 ⟺` Weil-positividad-hasta-`T* ⟺` RH-hasta-`T*` (H1′, tribunal). **Signo = RH.**
- (F3) `ξ^{(0)}` par y simple a cada `λ` finito ⟹ `ε_1(λ)>ε_0(λ)` **estricto** (B.3).
- (F4) El núcleo de Loewner crudo `K_λ` (operador integral cuyo símbolo es la diferencia-dividida de seno) es **compacto** y suavizante (tribunal, C.4). Toda la dificultad de III está en distinguir **tres** cosas que el documento mezcla: | objeto | qué controla | estado |
|---|---|---|
| `γ(λ)=ε_1/ε_0−1` a `λ` fijo | aislamiento del fondo a escala finita | **>0 probado** (F3) |
| `liminf_λ γ(λ)` | que Davis–Kahan no degenere en el límite | **abierto** |
| `signo ε_0` | RH | **RH-hard** (F2) | La afirmación central de esta nota: **las dos primeras filas son separables del signo, y la
primera fila tiene contenido incondicional. La segunda fila NO es regalo de la estructura
finita** — y demuestro por qué. --- ## Parte I — Perturbación relativa rigurosa (III) ### Lema III.1 (Davis–Kahan relativo correcto). [SÓLIDO, incondicional] Sean `Â_λ=Q_λ/ε_0(λ)` (suponiendo `ε_0≠0`; ver Obs. III.1b para el signo) y un operador
límite candidato `Â_∞` autoadjunto con fondo simple aislado, espectro restante en
`[1+γ_∞,∞)`, `γ_∞>0`. Sea `P_λ`, `P_∞` los proyectores espectrales sobre el fondo. Entonces
``` ‖P_λ − P_∞‖ ≤ ‖(Â_λ − Â_∞) P_∞‖ / dist(1, spec(Â_λ)∖{1}).
```
Si `liminf_λ dist(1,spec(Â_λ)∖{1}) ≥ δ_0>0`, entonces
``` ‖P_λ − P_∞‖ ≤ δ_0^{-1} ‖Â_λ − Â_∞‖_{low} (low = restringido al rango relevante).
``` *Prueba.* Davis–Kahan `sinΘ` estándar para perturbación de subespacios invariantes de un
operador autoadjunto con gap. La normalización `/ε_0` lleva el fondo a `1` exactamente y el
gap absoluto `ε_1−ε_0` al gap relativo `γ=ε_1/ε_0−1`. La hipótesis de gap es sobre `Â`, no
sobre `Q`; el gap absoluto microscópico `ε_1−ε_0≈3ε_0` es irrelevante una vez dividido. ∎ **Observación III.1b (el signo está horneado).** `Â_λ=Q_λ/ε_0` está **mal definido si
`ε_0=0`** y **cambia de hoja si `ε_0<0`**. Si `ε_0<0` (RH-falsa-hasta-`T*`), el fondo de
`Â_λ` está en `+1` pero `Â_λ` no es positivo: `spec(Â_λ)` baja **por debajo** de `1` (los
modos con `ε_k<0` mapean a `ε_k/ε_0>1` si `ε_k<0`, y a negativos si `ε_k>0`). La hoja entera
de la teoría de perturbación presupone `ε_0>0`. **Confirmo la agravante de (tribunal,
III): toda la arquitectura `/ε_0` presupone régimen RH-true.** Esto NO es subsanable; es
parte de (H-pos). Lema III.1 es correcto **como implicación condicional**, no más. ### Lema III.2 (cota de estabilidad con el gap relativo). [SÓLIDO, módulo (H-gap)] Bajo `liminf γ(λ)≥γ_0>0` y existencia de `Â_∞` (siguiente lema),
``` ε_loc(λ) ≤ (C/γ_0)·√(logλ)·‖Â_λ−Â_∞‖_{low} + Cλ³e^{−πλ²}.
``` *Prueba.* `‖ξ̂_λ−ξ̂_∞‖_{L²}≲‖P_λ−P_∞‖` (Lema III.1) `≲γ_0^{-1}‖Â_λ−Â_∞‖`. Pasar de `L²` a
`sup` band-limited cuesta `√(logλ)` por Nikolskii/Plancherel–Pólya (N2, ahora con el factor
honesto `O(logλ)^{1/2}`, **no** `O(1)`). El término doble-exponencial es N0. ∎ Esto es exactamente el Teorema condicional III del documento, **con las hipótesis
correctamente expuestas**. No añade ni quita carga RH. El trabajo real está en **(H-lim)**. --- ### El núcleo analítico de III: ¿existe `Â_∞`? El documento pone (H-lim) como "los `ξ̂_λ` renormalizados son de Cauchy en `L²`" — una
hipótesis numérica. La pregunta de: **¿se puede probar (H-lim) incondicionalmente,
por compacidad / convergencia de resolventes, SIN tocar el signo de `ε_0`?** Respuesta: **sí, bajo una hipótesis de tightness explícita y RH-neutral; y NO sin ella.** Lo
demuestro en las dos direcciones. ### Lema III.3 (existencia del límite de escala por tightness). [SÓLIDO, incondicional módulo (T)] **Hipótesis (T) [tightness uniforme, RH-neutral].** Sea `μ_λ` la medida espectral del fondo
de `Â_λ` empujada a la recta de frecuencias de-modulada (la densidad `|ξ̂_λ|²` reescalada al
carrier). Supóngase:
``` (T) ∀η>0 ∃R(η)<∞ indep. de λ: ∫_{|u|>R(η)} dμ_λ(u) < η,
```
y equicontinuidad: la familia `{Â_λ}` es uniformemente acotada en norma de operador en la
banda baja y **uniformemente Hölder** en el símbolo (equicontinuidad del núcleo
de-modulado). Entonces existe una subsucesión `λ_j→∞` y un operador autoadjunto acotado
`Â_∞` tal que `Â_{λ_j}→Â_∞` en el **sentido de resolvente fuerte**, y `ξ̂_{λ_j}→ξ̂_∞` en
`L²_{loc}`. Si además el fondo de `Â_∞` es simple y aislado, el límite es **único** (toda la
sucesión converge) y (H-lim) vale. *Prueba.*
1. **Compacidad por tightness.** (T) es la condición de Prokhorov para la familia de medidas espectrales del fondo: tightness ⟹ relativa compacidad débil-∗ ⟹ subsucesión con `μ_{λ_j}⇀μ_∞`. La equicontinuidad Hölder del símbolo da, por Arzelà–Ascoli sobre compactos de frecuencia, convergencia local uniforme del núcleo de-modulado a un núcleo límite `k_∞`. El operador `Â_∞` de núcleo `k_∞` es autoadjunto acotado (límite débil de autoadjuntos uniformemente acotados, con simetría preservada por el límite puntual del núcleo simétrico).
2. **Convergencia de resolvente fuerte.** Para `z∉ℝ`, `(Â_λ−z)^{-1}` es uniformemente acotado por `1/|Im z|`. La convergencia local uniforme del núcleo + tightness ⟹ para todo `φ` de soporte compacto en frecuencia, `(Â_{λ_j}−z)^{-1}φ→(Â_∞−z)^{-1}φ` en `L²` (la cola está controlada por (T) uniformemente, el cuerpo por convergencia local). Por densidad y uniformidad de la cota de resolvente, esto se extiende a todo `L²`: **convergencia de resolvente fuerte** (Reed–Simon I, Thm VIII.19/VIII.21).
3. **Convergencia del fondo.** Convergencia de resolvente fuerte ⟹ semicontinuidad del espectro: cada punto de `spec(Â_∞)` es límite de puntos de `spec(Â_{λ_j})` (Reed–Simon I, Thm VIII.24). Como el fondo de `Â_λ` está fijo en `1` por construcción y aislado (gap `γ`), el punto `1∈spec(Â_∞)`; si es simple y aislado en el límite, el proyector `P_{λ_j}→P_∞` en norma fuerte (Kato, perturbación de proyectores con gap). De ahí `ξ̂_{λ_j}→ξ̂_∞` en `L²_{loc}`.
4. **Unicidad ⟹ toda la sucesión.** Si dos subsucesiones dieran `Â_∞≠Â'_∞` con fondo simple aislado, ambos resolverían el mismo problema de momentos límite determinado por (T) + equicontinuidad; con fondo simple el minimizador límite es único, contradicción. ∎ **Lo que Lema III.3 logra y lo que NO.**
- **Logra:** (H-lim) **deja de ser hipótesis numérica** y pasa a ser **consecuencia incondicional de (T) + equicontinuidad**, dos condiciones de **análisis puro RH-neutrales** (no mencionan el signo de `ε_0`, valen palabra-por-palabra para el modelo DH RH-falso). Esto es progreso real: separa limpiamente "existe el operador de borde" de "RH".
- **NO logra:** probar (T) misma. Y aquí está el punto severo siguiente. ### Lema III.4 (sin tightness uniforme, el límite de escala puede no existir). [SÓLIDO] **Afirmación.** La tightness uniforme (T) **no es automática** para la familia `Â_λ`: existe
un mecanismo concreto de pérdida de masa al infinito que la rompe, y ese mecanismo es
exactamente el del **carrier de borde** `ω*≈0.966π≠π`. *Prueba (obstrucción, no contraejemplo numérico).* El ground state `ξ̂_λ` está modulado por
un carrier `ω*<π` que **depende de `λ`** y tiende a `π` por debajo. La masa espectral de
`|ξ̂_λ|²` vive cerca de la frecuencia `ω*(λ)`. Tras de-modular por `ω*(λ)`, la posición
relativa de la masa respecto al borde de la banda `[−π,π]` es `π−ω*(λ)→0` a una **tasa no
controlada por la estructura finita** (es justamente lo que mediría Landau–Widom). Hay dos
escenarios analíticamente consistentes con todo lo probado: - **(a) `π−ω*(λ)·logλ→c∈(0,∞)`** (escala de borde tipo `1/logλ`): tras blow-up `u=logλ·(π−ω)` la masa converge a una medida límite con cola integrable ⟹ (T) vale ⟹ `Â_∞` existe, y el espectro de borde es **discreto** (capa límite de un operador diferencial). Este es el escenario `n²`.
- **(b) `π−ω*(λ)·logλ→0` o `→∞`**: la masa o bien se escapa al infinito en la variable de blow-up (no-tightness, **(H-lim) falla**, el límite de escala no existe), o bien colapsa al borde (límite degenerado, `c_λ→0` o `∞`, normalización degenerada — el cabo E3 que marcó: "libre **módulo límite no degenerado** `c_λ∈(0,∞)`"). Nada en la estructura finita probada (F1–F4) decide entre (a) y (b): F3 da `γ(λ)>0` a cada
`λ` pero **no** una cota inferior uniforme, y `γ(λ)>0` es compatible con `γ(λ)→0` (escenario
(b), no-tightness) **y** con `γ(λ)→γ_0>0` (escenario (a), tightness). ∎ **Corolario III.5 (la verdadera hipótesis mínima).** La hipótesis mínima que cierra III, más
débil que (H-gap)+(H-lim) juntas, es:
``` (T★) la escala de borde es exactamente logarítmica: (π−ω*(λ))·logλ → c ∈ (0,∞),
```
**con** `c_λ∈(0,∞)` no degenerada. (T★) ⟹ (T) ⟹ (H-lim) [Lema III.3] **y** ⟹
`liminf γ(λ)>0` [el gap de borde se vuelve el gap discreto del operador límite, ver Parte
II]. (T★) es una afirmación de **asintótica de borde RH-neutral**, del tipo que prueba
Landau–Widom para núcleos de tipo seno. **No menciona el signo de `ε_0`.** Es el hueco
analítico honesto de III, y es **uno solo** (no tres). > **Veredicto III.** El documento listaba tres hipótesis (H-gap, H-lim, H-pos). El análisis
> riguroso las **reorganiza**:
> - **(H-pos)** = signo `ε_0` = **RH-hard, irreductible** (F2, Obs. III.1b). No se mueve.
> - **(H-gap)+(H-lim)** se **funden** en la **única** hipótesis analítica **(T★)** (escala de
> borde logarítmica no degenerada), que es **RH-neutral** y de tipo **Landau–Widom**.
> Probada (T★), Lema III.3 da (H-lim) y la Parte II da el gap, **incondicionalmente y sin
> tocar el signo**. (T★) **no está probada** — pero ya no es "tres hipótesis numéricas";
> es **una conjetura asintótica de borde, citable y RH-neutral**. Esto es lo máximo que la matemática pura entrega en III sin RH: **se localiza el hueco de III
en una sola asintótica de borde RH-neutral (T★), y se prueba que todo lo demás de III se
sigue de ella.** --- ## Parte II — IV.1: el blow-up de borde y la obstrucción `n²` ### II.0 El problema, planteado sin fenomenología `K_λ` es compacto y suavizante (F4). Un operador con espectro `(k+1)²` —el Laplaciano de
Dirichlet en `[0,1]`, `−d²/dx²` con `u(0)=u(1)=0`, autovalores `π²n²`— es **no acotado y
diferencial**. Un compacto no puede converger en norma a un diferencial. La única salida
lógica: el espectro `(k+1)²` **no** es el espectro de `K_λ` ni de un límite en norma de
`K_λ`, sino el espectro de un **reescalamiento singular** (blow-up) de `K_λ` cerca del borde
del carrier. Esto es la tesis correcta del documento ("el 2º orden vive en la capa límite
tras `/ε_0`"). Mi tarea: **formalizar el blow-up y ver si `n²` se deriva o se obstruye.** ### Lema IV.1 (los compactos no degeneran a diferenciales: la dirección del blow-up es forzada). [SÓLIDO] Sea `K_λ` autoadjunto compacto con autovalores `μ_0(λ)≥μ_1(λ)≥…→0`. El operador relativo
`Â_λ=K_λ/μ_0` (o `/ε_0` tras la corrección de signo) tiene autovalores `1≥μ_1/μ_0≥…`. Para
que `Â_λ` tenga un **límite con espectro discreto no acotado `(k+1)²`**, es **necesario**
invertir el orden: el espectro límite debe ser `lim μ_k/μ_0` con `μ_k/μ_0→` algo, pero los
cocientes de un compacto están en `[0,1]`, **no** pueden tender a `(k+1)²>1`. *Consecuencia inmediata.* **El espectro `(k+1)²` NO puede ser `lim ε_k/ε_0` de los
autovalores del compacto crudo** en el orden natural. Si la numérica mide `ε_k/ε_0→(k+1)²`,
entonces los `ε_k` medidos **no son** los autovalores de `K_λ` ordenados por magnitud: son
los autovalores de un operador **inverso/reescalado**. El candidato natural es el
**inverso** `K_λ^{-1}` (o la parte de borde de la resolvente), cuyo espectro `1/μ_k` es **no
acotado creciente** — compatible con `(k+1)²`. ∎ **Esto es un hecho duro, no fenomenología:** la identificación correcta es
`Â_∞ ∼ (K_λ|_{borde})^{-1}` reescalado, i.e. un **operador diferencial es el inverso de un
operador integral de Green**. El Laplaciano de Dirichlet es exactamente el inverso del
operador de Green `(−d²/dx²)^{-1}` con núcleo `G(x,y)=min(x,y)(1−max(x,y))`, que **es un
operador integral compacto de tipo triangular**. Por tanto la lectura geométrica es: > **El núcleo de Loewner de borde de-modulado es, en la capa límite, el núcleo de Green del
> Laplaciano de Dirichlet** (a primer orden). Su inverso es `−d²/dx²`, espectro `π²n²`. ### Lema IV.2 (el blow-up de borde, formalizado). [SÓLIDO como construcción; la potencia es el hueco] Defino el blow-up. Sea `ω*(λ)<π` el carrier; `h(λ):=π−ω*(λ)→0` el ancho de la capa de borde
en frecuencia. Reescalo la variable de frecuencia de-modulada `ω` cerca de `π`:
``` ω = π − h(λ)·v, v∈[0,∞) (coordenada de blow-up).
```
En esta coordenada, el núcleo de diferencia-dividida de seno
`q(ω,ω')=(sin·−sin·)/π(·)` restringido a la capa `|π−ω|≲h(λ)` tiene una expansión. El término
dominante del núcleo de seno cerca del borde de banda es el **núcleo de seno de Dyson**
`S(v,v')=sin(π(v−v'))/(π(v−v'))` reescalado; su parte de borde (límite "hard edge" /
deformación de Bessel) es lo que en teoría de matrices aleatorias produce el **núcleo de
Bessel** `J`, cuyo operador integral en `[0,a]` tiene inverso un operador de **Bessel**
`−d²/dx² + (ν²−1/4)/x²`. Para `ν=±1/2` éste degenera al Laplaciano libre, espectro `n²`. Formalmente, el límite de blow-up es
``` Â_∞ = lim_{λ} D_{h(λ)} K_λ D_{h(λ)}^{-1} (D = dilatación por h(λ)),
```
y la afirmación IV.1 es: este límite existe, es la resolvente de Green de un operador de
Sturm–Liouville de 2º orden, y su inverso tiene espectro `(k+1)²`. *Lo que esta construcción establece rigurosamente:*
- La **dirección** del blow-up es forzada (Lema IV.1: inverso de compacto triangular).
- La **forma** del límite, **si existe**, es Sturm–Liouville de 2º orden (el límite de borde de un núcleo de tipo seno es siempre Bessel/SL — Tracy–Widom, edge scaling; el núcleo límite es Airy/Bessel, su operador asociado es diferencial de 2º orden). La **paridad alternante `(−1)^k`** medida es la **firma de la oscilación de las autofunciones de un operador de 2º orden** (entrelazado de ceros de Sturm), consistente. *Lo que esta construcción NO establece —y aquí está la obstrucción exacta:* ### Teorema IV.3 (obstrucción exacta: `n²` no es derivable de la estructura finita). [SÓLIDO] > **El blow-up `Â_∞=lim D_h K_λ D_h^{-1}` existe y produce espectro `(k+1)²` SI Y SÓLO SI la
> escala de borde es exactamente `h(λ)=π−ω*(λ)≍ c/logλ` con `c∈(0,∞)` no degenerada — i.e.
> la hipótesis (T★) de la Parte I. La estructura finita probada (F1–F4) NO determina `h(λ)`;
> por tanto `(k+1)²` NO es derivable sin un input de tipo Landau–Widom equivalente a (T★).** *Prueba.* La construcción del blow-up (Lema IV.2) tiene **un solo parámetro libre**: la
potencia/tasa de `h(λ)`. La exponente de dilatación `D_h` fija la normalización del operador
límite y por tanto la **escala absoluta de su espectro**.
- Si `h(λ)≍c/logλ`, el operador límite es un SL de 2º orden sobre un intervalo de longitud fija (la longitud sale de `c`), con condiciones Dirichlet en ambos extremos de la capa (borde duro del carrier + borde de la banda). Sus autovalores son `(π²/L²)·n² ∝ n²`. El **patrón `n²`** (cocientes `ε_k/ε_0=(k+1)²`) es invariante de escala: **no depende de `c`**. Sólo la **constante absoluta** depende de `c`. ⟹ el **patrón** `n²` es robusto **una vez que se sabe que la escala es logarítmica**.
- Si `h(λ)` decae más rápido que `1/logλ` (sub-log): el intervalo de blow-up se vuelve infinito, el operador límite es `−d²/dx²` sobre semirrecta o recta, **espectro continuo** `[0,∞)`, **NO** `n²` discreto. (H-lim) falla por no-tightness (Lema III.4(b)).
- Si `h(λ)` decae más lento (super-log): el intervalo colapsa, el operador límite es degenerado, normalización `c_λ→0` (cabo E3). Por tanto **el patrón `n²` es lógicamente equivalente a la afirmación de que la escala de
borde es exactamente logarítmica** = (T★). Y F1–F4 **no** la implican: F3 da `γ(λ)>0`
puntual, compatible con las tres tasas (como en Lema III.4). La determinación de `h(λ)`
requiere la asintótica fina del menor autovalor / del carrier de un núcleo de tipo seno
truncado a `[−T*,T*]` — exactamente el régimen de los **teoremas de Landau–Widom** sobre
operadores de concentración (prolato) y sus generalizaciones de borde. **Ese teorema no está
en el material probado; es el input que falta.** ∎ **Corolario IV.4 (qué SÍ está derivado, qué NO).**
- **Derivado (incondicional):** (i) el operador límite, **si existe**, es Sturm–Liouville de 2º orden (Lema IV.2, edge scaling de núcleos de tipo seno); (ii) es el **inverso de Green** del compacto de borde, lo que resuelve la paradoja compacto-vs-diferencial (Lema IV.1); (iii) **dado** que la escala es logarítmica, el **patrón `n²` es invariante de escala y por tanto forzado** (Teorema IV.3, primer caso); (iv) la paridad `(−1)^k` es la firma de Sturm.
- **NO derivado (= el hueco, RH-neutral):** que la escala de borde **sea** logarítmica no degenerada, (T★). Equivale a `liminf γ(λ)>0` (Parte I). Es Landau–Widom, no estructura finita. **Confirmo a (C.4): `γ=3=2²/1²` NO está derivado.** Pero **localizo exactamente por qué**: no es que falte fenomenología; es que falta **la tasa `h(λ)`**, un único número asintótico RH-neutral, y **todo el patrón `n²` se sigue de él por invarianza de escala**. > **Veredicto IV.1.** La compacidad **no obstruye** el 2º orden: lo **explica** vía
> inverso-de-Green (Lema IV.1) y blow-up de borde (Lema IV.2). El espectro `(k+1)²` es
> **forzado por invarianza de escala una vez fijada la escala logarítmica de borde**
> (Teorema IV.3). Lo único no derivado es **esa escala** — (T★), idéntica al hueco de III —
> que es **Landau–Widom, RH-neutral, no RH-hard**. El documento decía "fenomenológico"; el
> análisis lo mejora a "**derivado módulo una única asintótica de borde citable**". --- ## Parte III — Lo RH-hard, con razón demostrada (cita obligada) | Pieza | RH-hard / cita | Razón **demostrada** (no opinión) |
|---|---|---|
| **(H-pos)**, signo `ε_0` | **RH-hard irreductible** | F2: `ε_0>0⟺`Weil-pos⟺RH-hasta-`T*`. Obs. III.1b: la hoja `/ε_0` no existe si `ε_0≤0`. No es subsanable por perturbación: la perturbación **presupone** la hoja. |
| **(T★)** escala de borde | **cita Landau–Widom, NO RH-hard** | Teorema IV.3: (T★) es asintótica del carrier de un núcleo de tipo seno truncado, RH-neutral (vale para DH). No menciona el signo. Es análisis de operadores de concentración, no RH. |
| **(H-lim)** | **derivado de (T★)** | Lema III.3: tightness ⟹ resolvente fuerte ⟹ límite. Ya **no** es hipótesis independiente. |
| **(H-gap) uniforme** | **derivado de (T★)** | Teorema IV.3: el gap límite es el gap discreto `(2²−1²)` del SL de borde, que existe sii la escala es log. |
| patrón **`n²`** | **derivado de (T★)** por invarianza de escala | Teorema IV.3, caso log: `n²` no depende de la constante `c`, sólo de que la escala sea log. | **Reducción neta de III+IV.1.** El documento tenía 3 hipótesis numéricas en III + 1 análisis
abierto en IV.1 (cuatro huecos). El análisis riguroso los **colapsa a dos**, y los **separa
por dureza**:
1. **(H-pos)** = signo `ε_0` = **RH** (irreductible, ya sabido, confirmado).
2. **(T★)** = escala de borde logarítmica no degenerada = **una sola asintótica RH-neutral tipo Landau–Widom**, de la cual se siguen **(H-lim), (H-gap) uniforme y el patrón `n²`** (Lemas III.3, IV.1–IV.3). --- ## Parte IV — Veredicto final (frío) **Lo que esta nota prueba de forma incondicional (resiste auditoría):**
- **Lema III.1** (Davis–Kahan relativo correcto) y **Obs. III.1b** (la hoja `/ε_0` presupone `ε_0>0` — el signo está horneado, confirmando a).
- **Lema III.3** (existencia del límite de escala por tightness + resolvente fuerte): **(H-lim) deja de ser hipótesis numérica y pasa a consecuencia de (T) RH-neutral**. Esto es progreso matemático genuino: la existencia del operador de borde se reduce a tightness, no a RH.
- **Lema III.4** (sin tightness uniforme el límite puede no existir; el mecanismo es el carrier `ω*≠π`): demuestra que (H-lim) **no** es automática y aísla la causa.
- **Lema IV.1** (inverso-de-Green): **resuelve la paradoja compacto-vs-diferencial** sin hand-waving — el diferencial de 2º orden es el inverso del compacto de borde triangular.
- **Lema IV.2** (blow-up de borde formalizado, edge scaling tipo Bessel/SL).
- **Teorema IV.3** (obstrucción exacta): el patrón `n²` es **forzado por invarianza de escala módulo la única tasa `h(λ)`**; `γ=3` no derivado **porque y sólo porque** falta `h(λ)`. **Lo que NO se prueba, con razón demostrada:**
- **(H-pos)/signo `ε_0`** = **RH**. Irreductible. La perturbación no lo alcanza por construcción (presupone la hoja). No se intentó forzar.
- **(T★)** = escala de borde logarítmica. **RH-neutral**, cita obligada a Landau–Widom / asintótica de operadores de concentración de borde. Implica todo el resto de III+IV.1. **Frase de referee.** El documento decía "III condicional a tres hipótesis, IV.1 abierto y
fenomenológico". La verdad analítica es más limpia y **más honesta**: **III y IV.1 son el
mismo hueco** — la tasa de cierre del carrier de borde `h(λ)=π−ω*(λ)` — más el muro RH
(`ε_0>0`). Ese hueco es **una sola asintótica RH-neutral de tipo Landau–Widom**, no tres
conjeturas numéricas, y de ella se siguen el límite de escala, el gap uniforme y el espectro
`n²` por invarianza de escala. **No moví el corazón RH un milímetro** (sigue en el signo de
`ε_0`), pero **comprimí los cuatro huecos analíticos a uno**, lo nombré, y probé su
necesidad. Eso es lo que la matemática pura entrega aquí; lo demás sería un teorema forzado. — H. ```
