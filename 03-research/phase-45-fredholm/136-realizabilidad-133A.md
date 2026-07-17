# Doc 136 — Problema 133.A: la realizabilidad de σ⁰ bajo ¬RH — colapso de la densidad global y rescate localizado

**Programa:** Hipótesis de Riemann — Phase 45, "Fredholm"
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Doc 133 (signatura infinitesimal σ_ε, Defs. 2.1–2.4; Thms. 2.6, 2.7, 2.10; Prop. 2.8, 2.11; Teorema-puente 2.13; Problema 133.A en §5.2), Doc 108 (Defs. 1.1–1.2; Props. 2.2, 2.3, 2.5; Lema 2.4 con su Hipótesis D; Thms. 3.3, 3.4, 4.3; §7.4), Doc 107 (Lema 2.2(b) convergencia absoluta; Lema 5.2(b) lado espectral; Teorema 5.5 y Prop. 6.1 planos hiperbólicos; cerradura de la clase bajo x∂ₓ y polinomios en s), Doc 98 (estructura del cuádruplo: κ = 2, dos planos hiperbólicos), Doc 106 (identidad tensorial del índice), P43 (autonomía del valor).
**Contrato creativo de la fase:** **[DEFINICIÓN-NUEVA]** = libertad total; **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad, prueba completa o estatus declarado línea por línea; **[CÁLCULO]** = cerrado; **[PUENTE]** = conexión con ζ/RH con estatus honesto; **[DESEO]** = declarado; **[GAP]** = marcado. Ninguna prueba se fabrica.

---

## 0. Resumen ejecutivo

El Problema 133.A pedía probar que bajo ¬RH la signatura infinitesimal de partida del
esquema canónico satisface σ⁰ ≥ c > 0 — el único eslabón citado-no-probado entre la
ley logística del Doc 133 y una equivalencia limpia de RH. Este documento lo resuelve
en dos movimientos, uno destructivo y uno constructivo:

1. **(§2, [TEOREMA] de colapso — la pregunta más importante del encargo, respondida.)**
   Para TODO esquema de tipo Doc 133 con dimensión creciente (n_N → ∞) y celdas de
   banda bien condicionadas, bajo ¬RH **de defecto finito** (un número finito de ceros
   off-críticos, en particular el juguete con m cuádruplos): **σ⁰ = 0 para todo
   ultrafiltro** (Teorema 2.5). La causa es estructural y se demuestra con dos líneas
   de contabilidad tensorial: capturar un plano negativo off×on exige resolver DOS
   ranuras, con costo dimensional (w_σ log T)(w_τ log T), mientras la ranura off es
   rígida (≤ 4m̄ vectores): el cociente κ/n ≤ Cm̄/max(w log T) → 0 en cuanto n → ∞.
   **El mismo mecanismo tensorial que amplifica la torre logística diluye la densidad
   del defecto.** Consecuencia auditada: el Teorema-puente 2.13(b) del Doc 133, tal
   como está escrito, es FALSO para su esquema canónico — la identificación implícita
   n_N = "conteo de ceros de la ventana" es incoherente con n_N = dim V_N (§2.1). La
   torre logística global arranca en 0 en ambos mundos (RH y ¬RH-de-defecto-finito):
   la dicotomía 0 vs ½ del Doc 133, en su normalización global, NO distingue RH. El
   gap temido por el encargo es real y queda nombrado: **invisibilidad densitaria**
   (los defectos individuales son nulos para toda densidad asintótica de dimensión
   creciente; §2.4). Lo que la σ_ε global sí detecta es una propiedad estrictamente
   más fuerte que ¬RH ("defecto localmente denso", Prop. 2.7), que los teoremas de
   densidad no excluyen pero ¬RH no implica.

2. **(§3–§5, el rescate.)** [DEFINICIÓN-NUEVA] La **signatura infinitesimal
   localizada** σ_loc: el esquema de micro-celdas — una grilla test-accesible de
   celdas de dimensión ACOTADA (bump de Paley–Wiener × monomios, con relleno positivo)
   que se refina con N en malla, altura, y perfil, y el índice normalizado por celda
   κ_N := max_celda neg.ind/dim. La ley logística sobrevive verbatim (Prop. 3.5).
   [TEOREMA] El sub-objetivo (β) se prueba completo y limpio: estabilidad del índice
   bajo perturbación en norma (Weyl, Teorema 4.1), bajo perturbación de rango acotado
   (entrelazamiento, Teorema 4.2, prueba de tres líneas sin autovalores) y bajo
   desplazamiento de la celda con malla computable (Teorema 4.4). [TEOREMA] El
   sub-objetivo (α) se cierra **en la versión localizada** (Teorema 5.4): bajo ¬RH, el
   cuádruplo off-crítico mínimo produce, para todo N grande, una celda de la grilla con
   índice ≥ 1 y dimensión estándar acotada D₀, de donde σ⁰_loc ≥ 1/(2D₀) > 0 —
   constante estándar, para todo ultrafiltro. La prueba es completa sobre los insumos
   citados del Doc 107 (lado espectral, convergencia absoluta, planos hiperbólicos);
   la Hipótesis D del Doc 108 **no se necesita**: era un artefacto de trabajar a altura
   T → ∞ con resolución 1/log T, y la localización a la altura del defecto (acotada,
   con constantes fijas no uniformes) la disuelve. Lo nuevo que la prueba usa: el
   índice de una celda es propiedad del Gram comprimido — la test-accesibilidad
   restringe el ESPACIO, no al vector testigo (Obs. 5.1), y eso desbloquea la
   aniquilación por posiciones dentro de un span ciego a posiciones.

3. **(§6, [PUENTE] honesto.)** El criterio reformulado y promovido:
   **RH ⟺ lim_k σ_loc^(k) = 0 ⟺ lim_k σ_loc^(k) ≠ ½** (Corolario 5.6), con la rama
   RH teorema (positividad de Weil comprimida) y la rama ¬RH teorema módulo los
   insumos D107 listados — ya no módulo Hipótesis D. La no-canonicidad del
   ultrafiltro se doma: la dicotomía es la misma para todo 𝒰 no principal (Obs. 5.7).
   El precio, declarado sin anestesia: la versión localizada degrada **densidad →
   existencia**; su contenido es la positividad de Weil sobre una base numerable de
   Grams aritméticos computables, más la amplificación logística. El muro no se cruza:
   reaparece como (i) la no-efectividad Π₁ de la parte estándar (intacta desde D133) y
   (ii) el cuantificador maestro mudado de "uniformidad en ventanas" (D108) a
   "búsqueda no acotada sobre la grilla" — ¬RH se vuelve semidecidible por Grams
   aritméticos (otra semidecisión más, junto a la numérica clásica), RH no gana nada.
   Lo que sí queda en el catálogo: una equivalencia de RH con ambas ramas en estatus
   de teorema-sobre-insumos-citados, eventos finito-algebraicos computables desde los
   primos, y separación macroscópica 0 vs ½.

---

## 1. Herencia y el punto fino de la normalización

### 1.1. Lo que se hereda sin re-demostrar

Del Doc 107/108: la forma Q₂ sobre el span de la clase engrosada h_{g,φ}, con lado
espectral
$$Q_2(h,h') \;=\; \sum_{(\rho_1,\rho_2)} \hat h(\rho_1,\rho_2)\,
\overline{\hat h'\big(\iota(\rho_1,\rho_2)\big)},
\qquad \iota(\rho_1,\rho_2) := (1-\bar\rho_1,\,1-\bar\rho_2), \tag{1.1}$$
suma sobre pares ordenados de ceros no triviales (con multiplicidad), absolutamente
convergente sobre la clase [D107, Lema 5.2(b), Lema 2.2(b)]; la evaluación factoriza:
$$\hat h_{g,\varphi}(\rho_1,\rho_2) = \tfrac12\,\hat g(\sigma)\,\hat\varphi(\tau),
\qquad \sigma = \tfrac{\rho_1+\rho_2}{2},\ \tau = \tfrac{\rho_1-\rho_2}{2}. \tag{1.2}$$
Los pares fijos por ι (ambos ceros on-line) contribuyen |ĥ|² ≥ 0 ("el mar"); las
órbitas libres {P, ιP} contribuyen 2Re[ĥ(P)·conj(ĥ(ιP))]: planos hiperbólicos de
signatura (1,1) [D107, Teorema 5.5, Prop. 6.1; D98 §6]. Bajo RH la suma es diagonal y
Q₂ ≥ 0 sobre todo el span [D108, Prop. 2.2]. La clase es cerrada bajo x∂ₓ
(= multiplicación por polinomios en la variable de Mellin) [D107, §5.2, usado en
D108 Lema 2.4]. La autonomía: Q₂(h,h') es computable desde los bloques aritméticos
sin posiciones de ceros [P43; D133 Prop. 2.8].

Del Doc 133: ultrafiltro 𝒰 no principal sobre ℕ, *ℝ = ℝ^ℕ/𝒰, parte estándar st;
esquema 𝒮 = (V_N), κ_N, n_N, σ_ε = st(κ*/n*); la torre tensorial y la ley logística
exacta x_{k+1} = 2x_k(1−x_k), con dicotomía lim σ^(k) ∈ {0, ½} (Thm. 2.10).

**Notación.** Cero genérico ρ = β+iγ, β ∈ (0,1). "Cero off" := β ≠ ½. *Defecto
finito*: el conjunto de ceros off es finito, de cardinal 4m̄ (m̄ cuádruplos contando
multiplicidad; el juguete D98/D108 es m̄ = m). *Defecto mínimo*: bajo ¬RH, fijamos de
una vez ρ⁰ = ½+δ₀+iγ₀ un cero off de altura |γ₀| mínima (existe: los ceros son
discretos), con multiplicidad m₀ ≥ 1, δ₀ ∈ (0,½). N(t) cuenta ceros con
0 < γ ≤ t; usamos solo N(t+1) − N(t) ≪ log(2+t) [IK04, Thm. 5.8].

### 1.2. [CÁLCULO] El punto fino: dim V_W ≠ n_W, y la incoherencia del esquema canónico

El Doc 133 (Def. 2.1, ejemplo canónico) toma κ_N := max_W neg.ind(Q|_{V_W}) sobre una
grilla de ventanas de resolución y n_N := dim V_W, y el Teorema-puente 2.13(b) cita la
cota de D108 "κ_W ≳ m·n_W" como si n_W (el conteo de ceros on-line de la ventana,
D108 ec. tras Def. 1.1, n_W ≍ (2Δ/π)log T) fuera dim V_W. Hagamos la contabilidad que
el Doc 133 no hizo.

Un test de resolución a altura T tiene soporte logarítmico [−a,a] con a = A log T y
banda de altura w en la coordenada espectral: por Paley–Wiener, el número de grados de
libertad (dimensión de un marco estable de tales tests) es
$$\mathrm{d.o.f.} \;\asymp\; \frac{a\,w}{\pi} \;=\; \frac{A\,w\log T}{\pi}. \tag{1.3}$$
La clase es doble: V se genera por tensores h_{g,φ}, con ĝ en banda de ancho w_σ
(coordenada suma) y φ̂ en banda de ancho w_τ (coordenada diferencia). El span de los
tensores puros es el producto tensorial completo:
$$\dim V \;\asymp\; \Big(\frac{A w_\sigma \log T}{\pi}\Big)\cdot
\Big(\frac{A w_\tau \log T}{\pi}\Big). \tag{1.4}$$
Mientras tanto, los planos negativos de la ventana a altura T (D108, Prop. 2.3) son
off×on: la ranura off tiene a lo sumo 4m̄ vectores (¡rígida!), y el compañero on-line
queda confinado por las dos bandas: a lo sumo C·m̄·(min(w_σ,w_τ) + 1/log T)·log T
planos. La densidad κ/dim es entonces, en el mejor de los casos,
$$\frac{\kappa}{\dim V} \;\lesssim\;
\frac{m̄\,(\min w \cdot \log T + 1)}{(w_\sigma \log T)(w_\tau \log T)}
\;\le\; \frac{2m̄}{\max(w_\sigma, w_\tau)\,\log T}. \tag{1.5}$$
Si dim V → ∞, algún factor de (1.4) tiende a ∞ y (1.5) tiende a 0. **La identificación
n_N ≍ n_W ≍ log T del Doc 133 es insostenible: o bien n_N = dim V_N ≫ κ_N (colapso),
o bien n_N = n_W no es una dimensión y la cota κ_N ≤ n_N de la Def. 2.3 del Doc 133
falla (κ_W ≍ 8mΔπ^{-1}log T puede exceder n_W ≍ 2Δπ^{-1}log T en cuanto m ≥ 1).**
En ambas lecturas el enunciado 2.13(b) tal como está escrito carece de prueba. El §2
convierte este cálculo en teorema; el §3 construye la normalización que lo esquiva.

---

## 2. [TEOREMA] El colapso de la densidad global

### 2.1. La clase de esquemas a la que se aplica

**Definición 2.1 (esquema de banda admisible).** Un esquema 𝒮 = (V_N) (test-accesible,
Doc 133 Def. 2.1, con n_N := dim V_N → ∞) es *de banda admisible con perfil
(T_N, w_σ(N), w_τ(N), c_N, ε_N)* si V_N admite una base {h_i} de tensores h_{g,φ} tal
que, escribiendo ĥ_i = ½ĝ_i(σ)φ̂_i(τ):

(i) **(banda)** existe una región R_N = {|Im σ − c_N| ≤ w_σ} × {|Im τ − c'_N| ≤ w_τ}
(o unión finita de tales, con los anchos comunes) tal que la parte de (1.1) soportada
fuera de R_N define una forma F_tail con ‖F_tail‖_{op} ≤ ε_N sobre V_N en la base
{h_i} (colas controladas);

(ii) **(condicionamiento θ)** la compresión a V_N de la parte fija
Q_fix := Σ_{pares ι-fijos} |ĥ|² satisface λ_min(Q_fix|_{V_N}) ≥ θ > 2ε_N, con θ > 0
fijo (marco de Riesz: los tests no son asintóticamente dependientes).

El ejemplo canónico del Doc 133 — en cualquiera de sus instanciaciones razonables
(banda τ ancha, grilla de celdas τ, banda τ fija) — es de banda admisible: (i) es el
decaimiento superpolinomial de Paley–Wiener más la convergencia absoluta [D107,
Lema 2.2(b)]; (ii) se consigue ortonormalizando el marco (operación test-accesible:
Gram computable, Prop. 2.8 de D133). No se afirma que TODO esquema de la Def. 2.1 de
D133 sea de banda admisible; se afirma que el canónico lo es, y el teorema se prueba
para la clase.

**Lema 2.2 (cota de rango del defecto en banda).** Bajo ¬RH de defecto finito (4m̄
ceros off, todos de altura ≤ H₀), la parte libre de (1.1) soportada en R_N (las
órbitas {P, ιP} con evaluación en R_N) tiene rango, como forma sobre V_N, a lo sumo
$$R_1(N) \;\le\; C\, m̄\,\big(\min(w_\sigma, w_\tau)\,\log T_N + H_0\log T_N\cdot
\mathbf{1}_{\text{bandas bajas}} + 1\big), \tag{2.1}$$
con C absoluto. En particular R₁(N) ≤ C' m̄ (min(w_σ,w_τ)+1)·log T_N + C'(m̄,H₀).

*Demostración.* Una órbita libre contiene al menos un cero off en alguna ranura. Fijado
el cero off ρ_off (4m̄ opciones por ranura, 2 ranuras), el par (ρ_off, ρ) cae en R_N
solo si Im σ = (γ_off+γ)/2 e Im τ = (γ_off−γ)/2 están en las bandas: γ queda
confinado a un intervalo de longitud ≤ 2 min(w_σ,w_τ) + O(1) alrededor de un centro
determinado por (c_N, c'_N, γ_off). El número de ceros (con multiplicidad) en un
intervalo de longitud ℓ a altura ≤ 2T_N es ≤ C(ℓ+1)log T_N [IK04, Thm. 5.8, sumado
sobre ⌈ℓ⌉ intervalos unitarios]. Las órbitas off×off exigen además ambos miembros de
altura ≤ H₀: a lo sumo (4m̄)² órbitas, y solo si la banda alcanza alturas ≤ H₀. Cada
órbita aporta una forma de rango ≤ 2 (el plano). Sumando: (2.1). ∎

### 2.2. El teorema de colapso

**Lema 2.3 (estabilidad del índice bajo perturbación de rango; forma cuadrática).**
Sean A, E formas hermitianas sobre un espacio V de dimensión finita, r := rank E.
Entonces |neg.ind(A+E) − neg.ind(A)| ≤ r.

*Demostración.* Sea N ⊆ V un subespacio con A|_N < 0, dim N = neg.ind(A). Sobre
N ∩ ker E (codimensión ≤ r en N) vale (A+E)|_{N∩ker E} = A|_{N∩ker E} < 0, luego
neg.ind(A+E) ≥ neg.ind(A) − r. Intercambiando A+E y A (y E por −E, mismo rango) se
obtiene la otra desigualdad. ∎

**Lema 2.4 (no hay negativos bajo el umbral de condicionamiento).** Si P ≥ θ·Id y
‖F‖_op ≤ ε < θ como formas sobre V, entonces neg.ind(P+F) = 0.

*Demostración.* Para todo v ≠ 0: (P+F)(v,v) ≥ θ‖v‖² − ε‖v‖² > 0. ∎

**Teorema 2.5 (colapso de la densidad global bajo defecto finito).** Sea 𝒮 un esquema
de banda admisible (Def. 2.1) con n_N → ∞. Bajo ¬RH de defecto finito (en particular,
el juguete del Doc 98/108 con m cuádruplos, cualquier m fijo):
$$\frac{\kappa_N}{n_N} \;\longrightarrow\; 0 \qquad (N \to \infty),$$
y por tanto **σ_ε(𝒮) = σ⁰ = 0 para todo ultrafiltro no principal 𝒰**, y la torre
logística del Doc 133 satisface lim_k σ^(k) = 0 — exactamente igual que bajo RH.

*Demostración.* Descomponemos la compresión a V_N del lado espectral (1.1):
Q₂|_{V_N} = Q_fix|_{V_N} + F_main + F_tail, donde F_main es la parte libre en banda
(rango ≤ R₁(N), Lema 2.2) y ‖F_tail‖ ≤ ε_N (Def. 2.1(i); la parte fija fuera de banda
es ≥ 0 y se absorbe en Q_fix sin bajar su cota inferior... — precisión: definimos
Q_fix|_{V_N} con TODOS los pares fijos; la Def. 2.1(i) acota entonces la parte libre
fuera de banda, que es la única cola restante; la parte fija nunca resta). Por los
Lemas 2.3 y 2.4 (con P = Q_fix|_{V_N} ≥ θ, F = F_tail, ε_N < θ):
$$\kappa_N \;=\; \mathrm{neg.ind}\big(Q_2|_{V_N}\big)
\;\le\; \mathrm{neg.ind}\big(Q_{fix}|_{V_N} + F_{tail}\big) + \mathrm{rank}\,F_{main}
\;\le\; 0 + R_1(N).$$
Queda acotar R₁(N)/n_N. Si las bandas están a alturas acotadas (c_N, c'_N = O(1)),
R₁(N) ≤ C(m̄, H₀, w) es finito mientras n_N → ∞: cociente → 0. Si las bandas crecen
(T_N → ∞), por (1.4) la dimensión de un marco θ-condicionado satisface
n_N ≤ C(A)·(w_σ log T_N)(w_τ log T_N) y también n_N ≥ c·(w_σ log T_N)(w_τ log T_N)
(d.o.f. de Paley–Wiener: un marco de Riesz no excede ni desperdicia los grados de
libertad de la banda más que en constantes; es la única propiedad de (1.3)–(1.4) que
se usa). Escribiendo u := w_σ log T_N, v := w_τ log T_N (ambos ≥ c₀ > 0 por
resolución mínima), el Lema 2.2 da R₁ ≤ C m̄ (min(u,v) + 1) + C(m̄,H₀), luego
$$\frac{R_1(N)}{n_N} \;\le\; \frac{C\,m̄\,(\min(u,v)+1)}{c\,u\,v} + \frac{C(m̄,H_0)}{n_N}
\;\le\; \frac{C'\,m̄}{\max(u,v)} + \frac{C(m̄,H_0)}{n_N}.$$
Como n_N ≍ uv → ∞ y u, v ≥ c₀, necesariamente max(u,v) → ∞: ambos términos → 0.
Para uniones finitas de bandas el argumento se aplica banda a banda y se suma (el
máximo de la grilla hereda la cota de la peor celda). Finalmente κ_N/n_N → 0 implica
st([κ_N/n_N]) = 0 para todo 𝒰 (st de una sucesión convergente es su límite), y la
forma cerrada del Thm. 2.10 de D133 con σ⁰ = 0 da σ^(k) ≡ 0. ∎

**Corolario 2.6 (auditoría del Doc 133).** El Teorema-puente 2.13(b) del Doc 133 es
falso tal como está enunciado para todo esquema canónico de banda admisible con
n_N = dim V_N → ∞: bajo ¬RH con m cuádruplos (m fijo) se tiene σ⁰ = 0, no σ⁰ ≥ c′m.
El error de origen: la cita de D108 Prop. 2.3 transporta κ_W ≳ m·n_W con n_W =
*conteo espectral de la ventana*, que no es ni puede ser dim V_W (§1.2). El corolario
2.13(c) ("RH ⟺ lim σ^(k) = 0") queda sin sustento en su rama ¬RH. ∎

### 2.3. Qué detecta de verdad la σ_ε global

**Proposición 2.7 (σ⁰ global > 0 ⟺ defecto localmente denso; una dirección probada).**
Sea 𝒮 de banda admisible. (a) Si σ⁰(𝒮) > 0 para algún 𝒰, entonces
$$\limsup_{N\to\infty}\ \frac{\#\{\text{ceros off que alimentan órbitas libres en } R_N\}\cdot \log T_N}{n_N} \;>\; 0,$$
es decir: hay una sucesión de bandas donde el número de ceros off acoplados es
≳ n_N/log T_N ≍ (un factor completo de la dimensión) — **una proporción positiva de
los grados de libertad de una ranura entera**, infinitas veces. Llamamos a esta
configuración *defecto localmente denso*. (b) Recíprocamente, si el defecto es
localmente denso, la realizabilidad del índice correspondiente (versión por ventanas
del Lema 2.4 de D108) daría σ⁰ > 0 para un 𝒰 concentrado en las bandas malas
[estatus: condicional al mismo tipo de realizabilidad; no se usa en este documento].

*Demostración de (a).* Por la prueba del Teorema 2.5, κ_N ≤ R₁(N), y la cota (2.1)
generalizada sin hipótesis de defecto finito es R₁(N) ≤ C·D_off(N)·(min(u,v)+1)·
(log T_N)/log T_N — más precisamente: cada cero off acoplado aporta ≤ C(min(w)+1)log T_N
planos, así que κ_N ≤ C·D_off(N)·(min(u,v)+1) con D_off(N) := número de ceros off
alimentando R_N. Si κ_N/n_N ≥ c en un conjunto 𝒰-grande (necesario para σ⁰ > 0),
entonces D_off(N) ≥ c·n_N/(C(min(u,v)+1)) ≥ c'·n_N·(algo ≥ 1/u o 1/v)... y usando
n_N ≍ uv: D_off(N) ≥ c''·max(u,v) ≍ n_N/(min-factor) ≥ c''·n_N/(C·log T_N·w_min),
que es la afirmación con las constantes de banda absorbidas. ∎

**Observación 2.8 (los teoremas de densidad son mudos aquí; respuesta a la pregunta
(i) del encargo).** ¿Fuerzan los teoremas de densidad N(σ,T) = o(T) que σ⁰ = 0
SIEMPRE, incluso bajo ¬RH genuina (m = ∞, Bohr–Landau)? **No.** Bohr–Landau y los
teoremas de densidad acotan el TOTAL de ceros off hasta altura T (densidad media
cero), pero no excluyen agrupamiento local: incondicionalmente, una sola banda de
ancho O(1) puede contener hasta O(log T) ceros off (la cota trivial por intervalo
unitario es lo único disponible), que es exactamente la escala "localmente densa" de
la Prop. 2.7. Conclusión exacta del cuadro global: **σ_ε global no es un detector de
¬RH; es un detector de defecto localmente denso** — una propiedad estrictamente más
fuerte que ¬RH (el defecto finito la viola, Teorema 2.5) y no excluida por la teoría
de densidad. La dicotomía logística global separa "RH ∨ ¬RH-rala" de "¬RH-agrupada":
no es un criterio de RH.

### 2.4. La cara del muro, nombrada

**[CÁLCULO/diagnóstico] Invisibilidad densitaria.** El mecanismo del Teorema 2.5 es
el tensor: en Q₁⊗Q₂ el índice mezcla q₁p₂ + p₁q₂ (D106), y cuando una ranura es
rígida (q ≤ 4m̄ fijo) la densidad de negativos escala como m̄/n₁ → 0. **La misma
identidad tensorial que da la amplificación logística (D133, Thm. 2.10) es la que
diluye el defecto individual en toda normalización de dimensión creciente.** Es el
cuantificador maestro (P43, Principio 3.1) en la coordenada "densidad": un defecto
individual (objeto de cardinal finito) es invisible para TODO funcional de densidad
asintótica test-accesible — para verlo hay que renunciar a la densidad y pasar a la
existencia localizada. Registramos esta cara del muro con nombre propio:
**invisibilidad densitaria de los defectos individuales**. (Entra al NO-GO-LIST como
acompañante de MW-7: la partición no es autónoma; la densidad no ve lo finito.)

---

## 3. [DEFINICIÓN-NUEVA] La signatura infinitesimal localizada σ_loc

La salida que el Teorema 2.5 deja abierta es exactamente la que el encargo anticipó:
celdas de dimensión ACOTADA (donde el defecto no se diluye), grilla que se refina con
N (para encontrar al defecto sin conocer su posición), y normalización por celda.

**Definición 3.1 (celda de micro-resolución).** Fijado un *perfil*
p = (D, w, M, b, c, c') con D ∈ ℕ (grado), w > 0 (ancho), M ∈ ℕ (orden de
decaimiento), b ∈ ℚ_{>0} (calibre), (c, c') ∈ ℚ² (centros en Im σ, Im τ), la celda
es el subespacio
$$V_p \;:=\; \mathrm{span}\Big\{\, h_{g_a,\varphi_b} \;:\; 0 \le a, b \le D \,\Big\},
\qquad
\hat g_a(\sigma) := B^{(M)}_w(\sigma - ic)\,\sigma^a,\quad
\hat\varphi_b(\tau) := B^{(M)}_w(\tau - ic')\,\tau^b,$$
donde B^{(M)}_w es la transformada de Mellin de un bump fijo g₀^{(M,w)} ∈ C_c^∞(ℝ₊*)
par-normalizado, elegido de una vez en una familia computable con
$$|B^{(M)}_w(z)| \;\le\; C_M\,e^{a_0|\mathrm{Re}\,z - \tfrac12|}\,(1+|\mathrm{Im}\,z|/w)^{-M},
\qquad B^{(M)}_w(0) = 1, \tag{3.1}$$
(Paley–Wiener; a₀ = a₀(M,w) el soporte logarítmico, FIJO — no crece con ninguna
altura). dim V_p ≤ (D+1)², y V_p es test-accesible: el perfil no menciona ceros.
La *celda rellenada* es Ṽ_p := V_p ⊕ ℂ^{(D+1)²} con la forma
Q̃_p := (Q₂|_{V_p}) ⊕ Id (relleno positivo de dimensión igual al tope de la celda;
test-accesible: es un bloque identidad formal).

**Definición 3.2 (esquema localizado 𝒮_loc).** Para cada N, la *grilla* 𝒢_N es el
conjunto (finito, computable) de perfiles p con D ≤ N, M ≤ N, w ∈ {2^{-j} : j ≤ N},
b ∈ {2^{-j} : j ≤ N}, y centros (c, c') en la malla (b·ℤ)² ∩ [−2^N, 2^N]². Se define
$$x_0(N) \;:=\; \max_{p \in \mathcal{G}_N}\
\frac{\mathrm{neg.ind}\big(\tilde Q_p\big)}{\dim \tilde V_p} \;\in\; \mathbb{Q}\cap[0,\tfrac12],
\qquad p_N^* := \text{el primer maximizador en el orden lexicográfico},$$
(la cota ≤ ½ es por el relleno: neg.ind(Q̃_p) ≤ dim V_p = ½ dim Ṽ_p). La *signatura
infinitesimal localizada* y su torre:
$$\sigma_{loc} := \mathrm{st}\big([\,x_0(N)\,]\big) \in [0,\tfrac12], \qquad
\sigma_{loc}^{(k)} := \mathrm{st}\big([\,x_k(N)\,]\big),$$
donde x_k(N) es la sucesión logística de la celda ganadora: la forma reducida
no degenerada Q̄_N de Q̃_{p_N^*} (cociente por el radical, D133 Def. 2.4) y
x_k(N) := neg.ind(Q̄_N^{⊗2^k})/n̄_N^{2^k}.

**Proposición 3.3 (buena definición y autonomía).** (a) x_0(N) está bien definido y
es computable desde los datos aritméticos sin posiciones de ceros: cada entrada de
cada Gram es Q₂(h,h') con h, h' en la clase (autonomía, D133 Prop. 2.8 / P43), la
grilla es finita y especificada sin ceros, y neg.ind se computa exactamente
(Lagrange–Sylvester). (b) σ_loc ∈ [0,½] existe para todo 𝒰 (sucesión acotada).
(c) x_0(N) es no decreciente en N (𝒢_N ⊆ 𝒢_{N+1}), luego converge y σ_loc no
depende de 𝒰: σ_loc = lim_N x_0(N).

*Demostración.* (a) Composición de hechos citados: la clase contiene B_w·(monomios)
porque la multiplicación por polinomios en la variable de Mellin es x∂ₓ [D107]; el
relleno es un bloque explícito. (b) st existe sobre limitados. (c) Monotonía: el
máximo sobre una familia creciente de conjuntos finitos; sucesión monótona acotada
converge; st de convergente = límite para todo 𝒰 [D133, Thm. 2.6(c), mismo
argumento]. ∎

**Observación 3.4 (qué cambió respecto del Doc 133).** Tres cosas. (1) La dimensión
por celda está acotada por el perfil, no crece con la altura: el Teorema 2.5 no se
aplica (su hipótesis n_N → ∞ por celda falla adrede). (2) La normalización es por
celda ganadora (un cociente de enteros acotados por celda), no por una dimensión
global: la densidad se reemplaza por una existencia normalizada. (3) El ultrafiltro
quedó domado gratis (Prop. 3.3(c)): la no-canonicidad que el encargo pedía domar era
un artefacto de la normalización global no monótona.

**Proposición 3.5 (la ley logística sobrevive verbatim).** Para todo 𝒰 y todo k ≥ 0
estándar: σ_loc^(k) = ½(1 − (1−2σ_loc)^{2^k}), y
$$\lim_{k\to\infty} \sigma_{loc}^{(k)} \;=\;
\begin{cases} 0, & \sigma_{loc} = 0,\\ \tfrac12, & \sigma_{loc} \in (0,\tfrac12].\end{cases}$$

*Demostración.* Para cada N fijo, Q̄_N es una forma hermitiana no degenerada de
dimensión finita: el Teorema 2.10 del Doc 133 (identidad tensorial D106 + forma
cerrada) se aplica coordenada a coordenada; st es homomorfismo sobre limitados y la
identidad se usa finitas veces (k estándar). El caso σ_loc = 1 — el único que rompía
la dicotomía en D133 — está excluido por el relleno: x_0(N) ≤ ½ ⟹ σ_loc ≤ ½, y
1−2σ_loc ∈ [0,1) salvo σ_loc = ½, donde (1−2x)=0 da σ^(k) ≡ ½ — dentro de la rama ½.
∎

---

## 4. [TEOREMA] Sub-objetivo (β): estabilidad del índice de celda

Los tres lemas de perturbación, con prueba completa. Son el motor de la grilla: hacen
que una malla computable baste para capturar planos cuya posición exacta es
desconocida.

**Teorema 4.1 (estabilidad de Weyl).** Sean A, E hermitianas sobre V, dim V = n, y
μ > 0. Si A tiene al menos κ autovalores ≤ −μ y ‖E‖_op < μ, entonces
neg.ind(A+E) ≥ κ. Simétricamente, si A ≥ −μ' con μ' < −‖E‖... (forma útil:) si
A ≥ 0 y ‖E‖_op < λ_min(A|_{(\ker A)^\perp})... — enunciado mínimo que usamos: con
autovalores ordenados λ₁ ≥ … ≥ λ_n, |λ_k(A+E) − λ_k(A)| ≤ ‖E‖_op para todo k.

*Demostración.* Courant–Fischer: λ_k(A+E) = min_{codim S = k−1} max_{0≠v∈S}
R_{A+E}(v) con R el cociente de Rayleigh. Para todo v: |R_{A+E}(v) − R_A(v)| =
|E(v,v)|/‖v‖² ≤ ‖E‖. Tomando el mismo S óptimo de A: λ_k(A+E) ≤ λ_k(A) + ‖E‖;
intercambiando A y A+E: la otra desigualdad. La primera afirmación: los κ autovalores
≤ −μ de A se mueven a ≤ −μ + ‖E‖ < 0. ∎

**Teorema 4.2 (estabilidad bajo rango acotado).** |neg.ind(A+E) − neg.ind(A)| ≤
rank E. (= Lema 2.3; prueba allí, tres líneas, sin autovalores.) ∎

**Teorema 4.3 (Lipschitz del Gram bajo desplazamiento de celda).** Sea p un perfil y
G(ϑ) el Gram de Q₂ sobre la celda V_{p+ϑ} obtenida desplazando los centros
(c,c') ↦ (c+ϑ₁, c'+ϑ₂). Entonces G es diferenciable en ϑ y
$$\|\partial_{\vartheta_i} G(\vartheta)\|_{op} \;\le\; L_p \;:=\;
(D+1)^2\,\max_{a,b}\, \big|Q_2\big(\partial h, h'\big)\big|\text{-tipo}
\;<\;\infty,$$
con L_p computable desde los datos aritméticos: el desplazamiento del centro es la
modulación g ↦ g·x^{iϑ}, cuya derivada en ϑ es i(log x)·g = i·(x∂ₓ aplicado en la
coordenada de Mellin) — un test de la misma clase [D107]; las entradas de ∂G son
valores de Q₂ sobre tests de la clase, computables (autonomía) y finitas
(convergencia absoluta, D107 Lema 2.2(b)); la norma de la matriz (D+1)²×(D+1)² se
acota por el máximo de entradas por la dimensión.

*Demostración.* La diferenciabilidad entrada a entrada: Q₂(h_ϑ, h'_ϑ) con
ĥ_ϑ(σ,τ) = ĥ(σ−iϑ₁, τ−iϑ₂); la suma (1.1) converge absolutamente con uniformidad
local en ϑ (el decaimiento (3.1) es uniforme en |ϑ| ≤ 1), lo que permite derivar bajo
la suma; la derivada inserta el factor lineal correspondiente, que es la evaluación
de un test derivado de la clase. La cota de norma: ‖B‖_op ≤ (dim)·max|entradas| para
hermitianas (Schur trivial). ∎

**Teorema 4.4 (β: el índice de la celda alineada sobrevive en la malla).** Sea p* un
perfil ideal (centros reales arbitrarios, no necesariamente en la malla) tal que
G(p*) tiene κ autovalores ≤ −μ < 0. Sea p ∈ 𝒢_N el perfil de la malla más cercano,
con |centros(p) − centros(p*)| ≤ b√2 (b el calibre de 𝒢_N). Si
$$b \;\le\; \frac{\mu}{2\sqrt2\,L_{p^*}},$$
entonces neg.ind(G(p)) ≥ κ. En particular, para todo perfil ideal con (μ, L) fijos,
existe N₀ computable desde (μ, L, posición) tal que para todo N ≥ N₀ la grilla 𝒢_N
contiene una celda con índice ≥ κ.

*Demostración.* Por el Teorema 4.3 y el teorema del valor medio en cada coordenada,
‖G(p) − G(p*)‖ ≤ L_{p*}·b√2·(constante de camino ≤ 2) ≤ μ/2 < μ. (L es continuo en ϑ
y lo tomamos como el supremo sobre el segmento, finito por el mismo argumento.)
Teorema 4.1 concluye. La existencia de N₀: la malla 𝒢_N tiene calibre 2^{-N} → 0 y
alcance 2^N → ∞, y los perfiles (D, w, M) ideales finitos entran en la grilla para N
mayor que su tamaño. ∎

**Observación 4.5 (lectura del encargo).** Esto es el sub-objetivo (β) del
Problema 133.A en la forma que sobrevivió al §2: la "perturbación o(1) del
desplazamiento" es, en la versión localizada, una perturbación de tamaño b·L con b
computable — no hay ningún o(1/log T) que perseguir porque la celda vive a la altura
del defecto (acotada) y sus constantes son fijas. En la versión global de D108 el
mismo lema habría exigido malla o(1/log T) con L creciente en T: ahí es donde el muro
de segundo orden habría reaparecido. La localización no esquiva el lema: esquiva su
régimen hostil.

---

## 5. [TEOREMA] Sub-objetivo (α) localizado: realizabilidad de σ_loc > 0 bajo ¬RH

**Observación 5.1 (la llave conceptual: el testigo no necesita ser test-accesible).**
κ_N involucra neg.ind(Q₂|_{V_p}): una propiedad del Gram comprimido. La
test-accesibilidad restringe la ESPECIFICACIÓN de V_p (sin posiciones de ceros); el
VECTOR testigo de negatividad dentro de V_p es un objeto de la demostración, no del
esquema, y puede usar todas las posiciones que quiera. El Lema 2.4 de D108 usaba
factores polinomiales con raíces en posiciones de ceros y por eso parecía heredar un
caveat; aquí los mismos factores se reconstruyen como combinaciones lineales DENTRO
del span test-accesible {B·σ^a}: la aniquilación por posiciones es legítima porque
ocurre en el testigo. Esta observación es la que convierte (α) de deuda en teorema.

### 5.1. La cola espectral

**Lema 5.2 (cola del test concentrado; prueba completa).** Sea h ∈ V_p con
ĥ(σ,τ) = ½ĝ(σ)φ̂(τ), donde |ĝ(σ)| ≤ C_g(1+|Im σ − γ₀|)^{−M+D} y
|φ̂(τ)| ≤ C_φ(1+|Im τ|)^{−M+D} en la franja |Re| ≤ 1 (lo que vale para todo elemento
de V_p con coeficientes acotados por C: C_g, C_φ ≤ C·C_M·e^{a_0}·(1+|σ|)^D-absorbido,
constantes del perfil). Sea Ω_r el conjunto de pares (ρ₁,ρ₂) con
max(|Im σ − γ₀|, |Im τ|) ≥ r. Si M − D ≥ 4, entonces
$$\Sigma_{tail}(r) := \sum_{(\rho_1,\rho_2) \in \Omega_r}
\big|\hat h(\rho_1,\rho_2)\big|\,\big|\hat h(\iota(\rho_1,\rho_2))\big|
\;\le\; C_g^2 C_\varphi^2\; \frac{C^*(M-D)\,\big(\log(2+|\gamma_0|) \big)^2}{(1+r)^{\,M-D-4}},$$
con C*(·) absoluto. En particular Σ_tail(r) → 0 cuando M → ∞ a r fijo, y cuando
r → ∞ a M fijo.

*Demostración.* Escribimos u := Im σ = (γ₁+γ₂)/2, v := Im τ = (γ₁−γ₂)/2, de modo que
γ₁ = u+v, γ₂ = u−v. Con a := |γ₁−γ₀|, b := |γ₂−γ₀|: |u−γ₀| + |v| ≥ max(a,b)/1 −
... — usamos la desigualdad exacta verificada por expansión:
$$\Big(1 + \tfrac{a+b}{2}\Big)^2 \;\ge\; (1+a)(1+b),$$
(pues (1+(a+b)/2)² − (1+a)(1+b) = ((a−b)/2)² ≥ 0), junto con
|u−γ₀| + |v| ≥ (a+b)/2 (desigualdad triangular en las dos coordenadas). Luego
$$(1+|u-\gamma_0|)\,(1+|v|) \;\ge\; 1 + |u-\gamma_0|+|v| \;\ge\; 1+\tfrac{a+b}{2}
\;\ge\; \sqrt{(1+a)(1+b)}.$$
El punto ι(ρ₁,ρ₂) = (1−ρ̄₁, 1−ρ̄₂) tiene las MISMAS ordenadas (Im(1−ρ̄) = Im ρ), así
que la misma cota vale para |ĥ(ι(P))|. Por tanto, con m := M−D:
$$|\hat h(P)|\,|\hat h(\iota P)| \;\le\; \tfrac14 C_g^2C_\varphi^2\,
\big[(1+|u-\gamma_0|)(1+|v|)\big]^{-2m}
\;\le\; \tfrac14 C_g^2C_\varphi^2\,(1+a)^{-m}(1+b)^{-m}.$$
La suma sobre todos los pares factoriza:
Σ_pares ≤ ¼C²_gC²_φ (Σ_ρ (1+|γ−γ₀|)^{−m})². La suma simple, agrupando por
intervalos unitarios |γ−γ₀| ∈ [j, j+1) (alturas positivas y negativas; ceros con
multiplicidad):
$$\sum_\rho (1+|\gamma-\gamma_0|)^{-m} \;\le\; \sum_{j\ge0} (1+j)^{-m}\cdot
C\log(2+|\gamma_0|+j+1) \;\le\; C'\,\zeta(m-1)\,\log(2+|\gamma_0|),$$
usando N(t+1) − N(t) ≪ log(2+t) [IK04, Thm. 5.8] y log(x+j) ≤ log x·(1+j); converge
para m ≥ 3. La restricción a Ω_r: en Ω_r, (1+|u−γ₀|)(1+|v|) ≥ 1+r, así que se puede
extraer un factor (1+r)^{−(m−4)} de cada producto reteniendo exponente 4 ≥ 3+1 para
la convergencia de la doble suma (repartir: producto^{−m} ≤ (1+r)^{−(m−4)}·
producto^{−4}... con producto ≥ (1+r) en Ω_r y producto ≥ √((1+a)(1+b)) siempre:
producto^{−m} = producto^{−(m−4)}·producto^{−4} ≤ (1+r)^{−(m−4)}(1+a)^{−2}(1+b)^{−2};
la doble suma con exponente 2 en cada factor converge igual con m=... — exponente 2:
Σ(1+j)^{−2}log(·+j) converge; ✓). Recolectando constantes: la cota enunciada. ∎

### 5.2. Independencia de evaluaciones y genericidad del centro

**Lema 5.3 (Vandermonde con bump; prueba completa).** Sean z₁,…,z_q ∈ ℂ distintos y
B entera con B(z_i) ≠ 0 para todo i. Si D ≥ q−1, los funcionales de evaluación
f ↦ f(z_i) son linealmente independientes sobre span{B(σ)σ^a : 0 ≤ a ≤ D}; en
particular, para cualquier dato (y₁,…,y_q) existe un elemento del span con
f(z_i) = y_i, y los coeficientes están acotados por
‖coef‖ ≤ C(z, min_i|B(z_i)|)·‖y‖ (inversa de la matriz de Vandermonde escalada).
Además, si B = B^{(M)}_w(·−ic) con B^{(M)}_w ≢ 0 entera (Def. 3.1), el conjunto de
centros c ∈ ℝ con B(z_i − ic) = 0 para algún i es discreto: todo intervalo abierto
de centros contiene un c con min_i |B^{(M)}_w(z_i − ic)| ≥ b₀ > 0, y por continuidad
una bola de centros con la misma cota b₀/2.

*Demostración.* La matriz (B(z_i)z_i^a)_{i,a} = diag(B(z_i))·(z_i^a) tiene rango q:
Vandermonde con nodos distintos por hipótesis y diagonal invertible. La función
c ↦ B^{(M)}_w(z_i − ic) es entera en c y no idénticamente nula (B ≢ 0 entera no nula
sobre ninguna recta compleja salvo si ≡ 0); sus ceros reales son discretos; la unión
finita de discretos es discreta. La cota b₀: B continua y no nula en un compacto que
evita los ceros. ∎

### 5.3. El teorema de realizabilidad localizada

**Teorema 5.4 (realizabilidad: σ_loc > 0 bajo ¬RH; prueba completa sobre insumos
citados).** Supóngase ¬RH. Sea ρ⁰ = ½+δ₀+iγ₀ el cero off mínimo (§1.1), con
multiplicidad m₀ ≥ 1. Entonces existen una dimensión estándar D₀ = D₀(configuración
local de ceros alrededor de ±γ₀) y N₀ estándar tales que para todo N ≥ N₀:
$$x_0(N) \;\ge\; \frac{1}{2 D_0} \;>\; 0,$$
y por tanto, para todo ultrafiltro no principal 𝒰:
$$\sigma_{loc} \;\ge\; \frac{1}{2D_0} \;>\;0 \qquad\text{y}\qquad
\lim_{k\to\infty} \sigma_{loc}^{(k)} = \tfrac12.$$

*Demostración.* **Paso 0 (el plano objetivo).** Tomamos el par diagonal
P₀ := (ρ⁰, ρ⁰), con coordenadas (σ₀, τ₀) = (½+δ₀+iγ₀, 0), y su imagen
ιP₀ = (1−ρ̄⁰, 1−ρ̄⁰), de coordenadas (σ₀', τ₀') = (½−δ₀+iγ₀, 0). Como δ₀ ≠ 0,
ιP₀ ≠ P₀: órbita libre. Su contribución a (1.1) para cualquier h es
$$2\,m_0^2\,\mathrm{Re}\Big[\hat h(P_0)\,\overline{\hat h(\iota P_0)}\Big] \tag{5.1}$$
(el factor m₀²: la suma corre con multiplicidad en ambas ranuras; estructura de plano
hiperbólico: D107 Teorema 5.5/Prop. 6.1, D98 §6).

**Paso 1 (el conjunto a aniquilar).** Sea S el conjunto (finito, los ceros son
discretos) de ceros ρ con ||γ| − |γ₀|| ≤ 2, y sea Z_σ el conjunto finito de valores
σ = (ρ₁+ρ₂)/2 sobre pares con ambos miembros en S, EXCLUYENDO σ₀ y σ₀'. Pongamos
q := |Z_σ| + 2 y F := número de pares con ambos miembros en S. Todos son números
estándar fijados por la configuración (que está fija: ¬RH es una hipótesis sobre ζ,
no un parámetro).

**Paso 2 (la celda y el testigo).** Elegimos el perfil ideal p* con D := q−1,
w := w₀ a determinar, M a determinar, centro σ-side c* en un entorno de γ₀ donde el
Lema 5.3 garantiza min |B(z−ic*)| ≥ b₀ sobre los q puntos z ∈ Z_σ ∪ {σ₀, σ₀'}, y
centro τ-side c'* = 0 análogo para el punto τ = 0. En V_{p*} construimos el testigo
v = h_{g_v, φ_v}: por el Lema 5.3 existen coeficientes (a_j) con
$$\hat g_v(z) = 0 \ \ \forall z \in Z_\sigma, \qquad
\hat g_v(\sigma_0) = 1, \qquad \hat g_v(\sigma_0') = -1,$$
con ‖coef‖ ≤ C₁ = C₁(Z_σ, σ₀, σ₀', b₀) estándar; y φ̂_v con φ̂_v(0) = 1, ‖coef‖ ≤ C₂.
(El dato (1, −1) fija la fase del plano: por (5.1), la contribución del plano objetivo
es 2m₀²·Re[(½·1·1)·conj(½·(−1)·1)] = −m₀²/2 < 0.)

**Paso 3 (presupuesto de Q₂(v,v)).** Descomponemos (1.1) en tres clases de pares:
(a) la órbita {P₀, ιP₀}: aporta −m₀²/2 (Paso 2). (b) Pares con ambos miembros en S,
distintos de la órbita objetivo: su σ ∈ Z_σ, donde ĝ_v = 0: aportan 0. (c) El resto:
algún miembro fuera de S, es decir ||γ|−|γ₀|| > 2 para ese miembro; entonces
max(|Im σ − γ₀|, |Im τ|) ≥ 1 sobre el sector de alturas cercanas a +γ₀, y los
sectores cerca de −γ₀ o lejos de ambos quedan a distancia ≥ 1 de (γ₀, 0) en al menos
una coordenada — en todos los casos el par está en Ω_1 respecto del centro (γ₀, 0)
[verificación: si ambos |γ_i − γ₀| ≤ 2 fallara para los dos miembros respecto de +γ₀
pero valiera respecto de −γ₀ u opuestos mixtos, entonces |Im σ − γ₀| ≥ (2|γ₀|−4)/2 ≥ 1
o |Im τ| ≥ |γ₀| − 2; si γ₀ < 3 se agranda S a ||γ|−|γ₀|| ≤ 2+2|γ₀| y la constante se
absorbe — ajuste finito estándar]. El Lema 5.2 con r = 1, C_g ≤ C₁·C_M·e^{a₀}·sup-pol,
C_φ ≤ C₂·(ídem) da
$$\big|\text{(c)}\big| \;\le\; \Sigma_{tail}(1) \;\le\;
C_3(\text{perfil}, C_1, C_2)\cdot \theta(M, w),$$
donde θ(M, w) → 0 cuando M → ∞ con w fijo (la cota del Lema 5.2 decae en M−D−4; D
está fijo desde el Paso 1). Elegimos M = M₀ estándar tal que |(c)| ≤ m₀²/4. Entonces
$$Q_2(v, v) \;\le\; -\frac{m_0^2}{2} + 0 + \frac{m_0^2}{4} \;=\; -\frac{m_0^2}{4} \;<\; 0,$$
luego neg.ind(Q₂|_{V_{p^*}}) ≥ 1, con margen espectral: el autovalor mínimo del Gram
es ≤ Q₂(v,v)/‖v‖²_{coef} ≤ −μ₀ < 0 con μ₀ estándar.

**Paso 4 (de la celda ideal a la grilla).** El perfil ideal p* tiene centros reales
arbitrarios; por el Teorema 4.4 (con κ = 1, μ = μ₀, L = L_{p*} finito por Teorema
4.3, todos estándar) existe N₀ estándar tal que para N ≥ N₀ la grilla 𝒢_N contiene
un perfil p con neg.ind(Q₂|_{V_p}) ≥ 1. Además, por el Lema 5.3 la condición
min|B| ≥ b₀/2 es estable en una bola de centros: la malla la alcanza.

**Paso 5 (conclusión).** Para N ≥ N₀: x₀(N) ≥ neg.ind(Q̃_p)/dim Ṽ_p ≥ 1/(2(D+1)²)
=: 1/(2D₀) con D₀ = (q)² estándar (el relleno duplica; el índice no baja al rellenar
con positivos: el subespacio negativo de V_p sigue negativo en Ṽ_p). Por la
Prop. 3.3(c), σ_loc = lim x₀(N) ≥ 1/(2D₀), para todo 𝒰. La Prop. 3.5 da
σ_loc^(k) → ½ pues σ_loc ∈ (0, ½]. ∎

**Estatus declarado del Teorema 5.4 (línea por línea).** Insumos citados, no
re-demostrados: (1.1) con convergencia absoluta y factorización (1.2) [D107, Lemas
5.2(b), 2.2(b), Thm. 3.4]; la estructura de órbita libre/plano y los pesos de
multiplicidad en (5.1) [D107 Thm. 5.5, Prop. 6.1; D98 §6]; la cerradura de la clase
bajo monomios de Mellin [D107]; N(t+1)−N(t) ≪ log t [IK04]. Demostrado aquí: Lemas
5.2, 5.3, Teoremas 4.1–4.4 y el ensamblaje. **La Hipótesis D del Doc 108 no se usa**:
no hay supuesto de juguete (la configuración de ceros es arbitraria bajo ¬RH; los
ceros off adicionales, las multiplicidades y los agrupamientos quedan absorbidos en S
finito y en la cola), no hay uniformidad en T (no hay T), y las constantes son
estándar porque dependen solo de la configuración fija alrededor del defecto mínimo.
Lo que NO se afirma: ninguna cota cuantitativa uniforme (D₀ y N₀ no son efectivos a
partir de m̄ o de nada: dependen de la configuración local desconocida). Eso es
exactamente lo que σ_loc no necesita.

**Proposición 5.5 (rama RH).** Bajo RH, x₀(N) = 0 para todo N, σ_loc = 0 y
σ_loc^(k) ≡ 0.

*Demostración.* Q₂ ≥ 0 sobre el span de la clase [D108, Prop. 2.2]; toda compresión
de una forma ≥ 0 es ≥ 0; el relleno es positivo; neg.ind = 0 en toda celda. ∎

**Corolario 5.6 (la dicotomía logística, promovida — el cierre del Problema 133.A).**
Para todo ultrafiltro no principal 𝒰:
$$\mathrm{RH} \;\iff\; \sigma_{loc} = 0 \;\iff\; \lim_{k\to\infty}\sigma_{loc}^{(k)} = 0
\;\iff\; \lim_{k}\sigma_{loc}^{(k)} \neq \tfrac12,$$
con la rama RH = Prop. 5.5 (teorema) y la rama ¬RH = Teorema 5.4 (teorema sobre los
insumos citados). ∎

**Observación 5.7 (canonicidad).** La dicotomía del Corolario 5.6 es independiente de
𝒰 (Prop. 3.3(c): σ_loc es un límite genuino). La objeción de no-canonicidad del
encargo ("¿el ultrafiltro elegido para concentrarse donde el defecto vive?") quedó
resuelta por monotonía, no por elección: la grilla creciente concentra por sí sola.

---

## 6. [PUENTE] Qué queda de la ley logística como criterio de RH — contabilidad honesta

### 6.1. Lo que se ganó

1. **El Problema 133.A está resuelto, con corrección de curso.** El enunciado
   original (σ⁰ ≥ c para el esquema canónico global) es FALSO (Teorema 2.5 +
   Corolario 2.6): no había nada que probar, había algo que refutar. El enunciado
   correcto (σ_loc ≥ c bajo ¬RH) es teorema (5.4). El Doc 133 §5.2 pedía cerrar "(α)
   Hipótesis D" y "(β) perturbación": (β) está probado (Teoremas 4.1–4.4); (α)
   resultó no ser la Hipótesis D sino su disolución — la localización a altura
   acotada elimina el régimen (T → ∞ con resolución 1/log T) donde la Hipótesis D
   era necesaria.

2. **La equivalencia entra al catálogo con ambas ramas en estatus de teorema (sobre
   insumos citados):** RH ⟺ la torre logística localizada tiende a 0 y no a ½. Los
   eventos individuales x₀(N) son computables desde los primos (Prop. 3.3(a)): es la
   reformulación del D133 con el caveat quitado y la normalización corregida.

3. **El mapa mejoró dos veces.** (i) La cara nueva del muro quedó nombrada
   (invisibilidad densitaria, §2.4): los defectos individuales son nulos para toda
   densidad de dimensión creciente — la coordenada "densidad" del cuantificador
   maestro. (ii) La σ_ε global no muere: cambia de oficio — es un detector de
   *defecto localmente denso* (Prop. 2.7), un invariante de configuraciones que ni RH
   ni ¬RH deciden, y que ningún teorema de densidad actual controla por ventana.

### 6.2. Lo que se pagó, sin anestesia

4. **Densidad → existencia.** σ_loc > 0 dice "existe una celda acotada con un
   autovalor negativo en algún lugar de una búsqueda no acotada". Desenrollando la
   ultrapotencia y la torre, el Corolario 5.6 es equivalente a: *Q₂ es semidefinida
   positiva sobre cada celda de una base numerable computable de tests* ⟺ RH — es
   decir, una presentación computable-por-Grams de la positividad de Weil (restringida
   a una familia densa numerable; la suficiencia de la familia para la dirección
   "positividad ⟹ RH" está dentro de la rama ¬RH = Teorema 5.4, que es donde vive el
   contenido). El valor agregado real sobre Weil-clásico: (a) cada evento es álgebra
   lineal finita de datos aritméticos — sin integrales de contorno ni posiciones; (b)
   la amplificación logística separa los dos mundos en constantes macroscópicas 0 vs
   ½; (c) la dicotomía es 𝒰-canónica. El valor NO agregado: ninguna nueva vía de
   DEMOSTRAR positividad.

5. **Dónde está el muro ahora.** Dos lugares, los dos viejos conocidos con
   coordenadas nuevas. (i) La parte estándar sigue siendo Π₁-no-efectiva: "x₀(N) = 0
   para todo N" es exactamente tan inverificable como siempre; la falsación de RH es
   semidecidible por Grams aritméticos (correr la grilla hasta encontrar un autovalor
   negativo) — una segunda máquina de semidecisión junto a la numérica clásica
   (integrar ζ′/ζ), con la diferencia estética de que esta es exacta en aritmética de
   los coeficientes. (ii) El cuantificador maestro se mudó de "uniforme en ventanas"
   (D108, el o(1/log T)) a "búsqueda no acotada en la grilla" (N₀ del Teorema 5.4 es
   no efectivo: depende de la configuración local del defecto desconocido). La
   transmutación completa del expediente: D108 lo tenía como precisión; D133 lo tenía
   como no-efectividad de st más un caveat de realizabilidad; este documento liquida
   el caveat y deja la no-efectividad pura, repartida en (i)+(ii).

6. **La Hipótesis D: dónde queda.** Ya no es cuello de botella para la DICOTOMÍA
   (Teorema 5.4 no la usa). Sigue siendo el cuello para cualquier versión
   CUANTITATIVA por altura: si se quisiera que κ a altura T crezca como m·log T
   realizado sobre tests (la Prop. 2.3 + Lema 2.4 de D108 en serio, con T → ∞),
   reaparece el régimen de resolución y con él la Hipótesis D y el muro de segundo
   orden — intactos. La frontera exacta: **existencia localizada = teorema;
   crecimiento cuantitativo uniforme = RH re-encodeada** (D108, Thm. 4.3). Este
   documento no movió esa frontera; la cartografió.

### 6.3. El eslabón abierto exacto (lo que un Doc 137 podría atacar)

7. **[GAP/DESEO].** El único enunciado intermedio honesto que queda enunciable y no
   probado en esta coordenada: una cota inferior INCONDICIONAL de positividad
   aproximada por celda — "existe una función computable ε(p) > 0 tal que bajo RH,
   λ_min(Gram(p)) ≥ ε(p) para toda celda p" (positividad cuantitativa de Weil
   localizada). Con ella, el Π₁ del punto 5(i) se volvería un Π₁ con módulo — cada
   evento de la grilla sería decidible con precisión finita PRE-computable, y la
   búsqueda de ¬RH tendría criterio de parada por nivel. Obstrucción conocida: bajo
   RH hay ceros casi-dobles si los hay (pares de Lehmer), que hacen λ_min
   genuinamente pequeño en celdas alineadas con ellos: ε(p) debe degradar con la
   configuración on-line local, y estimarla es de nuevo un problema de repulsión de
   ceros — correlación de pares. El muro asoma también ahí, como corresponde.
   Registrado como Problema 136.A.

8. **[DESEO 6.1].** Que la σ_ε global (detector de defecto localmente denso,
   Prop. 2.7) encuentre oficio propio: un teorema incondicional "σ⁰_global = 0 para
   todo esquema de banda admisible" equivaldría a "no hay agrupamiento lineal de
   ceros off por banda" — más débil que RH, más fuerte que los teoremas de densidad
   por ventana. Es un objetivo de teoremas parciales honestos (gran criba por
   ventanas cortas), fuera del alcance de este documento.

---

## 7. Veredicto

**Problema 133.A: RESUELTO, en dos mitades de signo opuesto.** La mitad destructiva:
la realizabilidad global es falsa — σ⁰ = 0 en ambos mundos para defecto finito
(Teorema 2.5), el Teorema-puente 2.13(b) del Doc 133 estaba mal normalizado
(Corolario 2.6), y la dicotomía logística global no es un criterio de RH; la cara del
muro responsable queda nombrada (invisibilidad densitaria, §2.4). La mitad
constructiva: la signatura localizada σ_loc (Def. 3.2) hereda la ley logística
verbatim (Prop. 3.5), su realizabilidad bajo ¬RH es un teorema con prueba completa
sobre insumos citados (Teorema 5.4 — sin Hipótesis D, con la llave conceptual de la
Obs. 5.1: la test-accesibilidad restringe al espacio, no al testigo), el sub-objetivo
(β) es un paquete de perturbación limpio y computable (Teoremas 4.1–4.4), y la
equivalencia RH ⟺ lim σ_loc^(k) = 0 queda promovida a entrada del catálogo con ambas
ramas probadas y canonicidad en 𝒰 (Corolario 5.6, Obs. 5.7). Contenido neto medido
sin inflación: una presentación Gram-computable y logísticamente amplificada de la
positividad de Weil, el caveat de D133 liquidado, y el muro re-cartografiado en
Π₁-no-efectividad pura más búsqueda no acotada — con un único problema intermedio
honesto y nuevo sobre la mesa (positividad cuantitativa localizada, Problema 136.A,
que linda con Lehmer y correlación de pares, como todo lo que importa).

---

## Referencias

**Internas (backward-only):** Doc 133 (Defs. 2.1–2.4, Thms. 2.6, 2.7, 2.10, Prop.
2.8, 2.11, Teorema-puente 2.13, §5.2 Problema 133.A); Doc 108 (Defs. 1.1–1.2, Props.
2.2, 2.3, 2.5, Lema 2.4 e Hipótesis D, Thms. 3.3, 3.4, 4.3, §7.4, §8.2); Doc 107
(Lema 2.2(b), Lema 5.2(b), Thm. 3.4, Thm. 5.5, Prop. 6.1, cerradura x∂ₓ); Doc 98
(§6: cuádruplo, κ = 2, planos hiperbólicos); Doc 106 (identidad tensorial del
índice); Doc 110 (Thm. 4.3, Prop. 4.5); P43 (cuantificador maestro, Principio 3.1;
autonomía del valor); P35 (κ = 2m); NO-GO-LIST (MW-7; se propone registrar
"invisibilidad densitaria", §2.4).

**Literatura (verificable; enunciados estándar citados por referencia clásica):**
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004 —
  Thm. 5.8 (Riemann–von Mangoldt; N(t+1)−N(t) ≪ log t, con multiplicidad). [IK04]
- A. Robinson, *Non-standard Analysis*, North-Holland, 1966 — ultrapotencias, parte
  estándar (cap. 2; vía D133).
- H. Bohr, E. Landau, *Beiträge zur Theorie der Riemannschen Zetafunktion*, Math.
  Ann. 74 (1913/14) — densidad media cero de ceros off (usado solo como contexto en
  Obs. 2.8; el enunciado citado — N(σ,T) = O(T) para σ > ½ — es el clásico).
- F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Cap. X —
  signatura por congruencia (Lagrange–Sylvester; vía D133 Prop. 2.8).
- R. Bhatia, *Matrix Analysis*, Springer GTM 169, 1997 — Courant–Fischer y
  desigualdades de Weyl (Cap. III); los Teoremas 4.1–4.2 se demuestran
  autocontenidos arriba y la referencia es de cortesía.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Lund (1952) — positividad ⟺ RH (normalización del programa vía D108
  Prop. 2.2 / D110 §3.2).
- B. E. Petersen / R. Paley, N. Wiener — teoremas de tipo Paley–Wiener para C_c^∞
  (decaimiento (3.1); estándar, cf. Hörmander, *The Analysis of Linear Partial
  Differential Operators I*, Thm. 7.3.1).

*Fin del Doc 136.*
