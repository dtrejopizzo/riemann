# Ronda 11, A: los residuos abiertos de (PC) y la discrepancia reticular unilateral

Notación del brief común. τ_aF(t) = F(t+a); S_N = Σ_{n≤N} n^{−1/2}τ_{log n}; C_N(D) su continuo polar,
(C_N(D)g)(t) = e^{−t/2}∫_{−∞}^{t+log N} e^{y/2}g(y)dy; S_N^ren = S_N − C_N(D); P = P_T; A = A_M el operador de la
forma; ℓ_T(F) = (1−P)AF la fuga exterior; 𝓕 la transformada aditiva transportada.

**Resultado.** Ninguna candidata pasa la puerta. El mecanismo de discrepancia reticular con signo (test integral,
Hermite–Hadamard, primer resto de Euler–Maclaurin) muere ante L161.3 por dos motivos. (a) El resto Δ^R ℓ_T(F) es
lineal en F, y un signo uniforme de un funcional lineal impar sólo es posible si el funcional es idénticamente nulo.
(b) El peine que muestrea es de pesos unidad n^{−1/2}: el signo de Euler–Maclaurin no ve Λ y es el mismo para cΛ,
para el borrado y para Beurling. El intercambio log n = ∫dx/x vía Λ∗1 = log recae en el primitivo escalar de
Stieltjes (R161_004 Cor. 2.1; Paper 41 C4–C5) y en el resto de Bernoulli firmado (106_109 (9)–(10)). Ambos están
cerrados.

## 0. Paso 0: los cuatro residuos, en primaria

Leí completos R161_004, 005, 006, 020 y 023. De R161_015, 016, 021, 022, 029, 038, 041 y 050 leí las secciones de
enunciado y de estado. También leí R163_153 y R170_853 §§4–5, RULES_AVOID K, L y T, y ANNEX_161_FILES_1 §(c)
y _2 (038, 050).

### 0.1 L161.3 / PC-port (R161_004 §6, R161_005 §5, R161_006)

- **Enunciado abierto.** Sea F un estado primitivo de primer contacto: PAPF = r = αe^{−t/2} + βe^{t/2}. El puerto
  B^ren_{N,T}(F) = PS_N^ren(1−P)AF, en su límite orientado y antes de cualquier traza, tendría que tener un símbolo
  normal crítico no nulo. Además, la ecuación de igualdad junto con la cancelación de Tate tendría que anularlo
  (R161_005 §5).
- **PROVED alrededor.**
  - (005 Teor. 1.1) PR_{M,N}𝓕F = PS_N r + B_{N,T}(F).
  - (006 Teor. 2.1) B^ren(F)(t) = Δ^R_{N,T}ℓ_T(F)(t) − e^{−t/2}a_−(ℓ_T(F)), con
    Δ^R_{N,T}g(t) = Σ_{e^{T−t}<n≤N} n^{−1/2}g(t+log n) − e^{−t/2}∫_T^{t+log N}e^{y/2}g(y)dy,
    y la reflexión correspondiente para Δ^L.
  - Cámara 0.8 < T < ½log5: Z_{T,−}^{−1} = I − K + K² (005 §4).
- **Por qué se detuvo.** El cuadrado ‖B‖² pierde la orientación (005 §2). La traza escalar recae en Paper 41 C5
  (004 §2). Llevarlo a una historia de divisores recae en el no-go CMO de la fase 121 (004 §3).
- **Memos posteriores.** R161_028–029: la capa polar es la imagen exterior. La norma de la discrepancia móvil
  N_f(a) = ‖Z_af‖² tiene derivada (2.2) y saltos (3.2) indefinidos; la monotonía ordinaria es **FALSA** (029 §7).
  El signo que queda se identifica con la compuerta inversa de Markov de R161_016. Cerrado en la clase
  «monotonía de la norma de la discrepancia» por un falsificador numérico (script 161_02). La versión orientada
  sigue OPEN.
- **Controles.** Δ^R tiene pesos unidad y no contiene Λ. Los pesos sólo entran a través de g = ℓ_T(F). Con cΛ y con
  el borrado de una potencia de primo cambia g y el operador Δ^R queda igual. Beurling cambia la retícula del peine
  (R161_001 Teor. 4.1: falta el dato de Poisson entero).

### 0.2 L161.4 (R161_020 §5)

- **Enunciado abierto.** Construir V_{M,N,T}F a partir de (PC-ren), heredado del producto zeta y de los términos
  de Tate cruzados y sin definirlo a partir de L^sc, tal que lim‖H_T^−E_N^ren V F‖² = L_T^sc(F) := ‖(I−P_+)C_log g‖².
  La identidad finita de primer contacto tendría que anular el miembro izquierdo.
- **PROVED alrededor.**
  - Rigidez de compresión unitaria (Lema 1.1).
  - Cuadrado de fuga (0.2).
  - Error (3.4).
  - Forma de Hardy (4.3).
  - Cierre por la red de polos Gamma (R161_019).
- **Por qué se detuvo.** E_N^ren → 0 fuertemente, de modo que todo límite lineal acotado mata ambos lados
  (R161_016 §3 lo prueba en la clase de límites fuertes acotados). Falta una V que no sea circular.
- **Posteriores.** K1 de RULES_AVOID: «los cuadrados de fuga son correctos, pero no hay identidad que los conecte
  con el defecto de PC». No hay no-go ni falsificador. Sigue OPEN.
- **Controles.** L^sc no contiene pesos aritméticos; sólo C_log y el soporte. El dato aritmético tendría que entrar
  por V, y por eso los controles no se pueden evaluar hasta que V exista.

### 0.3 L161.5–L161.6 (R161_021 §5, R161_022 §4, R161_023 §5)

- **Enunciado abierto.** Encontrar una ley de borde antisimétrica, obtenida de (PC-ren) en dos orientaciones antes
  de recombinar, que lleve Re⟨g_N, S_N^ren w_N⟩ → 0. Tiene que distinguir ⟨g_N, S w_N⟩ de ⟨S*g_N, w_N⟩ a través del
  borde móvil y no puede seguirse de a_T(F,H) = 0 para H primitivo.
- **PROVED alrededor.**
  - Criterio X_T(F) = 0 ⇔ C_log g = −εg ⇒ F = 0 (021, 023 (5.1)).
  - Proyección de Tate ⟨r, ΤPy⟩ = ⟨Sr, g⟩ (023 (1.3)).
- **Por qué se detuvo.** El test canónico Π_TP_TZ*g recombina tautológicamente en (PC-ren). Usar la matriz cruzada
  como Gram es REJECTED.
- **Posteriores.**
  - R163_153: para un puerto con soporte a la derecha, el test vale exactamente 0 para todo N. Es un no-go por
    soporte y polaridad que vale para cualquier peine de pesos unidad.
  - R170_853 §4: imponer z_F = 0 repite L161.6.
  - Índice 04, G1C-R161_022-023: REF-D.
- **Controles.** El colapso de R163_153 no usa Λ, de modo que es ciego a los tres controles. La ley buscada no
  existe todavía.

### 0.4 Mínimo del puerto / pullback inverso (R161_015 §4, R161_016 §2)

- **Enunciado abierto.** Sobre el radical de primer contacto, N_T(δ) − N_T(0) = ‖D_{EΓ,δ}E^phys_{T,δ}F‖² + R con
  liminf R/δ ≥ 0, construido desde las fuentes (016 (2.2)).
- **PROVED alrededor.**
  - Pendiente de norma −2∫(t−T)|g|² (015 Teor. 3.1).
  - Equivalencia con la última cota superior (015).
  - Criterio condicional de cierre (016 Teor. 2.1).
  - El pullback directo de Markov da la flecha automática (016 Prop. 1.1).
  - El dato finito 2, 3, 4 controla sólo el primer collar (016 §5).
- **Por qué se detuvo.** Hace falta una dispersión de orden cero que invierta entrada y salida, y E_N^ren no puede
  serlo.
- **Posteriores.** R161_029 identifica L161.11 con esta compuerta. R161_038 y R161_050 cierran la clase formal
  (involuciones + (PC) lineal + radicalidad + paridad) mediante contramodelos 2×2 y 3×3. Sigue OPEN fuera de esa
  clase.
- **Controles.** No están evaluados.

Los cuatro residuos están formulados sobre el radical de un primer contacto supuesto. Ninguno es una identidad
sobre todo P_T (aviso de ANNEX_161_FILES_1 §(c)).

## 1. Paso 1: la discrepancia reticular sobre L161.3

**(i) La función φ.** En Δ^R hago el cambio y = t + log x. Queda
Δ^R g(t) = Σ_{e^{T−t}<n≤N} φ_t(n) − ∫_{e^{T−t}}^{N} φ_t(x)dx, con φ_t(x) = x^{−1/2} g(t + log x) y g = ℓ_T(F).
Es exactamente una discrepancia reticular unilateral con extremo inferior móvil e^{T−t} (PROVED, cálculo directo).
φ_t no es ni un cuadrado ni un producto: es **lineal** en F.

**(ii) Ordenamiento monótono o convexo para todo F.**

- **Lema 1 (PROVED).** Supongamos que existe una regla de signo σΔ^R ℓ_T(F)(t) ≥ 0 válida para todo F de P_T, o
  para todo F de un cono que contenga a −F junto con F. Entonces Δ^R ℓ_T(F)(t) = 0.
  *Prueba.* El funcional es lineal e impar. ∎
- Para obtener un signo útil hay que pasar a una forma cuadrática ⟨h(F), Δ^R ℓ_T F⟩. El sumando resultante es
  bilineal, φ_t(n)·(dato de h), y no tiene monotonía uniforme. La monotonía de x ↦ x^{−1/2}g(t+log x) en (e^{T−t}, N)
  exige que g sea esencialmente monótona en (T, ∞). La imagen exterior de A sobre P_T no es un cono de funciones
  monótonas (ARGUED: contiene ℓ_T(F) y −ℓ_T(F)).
- **Lema 2 (PROVED).** Δ^R depende sólo de la retícula ℤ_{≥1} y de los pesos n^{−1/2}; no contiene Λ. Por tanto,
  cualquier signo que provenga de la monotonía o la convexidad de φ_t (integral test, Hermite–Hadamard, primer resto
  de Euler–Maclaurin con B_1 firmado) se conserva sin cambios para cΛ con c = 2 y para el borrado de una potencia de
  primo, porque estos sólo modifican g. Por la disciplina R3-i, un signo así no rompe ante dos de los tres controles.
- **Intercambio por Λ∗1 = log.** La desigualdad log n ≤ Σ_{m<n}1/m (error firmado γ + O(1/n)) es una afirmación
  escalar. Introducirla en Δ^R obliga a escalarizar la fibra de divisores antes del puerto. Eso es exactamente la
  clase cerrada de R161_004 Cor. 2.1: primitivo de Stieltjes de Paper 41 (3.10), completación C5 con cuadrado
  negativo e intervalo negativo bajo log 2. Lo que sí rompe ante cΛ es el defecto δ_a(k) = Σ_{d|k}a(d) − log k
  (R161_001 Teor. 4.1). Ese defecto es lineal en el peso y no es una discrepancia monótona (U1 de ANNEX_161: Λ∗1
  entra sólo linealmente).

**(iii) Cotejo con lo cerrado.**

- **106_109 §2 (9)–(10), §§5, 8–9.** La sumación por partes gaussiana deja un resto de Bernoulli firmado cuyo núcleo
  cambia de signo en cada celda del retículo. El signo de Euler–Maclaurin ya está identificado y no se transporta.
- **POWER_GRAM_SLICES §§8–8.3.** Los prefijos theta, la cola continua y la simetrización no restauran PSD. La
  discrepancia «enteros menos continuo» de una función theta pertenece a esa familia.
- **R161_004.** Los sucesores escalares de Stieltjes y las fibras positivas de divisores están cerrados. R161_041 no
  añade signo: la derivada de E da U+V y la de C da U−V.
- **R161_029.** La versión cuadrática natural, N_f(a) = ‖Z_af‖², tiene derivada y saltos indefinidos, y la monotonía
  es FALSA. Ésta es precisamente la «discrepancia reticular con signo» aplicada al objeto del residuo: ya está
  probada y falsada.
- **R161_038 y R161_050.** Los contramodelos no tienen semigrupo de traslaciones enteras ni continuo de
  Euler–Maclaurin (038 lo declara en «No modela»), así que en ellos no hay signo reticular disponible. Esto indica
  que el mecanismo está **fuera** de su clase. Pero no le da contenido: los Lemas 1 y 2 lo matan por linealidad y
  por ceguera al peso, independientemente de esos contramodelos.

**Diferencia neta: ninguna.** Me detengo antes de derivar.

## 2. Paso 2: no sobrevive ninguna candidata

| Residuo | Clase que lo cierra, u operación que falta |
|---|---|
| L161.3 | La monotonía de la norma de la discrepancia móvil es FALSA (029). El signo reticular lineal es trivial (Lema 1) y ciego al peso (Lema 2). La escalarización está cerrada (004). Falta un apareamiento **orientado** de dos orientaciones cuyo término cruzado tenga el signo de D^Poisson ≥ 0 (029 (6.1)). |
| L161.4 | No hay no-go. Falta V_{M,N,T} no circular, con convergencia de grafo proyectada (no fuerte), que lleve el dato aritmético. |
| L161.5–6 | El test conjugado directo es tautológico (023) y vale idénticamente 0 para un puerto derecho (R163_153). Falta una ley de concomitante de borde que no sea una consecuencia de la radicalidad, insertando 𝓕 antes de la adjunción. |
| Mínimo del puerto | La clase formal está cerrada (038, 050) y el pullback directo da la flecha automática (016). Falta una dispersión de orden cero que invierta entrada y salida. Es la misma compuerta que L161.11. |

**Orden.** Pondría primero **L161.4**. Es el único residuo cuyo objetivo es una igualdad entre dos cuadrados ya
PROVED ≥ 0, y nada en el corpus lo cierra: ni no-go ni falsificador, sólo «falta V». Los otros tres colapsan, en
memos posteriores, en una misma compuerta: el término cruzado orientado de 029 (6.1) y 016 (2.2). L161.4 tiene dos
reservas. Hereda la dependencia del radical. Y el enlace (4) con la positividad global sobre todo P_T no está
escrito en ninguna parte, de modo que habría que añadirlo antes de cualquier construcción.

## Afirmaciones y etiquetas

1. Δ^R ℓ_T(F)(t) = Σ φ_t(n) − ∫φ_t, con φ_t(x) = x^{−1/2}ℓ_T(F)(t+log x) y extremo inferior e^{T−t}: PROVED.
2. Lema 1 (un signo uniforme de un funcional lineal impar obliga a que sea nulo): PROVED.
3. Lema 2 (Δ^R no contiene Λ; un signo de monotonía es invariante ante cΛ y el borrado): PROVED.
4. La imagen exterior ℓ_T(P_T) no es un cono monótono: ARGUED.
5. El intercambio log n ↔ Σ1/m recae en R161_004 Cor. 2.1 y Paper 41 C5: CITED.
6. El resto de Bernoulli firmado ya está identificado (106_109; POWER_GRAM_SLICES §8): CITED.
7. La monotonía de la norma de la discrepancia móvil es falsa (R161_029): CITED (NO-GO numérico de esa memo).
8. 038 y 050 carecen de retícula entera, y el mecanismo cae fuera de su clase sin ganar contenido: PROVED (lectura
   de las definiciones).
9. Los estados de L161.3, L161.4, L161.5–6 y del mínimo del puerto son los de la tabla del §2: CITED / OPEN.
10. Candidata que pasa la puerta: ninguna. NO-GO de selección en la clase «discrepancia reticular firmada aplicada
    a los restos de PC».
11. L161.4 primero en el orden: ARGUED.
