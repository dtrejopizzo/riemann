# Anexo — Cotejo dirigido: Hodge, Lorentz, Alexandrov–Fenchel, log-concavidad

Pregunta cotejada. En cada sector de paridad de J: t ↦ −t, P_T tiene codimensión uno; (★) en un sector
equivale a que a_T tenga a lo sumo una dirección negativa en el espacio entero del sector, con el vector
de Tate (cosh(t/2) o sinh(t/2)) como dirección temporal, es decir a una Cauchy–Schwarz invertida
a_T(F, G)² ≥ a_T(F) a_T(G) para G temporal. Se busca en el corpus si alguien intentó probar esa signatura
por un MECANISMO DE CIERRE (inducción, log-concavidad, cierre bajo producto, derivada direccional,
límite, borrado/contracción), y no sólo enunciarla o contarla. Este anexo no propone construcciones.

## 1. Qué se buscó

Grep sin distinguir mayúsculas en `03-research/` (todas las fases), `04-papers/` (43–48),
`00-references/`, `05-meta-and-planning/` (índice, SURVEY_MODERN_UNTRIED, crucigrama) y el grid maestro,
con las palabras del encargo agrupadas en una sola expresión (Hodge index, índice de Hodge, Hodge–Riemann,
Kähler package, hard Lefschetz, Lorentz/Lorentzian, reverse Cauchy, Cauchy–Schwarz invertida, Alexandrov,
Aleksandrov, Fenchel, mixed volume, mixed discriminant, Brunn–Minkowski, log-concav/log-cóncav, matroid,
Chow ring, Adiprasito, Brändén, one positive eigenvalue, exactly one negative, hyperbolic polynomial,
completely log, Gårding). Resultado: **740 archivos** con al menos una coincidencia (la mayoría por
«Hodge index» en las fases 4–50 y por copias de respaldo del grid). Después se afinó por subfamilia
(Lorentzian/completely log: ~25 archivos de investigación; log-concav: ~25; matroid/Chow ring/Adiprasito:
~25; Alexandrov/mixed volume/mixed discriminant: 10; Gårding/hyperbolic polynomial/Borcea: ~25) y se
cruzó con el índice (README, 02, 03, 04, 05, 05b, 06, AUDIT_PHASE193_CERTAINTY, SURVEY_MODERN_UNTRIED).

**Abiertos en primaria (lectura de la sección pertinente o completa), 31 archivos:**
fase 212: README, OBJECT_SPEC, LEDGER, BRIEF_CONSTRUCTOR, REVIEW_003, REVIEW_004, ROUND_004_E (§§Cotejo,
1, 2); fase 211: STATEMENT_001, ROUND_004_A §3; `phase-160/R160_C7_R1.md` §0, §6; `R160_S3_SURVEY.md`
§3.1 (T20) y lead 4; `phase-138/R138_001_ROUND1.md` D.15.2 y lista de cierre; `phase-120/
P3_MATROID_FUSION_NO_GO.md` completo; `P3_G125_T2_AHK_CORRECTION.md` §§4–5, 8;
`phase-114/114_d_244_FOURIER_TANGENT_HODGE_FORM.md` veredicto, §§3, 5–7; `phase-41/126-hodge-index-on-
the-square-attainable.md` resumen y §1; `phase-195/INV_M_001_REAL_STABILITY_GARDING_MSS_NO_GO.md` §§2–5;
`phase-200/D_CONSTRUCTION_001.md` resumen y tabla de cotejo (§5 por encabezado); `phase-201/
FAMILIES_A_001.md` A1; `FAMILIES_B_001.md` F30; `phase-193/CA_F_000_SEEDS.md` F5; `CA_F_SYNTHESIS.md`;
`phase-186/R186_033_NEW_INSIGHT.md` Idea 2; `phase-135/R135_007_CLOSING_DECISION.md`;
`phase-16/06-hunt-indefinite-object.md` principio; `phase-11/M11.4-5-verdict…` veredicto;
`phase-104/104_21_GLOBAL_COMPOUND_POISSON_TP_GATE.md` (línea de log-concavidad); líneas de coincidencia
en `phase-211/ROUND_005_D.md`, `phase-207/CLASS_001.md`, `phase-206/AUDIT_206_001.md`,
`phase-212/ROUND_004_D.md`, `phase-162/R162_1602`, `phase-200/SPEC_SIGN_OBJECT_008.md`; y las filas del
índice citadas abajo.

**No abiertos en primaria (sólo vistos por la fila del índice o por la línea de grep):** Paper 46
(`main.tex`, §§11–12, 17, 22–26), Paper 47 (thm:P / cor:P3 y thm:parityschur sólo vía ROUND_004_E),
Paper 43 Thm 14.1, fase 15 (M1–M10), fase 41 doc 125, fases 40, 42, 43, 107 (107_241), 113, 122, 137,
139–142, 155 (R155_054), 159 (G1_B1_R3/R4), 184 (R184_011), las fuentes de `00-references/` (Tropical
Hodge theory, Cartwright, Hodge index de Yuan–Zhang) y las fases 4, 10, 28, 33, 54, 103, 106 donde la
palabra aparece en otros sentidos.

## 2. Inventario de antecedentes

**A1. Criterio lorentziano (R138_001 D.15.2, PROVED, álgebra lineal).** Para Q simétrica y K con
Q(K) > 0: Q ≤ 0 en K^⊥ ⟺ Q(F, K)² ≥ Q(F)Q(K) para todo F ⟺ lo mismo sobre un conjunto absorbente en K.
Es exactamente la Cauchy–Schwarz invertida contra el vector temporal. Se refutó la versión «para todos
F, G en un cono convexo» (D.15.2(e)). D.15.2b: el cono efectivo es el cono equivocado; la forma
Khovanskii–Teissier sobre ese cono no está disponible; D.17.3 cae en el no-go del resto de Chebyshev
(114_d_185). Etiqueta del registro: PROVED (criterio) / RESTATEMENT; índice: G6 «retry, no sign»,
P46 §17 DEAD. Dónde se detuvo: el criterio no aporta signo; probarlo sobre el cono que detecta exige el
signo mismo.

**A2. Completación polar del cuadrado y residuo (HR-T) (R160_C7_R1, §§0, 5–6).** Construye un álgebra
𝒜 = ℝf₁ ⊕ ℝf₂ ⊕ (T) con forma B; Teor. 2: Castelnuovo Z² ≤ 2(Z·f₁)(Z·f₂) en Γ_F es literalmente W_T ≥ 0;
Teor. 3: estructura de Metzler (fuera de diagonal > 0, diagonal −∞) y estado fundamental de Perron de
A_T en L²(I_T); Teor. 4 enuncia «a lo sumo una dirección negativa en L²(I_T)» como reformulación (usa una
equivalencia externa). **§6.2 es el único examen explícito del mecanismo pedido:** (a) la clase cuadrática
de Brändén–Huh exige entradas ≥ 0 y a lo sumo un autovalor positivo; aquí la diagonal es −∞; quitar la
diagonal lleva a matrices de ceros en la diagonal que sólo son lorentzianas en el caso multipartito
completo, y las compresiones de divisibilidad no lo son; (b) cierre bajo límites: no hay familia
generadora finita (cota de arena N*(T) ≥ exp(4e^T(1+o(1)))), luego el límite no da nada más que la
definición; (c) Alexandrov–Fenchel: un modelo de volúmenes mixtos tendría diagonal V(K, K) ≥ 0, imposible
con diagonal −∞; (d) AHK: en una superficie el polinomio de volumen y el índice de Hodge coinciden. §6.3(2):
**subir de grado** (polinomio homogéneo de grado k ≥ 3 cuya hessiana sea −a_T) — candidatos Str(Γ_F^k)
dan formas bilineales complejas sin transpuesta; los candidatos con transpuesta son −a twisted por Φ_F^{k−2}
y sólo son lorentzianos si la propiedad ya vale para las formas torcidas. OPEN; «necesita una fuente
independiente de coeficientes no negativos». Etiqueta: PARTIAL / REF-D en el índice (G8H-R160_C7_R1).

**A3. Forma tangente lorentziana sobre primos (114_d_244, PROVED).** h_S = xx* − diag(|x_p|²) sobre los
canales tangentes de un conjunto finito S de primos; inercia (1, |S|−1, 0) para |S| ≥ 2, por un lema de
determinante de rango uno menos diagonal. **Cierre por límite cofinal en S** (§5): compatibilidad por
extensión por cero, forma límite |Σ√log p z_p|² − Σ log p |z_p|², negativa sobre el núcleo primitivo;
levantamiento a potencias de primos con coeficiente Λ(p^{k+ℓ})/√p^{k+ℓ}. Se detuvo (§6): obstrucción de
rango — el término de grado es de rango uno en cada S y la parte arquimediana G_∞ tiene rango infinito;
además es de segundo orden en las velocidades mientras la forma objetivo es de primer orden (R160_S3 lead 4,
D.258–259). Índice: G4D «PARTIAL, genuine signature theorem, dead-ended».

**A4. Persistencia puntual de Hodge–Riemann bajo sistemas dirigidos (P3_G125_T2_AHK_CORRECTION §5,
PROVED).** Si q_{S′} restringe a q_S y q_S ≤ 0 en los primitivos compatibles, la forma inducida es ≤ 0 en
el colímite algebraico, sin tomar límites de signatura. Es una regla de cierre bajo «agregar primos», pero
presupone la signatura en cada S finito, que debía venir de un anillo de Chow de matroide (AHK) sobre los
estratos de colisión de primos (§4, condiciones 1–6). **P3_MATROID_FUSION_NO_GO (PROVED):** no existe
inyección ℕ → retículo de flats con Φ(i + j) = Φ(i) ∨ Φ(j), porque el join es idempotente
(Φ(2i) = Φ(i)); la iteración aditiva fiel de Frobenius no cabe en un retículo de matroide. Candidato
retirado antes de llegar a Hodge–Riemann. Índice: G4H-phase-120/P3 DEAD.

**A5. AHK frente al cuadrado del sitio de escalado (fase 41, doc 126).** Análisis del paquete de Kähler:
AHK requiere anillo graduado finito, dualidad de Poincaré, clase amplia y la inducción por flips sobre un
retículo finito; el objeto es infinito y continuo, lo que rompe la inducción finita; obstrucción de tipo
Babaee–Huh. Veredicto (d) «indeterminable», sesgo a circular (usa una equivalencia externa). Etiqueta:
análisis, sin teorema; índice P41-2 NO-GO, G8H-R160_S2 PARTIAL (señal (1,2) de juguete no persistente a
rango infinito).

**A6. Estabilidad real, conos de Gårding, MSS (phase-195 INV_M_001, PROVED).** Sobre el símbolo
multiafín polarizado del bloque 𝔸 en {1, 2, 3, 6}: Teor. M1/M2, no es real estable — en cada cara
coordenada donde la forma es definida positiva la desigualdad de Rayleigh Δ_ij p ≥ 0 falla, porque
estabilidad = Cauchy–Schwarz invertida (signatura (1, n−1)) y el blanco allí era definido. §3: una
cuadrática definida no es hiperbólica en ninguna dirección; el único cono de Gårding útil es el cono PSD
(REF-D). §4: MSS da ∃ y no ∀. **Nota:** este intento aplicó la teoría estable/lorentziana a la forma
restringida (blanco definido), no a la forma en el espacio entero del sector con la dirección de Tate.

**A7. Hodge–Riemann/Lorentz no AHK (phase-193 CA_F_000_SEEDS F5; CA_F_SYNTHESIS).** Lema F5
(Haynsworth, PROVED): positividad sobre los primitivos ⟺ k ≤ 2 negativos y una condición 2×2 de Schur
(= P47 thm:parityschur). Descartada como «retry» con el argumento «Theorem P: n₋ en el espacio entero > 2
a T grande, la hipótesis de signatura es falsa». **Ese argumento está mal citado:** AUDIT_PHASE193 fila 35
lo marca «Theorem P mis-cited; FIX», y ROUND_004_E Prop. 1 y tabla §1 muestran que los conteos
crecientes son de 𝔪_T (sin peine), mientras que para a_T, si λ_A(T) > 0, n₋(a_T|L²(I_T)) ≤ 2. El
descarte de F5 queda, pues, sólo como «reformulación sin mecanismo».

**A8. Transferencia del índice de Hodge condicional a h⁰ (R135_007 Thm 12.3; P46 §§11–12; fases
137–142, 155).** Clase canónica K, dualidad σ_K, teorema de transferencia PROVED condicional a una
h⁰ ≥ 0 con (a), (b′) y la desigualdad de Riemann–Roch (c). h⁰_Z sobre traslaciones de potencias de
primos cumple (a), (b′) y falla (c) (crecimiento (log m)^{3/2} frente a ¼m², D.11.3); h⁰ tensorial (140)
lee sólo bidegrados; frame defect (142 Thm 19.25) excluye la h⁰ con (a), (b′), (c); el falsificador Ξ_a
rompe la transferencia. Índice: W10 MW-5/OT-5′ NO-GO; G1H-P46 DEAD.

**A9. Arakelov / índice de Hodge aritmético (fase 15, 40, 122; R9-05, R9-09; L26, L80, L83).** Import
de Faltings–Hriljac/Yuan–Zhang: controla alturas, no tipa en el portador; P40-3 CIRCULAR (positividad
espectral frente a de intersección). No abiertos en primaria aquí.

**A10. Volumen mixto (phase-200 D_CONSTRUCTION_001 §5).** Kazarnovskiĭ/BKK + Minkowski
V(P, Q)² ≥ V(P, P)V(Q, Q): da una forma entera cuadrática con signatura de Hodge, pero no ve los
coeficientes, es genérica para Beurling y Epstein, y su inmersión isométrica equivale a (W⁰)
(REF-D, PROVED). R160_C7_R1 §6.2(c) añade: diagonal de volumen ≥ 0, incompatible con la diagonal −∞.

**A11. Discriminante mixto (211 ROUND_004_A Prop. 1, PROVED).** Las condiciones necesarias (C_k) en
2×2 contienen Σ v_m v_n ½D(R_m, R_n), discriminante mixto de matrices de solapamiento; acopla pares de
potencias de primos sin relación aritmética. Condición necesaria, no mecanismo; NO-GO de clase
(Prop. B: subespacios finitos independientes de Λ no llevan el signo).

**A12. Log-concavidad/log-convexidad.** (i) R186_033 Idea 2: convexidad de log λ_A(T) en una variable
canónica — NO-GO NUMÉRICO (falsificada en T, e^{2T}, e^{4T}). (ii) 211 ROUND_005_D: log-concavidad del
perfil de estado fundamental OPEN, «no esperada», NUMÉRICO. (iii) 212 ROUND_004_D: funciones de Pólya
PF₂ excluidas porque 𝖡 no es ≥ 0. (iv) R162_1602: suma de ≥ 2 deltas falla PF₂. (v) 104_21: secuencia
compuesta de Poisson ni log-cóncava ni PF₂ para 1 < Q < 3. (vi) Turán/Jensen/Laguerre–Pólya/log-concavidad
de coeficientes de Taylor (índice L22, L23, L75, A14a; NG-D1/D2; G1F-103): propiedades del lado de
Fourier o de toda serie de Euler con coeficientes ≥ 0, clase 𝒦_inh, Teor. B de 207 CLASS_001 (falsificador
a_P). (vii) FAMILIES_A A1: «aplicar log-concavidad a (Λ(n)/√n) o a (c_N) sería una condición de cono
sobre una sucesión» — descartado por adyacencia, sin construcción.

**A13. Indefinición como principio (fase 16, memo 06; fase 11).** Principio: el portador debe tener
signatura intrínseca Lorentz/Pontryagin; una modificación de Klein–Gordon ingenua de las resonancias
modulares sigue definida. Fase 11: la ruta de hiperbolicidad/total positividad «es una positividad».
Sin objeto.

**A14. Inercia y formato de Pontryagin (ROUND_004_E; P47 thm:parityschur, prop:polarcap,
subsec:inertia-excl; fase 197 BARRIER_W).** Conteo de índices; constancia en c cerca de 1. Ya cubierto
por el encargo.

## 3. Clasificación

| Antecedente | Clase |
|---|---|
| A1 criterio lorentziano D.15.2 | (a) reformulación |
| A2 R160_C7_R1 (Teor. 4; §6) | (a) reformulación; §6.2–6.3 es examen negativo del mecanismo (sin construcción) |
| A3 forma tangente 114_d_244 | (c) degenerada: signatura (1, n−1) sobre primos con cierre por límite cofinal en S, pero el mecanismo es un lema de rango uno menos diagonal, no inducción ni log-concavidad, y la forma no es a_T |
| A4 persistencia + matroide de fusión (fase 120) | intento de (c) sobre objetos del problema (estratos de colisión de potencias de primos), con cierre por colímite en S; murió antes de Hodge–Riemann |
| A5 AHK/cuadrado (fase 41) | (b) transferencia |
| A6 estabilidad/Gårding/MSS (195) | (c) aplicado al blanco equivocado (forma definida); NO-GO sobre esa formulación |
| A7 F5 no AHK (193) | (a) reformulación (descartada con cita errónea) |
| A8 transferencia h⁰ (135–142, P46) | (b) transferencia |
| A9 Arakelov | (b) transferencia |
| A10 volumen mixto (200) | (b) transferencia desde cuerpos convexos/BKK, REF-D |
| A11 discriminante mixto (211) | (a) condición necesaria |
| A12 log-concavidad (186, 211, 212, 162, 104, Turán…) | pruebas de log-concavidad de cantidades escalares (λ_A en T, perfiles, sucesiones); ninguna es un mecanismo de cierre para la signatura de la forma |
| A13 principio de indefinición | (a) |
| A14 inercia | (a) conteo |

## 4. Respuesta

**¿Hay en el corpus un intento de clase (c)?** Sólo dos parciales, y ninguno sobre a_T con la dirección
de Tate en un sector de paridad.

- **Fase 120 (A4).** Operación de cierre: unión de conjuntos de primos (colímite dirigido en S, con el
  lema de persistencia puntual PROVED) y, dentro de cada S, la inducción de AHK por flips/borrado–
  contracción sobre un retículo de flats que debía codificar las colisiones C_{p^i}∘C_{p^j} → C_{p^{i+j}}.
  Lo detuvo una incompatibilidad de tipos PROVED: la iteración aditiva fiel no se inyecta en un join
  idempotente (Φ(2i) = Φ(i)). El retículo usado era el de colisiones, no el retículo de divisibilidad
  de la ventana; la inducción de AHK nunca se ejecutó.
- **114_d_244 (A3).** Operación de cierre: agregar primos (extensión por cero, límite cofinal), con
  levantamiento a todas las potencias. La signatura (1, |S|−1) sale de un lema de determinante, no de
  inducción. Lo detuvo una obstrucción de rango: el término de grado es de rango uno, la parte
  arquimediana es de rango infinito, y la forma es de segundo orden frente a la forma objetivo de primer
  orden; nunca se identificó con a_T.
- **Exámenes negativos sin construcción:** R160_C7_R1 §6.2 descarta la clase cuadrática de Brändén–Huh
  (diagonal −∞), el cierre bajo límites (no hay familia generadora finita), Alexandrov–Fenchel (diagonal
  de volumen ≥ 0) y AHK en una superficie (coincide con el enunciado); §6.3(2) deja OPEN la subida de
  grado (polinomio de grado ≥ 3 con hessiana −a_T) por falta de una fuente independiente de coeficientes
  no negativos. Phase 195 refuta estabilidad real sobre la forma definida, no sobre la forma entera del
  sector. Las demás menciones son reformulaciones (a) o transferencias (b).

Ningún archivo abierto ejecuta una inducción del tipo «signatura en la ventana T ⇒ signatura en T′ > T»,
ni una derivada direccional/polarización sobre a_T, ni borrado/contracción en el retículo de divisores de
[1, e^{2T}).

## 5. Lo no encontrado (sin afirmar novedad)

En los archivos abiertos y en las coincidencias de grep no se encontró:

1. Un intento de probar «a lo sumo una dirección negativa por sector de paridad para a_T en L²(I_T),
   con cosh(t/2) o sinh(t/2) como dirección temporal» por inducción en T (alargar la ventana) o por
   cualquier regla de cierre. El enunciado aparece sólo como reformulación (A2 Teor. 4, A7, A14) o como
   conteo.
2. Un polinomio de grado ≥ 3 en el test, construido de los objetos del problema, cuya hessiana sea a_T
   (o −a_T) y al que se aplique la caracterización de Brändén–Huh por derivadas; sólo el examen negativo
   de R160_C7_R1 §6.3(2) sobre Str(Γ_F^k).
3. Anillos de Chow, retículos de flats o deletion–contraction sobre el retículo de divisibilidad
   {n < e^{2T}} o sobre el peine; el único retículo de matroide tratado (fase 120) fue el de colisiones de
   correspondencias.
4. Estabilidad real o conos de Gårding aplicados a la forma del sector entero (signatura de Lorentz), en
   lugar de a la forma restringida o al bloque 𝔸_M (A6).
5. Log-concavidad de una sucesión o polinomio generador ligado a la signatura (por ejemplo, de
   coeficientes de un polinomio característico de compresiones de a_T); las log-concavidades examinadas
   son de cantidades escalares o de coeficientes del lado de Fourier.
6. Alexandrov–Fenchel/discriminantes mixtos con diagonal no positiva o con «cuerpos virtuales»; sólo el
   descarte por diagonal de R160_C7_R1 §6.2(c) y la condición necesaria de 211 ROUND_004_A.

Una búsqueda sin coincidencias no prueba que no se haya intentado: quedan sin abrir en primaria Paper 46,
fases 15, 40–43, 107, 113, 122, 137–142, 155, 159, 184 y las fuentes de `00-references/`. Además, un
mecanismo de signatura sobre el espacio entero del sector sigue sujeto a lo PROVED en ROUND_004_E Lema 2
(toda cota del índice negativo es una positividad en codimensión finita) y a la prueba de falsificadores
de `RULES_AVOID.md` §E: este anexo no examina si alguna regla de cierre distingue Λ de cΛ o de a_P.
