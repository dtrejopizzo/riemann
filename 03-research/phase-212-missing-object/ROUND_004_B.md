# Ronda 4, zona 1 — Defecto de divisores cuadrático que entra sumando (memo de selección)

Memo de selección, no de construcción. Objetivo (★): λ_A(T) ≥ 0 para todo T, con las definiciones de
`../phase-211-sign-sandbox/STATEMENT_001.md`. N = e^{2T}, 𝒩 = {n : 2 ≤ n < N}. Etiquetas: PROVED /
CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

Notación. Para un peso a ∈ ℝ^𝒩: γ_n(F) = 2n^{−1/2} Re c_F(log n); a_T^{(a)}(F) = Arch(F) − Σ_n a(n)γ_n(F);
b_T(F) = Σ_n Λ(n)γ_n(F), de modo que a_T = Arch − b_T. Átomos ℓ_k(a) = Σ_{d|k, d≥2} a(d) − log k, k ∈ 𝒩.
U es la matriz de incidencia (Ue)_k = Σ_{d|k} e_d (unitriangular; U^{−1} es la convolución de Möbius
truncada), y ℓ(a) = U(a − Λ) porque UΛ = log.

Formato examinado (𝔉): para cada F ∈ P_T ∩ 𝒟_T una matriz simétrica K(F) ⪰ 0 indexada por 𝒩 (entradas
cuadráticas en F) y, para todo peso a de una clase 𝒜 ∋ Λ,

    a_T^{(a)}(F) + 𝔇_a(F) = ‖V_T(a)F‖² + ρ(a; F),   𝔇_a(F) = ⟨ℓ(a), K(F) ℓ(a)⟩,   ρ ≥ 0 manifiesta.   (𝔉)

## Cotejo

### Qué se buscó y dónde

Grep en `03-research/` (todas las fases), `04-papers/47` y `48`, `05-meta-and-planning/` (índice y
crucigrama) y el grid por: «defecto de divisores», «divisor defect», «δ_a(», «penalt», «penaliz»,
«Lagrang», «augmented», «aumentad», «joint positivity», «positividad conjunta», «window in c»,
«(c − 1)²», «inf over a», «stability», «Moreau», «𝒦_D2», «BARRIER_D2». Abiertos en primaria:
fase 197 `BARRIER_D2_001_DEFECT_STABILITY_SPLITTING_AND_CONTINUATION_NO_GO.md` (entero) y
`AUDIT_197_HOSTILE.md` §(f) (la puerta (D2)); fase 170 `R170_866` §§0–3, `R170_868` §§0–3 y §7; fase
211 `LEDGER.md` C35, C39, C43, `ROUND_021_A.md` Lema 3.3 y §3.4, `ROUND_017_A.md` tabla y lecturas
(l. 135–163), y de `ROUND_002_E.md` y `ROUND_003_A.md` los enunciados (Lemas 1–3, Cor. 4; Lemas 3–4);
de esta fase `ROUND_003_6.md` y `ROUND_003_2.md` enteros, `ROUND_003_4.md` Lema 4, `REVIEW_003.md`,
`LEDGER.md`, `RULES_AVOID.md`, `OBJECT_SPEC.md`, `README.md`, `BRIEF_CONSTRUCTOR.md`; las entradas del
índice README l.422 y 06 l.89–90. Las coincidencias de «penalt/Lagrang/augmented» (≈ 400 archivos) no se
abrieron una por una: por contexto son usos ajenos (Lagrangianos de restricciones de Tate, matrices
aumentadas de certificados). No abiertos en primaria: `R161_030` (se usa su resumen en `RULES_AVOID.md`
K2 y `ANNEX_161_FILES_1.md`), `R170_869` (se usa su estado en `RULES_AVOID.md` I2), las memos INV_P/INV_Q
de la fase 193 que BARRIER_D2_001 declara subsumidas, y el capítulo de P48 sobre estabilidad (el grep sólo
devolvió «sparse stability», ajeno). Una búsqueda sin coincidencias no prueba novedad.

### (1) Antecedente más cercano

**Fase 197, `BARRIER_D2_001`, Teorema 1 (PROVED allí; auditado en `AUDIT_197_2.md`; índice README
l.422, NO-GO de clase 𝒦_D2).** Para cualquier clase de peines 𝓔 ∋ Λ y cualquier defecto Δ ≥ 0 con
Δ(Λ) = 0, la desigualdad de estabilidad (I_T; C): λ_A(T; a) ≥ −CΔ(a) sobre 𝓔 equivale a la positividad en
Λ conjugada con una rigidez sin signo de Δ; la condición necesaria (Rig^w) es
Δ(a) ≥ C^{−1}(⟨a − Λ, w_T⟩ − μ), con w_T el vector de correlaciones del minimizante. El formato (𝔉)
implica, tomando ínfimo en F, una desigualdad de ese tipo con Δ(a) = sup_{‖F‖=1} 𝔇_a(F). La diferencia de
forma es que aquí el defecto depende de F, es cuadrático en los átomos y se exige la identidad
manifiesta para cada F, no la desigualdad entre ínfimos.

Antecedentes de las piezas: `R170_866` (la forma ℒ_N = 𝒟_N*𝒟_N con núcleo exactamente ℝ(Λ,1), que es
𝔇 con K = diag(1/k) sin F); `R170_868` §3 (toda extensión lineal positiva que conserva la línea nula
es 𝒟_N*(I + ΣQ_j*Q_j)𝒟_N, cambio de métrica); `ROUND_003_6.md` Lema 3 y (4.4) (la única cantidad
escrita que distingue c = 1 es (c − 1)b_T); `ROUND_003_2.md` Lemas 1 y 3; `R161_030` (varianza orientada,
de grado dos y genérica); 211 C43 y `ROUND_021_A` Lema 3.3 (ventana J_R ≍ λ₀/K₀).

### (2) Objeto realmente nuevo

No hay objeto (ℋ_T, V_T, ρ_T) que pase. Lo nuevo es un lema que decide el formato entero (§1):
(𝔉) para todos los pesos equivale, punto a punto en F, a la desigualdad con margen

    a_T(F) ≥ ¼ ⟨η(F), K(F)^+ η(F)⟩,   η(F) := U^{−T}γ(F),   η_d(F) = Σ_{m: dm<N} μ(m) γ_{dm}(F),     (M_K)

más η(F) ∈ ran K(F). Es una versión punto a punto y cuadrática de BARRIER_D2_001 Teorema 1(c), con el
término lineal escrito (el «primer jet» de `R170_868`) y con la consecuencia cuantitativa a lo largo de
cΛ (Lema 2). No es un objeto de signo: es la descripción exacta de lo que (𝔉) exige.

### (3) ¿Evita la dificultad del antecedente?

No. La dificultad de BARRIER_D2_001 es que todo el signo queda en el punto Λ. Pasar a un defecto
cuadrático que depende de F no lo cambia: un término que se anula a segundo orden en Λ no puede pagar
el término de primer orden −⟨ℓ, η(F)⟩, de modo que (𝔉) obliga a que a_T(F) tenga margen (M_K) en cada
F. Es más fuerte que (★), no más débil. El caso de `R170_868` se repite literalmente: 𝔇 es un cambio de
métrica (dependiente de F) sobre la imagen de 𝒟_N y pierde el primer jet (Lema 0 y Lema 1).

### (4) Identidad que conecta con la forma completa sobre P_T

En a = Λ, (𝔉) es exactamente (G): 𝔇_Λ = 0. Fuera de Λ, por el Lema 1, (𝔉) se escribe siempre así:

    a_T^{(a)}(F) + 𝔇_a(F) = [a_T(F) − ¼⟨η, K^+η⟩] + ⟨ℓ(a) − ½K^+η, K(F)(ℓ(a) − ½K^+η)⟩,

de modo que la única afirmación con signo es (M_K), en Λ. La conexión con la positividad global existe
y es trivial (evaluar en Λ); el formato no aporta mecanismo.

### (5) cΛ y a_P: por qué el resto deja de ser ≥ 0

En (𝔉) el resto no deja de ser ≥ 0 para cΛ ni para a_P: la identidad sigue valiendo y lo que se rompe es
la conclusión, porque 𝔇 > 0 absorbe la negatividad (a_T^{(cΛ)} ≥ −(c − 1)²Q; a_T^{(a_P)} ≥ −Q para
P > N, pues a_P vale 0 en la ventana y ℓ(a_P) = −log). Esto cumple R3-i en la letra, pero el Lema 1
muestra que esa ruptura es automática para cualquier K que cumpla (M_K) y no contiene signo. Cuartetos
y f_t tienen los mismos Λ(n), n < N: (𝔉) en su peso es (𝔉) en Λ, no los separa (RULES_AVOID §E).

## 1. Lemas

### Lema 0 (todo defecto cuadrático semidefinido nulo en la línea es de este formato; PROVED)

Sea q una forma cuadrática semidefinida positiva en (a, c) ∈ ℝ^𝒩 ⊕ ℝ con q(Λ, 1) = 0. Entonces existe
K̃ ⪰ 0 con q(x) = ⟨𝒟_N x, K̃ 𝒟_N x⟩, 𝒟_N(a,c)_k = k^{−1/2}((a∗1)(k) − c log k).

*Demostración.* Para q ⪰ 0, q(v) = 0 implica que v está en el radical (Cauchy–Schwarz:
|q(v,x)|² ≤ q(v)q(x) = 0). Luego q se anula en ℝ(Λ,1) = ker 𝒟_N (`R170_866` Teor. 2.1) y desciende al
cociente, que 𝒟_N identifica con ℝ^𝒩 por sobreyectividad (`R170_868` §1). ∎

Lectura: (𝔉) con c = 1 fijo es el defecto cuadrático semidefinido más general que se anula en Λ; K(F)
es una métrica sobre la imagen de 𝒟_N, como en `R170_868` (3.3), ahora dependiente de F.

### Lema 1 (equivalencia de Legendre; PROVED)

Sea 𝒜 = ℝ^𝒩 (todos los pesos reales). Para cada F fijo son equivalentes:
(i) a_T^{(a)}(F) + 𝔇_a(F) ≥ 0 para todo a ∈ 𝒜;
(ii) η(F) ∈ ran K(F) y a_T(F) ≥ ¼⟨η(F), K(F)^+ η(F)⟩.
En particular (𝔉) sobre 𝒜 implica (★) con el margen (M_K), y si se cumple (ii) la identidad del §(4)
da el miembro derecho como un número ≥ 0 más un cuadrado.

*Demostración.* Con e = a − Λ, Σ a(n)γ_n = b_T + ⟨e, γ⟩ y e = U^{−1}ℓ, luego ⟨e, γ⟩ = ⟨ℓ, U^{−T}γ⟩ = ⟨ℓ, η⟩;
(U^{−T}γ)_d = Σ_{k: d|k} μ(k/d)γ_k. Así a_T^{(a)}(F) + 𝔇_a(F) = Φ_F(ℓ) := a_T(F) − ⟨ℓ, η⟩ + ⟨ℓ, Kℓ⟩, y
ℓ = ℓ(a) recorre todo ℝ^𝒩 cuando a lo hace (U invertible). Si η ∉ ran K = (ker K)^⊥, existe v ∈ ker K con
⟨v, η⟩ > 0 y Φ_F(tv) = a_T − t⟨v, η⟩ → −∞: falla (i). Si η ∈ ran K, completando el cuadrado
Φ_F(ℓ) = a_T − ¼⟨η, K^+η⟩ + ⟨ℓ − ½K^+η, K(ℓ − ½K^+η)⟩, cuyo mínimo es a_T − ¼⟨η, K^+η⟩. ∎

Respuesta a (iii) del encargo, a = 0 y a grande: a = 0 da Arch(F) + Q(F) ≥ 0 con Q(F) := ⟨log, K(F) log⟩;
el coeficiente principal en a grande es ⟨·, K·⟩ ≥ 0. Ninguno de los dos extremos es falso para K
grande: la restricción efectiva está en el entorno de Λ (primer jet), y es (M_K).

### Lema 2 (a lo largo de cΛ; PROVED)

Supóngase (𝔉) para todo cΛ, c ≥ 0 (lo cumple toda clase que contenga los pesos ≥ 0). Como
ℓ(cΛ) = (c − 1) log y ⟨log, η⟩ = ⟨U^{−1}log, γ⟩ = ⟨Λ, γ⟩ = b_T,

    a_T(F) − (c − 1) b_T(F) + (c − 1)² Q(F) ≥ 0   para todo c ≥ 0 y todo F.

(a) λ_A(T; cΛ) ≥ −(c − 1)² Q_T, con Q_T := sup_{‖F‖=1} Q(F).
(b) Si b_T(F) ≥ 0, o |b_T(F)| ≤ 2Q(F): a_T(F) ≥ b_T(F)² / (4Q(F)).
(c) Si u ∈ P_T es un vector nulo exacto de a_T con Q(u) < ∞, entonces b_T(u) = 0 y Arch(u) = 0.

*Demostración.* a_T^{(cΛ)} = a_T − (c − 1)b_T da (a). (b): c − 1 = b/(2Q) ≥ −1 en ambos casos. (c): si
b(u) > 0, (b) da 0 ≥ b²/(4Q) > 0; si b(u) < 0 y |b| ≤ 2Q, igual; si b(u) < −2Q(u), c = 0 da
0 + b + Q ≥ 0, contradicción; si Q(u) = 0, c → ∞ da b ≤ 0 y c = 0 da b ≥ 0. Luego b(u) = 0 y
Arch(u) = a_T(u) + b_T(u) = 0. ∎

Respuesta a (i), condición necesaria comprobable frente a C43. Sobre todo F: el discriminante
b_T(F)² ≤ 4a_T(F)Q(F) (con b ≥ 0); en los casi-minimizantes u (a_T(u) ≈ λ_A): Q(u) ≥ b_T(u)²/(4λ_A); y en
cada c fuera de la ventana J_T: Q_T ≥ −λ_A(T; cΛ)/(c − 1)². La ventana que se cierra a primer orden
(c_+ − 1 ≍ λ_A/b_T(u), 211 C43, `ROUND_021_A` Lema 3.3, `ROUND_017_A` lectura (i)) es compatible con (𝔉)
sólo si Q es del orden de b_T(u)²/λ_A sobre el minimizante. En una ventana de contacto exacto, (c) exige
b_T ≡ 0 en el vector nulo, es decir tangencia exacta con pendiente nula, que 211 `ROUND_003_A` Prop. 2
describe como coincidencia de codimensión uno (allí el fondo calculado tiene Π > 0: NUMÉRICO).

### Corolario 3 (núcleos acotados; CONDITIONAL y NUMÉRICO)

Clase 𝒦_b: K(F) ⪯ κ_T‖F‖² I con κ_T fijo. Incluye los dos núcleos naturales del encargo:
- K_{kk'}(F) = (kk')^{−1/2}⟨S_{log k}F, S_{log k'}F⟩ (traslaciones comprimidas, ‖S‖ ≤ 1): es el Gram de
  w_k = k^{−1/2}S_{log k}F, luego κ_T ≤ Σ_{k<N} 1/k ≤ 2T, y Q(F) ≤ (Σ_{k<N} log k/√k)²‖F‖²;
- el de `R170_866` tensorizado, K = diag(1/k)‖F‖²: Q(F) = (Σ_{k<N} log²k/k)‖F‖².

(PROVED) En 𝒦_b, (𝔉) sobre todos los pesos implica a_T(F) ≥ |η(F)|²/(4κ_T) para ‖F‖ = 1, y por tanto todo
casi-minimizante unitario u (a_T(u) ≤ λ_A + ε) cumple |η(u)|² ≤ 4κ_T(λ_A + ε). Con P47 cor:margin1
(CITED: λ_A(T) ≤ 4·10⁹ T e^{−15.449T} para T ≥ 1): |η(u)| ≤ 4·10^{4.8} T e^{−7.72T}, y por el Lema 2(b)
|b_T(u)| ≤ 2(Q_T λ_A)^{1/2} con Q_T polinómico en N.
(CONDITIONAL) Si b_T(u_T) no decae más rápido que una potencia de N sobre los casi-minimizantes, ningún
núcleo de 𝒦_b con κ_T, Q_T polinómicos en N realiza (𝔉) para T grande. No hay cota inferior PROVED de
|b_T(u)|: el caso degenerado w_T = 0 tampoco está excluido en la fase 197 (`AUDIT_197_HOSTILE` §(e)).
(NUMÉRICO, valores registrados en 211 `ROUND_017_A`, no recalculados aquí) En T = 1, Galerkin par:
λ_A(1; (1 + 10^{−20})Λ) ≈ −3.2·10^{−22}, luego el Lema 2(a) exige Q_1 ≥ 3.2·10^{18}; en T = 0.8,
λ_A(0.8; (1 + 10^{−10})Λ) ≈ −3.8·10^{−13} exige Q_{0.8} ≥ 3.8·10^7. Para los dos núcleos naturales en
T = 1 (n ≤ 7): Q_1 ≤ (Σ_{k=2}^{7} log k/√k)² ≈ 4.004² ≈ 16.0 y Q_1 = Σ_{k=2}^{7} log²k/k ≈ 2.72. Ambos
violan la condición necesaria por ≥ 17 órdenes de magnitud. Un K que la cumpla tiene que valer
≳ b_T(u)²/λ_A precisamente sobre el fondo de a_T, es decir ser un funcional ajustado al minimizante
(patrón B9; ARGUED).

### Respuesta a (iv): `R170_868`/`869` sobre este formato

`R170_868` cierra las filas lineales que anulan la línea nula: factorizan por 𝒟_N y toda extensión
positiva es un cambio de métrica que pierde el primer jet. El formato (𝔉) es cuadrático, no lineal, en
𝒟_N, pero por el Lema 0 es exactamente un cambio de métrica (dependiente de F) de ℒ_N, y el Lema 1 hace
precisa la pérdida del primer jet: la derivada de 𝔇_a en Λ es cero, el término de primer orden
−⟨ℓ, η(F)⟩ sólo lo paga a_T(F), y por eso hace falta el margen (M_K). Que K dependa de F no escapa: el
argumento es punto a punto en F. Escapar exige una de las tres salidas de `R170_868` §0: salir del espacio
de coeficientes (coordenada de borde β_T), un término no polinómico en ℓ que no se anule a segundo orden
(con lo que deja de ser ≥ 0 cerca de Λ en la dirección de η, por el mismo cálculo), o no anular la línea
(con lo que 𝔇_Λ ≠ 0 y (𝔉) en Λ ya no es (G)). `R170_869` (todo uso lineal cae en el ideal Q𝒟_N) no se
aplica en la letra a un término cuadrático, pero por el Lema 1 el único uso del formato en Λ es lineal:
la evaluación.

## Resultado

Repetición en lo esencial, más un lema corto PROVED que cierra el formato tal como se enunció. El formato
(𝔉) es la versión punto a punto y cuadrática de la puerta (D2) de la fase 197 (`BARRIER_D2_001`
Teorema 1, NO-GO de clase 𝒦_D2) y un cambio de métrica en el sentido de `R170_868`. Lema 1: sobre todos
los pesos, (𝔉) equivale a la desigualdad con margen (M_K) en Λ, más fuerte que (★); el defecto no aporta
signo. Para los núcleos naturales el margen es incompatible con lo registrado (NUMÉRICO en T = 0.8, 1;
CONDITIONAL en general). Sin candidata lista para construcción.

## Qué se probó

1. Lema 0 (PROVED): todo defecto cuadrático semidefinido en (a, c) nulo en (Λ, 1) es ⟨𝒟_N·, K̃𝒟_N·⟩.
2. Lema 1 (PROVED): (𝔉) sobre todos los pesos ⟺ η(F) ∈ ran K(F) y a_T(F) ≥ ¼⟨η, K^+η⟩ para cada F, con
   η = U^{−T}γ el vector de correlaciones con pesos de Möbius. Los extremos a = 0 y a grande no restringen.
3. Lema 2 (PROVED): a lo largo de cΛ, λ_A(T; cΛ) ≥ −(c − 1)²Q_T; a_T ≥ b_T²/(4Q) cuando b_T ≥ 0; en un
   vector nulo exacto, b_T = Arch = 0. Condición necesaria comprobable frente a C43.
4. Corolario 3: en la clase de núcleos acotados, |η(u)|² ≤ 4κ_T(λ_A + ε) en casi-minimizantes (PROVED);
   imposibilidad para T grande CONDITIONAL a una cota inferior polinómica de |b_T(u)|; violación por
   ≥ 17 órdenes en T = 1 para los dos núcleos naturales (NUMÉRICO, con valores registrados en la 211).

## Qué falló y por qué

- Un término que se anula a segundo orden en Λ no paga el término de primer orden en el peso; ese término
  es lineal y queda a cargo de a_T(F), que tiene que tener margen. Es la pérdida de primer jet de
  `R170_868`, ahora en la versión cuadrática.
- La «ruptura bajo cΛ por un término escrito» que el formato cumple es automática para cualquier K que
  satisfaga (M_K): la conclusión sobre a_T^{(c)} falla porque 𝔇 > 0, pero eso no aporta signo en Λ.
- El signo vive en (M_K) en Λ, igual que en la fase 197 vive en WP_T(Λ).

NO excluido (delimitación; nada de esto tiene objeto escrito):
1. núcleos K(F) no acotados en L² y no ajustados al minimizante: el Lema 1 sólo dice que deben cumplir
   (M_K), y el Corolario 3 sólo cubre la clase acotada; con K relativamente acotado por la norma N_T de
   R3-h la conclusión es la misma (ARGUED: los casi-minimizantes tienen norma N_T acotada);
2. clases 𝒜 que no contengan un entorno de Λ ni la recta cΛ (por ejemplo, sólo peines de Euler con
   exponentes enteros): el Lema 1 usa todas las direcciones, el Lema 2 la recta; sobre clases discretas
   alrededor de Λ el término lineal no está forzado;
3. defectos que no se anulan a segundo orden en Λ ni son polinómicos en ℓ, y la coordenada de borde β_T
   de `R170_868` §5;
4. la falta de una cota inferior PROVED de |b_T| sobre los casi-minimizantes, que convertiría el
   Corolario 3 en NO-GO incondicional para la clase acotada.

## Siguiente paso concreto

No construir sobre este formato. Anotar en el índice (fila de la fase 197, BARRIER_D2_001), en el grid y en
el ledger: «Fase 212, defecto de divisores cuadrático que suma (formato a_T^{(a)} + ⟨ℓ(a), K(F)ℓ(a)⟩ =
‖V(a)F‖² + ρ): repetición de BARRIER_D2_001 Teor. 1 y de `R170_868` §3 en versión punto a punto; Lema 1
PROVED: equivale a a_T(F) ≥ ¼⟨η, K^+η⟩ con η = U^{−T}γ (objetivo más margen); Lema 2 PROVED: λ_A(T; cΛ)
≥ −(c − 1)²Q_T; núcleos acotados incompatibles con la ventana registrada (NUMÉRICO T = 0.8, 1;
CONDITIONAL en general). Signo global OPEN.» Antes de anotarlo, un segundo lector debe verificar el
cambio de variables ⟨e, γ⟩ = ⟨ℓ, U^{−T}γ⟩ y el caso Q(u) = 0 del Lema 2(c). La pieza que convertiría el
Corolario 3 en NO-GO incondicional es una cota inferior de |b_T| (o de |η|) sobre los casi-minimizantes;
es el mismo hueco w_T ≠ 0 de la fase 197 y no se propone como ruta.
