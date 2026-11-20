# Anexo — Lectura primaria completa de la fase 193 y contraste con ANNEX_PHASE_193_LABELS.md

Objeto: el signo de la forma de ventana 𝔞_T sobre el subespacio primitivo P_T (objetivo λ_A(T) ≥ 0 para todo T),
tratado sólo como problema sobre esa forma cuadrática. Cuando una fuente usa redacción que vincula el objetivo con otro
enunciado, aquí se escribe «(★)» y no se usa.

Fuente: los 128 archivos `.md` de `03-research/phase-193-creation-campaign/`, leídos completos (memos, tablas de
semillas, revisiones, síntesis, ledger, índice, README). Abreviaturas como en `ANNEX_PHASE_193_LABELS.md` («LABELS»):
O1–O15 numeración de P47 (fe de erratas del ledger); (B″) identidad válida para todo peine; (B′) estimación con resto;
REF-D reformulación exacta; CIRC cláusula de muerte que en P47 es ARGUED/OPEN. Etiquetas: PROVED / CITED / CONDITIONAL /
OPEN / NO-GO / NUMÉRICO / ARGUED.

Base del descarte: **(i)** falsificador explícito (se nombra y se dice si su fallo está PROVED, CITED, NUMÉRICO o
ARGUED); **(ii)** NO-GO de clase probado; **(iii)** sólo argumento; **(iv)** reducción al objetivo (REF-D);
**(v)** nada (no examinado). Clase: (a)–(e) como en LABELS.

Nota de numeración: las revisiones de CA_A_001–004 y CA_B_001–005 usan la numeración del brief («O7 Beurling», «O8
cuartetos», «O11 Epstein»); aquí se traduce siempre a P47 (O11 Beurling, O7 cuartetos, O10 Epstein).

---

## 1. Entradas por archivo

### Frente A

| archivo | mecanismo | veredicto primario (con etiquetas) | base | clase |
|---|---|---|---|---|
| CA_A_000_INDEX | índice del frente A | resume A001–A008; sin contenido propio | — | — |
| CA_A_001 | positividad de norma (Maass–Selberg, Petersson, RS con pesos E(·,w)>0) en PSL₂(ℤ)\ℍ | Lema 1 PROVED; Lema 2 (sin forma invariante positiva en Re s=¼) PROVED; Cor 3 (clase «norma en variable espectral»: peine Λ(n)/n en abscisa 1) PROVED; extensión a «toda positividad de Eisenstein» RETIRADA (adenda) | (ii) para la clase norma; además O10/O12 sobreviven (fallo de O10/O12: CITED en P47) | (a) clase norma |
| CA_A_001_REVIEW | — | confirma Lema 2 (FIX: irreducibilidad innecesaria), Cor 3 (FIX de signo del peine); rechaza «duplicación de línea» como barrera general: Mellin en y y RS en w alcanzan ζ(½+iτ) en el eje unitario | = memo | (a) clase norma |
| CA_A_002 | operador de transferencia / funciones de período | Prop 1 PROVED (identidad Σ(m+n)^{−2s}); NO-GO ARGUED en conjunto; fórmula de ψ_s CITED-UNVERIFIED; «no preserva conos en Re s=¼» ARGUED | (ii)-trivial: el objeto no contiene Λ ⇒ O1–O7, O15 lo dejan invariante (patrón lem:shape-ident); Λ sólo vía det (lado de ceros); O12 sobrevive (CITED en esbozo) | (a) objeto tal como se formuló (ver desacuerdo D3) |
| CA_A_002_REVIEW | — | EXCLUIDO por (R)(1),(3),(4) y ausencia de Λ; retira «duplicación de línea» como razón | = memo | (a) |
| CA_A_003 | multiplicatividad de Hecke sobre σ_T; tests de Hecke; escape metapléctico | §2 Thm PROVED (relaciones de Hecke = identidades de producto de cosenos, válidas para toda posición) ⇒ (B″); §3 lado de test = (S) y (B′); §4 forma de paquete metapléctico fuera de diagonal OPEN, no construida | §2 (ii) vía (B″); §3 (iv); §4 (v) en este memo | §2 (a); §3 (c); §4 → desarrollado en CA_A_004 |
| CA_A_003_REVIEW | — | confirma; §4 CITED-UNVERIFIED, prealerta: positividad de paquete es norma | = memo | — |
| CA_A_004 | serie de Eisenstein de peso ½ en Γ₀(4), Parseval en horociclo | cita verificada (coeficientes L_D(2s−½)/ζ(4s−1)); Prop 1 núcleo fuera de diagonal de rango uno por índice PROVED; Cor 2 (igualar un multiplicador exige ortogonalidad en D) PROVED como condición necesaria, «⇒ (B′)» ARGUED; Cor 3 ARGUED con FIX (thm:sos no cubre literalmente cuadrados de L_D suavizados); variante Kuznetsov/Salié OPEN-RESIDUE | (ii)-trivial: objeto sin Λ ⇒ O1–O7, O15 invariantes; O12 en esbozo | (a) objeto; variante → (e) |
| CA_A_004_REVIEW | — | EXCLUIDO; Cor 2 sólo reducción; adenda R3 (apertura) no avalada | = memo | (a) |
| CA_A_005 | RS regularizado con vector test del polinomio del minimizador | Prop 1 (RS_w ≥ 0 para todo test, w>1, sin peine) PROVED; Prop 2 (ningún núcleo continuo es el multiplicador de ventana) PROVED; Prop 3 PROVED; Prop 4 (continuación a ½ pierde positividad: PROVED; núcleo continuado = segundo momento: ARGUED) | (ii) vía (B″) para w>1; (iv) para la continuación (ARGUED) | (a) w>1; continuación (c)/(b) |
| CA_A_005_REVIEW | — | confirma Props 1–3; Prop 4 ARGUED; O12 sobrevive | = memo | (a) |
| CA_A_006 | transporte de abscisa 1→½ de Maass–Selberg: (i) promedio de Hecke, (ii) integración en Y | Lema 1 PROVED; Thm 2 (integración positiva en Y no mueve la abscisa aritmética) PROVED; Obs. 3 (MS = forma de ventana de ζ(2s) sobre cuadrados) PROVED como identidad, «clase 𝒞_PNT» ARGUED; (i) = (S): truncación indefinida PROVED, valor |ζ|² sólo formal | (ii) para (ii); (iv) para (i) | (a) (ii); (c) (i) |
| CA_A_006_REVIEW | — | confirma; §6 (homotopía) prealertada como reintento: por concavidad, no-cruce en segmento = objetivo | = memo | — |
| CA_A_007_SEED_TRIAGE… | homotopía/no-cruce; ternas de frontera; RP entre lugares; t-concavidad; autovectores equipados | homotopía retirada (reintento N_012/W5/flowdet/W-cont); ternas = coordenadas de thm:parityschur (Prop 1 PROVED reducción); Lema 1 (𝔞(f+Θf)=2𝔞(f)+2H_K(f), nivel Toeplitz) PROVED; Thm 2 (RP falla para todo peine con un átomo) PROVED; t-concavidad y autovectores equipados: una línea ARGUED | homotopía (iv)+reintento; ternas (iv); RP (i) falsificador: bump simétrico en ½log n₀, fallo PROVED, para todo peine; t-concavidad (iii); autovectores (iii) | (c), (c), (a), (d), (e) |
| CA_A_007_REVIEW | — | confirma; §6 (índice) prealertado: n₋ / primer contacto | = memo | — |
| CA_A_008 | invariante entero (flujo espectral, Maslov, índice firmado) | Lema 1 (constancia ⟺ sin cruce) PROVED; COLAPSA (REF-D); mecanismos de forzado muertos por NO-GO citados del corpus | (iv) | (c) |
| CA_A_008_REVIEW | — | confirma; índice de Cayley (corpus 632) sigue sin construir | = memo | (c) |
| CA_A_SYNTHESIS | cierre del frente A | lista hechos PROVED; residuos: Kuznetsov/Salié, propagación (M) general, índice de Cayley | — | — |

### Frente B

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_B_001 | identidad de emparejamiento I_ζζ = −J′(½)/2π | identidades (1.1)–(1.3) PROVED; signo de J′(½) = geometría de ceros ARGUED (después acotado por CA_D_001 a su peso congelado) | (iv) (sign = pieza de la propia forma) + O10/O12 sobreviven | (c) |
| CA_B_001_REVIEW | — | EXCLUIDO (O10, O12; (R)(4),(9)); REF-D | = memo | (c) |
| CA_B_002 | Riesz/Jensen de −∂_σ log|ζ/Z_{<X}| en la banda | (2.1) PROVED módulo potencial CITED; lectura sin ceros = identidad para todo peine | (ii) vía (B″) en la lectura sin ceros; (R)(4) en la otra | (a) |
| CA_B_002_REVIEW | — | EXCLUIDO; añade (R)(5) local | = memo | (a) |
| CA_B_003 | auto-emparejamiento Δ_a ≡ 0 | Thm 1 (Δ_a≡0 ⟺ ecuación funcional) PROVED; unicidad a=Λ CONDITIONAL (teorema de unicidad citado), caso ε=−1 OPEN; paso de signo por penalización ARGUED falso | (i) falsificador O7 (cuartetos mantienen el peine; fallo PROVED en P47 lem:shape-quartet) | (a) O7 para la propiedad sola |
| CA_B_003_REVIEW | — | confirma; FIX sobre DH; exclusión por O7 | = memo | (a) |
| CA_B_004 | símbolo en la línea sin ζ; transporte J(σ), identidad de Green | Prop 1 PROVED (reescritura); (3.1) PROVED en [½,1) y (1,2]; cadena de convexidad (3.3) FALSA por J(1)=∞ (PROVED); (W_σ) para g_X: OPEN, falso genéricamente ARGUED | (ii) (B″) para la identidad; NO-GO PROVED para convexidad a través de σ=1 | (a); residuo (W_σ) en [½,1) sin registrar (ver §3) |
| CA_B_004_REVIEW | — | FIX mayor (polo); NO-GO convexidad PROVED | = memo | (a) |
| CA_B_005 | inversión «defecto ⇒ fondo negativo» | Prop 2 PROVED tras FIX (es prop:wit-sens); (Inv) FALSA; §3 (apertura excluye propiedades finas) NON-SEQUITUR; §4 distancias de emparejamiento ARGUED | (i) falsificador Λ+cδ₂ con c pequeño (positivo y con Δ≢0), PROVED | (a) para (Inv) |
| CA_B_005_REVIEW | — | Prop 2 corregida (radio ℓ¹); §3 no avalado | = memo | (a) |
| CA_B_006 | lema de bola abierta; conjuntos interiores; (W_X) | Lema B (i)–(iii) PROVED (= prop:wit-sens); (iv) lectura metodológica RETIRADA; (W_X) pasa (R)(4) (PROVED) pero controla sólo I_ζζ | (iv)-parcial: I_ζζ es una de cuatro piezas (PROVED vía EI_002) | (a) para (W_X) como portador completo |
| CA_B_006_REVIEW | — | confirma (i)–(iii); FIX de escala; FIX polo repetido | = memo | (a) |
| CA_B_007 | O7/O8 como movimientos de punto; descomposición convexa | Prop 1(a) PROVED, 1(b) ARGUED; descomposición = objetivo / segmento extendido / clase (D); Prop 2 (Γ=0 ⟺ minimizador común) PROVED | (iv) | (c) |
| CA_B_007_REVIEW | — | confirma; Γ OPEN prealerta REF-D | = memo | (c) |
| CA_B_008 | brecha de concavidad Γ, cota de ángulo | Thm 1 (Γ ≥ min(θg₁,(1−θ)g₂)(1−|⟨h₁,h₂⟩|)) PROVED; REF-D tautología PROVED; (B″); (R)(5) | (iv) + (ii) (B″) | (c) |
| CA_B_008_REVIEW | — | confirma; familia de descomposiciones cerrada | = memo | (c) |
| CA_B_SYNTHESIS | cierre B; lista (P1)–(P6) | — | — | — |

### Frente C

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_C_000_SEEDS | C1–C6 | C1 descartada (división HM ponderada; argumento de cono negativo «implausible», ARGUED); C2 (B″) y identidad de salto PROVED; C3 → C_001; C4 REF-D; C5 → C_002; C6 → C_002 | C1 (iii); C2 (ii); C4 (iv) | C1 (b); C2 (a); C4 (c) |
| CA_C_000_REVIEW | — | C1: descarte correcto, razón parcialmente equivocada; condensado arquimediano ARGUED | = | — |
| CA_C_001 | fórmula del producto como acoplamiento | Lemas 1–4 PROVED; Thm 1 (tabla local/global) PROVED, dos celdas CONDITIONAL (κ_T≠0); (Fam_η) OPEN sub-enunciado | (i) falsificadores Λ±c1₆, Λ±c1_{p₀}, a_P, Λ+c1₂, fallo PROVED (Lema 3 + lem:cpos); revisión añade O7 para todas las celdas | (a) |
| CA_C_001_REVIEW | — | confirma; añade exclusión O7 | = | (a) |
| CA_C_002 | Hasse–Minkowski clásico; toro vs línea | Prop 1 (clase 𝓗) PROVED con falsificador ⟨−1,−1,−1,−1⟩⊥r; Prop 2 (Near = línea − Haar en cajas) PROVED, coordenadas; positividad = (S); condensado con entrada arquimediana ARGUED | (i) PROVED para 𝓗; (iv) | (a) 𝓗; (c) |
| CA_C_002_REVIEW | — | confirma | = | — |
| CA_C_003 | (Fam_η) = T*₃(η), η>2/3 | Prop 1 PROVED; Prop 2 deducción PROVED de entrada NUMÉRICO (minimizador fuera del span); obstrucción §3 ARGUED | (iii)+NUMÉRICO: «sólo necesaria» | (b) (ver D6) |
| CA_C_003_REVIEW | — | confirma; no correr μ_M | = | — |
| CA_C_004_SEEDS_BATCH2 | D1–D6 | D1 = (N) REF-D y falso puntualmente en 0 (σ_T(0)<0 PROVED); D2 O7 con parámetros racionales ARGUED; D3 categoría (ℚ_p no ordenado) + O7 ARGUED; D4 categoría (λ, μ son rangos/valuaciones) + (R)(10); D5 reintento prop:shape-phase (B″); D6 REF-D | D1 (iv); D2 (iii); D3 (ii)-categoría; D4 (ii)-categoría (misma base que D3); D5 (ii); D6 (iv) | (c), (b), (a), (a)/(b) igual que D3, (a), (c) |
| CA_C_004_REVIEW | — | confirma; D2 testigo O7 ARGUED | = | — |
| CA_C_005 | μ_M(η) numérico | NUMÉRICO todos positivos; conclusión «crítico» RETIRADA (norma ℓ² errónea) | — | — |
| CA_C_005_REVIEW | — | error de dirección (cota inferior) | = | — |
| CA_C_006_SEEDS_BATCH3 | E1–E6 | E1 conjunto semialgebraico ⇒ Pila–Wilkie vacío ARGUED; E2 conmutativos no libres PROVED elemental, asintótico ARGUED; E3 O11/O15; E4 = toro/línea + (B′); E5 SOS clase (D); E6 descartada como ruta, conservada como clasificación | E1 (iii); E2 (ii) exacto/(iii) asintótico; E3 (i) CITED/ARGUED en P47; E4 (iv); E5 (iv); E6 → desarrollada en C_007 | (b), (a)/(b), (a), (c), (c), ver C_007 |
| CA_C_006_REVIEW | — | confirma; FIX premisa [crit] | = | — |
| CA_C_007 | familia η: norma Gram, reducción a un escalar, test de falsificadores | premisa crítica retractada; Lemas 1–2, Prop 3 (s_M escalar de Schur) PROVED; identidad del lado de ceros PROVED, mecanismo ARGUED; positividad de la familia FE-genérica (x²+5y² positiva en la familia, forma completa negativa: NUMÉRICO) | (i) falsificador x²+5y² para la propiedad «ζ-específica», fallo NUMÉRICO (y CITED en P47 para la forma completa) | (b) |
| CA_C_007_REVIEW | — | confirma; exclusión por thm:shape(C) con etiqueta NUMÉRICO | = | (b) |

### Frente D

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_D_000_SEEDS | D1–D9 | D1 coordenada (B″); D2 → herramienta; D3 reintento (falsificador ζ·E, PROVED en corpus); D4 (R)(4)/(B″); D5 reintento (f_χ); D6 ⟺ semiplano sin ceros de Z_X; D7 σ_T(0)<0 + certificado; D8 una línea (corregida en CA_R2_001); D9 → D_002 | D1 (iv); D3 (i) PROVED; D5 (i) corpus; D6 (iv); D7 (i) σ_T(0)<0 PROVED | (c),(a),(a),(c),(a) |
| CA_D_000_REVIEW | — | confirma; O7 para D2 prealertado | = | — |
| CA_D_001 | transferencia de amplitud de Hardy | Thm 1, 1′, Cor 1.1, cota celda central PROVED; Thm 1″ (clase FE) PROVED; excluido como paso de signo porque vale en O10/O12 | (i) O10/O12: el teorema se cumple en objetos cuya forma es negativa (fallo CITED en P47; NUMÉRICO en CA_C_007) | (a) como paso de signo; herramienta viva |
| CA_D_001_REVIEW | — | re-derivado; acota el alcance de CA_B_001 §4 | = | — |
| CA_D_002 | clausura del cono transferido | Thm 2, 2′, Cor 2.1 PROVED (Thm 2 usa resultados clásicos CITED sólo dentro del NO-GO; Thm 2′ sin ceros); clasificación de amplitudes §3.6 OPEN | (ii) | (a) |
| CA_D_002_REVIEW | — | confirma | = | (a) |
| CA_D_003 | transferencia vs familia s_w; residuo amplitud uno | §1 (a)(b)(c) PROVED (2 FIX); §2 cinco residuos DEAD/REF-D | (iv)/(R)(4)/(R)(5) | (c) |
| CA_D_003_REVIEW | — | confirma | = | — |
| CA_D_SYNTHESIS | cierre D | «el defecto vive en {|ζ/Z_{<X}|<1}», lectura, no reducción | — | — |

### Frente E

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_E_000_SEEDS | E1–E12 | E1 β real sólo (ARGUED), O11, reintento; E2 conmutativo ⇒ criterio puntual falso en 0; E3 «no hay objeto»; E4/E5 → E_001; E6 reintento; E7 densidad (O11/O15) + Thm 2 de E_001; E8 (B′) + igualdad antes de compresión, compresión «territorio cerrado» ARGUED; E9 reintento, (B′), (R)(4); E10 dirección (lem:monoT); E11 REF-D; E12 colapso conmutativo PROVED | E1 (iii); E2 (i) σ_T(0)<0 PROVED; E3 (v); E6 herencia; E7 (ii); E8 (ii)/(iii); E9 (iii); E10 (ii); E11 (iv); E12 (ii) | (b),(a),(d),—,(a),(a),(a)/(b),(b),(a),(c),(a) |
| CA_E_000_REVIEW | — | confirma | = | — |
| CA_E_001 | colapso conmutativo; NO-GO de factorización de Schur | Lemas 0–1, Thm 1 (vectores producto bastan), Cor 1.1 (medias de Fejér en puntos y∈Ĝ), Cor 1.2, Thm 2 PROVED; factorización de tipo línea (ν=ν₁∗ν₂) ARGUED; 𝔸_M=𝔾_M∘𝔹_M a M fijo no excluida | Thm 1 (iv); Thm 2 (ii) | (c) E4; (a) E5 |
| CA_E_001_REVIEW | — | confirma | = | — |
| CA_E_SYNTHESIS | cierre E | — | — | — |

### Frente F

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_F_000_SEEDS | F1–F15 | F1 Lema F1 PROVED (espectral); F2 Lema F2 formal; F3 → F_001; F4 firma; F5 Lema F5 con FIX, hipótesis de firma ARGUED; F6 reintento R164_502 + (B′)/(B″) (luego cubierto por F_003 Prop 2); F7 → F_002; F8 certificado; F9/F13/F15 → F_003; F11 O2/O6; F12 espectral; F14 σ_T(0)<0 | F1/F2/F4/F12 (iv); F5 (iii); F6 (iv) vía F_003 Prop 2; F8 (iv); F11 (i) O2/O6 PROVED en P47; F14 (i) | (c),(c),(c),(b),(c),(c),(a),(c),(a) |
| CA_F_000_REVIEW | — | confirma; FIX F5 | = | — |
| CA_F_001 | MW-3 condensado/líquido | Lemas 1–2 (reformulación condensada o líquida = mismo enunciado, para toda topología Hausdorff con densidad) PROVED; Prop 3 (positividad local desnuda falsa en todo p) PROVED; Prop 4 (asignada = división convexa) REF-D | (iv) + (i) test F₊ de prop:cone(ii), PROVED | (a)/(c) — cubre también C5L (ver D5) |
| CA_F_002 | fórmulas de traza exactas, horociclos, Heegner | Lema 1 PROVED (FIX multiplicidad, paridad); Cor 2–3 PROVED; NO-GO clase TF⁺ PROVED; Arthur (G,M) ARGUED | (ii) | (a) — cubre F7 exacto |
| CA_F_003 | objeto polarizado sobre ℤ | Lema 1 tautológico PROVED; Prop 2 (invariantes unitarios = datos espectrales) PROVED; tricotomía fuera de 𝒢_u ARGUED; brecha G-F OPEN | Prop 2 (iv); G-F (v)-objeto | (c); G-F (e) |
| CA_F_001_003_REVIEW | — | confirma; eleva F_001 a PROVED | = | — |
| CA_F_SYNTHESIS | cierre F | — | — | — |

### Frente G

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_G_000_SEEDS | G1–G12 + hechos G0 (cuadrados = Gram) y G1 (monoide) | G1 REF-D; G2 ambos sumandos indefinidos; G4 G0(c); G5 O10 por caracteres de retículo; G6 reintento; G7 PF₅ falla CITED, PF₄ OPEN; G8 = thm:D1; G9 = Wiener–Hopf; G10 G1+G0; G11 reintento; G12 G1 / O7 | G1 (iv); G2 (ii) partición natural; G5 (iii); G7 (i) CITED orden ≥5; G12 (iii)/(i) | como LABELS |
| CA_G_001 | lema del monoide; SUSY; escalera tipo Elias–Williamson | Lema G1 PROVED (isomorfismo); exclusión vía (R)(10) (revisión), no por thm:shape(A) porque O11 ARGUED, O12 OPEN en P47; §2 REF-D; §3 REF-D/reintento | G1 (iii)-cláusula (R)(10); §2–§3 (iv) | (b) monoide; (c) |
| CA_G_000_REVIEW | — | confirma; FIX alcance de G1 | = | — |
| CA_G_SYNTHESIS | cierre G | — | — | — |

### Frente H

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_H_000_SEEDS | H1–H10; hecho H0 (test +/·) | H0(a),(c) PROVED, (b) ARGUED; H3 plegada en H_001 §1.4; H4 sobrevive O11/O15 y (B′); H7 dirección necesaria; H9 reintento; H10 G1 | H3 (ii)-definicional; H4 (i) O11/O15; H7 (ii); H10 (iii) | (a),(a),(a),(c),(b) |
| CA_H_000_REVIEW | — | confirma; FIX H0(b) | = | — |
| CA_H_001 | p-derivaciones, wronskiano, δ-log de ζ, levantamientos de Frobenius | Props 1.1–1.3, 2.2, 3.1–3.5, 5.1, 5.3, Cor 5.4 PROVED (+CITED); Cor 2.3 PROVED caso producto, ARGUED general; §1.4 «forma ciega al acarreo» PROVED (definicional) | (ii) clases declaradas | (a) |
| CA_H_002 | invariante sucesor (S⁺); Div = Haar, Near = línea − Haar | Thm 2.2 PROVED (de teorema citado); Cor 2.3 O7; Prop 2.4 PROVED; Thm 3.1/3.2 PROVED (extensión de CA_C_002 Prop 2); Prop 3.4 PROVED, lectura ARGUED; Cor 3.5 REF-D | H5 (i) O7 PROVED; H6 (iv) | (a); (c) |
| CA_H_001_002_REVIEW | — | confirma; FIX Lema 4.1(ii) | = | — |
| CA_H_REVIEW | — | autocomprobación línea por línea | = | — |
| CA_H_SYNTHESIS | cierre H | — | — | — |

### Frente I

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_I_000_SEEDS | I1–I10; hecho I0 | I6 automático (tipo exponencial); el resto → memos | I6 (ii) | (a) |
| CA_I_J_000_REVIEW | — | confirma I_000 y J_000; recalcula J0/J0′ | = | — |
| CA_I_001 | Markov / Krein–Rutman / máximo; rigidez «Markov ∀T»; 𝖯⋆ | Thm 1 PROVED; Prop 1.1–1.2 PROVED; Thm 2 (clase 𝒦_M cerrada bajo O2, λ_A→−∞) PROVED; Thm 3 PROVED (fórmula para E racional general ARGUED); Lema 4 (≥2 cambios de signo) PROVED; Prop 5 PROVED; Cor 6 separación, REF-D como ruta | I1 (i) falsificador Λ+c1_{n₀}, fallo PROVED (construcción de tres bumps); I1⋆ (iv) | (a); (c) |
| CA_I_002 | virial, capa de borde, frecuencia, Γ-convergencia, concentración–compacidad | Prop 1.1 (B″) PROVED; Prop 1.2: V3 falsificado por DH con transversalidad ARGUED, V3 es REF-D; Props 2.1–2.3 PROVED (información de borde unilateral, Lema S(iv)); §3 usa cota superior interna CITED (concluye también con cor:margin1 de P47); §4 o(1) absoluto (ARGUED vs margen); §5 I(α)=αL lineal PROVED | I4 (ii) identidades + (iv) V3; I9 (iv); I5 (ii); I7 (iii); I8 (ii) | I4 (a)/(c); I9 (c); I5 (a); I7 (b); I8 (a) |
| CA_I_001_002_REVIEW | — | confirma; Thm 3 hecho nuevo destacado | = | — |
| CA_I_SYNTHESIS | cierre I | O14 abierto (cerrado después en CA_R1_001) | — | — |

### Frente J

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_J_000_SEEDS | J1–J12; Lemas J0, J0′ | J0/J0′ PROVED (valores de núcleo, no de forma); J4 REF-D; J4′ datos de dimensión (O11); J5 reintento PF; J8 una línea; J10 perturbativo | J4 (iv); J4′ (iii); J5 (i) CITED; J8 (iii); J10 (iii) | (c),(b),(a),(d),(b) |
| CA_J_001 | RP reticular por primo; tablero | Thm 1 PROVED (T₀ pequeño, explícito p=2); Thm 2 (RP_p ⟺ soporte de ν en (π/log p)ℤ) PROVED; Cor 3 PROVED (CITED); Cor 4 PROVED p≤7, ARGUED general; Prop 5 PROVED transposiciones | (i) δ_{e_p}: R_p=𝖡(2log p)<0, PROVED | (a) |
| CA_J_002 | GKS (frustración); FKG en retículo de divisores | Lemas 1.1–1.2 PROVED; Thm 1.3 PROVED (incondicional para 2T₀≤0.1); Prop 2.1, Cor 2.2, Prop 2.3 PROVED; Prop 2.4 (Holley) ARGUED | J1 (ii); J2 (ii); J11 (iii) | (a),(a),(b) |
| CA_J_001_002_REVIEW | — | confirma | = | — |
| CA_J_SYNTHESIS | cierre J | — | — | — |

### Frente K

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_K_000_SEEDS | K1–K13 | K3 REF-D; K4 SDP exacto = clase (D); K5 = PSD; K9 requiere RP; K11 reintento; K12 local; K13 perturbativo | K3/K4/K5 (iv); K9 (i) vía J_001; K13 (iii) | (c),(c),(c),(a),(a),(a),(b) |
| CA_K_000_REVIEW | — | confirma | = | — |
| CA_K_001 | diamagnetismo, holonomía, laplaciano con signo | Lema 0, Lema 1.1, Thm 1.2, Prop 1.3, Thm 2.1, Thm 2.2 (orden invertido: λ_A(0.7;0)<0<λ_A(0.7;Λ), entradas CITED), Props 3.1–3.4, Lema 4.1, Thm 4.2 PROVED; Cor 4.3 PROVED con constantes de Cheeger CITED | K8 (ii); K6 (i) falsificador g𝖡 (Prop 3.2, PROVED, clase genérica); K7 (ii) brecha estructural PROVED | (a),(a),(a) |
| CA_K_002 | interpolación de Guerra; desorden; flujo de calor en Ĝ; independencia de sitios | Thm 1.2 PROVED (signo del camino = enunciado del minimizador); Prop 2.1 PROVED; Prop 3.1 PROVED; Thm 3.2, Cor 3.3 PROVED; «Comb_M(s₁) ≤ 0» OPEN (enunciado del minimizador) | K1 (iv); K2 (ii); K10 (iv) | (c),(a),(c) |
| CA_K_001_002_REVIEW | — | confirma | = | — |
| CA_K_SYNTHESIS | cierre K | — | — | — |

### Frente L

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_L_000_SEEDS | L1–L10; tabla V1–V3 | L7 una línea; L9 una línea; L10 reintento | L7/L9 (iii) | (d),(d),(a) |
| CA_L_000_REVIEW | — | confirma | = | — |
| CA_L_001 | función mágica literal; dirección CE; clase de datos modulares | Thm 1.1 (= thm:O como holgura) PROVED; Rem 1.1′ ARGUED; Prop 2.1, 3.1 PROVED; Thm 4.2 (nivel 20) PROVED módulo falsificador O10 CITED; nivel 1 reducido a construcciones sobre el peine | L1 (ii); L2 (i) par de género x²+5y², fallo CITED; L3 (ii) dirección | (a),(a),(a) |
| CA_L_002 | LP de sitios primos; certificados en el toro | Props 1.2, 1.3, Thms 2.1–2.3, Cor 2.4, Props 3.1–3.2 PROVED (2.2 con CITED); REF-D con duales alcanzados | (iv) | (c) |
| CA_L_001_002_REVIEW | — | confirma | = | — |
| CA_L_SYNTHESIS | cierre L | — | — | — |

### Frente M

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_M_000_SEEDS | M1–M8 | M4 reintento; M5/M7 descartadas tras §1.3–§1.4 y probadas en la clase decisiva por §3 | M4 (i) corpus; M5/M7 (ii) clase decisiva | (a),(a),(a) |
| CA_M_000_REVIEW | — | confirma | = | — |
| CA_M_001 | forma en sitios primos; paridad; integralidad; inversión antidiamagnética | Prop 1.1 PROVED; §1.2 (cada Near_q traza 0 ⇒ indefinido) PROVED; §1.3 PROVED; §1.4 ARGUED; Thm 3.1, Cor 3.2, Prop 3.3 PROVED; Prop 4.1 PROVED; Cor 4.2 (i),(iii) PROVED, (ii) ARGUED; Prop 4.3 ARGUED | M2 (ii); M3/M8 (ii)/(iv); M6 (i) O10/O12 (identidad sólo usa FE) | (a),(a),(a) |
| CA_M_001_REVIEW | — | confirma | = | — |
| CA_M_SYNTHESIS | cierre M | — | — | — |

### Frente N y ronda R

| archivo | mecanismo | veredicto primario | base | clase |
|---|---|---|---|---|
| CA_N_000_PLAN | plan V1–V3 | — | — | — |
| CA_N_001 | V1 primal discreto alcanzado | Lema 1.1, Prop 1.2 PROVED; Cor 1.3 «M(T) no acotado» ARGUED; Prop 2.1 PROVED (|X|=2; general ARGUED); Prop 2.2 PROVED, identificación con peine de ceros ARGUED; Prop 2.3 PROVED | (ii) LP de ventana; (iv) sitios | (a)/(c) |
| CA_N_002 | V2 peines positivos | Prop 1.1, 2.2, 2.3 PROVED/CITED; Thm N2 PROVED (para T>½log3 tras FIX); 𝒰_T para T≤½log3 sin decidir | (ii) clase 𝒰_T | (a) |
| CA_N_003 | V3 autoestructura; ensamblaje | Prop 1.1; Thm 3 PROVED (alcance: candidatos declarados); Thm 4 PROVED crecimiento moderado, ARGUED débilmente holomorfo; Thm 5 condicional al falsificador O10 (forma completa CITED, primitiva ARGUED) | (ii) Thms 3–4; (i) O10 para Thm 5 | (a) |
| CA_N_REVIEW | — | confirma; FIX umbral N2 | = | — |
| CA_N_SYNTHESIS | cierre N; residuo: transferencias no unimodulares | — | — | N2r (e) |
| CA_SYNTHESES_REVIEW | revisión de síntesis A–H | avala; precisa: auto-emparejamiento por O7 solo; monoide por (R)(10) | — | — |
| CA_R1_001 | 𝖯⋆: separación vs desigualdad; O14 | §0 criterio de medida de salto PROVED; Props 1.1–1.3 PROVED (O14 cerrado); Prop 1.2 Markov a T pequeño PROVED, T grande OPEN; Thms 2.1–2.3 PROVED; resto no identificante ARGUED; D_∃c OPEN | (iv) por identificación | (c); D_∃c (e) |
| CA_R2_001 | homotopía de amplitud W_F(α) | §1 familia sin ceros PROVED (corrige D8); §2 PROVED; Prop 3.1 NO-GO de clase de método PROVED (modelo de dos átomos); Prop 3.2 puntual FALSO PROVED, integrado ARGUED; Prop 4.1 PROVED término principal, ARGUED completo; §5 REF-D | (ii) clase de método | (a); resto (c) |
| CA_R2_002 | SPEC_A (γ) con margen probado | (1.1) PROVED; (γ) falla con exponente ≥7.72 vs δ≤½ (δ≤½ ARGUED); versión sólo-identidades OPEN | (iii) + margen PROVED | (b); identidades (e) |
| CA_R1_R2_REVIEW | — | confirma los tres | = | — |
| CA_R3_001 | línea θ, L*_j(θ) | Prop Θ, Lema C PROVED; (Ch) CITED; «ADMISIBLE» no avalado → REF-D | (iv) | (c) |
| CA_R3_001_REVIEW | — | REF-D; O7/O9 escapan sólo por identificación | = | (c) |
| CA_R4_001 | L*_j(θ) en ½log5 → ½log7 | Props R4.1, R4.2 PROVED; signo OPEN; NO-GO de método ARGUED; línea viva: continuación exterior de la ecuación de Euler–Lagrange | (iv) + (iii) | (e) |
| CA_R4_001_REVIEW | — | confirma; prealerta: la línea viva es REF-D | = | (e) |

### Documentos de control

| archivo | contenido | observación |
|---|---|---|
| CAMPAIGN_LEDGER | tabla maestra por rondas | coincide con revisiones; registra fe de erratas O1–O15, O14 cerrado, D_∃c |
| README | resumen de fase | coincide con ledger |

---

## 2. Desacuerdos con ANNEX_PHASE_193_LABELS.md

| # | candidata | clase en LABELS | clase según memo primario | razón | cita / línea |
|---|---|---|---|---|---|
| D1 | A1r (Mellin en y / RS en w) | (e) «ABIERTO, nunca desarrollado» | (a) para RS en w con w>1 (= A5); (b) para la continuación a Re w=½; (d) para Mellin en y | CA_A_005 es exactamente RS en w con test del minimizador: positividad w>1 ciega al peine (PROVED); la continuación pierde positividad (PROVED) y su identificación con (S) es ARGUED; Mellin en y sólo recibe una línea ARGUED en CA_A_004 §6 R1 | CA_A_005 §2 Prop 1, §3 Prop 4 «(ARGUED: the off-diagonal part of the continued kernel is not evaluated.)»; CA_A_004 §6: «This is ARGUED, not built.» |
| D2 | A3r (paquete metapléctico fuera de diagonal) | (e) «nunca desarrollado» | (b), absorbida en A4/A4r | CA_A_004 Q3 y Prop 1 tratan justamente el término fuera de diagonal: rango uno por índice (PROVED); la exclusión vía (B′) es ARGUED; lo no excluido es la resolución exacta tipo Kuznetsov = A4r | CA_A_004 §1 «Q3 … No. See §2, Prop. 1: per index n the off-diagonal kernel is rank one»; revisión: «"⇒ estimate (B′)" ARGUED (an exact Kuznetsov-type resolution is not excluded)» |
| D3 | A2 (operador de transferencia) | (b) | (a) para el objeto tal como se formuló — misma base que A4, que LABELS pone en (a) | la revisión excluye por ausencia de Λ (todas las O1–O7, O15 dejan el objeto igual), no por el argumento de conos; lo ARGUED/CITED-UNVERIFIED no es portante | CA_A_002_REVIEW: «EXCLUDED ((R)(1),(3): Λ absent ⇒ invariant under O1–O7, O14, O15 trivially…)» |
| D4 | CD4 (Iwasawa) vs CD3 (Kummer) | CD4 (d), CD3 (a) | misma clase para ambas | ambas descansan en la misma razón de categoría (rangos/valuaciones; ℚ_p no ordenado, CA_C_002 Prop 1 PROVED) más una línea O7 ARGUED; no hay base para separarlas | CA_C_004 D4: «the invariants λ, μ ≥ 0 are ranks and valuations… They carry no real sign (CA_C_002 Prop 1)» |
| D5 | C5L (HM condensado con entrada líquida arquimediana) | (b) «falta clase con entrada líquida» | (c) (y (a) para las partes locales) | CA_F_001 Lema 2 (PROVED) cubre toda completación Hausdorff, líquida incluida: el enunciado condensado/líquido es literalmente el mismo; Prop 4 la asignación local es división convexa (REF-D); la revisión eleva a PROVED | CA_F_001 Lema 2: «Suppose q is continuous for a p-liquid (or any Hausdorff) topology … q ≥ 0 on V ⟺ q̂ ≥ 0 on V̂»; CA_F_001_003_REVIEW: «upgrade from my F_000 review's ARGUED» |
| D6 | C7 ((Fam_η) = T*₃(η), η>2/3) | (d) «dato numérico; no examen de signo» | (b) | examinada en tres memos (C_003, C_005, C_007): reducción a un escalar PROVED; separación de falsificadores NUMÉRICO (x²+5y² positiva en la familia; Beurling negativa); exclusión como paso de signo por thm:shape(C) con falsificador NUMÉRICO — misma situación que C8 | CA_C_007 §6: «Its positivity is FE-generic (NUMÉRICO …), so it is excluded as a sign step by O10» |
| D7 | CE6 (identidad del lado de ceros para la familia) | (d) «no desarrollada» | (b) (clasificación hecha, mecanismo ARGUED) | fue la tarea principal de CA_C_007 §1: identidad PROVED; «criticidad producida por ceros» ARGUED | CA_C_007 cabecera: «coordinator: make E6 the main task»; §1 «Label: ARGUED (the identity is PROVED…)» |
| D8 | CE1 (o-minimalidad) | (a) «falta sólo redactarla» | (b) | el memo y la revisión lo etiquetan ARGUED; por la regla del propio LABELS, lo no redactado no es (a) | CA_C_006 E1: «semialgebraic (ARGUED)»; revisión: «"never constructed → pre-screened NO-GO (ARGUED)" ENDORSED» |
| D9 | F6 (leyes de Weyl / calor) | (d) | (c) | CA_F_003 Prop 2 (PROVED) incluye explícitamente invariantes de calor/Weyl entre los invariantes unitarios = datos espectrales; además reintento DEAD R164_502 | CA_F_003 §3: «This covers Floer homology, capacities, signatures, A¹-/GW-degrees of real forms, and heat/Weyl invariants (F1, F2, F4, F6, F12)» |
| D10 | F7 (traza de Selberg / horociclos) | (d) | (a) para la forma exacta (clase TF⁺, = F16); (B′) para tasas | CA_F_002 «develops F6, F7 and F14 … in their exact forms»; NO-GO PROVED para TF⁺; horociclo exacto en abscisas 0 y 1 | CA_F_002 cabecera y §3 |
| D11 | F13 (tilting perfectoide) | (d) | (a) en la parte local; el resto es G-F (e) | CA_F_003 §4: la parte local es CA_F_001 Prop 3 (PROVED); no produce superficie | CA_F_003 §4: «F13 … local at one p … The local part is CA_F_001 Proposition 3» |
| D12 | H3 (acarreos / Witt) | (b) «falta enunciado probado de ceguera» | (a) (definicional) / (c) por su único canal (Near = H6) | el memo enuncia la ceguera y la etiqueta PROVED: el objeto forma = (factor Γ, peine), ningún C_p(a,b) entra; las sumas de índices sólo entran por Near | CA_H_001 §1.4: «Carries (seed H3 folded here; PROVED) … no quantity C_p(a,b) for a pair of integers enters the definition» |
| D13 | I9 (capa de borde) | (b) «falta prueba de transversalidad DH» | (c) | la transversalidad DH pertenece a I4 (V3), no a I9; I9 descansa en Props 2.1–2.3 PROVED: la información de borde sólo acota desde arriba (Lema S(iv)) y es genérica de clase (muere en O7) | CA_I_002 §2 Prop 2.2 «bounds the Schur margin from above … a lower bound on λ_A needs 𝔰_j ⪰ 0, the target (REF-D)»; §7.1 «Prop 1.2(V3) DH falsification relies on a transversal DH crossing: ARGUED» |
| D14 | I8 (concentración–compacidad) | (b) «redactar como lema» | (a) | la prueba (I(α)=αL lineal ⇒ sin subaditividad estricta) está escrita y etiquetada PROVED | CA_I_002 §5 «(PROVED inadequacy)» |
| D15 | I5 (frecuencia de Almgren) | (a) «Prop 2.2 PROBADA» | (a), pero por otra razón | Prop 2.2 es de I9; I5 descansa en §3: frecuencia acotada ⇒ decaimiento polinomial, incompatible con la cota superior exponencial de P47 (cor:margin1); la cita interna superexponencial no es necesaria | CA_I_001_002_REVIEW: «with only P47 cor:margin1 the frequency is still ≥ 15.449T-scale, conclusion (R)(6) unchanged» |
| D16 | J11 (Holley) | (a) «clase de igualdad J2» | (b) | la Prop 2.4 que la trata está etiquetada ARGUED | CA_J_002 Prop 2.4 «(ARGUED)»; síntesis: «linear in Λ and local (Prop 2.4, ARGUED)» |
| D17 | K7 (laplaciano con signo / Cheeger) | (b) «pérdida ARG/NUM» | (a) | Thm 4.2 PROVED (se exige 1−O(1/M)); Cor 4.3 PROVED con constantes de Cheeger CITED (≤½); no hay NUMÉRICO | CA_K_001_002_REVIEW: «Cheeger constants CITED, structural gap PROVED» |
| D18 | M7 (arcos de Vinogradov) | (b) «falta probar peso despreciable fuera de θ≈0» | (a) en la clase decisiva (igual que M5) | §1.4 es ARGUED, pero el veredicto final se apoya en Thm 3.1/Cor 3.2/Prop 3.3 (PROVED): la aritmética de sitios no tiene información y los desplazamientos acotados pesan cero | CA_M_001 §6: «M5/M7: DISCARD (resolution; PROVED in decisive class)» |
| D19 | E8 (Golden–Thompson) | (a) | (a) sin compresión; (b) con compresión | la igualdad por conmutación vale antes de comprimir; el contenido de la compresión se declara «territorio cerrado» sólo ARGUED | CA_E_000 E8; CA_E_SYNTHESIS «(ARGUED)» |
| D20 | CE2 (probabilidad libre) | (a) | (a) para libertad exacta; (b) para libertad asintótica | conmutativos ⇒ no libres PROVED; el caso truncado y el argumento [crit]/O5 quedan ARGUED (FIX) | CA_C_006 E2 «ARGUED: asymptotic freeness fails»; revisión FIX (2) |
| D21 | §17 ítem 12 de LABELS (celda central con la herramienta CA_D_001) | propuesto como objetivo | contradicho por la fuente | CA_D_002 Thm 2′ (PROVED) muestra que la clausura del cono transferido es doblemente exponencialmente pequeña en la celda central; CA_D_003 §2 cierra los cinco residuos en {Z_T²<1}; la herramienta es ciega justo allí | CA_D_002 §2.2 «CA_D_001 proves the sign where the Hardy amplitude is large … Row D asks for it with amplitude one» |
| D22 | B4 (transporte J(σ)) | (a) | (a) para la convexidad a través de σ=1; residuo sin registrar | (W_σ) en [½,1) para g_X quedó OPEN (sólo «falso genéricamente» ARGUED); el polo no lo excluye en [½,1) y CA_B_006 §3 probó que el transporte de g no usa ceros | CA_B_004 §3 «Status: OPEN for g_X; ARGUED false as a comb-generic statement» |

Coincidencias que conviene anotar (no son desacuerdos de clase): G1m, H10, G5, G12-monoide, J4′ siguen en (b) — la
revisión primaria dice «PROVED as a (R)(10) exclusion», pero (R)(10) es una cláusula y no un falsificador con fondo
negativo; con la regla de cierre de LABELS la clase (b) es correcta. I4 en LABELS como (a)(B″) es correcto para las
identidades; la afirmación «DH falsifica V3» es ARGUED, y V3 es de todos modos REF-D.

Total: **22 desacuerdos** (D1–D22): 7 en que el cierre es más débil que lo registrado (D1, D2, D8, D16, D19, D20, D22);
11 en que el memo sostiene un cierre más fuerte o una reformulación probada (D3, D4, D5, D9, D10, D11, D12, D13, D14, D17,
D18); 2 filas marcadas (d) que en realidad fueron examinadas en profundidad y quedan en (b) (D6, D7); 2 correcciones de
razón o de recomendación (D15, D21).

---

## 3. Descartes más débiles que lo registrado y objeto que falta

1. **A1r — continuación de RS en w a Re w = ½.** Falta: (a) evaluación exacta del núcleo continuado fuera de la diagonal
   (CA_A_005 Prop 4 sólo lo identifica en la diagonal); (b) una positividad del núcleo continuado que no sea norma ni
   segundo momento. Para Mellin en y: un primer examen real (hoy una línea).
2. **A3r/A4r — resolución exacta tipo Kuznetsov en peso ½.** Falta: una desigualdad del lado de sumas de Salié que falle
   para a_P y sea estable a escala λ_A; sin ella la fórmula exacta es genérica en el espectro de Γ₀(4) ((B″)).
3. **B4 residuo — (W_σ) en [½,1).** Falta: la desigualdad de Wirtinger ponderada ∫ω″|g_X|² ≤ 4∫ω|g_X′|² en [½,1) con
   control del polo. Aun probada, cubre sólo I_ζζ (una de cuatro piezas, EI_002): valor bajo.
4. **C1 — división de Hasse–Minkowski ponderada.** Falta un lema escrito: para T ≥ 0.60 y toda (c_p), Σc_p ≤ 1, existe
   F ∈ P_T con 𝔞_∞(F) < 0 y 𝔮_{p,T}(F) > c_p𝔞_∞(F) para algún p con c_p > 0 (por ejemplo, F en el cono negativo de 𝔞_∞ con
   c_F(log p) = 0 para un primo p); hoy la muerte es ARGUED.
5. **CD2 — racionalidad de ζ(2k)/π^{2k}.** Falta el testigo explícito: un cuarteto con parámetros racionales y fondo
   negativo en alguna ventana (lem:shape-quartet con parámetros en un conjunto denso).
6. **CE1 — o-minimalidad.** Falta redactar el lema: el conjunto {xy/z ∈ (a,b)} es semialgebraico y su parte trascendente
   es vacía, por lo que el conteo de Pila–Wilkie no aporta; más el enunciado (B′) para los conteos.
7. **C7/C8/CE6 — familia η.** Falta: prueba manual de s_M = κM + O(1) con κ > 0 (sugerida en CA_C_007), y prueba (no
   numérica) del signo de s_M para x²+5y² y para un sistema de Beurling. Es enunciado necesario, no ruta.
8. **E1 — KMS.** Falta: lema de que β complejo no define estado ni forma positiva útil, y un falsificador probado en lugar
   de la densidad O11.
9. **E9, F5, J4′, J10, K13, I7.** Falta, respectivamente: falsificador propio (E9); prueba de que la hipótesis de firma
   del espacio completo falla (n₋ del espacio completo > 2, información tipo thm:inertia-nogo) (F5); falsificador probado
   para datos de dimensión (J4′); comparación explícita de la pérdida perturbativa con el margen probado
   4·10⁹Te^{−15.449T} (J10, K13, I7).
10. **Grupo que depende del falsificador O11/O12 (G1m, H10, G5, G12-monoide; también parte de E1).** Un único lema
    cerraría varias filas: **un falsificador de Beurling (O11) o de ζ_K (O12) con fondo negativo PROVED**. Hoy O11 es
    ARGUED y O12 OPEN en P47.
11. **Grupo que depende del falsificador O10 en la forma primitiva (D2 como paso de signo, L2, N3 Thm 5, M6, C7/C8).** Un
    único lema reforzaría todas: **fondo primitivo negativo PROVED para x²+5y²** (hoy CITED para la forma completa, ARGUED
    para la primitiva; NUMÉRICO en CA_C_007 para la forma completa).
12. **I1g — Markov para E racional general.** Falta la contabilidad de fórmula explícita para E general (confirmada sólo
    para cuartetos).
13. **J11 — Holley.** Falta la prueba de Prop 2.4 (linealidad en Λ y separación por coordenadas en la clase decisiva).
14. **R4 — paso L*_j(θ) en ½log5 → ½log7.** Línea viva: continuación exterior de la ecuación de Euler–Lagrange (SPEC_A §3);
    prealertada como REF-D. Objeto que falta: una identidad que evalúe 𝔄_j^{−1} sobre el campo exterior de cuatro átomos.

Residuos presentes en la fuente que LABELS no recoge:
- **Medias de Fejér en puntos y ∈ Ĝ ∖ ι(ℝ)** (CA_E_001 Cor 1.1): familia de tests nunca usada (cajas de divisores torcidas
  por funciones completamente multiplicativas unimodulares fuera de la línea). Bajo el objetivo son ≥ 0; un valor negativo
  sería falsificador. No calculado.
- **Factorización de Schur a M fijo** 𝔸_M = 𝔾_M ∘ 𝔹_M (CA_E_001 Remark (scope)): no excluida; y factorización de tipo
  línea ν = ν₁ ∗ ν₂, excluida sólo ARGUED.
- **Índice firmado de Cayley** (corpus 632): sin construir (CA_A_007, CA_A_008, síntesis A).
- **Propagación (M)** en general (L2_027): sólo su instancia Maass–Selberg/Hecke cerrada (CA_A_006).
- **Comb_M(s₁) ≤ 0** en el vector inferior de 𝔸_M (CA_K_002 Thm 1.2): OPEN, enunciado sobre el minimizador.
- **Cota superior tipo Courant** del número de cambios de signo de h* (CA_I_001 Lema 4): OPEN.
- **Caso ε = −1** del auto-emparejamiento (CA_B_003 Cor): OPEN.
- **Clase 𝒰_T para T ≤ ½log3** (CA_N_002): sin decidir (irrelevante donde el signo ya está probado).
- **Resto no identificante de 𝖯⋆**: clase {a = Λ, 0 ≤ K ≤ ν} (CA_R1_001 §2), no estable en signo, ARGUED.
- **Correspondencias no gráficas** (Hecke, escala) para G-F (CA_H_001 Cor 5.4, alcance): fuera de 𝒦_δ, OPEN.
- **Lectura directa de una referencia de la brecha G-F** (CA_F_003 §1, último ítem): pendiente, baja prioridad.

---

## 4. Lemas PROVED reutilizables hallados en los memos

Los que dan positividad o reducciones exactas útiles para el signo:
- **CA_D_001 Thm 1 / 1′ / Cor 1.1.** Para F ∈ P_T: (1/π)∫Θ_X′|F̂|²Z_T² = 2∫_T^∞u(|R_E|²+|R_O|²) ≥ 2Tρ_F ≥ 0; desigualdad de
  valor medio ∫|F̂|²|ζ(½+iτ)|²e^{−2C_X} ≥ ∫|F̂|². Cota en la celda central: Z_T² ≤ 6.6e^{−√2B_X}.
- **CA_D_002 Thm 2′.** Elementos de la clausura del cono transferido son ≤ ε·η_T en |τ| ≤ π/(8T) (sin ceros).
- **CA_N_002 Thm N2.** Para T > ½log3 no hay multiplicador unimodular con fase de ventana que haga unilateral (WF̂)ˇ;
  cota φ′ ≥ T − 1/(τ²+¼).
- **CA_I_001 Thm 1.** La forma (sin término polar) es Markov que mejora positividad; λ_A > λ₀ estrictamente.
- **CA_I_001 Thm 3 + CA_R1_001 §0.** Markov en T ⟺ medida de salto J_T = ν − K + ½Σv_nδ_{log n} ≥ 0; todo ξE entero con E
  racional no constante deja de ser Markov para T grande.
- **CA_C_007 Lema 1, Prop 3.** Bloque de cola de la familia η = ventana pequeña con A_t ⪰ λ_A(T_eff)G_t; positividad en la
  familia ⟺ un escalar de Schur s_M ≥ 0.
- **CA_E_001 Thm 1, Cor 1.1, Thm 2.** Vectores producto (Euler) bastan; forma de medias de Fejér en Ĝ; no hay factorización
  de Schur con factor de producto sin átomos o absolutamente continuo.
- **CA_K_002 Thm 3.2, Cor 3.3 / CA_M_001 Thm 3.1, Cor 3.2.** Cualquier conjunto discreto de sitios con cocientes
  consecutivos → 1 es decisivo; en sitios primos Div ≡ 0 y el objetivo es Arch ≥ Near; la aritmética entera de los sitios
  no aporta información.
- **CA_L_002 Prop 1.2, Thms 2.1–2.3, Cor 2.4.** LP en el toro: s^TM_Xs = (𝖡(0) − η(𝕋^X)) + ∫|P_s|²dη; dual alcanzado;
  holgura en Z_s; exacto para |X| ≤ 5; dual tipo Grothendieck.
- **CA_H_002 Thm 3.1/3.2.** Div = ∫g_s dHaar, Div + Near = ∫g_s dν₀ en Ĝ; anatomía Σ_q[α(log q)N_s(q) − c₀(log q)M_s(q)].
- **CA_M_001 Prop 4.1.** m(τ) + 2Re(ζ′/ζ)(½+iτ) = 0 fuera de ordenadas (sólo FE); C₀ = −2ζ′/ζ(½).
- **CA_R3_001 Prop Θ / CA_R4_001 Prop R4.1–R4.2.** En el paso de Schur, la parte de densidad y la polar se anulan
  exactamente en P_{T_j}; (Ch) + posiciones ≡ datos en cada contacto.
- **CA_R2_002 (1.1).** 𝔰_j(e_min) ≤ λ_A(T_{j+1}) ≤ 4·10⁹T_{j+1}n_{j+1}^{−7.7245}.

Coordenadas y obstrucciones probadas (útiles para filtrar): CA_A_001 Lema 2; CA_A_003 §2; CA_A_005 Prop 2; CA_A_006 Thm 2;
CA_A_007 Lema 1, Thm 2; CA_A_008 Lema 1; CA_B_003 Thm 1; CA_B_004 Prop 1 y (3.1); CA_B_007 Prop 1(a); CA_B_008 Thm 1;
CA_C_001 Lemas 2–4, Thm 1; CA_C_002 Props 1–2; CA_F_001 Prop 3; CA_F_002 Lema 1; CA_F_003 Prop 2; G0, G1; CA_H_001 Props
1.1–5.3; CA_H_002 Thm 2.2; CA_I_001 Thm 2, Lema 4, Prop 5; CA_J_000 J0/J0′; CA_J_001 Thm 2, Prop 5; CA_J_002 Thm 1.3, Prop
2.1; CA_K_001 Thm 2.1–2.2, Prop 1.3, Prop 3.2, Lema 4.1, Thm 4.2; CA_K_002 Thm 1.2, Prop 2.1; CA_L_001 Thm 1.1; CA_M_001 §1.2,
Prop 3.3; CA_N_001 Lema 1.1, Prop 2.1; CA_N_003 Thms 3–4; CA_R1_001 Thms 2.1–2.3, Prop 1.3; CA_R2_001 §1, Prop 3.1.

---

## 5. Cobertura

- Archivos en la carpeta: **128** `.md`.
- Leídos completos: **128** (todos los memos CA_*_001 en adelante, sus revisiones, las tablas de semillas CA_*_000 y lotes
  CA_C_004/006, síntesis, CA_SYNTHESES_REVIEW, CAMPAIGN_LEDGER, CA_A_000_INDEX, README).
- No leídos: ninguno. Ningún archivo ilegible.
- Fuera de la carpeta no se leyó nada salvo ANNEX_PHASE_193_LABELS.md; las referencias de los memos a P47 y al índice de
  rutas se tomaron tal como las citan los memos y sus revisiones, sin verificarlas contra P47.
