# Auditoría de δV: densidad o posición — y verificación del "polo" Documento de trabajo (post-LaTeX, en.md). Audita el último GAP de la cascada
Eslabón 2 / ε₀≥0: la discrepancia δV = V_λ − Kφ₀/φ₀. Marcadores: **[P]** probado · **[N]** numérico robusto · **[O]** abierto. --- ## 0. Contexto: la cascada hasta acá ```
A_λ ⪰ 0 ⟺ (Schur) (i) K−V ⪰ 0 sobre φ_polo^⊥ + (ii) escalar b+κ ≥ r*M⁺r
(i) ⟸ (FLS, no-local) K−V₀ ⪰ 0 sobre φ_polo^⊥ [P] + cota de δV = V_λ−V₀ [O]
```
- Schur: **[P]** (álgebra exacta).
- Frank–Lieb–Seiringer (representación de estado fundamental): **[P]**, resuelve la no-localidad para el potencial de estado fundamental V₀ = Kφ₀/φ₀.
- Queda: la cota de δV sobre φ₀^⊥, y la escalar (ii). --- ## 1. Verificación previa: ¿φ₀ es el modo-polo? (era un riesgo de conflación) La cascada usa **dos** objetos que ambos se llamaron "φ_polo":
1. **φ₀** = autovector fundamental de A_λ en E_λ (donde vive ε₀, la dirección de riesgo).
2. **u_polo** = dirección uniforme en el espacio de *pesos de primos* (vía #9, densidad global = polo s=1, incondicional). La cascada **requiere** que coincidan (que P, sobre u_polo, actúe sobre φ₀). ### Test numérico (decisivo) | precisión | ε₀ | overlap φ₀·U₀ | peso baja-frec | masa centro/borde | lectura |
|---|---|---|---|---|---|
| float64 | ~1e-15 (ruido) | 0.003 | 0.025 | 0.32 / 1.52 | "edge-localized, ⊥ polo" → **FALSO** |
| **mpmath dps=40** | **9.28e-21** | **0.76** | **0.996** | **0.52 / 0.51** | **φ₀ suave = modo-polo** | **[N, robusto] φ₀ ES el modo suave tipo polo:** 99.6% baja-frecuencia, 76% overlap con
el modo constante. El "edge-localized" de float64 era **ruido** (autovalor ~1e-15 bajo
el piso de máquina; misma trampa que la vía #9). **Corrección de registro:** la caracterización previa "autovectores edge-localized con
anulación central" es muy probablemente **artefacto de float64**. El ground state
verdadero es suave / polo-alineado. **Consecuencia:** la conflación NO es un crack. φ₀ ≈ u_polo. El mecanismo de la cascada
(el polo actúa sobre la dirección de riesgo) **se sostiene**. --- ## 2. La auditoría de δV: ¿densidad o posición? Con φ₀ suave confirmado, V₀ = Kφ₀/φ₀ es el **potencial de campo medio suave**, y
δV = V_λ − V₀ es **la fluctuación de los primos alrededor de la media**. ### Argumentos de que δV es DENSIDAD (Escenario A) 1. **V_λ es finito y entero.** V_λ(w) = Σ_{n≤λ²} (Λ(n)/√n)·[masa en log n]. Es un polinomio de Dirichlet truncado: **sin polos, sin ceros**. No "contiene" la posición de ningún cero. Los ceros sólo aparecerían si se relacionara V_λ con −ζ'/ζ *completa*; pero la cota que necesitamos es sobre V_λ *directamente*.
2. **δV es puramente aritmético:** primos (V_λ) menos media suave (V₀ = Kφ₀/φ₀, con K arquimediano y φ₀ smooth). Ningún cero.
3. **Su tamaño lo controla el término de error del PNT.** La fluctuación Σ_{p≤λ²}(...) − (media) es exactamente lo que acotan las **regiones libres de ceros clásicas (Vinogradov–Korobov)**: input incondicional, **no usa Θ=½**. ### El único resto: suficiencia cuantitativa [O] La cota (i) cierra ⟺
``` ∫ δV |g|² ≤ β_λ ‖g‖² ∀ g ∈ φ₀^⊥,
```
con β_λ la brecha de Hardy mejorada (remanente FLS). Es una **carrera cuantitativa**:
- **lado δV:** cota clásica por regiones libres de ceros ~ λ²·exp(−c(log λ)^{3/5}) o similar (término de error PNT incondicional).
- **lado β_λ:** la brecha del remanente FLS, ~ orden de ε-gaps de la torre (k+1)², esperable ~ C₀/λ² o (log λ)^{−A}. **No es una equivalencia con RH.** Es: ¿la cota incondicional de δV (densidad) es
< β_λ? Si sí → (i) cierra de forma no-circular. Si la cota clásica no alcanza y hace
falta δV ~ RH-óptimo → reentra el Escenario C. ### Dónde puede esconderse el Escenario C (lo que hay que vigilar) - Si β_λ decae *más rápido* que la cota clásica de δV, la carrera se pierde por densidad y habría que ajustar δV con info fina (posición) → C.
- La proyección a φ₀^⊥ podría *no* matar la parte de δV que correlaciona con la estructura de ceros. Hay que verificar que δV sobre φ₀^⊥ es genuinamente la fluctuación "blanca" (PNT) y no retiene un eco de Σ_ρ. --- ## 3. Veredicto del audit - **[N]** φ₀ = modo-polo suave: confirmado en mpmath. La conflación temida NO existe; la cascada se sostiene. (Float64 daba un falso "edge-localized".)
- **[P/argumentado]** δV es del **lado densidad**: objeto aritmético finito (primos + media suave), sin ceros explícitos; su tamaño lo gobiernan regiones libres de ceros clásicas (no Θ=½). **Se inclina a Escenario A.**
- **[O]** La **suficiencia cuantitativa** (cota clásica de δV < β_λ) es lo único que queda para (i), más la escalar (ii). Es una carrera de tamaños, computable. **Lectura honesta:** el audit no rompió la cascada — al contrario, descartó una posible
conflación (vía mpmath) y mostró que δV vive del lado densidad. Pero **traslada** el
problema a dos cotas cuantitativas (δV y la escalar (ii)) cuya suficiencia hay que
*calcular*, no asumir. El Escenario C no está excluido: podría reentrar si β_λ decae más
rápido que la cota incondicional de δV. ## 4. Próximo paso concreto Medir numéricamente las **dos magnitudes de la carrera**:
1. **β_λ** = brecha del remanente FLS = menor autovalor de (K−V₀) sobre φ₀^⊥ (computable: K, V₀=Kφ₀/φ₀, proyectar).
2. **‖δV‖ sobre φ₀^⊥** = norma de la fluctuación primos−media proyectada. Si β_λ ≳ ‖δV‖_{φ₀^⊥} numéricamente (y la tendencia en λ se mantiene), Escenario A toma
fuerza cuantitativa. Si ‖δV‖ domina, hay que entender por qué y si la proyección ayuda.
Esto es **calculable** con las matrices ARCH, ARITH ya construidas + φ₀ en mpmath. --- ## 5. Medición de la carrera (mpmath dps=40, λ=3.7/5/7) ### Lado izquierdo: β_λ (margen de Hardy mejorada sobre ℓ^⊥) | λ | ε₀ | β_λ = min A_λ|_{ℓ⊥} | β_λ/ε₀ |
|---|---|---|---|
| 3.7 | 1.67e-20 | 7.59e-20 | 4.53 |
| 5 | 1.00e-20 | 3.78e-20 | 3.79 |
| 7 | 5.81e-21 | 2.30e-20 | 3.95 | **[N] β_λ ≈ 4ε₀, estable.** La dirección-polo ℓ carga TODO el riesgo (ahí el form vale
ε₀, el mínimo); al proyectarla fuera, la margen salta a ~4ε₀. **El remanente positivo de
Brezis–Vázquez es real y robusto (4×).** Confirma el cuadro de Hardy mejorada. ### Alineación de la dirección de riesgo con el polo | λ | overlap(φ₀, ℓ) | torre |
|---|---|---|
| 3.7 | 0.771 | ε₁/ε₀=4.58, ε₂/ε₀=9.14 |
| 5 | 0.782 | 3.86, 9.08 |
| 7 | 0.797 | 4.07, 9.05 | **[N]** φ₀ está ~78% alineado con el funcional-polo ℓ (=e^{u/2}), **creciendo con λ**
→ tiende a alinearse más. Torre (k+1)² confirmada. ### Lectura honesta de la carrera - **Lado izquierdo β_λ ≈ 4ε₀ ~ 4C₀/λ²:** medido, positivo, estable. La Hardy mejorada tiene holgura 4× sobre ℓ^⊥.
- **CAVEAT decisivo:** esto es data RH-true. El β_λ medido ya COMBINA la positividad FLS (β_FLS) y la corrección δV — no los separa. Que el neto sea +4ε₀>0 dice que **δV NO domina a β_FLS** (empíricamente, para esta data), pero no aísla δV.
- **Lo que NO puede dar la numérica:** la separación β_FLS vs δV es analítica (sólo tenemos data con ceros en línea). La prueba incondicional necesita β_FLS ≥ δV probado del lado primo. ## 6. Síntesis del estado (post-medición) **Confirmado numéricamente [N]:**
- Torre (k+1)²; φ₀ polo-dominante (78%, creciente); β_λ≈4ε₀>0 estable.
- La estructura de Hardy mejorada (déficit en el extremal-polo, complemento positivo) es REAL, no supuesta. **Lo que falta, ahora puramente analítico [O]:**
1. β_FLS ≥ δV sobre ℓ^⊥, incondicional (δV = fluctuación de primos, lado densidad).
2. La escalar de Schur (ii) sobre la dirección-polo. **Veredicto:** la cascada pasó todas las verificaciones numéricas que podían romperla.
No es circular ni vacua. Lo que queda son dos desigualdades aritméticas concretas cuya
prueba es analítica (no numérica), porque la numérica sólo accede al régimen RH-true.
El frente está vivo y localizado al milímetro.
