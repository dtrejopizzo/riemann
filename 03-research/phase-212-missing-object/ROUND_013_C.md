# Ronda 13, C — mapa de operaciones de combinación entre objetos con signo y objetos que ven el peso

Notación del brief común. a_T(F) = Arch(F) − Σ_n v_n c_F(log n) sobre P_T, v_n = 2Λ(n)/√n. Para un peso real
a = (a_n) se escribe a_T^a la forma con v_n = 2a_n/√n, A(ξ) = Σ a_n n^{−1/2}n^{iξ}, A_M el multiplicador de
R161_001, g_F = c_F ∗ c_F. Controles: 𝒞 = {2Λ, Λ con una potencia de primo borrada, peso de tipo Beurling}.

**Resultado de selección.** No se construyó una candidata con identidad completa y signo global.
Las operaciones examinadas tienen antecedentes o dejan una obligación de signo sin resolver.
El Lema T excluye transferencia sólo bajo TODAS sus hipótesis, incluida la no negatividad de la
contribución adicional en el control. No prueba imposibilidad por la mera supervivencia del signo
auxiliar. La paridad de los cuadrados canónicos de (PC) tampoco se extiende a todos los cuadrados
mixtos; véase T5. Las listas siguientes son un inventario de selecciones, no una clasificación
exhaustiva de las fuentes posibles de signo.

Lectura en primaria para este memo: RULES_AVOID §§Q–V; ROUND_007_C completo; ROUND_009_G3; REVIEW_009;
ROUND_010_A; ROUND_011_A; ROUND_012_A; ANNEX_SONIN_READING §§4–6; R161_002 §§0–2 y §8 (enunciado del Teor. 8.1).
ROUND_009_G1, ROUND_009_G2 y ANNEX_LITERATURE_CONCENTRATION: a través de REVIEW_009 y RULES_AVOID S, T
(lectura indirecta). Índice de rutas, grilla y crucigrama: a través de las citas de esos memos y anexos, que
reproducen las entradas pertinentes (lectura indirecta; no se releyó el índice entero).

## 0. Filtro de cuatro puntos (del encargo en su conjunto)

1. **Antecedente más cercano.** ROUND_007_C §3: a_T = αQ_T + R_T, con Q_T el canal cociente (≥ 0) y R_T el resto,
   que es la combinación «suma» de un objeto S con un objeto W. R161_002 §2 (OR): el apareamiento orientado. ROUND_012_A
   Prop. B: el certificado de Lyapunov Re⟨H_TF, M_TF⟩. ROUND_009_G3 §4: flujo con historia y funcional convexo, los dos
   sin objeto.
2. **Lo nuevo.** No es un objeto. Es (i) la tabla de operaciones de §2 y (ii) el Lema T de §3, que dice cuándo una
   operación de combinación puede, en principio, discriminar los controles.
3. **Por qué evitaría la dificultad.** No la evita. Localiza la dificultad: la operación no es el lugar del signo.
4. **Enlace global.** Ninguno nuevo. (OR) es un enlace ya registrado, sin signo demostrado.
   No se deduce del Lema T que toda candidata deba ser impar en A_M ni adoptar ese enlace.

## 1. Las dos listas, exactas

«Ciego» significa aquí: el enunciado de signo del objeto vale, sin cambios, para todo peso de 𝒞 (y para Λ).
«Ve el peso» significa: el valor del objeto cambia bajo cada control y alguna identidad en la que entra falla en un
término nombrado. «Sin signo» significa: hay F (o pesos) con los dos signos.

### Lista S (signo manifiesto, ciego)

| # | Objeto | Archivo, sección | Signo | Ceguera: qué y con qué estado |
|---|---|---|---|---|
| S1 | Cuadrado de Sonin Son_S | R183_018 Prop 3.1; PROOF_L_SHARP_D_001 Thm 2.1; R186_015 | ≥ 0 (cuadrado de una involución unitaria) | Vale para cΛ y para el borrado: D_001 Thm 4.1, Cor 4.2, PROVED. Para Beurling: ARGUED (ANNEX_SONIN_READING §4; F_S es unitaria para toda fase impar) |
| S2 | Canal cociente ∫\|F̂\|⁴\|A\|² | ROUND_007_C (1.1); R161_034 §§0–1 | ≥ 0 | ≥ 0 para todo peso real: PROVED (es \|·\|²) |
| S3 | Cuadrados de fuga de la fase 161: L^sc = ‖(I−P_+)C_log g‖²; paralelogramo ¼‖(U_N−V_N)f‖²; Toeplitz–Hankel ‖(1−P)SP‖² | R161_020 (0.2); R161_035; R161_045; RULES_AVOID R2 | ≥ 0; L^sc > 0 si F ≠ 0 | ROUND_012_A Lema A: positividad estricta para Λ, 2Λ y el borrado, PROVED; Beurling sin definir. TH: ≥ 0 para todo S, PROVED (trivial) |
| S4 | Cuadrado canónico de PC, ‖S_NA_M𝓕F‖² | R161_002 Teor. 1.1 | ≥ 0 | Par en A_M: PROVED. Ve A², no A |
| S5 | Discrepancias reticulares Δ^R (test integral, Euler–Maclaurin) | ROUND_011_A §1, Lemas 1–2 | sólo con φ_t monótona; ningún signo uniforme en F (Lema 1) | Sin Λ: PROVED (Lema 2) |
| S6 | Incertidumbre logarítmica (Arch como Beckner, constante C_0) | R160_C8_R1 Teor. 1, Cor. 2.4; ROUND_010_A Lema C (α) | ≥ 0 en la recta | Sin pesos: PROVED. En la ventana no es ≥ 0 más allá de T ≈ 0.60 (P47 cor:Tarch, CITED) |
| S7 | Resto de hipérbola h(k) = Σ_{dm=k, d≤M, m≤N}Λ(d) ≥ 0 | R161_002 §8; RULES_AVOID K5, K7 | ≥ 0 | ≥ 0 para todo peso ≥ 0, y por tanto para 2Λ y el borrado: PROVED (trivial) |

S7 entra en la tabla de H_{M,N} (lista W) como pieza con signo. Su signo es el de un peso no negativo, y por eso es
ciego a c = 2.

### Lista W (ve el peso, sin signo)

| # | Objeto | Archivo, sección | Sin signo | Ve el peso |
|---|---|---|---|---|
| W1 | Canal producto ∫\|F̂\|⁴ Re A² | ROUND_007_C (1.2)–(1.3), (2.1) | PROVED: un solo átomo da g_F(2log n) < 0 | Λ∗Λ = μ∗log² − Λ·log se rompe con el borrado: ARGUED en ROUND_007_C §3 |
| W2 | Conmutador de soporte ⟨g,[P,S]w⟩ y concomitante de borde | R161_057–065; R161_042–044; RULES_AVOID R1, K1 | CITED (expansión positiva retirada) | lineal en la corriente: CITED |
| W3 | Hipérbola H_{M,N} = L_MS_N − K_N y defecto δ_a(k) = Σ_{d\|k}a(d) − log k | R161_001 Teor. 3.1, 4.1 | δ_a cambia de signo según el control (log 2 en k = 2 con c = 2; −log 2 en k = 4 con el borrado de 4) | PROVED (ROUND_010_A afirmación 10) |
| W4 | Parte de primos de Sonin: C_p, K_s, κ_S | R183_018 Prop 4.1; ANNEX_SONIN_READING §4 | C_p indefinido, espectro ± de multiplicidad infinita: CITED | el fallo bajo cΛ vive en C_{ε_c}: CITED (D_001 Cor 4.2) |
| W5 | Puerto producto g y defecto G_+ + χG_− = ζW_ε | R161_015, R161_017 Teor. 2.1 | lineal en F | lineal en el peso: CITED |

**Observación (ARGUED, por la tabla).** Todos los objetos de W son lineales en el peso, salvo W1, que es
cuadrático y holomorfo (A², no |A|²). Todos los objetos de S son o bien libres de peso (S5, S6), o bien funciones
de |A|² o de normas de operadores lineales en el peso (S1–S4), o bien funciones de un peso positivo (S7).

## 2. Operaciones de combinación: tabla

Cada fila indica S-objeto, W-objeto, antecedente y motivo del fracaso. «Lema T» remite a §3.

| # | Operación | Antecedente (archivo, sección) | Estado | Motivo |
|---|---|---|---|---|
| O1 | Suma o combinación positiva αS + R | ROUND_007_C §3; J2; L3 (BARRIER_D2_001); identidad de Sonin (T1) | NO-GO de selección, repetición | El signo queda en el resto R = W − αS; S es ≥ 0 bajo los controles y el fallo vive en R (R3-i automático). Lema T con Φ(s,w) = αs + w y hipótesis «w ≥ −αs», que es el objetivo |
| O2 | Apareamiento orientado ⟨x, W x⟩ con x un vector S | R161_002 §2 (OR) = ⟨A_MG, S_N^*S_NG⟩; SP-161/K7; T3 (pesos w_N con signo, cerrado en L1, R4-a) | NO-GO / reformulación | En la recta equivale al signo del multiplicador (R161_002 §2). En la ventana es SP-161; la rama w_N ≥ 0 muere (Teor. 8.1) y la rama con signo queda cerrada por R4-a |
| O3 | Cauchy–Schwarz / defecto de Gram | R161_035 (paralelogramo); R161_045 y R2 (PS²P − (PSP)² = \|(1−P)SP\|²); fase 122 | repetición | El defecto de Gram es ≥ 0 para todo peso (S3), y por tanto ciego. La identidad que lo une al defecto de PC no existe (K1) |
| O4 | Complemento de Schur en un bloque [[S, W],[W*, S′]] | J3; L5; D17 (suelo de Schur); W11′ (R184_015 Teor. 2) | NO-GO con clase | Positividad del bloque ⟺ S′ ⪰ W*S^{−1}W: cota de norma de W relativa a S (W11′, B2), o raíz de la forma (J3) |
| O5 | Conjugación U*WU con U un factor S (Sonin) | R186_015; ANNEX_SONIN_READING §4; L6 (inercia) | repetición | La conjugación unitaria es la identidad de Sonin misma, que vale para toda fase impar. La congruencia conserva la inercia (Sylvester): clase 6 de G3 |
| O6 | Conmutador i[H, A] (Mourre, virial) | J5 (clase 18 de G3); R161_057–065; ROUND_012_A Prop. B; CS0_COMMUTE_001 | repetición | ⟨F, i[H,A]F⟩ = 2 Im⟨HF, AF⟩ es el formato Lyapunov Re⟨HF, MF⟩ con M = −2iA. Por Prop. B, sin una A de fórmula propia equivale a ker H = {0}. Con A = dilatación, el borde de la ventana deja un resto sin cota inferior (J5) |
| O7 | Monotonía en un flujo (dS/dτ = W) | clase 16 de G3 (D17, B10 Danskin en c); R161_015 Teor. 3.1; R161_029 (monotonía FALSA); Q2/R7-b; G3 candidata A | NO-GO con paso uniforme; con historia, sin objeto (§4.1) | La derivada tiene que tener signo, y W no lo tiene. Los flujos naturales (T, c) dan la flecha equivocada o son genéricos en c |
| O8 | Dualidad de Legendre / Fenchel–Young | Q1 (R7-a, contacto ≤ potencial); fase 154 (Teor. Z: certificado dual = fórmula explícita) | NO-GO con clase | ⟨x, W⟩ ≤ S(x) + S*(W) acota contactos por arriba con una pieza ≥ 0: muere antes de T ≈ 0.60 (cor:Tarch) |
| O9 | Interlazado / min-max (n₋(W) ≤ rango de un defecto S) | L6 (R4-f); P47 Teor. P (n₋ ≤ 5/7/8); W-lin | repetición | Los índices son constantes cerca de c = 1; un conteo no ve el margen (P6 de G3) |
| O10 | Producto tensorial / de Schur / segunda cuantización | R7-c §§1–2 (Λ∗Λ, grado 2); K2; J2; N3 (R5-c); N5 (R5-e) | repetición | El producto de Schur S∘W necesita W ⪰ 0. La exponencial (Schoenberg / Fock) de una forma es positiva ⟺ la forma es condicionalmente negativa: reformulación. El grado 2 en el peso cae en K2/J2 |
| O11 | Posición relativa de dos subespacios (operador ángulo) | ANNEX_SONIN_READING §4 (construcción de Halmos); K1; R2 | repetición | La teoría de dos subespacios es la que produce Son_S y los cuadrados de fuga: sin\|ángulo\|² = ‖(1−P)SP‖², ciego |
| O12 | Espacio de Kreĭn: S como simetría fundamental, W J-autoadjunto | L6; N1 (R5-a); M1 | repetición | Conteo de Pontryagin, constante cerca de c = 1 |
| O13 | Contracción en métrica proyectiva de Hilbert (Birkhoff) | G3 candidata A | sin objeto | Falta un mapa T → T′ que preserve el cono; la inclusión P_T ⊂ P_T′ va en la dirección equivocada (G3 afirmación 7) |
| O14 | Funcional convexo con hessiano a_T | G3 candidata B; N5 (R5-e) | sin objeto (§4.2) | Falta la identificación de la Hessiana positiva con la forma; su positividad auxiliar universal no es una exclusión (Lema K corregido) |

Cotejos: ARGUED, por lectura de las entradas citadas; no exhaustivos.

## 3. La razón común

**Clase 𝔐 (declarada).** Certificados de la forma a_T^a(F) = Φ(S^a(F), W^a(F)) + (términos que se anulan
idénticamente para a = Λ), en los que la desigualdad Φ(s, w) ≥ 0 se deduce sólo de dos cosas:
- (a) s ≥ 0, que es el enunciado de signo del objeto S;
- (b) un conjunto ℛ de relaciones (identidades o desigualdades) entre s, w y los datos libres de peso.

**Lema T (PROVED, con hipótesis de transferencia precisadas).** Sea 𝒜 el conjunto de pesos para los que
valen (a), (b), la descomposición y la no negatividad de la contribución conjunta de los términos
adicionales que se anulan para a = Λ. No se exige signo individual de esos términos. Si 𝒜 contiene un
peso a con λ_A(T; a) < 0 para algún T, entonces ningún certificado de 𝔐 con esos (S, W, ℛ) prueba a_T^Λ ≥ 0 en P_T
para todo T.

*Prueba.* Para a ∈ 𝒜, (a) y (b) dan Φ ≥ 0; la contribución adicional también es no negativa por hipótesis.
La descomposición da a_T^a ≥ 0 en P_T para todo T, lo que contradice λ_A(T; a) < 0. ∎

**Precisión de alcance.** La descomposición sola no transporta la nulidad de los términos adicionales
desde Λ a otro peso. Por ejemplo q_w(x)=(2−w)|x|²=|x|²+(1−w)|x|² tiene segundo término nulo en w=1,
pero es negativa para w>2 y x≠0. Tampoco se exige que una expresión auxiliar positiva pierda su signo:
puede fallar únicamente su identificación con la forma objetivo. Estas precisiones corrigen la lectura
literal anterior; no proporcionan una representación positiva de a_T.

Con la batería E (CITED: λ_A < 0 certificado para c > 1 en T = 1 y en ½log5, CERT_FALSIFIERS_001),
alguna hipótesis completa de transferencia debe fallar en cada control negativo. Sólo si sobreviven
la descomposición y los demás signos se fuerza un fallo de ℛ. Se tienen además los hechos siguientes.

- (T1) Si S es ciego (lista S), (a) vale en todo 𝒞. PROVED, por la columna de ceguera de §1.
- (T2) Una relación de ℛ que sea una desigualdad de signo sobre un peso no negativo (por ejemplo h(k) ≥ 0, o las
  leyes de probabilidad de ζ^c) vale para 2Λ. PROVED (trivial).
- (T3) Una relación que use sólo divisores, como Σ_{d|n}a(d) = log n, vale en Beurling (Lema A de R9-b, PROVED
  allí). Una relación libre de peso (Tate–Beckner, Poisson sobre ℤ) vale para 2Λ y el borrado (ROUND_010_A Lema C
  (α), (β), PROVED).
- (T4) Por tanto ℛ tiene que contener, como restricción efectivamente usada, la conjunción de Poisson sobre ℤ con
  Λ∗1 = log, que es la identidad (PC) de R161_001 (canal (γ)). Esto es PROVED dentro del inventario de relaciones de
  ROUND_010_A Lema C; la exhaustividad de ese inventario es ARGUED.
- (T5) **Paridad con clase precisada.** R161_002 Teor. 1.1 y Cor. 1.2 prueban invariancia bajo
  A_M→−A_M del cuadrado ||S_N A_M 𝓕F||² y de sus sumas o integrales no negativas con coeficientes
  independientes del signo. Esa información sola no determina la orientación de A_M. No cubre
  todos los cuadrados construidos usando (PC): si L es lineal en A_M, entonces

      ||u_0+L(A_M)F||²
        =||u_0||²+2Re⟨u_0,L(A_M)F⟩+||L(A_M)F||²

  contiene un término impar. No se deduce que una expresión candidata completa deba ser impar;
  puede tener componentes pares e impares. Sigue vigente ROUND_003_2 Lema 3 para la subclase afín
  cuyo cruce reproduce exactamente el peine. Una identidad específica para Λ con cruce distinto
  requiere construcción y prueba propias; no se revalida ninguna candidata por esta corrección.

**Enunciado común con alcance precisado.** El Lema T transfiere la no negatividad al control
sólo si sobreviven la descomposición, las relaciones empleadas y el signo conjunto de los términos
adicionales. No basta que sobreviva el signo del objeto auxiliar. La identificación puede fallar
únicamente en el control. La lista de objetos S/W no prueba que toda combinación quede en la
clase excluida ni que deba reducirse a (OR).

## 4. Los dos formatos sin objeto de ROUND_009_G3

### 4.1 Flujo con paso dependiente de la historia (S monótono, W derivada)

Intento de par explícito, con el flujo en T:
- 𝔖(T) := λ_min(Son_{S(T)}|P_T), con S(T) = {∞} ∪ {p ≤ e^{2T}};
- derivada: entre saltos, 𝔖 es no creciente por inclusión de dominios, para todo peso (ciego); en T = ½log p,
  el salto de 𝔖 viene de la entrada de p (es la parte W4).

El formato «entropía» exige una cantidad que no decrezca y cuyo valor inicial sea ≥ 0. Toda cantidad obtenida por
inclusión P_T ⊂ P_T′ decrece (G3 afirmación 7, PROVED trivial), y por tanto la flecha es la equivocada. Para
invertirla hace falta que el salto de W tenga signo en cada T = ½log p, y W4 es indefinido (CITED). La comparación
𝔖 frente a λ_A es Lemma H (iv) de R186_029: 1 − ρ* ≤ λ_A/λ_min(Son_S|P_T), que hereda el margen (CITED).
Conclusión: el par existe pero es repetición (R186_029, W-fam). ARGUED.

Con el flujo en c (a_T^{cΛ}, c ∈ [0,1]): d/dc = −comb (W, sin signo) y a_T^0 = Arch, que no es ≥ 0 en P_T más allá
de T ≈ 0.60. Es B10 / clase 16. Repetición.

La dependencia de la historia pedida por Q2 tendría que entrar como dato de fórmula propia en el paso. Ningún objeto
de S proporciona ese dato: todos son funciones del estado en T, sin memoria. ARGUED.

### 4.2 Funcional convexo con hessiano a_T (S convexo, W hessiano)

**Lema K (PROVED).** Sea Φ(F) = ∫ ψ(F̂(ξ)) dμ_a(ξ) o Φ(F) = log Σ_n w_n e^{⟨F, φ_n⟩}, con ψ convexa, μ_a ≥ 0 y
w_n ≥ 0 construidos a partir de un peso a. Entonces D²Φ(F_0) ⪰ 0 en todo punto base donde las expresiones y
sus derivadas estén definidas, para todo peso con μ_a ≥ 0 (respectivamente w ≥ 0). Esto incluye 2Λ sólo
si la construcción conserva allí esas hipótesis. El lema no excluye una identidad específica que
identifique esta Hessiana positiva con a_T para Λ y falle para un falsificador.

*Prueba.* En el primer caso, D²Φ(F_0)[H,H] = ∫ D²ψ(F̂_0)[Ĥ,Ĥ] dμ_a ≥ 0. En el segundo, el hessiano es la
covarianza de ⟨H, φ_n⟩ bajo la ley proporcional a w_ne^{⟨F_0,φ_n⟩}, que es ≥ 0. ∎

Aplicaciones:
- El canal cociente S2, visto como funcional cuártico F ↦ ∫|F̂|⁴|A|², es del primer tipo, con μ = |A|²dξ ≥ 0
  para todo peso. Su hessiano en 0 es nulo, y en otros puntos es ≥ 0 y ciego.
- El segundo tipo es la varianza N5 (R5-e).
- Si la convexidad se certifica por un supremo de afines indexado por factorizaciones, cada rama es lineal en el
  peso: G3 §4B, J2.

Las dos fuentes del Lema K dan Hessianas positivas bajo sus hipótesis, pero no se ha construido
su identificación con a_Λ. Esto es ausencia de objeto en la selección, no una exclusión universal.
En particular, que la Hessiana auxiliar siga positiva bajo un falsificador no impide que falle allí
la igualdad con la forma objetivo.

## 5. Candidatas

**No se obtuvo una candidata que pase la puerta.** No se afirma que O13, O14 y una rama impar
no lineal de O2 agoten las operaciones abiertas. La restricción a esas tres posibilidades dependía
de la generalización indebida de T5 y del uso de la ceguera auxiliar como exclusión.

Un bloque, Hessiana o cuadrado mixto explícito puede ser admisible si se demuestra su identidad
completa con a_Λ y su signo sobre el portador. No se exige que pierda positividad el objeto auxiliar
en c=2: puede fallar sólo la identidad. No se ha proporcionado aquí tal construcción.

Advertencia (PROVED, trivial). Si B(A_M) = f(A_M) con f ≥ 0, entonces ⟨A_MG, f(A_M)G⟩ = ∫ λ f(λ) dE_G(λ), cuyo signo
es el de A_M sobre el soporte de f. Toda Φ de esta forma es una reformulación (B3). Una B que no conmute con A_M cae
en el formato de Lyapunov de ROUND_012_A Prop. B.

## 6. Afirmaciones y etiquetas

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | Listas S y W con archivo, sección y estado de ceguera | CITED (columna por columna); la observación de §1 es ARGUED |
| 2 | S2 ≥ 0 y S7 ≥ 0 para todo peso real (respectivamente no negativo) | PROVED (trivial) |
| 3 | Tabla O1–O14: antecedentes y motivos | ARGUED (cotejo; no exhaustivo) |
| 4 | O6: el formato Mourre/virial es el formato Lyapunov con M = −2iA | PROVED (⟨F,i[H,A]F⟩ = 2 Im⟨HF,AF⟩ para F en el dominio) |
| 5 | Lema T | PROVED en la clase 𝔐 |
| 6 | (T2), (T3) | PROVED (T3 a partir del Lema A de R9-b y del Lema C (α), (β), CITED) |
| 7 | (T4): la restricción efectiva tiene que ser (PC) | PROVED dentro del inventario del Lema C; exhaustividad ARGUED |
| 8 | (T5): paridad del cuadrado canónico y sus sumas con coeficientes independientes del signo; no extensión universal a cuadrados mixtos | PROVED en la clase citada; alcance corregido |
| 9 | §4.1: el flujo en T da la flecha equivocada; el par con Son_{S(T)} es R186_029 | PROVED (inclusión) / CITED |
| 10 | Lema K | PROVED |
| 11 | Advertencia de §5 (f(A_M) conmutante ⇒ reformulación) | PROVED (trivial) |
| 12 | Candidata que pasa la puerta: ninguna | NO-GO de selección |
| 13 | Signo global de a_T | OPEN |

Para el revisor, hay que rederivar: el Lema T y su aplicación a la batería E; el Lema K (los dos casos); la
identidad de O6; y la afirmación (T4), es decir, que ninguna relación de ℛ fuera de (PC) falle a la vez en los tres
controles (ésta es la pieza más débil, porque depende de la exhaustividad ARGUED del Lema C de ROUND_010_A).
