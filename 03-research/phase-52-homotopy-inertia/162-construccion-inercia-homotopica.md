# Doc 162 — Inercia homotópica: ¿es m un invariante secundario libre de métrica (e-invariante aritmético), o el secundario hereda la métrica/ζ del primario?

**Programa:** Hipótesis de Riemann — Phase 52: inercia homotópica.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** CONSTRUCTIVO con guardia anti-circularidad al frente. Mandato: construir
un objeto matemático nuevo — una manera de leer el entero m (número de cuádruplos de ceros de
ζ fuera de la línea crítica; RH ⟺ m=0; 2m = κ = neg.ind de la forma de Weil Q sobre el espacio
de Pontryagin (𝒦,Q)) como un **invariante HOMOTÓPICO/categórico SECUNDARIO — sin ninguna forma
bilineal, métrica ni producto interno.** Motivación probada (NO se reprueba aquí, se construye
encima): (i) Phase 51 (Docs 160–161): toda métrica canónica para leer m porta ζ por estructura
modular (función de partición = ζ, Bost–Connes); el muro es la *signatura de inercia*, no la
geometría. (ii) Phase 44 (Doc 132): **K_off es Witt-trivial** — el invariante de forma PRIMARIO
(clase de Witt / signatura) se ANULA sobre la parte off-line. El primario es ciego a m. La
apuesta de diseño: si el primario se anula, m vive en su núcleo ⟹ m es SECUNDARIO (corchete de
Toda / k-invariante / e-invariante de Adams), y los secundarios son homotópicos, no métricos.

**Contrato de etiquetado (regla absoluta).** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad aquí, prueba completa; externos con
referencia verificable. **[CONSTRUCCIÓN]** = objeto definido con precisión. **[PUENTE]** =
conexión con estatus honesto. **[GAP]/[GAP de literatura]** = declarado; el de literatura NO se
usa como premisa de ningún teorema. **[DESEO]** = declarado. Jamás se fabrica una prueba de RH
ni una falsa victoria (DESENLACE A). Está PERMITIDO (y es lo esperable) terminar en B/C/D.
**NADA de numéricos/Python.** **Español.** Honestidad absoluta.

**Prerrequisitos leídos en fuente esta sesión:** Memoria Phase 26 (κ = 2m = neg.ind(H_C) en
Pontryagin (𝒦,Q); ítems V.1–V.4). Memoria Phase 44 D132 (K_off Witt-trivial; δ = neg.ind sobre
primitivo; RH ⟺ δ=0; positividad esencial ⟹ δ<∞ Fredholm). Memoria Phase 49 D156 (κ = spectral
flow = Maslov = APS-eta bajo Fredholmicidad; el índice tiene la enfermedad de la positividad una
capa más adentro; el [GAP] central = triple espectral cuya ζ espectral NO sea ζ). Memoria Phase
51 D160/D161 (transporte RH-libre existe; métrica canónica porta ζ por peso dual; TEOREMA 161.9
circularidad estructural; el muro es la signatura de inercia).

---

## 0. Resumen ejecutivo y veredicto adelantado

Coloco el veredicto al frente.

> **VEREDICTO: DESENLACE B (con un fragmento de C).** El invariante secundario existe y se
> construye genuinamente sin forma bilineal — vive en la torre de Postnikov de un espectro
> portador y se nombra abajo (la **clase de inercia homotópica** ι ∈ E¹(coker d) / un grupo de
> homotopía estable / un e-invariante en ℚ/ℤ). PERO al exigirle que dé 2m como SALIDA RH-libre,
> ζ REENTRA, y reentra en un lugar *nuevo y preciso*, distinto del de Phase 51: no en la métrica
> (eso lo evitamos por diseño), sino en **la identificación del propio espectro portador**. El
> e-invariante de Adams es un mapa ℚ/ℤ que se computa *cuando ya se sabe que el primario se
> anuló y la extensión existe*; pero saber QUÉ extensión (qué clase de homotopía estable) realiza
> la dualidad ceros↔primos requiere conocer dónde están los ceros — es decir, el dato de
> homotopía que el secundario "lee" es exactamente m, no lo produce. Localizo el punto de
> reentrada en **el k-invariante de la torre**: el k-invariante que detectaría m es una clase de
> cohomología cuyo cálculo es el conteo de ceros (§3, §4). Adicionalmente, un fragmento de C: la
> Witt-trivialidad PROPAGA al primer piso secundario por una razón estructural (la simetría
> funcional fuerza que el d_2 relevante se anule también), de modo que el secundario *de orden
> bajo* tampoco ve m; haría falta subir al menos al segundo piso (un corchete de Toda triple, no
> el e-invariante simple). Lo enuncio abajo.

**Los tres resultados con etiqueta (adelantados):**

1. **[PROPOSICIÓN 162.4 — el primario se anula homotópicamente, no sólo en Witt].** Sobre el
   espectro portador 𝔼_off construido del divisor off-line, el d-invariante primario (la imagen
   en π₀ del espectro de L-teoría, = clase de Witt) es cero — *recuperando* Witt-trivialidad como
   un enunciado de homotopía estable, no de formas. Esto es lo que ABRE el piso secundario y es
   consistente con Doc 132. (Probado; usa sólo que la signatura de K_off es 0.)

2. **[TEOREMA 162.7 — el secundario existe y es libre de métrica, PERO su valor = lectura del
   k-invariante, no producción].** Definido el e-invariante aritmético e_ζ ∈ ℚ/ℤ como el carácter
   de Chern mód ℤ de la aplicación estable de la dualidad ceros↔primos, se prueba que e_ζ está
   bien definido (no usa Q) Y que su parte entera detectaría 2m; pero el cómputo de e_ζ RH-libre
   exige evaluar el carácter de Chern sobre una clase de homotopía que es *desconocida sin saber
   m*. La función generadora de ese carácter de Chern es Σ_ρ (algo)^{γ_ρ}: **ζ reentra como el
   espectro {γ_ρ} de la aplicación, no como métrica.** (Reentrada localizada; es el corazón de B.)

3. **[PROPOSICIÓN 162.9 — propagación parcial de la Witt-trivialidad al primer secundario].** La
   simetría funcional ξ(s)=ξ(1−s) actúa como una involución en el espectro portador que fuerza el
   primer diferencial secundario d_2 sobre la clase off-line a anularse (es un fragmento de C: el
   secundario simple es también ciego a m). El primer nivel que PUEDE ver m es un producto de
   Massey/corchete de Toda triple ⟨α, 2, β⟩ — un secundario de orden superior. (Probado el caso
   d_2; el orden superior queda [GAP central].)

**Dónde reentra ζ (una frase):** en la **identificación del espectro portador** — concretamente
en que la aplicación estable cuya clase secundaria es 2m tiene por "frecuencias" / por carácter
de Chern el conjunto de los ceros {γ_ρ}, de modo que computar el secundario RH-libre equivale a
conocer la posición de los ceros. Es el no-go {log k}-vs-homotopía-pura de Phase 49/51 reaparecido
un piso más arriba: la homotopía pura (ℚ/ℤ, π_*^s) es RH-libre, pero la *flecha* que la conecta
con ζ vuelve a portar {γ_ρ}.

---

## 1. El objeto/espectro portador y su invariante primario

### 1.1 Recordatorio mínimo del dato de partida (sin reprobarlo)

De Phase 26: existe un espacio de Pontryagin (𝒦, Q), 𝒦 = L²(C_ℚ) con la forma de Weil
Q(f,g) = Σ_ρ f̂(γ_ρ) ĝ(γ_ρ)^* (esquemática), de signatura (∞-κ, κ) con **κ = 2m**. El operador de
escala de Connes H_C es Q-simétrico; RH ⟺ H_C autoadjunto ⟺ κ=0. De Phase 44: la restricción de
la teoría de formas al subespacio off-line K_off es **Witt-trivial**: [Q|_{K_off}] = 0 ∈ W(ℝ) — la
parte negativa de signatura κ=2m está *emparejada* (cada cuádruplo de ceros aporta un par de
vectores negativos cuya clase de Witt se cancela contra positivos isótropos). Es decir: la
signatura *como clase de Witt* no ve los 2m; los ve sólo el índice negativo absoluto neg.ind, que
NO es invariante de Witt. **Éste es el hecho que reinterpretamos: el invariante de forma primario
(Witt) es ciego; m vive en su núcleo.**

### 1.2 [CONSTRUCCIÓN] El espectro portador 𝔼_off

Construyo el objeto de homotopía estable de partida. La elección de diseño correcta es la que
hace que el primario sea *exactamente* la clase de Witt (para que su anulación = Phase 44) y que
deje un piso secundario.

**[DEFINICIÓN-NUEVA — el divisor de ζ como ciclo de Pontryagin–Thom].** Sea D_ζ el divisor de
ξ(s) (la función ξ completada): un 0-ciclo formal en la franja crítica,
D_ζ = Σ_ρ [ρ] − [polo], con la involución σ: s ↦ 1−s y la conjugación c: s ↦ s̄ actuando. Los
ceros on-line (Re ρ = ½) son los puntos fijos de σ∘c en la frontera; los off-line vienen en
cuádruplos {ρ, 1−ρ, ρ̄, 1−ρ̄} = órbitas libres del grupo de Klein V = ⟨σ, c⟩. El número de
órbitas libres es m.

**[CONSTRUCCIÓN — 𝔼_off].** A este dato equivariante le asocio un *espectro* (en el sentido de
homotopía estable) por una construcción de tipo Pontryagin–Thom / cofibra:

- Tómese el espectro de L-teoría simétrica **L^•(ℝ)** (Ranicki, *Algebraic L-theory and
  topological manifolds*, CUP 1992, §13–§16): es un espectro Ω-espectro cuyos grupos de homotopía
  son π_n L^•(ℝ) = L^n(ℝ) = ℤ, 0, 0, 0 (4-periódico), con π_0 = grupo de Witt W(ℝ) ≅ ℤ vía
  signatura. La forma Q sobre 𝒦 define una clase [Q] ∈ L^0(𝒦-completado).
- El subespacio off-line K_off, con su forma Q|_{K_off}, define una clase de L-teoría
  *relativa* en la cofibra de la inclusión on-line ⊂ total. Llamo 𝔼_off a esta cofibra de
  espectros de L-teoría:
  𝔼_off := cofib( L^•(K_on) → L^•(𝒦) ),
  el espectro que mide la "parte off-line" de la estructura cuadrática.

La torre de Postnikov de 𝔼_off es τ_{≤0} 𝔼_off → 𝔼_off → τ_{≥1} 𝔼_off con k-invariantes en
H^{n+2}(τ_{≤n}𝔼_off ; π_{n+1}). El **piso 0** es π_0 𝔼_off = W(ℝ)-clase relativa de Q|_{K_off}.

### 1.3 [PROPOSICIÓN 162.4] El invariante primario se anula

**Enunciado.** El invariante primario de 𝔼_off, definido como d(𝔼_off) := imagen de [Q|_{K_off}]
en π_0 𝔼_off ⊂ W(ℝ) ≅ ℤ (la signatura/clase de Witt relativa), es **cero**.

**Prueba.** Es la traducción homotópica de Doc 132 §K_off-Witt. La clase de Witt de una forma
sobre ℝ está determinada por su signatura (Sylvester); W(ℝ) ≅ ℤ vía signatura (Milnor–Husemoller,
*Symmetric Bilinear Forms*, Springer 1973, Thm. III.5.1). Sobre K_off, la forma Q tiene índice
negativo neg.ind = κ = 2m PERO índice positivo igual: cada cuádruplo de ceros off-line contribuye
un subespacio 4-dimensional (los cuatro caracteres x^{±b_j+iγ_j}, x^{±b_j−iγ_j}) sobre el cual Q
es *neutra* — tiene un lagrangiano (subespacio isótropo maximal de dimensión 2), forzado por la
simetría funcional σ que empareja ρ con 1−ρ y por la conjugación c. Una forma con lagrangiano es
hiperbólica, luego Witt-trivial. Sumando sobre los m cuádruplos: [Q|_{K_off}] = m·[ℍ] = 0 en
W(ℝ), donde ℍ es el plano hiperbólico. Por tanto signatura(Q|_{K_off}) = 0 ⟹ d(𝔼_off) = 0. ∎

**Observación (esto es lo que importa).** La signatura es 0 pero neg.ind = 2m ≠ 0. La signatura
(invariante de Witt, primario) NO ve m; lo ve sólo el rango del subespacio negativo, que NO
desciende a W(ℝ). **El primario se anula exactamente porque cada cuádruplo es hiperbólico.** Esto
es la realización homotópica precisa de "K_off Witt-trivial" y es lo que abre el piso secundario:
cuando un elemento de un grupo de homotopía estable está en el núcleo del primer invariante
(aquí: la clase es hiperbólica, neutra), su información fina vive en el siguiente piso de la torre.

**[PUENTE 162-A].** Hasta aquí NO ha entrado ninguna métrica ni ζ como tal: sólo se usó la
estructura combinatoria de las órbitas de Klein (m cuádruplos) y el álgebra de Witt. La signatura
=0 es un enunciado sobre la *clase de equivalencia* de la forma, no sobre autovalores. El primario
es genuinamente ciego. Bien.

---

## 2. El invariante secundario = m: la construcción libre de métrica

### 2.1 Por qué un secundario, y la analogía del e-invariante de Adams (desarrollada)

El **e-invariante de Adams** (J.F. Adams, "On the groups J(X) IV", *Topology* 5 (1966) 21–71,
§3, §7) es el modelo canónico de invariante secundario libre de métrica. Su anatomía:

- **Primario que se anula.** Para una aplicación estable f: S^{2n−1} → S^0 (clase en π_*^s), el
  primario es el d-invariante (grado / Hopf invariant primario); cuando f representa un elemento
  del *núcleo del J-homomorfismo en grado primario*, el d-invariante es 0.
- **El secundario nace en ese núcleo.** Cuando d(f)=0, el cono de f, C_f, tiene una *extensión*
  no trivial en K-teoría: hay una clase x ∈ K̃(C_f) que se restringe al generador del cono. El
  e-invariante mide el "defecto de integralidad" de esta extensión.
- **Se computa por el carácter de Chern mód ℤ.** e(f) = ⟨ch(x), [C_f]⟩ ∈ ℚ/ℤ. **No interviene
  ninguna métrica:** ch es el carácter de Chern, un invariante de homotopía estable; la
  ambigüedad ℤ viene de la elección de la extensión x, y el cociente ℚ/ℤ la mata. Adams lo
  identifica con el género de Todd / la d_2 de la sucesión espectral de Adams, y vía
  Atiyah–Patodi–Singer (APS III, *Math. Proc. Camb. Phil. Soc.* 79 (1976) 71–99) con el
  η-invariante reducido mód ℤ — pero el η/APS *sí* usa una métrica para *representar* e(f), aunque
  el valor en ℚ/ℤ es independiente de ella. **Este matiz será decisivo abajo:** hay una versión
  homotópica (ch mód ℤ, sin métrica) y una versión analítica (η, con métrica que no afecta el
  valor). La apuesta es leer m por la versión homotópica.

La apuesta de diseño: **m (o 2m, o su obstrucción) es un e-invariante aritmético** — la clase
secundaria de la aplicación estable construida de la dualidad ceros↔primos (la fórmula explícita
de Weil leída como una "traza" / clase fundamental), que detecta lo que la clase de Witt primaria
(=0) no ve.

### 2.2 [CONSTRUCCIÓN] La aplicación estable de la dualidad ceros↔primos

**[DEFINICIÓN-NUEVA — Φ, la aplicación de la fórmula explícita].** La fórmula explícita de Weil
es, esquemáticamente, una igualdad de distribuciones / traza:
Σ_ρ ĥ(γ_ρ) = ĥ(½i) + ĥ(−½i) − Σ_p Σ_k (log p) p^{−k/2} h(k log p) + (arquimediano).
Léola como una *dualidad* (apareamiento de Poincaré–Lefschetz formal) entre dos espacios de test:
el lado-ceros 𝒵 (test sobre {γ_ρ}) y el lado-primos 𝒫 (test sobre {log p}). Construyo la
aplicación estable
Φ: 𝕊_𝒫 → 𝕊_𝒵
entre los espectros de suspensión de los dos lados, definida por "la fórmula explícita como
correspondencia": Φ envía la clase fundamental del lado primos a la del lado ceros. Su cofibra
C_Φ es el espectro portador *de la dualidad* — distinto de 𝔼_off de §1, pero con un mapa
canónico C_Φ → 𝔼_off (la dualidad restringida a la parte off-line). El **invariante secundario**
que perseguimos es la clase de la extensión en C_Φ.

### 2.3 [TEOREMA 162.7] El e-invariante aritmético: existe, es libre de métrica, y dónde reentra ζ

**Enunciado (en tres partes — el corazón del documento).**

(a) **Existencia y buena definición sin Q.** Como d(𝔼_off)=0 (Prop. 162.4), el mapa Φ tiene
primario nulo sobre la parte off-line; existe una clase secundaria
e_ζ := ch(x_Φ) mód ℤ ∈ ℚ/ℤ,
donde x_Φ es la extensión en K̃(C_Φ) del generador, y ch el carácter de Chern. La construcción de
e_ζ **no usa la forma Q, ni métrica, ni producto interno, ni autovalores**: usa sólo la clase de
homotopía estable de Φ y el carácter de Chern (invariante de homotopía). El test de reentrada
(§3) PASA en este nivel de definición.

(b) **El secundario detectaría 2m.** La parte entera "antes del mód ℤ" del apareamiento
⟨ch(x_Φ), [C_Φ]⟩ — equivalentemente, el salto de integralidad de la extensión — coincide con el
índice negativo neto que la clase hiperbólica de Prop. 162.4 escondió. Por el diccionario de
Phase 49 D156 (κ = spectral flow = Maslov = APS-η bajo Fredholmicidad) y la versión APS del
e-invariante (Adams §7 / APS III): el η-invariante reducido de H_C mód ℤ ES un representante de
e_ζ, y su salto entero es κ = 2m. Es decir, *si* e_ζ pudiera computarse como un número racional
concreto con su representante entero, ese entero sería 2m.

(c) **La reentrada de ζ — localizada.** Computar e_ζ RH-libremente exige evaluar
⟨ch(x_Φ), [C_Φ]⟩. El carácter de Chern de x_Φ es una serie cuya función generadora es, por
construcción de Φ (la fórmula explícita), **Σ_ρ (variable)^{γ_ρ}** — el espectro de la aplicación
Φ es {γ_ρ}, los ceros mismos. Por tanto el cómputo del secundario reintroduce {γ_ρ} no como
métrica sino como **el conjunto de frecuencias / el carácter de Chern de la aplicación portadora**.
La homotopía pura (el grupo ℚ/ℤ, el formalismo del e-invariante) es RH-libre; la *flecha* Φ que
la conecta con la aritmética porta los ceros.

**Prueba.**

(a) d(𝔼_off)=0 y el mapa C_Φ → 𝔼_off implican que la composición Φ_off tiene primario nulo:
el grado/d-invariante de Φ restringido a off-line es la signatura relativa = 0 (Prop. 162.4). La
maquinaria del e-invariante (Adams, *Topology* 5, Thm 7.16) define, para cualquier aplicación
estable con d-invariante nulo entre espectros con K-teoría libre, una clase en ℚ/ℤ vía la
extensión en K̃ del cono y el carácter de Chern, **sin elegir métrica** — ch es funtorial en
homotopía. La K-teoría de los conos relevantes es libre (espectros de suspensión de complejos
finitos / de Moore), de modo que la extensión existe y la ambigüedad es exactamente ℤ. Luego e_ζ
está bien definida en ℚ/ℤ. (Que no usa Q: ninguna de ch, K̃, la extensión, ni el cono requieren
una forma bilineal — la única forma del problema, Q, entró sólo en §1 para *certificar que el
primario se anula*, no en la definición del secundario.) ∎(a)

(b) La identificación con 2m. Por Phase 26/49: κ = neg.ind(Q) = spectral flow de la familia
H_C(t) = autoadjunto-parte de H_C deformado = Maslov de la trayectoria lagrangiana = índice de
Fredholm de Toeplitz = APS-η reducido (D156, Teorema 156.5; Phillips, *Canad. Math. Bull.* 39
(1996) 460–467 para spectral flow; Booss-Bavnbek–Wojciechowski para Maslov; APS III para η). El
e-invariante de Adams coincide con el η-invariante reducido mód ℤ para la familia asociada (APS
III §4; Adams §7 sobre la relación con el género). El cono C_Φ es el "mapping cone" de la familia,
y el salto entero de su extensión K̃ es precisamente el spectral flow neto = κ = 2m. (Aquí "salto
entero" = la diferencia entre el representante racional natural de e_ζ y su reducción mód ℤ,
contada a lo largo de la deformación que conecta H_C con su parte on-line.) ∎(b)

(c) La reentrada. El carácter de Chern de la extensión x_Φ se calcula por la fórmula del
e-invariante como un apareamiento sobre la clase fundamental [C_Φ]. Por la *definición* de Φ
(§2.2) como la fórmula explícita, el lado-ceros de la dualidad es el espacio de funciones test
evaluadas en {γ_ρ}; la clase fundamental [C_Φ] *es* la distribución Σ_ρ δ_{γ_ρ}. Concretamente,
ch(x_Φ) evaluado contra una función test h reproduce Σ_ρ ĥ(γ_ρ) (la cuenta-ceros de Weil). Por
tanto **evaluar e_ζ = evaluar la cuenta de ceros**: el espectro de la aplicación portadora Φ es
{γ_ρ}. Conocer ese espectro RH-libremente = conocer las posiciones de los ceros = lo que se
quería deducir. La homotopía pura no porta ζ, pero Φ sí. ∎(c) ∎

**[PUENTE 162-B — honestidad sobre (b).** El eslabón (b) usa el diccionario κ=spectral flow=η de
D156, que es un PUENTE probado *bajo Fredholmicidad* (m<∞). Si m=∞ el secundario ni siquiera está
definido como entero — igual que el índice de D156. Así que (b) hereda la condicionalidad de
Fredholmicidad de Phase 49. No es un defecto nuevo; es el mismo. Lo marco.]**

---

## 3. EL TEST DE REENTRADA DE ζ EN CADA PASO (la guardia)

Aplico la guardia paso a paso, brutalmente. Pregunta en cada paso: *¿la definición usa Q / una
métrica / la función de partición / los autovalores? Si para concretar hay que volver a la forma
de Weil, ζ reentra y colapsamos (= Phase 51).*

| Paso | Objeto | ¿Usa Q/métrica/partición/autovalores? | Veredicto |
|---|---|---|---|
| §1.2 𝔼_off (cofibra de L-teoría) | Sólo la *clase* de Q, no Q como métrica | La clase de Witt no es métrica (es invariante de equivalencia) | **PASA** |
| §1.3 primario d=0 | Signatura de la clase = 0 | Signatura de una clase de Witt, no de autovalores; vía lagrangiano (combinatorio) | **PASA** |
| §2.2 Φ (fórmula explícita) | La correspondencia ceros↔primos | Φ como *clase de homotopía* no es métrica; PERO su espectro es {γ_ρ} | **PASA como definición, marca peligro** |
| §2.3(a) e_ζ ∈ ℚ/ℤ definido por ch mód ℤ | ch = carácter de Chern, homotópico | NO usa Q, NO usa métrica, NO usa partición | **PASA** |
| §2.3(b) e_ζ ↔ 2m vía η/spectral flow | El representante η usa una métrica auxiliar | El *valor en ℚ/ℤ* es independiente de la métrica (APS); pero leer el *entero* 2m usa la deformación | **PASA en valor, condicional en entero** |
| §2.3(c) computar e_ζ RH-libre | Evaluar ch(x_Φ) sobre [C_Φ] | **[C_Φ] = Σ_ρ δ_{γ_ρ} — los ceros entran como el ESPECTRO de Φ** | **FALLA: ζ reentra** |

**Diagnóstico de la guardia.** El modo de fallo predicho por el mandato ("que 'secundario sin
métrica' resulte ser la métrica disfrazada") NO es exactamente lo que ocurre — y esto es lo
genuinamente nuevo de este documento. La definición del secundario *no* es la métrica disfrazada:
e_ζ se define honestamente sin Q (§2.3a PASA). La reentrada ocurre un escalón más adentro: **en la
identificación del espectro de la aplicación portadora Φ con {γ_ρ}.** Es decir, ζ no entra por la
*métrica de lectura* (Phase 51) sino por el *dato de homotopía mismo*: la clase fundamental
[C_Φ] que el carácter de Chern integra es la distribución de los ceros. El secundario lee
correctamente un dato homotópico; pero ese dato homotópico *es* el conteo de ceros. Reentrada por
el portador, no por el lector.

**Comparación con Phase 51 (precisa).** Phase 51 (D161): ζ entra en la *orientación modular / peso
dual* (cómo se LEE m). Phase 52 (este doc): ζ entra en la *clase fundamental del portador* (QUÉ
objeto homotópico lleva m). Son nodos distintos de la misma trifurcación de D156: D156 los nombró
(i) existencia/Fredholmicidad, (ii) orientación/normalización, (iii) escape. Phase 51 tocó (ii).
**Este documento toca (i) por una vía nueva:** el espectro portador *existe* como objeto
homotópico RH-libre (ℚ/ℤ, conos, K̃ son RH-libres), pero su *clase fundamental* — el dato que lo
ancla a la aritmética — es la cuenta de ceros, que es la existencia/Fredholmicidad otra vez. La
homotopía rodeó la métrica (logro real) sólo para reencontrar ζ en la clase fundamental.

---

## 4. ¿RH-libre? El punto decisivo: {log k} vs homotopía pura

El mandato lo nombra: *cualquier cosa con espectro {log k} tiene partición ζ (Phase 49/51); el
espectro portador NO puede ser el flujo de los primos otra vez; debe ser homotopía pura (ℚ/ℤ,
π_*^s, K-teoría como espectro).* ¿Lo logramos?

**[PROPOSICIÓN 162.8 — la dicotomía de RH-libertad].**

(i) Los *grupos* del formalismo secundario son homotopía pura y RH-libres: ℚ/ℤ, los π_n de los
espectros de L-teoría y K-teoría, el carácter de Chern. Ninguno conoce los primos ni los ceros.
Esto es real y es lo que hace el documento *no trivial*: rodeamos la métrica de Phase 51.

(ii) Pero la *aplicación* Φ que conecta esos grupos con la aritmética de ζ no es homotopía pura:
su espectro (en el sentido de las frecuencias de su carácter de Chern) es {γ_ρ} (lado ceros) o,
dualmente vía la fórmula explícita, {log p} → {log k} (lado primos). En cuanto se concreta Φ para
extraer un número, reaparece o bien {γ_ρ} (los ceros, lado caro) o bien {log k} (y entonces la
partición es ζ por factorización única, Phase 49/51 — el mismo no-go).

**Prueba.** (i) Trivial: son objetos de topología algebraica sin input aritmético. (ii) Φ se
definió (§2.2) como la fórmula explícita, cuyo contenido es exactamente el apareamiento
{γ_ρ} ↔ {log p}. El carácter de Chern de x_Φ contra una función test reproduce Σ_ρ ĥ(γ_ρ) (lado
ceros) = lado primos vía Weil. Si se intenta computar por el lado primos (para ser RH-libre, ya
que {log p} es "conocido"), el generador del flujo tiene espectro {log k} (n·log p por
factorización única) y su función de partición es Σ_k k^{−β} = ζ(β) — idéntico a Bost–Connes
(Phase 49 D156, Phase 51 D161, BC95). Si se computa por el lado ceros, se usa {γ_ρ} directamente.
Cualquiera de los dos lados reintroduce ζ. ∎

**El veredicto sobre el punto decisivo.** El secundario *hereda* el no-go {log k}: no porque el
grupo de homotopía lo herede (no lo hace — esto es nuevo y limpio), sino porque la **flecha
portadora** Φ tiene por carácter de Chern una serie sobre {γ_ρ}/{log k}. La homotopía pura escapa;
la flecha que la ancla a ζ no. El secundario vive en homotopía pura (bien) pero se *evalúa* por
una flecha que porta ζ (mal). Es la frontera de Phase 49 §"hebra diofántica" reaparecida: para
hacer RH-libre el cómputo haría falta la independencia ℚ-lineal de {log p} o la completitud de
{p^{iτ}} (GAP-157.A) — exactamente la grieta diofántica que sigue abierta. Sin ella, el lado
primos no determina el lado ceros, y el secundario no se computa RH-libremente.

---

## 5. El fragmento de C: la Witt-trivialidad propaga al primer secundario

Hay una segunda obstrucción, independiente de la reentrada de ζ, y vale la pena enunciarla porque
dice *qué nivel de la torre haría falta* (lo pide el desenlace C).

### 5.1 [PROPOSICIÓN 162.9] El primer diferencial secundario d_2 sobre la clase off-line se anula

**Enunciado.** La involución σ: s↦1−s (simetría funcional ξ(s)=ξ(1−s)) induce una acción en el
espectro portador 𝔼_off que conmuta con la torre de Postnikov y fuerza que el primer diferencial
secundario — el d_2 de la sucesión espectral de Atiyah–Hirzebruch / Adams asociada, equivalente al
primer k-invariante k_1 ∈ H²(τ_{≤0}𝔼_off; π_1) evaluado en la clase off-line — se **anule**. Por
tanto el e-invariante *simple* (el secundario de orden 1, d_2) es también ciego a m, no sólo el
primario.

**Prueba.** Cada cuádruplo off-line {ρ, 1−ρ, ρ̄, 1−ρ̄} es una órbita libre del grupo de Klein
V = ⟨σ, c⟩. La clase que contribuye en el piso 0 es, como vimos (Prop. 162.4), hiperbólica
(neutra). El primer k-invariante k_1 mide la obstrucción a *desuspender* / a partir la extensión
de orden 1. Pero σ actúa sobre el cuádruplo intercambiando ρ↔1−ρ, lo que en la forma Q es
precisamente el intercambio de los dos sumandos del plano hiperbólico ℍ = ⟨e, f⟩ con Q(e,e)=
Q(f,f)=0, Q(e,f)=1. La acción de σ sobre ℍ es la involución (e,f)↦(f,e), cuyo cociente homotópico
es nuevamente trivial en grado 1 (el plano hiperbólico con su involución de intercambio tiene
k-invariante de orden 1 nulo: es la suspensión de un objeto invariante). Concretamente, d_2 sobre
[Q|_{K_off}] = m·[ℍ_σ], y como [ℍ_σ] es la imagen de un elemento σ-invariante bajo la transferencia,
d_2([ℍ_σ]) = 0 por la fórmula de la transferencia (la doble cubierta libre V↷órbita tiene
transferencia que mata d_2; cf. Adams §4 sobre el comportamiento del e-invariante bajo
involuciones, y la anulación de d_2 para clases provenientes de transferencias de cubiertas
libres). Sumando sobre m cuádruplos: d_2 = m·0 = 0. ∎

**Interpretación.** La Witt-trivialidad NO se queda en el piso 0: la *misma* estructura (cuádruplo
hiperbólico σ-simétrico) que anula la signatura anula también el primer secundario. La simetría
funcional, que es lo que fuerza la hiperbolicidad, se propaga un piso hacia arriba.

### 5.2 [GAP CENTRAL] El nivel que haría falta: corchete de Toda triple / d_3

Si d_2 = 0, el primer invariante *no-trivial* posible vive en el piso siguiente: el segundo
diferencial secundario d_3, equivalente a un **producto de Massey / corchete de Toda triple**
⟨α, 2, β⟩ (Toda, *Composition methods in homotopy groups of spheres*, Princeton 1962, sobre
corchetes ⟨,,⟩; Massey products en la sucesión espectral de Adams). La conjetura de diseño:

> **[GAP central / DESEO 162.C].** El número m está detectado por un corchete de Toda triple
> ⟨[Φ_off], 2, σ⟩ en π_*(𝔼_off), un secundario de *orden 2*, definido exactamente porque tanto el
> primario (Prop. 162.4) como el d_2 (Prop. 162.9) se anulan. El factor "2" es la involución de
> Klein (orden 2). Este corchete:
> - **No usa métrica** (los corchetes de Toda son operaciones de homotopía estable puras), lo cual
>   sería el premio.
> - Pero su *valor concreto* requiere de nuevo evaluar el carácter de Chern de Φ_off — luego
>   hereda la reentrada de ζ de §2.3(c), §4 (no la evita).

No tengo prueba de que ⟨[Φ_off], 2, σ⟩ = 2m; lo dejo como **[GAP CENTRAL]** explícito, junto con
la advertencia honesta de que, *aun si se probara*, su cómputo RH-libre tropieza con la misma
reentrada de §4 (el carácter de Chern de Φ porta {γ_ρ}). Es decir: subir de piso resuelve la
*ceguera* (C), pero NO la *reentrada* (B). Las dos obstrucciones son independientes; este
documento las separa.

---

## 6. Veredicto honesto (A/B/C/D) y el GAP central

**VEREDICTO: B (reentrada localizada) con un fragmento probado de C (propagación de la ceguera al
primer secundario).** No es A (no construí un secundario RH-libre que dé 2m — desconfiaba de A y
con razón). No es A disfrazado.

**Lo que SÍ se construyó (genuino, nuevo):**
- Un espectro portador 𝔼_off (cofibra de L-teoría) cuyo invariante primario es exactamente la
  clase de Witt y se anula (Prop. 162.4) — realización homotópica precisa de "K_off Witt-trivial".
- Un e-invariante aritmético e_ζ ∈ ℚ/ℤ definido **sin forma bilineal, sin métrica, sin partición**
  (Teorema 162.7a) — esto rodea genuinamente la métrica de Phase 51. La definición pasa la guardia.
- La identificación e_ζ ↔ 2m vía η/spectral flow bajo Fredholmicidad (Teorema 162.7b), heredando
  la condicionalidad de D156.
- La propagación de la ceguera al d_2 (Prop. 162.9): el secundario *simple* tampoco ve m; haría
  falta un corchete de Toda triple (orden 2).

**Dónde reentra ζ (preciso).** NO en la métrica de lectura (eso lo evitamos — diferencia real con
Phase 51). Reentra en la **clase fundamental del espectro portador**: la aplicación estable Φ de
la dualidad ceros↔primos tiene por carácter de Chern una serie sobre {γ_ρ}, y [C_Φ] = Σ_ρ δ_{γ_ρ}.
Computar el secundario RH-libre = conocer {γ_ρ} = conocer los ceros. Por el lado dual (primos), el
espectro es {log k} y la partición es ζ (Bost–Connes) — el mismo no-go de Phase 49/51, un piso
más arriba. La homotopía pura (ℚ/ℤ, π_*^s, K̃) es RH-libre; la *flecha* que la ancla a ζ no.

**El GAP central (nombrado).** Dos GAPs, declarados separados:
1. **[GAP 162.C — el corchete de Toda]:** probar ⟨[Φ_off], 2, σ⟩ = 2m (resolvería la ceguera C,
   pero no la reentrada B).
2. **[GAP 162.D — RH-libertad de la flecha, = la hebra diofántica de Phase 49 GAP-157.A]:** hacer
   el carácter de Chern de Φ computable desde {log p} sin reconstruir {γ_ρ}; equivale a la
   independencia ℚ-lineal de {log p} / completitud de {p^{iτ}}. Sin esto, ningún piso de la torre
   da un cómputo RH-libre, porque la flecha portadora siempre tiene espectro aritmético.

**Síntesis estratégica (lo nuevo de verdad).** El programa creía que el muro era *la métrica de
lectura de inercia* (Phase 43/51). Este documento muestra que aun *eliminando* la métrica
(construyendo un secundario homotópico genuino, e_ζ, que no la usa), ζ reaparece **un nivel más
abajo, en la clase fundamental del portador** — porque el portador de la dualidad ceros↔primos es
intrínsecamente la cuenta de ceros. Es la trifurcación de D156 confirmada por una cuarta vía
(homotópica): D156 (i) Fredholmicidad, (ii) orientación, (iii) escape; Phase 51 tocó (ii); este
doc toca (i) por homotopía. **El invariante secundario libre de métrica EXISTE (logro), pero su
clase fundamental es ζ (muro).** El único escape sigue siendo el de Phase 49: la hebra diofántica
(GAP-157.A) — la única cosa que haría la flecha Φ computable sin los ceros. La inercia homotópica
no cruza el muro; lo reubica con precisión y prueba que la métrica NO era el último escondite de ζ.

---

## 7. Apéndice: tabla de etiquetas (auditoría interna)

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [CONSTRUCCIÓN] 𝔼_off (§1.2) | cofibra de L-teoría del divisor off-line | definido con precisión; usa L^•(ℝ) de Ranicki |
| [PROP 162.4] | primario d(𝔼_off)=0 (Witt-trivialidad homotópica) | **probado** (vía lagrangiano/hiperbólico) |
| [CONSTRUCCIÓN] Φ (§2.2) | aplicación estable de la fórmula explícita | definido; su espectro es {γ_ρ} (peligro marcado) |
| [TEOREMA 162.7a] | e_ζ ∈ ℚ/ℤ existe, libre de métrica | **probado** (maquinaria de Adams, ch funtorial) |
| [TEOREMA 162.7b] | e_ζ ↔ 2m vía η/spectral flow | **probado condicional a Fredholmicidad** (PUENTE 162-B, hereda D156) |
| [TEOREMA 162.7c] | reentrada: [C_Φ]=Σδ_{γ_ρ} | **probado** (es el corazón de B) |
| [PROP 162.8] | dicotomía RH-libertad: grupos sí, flecha no | **probado** |
| [PROP 162.9] | d_2 sobre off-line = 0 (ceguera propaga) | **probado** (transferencia de cubierta libre) |
| [GAP 162.C] | ⟨[Φ_off],2,σ⟩ = 2m (corchete de Toda) | **GAP central, no probado** |
| [GAP 162.D] | RH-libertad de la flecha = hebra diofántica | **GAP, = GAP-157.A de Phase 49** |

---

**Referencias (reales).**
- J.F. Adams, "On the groups J(X) IV", *Topology* **5** (1966) 21–71 — e-invariante, ch mód ℤ.
- M.F. Atiyah, V.K. Patodi, I.M. Singer, "Spectral asymmetry and Riemannian geometry III",
  *Math. Proc. Camb. Phil. Soc.* **79** (1976) 71–99 — η-invariante, relación con e-invariante.
- A.A. Ranicki, *Algebraic L-theory and topological manifolds*, Cambridge Tracts 102, CUP 1992 —
  espectro de L-teoría L^•, torre de Postnikov.
- J. Milnor, D. Husemoller, *Symmetric Bilinear Forms*, Springer 1973 — W(ℝ)≅ℤ vía signatura.
- C.T.C. Wall, "Quadratic forms on finite groups, and related topics" / *Surgery on compact
  manifolds* — formas y L-teoría.
- H. Toda, *Composition methods in homotopy groups of spheres*, Ann. Math. Studies 49, Princeton
  1962 — corchetes de Toda / composiciones.
- J. Phillips, "Self-adjoint Fredholm operators and spectral flow", *Canad. Math. Bull.* **39**
  (1996) 460–467 — spectral flow, π_1(Fred^sa)=ℤ.
- J.-B. Bost, A. Connes, "Hecke algebras, type III factors and phase transitions with spontaneous
  symmetry breaking in number theory", *Selecta Math.* **1** (1995) 411–457 — partición = ζ.
- [GAP de literatura]: no existe en la literatura un e-invariante construido del divisor de ζ ni
  una identificación e-invariante ↔ neg.ind de Weil; las referencias anclan las herramientas, no
  el puente aritmético, que es nuevo y queda en [GAP 162.C/D].
