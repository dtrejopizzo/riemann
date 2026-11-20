# Triage D — lista 4 (ítems 124–164, fases 170–211)

Ámbito: ideas de la fila D anotadas en el corpus como propuestas y nunca llevadas a término, o abiertas con una
condición de reapertura escrita. Filtro aplicado: F1 (Lema T, controles 2Λ, borrado de una potencia de primo,
peso tipo Beurling), F2 (Arch y peso salen del mismo objeto en el mismo paso; a_T(1) < 0), F3 (formatos afines en
el peso, Gram/Schur, piezas por primo, cambio de operador de referencia), F4 (margen doblemente exponencial),
F5 (una reformulación no es un mecanismo). «IDX l.N» remite a `05-meta-and-planning/ROUTES-MASTER-INDEX.md`.
Donde la fuente nombra la hipótesis clásica se escribe [H]. Esto es un triage: no se deriva ni se calcula nada.

## §1 Tabla

| nº | idea (una línea) | fuente | clase | motivo y cita |
|---|---|---|---|---|
| 124 | VIR–LB: cota inferior virial vía levantamiento Wronskiano; derivada covariante (8.2) | phase-170/R170_844 | CIEGA | El levantamiento estático da el signo opuesto a VIR–LB (R170_844 l.113–125); lo que queda es una cota del virial de la propia forma (energía auxiliar sin mecanismo nuevo). Familia virial/Kato listada en IDX l.470 (residuos R170). Cualquier cota virial que use sólo la forma es afín en el peso (F3) y sobrevive a 2Λ. |
| 125 | (REG) regularidad C¹ de la familia de formas; RES–WARD (sándwich resolvente) | R170_857, R170_858 | REF | (REG) es una hipótesis técnica de regularidad; el sándwich de Ward es una representación del residuo (R170_858 §0: «VIR–LB and D remain open»). Ninguno tiene lado independiente. IDX l.470. |
| 126 | Teorema cuantitativo que construya un testigo negativo desde el desacople Euler–Poisson, o ley de signo para (5.1) con totalización canónica | phase-172/R172_FINAL §§6–7 | CERRADA | El propio memo prueba el trilema de ventana (Prop. «window trilemma», PROVED / NO-GO, l.185–220) para la reparación simultánea; lo restante es pedir un falsificador (no una prueba de signo) o una «ley de signo» sin objeto. R172-candidate en IDX l.470 como residuo ARGUED; F5. |
| 127 | Operador de retorno semilocal: tipado (3.6), límite (4.2), contractividad (4.3), factorización (4.4) | phase-183/R183_003 | CERRADA | Cabecera: R183_014–016 retiran su uso como reducción; el sándwich es indefinido para todo test liso no nulo (IDX l.15493–15499). Clase: contracción Poisson cola→cola, ARGUED/PROVED por indefinición. |
| 128 | Cancelación Poisson–Tate de fibras (3.4) y cuadrado finito (4.2) | R183_005 | CERRADA | La ortogonalidad por primer cruce está REFUTADA en el memo (IDX l.15502); (4.2) es un cuadrado finito de cocientes, Gram de vectores construidos desde F: F3 (Gram válido para todo peso o circular). |
| 129 | Cálculo numérico de ρ_S para S={∞,2}, |s|∈[50,500]; (L-C) sin positividad de Weil | R183_021 | LOCAL/NUMÉRICA — no decide nada | Decidiría sólo (CF-S), ya juzgada «most likely false» (R183_027) y falsa en el modelo de dos bordes (R183_025 Cor 2.2); (L-C) ∀T es REF (IDX l.15511). Coste: evaluar ξ_S en una banda, horas. |
| 130 | Conj G: sentencia no convexa, no de conteo, sensible al borrado | phase-185/R185_002 | REF | Es una descripción de la clase donde tendría que vivir un mecanismo (negativo de Thm C/Thm F), no un objeto; cubierta por OBJECT_SPEC (sensibilidad al borrado) y RULES_AVOID A/E. IDX l.15627. F5. |
| 131 | (iii-c) frontera θ ≤ ⅓ sin soporte en log ℕ; exhaustividad de 𝔐_Λ | R185_004 | OTRO OBJETO | Pregunta de rigidez sobre sistemas discretos generalizados (falsificadores de clase), no sobre la forma a_T en P_T; BF^disc «no toca la forma» (IDX l.7178). |
| 132 | Selector ρ3 sin clasificar; N-U2 «producir K*_π desde Λ» | R185_005B | REF | (★_π) es, por la identidad (1.1) verdadera, equivalente a un enunciado sobre el lado espectral (R185_005B l.86–132); producir K*_π desde Λ es pedir el certificado mismo. Nodo RETIRADO (l.29). |
| 133 | L-TB1.0: flujo de Kreĭn en (½log2, ½log3]; Schur de modos de borde | phase-186/R186_004 | CERRADA | «The flow is not a tool for L-TB1.0» (IDX l.15726–15733); además el signo en T ≤ ½log3 ya está probado en P47; el margen está en el acoplamiento J/M/J′ (R186_019). Sin reapertura. |
| 134 | ¿‖PF_SP‖ < 1 en λ = 1? | R186_013 | CERRADA | Cerrada numéricamente en R186_018 (IDX l.15735–15745). ρ*(T) es REF-D (IDX l.3972). |
| 135 | (L1),(L2) y LP sectoriales en ½log3; ruta 4×4 con intervalos | R186_019 / R186_100 | LOCAL/NUMÉRICA — no decide nada | Certificado en un solo T ya cubierto por P47 (signo probado en ½log3); sectores descartados (−0.637), acoplamientos necesarios (IDX l.15751); Schur44 a lo largo de T NO-GO (IDX l.3886). F4. |
| 136 | Residuo ρ1‴ de la barrera BR (tests no compactos, ba(𝔉)) | R186_037 | REF | «Closing ρ1′ reaffirms the barrier; it opens no positive route» (R186_037 l.18); ρ1‴ es una hoja de la barrera relativa con falsificador escrito (Ex. F). IDX l.3808. |
| 137 | Lema H′: K ≤ N(T*) + O(1) direcciones de cabeza | R186_040 | REF | Cota de conteo de direcciones de cabeza; no da signo (Pos y Neg iguales a 11 cifras; NO-GO de fuga en la clase declarada, IDX l.15774). Un conteo de inercia no decide el signo del último modo (F4). |
| 138 | (COMP) V_X = 𝒫_T para la medida nodal de Gauss; casilla S2 | R186_041 | OTRO OBJETO | Completitud de un sistema de muestreo construido sólo desde σ_T («No contact with the sign», R186_041 l.15); evidencia numérica parcial negativa. Sin peso: F1 ciega si se usara para el signo. Familia PF/nodal DEAD (IDX l.5751). |
| 139 | Autovalor extremo de W_T(σ_β) en el cruce de inercia | R186_042 | CERRADA | Teoría de meseta NO-GO como objetivo; modelos sólo desde σ dan signo erróneo (Lema 3.1, Prop 4.1 PROVED); criterio local NO-GO (IDX l.3925, l.15791). La caja nueva es un valor en un T (cruce) = F4. |
| 140 | D3 (diccionario a nivel λ) para λ > 1 | R186_017 | OTRO OBJETO | Verificación técnica (Frullani, signo para b > 1) de una identidad de traza; herramienta de Sonin semilocal sin efecto en el signo; ρ* REF-D (IDX l.3972). |
| 141 | ¿Maximizador de C/Son_S = autovector inferior de Son_S?; RB(T); n₋(−C) | R186_101 | CERRADA | «1−λ₂(A_S)² NO-GO», «s₀ = continuación … NO-GO», 1D(T) NO-GO como reducción de RB; FATAL-2 n₋ no robusto (IDX l.15760, l.15865). RB(T) es REF. |
| 142 | Test preregistrado de cuatro ventanas de la ley −ln λ_A ≈ 2πN(T*)+δ | phase-187/PREREG_LAW_TEST | LOCAL/NUMÉRICA — no decide nada | Ajuste de tamaño del margen; W-pat NO-GO como ruta (IDX l.3927, l.15968). Coste: λ_A en 4 ventanas a M ≥ 120 con precisión extrema. No toca el signo (F4/F5). |
| 143 | F_k ∈ P_T con partes aleatorias de rezagos disjuntos | phase-188/L2_BUILD_022 §3 | CERRADA | Resuelto por L2_BUILD_023 Lema L (IDX l.12812, l.12950: Thm T, sólo necesario). |
| 144 | (Ω_EM)/(Ω_μ); norma no absoluta desde el cono de autocorrelaciones | N_BUILD_005–007 | CERRADA | N_007 §3: NO-GO PROVED (resolvente indefinido en el orden del cono); prop:cone NO-GO (IDX l.3874; meta-teorema N_018, l.5761). |
| 145 | Reducción 𝒯₀ → (E₀) condicionada a concentración del minimizador | L2_BUILD_008 §5 | REF | (E₀) es el caso borde de (E_γ) de P47: reformulación asintótica; la hipótesis de concentración es el dato faltante. Estado fundamental de la parte arquimediana: además F2. |
| 146 | Intervalo (0.8047, T_loc]: signo de Π_T(F_odd) | L2_BUILD_004 | OTRO OBJETO | Es negatividad de 𝔞_T en L²(I_T) sin las restricciones de P_T (L2_004 l.79–90); a_T(1)<0 ya excluye L²(I) (F2). Umbral 0.8047 corregido a 0.74921 (IDX l.165). |
| 147 | Signo de I_{2,3}; «cubo × ventanas»; segundo momento 𝒱²; direcciones casi autoduales | L2_015 §2; N_004 §3; N_010 §4(2) | CIEGA | Interacción par de primos y segundo momento: piezas por primo/pares con signo propio (F3, fallan pasado T≈0.697); 𝒱² NO-GO ARGUED (IDX l.4004); «(Q) mal planteado» (IDX l.3869). IDX l.16140. |
| 148 | Clasificación de amplitudes admisibles A ≥ 0 | phase-193/CA_D_002 §3.6 | OTRO OBJETO | Pregunta de análisis de Hardy sobre multiplicadores que preservan una separación de soporte; los tests ponderados no aproximan P_T (PROVED, IDX l.8923–8925); el boceto razona por ceros sobre la línea (fuera del sandbox). IDX l.16283. |
| 149 | Wirtinger ponderada (W_σ) para g_X | CA_B_004/006 | CERRADA | ARGUED falsa en genérico (fuente); cualquier Poincaré/Wirtinger es arquimediana y ciega al peso (F1/F2). IDX l.325, l.517. |
| 150 | Signo de medias de Fejér en y ∉ ι(ℝ) del solenoide, S pequeño | CA_E_001 §7 | LOCAL/NUMÉRICA — decide algo | Búsqueda de falsificador no ejecutada («Not computed», l.56). Decide si el objetivo producto (eq:target) de CA_E_001 falla fuera de ι(ℝ): sólo poda esa reformulación; no prueba signo. Ver §3. | [Corrección, ROUND_024_C: por densidad de ι(ℝ) (Kronecker) el ínfimo fuera de la recta es el de la recta; no decide nada.]
| 151 | Transferencias no unimodulares con peso en u≠u; 𝒰_T para T<½log3 | CA_N_SYNTHESIS, CA_N_002 §4 | REF | Esperado Gram/G0 (REF-D) según la fuente; T<½log3 «irrelevante al signo» (IDX l.16437). F3 (Gram). |
| 152 | Clase {a = Λ, 0 ≤ K ≤ ν} | CA_R1_001 §2 | CERRADA | El propio memo muestra que no es estable en signo: K concentrado baja 𝔞_T en ≍∫ν|c_h| ≫ margen (IDX l.16449). F4. |
| 153 | Término polar amortiguado G1; localización vs subordinación G3 | phase-194/INV_A_001 | CERRADA | Lévy–Khintchine clásico (= P60-1), RETRY de R162_2601c, Θ⁺ FALSO, G2 circular (IDX l.5961, l.9091). G1 es un cálculo finito de normalización en un esquema ya clasificado. |
| 154 | Comb_M(s₁) ≤ 0 en el camino arquimediano → completo | CA_K_002 §1 | REF | Enunciado sobre el minimizador de la forma completa; «deterministic path sign = minimizer statement» (IDX l.13539). |
| 155 | Cota superior de cambios de signo del minimizador (Courant no local) | CA_I_001 §4 | OTRO OBJETO | Propiedad de toda forma de Markov (clase Thm 2, fuente l.100): no distingue Λ de los controles (F1); nodal/PF DEAD (IDX l.5751). |
| 156 | Portador con peso |ξ_S|² en σ=½; requiere (L1) fuera de la ventana | phase-195/INV_R_001 | CERRADA | Lema de normalización «only if» FALSO (AUDIT_4); Hermite–Biehler falso en (½,1) para todo S y Beurling; NO-GO 𝒦_R (IDX l.5967, l.632). |
| 157 | Cota cuantitativa de κ̃_T en la clase 𝓔^{≥log2} | phase-197/REVIEW_BARRIER_EST_001 | OTRO OBJETO | Pieza de un teorema de barrera sobre estimaciones (no del signo); 𝓔 casi tautológica (IDX l.5975). |
| 158 | D_even como mitad vinculante; Beurling/Ξ_Q/O_6+ en el sector impar | phase-198/AA_001, AUDIT_198 | CERRADA | División por paridad NO-GO: «no reintentar la división por paridad como mitad» (IDX l.5982); D_even es REF. |
| 159 | ε explícito en W1′ (n₋=0 en (0,T₅+ε)) | phase-197/BARRIER_W_001 | LOCAL/NUMÉRICA — no decide nada | Extiende el signo un ε pasado ½log5 (ya superado: frontera ½log15). Un rango finito más no toca ∀T (las reglas del proyecto: «no acumular órdenes finitos»). |
| 160 | Separador en P_T con muestreo de Cauchy en (2π/log p)ℤ de los primos presentes (O2 al revés) | phase-200/R11_2_ORIGIN_001 «Next lemma» | REF | Un separador distingue ζ de falsificadores; no es una desigualdad. Pedir que un funcional sea ≥0 para Λ y <0 en los testigos a_P es el certificado mismo (F5); la familia peine de un primo / a_P está en SPEC_SIGN_OBJECT_007 (IDX l.9244). Funcional lineal en el peso ⇒ además F3. |
| 161 | Especificación de positivo: 𝒱_b, identidad con FE, B_Λ≥0 sin Q_T≥0, prueba b=Λ vs b^{(p)} | phase-209/REVIEW_TARGETS_002 | REP212 | Es la especificación que OBJECT_SPEC (O1–O17) y RULES_AVOID (A, E, O–AB) de la fase 212 ya incorporan; el memo concluye «OPEN; no candidato» (IDX l.17229). |
| 162 | Cap de densidad tipo Malmquist para ternas de polos ≥31.5 | phase-211/POWER_ARCH_TRIPLE_004 | CIEGA | Positividad arquimediana en un subespacio exponencial: no contiene el peso, sobrevive a los tres controles (F1) y es el esquema «esqueleto arquimediano» (F2). Además superado por POWER_CONFLUENT_004 (IDX l.17316). |
| 163 | Cov_μ(m,R) ≥ (E_μ[R]−r0)p_u en el sector p_u>0; transporte de orden cuatro | POWER_AUDIT_005, POWER_POLAR_MOVEMENT_005 | CIEGA | Identidad ARCH+POLAR sin primos: ciega al peso (F1/F2); su extensión general ya tiene falsificador 4/5−π (IDX l.17327); transportar movimiento a la forma completa no es automático (IDX l.9883). |
| 164 | Paquetes Tate f_n: control unilateral de W_{n+1}−W_n o razón renormalizada | POWER_PACKET_SCOPE_AUDIT_009 | CERRADA | Misma cadena que POWER_TATE_CHAIN_009: límite E0 ya conocido, familia individual no densa (IDX l.7340, l.9903, l.17463). Positividad en una familia no densa no da ∀F ∈ P_T. |

Recuento: CERRADA {126,127,128,133,134,139,141,143,144,149,152,153,156,158,164} = 15; REF {125,130,132,136,137,145,151,154,160} = 9; REP212 {161} = 1; CIEGA {124,147,162,163} = 4; LOCAL/NUMÉRICA {129,135,142,150,159} = 5; OTRO OBJETO {131,138,140,146,148,155,157} = 7. VIVA 0. Total 41.

## §2 Ítems VIVA

Ninguno. Los dos más cercanos a sobrevivir y por qué no:
- 160 (separador por muestreo de Cauchy): el único que la fuente deja como «única dirección viva», pero es un separador, no una identidad «forma = no negativo»; como funcional lineal en el peso cae en F3 y como pedido «≥0 para Λ, <0 en testigos» es F5.
- 130 (Conj G): describe correctamente la clase admisible (no convexa, sensible al borrado), pero no nombra objeto; esos requisitos ya están en OBJECT_SPEC.

## §3 LOCAL/NUMÉRICA que deciden algo

- 150 (CA_E_001 §7). Ejecutar: medias de Fejér multivariadas de φ en puntos y del solenoide Ĝ fuera de ι(ℝ), para S ⊂ {2,3,5}, N pequeño (cajas de divisores torcidas); buscar un valor negativo. Coste: bajo (cajas finitas, minutos). Decide: si aparece un negativo, el objetivo producto (eq:target) de CA_E_001 es más fuerte que la positividad en P_T y esa reformulación queda falsificada; si no aparece, nada se prueba. No decide el signo de a_T. [Corrección, ROUND_024_C: no ejecutar; ver la nota del ítem 150 en la tabla.]

## §4 Lo que no pude abrir o decidir

- 124/125: no leí R170_844 §8 completo (derivada covariante (8.2)); la clasificación se apoya en las secciones de estado y en IDX l.470.
- 143–147: los memos L2_BUILD/N_BUILD se leyeron sólo en las líneas de estado; 147 agrupa tres ideas menores que el índice tampoco desglosa (IDX l.16140).
- 153: no se verificó si G1 (normalización polar amortiguada) cambiaría la conclusión de INV_A_001; se clasifica por el cierre de clase del índice.
- 157: la frontera entre OTRO OBJETO y CERRADA depende de si se acepta que la clase 𝓔 es casi tautológica (AUDIT_7).
