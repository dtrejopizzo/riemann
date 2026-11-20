# Ronda 14, memo C: transición entre ventanas que no es la inclusión

Notación del brief común. a_T(F) = Arch_T(F) − Σ_n v_n c_F(log n) sobre P_T, v_n = 2Λ(n)/√n,
λ(T) = inf{a_T(F)/‖F‖² : F ∈ P_T, F ≠ 0}. Controles: 𝒞 = {2Λ, borrado de una potencia de primo, Beurling}.

Idea sometida a la puerta: una aplicación lineal Φ = Φ_{T→T′}: P_{T′} → P_T, distinta de la restricción, con

  (E) a_{T′}(F) = κ·a_T(ΦF) + R(F),   R ≥ 0 manifiesto, κ > 0,

o la versión en desigualdad a_{T′} ≥ κ a_T∘Φ, de modo que la positividad suba de ventana en ventana desde la región
probada (T < ½log 2, donde no hay contactos y a_T = Arch_T ≥ 0 hasta T ≈ 0.60, Paper 47 cor:Tarch).

## 1. Filtro de cuatro puntos

**(1) Antecedentes más cercanos, leídos en primaria.**
- `phase-186-toolbox/R186_029_SYNTHESIS_ROUND14.md`, Lema H y lista (α)–(δ) de lo que escapa: congruencia,
  Schur, rango finito y cociente relativo heredan el margen; escapa sólo (β) «descomposición exacta con resto
  cero», que uniforme en T colapsa en thm:Z de Paper 47. También W11′ (R184_015): toda descomposición
  W_T = Pos + Δ_T tiene a la positividad misma como mitad inferior.
- `phase-160-row-d-infinite-T/R160_D4_R2.md`, Thm 3.4 y Thm 5.1: la completación de Chebyshev
  comb(S_X F) = ℒ_X(F) − ℛ_X(F) y el cierre «positividad a través de cualquier identidad de convolución sobre
  tests = λ^W_{T+½log X} ≥ 0 por ventana, W^{Li} ≥ 0 en el límite». Cubre exactamente: aplicaciones que actúan
  sobre los tests por dilataciones/convoluciones de Dirichlet sin compresión de borde; S_X lleva P_T a funciones
  con soporte en la ventana desplazada T + ½log X. Es decir, cubre la dirección P_T → P_{T′} (hacia arriba en
  soporte), que transporta la positividad en la dirección equivocada.
- `phase-161-row-d-sum-product-square/R161_002*.md` §3: la única salida a Thm 5.1 es la versión comprimida
  E_{N,T} = P_T(S_N𝓕 − J S_N)Π_T y las fugas C_T, C_T^{(N)}. Sus residuos: RULES_AVOID R1 (el término de borde es
  el conmutador de soporte ⟨g,[P,S]w⟩, sin signo; R161_057–065), U2 y V1 (L161.3–L161.6 cerrados o circulares).
- `phase-211-sign-sandbox/ROUND_021_A*.md` Lema 3.3 (sándwich de ventana): J_R ⊇ [1 − λ_0/‖𝒦‖, 1 + λ_0/‖𝒦‖] y
  J_R → {1} cuando λ_0 → 0.
- `ROUND_013_C.md` §4.1 (flujo en T con paso dependiente de la historia; flecha equivocada; repetición de Lema H(iv))
  y RULES_AVOID Q2 (predicado de etapa con paso uniforme = reparto local).
- Índice: `04_PHASES_100-189.md` filas W7 («Λ∗1 = log lineal = desplazamiento de ventana»), G6A-R160_D4_R2
  (DEAD, window shift), G6E-R162_802 (Λ∗1 = log = traslación de ventana en el flujo), G2E-R160_S4 §3.2#7
  («desplazamiento efectivo RD_{T′} implica λ^W_T ≥ 0», OPEN-RESIDUE: la flecha es la de la restricción).

**(2) Objeto nuevo.** Una transición Φ_{T′→T} hacia abajo en soporte, no restricción, con resto R de (E). En el
corpus las transiciones aparecen en la dirección de la inclusión (P_T ⊂ P_{T′}, S_X: P_T → P_{T+½log X}); la
dirección descendente con resto firmado no tiene memo propio. Esto es lo único con marca.

**(3) Por qué esquivaría la dificultad.** La inclusión da λ(T′) ≤ λ(T): flecha equivocada. Una Φ descendente
invierte la flecha formalmente: si a_T ≥ 0 y R ≥ 0 entonces a_{T′} ≥ 0.

**(4) Conexión con la positividad global.** Encadenando T_0 < T_1 < … con T_k → ∞ y T_0 < ½log 2: a_{T_k} ≥ 0 para
todo k, luego para todo T por monotonía. Es exactamente la positividad global.

**Resultado de la puerta.** El punto (3) es sólo formal: §2 prueba que el resto R hereda íntegra la obligación de
signo de la ventana grande, con margen ≤ λ(T′). Es la cara entre ventanas de W11′ y de Lema H; no hay mecanismo
nuevo para el signo. **No pasa.** No se construye. Se registra un NO-GO de clase (§2) y el estado exacto (§4).

## 2. La transición no rebaja la obligación de signo

**Proposición M (PROVED, álgebra lineal).** Sea Φ: P_{T′} → P_T lineal cualquiera, κ > 0, y R := a_{T′} − κ a_T∘Φ.
Supóngase a_T ≥ 0 (hipótesis inductiva). Entonces:
(i) R ≤ a_{T′} como formas en P_{T′}; en particular inf_{‖F‖=1} R(F) ≤ λ(T′).
(ii) R ≥ 0 en P_{T′} implica a_{T′} ≥ 0; si F*_{T′} es un minimizante unitario, R(F*) ≤ λ(T′) y
κ a_T(ΦF*) ≤ λ(T′).
(iii) Si R ≥ 0 y ‖ΦF‖ ≥ s‖F‖ en P_{T′}, entonces λ(T′) ≥ κ s² λ(T); como λ(T′) ≤ exp(−e^{(2−ε)T′}) (Paper 47
thm:margin, CITED), κ s² ≤ λ(T′)/λ(T): o bien Φ es casi no inyectiva exactamente en la dirección del minimizante,
o bien R es una forma cuyo fondo es ≤ λ(T′).
*Prueba.* (i) κ a_T(ΦF) ≥ 0. (ii) a_{T′} = R + κ a_T∘Φ ≥ R, y a_{T′}(F*) = λ(T′) con ambos sumandos ≥ 0.
(iii) a_{T′}(F) ≥ κ λ(T)‖ΦF‖² ≥ κ s² λ(T)‖F‖². ∎

Lectura. «R ≥ 0» es un enunciado de signo en la ventana T′ más fuerte que la meta (R ≤ a_{T′}) con fondo de
tamaño a lo sumo λ(T′). Hay dos maneras de certificarlo: (a) por otra transición (regreso infinito, misma
obligación) o (b) como suma manifiesta de cuadrados con resto cero en la ventana T′, que es el tipo (β) de
R186_029 = certificado dual de Paper 47 def:PD en esa ventana; uniforme en T, thm:Z. La transición sólo reparte la
forma en dos piezas, una de ellas positiva por hipótesis: es W11′ con Pos := κ a_T∘Φ. Repetición. La dependencia de
la historia (Φ construida con todos los primos previos, a la Λ∗1 = log) no cambia (i)–(iii): éstos valen para
cualquier Φ.

**Lema C (PROVED, combinando Lema T de ROUND_013_C y Lema 3.3 de 211 ROUND_021_A).** El caso base T_0 < ½log 2 es
ciego a los controles cΛ y al borrado (no hay contactos: a_{T_0} = Arch_{T_0}, independiente del peso). Para el
control c = 2 existe T con a_T^{2Λ} no ≥ 0 en P_T (ROUND_021_A Lema 3.3: J_R ⊂ [1 − δ_−, 1 + δ_+] con δ_+ ≤ λ_0/K_0
→ 0, NUMÉRICO en las celdas medidas; CITED). Por tanto, en toda cadena T_0 < … < T_k que alcance esa T, algún resto
R_j debe dejar de ser ≥ 0 bajo c = 2. Como R_j es afín en c, su positividad debe usar c = 1 con precisión del
orden de λ(T_{j+1})/‖𝒦‖. Un R_j certificado por cuadrados ciegos y relaciones válidas en c = 2 probaría el
enunciado falso: ese es el paso que debe romperse, y tiene que romperse dentro de R, no en Φ. ∎

## 3. Las cuatro familias de Φ propuestas

- **Müntz / S_N^* comprimido**, ΦF = P_T Σ_{n≤N} n^{−1/2}F(· + log n). Su forma de pullback es
  ⟨F, S_N P_T A_T P_T S_N^* F⟩; frente a A_{T′} la diferencia contiene la completación de Chebyshev (Thm 3.4 de
  R160_D4_R2, versión adjunta) más el conmutador de soporte [P_T, S_N]. Sin compresión, Thm 5.1 identifica la
  positividad con la de la ventana desplazada (cubierto). Con compresión, el término nuevo es el conmutador de
  borde de R161_057–065 (RULES_AVOID R1), sin signo. Φ-como-transición no es un residuo distinto: es el
  emparejamiento comprimido de R161_002 §3 leído con a_T en lugar de un cuadrado. ARGUED (no se rederivó la
  expansión completa). Además Φ anula toda F con soporte en [−T′, −T − log N) (las traslaciones mueven a la
  izquierda), de modo que en ese subespacio (codimensión ≤ 2 dentro de P_{T′}) (E) exige R = a_{T′}: allí la
  transición no aporta nada (PROVED, trivial).
- **Plegado** F ↦ F ± F(· − log p) con truncación: suma finita de traslaciones, misma clase; Proposición M aplica.
- **Escala** t ↦ 2t, F ↦ √2 F(2·): no preserva P (∫F(2t)e^{±t/2}dt = ½∫F(s)e^{±s/4}ds, constraints distintas),
  K(u) no es homogéneo, y los contactos log n van a ½log n, que no son logaritmos de enteros salvo n cuadrado; el
  resto contiene el peine en posiciones no aritméticas con pesos n^{−1/2} desajustados. Proposición M aplica
  igual. ARGUED en cuanto a la forma del resto; PROVED en cuanto a P.
- **Promedio de Hecke** sobre d | N: suma finita de traslaciones por log d; misma clase.

Primera instancia pedida ({2,3} → {2,3,4} → {2,3,4,5}): Proposición M fija que todo resto R tiene fondo
≤ λ(T′) ≈ 5·10⁻⁵ (orden de los márgenes medidos en 211 para R = 4, CITED) y, por Lema C, debe distinguir c = 1
de c = 1 + O(λ_0/K_0). No se escribe Φ explícita porque ninguna elección cambia esa obligación.

## 4. Veredicto y estado

- Puerta: **no pasa**. La transición descendente es W11′/Lema H (β) entre ventanas: R ≤ a_{T′} y R ≥ 0 es la meta en
  T′ con margen igual o menor (Proposición M, PROVED, para toda Φ lineal y todo κ). Clase NO-GO declarada: «paso
  inductivo T → T′ de la forma (E) con Φ lineal arbitraria y R certificado por otro paso del mismo tipo o por
  cuadrados ciegos»: no rebaja la obligación (PROVED) y, con cuadrados ciegos, probaría el control c = 2 (Lema C,
  PROVED relativo a la falla de c = 2, CITED/NUMÉRICO).
- Pregunta (1): Thm 5.1 cubre las Φ ascendentes no comprimidas; las descendentes comprimidas por S_N^* caen en
  R161_002 §3 / R161_057–065 (ARGUED). Pregunta (2): el paso que debe romperse bajo c = 2 es el certificado de R,
  no Φ. Pregunta (3): la pérdida multiplicativa no es el problema; con R ≥ 0 se obtiene λ(T′) ≥ κ s² λ(T), y el
  margen obliga a κ s² ≤ λ(T′)/λ(T).
- Lo que queda (OPEN, sin objeto): transiciones no lineales en F (tipo (γ) de R186_029: Φ que dependa del
  minimizante de a_T), donde Proposición M (i) sigue valiendo si a_T(Φ(F)) ≥ 0, y por tanto tampoco escapan
  salvo que R sea de resto cero. No hay siguiente operación explícita defendible desde esta idea.

## 5. Para el revisor

Rederivar: Proposición M (tres líneas); Lema C (requiere sólo la afinidad en c y la existencia de T con
a_T^{2Λ} indefinida, que se toma de 211 ROUND_021_A §2–3); la no preservación de P bajo t ↦ 2t; el núcleo de
P_T S_N^* sobre [−T′, −T − log N). Verificar en primaria que la lectura de R161_057–065 como cierre del término
de borde corresponde a [P_T, S_N] y no a otra compresión.
