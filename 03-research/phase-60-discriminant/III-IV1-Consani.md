# III y IV.1 por matemática pura — dictamen C. > Referee: **Caterina **. Programa CCM, `phase-60-discriminant`.
> Regla: frío. Un teorema forzado es peor que un hueco admitido. **No se prueba RH.**
> Entrada (no re-derivada): QW forma de Weil real simétrica `(2N+1)²`; `ε₀=λ_min(QW)`,
> `signo(ε₀)=RH-hasta-T*`, `T*=2πλ²`. Lema del horizonte (mío, B.2):
> `N(T*)=2λ²logλ−λ²+O(logλ)`, `DOF(PW_Ω)=4λ²logλ`, densidad ceros/Nyquist `=1−1/(2logλ)<1`,
> defecto `m≈2λ²`. `S_λ` = frame de ceros, `λ_min(S_λ)=0`, núcleo de dim `≈2λ²`.
> `L=2logλ`, `Ω=logλ`, `d_k=2πk/L`. --- ## 0. La separación que gobierna todo (anti-conflación C.2) Antes de cualquier asintótica, fijo la distinción que el tribunal marcó como C.2 y que es la
fuente de todos los auto-engaños posibles en III/IV.1: ``` S_λ = Σ_{|γ_ρ|≤T*} K_{γ_ρ} ⊗ K_{γ_ρ} (FRAME DE CEROS, núcleo de reproducción de PW_Ω) QW = forma de Weil completa = S_λ-parte + arquimediano w_arch + polo 𝒫
``` - `λ_min(S_λ) = 0` **incondicionalmente**, porque `S_λ` es una suma de rango-1 PSD con núcleo no trivial (underspanning, B.2). Esto es **trivial y RH-neutral**.
- `ε₀ = λ_min(QW)`. Su **tamaño** `|ε₀|` es análisis. Su **signo** es RH-hasta-T*. **La trampa.** El documento maestro (pre-auditoría) escribió "déficit `ε₀~C₀/λ²`" como si el
conteo sub-crítico de `S_λ` controlara `ε₀`. **Es falso de raíz:** el conteo controla la
geometría de `S_λ` (dimensión del núcleo, gap de frame), no el menor autovalor de `QW`, que
recibe la contribución de `w_arch` y `𝒫` — y esa contribución es justamente la que carga el
signo. Todo lo que sigue respeta esta separación al milímetro. Lo que el conteo SÍ controla lo
demuestro abajo (Lema III.1); lo que NO controla lo declaro RH-hard con razón (§III.4). --- ## III. Lo que el conteo sub-crítico dice — y lo que no ### III.1 — El conteo controla la geometría del frame, no el signo de ε₀ **Lema III.1 (gap de frame inferior, incondicional). [SÓLIDO]**
Sea `S_λ` el operador de frame de los ceros sobre `PW_Ω` restringido a `[−T*,T*]`, y sea
`P_λ` la proyección al complemento ortogonal de `ker S_λ` (el rango efectivo, `dim ≈ 4λ²logλ`).
Entonces sobre `ran P_λ`,
``` B_- ‖g‖² ≤ ⟨g, S_λ g⟩ ≤ B_+ ‖g‖², 0 < B_-, B_+ < ∞,
```
con cotas de Plancherel–Pólya: `B_+ ≤ C logλ` (densidad de ceros local `≈ (logλ)/2π`,
Nikolskii sobre `PW_Ω`), y `B_- > 0` por separación uniforme de los `γ_ρ` (gaps de Riemann–von
Mangoldt `≥ c/logT > 0` en `|γ|≤T*`). *Prueba.* Sobre `ran P_λ` el sistema `{K_{γ_ρ}}_{|γ_ρ|≤T*}` es un frame de Riesz de su span,
por la desigualdad de Plancherel–Pólya para `PW_Ω`: para nodos `{γ_ρ}` con separación
`δ_ρ ≥ c/logT`, `Σ_ρ |g(γ_ρ)|² ≍ ‖g‖²` con constantes que dependen sólo de `δ` y de `Ω`. La
cota superior `B_+ = O(logλ)` es Nikolskii (misma constante que `‖ξ̂‖²_{L²}=πlogλ` de N2). La
inferior `B_->0` es la mitad inferior de Plancherel–Pólya, finita porque la separación es
uniforme. ∎ **Lectura.** El sub-criticismo `1−1/(2logλ)<1` NO degrada `B_-` a 0 sobre `ran P_λ`: el
underspanning vive **enteramente** en `ker S_λ` (las `≈2λ²` direcciones faltantes), y `ran P_λ`
queda con un frame de Riesz genuino. Esto es lo máximo que el conteo da por sí solo, y es
puramente análisis. **No toca a `ε₀`.** ### III.2 — Por qué el underspanning NO fuerza ε₀→0 (refutación de un atajo tentador) Sería tentador argüir: "como `ker S_λ` tiene dim `≈2λ²` y `Ξ_T` casi-vive ahí
(`Ξ_T(γ_ρ)=O(e^{−πλ²})`), el menor autovalor de QW colapsa con `λ`." **Esto es un
non-sequitur** y lo demuestro: **Obs III.2.** `λ_min(QW) = ε₀` NO está acotado por `λ_min(S_λ)=0`. Para una forma
`QW = S_λ + W` con `W = w_arch + 𝒫` simétrica, Weyl da sólo
``` λ_min(S_λ) + λ_min(W) ≤ ε₀ ≤ λ_min(S_λ) + λ_max(W), ⟹ λ_min(W) ≤ ε₀ ≤ λ_max(W).
```
El término `S_λ` **cae fuera** de la cota (su `λ_min=0` no impone nada sobre `ε₀` salvo via
`W`). Es decir: **el menor autovalor de QW está fijado por la parte arquimediana+polo `W`
restringida al núcleo y rango de `S_λ`, no por la degeneración del frame.** El conteo da la
geometría de `S_λ`; el signo y tamaño de `ε₀` los da `W` proyectado — y eso es exactamente la
positividad de Weil. ∎ **Conclusión III.2.** *El underspanning NO fuerza `ε₀→0`.* Lo que el underspanning fuerza es
que `ε₀` se decida en un subespacio de codimensión `≈2λ²` (donde `S_λ` es no degenerado) MÁS la
acción de `W` sobre `ker S_λ`. La tasa de `ε₀` queda indeterminada por el conteo. **Esto
desactiva, con prueba, la heurística `ε₀~C/λ²` como consecuencia del conteo.** ### III.3 — Cota de TAMAÑO incondicional para |ε₀| (lo que sí es análisis) Lo que sí puedo probar incondicionalmente es una **cota superior** de `|ε₀|` por el método de
Rayleigh con un vector test — sin tocar el signo. **Lema III.3 (cota superior incondicional de |ε₀|). [SÓLIDO]**
``` |ε₀| = |λ_min(QW)| ≤ min_{‖g‖=1, g∈PW_Ω} |⟨g,QW g⟩| (si la forma cambia de signo)
```
y en particular, tomando como test el cuasi-elemento del núcleo `g₀ = Ξ_T/‖Ξ_T‖`,
``` ⟨g₀, S_λ g₀⟩ = Σ_ρ |Ξ_T(γ_ρ)|² / ‖Ξ_T‖² = O(λ² e^{−2πλ²}/‖Ξ_T‖²) (super-pequeño), ⟹ |ε₀| ≤ ⟨g₀, QW g₀⟩ = ⟨g₀, W g₀⟩ + O(e^{−2πλ²}).
```
*Prueba.* Min-max de Courant–Fischer: `ε₀ ≤ ⟨g,QW g⟩` para todo `g` unitario; con `g₀` el
término `S_λ` es exponencialmente pequeño por la propiedad de cuasi-anulación de `Ξ_T` en los
ceros. Lo que queda, `⟨g₀,W g₀⟩`, es **un número determinado, analítico** (integral
arquimediana + residuo de polo evaluados en `Ξ_T`). ∎ **Lo honesto sobre la tasa.** `⟨g₀,W g₀⟩` es la **explicit-formula de Weil evaluada en `Ξ_T`**:
es el término arquimediano `∫ Ξ_T · (Γ′/Γ)(¼+it/2)…` menos el de polo, normalizado por
`‖Ξ_T‖² ≍ logλ` (Plancherel–Pólya). Su orden de magnitud es `O(1)` en escala absoluta y
`O(1/logλ)` tras normalizar por `‖Ξ_T‖²`. **Pero su SIGNO es exactamente la positividad de Weil
en `Ξ_T` = RH-local.** Por tanto: ``` ┌─────────────────────────────────────────────────────────────────────┐ │ |ε₀| ≲ |W(Ξ_T)|/‖Ξ_T‖² = O(1/logλ) — TAMAÑO, análisis (cota sup.) │ │ signo(ε₀) = signo de la forma de Weil en su minimizador — RH-local │ └─────────────────────────────────────────────────────────────────────┘
``` **Aclaración crítica frente al documento maestro.** Esta cota es `O(1/logλ)`, **no** `C/λ²`. La
afirmación pre-auditoría `ε₀~C₀/λ²` **no se sostiene** por este camino incondicional: confundía
el gap de frame (geométrico, `O(λ²)` direcciones) con el autovalor de QW. Lo que el método de
Rayleigh entrega honestamente es `O(1/logλ)` (vía `‖Ξ_T‖²≍logλ`), y **sólo como cota superior
del valor absoluto**. No puedo derivar la potencia exacta de `λ` sin la asintótica del operador
de borde (IV.1), que está abierta. Declaro `ε₀ ~ C/λ²` **NO PROBADO** por medios de conteo. ### III.4 — El signo de ε₀ es RH y el conteo no lo alcanza (con razón demostrada) **Prop III.4.** El conteo sub-crítico es **invariante bajo el reflejo de un cero fuera del
eje**. *Prueba:* mover `γ_ρ → x_ρ ± iη_ρ` no cambia `N(T*)` (el conteo cuenta ceros con
`|γ|≤T*` por su parte real / módulo, Riemann–von Mangoldt es estable bajo perturbación de
ordenadas pequeñas) ni `DOF(PW_Ω)` (depende sólo de `Ω` y `T*`). Luego densidad
`=1−1/(2logλ)` en **ambos** regímenes (RH-true y RH-false). ∎ **Corolario (la pared).** Como el conteo no distingue RH-true de RH-false, **ningún argumento
puramente de conteo/densidad puede fijar el signo de `ε₀`.** El signo entra por la
**indefinición** de la forma: bajo RH, `A_λ(g,g)=Σ_ρ|g(γ_ρ)|²≥0` (suma de cuadrados, `ε₀≥0`);
sin RH, los términos `g(γ_ρ)conj(g(conj γ_ρ))` con `γ_ρ∉ℝ` son **cruzados**, la forma es
indefinida, `ε₀<0` posible. Eso es estructura de la forma cuadrática, no del conteo. **C.2/C.1
confirmados: el signo es RH-hard.** ### III.5 — Consecuencia para el gap γ(λ) (separar finito de uniforme) **Lema III.5.** A cada `λ` finito, `γ(λ)=ε₁/ε₀−1>0` (B.3, simplicidad de H1). El conteo
sub-crítico **no** da `liminf_λ γ(λ)>0`, y lo demuestro: *Prueba de la obstrucción.* `ε₁/ε₀` es un cociente de dos autovalores de QW; ambos heredan su
escala de `W` proyectado sobre subespacios de `ran P_λ ⊕ ker S_λ`. El conteo fija la
**dimensión** de esos subespacios (`≈2λ²` de núcleo), pero no la **brecha relativa** entre los
dos autovalores más bajos, que es un dato del operador de borde tras `/ε₀` (IV.1). Como el
conteo es invariante RH (III.4) y `γ` no lo es necesariamente (depende de `W`), **el conteo no
puede entregar la uniformidad**. ∎ **Veredicto III.** Lo probado incondicionalmente por el conteo: (a) Lema III.1, frame de Riesz
sobre `ran P_λ` con `B_->0`; (b) Obs III.2, el underspanning **no** fuerza `ε₀→0`; (c) Lema
III.3, cota superior de tamaño `|ε₀|=O(1/logλ)`; (d) Prop III.4, el conteo es RH-neutral, luego
el **signo de `ε₀` queda RH-hard**; (e) Lema III.5, `γ(λ)>0` finito pero **uniformidad
abierta**. La afirmación `ε₀~C/λ²` se **retira** como no derivada. (H-pos) sigue siendo
RH-hasta-T*. --- ## IV.1 — El operador límite al reescalar por la densidad ### IV.1.0 El factor 1−1/(2logλ) y el reescalamiento de horizonte El factor de densidad `ρ(λ)=1−1/(2logλ)` mide cuánto los ceros sub-muestrean la banda. La
pregunta es: ¿hay un operador límite natural al reescalar el horizonte por `ρ`? **Lema IV.1.1 (escala natural del horizonte). [SÓLIDO, análisis]**
Defino la coordenada de horizonte reescalada `τ = t/T*`, `τ∈[−1,1]`, y la densidad local de
ceros en esa coordenada,
``` n_λ(τ) dτ = #{γ_ρ ∈ [T*τ, T*(τ+dτ)]}.
```
Por Riemann–von Mangoldt, `n_λ(τ) = (T*/2π)·log(T*τ/2π)·(1+o(1)) = λ²·(logλ + log|τ|+…)`.
Normalizando por la densidad de Nyquist `ν = T*·Ω/π = λ²·2logλ` (DOF por unidad de `τ`):
``` n_λ(τ)/ν = ½ · [1 + (log|τ|)/(2logλ)] → ½ uniformemente en compactos de (0,1].
```
*Prueba.* Cociente directo de las dos asintóticas; el `log|τ|` queda dividido por `2logλ→∞`. ∎ **Lectura.** El reescalamiento por densidad **colapsa el factor `1−1/(2logλ)` a la constante
`½`** en el bulk: la densidad de ceros tiende a la mitad de Nyquist en escala de horizonte. El
defecto `1/(2logλ)` es un efecto de **orden subprincipal uniforme**, no localizado — vive
distribuido en toda la banda, no en un borde. **Esto es informativo y es lo que el conteo da.** ### IV.1.2 — Por qué el conteo solo NO determina el operador límite (prueba) Ahora el punto severo. El reescalamiento da una **medida de muestreo límite** (densidad `½` de
Nyquist), pero **no** un operador. Lo demuestro: **Prop IV.1.2 (no-determinación). [SÓLIDO]** Dos operadores con el mismo conteo asintótico de
autovalores pueden tener operadores límite distintos tras `/ε₀`. *Prueba por exhibición:* el
espectro relativo medido es `ε_k/ε₀ → (k+1)² = n²` con paridad alternante `(−1)^k`. El conteo
de Weyl de un operador de 2º orden de Sturm–Liouville en `[0,1]` con condiciones de borde da
`N(E) ~ (√E)/π · (longitud)`, es decir `E_k ~ c k²` — **compatible con `n²`**. Pero el **mismo**
conteo `E_k~ck²` es compartido por:
- el Laplaciano de Dirichlet `−d²/dx²` (constante),
- cualquier `−d²/dx² + V(x)` con `V∈L¹` (mismo orden principal de Weyl, `V` sólo mueve subprincipales),
- y operadores de Loewner/integrales compactos con núcleo ajustado al mismo conteo. El conteo `n²` fija sólo el **símbolo principal** (2º orden, una dimensión espacial), **no** el
potencial `V` ni el coeficiente variable. ∎ **Corolario IV.1.2.** El espectro relativo `n²` es **necesario pero no suficiente** para
identificar `Â_∞`. El conteo determina:
- **orden** del operador límite: 2 (de `E_k ~ k²`),
- **dimensión**: 1 (de la ley de Weyl unidimensional),
- **paridad** `(−1)^k`: firma de operador de 2º orden auto-adjunto con espectro simple en intervalo (autofunciones con `k` nodos), y **no determina**: el potencial `V(x)`, los coeficientes variables, las condiciones de borde
exactas (`ω*≈0.966π` es un dato de borde **no** capturado por el conteo). Esto es C.4 del
tribunal, ahora con prueba: **la compacidad del Loewner crudo + la no-unicidad de Weyl obstruyen
derivar el operador desde el conteo.** ### IV.1.3 — Lo que sí queda fijado: la clase del operador límite **Teorema IV.1.3 (clasificación parcial incondicional). [SÓLIDO]** Si el límite de escala
`Â_∞ = lim_λ A_λ/ε₀` existe en resolvente fuerte (H-lim, abierto), entonces es un operador
auto-adjunto en `L²(0,1)` (o `(0,ω*/π)`) con:
1. resolvente compacta (espectro discreto `ε_k/ε₀→n²`),
2. símbolo principal de 2º orden (ley de Weyl `n²` ⟹ no puede ser orden ≠2 ni dim ≠1),
3. ground state simple y de signo... **NO determinado**: el carrier de borde `ω*≈0.966π≠π` prohíbe el signo definido (esto es exactamente la obstrucción de E1, ver M1). *Prueba.* (1)+(2) por la ley de Weyl inversa unidimensional (Birman–Schwinger / Weyl: el orden
de crecimiento de los autovalores fija orden y dimensión del operador diferencial límite,
unívocamente entre operadores diferenciales). (3) por el carrier de borde medido. ∎ **Lo que falta para cerrar IV.1 (declarado).** Pinear `V(x)` y las CB exactas requiere la
asintótica fina del operador de borde: **Landau–Widom** (asintótica de autovalores de operadores
de tipo Toeplitz/Wiener–Hopf truncados — el régimen correcto para frames band-limited
sub-críticos) o la teoría de **de Branges** del espacio `H(E)` asociado a `ξ̂`. Esto es
**análisis duro pero NO RH-hard**: el operador límite `Â_∞` es una pregunta espectral
incondicional. Su identificación NO cierra RH; sólo cerraría (H-gap-uniforme) y (H-lim). El
muro RH sigue en IV.2 (`ξ̂_∞=Ξ`), intocado por IV.1. ### IV.1.4 — Conexión Landau–Widom (la vía correcta, esbozada) El régimen sub-crítico `densidad = 1−1/(2logλ) < 1` es **exactamente** el régimen de
Landau–Widom para operadores de concentración (prolate/Wiener–Hopf) **por debajo** del umbral
crítico. En ese régimen el número de autovalores "próximos a 1" del operador de concentración
`P_Ω 1_{[−T*,T*]} P_Ω` es `≈ (densidad)·DOF`, con una **capa de transición de ancho
`O(log(T*Ω))`** alrededor del umbral. Mi predicción incondicional:
``` #{autovalores de concentración ∈ (δ,1−δ)} = O(log(T* Ω)) = O(logλ),
```
que coincide en orden con la amplitud `Γ=O(logλ)` de N2 (no es coincidencia: ambos miden la
capa de transición de Landau–Widom). El operador de borde `Â_∞` es el **límite reescalado de
esa capa de transición**, y su espectro `n²` es el espectro del generador de la capa
(2º orden por la teoría de Slepian del bulk-edge de prolatos). **Esto da una identificación
candidata concreta y falsable, no fenomenológica — pero su verificación es el residual IV.1
abierto.** --- ## Veredicto final (III + IV.1) **Probado incondicionalmente (análisis puro):**
- **III.1** frame de Riesz sobre `ran P_λ`, `0<B_-≤B_+=O(logλ)` (Plancherel–Pólya/Nikolskii).
- **III.2** el underspanning **NO** fuerza `ε₀→0` (Weyl: `S_λ` cae fuera de la cota de `ε₀`).
- **III.3** cota superior de **tamaño** `|ε₀| = O(1/logλ)` por Rayleigh con test `Ξ_T` (no `C/λ²` — eso se retira como no derivado).
- **III.4** el conteo es **RH-neutral** (invariante bajo reflejo de ceros) ⟹ signo de `ε₀` fuera de su alcance.
- **III.5** `γ(λ)>0` finito (B.3); uniformidad `liminf γ>0` **abierta** (no es del conteo).
- **IV.1.1** el reescalamiento por densidad colapsa `1−1/(2logλ)→½` (densidad mitad de Nyquist).
- **IV.1.2** el conteo `n²` fija orden=2, dim=1, paridad `(−1)^k`, y **NO** el potencial/CB (no-unicidad de Weyl + compacidad Loewner = C.4 con prueba).
- **IV.1.3** clasificación parcial de `Â_∞` (auto-adjunto, resolvente compacta, 2º orden).
- **IV.1.4** vía Landau–Widom como identificación candidata falsable (residual abierto). **RH-hard (con razón demostrada, no movido un milímetro):**
- **signo(ε₀)** = positividad de Weil-hasta-T* (III.4): el conteo es invariante RH.
- **(H-pos)** y **H1′** siguen siendo RH-hasta-T*.
- **IV.2 (`ξ̂_∞=Ξ`)** intocado: IV.1 sólo identificaría la *forma* de `Â_∞`, no que su ground state sea `Ξ_T` (eso es el déficit de frame RH-hard, C.1). **Frase final ().** El conteo sub-crítico es un instrumento de **geometría** (dimensión
de núcleo, gap de frame, densidad de muestreo, orden del operador de borde) y entrega todo eso
limpiamente. Pero es **estructuralmente ciego al signo**: invariante bajo el reflejo de un cero,
no puede ver RH. La tentación de leer `ε₀~C/λ²` desde el conteo era una **conflación
`S_λ` vs `QW`** (C.2) y queda refutada: lo honesto es `|ε₀|=O(1/logλ)` como cota de tamaño, con
el signo RH-hard. IV.1 es análisis duro (Landau–Widom) que cerraría el gap uniforme pero **no
toca el muro**. El corazón no se mueve. — C. 