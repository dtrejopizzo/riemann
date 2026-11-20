# Revisión de las memos de selección ROUND_001_A, ROUND_001_B y ROUND_001_D

Objetivo de referencia (★): λ_A(T) ≥ 0 para todo T > 0, con las definiciones de
`../phase-211-sign-sandbox/STATEMENT_001.md`. Se rehízo cada demostración, se cotejó con
P47 (`04-papers/47-row-d-dual-certificates/main.tex`: sec:firstcontact, thm:PCfinite, prop:GEgap,
prob:annihilate, prop:annihilate-equiv, rem:returnremarks, prop:opcalc, thm:sos, rem:sosatoms,
prop:nearfree, rem:boxes, thm:oneprofile, prop:AM, lem:shape-scale, thm:geo-split), con 211/LEDGER
(C6, C7, C9, C33b, C49), con `phase-186-toolbox/R186_005` y `R186_092`, con el índice de rutas y con la
fase 170 (`phase-170-global-prime-inequality/R170_811`–`R170_862`), que ninguna de las tres memos cita.
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO. Los cómputos de esta
revisión son comprobaciones de un punto y no prueban nada.

Resumen de veredictos.

| Memo | Veredicto | Defecto más grave |
|---|---|---|
| A (K1) | ACEPTAR con correcciones (mayores en el cotejo y en el alcance) | El Lema A(2) es vacío en el álgebra formal (allí A = 0) y la frase «la orientación entra exclusivamente por los defectos» es falsa; el cotejo omite la fase 170, donde la «pieza que falta» ya está registrada |
| B (K2) | ACEPTAR con correcciones | La lectura de la Prop. 5 («no existe fórmula del pivote obtenida por Λ∗1 = log») es un non sequitur que la propia Prop. 6 contradice; el «se ha probado» del Resultado descansa en un dato NUMÉRICO |
| D (K4) | ACEPTAR con correcciones | El caso (iv) del Teorema B no es un NO-GO, ni siquiera condicional, en la generalidad enunciada: hay instancias verdaderas PROVED |

Ninguna de las tres conclusiones «sin mecanismo nuevo» es una imposibilidad, y ninguna debe
registrarse como tal. Las tres memos lo dicen en su sección de resultado, pero las tres contienen
frases que lo contradicen (señaladas abajo).

---

## 1. Memo A

### 1.1 Verificación de los enunciados

**Relaciones frente a P47.** Las definiciones coinciden con P47 (l. 6627–6665): X, 𝓕 = u_∞(D)J,
𝓕* = 𝓕⁻¹ = 𝓕, JV_aJ = V_{−a}, X + 𝓕X𝓕 = 𝓜, S_N, S′_N, L_M, A_M, E_N = S_N𝓕 − JS_N,
H_{M,N} = L_MS_N − S′_N. Las relaciones (b) S𝓕 = JS y (c) [X,S] = −LS son E = 0 y H = 0. Correcto.
La relación (a) J𝓜J = 𝓜 es la paridad de m. Correcto.

**Lema A(1).** Rehecho: S𝓜𝓕 = SX𝓕 + S𝓕X = (XS + LS)𝓕 + JSX = XJS + LS𝓕 − XJS + L^♭JS
= (L + L^♭)S𝓕. Correcto. La hipótesis (a) no se usa en (1). Con defectos el mismo cálculo da
S_N𝓜𝓕 = JS′_N + S′_N𝓕 + {X,E_N}, que es la demostración de thm:PCfinite. PROVED.

**Lema A(2).** Las cuatro comprobaciones ((𝓕°)² = 1, (b), (c), (a)) son correctas. Además la
sustitución respeta la relación no listada 𝓕t = t^♭𝓕 (t ∈ 𝒯; u_∞(D) conmuta con las traslaciones) y
es compatible con la involución * de la realización (X* = X, J* = J, 𝓕* = 𝓕, t* = t^♭). PROVED como
enunciado algebraico. Defectos:

- **E-A1 (alcance; §3, «Lectura» del Lema A, y §2(iii)).** En el álgebra universal definida por las
  relaciones del lema, la parte (1) da A = 0. Entonces «A ↦ −A» es 0 ↦ 0 y la frase en negrita «el
  álgebra formal de las tres entradas no contiene orientación, en ningún grado» es una trivialidad:
  en esa álgebra toda identidad A = ΣV_i*V_i + ρ dice 0 = ΣV_i*V_i + ρ. El enunciado (2) no añade
  nada a (1) mientras las relaciones sean exactas.
- **E-A2 (el caso con defectos no está demostrado ni enunciado).** Lo que importa es la versión con
  truncaciones. Allí (b) y (c) no son relaciones: definen E_N y H_{M,N}. La tupla especular
  (X, J, J𝓕J, S°, −L_M) satisface thm:PCfinite con A_M ↦ −A_M para **cualquier** S° ∈ 𝒯 (incluido
  S° = S_N), con E° := S°J𝓕J − JS° y H° := −L_MS° − S°′. El «peine de Möbius» sólo interviene en
  dónde se anula H°: con S° = Φ_{≤N}(μ) y M ≥ N, H° no tiene coeficiente en k ≤ N (porque
  μ·log = −Λ∗μ) y fuera sus coeficientes −Σ_{dm=k, d≤M, m≤N}Λ(d)μ(m) no tienen signo (NUMÉRICO, M = 9,
  N = 6: entre −1.95 y +2.71). El enunciado correcto es el Lema A′ de §1.3. Es una reformulación de
  la observación de P47 tras thm:PCfinite (invariancia del cuadrado por A_M ↦ −A_M; código F2); no
  la supera.
- **E-A3 (afirmación falsa; §3, «Lectura», y §4 primera frase).** «La orientación entra exclusivamente
  por la asimetría de los defectos» es falso. La imagen especular tampoco comparte: Λ ≥ 0 coeficiente
  a coeficiente (pesos −Λ), b ≡ 1 ≥ 0 (frente a μ), y la positividad de la medida de Lévy K(u) > 0
  de m (STATEMENT §1; la imagen tiene −m). Ninguna de las tres es un defecto de (b) o (c): son
  propiedades de la realización que las relaciones (a)–(c) no expresan. h_{M,N} ≥ 0 es consecuencia
  de la primera. La lista (α), (β) del §4 está incompleta en consecuencia.
- **E-A4 (el álgebra está infradeterminada).** Las relaciones (a)–(c) omiten la graduación de 𝒯 por
  log ℕ, Φ(α)Φ(β) = Φ(α∗β), [X, V_a] = aV_a y 𝓕t = t^♭𝓕. La simetría las respeta, de modo que la
  conclusión no cambia, pero «toda identidad deducida formalmente de (a), (b), (c)» debe leerse como
  «toda identidad polinómica válida en toda realización de las relaciones, sin usar ninguna
  desigualdad de coeficientes ni la forma de E, H».

**Lema B.** Rehecho: [X,H] = −L′_MS_N − L_MS′_N + S″_N y S′_N = L_MS_N − H dan
H⁽²⁾ = L_MH − [X,H]. Comprobado en coeficientes con pesos arbitrarios (NUMÉRICO, M = 9, N = 6, error
10⁻¹⁵). PROVED. Consecuencias (1)–(3) correctas. La (4) es correcta con la definición
P_{j+1} := L_MP_j − [X,P_j], H^{(j)} := P_jS_N − S^{(j)}_N, que da H^{(j+1)} = P_jH − [X,H^{(j)}]; la
memo no escribe esa definición: ARGUED tal como está, PROVED con la línea añadida. Defectos:

- **E-A5 (truncación).** «Pesos y truncaciones cualesquiera» vale para la truncación
  (L′_M + L_M²), que es Φ(Λ_{≤M}∗Λ_{≤M}) y no Φ_{≤M}(Λ∗Λ). Con la segunda aparece otro defecto con
  soporte en (M, M²]. Precisar.
- **E-A6 (sobre-alcance grave; «Siguiente paso concreto», primera frase).** «No relanzar K1 con otra
  relación del anillo de Dirichlet (grado tres, Vaughan, identidades de convolución): el Lema B las
  deriva de (c) y el Lema A les quita la orientación.» Toda afirmación verdadera sobre Λ se deriva de
  Λ∗1 = log, porque esa identidad define Λ. «Es consecuencia de (c)» no excluye nada y no puede
  usarse como criterio de cierre. Lo que el Lema B demuestra es más estrecho: el defecto truncado de
  grado j está en el ideal generado por H, [X,H], …, y se anula en k ≤ N cuando H se anula. No dice
  que un uso de grado dos carezca de contenido de signo: dice que no introduce un defecto nuevo.
  La frase debe retirarse del registro.
- **E-A7 (antecedente no citado).** El contenido del Lema B y de su consecuencia (1) está en
  `R170_851` §§0–2 (colisión de Selberg; el canal sincronizado se anula en k ≤ N y conserva sólo la
  hipérbola incompleta) y `R170_841`. No es una pieza nueva.

**Lema C.** Rehecho. El átomo de ΣV_i*V_i en log(3/2) proviene sólo de L*L con (n,m) = (3,2)
(2n = 3m con n, m potencias de primo obliga n = 3, m = 2), vale (log 2·log 3/√6)Σ(|β_i|² + |γ_i|²), y
el aislamiento de átomos es el de rem:sosatoms (l. 8469–8474), que aplica a la parte real par de la
medida. La desigualdad estricta T > ½log3 es la correcta para L = Φ_{<N}(Λ). PROVED (con CITED).
Es rem:sosatoms con coeficientes; la memo lo dice. Alcance: cuadrados de grado uno con coeficientes
escalares; no dice nada de V_i con X, J, 𝓕.

**§2(iv), identidad de signatura.** Errónea por un factor 2 (l. 125). El desarrollo del lado derecho
da ½(u(λ) + u(μ)). La identidad correcta es
u(λ) + u(μ) = (1/ε)(1 + εu(λ))(1 + εu(μ)) − 1/ε − ε u(λ)u(μ). La conclusión (signatura (1,1) del
núcleo u⊗1 + 1⊗u para u no constante) es correcta. La etiqueta PROVED del resumen («Qué se probó»,
último ítem) se mantiene sólo con la fórmula corregida.

**§1(5), cΛ y a_P.** δ(k) = (c − 1) log k y, para a_P con P > N, δ(k) = −log k en k ≤ N: correcto
(NUMÉRICO, c = ½ y c = 2). Pero la memo no extrae la consecuencia útil: véase R1 en §4.3.

**§5, batería.** La frase sobre cuartetos y f_t está etiquetada ARGUED por la propia memo; correcto.

### 1.2 Errores de cotejo y de cita

- **E-A8 (omisión mayor en §0 y §1(1)).** La fase 170 trabajó exactamente los apareamientos de
  thm:PCfinite: `R170_816` §2 (ecuación (2): ⟨JH_{M,N}F, g⟩ = 0 por soporte; (3)–(4): salida exacta
  de la identidad con h_{M,N} ≥ 0), §3 (cota bilateral con pérdida √N), §4 (falsación explícita del
  paso «h(k) ≥ 0 ⟹ el apareamiento es ≥ 0»), §6 (separación orientada del canal d = 2: quedan dos
  correlaciones de Fourier sin signo); `R170_819`–`R170_823` (PC a dos escalas, la cancelación divisorial
  sobrevive a la dilatación); `R170_837`, `R170_843`, `R170_847`–`R170_856`. La memo no los cita y
  presenta §4 como «pieza que falta, señalada con precisión». El índice de rutas tiene la fila
  G4A-R161_001-002 (catálogo 04, l. 759) pero no tiene filas para R170_811–R170_840; esa laguna del
  índice explica la omisión y debe repararse (§4.5).
- **E-A9 (identificación indebida; §4, última frase).** «Convertirlos en diagonales es exactamente lo
  que piden las condiciones (ii)–(iii) de prob:annihilate … y prop:annihilate-equiv lo identifica con
  (★).» prob:annihilate pide 𝒪_LF = 0 para vectores de primer contacto, con la minimalidad de la
  ventana (i) como ingrediente; no menciona h_{M,N} ≥ 0 ni una diagonalización. La identidad del §4
  es de otra forma: vale sobre todo P_T y no usa primer contacto. Que ambas impliquen (★) no las hace
  la misma pregunta. Lo que P47 sí registra sobre la diagonalización está en rem:returnremarks
  (l. 6940–6943): la varianza indexada por caminos de divisores no es la norma de la suma coherente
  en k, que contiene términos de Gram cruzados entre k distintos; las fases aditivas diagonalizan en k
  pero no factorizan por de = k, y los caracteres multiplicativos factorizan pero cambian el operador.
  Ésa es la cita pertinente y la memo no la da.
- Citas comprobadas y correctas: P1_BBSTAR_001 §2.8 y Teorema P1.A; índice README Prop N.2; R162_2301
  Lema S; thm:sos y su extensión; observación tras thm:PCfinite. No se comprobaron N_BUILD_018/019/022
  ni ROUND_023_A.

### 1.3 Enunciados corregidos

- **Lema A′ (PROVED).** (1) En toda álgebra con las relaciones exactas del Lema A, 𝓜 = L + L^♭.
  (2) Para M, N cualesquiera y todo S° ∈ 𝒯, la tupla (X, J, J𝓕J, S°, −L_M) satisface la identidad
  de thm:PCfinite con A_M sustituido por −A_M y defectos E° = S°J𝓕J − JS°, H° = −L_MS° − S°′.
  Consecuencia: una identidad polinómica deducida de thm:PCfinite que trate E_N y H_{M,N} como
  símbolos no determina el signo de A_M. Alcance: identidades algebraicas que no usan ninguna
  propiedad de E_N, H_{M,N}, Λ, b ≡ 1 ni K más allá de las relaciones. No es un NO-GO de ninguna
  clase de construcciones: toda construcción que use Λ ≥ 0, K > 0, el soporte de H o el rango de E_∞
  queda fuera.
- **Lema B (PROVED, no nuevo: R170_851).** Como en la memo, con la truncación precisada y la
  recursión de grado j escrita.
- **Lema C (PROVED con CITED).** Como en la memo.
- **Observación D.** ARGUED; se mantiene como tal.

### 1.4 ¿Cierra la pregunta de diseño?

Cierra una cosa: la relación de grado dos no aporta un defecto independiente del de grado uno y, en
la clase de multiplicadores, no completa un cuadrado (thm:sos, P1_BBSTAR §2.8, Lema C). No cierra
K1 como conjunción separador + Poisson + factor arquimediano con paso no lineal; la memo lo dice en
«Resultado» y lo contradice en «Siguiente paso concreto» (E-A6). El hueco concreto es el residuo
común, tratado en §4.

### 1.5 Qué puede registrarse

Índice de rutas y grid, redacción admisible:

> «Relación de grado dos del anillo de Dirichlet como paso no lineal junto con thm:PCfinite: sin
> mecanismo nuevo. PROVED: el defecto truncado de grado dos es L_MH − [X,H] (ya en R170_851); la
> identidad de thm:PCfinite admite una tupla especular con A_M ↦ −A_M, de modo que ninguna
> consecuencia polinómica que trate E_N, H_{M,N} como símbolos fija el signo (reformulación de F2);
> cuadrados de grado uno en (L, L*) con átomos en log ℕ son constantes para T > ½log3 (rem:sosatoms).
> No es NO-GO de la conjunción (E)∧(F)∧(I). Antecedentes: R170_816, R170_819–823, R170_851,
> P47 rem:returnremarks.»

No puede registrarse: «ninguna consecuencia formal de las tres relaciones está orientada» sin la
cláusula de alcance (la fila K1 del LEDGER de la fase lo dice así y debe corregirse); «la orientación
vive sólo en los defectos»; «no relanzar con grado tres, Vaughan o identidades de convolución»;
cualquier redacción que presente los Lemas A, B, C como obstrucción a un objeto que use Λ ≥ 0 o K > 0.

---

## 2. Memo B

### 2.1 Verificación de los enunciados

**Prop. 1.** Correcta. Falta declarar β > 0 como paso j = 0 de (a) (la memo lo usa: «β = π(∅; n_1) >
0»). PROVED, reformulación.

**Prop. 2.** Correcta (densidad de ℤ log p + ℤ log q, continuidad de 𝖡, thm:oneprofile). No requiere
2T_0 < log 2. PROVED, reformulación.

**Prop. 3.** Correcta como enunciado: es la unicidad de Kolmogórov de la realización de un núcleo
semidefinido positivo. Defectos:

- **E-B1 (hipótesis oculta).** La existencia de r presupone que 𝖡 es definida positiva, es decir
  (★). Sin ella la proposición es vacía; en espacios con forma indefinida la unicidad no vale en
  general. Debe enunciarse «si existe».
- **E-B2 (lectura que excede lo probado; «Lectura» del §2 y «Qué falló», primer ítem).** «La identidad
  (G) tiene, si existe, una sola solución salvo isometría» sólo vale para la realización completa con
  resto nulo sobre el portador de un perfil; la partición entre ‖V_TF‖² y ρ_T no es única. Y la
  unicidad salvo isometría vale para todo núcleo semidefinido positivo: no distingue una presentación
  explícita de otra ni dice nada sobre cuál existe. «K2 no es una reducción de (G), es (G) con una
  condición de forma añadida» es correcto como clasificación (reformulación, B3), no como obstáculo.

**Lema 4.** Rehecho y comprobado (NUMÉRICO, conjunto cerrado por divisores de 9 elementos, error
10⁻¹⁵): 𝕍_a = 2U⁻¹[D,U]; U Div_a U^⊤ = DG + GD − 2UDU^⊤; fórmulas de G y de Z Div Z^⊤. Las unidades
para cΛ (d_c) y a_P (indicador de P-rugosos) son correctas. PROVED. Coincide con (𝕍_M)_{mk} = v_{m/k}
de prop:AM(iii).

**Prop. 5.** Correcta (álgebra lineal estándar; C_f es triangular en el orden de toda cadena cerrada
por divisores). PROVED. Defecto principal de la memo:

- **E-B3 (non sequitur; «Lectura» del §3, frase en negrita, y «Qué falló», segundo ítem).** De «los
  pivotes son invariantes por congruencias triangulares unipotentes» la memo concluye «no existe una
  fórmula del pivote obtenida por Λ∗1 = log en esta clase». No se sigue. Los pivotes son invariantes
  de la matriz; toda factorización LDL^⊤ **es** una congruencia triangular unipotente que los exhibe.
  La invariancia no impide que una congruencia los haga visibles: es el modo en que se calculan. La
  Prop. 6 de la propia memo es el contraejemplo: [log mcd(m,k)] = E diag(Λ) E^⊤ es la identidad
  Σ_{d|n}Λ(d) = log n usada como congruencia por E⁻¹, elemento unipotente del álgebra de incidencia, y
  da los pivotes Λ(n). Lo que el §3 demuestra es sólo esto: la congruencia por Z no diagonaliza 𝔸_𝒩;
  transforma Div en DG + GD − 2ZDZ^⊤ y deja Arch y Near sin tratar. Si otra congruencia unipotente
  (del álgebra de incidencia o no) lleva 𝔸_𝒩 a una forma manifiestamente positiva es la pregunta
  abierta, no una pregunta cerrada.
- **E-B4 (etiqueta; «Resultado», última frase; «Qué se probó», Prop. 6 y (4.1)).** «Se ha probado que
  las tres fuentes de explicitud … no lo producen.» Para el patrón de incidencia, lo PROVED es la
  condición necesaria (4.1); su fallo es NUMÉRICO. Esta revisión lo comprobó en el caso mínimo
  𝒩 = {1,2,3} con el perfil a = 0.15, b = 1 (NUMÉRICO, c_0(0) = 1): β·𝖡(log(3/2)) = 0.1435 frente a
  𝖡(log 3)·𝖡(log 2) = 0.3888; también falla en (4,3), (5,2), (5,3), (5,4). La exclusión del patrón de
  incidencia queda como NO-GO NUMÉRICO en un perfil, no PROVED. Una demostración sin cómputo de que
  (4.1) falla exigiría una cota inferior de β − |𝖡(log k)| que no está disponible sin estimaciones.
  Para la sustitución por Z, lo probado es lo dicho en E-B3. Para el producto sobre primos (Prop. 8)
  la afirmación es correcta en el modelo sin Near, que la memo reconoce que no describe 𝔸.

**Prop. 6.** Correcta. Nota: sobre un 𝒩 que contiene al 1 la matriz [log mcd] es singular
(pivote Λ(1) = 0 y Λ(n) = 0 fuera de potencias de primos); «pivotes Λ(n) ≥ 0» debe leerse con la
factorización E diag(Λ) E^⊤, no con cocientes de menores.

**Prop. 7.** Rehecha: π(S;n) ≤ 𝔞(e_{log n} − e_{log k}) = 2[β − 𝖡(log n − log k)]; para
d < log 2 − 2T_0 no hay peine; 1 − cos x ≤ x²/2 da κ_0d². Comprobada en tres puntos (NUMÉRICO:
d = 0.01, 0.03, 0.08; 2(β − 𝖡(d)) = 0.041, 0.311, 1.544 frente a κ_0d² = 0.046, 0.411, 2.925).
PROVED. Defecto:

- **E-B5 (lectura).** «La recursión de pivotes no tiene margen uniforme en ningún paso tardío» es un
  efecto de normalización. La cota κ_0d² es la distancia al cuadrado entre dos traslados vecinos y
  vale igual para la forma arquimediana sola. La cantidad con contenido es el cociente
  π(S;n)/(2[β − 𝖡(log n − log k)]) ∈ [0,1] (o el pivote relativo al pivote arquimediano), sobre el
  que la Prop. 7 no dice nada. «Idéntica para todo peine» describe la cota, no el pivote. La memo dice
  que no es un NO-GO; la condición de reapertura («numerador que se anule al orden exigido») sí la
  trata como restricción dura y debe rebajarse a observación.

**Prop. 8.** Correcta. Coincide con rem:boxes (suma de Kronecker de matrices de Toeplitz de un
primo). PROVED.

**Cotejo con 211.** C49 y C9 están citados conforme al LEDGER (C49: NO-GO PROVED del producto de Schur
local × arquimediano; C9: la dominancia diagonal ponderada se reduce a Σ_{n|m}Λ(n) = log m). C6 y C7
figuran como NOT STARTED, como dice la memo. La propuesta «cerrar 211/C6 con la misma referencia» no
procede: C6 queda «sin mecanismo en el orden multiplicativo», no cerrado.

**Dato NUMÉRICO heredado.** La memo usa de STATEMENT_001 §3 los valores β = 0.01492 y
|𝖡(d)| ≤ 0.0122 en 0 < d ≤ 13. Esta revisión reproduce β = 0.014923 sólo **sin** normalizar F_0 (con
‖F_0‖ = 1, como dice el texto de STATEMENT §2, β = 0.8973), y obtiene 𝖡(log 6) = 0.01373 en la misma
escala (0.8253 normalizado), mayor que 0.0122 y menor que β (NUMÉRICO, dos mallas). El argumento de la
memo para (4.1) no depende de ello (sólo necesita un valor menor que β), pero la cota 0.0122 de
STATEMENT_001 debe recomprobarse y su normalización aclararse.

### 2.2 Enunciados corregidos

- Prop. 1, 2, 4 (Lema), 5, 7, 8: PROVED como están, con las precisiones anteriores.
- Prop. 3: PROVED, condicionada a que 𝖡 sea definida positiva.
- (4.1): condición necesaria PROVED; fallo NUMÉRICO (caso {1,2,3} y otros cuatro pares).
- Lectura del §3, corregida: «La congruencia por Z = C_z, que realiza Λ∗1 = log sobre Div, no
  diagonaliza 𝔸_𝒩 ni cambia sus pivotes; no se conoce una congruencia unipotente explícita que lo
  haga. OPEN.»

### 2.3 ¿Cierra la pregunta de diseño?

No. Deja establecido que K2 es una reformulación (Prop. 1–3) y que tres intentos concretos de
explicitud no funcionan (uno de ellos sólo NUMÉRICO). Huecos que la memo no examina:

1. Congruencias unipotentes fuera del patrón de incidencia, o triangulares respecto de un orden que
   no sea de divisibilidad. La condición de reapertura de la memo las excluye de palabra («que no sea
   una congruencia triangular en el orden de divisibilidad») apoyándose en E-B3; debe invertirse:
   son precisamente el terreno no examinado.
2. La pieza 2ZDZ^⊤ = [2(mk)^{−1/2}Σ_{d|mcd(m,k)} d log d] que el Lema 4 saca de −Div es semidefinida
   positiva y está escrita como suma de cuadrados (paradigma de mcd con g(d) = d log d). La memo no la
   señala. Es genérica en el peine (UDU^⊤ ⪰ 0 para toda unidad u), luego por sí sola no es un paso de
   signo (B1); pero Z𝔸Z^⊤ = Z(Arch − Near)Z^⊤ + 2ZDZ^⊤ − (DG + GD) es una identidad exacta donde
   u ≡ 1 entra en G y en ZDZ^⊤, y la memo no analiza el término −(DG + GD) contra Z·Arch·Z^⊤. No se
   propone como candidata: falta la operación que firme ese resto y no pasa el filtro de cuatro
   puntos (el antecedente es C33b y A_MU_FACTORIZATION §1(f), y no hay mecanismo nuevo identificado).
3. Pivotes relativos (E-B5).

Ninguno de los tres es una candidata lista para construcción. La conclusión «sin mecanismo nuevo» es
correcta; «la pregunta no se relance» (final del §0) excede lo demostrado.

### 2.4 Qué puede registrarse

> «K2, pivotes de Schur por anidamiento multiplicativo de índices: sin mecanismo nuevo; reformulación
> (pivotes positivos a lo largo de una cadena que agota ⟺ objetivo salvo pivote nulo). Herramientas
> PROVED: peine = 2U⁻¹[D,U] en el álgebra de incidencia (válido para todo peine; u ≡ 1 ⟺ Λ);
> cota π(S;n) ≤ 2[β − 𝖡(log n/k)] ≤ κ_0 log²(n/k), independiente del peine; complemento de Schur de
> una suma de Kronecker. Un factor triangular con patrón de incidencia exigiría
> β𝖡(log m/k) = 𝖡(log m)𝖡(log k) en pares coprimos, que falla (NUMÉRICO). No es NO-GO de clase;
> congruencias fuera del patrón de incidencia no examinadas.»

No puede registrarse: «pivotes invariantes bajo el grupo unipotente de incidencia» como motivo de
cierre; «la misma realización (Prop. 3)» como obstrucción; el cierre de 211/C6; «se ha probado que
las tres fuentes de explicitud no lo producen».

---

## 3. Memo D

### 3.1 Verificación de los enunciados

**Lema 1 y Corolario 1.** Rehechos: soporte, condiciones A = B = 0, c_F = 2c_φ + ε c_φ(· − u)
+ ε c_φ(· + u), separación |log n − log n_0| > 1/N > 2η. Correctos. PROVED.

**Lema A.** (i) κ_n = Σ_{d|n, d≥2}(x_d − Λ(d)) y la inversión de Möbius: correcto. (ii) y (iii):
correctos. PROVED. Alcance real: (ii) es la tautología «un polinomio que se anula en un punto está en
el ideal maximal del punto», con el conjunto **completo** de átomos 2 ≤ n < N. No es un enunciado
sobre desigualdades ni sobre certificados de positividad. La «Lectura» («una no linealidad en Λ que
decida el signo tiene que estar en el acoplamiento de Λ con F») no se deduce del lema: es ARGUED y
coincide con la cláusula O2 de OBJECT_SPEC.

**Principio de transferencia.** Correcto en la clase declarada. PROVED.

**Teorema B.** (i), (ii), (iii): correctos; (ii) no usa el signo de λ_A (dirección de recesión de un
convexo cerrado no acotado y Corolario 1). PROVED. (iv): las dos desigualdades son consecuencias
correctas de (MS) (la segunda, por Cauchy–Schwarz en q_± ≤ 2a_T). PROVED como implicaciones. Defectos:

- **E-D1 (etiqueta errónea; «Estado del caso (iv)/(c)», «Conclusión del §3», §7 (P2), §8).** El caso
  (iv) se etiqueta «CONDITIONAL NO-GO» y «no es un objetivo razonable». En la generalidad del
  Teorema B (K convexo cerrado cualquiera) es falso que sea un NO-GO: sea T ≤ ½log5, donde
  λ_A(T) > 0 (PROVED, P47 thm:log5A y monotonía), E = ∅ y K la bola cerrada de radio r en torno a Λ.
  Entonces Π es acotado, Π ≠ {Λ}, y para r·Σ_{n<N}2n^{−1/2} ≤ λ_A(T) se tiene
  a_T^λ(F) ≥ (λ_A(T) − r Σ 2n^{−1/2})‖F‖² ≥ 0: (MS) es verdadero. El caso (iv) es «objetivo con
  margen», cuya verdad depende del tamaño del politopo frente al margen; la etiqueta correcta es
  OPEN en general, verdadero para politopos pequeños donde hay margen estricto, y CONDITIONAL
  (falso bajo la hipótesis W[δ](F_⋆) ≠ 0 y s|W[δ](F_⋆)| > λ_A(T)) sólo para politopos de tamaño fijo
  como los de K_0. La tricotomía enunciada en el resumen («o es falsa, o es identificación, o exige
  margen») es correcta; lo incorrecto es llamar NO-GO al tercer brazo.
- **E-D2 («estrictamente más fuerte»).** La memo define el sentido (existe F con h_Π(F) > 0), y en
  ese sentido es correcto. No está probado que (★) en T no implique (MS): por E-D1, con margen
  estricto lo implica para politopos pequeños. Sustituir por «implica (★) en T y añade la desigualdad
  s|W[δ](F)| ≤ a_T(F)».
- **E-D3 (sobre-alcance; resumen inicial (b) y §0(3)).** «Cierra esa dirección como fuente de signo» y
  «ningún E la convierte en mecanismo». El brazo (iii) (Π = {Λ}) no está cerrado: es el caso en que
  la clase no restringe nada, y por el Corolario C(b) se alcanza con E muy parcial (basta, para
  N ≤ X², un n ∈ E con p^j ∥ n por cada potencia de primo p^j ∈ [X,N)). Lo que el §3 demuestra es
  que una deducción con Π ≠ {Λ} o es falsa o paga margen. Eso es una clasificación, no un cierre.

**Corolario C.** (a) Rehecho: el cono de recesión es D(E) ∩ K_0 y un δ ≥ 0 con Σ_{d|n}δ(d) = 0 se
anula en los divisores de n. Correcto. (b) Rehecho: para n < N ≤ X² las potencias de primo ≥ X que
dividen a n son de un solo primo; el sistema se desacopla en sumas parciales por torre; solución
única ⟺ 𝒯_p ⊂ J_p(E). Correcto. (c) Correcto, incluido el segmento |s| ≤ log p y la desigualdad
exhibida. PROVED. Nota: la desigualdad de (c) es refutable o confirmable en una ventana concreta
(por ejemplo p = 2, a = 2, X ∈ (2√2, 4), N ≤ X²), lo que decidiría el brazo (iv) para K_0 en esa
ventana; no se hizo.

**Observaciones 1 y 2.** Rehechas: N_λ(q_1q_2) = λ(q_1)λ(q_2)/(log q_1 log q_2) para primos distintos
y λ con soporte en potencias de primo; la hipérbola no es convexa pero es no acotada y el argumento
con el Lema 1 en n_0 = q_1 vale. Correctas. PROVED.

**Proposición D.** Rehecha y comprobada (NUMÉRICO: X = 7, N = 49, todo n ∈ [7,49)). (E2), la
triangularidad de 𝖳 (n/k ∈ [X,N) porque k ≤ n/X) y (I2) son correctas. PROVED. «Lo que (I2) no da»:
(1) y (2) correctos; (3) es la tautología de que (I2) reescribe un mismo vector de pesos.

**Cotejo con R186_005 / R186_092.** Las citas son fieles: Lema S0 (identidad de Selberg generalizada
con sistema propio), Lema S1 (triangularidad), TB3-neg, el residuo «completitud más allá de X que no
es identificación total: OPEN», y la corrección M5.1 de R186_092 al inciso (ii). El Corolario C(a)
y la Observación 1 dan una demostración directa de lo que TB3-neg(ii) corregido afirma en la clase
de átomos de completitud; es coherente con R186_092.

**Cotejo con P47.** thm:geo-split(i) dice lo que la memo le atribuye (el signo en la clase es el
signo en Λ más una rigidez sin signo), pero con hipótesis propias (funcional Δ, minimizador
unitario F_⋆); la frase «por thm:geo-split su contenido de signo es el signo en Λ» es una analogía
correcta, no una aplicación: el Teorema B(i) ya lo dice por sí mismo y la cita puede suprimirse.
lem:shape-scale: «proved for c large and small, conditional for O₄^ε»; la memo no lo cita en falso.
cor:margin1 se usa sólo en el brazo condicional.

- **E-D4 (clase más estrecha que el título).** El título habla de «Λ más allá de la ventana», pero
  la clase del §3 sólo admite pesos en [2,N) y átomos en E ⊂ [X,N). Premisas que involucren
  Λ(d) con d ≥ N (como los coeficientes h_{M,N}(k) con M > N de thm:PCfinite) no están en la clase.
  La extensión es inmediata (variables en [2,N′), proyección de Π sobre [2,N), que sigue siendo
  convexa) y el Teorema B se aplica a la proyección; debe decirse.
- **E-D5 (cotejo).** Tampoco cita la fase 170 (`R170_819`–`R170_823`, PC a dos escalas), que es el
  antecedente directo del «diseño X → X²» con la identidad de Poisson–Chebyshev.

### 3.2 Enunciados corregidos

- **Teorema B (PROVED).** (i)–(iii) como en la memo. (iv): «Si Π es acotado y Π ≠ {Λ}, (MS) equivale
  a la positividad en los puntos extremos, implica (★) en T y las desigualdades
  s|W[δ](F)| ≤ a_T(F), s|W[δ](F,G)| ≤ 2(a_T(F)a_T(G))^{1/2}. Recíprocamente, si λ_A(T) > 0 y
  sup_{λ∈Π}Σ_n 2n^{−1/2}|λ(n) − Λ(n)| ≤ λ_A(T), (MS) vale.» Estado del brazo (iv): OPEN; verdadero en
  las instancias del recíproco; CONDITIONAL-falso para K_0 bajo la hipótesis sobre el minimizador.
- **Conclusión del §3.** «Clasificación PROVED. NO-GO PROVED sólo en el brazo no acotado
  (Teorema B(ii), Corolario C(a), Observación 1). El brazo de identificación es el objetivo sin
  restricción añadida. El brazo de politopo es un objetivo con margen, no un NO-GO.»
- Lema A, Corolario C, Proposición D: PROVED como están.

### 3.3 ¿Cierra la pregunta de diseño?

Cierra el casillero «completitud parcial más allá de X» en un sentido preciso: en la clase de
átomos lineales con K convexo, una premisa de completitud que no identifique a Λ o es falsa (PROVED)
o pide margen. Eso responde a R7 mejor que el estado anterior («OPEN; no hay candidata»). No cierra:
el brazo de identificación (que es donde vive cualquier objeto que cumpla O4); el brazo de politopo;
clases no convexas; premisas que no son propiedades del peine. El enunciado (P1) del §7 es O2 ∧ O4 de
OBJECT_SPEC y no es un resultado. No veo un objeto que satisfaga OBJECT_SPEC §1 y escape a los lemas
de la memo, porque esos lemas no excluyen ningún objeto del brazo de identificación.

### 3.4 Qué puede registrarse

> «O166.802.1, completitud parcial más allá de X (átomos lineales Σ_{d|n}λ(d) = log n en E ⊂ [X,N),
> restricción convexa K): clasificada. Π(E,K) no acotado ⟹ la clase contiene un peine con forma
> negativa (NO-GO PROVED, sin usar el signo en Λ); para K_0 esto ocurre si y sólo si alguna potencia
> de primo de [X,N) no divide a ningún elemento de E. Π = {Λ} ⟹ el enunciado es el objetivo en T
> (para N ≤ X² y K_0: si y sólo si cada p^j ∈ [X,N) divide exactamente a algún n ∈ E). Π acotado
> ≠ {Λ} ⟹ objetivo con margen s|W[δ](F)| ≤ a_T(F): OPEN, verdadero para politopos pequeños donde
> λ_A(T) > 0. La identidad de dos escalas de grado dos es lineal en los contactos nuevos para
> N ≤ X² (PROVED). Residuo vivo: identificación total con no linealidad en el acoplamiento peso–vector
> (O2 ∧ O4).»

No puede registrarse: «NO-GO (clase) … CONDITIONAL en (iv)»; «cierra la dirección como fuente de
signo»; «no es un objetivo razonable»; «ningún E la convierte en mecanismo».

---

## 4. El residuo común de las memos A y D

Enunciado en A §4 y recogido en D §8(3) y en la fila K1 del LEDGER de la fase: una identidad

    a_T(F) = ‖V_TF‖² + Σ_{k>N} h_{M,N}(k) |ℓ_k(F)|² + (términos polares como cuadrados),
    h_{M,N}(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) ≥ 0,   M ≥ N,

que convierta en diagonales los apareamientos de H_{M,N} y E_N de thm:PCfinite.

### 4.1 ¿Está bien enunciado?

La fórmula de h_{M,N} y su soporte en k > N coinciden con thm:PCfinite (l. 6673–6678); el rango dos
de E_∞ sobre el núcleo de Schwartz es correcto (para F(t) = e^{t/2}f(e^t), SF − JS𝓕F
= ½e^{−t/2}f̂(0) − ½e^{t/2}f(0)). Pero como objetivo está **infradeterminado**:

- Con ℓ_k ≡ 0 es la identidad (G) de OBJECT_SPEC §1. Sin especificar de dónde salen los ℓ_k no es un
  enunciado distinto de (G) con una forma prescrita para parte de ρ_T. Para que sea un residuo y no
  un deseo hay que fijar los ℓ_k; lo único que thm:PCfinite ofrece es
  ⟨Y, V_{−log k}𝓕F⟩ con Y = (S_N⁻¹)*F, que no es un módulo al cuadrado.
- S_N⁻¹ es formal: el símbolo Σ_{n≤N}n^{−1/2−iτ} no está acotado inferiormente de manera uniforme y
  P47 rem:Sren advierte que S_N no tiene límite; la identidad «despejada» de A §1(4) no está definida
  como identidad de formas sobre P_T ∩ 𝒟_T. La memo lo marca «formal» y no lo resuelve.
- thm:PCfinite es una identidad sobre la recta; no contiene la compresión a la ventana. Sobre la
  recta, A_M no tiene signo (su símbolo es negativo en un conjunto no vacío). Todo el signo de a_T
  depende de que F tenga soporte en I_T, mientras que 𝓕F y Y no lo tienen. El residuo no dice cómo
  entra el soporte.

### 4.2 ¿Está registrado en el corpus?

Sí, en lo esencial, y las memos no lo citan.

- `R170_816` §2: salida exacta de la identidad sobre vectores de ventana, con ⟨JH_{M,N}F, g⟩ = 0 por
  soporte y C = Re⟨H_{M,N}𝓕F, g⟩ como único término de hipérbola; §3: sólo cota bilateral, pérdida
  ≥ (log 2/2√2)√N con M = N²; §4: **falsación explícita** de «h(k) ≥ 0 ⟹ apareamiento ≥ 0» (dos
  funciones u, τ_au de soporte pequeño); §6: separación orientada del canal d = 2, que deja dos
  correlaciones de Fourier sin signo; §5 y §7: la correlación que falta «sería exactamente la ley
  aritmética nueva».
- `R170_819`–`R170_823`, `R170_837`, `R170_843`, `R170_847`–`R170_856`: variantes a dos escalas,
  curvatura, Wronskiano exterior, extracción de Möbius, colisión de Selberg.
- P47 rem:returnremarks: términos de Gram cruzados entre k distintos; fases aditivas frente a
  caracteres multiplicativos.
- P47 eq:Qbalance, eq:Qrecombine, eq:Qspectral: ya existe una identidad exacta con coeficientes
  aritméticos no negativos emparejados con módulos al cuadrado de funcionales exteriores,
  c_{N,L}(F) = Σ_{m≤L} d_{m,N}|(𝒪_LF)_m|², d_{m,N} = Σ_{n≤N}Λ(n)n^{−(a_m+1/2)} > 0; y P47 demuestra que
  es ciega al signo (vale para todo autovector, con λ de cualquier signo) y que Q_{N,L} no admite
  representación como suma de cuadrados sobre todo P_T.
- Índice de rutas: fila G4A-R161_001-002 (catálogo 04, l. 759). **No hay filas para R170_811–R170_840**
  (el catálogo 04 salta de R170_808 a R170_841). Los anexos de la fase 212 heredan la laguna
  (`ANNEX_INDEX_04.md` sólo menciona la fila de la fase 160/161).

El residuo no es, por tanto, una pieza recién identificada: es la obligación abierta de R170_816 §5
trasladada de «vectores de primer contacto» a «todo P_T», más la exigencia de forma diagonal.

### 4.3 ¿Algo de lo probado lo obstruye?

No hay obstrucción PROVED. Los lemas de A no lo tocan (el Lema A′ deja fuera toda construcción que
use h ≥ 0; los Lemas B y C no hablan de él). El Teorema B de D lo sitúa en el brazo de
identificación (usa todos los átomos k ≤ N), donde no hay restricción. Sí hay cuatro restricciones
que cualquier versión debe cumplir; las dos primeras se demuestran aquí.

- **R1 (PROVED, con CITED lem:shape-scale, parte probada).** No existe una familia de identidades
  a_T^a(F) = ‖V^aF‖² + Σ_{k≥2} h^a(k) q_k^a(F), válida para todo peso a ≥ 0 en un cono que contenga
  {cΛ : c ≥ 1}, con q_k^a ≥ 0 y h^a(k) = Σ_{dm=k, d≤M, m≤N}a(d) − log k·1_{k≤N}.
  *Demostración.* Para a = cΛ, c > 1, M ≥ N: h^a(k) = (c − 1) log k ≥ 0 en k ≤ N y h^a(k) = c·h(k)
  ≥ 0 en k > N (NUMÉRICO de control, c = 2). La identidad daría a_T^{cΛ} ≥ 0 sobre P_T, falso para c
  grande y T > ½log2 (lem:shape-scale; también Lema 1 de la memo D). ∎
  Consecuencia: el residuo no puede obtenerse de la versión de thm:PCfinite con pesos genéricos
  tratando por igual los coeficientes interiores y exteriores y especializando a Λ al final. Los
  términos en k ≤ N no pueden entrar como cuadrados con el mismo patrón; la línea que se rompe para
  cΛ (cláusula O4) tiene que ser ésa, y debe romperse también para c < 1, donde el defecto interior
  es negativo y la restricción R1 no dice nada.
- **R2 (PROVED; ya en R170_816 (2)).** Para F, G ∈ L²(I_T) y M ≥ N ≥ e^{2T}, ⟨G, H_{M,N}F⟩ = 0. Los
  funcionales ℓ_k(F) no pueden ser funcionales de la compresión de H a la ventana; dependen de F a
  través de vectores no locales (𝓕F, (S_N⁻¹)*F, colas exteriores). El nexo natural son los momentos
  exteriores de P47 §collars, y allí está la advertencia de eq:Qspectral.
- **R3 (CITED, R170_816 §4 y rem:returnremarks).** La positividad de los coeficientes no firma un
  apareamiento entre dos vectores distintos, y la suma en k es coherente (términos cruzados entre k
  distintos). Una diagonalización exige una operación que identifique los dos vectores
  JS⁻¹JF y S⁻¹JSF (formales) o que cancele los cruces; ninguna está escrita.
- **R4.** La identidad debe ser sensible al soporte de F en I_T (§4.1, tercer punto).

### 4.4 Filtro de cuatro puntos aplicado al residuo

(1) Antecedente más cercano: `R170_816` §§2–7; P47 thm:PCfinite, rem:returnremarks, eq:Qbalance.
(2) Objeto nuevo: ninguno escrito; ℓ_k y V_T sin definir. (3) Diferencia con el antecedente: forma
global sobre P_T en lugar del radical de primer contacto, lo que evita necesitar la minimalidad de
la ventana pero no evita la dificultad registrada (apareamiento entre dos vectores, cruces en k,
pérdida √N en valor absoluto). (4) Identidad de conexión: thm:PCfinite, que es bilineal y sin signo.
Conclusión: **no pasa el filtro**; no es una candidata lista para construcción. Es un casillero
abierto con especificación R1–R4, no un mecanismo. Reabrirlo exige escribir la operación de R3.

### 4.5 Qué registrar

> «Residuo PC-diagonal: identidad a_T = ‖V_TF‖² + Σ_{k>N}h_{M,N}(k)|ℓ_k(F)|² + polares. OPEN, sin
> objeto. Antecedentes: R170_816 (salida exacta, falsación de h ≥ 0 ⟹ apareamiento ≥ 0, canal d = 2),
> R170_819–823, P47 rem:returnremarks y eq:Qspectral. Restricciones: no puede ser especialización de
> una identidad genérica en el peso con coeficientes interiores y exteriores tratados por igual
> (falsificador cΛ, c grande; PROVED); los ℓ_k son funcionales exteriores (H se anula comprimido a la
> ventana; PROVED); hace falta una operación que diagonalice los cruces en k (no escrita). No reabrir
> sin esa operación.»

Además: añadir al catálogo 04 del índice las filas que faltan para R170_811–R170_840, y corregir la
fila K1 del LEDGER de la fase («la orientación vive sólo en los defectos» → «en propiedades de la
realización que las relaciones no expresan: Λ ≥ 0, b ≡ 1, K > 0 y los defectos»).

---

## 5. Lista de correcciones obligatorias antes de registrar

| Ref. | Lugar | Corrección |
|---|---|---|
| E-A1, E-A2 | A §3 Lema A, lectura; §2(iii) | Sustituir por Lema A′; declarar el alcance |
| E-A3 | A §3 lectura; §4 | Retirar «exclusivamente»; añadir Λ ≥ 0, b ≡ 1, K > 0 |
| E-A5 | A Lema B | Precisar la truncación; escribir la recursión de grado j |
| E-A6 | A «Siguiente paso concreto» | Retirar la prohibición de grado tres / Vaughan / convolución |
| E-A7, E-A8 | A §0, §1(1), §4 | Citar R170_816, R170_819–823, R170_851; rem:returnremarks |
| E-A9 | A §4 | Retirar la identificación con prob:annihilate |
| — | A §2(iv) | Corregir el factor 2 de la identidad de signatura |
| E-B1, E-B2 | B Prop. 3 y lectura | Condicionar a 𝖡 definida positiva; rebajar la lectura |
| E-B3 | B §3 lectura; «Qué falló» | Sustituir por la lectura corregida de §2.2 |
| E-B4 | B «Resultado»; «Qué se probó» | (4.1): fallo NUMÉRICO; retirar «se ha probado» |
| E-B5 | B Prop. 7 lectura; reapertura | Rebajar a observación; invertir la condición de reapertura |
| — | B «Siguiente paso» | No cerrar 211/C6 |
| E-D1, E-D2 | D §3, §7 (P2), §8 | Brazo (iv): OPEN / objetivo con margen; añadir el recíproco |
| E-D3 | D resumen, §0(3) | Retirar «cierra la dirección» y «ningún E» |
| E-D4, E-D5 | D §3, §0 | Declarar la extensión a pesos más allá de N; citar R170_819–823 |
| — | STATEMENT_001 §3 (fuera de las memos) | Aclarar la normalización de β y recomprobar la cota 0.0122 (NUMÉRICO de esta revisión: 𝖡(log 6) = 0.01373 en la misma escala) |
