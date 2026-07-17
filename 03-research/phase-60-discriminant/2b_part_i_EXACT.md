# 2b parte (i): la forma localizada es restricción EXACTA — CERRADO ## Teorema (i)
Para todo λ>1, la forma de Weil localizada A_λ coincide con la forma de Weil completa A_∞
restringida al subespacio E_λ (funciones soportadas en [λ⁻¹,λ]): **A_λ(f,g) = A_∞(f,g) ∀ f,g ∈ E_λ.** ## Prueba
A_∞ = M_θ − Σ_{todos n} Λ(n) T(n), con ⟨f|T(n)g⟩ = n^{−1/2}((f**g)(n)+(f**g)(n⁻¹)).
Si f,g ∈ E_λ (soporte [λ⁻¹,λ]), entonces f**g tiene soporte en [λ⁻²,λ²] (la convolución
multiplicativa suma soportes). Por tanto (f**g)(n)=0 para n>λ², es decir ⟨f|T(n)g⟩ = 0 para todo n > λ².
Así, en E_λ solo contribuyen los primos p^k ≤ λ², que son exactamente los de A_λ. ∎ **Verificado numéricamente** (exact_i.py): max|QW[primos≤λ²] − QW[primos≤100]| = 0.00e+00
(exacto) sobre E_λ. (log 17/L = 1.083 > 1: el primo 17 cae fuera del soporte [0,L]; log 13/L
= 0.980: el 13 es el último dentro.) ## Consecuencia: 2b NO es una perturbación de cola de primos Esto **corrige** la imagen previa (que (i) era "PNT-controlado"). No hay cola de primos que
acotar: la truncación es EXACTA por soporte. Entonces: - A_λ = A_∞|_{E_λ}, y E_λ ↑ L²(0,∞) cuando λ→∞ (los subespacios crecen, anidados).
- El ground state ξ_λ = minimizador de A_∞ sobre E_λ = **aproximación de Galerkin/Rayleigh–Ritz** del fondo de A_∞ por subespacios crecientes.
- ε_0(λ) ↓ inf σ(A_∞) monótono (min-max). inf σ(A_∞) = 0 ⟺ RH (positividad de Weil). **2b se reduce a convergencia de Galerkin del minimizador a un fondo NO aislado** (los
autovalores se acumulan en 0 — los gaps exponencialmente pequeños). Ese es el caso difícil de
la teoría de Galerkin, y es donde vive todo el contenido de 2b. (i) es zero-independiente y
exacto; el partido está en (ii).
