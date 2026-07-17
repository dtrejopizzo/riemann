# Eslabón 2-blando como teorema de aproximación + la frontera exacta con lo duro Reencuadre Mundo A (positividad) / Mundo B (convergencia). Este documento formaliza
el objeto del Mundo B que NO nace de RH/Weil/de Branges: la descomposición
banda + piso Euler. Y aísla, en lenguaje de aproximación, el único upgrade que es duro. **[P]** probado · **[N]** numérico · **[O]** abierto · **[GAP]** paso a probar. --- ## 0. Los dos mundos (mapa acordado) | | Mundo A — Positividad | Mundo B — Convergencia |
|---|---|---|
| objetos | A_λ, ε₀, 𝓛, (k+1)² | ξ̂_{λ,N}, Ξ, truncación Euler, T* |
| pregunta | A_∞ ⪰ 0 ? | ξ̂_{λ,N} → Ξ ? |
| tradición | Weil / de Branges / Hilbert–Pólya | teoría de aproximación |
| naturaleza del error | autovalor mínimo | banda e^{−cλ²} + piso Euler | **Tesis:** el Mundo B tiene dinámica propia (banda + Euler), que NO pasa por 𝓛.
Las fases previas atacaban B con objetos de A. Acá tratamos B en sus propias variables. --- ## 1. Teorema objetivo (E2-blando): convergencia LOCAL en el eje real **Enunciado (target).** Fijado n, sea ρ̂_n(λ,N) el n-ésimo cero real de ξ̂_{λ,N} y
γ_n el n-ésimo cero de Ξ. Existe λ_n tal que para λ ≥ λ_n (y N → ∞ tomado),
``` | ρ̂_n(λ) − γ_n | ≤ C_banda · e^{−c (T*(λ) − γ_n)} + C_Euler · 𝓔_λ(γ_n),
```
con:
- **T*(λ) ~ 2πλ²** el horizonte de Nyquist (Lema 2, densidad de ceros = densidad de muestreo en T*);
- **𝓔_λ(γ_n)** la cola de truncación de Euler a primos ≤ λ², controlada por PNT. Ambos términos son **incondicionales** y **no mencionan la posición de los ceros off-line**.
Es convergencia *local* (cada γ_n fijo, dentro del horizonte móvil). ### Estado de los dos términos **Término de banda [N→GAP]:** medido e^{−cλ²} (c≈11, λ=2.0–2.3, primos fijos {2,3}).
Es el error de aproximación band-limited: ξ̂_{λ,N} ∈ PW_{L/2} (tipo L/2=logλ), y aproximar
γ_n (interior al horizonte) tiene error exponencial en la "sala" T*−γ_n.
- **[GAP] Prueba:** desigualdad de Beurling–Selberg / Plancherel–Pólya para el residuo de interpolación a densidad crítica. Herramienta clásica; falta la constante c y la uniformidad. No usa ceros off-line (sólo densidad). **Término Euler [N→GAP]:** medido < 1e-19 ya con primos ≤13 (ultrarrápido). Es el resto
de la fórmula explícita truncada, R_λ(½+iγ_n) (cf. weil-remainder-attack).
- **[!] Subtileza honesta:** R_λ ~ Σ_ρ (λ²)^{ρ−s} ES sensible a Re ρ. PERO para γ_n FIJO y dentro del horizonte, la cola que importa es la de primos > λ², y su efecto sobre el cero ya resuelto es de orden PNT (regiones libres de ceros clásicas), no la posición de los γ globales. La sensibilidad RH aparece sólo en el régimen UNIFORME (ver §3), no en la convergencia local de un cero fijo. **Lectura:** E2-blando = convergencia local de cada cero, gobernada por Nyquist (banda)
+ PNT (Euler). Incondicional. Es el "quick win" que además **escribe la frontera**. --- ## 2. Por qué E2-blando NO da RH (y está bien que no) La convergencia local ρ̂_n(λ) → γ_n es sobre el **eje real**: dice que el n-ésimo
autovalor real del modelo finito converge al n-ésimo γ_n. **No constata que ρ_n esté en
línea**, porque γ_n es la altura (parte imaginaria), que existe esté ρ_n on u off line. Para RH hace falta que la convergencia **vea la parte real** β_n de ρ_n, lo cual requiere
convergencia en un **entorno COMPLEJO** del eje (Hurwitz), no sólo en el eje real. --- ## 3. La frontera exacta: LOCAL (blando) → UNIFORME-EN-FRANJA (duro) Acá está el corazón, en lenguaje de aproximación (no de positividad): - ξ̂_{λ,N} es entera de **tipo exponencial L/2 = log λ** (band-limited).
- Por Paley–Wiener, un aproximante de tipo log λ matchea Ξ en una franja compleja de ancho **~ 1/log λ → 0**. La franja **se angosta** con λ.
- Un cero off-line ρ₀ = ½+β₀+iγ₀ está a profundidad **fija** δ₀ = β₀ del eje real (en variable t). Para que ξ̂_{λ,N} lo "capture" (y Hurwitz fuerce β₀=0), la franja de ancho 1/logλ tendría que alcanzar profundidad δ₀ — que es fija. **No alcanza.** ### El cálculo que CASI cierra (y por qué falla) Error en el eje real ~ e^{−cλ²} (banda, super-rápido). Continuación a profundidad δ
amplifica por el tipo: factor ~ e^{δ·logλ} = λ^δ. Producto:
``` error a profundidad δ ~ λ^δ · e^{−cλ²} → 0 (∀ δ fijo, λ→∞).
```
**Si esto fuera la sup-norma real, daría convergencia uniforme en franja fija ⟹ RH.** **Por qué falla [!]:** e^{−cλ²} es el error de los CEROS (local), no la **sup-norma**
|ξ̂_{λ,N} − Ξ| en un intervalo real. ξ̂_{λ,N} es band-limited y Ξ no; su diferencia en
sup-norma NO es e^{−cλ²} uniformemente — sólo cada cero converge así, localmente. Sin
cota sup-norma uniforme no hay nada que amplificar off-axis. ### ⟹ La pregunta dura, en variables de aproximación ``` ¿La convergencia LOCAL de los ceros (e^{−cλ²}, incondicional) se puede UPGRADEAR a convergencia UNIFORME en sup-norma en un intervalo real, con control de tipo suficiente para una franja de ancho FIJO?
``` - **Si sí ⟹ RH** (Hurwitz + amplificación off-axis).
- **Es una pregunta de de Branges / Paley–Wiener / Beurling**, NO de positividad de Weil.
- **No sabemos si es RH-por-necesidad o RH-por-formulación.** Esta es la frontera precisa que tu colaborador pedía escribir. --- ## 4. Qué cambia esto (honesto) **No escapamos la RH-hardness todavía.** Pero **reubicamos el muro** de
"positividad / posición de ceros" a una pregunta **limpia de teoría de aproximación**: > upgrade de convergencia local (incondicional) a uniforme-en-franja-fija, con tipo log λ. Esto es un **objeto nuevo del Mundo B**, distinto de A_∞⪰0. Las herramientas candidatas
son de aproximación (Beurling–Selberg, Plancherel–Pólya, espacios modelo, de Branges
sin positividad), no de positividad. **Por primera vez el Eslabón 2-duro está escrito
sin nombrar a Weil ni a los ceros**: es "uniformidad de tipo en band-limited". ## 5. Plan 1. **[GAP] Probar E2-blando** (Teorema §1): cota local banda+Euler, incondicional. Formaliza la frontera. Herramientas: Beurling–Selberg (banda), PNT (Euler).
2. **[O] Atacar el upgrade §3** como problema de aproximación: ¿la sup-norma real converge?, ¿con qué tipo efectivo? Aquí se decide necesidad vs formulación. **Lo nuevo:** dejamos de preguntar "¿A_∞⪰0?" y empezamos a preguntar "¿uniformidad de
tipo en la convergencia band-limited?". Mismo muro tal vez — pero **otra cara, otras
herramientas**, y la primera que no nació de RH/Weil/de Branges-positividad.
