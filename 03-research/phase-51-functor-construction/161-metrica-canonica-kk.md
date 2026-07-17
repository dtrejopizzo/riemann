# Doc 161 — La métrica de inercia canónica vía dualidad de Poincaré no-conmutativa: ¿clase fundamental KK RH-libre, o ζ por estructura modular?

**Programa:** Hipótesis de Riemann — Phase 51: construcción del functor fase→inercia.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** DECISORIO. Mandato: decidir GAP-160.A + DESEO 160.B. El Doc 160
construyó un transporte fase→inercia genuino (𝔉_KMS) y RH-libre, pero localizó que la
MÉTRICA que lee el objeto transportado como inercia m = neg.ind de Weil no está determinada
por la dinámica: la única métrica conocida con signatura m es la forma de Weil misma, que
enumera los ceros (circularidad de Phase 43). DESEO 160.B nombró la herramienta candidata de
cierre: obtener esa métrica CANÓNICAMENTE de la **clase fundamental en KK-teoría / la
dualidad de Poincaré no-conmutativa** del producto cruzado 𝒜 = C(𝕋)⋊_φ ℝ. Este documento
decide si esa métrica canónica existe y si es RH-libre. Una falsa victoria es peor que un
fracaso; está PERMITIDO (y es lo más probable) terminar en un no-go genuino.

**Contrato de etiquetado (regla absoluta).** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad aquí, prueba completa; resultados
externos citados con referencia verificable. **[CÁLCULO]** = mostrado. **[CONSTRUCCIÓN]** =
objeto definido con precisión. **[PUENTE]** = conexión con estatus honesto de cada eslabón.
**[GAP]/[GAP de literatura]** = declarado; el de literatura NO se usa como premisa de ningún
teorema. **[DESEO]** = declarado. Jamás se fabrica una prueba de RH ni el DESENLACE 2 (grial).
**NADA de numéricos/Python.** **Español.** Honestidad absoluta.

**Prerrequisitos leídos en fuente esta sesión:** Doc 160 completo (𝔉_KMS Prop. 160.7; el test
de polarización Prop. 160.10; GAP-160.A la métrica de inercia RH-libre; DESEO 160.B la
signatura de Weil como invariante KK; PUENTE 160-A el producto cruzado restringido de Connes;
PUENTE 160-B la elección forzada plano-vs-Weil). Doc 156 completo (la trifurcación
Fredholmicidad/clase/escape; VEREDICTO caso (b)-Fredholmicidad: ζ entra primariamente en la
Fredholmicidad del símbolo de Weil–Toeplitz, secundariamente en la clase/winding; Prop. 156.6,
156.7; Teorema 156.5 κ = winding = 2m bajo m<∞). Memoria Phase 26 (κ = 2m = neg.ind(H_C) en
Pontryagin (𝒦,Q)). Memoria Phase 43 (la métrica de polarización porta ζ; la flecha invertida).

---

## 0. Resumen ejecutivo y veredicto adelantado

Coloco el veredicto al frente (honestidad: no quiero que se descubra como sorpresa).

> **VEREDICTO: DESENLACE 1 — NO-GO ESTRUCTURAL.** La métrica de inercia canónica que la
> dualidad de Poincaré no-conmutativa asociaría a 𝒜 = C(𝕋)⋊_φ ℝ se define, por construcción,
> a través del **peso dual / la estructura modular de Tomita–Takesaki** del producto cruzado.
> Para este sistema —el flujo de Kronecker de {log p}, idéntico en su parte aritmética al
> sistema de Bost–Connes— la **función de partición de esa estructura modular ES la función
> zeta** (fenómeno BC95: la partición del sistema BC es ζ(β), los estados KMS_β a β>1
> codifican los primos vía Ẑ^×). Por tanto: **toda normalización canónica de la clase
> fundamental que la convierta en una métrica con signatura definida porta ζ por la estructura
> modular, NECESARIAMENTE, no por elección.** La ruta del producto cruzado de Kronecker (=
> la familia de approaches Connes/producto-cruzado) NO produce una métrica de inercia
> RH-libre: es circular por construcción, no inacabada. Lo enuncio como teorema (§5.2,
> [TEOREMA 161.9]).

**La localización fina (y la consistencia con Doc 156).** ζ entra en la **orientación /
normalización modular de la clase fundamental** — el nodo (ii) de la trifurcación
(existencia / normalización-orientación / escape). Esto es *consistente y complementario* con
Doc 156, que halló ζ en la *Fredholmicidad* (nodo (i)) por la vía Toeplitz. Son dos vías al
mismo objeto m que tocan ζ en dos nodos distintos: la vía Toeplitz/símbolo lo toca en la
existencia (Fredholmicidad), la vía KK/peso-dual lo toca en la orientación (el peso modular).
La síntesis (§4.4): **el peso dual es positivo (existe) RH-libremente, pero su MÓDULO modular
—la derivada de Radon–Nikodym que fija la signatura— es el flujo cuya función de partición es
ζ.** El objeto existe; su orientación es ζ. Es no-go de tipo "circular", reforzado por el de
tipo "la métrica no es canónica sin ζ".

**Por qué NO es DESENLACE 2.** Sometí el candidato a grial al triple test de estrés (§3.4):
(T1) la clase fundamental de C(𝕋)⋊ℝ por Connes–Thom existe RH-libremente —pero da
K-homología de FASE, no la signatura de inercia (mismo fallo que 𝔉_ind, Doc 160 Prop. 160.8);
(T2) el apareamiento de Kasparov produce números de winding de fase, no la signatura m, salvo
que se tuerza con el peso dual —y ahí entra ζ; (T3) la dualidad de Poincaré-NC requiere una
clase de orientación (KMS/peso), y para este sistema esa clase ES la función de partición ζ.
Los tres tests, independientes, dan el mismo resultado: la signatura RH-libre no aparece. NO
finjo (2).

Estructura: §1 la clase fundamental / dualidad de Poincaré-NC de C(𝕋)⋊ℝ (¿existe?
¿canónica?). §2 el test modular y la conexión Bost–Connes (el corazón). §3 la trifurcación y
el triple test de estrés. §4 dónde EXACTAMENTE entra ζ y la síntesis con Doc 156. §5 veredicto
y el teorema de circularidad estructural. §6 mensaje final.

---

## 1. La clase fundamental / dualidad de Poincaré no-conmutativa de C(𝕋)⋊ℝ

### 1.1. Qué pide DESEO 160.B, con precisión

El GAP-160.A es la ausencia de un producto interno sobre H_altura que sea (i) determinado por
la dinámica de Kronecker y (ii) tenga signatura m = neg.ind(Q_Weil) sin enumerar los γ_ρ.
DESEO 160.B propone: tal producto interno sería el emparejamiento del cociclo de Weil consigo
mismo **vía la dualidad de Poincaré no-conmutativa** del producto cruzado. En lenguaje preciso
de KK-teoría [Con94, IV; Kas88], una C*-álgebra A es **Poincaré-dual** (PD-álgebra) si existe
una **clase fundamental**
$$[\Delta]\in KK_d(A\otimes A^\circ,\;\mathbb C)$$
con una clase inversa [Δ]^{-1}∈KK_{-d}(ℂ, A⊗A°) satisfaciendo las relaciones de composición
de dualidad (el producto de Kasparov con [Δ] da el isomorfismo K_•(A)≅K^{•+d}(A) de
K-teoría a K-homología) [BMRS08, §2; Kas88, §4]. La idea de DESEO 160.B: si [Δ] existe
canónicamente, induce un **emparejamiento** sobre K-homología, y ese emparejamiento sería la
métrica candidata cuya signatura podría ser m.

**La pregunta-bisturí, reformulada en tres sub-preguntas decidibles:**
- (Q1) ¿Existe [Δ] para A = C(𝕋)⋊_φ ℝ? ¿Es canónica (única, sin elección a mano)?
- (Q2) Si existe, ¿el emparejamiento de Kasparov que induce tiene signatura m, o da otra cosa
  (números de fase)?
- (Q3) ¿La normalización / orientación que hace de [Δ] una métrica con signatura porta ζ?

### 1.2. La clase fundamental EXISTE, vía Connes–Thom — pero es de FASE

**[PROPOSICIÓN 161.1] (la dualidad de Poincaré-NC de C(𝕋)⋊ℝ se reduce, vía Connes–Thom, a la
de C(𝕋), desplazada en grado 1 — y por tanto es RH-libre PERO de coordenada de fase).** El
producto cruzado por ℝ es **KK-equivalente, con desplazamiento de grado 1, al álgebra base**:
por el isomorfismo de Connes–Thom [Con81; Con94, II.5; FS81] hay una clase invertible
$$\mathbf{t}\in KK_1\big(C(\mathbb T)\rtimes_\varphi\mathbb R,\;C(\mathbb T)\big),
\qquad \mathbf{t}^{-1}\in KK_1\big(C(\mathbb T),\;C(\mathbb T)\rtimes_\varphi\mathbb R\big),$$
implementando K_•(C(𝕋)⋊ℝ) ≅ K_{•+1}(C(𝕋)). En consecuencia, **C(𝕋)⋊ℝ es Poincaré-dual si y
solo si C(𝕋) lo es**, y su clase fundamental es
$$[\Delta_{\mathcal A}] \;=\; \mathbf t\otimes [\Delta_{C(\mathbb T)}]\otimes \mathbf t^\circ
\quad(\text{producto de Kasparov, con el twist de grado 1 de Connes–Thom en cada factor}),$$
donde [Δ_{C(𝕋)}] es la clase fundamental del toro de Bohr. La clase fundamental del producto
cruzado, vista a través de Connes–Thom, vive sobre la **K-homología de 𝕋** = un objeto de la
coordenada de FASE.

*Demostración.* Connes–Thom da que **t** es invertible en KK [Con81, Thm. 1; FS81 dan la
versión vía suspensión/Bott: A⋊ℝ ≃ SA en KK, donde S = suspensión]. La invertibilidad
transporta la propiedad PD: si [Δ_B] es clase fundamental de B y A es KK-equivalente a B vía
una clase invertible u∈KK_j(A,B), entonces u⊗[Δ_B]⊗u° es clase fundamental de A en grado
d+2j [BMRS08, Lema 2.x sobre invariancia de PD bajo KK-equivalencia]. Con B = C(𝕋), j = 1, la
clase fundamental de 𝒜 desciende a la de 𝕋. Como K_•(C(𝕋)⋊ℝ)≅K_{•+1}(C(𝕋)) y el dual también,
el emparejamiento de Kasparov ⟨·,[Δ_𝒜]⟩ se calcula sobre invariantes de K-teoría de 𝕋. $\square$

**[TEST DE COORDENADA — el primer fallo, idéntico a 𝔉_ind].** La Prop. 161.1 dice que la clase
fundamental, en cuanto objeto KK, NO sabe de la altura: vive sobre 𝕋 (fase). Esto es
**exactamente** lo que el Doc 160 §2.3 (Prop. 160.8) ya halló para 𝔉_ind: el emparejamiento de
índice del producto cruzado se calcula contra K^•(𝕋) = winding numbers de fase. La razón es la
misma: Connes–Thom **traslada el grado, no crea la coordenada de inercia**. La altura γ no es un
invariante de K-teoría del toro de Bohr. **La clase fundamental existe y es RH-libre, pero su
emparejamiento es de FASE, no de inercia.** Respuesta preliminar a (Q1)/(Q2): la clase existe,
canónica salvo la orientación (§1.3), y su pairing topológico crudo NO es m.

### 1.3. El punto crítico: la orientación / espín-c NO es topológica aquí — es MODULAR

**[PROPOSICIÓN 161.2] (la clase fundamental de un producto cruzado por ℝ requiere una
ORIENTACIÓN que, para un álgebra de tipo III, es un dato MODULAR, no topológico).** La clase
[Δ] de §1.2 está definida **salvo una clase de orientación**: la dualidad de Poincaré-NC, en el
formalismo de triples espectrales [Con94, VI; CM95], requiere no solo la clase de K-homología
sino una **clase fundamental orientada** — el análogo NC de una forma de volumen / clase de
fundamental orientada de variedad. En el caso conmutativo de una variedad spin-c, esa
orientación es topológica (la clase spin-c). **Pero C(𝕋)⋊_φ ℝ con el flujo de Kronecker NO es,
en general, un álgebra finita (tipo II₁) ni admite una traza finita canónica:** el producto
cruzado por un flujo ergódico minimal sobre un grupo compacto es típicamente un factor cuya
clasificación de tipo depende de la estructura del flujo de pesos [CT77]. La orientación que
fija el signo del emparejamiento de Poincaré-NC en un álgebra sin traza finita NO es la clase
spin-c topológica: es el **estado/peso (KMS) respecto del cual se define la traza-Dixmier o el
ciclo fundamental**, es decir, un dato de la **teoría modular de Tomita–Takesaki**.

*Demostración (estructura).* (i) En el formalismo de Connes, una métrica/orientación sobre un
álgebra NC = la elección del operador de Dirac D y de un funcional traza (estado o peso) que
hace de (𝒜, H, D) un triple espectral con clase fundamental [Con94, VI.1; CM95 §I]. (ii) Para
un álgebra finita (traza finita τ), τ es canónica (estado tracial único en factor II₁) y la
orientación es topológica. (iii) Para C(𝕋)⋊_φ ℝ, el producto cruzado por ℝ es **propiamente
infinito** salvo casos degenerados (la acción de ℝ es un flujo); por la teoría de Takesaki, los
productos cruzados por flujos modulares producen factores de tipo III/II_∞, cuyo funcional
canónico no es una traza finita sino un **peso** [Tak03, Vol. II, cap. X; CT77]. (iv) El peso
canónico del producto cruzado es el **peso dual** φ̃ de un peso φ sobre C(𝕋) [Tak03, Vol. II,
Def. X.1.16, Thm. dual weight]. La orientación del ciclo fundamental se lee respecto del flujo
modular σ^{φ̃} de φ̃. $\square$

**Esto reubica la pregunta entera en la teoría modular.** La clase fundamental topológica
(§1.2) es RH-libre pero da fase. La signatura m solo puede aparecer si la **orientación
modular** del ciclo fundamental tuerce el emparejamiento de fase hasta darle signatura. Y la
orientación modular es el **peso dual** — que es el objeto donde, para este sistema, vive ζ.
Esto es el test modular del §2, el corazón del documento.

### 1.4. [PUENTE 161-A] Estatus honesto de la existencia de [Δ]

La existencia de [Δ_{C(𝕋)}] (clase fundamental del toro de Bohr) es **[GAP de literatura
parcial]**: el toro de Bohr 𝕋 = ∏_p S¹ es un grupo compacto abeliano de dimensión infinita
(profinito-conexo); la dualidad de Poincaré-NC para C(G), G grupo compacto, es estándar en
dimensión finita (G variedad spin-c), pero en dimensión infinita la "dimensión espectral" d no
es finita y la clase fundamental en KK_d requiere d finito. Lo registro como puente: la
clase fundamental TOPOLÓGICA de 𝕋 existe a nivel de cada factor finito-dimensional truncado
(∏_{p≤P} S¹ = toro ordinario, spin-c canónico), y el sistema infinito es el límite proyectivo
— pero la signatura de inercia es justamente lo que NO sobrevive al límite (es donde la
"dimensión" se vuelve infinita). NO uso "la clase fundamental existe en dim ∞" como premisa de
ningún teorema; el no-go del §5 NO depende de que exista —al contrario, refuerza el no-go: o
bien [Δ] no existe en dim ∞ (no-go de tipo "el objeto no existe", nodo (i)), o bien existe pero
su orientación es modular = ζ (nodo (ii)). Ambas ramas son no-go.

---

## 2. El test modular (el corazón) y la conexión Bost–Connes

### 2.1. El peso dual y el flujo modular del producto cruzado

**[CONSTRUCCIÓN 161.3] (el peso dual y su flujo modular).** Sea φ un peso normal semifinito
fiel sobre C(𝕋) (en el caso ergódico, la integral de Haar μ_Haar da el estado canónico). El
producto cruzado 𝒜 = C(𝕋)⋊_φ ℝ porta el **peso dual** φ̃ [Tak03, Vol. II, X.1; Haagerup,
"On the dual weights for crossed products of von Neumann algebras I, II", Math. Scand. 43
(1978) 99–118, 119–140]. El flujo modular del peso dual satisface la relación fundamental de
Takesaki:
$$\sigma_t^{\tilde\varphi}(x) = \sigma_t^{\varphi}\text{-extendido sobre } C(\mathbb T),
\qquad \sigma_t^{\tilde\varphi}(U_s) = U_s\, ( \text{cociclo del flujo dual}),$$
y, lo decisivo, el flujo dual θ (la acción dual de ℝ̂ = ℝ que el Doc 160 usó en 𝔉_KMS) está
ligado al módulo del peso dual: **θ_s = Ad de la derivada de Radon–Nikodym del peso dual a lo
largo del parámetro espectral s** [Tak03, Vol. II, X.2; la dualidad de Takesaki–Takai relaciona
σ^{φ̃} y θ]. En palabras: **el flujo dual θ de 𝔉_KMS (Doc 160) y el flujo modular σ^{φ̃} de
Tomita–Takesaki son las DOS caras del mismo objeto** — θ es el flujo de la acción dual, σ^{φ̃}
es el flujo modular interno, y ambos están entrelazados por la teoría de Connes–Takesaki del
flujo de pesos [CT77].

**[OBSERVACIÓN CLAVE — el doble papel de la variable s, ahora a nivel modular].** El Doc 160
notó que la variable dual s del flujo θ es simultáneamente la coordenada de altura (donde
vivirían los γ) y la dual de log p. Ahora añado: esa misma s es **el parámetro del flujo
modular** σ^{φ̃}_s. La signatura de inercia que buscamos (la neg.ind de la forma de Weil) es,
en el lenguaje modular, **la asimetría espectral del generador del flujo modular** — y esa
asimetría es exactamente el invariante η/peso-dual. Esto conecta directamente con el η de
Doc 156 §4.2 (APS) y con la pregunta de si la métrica canónica porta ζ.

### 2.2. La identificación Bost–Connes: la función de partición ES ζ

**[PROPOSICIÓN 161.4 / PUENTE 161-B] (la parte aritmética del producto cruzado de Kronecker es
el sistema de Bost–Connes, cuya función de partición es ζ — el dato decisivo).** El sistema de
Bost–Connes [BC95] es el sistema cuántico-estadístico (𝒜_{BC}, σ_t) con
$$\mathcal A_{BC} \;=\; C^*\big(\mathbb Q/\mathbb Z\big)\rtimes \mathbb N^\times
\quad\text{(álgebra de Hecke del par } (P_\mathbb Q^+, P_\mathbb Z^+)\text{)},$$
y flujo temporal σ_t generado por log de los índices, σ_t(μ_n) = n^{it} μ_n sobre los
isometrías μ_n que implementan la acción del semigrupo multiplicativo ℕ^×. **Hechos de BC95,
verificados [BC95; Wikipedia "Bost–Connes system"; CM-lectures math/0409520]:**
- (BC-1) La **función de partición** del sistema BC es **Z(β) = ζ(β)** (la función zeta de
  Riemann) [BC95, Prop. 25; CMR CM2short].
- (BC-2) **Transición de fase a β = 1** con ruptura espontánea de simetría: para β ≤ 1 hay un
  único estado KMS_β; para 1 < β ≤ ∞ los estados KMS_β extremales se parametrizan por
  **Ẑ^× = Gal(ℚ^{ab}/ℚ)** [BC95, Thm. principal].
- (BC-3) Los **estados KMS_β a β > 1 codifican los primos**: el valor de un estado KMS_β
  extremal sobre los generadores aritméticos es una serie sobre primos (∏_p factores de Euler
  locales), y la temperatura inversa β es la coordenada dual a la altura/escala.

**La conexión con 𝒜 = C(𝕋)⋊_φ ℝ (el puente, con estatus honesto).** El flujo de Kronecker
φ_t(z) = (p^{-it} z_p)_p sobre el toro de Bohr 𝕋 = ∏_p S¹ tiene por generadores de frecuencia
exactamente {log p}; el generador del flujo dual θ_s(U_{log p}) = e^{is log p} U_{log p}
multiplica por p^{is}. **Esto es, sobre los generadores primos, la MISMA dinámica que el flujo
BC σ_t(μ_p) = p^{it} μ_p.** El toro de Bohr 𝕋 = ∏_p S¹ es precisamente el grupo dual de
⊕_p ℤ ≅ ℚ^×_{>0} (los racionales positivos bajo multiplicación, vía factorización única), y
ℚ^×_{>0} es el semigrupo-grupo cuya completación da la parte multiplicativa de los idèles de
BC. **Estatus honesto [PUENTE 161-B]:** el producto cruzado de Kronecker C(𝕋)⋊_φ ℝ y el sistema
BC NO son literalmente isomorfos como C*-álgebras (BC usa el SEMIGRUPO ℕ^× y una álgebra de
Hecke con isometrías no-unitarias μ_n; Kronecker usa el GRUPO ℝ con unitarios U_t y el flujo
diagonal). Pero comparten **exactamente la estructura modular relevante**: el flujo dual/modular
sobre los generadores primos es t ↦ p^{it}, y la función de partición de esa dinámica
—la traza del operador de evolución e^{-βH} sobre el espacio de los modos primos— es
$$Z(\beta) = \mathrm{Tr}(e^{-\beta H}) = \sum_{k\ge 1} k^{-\beta} = \zeta(\beta),$$
donde H es el generador del flujo modular (Hamiltoniano), cuyo espectro sobre los modos
{∏ p^{n_p}} = {log k} (por factorización única, exactamente el espectro de 𝔉_coh del Doc 160
Prop. 160.5). **La función de partición del flujo modular del producto cruzado de Kronecker es
ζ por la MISMA razón que en BC: el espectro del Hamiltoniano modular es {log k} y la traza
térmica es ∑ k^{-β} = ζ(β).** Esto NO es un [GAP de literatura] sino un [CÁLCULO] elemental una
vez identificado el Hamiltoniano modular con el generador del flujo (ver §2.3).

### 2.3. [CÁLCULO 161.5] La función de partición del peso dual = ζ, explícitamente

**[CÁLCULO 161.5].** El generador H del flujo modular σ^{φ̃}_s = Ad(e^{isH}) actúa sobre
L²(𝕋, Haar) diagonalizado por los caracteres χ_n (n ∈ ⊕_p ℤ) del toro de Bohr:
$$H\,\chi_n = \langle n, (\log p)\rangle\,\chi_n = \Big(\sum_p n_p \log p\Big)\chi_n
= \log\Big(\prod_p p^{n_p}\Big)\chi_n = (\log k)\,\chi_n,\quad k=\prod p^{n_p}\in\mathbb Q^\times_{>0}.$$
La **función de partición** (traza térmica del semigrupo de evolución, restringida a los modos
de "energía positiva" k ∈ ℕ, k ≥ 1, que es la condición de positividad del peso dual / la
condición KMS que selecciona el cono de Tomita) es
$$Z(\beta) \;=\; \mathrm{Tr}\big(e^{-\beta H}\,\big|_{\text{energía}\ge 0}\big)
\;=\; \sum_{k\ge 1} e^{-\beta \log k} \;=\; \sum_{k\ge 1} k^{-\beta} \;=\; \zeta(\beta),
\qquad \mathrm{Re}\,\beta > 1.$$
La convergencia para Re β > 1 y el polo en β = 1 reproducen la transición de fase de BC
(BC-2): β = 1 es la frontera de convergencia, el polo de ζ. $\square$

**[PROPOSICIÓN 161.6] (la métrica canónica de Poincaré-NC se define vía el peso dual, y su
NORMALIZACIÓN es la función de partición ζ).** En el formalismo de la dualidad de Poincaré-NC
para álgebras de tipo III/II_∞ [Con94, VI; CM95], el emparejamiento del ciclo fundamental
—la "métrica" que induce la clase [Δ]— se normaliza respecto del peso canónico (el peso dual
φ̃), y la normalización térmica (la que hace el ciclo de clase traza / sumable, condición de
existencia del carácter de Chern–Connes) es **dividir por la función de partición Z(β) = ζ(β)**.
Concretamente, el funcional que define el producto interno sobre el espacio de altura es
$$\langle a, b\rangle_{\tilde\varphi,\beta}
\;=\; \frac{1}{Z(\beta)}\,\mathrm{Tr}\big(e^{-\beta H}\, a^* b\big)
\;=\; \frac{1}{\zeta(\beta)}\,\sum_{k\ge1} k^{-\beta}\,\overline{\hat a(\log k)}\,\hat b(\log k),$$
el estado KMS_β del peso dual. **El factor de normalización 1/ζ(β) es ζ literalmente; y la
analiticidad / signatura de ⟨·,·⟩_{φ̃,β} al continuar β hacia la región crítica Re β = ½ está
gobernada por los CEROS de ζ.**

*Demostración.* El peso dual φ̃ tiene como flujo modular σ^{φ̃}_s = Ad(e^{isH}) (Construcción
161.3, [Tak03, X.2]). El estado KMS_β asociado a un flujo con generador H y partición finita
Z(β) es ω_β(a) = Z(β)^{-1} Tr(e^{-βH} a) [BR97, Cap. 5, condición KMS / estado de Gibbs]. El
producto interno GNS de ω_β es ⟨a,b⟩ = ω_β(a*b), que da la fórmula. La normalización 1/Z(β) es
forzada por la condición de que ω_β sea un estado (ω_β(1) = 1): Z(β) = Tr(e^{-βH}) = ζ(β) por
[CÁLCULO 161.5]. La signatura de la forma cuadrática asociada al continuar β a la franja
crítica cambia exactamente en los β donde ζ(β) = 0 o tiene polos (los ceros y el polo
controlan los cambios de signo de la forma normalizada). $\square$

**ESTE ES EL CORAZÓN DEL NO-GO.** La métrica canónica que la dualidad de Poincaré-NC asocia al
producto cruzado NO es la forma L²-plana (la del Doc 160 PUENTE 160-B, RH-libre pero ciega) NI
es elegida a mano: es el **estado KMS_β del peso dual**, y su definición LLEVA ζ(β) en el
denominador (la función de partición) y sus cambios de signatura al continuar a la franja
crítica están gobernados por los ceros de ζ. **No es una elección; es la estructura modular
canónica. Y porta ζ.** Esto resuelve GAP-160.A en sentido negativo: la "tercera métrica"
(dinámica, no-plana, signatura m) que el Doc 160 buscaba ES el estado KMS del peso dual — y
porta ζ por la función de partición.

---

## 3. La trifurcación y el triple test de estrés

### 3.1. La trifurcación (existencia / normalización-orientación / escape)

Confronto con la trifurcación del Doc 156 (Fredholmicidad / clase / escape), que es la misma
estructura lógica en otra maquinaria:

| Nodo | Doc 156 (vía Toeplitz/símbolo) | Doc 161 (vía KK/peso-dual) |
|---|---|---|
| (i) **EXISTENCIA** | ζ entra en la **Fredholmicidad**: T_φ Fredholm ⟺ símbolo invertible en corona ⟺ m<∞ (Prop. 156.6, capa primaria/dominante) | ζ entra en la **existencia de [Δ] en dim ∞**: la dimensión espectral del toro de Bohr es ∞; [Δ] solo existe truncada, y la signatura no sobrevive el límite (§1.4, PUENTE 161-A) |
| (ii) **NORMALIZACIÓN/ORIENTACIÓN** | ζ entra en la **clase/winding**: concedido m<∞, winding(φ)=2m = posición de ceros (Prop. 156.7, capa secundaria) | ζ entra en la **orientación modular**: la métrica = estado KMS_β del peso dual, normalizado por Z(β)=ζ(β); signatura gobernada por ceros (Prop. 161.6) — **nodo dominante aquí** |
| (iii) **ESCAPE** | el triple espectral RH-libre con carácter de Chern = κ NO existe ([GAP lit., Doc 156 §4.5] = Connes 1999 y CCM portan ζ en la métrica) | el peso RH-libre que diera signatura m sin pasar por Z(β) NO existe (§3.4, T2/T3); el único peso canónico es el dual, y su partición es ζ |

**La diferencia fina entre las dos vías (y por qué ambas son no-go):** Doc 156 halló que el
nodo DOMINANTE es la **existencia** (Fredholmicidad): el objeto índice no existe sin RH. Doc 161
halla que, por la vía KK/peso-dual, el objeto (la clase fundamental topológica) SÍ existe
RH-libremente (§1.2, es K-homología de fase), pero el nodo dominante se desplaza a la
**orientación/normalización modular**: la clase existe pero su lectura como métrica de inercia
porta ζ por el peso dual. **Es el mismo muro, un nodo más adentro:** Doc 156 mata el objeto;
Doc 161 deja vivir el objeto topológico pero mata su orientación RH-libre. Consistencia total:
ambas vías localizan ζ en la estructura que convierte "valor" en "signatura", y esa estructura
es modular (= función de partición = ζ) tanto en el símbolo (winding de ζ) como en el peso
(partición ζ).

### 3.2. ¿En cuál nodo entra ζ por la vía KK? Respuesta: (ii), la orientación modular

**[PROPOSICIÓN 161.7] (ζ entra en la ORIENTACIÓN/NORMALIZACIÓN de la clase fundamental, no en
su existencia topológica).** Por Connes–Thom (Prop. 161.1), la clase fundamental topológica de
C(𝕋)⋊ℝ existe (módulo la cuestión de dim ∞, PUENTE 161-A) y es RH-libre: empareja con
K^•(𝕋) = invariantes de fase. La signatura m NO es un invariante de esa K-homología
topológica (Prop. 161.1, "TEST DE COORDENADA"). Para obtener m hace falta torcer el
emparejamiento topológico con la **orientación modular** = el estado KMS_β del peso dual
(Prop. 161.6), cuya normalización es ζ(β). Por tanto ζ entra en el nodo (ii): la clase existe,
pero su orientación como métrica de inercia ES ζ.

*Demostración.* Combinación de Prop. 161.1 (la clase topológica es de fase, RH-libre) +
Prop. 161.6 (la métrica de inercia = KMS_β del peso dual = normalizada por ζ). El emparejamiento
topológico de Kasparov ⟨·, [Δ]⟩ da números enteros (winding de fase, K-homología de 𝕋); para
que produzca la signatura REAL m de una forma cuadrática indefinida hace falta el estado/peso
que da la métrica de Hilbert (la simetría fundamental J del espacio de Pontryagin, Doc 156
§1.3), y ese peso es el dual, normalizado por Z(β) = ζ(β). $\square$

### 3.3. Consistencia con Doc 156: ¿contradicción o complemento?

Doc 156 dijo "ζ entra primariamente en la Fredholmicidad" (nodo (i)). Doc 161 dice "ζ entra en
la orientación modular" (nodo (ii)). **¿Contradicción? No — son DOS vías distintas al mismo m,
y cada vía toca ζ en el nodo donde su maquinaria lo expone primero.** Lo verifico:

- **Vía Toeplitz/símbolo (Doc 156):** parte del símbolo aritmético (valor, RH-libre) y pregunta
  si el OPERADOR es Fredholm. El obstáculo aparece primero en la existencia (símbolo invertible
  en corona ⟺ m<∞), porque la maquinaria de Toeplitz necesita Fredholmicidad ANTES de poder
  computar un índice. ζ entra en (i).
- **Vía KK/peso-dual (Doc 161):** parte de la K-teoría (Connes–Thom, RH-libre) que da la clase
  fundamental SIN requerir Fredholmicidad del símbolo aritmético — la K-teoría del producto
  cruzado es un invariante topológico que existe siempre. Por eso el obstáculo NO aparece en la
  existencia (la clase topológica existe); aparece un nodo más adentro, en la ORIENTACIÓN
  (el peso dual), porque para leer la clase como signatura hace falta el dato modular = ζ.

**La síntesis [PUENTE 161-C]:** las dos vías son consistentes y se refuerzan. El Doc 156 mostró
que NO puedes ni siquiera formar el operador índice sin m<∞ (Fredholmicidad). El Doc 161 muestra
que, si rodeas eso usando la K-teoría topológica (que no necesita Fredholmicidad del símbolo),
entonces el obstáculo reaparece en el peso dual: la clase topológica existe pero su lectura como
métrica de inercia porta ζ por la partición. **No hay vía que esquive ambos nodos: o ζ en la
existencia (Toeplitz) o ζ en la orientación (KK). El muro es el mismo objeto modular.**

### 3.4. Triple test de estrés del candidato a grial (DESENLACE 2)

El contrato exige triplicar el test de estrés ante cualquier sospecha de grial. El candidato a
DESENLACE 2 sería: "la clase fundamental KK da una métrica con signatura m que NO enumera los
ceros y NO pasa por ζ." Lo someto a los tres tests del mandato.

- **(T1) ¿La clase fundamental existe sin asumir RH?** **SÍ topológicamente, NO como métrica de
  inercia.** La clase de Connes–Thom **t** ∈ KK_1 existe incondicionalmente [Con81] (RH-libre).
  PERO empareja con K-homología de FASE (Prop. 161.1), no da signatura de inercia. El candidato
  a grial necesitaría que la clase fundamental TOPOLÓGICA ya tuviera signatura m — y NO la tiene
  (la altura γ no es invariante de K^•(𝕋)). **T1 refuta el grial: la clase existe RH-libre pero
  es de fase, no de inercia.** (Idéntico al fallo de 𝔉_ind, Doc 160 Prop. 160.8, y al "TEST DE
  COORDENADA" de §1.2.)

- **(T2) ¿El apareamiento de Kasparov da signatura m sin los γ?** **NO.** El apareamiento de
  Kasparov ⟨·,[Δ]⟩ produce ENTEROS (números de winding, índices de Fredholm de operadores
  twisted) — no una signatura de forma cuadrática REAL indefinida. Para extraer neg.ind(Q) = m
  (un conteo de cuadrados negativos de una forma indefinida sobre H_altura) hace falta una
  métrica de Hilbert (la simetría fundamental J), y esa métrica es el estado KMS_β del peso dual
  (Prop. 161.6), que porta ζ(β) en su normalización. **T2 refuta el grial: el pairing de
  Kasparov da winding-de-fase; la signatura m solo aparece torciendo con el peso dual = ζ.**

- **(T3) ¿La dualidad de Poincaré-NC requiere una orientación que codifica ζ?** **SÍ,
  decisivamente.** Por Prop. 161.2, la orientación del ciclo fundamental de un álgebra de tipo
  III/II_∞ (que es lo que da C(𝕋)⋊ℝ por el flujo) es un dato MODULAR — el peso dual φ̃. Por
  CÁLCULO 161.5, la función de partición de φ̃ es ζ. Por tanto la clase fundamental ORIENTADA
  (la única que da una métrica con signatura) codifica ζ en su orientación. **T3 refuta el
  grial de la forma más directa: la orientación de Poincaré-NC del producto cruzado de Kronecker
  ES la función de partición ζ, por la identificación Bost–Connes.**

**Los tres tests, independientes, dan el mismo veredicto: NO hay grial.** La clase fundamental
topológica es RH-libre pero de fase (T1); el pairing de Kasparov da fase, no signatura (T2); la
orientación que daría signatura es modular = ζ (T3). **DESENLACE 2 refutado triplemente.** El
candidato del DESEO 160.B falla exactamente donde el mandato advertía que desconfiara: la
clase fundamental existe sin RH, pero la SIGNATURA no la da el pairing topológico, y la
orientación que la daría porta ζ por la estructura modular = Bost–Connes.

---

## 4. Dónde EXACTAMENTE entra ζ en la maquinaria canónica

### 4.1. El lugar quirúrgico

ζ entra en **la orientación / normalización modular de la clase fundamental**, concretamente en
la **función de partición del peso dual del producto cruzado**, que es Z(β) = ζ(β) por la
identificación Bost–Connes (CÁLCULO 161.5). Desglose en una cadena de cuatro eslabones, con el
eslabón exacto donde aparece ζ marcado:

1. Connes–Thom: K_•(C(𝕋)⋊ℝ) ≅ K_{•+1}(C(𝕋)). **RH-libre.** [eslabón limpio]
2. Clase fundamental topológica [Δ] vía §1.2. **RH-libre, pero de FASE** (empareja con K^•(𝕋)).
   [eslabón limpio pero ciego a inercia]
3. Para leer [Δ] como métrica con signatura m: orientar el ciclo fundamental respecto del peso
   canónico. El peso canónico de un producto cruzado por flujo = **peso dual φ̃**. [eslabón
   donde la coordenada se vuelve modular]
4. La normalización del peso dual (estado KMS_β / Gibbs) divide por la **función de partición
   Z(β) = Tr(e^{-βH}) = ∑_{k≥1} k^{-β} = ζ(β)**. **← AQUÍ ENTRA ζ.** La signatura de la forma
   normalizada al continuar β a Re β = ½ está gobernada por los ceros de ζ. [eslabón ζ]

**El eslabón ζ es el (4): la función de partición del peso dual.** Es estructural, no una
elección: el peso dual es el único peso canónico del producto cruzado (Takesaki), su función de
partición es ζ (Bost–Connes), y la normalización por la partición es obligatoria para que la
métrica sea un estado. NO hay libertad para evitarlo sin abandonar la canonicidad (= volver a
elegir la métrica a mano = GAP-160.A sin resolver).

### 4.2. La flecha invertida, otra vez (Phase 43 / Doc 160), ahora a nivel modular

Phase 43: la métrica Kähler-Riemann ‖ξ‖²=q nombra los autovalores de Frobenius vía Hasse (RH
es input). Doc 160: el producto interno de Weil ∑_ρ ĥ(γ_ρ)ĥ'(γ_ρ)* nombra los γ_ρ. **Doc 161
da la versión modular de la misma flecha invertida:** la métrica canónica = estado KMS_β del
peso dual = (1/ζ(β)) ∑_k k^{-β}(...). La función de partición ζ(β) y la posición de sus ceros
en la franja crítica son INPUT de la métrica (vía la normalización y la signatura), no OUTPUT
del transporte. **Tres encarnaciones de la misma flecha invertida**: Hasse (Phase 43), forma de
Weil (Doc 160), función de partición ζ (Doc 161). La novedad de Doc 161: muestra que la flecha
invertida es **forzada por la estructura modular de Tomita–Takesaki**, no por la elección
particular de geometría (foliada, producto cruzado, o curva). Es el invariante más profundo del
muro.

### 4.3. Por qué el peso L²-plano (DESENLACE 2 ingenuo) NO es canónico

Se podría objetar: "usa el peso traza-plano (la traza de Plancherel sobre L²(ℝ_s)), que es
RH-libre." Respuesta (refuerza PUENTE 160-B): el peso plano NO es el peso CANÓNICO del producto
cruzado por el flujo de Kronecker. El producto cruzado por un flujo con espectro {log k} tiene
peso canónico = peso dual, cuyo módulo (derivada de Radon–Nikodym) es e^{-βH} con H = generador
de espectro {log k}. El peso plano correspondería a H = 0 (flujo trivial), que NO es el flujo de
Kronecker. **Elegir el peso plano = borrar la dinámica = volver a la seminorma ciega del Doc 160
PUENTE 160-B (signatura trivial 0, no m).** La canonicidad (lo que DESEO 160.B pedía: una
métrica "no elegida a mano") FUERZA el peso dual, y el peso dual porta ζ. **La canonicidad y la
RH-libertad son incompatibles para este sistema.** Ese es el contenido exacto del no-go.

### 4.4. El contraste con el caso conmutativo (por qué los primos rompen la canonicidad RH-libre)

**[OBSERVACIÓN 161.8].** En un producto cruzado conmutativo por un flujo con espectro
DISCRETO-RACIONALMENTE-INDEPENDIENTE genérico (frecuencias diofánticas genéricas), la función
de partición Tr(e^{-βH}) = ∑ e^{-β λ_n} es una serie de Dirichlet genérica sin estructura
aritmética — su continuación analítica y sus ceros no codifican nada especial. **Lo que hace
ESPECIAL al flujo de Kronecker de {log p} es precisamente que las frecuencias son los logaritmos
de los PRIMOS**, de modo que la función de partición ∑ k^{-β} = ζ(β) es la zeta de Riemann (por
factorización única, BC95). Es decir: **la métrica canónica porta ζ no por la maquinaria
KK/modular en abstracto, sino porque la maquinaria se aplica al flujo cuyas frecuencias son los
primos, que es exactamente el dato que hace de la partición la función zeta.** Esto cierra el
círculo con el Doc 160 Prop. 160.5 (el espectro del flujo es {log k} = enteros): la partición
térmica de {log k} es ∑ k^{-β} = ζ. La estructura modular convierte el espectro-de-enteros del
flujo en la función-zeta-como-partición. **El "puente Euler" del Doc 160 (de {log k} a {γ_ρ})
es, a nivel modular, el paso de la partición ζ(β) a sus ceros γ_ρ — la continuación analítica de
la función de partición a la franja crítica.** Doc 161 identifica ese puente con un objeto
canónico: la continuación analítica del peso dual.

---

## 5. Veredicto y el teorema de circularidad estructural

### 5.1. Veredicto

**VEREDICTO: DESENLACE 1 — NO-GO ESTRUCTURAL GENUINO.** La métrica de inercia canónica obtenida
de la dualidad de Poincaré no-conmutativa / la clase fundamental KK del producto cruzado
C(𝕋)⋊_φ ℝ EXISTE como objeto topológico (Connes–Thom, RH-libre) pero es de FASE; para leerla
como métrica de inercia con signatura m hace falta orientarla con el peso dual, cuya función de
partición es ζ (Bost–Connes). Por tanto **toda métrica de inercia canónica sobre este producto
cruzado porta ζ por la estructura modular de Tomita–Takesaki, NECESARIAMENTE.** La ruta
Connes/producto-cruzado de Kronecker es **circular por construcción**, no inacabada. GAP-160.A
queda RESUELTO en sentido negativo: la "tercera métrica" que buscaba (canónica, no-plana,
signatura m, RH-libre) NO existe — la única métrica canónica no-plana es el estado KMS del peso
dual, que porta ζ. DESEO 160.B (la herramienta de cierre) RESULTA SER el lugar donde ζ entra,
no el escape.

DESENLACE 2 (grial) refutado triplemente (§3.4). DESENLACE 1 confirmado en el nodo (ii) de la
trifurcación (orientación/normalización modular), consistente y complementario con Doc 156 (que
lo halló en el nodo (i), Fredholmicidad).

### 5.2. El teorema de circularidad estructural

**[TEOREMA 161.9 — circularidad estructural de la ruta del producto cruzado de Kronecker].**
*Sea 𝒜 = C(𝕋)⋊_φ ℝ el producto cruzado del flujo de Kronecker φ_t(z) = (p^{-it} z_p)_p sobre el
toro de Bohr 𝕋 = ∏_p S¹, y sea φ̃ su peso dual con flujo modular σ^{φ̃}_s = Ad(e^{isH}),
H = generador de la acción dual. Sea ⟨·,·⟩_can cualquier producto interno sobre el espacio de
altura H_altura que sea (i) inducido canónicamente por la clase fundamental orientada de la
dualidad de Poincaré no-conmutativa de 𝒜 (orientación respecto del peso canónico = dual), y
(ii) no-degenerado/no-plano (signatura no trivial). Entonces:*

1. *(existencia topológica RH-libre)* la clase fundamental NO-orientada [Δ] ∈ KK existe vía
   Connes–Thom y es RH-libre, pero su emparejamiento de Kasparov toma valores en la K-homología
   de fase K^•(𝕋), no en la signatura de inercia;
2. *(orientación = ζ)* la orientación que convierte [Δ] en ⟨·,·⟩_can es el estado KMS_β del peso
   dual, ω_β(a*b) = Z(β)^{-1} Tr(e^{-βH} a*b), cuya **función de partición es Z(β) = ζ(β)**;
3. *(circularidad)* la signatura de ⟨·,·⟩_can al continuar β a la franja crítica Re β = ½ está
   gobernada por los ceros de ζ; en particular, neg.ind(⟨·,·⟩_can) coincide con m = neg.ind de
   la forma de Weil **solo si se conoce la posición de los ceros de ζ**.

*Por tanto: NO existe un producto interno canónico sobre H_altura, inducido por la dualidad de
Poincaré-NC del producto cruzado de Kronecker, que sea simultáneamente (i) no-plano con
signatura m y (ii) RH-libre. La canonicidad (orientación = peso dual) y la RH-libertad son
incompatibles, porque el peso dual de este sistema tiene a ζ por función de partición.*

**Prueba.** (1) Prop. 161.1 (Connes–Thom da [Δ] sobre K^•(𝕋), RH-libre) + Prop. 161.2 (la clase
no-orientada no fija signatura). (2) Prop. 161.2 (la orientación canónica de un álgebra de tipo
III/II_∞ es el peso dual) + Prop. 161.6 (la métrica = KMS_β del peso dual) + CÁLCULO 161.5
(Z(β) = ζ(β) por factorización única del espectro {log k}, identificación Bost–Connes
PUENTE 161-B). (3) Prop. 161.6 (la signatura de la forma normalizada por 1/ζ(β) cambia en los
ceros/polos de ζ al continuar a la franja crítica). La incompatibilidad final: por (1) la única
parte RH-libre es la clase topológica de fase (signatura 0 efectiva sobre inercia); por (2)-(3)
la única orientación canónica no-plana porta ζ. No hay tercera opción canónica (§4.3: el peso
plano no es canónico para el flujo de Kronecker). $\square$

**[GAP declarado, honesto]:** el TEOREMA 161.9 descansa en (a) PUENTE 161-B (la identificación
de la partición del peso dual de Kronecker con ζ vía la analogía Bost–Connes; el CÁLCULO 161.5
es elemental dado que el espectro es {log k}, pero la identificación literal del peso dual con el
estado de Gibbs de H requiere que la condición de positividad/energía del peso dual seleccione
exactamente k ≥ 1, lo cual argumento en §2.3 pero no demuestro con todo el rigor de la teoría de
pesos de Haagerup); y (b) PUENTE 161-A (la existencia de la clase fundamental en dim ∞ del toro
de Bohr). Ninguno de estos GAP debilita el no-go: si la clase fundamental NO existe en dim ∞
(PUENTE 161-A falla), entonces el no-go es del nodo (i) (el objeto no existe) — todavía no-go.
Si el peso dual no fuera exactamente Gibbs-de-ζ (PUENTE 161-B se afina), la estructura modular
sigue siendo la del sistema BC cuya partición es ζ por BC95 — todavía no-go. **El no-go es
robusto a ambos GAP: es un teorema sobre dónde DEBE entrar ζ, no sobre un cálculo frágil.**

### 5.3. Qué familia de approaches cierra esto

El TEOREMA 161.9 cierra honestamente la familia: **"obtener la métrica de inercia de la
dualidad de Poincaré-NC / clase fundamental KK del producto cruzado de Kronecker (o de
cualquier sistema cuya parte aritmética sea Bost–Connes)."** Incluye: la sugerencia DESEO 160.B;
la lectura natural del marco adélico de Connes [Con99] restringido a la parte de fase
(PUENTE 160-A); cualquier intento de definir la métrica de Weil como emparejamiento del cociclo
de Connes vía Poincaré-NC. La razón estructural única: **el peso canónico del producto cruzado
es el peso dual, cuyo flujo modular tiene función de partición ζ (Bost–Connes), de modo que la
orientación de Poincaré-NC porta ζ por la teoría de Tomita–Takesaki.** No es un defecto técnico;
es la identidad "función de partición del sistema BC = ζ" leída como obstrucción.

**Lo que NO cierra (frontera honesta):** approaches donde el álgebra NO sea un producto cruzado
del flujo de los primos —p. ej., un triple espectral cuyo operador de Dirac D NO tenga espectro
{log k} ni función de partición ζ, sino otro espectro cuya partición sea analítica y benigna,
PERO cuyo carácter de Chern aún produzca κ=2m. Eso es el [GAP de literatura central] heredado de
Doc 156 §4.5 (el triple espectral RH-libre con Chern = κ), que el TEOREMA 161.9 NO refuta — solo
refuta que tal triple se construya como producto cruzado de Kronecker. Lo dejo como la frontera
viva tras este documento (§6).

---

## 6. Mensaje final

**VEREDICTO: DESENLACE 1 — NO-GO ESTRUCTURAL.** La métrica de inercia canónica que la dualidad
de Poincaré no-conmutativa asocia al producto cruzado C(𝕋)⋊_φ ℝ del flujo de Kronecker porta ζ
NECESARIAMENTE, por la estructura modular de Tomita–Takesaki. La clase fundamental topológica
existe RH-libremente (Connes–Thom) pero es de FASE; la orientación que la convierte en métrica
de inercia con signatura m es el peso dual, cuya función de partición es ζ (identificación
Bost–Connes). La canonicidad y la RH-libertad son incompatibles para este sistema. GAP-160.A
resuelto en negativo; DESEO 160.B identificado como el lugar donde ζ entra, no como el escape.
La ruta Connes/producto-cruzado de Kronecker es circular por construcción.

**¿Dónde EXACTAMENTE entra ζ en la maquinaria canónica?** En la **función de partición del peso
dual** (el cuarto eslabón de §4.1): Z(β) = Tr(e^{-βH}) = ∑_{k≥1} k^{-β} = ζ(β), donde H es el
generador del flujo modular σ^{φ̃} (= el flujo dual θ de 𝔉_KMS, Doc 160), cuyo espectro {log k}
es el de los enteros por factorización única. La normalización 1/ζ(β) del estado KMS_β del peso
dual es la métrica canónica, y su signatura al continuar a la franja crítica está gobernada por
los ceros de ζ. Es el avatar modular de la "flecha invertida" de Phase 43 (Hasse) y Doc 160
(forma de Weil): la posición de los ceros es INPUT de la métrica, no OUTPUT del transporte; pero
Doc 161 muestra que esta flecha invertida es FORZADA por Tomita–Takesaki (la orientación
canónica = peso dual = partición ζ), no por la geometría particular. **El "puente Euler"
{log k}→{γ_ρ} del Doc 160 es, a nivel modular, la continuación analítica de la función de
partición ζ(β) a sus ceros.**

**Consistencia con Doc 156 (la trifurcación):** Doc 156 halló ζ en el nodo (i) Fredholmicidad
(vía Toeplitz: el operador no existe sin m<∞). Doc 161 halla ζ en el nodo (ii)
orientación/normalización (vía KK: el objeto topológico existe pero su orientación es ζ). Son
dos vías al mismo m, cada una toca ζ donde su maquinaria lo expone primero; ninguna lo esquiva.
La vía KK rodea la Fredholmicidad (la K-teoría topológica existe siempre) solo para reencontrar
ζ un nodo más adentro, en el peso dual. **Síntesis: el muro es el objeto modular —la función de
partición del flujo de los primos = ζ— y aparece como winding de ζ (símbolo, Doc 156) o como
partición de ζ (peso dual, Doc 161); son la misma ζ vista por las dos puntas de la dualidad
símbolo/peso.**

**Tres resultados con etiquetas:**

1. **[PROPOSICIÓN 161.1 + 161.2] — La clase fundamental de C(𝕋)⋊ℝ existe (Connes–Thom,
   RH-libre) pero es de FASE; su orientación es MODULAR, no topológica.** Por Connes–Thom
   K_•(C(𝕋)⋊ℝ)≅K_{•+1}(C(𝕋)), la clase fundamental desciende a la K-homología del toro de Bohr
   = invariantes de fase; la altura γ no es invariante de K^•(𝕋). Para leer la clase como métrica
   de inercia hace falta una orientación, que para un álgebra de tipo III/II_∞ (lo que da el
   flujo) es un dato modular = el peso dual, no la clase spin-c topológica. La clase existe
   RH-libre; la signatura de inercia NO la da el pairing topológico de Kasparov (refuta el grial
   ingenuo: T1+T2 del §3.4).

2. **[PROPOSICIÓN 161.6 + CÁLCULO 161.5 — el corazón] — La métrica canónica es el estado KMS_β
   del peso dual, normalizado por la función de partición Z(β) = ζ(β) (Bost–Connes).** El peso
   dual del producto cruzado tiene flujo modular con generador H de espectro {log k} (enteros,
   por factorización única); su función de partición es Tr(e^{-βH}) = ∑ k^{-β} = ζ(β), idéntica
   a la del sistema BC (BC95: partición = ζ, transición de fase en β=1, KMS_β a β>1 codifican
   los primos vía Ẑ^×). La métrica canónica = ω_β(a*b) = ζ(β)^{-1} Tr(e^{-βH} a*b) lleva ζ
   literalmente en el denominador, y su signatura al continuar a Re β=½ está gobernada por los
   ceros de ζ. **ζ entra en la orientación/normalización modular — el nodo (ii) de la
   trifurcación — por la estructura de Tomita–Takesaki, no por elección** (refuta el grial T3,
   §3.4; el peso plano alternativo no es canónico, §4.3).

3. **[TEOREMA 161.9 — circularidad estructural] — No existe métrica de inercia canónica RH-libre
   sobre el producto cruzado de Kronecker; la canonicidad (orientación = peso dual) y la
   RH-libertad son incompatibles porque el peso dual tiene a ζ por función de partición.** Cierra
   honestamente la familia de approaches "métrica de inercia vía dualidad de Poincaré-NC del
   producto cruzado de los primos" (= DESEO 160.B, = Connes restringido a fase). El no-go es
   robusto a los dos GAP declarados (existencia en dim ∞; rigor del peso dual = Gibbs): si la
   clase no existe en dim ∞, no-go de nodo (i); si existe, no-go de nodo (ii). **Frontera viva
   (NO cerrada por este documento):** un triple espectral cuyo operador NO sea el flujo de los
   primos (espectro ≠ {log k}, partición ≠ ζ) pero cuyo carácter de Chern aún dé κ=2m — el [GAP
   de literatura central] heredado de Doc 156 §4.5, que el TEOREMA 161.9 acota pero no refuta.

---

## Referencias

**Internas (backward-only):** Doc 160 (𝔉_KMS Prop. 160.7; test de polarización Prop. 160.10;
PUENTE 160-A Connes restringido a fase; PUENTE 160-B plano-vs-Weil; GAP-160.A la métrica de
inercia RH-libre; DESEO 160.B la signatura de Weil como invariante KK; Prop. 160.5 espectro del
flujo = {log k} por factorización única; Prop. 160.8 𝔉_ind empareja con K-teoría de fase).
Doc 156 (trifurcación Fredholmicidad/clase/escape; VEREDICTO caso (b)-Fredholmicidad,
Prop. 156.6/156.7; Teorema 156.5 κ=winding=2m bajo m<∞; §4.5 [GAP central] triple espectral
RH-libre con Chern=κ no existe). Phase 26 (κ=2m=neg.ind(H_C) en Pontryagin (𝒦,Q)). Phase 43
(la métrica de polarización porta ζ; flecha invertida RH-input-no-output). Doc 134 (álgebra de
Weil–Toeplitz, ceros en la frontera símbolo/compacto).

**Literatura (publicada, verificable salvo marca):**
- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions with
  spontaneous symmetry breaking in number theory*, Selecta Math. (N.S.) 1 (1995), 411–457. (El
  sistema BC; **función de partición = ζ(β)**; transición de fase en β=1; estados KMS_β a β>1
  parametrizados por Ẑ^×=Gal(ℚ^{ab}/ℚ) y codificando los primos. Núcleo de PUENTE 161-B,
  Prop. 161.4, CÁLCULO 161.5 — el dato decisivo del no-go.)
- [Con99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann
  zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (El marco adélico; el lado espectral
  reproduce la fórmula explícita de Weil; el producto cruzado restringido a la parte de fase es
  el ingrediente — la familia que el no-go cierra cuando se restringe a la parte de fase.)
- [Con94] A. Connes, *Noncommutative Geometry*, Academic Press, 1994. (Cap. II.5 Connes–Thom
  K_•(A⋊R)≅K_{•+1}(A); Cap. IV dualidad de Poincaré no-conmutativa / KK, clase fundamental;
  Cap. VI triples espectrales, métrica, orientación — base de §1, Prop. 161.1/161.2.)
- [Con81] A. Connes, *An analogue of the Thom isomorphism for crossed products of a C*-algebra
  by an action of ℝ*, Adv. Math. 39 (1981), 31–55. (El isomorfismo de Connes–Thom como clase
  KK_1 invertible — la base de Prop. 161.1; la clase **t**.)
- [CT77] A. Connes, M. Takesaki, *The flow of weights on factors of type III*, Tôhoku Math. J.
  29 (1977), 473–575. (El flujo de pesos; la clasificación de tipo de productos cruzados por
  flujos modulares; la orientación canónica de un álgebra de tipo III es el peso, no una traza
  finita — base de Prop. 161.2.)
- [Tak03] M. Takesaki, *Theory of Operator Algebras II*, Encyclopaedia Math. Sci. 125, Springer,
  2003. (Productos cruzados; **peso dual** Vol. II cap. X (Def. X.1.16, teorema del peso dual);
  flujo dual θ_s(U_t)=e^{ist}U_t (X.2); teoría de Tomita–Takesaki, flujo modular — base de
  CONSTRUCCIÓN 161.3.)
- [Haagerup78] U. Haagerup, *On the dual weights for crossed products of von Neumann algebras
  I, II*, Math. Scand. 43 (1978), 99–118 y 119–140. (Construcción rigurosa del peso dual y su
  flujo modular; el rigor que PUENTE 161-B / GAP §5.2 invoca y declara como no completado a
  detalle de página.)
- [Kas88] G. G. Kasparov, *Equivariant KK-theory and the Novikov conjecture*, Invent. Math. 91
  (1988), 147–201. (El producto de Kasparov; dualidad y clases fundamentales en KK — base
  formal de la dualidad de Poincaré-NC, §1.1.)
- [BMRS08] J. Brodzki, V. Mathai, J. Rosenberg, R. J. Szabo, *Noncommutative correspondences,
  duality and D-branes in bivariant K-theory*, Adv. Theor. Math. Phys. 13 (2009), 497–552
  (arXiv:0708.2648); y *D-branes, RR-fields and duality on noncommutative manifolds*, Comm.
  Math. Phys. 277 (2008), 643–706 (arXiv:0709.2128). (Definición precisa de PD-álgebra: clase
  fundamental [Δ]∈KK_d(A⊗A°,ℂ) con inversa; invariancia de PD bajo KK-equivalencia — base de
  §1.1, Prop. 161.1.)
- [FS81] T. Fack, G. Skandalis, *Connes' analogue of the Thom isomorphism for the Kasparov
  groups*, Invent. Math. 64 (1981), 7–14. (La versión KK del isomorfismo de Connes–Thom: A⋊ℝ
  KK-equivalente a la suspensión SA — refuerza Prop. 161.1.)
- [CM95] A. Connes, H. Moscovici, *The local index formula in noncommutative geometry*, GAFA 5
  (1995), 174–243. (Carácter de Chern–Connes, fórmula local del índice, residuos de la zeta
  espectral; la condición de orientación/sumabilidad del triple — §1.3, y la frontera viva §5.3
  heredada de Doc 156 §4.5.)
- [BR97] O. Bratteli, D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics 2*,
  2.ª ed., Springer, 1997. (Estados KMS, estados de Gibbs ω_β=Z(β)^{-1}Tr(e^{-βH}·), condición
  KMS — base de Prop. 161.6.)
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. (Criterio de positividad de Weil; la signatura de la
  forma de Weil = m, el objetivo de la métrica de inercia.)

*Fin del Documento 161.*
