# Doc 163 — Destructor de la inercia homotópica secundaria

**Fase 52, junio 2026. Mandato adversarial: MATAR.**

## Afirmación bajo ataque

> *m* (número de ceros de ζ fuera de la línea crítica; RH ⟺ m=0; 2m = índice
> negativo de la forma de Weil Q) es un **invariante secundario homotópico**
> —e-invariante aritmético, corchete de Toda ⟨f,g,h⟩, o k-invariante— definible
> **sin** la forma Q, **RH-libre**, y que entrega 2m como salida.

**Motivación de la construcción (a derrotar):** el invariante PRIMARIO (clase de
Witt en L⁰) es ciego a m porque K_off es Witt-trivial (D132). Lo que es ciego al
primario es candidato a vivir en un piso secundario. Y los secundarios al estilo
e-invariante de Adams (Adams, *On the groups J(X) IV*, Topology 1966) son
"libres de métrica" —se leen de la estructura de homotopía estable, no de una
forma cuadrática.

**Tesis del destructor:** las tres vías de muerte son, en el fondo, **una sola
obstrucción vista tres veces**, y esa obstrucción ya está probada en el programa
(D156, D161). Procedo vía por vía y luego doy el veredicto.

---

## Preliminar: anatomía honesta de un invariante secundario

Para no atacar un fantasma, fijo qué ES un secundario, en cualquiera de sus tres
encarnaciones. Las tres comparten una arquitectura idéntica:

- **Corchete de Toda ⟨f,g,h⟩** (Toda, *Composition methods in homotopy groups of
  spheres*, 1962): definido cuando g∘f ≃ 0 y h∘g ≃ 0. El valor es
  H̄∘(g∘f-nullhtpy) − (h∘g-nullhtpy)∘F̄, vive en un cociente
  [ΣA,D]/(indeterminación). **Requiere DOS nullhomotopías** (las dos relaciones
  primarias nulas) y el secundario es la "diferencia entre los dos rellenos".
- **e-invariante de Adams** (Adams J(X) IV; APS II §4, Atiyah–Patodi–Singer,
  *Spectral asymmetry and Riemannian geometry II/III*, 1975–76): para
  f: S^{2n-1}→S^q estable con d-invariante (Chern primario) nulo, e(f)∈ℚ/ℤ se
  define eligiendo una variedad/cobordismo W con ∂W realizando f y leyendo
  ⟨ch∪Todd, [W,∂W]⟩ mód ℤ. **Requiere un RELLENO W (un cobordismo nulo del
  primario) y un género (ch·Td) integrado sobre él.**
- **k-invariante de Postnikov**: la obstrucción en H^{n+1}(X;π_n) a deformar la
  sección sobre el (n-1)-esqueleto; vive sobre el núcleo del invariante de orden
  inferior.

**Hecho estructural común (clave del ataque):** un invariante secundario es
*una integral de un relleno del primario*. Su buena definición exige (a) que el
primario se anule (estamos sobre su núcleo) y (b) elegir un relleno/nullhomotopía;
la indeterminación se mata por la imagen del primario de orden inferior. **Donde
el constructor diga "secundario sin métrica" yo pregunto: ¿qué es el relleno y
con qué se integra?** Ahí estará Q o no estará nada.

---

## Vía 1 — El secundario reintroduce la forma Q

**Pregunta:** ¿la nullhomotopía/relleno que define el e-invariante aritmético es
exactamente la forma de Weil (o la partición ζ)?

### Argumento de muerte (CERRADO)

Identifico el primario y el secundario con los objetos del programa, sin
ambigüedad:

- **Primario = clase de Witt de K_off en L⁰(ℝ) (o W(ℝ)=ℤ vía signatura).**
  D132 probó: K_off es **Witt-trivial**. Esto significa que la forma off-line es
  *metabólica/hiperbólica* en el sentido de Witt: posee un **lagrangiano**
  (subespacio isótropo de dimensión mitad). En L-teoría (Ranicki, *Algebraic
  L-theory and topological manifolds*, 1992, Cap. 1–3) la clase es cero PRECISAMENTE
  porque existe ese lagrangiano L con L=L^⊥.

- **El relleno del secundario ES la elección de ese lagrangiano.** Aquí está la
  trampa. La buena definición de cualquier secundario sobre el núcleo del primario
  Witt exige fijar el testigo de la nulidad primaria. El testigo de "Witt-trivial"
  NO es un dato libre: es el lagrangiano L, y un lagrangiano de una forma simétrica
  no degenerada **es un dato que sólo existe relativo a la forma**. No se puede
  nombrar L "sin Q": L=L^⊥ es una ecuación EN Q. (Ranicki, ibíd., §1.6: la clase
  de Witt es el cobordismo de formas; el cobordismo se exhibe por una *formación*
  (L, Q|L), que contiene Q.)

  Formalmente: el corchete de Toda análogo es ⟨ι, Q_off, π⟩ donde la relación
  intermedia nula "Q_off ≃ 0 en Witt" se realiza por la nullhomotopía =
  contracción a lo largo del lagrangiano. **Esa nullhomotopía transporta Q.**

- **Identificación con D161 (NUEVO, y es el golpe).** En el lenguaje de KK/peso
  dual de D161: la "orientación que convierte la clase de fase en signatura de
  inercia" es modular (el peso dual), no topológica. Traducción al lenguaje
  secundario: el relleno del e-invariante = la **orientación de Poincaré-NC** =
  el peso dual = el dato que D161 probó que tiene a ζ por función de partición.
  El secundario no esquiva esto; lo hereda, porque la nullhomotopía del primario
  ES la orientación que D161 ya identificó con ζ(β).

**Conclusión Vía 1: MATA.** El relleno (lagrangiano / orientación) que define el
secundario es la forma Q disfrazada de "testigo de la trivialidad de Witt".
Q reentra por la puerta de atrás —EXACTAMENTE el patrón de Phase 51 Doc 161
(la métrica canónica era ζ disfrazada vía el peso dual) y de Phase 43 (la métrica
de polarización porta los autovalores de Frobenius). El "secundario sin métrica"
es la métrica disfrazada de nullhomotopía.

[GAP residual menor] No descarto un secundario cuyo relleno NO sea el lagrangiano
de Witt sino una nullhomotopía de *otro* primario (p.ej. el d-invariante / Chern
de un mapa estable, no la clase de Witt). Eso lo capturan las Vías 2 y 3.

---

## Vía 2 — La Witt-trivialidad se propaga al secundario

**Pregunta:** si K_off es trivial en el primario, ¿hay razón para que el
secundario también lo mate? ¿El secundario captura m, o lo pierde por la misma
razón que el primario?

### Argumento de muerte (CERRADO, con un matiz importante)

Aquí debo ser justo con el constructor: el e-invariante existe **precisamente
para detectar lo que el primario no ve**. El d-invariante (Chern entero) no ve la
torsión; el e-invariante en ℚ/ℤ sí. Así que "primario trivial ⟹ secundario
trivial" es FALSO en general (ése es el punto entero de Adams). No puedo matar
por propagación automática. Tengo que mirar la ARITMÉTICA de m.

**El dato decisivo: 2m = κ es PAR y ENTERO.** (D132: κ=2m par; D156: κ=2m =
spectral flow = Maslov = APS-eta, **el mismo entero**.) Ahora confronto esto con
dónde vive cada invariante:

- **Un e-invariante de Adams vive en ℚ/ℤ.** Detecta torsión / la parte
  *fraccionaria* de un género. Captura lo que es invisible al entero porque el
  entero ya fue "modado fuera". Pero **m ya es un entero**, y de hecho 2m es el
  spectral flow —que es el invariante PRIMARIO entero de la inercia (π₁(Fred^sa)=ℤ,
  Atiyah–Patodi–Singer III §7; Phillips, *Self-adjoint Fredholm operators and
  spectral flow*, 1996). El spectral flow ES κ=2m (D156). **Entonces el "primario
  natural de la inercia" ya captura m completo, sin residuo en ℚ/ℤ.**

- **Pregunta del constructor invertida (y respondida):** *"si el flujo espectral
  ya ES el primario y captura κ, ¿qué piso secundario queda?"* — **Ninguno con
  carga.** La parte de ℚ/ℤ del e-invariante es exactamente la parte que el flujo
  espectral entero **NO** ve. Pero m=½κ ya está enteramente en el flujo espectral
  entero. Por tanto la proyección de κ al receptor secundario ℚ/ℤ es
  **2m mód ℤ = 0** (m entero). **El secundario en ℚ/ℤ aniquila m por construcción
  del receptor.** No por Witt-trivialidad del primario, sino porque el receptor
  natural del secundario es un grupo donde los enteros son cero.

- **¿Y un secundario con receptor NO-ℚ/ℤ?** (p.ej. un corchete de Toda con valor
  en un grupo de homotopía estable finito π^s_k, o un k-invariante en
  H^{n+1}(·;ℤ).) Aquí la Witt-trivialidad SÍ se propaga, vía D132 directamente:
  K_off Witt-trivial = existe lagrangiano = la formación es *split*. Una
  formación split tiene **corchete de Toda con indeterminación total** (la
  nullhomotopía del medio es canónica vía el lagrangiano, luego ⟨f,Q_off,h⟩
  contiene el cero / es indeterminado). En el lenguaje de Ranicki: el cobordismo
  de la formación split es trivial también en el nivel de cobordismo de
  cobordismos (L-teoría es 4-periódica y los grupos relativos de una clase nula
  con relleno canónico se anulan). **Witt-trivial + relleno canónico ⟹ secundario
  indeterminado/trivial.**

**Conclusión Vía 2: MATA, por dicotomía de receptor.**
- Si el receptor es ℚ/ℤ (estilo Adams): m entero ⟹ proyección = 0. El secundario
  pierde m por *aritmética del receptor*, no por la métrica. **Nodo NUEVO**
  (distinto de D156/D161: aquí ζ ni siquiera entra; muere antes, por paridad).
- Si el receptor es entero (estilo spectral flow / k-invariante en ℤ): entonces el
  secundario **es** el primario de inercia (κ ya entero), no hay piso por debajo,
  y la Witt-trivialidad de D132 vuelve la formación split ⟹ indeterminación total.

El constructor está atrapado entre dos receptores: el "honestamente secundario"
(ℚ/ℤ) no puede llevar un entero, y el "que lleva el entero" no es secundario sino
el spectral flow primario que D156 ya mostró que exige Fredholmicidad = m<∞ = RH
por la puerta de atrás.

---

## Vía 3 — El espectro portador rehereda {log k} ⟹ partición ζ

**Pregunta:** ¿el espectro de homotopía estable / la aplicación estable de la que
se toma el e-invariante está construida, en el fondo, del operador de los primos
(espectro {log k})? ¿Hay un portador SIN el flujo de los primos, o es inevitable?

### Argumento de muerte (CERRADO bajo una hipótesis nombrada; si no, [GAP])

El no-go de Phase 49/51 dice: cualquier objeto cuyo espectro sea {log k} tiene
función de partición ζ (D161 §161.5: Z(β)=Σk^{-β}=ζ(β), idéntico a Bost–Connes).
El e-invariante aritmético, para *computar 2m a partir de los primos*, necesita un
portador cuya información aritmética sean los primos. Hay exactamente dos
posibilidades:

**(3a) El portador SÍ es el flujo de los primos.** El e-invariante aritmético se
computaría vía un carácter de Chern / género de Todd de un objeto (mapa estable,
o D del triple espectral) cuya zeta espectral es ζ. Esto es forzoso si el
constructor quiere que el secundario "salga de los primos" para ser RH-libre y
aún así *hablar de los ceros de ζ*. Pero entonces:

- El género de Todd / ch·Td que define el e-invariante (APS II §4) se integra
  contra la **densidad espectral del portador**, y esa densidad es exactamente la
  que produce ζ(β) (D161). El "puente Euler {log k}→{γ_ρ}" reaparece: pasar de la
  partición ζ(β) a los γ_ρ es continuación analítica a los ceros. **ζ reentra
  como función de partición del portador** —MISMO nodo que D161 (orientación/
  normalización), no nuevo.

**(3b) El portador NO es el flujo de los primos** (espectro ≠ {log k}, partición
≠ ζ). Entonces el portador no sabe nada de los γ_ρ ni de m. El e-invariante sería
RH-libre pero **vacío respecto de m**: computa un número de homotopía de un objeto
sin relación probada con los ceros. Para conectarlo con m haría falta una
identificación "este e-invariante = 2m", y esa identificación es exactamente el
[GAP central] heredado de D156 §4.5 / D161 §confín: *un triple espectral cuyo D NO
sea el flujo de los primos pero cuyo Chern = κ = 2m*. **Ese objeto es el grial
inexistente del programa, no algo que el e-invariante regale.**

**Conclusión Vía 3: MATA por dicotomía (la misma trifurcación de D156),
salvo un GAP nombrado.**
- Rama (3a): portador = primos ⟹ partición = ζ ⟹ NO RH-libre. ζ en el nodo
  ORIENTACIÓN/NORMALIZACIÓN (conocido, = D161).
- Rama (3b): portador ≠ primos ⟹ RH-libre pero el puente "e = 2m" es
  precisamente el objeto Connes/Deninger inexistente [GAP-central, = D156 §4.5].

El e-invariante no abre un escape nuevo a la rama (3b): la *traslada* del nivel
"métrica" (D161) al nivel "identificación homotópica", pero el contenido del GAP
es idéntico —construir un portador aritmético genuino sin que su zeta espectral
sea ζ. **El secundario no toca un nodo nuevo de ζ; toca el MISMO nodo de D161
(partición del portador) o cae en el MISMO GAP de D156 (objeto inexistente).**

---

## Veredicto

**Las tres vías MATAN**, y —hallazgo central— **matan por una sola obstrucción
vista en tres niveles**, que es la misma trifurcación de D156 trasladada al piso
secundario:

| Vía | Mecanismo de muerte | Nodo de ζ | ¿Nuevo? |
|-----|--------------------|-----------|---------|
| 1 (relleno = forma) | la nullhomotopía/lagrangiano que define el secundario ES Q (orientación = peso dual) | ORIENTACIÓN | conocido (= D161) |
| 2 (Witt se propaga) | dicotomía de receptor: ℚ/ℤ aniquila m entero (2m mód ℤ=0); ℤ ⟹ es el spectral flow primario, no secundario | — (muere antes de ζ, por paridad) | **NUEVO** |
| 3 (portador {log k}) | portador=primos ⟹ partición ζ; portador≠primos ⟹ GAP-grial | ORIENTACIÓN o GAP-existencia | conocido (= D161/D156) |

La construcción no sobrevive. **La razón profunda:** un invariante secundario es
una *integral de un relleno del primario*; el primario relevante (Witt) es trivial
por D132 *vía un lagrangiano que es un dato de Q*, así que el relleno reintroduce
Q (Vía 1); y el receptor honesto de un secundario (ℚ/ℤ) no puede albergar el
entero m (Vía 2). La "ceguera del primario a m" que motivaba la construcción es
real pero **estéril**: el primario es ciego a m no porque m viva en un piso
secundario accesible, sino porque m es la *signatura*, que ningún invariante
Witt/homotópico-estable lee sin reintroducir la forma o el portador-primos.

### Lo que tendría que ser verdad para que sobreviviera (complemento de los 3 ataques)

Aunque mi veredicto es muerte, registro honestamente el escape lógico —es el
mismo grial de D156/D161, ahora con una condición homotópica precisa añadida:

1. **(contra Vía 1)** Existe una nullhomotopía del primario de inercia que
   **no** sea el lagrangiano de Q ni la orientación modular —un relleno
   *puramente homotópico* (p.ej. una contracción en un espectro estable) cuya
   buena definición no invoque ninguna forma cuadrática ni el peso dual. Tendría
   que probarse que la indeterminación del corchete de Toda asociado se mata
   **sin** usar Q.
2. **(contra Vía 2)** El secundario tiene receptor que **distingue 2m de 0
   módulo la indeterminación** y no es ℚ/ℤ (que mata enteros) ni ℤ (que lo
   colapsa al spectral flow primario). Candidato lógico: un grupo de homotopía
   estable π^s_* con torsión *adecuada* tal que la imagen de 2m sea no nula y
   distinga m —pero NINGÚN ejemplo conocido empareja π^s_* con un conteo de ceros
   [GAP de literatura, fuerte].
3. **(contra Vía 3)** Existe un portador estable / triple espectral aritmético
   cuyo D **no** tenga espectro {log k} (luego partición ≠ ζ) y cuyo e-invariante
   (ch·Td mód ℤ) **iguale 2m** por un teorema. Este es exactamente el
   [GAP-central D156 §4.5] = el objeto Connes/Deninger inexistente. El aporte de
   Fase 52 es estrecharlo: ya no basta "Chern=κ"; ahora se pide además que el
   invariante sea de orden ≥2 (secundario) con relleno no-Q. **Es MÁS difícil,
   no menos.**

Las tres condiciones deben darse **simultáneamente** (un relleno no-Q sobre un
portador no-primos con receptor que distinga el entero). No conozco ningún
candidato en la literatura que cumpla siquiera dos.

---

## Mensaje final

**MATAN LAS TRES.** La más limpia y la única con sabor genuinamente nuevo es la
**Vía 2 (dicotomía de receptor)**: el e-invariante honesto vive en ℚ/ℤ y *m es un
entero* (2m=κ par, D132), de modo que 2m mód ℤ = 0 —el secundario aniquila m por
**aritmética del receptor**, antes de que ζ tenga ocasión de aparecer. Las Vías 1
y 3 reconducen al nodo ya conocido (ζ en la ORIENTACIÓN/partición del portador,
= D161) o al GAP-grial de existencia (= D156). **El secundario NO toca a ζ en un
nodo nuevo:** o muere antes (Vía 2, por paridad), o muere en el nodo
ORIENTACIÓN de D161 (Vías 1 y 3a), o cae en el GAP de EXISTENCIA de D156 (Vía 3b).

**Tres hallazgos etiquetados:**

- **[HALLAZGO 163.1 — el relleno ES la forma]** La nullhomotopía que da buena
  definición a cualquier secundario sobre el núcleo de Witt es el *lagrangiano*
  que atestigua la Witt-trivialidad de K_off (D132); un lagrangiano L=L^⊥ es un
  dato de Q por definición. Identificado con la "orientación = peso dual" de D161:
  el secundario hereda ζ por el MISMO eslabón que la métrica canónica. *Q reentra
  como testigo de su propia trivialidad.*

- **[HALLAZGO 163.2 — paridad mata el receptor]** (NUEVO, no en D156/D161.)
  Como κ=2m es par y entero, su imagen en el receptor natural del e-invariante
  (ℚ/ℤ) es 0. El secundario "estilo Adams" no puede transportar a m por la
  estructura misma de su grupo de valores, independientemente de ζ y de la métrica.
  El único receptor que lleva el entero es ℤ, donde el "secundario" colapsa al
  spectral flow primario —que D156 ya mostró que exige Fredholmicidad = m<∞ = RH.

- **[HALLAZGO 163.3 — el secundario estrecha, no abre, el GAP-grial]** La ruta
  homotópica secundaria es una *traslación* de la trifurcación de D156, no un
  escape: traslada la exigencia "Chern=κ sin portar ζ" a "e-invariante=2m con
  relleno no-Q sobre portador no-primos y receptor que distinga el entero". Esto
  AÑADE condiciones al grial inexistente; lo hace estrictamente más difícil. Es
  consistencia, no progreso: el muro de Phase 43 sigue en pie, ahora también
  contra la inercia homotópica secundaria.

**Disciplina:** ningún teorema "RH ⟺ X" producido; ningún numérico; el escape
lógico (sección "qué tendría que ser verdad") queda registrado como [GAP] honesto,
no como esperanza. Veredicto: la afirmación de Fase 52 está **destruida** salvo
por el grial Connes/Deninger ya conocido, ahora con tres candados adicionales.
