# Ronda 1, candidata K4 — desigualdad multiescala no lineal con Λ más allá de la ventana

Memo de selección. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`; N = e^{2T}, X = e^{2T_0},
0 < T_0 < T. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO.

Resultado adelantado: **sin mecanismo nuevo**. No se pudo escribir el objeto. Se entrega (a) el enunciado
preciso de lo que el casillero pide, con todos los cuantificadores; (b) una clasificación PROVED de la
«completitud parcial más allá de X» en la clase de átomos lineales con restricciones convexas, que cierra
esa dirección como fuente de signo (NO-GO PROVED en un caso, identificación total en otro, y en el
tercero un enunciado estrictamente más fuerte que (★) con margen explícito); (c) la identidad de dos
escalas de grado dos escrita, con la demostración de que es lineal en los contactos nuevos para N ≤ X² y
de que la forma no ve el grado en Λ.

## 0. Cotejo

Fuentes consultadas: IDX `06_OPEN_RESIDUES_DEAD_SUBROUTES.md` R7; IDX `README.md` (fase 191, SPEC_A y
SPEC_B; principio del semianillo); IDX `04_PHASES_100-189.md` (filas N′ localizado, R185-circ,
G3A-R166_802); GRID §8 entradas 28 y 30 del registro de la fase 186; CW §3.3 (cierre), §4.2 (U1), §5 y
apéndice posterior; P48 «Statements weaker in appearance», «The live gate», tab:signobject (escalera
jerárquica de contactos); P47 lem:shape-ident, thm:shape, cor:void, prop:wit-sens, lem:degen,
thm:geo-split, thm:X, thm:noimport, rem:conjunctions, rem:spec-scope; `phase-186-toolbox/R186_005`
(con la corrección de `R186_092`); `phase-185-*/R185_004`; 211 `SQUARE_COMPLETENESS_OBSTRUCTION.md` §§1–2,
`POWER_CORPUS_OPPORTUNITY_AUDIT.md` (fila «Completitud parcial fuera de una ventana»), `LEDGER.md` C43,
C45, C47, `POWER_DESCENT_016.md` §2, `POWER_RECURRENCE_BOUNDARY_036.md` §7.

**(1) Antecedente más cercano.**
- `phase-186-toolbox/R186_005_DEGREE_TWO_SELBERG.md`: Lema S0 (la identidad de grado dos
  μ_b ∗ (N_b log²) = b·log + b∗b vale para todo b con su propio sistema (N_b, μ_b)), Lema S1
  (triangularidad), Teorema TB3-neg (lo cerrado por borrado más allá de X no decide; lo que usa
  completitud total identifica) y §5: «sobrevive sólo la completitud parcial más allá de X …
  OPEN; no hay candidata». La nota de `R186_092` corrige el inciso (ii) de ese teorema.
- `phase-185-*/R185_004`, Teorema U3 (borrado o identificación) y Lema 3 (completitud exacta).
- P47 thm:geo-split: la positividad sobre una clase que contiene a Λ se parte en el signo en Λ más una
  propiedad de rigidez sin signo.
- 211 `SQUARE_COMPLETENESS_OBSTRUCTION.md`: una familia concreta de completitud parcial (potencias
  perfectas) contiene un miembro negativo.
- IDX README, fase 191, SPEC_A (inducción exacta en T por contactos): NOT ADMISSIBLE.

**(2) Objeto o afirmación nuevos.** Ningún objeto 𝒪 = (ℋ_T, V_T, ρ_T). Afirmaciones nuevas respecto de los
antecedentes, todas en el lenguaje de la forma a_T:
- Teorema B (§3): para átomos lineales (λ∗1)(n) = log n sobre un conjunto arbitrario E ⊂ [X,N) y
  cualquier restricción convexa cerrada K, clasificación completa del enunciado «a_T^λ ≥ 0 sobre P_T
  para todo λ de la clase». Es el paso «especificar E primero» pedido en
  `POWER_CORPUS_OPPORTUNITY_AUDIT.md`, resuelto para todos los E a la vez.
- Corolario C (§3): con soporte en potencias de primos y N ≤ X², criterio combinatorio exacto en
  términos de E (divisores y valuaciones exactas).
- Proposición D (§4): la identidad de dos escalas de grado dos es lineal en los contactos nuevos si
  N ≤ X²; el primer término cuadrático en contactos nuevos aparece en N > X² y vive en los semiprimos.
- Lema A (§2): el grado en Λ es invisible para la forma (a_T es afín en el peine y todo hecho polinómico
  sobre Λ en [2,N) es consecuencia de los átomos lineales).

**(3) Por qué el cambio evita la dificultad del antecedente.** No la evita. R186_005 dejó abierta la rama
«completitud parcial» por falta de un E; aquí se demuestra que ningún E la convierte en mecanismo: o bien
un átomo queda libre y la clase contiene un peine con forma negativa (PROVED, por amplificación no
acotada, sin usar el signo de λ_A), o bien E identifica a Λ en [2,N) y el enunciado sobre la clase es
(★) en T sin información añadida, o bien la clase es un politopo acotado que contiene a Λ en su interior
relativo y el enunciado es (★) con un margen explícito, que es más fuerte que (★). El diseño propuesto en
la tarea (recursión X → X² con Σ_{d|n}Λ(d) = log n entrando en grado dos) cae en los fallos registrados:
véase §5.

**(4) Conexión con la positividad global.** No hay identidad (G). La única conexión que se prueba es
negativa: una identidad (G) cuyas premisas sobre el peine sean átomos de completitud en E y pertenencia a
K da positividad sobre toda la clase Π(E,K) (principio de transferencia, §3), y por el Teorema B eso sólo
es compatible con la cláusula O4 de `OBJECT_SPEC.md` si Π(E,K) = {Λ}.

**(5) Línea que se rompe para cΛ y a_P.** No hay paso de signo, luego no hay línea que señalar. Para la
identidad de dos escalas (I2) de §4, que es la única identidad escrita: se rompe para cΛ, c ≠ 1, en el
dato g = μ∗log² (el lado izquierdo de (E2) vale c g + (c² − c)·Λ∗Λ en todo n con (Λ∗Λ)(n) ≠ 0) y para
a_P en el mismo dato en el primer n ≥ 2 con factor primo menor que P; pero la versión con (N_b, μ_b)
propios vale para ambos (Lema S0 de R186_005), y (I2) no contiene ninguna cantidad no negativa. Según
`OBJECT_SPEC.md` §4, la candidata **no está lista para construcción**.

El cotejo no identifica una repetición literal (la clasificación del §3 no figura en el corpus), pero sí
que el diseño constructivo repite SPEC_A y la compensación entre escalas sin positividad por átomo. La
memo continúa sólo para dejar PROVED la clasificación y el enunciado preciso del casillero.

## 1. Preliminares

Para un vector real b = (b(n))_{2 ≤ n < N} y F ∈ P_T ∩ 𝒟_T real,

    w_n(F) = 2 n^{−1/2} c_F(log n),   W[b](F) = Σ_{2 ≤ n < N} b(n) w_n(F),
    𝔪_T(F) = (1/2π) ∫ m |F̂|² dτ,    a_T^b(F) = 𝔪_T(F) − W[b](F),

de modo que a_T = a_T^Λ. Para todo F, la aplicación b ↦ a_T^b(F) es afín.

**Lema 1 (átomos de prueba). PROVED.** Sea 2 ≤ n_0 < N, ε ∈ {+1, −1}. Existe F ∈ P_T ∩ C_c^∞(I_T) real,
F ≠ 0, con w_{n_0}(F) = 2 ε n_0^{−1/2}‖φ‖² ≠ 0 y w_n(F) = 0 para todo n ≠ n_0, 2 ≤ n < N.

*Demostración.* Sea u = log n_0 ∈ (0, 2T) y η > 0 con u/2 + η < T y 2η < min(log 2, 1/N). Sea φ real, C^∞,
no nula, con soporte en (−η, η) y A(φ) = B(φ) = 0 (dos condiciones lineales en un espacio de dimensión
infinita). Póngase F(t) = φ(t + u/2) + ε φ(t − u/2). Entonces A(F) = (e^{−u/4} + ε e^{u/4}) A(φ) = 0, y lo
mismo para B; el soporte de F está en I_T. Además
c_F(s) = 2 c_φ(s) + ε c_φ(s − u) + ε c_φ(s + u), y c_φ tiene soporte en (−2η, 2η). Para 2 ≤ n < N,
log n ≥ log 2 > 2η, log n + u > 2η, y, si n ≠ n_0, |log n − u| ≥ log(1 + 1/m) > 1/(m+1) > 1/N > 2η con m = min(n, n_0) (pues m + 1 < N). Luego
c_F(log n) = ε c_φ(0) = ε‖φ‖² si n = n_0 y 0 en otro caso. ∎

**Corolario 1 (independencia). PROVED.** Si δ es un vector real sobre [2,N) y W[δ](F) = 0 para todo
F ∈ P_T ∩ 𝒟_T, entonces δ = 0. Si δ ≠ 0 existe F con W[δ](F) > 0.

*Demostración.* Con δ(n_0) ≠ 0 y ε = signo de δ(n_0), el Lema 1 da W[δ](F) = 2 |δ(n_0)| n_0^{−1/2} ‖φ‖² > 0. ∎

## 2. El grado en Λ no es visible para la forma

Sea R = ℝ[x_n : 2 ≤ n < N] y, para 2 ≤ n < N, el átomo de completitud

    κ_n(x) = Σ_{d | n, d ≥ 2} x_d − log n      (polinomio afín-lineal).

**Lema A. PROVED.** (i) El ideal (κ_n : 2 ≤ n < N) es el ideal maximal del punto Λ: coincide con
(x_n − Λ(n) : 2 ≤ n < N). (ii) En consecuencia, todo polinomio P ∈ R con P(Λ) = 0, de cualquier grado,
es combinación con coeficientes en R de los átomos lineales κ_n. (iii) Para E ⊂ [2,N) ∩ ℕ, el ideal
I_E = (κ_n : n ∈ E) es primo y es el ideal de todos los polinomios que se anulan en el subespacio afín
V(E) = {x : κ_n(x) = 0, n ∈ E}.

*Demostración.* (i) Por inversión de Möbius sobre el retículo de divisores,
x_n − Λ(n) = Σ_{d | n, d ≥ 2} μ(n/d) κ_d(x), usando Σ_{d|n} μ(n/d) log d = Λ(n); y κ_n = Σ_{d|n, d≥2}
(x_d − Λ(d)). (ii) Un polinomio que se anula en un punto pertenece al ideal maximal de ese punto.
(iii) El sistema lineal κ_n = 0, n ∈ E, es compatible (Λ lo resuelve); tras un cambio afín de coordenadas
I_E = (y_1, …, y_r), que es primo y es el ideal de anulación de {y_1 = … = y_r = 0}. ∎

Lectura. La identidad de grado dos Λ·log + Λ∗Λ = μ∗log², y cualquier otra relación polinómica entre los
valores Λ(n), n < N, no añade información a los átomos lineales; lo único que distingue una relación de
otra es el conjunto E de átomos del que es consecuencia. Y como a_T^b(F) es afín en b, sustituir una
relación polinómica en el término del peine reescribe W[Λ] como W[b′] con b′ = Λ: la forma sólo recibe el
vector de pesos. Una no linealidad en Λ que decida el signo tiene que estar en el acoplamiento de Λ con F
(en V_T F), no en una relación entre los pesos.

## 3. Clasificación de la completitud parcial

**Clase.** Sea E ⊂ [X, N) ∩ ℕ y K ⊂ ℝ^{[2,N)} convexo cerrado con Λ ∈ K. Se definen

    D(E) = {δ : δ(n) = 0 para n < X,  Σ_{d | n} δ(d) = 0 para todo n ∈ E}      (subespacio lineal),
    Π(E,K) = {λ ∈ K : λ = Λ en [2,X),  Σ_{d | n, d ≥ 2} λ(d) = log n para todo n ∈ E} = (Λ + D(E)) ∩ K.

Π es el conjunto de peines que comparten con Λ los datos de la escala X, la completitud en E y las
propiedades K. El enunciado asociado es

    (MS_{X,N,E,K})    a_T^λ(F) ≥ 0   para todo λ ∈ Π(E,K) y todo F ∈ P_T ∩ 𝒟_T.

**Principio de transferencia. PROVED.** Toda deducción de «a_T^Λ ≥ 0 sobre P_T» cuyas únicas premisas
sobre el peine sean: sus valores en [2,X), los átomos κ_n = 0 con n ∈ E y la pertenencia a K, demuestra
(MS_{X,N,E,K}). En particular, si V^x y ρ^x dependen polinómicamente de x, ρ^x(F) ≥ 0 para x ∈ K, y para
cada F el polinomio a_T^x(F) − ‖V^x F‖² − ρ^x(F) pertenece a I_{[2,X) ∪ E}, entonces vale
(MS_{X,N,E,K}).

*Demostración.* Las premisas valen para todo λ ∈ Π. En el caso polinómico, por el Lema A(iii) la
identidad vale en todo punto de V([2,X) ∪ E) = Λ + D(E), y en los puntos de K el lado derecho es ≥ 0. ∎

Para F fijo sea h_Π(F) = sup_{λ ∈ Π} W[λ − Λ](F) ∈ [0, +∞].

**Teorema B. PROVED.**
(i) (MS_{X,N,E,K}) equivale a:  a_T(F) ≥ h_Π(F) para todo F ∈ P_T ∩ 𝒟_T.
(ii) Si Π no es acotado, (MS_{X,N,E,K}) es falso: existen λ ∈ Π y F ∈ P_T con a_T^λ(F) < 0. Esto no usa
ninguna hipótesis sobre el signo de λ_A.
(iii) h_Π ≡ 0 sobre P_T ∩ 𝒟_T si y sólo si Π = {Λ}. En ese caso (MS_{X,N,E,K}) es literalmente (★) en la
ventana T.
(iv) Si Π es acotado y Π ≠ {Λ}, (MS_{X,N,E,K}) equivale a la positividad de a_T^λ en los puntos extremos
λ de Π, implica (★) en T y es estrictamente más fuerte en el sentido siguiente: existe F ∈ P_T con
h_Π(F) > 0, y para todo segmento [Λ − sδ, Λ + sδ] ⊂ Π (s > 0) y todos F, G ∈ P_T ∩ 𝒟_T reales,

    s |W[δ](F)| ≤ a_T(F),        s |W[δ](F,G)| ≤ 2 (a_T(F) a_T(G))^{1/2},

donde W[δ](F,G) es la forma bilineal simétrica de W[δ].

*Demostración.* (i) a_T^λ(F) = a_T(F) − W[λ − Λ](F); tomar el ínfimo en λ ∈ Π.
(ii) Π es convexo, cerrado y no acotado, luego tiene una dirección de recesión δ ≠ 0: Λ + sδ ∈ Π para
todo s ≥ 0. Por el Corolario 1 hay F ∈ P_T ∩ C_c^∞ con W[δ](F) > 0, y
a_T^{Λ+sδ}(F) = a_T(F) − s W[δ](F) < 0 para s > a_T(F)/W[δ](F) (a_T(F) es finito).
(iii) Si λ ∈ Π, λ ≠ Λ, el Corolario 1 aplicado a δ = λ − Λ da h_Π(F) ≥ W[δ](F) > 0 para algún F. El
recíproco es trivial, y entonces (i) es (★).
(iv) Para F fijo, λ ↦ a_T^λ(F) es afín y Π es convexo compacto, luego su mínimo se alcanza en un punto
extremo. Λ ∈ Π da (★). La existencia de F con h_Π(F) > 0 es (iii). La primera desigualdad es (i) con
λ = Λ ± sδ. Para la segunda, q_± = a_T ± s W[δ] son formas no negativas sobre P_T ∩ 𝒟_T con q_± ≤ 2a_T;
de 2s W[δ](F,G) = q_+(F,G) − q_−(F,G) y Cauchy–Schwarz para cada q_± sale
2s |W[δ](F,G)| ≤ 2·(2a_T(F))^{1/2}(2a_T(G))^{1/2}. ∎

**Caso de las restricciones clásicas.** Sea K_0 = {λ ≥ 0, λ(n) = 0 si n no es potencia de primo}. Sea
Div(E) el conjunto de divisores de elementos de E.

**Corolario C. PROVED.**
(a) Π(E,K_0) no es acotado si y sólo si alguna potencia de primo q ∈ [X,N) no divide a ningún elemento de
E. En ese caso Λ + c·1_{n=q} ∈ Π(E,K_0) para todo c ≥ −Λ(q) y (MS) es falso. En particular (MS) es
falso salvo que E contenga todas las potencias de primo de [N/2, N), y, para cada j ≥ 1 y cada potencia
de primo q ∈ [N/(j+1), N/j), alguno de q, 2q, …, jq.
(b) Supóngase N ≤ X². Para cada primo p sea 𝒯_p = {j : X ≤ p^j < N} y
J_p(E) = {v_p(n) : n ∈ E, p^{v_p(n)} ≥ X}. Entonces Π(E,K_0) = {Λ} si y sólo si 𝒯_p ⊂ J_p(E) para todo p;
es decir, si y sólo si para cada potencia de primo q = p^j ∈ [X,N) hay n ∈ E con p^j ∥ n.
(c) Si N ≤ X², toda potencia de primo de [X,N) divide a un elemento de E, y algún nivel j ∈ 𝒯_p falta en
J_p(E), entonces Π(E,K_0) es un politopo acotado, producto de politopos indexados por primos p < N^{1/2},
con Λ en su interior relativo. Ejemplo mínimo: 𝒯_p = {a, a+1}, J_p = {a+1}; Π contiene el segmento
λ_s = Λ + s(1_{n=p^a} − 1_{n=p^{a+1}}), |s| ≤ log p, y (MS) contiene la desigualdad

    a_T(F) ≥ 2 log p · | p^{−a/2} c_F(a log p) − p^{−(a+1)/2} c_F((a+1) log p) |   para todo F ∈ P_T.

*Demostración.* (a) El cono de recesión de Π es D(E) ∩ K_0. Si δ ≥ 0 y Σ_{d|n} δ(d) = 0 con n ∈ E, entonces
δ(d) = 0 para todo d | n; luego D(E) ∩ K_0 = {δ ≥ 0 con soporte en potencias de primo de [X,N) ∖ Div(E)}.
Si q ∉ Div(E), ningún átomo con n ∈ E contiene la variable x_q y Λ + c·1_{n=q} ∈ Π para c ≥ −Λ(q);
Teorema B(ii). Un múltiplo de q menor que N es uno de q, 2q, …, jq cuando q ≥ N/(j+1).
(b) Las direcciones admisibles en Λ dentro de K_0 son los δ ∈ D(E) con soporte en potencias de primo
(ambos signos, pues Λ(q) > 0), y Π = {Λ} si y sólo si no hay ninguna no nula. Si n < N ≤ X² tuviera
divisores p^i ≥ X y p′^{i′} ≥ X con p ≠ p′, sería n ≥ X². Luego para n ∈ E las potencias de primo
≥ X que dividen a n son potencias de un solo primo p, a saber p^i con i ∈ 𝒯_p, i ≤ v_p(n), y el átomo en
n es la ecuación Σ_{i ∈ 𝒯_p, i ≤ v_p(n)} δ(p^i) = 0 (vacía si p^{v_p(n)} < X para todo p). El sistema se
desacopla por primos, y sobre la torre de p dice que las sumas parciales S_j = Σ_{i ∈ 𝒯_p, i ≤ j} δ(p^i)
se anulan para j ∈ J_p(E). Tiene sólo la solución nula si y sólo si J_p(E) ⊃ 𝒯_p.
(c) Por (a) Π es acotado; por (b) no se reduce a Λ y las direcciones son sumas de direcciones de torre;
una torre con un solo nivel está cubierta por la hipótesis de divisibilidad, luego sólo intervienen
primos con p² < N. En el ejemplo, la única ecuación es δ(p^a) + δ(p^{a+1}) = 0 y λ_s ≥ 0 equivale a
|s| ≤ log p; la desigualdad es el Teorema B(iv). ∎

**Observación 1 (variante con átomos N_λ(n) = 1). PROVED en lo que se enuncia.** R186_005 usa el átomo
N_λ(n) = 1, con N_λ dada por N_λ(1) = 1, N_λ(n) log n = Σ_{d|n, d≥2} λ(d) N_λ(n/d). Por inducción en n,
N_λ(n) depende sólo de los λ(d) con d | n; luego si q ∉ Div(E) el átomo λ(q) queda libre y vale el
Corolario C(a) sin cambios. Si E es cerrado por divisores las dos nociones coinciden (la recursión con
N_λ ≡ 1 en los divisores es el átomo lineal). Para N > X² las variedades difieren y la versión N_λ es
peor: con primos q_1 ≠ q_2 en [X, N^{1/2}) y E = {q_1 q_2}, dentro de K_0 se tiene
N_λ(q_1 q_2) = (λ(q_1)/log q_1)(λ(q_2)/log q_2), y la clase contiene la hipérbola λ(q_1) = t log q_1,
λ(q_2) = t^{−1} log q_2, t > 0, no acotada; el argumento del Teorema B(ii) con el Lema 1 en n_0 = q_1 da
un miembro con forma negativa.

**Observación 2 (primer acoplamiento entre contactos nuevos distintos). PROVED.** Con átomos lineales y
K_0, un átomo acopla dos primos nuevos distintos sólo si N > X² y n es múltiplo de un producto q_1 q_2 de
potencias de primos distintos de [X,N): la ecuación es δ(q_1) + δ(q_2) + … = 0. Para E formado por
semiprimos q_i q_j (primos q_i ∈ [X, N^{1/2})), D(E) ∩ {soporte en los q_i} es el espacio de funciones
alternantes sobre el grafo de aristas {i,j}: nulo en las componentes con un ciclo impar, de dimensión
uno en las bipartitas. Así, incluso donde la completitud parcial es genuinamente multiescala, la
alternativa sigue siendo identificación o politopo.

**Estado del caso (iv)/(c).** CONDITIONAL NO-GO. Por el Teorema B(iv), (MS) obliga a que
s|W[δ](F)| ≤ a_T(F) en todo P_T. Si existe un minimizador unitario real F_⋆ de a_T en P_T con
W[δ](F_⋆) ≠ 0 y λ_A(T) < s |W[δ](F_⋆)|, (MS) es falso; por P47 cor:margin1 (CITED) basta, para T ≥ 1,
s|W[δ](F_⋆)| > 4·10⁹ T e^{−15.449T}. Es la misma hipótesis no verificada que hace condicional a
P47 thm:shape (A′) para la amplificación de un término. Sin ella, (MS) queda como un enunciado OPEN
estrictamente más fuerte que (★) en T, y por P47 thm:geo-split (CITED) su contenido de signo es el signo
en Λ: la parte añadida es rigidez, no mecanismo.

**Conclusión del §3. NO-GO (clase), PROVED en los casos (ii)/(a) y (iii)/(b), CONDITIONAL en (iv)/(c).**
Clase: deducciones cuyas premisas sobre el peine son datos en [2,X), átomos lineales de completitud en un
E ⊂ [X,N) y pertenencia a un convexo cerrado K. Dentro de esa clase «completitud parcial más allá de X»
no es un mecanismo: o es falsa como fuente de positividad, o es identificación total (y entonces la clase
no restringe nada: por el Lema A(ii) toda igualdad polinómica cierta en Λ es derivable), o exige un
margen. La cláusula O4 de `OBJECT_SPEC.md` (la identidad es falsa para todo otro peine) equivale, para
una identidad de esta clase, a Π(E,K) = {Λ}.

## 4. La identidad de dos escalas de grado dos, escrita

Sea g = μ∗log² (función de los enteros). Se escribe Λ_< = Λ·1_{[2,X)}, Λ_≥ = Λ·1_{[X,N)}.

**Proposición D. PROVED.** Supóngase N ≤ X². Para X ≤ n < N,

    (E2)   Λ(n) log n + 2 Σ_{k | n, 2 ≤ k ≤ n/X} Λ(k) Λ(n/k) = g(n) − Σ_{km = n; k,m < X} Λ(k) Λ(m).

El operador (𝖳f)(n) = f(n) log n + 2 Σ_{k | n, 2 ≤ k ≤ n/X} Λ(k) f(n/k) sobre funciones en [X,N) es
triangular con diagonal log n > 0 y coeficientes Λ(k), k < N/X ≤ X, de la ventana vieja. Por tanto
Λ_≥ = 𝖳^{−1}[(g − Λ_<∗Λ_<)|_{[X,N)}] y, para todo F ∈ P_T ∩ 𝒟_T,

    (I2)   a_T(F) = a_T^{Λ_<}(F) − W[ 𝖳^{−1}((g − Λ_<∗Λ_<)|_{[X,N)}) ](F).

(I2) es lineal en el dato nuevo g|_{[X,N)}. Si N > X² aparece además en (E2) el término
Σ_{km=n; k,m ≥ X} Λ(k)Λ(m), que es el primer término cuadrático en contactos nuevos; es no nulo sólo en
n = q_1 q_2 con q_1, q_2 potencias de primo ≥ X, donde Λ(n) log n = 0 salvo que n sea potencia de primo.

*Demostración.* La identidad de grado dos Λ(n) log n + (Λ∗Λ)(n) = g(n) (coeficientes de ζ″/ζ = (ζ′/ζ)′ +
(ζ′/ζ)², o directamente de Λ∗1 = log) se separa según los pares (k,m), km = n: ambos < X; exactamente uno
≥ X (entonces el otro es ≤ n/X < N/X ≤ X), contado dos veces; ambos ≥ X, imposible si n < X². Esto da (E2);
𝖳 es triangular respecto del orden de n porque n/k < n. (I2) es a_T = a_T^{Λ_<} − W[Λ_≥]. ∎

**Lo que (I2) no da. PROVED.** (1) No contiene ninguna cantidad manifiestamente no negativa: por el
Lema 1, W[b] es una forma indefinida sobre P_T para todo b ≠ 0, y a_T^{Λ_<} no está controlada por la
positividad en T_0, que sólo dice a_{T_0}(F) ≥ 0 para F con soporte en I_{T_0}. (2) Es genérica en el
peine: por el Lema S0 de R186_005 (CITED) la misma identidad vale para todo b con g_b = μ_b∗(N_b log²);
lo no genérico es g_b = μ∗log² en [X,N), que por la invertibilidad de 𝖳 equivale a b = Λ en [X,N):
identificación total, caso (iii) del Teorema B. (3) Por el Lema A, (I2) es la reescritura W[Λ_≥] =
W[𝖳^{−1}(…)] de un mismo vector de pesos: la forma no distingue el miembro izquierdo del derecho. Cae en
el patrón B1 de `RULES_AVOID.md` (identidad válida para todo peine) más el patrón B3 (reformulación).

La variante «copias escaladas por divisores» (Λ = μ∗log sustituida en el peine) es
W[Λ](F) = Σ_{k<N} μ(k) Σ_{n<N/k} log n · 2(kn)^{−1/2} c_F(log k + log n): es la forma sobre el retículo
de enteros con el peine colapsado, registrada como SPEC_B T*₃ en IDX README (fase 191) y como «matrices
de retículo entero (reformulación)» en `RULES_AVOID.md` §C. No se reintenta.

## 5. Respuesta a los fallos registrados

| Fallo registrado | ¿El diseño difiere? | Motivo |
|---|---|---|
| Compensación entre escalas sin positividad por átomo; telescopado sin cota nueva del resto (memoria de las reglas del proyecto; 211 `POWER_DESCENT_016` §§2–4, `POWER_RECURRENCE_BOUNDARY_036` §§5–7) | No | El incremento entre escalas es −W[Λ_≥], forma indefinida (Lema 1); (I2) lo reescribe sin firmarlo. No hay cota nueva del resto. |
| «No hay inducción hacia arriba en T, no hay Grönwall» (CW I15, I16) | No | La positividad en T_0 no controla a_T^{Λ_<} fuera de las funciones con soporte en I_{T_0}; la recursión X → X² es una inducción hacia arriba. |
| SPEC_A, inducción exacta por contactos (IDX README, fase 191) | No | El paso X → N hereda el margen completo de la ventana N; el Teorema B(iv) muestra además que cualquier relajación del paso a una clase mayor que {Λ} pide margen, que es lo que SPEC_A no tenía. |
| P47 thm:geo-split y barrera defecto/continuación (fase 197) | No | El Teorema B(i),(iv) es una instancia: positividad sobre Π = signo en Λ + rigidez h_Π sin signo. |
| Escalera jerárquica de contactos (P48 tab:signobject: genérica en el peine) | No | (I2) es genérica por el Lema S0. |
| Circularidad PROVED para tests únicos y familias de potencias (IDX 06 R7) | Distinto alcance, no la evita | El §3 trata desigualdades de grado arbitrario, pero sólo las derivables de completitud parcial lineal más K; no extiende el teorema registrado a toda B no lineal. |
| 211 LEDGER C45/C47 (ℕ en el borde derecho del segmento positivo; sin palanca variacional) | No | Coherente con el Teorema B(iv): un politopo Π con Λ en su interior relativo pide positividad a ambos lados de Λ. |

Ninguna de las diferencias evita el motivo registrado del fracaso. Conforme a la instrucción, la
construcción se detiene aquí.

## 6. Batería de falsificadores

No hay paso de signo que someter. Para las clases Π(E,K_0) del §3: borrado y amplificación finitos están
en Π si y sólo si el átomo modificado está fuera de Div(E) (Corolario C(a)); cΛ con c ≠ 1 y a_P no están
en Π porque violan los datos en [2,X) (y, si se retiran esos datos, violan cada átomo κ_n, n ∈ E, pues
c log n ≠ log n); b_θ = Λ·½(1 + cos(γ log n + ϑ)) está en Π sólo si coincide con Λ en Div(E) ∩ potencias
de primo. Los modelos de cuarteto y f_t conservan los valores Λ(n) de la ventana: satisfacen todo átomo
κ_n con n < N (respectivamente n < λ_1), de modo que ninguna premisa de completitud, parcial o total, los
separa; cualquier objeto tendría que romperlos en una línea que use el factor arquimediano, y esta memo
no aporta esa línea. Davenport–Heilbronn, Epstein y los sistemas de Beurling violan los átomos en cuanto
E contiene un entero donde su peine difiere de Λ.

## 7. Enunciado preciso de lo que el casillero pide

Tras el §3, «completitud parcial más allá de X» sólo puede significar una de dos cosas.

**(P1) Identificación total con no linealidad en el acoplamiento.** Un objeto (ℋ_T, V_T, ρ_T) con V_T
polinómico en los pesos, tal que el lugar de la identidad

    Z_T = {x ∈ K : a_T^x(F) = ‖V_T^x F‖² + ρ_T^x(F) para todo F ∈ P_T ∩ 𝒟_T}

sea Z_T = {Λ|_{[2,N)}} para todo T. Por el principio de transferencia y el Teorema B esto es necesario si
no se quiere pagar margen: (★) para todo T se sigue de (G) si y sólo si Λ ∈ Z_T, y la positividad se
transfiere a todo Z_T, luego a_T(F) ≥ sup_{x ∈ Z_T} W[x − Λ](F). La no linealidad no puede estar en una
relación entre los pesos (Lema A): tiene que estar en V_T^x F como función conjunta de x y F. Estado:
OPEN, sin candidata; es la cláusula O2 ∧ O4 de `OBJECT_SPEC.md`, no un enunciado más débil.

**(P2) Desigualdad con margen sobre un politopo.** Para algún (X, N, E, K) con Π(E,K) acotado y ≠ {Λ}:

    para todo F ∈ P_T ∩ 𝒟_T:   a_T(F) ≥ max_{λ extremo de Π(E,K)} W[λ − Λ](F).

Es estrictamente más fuerte que (★) en T; CONDITIONAL NO-GO (§3). No es un objetivo razonable.

No existe una tercera lectura dentro de la clase de átomos lineales con restricciones convexas. Fuera de
ella (restricciones no convexas sobre el peine, por ejemplo integralidad de multiplicidades, o premisas
que no son propiedades del peine en [2,N)) esta memo no afirma nada.

## 8. Cierre

**Resultado.** Sin mecanismo nuevo. Pieza PROVED: clasificación de la completitud parcial (Teorema B,
Corolario C) y linealidad de la identidad de dos escalas para N ≤ X² (Proposición D). NO-GO con clase:
deducciones desde datos en [2,X), átomos lineales de completitud en E ⊊ generador y un convexo cerrado K
— PROVED cuando Π no es acotado, CONDITIONAL cuando Π es un politopo no trivial.

**Qué se probó.** Lema 1 y Corolario 1 (átomos de prueba; independencia de los funcionales
F ↦ c_F(log n) sobre P_T). Lema A (todo hecho polinómico sobre Λ en [2,N) es consecuencia de los átomos
lineales; I_E es el ideal de un subespacio afín). Principio de transferencia. Teorema B. Corolario C
(criterio en términos de divisores y valuaciones exactas para N ≤ X²). Observaciones 1 y 2 (variante
N_λ; grafo de semiprimos para N > X²). Proposición D.

**Qué falló y por qué.** No se pudo escribir (ℋ_T, V_T, ρ_T): la única fuente de no linealidad propuesta
(Λ·log + Λ∗Λ = μ∗log² a dos escalas) es lineal en los contactos nuevos para N ≤ X², es genérica en el
peine salvo por la identificación total, y la forma, afín en el peine, no ve el grado. El incremento
entre escalas −W[Λ_≥] no tiene signo y ninguna identidad escrita lo firma. El caso (iv) del Teorema B no
se pudo cerrar sin la hipótesis W[δ](F_⋆) ≠ 0 sobre un minimizador.

**Siguiente paso concreto.** (1) Anotar en IDX 06 R7 y en GRID §8 que la dirección «completitud parcial
más allá de X» queda clasificada (este archivo, §3) y que el residuo vivo de R7 es (P1). (2) Si se quiere
cerrar el caso (iv): probar o refutar, para el segmento de torre del Corolario C(c) con p = 2, que existe
F ∈ P_T con a_T(F) < 2 log 2 · |2^{−a/2} c_F(a log 2) − 2^{−(a+1)/2} c_F((a+1) log 2)|; es una pregunta
sobre una forma explícita de dos átomos. (3) Para (P1), la única pieza del registro que acopla pesos y
vector en un mismo paso es la identidad finita de Poisson–Chebyshev (P47 thm:PCfinite), que corresponde a
la candidata K1; K4 no aporta un objeto independiente de ella.
