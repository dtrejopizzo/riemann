# Ronda 1, memo A — Candidata K1: realización de Gram desde el separador exacto con Poisson y el factor arquimediano

Memo de selección. Objetivo (★): λ_A(T) ≥ 0 para todo T > 0, con las definiciones de
`../phase-211-sign-sandbox/STATEMENT_001.md`. Pregunta de diseño: si el separador exacto
Σ_{d|n}Λ(d) = log n, usado junto con la sumación de Poisson sobre los enteros (coeficientes b ≡ 1) y el
factor arquimediano a conductor 1, puede convertirse en una identidad de Gram (G) de `OBJECT_SPEC.md` §1
con V_T no lineal en los valores exactos Λ(n), en particular mediante la relación de grado dos
Λ·log + Λ∗Λ = μ∗log².

Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO. Sin cómputos.

**Veredicto anticipado: sin mecanismo nuevo.** El cotejo identifica repetición en la clase de
multiplicadores y derivación (no independencia) en la clase con X, J y 𝓕. Según la regla 3 del brief la
memo no construye objeto. Se registran, con demostración, las tres piezas algebraicas que explican por
qué la relación de grado dos no produce un cuadrado orientado (§3); dos de ellas no figuran literalmente
en las fuentes cotejadas y no son resultados de signo.

Notación (P47 sec:firstcontact). X = multiplicación por t; V_a traslación; J reflexión;
𝓜 = m(D); 𝓕 = u_∞(D)J, con 𝓕² = 1, 𝓕* = 𝓕, JX = −XJ, X + 𝓕X𝓕 = 𝓜. Para α: ℕ → ℂ,
Φ(α) = Σ_n α(n) n^{−1/2} V_{−log n}; S = Φ(1), L = Φ(Λ), S′ = Φ(log), S″ = Φ(log²), L′ = Φ(Λ·log),
con subíndices N, M para las truncaciones n ≤ N, d ≤ M. Φ(α)Φ(β) = Φ(α∗β) (sin truncar) y
[X, Φ(α)] = −Φ(α·log). A = 𝓜 − L − L*; a_T(F) = ⟨F, A F⟩ para F ∈ L²(I_T) en el dominio de forma
(sólo intervienen d < N = e^{2T}).

---

## 0. Fuentes cotejadas

P47: thm:PCfinite, rem:Sren, prop:GEgap, prob:annihilate, prop:annihilate-equiv, rem:returnremarks,
prop:opcalc, thm:sos y su extensión a frecuencias reales, rem:sosatoms, prop:cone, lem:shape-ident,
thm:noimport, rem:conjunctions, rem:spec-scope, def:ext (mapa de sumación). P48: nota de alcance tras
req:spec, códigos F1–F3, fila «Selberg difference channel». Fase 211: LEDGER C33, C33b, C47;
ROUND_015_B §§3.4, 4.1; ROUND_023_A Lema 2.1; ROUND_022_A Lema 3.1; POWER_GLOBAL_ROUTE_REVIEW §1,
«Retorno a (S)», «Selberg completo», «Covarianza divisorial agrupada», «El resto divisorial es
indefinido», «Extensión factorial antes de resonancia», «Control de la sustitución ortogonal». Fase 188:
N_BUILD_018, N_BUILD_019, N_BUILD_022 §1. Fase 204: P1_BBSTAR_001 §§2.6–2.8. Fase 162: R162_2301
(Lema S), R162_501, R162_502 (M_T(Λ) = ZXZ⁻¹ − X), R162_901. Índice: README (NODE_001 Prop N.2 y
candidatas (a)–(c); AUDIT_206_001; A_MU_FACTORIZATION_001 (e)); 04 filas G6C-R166_502, G6C-R162_501/901,
G6A-R163_802, G4A-R164_502, G6C-R166_103A; 06 (TB-3, R186_005). Grid §§ de testigos y «Already NO-GO»
(canal de diferencias de Selberg). Crucigrama: fila TB-3.

---

## 1. Cotejo

**(1) Antecedente más cercano.** Son tres, y entre los tres cubren la pregunta entera.

- Uso conjunto, de grado uno, de las tres entradas: P47 thm:PCfinite,
  S_N A_M 𝓕 = {X, E_N} − L_M* E_N − J H_{M,N} − H_{M,N} 𝓕, con E_N el defecto de Poisson y H_{M,N} la
  hipérbola de divisores incompleta; su cuadrado es invariante por A ↦ −A (código F2), y la forma
  orientada que haría falta es prob:annihilate, que prop:annihilate-equiv identifica con (★). El mismo
  contenido en la imagen del mapa de sumación: 211 C33/C33b («peine sobre colas de Poisson
  = 2⟨𝒯_log u, 𝒯u⟩»), con libro mayor robusto frente al peine.
- Grado dos en la clase de multiplicadores: fase 204 P1_BBSTAR_001 §2.8 (PROVED): L² = Φ(Λ₂) − Φ(Λ·log);
  S_T²/4 = (Im ℓ)² + peine de (Λ₂ − Λ·log); σ_T = |1 − ℓ|² + (m − 1 − |ℓ|²); toda compleción de cuadrado
  cae en la extensión de thm:sos. «Selberg entra en 𝒞², no en 𝒞*𝒞.» Igual contenido en
  POWER_GLOBAL_ROUTE_REVIEW «Selberg completo» (Re⟨g, B²g⟩ = ‖Bg‖² − ½‖(B − B*)g‖²) y en la fila
  G6C-R166_502 del índice («Selberg actúa sobre V² y no sobre V∗V»; repetición de E70_11/12).
- Genericidad de las relaciones de tipo Selberg: índice README NODE_001 Prop N.2 (PROVED: valen para
  toda serie de Dirichlet; a_P, cΛ, DMV, DH las cumplen), R186_005 Thm TB3-neg (todo grado),
  AUDIT_206_001 («Selberg en la ventana: identidad universal, log es una derivación»); forma operatorial
  en 211 ROUND_023_A Lema 2.1 (C47), usada allí en una variación primera sin palanca.

**(2) Objeto o afirmación realmente nuevos.** Ninguno que lleve signo. No se encontró un mecanismo que
difiera de los antecedentes: en la clase de multiplicadores la pregunta está respondida (P1_BBSTAR §2.8,
thm:sos, N019); fuera de ella (operadores con X, J, 𝓕) la relación de grado dos no es una entrada
independiente sino la regla de Leibniz aplicada a la de grado uno (Lema B, §3), de modo que la candidata
se reduce a thm:PCfinite y a prob:annihilate sin añadirles nada. Lo único que esta memo aporta son tres
enunciados algebraicos de registro (§3): simetría especular del álgebra formal (Lema A), defecto de
grado dos derivado del de grado uno (Lema B), y traza nula de la parte linealizable (Lema C, que es
rem:sosatoms y P1_BBSTAR §2.8 en otra redacción). Ninguno es un paso de signo.

**(3) Por qué el cambio evitaría la dificultad del antecedente.** No la evita. La dificultad de
thm:PCfinite es que su contenido orientado está en los defectos E_N y H_{M,N} y sólo aparece en forma
bilineal entre dos vectores distintos; el grado dos produce el defecto L_M H_{M,N} − [X, H_{M,N}]
(Lema B), que está en el ideal izquierdo generado por H y [X, H], se anula exactamente donde se anula el
de grado uno y no contiene dato orientado nuevo. La dificultad de P1_BBSTAR §2.8 es que Selberg
linealiza ℓ² y no |ℓ|²; eso es una propiedad de la relación, no del modo de usarla (Lema C).

**(4) Identidad o desigualdad que conectaría con la positividad global.** No hay ninguna nueva. La única
conexión exacta disponible es la ya registrada: thm:PCfinite despejada,
⟨F, A_M F⟩ = ⟨(S_N^{−1})* F, [{X, E_N} − L_M* E_N − J H_{M,N} − H_{M,N} 𝓕] 𝓕 F⟩ (formal en S_N^{−1}),
bilineal en dos vectores distintos y sin signo. Lo que falta está señalado en §4.

**(5) Línea que se rompe para cΛ y a_P (ítem (5) de `OBJECT_SPEC.md` §4).** No hay identidad (G) cuya
línea pueda romperse. Sí se puede señalar la línea de identificación, que es la misma en grado uno y en
grado dos (Lema B): «H_{M,N} no tiene coeficiente en k ≤ N». Para pesos a con δ(k) = Σ_{d|k}a(d) − log k,
el defecto interior de grado uno es δ(k) y el de grado dos es (a∗δ)(k) + δ(k) log k. Para cΛ,
δ(k) = (c − 1) log k ≠ 0 en todo 2 ≤ k ≤ N; para a_P, δ(k) = −Σ_{p<P} v_p(k) log p, no nulo en k = 2
(y, si P > N, igual a −log k en todo k ≤ N). En ambos casos la identidad sigue siendo una identidad,
con un término interior más; como ningún paso posterior firma nada, eso no constituye la ruptura que
exige O4. Por la cláusula final de `OBJECT_SPEC.md` §4, **la candidata no está lista para construcción.**

El cotejo identifica repetición. Lo que sigue es el registro de la obstrucción, pedido para esta memo;
no es una construcción.

---

## 2. Respuesta a los cinco obstáculos conocidos

(i) *thm:sos / N019 (cuadrados aritméticos puros imposibles para T ≥ ½log3).* Vigente y no esquivado. La
relación de grado dos vive en el álgebra de multiplicadores; un cuadrado formado con L, L′, Φ(Λ₂), Φ(μ)
es un cuadrado de polinomio casi periódico y cae en la extensión de thm:sos a frecuencias reales
(P1_BBSTAR Thm P1.A). Con parte definida positiva libre es la clase dual (N019 Prop 1). CITED.

(ii) *prop:opcalc / N018 (identidades lineales en la autocorrelación más Bochner).* Para salir de la
clase hay que usar operadores que no sean multiplicadores: X, J, 𝓕, Q_T. Es lo que hace thm:PCfinite.
Pero respecto de esos operadores Selberg no es una relación nueva: es ad_X aplicada a
[X, S] = −LS (Lema B). Toda consecuencia de «Poisson + arquimediano + Selberg» es consecuencia de
«Poisson + arquimediano + Λ∗1 = log + Leibniz». PROVED (Lema B).

(iii) *prob:annihilate exige identidad orientada.* El álgebra formal de las tres entradas es invariante
por una involución que envía A a −A (Lema A); por tanto ninguna consecuencia formal está orientada, de
ningún grado. La orientación está sólo en la manera en que las relaciones fallan en la realización:
h_{M,N}(k) ≥ 0 con soporte en k > N, y la estructura de E_N. El grado dos hereda h₂ = Λ∗h + h·log ≥ 0,
que es consecuencia de h ≥ 0 y Λ ≥ 0, no un dato nuevo. PROVED (Lemas A, B); la positividad de
coeficientes no es positividad de forma (CITED: «El resto divisorial es indefinido incluso sobre tests
pares primitivos»).

(iv) *Extensión factorial: D + E sin firmar.* K1 no aporta nada a D + E. La extensión factorial ya usa el
separador en forma de mcd (log mcd(q, r) = Σ_{m|q, m|r} Λ(m), núcleo semidefinido positivo), y el resto
contiene el núcleo ½(log λ + log μ), de la forma u(λ) + u(μ), con exactamente un autovalor positivo y
uno negativo. El grado dos ofrece el núcleo de rango uno log λ · log μ, que es semidefinido positivo y
sólo puede pagar uno de los dos signos:
u(λ) + u(μ) = (1/2ε)(1 + εu(λ))(1 + εu(μ)) − 1/(2ε) − (ε/2)u(λ)u(μ). La signatura (1,1) no cambia.
PROVED (identidad elemental); no es una exclusión de la compensación conjunta de D + E.

(v) *C33b (libro mayor de Λ∗1 = log robusto frente al peine).* Vigente. El libro mayor de grado dos se
obtiene del de grado uno por derivación en la escala (Lema B), y la derivación conserva la robustez:
si el de grado uno sobrevive a cΛ, c < 1, y a a_P, el de grado dos también, con el mismo primer índice
de fallo de la identificación. ARGUED (la parte PROVED es el Lema B; no se rehízo el libro mayor).

---

## 3. La obstrucción algebraica, registrada

### Lema A (simetría especular del álgebra formal; PROVED)

Sea 𝔸 un álgebra asociativa con unidad y elementos X, J, 𝓕, S, L tales que: J² = 𝓕² = 1; JX = −XJ;
S y L pertenecen a una subálgebra conmutativa 𝒯 estable por t ↦ t^♭ := JtJ; S es invertible en 𝒯; y

    (a) 𝓜 := X + 𝓕X𝓕 satisface J𝓜J = 𝓜;   (b) S𝓕 = JS;   (c) [X, S] = −LS.

Entonces: (1) 𝓜 = L + L^♭, es decir A := 𝓜 − L − L^♭ = 0. (2) La sustitución
X ↦ X, J ↦ J, 𝓕 ↦ 𝓕° := J𝓕J, S ↦ S⁻¹, L ↦ −L conserva todas las hipótesis y envía 𝓜 ↦ −𝓜, A ↦ −A.

*Demostración.* (1) De 𝓕² = 1, 𝓜𝓕 = X𝓕 + 𝓕X. De (c), SX = XS + LS. Entonces, con (b), JX = −XJ y
JL = L^♭J,

    S𝓜𝓕 = SX𝓕 + S𝓕X = (XS + LS)𝓕 + JSX = XJS + LS𝓕 + J(XS + LS)
         = XJS + LS𝓕 − XJS + L^♭JS = (L + L^♭)S𝓕.

Como 𝒯 es conmutativa, S(𝓜 − L − L^♭)𝓕 = 0, y S, 𝓕 son invertibles.
(2) (𝓕°)² = 1. Para (c): [X, S⁻¹] = −S⁻¹[X, S]S⁻¹ = S⁻¹LSS⁻¹ = LS⁻¹ = −(−L)S⁻¹. Para (b): de (b),
𝓕 = S⁻¹JS, luego 𝓕° = (JS⁻¹J)·S·J = (S^♭)⁻¹SJ y S⁻¹𝓕° = (S^♭)⁻¹J = JS⁻¹JJ = JS⁻¹. Para (a):
X + 𝓕°X𝓕° = X + J𝓕(JXJ)𝓕J = X − J𝓕X𝓕J = X − J(𝓜 − X)J = X − 𝓜 − X = −𝓜, y J(−𝓜)J = −𝓜. Por
último −𝓜 − (−L) − (−L)^♭ = −A. ∎

*Lectura.* En la realización, (a) es exacta (L^♭ = L*); (b) es Poisson para b ≡ 1 y (c) es Λ∗1 = log,
ambas válidas sólo con defectos (E_N; H_{M,N}); (1) con defectos es thm:PCfinite (CITED). La imagen
especular es el sistema (peine de Möbius, pesos −Λ, factor arquimediano inverso). Consecuencia: toda
identidad deducida formalmente de (a), (b), (c) —en particular toda la que use la relación de grado dos,
que es consecuencia de (c) por el Lema B— tiene una gemela con A cambiado de signo; una identidad
«A = Σ V_i*V_i + ρ» obtenida así tendría gemela «−A = Σ V°_i*V°_i + ρ°», y ambas sólo dicen A = 0, que
es (1). **El álgebra formal de las tres entradas no contiene orientación, en ningún grado.** La
orientación entra exclusivamente por la asimetría de los defectos entre el sistema y su imagen: para el
peine entero, h_{M,N} ≥ 0 con soporte fuera de [1, N] y E_∞ es de rango dos (términos polares) sobre el
núcleo de Schwartz; para el peine de Möbius no vale ninguna de las dos cosas. Esto precisa la condición
(ii) de prob:annihilate y el código F2 de P48; no los supera. No se localizó el enunciado (2) literal en
las fuentes cotejadas; no se afirma más que eso.

### Lema B (el defecto de grado dos es derivado; PROVED)

Para pesos cualesquiera a (en lugar de Λ), M, N ≥ 1, sean L_M = Φ_{≤M}(a), L′_M = Φ_{≤M}(a·log),
H_{M,N} = L_M S_N − S′_N y H⁽²⁾_{M,N} := (L′_M + L_M²) S_N − S″_N. Entonces, sobre el núcleo de Schwartz,

    H⁽²⁾_{M,N} = L_M H_{M,N} − [X, H_{M,N}].

Sin truncar, con h = a∗1 − log y h₂ = (a·log + a∗a)∗1 − log²: h₂ = a∗h + h·log.

*Demostración.* [X, L_M] = −L′_M, [X, S_N] = −S′_N, [X, S′_N] = −S″_N. Luego
[X, H_{M,N}] = −L′_M S_N − L_M S′_N + S″_N = −L′_M S_N − L_M(L_M S_N − H_{M,N}) + S″_N
= −H⁽²⁾_{M,N} + L_M H_{M,N}. La versión en coeficientes: log·(a∗1) = (a·log)∗1 + a∗log, de donde
h·log = (a·log)∗1 + a∗log − log², y a∗h = a∗a∗1 − a∗log; se suma. ∎

*Consecuencias (PROVED).* (1) Para a = Λ y M ≥ N, H no tiene coeficientes en k ≤ N (thm:PCfinite), y
entonces H⁽²⁾ tampoco: L_M H tiene coeficientes en múltiplos propios de índices > N, y [X, ·] conserva el
soporte. La relación de grado dos «en k ≤ N» es la de grado uno. (2) Para pesos a con a(1) = 0, si k₀ es
el primer índice con δ(k₀) ≠ 0, el defecto de grado dos en k₀ es δ(k₀) log k₀: ambos grados fallan en la
misma línea y en el mismo índice. La relación de grado dos no separa nada que la de grado uno no separe
(coincide con R162_2301 Lema S: Selberg ⟺ a = Λ, por recursión). (3) Si h ≥ 0 y a ≥ 0 entonces
h₂ ≥ 0: el único dato orientado del grado dos es consecuencia del de grado uno. (4) Por iteración, lo
mismo vale en todo grado: el defecto de grado j está en el ideal izquierdo generado por
H, [X, H], …, ad_X^{j−1}(H).

### Lema C (la parte linealizable tiene traza nula; PROVED, con CITED para el aislamiento de átomos)

Sea T > ½ log 3 y L = Φ_{<N}(Λ) el peine en la ventana. Sean V_i = α_i + β_i L + γ_i L*, i ≤ r, con
α_i, β_i, γ_i ∈ ℂ. Si la forma Σ_i ‖V_i F‖² coincide sobre P_T con ∫ Re c_F dν para una medida finita ν
en (−2T, 2T) con átomos sólo en {0} ∪ ±log ℕ, entonces β_i = γ_i = 0 para todo i.

*Demostración.* V_i*V_i = |α_i|² + (ᾱ_iβ_i + γ̄_iα_i)L + (ᾱ_iγ_i + β̄_iα_i)L* + (|β_i|² + |γ_i|²)L*L
+ β̄_iγ_i L*² + γ̄_iβ_i L². Los átomos de L, L* están en ±log de potencias de primos; los de L², L*² en
±log(mn) con m, n ≥ 2, de módulo ≥ log 4; L*L = Σ Λ(m)Λ(n)(mn)^{−1/2}V_{log n − log m}. El punto
log(3/2) ∈ (0, 2T) no es ±log de un entero y 3/2 = n/m con n, m potencias de primos sólo para
n = 3, m = 2 (2n = 3m obliga n = 3k, m = 2k, y k = 1). Luego el átomo de Σ_i V_i*V_i en log(3/2) es
(log 2 · log 3/√6) Σ_i(|β_i|² + |γ_i|²). Dos medidas que definen la misma forma sobre P_T tienen los
mismos átomos en (0, 2T) (CITED: argumento de aislamiento de rem:sosatoms). Luego la suma es cero. ∎

*Lectura.* En las variables x = Re ℓ, y = Im ℓ del símbolo ℓ de L, una suma de cuadrados de grado uno
tiene parte cuadrática semidefinida positiva; las formas cuadráticas con átomos enteros —las que la
relación de grado dos linealiza, Re ℓ² = x² − y² e Im ℓ² = 2xy, por L² = Φ(Λ₂) − L′ módulo átomos
≥ 2T— son las de traza nula. Semidefinida positiva y traza nula implica nula. La relación de grado dos
es una identidad del anillo del semigrupo log ℕ, sin involución; la positividad necesita la involución,
que saca del semigrupo a log ℚ_{>0}. Es rem:sosatoms y P1_BBSTAR §2.8 en redacción de traza; se registra
porque responde literalmente a la pregunta «qué impide que una relación de tipo Selberg dé un cuadrado
con la orientación correcta» en esta clase. Para grado mayor en (L, L*, L′, …) no hace falta lema
propio: la extensión de thm:sos cubre todo polinomio casi periódico (CITED).

### Observación D (orden en la derivación; ARGUED)

El separador hace entrar a Λ por la derivación ad_X: L = −[X, S]S⁻¹, esto es X + L = SXS⁻¹
(CITED: R162_502, N_BUILD_022 §1). El peine de a_T es de primer orden en ad_X; los cuadrados formados
con X y S son de orden cero o dos. Por ejemplo, para G en el dominio natural,
‖(X + L)G‖² − ‖XG‖² − ‖LG‖² = 2Re⟨XG, (Re L)G⟩ − Re⟨G, L′G⟩ (PROVED: XL + L*X = {X, Re L} − ½(L′ + L′*)),
que produce el peine de Λ·log, no el de Λ. Bajar un orden exige integrar en la escala, lo que lleva a
los pesos Λ/log (cono homogéneo de O10, que cΛ conserva) y a la divergencia separada de las dos piezas
registrada en «Selberg completo» (CITED). La relación de grado dos es la regla de Leibniz de segundo
orden y da información de tipo convexidad en la escala, familia cerrada «transporte en σ»
(RULES_AVOID §C). No se presenta como teorema.

---

## 4. La pieza que falta, señalada con precisión

Por los Lemas A y B, un objeto de tipo K1 sólo puede obtener orientación de los dos hechos que la
imagen especular no comparte: (α) h_{M,N}(k) ≥ 0, con soporte en k > N; (β) la forma de E_N. Un dato de
coeficientes no negativos sólo firma una forma si se aparea con funciones no negativas. La pieza que
falta es entonces una identidad del tipo

    a_T(F) = ‖V_T F‖² + Σ_{k>N} h_{M,N}(k) |ℓ_k(F)|² + (términos polares escritos como cuadrados),

con ℓ_k funcionales lineales explícitos de F (OPEN; no se encontró ninguna). En thm:PCfinite los
términos de H aparecen como ⟨Y, V_{−log k} 𝓕F⟩ con Y = (S_N^{−1})*F ≠ 𝓕F: apareamientos entre dos
vectores distintos, no módulos al cuadrado. Convertirlos en diagonales es exactamente lo que piden las
condiciones (ii)–(iii) de prob:annihilate; no es un objetivo nuevo, y prop:annihilate-equiv lo
identifica con (★). No se propone como candidata: falta la operación.

---

## 5. Batería de falsificadores

No hay paso de signo que someter a la batería. Para las relaciones usadas: cΛ (c ≠ 1) y a_P rompen (c)
en el primer índice (§1 (5)), en grado uno y dos por igual; borrado y amplificación finitos rompen (c)
en el primer índice modificado y en sus múltiplos; Davenport–Heilbronn y Epstein no tienen pesos de
tipo derivada logarítmica soportados en potencias de primos, con lo que (c) no se plantea con b ≡ 1;
un sistema de Beurling cumple (c) en su propio semigrupo y pierde (b); b_θ rompe (c). Para los modelos
de cuarteto y f_t, que conservan Λ(n) en la ventana y la ecuación funcional, las tres relaciones
(a), (b), (c) siguen valiendo en la ventana y no los separan: consistente con que ninguna consecuencia
de ellas lleva signo (Lema A) y con P47 cor:shape (a). Esta última frase es ARGUED: no se verificó
contra las definiciones de esos modelos en P47 más allá de lo que resume `RULES_AVOID.md` §E.

---

## Resultado

**Sin mecanismo nuevo.** K1, tal como está planteada (separador exacto + Poisson con b ≡ 1 + factor
arquimediano, con no linealidad aportada por la relación de grado dos), repite: P47 thm:PCfinite /
prob:annihilate en la clase con X, J, 𝓕; P1_BBSTAR_001 §2.8, thm:sos y N019 en la clase de
multiplicadores; NODE_001 Prop N.2 y TB3-neg en cuanto a genericidad. No se escribe (ℋ_T, V_T, ρ_T). No
es un NO-GO de la conjunción (E)∧(F)∧(I) con paso no lineal, que sigue sin falsificador común
(rem:conjunctions): lo que se descarta es que la relación de grado dos sea ese paso.

## Qué se probó

- Lema A (PROVED): las relaciones (a), (b), (c) implican A = 0 y son invariantes por una involución
  que cambia A en −A; el álgebra formal no tiene orientación en ningún grado.
- Lema B (PROVED): H⁽²⁾ = L_M H − [X, H] para pesos y truncaciones cualesquiera; h₂ = a∗h + h·log; el
  grado dos falla en la misma línea e índice que el grado uno y su positividad de coeficientes es
  heredada.
- Lema C (PROVED, aislamiento de átomos CITED): una suma de cuadrados de grado uno en (L, L*) con
  átomos enteros es constante, T > ½ log 3; la parte que Selberg linealiza tiene traza nula.
- Identidad de signatura del núcleo u(λ) + u(μ) frente al núcleo de rango uno (PROVED, elemental).

## Qué falló y por qué

- Compleción de cuadrado con L: genera |ℓ|², con átomos en log(p/q); Selberg sólo conoce ℓ². Falla la
  identidad «Σ|V_i|² tiene átomos enteros», por el átomo (log 2 · log 3/√6) Σ(|β_i|² + |γ_i|²) en
  log(3/2).
- Cuadrados con X y S: son de orden cero o dos en ad_X y producen el peine de Λ·log; el peine de Λ es de
  orden uno.
- Uso del grado dos en la identidad de Poisson–Chebyshev: no añade relación (Lema B) ni orientación
  (Lema A).
- No se obtuvo ninguna identidad que convierta h_{M,N} ≥ 0 en una suma de módulos al cuadrado.

## Siguiente paso concreto

No relanzar K1 con otra relación del anillo de Dirichlet (grado tres, Vaughan, identidades de
convolución): el Lema B las deriva de (c) y el Lema A les quita la orientación. Una reapertura exige
una operación explícita que diagonalice los apareamientos de H_{M,N} y E_N de thm:PCfinite (los ℓ_k de
§4) y los cuatro puntos del filtro. Líneas propuestas para quien mantenga los registros (esta memo no
edita otros archivos):

- LEDGER de la fase, K1: «SIN MECANISMO NUEVO — grado dos = Leibniz de Λ∗1 = log (Lema B); álgebra
  formal sin orientación (Lema A); traza nula (Lema C); falta la diagonalización de H_{M,N}, E_N».
- Índice de rutas y grid: «Relación de grado dos (y superiores) del anillo de Dirichlet como paso no
  lineal de la conjunción separador + Poisson + arquimediano: repetición de thm:PCfinite /
  P1_BBSTAR §2.8 / Prop N.2; Lemas A, B, C PROVED en ROUND_001_A de la fase 212; no es NO-GO de la
  conjunción».
