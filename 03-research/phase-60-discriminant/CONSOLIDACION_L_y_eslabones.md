# Consolidación — caracterización de 𝓛, mapa de eslabones, lo probado vs lo inferido Para revisión de /. Distingue rigurosamente: [P] probado · [N] establecido
numéricamente (inferencia robusta) · [O] abierto (matemática dura). --- ## 1. MAPA DE ESLABONES (0 → 4): el camino CCM ⟹ RH | Eslabón | Enunciado | Estado |
|---|---|---|
| **0** Construcción | cada (λ,N) define ξ̂_{λ,N} entera | **[P]** engine validado (ceros a 1e-15) |
| **1** Real-rootedness finita | ξ̂_{λ,N} tiene SOLO raíces reales, incondicional | **[P]** H1+H2 (Perron–Frobenius, Λ≥0) + Thm 1.1.iii |
| **2** Convergencia | ξ̂_{λ,N} → Ξ localmente uniforme | **[O]** EL HUECO (objetivos A, B abajo) |
| **3** Hurwitz | real-rooted + conv. uniforme ⟹ Ξ real-rooted | **[P]** clásico |
| **4** Equivalencia | Ξ real-rooted ⟺ RH | **[P]** clásico | **0,1,3,4 cerrados. Todo se reduce al Eslabón 2.** Por Eslabón 1, la real-rootedness finita es
GRATIS e incondicional ⟹ el contenido RH vive SÓLO en la convergencia (Eslabón 2). ## 2. DENTRO DEL ESLABÓN 2: lo probado y lo que falta **[P] Probado / derivado de matemática real:**
- (i) restricción exacta A_λ = A_∞|_{E_λ} (primos >λ² contribuyen 0 por soporte).
- Forma de muestreo de Weil: A_λ(f,f)=Σ_ρ f̂(ρ)conj(f̂(1−ρ̄)).
- **Lema 2 (horizonte):** T*~2πλ² (tipo exp ↔ densidad de ceros ↔ PNT). Independiente, fuerte.
- **c = −ψ''(¼)/8** (coef. cinético arquimediano, exacto, 2 vías).
- **M₀,M₂ ~ λ^{1/2−|x|}** (momentos aritméticos de frontera, PNT).
- Descomposición de Beurling–Deny + cota superior de forma (𝓔_θ ≤ C₂∫|f'|²).
- ε₀: >0 (completitud); ≤O(1/λ²); minimizador = producto canónico (Hadamard+Thm 1.1.iii).
- **Reducción de Fourier:** A_λ(f,f)=(1/2π)∫|f̂|²W_λ, W_λ=2θ'−2Re[−ζ'/ζ]_{≤λ²} (fórmula explícita). **[N] Establecido numéricamente (los tres niveles que pediste distinguir):**
- **Nivel (1) — convergencia espectral robusta [N fuerte]:** (1/ε₀)A_λ tiene autovalores (k+1)² (√=k+1 a k=6, paridad alterna máquina-limpio) y autovectores que colapsan a perfiles universales (edge-localized, anulación central). **ε₀ ~ C₀/λ²** (S=1, 3 puntos convergidos: 46.0, 46.7, ~47.3; C₀≈1.4e-19).
- **Nivel (2) — existencia/unicidad de 𝓛 [O]:** que exista un ÚNICO operador límite con esas propiedades NO está demostrado (sólo convergencia espectral numérica).
- **Nivel (3) — 𝓛 controla Eslabón 2 [O]:** que la convergencia espectral ⟹ ξ̂_λ→Ξ (vía Mosco + minimizador) NO está demostrado. **[O] Los dos teoremas abiertos que cierran Eslabón 2:**
- **A (forma/(k+1)²):** identificar 𝓛 y probar Spec(𝓛)=(k+1)² ⟹ (Mosco) convergencia.
- **B (escala):** ε₀~C₀/λ² (tasa = déficit de muestreo crítico; constante C₀ a derivar). ## 3. CARACTERIZACIÓN DE 𝓛 (lo establecido, sin presentar identificación como cerrada) **[N] Establecido:** 𝓛 = lim(1/ε₀)A_λ existe en sentido ESPECTRAL: universal (independiente de λ
en el límite), espectro (k+1)² (Weyl de 2º orden, √ε_k lineal en k), autovectores edge-localized
de paridad alterna con anulación central en u=1. Es la **segunda variación de la balanza
arquimediano↔primos** (arch(φ_k)=arith(φ_k) a 15 díg sobre cada autovector; ε_k es el residuo). **[O] NO establecido — identificación:** 8 vías refutadas con datos, TODAS de la misma manera:
| Vía | Resultado |
|---|---|
| ARCH aislado | √k-like, NO (k+1)² |
| ARITH aislado | √k-like, NO (k+1)² |
| símbolo/homogeneización | σ_prime satura, símbolo ≠ Weyl |
| Slepian (commuting diff.) | sin milagro tridiagonal (decay 1/d) |
| de Branges factorización | trivial (corrimiento espectral, vacuo) |
| de Branges–Bessel / SL local | no-local (85% hops grandes) |
| momentos M₀/M₂ | saturan, no homogeneizan |
| unfolding fase Riemann–Siegel (#8) | ARCH es √k-like, refutado | **Patrón clave (observación de):** ningún bloque aislado da (k+1)²; sólo
A_arch−A_arith lo da, tras cancelación de ~20 órdenes. ⟹ el fenómeno NO es "un operador
escondido" sino una **estructura de cancelación extremadamente rígida** — más cerca del espíritu
de la fórmula explícita de Weil / programa de que de Sturm–Liouville clásico. ## 4. PRÓXIMO PASO (vía #9, propuesta de): rigidez diferencial de la cancelación NO buscar otra identificación clásica. Medir el **Hessiano de la cancelación**: perturbar
pesos Λ(p)→Λ(p)(1+δ_p) y medir ∂²ε_k/∂δ_j∂δ_l. Si 𝓛 es la 2ª variación de la balanza de Weil,
su estructura debe emerger como ese Hessiano — un objeto nuevo, distinto de las 8 vías. **[N — COMPUTADO en mpmath dps=50, primer resultado POSITIVO Y ESTRUCTURAL del programa].**
Hessiano de 2º orden (repulsión de niveles, ∂²A/∂δ²=0 pues A lineal en δ):
H^(k)_jl = 2 Σ_{m≠k} ⟨φ_k,P_j φ_m⟩⟨φ_m,P_l φ_k⟩/(ε_k−ε_m), sobre {2,3,5,7}, modo k=0 seguido
por CONTINUACIÓN (overlap de autovectores, no min|ε|). PRECAUCIÓN (, correcta): en float64 los modos profundos tienen ε~1e-17 < piso de máquina
⟹ AUTOVECTOR contaminado; float64 daba rango_ef~2 y dirección errática {5,2,5} = ARTEFACTO.
En mpmath (ε resuelto a ~1e-21) el cuadro es limpio y OPUESTO: | λ | ε (mpmath) | rango_ef | dirección principal (2,3,5,7) | ∠ vs prev |
|---|---|---|---|---|
| 3.7 | 1.7e-20 | 1.00 | (−.72,−.70,−.03, 0) | — |
| 5 | 1.0e-20 | 1.02 | (−.64,−.69,−.35,−.05) | 19.3° |
| 7 | 6.2e-21 | 1.01 | (−.54,−.54,−.55,−.34) | 22.9° |
| 9 | 4.5e-21 | 1.01 | (−.49,−.50,−.53,−.47) | 8.6° |
| 11 | 3.9e-21 | 1.01 | (−.49,−.49,−.51,−.51) | 2.8° |
| 13 | 3.3e-21 | 1.01 | (−.49,−.49,−.50,−.52) | **0.5°** | DOS hechos robustos: (1) **rango-1 estable** (2º sv ~0.5% del 1º en todo λ); (2) la dirección
principal **CONVERGE al vector UNIFORME** (1,1,1,1)/2; ángulo entre λ sucesivos → 0 (8.6→2.8→0.5°,
monótono tras el transitorio de primos encendiéndose). Discriminante de: dirección que
converge ⟹ OBJETO GEOMÉTRICO REAL (no accidente rango-1, no mezcla numérica). ⟹ **𝓛 = Hessiano RANGO-1 de la cancelación de Weil.** La balanza arch↔arith es RÍGIDA contra
TODA perturbación de pesos de primos salvo UNA: el escaleo global Λ(n)→Λ(n)(1+δ) = densidad
global de primos = conjugada al POLO de ζ en s=1 (a PNT). Coherente con H1: el polo es el término
+1 de rango-1 (interlacing) — aquí reaparece como la única dirección curva del residuo; el resto
es núcleo exacto. Reduce el Eslabón 2 a controlar una curvatura RANGO-1 en la dirección del polo.
Estatus [N] robusto, NO [P]. Scripts: /tmp/via9.py, via9b.py (float, artefacto), via9mp(2).py (mpmath). PRÓXIMO: ¿el autovalor de curvatura (1er sv) escalado por ε₀ da (k+1)²? ¿la dirección-polo
controla la tasa ε₀~C₀/λ² y la convergencia (Eslabón 2)? Conecta geometría rígida con tasa. ## 5. VEREDICTO HONESTO
Eslabón 2 NO cerrado. Reducido a: identificar el **operador residual universal 𝓛** (existencia
espectral [N], espectro Weyl (k+1)², autovectores caracterizados) y probar que controla la
convergencia. El objeto está perfectamente caracterizado y falsado contra 8 identificaciones;
es una estructura de **cancelación rígida** (de Branges/Weil), no clásica. NO es prueba de RH;
es la localización final del núcleo, con todos los ingredientes derivados (c, M₀, M₂, horizonte,
ε₀~C₀/λ², 𝓛 universal), lista para la maquinaria de de Branges/cancelación fina.
