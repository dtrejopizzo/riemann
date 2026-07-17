# Doc 166 — Teoría de deformación del espacio de métricas sobre el espacio de Krein de la forma de Weil: el funcional de incompatibilidad, el flujo de Gram y la ley de conservación del índice

**Programa:** Hipótesis de Riemann — Phase 54: dinámica del índice.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** CONSTRUCTOR. Mandato: tras Phases 49–53 (toda ruta que busca UN operador, UNA
métrica o UNA positividad termina preguntando "¿por qué la forma de Weil es positiva?" = RH), cambiar
de objeto: estudiar el **espacio completo de métricas** 𝕄 sobre el espacio de Krein (𝒦,Q) de la forma
de Weil, el **funcional de incompatibilidad** 𝔇 que mide el fallo de unitariedad simultánea de la
reflexión funcional J y del flujo de escala U_t (el GAP 164.D), y la **dinámica de deformación**
(el flujo de Gram) sobre 𝕄. Pregunta del director: *¿por qué toda deformación de la métrica candidata
es expulsada?* — convertirla en un teorema de estabilidad/conservación, no en una re-pregunta de
existencia.

**Contrato de etiquetado (regla absoluta).** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad aquí, prueba completa; externos con referencia
verificable. **[CONSTRUCCIÓN]** = objeto definido con precisión. **[PUENTE]** = conexión con estatus
honesto. **[GAP]/[GAP de literatura]** = declarado; jamás premisa de un teorema. **[DESEO]** =
declarado. PERMITIDO (y esperable) terminar en B/C/D. **NADA de numéricos/Python. Español. Honestidad
absoluta: una falsa victoria es peor que un fracaso.**

**Prerrequisitos leídos en fuente esta sesión:** Doc 164 (Stone invertido; J unitaria RH-libre pero en
ℤ/2, ciega a m; GAP 164.D: RH ⟺ la métrica de la reflexión = la métrica de la evolución). Memoria
Phase 26 (puente: κ=2m=neg.ind(Q)=neg.ind(H_C) en Pontryagin (𝒦,Q); ítems V.1–V.4 NO probados).
Memoria Phase 28 (segunda variación de Q en dirección b_j; DBN = gradiente de E_log; Conj. A.15:
Λ = max b_j²/2). Memoria Phase 37 (arquitectura RH = (m<∞) ∧ (m<∞ ⟹ m=0)). Memoria Phase 53/D165
(Stone NO da espectro real en Krein con κ>0; Bognár; Azizov–Iokhvidov).

---

## 0. Resumen ejecutivo y veredicto adelantado

> **VEREDICTO: B′ — el muro reaparece, pero NO donde el mandato temía.** La teoría se construye
> completa y es RH-libre (módulo las hipótesis del puente de Phase 26, declaradas): 𝕄 es un cono
> convexo abierto no vacío y contráctil SIN asumir RH (desenlace C excluido, §2); 𝔇 es convexo,
> Lipschitz y 1-homogéneo (§3); el flujo de Gram existe y converge (§4). El test anti-circularidad da
> un resultado NEGATIVO INESPERADO Y LIMPIO: **la segunda variación de 𝔇 NO es la forma de Weil** —
> es el operador L = ∫e^{−2|t|}A_t^*A_t dt + A_J^*A_J ≥ 0, manifiestamente semidefinido positivo y
> RH-libre (§5.1). La circularidad NO está en la curvatura (el Hessiano); está en otros tres lugares,
> ahora localizados con exactitud: (1) **la forma de Weil W es SIEMPRE un punto crítico del funcional
> extendido** — A_t(W)=0, A_J(W)=0 incondicionalmente — y RH es exactamente la afirmación de que ese
> punto crítico **está dentro del cono 𝕄** (W>0) en vez de fuera; la existencia del punto crítico es
> gratis, su PERTENENCIA al cono es RH (Teorema 166.10). (2) **κ es una ley de conservación exacta de
> toda deformación de métricas** (Teorema 166.9, por inercia de Sylvester): mientras G recorre 𝕄, el
> índice negativo del par (Q,G) está congelado en κ; solo puede saltar en la frontera ∂𝕄 (métricas
> degeneradas). Esto RESPONDE la pregunta del director: toda deformación es expulsada porque intenta
> cambiar una carga topológica conservada — la expulsión es conservación de inercia, no un accidente
> analítico. (3) El ínfimo de 𝔇 está acotado inferiormente por una función EXPLÍCITA de los ceros
> off-line: 𝔇(G) ≥ φ(|b_j|)·⟨Gv_j,v_j⟩ con φ(b)=2b(1−2b)^{(1−2b)/(2b)} ~ (2/e)b (Teorema 166.6), y
> el peso e^{−|t|} del funcional está **calibrado exactamente por la franja crítica** (φ(b)<∞ ⟺
> b<1/2, que es el teorema de Hadamard–de la Vallée Poussin). El flujo de Gram no se estanca: EXPULSA
> la métrica hacia ∂𝕄, aplastando exactamente las direcciones propias de los ceros off-line, con tasa
> espectral ℓ(b_j)=2b_j²+O(b_j⁴) — eco cuantitativo de la conjetura A.15 de Phase 28 (Λ = max b_j²/2).
> **Lo nuevo no-RH-equivalente:** la ley de conservación (166.9), la calibración franja↔peso (166.6),
> la tasa 2b² (166.13), y la reescritura estructural "RH ⟺ el ínfimo se alcanza" — isomorfa en FORMA
> a Rodgers–Tao Λ≥0 (RH como pertenencia a la frontera de un problema variacional, §4.4).
> **Lo RH-reescrito (declarado):** "∃G∈𝕄 con 𝔇(G)=0" ⟺ m=0 (Teorema 166.7) — eso es el GAP 164.D
> formalizado, no contenido nuevo. La herramienta de estabilidad que el mandato esperaba
> (Łojasiewicz–Simon) resulta INAPLICABLE por una buena razón: cuando m≥1 no hay punto crítico
> interior que estabilizar (Corolario 166.8); la herramienta que el muro pide es otra y queda
> nombrada: **teoría del salto de índice en la frontera de 𝕄** (degeneraciones singulares de métricas),
> dual exacto de la frontera Λ=0 de De Bruijn–Newman.

---

## 1. Marco e hipótesis declaradas

### 1.1 El escenario de fondo (RH-libre, con un GAP de no-degeneración)

Trabajo sobre un espacio vectorial complejo K con:

- **(H-W) La forma de Weil como forma acotada no degenerada.** Un producto interno hermitiano de
  fondo ⟨·,·⟩₀ (RH-libre: por ejemplo el L² de Haar del setting de Connes, o el L²(dτ) de la recta
  crítica — Doc 164 §2.2 verifica que existe sin ζ) que hace de K un espacio de Hilbert, y la forma
  de Weil Q(·,·), hermitiana, ⟨·,·⟩₀-acotada, representada por su **operador de Gram**
  W = W* ∈ B(K): Q(x,y) = ⟨Wx,y⟩₀, con W **acotadamente invertible**.
  [GAP 166.A] La forma de Weil sobre funciones test puede tener radical y W puede no ser invertible
  (0 en el espectro continuo); el enunciado limpio requiere pasar al cociente por el radical y
  completar. Es la maniobra estándar de la teoría (Bognár 1974, cap. I §11), pero la acotación
  inferior |W| ≥ ε NO está verificada para la forma de Weil concreta. Todo lo que sigue es la teoría
  sobre el modelo (K, ⟨·,·⟩₀, W) con W invertible; la transferencia al objeto aritmético hereda este
  GAP.

- **(H-Π) Régimen de Pontryagin: m < ∞.** El índice negativo de Q es κ = 2m < ∞ (Phase 26;
  convención del programa: m órbitas de Klein de ceros off-line ↦ κ=2m). Esto NO es gratis: la
  arquitectura de Phase 37 es RH = (m<∞) ∧ (m<∞ ⟹ m=0). **Este documento vive íntegramente en el
  segundo conyunto**: asumo m<∞ y estudio la deformación de métricas en Π_κ. Con κ<∞, (K,Q) es un
  espacio de Pontryagin y se aplica la teoría clásica (Pontryagin 1944; Iokhvidov–Krein 1956;
  Bognár 1974; Azizov–Iokhvidov 1989).

- **(H-26) El puente dinámico de Phase 26 (declarado, no probado).** Las dos simetrías de D164:
  (i) un grupo de un parámetro U_t ∈ B(K), **Q-unitario** (Q(U_tx,U_ty)=Q(x,y), equivalentemente
  U_t^*WU_t = W, con * el adjunto de fondo) — el flujo de escala —, y una involución J = J^{−1},
  **Q-unitaria y además ⟨·,·⟩₀-unitaria** (D164 Prop 164.6: la reflexión funcional es unitaria
  RH-libre), con la relación de reflexión J U_t J = U_{−t};
  (ii) para cada cero off-line ρ_j = (½+b_j) + iγ_j (j=1,…,m′, con m′ contando el cuádruple de Klein
  según la convención de Phase 26) un **autovector genuino** v_j ∈ K del grupo:
  U_t v_j = e^{itλ_j} v_j con λ_j = γ_j + i b_j, b_j ≠ 0 — esto es V.2 de Phase 26, NO probado
  (los caracteres x^{b+iγ} podrían ser solo autovectores generalizados/isotrópicos);
  (iii) cota de crecimiento ‖U_t‖₀ ≤ C(1+|t|)^d e^{b_max|t|} con b_max = max_j|b_j| < ½ — la forma
  cuantitativa de que U_t es π-unitario en Π_κ con espectro no-real confinado a la franja
  (Iokhvidov–Krein 1956: los π-unitarios son acotados; el crecimiento exponencial del grupo está
  gobernado por las partes imaginarias de los autovalores no-reales del generador, con factor
  polinómico por los bloques de Jordan en los subespacios raíz, de dimensión total finita ≤ 2κ).
  **Toda proposición que use (H-26) lo cita explícitamente.** Que b_max < ½ estrictamente para cada
  cero es incondicional: no hay ceros en Re s = 1 ni Re s = 0 (Hadamard 1896; de la Vallée Poussin
  1896), de modo que cada b_j ∈ (−½,½) — aunque sup b_j = ½ no está excluido si m=∞; bajo (H-Π) el
  máximo se alcanza y b_max < ½.

- **(H-26⁺) Concentración del índice (refuerzo, declarado).** El subespacio raíz N ⊂ K del espectro
  no-real del generador (dim N ≤ 2κ < ∞) es Q-no-degenerado (esto sí es teoría general: el subespacio
  raíz del espectro no-real de un operador π-autoadjunto es no-degenerado y los subespacios raíz de
  λ y λ̄ se aparean hiperbólicamente — Azizov–Iokhvidov 1989, cap. 2 §2; Krein–Langer 1973), TODO el
  índice negativo de Q vive en N, y Q es **uniformemente positiva** en el Q-ortocomplemento
  K₁ = N^{[⊥]}: Q|_{K₁} ≥ ε₁ > 0. [GAP 166.B] La concentración del índice en N no es automática
  (autovalores reales pueden portar autovectores negativos) y la uniformidad ε₁>0 es exactamente el
  GAP 166.A restringido a K₁. (H-26⁺) solo se usa en la Proposición 166.11 (colapso) y se marca.

### 1.2 Anti-circularidad del marco

⟨·,·⟩₀ es RH-libre (Haar/Lebesgue). W es la forma de Weil: objeto incondicional (la forma cuadrática
de la fórmula explícita), RH-libre como FORMA; lo que sería RH es su positividad, que NO se asume.
U_t y J son RH-libres como operadores (D164); lo condicional es (H-26)(ii) — que los ceros off-line
den autovectores en K — que es una hipótesis sobre el ESPACIO, no sobre RH (si m=0 la hipótesis es
vacua y todo el documento sigue en pie trivialmente). El marco pasa la guardia.

---

## 2. El espacio 𝕄 de métricas

### 2.1 [DEFINICIÓN-NUEVA 166.1 — el espacio de métricas y su frontera]

$$\mathbb{M} \;=\; \{\,G \in B(K) \;:\; G = G^{*},\ \exists\, \varepsilon>0:\ G \geq \varepsilon I\,\}$$

(operadores de Gram admisibles respecto del fondo; la métrica asociada es ⟨x,y⟩_G = ⟨Gx,y⟩₀, que es
un producto interno definido positivo con norma equivalente a la de fondo si además G es acotado —
ambas cosas en la definición). Dos subobjetos:

- **La frontera** ∂𝕄 = {G ≥ 0, G = G*, G no acotadamente invertible}: las **métricas degeneradas**
  (seminormas). No pertenecen a 𝕄; son los límites de sus sucesiones.
- **El subespacio Q-adaptado** 𝕄_Q = {G ∈ 𝕄 : G = WS para alguna involución S (S²=I) con WS > 0}
  — equivalentemente, las métricas de la forma ⟨x,y⟩_S = Q(Sx,y) con S una **simetría fundamental**
  del espacio de Krein (K,Q) (Bognár 1974, cap. IV; Azizov–Iokhvidov 1989, cap. 1 §3). Son las
  métricas "que leen a Q": en ellas Q se diagonaliza en bloque positivo ⊕ negativo.

### 2.2 [PROPOSICIÓN 166.2 — 𝕄 es no vacío, cono convexo abierto, contráctil; RH-libre]

**Enunciado.** Bajo (H-W) solamente (sin RH, sin (H-26)): (a) 𝕄 ≠ ∅ (contiene I). (b) 𝕄 es un cono
convexo abierto en el espacio de Banach real B_h(K) de los operadores ⟨·,·⟩₀-autoadjuntos acotados.
(c) 𝕄 es contráctil (de hecho, convexo). (d) En dimensión finita n, 𝕄 ≅ GL(n,ℂ)/U(n), el espacio
simétrico de las métricas; en general es la versión Banach de ese espacio homogéneo, con
GL(K)-acción transitiva G ↦ T*GT.

**Prueba.** (a) I ∈ 𝕄. (b) Si G₁ ≥ ε₁, G₂ ≥ ε₂, entonces sG₁+(1−s)G₂ ≥ min(ε₁,ε₂) > 0, y λG₁ ≥ λε₁
para λ>0: cono convexo. Abierto: si G ≥ ε y ‖H−G‖ < ε/2 con H autoadjunto, entonces H ≥ ε/2. (c)
Convexo ⟹ contráctil. (d) Transitividad: dados G₁,G₂ ∈ 𝕄, T = G₁^{−1/2}G₂^{1/2} cumple T*G₁T = G₂
(cálculo directo con raíces cuadradas positivas, funcional continuo); el estabilizador de I es
{T: T*T = I} = el grupo unitario de fondo. En dimensión finita esto es la identificación clásica del
cono de matrices definidas positivas con GL(n,ℂ)/U(n). ∎

### 2.3 [PROPOSICIÓN 166.3 — 𝕄_Q es no vacío y contráctil sin RH: la parametrización de Krein por operadores de ángulo]

**Enunciado.** Bajo (H-W) y (H-Π) (κ<∞), sin RH: (a) 𝕄_Q ≠ ∅. (b) 𝕄_Q está en biyección con el
conjunto de subespacios κ-dimensionales Q-negativos-definidos máximos, y éste con la bola abierta de
contracciones estrictas {T ∈ B(K₋⁰, K₊⁰) : ‖T‖ < 1}, donde K = K₊⁰ ⊕ K₋⁰ es una descomposición
fundamental de referencia (dim K₋⁰ = κ). En particular 𝕄_Q es no vacío, conexo y contráctil. (c)
Todas las métricas de 𝕄_Q inducen normas equivalentes (entre sí y con la de fondo). (d) **Ninguna
G ∈ 𝕄_Q hace positiva a Q**: en toda descomposición fundamental la parte negativa tiene dimensión
exactamente κ.

**Prueba.** (a) W = W* invertible; descomposición espectral W = W₊ − W₋ con W± ≥ 0 de rangos
espectrales complementarios; S₀ := sign(W) (cálculo funcional boreliano sobre el espectro de W, que
no contiene 0) cumple S₀² = I y WS₀ = |W| ≥ ε > 0; luego G₀ = WS₀ ∈ 𝕄_Q. Esto usa solo (H-W). Bajo
(H-Π), dim ran(proyector espectral negativo) = κ. (b) Es la teoría clásica del operador de ángulo:
toda descomposición fundamental K = K₊ [+] K₋ está determinada por su parte negativa K₋ (la positiva
es el Q-ortocomplemento), K₋ es Q-negativo-definido máximo de dimensión κ (Pontryagin 1944:
en Π_κ todo subespacio no-positivo máximo tiene dimensión κ), y K₋ = {x + Tx : x ∈ K₋⁰} para una
única T: K₋⁰ → K₊⁰ con Q(x+Tx, x+Tx) = ‖Tx‖²_+ − ‖x‖²_- < 0 para x ≠ 0, lo que en dimensión finita
de K₋⁰ equivale a ‖T‖ < 1 (compacidad de la esfera de K₋⁰). Recíprocamente toda contracción estricta
da una parte negativa máxima. (Azizov–Iokhvidov 1989, cap. 1 §8; Bognár 1974, cap. V.) La bola
{‖T‖<1} es convexa, luego contráctil. (c) Equivalencia de normas entre simetrías fundamentales:
Bognár 1974, cap. IV, Thm 6.4 (en Π_κ, consecuencia de la dimensión finita del defecto). (d) Ley de
inercia en Π_κ (Pontryagin 1944): κ es invariante de la forma, no de la descomposición. ∎

**Interpretación.** **El desenlace C queda excluido**: el espacio de métricas NO colapsa sin RH — es
enorme (un cono convexo de dimensión infinita) y hasta su parte Q-adaptada es una bola de
contracciones no vacía y contráctil. Lo que no existe sin RH no es "métricas" sino *una métrica
compatible con la dinámica* — eso es §3. Y (d) ya anuncia la ley de conservación: ninguna deformación
de la métrica mueve κ.

### 2.4 [OBSERVACIÓN 166.4 — el escape de Haar y por qué no trivializa el problema]

Sobre el espacio GRANDE L²(ℝ₊*, d*λ), tanto U_t (dilataciones) como J (inversión v↦1/v, pues d*λ es
inversión-invariante) son unitarios respecto de la métrica de Haar: allí 𝔇 = 0 con métrica RH-libre.
NO contradice nada de lo que sigue: en ese espacio el generador tiene espectro ℝ continuo y NINGÚN
autovector con autovalor no-real — es el flujo ciego a ζ de D164 §2.2(i). La teoría de este documento
vive en K = el espacio del puente de Phase 26, donde (H-26)(ii) pone los ceros off-line como
autovalores. **La incompatibilidad métrica nace exactamente al pasar del espacio ciego al espacio
aritmético**; el funcional 𝔇 mide el costo de ese paso.

---

## 3. El funcional de incompatibilidad 𝔇

### 3.1 [DEFINICIÓN-NUEVA 166.5 — los defectos y el funcional]

Para G ∈ B_h(K) defino los **operadores de defecto** (lineales en G):

$$A_t(G) \;=\; U_t^{*} G\, U_t - G \qquad (t\in\mathbb{R}), \qquad A_J(G) \;=\; J^{*} G\, J - G,$$

y el **funcional de incompatibilidad**

$$\boxed{\;\mathfrak{D}(G) \;=\; \sup_{t\in\mathbb{R}} e^{-|t|}\,\bigl\|A_t(G)\bigr\|_0 \;+\; \bigl\|A_J(G)\bigr\|_0\;}$$

Significado: A_t(G) = 0 ∀t ⟺ U_t es G-unitario; A_J(G) = 0 ⟺ J es G-unitario. 𝔇(G) = 0 ⟺ G es la
métrica común del GAP 164.D. El peso e^{−|t|} se justificará en el Teorema 166.6: está calibrado por
la franja crítica.

**[PROPOSICIÓN 166.5′ — propiedades estructurales].** Bajo (H-26)(i),(iii):
(a) 𝔇 está bien definido (finito) en B_h(K) y es Lipschitz: 𝔇(G) ≤ c_U‖G‖ con
c_U = sup_t e^{−|t|}(1+‖U_t‖₀²) + (1+‖J‖₀²) < ∞ (finito porque 2b_max < 1 por (H-26)(iii)).
(b) 𝔇 es **convexo** y positivamente 1-homogéneo.
(c) 𝔇 es invariante bajo la involución isométrica σ(G) = J^*GJ, y **el término J es gratuito**: para
todo G ∈ 𝕄, el promedio G′ = ½(G + σG) ∈ 𝕄 cumple A_J(G′) = 0 y 𝔇(G′) ≤ 𝔇(G). Por tanto
inf_𝕄 𝔇 = inf{ sup_t e^{−|t|}‖A_t(G)‖ : G ∈ 𝕄, J^*GJ = G }.

**Prueba.** (a) ‖A_t(G)‖ ≤ (‖U_t‖₀²+1)‖G‖ y e^{−|t|}‖U_t‖₀² ≤ C²(1+|t|)^{2d}e^{(2b_max−1)|t|} → 0;
sup finito. La diferencia |𝔇(G)−𝔇(H)| ≤ c_U‖G−H‖ por desigualdad triangular en cada término.
(b) G ↦ A_t(G) y G ↦ A_J(G) son lineales; la norma es convexa; el supremo de convexas es convexo; la
suma preserva. Homogeneidad evidente. (c) J es ⟨·,·⟩₀-unitaria e involutiva ((H-26)(i)), luego σ es
una involución lineal isométrica de B_h(K) que preserva 𝕄. Con JU_t = U_{−t}J:
U_t^*J^*GJU_t = (JU_t)^*G(JU_t) = (U_{−t}J)^*G(U_{−t}J) = J^*A_{−t}(G)J + J^*GJ, de donde
A_t(σG) = J^*A_{−t}(G)J y ‖A_t(σG)‖ = ‖A_{−t}(G)‖; como el peso es par en t, el primer término de 𝔇
es σ-invariante; además A_J(σG) = J^*(J^*GJ)J − J^*GJ = G − J^*GJ = −J^*A_J(G)J... directamente
‖A_J(σG)‖ = ‖A_J(G)‖. Luego 𝔇∘σ = 𝔇. Para el promedio: A_J(G′) = ½(A_J(G) + A_J(σG)) =
½(J^*GJ − G + G − J^*GJ) = 0, y 𝔇(G′) ≤ ½𝔇(G) + ½𝔇(σG) = 𝔇(G) por convexidad e invariancia. ∎

**Interpretación de (c).** Reencuentra cuantitativamente a D164: la reflexión funcional es la
simetría BARATA (su compatibilidad se consigue gratis promediando); todo el costo de 𝔇 está en el
flujo de escala. El GAP 164.D se concentra, sin pérdida, en el término dinámico.

### 3.2 [TEOREMA 166.6 — cota inferior universal: la incompatibilidad ve cada cero off-line, con peso calibrado por la franja]

**Enunciado.** Bajo (H-26). Sea G ∈ 𝕄 y sea v_j el autovector de un cero off-line con b_j ≠ 0.
Entonces

$$\mathfrak{D}(G) \;\geq\; \varphi(|b_j|)\,\frac{\langle G v_j, v_j\rangle_0}{\|v_j\|_0^2}, \qquad
\varphi(b) := \sup_{t>0} e^{-t}\bigl(e^{2bt}-1\bigr) \;=\; 2b\,(1-2b)^{\frac{1-2b}{2b}},$$

donde φ: (0,½) → (0,1) es estrictamente creciente, φ(b) = (2/e)\,b\,(1+O(b)) cuando b→0⁺,
φ(b) → 1 cuando b→½⁻, **y φ(b) = +∞ si b ≥ ½**. Consecuencias:

(i) (calibración) El peso e^{−|t|} es exactamente el peso más débil que mantiene 𝔇 finito sobre los
grupos π-unitarios cuyo espectro no-real está en la franja crítica: la finitud de 𝔇 usa b_max < ½,
es decir, el teorema de Hadamard–de la Vallée Poussin. La franja crítica ES la región de
integrabilidad del funcional.

(ii) (positividad puntual) Si m ≥ 1, entonces 𝔇(G) > 0 para TODO G ∈ 𝕄: **el funcional no tiene
ceros en el interior del cono**.

(iii) (cota normalizada) inf{𝔇(G) : G ∈ 𝕄, G ≥ I} ≥ φ(b_max) > 0 si m ≥ 1.

**Prueba.** Sea λ_j = γ_j + ib_j, U_t v_j = e^{itλ_j}v_j, |e^{itλ_j}|² = e^{−2b_jt}. Entonces

⟨A_t(G)v_j, v_j⟩₀ = ⟨G U_t v_j, U_t v_j⟩₀ − ⟨Gv_j,v_j⟩₀ = (e^{−2b_j t} − 1)⟨Gv_j,v_j⟩₀.

Eligiendo el signo de t con b_j t < 0 (ambos signos disponibles en el supremo), el factor es
e^{2|b_j||t|} − 1 > 0, y como ‖A_t(G)‖₀ ≥ |⟨A_t(G)v_j,v_j⟩₀|/‖v_j‖₀²,

𝔇(G) ≥ sup_{s>0} e^{−s}(e^{2|b_j|s} − 1)·⟨Gv_j,v_j⟩₀/‖v_j‖₀².

Cálculo de φ: g(s) = e^{(2b−1)s} − e^{−s} con 0<b<½; g(0)=0, g(∞)=0, g′(s) = (2b−1)e^{(2b−1)s} +
e^{−s} = 0 ⟺ e^{−2bs} = 1−2b ⟺ s_* = −log(1−2b)/(2b); valor
φ(b) = e^{−s_*}(e^{2bs_*}−1) = (1−2b)^{1/(2b)}·\frac{2b}{1−2b} = 2b(1−2b)^{(1−2b)/(2b)}.
Monotonía: el integrando e^{−s}(e^{2bs}−1) es creciente en b para cada s>0, luego el sup lo es.
Asintóticas: (1−2b)^{1/(2b)} → e^{−1} (b→0) da φ ~ 2b/e; en b→½⁻ el exponente (1−2b)/(2b) → 0 da
φ → 2·½·1 = 1. Si b ≥ ½, g(s) no decae y el sup es ∞ — de ahí (i): para un grupo con autovalor a
distancia ≥ ½ de ℝ el funcional con peso e^{−|t|} diverge sobre TODA G (misma identidad con
⟨Gv,v⟩ > 0); que esto no ocurre es exactamente b_j < ½ para todo cero, i.e. la no-anulación en
Re s = 1. (ii): G ≥ εI con ε>0 dependiente de G da ⟨Gv_j,v_j⟩₀ ≥ ε‖v_j‖₀² > 0, luego
𝔇(G) ≥ εφ(|b_j|) > 0. (iii): con ε = 1 uniforme, 𝔇(G) ≥ max_j φ(|b_j|) = φ(b_max). ∎

### 3.3 [TEOREMA 166.7 — el cero de 𝔇 es RH reescrita (la parte honesta-declarada)]

**Enunciado.** Bajo (H-26): existe G ∈ 𝕄 con 𝔇(G) = 0 ⟹ m = 0. Recíprocamente, si m = 0 Y la forma
de Weil es uniformemente positiva (W ≥ ε, el GAP 166.A), entonces G = W ∈ 𝕄 y 𝔇(W) = 0. En suma,
módulo (H-26) y el GAP de uniformidad: **∃G ∈ 𝕄: 𝔇(G)=0 ⟺ RH.** Este enunciado es el GAP 164.D
formalizado; se declara como RH-reescrito, sin contenido nuevo. El contenido nuevo del documento está
en la geometría alrededor (166.6, 166.9, 166.10, 166.12, 166.13).

**Prueba.** (⟹) Contrapositivo de 166.6(ii). (⟸) U_t es Q-unitario ((H-26)(i)) ⟺ U_t^*WU_t = W ⟺
A_t(W) = 0 ∀t; J Q-unitaria da A_J(W) = 0. Si W ≥ ε entonces W ∈ 𝕄 y 𝔇(W) = 0. ∎

**[PROPOSICIÓN 166.7′ — lectura Pontryagin–Stone en 𝕄_Q: compatibilidad = descomposición invariante].**
Bajo (H-26), si G = WS ∈ 𝕄_Q y sup_t‖A_t(G)‖ = 0, entonces [S, U_t] = 0 ∀t, la descomposición
fundamental K = K₊ [+] K₋ asociada a S es U_t-invariante, y U_t se parte en dos grupos unitarios
genuinos: sobre (K₊, Q) y sobre (K₋, −Q), ambos espacios de Hilbert (el segundo de dimensión κ<∞).
Por Stone (en K₋, dimensión finita: álgebra lineal) ambos generadores tienen espectro real; luego no
existe el autovector v_j de (H-26)(ii) con b_j ≠ 0, i.e. m = 0.
**Prueba.** A_t(WS) = U_t^*WSU_t − WS = W(U_t^{−1}SU_t − S) usando U_t^*W = WU_t^{−1} (de
U_t^*WU_t = W y W invertible); como W es invertible, A_t(WS) = 0 ⟺ U_t^{−1}SU_t = S ⟺ [S,U_t]=0.
Entonces los autoespacios K_± = ker(S ∓ I) son U_t-invariantes; sobre K₊ la forma Q es el producto
interno ⟨·,·⟩_S restringido (positivo, completo: Bognár 1974 cap. V) y U_t lo preserva (Q-unitario +
invariancia) ⟹ grupo unitario ⟹ generador autoadjunto ⟹ espectro real (Stone 1932; Reed–Simon I
Thm VIII.8); sobre K₋, −Q es un producto interno en dimensión κ y lo mismo vale por álgebra lineal.
Un autovector con autovalor no-real tendría componentes en K₊ o K₋ que serían autovectores no-reales
de grupos unitarios: imposible. ∎

**Interpretación.** El mecanismo del muro en lenguaje de deformación: *compatibilidad métrica =
existencia de una descomposición fundamental invariante bajo el flujo* — y eso particiona el flujo en
dos bloques unitarios con espectro real. Es la versión métrica del teorema de D165 ("Stone no da
espectro real en Krein con κ>0"): aquí se ve POR QUÉ — el flujo con espectro no-real no deja
invariante ninguna parte negativa máxima definida (deja invariantes subespacios no-positivos máximos
— Pontryagin 1944 — pero ésos son isotrópicos en las direcciones raíz, no definidos, y no inducen
métrica).

### 3.4 [COROLARIO 166.8 — cuando m ≥ 1 no hay punto crítico interior: Łojasiewicz–Simon no aplica, por una buena razón]

Si m ≥ 1, por 166.6(ii) el funcional convexo 𝔇 es estrictamente positivo en todo 𝕄; como además es
1-homogéneo, no tiene mínimos locales interiores no triviales (un mínimo local de una función convexa
es global; el valor global con la normalización G ≥ I está ≥ φ(b_max) y no se alcanza en general —
§3.5). **La herramienta que el mandato proponía importar (Łojasiewicz 1963; Simon 1983) presupone un
punto crítico al que estabilizarse; aquí, en el caso m ≥ 1, no existe NINGÚN punto crítico interior.**
El problema no es de estabilidad de un equilibrio: es de comportamiento de frontera. (Bajo m=0 +
uniformidad sí hay mínimo W, y por convexidad cuadrática del sustituto liso §4 la desigualdad de
Łojasiewicz vale trivialmente con exponente ½ — pero entonces RH ya está dada; la herramienta llega
tarde en ambos escenarios.)

### 3.5 [PROPOSICIÓN 166.11 — el colapso dirigido: el ínfimo normalizado es 0 y no se alcanza; RH ⟺ se alcanza]

**Enunciado.** Bajo (H-26) y (H-26⁺). Con la normalización ‖G‖₀ = 1 (en lugar de G ≥ I):

(a) inf{𝔇(G) : G ∈ 𝕄, ‖G‖₀ = 1} = 0 **aunque m ≥ 1**, realizado por sucesiones G_δ que degeneran
exactamente sobre N (el subespacio raíz de los ceros off-line): G_δ = δ·g_N ⊕ W₁ con
𝔇(G_δ) ≤ Cδ → 0, donde W₁ = Gram de Q|_{K₁} y g_N cualquier métrica J-invariante sobre N.

(b) Toda sucesión minimizante aplasta los autovectores off-line: 𝔇(G_n) → 0 ⟹
⟨G_n v_j, v_j⟩₀ → 0 para todo j, con tasa ⟨G_nv_j,v_j⟩₀ ≤ 𝔇(G_n)‖v_j‖₀²/φ(|b_j|).

(c) El ínfimo SE ALCANZA en 𝕄 ⟺ m = 0 (módulo el GAP de uniformidad de 166.7).

**Prueba.** (a) Bajo (H-26⁺), K = N [+]_Q K₁ con ambos sumandos U_t- y J-invariantes (N es suma de
subespacios raíz del espectro no-real: invariante por el grupo y por J pues J conjuga el espectro
γ↦−γ permutando esos subespacios raíz; K₁ es su Q-ortocomplemento, invariante porque U_t y J son
Q-unitarios). Elijo el producto de fondo de modo que la suma sea ⟨·,·⟩₀-ortogonal (lícito: normas
equivalentes, dim N < ∞). Entonces todo es diagonal por bloques: A_t(G_δ) = δ·A_t^N(g_N) ⊕ A_t^1(W₁).
El segundo bloque es 0: U_t|_{K₁} es Q₁-unitario y W₁ es el Gram de Q₁ (positivo ≥ ε₁ por (H-26⁺),
luego G_δ ∈ 𝕄 para todo δ>0). El primero: ‖A_t^N(g_N)‖ ≤ ‖g_N‖(1+‖U_t|_N‖²) ≤ C(1+|t|)^{2d}
e^{2b_max|t|}, y con el peso, sup_t e^{−|t|}δ(⋯) ≤ C′δ porque 2b_max<1. El término J se anula
promediando g_N bajo J|_N (Prop. 166.5′(c), en dimensión finita el promedio es métrica). ‖G_δ‖₀ ≈
‖W₁‖ se renormaliza a 1 sin tocar los órdenes. Luego 𝔇(G_δ) ≤ C′δ → 0. (b) Inmediato de 166.6.
(c) (⟸) 166.7. (⟹) Si G ∈ 𝕄 alcanza el ínfimo 0, 166.6(ii) fuerza m = 0. ∎

**Interpretación (el resultado estructural del documento, junto con 166.9).** El problema variacional
tiene la estructura **"ínfimo cero, alcance ⟺ RH"**: el valor crítico es alcanzable solo en la
frontera ∂𝕄 (métricas degeneradas cuyo núcleo es exactamente N). Las sucesiones minimizantes no
eligen cualquier degeneración: **aplastan exactamente las direcciones de los ceros off-line** — la
dinámica de optimización intenta EXPULSAR del espacio a los vectores que portan κ, cociente
K → K/N mediante. El modo de fallo que el mandato predijo ("el único punto crítico es la métrica
espectral construida de los ceros") se confirma pero con la geometría precisa: el objeto límite es la
métrica de Weil sobre la parte positiva K₁, degenerada sobre N — y ahora ese objeto está
caracterizado como **atractor de frontera de una dinámica RH-libre**, no como una elección.

---

## 4. El flujo de Gram y la ley de conservación del índice

### 4.1 [TEOREMA 166.9 — κ es una ley de conservación exacta de TODA deformación de métricas]

**Enunciado.** Bajo (H-W) y (H-Π), sin RH y sin (H-26). Para G ∈ 𝕄 defino el **índice visible**
κ(G) := dimensión del subespacio espectral negativo de G^{−1/2} W G^{−1/2} (el operador de Gram de Q
en la geometría de G). Entonces:

$$\kappa(G) \;=\; \kappa \qquad \text{para TODO } G \in \mathbb{M}.$$

En particular κ(G(s)) es constante a lo largo de cualquier curva (continua, ni siquiera hace falta)
en 𝕄 — bajo el flujo de Gram, bajo cualquier flujo. **El índice negativo no es deformable por
métricas: es una carga topológica del par (Q, 𝕄), y solo puede saltar en ∂𝕄.**

**Prueba.** T := G^{−1/2} es invertible; G^{−1/2}WG^{−1/2} = T^*WT es congruente a W. La inercia es
invariante por congruencia: si M ⊂ K es un subespacio sobre el que ⟨T^*WTx,x⟩₀ < 0 (x≠0), entonces
T(M) es un subespacio de la misma dimensión sobre el que ⟨Wy,y⟩₀ < 0, y viceversa con T^{−1}; tomar
supremos de dimensiones da n_−(T^*WT) = n_−(W) = κ (ley de inercia de Sylvester; en Π_κ, Pontryagin
1944 / Bognár 1974 cap. IV: todas las partes negativas máximas tienen dimensión κ). En ∂𝕄 el
argumento muere exactamente donde debe: T = G^{−1/2} deja de ser acotado/invertible y la congruencia
deja de ser un isomorfismo — los autovalores de G^{−1/2}WG^{−1/2} pueden alcanzar 0 y cruzar. ∎

**Interpretación — la respuesta a la pregunta del director.** *"¿Por qué toda deformación de la
métrica candidata es expulsada?"* Respuesta probada: porque el defecto que la deformación intenta
eliminar (κ > 0 visible en la incompatibilidad 𝔇 > 0, Teorema 166.6) es una **cantidad conservada**
de la deformación de métricas. No es que el punto bueno sea inestable o esquivo: es que la clase de
deformaciones permitidas (G ∈ 𝕄, Q fija) conserva exactamente la obstrucción. La expulsión es
conservación de inercia. Esto además DEMUESTRA un no-go nuevo y útil: **ningún esquema que deforme
solo la métrica (con la forma de Weil fija) puede reducir κ** — la única salida es por la frontera
(degenerar la métrica = cocientar el espacio) o moviendo la FORMA (el flujo de De Bruijn–Newman).

### 4.2 [PUENTE 166-DBN — dualidad exacta con el flujo de De Bruijn–Newman]

| | flujo DBN (función) | flujo de Gram (métrica) |
|---|---|---|
| variable dinámica | la forma: W_t (Gram de la forma de Weil de H_t, el calor sobre Ξ) | la métrica: G(s), con W FIJA |
| qué está congelado | la métrica ambiente (DBN es ciego a la métrica) | la forma de Weil W |
| índice κ | puede BAJAR: la realidad de los ceros es monótona en t (de Bruijn 1950, Thm 13: si H_{t₀} tiene solo ceros reales, H_t también para t ≥ t₀); κ(t) no-creciente en el sentido del conteo de pares no-reales | CONSERVADO exactamente (Teorema 166.9) |
| RH como frontera | RH ⟺ Λ = 0: Λ ≤ 0 (def. de Λ, Newman 1976) y Λ ≥ 0 (Rodgers–Tao 2020) — "RH apenas verdadera", el punto aritmético está EN la frontera | RH ⟺ el ínfimo de 𝔇 (que es 0) SE ALCANZA — el minimizador está EN la frontera ∂𝕄 (166.11) |
| mecanismo de cruce | el calor empuja los ceros a la recta (colisiones en t>Λ) | la degeneración aplasta N y cocienta los ceros off-line fuera del espacio |

**Estatus honesto.** La fila "κ(t) no-creciente" del lado DBN es la traducción del teorema de
monotonía de de Bruijn al lenguaje de índices vía el puente de Phase 26, que NO está probado
([PUENTE], no teorema; la igualdad fina conjetural es A.15 de Phase 28: Λ = max b_j²/2). La
estructura dual es nítida: **DBN mueve la forma con métrica congelada y el índice puede caer; Gram
mueve la métrica con forma congelada y el índice no puede caer.** La variable dinámica de uno es la
cantidad conservada del otro. Ambos colocan a RH en la FRONTERA de su espacio de deformación. Si
existe un flujo acoplado (W_t, G_s) que intercambie las dos frontera, no lo sé: [DESEO 166.C].

### 4.3 [CONSTRUCCIÓN 166.12 — el flujo de Gram; sustituto liso]

El funcional 𝔇 es convexo pero no diferenciable (normas, supremo). Para la dinámica uso el
**sustituto liso cuadrático**

$$\mathfrak{D}_2(G) \;=\; \tfrac12\int_{\mathbb{R}} e^{-2|t|}\,\|A_t(G)\|_{HS}^2\,dt \;+\; \tfrac12\|A_J(G)\|_{HS}^2,$$

con ‖·‖_{HS} la norma Hilbert–Schmidt. [GAP 166.D] En dimensión infinita ‖A_t(G)‖_{HS} puede ser
infinita para G genérico; la teoría del flujo se establece con prueba completa en el **modelo
finito-dimensional** (K_fin, Q_fin, U_t, J) — en particular en el bloque N ⊕ (trozo finito de K₁),
que es donde vive toda la obstrucción — y se enuncia como formal en general. En el modelo:

𝔇₂ es una forma cuadrática ≥ 0 en el espacio real H_h := {G hermitiana} con el producto HS:
𝔇₂(G) = ½⟨LG, G⟩_{HS}, donde

$$L \;=\; \int_{\mathbb{R}} e^{-2|t|} A_t^{*}A_t\,dt + A_J^{*}A_J \;\geq\; 0,
\qquad A_t^{*}(M) = U_t M U_t^{*} - M,$$

(el adjunto HS de A_t; cálculo directo: ⟨A_t(G),M⟩_{HS} = ⟨G, A_t^*(M)⟩_{HS}). El **flujo de Gram** es
el flujo de gradiente

$$\dot G \;=\; -\nabla \mathfrak{D}_2(G) \;=\; -LG, \qquad G(0)=G_0\in\mathbb{M},$$

que es **lineal**: G(s) = e^{−sL}G₀. (Para el 𝔇 no liso, el flujo de subgradiente de una convexa
existe y es contractivo — Brezis 1973 — pero el lineal basta para extraer toda la estructura.)

### 4.4 [TEOREMA 166.13 — dinámica del flujo de Gram en el modelo: el punto crítico universal es W; el flujo expulsa hacia la frontera; tasa 2b²]

**Enunciado.** En el modelo finito-dimensional, bajo (H-26) restringida al modelo:

(a) **(El punto crítico universal es la forma de Weil.)** ker L = {G hermitiana : A_t(G)=0 ∀t,
A_J(G)=0}, y **W ∈ ker L incondicionalmente** (sin RH). El conjunto de puntos fijos del flujo
contiene siempre a la forma de Weil — como FORMA hermitiana, no necesariamente como métrica.

(b) **(Estructura de ker L: solo apareamientos λ↔λ̄.)** Si el generador es semisimple con
autovectores {v_μ} formando base ⟨·,·⟩₀-ortonormal (modelo normal), entonces G ∈ ker L ⟺
⟨Gv_μ, v_ν⟩ = 0 salvo λ_μ = λ̄_ν. En particular, todo G ∈ ker L cumple ⟨Gv_j, v_j⟩ = 0 sobre cada
autovector off-line (b_j ≠ 0): los elementos de ker L son "hiperbólicos" sobre N, exactamente como W.

(c) **(Expulsión.)** Si m ≥ 1, **ningún elemento de ker L es definido positivo** (G ∈ ker L, G ≥ 0 ⟹
Gv_j = 0, propagado por las cadenas de Jordan ⟹ G se anula sobre N). El flujo G(s) = e^{−sL}G₀
converge a G_∞ = P_{ker L}G₀, que o bien es degenerado (∈ ∂𝕄 con núcleo ⊇ N si G_∞ ≥ 0) o bien es
indefinido — en cuyo caso el flujo ABANDONA el cono 𝕄 en tiempo finito. En cualquiera de los dos
casos: **el flujo de Gram expulsa toda métrica inicial hacia (o a través de) la frontera ∂𝕄**, en
consistencia exacta con la conservación de κ (166.9): dentro de 𝕄 el defecto no puede anularse,
así que el descenso de gradiente solo puede salir.

(d) **(Tasa de expulsión = 2b².)** En el modelo normal, la dirección diagonal E_j = ⟨·,v_j⟩₀v_j de un
cero off-line es autovector de L con autovalor exacto

$$\ell(b_j) \;=\; \frac{1}{1-4b_j^2} \;-\; \frac{2}{1-b_j^2} \;+\; 1 \;=\; 2b_j^2 + O(b_j^4),$$

creciente en |b_j| y divergente cuando |b_j| → ½. El flujo aplasta la dirección del cero off-line j a
ritmo exponencial e^{−ℓ(b_j)s}.

**Prueba.** (a) ⟨LG,G⟩ = 2𝔇₂(G) = ∫e^{−2|t|}‖A_t(G)‖²dt + ‖A_J(G)‖²; como L ≥ 0, LG = 0 ⟺
⟨LG,G⟩=0 ⟺ A_t(G)=0 para casi todo t — y por continuidad en t, para todo t — y A_J(G)=0. W: la
Q-unitariedad de U_t y J ((H-26)(i)) es A_t(W)=0, A_J(W)=0. (b) Para G con A_t(G)=0:
⟨Gv_μ,v_ν⟩ = ⟨GU_tv_μ, U_tv_ν⟩ = e^{it(λ_μ−\bar\lambda_ν)}⟨Gv_μ,v_ν⟩ para todo t, luego o
⟨Gv_μ,v_ν⟩=0 o λ_μ = λ̄_ν. Diagonal μ=ν con λ_μ no-real: λ_μ ≠ λ̄_μ fuerza ⟨Gv_μ,v_μ⟩=0.
(c) Si G ∈ ker L y G ≥ 0: ⟨Gv_j,v_j⟩=0 y Cauchy–Schwarz para formas semidefinidas dan Gv_j = 0. Si
w es vector de Jordan con (H−λ_j)w = v_j (caso no semisimple), U_tw = e^{itλ_j}(w + it v_j) y
⟨GU_tw,U_tw⟩ = e^{−2b_jt}(⟨Gw,w⟩ + 2Re(it̄⟨Gv_j,w⟩) + |t|²⟨Gv_j,v_j⟩) = e^{−2b_jt}⟨Gw,w⟩ (usando
Gv_j=0); la constancia en t fuerza ⟨Gw,w⟩=0 ⟹ Gw=0; inducción sobre la cadena: G|_N = 0. Entonces:
G_∞ = lim e^{−sL}G₀ = P_{ker L}G₀ (descomposición espectral de L ≥ 0 en dimensión finita; la
componente en (ker L)^⊥ decae como e^{−s·gap}). G_∞ ∈ ker L; G_∞ es hermitiana, límite de... el flujo
lineal NO preserva el cono en general, y ése es el contenido: si G_∞ ≥ 0, por lo anterior
ker G_∞ ⊇ N ≠ 0 y G_∞ ∈ ∂𝕄; si G_∞ no es ≥ 0, por continuidad de los autovalores existe s_* < ∞ con
λ_min(G(s_*)) = 0: el flujo cruza ∂𝕄 en tiempo finito. En ambos casos la trayectoria no permanece en
𝕄 con 𝔇₂ → 0: consistente con 166.6(ii) (no hay ceros interiores) y 166.9 (κ congelado en el
interior). (d) En el modelo normal U_t^*v_j = e^{i t \bar\lambda_j}... con base ortonormal de
autovectores, U_t es diagonal, U_t^* también, y A_t actúa diagonalmente sobre las unidades matriciales
E_{μν}: A_t(E_{μν}) = (e^{it(\bar\lambda_μ−λ_ν)}... cálculo sobre la diagonal E_j := E_{jj}:
U_t^*E_jU_t = |e^{itλ_j}|²E_j = e^{−2b_jt}E_j, luego A_t(E_j) = (e^{−2b_jt}−1)E_j y A_t^*A_t(E_j) =
(e^{−2b_jt}−1)²E_j. El término J permuta E_j con la unidad del autovector reflejado y se anula sobre
el promedio J-simétrico; sobre la componente relevante el autovalor de L es

ℓ(b) = ∫_ℝ e^{−2|t|}(e^{−2bt}−1)² dt = ∫₀^∞ e^{−2t}(e^{2bt}−1)²dt + ∫₀^∞ e^{−2t}(e^{−2bt}−1)²dt.

Primera integral: ∫₀^∞ e^{−2t}(e^{4bt}−2e^{2bt}+1)dt = 1/(2−4b) − 2/(2−2b) + ½; segunda con b↦−b.
Suma: [1/(2−4b)+1/(2+4b)] − 2[1/(2−2b)+1/(2+2b)] + 1 = 1/(1−4b²) − 2/(1−b²) + 1. Taylor:
(1+4b²) − 2(1+b²) + 1 + O(b⁴) = 2b² + O(b⁴). Polo en b=½: divergencia, coherente con 166.6(i). ∎

**Interpretación.** (a)+(c) es la imagen completa del muro en esta teoría: **el punto fijo del flujo
de Gram existe SIEMPRE y es canónico — es la forma de Weil W. RH no es la existencia del punto
crítico: es su pertenencia al cono de las métricas (W > 0).** El flujo RH-libre lo encuentra (converge
a la parte de G₀ apareada como W), pero si m ≥ 1 lo encuentra FUERA del cono, y la trayectoria
atraviesa ∂𝕄. (d) cuantifica: cada cero off-line es aplastado a tasa 2b_j² — la misma escala
cuadrática b² de la energía DBN (Phase 28, Conj. A.15: Λ = max b_j²/2). **[PUENTE 166-E, honesto]:**
la coincidencia de escala 2b_j² ↔ b_j²/2 es un eco estructural (ambas son la primera potencia par
permitida por la simetría γ↦−γ), no una identidad probada; el factor 4 de discrepancia no está
explicado. Queda como dato para el [DESEO 166.C] (flujo acoplado).

---

## 5. El test anti-circularidad: ¿la segunda variación es Q?

### 5.1 [TEOREMA 166.10 — la segunda variación NO es la forma de Weil; la circularidad está localizada en otra parte]

**Enunciado.** (a) El Hessiano de 𝔇₂ en CUALQUIER punto G (en particular en el candidato crítico) es
el operador constante L = ∫e^{−2|t|}A_t^*A_t dt + A_J^*A_J ≥ 0: una forma cuadrática semidefinida
positiva, RH-libre, definida solo por la dinámica (U_t, J) y el peso. **No es Q.** No hay ninguna
identificación "segunda variación de 𝔇 = forma de Weil": la respuesta a la pregunta 4 del mandato es
NO. (b) La forma de Weil aparece en la teoría exactamente en tres lugares, todos distintos del
Hessiano: (1) como punto fijo universal del flujo (166.13(a): W ∈ ker L — la POSICIÓN del crítico,
no su curvatura); (2) como carga conservada (166.9: κ = n_−(W) congelado en 𝕄); (3) como escala del
valor crítico (166.6: 𝔇 ≥ φ(|b_j|)⟨Gv_j,v_j⟩, con b_j el dato espectral de Q). (c) En consecuencia,
el muro NO reaparece como "rigidez de un punto fijo" (curvatura positiva = positividad de Weil): la
curvatura es positiva GRATIS (L ≥ 0 es un cuadrado). Reaparece como **pertenencia al cono + ley de
conservación**: RH ⟺ W ∈ 𝕄 (el punto fijo universal cae dentro del cono) ⟺ el ínfimo 0 se alcanza
(166.11(c)); y mientras tanto κ está congelado para toda deformación interior (166.9).

**Prueba.** (a) 𝔇₂ es cuadrática: 𝔇₂(G) = ½⟨LG,G⟩_{HS}; su Hessiano es L en todo punto, y
⟨LM,M⟩ = ∫e^{−2|t|}‖A_t(M)‖² + ‖A_J(M)‖² ≥ 0 es un cuadrado (suma de cuadrados de mapas lineales).
Que L ≠ "Q como forma sobre deformaciones" se ve en el contenido: ker L está descrito por
conmutación con la dinámica (166.13(b)) y contiene a W; Q como forma cuadrática sobre K tiene índice
κ; L como forma sobre H_h tiene núcleo = el conmutante apareado y NINGÚN índice negativo. Objetos de
tipo distinto, con firmas distintas, sobre espacios distintos. (b) Son los teoremas citados.
(c) Combinación de 166.6(ii), 166.7, 166.9, 166.11(c), 166.13(a)(c). ∎

### 5.2 Relación con la segunda variación de Phase 28 — y por qué no se re-encuentra el mismo muro en el mismo lugar

Phase 28 (Pregunta D.15) preguntaba por la segunda variación de Q en la dirección transversal b_j: la
Hessiana de una ENERGÍA de la función (E_log) respecto del movimiento de los CEROS — y encontró que
el sector aritmético G_ζ es incontrolable sin RH (Wall A). Aquí la variable es otra (la métrica, con
los ceros fijos) y los b_j entran a PRIMER orden en el valor del funcional (φ(b) ~ 2b/e, 166.6) y a
SEGUNDO orden en la tasa del flujo (ℓ(b) ~ 2b², 166.13(d)) — no como una Hessiana que haya que
demostrar positiva. La positividad que en Phase 28 era el problema (Hessiana de E en b=0) aquí es
gratuita (L ≥ 0); el problema se transfiere íntegro a la PERTENENCIA AL CONO del punto fijo. El muro
no desapareció: cambió de tipo lógico — de "demostrar una desigualdad" a "demostrar que un punto fijo
canónico de una dinámica RH-libre cae en un cono convexo dado". No afirmo que esto sea más tratable;
afirmo que es un enunciado DISTINTO con herramientas distintas (geometría convexa del cono de
métricas y teoría del salto de índice en su frontera, en lugar de positividad de formas).

### 5.3 [GAP 166.F — la herramienta ausente, nombrada]

Lo que esta teoría deja como única salida dentro de su propio lenguaje: un mecanismo de **salto de
índice en ∂𝕄**. Dentro de 𝕄, κ congelado (166.9); el flujo alcanza ∂𝕄 (166.13(c)); EN la frontera
la inercia puede saltar (la congruencia deja de ser isomorfismo). La pregunta precisa que queda
abierta: *¿existe una noción de "métrica degenerada renormalizada" (un blow-up de ∂𝕄, al estilo de
las compactificaciones de espacios de móduli) en la que el límite del flujo de Gram G_∞ (degenerado
sobre N) se re-expanda a una métrica genuina sobre un espacio MODIFICADO, y tal que la dinámica
re-expandida tenga κ estrictamente menor?* Esto es una pregunta de análisis geométrico de
degeneraciones (no de positividad), estructuralmente paralela a cruzar Λ=0 en DBN. No conozco
literatura que la trate para pares (forma de Krein fija, métrica degenerando) [GAP de literatura:
la teoría de Langer de operadores definitizables (Langer 1982) clasifica espectros para UNA métrica
de Krein dada; no hay, que yo sepa, teoría de límites de familias de simetrías fundamentales
degenerando con control del índice]. Es el sucesor natural de este documento.

---

## 6. Veredicto

**VEREDICTO: B′ (entre A y B, más cerca de B, con dividendos genuinos de tipo A).**

- **No es C:** 𝕄 y 𝕄_Q son no vacíos, convexos/contráctiles, RH-libres (166.2, 166.3).
- **No es A pleno:** la pieza central "∃G: 𝔇(G)=0 ⟺ RH" (166.7) es el GAP 164.D formalizado = RH
  reescrita, como el mandato advirtió que podía pasar; lo declaro sin maquillaje.
- **No es B tal como estaba previsto:** el modo de fallo esperado era "segunda variación de 𝔇 = forma
  de Weil = RH otra vez". **Eso es FALSO** (166.10): el Hessiano es L ≥ 0, RH-libre, un cuadrado. La
  circularidad no está en la curvatura; está en la pertenencia al cono del punto fijo universal W y
  en la ley de conservación de κ. Por eso Łojasiewicz/centro-variedad no son las herramientas
  ausentes (166.8): no hay equilibrio interior que estabilizar cuando m ≥ 1.
- **Los dividendos no-RH-equivalentes (por qué B′ y no B):**
  1. **[TEOREMA 166.9]** κ es ley de conservación exacta de toda deformación de métricas (inercia de
     Sylvester): no-go nuevo — deformar la métrica con la forma fija no puede reducir κ; responde la
     pregunta del director (la expulsión ES conservación).
  2. **[TEOREMA 166.6]** cota inferior explícita 𝔇 ≥ φ(|b_j|)⟨Gv_j,v_j⟩ con
     φ(b)=2b(1−2b)^{(1−2b)/(2b)}, y la calibración del peso e^{−|t|} por la franja crítica
     (φ < ∞ ⟺ b < ½ = Hadamard–de la Vallée Poussin): la geometría del funcional codifica el único
     resultado de localización de ceros que la humanidad tiene, y lo usa como condición de
     integrabilidad.
  3. **[TEOREMA 166.13]** el flujo de Gram es lineal, su punto fijo universal es W (existe SIEMPRE;
     RH = que caiga dentro del cono), expulsa toda métrica hacia/através de ∂𝕄 aplastando exactamente
     las direcciones off-line, con tasa ℓ(b_j) = 2b_j² + O(b_j⁴) — eco de escala con Λ = max b_j²/2
     (Phase 28 A.15), no explicado (factor 4), anotado como dato.
  4. **[PROP 166.11] + [PUENTE 166-DBN]** la estructura "ínfimo 0, alcance ⟺ RH" coloca a RH en la
     frontera de un problema variacional de métricas, en dualidad formal exacta con Rodgers–Tao
     (Λ ≥ 0: RH en la frontera del problema de deformación de la función). Dos deformaciones duales
     (forma vs métrica), una cantidad (κ) que es dinámica en una y conservada en la otra.
- **El sucesor nombrado:** teoría del salto de índice en ∂𝕄 (blow-up de métricas degeneradas,
  GAP 166.F) — y el posible flujo acoplado forma+métrica (DESEO 166.C) que pondría DBN y Gram en un
  solo retrato de fases.

**Dónde está RH en esta teoría (una frase):** no en la existencia del punto crítico (gratis: W), no
en su estabilidad (gratis: L ≥ 0), sino en que **el punto crítico universal de la dinámica de
métricas pertenezca al cono de las métricas** — y mientras se deforma dentro del cono, la obstrucción
κ es una carga conservada que ninguna deformación de métricas puede descargar; solo la frontera
(degeneración del espacio) o el otro flujo (DBN, que mueve la forma) pueden tocarla.

---

## 7. Apéndice: tabla de etiquetas y auditoría RH-libre

### 7.1 Etiquetas

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [DEF 166.1] 𝕄, ∂𝕄, 𝕄_Q | cono de Gram admisibles; degeneradas; simetrías fundamentales | definido |
| [PROP 166.2] estructura de 𝕄 | no vacío, cono convexo abierto, contráctil, GL/U | **probado** (solo H-W) |
| [PROP 166.3] estructura de 𝕄_Q | ≅ bola de contracciones estrictas ℂ^κ→K₊; no vacío sin RH; κ invariante | **probado** (H-W, H-Π; Pontryagin/Bognár/Azizov–Iokhvidov) |
| [OBS 166.4] escape de Haar | compatibilidad gratis en el espacio ciego; el costo nace en K | **establecido** |
| [DEF 166.5] 𝔇 | defectos A_t, A_J; peso e^{−|t|} | definido |
| [PROP 166.5′] | 𝔇 convexo, Lipschitz, 1-homog; término J gratuito | **probado** (H-26 i,iii) |
| [TEOREMA 166.6] cota inferior | 𝔇 ≥ φ(\|b_j\|)⟨Gv_j,v_j⟩/‖v_j‖²; φ exacta; calibración franja↔peso; sin ceros interiores | **probado** (H-26) |
| [TEOREMA 166.7] cero de 𝔇 | ∃G∈𝕄: 𝔇=0 ⟺ m=0 (⟸ con GAP de uniformidad) | **probado**; **declarado RH-reescrito (= GAP 164.D)** |
| [PROP 166.7′] Pontryagin–Stone | compatibilidad en 𝕄_Q = descomposición fundamental invariante ⟹ espectro real | **probado** (H-26) |
| [COR 166.8] | m≥1 ⟹ sin crítico interior; Łojasiewicz–Simon inaplicable | **probado** |
| [TEOREMA 166.9] conservación | κ(G) = κ en todo 𝕄 (Sylvester); salto solo en ∂𝕄 | **probado** (H-W, H-Π; sin H-26, sin RH) |
| [PUENTE 166-DBN] | dualidad forma/métrica con De Bruijn–Newman; RH en frontera en ambos | honesto, traducción vía puente Phase 26 no probado |
| [PROP 166.11] colapso | inf normalizado = 0 sin alcance si m≥1; minimizantes aplastan N; alcance ⟺ RH | **probado bajo (H-26⁺)**, marcado |
| [CONSTR 166.12] flujo de Gram | Ġ = −LG, sustituto liso; teoría completa en el modelo finito | definido; [GAP 166.D] HS en dim ∞ |
| [TEOREMA 166.13] dinámica | W ∈ ker L siempre; ker L apareado λ↔λ̄; expulsión hacia/por ∂𝕄; tasa ℓ(b)=2b²+O(b⁴) | **probado en el modelo** (H-26 restringida) |
| [TEOREMA 166.10] anti-circularidad | Hessiano = L ≥ 0 ≠ Q; circularidad en pertenencia-al-cono + conservación + escala del valor | **probado** |
| [PUENTE 166-E] | eco 2b² ↔ Λ=b²/2 (A.15); factor 4 sin explicar | honesto, no identidad |
| [GAP 166.A] | no-degeneración/uniformidad del Gram de Weil (radical, W ≥ ε) | declarado |
| [GAP 166.B] | concentración del índice en N + uniformidad en K₁ (H-26⁺) | declarado |
| [DESEO 166.C] | flujo acoplado (W_t, G_s) DBN+Gram | declarado |
| [GAP 166.D] | finitud HS del sustituto liso en dim ∞ | declarado |
| [GAP 166.F] | teoría del salto de índice en ∂𝕄 (blow-up de métricas degeneradas) | declarado; [GAP de literatura] sin teoría conocida de límites de simetrías fundamentales degenerando |

### 7.2 Auditoría RH-libre, pieza por pieza

| Objeto | ¿RH-libre? |
|---|---|
| ⟨·,·⟩₀ (fondo Haar/Lebesgue) | SÍ (D164) |
| W (forma de Weil como forma) | SÍ como forma; su positividad NO se usa en ningún teorema |
| U_t, J | SÍ como operadores (D164); su Q-unitariedad es (H-26)(i) = V.1 de Phase 26, hipótesis declarada |
| v_j (autovectores off-line) | hipótesis (H-26)(ii) = V.2 de Phase 26; si m=0 es vacua |
| 𝕄, 𝕄_Q, ∂𝕄 | SÍ (166.2, 166.3 usan solo H-W, H-Π) |
| 𝔇, 𝔇₂, L, el flujo | SÍ: definidos solo por (U_t, J, ⟨·,·⟩₀, peso) |
| κ(G) y su conservación | SÍ (166.9 no usa ni H-26 ni RH) |
| El valor inf 𝔇 y su alcance | el ALCANCE es RH (declarado, 166.7/166.11(c)); el resto de la geometría (cotas, tasas, conservación) es RH-libre |

---

**Referencias (reales).**
- L.S. Pontryagin, "Hermitian operators in spaces with indefinite metric", *Izv. Akad. Nauk SSSR,
  Ser. Mat.* **8** (1944) 243–280.
- I.S. Iokhvidov, M.G. Krein, "Spectral theory of operators in spaces with an indefinite metric I",
  *Trudy Moskov. Mat. Obshch.* **5** (1956) 367–432 (AMS Transl. (2) 13).
- J. Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik 78, Springer 1974 —
  simetrías fundamentales (cap. IV–V), cociente por el radical (cap. I §11).
- T.Ya. Azizov, I.S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric*, Wiley 1989 —
  operadores de ángulo (cap. 1 §8), subespacios raíz del espectro no-real (cap. 2 §2), acotación de
  π-unitarios.
- M.G. Krein, H. Langer, "Über die Q-Funktion eines π-hermiteschen Operators im Raume Π_κ", *Acta
  Sci. Math. (Szeged)* **34** (1973) 191–230.
- H. Langer, "Spectral functions of definitizable operators in Krein spaces", en *Functional
  Analysis (Dubrovnik 1981)*, Lecture Notes in Math. **948**, Springer 1982, pp. 1–46.
- M.H. Stone, "On one-parameter unitary groups in Hilbert space", *Ann. of Math.* **33** (1932)
  643–648; M. Reed, B. Simon, *Methods of Modern Mathematical Physics I*, Academic Press 1980,
  Thm VIII.7–VIII.8.
- N.G. de Bruijn, "The roots of trigonometric integrals", *Duke Math. J.* **17** (1950) 197–226 —
  monotonía en t de la realidad de los ceros (§13).
- C.M. Newman, "Fourier transforms with only real zeros", *Proc. Amer. Math. Soc.* **61** (1976)
  245–251 — existencia de Λ y conjetura Λ ≥ 0.
- B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative", *Forum Math. Pi* **8** (2020)
  e6 — Λ ≥ 0.
- S. Łojasiewicz, "Une propriété topologique des sous-ensembles analytiques réels", en *Les Équations
  aux Dérivées Partielles* (Paris 1962), Colloques Internationaux du CNRS **117** (1963) 87–89.
- L. Simon, "Asymptotics for a class of non-linear evolution equations, with applications to
  geometric problems", *Ann. of Math.* **118** (1983) 525–571.
- H. Brezis, *Opérateurs maximaux monotones et semi-groupes de contractions dans les espaces de
  Hilbert*, North-Holland Math. Studies 5, 1973 — flujos de subgradiente de funcionales convexos.
- J. Hadamard, "Sur la distribution des zéros de la fonction ζ(s) et ses conséquences arithmétiques",
  *Bull. Soc. Math. France* **24** (1896) 199–220; Ch.-J. de la Vallée Poussin, "Recherches
  analytiques sur la théorie des nombres premiers", *Ann. Soc. Sci. Bruxelles* **20** (1896) 183–256
  — no anulación en Re s = 1 (⟹ b_j < ½ para cada cero).
- A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function",
  *Selecta Math. (N.S.)* **5** (1999) 29–106 — el flujo de escala y el espacio de fondo.
- [GAP de literatura]: no conozco (i) una formulación del problema de la métrica común para los dos
  grupos (J, U_t) como problema variacional sobre el espacio de simetrías fundamentales, (ii) una
  teoría de degeneración de familias de simetrías fundamentales con control del salto de índice
  (GAP 166.F), ni (iii) el funcional 𝔇 con peso calibrado por la franja. Las referencias anclan las
  herramientas (Pontryagin/Krein/Langer, Stone, DBN, Łojasiewicz–Simon); la teoría de deformación de
  métricas de este documento es nueva.
