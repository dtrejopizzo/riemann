# Ronda 4, zona D — Factorización de 𝔸_M con soporte en las casi-coincidencias m ≈ kn (memo de selección)

Objetivo (★): λ_A(T) ≥ 0 para todo T, definiciones de `../phase-211-sign-sandbox/STATEMENT_001.md`. Reducción usada
(PROVED, P47 prop:AM, thm:oneprofile): perfil fijo F_0 ∈ P_{T_0}, 2T_0 < log 2; (★) equivale a
𝔸_M = [𝖡(log m − log k)]_{m,k≤M} ⪰ 0 para todo M, con 𝔸_M = Arch_M − Div_M − Near_M. Notación: β(d) parte
arquimediana de 𝖡, c_0 = c_{F_0} (sop ⊂ [−2T_0, 2T_0], c_0(0) = 1), v_n = 2Λ(n)n^{−1/2}, θ_0 := 2T_0.
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

### Qué se buscó, qué se abrió, qué no

Grep (sin distinguir mayúsculas) en `03-research/` (todas las fases), P47, P48 y `05-meta-and-planning/` (índice,
crucigrama) por: near-divisib, casi-divisib, almost divisor, interval order, orden de intervalo, semiorder, Farey,
continued fraction, fracción continua, Green matri(x), matriz de Green, semisepar, totally positive, totalmente
positiv, Pólya frequency, sign-regular, complemento de Schur, closed under elimination, transitive. Resultados:
«near-divisib», «casi-divisib», «almost divisor», «semiorder», «closed under elimination», «orden de intervalo»: 0
coincidencias; «interval order»: 1 (fase 73, E73_115, no pertinente por título, no abierto); «Farey»: 42 archivos
(fases 167, 191, 200, 194); «totally positive»/«Pólya frequency»: 24/14 (fases 102–104, 114–116, 154, 162, 184, 186,
200, 201) más el índice AUDIT_A (A14a-1: PF₅ del núcleo de de Bruijn–Newman, NO-GO CITED; A14a-2: PF₄ OPEN), L23,
L48, L49; «Green»: fases 116, 170, 194, 205, 206.

Abiertos en primaria: P47 prop:AM con demostración, thm:oneprofile con demostración, prop:nearfree con demostración,
rem:boxes, rem:bar-arith; `ROUND_003_7` (entera), `REVIEW_003`, `RULES_AVOID` §§B, E, F, J; `OBJECT_SPEC`;
`BRIEF_CONSTRUCTOR`; STATEMENT_001; fase 194 `INV_C_001` §§0–1 (fibración por razones r = a/b, Lema 1–3);
fase 205 `SKELETON_001` (líneas de §5 «Pole Green identity» y su tabla de búsqueda: «semiseparable: 0»);
211 LEDGER filas C9 y C43; índice AUDIT_A §1 (PF₅). No abiertos en primaria (límite del cotejo): `N_BUILD_022`,
`L2_BUILD_031`, `CA_K_001`, `CA_K_002` (usados sólo a través de su lectura en `ROUND_003_7` §Cotejo y `REVIEW_003`,
que los confirma); fase 202 (tabla exterior); fase 206 salvo la línea de NODE_001 que nombra el núcleo de Green
del polo; 211 `ROUND_003_B` (sólo vía LEDGER C9); los 42 archivos de Farey salvo INV_C_001; los archivos de
total positividad de las fases 102–116 y 186. Una búsqueda sin coincidencias no prueba novedad.

### (1) Antecedente más cercano

- `ROUND_003_7` Lema 1 y «no excluidos» (factor en la divisibilidad: NO-GO de formato), con `ROUND_001_B` §4.
- `INV_C_001` §1 (fase 194): la fibración de los pares (m, n) por la razón r ∈ ℚ_{>0} con masa de fibra κ_K(r);
  el ordenamiento Farey/coprimo de los pares se examinó allí y aterriza en un objeto sin información de signo
  (los pesos de las razones primas son 1, no Λ(q), salvo inserción a mano).
- 211 LEDGER C9 (`ROUND_003_B`): métricas de tamaño |log m/k| y de factorización log(lcm/gcd) acopladas sobre
  𝔸_M: reformulación, menores negativos explícitos.
- fase 205 `SKELETON_001` §5: identidad de Green del polo (núcleo e^{|s|/2} = rango 2 + Green de ¼ − ∂²) en la
  ventana: es la única estructura de tipo Green registrada; vive en el polo, no en 𝖡 ni en Near.
- Índice AUDIT_A A14a-1/2: total positividad de orden ≥ 5 del núcleo de de Bruijn–Newman, NO-GO CITED; no es 𝖡.

### (2) Objeto realmente nuevo

No hay ℋ_T, V_T, ρ_T nuevos. No sé escribir una W con soporte en las casi-coincidencias y fórmula propia que lleve
signo. Lo que esta memo aporta son tres piezas de delimitación, demostradas en §1, que responden (i), (ii) y (iv):

- **Lema A (grafo de acoplamiento; PROVED salvo una cita).** Descripción exacta de los soportes de Div, Near, Arch;
  el soporte de Div + Near depende del peso sólo a través del conjunto finito {n ≤ n_* : a(n) ≠ 0}.
- **Lema B (estructura de orden; PROVED).** La relación de casi-divisibilidad no es un orden parcial (no es
  transitiva); su soporte está contenido en el semiorden de umbral {m/k > 2e^{−θ_0}} y coincide con él para
  m/k ≥ R_0. Toda «función de Möbius» extraída del patrón es, salvo en un conjunto acotado de razones, la del
  semiorden de umbral, que no depende del peso.
- **Lema C (cierre bajo eliminación; NO-GO de formato, PROVED).** Si 4T_0 < log 2, 𝖡 toma valores estrictamente
  negativos en (θ_0, log 2 − θ_0) y 𝖡(0) > 0; y 𝖡 no coincide en (0, ∞) con ninguna transformada de Laplace de una
  medida (en particular con ninguna suma finita de exponenciales). Luego 𝔸_M, para M grande, no pertenece a ninguna
  de las familias cerradas bajo complemento de Schur por las que preguntaba el encargo: núcleos totalmente
  positivos o signo-regulares de orden 1, matrices de Green de árbol o de la recta con pesos positivos
  (semiseparables de rango acotado), matrices f(mcd).

### (3) Por qué el cambio evitaría la dificultad del antecedente

No la evita. El antecedente (`ROUND_003_7` Lema 1) falla por formato: la incidencia de divisores no ve los pares
coprimos casi proporcionales. Pasar al soporte de casi-coincidencias corrige el formato (el soporte ya no es
escaso: Lema A muestra que es casi completo fuera de una banda alrededor de la diagonal), pero el Lema B muestra
que la estructura combinatoria de ese soporte es esencialmente un semiorden de umbral independiente del peso, y el
Lema C que 𝖡 no está en ninguna clase conocida cerrada bajo eliminación. La información aritmética está en los
**valores** de las entradas de Near, no en su patrón; un pivote explícito tendría que leerse de los valores, y eso
es la LDL de `ROUND_003_2` Lema 2 (circular, RULES_AVOID J3).

### (4) Identidad que conectaría con la positividad global

Ninguna escrita. La forma que tendría que tener: 𝔸_M = WᵀDW + ρ_M con D ≥ 0, W soportada en el grafo del Lema A,
W y D dados por fórmula propia en los valores Λ(n), n < M e^{θ_0}, y ρ_M con signo manifiesto; por el Lema 2 de
`ROUND_003_7` (sitios primos ya equivalentes) la restricción a primos de WᵀDW tendría que llevar rango alto, lo que
el soporte de Near permite (Lema A(c)) pero ningún antecedente ni esta memo realiza. Lo que sí queda fijado
(Lemas B, C): la «cierre bajo eliminación» que haría de los pivotes una identidad no puede venir de la clase del
núcleo 𝖡 ni del patrón de soporte; tendría que ser una propiedad de la familia {𝔸_M} que use los valores exactos.

### (5) cΛ y a_P: por qué el resto dejaría de ser ≥ 0

- Para cualquier construcción que use sólo el patrón del Lema A (y su Möbius, Lema B): el patrón es idéntico para
  todo c > 0 (Lema A(d)), luego W y D serían los mismos para cΛ y para Λ; el resto ρ^{(c)} = 𝔸^{(c)} − WᵀDW =
  ρ^{(1)} + (1 − c)(Div + Near) es afín en c, y su conjunto de positividad es un intervalo de c. No hay línea que
  lo rompa por el patrón; la ruptura tendría que venir de que (Div + Near) no es ⪰ 0 ni ⪯ 0 en la dirección de ρ,
  es decir, de valores. Por R3-i esto no es mecanismo: es la condición misma.
- a_P borra las potencias de primos p < P: el patrón cambia sólo en razones acotadas (Lema A(d)) y en Div; sobre
  el resto del soporte (razones ≥ R_0 P-dependiente) el patrón coincide. La ruptura no puede estar en el patrón
  de razones grandes.
- En una W con valores propios (no escrita) la ruptura debe señalarse en los valores; no hay objeto donde
  señalarla.

### Veredicto del cotejo

Sin mecanismo nuevo. La zona «W con soporte en m ≈ kn» queda delimitada: su patrón es un semiorden casi independiente
del peso, y 𝖡 no pertenece a clases cerradas bajo eliminación. Se demuestran tres lemas de delimitación (§1); ninguno
lleva signo. No hay candidata lista para construcción.

## 1. Demostraciones

### Lema A (grafo de acoplamiento)

Sea a un peso real ≥ 0 sobre {n ≥ 2} (Λ, cΛ, a_P), v_n^a = 2a(n)n^{−1/2}. Para m > k ≥ 1, r := m/k.

(a) **Div** (PROVED, P47 prop:AM(iii)): (Div)_{mk} = ½ v^a_{r} si r ∈ ℕ, y 0 si no. Soporte potencial: k | m con
a(m/k) ≠ 0 (para Λ: m/k potencia de primo). Diagonal nula.

(b) **Near** (PROVED, ibíd.): (Near)_{mk} = ½ Σ_{n ≥ 2, n ≠ r} v^a_n c_0(log(kn/m)), y el término n contribuye sólo si
|log n − log r| < θ_0. Soporte potencial: existe n ≥ 2, n ≠ r, a(n) ≠ 0, con n ∈ (r e^{−θ_0}, r e^{θ_0}). Como n ≥ 2,
esto exige r > 2e^{−θ_0} > 1. Diagonal nula; además Near_{mk} = Near_{km}.

(c) **Arch** (PROVED a partir de STATEMENT_001 §3 y P47 lem:transl(iv)): para d := log r > θ_0,
Arch_{mk} = β(d) = −Σ_{j≥1} γ_j e^{−(2j+½)d}, γ_j = ∫e^{(2j+½)u}c_0(u)du. Como F_0 es par y real (g ∗ g̃ y G_0 son
pares), γ_j = (∫F_0(t)e^{(2j+½)t}dt)² ≥ 0, y ∫F_0 e^{st} = F̂_0(−is) = (¼ − s²)ĝ(is)²ĝ(−is)² con
ĝ(±is) = (e^{(b∓s)a} − 1)/(b ∓ s), real y no nulo si b ≠ ±s. Así, para b ∉ {±(2j+½)}, γ_j > 0 para todo j ≥ 1, y
Arch_{mk} < 0 para toda razón r > e^{θ_0}: Arch acopla **todos** los pares, con entradas negativas fuera de la
banda |log r| ≤ θ_0 y decaimiento e^{−5d/2}.

(d) **Dependencia del soporte en el peso.** CITED (teorema de los números primos): para cada η > 0 existe x_η con
un primo en (x, x(1+η)) para todo x ≥ x_η. Tomo η con 1 + η ≤ e^{θ_0}. Para r ≥ R_0 := x_η e^{θ_0}, los dos
intervalos (r e^{−θ_0}, r) y (r, r e^{θ_0}) contienen cada uno un primo, y al menos uno es ≠ r. Luego, para todo peso
con a(p) ≠ 0 en todos los primos p ≥ x_η (en particular Λ, cΛ con c > 0, y a_P si además R_0 ≥ P e^{θ_0}):
**todo par con r ≥ R_0 está en el soporte potencial de Near.** Para
r < R_0, el soporte depende sólo de {n ≤ n_* := R_0 e^{θ_0} : a(n) ≠ 0}, un conjunto finito. En consecuencia:

- el soporte potencial de Div + Near es el mismo para Λ y para cΛ, todo c > 0 (PROVED, trivial: a(n) ≠ 0 no cambia);
- para a_P difiere del de Λ sólo en pares con r < R_0(P) (PROVED dado lo CITED).

Observación: «soporte potencial» porque una suma Σ v_n c_0(·) puede anularse por cancelación (c_0 cambia de signo);
el soporte efectivo es un subconjunto. ∎

### Lema B (estructura de orden de la casi-divisibilidad)

Sea ⊲ la relación k ⊲ m :⟺ m > k y (m, k) en el soporte potencial de Div + Near (Lema A) para el peso Λ.

(a) ⊲ está contenida en el semiorden de umbral S := {(k, m) : log m − log k > log 2 − θ_0}. PROVED: Lema A(a),(b).
S es un semiorden (orden de intervalos unitarios en la recta log): x ≺ y ⟺ y − x > δ, δ := log 2 − θ_0 > 0.

(b) ⊲ no es transitiva en general, luego no es un orden parcial y no tiene álgebra de incidencia ni función de
Möbius propia. PROVED con ejemplo: 1 ⊲ 2 (Div, Λ(2) > 0); 2 ⊲ 6 (Div, 6/2 = 3, Λ(3) > 0); pero (1, 6) no está en
el soporte si θ_0 < log(7/6): Λ(6) = 0, y el intervalo (6e^{−θ_0}, 6e^{θ_0}) ⊂ (5, 7) no contiene ningún entero
n ≠ 6. Luego 1 ⊲ 2 ⊲ 6 y no 1 ⊲ 6. ∎
La clausura transitiva de ⊲ está contenida en S (S es transitivo: δ + δ > δ) y contiene todos los pares con
r ≥ R_0 (Lema A(d)).

(c) Consecuencia para pivotes de «Möbius». Cualquier construcción de pivotes que dependa sólo del orden
(clausura transitiva de ⊲, o S) es: en las razones r ≥ R_0, idéntica a la del semiorden S, que depende sólo de δ
(arquimediano) y no del peso; en las razones r < R_0, depende del peso sólo a través del conjunto finito
{n ≤ n_* : Λ(n) ≠ 0}. PROVED (Lemas A(d), B(a)). Por B1/B5 de RULES_AVOID (clase cerrada por modificación que
conserva ese conjunto finito, p. ej. f_t con λ₁ > n_*, o cΛ), una tal construcción no puede llevar el signo
sola. Es NO-GO de clase para «pivotes determinados por el patrón de soporte», no para W con valores propios.

El semiorden S, restringido a {log m : m ≤ M}, sí es un orden de intervalos y su función de Möbius es explícita
por cadenas (μ_S(x, y) = Σ_{cadenas} (−1)^{long}), pero no contiene ningún dato de Λ. Una «inversión de Möbius en
el semigrupo de intervalos» (la que transforma sumas sobre (r e^{−θ_0}, r e^{θ_0}) en valores puntuales) es la
deconvolución por c_0, que es exactamente pasar de Near a la medida puntual Σ v_n δ_{log n}: devuelve el peine, no
un pivote. ARGUED (es la definición de Near como convolución, P47 prop:AM(iii)).

### Lema C (𝖡 no está en las clases cerradas bajo eliminación)

Hipótesis: 4T_0 < log 2 (es decir θ_0 < log 2 − θ_0), b ∉ {±(2j+½) : j ≥ 1}.

(a) 𝖡(d) < 0 para d ∈ (θ_0, log 2 − θ_0). PROVED: allí |log n ± d| ≥ log 2 − d > θ_0 para todo n ≥ 2, luego la parte
del peine es nula y 𝖡(d) = β(d) = −Σ_{j≥1}γ_j e^{−(2j+½)d} < 0 por Lema A(c).

(b) 𝖡(0) = a_{T_0}(F_0) (P47 thm:band, STATEMENT_001 §3). Es > 0 en las ventanas certificadas T_0 ≤ ½ log 5
(PROVED en P47; aquí T_0 < (log 2)/4 está dentro). Si 𝖡(0) = 0 con 𝖡(d) < 0 en otro punto, 𝔸_M ya no sería ⪰ 0
para el par {log 1, log m} con log m ≈ d — no ocurre por lo certificado; basta 𝖡(0) ≥ 0 y (a).

(c) 𝖡 restringida a (0, ∞) no es la transformada de Laplace ∫e^{−td}dν(t) de ninguna medida con signo ν para la que
esa integral converja en un entorno de (0, ∞) (en particular no es una suma finita de exponenciales). PROVED: tal
transformada es real-analítica en (0, ∞). En (θ_0, log 2 − θ_0) coincidiría con β, y β en (θ_0, ∞) es también una
serie de exponenciales −Σγ_j e^{−(2j+½)d} analítica en (θ_0, ∞); dos funciones analíticas que coinciden en un
intervalo coinciden en (θ_0, ∞); luego la parte del peine sería ≡ 0 en (θ_0, ∞). Pero en d ∈ (log 2 − θ_0, log 2 + θ_0)
con θ_0 < (log(3/2))/2 el único n que contribuye es n = 2 y la parte del peine es −½v_2 c_0(log 2 − d), que vale
−½v_2 ≠ 0 en d = log 2. Contradicción. ∎

(d) Consecuencias (PROVED a partir de (a)–(c) y de las definiciones de cada clase):
- Núcleos totalmente positivos, o signo-regulares de orden 1 (todas las entradas de un mismo signo): excluidos por
  (a)–(b): para M grande existe un par m > k con log(m/k) ∈ (θ_0, log 2 − θ_0) (densidad de los log(m/k)), así que
  𝔸_M tiene entradas > 0 (diagonal) y < 0. La positividad total exige en particular entradas ≥ 0.
- Funciones de Pólya (PF₂ o más): requieren 𝖡 ≥ 0 y log-cóncava; excluidas por (a).
- Matrices de Green de la recta o de un árbol, semiseparables de rango ≤ r (las que se cierran bajo complemento de
  Schur con parámetros explícitos): para puntos ordenados x_1 < … < x_M exigen 𝖡(x_j − x_i) = Σ_{l≤r} u_l(x_i)w_l(x_j)
  para i < j; para un núcleo de diferencias continuo y para todos los M esto fuerza (ecuación funcional de
  d'Alembert/Levi-Civita, CITED) que 𝖡|_{(0,∞)} sea una suma finita de exponenciales-polinomio, excluida por (c).
- Matrices f(mcd): las entradas sobre primos distintos serían constantes f(1); 𝖡(log p − log q) no es constante
  (`ROUND_003_7` Lema 1, pasos 2–3). Excluidas.
- Funciones condicionalmente definidas positivas de orden 1: no se cierran bajo eliminación en el sentido pedido y
  su positividad sobre vectores de suma nula es más débil que el objetivo; no aportan pivotes. ARGUED.
- Núcleos de tipo Green en la recta para la parte Near sola: Near_{mk} = ½Σ v_n c_0(log n − log r) es la
  convolución de la medida del peine con c_0 de soporte compacto; por el mismo argumento de analiticidad no es
  semiseparable de rango acotado. PROVED (c_0 ≠ 0 de soporte compacto no es exponencial-polinomio).

Todo el Lema C es arquimediano o de formato: vale para cualquier peso con a(2) ≠ 0. NO-GO de formato, sin signo.

## Resultado

**Sin mecanismo nuevo.** Tres piezas de delimitación PROVED (Lemas A, B, C; la parte (d) de A usa el teorema de los
números primos, CITED): el grafo de acoplamiento de 𝔸_M está descrito; la casi-divisibilidad no es un orden parcial
y su patrón es, salvo razones acotadas, un semiorden de umbral independiente del peso; 𝖡 no pertenece a ninguna
clase cerrada bajo eliminación de las examinadas. Sin candidata lista para construcción.

## Qué se probó

- Lema A: Div en k | m; Near en pares con algún n ≥ 2, a(n) ≠ 0, |log(kn/m)| < θ_0 (exige m/k > 2e^{−θ_0}); Arch en
  todos los pares, negativa fuera de la banda |log(m/k)| ≤ θ_0. El patrón de Div + Near es el mismo para todo cΛ y
  cambia para a_P sólo en razones acotadas.
- Lema B: ⊲ no es transitiva (1 ⊲ 2 ⊲ 6, no 1 ⊲ 6, para θ_0 < log(7/6)); su clausura está en el semiorden de umbral y
  lo llena en razones ≥ R_0. Pivotes determinados por el patrón: NO-GO de clase (ciegos a cΛ, a f_t con λ₁ > n_*).
- Lema C: con 4T_0 < log 2, 𝖡 < 0 en (θ_0, log 2 − θ_0), 𝖡(0) > 0, 𝖡|_{(0,∞)} no es transformada de Laplace; excluye TP,
  PF₂, Green/semiseparable de rango acotado, f(mcd).

## Qué falló y por qué

- El patrón m ≈ kn no es escaso (casi completo fuera de la banda) ni estructurado aritméticamente: la aritmética
  vive en los valores de Near, no en su soporte. Un factor con soporte en el patrón y pivotes leídos de los valores
  es la LDL circular (J3).
- 𝖡 cambia de signo y no es analítica en (0, ∞): ninguna de las clases clásicas de cierre bajo eliminación aplica.
  Las razones son arquimedianas (γ_j > 0) y de soporte compacto de c_0; genéricas en el peine.
- La deconvolución en el «semigrupo de intervalos» devuelve el peine Σ v_n δ_{log n}, no pivotes.

## Qué queda NO excluido

- W con soporte en el grafo y valores dados por una fórmula propia no derivada de 𝔸_M (ninguna escrita).
- Cierre bajo eliminación de la **familia** {𝔸_M} que use los valores exactos de Λ (por ejemplo, que el complemento
  de Schur al eliminar el sitio M sea 𝔸_{M−1} para otro peso explícito a′, o para otro perfil F_0′); no examinado.
- Clases cerradas bajo eliminación distintas de las del Lema C (por ejemplo, matrices de desplazamiento de rango
  bajo con generador aritmético); no examinadas.
- Las demás reducciones PROVED ((L2), escalera, perfil continuo).

## Siguiente paso concreto

1. Anotar en el índice (06 §R9), en el grid y en el ledger: «𝔸_M con factor soportado en m ≈ kn: patrón = semiorden
   de umbral salvo razones acotadas, ciego a cΛ (ROUND_004_D Lemas A–B); 𝖡 fuera de TP/PF₂/Green/f(mcd) (Lema C);
   NO-GO de formato, sin signo».
2. La única pregunta concreta que queda de esta zona: ¿existe un peso explícito a′ (función de Λ) tal que el
   complemento de Schur de 𝔸_M^{Λ} respecto de un sitio sea, exactamente, una matriz 𝔸^{a′} de la misma familia?
   Antes de derivar, cotejarla con R3-b/J2 (si a′ es afín en Λ con coeficientes independientes del peso, cae allí)
   y con la fase 70 (Riccati/Darboux, J8), que es el antecedente natural de «el complemento es la misma familia con
   peso transformado».
