# Doc 116 — Auditoría adversarial del Teorema 5.2 de Doc 113 (no-casi-periodicidad de Stepanov de ζ en la franja)

**Programa:** Hipótesis de Riemann — Phase 38, auditoría final
**Fecha:** junio 2026
**Auditor:** rol adversarial — el mandato es DESTRUIR el teorema, no confirmarlo
**Objetivo:** Doc 113 (phase-37-physics/113-LP112-contra-literatura.md), §5.2, Teorema 5.2:
*"ζ no es S^p-casi-periódica en ninguna sub-banda de la franja crítica, para ningún p ≥ 1 — incondicional"* — citado en P44 como Theorem 4.2 (main.tex, líneas 282–288).
**Naturaleza:** auditoría de definiciones, de la prueba paso a paso, de las referencias externas (verificadas en fuente en esta sesión vía web) y del uso en P44. Sin numéricos. Honestidad absoluta: se reporta lo que sobrevive y lo que no, con localización exacta.

---

## 0. Resumen ejecutivo del ataque

Se ejecutaron las cuatro líneas de ataque obligatorias más tres adicionales. Resultado
anticipado (detalle en §§1–6, veredicto formal en §7):

- **El teorema, TAL COMO ESTÁ ENUNCIADO EN DOC 113, sobrevive intacto.** La razón
  central es que Doc 113 enuncia y prueba la versión **de banda (vectorial)**: la
  norma de Stepanov que el teorema declara infinita es explícitamente
  ‖ζ‖_{S^p(B)}^p = sup_x ∫_x^{x+1} ∫_{σ₁}^{σ₂} |ζ(σ+it)|^p dσ dt (§5.2 del doc, la
  fórmula precede al teorema). Con esa norma, el paso "subarmonicidad 2D → ventana
  1D" que el encargo señalaba como lugar más probable del error **no existe**: el
  disco de la desigualdad submedia se compara directamente con el rectángulo
  banda × ventana, sin Fubini y sin ningún σ′ móvil. La fuga del σ móvil — real —
  solo aparece en la versión de recta fija, que **Doc 113 explícitamente NO afirma**
  y declara como gap abierto (§5.2, párrafo final: "Sobre la versión de recta
  única... no se sigue del Teorema 5.2... GAP menor, abierto").
- **Las referencias Ω se verificaron en fuente y sobran.** Aistleitner (Math. Ann.
  365 (2016), arXiv:1409.6035, abstract verificado en esta sesión): para α ∈ (½,1)
  FIJO, incondicionalmente, max_{0≤t≤T}|ζ(α+it)| ≥ exp(c_α(log T)^{1−α}/(log log T)^α),
  c_α = 0.18(2α−1)^{1−α} — exactamente lo que Doc 113 cita, verbatim. Además el
  insumo real de la prueba es muchísimo más débil: basta CUALQUIER no-acotación de
  ζ en una recta interior de la banda, y eso es Titchmarsh incondicional con
  Ω(exp((log t)^{1−σ−ε})) (Cap. VIII), verificado vía fuente secundaria.
- **El único hallazgo accionable es de redacción, y está en P44, no en Doc 113:**
  el enunciado de P44 Theorem 4.2 ("ζ is not Stepanov almost-periodic (S^p, any
  p≥1) on any sub-strip") no especifica el sentido (banda/vectorial vs. recta a
  recta) y admite la lectura fuerte no probada. Corrección exacta en §6.

**VEREDICTO: SOBREVIVE INTACTO (Doc 113, Thm 5.2). P44 Theorem 4.2: SOBREVIVE CON
UNA CORRECCIÓN de precisión de enunciado (una cláusula).**

---

## 1. Ataque 1 — Definiciones: ¿qué es S^p-c.p. para una función de dos variables, y la prueba usa la definición que enuncia?

### 1.1. La definición que Doc 113 usa

Doc 113 §5.1 da la norma de Stepanov escalar clásica
‖f‖_{S^p}^p = sup_x ∫_x^{x+1}|f|^p, con f S^p-c.p. si es límite en esa norma de
polinomios trigonométricos (equivalentemente: casi-períodos relativamente densos en
esa norma). Esto coincide con la definición clásica (Besicovitch 1932, Cap. II;
Levitan–Zhikov): las dos formulaciones (clausura de polinomios / casi-períodos
relativamente densos à la Bohr en norma S^p) son equivalentes para Stepanov — la
equivalencia es teoría estándar y no la cuestionamos.

Para la función de dos variables, Doc 113 §5.2 hace exactamente lo que el encargo
exigía verificar: **declara la forma del enunciado antes de probarlo**. Cito la
estructura: "la versión útil es la de banda: para una banda cerrada
B = [σ₁,σ₂] ⊂ (½,1), considérese ζ como función t ↦ ζ(·+it) ∈ L²(B) y la norma de
Stepanov vectorial ‖ζ‖_{S²(B)}² := sup_x ∫_x^{x+1}∫_{σ₁}^{σ₂}|ζ(σ+it)|² dσ dt."
Es decir: ζ se trata como función de UNA variable real t con valores en el espacio
de Banach L^p(σ₁,σ₂), y la norma de Stepanov vectorial es la clásica con |f(t)|
reemplazado por ‖ζ(·+it)‖_{L^p(B)}. Para p general la fórmula es la integral doble
de |ζ|^p — consistente con lo que la prueba usa. La definición es precisa, es la
estándar de la teoría vectorial de casi-periodicidad (Levitan–Zhikov, funciones
c.p. con valores en Banach), y **la prueba usa exactamente esa norma**: no hay
deslizamiento definicional entre enunciado y demostración. Primer punto de ataque:
fallido.

### 1.2. ¿"S^p-c.p. ⟹ S^p-acotada" (Lema 5.1) es teorema verdadero?

Sí, bajo ambas definiciones, y lo verificamos por las dos vías:

- **Vía clausura (la que el doc usa):** si f es límite S^p de polinomios
  trigonométricos, entonces ‖f‖_{S^p} ≤ ‖f−P‖_{S^p} + ‖P‖_{S^p} < ε + ‖P‖_{S^p},
  y un polinomio trigonométrico (escalar o con coeficientes en L^p(B)) es una
  función acotada de t, luego de norma S^p finita. La acotación obtenida es
  **acotación de la norma S^p** (‖f‖_{S^p} < ∞), NO acotación puntual — y esto es
  exactamente lo que el doc usa después. El encargo advertía contra la confusión
  S^p-acotado / puntualmente acotado: la confusión no está en el doc. El límite S^p
  de funciones acotadas puede ser puntualmente no acotado, correcto — pero su norma
  S^p es finita por convergencia, que es lo único que el Teorema 5.2 contradice.
- **Vía casi-períodos (definición alternativa), por completitud adversarial:** si f
  ∈ L^p_loc tiene casi-períodos S^p relativamente densos, tomemos ε = 1 y L tal que
  todo intervalo de longitud L contiene un 1-casi-período. Dado x, hay τ ∈ [x−L, x]
  casi-período... más precisamente: τ casi-período en [x, x+L] da, con y = x−τ ∈
  [−L,0], que ‖f‖_{L^p(x,x+1)} ≤ 1 + ‖f‖_{L^p(y,y+1)} ≤ 1 + sup_{y∈[−L,1]}
  ‖f‖_{L^p(y,y+1)} < ∞ por integrabilidad local (ζ es continua en la banda cerrada,
  luego localmente acotada — el requisito se cumple). Misma conclusión.

El Lema 5.1 es, como el doc dice, esencialmente definicional. Segundo punto de
ataque: fallido.

### 1.3. Subarmonicidad: dirección de la desigualdad y validez para |ζ|^p

- |g|^p es subarmónica para g holomorfa y todo p > 0 (log|g| subarmónica y
  composición con exp(p·), convexa creciente). El teorema pide p ≥ 1 solo para que
  S^p sea la clase clásica con norma; la subarmonicidad no es la restricción. ✓
- La desigualdad submedia se usa en la dirección correcta: u(centro) ≤ media en el
  disco, es decir media ≥ V_n^p. El doc escribe V_n^p ≤ (1/πr²)∬_{D(σ+it_n,r)}|ζ|^p dA.
  ✓ No hay inversión de desigualdad.

---

## 2. Ataque 2 — El corazón: el paso 2D→1D y la fuga del σ móvil

### 2.1. Reconstrucción exacta de la prueba

Datos: B = [σ₁,σ₂] ⊂ (½,1), σ ∈ (σ₁,σ₂) fijo, r = min(σ−σ₁, σ₂−σ, ¼)/2 > 0.
Aistleitner/Titchmarsh dan t_n → ∞ con V_n := |ζ(σ+it_n)| → ∞ (sobre la extracción
de la sucesión, ver §3.2). Cadena:

1. **Submedia:** V_n^p ≤ (1/πr²) ∬_{D(σ+it_n, r)} |ζ|^p dA.
2. **Inclusión geométrica:** D(σ+it_n, r) ⊂ [σ₁,σ₂] × [t_n−r, t_n+r], porque
   r ≤ (σ−σ₁)/2 y r ≤ (σ₂−σ)/2. ✓ El integrando es ≥ 0, luego la integral en el
   disco ≤ la integral en el rectángulo. ✓
3. **La ventana cabe:** r ≤ ⅛ < ½, así que [t_n−r, t_n+r] ⊂ [x_n, x_n+1] con
   x_n = t_n − r. ✓
4. **Conclusión:** ∫_{x_n}^{x_n+1}∫_{σ₁}^{σ₂}|ζ|^p dσ dt ≥ πr² V_n^p → ∞, luego
   ‖ζ‖_{S^p(B)}^p = sup_x (…) = ∞. Con el Lema 5.1 (contrapuesto): ζ no es
   S^p(B)-c.p. ∎

### 2.2. ¿Dónde está el Fubini, dónde el σ′ móvil?

**En ninguna parte.** Este era el ataque principal del encargo, y la respuesta de la
auditoría es categórica: la prueba NUNCA convierte la media 2D en una media 1D a σ
fijo. La cantidad que el teorema declara infinita ES la media 2D en
banda × ventana-unitaria (la norma vectorial S^p(B)). El paso 2 de arriba es una
inclusión de dominios con integrando positivo — monótono, trivial, sin pérdida. No
hay selección de σ′ dependiente de n, no hay problema de acumulación de σ′_k, no
hay necesidad de uniformidad en σ. La arquitectura de la prueba está diseñada
exactamente para esquivar la fuga: la norma de banda absorbe el carácter
bidimensional de la información subarmónica.

La fuga del σ móvil es REAL — pero solo si uno quisiera concluir algo sobre la
norma S^p escalar de t ↦ ζ(σ₀+it) en una recta fija σ₀: ahí "punto grande en
(σ,t_n)" + submedia solo da "ALGÚN σ′′ (dependiente de n) tiene media 1D grande", y
no se puede fijar σ′′. ¿Comete Doc 113 ese paso? **No.** El párrafo final de §5.2
lo declara explícitamente: "si ζ(σ+i·) es S²-acotada en UNA recta fija no se sigue
del Teorema 5.2 (la subarmonicidad reparte la masa en un entorno bidimensional, no
en la recta misma)… Estado declarado: GAP menor, abierto — e irrelevante para
LP-112". El documento no solo no comete el error: lo nombra, lo localiza y lo
descarta como irrelevante para su uso (Rouché necesita control de área, la banda).
Honestidad verificada en el punto más delicado.

### 2.3. Conclusión del ataque al corazón

De las tres opciones del encargo — (a) vale a σ fijo, (b) vale solo en versión
banda/vectorial, (c) no vale — la respuesta es **(b), y (b) es exactamente lo que
Doc 113 enuncia y prueba**. La versión (a) (recta fija) queda genuinamente abierta:
no la prueba el argumento, no la afirma el doc, y esta auditoría tampoco encontró
una vía barata para probarla (la convexidad logarítmica tipo Hardy de
σ ↦ ∫|ζ(σ+it)|^p dt vale para integrales sobre toda la recta, no sobre ventanas; y
no hay desigualdad submedia 1D para |hol|^p sobre segmentos verticales). La versión
(c) está refutada por esta auditoría: la prueba de (b) es correcta.

---

## 3. Ataque 3 — Los Ω-teoremas: enunciados, conditionalidad, suficiencia

### 3.1. Verificación en fuente (esta sesión)

- **Aistleitner, arXiv:1409.6035 / Math. Ann. 365 (2016)** — verificado el abstract
  en arXiv: para α ∈ (½,1) fijo, **incondicional**, para todo T grande:
  max_{0≤t≤T}|ζ(α+it)| ≥ exp(c_α(log T)^{1−α}/(log log T)^α), con
  c_α = 0.18(2α−1)^{1−α}, por método de resonancia (resonadores largos). La cita de
  Doc 113 es verbatim correcta, incluida la atribución del precedente: el paper
  dice que "el mismo resultado ya fue obtenido por Montgomery, con menor valor de
  c_α".
- **Montgomery 1977 (Comment. Math. Helv. 52):** Doc 113 lo cita "[vía Aistleitner,
  original NO VERIFICADO]" — etiqueta honesta. Matiz que la auditoría agrega: en la
  literatura el resultado de Montgomery con denominador (log log T)^σ aparece a
  veces como condicional a RH, con la versión incondicional de esa época en forma
  más débil (Levinson: (log T)^{1−σ}/log log T, incondicional — verificado vía
  fuente secundaria, survey de Ω-teoremas cerca de Re s = 1, arXiv:1706.07364 y
  hal-01425575). **Esto es irrelevante para la validez del teorema** porque la
  referencia load-bearing es Aistleitner (incondicional, verificado), pero como
  higiene de citas conviene no apoyar la palabra "incondicional" en Montgomery
  (ver §6, corrección menor opcional).
- **Titchmarsh, Cap. VIII (§8.12):** verificado vía fuentes secundarias: para
  0 < σ < 1 fijo y todo ε > 0, |ζ(σ+it)| = Ω(exp((log t)^{1−σ−ε})), incondicional.
  Más que suficiente como respaldo independiente.

### 3.2. ¿El insumo Ω alcanza para reventar la norma S^p? Sí — y está sobredeterminado

El punto fino del encargo: el Ω-valor vive en un punto; ¿la prueba necesita que la
media local sea no acotada? Respuesta: la prueba necesita exactamente
V_n = |ζ(σ+it_n)| → ∞ con t_n → ∞, y la subarmonicidad + inclusión de dominios hace
todo el resto (§2.1). Para extraer la sucesión: los resultados son de tipo
max_{0≤t≤T} ≥ Φ(T) → ∞ (Aistleitner) o limsup (Titchmarsh, Ω directo). En el caso
max: los maximizadores t_T no pueden quedarse en un compacto (ζ es continua, luego
acotada, en [σ₁,σ₂] × [0,K] para todo K), así que t_n → ∞ a lo largo de una
subsucesión. ✓ Sin gap.

Más aún — y esto blinda el teorema contra cualquier disputa de citas: **el
crecimiento cuantitativo es irrelevante**. El Teorema 5.2 solo necesita que ζ sea
NO ACOTADA en una recta interior de cada sub-banda. La tasa exp(c(log T)^{1−σ}…)
es lujo; la mera no-acotación (clásica, incondicional, por múltiples vías:
Titchmarsh con cualquier ε, o incluso universalidad de Voronin, que produce valores
arbitrariamente grandes en discos de la franja) ya da V_n → ∞. La S^p-c.p. implica
una COTA FIJA finita de la norma (‖ζ‖_{S^p(B)} = C < ∞); cualquier sucesión
V_n → ∞ la contradice vía πr²V_n^p ≤ C^p. No se necesita que el crecimiento "le
gane" a nada: se necesita que sea no acotado. Tercer punto de ataque: fallido, con
margen amplio.

---

## 4. Ataque 4 — ¿Contradice algo conocido? Búsqueda de literatura en contra

- **Sanity check σ > 1:** ζ es Bohr-c.p. uniforme en σ ≥ 1+ε (Bohr 1918,
  convergencia absoluta) ⟹ S^p-c.p. allí (uniforme ⟹ Stepanov, jerarquía clásica
  Bohr ⊂ S^p ⊂ W^p ⊂ B^p). El Teorema 5.2 se restringe a sub-bandas de (½,1):
  consistente, sin colisión. ✓
- **¿Alguien afirma S-casi-periodicidad de ζ en la franja?** Búsquedas en esta
  sesión ("Stepanov almost periodic Riemann zeta function critical strip" y
  variantes; revisión del survey reciente de procesos casi-periódicos con
  aplicaciones a teoría de números, arXiv:2502.04969, que trabaja en B² y NO trata
  ζ en la franja en sentido Stepanov): **ningún resultado pertinente**. Lo clásico
  para ζ en ½ < σ < 1 es casi-periodicidad de Besicovitch B^p (medias sobre
  intervalos crecientes — compatible con el Teorema 5.2: B^p no controla ventanas
  fijas) y la noción local-compacta de Bohr 1922 (RH-equivalente, Doc 113 §2.1).
  Sobre Besicovitch mismo: su teoría aplicada a ζ en la franja es B² (es el
  contenido del Lema 2.1 de D112, vía valor medio cuadrático); no encontramos
  ninguna afirmación suya de tipo Stepanov en la franja. **No hay literatura que el
  teorema contradiga.** Y la dirección del teorema es la esperable: la norma de
  Stepanov es la más fuerte de las normas de media (S^p ⊃ ventanas fijas) y es
  natural que el crecimiento la mate, igual que mata a Bohr uniforme (ζ no acotada
  en ninguna recta σ ≤ 1).
- **Consistencia interna del programa:** el Teorema 5.2 es coherente con la tabla
  de seminormas de Doc 113 §5.4 y con D112 (B² sobrevive porque sus ventanas
  crecen; Weyl anula compactos — el argumento de §5.3 del doc, sup antes del
  límite, es correcto: para f·1_K la media en ventanas de largo L decae como 1/L
  uniformemente en x). Cuarto punto de ataque: fallido.

---

## 5. Ataques adicionales del auditor (no pedidos, ejecutados igual)

1. **"No-c.p. por no pertenencia al espacio":** el Teorema 5.2 prueba algo más
   fuerte que "no c.p.": prueba ‖ζ‖_{S^p(B)} = ∞, o sea ζ ni siquiera pertenece al
   espacio S^p(B) donde la c.p. se define. ¿Hace esto al enunciado "trivialmente
   verdadero pero engañoso"? No: es exactamente la forma útil (Corolario 5.3 del
   doc necesita la falsedad de la premisa "ζ ∈ S²(B)-c.p.", y la no-pertenencia la
   da con creces). Pero el enunciado en prosa "ζ no es S^p-casi-periódica" es la
   consecuencia correcta y no sobreafirma.
2. **Medibilidad/valores vectoriales:** t ↦ ζ(·+it) ∈ L^p(B) es continua (ζ
   uniformemente continua en B × compactos), así que todas las integrales tienen
   sentido y la teoría vectorial aplica. Sin gap.
3. **¿El sup_x se alcanza/diverge legítimamente?** El sup sobre x de una familia de
   integrales locales finitas (cada ventana da integral finita: ζ continua) puede
   ser ∞ sin contradicción; la prueba exhibe la divergencia a lo largo de x_n. Sin
   gap.
4. **Borde de la banda:** σ se toma en el INTERIOR (σ₁,σ₂) y r se calibra con la
   distancia a ambos bordes; el caso degenerado σ₁ = σ₂ (recta, no banda) está
   excluido por hipótesis (σ₁ < σ₂ en el enunciado). Sin gap.
5. **Uso del teorema dentro de Doc 113 (Cor. 5.3 y tabla §5.4):** la implicación
   "S²-banda-c.p. ⟹ LP-112" se usa solo como motivación (queda vacua); la fila de
   la tabla "Stepanov S^p, banda — NO (Teorema 5.2)" dice "banda" explícitamente.
   El propio Doc 113 §5.4 y el resumen ejecutivo (punto 5) hablan de "ζ no es
   S^p-casi-periódica en ninguna sub-banda" — lectura natural: como función en la
   banda. Consistente.

---

## 6. El uso en P44: la única corrección que esta auditoría exige

P44 (06-papers/P44-two-lemma-architecture/main.tex, Theorem 4.2 = \thm:stepanov,
líneas 282–288) enuncia:

> "ζ is not Stepanov almost-periodic (S^p, any p≥1) on any sub-strip of the open
> critical strip: Stepanov almost-periodicity implies Stepanov boundedness, which
> the unconditional Ω-theorems for large values of ζ (with subharmonicity) violate."

Dos lecturas posibles de "Stepanov almost-periodic on a sub-strip":

- **(i) Lectura de banda (vectorial):** ζ como función L^p(σ₁,σ₂)-valuada de t, con
  la norma S^p(B) de Doc 113. PROBADA.
- **(ii) Lectura recta-a-recta:** para cada (o algún) σ fijo en la sub-banda,
  t ↦ ζ(σ+it) es S^p-c.p. escalar. NO PROBADA — abierta, declarada como gap en
  Doc 113 §5.2.

La lectura (i) es la natural ("almost periodic on a region" en la tradición de
Bohr para funciones holomorfas en bandas es una noción de la función en la región)
y es la que Doc 113 (la fuente citada) define con fórmula. Pero un árbitro hostil
puede leer (ii). **Corrección exacta recomendada** — reemplazar el enunciado del
Theorem 4.2 por:

> "ζ is not Stepanov almost-periodic ($S^p$, any $p\geq 1$) on any sub-strip
> $[\sigma_1,\sigma_2]\subset(\tfrac12,1)$ **in the band sense**: the vectorial
> Stepanov norm $\sup_x \int_x^{x+1}\!\int_{\sigma_1}^{\sigma_2}|\zeta(\sigma+it)|^p\,
> d\sigma\,dt$ is infinite, hence ζ, viewed as an $L^p(\sigma_1,\sigma_2)$-valued
> function of $t$, is not $S^p$-almost-periodic. (The fixed-line scalar version is
> not claimed and remains open.) Stepanov almost-periodicity implies finiteness of
> the Stepanov norm, which the unconditional Ω-theorems for large values of ζ
> (Titchmarsh; Aistleitner 2016), promoted by subharmonicity of $|\zeta|^p$ to
> unit-window area integrals, violate."

Correcciones menores opcionales (higiene, no validez):

- En Doc 113 y P44, no apoyar "incondicional" en Montgomery 1977 (cuya versión con
  (log log T)^σ aparece en la literatura asociada a RH, con Levinson como la
  versión incondicional coetánea más débil); la referencia incondicional
  load-bearing es Aistleitner 2016 (verificada) y, como respaldo mínimo suficiente,
  Titchmarsh Cap. VIII. Doc 113 ya marca Montgomery "[original NO VERIFICADO]";
  basta degradarlo a precedente histórico sin la palabra incondicional adosada.
- El abstract de P44 (líneas 68–73) repite la frase sin la precisión de banda;
  añadir "in the band (vector-valued) sense" o equivalente.

---

## 7. VEREDICTO

**SOBREVIVE INTACTO — Doc 113, Teorema 5.2, tal como está enunciado.**

1. La definición es precisa (norma de Stepanov vectorial de banda, dada con fórmula
   antes del teorema), la prueba usa esa misma definición, y el Lema 5.1
   (c.p. ⟹ norma finita) es correcto bajo las dos definiciones estándar de
   S^p-c.p. La prueba usa acotación de la NORMA, nunca acotación puntual.
2. El paso señalado como lugar más probable del error — subarmonicidad 2D → ventana
   1D — **no existe en la prueba**: la norma atacada es 2D (banda × ventana
   unitaria) y la submedia se compara por inclusión monótona de dominios. La fuga
   del σ móvil solo afectaría la versión de recta fija, que el documento no afirma
   y declara abierta explícitamente. De las opciones (a) σ fijo / (b) banda-
   vectorial / (c) nada: **vale (b), y (b) es lo enunciado**. (a) queda
   genuinamente abierta; (c) queda refutada por esta auditoría.
3. Los Ω-teoremas citados se verificaron en fuente (Aistleitner 2016: incondicional,
   σ fijo en (½,1), enunciado verbatim correcto; Titchmarsh Cap. VIII como respaldo
   incondicional independiente), y el insumo que la prueba realmente necesita —
   no-acotación de ζ en una recta interior — está sobredeterminado por un orden de
   magnitud. Único matiz: la conditionalidad histórica de Montgomery 1977, no
   load-bearing.
4. No existe literatura que afirme S-casi-periodicidad de ζ en la franja (búsqueda
   ejecutada); lo clásico (B² de Besicovitch, noción local-compacta de Bohr) es
   compatible y la posición del teorema en la jerarquía Bohr ⊃ S^p ⊃ W^p ⊃ B^p es
   la esperable. El teorema no contradice nada conocido.
5. **P44 Theorem 4.2: SOBREVIVE CON UNA CORRECCIÓN** de redacción (cláusula "in the
   band/vector-valued sense" + nota de que la versión de recta fija queda abierta;
   texto exacto en §6). Sin esa cláusula, el enunciado de P44 admite una lectura
   (recta-a-recta) estrictamente más fuerte que lo probado.

El teorema es, además, robusto: no depende de la tasa de crecimiento (cualquier
no-acotación en una recta interior basta), no depende de p (todo p > 0 con la
misma prueba; p ≥ 1 solo normaliza la clase), y no depende de la sub-banda (el
radio r se calibra localmente). Es uno de los enunciados mejor blindados del
programa, y su honestidad interna (el gap de recta única declarado en el propio
§5.2) le ahorró el único error que esta auditoría podía encontrarle.

---

## Referencias de la auditoría

- Doc 113, §5.1–5.4 (objetivo); D112 (Lemas 2.1–2.2, Obs. 2.4, Prop. 2.6 — contexto).
- P44, main.tex, abstract (l. 68–73), Theorem 4.2 (l. 282–288), honest assessment (l. 365).
- C. Aistleitner, *Lower bounds for the maximum of the Riemann zeta function along
  vertical lines*, Math. Ann. 365 (2016); arXiv:1409.6035. [VERIFICADO en esta
  sesión: abstract; enunciado, incondicionalidad, constante c_α = 0.18(2α−1)^{1−α}.]
- H. L. Montgomery, *Extreme values of the Riemann zeta function*, Comment. Math.
  Helv. 52 (1977). [Vía Aistleitner; conditionalidad histórica señalada como matiz
  de higiene, no load-bearing.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Cap. VIII
  (Ω-teoremas, incondicionales, σ fijo). [Verificado vía fuentes secundarias en esta
  sesión: |ζ(σ+it)| = Ω(exp((log t)^{1−σ−ε})), con las mejoras de Levinson y
  Montgomery; survey arXiv:1706.07364, hal-01425575.]
- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge, 1932, Cap. II (clases
  S^p, W^p, B^p; c.p. ⟹ acotación en la norma respectiva). B. M. Levitan,
  V. V. Zhikov, *Almost Periodic Functions and Differential Equations* (versión
  vectorial/Banach). [Teoría estándar; equivalencia de definiciones y Lema 5.1
  re-derivados independientemente en §1.2.]
- Búsqueda negativa de literatura "Stepanov almost periodic zeta": sin resultados
  pertinentes (sesión de junio 2026; incluye revisión de arXiv:2502.04969, que
  trabaja en B² y no toca Stepanov-ζ en la franja).

*Fin del Documento 116.*
