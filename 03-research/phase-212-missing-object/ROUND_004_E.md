# ROUND_004_E — Selección: formas indefinidas (Kreĭn/Pontryagin) con vector neutro no radical

Memo de selección, no de construcción. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md` y de
P47 §sec:complete; N = e^{2T}. 𝔪_T(F) = (1/2π)∫m|F̂|² (forma arquimediana, peine borrado; en P47 𝒜_∞ sobre
P_T), Π_T(F) = −Σ_{n<N} v_n Re c_F(log n), a_T = 𝔪_T + Π_T, W_T = a_T + 2Re(A B̄) (forma completa con
término polar). Para un peso a se escribe a_T^{(a)}; para cΛ, a_T^{(c)} = 𝔪_T + cΠ_T. n_-(q|V) es la
mayor dimensión de un subespacio de V ∩ 𝒟_T donde q < 0. Etiquetas: PROVED / CITED / CONDITIONAL /
ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

### Búsqueda realizada

- Lectura entera: `BRIEF_CONSTRUCTOR.md`, `README.md`, `RULES_AVOID.md`, `OBJECT_SPEC.md`, `LEDGER.md`,
  `REVIEW_003.md`, `ROUND_003_4.md`, `STATEMENT_001.md`.
- P47 en primaria: §sec:complete entero (lem:Onat, thm:Al, thm:parityschur, prop:polarcap y el párrafo
  que sigue); thm:index, cor:Tarch, prop:NC, cor:P3, thm:J, cor:nasym, cor:H1 y observaciones
  (l. 2420–2780); §sec:inertia (thm:inertia-finite, thm:inertia-quartet, thm:inertia-rank,
  §subsec:inertia-excl «Inertia alone (conditional)»); lem:polar; enunciado de thm:coer-schur;
  enunciado de cor:convfail.
- grep en `03-research/` (todas las fases), P47, P48 y `05-meta-and-planning/` por «Pontryagin»,
  «Krein–Langer», «generalized Nevanlinna», «N_κ», «Π_κ», «Kreĭn signature», «firma de Kreĭn»,
  «negative squares», «n_-», «inertia», «polar capacity». Abiertos (cabecera y sección central):
  `phase-197-barrier-theorem/BARRIER_W_001_…NO_GO.md` §§0–4; `phase-16-surf-witness-variety/
  07-pontryagin-the-indefinite-object.md`; `phase-186-toolbox/R186_004_KREIN_FLOW_FIRST_THRESHOLD.md`;
  `phase-162-…/R162_1301_KREIN_JORDAN.md` §0.
- Fase 170 y 161: R170_854 sólo por grep en primaria (líneas 236, 372, 410: «toda completación por
  cuadrados es indefinida», (3.4)) y por `ANNEX_170_FILES_3.md` (entradas 854, 861, 862); R161_032 sólo
  por grep ((4.2) en l. 114, «OPEN / TERMINAL» en l. 146); R161_023, 061–063 sólo por
  `ANNEX_161_FILES_3.md` y `RULES_AVOID.md` §K4. R170_866–870 sólo por `ROUND_003_4.md` y §I1–I3.
- No abiertos: las memos de la fase 156 (per-window converse; su contenido está en P47 thm:parityschur y
  prop:polarcap, que sí leí); la ronda 5 de la fase 155 («Kreĭn indeterminacy»); las memos de las fases
  15/16 distintas de la 07; `POLAR_CAP_001` (citado en 211 ROUND_008_A l. 26 como «bordered Schur
  complement that inverts a_T|P_T itself — consumes λ_A > 0»; no hay archivo con ese nombre); el ledger
  y las memos de la ronda 21 de la 211 salvo la fila C43 de `LEDGER.md`.

### (1) Antecedente más cercano

- **P47 thm:parityschur (a1)–(a2), (c) y prop:polarcap.** Es exactamente el formato de Pontryagin del
  encargo, ya escrito y PROVED: n_-(W_T) = n_-(a_T|P_T) + n_-(𝔊_T), 𝔊_T = S^Sch_T + diag(2, −2), con
  S^Sch_T la compresión de a_T al a_T-ortogonal de P_T (complemento de Schur sobre P_T), y la lectura
  «capacidad polar» E_T(β, α). El párrafo siguiente reduce el recíproco por ventana a dos signos.
- **P47 §subsec:inertia-excl, «Inertia alone (conditional)».** Exclusión condicional de la clase
  «descomposición a_T = 𝔪_T − C_ε + Π_T + propiedades estables por rango finito + aritmética de inercia
  (Sylvester, Haynsworth, entrelazado, lem:monoT)», mediante thm:inertia-rank.
- **Fase 197, BARRIER_W_001 Teor. W1–W3** (PROVED en la memo): el índice n_-(a_T|P_T) es monótono en T,
  todos los cruces tienen el mismo signo de Kreĭn; «índice constante» equivale al objetivo; la
  codimensión de von Neumann–Wigner no da nada.
- **RULES_AVOID §C1** registra «coercividad, Schur, inercia, Wiener–Hopf … como fuente de signo» y
  «defecto/continuación, índice de Morse, firma de Kreĭn» entre las familias cerradas; §K4 registra que en
  la fase 161 ninguna memo estudia un vector neutro no radical; R3-c (`ROUND_003_4.md` Lema 1) deja
  fuera de su clase las formas indefinidas.
- **Fase 16, memo 07; R162_1301 §0:** espacios de Pontryagin cuyo índice cuenta datos espectrales
  externos al sandbox; registrados allí como detectores, no como fuentes de signo. No se usan aquí.

### (2) Objeto realmente nuevo

Ninguno con mecanismo. Lo que sí es nuevo respecto del corpus son cinco lemas cortos (§2), todos sin
signo, que cierran la zona tal como el encargo la formula:

- la resolución de la tensión «κ(T) > 2» (Prop. 1): los conteos que crecen con T son de 𝔪_T, no de
  a_T; bajo el objetivo, n_-(a_T|L²(I_T)) ≤ 2 para todo T;
- toda cota superior de un índice negativo es una positividad sobre un subespacio de codimensión
  finita (Lema 2): «inercia en lugar de desigualdad» no existe como alternativa;
- un vector neutro dentro de un subespacio no negativo es radical allí (Lema 3), y un vector neutro
  cuyo componente de coeficientes pasa por las filas de 𝒟_N es radical en cualquier signatura
  (Lema 4);
- en cada ventana con λ_A(T) > 0 todos los índices del formato son constantes en c cerca de 1
  (Lema 5), y sus saltos están exactamente en los extremos de la ventana de positividad en c (Lema 6):
  un argumento de inercia no cumple O4 en ninguna ventana fija y sólo lee el signo a través de un
  valor.

No escribo ℋ_T, V_T ni ρ_T: el formato de Kreĭn, en todas sus lecturas examinadas, se reduce a
thm:parityschur/prop:polarcap (ya en P47), a thm:coer-schur (L2), o a (G) con otra inmersión.

### (3) ¿Evita la dificultad del antecedente?

No. La dificultad de prop:polarcap es que, dado WP_T, el signo de W_T es el de dos números
𝔤_ev, 𝔤_odd que nadie controla, y que el recíproco falla para pesos modificados (cor:convfail). El formato
de Pontryagin pedido (positividad sobre P_T ⟺ la matriz 2×2 de la forma inversa sobre los vectores de
Tate tiene tantos autovalores negativos como cuadrados negativos tiene la forma ambiente) es la misma
identidad de inercia con a_T en lugar de W_T (Prop. 1(b)), y exige conocer dos enteros que sólo se
conocen calculando valores (Lemas 2 y 6). El vector neutro no radical no cambia esto (Lemas 3 y 4).

### (4) Conexión con la positividad global

La identidad que conecta es exacta y ya conocida: para el operador Q de a_T sobre L²(I_T), si 0 no está
en el espectro de Q ni de a_T|P_T,

    n_-(a_T|P_T) = n_-(a_T|L²) − n_-(Γ_T),   Γ_T = [⟨Q^{-1}χ_i, χ_j⟩]_{i,j}, χ_{1,2} = e^{±t/2}1_{I_T},

(Prop. 1(c)). (★) en T es «n_-(a_T|L²) = n_-(Γ_T)». Ninguno de los dos enteros se conoce sin el signo.

### (5) cΛ y a_P: por qué el resto deja de ser ≥ 0

No hay resto: un argumento de inercia no tiene término que deje de ser ≥ 0; tiene enteros. El Lema 5
prueba que en cada ventana con λ_A(T) > 0 los enteros no cambian en un entorno de c = 1, de modo que la
cuenta es la misma para cΛ con |c − 1| pequeño: no hay línea que se rompa en c ≠ 1 cerca de 1. El
Lema 6 dice dónde se rompe: en c_±(T), los ceros de c ↦ λ_A(T; c). Para a_P vale lo mismo con la
homotopía Λ + s(a_P − Λ). La ventana de 211 LEDGER C43 que se cierra sobre c = 1 por ambos lados
(NUMÉRICO, formas de celda R = 2…8) es compatible con la cuenta sólo como degeneración en el límite
T → ∞ de los puntos de salto c_±(T), y esos puntos son información de valor (§3).

## 1. Respuesta a la pregunta (i): cuántos cuadrados negativos y de qué forma

| Forma | Espacio | n_- | Fuente |
|---|---|---|---|
| 𝔪_T (sin peine) | L²(I_T) | ≥ ⌈2Tτ_0/π⌉ − 1; ≤ 5, 7, 8 en ½log3, log 2, 0.80; ~ 4.0042 T | P47 thm:J, cor:P3, cor:nasym (CITED) |
| 𝔪_T | P_T | ≥ ⌈2Tτ_0/π⌉ − 3; = 0, 1, 2 hasta 0.90; ~ 4.0042 T | P47 thm:J, thm:index, cor:nasym (CITED; thm:index con verificación por intervalos) |
| a_T (con peine) | L²(I_T) | finito para cada T | P47 thm:inertia-finite con η = 1, k = 0 (CITED) |
| a_T | P_T | el objetivo es que valga 0 | — |
| W_T | L²(I_T) | n_-(a_T|P_T) + n_-(𝔊_T) | P47 thm:parityschur (c) (CITED) |
| 2Re(AB̄) | L²(I_T) | exactamente 1 (signatura (1,1)) | P47 lem:polar (CITED) |

La tensión aparente se debe a la forma con la que se cuenta. «Theorem P, n_- ≤ 5/7/8» (cor:P3) y el
crecimiento lineal en T (cor:nasym) se refieren a 𝔪_T, la forma arquimediana con el peine borrado. Por
eso cor:Tarch dice que 𝔪_T es negativa en algún vector de P_T para T ≥ 0.60: allí el peine es la
fuente de la positividad, no una perturbación (observación tras cor:Tarch). Para a_T no hay conteo
creciente. Al contrario, bajo el objetivo el conteo está acotado por 2 (Prop. 1(b)).

## 2. Lemas

**Proposición 1 (inercia con borde de Tate).** Fijo T. Sea q = a_T (o W_T) en su dominio 𝒟_T.

(a) (CITED, P47 thm:parityschur (a2), (c).) Si 0 no está en el espectro del operador de a_T|P_T,
n_-(W_T) = n_-(a_T|P_T) + n_-(𝔊_T).

(b) (PROVED.) Con la misma hipótesis y S^Sch_T = diag(a_T(h_ev), a_T(h_odd)),
n_-(a_T|L²(I_T)) = n_-(a_T|P_T) + n_-(S^Sch_T). En particular, si λ_A(T) > 0 entonces
n_-(a_T|L²(I_T)) = n_-(S^Sch_T) ≤ 2.

(c) (PROVED, finito-dimensional; ARGUED en la versión de formas.) Sea Q el operador de a_T en L²(I_T),
con 0 ∉ σ(Q), y sea Γ_T la matriz 2×2 de (b) del Cotejo (4). Si además a_T|P_T no es degenerada, entonces
n_-(a_T|P_T) = n_-(Q) − n_-(Γ_T). Así, a_T|P_T > 0 ⟺ n_-(Γ_T) = n_-(Q), lo que exige n_-(Q) ≤ 2.

*Demostración.* (b) Es la prueba de thm:parityschur (a1)–(a2) con ε_par = 0. Esa prueba sólo usa la
estructura de forma cerrada acotada inferiormente con resolvente compacta, la paridad y el funcional
ℓ_par. En cada sector, 𝒟^par_T = 𝒬^par ⊕ ℝh_par, a_T-ortogonalmente, y
a_T(G + xh_par) = a_T(G) + a_T(h_par)x². Se suma sobre los dos sectores (P47 thm:parityschur (o), que vale
para a_T sin término polar). (c) Matriz con borde M = [[Q, X], [X*, 0]], X = [χ_1, χ_2] de rango 2. Por
Haynsworth respecto de Q: In(M) = In(Q) + In(−X*Q^{-1}X) = In(Q) + In(−Γ_T). Respecto del
subespacio ker X* = P_T: In(M) = In(Q|P_T) + (2, 2, 0) (un borde de rango pleno r añade r cuadrados de
cada signo cuando la restricción no es degenerada). Igualando las cantidades de cuadrados negativos:
n_-(Q|P_T) + 2 = n_-(Q) + n_+(Γ_T), y con Γ_T no singular n_+ = 2 − n_-. En dimensión infinita se
aplica a la descomposición espectral finita de la parte negativa (compacidad de la resolvente). No
reescribo esa reducción: ARGUED. ∎

Lectura: la condición de Pontryagin del encargo («Γ_T ⪯ 0 en la cantidad correcta») es la misma
identidad que prop:polarcap, con a_T en lugar de W_T. Γ_T y S^Sch_T son inversas en coordenadas ℓ (el
complemento de Schur sobre P_T es la inversa de la compresión de Q^{-1} al espacio de los funcionales).
No es objeto nuevo.

**Lema 2 (una cota superior de índice es una positividad).** Sea q una forma hermítica sobre un
espacio E y κ ∈ ℕ. Entonces n_-(q) ≤ κ si y sólo si existe un subespacio U ⊂ E de codimensión ≤ κ con
q ≥ 0 sobre U, en el caso en que q tenga una descomposición espectral con parte negativa
finito-dimensional (formas cerradas acotadas inferiormente con resolvente compacta, como todas las de
este memo).

*Demostración.* (⇐) Si N es un subespacio negativo con dim N > κ, entonces N ∩ U ≠ {0} por
dimensión, y en un vector no nulo de esa intersección q es < 0 y ≥ 0 a la vez. (⇒) Sea E_- la suma de
los autoespacios de autovalor negativo, de dimensión n_-(q) ≤ κ. U = E_-^⊥ ∩ 𝒟 (ortogonal en L²; es
q-ortogonal por ser espacios espectrales) tiene codimensión n_-(q) y q ≥ 0 en U. ∎ PROVED.

Consecuencia: «sacar la positividad de un conteo de signatura y no de una desigualdad» es imposible
en sentido literal. Toda cota superior de un índice negativo que entre en el argumento es una
positividad sobre un subespacio de codimensión finita de alguna forma. La aritmética de inercia
(Sylvester, Haynsworth, perturbación de rango r) sólo transporta esas positividades. Las cotas
inferiores de índice salen de exhibir vectores negativos y no sirven para concluir n_- = 0. Las
positividades de codimensión finita de a_T que el corpus tiene escritas son:

- thm:inertia-finite: positividad en el ortogonal de los autovectores de la limitación tiempo–banda
  con autovalor ≥ A′/(A′ + L);
- thm:coer-schur: coercividad sobre 𝒱_k, de codimensión 2k − 2.

Transportarlas a P_T por Haynsworth deja exactamente un complemento de Schur finito: es (L2),
thm:coer-schur (iii). P47 §subsec:inertia-excl ya lo dice para la primera («the finite structure of
Theorem coer-schur with a larger dimension»).

**Lema 3 (un vector neutro dentro de un subespacio no negativo es radical allí).** Sea 𝔊 hermítica
sobre E, de cualquier signatura, U ⊂ E un subespacio con 𝔊 ≥ 0 sobre U y v ∈ U con 𝔊(v) = 0. Entonces
𝔊(x, v) = 0 para todo x ∈ U y 𝔊(x + v) = 𝔊(x). Recíprocamente, si V es no negativo y v es neutro,
V + ℂv es no negativo sólo si 𝔊(x, v) = 0 para todo x ∈ V con 𝔊(x) = 0. Si V es definido positivo, la
condición es vacía para x ≠ 0, y entonces el criterio exacto es |𝔊(x,v)|² ≤ 0·𝔊(x), es decir, de nuevo
𝔊(x,v) = 0.

*Demostración.* La primera parte es `ROUND_003_4.md` Lema 1 aplicado a 𝔊|_U, que es semidefinida. Para
la recíproca: 𝔊(x + tv) = 𝔊(x) + 2Re(t̄𝔊(x, v)) es ≥ 0 para todo t ∈ ℂ sólo si 𝔊(x, v) = 0, porque el
término en t es lineal y no tiene término cuadrático que lo compense (𝔊(v) = 0). ∎ PROVED.

Consecuencia para el encargo (iii). Que a_T(F) = 𝔊(ι_T F) con ι_T(F) = w_T(F) + ê_T(F),
ê_T(F) = ((Λ,1)⊗F, β_T(F)) neutro, dé a_T ≥ 0 sobre P_T es la afirmación de que el subespacio
ι_T(P_T) es no negativo para 𝔊. Hay dos casos.

- Los ê_T(F) están en un subespacio no negativo que contiene a ι_T(P_T). Entonces el ancla es radical
  allí (Lema 3) y se vuelve a la invisibilidad de R3-c.
- No lo están. Entonces el ancla actúa sólo a través del término cruzado 2Re𝔊(w_T F, ê_T F), que es
  una forma cuadrática más en F dentro de la inmersión ι_T. La no negatividad de ι_T(P_T) es el
  objetivo con otra inmersión: es (G) cuando 𝔊|ι_T(P_T) se escribe como suma de cuadrados, y es una
  reformulación cuando no (B3).

La neutralidad del ancla no fuerza ninguno de los dos casos. Que el vector sea neutro y no radical no
da por sí solo ninguna información de signo sobre el subespacio que se quiere probar no negativo.

**Lema 4 (las filas de 𝒟_N vuelven radical el ancla en cualquier signatura).** Si 𝔊(x, y) = 𝔥(Dx, Dy)
para una aplicación lineal D y una forma sesquilineal 𝔥 cualquiera (indefinida incluida), entonces
ker D está en el radical de 𝔊. PROVED (trivial: 𝔊(x, k) = 𝔥(Dx, 0) = 0).

Con R170_866 (ker 𝒟_N = ℝ(Λ,1), PROVED allí) y R170_867–868 (toda fila lineal que anula (Λ,1)
factoriza por 𝒟_N; RULES_AVOID §I1), resulta lo siguiente. En toda 𝔊 cuya dependencia en la
coordenada de coeficientes pase por filas lineales que anulan (Λ,1), el ancla (Λ,1)⊗F es radical
aunque 𝔊 sea indefinida. Un vector neutro no radical exige que la nulidad de 𝔊 sobre (Λ,1)⊗F sea una
condición cuadrática en el peso que no factoriza por filas. Por O2 (`ROUND_001_D.md` Lema A), esa
condición está en el ideal de los átomos Σ_{d|n}a(d) − log n. Nada en ella indica un signo.

**Lema 5 (los índices son constantes en c cerca de 1 en cada ventana).** Fijo T con λ_A(T) > 0. Sea
V_T := Σ_{n<N} |v_n|. Entonces:

(a) λ_A(T; c) ≥ λ_A(T) − |c − 1|V_T, de modo que n_-(a_T^{(c)}|P_T) = 0 para |c − 1| < λ_A(T)/V_T;

(b) c ↦ a_T^{(c)}(h_par(c)) es continua en ese intervalo. Si a_T(h_par) ≠ 0 en c = 1 para las dos
paridades, n_-(a_T^{(c)}|L²) y n_-(S^Sch_T(c)) son constantes en un entorno de c = 1. Si 𝔤_par ≠ 0 en
c = 1, lo mismo vale para n_-(W_T^{(c)}) y n_-(𝔊_T(c)).

*Demostración.* (a) |Π_T(F)| ≤ V_T‖F‖², porque |c_F(log n)| ≤ ‖F‖² (P47, prueba de thm:parityschur,
«Solvability»). Entonces a_T^{(c)} = a_T + (c − 1)Π_T ≥ (λ_A(T) − |c − 1|V_T)‖·‖² sobre P_T. (b) En el
intervalo de (a), la parte (a3) de thm:parityschur (con ε = 0 para a_T, que es la misma prueba) da
a_T^{(c)}(h_par(c)) = min{a_T^{(c)}(F) : F ∈ 𝒟^par_T, ℓ_par(F) = 1}. Es un ínfimo de funciones afines
en c, luego cóncavo, y es finito en un intervalo abierto, luego continuo. Lo mismo para
𝔤_par(c) = a_T^{(c)}(h_par(c)) + 2ε_par. Un valor no nulo conserva su signo en un entorno. Se concluye
con la Prop. 1(b) y con thm:parityschur (a2). ∎ PROVED.

**Lema 6 (los saltos de la cuenta están en los ceros de λ_A(T; ·)).** Fijo T. J(T) := {c ≥ 0 :
λ_A(T; c) ≥ 0} es un intervalo cerrado; n_-(a_T^{(c)}|P_T) = 0 si y sólo si c ∈ J(T). Supóngase una
identidad de inercia

    n_-(a_T^{(c)}|P_T) = κ(c) − n_-(Γ(c)),

válida en un intervalo de c, con κ(c) y Γ(c) enteros y matrices dadas por una construcción. Si κ es
constante en ese intervalo (por ejemplo, si cuenta cuadrados polares o de Tate, que no dependen de c),
entonces Γ(c) es singular, o la identidad deja de valer, en cada punto c_±(T) de ∂J(T) del
intervalo. Si Γ(c) depende continuamente de c, el signo de Γ(1) se decide por la posición de 1
respecto de c_±(T), es decir, por el signo de λ_A(T; 1).

*Demostración.* λ_A(T; c) es un ínfimo de funciones afines en c: es cóncava y continua (Lema 5(a) da
el módulo), de modo que {≥ 0} es un intervalo cerrado. n_- = 0 ⟺ λ_A ≥ 0 (P47 lem:parity, compacidad
de la resolvente). En c_+(T), el lado izquierdo pasa de 0 a ≥ 1 (λ_A(T; ·) es cóncava y no idénticamente
nula, luego cambia de signo en el extremo, salvo que se anule en todo un intervalo; ese caso se excluye
por la pendiente no nula de `ROUND_003_4.md` Lema 4, ARGUED allí). Con κ constante, n_-(Γ(c)) salta.
Una matriz continua sólo cambia su inercia pasando por una matriz singular. ∎ PROVED salvo el caso
de pendiente nula, que es ARGUED.

## 3. Clase cerrada y respuesta a (iii)–(iv)

NO-GO con clase (PROVED: Lemas 2, 3, 5 y 6; Prop. 1(b); la parte (c) es ARGUED en dimensión infinita).
**Clase 𝓘:** argumentos que concluyen n_-(a_T|P_T) = 0 en una ventana T a partir de (1) una o varias
formas hermíticas de cualquier signatura, ligadas a a_T por identidades exactas o por restricción,
(2) vectores neutros, radicales o no, y (3) aritmética de inercia: Sylvester, Haynsworth, entrelazado,
perturbaciones de rango finito y la identidad con borde de la Prop. 1. En esa clase:

(a) la información de signo entra sólo por cotas superiores de índice, que son positividades sobre
subespacios de codimensión finita (Lema 2). Las únicas de a_T escritas en el corpus llevan a (L2)
(thm:coer-schur);

(b) un vector neutro no aporta nada. Dentro del subespacio no negativo es radical (Lema 3). Fuera de
él, es parte de la inmersión y la no negatividad del subespacio imagen es el objetivo. Y si 𝔊 pasa
por filas de 𝒟_N, es radical en cualquier signatura (Lema 4);

(c) en toda ventana con λ_A(T) > 0, el veredicto es el mismo para cΛ con |c − 1| < λ_A(T)/V_T
(Lema 5), de modo que la cláusula O4 no se cumple en ninguna ventana fija;

(d) los saltos de los enteros están en los ceros de c ↦ λ_A(T; c) (Lema 6). Un κ «por construcción»,
constante en c, obliga a que la matriz pequeña Γ (la capacidad polar o su inversa) contenga
exactamente la posición de c_±(T). Leer su signo en c = 1 es leer el signo de λ_A(T). Ésa es la
circularidad. No es un argumento «tan difícil como»: es la igualdad de la Prop. 1(c).

Respuesta a C43. Una ventana de positividad J(T) que se cierra sobre c = 1 por ambos lados
(NUMÉRICO en las formas de celda de 211 ROUND_021_A; sobre a_T, README §1.1) significa que
c_±(T) → 1. En cada T finito no hay degeneración en c = 1 (Lema 5). En el límite, el punto c = 1 es
el límite de dos puntos de degeneración. Esto no refuta un argumento de inercia en el límite, pero muestra
que un argumento así necesita, para cada T, la posición de c_±(T), que es información de valor
(Lema 6). Un índice que salte exactamente en c = 1, y no en sus cercanías, sólo podría venir de una
forma degenerada en c = 1. Eso es una identidad exacta en el peso verdadero, del tipo
(c − 1)·(…) = 0. Por R3-e y R3-i, una identidad así es una combinación de átomos y no fija el signo.

**Lo que la clase NO excluye.**

1. Cotas superiores de índice que no vengan de una positividad escrita sino de un conteo por principio
   del argumento de una función explícita de un parámetro espectral, construida con datos de la ventana
   y sin conocer el espectro de a_T. Para la función natural, Γ_T(z) = [⟨(Q − z)^{-1}χ_i, χ_j⟩], matriz
   de Nevanlinna 2×2, los autovalores de a_T|P_T son los ceros de det Γ_T(z) (Weinstein–Aronszajn,
   CITED como hecho estándar; su aplicación aquí es ARGUED). Contarlos en (−∞, 0) exige el espectro
   negativo de Q, y la cuenta vuelve a la Prop. 1(c). No conozco otra función con esa propiedad. Las
   construcciones del corpus de tipo Kreĭn–Langer / de Branges (fase 16 memo 07; R162_1301) cuentan
   datos fuera del sandbox y no se usan.
2. Argumentos uniformes en T que no lean sólo enteros. Por ejemplo, una cota de valor sobre
   λ_A(T; c) que fije c_±(T) a ambos lados de 1. Eso ya no es inercia: es el objetivo con margen.
3. Formas indefinidas usadas para algo distinto de concluir por conteo, por ejemplo una identidad de
   Green indefinida (R170_854 (3.4)) cuya parte negativa se cancele exactamente contra un término
   identificado. Esto es (G) y no está excluido por este memo; R3-g sólo cubre la clase de tipo
   resolvente.
4. La contabilidad conjunta R161_032 (4.2), OPEN / TERMINAL en la fuente, sin relación con este memo.

## Resultado

Sin mecanismo nuevo, más un NO-GO con clase (𝓘, inercia con vectores neutros), PROVED en sus partes
centrales (Lemas 2–6, Prop. 1(b)). El formato de Pontryagin del encargo ya está en P47
(thm:parityschur, prop:polarcap) con W_T, y aquí se repite con a_T. La tensión «κ(T) > 2» se debe a contar
con 𝔪_T: bajo el objetivo, n_-(a_T|L²) ≤ 2 para todo T. La candidata no pasa la puerta: no escribe (2)
y su punto (5) se responde en contra (Lema 5).

## Qué se probó

- Prop. 1(b): n_-(a_T|L²) = n_-(a_T|P_T) + n_-(S^Sch_T); bajo λ_A(T) > 0 vale ≤ 2. PROVED (misma prueba
  que thm:parityschur con ε = 0). Prop. 1(c), la forma con la matriz Γ_T de la resolvente: PROVED en
  dimensión finita, ARGUED en la versión de formas.
- Lema 2: n_-(q) ≤ κ ⟺ q ≥ 0 en un subespacio de codimensión ≤ κ. PROVED.
- Lema 3: un vector neutro en un subespacio no negativo es radical allí; un vector neutro sólo se
  añade a un subespacio no negativo si es 𝔊-ortogonal a él. PROVED.
- Lema 4: si 𝔊 factoriza por D, entonces ker D está en el radical, en cualquier signatura. Con R170_866–868,
  el ancla (Λ,1)⊗F es radical en toda 𝔊 que vea los coeficientes por filas que anulan (Λ,1). PROVED.
- Lema 5: constancia de todos los índices del formato para |c − 1| < λ_A(T)/V_T. PROVED.
- Lema 6: los saltos están en ∂J(T); con κ constante, Γ(c) es singular allí. PROVED, salvo el caso de
  pendiente nula, que es ARGUED.
- Tabla del §1 (qué forma tiene qué índice): CITED de P47, comprobado en primaria.

## Qué falló y por qué

- La positividad no puede salir «de una cuenta y no de una desigualdad». Las cotas superiores de
  índice son positividades (Lema 2), y la única que haría falta aquí es la del propio P_T, o la de un
  subespacio coercivo que lleva a (L2).
- El vector neutro no radical no tiene función. Dentro del subespacio no negativo es radical. Fuera de
  él, el objetivo es la no negatividad del subespacio imagen. Y la vía natural por filas de 𝒟_N lo
  vuelve radical en cualquier signatura.
- La cuenta es estable en c alrededor de 1 en cada ventana. O4 sólo puede salir de la posición de
  c_±(T), que es un dato de valor.

## Siguiente paso concreto

No relanzar «inercia / Pontryagin / vector neutro» como fuente de signo. Ninguna de las tres salidas
no excluidas tiene objeto. La única que no es (G) ni el objetivo con margen es la 1: una función
explícita de un parámetro espectral, construida con datos de la ventana sin conocer el espectro de
a_T, cuya cuenta de ceros o polos en una semirrecta acote n_-(a_T|L²) por 2 y fije la inercia de Γ_T.
Antes de proponerla habría que escribir esa función y explicar por qué su cuenta no pasa por la
Prop. 1(c).

Anotación sugerida para el índice y el grid (no hecha desde aquí): «P212-4E: formas indefinidas con
vector neutro no radical / conteo de Pontryagin — NO-GO con clase PROVED (cota superior de índice =
positividad en codimensión finita; neutro en subespacio no negativo = radical; índices constantes en c
cerca de 1 por ventana; saltos en ∂J(T)). El formato de Pontryagin = P47 thm:parityschur/prop:polarcap
con a_T; bajo el objetivo n_-(a_T|L²) ≤ 2. No excluye: conteo por principio del argumento de una función
de ventana sin espectro de a_T; (G) con forma de Green indefinida y cancelación exacta».
