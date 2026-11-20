# Ronda 9, encargo G3 — dónde el mapa no tiene marcas

Notación de la fase: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real, sop F ⊂ [−T,T], F ∈ P_T.
Memo de selección. No se deriva nada nuevo. La conclusión (§4) es que **ninguna candidata pasa mi propio
cotejo**; se dan, para las dos mejores, la operación que falta.

Fuentes leídas en primaria para este memo: `RULES_AVOID.md` §§A–R; `REVIEW_003.md`–`REVIEW_007.md`;
`ROUND_008_A.md`; IDX `README.md` (búsquedas dirigidas: renovación BPY l.2270–2357, FAMILIES_B_001 l.571);
IDX `AUDIT_A.md` (A14a-1); `phase-188-closing-D/N_BUILD_007_CONE_ORDER_ON_A_T.md` §§0–3;
`phase-106-global-modular-star-audit/106_115_FOLDED_STOCHASTIC_MONOTONICITY_AND_REFLECTION_GATE.md` §§1–3.
Búsquedas por grep en `03-research/` y `05-meta-and-planning/` de: Birkhoff, métrica de Hilbert proyectiva,
Kreĭn–Rutman, mayorización, disminución de variación, Donsker/Gibbs variacional, Hamilton–Jacobi, Hopf–Lax,
Prékopa, determinantal, renovación, cono invariante. Una búsqueda sin coincidencias no prueba novedad.

## 1. Taxonomía de clases de método recorridas (operación que produce el signo · por qué falla)

| # | Clase | Operación de signo | Motivo estructural del fracaso | Referencia |
|---|---|---|---|---|
| 1 | Suma de cuadrados con multiplicador/símbolo | reparto puntual del símbolo en sectores de paridad | lineal en la autocorrelación; ciego al peso | J1 (R3-a), B4 |
| 2 | Reparto local por contactos | q_∞ + Σ_p q_p, cada q_v ⪰ 0 | con reparto libre = objetivo; con regla fija muere en el umbral arquimediano | O1–O3, Q1 (R7-a), M2 (G2_B8) |
| 3 | Cota de contacto por potencial / estado fundamental | contacto ≤ potencial ≥ 0 | resto ⪯ Arch, indefinido para T ≳ 0.60 | Q1 (R7-a) |
| 4 | Reducción a matriz de Schur finita / LDL / factorización canónica | pivotes, raíz de la forma | existe con resto ≥ 0 sii vale el objetivo | J3, L5, D17 (suelo de Schur) |
| 5 | Término de segundo orden en el peso | cuadrado afín V_0 + V_1(Λ) o defecto cuadrático que suma | ρ ≤ Arch; o el objetivo con margen; no paga el primer jet | J2 (R3-b), L3 (R4-c) |
| 6 | Signatura, inercia, Kreĭn/Pontryagin, Lorentz | conteo de índices negativos | constante para c cerca de 1 | L6 (R4-f), N1 (R5-a), M1 |
| 7 | Polinomio hiperbólico / estabilidad real / Lee–Yang | raíces reales de un objeto de grado ≥ 3 | grado dos o el objetivo con margen | N2 (R5-b), M3 |
| 8 | Inducción en la ventana / predicados de etapa | herencia del signo al alargar T | en el cruce el peso entrante no influye; paso uniforme = reparto local | N4 (R5-d), Q2 (R7-b), BARRIER_W_001 |
| 9 | Dilatación de Naimark / canal producto–cociente | paralelogramo ¼‖(U−V)f‖² | término firmado ciego al peso; el aritmético es [P,S], indefinido | Q3 (R7-c), R1, K2–K3 |
| 10 | Fuga / compresión a la ventana / Toeplitz–Hankel | ‖(1−P)SP‖² | sin identidad con el defecto de PC; ensamblaje global cerrado | K1, R2, fase 122 |
| 11 | Varianza / función de partición / entropía | Var ≥ 0 | las leyes de ζ^c son probabilidades para todo c | N5 (R5-e), I5 |
| 12 | Modelo positivo + transferencia o comparación | K ≥ εK_ref, transporte desde C_0 | prefactores y comparadores aditivos excluidos con prueba | B4 (211 HYPERBOLIC §§7–13) |
| 13 | Positividad total / variación decreciente / PF_k | menores ≥ 0 | falla en PF₂ (104_21) y PF₅ (A14a-1); 𝖡 no es TP | C1, L5 (R4-e), 106_42 |
| 14 | Monotonía estocástica / Markov / principio del máximo | semigrupo que preserva un cono de funciones | la rama reflejada |t−u| invierte el orden en cada átomo | 106_115 §1, C1 (Markov) |
| 15 | Orden de cono dual en el álgebra causal | convolución que preserva 𝒦_T^* | el resolvente es indefinido en orden; δ_a ∉ ±𝒦_T^* | N_BUILD_007 §§1–3 |
| 16 | Flujo de calor / Laguerre–Pólya / Bakry–Émery Γ₂ / Grönwall en T | monotonía bajo un flujo | flujo genérico en c, o reformulación | C1, D17 |
| 17 | Reflexión positiva (OS, tablero, GKS/FKG) | ⟨θF,F⟩ ≥ 0 | por lugar o en el borde excluido; frustración en 𝔸_M | C1, G2 (R-K1), M3 |
| 18 | Virial / dilatación / Pohozaev | identidad de dilatación | sin resto acotado inferiormente; genérico en el peine | J5 (R3-d), I5 |
| 19 | Criba / Möbius truncado / inversos aproximados | test de criba como inverso | no eleva el grado en el peso; R ≤ 0 falso | L2, L4 (R4-b, R4-d) |
| 20 | Identidad válida para todo peine (Poisson, theta, Selberg) | igualdad exacta + bloque positivo | no lleva signo | B1, D6, D16 |
| 21 | Estimación con resto | cota ≥ margen | margen exponencialmente pequeño en T | B2 |
| 22 | Cierre bajo producto de Euler | n₋ ≤ κ estable por producto | producto = suma de formas; índice no acotado | N3 (R5-c) |
| 23 | Incidencia de divisores como forma | E diag(Λ) Eᵀ, filas lineales sobre coeficientes | factoriza por 𝒟_N; pierde el primer jet | I1–I2, J7, J10 |
| 24 | Renovación aditiva / autodescomposición BPY | semigrupo de saltos con densidad invariante | sin densidad reversible; capas con jetdet < 0 | IDX README l.2270–2321 |
| 25 | Invariantes enteros (rango no negativo, recurrencia {x+y,xy}, Forster) | invariante sin valor genérico | cerrados en C1 tras la fase 201 | C1, IDX l.571 |

(Clasificación por clase: ARGUED; cada motivo es CITED de la entrada indicada.)

## 2. Propiedades que todo objeto superviviente debe tener a la vez

Lista extraída de los NO-GO PROVED; cada línea cita lo que obliga.

P1. **No afín en el peso**, ni afín con término cruzado emparejado (R3-b); y no polinómica de forma que la
    diferencia con cΛ sea sólo combinación de átomos Σ_{d|n}a(d) − log n sin resto firmado (R3-i).
P2. **Los contactos son fuente, no costo, en las direcciones negativas de Arch**: ninguna pieza que acote
    contactos por arriba sirve más allá de T ≈ 0.60 (R7-a; Paper 47 cor:Tarch, CITED).
P3. **Paso dependiente de la historia**: un predicado de etapa con paso uniforme en un cono convexo es un
    reparto local (R7-b); el peso entrante no influye en el cruce (R5-d).
P4. **Usa la ley de semigrupo entera** τ_{log k}τ_{log l} = τ_{log kl} acoplada a la compresión P_T: los
    contramodelos 2×2 (R161_038) y 3×3 (R161_050) satisfacen (PC), radicalidad, paridad y transferencia
    algebraica sin saturar (ROUND_008_A §3).
P5. **Exacto a la precisión del margen**: el ancho de la ventana en c es del orden del margen
    (211 ROUND_021_A Lema 3.3; §P), y el margen es ≤ 4·10⁹Te^{−15.449T} (B2). Ninguna estimación con resto.
P6. **No es un conteo de inercia ni un invariante local en c**: índices constantes cerca de c = 1 (R4-f).
P7. **No es una realización de Gram en un punto base** (log-concavidad, varianza, hessiana de un polinomio
    homogéneo): R5-a, R5-e. Puede ser una propiedad válida en todo un cono con certificado propio
    (lo que R5-a deja explícitamente sin excluir).
P8. **No local por lugar**: el producto de Euler suma formas (R5-c); Teorema D de la fase 159 (G2_B8_R5):
    el reparto óptimo es holgura complementaria de estados obstructores, circular como regla previa (J3).
P9. **Ve el lado aritmético con valores exactos y la estructura atómica**, no sólo la masa del peine
    (𝒦_S, W-pat; P47 rem:bar-pat) y no factoriza por un objeto Λ-libre fijo (fase 170, «factor-through»:
    toda fila lineal que anula ℝ(Λ,1) factoriza por 𝒟_N, I1).
P10. **Dos canales acreditados por falsificadores distintos**: a_P rompe la ecuación funcional, cuartetos
     el producto de Euler (G1); y el resto (no la identidad) deja de ser ≥ 0 en c = 2, en el borrado y
     en Beurling (R3-i).
P11. **Dimensión creciente con T** (Thm finZ; §P; D12 soporte fijo excluido).
P12. **Un cono preservado por la operación no puede ser 𝒦_T^* bajo convolución por medidas firmadas
     con átomos en (0,2T)** (N_BUILD_007 §§1–2): si el mecanismo es de orden, la operación no es una
     convolución en el álgebra causal.

(P1–P12: ARGUED como lista; cada ítem CITED de su fuente.)

## 3. Operaciones de signo fuera de la taxonomía: cotejo

| Operación | Antecedente más cercano | Qué está excluido exactamente | ¿Se conserva? |
|---|---|---|---|
| Varianza con ley genuinamente no lineal | N5 (R5-e); 104_54, 104_71 (Gibbs/entropía); IDX FAMILIES_B (DPP, RMT) | toda identidad de varianza bajo las leyes de ζ^c (genérica en c); DPP «no virgen» | No: una ley construida desde el peso hereda la genericidad en c salvo que use P4, y no tengo objeto |
| Punto fijo / flujo monótono con límite conocido | R7-b, R5-d, D17 (Grönwall en T), N_BUILD_007, 106_115 | paso uniforme; convolución en el álgebra causal; semigrupo de Markov plegado | **Sí como hueco (candidata A, sin objeto)**: contracción en métrica proyectiva de Hilbert (Birkhoff) con paso no uniforme; «Hilbert projective metric» sin coincidencia en el corpus (las 46 coincidencias de «Hilbert metric» son métricas de producto interno, 114_d_102–139) |
| Orden: retículo, mayorización, PT, variación decreciente | C1 (PT orden ≥ 5, PF₂), L5, 106_42, 106_115, N_BUILD_007, M3 (FKG) | núcleos TP/Pólya; pivotes por patrón; monotonía estocástica; convolución preservando 𝒦_T^* | No: la mayorización «peine ≺ Arch en el orden de 𝒦_T^*» es exactamente la positividad de ventana (N_BUILD_007, encabezado): reformulación |
| Convexidad en otro parámetro (forma = segunda derivada) | R5-a, R5-b, M1 (R160_C7_R1 §6.3(2)), B10 (Danskin en c) | log-concavidad en punto base; polinomio hiperbólico; concavidad en el peine | **Sí como hueco (candidata B, sin objeto)**: funcional convexo en todo un cono con certificado propio (R5-a lo deja explícito) |
| Reflexión positiva t ↦ −t con contactos cruzando | C1 (OS/tablero, OS en el borde, OS por lugar NG-E1), J1 (J en sectores de paridad), G2 R-K1, 106_115 (rama reflejada |t−u|) | reflexión en el borde, por lugar, en sectores de paridad; R-K1 prohíbe reflexiones de borde | No: con reflexión en 0, ⟨θF,F⟩ es ⟨JF,F⟩, y el álgebra de multiplicadores + J es R3-a; los contactos que cruzan el plano son el término ε⟨X²F,F⟩ de signo opuesto en los dos sectores |
| Conteo (forma = cardinal o medida) | C1 (rango no negativo, recurrencia {x+y,xy}); I5 (energía de Laplace en la retícula Gamma, genérica); K5 (resto de hipérbola ≥ 0, ninguna ponderación lo cancela) | invariantes enteros de la fase 201; h(k) ≥ 0 | No: un cardinal es ≥ 0 para todo peso con soporte en ℕ; no rompe en c = 2 (P10) sin un término restado, y entonces no es conteo |
| Categórica / traza | C3 (Floer, motívico, Bridgeland, sitio aritmético) | reformulaciones | No: no puedo escribir el objeto (regla del encargo) |

(Cotejos: ARGUED, por lectura de las entradas citadas; no exhaustivos.)

## 4. Candidatas

**Ninguna sobrevive a mi propio cotejo.** No hay objeto escrito para ninguna. Doy las dos mejores con la
operación que falta, en el formato de la puerta, para que un revisor decida si merecen una ronda.

### A. Contracción proyectiva con paso dependiente de la historia (Birkhoff–Hopf)

1. *Antecedente:* `ROUND_007_B.md` Lema 1 / R7-b (paso uniforme = reparto local); `N_BUILD_007` §2
   (convolución preservando 𝒦_T^*: sólo múltiplos de δ₀ conocidos; general sin decidir); 106_115 §1.
2. *Objeto que haría falta:* una aplicación **no lineal** Φ_{T→T′} entre conos de formas (o de medidas
   duales) de las ventanas T < T′, que preserve el cono, con diámetro proyectivo finito de la imagen, y
   cuyo punto fijo o límite sea la forma de Λ. La positividad saldría del teorema de Birkhoff–Hopf
   (CITED como herramienta clásica), no de un reparto.
3. *Por qué esquivaría el antecedente:* R7-b exige que el paso valga para toda Q; una contracción proyectiva
   sólo exige preservar el cono en la imagen del paso anterior (dependencia de la historia, P3). No es
   convolución (P12).
4. *Conexión global:* si Φ preserva {a_T ⪰ 0 en P_T} y la iteración desde una ventana certificada
   (T ≤ ½log15, citada) alcanza toda T, se obtiene a_T ⪰ 0 para todo T.
- **Operación que falta:** no conozco ninguna aplicación natural de ventana a ventana que preserve
  positividad y use P4. La única transición conocida (alargar la ventana) es la inclusión P_T ⊂ P_{T′}, que
  va en la dirección equivocada (el signo en T′ implica el de T). Sin esa aplicación, la candidata es un
  esquema vacío. Primer enunciado que habría que intentar: «existe Φ explícita con Φ(a_T^{Λ}) = a_{T′}^{Λ}
  sobre P_{T′} que lleve formas ⪰ 0 a formas ⪰ 0». Falsificador: cΛ con c = 2 debe violar la preservación
  del cono (no sólo la identidad), y a_P debe romperla en una línea distinta que los cuartetos.

### B. Funcional convexo en todo un cono con certificado propio, cuya hessiana sea a_T

1. *Antecedente:* R5-a (deja sin excluir «una propiedad válida en un cono entero con certificado propio»);
   R5-b; M1 / R160_C7_R1 §6.3(2); N5.
2. *Objeto que haría falta:* Φ: P_T → ℝ, definido con la ley de semigrupo y la compresión P_T, convexo en
   todo P_T por una razón que no sea Gram en un punto (p. ej. supremo de funciones afines indexado por
   factorizaciones k·l, o composición de una función convexa creciente con funciones convexas), con
   D²Φ(0) = a_T.
3. *Por qué esquivaría el antecedente:* R5-a y R5-b miran un punto base o un polinomio; un certificado
   global de convexidad no es una realización de Gram en un punto.
4. *Conexión global:* D²Φ(0)[F,F] = a_T(F) ≥ 0 en P_T, cada T.
- **Operación que falta:** un supremo de afines indexado por factorizaciones es lineal en el peso en cada
  rama (cae en P1/J2); una composición convexa-creciente necesita una pieza interior convexa que ya lleva el
  signo. No tengo una tercera fuente de convexidad. Primer enunciado: «Φ(F) = sup_{k,l} ℓ_{k,l}(F) + q(F) con
  q ⪰ 0 Λ-libre y D²Φ(0) = a_T» — sospecho que es el formato J2 y no lo propongo.

## 5. Lista de afirmaciones

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | Taxonomía de 25 clases y sus motivos | ARGUED (cada motivo CITED) |
| 2 | Propiedades P1–P12 obligatorias | ARGUED (cada ítem CITED) |
| 3 | Mayorización en el orden de 𝒦_T^* = positividad de ventana | CITED (N_BUILD_007, encabezado) |
| 4 | Reflexión en 0 con contactos cruzando cae en R3-a | ARGUED |
| 5 | Un conteo puro no rompe en c = 2 | ARGUED |
| 6 | «Hilbert projective metric» / Birkhoff sin coincidencia sustantiva en el corpus | NUMÉRICO (grep; no prueba novedad) |
| 7 | La inclusión P_T ⊂ P_{T′} transfiere el signo sólo de T′ a T | PROVED (trivial) |
| 8 | Candidatas A y B: sin objeto; no pasan la puerta | OPEN |
| 9 | Signo global | OPEN |
