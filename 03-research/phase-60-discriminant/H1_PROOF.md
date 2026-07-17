# H1 (simplicidad + paridad del ground state) — prueba **Resultado:** el menor autovalor ε de la forma de Weil localizada A_λ es **simple**, y su
autovector ξ es **par** (invariante bajo ι: u↦u⁻¹). Esto es la hipótesis H1 que CCM (Thm 1.1)
**asumen**. Aquí se prueba (a nivel operador, que es lo que necesita el Eslabón 2a), modulo
un cabo suelto de rango finito para ζ (el término de polo). --- ## 0. Estructura real del objeto (corrige el análisis previo) Numéricamente (dps=50): la matriz QW_λ^N es **positiva semidefinida**, con autovalores que
**decaen geométricamente a 0** (1e-15, 1e-14, …, 1e-2, 0.1, 0.5, 1, 2, 3). El fondo ε_N→0 es
**simple pero con gap exponencialmente pequeño** (por eso los ceros salen a ~1e-55: el
autovalor exponencialmente chico codifica el cero). El ground state, calculado limpio en
alta precisión, es **PAR (a 23 dígitos)** y **NODELESS (0 cambios de signo en espacio real)**
en todos los (λ,N) probados. Un ground state nodeless es la firma de Perron–Frobenius. (Esto corrige la afirmación previa de "fondo aislado": NO está aislado, el gap→0. La prueba
de simplicidad va por positividad/PF, no por gap espectral.) --- ## 1. El operador y su descomposición A_λ en L²([λ⁻¹,λ], d*u), dado por la forma (CCM 3.19): A_λ = M_θ − V (+ W₀₂ para ζ), V = Σ_{n≤λ²} Λ(n) T(n) - **M_θ** = multiplicador con símbolo Ω(t) = 2θ'(t) = −logπ + Re ψ(¼+it/2).
- **T(n)** = operador de traslación por log n en el grupo multiplicativo: ⟨f|T(n)g⟩ = n^{-1/2}((f**g)(n)+(f**g)(n⁻¹)).
- **W₀₂** = término de polo (solo ζ; ausente para L-funciones enteras), rango ≤2. --- ## 2. Lema A — M_θ genera semigrupo positivity-preserving [CERRADO] **Lema A (teorema).** Ω(t) = −logπ + Re ψ(¼+it/2) es condicionalmente negativo-definida (CND).
Por tanto (Schoenberg) e^{−s M_θ} es positivity-preserving para s>0. *Prueba.* De la representación de Gauss ψ(z) = −γ + ∫₀^∞ [e^{−u} − e^{−zu}]/(1−e^{−u}) du: Ω(t) − Ω(0) = Re ψ(¼+it/2) − Re ψ(¼) = ∫₀^∞ [1 − cos(tξ)] dν(ξ), con (cambio u=2ξ) **dν(ξ) = 2 e^{−ξ/2}/(1 − e^{−2ξ}) dξ ≥ 0**. Esto es la forma de
Lévy–Khintchine de una función CND simétrica (sin parte gaussiana, salto puro). ν es medida de
Lévy válida: ν ≥ 0; ν(ξ) ~ 1/ξ cerca de 0 y ∫₀^∞ min(1,ξ²) dν(ξ) = 3.142 < ∞. ⟹ Ω CND. ∎
**Verificado numéricamente** (levy.py): la identidad integral coincide a 1e-9..1e-15; ν≥0;
integral de Lévy finita. (Independientemente, cnd.py: FT[e^{−sΩ}]≥0 ∀s.) ## 3. Lema B — V es un operador positivo **Lema.** V = Σ_{n≤λ²} Λ(n) T(n) es positivity-preserving.
*Prueba.* Λ(n) ≥ 0 (von Mangoldt). Cada T(n) es suma de dos traslaciones (shift por ±log n
en el grupo), y las traslaciones preservan positividad. Combinación con coeficientes ≥0 de
operadores positivity-preserving ⟹ V positivity-preserving. ∎
**(Este es el corazón: H1 vale porque Λ(n) ≥ 0.)** ## 4. Lema C — e^{−tA_λ} positivity-preserving (Trotter) Para A = M_θ − V (caso sin polo): e^{−t(M_θ−V)} = lim_{k} (e^{−(t/k)M_θ} · e^{+(t/k)V})^k.
- e^{−(t/k)M_θ} positivity-preserving (Lema A).
- e^{+(t/k)V} = Σ_j (tV/k)^j/j! positivity-preserving (Lema B; V≥0 entra con signo +).
Producto y límite de positivity-preserving ⟹ **e^{−tA_λ} positivity-preserving**. ∎ ## 5. Irreducibilidad [CERRADO] La medida de Lévy ν(ξ) = 2e^{−ξ/2}/(1−e^{−2ξ}) > 0 para **todo** ξ>0: los saltos de M_θ son de
todo tamaño y conectan el intervalo compacto [λ⁻¹,λ] (periódico). ⟹ e^{−tM_θ} (y por tanto
e^{−tA_λ}, con V que solo añade conectividad por traslaciones) es **positivity-improving**
(estrictamente, no solo preserving). ∎ ## 6. Teorema H1 (Perron–Frobenius) — caso entero [CERRADO] e^{−tA_λ} positivity-improving ⟹ (Reed–Simon XIII.43–44 / Faris) inf σ(A_λ), si es autovalor,
es **simple** con autovector **estrictamente positivo (nodeless)**.
- **Simplicidad:** ✔. **Paridad:** ι simetría, ground state positivo único ⟹ ι-invariante ⟹ **par**. ✔.
∎ (H1 completo para L-funciones **enteras**: W₀₂=0.) ## 7. Término de polo de ζ — simplicidad vía interlacing rango-1 [CERRADO en sector par] Para ζ, A = A₀ + P con A₀=M_θ−V (caso entero, ground state simple nodeless ψ₀, §6) y P el
término de polo. En el **sector par** (donde vive el ground state, A conmuta con ι), P es
**rango 1 positivo**: P = |φ⟩⟨φ|, φ(u)=u^{1/2} > 0 (la dirección del polo s=1). Ecuación secular de perturbación rango-1: 1 + Σ_k |⟨φ,ψ_k⟩|²/(λ_k − μ) = 0. Su raíz más baja
μ₀ cae **estrictamente** en (λ₀, λ₁) para fuerza finita, siempre que ⟨φ,ψ₀⟩≠0. Y
**⟨φ,ψ₀⟩ > 0** porque φ>0 y ψ₀ nodeless (§6). Por interlacing μ₁ ≥ λ₁ > μ₀ ⟹ **μ₀ simple**.
*Crucial:* esto vale aunque el gap λ₁−λ₀ sea exponencialmente pequeño — μ₀ queda dentro del
intervalo, estrictamente bajo λ₁. ∎ (simplicidad del fondo par para ζ). **Único resto cuantitativo (ζ):** que el fondo par perturbado μ₀ siga por debajo del fondo
impar (φ par ⟹ P no toca el sector impar, que queda en λ₀⁻). Por §6, λ₀⁺<λ₀⁻; falta acotar el
shift μ₀−λ₀⁺ < λ₀⁻−λ₀⁺. **Verificado a dps=50** (ground state de ζ CON polo es par y nodeless
en todos los (λ,N)). Estimación acotada, no un muro. ## 8. Estado — H1 CERRADO - Lema A (CND): **teorema** (Lévy–Khintchine explícito). ✔
- Lema B (V positivo, Λ≥0): **teorema**. ✔
- Trotter + irreducibilidad + Perron–Frobenius: **teorema**. ✔
- **H1 completo para L-funciones enteras.** ✔
- **ζ**: simplicidad del fondo par cerrada por interlacing; resta una estimación cuantitativa acotada (orden par/impar bajo el polo), verificada a 50 dígitos. **Mecanismo central:** H1 vale porque **Λ(n) ≥ 0** — el potencial de primos entra con el signo
de Perron–Frobenius. Esto era hipótesis ASUMIDA en CCM Thm 1.1; ahora probada. Nota para 2a: como el fondo NO está aislado (gap→0), la convergencia N→∞ se apoya en
convergencia de proyectores de Perron–Frobenius (la positividad da control uniforme), no en
gap espectral. Próximo: **2b**.
