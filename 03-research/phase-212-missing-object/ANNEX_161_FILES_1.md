# Anexo: lectura por archivo de la fase 161, tramo 1 (README y R161_000 a R161_027)

Carpeta leída: `03-research/phase-161-row-d-sum-product-square/`. Existe; contiene README.md, R161_000 a
R161_081 y `scripts/` con: 161_01_hyperbola_defect.py, 161_02_poisson_defect_probe.py,
161_03_gamma_hankel_identity.py, 161_04_pc_matrix_countermodel.py (no analizados).

Cotejo contra lo que `REVIEW_003.md` deja sin excluir:
U1 término de grado ≥ 2 en el peso que entre sumando y se anule en Λ por Σ_{d|n}Λ(d) = log n;
U2 compresión a la ventana (fuga ‖(I−P)·PF‖², palabras QV_aQ), operador de posición, rango finito, contabilidad
conjunta con el bloque de Tate; U3 formas indefinidas con vector neutro no radical; U4 resto de casi-coincidencias
con Möbius truncado c_N(k); U5 dilatación de fuente isométrica (salida A de R161_033).

Advertencia general de lectura. A partir de R161_004 §4 la fase trabaja sobre un «estado de primer contacto» (vector
del radical de la forma primitiva semidefinida en el primer T donde deja de ser definida) y busca probar que ese
vector es nulo. Para ello las memos R161_004, 005, 007–012, 014, 019–021 usan una equivalencia externa (reducción a
valores en un conjunto de ceros y un argumento de conteo tipo Cartwright importado de la fase 121). Se registra
neutralmente como «usa una equivalencia externa»; no se desarrolla. Las piezas que no dependen de ella se marcan.

Notación de la fase: τ_aF(t) = F(t+a), JF(t) = F(−t), X = Q = multiplicación por t, 𝓕 = Fourier aditivo en
coordenada logarítmica, M = m(D) con m(τ) = Re ψ(1/4+iτ/2) − log π, X + 𝓕X𝓕 = M (importada, R160_C8_R1);
S_N = Σ_{n≤N} n^{−1/2}τ_{log n}, K_N = Σ (log n)n^{−1/2}τ_{log n}, L_M = Σ_{d≤M} Λ(d)d^{−1/2}τ_{log d},
A_M = M − L_M − L_M*.

---

## 1. Entradas por archivo

### README.md
Índice de la fase con 35 ítems de «veredicto» y una «actualización de auditoría hacia atrás» que resume R161_046 a
R161_081 (fuera de este tramo). Estado declarado: OPEN. Ítems relevantes para este tramo: 1–19. Los ítems 20–35 y la
auditoría resumen memos posteriores: la «varianza a dos niveles» por fibras de producto (ítem 20), el cuadrado de
Poisson en suma directa (21), el bloque de Tate cruzado positivo por paridad (22, luego anulado en el orden de
derivada de fuente, ítem 33), la falta de un paso de Gram coherente frente a suma directa (23: «se requiere una
dilatación explícita de Parseval/Naimark o una identidad de Green exacta») — antecedente directo de U5 —, la
fuga comprimida coherente ‖(I−P_T)Σ_k(log k)d_kP_TF‖² (24) — antecedente directo de U2 —, el contramodelo 2×2 que
cumple todas las identidades algebraicas con A = 0 y D^coh(f) = ‖f‖² (28), y R161_081: en un autovector de paridad
Hf = λf, el resto exacto es Q = −2Σ_m(d_{m,N}+λ)|(R_Lf)_m|², luego no admite representación por cuadrados no
negativos en todo el espacio primitivo. Etiquetas: no se da ninguna propia. Cotejo: U2 sí (ítems 10, 24, 30–32,
como resumen); U5 sí (ítem 23, como resumen); U1, U3, U4 no.

### R161_000_BLUEPRINT.md
Objeto: plan. Fija la normalización anterior, define E_N = S_N𝓕 − JS_N (defecto finito de Poisson) y el multiplicador
A_{M0}. Exige cuatro propiedades a una candidata: conjunción (Poisson y Λ∗1 = log en una misma identidad de
operadores), cuadraticidad, orientación (retener A_T, no A_T² ni |A_T|), separación (defecto interior explícito
para Λχ_2, Ξ_a, borrado, amplificación, Dedekind, Beurling). Premisas citadas: positividad primitiva PROVED hasta
log 2, completa CITED hasta 0.8; margen sin cota inferior uniforme. Sin afirmaciones probadas. No se corrige.
Cotejo: U1 no; U2 no (sólo anuncia); U3 no; U4 no; U5 no.

### R161_001_MUNTZ_CHEBYSHEV_ANOMALY.md
Objeto: el operador de hipérbola H_{M0,N} = L_{M0}S_N − K_N y la identidad conjunta
(PC) S_N A_{M0} 𝓕 = {X, E_N} − L_{M0}* E_N − J H_{M0,N} − H_{M0,N} 𝓕.
Afirmaciones: Teorema 2.1 (soporte de la hipérbola; PROVED, sostenido): si M0 ≥ N, H_{M0,N} =
Σ_{k>N} h(k) k^{−1/2}τ_{log k} con h(k) = Σ_{dm=k, d≤M0, m≤N} Λ(d) ≥ 0, sin coeficientes en k ≤ N. Teorema 3.1 ((PC);
PROVED sobre S(ℝ), sostenido: usa [X,S_N] = −K_N, X𝓕 + 𝓕X = M𝓕, JL = L*J y conmutación de sumas de traslaciones).
Teorema 4.1 (defecto interior; PROVED, sostenido): con peso general a, el coeficiente en k ≤ N es
δ_a(k) = Σ_{d|k}a(d) − log k; lista de valores para los falsificadores (borrado −log 2 en k = 2, amplificación c en
n_0, Λχ_2 −2 log 2, Ξ_a log 2(2^a+2^{−a}−1), etc., tomados de R160_D4_R2). §5: el paso al límite M0, N → ∞ está
prohibido sin teorema de dominio (S_∞ no acotado en densidad crítica). §6: no afirma signo; «coeficientes positivos
no hacen positiva una suma de traslaciones». Se detuvo: sin signo; el cuadrado se analiza en R161_002. No se retira.
Cotejo: U1 no (Λ∗1 = log entra linealmente, como átomo δ_a(k); es exactamente el fenómeno de R3-i); U2 no (sin
compresión); U3 no; U4 no, pero es el antecedente con pesos Λ en lugar de μ: h(k) para N < k ≤ M0·N es el resto
truncado de la convolución Λ∗1, de coeficientes ≥ 0; U5 no.

### R161_002_SQUARE_VERDICT_AND_NEXT_LEMMA.md
Objeto: el cuadrado canónico Q_{M,N}(F) = ‖R_{M,N}F‖² = ‖S_N A_M 𝓕F‖² y el emparejamiento orientado
B_{M,N}(F) = Re⟨R_{M,N}F, S_N𝓕F⟩ = ⟨A_M G, S_N*S_N G⟩, G = 𝓕F. Define las fugas C_T = (1−P_T)𝓕P_T,
C_T^{(N)} = (1−P_T)S_N𝓕Π_T y el defecto comprimido E_{N,T} = P_T(S_N𝓕 − JS_N)Π_T.
Afirmaciones: Teorema 1.1 (pérdida de orientación; PROVED, trivial y sostenido): Q invariante bajo A ↦ −A; Cor. 1.2:
toda suma no negativa de tales cuadrados es ciega al signo. §2 (ARGUED, correcto): positividad de B en todo L² ⇔
A_M ≥ 0 salvo un conjunto nulo; falsa para M finito en la recta (fondo semilocal negativo, citado). §3: sin
compresión se vuelve al desplazamiento de ventana (CITED R160_D4_R2 Thm 5.1). Problema SP-161 y Lema L161.1 (OPEN):
pesos canónicos w_N ≥ 0 con Σ w_N B_{M,N} = a_T + borde ≥ 0 (borde = cuadrados de fuga con C_T, C_T^{(N)}).
Teorema 8.1 (no hay telescopado positivo; PROVED, sostenido): para w_N ≥ 0 no todos nulos, el coeficiente de
Σ w_N H_{M,N} en un primo p grande es log p·Σ_{N<p} w_N > 0. Cor. 8.2: el salto discreto h_p(p) − h_{p−1}(p) = −log p;
el signo aparece como derivada de borde terminal. Se detuvo: L161.1 muere en la rama de pesos positivos (Thm 8.1);
la de cuadrados de fuga nunca se construyó. Corregido/retirado por R161_004 (lecturas escalar y por fibras de L161.2).
Cotejo: U1 no (sólo grado uno; prueba «sign-flip» Λ(2) ↦ −Λ(2) en §6); U2 sí: SP-161 es literalmente
«a_T = Σ emparejamientos orientados + cuadrados de fuga de compresión ≥ 0» — quedó OPEN sin objeto escrito, y la
rama positiva murió por Thm 8.1, no por un argumento sobre la fuga; U3 no; U4 no (Thm 8.1 es el análogo con Λ:
ninguna ponderación positiva de restos de hipérbola cancela); U5 no.

### R161_003_POLAR_RENORMALIZATION.md
Objeto: C_N(s) = N^{1−s}/(1−s), Z_N = D_N − C_N, S_N^ren = Z_N(1/2+iD) = S_N − ∫_0^N x^{−1/2}τ_{log x}dx,
E_N^ren = S_N^ren𝓕 − JS_N^ren, y la identidad (PC-ren) con H^ren = H_{M,N} − L_M C_N(D) + [X, C_N(D)].
Afirmaciones: Prop. 1.1 (obstrucción del truncamiento crudo; PROVED, sostenido): |e_N(τ)| ≥ c_τ N^{1/2} infinitas
veces. Teorema 2.1 (convergencia renormalizada; PROVED en datos de Schwartz, sostenido vía Euler–Maclaurin y la
ecuación funcional). Teorema 2.2 (retículo menos continuo; PROVED): (C_N(D)F)(t) = e^{−t/2}∫_{−∞}^{t+log N}e^{y/2}F;
si ∫e^{y/2}F = 0, soporte de C_N(D)F en [−T−log N, T−log N] (capa de borde trasladada). (PC-ren) PROVED (misma
álgebra). §4: el término polar es de tamaño N^{1/2} y no se puede descartar ni cancelar tras normas. Lema L161.2
(OPEN, luego RETIRADO por R161_004 en sus formas escalar y por fibras). Se detuvo: sin signo.
Cotejo: U1 no; U2 parcialmente: la capa polar es un objeto de borde de ventana pero no se forma ninguna fuga
cuadrática; U3 no; U4 no; U5 no.

### R161_004_CORPUS_COLLISION_AND_STOP_GATES.md
Objeto: cotejo de L161.2 contra el corpus. Prop. 1.1 (estabilización; PROVED, sostenido): para N ≥ e^{2T},
P_T S_N P_T = Z_{T,−} y P_T JS_NJ P_T = Z_{T,+}, observaciones causales de la fase 121, invertibles con parte no
identidad nilpotente. §2 (Cor. 2.1, PROVED por identidades citadas de Paper 41 C4–C5): la versión escalar de L161.2
(primitiva D(u) = Σ_{log n≤u}Λ(n)/√n − 2(e^{u/2}−1)) cae en la clase excluida: completado local con cuadrado de signo
equivocado y densidad escalar negativa bajo log 2. §3 (Cor. 3.1, CITED de fases 104/106 y 121): el levantamiento por
fibras de divisores P(D=d|N) = Λ(d)/log N tiene hueco espectral nulo; la eliminación unitriangular de Möbius
(D = {1,2,3,4,6,12}) mata la diagonal identidad al derivar logarítmicamente. §4: usa una equivalencia externa
(certificado de rango orientado (4.1) de la fase 121). §5: en 0.8 < T < ½ log 5 sólo contactan 2, 3, 4 (orden de
nilpotencia 3). Decisión: L161.2 RETIRADO; reemplazo L161.3 (OPEN). Cotejo: U1 no (la fibra de divisores usa Λ∗1
como desintegración positiva, lineal; muere por hueco nulo, no por grado); U2 sí, parcialmente: la compresión
doble P S_N P se identifica con objetos viejos (fase 121) — «lo nuevo debe salir del puerto extra», no de S_N;
rango finito: la cámara 2,3,4; U3 no; U4 no (la eliminación de Möbius es unitriangular sobre divisores, no c_N(k));
U5 no.

### R161_005_FIRST_CONTACT_POISSON_PORT.md
Objeto: para F en el radical (P A P F = r ∈ span{e^{∓t/2}}), el puerto exterior ℓ_T(F) = (1−P)AF, AF = r + ℓ_T(F), y
Teorema 1.1 (PROVED, trivial y sostenido): P R_{M,N}𝓕F = P S_N r + B_{N,T}(F), B_{N,T}(F) = P S_N(1−P)AF; versión
renormalizada (3.1). §2: P S_N(1−P) no se estabiliza; ‖B‖² pierde orientación. §4: álgebra interior finita en la
cámara 0.8 < T < ½ log 5: Z_{T,−}^{−1} = I − K + K² (PROVED). §5 «PC-port theorem» (OPEN; usa una equivalencia
externa). Cotejo: U1 no; U2 sí: es exactamente un bloque de compresión P S_N (1−P) A P (palabra Q V Q′ con
proyecciones complementarias); se dejó sin signo y como incógnita; U3 no; U4 no; U5 no.

### R161_006_EXTERIOR_PORT_KERNEL.md
Objeto: núcleo exacto del puerto renormalizado. Teorema 2.1 (PROVED, sostenido): para g = (1−P)g,
(P S_N^ren(1−P)g)(t) = Δ^R_{N,T}g(t) − e^{−t/2}a_−(g), con Δ^R la discrepancia «enteros menos continuo» sobre la
cola derecha con extremo móvil e^{T−t}, y a_−(g) = ∫_{−∞}^{−T}e^{y/2}g. Reflejado (3.2) con a_+(g). La
contaminación cruzada de colas es exactamente el plano de Tate. Restos no locales: Δ^R ℓ_T(F), Δ^L ℓ_T(F) (OPEN).
Cotejo: U2 sí (cálculo exacto de un bloque de fuga de compresión y su parte de Tate; sin signo); resto no.

### R161_007_CHEBYSHEV_CRITICAL_JET.md
Objeto: G_{+,T}F = ζ(s)H_{+,T}F = −ζ′(s)K_F(z) − ζ(s)Q_{+,T}(z); en Re s > 1 es (Σ1·n^{−s})(ΣΛ(d)d^{−s}) = Σ log k·k^{−s}.
Teorema 2.1 (PROVED; usa una equivalencia externa: valor en un conjunto de ceros). §5: compatibilidad (5.1) OPEN.
§4: «la ceguera de signo es fatal para positividad directa pero no para rigidez en el estado de igualdad». Cotejo:
U1 no (producto de series = Λ∗1 = log, lineal en Λ); U2–U5 no.

### R161_008_PRODUCT_HARDY_SEPARATION.md
Objeto: puerto corregido G_+^0 = G_+ − c_+(F)ζ(1/2+z)Θ_T(z), con θ_T ∈ C_c^∞((T,T+1)). Teorema 3.1 (PROVED):
e^{Tz}G_+^0 ∈ H²(ℂ_+); reflejado en H²(ℂ_−). Usa la regularidad H^s, s < 1/2, de los vectores del radical (CITED
fase 121) y la cota de convexidad (CITED). Reserva del lector: el paso de Paley–Wiener desde soporte causal y frontera
L² requiere control de crecimiento en la banda 0 < Re z ≤ 1/2 que la memo no escribe (ARGUED en ese punto). §4–§5:
cierre por soporte disjunto si «límite PC = g_+ + g_−» (OPEN; usa una equivalencia externa). Corregido por R161_011
(falta la dispersión coseno). Cotejo: U1–U5 no.

### R161_009_POLAR_COEFFICIENT_MATCH.md
Objeto: residuos polares del puerto = momentos de Tate exteriores; por primitividad c_+′(F) =
Σ_{2≤n<e^{2T}} Λ(n)/n ∫_{T−log n}^T e^{−u/2}F (colar finito); más colares Gamma continuos; sistema de Tate cruzado
[[2T, 2sinh T],[2sinh T, 2T]](α,β)ᵀ = (J_+, J_−)ᵀ, determinante 4(T² − sinh²T) ≠ 0. Teorema 3.1 (PROVED, relativo
al teorema de colar de la fase 121). (5.2) OPEN. Cotejo: U2 sí, en la parte «bloque de Tate»: es la contabilidad
del bloque de Tate cruzado que U2 menciona; la matriz cruzada es indefinida (ver R161_023 §4); U3 roza: matriz
indefinida, pero sólo se usa para resolver (α,β), no como forma; U1, U4, U5 no.

### R161_010_FIRST_CONTACT_CLOSURE.md
Objeto: «cierre» por división de Hardy. Teorema 3.1 (originalmente PROVED) RETRACTADO por la propia nota de
errata (R161_011): omite la dispersión coseno/reflexión. Conclusiones 4.1, 5.1, 5.2 rebajadas a CONDITIONAL. Usa
una equivalencia externa. Cotejo: U1–U5 no.

### R161_011_TYPED_SCATTERING_AUDIT.md
Objeto: ecuación tipada g_+ + C_log R g_− = 0 (en lugar de g_+ + g_− = 0); para paridad
(I + εC_log)g_+ = 0 con soporte en [T,∞): espacio de Sonin, no trivial. Lema terminal (4.2) OPEN: intersección
del rango del puerto aritmético con Son_T^ε trivial. Retracta R161_010 Thm 3.1. Menciona que la sombra escalar de
dos contornos de la fase 116 tiene inercia de Kreĭn (CITED). Cotejo: U3 roza (cita la inercia de Kreĭn de una
sombra escalar, no construye vector neutro); U2 no; U1, U4, U5 no.

### R161_012_PRODUCT_RANGE_AND_FIRST_COLLAR.md
Objeto: rango físico Ran_phys(Z_+) (definido como rango de grafo); Prop. 1.1 (PROVED CONDITIONALLY; usa una
equivalencia externa). Germen exacto (3.2) en el primer colar T < t < T+δ, 0.8 < T < ½ log 5:
g_+^0(t) = (log2/√2)F(t−log 2) + (log3/√3)F(t−log 3) + (log2/2)F(t−log 4) (PROVED, sostenido por finitud local).
§4–§5: la ecuación derivada no es independiente (ver R161_013). Cotejo: U2 sí en «rango finito»: cámara finita
2,3,4; resto no.

### R161_013_FIRST_COLLAR_TRANSMISSION.md
Objeto: Y_3(F) como en (3.2); transmisión exacta: Y_3(F) = D_ΓF − r_ε en el colar interior y = g_+^0 en el
exterior (PROVED). §3: [Q,Z_+]F = Z_+B_+F se reduce a tautología en el colar (REJECTED como segunda fila; PROVED).
§4: con D_Γ = Q + C_log Q C_log, ecuación no local Y_3(F) − tF + r_ε = C_logQC_logF en el colar interior (PROVED
como ecuación); su consecuencia de rigidez OPEN. Cotejo: U2 sí: usa el operador de posición Q y la palabra
C_log Q C_log restringida a un colar de la ventana; sin signo; U1, U3, U4, U5 no.

### R161_014_SONIN_GAMMA_COERCIVITY.md
Objeto: Teorema 2.1 (PROVED, elemental y sostenido): si g ∈ Dom Q, sop g ⊂ [T,∞) y C_log g = σg, entonces
⟨D_Γg,g⟩ = 2⟨Qg,g⟩ = 2T‖g‖² + 2∫(t−T)|g|² ≥ 2T‖g‖², igualdad sólo en g = 0. Energía de exceso
E_T^PC(F) = 2‖(Q−T)^{1/2}g‖². Cor. 3.1 (PROVED CONDITIONALLY; usa una equivalencia externa): cierre si
E_T^PC ≤ 0 en el radical. §1 dominio: G′ ∈ L² (ARGUED con la misma convexidad). Meta (5.2) OPEN. Cotejo: U2 sí:
operador de posición Q compuesto con la reflexión C_log; la coercividad es exactamente el fenómeno «multiplicador +
reflexión en un sector de paridad» de R3-a (ε⟨X²F,F⟩ análogo con X en lugar de X²); U1, U3, U4, U5 no.

### R161_015_CANONICAL_HARDY_GAUGE_AND_NORM_SLOPE.md
Objeto: calibre canónico Θ_T(s) = e^{−T(s−1)}/s (núcleo reproductor normalizado), G_+^can, contorno móvil
G_{T,δ}(τ) = e^{Tδ}G_+^can(1/2+δ+iτ), g_δ(t) = e^{−δ(t−T)}g(t), N_T(δ) = ‖g_δ‖². Teorema 3.1 (PROVED, sostenido):
N_T′(0+) = −2∫(t−T)|g|² = −E_T^PC(F) ≤ 0. La desigualdad buscada es N_T′(0+) ≥ 0 («teorema del mínimo del puerto»,
OPEN). §5: el obstáculo de calibre de la fase 116 (sumar δh a un puerto y −δh al otro) queda reducido a la parte de
Sonin. Cotejo: U2 sí (posición: momento ∫(t−T)|g|²); U1, U3, U4, U5 no.

### R161_016_MARKOV_PULLBACK_AND_ARROW_AUDIT.md
Objeto: comparación entre el defecto de Markov Euler–Gamma (contracciones M_δ con defecto de Julia
D_δ = (I − M_δ*M_δ)^{1/2}) y la norma de Hardy. Prop. 1.1 (obstrucción de flecha; PROVED, sostenido): una contracción
que identifica entrada con el puerto crítico y salida con el desplazado sólo da N_T(0) − N_T(δ) = ‖D_δE_0g‖² ≥ 0,
la dirección ya conocida. Teorema 2.1 (PROVED CONDITIONALLY): cierre si existe (2.2)
N_T(δ) − N_T(0) = ‖D E^phys F‖² + R, liminf R/δ ≥ 0. §3 (PROVED en la clase de límites fuertes acotados): E_N^ren → 0
no puede ser la dispersión de orden cero; Gram de puertos ± difieren en S_a + S_{−a} ≠ 0. §4 (PROVED por el teorema
de divergencia de la fase 116, CITED): la familia etiquetada de innovaciones de Julia {d_{n,δ}J_{log n,−}F}_n tiene
energía exterior divergente; no puede completarse ortogonalmente y sumarse después; el orden norma/síntesis no
conmuta. §5 (PROVED): los datos finitos 2,3,4 controlan sólo el primer colar, no la pendiente global. Abiertas: (2.2)
global y la ruta local Y_3(F) = 0. Cotejo: U5 sí, como antecedente: la «suma directa etiquetada antes de sintetizar»
(que es lo que una dilatación isométrica de fuente proveería) choca con la divergencia de energía exterior de la
fase 116; y la contracción con defecto de Julia (dilatación de Sz.-Nagy implícita) da la flecha equivocada; U2 sí
(compresión/colar finito); U1, U3, U4 no.

### R161_017_EXACT_SCATTERING_DEFECT.md
Objeto: Teorema 2.1 (PROVED, sostenido; cálculo directo con ζ′(s) + χ(s)ζ′(1−s) = (χ′/χ)ζ):
G_+ + χG_− = ζ(s)W_ε, W_ε = d_ΓK_F − Q_+ − Q_−, d_Γ = −χ′/χ. (3.3): (W_ε)^∨ = D_ΓF − B_+F − B_−F = r_ε en la ventana
(PROVED). Cor. 5.1 (PROVED CONDITIONALLY): dispersión física exacta ⇒ r_ε = 0. La afirmación de que quedaría un
problema homogéneo abierto queda corregida por R161_019. Cotejo: U1–U5 no (U2 sólo en que la corrección polar es de
soporte exterior y no altera la restricción a la ventana).

### R161_018_PC_GRAPH_COMPARISON_NO_GO.md
Objeto: split w_ε = A_∞u + h_+ + h_−; comparación (2.3)–(2.4) ⇒ ZA_∞u = 0 = [Z,D_Γ]. Teorema 2.1 y Cor. 5.1
(etiquetados PROVED: «no hay cierre lineal por PC»). Nota de auditoría de dominio al inicio (de R161_075): la
identificación ZA_∞ = [Z,D_Γ] = 0 y la exclusión universal de límites lineales NO están establecidas; multiplicación
L², distribucional y meromorfa tienen implicaciones distintas. Estado actual: la etiqueta PROVED no se sostiene;
léase ARGUED/sin probar. Lo que sí queda: la necesidad de retener un defecto cuadrático finito es una conclusión
de diseño, no un teorema. Cotejo: U1–U5 no.

### R161_019_GAMMA_POLE_LATTICE_RIGIDITY.md
Objeto: polos de d_Γ = −log π + ½ψ((1−s)/2) + ½ψ(s/2) en s = 3, 5, 7, …; Lema 2.1 (PROVED): anulación de W_ε^0 ⇒
K_F(2m+1/2) = 0, m ≥ 1. Teorema 3.1 (PROVED, sostenido; independiente de toda equivalencia externa): si
∫_{−T}^T F(t)e^{−(2m+1/2)t}dt = 0 para todo m ≥ 1, F = 0 (cambio x = e^{−2t}, densidad de {x^m, m ≥ 1} en L²(a,b),
a > 0). Teorema 4.1 (PROVED CONDITIONAL a la dispersión física). Corrige R161_017 §5. Cotejo: U1–U5 no.

### R161_020_COMPRESSED_SCATTERING_AND_LEAKAGE_SQUARE.md
Objeto: Lema 1.1 (PROVED, elemental): si U unitario, Pg = g y PUg = λg con |λ| = 1, entonces Ug = λg. Cuadrado de
fuga L_T^sc(g) = ‖(I−P_+)C_log g‖² = ‖g‖² − ‖P_+C_log g‖² ≥ 0 (PROVED); con error e, L = −2σRe⟨g,e⟩ − ‖e‖².
Forma de Hardy (4.1)–(4.3) (PROVED). L161.4 (OPEN): normalización V_{M,N,T}F con
lim‖H_T^− E_N^ren V F‖² = L_T^sc(F) y anulación en el radical; sin construir. Cotejo: U2 sí, de lleno: fuga de
compresión ‖(I−P)·Pg‖² de un unitario (P a la semirrecta [T,∞), no a la ventana); la identificación con el defecto
finito de PC quedó sin objeto; U5 roza (la rigidez de compresión unitaria es la versión «sin dilatación»); U1, U3,
U4 no.

### R161_021_EXTREMAL_CROSS_CORRELATION.md
Objeto: Lema 1.1 (PROVED, elemental): con C involución autoadjunta, Pg = g, e = PCg − σg: Re⟨g,e⟩ = ⟨g,Cg⟩ − σ‖g‖²,
‖g − σCg‖² = −2σRe⟨g,e⟩. X_T(F) = ‖g‖² + ε⟨g,Cg⟩ = ½‖(I+εC)g‖² ≥ 0. Forma de Mellin X_T = Re⟨G_+^0, ζW_ε^0⟩
(PROVED). §4: radicalidad a_T(F,H) = 0 ∀H primitivo; buscar test conjugado H_F con a_T(F,H_F) = X_T(F). L161.5 OPEN.
Cotejo: U3 roza: trabaja con un vector del radical de una forma semidefinida (vector neutro radical), no con
uno no radical de una forma indefinida; U2 sí (compresión P y fuga); U1, U4, U5 no.

### R161_022_CANONICAL_CONJUGATE_TEST_AND_BOUNDARY_RECIPROCITY.md
Objeto: test canónico H_F = Π_T P_T Z*g (primitivo; a_T(F,H_F) = 0). Teorema 3.1 (PROVED en el grafo común):
X_T(F) = Re[⟨r, Τ P y⟩ + ⟨ℓ,(I−P)y⟩ + ⟨d,y⟩], y = Z*g, d = w − AF con Pd = 0. Reciprocidad exterior (4.2) OPEN.
Versión finita (5.1) con y_{M,N} = (S_N^ren)*g_{M,N}: DEFINIDA, convergencia OPEN. Corregido por R161_023 (colapso
tautológico). Cotejo: U2 sí, de lleno: descomposición Π + Tate + exterior de una palabra Π P Z* con compresión; el
bloque de Tate cruzado aparece como B_T^Tate = Re⟨r, Τ P Z*g⟩; U1, U3, U4, U5 no.

### R161_023_CONJUGATE_TEST_COLLAPSE_AND_TRUE_RECIPROCITY_GATE.md
Objeto: (1.3) ⟨r, Τ P y_N⟩ = ⟨Sr, g_N⟩ (PROVED); el término de Tate más la fuga de Weil exterior recombinan en
⟨S AF, g_N⟩ = ⟨R^ren 𝓕F, g_N⟩, el emparejamiento mixto de (PC-ren) (PROVED); añadiendo d se reconstruye X_T (PROVED).
§4: la matriz de Gram positiva de Tate es G_T = 2[[sinh T, T],[T, sinh T]]; la del sistema de colar es la cruzada
G_TC = 2[[T, sinh T],[sinh T, T]], indefinida; usarla como Gram da signo falso (REJECTED). L161.6 (OPEN): ley de borde
antisimétrica independiente que distinga ⟨g_N, S w_N⟩ de ⟨S*g_N, w_N⟩ por su borde móvil. Cotejo: U2 sí: es la
prueba de que la palabra «test conjugado por compresión Π P S*» es tautológica con la radicalidad; U3 sí, en
negativo: la forma indefinida disponible (matriz de Tate cruzada) se rechaza como Gram; no se estudia vector neutro;
U1, U4, U5 no.

### R161_024_POLE_REMOVABILITY_IS_ENOUGH.md
Objeto: Teorema 1.1 (PROVED, sostenido): si W_ε^0 es holomorfa en s_m = 2m+1, m ≥ 1, entonces F = 0. Equivalencias
§2 (PROVED). §3: el atajo de conmutador de soporte (I−P_+)M_χP_+ (bloque de Hankel) es CIRCULAR (CITED fase 114:
su anulación es interioridad del multiplicador). §5: probar contra exponenciales altas directamente está REJECTED
(auditoría de momentos de la fase 121). L161.7 OPEN, superado por L161.8. Corrección final: no hay segundo residuo
que cancele el de Gamma. Cotejo: U2 sí: el bloque de Hankel de compresión (I−P_+)M_χP_+ se descarta como
circular; U1, U3, U4, U5 no.

### R161_025_EXACT_GAMMA_RESIDUE_ENERGY.md
Objeto: Res_{s=2m+1} d_Γ = 1; Res[ζW_ε^0] = ζ(2m+1)K_F(2m+1/2) (PROVED, sostenido; comprobado también vía
G_−^0(s_m) = −ζ′(−2m)K_F(a_m)). §2: el paso lineal al semiplano seguro es insuficiente (convergencia local uniforme en
círculos ya contiene el teorema). Energía D_T^pole(F) = Σ 2^{−m}a_m e^{−2a_mT}|K_F(a_m)|² ≥ 0, fiel (Teorema 3.1,
PROVED). L161.8 OPEN. Cotejo: U1–U5 no.

### R161_026_GAMMA_POLE_ENERGY_IS_A_HANKEL_BOUNDARY_DERIVATIVE.md
Objeto: k_Γ^+(v) = c_Γ(v) − e^{−v/2} = Σ_{m≥1}e^{−a_mv}; B_{T,δ}^Γ(F) = Σ e^{−2a_m(T+δ)}|K_F(a_m)|²,
D_{T,δ}^Γ = Σ a_m e^{−2a_m(T+δ)}|K_F(a_m)|² = −½∂_δB ≥ 0. Teorema 3.1 (PROVED): núcleos de Hankel
k_Γ^+(2T+2δ+t+u) y −(k_Γ^+)′(·). D_T^pole = 2^{1/4}D_{T,δ_0}^Γ con δ_0 = (log 2)/4 (PROVED). Observación acotada
R^Γ_{T,δ} a ℓ² con D = ‖R F‖² (PROVED). L161.9 OPEN: signo inverso ∂_δB ≥ 0 en el radical. Cotejo: U2 roza
(observación de rango infinito, no compresión de ventana); U5 no (R^Γ no es isométrica); U1, U3, U4 no.

### R161_027_METHOD_OF_IMAGES_AND_PRIME_FORCE_AUDIT.md
Objeto: imagen reflejada (M_{T,δ}F)(x) = F(−x−2L), L = T+δ; Teorema 2.1 (PROVED): B^Γ = ⟨F, C_{k_Γ^+}M_{T,δ}F⟩,
D^Γ = −½∂_δ⟨F, C M F⟩. Contacto primo I_{a,T,δ}(F) = ⟨F, τ_aM F⟩; su derivada en δ no tiene signo (PROVED por
ejemplo: cambio de fase de F). Fuerza prima B^prime = Σ Λ(n)/√n [I + Ī] indefinida («signo fijo: FALSE»). §5: una ley
de conservación ∂_δ(B^Γ − B^prime) = 0 no basta; L161.10 (OPEN): 0 = 2D^Γ + D^Poisson + o(1) con D^Poisson ≥ 0 del
defecto de borde aditivo. Cotejo: U3 roza: registra que «2D^Γ − D^Poisson = 0» es una conservación de Green
indefinida que no cierra; U2 roza (el imagen está fuera de la ventana; la reflexión con traslación es una palabra
JτQ); U1 no (Λ ≥ 0 lineal); U4 no; U5 no.

---

## 2. Síntesis

### (a) Piezas PROVED reutilizables (independientes de toda equivalencia externa)

1. Identidad finita (PC) y su versión (PC-ren): R161_001 Thm 3.1; R161_003 §3.
2. Soporte de la hipérbola y defecto interior para peso general δ_a(k) = Σ_{d|k}a(d) − log k: R161_001 Thms 2.1, 4.1.
3. Ceguera de signo de ‖S_N A_M 𝓕F‖² y de sus sumas positivas: R161_002 Thm 1.1, Cor. 1.2.
4. No hay telescopado positivo de los restos de hipérbola; salto terminal −log p en primos: R161_002 Thm 8.1, Cor. 8.2.
5. Obstrucción del truncamiento crudo y convergencia renormalizada; representación retículo menos continuo y soporte
   de la capa polar en datos con momento de Tate nulo: R161_003 Prop. 1.1, Thms 2.1, 2.2.
6. Estabilización P_T S_N P_T = Z_{T,−}, nilpotencia; álgebra finita de la cámara 0.8 < T < ½ log 5:
   R161_004 Prop. 1.1; R161_005 §4.
7. Núcleo exacto del puerto exterior P S_N^ren (1−P) = Δ^R − e^{−t/2}a_−: R161_006 Thm 2.1, (3.2).
8. Identidad del defecto de la ecuación funcional G_+ + χG_− = ζW_ε: R161_017 Thm 2.1.
9. Completitud de momentos exponenciales {e^{−(2m+1/2)t}}_{m≥1} en L²(−T,T): R161_019 Thm 3.1.
10. Residuos Res d_Γ = 1 en 2m+1; energía de polos fiel; identidad de Hankel Gamma y método de imágenes:
    R161_025 §1, Thm 3.1; R161_026 Thm 3.1, §5; R161_027 Thm 2.1.
11. Lemas hilbertianos elementales: rigidez de compresión unitaria y cuadrado de fuga (R161_020 Lema 1.1, (3.2),
    (3.4)); correlación extremal para involuciones (R161_021 Lema 1.1); coercividad de Q en sectores de C_log con
    soporte en [T,∞) (R161_014 Thm 2.1); pendiente de norma −2∫(t−T)|g|² (R161_015 Thm 3.1); flecha de una
    contracción con defecto de Julia (R161_016 Prop. 1.1).
12. Proyección de Tate: ⟨r, ΤPy⟩ = ⟨r,y⟩; Gram de Tate positiva G_T frente a la cruzada G_TC indefinida:
    R161_023 (1.1)–(1.3), §4.

### (b) Cierres con clase y falsificador

- Cuadrados de (PC) y sumas no negativas de ellos: ciegos al signo (A ↦ −A). R161_002 Thm 1.1.
- Ponderaciones w_N ≥ 0 de los restos de hipérbola: nunca se cancelan (coeficiente log p·Σ_{N<p}w_N > 0 en primos
  grandes). R161_002 Thm 8.1.
- Emparejamiento orientado sin compresión: se reduce al desplazamiento de ventana (CITED R160_D4_R2 Thm 5.1).
  R161_002 §3.
- Versión escalar de L161.2 (primitiva de Stieltjes D(u)): clase de Paper 41 C4–C5, cuadrado de signo equivocado y
  densidad negativa bajo log 2. R161_004 Cor. 2.1.
- Levantamiento por fibras de divisores Λ(d)/log N, varianza condicional, Möbius unitriangular: hueco espectral nulo
  (padres primos), diagonal identidad aniquilada al derivar. R161_004 Cor. 3.1 (CITED 104/106/121).
- Segunda fila por [Q,Z_+] = Z_+B_+: tautológica en el colar. R161_013 §3.
- Contracción directa de Markov: flecha automática, falsificador = cualquier contracción (no usa aritmética).
  R161_016 Prop. 1.1.
- E_N^ren como dispersión de orden cero: imposible en límites fuertes acotados. R161_016 §3.
- Suma ortogonal de innovaciones etiquetadas antes de sintetizar: energía divergente (CITED fase 116). R161_016 §4.
- Test conjugado Π_T P_T Z*g: tautológico con la radicalidad. R161_023 §§2–3.
- Matriz de Tate cruzada como Gram: signo falso. R161_023 §4.
- Conmutador de soporte (I−P_+)M_χP_+: circular (CITED fase 114). R161_024 §3.
- Paso lineal al semiplano seguro: insuficiente. R161_025 §2.
- Fuerza prima cruda por imágenes: indefinida (falsificador: cambio de fase de F). R161_027 §§3–4.
- Split lineal del grafo PC (R161_018): la etiqueta NO-GO no se sostiene tras la auditoría de dominio de R161_075.

### (c) Explícitamente abierto, con obstáculo exacto

- SP-161 / L161.1 (R161_002 §§4–5): a_T = Σ w_N Re⟨R_{M,N}F, S_N𝓕F⟩ + cuadrados de fuga de C_T = (1−P_T)𝓕P_T y
  C_T^{(N)} = (1−P_T)S_N𝓕Π_T. Sólo murió la rama de pesos positivos; la versión con pesos con signo o derivadas
  discretas y con las fugas comprimidas nunca se escribió.
- L161.3 / PC-port (R161_005–006): signo u objeto para los restos Δ^R ℓ_T(F), Δ^L ℓ_T(F) (discrepancias
  unilaterales enteros menos continuo de la fuga exterior de Weil).
- L161.4 (R161_020): identificar la fuga ‖(I−P_+)C_log g‖² con un límite proyectado de ‖H_T^−E_N^ren V F‖²;
  falta la normalización V no circular.
- L161.5–L161.6 (R161_021–023): ley de borde antisimétrica independiente de la radicalidad que distinga
  ⟨g_N, S w_N⟩ de ⟨S*g_N, w_N⟩ por el borde móvil.
- Teorema del mínimo del puerto / pullback inverso (R161_015–016): N_T(δ) − N_T(0) = cuadrado + R con liminf R/δ ≥ 0;
  falta una dispersión de orden cero que invierta entrada y salida.
- Ruta local 2,3,4 (R161_013, R161_016 §5): forzar Y_3(F) = 0 en un colar con la ecuación no local
  Y_3 − tF + r_ε = C_logQC_logF.
- L161.8–L161.10 (R161_025–027): realizar D^pole o −∂_δB^Γ desde (PC-ren) con el signo inverso; completar la fuerza
  prima combinada en un cuadrado de Poisson del mismo signo (0 = 2D^Γ + D^Poisson).
Todas estas metas, salvo SP-161, están formuladas sobre un vector del radical y dependen de una equivalencia
externa para concluir; ninguna es una identidad (G) sobre todo P_T.

### (d) Lo que ya recorre U1–U5 y razón registrada del fracaso

- U1: nada en este tramo. Λ∗1 = log entra sólo linealmente (R161_001 Thm 4.1: átomo δ_a(k); R161_007: producto de
  series de Dirichlet). R161_002 §6 pide la prueba «Λ(2) ↦ −Λ(2)», lineal. No hay término cuadrático en el peso.
- U2: es el terreno central del tramo, siempre sobre el radical y sin signo para todo P_T.
  · SP-161 (R161_002 §§3–4): forma propuesta «a_T = emparejamientos orientados + fugas de compresión», OPEN sin objeto;
    sólo se cerró la rama de pesos positivos (Thm 8.1), no la de fugas.
  · Compresión doble P S_N P = observación causal vieja (R161_004 Prop. 1.1): lo nuevo debe salir del bloque
    P S_N (1−P), cuyo núcleo exacto es R161_006; sin signo.
  · Fuga unitaria ‖(I−P_+)C_log g‖² (R161_020) y correlación X_T = ½‖(I+εC)g‖² (R161_021): cuadrados correctos, pero
    no hay identidad que los conecte con el defecto finito de PC; L161.4/5 OPEN.
  · Palabra Π_T P_T S* como test (R161_022–023): colapsa en el emparejamiento mixto de (PC-ren) — tautología.
  · Operador de posición: D_Γ = Q + C_logQC_log da coercividad 2T‖g‖² en sectores de Sonin (R161_014) y la pendiente
    −2∫(t−T)|g|² (R161_015); el signo producido es siempre el automático (R161_016 Prop. 1.1).
  · Bloque de Hankel (I−P_+)M_χP_+: circular (R161_024 §3).
  · Rango finito: cámara 2,3,4; controla sólo el primer colar (R161_016 §5); la fila derivada es tautológica
    (R161_013 §3).
  · Contabilidad con el bloque de Tate cruzado: R161_009 fija (α,β) por la matriz cruzada; R161_022 aísla
    B_T^Tate; R161_023 prueba que ⟨r,ΤPy⟩ = ⟨Sr,g⟩ y que la matriz cruzada no es Gram. La versión positiva por
    paridad (README ítem 22, memo R161_032) queda fuera de este tramo; README ítem 33 dice que en el orden de derivada
    de fuente ese bloque se anula por paridad opuesta.
- U3: no se construye vector neutro no radical. Contactos: matriz cruzada de Tate indefinida rechazada como Gram
  (R161_023 §4); inercia de Kreĭn de la sombra escalar de la fase 116 citada (R161_011 §1); «2D^Γ − D^Poisson = 0»
  descartada por ser conservación indefinida (R161_027 §5). Todo el programa usa vectores radicales de una forma
  semidefinida (R161_021 §4).
- U4: no hay Möbius truncado. El análogo con Λ es el resto de hipérbola h(k) = Σ_{dm=k,d≤M,m≤N}Λ(d) en k > N
  (R161_001 Thm 2.1): coeficientes ≥ 0 que no hacen positiva la suma de traslaciones (R161_001 §6, R161_027 §4), y
  ninguna ponderación positiva en N los cancela (R161_002 Thm 8.1). El resto con pesos de Möbius c_N(k) no aparece.
- U5: la salida A de R161_033 está fuera del tramo. Antecedentes en este tramo: R161_016 §4 — completar la familia
  etiquetada de innovaciones de Julia en suma ortogonal y sumar después está bloqueado por la divergencia de
  energía exterior (fase 116); R161_016 §1 — la contracción con defecto de Julia da la flecha automática. README
  ítem 23 (resumen de memo posterior) pide explícitamente «una dilatación de Parseval/Naimark» para pasar de la suma
  coherente a la suma directa.

### (e) Inconsistencias entre memos

1. R161_010 Thm 3.1 se dio PROVED; retractado por R161_011 (falta la dispersión coseno). El README lo registra.
2. R161_017 §5 afirma que tras la dispersión quedaría el problema homogéneo; R161_019 lo corrige (red de polos).
3. R161_018 se titula NO-GO y su Cor. 5.1 dice PROVED; la nota inicial (de R161_075) declara la identificación
   ZA_∞ = [Z,D_Γ] = 0 no establecida. El README ítem 8 y R161_019, 020, 025 siguen apoyándose en R161_018 como
   probado.
4. R161_024 describe «cancelación por el residuo continuo/Tate»; su propia corrección final dice que no hay residuo
   que cancele. R161_025 lo confirma.
5. R161_008 Thm 3.1 etiqueta PROVED la pertenencia a H²; el paso de Paley–Wiener en la banda 0 < Re z ≤ 1/2 no
   escribe control de crecimiento (ARGUED en ese punto). R161_014 §1 (dominio de G′) igual.
6. README ítem 21 afirma que la costura de divisores se anula; el ítem 23 lo matiza (falta el paso de Gram coherente);
   ambos son resúmenes de memos fuera del tramo.
7. Status de R161_003 dice «L161.3 OPEN», objeto definido recién en R161_004: anotación retroactiva, no
   contradicción.

### (f) Archivos leídos (lectura completa con Read)

README.md (298 líneas), R161_000 (85), R161_001 (185), R161_002 (183), R161_003 (216), R161_004 (193),
R161_005 (153), R161_006 (123), R161_007 (137), R161_008 (178), R161_009 (156), R161_010 (200), R161_011 (148),
R161_012 (149), R161_013 (127), R161_014 (159), R161_015 (175), R161_016 (231), R161_017 (227), R161_018 (203),
R161_019 (196), R161_020 (187), R161_021 (171), R161_022 (199), R161_023 (149), R161_024 (173), R161_025 (169),
R161_026 (192), R161_027 (167). Veintinueve archivos, todos leídos enteros. `scripts/` sólo listado.
