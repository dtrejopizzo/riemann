# Anexo — Re-etiquetado de las candidatas de la fase 193

Objeto: el signo de la forma de ventana a_T sobre el subespacio primitivo P_T (objetivo λ_A(T) ≥ 0 para todo T),
tratado sólo como problema sobre esa forma cuadrática. Fuentes: `03-research/phase-193-creation-campaign/`
(memos CA_*, tablas de semillas CA_*_000, revisiones CA_*_REVIEW, síntesis, `CAMPAIGN_LEDGER.md`),
`05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` (secciones de las fases 190–193 y re-exámenes),
`AUDIT_PHASE193_CERTAINTY.md` («AUD», con su número de fila), `AUDIT_A.md`, `AUDIT_B.md` y `RULES_AVOID.md` §C.

Regla aplicada: una ruta se cierra sólo por prueba de imposibilidad dentro de una clase de métodos declarada o por un
falsificador explícito. Una reformulación exacta es un objetivo válido, no un cierre.

Clases: **(a)** CERRADA–PROBADA (falsificador explícito o NO-GO probado de clase; se nombra) · **(b)** CERRADA sólo
ARGUMENTADA (se dice qué falta) · **(c)** REFORMULACIÓN EXACTA (objetivo válido; se dice de qué enunciado) · **(d)**
UNA LÍNEA / examen insuficiente para contar como intentada · **(e)** residuo ABIERTO.

Abreviaturas: O1–O15 = modificaciones de P47 (numeración de P47, fe de erratas del ledger, ronda 3); (B″) = identidad
válida para todo peine (lem:shape-ident, PROBADO); (B′) = lectura «ninguna estimación lleva el signo» (lem:shape-est (iv),
ARGUMENTADA); CIRC = cláusula de muerte que en P47 es ARGUED/CONDITIONAL/OPEN (O11, O12, O10 primitiva, (B′)(iv), O4^ε/O5,
G1→(R)(10)); [crit] = cribado de precisión M^{−3} (NUMÉRICO); (S), (N) = reformulaciones de P47 §Open problems; «lado
espectral» = cláusula (R)(4). «Ín.» = veredicto del índice (README o ledger); «Prim.» = lo que sostiene el memo primario
y su revisión.

Nota de método: para los memos desarrollados se leyó la sección de veredicto/resultado y su revisión (o la fila del
ledger que la resume, cuando la revisión es conjunta); para las semillas de pre-cribado la fuente primaria es la fila o
el párrafo de la tabla CA_*_000, que en muchos casos es todo lo que existe.

## 1. Frente A — grupo modular / Hecke

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| A1 | CA_A_001 | positividad Petersson/Maass–Selberg/RS en PSL₂(ℤ)\ℍ | cerrada (no reintentar) | NO-GO PROBADO sólo para la clase «norma de Eisenstein en variable espectral» (Cor 3); extensión «toda positividad de Eisenstein» RETIRADA; exclusión general por O11/O12 = CIRC | (a) para la clase norma; resto → A1r |
| A1r | CA_A_001 (abierto del ledger) | Mellin en y / Rankin–Selberg en w alcanzando ζ(½+iτ) en el eje unitario | no figura como cerrada; README audit lo lista como «re-examinar» | ABIERTO, nunca desarrollado | (e) |
| A2 | CA_A_002 | operador de transferencia Lewis–Zagier/Mayer | «NO-GO» (corregido a ARGUED en README) | NO-GO ARGUED; fórmula de ψ_s CITED-UNVERIFIED | (b): falta verificar ψ_s y probar que Λ entra sólo vía log det en toda lectura |
| A3 | CA_A_003 §2 | multiplicatividad de Hecke sobre σ_T | NO-GO PROBADO | relaciones de Hecke = identidades de Chebyshev, (B″) PROBADO | (a) (B″) |
| A3s | CA_A_003 §3 | tests de Hecke sobre la familia | REF-D | = (S) + (B′) | (c) de (S) |
| A3r | CA_A_003 §4 | forma de paquete metaplectico fuera de la diagonal | ABIERTO en ledger | ABIERTO, nunca desarrollado | (e) |
| A4 | CA_A_004 | Eisenstein metapléctica peso ½ P₀⁺, Parseval | cerrada | Prop 1 CONFIRMADA (independiente del peine: O1–O7, O15); Cor 3 («Parseval = cuadrados aritméticos») ARG con FIX | (a) por O7/O15 sobre el objeto tal como se formuló |
| A4r | CA_A_004 (abierto) | variante Salié/Kuznetsov | OPEN-RESIDUE (baja) | no desarrollada | (e) |
| A5 | CA_A_005 | RS con vector test del minimizador | cerrada | ciego al peine, (B″) PROBADO; ningún núcleo continuo = multiplicador de ventana (PROBADO); continuación = (S) | (a) (B″) |
| A6 | CA_A_006 | transporte de abscisa 1→½ (Y-integración, promedio de Hecke) | NO-GO PROBADO | (ii) PROBADO (Thm 2); (i) = (S) | (a) para (ii); (i) es (c) de (S) |
| A7a | CA_A_007 §1 | homotopía desde extremo positivo | retirada (reintento N_012/W5) | no-cruce = positividad | (c) del objetivo (constancia de signo en el camino) |
| A7b | CA_A_007 | triples de borde para W_λ | «= capacidad polar 𝔊_T, PROBADO» | coordenadas de thm:parityschur | (c) de la condición polar 2×2 |
| A7c | CA_A_007 Thm 2 | positividad por reflexión entre lugares | NO-GO PROBADO | RP falla para todo peine atómico (PROBADO) | (a) |
| A7d | CA_A_007 §4 | t-concavidad de log\|ξ\| (NG-D2) | sin intento (RULES_AVOID §C, última línea) | ARG, no desarrollada | (d) |
| A7e | CA_A_007 §4 | autovectores equipados x^{b+iγ} | sin intento | ARG; el escape (equipamiento construido con primos) está nombrado en el memo | (e) |
| A8 | CA_A_008 | invariante entero / flujo espectral / Maslov | REF-D | Lema 1 PROBADO: constancia ⟺ objetivo | (c) del objetivo (sin cruce de autovalor por 0) |

## 2. Frente B — tests construidos con ζ

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| B1 | CA_B_001 | identidad de emparejamiento J′(½) | cerrada | identidades CONFIRMADAS; signo en el lado espectral; exclusión O11/O12 = CIRC, pero (R)(4) es estructural | (c) (contenido de signo = lado espectral (R)(4)) |
| B2 | CA_B_002 | descomposición Riesz/Jensen de −∂_σH | cerrada | lectura sin ζ: (B″); lectura con ζ: (R)(4) | (a) (B″) en la lectura genérica |
| B3 | CA_B_003 | auto-emparejamiento Δ_a ≡ 0 ⟺ EF | cerrada | Thm 1 PROBADO; la propiedad sobrevive O7 (cuartetos) | (a) O7 |
| B3r | CA_B_003 (residual) | desigualdad que USE Δ≡0 (no la propiedad sola) | pendiente en ledger | no desarrollada | (e) |
| B4 | CA_B_004 | transporte J(σ), identidad de Green | cerrada | J(1)=∞ por el polo (PROBADO); cadena de convexidad falsa | (a) |
| B5 | CA_B_005 | inversión «defecto ⇒ fondo negativo» | cerrada | (Inv) FALSA (PROBADO); Prop 2 = prop:wit-sens | (a) |
| B6 | CA_B_006 | lema de bola abierta; conjuntos interiores | cerrada | = prop:wit-sens; pertenencia a la cola de Euler no lleva signo | (a) (sólo controla I_ζζ) |
| B7 | CA_B_007 | descomposición convexa en 𝒱_T^meas | cerrada | = objetivo o certificado (clase (D)) | (c) del objetivo / certificado dual |
| B8 | CA_B_008 | brecha de concavidad Γ | REF-D (tautología) | Thm 1 coordenada; Γ = tautología | (c) del objetivo |

## 3. Frente C — local–global / adélico y áreas nuevas

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| C1 | CA_C_000 C1 | Hasse–Minkowski ponderado, partición convexa por primos | cerrada | razón REF-D incorrecta (FIX); muerte correcta (cor:Qp) ARGUMENTADA | (b): falta escribir la contradicción con cor:Qp para toda elección de c_p |
| C2 | CA_C_000 C2 | Lévy–Khintchine por lugar | cerrada | (B″), O7/O15 | (a) (B″), O7 |
| C3 | CA_C_001 | fórmula del producto como acoplamiento | NO-GO PROBADO | Thm 1 PROBADO; 2 celdas CONDITIONAL (O4^ε, O5) pero caen también por O7 | (a) O7 / Thm 1 |
| C4 | CA_C_000 C4 | residuos de Tate / espacio de clases de adeles | REF-D | reformulación exacta | (c) (formulación de Tate del objetivo) |
| C5 | CA_C_000 C5, CA_C_002 | HM clásico (MW-3) | NO-GO en clase clásica | Prop 1 PROBADO (clase 𝓗); lectura bien planteada = (S) | (a) clase 𝓗; resto (c) de (S) |
| C5L | CA_C_002 abierto; F3 | HM condensado con entrada arquimediana (líquida) | «NO-GO PROBADO» (README F) | PROBADO sólo para 3 clases declaradas (CA_F_001); caso arquimediano ARGUED | (b): falta clase que incluya entrada líquida arquimediana |
| C6 | CA_C_000 C6, CA_C_002 Prop 2 | partición toro/línea en cajas | REF-D | Near = línea de Kronecker − Haar | (c) de (S) |
| C7 | CA_C_003, CA_C_005 | (Fam_η) = T*₃(η) | criticidad retractada | sólo necesaria para η>2/3 (NUMÉRICO); μ_M cota inferior | (d) (dato numérico; no examen de signo) |
| C8 | CA_C_007 | familia η como paso de signo | EXCLUIDA | Lemas 1–2, Prop 3 PROBADOS; genericidad FE-clase NUMÉRICA | (b): falta probar positividad para Epstein/negatividad Beurling (hoy NUMÉRICO) |
| CD1 | CA_C_004 D1 | Γ vs términos locales en malla Nyquist | REF-D | = (N) | (c) de (N) |
| CD2 | CA_C_004 D2 | racionalidad de ζ(2k)/π^{2k} | cerrada | O7 con cuartetos racionales, ARG (testigo «plausible») | (b): falta testigo explícito de cuarteto racional |
| CD3 | CA_C_004 D3 | Kummer / p-ádico | cerrada | ℚ_p no ordenado (PROBADO, categoría) | (a) (categoría: no hay desigualdad en p) |
| CD4 | CA_C_004 D4 | Iwasawa / μ=0 | cerrada | 1 línea + (R)(10) CIRC | (d) |
| CD5 | CA_C_004 D5 | unitariedad del factor EF | cerrada | prop:shape-phase, (B″) | (a) (B″) |
| CD6 | CA_C_004 D6 | ley local del minimizador | REF-D | = Teorema X / C*_A | (c) del enunciado sobre el minimizador (Lemma S) |
| CE1 | CA_C_006 E1 | o-minimalidad / Pila–Wilkie | NO-GO ARGUED | conjunto semialgebraico ⇒ método vacío (casi inmediato) | (a) (vacuidad elemental; falta sólo redactarla) |
| CE2 | CA_C_006 E2 | probabilidad libre Arch vs Div | cerrada | conmutan ⇒ no libres (PROBADO elemental) | (a) para independencia libre |
| CE3 | CA_C_006 E3 | Ax–Schanuel | cerrada | O15 (PROBADO) | (a) O15 |
| CE4 | CA_C_006 E4 | Helson H²(𝔻^∞) | cerrada | toro/línea (= (S)) + (B′) CIRC | (c) de (S) |
| CE5 | CA_C_006 E5 | Positivstellensatz en η>2/3 | cerrada | SOS = clase (D); premisa [crit] retractada | (c) (certificado dual) |
| CE6 | CA_C_006 E6 | identidad del lado espectral de la familia sin primos | «mantener como clasificación» | no desarrollada | (d) |

## 4. Frente D — fase / función de Hardy

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| D1 | CA_D_000 D1 | primer momento espectral (retardo de Wigner–Smith) | cerrada | 𝔞_T = −2∫u\|ȟ\|²: reescritura exacta | (c) del objetivo (media de frecuencia ≤ 0) |
| D2 | CA_D_001 | transferencia de amplitud de Hardy | HERRAMIENTA | Thm 1/1′/1″ PROBADOS; FE-genérica; exclusión O10/O12 CIRC, O7 ARG | (a) como paso de signo por (R)(11) sólo vía O10 citado; herramienta viva |
| D3 | CA_D_000 D3 | Landau / máximo, Bohr–Jessen | cerrada | reintento R164_102 (falsificador ζ·E) | (a) (falsificador ζ·E) |
| D4 | CA_D_000 D4 | Kramers–Kronig / DtN | cerrada | (R)(4) o (B″) | (a) (B″) en la lectura de identidad |
| D5 | CA_D_000 D5 | chirp Riemann–Siegel + FM | cerrada | R163_603 (f_χ) | (a) falsificador f_χ |
| D6 | CA_D_000 D6 | causalidad de scattering | cerrada | ⟺ semiplano sin polos de S_X | (c) (región sin polos de S_X) |
| D7 | CA_D_000 D7 | fase de de Branges/Kreĭn | cerrada | σ_T(0)<0 (PROBADO); extensión positiva = certificado (thm:Z) | (a) σ_T(0)<0 |
| D8 | CA_D_000 D8, CA_R2_001 | homotopía de exponente W(α) | muerte 1L → THM | interpolación desde enteros NO-GO (clase, PROBADO); W(0)≥W(1) falso en la celda central (PROBADO); entrada restante sobre {\|Z_T\|<1} | (a) para interpolación; residuo = (c) de la celda central de Nyquist |
| D9 | CA_D_002 | clausura del cono transferido | NO-GO PROBADO | Thm 2, 2′ PROBADOS | (a) |
| D10 | CA_D_003 | transferencia vs familia s_w; residual amplitud uno | cerrada | residuos DEAD/REF-D (2 FIX) | (c) de (R)(7)/celda central |

## 5. Frente E — álgebras de operadores / cuántico

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| E1 | CA_E_000 | KMS más allá de Bost–Connes | dead | β real sólo (ARG); O11 CIRC; reintento 114_d_116 | (b): falta probar que β complejo no aporta y un falsificador PROBADO en lugar de O11 |
| E2 | CA_E_000 | cociclo de Connes | dead | conmutativo ⇒ símbolo puntual (falso en 0); REF-D | (a) (σ_T(0)<0) |
| E3 | CA_E_000 | índice de Jones / TL | dead | «no se conoce objeto» | (d) |
| E4 | CA_E_001 Thm 1 | CP / Choi / entrelazamiento | REF-D | separabilidad PROBADA: objetivo ⟺ positividad en vectores producto de Euler | (c) (forma sobre vectores de Euler) |
| E5 | CA_E_001 Thm 2 | multiplicadores de Schur / factorización GCD | NO-GO PROBADO | PROBADO | (a) |
| E6 | CA_E_000 | CCR / Robertson | dead | reintentos (R178 NO-GO) | (a) por herencia de R178 |
| E7 | CA_E_000 | ITPFI / Kakutani | dead | O11 (CIRC), O15 (PROBADO), Thm U | (a) O15 |
| E8 | CA_E_000 | Golden–Thompson / Gibbs | dead | igualdad por conmutación (elemental) | (a) |
| E9 | CA_E_000 | Kadison–Singer / MSS / Lee–Yang | dead | reintento fase 11; (B′) CIRC; (R)(4) | (b): sin falsificador PROBADO propio; descansa en (B′)(iv) |
| E10 | CA_E_000 | Araki / Petz | dead | monotonía en dirección equivocada (lem:monoT) | (a) dirección |
| E11 | CA_E_000 | sistemas de operadores / Arveson | dead | REF-D (KEP), 1 línea | (c) (indeterminación de Kreĭn) |
| E12 | CA_E_000 | NC-SOS / de Finetti | dead | colapso conmutativo (PROBADO) | (a) |

## 6. Frente F — topología / geometría

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| F1 | CA_F_000 F1 | Floer más allá de Maslov | REF-D | Lema F1 PROBADO: = datos espectrales | (c) (datos espectrales de 𝔞_T) |
| F2 | CA_F_000 F2 | Bridgeland | REF-D | Lema F2: soporte en ker Z = P_T ⟺ 𝔞_T ≻ 0 | (c) del objetivo |
| F3 | CA_F_000 F3, CA_F_001 | MW-3 condensado/líquido | NO-GO PROBADO (README) | PROBADO para 3 clases; Prop 3 (positividad local falsa en todo p) PROBADA | (a) en las 3 clases; caso arquimediano → C5L |
| F4 | CA_F_000 F4 | motívico / A¹ / RO(G) | REF-D | firmas = espectral | (c) (firma de 𝔞_T) |
| F5 | CA_F_000 F5 | Hodge–Riemann / lorentziano no-AHK | dead | Teorema P mal citado (FIX); hipótesis de firma ARG | (b): falta prueba de que la firma requerida falla (sólo cota n₋) |
| F6 | CA_F_000 F6 | leyes de Weyl / invariantes de calor | dead | 1 línea (espectral + (B″)) | (d) |
| F7 | CA_F_000 F7 | Selberg / equidistribución de horociclos | dead | estimaciones (B′) CIRC; L31 | (d) |
| F8 | CA_F_000 F8 | calibraciones | dead | certificado dual, 1 línea | (c) (certificado dual) |
| F9 | CA_F_000 F9, CA_F_003 §4 | DAG / trazas ∞ | dead | objeto no construido; = G-F ABIERTO | (e) (G-F) |
| F11 | CA_F_000 F11 | álgebras cluster | dead | O2/O6 (PROBADOS) | (a) O2/O6 |
| F12 | CA_F_000 F12 | capacidades simplécticas | REF-D | espectral | (c) |
| F13 | CA_F_000 F13 | tilting perfectoide | dead | ℚ_p no ordenado, 1 línea | (d) |
| F14 | CA_F_000 F14 | dinámica homogénea exacta | dead | clase de Bochner; σ_T(0)<0 | (a) σ_T(0)<0 |
| F15 | CA_F_000 F15 | nef/amplio, Nakai–Moishezon | dead | clase (D), presupone el objeto | (c) (certificado dual) |
| F16 | CA_F_002 | fórmulas de traza exactas (TF⁺) | NO-GO PROBADO | PROBADO para la clase declarada | (a) clase TF⁺ |
| F17 | CA_F_003 | objeto polarizado sobre ℤ (G-F) | gap ABIERTO | «OPEN (object unbuilt)»; Prop 2 PROBADA (invariantes unitarios = espectrales) | (e) |

(F10 fue excluida por el brief y no se clasifica.)

## 7. Frente G — álgebras exóticas / combinatoria

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| G0 | CA_G_001 | cuadrados = factorizaciones de Gram | PROBADO | REF-D o certificado | (c) (factorización de Gram) |
| G1 | CA_G_000 G1 | SUSY / Witten / Riccati | dead | factorización ⟺ positividad | (c) del objetivo |
| G1m | CA_G_001 §1 | lema del monoide libre ℕ^× | PROBADO | isomorfismo PROBADO; excluye sólo vía (R)(10) (O11 ARG, O12 OPEN) | (b): falta falsificador Beurling/ζ_K PROBADO |
| G2 | CA_G_000 G2 | Clifford / Weitzenböck | dead | partición natural: ambos sumandos indefinidos (cor:Tarch, cor:Qp) | (a) sólo para la partición natural |
| G3 | CA_G_001 §3 | escalera Elias–Williamson | REF-D/reintento | complemento primitivo lleva el objetivo | (c) (torre de Schur) |
| G4 | CA_G_000 G4 | categorificación | dead | G0(c), 1 línea | (c) |
| G5 | CA_G_000 G5 | VOA / moonshine | dead | sólo O10 primitiva (CIRC) | (b): falta O10 PROBADO para la forma primitiva |
| G6 | CA_G_000 G6 | polinomios lorentzianos | reintento | criterio D.15.2 PROBADO sin signo | (a) por herencia R138 |
| G7 | CA_G_000 G7 | cluster TP | dead | PF₅ falla (CITED); PF₄ ABIERTO | (a) orden ≥5; orden ≤4 → (e) |
| G8 | CA_G_000 G8 | Jordan / conos simétricos | dead | auto-dualidad = thm:D1 | (c) |
| G9 | CA_G_000 G9 | Connes–Kreimer Birkhoff | dead | = Wiener–Hopf (W-det) | (a) por herencia W-det |
| G10 | CA_G_000 G10 | involuciones que invierten signo | dead | G1 (CIRC) + G0(b) | (c) (mitad SOS) / (b) (mitad monoide) |
| G11 | CA_G_000 G11 | grupos cuánticos / Shapovalov | dead | reintento NG-67, 1 línea | (d) |
| G12 | CA_G_000 G12 | Hecke de ℕ^× «Soergel» | dead | forma monoide: G1 (CIRC); con ℕ: O7 | (a) O7 en forma con peine; forma monoide (b) |

## 8. Frente H — semianillo (ℕ,+,·)

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| H1 | CA_H_001 | p-derivaciones de Buium, wronskiano | NO-GO | PROBADO/CITED para la clase declarada | (a) clase 𝒦_δ |
| H2 | CA_H_000 H2 | Stepanov sobre ℤ | dead | reintento G1_B9 Lema 3 (PROBADO char 0) | (a) |
| H3 | CA_H_000 H3 | acarreos / Witt | dead | forma ciega al acarreo (ARG, CA_H_001 §1.4) | (b): falta enunciado probado de ceguera |
| H4 | CA_H_000 H4 | suma-producto | dead | enunciados de conjuntos sobreviven O2/O7/O15 | (a) O2/O7/O15 |
| H5 | CA_H_002 | invariante de Erdős (S⁺) | separa pero no O7 | sobrevive O7, asintótico | (a) O7 como paso de signo |
| H6 | CA_H_002 Thm 3.1 | línea de Kronecker − Haar | REF-D | = (S) | (c) de (S) |
| H7 | CA_H_000 H7 | brecha de integralidad / Liouville | dead | sólo techo de densidad (thm:ceiling) | (a) dirección necesaria |
| H8 | CA_H_001 §5 | levantamientos globales de Frobenius | NO-GO clase | PROBADO/CITED, clase declarada | (a) clase declarada; correspondencias no-gráfica → F17 |
| H9 | CA_H_000 H9 | divisibilidad CRT (SPEC_B línea 3) | dead | W7 lineal; REF-D η≤η₀ | (c) |
| H10 | CA_H_000 H10 | derivada aritmética | dead | sólo G1 (CIRC) | (b): falta falsificador PROBADO del monoide |

## 9. Frente I — análisis del minimizador

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| I1 | CA_I_001 Thm 1–2 | Markov / Krein–Rutman / máximo | NO-GO PROBADO | Thm 2 vía O2 PROBADO | (a) O2 |
| I1⋆ | CA_I_001 Cor 6, CA_R1_001 | conjunto separador 𝖯⋆ | REF-D (ahora PROBADO) | REF-D por identificación PROBADO; toda subconjunción tiene falsificador | (c) (fuerza a = Λ, K ≡ 0) |
| I1g | CA_I_001 | fórmula de Markov para E general | — | ARG (FIX) | (b): falta la prueba de la fórmula |
| I2 | CA_I_000 I2 | estructura nodal de h* | lema | ≥2 cambios de signo PROBADO; sin signo | (a) (B″: sólo geometría de restricciones) |
| I3 | CA_I_001 §5 | simetrización | dead | Prop 5.1 PROBADA | (a) |
| I4 | CA_I_002 | virial / Pohozaev | dead | vale para todo peine (DH incluido) | (a) (B″) |
| I5 | CA_I_002 | frecuencia de Almgren | dead | Prop 2.2 PROBADA | (a) |
| I6 | CA_I_000 I6 | continuación única | dead | automática (Paley–Wiener) | (a) |
| I7 | CA_I_002 §3 | Γ-convergencia | dead | o(1) absoluto vs margen, ARG | (b): falta comparar explícitamente con el margen probado 4·10⁹Te^{−15.449T} |
| I8 | CA_I_002 §4 | concentración–compacidad | dead | cuadrática ⇒ sin subaditividad estricta (ARG corto) | (b): redactar como lema |
| I9 | CA_I_002 §2 | capa de borde ±T | dead (sólo cota superior) | transversalidad DH ARG | (b): falta prueba de transversalidad |
| I10 | CA_I_001 §3 | comparación de semigrupos | plegada | λ₀ monótona, λ_A no | (a) (O2) |

## 10. Frente J — desigualdades de correlación

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| J1 | CA_J_002 §1 | GKS con 𝔸_M | NO-GO | frustración Thm 1.3 PROBADO | (a) |
| J2 | CA_J_002 §2 | FKG en retículo de divisores | NO-GO | clase de igualdad = vectores de Euler (PROBADO) | (a) |
| J3 | CA_J_000 J3 | Ginibre/GHS/Lebowitz | dead | presuponen ferromagnetismo ⇒ Thm 1.3 | (a) |
| J4 | CA_J_000 J4 | Brascamp–Lieb varianza | dead | entrada Hess V ⪰ 0 = objetivo | (c) del objetivo |
| J4′ | CA_J_000 J4′ | BL geométrico / BCCT | dead | datos de dimensión; sólo O11 (CIRC) | (b): falta falsificador PROBADO |
| J5 | CA_J_000 J5 | Prékopa–Leindler | reintento PF | PF₅ falla; PF₄ ABIERTO | (a) orden ≥5; ≤4 → (e) con G7 |
| J6 | CA_J_001 | tablero / RP en coordenadas primas | NO-GO PROBADO | Thm 1–2 PROBADOS | (a) |
| J7 | CA_J_000 J7 | dominación gaussiana | dead | requiere RP ⇒ J6 | (a) |
| J8 | CA_J_000 J8 | Rayleigh fuerte | dead | localización de ceros (R)(4), 1 línea | (d) |
| J9 | CA_J_000 J9 | FK / cluster aleatorio | dead | requiere pesos ferromagnéticos | (a) |
| J10 | CA_J_000 J10 | Dobrushin / Kotecký–Preiss | dead | perturbativo, [crit] NUM | (b): falta comparación con el margen probado |
| J11 | CA_J_002 Prop 2.4 | comparación de Holley | plegada | lineal en Λ | (a) (clase de igualdad J2) |
| J12 | CA_J_000 J12 | log-supermodularidad | plegada | φ toma valores negativos (Lema J0′) | (a) |

## 11. Frente K — formas cuadráticas frustradas

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| K1 | CA_K_002 §1 | interpolación de Guerra | NO-GO PROBADO | Thm 1.2: signo del camino = enunciado del minimizador | (c) (enunciado sobre el minimizador) |
| K2 | CA_K_000 K2 | Talagrand/Parisi | dead | sin desorden | (a) (vacuidad) |
| K3 | CA_K_000 K3 | cavidad ASS | dead | reducciones de Schur | (c) (torre de Schur) |
| K4 | CA_K_000 K4 | Grothendieck / SDP | dead | lado vectorial = Gram | (c) (G0) |
| K5 | CA_K_000 K5 | Lasserre | dead | nivel 1 = PSD = objetivo; thm:sos | (c) |
| K6 | CA_K_001 §3 | holonomía ℤ/2 | NO-GO | contraejemplo g𝖡 (PROBADO) | (a) |
| K7 | CA_K_001 §4 | Laplaciano con signo / Cheeger | NO-GO | descomposición PROBADA; pérdida ½ vs 1−O(1/M) ARG/NUM | (b): falta pérdida demostrada contra el margen |
| K8 | CA_K_001 §1–2 | diamagnetismo | NO-GO PROBADO | Thm 1.2, Thm 2.2 (orden invertido) | (a) |
| K9 | CA_K_000 K9 | flujo de Lieb | dead | requiere RP | (a) |
| K10 | CA_K_002 §3 | flujo de calor en Ĝ / independencia de sitios | REF-D | Thm 3.2/Cor 3.3 PROBADOS: objetivo ⟺ Arch ≥ Near en tests primos | (c) (Arch ≥ Near sobre sitios primos) |
| K11 | CA_K_000 K11 | transformada de Doob | reintento Paper 41 | 31 no-gos heredados | (a) |
| K12 | CA_K_000 K12 | descomposiciones frustration-free | dead | CA_F_001 Prop 3 PROBADA | (a) |
| K13 | CA_K_000 K13 | TAP / Plefka | dead | perturbativo | (b): igual que J10 |

## 12. Frente L — construcciones mágicas exactas

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| L1 | CA_L_001 Thm 1.1 | certificado flat-top mágico | NO-GO PROBADO | thm:O como holgura complementaria | (a) |
| L2 | CA_L_001 | familia ε-mágica con datos modulares | NO-GO | nivel 20: O10 forma completa (CITED); nivel 1 reduce al peine | (a) nivel 20; nivel 1 → (c) del peine |
| L3 | CA_L_001 Prop 1.3 | Cohn–Elkies | dead | dirección superior (PROBADO) | (a) |
| L4 | CA_L_000 L4 | interpolación RV | dead | reintento P35-4; finZ | (a) |
| L5 | CA_L_002 | LP en sitios primos | REF-D | dual alcanzado, holgura en Z_s, exacto \|X\|≤5 | (c) (LP de sitios = objetivo) |
| L6 | CA_L_002 §3 | certificado en el toro de Bohr | REF-D | ídem | (c) |
| L7 | CA_L_000 L7 | incertidumbre de signo Cohn–Gonçalves | dead | 1 línea | (d) |
| L8 | CA_L_000 L8 | Delsarte/Turán | dead | = certificado | (c) |
| L9 | CA_L_000 L9 | CKMRV | dead | requiere retículo, 1 línea | (d) |
| L10 | CA_L_000 L10 | theta autodual + sinc | reintento | R164_401: sólo EF | (a) (falsificador de clase EF) |

## 13. Frente M — problema en sitios primos

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| M1 | CA_M_001 §1 | descomposición tipo Chen Near = ΣC_s(h) | PROBADO | identidad (B″) | (a) (B″) |
| M2 | CA_M_001 §2 | paridad / residuos | NO-GO | traza 0, lineal en Λ (PROBADO) | (a) |
| M3 | CA_M_001 §3 | integralidad de p − np′ | PROBADO | Thm 3.1/Cor 3.2: sitios perturbados dan el mismo valor de verdad | (a) |
| M4 | CA_M_000 M4 | pesos de criba / Chen | dead | W-sieve, NG-A4 | (a) |
| M5 | CA_M_000 M5 | serie singular | dead | ARG §1.3; PROBADO en clase decisiva vía Thm 3.1 | (a) en la clase decisiva |
| M6 | CA_M_001 §4 | inversión antidiamagnética | PROBADO | cancelación exacta EF-genérica | (a) (O10/O12 por EF) |
| M7 | CA_M_000 M7 | arcos de Vinogradov | dead | ARG §1.4 | (b): falta probar el peso despreciable fuera de θ≈0 |
| M8 | CA_M_001 Cor 3.3 | Beurling en sitios primos | plegada | Thm 3.1 | (a) |

## 14. Frente N y ronda R

| id | archivo | mecanismo | Ín. | Prim. | clase |
|---|---|---|---|---|---|
| N1 | CA_N_001 | V1 primal discreto alcanzado | 0 admisibles | en sitios: REF-D; exacto+alcanzado imposible en LP de ventana (thm:O) | (a) en LP de ventana; versión en sitios (c) |
| N2 | CA_N_002 | V2 peines positivos | Thm N2 PROBADO (T > ½log3, FIX) | transferencia unimodular imposible; no unimodular ABIERTA | (a) unimodular; → N2r |
| N2r | CA_N_002 / ledger | transferencias no unimodulares | ABIERTO («esperado G0») | no desarrollado | (e) |
| N3 | CA_N_003 | V3 auto-estructura | NO-GO (clases declaradas) | sin retículo autodual multiplicativo (PROBADO); sin forma automorfa generadora (PROBADO); Thm 5 vía O10 | (a) clases declaradas |
| R1 | CA_R1_001 | 𝖯⋆ y residuo D_∃c | REF-D PROBADO; D_∃c ABIERTO | D ⇒ D_∃c; recíproco = O4^ε | (e) D_∃c |
| R2a | CA_R2_001 | = D8 | ver D8 | — | (a) (ver D8) |
| R2b | CA_R2_002, README | SPEC_A (γ) con margen probado | ARG | (γ) falla con fuentes de potencia (ARG); versión sólo-identidades ABIERTA | (b) para (γ) con estimaciones; (e) versión de identidades |
| R3 | CA_R3_001 | línea θ, L*_j(θ) | «ADMISIBLE» no avalado → REF-D | identidades CONFIRMADAS | (c) (lema de paso L*_j) |
| R4 | CA_R4_001 | L*_j(θ) en ½log5 → ½log7 | ABIERTO | reducción PROBADA; signo ABIERTO; prueba 𝒞_θ en este contacto ARG NO-GO | (e) |

## 15. Recuento por clase

| clase | n | ids |
|---|---|---|
| (a) | ≈85 | A1, A3, A4, A5, A6, A7c, B2–B6, C2, C3, C5, CD3, CD5, CE1, CE2, CE3, D2, D3, D4, D5, D7, D8/R2a, D9, E2, E5–E8, E10, E12, F3, F11, F14, F16, G2, G6, G7, G9, G12, H1, H2, H4, H5, H7, H8, I1–I6, I10, J1–J3, J5–J7, J9, J11, J12, K2, K6, K8, K9, K11, K12, L1–L4, L10, M1–M6, M8, N1, N3 (contados una vez; D8 y R2a como uno) |
| (b) | 22 | A2, C1, C5L, C8, CD2, E1, E9, F5, G1m, G5, G10 (mitad monoide), H3, H10, I1g, I7, I8, I9, J4′, J10, K7, K13, M7 (+ R2b-(γ)) |
| (c) | 41 | A3s, A7a, A7b, A8, B1, B7, B8, C4, C6, CD1, CD6, CE4, CE5, D6, D10, E4, E11, F1, F2, F4, F8, F12, F15, G0, G1, G3, G4, G8, H6, H9, I1⋆, J4, K1, K3, K4, K5, K10, L5, L6, L8, R3 |
| (d) | 12 | A7d, C7, CD4, CE6, E3, F6, F7, F13, G11, J8, L7, L9 |
| (e) | 11 | A1r, A3r, A4r, A7e, B3r, F9/F17 (G-F), G7/J5-PF₄, N2r, R1 (D_∃c), R2b-identidades, R4 |

Las filas con doble clase (A6, C5, D8, G7, G10, G12, L2, N1, N2, R2b) se cuentan en la clase de su núcleo
principal; su otra mitad aparece como fila propia o como residuo. Por eso los totales por clase no suman exactamente
el número de filas (≈170 filas, ≈165 candidatas distintas tras identificar D8=R2a, F9≈F17, G7≈J5).

## 16. Redacción de RULES_AVOID.md §C que debe cambiarse

§C dice «Familias cerradas». Con esta tabla, las siguientes palabras de §C (todas de la fase 193) no están cerradas o
lo están sólo en un sentido parcial:

1. «**modular/Hecke (Petersson, Rankin–Selberg, Maass–Selberg, Eisenstein metapléctica, flujo espectral)**» —
   Petersson/MS sólo en la clase «norma» (A1); RS en w en el eje unitario (A1r), paquete metapléctico fuera de la
   diagonal (A3r) y Salié/Kuznetsov (A4r) siguen ABIERTOS; «flujo espectral» es reformulación exacta (A8), no cierre.
   Reescribir: «modular/Hecke: cerrados la clase norma, la multiplicatividad sobre σ_T y el transporte por
   Y-integración; abiertos A1r, A3r, A4r; flujo espectral = reformulación».
2. «**KMS, Bost–Connes, Jones, Araki/Petz, NC-SOS**» — KMS es sólo ARGUMENTADA (E1); Jones es una línea (E3, sin
   objeto). Mover KMS a «argumentadas» y Jones a «sin examen suficiente».
3. «**Floer, Bridgeland, motívico, Hodge–Riemann lorentziano, trazas de Selberg/Arthur**» — Floer, Bridgeland y
   motívico son reformulaciones exactas (F1, F2, F4); Hodge–Riemann lorentziano es ARGUMENTADA (F5); sólo trazas
   (TF⁺, F16) está PROBADA. Mover los tres primeros a «reformulaciones (objetivo válido)».
4. «**supersimetría, Soergel, VOA, cluster, Jordan**» — supersimetría y Jordan son reformulaciones (G1, G8); Soergel
   en forma monoide y VOA descansan sólo en cláusulas CIRC (G12, G5); cluster está cerrado sólo en orden ≥5, con PF₄
   ABIERTO (G7).
5. «**p-derivaciones, Stepanov, suma-producto**» — correcto como cerradas; pero la «derivada aritmética» y
   «acarreos» (H10, H3), si se agregan implícitamente, son ARG/CIRC.
6. «**Markov, principio del máximo, virial/Pohozaev, Almgren, Γ-convergencia**» — Γ-convergencia es ARGUMENTADA (I7);
   el conjunto 𝖯⋆ es reformulación PROBADA (I1⋆) y deja el residuo ABIERTO D_∃c.
7. «**OS/tablero, GKS, FKG, Lee–Yang, Brascamp–Lieb, Dobrushin, formas frustradas, Lasserre**» — Brascamp–Lieb: la
   versión de varianza es reformulación (J4) y la geométrica sólo CIRC (J4′); Dobrushin ARG (J10); Lasserre es
   reformulación (K5); Lee–Yang/Rayleigh es una línea (J8).
8. «**funciones mágicas tipo Viazovska**» — la función mágica literal está PROBADA (L1, N1), pero el LP en sitios
   primos / certificado en el toro (L5, L6) es reformulación exacta con dual alcanzado; debe figurar como objetivo.
9. «**aritmética de sitios primos (paridad, residuos, series singulares)**» — correcto (M2, M3, M5 PROBADOS en la
   clase decisiva); Vinogradov (M7) es ARG.
10. «**positividad total, PF, …(falla en PF₂; el núcleo no es PF₅)**» — añadir explícitamente «PF₄ ABIERTO».
11. «**Sonin…; cuerpos de funciones, Hodge, Arakelov, sitio aritmético, portadores h⁰**» — en lo que toca a la fase
    193, el objeto polarizado sobre ℤ (G-F, F17) está ABIERTO (objeto no construido), no cerrado.
12. La frase de cabecera «Familias cerradas» debe acompañarse de la advertencia de AUDIT_PHASE193_CERTAINTY: para la
    fase 193, «0 admisibles» significa «ninguna semilla tal como se formuló pasa los filtros PROBADOS», no «el área
    está cerrada».

Además §C, última línea: «Aún figuran sin intento: autovectores en espacio equipado, …, t-concavidad» — coincide con
A7e (e) y A7d (d); «repulsión anti-Siegel» no aparece en la fase 193.

## 17. Elementos (c)–(e) que merecen examen como objetivos de construcción

Cada uno con el objeto preciso que falta.

1. **K10 / M3 — Arch ≥ Near sobre tests en sitios primos** (c). Falta: una desigualdad matricial finita
   Arch_M − Near_M ⪰ 0 cuyo paso de signo use las posiciones log n y los pesos Λ(n)n^{−½} del peine (lo único que
   M3 deja), con control uniforme en M.
2. **L5/L6/N1 — LP en sitios primos sobre el toro** (c). Dual alcanzado, holgura sobre Z_s, exacto para \|X\| ≤ 5.
   Falta: una familia de restricciones que contenga un dato de la columna arquimediana (polo/EF) y un control del
   rango de la elipsótopa cuando \|X\| → ∞.
3. **R1 — D_∃c** (e). Falta: para cada T un c>0 con λ_A(T; cΛ) ≥ 0, y luego la cuestión O4^ε (κ_T ≠ 0) que
   identifica el c común; cada mitad es un objeto definido.
4. **R4 / R3 — lema de paso L*_j(θ)** (e)/(c). Falta: la evaluación exacta de 𝔄_j^{−1} sobre el campo exterior de
   cuatro átomos (casi cancelación a precisión relativa ≲ 1.6·10⁻⁶) con un mecanismo distinto del encierro
   certificado.
5. **R2b — inducción exacta sólo con identidades (SPEC_A)** (e). Falta: dónde entra log ℕ en ‖ℓ_e‖_{𝔄_j^{−1}}
   (coincidencia del bloque de contacto v_{n_j} contra 2n_j^{−½} en el desfase 2T_j) en forma de identidad, no de
   estimación.
6. **N2r — transferencias no unimodulares de señal analítica** (e). Falta: la clase de amplitudes admisibles
   (CA_D_002 §3.6) y una prueba de que alguna escapa a G0 (no es una factorización de Gram).
7. **F17 / F9 — objeto polarizado sobre ℤ (G-F)** (e). Falta: el objeto mismo — clase amplia, h⁰ cuadrático y
   propiedad de traza — cuya positividad venga de amplitud y no de la firma de 𝔞_T.
8. **A1r, A3r, A4r — residuos modulares** (e). Falta: la forma de RS en w restringida al eje unitario, la forma de
   paquete metapléctico fuera de la diagonal y la variante de Kuznetsov, cada una con la prueba de que su
   positividad no es una norma (no cae en O11/O12 ni en (R)(4)).
9. **G7/J5 — positividad total de orden ≤ 4 (PF₄)** (e). Falta: una prueba (no local) de PF₄ del núcleo y una
   desigualdad que conecte orden 4 con la forma de ventana.
10. **A7e — autovectores equipados construidos con primos** (e). Falta: el espacio equipado cuyo equipamiento use
    sólo el peine, y la identidad que exprese a_T en esa base.
11. **B3r — desigualdad que use Δ_a ≡ 0** (e). Falta: una desigualdad (no la propiedad sola, que cae por O7) en la
    que Δ≡0 sea hipótesis cargada junto con un dato que los cuartetos no tienen.
12. **D8 / D10 — celda central de Nyquist {\|Z_T\| < 1}** (c). Falta: una entrada específica que actúe sobre esa
    celda (amplitud uno) con la herramienta PROBADA CA_D_001.
13. **E4 — forma sobre vectores producto de Euler** (c). Falta: una propiedad de positividad que sea propia de esos
    vectores (no CP, que es equivalente) y que no sea una factorización de Schur (E5).
14. Elementos (d) que, si se quieren usar, deben examinarse antes de contarlos como intentados: A7d (t-concavidad),
    CE6 (clasificación de la familia sin primos), E3 (Jones), F6, F7, F13, G11, J8, L7, L9, CD4, C7.

## 18. Cobertura

- Archivos en la carpeta: 128 `.md` (memos, semillas, revisiones, síntesis, ledger, README).
- Candidatas/familias halladas: ≈165 distintas (A 16, B 9, C 20, D 10, E 12, F 16 + F10 excluida por el brief, G 14,
  H 10, I 12, J 13, K 13, L 10, M 8, N/R 9). Clasificadas: todas las halladas (≈170 filas).
- Lectura: AUDIT_PHASE193_CERTAINTY, README del índice (fases 190–193 y re-exámenes), AUDIT_A, AUDIT_B, RULES_AVOID,
  CAMPAIGN_LEDGER y CA_A_000_INDEX completos; tablas de semillas CA_*_000 y lotes CA_C_004/006 en sus filas/párrafos
  de veredicto; secciones de resultado de CA_A_002 y CA_F_003 §4. Para los demás memos desarrollados el veredicto
  primario se tomó de la fila del ledger que resume memo + revisión, no de una lectura completa de cada memo; esa
  diferencia es la principal limitación de este anexo. Ninguna lectura falló; no hubo memo ilegible.
