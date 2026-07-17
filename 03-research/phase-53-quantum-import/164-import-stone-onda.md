# Doc 164 — Importación del teorema de Stone: ¿una evolución unitaria estructural cuyo generador tenga espectro {γ}, con unitariedad RH-libre? ¿O la unitariedad es la métrica de Weil disfrazada?

**Programa:** Hipótesis de Riemann — Phase 53: importación cuántica.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** CONSTRUCTIVO con la GUARDIA DE UNITARIEDAD al frente. Mandato: importar la
maquinaria de mecánica cuántica matemática (teorema de Stone, autoadjunción esencial, dualidad de
Fourier posición-momento) para CONSTRUIR el objeto X del cual primos y ceros son dos
representaciones —por analogía con cómo ψ resolvió la dualidad onda-partícula— o LOCALIZAR con
precisión la obstrucción. La herramienta central a importar es el **teorema de Stone**: en QM la
realidad del espectro (autovalores reales) NO sale de una métrica elegida sino de que la evolución
es UNITARIA (ley de conservación), {U(t)=e^{itH}} grupo ⟺ H autoadjunto ⟺ espec(H)⊂ℝ. Apuesta:
si {γ} fuera el espectro del generador de una evolución unitaria cuya unitariedad proviene de una
SIMETRÍA estructural (la ecuación funcional s↔1−s), no de una métrica, entonces RH = "espectro
real" = automático por Stone, y la métrica donde ζ reentra quedaría reemplazada por una
conservación estructural.

**Contrato de etiquetado (regla absoluta).** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad aquí, prueba completa; externos con
referencia verificable. **[CONSTRUCCIÓN]** = objeto definido con precisión. **[PUENTE]** = conexión
con estatus honesto. **[GAP]/[GAP de literatura]** = declarado; el de literatura NO se usa como
premisa de ningún teorema. **[DESEO]** = declarado. Jamás se fabrica una prueba de RH ni una falsa
victoria (DESENLACE A). PERMITIDO (y esperable) terminar en B/C/D. **NADA de numéricos/Python.**
**Español.** Honestidad absoluta. Una falsa victoria es peor que un fracaso.

**Prerrequisitos leídos en fuente esta sesión:** Doc 162 (Phase 52: e-invariante aritmético
RH-libre, pero ζ reentra en la *clase fundamental del portador* [C_Φ]=Σ_ρ δ_{γ_ρ}; trifurcación de
D156: (i) Fredholmicidad, (ii) orientación, (iii) escape; Phase 51 tocó (ii), Phase 52 tocó (i)).
Doc 163 (destructor: un secundario = integral de un relleno del primario; "¿qué es el relleno y con
qué se integra?"). B3.1 (template universal de Kreĭn ‖K‖≤1; Connes–Consani: espectro de
ABSORCIÓN sobre el espacio de Sonin, fórmula semilocal). Memoria Phase 26 (κ=2m=neg.ind(H_C) en
Pontryagin (𝒦,Q); RH ⟺ H_C autoadjunto). Memoria Phase 33 (DBN: Λ=inf{t:T_λ(t)=0}; flujo de
calor). Memoria Phase 38/45 (P_n = Meixner–Pollaczek, medida dm_∞=|Γ(1/4+is/2)|²ds; criterio de
momentos). Memoria Phase 49–51 (la métrica canónica porta ζ por partición Bost–Connes; el muro es
la signatura de inercia, RH-libre la homotopía pura pero no la flecha).

---

## 0. Resumen ejecutivo y veredicto adelantado

> **VEREDICTO: DESENLACE B con un fragmento nuevo de D.** La importación de Stone NO da (A): no
> existe una evolución unitaria estructural cuyo generador tenga espectro {γ} y cuya unitariedad sea
> RH-libre. La razón es precisa y constituye el aporte del documento: **la unitariedad ES la métrica
> de Weil disfrazada, pero por un mecanismo que el programa aún no había nombrado con esta nitidez —
> el "teorema de Stone invertido".** En QM uno tiene el espacio de Hilbert (la métrica) *dado a
> priori* por la física (probabilidad = ‖ψ‖²), y de la unitariedad deduce espectro real. En RH la
> dirección está INVERTIDA: no hay métrica dada a priori; lo único dado es la dinámica (el flujo de
> escala / la ecuación funcional) y el dato espectral {γ}. Para que Stone se aplique hay que EXHIBIR
> el espacio de Hilbert respecto del cual U(t) es unitario — y exhibirlo *es* construir el producto
> interno que hace reales los γ, que es exactamente la forma de Weil Q (la métrica que porta ζ,
> Phase 51). **La simetría funcional s↔1−s sí da una involución unitaria RH-libre (Prop. 164.6) —
> pero es una unitariedad en el parámetro EQUIVOCADO: conjuga el espectro (γ↦−γ̄ del lado off-line),
> no lo hace real. La unitariedad estructural disponible (la funcional) no es la que Stone necesita
> (la del flujo de escala), y la que Stone necesita no es estructural.** Ése es el nodo, y es
> *distinto* del de Phase 52: Phase 52 ubicó ζ en la clase fundamental del portador; este documento
> la ubica en **la elección del producto interno que realiza la unitariedad del flujo de escala**, y
> prueba que la única simetría RH-libre a mano (la funcional) actúa en la dirección de conjugación
> (γ↦γ̄), no en la de evolución (γ real). El fragmento de D (nuevo): la **discrepancia de los dos
> grupos de un parámetro** —dilatación (escala, Connes) versus traslación (Fourier/onda)— es ella
> misma una obstrucción nombrable y no es la dualidad de Phase 52.

**Los tres resultados con etiqueta (adelantados):**

1. **[PROPOSICIÓN 164.4 — el teorema de Stone invertido].** En QM la métrica (‖ψ‖²) es input físico
   y Stone deduce espectro⊂ℝ. En el problema aritmético la métrica NO es input; el dato es la
   dinámica de escala θ_λ y el espectro candidato {γ}. Exhibir el espacio de Hilbert que vuelve U(t)
   unitario es lógicamente equivalente a exhibir el producto interno que vuelve {γ} reales — y ese
   producto interno, sobre el espacio de clases de adeles, es la forma de Weil Q, que porta ζ. La
   unitariedad RH-libre del flujo de escala implicaría RH directamente sin contenido nuevo: es la
   métrica disfrazada. (Probado como implicación lógica; usa el diccionario κ=neg.ind(Q) de Phase 26.)

2. **[PROPOSICIÓN 164.6 — la involución funcional es unitaria RH-libre, pero conjuga, no evoluciona].**
   La ecuación funcional ξ(s)=ξ(1−s) induce una involución J (s↦1−s) que es unitaria respecto del
   producto interno *natural sin ζ* (el de L² de la recta crítica) y RH-libre. PERO J es una
   conjugación de carga (γ↦γ̄ sobre el divisor off-line, intercambia ρ↔1−ρ̄), no el generador de la
   evolución que haría reales los γ. Stone necesita un grupo U(t)=e^{itH} con H el *generador de
   escala*; la simetría que tenemos gratis es la *reflexión*, que vive en el grupo equivocado
   (ℤ/2 ⊄ ℝ-flujo). La unitariedad estructural disponible no es la que Stone consume. (Probado: J²=1,
   J unitaria sin métrica-ζ; la prueba de que no es e^{itH} para el H de escala es por incompatibilidad
   de espectros, §3.)

3. **[PROPOSICIÓN 164.8 — autoadjunción por la forma falla porque el "potencial" es el contaje de
   ceros].** Para el candidato natural a operador autoadjunto-por-su-forma con espectro {γ} (un
   −d²/dx² + V tipo Berry–Keating regularizado, o el H_C de Connes), la condición "V real / forma
   simétrica manifiesta" no se cumple *por la forma*: las condiciones de borde / el término que fija
   {γ} exacto codifican ζ (autoadjunción esencial de xp falla — Berry–Keating; el defecto de
   índice de von Neumann (n₊,n₋) que hay que igualar es el dato que enumera los ceros). No hay forma
   manifiestamente autoadjunta RH-libre. Reproduce y *localiza* el muro de Berry–Keating: el punto de
   parada es la igualdad de los índices de deficiencia, y ése es ζ. (Probado el caso xp / esencial
   autoadjunción; el caso H_C reduce a Phase 26.)

**Dónde reentra ζ (una frase):** en **la elección del espacio de Hilbert que hace unitario al flujo
de escala** —que es la forma de Weil Q (Phase 51, métrica con partición ζ)— porque la única simetría
unitaria RH-libre disponible (la ecuación funcional) actúa como conjugación γ↦γ̄, no como la
evolución γ∈ℝ que Stone necesita. **Teorema de Stone invertido:** en QM la métrica es dada y el
espectro real se deduce; aquí el espectro real ES la métrica por deducir.

---

## 1. El diccionario QM↔RH, preciso

Fijo el diccionario con el rigor que exige el mandato, y marco en cada fila si el objeto del lado
derecho es RH-libre o porta ζ. Esto es lo que después auditará la guardia.

| QM (conocido, simple) | RH (el objeto X buscado) | Estatus |
|---|---|---|
| Espacio de Hilbert ℋ, ‖ψ‖² = probabilidad | ¿𝒦 = L²(C_ℚ) (clases de adeles, Connes) ó L²(ℝ,dm_∞), dm_∞=\|Γ(1/4+is/2)\|²ds (CCM)? | **el producto interno es el nodo** |
| Posición x | Lado primos: distribución sobre {log p} (escala logarítmica) | dato "conocido" |
| Momento p | Lado ceros: distribución sobre {γ_ρ} | dato a determinar |
| Transformada de Fourier ⟨x\|p⟩=e^{ixp} | **Fórmula explícita de Weil** Σ_ρ ĥ(γ_ρ) = ĥ(±½i) − Σ_p Σ_k (log p)p^{−k/2}h(k log p)+arq. | el "cambio de base" |
| Función de onda ψ (objeto previo a las dos bases) | **El objeto X** = un vector/estado en 𝒦 cuyas dos representaciones de Fourier son primos y ceros | el grial buscado |
| Hamiltoniano H, generador de e^{itH} | Generador de la dilatación/escala (Connes H_C; Berry–Keating xp) | autoadjunto ⟺ RH |
| Evolución unitaria U(t)=e^{itH} | Flujo de escala θ_λ: ξ(v)↦ξ(λ^{−1}v), λ=e^t | **unitariedad = el test** |
| "Energía" conservada por U(t) | la cantidad cuya conservación da unitariedad: aquí, la *norma de Weil* | **= ζ (Phase 51)** |
| Espectro(H) ⊂ ℝ (Stone) | {γ_ρ} ⊂ ℝ, i.e. Re ρ = ½ | **= RH** |
| Realidad del espectro = unitariedad (no métrica) | RH = unitariedad estructural (la apuesta del mandato) | **a decidir aquí** |

**Comentario sobre "ψ = el objeto X".** La analogía guía es correcta y profunda: la dualidad
onda-partícula no se resolvió eligiendo bando, sino exhibiendo ψ con sus dos representaciones de
Fourier (posición/momento) como bases de un mismo espacio. El análogo aritmético existe y el programa
lo tiene parcialmente: el **flujo de escala de Connes sobre L²(C_ℚ)** es exactamente una dualidad de
Fourier (Mellin) entre escala (∼ primos, vía la acción adélica) y frecuencia (∼ ceros, vía el espectro
del generador de escala). La fórmula explícita ES el cambio de base de Fourier–Mellin. Hasta aquí la
analogía es *literal*, no metafórica. El problema —que aíslo en §2–§3— no es la falta del objeto X
(existe: es el espacio de clases de adeles con su flujo de escala), sino **cuál es la "energía"
conservada que da la unitariedad**, porque ahí es donde el diccionario se rompe.

**[PUENTE 164-A].** El diccionario es honesto y casi todo RH-libre EXCEPTO dos casillas, ambas la
misma: "energía conservada" y "producto interno de ℋ". En QM esas dos casillas vienen gratis de la
física (probabilidad). En RH son justo lo que falta, y la guardia (§2) muestra que son ζ.

---

## 2. La importación de Stone y la evolución unitaria candidata

### 2.1 El teorema de Stone, exacto (Stone 1932; Reed–Simon I, Thm VIII.7–VIII.8)

**[Recordatorio — teorema de Stone].** Sea ℋ un espacio de Hilbert. Hay una biyección entre:
(a) grupos de un parámetro fuertemente continuos de operadores unitarios {U(t)}_{t∈ℝ}, U(t+s)=U(t)U(s),
U(0)=1; y (b) operadores autoadjuntos H (en general no acotados, densamente definidos), vía
U(t)=e^{itH}, donde H = −i d/dt U(t)|_{t=0} sobre su dominio natural. Corolario inmediato:
**H autoadjunto ⟹ espec(H) ⊂ ℝ.** Ref.: M.H. Stone, "On one-parameter unitary groups in Hilbert
space", *Ann. of Math.* 33 (1932) 643–648; M. Reed, B. Simon, *Methods of Modern Mathematical
Physics I: Functional Analysis*, Academic Press 1980, Thm VIII.7 (Stone) y VIII.8.

**El punto físico que el mandato quiere importar (correcto).** En QM la realidad del espectro NO se
verifica eligiendo una métrica: sale de que U(t) preserva ‖ψ‖² (conservación de probabilidad =
unitariedad), y ‖ψ‖² es input físico. La realidad del espectro es consecuencia de una **ley de
conservación**, no de un producto interno impuesto a posteriori. Bellísimo. La pregunta es si esto
se puede trasplantar.

### 2.2 [CONSTRUCCIÓN] El grupo de un parámetro candidato: el flujo de escala

Hay UNA elección natural, no varias, y conviene comprometerse con ella para que la guardia mumuerda
algo concreto.

**[CONSTRUCCIÓN — U(t) = flujo de escala].** Sobre ℋ = L²(ℝ₊*, d*λ) (la versión arquimediana, par,
de Connes–Consani; B3.1 §2) ó sobre L²(C_ℚ) (clases de adeles), defino
U(t) ξ(v) = ξ(e^{−t} v), t ∈ ℝ.
Es un grupo de un parámetro (composición de dilataciones). Su generador formal es
H = −i (v d/dv + ½) = −i d/d(log v) − i/2,
es decir, en la coordenada logarítmica u = log v, H = −i d/du − i/2 (un operador de
traslación/momento desplazado). En la representación de Mellin (la transformada de Fourier de este
flujo), el espectro de H es la recta de frecuencias; el dato espectral aritmético {γ_ρ} aparece como
las frecuencias donde ζ(½+iγ)=0, vía la fórmula explícita leída como fórmula de traza del flujo (la
"distribución de Connes"). Esto es exactamente el setup de Connes 1999 y de Berry–Keating (H ∼ xp en
coordenadas adecuadas: u d/du es xp tras x=u).

**La "energía" conservada.** Para que U(t) sea unitario sobre ℋ con su d*λ, necesito que d*λ sea
invariante bajo dilatación — y lo es: d*λ = dλ/λ es la medida de Haar de ℝ₊*. Entonces U(t) es
unitario y H autoadjunto sobre L²(ℝ₊*,d*λ) **trivialmente**, y su espectro es ℝ entero (es el
operador de momento en u=log λ). **Pero su espectro es TODA la recta, no {γ_ρ}.** Aquí está el primer
problema, que anticipa todo: la unitariedad fácil (medida de Haar) da el operador equivocado
(espectro continuo = ℝ, no los ceros). Para obtener {γ_ρ} como espectro hay que *recortar* el espacio
(condiciones de borde, proyección de Sonin, espectro de absorción) — y ahí muere la unitariedad fácil.

### 2.3 [PUENTE 164-B] Tres encarnaciones del mismo flujo, y dónde cada una pone {γ}

El programa ya tiene tres versiones de este flujo; las alineo para no reinventar:

1. **Berry–Keating xp** (Berry–Keating, "H=xp and the Riemann zeros", en *Supersymmetry and Trace
   Formulae*, ed. Lerner et al., Kluwer 1999, pp. 355–367; y Berry–Keating, "The Riemann zeros and
   eigenvalue asymptotics", *SIAM Review* 41 (1999) 236–266). H=xp = ½(xp+px) es simétrico pero **no
   esencialmente autoadjunto** sobre ℝ₊; da la densidad PROMEDIO de ceros (la cuenta de Riemann–von
   Mangoldt N(T)∼(T/2π)log(T/2πe)) vía la regla semiclásica de Weyl, pero NO el espectro exacto. Las
   condiciones de borde / la regularización (Sierra, Connes) que fijarían {γ_ρ} exacto codifican ζ.

2. **Connes 1999** (A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann
   zeta function", *Selecta Math. (N.S.)* 5 (1999) 29–106). El flujo de escala sobre L²(C_ℚ)/(idele
   class group). Los ceros aparecen como espectro de **ABSORCIÓN** (huecos en el espectro continuo del
   flujo, no autovalores de emisión). La fórmula de traza es semilocal y la **positividad de la traza
   de Weil ⟺ RH** es lo que queda abierto.

3. **CCM del programa** (Phase 29–45). Medida dm_∞=|Γ(1/4+is/2)|²ds; polinomios de Meixner–Pollaczek
   P_n^(λ)(s;φ) como autofunciones de un operador tipo QM (un operador de Jacobi / de creación-
   aniquilación en esa medida). Aquí el flujo de escala se representa concretamente y la pregunta de
   autoadjunción se vuelve un problema de momentos (Phase 38: RH ⟺ Δ_n constante).

**Las tres son el MISMO flujo de escala en distintas realizaciones.** Y las tres ponen {γ} no como
espectro de emisión de un operador autoadjunto manifiesto, sino vía un recorte (borde / absorción /
medida) que es donde entra ζ. Esto NO es coincidencia; §3 lo prueba.

---

## 3. EL TEST DE LA UNITARIEDAD (la guardia, AL FRENTE)

Aplico la guardia sin piedad, como exige el mandato. **Unitario = preserva un producto interno.**
Pregunta decisiva: *¿la unitariedad de U(t) se establece SIN elegir el producto interno que carga ζ?*

### 3.1 [PROPOSICIÓN 164.4 — el teorema de Stone invertido]

**Enunciado.** Considérese el flujo de escala U(t) (§2.2) como candidato a tener generador H con
espectro {γ_ρ}. Entonces:

(i) Sobre la medida de Haar d*λ, U(t) es unitario *gratis y RH-libre*, pero espec(H)=ℝ (continuo) —
el operador equivocado: no ve los ceros.

(ii) Para que espec(H)={γ_ρ} (los ceros como autovalores reales/espectro de emisión), hace falta
restringir ℋ a un subespacio ℋ_{γ} (condiciones de borde / proyección). U(t) es unitario sobre ℋ_{γ}
⟺ ℋ_{γ} es U(t)-invariante con el producto interno restringido. **Exhibir ese ℋ_{γ} y certificar la
unitariedad sobre él es lógicamente equivalente a exhibir el producto interno respecto del cual los
{γ_ρ} son reales, que es la forma de Weil Q (Phase 26: RH ⟺ Q≥0 ⟺ H_C autoadjunto), la métrica que
porta ζ (Phase 51).**

(iii) Por tanto: una prueba RH-libre de que U(t) es unitario sobre ℋ_{γ} sería una prueba RH-libre de
RH sin contenido nuevo. **La unitariedad en el espacio correcto ES la métrica de Weil disfrazada.**

**Prueba.**
(i) U(t)ξ(v)=ξ(e^{−t}v); ∫|ξ(e^{−t}v)|² dλ/λ = ∫|ξ(w)|² dw/w (cambio w=e^{−t}v, dw/w=dλ/λ invariante
de Haar) = ‖ξ‖². Luego U(t) unitario, sin usar ζ. H=−i d/du−i/2 (u=log v) es el momento desplazado,
autoadjunto sobre L²(ℝ,du) por Fourier estándar (Reed–Simon I, VIII); su espectro es ℝ. No hay ceros
en ningún lado: este H "ve" sólo la estructura de grupo de ℝ₊*, que es RH-libre y por eso *ciega a
ζ* — exactamente el no-go dinámico N5 de Phase 8 (el flujo solo es aritmético-ciego). ∎(i)

(ii) El espectro de un operador autoadjunto es real *automáticamente*; conversely, dado el conjunto
{γ_ρ}⊂ℂ que queremos como espectro, "los γ_ρ son reales" NO es un teorema sobre H sino el enunciado
RH mismo. La única manera de que Stone *fuerce* γ_ρ∈ℝ es que H sea autoadjunto sobre algún ℋ_{γ}. Pero
H autoadjunto presupone un producto interno ⟨·,·⟩_{ℋ_γ} respecto del cual H=H*. Construir ese
producto interno sobre el espacio de funciones test del flujo de escala, tal que H_C (el generador de
Connes) sea simétrico y los autovectores asociados a {γ_ρ} sean ortonormales con norma positiva, es
*exactamente* construir la forma de Weil Q con Q≥0. Esto es el contenido de Phase 26 (κ=2m=neg.ind(Q);
RH ⟺ Q≥0 sobre el espacio de Pontryagin (𝒦,Q) ⟺ H_C autoadjunto, no meramente Q-simétrico). Y por
Phase 51 (D161) toda métrica canónica sobre el espacio de clases de adeles tiene función de partición
ζ (Bost–Connes): el producto interno que vuelve positiva a Q *es* ζ-portador. ∎(ii)

(iii) Inmediato de (ii): "U(t) unitario sobre ℋ_γ" = "Q≥0" = "H_C autoadjunto" = "espec(H_C)⊂ℝ" =
RH. Sin contenido extra. ∎

**Interpretación (el aporte conceptual).** En QM el orden lógico es:
**[métrica física dada] ⟹ [unitariedad] ⟹ [espectro real (Stone)].**
La métrica (‖ψ‖²) es un AXIOMA de la teoría (regla de Born), no un teorema. Stone convierte
unitariedad en realidad espectral *gratis* porque la métrica ya estaba puesta. En RH el orden está
**INVERTIDO**: no hay métrica axiomática; el dato es el flujo (RH-libre, pero ciego a ζ por (i)) y el
conjunto {γ_ρ}. Lo que en QM es dato (la métrica) es aquí justamente la incógnita, y "espectro real"
no es la conclusión de Stone sino la hipótesis de partida disfrazada. **Stone no ayuda porque
importa la conclusión, no la hipótesis: necesitaríamos importar la regla de Born, y la regla de Born
aritmética es la positividad de Weil = ζ.** Llamo a esto el *teorema de Stone invertido*. Es un modo
de fallo nuevo respecto de Phase 52 (que ubicó ζ en la clase fundamental del portador): aquí ζ está
en *el axioma de métrica que QM tiene gratis y la aritmética debe demostrar*.

### 3.2 ¿Y si la unitariedad viene de una SIMETRÍA en vez de una métrica? — la ecuación funcional

Ésta es la jugada precisa que pide el mandato (punto 2–3): que U(t) sea unitario por una **simetría
estructural RH-libre** (la ecuación funcional s↔1−s) en lugar de una métrica elegida. La examino y la
mato con cuidado, porque es la mejor esperanza de (A).

### 3.3 [PROPOSICIÓN 164.6 — la involución funcional es unitaria y RH-libre, pero está en el grupo equivocado]

**Enunciado.** La ecuación funcional ξ(s)=ξ(1−s) (ξ = la xi completada, entera, simetría exacta sin
hipótesis) induce una involución J: s↦1−s sobre el plano s, equivalentemente sobre el eje crítico
una reflexión. Entonces:

(a) J es **unitaria respecto del producto interno NATURAL sin ζ** (el de L² del eje s con la medida de
Lebesgue, o el de la realización de de Branges donde la funcional es la regla de simetría), y J²=1.
Es RH-libre: la ecuación funcional es un teorema incondicional (Riemann 1859; vía la representación
theta / la simetría de la integral de Mellin de θ). **PASA la guardia: unitariedad sin métrica-ζ.**

(b) PERO J es una **conjugación / reflexión** (un elemento de orden 2, J∈ℤ/2), NO el generador de un
flujo ℝ. Sobre el divisor off-line, J intercambia ρ↔1−ρ; compuesta con la conjugación compleja c
(ρ↦ρ̄), genera el grupo de Klein V=⟨J,c⟩ cuyas órbitas libres son los cuádruplos {ρ,1−ρ,ρ̄,1−ρ̄}
(exactamente el m de Phase 52). La acción de J sobre el espectro candidato {γ} del generador de escala
es **γ↦−γ** (reflexión del eje imaginario), no "γ real". J conmuta con H_C pero NO ES e^{itH_C} para
ningún t (es involución, no flujo; su espectro es {±1}, el de H_C es {γ}).

(c) Conclusión: la simetría unitaria RH-libre que tenemos (J, la funcional) vive en el grupo de
REFLEXIÓN ℤ/2, no en el grupo de EVOLUCIÓN ℝ que Stone consume. Stone necesita unitariedad de
{e^{itH_C}}_{t∈ℝ} (flujo de escala); la funcional da unitariedad de {1,J} (reflexión). **La
unitariedad estructural disponible no es la que Stone necesita.** Y la realidad de {γ} (RH) NO es la
J-invariancia (que es incondicional: J actúa sobre off-line y on-line por igual, no distingue m); es
la autoadjunción de H_C, que J no da.

**Prueba.**
(a) La ecuación funcional es ξ(s)=ξ(1−s), ξ entera, demostrada incondicionalmente (la prueba clásica
vía la transformación modular θ(1/t)=√t θ(t) y la integral de Mellin; Titchmarsh, *The Theory of the
Riemann Zeta-Function*, 2ª ed. Oxford 1986, §2.6). Sobre el eje crítico s=½+iτ, J: τ↦−τ es la
reflexión, manifiestamente unitaria en L²(ℝ,dτ) (es f(τ)↦f(−τ), una isometría) y J²=1. Ningún ζ ni
métrica especial: PASA. ∎(a)

(b) J intercambia el semiplano Re s>½ con Re s<½; sobre un cero off-line ρ=β+iγ con β≠½, Jρ=1−ρ es el
cero conjugado-por-funcional; junto con c: ρ↦ρ̄ se obtiene la órbita de Klein. El espectro de J como
operador es {+1,−1} (involución): autoespacios par/impar bajo la reflexión. El espectro de H_C
(generador de escala) es {γ_ρ} (continuo + absorción, Connes). Un operador con espectro {±1} no puede
ser e^{itH} con espec(H)={γ_ρ} salvo en casos triviales (requeriría e^{itγ_ρ}∈{±1} ∀ρ, imposible para
{γ_ρ} denso). Luego J≠e^{itH_C}. Y J conmuta con H_C (ambos respetan la funcional) pero esto sólo dice
que H_C es J-equivariante, no autoadjunto. ∎(b)

(c) Stone es una biyección {flujos unitarios ℝ}↔{autoadjuntos}. J no es un flujo ℝ (es ℤ/2), así que
Stone no lo consume: no produce "espec(H_C)⊂ℝ" a partir de J. La realidad de {γ_ρ} (RH) es propiedad
de H_C (autoadjunción), y J —incondicional, ciego a m por la simetría par/impar— no la implica: J
está satisfecha tanto si los ceros están en la línea como si están en cuádruplos off-line (los
cuádruplos son J,c-simétricos por construcción). **J no ve m.** (Esto reencuentra Phase 52 Prop.
162.9: la funcional fuerza la hiperbolicidad/ceguera; aquí: la funcional es unitaria pero ciega a m.) ∎

**Interpretación (el corazón del veredicto B).** Hay DOS grupos de un parámetro/simetrías en juego y
NO coinciden:
- El **flujo de escala** (dilatación, e^{itH_C}, grupo ℝ): su unitariedad daría RH por Stone, pero su
  unitariedad en el espacio correcto = forma de Weil = ζ (Prop. 164.4). Estructural pero ζ-portador.
- La **reflexión funcional** (J, grupo ℤ/2): unitaria RH-libre, estructural, pero está en el grupo
  equivocado y es ciega a m (Prop. 164.6). RH-libre pero impotente.

La esperanza de (A) era que la segunda diera la unitariedad de la primera. NO lo hace: actúa en la
dirección de conjugación (γ↦−γ, reflexión del eje), no en la dirección de evolución (γ∈ℝ). **La
unitariedad esquiva la métrica sólo en el parámetro inútil.**

---

## 4. Dónde paran Berry–Keating y Connes, y si Stone toca un punto nuevo

### 4.1 Berry–Keating: para en la autoadjunción esencial / las condiciones de borde

**Lo que logran** (Berry–Keating 1999, *SIAM Rev.* 41): H=xp con la regularización semiclásica
reproduce la densidad promedio de ceros N(T)∼(T/2π)log(T/2πe)−T/2π+… vía la fórmula de Weyl
(área del espacio de fases bajo las hipérbolas xp=E con cortes ℓ_x,ℓ_p). El número de niveles hasta E
sale del área (2π)^{−1}∮ = correcto a primer orden.

**Dónde paran (preciso).** xp = ½(xp+px) sobre L²(ℝ₊) es simétrico pero tiene **índices de
deficiencia (1,1)** (no es esencialmente autoadjunto): la ecuación x f' + ½f = ±i f tiene una solución
L² en cada signo, f_±(x)=x^{−1/2±i}, ambas en L²(0,1] pero el comportamiento en 0/∞ deja un defecto.
Hay por tanto una familia U(1) de extensiones autoadjuntas (parametrizada por una fase de borde
θ∈[0,2π)). **Cada extensión da un espectro discreto distinto; NINGUNA da {γ_ρ} salvo una elección de
condición de borde que codifica ζ.** El "potencial de borde" que seleccionaría la extensión correcta
es la fase de ζ en la línea crítica (arg ζ(½+it)) — exactamente el dato que enumera los ceros. Sierra
y colaboradores (G. Sierra, "The Riemann zeros as spectrum and the Riemann hypothesis", *Symmetry* 11
(2019) 494; Sierra–Townsend; Berry–Keating "A compact hamiltonian with the same asymptotic mean
spectral density as the Riemann zeros", *J. Phys. A* 44 (2011) 285203) han construido Hamiltonianos
xp-modificados (x p en una región, con reflexión) que dan la densidad promedio *exacta* incluso con
correcciones, pero las fluctuaciones (los γ exactos) requieren un término semiclásico = Σ_p (la suma
sobre primos) — i.e., el dato de ζ entra como las "órbitas periódicas" del sistema. **El muro de
Berry–Keating = la elección de extensión autoadjunta / las órbitas periódicas = ζ.**

### 4.2 Connes: para en el espectro de absorción y la positividad de la traza

**Lo que logran** (Connes 1999, *Selecta* 5). Sobre el espacio de clases de adeles C_ℚ con el flujo de
escala, los ceros aparecen como espectro de **absorción** (huecos en el espectro continuo), no de
emisión. La fórmula de traza es semilocal (suma sobre lugares), y vale la identidad de Weil. **El muro:
la positividad de la distribución de Weil (Tr de Weil ≥0) ⟺ RH** — Connes reduce RH a esa positividad,
que queda abierta. Connes–Consani (B3.1; 2006, *2006.13771*) refinan: realizan la parte arquimediana
como traza sobre el espacio de Sonin (cuadrado manifiesto TT*≥0) más un residual ε(ρ), y RH ⟺ el
residual mantiene el signo. El espacio de Sonin es **zero-independent** (definido por el cutoff de
fase, funciones prolatas), pero el residual ε *no* lo es.

**Dónde paran (preciso).** El espectro de absorción NO es el espectro de un operador autoadjunto de
emisión: es la ausencia de algo en un continuo. Stone se aplica al generador del flujo (autoadjunto,
espectro continuo ℝ), no a la estructura de absorción. La positividad de la traza de Weil = la métrica
de Weil ≥0 = forma Q≥0 (Phase 26). **El muro de Connes = positividad de la traza = forma de Weil Q≥0 =
exactamente Prop. 164.4(ii).**

### 4.3 ¿Toca Stone un punto NUEVO, o reproduce su muro?

**Respuesta: reproduce el muro de Connes (la positividad = métrica = Q), pero lo NOMBRA con una
estructura nueva (Stone invertido) y descarta limpiamente la ruta de la simetría funcional.** Detalle:

- Stone *no* toca un punto que Berry–Keating/Connes no tocaran. La positividad de la traza de Weil
  (Connes) ES "U(t) unitario sobre el espacio correcto" (Prop. 164.4(iii)). El defecto de índices de
  deficiencia (Berry–Keating) ES "qué extensión autoadjunta = qué producto interno" (Prop. 164.4(ii)).
  Son la misma cosa. Stone los unifica: ambos son "la métrica que falta".
- Lo NUEVO de este documento (no de Stone, sino de su importación honesta):
  1. **El diagnóstico Stone-invertido** (Prop. 164.4): explicita POR QUÉ Stone no transfiere —en QM la
     métrica es axioma (Born), en RH es teorema (positividad de Weil). Esto reordena el muro de Connes
     como "falta el axioma de Born aritmético", lo cual es más preciso que "falta la positividad".
  2. **El descarte de la simetría funcional** (Prop. 164.6): la mejor candidata a "unitariedad
     estructural RH-libre" (la funcional) se prueba que está en el grupo equivocado (ℤ/2 reflexión, no
     ℝ flujo) y es ciega a m. Esto cierra una ruta que el mandato planteaba como abierta, sin dejarla
     en [GAP].
- Stone **NO** reproduce el muro de Phase 52 (la clase fundamental del portador): es un nodo
  distinto. Phase 52: ζ en el dato de homotopía [C_Φ]=Σδ_{γ_ρ}. Phase 53: ζ en el producto interno
  que hace unitario el flujo. Ambos son facetas de la trifurcación D156 (i)/(ii), pero la formulación
  Stone-invertida es genuinamente otra lente.

---

## 5. ¿Autoadjunción POR LA FORMA? El punto decisivo

El mandato pregunta lo correcto: en QM −Δ+V es autoadjunto *por su forma* (V real, −Δ semiacotado;
Reed–Simon II, Thm X.28, Kato–Rellich), y el espectro real es automático sin verificar nada. ¿Hay un
operador aritmético autoadjunto-por-su-forma con espectro {γ}?

### 5.1 [PROPOSICIÓN 164.8 — no hay forma manifiestamente autoadjunta RH-libre; el "potencial" es ζ]

**Enunciado.** Para los candidatos naturales a "operador con espectro {γ_ρ} autoadjunto por su forma":

(a) **Berry–Keating −d²/dx²+V o xp regularizado:** no es autoadjunto por su forma. xp tiene índices de
deficiencia (1,1) (§4.1); el operador no es semiacotado (su espectro clásico es toda la recta, las
hipérbolas xp=E cubren E∈ℝ), de modo que la maquinaria Kato–Rellich/forma-cerrada-semiacotada **no
aplica**. El "potencial" que produciría {γ_ρ} exacto es la condición de borde/órbitas periódicas = ζ.

(b) **Connes H_C (generador de escala):** es autoadjunto sobre L²(Haar) pero con espectro ℝ (ciego a
ζ, Prop. 164.4(i)); restringido al espacio que da {γ_ρ} (Pontryagin (𝒦,Q)), es Q-simétrico pero
autoadjunto ⟺ Q≥0 ⟺ RH (Phase 26). El "potencial real" aquí es la positividad de Q = ζ.

(c) **CCM / Meixner–Pollaczek:** el operador de Jacobi cuyas autofunciones son los P_n^(λ) ES
autoadjunto sobre L²(dm_∞), dm_∞=|Γ(1/4+is/2)|²ds, *por su forma* (operador de Jacobi con coeficientes
reales, esencialmente autoadjunto si el problema de momentos es determinado; Phase 38: RH ⟺ Δ_n
constante). Pero su espectro es el de los P_n (la medida de Meixner–Pollaczek = espectro de un
operador de creación-aniquilación tipo oscilador), **NO {γ_ρ}** — los γ_ρ entran sólo al *acoplar*
esta base a ζ vía la condición Δ_n constante, que es ζ. La forma es autoadjunta RH-libre, pero su
espectro no es el de los ceros; volverlo el de los ceros requiere ζ.

**Conjunción.** En los tres casos: o bien la forma es autoadjunta RH-libre pero su espectro NO es {γ}
(b: H_C sobre Haar; c: Meixner–Pollaczek), o bien el espectro sería {γ} pero la forma no es
autoadjunta-por-construcción y el término que la cerraría es ζ (a: Berry–Keating; b: H_C sobre 𝒦).
**No existe la combinación deseada (forma manifiestamente autoadjunta RH-libre CON espectro {γ}).** El
"potencial V" que produce {γ} es real ⟺ RH: ζ está en el potencial. Es el mismo muro.

**Prueba.**
(a) Índices (1,1) de xp: §4.1, la ecuación de deficiencia (x∂_x+½∓i)f=0 da f=x^{−1/2±i}∈L²(0,1] pero
la simetría requiere igualar dos extensiones; el operador no es semiacotado (espectro clásico ℝ), luego
los criterios de forma semiacotada (Reed–Simon II X.23, KLMN) no se aplican: no hay forma cerrada
inferiormente acotada cuyo operador asociado sea xp. La autoadjunción, si se logra, es por elección de
extensión, no por la forma. ∎(a)

(b) H_C sobre L²(Haar): autoadjunto, espectro ℝ (Prop. 164.4(i)). Sobre (𝒦,Q): Phase 26, H_C es
Q-simétrico; autoadjunto en el sentido de Pontryagin ⟺ neg.ind(Q)=0 ⟺ κ=0 ⟺ m=0 ⟺ RH. La "realidad
del potencial" = positividad de Q. ∎(b)

(c) El operador de Jacobi J_MP con coeficientes a_n,b_n reales (los de la relación de recurrencia de
Meixner–Pollaczek) es esencialmente autoadjunto sobre los polinomios densos en L²(dm_∞) sii el
problema de momentos de dm_∞ es determinado (Akhiezer, *The Classical Moment Problem*, Oliver & Boyd
1965, cap. 1–2; dm_∞ es determinado, decaimiento |Γ|² exponencial). Su espectro = soporte de dm_∞ =
ℝ (los P_n son ortogonales en toda la recta). Ése NO es {γ_ρ}: es el espectro del oscilador de
Meixner–Pollaczek (continuo absolutamente continuo), no los ceros discretos. La conexión con ζ es la
fórmula de momentos / la condición Δ_n=const (Phase 38), que es donde entra ζ. La forma autoadjunta es
RH-libre pero "su V" no es el de los ceros. ∎(c) ∎

**Interpretación.** Éste es el test decisivo del mandato y su resultado es nítido: **autoadjunción
por la forma SÍ existe (Meixner–Pollaczek, H_C sobre Haar) pero con el espectro equivocado; el
espectro {γ} SÍ se puede pedir pero entonces la forma no es autoadjunta-por-sí-misma.** Las dos
propiedades deseadas son mutuamente excluyentes sin ζ. El potencial real ⟺ RH. No hay grial.

---

## 6. Veredicto honesto (A/B/C/D) y el GAP central

**VEREDICTO: B (la unitariedad/autoadjunción es la métrica de Weil disfrazada, nodo localizado) con
un fragmento nuevo de D (la discrepancia de los dos grupos de un parámetro).** NO es A: no construí una
evolución unitaria estructural con espectro {γ} y unitariedad RH-libre, y desconfiaba de A con razón.
NO es A disfrazado.

**Lo que SÍ se estableció (genuino):**
- El diccionario QM↔RH preciso (§1), con las únicas dos casillas no-RH-libres aisladas: "energía
  conservada" y "producto interno", que son la misma y son ζ.
- **El teorema de Stone invertido** (Prop. 164.4): en QM la métrica es axioma (Born) y Stone da
  espectro real gratis; en RH la métrica es teorema (positividad de Weil), Stone importa la conclusión
  no la hipótesis, y "U(t) unitario en el espacio correcto" = Q≥0 = RH. Modo de fallo nuevo respecto
  de Phase 52.
- **El descarte de la simetría funcional** (Prop. 164.6): la mejor candidata a unitariedad estructural
  RH-libre (la ecuación funcional J) ES unitaria y RH-libre, PERO vive en el grupo de reflexión ℤ/2,
  no en el flujo ℝ que Stone consume, y es ciega a m (γ↦−γ, conjugación, no γ∈ℝ, evolución). Ruta
  cerrada, no dejada en GAP.
- **No hay autoadjunción por la forma RH-libre con espectro {γ}** (Prop. 164.8): existe forma
  autoadjunta (Meixner–Pollaczek, H_C/Haar) con espectro equivocado, o espectro {γ} con forma no
  autoadjunta-por-sí (Berry–Keating, H_C/𝒦); las dos no coexisten sin ζ. El potencial real ⟺ RH.

**Dónde reentra ζ (preciso, y por qué es NUEVO).** NO en la clase fundamental del portador (Phase 52),
NO en la orientación modular (Phase 51). Reentra en **el producto interno que vuelve unitario el flujo
de escala** = la forma de Weil Q = la "regla de Born aritmética". El mecanismo nuevo: la dirección
lógica de Stone está INVERTIDA respecto de QM. En QM la métrica es el axioma de partida; en RH es la
incógnita de llegada. La única simetría unitaria RH-libre disponible (la funcional) está en el grupo
equivocado.

**El GAP central / fragmento de D (nombrado y nuevo).**

> **[GAP/DESEO 164.D — la discrepancia de los dos grupos de un parámetro].** El programa tiene dos
> simetrías unitarias: la **dilatación** (flujo de escala, grupo ℝ, e^{itH_C}, generador con espectro
> {γ} pero unitariedad=ζ) y la **reflexión funcional** (J, grupo ℤ/2, unitaria RH-libre pero ciega a
> m). La obstrucción a (A) es que estos dos grupos NO se combinan en un único grupo de un parámetro
> cuya unitariedad sea simultáneamente estructural (de J) y evolutiva (de H_C). En QM esto sí pasa: la
> reflexión de paridad y la evolución temporal son ambas unitarias respecto de la MISMA métrica de
> Born, y conmutan dando un grupo más grande (ℝ⋊ℤ/2). El [GAP] es: **¿existe una métrica RH-libre
> respecto de la cual TANTO J COMO el flujo de escala sean unitarios, de modo que la J-invariancia
> (RH-libre) propague a la realidad del espectro de H_C (RH)?** En QM la propagación es trivial (una
> sola métrica). Aquí, J es unitaria respecto de la métrica de Lebesgue/de Branges (RH-libre) y H_C es
> unitario respecto de la métrica de Weil Q (ζ); que sean la MISMA métrica es exactamente RH (Phase 26:
> Q≥0 = realidad de {γ}). Este GAP es distinto de la "hebra diofántica" (GAP-157.A) y de la "dualidad"
> (Phase 52): es la **no-compatibilidad de las dos métricas naturales (reflexión vs. evolución)**, y
> es, creo, una formulación nueva del muro: *RH ⟺ la métrica de la reflexión funcional = la métrica de
> la evolución de escala.* No tengo prueba de que esta reformulación sea más tratable; la dejo como
> [GAP central], honestamente, porque podría ser circular (la igualdad de métricas ES Q≥0). Pero la
> *forma* —"unificar dos grupos de un parámetro en una métrica común"— es un problema de física
> matemática estándar (representaciones del grupo de Galilei/Poincaré: una métrica, varios generadores)
> y nombra el muro en lenguaje de teoría de representaciones, que el programa no había usado.

**Síntesis estratégica (lo nuevo de verdad).** El programa creía haber aislado el muro en la
*métrica de lectura de inercia* (Phase 51) y luego en la *clase fundamental del portador* (Phase 52).
Este documento muestra que la importación de Stone —la herramienta de QM que da realidad espectral
gratis— **no transfiere, porque transfiere la conclusión y no la hipótesis**: QM tiene la métrica
gratis (Born) y RH debe demostrarla (positividad de Weil). La simetría funcional, que parecía la vía
de escape (unitariedad por simetría, no por métrica), es unitaria y RH-libre pero en el grupo
equivocado (reflexión ℤ/2, no evolución ℝ) y ciega a m. El muro se reubica con precisión: **RH ⟺ la
métrica que vuelve unitaria la reflexión funcional coincide con la que vuelve unitaria la evolución de
escala** (GAP 164.D). No es A; es B con un GAP de tipo D formulado en teoría de representaciones,
distinto de los GAPs previos del programa. La unitariedad NO esquiva la métrica: en el parámetro útil
(el flujo de escala) la unitariedad ES la métrica de Weil; en el parámetro RH-libre (la funcional) la
unitariedad existe pero no toca m.

---

## 7. Apéndice: tabla de etiquetas (auditoría interna) y test de unitariedad por paso

### 7.1 Etiquetas

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| §1 Diccionario QM↔RH | mapa preciso, dos casillas no-RH-libres | **establecido** (PUENTE 164-A) |
| [CONSTRUCCIÓN] U(t) flujo de escala (§2.2) | grupo de dilataciones, H_C generador | definido; espectro Haar = ℝ (ciego), espectro {γ} requiere recorte |
| [PROP 164.4] Stone invertido | unitariedad en el espacio correcto = Q≥0 = RH | **probado** (implicación lógica vía Phase 26/51) |
| [PROP 164.6] funcional unitaria RH-libre pero grupo equivocado | J∈ℤ/2 reflexión, ciega a m, ≠e^{itH_C} | **probado** (J²=1, espectros incompatibles, ceguera a m) |
| §4 Berry–Keating/Connes | paran en deficiencia (1,1)/borde y en positividad de traza=Q | **localizado** (con refs) |
| [PROP 164.8] no hay forma autoadjunta RH-libre con espectro {γ} | forma OK ⟹ espectro≠{γ}; espectro={γ} ⟹ forma no autoadj. sin ζ | **probado** (xp deficiencia; H_C; Meixner–Pollaczek momentos) |
| [GAP/DESEO 164.D] dos grupos de un parámetro | RH ⟺ métrica(reflexión)=métrica(evolución) | **GAP central, nuevo, no probado; posible circularidad declarada** |

### 7.2 El test de unitariedad, paso a paso (la guardia)

| Paso | ¿Unitariedad usa métrica-ζ? | Veredicto |
|---|---|---|
| U(t) sobre L²(Haar) (§2.2) | No (Haar es RH-libre) | **PASA pero espectro=ℝ, ciego a ζ** |
| U(t) sobre ℋ_γ (espectro={γ}) | Sí: el producto interno = forma de Weil Q | **FALLA: ζ reentra (Prop. 164.4)** |
| J = reflexión funcional (§3.3) | No (Lebesgue/de Branges, RH-libre) | **PASA pero grupo ℤ/2, ciego a m (Prop. 164.6)** |
| Forma de Jacobi Meixner–Pollaczek (§5) | No (coeficientes reales, momentos determinados) | **PASA pero espectro≠{γ} (Prop. 164.8c)** |
| xp / Berry–Keating con borde que da {γ} | Sí: la fase de borde = arg ζ / órbitas = primos | **FALLA: ζ en el borde (§4.1, Prop. 164.8a)** |
| H_C sobre Pontryagin (𝒦,Q) | Sí: autoadjunción = Q≥0 = RH | **FALLA: ζ = positividad (Prop. 164.4b, Phase 26)** |

**Lectura de la tabla.** Todo lo que es unitario/autoadjunto RH-libre tiene espectro equivocado
(ℝ o el del oscilador, no {γ}); todo lo que tiene espectro {γ} necesita la métrica de Weil = ζ para su
unitariedad. La frontera es exacta y sin huecos: **no hay una sola fila que sea simultáneamente
RH-libre Y de espectro {γ} Y unitaria.** Eso ES el desenlace B.

---

**Referencias (reales).**
- M.H. Stone, "On one-parameter unitary groups in Hilbert space", *Ann. of Math.* **33** (1932) 643–648.
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press
  1980 — Stone Thm VIII.7–VIII.8; *Vol. II: Fourier Analysis, Self-Adjointness*, 1975 — Thm X.1 (von
  Neumann, índices de deficiencia), X.23/KLMN (formas), X.28 (Kato–Rellich).
- M.V. Berry, J.P. Keating, "H=xp and the Riemann zeros", en *Supersymmetry and Trace Formulae: Chaos
  and Disorder*, ed. I.V. Lerner et al., Kluwer/Plenum 1999, pp. 355–367.
- M.V. Berry, J.P. Keating, "The Riemann zeros and eigenvalue asymptotics", *SIAM Review* **41** (1999)
  236–266.
- M.V. Berry, J.P. Keating, "A compact hamiltonian with the same asymptotic mean spectral density as
  the Riemann zeros", *J. Phys. A: Math. Theor.* **44** (2011) 285203.
- G. Sierra, "The Riemann zeros as spectrum and the Riemann hypothesis", *Symmetry* **11** (2019) 494.
- A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function",
  *Selecta Math. (N.S.)* **5** (1999) 29–106.
- A. Connes, C. Consani, "Weil positivity and trace formula, the archimedean place", arXiv:2006.13771
  (2020) — espacio de Sonin, cuadrado manifiesto, residual.
- J.-B. Bost, A. Connes, "Hecke algebras, type III factors and phase transitions with spontaneous
  symmetry breaking in number theory", *Selecta Math.* **1** (1995) 411–457 — partición = ζ.
- E.C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. Heath-Brown), Oxford 1986 —
  ecuación funcional §2.6.
- N.I. Akhiezer, *The Classical Moment Problem*, Oliver & Boyd 1965 — operador de Jacobi, determinación.
- [GAP de literatura]: no existe en la literatura una identificación "unitariedad del flujo de escala
  = forma de Weil" formulada como teorema de Stone invertido, ni la reformulación de RH como igualdad
  de las métricas de reflexión y evolución (GAP 164.D). Las referencias anclan las herramientas
  (Stone, von Neumann, Berry–Keating, Connes); el puente Stone-invertido y el GAP 164.D son nuevos.
```
