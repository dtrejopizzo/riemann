# Anexo: fase 170, archivos R170_823 a R170_840

Registro de lectura completa de los dieciocho archivos R170_823–R170_840 de
`03-research/phase-170-global-prime-inequality/`. No se propone ninguna construcción. Para cada
memo: objeto, afirmaciones (etiqueta declarada / lo que el texto sostiene), punto de detención,
memo posterior que la corrige o audita, y cotejo con el terreno no excluido T1–T4 de la ronda 1.

Notación común del tramo. N = ⌈e^{2T}⌉, M ≥ N. S_N = Σ_{n≤N} n^{-1/2} τ_{log n},
K_N = Σ_{n≤N} (log n) n^{-1/2} τ_{log n}, L_M = Σ_{d≤M} Λ(d) d^{-1/2} τ_{log d},
A_M = m(D) − (L_M + L_M^*), E_N = S_N 𝓕 − J S_N (defecto de Poisson), H_{M,N} = L_M S_N − K_N =
Σ_{k>N} h_{M,N}(k) k^{-1/2} τ_{log k} con h_{M,N}(k) = Σ_{dm=k, d≤M, m≤N} Λ(d). «PC» es la identidad
finita de Poisson–Chebyshev S_N A_M 𝓕 = {X,E_N} − L_M^* E_N − J H_{M,N} − H_{M,N} 𝓕.
Z = ker H_T es el radical de un primer contacto hipotético; R_L los L momentos Gamma
(a_m = 2m+½); D_{N,L} la contracción Gamma–Euler; D_Δ = R_L^*(I − D_{N,L}) R_L ⪰ (1−q_0) R_L^*R_L,
q_0 = log2/4 + 1/16.

Todo el tramo trabaja en el marco «primer contacto ⟹ radical finito ⟹ probar R_L F = 0», no sobre
una identidad (G) a_T = ‖V_T F‖² + ρ_T del tipo que busca la fase 212.

---

## R170_823 — Promedio multiescala de Poisson–Chebyshev

**Objeto.** Peso fijo w ∈ C_c^k((ρ_0,1)), ∫w = 1 (o perfil w_h(ρ) = h^{-1}W((1−ρ)/h)), promedio
débil ⟨B⟩_w = ∫ w(ρ) B_ρ dρ de la PC conjugada por la dilatación D_ρ:
S_ρ A_ρ U_ρ = {ρX, E_ρ} − L_ρ^* E_ρ − J H_ρ − H_ρ U_ρ, U_ρ = D_ρ^* 𝓕 D_ρ (5); su promedio (APC).
H_ρ = Σ_{N<j≤MN} h_{M,N}(j) j^{-1/2} τ_{log j/ρ} conserva los coeficientes exactos (6).
Operador T_{a,w} = ∫ w(ρ) τ_{a/ρ} dρ con multiplicador q_{a,w}(ξ) = ∫ η(s) e^{-iaξs} ds,
η(s) = w(1/s)s^{-2} (9)–(10). Interfaz exacta (24) entre ∫w(Φ_ρ + 𝓔_ρ^int) y cuatro líneas: PC
ordenada vía χ^{(ρ)}, conmutador [A_ρ,S_ρ], defecto A_1 − A_ρ = m(D) − m(D/ρ) − (L_1+L_1^*) +
(L_ρ+L_ρ^*), y error de alineación con la energía interior 𝓔_ρ^int = (1−ρ)^{-1} a_M(δ_ρ,δ_ρ) ≥ 0.

**Afirmaciones.**
- (11)–(12) T_{a,w}: L² → H^k acotado, a ≠ 0. Declarada como hecho probado; sostenida (integración
  por partes en el multiplicador, sin términos de borde).
- (13)–(17) P_T T_{a,w} P_T Hilbert–Schmidt, con ‖κ‖₂² = |a|^{-1}∫ρ²|w|²; cota HS (17) para
  P_T⟨H_ρ⟩_w P_T. Sostenida.
- (19) ‖T_{a,w} − τ_a‖ ≥ 1: restar contra la escala uno no es pequeño. Sostenida (Riemann–Lebesgue).
- (24) interfaz exacta; sostenida como identidad (supone el mismo par de correctores primitivos en
  todo el intervalo de escalas).
- No se prueba compacidad del collar acoplado ⟨H_ρ U_ρ⟩_w ni signo alguno. Declarado OPEN.

**Detención.** Ninguna línea de (24) tiene signo; la compacidad se prueba sólo para el bloque
desacoplado; la constante no es uniforme en T, N, M ni en h → 0. El dominio del generador de
dilatación 𝒜 = −½ − t∂_t no está probado para vectores de primer contacto (§6).

**Corrección/auditoría.** R170_824 (tres correcciones de la primera versión: orden S_ρA_ρ vs A_ρS_ρ,
soporte del núcleo en u = −a/ρ, retiro de la afirmación de núcleo acotado para P_T H_ρ U_ρ P_T).
R170_825 cierra la compacidad del collar acoplado.

**Cotejo T1–T4.** T1: sí, parcialmente — es un promedio con peso w sobre la dilatación, pero no
produce cuadrados ni signo; sólo regularidad/compacidad. T2: no. T3: Λ∗1 = log sólo en la ausencia
de coeficientes j ≤ N de H_ρ. T4: toca la cola Σ_{k>N} h(k) k^{-1/2} τ, pero como operador
promediado (compacto), no como suma Σ h(k)|ℓ_k(F)|² con h ≥ 0.

## R170_824 — Auditoría de la pieza multiescala

**Objeto.** Auditoría de R170_823.

**Afirmaciones.** Acepta: ganancia de derivadas de T_{a,w}, HS tras compresión, preservación exacta
de h_{M,N}(k); ‖T_{a,w} − τ_a‖ ≥ 1; interfaz (24) con cuatro bloques. No acepta compacidad ni signo
para ∫w H_ρ U_ρ. Registra y corrige tres errores de la primera versión (doble orden, orientación del
núcleo, núcleo acotado retirado). Etiquetas coherentes con el texto.

**Detención.** Ningún bloque de (24) tiene signo; convertir compacidad en signo requeriría otro
insumo aritmético.

**Cotejo.** Igual que R170_823; ninguno de T1–T4 avanza.

## R170_825 — Fase del collar promediado acoplado

**Objeto.** C_{a,w} = ∫ w(ρ) τ_{a/ρ} U_ρ dρ = q_{a,w}(D) J con
q_{a,w}(ξ) = ∫ η(s) e^{i[θ(sξ) − asξ]} ds, θ' = m (5)–(6). Derivada de fase ξ[m(sξ) − a].

**Afirmaciones.**
- m par, estrictamente creciente en [0,∞) (serie de Bernstein de P47), m(0) = −5.372…; punto
  estacionario confinado a ρ_0 r_a ≤ |ξ| ≤ r_a, r_a = m^{-1}(a) (9). Sostenida.
- Para la orientación opuesta (m + a), raíces sólo si 0 < a ≤ −m(0), es decir k ≤ 215 para a = log k
  (10). Sostenida.
- |q| ≤ A_w/|ξ| para |ξ| ≥ B_a = 2πe^{a+2}, A_w = ‖η'‖₁ + C_m‖η/s‖₁ (13)–(14); C_{a,w}: L² → H¹ (17);
  ‖P_T C_{a,w} P_T‖²_HS ≤ (T/π)(2B_a‖w‖₁² + 2A_w²/B_a) (18); cota (20) para el bloque aritmético
  finito. Sostenidas (sólo una derivada; no se reclama más).
- Cota no uniforme: B_{log k} = 2πe²k da crecimiento k^{1/2}, que compensa k^{-1/2}.

**Detención.** HS ≠ signo; no uniforme en cortes; no controla las otras líneas de (24).

**Corrección/auditoría.** R170_826 la acepta.

**Cotejo.** T1: sigue siendo promedio de dilatación sin cuadrado. T4: el bloque Σ_{N<k≤MN}
h(k) k^{-1/2} C_{log k,w} es la cola de T4 en forma de operador, sin forma diagonal |ℓ_k(F)|² ni signo.
T2, T3: no.

## R170_826 — Auditoría del collar multiescala acoplado

**Objeto.** Auditoría de R170_825.

**Afirmaciones.** Acepta fase, signo de la derivada, localización del punto estacionario, cota
A_w/|ξ|, L² → H¹, HS local. Señala: constante creciente con a = log k, no uniforme; HS significa
compacidad, no signo; un compacto autoadjunto tiene autovalores de ambos signos.

**Detención.** Pide explotar la matriz sobre el radical junto con Tate, Gamma y alineación (lo hace
R170_827).

**Cotejo.** Ninguno de T1–T4 avanza.

## R170_827 — Matriz multiescala sobre el radical

**Objeto.** Base F_1…F_d de Z (sin separar paridades), Gram fiel B_ij = ⟨R_L F_j, R_L F_i⟩ ≻ 0.
Forma q_ms(F) = ∫ w(Φ_ρ + 𝓔_ρ^int); matrices K = P + E con E_ij = ∫ w/(1−ρ) a_M(δ_ρF_j, δ_ρF_i) ⪰ 0,
y Q = K (hermitización conjunta de las cuatro líneas, (10)–(11a)). Collar autoadjunto:
q_{a,w}(−ξ) = conj q_{a,w}(ξ) ⟹ C_{a,w} = C_{a,w}^* (18). Valores singulares
s_{r+1} ≤ ‖𝒞‖_HS/√(r+1) (21a). Criterio espectral: q_ms ≤ 0 en Z ⟺ λ_max(B^{-1/2}KB^{-1/2}) ≤ 0 (25).
Mapa matricial de cierre: P − (1−q_0)B ⪰ 0 y P + E ⪯ 0 juntos dan contradicción (28a)–(28b).

**Afirmaciones.** B ≻ 0, hermitización correcta, autoadjunción del collar, (21a), (25): sostenidas
(álgebra finita y min–max). Las dos desigualdades (28a): OPEN, declaradas no probadas. Advierte que
(27) (reserva Gamma–Euler) no puede sumarse a (8) sin identidad conjunta.

**Detención.** Faltan ambas desigualdades de (28a); además la reducción no usa la minimalidad
dinámica del primer contacto (vale para cualquier modo nulo de H_T ≥ 0).

**Corrección/auditoría.** R170_828 (corrige doble conteo de la primera versión: el residuo de cuatro
líneas más la energía interior otra vez; queda Q = K = P + E).

**Cotejo.** T1–T4: no. Es un criterio finito de Rayleigh sobre el radical, sin mecanismo de signo.

## R170_828 — Auditoría de la matriz del radical

**Objeto.** Auditoría de R170_827.

**Afirmaciones.** Valida seis puntos (B ≻ 0, hermitización, no invariancia de paridad, autoadjunción,
cota de valores singulares, normalización). Registra el doble conteo corregido. Reafirma que
D_Δ ⪰ (1−q_0)B no prueba que P la domine; insertarlo sin identidad conjunta sería circular.

**Detención.** No uniforme en T; no usa minimalidad.

**Cotejo.** Ninguno de T1–T4.

## R170_829 — Puente matricial Gamma–Euler hacia el flujo multiescala

**Objeto.** Flujo exterior como defecto de transporte p(F) = Re e_F^{(1)}(z̄_F − g_F), con
z̄_F = ∫w S_ρU_ρ S_L F, g_F = S_L F, usando e_F^{(1)}(g_F) = 0 (5). Reserva d(F) = ⟨R_LF,(I−D)R_LF⟩.
Funcional Λz(F) = ⟨F, A_1 z⟩ − ⟨r_F, z⟩; ecuación de levantamiento Herm[Λ Y_L] = D_Δ (12).
Candidato exterior ι_+c = 1_{(T,∞)} Σ b_m c_m e^{-a_m t}, Y_+ = ι_+(I−D)R_L (14). Residuo exacto
R_GE = P − D_Δ = Q − E − D_Δ = Q − E − B − ½Q^{(1)} (18), (25), (26).

**Afirmaciones.**
- Obstrucción interior: si Yz tiene soporte en la ventana, Λz = 0 por la ecuación débil (13); ninguna
  síntesis interior (R_L^*CR_L, G_L, JG_LJ, S_L, adjunto del collar) resuelve (11). Sostenida.
- R_GE ⪰ 0 suficiente (no necesaria) para P − (1−q_0)B ⪰ 0. Sostenida; (32) equivale exactamente a
  la cota buscada (declarado: no asumirla).
- La identidad del collar R_LB_N = D_{N,L}R_L − 𝓔_{N,L} no transporta R_L S_ρ U_ρ S_L F (§5).
- Signo de R_GE: OPEN.

**Detención.** Ninguna identidad reduce R_GE a forma positiva; la minimalidad no aporta desigualdad
para el test exterior; Λι_+ no está calculado.

**Corrección/auditoría.** R170_830; R170_831 calcula Λι_+ y detecta el defecto de tipado del puerto
Tate.

**Cotejo.** T1–T4: no. (Menciona al final otro enunciado sólo como descargo; usa una equivalencia
externa sólo en ese descargo, sin desarrollo.)

## R170_830 — Auditoría del puente Gamma–Euler exterior

**Objeto.** Auditoría de R170_829.

**Afirmaciones.** D_Δ = B + ½Q^{(1)} verificado; D_Δ ≻ 0 sobre Z. Ecuación Herm(ΛY_L) = D_Δ
verificada; exclusión de todos los candidatos interiores exacta. Y_+ está en el dominio logarítmico
pese al salto, pero R_LB_N = D_NR_L − 𝓔 no calcula Λι_+ (faltan m(D), salto y Tate). Contribución
estructural: el levantamiento debe cruzar el borde.

**Detención.** Pide una fórmula de Green exterior para las colas exponenciales.

**Cotejo.** Ninguno de T1–T4.

## R170_831 — Fórmula Gamma–Euler exterior y defecto de tipado de Tate

**Objeto.** Lema 2.1: para z_a^+ = 1_{(T,∞)} e^{-as}, en I_T,
(A_1 z_a^+)(t) = −½ ∫_{T−t}^∞ K(u) e^{-a(t+u)} du − e^{-at} Σ_{d≤M, t>T−log d} Λ(d) d^{-a−1/2} (2.2),
con K(u) = 2Σ_j e^{-(2j+1/2)u}. Salto: m(D)z_a^+ ~ −(e^{-aT}/2) log(1/(T−t)) (3.1), no delta.
Reflejo g^-(t) = g^+(−t), con L_M^* en vez de L_M (4.1). Lema 5.1: r_F = α e^{-t/2} + β e^{t/2} en I_T
no determina ⟨r_F, z⟩ para z exterior. Ecuación matricial tras elegir puerto Θ_±:
Herm[(Γ_{+,M} − Θ_+)(I−D)R_L] = R_L^*(I−D)R_L (6.3).

**Afirmaciones (ledger propio).** Dominio de colas: PROVED (sostenido). Respuesta derecha/izquierda:
PROVED (sostenido; especialización del núcleo de R162_404 §4, declarado no nuevo). Salto logarítmico:
PROVED (sostenido). Identificación con collares truncados: PROVED. «Puerto Tate exterior determinado
por la ecuación débil»: FALSE (sostenido por Lema 5.1). Elección canónica Θ_±: OPEN. Ecuación (0.2):
OPEN.

**Detención.** Defecto de tipado: el término Tate no está definido sobre colas exteriores; elegir
Θ = 0 sería imponer una ley de transmisión (señalada abierta en P122_029).

**Corrección/auditoría.** R170_833 (valida); R170_834 refina.

**Cotejo.** T1–T4: no. Usa Λ(d) sólo linealmente en el collar primo.

## R170_832 — Mapa del rompecabezas v2

**Objeto.** Mapa de piezas R170_819–831 con cotejo contra fases 121, 122, 124, 155, 162. Divide el
hueco en G1 (puerto exterior Tate canónico), G2 (levantamiento orientado), G3 (ley de signo
aritmética con Λ∗1 = log esencial), G4 (minimalidad y uniformidad). Tabla «qué no reconstruir»:
P121 (localización Tate), P122_028–029 (complejo de Green, transmisión), P124_009 (fuga; contraejemplo
finito a Cauchy–Schwarz), P124_011 (Schur), R162_404, R162_301 (levantamiento Euler/Hankel indefinido),
R162_503 (suma–producto), colas exponenciales pequeñas.

**Afirmaciones.** Inventario; sin teoremas nuevos. §7 (añadido posterior) corrige G1: el puerto
Hardy de la fuente ya es canónico (R161_009, R161_015); falta un mapa fuente–puerto, no otro gauge;
lo independiente de gauge vive sólo en Z_0 = {r_F = 0}.

**Detención.** G1–G4 abiertos.

**Cotejo.** No toca T1–T4.

## R170_833 — Auditoría de la fórmula exterior

**Objeto.** Auditoría de R170_831.

**Afirmaciones.** Verifica dominio, núcleo, salto logarítmico, orientación primo/reflejo. Declara que
la fórmula de núcleo ya está en R162_404 §4 (no presentarla como nueva). Lo útil: el chequeo de tipos
(extensión por cero vs por caracteres globales dan puertos distintos). Θ_± parametriza, no construye.

**Detención.** Pide derivar Θ_± de una identidad global o cociente de borde; exigencias: hermitizar a
D_Δ, usar minimalidad, usar Λ∗1 = log en la línea de signo, no transportarse a falsificadores.

**Cotejo.** Ninguno de T1–T4.

## R170_834 — Puerto Tate canónico: rango Hardy, ambigüedad exterior y cociente exacto

**Objeto.** Dos extensiones naturales: por caracteres globales Θ^char (2.3)–(2.4) y forma de borde
Hardy Θ^H(c)(F) = p_±(F) conj ℓ_±(z_c^±), con ℓ_+(z) = ∫_T^∞ z e^{-t/2} (2.5)–(2.7). Líneas
κ_m^- = b_m e^{-(a_m+½)T}/(a_m+½), κ_m^+ = b_m e^{-(a_m−½)T}/(a_m−½), cociente κ^+/κ^- =
e^T (a_m+½)/(a_m−½) dependiente de m (2.9). Perturbación E_λ = E_0 + λH, H soportada fuera de I_T,
compatible con reflexión (3.1)–(3.4). Cociente intrínseco Z^*/Ran 𝒜^*, realización Z_0 = ker 𝒜 (4.2)–
(4.4). Residuos ℛ_H = M_H − D_Δ (5.4), ℛ_char − ℛ_H de rango ≤ 4 (5.7), ℛ_0 = P_0(Herm[Γ_+C_+ +
Γ_−C_−] − D_Δ)P_0 (5.8).

**Afirmaciones (ledger).** Puerto Hardy de la fuente: PROVED/CANONICAL (citado de R161). Θ^char ≠ Θ^H
para L ≥ 2: sostenido. Unicidad de Θ_± sobre Ran ι_±: FALSE (sostenido). Cancelación bilateral de la
ambigüedad: FALSE (sostenido, (3.4) la duplica). Cociente por Ran 𝒜^*: PROVED. M_H y ℛ_H: COMPUTED
EXACTLY (como definición explícita; ningún valor numérico). ℛ_H = 0 o con signo: OPEN; ℛ_0 = 0: OPEN.
Equivalencia con la dispersión inversa de R161_018: NOT PROVED / formalmente falsa.

**Detención.** Sin un mapa fuente–puerto cuadrático, elegir entre (2.3) y (2.7) impone la ley de
transmisión que se quiere probar. El cociente Z_0 pierde justamente las direcciones Tate.

**Corrección/auditoría.** R170_836 (valida).

**Cotejo.** T1–T4: no.

## R170_835 — Mapa cuadrático fuente–innovación–puerto y residuo exacto

**Objeto.** En un sector de paridad Z_ε: innovaciones 𝒥_+ = (I−D)^{1/2}R_L, 𝒥_- = (I−D)^{1/2}R_LJ,
½(𝒥_+^*𝒥_+ + 𝒥_-^*𝒥_-) = D_Δ (0.3). Portador PC finito con innovaciones centradas
𝓘_{M,N}F = (Δ^R_{N,T}ℓ_F, Δ^L_{N,T}ℓ_F) y escalares Tate a_∓(ℓ_F) (2.6)–(2.9). Defecto por sustitución
de pesos: δ_a(k) = Σ_{d|k} a(d) − log k; bloque (2.11) −J Σ_{k≤N} δ_a(k)k^{-1/2}τ_{log k} − (…)𝓕, nulo
para a = Λ. Mapa a columnas 𝒦_± = ι_±(I−D)^{1/2}; Gram de pendiente con W_+ = 2(X−T):
G^col_mn = 2 b_m b_n e^{-(a_m+a_n)T}/(a_m+a_n)² (cuadrado de Cauchy) (3.7). Residuo ℛ_col = 𝒮_col − D_Δ =
Σ_σ 𝒥_σ^*[(I−D)^{1/2}G^col(I−D)^{1/2} − ½I]𝒥_σ (3.9). Forma de pendiente canónica
𝒮_can = 𝒢_+^*W_+𝒢_+ + 𝒢_-^*W_-𝒢_- ⪰ 0 (4.3). Descomposición 𝒮_can − D_Δ = ℛ_range + ℛ_col (5.1).
Especificación de una forma mixta 𝔅^ε_{M,N,L} (6.3) con dos lecturas de residuo común.

**Afirmaciones.**
- (0.3), (3.4), (3.7), (3.9), (3.12), (5.1): PROVED/EXPLICIT; sostenidas (álgebra y una integral
  elemental).
- Proposición 4.1 (PROVED): no existe factorización universal 𝐆_+^prod(F) = 𝒦 R_L F con L finito
  sobre un portador que preserve el jet crítico. La prueba evalúa el germen producto en un cero de una
  función externa y usa independencia de exponenciales; es decir, usa una reducción a ceros (se
  registra neutralmente, sin desarrollar). Lo que el texto sostiene: el argumento de independencia de
  exponenciales es correcto bajo la premisa de que tal evaluación es un funcional del portador.
- Factorización restringida al radical (4.9): existe a posteriori vía (𝒥_+|_{Z_ε})^{-1}; no uniforme.
- (5.3) ⟨F,(𝒮_can + D_Δ)F⟩ = 0 forzaría F = 0: sostenido trivialmente (suma de dos formas ⪰ 0, una
  ≻ 0). Muestra que la «ley inversa» ya es el cierre.
- §7 falsificadores: el Gram de columnas sobrevive a pesos positivos arbitrarios (d_m^w), a Λ1_{n≥5},
  a Tipo I, a autovectores positivos ((7.2) Q_{N,L} < 0); sólo (2.11) distingue Λ.

**Detención.** La identidad Λ∗1 = log entra sólo en el portador PC (2.11), no en el Gram de columnas;
por eso cualquier signo del Gram pasa los falsificadores de peso. Falta la forma mixta (6.3): NOT BUILT.
Minimalidad ausente; uniformidad ausente.

**Corrección/auditoría.** R170_836 (valida; (6.3) es especificación, no construcción); R170_837
prueba que la condición de residuo común es el cierre mismo.

**Cotejo.** T3: sí — registra la entrada exacta de Σ_{d|k}Λ(d) = log k como anulación de δ_Λ(k), y
que esa anulación no da signo por sí sola. T4: parcialmente — trabaja con los apareamientos mixtos de
PC (E_N, H_{M,N}) pero los dirige hacia puertos Hardy/columnas Gamma, no hacia Σ_{k>N} h(k)|ℓ_k(F)|².
T2: el Gram de Cauchy G^col es un Gram explícito, pero de exponenciales Gamma, no de divisores. T1: no.

## R170_836 — Auditoría del puerto canónico y del mapa cuadrático

**Objeto.** Auditoría de R170_834–835.

**Afirmaciones.** Valida: no unicidad del puerto Tate; reducción a Z_0 correcta pero incompleta; Gram
de columnas exacto; obstrucción de rango finito (excluye sólo factorización universal finita, no un
mapa infinito, dependiente de la fuente ni una identidad sólo sobre el radical); la factorización vía
inversa es legítima pero depende del objeto a excluir. Entrada real de la aritmética: sólo δ_a(k).
Cinco requisitos para la siguiente pieza (escrita desde PC, preservando términos, cancelación de
δ_Λ algebraica, mismo residuo en ambas lecturas, variación unilateral en T).

**Cotejo.** T3: confirma el papel registrado en R170_835. Resto no.

## R170_837 — Forma PC mixta: construcción maximal, incompatibilidad exacta y dato de dos ventanas

**Objeto.** Z_N = S_N^ren, E_N = Z_N𝓕 − JZ_N, C_N = Z_N𝓕 + JZ_N, K_N = −[X,Z_N],
𝒥_N = K_N𝓕 − JK_N = Z_N𝓜𝓕 − {X,C_N}; hipérbola renormalizada H̃_{M,N} = L_M Z_N − K_N.
Forma mixta 𝔐_N^ε[T_L](F,G) = Herm⟨E_NF, 𝒥_N T_L G⟩ (0.4), T_L = S_L. Green polarizado
Herm⟨e_N(F), X c_N(G)⟩ = Herm(⟨a_N,Xa_N⟩ − ⟨d_N,Xd_N⟩) (3.1); descomposición por soportes
𝔖^phys − 𝔖^wrong + TΦ_N + 𝔊_{0,N} (3.6); lectura Hardy (3.8)–(3.9); lectura Euler–hipérbola (4.3).
Teorema 5.1. Monitor 𝔄_a (6.9). Dato de dos ventanas
ℭ^ε_{M,N;T,δ}(F,F_δ) = ⟨1_{C_δ} 𝔓^ren 𝓕 F̃, F_δ|_{C_δ}⟩ (8.3), con identidad de collar
λ_δ⟨F_δ, E_TF⟩ = ⟨ξ_F^δ, F_δ|_{C_δ}⟩ (7.5).

**Afirmaciones (ledger).**
- Polarización E_N–C_N finita, orientación, Green sesquilineal, cuatro bloques: PROVED (sostenido;
  declarada idéntica a R161_056–057, no nueva).
- Término líder Hardy para T_L = S_L: cruzado, FALSE como 𝒮_can (sostenido).
- Expansión (4.3): PROVED; aparición de +D_Δ en ella: FALSE (sostenido: incompatibilidad de ranuras).
- Teorema 5.1 (PROVED): si existen 𝔅, ℜ con 𝔅 = D_Δ + ℜ y 𝔅 = −𝒮_can + ℜ, entonces Z_ε = 0. Sostenido
  (resta y positividad). Consecuencia: el «residuo común» es el cierre completo, no contabilidad.
- (6.7) PROVED: tras la recombinación K_N = L_M^a S_N − H^a_{M,N}, 𝔐 es independiente del peso a
  (ciega al peso). Sostenido.
- Monitor 𝔄_Λ = 0 exacto; no aporta signo.
- §7: derivada interior con término lineal nulo (R162_101); minimalidad derecha no cabe en forma sobre
  Z_T × Z_T (7.6): FALSE/WRONGLY TYPED.
- (8.3) declarado PROVED/EXACT y «primer portador que usa (6.5) y (7.5) a la vez». Lo que el texto
  sostiene: (8.3) es sólo una reescritura de PC-ren en el núcleo regular; la auditoría R170_838 retira
  la pretensión de contener la minimalidad firmada y de novedad.

**Detención.** Tres incompatibilidades (residuo común, ranura de test, minimalidad). Signo de (8.3) y
transporte a R_LF: OPEN.

**Corrección/auditoría.** R170_838 (nueve correcciones; ver (e)).

**Cotejo.** T4: sí, de cerca — es el intento maximal de convertir apareamientos mixtos de PC (E_N con
el jet de la suma) en una forma con término líder positivo; fracasa porque el término líder es una
correlación cruzada 𝔖^phys[I,S_L] y el resto (𝔖^wrong, Φ_N, 𝔊_0) no tiene signo; nunca aparece una
suma Σ_{k>N} h(k)|ℓ_k(F)|². T3: sí — registra que Λ∗1 = log sólo anula el bloque k ≤ N antes de
recombinar y que tras recombinar la forma olvida el peso (6.7). T1, T2: no.

## R170_838 — Auditoría del dato PC–collar de dos ventanas

**Objeto.** Auditoría de R170_837 §§7–8. Expansión exacta
ℭ = λ_δ⟨F_δ,E_TF⟩ + ℛ^Tate + ℛ^Z, ℛ^Tate = ⟨r_F, F_δ|_{C_δ}⟩, ℛ^Z = ⟨1_{C_δ}(Z_N − I)A_ME_TF, F_δ|_{C_δ}⟩
(0.3)–(0.4); expansión de ℛ^Z en traslaciones y continuo polar (4.6); residuo ℛ^tot = ℛ^{>L} + ℛ^Tate +
ℛ^Z (6.3)–(6.4), con ξ_F^δ = −ℓ_L(R_LF) + ξ_F^{>L} (R162_406 Prop. 4.1).

**Afirmaciones (ledger corregido).**
- Identidad de collar entre T y T+δ: PROVED; signo para todo F del radical: FALSE; signo sólo para el
  límite G normalizado con fase fijada: PROVED.
- 𝒫^pol_{M,N} = 0 en el núcleo común (PC para C^pol menos PC para C^pol): PROVED; no es bloque nuevo.
- 1_{C_δ}A_ME_TF = r_F + ξ_F^δ en 𝒬'_log si M ≥ e^{2T'}: PROVED; pasar Z_N por la restricción: FALSE.
- (8.3) = apareamiento firmado de minimalidad: FALSE. Estabilización en M: FALSE. Dependencia en N:
  explícita.
- δ_Λ(k) = 0 requiere M ≥ N (R170_837 sólo imponía M ≥ e^{2T'}); escala limpia N ≥ e^{2T'}, M ≥ N.
- δ_Λ = 0 y λ_δ < 0 en el mismo escalar: FALSE.
- Novedad de (8.3): NO / reempaquetado de R162_405–406; transporte del signo a R_LF con estos datos:
  NO-GO (por R162_406–408).
- Extensión de (8.3) al dominio real de primer contacto: NOT PROVED (requiere Z_N^* que preserve
  𝒬_log).

**Detención.** El residuo total (6.4) no tiene signo ni anulación; aun sin residuos, (6.2) es una
única desigualdad escalar contra un perfil desconocido y no fuerza R_LF = 0.

**Cotejo.** T3: sí (la anulación δ_Λ vive en los coeficientes de la hipérbola cruda, la minimalidad en
otro apareamiento; no se encuentran en un escalar). T1, T2, T4: no.

## R170_839 — Mapa del rompecabezas v3

**Objeto.** Inventario actualizado: A (13 piezas probadas), B (12 conexiones refutadas o agotadas), C
(8 piezas faltantes: ley bilateral del collar, dominación de la cola, conversión peine–Gamma, control
del perfil de la ventana mayor, uso no perturbativo de minimalidad, separación de falsificadores,
uniformidad en T, anulación final), D (pieza admisible: ley bilateral del collar con ℓ_L(R_LF) y
ξ_F^{>L} en lados o escalas distintas, usando el peine exacto de ℤ).

**Afirmaciones.** Inventario; las piezas A.1–A.13 citan sus memos. B.4 repite la obstrucción de
R170_835 que se apoya en evaluación en ceros (usa una reducción externa; registrado neutralmente).

**Cotejo.** C.3 («conversión peine–Gamma: identidad que convierta la geometría exacta de los divisores
enteros en coeficientes de los momentos Gamma») está cerca de T2/T3 como pregunta, sin construcción.

## R170_840 — Ley bilateral del collar: forma normal, no-go y dato virial mínimo

**Objeto.** Escalas explícitas δ_gap(T) = ½ min{log(n_1/e^{2T}), log 2}, δ_j = 2^{-j}δ_gap,
N_j = M_j = ⌈e^{2T_j}⌉ (1.3)–(1.4); L_T mínimo con R_L inyectivo (1.5). Descomposición de collar
ξ_{F,+}^δ = −γ_F − Π^δ_{Λ,T}F − r_F, γ_F = Σ_{m≥1} e^{-a_m t} μ_F(a_m),
Π^δ_{Λ,T}F(t) = Σ_{2≤d<e^{2T}} Λ(d)d^{-1/2} F(t − log d) + θ_T ε Λ(n_0) n_0^{-1/2} F(2T − t) (2.1)–(2.3);
cola sin Tate ξ̂^{>L} (2.5); forma normal directa λ_δ a_δ = −⟨ℓ_L^ε(R_LF), f⟩ + ⟨ξ̂^{>L}, f⟩ − ⟨r_F, f⟩
(0.3)/(2.8); forma normal PC (0.1)/(4.5) con cancelación del Tate local y residuo no local ℛ^Z (4.7).
Funcional virial 𝒱_{Λ,T}(F) = (2π)^{-1}∫ τ m'(τ)|F̂|² − Σ_{n<e^{2T}} 2Λ(n)n^{-1/2} log n · c_F'(log n) +
2Re⟨F, t r_F'⟩ (8.1), con λ_A(T+δ) = −(δ/T)𝒱(G) + o(δ) (8.2) bajo (REG). Dato abierto VIR–EP (8.3).

**Afirmaciones (ledger).**
- Elecciones de escalas: PROVED/EXPLICIT. L_T finito: PROVED / no uniforme.
- Descomposición (2.6) y forma normal (0.3): PROVED (reorganización exacta de R162_406).
- Igualdad de las dos orientaciones locales por paridad (3.2)–(3.3): PROVED; segunda desigualdad
  independiente por antisimetría: FALSE. Sostenido.
- Forma normal PC (4.5), cancelación del Tate local: PROVED (contable, sin signo). Estabilización de
  ℛ^Z: FALSE.
- δ_Λ = 0 localizado antes de recombinar: PROVED; signo producido por esa cancelación: FALSE; escalar
  aritmético tras recombinar: FALSE.
- Cola universalmente o-pequeña frente a la parte observada (6.1): FALSE (por R162_408 Prop. 5.1;
  independencia de jets y momentos). Feshbach orienta la suma, no las componentes (6.4)–(6.6).
- Teorema 6.1 (NO-GO, PROVED): toda identidad escalar de dos ventanas cuyo único argumento de la
  ventana mayor es F_δ, obtenida por composiciones lineales de PC finita, Chebyshev comprimido,
  reflexión, restricción a collares, apareamiento con F_δ, ecuación débil e identidad de minimalidad,
  se reduce a la forma normal + cambios de base invertibles + monitor nulo 𝒟_Λ^{≤N} = 0; ninguna da
  dominación estricta de cola/Tate/ℛ^Z por R_LF. Lo que el texto sostiene: la prueba es un argumento
  de clausura por casos sobre las operaciones listadas (el término «toda identidad» queda sostenido
  para esa lista; el paso «§§6.1–6.4 prueban que no sigue signo» se apoya en R162_406–408 citados). Es
  un NO-GO de clase declarada, puntual en T.
- Falsificadores: pasa F1 (autovectores positivos, (7.2)), pesos positivos, Davenport–Heilbronn.
- Proposición 8.1 (PROVED): VIR–EP ⟹ R_LG = 0. Sostenida (0 ≤ 𝒱(G) ≤ 0 y cota inferior por la
  reserva). VIR–LB (𝒱|_N ⪯ 0) y VIR–DET (𝒱(G) ≥ c_T D_Δ(G)): OPEN. (REG) y traza umbral: OPEN.

**Detención.** No-go para el portador actual; el dato mínimo VIR–EP tiene exactamente la fuerza del
cierre y debe probarse con una operación de coeficientes sobre la hipérbola finita antes de recombinar
en K_N.

**Cotejo.** T3: sí — registra con precisión que la identidad de divisores sólo anula un bloque y que,
tras recombinar, la forma «olvida la razón aritmética»; VIR–LB exige su uso antes de la recombinación,
abierto. T4: parcialmente — la «parte de cola k > N» aparece en la condición 3 de VIR–EP («retener la
contribución de borde k > N»), sin forma Σ h(k)|ℓ_k|². T1: el término (2π)^{-1}∫τ m'(τ)|F̂|² es el
derivado de dilatación del multiplicador (peso de dilatación), pero sin cuadrado aritmético. T2: no.

---

## (a) Piezas PROVED reutilizables

1. T_{a,w} = ∫w τ_{a/ρ}: L² → H^k; P_T T_{a,w} P_T HS con ‖κ‖₂² = |a|^{-1}∫ρ²|w|² — R170_823 §3 (11)–(17).
2. ‖T_{a,w} − τ_a‖ ≥ 1 — R170_823 §4 (19).
3. Interfaz multiescala exacta con energía interior ⪰ 0 — R170_823 §5 (24) (auditada en R170_824).
4. Collar acoplado C_{a,w} = q_{a,w}(D)J; región estacionaria ρ_0 r_a ≤ |ξ| ≤ r_a; |q| ≤ A_w/|ξ| fuera de
   la banda; L² → H¹; HS con cota explícita (18); para la orientación m + a, raíces sólo si
   log k ≤ −m(0) (k ≤ 215) — R170_825 §§2–5.
5. Autoadjunción del collar promediado con peso real; cota de valores singulares
   s_{r+1} ≤ ‖·‖_HS/√(r+1) — R170_827 §4 (18), (21a).
6. Gram fiel B ≻ 0 y criterio espectral finito λ_max(B^{-1/2}KB^{-1/2}) ≤ 0 — R170_827 §§1, 5.
7. Exclusión de todo levantamiento interior de D_Δ (ΛY = 0 para tests en la ventana) — R170_829 §2 (13).
8. Identidades R_GE = P − D_Δ = Q − E − B − ½Q^{(1)} — R170_829 (18), (25), (26).
9. Respuesta exterior de A_1 sobre colas exponenciales cortadas, salto logarítmico, reflejo —
   R170_831 Lema 2.1, §§3–4 (especialización de R162_404 §4).
10. No determinación del puerto Tate exterior por la ecuación débil — R170_831 Lema 5.1.
11. Θ^char ≠ Θ^H (cociente κ^+/κ^- dependiente de m); no cancelación bilateral; cociente intrínseco
    Z^*/Ran 𝒜^* — R170_834 §§2–4.
12. Gram de columnas de Cauchy G^col_mn = 2b_mb_n e^{-(a_m+a_n)T}/(a_m+a_n)² y residuos ℛ_col, (5.1) —
    R170_835 §3, §5.
13. Defecto por sustitución de pesos δ_a(k) y bloque (2.11), nulo exactamente para Λ — R170_835 §2.2;
    R170_837 §6 (6.2)–(6.5).
14. Teorema 5.1 (residuo común ⟹ Z_ε = 0) — R170_837 §5.
15. Ceguera al peso tras recombinar K_N = L_M^aS_N − H^a_{M,N} (6.7) — R170_837 §6.
16. 𝒫^pol_{M,N} = 0 en el núcleo común — R170_838 §2 (2.4).
17. Expansión ℭ = λ_δ⟨F_δ,E_TF⟩ + ℛ^Tate + ℛ^Z — R170_838 §4.
18. Igualdad de las dos orientaciones locales en un sector de paridad — R170_840 §3.
19. Forma normal PC con cancelación del Tate local — R170_840 §4 (4.5).
20. Teorema 6.1 (no-go de clase) y Proposición 8.1 (VIR–EP ⟹ R_LG = 0) — R170_840 §§6.5, 8.

## (b) Cierres (clase y falsificador)

- Restar el promedio multiescala contra la escala uno: norma ≥ 1, no es resto pequeño (R170_823 §4).
- Compacidad / Hilbert–Schmidt como fuente de signo: un compacto autoadjunto tiene ambos signos; en el
  radical finito toda matriz es compacta (R170_826, R170_829 §6).
- Levantamiento interior de D_Δ (cualquier síntesis con imagen en la ventana): imposible por la
  ecuación débil (R170_829 (13), R170_830).
- Elección del puerto Tate exterior: no forzada; dos elecciones naturales difieren; bilateralidad
  duplica la ambigüedad (R170_831 Lema 5.1, R170_834 §§2–3).
- Factorización universal del puerto Hardy por R_L finito: falsa (R170_835 Prop. 4.1; argumento con
  evaluación en ceros, registrado neutralmente).
- Signo deducido del Gram de columnas o de D_Δ: falsificado por pesos positivos arbitrarios, Λ1_{n≥5},
  Tipo I y autovectores positivos (Q_{N,L} < 0) (R170_835 §7).
- Forma mixta con +D_Δ, −𝒮_can y residuo común como consecuencia formal de PC: es el cierre mismo
  (R170_837 Teorema 5.1); falsificador: modelos con primer contacto no trivial.
- Polarización E_N–C_N tras recombinar: ciega al peso (R170_837 (6.7)).
- Minimalidad derecha dentro de una forma sobre Z_T × Z_T: mal tipada (R170_837 (7.6)).
- Dato de dos ventanas (8.3) como portador firmado: falso; reempaquetado de R162_405–406 (R170_838).
- Ley bilateral del collar con PC/Chebyshev/collar/Feshbach: NO-GO de clase (R170_840 Teorema 6.1);
  falsificadores F1 (autovector positivo con descenso), pesos positivos, Davenport–Heilbronn.

## (c) Explícitamente abierto, con su obstáculo exacto

- Signo de las líneas de (24) de R170_823 sobre F ∈ ker H_T sin estimar cada una en valor absoluto.
- Las dos desigualdades matriciales P − (1−q_0)B ⪰ 0 y P + E ⪯ 0 (R170_827 (28a)); equivalentemente
  R_GE ⪰ −[D_Δ − (1−q_0)B] (R170_829 (32)).
- Fórmula de Green exterior y puerto canónico Θ_± derivado de una identidad global (R170_831, R170_833);
  Herm(ΛY) = D_Δ sobre todo Z; ℛ_0 = 0 en Z_0 (R170_834 (5.8)), que aun probado no controla las
  direcciones Tate.
- Construcción de la factorización del puerto sobre el radical desde PC sin invertir R_L|_Z
  (R170_835 §4.2).
- Forma mixta finita 𝔅^ε_{M,N,L}: NOT BUILT; por R170_837 equivale al cierre.
- Signo de (8.3) y transporte a R_LF; control del residuo total ℛ^{>L} + ℛ^Tate + ℛ^Z (R170_838 (6.4)).
- Piezas C.1–C.8 de R170_839 (ley bilateral, dominación de la cola, conversión peine–Gamma, perfil de
  F_δ, minimalidad no perturbativa, separación de falsificadores, uniformidad, anulación final).
- VIR–EP: (REG) y traza umbral; VIR–LB 𝒱_{Λ,T}|_{N_T^ε} ⪯ 0 probada sobre la hipérbola antes de la
  recombinación usando 𝒟_Λ^{≤N} = 0; VIR–DET 𝒱(G) ≥ c_T⟨R_LG,(I−D)R_LG⟩ controlando cola, Tate y ℛ^Z
  sin inversa a posteriori; cuantificadores L_*, c_* computables y uniformes en compactos
  (R170_840 §8). Obstáculo de uniformidad: inf_T δ_gap(T) = 0 y no hay cota de L_T.

## (d) Lo que en este tramo ya recorre T1–T4, con la razón registrada del fracaso

- **T1 (cuadrados continuos con pesos de dilatación).** R170_823–826 promedian en la dilatación con
  peso w (incluido perfil w_h) y obtienen sólo suavizado y compacidad; razón: la operación es lineal en
  el operador y no produce ningún cuadrado; HS no da signo; constantes no uniformes en k, T, h. El
  término virial (2π)^{-1}∫τ m'(τ)|F̂|² de R170_840 (8.1) es un cuadrado continuo con peso de
  dilatación, pero el signo global de 𝒱 en el radical (VIR–LB) queda abierto. No hay intento de poner
  la aritmética en el índice de un cuadrado continuo.
- **T2 (Gram de divisores [log mcd] = E diag(Λ) Eᵀ).** No aparece. El único Gram explícito es el de
  Cauchy de exponenciales Gamma (R170_835 (3.7)), ciego al peso; razón de su fracaso: sobrevive a todo
  sistema de pesos positivos. R170_839 C.3 formula como pregunta abierta una «conversión peine–Gamma».
- **T3 (Σ_{d|n}Λ(d) = log n convertida en cota cuadrática).** Recorrido de modo directo en R170_835 §2.2,
  R170_837 §6, R170_838 §5, R170_840 §5: la identidad anula exactamente el bloque de coeficientes
  k ≤ N de la hipérbola (𝒟_Λ^{≤N} = 0), pero (i) un monitor nulo no aporta signo; (ii) al recombinar
  K_N = L_M^aS_N − H^a la forma vuelve a ser independiente del peso (R170_837 (6.7)); (iii) la anulación
  vive en un escalar distinto del que lleva el signo de minimalidad (R170_838). Lo que queda pedido
  (VIR–LB) es usarla antes de la recombinación como desigualdad: abierto. Ninguna memo la convierte en
  una cota cuadrática.
- **T4 (apareamientos mixtos de PC → Σ_{k>N} h(k)|ℓ_k(F)|², h ≥ 0).** Más cercano: R170_837 (forma
  mixta E_N–𝒥_N, Green polarizado (3.6)) y R170_823/825/827 (la cola H_{M,N} = Σ_{k>N} h(k)k^{-1/2}τ
  promediada y compacta). Razón del fracaso: el término líder es una correlación cruzada
  𝔖^phys[I,S_L], no una norma; los restos 𝔖^wrong, TΦ_N, 𝔊_0 no tienen signo; la cola aparece como
  operador, nunca diagonalizada en cuadrados |ℓ_k(F)|²; además el residuo común exigido equivale al
  cierre (Teorema 5.1). La conversión exacta pedida por T4 no se intenta en el tramo.

## (e) Inconsistencias o errores entre memos

1. R170_823 primera versión: confundía S_ρA_ρU_ρ con A_ρS_ρU_ρ, orientaba mal el núcleo (u = a/ρ en vez
   de −a/ρ) y afirmaba núcleo acotado para P_TH_ρU_ρP_T; corregido según R170_824.
2. R170_823 deja abierta la compacidad de ⟨H_ρU_ρ⟩_w; R170_825 la prueba (no es contradicción, es
   cierre posterior).
3. R170_827 primera versión: doble conteo (residuo de cuatro líneas + energía interior); corregido a
   Q = K = P + E (R170_828).
4. R170_830 dice que Y_+ está en el dominio logarítmico; R170_831 añade que eso no basta porque el
   término Tate no está tipado para tests exteriores.
5. R170_832 §§5–6 pedía «fijar canónicamente el puerto Tate exterior»; su §7 (añadido) y R170_834
   corrigen: el puerto de la fuente ya es canónico, lo que falta es un mapa fuente–puerto.
6. Estado del no-go lineal de R161_018: R170_834 §1 dice que R161_075 corrige su alcance; R170_835 §1
   añade que R162_2302 lo restablece para el portador débil. Las dos memos no se contradicen pero
   R170_834 omite la restitución.
7. R170_837 introduce 𝒫^pol_{M,N} como bloque polar adicional; R170_838 prueba 𝒫^pol = 0 en el núcleo.
8. R170_837 §7.2 afirma que el apareamiento tiene el signo de λ_δ sin restricción; R170_838 lo limita al
   vector límite normalizado con fase fijada.
9. R170_837 §8 impone sólo M ≥ e^{2T'} pero usa δ_Λ(k) = 0, que requiere M ≥ N (R170_838 §5).
10. R170_837 omite R162_406 en su auditoría de no duplicación; su «nueva obligación» ya estaba decidida
    negativamente allí (R170_838 §7.3). Además colisión de notación Z_N (operador) / Z_T (radical).
11. R170_837 etiqueta (8.3) «PROVED/EXACT» como portador que contiene minimalidad; R170_838 lo rebaja a
    reescritura válida sólo en el núcleo regular, sin extensión probada al dominio de primer contacto.
12. R170_827 advierte no descomponer por paridad porque U_ρ no preserva sectores; R170_835 y siguientes
    trabajan en Z_ε. No es inconsistencia (ya no usan U_ρ), pero el cambio de marco no se señala.
13. R170_840 usa la notación ξ̂^{>L} (sin Tate) distinta de ξ^{>L} de R162_406/R170_838 (con −r_F); la
    memo lo declara en (2.7), pero ℛ^{>L} de R170_838 (6.2) y la cola de R170_840 (0.1) no son el mismo
    objeto.

## (f) Archivos leídos (lectura completa con Read)

R170_823_MULTISCALE_AVERAGED_PC.md (424 líneas) — completo.
R170_824_MULTISCALE_AUDIT.md (95) — completo.
R170_825_COUPLED_COLLAR_PHASE.md (276) — completo.
R170_826_COUPLED_COLLAR_AUDIT.md (95) — completo.
R170_827_RADICAL_MATRIX_CANCELLATION.md (430) — completo.
R170_828_RADICAL_MATRIX_AUDIT.md (77) — completo.
R170_829_GAMMA_EULER_MATRIX_BRIDGE.md (342) — completo.
R170_830_GAMMA_EULER_BRIDGE_AUDIT.md (95) — completo.
R170_831_EXTERIOR_GREEN_FORMULA.md (262) — completo.
R170_832_PUZZLE_MAP_V2.md (171) — completo.
R170_833_EXTERIOR_GREEN_AUDIT.md (88) — completo.
R170_834_CANONICAL_TATE_PORT.md (418) — completo.
R170_835_QUADRATIC_SOURCE_PORT.md (773) — completo.
R170_836_SOURCE_PORT_AUDIT.md (116) — completo.
R170_837_MIXED_PC_FORM.md (932) — completo, en dos lecturas.
R170_838_TWO_WINDOW_AUDIT.md (669) — completo.
R170_839_PUZZLE_MAP_V3.md (133) — completo.
R170_840_BILATERAL_COLLAR_LAW.md (838) — completo, en dos lecturas.
