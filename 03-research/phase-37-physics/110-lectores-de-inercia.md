# Doc 110 — Invariantes que cuentan modos uno a uno: el principio del argumento, el flujo espectral y la especificación del lector de inercia

**Programa:** Hipótesis de Riemann — Phase 37, "modo físico"
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** P43 (§4 valor vs inercia, §6 principio de frontera); Doc 108 (autonomía del valor ≠ autonomía de la inercia; binariedad de índices por ventana; Teoremas 3.3, 3.4, Prop. 2.3, 2.5); Doc 107 (W₂, nueve bloques, Prop. 6.1); Doc 106 (identidad tensorial, amplificación); Doc 100 (índice de Maslov semilocal, lema de agotamiento, Conjetura 100.A); Doc 99 (CCM-ZST, rigidez CF, ruta E5: κ_λ(N)); Doc 96 (Teorema 8.1); P35 (κ(Q) = 2m); P41 (no-go interior/frontera); NO-GO-LIST (MW-1…MW-7).
**Regla absoluta:** ninguna prueba se fabrica. Cada paso es demostración completa, enunciado de literatura con referencia verificable, o GAP declarado. Sin numéricos, sin simulaciones. Citas backward-only; lo no verificado se marca [NO VERIFICADO].

---

## 0. Resumen ejecutivo

P43 cerró el programa con el cuantificador maestro: todos los métodos fallan porque
certifican el lado promediado de un enunciado cuyo refinamiento individual es RH. Pero la
matemática tiene objetos que cuentan **sin promediar**: números de enrollamiento, flujos
espectrales, índices de Fredholm, clases de K-teoría. Un entero no se promedia: se lee.
Este documento examina por qué ninguno de esos enteros resuelve RH, localiza el punto de
falla de cada uno, y produce la contribución central: la **especificación axiomática del
lector de inercia** (axiomas L1–L6) y un **teorema de imposibilidad** en la clase de los
funcionales cuadráticos aritméticos. Hallazgos, en orden:

1. **(§2) El principio del argumento, en serio: el entero es individual y decidible
   caja por caja (método de Turing), pero su EVALUACIÓN uniforme exige o cotas
   puntuales en la franja (RH-strength) o promediar (lema de Littlewood → densidad
   de ceros: se pierde la individualidad).** Lema 2.4 ("lema de no-evaluación"): la
   brecha numérica es exactamente la del Doc 108 — el enrollamiento por caja se
   conoce con error O(log T) y distinguir 0 de ≥1 requiere error < 2π: precisión
   relativa o(1/log T), la escala de la Conjetura 108-N. El muro del enrollamiento
   ES el muro de la criba con coordenadas de contorno.

2. **(§2.6) La obstrucción de paridad es vacua.** La simetría cuádruple fuerza
   N_off ≡ 0 (mod 2) en cajas simétricas en t — incondicionalmente, en ambos mundos:
   un invariante constante no detecta nada (Prop. 2.6). Mod 4 equivale a la paridad
   de la semicaja superior, que ninguna simetría conocida determina (GAP). Y la
   lectura de paridad vía cambios de signo de la Z de Hardy se rompe exactamente en
   la **partición** on/off — la no-autonomía de la inercia del Doc 108 en
   coordenadas de paridad (Obs. 2.7).

3. **(§3) El flujo espectral de la filtración de Euler reformula RH exactamente
   (Teorema 3.2, incondicional): RH ⟺ sf{A_λ} = 0, con A_λ el operador semilocal de
   CCM-ZST y los primos entrando uno a uno en λ = √p por localidad automática del
   soporte.** Bajo ¬RH el cruce ocurre en un λ₀ **finito**: el evento es individual.
   El muro: λ₀ depende de la altura del cero desconocido, el flujo por paso de los
   aproximantes CF es 0 incondicionalmente (rigidez de Carathéodory–Fejér: ceros de
   los H_x reales en todo paso finito), y el paso al límite del flujo requiere el
   gap uniforme — MW-6 literal (Prop. 3.4).

4. **(§4) Especificación del lector de inercia: axiomas L1–L6.** El refinamiento
   clave es el axioma de **finitud** (L6): I debe factorizar por un objeto de
   dimensión finita acotada **a priori** (sin posiciones de ceros) con trazas
   aritméticas. Teorema 4.3 (imposibilidad, clase ℱ): para I = neg.ind(Q|_V′) con Q
   de tipo fórmula explícita y V′ test-accesible, (L2)+(L3)+(L4) son
   **inconsistentes** — lo fuerza la dicotomía sub-resolución/resolución del
   Doc 108. Prop. 4.5 (contraejemplo abstracto): en **rango finito a priori** la
   inercia SÍ es autónoma — las identidades de Newton convierten finitas trazas
   (valores) en la signatura (inercia). Corolario 4.6: la especificación es
   consistente si y solo si incluye un teorema de finitud; el lector de inercia, si
   existe, es cohomológico en el sentido preciso de L6.

5. **(§5) Connes–Consani, medido contra la especificación: lo que falta es
   exactamente L6 con trazas de Lefschetz y la positividad de L3 — la forma
   "conjeturas estándar sobre Spec ℤ".** Su Riemann–Roch tropical produce
   características de Euler (valores); no una signatura con positividad. Obs. 5.3:
   la amplificación tensorial de la Forma B (Docs 106–108) es el truco de Deligne
   **menos la finitud** — y murió precisamente por eso.

6. **(§6–§7) Pasado todo por el cuantificador maestro: cada candidato cae en la
   misma inversión, pero el pasaje deja un residuo nuevo — RH es una conjunción
   numerable de eventos enteros individualmente decidibles (Π₁ manifiesto en dos
   coordenadas: cajas y pasos primos), y el muro es la ausencia de una razón LOCAL
   (curvatura, positividad por paso) que fuerce cada entero a 0.** En cuerpos de
   funciones esa razón existe (Castelnuovo). VEREDICTO: **PARCIAL** (§7).

---

## 1. Marco: la pregunta física

P43 §6 (principio de frontera): el mecanismo faltante debe **leer inercia, no
valor** — individuar una signatura donde solo una traza está disponible
incondicionalmente; la pista histórica es la cohomología ℓ-ádica, que en cuerpos de
funciones da una signatura entera directamente. El Doc 108 §7.4 dio la fórmula:
*autonomía del valor ≠ autonomía de la inercia* — el lado aritmético computa el
total de la ventana, no la partición en bloques.

La pregunta de este documento: la matemática posee invariantes que cuentan modos
**uno a uno, sin promediar** — el número de enrollamiento (principio del argumento:
cuenta ceros exactamente), el flujo espectral de una familia de operadores
autoadjuntos (cuenta cruces de autovalores por 0; [APS76], [Phi96], [RS95]), el
índice de Fredholm y sus localizaciones (Atiyah–Singer [AS63]: índice analítico =
índice topológico, suma de contribuciones locales), las clases de K-teoría y las
cargas topológicas de la física (cuantizadas, estables bajo deformación). ¿Por qué
ninguno de estos lee la inercia de ζ? La respuesta no es "porque sí promedian" (el
cuantificador maestro como mantra); es una disección de **dónde**, en cada caso, la
lectura del entero se convierte en un problema de promedios, y qué axioma exacto
falla. El residuo positivo es la especificación de §4.

---

## 2. (i) El principio del argumento, tratado en serio

### 2.1. El entero

Para σ₀ ∈ (1/2, 1) y 0 < T₁ < T₂, sea R = [σ₀, 2] × [T₁, T₂] (sin ceros en el
borde — asegurable moviendo T₁, T₂ en o(1)). El principio del argumento da

$$N_{\mathrm{off}}(R) \;=\; \frac{1}{2\pi i}\oint_{\partial R}\frac{\zeta'}{\zeta}(s)\,ds
\;=\; \frac{1}{2\pi}\,\Delta_{\partial R}\arg\zeta \;\in\; \mathbb{Z}_{\geq 0},$$

el número exacto de ceros de ζ en R, contados con multiplicidad. Es un número de
enrollamiento: el grado de la curva ζ(∂R) alrededor de 0. Individual, entero, no
promediado, estable bajo perturbaciones del contorno que no cruzan ceros. Y

$$\mathrm{RH} \iff N_{\mathrm{off}}(R) = 0 \ \text{ para todo rectángulo } R
\text{ a la derecha de la línea crítica}.$$

RH es la anulación de una familia numerable de enrollamientos (basta σ₀, T_i ∈ ℚ).
Nada más individual: cada cero off-crítico, si existe, aporta su unidad entera a
algún R. ¿Por qué no podemos evaluar el entero?

### 2.2. Inventario de control de los cuatro lados

Escribimos Δ_L arg ζ para la variación del argumento a lo largo del lado L, de modo
que 2π N_off(R) = Δ_der + Δ_sup + Δ_izq + Δ_inf.

**(a) Lado derecho, Re s = 2 (de 2+iT₁ a 2+iT₂): control O(1), incondicional y
uniforme.** Sobre Re s = 2 el producto de Euler converge absolutamente y
|log ζ(2+it)| ≤ Σ_p Σ_k p^{-2k}/k = log ζ(2) < ∞, de donde
|Δ_der| ≤ 2 log ζ(2) — una constante absoluta, independiente de T. Este lado está
"comprado" por la región de convergencia absoluta: es la única porción del contorno
que un primo individual controla (cf. MW-2).

**(b) Lados horizontales, t = T_j (de 2+iT_j a σ₀+iT_j): control O(log T),
incondicional.** Argumento clásico de Backlund/von Mangoldt ([Tit86, §9.4]): la
variación de arg ζ sobre el segmento está acotada por π(1 + número de ceros de
Re ζ(σ+iT_j) en σ ∈ [σ₀,2]), y ese número se acota por Jensen aplicado a
½(ζ(s+iT_j) + ζ(s̄+iT_j)) en un disco centrado en 2: |Δ_sup|, |Δ_inf| = O(log T_j),
válido si el segmento no pasa por un cero. "Típicamente" no es mejorable: la
variación alcanza ≍ log T cuando el segmento pasa cerca de ≍ log T ceros (densidad
de von Mangoldt N(T+1) − N(T) ≍ (1/2π) log T).

**(c) Lado izquierdo, Re s = σ₀ (de σ₀+iT₂ a σ₀+iT₁): aquí vive todo el problema.**
La variación es π[S(σ₀,T₂) − S(σ₀,T₁)] con S(σ,T) := (1/π) arg ζ(σ+iT) (rama
continua desde 2+iT). Lo que se sabe:

- **Incondicional, puntual:** S(σ,T) = O(log T), uniforme en σ ≥ 1/2 (Backlund
  corrido a la abscisa σ; [Tit86, Thm. 9.4] y la observación estándar de
  uniformidad). Nada puntualmente mejor se conoce para σ₀ ∈ (1/2, 1) fijo sin
  hipótesis. Bajo RH: S(T) = O(log T / log log T) (Littlewood; [Tit86, Thm. 14.13]).
- **Incondicional, en media:** S₁(T) := ∫₀^T S(t)dt = O(log T) ([Tit86, Thm. 9.9]):
  el promedio de S sobre [0,T] es o(1). Selberg [Sel46]: ∫₀^T |S(t)|^{2k} dt ∼
  c_k T (log log T)^k — S es en media de tamaño √(log log T). **El promedio de S es
  minúsculo; su valor puntual solo se sabe O(log T).** Toda la información
  individual (las posiciones de los ceros) vive en la diferencia entre valor y
  media — exactamente la estructura valor/inercia.

### 2.3. El punto preciso donde el entero se vuelve promedio

La integral del argumento sobre el lado izquierdo es **una suma de saltos
individuales**: por la identidad de Hadamard ζ'/ζ(s) = Σ_ρ [1/(s−ρ) + 1/ρ] +
O(log|s|), la contribución de cada cero a la variación sobre el lado izquierdo es el
ángulo subtendido por el segmento visto desde ρ — cercano a 2π·(fracción del
enrollamiento) si ρ está a la derecha y cerca del lado, cercano a 0 si está lejos.
**Para acotar la suma de los ángulos hay que saber dónde están los ceros: el entero
individual se evalúa solo conociendo a los individuos.** Las dos únicas rutas
conocidas para extraer algo del lado izquierdo:

**(α) Cotas puntuales en la franja.** Si se supiera ζ(s) ≠ 0 en Re s > σ₀ con cota
inferior |ζ(σ₀+it)| > exp(−φ(t)) controlada, arg ζ se seguiría por integración de
ζ'/ζ por una región libre de ceros. Pero "ζ no se anula en Re s > σ₀" **es** la
cuasi-RH a nivel σ₀: la entrada necesaria es (una versión de) la conclusión.

**(β) Promediar en σ: el lema de Littlewood.** La herramienta incondicional estándar
([Tit86, §9.9]; [IK04, Thm. 5.12 y Cap. 10]) es

$$2\pi \int_{\sigma_0}^{2} N_{\mathrm{off}}(\sigma, T)\, d\sigma
\;=\; \int_{0}^{T}\log|\zeta(\sigma_0+it)|\,dt \;+\; O(\log T).$$

El lado derecho es un **valor medio** de log|ζ| sobre el lado izquierdo, accesible
por momentos de ζ: así se prueban TODOS los teoremas de densidad de ceros,
N(σ,T) ≪ T^{κ(σ)}(log T)^{O(1)} ([Ing40], [IK04, Cap. 10]). Nótese qué
pasó: el entero individual N_off(σ₀,T) fue reemplazado por su **promedio en σ** — un
promedio de enrollamientos sobre rectángulos anidados. El promedio es evaluable; el
individuo no: un solo cero en β = σ₀ + ε aporta a la integral una masa ε que se
ahoga en el error O(log T).

### 2.4. El lema de no-evaluación

**Lema 2.4 (no-evaluación del enrollamiento).** Sea R_T = [σ₀,2] × [T, T+1] la caja
de altura unidad. Entonces:

(a) *El presupuesto incondicional del contorno es O(log T):* las cotas de §2.2 dan
|2π N_off(R_T)| ≤ |Δ_der| + |Δ_sup| + |Δ_inf| + |Δ_izq| = O(log T), y este orden se
alcanza (lado izquierdo y horizontales realmente fluctúan a escala log T).

(b) *La detección requiere precisión absoluta < 2π:* distinguir N_off(R_T) = 0 de
N_off(R_T) ≥ 1 exige evaluar Δ_izq con error absoluto < 2π, es decir **error relativo
o(1/log T) sobre el presupuesto del lado** — la misma escala de precisión de segundo
orden de la Conjetura 108-N (Doc 108, ec. (4.1)).

(c) *Dicotomía de evaluación:* toda ruta de evaluación de Δ_izq conocida es de uno de
dos tipos. (α) puntual: requiere una región libre de ceros a la derecha de σ₀ con
cota inferior de |ζ| — un enunciado de fuerza cuasi-RH al nivel σ₀ (la conclusión como
insumo); o (β) promediada: integra en σ (Littlewood) o en t (momentos de S, Selberg)
y produce teoremas de densidad — válidos para **casi toda** caja, sin información
sobre la caja individual alineada con el cero hipotético. La caja excepcional que la
media no controla es exactamente donde vive la señal.

*Demostración.* (a) es §2.2. (b): N_off es entero ≥ 0; 0 vs ≥1 es un gap absoluto
de 2π en 2πN_off; los otros tres lados se evalúan con error O(1) (lado derecho:
producto de Euler; horizontales: la reducción estándar — mover σ₀ en o(1) para
esquivar ceros de Re ζ — deja el peso de la detección en Δ_izq). Para (c) no
afirmamos clasificar "todas las rutas posibles" (no demostrable); afirmamos, con
prueba, que las dos rutas de la literatura tienen esos perfiles: (α) integrar ζ'/ζ
necesita un dominio sin ceros de ζ más una cota inferior para fijar la rama — y
"sin ceros a la derecha de σ₀" es N_off = 0, lo que se quería evaluar; (β) el lema
de Littlewood tiene por lado evaluable un promedio en σ, y los momentos de Selberg
son promedios en t; ninguno separa la caja individual (Doc 108 §5.2: el paso de
"casi toda" a "toda" es la teoría de valores grandes, y bajo ¬RH el valor grande
está exactamente en la frecuencia del cero off). ∎

**Observación 2.5 (el entero es decidible caja por caja; el muro es el cuantificador,
no la decisión).** Honestidad obligada: para cada caja FIJA R_T, el entero N_off(R_T)
**sí es computable** — es lo que hace el método de Turing [Tur53], con el que RH está
verificada hasta altura 3·10¹² [PT21]: un cómputo finito por caja. Lo que no existe
es una **evaluación uniforme**: un argumento que dé N_off(R_T) = 0 para TODA T de una
vez. RH es así una conjunción numerable de eventos enteros individualmente decidibles
— un enunciado Π₁ manifiesto — y el Lema 2.4 dice que el paso de "cada uno, por
cómputo" a "todos, por una razón" es la inversión del cuantificador maestro. El
enrollamiento no esquiva el muro: lo presenta en coordenadas lógicas. Aporta, eso sí,
la **individualidad de la falsación**: un solo cómputo puede refutar RH; ninguno
puede probarla.

### 2.6. La obstrucción de paridad: análisis y cierre

¿Se puede evaluar el enrollamiento MÓDULO algo? La esperanza: una simetría que
determine N_off mod 2 (o mod 4) sin evaluar la integral.

**Proposición 2.6 (la paridad forzada es vacua).** Sea R^sim = [σ₀,2] × [−T,T] la
caja simétrica respecto del eje real (sin ceros en el borde). Entonces
N_off(R^sim) ≡ 0 (mod 2), incondicionalmente. La misma conclusión para cualquier caja
simétrica en t. En cambio, para cajas superiores R = [σ₀,2] × [T₁,T₂] con T₁ > 0,
ninguna simetría de ζ liga N_off(R) con N_off de la misma caja: las simetrías
disponibles, s ↦ s̄ (realidad: ζ(s̄) = conj ζ(s)) y s ↦ 1−s (ecuación funcional),
mandan R a su reflejo en el eje real (disjunto de R) y a su reflejo a la izquierda de
la línea crítica (disjunto de R), respectivamente. En particular: (a) el mod 2 de la
caja simétrica es 0 en ambos mundos (RH y ¬RH) — un invariante idénticamente nulo no
detecta nada; (b) N_off(R^sim) mod 4 = 2·N_off(R^sup) mod 4 equivale a la paridad del
conteo de la semicaja superior, que por (la segunda parte) ninguna simetría conocida
determina. GAP ABIERTO (sin candidato): no se conoce obstrucción de paridad
explotable.

*Demostración.* La realidad de ζ da: ρ cero ⟺ ρ̄ cero, con igual multiplicidad. La
caja simétrica es estable bajo conjugación y sin ceros reales (ζ(σ) ≠ 0 en (0,1),
[Tit86, §2.12]): los ceros van en pares {ρ, ρ̄} de órbita libre, conteo par. Para
(b): la involución ρ ↦ 1−ρ̄ intercambia los semiplanos y no actúa dentro de R^sup.
Que "ninguna simetría conocida" determine la paridad superior es inventario, no
teorema: las simetrías exactas de ζ son las generadas por s ↦ s̄ y s ↦ 1−s. ∎

**Observación 2.7 (dónde se rompe la lectura de paridad: en la partición, otra
vez).** Hay una paridad que SÍ se lee individualmente: la de N(T) total. La función
de Riemann–Siegel Z(t) es real, |Z(t)| = |ζ(½+it)|, su signo es computable
puntualmente, y N(T) = (1/π)θ(T) + 1 + S(T) con θ explícita — el método de Turing
explota esto. Pero la paridad que necesitamos es la de N_off = N − N₀ (N₀ = ceros
en la línea), y los cambios de signo de Z dan solo **cota inferior** de N₀ (un cero
de multiplicidad par o un par off-crítico simétrico no cambian el signo). Leer la
paridad de N_off exige separar el conteo total en bloques on/off — **la misma
partición que el Doc 108 §7.4 identificó como no-autónoma para la inercia de Q₂**.
La paridad no es una puerta lateral: es la inercia mod 2, y hereda su no-autonomía.
La simetría mata la parte impar (Prop. 2.6(a)) y la parte par es invisible para
todo argumento de paridad — estructuralmente idéntico al principio de paridad de
Selberg en el Arc A (P43 §3.2): la simetría determina la paridad, y la paridad así
determinada no distingue los mundos.

### 2.8. Dictamen parcial (i)

El principio del argumento no es trivialidad ni salida: es el cuantificador maestro
en su forma más limpia. El entero existe, es individual, es decidible caja por
caja; su evaluación uniforme exige (α) la conclusión como insumo o (β) promediar y
perder al individuo; su mod 2 es vacuo por simetría; su mod 4 equivale a una
partición no-autónoma. Aporte neto: la identificación cuantitativa con el Doc 108
(precisión relativa o(1/log T) en ambos) y la forma Π₁ explícita de RH como familia
de enteros decidibles (Obs. 2.5), que §3 reencontrará.

---

## 3. (ii) Flujo espectral de la filtración de Euler

### 3.1. La familia aritmética es la familia analítica: localidad automática

El input verificado (Doc 99, §2, contra arXiv:2511.22755): CCM-ZST construyen, para
cada λ > 1, la forma de Weil semilocal QW_λ = restricción de la forma de Weil
completa a L²([λ^{-1}, λ], d*u), con la **localidad automática**: si supp f ⊆
[λ^{-1},λ], entonces W_p(f^* * f) = 0 para todo p^m > λ². El "producto de Euler
truncado en p ≤ λ²" no es una mutilación: es un teorema de soporte. QW_λ define un
operador autoadjunto A_λ de espectro discreto acotado inferiormente, con
μ_λ := inf spec(A_λ) **decreciente en λ** (CCM-ZST ec. (3.27), via Doc 99), y

$$\lim_{\lambda\to\infty}\mu_\lambda \geq 0 \iff \mathrm{RH}$$

(⟸: criterio de Weil restringido; ⟹: CCM-ZST Cor. 3.8; véase Doc 99 §2.2).

Consecuencia estructural: **la familia aritmética ζ_S → ζ_{S∪{p}} y la familia
analítica λ → λ′ son la misma familia.** El primo p entra exactamente cuando λ
cruza √p: la filtración de Euler está realizada como un camino continuo de formas
cuadráticas — el escenario canónico del flujo espectral [Phi96], [RS95].

### 3.2. RH como anulación del flujo espectral: teorema exacto

Definición (estándar, [Phi96]): para un camino {B_t} de operadores autoadjuntos con
espectro discreto semiacotado, el flujo espectral sf{B_t} a través de 0 es el número
neto de autovalores que cruzan 0 hacia abajo menos hacia arriba, contado con
multiplicidad. Para nuestro camino conviene la versión "conteo de entrada": como
μ_λ es monótona decreciente, los autovalores solo pueden cruzar 0 hacia abajo.

**Teorema 3.2 (RH = flujo espectral nulo de la filtración de Euler;
incondicional).** Sea {A_λ}_{λ>1} la familia CCM-ZST. Entonces:

(a) Bajo RH, μ_λ ≥ 0 para todo λ; ningún autovalor cruza 0; sf{A_λ : λ ∈ (1,Λ]} = 0
para todo Λ.

(b) Bajo ¬RH, existe λ₀ < ∞ **finito** tal que μ_λ < 0 para todo λ > λ₀: el primer
cruce ocurre en un parámetro finito, y sf ≠ 0 ya en el segmento (1, λ₀ + ε].

(c) Por tanto: RH ⟺ sf{A_λ} = 0 sobre todo segmento finito ⟺ el flujo espectral
total de la filtración de Euler es 0.

*Demostración.* (a) RH ⟹ positividad de Weil sobre C_c^∞(ℝ₊*) (Weil 1952; en la
normalización CC: Doc 100, Lema 2.0) ⟹ QW_λ ≥ 0 para todo λ (restricción de una
forma positiva) ⟹ μ_λ ≥ 0. (b) ¬RH ⟹ existe f ∈ C_c^∞(ℝ₊*) con QW(f,f) < 0
(criterio de Weil, contrapositivo); supp f ⊆ [λ₀^{-1}, λ₀] para algún λ₀ finito;
entonces μ_{λ₀} ≤ QW(f,f)/‖f‖² < 0, y por monotonía μ_λ < 0 para λ ≥ λ₀. Como
μ_λ ≥ 0 para λ < √2 (ANTES del primer primo solo hay términos polares/arquimedianos:
la positividad arquimediana de CC 2021 cubre soporte en (1/2,2) — Doc 100 §2), el
camino empieza con μ ≥ 0 y termina con μ < 0: hay cruce, sf ≠ 0. (c) es (a)+(b). ∎

Tres comentarios exactos:

1. **El evento es individual y finito.** Bajo ¬RH, el cruce ocurre en λ₀ finito, en
   el paso en que la ventana [λ₀^{-1}, λ₀] alcanza a resolver el cero off-crítico:
   un evento contable, de multiplicidad entera, detectable por un cómputo (de
   nuevo: falsable, no certificable).

2. **El flujo por paso primo está bien definido.** sf_p := sf{A_λ : λ ∈ [√p, √p′]}
   (p′ = primo siguiente) es un entero por paso; RH ⟺ sf_p = 0 para todo p Y no hay
   cruce en el límite. Es la versión "filtración de Euler" del índice de Maslov
   semilocal del Doc 100 (§3, con su lema de agotamiento κ(Q) = lim_n κ(Q|_{𝒟_n})
   demostrado allí) y del objeto E5 del Doc 99 (κ_λ(N)).

3. **El caso base está probado.** sf = 0 en el tramo sin primos (λ < √2) es el
   teorema arquimediano incondicional (Yoshida 1992; Connes–Consani, Selecta 2021;
   Doc 100 §§2, 4: μ_∞ = 0 con mecanismo operatorial). El primer paso aritmético,
   sf₂ = 0 (un solo primo), es exactamente la Conjetura 100.A — abierta, falsable,
   con la infraestructura construida en la literatura (CCM 2024).

### 3.3. Los aproximantes CF tienen flujo cero en cada paso — y por qué eso no suma

Doc 99 (§§2–4, verificado contra CCM-ZST y CvS): los truncados QW_λ^N tienen
estructura de Loewner τ_ij = (b_i − b_j)/(i−j); la rigidez de Carathéodory–Fejér
generalizada (Connes–van Suijlekom) aplicada al shiftado QW_λ^N − ε_N ≥ 0 produce
operadores autoadjuntos H_x cuyo determinante regularizado tiene **todos los ceros
reales, incondicionalmente, para todo paso finito**. *El espectro de los
aproximantes nunca delata el cruce*: la negatividad, si existe, vive en μ_λ < 0 (el
shift ε_N la absorbe), no en ceros no-reales del aproximante. La pregunta del
encargo — "¿los aproximantes CF tienen flujo CERO en cada paso, y RH es 'flujo
total de la filtración = 0', con el problema en el límite?" — se responde: **sí, y
el problema en el límite es MW-6 en forma literal.**

**Proposición 3.4 (la suma telescópica no converge sin el gap uniforme).** Sea
sf_p el flujo por paso primo (§3.2) y sea sf^∞ el flujo del camino completo
(equivalentemente, por el lema de agotamiento del Doc 100 §3, κ(Q) = 2m). Entonces:

(a) La identidad telescópica sf^∞ = Σ_p sf_p vale **si** los cruces ocurren en
parámetros finitos — y bajo ¬RH eso es exactamente lo que pasa (Teorema 3.2(b)):
la serie detecta el cruce en el paso finito p ≈ λ₀². No hay aquí pérdida en el
límite: ¬RH es visible en tiempo finito.

(b) Lo que NO es computable es el valor de cada sumando: certificar sf_p = 0
requiere una cota inferior μ_λ ≥ 0 en el tramo [√p, √p′], es decir, la positividad
semilocal de Weil con p primos — cuyo caso p = 2 ya es la Conjetura 100.A abierta, y
cuya versión uniforme en p es lim μ_λ ≥ 0 = RH (MW-1 semilocal = MW-6; Doc 99
§2.2). El flujo por paso es un entero individual cuya evaluación por paso es un
problema de positividad por paso, y la cadena de positividades por paso, sin una
razón estructural uniforme, es la conjunción Π₁ de la Obs. 2.5 con otra coordenada.

(c) La aproximación por truncados N finitos agrega el límite interno: el flujo de
QW_λ^N converge al de QW_λ si hay gap espectral uniforme en N en torno a 0 (el flujo
espectral no es continuo bajo convergencia fuerte de resolventes sin gap; [Phi96] da
la continuidad EN presencia de gap). La cota uniforme del paquete negativo κ_λ(N) es
exactamente el objeto E5 del Doc 99, no iniciado, con la advertencia registrada allí:
una cota inferior creciente incondicional de κ_λ(N) que sobreviva N → ∞ refutaría
RH; una cota superior → 0 la probaría. GAP ABIERTO en ambas direcciones.

*Demostración.* (a): Teorema 3.2(b) + aditividad del flujo en concatenación de
caminos [Phi96]. (b): sf_p = 0 ⟺ μ_{√p′} ≥ 0 (monotonía) = positividad de QW con
primos ≤ p′; la identificación con 100.A y MW-6 es Doc 100 §6 y Doc 99 §2.2. (c):
contraejemplos estándar de discontinuidad del flujo sin gap; la condición
suficiente de gap es [Phi96]. ∎

### 3.5. Qué significa, entonces, el flujo espectral de la filtración de Euler

Síntesis del frente (ii): el flujo espectral SÍ es el invariante correcto en un
sentido preciso — reformula RH **exactamente** (Teorema 3.2, incondicional, nuevo en
esta forma aunque ensamblado de piezas conocidas), convierte ¬RH en un evento
individual de parámetro finito, y descompone RH en enteros por paso primo. Donde
muere: cada entero por paso es una positividad semilocal sin razón local que la
fuerce. En cuerpos de funciones, lo que hace positivo cada paso no es un cómputo
paso a paso sino UNA razón local-geométrica válida en todos los pasos a la vez — la
desigualdad de Castelnuovo (índice de Hodge en C×C), de la que Weil dedujo RH para
curvas [Wei48]. El flujo de la filtración de Euler identifica el agujero: **falta el
análogo de "la curvatura es positiva en cada carta" — un teorema local que anule
cada sf_p por la misma razón.** No es promediar lo que falta (el flujo no promedia);
es la razón local. Esto alimenta el axioma L5 de §4.

---

## 4. (iii) La especificación del lector de inercia

### 4.1. Los axiomas

**Definición 4.1 (lector de inercia).** Un *lector de inercia* para ζ es un
invariante I con:

- **(L1) Cuantización.** I toma valores en ℤ (o un grupo discreto): no es
  promediable; toda deformación continua de los datos lo deja fijo o lo cambia en
  un salto entero detectable.
- **(L2) Autonomía del valor.** I es computable desde los datos aritméticos
  incondicionales — primos, polo, factor gamma — SIN las posiciones de los ceros
  (como funcional de los bloques aritméticos de una fórmula explícita, o de un
  objeto construido funtorialmente de Spec ℤ).
- **(L3) Detección de inercia.** I = 0 ⟺ m = 0; mejor aún, I = 2m = κ(Q) (P35).
  I lee la signatura, no la traza.
- **(L4) Estabilidad bajo el cómputo.** I es estable bajo las deformaciones que el
  cómputo involucra — truncamiento de primos (filtración de Euler), de rango (N
  finito), límites de ventana — SIN una uniformidad RH-equivalente (sin MW-6 como
  peaje).
- **(L5) Localización.** I satisface un teorema de índice: I = Σ contribuciones
  locales computables, tipo Atiyah–Singer (índice analítico = topológico) o tipo
  Castelnuovo (positividad local ⟹ anulación global por la misma razón en cada
  lugar). Es el axioma que §3.5 mostró faltante en el flujo de Euler.
- **(L6) Finitud a priori.** I factoriza por un objeto de dimensión finita, acotada
  por datos aritméticos (NO por posiciones de ceros), con trazas aritméticamente
  computables sobre ese objeto.

L1–L5 son la lista del encargo, refinada (L2 fija "computable"; L4 nombra el peaje
prohibido; L5 admite la variante Castelnuovo además de la AS). L6 es la adición de
este documento, y §§4.2–4.4 muestran que es el axioma decisivo: sin él, L2+L3+L4
son inconsistentes en la clase donde el programa trabajó; con él, consistentes por
un mecanismo elemental.

### 4.2. La tensión (L2)+(L3): formulación del teorema de imposibilidad

El Doc 108 probó, para Q₂: valor autónomo, inercia no-autónoma (la partición
off×off / off×on requiere posiciones; P43 §4). ¿Accidente de Q₂ o teorema de
imposibilidad? Fijemos la clase honestamente.

**Definición 4.2 (clase ℱ de funcionales cuadráticos aritméticos).** ℱ consta de los
invariantes de la forma I = neg.ind(Q|_{V′}), donde:

(i) Q es una forma hermitiana sobre un espacio de funciones de prueba 𝒱 con una
identidad de tipo fórmula explícita: lado espectral = suma sobre (tuplas de) ceros
de evaluaciones de la transformada de Mellin de los tests, lado aritmético = suma
finita de bloques computables desde primos/polo/gamma (las realizaciones del
programa: la forma de Weil Q de una variable [Doc 91], W₂ y Q₂ [Doc 107], los W_k
[Doc 107 §6.5], las formas semilocales QW_λ [Doc 99]);

(ii) V′ ⊆ 𝒱 es **test-accesible**: especificado sin posiciones de ceros (por
soportes, ventanas de frecuencia, normas — Doc 108, Def. 1.2).

**Teorema 4.3 (imposibilidad en ℱ).** Ningún I ∈ ℱ satisface simultáneamente (L2),
(L3) y (L4). Más precisamente, vale la dicotomía de resolución:

(a) *Régimen sub-resolución.* Si V′ tiene resolución acotada (tests de soporte fijo
a, ventanas de altura T → ∞), entonces I(V′) = 0 **incondicionalmente** para T ≥
T₀(a) — en ambos mundos (Doc 108, Teorema 3.3: AA ∼ c(log T)² domina todos los
bloques, la forma es definida positiva sobre esos tests). Un I sub-resolución viola
(L3): no detecta m.

(b) *Régimen de resolución.* Si V′ resuelve ceros individuales (ancho de banda
≲ 1/log T, i.e. soporte a ≳ log T), entonces I es **binario**: 0 en toda ventana
bajo RH, y ≍ m·n_W ≍ m·log T sin cota sobre ventanas bajo ¬RH, por la contaminación
off×on (Doc 108, Prop. 2.3 + Lema 2.4 + Prop. 2.5; en una variable: Doc 107
Prop. 6.1 y Doc 96 Teorema 8.1 — el índice global es ∞ bajo ¬RH y solo el bloque
relativo es finito). Entonces: o bien I se define como índice por ventana — y
cualquier cota uniforme finita sobre I es lógicamente equivalente a RH (Prop. 2.5
Doc 108), violando (L4) (la estabilidad uniforme requerida ES RH) — o bien I se
define como el bloque relativo off×off (finito, = 8m² para Q₂) — y entonces la
compresión que lo define usa las posiciones de los ceros, violando (L2): el bloque
relativo no es test-accesible (Doc 108 §2.4, GAP estructural declarado allí).

(c) *No hay tercer régimen:* la evaluación de cualquier I ∈ ℱ con (L3) en el régimen
(b) requiere localizar el déficit aritmético Π con precisión relativa o(1/log T)
uniforme en ventanas, lo que implica RH (argumento de los dos mundos: Doc 108,
Teorema 3.4 y Teorema 4.3).

**Estatus de la prueba — declarado con exactitud.** (a) y (c) son teoremas del
Doc 108 (3.3, 3.4, 4.3) para las formas del programa citadas en 4.2(i); la
extensión a los W_k es mecánica (Doc 108, Prop. 7.3), pero NO está escrita para una
clase axiomática arbitraria: en la generalidad literal de 4.2 el enunciado es
**teorema para las realizaciones del programa + esquema para la clase** (los
ingredientes — mar on×on positivo, contaminación off×on por órbitas libres,
jerarquía AA ≫ resto en sub-resolución — dependen solo de la estructura "fórmula
explícita + involución ρ ↦ 1−ρ̄", pero no fabricamos el teorema general). (b)
hereda el caveat del Doc 108: la realizabilidad sobre la clase de prueba (Lema 2.4
allí) está probada en el juguete bajo Hipótesis D. GAP declarado: clase axiomática
general y m general sin Hipótesis D.

**Corolario 4.4 (lectura).** En la categoría donde el programa pasó tres fases
(formas cuadráticas con lado aritmético y compresiones test-accesibles) el muro es
total: la inercia de CUALQUIER funcional cuadrático aritmético es no-autónoma o
no-detectante o RH-de-peaje. El lector de inercia, si existe, es de otra categoría.
La fórmula del Doc 108 §7.4 queda promovida a principio de clase, con el estatus
declarado arriba.

### 4.3. El contraejemplo abstracto: rango finito

¿Refuta algo la especificación? Sí — y el contraejemplo es elemental, lo cual es
exactamente la pista.

**Proposición 4.5 (en rango finito, la inercia ES autónoma desde el valor).** Sea Q
una forma hermitiana sobre un espacio de dimensión finita n, con n conocido a
priori. Entonces la inercia (p, q) de Q está determinada por los n valores
t_j = tr(Q^j), j = 1, …, n. En particular: si las trazas de potencias son
computables desde datos aritméticos, la signatura — el dato individual, la inercia —
es computable desde datos aritméticos, mediante un procedimiento entero, estable y
local en los t_j.

*Demostración.* Las identidades de Newton recuperan los coeficientes del polinomio
característico de Q a partir de t_1, …, t_n; los autovalores son reales (Q
hermitiana); el número de raíces negativas de un polinomio real con raíces reales se
lee de los signos de los coeficientes (regla de los signos de Descartes, exacta en
el caso de raíces todas reales) o, equivalentemente, la signatura se lee de la forma
de Hankel de las sumas de potencias (teorema de Jacobi–Frobenius; [Gan59, Vol. 2,
Cap. X]). Todos los pasos son algebraicos en los t_j. ∎

La Proposición 4.5 no contradice el Teorema 4.3: las formas de ℱ tienen rango
infinito (o rango finito relativo definido por posiciones de ceros — justamente lo
no-autónomo). El contraste aislado:

> **Computar una traza es promediar; computar finitas trazas de un objeto de rango
> finito conocido es individuar.** La frontera valor/inercia no es la frontera
> traza/signatura: es la frontera rango-infinito/rango-finito-a-priori. En dimensión
> finita el promedio determina al individuo porque hay finitos individuos y finitos
> promedios independientes.

**Corolario 4.6 (consistencia condicionada de la especificación).** (L1)–(L5) más
(L6) son consistentes: el modelo abstracto de la Prop. 4.5 los satisface todos
(con L5 trivializado por la dimensión finita). (L1)–(L5) sin (L6), dentro de ℱ, son
inconsistentes (Teorema 4.3). Por tanto el contenido completo de la búsqueda del
lector de inercia se reduce a:

> **(L6) como teorema faltante: una FINITUD.** Existe un objeto de dimensión finita
> acotada a priori por datos aritméticos (no por ceros), cuyas trazas son
> aritméticamente computables (una fórmula de Lefschetz), y cuya signatura/inercia
> equivale a 2m.

Esto es exactamente lo que la cohomología ℓ-ádica provee en cuerpos de funciones:
dim H¹ = 2g — computable del dato geométrico SIN conocer los ceros — y
tr(Frob^n | H¹) = conteo de puntos (Lefschetz; [Wei48], [Del74]): finitas trazas
aritméticas de un objeto de rango finito a priori. La Prop. 4.5 es la razón
algebraica por la que, con eso en la mano, los ceros individuales (autovalores de
Frobenius) quedan determinados por promedios (conteos de puntos): **en cuerpos de
funciones el cuantificador maestro se cruza por finitud, no por mejor estimación.**
El paso restante (|α_i| = q^{1/2}) requirió además una positividad (Castelnuovo
para Weil; Rankin para Deligne) — L3+L5 en nuestra lista. Sin la finitud, ni
siquiera se plantea.

### 4.4. Refinamiento final de la tensión (2)+(3)

Respuesta a la pregunta central: (L1)–(L5) NO es internamente consistente en la
clase donde el programa puede instanciarla hoy (Teorema 4.3), y SÍ es consistente
en abstracto — el contraejemplo es el rango finito (Prop. 4.5). El teorema de
imposibilidad no dice "no hay lector de inercia"; dice: **el lector de inercia no
es una forma cuadrática comprimida — es un teorema de finitud con fórmula de
trazas.** La categoría correcta no es (formas, compresiones, índices negativos)
sino (objeto coherente de rango finito, Frobenius, Lefschetz, positividad de
Hodge). El muro, visto desde aquí, tiene nombre clásico: la ausencia de una
cohomología de Weil para Spec ℤ.

---

## 5. (iv) K-teoría y el sitio: inventario honesto contra la especificación

Sin re-derivar MW-5 (NO-GO-LIST; Phase 27): la factorización local-global del lado
de ceros requiere (1) una cohomología H¹(Spec ℤ, F), (2) un Frobenius por lugar,
(3) una forma de intersección positiva. Aquí solo medimos el programa de
Connes–Consani contra L1–L6.

**5.1. Lo que tienen** (los ítems con asterisco fueron verificados contra fuente en
Docs 99/100; el resto se cita por sus datos publicados):

- El **sitio aritmético** (C.R.A.S. 352, 2014; Adv. Math. 291, 2016): el espacio de
  puntos sobre ℝ₊^max recupera ℚ^×\𝔸_ℚ/ẑ^× con su flujo de escala — el "Frobenius"
  es un flujo a UN parámetro real, no un endomorfismo discreto.
- El **sitio de escala** y su Riemann–Roch tropical (C.R.A.S. 354, 2016; Selecta 23,
  2017): divisores, grado y RR sobre las curvas tropicales C_p = ℝ₊^*/p^ℤ; la
  estrategia declarada es replicar la prueba de Weil/Mattuck–Tate–Grothendieck sobre
  el cuadrado del sitio (*The Riemann–Roch strategy*, Springer 2019) [datos
  editoriales NO VERIFICADOS en detalle].
- (*) La **positividad arquimediana y semilocal**: Selecta 27 (2021,
  arXiv:2006.13771); J. Number Theory 2021 (arXiv:2008.10974); CCM, Ann. Funct.
  Anal. 2024 (arXiv:2310.18423) — verificado en Doc 100.
- (*) Los **triples espectrales zeta** (CCM-ZST, arXiv:2511.22755) y la rigidez CF
  (Connes–van Suijlekom, CMP 406:312, 2025) — verificado en Doc 99.

**5.2. La medición contra L1–L6.**

| axioma | estado en el programa CC | comentario |
|---|---|---|
| L1 (entero) | ✓ en el RR tropical (grados, dimensiones) | los invariantes del sitio son enteros/cuantizados |
| L2 (valor autónomo) | ✓ | toda la construcción es funtorial desde los datos aritméticos; ningún input de posiciones de ceros |
| L3 (detecta inercia) | ✗ | ningún invariante del sitio se ha conectado con m ni con κ(Q); la positividad probada (2021–2024) es por ventana semilocal, no una signatura global |
| L4 (estable sin peaje RH) | ✗ (es MW-6) | el paso semilocal → global es lim μ_λ ≥ 0 = RH; Doc 100 lo midió como Obstáculo O_SL |
| L5 (localización) | parcial | el lado geométrico de la fórmula explícita ES aditivo por lugares (incondicional — Doc 100 §5); falta la razón local de positividad por lugar |
| **L6 (finitud + trazas)** | **✗ — el agujero exacto** | no hay H¹ de dimensión finita con fórmula de Lefschetz: el RR tropical produce característica de Euler (un VALOR: diferencia de dimensiones, K-teoría), no una signatura sobre un espacio finito con Frobenius; el "Frobenius" es un flujo continuo, sin estructura entera de pesos |

La fila L6 es la respuesta a la pregunta del encargo ("¿qué les falta exactamente
para que su H¹ cuente ceros individualmente?"): **les falta el teorema de finitud
con fórmula de trazas — el análogo del par (finitud de la cohomología, Lefschetz) de
Grothendieck — y, encima de él, la positividad (L3/L5) — el análogo del índice de
Hodge.** En char p, ese segundo piso es la parte aún abierta de las conjeturas
estándar [Gro69], [Ser60]; Deligne la esquivó con el argumento de Rankin (cuadrar y
ganar medio peso por iteración, [Del74]) — que funciona porque las dimensiones son
finitas y los pesos se multiplican en los tensores.

**Observación 5.3 (la Forma B fue el truco de Deligne sin finitud).** La
amplificación tensorial del programa — κ(ψ^{⊗k}) = ½(4m)^k (Doc 106; ledger L3 de
P43) — es estructuralmente el squaring de Rankin–Deligne: tensar para amplificar el
defecto hasta hacerlo visible contra el término principal. Murió (Doc 108, Prop.
7.3) porque la masa de comparación (el mar on×on, n_W^k) crece al mismo ritmo que
la señal: en rango infinito, amplificar el numerador amplifica el denominador. En
Deligne el denominador está CLAVADO por la finitud (dim H^i fija, independiente del
twist): la amplificación gana porque itera contra una cota fija. Diagnóstico:
**Forma B = método de Deligne − L6** — la identificación del único ingrediente cuya
ausencia invirtió el resultado. El lector de inercia que CC buscan y el que la
Forma B necesitaba son el mismo objeto, y el axioma que ambos no satisfacen es el
mismo (L6).

---

## 6. (v) Todo por el cuantificador maestro

Aplicamos el Principio maestro (P43, Principle 3.1) a cada candidato. Columnas:
objeto controlado incondicionalmente / refinamiento equivalente a RH / dónde está la
inversión.

| candidato | controlado (promedio/genérico/interior) | RH-equivalente (individual/uniforme/frontera) | la inversión |
|---|---|---|---|
| enrollamiento N_off(R) | ∫_σ N_off(σ,T)dσ (Littlewood → densidad); momentos de S (Selberg); cada caja FIJA por cómputo (Turing) | N_off(R) = 0 para TODA caja | media en σ/t → caja individual; conjunción Π₁ sin razón uniforme (Lema 2.4, Obs. 2.5) |
| paridad / mod k | paridad de cajas simétricas (≡ 0, ambos mundos); paridad de N(T) (signo de Z) | paridad de N_off = inercia mod 2: partición on/off | el mod 2 forzado por simetría es constante = sin información; el informativo exige la partición (Obs. 2.7) |
| flujo espectral de Euler | sf de cada aproximante CF = 0 (rigidez, todo paso finito); μ_λ por paso, en principio computable | sf_p = 0 para TODO p + límite (gap uniforme) | positividad por paso sin razón local; MW-6 en el límite interno (Prop. 3.4) |
| índice de formas cuadráticas (ℱ) | el VALOR de Q (autónomo); índices sub-resolución (= 0 incondicional) | la INERCIA por ventana (binaria: 0 vs ≍ m log T) | Teorema 4.3: (L2)+(L3)+(L4) inconsistentes en ℱ |
| K-teoría / sitio CC | característica de Euler tropical, positividad semilocal por ventana | signatura global de un H¹ finito con Lefschetz | L6 ausente: sin finitud, el entero disponible es un valor, no una inercia (§5.2) |

Dictamen: **ningún candidato esquiva el cuantificador, y el modo de caer es
informativo.** Los candidatos topológicos no caen por promediar — no promedian —
sino por la EVALUACIÓN: el entero existe y es decidible evento por evento, pero la
única maquinaria incondicional de evaluación es promediada, y la alternativa es la
conjunción infinita sin razón local. Esto refina a P43: para invariantes
cuantizados el muro no es "promedian"; es **"no hay localización (L5) ni finitud
(L6) que evalúe el entero de una vez para todas las instancias"**. La inversión del
cuantificador reaparece como el paso de "cada entero, por cómputo" a "todos, por
una razón" — la forma Π₁ del muro. En la única instancia histórica ganada, la razón
fue cohomológica: finitud + Lefschetz + positividad local.

---

## 7. (vi) VEREDICTO

### 7.1. Especificación final del lector de inercia

Un invariante I que cruce el muro debe satisfacer **L1–L6** (§4.1), con la
estructura lógica probada en este documento:

- (L1–L4) sin L6 es **inconsistente** en la clase ℱ (Teorema 4.3; estatus: teorema
  para las realizaciones del programa, esquema para la clase axiomática, caveats
  del juguete declarados).
- (L1–L6) es **consistente** (Prop. 4.5: en rango finito a priori, finitas trazas
  determinan la inercia — Newton / Jacobi–Frobenius).
- La especificación operativa se comprime así en **L6 + Lefschetz + positividad
  local (L3/L5)** — una cohomología de Weil para Spec ℤ: objeto de rango finito
  acotado aritméticamente, fórmula de trazas aritmética, positividad local que
  anule el flujo por paso. Los demás axiomas vienen gratis (Prop. 4.5 da L1, L2,
  L4 desde L6 + trazas).

### 7.2. Estado del teorema de imposibilidad

**Probado en su clase, con frontera exacta.** La inercia de cualquier funcional
cuadrático aritmético del tipo del programa es no-autónoma (Teorema 4.3, vía la
dicotomía sub-resolución/resolución del Doc 108); la refutación abstracta de la
imposibilidad general es elemental (rango finito, Prop. 4.5); la combinación
localiza el muro en la finitud, no en la cuadraticidad ni en la positividad. La
pista del contraejemplo: el lector no se busca mejorando estimaciones en rango
infinito — se busca probando que el problema VIVE en rango finito (una
coherencia/finitud à la Grothendieck sobre el sitio correcto). GAP ABIERTO (el de
siempre, con coordenadas nuevas): ese teorema de finitud no existe; es MW-5, ítem
(1), promovido de "ingrediente" a "el único ingrediente".

### 7.3. Enunciado falsable más prometedor

Dos niveles, del más cercano al más estructural:

1. **(Falsable ya, infraestructura publicada.) Conjetura 100.A efectiva, leída como
   flujo espectral:** sf{A_λ : λ ∈ (1, √3]} = 0, i.e. μ_λ ≥ 0 hasta incluir el
   primo 2 — en versión cuantitativa, con gap explícito μ_λ ≥ c₂ > 0. Es el primer
   entero no trivial de la filtración de Euler (Teorema 3.2 + Doc 100 §6); su
   falsación refutaría la positividad de Weil semilocal en su primer paso; su
   prueba sería el primer teorema de positividad por paso — el germen de la razón
   local que L5 pide. Cada paso adicional (sf_p = 0 con gap c_p subexponencial) es
   un teorema parcial honesto; la uniformidad en p es MW-6, declarada como muro.

2. **(Diana estructural, D108 §8.2, reformulada como enrollamiento.) Cota lineal
   del enrollamiento por ventana:** κ_W ≤ C·n_W con C absoluto, que implicaría
   m ≤ C/2 — una cota ABSOLUTA del número de cuádruplos off-críticos, más débil que
   RH y más fuerte que toda densidad conocida. Está detrás del mismo muro de
   segundo orden (D108 §8.1), pero es el único enunciado intermedio identificado
   que un lector de inercia parcial (sin L6 completo) podría alcanzar.

### 7.4. Veredicto

**VEREDICTO: PARCIAL.**

- **SIN CANDIDATO construido:** ninguno de los invariantes que cuentan uno a uno
  (enrollamiento, paridad, flujo espectral, índices de formas, K-teoría del sitio)
  lee hoy la inercia de ζ; el documento localiza el punto de caída de cada uno
  (Lema 2.4, Prop. 2.6/Obs. 2.7, Prop. 3.4, Teorema 4.3, §5.2).
- **CON especificación cerrada y no vacía:** L1–L6, consistente (Prop. 4.5),
  inconsistente sin L6 en la clase del programa (Teorema 4.3), equivalente en la
  práctica a una cohomología de Weil para Spec ℤ; con dos identificaciones nuevas:
  la Forma B fue el método de Deligne menos la finitud (Obs. 5.3), y el flujo
  espectral de la filtración de Euler reformula RH exactamente (Teorema 3.2) — el
  evento ¬RH es individual y de parámetro finito; lo que falta no es individualidad
  sino una razón local válida en todos los pasos.
- El residuo conceptual para la Phase 37: **un entero no se promedia: se lee — pero
  leerlo uniformemente requiere finitud (L6) o localización (L5). La física llama a
  eso "carga topológica protegida": la protección, no la carga, es lo que ζ no
  tiene todavía.**

---

## Referencias

**Internas (backward-only):** P43 (§3 Principio maestro, §4 valor/inercia, §6
frontera); P42 (§6 Lema Faltante 6.1); P41 (no-go interior/frontera); P35
(κ(Q) = 2m); Doc 108 (Teoremas 3.3, 3.4, 4.3; Prop. 2.3, 2.5; Lema 2.4; §§7.4,
8.1–8.2); Doc 107 (W₂, Teorema 2.4, Prop. 6.1, §6.5); Doc 106 (identidad tensorial,
Prop. 3.6); Doc 100 (Lema 2.0, lema de agotamiento §3, μ_∞ = 0 §4, Obstáculo O_SL
§5, Conjetura 100.A §6); Doc 99 (CCM-ZST §2, rigidez CF §§3–4, E5 κ_λ(N)); Doc 96
(Teorema 8.1); Doc 91 (forma de Weil, Prop. 4.5); NO-GO-LIST (MW-1…MW-7).

**Literatura (verificable):**
- [APS76] M. F. Atiyah, V. K. Patodi, I. M. Singer, *Spectral asymmetry and
  Riemannian geometry III*, Math. Proc. Cambridge Philos. Soc. 79 (1976), 71–99
  (flujo espectral).
- [AS63] M. F. Atiyah, I. M. Singer, *The index of elliptic operators on compact
  manifolds*, Bull. Amer. Math. Soc. 69 (1963), 422–433.
- [Del74] P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974),
  273–307 (argumento de Rankin/squaring).
- [Gan59] F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Cap. X
  (signatura vía formas de Hankel de sumas de Newton; Jacobi–Frobenius).
- [Gro69] A. Grothendieck, *Standard conjectures on algebraic cycles*, en Algebraic
  Geometry (Bombay Colloquium 1968), Oxford Univ. Press, 1969, 193–199.
- [IK04] H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53,
  2004 (Thm. 5.8: N(T); Thm. 5.12 y Cap. 10: lema de Littlewood y densidad).
- [Ing40] A. E. Ingham, *On the estimation of N(σ,T)*, Quart. J. Math. Oxford 11
  (1940), 291–292. (Littlewood 1924, S(T) bajo RH, se cita vía [Tit86, Thm. 14.13].)
- [Phi96] J. Phillips, *Self-adjoint Fredholm operators and spectral flow*, Canad.
  Math. Bull. 39 (1996), 460–467.
- [PT21] D. J. Platt, T. S. Trudgian, *The Riemann hypothesis is true up to
  3·10¹²*, Bull. London Math. Soc. 53 (2021), 792–797.
- [RS95] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull.
  London Math. Soc. 27 (1995), 1–33.
- [Sel46] A. Selberg, *Contributions to the theory of the Riemann zeta-function*,
  Arch. Math. Naturvid. 48 (1946), 89–155 (momentos de S(T)).
- [Ser60] J.-P. Serre, *Analogues kählériens de certaines conjectures de Weil*,
  Ann. of Math. 71 (1960), 392–394.
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed.
  (rev. D. R. Heath-Brown), Oxford Univ. Press, 1986 (§2.12; Thm. 9.4: S(T) =
  O(log T); §9.9: lema de Littlewood y S₁(T); Thm. 14.13).
- [Tur53] A. M. Turing, *Some calculations of the Riemann zeta-function*, Proc.
  London Math. Soc. (3) 3 (1953), 99–117.
- [Wei48] A. Weil, *Sur les courbes algébriques et les variétés qui s'en
  déduisent*, Hermann, Paris, 1948 (RH para curvas vía Castelnuovo/índice de Hodge).
- Connes–Consani: *The Arithmetic Site*, C. R. Acad. Sci. Paris 352 (2014),
  971–975; *Geometry of the Arithmetic Site*, Adv. Math. 291 (2016), 274–329;
  *The Scaling Site*, C. R. Acad. Sci. Paris 354 (2016), 1–6; *Geometry of the
  Scaling Site*, Selecta Math. (N.S.) 23 (2017), 1803–1850; *The Riemann–Roch
  Strategy: Complex Lift of the Scaling Site*, en Advances in Noncommutative
  Geometry, Springer, 2019 [datos editoriales NO VERIFICADOS en detalle];
  *Weil positivity and trace formula: the archimedean place*, Selecta Math. 27
  (2021) (arXiv:2006.13771, verificado en Doc 100); arXiv:2008.10974 (J. Number
  Theory 2021, verificado en Doc 100).
- Connes–Consani–Moscovici: Ann. Funct. Anal. 2024 (arXiv:2310.18423, verificado en
  Doc 100); *Zeta Spectral Triples* (arXiv:2511.22755, verificado en Doc 99).
- A. Connes, W. D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the
  Spectral Action*, Commun. Math. Phys. 406:312 (2025) (arXiv:2511.23257,
  verificado en Doc 99).
- H. Yoshida, positividad arquimediana de la forma de Weil (1992), citado vía
  Doc 100 §4 [identificación bibliográfica exacta en Doc 100].

*Fin del Doc 110.*
