# Doc 108 — El puente criba→índice: formulación, inventario incondicional y medición de la distancia

**Phase 36 — Formas A/B/C · junio 2026**
**Autor: David Alejandro Trejo Pizzo**
**Prerrequisitos:** P42 (§6: Lema Faltante 6.1 "sieve-to-index bridge", pasos (1)–(3) y sus falsadores); Doc 107 (W₂, clase engrosada, nueve bloques, Teoremas 3.4, 4.2, 4.4, 5.5, Prop. 6.1, Lema Faltante 7.2); Doc 106 (§3 Prop. 3.4/3.5, lema de esterilidad Prop. 3.6, Lemas Faltantes 5.2/5.3); Doc 99 (patrón de transmutación, discriminador I2a); Doc 96 (Teorema 8.1); Doc 94 (condición C5); P41 (no-go unidimensional: interior controlado / frontera = RH).
**Regla absoluta:** ninguna prueba se fabrica. Cada paso es demostración completa, cálculo cerrado, o GAP declarado. Sin numéricos, sin simulaciones.

---

## 0. Resumen ejecutivo

Este documento ejecuta el **paso (1)** del Lema Faltante 6.1 de P42 (el puente criba→índice)
y mide la distancia entre la cota de criba disponible y la cota que el puente necesita.
Resultado en una línea: **la distancia no es una constante ni un logaritmo: es el paso de
"en media sobre ventanas" a "uniforme en ventanas", y ese paso es RH re-encodeada. PUENTE
MUERTO**, con la localización exacta del muro en §7 y la transmutación documentada en §8.

Hallazgos principales, en orden:

1. **(§2) El problema variacional está bien planteado pero el invariante "relativo" no es
   funcional-accesible.** κ(Q₂^rel) = 8m² (el bloque off×off) es una compresión espectral.
   Lo que la clase de prueba ve son **índices por ventanas** de la forma completa Q₂, y
   bajo ¬RH esos índices crecen: en la ventana de altura T de la variable suma,
   κ_W(Q₂) ≈ 2m·n_W con n_W ≍ |W|·(log T)/π (Proposición 2.6: contaminación off×on,
   el mecanismo de la Prop. 6.1 del Doc 107 localizado por ventanas). Bajo RH, κ_W = 0
   para toda ventana. **El índice test-accesible es binario: 0 para toda ventana (RH) o
   no acotado sobre ventanas (¬RH).** Cualquier teorema incondicional
   "sup_W κ_W ≤ f(2) < ∞" es, por tanto, equivalente a RH ya en k = 2: la frontera del
   no-go de P41 reaparece dentro de la forma doble.

2. **(§3) Respuesta al falsador del paso (1): ni "el aritmético controla" ni "el
   arquimediano domina" — el arquimediano domina exactamente en el régimen donde el
   índice es invisible.** En el libro mayor con signos
   Q₂ = [DD+AA+PP+PA+AP] − [DP+PD+DA+AD], el bloque casi-primo entra con **signo
   positivo** (a diferencia del funcional de Weil de una variable, donde el lado primo se
   resta). Con soportes fijos y altura de ventana T → ∞, todos los bloques primos y
   polares son O_sop(log T) mientras AA ~ c·(log T)² > 0: la forma es definida positiva
   sobre esos tests (Teorema 3.3, "ceguera sub-resolución"). El índice solo se vuelve
   visible cuando el soporte crece con T (a ≍ c log T, primos hasta T^{O(1)}), y ahí los
   bloques primos alcanzan por identidad el mismo orden (log T)² que el arquimediano: la
   negatividad es un fenómeno de **cancelación al segundo orden**, no de dominación de un
   bloque.

3. **(§3.4) La heurística literal del paso (1) de P42 — "acotar κ por los cambios de
   signo del núcleo aritmético K(N)" — queda refutada:** para φ ≥ 0 el núcleo
   K(N) = Σ_{d|N}Λ(d)Λ(N/d)φ(d²/N) es **no negativo, sin ningún cambio de signo**, y sin
   embargo el índice es positivo bajo ¬RH. La oscilación que porta el índice vive en las
   funciones de prueba, no en el núcleo; el objeto correcto es el **núcleo de déficit**
   ΔK := K − (predicción polar/arquimediana), cuyas fluctuaciones son exactamente las de
   la correlación de pares.

4. **(§4–§5) La cota necesaria es ASINTÓTICA y de segundo orden; el inventario
   incondicional da otra cosa.** El término principal de S(g,φ) es ½ĝ(1)φ̂(0), **sin
   serie singular** (correlación multiplicativa, no aditiva: Teorema 4.2 — PNT² lo da
   incondicionalmente con ahorro de Vinogradov–Korobov a frecuencia fija; ni siquiera
   hace falta criba para la asintótica estática). Lo que el puente necesita es esa
   asintótica **uniforme en la frecuencia de oscilación T** (hasta escalas X = T^C) con
   **error relativo o(1/log T)** — un orden logarítmico por debajo del término principal
   de correlación de pares, en la escala de los términos de orden inferior
   (Bogomolny–Keating / Montgomery–Soundararajan). La criba de Selberg da factor 8 sobre
   el término principal en el problema aditivo análogo (precisión relativa O(1));
   Vaughan/Heath-Brown y la gran criba dan cancelación **en media sobre T** (valores
   medios de polinomios de Dirichlet); ninguna técnica da uniformidad en T, y la ventana
   excepcional que la media no controla **es exactamente donde vive la señal**.

5. **(§6–§7) Medición: salida (C), agravada.** No es solo que la cota necesaria sea de
   tipo asintótico (el muro de correlación de pares anticipado por P42 §6.2): es su forma
   **uniforme-en-ventanas y al segundo orden**, que (Teorema 6.2) implica RH directamente
   — falla el test de "RH disfrazada" del punto (vi). La versión en media es un teorema
   (Montgomery–Vaughan) y es estructuralmente insuficiente. Incluso el premio de
   consolación (κ_W ≤ C·n_W ⇒ m ≤ C/2, una cota de densidad de cuádruplos) requiere la
   misma precisión de segundo orden: también está detrás del muro. La amplificación en k
   no cambia la frontera media/uniforme (Proposición 7.3).

**VEREDICTO: PUENTE MUERTO** (§9), con la localización: el muro no está en la fuerza de
la criba (la criba da incluso asintóticas aquí), está en el cuantificador sobre ventanas
— la misma estructura interior/frontera del no-go de P41, reaparecida con ropa de criba.

---

## 1. Notación y lo que se hereda

Heredamos del Doc 107 sin re-demostrar:

- La clase de prueba engrosada: h_{g,φ}(x₁,x₂) = g(x₁x₂)φ(x₁/x₂), g, φ ∈
  C_c^∞(ℝ₊*); Mellin doble ĥ(s₁,s₂) = ½ ĝ(σ) φ̂(τ), con σ := (s₁+s₂)/2,
  τ := (s₁−s₂)/2 (Doc 107, Teorema 3.4).
- La forma cuadrática Q₂(h,h') := W₂(h ⋆ h̃') (Doc 107, Def. 5.1), con la clase
  engrosada cerrada bajo ⋆ e involución: h_{g₁,φ₁} ⋆ h_{g₂,φ₂} = ½ h_{g₁⋆g₂, φ₁⋆φ₂},
  h̃_{g,φ} = h_{g̃, φ^∨} (Doc 107, Lema 5.2(a)).
- El lado espectral:
  Q₂(h,h) = Σ_{ρ₁,ρ₂} ĥ(ρ₁,ρ₂) · conj( ĥ(1−ρ̄₁, 1−ρ̄₂) ), absolutamente convergente
  (Doc 107, Lema 5.2(b)).
- Los nueve bloques aritméticos de W₂ = (D−P−A)⊗(D−P−A) (Doc 107, §2.3, Teorema 2.4),
  todos computables sin posiciones de ceros.
- El bloque casi-primo: P⊗P(h_{g,φ}) = Σ_I + Σ_II + Σ_III + Σ_IV con
  Σ_I = Σ_N g(N) (Λ⋆_φΛ)(N), (Λ⋆_φΛ)(N) := Σ_{d|N} Λ(d)Λ(N/d) φ(d²/N)
  (Doc 107, Teorema 4.2).
- El modelo de juguete (Hipótesis D, m = 1): cuádruplo {½±δ±iγ₀}, parámetros
  z = ρ − ½; bloque off×off de signatura (8,8), 8 planos hiperbólicos, con la mitad del
  índice portada por φ̂ en Re τ = ±δ (Doc 107, Teorema 5.5, Corolario 5.6).
- κ(Q₂) global = ∞ bajo ¬RH, por los planos off×on (Doc 107, Prop. 6.1); el invariante
  de la Forma B es el **bloque relativo** off×off, κ(Q₂^rel) = (4m)²/2 = 8m².

Notación de ventanas. Para T ≥ 2 y Δ ∈ (0,1] fijo, la **ventana de la variable suma**
es
$$W_{T,Δ} := \{ σ ∈ ℂ : |\mathrm{Im}\,σ - T| ≤ Δ,\ |\mathrm{Re}\,σ - \tfrac12| ≤ \tfrac14 \}.$$
(La banda Re σ ∈ [¼, ¾] contiene todos los σ = (ρ₁+ρ₂)/2 posibles, pues
Re ρ_i ∈ (0,1).) La ventana es estable bajo la involución σ ↦ 1−σ̄ (que fija Im σ y
refleja Re σ alrededor de ½). Escribimos
$$n_W := \#\{γ : ζ(\tfrac12+iγ)=0 \text{ on-line},\ |γ - 2T| ≤ 2Δ\} \;\asymp\; \frac{2Δ}{\pi}\log T$$
(densidad de von Mangoldt; [IK04, Thm. 5.8]).

**Definición 1.1 (índice por ventana, versión espectral).** Sea B la forma de Gram
espectral de Q₂ sobre el conjunto de pares ordenados de ceros (la del Lema 5.2(b) del
Doc 107, con la involución (ρ₁,ρ₂) ↦ (1−ρ̄₁,1−ρ̄₂)). Definimos
$$κ_W(Q₂) := \mathrm{neg.ind}\bigl( B|_{\{(ρ₁,ρ₂):\, (ρ₁+ρ₂)/2 \,\in\, W\}} \bigr),$$
la compresión de B a los pares cuya media cae en la ventana W. Como W es estable bajo
la involución, la compresión es hermitiana y el índice está bien definido.

**Definición 1.2 (índice test-accesible).** Para un subespacio V' ⊆ span{h_{g,φ}},
κ(Q₂; V') := sup{dim U : U ⊆ V', Q₂|_U < 0}. Es el único índice que un certificado
aritmético (un teorema sobre los bloques de §2.3 del Doc 107) puede acotar, porque los
bloques son funcionales de (g,φ), no de los ceros.

---

## 2. (i) El problema variacional para κ(Q₂^rel)

### 2.1. La forma sobre la clase engrosada: bi-cuadrática, con acoplamiento

Sobre un núcleo puro h = h_{g,φ}, el lado espectral es, por el Teorema 3.4 y el
Lema 5.2(b) del Doc 107:

$$Q₂(h_{g,φ}, h_{g,φ}) \;=\; \frac14 \sum_{ρ₁,ρ₂}
\hat g(σ_{12})\,\overline{\hat g(1-\bar σ_{12})}\;
\hat φ(τ_{12})\,\overline{\hat φ(-\bar τ_{12})},
\qquad σ_{12}=\tfrac{ρ₁+ρ₂}{2},\ τ_{12}=\tfrac{ρ₁-ρ₂}{2}. \tag{2.1}$$

**Observación 2.1 (no factoriza; respuesta a la pregunta del enunciado).** (2.1) es
cuadrática en g y cuadrática en φ por separado (bi-cuadrática en el par), pero **no**
factoriza como (forma en ĝ)·(forma en φ̂): cada par de ceros acopla el valor de ĝ en la
suma con el valor de φ̂ en la diferencia, y la suma sobre pares no se separa. Q₂ es una
forma hermitiana genuina sobre el span lineal de los núcleos engrosados (no solo sobre
el cono de tensores puros g⊗φ); los tensores puros forman un cono no lineal dentro del
span, y el índice negativo se computa sobre el span (Doc 107, Lema 5.4: el mapa de
evaluación es sobreyectivo desde el span).

**Proposición 2.2 (positividad bajo RH).** Si todo cero cumple ρ = 1−ρ̄, entonces para
todo h en el span de la clase engrosada, Q₂(h,h) = Σ_{ρ₁,ρ₂} |ĥ(ρ₁,ρ₂)|² ≥ 0.

*Demostración.* Doc 107, Obs. 5.3: bajo RH el apareamiento del Lema 5.2(b) es diagonal.
∎

**El problema variacional, enunciado.** Bajo ¬RH (juguete), ¿para qué (g,φ) — más
precisamente, para qué h en el span — es Q₂(h,h) < 0? Por (2.1) y la estructura de
órbitas: descomponiendo la suma espectral en bloques on×on, off×on y off×off,

- **on×on**: pares con ρ₁, ρ₂ ambos on-line son puntos fijos de la involución y
  contribuyen |ĥ(ρ₁,ρ₂)|² ≥ 0 — un "mar" positivo;
- **off×off**: 16m² pares, 8m² planos hiperbólicos (Doc 107, Teorema 5.5);
- **off×on**: para cada cero on-line ½+iγ y cada par {z, z* = −z̄} de parámetros off,
  un plano hiperbólico {(z, iγ), (z*, iγ)} (Doc 107, Prop. 6.1): 2m planos por cada γ,
  más los simétricos en la otra ranura.

Q₂(h,h) < 0 exige que la masa de ĥ sobre los planos hiperbólicos (alineada con sus
vectores negativos) supere la masa de |ĥ|² sobre el mar on×on. Esa es la formulación
variacional exacta; las direcciones negativas viven donde ĥ está alineada con pares que
contienen al menos un cero off, y suprimida sobre los pares on×on.

### 2.2. Dónde viven las direcciones negativas: lectura en (σ,τ)

Del Corolario 5.6 del Doc 107, en el juguete los 8 negativos del bloque relativo se
reparten: 2 en sumas off plenas (σ = ±δ±iγ₀), 2 en sumas reales (σ = ±δ, τ = ±iγ₀),
2 en sumas imaginarias (σ = ±iγ₀, τ = ±δ), 2 en sumas nulas (σ = 0, τ ∈ {±z₁,±z̄₁}).
Dos consecuencias operativas para el problema variacional:

(a) **Todo el bloque relativo vive en ventanas de altura acotada**: |Im σ| ≤ γ₀. Las
ventanas altas (T ≫ γ₀) no contienen pares off×off.

(b) **Realizar cualquiera de los 8 negativos exige oscilación a la frecuencia del cero
en alguna de las dos variables**: o ĝ oscila a frecuencia ~γ₀ (sumas imaginarias), o
φ̂ debe evaluarse en alturas Im τ = ±γ₀ (sumas reales: φ oscila a frecuencia γ₀ en la
variable cociente x₁/x₂), o ambas. Como γ₀ es desconocido, **cualquier certificado debe
ser uniforme en la frecuencia de alineación** — primera aparición del cuantificador que
matará al puente.

### 2.3. El índice por ventanas bajo ¬RH: la contaminación off×on crece

**Proposición 2.3 (conteo espectral por ventana).** En el juguete (m ≥ 1 cuádruplos,
todos de altura ≤ γ₀ fija), para T ≥ 2γ₀ + 2 y Δ ∈ (0,1]:
$$κ_{W_{T,Δ}}(Q₂) \;=\; 2m \cdot n_{W}^{(1)} + 2m \cdot n_{W}^{(2)}
\;=\; \frac{8mΔ}{\pi}\,\log T\,(1+o(1)) \qquad (T \to \infty),$$
donde n_W^{(1)}, n_W^{(2)} cuentan los ceros on-line γ con (z_off + iγ)/2 ∈ W según la
ranura. Bajo RH, κ_W(Q₂) = 0 para toda ventana W.

*Demostración.* Los pares en la ventana alta se clasifican: (i) on×on: puntos fijos de
la involución, planos de signatura (1,0): no aportan negativos. (ii) off×off: ausentes
(σ tiene |Im σ| ≤ γ₀ < T − 1). (iii) off×on: el par (ρ_off, ½+iγ) con
σ = ½ + (z+iγ)/2 ∈ W exige |γ + γ_off − 2T| ≤ 2Δ (con z = ±δ + iγ_off,
γ_off ∈ {±γ₀}); la involución manda (z, iγ) ↦ (z*, iγ) con z* = −z̄ ≠ z (pues
Re z = ±δ ≠ 0): órbita libre, plano hiperbólico, signatura (1,1), exactamente el
mecanismo de la Prop. 6.1 del Doc 107. Por cada γ admisible hay 4m vectores off en la
primera ranura = 2m planos; ídem segunda ranura. El conteo de γ admisibles es
n_W ≍ (2Δ/π)·... por la fórmula de von Mangoldt N(T+h)−N(T) = (h/2π)log T (1+o(1))
para h fijo. La afirmación bajo RH es la Proposición 2.2 comprimida. ∎

**Lema 2.4 (realizabilidad sobre la clase de prueba).** Para todo J ≤ κ_{W}(Q₂)
(conteo de la Prop. 2.3) y todo ε > 0, existe un subespacio U ⊂ span{h_{g,φ}} de
dimensión J con Q₂|_U < 0.

*Demostración.* Es la extensión por ventanas del argumento de la Prop. 6.1 del Doc 107,
con el mismo aparato. Elegimos J planos hiperbólicos objetivo, con puntos espectrales
(σ_j, τ_j) y (σ_j', τ_j') = (1−σ̄_j, −τ̄_j), todos distintos (biyección lineal
(z_i,z_j) ↦ (σ,τ), Doc 107 §5.2, extendida a pares off×on: los puntos siguen siendo
distintos porque los γ son distintos y Re τ = ±δ/... distingue las ranuras). Para cada
plano j, tómese h_j = h_{g_j,φ_j} con: ĝ_j concentrada en σ_j con decaimiento
superpolinomial fuera de un entorno de radio η en Im σ (Paley–Wiener, Doc 107 Lema 1.2),
multiplicada por el polinomio en σ que se anula en los finitos puntos σ de los demás
planos objetivo y en los 9 valores σ del bloque off×off (la multiplicación por
polinomios en s preserva la clase: corresponde a aplicar x∂_x a g); φ̂_j concentrada en
τ_j del mismo modo. La evaluación de h_j sobre su plano se normaliza al vector negativo
(a, ā') con B = anti-diagonal: Q₂-contribución del plano = −2|a|². Las contribuciones
restantes: (1) los demás planos objetivo: anuladas por los factores polinomiales; (2) la
cola on×on y los pares no objetivo: positivas o acotadas por
Σ_{(ρ₁,ρ₂) \text{ no obj.}} |ĥ_j| |ĥ_j∘inv| ≤ ε_j por el decaimiento rápido y la
convergencia absoluta (Doc 107, Lema 2.2(b)), eligiendo η y el orden de decaimiento; las
colas positivas suman ≥ 0 pero el término diagonal de la matriz de Gram de
U = span{h_j} es ≤ −2|a|² + ε_j y los términos cruzados son O(ε): para ε pequeño la
matriz de Gram es definida negativa. ∎

**Caveat declarado.** El Lema 2.4 hereda el estatus de la Prop. 6.1 del Doc 107 (misma
técnica, mismos supuestos del juguete con Hipótesis D); el seguimiento fino de las
constantes ε(η, J) no es load-bearing: lo único que se usa después es
κ(Q₂; clase de prueba, ventana W) ≥ (1−o(1))·κ_W(Q₂) en el sentido de la Prop. 2.3.

### 2.4. Primera conclusión estructural: el invariante relativo no es el que la
aritmética puede ver

**Proposición 2.5 (binariedad del índice test-accesible).** (a) Bajo RH,
κ_W(Q₂) = 0 para toda ventana. (b) Bajo ¬RH con m ≥ 1, sup_W κ_W(Q₂) = ∞
(Proposición 2.3: crece como log T). En consecuencia, **cualquier enunciado
incondicional de la forma "existe f(2) < ∞ con κ_W(Q₂) ≤ f(2) para toda ventana W" es
lógicamente equivalente a RH**.

*Demostración.* (a) = Prop. 2.2. (b) = Prop. 2.3 + Lema 2.4. La equivalencia: si RH,
la cota vale con f(2) = 0; si ¬RH, falla para todo f(2) finito. ∎

Esto reconfigura el paso (1) de P42. El Lema 7.2 del Doc 107 pedía exactamente la cota
uniforme por ventanas; la Proposición 2.5 muestra que **esa formulación ya es RH** —
no un lema intermedio amplificable sino el enunciado completo. El bloque relativo
κ(Q₂^rel) = 8m² (finito, amplificable) es una compresión a los pares off×off, que está
definida por las posiciones de los ceros: para aislarlo dentro de una ventana habría que
separar los planos off×off de los planos off×on que conviven en las mismas ventanas
bajas (|Im σ| ≤ γ₀: allí los off×on con γ ≈ −γ_off también caen, en número
O(m·Δ·log γ₀) — finito pero presente). No se conoce ningún funcional de (g,φ),
computable desde el lado aritmético, cuyo índice sea el del bloque off×off y no el de
la ventana completa; y §3–§6 mostrarán que cualquier sustituto pasa por evaluar el
déficit casi-primo al segundo orden. GAP estructural declarado: **la noción "κ(Q₂^rel)"
del Lema Faltante 6.1 de P42 no tiene, hoy, una definición test-accesible.**

---

## 3. (ii) El libro mayor aritmético: quién puede volverse negativo y por qué

### 3.1. La descomposición con signos

Por el Teorema 2.4 del Doc 107 aplicado a H := h ⋆ h̃ (que sigue en la clase engrosada,
con G := ½ g⋆g̃, Ψ := φ⋆φ^∨):

$$Q₂(h,h) \;=\; \underbrace{DD(H) + AA(H)}_{\text{polar/arquimediano}}
\;+\; \underbrace{PP(H)}_{\text{casi-primo}}
\;+\; \underbrace{PA(H)+AP(H)}_{\text{primo×arq.}}
\;-\; \underbrace{[DP+PD](H)}_{\text{polo×primo}}
\;-\; \underbrace{[DA+AD](H)}_{\text{polo×arq.}} \tag{3.1}$$

**Observación 3.1 (el signo del bloque casi-primo se invierte respecto de una
variable).** En una variable, Q(f,f) = D(F) − P(F) − A(F): el lado primo se **resta**,
y la analogía guía del enunciado ("el lado aritmético puede en principio ganarle al
polo") es la mecánica clásica de la positividad de Weil. En (3.1), por la paridad de
los signos del producto (D−P−A)⊗(D−P−A), el bloque casi-primo PP entra con **signo
positivo**, y los candidatos a "ganar en negativo" son los bloques mixtos polo×primo y
polo×arquimediano. La analogía de una variable se traslada, pero con los papeles
permutados: el detector de ¬RH no es "primos > polo" sino una cancelación entre PP y
AA al orden de sus fluctuaciones (§3.3).

Verificación de realidad: cada bloque de (3.1) es real sobre H = h⋆h̃ (la involución
hace de H una autocorrelación; el cálculo es el de una variable, Doc 107 §1, en cada
ranura).

### 3.2. Jerarquía de tamaños I: régimen de soporte fijo (sub-resolución)

Fijamos los soportes: supp g, supp φ ⊆ [e^{−a}, e^{a}] con a fijo, y dejamos crecer la
altura de la ventana: tests con ĝ concentrada en Im σ ≈ T → ∞ (g oscila a frecuencia
T), φ̂ a alturas O(T) según el objetivo. Normalizamos ‖g‖₂ = ‖φ‖₂ = 1 (norma L² en
medida de Haar d*x).

**Lema 3.2 (tamaños con soporte fijo).** Con soportes fijos y T → ∞:

(i) AA(H) = (1/4π²)∬ Ω(t₁)Ω(t₂) |ĥ(½+it₁, ½+it₂)|² dt₁dt₂, y como
Ω(t) = −log|t| + O(1), sobre tests concentrados a alturas t₁+t₂ ≈ 2T con t₁−t₂ = O(1):
AA(H) = (log T)²·c(h)·(1+o(1)) con c(h) ≍ ‖ĥ‖²_{L²(líneas)} > 0. **Positivo y de orden
(log T)².**

(ii) |PP(H)| ≤ Σ_{N} |G(N)|·(Λ⋆_{|Ψ|}Λ)(N) + (términos II–IV finitos)
≤ C(a)·‖g‖₂²‖φ‖₂² = O_a(1): la suma corre sobre los O(e^{2a}) enteros del soporte
fijo, **sin crecimiento en T**.

(iii) |[DP+PD](H)| ≤ C(a) y |DD(H)| ≤ C(a) e^{a/2}: sumas finitas y evaluaciones de
Mellin fuera de la línea, acotadas por Paley–Wiener con constante e^{O(a)},
**O_a(1) en T**.

(iv) |[PA+AP](H)| ≤ C(a)·log T y |[DA+AD](H)| ≤ C(a)·log T: un solo factor
arquimediano aporta un log.

*Demostración.* (i): bloque (6) del Doc 107 §2.3 evaluado en H, con
Ĥ = |ĥ|² sobre las líneas críticas (Lema 5.2(b) del Doc 107) y Ω(t) = −log|t| + O(1)
(Def. 1.3 del Doc 107, Stirling). (ii): Teorema 4.2 del Doc 107; el soporte de G acota
N ≤ e^{2a}; (Λ⋆_{|Ψ|}Λ)(N) ≤ ‖Ψ‖_∞ (log N)·d(N)-trivial sobre un conjunto finito.
(iii)–(iv): bloques (1)–(3),(5) del Doc 107 §2.3: las sumas sobre n están confinadas al
soporte compacto; cada factor A aporta ∫Ω·(decaimiento rápido) ≪ log T sobre tests a
altura T. ∎

**Teorema 3.3 (ceguera sub-resolución: el arquimediano domina donde no hay nada que
ver).** Con soportes fijos a y tests de ventana a altura T, existe T₀(a) tal que para
T ≥ T₀(a): Q₂(h,h) = AA(H)(1 + O_a(1/log T)) > 0. En particular, **sobre tests de
soporte fijo el índice por ventanas altas es 0 — incondicionalmente** — y la primera
mitad del falsador del paso (1) de P42 ("si el bloque arquimediano domina, el lado
aritmético es irrelevante") se cumple **exactamente en el régimen en que el índice es
invisible**: la dominación arquimediana y la ceguera son el mismo fenómeno.

*Demostración.* Lema 3.2: AA ~ c(h)(log T)² con c(h) > 0 acotado lejos de 0 sobre la
clase normalizada concentrada, y todos los demás bloques son O_a(log T). ∎

Consistencia espectral: con soporte fijo, ĥ tiene ancho de banda ≥ 1/a fijo, no
resuelve ceros individuales, y los planos hiperbólicos de la ventana (Prop. 2.3) no son
alineables: el mar on×on (que es lo que AA mide al orden principal) domina. No hay
contradicción entre el Teorema 3.3 y la Prop. 2.3: el Lema 2.4 usa tests cuya
localización η y cuyos factores polinomiales requieren **soporte creciente con T**.

### 3.3. Jerarquía de tamaños II: régimen de resolución (a ≍ c·log T) y el argumento de
los dos mundos

Para alinear un test con un plano hiperbólico de la ventana W_{T,Δ} hay que separar
puntos espectrales a distancia ≍ 1/log T (espaciado de ceros) o distinguir
Re σ = ½ ± δ/2 de ½: por Paley–Wiener, ancho de banda 1/log T exige a ≳ log T. En ese
régimen las sumas de primos corren hasta e^{O(a)} = T^{O(1)} y las cotas (ii)–(iii) del
Lema 3.2 ya no son O(1): todos los bloques pueden alcanzar el orden (log T)². ¿Quién
controla entonces el índice? La respuesta no necesita estimaciones nuevas: la da la
identidad misma.

**Teorema 3.4 (el argumento de los dos mundos: necesidad de precisión de segundo
orden).** Sea E(g,φ) := DD + AA − DA − AD (los bloques sin primos: funcionales
explícitos de (ĝ, φ̂, Ω), idénticos en cualquier mundo) y Π(g,φ) := PP + PA + AP − DP
− PD (los bloques con primos), de modo que Q₂(h,h) = E + Π. Supóngase que un
**certificado aritmético incondicional** — un teorema sobre Π válido sin hipótesis —
implica κ(Q₂; tests de ventana W_{T,Δ}) ≤ f(W) con f(W) = o(n_W) para toda ventana.
Entonces ese certificado distingue el valor de Π, en los tests realizadores del
Lema 2.4, con precisión
$$|Π_{\neg RH} - Π_{RH}| \;\gtrsim\; m\,n_W \cdot \|h\|_W^2
\qquad \text{frente a } E ≍ n_W^2\,\|h\|_W^2,$$
es decir, **precisión relativa o(1/log T) uniforme en T**; y de hecho el certificado
implica RH.

*Demostración.* E depende solo de (g,φ) y de datos arquimedianos: toma el mismo valor
en el mundo RH y en el mundo ¬RH. Toda la diferencia entre mundos vive en Π (que es
igual, por la identidad, a Σ_{ρ₁,ρ₂} − E). En el mundo ¬RH, los J = (1−o(1))·8mΔπ^{-1}
log T tests del Lema 2.4 satisfacen Q₂ < 0, o sea Π < −E en cada uno; en el mundo RH
los mismos (g,φ) dan Q₂ ≥ 0, o sea Π ≥ −E. La separación entre los dos valores de Π es
al menos la masa negativa de los planos, que es ≍ m n_W por test-familia normalizada,
mientras E ≍ n_W² (Teorema 3.3 persiste al orden principal: el mar on×on). Un
certificado que fuerza κ ≤ o(n_W) debe excluir el valor ¬RH de Π en al menos
(1−o(1))J de esas direcciones: debe localizar Π con error relativo o(m n_W / n_W²) =
o(1/log T). Y como bajo ¬RH el valor verdadero de Π es el del mundo ¬RH, un teorema
incondicional con esa precisión es falso bajo ¬RH salvo que ¬RH sea falsa: el
certificado implica RH. ∎

**Respuesta al falsador del paso (1) de P42 (formulación exacta).** El bloque
arquimediano domina y vuelve el índice invisible en sub-resolución (Teorema 3.3); en
resolución, el índice **sí** está controlado por el lado aritmético — pero al **segundo
orden**: por el déficit de Π respecto de su predicción arquimediana, con señal
m·n_W contra masa n_W². Ninguna de las dos ramas del falsador tal como estaban
escritas: el aritmético no es irrelevante, pero su control requerido no es de tipo cota
(tamaño) sino de tipo evaluación (segundo orden). Esto activa exactamente el riesgo que
P42 §6.2 dejó señalado.

### 3.4. Refutación de la heurística de cambios de signo, y el núcleo correcto

**Observación 3.5 (K(N) no tiene cambios de signo).** El paso (1) de P42 propone
"acotar el índice por el número de cambios de signo del núcleo aritmético
K(N) = Σ_{d|N}Λ(d)Λ(N/d)φ(d²/N)". Pero para φ ≥ 0 (y los engrosamientos de referencia
lo son), K(N) ≥ 0 para todo N: **cero cambios de signo**, mientras κ > 0 bajo ¬RH. La
heurística literal es falsa: Q₂ no es una forma de tipo Hankel/Toeplitz cuyo índice
cuente oscilaciones del símbolo; la oscilación que porta el índice está en las funciones
de prueba (frecuencias T, γ₀), no en el núcleo.

**Definición 3.6 (núcleo de déficit).** El objeto cuyos signos sí gobiernan el índice es
$$ΔK_φ(N) \;:=\; (Λ⋆_φΛ)(N) \;-\; \mathbb{E}_∞[(Λ⋆_φΛ)](N),$$
donde 𝔼_∞ es la predicción polar/arquimediana (el integrando continuo que produce los
bloques DD−DA−AD+AA al insertarse en la misma suma: explícito, sin ceros). Por la
identidad de §3.1, las sumas ponderadas de ΔK contra tests oscilantes son exactamente
las fluctuaciones de pares de ceros: ΔK es la encarnación casi-prima de la correlación
de pares. La pregunta correcta del paso (1) — "¿qué condición sobre K(N) daría
κ(Q₂^rel) ≤ f(2)?" — se responde: **una asintótica de ΔK al segundo orden, uniforme en
la frecuencia del test** (§4), no ninguna propiedad de tamaño o signo de K.

---

## 4. (iii) La cota necesaria, enunciada con exactitud

### 4.1. El funcional de orden k

Para k ≥ 2, con g ∈ C_c^∞(ℝ₊*) y Φ ∈ C_c^∞((ℝ₊*)^{k−1}) (peso transversal en las
coordenadas v_i = x_i/x_{i+1}), el bloque k-primo del cuadrante principal es
$$S_k(g,Φ) \;:=\; \sum_{n_1,\dots,n_k \ge 2} Λ(n_1)\cdots Λ(n_k)\;
g(n_1\cdots n_k)\,Φ\!\Bigl(\tfrac{n_1}{n_2},\dots,\tfrac{n_{k-1}}{n_k}\Bigr)
\;=\; \sum_{N} g(N)\,(Λ^{\star_Φ k})(N),$$
con (Λ^{⋆_Φ k})(N) := Σ_{N = n₁⋯n_k} Λ(n₁)⋯Λ(n_k) Φ(n₁/n₂, …, n_{k−1}/n_k), soportado
en el semigrupo de k-casi-primos con factorización balanceada (cada n_i ≍ N^{1/k} sobre
el soporte compacto de Φ). Es el funcional del Doc 107 §6.5; para k = 2,
S₂(g,φ) = S(g,φ) = Σ_N g(N)(Λ⋆_φΛ)(N).

### 4.2. El término principal: PNT por ranuras, sin serie singular

**Teorema 4.1 (asintótica estática, incondicional).** Para g, Φ fijos (sin oscilación
impuesta) con soportes en [e^{−a}, e^{a}]^{...}, X := e^{a}:
$$S_k(g,Φ) \;=\; \hat g(1)\,\widehat Φ(0,\dots,0)\;+\;
O_k\!\left( \|g\|_{\infty}\,\|Φ\|_{C^1}\; X \,e^{-c (\log X)^{3/5-\varepsilon}} \right),$$
donde ĝ(1) = ∫g(x)dx y Φ̂(0) = ∫Φ(v) d*v (transformadas en los puntos polares). Para
k = 2 esto es S(g,φ) = ĝ(1)·φ̂(0)·(1 + error) en la normalización Lebesgue×Haar del
cambio (u, v) (el ½ del jacobiano queda absorbido según la convención del Doc 107,
Lema 3.3; en la presentación de bloques, el término principal de PP coincide
exactamente con el sumando ĝ(1)φ̂(0)-tipo de DD — la cancelación polo/primo clásica,
doblada).

*Demostración.* Inducción en las ranuras: Σ_{n_k} Λ(n_k) G_{n_1..n_{k-1}}(n_k) con
G suave de soporte compacto se evalúa por el PNT con error de Vinogradov–Korobov
(ψ(x) = x + O(x e^{−c(log x)^{3/5−ε}}); [IK04, Cor. 8.30]) y suma parcial; el término
principal reemplaza Λ por 1·dx en cada ranura; el cambio de variables del Lema 3.3 del
Doc 107 (y su versión k, §6.5) separa las integrales. ∎

**Observación 4.2 (sin serie singular: la correlación es multiplicativa).** El análogo
de Goldston–Yıldırım para correlaciones **aditivas** Σ Λ(n)Λ(n+h) lleva la serie
singular 𝔖(h) (interacción de congruencias entre n y n+h) y es **conjetural**
[GY03 para los aproximantes; la asintótica plena es Hardy–Littlewood]. Aquí la
correlación es **multiplicativa** — (n₁, …, n_k) ↦ n₁⋯n_k — y no impone ninguna
condición de congruencia cruzada: la constante aritmética es 1 y la asintótica estática
es un **teorema incondicional** (Teorema 4.1). El régimen diagonal d ≈ √N que el peso
φ(d²/N) impone no es una dificultad para la asintótica: la restringe a semiprimos
balanceados, que se cuentan con PNT² (densidad ~ 2 log(b/a)·X/log²X para ratio en
[a,b], pesada a c·X con pesos log·log). **La criba ni siquiera es necesaria para esto.**
Toda la dificultad del puente está, por el Teorema 3.4, en otra parte: la uniformidad
en frecuencia.

### 4.3. La conjetura que el paso (2) necesita

Por el Teorema 3.4, el certificado debe evaluar el déficit en tests oscilantes. La
formulación exacta (forma k = 2; la k general es idéntica con S_k y el peso transversal
vectorial):

**Conjetura 108-N (cota necesaria; enunciado exacto).** *Existe δ(T) → 0 tal que para
todo T ≥ 2, todo A ≥ 1 fijo, y todos g, φ ∈ C_c^∞ con soportes en
[e^{−A log T}, e^{A log T}] y normalización ‖g‖_{H} := ‖ĝ(½+it)‖_{L²(dt)} +
‖t·∂_t ĝ‖_{L²} ≤ 1 (ídem φ):*
$$\Bigl|\, S(g,φ) \;-\; \hat g(1)\hat φ(0) \;-\; \mathcal{A}_∞(g,φ) \,\Bigr|
\;\le\; δ(T)\,\log T, \tag{4.1}$$
*donde 𝒜_∞(g,φ) es la predicción arquimediana explícita (la combinación
−AA−PA−AP+DA+AD+DP+PD de los bloques continuos evaluada según (3.1), computable sin
ceros). Uniformidad exigida: en T (la frecuencia de oscilación de g y φ es libre hasta
T), en A (escala polinomial X = T^A), y sobre toda la bola de la norma ‖·‖_H — no solo
sobre un cono.*

Tres aclaraciones pedidas por el enunciado del encargo:

(a) **¿Norma de operador o cono?** Debe ser sobre toda la bola (norma de operador). El
cono realizador — los (g,φ) alineados con los planos hiperbólicos — está parametrizado
por las posiciones (δ, γ₀, y los γ on-line vecinos), que son **desconocidas**: un
certificado restringido a un cono conocido de antemano no puede cubrir el cono
realizador sin uniformidad sobre el parámetro de alineación, lo que equivale a la bola
completa (a lo sumo con pérdidas polinomiales en la norma de Sobolev, irrelevantes
frente a la jerarquía log).

(b) **¿Uniformidad en k?** Sí: el puente de P42 necesita f(k) subexponencial con la
misma fuente; la versión k de (4.1) tiene señal m·k·n_W^{k−1} contra masa n_W^k:
precisión relativa o(k/log T) — más débil en apariencia para k grande, pero véase la
Proposición 7.3: la ganancia es ilusoria porque el presupuesto transversal crece a la
par.

(c) **Tamaño del main term y de la señal.** Main term de S a frecuencia 0: ĝ(1)φ̂(0)
(Teorema 4.1). En el régimen oscilante de (4.1), ĝ(1) y φ̂(0) son despreciables
(decaimiento rápido lejos de la ventana): S es **pura fluctuación**, su parte
predecible es 𝒜_∞ ≍ (log T)² (el mar de pares), y la señal a resolver es
≍ m log T — relativa o(1/log T), como en el Teorema 3.4.

### 4.4. La conjetura es RH disfrazada (test del punto (vi), anticipado)

**Teorema 4.3.** La Conjetura 108-N implica RH.

*Demostración.* Supóngase ¬RH (juguete con m ≥ 1; el caso general con Hipótesis D es
idéntico ventana a ventana). Tómense los tests realizadores del Lema 2.4 en la ventana
W_{T,Δ} con T → ∞: satisfacen Q₂(h,h) ≤ −c·m·‖h‖²_W con masa arquimediana
E ≍ n_W². Por la identidad (3.1), S(g,φ) (más los bloques primos restantes, que se
acotan igual o se incorporan a 𝒜_∞ por el mismo patrón) difiere de su predicción
ĝ(1)φ̂(0) + 𝒜_∞ en al menos la masa negativa de los planos: ≫ m·log T. Esto
contradice (4.1) con δ(T) → 0 para T grande. Luego ¬RH es imposible. ∎

Por el test del programa (Doc 99, discriminador I2a; lista de equivalencias del
programa): un "Lema 108" cuyo enunciado implica directamente κ_W ≡ 0 — que es la
equivalencia espectral de RH (P35/Doc 96) — **no es un lema: es la conclusión**. La
salida (B) del encargo queda así condicionada: cualquier candidato con la uniformidad
de (4.1) está descartado como "teorema esperable"; véase §6 para la medición fina y §8
para lo que queda.

---

## 5. (iv) Inventario incondicional: qué dan hoy criba, identidades y gran criba

### 5.1. Criba de Selberg / Λ₂

**(a1) El problema aditivo análogo.** La cota clásica de Selberg (1947; [HR74, Cap. 3];
exposiciones modernas: Tao, 254A Notes 4) da
$$\sum_{n \le X} Λ(n)\,Λ(n+h) \;\le\; (8 + o(1))\,\mathfrak{S}(h)\,X,$$
**factor 8** sobre la predicción de Hardy–Littlewood 𝔖(h)X. Verificado: el 8 es el
valor del método de Selberg puro (π₂(x)/Π_{HL}(x) ≲ 8); la versión vía gran criba
analítica de Montgomery–Vaughan elimina términos de error y las refinaciones
posteriores bajan la constante (≈ 7 y mejoras; valores exactos de las mejoras
[NO VERIFICADO en detalle; no load-bearing]). El "factor 4" que circula corresponde a
otra normalización (cotas tipo Brun–Titchmarsh/Bombieri–Davenport comparadas con
X/log²X sin la constante gemela) [origen exacto NO VERIFICADO; no load-bearing]. Lo
load-bearing es: **la criba da precisión relativa O(1) — una constante absoluta > 1 —
sobre el término principal, y solo para pesos no negativos.**

**(a2) Transporte a S(g,φ).** Para g, φ ≥ 0 la cota se transporta trivialmente — pero
no hace falta: el Teorema 4.1 da la **asintótica** (constante 1) porque la correlación
es multiplicativa. El régimen diagonal d ≈ √N no es el de la criba sino el de PNT²:
los divisores de N en [c₁√N, c₂√N] con ambos cofactores primos. La teoría de Ford de
H(x,y,z) [For08] — #{n ≤ x : ∃ d|n, d ∈ (y, 2y]} ≍ x/(log y)^{δ}(log log y)^{3/2} con
δ = 1 − (1+log log 2)/log 2 ≈ 0.086 — acota el **soporte** de la relajación sin pesos
de Λ (los enteros con algún divisor balanceado): es relevante si uno reemplaza Λ⋆Λ por
un mayorante de criba Λ_R⋆Λ_R, cuyo soporte se engorda exactamente a ese conjunto
Ford-delgado; registra que la mayorización pierde estructura (el mayorante vive en un
soporte (log)^δ-más denso que los semiprimos) — otra señal de que la dirección
"mayorar" no es la que el puente pide.

**(a3) Lo que la criba no puede dar, por construcción.** Las cotas de criba son
desigualdades de **pesos no negativos**: mayorar Σ a_N K(N) por Σ a_N (mayorante) exige
a_N ≥ 0. Los tests del índice tienen g oscilante (frecuencia T): la criba acota
Σ |g(N)| K(N) — la masa L¹, de tamaño X·‖·‖ — cuando lo necesario es la cancelación de
Σ g(N) ΔK(N) hasta o(log T). Distancia: **no es la constante 8 vs 1; es que la criba
acota la norma equivocada.** El problema de paridad, como anticipó P42 §6.2, es
efectivamente irrelevante aquí (ni siquiera bloquea la asintótica estática, Obs. 4.2);
la barrera operativa es otra.

### 5.2. Vaughan / Heath-Brown

S(g,φ) = Σ_{m,n} Λ(m)Λ(n) g(mn)φ(m/n) con m ≍ n ≍ √X **ya es** una suma bilineal de
tipo II en el régimen balanceado óptimo — no hay nada que descomponer (las identidades
de Vaughan [Vau77] y Heath-Brown [HB82] sirven para llevar sumas de Λ a este régimen;
aquí nacemos en él). La pregunta es si la maquinaria tipo II da cancelación contra el
núcleo específico: g oscilando a frecuencia T en mn, φ (acaso) a frecuencia γ en m/n.
Dos estructuras exactas:

(i) Si φ̂ se concentra en τ = iγ (sumas reales del Corolario 5.6 del Doc 107), el
núcleo se separa: φ(m/n) ≈ (m/n)^{iγ}φ₀(m/n), y
S ≈ Σ_m Λ(m) m^{iγ} w₁(m) · conj(Σ_n Λ(n) n^{iγ} w₂(n))-tipo más acoplamiento por
g(mn): polinomios de Dirichlet de Λ a frecuencia γ desconocida, escala √X.

(ii) Si ĝ oscila a frecuencia T (ventanas altas), S es Σ_N (Λ⋆_φΛ)(N) N^{−iT}-tipo:
el polinomio de (ζ'/ζ)² truncado.

Lo que la técnica da incondicionalmente: **valores medios**. El teorema de valor medio
de Montgomery–Vaughan [MV74],
∫_0^{T_0} |Σ_{n≤X} a_n n^{it}|² dt = (T_0 + O(X)) Σ|a_n|², da cancelación de raíz
cuadrada **en media sobre t** para X ≤ T_0^{1−ε}: la asintótica (4.1) vale para
**casi toda** ventana (fuera de un conjunto excepcional de medida o(T₀)). Lo que la
técnica no da: la ventana individual. El paso de "casi toda" a "toda" es la teoría de
valores grandes / densidad de ceros — y bajo ¬RH el polinomio (i)/(ii) **es** grande
exactamente en las frecuencias de los ceros off: la ventana excepcional no es un
defecto del método, **es la señal misma**. Un teorema "sin ventanas excepcionales" a la
precisión (4.1) implica RH (Teorema 4.3).

### 5.3. Gran criba / desigualdad de Montgomery; F(α,T)

La gran criba aporta exactamente el insumo del §5.2 (es la fuente del valor medio
MV74). Sobre la forma Q₂ restringida no hay ninguna cota espectral directa: la gran
criba acota momentos segundos promediados de evaluaciones lineales, es decir,
**trazas de compresiones promediadas en ventanas** — de nuevo la media, no el supremo.
El diccionario con la correlación de pares (Doc 107, Obs. 3.8): la versión con dos
funciones de prueba de F(α,T) de Montgomery [Mon73]. El estatus honesto de F(α,T):
la asintótica F(α,T) = (1+o(1))T^{−2α}log T + α + o(1) en 0 ≤ α ≤ 1 está probada
**bajo RH**; incondicionalmente solo hay versiones parciales/promediadas. Los errores
de la versión RH son o(1) **relativos** (primer orden); los términos de orden inferior
de la correlación de pares (los aritméticos, más allá de GUE) son del orden relativo
1/log T y siguen siendo **conjeturales** incluso bajo RH [BK96; MS04]. (4.1) exige
precisión o(1/log T): **un orden por debajo de lo que la teoría de correlación de
pares enuncia siquiera condicionalmente como teorema.**

---

## 6. (v) Medición de la distancia

### 6.1. Tabla disponible vs. necesario

| insumo | tipo | precisión relativa | uniformidad en frecuencia | pesos |
|---|---|---|---|---|
| Selberg/Λ₂ (§5.1) | cota superior | O(1) (factor 8) | n/a (sin oscilación) | ≥ 0 |
| PNT² (Teo. 4.1) | asintótica | e^{−c(log X)^{3/5}} | **solo frecuencia fija** | libres |
| Vaughan/HB + MV74 (§5.2) | asintótica en media | raíz cuadrada en media | **casi toda ventana** | libres |
| F(α,T) bajo RH (§5.3) | asintótica | o(1) relativo | promediada en [0,T] | clase fija |
| **necesario: (4.1)** | **asintótica** | **o(1/log T)** | **toda ventana, todo T** | **bola completa** |

### 6.2. Cuál salida ocurre

**(A) — descartada con prueba.** La cota de criba disponible no implica el control del
índice: acota la norma equivocada (§5.1(a3)) y su precisión relativa es O(1) cuando se
necesita o(1/log T) (Teorema 3.4). Además la heurística mecánica del paso (1) (cambios
de signo de K) es falsa (Obs. 3.5).

**(B) — descartada.** No es "misma forma, constantes distintas": la forma disponible es
*cota superior de masa con pesos positivos / asintótica en media*, la necesaria es
*evaluación uniforme al segundo orden con pesos oscilantes*. No hay un "Lema 108" con
la misma forma y mejor constante: cerrar el gap de constante (8 → 1+o(1)) no acerca
nada (la asintótica estática ya está, Teorema 4.1, y no basta); cerrar el gap de
uniformidad es el Teorema 4.3: RH. El único enunciado intermedio identificable — la
versión a constante de (4.1), que daría κ_W ≤ C·n_W y de ahí la cota de densidad
m ≤ C/2 — exige la **misma** precisión de segundo orden con constante en lugar de
o(1): la señal m·n_W debe distinguirse de la masa n_W² igualmente; está detrás del
mismo muro (véase §8.2).

**(C) — es la que ocurre, agravada.** La cota necesaria es de tipo asintótico (main
term exacto al segundo orden), uniforme en ventanas. El muro nominal anticipado por
P42 §6.2 era "correlación de pares (Montgomery–Goldston): barrera de evaluación, no de
signo". La medición precisa de este documento lo agrava en dos grados:

1. **Grado de uniformidad**: lo que se necesita no es la asintótica de correlación de
   pares en su forma estándar (promediada en T, que es como se enuncia y como se
   probaría), sino su forma uniforme-en-cada-ventana; esa forma implica RH
   (Teorema 4.3). El muro no es un vecino de RH: es RH.
2. **Grado de precisión**: la señal vive al orden relativo 1/log T — la escala de los
   términos de orden inferior aritméticos de la correlación de pares, conjeturales
   incluso bajo RH [BK96; MS04]. La asintótica suficiente podría ser **falsa o
   inaccesible incluso en el mundo RH** con la técnica actual: no hay enunciado
   condicional conocido que la cubra.

---

## 7. La transmutación, documentada (patrón Doc 99)

### 7.1. La cadena

$$\text{cota de criba sobre } S(g,φ)
\;\xrightarrow{\ \S3.4\ }\; \text{evaluación del déficit } ΔK
\;\xrightarrow{\ \text{Teo. 3.4}\ }\; \text{asintótica al 2º orden, uniforme en ventanas}
\;\xrightarrow{\ \text{Teo. 4.3}\ }\; \text{RH}.$$

En la taxonomía del programa: el Lema Faltante 6.1 de P42 (paso (1)+(2)) **transmuta**
— no a CAP (no hay positividad RH-equivalente involucrada; consistente con lo
anticipado en Doc 107 §6.4(γ)) sino al muro de **uniformidad media/uniforme en el
parámetro de ventana**, que es exactamente la estructura interior/frontera del no-go de
P41: el interior (casi toda ventana) es un teorema incondicional (MV74/gran criba); la
frontera (toda ventana, incluidas las alineadas con los ceros desconocidos) es RH. La
novedad respecto del mapa previo: el muro de correlación de pares, al medirse, no
resultó ser un muro distinto de la frontera de P41 — **es la misma frontera con
coordenadas de criba.**

### 7.2. Paralelo exacto con la Forma C

P42, Teorema 2.1 (Forma C): la densidad anclada que forzaría RH y el techo de densidad
de ceros N(σ,T) = O(T^{κ(σ)}) que la acota llevan el mismo exponente: auto-bloqueo.
Aquí: los teoremas de densidad de ceros son precisamente la mitad **en media sobre
ventanas** del enunciado κ_W ≤ C (dicen que casi toda ventana está libre de ceros off);
la mitad uniforme es RH. El amplificador de la Forma B se auto-bloquea con la misma
geometría: lo que se puede probar mejora ambos lados de la desigualdad a la vez.

### 7.3. Por qué la amplificación en k no ayuda

**Proposición 7.3 (la frontera es k-invariante).** Para todo k ≥ 2 fijo, el índice por
ventanas de Q_k bajo ¬RH crece sin cota sobre las ventanas (los (k−1)-tuplos on-line
con un factor off pueblan toda ventana, con multiplicidad ≍ k·m·n_W^{k−2}·(presupuesto
transversal); el mecanismo es el del Lema 2.4 ranura a ranura), y bajo RH es 0. Por
tanto el enunciado "κ_W(Q_k) ≤ f(k) uniformemente en W" es RH-equivalente **para cada
k por separado**, y la cadena de P42 — 2mk ≤ κ ≤ f(k) con f(k)/k → 0 — nunca llega a
usar la amplificación: su premisa (b) ya es la conclusión en k = 2. Esta es la forma
cuantitativa, sobre el objeto realizado, del lema de esterilidad (Doc 106, Prop. 3.6):
la realización analítica no aportó la segunda fuente; aportó otra presentación de la
misma fuente.

*Demostración (esquema, mismo estatus que Lema 2.4).* La señal de orden k en la ventana
W: tuplos con exactamente una ranura off y k−1 on alineadas; la involución actúa
libremente en la ranura off: planos hiperbólicos; conteo ∝ m·(densidad local)^{k−2}
limitado por el ancho de banda transversal de Φ̂ — un presupuesto geométrico que crece
con el soporte de Φ. La relación señal/masa es k·m/n_W para presupuesto transversal
fijo: el cociente mejora linealmente en k, pero ampliar el presupuesto transversal para
explotar k grande re-infla la masa on^k en la misma proporción (cada dirección
transversal nueva multiplica masa y señal por el mismo factor de densidad): el cociente
señal/masa en el régimen realizador es ≍ m/n_W **independiente de k** tras optimizar.
No se reclama la optimización exacta como teorema; lo load-bearing es la mitad fácil:
para cada k, bajo ¬RH el índice por ventanas no está acotado (basta una familia, la de
una ranura off con presupuesto transversal mínimo), lo que ya da la RH-equivalencia de
la cota uniforme en k fijo. ∎

### 7.4. Dónde reaparece MW-7

El Doc 107 probó que MW-7 (la barrera de Hadamard: necesitar las posiciones de los
ceros) no reaparece **en el funcional** W₂. Este documento localiza dónde sí reaparece:
**en la estructura de bloques de la forma cuadrática**. El bloque relativo off×off —
el único invariante finito y amplificable — es una compresión espectral; separarlo de
la contaminación off×on dentro de la misma ventana requiere conocer qué pares de la
ventana son off×off, es decir, las posiciones. El lado aritmético computa el **total**
de la ventana (eso es autonomía, y sigue siendo cierto); no computa la **partición** en
bloques (eso es MW-7, y es lo que el índice relativo necesita). La fórmula del programa:
*autonomía del valor ≠ autonomía de la inercia.*

---

## 8. (vi) ¿Queda algún "Lema 108"? Lo que sobrevive

### 8.1. El candidato (B) formal, y su descarte

Para el registro, el enunciado que habría sido el Lema 108 si la salida fuera (B):

> **(Lema 108, no viable.)** Existe C < ∞ absoluto tal que para todo T, Δ y toda
> familia ortonormal {h_j} de tests de ventana W_{T,Δ}: el número de j con
> Q₂(h_j,h_j) < 0 es ≤ C·n_W, con C independiente de T y de la configuración de ceros.

Plausibilidad contra la literatura: por el Teorema 3.4 (con f(W) = C·n_W en lugar de
o(n_W), misma demostración mutatis mutandis), probarlo exige evaluar Π con precisión
relativa O(C/log T) — la misma escala de segundo orden; y su consecuencia
(§8.2) ya sería un teorema de densidad de ceros de fuerza nueva. Aplicando el test del
programa: no es un teorema esperable con técnica actual (está en la escala de los
términos de orden inferior de correlación de pares, conjeturales bajo RH), y no es
exactamente RH disfrazada (con C ≥ 2 no implica m = 0) — es un **problema abierto
respetable de tipo correlación-de-pares-cuantitativa**, pero no un puente: aunque se
probara, mata solo m > C/2, y la uniformidad en k (Prop. 7.3) no lo amplifica.

### 8.2. El subproducto genuino: cota de densidad de cuádruplos por ventana

**Observación 8.1.** La cadena κ_W ≤ C·n_W ⇒ 2m·n_W(1+o(1)) ≤ C·n_W ⇒ **m ≤ C/2** es
correcta (Prop. 2.3). Es decir: una cota lineal-en-densidad del índice por ventanas
implicaría una cota absoluta del número de cuádruplos off-críticos — un enunciado más
fuerte que todo teorema de densidad conocido en esa región (los N(σ,T) dan o(T) ceros
off hasta altura T, no una cota absoluta). Esto confirma, por reducción al absurdo
metodológico, que κ_W ≤ C·n_W no puede ser barato. Se registra como diana de largo
plazo, fuera del alcance de la Forma B.

### 8.3. Lo que queda vivo del aparato

(1) **El funcional W_k como máquina de identidades**: la identidad bloque-aritmético =
pares de ceros con dos funciones de prueba (Doc 107) generaliza el diccionario
Montgomery/Goldston–Montgomery y es correcta e incondicional; tiene interés
independiente del puente (p.ej. para reformular términos de orden inferior de
correlación de pares como déficits casi-primos ΔK, Def. 3.6 — una reformulación, no un
progreso, pero limpia). (2) **El Teorema 3.3 (ceguera sub-resolución)**: positividad
incondicional de Q₂ sobre tests de soporte fijo en ventanas altas — un fragmento
genuino de positividad de Weil doblada, nuevo aunque modesto. (3) La **Observación
4.2** (la correlación multiplicativa no tiene serie singular y su asintótica estática
es teorema): delimita con precisión que el contenido aritmético duro del objeto doble
está íntegramente en la uniformidad de frecuencia, no en la aritmética de los
casi-primos.

---

## 9. VEREDICTO

**VEREDICTO: PUENTE MUERTO.**

**Localización exacta del muro.** El Lema Faltante 6.1 de P42 muere en su paso (1), y
el modo de muerte es el previsto como riesgo en P42 §6.2, agravado:

1. El invariante κ(Q₂^rel) (bloque off×off, finito, amplificable) **no es
   test-accesible**: lo que la clase de prueba y el lado aritmético pueden ver son los
   índices por ventanas de la forma completa, que son binarios — 0 en toda ventana bajo
   RH, ≍ m·log T (no acotado) bajo ¬RH (Prop. 2.3, Lema 2.4, Prop. 2.5). Cualquier
   cota uniforme finita es RH, ya en k = 2: no queda nada que amplificar (Prop. 7.3:
   la esterilidad del Doc 106 reaparece sobre el objeto realizado).

2. El mecanismo literal del paso (1) (índice ≤ cambios de signo de K(N)) es **falso**:
   K ≥ 0 sin cambios de signo, índice > 0 bajo ¬RH (Obs. 3.5). El mecanismo corregido
   (déficit ΔK) exige evaluación, no mayoración.

3. La cota de criba necesaria es de tipo **asintótico al segundo orden, uniforme en
   ventanas** (Conjetura 108-N, ec. (4.1)): error relativo o(1/log T), uniforme en la
   frecuencia T y sobre la bola entera de tests. Implica RH (Teorema 4.3): falla el
   test de RH disfrazada. Y su precisión está en la escala de los términos de orden
   inferior de la correlación de pares, conjeturales incluso bajo RH: la salida es la
   (C) del encargo, con el agravante de que el muro nominal (Montgomery–Goldston) es,
   medido, la misma frontera media/uniforme del no-go de P41 — no un muro nuevo.

4. La distancia con el inventario incondicional, medida: Selberg da precisión relativa
   O(1) (factor 8) en la norma equivocada (masa con pesos positivos); PNT² da la
   asintótica exacta pero solo a frecuencia fija (Teorema 4.1 — la criba ni siquiera
   hace falta ahí); Vaughan/Heath-Brown + valor medio de Montgomery–Vaughan dan la
   asintótica **en media sobre ventanas** (casi toda ventana); la ventana excepcional
   que la media no controla es exactamente donde vive la señal. El gap no es una
   constante ni un logaritmo: es el cuantificador.

**Qué se gana.** El mapa: la Forma B queda cerrada por el mismo tipo de frontera que
cerró las Formas A y C — con la precisión adicional de que su "segunda fuente"
candidata (cotas de criba casi-primas) resultó ser la presentación en media de la misma
fuente espectral, no una fuente independiente; el análogo de la racionalidad de Deligne
no apareció. Sobreviven como subproductos: el Teorema 3.3 (positividad sub-resolución
incondicional de Q₂), la identidad ΔK ↔ correlación de pares con dos funciones de
prueba, y la diana de largo plazo κ_W ≤ C·n_W ⇒ m ≤ C/2 (§8.2), registrada fuera de la
Forma B.

**Próximo paso (fuera de este puente).** Ninguno dentro de la Forma B por esta vía. Si
el programa continúa, la única dirección no descartada por este documento es la
señalada en §8.2/§5.3: el estudio de los términos de orden inferior de la correlación
de pares como déficits casi-primos — terreno de teoremas parciales honestos, sin
pretensión de RH.

---

## Referencias

**Internas (backward-only):** P42 (§6: Lema Faltante 6.1, pasos (1)–(3) y falsadores;
§2 Teorema 2.1 Forma C); Doc 107 (Teoremas 2.4, 3.4, 4.2, 4.4, 5.5; Lemas 2.2, 3.3,
5.2, 5.4; Cor. 3.6, 5.6; Obs. 3.8, 4.5, 5.3; Prop. 6.1; §6.4–6.5; Lema Faltante 7.2);
Doc 106 (Prop. 3.4, 3.5, 3.6; Obs. 3.9; Lemas Faltantes 5.2/5.3; Problema 5.4); Doc 99
(patrón de transmutación; discriminador I2a); Doc 96 (Teorema 8.1); Doc 94 (condición
C5); Doc 98 (juguete); P41 (no-go interior/frontera); P35 (forma de Weil, κ = 2m).

**Literatura (verificable):**
- A. Selberg, sieve superior y π₂(x) ≲ 8·Π_{HL}(x) (1947); exposición en
  H. Halberstam, H.-E. Richert, *Sieve Methods*, Academic Press, 1974, Cap. 3. El
  factor 8 confirmado en exposiciones modernas (T. Tao, 254A Notes 4: Some sieve
  theory; G. Oh, Applications of the Selberg sieve, notas Princeton). Refinaciones por
  debajo de 8: [constantes exactas NO VERIFICADAS; no load-bearing].
- H. L. Montgomery, R. C. Vaughan, *The large sieve*, Mathematika **20** (1973),
  119–134; y el teorema de valor medio para polinomios de Dirichlet
  (Montgomery–Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974),
  73–82). [MV74]
- R. C. Vaughan, *Sommes trigonométriques sur les nombres premiers*, C. R. Acad. Sci.
  Paris Sér. A **285** (1977), 981–983. [Vau77]
- D. R. Heath-Brown, *Prime numbers in short intervals and a generalized Vaughan
  identity*, Canad. J. Math. **34** (1982), 1365–1377. [HB82]
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos.
  Pure Math. **24**, AMS (1973), 181–193. [Mon73] (F(α,T): asintótica en 0 ≤ α ≤ 1
  **bajo RH**.)
- D. A. Goldston, H. L. Montgomery, *Pair correlation of zeros and primes in short
  intervals*, Progr. Math. **70**, Birkhäuser (1987), 183–203. [GM87]
- D. A. Goldston, C. Y. Yıldırım, *Higher correlations of divisor sums related to
  primes I*, Proc. London Math. Soc. (3) **87** (2003) [referencia de la tecnología de
  términos principales con serie singular para correlaciones aditivas; detalles
  bibliográficos del volumen NO VERIFICADOS aquí; no load-bearing]. [GY03]
- K. Ford, *The distribution of integers with a divisor in a given interval*, Ann. of
  Math. (2) **168** (2008), 367–433; H(x,y,2y) ≍ x (log y)^{−δ}(log log y)^{−3/2},
  δ = 1 − (1+log log 2)/log 2 ≈ 0.086. [For08]
- E. B. Bogomolny, J. P. Keating, términos de orden inferior de la correlación de pares
  más allá de GUE (1995–96, *Gutzwiller's trace formula and spectral statistics* /
  Nonlinearity) [identificación exacta del artículo NO VERIFICADA; lo citado — que los
  términos aritméticos de orden inferior son conjeturales y de orden relativo 1/log —
  es estándar]. [BK96]
- H. L. Montgomery, K. Soundararajan, *Primes in short intervals*, Comm. Math. Phys.
  **252** (2004), 589–617 (términos de orden inferior de varianzas de primos /
  correlaciones). [MS04]
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004
  (Thm. 5.8: N(T); Thm. 5.12: fórmula explícita; Cor. 8.30: PNT con error
  Vinogradov–Korobov). [IK04]
- J. Friedlander, H. Iwaniec, *Opera de Cribro*, AMS Colloq. Publ. 57, 2010 (paridad:
  bloquea asintóticas con signo, no cotas superiores; aquí resultó no ser el muro
  operativo).

*Fin del Doc 108.*
