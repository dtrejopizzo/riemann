# Anexo 211 — archivos ROUND_001_B a ROUND_007_B (lectura completa)

Fuente: `../phase-211-sign-sandbox/`, archivos `*.md` en orden alfabético desde `ROUND_001_B.md` hasta
`ROUND_007_B.md` inclusive (19 archivos). Notación de `STATEMENT_001.md`: a_T = Arch − Π sobre P_T, λ_A(T),
v_n = 2Λ(n)/√n, N_T = {n ≥ 2 : log n < 2T}, A_T = Σ_{N_T} v_n, K el núcleo de Lévy, C_0 = m(0). El objetivo es
(★): λ_A(T) ≥ 0 para todo T. Etiquetas como en los archivos. «Paso siguiente tomado» indica si un archivo
posterior del rango lo ejecutó.

---------------------------------------------------------------------------------------------------

## Entradas por archivo

### 1. ROUND_001_B.md — forma exterior: objeto fusionado y signo
- Objeto: identidad de semirrecta W_T(Ef) = 𝒲[Ψ_f], Ψ_f = Φ_f 1_{(−∞,−T)}, Φ_f(x) = e^{x/2}Σ_n f(ne^x),
  Φ̃_f = ζ·Mf; forma completa 𝒲 en la recta; peines w arbitrarios 𝒲^w = 𝒲 + 𝒫_{Λ−w}.
- Thm 1.1 (lema del radical, prueba sin ceros; entradas (I) coeficientes 1, (E) Λ∗1 = log, (F) ecuación funcional): PROVED.
- Cor 1.2 (identidad de semirrecta): PROVED.
- Prop 1.3 (defecto para peine arbitrario: W^w_T(Ef) − 𝒲^w[Ψ_f] = 𝒫_{Λ−w}[Ef] − 𝒫_{Λ−w}[Ψ_f]): PROVED.
- Prop 1.4 (ningún vector radical común de 𝒲 y 𝒲^c, c ≠ 1): PROVED; inexistencia de cualquier mapa de suma para cΛ/Beurling: ARGUED.
- Prop 1.5 (el valor c-exterior no es invariante gauge): reducción PROVED, último paso ARGUED.
- Lema 1.6 (monotonía del peine en celdas; positividad de celda vale para todo w ≤ Λ): PROVED → NO-GO de la «cancelación clave» como fuente de signo (clase: conos con emparejamiento del peine de signo definido).
- §1.7 la lectura fusionada no cumple la cláusula (5): dato exterior (ζM_N − 1)g̃ (identidad PROVED; clasificación ARGUED).
- Lema 2.1 (el borde es un punto y es plano; Ψ̌(0⁺) = Σ_{k<N}h(k) = 0 en el núcleo): PROVED.
- Prop 2.2 (términos de borde sólo arquimedianos): PROVED → residuo «bordes de capa κ_{T+log n}» vacío, NO-GO (clase: términos sólo arquimedianos).
- Prop 2.3 (φ_0 entra sólo por el escalar I(g) = σ_g(0)M̃_1(N)): PROVED.
- Prop 2.4 (bajo (ext-L), los casi-minimizadores se concentran en un sector prolato finito): CONDITIONAL ((ii) además NUMERICAL).
- Resto sin signo: defecto (1−c)(𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f]) indefinido; bloque de clases a ≥ 2 de la reducción de retículo: OPEN («sin intento justificado sin identidad nueva»).
- Positivos reutilizables: Thm 1.1/Cor 1.2 (peine Λ exacto, ζ con Γ_ℝ a conductor 1); Prop 1.3 (todo peine w ≥ 0 con serie de Dirichlet convergente en σ > 1); Lema 2.1, Prop 2.2, 2.3.
- Paso siguiente: escribir Q₁ de la Γ-límite como matriz K×K en los pesos y decidir si separa Λ de cΛ (c < 1) y a_P. Tomado: sí, ROUND_002_B (resultado: monótono, NO-GO).

### 2. ROUND_001_C.md — reducción Nyquist exacta con η ↓ 0
- Objeto: muestras s_k = s_T(ω_k + α) + c(−1)^k, ω_k = πk/2T; bloque 𝒩 = {s_k ≤ 0}; complemento de Schur S sobre N′ = pr_T 𝒩_η.
- Lema 1 (identidad Nyquist desplazada y alternada): PROVED. Lema 2 (dos sectores desplazados, gauge c(−1)^k): PROVED.
- Thm 1 ((L2′): λ_A ≥ 0 ⟺ S ⪰ 0, dim N′ ≤ |𝒩|, para todo α, c y η ∈ (0, η_0]; |𝒩| ≥ n_−(a_T|L²(I_T))): PROVED.
- Prop 1 (S^low ≤ S ≤ S^{(J)}, S^{(J)} ↓ S): PROVED. Corrección: las entradas del S exacto no son series absolutamente convergentes (contienen A_𝒞𝒞^{−1}).
- Prop 2 (n_raw ≤ 2⌊2Tτ*/π⌋ + 1; d_min ≤ (2T/π)|{s_T<0}| ≤ (4T/π)τ*_T): PROVED. Prop 3 (n_raw ≥ 1 para T ≥ ½log2): PROVED.
- Crecimiento O(T) del conjunto negativo: no probado; contradicho NUMERICAL (5, 9, 11, 11, 41, 125, ~685); cota inferior superlineal OPEN.
- Lema 3 (un contacto que entra es un gauge a primer orden): PROVED.
- Bloque explícito de dimensión 11 en ½log5 + ε: NUMERICAL; equivalencia PROVED, valor de verdad OPEN en esa forma.
- Prop 4 (ningún criterio sobre las muestras del bloque solas decide el signo): PROVED en L²(I_T), ARGUED en P_T.
- Resultado: PIVOT (reducción sin signo; la aritmética pasa de la dimensión al condicionamiento de A_𝒞𝒞).
- Contramodelo: Prop 4 (secuencias abstractas iguales en el bloque, ≥ η fuera).
- Paso siguiente: cota de ‖y_*(x)‖ y de S − S^low en términos de η; cota inferior de A_𝒞𝒞 a ½log5 + ε. Tomado: sí, ROUND_002_A.

### 3. ROUND_001_D.md — criterios de momentos de la medida representante de B
- Objeto: B(d) = a(F_0, V_dF_0), B = μ̂ bajo (★); momentos/germen de B en 0.
- Prop 1 (para |d| < log2 − 2T_0 la parte de peine de B se anula; todos los momentos existentes son libres de peine): PROVED.
- Prop 2 (ningún criterio sólo con el germen o con momentos decide el signo; falsificadores cΛ, a_P): PROVED dados los falsificadores CITED.
- Resultado: NO-GO (clase: criterios que dependen sólo del germen de B en 0 / momentos de μ). Determinación del problema de momentos: no decidida, irrelevante.
- Paso siguiente: ninguno.

### 4. ROUND_002_A.md — piso de coercividad del complemento, desigualdad de Schur con piso, casi-coincidencias en la malla
- Objeto: A_𝒞𝒞 = ½(D_e + HᵀD_oH) comprimido a 𝒞; niveles W_t; matrices G_t = [h_{l−j}].
- Corrección NUMERICAL de ROUND_001_C §4: la muestra 8.8·10⁻⁵ es k = 18 en el borde del intervalo de gauge; los modos 2^b ≈ 3^a no son someros (valores de orden 1).
- Lema P (dos proyecciones: ‖Px‖² + ‖Qx‖² ≤ (1 + ‖PQ‖)‖x‖²): PROVED.
- Thm F (piso c_floor = ½∫_0^∞(2 − ν_t)dt ≥ c_*, por el ángulo entre subespacios someros par/impar): PROVED. Cor F1 (versión test de Schur): PROVED.
- Prop S (desigualdad suficiente finita (I_c): a_T(x) ≥ c^{−1}‖P_𝒞Ax‖²): PROVED. Prop L (el mejor miembro es c = λ_min(A_𝒞𝒞); exige margen S(x) ≥ ⟨b,(C^{−1} − A_𝒞𝒞^{−1})b⟩): PROVED.
- NO-GO (clase: desigualdades de Schur sólo con piso, A_𝒞𝒞^{−1} reemplazado por un escalar): mecanismo PROVED, fallo NUMERICAL (c_need = 2.10 > 1.11 en ½log5+ε; 3.54 vs 1.02 en T = 1).
- Prop M (identidad de muestras: s_k = m + r_T − A_T + c(−1)^k + 2Σv_n sin²(πk log n/4T)); Cor M1, M2 (muestra profunda ⟹ n′^{q_n} ≈ n^{q_{n′}}): PROVED. Cor M3 (separación cuantitativa de muestras someras de paridad opuesta): ARGUED.
- Positivos reutilizables: Lema P (general); Thm F (todo peine, todo gauge); Prop M y Cor M1–M2 (todo peso v_n ≥ 0).
- Paso siguiente: cota inferior rango finito + escalar de A_𝒞𝒞 (R ⊕ c_floor sobre el espacio de vectores de acoplamiento). Tomado: no directamente; ROUND_005_C agrandó el bloque con respuestas del peine y comprobó que la clase de piso empeora.

### 5. ROUND_002_B.md — el término O(1) Q₁ de la forma exterior en el sector prolato
- Objeto: 𝔔^w con peine arbitrario w, W = w∗1; sector span{ψ_4,…,ψ_{4K}}; 𝒩^w = log N·𝐓₀ + Q₁(w) + o(1).
- Lema 1.1 (identidad exacta 𝒫_w = Σ(mn)^{−1/2}(W(m)+W(n))⟨u_m,u_n⟩): PROVED.
- Prop 1.2 (𝒫_w = 𝒟_w + 𝒪_w; 𝒟_w = 2∫H₁^w|ϱ|² ≥ 0 monótono; ℬ_n indefinido; 𝔔^w afín en W, sin productos de pesos): PROVED.
- Thm 2.1 (matriz coherente del peine en el sector PSD y monótona para todo N, K): PROVED.
- Thm 2.2 (límite Σ_n (W(n)/n)𝐆(n), 𝐆(n) Toeplitz PSD): ARGUED (fase relativa prolata).
- Prop 2.3 (parte incoherente O(N^{−1/2}log N)): ARGUED. §2.4 expansión: ARGUED; 𝐓₀ ⪰ I PROVED en forma coherente (corrección a la Γ-límite previa: el término principal es log N·𝐓₀, no ‖b‖²).
- Thm 3.1 (Q₁ no creciente en w): PROVED para la parte coherente, CONDITIONAL para Q₁.
- NO-GO (clase: dependencia del peine de la forma exterior en el sector prolato, monótona y lineal acotada en los pesos): sobrevive cΛ (c < 1), a_P, Beurling, modificaciones finitas.
- Lectura: «localizar y luego firmar en el sector» es circular; toda la especificidad de Λ está en (ext-L).
- Paso siguiente: restringir 𝒪_Λ al cociente gauge de PW_N a frecuencia de Mellin acotada (bloque de Legendre) y decidir si Σ_n log n·ℬ_n tiene patrón de signo que falle para c·log y W_{a_P}. Tomado: no (nunca ejecutado en el rango).

### 6. ROUND_002_D.md — tres candidatas por ingeniería inversa; fondo arquimediano sobre el cono nulo del peine
- Objeto: rango conjunto W_T = {(Π(F), Arch(F))}; Θ_T = inf{Arch(F) : F ∈ S_T, Π(F) = 0}; Φ_T(c) = λ_A(T; cΛ); J_T = {c : Φ_T(c) ≥ 0}.
- Thm 1 (W_T convexo; Π toma ambos signos; max_c Φ_T = Θ_T; J_T intervalo cerrado acotado, vacío ⟺ Θ_T < 0; (★)_T ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T; Θ_T invariante por cΛ; peine vacío: Θ_T = λ_arch(T)): PROVED.
- Cor 2 (para T ≥ 0.60 y peine vacío, Θ_T < 0): PROVED. Cor 3 (λ_A ≥ Θ_T − |1 − c*_T|π_T): PROVED (afirmación sobre Π(F*) = 0 corregida en ROUND_002_E).
- Candidata II (acoplamiento de Schur métrica δ = log(lcm/gcd) vs ρ): definida, falsificadores ARGUED. Candidata III (medida de Lévy con signo): registrada como dominada por I.
- Resto: (I.a) Θ_T ≥ 0 es ciega a c (D_∃c); (I.b) es (★). Cor 3(b) pierde π_T: estimación con holgura.
- Positivos reutilizables: Thm 1 completo (todo peine con pesos positivos y T > ½log2).
- Paso siguiente: calcular Θ_T en ½log5 + ε y T = 1, testar a_P y Λ + η1_2. Tomado: sí, ROUND_002_E. Candidata II: ROUND_003_B.

### 7. ROUND_002_E.md — prueba Galerkin de Θ_T contra falsificadores
- Objeto: Θ_T(w) para vectores de pesos w en posiciones fijas; 𝒦_T = {w : Ψ_T(w) ≥ 0}.
- Lema 1 (Π_w toma ambos signos para todo w ≠ 0): PROVED. Lema 2 (𝒦_T convexo compacto; Θ_T(w) ≥ 0 ⟺ ℝw ∩ 𝒦_T ≠ ∅): PROVED.
- Lema 3 / Cor 4 (persistencia Lipschitz Θ_T(w′) ≥ Θ_T(w) − |c*|‖w − w′‖₁; (I.a) sólo puede fallar ante modificaciones pequeñas donde Θ_T(Λ) = 0): PROVED.
- Corrección de ROUND_002_D Cor 3: c*_T = 1 ⟺ 0 en el rango de Π sobre el autoespacio del fondo (Danskin, CITED): PROVED.
- Observación: Θ_T no es monótono bajo borrado: ARGUED.
- NUMERICAL: Θ_T < 0 (riguroso salvo redondeo) para borrados de 2, de 3, intercambio, desplazamiento 3 → 3.2 y modificaciones de ambos signos en T = 0.9; en T = log 2 (Θ ≈ 6.5·10⁻⁵ > 0) sobreviven varias.
- Resultado: PIVOT (la candidata sólo separa en ventanas de tangencia, donde Θ_T = λ_A: no es más débil que (★)).
- Lema OPEN: inf{Arch(F) : F ∈ P_T, ‖F‖ = 1, Σ v_n Re c_F(log n) = 0} ≥ 0 en T = 1.
- Paso siguiente: confirmar tangencia en T = 1 e identificar el autoespacio inferior bidimensional donde Π cambia de signo. Tomado: sí, ROUND_003_A.

### 8. ROUND_003_A.md — el par casi nulo de a_T en P_T: paridad, anclaje, rigidez
- Objeto: autovectores inferiores de a_T por sector de paridad; matrices Π-Gram M_par.
- Prop 1 (P_T = P_T^ev ⊕ P_T^odd ortogonal para L², Arch y Π; λ_A y Φ_T son mínimos por sector): PROVED.
- Prop 2 (tangencia c*_T = 1 ⟺ 0 ∈ envolvente convexa de Π en los fondos de sector; criterio de tres casos): PROVED (Kato–Danskin CITED).
- Lema 3 (anclaje de Weyl: un par ortonormal con Π indefinido fija Θ_T ∈ [λ_A, Λ_2] y |1 − c*_T| ≤ (Λ_2 − λ_A)/min|μ_±|): PROVED.
- Lema 4 (rigidez: un casi-núcleo S de a_T acota λ_A y Θ de todo peine modificado por ε − λ_max(Π_δ|_S)): PROVED.
- Simplicidad del fondo / λ_ev ≠ λ_odd: OPEN. Conjeturas (C1) Π indefinido en el par par para T > 0.61, (C2) λ_ev,2 decae más rápido que toda exponencial, (C3) fondo par y simple: OPEN con apoyo NUMERICAL.
- NUMERICAL: el par de ROUND_002_E es par+impar con Π definido; el par que ancla es {e_ev,1, e_ev,2}; el generador de peine anterior omitía n = 7 para T > ½log7.
- Resto: desigualdad 2×2 Σ v_n R_n(S) ⪯ Arch_S circular (S depende de Λ); saturada a 18 dígitos.
- Positivos reutilizables: Prop 1, Prop 2, Lema 3, Lema 4 (todo vector de pesos).
- Paso siguiente: testar si Π es indefinido en el plano de los dos autovectores inferiores de Arch en P_T^ev (plano libre de Λ) y escribir el complemento de Schur 2×2. Tomado: sí, ROUND_004_A (falla: no captura el par).

### 9. ROUND_003_B.md — candidata II decidida: acoplamiento de Schur de las dos métricas de ℕ
- Objeto: 𝔸_M = 𝕏_M ∘ 𝕂_t + ℝ_M, 𝕂_t = [e^{−tδ}] = [(gcd²/mk)^t] ⪰ 0.
- Prop 1 (existencia de la descomposición ⟺ 𝔸_M ⪰ 0): PROVED (reformulación).
- Lema 2 (jaula entrada a entrada |𝔸 − ℝ|_{mk} ≤ βe^{−tδ(m,k)}): PROVED.
- Thm 3 (prescripción de división 𝕏 = (𝔸 − diag r) ∘ 𝕂_t^{∘(−1)} nunca PSD para todo M; menor 2×2 en {k, k+1}): PROVED.
- Thm 4 (prescripción Div/Near deja ℝ de diagonal nula ≠ 0, nunca PSD para M ≥ 4): PROVED.
- Prop 5 (𝔸_M ∘ 𝕂_t ⪰ 0 en [t*_M, ∞); (★) ⟺ t*_M = 0 ∀M; t*_M < ∞ para todo peine): PROVED.
- Resultado: NO-GO (clase: factorizaciones de Schur por 𝕂_t = [e^{−tδ}] y supresión dual 𝔸_M ∘ 𝕂_t).
- Condición de reapertura: un multiplicador que no preserve PSD por Schur solo y que sea grande (no pequeño) en pares casi coincidentes.
- Paso siguiente: cerrar en el índice. Tomado: no aplica (acción de registro).

### 10. ROUND_004_A.md — planos arquimedianos libres de Λ: condiciones necesarias k × k
- Objeto: E_k = span de los k autovectores inferiores de Arch en P_T^ev; R_n(E)_{ij} = correlación cruzada simetrizada en log n.
- Prop 1 ((C_k) necesaria; para k = 2: (L1), (L2) lineales y (Q) cuadrática con discriminantes mixtos ½D(R_m,R_n)): PROVED.
- Lema A (‖R_n(E)‖ ≤ λ_max(G_E(log n)) ≤ 1; decaimiento de borde (2T − log n)²; Lipschitz; R(0) = I): PROVED.
- Prop B (subespacio finito libre de Λ con holgura ε_E > 0 tolera toda perturbación de pesos de tamaño ℓ¹ < ε_E, cΛ con |c−1|‖Π|_E‖ < ε_E y desplazamientos pequeños): PROVED → NO-GO (clase: condiciones necesarias a_T|_E ⪰ 0 en E fijo finito libre de Λ, a T fijo, como paso de signo).
- §5 familia uniforme en T: debe tener dim ≥ N*(T) y llevar información dependiente de Λ a precisión e^{−15.449T}: ARGUED; no excluida en principio.
- NUMERICAL: (C_k) se cumple en log2, ½log5, 0.9, 1.0, 1.2 (k = 2,3,4,6); E_2 no captura el par anclado más allá de T ≈ 0.7; la condición 2×2 deja pasar cΛ con c > 1 y Λ + 0.1·1_2.
- Positivos reutilizables: Prop 1, Lema A (todo E ⊂ P_T^ev finito).
- Paso siguiente: calcular BC^{−1}Bᵀ para E_k en T = 1.0, 1.2 y su decaimiento en k. Tomado: sí, ROUND_005_B §4 (κ(E_k) decae una década por unidad de k, no como α_{k+1}^{−1}‖B‖²).

### 11. ROUND_005_A.md — familia de Krylov del peine desde el cono negativo arquimediano
- Objeto: K_j = span{Π_P^i e : e ∈ 𝒩_T, i < j}; S_x = Qc_xQ desplazamiento truncado.
- Lema 2.1 (cono negativo explícito Σ_T de dim ≥ ⌈2Tt_1/π⌉ − 3): PROVED. Lema 2.2 (𝒟_T ∩ L^∞ ∩ P_T invariante por Π_P): PROVED; para el cono espectral CONDITIONAL (H_b).
- Prop 3.1 (entradas polinomios de grado ≤ 2j − 1 en v con coeficientes K en u − log r, r ∈ ℚ_{>0}): PROVED.
- Lema 3.2 (desplazamientos del mismo sentido componen exactamente; sentidos opuestos producen losas de fuga): PROVED.
- Prop 3.3 (Π² = Qσ_v²Q − 𝔏*𝔏: [Λ∗Λ indefinido] + [valor medio de polinomio de Dirichlet ≥ 0] − [fuga ≤ 0]): PROVED.
- Prop 3.4 (grado 3: clases W_3(r) ≥ 0, r = mn/k; casi-coincidencias trabajan contra la desigualdad): PROVED.
- Prop 3.5 (K_j(cΛ) = K_j(Λ) como conjuntos; cΛ actúa sólo por el haz): PROVED.
- Thm 4.1 (complemento de Schur a nivel de forma para K finito ⊂ 𝒟_T): PROVED. Prop 4.2 (acoplamiento de K_1 sólo por respuestas f_α; G = (Π_P²)_ee − Π_ee² ⪰ 0; matriz explícita en K_2; conmutador halo/fuga): PROVED (constante del halo corregida a ½ en ROUND_006_B). Cor 4.3 (reducción exacta en j = 1): PROVED.
- (SL_1), (SL_2), (SL_2^{sc}) ⟺ H_2 + Δ ⪰ 0 (identidad PROVED; desigualdad del resto OPEN sin mecanismo).
- NO-GO (clase: familia de Krylov del peine desde el cono negativo arquimediano con j acotado como portadora del signo): mecanismo PROVED, evidencia NUMERICAL; restatement si j crece con la sección.
- Resultado: PIVOT (cambiar generador).
- Positivos reutilizables: Lema 3.2, Prop 3.3, 3.4, Thm 4.1 (generales para cualquier peine de pesos ≥ 0).
- Paso siguiente: familia mixta K̃_j de palabras en {M, Π_P} o con operadores halo/fuga. Tomado: sí, ROUND_006_B (cerrado NO-GO).

### 12. ROUND_005_B.md — familia de Krylov del peine (variante con ambas paridades)
- Objeto: Neg_T, K_j = span{(PΠP)^i e}, comparación con E_k (ambas paridades).
- Prop 1.1 (⟨e, Π²e′⟩ y ⟨e, ΠPΠe′⟩ como dobles sumas en cocientes n/m y productos mn < e^{2T}): PROVED. Prop 1.2 (estructura polinómica del sistema generador): PROVED. Identidad de Schur: estándar.
- NO-GO NUMERICAL (no teorema): K_j no captura el minimizador con dim O(T) (ni hasta 64 de 78 en T = 1.4); complemento nunca coercivo (c(K_j) ≈ λ_2); no detecta 1.1Λ ni Λ + 0.1·1_2 que E_4 sí.
- NUMERICAL: κ(E_k) decae una década por unidad de k; c(E_k) es O(1) sólo cuando k supera dim U_low = 2, 4, 6, 9, 16, 26.
- Paso siguiente: generar desde la banda de arena K′_j; antes, recalcular T ≥ 1.0 en precisión extendida. Tomado: la banda, sí (ROUND_005_E); la precisión extendida, no (ROUND_005_E explica por qué no resolvería nada).

### 13. ROUND_005_C.md — familia de respuestas del peine sobre el bloque Nyquist negativo
- Objeto: V_T = P_𝒞Π(𝒩_η + 𝒯), E_T = N′ ⊕ V_T, dim ≤ 2|𝒩| + 2; muestras C_q, m_q, s_q; presupuesto a_T = σ_T‖F‖² + κ(F) − ℛ(F).
- Prop 2 (respuestas = polinomios de Dirichlet torcidos por Λ en la malla: Πφ_q = φ_qψ_q): PROVED. Prop 2′ (forma de fluctuación sin polo): PROVED.
- Lema 1 (gauge de Tate g_q = (−1)^q 2sinh T/(¼+ω_q²); (L2′) vale con dos gauges): PROVED.
- Prop 3 (presupuesto σ_T + κ − ℛ y su forma en la malla): PROVED (versión de ventana de una identidad registrada).
- Thm 2 (reducción exacta sobre E_T; el bloque se acopla al complemento sólo vía Arch): PROVED (con las respuestas de Tate incluidas).
- Prop 4 (entradas de grado ≤ 3 en v), Prop 5 (productos y cocientes que aparecen), Lema 6 (falsificadores; familia invariante bajo ϑΛ para |ϑ − 1| < δ_T): PROVED.
- NO-GO (NUMERICAL, lógica PROVED): certificados de Schur sólo con piso sobre todo agrandamiento del bloque (c_need 2.5–8.9 vs λ_min(C) ≈ 1.3); mecanismos de signo basados en identidades del peine (Λ∗1 = log, identidad tipo Selberg Λ_2 = Λlog + Λ∗Λ, factores de Euler locales, identidad del núcleo de Lévy) sobre E_T (sobreviven Beurling 3 → 3.2 y a_3, donde (SL_T) falla por 0.24 y 0.51).
- Resultado: PIVOT; (SL′_T) ℛ ≤ κ − |σ_T| en E_T, exacta a 5·10⁻¹⁰ / 10⁻¹⁵, falla para todo falsificador con el valor de λ_A(T; w).
- Estado R4: dimensión probada del orden de la arena; escape sólo NUMERICAL (OPEN).
- Positivos reutilizables: Lema 1, Prop 2, 2′, 3, Thm 2, Props 4–5 (todo vector de pesos y posiciones).
- Paso siguiente: localizar el cruce T_× de 𝒦_T(F*_T) y escribir ℛ ≤ 𝒦 en E_{T_×}. Tomado: sí, ROUND_007_B (retirado: NO-GO).

### 14. ROUND_005_D.md — forma de ventana como forma de Dirichlet de saltos; representación de estado fundamental
- Objeto: μ_T = K du + Σ v_nδ_{log n}; a_T = (C_0 − A_T)‖F‖² + 𝔈_μ(F); estado fundamental h_T de la forma completa en L²(I_T).
- Lema 1.1 (descomposición y forma núcleo de saltos/matanza κ): PROVED. Prop 1.2 (i)–(iv) CITED; (v) h_T par, (vi) λ_A > μ_0, λ_A ≤ μ_2, (vii) no separabilidad: PROVED.
- Thm 2.1 (representación de estado fundamental sin término residual de matanza): PROVED. Cor 2.2 ((★) ⟺ desigualdad de Poincaré ponderada Q_h(φ) ≥ |μ_0|‖φ‖²_{h²} en φ ⊥ {e^{±t/2}/h}): PROVED.
- Thm 3.1 (reducción de rango uno por sector; (★)_par ⟺ W_par(0) ≤ 0 si n₋ = 1): PROVED (= capacidad polar registrada). Cor 3.2 (μ_1 − λ_A = τ_1²/D; entrelazado λ_A ≤ μ_1 ≤ λ_{A,2}): PROVED. Cor 3.3 (condición suficiente cos²∠(h_T, χ) ≥ |μ_0|/g_1): PROVED; falla NUMERICAL por 0.2–0.5 %.
- Prop 4.2 (a_Tχ_+ = χ_+ω_+ con ω_+ explícito conteniendo ψ(e^{T−t}) y Σ_{n<e^{T+t}}Λ(n)/n): PROVED, validada a 6·10⁻⁹.
- Thm 6.1 (NO-GO, clase 𝒦_gap: cotas inferiores del hueco espectral con pérdida intrínseca — isoperimetría, funciones de Lyapunov, acoplamiento, curvatura-dimensión, supersoluciones): PROVED módulo el tamaño NUMERICAL de la holgura (≤ 4·10⁻⁸ en log 2, ≤ 10⁻¹² en ½log5).
- Monotonía y log-concavidad de h_T: OPEN (NUMERICAL: no monótona). Velocidad de borde: OPEN.
- NUMERICAL: W_ev(0) = −½, W_odd(0) = +½ a 5–6 dígitos en 17 ventanas de [0.60, 1.00] (𝔊_T ≈ 0); cúmulo bajo nulo para Tate al orden de sus autovalores.
- Lema del signo (exacto, OPEN): g_1^{ev} ≥ |μ_0^{ev}| + τ_1²/D y μ_0^{odd} ≥ 0.
- Positivos reutilizables: Lema 1.1, Thm 2.1, Cor 2.2, Thm 3.1, Cor 3.2, Prop 4.2 (todo peine positivo; 4.2 con Λ exacto en ω_+).
- Paso siguiente: probar o refutar y_T = a_T^{−1}χ_ev con ‖y_T‖ ≤ C(T) explícita (ansatz y = χ_+ν, L_+ν = 1). Tomado: no.

### 15. ROUND_005_E.md — familia de Krylov desde la banda de arena
- Objeto: Band(t) = autovectores de Arch_T con autovalor ≤ t, t ∈ {A_T, λ_max(Π_T)}; K′_j(t); cúmulo U_δ, m_δ.
- Lema 3.0 (π_± ≤ A_T): PROVED. Thm 3.1 (conteo de Weyl bilateral N_Arch(δ − π_−) ≤ m_δ ≤ N_Arch(δ + π_+) ≤ N_Arch(δ + A_T)): PROVED. Prop 3.2 (cotas inferiores por comparación puntual son nulas si π_− > δ − α_1): PROVED.
- NUMERICAL: la banda en A_T satura el espacio Galerkin; la banda aguda captura el cúmulo en j = 1 con complemento coercivo (c ≈ 0.4–0.62); j = 2 no ahorra dimensión frente a E_k; m_{10⁻³} ≈ 0.15e^{4T}; λ_max(Π_T)/A_T decreciente (valores Galerkin, corregidos en ROUND_006_A).
- Resultado: PIVOT. La banda aguda es E_{n_P}, dependiente de Λ sólo por un escalar: Prop B de ROUND_004_A se aplica.
- Crecimiento asintótico de λ_max(Π_T) frente a A_T: OPEN (resuelto en ROUND_006_A).
- Paso siguiente: cota λ_max(Π_T) ≤ A_T − pérdida y decidir si λ_max/A_T → 0. Tomado: sí, ROUND_006_A (no tiende a 0).

### 16. ROUND_006_A.md — tamaño de la forma del peine: λ_max(Π_T) frente a A_T
- Objeto: π_±(H) para H = L²(I_T), P_T; V(s) = Σ_{u_n ≤ s} v_n.
- Lema 1.0 (|Π_T(F)| ≤ Π_T(|F|)): PROVED. Thm 1 (π_±(P_T) = π_±(L²(I_T)), por paquetes modulados y aproximación simultánea): PROVED. Corrección: los valores de ROUND_005_E son Galerkin.
- Thm 2 (π_+ ≤ ½max_s[V(s)+V(2T−s)] ≤ ½(A_T+V(T))): PROVED; Cor 2.1 (limsup π_+/A_T ≤ ½): PROVED con cotas de tipo Chebyshev CITED.
- (HT_T) cabeza-cola Σ_{n≤a}v_n ≤ Σ_{X/a<n<X}v_n ∀a ≤ √X: OPEN.
- Thm 3 (π_+ ≥ N_T/(sinh T + T), expresión aritmética exacta): PROVED; Cor 3.1 (liminf ≥ ¼): PROVED dado el teorema de los números primos CITED. Constante exacta en [¼, ½]: OPEN.
- Thm 4 (en P_T la parte de densidad del peine es −∫(u_F′² + ¼u_F²) ≤ 0): PROVED.
- Lema 5.1 (conteo de Weyl arquimediano superior N_Arch(s) ≤ 12.92·T·e^s(s + 6.373)): PROVED. Thm 5 (m_δ ≤ exp(2e^T(1+o(1)))): PROVED.
- Thm 6 (NO-GO, clase: cotas de Weyl del cúmulo desde comparaciones puntuales a_T ≥ Arch_T − θ; ninguna baja de 2T·exp(e^T(1+o(1)))): PROVED dado PNT.
- Fallido: cota Gram/Toeplitz sobre copias desplazadas (circular).
- Positivos reutilizables: Thm 1–5 (genéricos en el peine; Thm 4 sólo densidad).
- Paso siguiente: conteo de espacio de fases por el símbolo conjunto con cola uniforme. Tomado: sí, ROUND_006_C.

### 17. ROUND_006_B.md — familia de palabras mixtas de (M, Π_P)
- Objeto: 𝒲_j(𝒢; S) con 𝒢 ⊂ {M, Π_P, [M,Π_P], H_x, L_x}, S ∈ {𝒩_T, Band}.
- Lema 2.1 (escala log-Sobolev 𝓗 invariante por todas las palabras; incondicional para semillas seno, (H_𝓗) para el cono espectral): PROVED / CONDITIONAL.
- Prop 4.1 (familias de palabras de generadores v-homogéneos desde semilla libre de Λ son invariantes por escala como conjuntos; cΛ actúa sólo por el haz; criterio de rechazo de Danskin): PROVED. Refuta la premisa de ROUND_005_A.
- Prop 4.2 (la única familia inhomogénea es la de Lanczos; ciega a un cúmulo de dispersión δ salvo O(δ)): PROVED.
- Prop 4.3 (halo y fuga con constante ½; H_x* = L_x; [M_0, S_x] = L_x* − L_x): PROVED; corrección a ROUND_005_A Prop 4.2(v).
- Prop 4.4 (matriz 3×3 𝔄_3 en {e, Π_Pe, [M,Π_P]e}; Arch(Πe) − α‖Πe‖² = ⟨Πe, Le⟩ − ⟨LΠe, e⟩ + polar): PROVED.
- (SL̃_3) se cumple NUMERICAL pero nunca rechaza c > 1 ni η > 0 (el fondo crece con c): no puede ser paso de signo.
- NO-GO (clase: familias finitas 𝒲_j(𝒢; S) desde semilla libre de Λ con generadores v-homogéneos, a dimensión pequeña frente a la de captura del cúmulo; y familias de Lanczos de generador inhomogéneo mientras el cúmulo no se resuelve): mecanismo PROVED, confirmación NUMERICAL. Cierra LEDGER C13.
- Positivos reutilizables: Prop 4.1, 4.2, 4.3 (todo peine).
- Paso siguiente: complemento de Schur exacto sobre la banda aguda, desarrollo de Neumann del resolvente y grado al que rechaza 1.01Λ y Λ + 0.1·1_2 en T = 0.9. Tomado: no (en el rango).

### 18. ROUND_006_C.md — conteo del cúmulo por el símbolo conjunto
- Objeto: s_T = m − M_T, q_T; m_δ, m_δ^{L²}; P(τ) = Σ v_n n^{iτ}; S_T = Σ_p a_p².
- Lema 1.1 (promediado exacto a escala 1/T no cambia q_T y fija el peine: M̃_T = M_T): PROVED.
- Thm A (m_δ ≤ (T/(πη))∫(δ+η−s_T)_+ ≤ (T/(πη))(δ+η−s_min)|{s_T < δ+η}|): PROVED. Cor A.1, A.2 (escala de arena exp(4e^T)): PROVED.
- Lema B.0 (modelo de toro: Σb_m² = E|𝒫|^{2k} ≤ (2k)!(eS_T/k)^k; usa factorización única): PROVED. Thm B (grandes valores uniforme |{τ ≤ Ω : M_T > s}| ≤ (Ω + 3π(X^k+1))e√(2k)(4kS_T/(es²))^k): PROVED (teorema de valor medio CITED). Obs B.1 (cola gaussiana como densidad de Bohr sin velocidad): PROVED. S_T = 8T²(1+o(1)): PROVED dado Mertens.
- Cor C, Cor D (m_δ ≤ exp(2e^T(1 + (log T + 0.39 + o(1))/T))): PROVED dado PNT y Mertens.
- Límite de la clase «Thm A + grandes valores con error controlado por el espaciado de {log m : m ≤ X^k}»: ARGUED; no baja de exp(2e^T(1+o(1))).
- Thm B es específico de ℕ (factorización única y espaciado 1/(m+1)), pero es enunciado de tamaño, no de signo.
- Paso siguiente: acotar la energía multiplicativa 𝒩_k(ν) de productos k-ésimos de N_T cerca de razón 1 (θ < 1 da exp((4 − 2/θ)e^T); ventana independiente de k da exp(O(T²))). Tomado: no.

### 19. ROUND_007_B.md — el presupuesto de signo desarmado
- Objeto: a_T = σ_T‖F‖² + κ(F) − ℛ(F) en P_T; ℛ = Π + 𝔢; (SL′_T) en E_T.
- Lema 1.1 (σ_T = C_0 + 4 + ∫_{2T}^∞K_1, C_0 + 4 = 4 − γ − π/2 − log(8π); decreciente, convexo, σ_T < 0 ⟺ T > T_0 = 0.052): PROVED (T_0 raíz NUMERICAL). Corrección: escribir −σ_T, no |σ_T|.
- Prop 1.2 (σ_T‖F‖² + κ(F) = 𝔞^♯(F), forma sin polo de P47, independiente de T, ≥ Arch): PROVED.
- Lema 1.3 (todo F ∈ P_T real cambia de signo ≥ 2 veces; anclaje de Tate |F̂(τ)|² ≤ d_T(τ)‖F‖², d_T(0) = T⁵/360 + O(T⁷); cotas de conteo): PROVED.
- Prop 1.4 (ℛ = Π + 𝔢; 𝒮_q = (1 − (−1)^q e^T)/(¼+ω_q²)): PROVED/CITED. Cor 1.5 (cuatro formas equivalentes del lema del signo, la última Π ≤ Arch en E_T; forma en G ∈ H²_0): PROVED.
- Lema 2.1 (una sola forma sobre la familia anidada P_T): PROVED. Lema 2.2 (continuidad de las piezas sobre el minimizador): PROVED bajo simplicidad (hipótesis invisible a toda precisión alcanzable).
- Prop 2.4 (teorema de contabilidad: el «rol portador» y el cruce dependen de la densidad ν elegida): PROVED.
- Prop 3.1 (cúbica explícita de una respuesta con cortes de ventana): PROVED. Cor 3.2 (clases m ≈ nk, mn ≈ k, mnk ≈ 1; umbrales ½log5, ½log7, ½log8, ½log9; pesos (2T − log max(m,nk))_+): PROVED.
- NO-GO (i) (clase: valores de formas sobre F*_T, en particular localizar T_×): contabilidad PROVED, escalera casi nula NUMERICAL; retira el paso siguiente de ROUND_005_C.
- NO-GO (ii) (clase: firmar una subparte de ℛ o de a_T en E_T — un grado, una clase de coincidencia, la parte exacta o la de factores locales — con error no ≤ λ_A): lógica PROVED; las tres partes de grado (+1.4·10⁻³, −2.8·10⁻³, +1.4·10⁻³) cancelan a 3·10⁻¹².
- Resto exacto OPEN: Π(F) ≤ Arch(F) para todo F unitario en E_T.
- Positivos reutilizables: Lema 1.1, Prop 1.2, Lema 1.3, Prop 1.4, Cor 1.5, Lema 2.1, Prop 2.4, Prop 3.1, Cor 3.2.
- Paso siguiente: fórmula de variación unilateral de λ_A(T) en un umbral de entrada T_e ∈ {½log7, ½log8, ½log9}. Tomado: no (fuera del rango).

---------------------------------------------------------------------------------------------------

## A. Lista deduplicada «no reintentar» (con condición de reapertura) y cotejo con RULES_AVOID.md

Marcas: [AUSENTE] no figura en RULES_AVOID.md; [INEXACTO] figura con enunciado distinto; [OK] figura.

A1. Forma exterior como fuente de signo: identidad de semirrecta, defecto para cΛ/a_P, cancelación de celda,
    sector prolato Q₁ (comb-monótono, lineal acotado). Reapertura: un término no monótono del peine de orden 1;
    el único candidato señalado es 𝒪_w a baja frecuencia de Mellin (nunca ejecutado). (001_B, 002_B) [OK en C1:
    «programa L♯ (forma exterior, …)»; no se menciona el resultado de monotonía de Q₁ ni la circularidad
    «localizar y luego firmar».]
A2. Residuo «bordes de capa κ_{T+log n}»: vacío (un solo borde plano; términos sólo arquimedianos). (001_B) [AUSENTE
    como tal; C1 dice «tabla exterior de la fase 202» sin este cierre.]
A3. Lectura fusionada de la forma exterior como objeto que cumple la cláusula (5): es ζ con mollificador de Möbius.
    (001_B) [AUSENTE; RULES_AVOID F lista la cláusula (5) como no excluida sin esta advertencia.]
A4. Criterios sobre las muestras del bloque Nyquist solas (Prop 4 de 001_C); cuenta de dimensión del bloque como
    portadora de signo. Reapertura: ninguna; todo criterio debe involucrar A_𝒞𝒞^{−1}. [AUSENTE; C1 menciona «dos
    sectores de Nyquist como fuente de signo» en general.]
A5. Germen de B en 0 / momentos de la medida representante. (001_D) [OK: C1 «criterios de germen de Carleman».]
A6. Desigualdades de Schur sólo con piso (I_c), en el bloque mínimo y en todo agrandamiento por respuestas.
    Reapertura: cota inferior de A_𝒞𝒞 de rango finito más escalar que siga la alineación de b = P_𝒞Ax con el
    espectro (propuesta en 002_A, no ejecutada). (002_A, 005_C) [AUSENTE.]
A7. Fondo arquimediano sobre el cono nulo del peine Θ_T como paso de signo: ciego a c; sólo separa en ventanas de
    tangencia, donde Θ_T = λ_A. (002_D, 002_E) [INEXACTO: B10 de RULES_AVOID dice «La concavidad en el peine
    (Danskin) da sólo cotas superiores mientras falte la representación dual de Θ_T; con ella no está cerrada».
    La representación dual existe (002_D Thm 1, PROVED) y 002_E muestra que Θ_T(w) ≥ 0 sobrevive toda modificación
    de tamaño ℓ¹ < Θ_T(Λ)/|c*| donde Θ_T(Λ) > 0 (Cor 4): el estado correcto es PIVOT, «no más débil que (★) donde
    separa».]
A8. Acoplamiento de Schur de las métricas ρ y δ = log(lcm/gcd) por 𝕂_t = [e^{−tδ}], y supresión 𝔸_M ∘ 𝕂_t.
    Reapertura: núcleo que no preserve PSD por Schur solo y sea grande en pares casi coincidentes. (003_B)
    [AUSENTE.]
A9. Condiciones necesarias a_T|_E ⪰ 0 en subespacio fijo finito libre de Λ (planos E_k, banda aguda E_{n_P})
    usadas como paso de signo. Reapertura: familia con dim E_T → ∞ que lleve información dependiente de Λ a
    precisión λ_A. (004_A Prop B, 005_E) [OK parcial: D17 «planos Λ-libres E_k»; falta la forma general de Prop B
    (todo E fijo finito libre de Λ, incluida la banda aguda).]
A10. Familias de Krylov del peine desde el cono negativo arquimediano (j acotado); familias de palabras de
     generadores v-homogéneos desde semilla libre de Λ; familias de Lanczos de A mientras el cúmulo no está
     resuelto. Reapertura: ninguna dentro de la clase; el signo debe ir al complemento de Schur exacto sobre la
     banda capturada. (005_A, 005_B, 006_B) [OK: D17 «familias de Krylov y de palabras de (M, Π) a grado acotado u
     homogéneas»; C1 «familias de palabras de (M,Π) homogéneas». Falta la parte de Lanczos (Prop 4.2 de 006_B).]
A11. Krylov desde la banda de arena con umbral A_T (satura) o con j = 2 como ahorro de dimensión. (005_E) [AUSENTE.]
A12. Mecanismos de signo para (SL_T) construidos con identidades válidas en todo sistema de Beurling o en a_P
     (Λ∗1 = log, Λ_2 = Λlog + Λ∗Λ, identidades generalizadas, cotas de factores de Euler locales, identidad del
     núcleo de Lévy) sobre E_T. (005_C) [OK en esencia: B1 y B7; no se nombra la familia E_T.]
A13. Clase 𝒦_gap: cotas inferiores del hueco espectral de la forma transformada por el estado fundamental con
     pérdida intrínseca (isoperimetría, Lyapunov, acoplamiento, curvatura-dimensión, supersoluciones). Reapertura:
     ninguna (la desigualdad es una igualdad a 10⁻⁸–10⁻¹⁵). (005_D) [INEXACTO/parcial: C1 lista «Markov, principio
     del máximo» y «Bakry–Émery Γ₂», no la clase 𝒦_gap con la representación de estado fundamental de la forma
     completa con el peine.]
A14. Cotas de Weyl del cúmulo por comparación puntual a_T ≥ Arch_T − θ (θ ≥ π_+ ≥ e^T(1+o(1))); suponer
     λ_max(Π_T)/A_T → 0. (006_A) [AUSENTE.]
A15. Cota Gram/Toeplitz de Π_T por las copias desplazadas (circular). (006_A) [AUSENTE.]
A16. Ganancia por suavizado del peine a escala 1/(2T) (exacta, nula). (006_C) [AUSENTE.]
A17. Conteo por Thm A + grandes valores con error controlado por el espaciado trivial de {log m}: no baja de
     exp(2e^T(1+o(1))) (ARGUED). Reapertura: energía multiplicativa de productos k-ésimos más allá del espaciado
     trivial. (006_C) [AUSENTE.]
A18. Valores de formas sobre «el minimizador» F*_T; localizar la ventana de cruce T_×; afirmaciones de «rol
     portador» (dependen de la densidad ν y de la escalera casi nula). (007_B §4.3) [AUSENTE.]
A19. Firmar una subparte de ℛ o de a_T en E_T (un grado, una clase de coincidencia, parte de coincidencias
     exactas, factores locales) con error mayor que λ_A. (007_B §3.4) [AUSENTE como clase; B2 de RULES_AVOID
     cubre estimaciones con holgura en general.]
A20. Anclar el signo en la condición 3×3 (SL̃_3) o en (SL_2^{sc}) sobre {e, Π_Pe, [M,Π_P]e}: comb-monótona en el
     fondo, nunca rechaza c > 1. (006_B §4.4) [AUSENTE.]

Total: 20 ítems. Ausentes 13 (A2, A3, A4, A6, A8, A11, A14, A15, A16, A17, A18, A19, A20); inexactos 2 (A7, A13);
presentes 5, de ellos con omisiones A1, A9, A10, A12 y correcto A5.

## B. Resultados positivos PROVED con alcance exacto

B1. Lema del radical y la identidad de semirrecta W_T(Ef) = 𝒲[Ψ_f] (001_B Thm 1.1, Cor 1.2): f admisible en T;
    sólo para Λ; prueba sin ceros con (I), (E), (F), ζ(0) = −½ y residuo 1.
B2. Defecto para peine arbitrario y ausencia de vector radical común para c ≠ 1 (001_B Prop 1.3, 1.4): w ≥ 0 con
    serie de Dirichlet convergente en σ > 1; F ∈ L², F = O(e^{3x/2}) en −∞, F = 0 en [T, ∞).
B3. Borde plano, términos de borde sólo arquimedianos, φ_0 entra por un escalar (001_B Lema 2.1, Prop 2.2, 2.3):
    datos del núcleo de la forma exterior, N ∉ ℤ para la parte C¹.
B4. Identidad de Nyquist desplazada y con gauge alternado, reducción (L2′) y sus cotas de dimensión (001_C Lema 1–3,
    Thm 1, Prop 1–3): todo T, α, c, η ∈ (0, η_0]; todo peine de pesos ≥ 0.
B5. Lema de dos proyecciones y piso de coercividad c_floor (002_A Lema P, Thm F, Cor F1): complemento 𝒞 del bloque,
    todo gauge, todo peine.
B6. Identidad de muestras y casi-coincidencias en la malla (002_A Prop M, Cor M1–M2): todo k, todo gauge, todo
    peso.
B7. Rango conjunto convexo, max_c λ_A(T; cΛ) = Θ_T, J_T intervalo, 𝒦_T convexo compacto, persistencia Lipschitz,
    criterio de tangencia por el autoespacio inferior (002_D Thm 1, Cor 2–3; 002_E Lemas 1–3, Cor 4, corrección):
    T > ½log2; pesos sobre posiciones fijas.
B8. Factorización de Schur por 𝕂_t ⟺ 𝔸_M ⪰ 0, jaula entrada a entrada, fallo de las prescripciones división y
    Div/Near, semirrecta [t*_M, ∞) (003_B): todo M, todo t > 0, matrices simétricas con diagonal positiva constante.
B9. Separación por paridad de a_T en P_T, criterio de tangencia, anclaje de Weyl, rigidez de casi-núcleo (003_A
    Prop 1–2, Lema 3–4): todo T; Lema 4 para todo vector de modificación δ.
B10. Condiciones necesarias (C_k) explícitas, cotas de R_n(E) y Prop B de tolerancia (004_A): E ⊂ P_T^ev (Lema A) o
     E ⊂ P_T (Prop B) finito libre de Λ, T fijo.
B11. Álgebra de palabras de desplazamientos truncados; Π² = Qσ_v²Q − 𝔏*𝔏 (Λ∗Λ + valor medio ≥ 0 − fuga); grado 3
     con clases W_3(r) ≥ 0; complemento de Schur a nivel de forma (005_A Lema 3.2, Prop 3.3–3.5, Thm 4.1, Prop 4.2,
     Cor 4.3): L²(I_T), K ⊂ 𝒟_T ∩ P_T finito.
B12. Fórmulas de grado 2 de ⟨e, Π²e′⟩, ⟨e, ΠPΠe′⟩ (005_B Prop 1.1–1.2): e, e′ ∈ L²(I_T).
B13. Respuestas del peine como polinomios de Dirichlet torcidos por Λ en la malla; gauge de Tate; presupuesto
     σ_T + κ − ℛ; reducción exacta sobre E_T con acoplamiento sólo arquimediano del bloque; fórmulas de entradas de
     grado ≤ 3 (005_C Lema 1, Prop 2, 2′, 3, 4, 5, Thm 2, Lema 6): todo T, todo peso y posiciones en (0, 2T).
B14. Forma de Dirichlet de saltos con el peine, representación de estado fundamental exacta, reducción de rango uno,
     μ_1 − λ_A = τ_1²/D, entrelazado, a_Tχ_+ = χ_+ω_+ (005_D Lema 1.1, Thm 2.1, Cor 2.2, Thm 3.1, Cor 3.2–3.3,
     Prop 4.2): L²(I_T), toda φ Lipschitz acotada (extensión CITED); Prop 4.2 con Λ exacto.
B15. Conteo de Weyl bilateral m_δ (005_E Lema 3.0, Thm 3.1, Prop 3.2): P_T y toda compresión de Galerkin.
B16. π_±(P_T) = π_±(L²); ¼ ≤ liminf π_+/A_T ≤ limsup ≤ ½; densidad del peine ≤ 0 en P_T; conteo arquimediano
     N_Arch(s) ≤ 12.92Te^s(s+6.373); m_δ ≤ exp(2e^T(1+o(1))) (006_A Thm 1–5, Lema 5.1): todo T (asintóticas dado PNT).
B17. Escala log-Sobolev invariante por palabras; invariancia por escala de familias homogéneas; ceguera de Lanczos
     a cúmulos; halo/fuga con constante ½; matriz 𝔄_3 (006_B Lema 2.1, Prop 4.1–4.4): P_T, semillas en 𝓗.
B18. Promediado exacto inútil; conteo tipo Landau por el símbolo conjunto; momentos en el toro y grandes valores
     uniformes; m_δ ≤ exp(2e^T(1 + (log T + 0.39 + o(1))/T)) (006_C Lema 1.1, Thm A, Lema B.0, Thm B, Cor C–D):
     Thm A para todo peine; Lema B.0/Thm B usan factorización única y espaciado de enteros (específicos de ℕ).
B19. σ_T en forma cerrada; σ_T‖·‖² + κ = 𝔞^♯ independiente de T; anclaje de Tate y nodos; ℛ = Π + 𝔢; cuatro formas
     del lema del signo; una sola forma sobre la familia anidada; contabilidad por densidad ν; cúbica explícita de
     respuesta y umbrales de entrada (007_B Lema 1.1, Prop 1.2, Lema 1.3, Prop 1.4, Cor 1.5, Lema 2.1, Prop 2.4,
     Prop 3.1, Cor 3.2): P_T, todo T.

## C. Obligaciones abiertas (enunciado preciso y lo intentado)

C1. (L2′) en ½log5 + ε: S = A_{N′N′} − A_{N′𝒞}A_{𝒞𝒞}^{−1}A_{𝒞N′} ⪰ 0 en el bloque de dimensión 11 con gauge 1.21–1.24.
    Intentado: piso escalar (002_A, falla), agrandamiento por respuestas (005_C, falla la clase de piso).
C2. Crecimiento del conjunto negativo de la malla: cota inferior superlineal de min_{α,c}#{s^{α,c}_k ≤ 0} y de
    n_−(a_T|L²(I_T)). Intentado: sólo cotas superiores (001_C Prop 2) y numérica.
C3. Bloque a ≥ 2 de la reducción de retículo de la forma exterior: desigualdad sobre 𝔊 que no sea cota de tamaño
    ni reescritura de 𝒲[g] (001_B §2.5). Nada intentado más allá de la observación.
C4. Q₁: término O(1) de la forma exterior; parte incoherente 𝒪_Λ a baja frecuencia de Mellin (002_B). No intentado.
C5. Θ_T ≥ 0 en T = 1: inf{Arch(F) : F ∈ P_T, ‖F‖ = 1, Π(F) = 0} ≥ 0 (002_E). Intentado: Galerkin; reducido a
    tangencia (003_A).
C6. Simplicidad del fondo de a_T en P_T y λ^a_ev(T) < λ^a_odd(T); (C1)–(C3) de 003_A. Intentado: no hay
    Perron–Frobenius en P_T.
C7. Resto de (SL_2^{sc}): Δ_{22} ≥ ((1/2π)∫s_Tσ_v|ê|² + Δ_{12})²/((1/2π)∫s_T|ê|²) − (1/2π)∫s_Tσ_v²|ê|² (005_A §5.3).
    Intentado: descomposición productos/cocientes; sin mecanismo.
C8. (SL′_T) / Π(F) ≤ Arch(F) para todo F ∈ E_T (005_C §5.2, 007_B §3.4): desigualdad cúbica en (v_n) con 2|𝒩|+2
    incógnitas (24 en ½log5 + ε, 84 en T = 1). Intentado: identidades del peine (NO-GO), subpartes (NO-GO).
C9. Lema del signo de 005_D: g_1^{ev}(T) ≥ |μ_0^{ev}| + τ_1²/D(λ_A^{ev}) y μ_0^{odd} ≥ 0. Intentado: herramientas
    de hueco espectral (NO-GO 𝒦_gap).
C10. Rango uniforme de la función de Tate: y_T = a_T^{−1}χ_ev ∈ L²(I_T) con ‖y_T‖ ≤ C(T) explícita (005_D). No
     intentado.
C11. Monotonía, log-concavidad y velocidad de borde de h_T (005_D §4.3). No intentado (numérica: no monótona).
C12. (HT_T) Σ_{n≤a}v_n ≤ Σ_{X/a<n<X}v_n para todo 1 ≤ a ≤ √X y todo T; constante exacta de π_+/A_T en [¼, ½] (006_A).
     No intentado.
C13. Conteo de espacio de fases con cola uniforme en R para M_T, o energía multiplicativa 𝒩_k(ν) ≤ C^kΣb_m² para
     ν ≥ X^{−θk}, θ < 1 (006_C §7). Intentado: momentos con valor medio (cap exp(2e^T)).
C14. Complemento de Schur exacto sobre la banda aguda S_T = D_b − Π_bb − Π_bc(Arch_c − Π_cc)^{−1}Π_cb ⪰ 0 y grado de
     Neumann al que rechaza 1.01Λ (006_B). No intentado.
C15. Fórmula de variación unilateral dλ_A/dT⁺ en umbrales de entrada T_e (007_B §4.5). No intentado.
C16. Familia uniforme en T con dim E_T ≥ N*(T) que lleve el signo en su complemento de Schur a precisión λ_A
     (004_A §5). No excluida; no construida.

## D. Objetos, pasos siguientes o ideas nombrados y nunca retomados (dentro del rango)

D1. Bloque a ≥ 2 / correlación firmada de medias de Möbius con entradas de Gram (001_B §2.5).
D2. 𝒪_Λ restringido al cociente gauge de PW_N a frecuencia de Mellin acotada; matriz en base de Legendre (002_B).
D3. Cota inferior rango finito + escalar de A_𝒞𝒞 sobre el espacio de vectores de acoplamiento y modos W_{t_1}
    (002_A).
D4. Candidata III, medida de Lévy con signo / subordinación entre dos leyes infinitamente divisibles (002_D;
    registrada como dominada, no construida).
D5. Primera prueba de la candidata II con 𝔸_M ∘ [e^{tδ}] para M ≤ 12 y casos simbólicos {1, p, q} (002_D): resuelta
    negativamente en general por 003_B, sin los casos simbólicos.
D6. Desigualdad 2×2 en el plano fijo de Arch con complemento de Schur «no circular» (003_A): ejecutada como test en
    004_A, falla la captura; el complemento de Schur 2×2 explícito no se escribió.
D7. Ancla con semilla E_k (k ≥ 6) bajo generador mixto (005_A, alternativa final): no tomado.
D8. Recalcular T ≥ 1.0 en precisión extendida con Arch de alta precisión (005_B, 005_E): no tomado.
D9. Rango de la función de Tate y_T = a_T^{−1}χ_ev, ansatz y = χ_+ν, L_+ν = 1 (005_D).
D10. Ley de cruce de ventana y desigualdad de dos formas en N′ (005_C): retirada por 007_B.
D11. Conteo de espacio de fases con prueba numérica de Landau–Widom en base de alta frecuencia (006_A §7): sustituido
     por Thm A de 006_C sin la prueba numérica.
D12. Energía multiplicativa 𝒩_k(ν) de productos de N_T (006_C §7).
D13. Complemento de Schur exacto en la banda aguda, desarrollo de Neumann, grado de rechazo (006_B).
D14. Fórmula de variación de λ_A en umbrales de entrada (007_B).
D15. Inyección del índice: entradas pedidas para 003_B, 005_D (𝒦_gap, Prop 4.2, valores W_par(0) = ∓½), 007_B
     (P211-7B): acciones de registro, fuera del alcance de esta lectura.

## E. Cobertura

Archivos en el rango (orden de `ls *.md | sort`): ROUND_001_B, ROUND_001_C, ROUND_001_D, ROUND_002_A, ROUND_002_B,
ROUND_002_D, ROUND_002_E, ROUND_003_A, ROUND_003_B, ROUND_004_A, ROUND_005_A, ROUND_005_B, ROUND_005_C, ROUND_005_D,
ROUND_005_E, ROUND_006_A, ROUND_006_B, ROUND_006_C, ROUND_007_B — 19 archivos, ≈ 470 KB. Leídos completos: 19 de 19.
No hay archivos ROUND_002_C, ROUND_004_B…, ROUND_006_D ni ROUND_007_A en el listado del rango. Se leyeron además
`RULES_AVOID.md`, `OBJECT_SPEC.md` y `STATEMENT_001.md` para el cotejo. Ningún archivo o tramo del rango quedó sin
leer. Los guiones numéricos citados por los archivos (scratchpad) no se leyeron.
