# Ronda 5, memo G5: invención libre desde A1–A6 (deducción hacia atrás de los tipos de objeto)

Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`. Arch(F) = C_0‖F‖² + ∫_0^∞ (c_F(0) − Re c_F(u))K(u)du;
Π_p(F) = Σ_{k: k log p < 2T} v_{p^k} Re c_F(k log p); a_T = Arch − Σ_p Π_p. Para el peso cΛ, a_T^{(c)} = Arch − cΣ_pΠ_p.
Sector de paridad: P_T^± = P_T ∩ {F par / impar}; en cada sector hay un solo vector de Tate, τ_+ = cosh(t/2) (par)
y τ_− = sinh(t/2) (impar), y P_T^± = τ_±^⊥ dentro del sector.

## Cotejo (va primero, por regla)

1. **Antecedentes más cercanos, leídos en primaria.**
   - `phase-160-row-d-infinite-T/R160_C7_R1.md` §§5–6, en especial §6.3(2) y §7 ítem 2 (P160.C7.1): pide un
     polinomio de grado k ≥ 3 cuya hessiana sea −a_T, con una fuente independiente de coeficientes no negativos;
     descarta los candidatos Str(Γ_F^k). Leído entero en §§5–7.
   - `phase-159-row-d-two-front-construction/G2_B8_R1.md` §§1–2 (Teorema S y Corolario S′: vacío del toro de
     Satake) y `G2_B8_R5.md` §§1–2 (Teorema D: certificación local con reparto Lévy–Khintchine del factor
     arquimediano; umbral T_loc ≤ 0.5925). Leídos en esas secciones.
   - `phase-200-sign-object/SPEC_SIGN_OBJECT_010.md`, variante 20.3 (a_T como log θ; «su signo es el de la
     hessiana de log θ, un segundo cumulante indefinido»). Leído el pasaje.
   - `phase-193-creation-campaign/CA_G_000_SEEDS.md` G6 y `CA_F_000_SEEDS.md` F5; `phase-201-untried-families/FAMILIES_A_001.md`
     A1: polinomios lorentzianos registrados como «retry, no sign» / NON-VIRGIN. Leídas las líneas pertinentes.
   - `ANNEX_COTEJO_LORENTZ_1.md` §§3–5 y `ANNEX_COTEJO_LORENTZ_2.md` §§3–5 de esta carpeta: M5 «cierre bajo
     producto de factores de Euler aplicado a la signatura con el factor arquimediano fijo, y su comprobación en
     c = 2» figura como no encontrado.
2. **Qué es nuevo aquí.** No un objeto: tres lemas de clase (PROVED, elementales) que cierran, en clases
   declaradas, los tipos de objeto que la deducción hacia atrás señala como «nativos» para A1–A6:
   (L1) todo objeto cuyo signo salga de la log-concavidad (o log-convexidad) en un punto interior —
   determinantes, funciones de partición, polinomios lorentzianos homogéneos en un punto del cono— da a_T como
   una forma de Gram cuyo vector es exactamente el V_T de (G), sin aporte de signo propio; (L2) el cierre bajo
   producto de factores de Euler de esa log-concavidad equivale a un reparto local a_T = Σ_v q_v, q_v ⪰ 0, que
   con repartos sin restricción es el enunciado (Farkas trivial) y con repartos covariantes por rotación local
   cae en el Teorema S de G2_B8_R1; (L3) en el formato lorentziano homogéneo la dirección del gradiente queda
   forzada a ser el vector de Tate del sector. L2 responde al punto M5 del anexo (cierre por producto con el
   factor arquimediano fijo, con su comprobación en c = 2): la ruptura en c = 2 está exactamente en el
   presupuesto arquimediano, pero el mecanismo no tiene contenido de signo.
3. **Por qué no repite.** R160_C7_R1 §6.3(2) examina sólo Str(Γ_F^k) y deja abierta la clase; G2_B8 trata
   repartos de Lévy–Khintchine (invariantes por traslación) y rotaciones de Satake, no la clausura por producto
   de log-concavidad de factores arbitrarios. L1–L3 cubren la clase «signo por log-concavidad en punto
   interior, cerrada por productos», que incluye el ítem P160.C7.1 en cuanto se quiera probar con las reglas de
   cierre de producto.
4. **Conexión con la positividad global.** Ninguna: los tres lemas muestran que en esas clases la
   positividad global equivale a la existencia de V_T (L1) o a la del reparto (L2), es decir al objetivo. No se
   afirma signo alguno.

Resultado anticipado: **no logré escribir un objeto que cumpla A1–A6.** Lo que sigue es la deducción y los
lemas de clase.

## 1. Deducción hacia atrás (pasos (1)–(3) de la semilla)

| Propiedad forzada por A1–A6 y los hechos | Tipos que la tienen de forma nativa | Qué queda tras L1–L3 o tras lo PROVED en el corpus |
|---|---|---|
| (P1) Dependencia no afín del peso que en c = 1 degenera (A1) | determinante, función de partición, índice, dimensión, cohomología que salta | Índices y dimensiones: constantes cerca de c = 1 en ventana fija (R4-f). Determinante / partición: L1 |
| (P2) Positividad sin margen (λ_A ≤ 4·10⁹Te^{−15.449T}) | identidad «= Σ cuadrados»; desigualdad con caso de igualdad; cantidad entera | Cantidad entera: R4-f. Identidad: es (G) misma |
| (P3) Usa las dos condiciones de momento de forma esencial (A3) | objeto cuyo gradiente en el punto base es el vector de Tate | L3: en el formato lorentziano esto es forzado, no una elección |
| (P4) Ventana en c que se cierra sobre 1 por ambos lados | función cóncava de c con máximo en c = 1 (λ_A(T;c) es ínfimo de afines) | Cualquier mecanismo cuya hipótesis valga en un conjunto de c independiente de T falla (P47 thm:shape, cor:void) |
| (P5) Producto de Euler y factor arquimediano fijo; c = 2 debe romper por el factor arquimediano (A5) | cierre bajo producto (log-concavidad, lorentzianidad, estabilidad) | L2: el cierre por producto es un reparto local; con reparto libre es el objetivo, con reparto covariante cae en el Teorema S |
| (P6) c = 1 único: red ℤ autodual por Poisson | identidad de Poisson / theta | D6, D14, D15 de `RULES_AVOID.md` (theta, completitud de cuadrados, métricas locales) |

Intersección de (P1)–(P5) en tipos de objeto: «función positiva p cerca de un punto base x_0, con log p
cóncava, producto de un factor arquimediano y factores por primo, gradiente en el vector de Tate, y hessiana de
log p igual a −a_T». Los lemas siguientes muestran que esa intersección no aporta signo propio.

## 2. Lemas de clase

**Lema L1 (log-concavidad en punto interior = Gram de (G); PROVED).** Sea E ⊂ P_T un subespacio de dimensión
finita (o P_T ∩ 𝒟_T con la topología de la norma del grafo), U ⊂ ℝ^d abierto, x_0 ∈ U, ℓ : E → ℝ^d lineal y
p : U → (0, ∞) de clase C² con

  ∇² log p(x_0)[ℓF, ℓF] = −a_T(F)  para todo F ∈ E.  (2.1)

(a) Si log p es cóncava cerca de x_0, entonces a_T ⪰ 0 en E y existe un espacio de Hilbert ℋ y V : E → ℋ lineal
con a_T(F) = ‖VF‖² (es decir, (G) con ρ = 0).
(b) Caso determinante: p(x) = det(X_0 + Σ_i x_i A_i) con X_0 ≻ 0 y A_i simétricas cualesquiera. Entonces
−∇² log p(0)[y, y] = tr((X_0^{−1}A(y))²) = ‖X_0^{−1/2}A(y)X_0^{−1/2}‖²_HS, A(y) = Σ y_iA_i; el signo no usa
ninguna positividad de los A_i.
(c) Caso partición: p(x) = ∫ e^{⟨x, X⟩} dμ con μ medida de probabilidad y momentos exponenciales. Entonces
∇² log p(0)[y, y] = Var_μ⟨y, X⟩ ≥ 0; (2.1) con signo cambiado (log-convexidad) da a_T(F) = Var_μ⟨ℓF, X⟩, y un tal μ
existe para algún ℓ si y sólo si a_T ⪰ 0 en E.
(d) Recíprocamente, si a_T ⪰ 0 en E, existen p log-cóncava y ℓ con (2.1): p = exp(−½a_T∘ℓ^{−1}) en la imagen.

*Prueba.* (a) Concavidad de log p ⇒ ∇²log p(x_0) ⪯ 0 ⇒ por (2.1) a_T ⪰ 0; la raíz cuadrada de la forma
(teorema espectral en dimensión finita, o completación de E por a_T en general) da V. (b) ∂_y log det(X) =
tr(X^{−1}A(y)), ∂_y² = −tr(X^{−1}A(y)X^{−1}A(y)); con X_0 ≻ 0, tr((X_0^{−1}A)²) = tr((X_0^{−1/2}AX_0^{−1/2})²) =
‖X_0^{−1/2}AX_0^{−1/2}‖²_HS ≥ 0 porque X_0^{−1/2}AX_0^{−1/2} es simétrica. (c) Fórmula estándar de cumulantes:
∂² log ∫e^{⟨x,X⟩}dμ = covarianza bajo la medida inclinada; en x = 0 es Var_μ. Si a_T ⪰ 0 en E, el campo
gaussiano centrado con covarianza a_T existe (Kolmogorov; en dimensión finita, la gaussiana de matriz a_T); si
no, la varianza no puede ser negativa. (d) Directo. ∎

*Lectura.* En la clase «el signo sale de la log-concavidad (o log-convexidad) de una función positiva en un
punto interior», el objeto construido es exactamente un V_T de (G); la log-concavidad no aporta nada que no
sea la existencia de V_T. Esto incluye determinantes y funciones de partición (P1) y responde a la variante 20.3
de `SPEC_SIGN_OBJECT_010.md`: allí el segundo cumulante quedaba indefinido; aquí, cuando está definido, es un
Gram y su existencia es el objetivo.

**Lema L3 (formato lorentziano homogéneo y vector de Tate; PROVED).** Sea p homogéneo de grado k ≥ 2, positivo
en un abierto cónico que contiene x_0, de clase C². Pongamos g = ∇p(x_0) ≠ 0 y H = ∇² log p(x_0). Entonces
∇²p(x_0) = p(x_0)(H + ĝĝᵀ), ĝ = g/p(x_0), y son equivalentes:
 (i) ∇²p(x_0) tiene a lo sumo un autovalor positivo;
 (ii) H ⪯ 0 sobre g^⊥.
Si además (2.1) vale con ℓ un isomorfismo del sector P_T^± ⊕ ℝτ_± sobre ℝ^d tal que ℓ(P_T^±) = g^⊥, entonces (i)
para p equivale a a_T ⪰ 0 en P_T^±, y el hiperplano g^⊥ es la imagen del núcleo del funcional de Tate.

*Prueba.* ∇²p = ∇(p∇log p) = p(∇²log p + ∇log p ∇log pᵀ). Por Euler, ∇²p(x_0)x_0 = (k−1)g y
∇²p(x_0)[x_0,x_0] = k(k−1)p(x_0) > 0. (i)⇒(ii): x_0 es dirección positiva; el complemento ∇²p-ortogonal de x_0 es
{y : ⟨g, y⟩ = 0} = g^⊥; con a lo sumo un autovalor positivo, ∇²p ⪯ 0 en ese complemento, y allí ∇²p = p·H porque
⟨ĝ, y⟩ = 0. (ii)⇒(i): ∇²p ⪯ 0 en el hiperplano g^⊥, luego por min-max a lo sumo un autovalor positivo. La última
frase es (2.1) restringida. ∎

*Lectura.* (P3) no es una elección de diseño: en cualquier objeto lorentziano homogéneo cuya hessiana
reproduzca a_T en un sector, el gradiente en el punto base es el funcional de Tate. El contenido de signo es
H ⪯ 0 en g^⊥, que es (2.1) con a_T ⪰ 0: de nuevo el objetivo, salvo que la lorentzianidad de p se obtenga por
una regla de cierre. La regla de cierre nativa con el producto de Euler es el producto; es el lema siguiente.

**Lema L2 (cierre por producto de factores de Euler = reparto local; PROVED en dimensión finita).** Sea E ⊂ P_T
de dimensión finita y Π_T el conjunto de primos p < e^{2T}. Supongamos p = p_∞ ∏_{p∈Π_T} p_p, cada factor positivo
y C² cerca de x_0, y (2.1). Pongamos q_v(F) := −∇²log p_v(x_0)[ℓF, ℓF].
(a) a_T = q_∞ + Σ_p q_p en E. Si cada factor es log-cóncavo (en particular si cada factor es lorentziano, por la
log-concavidad de los lorentzianos en el ortante abierto, CITED: Brändén–Huh, Ann. Math. 2020, Thm 2.30), cada
q_v ⪰ 0.
(b) (Reparto libre.) Existen formas simétricas r_p en E con r_p − Π_p ⪰ 0 para todo p y Arch − Σ_p r_p ⪰ 0 si y
sólo si a_T ⪰ 0 en E.
(c) (Reparto con dependencia del peso sólo local.) Si la construcción vale para todo peso w en un entorno de Λ,
con p_∞ independiente de w y p_p dependiente sólo de (w_{p^k})_k, entonces q_p^{(w)} = r_p − Π_p^{(w)} con r_p
independiente de w_p, y q_∞ = Arch − Σ_p r_p.
(d) (c = 2 y c no entero.) Bajo (c), para el peso cΛ la misma construcción da a_T^{(c)} = (Arch − cΣ_pr_p) +
Σ_p c(r_p − Π_p). Los términos de primo son c·q_p ⪰ 0 para todo c > 0; la única línea que puede fallar es
q_∞^{(c)} = Arch − cΣ_pr_p ⪰ 0, el presupuesto del factor arquimediano fijo.
(e) (Covariancia por rotación.) Si la log-concavidad de p_p se deduce de una propiedad de los datos locales que
vale para Haar-casi todo α_p = e^{iθ_p} (temperancia, estabilidad local de Lee–Yang, forma de grado uno), la
construcción prueba a_T^{(v(θ))} ⪰ 0 para casi todo θ del toro de Satake, lo que es falso para T ≥ 0.60
(G2_B8_R1 Teorema S(1) y Corolario S′, CITED del corpus, leídos en primaria).

*Prueba.* (a) log p = log p_∞ + Σ log p_p; derivar dos veces. (b) ⇒: sumando, a_T = (Arch − Σr_p) + Σ(r_p − Π_p) ⪰ 0.
⇐: si Π_T = ∅ no hay nada que probar; si no, r_p := Π_p + a_T/|Π_T| da r_p − Π_p = a_T/|Π_T| ⪰ 0 y Arch − Σr_p =
a_T − a_T = 0. (c) Derivando la identidad a_T^{(w)} = q_∞ + Σq_p^{(w)} respecto de w_{p^k}: el lado izquierdo da
−(2/√(p^k))Re c_F(k log p) = −∂_{w_{p^k}}Π_p^{(w)}(F), y sólo q_p^{(w)} depende de w_{p^k}; como a_T^{(w)} es
afín en w, q_p^{(w)} es afín en (w_{p^k})_k con la misma parte lineal que −Π_p^{(w)}; se define r_p := q_p^{(w)} +
Π_p^{(w)}, independiente de w_p y, por la hipótesis de localidad, de los demás pesos; entonces q_∞ = a_T − Σq_p =
Arch − Σr_p. (d) Sustituir w = cΛ en (c). (e) Las hipótesis de (e) se conservan bajo la rotación, luego la
construcción (si existe para Λ por esa vía) existe para v(θ), contradicción con S(1) en un conjunto de θ de
medida positiva. ∎

*Lectura de L2.* La clausura por producto, que es lo único que el producto de Euler aporta a la
log-concavidad, convierte el signo en un reparto del factor arquimediano entre primos. Con repartos sin
restricción el reparto existe exactamente cuando vale el objetivo (b): el mecanismo no tiene contenido. Con
repartos de Lévy–Khintchine es la certificación local de G2_B8_R5, que no existe para T ≥ 0.5925. Con
propiedades locales invariantes por rotación es el vacío de Satake. Lo único no excluido es un r_p que dependa
de la fase exacta α_p = 1 (no de una propiedad casi segura del toro) y que no sea invariante por traslación; no
logré escribir ninguno con fórmula propia.

## 3. Objeto

No escrito. La intersección de §1 se reduce, por L1–L3, a «V_T de (G)» o a «reparto local (r_p) con
Arch − Σr_p ⪰ 0 y r_p ⪰ Π_p», y ninguna de las dos lleva una fuente de signo independiente del enunciado.

## 4. Identidad

L1(a), L1(d) y L2(b) son las identidades exactas entre las clases examinadas y a_T: (2.1) ⟺ (G) con ρ = 0; producto
de factores log-cóncavos ⟺ a_T = q_∞ + Σq_p con q_v ⪰ 0 ⟺ a_T ⪰ 0 en E. Comprobación en el caso más simple: para
T < ½log 2 no hay primos, L2 se reduce a q_∞ = a_T = Arch, y L1 da a_T = ‖VF‖² exactamente cuando Arch ⪰ 0 en P_T,
que es lo certificado en ese rango. No se hizo ningún cómputo: las pruebas son de dos líneas.

## 5. Mecanismo

El candidato natural era: «p lorentziano por producto de factores lorentzianos (Brändén–Huh, cierre por
producto, CITED) ⇒ ∇²p con a lo sumo un autovalor positivo ⇒ (L3) a_T ⪰ 0 en P_T^±». Hipótesis: (H1) cada factor
local es lorentziano; (H2) (2.1) con gradiente en el vector de Tate. (H2) es consistente (L3). (H1) para todos los
factores implica, por L2(a), q_v ⪰ 0 para cada v, y entonces el contenido de (H1) es el reparto de L2(b)–(e).
Hipótesis abierta señalada: existencia de r_p con fórmula propia, dependiente de la fase exacta, no invariante
por traslación, con r_p ⪰ Π_p y Σr_p ⪯ Arch en P_T para todo T. Esto equivale al objetivo (L2(b)), así que no es
una hipótesis más débil: queda registrada sólo como forma del problema, no como avance (B3).

## 6. Controles (sobre el mecanismo de §5, que no prueba nada)

- **c = 2.** Rompe en la línea q_∞^{(2)} = Arch − 2Σr_p ⪰ 0 (L2(d)): los factores de primo duplicados siguen
  siendo log-cóncavos (producto de dos copias), el factor arquimediano fijo no paga el doble presupuesto. Es la
  ruptura que pide A5, pero el mecanismo no tiene contenido para c = 1.
- **c no entero.** No hay factorización en copias; con (c) la construcción se extiende a todo c > 0 por
  escalado de q_p, y la misma línea q_∞^{(c)} es la única que puede fallar. Para c < 1, q_∞^{(c)} =
  q_∞ + (1 − c)Σr_p no es ⪰ 0 a menos que Σr_p ⪰ 0, que no está garantizado: la ruptura a la izquierda de 1
  depende de r_p, no del factor arquimediano. No verificado en ningún ejemplo.
- **a_P (borrado de primos p < P).** Desaparecen los factores p_p, p < P; si el reparto no se recalcula,
  a_T^{(a_P)} = q_∞ + Σ_{p<P}r_p + Σ_{p≥P}q_p, y falla la línea Σ_{p<P} r_p ⪰ 0 (los r_p no tienen signo propio).
- **Sin producto de Euler (Davenport–Heilbronn).** La hipótesis «p = p_∞∏p_p» no se puede escribir: falla la
  primera línea de L2; L1 sigue valiendo (es genérico), lo cual confirma que L1 no aporta signo.
- **Rotación de Satake.** L2(e).

## 7. Veredicto propio

**No logré escribir un objeto que cumpla A1–A6.** Resultados de clase, todos sin signo: L1 (PROVED): signo por
log-concavidad o log-convexidad en punto interior, incluidos determinante y función de partición, es exactamente
un V_T de (G); L3 (PROVED): en el formato lorentziano homogéneo el gradiente es el vector de Tate y la condición
es a_T ⪰ 0 en el sector; L2 (PROVED en dimensión finita, (e) relativo a G2_B8_R1 Teorema S): el cierre por producto
de factores de Euler es un reparto local que con reparto libre equivale al objetivo, con Lévy–Khintchine es la
clase muerta de G2_B8_R5, y con propiedades locales casi seguras en el toro cae en el vacío de Satake; rompe en
c = 2 sólo en el presupuesto arquimediano.

## Resultado

NO-GO con clase (L1–L3), sin mecanismo nuevo. Ninguna afirmación de signo.

## Qué se probó

L1(a)–(d), L3, L2(a)–(d) completos; L2(e) relativo a un teorema del corpus.

## Qué falló y por qué

Todo tipo de objeto «nativo» para (P1)–(P5) que obtenga el signo de una concavidad en un punto interior
traslada el signo a una forma de Gram o a un reparto, y la existencia de cualquiera de los dos es el objetivo.
La única regla de cierre que usa el producto de Euler (producto de factores) es aditiva en la hessiana de log y
reproduce la certificación local.

## Siguiente paso concreto

Si se quiere seguir por esta clase: escribir un r_p con fórmula propia que dependa de α_p = 1 de forma no casi
segura en el toro y no sea invariante por traslación, y verificar r_p ⪰ Π_p para p = 2, 3 en T = 0.5925 sobre el
par de prueba de G2_B8_R5 §4 (donde todo reparto LK falla). Sin esa fórmula, la clase queda cerrada como se dice
arriba. No cotejado en primaria: fases 15, 40–43, 120 (matroide de colisiones, citada por el anexo), 137–142,
Paper 46, y `00-references/`.
