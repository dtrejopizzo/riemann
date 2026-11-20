# Ronda 3, opción 1 — Familias de funcionales que ven la ventana y no son la modal theta (memo de selección)

Objetivo (★): λ_A(T) ≥ 0 para todo T, con las definiciones de `../phase-211-sign-sandbox/STATEMENT_001.md`.
Pregunta: ¿hay una familia por ventana, no recorrida, en la que la incidencia Σ_{d|k}Λ(d) = log k actúe sobre
funcionales que no conmutan con traslaciones, de modo que la fuga que resta la truncación (`REVIEW_002_BC.md`,
Lema B-1) quede compensada exactamente por un término de borde con signo, específico de Λ? En particular, ¿da la
malla de Nyquist un cuadrado en los valores muestreados F̂(ω_k)?
Notación: Q = 1_{I_T}, R = 1 − Q, U_a la traslación por a en ℝ, ω_k = πk/(2T) (P47 thm:nyq; el encargo escribe
πj/T, que es la subred par), s_k = s_T(ω_k) con el símbolo truncado de thm:nyq, N = e^{2T}.
Abreviaturas: «GRAM», «GLOBAL» como en `ROUND_002_B.md`. Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED /
OPEN / NO-GO / NUMÉRICO.

## Cotejo

### Qué se buscó

grep (sin distinguir mayúsculas) en `03-research/` (todas las fases), `04-papers/47…/main.tex`, el grid, el
crucigrama y los `ANNEX_*.md` de esta fase, por: truncated translation, traslaciones truncadas, compressed
dilation, Wiener–Hopf, Toeplitz–Hankel, Nyquist, malla de Nyquist, omega_k, Shannon, prolate, Slepian, boundary
jet, collar, leakage, fuga, time-limited, band-limited, Paley–Wiener, de Branges, reproducing kernel; y, dentro
de los archivos con «Nyquist», por divisor / incidence / mcd / gcd / Λ∗1. Las mayores concentraciones: Nyquist
en 60, 155, 159, 186, 193, 211; collar en 101, 121, 124, 161, 162, 163, 170; prolate/leakage en 72, 106, 114,
116, 186, 199, 200, 211; de Branges/Paley–Wiener en 159, 160, 60, 64. Abiertos en primaria: P47 thm:nyq,
lem:nyq-sampling, prop:nyq-alias, prop:nyq-LK, prop:nearfree, rem:boxes, thm:coer-schur, eq:collar;
R186_052 §§0–1, R186_053 §§0–1, R186_117/118 (veredictos); 204 `P1_BBSTAR_001.md` §3; 211 `ROUND_005_C.md`
§§1, 5.2–5.3 y su ficha en `ANNEX_211_FILES_6.md` (con las de ROUND_001_C, ROUND_002_A, ROUND_005_A,
ROUND_006_B); 191 `SPEC_B_SELECTED_FREQUENCY.md` §1. No abiertos en primaria (sólo por anexo o por el
listado del grep): fases 60, 72, 114, 116 (salvo lo que cita `REVIEW_002_BC.md`), 121, 124, 155, 159, 161,
170 (salvo por `RULES_AVOID.md` §I), 199, 200. Una búsqueda sin coincidencias no prueba novedad.

### Inventario de familias por ventana ya escritas

| # | Familia | Dónde | Qué dio | Por qué se detuvo |
|---|---|---|---|---|
| 1 | Traslaciones truncadas término a término B_nF = Qτ_{log n}F − F | 204 `P1_BBSTAR_001` §3, Prop. 3.1 | 𝒲 = Σ(v_n/2)‖B_nF‖² + [arch − ⟨F,wF⟩], w ≥ ½Σv_n | resto cuesta la masa del peine (PROVED mód. prop:primeblind); lineal en Λ |
| 2 | Traslaciones truncadas agrupadas en base fija | misma memo, §3 («grouped Cholesky of A_MU (b) / C8: indexed, not retried»); `REVIEW_002_BC` Lema B-1 | Q_B = clase (i) − fuga | resto no examinado; residuo K3 no agrupado: «clase vacía de candidatas», OPEN |
| 3 | Palabras de traslaciones truncadas, Krylov del peine | 211 ROUND_005_A Lema 3.2, Prop. 3.3 (Π² = Qσ_v²Q − 𝔏*𝔏); ROUND_006_B Prop. 4.1–4.3 (halo/fuga, constante ½) | [Λ∗Λ indefinido] + [valor medio ≥ 0] − [fuga] | NO-GO de clase para j acotado y generadores v-homogéneos (cΛ actúa sólo por el haz) |
| 4 | J_T comprimido, B_T^{−1/2}J_TB_T^{−1/2}, funcionales ⟨F,c⟩, ⟨F,s⟩ | R170_301 §§2–5 (vía `REVIEW_002_BC` B.1.5) | E_T = Γ_T + 2A_T I − J_T + 2\|c⟩⟨c\| | genérico; falsificador a₂ = 100 |
| 5 | Muestreo de Nyquist: identidad diagonal en las muestras | P47 thm:nyq, prop:nyq-alias, prop:nyq-LK | a_T = (1/4T)Σ_k s_k\|F̂(ω_k)\|² | reformulación (N); 191 SPEC_B §1 la clasifica REF-D |
| 6 | Álgebra de Nyquist: dos estructuras de espín, conos, Herglotz del peine muestreado | R186_052 Teor. 1.2, 2.1–2.4, 3.1–3.5, §4; R186_053 Teor. 2.1 | a_T = ½[s(D_per) + s(D_anti)]; cono circulante falla en toda ventana | «contact with the sign: none»; Bochner–Herglotz en ℤ es positividad en el círculo, no en la semicircunferencia; M₁ |
| 7 | Bloque negativo de Nyquist y complemento de Schur | 211 ROUND_001_C Teor. 1, Prop. 4; ROUND_002_A Teor. F, Prop. M, Cor. M1–M2 | (L2′); muestra profunda ⟹ casi-coincidencias n′^{q_n} ≈ n^{q_{n′}} | ningún criterio sobre las muestras solas decide (Prop. 4); Schur sólo con piso NO-GO |
| 8 | Respuestas del peine en la malla con Λ∗1 = log | 211 ROUND_005_C Prop. 2 (Πφ_q = φ_qψ_q, polinomios de Dirichlet torcidos por Λ en la malla), §5.3 | identidad de Selberg en las entradas cúbicas; cotas de factores de Euler locales | NO-GO de clase (§5.3(iv)): identidades del peine válidas en todo sistema de Beurling o para a_P, aplicadas sobre E_T |
| 9 | Collar / operador de borde 𝓔_N | P47 eq:collar, thm:PCfinite, prop:GEgap; R170_840 Teor. 6.1, 862, 863, 870 (vía `RULES_AVOID` §I) | 𝓞B_N = D_N𝓞 − 𝓔_N | ley bilateral de collar NO-GO por composición lineal (840); pared de paridad (870); conversión de la cola en cuadrados: `ROUND_002_A` + `REVIEW_002_A` |
| 10 | Jets de borde y de Tate | 121 atlas («two Tate jets»), R170_862–863, 211 LEDGER C21 (presupuesto de borde (EB_C), OPEN) | inercia de Pontryagin; presupuesto de borde | sin signo; (EB_C) OPEN |
| 11 | Proyección sobre P_T, funcionales A, B, exponenciales de Tate a trozos | P47 thm:coer-schur, prop:AM; 211 ROUND_005_C Lema 1 (gauge de Tate) | reducción exacta a S_{T,k} finita | reformulación (L2) |
| 12 | Prolatos / Slepian / Paley–Wiener / de Branges de la ventana | fases 72, 114, 155, 159, 186 (R186_044), 199, 200, 211 | sector prolato, kernels reproductores | `RULES_AVOID` C1: «Sonin, prolatos, semilocal como fuente de signo» cerrados |
| 13 | Resonadores (tests ciegos a casi-coincidencias) | P47 prop:nearfree, rem:boxes | a_T(F_b) ≥ c_0‖F_b‖²; Σ_{d\|m}Λ(d) = log m entra en el test de Schur | barrera: no informan del signo (rem:boxes) |

Sobre la pregunta concreta (incidencia en la malla de Nyquist): **está escrita** en 211 ROUND_005_C. Prop. 2
identifica las respuestas del peine en la malla con polinomios de Dirichlet torcidos por Λ; §5.3(i) usa la
multiplicatividad de forma no lineal (Selberg sobre las entradas cúbicas, cuyo corte depende sólo de N = mn) y
§5.3(iv) cierra con NO-GO de clase el uso de Λ∗1 = log, Selberg y los factores de Euler locales como mecanismo
de signo sobre E_T, porque esas identidades valen literalmente en sistemas de Beurling y para a_P, donde (SL_T)
falla (ejemplo NUMÉRICO 0.24 y 0.51). La lectura de la identidad Σ_{n<N}(log n)n^{−s} = Σ_{dm<N}Λ(d)(dm)^{−s}
evaluada en s_k = ½ + iω_k es thm:PCfinite (fila K1) en la malla.

### (1) Antecedente más cercano

Para la malla: 211 `ROUND_005_C.md` Prop. 2 y §5.3 (leído en primaria), con R186_052 §4 (el peine muestreado
es de tipo positivo, sin signo) y P47 thm:nyq. Para las traslaciones truncadas agrupadas: 204 `P1_BBSTAR_001.md`
§3 y `REVIEW_002_BC.md` Lema B-1. Para el borde: P47 eq:collar y R170_840 Teor. 6.1.

### (2) Objeto realmente nuevo

Ninguno que lleve signo. Lo que esta memo añade son tres restricciones PROVED (§1) que delimitan dónde puede
estar un V_T por ventana y qué hace la fuga, y una descripción exacta de por qué la malla separa la incidencia
de la ventana (§2). Con ellas, lo que faltaría escribir de un candidato es: una familia de funcionales acotados
en la norma N_T (Lema E), soportados en el collar (T − log I, T) (Lema F), que acoplen nodos distintos de la
malla con coeficientes que dependan de los valores Λ(n) del peine (Lema S); ℋ_T, V_T, ρ_T de tal familia no
están escritos y no sé escribirlos.

### (3) Por qué el cambio evitaría la dificultad del antecedente

No la evita. La dificultad registrada en ROUND_005_C §5.3 es que las identidades del peine que se usan valen en
todo sistema de Beurling y para a_P. La incidencia en la malla es exactamente una de ellas (Lema S: actúa nodo
a nodo, como identidad de polinomios de Dirichlet en el mismo s_k). Pasar de E_T a la malla completa no cambia
la clase de identidades.

### (4) Identidad que conectaría con la positividad global

Sólo reformulaciones ya registradas: thm:nyq (diagonal en las muestras), (L2′) de ROUND_001_C, y, para las
traslaciones truncadas, Lema B-1. El Lema F de abajo dice qué parte de ρ_T es la obligación de signo: en el
interior es una forma de símbolo s_T − σ_B sobre P_{T′}.

### (5) Líneas que se rompen para cΛ y a_P

No hay paso de signo, luego no hay línea de signo que señalar. La única línea que deja de ser cierta es la
sustitución Σ_{d|n}a(d) = log n en el valor de cada nodo (c log n para cΛ; el logaritmo de la parte P-rugosa
para a_P): rompe la identidad linealmente, como el separador; no rompe una desigualdad. Por `OBJECT_SPEC.md` §4
la familia no está lista para construcción.

**Veredicto del cotejo: repetición para la malla con incidencia (ROUND_005_C §5.3; K1) y para las traslaciones
truncadas agrupadas en base fija (P1_BBSTAR §3; B-1). Sin mecanismo nuevo.** Las piezas de §1 son cortas y
completas; se escriben porque delimitan el terreno y no requieren derivación adicional.

## 1. Tres restricciones PROVED sobre un V_T por ventana

En todo lo que sigue, (G) es a_T(F) = ‖V_TF‖² + ρ_T(F) sobre P_T ∩ 𝒟_T con ρ_T ≥ 0.

**Norma de control.** Sea N_T(F)² := (1/2π)∫(1 + log(2 + |τ|))|F̂(τ)|² dτ. Existe C_T con
|a_T(F)| ≤ C_T N_T(F)² en 𝒟_T. *Demostración.* |m(τ)| ≤ C + log(2 + |τ|) (asintótica de ψ; CITED, P47
lem:mbounds) y |Σ_{log n<2T} v_n cos(τ log n)| ≤ 𝒜_T = Σ v_n; luego |s_T(τ)| ≤ C_T(1 + log(2 + |τ|)). ∎

**Lema E (NO-GO con clase, PROVED).** Si vale (G), entonces V_T es acotado de (P_T ∩ 𝒟_T, N_T) en ℋ_T. En
particular ninguna componente escalar de V_T (ningún ⟨V_TF, e⟩, e ∈ ℋ_T) puede ser, sobre las funciones lisas
hasta el borde, de la forma αF^{(j)}(T−) + (funcional N_T-acotado) con α ≠ 0, j ≥ 0; lo mismo en −T y en
cualquier punto interior.

*Demostración.* ‖V_TF‖² ≤ a_T(F) ≤ C_T N_T(F)² por ρ_T ≥ 0. Para la segunda parte, sea φ ∈ C^∞[0,∞) con
soporte en [0,1] y φ^{(j)}(0) = (−1)^j, y g_λ(t) := λ^{−j}φ(λ(T − t)) en I_T. Entonces g_λ^{(j)}(T−) = 1, y
|ĝ_λ(τ)| ≤ λ^{−j−1}‖φ‖_1 para |τ| ≤ λ, |ĝ_λ(τ)| ≤ Cλ^{−j}/|τ| para |τ| > λ (una integración por partes: el
término de borde en T es λ^{−j}φ(0) y ‖g_λ′‖_1 = λ^{−j}‖φ′‖_1), de modo que N_T(g_λ)² ≤ C(λ^{−2j−1} log λ) → 0. Fijense h_1, h_2 ∈ C_c^∞(−T, 0)
con det[A(h_i), B(h_i)] ≠ 0 (existen porque e^{t/2} y e^{−t/2} son linealmente independientes en (−T,0)) y
F_λ := g_λ − a_λh_1 − b_λh_2 ∈ P_T con |a_λ| + |b_λ| ≤ C(|A(g_λ)| + |B(g_λ)|) ≤ Cλ^{−j−1}. Entonces
N_T(F_λ) → 0 (N_T es una norma) y F_λ^{(j)}(T−) = 1. Si ⟨V_TF, e⟩ = αF^{(j)}(T−) + β(F) con β N_T-acotado,
|α| ≤ |⟨V_TF_λ, e⟩| + |β(F_λ)| ≤ (C_T^{1/2}‖e‖ + ‖β‖)N_T(F_λ) → 0, contradicción. ∎

Clase declarada: V_T con alguna componente que no es N_T-acotada sobre P_T ∩ 𝒟_T. Consecuencia: los
«funcionales de borde» admisibles son promedios de collar ∫F φ con φ ∈ L² (en rigor, con φ̂ en el dual de N_T),
no valores ni jets. Es la contrapartida por ventana de R-cont (que no aplica aquí: `OBJECT_SPEC.md` §3 la
restringe al portador de escalas enteras de A_0 y a la holomorfía de z ↦ P_z; L²(I_T) con la malla fija no es
ese caso). Las muestras F̂(ω_k) sí son N_T-acotadas (|F̂(ω)|² ≤ 2T‖F‖²), luego el Lema E no las excluye.

**Lema F (localización de la fuga, PROVED).** Sea ℓ_i = x_iQU_{log i}, x_i ∈ ℂ, con x_i = 0 para i > I, y
Q_B como en `REVIEW_002_BC.md` Lema B-1 (σ_B(τ) = Σ_dΛ(d)|Σ_{d|i}x_i i^{iτ}|²). Sea T′ := T − ½log I > 0. Si
a_T = Q_B + ρ_T con ρ_T ≥ 0 sobre P_T, entonces para todo F ∈ P_{T′} ∩ 𝒟_{T′}

    a_{T′}(F) ≥ (1/2π)∫σ_B(τ)|F̂(τ)|² dτ.

En particular, toda sucesión casi-minimizante de a_{T′} sobre P_{T′} (‖F‖ = 1) cumple
(1/2π)∫σ_B|F̂|² ≤ λ_A(T′) + o(1).

*Demostración.* Para G ∈ P_{T′}, sea F := U_{−c}G con c = ½log I (soporte en (−T, T − log I)). (a) P_T: A(F) =
e^{−c/2}A(G), B(F) = e^{c/2}B(G), luego F ∈ P_T. (b) Fuga nula: para i ≤ I, U_{log i}F tiene soporte en
(−T + log i, T − log I + log i) ⊂ I_T, así RΣ_{d|i}x_iU_{log i}F = 0 y, por Lema B-1, Q_B(F) =
(1/2π)∫σ_B|F̂|². (c) a_T es invariante por traslación (forma de símbolo), y sobre L²(I_{T′}) coincide con
a_{T′}: los términos del peine con 2T′ ≤ log n < 2T aportan v_n Re c_G(log n) = 0 porque sop c_G ⊂ [−2T′, 2T′]
y c_G(±2T′) = 0. (d) |F̂| = |Ĝ|. Entonces a_{T′}(G) = a_T(F) = Q_B(F) + ρ_T(F) ≥ (1/2π)∫σ_B|Ĝ|². ∎

Lectura. En la familia de traslaciones truncadas agrupadas, la fuga sólo actúa sobre la masa de F en el collar
(T − log I, T). Sobre el interior, (G) exige una positividad de la forma de símbolo s_T − σ_B ≤ s_T en la
ventana T′, es decir (★) en T′ con margen (1/2π)∫σ_B|F̂|² ≥ 0 (cf. Lema B-2). Como λ_A(T′) ≤ 4·10⁹T′e^{−15.449T′}
para T′ ≥ 1 (P47 cor:margin1, CITED), los cuadrados agrupados tienen que anularse casi exactamente sobre los
casi-minimizantes de todas las ventanas más cortas. Si además los x_i no dependen de T y se exige (G) para
todo T (O5), esa condición vale para todo T′ grande. No es imposibilidad: no excluye σ_B pequeño donde
|F̂*|² vive. Respuesta a la pregunta del encargo: una compensación «fuga = término de borde con signo» sólo
puede ocurrir en el collar de longitud log I junto al borde derecho (y, simétricamente, con traslaciones
negativas, junto al izquierdo); fuera de él no hay ni fuga ni borde.

**Lema S (la incidencia en la malla es local en el nodo, PROVED).** (i) La operación n ↦ dn multiplica el modo
e^{iω_k log n} por d^{iω_k}: sobre las muestras es diag(d^{iω_k}), restricción a la malla del multiplicador
e^{iτ log d}, es decir la rotación del círculo 𝕋_{4T} por log d. (ii) Para 0 ≤ a < 2T y F ∈ L²(I_T),
QU_a^{𝕋}F = QU_aF (la parte que da la vuelta cae en (−2T, a − 3T) ⊂ ℝ∖I_T). (iii) La identidad
Σ_{n<N}(log n)n^{−s} = Σ_{dm<N}Λ(d)d^{−s}m^{−s} en s = s_k relaciona valores en el mismo nodo k. (iv) En la
identidad thm:nyq a_T es diagonal en las muestras, y lo que acopla nodos distintos es sólo la restricción de que
(F̂(ω_k))_k esté en la imagen de la compresión a la semicircunferencia, una matriz de Toeplitz sin Λ (núcleo
sinc; R186_053 Lema 1.1). *Demostración.* (i), (iii): directas. (ii): U_a^{𝕋}F tiene soporte en (−T + a, T + a)
módulo 4T; los puntos de (2T, T + a) pasan a (−2T, a − 3T) y a − 3T < −T. (iv): lem:nyq-sampling (i)–(ii). ∎

**Consecuencias de los lemas (PROVED, una línea cada una).**
- Si V_T es un multiplicador en el índice de muestras, (V_TF)_k = x_kF̂(ω_k), entonces ρ_T tiene muestras
  s_k − |x_k|² ≤ s_k: es el Lema B-2 en el círculo. (Por thm:nyq, ρ_T(F) = (1/4T)Σ(s_k − |x_k|²)|F̂(ω_k)|².)
- Por (i)–(ii), toda familia construida con la incidencia actuando sobre los modos y con Q está en el álgebra
  generada por multiplicadores del círculo y traslaciones truncadas de la recta: es la de las filas 2–3 del
  inventario, no una familia nueva.
- Toda componente de V_T que factorice por (A(F), B(F)) es nula sobre P_T (proyección sobre P_T, fila 11).
- Una incidencia sobre los índices de nodo (cuadrados Σ_dΛ(d)|Σ_{d|j}x_jF̂(ω_j)|², es decir [log mcd(j,l)] en
  la malla) no contiene los pesos v_n del peine: es la misma para Λ, cΛ, a_P y cada modelo de la batería, y toda
  la dependencia en el peine queda en ρ_T. No hay relación aritmética entre el índice j y los n del peine (la
  fase es πj log n/(2T)). Es una energía auxiliar sin mecanismo de signo (`RULES_AVOID.md` A4); no la excluyo.

## 2. Frente a O6, prop:nearfree y K1

- **O6.** Las muestras ven las casi-coincidencias: una muestra profunda s_k ≪ 0 exige ω_k log n ≈ 0 mod 2π para
  muchos n a la vez, lo que fuerza n′^{q_n} ≈ n^{q_{n′}} (211 ROUND_002_A Cor. M1–M2, CITED). Pero las ven en el
  valor s_k, no en un acoplamiento entre nodos (Lema S(iv)); por eso un V_T diagonal en las muestras no aporta
  nada (consecuencia 1) y uno no diagonal acopla nodos sólo a través de la matriz sin Λ o de una aritmética del
  índice sin peine.
- **prop:nearfree.** Los resonadores tienen a_T ≥ c_0‖F‖² con Σ_{d|m}Λ(d) = log m usado en un test de Schur
  (P47, prueba de prop:nearfree; rem:boxes): uso lineal y acotado del separador, sin signo sobre los vectores
  que ven Near. Una familia por ventana útil tendría que vivir donde prop:nearfree no da nada: vectores
  N_T-acotados (Lema E) con masa en el collar (Lema F) que vean casi-coincidencias. No tengo tal familia.
- **K1.** La lectura en la malla de la incidencia hiperbólica es thm:PCfinite en s_k; su residuo es el de K1 y
  K1′ (cola H_{M,N} sumada con E_N y Tate), sin objeto.

## Resultado

**Sin mecanismo nuevo** (repetición de 211 ROUND_005_C §5.3, de K1 y de P1_BBSTAR §3 / Lema B-1). Además, una
pieza **NO-GO con clase PROVED** (Lema E: componentes no N_T-acotadas, en particular valores y jets de borde) y
dos piezas **PROVED** sin signo (Lema F: la fuga de traslaciones truncadas agrupadas sólo actúa en un collar y el
resto interior es (★) en T′ con margen; Lema S: la incidencia en la malla es local en el nodo y su álgebra con Q
es la de traslaciones truncadas).

## Qué se probó

- Lema E (NO-GO, clase: V_T con alguna componente no acotada en N_T sobre P_T ∩ 𝒟_T).
- Lema F (localización de la fuga; condición necesaria sobre casi-minimizantes de ventanas más cortas).
- Lema S y sus cuatro consecuencias (multiplicadores de muestras ⟹ resto con muestras ≤ s_k; la incidencia en
  los modos no genera una familia nueva; funcionales de Tate nulos en P_T; incidencia en índices de nodo
  independiente del peine).
Nada de esto es avance de signo.

## Qué falló y por qué

- En la malla, la incidencia de divisores vive en el valor de cada nodo y la ventana en una matriz sin Λ que
  acopla nodos; no encontré operación que las junte en un cuadrado, y la que junta valores en un nodo ya fue
  usada y cerrada por la clase Beurling/a_P (ROUND_005_C §5.3(iv)).
- Los términos de borde puntuales están prohibidos (Lema E); los de collar son lineales en F y, como componentes
  de V_T, aportan cuadrados sin signo propio; la ley bilateral de collar por composición lineal está cerrada
  (R170_840 Teor. 6.1, CITED vía `RULES_AVOID` I6).
- La fuga del Lema B-1 sólo ayuda en el collar (Lema F); en el interior el resto exige más que (★) en T′.

## Qué queda NO excluido

- Funcionales de collar N_T-acotados con coeficientes que dependan de los valores Λ(n) (fuera de la hipótesis
  «ℓ_i independientes de los pesos»); ninguno escrito.
- Acoplamientos no diagonales entre muestras de Nyquist con coeficientes que dependan del peine (no la
  aritmética del índice de nodo, que es independiente de él); ninguno escrito.
- Traslaciones truncadas agrupadas con x_i elegidos de modo que σ_B sea pequeño sobre los casi-minimizantes
  (Lema F lo exige, no lo prohíbe), con la compensación de la fuga en el collar; sin objeto.
- Familias sobre 𝔸_M y la formulación (S); compensación conjunta D + E (GLOBAL); el residuo K3 no agrupado de
  P1_BBSTAR (clase vacía de candidatas, no NO-GO).
- Las fases listadas como no abiertas en primaria en el Cotejo.

## Siguiente paso concreto

Ninguno dentro de esta opción con objeto. Para el registro (esta memo no edita otros archivos): fila de ledger
«K2″, familias por ventana distintas de la modal (traslaciones truncadas agrupadas, Nyquist, borde, P_T): sin
mecanismo nuevo; NO-GO PROVED para componentes no N_T-acotadas (valores y jets de borde); fuga localizada en el
collar (Lema F); incidencia en la malla local en el nodo (Lema S)». Condición de reapertura: un acoplamiento entre
nodos de Nyquist, o un funcional de collar N_T-acotado, cuyos coeficientes dependan de los valores Λ(n) y cuya
identidad con a_T no valga en un sistema de Beurling ni para a_P, señalando la línea.
