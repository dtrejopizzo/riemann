# Propagación de la corrección de escala −log ε₀ ~ c·n(T*) por el Eslabón 2 **Corrección:** −log ε₀(λ) ~ c·n(T*) ~ c·λ²logλ (super-exp en L), NO ~ L. (De 4A Jensen +
minimizador = producto canónico vía Thm 1.1.iii + Hadamard.) Hay que propagarla y ver qué
sobrevive y qué cae. ## SOBREVIVE (todo lo que es RATIO o autovector — escala-independiente)
- (i) restricción exacta A_λ=A_∞|_{E_λ}.
- Lema 2: horizonte T*~2πλ² (independiente de la escala de ε₀).
- **Espectro relativo {ε_k/ε₀}=(k+1)²** — son RATIOS, no dependen de la escala absoluta. ✔
- Paridad alternante, colapso de perfiles φ_k(x) — son autovectores, escala-independientes. ✔
- Existencia de 𝓛 (de la convergencia del espectro relativo + autovectores). ✔
- Argumento #3 (reescalar por ε₀ → fondo aislado → Galerkin): el ARGUMENTO sobrevive; sólo ε₀ es mucho más chico. ✔
- Beurling–Deny: A_λ=∫q|f|²+𝓔_θ+𝓔_prime; c=−ψ''(¼)/8; M_0,M_2~λ^{1/2−|x|}. ✔ (Consistencia: los términos B–D son O(λ^{1/2}) y cancelan a ε₀~e^{−cλ²logλ} — cancelación super-precisa = el minimizador anula TODOS los ceros = positividad de Weil casi-saturada. OK.) ## CAE (toda interpretación de la ESCALA ABSOLUTA de ε₀)
- **"Acción S≈1":** −log ε₀/L = cλ²logλ/(2logλ) = cλ²/2 → ∞, NO 1. **MUERTA.** Era artefacto.
- **"ℏ=1/L semiclásico" para la escala:** la escala NO es e^{−S/ℏ}=e^{−SL}; es e^{−cλ²logλ}. La interpretación WKB de la ESCALA cae. (La corrección O(1/L) del espectro RELATIVO sobrevive, es ratio.)
- **"e^{−L} tunneling":** muerto (artefacto N-limited).
- **"ε₀ converge en N":** AFIRMACIÓN PREVIA FALSA. ε₀ NO converge — sigue bajando con N (el horizonte efectivo ~N·2π/L crece hacia T*). Lo que vi (N=8→24, ratios→1.1) era aproximación lenta, NO convergencia. [Test: eps0_highN.py — debe seguir bajando.] ## EXPLICA los datos previos (consistencia)
El operador a N=24 para λ=3.7 y 5 dio −log ε₀~46 casi constante. NO porque sea la escala real,
sino porque ambos estaban **N-limited al mismo horizonte efectivo (~50)**: ε₀~e^{−c·n(horizonte
efectivo)}, y horizonte efectivo ~50 en ambos ⟹ ε₀ similar. La escala real (N→∞, horizonte T*)
es e^{−c·n(T*)}~e^{−cλ²logλ}, nunca alcanzada por el operador N-limited. ## Veredicto de consistencia [CORREGIDO por el test eps0_highN]
TEST (λ=3.7, N=16..36): ε₀ CONVERGE (−log ε₀ plateau ~46.0, Δ→0.01) y a N=36 el horizonte
alcanza T*=86 completo. ⟹ **mi predicción "ε₀ no converge en N" era FALSA — RETRACTADA.**
ε₀ SÍ converge (la afirmación original era correcta). **ACTUALIZADO con λ=5 convergido (experimento discriminante):**
- **ε₀ converge en N** (verificado λ=3.7 N=36=T*, λ=5 N=75≈T*). Retracto "ε₀ no converge".
- **Dos puntos convergidos:** (λ=3.7,L=2.62)→−log ε₀=46.03; (λ=5,L=3.22)→46.66. Pendiente≈1.05.
- **λ²logλ (Jensen del producto desnudo) REFUTADA:** predecía −log~103 a λ=5; real 46.7.
- **e^{−L} RESTABLECIDO como hipótesis de trabajo:** ε₀≈C₀e^{−SL}, S≈1.05≈1, C₀≈e^{−43.3}. (Lo que confundió antes: la constante C₀~e^{−43} domina el valor absoluto ~46, pero la PENDIENTE en L es ~1 = e^{−L}.) El fenómeno NUEVO a explicar es C₀ grande (−log C₀≈43). SOBREVIVE: lo relativo (𝓛, (k+1)², #3, Beurling–Deny, c, M₀/M₂) + ε₀~C₀e^{−SL} con S≈1.
CAE/REFUTADO: λ²logλ (Jensen desnudo); "ε₀ no converge". Jensen sigue relevante (estructura del
producto) pero NO controla ε₀ (normalización + extremal del frame; cautela 4A′ de correcta). ## Implicación para Objetivo B
B ya no es "probar e^{−L}". Es **"probar −log ε₀ ~ c·n(T*)"**, con:
- minimizador identificado (= producto canónico, Thm 1.1.iii + Hadamard);
- orden líder derivado de DENSIDAD (PNT) = no-circular;
- falta: normalización rigurosa + cota inferior (de Branges) + la constante c (4B, posible dependencia de posición fina cerca del horizonte).
