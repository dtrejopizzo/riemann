# Anexo 211 — archivos ROUND_007_C a ROUND_016_A (lectura completa)

Fuente: `../phase-211-sign-sandbox/`, archivos `*.md` en orden alfabético (`ls *.md | sort`) desde `ROUND_007_C.md`
hasta `ROUND_016_A.md` inclusive: 22 archivos (no existen ROUND_008_B, ROUND_010_B ni ROUND_014_B). Notación de
`STATEMENT_001.md`: a_T = Arch − Π sobre P_T, λ_A(T), v_n = 2Λ(n)/√n, N = e^{2T}, λ = e^T, c = 2πN, m(τ) =
Re ψ(¼+iτ/2) − log π, K el núcleo de Lévy, C_0 = m(0). Objetivo (★): λ_A(T) ≥ 0 para todo T. Además: W_T forma
completa, E mapa de suma Ef(x) = e^{x/2}Σ_{n≥1}f(ne^x), ψ_k prolatos pares de [−λ, λ] con parámetro c, χ_k
concentraciones, d_k = 1 − χ_k, ε_k = i^k, 𝒯 mapa de cola, 𝒲 forma completa en la recta. Falsificadores de la regla 4:
(a) cΛ, (b) a_P / a_3 (primo 2 borrado), (c) sistemas de Beurling (desplazamiento 3 → 3.2), (d) modificación finita.
Etiquetas tal como figuran en los archivos. «Tomado» indica si un archivo posterior del rango ejecutó el paso.

---------------------------------------------------------------------------------------------------

## Entradas por archivo

### 1. ROUND_007_C.md — falsificadores certificados (a_3, 3 → 3.2, 1.1Λ)
- Objeto: a_T^w(F) = C_0‖F‖² + Lev(c_F) − Σ_x w_x c_F(x) para peines finitos w; testigos F = Σ a_k sin(kπ(t+T)/2T)
  en P_T con cerramiento en aritmética de bolas.
- Lema 1 (cota por testigo): PROVED. Lema 2 (extensión por cero: a_{T′}(F̃) = a_T(F), testigo vale para todo T′ ≥ T): PROVED.
- Lema 3 (forma de Lévy en senos de Dirichlet: fórmula cerrada de c_F, cola ∫_{2T}^∞K = −log tanh(T/2) + π − 2arctan e^T,
  cota en [0, δ] por ‖F′‖²(δ²/4 + δ³/12)): PROVED.
- Thm 1: λ_A(½log5 + 10⁻⁴; a_3) ≤ −0.50528: PROVED. Thm 2: λ_A(½log5 + 10⁻⁴; 3 → 3.2) ≤ −0.23448: PROVED.
  Thm 3: λ_A(1; 1.1Λ) ≤ −0.078244: PROVED (todos para todo T′ mayor).
- Registro: NO-GO (PROVED) de mecanismos de signo basados sólo en identidades válidas para a_3 o 3 → 3.2 (Λ∗1 = log,
  identidades de Selberg, cotas de factores de Euler, identidad del núcleo de Lévy) en T ≥ ½log5 + 10⁻⁴.
- Resto abierto: Θ_T(w) < 0 para a_3 y 3 → 3.2 (criterio de dos testigos en μ enunciado, no ejecutado): OPEN;
  λ_A(T; 1.1Λ) < 0 para T < 1: NUMERICAL; no-rechazo de la familia de Krylov en c = 1.1: NUMERICAL.
- Positivos reutilizables: Lemas 1–3 (todo peine finito); tres certificados con ≤ 5 coeficientes racionales.
- Paso siguiente: certificar Θ_T < 0 por cubrimiento en μ y 1.1Λ en T = 0.9. Tomado: no.

### 2. ROUND_007_D.md — mitad inferior de una ley bilateral para λ_A
- Objeto: ley λ_A(T) = L(T)(1 + o(1)); comparación con λ_W (forma completa) y con cΛ, a_3; autovalores no
  restringidos μ_k de a_T en L²_ev(I_T), momentos de Tate τ_k.
- Prop 4.1 (λ_W^par ≤ λ_A^par ≤ λ_{W,2}^par): PROVED. Cor 4.3 (pisos λ_A ≥ 2^{−1518} en T ≤ ½log12, ≥ 2^{−2904} en
  T ≤ ½log15): transferencia PROVED de insumos CITED.
- Prop 4.2 (corrección de capacidad; «λ_A ≥ λ_W − 𝔤/‖h‖²» REFUTADA en general por modelo 2×2): PROVED.
- Prop 4.4 (una ley para λ_W sólo transfiere piso; −log λ_A ≤ 4πe^{2T} − 9T + O(1)): CONDITIONAL (banda κ OPEN).
- Lema 4.6 (λ_A^ev ≥ L ⟺ τ₀²/(|μ₀|+L) ≥ Σ_{k≥1}τ_k²/(μ_k − L)): PROVED. Cor 4.7 (con n₋ = 1: μ₁ ≥ L y τ₁² ≤ ηL·D(L)
  ⟹ λ_A^ev ≥ (1−η)L; recíproco λ_A ≥ L ⟹ μ₁ ≥ L): PROVED reduction.
- NUMERICAL: λ_A a 40–80 dígitos en T = 1.0–1.4; ley de tasa 2: −ln λ_A = c₁e^{2T} + c₂T + c₃, c₁ → 4π desde arriba
  (12.99 → 12.59); familia simplemente exponencial NO-GO como ley (falla por 14 órdenes en T = 1.4); sin saltos en
  contactos ½log7, ½log8 (≥ 0.03 dígitos); falsificadores cruzan cero en T ≈ 0.48–0.67 con tamaño O(10⁻²), luego −|1−c|g(T).
- Resto: (N1′) μ₁(T) ≥ L(T) ≈ exp(−4πe^{2T}) — no más débil que (★), con margen; ningún mecanismo de la fase da un
  piso positivo para μ₁. PIVOT.
- Positivos reutilizables: Prop 4.1 (sándwich), Cor 4.3 (pisos hasta ½log15), Lema 4.6, Cor 4.7.
- Paso siguiente: cota inferior de μ₁ con sensibilidad de Hellmann–Feynman dμ₁/dc = Π_T(e₁). Tomado: no.

### 3. ROUND_007_E.md — familia de respuestas del peine E_T en multiprecisión (T = 1.0, 1.2, 1.4)
- Objeto: E_T = N′ ⊕ P_𝒞Π(𝒩_η + 𝒯) (bloque Nyquist negativo con gauge + respuestas Π), complemento de Schur exacto.
- Todo NUMERICAL; nada PROVED. PIVOT.
- Hallazgos: E_T captura el fondo del clúster a ángulo 10⁻⁸–10⁻¹⁵, complemento coercivo (λ_min(C) ∈ [0.9, 2.5]),
  pero λ_min(a_T|E_T) excede λ_A en 6/13/31 órdenes (T = 1.0/1.2/1.4): el signo vive en el acoplamiento de Schur.
  Condición necesaria falla para 0.99Λ, 1.01Λ, 1.1Λ, a_3, v_2 + 0.1 (confundida por saturación). dim E_T ≈ 7× clúster.
- Resto: R3(i) (captura a precisión λ_A) no cumplido; R1 (crecimiento vs saturación) OPEN; corrida T = 1.4 con q_cap = 120
  degenerada.
- Paso siguiente: acoplamiento B C⁻¹ Bᵀ con N ≥ 200, truncación del bloque a fracción fija de N. Tomado: sí, ROUND_008_D.

### 4. ROUND_008_A.md — complemento de Schur de banda exacto y expansión de Neumann en el peine
- Objeto: banda espectral B_t = span{u_l : α_l ≤ t} de Arch, complemento C_t; Arch diagonal por bloques, acoplados
  sólo por el peine; S_T = D_b − Π_bb − Π_bc C⁻¹ Π_cb, C = Arch_c − Π_cc.
- Thm 2.1 (reducción de banda exacta para t_c > π_+; (★)_T ⟺ S_T ⪰ 0; cotas cuantitativas con κ = ‖C⁻¹Π_cb‖): PROVED.
- Thm 3.1 (C = Arch_c^{1/2}(1−X)Arch_c^{1/2}; serie de Neumann converge sii r = ‖X‖ < 1, suficiente ‖Π‖ < t_c; término
  k homogéneo de grado k+2 en v con coeficientes sólo arquimedianos; cola bilateral ε_K; K impar ⟹ S_T ⪯ S_T^{(K)}): PROVED.
- Cor 3.2 (qué certifica una truncación; grado necesario K+1 ≳ log(‖Y*Y‖/((1−r)λ_min S_T))/log(1/r)): PROVED.
- Obs. 3.3: S^{(K)}(cv) no es homogénea (no ciega a c como las familias de palabras).
- El archivo termina en la Obs. 3.3: la §4 numérica anunciada y las secciones Result / Next step no figuran en el
  archivo leído (ROUND_008_D cita de él K* ≈ 150 con cola certificada, ≈ 25–40 en la práctica, y K ≈ 7 para 1.01Λ).
- Positivos reutilizables: Thm 2.1, Thm 3.1, Cor 3.2 (válidos para toda compresión de Galerkin y todo peine).
- Paso siguiente: no consignado. Tomado: la pregunta del grado la retoma ROUND_008_D.

### 5. ROUND_008_C.md — variación unilateral de λ_A en T, dos corchetes y Grönwall en la variable de ventana
- Objeto: dilatación U_rF; virial 𝒱^♯ = 𝒱_∞ − Σ v_n log n·c_F′(log n) + τ(F) (momentos de Tate × multiplicadores),
  pliegue de entrada φ; presupuesto de franjas de borde 𝔈_h.
- Lema 1.2 (m′ ≥ 0 en [0, ∞); 0 ≤ 𝒱_∞ ≤ M₁‖F‖²): PROVED.
- Thm 1 (λ_A(T+h) ≤ λ_A(T) − (h/T)𝒱^♯(F) − h⁺φ(F) + o(h) en el autoespacio inferior): PROVED bajo (R_E); igualdad de
  Danskin CONDITIONAL en (U). Cor 2.2 (𝒱^♯ ≥ 0 en E_T; pliegue: costo en sector par, pago en impar): PROVED bajo (R_E).
- Prop 2.3 (tres marcos: extensión por cero, dilatación, truncación): PROVED.
- Prop 3 (decremento ≤ energía de franjas de borde: (λ_A(T) − λ_A(T+h))‖G♯‖² ≤ 𝔈_h): PROVED para minimizadores acotados
  cerca de ±T; ARGUED en general. Cor 3.1 (derivada entre virial y presupuesto de borde): PROVED bajo hipótesis.
- Prop 4 (Grönwall discreto sobre incrementos, sólo continuidad): PROVED. Prop 5 (D ≤ Cλ, (EB_C), (VE_C) con C sin
  especificar = (★) + Lipschitz; todo falsificador falla automáticamente en su primer cero por su propio signo):
  PROVED; versión uniforme = (★) en el siguiente paso de Euler: ARGUED. Prop 6 (D/λ por el minimizador): PROVED bajo (R_E).
- NO-GO (reformulación): Grönwall en T, clase 𝒦_H; la constante que piden los datos C ≈ 8πe^{2T} − 21 es la constante
  de Slepian 2 en c. NUMERICAL: Hellmann–Feynman reproduce la derivada a 11–22 dígitos; virial ≈ 1.003 cancela a precisión
  relativa C·T·λ (3.4·10⁻²¹ en T = 1).
- Resto: (EB_C) con C(T) = 8πe^{2T}(1+o(1)) para T ≥ ½log5: OPEN; forma de Hadamard 𝔈_h ≍ (θ₊² + θ₋²)h: ARGUED.
- Positivos reutilizables: Thm 1, Cor 2.2, Prop 2.3, Prop 3, Prop 4 (para todo peine).
- Paso siguiente: medir 𝔈_h/h con base que resuelva el borde y las trazas θ_±; no reintentar Grönwall con otro
  denominador. Tomado: no.

### 6. ROUND_008_D.md — acoplamiento de Schur de E_T: rango, Neumann y grado de truncación
- Objeto: S_E = a_EE − a_EC a_CC⁻¹ a_CE con E = E_T, C = E_T^c; X = Arch_CC^{−1/2}Π_CC Arch_CC^{−1/2}.
- Prop 1 (a_CE = Arch_CE − Π_CE P_V; a_EC = Arch_EC sólo sobre N′): PROVED.
- Thm 2 (Neumann sobre E_T^c, cola, estructura de grados k, k+1, k+2): PROVED bajo (H₋); (H₋) NUMERICAL, sin prueba
  (π_− probado excede λ_min(Arch_CC) 2.4×). Cor 3 (grado necesario ∝ log(1/λ_A)/log(1/r)): PROVED bajo (H₋).
- Prop 4 (desigualdad polinomial explícita finita suficiente en T = 1, N fijo, V y C congelados): PROVED condicional a (H₋).
- NUMERICAL: acoplamiento O(1) y de rango casi completo; r ≈ 0.54 (T = 1), 0.65–0.67 (T = 1.2); truncaciones pares bajas
  con signo equivocado; K* ≈ 25–30 / 105–125, cola certificada K ≈ 80–84 / 205–220; falsificadores rechazados en K = 0–7.
- NO-GO (clase: truncación de Neumann de grado finito del acoplamiento de Schur sobre E_T con cola por radio espectral):
  mismo muro que la banda arquimediana de ROUND_008_A; términos sin signo, cancelación relativa 10⁻⁹ por orden.
- Resto: versión uniforme en N; cota de grado independiente de λ_A: OPEN.
- Paso siguiente: polinomio de Chebyshev/minimax de 1/(1−x) (sigue ∝ log(1/λ_A)); cerrar la clase salvo resumación
  firmada. Tomado: no.

### 7. ROUND_008_E.md — ley de margen de λ_A frente al defecto prolato 1 − χ_k(2πN)
- Objeto: R(T) = λ_A/(1 − χ_0(2πN)); imágenes Eψ_k; espacio 𝒜⁺_T (f par, C², f(λ) = f′(λ) = 0, f(0) = ℱf(0) = 0);
  energías fuera de banda L₁, L₂.
- Thm 3.1 (W_T(Ef) ≤ Kλ^{−2}(L₁² + L₂²) en 𝒜⁺_T): PROVED dado thm:ext-half. Cor 3.2 (λ_A ≤ 4K(L₁²+L₂²)/‖f|‖²): PROVED.
- Prop 3.3 (conteo de índices: 5 dimensiones para λ_A — cuatro funcionales f(0), ℱf(0), A(Ef), B(Ef) —, 3 para λ_W): PROVED.
- Lema 3.4 (fuga ponderada de prolatos con taper): ARGUED; Cor 3.5 (mitad superior índice 8): CONDITIONAL (superados por
  ROUND_009_A; la comparación con 1 − χ_0 vía cociente de Fuchs quedó retirada).
- Conj 4.1 (λ_A ≥ κ₋N^a(1 − χ_0), forma aguda κ₋(1 − χ_8)): OPEN. Prop 4.2 (bajo prob:ext-L, λ_A ≥ (κ/4)N^{−A_0−1}(1−χ_0)):
  transferencia PROVED, CONDITIONAL. Lema 4.3 (piso de fuga en subespacio restringido d_q/(1 + ‖C^{−1}‖²‖C‖²)): PROVED;
  aplicación (índice 6) CONDITIONAL en κ_C polinomial (OPEN).
- Prop 5.1 e identidad (5.1) W^w_T(Ef) = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef]; ley con robustez nula (sobrevive cΛ sólo con
  |1−c||Π_T(F★)| ≤ λ_A): PROVED.
- NUMERICAL: R ≈ e^{17.1}N^{9.6}; κ₈ = λ_A/(1 − χ_8) ∈ [0.74, 1.62] en 37 ventanas; el minimizador está en
  P_T ∩ span{Eψ_0, …, Eψ_8} a ángulo 10⁻⁴; sólo ψ_0, ψ_4, ψ_8 entran en el sector par; brecha λ_A/λ_W = cambio de índice 4 → 8.
- NO-GO (NUMERICAL): mitad superior con la sola función de prueba PEψ_0 (cociente 0.12–0.26, ángulo 63–75°).
- Resto: mitad inferior; rango intermedio 10 ≲ k ≲ 4N no tocado por ninguna coercividad; acoplamiento bloque bajo–resto.
- Positivos reutilizables: Thm 3.1, Cor 3.2, Prop 3.3, Lema 4.3, (5.1)/Prop 5.1.
- Paso siguiente: probar Lema 3.4; probar prob:ext-L en forma prolata por sectores. Tomado: sí, ROUND_009_A y ROUND_009_B.

### 8. ROUND_009_A.md — cota de fuga de prolatos molificados (Lema 3.4′); sólo cota superior
- Objeto: V_d = {f_a = (Σ_{k∈K_d}a_kφ_k(x/a)1_{[−a,a]}) ∗ ρ_ε}, a = λ − ε, b = λ²/a (c = 2πN exacto), ε = θλ^{−3},
  θ = 1/(48π²), ρ(u) = (35/32)(1 − u²)³₊, d ∈ {3, 5}.
- (F1) 0 ≤ ϑ_k ≤ k(k+1) + c²; (F2) ϑ_k ≥ c/8; (F3) m_k = ∫_1^∞φ_k² = (1−χ_k)/(2χ_k): PROVED.
- Lema 2.1 (lámina de borde de ancho 1/(12c²)): PROVED. Lema 2.2 (φ_k(1)² ≤ 27c²m_k, ∫_1^∞φ_k′² ≤ 60c⁴m_k): PROVED.
  Lema 2.3 (∫_0^hφ_k² ≤ 12h√c, función de Sonin): PROVED.
- Lema 3.4′ ((L₁² + L₂²)/‖f|‖² ≤ C_dN⁹(1 − χ_{2d−2}), C_5 = 1.3·10¹⁶, N ≥ 1.6·10⁶; existencia para 3 ≤ N < N₀): PROVED
  (Landau y Titchmarsh CITED).
- Cor 4.1 (λ_A ≤ 4KC_5N⁹(1 − χ_8), λ_W ≤ 4KC_3N⁹(1 − χ_4)): PROVED dado thm:ext-half. §7: K = 141 admisible (PROVED);
  Cor 7.1 (λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πe^{2T}} para N ≥ 1.6·10⁶): PROVED dado thm:ext-half y cota no asintótica CITED
  (arXiv:1804.01257, Thm 3.2).
- Falló: constante explícita para N < N₀; exponente b = 9 no agudo; comparación 1 − χ_8 vs 1 − χ_0 no reprobada.
- Positivos reutilizables: Lemas 2.1–2.3, Lema 3.4′, Cor 4.1, Cor 7.1 (cota superior doblemente exponencial explícita).
- Paso siguiente: bajar N₀ (sup|φ_k| ≤ C(k)c^{1/4}) y b (decaimiento 1/s exacto de Φ_a′). Tomado: no.

### 9. ROUND_009_B.md — regla de selección por clase de Fourier y mitad inferior en el sector autodual
- Objeto: clases de índice prolato ε_k = i^k; h_k = P_+Π_TEψ_k; par (M, D) con D = Σd_ka_k²; bloques L = {0, 4, 8},
  medio 12 ≤ k ≤ 4N, alto k > 4N.
- Thm 1.1 (defecto de paridad exacto P_{−ε}Π_TEf = ½RΠ_TE(ℱf − εf)): PROVED. Thm 1.2 (‖ℱf − εf‖² = Σ2(1 − εε_k√χ_k)a_k²):
  PROVED dado hechos CITED. Lema 1.3 (‖Eh‖² ≤ ζ(2s)λ^{2s}∫u^{2s}|h|²): PROVED. Cor 1.4: PROVED para datos C¹.
- Thm 1.5 + Lema 1.6 (desacople de clases en sector par; términos cruzados ≲ poly(N)√(d_jd_k)): PROVED.
- §1.7 (la clase casi nula del sector par es ℱ-autovalor +1): PROVED (lectura). Lema 2.1, Prop 2.2 (Schur de dos y tres
  niveles): PROVED. Cota (2.1) λ_A ≥ κ(1 − χ_8)N^{−b} en el subespacio: PROVED como implicación, CONDITIONAL en tres
  constantes (luego medidas en ROUND_010_A: factor 10⁻⁶; «no leer como cota de λ_A»).
- §2.4(iii) (decaimiento de α_HI por vectores casi-gauge): ARGUED — RETIRADO en ROUND_010_A.
- NUMERICAL: espectro par λ_j^ev ≈ (0.85–2.0)(1 − χ_{4j+8}); Schur de tres niveles cierra hasta 1.4–2.0·4N.
- Falsificadores: la regla clase–paridad es Λ-libre (no es paso de signo); la casi-nulidad de la clase +1 se destruye
  por 𝒫_{Λ−w}; el mapa adaptado a a_P no entrelaza ℱ con R (PROVED).
- Resto: (HR) estimación de rango alto: (a) inf a_T/ℓ_HI ≥ κ_HN^{−b}; (b) Γ′² ≤ (1−η)κ_LMκ_HN^{−b}: OPEN.
- Positivos reutilizables: Thm 1.1, Thm 1.2, Lema 1.3, Thm 1.5, Lema 1.6, Lema 2.1, Prop 2.2.
- Paso siguiente: probar (HR)(a) con D gauge-minimizado en el bloque alto; medir κ_C y ‖Gram‖. Tomado: sí, ROUND_010_A.

### 10. ROUND_010_A.md — (HR) con cociente gauge consistente; escala de las herramientas genéricas en el peine
- Objeto: par consistente (M(a) = W_T(Ef_a), D_g = D − DJH^{−1}JᵀD) en 𝒜_K (cinco condiciones: f(λ) = f(0) = ∫f =
  A(Ef) = B(Ef) = 0).
- Obs. 1.1 (el par de 9B difiere en tres puntos identificados): PROVED. (3.1) W_T(g) = (1/2π)∫(m − P_T)|ĝ|² + 2A(g)B(g),
  P_T(τ) = Σ_{n<N}v_n cos(τ log n): PROVED.
- Lema 3.1 (Markov L², (K+2)²/L): PROVED. Prop 3.2 (lem:ext-hf es vacío sobre datos de grado K salvo K superpolinomial
  en N): PROVED.
- Prop 3.3 NO-GO (clase 𝒦_S: estimaciones que ven el peine sólo por su masa total Σw_n ≤ S): existen w ∈ 𝒦_S y g ∈ P_T
  con espectro en Ω₀ ≤ |τ| ≤ 2Ω₀ y W^w_T(g) < 0 para log(2 + 3Ω₀) ≤ S − C₀: PROVED; transferencia al bloque alto ARGUED.
- Prop 4.1 (solapes cruzados de prolatos ≡ 0; todo el acoplamiento es el emparejamiento simbólico (4.1)): PROVED.
- NUMERICAL: α_HI = O(1) en el par consistente (no colapso), decrece ≈ 4N/K; Γ′ crece; cota de Schur ensamblada
  θ_K = 0.86 → 0.025; falsificadores rechazados sólo en el bloque bajo (≈ −10²⁰ d_8).
- Correcciones: 9B §2.4(iii) RETIRADO; constante de (2.1) medida (≈ 3–4·10⁻⁶).
- Resto: (HR)(a) uniforme en K, (HR)(b), (HR-Π) en el plunge (m×m, m = O(log N log(1/ε))): OPEN; el rango
  super-plunge hasta e^{cλ} no se reduce a dimensión finita.
- Positivos reutilizables: (3.1), Lema 3.1, Prop 3.2, Prop 4.1.
- Paso siguiente: herramienta de valor medio/valores grandes de P_T en el bloque alto; subir Nb. Tomado: sí, ROUND_011_A
  (teoría) y ROUND_011_B (numérica).

### 11. ROUND_011_A.md — (HR)(a) por valores grandes de P_T; incertidumbre; rango abierto exacto
- Objeto: paquetes g₀ = β(x/T)cos(τ₀x); P^ρ_T(τ) = Σ_{n<N}v_nρ(log n/T)cos(τ log n), ρ autocorrelación normalizada de β;
  Σ₀ = Σ_{n<N}v_n, S₂ = Σ_p a_p².
- Lema 1.1 (cálculo de paquetes): PROVED. Prop 1.2 (necesidad: toda (HR)(a) coerciva ⟹ P^ρ_T(τ₀) ≤ m(τ₀) − κ + O(1/(τ₀T))
  para todo τ₀ ≥ 2Ω_lo): PROVED.
- Lema 2.1 (energía local a escala 1/T): PROVED. Prop 2.2 (espesor de {P_T ≤ ϑm} + Kovrijkine CITED da sólo condición
  puntual (2.1), más fuerte que (1.2)): PROVED.
- Thm 3.1 (P^ρ_T < ϑm en [Ω, 2Ω] si (3.1); log Ω_B = (64/(eϑ²))Te^{2T}(1+o(1))): PROVED dado Mertens/PNT CITED.
  Cor 3.2 ((HR)(a) con θ → 0 para datos sobre Ω_B, coercividad ≍ TN): PROVED.
- Prop 4.1 (sup_{[Ω,2Ω]}P^ρ_T ≥ c₁T para Ω ≥ N²; luego (1.2) falla para cΛ con c ≥ c* absoluto): PROVED.
- NO-GO (clase: medida de valores grandes + Logvinenko–Sereda/Kovrijkine): colapsa a la cota puntual. NO-GO (clase:
  momentos de orden k con error por espaciado entero): no certifica bajo log τ ≈ (64/e)TN; sin error de espaciado, no
  bajo log τ ≈ 8T² (ARGUED, modelo de toro).
- Resto: (1.2) en 2T ≲ log τ < log Ω_B: OPEN; el plunge no tiene papel especial.
- Positivos reutilizables: Prop 1.2, Lema 2.1, Prop 2.2, Thm 3.1, Cor 3.2, Prop 4.1.
- Paso siguiente: (1) escaneo numérico de m − P^ρ_T; (2) gran criba por energía multiplicativa de productos k-ples.
  Tomado: (1) sí, ROUND_011_C; (2) no.

### 12. ROUND_011_B.md — ¿es uniforme en K el cociente gauge alto? (prueba de decisión)
- Objeto: α_HI(K), Γ′(K), θ_K del par consistente con Nb ≈ 2.5K; todo NUMERICAL, nada PROVED.
- Hallazgos: tope de resolución k_* ≈ 0.32–0.35·Nb (no 0.4·Nb); α_HI converge desde abajo en Nb (productos de 10A sesgados
  hacia abajo); α_HI ≳ 3·4N/K ajusta todo; piso positivo ≤ 0.2 (T = 0.8), no visto en T = 1.0; clase +1 sola plana
  (≈ 1.9, ≈ 2.9); el decaimiento es la mezcla de clases.
- NO-GO (clase: ensamblaje de Schur de dos bloques LM/HI con normalización ℓ_g diagonal por bloques, NUMERICAL): θ_K → 0
  en K ≈ 4.5·4N (T = 0.8), 3.3·4N (T = 1.0) mientras la forma sigue positiva (Ritz 1.3–1.5 λ_A). (HR)(a) uniforme no apoyado.
- Falsificadores: el bloque alto no ve 1.01Λ (Δ < 0.1 %); a_3 rechazado sólo en el bloque bajo.
- Paso siguiente: ensamblaje de tres bloques separando la clase en el bloque alto; (HR)(a) con normalización c·4N/K.
  Tomado: sí, ROUND_012_B (primera parte).

### 13. ROUND_011_C.md — margen de paquete m − P^ρ_T: reducción finita, mínimos y valores directos
- Lema 1.1 (m estrictamente creciente; P^ρ_T ≤ Σ^ρ_T; (1.2)_κ vale para τ ≥ τ*_κ, log τ*_κ ≤ Σ₀ + κ + 2 ≍ 4e^T): PROVED.
- NUMERICAL: inf(m − P^ρ_T) > 0 en todo el rango alto para T = 0.8–2.5 (tres perfiles) y T = 3 (cos², bump); mínimo
  0.341 (T = 2, indicatriz molificada); el peor centro está justo sobre el plunge (1.1–1.6·2πN); valores directos
  W_T(f)/‖f‖² coinciden con m − P^ρ_T a ≤ 2.4·10⁻³; zona de peligro del modelo de toro vacía para T ≲ 6.5 (el tope Σ^ρ_T
  manda); presupuesto en cΛ ≈ 9 % en T = 2.
- Resto: cota inferior uniforme en T del margen: no decidida; T = 3 ind en [2·10⁶, 3.4·10⁸] no escaneado.
- Positivos reutilizables: Lema 1.1 (vale para todo peine v_n ≥ 0 y |ρ| ≤ 1).
- Paso siguiente: probar (1.2) en las primeras celdas sobre el plunge uniformemente en T. Tomado: parcialmente,
  ROUND_012_A (rangos certificados y NO-GOs de prueba uniforme).

### 14. ROUND_012_A.md — (1.2) sobre el plunge: rango certificado, forma de operador para todo perfil, tres NO-GOs
- Lema 1.1 (|ρ_β| ≤ 1, ≤ ½ para |u| ≥ 1, 0 para |u| ≥ 2): PROVED. Lema 1.2 (ρ explícita y no creciente para cos²): PROVED.
- Thm 2.1 ((1.2) para todo perfil, T ≤ log 2, κ = 0.069): PROVED. Thm 2.2 (perfil cos², T ≤ 2.64, κ = 0.0486): PROVED
  asistido por computadora (intervalos).
- Prop 3.1 (sup_β P^{ρ_β}_T(τ) = λ_max(A_τ), A_τ f = ½Σv_n cos(τ log n)[f(x+log n) + f(x−log n)]1_{[−T,T]}): PROVED como
  enunciado; su lectura como condición para (HR)(a) quedó invalidada en ROUND_015_C.
- NO-GO 4.1 (cota trivial con perfil fijo: Σ^ρ_T crece exponencialmente): PROVED. NO-GO 4.2 (paquetes cortos de longitud
  o(T)): PROVED como enunciado lógico. NO-GO 4.3 (valor medio + Sobolev/Gallagher: pérdida e^T√T; familia cerrada).
  4.4 heurística de valor extremo gaussiano: ARGUED y contradicha (NUMERICAL: margen ind plano ≈ 0.355, T = 3–4.5).
- Resto (U): existe κ > 0 con λ_max(A_τ) ≤ m(τ) − κ para T > log 2 y 2πN(1+δ) ≤ τ ≤ 2π·exp(Σv_n + κ): OPEN (luego
  reformulado con banda en ROUND_016_A). Toda prueba debe ser aditivamente exacta a O(1) sobre una cantidad ≍ 2T.
- Positivos reutilizables: Lemas 1.1–1.2, Thm 2.1, Thm 2.2.
- Paso siguiente: explicar el bloqueo sup P ≈ log(τ/2π) − 0.35 por proceso B/Vaughan; calcular λ_max(A_τ). Tomado:
  sí, ROUND_013_A y ROUND_013_B.

### 15. ROUND_012_B.md — ensamblaje de tres bloques LM/H₊/H₋; estructura de clase del acoplamiento
- Thm 1.1 (conjugación de signo: W_T(Ef, Eg) = Σa_jb_kε_jε_k𝒢_{jk}, 𝒢_{jk} = 𝒲(𝒯u_j, 𝒯u_k), M = ZᵀS𝒢SZ): PROVED dado (S)
  ecuación de Slepian en toda la recta CITED y (T) ROUND_001_B.
- Cor 1.2 (acoplamiento H₊–H₋ = −Z₊ᵀ𝒢_{+−}Z₋, sin factor pequeño): PROVED → NO-GO de toda prueba de pequeñez de ese
  acoplamiento por la regla de selección o por simetría de clase. Cor 1.3 (M(a₊ + a₋) = 𝒢[a₊ − a₋]): PROVED.
- Prop 1.4 (acoplamiento bajo–alto: forma PROVED, constantes ARGUED, comparación de fuga CONDITIONAL).
- NO-GO (clase: Schur de tres bloques LM/H₊/H₋ con normalización ℓ_g diagonal por bloques, NUMERICAL): θ₃ < 0 desde
  K ≈ 3·4N / 2.4·4N, peor que dos bloques; corte por rango de índice también negativo (T = 1.0, K ≈ 3.2·4N).
  α₊, α₋ planos; crece G_{+−}; la forma sigue positiva.
- Falsificadores: Thm 1.1 usa Λ (relación del radical) pero no lleva signo; el bloque alto no distingue Λ de 1.01Λ, a_3.
- Positivos reutilizables: Thm 1.1, Cor 1.2, Cor 1.3; regla: descomponer en la variable ciega a la clase b = Sa a lo
  largo del eje de índices.
- Paso siguiente: barrido en bandas de 𝒢 en b = Sa; expresar 𝒢_{jk} por el símbolo de paquete. Tomado: sí, ROUND_014_A.

### 16. ROUND_013_A.md — bloqueo de picos bajo el proceso B: Tipo I dual, dual completo = polinomio conjugado
- Objeto: D_w(s) = Σ Λ(n)n^{−s}w(n), w(x) = ρ(|log x|/T), P^ρ_T = 2Re D_w(½+iτ); Λ = μ∗log.
- Lema 1.1 (sobre 2πN(1+δ) cada suma Tipo I es su dual de Poisson con frecuencias j ≥ m(1+δ); término j = 0 es
  O(τ^{−K})): PROVED (segundo orden CITED); comprobación NUMERICAL 3.5 %.
- Prop 2.1 / (2.2) (P^ρ_T(τ) = 𝒜_w(½+iτ) + R_w(½+iτ) exacto vía Mellin y ecuación funcional de ζ′/ζ; dual = polinomio
  conjugado por paridad del perfil): PROVED. Lema 2.2 (𝒜_w = m(τ) + O(T^{−2}τ^{−2}); parte polar O(e^T(Tτ)^{−k})): PROVED.
- Lectura: (U) para un perfil ⟺ R_w(½+iτ) ≤ −κ + O(τ^{−2}) (reformulación); el bloqueo 0.355 = inf R_w.
- Prop 3.1 NO-GO (clase 𝒱: Vaughan/Heath-Brown/μ∗log + Poisson/proceso B de van der Corput para P^ρ_T en τ ≍ 2πN):
  estructura PROVED, tamaño ARGUED: o reproduce (U) literalmente o pierde más que el presupuesto ≈ 0.35/(2T).
- Positivos reutilizables: Lema 1.1, Prop 2.1, Lema 2.2.
- Paso siguiente: dejar los métodos de suma; calcular λ_max(A_τ) y buscar estructura de positividad de m(τ)I − A_τ como
  operador de celda. Tomado: el cálculo sí (ROUND_013_B); la estructura de positividad no.

### 17. ROUND_013_B.md — cálculo directo de λ_max(A_τ)
- Todo NUMERICAL; nada PROVED; herramienta reutilizable: elementos de matriz cerrados exactos de Sh(s) en la base de senos.
- Reportado: margen m − λ_max = 0.668, 0.311, −0.504, 0.273, 0.255, 0.114 en T = 0.8, 1.0, 1.5, 2.0, 2.5, 3.0 (Nb = 400);
  presupuesto cΛ: cruce en c ∈ (1.05, 1.10) en T = 2, (1.00, 1.05) en T = 3. Discretización nodal con interpolación
  descartada (diverge por aliasing).
- Corrección posterior (ROUND_015_C): los valores positivos en T ≥ 2 eran artefactos de truncación de base
  (Nb·π/2T < τ); con Nb = 800, T = 2 da −1.71.
- Paso siguiente: malla fina en T ∈ [1.2, 1.8]; falsificadores (b), (d) en T = 1.5. Tomado: la malla en T sí (ROUND_015_C,
  [1.40, 1.60]); los falsificadores no.

### 18. ROUND_014_A.md — Gram de cola ciega a la clase en el bloque alto; barrido en el eje de índices
- §1.0 (u_k = ε_kψ_k(λ)sin(2πλξ)/(πξ) + O(ξ^{−2}); el 𝒢 entrada por entrada no está definido en prolatos crudos; dominio
  S{f(λ) = 0}): PROVED.
- Thm 1.1 (M ⪰ 0 en 𝒜 ⟺ 𝒢 ⪰ 0 en S𝒜; mínimos generalizados con D y ℓ_g^S = Sℓ_gS): PROVED. Prop 1.2 (S𝒜 ≠ 𝒜; cosenos
  principales hasta 0.135): PROVED en forma, NUMERICAL en tamaño. Cor 1.3 (transferencia unilateral): PROVED.
- Thm 3.1 (cota de barrido Toeplitz/banda con error explícito): PROVED (álgebra lineal).
- Prop 3.2 NO-GO (clase: cotas inferiores por símbolo en el eje de índices prolatos + error de banda/Toeplitz en
  normalización D; NUMERICAL): fondo D en S𝒜 → 0 con K (0.98 → 0.015), dirección casi nula = gauge (ciega al peine),
  banda sin decaimiento (0.3–0.55 en desplazamientos 8–16), Gershgorin −5.7/−8.4. Las colas sobre el plunge son chirps,
  no paquetes (ARGUED).
- Falsificadores: colapso D y alineación gauge sobreviven 1.01Λ y a_3: no llevan aritmética.
- Positivos reutilizables: §1.0, Thm 1.1, Cor 1.3, Thm 3.1.
- Paso siguiente: cociente exacto por el gauge antes de barrer; probar si la banda de largo alcance es la corrección del
  radical; datos molificados. Tomado: sí, ROUND_015_A.

### 19. ROUND_015_A.md — bloque alto en el cociente gauge; Gram de cola molificada; libro de chirps del peine
- Lema 1.0 (dos formas que coinciden en codim r difieren en rango ≤ 2r): PROVED. Prop 1.1 (Gram de cola entrada por
  entrada en datos molificados; SM^ρS − 𝒢^ρ de rango ≤ 8, invisible en el subespacio compatible): PROVED dado (S), (T).
- Thm 3.1 (peine sobre colas de Poisson = 2⟨𝒯_log u, 𝒯u⟩, Λ ∗ 1 = log; = colapso de primos ya registrado): PROVED
  (usado, no reclamado). Obs. de dominio: obstrucción cruda = Σ log N/N = ∞: PROVED.
- Cor 3.2 (libro exacto: diagonal B_{NN} = (⟨m⟩_N − 2log N)‖F_N‖²; el peine es resonante, no se promedia): PROVED.
- Thm 3.3 (pares no resonantes por la desigualdad de Hilbert generalizada de Montgomery–Vaughan en el modelo de
  dilatación, constantes explícitas): PROVED. Cor 3.4 (criterio (C): ⟨m⟩_G − log X ≥ κ con barrido largo frente al número
  de chirps): PROVED en el modelo. §3.5 margen WKB ≈ 2T + 1/(p−1): ARGUED.
- Hipótesis FALSADA (NUMERICAL): «la banda de largo alcance de signo constante es la corrección finita del radical».
- NUMERICAL: fondo del cociente gauge no se estabiliza (2.64 → 1.63; 3.08 → 2.27); colapso más allá de K ≈ 0.3·Nb es
  artefacto; diagonal Ĝ_kk − m(k) casi independiente de k; núcleo de borde explica sólo la parte baja de la banda.
- Falsificadores: el criterio (C) sobrevive c < 1, a_P, (d) pequeño: no es paso de signo; el bloque alto rechaza c > 1
  sólo asintóticamente (k ≈ e^{290} para c = 1.01).
- Resto: transferencia del modelo de dilatación a colas truncadas (G_N depende de N); localización WKB; paso de perfiles
  únicos a combinaciones oscilantes de vecinos: OPEN. PIVOT.
- Positivos reutilizables: Lema 1.0, Prop 1.1, Thm 3.1, Cor 3.2, Thm 3.3, Cor 3.4.
- Paso siguiente: construir colas por la fórmula Legendre–Bessel esférica, matriz de chirps B_{NN′} del vector de fondo,
  separar diagonal / no resonante / salto en x = −T; versión por capas del Thm 3.3. Tomado: no.

### 20. ROUND_015_B.md — bloque bajo: qué deja la identidad de semirrecta, cancelaciones anidadas, dónde mueren los falsificadores
- §1.1 (la identidad deja la forma completa con el peine completo; sobre colas el peine colapsa a log N): PROVED
  (ensamblado). (1.2) entradas 𝒢_{jk} del bloque bajo: PROVED; caso f(λ) ≠ 0 como límite molificado: ARGUED.
- (1.3)–(1.4) forma principal Langer/WKB, κ₈ ≈ ½[D(N) + R_{88}]a_8²/‖Ef_*‖²: ARGUED. El fondo lleva f(λ) ≠ 0 (canal de
  borde a orden principal): ARGUED.
- §2.1: el bloque bajo no ve casi-coincidencias ni átomos log n > T; ve sumas divisorales de las primeras celdas y pares
  resonantes (1, n): estructura PROVED, tamaños ARGUED. §2.2 constante armónica (f(λ)²/(12λ))(2T + 0.430): ARGUED.
- §3.1 identidad (3.1) Π_T(Ef) = 𝒜_∞(Ef) + 2A(Ef)B(Ef) − 𝒲[Ψ_f] (primera cancelación O(1) → O(d_8)): PROVED.
- Lema 3.1 (𝔴_N(ω) ≥ 2T·H(ω) ≥ 2T; ≥ 2T + log 2 en la capa cáustica): PROVED.
- §3.3 primer término no cancelado positivo para T ≥ log 2: ARGUED. §3.4 ese término es positivo para todo c < 1 y
  c − 1 ≲ T, sobrevive a_P y (d) pequeño: PROVED (álgebra) → no es paso de signo.
- §3.5 el signo a orden d_8 lo decide la competencia de Schur «libro (+, robusto) menos acoplamiento 𝒲(Ψ_{f*}, ·)»
  (quita 33–40 %): NUMERICAL + ARGUED. §4.2 ley de dos umbrales en T = 1: c > 1 muere a primer orden (≈ 7·10⁻²²),
  c < 1 a segundo orden (≈ 1.5·10⁻⁴): NUMERICAL; falla en T = 1.2.
- PIVOT: no hay paso de signo en el bloque bajo solo.
- Positivos reutilizables: §1.1, (1.2), (3.1), Lema 3.1, §4.1 (bajo cΛ el defecto es (1−c)Π_T(Ef) en la ventana).
- Paso siguiente: aislar el acoplamiento 𝒲(Ψ_{f*}, ·) en T = 1 (partes arquimediana, peine colapsado, Tate) y buscar
  una identidad tipo (3.1) para el par (f_*, g) con falsificadores c = 1 ± 10⁻⁴, a_3. Tomado: no (fuera del rango).

### 21. ROUND_015_C.md — la violación en T = 1.5 de λ_max(A_τ) ≤ m(τ): real para el operador, artefacto para la forma
- Todo NUMERICAL; nada PROVED.
- Hallazgos: −0.504 real para el operador (≤ −0.511 en Nb = 1000), negativo en todo T ∈ [1.40, 1.60] y en T = 2.0
  (−1.71 con Nb = 800); los valores positivos de 013B en T ≥ 2 eran artefactos. El maximizador oscila a frecuencia τ
  (99.95 % de ‖f̂‖² sobre τ/2): fuera de la validez de la reducción a paquetes. W_T directo en la función proyectada:
  +0.79 (T = 1.5), +1.05 (T = 2.0). Restringido a envolventes con banda |ξ| ≤ τ/4: margen +0.46 a +0.72.
- NO-GO: la forma de operador sin restricción «λ_max(A_τ) ≤ m(τ)» de 012A Prop 3.1 es falsa y no es condición válida
  para (HR)(a). λ_A(1.5) a 30 dígitos: no resuelto.
- Paso siguiente: re-enunciar Prop 3.1 con restricción de banda |ξ| ≤ ητ, η < ½, y recalcular. Tomado: sí, ROUND_016_A.

### 22. ROUND_016_A.md — reducción a paquetes con banda restringida; márgenes de envolvente T = 1–3; λ_A(1.5) a 150 dígitos
- Objeto: V_η(τ) = span{e_k : a_k ≤ ητ}, A_τ^{(η)} = Π_ηA_τΠ_η; forma libre Q_T en L²[−T, T].
- Thm 1.1 (identidad exacta: Q_T(β cos τx) = ½[m(τ)‖β‖² − ⟨A_τβ, β⟩] + ½[D_τ + X_τ − R_τ]): PROVED.
- Lema 1.2 (ê_k cerrado; fuga |β̂(ξ)|² ≤ (8/π)η³τ³‖β‖²/(ξ² − η²τ²)²; L(η, θ)): PROVED. Lema 1.3 (i) m par y creciente:
  PROVED; (ii) Stirling: CITED + NUMERICAL; (iii) |m(s)| ≤ 5.38 + log(1+s): CITED + NUMERICAL.
- Prop 1.4 (curvatura D_τ ≥ −‖β‖²d(η, θ, τ)): PROVED dado 1.3(ii). Prop 1.5 (|X_τ| ≤ √(2L₁)(5.72 + log τ)‖β‖²,
  |R_τ| ≤ 2√L₁Σv_n‖β‖²): PROVED. Thm 1.6 (Q_T(f) ≥ ½‖β‖²[m(τ) − ⟨A_τ^{(η)}β, β⟩/‖β‖² − E]; condición (HB_η)
  λ_max(A_τ^{(η)}) ≤ m(τ) − κ − E): PROVED. Transferencia de Q_T a W_T en P_T: corrección de norma PROVED, de forma ARGUED.
- Falló: E no es pequeño (2√L₁Σv_n ≍ e^T; en T = 2, η = ⅛: E ≥ 1.55 contra margen 0.28): el Thm 1.6 no certifica (HB_η).
  Causa: Cauchy–Schwarz carga cada término del peine con toda la fuga de la capa de borde.
- NUMERICAL: margen con banda 0.888 / 0.544 / 0.280 / ≤ 0.256 / ≤ 0.114 (η = ⅛, T = 1, 1.5, 2, 2.5, 3), decreciente,
  extrapolación lineal cruza cero cerca de T ≈ 3.3 (advertencia, no resultado); c* → 1 (1.072 en T = 2, ≤ 1.022 en T = 3);
  W_T directo coincide a ≤ 0.002. λ_A(1.5): todos los valores de Galerkin positivos, ≤ 5.1·10⁻⁸³ (N = 160), no convergido.
- Resto: lema agudo de términos cruzados; rango completo en T = 2.5, 3, y T = 3.5: OPEN.
- Positivos reutilizables: Thm 1.1, Lema 1.2, Lema 1.3(i), Prop 1.4, Prop 1.5, Thm 1.6 (todo peine real; con pesos con
  signo, Σ|v_n|).
- Paso siguiente: (i) lema agudo de R_τ por integración por partes contra la fase 2τ, o clase β = χ·γ con corte suave;
  (ii) completar τ en T = 2.5, 3 y T = 3.5 con rutina sin matriz; (iii) λ_A(1.5) con N = 200–240. Tomado: fuera del rango.

---------------------------------------------------------------------------------------------------

## A. «No reintentar» deduplicado (con condición de reapertura) y cotejo con RULES_AVOID.md

Clave: [AUSENTE] no figura en RULES_AVOID.md; [INEXACTO] figura con enunciado que no coincide; [PRESENTE] figura bien.

A1. Mecanismos de signo basados sólo en identidades que también valen para a_3 o el sistema 3 → 3.2 (Λ∗1 = log,
    Selberg, factores de Euler, identidad de Lévy), en T ≥ ½log5 + 10⁻⁴ — NO-GO PROVED (007C). Reapertura: argumento que
    falle en a_3 y en 3 → 3.2. [PRESENTE en esencia: B1/§E; el certificado PROVED no se menciona.]
A2. Leyes simplemente exponenciales cT^a e^{−bT} para λ_A (007D) — NO-GO NUMERICAL. [PRESENTE vía B8 «ley en un rango
    acotado».]
A3. Mitad inferior de la ley bilateral λ_A ≥ L(T)(1 − o(1)): equivale a (N1′) μ₁ ≥ L con margen exp(−4πe^{2T}); no es más
    débil que (★); transferencia desde λ_W sólo da pisos 10⁵–10⁷ más débiles (007D). Reapertura: piso positivo para μ₁ con
    sensibilidad a perturbaciones relativas de tamaño L(T). [INEXACTO] RULES_AVOID §F: «Leyes bilaterales λ_A = L(T)(1+o(1))
    en rangos no acotados (P47 rem:bar-fam)» figura como terreno no excluido, sin advertir que su mitad inferior es (★) más
    un margen (007D Lema 4.6/Cor 4.7; 008E Conj 4.1).
A4. «λ_A ≥ λ_W − capacidad» como herramienta de transferencia — REFUTADA (007D Prop 4.2, modelo 2×2). [AUSENTE]
A5. Captura de signo sobre la familia de respuestas del peine E_T sola (Rayleigh en E_T) — PIVOT/NO-GO NUMERICAL (007E): falla
    por 13–31 órdenes. Reapertura: control del acoplamiento de Schur. [AUSENTE] (D17 cita «planos Λ-libres E_k», objeto distinto.)
A6. Truncación de Neumann de grado finito del acoplamiento de Schur (banda arquimediana B_t de 008A o familia E_T de 008D),
    con cola por radio espectral — NO-GO (008D): grado ∝ log(1/λ_A)/log(1/r); términos sin signo, truncaciones pares bajas
    con signo equivocado; Chebyshev sólo cambia la constante. Reapertura: resumación firmada de los términos k sobre V.
    [AUSENTE]
A7. Grönwall en la variable de ventana T (D ≤ Cλ, (EB_C), (VE_C)) — NO-GO como reformulación (008C Prop 5; clase 𝒦_H):
    con C sin especificar es (★) + Lipschitz, todo falsificador falla por su propio signo; con C = 8πe^{2T} es la mitad
    inferior de la ley. «No reintentar Grönwall con otro denominador». Reapertura: (EB_C) probado desde las trazas de borde
    θ_± con mecanismo propio. [INEXACTO] RULES_AVOID C1 sólo nombra «programa L♯ (forma exterior, Grönwall, …)» (variable
    de frecuencia); la versión en T, la identidad de constantes 8πe^{2T} = 2 en c y el Grönwall discreto no figuran.
A8. Mitad superior de la ley con una sola función de prueba PEψ_0 — NO-GO NUMERICAL (008E). [AUSENTE]
A9. Regla de selección clase–paridad (Poisson entrelaza ℱ con la reflexión R) como fuente de signo, y como prueba de
    pequeñez del acoplamiento H₊–H₋ — NO-GO (009B §3.1 Λ-libre; 012B Cor 1.2 PROVED: acoplamiento sin factor pequeño).
    [PARCIAL] C1 «Sonin, prolatos, semilocal como fuente de signo»; la imposibilidad de pequeñez por clase no figura.
A10. Lectura «decaimiento de α_HI por vectores casi-gauge» — RETIRADA (010A); par de 9B (P_+Π_TEψ_k contra D sin
    admisibilidad) inconsistente. [AUSENTE]
A11. Estimaciones del bloque alto que ven el peine sólo por su masa total (clase 𝒦_S, incluido lem:ext-hf) — NO-GO PROVED
    (010A Prop 3.2–3.3): negativas en toda frecuencia ≤ e^{S−C}; lem:ext-hf vacío en índices polinomiales. Reapertura:
    usar la dispersión de Λ sobre n < N (S₂, espaciado entero). [AUSENTE]
A12. Medida de valores grandes de P_T + incertidumbre Logvinenko–Sereda/Kovrijkine — NO-GO (011A Prop 2.2): colapsa a la
    cota puntual. [AUSENTE]
A13. Momentos de orden k con error por espaciado entero — NO-GO: no certifica bajo log τ ≈ (64/e)TN; modelo de toro ciego
    bajo 8T² (ARGUED) (011A). Reapertura: correlaciones aritméticas entre celdas (casi-coincidencias de productos k-ples).
    [PARCIAL] B2 «gran criba y media cuadrática»; el umbral y la condición de reapertura no figuran.
A14. Ensamblaje de Schur de dos bloques LM/HI y de tres bloques LM/H₊/H₋ (y corte por rango de índice) con normalización ℓ_g
    diagonal por bloques — NO-GO NUMERICAL (011B, 012B): θ → 0 mientras la forma sigue positiva. Reapertura: descomposición
    en la variable b = Sa cortada a lo largo del eje de índices con un acoplamiento controlado. [PRESENTE] D17 «ensamblajes
    de dos y tres bloques» (sin la variante por rango ni la condición).
A15. (HR)(a) como constante uniforme en K — no apoyado (011B: α_HI ≳ 3·4N/K). Reapertura: normalización dependiente de K.
    [AUSENTE]
A16. Cota trivial P^ρ_T ≤ Σ^ρ_T con perfil fijo; paquetes cortos de longitud o(T); valor medio + Sobolev/Gallagher para la
    cota puntual — tres NO-GOs (012A §4); todo método que pierda una constante multiplicativa queda excluido (presupuesto
    ≈ 0.35/(2T)). [PARCIAL] B2 cubre «media cuadrática»; 4.1 y 4.2 están ausentes.
A17. Heurística de valor extremo gaussiano para P^ρ_T — contradicha por los datos (012A §4.4; 011C §4(ii)). [AUSENTE]
A18. Clase 𝒱 (Vaughan/Heath-Brown/μ∗log + Poisson/proceso B) para P^ρ_T en τ ≍ 2πN — NO-GO (013A Prop 3.1): reproduce (U)
    o pierde más que el presupuesto; la constante vive en R_w. Indicado: «dejar los métodos de suma sobre el polinomio».
    [PRESENTE] D17 «proceso B / Vaughan» (sin la identidad (2.2) ni el alcance).
A19. Forma de operador sin restricción λ_max(A_τ) ≤ m(τ) − κ (sup sobre todo perfil L²) — FALSA (015C; violada en T = 1.4–1.6
    y 2.0) y no es condición válida para (HR)(a); los valores positivos de 013B en T ≥ 2 eran artefactos. Reapertura: sólo
    con banda de envolvente |ξ| ≤ ητ, η < ½ (016A). [AUSENTE]
A20. Cotas inferiores del bloque alto por símbolo en el eje de índices prolatos + error de banda/Toeplitz/Gershgorin en
    normalización D — NO-GO NUMERICAL (014A Prop 3.2). Reapertura: cociente exacto por el gauge y comparación con el promedio
    arquimediano a lo largo de chirps. [AUSENTE]
A21. Identificación «colas sobre el plunge = paquetes» (símbolo de paquete como símbolo del índice) — falla, son chirps
    (014A, ARGUED). [AUSENTE]
A22. Hipótesis «la banda de largo alcance de signo constante del Gram de cola es la corrección finita del radical/polar» —
    FALSADA (015A §1.3). [AUSENTE]
A23. «El bloque alto se controla por promedios del peine a lo largo de chirps» — CORREGIDA (015A): el peine no se promedia, se
    colapsa a los pesos resonantes log N; los valores medios sólo controlan el resto no resonante. [AUSENTE]
A24. Signo desde el bloque alto (cualquier forma) — excluido por la regla 4: todo falsificador se rechaza sólo en el bloque bajo
    y su acoplamiento (010A §5, 011B, 012B §3, 014A §4, 015A §4). [AUSENTE]
A25. Paso de signo en el bloque bajo solo (primer término no cancelado, segunda cancelación log² contra log²) — PIVOT (015B):
    positivo por razones robustas (sobrevive c < 1, a_P, (d) pequeño). Reapertura: desigualdad exacta en el peine sobre el
    acoplamiento 𝒲(Ψ_{f*}, ·). [AUSENTE]
A26. Premisa «la cola del bloque bajo ve los átomos log n > T / las casi-coincidencias» — falsa (015B §2.1). [AUSENTE]

Cotejo de un enunciado de RULES_AVOID.md con estos archivos:
- B2 dice: «Para T ≥ 1 el margen es ≤ 4·10⁹Te^{−15.449T}; toda cota con resto pierde más». [DESACTUALIZADO] 009A Cor 7.1
  prueba (dado thm:ext-half y una cota no asintótica citada) λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πe^{2T}} para N ≥ 1.6·10⁶, y 007D
  §2(iii) registra que la cota 15.449 es no informativa en todo el rango resuelto; el margen relevante es doblemente
  exponencial.
- B8 dice «determinante o momento del haz» y B2 «media cuadrática»; 011A §0(i) y 015A §0 precisan que valores medios y
  momentos son legítimos para la coercividad O(1) del bloque alto y para el resto no resonante, nunca para el signo. La
  frase de RULES_AVOID no distingue esos usos.

## B. Resultados positivos PROVED (enunciado y alcance)

B1. Lemas 1–3 de 007C: cota por testigo, invariancia por extensión por cero (todo peine), evaluación cerrada de la forma de
    Lévy en senos de Dirichlet; certificados λ_A ≤ −0.505 (a_3), −0.234 (3 → 3.2) en T ≥ ½log5 + 10⁻⁴, −0.078 (1.1Λ) en T ≥ 1.
B2. Sándwich λ_W^par ≤ λ_A^par ≤ λ_{W,2}^par; pisos λ_A ≥ 2^{−1518} (T ≤ ½log12), ≥ 2^{−2904} (T ≤ ½log15) con insumos citados
    (007D Prop 4.1, Cor 4.3).
B3. Forma secular exacta de la mitad inferior (Lema 4.6) y reducción a un autovalor no restringido μ₁ con momento de Tate
    τ₁ (Cor 4.7), sector par con n₋ = 1 (007D).
B4. Reducción de banda exacta (★)_T ⟺ S_T ⪰ 0 con banda espectral de Arch y t_c > π_+; serie de Neumann con grados
    homogéneos y cola bilateral (008A Thm 2.1, 3.1, Cor 3.2); válida para toda compresión de Galerkin.
B5. Fórmula de variación unilateral con multiplicadores de Tate y pliegue; 𝒱^♯ ≥ 0; desigualdad de franjas de borde
    (Prop 3, minimizadores acotados cerca de ±T); Grönwall discreto sobre incrementos (008C Thm 1, Cor 2.2, Prop 3, Prop 4);
    m′ ≥ 0 en [0, ∞) (Lema 1.2).
B6. a_CE = Arch_CE − Π_CE P_V (008D Prop 1); expansión de Neumann sobre E_T^c bajo (H₋) (Thm 2).
B7. Cota superior exterior W_T(Ef) ≤ Kλ^{−2}(L₁² + L₂²), K = 141, sobre 𝒜⁺_T; conteo de índices 5/3; identidad
    W^w_T(Ef) = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef]; robustez nula de la ley (008E Thm 3.1, Prop 3.3, (5.1), Prop 5.1; 009A §7.2).
B8. Lemas de prolatos 2.1–2.3, Lema 3.4′ (fuga ponderada ≤ C_dN⁹(1 − χ_{2d−2}), N ≥ 1.6·10⁶), y cota superior explícita
    λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πe^{2T}} (009A, dado thm:ext-half y cota no asintótica citada).
B9. Defecto de paridad exacto P_{−ε}Π_TEf = ½RΠ_TE(ℱf − εf); defecto de Fourier diagonal en prolatos; desacople de clases
    con términos cruzados ≲ poly(N)√(d_jd_k) (009B Thm 1.1, 1.2, 1.5, Lema 1.3, 1.6, Prop 2.2). Λ-libre.
B10. Forma simbólica en la ventana W_T(g) = (1/2π)∫(m − P_T)|ĝ|² + 2AB; Markov L²; lem:ext-hf vacío en grado polinomial;
    solapes prolatos cruzados ≡ 0 (010A).
B11. Necesidad de la cota puntual de paquete para toda (HR)(a) coerciva; vacuidad de P^ρ_T ≥ ϑm sobre Ω_B, log Ω_B =
    (64/(eϑ²))Te^{2T}(1+o(1)), y coercividad ≍ TN para datos sobre Ω_B; sup P^ρ_T ≥ c₁T para Ω ≥ N² (011A).
B12. Rango alto finito: (1.2)_κ vale para τ ≥ τ*_κ, log τ*_κ ≤ Σ₀ + κ + 2 (011C Lema 1.1, todo peine v_n ≥ 0).
B13. (1.2) en todo el rango alto para todo perfil si T ≤ log 2 (κ = 0.069) y para cos² si T ≤ 2.64 (κ = 0.0486, intervalos)
    (012A Thm 2.1, 2.2).
B14. Conjugación de signo M = S𝒢S con 𝒢 Gram de colas exteriores ciego a la clase; transferencia exacta al subespacio
    S𝒜; dominio S{f(λ) = 0}; lema de barrido Toeplitz/banda (012B Thm 1.1, Cor 1.2–1.3; 014A §1.0, Thm 1.1, Cor 1.3, Thm 3.1).
B15. P^ρ_T(τ) = 𝒜_w + R_w exacto con 𝒜_w = m(τ) + O(T^{−2}τ^{−2}); sumas Tipo I sobre el plunge son puramente duales (013A).
B16. Gram de cola entrada por entrada en datos molificados (corrección de rango ≤ 8); colapso del peine sobre colas de
    Poisson a log N; libro diagonal exacto (⟨m⟩_N − 2log N)‖F_N‖²; control Montgomery–Vaughan de pares no resonantes con
    constantes; criterio (C) en el modelo de dilatación (015A).
B17. Identidad (3.1) Π_T(Ef) = 𝒜_∞(Ef) + 2A(Ef)B(Ef) − 𝒲[Ψ_f] en datos admisibles; 𝔴_N ≥ 2T·H ≥ 2T (Lema 3.1);
    bajo cΛ el defecto es (1−c)Π_T(Ef) en la ventana (015B).
B18. Identidad exacta de paquete Q_T(β cos τx) = ½[m(τ)‖β‖² − ⟨A_τβ, β⟩] + ½[D_τ + X_τ − R_τ]; fuga de V_η;
    curvatura ≥ −η²/(2(1−θ²)) − …; reducción con banda (HB_η) (016A Thm 1.1, Lema 1.2, Prop 1.4–1.5, Thm 1.6; todo peine real).

## C. Obligaciones abiertas (enunciado matemático y lo intentado)

C1. (N1′) μ₁(T) ≥ L(T), L ≈ exp(−4πe^{2T}), μ₁ segundo autovalor par de a_T sin restricción, con τ₁² ≤ ηL·D(L). Intentado:
    sándwich con λ_W, clúster, capacidad polar (007D). OPEN.
C2. (EB_C): 𝔈_h(F*_{T+h}) ≤ C(T)hλ_A(T+h)(1 + o(1)), C(T) = 8πe^{2T}(1+o(1)), T ≥ ½log5. Intentado: Danskin, virial,
    Hellmann–Feynman (008C). OPEN; forma de Hadamard por trazas de borde ARGUED.
C3. Resumación firmada de la serie Σ_k W*X^kW en V_T, o cota de grado independiente de λ_A; (H₋): Arch_CC + Π_CC ≻ 0 en C
    (008D). OPEN.
C4. Conj 4.1 (008E): λ_A(T) ≥ κ₋(1 − χ_8(2πN)); vía prob:ext-L (Prop 4.2) o conditioning κ_C(T) polinomial (Lema 4.3). OPEN.
C5. (HR)(a)/(HR)(b) en el par consistente: inf_{HI} W_T/ℓ_g ≥ κ_H·(normalización, p. ej. 4N/K) y Γ′² ≤ (1−η)κ_LMα_HI.
    Intentado: Schur 2 y 3 bloques, rango, barrido en índice, cociente gauge (009B–015A). OPEN.
C6. (HR-Π): M|_{𝒜(Π_ε)} ≥ κ_Π·D_g|_{𝒜(Π_ε)} en el plunge (dimensión O(log N·log(1/ε))) (010A §3.4(iii)). Enunciado, no
    probado ni calculado.
C7. Cota puntual (1.2)/(U): P^ρ_T(τ) ≤ m(τ) − κ en 2πN(1+δ) ≤ τ ≤ τ*_κ uniformemente en T (con banda: (HB_η)). Intentado:
    cota trivial, valores grandes, Kovrijkine, momentos, MV+Sobolev, proceso B/Vaughan, operador sin banda (011A–016A).
    OPEN; certificado sólo T ≤ log 2 (todo perfil) y T ≤ 2.64 (cos²).
C8. Lema agudo de términos cruzados: |R_τ(β)| ≤ C(η)Σv_n/τ^{1/2} + (término de capa de borde pequeño) para β ∈ V_η, o una
    clase de envolventes con fuga o(1) (016A). OPEN.
C9. Transferencia de Thm 3.3 / criterio (C) del modelo de dilatación a colas truncadas (G_N = G1_{(−∞,−T−log N)}); localización
    WKB; paso a combinaciones oscilantes de vecinos que realizan el fondo en X (015A §3.6). OPEN.
C10. Acoplamiento del superviviente: sup_G |W_T(Ef_*, G)|²/(‖Ef_*‖²a_T(G)) acotado por (1 − η)·libro, mediante una
    identidad exacta en el peine del tipo (3.1) para pares (f_*, g) (015B §3.5). OPEN; es donde se rechazan c < 1 y donde
    debe actuar un paso de signo.
C11. Convergencia del límite molificado para f(λ) ≠ 0: cota uniforme de Σ_{N>X} log N⟨F_N, 𝒯u⟩ (015B §1.2). OPEN.
C12. Θ_T(w) < 0 certificado para a_3 y 3 → 3.2 por cubrimiento en μ (007C §3.2). OPEN, no intentado.
C13. Transferencia Q_T → W_T en P_T para β ∈ V_η a nivel de forma (016A). ARGUED.

## D. Objetos, pasos o ideas nombrados y no retomados

D1. Certificación de Θ_T(w) < 0 por dos testigos F_± (007C).
D2. Cota de μ₁ con sensibilidad Hellmann–Feynman dμ₁/dc = Π_T(e₁) y la prueba del signo de Π_T(e₁) − Arch(e₁) (007D).
D3. Medición de 𝔈_h/h con base que resuelva el borde ((log 1/(T∓t))^{−1/2} o pesos de Jacobi) y la ley λ_A ≍ θ²e^{−2T}/(8π)
    sobre dos números por ventana (008C).
D4. Resumación Chebyshev/minimax de 1/(1−x) en [−r_−, r_+] (008D).
D5. La §4 numérica de 008A (grado en v que rechaza 1.01Λ) no figura en el archivo leído.
D6. Bajar N₀ y b en el Lema 3.4′: sup|φ_k| ≤ C(k)c^{1/4} vía función de Sonin y escala de Airy; decaimiento 1/s exacto de Φ_a′ (009A).
D7. Medir κ_C y ‖Gram(h)‖ para hacer explícita (2.1) — medido en 010A pero la vía quedó sustituida por μ; la forma
    (HR-Π) del plunge nunca se calculó (010A).
D8. Gran criba para P^k sobre [Ω, 2Ω] que cuente casi-coincidencias de productos k-ples por energía multiplicativa (011A paso 2).
D9. Escaneo de T = 3 (ind) en [2·10⁶, 3.4·10⁸] (011C).
D10. Estructura de positividad de m(τ)I − A_τ como operador de celda (símbolo de Toeplitz de la cola del peine en
    frecuencias de Dirichlet) (013A).
D11. Falsificadores (b) a_P, (c) Beurling, (d) modificación finita en λ_max(A_τ) y en (HB_η) (013B, 016A).
D12. Construcción de colas por la fórmula Legendre–Bessel esférica, matriz de chirps B_{NN′} del vector de fondo, separación
    diagonal / no resonante / salto en x = −T; versión por capas del Thm 3.3 (015A).
D13. Aislar 𝒲(Ψ_{f*}, ·) en T = 1 por partes (arquimediana, peine colapsado, Tate) y buscar identidad tipo (3.1) por pares (015B).
D14. Validar la ley de dos umbrales de falsificadores fuera de T = 1 (falla en T = 1.2, causa no verificada) (015B).
D15. Rutina matricial libre para λ_max(A_τ^{(η)}) en T = 3.5 (K ≈ 2000) y decisión de cruce de margen cerca de T ≈ 3.3;
    λ_A(1.5) con N = 200–240 (016A).
D16. Medición de la cota de Lemma 1.3(iii)/(HB_η) con η dependiente de τ; envolventes β = χ·γ de corte suave (016A).

## E. Cobertura

Archivos en el rango ROUND_007_C.md … ROUND_016_A.md según `ls *.md | sort`: 22. Leídos completos: 22 (ROUND_007_C, 007_D,
007_E, 008_A, 008_C, 008_D, 008_E, 009_A, 009_B, 010_A, 011_A, 011_B, 011_C, 012_A, 012_B, 013_A, 013_B, 014_A, 015_A, 015_B,
015_C, 016_A). Ningún archivo ni tramo sin leer. Observación: ROUND_008_A.md termina en la Obs. 3.3 (127 líneas) sin §4
numérica ni secciones Result / Next step, aunque ROUND_008_D cita resultados numéricos suyos; lo leído es todo lo que contiene
el archivo. Se leyeron además, como referencia, RULES_AVOID.md, OBJECT_SPEC.md y STATEMENT_001.md.
