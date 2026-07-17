# #2: marco riguroso de la prueba (espectro de borde (k+1)²) — andamiaje + paso abierto **Honestidad:** este documento monta la prueba de #2 con rigor hasta donde es legítimo, e
identifica con precisión el ÚNICO paso analítico que queda abierto (= el "missing step" de). No se declara QED de ese paso. --- ## 1. Enunciado preciso a probar (#2) Sea A_λ la forma de Weil localizada en PW_{L/2} (L=2logλ), ε_0(λ)≤ε_1(λ)≤… sus autovalores.
**Teorema #2 (objetivo):** existe el límite de escala lim_{λ→∞} ε_k(λ)/ε_0(λ) = μ_k, con μ_k = (k+1)² (k=0,1,2,…),
y ε_0(λ) ≍ c·λ^{−2} (tunneling). Por #3 (reescalado), esto ⟹ ξ̂_λ→Ξ ⟹ RH. ## 2. Formulación de muestreo (de Branges) — el mecanismo Por la fórmula explícita (incondicional) + restricción exacta (i): A_λ(f,f) = Σ_ρ f̂(ρ) \overline{f̂(1−ρ̄)} (suma sobre ceros ρ de ζ),
donde f̂ ∈ PW_{L/2} (Paley–Wiener, tipo exponencial L/2, porque f vive en [−L/2,L/2]).
Sobre la recta crítica (parte on-line), los términos son |f̂(γ_j)|² ≥ 0. **Modos blandos = funciones band-limited pequeñas en los ceros.** ε_k = k-ésimo mínimo de la
forma sobre PW_{L/2}, ‖f‖=1. El minimizador f̂ se anula (o casi) en los ceros γ_1,…,γ_m hasta el
horizonte; ε_k = residual en los ceros no anulados. Esto es un **operador de concentración/muestreo** sobre PW_{L/2} con nodos en los ceros {γ_j}.
Su espectro bajo es lo que hay que identificar. ## 3. Por qué el espectro es (k+1)² — el modelo de capa límite (riguroso hasta el ansatz) Hecho numérico (softmodes.py): los minimizadores son **edge-localized** (concentrados en
w=±L/2) y se anulan en el centro. ⟹ el operador de concentración tiene su acción en una **capa
límite** de ancho fijo `a` (en w) junto a cada borde. **Lema-ansatz (capa límite):** en la capa límite, el band-limiting actúa como condición de
**Dirichlet** en el borde interior de la capa, y la forma A_λ se reduce a la energía de Dirichlet
∫|f'|² (segundo orden) en la coordenada de capa s∈[0,a]. Los modos son sin(jπs/a), j=1,2,…, con
energía (jπ/a)². ⟹ μ_k = ε_k/ε_0 = (jπ/a)²/(π/a)² = j² = (k+1)². □(ansatz) **Tunneling (escala ε_0):** dos capas límite (bordes u=λ, u=λ⁻¹) separadas por L=2logλ en w. El
splitting del modo fundamental ∝ solapamiento de colas ∝ e^{−κ·L}. Con κ=1: ε_0 ∝ e^{−L}=λ^{−2}.
**Verificado:** ε_0 ∝ λ^{−2.07}. □(verificado numéricamente; falta κ=1 analítico) ## 4. Lo que está RIGUROSO vs lo ABIERTO **Riguroso:**
- (i) restricción exacta A_λ=A_∞|_{E_λ}. ✔
- Fórmula de muestreo A_λ(f,f)=Σ_ρ f̂(ρ)\overline{f̂(1−ρ̄)} (Weil, incondicional). ✔
- #3: reescalado por ε_0 ⟹ fondo aislado ⟹ Galerkin ⟹ ξ̂_λ→Ξ (módulo existencia del límite). ✔
- H1/H2: el operador es positivity-improving ⟹ Gantmacher–Krein ⟹ k-ésimo modo k nodos (estructura Sturm/oscilatoria — consistente con espectro tipo j²). ✔ **ABIERTO (el missing step de, NO fabricado):**
- **Lema de capa límite riguroso:** probar que el operador de concentración sobre PW_{L/2} con nodos en {γ_j}, restringido al sector de borde, converge (reescalado) al Laplaciano de Dirichlet en [0,a] con espectro (jπ/a)². Requiere: (a) identificar el ancho `a` desde la densidad de ceros / el símbolo arquimediano; (b) controlar el band-limiting como condición de Dirichlet efectiva; (c) la asintótica de tunneling κ=1.
- Esto es análisis asintótico real (de Branges / prolate / capa límite). Es un enunciado bien-puesto y zero-independiente, NO un muro — pero NO está probado aquí. ## 5. Veredicto honesto #2 = límite de escala de borde (k+1)² + tunneling λ^{−2}. Marco riguroso montado; mecanismo
identificado (Dirichlet en la capa límite + tunneling entre bordes); 3 piezas verificadas
numéricamente; conexión con H1 (Sturm). **El lema de capa límite es el único paso abierto** y es
genuinamente el "missing step". No se declara probado. Trabajar matemática pura = no fingir ese
QED. El camino está montado para atacarlo con de Branges/prolate (herramientas que el programa ya
tiene: P7/P8).
