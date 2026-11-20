# Ronda 2 B — La factorización de incidencia [log mcd] = E diag(Λ) Eᵀ actuando sobre F (memo de selección)

Objetivo (★): λ_A(T) ≥ 0 para todo T, con las definiciones de `../phase-211-sign-sandbox/STATEMENT_001.md`.
Candidata: para una familia ℓ_i(F), i ≥ 1, lineal en F (con valores escalares o en un espacio de Hilbert),

    Q_B(F) := Σ_{i,j} log mcd(i,j) ⟨ℓ_i(F), ℓ_j(F)⟩ = Σ_{d≥2} Λ(d) ‖L_d F‖²,   L_d := Σ_{d|i} ℓ_i,      (B)

y la pregunta de si el peine −Σ v_n Re c_F(log n) de a_T, o una parte suya con resto manifiestamente no
negativo, se expresa por (B) con el signo correcto. Abreviaturas: «GRAM» = 211
`POWER_GRAM_SLICES_OBSTRUCTION.md`; «GLOBAL» = 211 `POWER_GLOBAL_ROUTE_REVIEW.md`.
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

### (1) Antecedente más cercano

El antecedente no es sólo la fase 170. La forma (B) con F en los índices ya está escrita en la fase 211,
sobre el portador de escalas enteras, en dos pasos.

a. **GRAM §17.2, identidad (RES-SOS)** (PROVED allí). En cada clase libre de cuadrados d, con coeficientes
   c_a del vector en los nodos k = da², la transformada de incidencia f_q = Σ_{a|q} √a c_a (es Eᵀ aplicada
   al vector) y la identidad Σ_{m|q}Λ(m) = log q dan

       R_res[c]/√d = Σ_q D_q |f_q|² + Σ_q Σ_{m|q, m≥2} Λ(m) I_q |f_q − f_{q/m}|²,   D_q > 0 (§17.3).

   Los pesos de los cuadrados son los Λ(m), la orientación sale del cruce −2Λ(m) I_q Re(f_q conj f_{q/m}) y la
   diagonal la paga el logaritmo arquimediano (D_q). Es la candidata B restringida a las coincidencias
   exactas kn² = lm². Alcance registrado en §17.4: no firma la contribución no resonante.

b. **GLOBAL, «Extensión factorial antes de resonancia: identidad completa con restos firmados»**
   (identidad PROVED allí; signo global OPEN). Sobre la forma completa en y = 0, con b_λ = Σ_{n²|λ} n^{−1/2}
   c_{λ/n²}, K el Gram modal, P_m la selección de índices divisibles por m² y R_m la dilatación,

       Q[c] = Σ_{m≥2} Λ(m) ‖P_m b − R_m b‖²_K + b*Db + E(b).

   El texto dice literalmente que Σ_m Λ(m) P_m*KP_m tiene entrada K_{λμ} log mcd(q_λ, q_μ) (q_λ = mayor
   entero cuyo cuadrado divide a λ): es el producto de Schur de un Gram en F con [log mcd] = E diag(Λ) Eᵀ,
   es decir (B) con ℓ_λ = (coordenada modal λ de F). Resultado registrado: D tiene todas las entradas
   positivas y no es semidefinida positiva; E(δ_1) < 0; ningún C finito da E ≥ −C·(suma de cuadrados); en
   el núcleo de los cuadrados (soporte libre de cuadrados) queda Q = L + M sin primos y la comparación
   suficiente B + M ⪰ 0 es falsa (test exacto en {1,2}). «Control de la sustitución ortogonal en la
   identidad factorial» (PROVED allí): cambiar P_m por la proyección ortogonal hace divergir
   Σ_m Λ(m)‖F − R_mF‖².

c. La selección está además en la memoria de selecciones rechazadas («Cuadrados factoriales y proyecciones
   físicas») y en `RULES_AVOID.md` D9 y D18.

Otros antecedentes consultados.
- Fase 170, R170_863–868 (primarias leídas): incidencia sobre el espacio de coeficientes; ker 𝒟_N = ℝ(Λ,1)
  (866, PROVED); toda fila lineal que anula la línea factoriza por 𝒟_N, también tras tensorizar con el
  espacio físico (868 §§3–4, PROVED). R170_870: pared de paridad para la clase de borde lineal en F.
- Fase 170, R170_201 y R170_301 (leídas en `ANNEX_170_FILES_1.md`): Σ_n (Λ(n)/√n)‖F − U_nF‖² con dilataciones
  unitarias; resto con constante divergente, genérico en los pesos (falsificador a₂ = 100).
- 211/ROUND_003_B (LEDGER C9): la métrica δ = log(mcm/mcd), condicionalmente negativa porque [log mcd] ⪰ 0,
  como multiplicador de Schur sobre 𝔸_M; NO-GO (reformulación, menores negativos explícitos). Su cotejo
  cita la fase 116 (núcleo de mcd como Gram de estados de dilatación); no comprobé la primaria de la 116.
- 211 GRAM §16.4–16.5: la matriz ρ(k,l) = mcd(a,b)/√(ab) es el término principal de A en escalas enteras
  fijas y es definida positiva; no domina uniformemente (pares k, k+1).
- `ROUND_001_B.md` Lema 4 y Prop. 6; `REVIEW_001_ABD.md` §2.3 punto 2: la pieza 2ZDZᵀ (paradigma de mcd con
  g(d) = d log d) es positiva y genérica; falta la operación que firme −(DG + GD) contra Z·Arch·Zᵀ.
- `ROUND_001_C.md` Teorema R, instancia 2 (R-cont de `OBJECT_SPEC.md` §3): ninguno de los cuadrados de
  RES-SOS sobrevive en una identidad exacta única para A_0.
- 211 LEDGER C33b, C49; fase 200 A_MU_FACTORIZATION §1(f) (por IDX README): peine colapsado por Λ∗1 = log,
  forma sin primos, sin paso de signo.
- Grid, crucigrama y Paper 48: sin entrada propia para matrices de mcd fuera de las ya citadas (el grid y
  el crucigrama reproducen las dos entradas de GLOBAL). Búsqueda por gcd, mcd, Smith, meet, lcm, incidencia
  y Ramanujan en `03-research/`: las coincidencias restantes (fases 159, 162, 193) no usan [log mcd] como
  Gram sobre F.

Corrección de registro que resulta del cotejo: la frase «la matriz [log mcd] = E diag(Λ) Eᵀ actuando sobre
F no fue usada literalmente» (`RULES_AVOID.md` I1, nota del `LEDGER.md`, IDX README, lista «no intentado»)
es cierta para la fase 170 y falsa para el corpus: fue usada en 211 (a, b).

### (2) Objeto nuevo

Ninguno que pueda escribirse. Lo que (B) exige y lo que hay:

- ℋ_T y V_T: ℋ_T = ⊕_d (espacio de valores, peso Λ(d)), V_T F = (L_d F)_d. Falta la familia ℓ_i.
- En una suma de cuadrados el único lugar de un término negativo es un cruce (PROVED, trivial). En (B) el
  cruce de i y j lleva el peso log mcd(i,j) ≥ 0, situado en el divisor común, mientras que en a_T el peso
  Λ(n) está en el cociente (el retardo log n de c_F). Pasar el peso del divisor común al cociente obliga a
  cuadrados de dos términos a lo largo de aristas de divisibilidad, ‖(·)_q − (·)_{q/m}‖², con conductancia
  Λ(m): es la forma de (a) y (b). ARGUED (no demuestro que sea la única disposición).
- Las ℓ_i disponibles se reparten en dos clases.
  (i) ℓ_i conmuta con las traslaciones (ℓ_i = x_i U_{log i}, o cualquier multiplicador). Entonces
      Q_B(F) = (1/2π)∫ σ_B |F̂|², σ_B(τ) = Σ_d Λ(d)|Σ_{d|i} x_i(τ)|² ≥ 0, y F entra sólo por su
      autocorrelación (PROVED, una línea). Es un certificado en el sentido de `OBJECT_SPEC.md` O2, de tipo
      suma de cuadrados aritmética (O8; `RULES_AVOID.md` C1 y C3). Con cuadrados de dos términos es
      R170_201/301: deuda diagonal 2Σ_{n<N}Λ(n)/√n ‖F‖², que el símbolo arquimediano no paga.
  (ii) ℓ_i ve la ventana (no conmuta con traslaciones). La única familia escrita en el corpus es la modal
      del portador theta (h_λ, K, P_m, R_m), y da exactamente (a) y (b).
- ρ_T: en (b) es b*Db + E(b). No es manifiestamente no negativo y sus dos piezas tienen falsificador por
  separado (CITED de GLOBAL). No tengo otra ρ_T que escribir.

Sobre los tres orígenes del signo que plantea el encargo:
- **Término arquimediano.** Es D_q de (a) y el factor log(t√(λμ)) de D en (b). Firma la diagonal de la parte
  resonante y nada más.
- **Identidad mcm/mcd.** −log mcd = log mcm − log i − log j. Es la entrada
  log(t√(λμ)) − log mcd(q_λ,q_μ) − S(√t) de D en (b): positiva entrada a entrada, no semidefinida (PROVED
  allí); y es la métrica δ de C9 (NO-GO). No cambia la orientación de forma utilizable.
- **Relación de grado dos Λ·log + Λ∗Λ = μ∗log².** Da [log² mcd] = E diag(μ∗log²) Eᵀ ⪰ 0: de nuevo pesos
  no negativos en el divisor común, sin cambio de orientación. La forma es afín en el peine
  (`OBJECT_SPEC.md` O2) y la relación es la regla de Leibniz sobre Λ∗1 = log (`ROUND_001_A.md` Lema B).
  Los usos registrados (R170_850–851, 856; `RULES_AVOID.md` D17b, término 2V) no dieron signo. ARGUED: no
  encuentro operación nueva; no es un NO-GO.

### (3) Por qué el cambio evitaría la dificultad del antecedente

No la evita.

- **R170_868.** El teorema concierne a la linealidad en los pesos (a, c), no en F. Si ℓ_i y ρ_T no dependen
  de los pesos, (B) es lineal en diag(Λ) y a_T es afín en el peine. La diferencia entre los dos miembros de
  (G), como función de (a, c) con valores en las formas hermíticas sobre el núcleo común, es una fila
  lineal que anula ℝ(Λ,1); por 868 §§3–4 (válido para cualquier espacio de llegada) factoriza por 𝒟_N. Luego
  (G) es un uso lineal de Σ_{d|k}Λ(d) = log k y ρ_T = Arch_T + Σ_k log k · Q_k(F) es una forma sin primos.
  PROVED como aplicación directa de 868. Ser cuadrática en F evita la pared de paridad de 870 (que es para
  funcionales impares), pero no sale de 868: toda la obligación de signo pasa a una forma sin primos, que
  es la situación de C33b y del resto D + E.
- **R-cont.** Si i indexa nodos o modos, L_d = Σ_{d|i} ℓ_i es la torsión por la indicadora de los múltiplos
  de d, excluida por el Teorema R como cuadrado de una identidad única (el P_m de (b) es eso, y por eso el
  resto E no tiene signo). Si i indexa dilataciones unitarias se cae en la clase (i). La variante admitida
  por R-cont con dilataciones no unitarias en la semirrecta es R_m; con la proyección ortogonal en lugar de
  P_m la suma diverge (GLOBAL, «Control de la sustitución ortogonal»).
- **Casi-coincidencias.** (B) agrupa por divisibilidad exacta. Los pares k, k+1 tienen mcd 1 y no comparten
  ningún L_d con d ≥ 2, mientras sus columnas en la forma son casi paralelas (GRAM §16.5, §17.6; `ROUND_001_B.md`
  §4). El contenido de `OBJECT_SPEC.md` O6 queda entero en ρ_T.

### (4) Identidad que conectaría con la positividad global

Sólo la ya registrada: Q = Σ_m Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b) (GLOBAL), o A_0 = R_res + Off con R_res
en la forma (RES-SOS). La positividad global equivale a firmar conjuntamente D + E (respectivamente
Off ≥ −R_res, que en y = 0 es el objetivo completo sin margen, `RULES_AVOID.md` D9). No tengo identidad
adicional.

### (5) Línea que se rompe para cΛ y para a_P

En (B) sola, ninguna: Q_B ≥ 0 para todo peso no negativo. Lo que deja de ser cierto para cΛ y para a_P es la
sustitución Σ_{d|k}Λ(d) = log k (da c·log k, o el logaritmo de la parte de k sin primos menores que P), es
decir la identificación de la diagonal de los cuadrados con el logaritmo arquimediano. Esa línea rompe la
identidad, pero no es un paso de signo: en (a) la parte firmada tiene margen uniforme (GRAM §17.5), de modo
que su positividad no puede romperse para c cercano a 1 (ARGUED; no derivado aquí). El paso de signo estaría
en ρ_T, y allí no hay línea que señalar porque no hay argumento. Por `OBJECT_SPEC.md` §4, la candidata no
está lista.

### Veredicto del cotejo

**Repetición; sin mecanismo nuevo.** La candidata coincide con RES-SOS (GRAM §17.2) y con la extensión
factorial de GLOBAL, ya rechazada como selección. La memo termina aquí; no hay construcción.

## Resultado

**Sin mecanismo nuevo.** No es un NO-GO de clase: no se excluye una compensación conjunta de D + E con los
cuadrados, ni una familia ℓ_i que vea la ventana distinta de la modal.

## Qué se probó

- (PROVED, una línea) Si las ℓ_i conmutan con las traslaciones, Q_B es un multiplicador con símbolo
  Σ_d Λ(d)|Σ_{d|i}x_i(τ)|² ≥ 0 y F entra sólo por c_F: clase de certificados.
- (PROVED, aplicación de R170_868 con espacio de llegada las formas hermíticas) Toda identidad
  a_T = Σ_d Λ(d)‖L_dF‖² + ρ_T con ℓ_i y ρ_T independientes de los pesos es un uso lineal de Λ∗1 = log, y su
  resto es una forma sin primos.
- (CITED, comprobado en la primaria) Σ_m Λ(m)P_m*KP_m = K ∘ [log mcd(q_λ,q_μ)] en GLOBAL: la matriz de
  incidencia sí actuó sobre F en la fase 211.

Nada de esto es avance de signo.

## Qué falló y por qué

- El peso Λ(d) de la incidencia está en el divisor común y el del peine en el cociente; el único puente
  escrito son los cuadrados sobre aristas de divisibilidad, ya construidos.
- Ninguna de las tres fuentes de orientación (logaritmo arquimediano, mcm/mcd, grado dos) da una operación
  que no esté ya en D, en C9 o en el descarte del término de Selberg.
- El resto contiene todas las casi-coincidencias y no tiene signo manifiesto; sus piezas D y E tienen
  falsificadores por separado.
- No puedo escribir ρ_T ni la línea de ruptura de un paso de signo.

## Siguiente paso concreto

Ninguno dentro de B. Para el registro (esta memo no edita otros archivos):
1. Corregir en `RULES_AVOID.md` I1, en la nota del `LEDGER.md` y en la lista «no intentado» del índice: [log mcd]
   sobre F fue usada en 211 (GRAM §17.2; GLOBAL, «Extensión factorial»); sólo en la fase 170 no aparece.
2. Línea de ledger propuesta: «K2′, [log mcd] = E diag(Λ) Eᵀ como Gram sobre F: repetición de RES-SOS y de
   la extensión factorial; sin mecanismo nuevo; no es imposibilidad».
3. Condición de reapertura: una operación explícita que firme conjuntamente b*Db + E(b) con los cuadrados
   factoriales (o Off con R_res) sin separar las piezas, o una familia ℓ_i que vea la ventana, no sea
   selección aritmética de nodos y cuyo resto pueda escribirse como suma de cuadrados o medida positiva.
   No conozco ninguna de las dos.
