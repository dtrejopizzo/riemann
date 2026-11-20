# Anexo 170 — tramo 4: archivos R170_863 a R170_900

Registro de lectura de los 38 archivos del tramo, en orden. Notación de cada memo. Las etiquetas
se citan como «declarada»; cuando la demostración leída no las sostiene se indica aparte. Cotejo
con el terreno no excluido de la ronda 1 de la fase 212:

- T1: cuadrados continuos con la aritmética en el índice o en los pesos de la dilatación;
- T2: factorización explícita tipo [log mcd(i,j)] = E diag(Λ) Eᵀ (incidencia de divisores) como modelo de Gram;
- T3: identificación total de Λ por Σ_{d|n}Λ(d) = log n convertida en cota cuadrática;
- T4: convertir los apareamientos mixtos de la identidad finita de Poisson–Chebyshev (H_{M,N}, E_N) en Σ_{k>N} h(k)|ℓ_k(F)|² con h ≥ 0.

Marco común del tramo. Todas las memos trabajan dentro del programa «primer contacto» de la fase 170:
un vector F en el radical ker H_T (o Z_T) de la forma primitiva en el umbral, la identidad PC
(Poisson–Chebyshev) renormalizada de R170_856, el puerto Tate (b, h = (PS_N^*P)^{-1}b, q = QS_N^*h,
z = QAF − ρq, ρ_F con PA_MF = ρ_F b) y la «ley exterior» buscada β_phys(F) = 𝔚_K(F) + Θ_ext(F) = 0
(etiquetas VIR–LB / D siempre OPEN). Ninguna memo del tramo escribe una identidad de la forma
a_T(F) = ‖V_T F‖² + ρ_T(F). Varias memos reflejan una lectura que usa una equivalencia externa
sólo en su encabezado de estado («VIR–LB / D OPEN»); no la desarrollan.

---

## 1. Entradas por archivo

### R170_863 — Null anchor of divisor incidence
- **Objeto.** Complejo de incidencia finito, M ≥ N: caminos 𝒫^{int}_{M,N} = {(d,m): dm ≤ N};
  C₁ = ℝ^{𝒫} ⊕ ℝ^{N}, C₀ = ℝ^{N}; borde (∂(x,y))_k = Σ_{dm=k} x_{d,m} − y_k (1.3);
  Laplaciano Δ_{M,N} = ∂^*∂ ⪰ 0 (1.4). Ancla x^Λ_{d,m} = Λ(d)/√(dm), y_k = log k/√k (2.1);
  ∂e_Λ = 0 por Σ_{d|k}Λ(d) = log k (2.2–2.3). Rigidez: con y = log fijo, e_a ∈ ker ⇔ a∗1 = log ⇔ a = Λ en [1,N] (3.2–3.3).
  Versión operador x_{d,m}(F) = Λ(d)/√(dm) τ_{log dm}F (4.1); deformación a dos escalas (5.1)
  con chorro antidiagonal ∂_−(∂e_Λ(r,q;F))|_{1,1} = (𝒜^{raw} − K_−)_{≤N}F (5.4).
  Energía E(r,q;F) = ‖∂e_Λ(r,q;F)‖²: E = 0, ∂_−E = 0, ∂_−²E = 2‖(𝒜^{raw} − K_−)_{≤N}F‖² (6.2–6.3).
- **Afirmaciones.** Complejo, Δ ⪰ 0, e_Λ en el núcleo, rigidez, versión operador, chorro normal,
  «la energía sólo ve el cuadrado del chorro»: PROVED (declarado; sostenido como identidades).
  La afirmación §0 de que la nulidad es «realización como vector nulo de una forma positiva» con
  selectividad F3: declarada en el cuerpo, rebajada por la propia cabecera (auditoría R170_865).
  Mapa de Green de la celda hiperbólica aislada (7.3): INADMISSIBLE; del complejo pegado: OPEN.
- **Detención.** La forma positiva Δ pierde la orientación del chorro de primer orden (sólo
  aparece al orden dos como cuadrado); el Dirac de incidencia (6.4) conserva orientación pero es
  indefinido. Falta un mapa de Green 𝔊_T con 𝔊_T((𝒜^{raw} − K_−)f) = 𝔚_K(f) + Θ_ext(f) (7.3).
- **Corregida por.** R170_864 (pegado Poisson: el chorro K_− se cancela) y R170_865 (∂ = [B, −I]
  sobreyectivo: el núcleo es el grafo universal y = Bx; la rigidez proviene de fijar y = log desde fuera).
- **Cotejo.** T2: sí, directamente — es un modelo de Gram por incidencia de divisores (B suma rutas
  (d,m) sobre dm = k); su forma positiva es ∂^*∂, ciega a los pesos. T3: sí — la nulidad codifica
  Σ_{d|k}Λ(d) = log k, y ∂_−²E es un cuadrado; pero el cuadrado es ‖(𝒜^{raw}−K_−)F‖², de segundo
  orden, sin relación con a_T. T1: parcial (traslaciones τ_{log d/r + log m/q} con pesos Λ), sin
  cuadrado útil. T4: no.

### R170_864 — Glued incidence–Poisson complex
- **Objeto.** Celda hiperbólica H(r,q) = L(r)S(q) − K(r,q), normal H_− = 𝒜^{raw} − K_−; normal PC
  orientada 𝒩_H = −H_−; celda Poisson–X con jet 𝒩_X = −K_− (de {X_r,E}𝓕_r = S𝓜_r − K − JK𝓕_r, (1.3)).
  Pegado: 𝒩_X + 𝒩_H = −𝒜^{raw} (0.4), y reflejado −JK_−𝓕 − JH_−𝓕 = −J𝒜^{raw}𝓕 (0.5).
  Normal PC completa 𝒩_{PC} (3.1) = R170_856(3.5); borde tras compresión 𝓡_cross + 𝒫^{comb}_{N,T} + B_μP𝒫_{C,A} (3.2).
- **Afirmaciones.** Todas PROVED (identidades de libro mayor); «normal de incidencia aislada es
  observable físico»: REFUTED; ancla «RETAINED»; extensión nula del ancla al puerto: OPEN.
- **Detención.** El pegado elimina toda K_− (y K2, Selberg); el objetivo de Green correcto actúa
  sobre la tupla (𝒩_PC, 𝓡_cross, 𝒫^{comb}, B_μP𝒫_{C,A}) (5.1–5.2), no construido.
- **Cotejo.** T2: sí (continúa el modelo de incidencia; queda como «condición de pegado exacta,
  no energía positiva terminal», §4). T4: roza — la normal pegada es la de PC completa con colas H,
  pero sin cuadrados. T1, T3: no más allá de 863.

### R170_865 — Audit of the incidence anchor
- **Objeto.** ∂ = [B, −I], (Bx)_k = Σ_{dm=k}x_{d,m}; Ran ∂ = C₀, ker ∂ = {(x,Bx)} (0.2);
  Δ = [[B^*B, −B^*],[−B, I]] (2.1), ∂∂^* = BB^* + I ⪰ I (2.2); pseudoinversa ∂^† = ∂^*(BB^*+I)^{-1} (2.3);
  proyector P_{ker∂} = I − ∂^*(BB^*+I)^{-1}∂ (6.1).
- **Afirmaciones.** Identidades de 863: CORRECT. Sobreyectividad y grafo universal: PROVED.
  «La positividad de Δ selecciona Λ»: FALSE. «Sección y = log más Möbius selecciona Λ»: PROVED
  (sólo reformula la unicidad de a∗1 = log). Green algebraico: BUILT / WEIGHT-BLIND. Ancla cierra
  el puerto: REFUTED. Proyector (6.1): TOOL. Sostenido.
- **Detención.** Nulidad = grafo universal; el primer chorro de ‖v(s)‖² en v(0) = 0 es cero por
  razón diferencial pura (4.2); convertir el ancla en ancla exterior equivale a 𝔚_K + Θ_ext = 0 (5.1).
- **Corregida por.** R170_866 (cabecera): imponer compatibilidad multiplicativa.
- **Cotejo.** T2: sí — es exactamente el fracaso de la incidencia como Gram: la forma ∂^*∂ y su
  inversa dependen sólo del grafo de divisores, no de Λ. T3: sí — la cota cuadrática ‖Bx − y‖² es
  ciega; la especificidad de Λ entra sólo por la sección fijada. T1, T4: no.

### R170_866 — Multiplicatively compatible null line
- **Objeto.** 𝒟_N: ℝ^N ⊕ ℝ → ℝ^N, (𝒟_N(a,c))_k = k^{-1/2}(Σ_{d|k}a_d − c log k) (0.1);
  ker 𝒟_N = ℝ(Λ|_{[1,N]}, 1) (0.2); 𝓛_N = 𝒟_N^*𝒟_N ⪰ 0 con línea nula única (0.3).
  U_N a = a∗1 unitriangular, det 1, inversa Möbius truncada (1.1–1.3).
  Energía ‖𝒟_N(a,1)‖² = Σ_{k≤N} |(a∗1)(k) − log k|²/k (4.1), nula ⇔ a = Λ en [1,N] (4.2).
  Tensorización (5.1), núcleo ℝ(Λ,1) ⊗ 𝓗 (5.4); chorro normal (6.1) = (𝒜^{raw}_{M,N} − K_−)_{≤N}F.
- **Afirmaciones.** Todo PROVED (declarado y sostenido: álgebra lineal triangular + μ∗log = Λ).
  Extensión positiva al complejo PC pegado: OPEN.
- **Detención.** El primer derivado de la energía se anula en el núcleo; el segundo es el cuadrado
  de (6.1): no firma el puerto. Hay que extender la línea a celdas Poisson, reflejada, polar y Tate.
- **Corregida por.** R170_867–868 (toda extensión lineal factoriza: sólo cambia la métrica normal).
- **Cotejo.** T3: sí, de lleno — es literalmente «identificación total de Λ por Σ_{d|n}Λ(d) = log n
  convertida en forma cuadrática» (4.1), con nulidad que separa Λ de toda modificación finita (y de
  cΛ, c ≠ 1, salvo el reescalado de la columna c). Fracasa porque la forma vive en el espacio de
  coeficientes (a,c), no en F, y su contenido en F es sólo el cuadrado de segundo orden del chorro.
  T2: sí (versión compatible del Gram de incidencia). T1, T4: no.

### R170_867 — PC graph extension of the null line
- **Objeto.** PC homogénea en (a,c): L_a = Σ_{d≤M} a(d)d^{-1/2}τ_{log d}, A_{a,c} = c𝓜 − (L_a + L_a^*),
  H_{a,c} = L_aS_N − cK_N; S_N A_{a,c}𝓕 = c{X,E_N} − L_a^*E_N − JH_{a,c} − H_{a,c}𝓕 (1.3).
  H^{≤N}_{a,c} = V_N(𝒟_N(a,c)), V_N(v) = Σ v_kτ_{log k} (2.3–2.4); residuo con sólo cola
  𝓡_{PC} = 𝒯_{PC}𝒟_N(a,c), 𝒯_{PC}(v) = −JV_N(v) − V_N(v)𝓕 (3.2–3.3).
  Laplaciano extendido 𝒟_N^*(I + 𝒯^*𝒯)𝒟_N, núcleo ℝ(Λ,1) (0.3–0.4). Prop. 5.1: toda extensión
  (I; Q)𝒟_N da 𝒟_N^*(I + Q^*Q)𝒟_N con el mismo núcleo.
- **Afirmaciones.** PROVED (sostenido). «Extensión factorizada produce bloque mixto de primer orden»:
  REFUTED. Componente de borde no factorizada: NECESSARY / OPEN.
- **Detención.** El chorro se transporta linealmente (6.2) pero la energía vuelve a empezar en orden dos.
- **Corregida por.** R170_868 (cierre: tal componente es imposible si es lineal en (a,c) y anula la línea).
- **Cotejo.** T2/T3: sí — Gram de incidencia con métrica I + Q^*Q; cambio de métrica sin signo. T4:
  roza — 𝒯_{PC} contiene el bloque interior de la hipérbola PC, pero sólo como métrica normal. T1: no.

### R170_868 — Universal factor-through theorem
- **Objeto.** Teorema: ℓ: ℝ^N ⊕ ℝ → Y lineal con ℓ(Λ,1) = 0 ⇒ ∃! Q con ℓ = Q𝒟_N (0.5);
  versión operador (4.4); extensiones positivas lineales = 𝒟_N^*(I + ΣQ_j^*Q_j)𝒟_N (3.3).
  Salida «aumentada por borde»: dominio Ê_N = (ℝ^N⊕ℝ)⊗𝓗 ⊕ B_T, vector nulo ê_T(f) = ((Λ,1)⊗f, β_T(f)),
  cancelación conjunta ℓ_ar((Λ,1)⊗f) = −ℓ_bd(β_T(f)) (5.4) y bloque mixto (5.5).
- **Afirmaciones.** Factorización, cambio de métrica, versión tensor: PROVED (sostenido, primer
  teorema de isomorfismo). Componente no factorizada en el mismo espacio: IMPOSSIBLE. Ampliación por
  borde: NECESSARY. Construcción de β_T: OPEN.
- **Detención.** NO-GO de clase: toda extensión lineal en (a,c) que anule la línea es cambio de métrica.
- **Cotejo.** T2/T3: sí — es el NO-GO que cierra el uso lineal de la incidencia y de la identidad de
  divisores como forma cuadrática en el espacio de coeficientes. T1, T4: no.

### R170_869 — Null line splitting and boundary class
- **Objeto.** Sección σ_N(v) = (U_N^{-1}W_N^{-1}v, 0); x = σ_N(𝒟_Nx) + c(Λ,1) (1.6).
  Toda fila ℓ = Q𝒟_N + cβ_ℓ, β_ℓ(F) = ℓ((Λ,1)⊗F) (0.2–0.3). Sucesión exacta
  0 → 𝓘_D → Hom(E,Y) → Hom(𝓗,Y) → 0 (3.3). Clase física β_phys = g_εΔ^{Tate} = 𝔚_K + Θ_ext (0.4).
- **Afirmaciones.** Descomposición, clasificación, cociente: PROVED. β_phys: IDENTIFIED (bajo REG/C1
  importado de R170_859). «PC/Möbius determinan β_phys»: REFUTED. «Minimalidad ⇒ β_phys = 0»: OPEN LAW.
- **Detención.** La aritmética fija el subespacio donde vive la clase, no su valor; manipular sólo
  el ideal 𝓘_D es circular (§4).
- **Cotejo.** T3: sí (todo lo que se deduce linealmente de Λ∗1 = log cae en el ideal y es mudo sobre
  la clase). T1, T2, T4: no directamente.

### R170_870 — Odd boundary class vs even minimality
- **Objeto.** β_phys lineal, impar en F (0.3); minimalidad Z_T Ḣ_T Z_T ⪯ 0 par (0.2). Lema 2.1: dual
  del espacio lineal entero es {0}. Teorema de independencia (§4): ℓ_β((a,c)⊗F) = Q𝒟_N(·) + cβ(ZF)
  para cualquier β ∈ Z^*, sin cambiar H_s, radical, cono tangente ni línea aritmética.
- **Afirmaciones.** Paridad, equivalencia «signo unilateral ⇔ β = 0», independencia: PROVED.
  Minimalidad + álgebra de coeficientes ⇒ β = 0: REFUTED. Acoplamiento impar o segundo radical común:
  NECESSARY / OPEN.
- **Observación textual.** §§6–7 son copia literal de §§6–7 de R170_871 (mencionan (3.5) y (4.4),
  que no existen en 870): error de edición.
- **Cotejo.** T1–T4: no; es la pared de paridad que afecta a todo funcional lineal.

### R170_871 — Factor swap exterior cycle
- **Objeto.** ι(d,m) = (m,d); anclas x^L = Λ(d)/√(dm), x^R = Λ(m)/√(dm), ambas con columna log;
  ciclo ω_Λ = x^L − x^R con suma por fibra cero e ιω = −ω (1.4–1.6). Con P = P_T, Q = I − P:
  PLQSP − PSQLP = −(PLPSP − PSPLP) (0.3), Φ_ext + Φ_int = 0 (3.5); derivada antidiagonal (4.4).
- **Afirmaciones.** PROVED (sostenido, inserción de I = P + Q en P(LS − SL)P = 0). Canal impar:
  REALIZED / CLASS ALREADY IN R161. Identificación con β_phys: PARTIAL. Anulación por minimalidad: OPEN.
- **Corregida por.** R170_872 (colisión con el concomitante de soporte R161_057/064).
- **Cotejo.** T2: roza (rutas (d,m) de incidencia). T1, T3, T4: no.

### R170_872 — Factor swap corpus collision
- **Objeto.** Auditoría: (0.1) = polarización del concomitante 𝒦_P(S;g,w) = ⟨Pg,PSQw⟩ − ⟨Qg,SPw⟩ de R161_064(2.2).
  Tabla de diccionario 871 ↔ R161. Falsificador operador: L, S conmutantes, P proyección con PLQSP − PSQLP ≠ 0
  (desplazamientos nilpotentes finitos).
- **Afirmaciones.** Identidad correcta; clase nueva: NO (colisión); «swap/conmutatividad ⇒ flujo
  cero»: REFUTED; reciprocidad Tate/exterior: OPEN.
- **Cotejo.** T1–T4: no.

### R170_873 — Tate modular cocycle and virial jet
- **Objeto.** Cociclo 𝐜_n(s) = a_n(e^{su_n}, e^{−su_n}), u_n = log n, a_n = Λ(n)/√n (0.1);
  𝐜_n(1/2) = (Λ(n), Λ(n)/n); 𝐜_n'(0) = Λ(n)log n/√n (1,−1) (0.2); generador A_n = diag(u_n, −u_n).
  Puerto deformado 𝒥^{ar}_T(s;F) = Σ_{2≤n<e^{2T}} a_n(e^{su_n}R_{n,+}(F), e^{−su_n}R_{n,−}(F)) (3.1),
  más colar Γ (3.3). Identidad suficiente abierta β_phys(F) = 𝔅_T(ZF, ∂_s𝒥^{full}_T(0;F)) (4.3).
- **Afirmaciones.** PROVED en pesos/collares; la cabecera de novedad dice que el chorro no es clase
  nueva (R170_845, R161_036/041). Realización como segundo vector nulo y (4.3): OPEN.
- **Corregida por.** R170_874 (no determina la clase exterior), R170_876.
- **Cotejo.** T1: sí, parcialmente — pesos aritméticos Λ(n)n^{±s} en el parámetro de dilatación
  y peso virial Λ(n)log n/√n; pero sin cuadrado: A_n tiene signos opuestos (§2). T2–T4: no.

### R170_874 — Modular cocycle quotient no-go
- **Objeto.** Lema de extensión independiente: ℰ_β((a,c)⊗F) = (D_N(a,c)⊗F, cβ(F)) (1.2) conserva
  cociclo, jet, línea (Λ,1), PC lineal y minimalidad diagonal para todo β. Criterio de continuación:
  operador 𝒥̂ con 𝒥̂ℰ_phys = ℰ_phys𝒥 y pr_∂𝒥̂ = −1 (3.1–3.2).
- **Afirmaciones.** Independencia: PROVED; «swap interior determina Θ_ext»: REFUTED; criterio:
  FORMULATED; extensión literal: OPEN.
- **Corregida por.** R170_876 (la involución pura es incompatible: A_L ↦ A_S).
- **Cotejo.** T1–T4: no.

### R170_875 — Static Tate port typing and falsifier
- **Objeto.** Reparación de tipo 𝔓̂^{ren} = Z_NA_M (0.2). Fórmula RZ_NA_MF − r_F = (RPZ_Nr_F − r_F)
  + RΔ^R_{N,T}ℓ_F − φ_−a_−(ℓ_F) (1.1). Gram G = Φ^*Φ = 2[[sinh T, T],[T, sinh T]]; coordenadas
  explícitas (2.1). Falsificador NUMÉRICO: T = ½log5, ℓ = 0, r = b_+: RZ_Nr ≈ (0.95543, −1.03070) ≠ (1,1) (2.4).
  Identidad de Wronskiano gΔ^{Tate} = ρ(κ−1)g + ((q̇,z) − (q,ż)) (3.1).
- **Afirmaciones.** Defecto original MISTYPED; reparación y fórmula finita: PROVED; igualdad
  estática: REFUTED (por un valor numérico, no verificado aquí); ley de signo: OPEN.
- **Cotejo.** T1–T4: no.

### R170_876 — Full PC factor swap obstruction
- **Objeto.** σ(L,S) = (S,L) fija H_L = LS − K pero A_L = 𝓜 − (L+L^*) ↦ A_S ≠ A_L (0.2–0.3);
  defecto 𝔒_{L,S} = SA_L − LA_S = (S−L)𝓜 + LS^* − SL^* (2.2); derivación −[X,S_N] = K_N^{(1)},
  −[X,L_N] = Σ Λ(n)log n/√n τ (3.1–3.2), Ω_N = K^{(Λ,1)} − K^{(1)} (3.3); chorro (4.2); ley covariante (5.1).
- **Afirmaciones.** PROVED/REFUTED según tabla; Ω_N «COMPUTED / CANCELS IN PC» (corregido por 877).
- **Corregida por.** R170_877.
- **Cotejo.** T1–T4: no.

### R170_877 — Swap PC cancellation and extraction obstruction
- **Objeto.** K_B = −[X,B]; H_{L,S} − H_{S,L} = −D_K (1.5); cancelación completa de D_K y su
  reflejo en PC (2.1–2.4); defecto par residual (3.2); variante polar −𝒫_C(A_L) − 𝒫_C(A_S) no canónica.
  Teorema: S = I + N_S, L = N_L (Λ(1) = 0), (PL^*P)^m = 0 para m log 2 > 2T, PL^*P no invertible (4.3–4.4).
  Ley pre-extracción (5.1): clase de ∂_−𝔒 − 𝒫_C(A_L) = −β_phys.
- **Afirmaciones.** PROVED (sostenido); ley (5.1): FORMULATED / OPEN.
- **Cotejo.** T1–T4: no (la asimetría usa el valor exacto Λ(1) = 0, dato aritmético, sin cuadrado).

### R170_878 — Möbius exterior loop for q
- **Objeto.** M = Σ μ(n)n^{-1/2}τ_{log n}, MS = SM = I; (PS_N^*P)^{-1} = PM^*P (N ≥ e^{2T}) (0.3);
  q_N = QS_N^*PM^*Pb (0.4a) = −QS_N^*QM^*Pb − QU_N^*M^*Pb, U_N = S − S_N (0.4b). Derivada congelada
  q̇ = QṠ_N^*PM^*Pb (2.1); 𝔚_ext = (q̇, z_F) − (q_N, ż_F) (2.3). L = MK por Λ = μ∗log (3.2);
  ℓ_F = Q𝓜F − QMKF − QK^*M^*F + Q(R_M + R_M^*)F (3.5); z_F (3.6).
- **Afirmaciones.** Todo PROVED; signo/anulación de (2.3): OPEN.
- **Corregida por.** Cabeceras de corte (truncación L_M, cola U_N; R170_884).
- **Inconsistencia.** (3.6) escribe +ρ_F QS^*QM^*Pb, que corresponde a la fórmula de peine completo
  previa a la corrección; con (0.4b) debería ser +ρ_F(QS_N^*QM^*Pb + QU_N^*M^*Pb) (o la forma
  equivalente de R170_884(0.2)). La cabecera dice que §3 está corregido, pero (3.6) no lo está.
- **Cotejo.** T3: sí, lineal — inserta Λ = μ∗log a nivel operador (L = MK), no como cota cuadrática;
  la memo advierte que separar términos de (3.6) y acotarlos perdería las cancelaciones. T1, T2, T4: no.

### R170_879 — Boundary Möbius divisor law
- **Objeto.** q_N(t) = Σ_k b(t − log k)k^{-1/2} 𝔪_{N;T,t}(k), 𝔪_{N;T,t}(k) = Σ_{n|k, n≤N, |t−log n|≤T} μ(k/n) (0.2–0.3);
  forma excluida 𝔪 = −Σ_{n>N o t−log n∉[−T,T]} μ(k/n) (2.2); operador de borde 𝔅_{N,T} (4.1);
  𝔚_ext = (𝔅̇b, z_F) − (𝔅b, ż_F) (4.2). Ejemplo de signo: k = 6, ventanas de divisores {6} → +1, {2,3,6} → −1.
- **Afirmaciones.** Expansión puntual, coeficiente como suma parcial de Möbius, equivalencia
  interior/excluido, finitud local: PROVED. Signo individual de 𝔪: FALSE IN GENERAL. Ley de sumación
  por partes con cola y polar: OPEN.
- **Detención.** 𝔪 cambia de signo; la anulación término a término es falsa.
- **Cotejo.** T3: sí, lineal — suma parcial de Möbius en el borde, sin cuadrado. T2: roza (poset de
  divisores). T1, T4: no.

### R170_880 — Boundary first moment is Mangoldt
- **Objeto.** 𝔪_{T,t}(k) = Σ_{n|k} μ(k/n) 1_{[log n − T, log n + T]}(t) (0.1); ∫𝔪 dt = 2T·1_{k=1} (0.2),
  ∫t𝔪 dt = 2TΛ(k) (0.3). Momento interior 𝔍_T(k) = ½Σ_{n|k, n<e^{2T}} μ(k/n)(T² − (log n − T)²) (2.4);
  ley 𝔈_T(k) = 2TΛ(k) − 𝔍_T(k) (2.2). Con corte: primer momento físico para k > N:
  2TΛ(k) − 2TΣ_{n|k, n>N} μ(k/n)log n (2.8). Ley de Ward (3.1): Σ w(k)𝔈_T + Σ w(k)𝔍_T = 2TΣΛ(k)w(k).
- **Afirmaciones.** PROVED (sostenido; μ∗1 = δ, μ∗log = Λ). Identificación del peso del Wronskiano
  físico y cancelación del continuo polar: OPEN.
- **Corregida por.** R170_884 (el predictor físico usa 𝔪_N, con cola).
- **Cotejo.** T3: sí — identificación exacta de Λ como primer momento de la incidencia de Möbius;
  identidad lineal en los pesos, sin cuadrado. T1, T2, T4: no.

### R170_881 — Affine Mangoldt extraction and shape remainder
- **Objeto.** ℳ_{T,k}[φ] = ∫𝔪_{T,t}(k)φ(t)dt = 2TaΛ(k) + ℛ_{T,k}[φ;a,c], ℛ = ∫𝔪(φ − at − c) (0.2–0.3).
  Desintegración hipotética 𝔚_ext + 𝔓_pol = Σ k^{-1/2}ℳ_{T,k}[φ_{F,k}] (3.1) ⇒ canal de Mangoldt + residuo de forma (3.2).
- **Afirmaciones.** Extracción afín, definición del residuo: PROVED. «El primer momento determina
  tests generales»: REFUTED (ψ ≥ 0 en un intervalo de signo constante). Aplicación directa a S_N para
  k > N: REFUTED. (3.1) y (3.3) Σ k^{-1/2}ℛ = 0: OPEN.
- **Cotejo.** T3: sí, lineal (extrae Λ del componente afín; el resto cociente por span{1,t} queda libre).
  T1, T2, T4: no.

### R170_882 — Log-weighted boundary Möbius Ward law
- **Objeto.** 𝔩_{N;T,t}(k) = Σ_{n|k, n≤N, |t−log n|≤T} μ(k/n)log n = Λ(k) + 𝔢_{N;T,t}(k) (0.1, 0.4),
  𝔢 = −Σ_{n>N o |t−log n|>T} μ(k/n)log n (0.5); q̇^0 = Q∂_t(Σ Λ(k)k^{-1/2}b(·−log k) + ℰ_{N,T}b) (2.3);
  𝔚_ext = −ΣΛ(k)k^{-1/2}∫b(t−log k)z_F' − ∫ℰ_{N,T}b z_F' − ∫q_N ż_F (3.3);
  residuo de rutas 𝔑_route (4.1); ley pendiente 𝔑_route + 𝔓_pol + Θ_Γ = 0 (4.2).
- **Afirmaciones.** PROVED (en el núcleo); cancelación coeficiente a coeficiente con el polar:
  REFUTED BY TYPE; identificación del colar de Mangoldt con el canal primo del virial y (4.2): OPEN.
- **Cotejo.** T3: sí, lineal (μ∗log = Λ localizado en (t,k)); los defectos 𝔢 cambian de signo. T4:
  roza — es un apareamiento de la cola de rutas con z_F', pero lineal en F. T1, T2: no.

### R170_883 — Boundary Dirichlet covariant derivative
- **Objeto.** Series 𝓜_{N;T,t}(s) = A_{N;T,t}(s)/ζ(s), A = Σ_{n≤N, e^{t−T}≤n≤e^{t+T}} n^{-s} (0.2–0.3);
  𝓛 = (1/ζ)Σ log n n^{-s} (0.4); ∇_ζ = ∂_s + ζ'/ζ, 𝓛 = −∇_ζ𝓜 (0.6); serie de rutas excluidas
  (2.3–2.4); continuo polar c_N(s) = N^s/s (3.2); A^{cont} (3.3–3.4); defecto suma–continuo 𝒟_{N;T,t} = A − A^{cont} (3.5).
- **Afirmaciones.** PROVED en Re s > 1 (sostenido; no se usa continuación). Comparación de tipo con
  el continuo polar: PROVED. Identificación transformada §4 y signo: OPEN.
- **Cotejo.** T3: sí, lineal (reformulación generatriz de μ∗log = Λ). T4: roza — (3.5) es el defecto
  suma–continuo, pero sin cuadrado. T1, T2: no.

### R170_884 — Finite cutoff and continuous polar audit
- **Objeto.** Corrección S → S_N: q_N = −QS^*QM^*Pb − QU_N^*PM^*Pb (0.2); incidencia física y
  momentos con cola (1.2–1.4); ley de Ward logarítmica finita (2.2–2.3); polar C_N = ∫_0^N x^{-1/2}τ_{log x}dx,
  coeficientes continuos 𝔠_{N;T,t}(y) = Σ_{m, y/m≤N, |t−log(y/m)|≤T} μ(m)/m (3.3); residuo mínimo 𝔑_min (4.1).
- **Afirmaciones.** PROVED; cancelación polar/discreto coeficiente a coeficiente: REFUTED (tipo);
  identidad Euler–Maclaurin emparejada: OPEN.
- **Nota.** (0.2) y R170_878(0.4b) son dos formas equivalentes de la misma identidad (comprobado:
  ambas salen de QS^*M^*Pb = 0 descomponiendo distinto); no hay contradicción.
- **Cotejo.** T4: sí, en el sentido de identificar el lugar — comb discreto vs continuo polar con
  colas U_N y R_M; no convierte nada en cuadrados. T3: lineal. T1, T2: no.

### R170_885 — Exact Euler–Maclaurin Wronskian port
- **Objeto.** W(u,v) = (u̇,v) − (u,v̇); Z_N = S_N − C_N; identidad 𝔚_ext + (h, P𝒫_{C,A_M}F) =
  W(QZ_N^*h, ℓ) − W(PC_N^*h, r) (0.2). Desintegración discreta–continua QZ_N^*h = Q[Σ_k b(t−log k)k^{-1/2}m^d_N(k,t)
  − ∫ b(t−log y)y^{-1/2}c_N(y,t)dy] (2.3), análoga logarítmica (2.6); separación
  (QZ_N^*h)˙ = Q∂_t[L_M^*b + R_M^*b + ℰ_{N,T}b − 𝓛^{cont}_{N,T}b] (3.1). Falsificadores de cierre
  algebraico: multiplicador Σ_{n≤N}n^{-s} − N^{1−s}/(1−s) ≢ 0 (4.1); en t < −T, QS_N^*h = 0 pero
  C_N^*h(t) = e^{t/2}∫e^{-u/2}h ≠ 0 (4.2). Residuo 𝔑_EM (5.2–5.3).
- **Afirmaciones.** PROVED (sostenido algebraicamente); anulación algebraica del predictor
  renormalizado: REFUTED; signo vía minimalidad: OPEN.
- **Cotejo.** T4: sí — es la versión Euler–Maclaurin del apareamiento mixto comb/continuo (Z_N) con
  colas, escrito como Wronskiano (forma alternada, lineal en F); no hay h(k)|ℓ_k(F)|². Fracaso
  registrado: Z_N no es cero y el Wronskiano no tiene signo propio. T3: lineal. T1, T2: no.

### R170_886 — Euler–Maclaurin anchor range law
- **Objeto.** Ancla e_EM = q_N − C_N^*h; 𝔚_ext + (h,P𝒫_{C,A_M}F) = W(e_EM, A_MF) (0.2); representante
  ω_EM = Π_{𝒫_T}(A_M^*ė_EM − Ȧ_M^*e_EM) (0.3), forma operador (2.4); ley exterior ⇔ ω_EM ∈ cl Ran H_T
  (3.1); ecuación de Poisson H_Tg_EM = ω_EM (3.2, 5.1); factorización suficiente (5.2).
- **Afirmaciones.** Fusión, representante, equivalencia: PROVED. «Reducción estrictamente nueva»:
  NO (criterio de Fredholm, autocorregido en la cabecera). Minimalidad cuadrática ⇒ rango: REFUTED.
  Construcción aritmética de g_EM: OPEN.
- **Corregida por.** R170_887 (conexión de la rama móvil), R170_889 (validada).
- **Cotejo.** T4: roza (mismo objeto que 885). T1–T3: no.

### R170_887 — Covariant EM anchor and minimality audit
- **Objeto.** e_s = Q_sS^*_{N,s}h_s − C^*_{N,s}h_s; de/ds = ė_fr + χ_e, χ_e = −ṖS_N^*h + (QS_N^* − C_N^*)ḣ (0.2–0.4);
  𝔚_cov = W_fr(e_EM, A_MF) + (χ_e, A_MF) − (e_EM, A_MḞ) (0.5); Pḣ = B^{-1}P(ḃ − Ḃh) (1.3);
  Wronskiano invariante W_∇ (2.6); Hellmann–Feynman ν = Re(F,ȦF) + 2Re(AF, Π̇F) ≤ 0 (3.2);
  pared de paridad ν(−F) = ν(F), 𝔚_cov(−F) = −𝔚_cov(F) (4.1–4.2).
- **Afirmaciones.** PROVED (algunas bajo REG/C1); signo de funcional lineal por minimalidad: REFUTED
  BY PARITY; ley covariante (5.1): OPEN.
- **Cotejo.** T1–T4: no.

### R170_888 — Z_N minimality ledger and parity wall
- **Objeto.** P Ȧ_MF = 𝒷_NP(Z_NȦ_M − Ż_NA_M)F + 𝒷_NP𝒫_{C,A_M}F + 𝒫^{comb}_{N,T}(F), 𝒷_N = (PS_NP)^{-1} (0.2);
  libro mayor ν = cuatro líneas ≤ 0 (0.3), sólo la suma es invariante de gauge; versión de collar
  finito importada (λ_δ − λ_0)⟨F_δ, E_δF⟩ = ⟨ξ^δ_F, F_δ|_{C_δ}⟩ (4.1).
- **Afirmaciones.** Libro mayor: PROVED UNDER REG/C1; signo del residuo lineal EM: REFUTED BY PARITY;
  identificación 𝔑_EM = λ̇: REFUTED; elevación impar a la identidad finita: OPEN.
- **Cotejo.** T1–T4: no. (Es la única expresión cuadrática en F del tramo, pero es la derivada del
  autovalor, con signo heredado de la minimalidad, no una suma de cuadrados.)

### R170_889 — Double neutral audit of the EM chain
- **Objeto.** Protocolo de doble control y clasificación de objeciones (A–E). Contraejemplo de gauge
  en ℝ²: rotación con U̇e₁ = e₂, U̇e₂ = −e₁ hace W(Ue, Uv) = 2 con W(e,v) = 0.
- **Afirmaciones.** 886(0.2) validada (comprobación NUMÉRICA declarada en 300 modelos matriciales
  finitos); criterio de rango = Fredholm; 887 validada con corrección de gauge; 888 validada bajo
  hipótesis; ley covariante: OPEN.
- **Cotejo.** T1–T4: no.

### R170_890 — Tate quadratization and correct moving coordinate
- **Objeto.** ρ(F) = (a,F); ρΩ_EM = (F, K_EM F), K_EM = (a⊗ω + ω⊗a)/2, rango ≤ 2 (0.3); coordenada física
  σ_ε(F) = 2Re(Π̇F, b_ε) = −2Re(F, t b_ε') (1.1), defecto 𝔑_Tate = Δσ_ε (1.3); autovalores
  ((a,ω) ± ‖a‖‖ω‖)/2 (2.1); contraejemplo finito en base (e₁,e₂,b) (3.1–3.4): ρΩ = xy de ambos signos;
  energía de Tate normal ρβ = ½D‖r‖² − … (4.2).
- **Afirmaciones.** PROVED; signo desde minimalidad: REFUTED (contraejemplo verificado al leer:
  Π(A₀+sV)Π = −sI y Ω(F) = y); relación firmada ρ–σ–Ω: OPEN.
- **Cotejo.** T1–T4: no. (Cuadratiza un funcional lineal por producto de dos funcionales: forma de
  rango dos, indefinida salvo colinealidad.)

### R170_891 — ρ/σ Gram and prime node separation
- **Objeto.** b_ε = e^{−t/2} + εe^{t/2}, g_ε = 4(sinh T + εT); a_ε = g_ε^{-1}Π_εPA_Mb_ε, s_ε = −2Π_ε(t b_ε') (0.3–0.4);
  det G(a_ε, s_ε) por (2.4) con d = 2(T cosh T − sinh T), E = T² sinh T − 2T cosh T + 2 sinh T − εT³/3;
  separación por el nodo x₀ = T − log 2 (saltos ℓ₂b_ε(T), ℓ₂b_ε'(T), posible colisión con d' = e^{2T}/2) ⇒ det G > 0 para T > ½log 2 (0.5).
- **Afirmaciones.** Representantes y Gram: PROVED; independencia primitiva: PROVED TWICE (argumento de
  regularidad: P𝓜b_ε suave en el interior, Π_εḃ_ε analítica; sostenido en esquema); independencia tras
  proyección al radical: OPEN / FALSE IN DIM 1.
- **Cotejo.** T1–T4: no (Gram de dos vectores; el nodo del 2 es dato aritmético, sin signo de a_T).

### R170_892 — Bordered KKT and Tate virtual work
- **Objeto.** Lagrangiano 𝓛_s = ½(F,A_sF) + α(F,b_s) + β/2(‖F‖² − 1); sistema KKT linealizado (1.3);
  2Re(Π̇F, Δb) = σΔ (2.2), bloque [[0,½],[½,0]] de signatura (1,1) (2.4); Schur −(y, H_𝒯^{-1}y) (3.4);
  contraejemplo en ℝ² con restricción móvil: σΔ = −2κδ de cualquier signo (4.6).
- **Afirmaciones.** PROVED / PROVED UNDER SIMPLE/REG; «KKT firma σΔ»: REFUTED BY COUNTEREXAMPLE;
  Ω_EM,cov = gΔ_tot y estabilización en N: OPEN. La memo declara que la auditoría delegada no pudo
  ejecutarse y no la sustituyó por aceptación.
- **Cotejo.** T1–T4: no.

### R170_893 — Exact polar normalization defect
- **Objeto.** Ω_EM := 𝔚_ext + (h, P𝒫_{C,A_M}F); gΔ^{Tate} − Ω_EM = ρ[(ḃ^0,b) − g] − (h,P𝒫_{C,A_M}F) (0.4);
  Ω_EM = gΔ ⇔ (h,P𝒫_{C,A_M}F) = ρ[(ḃ^0,b) − g] (0.5, «ley de normalización polar»); expansión literal (2.1);
  trabajo virtual tipado σΔ = (σ/g)[Ω_EM + ρ((ḃ^0,b) − g) − (h,P𝒫F)] (4.1).
- **Afirmaciones.** PROVED (algebra a partir de R170_856(8.4)); ley (0.5): OPEN.
- **Cotejo.** T1–T4: no.

### R170_894 — Polar moment residual and moving face
- **Objeto.** Con N ≥ e^{2T}: α(f) = ∫_I e^{u/2}f, β(f) = ∫_I u e^{u/2}f, H₀, H₁ (0.1–0.2);
  (h,PC_Nf) = H₀α(f), (h,PĊ_Nf) = (H₀ − H₁/2)α(f) + (H₀/2)β(f) (0.3–0.4); momentos exteriores
  𝖷_N(v), 𝖣_N(v) con cara móvil −(log N)√N v(t + log N) (2.3); residuo polar mínimo 𝔑_pol (3.2).
  Independencia abstracta: variar Qv con 𝖷_N(v) ≠ 0 conservando el dato interior (§4).
- **Afirmaciones.** PROVED; «primer contacto interior ⇒ 𝔑_pol = 0»: REFUTED IN THE ABSTRACT; identidad
  aritmética de la cara móvil: OPEN.
- **Cotejo.** T4: roza (cara t + log N = borde de corte del comb/continuo), lineal. T1–T3: no.

### R170_895 — Integer jump EM collar balance
- **Objeto.** N(T) = e^{2T}, T_n = ½log n; ancla a_T = Q_TZ^*_{N(T)}h_T; balance de medidas en T:
  D_Ta_T = −Ṗ_TZ_N^*h_T + Q_TΣ_n n^{-1/2}τ_{−log n}h_T δ_{T_n} − 2√N Q_Tτ_{−log N}h_T dT + Q_TZ_N^*D_Th_T (0.2);
  d_NZ_N = Σ n^{-1/2}τ_{log n}δ_n − N^{-1/2}τ_{log N}dN (1.2); D_Th_T (2.2), Ṗ_Tf = f(T)δ_T + f(−T)δ_{−T} (2.3);
  salto [a_T]_{T_n} = Q_{T_n}n^{-1/2}τ_{−log n}h_{T_n} (3.1); inserción Möbius (4.1) y fibras (Λ∗μ)(r) (4.2).
- **Afirmaciones.** PROVED; «conservación algebraica automática»: REFUTED; ley de medidas que cancele
  el balance: OPEN. La lectura (4.2) con Λ∗μ fue corregida por R170_896 (composición innecesaria).
- **Cotejo.** T4: roza — balance Euler–Maclaurin entero/continuo, lineal; T3: lineal (Möbius). T1, T2: no.

### R170_896 — Exact Möbius extraction of cutoff measure
- **Objeto.** K = Σ log d d^{-1/2}τ_{log d}, M (Möbius), L (Mangoldt); K(d_NZ_N)M = L(d_NZ_N) (0.1) por
  Σ_{dm=r} log d μ(m) = Λ(r); expansión (1.2–1.3); adjuntos [K dZ M]^* = (dZ)^*L^* (1.4); prohibido
  insertar P o Q entre factores (§2). Comparación: el Wronskiano de dilatación lleva
  −Λ(r)log(r/n)∂_tτ_{log nr} (3.2), que (0.1) no da.
- **Afirmaciones.** PROVED (sostenido; conmutatividad en el álgebra causal); «coincide con el canal
  virial de grado uno»: FALSE; elevación antidiagonal: OPEN (resuelta algebraicamente en 897).
- **Cotejo.** T3: sí, lineal — extracción exacta de Λ en la medida de corte (grado cero), sin
  conversión cuadrática. T1: roza (traslaciones en la dilatación con peso Λ(r)). T2, T4: no.

### R170_897 — Antidiagonal lift of cutoff measure
- **Objeto.** δτ_{log a} = log a ∂_tτ_{log a}, E = d_NZ_N; 𝔚_ad(E) = (δL)E − L(δE) = (δK)EM + KE(δM) − K(δE)M (0.2);
  parte atómica Σ_{n,r} Λ(r)log(r/n)(nr)^{-1/2}∂_tτ_{log nr}δ_n (0.3) por Σ_{dm=r} μ(m)[(log d)² + log d log m] = Λ(r)log r (2.2);
  δM = −M(δS)M (3.1); parte continua Σ_r Λ(r)log(N/r)(Nr)^{-1/2}∂_tτ_{log Nr}dN (4.2).
- **Afirmaciones.** PROVED (sostenido, regla de Leibniz); «canal virial primo de grado uno CLOSED
  ALGEBRAICALLY»; ensamblaje Γ/adjunto/cola/Tate: OPEN.
- **Cotejo.** T3: sí, en grado dos lineal (la relación de grado dos Leibniz sobre Λ∗1 = log, que
  OBJECT_SPEC O2 ya identifica), sin cuadrado en F. T1: roza (pesos aritméticos en la derivación de
  dilatación). T2, T4: no.

### R170_898 — Finite integrated cutoff Wronskian
- **Objeto.** Convención física τ̇_{log a} = −log a ∂_tτ_{log a}; 𝒲_{M,N} = L̇_MZ_N − L_MŻ_N (0.3);
  d_N𝒲 = 𝓘_{M,N} (0.4) con 𝓘^{at} = Σ_n Σ_{r≤M} Λ(r)log(n/r)(nr)^{-1/2}∂_tτ_{log nr}δ_n,
  𝓘^{cont} = Σ_{r≤M} Λ(r)log(r/N)(Nr)^{-1/2}∂_tτ_{log Nr}dN (0.5); ley integrada desde N = 1:
  𝒲_{M,N} = 𝒲_{M,1} + ∫_{(1,N]}𝓘, 𝒲_{M,1} = L̇_M(I − C_1) + L_MĊ_1 (0.6), o (0.7) con átomo n = 1 incluido;
  C_1, Ċ_1 explícitos (2.1–2.2), Ċ_N integrado con cara móvil (2.5); 𝖷_N, 𝖣_N desde N = 1 (4.1–4.2).
- **Afirmaciones.** PROVED; paso a peine primo infinito: NOT JUSTIFIED (series ΣΛ(r)/r divergentes en
  LC_Nf); ensamblaje: OPEN.
- **Cotejo.** T4: roza — ley finita del Wronskiano comb–continuo con colas, lineal. T1: roza. T2, T3: no.

### R170_899 — Finite polar Green assembly
- **Objeto.** 𝒢_B(N) = ḂC_N − BĊ_N; 𝒫_{C,A_M}(N) = 𝒢_𝓜(N) − 𝒢_{L_M}(N) − 𝒢_{L_M^*}(N) (0.2);
  𝒢_B(N) = 𝒢_B(1) + ∫_1^N[Ḃ dC_x − B dĊ_x] (2.1); bloque Γ 𝒥_Γ(x) = x^{-1/2}τ_{log x}[𝓜̇ + (log x)𝓜∂_t] (3.2);
  𝒥_+(x) = Σ_{r≤M} Λ(r)log(x/r)(rx)^{-1/2}∂_tτ_{log rx} (4.1), 𝒥_−(x) = Σ Λ(r)log(xr)(rx)^{-1/2}∂_tτ_{log(x/r)} (4.2);
  residuo de normalización 𝔑^{M,N}_pol (5.2–5.3); residuo tipado 𝔑_rem = Re(h,P[𝒢_𝓜 − 𝒢_{L_M^*}]F) − ρRe[(PṠ_N^*Ph,b) − g] (7.2);
  𝒜^{ren} = 𝒜^{raw} − 𝒢_{L_M} (7.3).
- **Afirmaciones.** PROVED; residuo finito: EXPLICIT; anulación o signo: OPEN.
- **Observación.** (4.4) define 𝓑_1 = 𝒫_{C,A_M}(1), pero en (5.3) aparece «Re(h,P𝓑_1F) + ρg», y la
  ρg sale de −ρ(−g); consistente. La afirmación «Ṡ_N^* = Σ log n n^{-1/2}∂_tτ_{−log n}» (5.1) usa el
  signo de la convención física para traslaciones negativas; coherente con (4.2).
- **Cotejo.** T1: roza (pesos Λ(r)log(x/r) en la dilatación, sin cuadrado). T4: roza (ensamblaje polar
  comb/continuo, lineal). T2, T3: no.

### R170_900 — PC–Tate collision audit
- **Objeto.** 𝒢_𝓜(C_N) − 𝒢_{L_M^*}(C_N) = 𝒞_PC + 𝒜^{raw} − 𝒢_{A_M+L_M}(Z_N), 𝒞_PC = S_NȦ_M − Ṡ_NA_M (0.1);
  𝒟_PC = 𝒞_PC + 𝒜^{raw} expandida (1.1) con H_{M,N} = Σ_{N<k≤MN} h_{M,N}(k)k^{-1/2}τ_{log k} (1.3);
  𝔑_rem = Re(h,P[𝒟_PC − 𝒢_{A_M+L_M}(Z_N)]F) − ρRe[…] (1.2) y forma de colisión (2.2) con factor 2 en
  −2ρRe(ḃ^0, b), obligatorio salvo ley de tangencia no probada.
- **Afirmaciones.** Identidad (0.1): PROVED (comprobada de dos maneras); reducción lógica nueva: NO;
  tangencia: NOT PROVED; signo/anulación: OPEN.
- **Cotejo.** T4: sí, en el sentido de que el residuo final conserva literalmente H_{M,N} (colas
  N < k ≤ MN) y los apareamientos mixtos de PC, pero sólo como funcional lineal en F; no hay
  conversión a Σ h(k)|ℓ_k(F)|². T1–T3: no.

---

## 2. Síntesis

### (a) Piezas PROVED reutilizables
1. Línea nula única de la incidencia multiplicativamente compatible: ker 𝒟_N = ℝ(Λ,1),
   ‖𝒟_N(a,1)‖² = Σ_{k≤N}|(a∗1)(k) − log k|²/k — R170_866 §§1–4.
2. Grafo universal y proyector de pegado P_{ker∂} = I − ∂^*(BB^*+I)^{-1}∂ — R170_865 §§1–2, §6.
3. Teorema de factorización universal ℓ(Λ,1) = 0 ⇒ ℓ = Q𝒟_N; extensiones positivas lineales = cambio de métrica — R170_868 §§1–4; descomposición ℓ = Q𝒟_N + cβ_ℓ y sucesión exacta — R170_869 §§1–3.
4. PC homogénea en (a,c) e H^{≤N}_{a,c} = V_N(𝒟_N(a,c)) — R170_867 §§1–3.
5. Pegado incidencia–Poisson: 𝒩_X + 𝒩_H = −𝒜^{raw} — R170_864 §2.
6. Identidad de corte PLQSP − PSQLP = −(PLPSP − PSPLP) — R170_871 §3.
7. Cociclo de Tate 𝐜_n(s) y jet Λ(n)log n/√n — R170_873 §§1–3.
8. Defecto físico del swap SA_L − LA_S = (S−L)𝓜 + LS^* − SL^*; cancelación PC de D_K; PL^*P nilpotente (Λ(1) = 0) — R170_876 §2, R170_877 §§1–4.
9. (PS_N^*P)^{-1} = PM^*P (N ≥ e^{2T}) y bucle de Möbius de q_N — R170_878 §1, R170_884 §0.
10. Expansión puntual de q_N con 𝔪_{N;T,t}(k) — R170_879 §1; momentos ∫𝔪 = 2Tδ_{k1}, ∫t𝔪 = 2TΛ(k), fórmula del momento interior — R170_880 §§1–2; extracción afín — R170_881 §1.
11. Ley de Ward logarítmica 𝔩 = Λ + 𝔢 y q̇^0 — R170_882 §§1–2, R170_884 §2; series de Dirichlet 𝓜 = A/ζ, 𝓛 = −∇_ζ𝓜 (Re s > 1) — R170_883 §§1–2.
12. Identidad Euler–Maclaurin 𝔚_ext + (h,P𝒫_{C,A_M}F) = W(QZ_N^*h,ℓ) − W(PC_N^*h,r) = W(e_EM, A_MF) y desintegración discreto–continua — R170_885 §§1–3, R170_886 §§1–2.
13. Derivada total del ancla EM y Wronskiano covariante W_∇ — R170_887 §§1–2; libro mayor Z_N de ν (bajo REG/C1) — R170_888 §1.
14. Gram de (a_ε, s_ε) y det > 0 para T > ½log 2 — R170_891 §§1–3.
15. Diferencia gΔ^{Tate} − Ω_EM = ρ[(ḃ^0,b) − g] − (h,P𝒫F) — R170_893 §1; momentos polares interiores/exteriores — R170_894 §§1–2.
16. Medida de corte d_NZ_N, balance (0.2) y saltos enteros — R170_895 §§1–3; K(d_NZ_N)M = L(d_NZ_N) — R170_896 §1; elevación antidiagonal con Λ(r)log(r/n) — R170_897 §§1–4; ley integrada finita 𝒲_{M,N} desde N = 1 — R170_898 §§1–2, §4; descomposición 𝒫_{C,A_M} = 𝒢_𝓜 − 𝒢_{L_M} − 𝒢_{L_M^*} — R170_899 §§1–4; identidad (0.1) de R170_900.

### (b) Cierres (clase y falsificador)
1. **Incidencia libre como forma positiva selectora** — clase: Laplaciano ∂^*∂ de ∂ = [B,−I]; falsificador: ker = grafo universal, todo a da vector nulo con y^a (R170_865).
2. **Extensiones lineales de la línea nula** — clase: filas lineales en (a,c) que anulan (Λ,1); NO-GO: factorizan por 𝒟_N y sólo cambian la métrica normal (R170_867 Prop. 5.1, R170_868).
3. **Determinación de la clase de borde por PC/Möbius/cociclo/minimalidad** — clase: identidades factorizadas + minimalidad par; falsificador: modelo aumentado ℓ_β con β arbitrario (R170_869 §3, R170_870 §4, R170_874 §1).
4. **Signo unilateral de un funcional lineal en el radical** — clase: minimalidad cuadrática; NO-GO por paridad (Lema 2.1 de R170_870; R170_887 §4; R170_888 §3).
5. **Swap / conmutatividad ⇒ flujo exterior nulo** — falsificador: desplazamientos nilpotentes finitos (R170_872 §4).
6. **Involución pura del swap en el puerto físico** — falsificador: A_L ↦ A_S ≠ A_L (R170_876); extracción simétrica imposible: PL^*P nilpotente (R170_877 §4).
7. **Puerto Tate estático R Z_NA_MF = r_F** — falsificador NUMÉRICO en T = ½log5: (0.95543, −1.03070) ≠ (1,1) (R170_875 §2).
8. **Signo término a término de 𝔪 o 𝔢** — falsificador: k = 6, ventanas de divisores {6} → +1, {2,3,6} → −1 (R170_879 §3).
9. **Primer momento determina tests generales** — falsificador: ψ ≥ 0 en intervalo de signo constante de 𝔪 (R170_881 §2).
10. **Cancelación polar/discreto coeficiente a coeficiente** — error de tipo: comb en k vs continuo en y (R170_882, R170_883 §3, R170_884 §3).
11. **Cierre algebraico Z_N = 0** — falsificadores: multiplicador Σ_{n≤N}n^{-s} − N^{1−s}/(1−s) ≢ 0 y C_N^*h ≠ 0 en t < −T (R170_885 §4).
12. **Ecuación de rango como reducción nueva** — es el criterio de Fredholm (R170_886, R170_889 B).
13. **Cuadratización ρΩ_EM firmada por minimalidad** — contraejemplo en ℝ³ con ρΩ = xy (R170_890 §3).
14. **KKT firma σΔ** — contraejemplo con restricción móvil σΔ = −2κδ (R170_892 §4).
15. **Primer contacto interior ⇒ 𝔑_pol = 0** — independencia abstracta del bloque exterior (R170_894 §4).
16. **Conservación algebraica automática del ancla** (R170_895); **coincidencia de grado cero con el virial** (R170_896 §3).
17. **Wronskiano ordinario invariante de gauge** — contraejemplo de rotación en ℝ² (R170_889 §2).

### (c) Abierto explícitamente, con obstáculo exacto
1. Extensión positiva de 𝓛_N al complejo PC pegado con nulidad uno en la coordenada aritmética y borde = puerto combinado (R170_866 §7); obstáculo: R170_868 obliga a salir del espacio (a,c) o de la linealidad con cancelación conjunta ℓ_ar((Λ,1)⊗f) = −ℓ_bd(β_T(f)) (5.4) y bloque mixto (5.5).
2. Ley de clase de borde: β_phys|_{ker H_T} = 0 (R170_869 §5, R170_870 §7, R170_871 (7.1)); obstáculo: β impar, minimalidad par; se necesita acoplamiento impar o segundo radical común.
3. Identidad mixta positiva (4.3) de R170_873 desde PC-ren con Tate en la posición de R161_064(1.1).
4. Naturalidad exterior: operador 𝒥̂ con (3.1)–(3.2) de R170_874; reemplazada por la ley covariante 𝒥̂ℰ_L(F) − ℰ_S(𝒥̂F) = Γ_{L,S}(F) (R170_876 (5.1)) y la ley pre-extracción: clase de ∂_−𝔒 − 𝒫_C(A_L) = −β_phys (R170_877 (5.1)).
5. Signo/anulación del Wronskiano exterior en bloques de Möbius (R170_878 (2.3)); identidad de sumación por partes en el poset de divisores con cola R_M y continuo polar (R170_879 §4).
6. Desintegración física coeficiente a coeficiente (R170_881 (3.1)) y anulación del residuo de forma Σ k^{-1/2}ℛ_{T,k} = 0 (3.3).
7. Identificación del colar de Mangoldt con el canal primo del virial y 𝔑_route + 𝔓_pol + Θ_Γ = 0 (R170_882 (4.2)); versión transformada en s (R170_883 §4).
8. Identidad Euler–Maclaurin emparejada en el residuo mínimo (R170_884 (4.1)); construcción aritmética de g_EM con H_Tg_EM = ω_EM (R170_886 (5.1)–(5.2)); ley covariante (R170_887 (5.1)); elevación impar a la identidad de collar finita (R170_888 §4).
9. Relación firmada ρ–σ–Ω en el radical (R170_890); independencia tras proyección al radical (R170_891 §4, falsa en dimensión 1).
10. Ω_EM,cov = gΔ_tot y estabilización en N de todos los puertos (R170_892 §5).
11. Ley de normalización polar (h,P𝒫_{C,A_M}F) = ρ[(ḃ^0,b) − g] (R170_893 (0.5)); obstáculo: dos momentos exteriores 𝖷_N(QȦ_MF), 𝖣_N(QA_MF) con cara móvil no determinados por el dato interior (R170_894 (3.3)).
12. Ley de medidas en T que cancele el balance (R170_895 §5); ensamblaje Γ/adjunto/cola/Tate (R170_897–899); anulación del residuo finito (R170_899 (5.3), (7.2)); ley de tangencia que elimine el factor 2 en (2.2) de R170_900.

### (d) Lo que en este tramo ya recorre T1–T4, con razón de fracaso
- **T2 (incidencia de divisores como Gram).** R170_863 (complejo ∂ = [B,−I], Δ = ∂^*∂), R170_865 (auditoría),
  R170_866 (versión compatible 𝒟_N con U_N unitriangular), R170_867–868 (extensiones). Razones: (i) con
  coordenadas libres la forma positiva es universal y ciega a los pesos (grafo y = Bx, pseudoinversa que
  depende sólo del grafo); (ii) con compatibilidad multiplicativa, la forma ‖𝒟_N(a,c)‖² vive en el espacio
  de coeficientes y sólo dice a = Λ; (iii) su contenido en F es la energía ‖∂e_Λ(r,q;F)‖², cuyo primer
  chorro es cero por razón diferencial y cuyo segundo chorro es ‖(𝒜^{raw} − K_−)_{≤N}F‖², que pierde la
  orientación; (iv) el pegado con la celda Poisson cancela K_− y deja −𝒜^{raw} (R170_864); (v) toda
  extensión lineal que conserve la línea es cambio de métrica (R170_868). No se usa la factorización
  [log mcd(i,j)] = E diag(Λ)Eᵀ en sí: el Gram usado es BB^* + I o 𝒟_N^*𝒟_N, no la matriz de mcd.
- **T3 (Σ_{d|n}Λ(d) = log n convertida en forma cuadrática).** R170_866 (4.1) es literalmente
  Σ_k |(a∗1)(k) − log k|²/k, nula sólo en a = Λ; fracasa por (ii)–(v) de arriba. Además, como usos
  lineales: R170_878 (L = MK), R170_879–884 (μ∗1 = δ, μ∗log = Λ en el borde, momentos, Ward), R170_883
  (series de Dirichlet), R170_896 (K dZ M = L dZ), R170_897 (Leibniz de grado dos). Razón común: todo
  lo que se deduce linealmente de la identidad cae en el ideal factorizado 𝓘_D (R170_869) y es mudo sobre
  la clase de borde; los coeficientes de borde 𝔪, 𝔢 cambian de signo (R170_879 §3); el primer momento
  no determina tests generales (R170_881 §2).
- **T1 (cuadrados continuos con aritmética en la dilatación).** Sólo roces: R170_873 (cociclo
  Λ(n)n^{±s}, generador diag(log n, −log n) de signos opuestos), R170_897–899 (pesos Λ(r)log(r/n),
  Λ(r)log(x/r), Λ(r)log(xr) en la derivación de dilatación). En ningún caso se forma un cuadrado; los
  objetos son Wronskianos alternados o jets lineales. No hay razón de fracaso de T1 propiamente dicha:
  T1 no se ensaya.
- **T4 (apareamientos mixtos PC → Σ_{k>N} h(k)|ℓ_k(F)|²).** R170_885–886 (Euler–Maclaurin Z_N = S_N − C_N),
  R170_894–895, R170_898–900 (cara móvil t + log N, saltos enteros, ley integrada, H_{M,N} con
  N < k ≤ MN preservado en el residuo final (R170_900 (1.2)–(1.3))). Todo se escribe como funcional
  LINEAL en F (Wronskianos y momentos) y su suerte la fija la pared de paridad (R170_870, R170_887 §4,
  R170_888 §3): un funcional lineal no hereda signo de la minimalidad. Nunca se intenta la conversión a
  suma de cuadrados con peso h(k) ≥ 0; la vía T4 en sentido estricto no está recorrida en este tramo.

### (e) Inconsistencias o errores vistos
1. R170_870 §§6–7 son copia literal de R170_871 §§6–7 (citan (3.5), (4.4) y el swap L ↔ S, inexistentes en 870).
2. R170_878 (3.6): el término +ρ_F QS^*QM^*Pb no incorpora la corrección de corte de su propia
   cabecera; con (0.4b) debería ser +ρ_F(QS_N^*QM^*Pb + QU_N^*M^*Pb). Además «M» denota a la vez el
   peine de Möbius y el índice de corte de L_M en la misma memo.
3. R170_863 §3 presenta la rigidez como selectividad F3 «exacta»; la propia cabecera (R170_865) la
   rebaja a fijación externa de y = log. La etiqueta del cuerpo no está corregida, sólo anotada.
4. R170_876 declara Ω_N como defecto de derivación; R170_877 prueba que se cancela en PC; 876 lo anota
   en cabecera y en su tabla («CANCELS IN PC»). Coherente tras corrección.
5. R170_895 (4.2) lee fibras Λ∗μ; R170_896 lo corrige (la composición correcta es K dZ M).
6. R170_875 (2.4) y R170_889 (300 modelos) apoyan afirmaciones en comprobaciones NUMÉRICAS no reproducidas en el texto.
7. R170_892 declara que una de sus dos revisiones no pudo ejecutarse; la etiqueta «audited twice»
   del título es por tanto más fuerte que lo que el texto describe.
8. R170_884 (0.2) y R170_878 (0.4b) parecen distintas pero son equivalentes (dos descomposiciones de QS^*M^*Pb = 0); no es error.

### (f) Archivos leídos (lectura completa con Read, cada uno hasta su última línea)
R170_863, R170_864, R170_865, R170_866, R170_867, R170_868, R170_869, R170_870, R170_871, R170_872,
R170_873, R170_874, R170_875, R170_876, R170_877, R170_878, R170_879, R170_880, R170_881, R170_882,
R170_883, R170_884, R170_885, R170_886, R170_887, R170_888, R170_889, R170_890, R170_891, R170_892,
R170_893, R170_894, R170_895, R170_896, R170_897, R170_898, R170_899, R170_900 — 38 archivos, todos completos.
