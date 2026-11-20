# Revisión de la puerta de selección tras la ronda 6 (reparto por reglas: bandas de distancia y potenciales por primo)

Memo revisada: `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§1–9 y la propuesta que sale de §9.4: probar que «para
acotar por debajo el término de un primo p, el núcleo a la distancia de su propio contacto no aporta nada»,
escribir con ello un reparto por reglas (cada distancia para el primo que no tiene contacto allí, más
potenciales W_p(t) libres), calcular su déficit a mano y buscar después una corrección con signo.

**Veredicto: RECHAZADA en la puerta.** El objeto propuesto es la clase M de la propia memo, cuya parte de
núcleo es exactamente la de `G2_B8_R5` Def. 1; la «regla de bandas» es la holgura complementaria del Teorema D
de ese antecedente y ya se lee en sus números impresos; el lema, en su enunciado literal, es falso; no hay
mecanismo de signo (formato afín en el peso, regla independiente del peso, corrección con signo sin objeto).
Signo global OPEN. Nada de lo que sigue lleva signo.

Notación: I = I_T = (−T, T), u_p = log p, ε_F(u) = ‖F‖² − c_F(u) = ½‖F − F_u‖², v_p = 2 log p/√p.

## A. Antecedentes

A1. **`phase-159-row-d-two-front-construction/G2_B8_R5.md`, Def. 1, Lema 2.1, Teorema D, Teorema L″, §5.**
Leído entero en primaria.
- Def. 1: reparto (C_p, K_p) con C_p **constantes** (ΣC_p = C_0) y K_p = θ_p(u)K(u), θ_p medible, función
  **sólo de la distancia**, θ_p ≥ 0, Σθ_p = 1. Forma local q_p = C_p‖F‖² + ∫ε_F K_p + Q_p. Admite cualquier
  θ_p(u) medible: los repartos todo-o-nada por bandas de distancia están dentro de la clase.
- Teorema D, paso 4 de la prueba: el máximo sobre θ contra una familia de estados se alcanza en
  θ_p(u) = 𝟙{p realiza max_q ε_{σ_q}(u)}. Es decir, **el reparto óptimo es todo-o-nada por distancia, y la
  distancia u va al primo cuyo estado tiene el mayor déficit ε_{σ_p}(u)**, que es el primo cuyo estado tiene
  la menor autocorrelación en u. Un primo cuyo estado maximiza c(u_p) pierde la distancia u_p. Esto es el
  contenido de la tabla de §9.3 y de la frase «cada primo cede el núcleo en las distancias de sus propios
  contactos».
- Los números ya impresos allí (§4, «Independent checks») dan la misma asignación: c_{F_2}(log 2) = 0.3688,
  c_{F_3}(log 2) = 0.3029, luego ε_{F_2}(log 2) = 0.631 < ε_{F_3}(log 2) = 0.697 y la distancia log 2 va al
  primo 3; c_{F_2}(log 3) = −0.0355, c_{F_3}(log 3) = 0.0010, luego ε_{F_2}(log 3) = 1.036 > ε_{F_3}(log 3)
  = 0.999 y la distancia log 3 va al primo 2. La «regla» de §9.3 está en el par de prueba de L″.
- §5 da la lectura del fallo: el signo en (T_loc, log 2] lo lleva la interferencia entre c_F(log 2) y
  c_F(log 3) dentro de una misma autocorrelación; un reparto por factores paga el máximo de los déficits.
- **Alcance exacto de D y L″ respecto de la propuesta.** Cubren θ por bandas de distancia con C_p constante.
  **No cubren** W_p(t) dependiente de la posición: con W_p libre el dual cambia (los estados han de tener
  igual densidad puntual; el par de L″ tiene densidades distintas y no es admisible), como dice la propia
  `ROUND_006` §5. Tampoco cubren θ(t, s) (clase DIR). L″ no excluye, tal como está escrito, la clase M.
- Estado del antecedente: L″ es «machine-verified», sin aritmética de intervalos, y figura sin auditar en
  IDX `04_PHASES_100-189.md` filas G4A-159 (l.414), G8A-159 (l.427), G4A-R160_S5 (l.533, «DEAD [T ≥ 0.5925
  uncertified]»), G4C-R160_S5 (l.544, «joint cross-prime constraint», OPEN-RESIDUE); GRID l.239, 517, 708;
  `R159_099_SYNTHESIS.md` l.157.

A2. **`G2_B8_R4.md` §1 (l.104–110).** Sin la restricción θ_p ≥ 0 (piezas que no son de Lévy) el reparto es
vacío: se da todo a una pieza y la existencia es el objetivo. Antecedente directo de «buscar después una
corrección con signo».

A3. **`ROUND_005_G1.md` §3 (bloque «Factores de Euler…») y `ROUND_005_G5.md` L2 y «Siguiente paso
concreto»; `REVIEW_005.md`, «Lo que la ronda deja sin excluir», punto 1; LEDGER fila R5; IDX README l.2489.**
Ya registrado: reparto de Lévy = G2_B8, muerto en T ≥ 0.5925; reparto no invariante por traslación «con
fórmula propia» = no excluido y sin objeto; «con reparto libre su existencia equivale al objetivo». La
ronda 6 es la exploración numérica de ese residuo; la propuesta revisada pretende dar la fórmula.

A4. **Potencial dependiente de la posición y contacto como átomo de salto.**
`phase-195-modern-tools/INV_N_001_BAKRY_EMERY_GAMMA2_GAP_CEILING_NO_GO.md` §1 (PROVED): 𝔞_T = E_T + ∫W_T F²
con −v c_F(u) = ½v∫(F(t) − F(t+u))² − v‖F‖², medida de salto ν(u)du + ½Σv_nδ_{log n} y W_T(s) explícito;
`phase-211-sign-sandbox/ROUND_005_D.md` §§1–2 (forma de saltos con el peine como medida atómica,
representación de estado fundamental; LEDGER 211 C17, NO-GO de clase 𝒦_gap); `phase-162…/R162_504` Teor. 1
(forma de Beurling–Deny); CA_I_001 Teor. 2 (clase de Markov cerrada bajo añadir masa positiva al peine).
La lectura de `ROUND_006` §4.5 («q_p tiene medida de salto θ_pK + (v_p/2)δ y un potencial») es esta
descomposición hecha primo a primo. Las herramientas que firmarían cada q_p ⪰ 0 (principio del máximo,
estado fundamental, Hardy/Picone, hueco) son las de esas clases, monótonas en la medida de salto.

A5. **Partición dependiente de la posición del núcleo arquimediano.** `phase-188-closing-D/
L2_BUILD_004_IMS_LOCALIZATION.md` §§1–4 (identidad de localización con ω̃(x, y)K; «los primos son puro
acoplamiento»; repetición declarada de 106_47, 106_59 y de la opción rechazada de la fase 121); 211
`POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION` §7 (resto IMS indefinido). Es partición por posición en el espacio,
no por primo: antecedente lateral, no coincidencia.

A6. **No encontrado** (búsqueda por «local certificate», «T_loc», «reparto», «bang-bang», «todo o nada»,
«igual densidad», «cross-prime», «cede», en `03-research/` y `05-meta-and-planning/`; no exhaustiva y sin
valor de prueba de novedad): un reparto por primo con θ_p(t, s) dependiente de las dos posiciones (clase
DIR); la dualidad con estados de igual densidad puntual; el umbral cerca de log 2 de esa clase. Estos tres
puntos de la ronda 6 no tienen antecedente textual. Ninguno es el objeto propuesto.

## B. El lema «el núcleo en el contacto propio no aporta»

B1. **No está enunciado, probado ni refutado en el corpus** como lema. Sólo aparece como heurística en
`ROUND_006` §9.4. Lo que sí está probado es su forma correcta: la holgura complementaria de A1 (Teorema D,
paso 4), que es una propiedad del par óptimo y no una regla previa.

B2. **Enunciado literal: FALSO (PROVED en el caso u_p − δ < T; ARGUED fuera de él).** Sea
q_θ(F) = ∫W_pF² + ¼∬θK(F(t) − F(s))² − v_p c_F(u_p), con θ ≥ θ_0 > 0 cerca de la diagonal (el ínfimo
μ(θ) sobre la esfera unidad de P_T se alcanza: la forma domina una energía logarítmica y la inclusión es
compacta), y sea B = {(t, s) ∈ I²: ||t − s| − u_p| < δ}, E_B(F) = ¼∬_B K(F(t) − F(s))². Para η > 0 sea
F_η un minimizador de q_{θ+η𝟙_B}. Entonces μ(θ) ≤ q_θ(F_η) = μ(θ + η𝟙_B) − ηE_B(F_η). Si el núcleo en B no
aportara, μ(θ + η𝟙_B) = μ(θ) y E_B(F_η) = 0, es decir F_η(t) = F_η(s) para casi todo par a distancia en
(u_p − δ, u_p + δ). Eso hace a F_η constante en (−T, T − u_p + δ) y en (−T + u_p − δ, T), con el mismo
valor. Si u_p − δ < T los dos intervalos se solapan y F_η es constante en I, incompatible con
∫F e^{t/2} = 0 salvo F = 0. Luego **μ crece estrictamente al añadir núcleo en cualquier banda alrededor del
contacto propio** en cuanto T > u_p − δ (para p = 2: toda T ≥ 0.70, que es justo el rango donde se quiere
usar la regla). Si u_p − δ ≥ T, la igualdad exigiría un minimizador constante en las dos zonas extremas:
no excluido por este argumento, no genérico (ARGUED).

B3. **Lo que la heurística sí contiene (PROVED, elemental, y sin alcance sobre el ínfimo).** La energía a
la distancia exacta u_p se anula sobre las F con F(t) = F(t − u_p) en la cadena. A distancias vecinas
u_p + w no se anula: sobre esas F vale ∫(F(t) − F(t − u_p − w))² ≈ 2ε_F(|w|), de modo que la banda actúa
como un núcleo de corto alcance acotado, K(u_p)𝟙_{|w|<δ}, frente al núcleo K(w) ~ 1/w ya presente. La
banda «vale poco» en proporción ~ K(u_p)|w| y sólo mientras |w| ≲ 1/‖F′‖; con ‖F′‖² ≈ 110 (par de L″) eso
da |w| ≲ 0.1, compatible con las anchuras de banda de §9.3. La anchura depende, pues, del estado y no del
primo: no hay bandas fijas. La cuenta con los términos de borde no se hizo (ARGUED).

B4. **Lectura.** La versión verdadera es comparativa («en el óptimo, la distancia u va al primo cuyo
estado obstructor tiene mayor ε(u)») y sus bandas son {ε_{σ_p} < ε_{σ_q}}, definidas por los estados
obstructores, que se obtienen resolviendo el problema. Como regla previa es circular en el sentido de
`RULES_AVOID.md` J3. Con tres o más primos la regla «para el primo sin contacto allí» no determina a quién
va cada distancia.

## C. Los cuatro puntos

**(1) Antecedente.** Correcto pero incompleto. Faltan A2 (vacío del reparto con signo), A3 (el residuo ya
registrado) y A4 (forma de saltos más potencial, clases 𝒦_M, 𝒦_gap, 𝒦_BE).

**(2) Objeto nuevo.** No se sostiene.
- θ_p por bandas de distancia: dentro de `G2_B8_R5` Def. 1; el óptimo todo-o-nada por distancia es el paso 4
  del Teorema D.
- W_p(t): única diferencia real con el antecedente. Pero «bandas de distancia + W_p(t) libre» es la clase M
  de `ROUND_006` §2, y la tabla de §3 de la misma memo da para M τ = −1.60·10⁻⁴ en T = 0.5925 con
  a_T ≻ 0 (NUMÉRICO, una sola resolución, N = 20; el script entregado no deja identificar a simple vista el
  modo M, no se recalculó). La clase que alcanza el techo bajo log 2 es DIR, y §4.2 dice que lo hace por la
  dependencia de θ en las dos posiciones, justamente lo que la regla suprime.
- El lema: falso en su letra (B2); en su forma verdadera es A1.

**(3) Por qué evitaría la dificultad del antecedente.** No la evita. El argumento presentado («L″ es para
repartos invariantes; los potenciales dependientes de la ventana alcanzan el techo hasta log 2») atribuye a
W_p(t) lo que los números atribuyen a θ(t, s): con W_p(t) y θ(|t − s|) el reparto ya no alcanza el techo
en 0.5925. La dificultad de `G2_B8_R5` §5 (el primo 3 paga dentro del test del primo 2; un reparto por
factores cobra el máximo de los déficits) queda intacta en la clase M y reaparece en DIR pasado log 2 con
el mismo dibujo (§9.3).

**(4) Enlace con la positividad global.** Σq_p = a_T es correcto y trivial; el contenido está en q_p ⪰ 0,
y ahí:
- Con θ ≥ 0 la clase falla para T ≥ 0.70 con a_T ≻ 0 (§§7.3, 8.1, 8.4; NUMÉRICO, tres optimizadores). En
  el rango abierto no hay nada que certificar con ella.
- El formato es afín en el peso y la regla (qué distancia va a qué primo) no depende del peso: sirve igual
  para cΛ, para a_P y para cualquier peine con los mismos soportes. Para c < 1 certifica (§7.2); nada en la
  regla cambia en c = 1. `RULES_AVOID.md` B1/B8 y J2; `OBJECT_SPEC.md` O2, O4. La candidata no puede
  escribir el punto (5) de `OBJECT_SPEC.md` §4 (la línea que se rompe para cΛ y a_P).
- «Calcular el déficit y buscar una corrección con signo»: con piezas con signo sin cota la existencia del
  reparto es el objetivo (A2, A3); con cotas, §7.3(iii) da valores cerca del techo sin fórmula. Todo el
  signo quedaría en la corrección, para la que no se propone operación alguna. Es «otra energía auxiliar sin
  mecanismo de signo» (A4 de `RULES_AVOID.md`) y formato de certificado por ventana (O5).

**Resumen.** Repetición en la parte de núcleo (G2_B8_R5 Def. 1 y Teorema D), diferencia real sólo en W_p(t),
que según los datos de la propia ronda no basta; lema falso en su letra y ya contenido, en su forma
verdadera, en el antecedente; formato de certificado sin mecanismo. No se autorizan derivaciones del
reparto por reglas ni el cálculo de su déficit.

## D. Condición de reapertura

Se reabre sólo con una de estas operaciones, escrita antes de derivar:

1. Una fórmula cerrada para θ_p(t, s) (dependiente de las dos posiciones, no de |t − s|) y W_p(t), no
   obtenida de un optimizador ni de los estados obstructores, **que dependa de los valores exactos del peso
   de modo no afín** o de una relación entre contactos de primos distintos (por ejemplo las posiciones
   log 2, log 3, log(9/4), log(3/2) juntas), con la línea que se rompe en cΛ y en a_P señalada como pérdida
   de no negatividad de un término concreto; y un enunciado para tres primos.
2. Para la parte con signo: una identidad que escriba la pieza negativa de θ_p como cuadrado compensado por
   un término nombrado de otro primo (acoplamiento entre q_2 y q_3 que no sea reparto), con resto
   manifiestamente ≥ 0. Sin esa identidad, «corrección con signo» es el objetivo.

Primer control de cualquier reapertura: en T = 0.5925, N = 20, la fórmula debe dar q_2, q_3 ⪰ 0 donde la
clase M da −1.60·10⁻⁴; si la fórmula cae en M, queda falsificada por ese punto (sujeto a confirmar el valor
de M en N = 30, 40).

## Resultados que se anotan (sin signo)

R6-a (PROVED relativo a `G2_B8_R5` Teorema D). La asignación «cada primo cede la distancia de su contacto»
es la holgura complementaria del reparto óptimo; ya está en los valores impresos del par de L″.

R6-b (PROVED para T > u_p − δ; B2). Añadir núcleo en una banda alrededor de la distancia del contacto propio
aumenta estrictamente el fondo de la forma local. «No aporta nada» es falso.

R6-c (NUMÉRICO, de `ROUND_006` §§3, 7.3; no recomprobado aquí). Clase M negativa en 0.5925; clase DIR con
θ ≥ 0 alcanza el techo hasta 0.69 y falla desde 0.70. Sin prueba en el continuo en ninguna dirección.

Sin antecedente textual y sin objeto: θ_p(t, s) de dos posiciones con fórmula propia; dual de igual
densidad puntual (ARGUED en §5, comprobado sólo en la discretización).

## Reservas de esta revisión

- No se reejecutó ningún script; los valores de la ronda 6 se toman como NUMÉRICO.
- L″ sigue sin aritmética de intervalos y sin auditoría registrada.
- B2 usa que el ínfimo se alcanza (compacidad por la singularidad 1/u del núcleo con θ ≥ θ_0 > 0 cerca de
  la diagonal); en la clase todo-o-nada con θ_p = 0 cerca de la diagonal el argumento se aplica a la pieza
  que conserva el núcleo corto, o al modelo de Galerkin.
- No cotejadas en primaria: fases 155–156 (certificados por ventana) más allá de grep, Paper 48, y las
  carpetas anteriores a la fase 100.
