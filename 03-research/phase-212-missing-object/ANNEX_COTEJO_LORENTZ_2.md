# Anexo de cotejo — signatura de tipo Lorentz y mecanismos con reglas de cierre (tramo 2: estabilidad, Lee–Yang, Laguerre–Pólya, positividad total, cierre bajo producto o convolución, flujos)

Cotejo de sólo lectura. No propone construcciones. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`.
Etiquetas citadas tal como las declara cada fuente; donde se añade una lectura propia se marca ARGUED.
Cuando una fuente usa una equivalencia del objetivo con otro enunciado, se registra «usa una equivalencia
externa» y no se desarrolla.

## 1. Qué se buscó y qué se abrió

**Búsqueda.** grep sin distinguir mayúsculas en `03-research/` (todas las fases), `04-papers/`,
`00-references/`, `05-meta-and-planning/` (índice, auditorías, `SURVEY_MODERN_UNTRIED.md`, crucigrama, grid
maestro) de: Lee–Yang, Lieb–Sokal, Newman, GKS, FKG, Griffiths, ferromagnet, stable polynomial, stability
preserv, hyperbolic polynomial, Gårding, Borcea, Laguerre–Pólya, multiplier sequence, Pólya frequency, PF_,
PF₂, PF∞, total(ly) positiv, variation diminish, Schoenberg, Karlin, log-concav, Prékopa, Brascamp, de Bruijn,
heat flow, infinitely divisible, Lévy–Khintchine, Hermite–Biehler, Jensen polynomial, interlac, Turán.
Resultado: 661 archivos .md/.tex con al menos una coincidencia. Concentración: fase 102 (39), Paper 47 (37,
casi todo en copias `main_pre_*`), 159 (33), 60 (24), 193 (19), 186 (19), 162 (18), 160 (18), 106 (18), 116 (17),
103 (16), 114 (15), 211 (14), 212 (14), Paper 48 (12), índice (10), fase 33 (10). Advertencia: el patrón
«rding» de Gårding coincide con «regarding»; las coincidencias de las fases 114/116 por ese término son
falsos positivos (comprobado). Las coincidencias auténticas de Gårding están en 195 INV_M_001, 201
FAMILIES_A_001, 204 TRACT_D, 106_25, 54 y el índice.

**Abiertos en primaria (36).** Obligatorios (9): README, OBJECT_SPEC, LEDGER, BRIEF_CONSTRUCTOR, REVIEW_003,
REVIEW_004, ROUND_004_E, ROUND_003_8 de esta carpeta; `phase-211/STATEMENT_001.md`. Del tramo (27):
`phase-70-lee-yang-dbn/README.md`, `E70_2_RESULTS.md`; `phase-11-hyperbolicity-total-positivity/README.md`;
`phase-194-invention/INV_F_001`, `INV_A_001`, `INV_I_001`, `AUDIT_194.md`; `phase-65-signature-continuity/README.md`,
`M3`, `D7`, `D10`; `phase-137/R137_005_ROUND3.md` §1; `phase-159/G2_B8_R1.md`, `G2_B8_R5.md` (y R3/R4 por grep);
`phase-104/104_21`, `104_83` §2; `phase-60-discriminant/H1_PROOF.md`; `phase-155/R155_046` (tabla N3);
`phase-211/POWER_FOUR_TURAN_084.md`; `04-papers/47-row-d-dual-certificates/main.tex` (rem:PF2, prop:spec (6),
pasajes de inercia y entrelazado); `phase-195/INV_M_001`; `phase-193/CA_J_002`; `phase-201/FAMILIES_A_001`,
`FAMILIES_B_001` (por secciones); `phase-200/SPEC_SIGN_OBJECT_011` (por secciones);
`phase-116/previous-phase-114/114_d_99`; `phase-162/R162_1602`; `phase-197/BARRIER_W_001`;
`phase-168/R168_203`; `phase-102/120_TOTAL_POSITIVITY_AND_LI_SEQUENCE_AUDIT.md`; índice `03_PHASES_000-099`,
`04_PHASES_100-189`, `AUDIT_A.md` (filas A14a), `06` (fila 215), grid y crucigrama (sólo líneas por grep).

**No abiertos en primaria.** Fases 8 y 33 (flujo del calor / constante de de Bruijn–Newman: sólo vía índice
N6, ES-15, NG-B5, G8E); fase 28 (log-concavidad en σ, vía NG-D1/D2); 106_98–120 (flujo del calor de la forma
primo–Gamma, vía grid G3E); 103_15–42 (log-concavidad de la medida theta, vía grid G1F); E70_10–12 (vía
`ROUND_003_8.md`, que los abrió); 211 POWER_RECIPROCAL_* (vía las reglas del proyecto y la memoria de selecciones);
186 (coincidencias PF_ y Lévy–Khintchine); 154 (lecturas bibliográficas); 160 (encuestas); Papers 46 y 48;
`SURVEY_MODERN_UNTRIED.md` (sólo grep); `00-references/` (sólo grep; preprints sin abrir).

## 2. Inventario

Columna «actúa sobre»: objeto al que se aplica la regla de cierre o la propiedad.

| # | Archivo y sección | Objeto construido | Etiqueta declarada | Actúa sobre | Dónde y por qué se detuvo |
|---|---|---|---|---|---|
| 1 | `phase-70-lee-yang-dbn` README, E70_1–2 | flujo del calor sobre el núcleo de la función completada; monotonía de la positividad de Nevanlinna en el parámetro | NUMÉRICO; índice P70: CIRCULAR | la función entera completada y su derivada logarítmica (ceros) | usa una equivalencia externa; la monotonía va en la dirección ya conocida; reduce a positividad de Cauchy–Weil (E70_3–4) |
| 2 | `phase-70` E70_10–12 (vía ROUND_003_8) | factorización de Riccati δV + V² = Z⁻¹δ²Z en el álgebra de semigrupo | PROVED como identidad; sin signo | serie de Dirichlet como operador (Z, V = Z⁻¹δZ) | «enteramente del lado de Euler»; el cuadrado hermítico produce V*V con peine de razones de signo positivo; con Z_c = Σd_c(n)e_n la identidad vale para cΛ |
| 3 | `phase-11` README, M11.2–M11.5 | polinomios de Jensen, entrelazado, preservadores de Borcea–Brändén, MSS | NO-GO; ceguera aritmética PROVED/ARGUED | coeficientes de Taylor de la función entera (clase de Laguerre–Pólya) | usa una equivalencia externa; el preservador (derivada) conserva la clase para toda función (control cos t); la hiperbolicidad equivale a PSD de formas de Hermite |
| 4 | índice N6, ES-15, NG-B5, G8E (fases 8, 33, Paper 13) | flujo del calor, identidad de Lyapunov | NO-GO / DEAD | la función entera completada | usa una equivalencia externa; la monotonía no fija el parámetro terminal; la identidad de Lyapunov vale para toda configuración simétrica (ceguera) |
| 5 | grid G3E (106_98–120) | flujo del calor de la forma primo–Gamma | DEAD | la forma | sin signo uniforme (orden del calor, no uniformidad); no abierto en primaria |
| 6 | grid G1F (103_15–42) | log-concavidad de la medida theta | DEAD [F3] | una medida (theta) | núcleos positivos genéricos con ceros fuera del eje: la propiedad no separa |
| 7 | `phase-102/120` | positividad total / PF / log-concavidad de la sucesión de Li | auditoría, sin cierre | coeficientes de la derivada logarítmica transformada | usa una equivalencia externa; se queda en reformulación |
| 8 | `104_21` | ley aritmética compuesta de Poisson sobre exponentes; prueba PF₂, TP, monotonía completa | NO-GO (PROVED con menor racional) | una medida de probabilidad producto sobre primos (independencia = cierre bajo producto) | el núcleo en la red de exponentes falla PF₂ por un menor de dos primos; el cociclo completado falla monotonía completa |
| 9 | `104_83` §2; AUDIT_A A14a-1/2; P47 rem:PF2 | orden de Pólya del núcleo Φ; PF₂ de K(\|·\|) | A14a-1 NO-GO (CITED, PF₅ falla); A14a-2 OPEN (PF₄); rem:PF2 PROVED | núcleo de de Bruijn–Newman Φ; núcleo arquimediano K de la forma | Φ no es PF∞ (Schoenberg); K es completamente monótono ⟹ log-convexo ⟹ no PF₂; P47 deja OPEN si la densidad de transición del semigrupo C₀ + Lév es PF₂ |
| 10 | `R155_046` N3 | método nodal / Karlin | PROVED (mitad del núcleo); semigrupo t ≥ 1 HEURÍSTICO | núcleo K y semigrupo asociado | K no PF₂; ruta de oscilación cerrada para el núcleo |
| 11 | `R162_1602` K1–K3 | resolvente y semigrupo corto de A_T; identidad de Courant no local | NO-GO PROVED (K2 PARTIAL) | operador de la forma a_T (resolvente) | ninguna resolvente ni semigrupo corto es TP₂; el obstáculo es la estructura de saltos, no el peine; Λ∗1 = log no restaura TP₂ |
| 12 | `114_d_99` | Picone matricial; positividad total de los saltos | auditoría, NO-GO de hipótesis | núcleos de salto de la forma (traslación por primo, densidad Gamma) | menor 2×2 negativo en la traslación por primo; densidad Gamma log-convexa; el mayorante de rango dos equivale a la positividad primitiva (circular) |
| 13 | `ROUND_004_D` Lema C (R4-e) | 𝖡 como núcleo | PROVED | la función 𝖡 de un perfil | 𝖡 no es totalmente positiva, ni de Pólya, ni transformada de Laplace en (0,∞) |
| 14 | `211/POWER_FOUR_TURAN_084` (+082, 083, 085, 090, 097) | criterio de Pfaffianos de cuatro nodos, desigualdades de tipo Turán | PROVED como criterio; aplicación exterior; órdenes superiores abiertos | núcleo de la escalera de potencias | orden finito a orden finito; falsificador de herencia (las propiedades escalares con RS = x no bastan); sin inducción en el orden |
| 15 | `phase-159/G2_B8_R1–R5` | factores de Euler como objetos localmente estables (Lee–Yang en x = p^{−s}); reparto de Lévy–Khintchine del lugar arquimediano entre primos; Teorema D (minimax), L″ | PROVED (L″ verificado a máquina, sin intervalos); índice G4A: DEAD | **formas locales q_p de a_T sobre P_T**, combinadas por suma; factores de Euler individuales | no existe certificado local para T > 0.5925: la positividad es interferencia de signo entre primos dentro de una autocorrelación; operaciones factor a factor no la ven. Teorema S (toro de Satake) usa una equivalencia externa en su punto (ii)–(iii) |
| 16 | `phase-195/INV_M_001` M1–M2 | símbolo polarizado multiafín por bloques de primos de 𝔸 (S-suave); estabilidad real, conos de Gårding, familias entrelazadas | NO-GO PROVED | **la forma 𝔸_M / 𝖡 en variables por primo** | p_𝖡 no es real estable (testigo explícito); Gårding = reformulación PSD; MSS con cuantificador equivocado. Sobrevive a cΛ con c cerca de 1 y a a_P (pantalla §6) |
| 17 | `phase-193/CA_J_002` 1.3, 2.1–2.3 | GKS/Griffiths, Ginibre, GHS, FK sobre 𝔸_M; FKG en el retículo de divisores | NO-GO PROVED | **la matriz 𝔸_M** como hamiltoniano o covarianza | frustración: ciclo con aristas + aditivas y una arista · negativa (𝔸_{m,2m} < 0); FKG: los tests de Euler son la clase de igualdad |
| 18 | `phase-201/FAMILIES_A_001` A1, `FAMILIES_B_001` F2–F3 | polinomios de Lorentz / log-concavidad; desigualdades de correlación; Lee–Yang–Newman | NON-VIRGIN; NO-GO por cita | sucesiones (Λ(n)/√n, c_N); medidas de espín | log-concavidad de una sucesión de pesos es condición de cono; correlaciones muertas por frustración; Lee–Yang requiere una medida cuya transformada sea la función completada (usa una equivalencia externa) |
| 19 | `phase-200/SPEC_SIGN_OBJECT_011` C8 | inventario de conteos nodales (Sturm–Hurwitz, Pólya frecuencia) | NO-GO de clase ARGUED con dos lemas PROVED | núcleos de traslación; conteos nodales | PF falla en PF₂; conteos genéricos en el peine |
| 20 | `phase-194/INV_A_001` | estructura de Lévy aritmética; forma amortiguada 𝔞^{(ε)} (subordinación de Cauchy); conjeturas Θ, Θ⁺ | Θ⁺ FALSO PROVED; Θ REF-D (AUDIT_194) | **la forma amortiguada** como familia en ε; medida de Lévy de la serie | Θ⁺ falso: el coeficiente c_F(log n) tiene signo; Θ es positividad de la extensión de Poisson/Herglotz (usa una equivalencia externa vía la medida espectral); la ventana no se conserva |
| 21 | `phase-194/INV_F_001` F0–F3 | transferencia de conos por f ↦ −f′/f | PROVED (F1, F2, F3); OPEN residuo no cónico | la serie y su derivada logarítmica | ver §4 |
| 22 | `phase-194/INV_I_001` | intersección de órbitas cΛ con integralidad de coeficientes | PROVED | coeficientes b_n de f_a | {c : cΛ ∈ coeficientes enteros} = ℕ; {c : cΛ ∈ {0,1}} = {1} |
| 23 | `phase-60/H1_PROOF` | Perron–Frobenius para la forma localizada A_λ | PROVED a nivel operador (salvo cabo de rango finito); índice P60-1 PARTIAL | **la forma A_λ** (−V mejora positividad porque Λ ≥ 0) | da simplicidad y paridad del fondo, no signo; el mecanismo es Λ(n) ≥ 0, conservado por cΛ (ARGUED aquí) |
| 24 | `phase-65` D0–D12, M3, D6, D7, D10; `R137_005` §1 | determinante graduado por índice, topología τ_κ, cono de índice ≤ κ cerrado bajo límites de Schur (shorting); κ(A_P) = 0 para P finito | DEAD en D8.5; R137_005: cadena REFUTADA (bifurcación: la cota y la identificación viven en objetos distintos) | **signatura de núcleos de sistemas canónicos** asociados al peine truncado en P, inducción en P | usa una equivalencia externa (continuidad de signatura ⟺ el objetivo, en sus propios términos); la cerradura de índice 0 es PROVED pero la convergencia de la renormalización es el muro; κ(A_P) = 0 sale de Λ ≥ 0, que cΛ conserva (ARGUED aquí); Davenport–Heilbronn cae por pesos con signo (D10) |
| 25 | P47 thm:parityschur, prop:polarcap, inertia passages; `ROUND_004_E` (R4-f) | n₋(W_T) = n₋(a_T\|P_T) + n₋(𝔊_T); bloque polar con signatura (1,1); aritmética de inercia, Haynsworth, entrelazado | PROVED; NO-GO de clase (R4-f) | **signatura de la forma a_T y de su borde polar** | índices constantes para \|c − 1\| < λ_A(T)/Σ\|v_n\|: un conteo no distingue c = 1; P47 muestra que la aritmética de inercia vale tal cual para formas con cuartetos añadidos |
| 26 | `phase-197/BARRIER_W_001` W1–W3 | monotonía de n₋ en T (extensión por cero), homotopía de peines, flujo espectral, codimensión | PROVED (W3 ARGUED a nivel de formas) | **signatura de a_T, inducción en la ventana** y en el peine | toda invariante de la clase 𝒮 (extensión por cero, concavidad, continuidad, paridad, resolvente compacta) vale para a_P, truncaciones, O_4 = cΛ, O_6 y Beurling; el único dato que lee Λ es el apareamiento de Hellmann–Feynman con el minimizador |
| 27 | `R165_201` (vía grid G7A) | entrelazado crítico ⟹ cuarteto fuera del cono | DEAD, refutado | ceros de funciones modelo | usa una equivalencia externa; refutado por contraejemplo sin–cos |
| 28 | `R168_203` | desigualdad de Laguerre local | OPEN, respuesta NEGATIVA | la función entera completada cerca de un cuarteto | usa una equivalencia externa; condiciones lógicamente independientes |

## 3. Respuesta precisa

**¿Hay mecanismo de cierre aplicado a la forma a_T o a su signatura, con inducción en primos o en la ventana?**
Sí, varios, y todos se detuvieron:

- Inducción en la ventana, sobre la signatura de a_T: BARRIER_W_001 (W1: n₋ no decrece en T; W2: homotopía de
  peines; W3: codimensión). Es la regla de cierre «extensión por cero» más concavidad. NO-GO: las cinco
  propiedades estructurales valen para cΛ, a_P y sistemas de Beurling.
- Inducción en primos, sobre una signatura: fase 65 (cono de índice ≤ κ cerrado bajo shorting de Schur y
  bajo límites; κ(A_P) = 0 para P finito). Actúa sobre núcleos de un sistema canónico, no sobre a_T
  directamente; la cadena quedó REFUTADA en R137_005 y usa una equivalencia externa.
- Cierre factor a factor, sobre formas locales de a_T: G2_B8 (Lévy–Khintchine, estabilidad local, Pólya–Schur).
  La regla combina por suma formas locales ≥ 0, no por producto; falla para T > 0.5925 porque el signo es
  interferencia entre primos.
- Estabilidad real / Gårding / entrelazado sobre el símbolo multiafín por primos de 𝔸: INV_M_001, falso.
- Correlaciones ferromagnéticas sobre 𝔸_M: CA_J_002, frustración.
- Positividad total / Karlin sobre el núcleo de la forma, su resolvente o 𝖡: P47 rem:PF2, R155_046, R162_1602,
  114_d_99, ROUND_004_D. Falla ya en orden dos. Queda OPEN en P47 sólo si la densidad de transición del
  semigrupo C₀ + Lév es PF₂.
- Perron–Frobenius sobre la forma: H1_PROOF, da simplicidad y paridad, no signo.
- Aritmética de inercia: P47 thm:parityschur, ROUND_004_E. Es constante cerca de c = 1.

**¿Alguno se rompe para c = 2 por el factor arquimediano fijo?** No se encontró ninguno. Ninguna fuente del
tramo trata c = 2 como falsificador de un mecanismo de cierre. c = 2 aparece sólo en INV_I_001 (la
integralidad de coeficientes admite exactamente c ∈ ℕ, así que un mecanismo que sólo use producto de Euler e
integralidad sobrevive a c = 2) y como control NUMÉRICO en REVIEW_001_ABD y ROUND_003_2. En las fuentes, los
mecanismos que leen el peine lo hacen por Λ ≥ 0 (fase 65, H1_PROOF, G2_B8) o por clases cerradas que
contienen cΛ (BARRIER_W_001, INV_M_001 §6, R4-f). Que el factor arquimediano quede fijo mientras el peine
escala aparece como hecho en INV_F_001 F2 y en P47 lem:shape-scale, pero nunca como la línea donde un
mecanismo de cierre se rompe.

## 4. Alcance del muro ∂log (INV_F_001; OBJECT_SPEC O10)

Hipótesis exacta del Teorema F2: premisas de la forma «log ζ ∈ K» o «−ζ′/ζ ∈ K′» en Re s > 1, con K, K′ conos
(cerrados bajo multiplicación por c > 0), junto con identidades genéricas en el peine. La conclusión es que
todas esas premisas valen para ζ^c, cuyo peine es cΛ.

**Alcanzadas por el muro:**
- divisibilidad infinita y Lévy–Khintchine de la serie (C2, C5, C10; INV_A_001 §0, Prop. 4.1);
- positividad de coeficientes de −f′/f;
- Bochner en t de φ_σ;
- log-concavidad o log-convexidad usada como signo de (log f)″ (C9, C11), porque es condición de cono sobre log f;
- toda «cierre bajo producto» de factores de Euler cuya conclusión sea una afirmación cónica sobre log ζ (el
  producto de factores ID es ID; esa es exactamente la regla que el muro declara ciega a c);
- la medida compuesta de Poisson de 104_21, cuando se lee como propiedad de log de su función generadora;
- el cono de Pick / Laguerre–Pólya de la función completada (C6–C8). Este cruza ∂log, pero sólo se verifica en
  σ > 1 y su transporte a la línea es REF-D (usa una equivalencia externa).

**No alcanzadas por el muro (formalmente fuera de su hipótesis):**
- Propiedades de signatura o de positividad de la forma a_T, de 𝔸_M, de 𝖡 o del núcleo de la escalera.
  a_T^{(cΛ)} = Arch − cΠ no es c·a_T, porque el término arquimediano no escala. Una afirmación sobre su
  signatura no es una premisa cónica sobre log ζ. Esto incluye la signatura de Lorentz por sector de paridad,
  los conos de índice ≤ κ (fase 65), la positividad total de K, 𝖡 o de la resolvente, la estabilidad real del
  símbolo por bloques, GKS sobre 𝔸_M y Perron–Frobenius sobre A_λ.
  Pero todas estas fueron cerradas por otros motivos (§2 filas 9–17, 23–26), y BARRIER_W_001 junto con R4-f
  cubren las invariantes de índice definibles en la clase 𝒮 o constantes cerca de c = 1.
- Condiciones de integralidad: el conjunto de coeficientes enteros no es un cono (INV_I_001: su intersección
  con la órbita es ℕ, no ℝ₊). No es premisa cónica, pero no separa c = 2.
- Medidas de Lee–Yang de espines (Newman, Lieb–Sokal) definidas a partir de la forma y no de log ζ. No están
  alcanzadas por F2, pero en el corpus sólo aparecen como cita (201 F3) o muertas por frustración (CA_J_002).
- La conclusión «toda positividad que cruza ∂log es ID o Pick» está etiquetada ARGUED en P47 prop:spec (6)
  más allá de la lista clasificada. La lista está PROVED en INV_F_001.

Lectura (ARGUED): el muro bloquea los mecanismos de cierre que operan sobre la serie o su logaritmo. No bloquea
por sí solo los que operan sobre la forma con el factor arquimediano fijo. Esos están cerrados en el corpus
por falsificadores propios: orden PF, frustración, no estabilidad, invariantes de clase 𝒮 y constancia de
inercia cerca de c = 1.

## 5. Lo no encontrado (sin afirmar novedad)

1. Un mecanismo de cierre bajo **producto** de factores de Euler (no bajo suma de formas locales, como G2_B8)
   aplicado a la **signatura** de a_T, con inducción en primos y el factor arquimediano tratado como fijo.
2. Cualquier mecanismo del tramo cuya ruptura se haya comprobado o buscado en c = 2 (o en c entero ≥ 2) por el
   factor arquimediano fijo.
3. Preservadores de estabilidad de tipo Borcea–Brändén aplicados al símbolo s_T o a la forma a_T. Sólo aparecen
   sobre la función completada (fase 11) y sobre el símbolo por bloques de 𝔸 (INV_M_001).
4. Medidas con propiedad de Lee–Yang construidas a partir de la forma, y el cierre de Newman o Lieb–Sokal bajo
   acoplamiento ferromagnético aplicado a ellas.
5. Sucesiones multiplicadoras (Pólya–Schur) actuando sobre los pesos Λ(n) o sobre los coeficientes del peine
   como operación de cierre. Pólya–Schur sólo aparece factor a factor en G2_B8.
6. Prékopa–Leindler o Brascamp–Lieb aplicados a la forma. Sólo hay menciones en listas (201, anexo 193).
7. Polinomios hiperbólicos de Gårding en el parámetro T o en el peso para det de matrices de ventana. Gårding
   sólo aparece como reformulación PSD en INV_M_001 §3.
8. Positividad total de la densidad de transición del semigrupo C₀ + Lév. Está OPEN y declarada así en P47
   rem:PF2; no se encontró intento.
9. PF₄ y PF₃ del núcleo Φ: OPEN (A14a-2), sin intento en el corpus.
10. Correlaciones de tipo GKS/FKG cerradas bajo producto de medidas por primo, aplicadas a una medida construida
    desde a_T y no desde 𝔸_M. CA_J_002 trata 𝔸_M en sitios enteros; FKG sólo en el retículo de divisores.

La ausencia de coincidencias textuales no prueba que estas ideas sean nuevas ni que sirvan.
