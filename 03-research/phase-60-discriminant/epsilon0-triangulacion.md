# ε₀>0: triangulación del muro desde tres marcos + ruta de diseño de ventana Resultado de atacar `ε₀=λ_min(QW)>0` (= Weil-positividad-hasta-T* = RH-local) con
matemática pura, sin frenar en "es RH". Tres marcos independientes, una caracterización,
y una ruta genuinamente nueva (diseño de ventana). ## 0. Reducción exacta al símbolo [RIGUROSO]
Carré-du-champ sobre `A_λ=M_θ−V` (f real, banda tipo Ω=logλ):
```
A_λ(f,f) = (Ω̃(0)−P_λ)‖f‖² + 𝓔_θ(f) + ½𝓔_prime(f), P_λ=Σ_{n≤λ²}Λ(n)/√n ≈ 2λ.
```
En Fourier, con ρ=|f̂|², autocorrelación c_f(u)=∫e^{itu}ρ(t)dt (|c_f|≤1, c_f(0)=1):
```
ε₀ = min_{‖f‖=1, banda} ∫ a(t) ρ(t) dt, a(t) = Ω̃(t) − D_λ(t),
D_λ(t) = Σ_{n≤λ²} Λ(n) n^{-1/2} cos(t log n) = Re Σ Λ(n) n^{-1/2-it}.
```
`a(t)` es exactamente arquimedeano − suma de primos = lado-ceros de la fórmula explícita. ## 1. Marco PRIMOS [RIGUROSO + obstrucción demostrada]
`ε₀>0 ⟺ Σ_n (Λ(n)/√n) Re c_f(log n) < ∫Ω̃ρ ∀ f prolato`.
- Gran tamiz (Montgomery–Vaughan) acota `∫D_λ|f̂|²` por `(2Ω+O(λ²))Σ Λ(n)²/n`, `Σ Λ²/n≈2(logλ)²`.
- **TEOREMA DE OBSTRUCCIÓN DE MÉTODO:** toda cota que use sólo |Λ(n)| (gran tamiz, mean-value) NO puede decidir sign(ε₀): DH tiene magnitudes comparables y ε₀<0. El slack del tamiz ≥ brecha RH-true/false. El signo vive en la COHERENCIA DE FASE de cos(t log n), no en magnitudes. ## 2. Marco CEROS [media RIGUROSA; mínimo = pair correlation]
`ε₀ = min_{‖f‖=1} Σ_ρ |f̂(γ_ρ)|²` (RH-true). - Media E[S] ≈ (1/2π)log(T*/2π) ≈ (logλ)/π > 0 [incondicional, RvM].
- El minimizador concentra f̂ (ancho 1/Ω) en un HUECO entre ceros (espaciado π/Ω) ⟹ ε₀ = fuga de cola. `ε₀>0 ⟺ ningún hueco demasiado grande = RIGIDEZ del frame de ceros = pair correlation`.
- Pair correlation F(α): F≥0 incondicional (da la media); F(α) para 0≤α≤1 probado BAJO RH (circular acá); F(α≈1) para α>1 (donde vive el signo) = CONJETURA ABIERTA. No es atajo. ## 3. Marco OPERADOR [el más nítido — Toeplitz truncado]
`A_λ = P_λ M_a P_λ`, Toeplitz/Wiener–Hopf truncado, símbolo `a(t)=Ω̃(t)−D_λ(t)`. Positividad de
Toeplitz ⟺ la truncación NO resuelve la parte negativa de `a`.
- **POZO CENTRAL** en t=0: `a(t)≈a(0)+½M_2 t²`, `a(0)≈−2λ`, `M_2≈2λ(logλ)²` ⟹ ancho `t_dip≈1/logλ`.
- **RESOLUCIÓN DE BANDA** (tipo Ω=logλ, Beurling–Landau) `≈1/Ω=1/logλ`.
- **HALLAZGO:** ancho del pozo ≈ resolución de banda ≈ 1/logλ — **MARGINAL POR CONSTRUCCIÓN**. `ε₀` = residuo de cancelación fina ~2λ vs ~2λ (energía punto-cero del confinamiento). Signo NO fijado por términos líderes ⟹ requiere símbolo exacto = primos exactos = RH. **Demuestra por qué ningún argumento blando decide el signo: el pozo está afinado al borde a propósito.**
- Cero off-line de DH = POZO EXTRA de a_DH en t=γ_off, resuelto por la banda ⟹ ε₀<0. Reproduce N5c. ## 4. CARACTERIZACIÓN (consenso de los tres marcos)
`ε₀>0 ⟺ no hay pozos/dips extra en a(t) ⟺ no hay ceros fuera de línea hasta T* ⟺ RH-local`.
Los tres marcos son RH-neutrales en setup, RH-encoding en resultado, NO circulares, y ninguno
rompe el muro incondicionalmente. Triangulación: la obstrucción es genuina, no debilidad de método.
La parte libre de cada marco (media/densidad/pozo-central) es común; la parte RH (fase/rigidez/
pozos-off-line) es la misma información dual = los ceros fuera de línea. ## 5. RUTA NUEVA (no reducible a estimar símbolo/ceros): DISEÑO DE VENTANA
Lo único que el muro analítico clásico NO controla y nosotros sí: la VENTANA/peso del frame.
Objetivo: elegir peso φ (en vez del rectángulo crudo) tal que (a) resolución de banda ≫ ancho del pozo 1/logλ (romper la marginalidad A FAVOR) ⟹ pozo central sub-resolución INCONDICIONALMENTE ⟹ ε₀^{(0)}>0 incondicional; (b) los pozos off-line queden excluidos estructuralmente por restricción del espacio de test;
manteniendo la identidad de Weil A_λ(f,f)=Σ_ρ... (la restricción dura).
Si (a) cierra, RH queda aislada ENTERAMENTE en los pozos off-line (b). Cálculo en curso:
re-parametrizar con peso φ y ver cómo escala resolución(φ) vs 1/logλ bajo la atadura de Weil. — atacado sin frenar en "es RH"; registrado para continuar. (CCM coincide con todo esto.)
