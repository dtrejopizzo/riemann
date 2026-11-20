# Ronda 1 — Candidata K3: sistema ampliado de cuadrados para los cruces no resonantes

Memo de selección. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md` y de
`../phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md` (citado «GRAM»); la nota
`../phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md` se cita «GLOBAL». Etiquetas: PROVED / CITED /
CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO. «CITED» se usa también para resultados PROVED en el
corpus que aquí no se vuelven a demostrar.

Pregunta de diseño. La parte resonante R_res del kernel completo A sobre escalas enteras es una suma de
cuadrados exacta indexada por la clase libre de cuadrados (GRAM §17.2, RES-SOS). ¿Existe un sistema
AMPLIADO de cuadrados, indexado además por datos aritméticos exactos (caracteres aditivos, componentes
de sumas de Ramanujan, retículo gcd/lcm con inversión de Möbius dentro del cuadrado), en el que los
cruces no resonantes Off = A − R_res queden absorbidos exactamente, de modo que
A = Σ cuadrados + (resto manifiestamente no negativo) sea una identidad?

Respuesta corta. No, dentro de la clase declarada en §3 (selección o torsión aritmética en el índice de
nodos o en el índice de modos): NO-GO PROVED (Teorema R y corolarios). Fuera de esa clase no se
identificó ningún mecanismo nuevo; lo que queda es la forma completa en la variable t, ya registrada.

---

## 0. Cotejo

**(1) Antecedente más cercano.** Tres piezas, las tres en la fase 211:

- GRAM §18.7, (TAIL-ZERO) y (NO-FIN-MARGIN) con su corolario: no existe una identidad única
  A_0[c] = Σ_α w_α|ℓ_α(c)|², w_α ≥ 0, con todos los ℓ_α de soporte finito; ningún observable de soporte
  finito sostiene un margen. Esto ya excluye el sistema ampliado cuando todos sus cuadrados dependen de
  un número finito de coeficientes.
- GLOBAL, «Extensión factorial antes de resonancia»: es literalmente el sistema ampliado natural (se
  conservan los productos de frecuencias distintas antes de completar cuadrados; identidad exacta
  Q = Σ_m Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b)); el resto D + E no es no negativo, y la «Consecuencia
  para el resto conjunto» de «Escalas libres de cuadrados» prueba que esos cuadrados no son continuos en
  la norma del grafo y que Q ≥ εS_sq es falsa para todo ε > 0.
- GLOBAL, «Control de la sustitución ortogonal»: al cambiar la selección coordenada P_m por la
  proyección ortogonal la suma de cuadrados diverge.

Otros antecedentes consultados: GRAM §§17.6–17.7 (márgenes y pago separado), GLOBAL «El presupuesto
resonante exige una comparación unilateral», «Covarianza divisorial agrupada», «El resto divisorial es
indefinido»; índice de rutas 06, residuos R1 y R9 (subrutas muertas: identidad matricial exacta de
1∗Λ = log más allá de divisores, Near como operador separado, subespacios equilibrados por residuos,
familia de conductor q > 1 por vectores torcidos); fase 188 L2_BUILD_030 y N_BUILD_021; memoria de
selecciones rechazadas (las ocho). Búsqueda de «Müntz», «Carlson», «soporte finito», «NO-FIN-MARGIN»
en índice, grid, crucigrama y Papers 47–48: no aparece el enunciado general de §3 de esta memo; aparece
su caso libre de cuadrados (GLOBAL, «Escalas libres de cuadrados») y su caso de soporte finito
(GRAM §18.7). Una búsqueda sin coincidencia literal no prueba novedad conceptual: el Teorema R es la
generalización común de esos dos casos con el mismo instrumento.

**(2) Objeto o afirmación realmente nuevos.** No hay objeto constructivo nuevo. La lectura constructiva
de K3 (ampliar el índice de los cuadrados de RES-SOS con datos aritméticos de los nodos o de los modos)
es **repetición** de la extensión factorial y de sus dos controles; según la regla 3 del brief esa
lectura termina aquí. Lo que la memo sí aporta es la respuesta a la pregunta de clase que el encargo
pide decidir: un teorema de rigidez (Teorema R, §3) que excluye de una vez todo cuadrado, de dependencia
finita o infinita, obtenido por selección o torsión aritmética, y que explica por qué los tres
antecedentes fallaron por la misma causa.

**(3) Por qué el cambio evita la dificultad del antecedente.** No la evita: la identifica. La dificultad
común es que la exactitud con resto no negativo obliga a cada cuadrado a ser continuo en la norma del
grafo de A, y la continuidad obliga a que sus coeficientes sean los valores en los enteros de una
función holomorfa de crecimiento polinómico en un semiplano. Ninguna selección aritmética tiene esa
propiedad.

**(4) Identidad o desigualdad que conecta con la positividad global.** Ninguna nueva. El resultado es
una condición necesaria sobre el operador V de la identidad (G) de `OBJECT_SPEC.md` en el portador de
escalas enteras (reducción PROVED, GRAM §18 y §18.9): V es continuo en la norma del grafo y sus
coeficientes son sucesiones analíticas en el sentido de §3.

**(5) Línea que se rompe para cΛ y a_P.** No hay paso de signo, luego no hay línea que deba romperse.
El Teorema R es una barrera y, como debe ser, no distingue pesos: sólo usa la continuidad de la forma
en el grafo (§8).

**Relación con las selecciones rechazadas de la memoria.** K3, leída constructivamente, coincide con
«Cuadrados factoriales y proyecciones físicas». No toca «(m,n) → (m+n, m−n)» ni «sumación por partes
discreta en theta» ni «compensación entre escalas»: no se reindexa, no se telescopa ni se propone una
cota del resto. La memo no reabre ninguna de las ocho.

---

## 1. Marco (CITED)

Se trabaja en y = 0, con coeficientes complejos c = (c_k)_{k ≥ 1} de soporte finito sobre los enteros
positivos, y

    A_0[c] = Σ_{k,l} c_k conj(c_l) A(½ log k, ½ log l).

Hechos usados, todos PROVED en la fase 211:

(M1) **Grafo** (GRAM §18.1). Con P_κ(t) = κ^{5/4} Σ_{n≥1} n² e^{−πκn²t}, T = πt^{5/4}(−2tD − 3),
F(P) = TP, G(P) = ½T Lg P − C TP y P(c) = Σ_k c_k P_k, se tiene

    A_0[c] = ∫_1^∞ [log t |F|² + 2 Re(G conj F)] dt/(2t),   F = F(P(c)), G = G(P(c)).   (A-GRAPH)

(M2) **Continuidad** (GRAM §18.2). Para 0 < a < π fijo y ‖P‖_{a,2} = max_{j≤2} sup_{t≥1} e^{at}|P^{(j)}(t)|
(espacio de Banach B_a²), existe C_a con

    |A_0[c]| ≤ C_a ‖P(c)‖²_{a,2}   para todo c finito.

No presupone signo de A_0.

(M3) **Holomorfía** (GLOBAL, «Escalas libres de cuadrados»). Para a/π < δ < 1, z ↦ P_z es holomorfa de
{Re z > a/π} en B_a², con ‖P_z‖_{a,2} ≤ C_δ(1 + |z|)^{13/4} en Re z ≥ δ. (Cada término
z^{5/4}n²e^{−πzn²t} es holomorfo con valores en B_a² y de norma ≤ |z|^{5/4}n²(1 + π|z|n²)²e^{a − πδn²};
la serie converge localmente uniformemente.) Del mismo modo E_z(t) = e^{−πzt} es holomorfa con
‖E_z‖_{a,2} ≤ (1 + π|z|)² e^{a − πδ}.

(M4) **Modos** (GRAM §17, §18.3). Con b_λ(c) = Σ_{kn²=λ} n^{−1/2} c_k se tiene
P(c) = Σ_{λ≥1} λ^{5/4} b_λ(c) E_λ, absolutamente en B_a²; y E_k = k^{−5/4} Σ_n μ(n) n^{−1/2} P_{kn²},
absolutamente en B_a² (MOB-P). Para λ = dq² con d libre de cuadrados, b_λ = q^{−1/2} f_{d,q},
f_{d,q} = Σ_{a|q} √a c_{da²}. R_res es la parte diagonal en λ, Off la parte λ ≠ μ.

(M5) **RES-SOS** (GRAM §17.2–17.5). R_res[c] = Σ_d √d [Σ_q D_q|f_{d,q}|² + Σ_q Σ_{m|q, m≥2}
Λ(m) I_q |f_{d,q} − f_{d,q/m}|²], con D_q ≥ c_* I_q > 0.

---

## 2. Sistemas de cuadrados y continuidad forzada

**Definición (sistema de cuadrados exacto).** Un sistema de cuadrados es un par (ℋ, V) con ℋ un
espacio de Hilbert y V lineal del espacio de coeficientes finitos en ℋ; su energía es 𝒮[c] = ‖Vc‖².
Esto incluye sumas discretas Σ_α w_α|ℓ_α(c)|² (ℋ = ℓ² ponderado) e integrales ∫|ℓ_t(c)|² dμ(t)
(ℋ = L²(μ)). El sistema es **exacto para A_0** si

    A_0[c] = ‖Vc‖² + ρ[c],   ρ[c] ≥ 0   para todo c finito.                         (EX)

Es la identidad (G) de `OBJECT_SPEC.md` §1 en el portador de escalas enteras.

**Lema 1 (continuidad forzada). PROVED.** Si (ℋ, V) cumple (EX), o sólo ‖Vc‖² ≤ M·A_0[c] para algún
M finito y todo c finito, entonces ‖Vc‖² ≤ M C_a ‖P(c)‖²_{a,2}. En particular, para cada g ∈ ℋ el
funcional ℓ_g(c) = ⟨Vc, g⟩ satisface |ℓ_g(c)| ≤ (M C_a)^{1/2} ‖g‖ ‖P(c)‖_{a,2}.

*Demostración.* ‖Vc‖² ≤ M A_0[c] ≤ M|A_0[c]| ≤ M C_a‖P(c)‖² por (M2); el resto es la desigualdad de
Cauchy–Schwarz en ℋ. ∎

Observación. No se usa que A_0 sea no negativa; sólo que el cuadrado queda por debajo de A_0. Un
cuadrado que no es continuo en la norma del grafo no puede figurar en ninguna identidad (EX), con
cualquier resto no negativo, sea cual sea el resto.

---

## 3. Teorema de rigidez

Fijar 0 < a < π y a/π < δ < 1. Llamar **divergente** a un conjunto Z de enteros positivos con
Σ_{k∈Z} 1/k = ∞.

**Teorema R. PROVED.** Sea (ℋ, V) con ‖Vc‖² ≤ M‖P(c)‖²_{a,2} para todo c finito (por el Lema 1, todo
sistema exacto lo cumple). Entonces, para cada g ∈ ℋ:

(R0) *Interpolación en nodos.* Existe N_g holomorfa en Re z > a/π, con
|N_g(z)| ≤ C(1 + |z|)^{13/4} en Re z ≥ δ, tal que ⟨Vδ_k, g⟩ = N_g(k) para todo entero k ≥ 1.

(R0′) *Interpolación en modos.* Existe n_g holomorfa en Re z > a/π, con |n_g(z)| ≤ C(1 + |z|)^{13/4} en
Re z ≥ δ, tal que ⟨Vc, g⟩ = Σ_{λ≥1} b_λ(c) n_g(λ) para todo c finito (serie absolutamente convergente).

(R1) *Unicidad sobre conjuntos divergentes.* Si N_g(k) = 0 para todo k de un conjunto divergente,
entonces ⟨Vc, g⟩ = 0 para todo c. Lo mismo si n_g(λ) = 0 para todo λ de un conjunto divergente.

(R2) *Ninguna torsión aritmética.* Sea (ℋ, V′) otro sistema con la misma cota y θ: ℕ → ℂ tal que
existe α ∈ ℂ con {θ = α} y {θ ≠ α} ambos divergentes. Si Vδ_k = θ(k)V′δ_k para todo k, entonces
V = V′ = 0. Lo mismo en modos: si n_g(λ) = θ(λ) n′_g(λ) para todo λ y todo g, entonces V = V′ = 0.

*Demostración.* (R0). ℓ_g se anula donde P(c) = 0, luego define un funcional lineal sobre el subespacio
{P(c)} ⊂ B_a², acotado por (M)^{1/2}‖g‖. Por Hahn–Banach se extiende a un funcional continuo ℓ̃_g sobre
B_a². Poner N_g(z) = ℓ̃_g(P_z). Por (M3), N_g es holomorfa y tiene la cota indicada; N_g(k) = ℓ_g(δ_k)
porque P(δ_k) = P_k.

(R0′). Poner n_g(z) = z^{5/4} ℓ̃_g(E_z), holomorfa con la cota indicada por (M3). Por (M4) y la
continuidad de ℓ̃_g, ℓ_g(c) = ℓ̃_g(P(c)) = Σ_λ λ^{5/4} b_λ(c) ℓ̃_g(E_λ) = Σ_λ b_λ(c) n_g(λ).

(R1). Sea N holomorfa en Re z > a/π con |N(z)| ≤ C(1 + |z|)^{13/4} en Re z ≥ δ y N(k) = 0 para k ∈ Z,
Z divergente; se puede suponer Z ⊂ (δ, ∞). Poner H(z) = N(z)/(z + 1)⁴. Como |z + 1|² ≥ (1 + |z|)²/2 en
Re z > 0, H es acotada en Re z ≥ δ, y es holomorfa en un entorno de ese semiplano cerrado. Para un
subconjunto finito Z₀ ⊂ Z, cada factor β_k(z) = (z − k)/(z + k − 2δ) tiene módulo 1 en Re z = δ, módulo
< 1 en Re z > δ y tiende a 1 en infinito. El cociente H/Π_{k∈Z₀} β_k es holomorfo y acotado en
Re z > δ, continuo hasta el borde, y de módulo ≤ ‖H‖_∞ en el borde; por el principio de
Phragmén–Lindelöf para funciones acotadas en un semiplano, lo es en todo el semiplano. Para z₀ real,
z₀ > δ, z₀ ∉ Z:

    |H(z₀)| ≤ ‖H‖_∞ Π_{k∈Z₀} |k − z₀|/(k + z₀ − 2δ).

Para k > z₀ el factor es 1 − 2(z₀ − δ)/(k + z₀ − 2δ), y Σ_{k∈Z} 1/(k + z₀ − 2δ) = ∞; el producto tiende
a 0 al agotar Z. Luego H(z₀) = 0 en un conjunto con puntos de acumulación y N ≡ 0. Aplicado a N_g:
N_g(k) = ⟨Vδ_k, g⟩ = 0 para todo k, luego ℓ_g = 0. Aplicado a n_g: n_g ≡ 0 y ℓ_g = 0 por (R0′).

(R2). Fijar g. N_g − αN′_g es holomorfa con la misma cota y se anula en {θ = α}, divergente; por (R1)
N_g = αN′_g en todo el semiplano. Entonces (θ(k) − α)N′_g(k) = 0 para todo k, luego N′_g se anula en
{θ ≠ α}, divergente, y N′_g ≡ 0, N_g ≡ 0. Como g es arbitrario, Vδ_k = V′δ_k = 0 para todo k. El caso
de modos es idéntico con n_g, n′_g. ∎

Comentario. (R1) es un enunciado de unicidad tipo Müntz en forma dual; aquí sólo se usa y se prueba
la dirección «Z divergente ⟹ unicidad». El caso Z = cola de libres de cuadrados es GLOBAL, «Escalas libres de
cuadrados»; el caso «complemento de un conjunto finito» da GRAM §18.7 sin usar (TAIL-ZERO). El
instrumento es el mismo; no se atribuye novedad a él.

---

## 4. Clases excluidas

**Clase 𝒜 (declarada).** Sistemas de cuadrados (ℋ, V) que contienen una componente no nula de alguno de
los tipos siguientes, en el índice de nodos k o en el índice de modos λ:

(a) *selección*: una componente ⟨V·, g⟩ cuyos coeficientes se anulan sobre un conjunto divergente;
(b) *torsión*: una componente de la forma θ·V′ con V′ continuo en el grafo y θ como en (R2);
(c) *selección o torsión más término continuo*: V = V₁ + V₂ con V₂ continuo en el grafo y V₁ de tipo
    (a) o (b).

**Corolario 2 (NO-GO, clase 𝒜). PROVED.** Ningún sistema de la clase 𝒜 es exacto para A_0, con ningún
resto no negativo. Más aún, ninguno cumple 𝒮 ≤ M·A_0 con M finito.

*Demostración.* Si lo fuera, V sería continuo en el grafo (Lema 1). En el caso (c), V₁ = V − V₂ también
lo sería. Entonces (R1) o (R2) fuerzan que la componente sea nula. ∎

Instancias, todas con la misma demostración:

1. **Dependencia finita** (soporte finito en k): el complemento es divergente. Recupera GRAM §18.7.
2. **Índice de clase libre de cuadrados.** Un cuadrado que sólo usa los c_{da²} de una clase d (o de un
   número finito de clases), con cualquier cantidad de coeficientes: su complemento contiene todos los
   enteros de otras clases, divergente. En particular **ninguno de los cuadrados de RES-SOS** (D_q|f_{d,q}|²
   ni Λ(m)I_q|f_{d,q} − f_{d,q/m}|²) puede sobrevivir, ni solo ni acompañado, en una identidad exacta
   para el A completo. El índice «clase libre de cuadrados» no puede ser parte del índice de ningún
   sistema exacto.
3. **Clases de residuos y caracteres.** Cuadrados soportados en k ≡ r (mod q), q ≥ 2; cuadrados con
   coeficientes e(rk/q)·N(k), χ(k)·N(k), c_q(k)·N(k) (suma de Ramanujan) o φ(gcd(k,q))·N(k) con N los
   coeficientes de un funcional continuo y la torsión no constante: excluidos por (R1) y (R2). Una
   familia de cuadrados indexada por caracteres aditivos módulo q con amplitud común admite a lo sumo
   un miembro no nulo.
4. **Retículo gcd/lcm con Möbius dentro del cuadrado.** Cuadrados soportados en los múltiplos de g ≥ 2,
   en los divisores de q, en los k con gcd(k,q) dado; cuadrados con peso μ(k)·N(k), μ²(k)·N(k) o
   Λ(k)·N(k): excluidos ({μ = 0} y {μ ≠ 0} son divergentes; {Λ = 0} y los primos son divergentes).
5. **Selección de modos.** Toda proyección coordenada sobre los modos λ divisibles por m² (m ≥ 2), o
   sobre cualquier conjunto de modos de complemento divergente, aplicada a un operador continuo. En la
   extensión factorial, V_m c = Σ_λ [(P_m b)_λ − (R_m b)_λ] h_λ ∈ L²([1,∞), dt/(2t)); el término R_m es
   continuo (‖R_mF‖ ≤ m^{−1/2}‖F‖) y el término P_m es la selección 1_{m²|λ} de la inmersión continua
   c ↦ F: caso (c). Así cada cuadrado Λ(m)‖P_m b − R_m b‖²_K, por separado, es incompatible con (EX);
   esto recupera la discontinuidad de S_sq de GLOBAL sin usar la densidad libre de cuadrados.
6. **Pesos diagonales no negativos** Σ_k w_k|c_k|² o Σ_λ w_λ|b_λ|² con algún peso positivo: caso 1.

La única función aritmética clásica que pasa el filtro (R0) como torsión es log k, que es holomorfa:
es coherente con que g_q use log a y con que el separador Σ_{d|n}Λ(d) = log n sea el punto donde la
aritmética entra en (A-GRAPH). Esto es una observación, no un mecanismo.

---

## 5. Dirección de energía estrictamente negativa del resto

**Proposición 3. PROVED.** Sea (ℋ, V) un sistema con una componente ℓ = ⟨V·, g⟩, ‖g‖ = 1, no continua
en la norma del grafo (por ejemplo, cualquier sistema de la clase 𝒜). Entonces existen c^{(n)} finitos
con

    ‖P(c^{(n)})‖_{a,2} → 0,   ℓ(c^{(n)}) = 1,   A_0[c^{(n)}] → 0,
    limsup (A_0 − 𝒮)[c^{(n)}] ≤ −1.

Para V = sistema RES-SOS: fijados d, q, existen c^{(n)} con f_{d,q}(c^{(n)}) = 1, A_0[c^{(n)}] → 0 y

    limsup Off[c^{(n)}] ≤ −√d·D_q < 0,    (Off + R_res)[c^{(n)}] → 0.

*Demostración.* Que ℓ no sea acotado respecto de ‖P(c)‖ significa que para cada n hay c con
|ℓ(c)| > n‖P(c)‖_{a,2}; dividiendo por ℓ(c) se obtiene c^{(n)} con ℓ(c^{(n)}) = 1 y ‖P(c^{(n)})‖ < 1/n.
(M2) da A_0[c^{(n)}] → 0, y 𝒮 ≥ |ℓ|² = 1. Para RES-SOS, f_{d,q} es un funcional no nulo de soporte
finito; si fuera acotado respecto de ‖P(c)‖ sería nulo por (R1), luego no lo es. Además
R_res ≥ √d·D_q|f_{d,q}|² por (M5), y Off = A_0 − R_res. ∎

Lectura. Off no es «pequeño frente a R_res»: en estas direcciones Off cancela a R_res por completo
(holgura cero, sin margen). La desigualdad crítica Off ≥ −R_res no queda refutada ni probada; queda
probado que ningún reparto de R_res en cuadrados de la clase 𝒜 puede conservarse al añadir Off.

---

## 6. Respuesta sobre GRAM §17.6–17.7

- §17.6 excluye Off ≥ −C·E_y y A ≥ δ·R_res: comparaciones con margen. §17.7 excluye pagar el operador
  de dilataciones C con la energía ∫(1 + log t)|F|². Ninguna de las dos excluye por sí misma una
  absorción exacta. **PROVED** (lectura de sus enunciados).
- La absorción exacta en la clase 𝒜 queda excluida por el Corolario 2. **NO-GO, PROVED**, clase 𝒜.
- Fuera de 𝒜 la absorción exacta no queda excluida y no puede quedarlo por un argumento de clase:

**Proposición 4. PROVED (elemental).** A_0 ≥ 0 sobre todo c finito si y sólo si existe un sistema
exacto (ℋ, V) con ρ = 0. En tal caso todas sus componentes son continuas en el grafo y cumplen (R0),
(R0′).

*Demostración.* Si A_0 ≥ 0, tomar ℋ como la compleción del cociente de los c finitos por el núcleo de
la seminorma A_0^{1/2} y V la aplicación canónica. El recíproco es trivial y el resto es el Lema 1 con
el Teorema R. ∎

Así, la existencia de un sistema ampliado exacto fuera de 𝒜 **es** el objetivo, sin información
adicional de signo; la factorización triangular correspondiente figura en las familias cerradas como
reformulación (`RULES_AVOID.md` §C, objeto de signo de la fase 200: Cholesky).

---

## 7. Lo que no queda excluido y por qué no es una candidata

(i) **Cuadrados del lado t.** Los funcionales continuos en el grafo son funcionales de la función
P (o F = TP) en t ≥ 1: valores F(t₀), diferencias F(t₀) − m^{−1/2}F(m²t₀), integrales contra medidas.
La aritmética puede entrar ahí por el índice de DILATACIÓN m (pesos Λ(m), caracteres en m), no por
nodos ni modos. El Teorema R no dice nada de esa clase. Pero esa forma es la forma completa causal en
la variable t (GLOBAL, «Control operativo de deduplicación de §18.5»), donde ya están registrados:
la divergencia Σ_m Λ(m)‖F − R_mF‖² = ∞ (GLOBAL, «Control de la sustitución ortogonal»), la pérdida de
tasas positivas tras T (GRAM §18.5), el signo desfavorable del potencial causal (GRAM §19.12) y el
residuo R9 del índice. No se encontró en esta memo una operación explícita que descomponga
T Lg T^{−1} + log t en términos que se emparejen con Λ(m) m^{−1/2} D_{m²} para cada m. **Sin mecanismo
nuevo.** OPEN.

(ii) **Formulación (S).** El Teorema R depende de la holomorfía de z ↦ P_z y no se transporta a la
matriz 𝔸_M = [B(log m − log k)] de P47 prop:AM. Allí sólo vale la restricción elemental siguiente.

**Observación 5. PROVED.** Si un funcional ℓ(x) = Σ_m w_m x_m sobre vectores finitos cumple
|ℓ(x)|² ≤ M·x*𝔸x (todo tamaño), entonces |w_m − w_k|² ≤ 2M[B(0) − B(log(m/k))]. Como B es par y C²
cerca de 0 (para |d| < log 2 − 2T₀ la parte aritmética de B(d) es nula, y en la parte arquimediana
F̂₀² = O(τ^{−4}) y m(τ) = O(log τ), de modo que τ² m(τ) F̂₀(τ)² es integrable),
|w_{m+1} − w_m| ≤ C_B M^{1/2}/m para m ≥ m₀(T₀).

*Demostración.* Aplicar la hipótesis a x = δ_m − δ_k: x*𝔸x = 2B(0) − 2B(log(m/k)). Taylor de orden
dos en d = log(1 + 1/m). ∎

Es una condición de módulo de continuidad, no una exclusión: un cuadrado torcido por un carácter
aditivo no queda prohibido en (S). La dirección admisible de R9 (componentes de carácter aditivo del
defecto m − kn, en la resolución e^{2T}) **no queda cerrada** por esta memo y tampoco queda
construida.

(iii) **Otras restas.** Identidades A = Σ cuadrados + ρ con ρ no negativo sólo sobre un subespacio, o
con ρ de signo no manifiesto, quedan fuera del enunciado. La extensión factorial es de este tipo
(D + E indefinido).

---

## 8. Batería de falsificadores

No hay paso de signo en esta memo. El Teorema R y el Corolario 2 usan de A_0 una sola propiedad: la
cota (M2). Esa cota vale para la forma análoga de cualquier peine cuyo operador
C_a = Σ a(m) m^{−1/2} D_{m²} sea acotado en H_γ, en particular para cΛ, a_P, borrado y amplificación
finitos y b_θ. La barrera es por tanto genérica en el peine (tipo B1 de `RULES_AVOID.md`), como
corresponde a un NO-GO, y no aporta ni pretende aportar signo. Para Davenport–Heilbronn, Epstein,
cuartetos, f_t y Beurling no se ha escrito la forma análoga en el portador de escalas enteras; no se
afirma nada sobre ellos.

Comprobación de coherencia con resultados positivos: RES-SOS es exacta para R_res, que no es continua
en el grafo (Proposición 3 aplicada a sus propios cuadrados); no hay contradicción porque (M2) es una
propiedad de A_0 completo, no de R_res ni de Off por separado.

---

## 9. Cierre

**Resultado.** NO-GO con clase, PROVED: ningún sistema de cuadrados que contenga una componente
obtenida por selección o torsión aritmética en el índice de nodos o de modos (clase 𝒜 de §4: dependencia
finita, clase libre de cuadrados, clases de residuos, caracteres aditivos o multiplicativos, sumas de
Ramanujan, retículo gcd/lcm, pesos μ o Λ, proyecciones coordenadas de modos) puede figurar en una
identidad exacta A_0 = Σ cuadrados + resto no negativo. Fuera de esa clase: **sin mecanismo nuevo**.
K3 no pasa a construcción.

**Qué se probó.** Lema 1 (exactitud con resto no negativo ⟹ continuidad en el grafo); Teorema R
(coeficientes = valores enteros de una función holomorfa de crecimiento polinómico; unicidad sobre
conjuntos de suma recíproca divergente; ninguna torsión aritmética); Corolario 2 (NO-GO de la clase
𝒜, que contiene como casos GRAM §18.7 y la discontinuidad de S_sq de la extensión factorial);
Proposición 3 (direcciones en que Off cancela exactamente a R_res); Proposición 4 (fuera de 𝒜 la
existencia de un sistema exacto es el objetivo mismo); Observación 5 (restricción de módulo de
continuidad en la formulación (S)).

**Qué falló y por qué.** La absorción exacta de Off en cuadrados con índice aritmético falla porque
toda componente de una identidad exacta es continua en la norma del grafo de A, y esa norma no ve la
aritmética de los nodos ni de los modos: sólo ve la función P(t). Los cuadrados resonantes viven
precisamente en coordenadas que esa norma no controla; por eso Off tiene que cancelarlos por completo
en las direcciones de la Proposición 3 y no admite reparto.

**Siguiente paso concreto.** (1) Anotar el NO-GO de la clase 𝒜 en el índice de rutas (06, residuo R9,
subrutas muertas) y en el grid; la memo no edita esos archivos. (2) Si se quiere reabrir K3, la única
lectura no excluida es (i) de §7: una identidad en la variable t con índice de dilatación m, y exige
escribir antes la descomposición de T Lg T^{−1} + log t que se empareja término a término con
Λ(m) m^{−1/2} D_{m²} con un corte que evite la divergencia registrada; sin esa operación explícita no
hay candidata. (3) La dirección de R9 en la formulación (S) sigue abierta con la restricción de la
Observación 5.

**No verificado.** Los hechos (M1)–(M5) se toman del corpus como PROVED y no se volvieron a derivar
(en particular la cota de continuidad (M2) de GRAM §18.2 y la holomorfía (M3)). No se hizo ningún
cómputo. La Observación 5 usa la fórmula de B de STATEMENT_001 §2 y el decaimiento F̂₀ = O(τ^{−2}) leído
de F̂₀ = (τ² + ¼)|ĝ|⁴; no se cotejó contra el texto del Paper 47. No se comprobó la forma análoga de (M2) para los modelos de la batería sin producto de Euler.
