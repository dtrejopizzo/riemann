# Ronda 7, memo A: el cuadrado del déficit, la representación de estado fundamental de los contactos y las condiciones de optimalidad del reparto

Notación: I = (−T, T), u_p = log p, v_p = 2 log p/√p, S_u F(t) = F(t − u) truncado a I, Π_p(F) = Σ_{n=p^k} v_n c_F(log n)
(para p = 2 incluye n = 4), ε_F(u) = ½‖F − F_u‖². Reparto DIR (`ROUND_006` §§2, 7–10):
q_p(F) = ∫W_pF² + ¼∬θ_p(t,s)K(|t−s|)(F(t)−F(s))² − Π_p(F), θ_p ≥ 0, Σθ_p = 1, ΣW_p = W.

## 0. Filtro de cuatro puntos

**(1) Antecedentes leídos en primaria.**
- `phase-212-missing-object/REVIEW_006.md` A1–A4 y D (condición de reapertura); `ROUND_006_WINDOW_SPLIT_NUMERIC.md`
  §§5, 7–10 (dualidad discreta, par obstructor, transferencia mínima X = λℓ⊗ℓ).
- `phase-211-sign-sandbox/ROUND_005_D.md` §2 Teor. 2.1 (representación de estado fundamental con el peine como medida
  atómica de salto, respecto del estado fundamental h_T **de la forma completa**) y Teor. 6.1 (NO-GO de la clase 𝒦_gap:
  cotas de hueco con pérdida intrínseca). LEDGER 211 C17.
- `phase-195-modern-tools/INV_N_001_BAKRY_EMERY_GAMMA2_GAP_CEILING_NO_GO.md` §1: −v c_F(u) = ½v∫(F − F_u)² − v‖F‖²,
  es decir el caso φ ≡ 1 de la identidad de §1 de esta memo.
- P47 cor:Tarch (citado en `ANNEX_COTEJO_NULLDIR.md` §2.1; PROVED con intervalos): 0.58 ≤ T*_{∞,P} ≤ 0.60, el fondo de
  Arch sobre P_T es < 0 para todo T ≥ 0.60. P47 thm:index: n₋(Arch|P_T) = 0, 1, 2 en (0,T*_ev), (T*_ev,T*_odd),
  (T*_odd, 0.90], log 2 ≤ T*_odd ≤ 0.81. `R155_029` l.27: «por encima de T*_{∞,P} los primos son necesarios».
- `phase-159-row-d-two-front-construction/G2_B8_R5.md` Def. 1 y Teorema D paso 4 (vía `REVIEW_006` A1; holgura
  complementaria todo-o-nada).
- Fases 202 y 205 (placa exterior, Toeplitz−Hankel de la cola): cotejadas por grep de «estado fundamental», «ground
  state», «gauge», «Schur»; no contienen una cota por primo del contacto por un potencial. Sin valor de prueba de
  ausencia.

**(2) Lo nuevo.** No hay objeto con signo. Lo que la memo afirma y no está en el corpus:
(a) una prueba de imposibilidad para la clase 𝒢 de certificados que acotan cada contacto Π_p por un potencial
V_p ≥ 0 (gauge, test de Schur, estado fundamental por primo con φ_p posicional, cadenas de cualquier longitud,
combinado con cualquier θ_p(t,s) y W_p(t)); la clase muere en T*_{∞,P} ≤ 0.60, antes de log 2;
(b) el dual continuo del reparto DIR y de la transferencia mínima, y la ecuación que cumple ℓ;
(c) la lectura de ℓ como dirección «periódica de periodo log 2 a lo largo de las cadenas» (ARGUED).

**(3) Por qué evita la dificultad del antecedente.** No la evita: la hipótesis del encargo cae en (a). La diferencia
con 211 ROUND_005_D (estado fundamental global h_T, comb incluido, y clase 𝒦_gap sobre el segundo autovalor) es real
—aquí φ_p es por primo y la cota es sobre el fondo de cada q_p—, pero el resultado (a) muestra que esa diferencia no
crea signo: el mecanismo se pierde por un hecho arquimediano ya probado, no por la geometría de las cadenas.

**(4) Enlace con la positividad global.** Ninguno positivo. (a) es un cierre de clase; (b) da la ecuación que cualquier
fórmula cerrada para ℓ, θ_p, W_p debería satisfacer, es decir el control que una futura candidata ha de pasar.
Por la regla del filtro se detuvo toda construcción de una fórmula para ℓ dentro de 𝒢; el resto del esfuerzo se dedicó
a (b) y (c).

## 1. La identidad de estado fundamental por primo (PROVED, elemental)

**Lema 1.1.** Sea u > 0, v > 0, φ > 0 medible en I, F ∈ L²(I) real. Sea J_u = {t ∈ I : t + u ∈ I}. Entonces

v∫_{J_u} F(t)F(t+u)dt = ∫_I V F² − (v/2)∫_{J_u} φ(t)φ(t+u)(F(t)/φ(t) − F(t+u)/φ(t+u))² dt,

V(t) = (v/2)[𝟙_{J_u}(t)φ(t+u) + 𝟙_{J_u}(t−u)φ(t−u)]/φ(t).

*Prueba.* Desarrollar el cuadrado: (v/2)∫_{J_u}[φ(t+u)F(t)²/φ(t) + φ(t)F(t+u)²/φ(t+u)] − v∫_{J_u}F(t)F(t+u); en el
segundo sumando cambiar t + u → t. □

Para n = p^k se suma sobre u = k u_p con su propio φ_{p,k} (o un φ común). Con φ ≡ 1 se recupera INV_N_001 §1. Para
T < u_p, J_u y J_u + u son disjuntos (las parejas forman un emparejamiento) y α(t) = φ(t+u)/φ(t) es la gauge libre
del encargo; para T > u_p hay cadenas t − u, t, t + u y V(t) suma dos vecinos. **La identidad vale igual en ambos
regímenes; la distinción emparejamiento/cadena no cambia el tipo de cota** (en ambos casos es la desigualdad de Schur
Π_p ≤ ∫V_pF², exacta en F ∝ φ a lo largo de las cadenas).

## 2. NO-GO de la clase 𝒢 (PROVED relativo a P47 cor:Tarch, CITED)

**Clase 𝒢.** Certificados de a_T ⪰ 0 sobre P_T de la forma: para cada primo p, una cota Π_p(F) ≤ ∫V_pF² sobre P_T
con V_p ≥ 0 c.t.p. (en particular la del Lema 1.1 descartando el cuadrado, con φ_p arbitrario, posicional, con cadenas
de cualquier longitud, para cualquier número de primos), y la positividad del resto
R_p := ∫W_pF² + ¼∬θ_pK(F(t)−F(s))² − ∫V_pF² ⪰ 0 sobre P_T, con θ_p ≥ 0, Σθ_p = 1, ΣW_p = W libres (también θ_p de
dos posiciones, también optimizados conjuntamente con los φ_p). Se admite además cualquier fracción κ_p ∈ [0,1) del
cuadrado del Lema 1.1 descartada (el resto con fracción conservada es la clase con v_p sustituido por κ_pv_p más un
término ⪰ 0 añadido a R_p, y el argumento se aplica igual porque sólo usa V_p ≥ 0).

**Teorema 2.1.** Para todo T ≥ 0.60 ningún certificado de 𝒢 existe. Para T ∈ (T*_{∞,P}, 0.60) tampoco.

*Prueba.* Σ_p R_p = Arch − ∫(Σ_pV_p)F² ⪯ Arch sobre P_T porque ΣV_p ≥ 0. Si cada R_p ⪰ 0, Arch ⪰ 0 sobre P_T.
Por cor:Tarch el fondo de Arch sobre P_T es < 0 para T > T*_{∞,P}, y T*_{∞,P} ≤ 0.60. □

**Corolario 2.2.** La representación de estado fundamental de los contactos (la hipótesis del encargo) no explica el
umbral DIR en 0.695–0.70: la clase que usa esa representación como cota muere en T*_{∞,P} ∈ [0.58, 0.60], por
debajo de log 2 = 0.6931, y en la misma forma en régimen de emparejamiento que de cadenas. Pasado T*_{∞,P} los
contactos deben aportar **positivamente** (−Π(e) > 0 en la dirección e de fondo de Arch, pues a_T(e) ≥ 0 >
Arch(e)); toda cota superior de Π_p por un potencial no negativo tira exactamente esa contribución. Esta es la
forma por primo de la frase «por encima de T*_{∞,P} los primos son necesarios» de R155_029; el teorema es su
consecuencia inmediata y no tiene más contenido que ese.

Lo que 𝒢 no cubre: cotas Π_p ⪯ M_{V_p} sobre P_T con V_p de signo variable (posibles por la restricción de Tate, pues
Π_p es indefinida), y certificados que conservan el cuadrado del Lema 1.1 con peso completo (entonces el lema es una
reescritura exacta de q_p y no aporta mecanismo: q_p ⪰ 0 vuelve a ser el problema). OPEN, sin objeto.

**Respuesta a (ii).** La identidad está en el corpus para φ ≡ 1 (INV_N_001 §1) y para φ = h_T global (211 ROUND_005_D
Teor. 2.1). Ninguno de los dos NO-GO registrados (𝒦_gap: segundo autovalor con pérdida; INV_N_001: techo de
curvatura) cubre literalmente la variante por primo con φ_p posicional y reparto DIR conjunto; esa variante queda
cubierta ahora por el Teorema 2.1, por una razón distinta (índice arquimediano, no pérdida de hueco).

## 3. Condiciones de optimalidad del reparto en el continuo

**3.1 Dual del reparto DIR (ARGUED en el continuo; PROVED en cada discretización de Galerkin por dualidad SDP con
Slater, que se cumple: θ_p = ½, W_p = W/2, τ muy negativo es estrictamente factible).** Primal:
τ* = sup{τ : q_p − τ ⪰ 0 sobre P_T, p = 2, 3}. Lagrangiano con Y_p ⪰ 0 (núcleos de traza finita sobre P_T):
τ + Σ_p tr(Y_p(q_p − τ)). Maximizar en τ da Σ tr Y_p = 1; en W_p con ΣW_p = W da diag Y_2 = diag Y_3 =: ρ (si no,
+∞); en θ_2 ∈ [0,1] (θ_3 = 1 − θ_2), con E_Y(t,s) = ¼K(|t−s|)(ρ(t)+ρ(s)−2Y(t,s)), da max(E_{Y_2}, E_{Y_3}). Luego

τ* = inf { ∫Wρ + ¼∬K(|t−s|)[ρ(t)+ρ(s) − 2 min(Y_2(t,s), Y_3(t,s))] − tr(Y_2Π_2) − tr(Y_3Π_3) :
           Y_p ⪰ 0 sobre P_T, diag Y_2 = diag Y_3 = ρ, ∫ρ = ½ }.

Con Y_2 = Y_3 = Y el funcional es tr(Y a_T); el déficit del reparto respecto del techo es exactamente lo que se gana
al separar los dos estados manteniendo densidad común: la energía de núcleo se cobra con min(Y_2,Y_3) en vez de con
Y. Esto reproduce la fórmula verificada en `ROUND_006` §9.1.

**Holgura complementaria.** (K1) Y_p(q_p − τ*) = 0: el rango de Y_p está en el autoespacio de fondo de q_p.
(K2) θ_2(t,s) = 1 donde Y_3(t,s) > Y_2(t,s), = 0 donde Y_3 < Y_2 (todo-o-nada, `G2_B8_R5` Teor. D paso 4, ahora con
dos posiciones). (K3) W_p libre sólo donde ρ = 0; donde ρ > 0 el reparto de W es indeterminado por el dual y lo fija
(K1).

**3.2 Transferencia mínima (`ROUND_006` §10.2).** Primal: min ‖X‖_* con q_2 + X ⪰ 0, q_3 − X ⪰ 0 (θ, W en DIR).
Dual: Y_2, Y_3 ⪰ 0 con las mismas condiciones de densidad y de θ, y Y_3 − Y_2 ∈ ∂‖X‖_*. Si X = λℓ⊗ℓ, ‖ℓ‖ = 1,
λ > 0, entonces

(E_ℓ)  (Y_3 − Y_2)ℓ = ℓ,  ‖Y_3 − Y_2‖_op ≤ 1,  (q_2 + λℓ⊗ℓ)Y_2 = 0,  (q_3 − λℓ⊗ℓ)Y_3 = 0,

y por (K1) ℓ es la dirección de autovalor negativo de q_2 en el óptimo (los datos: solapamiento 0.92–0.95).
**Ecuación de ℓ:** autovector de autovalor 1 (el máximo) de Y_3 − Y_2, con Y_p el par obstructor; equivalentemente
ℓ ∝ (q_3 − λℓ⊗ℓ)-núcleo ∩ dirección negativa de q_2. Es un problema de punto fijo acoplado al par obstructor; no da
fórmula sin resolverlo (ARGUED; sin prueba de existencia en el continuo).

## 4. Lectura de ℓ (ARGUED, sin prueba)

Por el Lema 1.1 con φ ≡ 1, el contacto de 2 es máximo relativo a ‖F‖² en las F con F(t) = F(t + log 2) a lo largo de
las cadenas, y sobre ellas la energía de núcleo a distancia log 2 es nula. Para T < log 2 esa condición sólo
empareja puntos y deja libre la mitad de la ventana; para T > log 2 liga ternas y fuerza periodicidad en la zona
central (−T + log 2, T − log 2): la proyección de cos(2πt/log 2) sobre P_T es el representante natural, y coincide
con el solapamiento observado 0.91–0.93. Esto es coherente con (K2) (2 cede el núcleo en la banda de log 2) pero
**no explica el umbral**: la zona central tiene longitud 2(T − log 2), que es 0.013 en T = 0.70, y el término de n = 4
se activa en el mismo T = log 2 (S_2² ≠ 0 ⟺ 2T > log 4), mientras que borrarlo no cambia el fallo (`ROUND_006` §7.3).
Pregunta abierta concreta: si el umbral DIR coincide con T*_odd (P47 thm:index, log 2 ≤ T*_odd ≤ 0.81, segunda
dirección negativa de Arch); ℓ es par, así que la coincidencia, si existe, no es directa. OPEN.

## 5. Respuesta a (iv)

No se produce fórmula cerrada para ℓ, θ_p, W_p. Lo que se prueba es la imposibilidad en la clase 𝒢 (Teorema 2.1),
para cualquier número de primos (el argumento sólo usa ΣV_p ≥ 0), con lo que el enunciado de tres primos de la
clase es el mismo NO-GO. Controles de falsificador: no proceden para un NO-GO; nótese que el Teorema 2.1 no depende
del peso (vale para cΛ, para el peine sin una potencia y para pesos de tipo Beurling), lo cual confirma que 𝒢 no
puede distinguir c = 1 y que, por `ROUND_006` §10.3 (ventana de positividad en c de anchura ≲ 10⁻³ en T = 0.70),
cualquier fórmula superviviente debe caer fuera de 𝒢 y depender del peso con esa precisión.

Condición para reabrir el punto (iv): una cota Π_p ⪯ M_{V_p} sobre P_T con V_p de signo variable, escrita a partir de
la restricción de Tate y de los valores exactos v_2, v_3, que cumpla (K1)–(K2) y (E_ℓ) en T = 0.70. No se propone.

## 6. Lista de afirmaciones

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | Lema 1.1, identidad de estado fundamental por primo, con truncamiento | PROVED |
| 2 | La gauge del régimen de emparejamiento y el estado fundamental de cadenas son la misma cota de Schur | PROVED (por 1) |
| 3 | P47 cor:Tarch: fondo de Arch sobre P_T < 0 para T > T*_{∞,P}, T*_{∞,P} ∈ [0.58, 0.60] | CITED |
| 4 | Teorema 2.1: la clase 𝒢 (contactos acotados por potenciales ≥ 0, φ_p posicional, cadenas, θ_p(t,s), W_p(t), cualquier número de primos) no certifica para T > T*_{∞,P} | PROVED relativo a 3 |
| 5 | Corolario 2.2: la hipótesis del encargo no explica el umbral 0.695–0.70 | PROVED relativo a 3 |
| 6 | Cobertura de los NO-GO previos (𝒦_gap, INV_N_001) sobre la variante por primo: no literal | ARGUED (lectura) |
| 7 | Dual continuo del reparto DIR con min(Y_2, Y_3) y densidad común | PROVED en Galerkin; ARGUED en el continuo |
| 8 | Holgura complementaria (K1)–(K3) | PROVED en Galerkin; ARGUED en el continuo |
| 9 | Ecuación (E_ℓ) para ℓ | PROVED en Galerkin bajo rango uno de X; ARGUED en el continuo |
| 10 | ℓ ≈ dirección periódica de periodo log 2 en cadenas | ARGUED |
| 11 | Relación del umbral DIR con T*_odd | OPEN |
| 12 | Clase de cotas con V_p de signo variable sobre P_T | OPEN, sin objeto |
| 13 | Datos de ROUND_006 usados (umbral, ℓ, ventana en c) | NUMÉRICO (no recalculados) |
| 14 | Signo global | OPEN |
