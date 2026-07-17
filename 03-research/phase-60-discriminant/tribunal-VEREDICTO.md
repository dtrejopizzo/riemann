# ACTA DEL TRIBUNAL — · · ## Veredicto consensuado sobre `RH-PROOF-FULL.md` (cadena E0→E4, programa CCM) Tres referees severos auditaron de forma independiente. Consistencia notable. Este acta
**consensúa** los veredictos, **asienta como demostración sólida** lo verificado por el
tribunal, y deja **honestamente abierto** lo demás. Regla: frío; un resultado forzado es
peor que un hueco admitido. **No se prueba RH** (el núcleo es RH-equivalente). --- ## A. VEREDICTO POR PIEZA (consenso de los tres) | Pieza | Veredicto unánime | Salvedades del tribunal |
|---|---|---|
| **E0** (def + `QW`=forma de Weil) | **SÓLIDO** | "exacto por soporte" → exacto vía **autocorrelación** `2Ω=L=2logλ` ⟹ corte primos `n'≤λ²` (); el término de polo `𝒫` es **load-bearing**, no decorativo (); **NO hay conflación** `QW=Weil` (los 3 lo verifican) |
| **E1** (real-rootedness) | **GAP** | prueba registrada **REFUTADA** por contraejemplo `(−1,2,−1)→−2/(s³−s)` (los 3). **Cita obligada CCM Thm 1.1(iii)**, NO cerrable con funciones enteras (, severo). RH-**neutral** (vale para DH) ⟹ usar E1 **no es circular** (+) |
| **H1** (estructura) | **SÓLIDO** (estructura) | PF da fondo simple + envolvente positiva de-modulada — NO da PSD |
| **H1′** (`QW` PSD) | **= RH** | `ε_0≥0 ⟺` Weil-pos `⟺` RH-hasta-T*. **PF≠PSD** = el hallazgo más importante (unánime) |
| **N0** | **SÓLIDO** | verificó el exponente `5/4+δ/2`; firmó línea por línea. Incondicional |
| **N1** | **SÓLIDO\*** (Boas) | medida armónica + dos constantes correcto; caso `x₀≠0` merece una línea (inocuo) |
| **N2** | **SÓLIDO** (como `O(logλ)`) | **RETIRAR `Γ=O(1)`** (los 3): sólo `O(logλ)` está probado — y **alcanza** |
| **N3** | **SÓLIDO\*** (Boas/PL) | |
| **Reducción (Thm 2)** | **SÓLIDO** (módulo E1) | "la joya": reduce RH a un único número `ε_loc=o(λ^{−½})`. **Sin circularidad** () |
| **III** | **CONDICIONAL** | (H-gap)+(H-lim)+**(H-pos)=RH-hasta-T***. **agrava**: toda la arquitectura `/ε_0` presupone régimen RH-true |
| **N5b** | **SÓLIDO** (reducción) | el borde se **fusiona** con el núcleo, no desaparece |
| **N5c** | **SÓLIDO\*** (módulo E1) | monotonía real-rooted correcta; marcar genericidad `Ξ_f(x₀)≠0` (verificable caso a caso para DH) |
| **IV.1** | **ABIERTO** (análisis) | id. coef. constante **refutadas**; SL 2º orden fenomenológico.: `γ=3` **NO derivado**, la compacidad **obstruye** derivar `n²` |
| **IV.2 ≡ §V** | **= RH** (núcleo) | RH-equivalente (variacional). Correctamente etiquetado |
| **E3** (Hurwitz) | **SÓLIDO** (módulo E1) | normalización "libre" → libre **módulo límite no degenerado** `c_λ∈(0,∞)` () |
| **E4** | **SÓLIDO** (clásico) | | --- ## B. ASENTADO COMO DEMOSTRACIÓN SÓLIDA (verificado por el tribunal) El tribunal verifica y **asienta** estos resultados, propuestos por los referees: **B.1 — Lema M1 (): sub-caso de E1 vía Herglotz. [SÓLIDO]**
> Si `f(s)=Σ_k r_k/(s−d_k)` con `d_k∈ℝ` distintos y **todos los residuos `r_k>0`**, entonces
> para `Im s>0`, `Im f(s)=−Im s·Σ_k r_k/|s−d_k|²<0`; luego `f` no se anula fuera de ℝ ⟹
> **todos los ceros de `f` son reales**, con interlacing estricto (un cero por hueco).
Como el residuo de la secular en `d_k` es `ξ_k`, esto prueba real-rootedness **en el sub-caso
`ξ_k>0`**, self-contained, sin citar CCM. **Verificado correcto.** *Limitación:* NO cubre el
ground state real (carrier de borde `ω*≈0.966π`: ni `ξ_k>0` ni `(−1)^kξ_k>0` — desajuste de
fase). El caso general **es** CCM Thm 1.1(iii). **B.2 — Lema del horizonte CORREGIDO (). [SÓLIDO; reemplaza el conteo erróneo]**
El documento afirmaba `#{γ_ρ≤T*}=dim` ("comparables"). **Es incorrecto.** Conteo correcto:
> `N(T*)=2λ²logλ−λ²+O(logλ)` (Riemann–von Mangoldt, `T*=2πλ²`); DOF de `PW_Ω` sobre
> `[−T*,T*]` `=(logλ/π)·(2T*)=(logλ/π)·4πλ²=4λ²logλ`. Dos lados: `#{|γ_ρ|≤T*}≈4λ²logλ−2λ²`
> vs `DOF≈4λ²logλ`. **Coinciden al orden líder `4λ²logλ`, con defecto `m≈2λ²>0`.**
> ⟹ **densidad ceros / densidad Nyquist `= 1 − 1/(2logλ) < 1`**: los ceros muestrean `PW_Ω`
> **estrictamente por debajo de la densidad crítica de Beurling** (underspanning sub-crítico).
**Verificado correcto.** El régimen es **sub-crítico, no crítico** — corrección sustantiva. **B.3 — `γ(λ)>0` a cada λ finito (). [SÓLIDO módulo H1]**
Por H1 el ground state es **par y simple** ⟹ `ε_1>ε_0` estricto a cada λ finito ⟹ `γ(λ)>0`.
**Verificado** (es la simplicidad de H1). *Limitación:* la **uniformidad** `liminf_λ γ(λ)>0`
(que la hipótesis (H-gap) de III necesita) queda **abierta** — requiere la asintótica del
operador de borde (Landau–Widom), no es regalo de la estructura finita. **B.4 — La identidad variacional `A_λ(g,g)=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` (+). [SÓLIDO]**
Verificada como la **forma cuadrática de Weil** restringida a `PW_Ω` (con el `𝒫` y el
arquimediano del lado-ceros, ceros simples, `conj γ_ρ` que la hace indefinida sin RH). **NO
hay conflación `QW≠Weil`.** El soporte-argumento es correcto vía autocorrelación `2Ω=L`. --- ## C. RECLASIFICACIONES DEL TRIBUNAL (el documento era demasiado optimista) **C.1 — El "déficit de frame" `g₀=Ξ_T` es RH-HARD, no cerrable por Landau–Beurling ().**
El frame de ceros `S_λ=Σ_{|γ_ρ|≤T*}K_{γ_ρ}⊗K_{γ_ρ}` tiene **núcleo de dimensión `≈2λ²`** (por
B.2, underspanning). `Ξ_T` es **uno de `≈2λ²`** candidatos casi-nulos (`Ξ_T(γ_ρ)=O(e^{−πλ²})`).
Nada en `S_λ` solo distingue `Ξ_T`. La selección requiere la forma de Weil **completa** (con
arquimediano+polo) siendo PSD = **RH-local**. ⟹ el Apéndice-2 del documento ("Landau–Beurling
cerraría `g₀→Ξ_T`") **se refuta**: reclasificado de "análisis cerrable" a **RH-hard**. **C.2 — Conflación de objetos: `λ_min(S_λ)=0` vs `ε_0=λ_min(QW)` ().**
El documento llama "déficit `ε_0~C₀/λ²`" al menor autovalor. Pero `λ_min(S_λ)=0` (el frame de
ceros puro es PSD-degenerado, trivial), mientras `ε_0=λ_min(QW)` (forma de Weil **completa**)
es el que tiene **signo = RH**. Son objetos distintos; el documento los conflaciona. **C.3 — E1 es cita obligada, no "reparación pendiente" ().**
Al nivel de la información aislada (envolvente de-modulada positiva), el desajuste de fase
`ω*≠π` impide la vía Herglotz/HB elemental. La real-rootedness **es** CCM Thm 1.1(iii)
(espectro real de la realización autoadjunta / membresía en `H(E)` de de Branges), no un lema
de funciones enteras pendiente. **C.4 — "γ=3 se sigue de IV.1" es demasiado optimista ().**
El espectro `n²` es **numérico, no derivado**; la compacidad del operador de Loewner crudo
**obstruye** derivarlo (compacto ⟹ suavizante, no diferencial). `γ=3` queda fenomenológico. --- ## D. ESTADO FINAL (consenso del tribunal) **Sólidamente demostrado (resiste los tres referees):**
- Andamiaje de aproximación: **N0, N1, N2 (como `O(logλ)`), N3, Reducción, E3, E4** — matemática correcta y reutilizable.
- E0 (def + identidad Weil, sin conflación), H1 (estructura), N5b, N5c (módulo E1).
- **Nuevos, asentados por el tribunal:** Lema M1 (sub-caso E1), lema del horizonte corregido (sub-crítico), `γ(λ)>0` finito, la identidad variacional de Weil. **Abierto no-RH-hard (análisis, localizado):**
- E1 propio = **cita obligada CCM 1.1(iii)** (no cerrable a este nivel).
- IV.1 (operador de borde, Landau–Widom/de Branges).
- (H-gap-res) `liminf γ(λ)>0` uniforme; (H-lim) existencia del límite de escala. **RH-hard (el muro — distribuido):**
- **IV.2≡§V** (`ξ̂_∞=Ξ`, tasa `o(λ^{−½})`) = el núcleo.
- **H1′** (`ε_0≥0`) y **(H-pos)** en III = Weil-positividad-hasta-T*.
- **El déficit de frame `g₀=Ξ_T`** (reclasificado C.1) = RH-local + unicidad. --- ## E. VEREDICTO UNÁNIME DEL TRIBUNAL El programa CCM, auditado por los tres, **no prueba RH y no lo reclama**. Es una **reducción
correcta y elegante de RH a un único núcleo RH-equivalente** (IV.2≡§V: "el ground state de la
forma de Weil es `Ξ_T`"), **rodeada de un andamiaje de aproximación genuinamente probado**
(N0–N3, Reducción, Hurwitz) que **resiste la auditoría severa**. Las dos afirmaciones que un referee hostil tomaría por incondicionales y NO lo son —**H1′
(PSD)** y **III/(H-pos)**— estaban **correctamente degradadas** a RH-equivalentes en la
auto-auditoría. **No detectamos auto-engaño ni circularidad oculta ni conflación `QW≠Weil`.** El tribunal **corrige** cuatro sobre-optimismos residuales (C.1–C.4): el déficit de frame es
RH-hard (no Landau–Beurling), el lema del horizonte estaba mal contabilizado (régimen
sub-crítico), E1 es cita obligada, y `γ=3` no está derivado. Con esas correcciones, **el
documento es honesto y su localización de RH es precisa**. **Frase final (consenso):** el "corazón" no se mueve un milímetro con análisis — **es RH**.
El valor del programa es la localización limpia + el andamiaje probado, no una prueba. — A. · C. · H. (tribunal)
