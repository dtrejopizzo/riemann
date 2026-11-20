# Anexo: lectura por archivo de la fase 161, tramo R161_028 – R161_055

Lectura completa de los 28 archivos del tramo, en orden. Notación de las memos: τ_a f(t) = f(t+a);
J f(t) = f(−t); 𝓕 (Fcal) la transformada de Fourier aditiva logarítmica, que en Mellin actúa como
reflexión con multiplicador unimodular u = u_∞; X = M_t (multiplicación por t); M = X + 𝓕X𝓕 (multiplicador
Gamma); S_N = Σ_{n≤N} n^{−1/2}τ_{log n}; C_N la contrapartida continua (polar) de Euler–Maclaurin;
S_N^ren = Z_N = S_N − C_N; L_M = Σ_{d≤M} Λ(d)d^{−1/2}τ_{log d}; K_N = Σ_{k≤N}(log k)k^{−1/2}τ_{log k}
= −[X, S_N]; H_{M,N} la cola de hipérbola (K_N = L_M S_N − H_{M,N} para M ≥ N); E_N = S_N𝓕 − JS_N
(defecto de Poisson); (PC) / (PC-ren) la identidad finita de Poisson–Chebyshev y su versión renormalizada;
P = P_T proyección a la ventana [−T, T]; Π_T proyección primitiva; Tate: φ_± = e^{±t/2}.
«Primer contacto» = vector radical primitivo hipotético F ≠ 0 de paridad ε (JF = εF) en la ventana crítica.
Etiquetas: se registra la que la memo se da; cuando la lectura no la sostiene, se dice aparte.

Varias memos (036, 037) trabajan con la función zeta, su ecuación funcional y, en 036, con la evaluación
en sus ceros; se registra neutralmente como «usa la función completa y su ecuación funcional / usa una
evaluación en ceros» sin desarrollarlo. Varias memos (039, 051) enuncian que su objetivo terminal «tiene la
fuerza lógica de cerrar la fila D» relativo a la reducción de primer contacto importada: es una
equivalencia interna de la arquitectura de la fila D, no con ningún enunciado externo.

---

## R161_028 — La capa polar de Euler–Maclaurin es exactamente la imagen exterior

Objeto. N = e^a; C_a(s) = e^{a(1−s)}/(1−s); en espacio físico (C_aF)(t) = e^{−t/2}∫_{−∞}^{t+a} e^{y/2}F(y)dy;
con (VF)(t) = e^{−t/2}∫_{−∞}^t e^{y/2}F, C_a = e^{a/2}τ_aV y (1.5) ∂_aC_a = e^{a/2}τ_a.
Si supp F ⊂ [−T,T] y el momento de Tate positivo ∫e^{y/2}F = 0, entonces supp C_aF ⊂ [−T−a, T−a]; con
a = 2(T+δ), supp ⊂ [−3T−2δ, −T−2δ] (intervalo imagen de R161_027). Operador imagen M_{T,δ} = τ_aJ.
Teorema 3.1: si JF = εF, ∂_a(C_aF) = ε e^{a/2} M_{T,δ}F. Energía Gamma (4.1)–(4.2):
B^Γ = ⟨F, K_Γ^+ M_{T,δ}F⟩ = ε e^{−a/2}⟨F, K_Γ^+ ∂_a(C_aF)⟩; D^Γ_{T,δ} = −½∂_δ{…}.
Peine con corte continuo S_a = Σ_{n≤e^a} n^{−1/2}τ_{log n}, discrepancia Z_a = S_a − C_a: velocidad continua
−e^{a/2}τ_a entre nacimientos, saltos n^{−1/2}τ_{log n} en a = log n.
Afirmaciones. PROVED: (1.5), soporte (2.2)–(2.4), Teorema 3.1, (4.2) como reescritura, velocidades y saltos de
Z_a. Sostenidas (cálculos elementales comprobados). OPEN: L161.11, identidad «0 = 2D^Γ + D^Poisson_a,
D^Poisson_a ≥ 0» (6.1) en a = 2(T+δ) o tras promedio positivo en δ.
Detención. La derivada ordinaria de ‖S_a − C_a‖² contiene un término cruzado no controlado; la orientación
tendría que salir de (PC-ren) y de los saltos terminales de la hipérbola. Se corrige/precisa en R161_029.
Cotejo. U1 no. U2 sí, parcialmente: usa el soporte de la ventana y la ley de Tate (momento nulo) para ubicar
la capa polar fuera de la ventana; no construye fuga ‖(I−P)·‖². U3 no. U4 no. U5 no.

## R161_029 — Auditoría de signo de la discrepancia móvil

Objeto. N_f(a) = ‖Z_a f‖². Entre nacimientos (2.2) N_f′(a) = −2e^{a/2}Re⟨Z_a f, τ_a f⟩. Salto en a = log n:
(3.2) N_f(a_n+) − N_f(a_n−) = 2n^{−1/2}Re⟨Z_− f, τ_{log n}f⟩ + n^{−1}‖f‖². Familia primitiva
H_a = Π P Z_a^*Z_a P Π ⪰ 0; si F es radical, a_T(F, H_aF) = 0 para todo a.
Afirmaciones. PROVED / INDEFINIDO: (2.2) y (3.2). FALSE: monotonía de la discrepancia ordinaria (falsificador
NUMÉRICO: oscilación en `161_02_poisson_defect_probe.py`). RECHAZADO COMO TAUTOLÓGICO: derivar (4.2).
IDENTIFICADO: L161.11 = retroceso de Markov centrado en Tate invertido de R161_016. OPEN/TERMINAL: forma
cuadrática de dos orientaciones definida por la fuente que reemplace los términos cruzados por
2D^Γ + D^Poisson_a, D^Poisson ≥ 0, y se anule en primer contacto.
Detención. Los términos cruzados Re⟨Z_a f, τ_a f⟩ no tienen signo; ponderarlos con coeficientes de Chebyshev
positivos no lo resuelve. La radicalidad contra H_aF es la tautología de R161_023.
Cotejo. U1 no. U2 sí: H_a usa la compresión P y Π (palabras de tipo Q V Q), declarado tautológico; la expansión
de la proyección reintroduce los términos móviles de Tate y de borde exterior (fase 121). U3 no. U4 no. U5 no.

## R161_030 — Varianza orientada de divisores (la puerta algebraica)

Objeto. Hilbert H; k ≥ 2; w_d = Λ(d) para d | k; W_k = Σ_{d|k} w_d = log k. Dos vectores x_d^± por camino;
m_d = (x_d^+ + x_d^−)/2, r_d = (x_d^+ − x_d^−)/2.
Teorema 1.1 (PROVED):
  (W_k/2)Σ_d w_d(‖x_d^+‖² + ‖x_d^−‖²) − ‖Σ_d w_d m_d‖²
    = W_k Σ_d w_d‖r_d‖² + ½Σ_{d,e} w_d w_e‖m_d − m_e‖²,              (1.1)
con igualdad ⟺ x_d^+ = x_d^− y m_d = m_e para todo d, e activos. Prueba: paralelogramo
(‖x^+‖² + ‖x^−‖²)/2 = ‖m‖² + ‖r‖² y varianza ponderada W Σw‖m‖² − ‖Σwm‖² = ½ΣΣw_dw_e‖m_d − m_e‖².
Comprobado línea por línea: correcto. Observación de lectura: la identidad es genérica en los pesos
(vale para cualquier w ≥ 0 con W_k := Σw_d); Λ entra sólo al escribir W_k = log k.
Primo k = p: lado izquierdo = (log p)²‖x_p^+ − x_p^−‖²/4 (2.1): la fibra de un solo divisor conserva la
diferencia de orientaciones; se declara que esto evita la obstrucción de la diagonal raíz de
P121_CMO_SOURCE_MATRIX_NO_GO. Interpretación como varianza total Var X = E_D Var(X|D) + Var_D E[X|D] con
P(D = d | k) = Λ(d)/log k.
Puerta (4.2) (OPEN/TERMINAL): construir x_{k,d}^±(F) definidos por la fuente, cuya diferencia sea el defecto
de Poisson proyectado y cuya media ponderada sea el puerto coherente de Chebyshev, y probar la saturación
Σ_k[(log k)/2 Σ_dΛ(d)(‖x^+‖² + ‖x^−‖²) − ‖Σ_dΛ(d)m_{k,d}‖²] = 0 en primer contacto.
Afirmaciones. PROVED: (1.1), núcleo de igualdad, supervivencia en fibras primas. «PROVED ALGEBRAICALLY»: escape
de la diagonal raíz (sostenido sólo como álgebra; no hay realización). OPEN: realización por vectores de
(PC-ren) y saturación (4.2).
Detención. §5: (4.2) no se sigue de (1.1); afirmar que la radicalidad la anula repetiría R161_023 (la
radicalidad anula un test primitivo lineal, no un segundo momento arbitrario de la fuente).
Corrigen. R161_031 (realización por caminos), R161_033 (retira la realización de la norma de suma directa),
R161_035 (sustituye por la versión coherente).
Cotejo. U1 sí en la forma, no en el mecanismo: el término ½ΣΣ w_dw_e‖m_d − m_e‖² es de grado 2 en el peso y
entra SUMANDO; pero se anula (R161_031) por coherencia de las traslaciones τ_{log d}τ_{log e} = τ_{log k}, para
cualquier peso, no por Σ_{d|n}Λ(d) = log n. La identidad (1.1) es válida para todo vector de pesos (no lleva
signo propio de Λ). U2 no. U3 no. U4 no. U5 no (antecede a U5).

## R161_031 — Realización por caminos: colapsa la costura de divisores y sobrevive la de Poisson

Objeto. Para de = k y f en el núcleo común: x_{k,d}^−(f) = k^{−1/2}Jτ_{log k}f, x_{k,d}^+(f) = k^{−1/2}τ_{log k}𝓕f
(salidas de los dos términos no recombinados J L_M S_N y L_M S_N 𝓕 de (PC), por
Jτ_{log d}τ_{log e} = Jτ_{log k}). En fibras completas k ≤ N ≤ M, Σ_{d|k}Λ(d) = log k da
Σ_dΛ(d)x^∓ = k^{−1/2}(log k)·(Jτ_{log k}f, τ_{log k}𝓕f); sumando: JK_Nf y K_N𝓕f.
Como x^± no dependen de d, m_{k,d} − m_{k,e} = 0 y (1.1) de 030 da (3.2):
  (log k)/2 Σ_dΛ(d)(‖x^+‖² + ‖x^−‖²) − ‖Σ_dΛ(d)m_{k,d}‖² = (log k)²/(4k)‖τ_{log k}𝓕f − Jτ_{log k}f‖².
Comprobado: correcto (W_kΣΛ(d)‖r‖² con ‖r‖² = ‖Δ_kf‖²/(4k)). Δ_k = τ_{log k}𝓕 − Jτ_{log k};
D^orient_{M,N}(f) = ¼Σ_{2≤k≤N}(log k)²/k ‖Δ_kf‖² ≥ 0 (4.2) — suma directa, NO ‖K_N𝓕 − JK_N‖².
Forma esperada del cierre (5.2): 0 = 2D^Γ_{T,δ}(F) + D^orient_{M,N}(F) + boundary_{M,N,T,δ}(F), con
boundary = 0 en primer contacto (5.3) (OPEN).
Afirmaciones. CONSTRUIDO: x^±. PROVED: uso de Λ∗1 = log en fibras completas; colapso de la costura.
«DEFINIDO Y POSITIVO; REALIZACIÓN DE LA NORMA FUENTE OPEN»: (4.2). PROVED por 026–028: componente continua.
OPEN/TERMINAL: saturación de Tate cruzada.
Lectura: el veredicto inicial («los vectores requeridos están identificados») es correcto; la frase de §0
sobre realización completa la retira R161_033 (la propia memo ya remite a 033).
Detención. (PC-ren) contiene la síntesis coherente Σ_k, no la norma de suma directa; falta la
identidad de borde (5.3).
Cotejo. U1: el uso de Λ∗1 = log es lineal (síntesis de K_N); el término cuadrático en el peso desaparece por
coherencia, para todo peso. No es U1. U2 no (todavía sin compresión). U3 no. U4 no: dice explícitamente
«no se usa eliminación de Möbius». U5: plantea la necesidad (la norma de suma directa).

## R161_032 — La paridad vuelve positivo el bloque cruzado de Tate

Objeto. Base de Tate (φ_−, φ_+) = (e^{−t/2}, e^{t/2}) en L²(−T,T):
G_T = 2[[sinh T, T],[T, sinh T]] (Gram), C = [[0,1],[1,0]] (intercambio),
A_T^cross = G_TC = 2[[T, sinh T],[sinh T, T]]; G_T y C conmutan. Forzamiento de primer contacto
r = αφ_− + βφ_+, v = (α, β)ᵗ, Cv = εv (paridad PROVED en fase 121).
Teorema 2.1 (PROVED): ε⟨v, G_TCv⟩ = ⟨v, G_Tv⟩ = ‖r‖²_{L²(−T,T)}; para v = c(1, ε)ᵗ, ‖r‖² = 4|c|²(sinh T + εT) > 0.
Comprobado (∫_{−T}^T e^{∓t} = 2 sinh T, ∫1 = 2T). Corriente de collar (fase 121) j = (J_+, J_−)ᵗ = G_TCv;
(3.2) ε⟨v, j⟩ = ‖r‖². Defecto de dispersión (R161_021) X_T(F) = ‖g‖² + ε⟨g, C_log g⟩ = ½‖(I + εC_log)g‖².
Identidad candidata (4.2):
  0 = X_T(F) + ‖r‖² + D_T^orient(F) + 2D^Γ_{T,δ}(F),
suma de no negativos que forzaría X_T = 0, r = 0, D^orient = 0, D^Γ = 0.
Afirmaciones. PROVED: (2.2), (3.2), «compatibilidad condicional con el signo de dispersión». OPEN/TERMINAL:
la identidad de contabilidad de Green finita (4.2).
Detención. Falta derivar que la expansión de Green de (PC-ren) produce el concomitante con el signo
+ε⟨v, j⟩ (y no otro orden/signo) y la compleción cruzada en k. §5 prohíbe insertar X_T por definición o
inferir (4.2) de la radicalidad. R161_033 añade que D^orient (suma directa) no está realizado; R161_043
muestra que en el orden «fuente derivada» (Xf) el término de Tate tiene paridad opuesta y da 0, no ‖r‖².
Cotejo. U1 no. U2 sí: es exactamente la «contabilidad conjunta con el bloque de Tate (4.2)» que REVIEW_003
deja abierta; la memo la deja como OPEN/TERMINAL sin derivación; los obstáculos registrados son: signo de
aparición no derivado (033 §6), D^orient no realizado (033), paridad opuesta en el orden Xf (043). U3 sí,
de modo parcial: G_TC es indefinida en el plano de Tate completo (R161_023) y se vuelve positiva en la
recta de paridad; no es una forma de Kreĭn con vector neutro, es restricción a un subespacio
invariante. U4 no. U5 no.

## R161_033 — Hueco coherente / suma directa; salidas A y B

Objeto. Y_N(f) = Σ_{2≤k≤N}(log k)k^{−1/2}Δ_kf (diferencia coherente de JK_Nf y K_N𝓕f);
‖Y_N‖² = Σ_{k,l}(log k)(log l)(kl)^{−1/2}⟨Δ_kf, Δ_lf⟩ (1.3); D^orient_N = ¼Σ(log k)²/k‖Δ_kf‖² (1.4) es su
diagonal (salvo el factor ¼). H_N^src = ⊕_{2≤k≤N}H; análisis Af = ((log k)k^{−1/2}Δ_kf)_k; síntesis
S((u_k)) = Σu_k; Y_N = SAf; ‖SAf‖² = ‖Af‖² ⟺ anulación del Gram cruzado total.
Contraejemplo finito (§3, PROVED): u_2 = u_3 = u da 4‖u‖² frente a 2‖u‖²; u_2 = −u_3 da norma coherente 0
y suma directa positiva: ninguna identidad entre ambas se sigue de la ecuación vectorial coherente.
Salidas (§5):
 A. Dilatación de fuente: construir explícitamente V_N : H → H_N^src a partir de datos de Poisson/Fourier
    aditivos con síntesis S V_N = puerto coherente de (PC-ren) y ‖V_Nf‖² = D^orient_N(f) (teorema de
    tipo Naimark/Parseval). Objetivo «‖V_NF‖² = D_N^orient(F)».
 B. Compensación exacta del Gram cruzado: con I_N(f) = Σ_{k≠l}(log k)(log l)(kl)^{−1/2}Re⟨Δ_kf, Δ_lf⟩,
    probar I_N + B_N^polar + B_T^Tate = 2D^Γ_{T,δ} + D_N^boundary, D_N^boundary ≥ 0 (7.1), con la ecuación de
    primer contacto anulando el lado izquierdo coherente. La memo juzga B más cercana a (PC-ren).
Afirmaciones. PROVED: factorización por caminos; identidad de varianza como álgebra abstracta; Gram de
paridad. OPEN / AFIRMACIÓN PREVIA RETIRADA: segundo momento desde (PC-ren). OPEN: aparición del Gram de Tate
con el signo requerido.
Detención. La síntesis S no es isometría; la traslación aditiva de Fourier no hace ortogonales copias
log-trasladadas de una fuente de soporte compacto; hace falta una identidad Parseval/Naimark o un Gram de
borde compensador.
Lectura (inconsistencia menor): la salida A pide «una isometría V_N : H → H_N^src» con ‖V_Nf‖² = D^orient(f);
ambas cosas no son compatibles literalmente (una isometría da ‖V_Nf‖² = ‖f‖²). El contenido real es: una
aplicación V_N con norma cuadrada igual a D^orient y cuya síntesis coincide con el puerto coherente, es
decir, una dilatación en que las etiquetas sean ortogonales.
Cotejo. U1 no. U2 sí en B: el Gram cruzado se compensaría con bloques polar y de Tate (concomitantes de
borde); queda OPEN. U3 no. U4 no. U5 sí: es la definición de la salida A. Seguimiento: R161_034 calcula el
Gram cruzado exacto (canales razón/producto) y descarta la cancelación en recta completa; R161_035 declara
la suma directa «innecesaria» y la reemplaza por la versión coherente; R161_052–053 construyen una
colligación unitaria (otra dilatación, no la de A); la síntesis (R161_099, en sus líneas sobre 033 y 035)
confirma que 035 «elimina la necesidad de una dilatación etiquetada». En este tramo nadie construyó V_N
ni probó que la salida A sea imposible.

## R161_034 — Gram de Mellin exacto: la interferencia que falta es el canal producto–razón

Objeto. s = ½ + iτ; (𝓕f)^ = u_∞(τ)f̂(−τ), (Jf)^ = f̂(−τ), |u_∞| = 1. Átomo d_k = k^{−1/2}(τ_{log k}𝓕 − Jτ_{log k}),
(d_kf)^ = q_k(τ)f̂(−τ), q_k = k^{−s}u_∞ − k^{−(1−s)} (sumando de un átomo del multiplicador D_N(s)u_∞ − D_N(1−s)).
Con a_k = log k: I_N(f) = ∫Σ_{k≠l}a_ka_l q_k conj(q_l)|f̂(−τ)|²dτ (2.3).
(3.1) q_k conj(q_l) = (kl)^{−1/2}[e^{−iτ log(k/l)} + e^{iτ log(k/l)} − u_∞e^{−iτ log(kl)} − conj(u_∞)e^{iτ log(kl)}];
(3.2) Re(q_k conj q_l) = 2(kl)^{−1/2}[cos(τ log(k/l)) − Re{u_∞e^{−iτ log(kl)}}].
Comprobado: correcto. Canal razón (orientaciones iguales, k/l) y canal producto (orientaciones opuestas, kl);
coincide con 106_50_TRIANGLE_VARIANCE_AND_PRODUCT_RATIO_SPLIT. La construcción suma–producto controla el
coeficiente producto por convolución de Dirichlet pero no agrupa el término razón por Λ∗1 = log.
§4: el contratérmino polar es una familia continua de un parámetro y el bloque de Tate es de rango dos tras
compresión; no hay identidad coeficiente a coeficiente que convierta todas las frecuencias log(k/l) en un
término de borde de rango dos (ARGUED como «no puede afirmarse en la recta completa»; es un argumento de
conteo, no un teorema con clase escrita).
Candidata (5.2): fuga coherente comprimida L_{N,T}(F) = ‖(I−P)Σ_{k≤N}(log k)d_kPF‖² ≥ 0; el objeto que puede
ser nuevo es el conmutador [P, d_k].
Afirmaciones. PROVED: símbolo, diferencia exacta coherente/suma directa, descomposición producto–razón.
IDENTIFICADO: colisión con la fase 106. CANDIDATA POSITIVA CANÓNICA: (5.2). OPEN: identificación con la fuga
de dispersión física de R161_020 y saturación en primer contacto.
Detención. Sin la compresión [P, d_k] se vuelve a la varianza estrella/triángulo de la fase 106 (dirección
de coherencia errónea). La fuga (5.2) queda sin identificación.
Cotejo. U1 no. U2 sí, de lleno: la fuga ‖(I−P)·PF‖² del operador coherente es la candidata; queda OPEN, sin
cálculo de su límite renormalizado ni de su saturación. U3 no. U4 no. U5 sí: muestra que la condición de A
(Gram cruzado nulo) es falsa en recta completa — el Gram cruzado es la suma de los canales razón y producto,
que no se anulan.

## R161_035 — Puerta coherente de dos orientaciones (paralelogramo)

Objeto. U_N = K_N𝓕, V_N = JK_N; de R161_001 (3.1) S_NM𝓕 = JK_N + K_N𝓕 + {X, E_N}, luego
U_N + V_N = S_NM𝓕 − {X, E_N} (2.2), y en versión renormalizada (2.3) con K_N^ren = −[X, S_N^ren].
Teorema 3.1 (PROVED):
  D_N^coh(f) := ½(‖K_N^ren𝓕f‖² + ‖JK_N^ren f‖²) − ¼‖[S_N^renM𝓕 − {X, E_N^ren}]f‖² = ¼‖(K_N^ren𝓕 − JK_N^ren)f‖² ≥ 0,
igualdad ⟺ K_N^ren𝓕f = JK_N^ren f. Ningún término cruzado en k se elimina. Orden: síntesis por Λ∗1 = log
(K_N = L_MS_N − H_{M,N}) → retener las dos orientaciones → varianza coherente de dos estados.
Componente exterior (5.1): D^ext_{N,T} = ¼‖(I−P)(U_N^ren − V_N^ren)f‖².
Objetivo terminal (5.2): ½(‖U f‖² + ‖V f‖²) = ¼‖(U+V)f‖² + o(1) en el límite de grafo de primer contacto,
equivalente a (U_N^ren − V_N^ren)f → 0 (5.3).
Afirmaciones. PROVED: vectores coherentes, fórmula de la suma, (3.2), retención del Gram producto–razón.
OPEN/TERMINAL: (5.2); OPEN: identificación de (5.3) con la dispersión física.
Lectura: (3.1) es la identidad del paralelogramo, genérica; todo el contenido está en (5.2). La identidad
no depende del peso salvo por la definición de K_N.
Detención. §7: (5.2) es igualdad de segundos momentos; la radicalidad da sólo un emparejamiento lineal nulo
tras proyección primitiva. Definir la identidad de Green como D^coh o usar la ley de dispersión sería
circular. R161_038 prueba que (5.2) no se sigue de (PC) + radicalidad + paridad.
Cotejo. U1 no. U2 sí: (5.1) es una fuga comprimida y la memo exige aplicar la misma descomposición ortogonal
a las tres normas; no lo calcula. U3 no. U4 no. U5 sí: abandona la salida A («innecesaria»).

## R161_036 — La diferencia coherente es el jet crítico covariante Gamma

Objeto. Z_N(s) = D_N(s) − N^{1−s}/(1−s), e_N(s) = Z_N(s)u(s) − Z_N(1−s), K_N^ren(s) = −Z_N′(s);
U_N(s) = −Z_N′(s)u(s), V_N(s) = −Z_N′(1−s). (2.2) U_N + V_N = −e_N′(s) + Z_N(s)u′(s) (conexión m = u′/u);
(3.1) U_N − V_N = −Z_N′(s)u(s) + Z_N′(1−s). Usando el límite Z_N → ζ y la ecuación funcional derivada
ζ′(s)u(s) + ζ(s)u′(s) + ζ′(1−s) = 0: (3.4) U_∞ − V_∞ = −2ζ′(s)u(s) − ζ(s)u′(s).
§4 evalúa en ceros de ζ y usa ζ′(ρ) ≠ 0 (usa una evaluación en ceros y una hipótesis de simplicidad; se
registra sin desarrollar).
Afirmaciones. PROVED: (2.2), (3.1). PROVED CONDICIONAL a convergencia diferenciada del grafo: (3.4), (4.1).
OPEN/TERMINAL: saturación y convergencia diferenciada.
Lectura: §4 apoya la conclusión en simplicidad (ζ′(ρ) ≠ 0) sin prueba; R161_037 elimina esa dependencia.
Corrige. R161_037 (sustituye §4–6 por argumento casi-en-todas-partes; elimina el requisito de convergencia
diferenciada fuerte).
Cotejo. U1 no. U2 no (sólo menciona la capa de borde). U3 no. U4 no. U5 no.

## R161_037 — La saturación sola fuerza F = 0

Objeto. B_N = U_N^ren − V_N^ren, multiplicador b_N(τ) = −Z_N′(s)u(s) + Z_N′(1−s); por Euler–Maclaurin
diferenciado puntual, b_N → b_∞ = −ζ′(s)u(s) + ζ′(1−s) = −2ζ′(s)u(s) − ζ(s)u′(s).
Si D_N^coh(F) = ¼‖B_NF‖² → 0, subsucesión c.t.p. ⇒ b_∞(τ)F̂(−τ) = 0 c.t.p. (2.3). b_∞ ≢ 0 porque
b_∞ ≡ 0 implicaría (ζ²u)′ = ζ[2ζ′u + ζu′] = 0, ζ²u constante, contradicción con el polo en s = 1. Ceros
discretos en la recta ⇒ F̂ = 0 c.t.p. ⇒ F = 0.
Afirmaciones. PROVED: convergencia puntual diferenciada, argumento de subsucesión, no anulación c.t.p.,
«D_N^coh(F) → 0 ⇒ F = 0». ELIMINADO: requisito de convergencia fuerte diferenciada. OPEN/ÚNICA PUERTA: (5.1)
saturación coherente en primer contacto.
Lectura: el argumento es correcto (usa la función completa y su ecuación funcional, y la continuación
meromorfa; no usa ceros). Nota: en (3.2) la contradicción también «con cualquier cero no trivial» es
superflua.
Detención. La saturación (5.1) debe salir del emparejamiento de Green finito; la radicalidad no basta.
Cotejo. U1 no. U2 no. U3 no. U4 no. U5 no.

## R161_038 — Contramodelo matricial finito a la saturación automática

Objeto. H = ℂ²; X = diag(1, −1); J = 𝓕 = [[0,1],[1,0]]; S = [[0,1],[0,0]]; L = 0. Entonces JXJ = −X,
M = X + 𝓕X𝓕 = 0, A = M − (L + L*) = 0 (todo vector es radical). K = −[X,S] = −2S, E = S𝓕 − JS = X, H = LS − K = 2S,
{X, E} = 2I, JH + H𝓕 = 2I: (PC) se cumple exactamente; también SM𝓕 = 0 = JK + K𝓕 + {X, E}.
U = K𝓕 = −2SJ = −2 diag(1,0), V = JK = −2 diag(0,1), U − V = −2X, D^coh(f) = ¼‖(U−V)f‖² = ‖f‖² para todo f,
también en ambas rectas de paridad.
Afirmaciones. PROVED (multiplicación directa; comprobado): realización exacta, A = 0, fallo de saturación en
las dos paridades. REFUTADO: saturación algebraica automática.
Clase cerrada: toda prueba cuyos únicos insumos sean (1) involuciones J, 𝓕; (2) X + 𝓕X𝓕 = M; (3) definiciones
de K, E, H, A; (4) (PC) lineal; (5) radicalidad Af = 0 y consecuencias polarizadas lineales; (6) paridad.
Falsificador: el modelo 2×2. No modela: núcleo coseno logarítmico, soporte en intervalo físico, semigrupo de
traslaciones enteras y su continuo de Euler–Maclaurin, ley de collar de Tate cruzada, retículo de polos Gamma.
Lectura: el contramodelo no tiene Λ ni producto de Euler ni ninguna relación aritmética; cierra una clase
de manipulaciones formales, no una clase con datos físicos (lo dice la propia memo y lo refuerza R161_046).
Cotejo. U1 no. U2 sí como frontera: el modelo carece de compresión a ventana; la memo deduce que la
compresión física debe entrar de forma esencial. U3 sí, indirectamente: A = 0 es la forma nula (todo radical);
no es un vector neutro no radical de una forma indefinida. U4 no. U5 no.

## R161_039 — Equivalencia terminal y ledger bloqueado

Objeto. Resumen: B_N = K_N^ren𝓕 − JK_N^ren; D_N^coh = ¼‖B_NF‖² ≥ 0; D_N^coh → 0 ⇒ F = 0 (037). Falta (2.1):
«F primitivo de primer contacto ⇒ D_N^coh(F) → 0». No lo prueban: (PC-ren) lineal, polarización radical,
paridad, paralelogramo abstracto, etiquetas de fuente/varianza de divisores, matriz de Tate cruzada sin
derivación de su aparición y signo, E_N^ren → 0, conmutador escalar completado.
Identidad requerida (3.1): lim ¼‖B_NF‖² = −lim Green^{PC}_{N,T}(F), con Green^{PC} = 0 por radicalidad aplicada a un
test primitivo definido por la fuente, que retenga ambas orientaciones causales, con término polar = capa
imagen de 028 y término de extremo literal +ε⟨v, G_TCv⟩ = ‖r‖², sin usar inversos de la compresión primitiva
ni la ley de dispersión ni la norma deseada.
Afirmaciones. PROVED: identidad PC conjunta, coordenadas polar/Tate y signo de paridad, puerta positiva,
«saturación ⇒ F = 0». «NO PROBADO / LÓGICAMENTE INDEPENDIENTE DEL ÁLGEBRA FORMAL»: saturación desde lo
existente. MISSING: identidad de Green de borde física. Fase: BLOQUEADA.
Ledger bloqueado: (1) dispersión/fuga 017–020; (2) desplazamiento Gamma–Hankel invertido 026–029;
(3) saturación de varianza de divisores 030–033; (4) saturación coherente 035–038.
Lectura: §0 afirma «el corpus no contiene identidad física adicional que la proporcione» e insinúa
independencia; R161_046 retira la afirmación más fuerte (independencia sólo de las identidades abstractas
listadas, no de las hipótesis físicas). §4 (equivalencia «relativa a la reducción de primer contacto») es
una equivalencia interna de la arquitectura; no se desarrolla.
Cotejo. U1 no. U2 sí: exige el término de Tate literal (contabilidad conjunta) como cláusula 4 de (3.1). U3 no.
U4 no. U5 no (la salida A no figura en la lista de requisitos).

## R161_040 — Poisson identifica las dos historias exteriores

Objeto. Z_N = S_N^ren, E_N = Z_N𝓕 − JZ_N; JZ_NJ = Z_N* (coeficientes reales, reflexión invierte orientación;
comprobado también para la parte polar C_N, cuyo núcleo de Volterra cumple JVJ = V*); (1.3) Z_N𝓕 = Z_N*J + E_N.
Teorema 2.1 (PROVED): con Jf = εf, f = Pf, (I−P)Z_N𝓕f − ε(I−P)Z_N*f = (I−P)E_Nf (2.2); interior análogo (2.3).
Historias H_N^+ = (I−P)Z_N𝓕P, H_N^− = (I−P)Z_N*P; ‖H_N^+f − εH_N^−f‖² = ‖(I−P)E_Nf‖² (3.3).
Autoconmutador comprimido: para Z normal, T = PZP, ⟨f, (T*T − TT*)f⟩ = ‖(I−P)Z*f‖² − ‖(I−P)Zf‖² (4.2).
Propuesta (6.1): derivada de borde de ‖(I−P)E_N^ren f‖² = ‖(I−P)(K_N^ren𝓕 − JK_N^ren)f‖² + 2D^Γ + ε⟨v, G_TCv⟩.
Afirmaciones. PROVED: JZ_NJ = Z_N*, (2.2), (3.3), identificación del transporte anular de la fase 121 con el
defecto de Poisson. RETIRADO (por 041, orientación errónea): (6.1).
Detención. Derivar la diferencia E_N produce la media U + V, no la diferencia crítica U − V.
Cotejo. U1 no. U2 sí: fuga exterior ‖(I−P)E_Nf‖², palabras (I−P)Z P, autoconmutador de compresión; X = M_t
conmuta con P (se usa para derivar sin derivar la ventana). Razón del fracaso: orientación (041). U3 no.
U4 no. U5 no.

## R161_041 — Auditoría de orientación: suma y diferencia

Objeto. Z, K = −[X,Z], E = Z𝓕 − JZ, C = Z𝓕 + JZ; U = K𝓕, V = JK; X𝓕 + 𝓕X = M𝓕.
(2.2) U + V = ZM𝓕 − {X, E}. Teorema 3.1 (PROVED): {X, JZ} = −J[X,Z] = JK, luego U − V = ZM𝓕 − {X, C} (3.3);
D_N^coh = ¼‖[Z_NM𝓕 − {X, C_N}]f‖² (3.4). Mellin: c_N = Z_Nu + Z_N(1−s), −c_N′ + Z_Nu′ = U − V (4.3).
Objeto propuesto (5.2): Re⟨exterior Ef, exterior [ZM𝓕 − {X, C}]f⟩ con correcciones polar y de Tate.
Afirmaciones. PROVED: (2.2), (3.3), comprobación Mellin. RETIRADO: 040 (6.1). OPEN: compleción de Green mixta
comprimida E–C.
Lectura: comprobado {X, JZ} = XJZ + JZX = −JXZ + JZX = −J[X, Z] = JK. Correcto.
Cotejo. U1 no. U2 sí: el emparejamiento mixto comprimido es de tipo compresión + M_t. U3 no. U4 no. U5 no.

## R161_042 — Wronskiano de Green mixto y defecto de Tate

Objeto. Lema 1.1 (PROVED): X = X*, e = a − d, c = a + d ⇒ Re⟨e, Xc⟩ = ⟨a, Xa⟩ − ⟨d, Xd⟩. Con a_N = Z_N𝓕f,
d_N = JZ_Nf: Re⟨E_Nf, XC_Nf⟩ = ⟨Z_N𝓕f, XZ_N𝓕f⟩ + ⟨Z_Nf, XZ_Nf⟩ (2.2)–(2.3) (por JXJ = −X).
Exterior: P_+ = 1_{[T,∞)}, P_− = 1_{(−∞,−T]}, a_+ = P_+a_N, d_− = P_−d_N;
⟨a_+, Xa_+⟩ − ⟨d_−, Xd_−⟩ − T(‖a_+‖² + ‖d_−‖²) = ‖(X−T)^{1/2}a_+‖² + ‖(−X−T)^{1/2}d_−‖² ≥ 0 (3.4).
Con B_N = Z_NM𝓕 − {X, C_N}: Re⟨E_Nf, B_Nf⟩ = Re⟨E_Nf, Z_NM𝓕f⟩ − Re⟨E_Nf, XC_Nf⟩ − Re⟨E_Nf, C_NXf⟩ (4.2);
el último término fuerza PXf = Π_TPXf + Tau_TPXf (primitivo + Tate).
Identidad de aceptación (6.2): 0 = ‖(X−T)^{1/2}a_+‖² + ‖(−X−T)^{1/2}d_−‖² + D_N^boundary(f).
Afirmaciones. PROVED: Lema 1.1, (2.2), (3.4), descomposición. RECHAZADO (tautología de modulación horizontal,
por 044): componente primitiva como ley nueva. OPEN: reducción de la componente de Tate a emparejamiento
nulo; signo de las piezas de borde residuales.
Lectura: el texto original anticipaba un cuadrado de Tate positivo; la propia memo ya incorpora la corrección
de 043. La retención de las piezas «interiores y exteriores del lado equivocado» de (2.2) no se calcula.
Cotejo. U1 no. U2 sí, de lleno: usa M_t (X) y la compresión a semirrectas exteriores, con la descomposición
primitivo + Tate; queda abierto el signo de las piezas residuales. U3 no (Lema 1.1 es la forma de Wronskiano
indefinida ⟨a,Xa⟩ − ⟨d,Xd⟩, pero no se trata como forma de Kreĭn con vector neutro). U4 no. U5 no.

## R161_043 — La paridad opuesta anula el término de Tate de la derivada de la fuente

Objeto. JX = −XJ ⇒ si Jf = εf, J(Xf) = −εXf. Tau_T conmuta con J ⇒ coeficiente w_X de Tau_TPXf cumple
Cw_X = −εw_X. Con r (Cv = εv) y j = G_TCv (paridad ε): ⟨r, Tau_TPXf⟩ = 0 (3.3), ⟨w_X, j⟩ = 0 (3.5).
Afirmaciones. PROVED: las tres. RECHAZADO / PARIDAD ERRÓNEA: cuadrado de Tate positivo en este orden. OPEN:
conversión del emparejamiento finito completo en los términos ortogonales literales; identidad de Green
primitiva/exterior restante.
Detención. ε⟨v, G_TCv⟩ = ‖r‖² (032) sólo aplica a vectores de extremo de la misma paridad que el forzamiento.
Cotejo. U1 no. U2 sí: cierra la contabilidad conjunta con el bloque de Tate en el orden «Xf» (da 0, no
‖r‖²); no cierra otras ordenaciones. U3 no. U4 no. U5 no.

## R161_044 — El término primitivo Xf es la tautología de modulación horizontal

Objeto. G_σ = Π_T(e^{σX}f), G_0′ = Π_TP_TXf; P121_HORIZONTAL_MODULATION_RADICAL_NO_GO Teor. 3.1: a_T(f, G_σ) = 0 y
sus derivadas sólo repiten a_T(f, h) = 0, h ∈ P_T. Toda información nueva sería un defecto de orden exterior:
con g_N puerto producto derecho y w_N defecto de dispersión, ⟨g_N, S_N^ren w_N⟩ y ⟨(S_N^ren)*g_N, w_N⟩ son
iguales antes de cortar el soporte; su diferencia tras proyectar es una suma de términos de Hankel
PS^ren(I−P), (I−P)S^ren P. Puerta escalar mínima (4.1): Re⟨g, e⟩ = 0, e = P_+C_log g + εg, pues
½‖(I + εC_log)g‖² = Re⟨g, e⟩ (R161_021).
Afirmaciones. PROVED: G_0′ = Π_TP_TXf. TAUTOLOGÍA CONOCIDA: emparejamiento primitivo. CERO (043): Tate.
PROVED ESTRUCTURALMENTE: reducción a conmutadores de Hankel exteriores. OPEN/TERMINAL: reciprocidad exterior
antisimétrica (L161.6 de R161_023).
Lectura: R161_046 añade que dos órdenes que coinciden por adjunción en su dominio común no generan término de
borde por sí mismos; hace falta proyección o dominio distinto explícito.
Cotejo. U1 no. U2 sí: modulación e^{σX} (M_t), proyección primitiva, Hankel de compresión; la parte interior es
tautológica, queda la reciprocidad exterior OPEN. U3 no. U4 no. U5 no.

## R161_045 — Toeplitz–Hankel: el cuadrado local no globaliza la puerta

Objeto. Para primo p, r = p^{−1/2}, S el desplazamiento unilateral, A_r = rS(1 − rS)^{−1}.
(1.2) (de P122_013_LOCAL_EULER_DETERMINANT_LINE): A_r*A_r − A_rA_r* = H_{φ̄_r}*H_{φ̄_r} = (1 − r²)^{−1}ℓ_r*ℓ_r ⪰ 0
(autoconmutador de rango uno, «observación de raíz» exacta, orientación correcta bajo inversión de puerto).
Cociclo determinante local (P122_015_EULER_CONTOU_CARRERE_DETERMINANT_BRIDGE): ⟨1 − rz, 1 − rz^{−1}⟩_Hdet = 1 − r²;
su derivada de graduación es la conexión (1.1) y su curvatura es (1.2).
Por qué no cierra (§2): las ecuaciones de primer contacto dan dos historias h_{p,+}, h_{p,−}, no un mismo
vector en las dos entradas de (1.2); dan una relación de norma entre puertos cruzados, no
‖A_rh‖ = ‖A_r*h‖ (2.1) (el «transporte anular» que falta desde la fase 121). La fase 161 da el transporte no
derivado H_N^+f − εH_N^−f = (I−P)E_N^ren f (2.2), pero la derivada logarítmica que pide (1.2) cambia la
orientación: derivada de la diferencia E_N → K_N𝓕 + JK_N; derivada de la suma C_N → K_N𝓕 − JK_N (2.3). Luego
(2.2) no se puede derivar en la hipótesis de historia única (2.1).
Obstrucción global (§3, citada de P122_015): multiplicar las rectas locales no construye (1) la recta
arquimediana de cuarto Gamma, (2) los dos factores de borde de Tate, (3) una extensión convergente del
determinante de borde crítico, (4) una anomalía métrica/trivialización que identifique las dos historias
físicas, (5) planitud de primer contacto.
Afirmaciones. PROVED (CITED de fase 122): cuadrado local de Toeplitz–Hankel; cociclo local y normalización.
PROVED (040): identificación de Poisson de historias no derivadas. FALSE / ORIENTACIÓN ERRÓNEA: diferenciación
a la orientación crítica. MISSING: anomalía/trivialización determinante global Gamma–Tate. OPEN/TERMINAL:
reciprocidad exterior antisimétrica.
Motivo exacto de la detención: (i) desajuste de orientación (2.3) entre el transporte de Poisson y la
derivada que pide el autoconmutador; (ii) ausencia de trivialización global del producto de rectas locales
(los cinco ítems de §3). Lectura: el ítem (ii) es CITED de la fase 122 y no se re-deriva aquí; el ítem (i) es
PROVED por 041. La memo no da falsificador explícito; el contramodelo de clase para la parte algebraica es
el de R161_038.
Cotejo. U1 no (cada factor local es lineal en Λ vía Euler; no hay término de grado ≥ 2 que sume). U2 sí:
operadores de Toeplitz (compresión a Hardy), autoconmutador = ‖Hankel‖² de rango finito (uno) por primo;
la globalización falla por orientación y por falta de trivialización. U3 no. U4 no. U5 no.

## R161_046 — Cadena hacia atrás y detección finita sobre el radical

Objeto. Corrección de alcance: 038 refuta la saturación desde las identidades abstractas listadas, no la
independencia respecto de las hipótesis físicas; la afirmación previa de que la reciprocidad exterior es un
axioma nuevo se retira (estado: no probado). Los dos órdenes de R161_023 (5.3) coinciden por adjunción en el
dominio común: invertir el orden no genera borde; hace falta proyección/dominio distinto explícito.
Lema de detección finita (PROVED, usando compacidad de resolvente importada de la fase 121 y completitud de
momentos de R161_019): N ⊂ L²(−T,T) de dimensión finita, a_m = 2m + ½, ℓ_m(F) = ∫F(t)e^{−a_mt}dt,
N_M = N ∩ ker ℓ_1 ∩ … ∩ ker ℓ_M; existe M finito con N_M = {0}; con pesos b_m > 0,
Σ_{m≤M} b_m|ℓ_m(F)|² ≥ c_N‖F‖² en N. No acota M por dim N ni uniformemente en T.
Criterio de certificado: tests primitivos H_{m,n}F desde datos PC finitos con
|ℓ_m(F)|² ≤ Re a_T(F, H_{m,n}F) + e_{m,n}(F), limsup_n e_{m,n} ≤ 0 (criterio de aceptación, no construido).
Bloques: ⟨g, Sw⟩ = ⟨PS*g, Pw⟩ + ⟨QS*g, Qw⟩, Q = I−P; si Pw = r (Tate), el primer término es ⟨Tau PS*g, r⟩.
Afirmaciones. PROVED: reducción a detección finita (con importaciones). No establecida: independencia de las
hipótesis físicas (retira 039). OPEN: certificado PC finito. Siguiente: emparejamiento proyectado de
coeficiente de Laurent en un polo Gamma impar positivo fijo.
Cotejo. U1 no. U2 sí: rango finito (detección en N_T de dimensión finita, finitos momentos) y descomposición
P/Q del emparejamiento; ningún término con signo. U3 no. U4 no. U5 no.

## R161_047 — Compresión en polo fijo y collar exponencial exacto

Objeto. z = s − ½, a_m = 2m + ½; Res_{z=a_m}W^0(½+z) = K_F(a_m) (R161_025). v = w − E_Tr (resto exterior);
Res_{z=a_m}Mv(z) = K_F(a_m) (1); toda distribución de soporte compacto tiene transformada entera (tests
primitivos interiores, correcciones de Tate interiores, distribuciones de extremo y prehistorias Q_± no
contribuyen residuo). Modelo: h(t) = −ke^{at}1_{t<−T} tiene transformada ke^{(z−a)T}/(z−a), residuo k.
Collar (2): ℓ_a(Pτ_hF) = e^{ah}[ℓ_a(F) − L_{a,h}(F)], L_{a,h}(F) = ∫_{−T}^{−T+h}F(u)e^{−au}du, 0 ≤ h ≤ 2T.
(3): ℓ_a(PS_NF) = Σ_{n≤min(N, e^{2T})} n^{a−1/2}[ℓ_a(F) − L_{a,log n}(F)] (análogos con log n o Λ(n)).
Afirmaciones. PROVED: (1)–(3). OPEN: aniquilación en polo fijo desde PC-ren.
Detención. El factor grande n^{a−1/2} multiplica también el collar; no hay resto pequeño; coincide con la
obstrucción de momentos grandes de R161_024 §5.
Cotejo. U1 no. U2 sí: compresión por traslación finita, collares exactos; sin signo. U3 no. U4 no. U5 no.

## R161_048 — Estabilización exacta del corte interior y ledger de reintento

Objeto. Si supp F ⊂ [−T,T] y momento de Tate positivo nulo: supp C_NF ⊂ [−T − log N, T − log N]; para
log N ≥ 2T, P_TC_NF = 0 (1); P_Tτ_{log n}F = 0 si log n ≥ 2T; luego, para N ≥ e^{2T},
P_TZ_NF = P_TS_NF = Σ_{n<e^{2T}} n^{−1/2}P_Tτ_{log n}F (2). Aumentar el corte sólo cambia el exterior; no hay
ecuación interior nueva al hacer N → ∞. La relación Z_N𝓕F − εZ_N*F = E_NF retiene la fuente no compacta 𝓕F,
a la que (2) no se aplica.
Afirmaciones. PROVED: (1)–(2). Estado: paso faltante definido — controlar el bloque exterior de Fourier junto
con los collares trasladados renormalizados. D OPEN; no se declara cierre.
Cotejo. U1 no. U2 sí: compresión a ventana y truncación finita exacta; sin signo. U3 no. U4 no. U5 no.

## R161_049 — Auditoría de dispersión en tres bloques

Objeto. P_L = 1_{(−∞,−T]}, P_0 = 1_{(−T,T)}, P_R = 1_{[T,∞)}; C coseno logarítmico; g = P_Rg puerto producto
derecho corregido; h = g + εCg. Puerta deseada P_Rh = 0 (1.2) (⇔ P_RCg = −εg; por R161_020 implica h = 0).
Lo probado por el teorema de corriente entrante completada (P121_GRAPH_RENORMALIZED_INCOMING_CURRENT) es
P_0h = 0 (1.3), el bloque central. Con a = P_RCg, b = P_0Cg = 0, c = P_LCg: ‖a‖² + ‖c‖² = ‖g‖² (2.1);
e_R = g + εa, e_L = εc; ‖e_R‖² − ‖e_L‖² = 2‖a‖² + 2εRe⟨g, a⟩ (2.3); ‖h‖² = 2‖g‖² + 2εRe⟨g, Cg⟩ (2.4).
Condición escalar que falta: Re⟨g, e_R⟩ = 0 (2.5). En la primera cámara 0.8 < T < ½log5, el collar derecho
inicial es el campo Y_3 (2, 3, 4) y la fila Gamma no local Y_3(F) − tF + r_ε = CQCF.
Afirmaciones. PROVED: identidades de tres bloques. Rechazado: identificar P_0 con P_R. OPEN: transferencia
exterior. Funciones de Sonin genéricas muestran (ARGUED, sin ejemplo escrito aquí) que cancelación central
+ simetría coseno no transfieren.
Cotejo. U1 no. U2 sí: compresión a tres bloques; ninguno con signo. U3 sí, en germen: C autoadjunto unitario
(forma ⟨g, Cg⟩ indefinida); no se construye vector neutro. U4 no. U5 no.

## R161_050 — Contramodelo unitario de tres bloques

Objeto. H = ℂ³, base e_L, e_0, e_R; C e_L = e_R, C e_R = e_L, C e_0 = e_0; g = e_R; h_ε = e_R + εe_L.
Entonces g = P_Rg, C = C* = C^{−1}, P_0h_ε = 0, Ch_ε = εh_ε, pero P_Rh_ε = e_R ≠ 0 y P_RCg = 0 ≠ −εg.
Clase cerrada (PROVED por multiplicación): «cancelación central + unitaridad autoadjunta + paridad de
dispersión ⇒ dispersión comprimida derecha» es falso. Falsificador: el modelo 3×3. Propiedades aritméticas
disponibles que lo excluirían (cada una implica la exclusión del primer contacto): pertenencia al rango
co-Poisson (R161_012), removibilidad en polos Gamma impares positivos (024), energía de residuo Gamma nula
(025–026), preservación de ideales de Euler activos (P121_ACTIVE_EULER_IDEAL_OVERDENSITY), identidad de
Green/reciprocidad PC exterior (021–023).
Cotejo. U1 no. U2 sí (frontera: muestra que la compresión en tres bloques sin aritmética no basta). U3 sí,
en germen: h_ε es vector propio de la forma indefinida ⟨·, C·⟩ con ⟨h_ε, Ch_ε⟩ = ε‖h_ε‖², no neutro; no se
estudia forma de Kreĭn. U4 no. U5 no.

## R161_051 — Equivalencia terminal tras la auditoría de tres bloques

Objeto. Lista de siete propiedades de estado de igualdad (dispersión comprimida derecha; X_T(F) = 0;
removibilidad de W_ε^0 en polos Gamma impares positivos; energía de polo nula; rango co-Poisson; preservación
de ideales de Euler activos para p < e^{2T}; saturación PC coherente de 037), cada una con implicación hacia
F = 0 PROVED en fases 161/121; equivalencia de fuerza relativa a la reducción de primer contacto importada.
Afirmaciones. PROVED: cierre aguas abajo y equivalencia de fuerza (trivial: vacuidad en la dirección
recíproca). No probado: derivación de cualquiera desde PC-ren + primer contacto. Explícitamente «no es una
afirmación de que no exista prueba».
Cotejo. U1 no. U2 no (inventario). U3 no. U4 no. U5 no.

## R161_052 — Colligación unitaria finita de Poisson

Objeto. A_N(τ) = Z_N(s), B_N = Z_N(1−s) = conj(A_N); e_N = A_Nu − B_N; θ_N = A_Nu/B_N, |θ_N| = 1 c.t.p.;
e_N = B_N(θ_N − 1). P proyección de Hardy/soporte, Q = I−P, U_N = M_{θ_N}, T_N = PU_NP:
I − T_N*T_N = (QU_NP)*(QU_NP) ⪰ 0, I − T_NT_N* = (QU_N*P)*(QU_N*P) ⪰ 0; ‖x‖² − ‖T_Nx‖² = ‖QU_Nx‖² (2.3);
si T_Nx = λx, |λ| = 1, entonces U_Nx = λx. Corriente de fase sin división:
|A_N|²θ_N′/θ_N = conj(A_N)A_N′ + |A_N|²u′/u − A_N conj(A_N′) (3.2). Proposición restante (5.1): para el vector
fuente x_{M,N,T}(F), ‖T_Nx‖² − ‖x‖² → 0 y el límite de QU_Nx es la fuga izquierda física.
Afirmaciones. PROVED: multiplicador unimodular, cuadrado de fuga Toeplitz–Hankel, corriente de fase.
RETIRADO por R161_056 (fuera del tramo; nota en cabecera): que la tangente unitaria sea el jet de cierre (es
la media U + V). OPEN: (5.1).
Cotejo. U1 no. U2 sí: es una compresión de un unitario con defecto ‖QU_NPx‖² (fuga exacta, sin raíz
cuadrada elegida); queda abierta la extremalidad y la tangente tiene orientación errónea. U3 no. U4 no.
U5: relacionado pero distinto — es una dilatación unitaria (colligación conservativa) del cociente de las
dos historias, no la dilatación de fuente con etiquetas k ortogonales de la salida A.

## R161_053 — Levantamiento canónico de la fuente y tangente covariante

Objeto. (E_N^ren F)^ = [A_Nu − B_N]F̂(−τ); x_N(F) = B_NF̂(−τ); U_Nx_N = A_NuF̂(−τ), (U_N − I)x_N = (E_N^renF)^ (1.3).
D_τ = (1/i)∂_τ, [D_τ, U]x = (1/i)U′x; U_N*[D_τ, U_N]x_N = q_Nx_N, q_N = (1/i)θ_N′/θ_N real;
|B_N|²q_N = (1/i)[conj(A_N)A_N′ + |A_N|²u′/u − A_N conj(A_N′)]. ‖PU_Nx‖² + ‖QU_Nx‖² = ‖x‖²; x_N no está en PH.
Aceptación (5.1): ‖QU_Nx_N^Tate(F)‖² + E_N^Γ(F) + E_N^Tate(F) = o(1).
Afirmaciones. PROVED: levantamiento, (1.3), tangente covariante. RETIRADO por 056: orientación de cierre
(la tangente es la media). OPEN: balance (5.1).
Cotejo. U1 no. U2 sí (compresión de Hardy y extremo de Tate). U3 no. U4 no. U5: el levantamiento x_N es una
dilatación de la fuente al espacio de frontera, pero sin etiquetas k ni norma D^orient: no es la salida A.

## R161_054 — Dos orientaciones causales: lema de apriete

Objeto. H = H_L ⊕ H_0 ⊕ H_R, U unitario, y = Ux: ‖y_R‖² − ‖x_R‖² = ‖x_L‖² − ‖y_L‖² + ‖x_0‖² − ‖y_0‖² (1.1).
Con ‖x_0‖ = ‖y_0‖: una orientación con x_L = 0 da ≤ 0 (1.4); la orientación reflejada da ≥ 0 (1.5); si es el
mismo escalar, ambos se anulan (1.6). Δ_0 = ‖x_0‖² − ‖y_0‖² no controlado (2.2); asignarle 0 desde el
conmutador completado es inválido (amplitud central ≠ diferencia de métricas). Aceptación (4.1)–(4):
Δ^+_{0,N} − Δ^−_{0,N} = 2Re⟨C_N^Tate(F), endpoint_N(F)⟩, normas exteriores comunes N_T(0), N_T(δ) en orden
invertido, restos o(δ) uniformes; entonces E_T^PC(F) = 0 (R161_015).
Afirmaciones. PROVED: (1.1), apriete abstracto. OPEN: igualdad métrica central (4.1), identificación de
puerto común y uniformidad. Nota 056: la aplicación a la tangente de θ_N no alcanza el jet crítico.
Cotejo. U1 no. U2 sí: balance de bloques de compresión con término de Tate; abierto. U3 sí, en el
mecanismo: dos desigualdades de signo opuesto sobre el mismo escalar (apriete), no una forma de Kreĭn; no
hay vector neutro. U4 no. U5 no.

## R161_055 — Igualdad métrica central por límite diagonal de grafo

Objeto. Lema diagonal (PROVED): E_N = Y_N − X_N, E_Nf → 0 y X_Nf → Xf en un núcleo denso en el grafo; existen
f_j → F y N_j con E_{N_j}f_j → 0, X_{N_j}f_j → XF, Y_{N_j}f_j → XF; para toda proyección P,
‖PY_{N_j}f_j‖² − ‖PX_{N_j}f_j‖² → 0. Aplicación: X_N = Z_N*J, Y_N = Z_N𝓕, E_N = E_N^ren; estable bajo una
corrección de rango finito T_j común a ambas historias.
Afirmaciones. PROVED: diagonal; igualdad métrica central no derivada a lo largo de ella; estabilidad bajo la
corrección de Tate. OPEN: tangente diferenciada e identificación de norma de puerto común; restos o(δ).
Lectura: la igualdad es de orden cero; la propia memo advierte que ambas diferencias proyectadas pueden
tender a cero sin informar sobre la capa de borde derivada. La aplicabilidad usa el grafo común de la fase
121 (importado).
Cotejo. U1 no. U2 sí (proyecciones y corrección de rango finito); sin signo. U3 no. U4 no. U5 no.

---

## Síntesis

### (a) Piezas PROVED reutilizables

- Capa polar = imagen exterior: ∂_aC_a = e^{a/2}τ_a; soporte de C_aF en [−T−a, T−a] bajo momento de Tate nulo;
  ∂_a(C_aF) = εe^{a/2}τ_aJF (R161_028 §§1–3). Estabilización interior P_TZ_NF = Σ_{n<e^{2T}} n^{−1/2}P_Tτ_{log n}F
  para N ≥ e^{2T} (R161_048 (1)–(2)).
- Derivada y saltos de ‖Z_af‖² (R161_029 (2.2), (3.2)): indefinidos, útiles como falsificadores de monotonía.
- Varianza orientada de divisores (R161_030 Teor. 1.1) y su realización por caminos con colapso de la
  costura (R161_031 (3.2)): D^orient = ¼Σ(log k)²/k‖Δ_kf‖² como suma directa.
- Gram de paridad de Tate: ε⟨v, G_TCv⟩ = ‖r‖² = 4|c|²(sinh T + εT) (R161_032 Teor. 2.1, (3.2)).
- Gram cruzado exacto en Mellin, canales razón y producto (R161_034 (2.3), (3.1)–(3.2)).
- Paralelogramo coherente D_N^coh = ¼‖(K_N^ren𝓕 − JK_N^ren)f‖² con U + V = S^renM𝓕 − {X, E^ren} (R161_035 Teor. 3.1)
  y U − V = ZM𝓕 − {X, C} (R161_041 Teor. 3.1).
- D_N^coh(F) → 0 ⇒ F = 0 (R161_037 §§2–3), usando la función completa y su ecuación funcional.
- JZ_NJ = Z_N*, transporte exterior de Poisson (I−P)Z_N𝓕f − ε(I−P)Z_N*f = (I−P)E_Nf (R161_040 Teor. 2.1, (3.3));
  autoconmutador comprimido como diferencia de dos fugas (R161_040 (4.2)).
- Lema de Green suma–diferencia Re⟨a−d, X(a+d)⟩ = ⟨a,Xa⟩ − ⟨d,Xd⟩ y exceso exterior (3.4) (R161_042).
- Paridad: J(Xf) = −εXf; el término de Tate de Xf es ortogonal a r y a j (R161_043).
- Π_TP_TXf = G_0′ de la modulación horizontal (R161_044 §1).
- Cuadrado local de Toeplitz–Hankel A_r*A_r − A_rA_r* = (1 − r²)^{−1}ℓ_r*ℓ_r (R161_045 §1, CITED de P122_013) y
  cociclo 1 − r² (CITED de P122_015).
- Detección finita en un radical de dimensión finita (R161_046), collar exponencial exacto (R161_047 (2)–(3)),
  residuos Gamma exteriores (R161_047 (1)).
- Identidades de tres bloques (R161_049 (2.1)–(2.4)); colligación unitaria θ_N y fuga exacta (R161_052 §2);
  levantamiento x_N y tangente covariante (R161_053 §§1–2); flujo de tres bloques y apriete (R161_054 §1);
  lema diagonal (R161_055 §1).

### (b) Cierres con clase y falsificador

- R161_038: clase = pruebas que usan sólo involuciones J, 𝓕, X + 𝓕X𝓕 = M, definiciones de K, E, H, A, (PC)
  lineal, radicalidad (y polarizaciones lineales) y paridad. Falsificador: modelo 2×2 con A = 0 y
  D^coh = ‖f‖². Conclusión: la saturación coherente no se sigue de esa clase.
- R161_050: clase = cancelación central + C autoadjunto unitario + paridad de dispersión. Falsificador:
  modelo 3×3. Conclusión: no hay transferencia P_0 → P_R.
- R161_033 §3: clase = deducir la norma de suma directa desde la ecuación coherente. Falsificador: u_2 = ±u_3.
- R161_029: monotonía de la discrepancia ordinaria FALSE (falsificador NUMÉRICO).
- R161_040 (6.1), R161_052–054 (tangente unitaria): retirados por orientación errónea (041, 056), con prueba
  algebraica de que la derivada de la diferencia es la media.
- R161_043: cuadrado de Tate positivo en el orden Xf: rechazado por paridad opuesta (PROVED).
- R161_044: componente primitiva de Xf: tautología (fase 121).
- R161_034 §4: cancelación polar/Tate del Gram cruzado en recta completa: ARGUED imposible (conteo de rango
  dos frente a infinitas frecuencias), no teorema con clase.

### (c) Explícitamente abierto, con obstáculo exacto

- L161.11 (028 (6.1)) / forma de dos orientaciones de 029 §6: término cruzado Re⟨Z_af, τ_af⟩ sin signo.
- Saturación de varianza de divisores (030 (4.2)) y borde (031 (5.3)): la norma de suma directa no está
  realizada por (PC-ren) (033).
- Contabilidad de Green finita (032 (4.2)) 0 = X_T + ‖r‖² + D^orient + 2D^Γ: no se derivó que el concomitante
  aparezca como +ε⟨v, j⟩; D^orient no realizado; en el orden Xf da 0 (043).
- Salidas A y B de 033 (7.1).
- Fuga coherente comprimida L_{N,T} = ‖(I−P)Σ(log k)d_kPF‖² (034 (5.2)): sin identificación con la fuga física ni
  saturación.
- Saturación coherente (035 (5.2), 037 (5.1), 039 (2.1)): «primer contacto ⇒ D_N^coh → 0»; requiere una identidad
  de Green de borde física (039 (3.1)) que no existe en el corpus.
- Compleción de Green mixta E–C comprimida (041 (5.2), 042 (6.2)): signo de las piezas residuales de borde.
- Reciprocidad exterior antisimétrica (044 §§3–4; 045): Re⟨g, e⟩ = 0; requiere trivialización global
  Gamma–Tate (045 §3) o identidad de orden exterior con proyección/dominio distinto (046).
- Certificado PC finito para detección (046); aniquilación en polo fijo (047): el factor n^{a−1/2} multiplica
  el collar.
- Transferencia exterior P_0 → P_R (049–051): exige una propiedad aritmética que excluya el modelo 3×3.
- Extremalidad de la colligación (052 (5.1)), balance PC–Γ–Tate (053 (5.1)), igualdad métrica central
  diferenciada (054 (4.1), 055 §4).

### (d) Lo que ya recorre U1–U5, con la razón registrada del fracaso

- U1 (término de grado ≥ 2 en el peso que sume y se anule en Λ). Sólo R161_030–031 tienen un término
  cuadrático en el peso que entra sumando: ½ΣΣ_{d,e|k}Λ(d)Λ(e)‖m_d − m_e‖². Se anula, pero por coherencia de las
  traslaciones (m_{k,d} no depende de d) y para cualquier peso, no por Σ_{d|n}Λ(d) = log n; la identidad (1.1)
  es genérica en el peso. El fallo registrado no es de U1 sino de realización (033). U1 queda sin tocar en su
  sentido de REVIEW_003.
- U2 (compresión, M_t, rango finito; bloque de Tate). Recorrido extensamente: fuga coherente comprimida
  (034 (5.2), sin identificar); fuga exterior de Poisson (040 (3.3), su derivada da la orientación media: 041);
  Green mixto con M_t y semirrectas exteriores (042, piezas residuales sin signo); término de Tate en orden Xf
  = 0 por paridad (043); término primitivo = tautología (044); autoconmutador Toeplitz–Hankel local de rango
  uno (045: no globaliza por orientación y falta de trivialización Gamma–Tate); rango finito / detección (046);
  collares (047–048); tres bloques (049–050: contramodelo); colligación unitaria y apriete (052–055: tangente
  con orientación media, igualdad central sólo de orden cero). La contabilidad conjunta con el bloque de Tate
  (032 (4.2)) quedó OPEN sin derivación; las tres razones registradas son: aparición/signo no derivados (033 §6),
  segundo momento de suma directa no realizado (033), y anulación por paridad en la ordenación Xf (043).
  No hay en el tramo un cálculo completo de (4.2) en otra ordenación.
- U3 (formas indefinidas con vector neutro no radical). No se construye ninguna. Lo más cercano: G_TC indefinida
  en el plano de Tate y positiva en la recta de paridad (032); forma ⟨g, Cg⟩ con C autoadjunto unitario
  (049–050, el vector h_ε es propio, no neutro); apriete de dos desigualdades opuestas (054); Wronskiano
  ⟨a,Xa⟩ − ⟨d,Xd⟩ (042). Ninguna se trata como espacio de Kreĭn.
- U4 (resto de Möbius truncado). No aparece en el tramo; 031 declara que no usa eliminación de Möbius. La cola
  H_{M,N} sólo entra como K_N = L_MS_N − H_{M,N}.
- U5 (salida A de 033). Definición: aplicación V_N : H → ⊕_{2≤k≤N}H construida de datos de Poisson/Fourier aditivos,
  con S V_N = puerto coherente de (PC-ren) y ‖V_Nf‖² = D^orient_N(f) = ¼Σ_{k≤N}(log k)²/k‖Δ_kf‖² (teorema de tipo
  Naimark/Parseval que vuelva ortogonales las etiquetas k). Exigiría: compensar o anular el Gram cruzado
  I_N = Σ_{k≠l}(log k)(log l)(kl)^{−1/2}Re⟨Δ_kf, Δ_lf⟩, que por 034 es exactamente la suma de los canales razón
  (cos(τ log(k/l))) y producto (−Re u_∞e^{−iτ log kl}), no nulos (colisión con fase 106). Nadie la tomó: 035 la
  declara innecesaria y pasa a la versión coherente; 052–053 construyen otra dilatación (colligación unitaria
  M_{θ_N} con levantamiento x_N = B_NF̂(−τ)), sin etiquetas k, cuya tangente resultó tener orientación media
  (056); la síntesis R161_099 confirma el abandono. No hay en el tramo prueba de imposibilidad de A.

### (e) Inconsistencias entre memos

1. 031 §0 dice que los vectores de 030 (4.1) quedan identificados y sugiere realización; 033 retira la
   realización de la norma de suma directa (031 ya remite a 033 en su texto).
2. 033 §5.A pide una «isometría» con ‖V_Nf‖² = D^orient(f): incompatible literalmente; el sentido real es una
   dilatación con etiquetas ortogonales. 033 (1.4) llama «diagonal de (1.3)» a una cantidad que difiere en el
   factor ¼.
3. 032 anticipa el término +ε⟨v, j⟩ = ‖r‖² en la contabilidad; 042 lo esperaba en el orden Xf; 043 prueba que en
   ese orden es 0.
4. 039 §0 sugiere independencia lógica de la saturación respecto del corpus; 046 la retira (sólo respecto de las
   identidades abstractas de 038).
5. 040 (6.1) propuesto y retirado por 041; 052–054 proponen la tangente de θ_N como jet de cierre, retirado por
   056 (fuera de tramo), con notas en cabecera.
6. 036 §4 usa simplicidad (ζ′(ρ) ≠ 0) y convergencia diferenciada; 037 elimina ambas dependencias.
7. 029 identifica L161.11 con la puerta de Markov invertida de 016; 031 y 035 cambian el objetivo a la versión
   suma directa y luego coherente; 039 los declara la misma puerta bloqueada.
8. 049 afirma que funciones de Sonin genéricas impiden la transferencia, sin ejemplo escrito en la memo (lo
   escribe 050 en forma matricial).

### (f) Archivos leídos (lectura completa con Read, de principio a fin)

R161_028 (198 l.), R161_029 (132), R161_030 (143), R161_031 (162), R161_032 (147), R161_033 (175), R161_034 (152),
R161_035 (158), R161_036 (149), R161_037 (151), R161_038 (171), R161_039 (111), R161_040 (160), R161_041 (151),
R161_042 (179), R161_043 (120), R161_044 (116), R161_045 (93), R161_046 (75), R161_047 (66), R161_048 (39),
R161_049 (70), R161_050 (53), R161_051 (44), R161_052 (99), R161_053 (97), R161_054 (99), R161_055 (69).
28 de 28, todos completos. Además, de la fase 212: README.md, OBJECT_SPEC.md, LEDGER.md, BRIEF_CONSTRUCTOR.md,
REVIEW_003.md (completos). Para el seguimiento de U5 se buscó «dilation/Naimark/direct-sum» en R161_056–099
(búsqueda auxiliar, no lectura completa de esos archivos).
