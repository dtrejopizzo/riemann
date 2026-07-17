# Reparación de los dos puntos de máxima severidad: E1 y III Auditoría → reparación, matemática pura. Honesto: III se repara como teorema condicional
limpio; E1 resulta MÁS grave de lo que el flag indicaba (la prueba registrada es falsa y la
correcta es no trivial). --- ## E1 — real-rootedness: la prueba registrada es FALSA (contraejemplo) y la correcta es difícil ### El contraejemplo que mata la prueba registrada `rh-proof.tex` Thm 3.1 dice: *"con `ξ_k>0`, `f(s)=Σξ_k/(s−d_k)` va `+∞→−∞` entre polos
consecutivos ⟹ una raíz real por hueco."* El paso usa **`ξ_k>0`**. Pero el autovector
fundamental real **no** es de signo definido (E12: 14–18 cambios de signo en dim 29–33,
porque `v_0(k) ≈ u_k cos(ω*k+φ)`, carrier de borde `ω*=0.966π`). **Contraejemplo concreto** de que sin `ξ_k>0` el argumento falla: tomar `ξ=(−1,2,−1)` en
`d=(−1,0,1)` (par, con cambios de signo). Entonces
``` f(s) = −1/(s+1) + 2/s − 1/(s−1) = −2/(s³−s).
```
El numerador es la **constante `−2`**: `f` no tiene **ninguna** raíz finita. Un vector
par con cambios de signo produce una secular **sin raíces reales**. ⟹ El argumento de
interlacing **no aplica** al `ξ` real, y la real-rootedness **no se sigue** de él. ### Por qué la real-rootedness igual es cierta — y por qué probarla es duro Empíricamente las raíces SON reales (el motor reproduce los ceros de ζ). La estructura
verdadera: `ξ_k = u_k cos(ω*k+φ)` con `u_k>0` (envolvente positiva de H1) y carrier de
borde `ω*≈0.966π`. Evaluando `ξ̂` en el retículo, `ξ̂(d_j)=ξ_j(L/2)(−1)^j`, que **no
alterna** de forma simple (carrier near-Nyquist) — así que el viejo cuadro "una raíz por
hueco" tampoco describe la realidad. **El marco correcto es Hermite–Biehler / de Branges:** una función entera real `ξ̂` tiene
sólo ceros reales ⟺ pertenece a la clase HB (⟺ `|E(s̄)|<|E(s)|` en el semiplano superior,
con `ξ̂` la parte real de la función de estructura `E`). La real-rootedness debe seguirse de
la **positividad de H1** (Perron–Frobenius, `Λ(n)≥0`) **traducida a la propiedad HB** — pero: - H1 da un autovector positivo en la representación **de-modulada** (envolvente `u_k>0`), no en la base sinc cruda.
- Conectar "PF-positividad de la envolvente" con "HB de `ξ̂` (carrier near-Nyquist incluido)" es **no trivial** y **no está hecho** en el programa. ### Estado honesto de E1 tras la auditoría
- La real-rootedness es **empíricamente cierta** y es **CCM Thm 1.1(iii)** dado H1+H2 (hipótesis que el programa probó). Pero **la prueba que registramos en el `.tex` es falsa** (contraejemplo arriba) — era una sobre-simplificación equivocada.
- La prueba correcta (HB/de Branges desde la positividad de H1, con el carrier de borde) **queda como reparación abierta**. Hasta cerrarla, E1 baja de ✅ a **🔧**: real-rootedness cierta, demostración self-contained **pendiente** (o se cita CCM Thm 1.1(iii) como caja negra, lo cual es legítimo pero no es "lo demostramos nosotros").
- **Impacto:** E1 alimenta Hurwitz (E3) y N5c. Ambos heredan el "🔧": son correctos **módulo la real-rootedness**, que es cierta pero cuya prueba propia falta. **Severidad real: ALTA.** No es un detalle expositivo — es que NO tenemos una demostración
propia de la real-rootedness; dependemos de CCM Thm 1.1(iii). Hay que (a) citarlo
honestamente como caja negra, o (b) probar HB-desde-H1 nosotros (reparación matemática real). --- ## III — estabilidad relativa: reparada como TEOREMA CONDICIONAL limpio III estaba marcada ✅ pero descansa en dos hipótesis no probadas. La reparo enunciándola
correctamente como condicional, con las hipótesis explícitas y verificando que, **dadas
ellas**, la prueba es correcta. ### Por qué la forma absoluta falla (recordatorio)
Davis–Kahan ingenuo: `‖δξ̂‖ ≤ ‖δA‖/(ε_1−ε_0)`. Pero `ε_1−ε_0 ≈ 3ε_0 ≈ 10^{−20}`
(gap absoluto poli/exp-pequeño) ⟹ cota inútil. La renormalización `Â=A/ε_0` lo arregla
**sólo si** el gap relativo es `O(1)`. ### Teorema III (condicional, enunciado correcto) **Hipótesis:**
- **(H-gap)** `inf_λ ε_1(λ)/ε_0(λ) = 1+γ` con `γ>0` (gap relativo uniforme). [= IV.1★]
- **(H-lim)** los ground states renormalizados forman familia de Cauchy: `‖ξ̂_λ − ξ̂_{λ'}‖_{L²} → 0` cuando `λ,λ'→∞` (equivalente: `Â_λ` converge en el bloque bajo). [= Conj 2b] **Tesis:** existe `ξ̂_∞:= lim ξ̂_λ` y
``` ε_loc(λ) ≤ (C/γ)·√(logλ)·η(λ) + C λ³ e^{−πλ²},
```
con `η(λ):=‖Â_λ−Â_∞‖_{low}→0` el módulo de convergencia. **Prueba [P, dada (H-gap)+(H-lim)]:** Por (H-gap) el bottom de `Â_λ` está aislado con gap
`γ>0`; Davis–Kahan da `‖ξ̂_λ−ξ̂_∞‖_{L²} ≤ η(λ)/γ`. Nikolskii (`‖g‖_∞≤C√(logλ)‖g‖_{L²}`,
tipo `logλ`) ⟹ `‖ξ̂_λ−ξ̂_∞‖_∞ ≤ (C/γ)√(logλ)η(λ)`. Sumando `‖Ξ_T−Ξ‖≤Cλ³e^{−πλ²}` (Thm 1)
y, **si además `ξ̂_∞=Ξ`** (= IV.2, RH-equivalente), se obtiene la cota de `ε_loc`. ∎ ### Estado honesto de III tras la reparación
- **(H-gap)**: sólo numérico (`ε_1/ε_0→4`). **No probado.** Es IV.1★.
- **(H-lim)**: sólo numérico (espectro relativo converge). **No probado.** Es Conj 2b.
- La tesis usa además **`ξ̂_∞=Ξ`** = IV.2, que es **RH-equivalente**.
- ⟹ III baja de ✅ a **teorema condicional** `[(H-gap) ∧ (H-lim) ⟹ cota]`, con la cota útil sólo si además IV.2. **Honesto:** III es correcto como implicación; sus hipótesis no están probadas; no es un teorema incondicional. **Reparación lograda:** III queda **correctamente enunciada** (condicional, hipótesis
explícitas, prueba válida dada ellas). El cabo de **normalización** (`ξ̂` salvo escala vs
`Ξ`) se fija aquí pidiendo `‖ξ̂_λ‖_{L²}=1` y comparando contra `Ξ_T/‖Ξ_T‖_{L²}` — la cota
`η(λ)` y `ε_loc` se entienden con esa normalización L² común. (Esto resuelve el cabo 🟠 de
normalización para III/N2/Thm 2.) --- ## Resumen de las dos reparaciones | | antes | después de la auditoría/reparación |
|---|---|---|
| **E1** | ✅ PROBADO | **🔧 real-rootedness cierta pero prueba propia FALSA**; correcta = HB/de Branges-desde-H1 (abierta) o citar CCM Thm 1.1(iii) como caja negra |
| **III** | ✅ PROBADO | **teorema CONDICIONAL** `[(H-gap)+(H-lim) ⟹ cota]`, hipótesis sólo numéricas; normalización L² fijada | **Lección de la auditoría:** dos ✅ bajan a estado honesto. E1 es el más serio: creíamos
tener la real-rootedness demostrada y resulta que la prueba registrada es refutable por
contraejemplo; la real-rootedness es cierta (CCM) pero **demostrarla nosotros vía
HB-desde-positividad es trabajo matemático real pendiente**. III se salva como condicional
limpia y de paso fija la normalización.
