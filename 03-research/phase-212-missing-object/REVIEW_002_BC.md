# REVIEW_002_BC — Revisión hostil de ROUND_002_B y ROUND_002_C

Alcance. Lectura completa de las dos memos y de `BRIEF_CONSTRUCTOR.md`, `README.md`, `OBJECT_SPEC.md`,
`LEDGER.md`, `RULES_AVOID.md`, `../phase-211-sign-sandbox/STATEMENT_001.md`. Primarias abiertas para
esta revisión: 211 `POWER_GLOBAL_ROUTE_REVIEW.md` («Extensión factorial antes de resonancia» y sus
corolarios; «Control de la sustitución ortogonal»), 211 `POWER_GRAM_SLICES_OBSTRUCTION.md` §§16.4,
17.2–17.5, 211 `ROUND_003_B.md`, 211 `ROUND_005_A.md` Prop. 3.3, 211 `LEDGER.md` (C9, C33b, C49);
fase 170: R170_201, R170_301, R170_850, R170_851, R170_854 §§3–6, R170_856 §§0, 3–4, R170_868;
R166_502 §5.2; fase 204 `P1_BBSTAR_001.md` §§2.2, 2.6–2.8, 3–4; `ROUND_001_C.md` (Teorema R, instancias y
§7); y la primaria de la fase 116 que la memo B no leyó
(`phase-116-the-logarithmic-schur-angle-conjecture/working-notes/outputs/row_d_gamma_fourier_tate_v94_audit.tex`,
ecuaciones (79)–(84), (132)–(153), (195)–(201), (223l)). Las derivaciones marcadas PROVED en esta
revisión están escritas completas aquí. Ningún otro archivo fue modificado.
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

Resumen.

| Memo | Veredicto global | Error en el núcleo | Correcciones |
|---|---|---|---|
| ROUND_002_B | ACEPTADO CON CORRECCIONES | ninguno en las identidades; una afirmación de corpus falsa, una aplicación correcta pero sin contenido, un uso de R-cont fuera de alcance | §B.3 |
| ROUND_002_C | ACEPTADO CON CORRECCIONES | ninguno en los dos hechos elementales; una frase falsa sobre la orientación, las tres lecturas no son exhaustivas, el residuo OPEN está mal planteado en su letra | §C.3 |

En ambos casos el veredicto «repetición, sin mecanismo nuevo» se sostiene para la candidata tal como
fue formulada. Ninguno de los dos es una imposibilidad, y ninguna de las dos memos lo redacta como tal
salvo en los puntos que se corrigen abajo.

---

## Parte B — ROUND_002_B

### B.1 Comprobación contra las primarias

1. **GLOBAL, «Extensión factorial antes de resonancia».** El texto primario dice: «sum Lambda P_m*KP_m
   tiene entrada K_lambda,mu log gcd(q_lambda,q_mu)», con q_λ el mayor entero cuyo cuadrado divide a λ,
   P_m la selección de índices divisibles por m², y la identidad exacta
   Q[c] = Σ_{m≥2} Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b). CITED, comprobado. Los restos citados por la
   memo (D con entradas positivas y no semidefinida; E(δ_1) < 0; ningún C finito con E ≥ −C·S_sq; núcleo
   de S_sq = soporte libre de cuadrados; B + M ⪰ 0 falsa en {1,2}) figuran allí como se citan.
   Precisión: la matriz es [log mcd(q_λ,q_μ)] = E′ diag(Λ) E′ᵀ con la incidencia E′_{λ,m} = 1_{m²|λ}
   sobre el índice modal, no [log mcd(i,j)] sobre un índice libre. Es una instancia de (B)
   (ℓ_λ = coordenada modal, índice aritmético q_λ), no el esquema (B) entero.
2. **GRAM §17.2.** (RES-SOS) figura como la cita la memo, con f_q = Σ_{a|q}√a c_a, la sustitución
   Σ_{m|q}Λ(m) = log q y D_q de §17.3; alcance de §17.4 como se cita. CITED, comprobado.
3. **211/ROUND_003_B (C9).** Es la métrica δ = log(mcm/mcd) como multiplicador de Schur sobre 𝔸_M;
   su Prop. 1 es una reformulación y los casos prescritos son NO-GO. No es la candidata (B): allí el
   núcleo multiplica a la matriz objetivo, aquí pesa un Gram en F. La memo lo cita con ese alcance.
4. **R170_868.** El teorema está enunciado para un espacio de llegada Y arbitrario (§0) y en versión
   tensorial sobre el núcleo algebraico (§4). Tomar Y = formas hermíticas no es una extensión: está
   dentro del enunciado. PROVED en la primaria, en dimensión finita en (a, c).
5. **R170_201 y R170_301 (primarias).** 201: cuadrados por canal primo D_p*D_p = C_p I − (V_p + V_p*),
   sin cocientes porque los canales se separan antes de la norma; coste constante óptimo C_P (Teor. 2,
   probado en frecuencia cero, con la salvedad expresa de que no cubre factorizaciones comprimidas a
   una ventana); genérico en los pesos (§6). 301: E_T = Γ_T + 2A_T I − J_T + 2|c⟩⟨c| con
   ⟨E_TF,F⟩ = Γ_T(F) + Σ a_n‖F − S_{log n}F‖² + 2|⟨F,c⟩|², W_T = E_T − C_T, y la equivalencia con una
   contracción (11); falsificador a₂ = 100. Ninguna usa una matriz de incidencia ni [log mcd]. El
   resumen de la memo es correcto para 201; para 301 omite que allí sí hay operadores que ven la
   ventana (J_T comprimido, funcionales ⟨F,c⟩, ⟨F,s⟩), lo que importa para B.2 punto 2.
6. **Fase 116 (primaria no leída por la memo).** El objeto es K(m,n) = mcd(m,n)/√(mn) como Gram de
   estados de dilatación ⟨V_n e_t, V_m e_t⟩ = (mn/g²)^{−t/2} en t ↓ 1 (ecs. (132)–(137)), con
   realización por columnas de incidencia de divisores y blanqueo por Möbius ((195)–(198), (150)–(152)).
   Se acopla a F por los canales J_{a,±}F = (τ_aE_TF ± E_TF)/√2 en L²(ℝ) ((79)–(84)), para los que
   ‖J_{a,∓}F‖² = ‖F‖² ∓ Re c_F(a): F entra sólo por su autocorrelación. Además el Gram de mcd se
   ortonormaliza (η_n = Σ (K_T^{−1/2})_{mn}χ_m, (138)), de modo que no interviene en la forma; la
   contractividad (84c) queda sin probar allí y la inversión canónica no la aporta ((223l)).
   Consecuencia: la fase 116 es un caso de la clase (i) de la memo y **no cambia el veredicto**.
   Relación con (B): derivando (mn/g²)^{−t/2} en t = 0 se obtiene log g − ½ log m − ½ log n, es decir
   [log mcd] menos dos términos de rango bajo; es la métrica δ de C9. PROVED (una línea).

### B.2 Las tres preguntas del encargo

**1. ¿Es literalmente el mismo objeto?** Como esquema, no; como única instancia escrita que ve la
ventana y usa la incidencia, sí. La frase del veredicto «la candidata coincide con RES-SOS y con la
extensión factorial» debe leerse «la única instancia de (B) con [log mcd] escrita en el corpus es la
modal theta». La corrección de registro que propone la memo (RULES_AVOID I1, ledger, índice) es
correcta y ya está incorporada en esos archivos.

**2. ¿La dicotomía de las ℓ_i es exhaustiva?** La partición «conmuta con traslaciones / no conmuta» es
exhaustiva por lógica. Lo que no es exhaustivo es la descripción de la segunda clase. La frase «la
única familia escrita en el corpus es la modal del portador theta» es **falsa como afirmación de
corpus**. Hay al menos tres familias que ven la ventana y no son la modal:

- traslaciones truncadas: B_nF = 1_Iτ_{log n}F − F (fase 204 `P1_BBSTAR_001` §3, clase K3; Prop. 3.1
  cierra sólo el uso término a término; el residuo «K3 no agrupado en base fija» queda allí OPEN como
  clase vacía de candidatas); palabras de traslaciones truncadas QV_aQ (211/ROUND_005_A Lema 3.2,
  Prop. 3.3); J_T comprimido y caminos B_T^{−1/2}J_TB_T^{−1/2} (R170_301 §§2–5);
- funcionales de rango uno: ⟨F,c⟩, ⟨F,s⟩ (R170_301 (3)–(4)), A(F), B(F);
- muestreo: la malla de Nyquist (P47 thm:nyq, listada en `README.md` §3).

Para la primera se puede decir qué da (B). **Lema B-1 (PROVED).** Sea Q = 1_{I_T}, R = 1 − Q,
U_i la traslación por log i y ℓ_i = x_i Q U_i con x_i ∈ ℂ. Entonces
⟨ℓ_iF, ℓ_jF⟩ = x_i x̄_j [c_F(log i − log j) − ⟨RU_iF, RU_jF⟩] (con la convención de c_F de STATEMENT §1,
salvo conjugación), y

    Q_B(F) = (1/2π)∫ σ_B(τ)|F̂(τ)|² dτ − Σ_d Λ(d) ‖R Σ_{d|i} x_i U_i F‖²,
    σ_B(τ) = Σ_d Λ(d) |Σ_{d|i} x_i i^{iτ}|² ≥ 0.

*Demostración.* ‖QG‖² = ‖G‖² − ‖RG‖² con G = Σ_{d|i} x_iU_iF, y Plancherel en el primer término. ∎
Es decir: forma de la clase (i) menos una fuga no negativa. La estructura es la de 211/ROUND_005_A
Prop. 3.3 (cocientes ≥ 0 menos fuga ≤ 0). No hay mecanismo de signo nuevo en esta instancia, pero
tampoco está excluida: el resto ρ_T = a_T − Q_B no fue examinado en ningún archivo.

Para los funcionales escalares (muestreo, borde, rango uno), (B) da Σ_d Λ(d)|Σ_{d|i}ℓ_i(F)|². Ninguna
memo del corpus la escribe. Ver el punto 4 de B.3 sobre el alcance real de R-cont en este caso.

Etiqueta correcta de la dicotomía: clase (i), PROVED; «la clase (ii) se reduce a la modal theta»,
**retirada**; en su lugar: «la única instancia de (ii) con incidencia escrita es la modal; las
traslaciones truncadas dan (i) menos fuga (Lema B-1); funcionales escalares por ventana, sin escribir».

**Lema B-2 (PROVED, refuerza la clase (i)).** Si las ℓ_i conmutan con las traslaciones, toda identidad
(G) con ‖V_TF‖² = Q_B(F) tiene resto ρ_T(F) = (1/2π)∫(s_T − σ_B)|F̂|², con s_T − σ_B ≤ s_T en todo τ.
Luego ρ_T ≤ a_T como formas, y probar ρ_T ≥ 0 sobre P_T es un enunciado del mismo tipo que (★) y más
fuerte. *Demostración.* σ_B ≥ 0. ∎ Esto vale también con valores en un Hilbert auxiliar (por ejemplo
ℋ_mcd ⊗ L²(ℝ) de la fase 116): el símbolo es Σ_{i,j} G_{ij}⟨x_i(τ), x_j(τ)⟩ ≥ 0 para todo Gram G.

**3. ¿La extensión de R170_868 a formas hermíticas está probada?** Sí, y no es una extensión (B.1
punto 4). Pero su contenido aquí es nulo. Escrita entera: con ℓ_i y ρ_T independientes de los pesos y
N′ ≥ todos los índices que intervienen, la fila

    ℓ(a, c) := c·(Arch − ρ_T) − Σ_n a_n κ_n − Σ_d a_d ‖L_d ·‖²,   κ_n := (2/√n) Re c_F(log n),

es lineal y se anula en (Λ, 1) si y sólo si vale (G). Factorizar por 𝒟_{N′} equivale a
κ_d + ‖L_d·‖² = −Σ_{k: d|k} Q_k/√k y Arch − ρ_T = −Σ_k (log k/√k) Q_k, es decir

    ρ_T = Arch + Σ_k (log k/√k) Q_k,   Q_k/√k = −Σ_m μ(m) [κ_{km} + ‖L_{km}·‖²].

Esto es la sustitución Λ = μ∗log en ρ_T = a_T − Σ_dΛ(d)‖L_d·‖², válida para toda expresión lineal en
los valores de Λ. PROVED y **tautológica**: no restringe el signo de ρ_T ni la elección de las ℓ_i.
«Forma sin primos» significa sólo «sin Λ escrita»; contiene μ y los propios cuadrados. La conclusión
de la memo «no sale de 868» sobre-enuncia: la conclusión negativa de 867–868 (toda extensión lineal
positiva es un cambio de métrica) se refiere a extensiones 𝓔_N*𝓔_N sobre el espacio de coeficientes,
no a (G). Además `OBJECT_SPEC.md` O2 pide exactamente esto (forma afín en el peine; la no linealidad
en la acción de V_T sobre F), de modo que ser «uso lineal de Λ∗1 = log» no descalifica por sí solo.
Y la hipótesis «ℓ_i independiente de los pesos» no es forzosa: ℓ_i construidas con Λ exacta quedan
fuera de 868 (condición 2 de su §0).

### B.3 Veredicto por afirmación y correcciones exactas

| # | Afirmación de la memo | Veredicto | Corrección |
|---|---|---|---|
| 1 | Clase (i): Q_B es un multiplicador con símbolo ≥ 0, F entra por c_F (PROVED) | ACEPTADO | añadir Lema B-2 |
| 2 | Σ_mΛ(m)P_m*KP_m = K ∘ [log mcd(q_λ,q_μ)] en GLOBAL (CITED) | ACEPTADO | precisar: incidencia m² \| λ sobre el índice modal |
| 3 | Aplicación de R170_868 con llegada en formas hermíticas (PROVED) | ACEPTADO CON CORRECCIONES | correcta y tautológica (B.2 punto 3); retirar «no sale de 868» y «toda la obligación de signo pasa a una forma sin primos» como obstáculo; añadir que no cubre ℓ_i dependientes de Λ |
| 4 | R-cont excluye L_d = Σ_{d\|i}ℓ_i cuando i indexa nodos o modos | ACEPTADO CON CORRECCIONES | sólo sobre el portador de escalas enteras de A_0: el Teorema R no se transporta a (S) ni a objetos por ventana (`ROUND_001_C.md` §7(ii); `OBJECT_SPEC.md` §3). Para muestreo de Nyquist o funcionales de borde no hay exclusión. Retirar «y por eso el resto E no tiene signo»: la falta de signo de E está probada directamente en GLOBAL |
| 5 | «La única familia escrita en el corpus [que ve la ventana] es la modal» | RECHAZADO | sustituir por la lista de B.2 punto 2 y el Lema B-1 |
| 6 | «La candidata coincide con RES-SOS y con la extensión factorial» | ACEPTADO CON CORRECCIONES | «la única instancia con incidencia escrita es ésa» |
| 7 | Tres orígenes del signo (arquimediano, mcm/mcd, grado dos): ARGUED, no NO-GO | ACEPTADO | la relación con la fase 116 de B.1 punto 6 confirma el segundo |
| 8 | Los pares k, k+1 no comparten ningún L_d, d ≥ 2 | ACEPTADO (PROVED, trivial) | — |
| 9 | Línea de ruptura: ninguna en Q_B; la sustitución Σ_{d\|k}Λ(d) = log k rompe la identidad, no un paso de signo | ACEPTADO | — |
| 10 | Resumen de R170_201/301 | ACEPTADO CON CORRECCIONES | 301 contiene operadores comprimidos a la ventana (B.1 punto 5) |
| 11 | Fase 116 sin comprobar | resuelto aquí | B.1 punto 6: clase (i), Gram ortonormalizado; no cambia nada |
| 12 | Resultado: «sin mecanismo nuevo; no es NO-GO de clase» | ACEPTADO | — |

### B.4 Qué queda no excluido

- ℓ_i que ven la ventana y no son la modal theta: traslaciones truncadas agrupadas por incidencia
  (Lema B-1: su resto ρ_T no fue examinado), funcionales escalares por ventana (muestreo de Nyquist,
  borde), y cualquier familia sobre 𝔸_M.
- ℓ_i que dependan de los valores exactos de Λ (fuera de la hipótesis de linealidad).
- Una compensación conjunta de b*Db + E(b) con los cuadrados factoriales, o de Off con R_res.

Ninguno de estos tiene hoy un objeto escrito ni un mecanismo de signo; se listan como terreno, no
como candidatas.

---

## Parte C — ROUND_002_C

### C.1 Las dos pruebas

**Matriz de coeficientes.** Σ_p y_p² − 2Σ_{p<q}y_py_q = 2Σ_p y_p² − (Σ_p y_p)². La matriz es 2I − J
(J de unos), con autovalores 2 (multiplicidad r − 1) y 2 − r; la congruencia por diag(ℓ_p) conserva la
inercia. Para r = 2 es (y_p − y_q)²; para r ≥ 3 hay una dirección negativa (en y = (1,…,1) vale
r(2 − r)). PROVED, correcto. Alcance, como dice la memo: sólo la matriz que resulta de asignar a cada
primo una diagonal ℓ_p² y a cada par el cruce −2ℓ_pℓ_q; la ley (0.2) reparte esos valores sobre nodos
distintos (p^k y p^aq^b), y esa identificación de nodos es una elección de lectura, no una
consecuencia de la ley.

**Homogeneidad.** La objeción natural es que Λ∗Λ es cuadrático en el peso, de modo que la expresión
a·log − a∗a evaluada en a = cΛ da cΛ·log − c²Λ∗Λ ≠ c·γ_Λ. La primaria resuelve cuál de los dos objetos
es γ: R170_850 (3.1) da B_Λ(s) = −ζ²(1/ζ)″, y para un peso general con serie A(s) el Wronskiano
aritmético es β_a = 1∗(a·log) − a∗log (serie −ζA′ + ζ′A), lineal en a con el peine entero fijo. Entonces
μ∗β_a = a·log − (μ∗a)∗log = a·log − a∗(μ∗log), que es R170_854 (4.7) (comprobado en la primaria: «μ∗β_a =
Da − (μ∗a)∗D1»). Con a = Λ, a∗(μ∗log) = Λ∗Λ. Con a = cΛ, γ_{cΛ} = c(Λ·log − Λ∗Λ) = c·γ_Λ. **PROVED,
correcto**, con esta precisión que la memo debe escribir: uno de los dos factores de «Λ∗Λ» es
μ∗log del peine entero fijo; el objeto cuadrático a·log − a∗a no es el que produce la extracción.
Para a_P: (a_P∗Λ)(p^aq^b) = (1_{p≥P} + 1_{q≥P})ℓ_pℓ_q; los valores de la memo son correctos.

Corrección de la conclusión. «No distingue c = 1» es demasiado. Para cΛ la ley de valores (0.2) queda
multiplicada por c, de modo que la identidad γ_a = −Σ_{d|n}μ(d)log²d es falsa para c ≠ 1: el canal
distingue c = 1 exactamente como lo hace el separador lineal Σ_{d|n}a(d) = log n, y no más. Lo que la
homogeneidad prueba es que el canal **no aporta una ruptura de grado dos**: no es la relación no
homogénea Λ·log + Λ∗Λ = μ∗log² de `OBJECT_SPEC.md` O10 (que sí es falsa para cΛ en un sentido
cuadrático), sino su mitad lineal. «Incumple O4» debe leerse «no añade a O4 nada que el separador
lineal no dé»; «incumple O10», correcto.

### C.2 Antecedentes

Comprobados en las primarias y conformes a la cita: R170_850 §§0, 4, 5 (ley (0.2), forma (4.2), «this
completion is not asserted here»); R170_851 §§0, 2 (γ = Λ·log − Λ∗Λ; con W vuelve a R162_501
Prop. 3.1(a)); R170_854 (3.4) («every exact quadratic representation of the current preserves an
indefinite metric») y §6.3 (cuadrar el sector: cocientes con la métrica positiva, o supertraza
indefinida); R170_856 §4 ((4.3)–(4.5): el W que completa γ se cancela con el −W de la rama de Poisson);
R166_502 §5.2 (V*V frente a V²; la parte no entera de V*V es Σ_{p≠q}V_p*V_q; «cancellation must come
from a signed second sector»); `P1_BBSTAR_001` Teorema P1.A, Lema 2.7, §2.8; 211/ROUND_005_A Prop. 3.3;
R186_005 Lema S0; índice README (filas R11_2_ORIGIN, P1_BBSTAR, P211-5A) y Paper 48 (fila «Selberg
difference channel»). Todo CITED.

Precisión sobre «antecedente literal». R166_502 §5.2 trata V*V con V causal (traslaciones de un solo
sentido). La candidata pide además diagonales «que a_T contiene» y admite traslaciones de ambos
sentidos. Es el antecedente más cercano y cubre la lectura causal; no cubre por sí solo la lectura de
C.3 punto 2.

### C.3 Las tres lecturas, la orientación y el residuo OPEN

**1. Una frase falsa.** En (3): «La orientación correcta del término cruzado se obtiene sólo en el
cuadrado de convolución (lineal en c_F), no en el hermítico». Contraejemplo de una línea: con
D(τ) = Σ_p w_p sin(τℓ_p), |D|² = ½Σ_{p,q}w_pw_q[cos τ(ℓ_p − ℓ_q) − cos τ(ℓ_p + ℓ_q)], un cuadrado hermítico
cuyo cruce en ℓ_p + ℓ_q es −w_pw_q, negativo para todos los pares a la vez. PROVED. Lo cierto es: en un
cuadrado hermítico de valores escalares el cruce negativo en sumas viene acompañado de cocientes con
coeficiente positivo y de masa. La propia lectura hermítica de la memo ya admite el emparejamiento de
un sentido con el contrario; (3) la contradice.

**2. Las tres lecturas no son exhaustivas.** Falta la lectura de **canales separados con valores
vectoriales**, que elimina los cocientes. **Lema C-1 (PROVED).** Sean ℓ_1,…,ℓ_r > 0, w_p > 0, r ≥ 2,
G = I − (2/r)J (simétrica, autovalores 1 y −1). En 𝒦 = ℝ^r ⊕ ℝ^r pónganse e_p = (δ_p, 0),
f_p = (Gδ_p, (I − G²)^{1/2}δ_p); ambas familias son ortonormales y ⟨e_p, f_q⟩ = G_{pq}. Con
a_p = w_p√r/2 y el multiplicador x_p(τ) = a_p(e^{iτℓ_p}e_p + e^{−iτℓ_p}f_p), X_p : L²(ℝ) → L²(ℝ; 𝒦_ℂ),

    ⟨x_p(τ), x_q(τ)⟩ = −w_pw_q cos τ(ℓ_p + ℓ_q)   (p ≠ q),
    ‖x_p(τ)‖² = (r/2) w_p² [1 + (1 − 2/r) cos 2τℓ_p],

y por tanto, para todo F,

    ‖Σ_p X_pF‖² = (r/2)Σ_p w_p² [‖F‖² + (1 − 2/r) Re c_F(2ℓ_p)] − 2Σ_{p<q} w_pw_q Re c_F(ℓ_p + ℓ_q).

*Demostración.* ⟨e_p,e_q⟩ = ⟨f_p,f_q⟩ = δ_{pq} anula los términos en ℓ_p − ℓ_q; los términos en ℓ_p + ℓ_q
dan 2a_pa_qG_{pq} cos τ(ℓ_p + ℓ_q) con G_{pq} = −2/r; la diagonal usa G_{pp} = 1 − 2/r. ∎
Así existe un cuadrado explícito, sin ningún átomo en log(p/q), con el cruce −2w_pw_q de signo fijo en
todos los pares. Su precio es masa (r/2)Σw_p², que crece con el número de primos (compárese con la
dirección 2 − r de la matriz de coeficientes: es el mismo hecho visto desde la diagonal). Vale para
pesos y frecuencias arbitrarios: es genérico, sobrevive a toda la batería de `RULES_AVOID.md` §E, y
por tanto no es un paso de signo. Pertenece a la clase de sumas de cuadrados de polinomios casi
periódicos (R170_201 §3 separa canales del mismo modo; `P1_BBSTAR_001` clase K1), y por el Lema B-2 de
la Parte B su uso en (G) deja un resto con símbolo menor que s_T. La afirmación de la memo «la clase
entera está cerrada para T ≥ ½log3 por P1.A» es exacta sólo cuando la compensación arquimediana es una
constante (enunciado de P1.A); en general lo que hay es el Lema B-2, que no es un NO-GO.

**3. El residuo OPEN está mal planteado en su letra.** La condición (a), «X_q*X_p es, para todos los
pares p ≠ q, el desplazamiento por log p + log q con coeficiente de signo fijo», es contradictoria
como identidad de operadores. **Lema C-2 (PROVED).** Si X_q*X_p = κ S_a y X_p*X_q = κ′ S_a con
a = ℓ_p + ℓ_q ∈ (0, 2T) y S_a la traslación (en L²(ℝ)) o su compresión a L²(I_T), entonces κ = κ′ = 0.
*Demostración.* X_p*X_q = (X_q*X_p)* = κ̄ S_{−a}, luego κ′S_a = κ̄S_{−a}. Para F ≠ 0 soportada en
(T − δ, T) con δ < min(a, 2T − a) se tiene S_{−a}F = 0 y S_aF ≠ 0 en la ventana (en la recta, S_a y
S_{−a} son linealmente independientes); luego κ′ = 0, y por simetría κ = 0. ∎
La condición con sentido es la simetrizada, Re⟨X_qF, X_pF⟩ = κ_{pq} Re c_F(ℓ_p + ℓ_q). Y por el Lema C-1
la simetrizada, junto con (b), **sí tiene solución** en la clase que conmuta con traslaciones. Todo el
peso del residuo está entonces en (c), y en esa clase (c) pide que la forma arquimediana pague sobre
P_T una masa creciente, que es la obstrucción de R170_201 Teor. 2 y de `P1_BBSTAR_001` Prop. 3.1 (CITED;
no probado aquí para toda compensación dependiente de τ).

Residuo correctamente delimitado: operadores X_p **que no conmutan con las traslaciones** (ven la
ventana), con Re⟨X_qF, X_pF⟩ = κ_{pq} Re c_F(ℓ_p + ℓ_q) para todos los pares, sin átomos en cocientes, y
con Σ_p‖X_pF‖² igual a una parte de la forma arquimediana más términos de traslación que a_T contiene,
uniformemente en T; además, por C.1, la no homogeneidad en el peso tiene que entrar por otra vía,
porque γ es lineal. OPEN, sin objeto.

### C.4 Veredicto por afirmación y correcciones exactas

| # | Afirmación de la memo | Veredicto | Corrección |
|---|---|---|---|
| 1 | Matriz 2·diag − rango uno; cuadrado sólo con dos primos; autovalor 2 − r (PROVED) | ACEPTADO | añadir que la lectura identifica nodos p^k y p^aq^b por elección; añadir el Lema C-1 como contraparte (con diagonal r/2 veces mayor sí hay cuadrado) |
| 2 | γ_{cΛ} = c·γ_Λ (PROVED desde R170_854 (4.7)) | ACEPTADO | escribir β_a = 1∗(a·log) − a∗log y que un factor es μ∗log fijo |
| 3 | «No distingue c = 1 (incumple O4 y O10)» | ACEPTADO CON CORRECCIONES | distingue c = 1 sólo linealmente, como el separador; no aporta ruptura de grado dos |
| 4 | Antecedentes (1)a–g | ACEPTADO (CITED, comprobado) | R166_502 §5.2 es el más cercano; «literal» sólo para la lectura causal |
| 5 | Lectura de coeficientes: uso lineal en la autocorrelación | ACEPTADO | — |
| 6 | Lectura hermítica convolutiva: «las traslaciones del mismo sentido producen los cocientes»; clase cerrada por P1.A | ACEPTADO CON CORRECCIONES | cierto con valores escalares; falso con canales separados (Lema C-1); P1.A sólo con compensación constante |
| 7 | Lectura comprimida = ROUND_005_A Prop. 3.3; «no hay cuarta pieza» | ACEPTADO CON CORRECCIONES | cierto para Π² con Π = Qσ_vQ; no es un enunciado sobre toda familia truncada |
| 8 | «Las tres lecturas posibles» | RECHAZADO como exhaustividad | son tres lecturas examinadas; añadir la de canales separados; quedan sin examinar las que ven la ventana |
| 9 | (3): la orientación correcta sólo en el cuadrado de convolución | RECHAZADO | C.3 punto 1 |
| 10 | (3): «NO-GO en esas clases, CITED» para R170_854 (3.4), §6.3 | ACEPTADO | las clases son: representaciones cuadráticas exactas de la corriente graduada; cuadrado del sector con métrica positiva o supertraza |
| 11 | (4): a_T no tiene desplazamientos en log(pq); el μ∗log² del puente se cancela (R170_856 §4) | ACEPTADO | — |
| 12 | Residuo OPEN (a)–(c) | ACEPTADO CON CORRECCIONES | (a) literal es imposible (Lema C-2); simetrizada y con (b) es resoluble (Lema C-1); el residuo real es C.3 punto 3 |
| 13 | «No relanzar … ni otra lectura de Λ·log ± Λ∗Λ» | RECHAZADO en esa amplitud | «no relanzar las lecturas de coeficientes, hermítica escalar, de canales separados y Π² sin los operadores de C.3 punto 3»; una selección rechazada no es una exclusión de clase |
| 14 | Resultado: «sin mecanismo nuevo; no es imposibilidad» | ACEPTADO | — |

### C.5 Qué queda no excluido

- El residuo de C.3 punto 3 (operadores que ven la ventana).
- Un segundo sector con signo que cancele los cocientes antes de tomar la norma (E70_10, R166_502),
  nunca construido.
- Un uso de la relación de grado dos no homogénea Λ·log + Λ∗Λ = μ∗log² que no pase por γ (que es su
  mitad lineal); no hay objeto.

---

## Textos de anotación (sin sobre-enunciar)

**LEDGER.md, dos filas nuevas.**

| K2′ | [log mcd] = E diag(Λ) Eᵀ como Gram sobre F: Q_B = Σ_dΛ(d)‖L_dF‖² | 2 | SIN MECANISMO NUEVO, ACEPTADO CON CORRECCIONES (ROUND_002_B; REVIEW_002_BC). No es imposibilidad. La única instancia con incidencia escrita es la modal theta (211 GLOBAL «Extensión factorial»; GRAM §17.2). PROVED: si las ℓ_i conmutan con traslaciones, el resto tiene símbolo ≤ s_T (incluye la fase 116, mcd/√(mn) con canales ambientes); con traslaciones truncadas, Q_B = forma de esa clase − fuga. Retirado: «la única familia que ve la ventana es la modal»; la aplicación de R170_868 es correcta y tautológica; R-cont sólo aplica sobre el portador de A_0 | no excluidas: ℓ_i por ventana (truncadas agrupadas, muestreo, borde), ℓ_i dependientes de Λ, compensación conjunta de D + E; ninguna con objeto escrito |
| K5 | Canal de dos bases primas −2 log p log q de γ = Λ·log − Λ∗Λ (R170_850 §5) | 2 | SIN MECANISMO NUEVO, ACEPTADO CON CORRECCIONES (ROUND_002_C; REVIEW_002_BC). No es imposibilidad. PROVED: matriz de coeficientes 2I − J, dirección negativa desde tres primos; γ_{cΛ} = cγ_Λ (un factor es μ∗log fijo: el canal es la mitad lineal de la relación de grado dos); existe un cuadrado de canales separados sin cocientes con cruce −2w_pw_q, genérico y con masa (r/2)Σw_p². Retirado: «la orientación sólo sale en el cuadrado de convolución»; «tres lecturas» como lista exhaustiva; la condición X_q*X_p = desplazamiento es contradictoria en su letra | residuo: X_p que ven la ventana con Re⟨X_qF,X_pF⟩ = κ_{pq}Re c_F(log p + log q), sin cocientes y con diagonal pagada por la forma arquimediana; OPEN, sin objeto |

**Índice de rutas (README, entrada de la fase 212).**

- P212-2B. [log mcd] = E diag(Λ) Eᵀ como Gram sobre F: selección rechazada por repetición (211 GLOBAL
  «Extensión factorial antes de resonancia»; GRAM §17.2; fase 116, núcleo mcd/√(mn) con canales que
  conmutan con traslaciones). Sin mecanismo nuevo; no es NO-GO. PROVED (elemental): en la clase que
  conmuta con traslaciones el resto tiene símbolo ≤ s_T; con traslaciones truncadas la forma es esa
  clase menos una fuga ≥ 0. No examinado: ℓ_i por ventana distintas de la modal, ℓ_i dependientes de Λ.
- P212-2C. Canal de dos bases primas de R170_850 §5: selección rechazada por repetición (R166_502 §5.2;
  R170_851, 854, 856; P1_BBSTAR; 211/ROUND_005_A). Sin mecanismo nuevo; no es NO-GO. PROVED
  (elemental): γ es lineal en el peso con el peine fijo; la matriz de coeficientes es 2I − J; un
  cuadrado de canales separados realiza el cruce sin cocientes a costa de masa creciente y es genérico.
  Reapertura: operadores que ven la ventana, con la condición simetrizada de `REVIEW_002_BC.md` C.3.

**Grid (misma sección que la nota de la fase 212).**

Ronda 2 de la fase 212: [log mcd] sobre F (K2′) y canal de dos bases primas (K5), ambos «sin mecanismo
nuevo» por repetición de 211 GLOBAL/GRAM §17.2 y de R166_502 §5.2; ninguno es NO-GO. Piezas PROVED
elementales en `REVIEW_002_BC.md` (Lemas B-1, B-2, C-1, C-2); ninguna es avance de signo. Terreno no
examinado: familias que ven la ventana y no son la modal theta.

**RULES_AVOID.md.** I1, sustituir la última frase por: «Es la selección rechazada "cuadrados
factoriales"; la única instancia con incidencia escrita es la modal theta, y las familias por ventana
distintas de ella no fueron examinadas (`ROUND_002_B.md`, `REVIEW_002_BC.md` Parte B)». I8, sustituir
«el canal de dos bases primas −2 log p log q (850 §5, no construido)» por: «el canal de dos bases
primas (850 §5): cotejado como repetición, lineal en el peso; residuo delimitado en
`REVIEW_002_BC.md` C.3 punto 3».
