# ROUND_003_4 — Selección: coordenada de borde y ancla nula con borde dentro de (G)

Memo de selección, no de construcción. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

### Búsqueda realizada

- Lectura primaria entera: R170_861, 862, 866, 868, 869, 870; inicio y estado de 859, 867, 874;
  R182_201 entero y README de la fase 182; `REVIEW_002_A.md`, `REVIEW_002_BC.md`, `LEDGER.md`,
  `RULES_AVOID.md` §§B, D, I.
- grep en `03-research/` (todas las fases), `04-papers/47*`, `04-papers/48*` y
  `05-meta-and-planning/` por: «null anchor», «bordered null», «boundary anchor», «boundary
  coordinate», «β_T(f)», «ancla nula», «ancla con borde», «coordenada de borde», «complemento de
  Schur» / «Schur complement» junto a a_T o P_T, «NGF», «invisib» junto a núcleo/kernel.
- Coincidencias abiertas en primaria: fase 170 (862–874), fase 182 (`R182_RECTANGULAR_TUNNEL.md`,
  `R182_201_AUDIT_AND_NONLOCAL_GATE.md`), R179_CHAIN_GATE l. 252 (sólo cita 866). En la 211,
  `ROUND_008_A.md` l. 26 y `ROUND_008_D.md` l. 18 citan «POLAR_CAP_001 (bordered Schur complement
  that inverts a_T|P_T itself — consumes λ_A > 0)»; no hay archivo con ese nombre en la carpeta de la
  211 (búsqueda por nombre sin resultado), de modo que sólo se conoce por esas dos citas.
  P47 l. 4340–4350 (complemento de Schur con borde de a_T sobre P_T, término polar) y l. 5299
  (thm:coer-schur): leídos sólo en las líneas citadas.
- Las demás coincidencias textuales («boundary coordinates» en P121, P3 de la fase 120, fases 57,
  72, 77, 78, 114/116) usan «borde» en otro sentido (coordenadas de Hadamard, borde de Weyl,
  fronteras de capacidad); no se abrieron enteras. No encontré ninguna memo que escriba una forma
  positiva con el vector nulo (Λ,1)⊗F ⊕ β_T(F) sobre todo P_T. Eso no prueba novedad: la §2 muestra
  que el formato no la tiene.

### (1) Antecedente más cercano

- R170_862 §§2–6: ley del ancla nula con borde. Lema 2.1 (familia bilateral positiva ⟹
  P_N Ḣ P_N = 0); §3 (un ancla fuera del núcleo no recibe la cancelación, modelo (3.2)); §4 las
  cuatro obligaciones de e_T; §5 la columna de Tate tiene ‖b‖² = 4(sinh T + εT) > 0.
- R170_868 §5: vector nulo ampliado ê_T(f) = ((Λ,1)⊗f, β_T(f)) con cancelación conjunta (5.4);
  §6: β_T(f) se construye con (ρ_f, ℓ_f) de la ecuación de primer contacto PAf = ρ_f b, Q_eAf = ℓ_f.
- R170_869 (0.2)–(0.4) y R170_870 §§2, 4: la clase de borde es lineal e impar; es independiente de
  todo lo probado.
- R170_861 (0.3), §§2, 6 y R182_201 §2: una extensión positiva con complemento de Schur fijo es
  congruencia triangular; completar el bloque en abstracto equivale a lo buscado; queda abierto sólo
  un factor fuente no local (NGF, R182_201 (3.1)–(NGF), OPEN).

Diferencia de marco que pide el encargo: toda la fase 170 trabaja con un vector f del radical de una
ventana de primer contacto supuesta y usa la positividad para deducir una igualdad (Lema 2.1). La
fase 212 pide la dirección contraria: una identidad (G) sobre todo P_T que produzca la positividad.

### (2) El objeto, escrito

Formato candidato (variante con borde de (G)). Espacio ampliado

    Ê_T = (ℝ^N ⊕ ℝ) ⊗ ℋ ⊕ ℬ_T ⊕ 𝒳_T,

una forma 𝔾_T ⪰ 0 manifiesta sobre Ê_T (por ejemplo 𝔾_T = 𝓔_T*𝓔_T con 𝓔_T escrito), un vector nulo
ê_T(F) = ((Λ,1)⊗F, β_T(F), 0) con 𝔾_T(ê_T(F)) = 0, una inmersión ι_T : P_T → Ê_T y una de las dos
lecturas

    (G-res)   a_T(F) = 𝔾_T(ι_T F),
    (G-Schur) a_T(F) = inf_{y ∈ 𝒴} 𝔾_T(ι_T F + y),   𝒴 ⊂ Ê_T un subespacio auxiliar.

Lo que el encargo pide fijar y lo que hay: β_T, según R170_868 §6, sale de la ecuación de primer
contacto, que sólo existe para f en el radical de una ventana con λ_A(T) = 0. Sobre un F ∈ P_T
general no hay ecuación de primer contacto. Su única extensión a todo P_T, la ecuación de
Euler–Lagrange de λ_A, sólo vale en un minimizador (patrón B9). La definición literal de R170_856
(8.7), β(F) = (b, PȦF) − (h, P𝒞F) − ρ_F g_ε, sí tiene sentido para todo F como funcional lineal. La
§2 prueba que, dentro de (G-res) o (G-Schur), ningún β_T y ningún vector nulo influye en la
identidad. Por eso no hay ℋ_T, V_T, ρ_T nuevos que escribir: el formato se reduce a (G) sin borde.

### (3) ¿Esquiva la dificultad del antecedente?

No. La dificultad de 862/870 es que la clase de borde es lineal e impar y la positividad es par.
Dentro de (G) todo es cuadrático y la paridad desaparece, pero sólo porque el ancla deja de actuar
(Lema 1). La dificultad de 861 y R182_201 §2 (Schur fijo = congruencia) se reproduce: con 𝔾_T
manifiesta, (G-Schur) es (G) con V_T explícito (Lema 3); con 𝔾_T no manifiesta, 𝔾_T ⪰ 0 equivale al
objetivo (861 (1.2)).

### (4) Conexión con la positividad global

Ninguna nueva: si (G-res) o (G-Schur) valen con 𝔾_T ⪰ 0, entonces a_T ≥ 0 sobre P_T de forma
inmediata, igual que con (G). Todo el contenido está en escribir 𝔾_T (o V_T) manifiestamente
positiva con la identidad exacta. El ancla no aporta ninguna desigualdad intermedia (Lema 1,
Proposición 2).

### (5) Líneas de ruptura para cΛ y a_P

- La nulidad del ancla falla en R170_866 (2.1), fila k = 2: Σ_{d|2} cΛ(d) − log 2 = (c − 1) log 2 ≠ 0;
  para a_P con P > 2, (a_P∗1)(2) − log 2 = −log 2 ≠ 0. PROVED (cuenta directa).
- Esas rupturas no son rupturas de (G): por el Lema 1, ê_T puede quitarse de ι_T sin cambiar la
  identidad. La línea que tendría que romperse es la prueba de 𝔾_T ⪰ 0 (o de ρ_T ≥ 0), que no está
  escrita. Además, para cΛ la ruptura cerca de c = 1 es automática en el formato (Lema 4) y no
  aporta signo. Punto (5) sin respuesta: la candidata no está lista para construcción.

## 1. Convenciones

E es un espacio vectorial real o complejo y 𝔾 una forma hermítica semidefinida positiva sobre E,
sin hipótesis topológicas. Se escribe 𝔾(x) = 𝔾(x,x) y K = {k : 𝔾(k) = 0}.

## 2. Lemas (todos PROVED, con demostración completa)

**Lema 1 (invisibilidad del núcleo).** K es un subespacio, 𝔾(x, k) = 0 para todo x ∈ E y k ∈ K, y
𝔾(x + k) = 𝔾(x). En consecuencia, para toda aplicación ι : P_T → E (lineal o no), toda aplicación
κ : P_T → K y todo subespacio 𝒴 ⊂ E:

    𝔾(ι F + κ F) = 𝔾(ι F),
    inf_{y∈𝒴} 𝔾(ι F + κ F + y) = inf_{y∈𝒴} 𝔾(ι F + y) = inf_{y∈𝒴+K} 𝔾(ι F + y).

*Demostración.* Cauchy–Schwarz para formas semidefinidas: |𝔾(x,k)|² ≤ 𝔾(x)𝔾(k) = 0. Luego
𝔾(x + k) = 𝔾(x) + 2Re 𝔾(x,k) + 𝔾(k) = 𝔾(x). K es cerrado por sumas (𝔾(k + k′) = 𝔾(k) = 0) y por
escalares. La segunda línea se sigue de la primera aplicada a x = ιF + y. ∎

**Corolario 1.** En (G-res) y en (G-Schur), la identidad vale con ι_T si y sólo si vale con
ι_T − κ_T para todo κ_T : P_T → K. En particular, ni la nulidad de ê_T(F) ni el valor de β_T(F)
intervienen en la identidad. Si ι_T = ê_T + w_T, la identidad equivale a a_T(F) = 𝔾_T(w_T F) (o al
ínfimo correspondiente). La forma inducida sobre Ê_T/K es la única que importa, y en ella el ancla es
el vector cero.

**Proposición 2 (el formato con borde equivale a (G)).** Toda identidad (G),
a_T(F) = ‖V_T F‖² + ρ_T(F) con ρ_T(F) = Σ_j |r_j(F)|² escrita, se realiza en (G-res) con cualquier
β_T y con ê_T nulo. Recíprocamente, toda realización (G-res) con 𝔾_T = 𝓔_T*𝓔_T da (G) con
V_T = 𝓔_T ι_T y ρ_T = 0.

*Demostración.* Directa: tómese Ê_T = (ℝ^{N+1} ⊗ ℋ) ⊕ ℬ_T ⊕ (ℋ_T ⊕ ℓ²), 𝓔_T(x, b, h) = h (proyección
sobre el último sumando) e ι_T(F) = ((Λ,1)⊗F, β_T(F), (V_T F, (r_j(F))_j)). Entonces 𝓔_T ê_T(F) = 0
y 𝔾_T(ι_T F) = ‖V_T F‖² + Σ_j |r_j(F)|² = a_T(F). La recíproca es la definición. ∎

Lectura: exigir que (Λ,1)⊗F ⊕ β_T(F) sea nulo no restringe qué V_T son admisibles. Toda V_T
admite esa ampliación. Es una reformulación (patrones B3 y A4), no un mecanismo.

**Lema 3 (la variante de Schur es (G) o es el objetivo).** Sean 𝓔 = [E_X, E_Y] con E_X : X → 𝒦 y
E_Y : 𝒴 → 𝒦 lineales y 𝒦 de Hilbert, y 𝔾 = 𝓔*𝓔 sobre X ⊕ 𝒴. Entonces

    inf_{y∈𝒴} 𝔾(x + y) = ‖P^⊥ E_X x‖²,   P^⊥ = proyección ortogonal sobre (cl Ran E_Y)^⊥.

*Demostración.* inf_y ‖E_X x + E_Y y‖² = dist(E_X x, Ran E_Y)² = dist(E_X x, cl Ran E_Y)² =
‖P^⊥E_X x‖² (proyección sobre un subespacio cerrado de un Hilbert). ∎

Así, con 𝔾_T manifiesta, (G-Schur) es (G) con V_T = P^⊥E_X ι_T y ρ_T = 0. Si 𝔾_T no es manifiesta y su
bloque auxiliar es G > 0, R170_861 (1.2) da 𝔾_T ⪰ 0 ⟺ a_T ⪰ 0 (CITED, comprobado en primaria): el
problema se transfiere entero. Coincide con R182_201 §2.

**Lema 4 (ruptura automática bajo cΛ en el formato lineal en el peso).** Supóngase que 𝔾 ⪰ 0 no
depende del peso, que ι_a(F) = ι_0(F) + J(a ⊗ F) con J lineal, y que a_T(F; a) = 𝔾(ι_a F) vale para
todo F ∈ P_T y para a = Λ + tδ con t en un intervalo abierto, donde δ está soportado en [2, N) y no
es nulo. Entonces se llega a una contradicción. En particular, la identidad sólo puede valer en
valores aislados de c para cΛ (δ = Λ) y para Λ + s(a_P − Λ).

*Demostración.* El lado derecho es un polinomio de grado ≤ 2 en t con coeficiente principal
𝔾(J(δ⊗F)). El lado izquierdo es afín en t, con pendiente −Σ_n (2δ_n/√n) Re c_F(log n). La igualdad
en un intervalo obliga a 𝔾(J(δ⊗F)) = 0, es decir J(δ⊗F) ∈ K. Por el Lema 1 el lado derecho no
depende entonces de t, de modo que la pendiente es cero para todo F ∈ P_T. Pero la forma
F ↦ Σ_n (δ_n/√n) Re c_F(log n) tiene símbolo τ ↦ Σ_n (δ_n/√n) cos(τ log n), que es casi periódico
y no nulo en ℝ. Sus valores sobre |F̂|², con F ∈ P_T, no son todos nulos: por polarización se
anularía como forma sesquilineal sobre P_T, y P_T tiene codimensión dos en L²(I_T), lo que permite
elegir F, G ∈ P_T con F̂ Ĝ‾ cuya integral contra el símbolo no es cero. ∎

Lectura: en este formato, la cláusula O4 para cΛ cerca de 1 se cumple gratis. Que «la identidad se
rompe bajo cΛ» no indica, por sí solo, ninguna maquinaria de signo.

Nota sobre la última línea: el paso «el símbolo no nulo no se anula como forma sobre un subespacio de
codimensión finita» se usa en la forma elemental siguiente. Si ∫ σ F̂ Ĝ‾ = 0 para todo F, G ∈ P_T,
tomando F fijo y G variando en un subespacio de codimensión dos, la función σF̂ restringida (vía
transformada inversa) a I_T está en el espacio generado por e^{±t/2}. Variando F en un subespacio de
dimensión ≥ 3 sale σ ≡ 0 por la independencia de las traslaciones por log n, n < N. Lo dejo con esta
redacción. La parte del Lema que se usa abajo (coeficiente principal nulo e invisibilidad) es
completa; el argumento de no anulación de la pendiente es ARGUED en esta forma resumida, aunque el
hecho es estándar.

## 3. Clase del resultado negativo

NO-GO con clase (PROVED, Lema 1, Proposición 2 y Lema 3). Clase: realizaciones exactas de a_T sobre
P_T por restricción o por ínfimo parcial de una forma hermítica **semidefinida positiva** 𝔾_T sobre
cualquier espacio ampliado, con cualquier vector nulo (en particular (Λ,1)⊗F ⊕ β_T(F), con cualquier
β_T, lineal o no). En esa clase:

(a) el ancla y la coordenada de borde no influyen en la identidad;
(b) el formato con borde coincide con (G);
(c) la variante de Schur es (G) si 𝔾_T es manifiesta, y es el objetivo si no lo es.

Lo que la clase NO excluye:

1. **Formas indefinidas (Kreĭn).** Si 𝔾_T es indefinida, un vector neutro (𝔾_T(v) = 0) no está en
   el radical y el Lema 1 falla. Es el caso de la graduación de R170_854 (métrica indefinida) y de
   861 §4. La positividad ya no es manifiesta y haría falta otro mecanismo. Sin objeto.
2. **Esquemas por familias y contradicción.** El uso original del ancla en 862 es el Lema 2.1, que
   va de positividad bilateral a una igualdad en el primer contacto. Ese esquema no es una identidad
   (G) y sigue OPEN en la fase 170 (VIR–LB; 869 §5; 870 §5, acoplamiento impar o segundo radical
   común). Este memo no lo toca.
3. **El propio (G)** con V_T construido de Λ exacta, y el factor fuente no local NGF de R182_201,
   que es una instancia de (G) con estructura de Schur (Lema 3). Ambos OPEN.
4. **Vectores nulos que restrinjan 𝔾_T** cuando 𝔾_T se fija de antemano por otras razones (por
   ejemplo 𝔾_T construida sólo con el peine y los puertos, sin Λ). La Proposición 2 dice que la
   condición de nulidad no restringe V_T en general. No dice que, para una 𝔾_T dada, la condición
   carezca de contenido. Pero entonces el contenido es la positividad de esa 𝔾_T sobre el cociente,
   y no se conoce ninguna con la identidad exacta.

## Resultado

Sin mecanismo nuevo, más una pieza de NO-GO con clase (PROVED). El ancla nula con borde y la
coordenada β_T son invisibles en cualquier identidad de Gram semidefinida, y el formato con borde
equivale a (G). La candidata no pasa la puerta de selección: no puede escribir (2) más allá de (G)
ni (5).

## Qué se probó

- Lema 1 (invisibilidad del núcleo) y Corolario 1: PROVED.
- Proposición 2 (el formato con borde equivale a (G); la nulidad de (Λ,1)⊗F ⊕ β_T(F) no restringe
  V_T): PROVED.
- Lema 3 (variante de Schur = (G) con V_T = P^⊥E_Xι_T, o el objetivo vía R170_861): PROVED, sin
  hipótesis de rango cerrado.
- Lema 4 (en el formato lineal en el peso, la ruptura bajo cΛ y bajo Λ + s(a_P − Λ) cerca del peso
  exacto es automática): coeficiente principal e invisibilidad PROVED; la no anulación de la
  pendiente es ARGUED en la redacción dada.
- Líneas de ruptura de la nulidad: R170_866 (2.1) en k = 2 para cΛ (c ≠ 1) y para a_P (P > 2):
  PROVED.

## Qué falló y por qué

- β_T no tiene definición sobre todo P_T con el contenido de 868 §6: sale de la ecuación de primer
  contacto, que sólo existe en el radical. Su extensión natural, la ecuación de Euler–Lagrange, vale
  sólo en el minimizador (B9).
- Aunque se defina β_T sobre todo P_T (por ejemplo con la fórmula lineal de R170_856 (8.7)), el
  Lema 1 la vuelve irrelevante en una identidad semidefinida. La paridad de 870 desaparece por la
  misma razón: no hay clase impar que firmar porque el ancla no actúa. Eso no aporta signo.
- La variante de Schur repite 861 y R182_201 §2.

## Siguiente paso concreto

No relanzar el ancla con borde como objeto de (G) en la clase semidefinida. Si se quiere usar la
zona, las dos salidas no excluidas tienen enunciado preciso:

(i) una forma indefinida 𝔾_T de Kreĭn, construida con el peine y los puertos, en la que
(Λ,1)⊗F ⊕ β_T(F) sea un vector neutro y de la que a_T salga como restricción a un subespacio
positivo. Habría que escribir antes qué mecanismo daría la positividad de ese subespacio, que no
puede ser ninguno de los de 861 §4 ni de R170_854 (3.4);

(ii) el factor NGF de R182_201 (3.1) como instancia de (G), con la admisibilidad allí escrita.

Ninguna tiene objeto escrito. Anotación sugerida para el índice y el grid (no hecha desde aquí):
«P212-3.4: ancla nula con borde en el formato (G) — NO-GO con clase PROVED (invisibilidad del
núcleo en formas semidefinidas; el formato con borde equivale a (G)). No excluye: formas
indefinidas, esquemas por familias de 862, NGF».
