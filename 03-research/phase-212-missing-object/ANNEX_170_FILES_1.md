# Anexo 170 — archivos, tramo 1 (R170_000 a R170_822)

Lectura archivo por archivo de `03-research/phase-170-global-prime-inequality/`, desde R170_000 hasta
R170_822 inclusive (30 memos). La carpeta **no contiene README.md** (comprobado con `ls`). Cotejo
contra el terreno no excluido por la ronda 1 de la fase 212:
(T1) cuadrados continuos con la aritmética en el índice o en los pesos de la dilatación;
(T2) factorización tipo [log mcd(i,j)] = E diag(Λ) Eᵀ como modelo de Gram;
(T3) identificación total de Λ por Σ_{d|n}Λ(d) = log n convertida en cota cuadrática;
(T4) residuo común: convertir los apareamientos mixtos de la identidad finita de Poisson–Chebyshev
(H_{M,N}, E_N) en Σ_{k>N} h(k)|ℓ_k(F)|² con h ≥ 0.

Notación común de la fase 170: W_T(F) = (1/2π)∫m|F̂|² + 2Re(A(F)B̄(F)) − Σ_{2≤n<e^{2T}} (2Λ(n)/√n) Re c_F(log n),
m(τ) = Re ψ(1/4+iτ/2) − log π, A(F)=∫F e^{t/2}, B(F)=∫F e^{−t/2}; c(t)=cosh(t/2), s(t)=sinh(t/2);
m₀ = m(0) = −γ_E − π/2 − 3log2 − logπ < 0; k(u) = e^{−u/2}/(1−e^{−2u}). Varias memos usan el operador
de Poisson–Chebyshev (PC) de P47: S_N A_M 𝓕 = {X,E_N} − L_M*E_N − JH_{M,N} − H_{M,N}𝓕, con
H_{M,N} = Σ_{k>N} h_{M,N}(k) k^{−1/2} τ_{log k}, h_{M,N}(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) ≥ 0.

Observación general: el idioma de las memos es inglés; varias usan una equivalencia externa (R163_401
Thm 1.2; P45 Theorem F); se registra neutralmente y no se desarrolla.

---

## Archivos no .md de la carpeta (sin análisis)

- `archimedean_transfer_diagnostics.json` — salida numérica del cotejo del transporte arquimediano (R170_807/808).
- `coherent_paths_diagnostics.json` — diagnósticos Galerkin de la serie de caminos (R170_301).
- `contact_response_diagnostics.json` — diferencias centrales y contacto artificial (R170_401).
- `gamma_detector_bridge_diagnostics.json` — diagnóstico del detector de momentos Gamma (R170_702).
- `multiplicative_compensation_diagnostics.json` — chequeos de la compensación por modulación (R170_501).
- `nonlocal_storage_diagnostics.json` — chequeos de la ecuación de Stein / almacenamiento no local (R170_601).

No hay scripts `.py` en la carpeta: los `verify_*.py` citados por las memos (301, 401, 501, 601, 805, 807,
810, 812) no están presentes.

---

## 1. Entradas por archivo

### R170_000 — Global target and effective dependencies
- **Objeto.** Enunciado autocontenido de W_T(F) ≥ 0 sobre 𝒟_T = {F ∈ L²(−T,T): ∫log(2+|τ|)|F̂|² < ∞}; fuera
  de 𝒟_T el término arquimediano vale +∞. Lista dependencias: rango certificado T ≤ ½log5 (P47 thm:log5W,
  importado); «primer contacto» T_c como contacto con cero, no contraejemplo estricto; Theorem M (P48
  thm:M(b)) como cota superior asintótica de ínfimos normalizados, no como equivalencia; reducción
  «twisted» (R167_101 Thm B) condicionada a (Dom_θ), régimen pequeño y (WS*).
- **Etiquetas.** Declarada OPEN. Usa una equivalencia externa (R163_401 Thm 1.2). Sostenido: es un
  enunciado y un inventario; no hay demostración propia.
- **Se detiene.** No aporta signo ni extiende rango; la ruta por suma torcida sigue condicional.
- **Corregida por.** No indica.
- **T1–T4.** No toca ninguno (menciona Eratóstenes como identidad exacta sin signo, R169_101/190).

### R170_101 — Domain, real tests, and scale quantifier
- **Objeto.** (§1) Forma extendida bien definida: |c_F| ≤ ‖F‖², c_F(u)=0 para |u|≥2T, |2Re(AB̄)| ≤ 4 sinh T ‖F‖²,
  m(τ) − log(2+|τ|) acotada (DLMF 5.11.2). (§2) W_T(f+ig) = W_T(f)+W_T(g). (§3) W_S(F)=W_T(F) para S ≥ T;
  basta una sucesión T_j → ∞. (§4) Σ_{n≤Y}Λ(n)a(n) = Σ_{dm≤Y} μ(d) log m a(dm).
- **Etiquetas.** Declarada PROVED (elemental). Sostenido: sí, las cuatro piezas son correctas y elementales.
- **Se detiene.** §4: la inversión de Möbius no es suma de cuadrados; μ y la parte real de los pesos no tienen
  signo. Coincide con R169_101.
- **T1–T4.** Toca T3: sí, débilmente — escribe Λ = μ∗log como identidad exacta y registra que no da signo;
  no la convierte en cota cuadrática.

### R170_201 — Prime channel construction
- **Objeto.** En L²(ℝ), U_p traslación por log p, r_p = p^{−1/2}, V_p = Σ_{k≥1} log p · r_p^k U_p^k,
  C_p = 2ℓ_p r_p/(1−r_p), b_p = ℓ_p r_p(1+r_p)/(1−r_p), D_p = √b_p (I−U_p)(I−r_pU_p)^{−1}.
  Prop. 1: D_p*D_p = C_p I − (V_p+V_p*). Ensamblaje ⊕_p: ‖𝒟_P F‖² = C_P‖F‖² − 2Σ_p Σ_k (log p/p^{k/2}) Re c_F(k log p),
  y W_T = ‖𝒟_P F‖² + R_P(F), R_P = 𝔞_∞ + 2Re(AB̄) − C_P‖F‖². Teorema 2: la constante C_P es óptima
  (símbolo q_P(0)=C_P). Versión truncada (4): C_N^min‖F‖² − 2Re⟨V_N F,F⟩ = Σ_{n≤N} (Λ(n)/√n)‖F−U_nF‖².
  (5) R_P(F) → −∞ cuando P crece (Σ1/p diverge).
- **Etiquetas.** «Construcción y obstrucción probadas». Sostenido: sí. Teorema 2 cubre factorizaciones del
  mismo operador con compensación constante, no compensaciones dependientes de τ ni comprimidas.
- **Se detiene.** El resto R_P no tiene signo y diverge a −∞; la construcción funciona para cualesquiera
  dilataciones a_j > 1 y pesos ℓ_j > 0, luego no usa la factorización de ℤ (falsificador implícito: cualquier
  sistema de pesos positivos).
- **Corregida por.** No; R170_301 la reemplaza por el acoplamiento común.
- **T1–T4.** Toca T1: sí — cuadrados continuos ‖D_pF‖² con aritmética en el índice (canal por primo) y pesos
  log p·p^{−k/2} en la dilatación; falla por compensación diagonal C_P divergente y genericidad en los pesos.
  T2/T3/T4: no.

### R170_202 — Hidden network audit
- **Objeto.** Energías de red E(y) = Σ c_ij|y_i−y_j|² + Σκ_i|y_i|², c_ij, κ_i ≥ 0, con eliminación variacional de
  vértices ocultos. Propiedad heredada E_eff(|x|) ≤ E_eff(x) ⇔ E_eff(f,g) ≤ 0 para f,g ≥ 0 de soporte disjunto.
  Contraejemplo: núcleo h(u) = 2cosh(u/2) − e^{−u/2}/(1−e^{−2u}); h(log(3/2)) = (7/10)√(2/3) > 0; con dos
  bultos en (−1/2,1/2) se tiene W_{1/2}(f,g) > 0.
- **Etiquetas.** «Obstrucción de clase probada; precedente 106.13». Sostenido: sí (verifiqué h(u₀)).
- **Se detiene.** NO-GO de clase: ninguna red escalar con conductancias positivas (con vértices ocultos)
  representa W en coordenadas físicas preservando el módulo. No cubre canales matriciales con fases ni
  acoplamientos con signo.
- **T1–T4.** No (es representación tipo Dirichlet/Beurling–Deny, no aritmética en el índice).

### R170_301 — Coherent archimedean paths
- **Objeto.** Γ_T(F) = (1/2π)∫(m−m₀)|F̂|² = ∫₀^∞ k(u)‖F−S_uF‖² du (1); Γ_T ≥ α_T I, α_T = 2[artanh(e^{−T})+arctan(e^{−T})].
  E_T = Γ_T + 2A_T I − J_T + 2|c⟩⟨c|, C_T = b_T I + 2|s⟩⟨s|, b_T = 2A_T − m₀, con A_T = Σ a_n, a_n = Λ(n)/√n;
  ⟨E_TF,F⟩ = Γ_T + Σ a_n‖F−S_{log n}F‖² + 2|⟨F,c⟩|² (5); W_T = ⟨E_TF,F⟩ − ⟨C_TF,F⟩ (6).
  Teorema 1: ‖R_T‖ ≤ r_T = 2A_T/(2A_T+α_T) < 1 y serie de Neumann para E_T^{−1} (7)–(8). Teorema 2:
  W_T ≥ 0 ⇔ K_T = C_T^{1/2}E_T^{−1}C_T^{1/2} ≤ I ⇔ ‖𝒯_T‖ ≤ 1 (11). (12) K_T = Σ_j L_j*L_j,
  L_j = (I+R_T)^{1/2}R_T^jY_T, con cota de cola (13). Objetivo reescrito (14): Σ_j‖L_jx‖² ≤ ‖x‖².
- **Etiquetas.** «Construcción incondicional; signo OPEN». Sostenido: sí; (14) es reformulación exacta.
- **Se detiene.** La contracción (14) no se sigue de la construcción. Falsificador explícito: T=1,
  F = 1_{(−1,1)}/√2, a₂ = 100 da W < 5+16−100 = −79 (verifiqué c_F(log2) = 1−log2/2 y Γ₁(F) < 5); la serie converge
  igual. r_T → 1 cuando T crece: no hay margen uniforme.
- **T1–T4.** Toca T1: sí — (5) es suma de cuadrados continuos con pesos aritméticos Λ(n)/√n en las
  traslaciones; el signo queda en el término C_T restado. Falla porque la forma es «cuadrados − constante»
  y todo es genérico en los pesos (falsificador a₂ grande).

### R170_401 — Contact response and divisor coordinates
- **Objeto.** Derivada del autovalor generalizado C f = κ E f: κ̇ = 2(1−κ)s_d‖f‖² + κ⟨H_d f,f⟩ (2); en contacto
  κ̇ = 2Σ d_n Re c_f(log n) (4). Teorema 1 (tangencia de segundo orden): si PDP = 0 y QDP ≠ 0,
  W_ε(f+εg) = −ε²q − ε³⟨Dg,g⟩ (5), luego W−εD no es ≥ 0 para ε pequeño de ningún signo; Cor.: robustez
  bilateral ⇔ DP = 0 (6). §4 coordenadas de divisores: e_m = Σ_{d|m}λ_d − log m, λ_n − Λ(n) = Σ_{d|n}μ(n/d)e_d (7);
  respuesta (8)–(9) con Σ_k μ(k)k^{−1/2} H_{dk}.
- **Etiquetas.** «Identidades y criterio local probados; signo OPEN». Sostenido: sí (cálculo de Schur;
  §3 condicional a hipótesis de contacto). Datos numéricos (derivadas positivas, q ≈ 15.46) son NUMÉRICO.
- **Se detiene.** «Límite decisivo»: imponer e_m = 0 ∀m ≤ N determina λ = Λ unívocamente; una curva que
  preserva todas las identidades a T fijo es constante. (8)–(9) miden la respuesta a violar la identidad, no el
  signo en el punto exacto.
- **T1–T4.** Toca T3: sí — es exactamente la identificación total de Λ por Σ_{d|n}Λ(d) = log n, usada
  linealmente (perturbativamente); registra que no produce dirección no trivial ni cota cuadrática. T2: no
  (la matriz de Möbius aparece, pero no como Gram).

### R170_501 — Multiplicative compensation law
- **Objeto.** Torsión χ_θ(n) = n^{iθ}: (Λχ_θ)∗(1χ_θ) = (log)χ_θ (1). Covarianza W_θ(F) = W_T(e^{iθX}F) con expansión (2).
  H_θ = H + θV + θ²R + O(θ³), V = i[H,X], R = XHX − ½(HX²+X²H). Teorema 1: PRP = PVQH_Q^{−1}QVP (4).
  Fórmula física (5) de R. (6) σ(H_θ) = σ(H). Teorema 2: v medible unimodular con v(t+log p) = χ(p)v(t) ∀p ⇒
  v = e^{iφ}e^{iθt}, χ(p) = p^{iθ} (usa log2/log3 irracional).
- **Etiquetas.** «Leyes de covarianza y rigidez probadas; ley de positividad no». Sostenido: sí.
- **Se detiene.** NO-GO de clase: la modulación es conjugación unitaria; transporta el núcleo, no crea exceso
  positivo; (4) no usa (1) y vale para pesos artificiales con forma negativa. Rigidez: no hay fases locales
  independientes por primo.
- **T1–T4.** No toca T1–T4 directamente (usa la identidad de divisores sólo para transportarla, sin cota).

### R170_601 — Nonlocal storage attempt
- **Objeto.** Desigualdades (L): Z − RZR ≥ I + R, Y*ZY ≤ I. Teorema 1: toda Z así es Z = G + Σ_j R^jSR^j ≥ G,
  G = (I−R)^{−1} (ecuación de Stein); (2) la segunda condición es K + O_S ≤ I con O_S ≥ 0. Detector de Möbius:
  M_d = Σ_{k≤N/d} μ(k)(dk)^{−1/2}H_{dk}, A_d = B^{−1/2}M_dB^{−1/2}, S₀ = [A₂,A₃]*[A₂,A₃].
- **Etiquetas.** «Construcción y teorema de costo probados». Sostenido: sí. Los η elegidos usando el margen
  calculado son NUMÉRICO y circulares por declaración propia.
- **Se detiene.** NO-GO de clase: compensación no local positiva consume margen I−K, no lo crea; existencia de Z
  ⇔ K ≤ I. Falsificador a₂ = 100 de R170_301.
- **Corregida por.** R170_701/702: el detector de Möbius se sustituye por el detector Gamma fiel de P47.
- **T1–T4.** No (las M_d vienen de T3 vía R170_401, pero no hay cota cuadrática).

### R170_701 — Paper 47 comparison
- **Objeto.** Tabla de precedentes en P47 para 301–601; lista de faltantes (detector Gamma fiel, collares
  exteriores, términos polares completos, identidad entera orientada, minimalidad). Errores en el texto de P47:
  «(P) has no minimizer» contradice la prueba de O; «m ≥ 0» falso (m(0) < 0); actualizar a lem:contA; extensión
  existencial más allá de ½log5 ya derivable de thm:log5W + lem:contT.
- **Etiquetas.** Comparación estructural, sin etiqueta de teorema. Sostenido: sí como auditoría.
- **Se detiene.** Ninguna identidad 301–601 usa minimalidad ni la identidad entera orientada.
- **T1–T4.** Menciona T4 (sección PC con Λ∗1 = log y orientaciones) como pendiente; no lo recorre.

### R170_702 — Gamma detector and complete collars
- **Objeto.** Detector (𝓡F)_m = b_m∫e^{−a_m t}F, a_m = 2m+1/2, b_m = √a_m e^{−a_m(T+δ)}; HS e inyectivo (P47);
  cola HS exacta h_L. O_Γ = Σ_j Y*R^j 𝓡*𝓡 R^jY > 0 estrictamente. Identidad de collar completa:
  𝓡U_N = D_N𝓡 − 𝓔_N; para autovector de paridad definida, Q^W_{N,L}(F) = −2Σ_{m≤L}(d_{m,N}+λ)|(𝓡_LF)_m|².
- **Etiquetas.** «Consecuencias probadas». Sostenido: sí.
- **Se detiene.** Fidelidad ≠ cota coerciva: K + ηO_Γ ≤ I ya excluye el contacto (circular). La identidad no usa
  minimalidad; en λ = 0 da Q = −2c.
- **T1–T4.** Toca T4: parcialmente — es el balance de collares de la identidad finita (D_N, 𝓔_N), con la
  cancelación 𝓔_{N'} − 𝓔_N = (D_{N'}−D_N)𝓡; no convierte nada en Σ h(k)|ℓ_k|².

### R170_703 — Explicit extension past log5
- **Objeto.** Con T₀ = ½log5, L = 10^{24}, ε = (T₀/4)e^{−L}: W_T(F) ≥ ½·10^{−18}‖F‖² para 0 < T ≤ T₀+ε.
  Constantes explícitas: sup|τm'(τ)| < 10, pesos primos < 200, control Q(F) ≤ W_{T₀}(F) + 20; dilatación U_r unitaria.
- **Etiquetas.** «Teorema derivado del certificado de P47» = CONDITIONAL al certificado importado (no reejecutado);
  la deducción analítica está completa. Sostenido: sí, con esa dependencia.
- **Se detiene.** Ancho e^{−10^{24}}: no útil; iterar continuidad no excluye anchos sumables.
- **Nota.** Conflicto de notación: aquí L = 10^{24}, en el resto de la fase L = 2T o número de momentos.
- **T1–T4.** No.

### R170_704 — First contact dilation flux
- **Objeto.** 𝒥_h(F) = [W_T(F) − W_{(1−h)T}(U_{1−h}F)]/h ≤ 0 en contacto; identidad exacta con
  [m(τ)−m(τ/r)] ≤ 0, término primo y polar sin signo. Inversión Σ Λ(n)q_h(n) = Σ μ(d) log k q_h(dk).
- **Etiquetas.** «Identidad y restricción de signo probadas». Sostenido: sí; la restricción J_h ≤ 0 sólo usa W_T ≥ 0,
  no la minimalidad (lo dice).
- **Se detiene.** J_h > 0 sería equivalente a W_{(1−h)T}(U_{1−h}F) < 0: escribirlo no es probarlo; Möbius sin signo.
- **T1–T4.** Toca T3: sí, débilmente (Λ = μ∗log sobre q_h, sin cota).

### R170_801 — Three Gates audit (fuente externa)
- **Objeto.** Identidades de Schur reconstruidas para A = M_a − β|1⟩⟨1|: ∫g/a = δθ, débito D = δ|θ|²/J; identidad
  residual ⟨g,B^{−1}g⟩ = ⟨x₀,Bx₀⟩ + 2Re⟨x₀,r⟩ + ⟨r,B^{−1}r⟩.
- **Etiquetas.** Auditoría parcial; álgebra correcta (CITED+reconstruida). Ejemplo A_δ = δ muestra que no hay cota
  uniforme de respuesta al cerrarse el gap. El transporte del lema 8.4 queda sin verificar (ni probado ni
  refutado).
- **T1–T4.** No.

### R170_802 — Selection transfer (fuente externa)
- **Objeto.** Para S = Σ a_p(q)Z_p con fases Haar: E exp(t Re S) ≤ exp(t²V/4); con ley ν de entropía H relativa a
  Haar, E_ν Re S ≤ √(VH).
- **Etiquetas.** PROVED (elemental). Sostenido: sí.
- **Se detiene.** Una selección puntual es Dirac (entropía infinita); la independencia de log p no excluye
  resonancias puntuales.
- **T1–T4.** No.

### R170_803 — Boundary repair and exact response (fuente externa)
- **Objeto.** Contraejemplo K = diag(−1,1), R = (1,0): K + R*R ≥ 0 sin K ≥ 0. Ejemplo ℓ²⊕ℂ con A = diag(n^{−2}),
  b = (n^{−1}): reparación escalar con costo divergente (b ∉ Ran A^{1/2}). Identidad (E): S = C − X₀*BX₀ − X₀*R₀
  − R₀*X₀ − R₀*B^{−1}R₀; desigualdad objetivo (P); fórmula (F) del costo oculto |η|²/(Jδ).
- **Etiquetas.** Elementales, correctas. NO-GO de inferencia (reparación positiva no transporta signo).
- **T1–T4.** No.

### R170_804 — Literature transfer review
- **Objeto.** Resumen de 801–803, 805 y tabla de 27 trabajos externos con profundidad de lectura. Coste de
  selección vía operador de modulación: norma de entrada ~X^{1/2+1/p}; error de linealización |γ|H²/(2X²).
- **Etiquetas.** Revisión; sin teorema nuevo salvo cotas elementales. No hay auditoría completa (lo declara).
- **T1–T4.** No.

### R170_805 — Common complement capacity
- **Objeto.** En (0,1), r[u] = ¼∬(1/|x−y|−1)|u(x)−u(y)|² + ∫[−½log(x(1−x)) − log2]|u|². Para intervalos
  disjuntos de longitud ε: r[u] ≥ Σ_ν[log(1/(2ε)) − Δ_ν]‖f_{ν,0}‖², Δ_ν = ½Σ_{μ≠ν} d(D_{νμ}),
  d(D) = log(1+1/D) − 1/(D+1), Δ_ν ≤ 1−γ_E. Mínimo de l₀ = β‖u‖² − ½|∫u|² (β = log2+½) sobre complemento común:
  β‖f‖² − β/(2log2+ℓ)|∫_S f|².
- **Etiquetas.** Reconstrucción PROVED. Sostenido: sí; auditado y confirmado en R170_807.
- **T1–T4.** No.

### R170_806 — Archimedean transfer
- **Objeto.** Con L = 2T, f(x) = √L F(L(x−½)): A_T[F] = b[f] − a_L‖f‖² − ⟨H_Lf,f⟩, a_L = γ_E + log(2πL),
  h_L(v) = Lk(Lv) − 1/(2v), b[f] = ¼∬|f(x)−f(y)|²/|x−y| + ∫−½log(x(1−x))|f|² (1). Forma completa (2):
  W_T = b − a_L − H_L − J_L + 2|⟨f,c_L⟩|² − 2|⟨f,s_L⟩|². Reformulación (4): sup spec(b^{−1/2}K_Lb^{−1/2}) ≤ 1.
- **Etiquetas.** Sin etiqueta explícita; identidad PROVED (confirmada en 807/808). (4) es reformulación.
- **Se detiene.** El resto K_L no tiene signo en la métrica de b; descartar R_S sería ilegítimo.
- **T1–T4.** No.

### R170_807 — Transfer independent audit
- **Objeto.** Verificación de 805 y 806 (constantes, factor ½, K(v) = 1/(2sinh(v/2)) + 1/(2cosh(v/2)) = 2k(v)).
  Contraejemplo a la relajación: senos normalizados en un intervalo J ⊂ S^c de ancho < log2/L dan W_rel →
  β − a_L < 0 para L > e^{β−γ_E}/(2π) ≈ 0.2947.
- **Etiquetas.** Auditoría; PROVED (1)–(4) de su lista; NUMÉRICO los diagnósticos a 45 dígitos.
- **T1–T4.** No.

### R170_808 — Final transfer audit
- **Objeto.** Mismo transporte; enunciado (A): inf{W_rel[f] : f|_S = 0} = −∞ para L > L_*. Valor límite ≈ −1.69783 en
  L = log5.
- **Etiquetas.** PROVED (restricción de la construcción). Sostenido: sí.
- **Se detiene.** NO-GO para la relajación que descarta R_S.
- **T1–T4.** No.

### R170_809 — Sign construction with retained reserve
- **Objeto.** P proyección a indicadores de M celdas; b[y] ≥ λ_M‖y‖², λ_M = log M + γ_E − ½ (1); K_L ≤ κ_L I con
  κ_L explícito; M > exp(κ_L+g−γ_E+½) ⇒ B ≥ g_M I (2). Extensión armónica V = b^{−1}PD^{−1}, C = D^{−1} − V*K_LV,
  A = QK_LV: W[Vx+y] = ⟨x,Cx⟩ − 2Re⟨y,Ax⟩ + B[y] (3); W ≥ ⟨x,(C−A*A/g_M)x⟩ + g_M‖y−Ax/g_M‖² (4);
  exacto (5) C − A*B^{−1}A; pérdida (6) A*(g_M^{−1} − B^{−1})A ≥ 0.
- **Etiquetas.** «Desigualdad de formas probada a cada escala». Sostenido: sí.
- **Se detiene.** C − A*A/g_M ≥ 0 no probado para todo L; las cotas valen para muchos pesos alterados (no
  rompen falsificadores).
- **Corregida/auditada por.** R170_810.
- **T1–T4.** No.

### R170_810 — Sign audit
- **Objeto.** Valida (4) de 809. Contraejemplo 2×2: b = diag(1,3), K = [[½,1],[1,1]], W semidefinido con
  W(1,½) = 0; con g = 1, C − A²/g = −½ mientras C − A²/B = 0. Otro: K = diag(2,0) ⇒ W = diag(−1,3).
- **Etiquetas.** NO-GO de inferencia operatorial (reserva + coercividad no fuerzan signo).
- **T1–T4.** No.

### R170_811 — Uniform arithmetic law proposal (FIDC)
- **Objeto.** Flujo orientado de incidencia divisor–collar: 𝔉^ε = Re⟨{X,E_N}F − L_M*E_NF − JH_{M,N}F − H_{M,N}𝓕F,
  χ_εS_LF⟩ − Re⟨S_N r_F, 𝓕(χ_εS_LF)⟩ (1); N = ⌈e^{2T}⌉, M = N². Conjetura FIDC: (FIDC+) 𝔉 ≥ (1−q₀)‖R_LF‖²,
  q₀ = log2/4 + 1/16, y (FIDC−) 𝔉 ≤ 0 en primer contacto primitivo; juntas darían R_LF = 0 ⇒ F = 0.
  Reserva (6) R_L*(I−D_{N,L})R_L ≥ (1−q₀)R_L*R_L (citada de P47). Mecanismo §5: zona saturada k ≤ N cancelada por
  Σ_{d|k}Λ(d) = log k; frontera k > N con pesos Λ(d) ≥ 0.
- **Etiquetas.** Declarada propuesta / CONJECTURE (en el sentido de OPEN). Usa una equivalencia externa (§3,
  pasos 3–4). Sostenido: la propuesta tiene errores de definición (ver 812).
- **Se detiene.** Signo del flujo exterior sin derivar.
- **Corregida por.** R170_812 (adjunto erróneo S_N en lugar de S_N*; regularización χ_ε vacía) y R170_813.
- **T1–T4.** Toca T4: sí, de lleno — es el intento de dar signo a los apareamientos mixtos de PC (H_{M,N}, E_N,
  puerto Tate) usando h_{M,N}(k) ≥ 0; no se escribe como Σ h(k)|ℓ_k(F)|². Toca T3: sí (cancelación interior
  por Λ∗1 = log).

### R170_812 — FIDC audit
- **Objeto.** U = 𝓕: U* = U, U² = I, Uτ_a = τ_{−a}U, US_N* = S_NU, UA_M = A_MU (1). Flujo original
  = Re⟨A_MF − r, S_NUg⟩ + Re⟨r,(S_N−S_N*)Ug⟩ (4): el segundo término sobra. χ_εg = g exactamente (regularización
  inoperante). Contraejemplo A_± = [[0,±1],[±1,0]]: mismo bloque interior, flujo opuesto. h_{M,N} ≥ 0 no da signo
  de apareamientos oscilantes; ⟨JH_{M,N}F,g⟩ = 0 por soporte pero H_{M,N}UF no se anula.
- **Etiquetas.** Auditoría; correcciones PROVED; NO-GO de la inferencia «ecuación local ⇒ signo del flujo».
  §5 usa una equivalencia externa (P45 thm:sufficiency) para el puente primitivo.
- **T1–T4.** Toca T4: sí — registra que la positividad de h_{M,N}(k) no se transfiere a la forma.

### R170_813 — FIDC revised
- **Objeto.** Definición sin regularización en Q_log: g = S_LF, h = S_NUg, e_{M,F}(v) = a_M(F,v) − ⟨r,v⟩,
  Flux_corr = Re e_{M,F}(h) (A); e_{M,F}(v) = 0 para v soportado en I_T (B); expansión PC (C) con puerto
  Re⟨S_N*r,Ug⟩; diferencia (D) con la original. Fórmula exterior puntual de A_MF fuera de I_T para F liso.
  Obligaciones (P+) Flux ≥ (1−q₀)‖R_LF‖², (P−) Flux ≤ 0.
- **Etiquetas.** Definición e identidades PROVED; (P±) OPEN. Usa una equivalencia externa (P45 Theorem F) en §3.
- **T1–T4.** Toca T4: sí (objeto bien definido del residuo exterior; sin signo).

### R170_814 — Arithmetic Green proposal
- **Objeto.** ρ = 1 − 1/(2N²), h = 1−ρ; correctores p, q con bump η, C(p)=1, S(q)=1; G_ρF = D_ρF − C(D_ρF)p − S(D_ρF)q
  primitivo soportado en I_{ρT} (3); E_ρ(F) = a_{ρT}(G_ρF,G_ρF)/h ≥ 0 y hE_ρ = a_T(G_ρF−F, G_ρF−F) (5) [lema
  probado]. Φ(F) = Re[a_M(F,z) − ⟨r_F,z⟩], z = S_NUS_LF. Propuesta (G): (i) (1−q₀)‖R_LF‖² ≤ Φ, (ii) Φ + E_ρ ≤ 0.
  (6) Φ = Ω − Σ_{d≤M}Λ(d)ξ_d/√d; (7) = Σ_{km≤M}μ(k)log m ξ_{km}/√(km); intervalo requerido (8).
- **Etiquetas.** Lema PROVED (sólo usa a_T ≥ 0 en la ventana del contacto); (G) OPEN. Usa una equivalencia
  externa (P45 Theorem F) en §4.
- **Se detiene.** Escribir (7) no da (8): μ y ξ sin signo.
- **T1–T4.** Toca T3: sí — Λ = μ∗log insertada en el flujo, sin cota. Toca T4: sí (Φ es el residuo exterior PC).

### R170_815 — Green sign attempt
- **Objeto.** Identidad interior [a_T(F,F) − a_{ρT}(G_ρF,G_ρF)]/h = −E_ρ ≤ 0 (1); (G−) equivale a (7):
  Re e_{M,F}(S_N𝓕S_LF) ≤ −(1/h)a_T(G_ρF−F, G_ρF−F). ⟨JH_{M,N}F,S_LF⟩ = 0 (9a); sobrevive −Re⟨H_{M,N}𝓕F,S_LF⟩ (9b).
  Contraejemplo 3×3 A_c = [[0,0,c],[0,1,0],[c,0,0]]: datos interiores fijos, Φ + E = c + 1/h recorre ℝ.
  (13) Σ_{d≤M}(Λ(d)/√d)ξ_d ≥ Ω + E_ρ.
- **Etiquetas.** Identidades PROVED; NO-GO de la inferencia puramente variacional (semidefinición + radical +
  competidor interior). (G−) OPEN.
- **Corregida por.** R170_817 (retira el uso de P_Tz sin justificar; restringe el alcance del modelo 3×3).
- **T1–T4.** Toca T4: sí — aísla (9b), el término de cola H_{M,N}𝓕F, como el residuo sin signo. T3: sí (14).

### R170_816 — Divisor sign attempt
- **Objeto.** Φ = B − C, C = Re⟨H_{M,N}UF,g⟩ (3); H_{M,N} = Σ_{N<k≤MN} h_{M,N}(k)k^{−1/2}τ_{log k} (4); masa
  W_{M,N} = Σ h_{M,N}(k)/√k (5); |C| ≤ W_{M,N}‖F‖‖S_LF‖ (6); forma autoadjunta K_{M,N,L} = (UH*S_L + S_LHU)/2 con
  −W‖S_L‖ ≤ K ≤ W‖S_L‖ (7); requerido (8) B − ⟨F,KF⟩ ≥ (1−q₀)‖R_LF‖². Cota inferior de la masa (8a):
  W_{M,N} ≥ (log2/(2√2))√N (verificada). Falsificador de la inferencia «h(k) ≥ 0 ⇒ apareamiento ≥ 0» (bultos
  trasladados). Separación orientada del canal d=2 (14): la familia reflejada JF se cancela por soporte; quedan
  dos familias de Fourier (desplazamientos log(m/2) y log(2m) sobre UF) sin términos opuestos.
- **Etiquetas.** Identidades y cotas PROVED; negativo para (G)(i), que queda OPEN.
- **Se detiene.** Cola de Fourier H_{M,N}UF sólo con estimación bilateral, pérdida ~√N; el reindexado m ↦ 4m
  cambia pesos y rangos.
- **Auditada por.** R170_817.
- **T1–T4.** Toca T4: sí, es el intento más directo — la cola Σ_{k>N} h(k)k^{−1/2}τ_{log k} aplicada a UF no se
  convierte en suma de módulos al cuadrado; sólo cotas bilaterales. Toca T3: sí (§4, Eratóstenes/Λ = μ∗log no da
  signo).

### R170_817 — Round validation
- **Objeto.** Tabla de veredictos sobre 815–816; correcciones (P_Tz retirado; alcance del modelo 3×3 y de los
  ejemplos de correlación negativa restringido; cota de norma no llamada «estimación aritmética nueva»).
  Confirma la estructura de desplazamientos del canal d=2.
- **Etiquetas.** Auditoría. Sostenido: sí.
- **T1–T4.** Toca T4: sí (confirma que la cola no se cancela término a término; no excluye cancelación más profunda).

### R170_818 — Puzzle map
- **Objeto.** Mapa: rutas directa (debito exacto A*B^{−1}A) y de flujo (dos huecos: reserva ≤ Φ, Φ ≤ −E_ρ).
  Tabla de piezas y prioridades 1–4 (compatibilidad exterior–interior; comparación conjunta Poisson–Tate/cola;
  transporte; uniformidad). Criterio de pieza discriminante (rompe falsificadores).
- **Etiquetas.** Síntesis; sin teorema. Usa una equivalencia externa (P47 + P45 Theorem F en el diagrama).
- **T1–T4.** Toca T4 como objetivo (prioridad 2), no lo recorre.

### R170_819 — Exterior–interior connection
- **Objeto.** 𝒬_{M,r}(v) = a_M(v,v) − 2Re⟨r,v⟩; 2Φ = 𝒬(F+z) − 𝒬(F) − a_M(z,z) (4); hE_ρ = 𝒬(G) − 𝒬(F) = a_M(δ,δ) (5);
  𝓡F = δ − hz (6); puente (8): Φ + E_ρ = Re e_G(z) + h^{−1}Re a_M(δ, 𝓡F). Conmutación de escala A_MD_ρ = D_ρA_M^{(ρ)}
  (9b), defecto (9d), descomposición (9e) de e_G(z) en cuatro piezas. Expansión PC (10), cancelación (11), collar
  (12), segundo resto (13). Obligación (16).
- **Etiquetas.** Identidades (4), (5), (8), (9e) PROVED (validadas en 822). (16) OPEN.
- **Error.** El texto alrededor de (9e) y §5 sugiere que hay que reconciliar una transformación de escala que
  rompería la hipérbola; R170_820 y R170_822 corrigen que la dilatación no destruye la multiplicación de divisores.
  (También hay un fragmento de prosa mal colocado: «where the defect is…» tras (9c').)
- **T1–T4.** Toca T4: sí (12) es el collar residual sin signo. T1: no.

### R170_820 — Joint arithmetic comparison
- **Objeto.** Conjugación completa O^{(ρ)} = D_ρ*OD_ρ: X ↦ ρX, τ_a ↦ τ_{a/ρ}, 𝓕 ↦ 𝓕_ρ; (PC_ρ) exacta; H^{(ρ)}_{M,N} con
  los mismos h_{M,N}(k) (6); resta exacta (7); ΔH = Σ h(k)k^{−1/2}(τ_{log k/ρ} − τ_{log k}) (8); corrector Tate (9).
  Dicotomía: conjugar todos los datos da tautología escalar; fijar datos deja resto no controlado. Multiplicador
  cos((log k)ξ/ρ) − cos((log k)ξ) sin signo (11).
- **Etiquetas.** Identidades PROVED («nueva sólo en contabilidad»). Sin desigualdad unilateral.
- **T1–T4.** Toca T4: sí — la cola reaparece a dos escalas con mismos h ≥ 0 y multiplicadores oscilantes; no hay
  conversión a Σ h|ℓ_k|². T3: la cancelación interior se conserva (sin signo nuevo).

### R170_821 — Uniformity of scale remainders
- **Objeto.** ‖τ_b − τ_a‖ = 2 para a ≠ b en L² y Q_log (5); convergencia fuerte (6), tasa con Df ∈ Q_log (7);
  ‖m(D/ρ) − m(D)‖ ≤ (8/7)C_m h, C_m = sup|xm'(x)| (12); cotas de correctores (15)–(16); módulo ω_T por radical (17)
  sin uniformidad en T (18).
- **Etiquetas.** PROVED (tamaño/topología). Sostenido: sí (822 advierte no extrapolar la norma 2 a sumas ni la
  continuidad fuerte de D_ρ a falta de continuidad en norma de 𝓕_ρ).
- **T1–T4.** Toca T4: sí, indirectamente (cota bilateral (9) de ΔH sin factor h).

### R170_822 — Sequential round audit
- **Objeto.** Valida 819 (4),(5),(8),(9e); corrige la lectura de pérdida de factorización bajo escala; valida (PC_ρ)
  y (7) de 820; corrige que e_F anula todo test admisible soportado en la ventana (no sólo primitivos); valida
  ‖τ_{a/ρ} − τ_a‖ = 2 y la cota O(h) de Gamma; prohíbe extrapolaciones.
- **Etiquetas.** Auditoría. Sostenido: sí.
- **T1–T4.** Toca T4: confirma que la ronda no obtuvo la desigualdad unilateral.

---

## 2. Síntesis

### (a) Piezas PROVED reutilizables
1. Dominio, reducción a tests reales y a sucesión de ventanas — R170_101 §§1–3.
2. Raíz explícita por torre prima D_p*D_p = C_pI − (V_p+V_p*) y versión truncada (4) Σ(Λ(n)/√n)‖F−U_nF‖² —
   R170_201 §§2–4; optimalidad de la constante (Teorema 2).
3. Representación de Lévy Γ_T = ∫k(u)‖F−S_uF‖²du, coercividad α_T, descomposición W = E_T − C_T, serie de
   caminos con cola (8), (13), criterio K_T ≤ I — R170_301 §§2–5.
4. Fórmula de respuesta κ̇ y tangencia de segundo orden / robustez bilateral ⇔ DP = 0 — R170_401 §§2–3;
   coordenadas de error de divisores (7) — §4.
5. Teorema de rigidez de fases locales (v = e^{iφ}e^{iθt}) y compensación PRP = PVQH_Q^{−1}QVP — R170_501 §§3,5.
6. Teorema de costo mínimo de la ecuación de Stein Z = G + ΣR^jSR^j — R170_601 §2.
7. Cola HS exacta del detector Gamma e identidad de collar completa Q^W = −2Σ(d_{m,N}+λ)|(𝓡_LF)_m|² — R170_702.
8. Extensión explícita a T₀ + (T₀/4)e^{−10^{24}} (condicional al certificado de P47) y constantes sup|τm'| < 10 —
   R170_703.
9. Cota de entropía E_ν Re S ≤ √(VH) — R170_802.
10. Identidades (E), (F) de respuesta con residuo — R170_803 §§3–4.
11. Capacidad con complemento común Δ_ν ≤ 1−γ_E y mínimo de l₀ — R170_805, auditado R170_807 §1.
12. Transporte exacto W_T = b − a_LI − H_L − J_L + 2|c_L⟩⟨c_L| − 2|s_L⟩⟨s_L| — R170_806 (2), R170_807 §§3–4, R170_808.
13. Extensión armónica con reserva retenida, desigualdad (4) y pérdida exacta (6) — R170_809 §§1–3.
14. Adjunto correcto del puerto Tate y flujo Φ bien definido en Q_log — R170_812 §1, R170_813 §§1–2.
15. Contracción primitiva G_ρ y E_ρ = a_T(G_ρF−F)/h ≥ 0 — R170_814 §3, R170_815 §2.
16. Separación Φ = B − C, ⟨JH_{M,N}F,S_LF⟩ = 0, masa W_{M,N} ≥ (log2/(2√2))√N, descomposición orientada del canal
    d=2 (14) — R170_816 §§2–3,6.
17. Puente Φ + E_ρ = Re e_G(z) + h^{−1}Re a_M(δ, δ−hz) y descomposición de escala (9e) — R170_819.
18. PC conjugada (PC_ρ), invariancia de h_{M,N} bajo dilatación, resta (7) — R170_820.
19. ‖τ_{a/ρ}−τ_a‖ = 2; ‖m(D/ρ)−m(D)‖ ≤ (8/7)C_m h — R170_821 §§2–3.

### (b) Cierres (NO-GO de clase o de inferencia) con falsificador
- Canales ortogonales por primo con compensación constante: C_P mínimo y R_P → −∞; genérico en dilataciones y pesos
  — R170_201 (sin falsificador nominal, la prueba vale para todo sistema a_j>1, ℓ_j>0).
- Redes escalares con conductancias ≥ 0 y vértices ocultos: falsificador h(log(3/2)) = (7/10)√(2/3) > 0 en T = ½ —
  R170_202.
- Acoplamiento coherente + convergencia ⇏ contracción: falsificador a₂ = 100, T = 1, F = 1_{(−1,1)}/√2, W < −79 —
  R170_301 §6.
- Cancelación escalar de primera variación en contacto no basta: Teorema 1 de R170_401.
- Modulaciones multiplicativas locales sólo transportan el núcleo; fases locales por primo rígidas — R170_501.
- Compensación no local positiva no crea margen; falsificador a₂ = 100 — R170_601.
- Fidelidad del detector ≠ cota coerciva — R170_702 §2.
- Reparación positiva K + R*DR ≥ 0 no transporta signo; falsificador diag(−1,1) y ejemplo de costo divergente —
  R170_803.
- Relajación que descarta R_S: ínfimo −∞ para L > 0.2947 — R170_807 §5, R170_808 (A).
- Reserva + gap del complemento no fuerzan signo: falsificador 2×2 b = diag(1,3), K = [[½,1],[1,1]] — R170_810.
- Ecuación local ⇒ signo del flujo: falsificador A_± — R170_812 §3.
- Semidefinición + radical + competidor interior ⇒ (G−): falsificador 3×3 A_c — R170_815 §4.
- h(k) ≥ 0 (o Λ(d) ≥ 0) ⇒ apareamiento ≥ 0: falsificador bultos trasladados — R170_812 §4, R170_816 §4.
- Uniformidad en norma de diferencias de traslación: norma exacta 2 — R170_821 §2.

### (c) Abierto explícitamente, con obstáculo exacto
- (14) de R170_301: Σ_j‖L_{j,T}x‖² ≤ ‖x‖² ∀T — no usa ninguna identidad exclusiva de ℤ.
- (4) de R170_806: sup spec(b^{−1/2}K_Lb^{−1/2}) ≤ 1, con R_S retenido en la métrica inversa.
- C − A*B^{−1}A ≥ 0 (o C − A*A/g_M ≥ 0) para todo L — R170_809 §3; la pérdida (6) puede comerse el margen nulo.
- (P+) Flux_corr ≥ (1−q₀)‖R_LF‖² y (P−) Flux_corr ≤ 0 — R170_813 §3; equivalentes a (G)(i),(ii) de R170_814.
- (8) de R170_816: B − ⟨F,K_{M,N,L}F⟩ ≥ (1−q₀)‖R_LF‖²; obstáculo: cola H_{M,N}UF sólo bilateral, masa ~√N; canal d=2 deja
  dos familias de Fourier log(m/2), log(2m) sin pares opuestos.
- (13) de R170_815: Σ(Λ(d)/√d)ξ_d ≥ Ω + E_ρ; μ y ξ cambian de signo.
- (16) de R170_819 / (12) de R170_820 / (19) de R170_821: Re e_G(z) + h^{−1}Re a_M(δ,𝓡F) ≤ 0; obstáculo: ninguna identidad
  correlaciona ΔE, ΔH, Δ𝓕, Δ_Tate y el error de alineación δ − hz en el radical del primer contacto; los restos no
  tienen orientación y no hay uniformidad en T.
- Ley de signo de primer orden en coordenadas de divisores — R170_401 §6 (la curva que preserva e_m = 0 es constante).
- Transporte del lema 8.4 de la fuente externa — R170_801 (ni probado ni refutado).
- Uso de la entropía de selección — R170_802 (falta una ley de fases con entropía controlada).

### (d) Lo que en este tramo ya recorre T1–T4 y por qué falló
- **T1** (cuadrados continuos con aritmética en índice/pesos de la dilatación):
  R170_201 (‖D_pF‖² por primo, pesos log p·p^{−k/2}; Σ(Λ(n)/√n)‖F−U_nF‖²) — falla: la expresión es «cuadrados − C_P‖F‖²»,
  C_P diverge, R_P → −∞, y la identidad es genérica en cualesquiera dilataciones/pesos positivos (no ve ℤ).
  R170_301 (5) — misma estructura con Γ_T y polo; la contracción K_T ≤ I no se sigue; falsificador a₂ = 100.
  Ninguno de los dos pone la no linealidad en V_T de modo que se rompa para cΛ: ambos son lineales en los pesos.
- **T2** (Gram por incidencia de divisores [log mcd] = E diag(Λ) Eᵀ): **no aparece** en este tramo. Lo más cercano es la
  matriz de Möbius de R170_401 §4 y los M_d de R170_601, usados como respuestas lineales, no como modelo de Gram.
- **T3** (identificación total por Σ_{d|n}Λ(d) = log n → cota cuadrática):
  R170_101 §4, R170_704, R170_814 §5 (7)–(8), R170_815 (14), R170_816 §4 — la inversión Λ = μ∗log es exacta pero deja μ y las
  correlaciones con signo libre; no se convierte en cota. R170_401 §4 — formulación más nítida: e_m = 0 ∀m ≤ N determina
  λ = Λ; la identificación es rígida (curva constante), así que no hay dirección para propagar el signo y la respuesta
  (8)–(9) sólo mide violaciones. R170_811 §5 — usa la identidad para cancelar la zona saturada k ≤ N de PC; deja sólo la cola.
- **T4** (residuo común):
  R170_811 (FIDC, conjetura), R170_812 (adjunto corregido; h ≥ 0 no da signo), R170_813 (Flux_corr bien definido),
  R170_814–815 (Φ como residuo exterior; (9a) ⟨JH_{M,N}F,S_LF⟩ = 0 pero (9b) −Re⟨H_{M,N}𝓕F,S_LF⟩ sobrevive),
  R170_816 (intento directo: C = Re⟨H_{M,N}UF,g⟩ = ⟨F,K_{M,N,L}F⟩ con K autoadjunta sólo acotada bilateralmente;
  masa ≥ c√N; canal d=2 con dos familias de Fourier sin cancelación término a término), R170_819–821 (el collar
  sobrevive a dos escalas con los mismos h_{M,N}(k) y multiplicadores cos((log k)ξ/ρ) − cos((log k)ξ) sin signo).
  Razón registrada del fracaso: los apareamientos de la cola actúan sobre UF = 𝓕F, que no está soportado en la
  ventana; h_{M,N}(k) ≥ 0 no fija el signo de un apareamiento oscilante entre funciones distintas (F y S_LF, no un
  cuadrado |ℓ_k(F)|²); y la reindexación que alinearía escalas cambia pesos y rangos. Ninguna memo de este tramo
  escribe la cola como Σ_{k>N} h(k)|ℓ_k(F)|²: lo que falta es exactamente que el par (F, S_LF) se vuelva un par
  diagonal (ℓ_k(F), ℓ_k(F)).

### (e) Inconsistencias o errores entre memos
1. R170_811: adjunto erróneo del puerto Tate (S_N en lugar de S_N*) y regularización χ_ε vacía — corregidos por
   R170_812 y R170_813.
2. R170_815 usa P_Tz sin justificar que el indicador preserve Q_log — retirado en R170_817.
3. R170_819 sugiere que escalar log d ↦ log d/ρ rompe la hipérbola — corregido por R170_820 §2 y R170_822 (la
   multiplicación de divisores se conserva).
4. R170_819 §1 enuncia la ecuación débil sólo para tests primitivos; R170_822 corrige que e_F anula todo test admisible
   soportado en la ventana.
5. R170_701 señala errores en el texto de P47 (minimizador de (P); «m ≥ 0»; referencia a lem:contA; extensión existencial
   pasado ½log5).
6. R170_812 §5 advierte que la referencia «(11.3)» de P47 es ambigua (etiqueta de ecuación).
7. Convenciones de núcleo: k (R170_301, 806) vs K = 2k (R170_807, 808); consistentes una vez explicitadas (comprobado).
8. Notación: L = 10^{24} en R170_703 frente a L = 2T (806–809) y L = número de momentos (702, 811–816).
9. R170_819 tiene un fragmento de prosa desplazado («where the defect is…») tras (9c').
10. R170_000, 811, 812, 813, 814, 818 usan una equivalencia externa (R163_401 Thm 1.2; P45 Theorem F); se registra sin
    desarrollarla.

### (f) Archivos leídos (lectura completa con Read)
README.md: no existe en la carpeta. Leídos enteros: R170_000, R170_101, R170_201, R170_202, R170_301, R170_401,
R170_501, R170_601, R170_701, R170_702, R170_703, R170_704, R170_801, R170_802, R170_803, R170_804, R170_805,
R170_806, R170_807, R170_808, R170_809, R170_810, R170_811, R170_812, R170_813, R170_814, R170_815, R170_816,
R170_817, R170_818, R170_819, R170_820, R170_821, R170_822 (34 archivos .md). Archivos no .md: seis JSON, listados
arriba sin análisis.
