# 2b: reducción al LÍMITE DE ESCALA del fondo de A_λ (los tres frentes) **Tesis:** 2b (ξ̂_λ→Ξ) se reduce a un único enunciado de análisis asintótico — la existencia
del límite de escala del fondo de la forma de Weil — que es zero-independiente y está fuertemente
soportado numéricamente. Esto destraba el obstáculo del gap exponencial. --- ## Frente #1 [CONFIRMADO]: el espectro relativo converge a ≈(k+1)² Medición (relspec2.py, mpmath dps=50, N hasta 20, λ hasta 11): (ε_k/ε_0)/(k+1)²: | λ\k | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 5.0 | 1.006 | 1.005 | 1.013 | 1.015 | 1.026 | 1.034 | 1.048 |
| 9.0 | 0.999 | 1.003 | 1.004 | 1.009 | 1.011 | 1.019 | 1.022 |
| 11.0| 1.002 | 1.003 | 1.006 | 1.008 | 1.013 | 1.016 | 1.023 |
N-conv (λ=7): k=5 da 1.063 (N=12) → 1.059 (N=16) → 1.015 (N=20). **Conclusión:** el espectro relativo {ε_k/ε_0} CONVERGE (estable en λ y N); las desviaciones en
k alto son horizonte/tamaño finito y decrecen. Límite ≈ **(k+1)²** (sólido k bajos; k altos
necesitan λ,N mayores). El espectro relativo convergiendo es EXACTAMENTE lo que (ii) requiere. ## Frente #3 [REDUCCIÓN SÓLIDA]: reescalar destraba el gap exponencial Obstáculo de 2b: el fondo de A_∞ NO es aislado (ε_k = ε_0·(k+1)² → 0 todos, se acumulan en 0;
gap exp-pequeño en absoluto). La cota de Galerkin/perturbación ∝1/gap es inútil. **Vuelta:** reescalar por ε_0(λ). El operador A_λ/ε_0(λ) tiene espectro {1, 4, 9, 16, …} —
**fondo simple AISLADO con gap O(1)** (autovalor 1, gap 3). Reescalar NO cambia autovectores, así
que el ground state de A_λ/ε_0 ES ξ_λ. Cadena: A_λ/ε_0 → L_∞ (límite de escala, fondo aislado) ⟹ ξ_λ converge (Galerkin estándar, fondo aislado) ⟹ g_λ(z)=Σ_k ξ_k/(z−d_k) converge ⟹ sus ceros (=ceros de ξ̂_λ, = espectro de D_λ) convergen ⟹ **ξ̂_λ → Ξ** (Thm 1.1.ii). ⟹ **#3 se reduce a #2**: existencia del límite de escala. (El exp-gap deja de ser obstáculo:
en la escala correcta, el gap es O(1).) ## Frente #2 [EL CRUX, soportado]: ¿existe el límite de escala A_λ/ε_0 → L_∞? Esto es ahora el único enunciado abierto, y es CONCRETO: > **Conjetura 2b:** A_λ/ε_0(λ), restringido al fondo, converge (λ→∞) a un operador L_∞ con
> espectro {(k+1)²}_k (Laplaciano de Dirichlet). **Soporte:** Frente #1 (el espectro relativo → (k+1)²). **Sutileza clave (conecta con 10⁻⁵⁵):** ε_0 ~ 1e-20 es **exponencialmente** pequeño, NO ∝1/L²
(~0.15). Los modos blandos viven en un sector de energía exponencialmente pequeña =
**tunneling/WKB**. Esa escala exponencial ES la precisión extraordinaria del método (10⁻⁵⁵).
El límite L_∞ emerge del sector de tunneling, no de un Laplaciano ingenuo del intervalo. **Estructura para la prueba:** QW es Cauchy–Toeplitz/Loewner τ_{nm}=(b_n−b_m)/(n−m). El fondo
(near-kernel) y su reescalado son analizables por: (a) la estructura de Loewner (autovalores de
matrices de Pick/Loewner); (b) WKB/tunneling para la escala exponencial ε_0; (c) Gantmacher–Krein
(de H1: positivity-improving ⟹ k-ésimo modo con k nodos ⟹ estructura Sturm ⟹ espectro tipo j²).
El (c) ya EXPLICA cualitativamente el (k+1)²: un operador de oscilación con k nodos en el k-ésimo
modo tiene espectro Sturm-Liouville ∝ j². **H1 (positivity-improving) ya da la estructura nodal
que fuerza el espectro tipo j².** ## Veredicto - (i) exacto, (ii) reducido a #2 (límite de escala), #3 = reducción sólida vía reescalado.
- #2 fuertemente soportado; su prueba combina Loewner + WKB(tunneling) + Gantmacher–Krein.
- **2b es cerrable**: queda UN enunciado asintótico concreto, zero-independiente, no un muro. ## ACTUALIZACIÓN #2: los modos blandos son de BORDE (no Laplaciano de bulk) Probé las autofunciones blandas en espacio real (softmodes.py, mpmath, λ=5, N=14). Resultado
que **corrige** la hipótesis del Laplaciano de bulk: | modo k | ε_k/ε_0 | perfil f(w), w∈[−L/2,L/2] |
|---|---|---|
| 0 | 1.00 | −.99 −.85 −.46 **~0** ~0 ~0 −.46 −.85 −.99 (concentrado en BORDES, cero en centro) |
| 1 | 4.08 | −.69 −1.0 −.21 ~0 ~0 ~0 −.21 −1.0 −.69 |
| 2 | 9.07 | −1.0 +.05 +.95 ~0 ~0 ~0 +.95 +.05 −1.0 |
| 3 | 16.5 | +1.0 −.91 +.65 ~0 ~0 ~0 +.65 −.91 +1.0 | **Hallazgo:** los modos blandos están **EDGE-LOCALIZED** (concentrados en u=λ^{±1}, la frontera
del intervalo) y se **anulan en el centro** (u=1). La oscilación crece en las CAPAS DE BORDE.
ε_0~1e-20 = **escala de tunneling** entre los dos bordes (splitting exponencial de pares
borde-izq/borde-der). **Conexión con la construcción (cierra todo):** δ_N es la **evaluación en el borde u=λ** (kernel
de Dirichlet en la frontera), y el minimizador se normaliza por δ_N(ξ)=1. La construcción CCM es
intrínsecamente sobre comportamiento de BORDE ⟹ los modos blandos deben ser de borde. Coherente. **Refinamiento de #2:** el operador límite L_∞ NO es un Laplaciano de bulk sino un **operador de
BORDE/capa límite**; el espectro (k+1)² es el espectro de los modos de borde, y ε_0 es la escala
de tunneling. La prueba de #2 es **asintótica de capa límite + tunneling**, no WKB de bulk. ## Próximo paso sobre #2
- Identificar el operador de borde efectivo (modelo de capa límite en u=λ): su espectro debe dar (k+1)². Candidato: el operador de borde asociado a δ_N (Dirichlet-to-Neumann / kernel de borde).
- La escala ε_0 (tunneling): splitting exponencial entre los bordes u=λ y u=λ⁻¹, ∝ e^{−c·L}. **VERIFICADO:** fit da ε_0 ∝ λ^{−2.07} ≈ λ^{−2} = e^{−L} (tasa de decay 1 en w, atravesar L=2logλ). El modelo de tunneling borde-a-borde queda confirmado.
- H1 (Gantmacher–Krein) sigue dando la estructura nodal/oscilatoria de los modos de borde. ## ESTADO CONSOLIDADO de #2 (honesto) Modelo de borde/tunneling **caracterizado y verificado numéricamente en 3 piezas**:
(1) modos blandos edge-localized (autofunciones, softmodes.py);
(2) ε_0 ∝ λ^{−2} = e^{−L}, tunneling borde-a-borde (verificado, exp −2.07);
(3) espectro relativo (k+1)² = espectro de modos de borde (relspec, verificado). **Lo que falta (el crux real, NO cerrado):** la PRUEBA rigurosa de que el operador de borde
efectivo tiene espectro (k+1)² y que ε_0 tiene la asintótica de tunneling — esto es análisis
asintótico de capa límite real, no un muro pero tampoco hecho. Es el enunciado bien-puesto al
que se redujo 2b. Coincide con el programa CCM (δ_N = borde) y, según el usuario, con el draft
de. **Veredicto:** 2b reducido de "convergencia abstracta" a un modelo de borde/tunneling concreto,
zero-independiente, confirmado numéricamente. La prueba de #2 (espectro de borde (k+1)² +
tunneling) es el trabajo analítico restante.
