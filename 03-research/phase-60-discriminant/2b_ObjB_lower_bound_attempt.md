# Objetivo B — intento de prueba de la cota inferior de ε₀ (transparente, con [GAP]) **Meta:** acotar por debajo ε₀(λ) = min_{g∈PW_{L/2}, ‖g‖=1} Σ_j |g(γ_j)|² (frame operator de los
ceros γ_j en PW_{L/2}; L=2logλ). Escala conjeturada ε₀ ~ C e^{−S L}, S≈1 (target no firme). Marcadores: [OK] paso riguroso · [GAP] paso inferencial que NO tengo justificado. --- ## Paso 1 [OK] — reducción al residual sobre el horizonte
g∈PW_{L/2} es entera de tipo L/2. Por Jensen, su densidad de ceros ≤ L/2π. Los γ_j tienen
densidad local (1/2π)log(T/2π), que iguala L/2π en T*=2πλ² (Lema 2). ⟹ g puede anularse en
los γ_j con T≤T* (interpolación posible) pero NO en todos los de T>T* (sobre-densidad). Luego ε₀ = min_{g∈PW_{L/2},‖g‖=1, g(γ_j)=0 ∀γ_j≤T*} Σ_{γ_j>T*} |g(γ_j)|² + (correcciones).
El minimizador se anula bajo T* y deja residual arriba. ## Paso 2 [OK] — el minimizador es el producto canónico truncado
La g óptima que se anula en {γ_j ≤ T*} y es de tipo L/2 es (módulo normalización) el producto
canónico P_{T*}(z) = ∏_{γ_j≤T*}(1 − z/γ_j)·e^{z/γ_j}, que tiene tipo exponencial ~ (densidad)·π
= (n(T*)/T*)·π → L/2 (usa exactamente la banda; Lema 2). P_{T*} es la truncación a tipo L/2 de
ξ. ⟹ ε₀ ≍ ‖P_{T*}‖^{−2} · Σ_{γ_j>T*} |P_{T*}(γ_j)|². ## Paso 3 [OK] — el residual es la cola del producto más allá del corte
Para γ_k > T* (primer cero arriba del horizonte), P_{T*}(γ_k) = ∏_{γ_j≤T*}(1−γ_k/γ_j)e^{γ_k/γ_j}
≠ 0. La magnitud |P_{T*}(γ_k)| / ‖P_{T*}‖ es el residual. Reescribiendo log: log|P_{T*}(γ_k)| = Σ_{γ_j≤T*} [log|1−γ_k/γ_j| + γ_k/γ_j].
Con γ_k ≈ T* y γ_j recorriendo {≤T*}: es una suma sobre ~n(T*)=λ²L/(2π)·(…) términos. ## Paso 4 [GAP] — la asintótica de la cola = teorema extremal de de Branges
Falta: la asintótica de R(λ):= ‖P_{T*}‖^{−2} Σ_{γ_j>T*} |P_{T*}(γ_j)|²
cuando λ→∞. Es decir, cuánto vale el residual del producto canónico truncado a tipo L/2,
evaluado justo arriba del horizonte, normalizado. **[GAP]** No tengo el argumento que da R(λ) ~ C e^{−SL}. Lo que se necesita: (a) controlar log‖P_{T*}‖ (norma del producto truncado) — vía la fórmula de Jensen/contar ceros, conectado con la fórmula explícita; (b) controlar log|P_{T*}(γ_k)| en el primer cero arriba de T* — la "cola" del producto; (c) la diferencia (b)−(a) da log R; mostrar que = −SL + O(1). Esto es la asintótica de productos canónicos en el régimen de densidad crítica = teoría de de Branges / Beurling–Selberg. Es el único paso ausente. ## Lo que el [GAP] necesitaría como input (para quien lo cierre)
- La regularidad de la distribución de ceros cerca de T* (espaciado ~2π/L, fluctuaciones). Bajo RH esto se controla; SIN RH, sólo por densidad (PNT) — y ahí está la pregunta de no-circularidad: ¿basta la DENSIDAD (PNT) para (a)-(c), o se necesita la posición fina (≈ RH)? Si basta densidad ⟹ B no-circular. Si necesita posición ⟹ B es RH-dependiente.
- Una estimación tipo Beurling–Selberg para el residual de interpolación a densidad crítica. ## Paso 4A [COMPUTADO] — CORRECCIÓN del scaling (Jensen, densidad pura) Integral de Jensen log|P_{T*}(x)| ≈ ∫_0^{T*}log|1−x²/t²|·(1/2π)log(t/2π)dt (sólo densidad).
Computado: J(T*)−min_x J crece como **c·λ²·logλ = c·n(T*)** (nº de ceros bajo el horizonte):
λ=3.7→19.9, 5→51.6, 7→137, 10→364, 15→1043, 25→3708. (J(T*)−minJ)/L CRECE (no constante). **[RETRACTADO] La "corrección" −log ε₀ ~ c·λ²logλ era FALSA.** El experimento discriminante
(ε₀ convergido a λ=5, sector par, N=75≈T*) la refutó: predecía −log ε₀~103 a λ=5, el valor real
es 46.7. La integral de Jensen describe el crecimiento del producto canónico DESNUDO, NO ε₀ —
por la normalización ‖·‖ y el ser autovalor del frame (cautela 4A′ de, correcta). **Estado real (dos puntos convergidos):** (λ=3.7,L=2.62)→−log ε₀=46.03; (λ=5,L=3.22)→46.66 ⟹
pendiente≈1.05 ⟹ **ε₀ ≈ C₀·e^{−SL}, S≈1, C₀≈e^{−43.3}** (hipótesis de trabajo restablecida; el
e^{−L} original era correcto en el exponente). El fenómeno nuevo a explicar es C₀ grande
(−log C₀≈43): domina el valor absoluto pero no la pendiente en L. ## Cotas rigurosas que SÍ enmarcan el [GAP]
- [OK] ε₀ > 0 (completitud, Paso 1 + Jensen).
- [OK] ε₀ ≤ C/L² (test sinc).
⟹ el [GAP] vive en el intervalo (0, C/L²], y lo que falta es la asintótica precisa de R(λ). ## Diagnóstico honesto de no-circularidad (lo más valioso del intento)
El [GAP] se reduce a (a)-(c), que son sumas Σ_{γ_j≤T*} f(γ_j) sobre ceros. Por la fórmula
explícita, Σ_{γ_j} f(γ_j) = (arquimediano) − Σ_p (primos). ⟹ las sumas (a)-(c) **se expresan
vía primos (PNT)** si f es suave. PERO log|1−γ_k/γ_j| tiene una SINGULARIDAD en γ_j→γ_k (cerca
del horizonte): los términos con γ_j cercano a T* dominan y NO son suaves. ⟹ el control de esos
términos cercanos requiere la POSICIÓN fina de los ceros cerca de T*, no sólo la densidad. **Indicio (no prueba):** B podría ser RH-dependiente vía los términos singulares cerca del horizonte. Ése es el punto exacto a decidir — y es donde de Branges/ deben mirar.
