# Ronda 5, semilla G1: objeto de grado ≥ 3 cuya hessiana sea la forma

Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`. Se trabaja en un sector de paridad
L²_±(I_T) (F(−t) = ±F(t)); allí B = ±A, y P_T ∩ L²_± = ker A ∩ L²_±, hiperplano del sector. Todas las
formas son reales. «n₊(H)» es la dimensión máxima de un subespacio donde H > 0.

Veredicto propio: **no logré escribir un objeto que cumpla A1–A6.** Lo que sí queda escrito es la
clase entera de objetos que pide la semilla (§1), la identidad exacta que los liga a a_T (§2) y un
lema de dicotomía con clase declarada (§3) que explica por qué el grado ≥ 3 no aporta una fuente
independiente de signo en las cuatro familias de certificados de hiperbolicidad que conozco
(determinantal, cambio de variables no negativo, producto de factores, generatriz exponencial). La
familia «producto» es la única donde el producto de Euler entra; se reduce a la certificación local de
`phase-159/G2_B8_R5.md` (Teor. D, L″).

## 0. Cotejo (va primero, BRIEF regla 3)

1. **Antecedente más cercano**, leído en primaria: `phase-160-row-d-infinite-T/R160_C7_R1.md` §6.2
   (la clase lorentziana de grado dos, el cierre por límites y Alexandrov–Fenchel se reducen al
   enunciado) y §6.3(2) (subir de grado: candidatos Str(Γ_F^k) sin transpuesta, o con transpuesta y
   torcidos por Φ_F^{k−2}; OPEN por falta de una fuente independiente de coeficientes no negativos).
   Segundo antecedente, leído en primaria: `phase-159-row-d-two-front-construction/G2_B8_R5.md` Def. 1,
   Lema 2.1, Teor. D y Teor. L″ (certificación local por factor de Euler: no existe para T ≥ 0.5925).
   Tercero: `phase-195-modern-tools/INV_M_001` §§1–3 (estabilidad real y Gårding aplicados a la forma
   definida del bloque 𝔸; leído §§0–2). Cuarto: R4-c (`REVIEW_004.md`; el formato «objetivo con
   margen»), leído vía la revisión.
2. **Qué es nuevo aquí:** el examen de la hessiana de un polinomio hiperbólico de grado d ≥ 3 en el
   punto base y la dicotomía del Lema 3 (los coeficientes de grado ≥ 3 sólo pueden entrar como margen
   a_T ≥ c|·|^{2/k}); la identificación de cada clase de certificados con (G) con ρ = 0 o con la
   certificación local de G2_B8. R160_C7_R1 §6.3(2) sólo examinó Str(Γ_F^k).
3. **Por qué esto no esquiva la dificultad:** porque el Lema 3 prueba que no la esquiva; ver §3.
4. **Identidad con la positividad global:** Lema 1 (equivalencia exacta del objetivo en un sector con
   «n₊(H_{e,κ}) ≤ 1») más la identidad de autovalores hiperbólicos (Lema 2).

No abiertos en primaria: Paper 46; Paper 47 thm:parityschur y prop:polarcap (sólo vía `REVIEW_004`);
`ROUND_004_B.md` (sólo vía `REVIEW_004`); fase 120 y 114_d_244 (sólo vía `ANNEX_COTEJO_LORENTZ_1.md`);
`SURVEY_MODERN_UNTRIED.md` B1 y `FAMILIES_A_001` A4 (sólo líneas de grep). Grep por «Renegar»,
«hyperbolic polynomial», «hiperbólico respecto», «triple correlation», «trilineal»: sólo los archivos ya
citados y P122_012 (una forma trilineal ajena a esto, línea 49). Esto no prueba novedad.

## 1. Objeto

**Espacio.** E_T^± := L²_±(I_T) (o cualquier compresión finita que contenga el punto base); el objeto
se define sobre compresiones finitas E ⊂ E_T^± ∩ 𝒟_T con e ∈ E, y «hiperbólico sobre E_T^±» significa
hiperbólico sobre toda compresión finita que contenga a e.

**Punto base.** Cualquier e ∈ E_T^± con A(e) ≠ 0; el natural es el vector de Tate del sector,
e_± := (e^{t/2} ± e^{−t/2})1_{I_T}.

**Forma objetivo en el punto base.** Para κ ∈ ℝ,

    H_{e,κ}(F) := −a_T(F) + (2/A(e)) A(F) a_T(e,F) + κ A(F)²,   F ∈ E_T^±.        (1.1)

**Objeto.** Un funcional p : E_T^± → ℝ homogéneo de grado d ≥ 3, polinómico en cada compresión finita,
con

    p(e) > 0,   D²p(e)[F,F] = H_{e,κ}(F)   para todo F,                            (1.2)

e hiperbólico respecto de e: para todo F el polinomio t ↦ p(F + t e) tiene sólo raíces reales.
Escribiendo p(te + F) = p(e) ∏_{i=1}^{d} (t + λ_i(F)), las λ_i(F) ∈ ℝ son los autovalores hiperbólicos
(1-homogéneos, continuos, no lineales en F).

Ejemplo trivial (muestra que la clase es no vacía si y sólo si vale el objetivo en el sector):
p = ℓ^{d−2}·q con q(F) := ½H_{e,κ}(F) + (term. en ℓ) y ℓ lineal, ℓ(e) > 0. No usa nada.

## 2. Identidad

**Lema 1 (PROVED).** Sea e con A(e) ≠ 0 y κ > −a_T(e)/A(e)². Entonces
(a) H_{e,κ}(e, F) = (a_T(e)/A(e) + κA(e)) A(F) y H_{e,κ}(e) = a_T(e) + κA(e)² > 0;
(b) H_{e,κ} = −a_T sobre P_T ∩ E_T^±;
(c) a_T ≥ 0 sobre P_T ∩ E_T^± ⟺ n₊(H_{e,κ}) ≤ 1.

*Prueba.* (a) Con ℓ := a_T(e,·)/A(e): H(e,F) = −a_T(e,F) + A(e)ℓ(F) + A(F)ℓ(e) + κA(e)A(F)
= A(F)(ℓ(e) + κA(e)), y ℓ(e) = a_T(e)/A(e). (b) A(F) = 0. (c) ⇒: H ≤ 0 en el hiperplano ker A, luego
todo subespacio donde H > 0 corta ker A sólo en 0 y tiene dimensión ≤ 1. ⇐: por (a), el H-ortogonal de
e es ker A. Si F ∈ ker A con H(F) > 0, en span{e, F} la matriz de H es diag(H(e), H(F)) > 0, y
n₊ ≥ 2. ∎

**Lema 2 (identidad de autovalores; PROVED, álgebra).** Si p es hiperbólico respecto de e con (1.2),
entonces para F ∈ P_T ∩ E_T^±

    Σ_i λ_i(F) = 0,     a_T(F) = p(e) Σ_i λ_i(F)².                                   (2.1)

*Prueba.* p(e + sF) = s^d p(e/s + F) = p(e)∏(1 + sλ_i(F)). El coeficiente de s es p(e)Σλ_i = Dp(e)[F];
por homogeneidad de Euler, D²p(e)[e,F] = (d−1)Dp(e)[F], y por (1.2) y el Lema 1(a) esto es múltiplo
de A(F) = 0. El coeficiente de s² es ½D²p(e)[F,F] = p(e)σ₂(λ) = ½p(e)((Σλ)² − Σλ²) = −½p(e)Σλ²; con
(1.2) y el Lema 1(b), −a_T(F) = −p(e)Σλ_i². ∎

(2.1) es una suma de cuadrados de funciones no lineales de F, exacta sobre todo P_T ∩ E_T^±: tiene la
forma de (G) con V_T F := √p(e)(λ_i(F))_i, salvo que V_T no es lineal. Pero su contenido es entero la
hiperbolicidad: la identidad es tautológica una vez que las raíces son reales.

## 3. Mecanismo, y por qué no funciona en las clases que sé escribir

**Teorema citado (CITED: Gårding 1959; Renegar 2006; Brändén–Huh 2020).** Si p es hiperbólico respecto
de e, D²p(e) tiene n₊ ≤ 1 (la derivada de Renegar D_e^{d−2}p es una cuadrática hiperbólica, de
signatura (1, ·)). Un polinomio con coeficientes ≥ 0 es lorentziano si y sólo si su soporte es M-convexo
y cada ∂^α p con |α| = d − 2 es una cuadrática con a lo sumo un autovalor positivo.

Con el Lema 1(c), la existencia del objeto da el objetivo en el sector. La única hipótesis abierta es
la hiperbolicidad. El lema siguiente muestra que basta (y hace falta) la hiperbolicidad sólo a lo largo
de las rectas e + sF, F ∈ P_T, y que allí los coeficientes de grado ≥ 3 no ayudan.

**Lema 3 (dicotomía del grado; PROVED).** Sea p homogéneo de grado d ≥ 3 con (1.2), y supóngase que
s ↦ p(e + sF) es real-raíz para todo F ∈ P_T ∩ E_T^±. Entonces para 3 ≤ k ≤ d y todo F ∈ P_T ∩ E_T^±

    |D^k p(e)[F^k]| ≤ k!·C(d,k)·p(e)^{1−k/2}·a_T(F)^{k/2}.                           (3.1)

En consecuencia, sobre ℝe ⊕ (P_T ∩ E_T^±) vale exactamente una de dos:
(i) D^kp(e)[F^k] = 0 para todo k ≥ 3 y todo F ∈ P_T; entonces
    p(αe + F) = α^{d−2}(α²p(e) − ½a_T(F)): el objeto es ℓ^{d−2} por una cuadrática, y su hiperbolicidad
    es la de la cuadrática, es decir n₊ ≤ 1 de grado dos: R160_C7_R1 Prop. 6.2 verbatim;
(ii) algún coeficiente de grado k ≥ 3 no se anula en P_T, y la hiperbolicidad implica el objetivo con
    margen a_T(F) ≥ c_{d,k} p(e)^{1−2/k} |D^kp(e)[F^k]|^{2/k}.

*Prueba.* Por el Lema 2, Σλ_i = 0 y Σλ_i² = a_T(F)/p(e), luego |λ_i| ≤ (a_T(F)/p(e))^{1/2}. El
coeficiente de s^k es D^kp(e)[F^k]/k! = p(e)σ_k(λ), y |σ_k(λ)| ≤ C(d,k) max|λ_i|^k. En el caso (i),
p(αe+F) = Σ_j α^{d−j}D^jp(e)[F^j]/j! se reduce a j ∈ {0, 2} (j = 1 se anula por el Lema 2). ∎

Para d = 3 el lema es exacto: con p(e) = 1 y Dp(e)[F] = 0, p(e+sF) = 1 − ½a_T(F)s² + c s³, c = p(F);
la cúbica x³ − ½a_T x + c (x = 1/s) es real-raíz si y sólo si a_T(F)³ ≥ 54·p(F)². La hiperbolicidad de un
objeto cúbico sobre P_T **es** la desigualdad a_T ≥ 54^{1/3}|p|^{2/3}: el objetivo reforzado.

**Lectura (PROVED como consecuencia del Lema 3).** Los términos de grado ≥ 3 no pueden ser fuente de
signo: en el caso (ii) son una cota inferior adicional que el objeto debe pagar; en el caso (i)
desaparecen. Es el patrón de R4-c (formato con defecto que suma = objetivo con margen), ahora en grado
mayor. Como λ_A(T) ≤ 4·10⁹Te^{−15.449T}, en (ii) los coeficientes D^kp(e)[F^k] deben ser
≤ C·λ_A^{k/2} sobre los casi-minimizantes: el objeto debería conocer los casi-minimizantes (patrón B9).
Esto último es ARGUED (no se probó que se anulen sólo allí).

**Clases de certificados de hiperbolicidad.** Lo único que quedaría es una prueba de la real-raíz de
s ↦ p(e+sF) que no use el signo de su coeficiente s². Las cuatro clases estándar:

**C1. Determinantal (PROVED).** p(x) = det(Σ_i x_iM_i), M_i simétricas, M(e) ≻ 0 (por ejemplo
det(tI + xE + y·𝒪_F) de la pista (iii)). Normalizando M(e) = I y X_F := M(F) (lineal en F):
p(e+sF) = det(I + sX_F), λ_i(F) = autovalores de X_F, y (2.1) es

    a_T(F) = ‖X_F‖²_HS   sobre P_T ∩ E_T^±,   con tr X_F = 0 allí.

Es (G) con ρ = 0 y V_T = X lineal: exactamente `OBJECT_SPEC.md` (G). El grado d = rango de X no
interviene. La pista (iii) no añade mecanismo: hay que escribir X_F, que es el problema original.

**C2. Cambio de variables no negativo de un lorentziano fijo (PROVED).** p = q∘𝒜 con q lorentziano en
ℝ^N (p.ej. un polinomio simétrico elemental) y 𝒜 lineal con 𝒜e en el ortante positivo. Entonces
D²p(e) = 𝒜ᵀD²q(𝒜e)𝒜, y D²q(𝒜e) = uuᵀ − GᵀG. Sobre P_T, como en el Lema 1(c), el H-ortogonal de 𝒜e se
diagonaliza explícitamente y a_T(F) = ‖W G𝒜F‖² con W = I − ww^T/(1 + √(1−|w|²)),
w = G𝒜e/(u·𝒜e), |w| < 1. Otra vez (G) con ρ = 0 y V lineal. Además, si las coordenadas son las de una
base {φ_i} con F = Σx_iφ_i y q con coeficientes ≥ 0, ∂_i²p(e) = H(φ_i) ≥ 0 exige a_T(φ_i) ≤ 0 + polar:
ninguna base con elementos localizados sirve, porque a_T(φ_ε) ≍ ‖φ‖² log(1/ε) (R160_C7_R1 Teor. 3(b),
CITED): es la obstrucción «diagonal −∞» de §6.2(a).

**C3. Generatriz exponencial (pista (ii); PROVED).** Z(F) = Σ_n w_n exp(ℓ_n(F)) (o ∫ dμ), w ≥ 0: log Z es
convexa y D² log Z(e)[F,F] = Var_{μ_e}(ℓ_·(F)) es una varianza. Si a_T = D² log Z(e) sobre P_T, es (G)
con ℋ = L²(μ_e) y V F = ℓ_·(F) − E ℓ_·(F), ρ = 0. La versión de Gårding (Z^{1/d} cóncava en un cono)
reduce, en el punto base, a la misma Cauchy–Schwarz invertida del Lema 1(c). Ni el cono {F ≥ 0} ni el
cono de momentos de Tate positivos dan nada: P_T está en el borde del segundo y {F ≥ 0} ∩ P_T = {0}
(una F ≥ 0 con ∫F e^{t/2} = 0 es nula).

**C4. Producto de factores hiperbólicos; aquí entra el producto de Euler (PROVED salvo lo citado).**
p = ∏_j p_j con cada p_j hiperbólico respecto de e (el producto lo es, y su cono es la intersección).
Entonces log p(e+sF) = Σ_j log p_j(e+sF) y, sobre P_T ∩ E_T^±,

    a_T(F) = Σ_j S_j(F),   S_j := −p(e)·D² log p_j(e) ⪰ 0 en todo E_T^±.             (3.2)

(Lema 2 aplicado a cada factor: S_j = p(e)Σ_i λ_i^{(j)}(F)², y Σ_j σ₁^{(j)} = 0 en P_T.)
(3.2) es una descomposición de a_T en formas semidefinidas positivas, una por factor, módulo términos
A·m que se anulan en P_T. Sin restricción sobre qué ve cada S_j la descomposición es trivial (S_1 = a_T).
Con la restricción que da sentido a «producto de Euler»:

- *Factor de Euler genuino (sin parte arquimediana).* S_p = −Q_p + A·m_p con
  Q_p(F) := Σ_k v_{p^k} Re c_F(k log p). **No es ⪰ 0 sobre P_T (PROVED).** Para log p < 2T, sea χ ∈ 𝒟
  par, de soporte de anchura < ½ log 2 cerca de 0, ψ := (¼ − ∂²)χ (entonces ∫ψ e^{±t/2} = 0, y lo mismo
  para sus trasladados) y F_± := ψ(· − ½log p) ± ψ(· + ½log p) ∈ P_T ∩ E_T^±. Entonces
  c_{F_±}(log p) = ±‖ψ‖², c_{F_±}(k log p) = 0 para k ≥ 2, y Q_p(F_±) = ±v_p‖ψ‖². En el sector par
  Q_p(F_+) > 0, luego S_p(F_+) = −v_p‖ψ‖² < 0; en el impar se usan dos pares de bultos con
  signos (+,+) a distancia log p separados simétricamente. Luego el factor de Euler aislado nunca es
  hiperbólico con esta hessiana, y la parte arquimediana tiene que repartirse entre los primos.
- *Factores de Euler con reparto arquimediano invariante por traslación y de Lévy (K_p ≥ 0):* es
  exactamente la certificación local de `G2_B8_R5.md` Def. 1 en la forma primitiva y en la variante con
  piezas polares. Teor. D: existe si y sólo si Φ_T ≥ 0; Teor. L″ (CITED; verificado a máquina, sin
  aritmética de intervalos): Φ_{0.5925} < 0, luego **no existe para T ≥ 0.5925**. La clase muere ya en
  c = 1.
- *Reparto arquimediano invariante por traslación pero con símbolos m_p arbitrarios (no de Lévy),
  Σ m_p = m.* No cubierto por G2_B8 (Def. 1 exige 0 ≤ K_p). OPEN; pero el factor p deja de ser un factor
  de Euler: es una pieza p_p cuya hessiana logarítmica es la del factor de Euler más un multiplicador
  elegido, y la hiperbolicidad de p_p es el signo de la forma local, cuadrática, de grado dos: vuelve a
  R160 §6.2 factor por factor. No escribí ningún reparto así.

**Pista (i), triple correlación (ARGUED/OPEN).** C(F) := Σ_{m,n}Λ(m)Λ(n)(mn)^{−1/2}⟨F, τ_{log m}F ⋆
τ_{log n}F⟩ es un candidato natural para D³p(e)[F³]. Por el Lema 3 caso (ii) con d = 3, la
hiperbolicidad exigiría a_T(F)³ ≥ (const)·C(F)² sobre P_T: un reforzamiento del objetivo, no un
mecanismo. Bajo cΛ, C escala como c² mientras a_T es afín en c. No verifiqué si esa desigualdad es
siquiera cierta en c = 1. Exigiría |C(F)| ≲ λ_A^{3/2} en los casi-minimizantes, y no veo razón para ello
(ARGUED). La relación Λ·log + Λ∗Λ = μ∗log² no entra en ninguna de las clases C1–C4. En C4 sólo entra
Λ ≥ 0 por factor.

## 4. Controles

Como no hay objeto con mecanismo, los controles se hacen sobre las clases de §3.

| Control | C1, C2, C3 (= (G) con ρ = 0) | C4 (producto) |
|---|---|---|
| c = 2 | La línea que se rompe es la construcción de V_T, que no está escrita: **no puedo señalarla**. | Factor (1−p^{−s})^{−2} = cuadrado de un factor hiperbólico, que sigue siendo hiperbólico; S_p se duplica en su parte de peine, la parte arquimediana queda fija: la descomposición (3.2) necesita reasignar el presupuesto arquimediano, y se rompe por ahí (lectura de G2_B8 Teor. D). Pero la clase ya falla en c = 1 para T ≥ 0.5925. |
| c no entero | ídem | Las potencias no enteras de factores no son polinomios: la hiperbolicidad polinómica no está definida. Ruptura formal, no de signo. |
| a_P (borrado) | ídem | Borrar factores conserva la hiperbolicidad del producto restante. La ruptura sólo puede venir de que las piezas arquimedianas de los primos borrados (C_p < 0 posible, ΣC_p = C_0 < 0) no son ⪰ 0 solas. ARGUED. Si todos los C_p de los borrados fueran ≥ 0, **el mecanismo sobreviviría a a_P y estaría mal**. |
| sin producto (Davenport–Heilbronn, Epstein) | ídem | No hay factorización: la clase no aplica. Correcto, pero vacío. |

Conclusión de los controles: en C1–C3 el mecanismo es (G) y los controles quedan por hacer sobre un V_T
que nadie escribió. En C4 el único reparto con contenido (Lévy) ya falla en c = 1, y el control a_P no
está garantizado.

## 5. Veredicto propio

**No logré escribir un objeto que cumpla A1–A6.**

Qué se probó (PROVED):
- Lema 1: equivalencia exacta del objetivo en un sector con n₊(H_{e,κ}) ≤ 1, con cualquier e con
  A(e) ≠ 0 como punto base (incluido el vector de Tate), sin suponer a_T(e) < 0.
- Lema 2: todo objeto hiperbólico de grado d con esa hessiana da a_T = p(e)Σλ_i(F)² sobre P_T, una
  suma de cuadrados no lineal y tautológica.
- Lema 3 (NO-GO con clase): en la clase «p homogéneo de grado d ≥ 3, hessiana H_{e,κ} en e, real-raíz a
  lo largo de e + P_T», los coeficientes de grado ≥ 3 o se anulan (y el objeto es ℓ^{d−2}·cuadrática, la
  clase de R160 Prop. 6.2) o fuerzan el objetivo con margen a_T ≥ c|D^kp(e)F^k|^{2/k}. Para d = 3 la
  hiperbolicidad es exactamente a_T³ ≥ 54p². El grado ≥ 3 no es fuente independiente de signo.
- C1–C3 reducen a (G) con ρ = 0 y V lineal. La diagonal −∞ excluye las bases localizadas en la
  versión con coeficientes ≥ 0.
- C4: un factor de Euler genuino nunca tiene log-hessiana ⪰ 0 en P_T (bultos a distancia log p). Con
  reparto de Lévy es G2_B8, muerto para T ≥ 0.5925 (CITED, sin intervalos).

Qué falló y por qué: el «coeficiente no negativo independiente» que pide R160 §6.3(2) no existe en estas
clases, porque en el punto base todo certificado de hiperbolicidad se lee como una suma de cuadrados
por factor (Lema 2, (3.2)). Los términos de grado ≥ 3 sólo restan holgura (Lema 3).

No excluido (sin objeto): certificados de real-raíz de s ↦ p(e+sF) no listados en C1–C4 (operadores de
Pólya–Schur o preservadores de Borcea–Brändén aplicados a una familia en F, límites de familias
real-raíz no factorizadas); repartos arquimedianos no de Lévy en C4; un punto base que dependa de F (el
Lema 3 es en un punto fijo).

Siguiente paso concreto: si se reabre, el único hueco con forma es C4 con símbolos m_p no de Lévy. Hay
que escribir los m_p y comprobar n₊ ≤ 1 por factor, sabiendo que eso es otra vez de grado dos factor a
factor. No lo recomiendo sin un mecanismo por factor que no sea el propio signo.
