# Ronda 5, semilla G3 — una medida construida desde la forma cuyo cierre dé el signo

Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`: a_T(F) = Arch_T(F) − Π_T(F), con
Arch_T(F) = (1/2π)∫ m|F̂|² y Π_T(F) = Σ_{log n<2T} v_n Re c_F(log n), v_n = 2Λ(n)/√n; P_T = {A = B = 0}.
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

Veredicto por adelantado: **no logré escribir un objeto que cumpla A1–A6.** Cada pieza de la semilla tiene
antecedente leído en primaria (§1). Los tres lemas de §3 responden a las preguntas (i)–(iv) y al control
c = 2 y delimitan la clase. Ninguno lleva signo.

## 1. Cotejo (antes de construir)

Antecedentes leídos en primaria, uno por cada componente de la semilla:

| Componente de G3 | Antecedente | Qué hay allí |
|---|---|---|
| Ley de valuaciones independientes y geométricas, E_s X_d = d^{−s}; positividad por construcción aritmética a s = 2α ∈ (0,1) | `phase-209-nonlocal-kernel/CONSTRUCTOR_005.md` §§2–5, §10 | P_s sobre finitas valuaciones (es probabilidad para todo s > 0). Completación exacta −R_α = (−Z_α)E_s\|A − μ_1A\|² + ∫y^{α−1}τ\|E_yA − μ_1A\|². La fuente de signo es un único número real, −2π^{−α}Γ(α)ζ(2α) > 0. §10: la positividad **sobrevive al borrado de cualquier conjunto finito de primos**. No hay mapa a la forma (GOAL_D_STATUS: OPEN; LINK_009–016 lo intentan y fallan) |
| Signo menos entre primos dentro de una covarianza | `phase-209-nonlocal-kernel/ANTICORRELATION_003.md` §§2–4; `POSITIVE_ASSOCIATION_002.md` §§3, 5 | Bajo la gaussiana discreta sobre ℤ∖{0} (theta: Poisson y la red ℤ), Cov(X_d, X_e) < 0 para d, e coprimos, y Var log\|N\| < Σ_p (log p)² Var Y_p. Es exactamente «log n = Σ v_p log p con cruces negativos». Con el origen incluido el signo es el contrario; quitar sólo el origen ya lo invierte. Sin enlace con la forma |
| El peine como producto de medias y el resto como covarianza | `phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`, «Covarianza divisorial agrupada» y «El resto divisorial es indefinido incluso sobre tests pares primitivos» | Levantamiento A_F = Σ μ(d)F(t − log d)X_d, B_F = Σ log m F(t + log m)X_m bajo E_{1/2}. Las medias dan U_μF y U_logF, y su apareamiento es el peine (μ∗log = Λ). La covarianza da R(F) = Σ n^{−1/2}C_{1/2}(n)Re c_F(log n). **PROVED: R es indefinido sobre P_T** (tests F_± explícitos con R(F_+) = (7/4)κ‖g‖², R(F_−) = −(1/4)κ‖g‖²) |
| Ley de varianza total con selector de divisores P(N = n \| b) = Λ(n)/log b (Λ como «esperanza del factor primo») | `phase-106-global-modular-star-audit/106_114_THETA_MARTINGALE_TOTAL_VARIANCE_GATE.md` §§2–6; R161_030 (vía `R161_099_SYNTHESIS.md` y `ANNEX_161_FILES_2.md`; RULES_AVOID K2) | 106_114 escribe la ley theta polar, la varianza total (8) y los martingalas de divisores (12)–(14). Teorema 2, NO-GO PROVED: ninguna torre martingala positiva completa, con todos los canales Gamma, centrales y de divisores, es exacta sobre los radicales; se contradice por la capacidad de las líneas de potencias de primos. R161_030 da la identidad de varianza orientada, genérica en los pesos |
| Ley zeta con marcas (Palm): log n = Σ_{d\|n}Λ(d) como suma de marcas | `phase-104-unconditional-a1-closure/104_50_SECOND_ORDER_UNIT_PALM_COVARIANCE_GATE.md` §1 | E_s[Z_fZ_g] = Cov_s(D_f, D_g) + M_s(f)M_s(g), es decir, varianza más producto de medias. Al centrar, las torres de primos distintos se cancelan por independencia |
| Lévy–Khintchine de la serie con la parte Γ_ℝ; simetría s ↦ 1 − s de la ley | `phase-194-invention/INV_A_001_ARITHMETIC_LEVY_STRUCTURE.md` §§0–5; `INV_F_001` F2 (vía `ANNEX_COTEJO_LORENTZ_2.md` §4) | Ley ID con medida de Lévy e^{−σu}u^{−1}[ΣΛ(n)δ_{log n} + du/(1 − e^{−2u})] para σ > 1. La reflexión la transporta a σ < 0 (Prop. 4.1); la banda queda sin positividad. Θ⁺ es FALSO. El muro ∂log alcanza toda premisa cónica |
| Promedio con probabilidad sobre la familia de pesos | `phase-159-row-d-two-front-construction/G2_B8_R1.md` §2, Teoremas B y S | Jensen para la función cóncava V_T: los promedios dan sólo cotas superiores, y la media de Haar del toro de Satake es < 0 para T ≥ 0.60 |
| Clase lorentziana, objeto de grado ≥ 3 | `phase-160-row-d-infinite-T/R160_C7_R1.md` §§5–6 | §6.3(2) OPEN. La fuente de esa sección usa una equivalencia externa del objetivo; no se desarrolla aquí |

No abiertos en primaria: 104_49, 106_65, 106_104, R161_030–031 (los leí a través de la síntesis y del anexo),
209 CONSTRUCTOR_002/004 y sus AUDIT, G2_B8_R2–R5, `phase-193/CA_J_002`, Paper 48 y los catálogos 01–06 del
índice (los leí a través de los anexos de esta carpeta).

**Conclusión del cotejo.** La semilla, tal como está formulada, es repetición. Tiene tres partes y cada una
está en el corpus con su obstáculo:
(a) el peine como «media al cuadrado» y el resto como covarianza: 211 GLOBAL, con el resto indefinido sobre P_T;
(b) la varianza total con el selector Λ(n)/log b: 106_114, con un NO-GO para toda torre martingala positiva;
(c) la ley aritmética a σ = ½ positiva por construcción: 209 CONSTRUCTOR_005, que sobrevive al borrado de primos.
El acoplamiento con la ley Gamma, con la ecuación funcional como simetría de la ley conjunta, está en INV_A_001.
Allí la simetría transporta positividad de σ > 1 a σ < 0 y no a la recta.
Lo que el cotejo no encontró, sin que eso pruebe novedad: un enunciado de que el peine no puede ser una
«varianza explicada» sobre P_T (Lema 2), y el control c = 2 hecho dentro de la clase de leyes (Lema 3).

## 2. Objeto (no escrito: qué se intentó y por qué no es un objeto)

Se intentó la forma pedida: (Ω, ℙ_T) aritmética y F ↦ X_F lineal con a_T(F) = Var(X_F) + ρ(F) sobre P_T.
Las tres realizaciones naturales son las del cotejo:

- Traslaciones aleatorias. Si X_F = U_Y F con Y ⊥ F, entonces Var(U_YF) = ‖F‖² − ‖μ∗F‖² = (1/2π)∫(1 − |μ̂|²)|F̂|².
  Esto es un multiplicador de Fourier y cae en R3-a. Cuando μ es la ley de log N bajo ζ^c, es ciego a c (Lema 3).
- El levantamiento por valuaciones de 211: el resto R es indefinido (PROVED en la fuente).
- La varianza total con selector de divisores de 106_114: NO-GO por su Teorema 2.

No tengo una cuarta realización con fórmula propia. El Lema 1 muestra que el formato de varianza por sí
mismo no aporta nada: sin una (Ω, ℙ, X) escrita no hay objeto.

## 3. Identidad, mecanismo y respuestas a (i)–(iv)

**Lema 1 (el formato de varianza es (G); PROVED).** Sea ℓ una forma lineal sobre L²(I_T) que se anula en
P_T. Las siguientes afirmaciones son equivalentes:
(a) existen (Ω, ℙ) y una aplicación lineal X con E X_F = ℓ(F) y a_T(F) = Var X_F + ρ(F) sobre P_T, ρ ≥ 0;
(b) existen ℋ y V con a_T = ‖VF‖² + ρ sobre P_T, es decir (G).
Además, si la identidad vale en todo L²(I_T), entonces E|X_F|² − |ℓ(F)|² = a_T^{ext}(F) + ρ(F) define una
extensión con n₋ ≤ 1. Ésa es la contabilidad polar de P47 thm:parityschur, que el conteo de inercia R4-f no
separa de c = 1.
*Prueba.* (a)⇒(b): sobre P_T se tiene ℓ = 0, luego Var X_F = E|X_F|² = ‖X_F‖²_{L²(ℙ)}. (b)⇒(a): se toma el
proceso gaussiano centrado de covarianza ⟨VF, VG⟩ y se le suma ℓ(F) como constante. Lo de n₋ ≤ 1:
E|X|² ≥ 0, y restar |ℓ|² resta a lo sumo una dirección. ∎
Lectura: «media nula exactamente en P_T» no añade mecanismo. La varianza restringida a P_T es una norma
cuadrada, y la novedad tendría que estar íntegra en (Ω, ℙ, X).

**Lema 2 (el peine no es una varianza explicada ni su opuesto sobre P_T; PROVED).** Si 2T > log 2, la
forma Π_T restringida a P_T tiene subespacios de dimensión arbitraria donde es definida negativa, y otros
donde es definida positiva.
*Prueba.* Se toma g ∈ C_c^∞(I_T) real, g ≥ 0, con soporte de longitud mayor que log 2; entonces c_g(log 2) > 0.
Sea F_ω(t) = g(t)cos(ωt). Por Riemann–Lebesgue, uniformemente en u:
c_{F_ω}(u) = ½c_g(u)cos(ωu) + o(1), ‖F_ω‖² → ½‖g‖², A(F_ω), B(F_ω) → 0, y
⟨F_ω, F_ω′⟩ → 0, Π_T(F_ω, F_ω′) → 0 cuando |ω − ω′| → ∞.
Se corrige F_ω hacia P_T restando una combinación de dos funciones fijas duales de A y B; la corrección es
O(|A| + |B|) → 0. Por tanto Π_T(F̃_ω) = P(ω) + o(1), con P(ω) = ½Σ_{log n<2T} v_n c_g(log n)cos(ω log n).
P es un polinomio trigonométrico de frecuencias distintas y no nulas. No es idénticamente cero porque el
coeficiente de log 2 es positivo, y su media de Bohr es 0. Por tanto P < −δ en un conjunto relativamente
denso, y P > δ en otro. Se eligen ω_1, …, ω_k en el conjunto negativo y suficientemente separados. La matriz de
Π_T sobre {F̃_{ω_j}} es diagonal negativa más o(1), y lo mismo con el conjunto positivo. ∎
*Consecuencia (respuesta a (iii)).* En a_T = E Var(X|𝒢) = Var X − Var E(X|𝒢), el término que se resta es
semidefinido positivo. Por el Lema 2 no puede ser Π_T. La covarianza condicional y la «varianza explicada»
**no producen el menos del peine**. Toda escritura Π_T = V⁺ − V⁻ con V^± varianzas deja
a_T = (Arch_T + V⁻) − V⁺: el mismo problema con otro nombre (A4).
En las realizaciones de independencia, cada primo contribuye con signo más (G2_B8). El único menos
aritmético que está escrito es la anticovarianza entre primos coprimos de ANTICORRELATION_003. Ese menos
vive entre pares de primos (p, q), con coeficientes (log p)(log q). El peine es diagonal en n = p^k, con
coeficiente c_F(log n). La anticovarianza tiene el formato del canal de dos bases −2 log p log q (K5,
R170_850 §5), que ya se sabe lineal en el peso.

**Lema 3 (control c = 2 y c no entero dentro de la clase de leyes; PROVED).**
(a) Para σ > 1 y todo c > 0, P(N_c = n) = d_c(n)n^{−σ}/ζ(σ)^c es una probabilidad, con
d_c(n) = Π_p binom(v_p + c − 1, v_p) ≥ 0. Las valuaciones son independientes, binomiales negativas
NB(c, p^{−σ}), y E N_c^{−iτ} = (ζ(σ + iτ)/ζ(σ))^c. La ley Gamma(σ/2), cuya transformada de Mellin da Γ_ℝ, no
depende de c.
(b) P(p | N_c) = 1 − (1 − p^{−σ})^c, y esto es igual a p^{−σ} si y sólo si c = 1. La función
x ↦ 1 − (1 − x)^c coincide con x en un punto de (0,1) sólo si c = 1, por estricta concavidad (c > 1) o
convexidad (c < 1).
*Prueba.* (a) Es el producto de Euler de ζ^c, con coeficientes binomiales no negativos. (b) Es cálculo directo. ∎
*Respuesta al control.* Para c = 2 **ninguna identidad deja de ser una varianza**. La ley conjunta (N_2, G)
es una probabilidad producto, y toda forma Var(·) o E|·|² en ella sigue siendo ≥ 0. Lo que cambia es la
identificación lineal de las medias: E X_d = d^{−σ} vale sólo en c = 1 (Lema 3(b)). Por eso, en el
levantamiento de 211, ⟨EA_F, EB_F⟩ deja de ser el peine 2Λ y pasa a ser otro funcional lineal. El signo del
resto no queda gobernado por nada. La ruptura está en una identificación lineal (D14, INV_I_001: identifica,
no firma), no en el factor arquimediano fijo. Por A5 el mecanismo no se rompe donde debe. Para c no entero
vale lo mismo, porque las leyes ζ^c existen para todo c > 0 (divisibilidad infinita).

**Respuestas puntuales.**
(i) X_F: las elecciones escritas son U_YF (traslación aleatoria), Σ_d μ(d)F(· − log d)X_d con
Σ_m log m F(· + log m)X_m (levantamiento de 211), y F evaluada en log de un factor primo elegido con
probabilidad Λ(n)/log b (106_114). F(log N) centrada bajo la ley zeta es la variante de traslación: su
varianza es un multiplicador (Lema 2 y R3-a).
(ii) La ventana: en todas, el soporte de F en I_T entra sólo porque c_F(log n) = 0 para log n ≥ 2T. La ley no
la ve: las valuaciones de un primo p < e^{2T} incluyen todas las potencias p^k, también las de fuera de la
ventana. No encontré un mecanismo que haga depender ℙ_T de T de forma no trivial. Lo único que acerca la
dependencia en T a la medida es la Mellin de 209, y allí no hay τ.
(iii) El signo menos: Lema 2.
(iv) σ = ½. No existe una probabilidad sobre ℕ con P(n) ∝ n^{−1/2}, porque Σ n^{−1/2} = ∞ (PROVED). Las leyes con
función característica Λ(σ + iτ)/Λ(σ) existen para σ > 1 y, por reflexión, para σ < 0 (INV_A_001 Prop. 4.1,
PROVED allí). A σ = ½ sólo quedan dos vías:
- finitos primos (209 §2);
- la Mellin de una theta con funcional firmado ν_y (209 CONSTRUCTOR_005 (2)).
En la segunda, el signo sale de un solo número real y sobrevive al borrado de primos. Seguir la pregunta
«¿es positiva la ley en el punto fijo de la reflexión?» exige una equivalencia externa del objetivo. No se
desarrolla.

## 4. Controles (de la clase, no de un objeto)

| Falsificador | Qué hipótesis falla | ¿Deja de ser ≥ 0? |
|---|---|---|
| c = 2 | E X_d = d^{−σ} (Lema 3(b)) | No: las varianzas siguen siendo varianzas; Gamma no cambia. **La clase no se rompe donde debe** |
| c no entero | Ídem; la ley ζ^c existe (Lema 3(a)) | No |
| a_P (borrado de primos) | Ninguna: la ley geométrica sobre los primos restantes es una probabilidad (209 §10) | No: la positividad se hereda |
| Davenport–Heilbronn | Coeficientes con signo: no hay ley | Sí, pero por Λ ≥ 0, cono que cΛ conserva: se usa un solo canal (G1) |
| Epstein x² + 5y² | Las valuaciones no son independientes (sin producto de Euler); las leyes r_Q(n)n^{−σ} existen para σ > 1 | Las varianzas siguen ≥ 0; sólo falla la identificación de medias |

Según A5, una clase que no se rompe en c = 2, c no entero ni a_P está mal como fuente de signo.

## 5. Veredicto propio

**No logré escribir un objeto que cumpla A1–A6.** La semilla es repetición de 211 GLOBAL (levantamiento por
valuaciones), 106_114 (varianza total, NO-GO), 209 CONSTRUCTOR_005 (ley a s ∈ (0,1), heredada por borrado) e
INV_A_001 (Lévy con Gamma y reflexión). No es una prueba de imposibilidad de toda medida construida desde la
forma.

## Resultado

Sin mecanismo nuevo. Piezas PROVED sin signo: Lemas 1, 2 y 3.

## Qué se probó

- Lema 1: el formato «varianza con media nula exactamente en P_T» equivale a (G); fuera de P_T es la
  contabilidad polar con n₋ ≤ 1.
- Lema 2: Π_T tiene subespacios de dimensión arbitraria definidos negativos y definidos positivos en P_T
  (2T > log 2). Por tanto no es una varianza explicada, y la ley de varianza total no produce el menos del peine.
- Lema 3: las leyes ζ^c son probabilidades para todo c > 0, con valuaciones binomiales negativas y Gamma fija.
  Toda identidad de varianza en la clase persiste para c ≠ 1, y la única línea que separa c = 1,
  P(d | N) = d^{−σ}, es una identificación lineal.

## Qué falló y por qué

El signo de la clase probabilística siempre es «varianza ≥ 0». Eso es cerrado bajo cΛ, bajo c no entero y bajo
borrado, porque la medida es positiva por los coeficientes ≥ 0, y éstos se conservan. El menos del peine es
indefinido sobre P_T (Lema 2), luego no puede ser una varianza restada. Y el único menos aritmético escrito,
la anticovarianza entre primos de 209, está en pares de primos y no en el canal diagonal de n.

## Siguiente paso concreto

Una reapertura tendría que dar una ley ℙ_T cuya positividad dependa de c = 1 por algo distinto de los
coeficientes ≥ 0. El candidato visible es una ley sobre ℤ (theta) en la que el borrado de un primo cambia el
signo de una covarianza: POSITIVE_ASSOCIATION_002 §3 lo prueba para y grande, pero §5 muestra que quitar el
origen ya lo hace. Haría falta además una X_F con fórmula que lleve esa covarianza al canal diagonal de n.
Sin esa X_F escrita, la reapertura no pasa la puerta.
