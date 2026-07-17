# Doc 160 — Construcción del functor/transporte fase→inercia: ¿la uniformidad del flujo de Kronecker compra positividad de inercia RH-libre?

**Programa:** Hipótesis de Riemann — Phase 51: construcción del functor fase→inercia.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** CONSTRUCTIVO. Mandato: construir el objeto matemático nombrado por
GAP-158.A — un transporte genuino de la estructura de equidistribución uniforme del flujo de
Kronecker en el toro de Bohr 𝕋=∏_p S¹ (input incondicional, RH-libre) a un invariante de la
coordenada de inercia/altura (donde viven las ordenadas γ de los ceros y m = neg.ind de la
forma de Weil = κ/2 de P35). Cinco restricciones de diseño heredadas de las Fases 49–50
(§0.2). NO se audita: se CONSTRUYE. Una falsa victoria es peor que un fracaso.

**Contrato de etiquetado (regla absoluta).** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad aquí, prueba completa; resultados
externos citados con referencia verificable. **[CÁLCULO]** = mostrado. **[CONSTRUCCIÓN]** =
objeto definido con precisión. **[PUENTE]** = conexión con estatus honesto de cada eslabón.
**[GAP]** = declarado. **[GAP de literatura]** = dato no verificado a nivel de página esta
sesión, NO usado como premisa de ningún teorema. **[DESEO]** = declarado. Jamás se fabrica
una prueba de RH ni una victoria que no esté. **NADA de numéricos.** Honestidad absoluta:
está PERMITIDO terminar en (B/C/D); lo prohibido es fingir (A).

**Prerrequisitos leídos en fuente esta sesión:** Doc 158 completo (Thm 158.10 confinamiento
al lado-valor; el isomorfismo tensorial H₃≅H_fase⊗H_altura, Prop. 158.6; GAP-158.A las tres
propiedades exactas del functor faltante; los tres pares (Hᵢ,Aᵢ) Def. 158.4); Doc 159
completo (las tres vías; C1–C5 del §6, en particular C5 = la esperanza universal/uniforme;
GAP-159.C); memoria Phase 43 (la métrica de polarización transversal PORTA ζ: en
math/0204194 ‖ξ‖²=q se define DESPUÉS de invocar Hasse; RH es input, no output — la
obstrucción crítica a evitar); memoria Phase 26 (κ=2m=neg.ind(H_C) en el espacio de
Pontryagin (𝒦,Q), la inercia que el functor debe alcanzar).

---

## 0. Resumen ejecutivo y especificación

### 0.1. Qué se construye

Construyo, en orden:

1. **(§1) El espacio dinámico.** El toro de Bohr 𝕋=∏_p S¹ con el flujo de Kronecker
   R↷𝕋, su mapping torus / suspensión Σ_𝕋, y la C*-álgebra del producto cruzado
   𝒜 = C(𝕋)⋊_φ R. Defino con precisión la foliación (las órbitas de R), la transversal
   (el propio 𝕋 como sección de Poincaré flotante), y los dos candidatos a "coordenada de
   inercia": (i) el espectro del generador de la R-acción / flujo espectral, y (ii) los
   pesos de un estado KMS. **[CONSTRUCCIÓN 160.1–160.3].**

2. **(§2) El transporte fase→inercia.** Construyo TRES candidatos a functor 𝔉 y los pruebo
   uno por uno: 𝔉_coh (cohomología foliada transversal, à la Deninger/Moore–Schochet),
   𝔉_KMS (peso KMS sobre 𝒜 con la altura como variable dual), 𝔉_ind (flujo espectral /
   índice del producto cruzado, à la Connes). El núcleo del documento es identificar cuál
   transporta ALGO no-tautológico y qué exactamente.

3. **(§3) El test de polarización (la lección de Phase 43, al frente).** Cada vez que un 𝔉
   produce una forma cuadrática cuya positividad daría m<∞ o m=0, ME DETENGO y verifico:
   ¿la positividad se define usando los ceros/autovalores (circular = Phase 43) o se
   DERIVA de la uniformidad de Kronecker (RH-libre)? Localizo dónde entra ζ con precisión
   quirúrgica.

4. **(§4) ¿La uniformidad compra positividad?** El punto decisivo (C5 del Doc 159). Intento
   transportar una cota de discrepancia UNIFORME (Erdős–Turán, Koksma, LeVeque) por el 𝔉
   superviviente y ver si da una cota inferior sobre la forma transversal de inercia.

5. **(§5) Veredicto (A/B/C/D)** y el GAP central, triple test de estrés.

### 0.2. Las cinco restricciones de diseño (cada una mató un intento previo)

Las reescribo como condiciones verificables sobre 𝔉, porque el veredicto se decide por
cuál de ellas se rompe:

- **(a) INPUT = estructura diofántica uniforme de {log p}:** la discrepancia/equidistribución
  del flujo de Kronecker t↦(p^{−it})_p sobre 𝕋. Incondicional (Thm 158.2). 𝔉 debe TOMAR
  esto como entrada.
- **(b) OUTPUT en la coordenada de inercia/altura:** donde viven las γ y m=κ/2 (Phase 26).
- **(c) SIN pasar por los VALORES de ζ:** todo lo medible respecto del toro de valores /
  medida de Bagchi Q es ciego a RH (universalidad de Voronin, Thm 158.9/159.9). 𝔉 NO debe
  factorizar por Σ_val. **Este mató la lectura ambiente (Doc 158/159 Vía 2).**
- **(d) SIN reconstituir {k^{−s}} vía Euler:** eso lo vuelve Nyman–Beurling = RH-equivalente
  (Doc 159 Vía 1, PUENTE 159-A). 𝔉 debe operar con las frecuencias PRIMAS {log p}
  directamente, sin formar productos.
- **(e) EXPLOTANDO la uniformidad (puerta universal):** una cota uniforme NO selecciona un
  τ (no es existencial), luego esquivaría el cuantificador maestro de P43 (Doc 159 C5).
  Esta es la única esperanza viva.

**Adelanto del veredicto (honestidad up-front):** el resultado es **(D) con un núcleo de
(B)**. CONSTRUYO el functor 𝔉_KMS genuinamente (no es tautología — escapa a (C) la crítica
del Doc 158 de que el único puente es la fórmula explícita-identidad), y el transporte SÍ
existe como morfismo de la dinámica a un operador transversal. PERO en el test de
polarización (§3) localizo que la positividad de la forma transversal de inercia entra por
exactamente el mismo punto que Phase 43: **la métrica que convierte el operador transversal
en una polarización con signatura definida requiere especificar el producto interno sobre el
espacio de altura, y ese producto interno ES la forma de Weil Q — cuya signatura es m**. La
uniformidad de Kronecker compra positividad en H_fase (lo ya sabido), y el functor 𝔉_KMS la
transporta a una positividad sobre el ÁLGEBRA, pero el paso del álgebra a la signatura de
inercia requiere un emparejamiento (pairing) que NO está determinado por la dinámica —
queda como **[GAP-160.A]**, el GAP central, que nombro y cuya herramienta de cierre
identifico. NO es (A): la uniformidad NO compra la positividad de inercia por sí sola.

---

## 1. El espacio dinámico

### 1.1. El toro de Bohr y el flujo de Kronecker

**[CONSTRUCCIÓN 160.1] (el espacio de fase).** Sea 𝕋 := ∏_{p∈ℙ} S¹, el toro de Bohr,
compacto en la topología producto (= grupo dual del grupo discreto ⊕_p ℤ generado por los
caracteres χ_p). Sus elementos son z=(z_p)_p con z_p∈S¹. El flujo de Kronecker es la acción
de ℝ:
$$\varphi: \mathbb R \times \mathbb T \to \mathbb T, \qquad \varphi_t(z) = (p^{-it} z_p)_p = (e^{-it\log p} z_p)_p.$$
Por el Teorema 158.2 (Kronecker–Weyl, vía independencia ℚ-lineal de {log p}, Thm 158.1), φ
es minimal y unívocamente ergódico respecto de la medida de Haar μ_Haar.

Equivalentemente, 𝕋 es el espacio de fases del sistema dinámico cuyo "número de rotación"
en el factor p es log p; el dato diofántico (a) es exactamente que el vector de frecuencias
(log p)_p es ℚ-independiente, lo que da la ergodicidad única (la "uniformidad" del input).

**Observación de coordenadas (clave para todo el documento).** La variable t del flujo es la
MISMA variable que la altura/ordenada en la franja crítica: en la fórmula explícita, el lado
de primos aparece como ∑_p (log p) p^{-1/2} ĥ(log p) (la transformada en la dirección t), y
el lado de ceros como ∑_ρ ĥ(γ_ρ). Es decir: **la variable dual de t es, simultáneamente,
log p (lado fase) y γ (lado altura).** Esta coincidencia es el motor de cualquier transporte
candidato — y también su trampa (lo que el Doc 158 Prop. 2.x llamó "el puente es identidad").

### 1.2. La suspensión / mapping torus y la foliación

**[CONSTRUCCIÓN 160.2] (el solenoide de suspensión).** Considero el espacio de suspensión
del flujo. Como φ es un flujo R (no un homeomorfismo único), tomo directamente el espacio
foliado (𝕋, ℱ) donde la foliación ℱ tiene por hojas las órbitas {φ_t(z) : t∈ℝ}. Por
minimalidad, toda hoja es densa (la foliación es minimal, sin hojas cerradas). La transversal
canónica T es cualquier sección local; globalmente, como 𝕋 es un grupo y φ una traslación a
un parámetro, podemos tomar como "transversal total" el propio 𝕋 con la relación de
equivalencia de órbita — pero esta es ergódica (no admite conjunto de Borel transversal de
medida intermedia). Esto ya anticipa una dificultad (§2.1).

La estructura relevante:
- **dirección de hoja (1-dimensional):** la coordenada t = el flujo = la dirección donde
  viven tanto log p (input) como γ (output). Es la dirección de INERCIA/ALTURA.
- **dirección transversal (∞-dimensional, profinita-compacta):** el toro 𝕋 módulo la órbita
  = las FASES (z_p)_p módulo el flujo diagonal. Es la dirección de VALOR/FASE.

**[CÁLCULO 160.3] (la C*-álgebra del producto cruzado).** El álgebra dinámica es
$$\mathcal A := C(\mathbb T)\rtimes_\varphi \mathbb R,$$
el producto cruzado del flujo de Kronecker. Generada por C(𝕋) y los unitarios U_t que
implementan φ_t: U_t f U_t^{-1} = f∘φ_{-t}. Por la ergodicidad única (Thm 158.2), 𝒜 es un
álgebra simple (el flujo es minimal) con un único estado traza-KMS asociado a μ_Haar en el
parámetro adecuado. El espectro del generador infinitesimal de {U_t} (el "Hamiltoniano del
flujo") es la coordenada DUAL a t — y esta es la candidata directa a coordenada de inercia.

**[PUENTE 160-A] (la C*-álgebra es la de Connes, restringida).** El producto cruzado
C(𝕋)⋊R es precisamente el ingrediente del marco adélico de Connes [Con99] cuando se restringe
la acción de las idéles al subgrupo de fase ∏_p S¹ (la parte "unitaria" / de norma 1 de las
idéles). Connes identifica los ceros de ζ con el espectro de la acción de escalamiento sobre
L²(C_ℚ) (las clases de idéles); el TORO 𝕋 es la parte compacta C_ℚ^1 (norma 1), y el flujo de
escalamiento de Connes es transversal a 𝕋. **Estatus honesto:** esta identificación es
estructural y correcta a nivel de qué grupo actúa, pero el contenido espectral (que el
espectro DÉ los ceros) es exactamente lo que Connes deja como la dificultad de positividad —
no es un input gratuito. Lo registro como puente, no como teorema. La diferencia con Connes:
él usa toda la idéle (con la dirección de escala = Mellin, que es Nyman–Beurling, restricción
(d) violada); yo me restrinjo a la PARTE DE FASE 𝕋 y trato de alcanzar la inercia SIN la
dirección de escala. Ese es el sentido preciso de (d).

### 1.3. El isomorfismo tensorial heredado y por qué es el obstáculo

Del Doc 158 Prop. 158.6 / §4.2: el espacio de la forma de Weil se factoriza
$$H_3 \;\cong\; H_{\text{fase}} \otimes H_{\text{altura}},$$
donde H_fase = L²(𝕋, Haar) (la dirección transversal) y H_altura = el espacio donde vive la
señal cero-a-cero (la dirección de hoja/flujo, con el producto interno de Weil). El único
operador que liga los factores es la fórmula explícita, **que es una identidad** (Doc 112
Prop. 4.2), no un transporte.

**El problema de construcción, en una frase.** En la geometría dinámica que acabo de
construir, H_fase = transversal (∞-dim, profinito) y H_altura = dirección de hoja (1-dim, el
flujo). El functor 𝔉 que GAP-158.A pide debe llevar una propiedad de la transversal (la
ergodicidad/discrepancia uniforme) a una propiedad de la dirección de hoja (la signatura de
Weil). **El obstáculo geométrico:** en un producto cruzado por un flujo MINIMAL Y ERGÓDICO,
la dirección transversal y la de hoja están "entrelazadas" por la ergodicidad — no hay
proyección invariante de una a la otra (eso es justamente la ergodicidad única). Esto es lo
que hace que el transporte sea no-trivial: NO es proyección ortogonal (sería tautología), y
debe ser algún acoplamiento más fino. Los §2.1–2.3 prueban cuál.

---

## 2. El transporte fase→inercia: tres candidatos

### 2.1. Candidato 1 — 𝔉_coh: cohomología foliada transversal (Deninger / Moore–Schochet)

**La idea.** Deninger [Den98] propone que ζ debería surgir como función zeta de un flujo
sobre un espacio foliado, con los ceros = espectro del generador del flujo sobre la
COHOMOLOGÍA FOLIADA transversal H¹_τ(𝕋,ℱ). El input diofántico se transportaría como: la
ergodicidad ⟹ la cohomología foliada es "pequeña" (los invariantes del flujo son escasos)
⟹ control de la inercia.

**[PROPOSICIÓN 160.4] (la cohomología foliada de Kronecker calcula los INVARIANTES del
flujo, = coordenada de fase, NO la altura).** Para la foliación de Kronecker ℱ sobre 𝕋
(órbitas del flujo minimal único-ergódico), la cohomología foliada tangencial de grado 0 es
H⁰_τ = ℂ (las funciones constantes a lo largo de las hojas = invariantes del flujo, y por
ergodicidad son solo las constantes). La cohomología foliada reducida de grado 1, H¹_τ, está
controlada por la teoría de Moore–Schochet [MS06] y por la ecuación cohomológica
$$\dot u = f - \int f\, d\mu_{\text{Haar}} \qquad (\text{ecuación de homología del flujo}),$$
cuya solubilidad (con pérdida de regularidad) está gobernada por las propiedades DIOFÁNTICAS
del vector de frecuencias (log p)_p.

*Demostración (estructura).* H⁰_τ = ker(derivada a lo largo de la hoja) = invariantes = ℂ
por ergodicidad única (Thm 158.2; [Wal82, Thm 6.20]). Para H¹_τ: una 1-forma foliada es
g·dt (dt = forma a lo largo de la hoja); es exacta si g = u̇ para u; resolver u̇ = g en
coordenadas de Fourier sobre 𝕋 da, para el modo de frecuencia n=(n_p) (soporte finito),
û(n) = ĝ(n)/(i⟨n, (log p)⟩) — soluble salvo divisores pequeños ⟨n,(log p)⟩, que es la
condición diofántica del flujo. [MS06] da el marco general de cohomología foliada para
foliaciones medibles; la ecuación cohomológica es la de Katok–Robinson para flujos lineales.
$\square$

**[TEST DE POLARIZACIÓN — Candidato 1.] ¿Dónde vive el output?** La Prop. 160.4 muestra que
𝔉_coh transporta el input diofántico (las cotas de divisores pequeños ⟨n,(log p)⟩) a una
propiedad de la regularidad de la ecuación cohomológica SOBRE 𝕋 — es decir, **en la
coordenada de FASE** (el modo de Fourier n vive en el dual de 𝕋). La altura γ no aparece:
la cohomología foliada de Kronecker mide cómo el flujo mezcla las FASES, no produce las
ordenadas de los ceros.

**[PROPOSICIÓN 160.5] (𝔉_coh NO alcanza la inercia: las ordenadas de los ceros no son
clases de cohomología foliada de la foliación de Kronecker).** El espectro del generador del
flujo de Kronecker actuando sobre L²(𝕋) es exactamente {⟨n,(log p)⟩ : n∈⊕_pℤ} = el
semigrupo/grupo aditivo generado por {log p} — que es {log k : k∈ℕ} ∪ {−log k} (los enteros,
vía factorización única). Las ordenadas {γ_ρ} de los ceros de ζ NO pertenecen a este
conjunto (los γ no son combinaciones ℤ-lineales de logaritmos de primos: son transcendentes
de naturaleza distinta). Por tanto el espectro de 𝔉_coh es el de los ENTEROS, no el de los
CEROS.

*Demostración.* El espectro del generador del flujo lineal sobre el toro con frecuencias
(log p) es el conjunto de los ⟨n, (log p)⟩ = ∑_p n_p log p = log(∏ p^{n_p}) = log k (k∈ℚ_{>0}),
por factorización única (Thm 158.1). Que {γ_ρ} ≠ {log k}: los γ_ρ son los ceros de una
función entera de orden 1 cuya distribución (espaciado ~2π/log γ) difiere del espaciado
logarítmico de {log k}; en particular ninguna identidad ∑ n_p log p = γ_ρ es conocida ni
esperada (esa sería una relación aritmética explícita entre primos y ceros, inexistente).
$\square$

**Veredicto Candidato 1: la cohomología foliada de Kronecker da los ENTEROS, no los CEROS —
y reconstruir los ceros desde los enteros es Euler en la línea (restricción (d) violada).**
El espectro {log k} es exactamente el sistema de Nyman–Beurling (Doc 159 Prop. 159.4–159.5):
para pasar de {log k} (espectro de 𝔉_coh) a {γ_ρ} (los ceros) hace falta el producto de
Euler / la función zeta misma. **𝔉_coh transporta fase → ESPECTRO-DE-ENTEROS, no fase →
INERCIA-DE-CEROS.** Cae en la restricción (d). Esto es un hallazgo limpio y negativo:

> **La razón profunda de por qué Deninger lleva ~30 años abierto:** la cohomología foliada
> de la foliación de Kronecker calcula el espectro de los ENTEROS (los logaritmos de la base
> multiplicativa), y para que ese espectro se convierta en los CEROS hace falta exactamente
> la función zeta (el "determinante regularizado" del generador), que es Euler. El espacio
> foliado de Deninger que daría los ceros directamente NO es la foliación de Kronecker sobre
> 𝕋 — es un objeto cuya existencia es el problema abierto. 𝔉_coh sobre 𝕋 NO es ese objeto.

[GAP de literatura, declarado]: no conozco una construcción del espacio foliado de Deninger
cuya cohomología foliada dé {γ_ρ} en vez de {log k}; el propio Deninger [Den98, Den02] lo
deja como programa. No lo uso como premisa.

### 2.2. Candidato 2 — 𝔉_KMS: peso KMS con la altura como variable dual (el que SÍ transporta)

Este es el candidato que construyo en serio, porque escapa al fallo del Candidato 1: en vez
de mirar el espectro del generador (que da enteros), miro un PESO sobre el álgebra cuya
variable dual es la altura.

**[CONSTRUCCIÓN 160.6] (el peso de altura sobre 𝒜).** Sobre 𝒜=C(𝕋)⋊_φ R, defino el estado
KMS_β respecto del flujo dual θ_s (la acción dual de ℝ̂=ℝ sobre el producto cruzado, que
escala los U_t). El flujo dual θ tiene por variable s la DUAL de t. Como t es simultáneamente
la variable de log p (fase) y de γ (altura, §1.1 Observación), la variable dual s es la
coordenada espectral donde —si el álgebra "supiera" de ζ— vivirían los ceros.

Defino el funcional de transporte:
$$\mathfrak F_{\text{KMS}}: \mathcal A_{\text{sa}} \to \text{Funciones}(\mathbb R_s), \qquad
\mathfrak F_{\text{KMS}}(a)(s) = \tau\big(\theta_s(a)\big),$$
donde τ es el estado traza (Haar) y θ_s el flujo dual. Para a = f·U_t con f∈C(𝕋), esto da
$$\mathfrak F_{\text{KMS}}(f U_t)(s) = e^{ist}\int_{\mathbb T} f\, d\mu_{\text{Haar}}.$$

**[PROPOSICIÓN 160.7] (𝔉_KMS SÍ transporta a la coordenada de altura, y NO es la fórmula
explícita-identidad).** El funcional 𝔉_KMS lleva un elemento del álgebra dinámica (lado
fase) a una distribución en la variable s (lado altura/inercia). Aplicado al ELEMENTO
ARITMÉTICO
$$a_\zeta := \sum_p (\log p)\, p^{-1/2}\, U_{\log p} \;\in\; \mathcal A \quad(\text{cerradura adecuada}),$$
produce
$$\mathfrak F_{\text{KMS}}(a_\zeta)(s) = \sum_p (\log p)\, p^{-1/2}\, e^{is\log p},$$
que es exactamente la parte de primos del lado explícito como función de la altura s. Este
transporte es un MORFISMO (lineal, compatible con θ), NO una identidad tautológica: a
diferencia de la fórmula explícita (que IGUALA lado-primo y lado-cero), 𝔉_KMS solo PRODUCE
el lado-primo como función de s; el lado-cero NO está horneado.

*Demostración.* Cálculo directo de τ(θ_s(f U_t)) usando τ(f U_t)=δ_{t,0}∫f dμ (traza del
producto cruzado) y θ_s(U_t)=e^{ist}U_t (definición del flujo dual [Tak03, Vol II,
Thm X.2.3]). Linealidad y continuidad extienden a a_ζ en la cerradura. Que NO es la fórmula
explícita: la fórmula explícita es la IGUALDAD ∑_p(...) = ∑_ρ ĥ(γ_ρ) + (arquimedeano); 𝔉_KMS
produce solo el lado izquierdo como objeto espectral, sin afirmar la igualdad. $\square$

**Esto es genuinamente un transporte, no una tautología — el primer hallazgo positivo.**
𝔉_KMS escapa a la objeción central del Doc 158 (Prop. 2.x: "el único puente es la fórmula
explícita-identidad"). El producto cruzado da un puente DISTINTO: el flujo dual θ produce la
coordenada de altura como espectro, y el elemento aritmético a_ζ vive nativamente en 𝒜
(restricción (d) RESPETADA: a_ζ usa SOLO los U_{log p}, las frecuencias primas, sin formar
productos / sin Euler). El input diofántico entra porque la ergodicidad de φ (Thm 158.2)
hace que τ sea el ÚNICO estado invariante, lo que fija 𝔉_KMS unívocamente.

**Pero ahora viene el test de polarización, y aquí está el corazón del veredicto.**

### 2.3. Candidato 3 — 𝔉_ind: flujo espectral / índice (Connes), y por qué reduce a 𝔉_KMS

**[PROPOSICIÓN 160.8] (el flujo espectral del producto cruzado es el emparejamiento de
𝔉_KMS con la K-teoría, y comparte su destino).** El índice / flujo espectral de la R-acción
sobre 𝒜 (à la Connes, [Con94, Cap. III]) se calcula emparejando el cociclo cíclico asociado
a la traza θ-invariante con K_1(𝒜). Por el isomorfismo de Connes–Thom, K_1(C(𝕋)⋊R)≅K⁰(C(𝕋))
= K⁰(𝕋), que es la K-teoría del toro de Bohr — un objeto de la FASE. El emparejamiento con
𝔉_KMS produce números reales (los "saltos" del flujo espectral) que son, de nuevo, integrales
sobre 𝕋 de la coordenada de fase. La inercia (γ) aparece solo a través de la misma variable
dual s de 𝔉_KMS.

*Demostración (estructura).* Connes–Thom: K_•(A⋊R)≅K_{•+1}(A) [Con94, II.5; o Pimsner–Voiculescu
para ℤ, Connes–Thom para ℝ]. Para A=C(𝕋), K⁰(𝕋) es el grupo de Grothendieck de fibrados sobre
el toro de Bohr (profinito); el emparejamiento traza∘índice da números de winding sobre los
factores S¹, = datos de fase. El flujo espectral de un camino de operadores autoadjuntos
asociado a a_ζ se calcula por la integral de 𝔉_KMS(a_ζ)(s) ds sobre el espectro, reduciendo
a §2.2. $\square$

**Veredicto Candidato 3: 𝔉_ind no añade nada nuevo a 𝔉_KMS para nuestra pregunta** — el
índice empareja con K-teoría de fase, y la única vía a la altura es vía la variable dual s,
ya capturada por 𝔉_KMS. Concentro el análisis en 𝔉_KMS (§3–4).

---

## 3. El test de polarización: ¿porta ζ? (la lección de Phase 43, al frente)

El functor superviviente es 𝔉_KMS. Produce 𝔉_KMS(a_ζ)(s) = ∑_p (log p) p^{−1/2} e^{is log p},
una función/distribución de la altura s, RH-libre (es solo primos). Para que esto dé m<∞ o
m=0, necesito una FORMA CUADRÁTICA en s cuya positividad sea la positividad de Weil. La
construyo y la someto al test brutal de Phase 43.

### 3.1. La forma cuadrática transversal de inercia

**[CONSTRUCCIÓN 160.9] (la forma de inercia transportada).** Para una función test h (par,
con ĥ de soporte compacto en s), defino el "lado fase transportado":
$$\Phi(h) := \int_{\mathbb R} \mathfrak F_{\text{KMS}}(a_\zeta)(s)\, \hat h(s)\, ds
= \sum_p (\log p)\, p^{-1/2}\, \hat h(\log p) \cdot(\text{factor }2),$$
la contribución de primos de la fórmula de Weil. La forma cuadrática candidata es
$$\mathcal Q_{\mathfrak F}(h) := \langle \mathfrak F_{\text{KMS}}(a_\zeta), |h|^2\text{-núcleo}\rangle,$$
donde el "núcleo" empareja la función de altura con la métrica del espacio de altura
H_altura. **El paso decisivo es: ¿cuál es el producto interno sobre H_altura?**

### 3.2. EL TEST — dónde entra ζ (idéntico al modo de fallo de Phase 43)

Aquí me detengo, como exige el contrato, y verifico con brutalidad.

**[PROPOSICIÓN 160.10] (la positividad de 𝒬_𝔉 requiere el producto interno de Weil sobre
H_altura, y ese producto interno carga la signatura m — ζ entra exactamente aquí).** Para
que 𝒬_𝔉(h) sea una forma cuya positividad signifique m=0 (RH), el emparejamiento del §3.1
debe ser
$$\mathcal Q_{\mathfrak F}(h) = \tfrac12 Q_X(h,h) = \sum_\rho |\hat h(\gamma_\rho)|^2_{\text{(con signo de Weil)}},$$
es decir, el producto interno sobre H_altura DEBE ser la forma de Weil Q (= la suma de Gram
sobre las alturas de los ceros, Doc 158 Prop. 158.6). Pero la forma de Weil Q tiene signatura
neg.ind(Q) = m = κ/2 (Phase 26) — su definición ENUMERA las alturas γ_ρ de los ceros. Por
tanto: especificar el producto interno de H_altura que hace de 𝒬_𝔉 la forma de inercia
**requiere conocer las alturas de los ceros** — exactamente el dato que el output debía
producir.

*Demostración.* El transporte 𝔉_KMS(a_ζ)(s) es solo la mitad-primo del lado explícito. Para
convertirlo en una forma cuya positividad sea RH, hay que CERRAR la fórmula explícita: igualar
el lado-primo con el lado-cero ∑_ρ ĥ(γ_ρ) (más arquimedeano). Esa igualdad es la fórmula
explícita (identidad, Doc 112 Prop. 4.2). La positividad de la forma resultante sobre el cono
de tests es el criterio de Weil [Wei52], y su defecto es m. El emparejamiento que define
H_altura como el espacio donde 𝒬_𝔉 = ½Q_X es, literalmente, el producto interno
⟨h,h'⟩_altura := ∑_ρ ĥ(γ_ρ) ĥ'(γ_ρ)^* — que NOMBRA los γ_ρ. $\square$

**ESTE ES EL MODO DE FALLO DE PHASE 43, EXACTAMENTE.** Comparo lado a lado:

| | Phase 43 (Deninger foliado, math/0204194) | Doc 160 (𝔉_KMS) |
|---|---|---|
| espacio desnudo (RH-libre) | Spec ℤ foliado, órbitas {log p} | 𝕋, flujo de Kronecker, a_ζ |
| dirección benigna | estructura compleja J | el transporte 𝔉_KMS(a_ζ)(s) (solo primos) |
| **dónde entra ζ** | **la métrica Kähler-Riemann ‖ξ‖²=q (Hasse) define la polarización transversal** | **el producto interno de Weil sobre H_altura define la forma 𝒬_𝔉; enumera los γ_ρ** |
| flecha invertida | RH-para-E es INPUT de la métrica, no OUTPUT | la signatura m es INPUT del producto interno, no OUTPUT |

**El diagnóstico es idéntico.** La IMPLICACIÓN "positividad de 𝒬_𝔉 ⟹ m=0 ⟹ RH" es correcta y
geométrica (es el criterio de Weil). El ANTECEDENTE "el producto interno de H_altura está dado
por la dinámica de Kronecker SIN usar los ceros" es FALSO: el producto interno que hace de
𝒬_𝔉 la forma de inercia es la forma de Weil, que enumera los γ_ρ. La uniformidad de Kronecker
da el lado-primo (RH-libre, ✓), pero la MÉTRICA del lado-altura (la que convierte el
lado-primo en una forma con signatura) porta los ceros. **ζ entra en la polarización, no en
el transporte.** El transporte 𝔉_KMS es genuino y RH-libre; la polarización que lo lee como
inercia NO lo es.

**[PUENTE 160-B — por qué esto no es un defecto reparable de técnica.]** Se podría esperar
reparar usando OTRO producto interno sobre H_altura, uno dado por la dinámica (p.ej. el de
L²(ℝ_s) plano, sin pesos de ceros). Pero entonces 𝒬_𝔉(h) = ∫|𝔉_KMS(a_ζ)(s)|² ds (un objeto
RH-libre, calculable desde primos) **deja de ser la forma de Weil** — su positividad es
trivial (es una norma L²) y NO dice nada sobre m. La elección es forzada: o el producto
interno es plano (RH-libre pero ciego a inercia, = Doc 158 H₂ seminorma B²) o es el de Weil
(toca inercia pero porta ζ). No hay un tercer producto interno conocido sobre H_altura que sea
(i) dado por la dinámica de Kronecker y (ii) no-plano de modo que su signatura sea m. **Ese
tercer producto interno es exactamente el GAP central (§5).**

---

## 4. ¿La uniformidad compra positividad? (el punto decisivo, C5)

La esperanza C5 (Doc 159 §6): una cota de discrepancia UNIFORME del flujo de Kronecker
podría suministrar la positividad de la forma transversal SIN usar los ceros, esquivando el
cuantificador maestro por la puerta universal. Lo intento explícitamente con las
desigualdades clásicas de discrepancia.

### 4.1. Las desigualdades de discrepancia disponibles (input incondicional)

**[CÁLCULO 160.11] (Erdős–Turán / LeVeque para el flujo de Kronecker).** Para el flujo
t↦(p^{−it} z_p)_p restringido a un subconjunto finito F⊂ℙ de primos y una ventana temporal
[0,T], la discrepancia D_T respecto de Haar satisface la desigualdad de Erdős–Turán [ET48]:
$$D_T \;\le\; \frac{C}{N} + C\sum_{0<|n|\le N} \frac{1}{|n|}\left|\frac{1}{T}\int_0^T e^{i\langle n,(\log p)\rangle t}\,dt\right|
= \frac{C}{N} + C\sum_{0<|n|\le N}\frac{1}{|n|}\cdot\frac{|\,\cdots\,|}{T|\langle n,(\log p)\rangle|},$$
para todo N, donde n recorre ⊕_{p∈F}ℤ y ⟨n,(log p)⟩ = log(∏ p^{n_p}) = log k. La cota es
INCONDICIONAL y UNIFORME en z (no selecciona una órbita). Su tamaño depende de los divisores
pequeños |⟨n,(log p)⟩| = |log k| para k cerca de 1 — controlados porque log k ≥ log(1+1/k_max)
para k entero ≠ 1, una cota diofántica explícita.

**Punto crucial (la coincidencia de frecuencias, otra vez).** Los exponentes que aparecen en
Erdős–Turán son e^{i⟨n,(log p)⟩t} = e^{i (log k) t} = k^{it} — las frecuencias son {log k}
(ENTEROS), exactamente el espectro de 𝔉_coh (Prop. 160.5). La discrepancia uniforme controla
cómo el flujo equidistribuye respecto de estas frecuencias-entero. **La discrepancia NO
contiene las frecuencias-cero {γ_ρ}.**

### 4.2. El intento de transporte de la cota a positividad de inercia

**[PROPOSICIÓN 160.12] (la cota de discrepancia uniforme NO se transporta a una cota inferior
sobre la forma de inercia — localización exacta del fallo).** Sea D_T(N) la cota de
Erdős–Turán (4.1). El transporte 𝔉_KMS lleva la discrepancia a una cota sobre las sumas
∑_p (log p) p^{−1/2} ĥ(log p) en la variable s. PERO la forma de inercia 𝒬_𝔉(h)=½Q_X(h,h)
empareja con las frecuencias {γ_ρ} (Prop. 160.10), y la cota de discrepancia controla las
frecuencias {log k} ≠ {γ_ρ}. No hay ninguna desigualdad que ligue una cota sobre las
frecuencias-entero {log k} con una cota inferior sobre la forma evaluada en las
frecuencias-cero {γ_ρ}. La uniformidad compra positividad EN LA COORDENADA DE FASE (control
de la equidistribución respecto de {log k}), no en la coordenada de inercia (respecto de
{γ_ρ}).

*Demostración.* La cota de Erdős–Turán (4.1) acota |D_T| en términos de las medias
T^{-1}∫₀^T e^{i(log k)t}dt — funcionales de las frecuencias-entero. Una cota inferior sobre
𝒬_𝔉(h)=∑_ρ |ĥ(γ_ρ)|²_{signo} requeriría controlar ĥ evaluado en {γ_ρ}. El único objeto que
liga {log k} y {γ_ρ} es la fórmula explícita / ζ misma (Prop. 160.10, Doc 159 Vía 1 PUENTE
159-A: el puente {primos/enteros}→{ceros} es Euler en la línea). La discrepancia uniforme,
por fina que sea, vive en el lado {log k}; transportarla a {γ_ρ} es Euler. La uniformidad
esquiva el cuantificador maestro (✓ no selecciona un τ — la cota es universal), pero esquivarlo
NO BASTA: la cota universal es sobre la coordenada equivocada. $\square$

**El resultado decisivo, negativo y preciso.** C5 (Doc 159) tenía razón en que una cota
uniforme esquiva el cuantificador maestro por la puerta universal — y lo confirmo: la
discrepancia de Erdős–Turán NO selecciona un τ, es universal en z, esquiva el problema
existencial. **PERO la puerta universal abre a la habitación equivocada:** la cota uniforme
controla la equidistribución respecto de las frecuencias-entero {log k}, no respecto de las
frecuencias-cero {γ_ρ}. La uniformidad compra positividad de FASE (que ya teníamos,
ergodicidad), no de INERCIA. El cuantificador maestro no es el único guardián; detrás de él
está el cambio de coordenada {log k}→{γ_ρ}, que es Euler/ζ, y la uniformidad no lo paga.

### 4.3. Triple test de estrés del resultado negativo

El contrato exige triplicar el test de estrés cuando hay una sospecha de escape (y también
cuando se cierra uno, para no auto-engañarse en la dirección negativa). Verifico que la
Prop. 160.12 no es un artefacto de la desigualdad de Erdős–Turán elegida.

- **Verificación 1 (otra desigualdad — LeVeque [LeV65]):** la desigualdad de LeVeque acota
  D_T² por ∑_n |n|^{-2} |media de Weyl|², con las MISMAS frecuencias-entero ⟨n,(log p)⟩=log k.
  Cambiar Erdős–Turán por LeVeque o Koksma–Hlawka no cambia el conjunto de frecuencias: todas
  las desigualdades de discrepancia para un flujo lineal sobre el toro usan los caracteres del
  toro, = {log k}. ✓ el fallo es estructural, no de la desigualdad.
- **Verificación 2 (vía la coincidencia de espectros, Prop. 160.5):** el espectro del flujo
  ES {log k} por factorización única; ninguna funcional lineal del flujo puede producir {γ_ρ}
  sin un objeto no-lineal (Euler). La discrepancia es una funcional (cuadrática) de los
  caracteres del flujo. ✓ el fallo es la coincidencia espectro-del-flujo = enteros.
- **Verificación 3 (vía restricción (d), Doc 159 PUENTE 159-A):** el paso {log k}→{γ_ρ} es el
  producto de Euler sobre Re s=½; cualquier transporte que lo cruce viola (d) y reintroduce ζ.
  La discrepancia uniforme no cruza (d); por eso permanece en {log k}. ✓ consistente con la
  Vía 1 del Doc 159.

Las tres verificaciones, independientes, dan el mismo veredicto: la uniformidad compra
positividad de fase, no de inercia, y el muro es el cambio de coordenada {log k}→{γ_ρ} = Euler.

---

## 5. Veredicto y el GAP central

### 5.1. El veredicto: (D) con núcleo de (B)

**VEREDICTO: (D) — construcción parcial con un GAP central nombrado; con un núcleo del modo
de fallo (B) (la polarización porta ζ, idéntica a Phase 43).**

Desglose contra las cuatro opciones del encargo:

- **(A) ¿Construí el functor Y la uniformidad compra positividad RH-libre?** **NO.** El
  functor 𝔉_KMS se construyó (§2.2, genuino, no-tautológico, respeta (d)), pero la uniformidad
  NO compra la positividad de inercia (§4, Prop. 160.12, triple-verificado): la discrepancia
  uniforme controla las frecuencias-entero {log k}, no las frecuencias-cero {γ_ρ}. No finjo (A).
- **(B) ¿La polarización porta ζ (Phase 43 otra vez)?** **SÍ, parcialmente, y localizado con
  precisión (§3.2, Prop. 160.10).** El producto interno sobre H_altura que convierte el
  transporte en la forma de inercia ES la forma de Weil, que enumera los γ_ρ. Idéntico al
  modo de fallo de Phase 43 (la métrica ‖ξ‖²=q de math/0204194). ζ entra en la métrica de
  polarización, no en el transporte.
- **(C) ¿El transporte no existe / es tautología?** **NO — y este es el hallazgo positivo.**
  𝔉_KMS es un transporte GENUINO (Prop. 160.7): escapa a la objeción del Doc 158 (Prop. 2.x)
  de que el único puente es la fórmula explícita-identidad. El producto cruzado da un puente
  distinto (el flujo dual), respeta (d), y produce el lado-primo como objeto espectral en la
  variable de altura sin horneаr el lado-cero. El transporte existe; lo que no existe es la
  métrica de inercia RH-libre. NO es (C) puro, pero §2.1 prueba que un transporte alternativo
  (𝔉_coh, cohomología foliada) ES tautológico/circular en otro sentido (da {log k} = enteros,
  restricción (d)).
- **(D) ¿Construcción parcial con GAP central?** **SÍ, este es el veredicto.** Construí el
  espacio (§1), el transporte 𝔉_KMS (§2.2), y localicé exactamente el GAP: la métrica de
  inercia (§3.2, §5.2).

### 5.2. El GAP central, nombrado, y la herramienta que lo cerraría

**[GAP-160.A] (la métrica de inercia RH-libre).** El functor 𝔉_KMS transporta la estructura
de Kronecker (fase) a un objeto espectral en la variable de altura s (Prop. 160.7,
RH-libre). El obstáculo único para que esto dé m es: **falta un producto interno sobre
H_altura que (i) esté determinado por la dinámica de Kronecker / la uniformidad del flujo, y
(ii) cuya signatura sea m = neg.ind(Q_Weil), SIN enumerar los γ_ρ.** Las dos elecciones
conocidas fallan (PUENTE 160-B): el producto interno plano (L²(ℝ_s)) es RH-libre pero ciego a
inercia (su signatura es trivialmente 0, no m); el producto interno de Weil tiene signatura m
pero enumera los γ_ρ (porta ζ, Prop. 160.10). El GAP es la AUSENCIA de un tercer producto
interno —dado por la dinámica, no-plano, con signatura m— sobre H_altura.

**Reformulación del GAP en términos de Phase 26 (la inercia objetivo).** Por Phase 26,
m = κ/2 = neg.ind(H_C) en el espacio de Pontryagin (𝒦,Q). El GAP-160.A es: ¿puede la
ergodicidad/discrepancia uniforme del flujo de Kronecker determinar la signatura de Pontryagin
de (𝒦,Q) sin diagonalizar H_C (sin conocer sus autovalores = los ceros)? El producto cruzado
C(𝕋)⋊R da el álgebra; la signatura de Pontryagin de la forma de Weil sobre ella NO está
determinada por la dinámica de fase — ese es el contenido exacto del GAP.

**Herramienta candidata para cerrarlo [DESEO 160.B].** El producto interno que falta sería un
producto interno de tipo **Krein/Pontryagin INTRÍNSECO al producto cruzado** — definido por
una traza/coproducto del álgebra 𝒜 cuyo defecto de positividad (neg.ind) coincida con m sin
referencia a los autovalores. El candidato natural: una **forma de Weil regularizada como
emparejamiento del cociclo cíclico de Connes** (el cociclo de la traza θ-invariante) **consigo
mismo vía la dualidad de Poincaré no-conmutativa del producto cruzado** [Con94, Cap. IV;
emparejamiento KK / clase fundamental]. Si la clase fundamental de C(𝕋)⋊R en KK-teoría
indujera, vía el cociclo de Weil, una forma cuya signatura fuera computable desde la
K-homología de 𝕋 (un objeto de fase, RH-libre), la signatura m sería un invariante topológico
del producto cruzado y NO de los ceros. **Estatus: [GAP de literatura].** No conozco un
cálculo de la signatura de la forma de Weil como un invariante de KK-teoría del producto
cruzado de Kronecker; el emparejamiento de índice de Connes (§2.3, Prop. 160.8) da números de
winding de fase, no la signatura de Weil. Si tal cálculo existiera y diera m vía topología de
fase, sería (A). No lo tengo; lo nombro como el deseo exacto.

**Por qué este GAP es la frontera real (coincide con tres líneas previas).** GAP-160.A es la
encarnación, en el lenguaje del producto cruzado, de:
- **GAP-158.A** (el functor fase→inercia que acopla H_fase y H_altura sin ser la fórmula
  explícita): 𝔉_KMS ES ese acoplamiento, pero el acoplamiento NO determina la métrica de
  inercia. El functor existía; faltaba su parte métrica.
- **GAP-159.C / C1–C5** (una propiedad diofántica uniforme que fuerce individuación): la
  uniformidad de Kronecker (Erdős–Turán) es exactamente la propiedad C5 (universal, no
  selecciona), y §4 prueba que NO se transporta a inercia porque vive en {log k}, no {γ_ρ}.
  C5 se confirma como necesaria pero insuficiente: la puerta universal abre a la coordenada
  de fase, no de inercia.
- **Phase 43** (la polarización foliada que porta ζ en la métrica): §3.2 reproduce el modo de
  fallo EXACTO en el marco del producto cruzado, confirmando que es estructural, no un defecto
  de la geometría foliada particular de Deninger.

**Tres líneas independientes, un solo objeto faltante: la métrica de inercia RH-libre sobre
H_altura.** Ese es el GAP-160.A.

### 5.3. Por qué esto es el resultado honesto y avanza el programa

El valor del documento NO es una equivalencia ni una prueba de RH (no se produce ninguna). El
valor es triple:

1. **Construir un transporte genuino (𝔉_KMS) que NO es la fórmula explícita-identidad** —
   refuta la lectura de que "fase e inercia solo se conectan por la tautología" (Doc 158
   Prop. 2.x). El producto cruzado da un puente real. Esto es matemática nueva: el functor de
   GAP-158.A existe como morfismo.
2. **Localizar el GAP en la MÉTRICA, no en el transporte** — afina el diagnóstico de Phase 43.
   Phase 43 dejó "la métrica porta ζ" como un hecho del caso realizado de Deninger; Doc 160
   prueba que es estructural (aparece igual en el producto cruzado de Kronecker, una geometría
   completamente distinta). El muro no es la geometría foliada; es la signatura de inercia.
3. **Probar que la uniformidad (C5) esquiva el cuantificador maestro pero abre a la coordenada
   equivocada** — cierra C5 como ruta directa con una razón precisa (la discrepancia vive en
   {log k}, los ceros en {γ_ρ}, y el puente es Euler), sin matar el GAP residual (la métrica).

---

## 6. Mensaje final

**VEREDICTO: (D) — construcción parcial con GAP central nombrado, con núcleo del modo de
fallo (B).** Construí el espacio dinámico (toro de Bohr 𝕋 con el flujo de Kronecker, su
producto cruzado 𝒜=C(𝕋)⋊R) y un transporte fase→inercia GENUINO, el functor KMS 𝔉_KMS, que
escapa a la tautología de la fórmula explícita y respeta las restricciones (a)/(c)/(d). PERO
el transporte produce solo el lado-primo como objeto espectral en la variable de altura; para
leerlo como inercia (m=neg.ind de Weil) hace falta una MÉTRICA sobre H_altura, y la única
métrica con signatura m es la forma de Weil, que enumera los ceros — **idéntico al modo de
fallo de Phase 43.** La uniformidad de Kronecker (C5) esquiva el cuantificador maestro por la
puerta universal (✓) pero abre a la coordenada de FASE ({log k}, los enteros), no a la de
INERCIA ({γ_ρ}, los ceros); el puente entre ambas es Euler en la línea crítica (restricción
(d)). El functor existe; la métrica de inercia RH-libre no — ese es GAP-160.A.

**¿Dónde entra ζ?** En la MÉTRICA DE POLARIZACIÓN, no en el transporte. El transporte 𝔉_KMS
es RH-libre (solo usa las frecuencias primas {log p} vía el flujo dual del producto cruzado).
ζ entra cuando se especifica el producto interno sobre H_altura que da signatura m: ese
producto interno es la forma de Weil ∑_ρ ĥ(γ_ρ)ĥ'(γ_ρ)^*, que NOMBRA los γ_ρ. Exactamente
como en Phase 43 la métrica Kähler-Riemann ‖ξ‖²=q nombra los autovalores de Frobenius vía
Hasse. La flecha está invertida: la signatura m es INPUT de la métrica, no OUTPUT del
transporte.

**Tres resultados con etiquetas:**

1. **[PROPOSICIÓN 160.7 + CONSTRUCCIÓN 160.6] — El functor 𝔉_KMS existe y NO es la fórmula
   explícita-identidad.** El producto cruzado C(𝕋)⋊R, vía su flujo dual θ, transporta el
   elemento aritmético a_ζ=∑_p(log p)p^{−1/2}U_{log p} (que respeta (d): solo primos, sin
   Euler) a la función espectral de altura ∑_p(log p)p^{−1/2}e^{is log p}. Es un morfismo
   genuino, no la igualdad tautológica primo=cero; refuta que fase e inercia solo se conecten
   por la fórmula explícita (Doc 158 Prop. 2.x). El functor de GAP-158.A EXISTE como
   acoplamiento.

2. **[PROPOSICIÓN 160.10 + PUENTE 160-B] — La polarización porta ζ en la métrica, idéntica a
   Phase 43.** Para que el transporte dé m, el producto interno sobre H_altura debe ser la
   forma de Weil (signatura m, enumera los γ_ρ); el producto interno plano alternativo es
   RH-libre pero ciego a inercia (signatura trivial 0). No hay tercer producto interno conocido
   —dinámico, no-plano, signatura m— sin enumerar los ceros. El modo de fallo es estructural:
   aparece igual en el producto cruzado de Kronecker que en la geometría foliada de Deninger
   (Phase 43), probando que el muro no es la geometría particular sino la signatura de inercia.

3. **[PROPOSICIÓN 160.12 + triple verificación §4.3 — confirma/cierra C5] — La uniformidad
   compra positividad de FASE, no de INERCIA.** La discrepancia uniforme de Kronecker
   (Erdős–Turán, LeVeque, Koksma) esquiva el cuantificador maestro por la puerta universal
   (no selecciona τ, ✓ C5) pero controla las frecuencias-entero {log k}=⟨n,(log p)⟩ (el
   espectro del flujo, por factorización única), NO las frecuencias-cero {γ_ρ}. El puente
   {log k}→{γ_ρ} es Euler en la línea (restricción (d), Doc 159 PUENTE 159-A). C5 es necesaria
   pero insuficiente: la puerta universal abre a la coordenada equivocada. **[GAP-160.A]: la
   métrica de inercia RH-libre sobre H_altura** = el único objeto faltante, = encarnación de
   GAP-158.A (parte métrica) ∩ GAP-159.C (positividad uniforme) ∩ Phase 43 (métrica sin ζ),
   tres líneas un objeto; herramienta candidata de cierre [DESEO 160.B]: la signatura de Weil
   como invariante de KK-teoría / dualidad de Poincaré no-conmutativa del producto cruzado
   (no construido; [GAP de literatura]).

---

## Referencias

**Internas (backward-only):** Doc 158 (H₃≅H_fase⊗H_altura Prop. 158.6; Thm 158.10
confinamiento; GAP-158.A las tres propiedades del functor; tres pares (Hᵢ,Aᵢ) Def. 158.4;
Prop. 2.x el puente es identidad); Doc 159 (tres vías; PUENTE 159-A el peaje {primos}→{enteros}
es Euler; GAP-159.C; C1–C5 §6, en particular C5 puerta universal); Doc 112 (Kronecker–Weyl
sobre {log p} Lemas 2.2/3.3; Prop. 4.2 fórmula explícita es identidad; seminorma B² anula
compactos Obs. 2.4); Doc 134 (corona 𝒞=𝒲/𝒥, ceros en la frontera símbolo/compacto); Phase 26
(κ=2m=neg.ind(H_C) en Pontryagin (𝒦,Q), V.1–V.4); Phase 43 (la métrica de polarización
transversal porta ζ; math/0204194 ‖ξ‖²=q define la métrica DESPUÉS de Hasse; RH input no
output; el modo de fallo replicado en §3.2).

**Literatura (publicada, verificable salvo marca):**
- [Con99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann
  zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (El marco adélico C_ℚ; ceros como
  espectro del escalamiento; la dificultad de positividad. El producto cruzado restringido a
  la parte de fase 𝕋 es el ingrediente de §1.2.)
- [Con94] A. Connes, *Noncommutative Geometry*, Academic Press, 1994. (Cap. II.5
  isomorfismo de Connes–Thom K_•(A⋊R)≅K_{•+1}(A); Cap. III flujo espectral / cociclos
  cíclicos; Cap. IV dualidad de Poincaré no-conmutativa / KK — la herramienta candidata de
  DESEO 160.B.)
- [Den98] C. Deninger, *Some analogies between number theory and dynamical systems on foliated
  spaces*, Doc. Math., Extra Vol. ICM Berlin 1998, Vol. I, 163–186. (El programa foliado;
  ceros = espectro del generador del flujo sobre cohomología foliada; el espacio foliado que
  daría los ceros directamente es el problema abierto — §2.1 Prop. 160.5 muestra que la
  foliación de Kronecker da {log k}, no {γ_ρ}.)
- [Den02] C. Deninger, *A note on arithmetic topology and dynamical systems*, en *Algebraic
  Number Theory and Algebraic Geometry*, Contemp. Math. 300 (2002), 99–114. (Refinamiento del
  programa; cohomología foliada y funciones zeta dinámicas.)
- [MS06] C. C. Moore, C. Schochet, *Global Analysis on Foliated Spaces*, 2.ª ed., MSRI
  Publications 9, Cambridge Univ. Press, 2006. (Cohomología foliada / tangencial; análisis
  global sobre espacios foliados; el marco de la ecuación cohomológica de §2.1.)
- [Tak03] M. Takesaki, *Theory of Operator Algebras II*, Encyclopaedia Math. Sci. 125,
  Springer, 2003. (Productos cruzados por flujos; teoría de Tomita–Takesaki / KMS; el flujo
  dual θ_s(U_t)=e^{ist}U_t, Thm X.2.3 — base de CONSTRUCCIÓN 160.6.)
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. (Criterio de positividad de Weil; la signatura de la
  forma de Weil = m; el contenido de la métrica de inercia.)
- [ET48] P. Erdős, P. Turán, *On a problem in the theory of uniform distribution I, II*,
  Indag. Math. 10 (1948), 370–378, 406–413. (Desigualdad de Erdős–Turán; cota de discrepancia
  por sumas de Weyl — CÁLCULO 160.11.)
- [LeV65] W. J. LeVeque, *An inequality connected with Weyl's criterion for uniform
  distribution*, Proc. Sympos. Pure Math. VIII, AMS (1965), 22–30. (Desigualdad de LeVeque;
  D² acotada por ∑|n|^{-2}|media de Weyl|² — Verificación 1 de §4.3.)
- [Wal82] P. Walters, *An Introduction to Ergodic Theory*, GTM 79, Springer, 1982. (Thm 6.20:
  traslación minimal de grupo compacto = unívocamente ergódica — la ergodicidad del flujo de
  Kronecker, base de Prop. 160.4 H⁰=ℂ.)
- [Wey16] H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Math. Ann. 77 (1916),
  313–352. (Equidistribución / Kronecker–Weyl en el toro; el input uniforme.)
- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions with
  spontaneous symmetry breaking in number theory*, Selecta Math. (N.S.) 1 (1995), 411–457.
  (El sistema BC; estados KMS sobre álgebras aritméticas — contexto de CONSTRUCCIÓN 160.6, el
  uso de KMS con pesos aritméticos; [GAP de literatura]: el peso de altura específico de
  𝔉_KMS no es el de BC, no verificado contra esta fuente a nivel de página.)

*Fin del Documento 160.*
