# Anexo: lectura por archivo de la fase 161, tramo 3 (R161_056 a R161_099)

Lectura completa de los archivos R161_056 … R161_081 y R161_099 de
`03-research/phase-161-row-d-sum-product-square/`. No hay archivos R161_082 … R161_098. Se registra lo que cada
memo construye y afirma; no se propone nada. Notación de las memos: Z_N = S_N^ren (síntesis entera menos
continuo), Fcal la involución de Fourier aditiva en escala log, J la reflexión, X la multiplicación por t,
P = P_T la compresión física a (−T, T), Q = I − P, Pi = Pi_T la proyección primitiva, Tau (o R) = P − Pi el
bloque de Tate de dimensión dos, E_N = Z_N Fcal − J Z_N (defecto de Poisson), C_N = Z_N Fcal + J Z_N,
A_M = 𝓜 − L_M − L_M* (operador de Weil finito), K_F(a) los momentos de Laplace de la fuente, a_m = 2m + ½.
"Primer contacto" significa un vector f del radical del operador primitivo comprimido H_T (H_T f = 0); las memos
razonan por contradicción a partir de tal f.

Advertencia de vocabulario. Varias memos (056 §2, 075 §§2–3, 079 §4 y la síntesis 099 §§4, 036–037) evalúan
símbolos en ceros de una función zeta o en «ceros críticos». Se registra sólo que **usan una equivalencia
externa / una reducción a ceros**; no se desarrolla.

---

## R161_056 — La fase unitaria finita tiene la tangente equivocada

- **Objeto.** A = Z_N(s), B = Z_N(1−s), e = Au − B (diferencia de Poisson), c = Au + B (suma complementaria),
  U = −A′u, V = −Z_N′(1−s). Identidades: U + V = −e′ + Au′ (1.1); en el lugar Au = B, B·θ′/θ = e′ para la fase
  unimodular θ = Au/B (1.3); U − V = −c′ + Au′ (2.1).
- **Afirmaciones.** Auditoría de la regla de la cadena: PROVED (cálculo directo, sostenido). La tangente de la
  fase unitaria controla la media U + V, no la diferencia U − V: PROVED. La identificación de la tangente
  unitaria con el chorro crítico propuesta en R161_052–055: rechazada. «Fuera del lugar Au = B el término
  principal no cambia» es ARGUED (no escrito).
- **Dónde se detuvo.** c es una suma aditiva de dos historias, no un cociente unimodular: el defecto
  Toeplitz–Hankel exacto de la colligación unitaria de R161_052 no se transfiere al chorro crítico. Queda abierta
  una identidad de Green cuadrática que mezcle e con c. En §2 usa una equivalencia externa (evaluación en un cero).
- **Corrección posterior.** Ninguna la retira; 057 desarrolla la identidad mixta.
- **Cotejo.** U1: no. U2: no directamente (sí de fondo: la colligación de 052 es de compresión). U3: no.
  U4: no. U5: sí, parcialmente: la colligación unitaria finita (dilatación por cociente unimodular) se conserva
  como transporte de la base, pero se prueba que su tangente da la orientación media, no la diferencia; no es
  una dilatación de fuente isométrica en el sentido de la salida A de R161_033.

## R161_057 — Forma exacta en cuatro bloques de la identidad de Green mixta

- **Objeto.** a = Z_N Fcal f, d = J Z_N f, e = a − d, c = a + d, proyecciones P_L, P_0, P_R (conmutan con X).
  Re⟨e, Xc⟩ = Σ_j [⟨a_j, X a_j⟩ − ⟨d_j, X d_j⟩] (1.1);
  Re⟨e, Xc⟩ = G_phys − G_wrong + T·Φ_ext + G_0 (1.4), con
  G_phys = ‖(X−T)^{1/2} a_R‖² + ‖(−X−T)^{1/2} d_L‖², G_wrong = ‖(−X−T)^{1/2} a_L‖² + ‖(X−T)^{1/2} d_R‖²,
  Φ_ext = ‖a_R‖² + ‖d_L‖² − ‖a_L‖² − ‖d_R‖², G_0 = ⟨a_0, X a_0⟩ − ⟨d_0, X d_0⟩.
  Bloques del conmutador de soporte: PZ − ZP = PZQ − QZP (4.1).
- **Afirmaciones.** (1.4) exacta a todo corte: PROVED (sostenido; álgebra de proyecciones que conmutan con X).
  Separación de flujo orientado y primer momento interior; la unitariedad total no cancela Φ_ext: PROVED
  (la fórmula (2.1) se enuncia «whenever a y d son las dos historias de la misma colligación»; es condicional a
  esa normalización). Reducción del conmutador de soporte a las dos discrepancias unilaterales Δ^R, Δ^L tras
  el ajuste de Tate: PROVED relativo a R161_006 y R161_009.
- **Dónde se detuvo.** Falta (3.3): G_wrong = conmutador_de_borde_N(f) + o(1), es decir la reciprocidad
  cuadrática de las dos discrepancias unilaterales con G_wrong. No se reemplaza por adjunción en todo el espacio
  porque (4.1) es exactamente lo que esa adjunción omite tras comprimir. OPEN.
- **Corrección posterior.** 058–060 y 065 muestran que la vía no produce el signo; 065 identifica el
  candidato de 064 con este conmutador.
- **Cotejo.** U2: sí, plenamente: usa X (= M_t), la compresión P_0 y los bloques fuera de diagonal PZQ, QZP
  (fuga), con contabilidad de Tate. U1, U3, U4, U5: no.

## R161_058 — Positividad del doble conmutador y prueba de reciprocidad

- **Objeto.** Para H ⪰ 0, f ∈ ker H, B acotado: ⟨f, [B*, [H, B]] f⟩ = ⟨Bf, HBf⟩ + ⟨B*f, HB*f⟩ ≥ 0 (1.1). Con
  JHJ = H, Jf = εf, JBJ = B*: ambos términos iguales, total 2⟨Bf, HBf⟩ (2.2).
- **Afirmaciones.** (1.1) y (2.2): PROVED (sostenidas). Anulación por paridad o ciclicidad de traza: rechazada
  (sostenido: es un estado vectorial, no una traza). Equivalencia «reciprocidad ⟺ el radical es invariante bajo
  B y B*»: PROVED (es lectura directa de (1.1)).
- **Dónde se detuvo.** La anulación (3.1) no es consecuencia formal de Hf = 0; haría falta derivar de (PC-ren)
  el balance negativo (4.1) «pareo mixto PC = −⟨f,[B*,[H,B]]f⟩ − D_N^Γ(F)». OPEN. Definir el pareo por el lado
  derecho sería circular.
- **Corrección posterior.** 059 da la forma en bloques; 060 sustituye PC-ren y no obtiene (4.1).
- **Cotejo.** U2: sí (H es la compresión primitiva; B la síntesis causal; bloques P_0BQ, QBP_0). U3: no (la forma
  es semidefinida). U1, U4, U5: no.

## R161_059 — Forma exacta en bloques del par conmutante comprimido

- **Objeto.** A = A*, AZ = ZA en todo el espacio; H = PAP, B = PZP, X = QAP, Y = QZP, Ȳ = QZ*P:
  [H, B] = Ȳ*X − X*Y (1.3), [H, B*] = Y*X − X*Ȳ (1.4); sobre el radical HBf = Ȳ*Xf − X*Yf.
- **Afirmaciones.** (1.3)–(1.4): PROVED (cálculo de inserción de Q, sostenido). Identificación de los puertos
  exteriores (Xf = imagen de Weil exterior; Yf, Ȳf historias de Poisson unilaterales): PROVED como lectura.
  Reducción a un cuadrado negativo desde conmutación + reflexión + Tate: rechazada (sostenido: los productos
  cruzados son indefinidos).
- **Dónde se detuvo.** Hace falta una relación adicional de PC-ren que identifique los productos cruzados con
  una forma de borde Γ/polar negativa; es la reciprocidad exterior cuadrática que falta. OPEN.
- **Corrección posterior.** 062 corrige que el portador de potencia es el anticonmutador, no el conmutador.
- **Cotejo.** U2: sí (compresión, palabras QZP, QAP, bloques de Tate añadidos por Pi). U3: sí, débilmente: los
  productos Ȳ*X − X*Y son formas indefinidas cruzadas; no se busca vector neutro. U1, U4, U5: no.

## R161_060 — Sustitución literal de PC en el doble conmutador

- **Objeto.** S A Fcal = R_PC; Af = r + ℓ (r Tate, ℓ exterior); Q_B(f) = ⟨Bf,HBf⟩ + ⟨B*f,HB*f⟩ se reescribe
  como Re⟨R_PC Fcal f, g_B^+⟩ + Re⟨R_PC Fcal f, g_B^−⟩ + términos polares/Tate explícitos (2.2).
- **Afirmaciones.** Inserción completada; sin anulación ni signo nuevo; la correlación exterior extremal de
  R161_023 se reconstruye. Etiquetas declaradas: «completed», «absent», «open». La forma (2.2) se da sin los
  términos polares/Tate escritos: es ARGUED en su detalle, aunque el diagnóstico es plausible.
- **Dónde se detuvo.** No se obtiene 0 = −Q_B(f) − D_N^Γ(F); haría falta una ley de borde antisimétrica para
  los dos pareos de (2.2). La ruta de Green mixta queda expandida en todas las capas (lista de §3).
- **Corrección posterior.** Ninguna.
- **Cotejo.** U2: sí (misma maquinaria de compresión y Tate). U1, U3, U4, U5: no.

## R161_061 — Identidad de borde lagrangiana Poisson–Tate (candidata)

- **Objeto.** K_T = G_T C (Gram de Tate por intercambio), simétrica e indefinida; forma simpléctica
  ω_T((v,j),(w,k)) = ⟨j,w⟩ − ⟨v,k⟩ en V_T ⊕ V_T; el grafo L_T = {(v, K_T v)} es lagrangiano (1.4). Portador
  infinito B_{N,T} = (E_R ⊕ E_L)², Ω((ξ,η),(ξ′,η′)) = ⟨η,ξ′⟩ − ⟨ξ,η′⟩, Ω_total = Ω + ω_T. Identidad propuesta
  (3.2): Ω_total(Λ_{N,T} f, Λ_{N,T} h) = ⟨PC_N f, h⟩ − ⟨f, PC_N h⟩.
- **Afirmaciones.** Grafo de Tate lagrangiano: PROVED (trivial por simetría de K_T). Portador de Green que
  reproduce el conmutador comprimido: PROVED «a nivel formal de bloques». (3.2) y su identificación con el
  escalar extremal (5.1) 2Re⟨g, P_R C_log g + εg⟩: OPEN/propuestas.
- **Dónde se detuvo.** Retirada por 062: la diagonal de una forma alternada es idénticamente nula.
- **Corrección posterior.** R161_062 §0 (retira la vía alternada como argumento de cierre); 065 cierra la familia.
- **Cotejo.** U3: sí: forma indefinida en el espacio de borde doble; pero simpléctica, donde todo vector es
  neutro; el grafo es isótropo para todo vector, no sólo para el de primer contacto, y por eso no lleva
  información. U2: sí (contabilidad conjunta con el bloque de Tate, K_T = G_T C de R161_009/032). U1, U4, U5: no.

## R161_062 — La identidad que falta debe ser una ley de potencia hermítica de borde

- **Objeto.** B(b,b′) = ⟨η,ξ′⟩ + ⟨ξ,η′⟩, B(b,b) = 2Re⟨η,ξ⟩; ⟨η,ξ′⟩ = (B + Ω)/2. Potencia de Tate
  B_T((v,K_Tv),(v,K_Tv)) = 2⟨v, K_T v⟩ (2.2). Anticonmutador comprimido (sin conmutación de A y Z):
  {H, B} = P{A,Z}P − Ȳ*X − X*Y (3.1); 2Re⟨Hf,Bf⟩ = ⟨f,P{A,Z}Pf⟩ − Re⟨Ȳf,Xf⟩ − Re⟨Xf,Yf⟩ (3.2); en el radical
  ⟨f,P{A,Z}Pf⟩ = Re⟨Ȳf,Xf⟩ + Re⟨Xf,Yf⟩ (3.3). Balance candidato (4.1) con 2⟨v_f, K_T v_f⟩ y término polar.
- **Afirmaciones.** Corrección a 061: PROVED (Ω(b,b) = 0). Forma B y potencia de Tate: PROVED algebraicamente.
  (3.1)–(3.3): PROVED (sostenido). (4.1): «bulk proved, primitive/polar expansion open». Límite (5.2) igual al
  escalar extremal: OPEN.
- **Dónde se detuvo.** Falta probar que, tras la compleción polar/Tate, la corriente de todo el espacio es
  exactamente el anticonmutador comprimido. Además 063 muestra que identificar R Z f con el collar cruzado está
  mal tipado.
- **Corrección posterior.** R161_063 §3 retira la identificación P_R(f) = 2⟨v_f, K_T v_f⟩ (introducida en la
  primera versión de 063 a partir de (4.1) de esta memo) y (4.4); 065 cierra la familia.
- **Cotejo.** U3: sí: B es una forma hermítica indefinida sobre el borde doble (tipo Kreĭn sobre (ξ,η)); no se
  estudian vectores neutros no radicales, se usa sólo su diagonal. U2: sí (compresión, puertos QA, QZ, bloque
  de Tate). U1, U4, U5: no.

## R161_063 — Descomposición exacta por compresión anidada de la potencia Poisson–Tate

- **Objeto.** I = Pi + R + Q (R bloque de Tate, Q exterior). H = Pi A Pi, B = Pi Z Pi.
  2Re⟨Hf,Bf⟩ = ⟨f, Pi{A,Z}Pi f⟩ − P_R(f) − P_Q(f) (2.1), P_R, P_Q pareos cruzados por bloque (2.2)–(2.3), sin
  término mixto Tate/exterior. En el radical: ⟨f,Pi{A,Z}Pi f⟩ = P_R(f) + P_Q(f) (2.4). Pareo mixto bien tipado
  con y = Z* g(f): Re⟨Af, y⟩ = Re⟨r, Ry⟩ + Re⟨ℓ, Qy⟩ (5.2); Re⟨r,Ry⟩ = Re⟨v_f, G_T C v_f⟩ (3.3).
- **Afirmaciones.** (2.1)–(2.4): PROVED (sostenido). Identificación diagonal R Z_N f = collar cruzado:
  rechazada/mal tipada. (3.3): PROVED relativo a R161_009 y R161_022. (5.2): PROVED pero coincide con la
  descomposición de retroceso ya auditada (R161_022). Anulación de la potencia mixta completa
  Re⟨r,Ry⟩ + Re⟨ℓ,Qy⟩ + Re⟨d,y⟩ (5.3): OPEN, terminal.
- **Dónde se detuvo.** (2.4) es tautología del radical; (5.3) es la reciprocidad exterior de R161_022.
- **Corrección posterior.** Se autocorrige (retira (3.2) y (4.4) de su propia primera versión). 064–065.
- **Cotejo.** U2: sí, en la forma más explícita del tramo: contabilidad conjunta exacta de los bloques primitivo,
  de Tate y exterior de la compresión. U1, U3, U4, U5: no.

## R161_064 — Potencia mixta bien tipada y concomitante de soporte

- **Objeto.** y_N = Z_N* g_N, Tau P y_N = j_N (collar). Re⟨Af, y_N⟩ = Re⟨r, j_N⟩ + Re⟨ℓ,(I−P)y_N⟩ (1.3), y con
  d = w − Af se reconstruye Re⟨y_N, w⟩ (1.4). Concomitante de soporte K_P(S;g,w) = ⟨Pg,PSw⟩ − ⟨PS*g,Pw⟩ =
  ⟨Pg,PSQw⟩ − ⟨Qg,SPw⟩ (2.2). Objetivo (4.2): C_{M,N,T}(f) = ε Re⟨v_f, j⟩ + D^Γ + ½‖P_R^ext C_log g + εg‖² + o(1),
  y (4.3) C = o(1) en el radical.
- **Afirmaciones.** Tipado mixto del collar: PROVED. (2.2): PROVED. Identificación de su bloque de rango finito
  con el collar; (4.2); (4.3): OPEN.
- **Dónde se detuvo.** Ni el álgebra de proyecciones ni PC-ren dan (4.2); la colocación de Tau ocurre antes de la
  síntesis en (3.1) y después en el collar.
- **Corrección posterior.** R161_065 prueba K_P = ⟨g,[P,S]w⟩ y retira (4.2)–(4.3) como consecuencias.
- **Cotejo.** U2: sí (concomitante de compresión; colocación de Tate). U1, U3, U4, U5: no.

## R161_065 — El concomitante de soporte es el conmutador exterior ya auditado

- **Objeto.** K_P(S;g,w) = ⟨g, [P,S] w⟩ (1.2).
- **Afirmaciones.** (1.2): PROVED (una línea; sostenido). Colisión con R161_042–044 y 057: PROVED. Expansión
  positiva de 064 (4.2): retirada. Ruta lagrangiana/hermítica nueva a partir de las hipótesis actuales: agotada
  (lista de cuatro variantes en §3). Falta un teorema aritmético exterior adicional que excluya el
  contramodelo de tres bloques de R161_050, por ejemplo Re⟨g, P_R C_log g + εg⟩ = 0.
- **Dónde se detuvo.** Cierre de familia (061–065): forma alternada (diagonal nula); potencia hermítica diagonal
  (tipo de collar equivocado R Z f en vez de Tau P Z* g); potencia mixta bien tipada (reconstruye la tautología de
  R161_023); defecto de orden finito (= [P,S]). «Agotada» se apoya en el contramodelo de R161_050 para el paquete
  formal (PC-ren, radicalidad, paridad, unitariedad, compresión); para la clase así declarada es NO-GO; no
  excluye entradas aritméticas adicionales.
- **Corrección posterior.** Ninguna.
- **Cotejo.** U2: sí, y es el registro de fracaso: toda reescritura de Green/potencia sobre la compresión, la
  fuga y el bloque de Tate vuelve a [P,S] o a la correlación extremal. U3: sí (cierra la forma alternada y la
  hermítica diagonal). U1, U4, U5: no.

## R161_066 — Selección de la nueva entrada aritmética

- **Objeto.** Observación de Laurent orientada R_{m,r}[G] = (1/2πi)∮_{|s−s_m|=r} G(s) ds, s_m = 2m+1;
  R_{m,r}[ζ W_ε^0] = ζ(s_m) K_F(2m+½) (3.2); energía E_T^Laur(F) = Σ ω_m |R_{m,r_m}[ζW_ε^0]|² con
  ω_m = 2^{−m}(2m+½)e^{−2(2m+½)T}/|ζ(2m+1)|², igual a D_T^pole(F). Ley OAL (4.1): germen finito orientado cuyas
  energías de contorno → 0 en el radical.
- **Afirmaciones.** Selección del blanco más pequeño (eliminabilidad de polos de Γ en s = 2m+1): completada.
  Realización por contorno de la energía de Γ: PROVED relativo a R161_025. Distinción del contramodelo de tres
  bloques: «sólo a nivel de tipado». OAL: OPEN. §2: la inversión local de Möbius no es la entrada nueva
  (colisión con P121_CMO_SOURCE_MATRIX_NO_GO: tras eliminación la conexión logarítmica tiene diagonal raíz nula
  y queda el bloque anular de transporte; la variante de regularidad de extremo produce la cola global de Möbius
  sin control).
- **Dónde se detuvo.** OAL retirada por 067.
- **Corrección posterior.** R161_067.
- **Cotejo.** U4: sí, tangencialmente: registra que la inversión de Möbius local (no los pesos truncados
  c_N(k)) no da la ley; no examina el resto de casi-coincidencias con pesos de Möbius truncado. U1, U2, U3, U5: no.

## R161_067 — Dicotomía para observaciones de Laurent finitas orientadas

- **Objeto.** Caso A (sin factor Γ): el germen es holomorfo dentro de C_m y su contorno es 0 para todo M, N.
  Caso B (con factor Γ): residuo ζ(s_m) K_F(2m+½) independiente de M, N (1.4). Forma requerida de una entrada
  genuina (3.1): Q^out − Q^in = Σ_{m≤L} ω_m|K_F(2m+½)|² + R, con el lado izquierdo ≤ 0 por radicalidad, R ≥ 0
  o → 0 uniformemente, y Q^out, Q^in no definidos por los momentos.
- **Afirmaciones.** Dicotomía: PROVED (Cauchy; sostenido). OAL: retirada (circular o topológicamente
  equivalente al objetivo). Ley de comparación cuadrática (3.1): OPEN. §3 afirma «una entrada genuina no puede ser
  un germen lineal ni un límite de contorno»: ARGUED; 080 §5 dice que no justifica la exclusión general.
- **Corrección posterior.** R161_080 §5 (la exclusión de todo enfoque lineal en §3 no está justificada por el
  cálculo).
- **Cotejo.** U1–U5: no. (La forma (3.1) es una comparación cuadrática con resto, sin objeto.)

## R161_068 — Identidad de observabilidad Gamma–Euler

- **Objeto.** (R_δ F)_m = √a_m e^{−a_m(T+δ)} K_F(a_m); traslación τ_b F(t) = F(t−b), R_δ τ_{log n} = D_n R_δ,
  (D_n x)_m = n^{−a_m} x_m. Generador L = Σ Λ(n) n^{−1/2} τ_{log n}; R_δ L F = C_ζ R_δ F, c_m = −ζ′/ζ(2m+1) > 0.
  Teorema 2.1: Re⟨R_δ F, R_δ L F⟩ = Σ_m c_m a_m e^{−2a_m(T+δ)} |K_F(a_m)|² ≥ 0, nulo sii F = 0.
- **Afirmaciones.** Teorema 2.1: PROVED (para la observación de Laplace completa; sostenido en esa convención).
  (4.2) pareo radical primitivo: PROVED pero no contiene la energía. (4.4): retirada (factor de operador
  equivocado: el pareo sin proyectar es ⟨R_δ L A_∞ F, R_δ F⟩). Factorización sin división (5.1)
  L*G_δ = A_∞ K_δ + Pi_T U_δ + V_δ(I − P_T): OPEN. La nota de encabezado (añadida por 070) declara que §§4–5 no
  establecen identidades adjuntas admisibles (dominios distintos) y que la novedad en el corpus no está
  establecida.
- **Dónde se detuvo.** La radicalidad inserta A_∞ en el vector observado; quitarlo o invertirlo es circular.
- **Lectura propia.** La positividad c_m > 0 es lineal en el peine y vale para cualquier peso no negativo no
  nulo (lo prueba 072 §2): el detector no distingue Λ.
- **Corrección posterior.** R161_070 (dominios), R161_072 (sustitución de coeficientes).
- **Cotejo.** U1: no (Λ entra linealmente vía −ζ′/ζ; no hay término de grado ≥ 2). U2: sí, débilmente (en §5 la
  factorización lleva bloques Pi_T y (I − P_T)). U3, U4, U5: no.

## R161_069 — Una observación fiel no se factoriza formalmente por el operador de modo nulo

- **Objeto.** Lema: si C ⪰ 0 es fiel y C = AK como forma, entonces Af = 0 ⇒ f = 0. Aplicación a
  C_δ = L* R_δ* R_δ: una identidad C_δ = A_∞ K_δ excluiría todo modo nulo.
- **Afirmaciones.** Lema abstracto: correcto como lema condicional. La aplicación al primer contacto: inválida
  según la corrección de encabezado de 070 (el primer contacto concierne a ker H_T de la compresión primitiva,
  no a ker A_∞; además falta la corrección de dominio). «Imposibilidad de derivar la factorización»: retirada por
  070; «equivalencia en fuerza no es circularidad».
- **Corrección posterior.** R161_070 (encabezado de 069 y §4 de 070, con el contraejemplo A = [[0,1],[1,0]],
  P = diag(1,0): A invertible pero PAP = 0 en el rango de P).
- **Cotejo.** U2: sí, en la corrección (la distinción núcleo global / núcleo comprimido es el efecto de la
  compresión a la ventana). U1, U3, U4, U5: no.

## R161_070 — Detector Gamma–Euler finito tipado y collar exacto

- **Objeto.** Sobre L²(I), I = (−T,T): (Rf)_m = b_m ∫_I e^{−a_m t} f, b_m = √a_m e^{−a_m(T+δ)} (Hilbert–Schmidt);
  L_N = Σ_{2≤n≤N} Λ(n) n^{−1/2} V_{log n}, c_{m,N} = Σ_{n≤N} Λ(n) n^{−(a_m+½)}, D_N = diag(c_{m,N}),
  C_N = R* D_N R. Collar exterior derecho (E_N f)_m = b_m Σ Λ(n) n^{−(a_m+½)} ∫_{max(−T,T−log n)}^T e^{−a_m u} f(u) du.
  Identidad R B_N = D_N R − E_N (2.1), B_N = P L_N P; C_N = (G B_N + B_N* G)/2 + (R*E_N + E_N*R)/2 (2.2);
  ⟨f, C_N f⟩ = Re⟨Rf, R B_N f⟩ + Re⟨Rf, E_N f⟩ (2.3). Estabilización E_{N′} − E_N = (D_{N′} − D_N) R para
  N′ ≥ N ≥ e^{2T} (3.1). Comparación suficiente (4.1): 2Re a_T(f, Kf) = ⟨f, C_N f⟩ + Q(f), Q ≥ 0, Kf primitivo.
- **Afirmaciones.** C_N positivo, traza, fiel (completitud de momentos R161_019); convergencia en norma de traza;
  (2.1), (2.2), (3.1): PROVED (sostenidas; cambio de variable y corte en T). (4.1): OPEN. Sin signo para el
  pareo de collar Re⟨Rf, E_N f⟩.
- **Dónde se detuvo.** No construye K ni Q. Los primos inactivos (n ≥ e^{2T}) viven enteramente en el collar:
  descartar el término exterior descarta toda su contribución.
- **Corrección posterior.** 071–072 explotan (2.1); 072 muestra que la construcción no distingue Λ.
- **Cotejo.** U2: sí (fuga exacta de las traslaciones truncadas por la compresión: E_N es la parte exterior de
  R L_N; observación de rango finito tras truncar m). U1: no (lineal en Λ). U3, U4, U5: no.

## R161_071 — Prueba de paridad y balance exacto Gamma–Euler

- **Objeto.** R_L (m ≤ L), G_L = R_L* R_L, S_L = G_L + J G_L J, test h_L = Pi S_L f (admisible en el dominio
  de forma logarítmico de Γ, pues su núcleo es suma finita de exponenciales). Con N ≥ e^{2T}, B = P L_N P, la
  ecuación de primer contacto (𝓜 − B − B*) f = r (r en Tate) da 0 = Re m_T(f, S_L f) − Re⟨(B+B*)f, S_L f⟩ −
  Re⟨r, S_L f⟩ (1.1). Balance (2.3): 0 = 2c_{N,L} + Q_{N,L}, con c = ⟨R_L f, D R_L f⟩ (detector positivo) y
  Q = 2v − 2e − Re m_T(f, S_L f) + Re⟨r, S_L f⟩ (2.4). Observación hacia atrás truncada (3.1).
- **Afirmaciones.** Test admisible, balance (2.3), fórmula (3.1): PROVED sobre el dominio de forma importado.
  Signo de Q en el radical: OPEN. Si Q ≥ 0 para todo L, f = 0.
- **Dónde se detuvo.** El signo de Q debe salir de los núcleos explícitos; ni la positividad de 𝓜 ni la de G_L ni
  la paridad lo dan.
- **Corrección posterior.** R161_072 (Q es la ecuación reformulada: Q = −2c en primer contacto); R161_081 (Q no
  puede ser ≥ 0 en todo el espacio primitivo).
- **Cotejo.** U2: sí (compresión P L_N P; collar; término de Tate r; rango finito L). U1: no. U3: no. U4, U5: no.

## R161_072 — Recombinación del balance y prueba de coeficientes

- **Objeto.** Antes de usar el primer contacto: Q = −2c − Re a_T(f, S_L f) + Re⟨r, S_L f⟩ (1.1). En primer
  contacto Q = −2c exactamente. Sustitución Λ(n) → w_n ≥ 0 arbitrarios: R_L B_N^w = D^w R_L − E^w textualmente;
  detector fiel si algún w_n > 0 (basta w_2). Para N′ ≥ N ≥ e^{2T}: ΔQ = −2Δc.
- **Afirmaciones.** (1.1): PROVED (sostenido). Prueba de coeficientes: la positividad y fidelidad del detector no
  distinguen el peine de von Mangoldt: PROVED. Cola inactiva exactamente balanceada: PROVED. «No es teorema de
  imposibilidad universal» (declarado).
- **Dónde se detuvo.** El test Pi(G_L + J G_L J) f es una reformulación exacta sin nueva restricción. Hace falta
  una cota que use el núcleo Γ junto con las relaciones aritméticas de los coeficientes.
- **Corrección posterior.** Ninguna; 081 la refuerza.
- **Cotejo.** U1: sí, como registro negativo pertinente: la construcción contiene valores aritméticos pero usa Λ
  sólo linealmente; sobrevive a todo peso w ≥ 0 (en particular a cΛ y a a_P), luego no tiene la cláusula de
  ruptura; no introduce término de grado ≥ 2. U2: sí (collar, rango finito). U3, U4, U5: no.

## R161_073 — Inversa estabilizada de momentos

- **Objeto.** H = H_T ⪰ 0 con resolvente compacta; R : ℋ → C^L inyectiva en ker H (existe por R161_046, no
  efectivo). S = H + R*R ≥ αI, M = R S^{−1} R* contracción positiva. Identidad
  ⟨y,(I−M)y⟩ = ‖y − Ru‖² + ‖H^{1/2}u‖², u = S^{−1}R*y (2.1). ker H ≅ ker(I − M); ker H = {0} ⟺ λ_max(M) < 1 (3.1).
- **Afirmaciones.** Todo PROVED bajo las hipótesis importadas (sostenido: argumento estándar de perturbación de
  rango finito). Cota estricta λ_max(M) < 1: OPEN.
- **Dónde se detuvo.** M ≤ I es todo lo que da (2.1); la matriz finita codifica la inversa completa S^{−1}; no hay
  cota uniforme en T.
- **Corrección posterior.** 074 da el certificado de residuo.
- **Cotejo.** U2: sí (perturbación de rango finito R*R del operador comprimido). U3: no. U1, U4, U5: no.
  Nota: (2.1) es una identidad «forma = suma de cuadrados» para I − M, pero genérica (vale para todo H ⪰ 0).

## R161_074 — Certificado superior por residuo para la matriz estabilizada

- **Objeto.** U aproximado, E = R* − SU, M_0 = RU + U*R* − U*SU: M = M_0 + E* S^{−1} E (1);
  M_0 ≤ M ≤ M_0 + α^{−1} E*E (2); certificado suficiente I − M_0 − α^{−1}E*E > 0 (3). Ejemplo 2×2:
  H = [[1,−1],[−1,1]], R = [1,0], U = (½,0)ᵗ: M = 1, M_0 = ½, E*S^{−1}E = ½.
- **Afirmaciones.** (1)–(3) PROVED; ejemplo verificado exactamente (sostenido). Galerkin sólo da cota inferior de
  M. Ningún certificado aritmético construido.
- **Dónde se detuvo.** Requiere α cuantitativo, columnas admisibles y cota del residuo en cada ventana; un
  cómputo en ventanas elegidas no da todo T.
- **Cotejo.** U2: sí (rango finito). U1, U3, U4, U5: no.

## R161_075 — Tres sentidos del producto cero completado

- **Objeto.** Distingue: producto L² (multiplicación maximal por la función en la recta, inyectiva); producto
  distribucional (la multiplicación anula deltas en ceros reales); identidad meromorfa
  d_Γ(s) + ζ′/ζ(s) + ζ′/ζ(1−s) ≡ 0.
- **Afirmaciones.** Inyectividad L² (2.1), contraejemplo distribucional (3.1), distinción meromorfa: PROVED. La
  exclusión de R161_018 («todo límite lineal de PC es un operador cero tautológico») no queda establecida por su
  argumento.
- **Dónde se detuvo.** Hay que dar portadores y límites compatibles para A_M f, S_N^ren A_M f y los puertos
  separados. Usa una equivalencia externa / reducción a ceros en §§2–3 (registrado sin desarrollar).
- **Corrección posterior.** Corrige a R161_018 (y, por arrastre, lo que en 099 se apoya en 018).
- **Cotejo.** U1–U5: no.

## R161_076 — Límite de Weil local físico y dominio de Poisson

- **Objeto.** f ∈ C_c^∞(−T,T), A_M f se estabiliza en |t| ≤ K para M ≥ e^{K+T}; límite A_loc f en D′(ℝ);
  convergencia en X_η = L²(e^{−2η|t|}dt), η > ½. Composición S_N A_M f estable en [−K,K] si M ≥ N e^{K+T} (3.1).
  El continuo C_N h(t) = e^{−t/2} ∫_{−∞}^{t+log N} e^{y/2} h(y) dy no está definido en X_η (ejemplo
  h = 1_{y<0} e^{−y/2}).
- **Afirmaciones.** Estabilización local, convergencia en X_η, (3.1), insuficiencia del espacio ponderado: PROVED
  (sostenido). Límite del producto renormalizado en fuentes de primer contacto: OPEN.
- **Cotejo.** U2: no en sentido estricto (análisis de dominios). U1, U3, U4, U5: no.

## R161_077 — Acción del continuo módulo Tate

- **Objeto.** J_f(x) = ∫_{−∞}^x e^{u/2} f; C_N L_M f(t) = e^{−t/2} Σ Λ(n) J_f(t + log N − log n) (1.1),
  C_N L_M* f = e^{−t/2} Σ Λ(n)/n J_f(t + log N + log n) (1.2). Ancla inferior C_{N,a}; la diferencia de dos anclas
  está en la recta de Tate negativa e^{−t/2} (2.1); Pi_K C_{N,a} h no depende del ancla (2.2). Límite proyectado
  a N fijo (3.2).
- **Afirmaciones.** Todo PROVED a N fijo y para fuentes lisas compactas (sostenido). El escalar quitado no se
  prueba nulo; sin cota uniforme en N.
- **Cotejo.** U2: sí, menor: la proyección Pi_K fuera de Tate elimina una ambigüedad de rango uno. U1, U3, U4, U5: no.

## R161_078 — Convergencia de la cola renormalizada en fuentes lisas

- **Objeto.** Con |ψ(x) − x| ≤ C x e^{−c√log x} (CITED, cota no reprobada) y ∫e^{−u/2} f = 0: corriente de Euler
  derecha l(t) = −∫E(x) d_x[x^{−1/2} f(t − log x)], |l| + |l′| ≤ C_f e^{t/2 − c′√t} (2.1); Σ_{n≤N} q_t(n) −
  ∫_1^N q_t converge uniformemente en |t| ≤ K (3.2); S_N h − C_{N,a} h converge localmente uniforme.
- **Afirmaciones.** PROVED relativo a la cota citada del término de error (sostenido). Constantes dependientes de
  derivadas de f; no se extiende a radicales; valor del límite no identificado.
- **Lectura propia.** La entrada es una cota de densidad (error de ψ), genérica para cualquier peso con el mismo
  error; no lleva signo.
- **Cotejo.** U1–U5: no.

## R161_079 — Renormalización débil sobre L² primitivo

- **Objeto.** T_N h = Σ_{n≤N} n^{−1/2} h(t + log n) − ∫_1^N x^{−1/2} h(t + log x) dx; para f ∈ L²([−T,T]) con
  ∫e^{−u/2} f = 0, T_N A_loc f converge en D′ con |⟨(T_B − T_A)A_loc f, φ⟩| ≤ C ‖f‖_2 p_J(φ) ρ(A) (1.3). Prueba
  por convolución k = f * φ̌ (las derivadas pasan al test). Continuo módulo Tate vía (∂_t + ½)v = h.
- **Afirmaciones.** Teorema: PROVED con la cota citada del término de error (sostenido). Transporte al grafo de
  Hilbert y anulación: no probados. Advierte que suavizar f no conserva H_T f = 0.
- **Cotejo.** U2: no (sí advierte que la compresión no conmuta con la convolución). U1, U3, U4, U5: no. En §4 usa
  una equivalencia externa (un producto con la función zeta), sin desarrollar.

## R161_080 — Escape del polo y observación a dos escalas

- **Objeto.** h_R(t) = −k e^{at} 1_{t<−R}: residuo k en z = a para todo R, mientras h_R → 0 en D′, en L² y en
  todo Sobolev (versión lisa). Observación de Abel B_ε(h) = −ε∫e^{−(a−ε)t} h; límites no conmutan (2.1);
  truncada B_{ε,L} requiere εR → 0, εL → ∞ (3.2). Estimación condicional |B_{ε,L}(v) − k| ≤ |k|[1 − e^{−εT} +
  e^{−εL}] + ε C_a(r) (4.1).
- **Afirmaciones.** Fórmulas de escape, ejemplo Sobolev, cota (4.1): PROVED (sostenido; (4.1) es CONDITIONAL a
  la hipótesis de resto ponderado). No se aplica al defecto físico. §5: el cálculo no justifica la exclusión
  general de enfoques lineales de 067 §3.
- **Cotejo.** U1–U5: no.

## R161_081 — Prueba del signo de Q en autovectores de Weil

- **Objeto.** Extensión canónica de la forzante r_f por Riesz en el espacio de Tate; K_L = Pi S_L Pi;
  Q_{N,L}(f) = −2c_{N,L}(f) − Re a(f, K_L f) (1.1). Para Hf = λf, Jf = εf:
  Q_{N,L}(f) = −2 Σ_{m≤L} [d_{m,N} + λ] |(R_L f)_m|² (2.1).
- **Afirmaciones.** (1.1), (2.1): PROVED bajo las hipótesis de forma/operador (sostenido). Q ≥ 0 universal en el
  espacio primitivo: descartado (NO-GO con clase: toda prueba que combine sólo H ⪰ 0 con pesos Γ/Euler
  positivos da el signo opuesto en autovectores con λ ≥ 0). La desigualdad específica del radical: OPEN, no
  circular, pero exige una consecuencia adicional de las ecuaciones del estado de igualdad.
- **Falsificador.** Cualquier autovector de paridad definida con λ ≥ 0 y R_L f ≠ 0 en una ventana no negativa.
- **Cotejo.** U2: sí (compresión primitiva, Tate, rango finito). U3: no. U1, U4, U5: no.

## R161_099 — Síntesis de la fase 161, primera construcción

- **Objeto.** Resume 001–045 (no cubre 046–081). Identidad (PC): S_N A_M Fcal = {X,E_N} − L_M* E_N − J H_{M,N} −
  H_{M,N} Fcal, con H_{M,N} = L_M S_N − K_N; renormalización S_N^ren = S_N − C_N(D), C_N(s) = N^{1−s}/(1−s).
  Hitos: cuadrado canónico ciego al signo (invariante por A_M → −A_M); pesos no negativos no telescopan la cola
  (h_N(p) = log p para N < p y 0 después); puertos exteriores y discrepancias unilaterales (005–006); excedente
  Sonin–Gamma ⟨D_Γ g,g⟩ − 2T‖g‖² = 2∫_T^∞(t−T)|g|² ≥ 0 (014); energía de polos D_T^pole y forma de Hankel
  B^Γ_{T,δ} con núcleo k_Γ^+(v) = Σ e^{−(2m+½)v} (025–026); imagen (027–028); variancia orientada (030):
  (log k)/2 Σ_d Λ(d)(‖x_d^+‖² + ‖x_d^−‖²) − ‖Σ_d Λ(d) m_d‖² = (log k) Σ_d Λ(d)‖r_d‖² + ½ Σ_{d,e} Λ(d)Λ(e)‖m_d − m_e‖²;
  vectores de camino (031), conversión de signo de Tate ε⟨v, G_T C v⟩ = ‖r‖² (032); retirada por interferencia
  cruzada en k y «salida A»: dilatación de Parseval/Naimark explícita (033); diagonalización por canales de
  razón y producto de la fase 106 y fuga coherente ‖(I − P_T) Σ_{k≤N}(log k) d_k P_T F‖² (034); paralelogramo de
  dos estados ½(‖U_N f‖² + ‖V_N f‖²) − ¼‖(U_N + V_N) f‖² = ¼‖(U_N − V_N) f‖² (035); contramodelo C² (038);
  equivalencia terminal (039); identificación de las dos historias exteriores (040); orientación (041);
  identidad mixta (042); Tate de paridad opuesta nula (043); pieza primitiva tautológica (044); Brown–Halmos y
  anomalía de determinante (045).
- **Afirmaciones.** Veredicto declarado: OPEN; «PARTIAL_NEW + STRUCTURAL_NEGATIVE». Usa una equivalencia externa
  / reducción a ceros en los resúmenes de 007, 008, 036, 037 (registrado sin desarrollar).
- **Lectura propia.** La síntesis afirma en §4 (resumen de 018) que todo límite lineal de (PC-ren) es tautológico;
  R161_075 dice que esa exclusión no está establecida. La síntesis no fue actualizada. También describe 019 como
  cierre de la mitad de rigidez de rango, y 024–025 la debilitan; eso sí está registrado dentro de la síntesis.
- **Cotejo.** U1: sí: la identidad de variancia de 030 es de grado dos en Λ (Λ(d)Λ(e)‖m_d − m_e‖²), entra
  sumando y usa Σ_{d|k}Λ(d) = log k; registrado su fracaso en 031–033: los vectores de camino no dependen de d (la
  variancia transversal es idénticamente nula) y la realización física es la suma coherente en k, cuya norma
  contiene la Gram cruzada Σ_{k≠l}(log k)(log l)/√(kl) Re⟨Δ_k F, Δ_l F⟩ que la suma directa omite. U2: sí: fuga
  coherente de 034, identificación de historias exteriores de 040, contabilidad Tate 032/043. U3: sí, menor: G_T C
  indefinida, positiva sólo en la recta de paridad (032). U4: no (la 121/CMO de Möbius local sólo se menciona en
  §4 resumen de 004). U5: sí: la «salida A» de 033 (dilatación explícita de Parseval/Naimark suministrada por
  Poisson) se enuncia y no se construye; 035 la declara innecesaria tras el paralelogramo coherente, y 038 muestra
  que (PC), radicalidad, polarización y paridad no implican la saturación (contramodelo en C²).

---

## Resumen

### (a) Piezas PROVED reutilizables

1. Identidad de Green mixta en cuatro bloques (1.4) de R161_057 §1 y el conmutador de soporte PZ − ZP = PZQ − QZP
   (§4).
2. Doble conmutador radical ⟨f,[B*,[H,B]]f⟩ = ⟨Bf,HBf⟩ + ⟨B*f,HB*f⟩ ≥ 0 y su igualdad por reflexión
   (R161_058 §§1–2).
3. Forma en bloques del par conmutante comprimido [H,B] = Ȳ*X − X*Y (R161_059 §1) y anticonmutador comprimido
   {H,B} = P{A,Z}P − Ȳ*X − X*Y sin hipótesis de conmutación (R161_062 §3).
4. Descomposición de tres bloques primitivo/Tate/exterior sin término mixto (R161_063 §2) y pareo mixto bien
   tipado (§5, (5.2)).
5. K_P(S;g,w) = ⟨g,[P,S]w⟩ (R161_065 §1).
6. Dicotomía de Laurent finita (R161_067 §1).
7. Detector Gamma–Euler fiel C_N = R*D_N R, collar exacto R B_N = D_N R − E_N, identidad hermítica y ley de
   estabilización (R161_070 §§1–3); observación hacia atrás truncada (R161_071 §3).
8. Balance exacto 0 = 2c + Q y su recombinación Q = −2c − Re a_T(f, S_L f) + Re⟨r, S_L f⟩ (R161_071 §2,
   R161_072 §1); fórmula espectral Q = −2Σ[d_{m,N} + λ]|(R_L f)_m|² (R161_081 §2).
9. Inversa estabilizada S = H + R*R, identidad ⟨y,(I−M)y⟩ = ‖y − Ru‖² + ‖H^{1/2}u‖², ker H ≅ ker(I−M)
   (R161_073); certificado de residuo M = M_0 + E*S^{−1}E (R161_074).
10. Límite local de Weil y convergencia en X_η (R161_076); continuo módulo Tate (R161_077); convergencia
    renormalizada lisa (R161_078) y débil sobre L² primitivo (R161_079), ambas relativas a la cota citada del
    término de error de ψ.
11. Escape del polo y extracción a dos escalas (R161_080; (4.1) condicional).
12. Distinción L² / distribucional / meromorfa del producto cero (R161_075).

### (b) Cierres con clase y falsificador

- Familia lagrangiana/hermítica de borde (R161_061–065): forma alternada (diagonal nula; el grafo es isótropo
  para todo vector); potencia hermítica diagonal (collar mal tipado); potencia mixta bien tipada (reconstruye la
  tautología de R161_023); defecto de orden finito (= [P,S]). Clase: reescrituras construidas sólo con (PC-ren),
  radicalidad, paridad, unitariedad y compresión. Falsificador: contramodelo de tres bloques de R161_050 (y el
  de C² de R161_038 para la saturación).
- Doble conmutador + reflexión + Tate (R161_058–060): no da anulación; la sustitución literal de PC-ren
  reconstruye la correlación extremal.
- OAL (R161_066–067): circular (con Γ) o topológicamente equivalente al objetivo (sin Γ).
- Factorización de un detector fiel por el operador de modo nulo (R161_069): lema condicional; la aplicación
  quedó invalidada por 070 (núcleo global ≠ núcleo comprimido; contraejemplo 2×2).
- Detector Gamma–Euler como portador de signo (R161_072): falsificador = cualquier peso w ≥ 0 con algún w_n > 0
  (en particular sólo w_2), que da un detector igualmente positivo y fiel.
- Q ≥ 0 en todo el espacio primitivo (R161_081): falsificador = autovectores de paridad definida con λ ≥ 0.
- Galerkin como certificado de λ_max(M) < 1 (R161_074): ejemplo 2×2 exacto.
- Unitaria de fase como chorro crítico (R161_056): da la orientación media U + V, no U − V.

### (c) Explícitamente abierto, con su obstáculo

- Reciprocidad cuadrática de las dos discrepancias unilaterales con G_wrong (R161_057 (3.3)).
- Balance negativo «pareo mixto PC = −⟨f,[B*,[H,B]]f⟩ − D^Γ» (R161_058 (4.1)); ley de borde antisimétrica para
  los dos pareos de R161_060 (2.2).
- Anulación de la potencia mixta completa Re⟨r,Ry⟩ + Re⟨ℓ,Qy⟩ + Re⟨d,y⟩ (R161_063 (5.3)).
- Comparación cuadrática independiente Q^out − Q^in = Σ ω_m|K_F(2m+½)|² + R (R161_067 (3.1)).
- Factorización sin división L*G_δ = A_∞K_δ + Pi_T U_δ + V_δ(I−P_T) (R161_068 (5.1)); comparación
  2Re a_T(f,Kf) = ⟨f,C_N f⟩ + Q(f), Q ≥ 0, Kf primitivo (R161_070 (4.1)) — falta construir K y Q.
- Q_{N,L} ≥ 0 sólo en el radical (R161_071, R161_081): exige una consecuencia adicional de las ecuaciones del
  estado de igualdad que no valga para autovectores con λ ≥ 0.
- λ_max(M) < 1 con certificado uniforme en T (R161_073–074).
- Límite del producto renormalizado sobre fuentes de primer contacto, uniforme en N, y su valor (R161_076–079);
  extracción de residuos con resto ponderado (R161_080).
- Teorema aritmético exterior que excluya el contramodelo de tres bloques, p. ej. Re⟨g, P_R C_log g + εg⟩ = 0
  (R161_065 §4).

### (d) Lo que ya recorre U1–U5 y por qué falló

- **U1.** La identidad de variancia orientada de grado dos en Λ con Σ_{d|k}Λ(d) = log k (resumida en R161_099,
  entrada 030) entra sumando; falló porque los vectores de camino físicos no dependen de d (031: variancia
  transversal nula) y la realización física es la suma coherente en k, con Gram cruzada no controlada (033); su
  diagonalización cae en los canales de razón/producto de la fase 106 (034). En el tramo propio, 068/070/072
  usan Λ sólo linealmente y 072 prueba que la construcción sobrevive a todo peso w ≥ 0.
- **U2.** Es la maquinaria central del tramo: compresión física P, bloques PZQ/QZP, fuga, operador de posición X,
  proyección primitiva, bloque de Tate K_T = G_T C, rango finito R_L, perturbación R*R. Todas las
  reescrituras (057, 059, 062–065) terminan en el conmutador [P,S] o en la correlación extremal de R161_023;
  las identidades con collar (070–072) son la ecuación de primer contacto reescrita (Q = −2c); la de rango finito
  (073) reduce a λ_max(M) < 1 sin cota. La fuga coherente ‖(I − P_T)Σ(log k)d_k P_T F‖² (034) y la contabilidad
  conjunta con Tate quedaron como blanco sin identidad que dé su saturación.
- **U3.** Formas indefinidas en el borde doble: simpléctica Ω (061, retirada: todo vector neutro) y hermítica
  B(b,b′) = ⟨η,ξ′⟩ + ⟨ξ,η′⟩ (062, usada sólo en la diagonal; tipo de collar equivocado, 063). K_T = G_T C es
  indefinida y sólo positiva en la recta de paridad (032). No se estudió ningún vector neutro no radical.
- **U4.** No recorrido en este tramo. Sólo aparece la inversión de Möbius local (066 §2, colisión con
  P121_CMO_SOURCE_MATRIX_NO_GO), no los pesos truncados c_N(k).
- **U5.** La «salida A» (dilatación explícita de Parseval/Naimark, 033) se enunció y no se construyó; 035 la
  reemplazó por el paralelogramo coherente y 038 mostró que (PC) + radicalidad + polarización + paridad no
  implican la saturación. La colligación unitaria finita (052–055) se conserva como transporte pero su tangente
  da la media, no la diferencia (056).

### (e) Inconsistencias entre memos

- R161_099 no cubre 046–081 y conserva la lectura de 018 («todo límite lineal de PC-ren es tautológico»), que
  R161_075 §5 declara no establecida.
- R161_067 §3 afirma que una entrada genuina no puede ser lineal; R161_080 §5 dice que ese cálculo no justifica
  la exclusión general.
- R161_068 §§4–5 y R161_069 §2 confunden dominios de observación y núcleo global con núcleo comprimido; lo
  corrigen las notas de encabezado escritas desde R161_070.
- R161_062 (4.1) usa 2⟨v_f, K_T v_f⟩ como potencia diagonal; R161_063 §3 lo declara mal tipado.
- R161_064 (4.2)–(4.3) se enuncian como objetivo «de forma única no circular»; R161_065 los retira como
  reformulación del teorema faltante.
- R161_065 §3 dice «agotada» la ruta; es agotamiento relativo a las hipótesis formales actuales, no un NO-GO
  universal (la propia memo lo matiza en §4).
- R161_072 y R161_081 declaran no ser teoremas de imposibilidad universal; R161_081 sí excluye Q ≥ 0 en todo el
  espacio primitivo.

### (f) Archivos leídos (lectura completa con Read)

Contexto de la fase 212: README.md, OBJECT_SPEC.md, LEDGER.md, BRIEF_CONSTRUCTOR.md, REVIEW_003.md.

Tramo: R161_056, R161_057, R161_058, R161_059, R161_060, R161_061, R161_062, R161_063, R161_064, R161_065,
R161_066, R161_067, R161_068, R161_069, R161_070, R161_071, R161_072, R161_073, R161_074, R161_075, R161_076,
R161_077, R161_078, R161_079, R161_080, R161_081, R161_099 (662 líneas, leído en dos llamadas). Veintisiete
archivos, todos leídos hasta la última línea. No existen R161_082 … R161_098.
