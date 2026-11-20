# Ronda 10, A: covariancia aditiva como mecanismo del signo

Notación del brief común. a_T(F) = Arch(F) − Σ_n v_n c_F(log n) sobre P_T, v_n = 2Λ(n)/√n.
En coordenada logarítmica, τ_a F(t) = F(t+a), X = multiplicación por t, 𝓕 es la transformada aditiva
transportada y M = m(D).

**Pista examinada.** Ninguna identidad de tipo Sonin puede llevar el signo por ser unitaria y covariante por
escala, porque F_S = I·m_∞(D)e^{iφ_S(D)} tiene esas dos propiedades para toda fase (ANNEX_SONIN_READING §4). La
propiedad que sólo tiene la transformada verdadera es la covariancia aditiva: relación canónica de conmutación,
núcleo e^{2πixy} y Poisson sobre ℤ. Esa covariancia tendría que acoplarse con Σ_{d|n}Λ(d) = log n. El Lema A de
ROUND_009_G2 explica por qué: un paso que use sólo divisores es ciego a Beurling.

**Resultado.** El acoplamiento que pide la pista ya está escrito en el corpus. Es la identidad de anomalía
Müntz–Chebyshev (PC) de la fase 161, R161_001 Teor. 3.1. Junta en una misma línea tres cosas: la relación de
Tate–Beckner X + 𝓕X𝓕 = M (R160_C8_R1 Teor. 1 y Cor. 2.4), el defecto de Poisson E_N = S_N𝓕 − JS_N y la
hipérbola de divisores H = L_M S_N − K_N, que contiene a Λ∗1 = log. La fase 161 la recorrió entre R161_001 y
R161_081.

Ninguna de las tres direcciones del encargo pasa la puerta. Más abajo se registra el residuo exacto que queda abierto.

## 0. Cotejo en primaria

| Tema | Archivo y sección | Qué se construyó | Dónde se detuvo y por qué |
|---|---|---|---|
| Arch como incertidumbre logarítmica, con constante exacta C_0 = ψ(¼) − log π | `phase-160-row-d-infinite-T/R160_C8_R1.md`, Teor. 1 y Cor. 2.3–2.5 | a_T es el funcional de incertidumbre logarítmica de la involución de Tate–Fourier 𝔉_S. Su parte arquimediana es la desigualdad de Beckner con constante exacta C_0 (PROVED en clase densa, CITED Beckner). Para S finito la constante semilocal es κ_S = C_0 − Σ 2log p/(√p−1) | O-1, «Beckner de ventana para todo T», quedó OPEN y es una reformulación. Fila I-12: los multiplicadores de Tate sólo fijan una constante por la fórmula del producto (Teor. 3). Fila S-8: X + 𝔉X𝔉 es indefinida en L²(ℝ) |
| (i) Parte de contactos como conmutador de log\|x\| con la suma E f(x) = Σ f(nx) | `phase-161-row-d-sum-product-square/R161_001_MUNTZ_CHEBYSHEV_ANOMALY.md` §§1–6 | Identidad (PC), PROVED para M_0 y N finitos: S_N A_{M_0}𝓕 se expresa mediante {X, E_N}, L*E_N, JH y H𝓕. Aquí S_N es el operador de suma de Müntz, que en coordenada x es Σ n^{−1/2}f(nx), y la «covariancia aditiva» es 𝓕 con E_N. Teor. 4.1: con cΛ y con borrados aparece un defecto interior δ_a(k) = Σ_{d\|k}a(d) − log k en el primer k afectado; en Beurling falta el dato de Poisson entero | R161_002 §§0–1: el cuadrado canónico ‖S_N A_M 𝓕F‖² ve A², no A, y por tanto es ciego al signo. Falta «una orientación del defecto de borde de Poisson» |
| Derivada covariante [X, ·] del defecto de Poisson | R161_040; R161_041 §§0, 3, 6 | Poisson identifica las dos historias exteriores (040). La derivada de la diferencia E da la media U+V; la de la suma C = Z𝓕 + JZ da el chorro crítico U − V = ZM𝓕 − {X,C} (041 Teor. 3.1, PROVED) | Sólo E da un conmutador lineal que se anula; sólo C no tiene control de Poisson. Hace falta el apareamiento mixto comprimido E–C |
| Apareamiento mixto E–C (Green) | R161_042–044 | Identidad de Green exacta: deja la diferencia de primeros momentos orientados, que es una energía positiva de distancia al borde | El término C_N X f rompe los momentos de Tate. Su corrección tiene paridad opuesta y el apareamiento se anula (043). El término primitivo colisiona con el NO-GO horizontal (044). RULES_AVOID K1: «piezas residuales sin signo» |
| Cuadrado local de Toeplitz–Hankel | R161_045; RULES_AVOID R2 | Toeplitz–Hankel de rango uno | No globaliza (ensamblaje cerrado en la fase 122) |
| Ondas de borde del defecto de Poisson | `phase-163-integrality-defect/R163_154_RESCALED_POISSON_BOUNDARY_WAVES.md` l. 68–83 | Expansión reescalada de E_N^ren mediante Tate–Beckner | l. 83: el operador principal usa sólo el peine entero y la ecuación funcional, sin Λ∗1 = log ni el peso de un primo. Es el mismo para cualquier peso a. Falta acoplarlo a los saltos de Euler (R163_152) |
| Intercambio de factores en PC completo | `phase-170-.../R170_876` §0 | Simetría exacta de la hipérbola causal | No lo es del operador de primer contacto. La extracción causal intercambiada no existe porque PL_N^*P no es invertible (J3) |
| (ii) Operador diferencial que conmuta con el corte y con la transformada | `phase-186-toolbox/R186_003` filas 3–4; `R186_006` filas 1, 4, 9; `R186_007` §6; `phase-200-sign-object/SPEC_SIGN_OBJECT_011` (CS-0) | W_λ = −∂(λ²−x²)∂ + (2πλx)² conmuta con P_λ y con 𝓕 (PROVED). Se usó como herramienta espectral y de funciones de prueba (prolatos), y como candidato a conmutar con P^S | NO-GO PROVED para S = {∞,2}: ninguna función del número de Hermite semilocal sumada a −𝔰² conmuta con P^S (003 fila 4), y L + κX no conmuta nunca (006 fila 4). Nunca se usó como **cota operatorial que domine los restos**. Ese uso cae, sin embargo, en las clases de §1(b) |
| (iii) Oscilador o representación metapléctica combinados con la dilatación por enteros | R186_003 §5 (número N_S y ϖ(k) = πx² − ∂²/4π); R186_006 (W^{mp} con E g(u) = Σ g(2^k u)) | Se combinó el oscilador con la dilatación por 2: η_S = E, F_S = EF_∞E^{−1} | NO-GO de conmutación (006 fila 4). La «escalera» a, a* nunca se usó como factorización B*B de a_T. Esa factorización cae en BB* (J8; P1_BBSTAR_001) |
| Hipercontractividad y Bonami–Beckner | `phase-201-untried-families/FAMILIES_B_001.md` F10 | Inventario de la familia | Sin mecanismo para el peine |
| Teta exacta, sumación de Bernoulli, métricas no locales | 211 `POWER_HYPERBOLIC_MODEL_GRAM.md` §§12.6–12.7; 106_109 §2; memoria de las reglas del proyecto | Realización teta (Poisson modular) del Gram | Rechazadas en selección: falta un núcleo no local positivo o una identidad de Green con resto controlado |
| Meta-ledger | `phase-200-sign-object/LEDGER_L5_META.md` C1 (l. 20) y l. 91 | «Poisson-ℤ» figura como identidad lineal y genérica en el peine | thm:shape(A): sobrevive a cΛ y a los borrados |

Búsquedas sin hallazgo relevante (grep sobre 03-research y 05-meta): «canonical commutation», Eisenbud,
«time delay» (aparece sólo en sentido de fase), Lax–Phillips (fase 64, colligación adélica, otro objeto),
Segal–Bargmann (fase 4, otro uso) y co-Poisson (phase-209 LINK_011/016, Mellin–Gauss y rango denso). Una
búsqueda sin coincidencias textuales no prueba novedad conceptual.

**Respuestas puntuales.**
- (i) Sí. La identidad de Beckner con C_0 exacta está en R160_C8_R1. La parte de contactos como anomalía entre
  X, el operador de suma S_N y Poisson está en R161_001 (PC). La línea terminó en R161_002 (cuadrado ciego), en
  R161_042–044 (Green mixto sin signo) y en K7, que sigue abierto.
- (ii) Como mecanismo de conmutación, sí, y es NO-GO para S ≥ {∞,2}. Como desigualdad operatorial dominante, no
  hay memo. La clase cae de todos modos en B2, B8 y W11′ (§1(b)).
- (iii) Sí, para la dilatación por 2 (R186_006), en forma de conmutación. Es NO-GO.

## 1. Lema de canales (cierra el encargo en su forma general)

**Lema C (por dónde puede entrar la covariancia aditiva; ARGUED, con dos piezas PROVED).** En a_T la estructura
aditiva de ℝ_x sólo puede entrar por tres vías:

- (α) **La relación de Tate–Beckner X + 𝓕X𝓕 = M**, que es la versión integrada de la relación canónica de
  conmutación. Produce Arch y nada del peine. Es ciega a los tres controles (PROVED: no contiene pesos).
  Por Paper 47 cor:Tarch (CITED), toda pieza de este canal que acote los contactos por arriba muere antes de
  T ≈ 0.60.
- (β) **Poisson sobre ℤ para el peine entero sin pesos.** Es idéntica bajo cΛ y bajo el borrado de una potencia
  prima (PROVED trivial: la retícula ℤ y la familia {log n} no cambian, sólo los pesos). Sólo detecta Beurling
  (R163_154 l. 83, CITED).
- (γ) **El acoplamiento de (β) con Σ_{d|n}Λ(d) = log n.** Es la identidad (PC) de R161_001. Su Teor. 4.1 da el
  comportamiento correcto frente a los tres controles al nivel de la identidad.

Consecuencia: la conjunción de la pista con el Lema A de ROUND_009_G2 apunta exactamente a (γ), que ya está
escrita y recorrida. La parte ARGUED es la exhaustividad de la lista; lo que la sostiene es que a_T sólo es
covariante por dilataciones (es Toeplitz en t), y que la modulación e^{2πiyx} conmuta con P_T pero no deja
invariante la forma.

**Primer caso no trivial (contactos 2, 3, 4; T ∈ (log 2, ½log 5]); PROVED como lectura de R161_001 Teor. 4.1
con N, M_0 ≥ 4.** Los defectos interiores son:
- cΛ con c = 2: δ(2) = log 2 en k = 2.
- Borrado de 4: δ(4) = −log 2 en k = 4.
- Beurling: el defecto E_N cambia de operador, porque falta el peine entero.

Los tres son visibles en la identidad, pero el signo no lo es: R161_002.

## 2. Candidatas (filtro de cuatro puntos; ninguna pasa)

### (a) Factorización escalera / número: a_T + (término nombrado ≥ 0) = ⟨F, B*B F⟩, con B construido de X, ∂ y dilataciones enteras

1. *Antecedente:* RULES_AVOID J8 y P1_BBSTAR_001 (BB* NO-GO PROVED en la clase convolutiva y término a término);
   R161_002 §1 (el cuadrado canónico de PC); R186_003 §5 (número de Hermite semilocal).
2. *Nuevo:* B = Σ_n β_n n^{−1/2}τ_{log n}(X + i𝓕X𝓕) o variantes, con coeficientes β fijados por Poisson y por
   Λ∗1 = log.
3. *Por qué evitaría la dificultad:* no la evita, por dos razones.
   - Si β es lineal en Λ, B*B es cuadrático en el peine: es un sector «Λ∗Λ» sin término de compensación, la
     clase R3-b y K2 (varianza orientada, genérica).
   - Si B se toma de PC, el cuadrado es ‖S_N A𝓕F‖², que ve A² (R161_002). Que exista B con B*B = a_T|_{P_T}
     equivale a a_T ⪰ 0 (J8: REF-D).
4. *Conexión global:* ninguna sin un B explícito que no salga de factorizar la propia forma (J3).

**Ruptura bajo controles.** No aplica: no hay objeto. Para el cuadrado de PC, cΛ produce otro cuadrado ≥ 0, y la
ruptura no está en el resto. **Repetición:** R161_002, K2, J8.

### (b) Dominar los restos de Sonin con un operador diferencial de segundo orden que conmute con el corte y con la transformada

1. *Antecedente:* R186_003 y R186_006 (W_λ, NO-GO semilocal); ANNEX_SONIN_READING §§1, 5 (los restos K_s, C_p
   y κ_S, n₋(R) = ∞); Paper 47, Teor. P (fase 155: direcciones negativas en ≤ 8 modos prolatos).
2. *Nuevo:* la desigualdad −⟨g,K_s g⟩ − ⟨g,C_p g⟩ ≥ −Φ(W_λ) y Son + 2ε′𝔅 ≥ Φ(W_λ) en P_T, con Φ explícita.
3. *Por qué evitaría la dificultad:* no la evita.
   - El único W conocido conmuta con P_λ y con 𝓕_∞, no con F_S (R186_006 fila 4, PROVED). Para la forma
     completa (S = S(T)) no existe uno local.
   - Una Φ(W_λ) es un multiplicador en la base prolata. La desigualdad pedida es un certificado lineal en una
     base fija (W-lin) o una cota de norma o inercia del resto (W11′, R184_015 Teor. 2). Además lleva holgura
     frente a un margen ≤ 4·10⁹Te^{−15.449T} (B2).
   - C_p es indefinido con espectro ± de multiplicidad infinita (R183_018 Prop. 4.1). Φ(W_λ) tendría que
     absorber infinitas direcciones negativas con margen superexponencialmente pequeño.
4. *Conexión global:* sólo vía «Son ≥ C_ε en P_T», que es la inercia N_T (OPEN, REF-D).

**Ruptura bajo controles.** Φ(W_λ) no ve el peine. Con c = 2 la desigualdad falla, pero porque el resto crece y
no porque cambie el signo de alguna pieza (patrón B1/B2). **Repetición de clase:** W-lin, W11′, B2. El ítem 9 de
R186_006 («¿existe un operador de segundo orden que conmute con P^S y con P̂^S?») sigue OPEN, pero es una pregunta
de conmutación y no de signo.

### (c) Bochner mixto en el semianillo: positividad definida en la variable aditiva x combinada con la convolución multiplicativa de los contactos

1. *Antecedente:* 211 POWER_HYPERBOLIC_MODEL_GRAM §§12.6–12.7 (realización teta exacta; falta un núcleo no local
   positivo); 106_109 §2 (sumación por partes en teta, resto de Bernoulli con signo); LEDGER_L5_META C1
   (Poisson-ℤ es lineal en el peine); R163_154.
2. *Nuevo:* sería un enunciado de la forma a_T(F) = ∫ Q_F(y) dμ(y), con μ ≥ 0 una medida en el dual aditivo y
   Q_F(y) ≥ 0 construido con e^{2πixy} y los contactos.
3. *Por qué evitaría la dificultad:* no la evita.
   - El peine sólo entra por Poisson-ℤ, el canal (β), que es ciego a cΛ y a los borrados. Para verlos hay que
     pasar por (γ).
   - Expresar a_T como integral firmada en la variable aditiva es la realización teta. Su obstrucción registrada
     es justamente que el núcleo no local no es positivo.
   - Positividad de Bochner en x de Σ v_n e^{2πi(log n)…} es positividad de la medida de contactos: PC rama 2,
     CPOS_CLASS_001.
4. *Conexión global:* ninguna nueva.

**Ruptura bajo controles.** Bajo cΛ, μ sigue siendo positiva, porque es la parte de Poisson y no tiene pesos.
**Repetición:** memoria de selecciones rechazadas («métricas no locales», «sumación por partes en theta») y canal
(β) del Lema C.

### (d) Otras

Las dos variantes de la covariancia aditiva quedan cubiertas por el Lema C, cada una en su canal:
- la relación canónica de conmutación como identidad de Green ([X, ·] sobre E y C) cae en (γ) y en R161_042–044;
- el núcleo e^{2πixy} como intertwiner de la suma S_N cae en (β)/(γ) y en R161_040.

No encuentro otra vía defendible.

## 3. Residuo preciso (la mejor de las tres)

El único punto de esta línea que no está cerrado por un NO-GO es RULES_AVOID K7, abierto:

  SP-161 / L161.1 (R161_002 §§4–5):
    a_T = Σ_N w_N Re⟨RF, S_N𝓕F⟩ + cuadrados de fuga de C_T = (1−P_T)𝓕P_T, sobre todo P_T.

Sólo murió la rama w_N ≥ 0 (R161_002 Teor. 8.1). Los pesos con signo, o las derivadas discretas en N, no se
escribieron.

**Operación que falta.** Hace falta una sucesión explícita w_N con signo, no tomada de un optimizador, que cumpla
dos cosas. Primero, que Σ w_N H_{M,N} cancele el resto de hipérbola positivo h(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) para
k > e^{2T}; una diferencia finita en N es candidata natural, porque h es monótono en N. Segundo, que el término de
Poisson resultante, Σ w_N E_N, quede orientado: que sea una fuga exterior ‖(1−P_T)·‖² y no un conmutador de
soporte [P,S].

Ésta es la «identidad que conecte un cuadrado de fuga con el defecto de PC» que exige la reapertura de K1. La
covariancia aditiva entra por E_N; la multiplicativa, por h(k). Bajo cΛ la cancelación interior fallaría en k = 2
por δ = log 2 (R161_001 Teor. 4.1); bajo Beurling falta E_N. No lo propongo como candidata porque no tengo los
w_N, y anunciarlo sin ellos repetiría K7.

## 4. Lista de afirmaciones

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | La pista «covariancia aditiva + Λ∗1 = log» es el contenido de R161_001 (PC) más R160_C8_R1 (Tate–Beckner) | CITED (lectura en primaria) |
| 2 | Arch es la incertidumbre logarítmica con constante exacta C_0 = ψ(¼) − log π | CITED (R160_C8_R1 Cor. 2.4) |
| 3 | El cuadrado canónico de PC es ciego al signo | CITED (R161_002) |
| 4 | El Green mixto E–C deja piezas sin signo; la corrección de Tate se anula por paridad | CITED (R161_042–044) |
| 5 | El operador prolato conmutante no existe en forma local para S ⊇ {∞,2} | CITED (R186_003 fila 4, R186_006 fila 4) |
| 6 | Oscilador más dilatación por 2: NO-GO de conmutación | CITED (R186_006) |
| 7 | Lema C, pieza (α): la relación de Tate–Beckner no contiene pesos | PROVED (trivial) |
| 8 | Lema C, pieza (β): Poisson-ℤ sin pesos es invariante bajo cΛ y bajo borrados | PROVED (trivial) |
| 9 | Lema C, exhaustividad de los tres canales | ARGUED |
| 10 | Defectos interiores en el caso 2, 3, 4: log 2 en k = 2 (c = 2), −log 2 en k = 4 (borrado de 4) | PROVED (lectura de R161_001 Teor. 4.1) |
| 11 | (a) repite R161_002, K2 y J8 | ARGUED (cotejo) |
| 12 | (b) cae en W-lin, W11′ y B2 | ARGUED (cotejo) |
| 13 | (c) repite la selección de métricas no locales y la de teta, y cae en el canal (β) | ARGUED (cotejo) |
| 14 | Residuo: K7, pesos w_N con signo en SP-161 | OPEN |
| 15 | Signo global de a_T | OPEN |
