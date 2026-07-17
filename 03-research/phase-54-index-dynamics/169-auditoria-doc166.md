# Doc 169 — Auditoría adversarial del Doc 166 (deformación de métricas, flujo de Gram, conservación de κ)

**Programa:** Hipótesis de Riemann — Phase 54: dinámica del índice.
**Fecha:** junio 2026.
**Rol:** ADVERSARIAL. Mandato: destruir los teoremas del Doc 166. Protocolo de 6 puntos ejecutado
íntegro, con re-derivación cerrada (sin numéricos). Patrón histórico vigilado: (i) parámetros como
constantes, (ii) finito-dimensional citado como general, (iii) H-26 usada en silencio,
(iv) cuadrados que no son cuadrados.

---

## 0. Veredicto por pieza

| Pieza | Enunciado | Veredicto |
|---|---|---|
| (a) Teorema 166.9, κ(G)=κ | conservación del índice en 𝕄 | **CORRECTO-PERO-VACÍO.** Verdadero también en dim ∞, pero es la ley de inercia de Sylvester re-etiquetada: κ(G) es por construcción la inercia de la forma FIJA Q transportada por congruencia. No es un teorema dinámico; la palabra "ley de conservación" es retórica. El "salto en ∂𝕄" no es teorema: es donde la definición deja de aplicar. |
| (b) Hessiano = L ≥ 0, "cuadrado RH-libre" | 166.10(a) + 166.12 | **CORRECTO-PERO-VACÍO, con caveat de alcance.** El Hessiano es de 𝔇₂ (no de 𝔇, que no es diferenciable); 𝔇₂ es cuadrática POR ELECCIÓN, luego su Hessiano es constante y ≥ 0 automáticamente: el "test anti-circularidad" no podía fallar. El cuadrado es genuino (adjunto HS verificado, sin error de conjugación). Bien definido con prueba solo en el modelo finito (GAP 166.D, declarado en §4.3 pero ausente del titular de §5.1). El peso NO introduce ζ — pero ver §2: la "calibración" es una elección de gauge presentada como descubrimiento. |
| (c) W punto fijo "incondicional"; RH = W en el cono | 166.13(a), resumen §0 | **CORRECTO-PERO-VACÍO + sobreventa de hipótesis.** A_t(W)=0 es EXACTAMENTE (H-26)(i) = V.1 de Phase 26, NO probado. El cuerpo lo cita; el resumen ejecutivo dice "incondicionalmente" — patrón (iii) a nivel titular. Y "RH ⟺ W>0" es el criterio de Weil (Weil 1952) verbatim, con decoración dinámica: CERO contenido nuevo más allá de la observación (correcta, modesta) de que ker L = formas apareadas λ↔λ̄. |
| (d) Teorema 166.6, φ(b) | cota inferior universal | **AGUANTA.** φ(b)=2b(1−2b)^{(1−2b)/(2b)} re-derivada y CORRECTA (cálculo §4.1). Es la pieza con más contenido real del documento — condicional a (H-26)(ii) (autovector genuino v_j, V.2 no probado), correctamente citada. La "calibración franja↔peso" (166.6(i)) es correcta pero de contenido menor (el peso es gauge; ver §2 y §4.3). |
| (e) Teorema 166.13, flujo lineal, ℓ(b) | expulsión + tasa | **CORRECTO en el modelo; el "eco de escala" MUERE.** ℓ(b)=1/(1−4b²)−2/(1−b²)+1 re-derivada y correcta; la lógica de expulsión es válida (§5). PERO el coeficiente 2 de ℓ(b)≈2b² es un artefacto del peso: con peso e^{−2a|t|} se obtiene ℓ_a(b)≈2b²/a³ (cálculo §4.3). El "factor 4 sin explicar" frente a A.15 (Λ=max b²/2) no es un dato: es dependencia de gauge. Solo el EXPONENTE 2 es invariante, y está forzado por la paridad γ↦−γ — lo que el propio doc admite y luego desoye en el veredicto al listar "tasa 2b²" como dividendo. |
| (f) Dualidad con Rodgers–Tao | PUENTE 166-DBN | **ANALOGÍA VERBAL con un único punto de contacto formal.** Ambos colocan RH "en una frontera" — eso es real como forma de enunciado. Pero la tabla aparea un teorema profundo (Λ≥0, Rodgers–Tao 2020) con una tautología (166.9) más una reescritura de Weil (166.11(c)). "La variable dinámica de uno es la conservada del otro" es asimétrico en profundidad: la monotonía de κ bajo DBN es de Bruijn 1950 (real); la conservación de κ bajo Gram es Sylvester (vacía). Consistente con Doc 167 (sin contradicción, §6). |

**Veredicto global:** ningún teorema del Doc 166 es FALSO. Pero de sus cuatro "dividendos
no-RH-equivalentes" declarados en §6, sobrevive entero solo uno (166.6/φ, condicional a V.2);
166.9 es tautología vestida, 166.13(a)+(c)-interpretación es Weil reescrito y condicional a V.1,
y la tasa 2b² pierde su coeficiente (queda solo el exponente, forzado por simetría). El documento
es honesto en el cuerpo (etiqueta sus GAPs) pero su resumen ejecutivo y su veredicto sobreviven
mejor que su letra pequeña — exactamente el modo de inflación que esta fase debía vigilar.

---

## 1. κ(G): ¿bien definido? ¿qué contenido tiene 166.9?

**Buena definición.** κ(G) := dim del subespacio espectral negativo de M_G := G^{−1/2}WG^{−1/2}.
Con G ≥ εI acotado y W acotadamente invertible (H-W), M_G es autoadjunto de fondo y acotadamente
invertible (M_G^{−1} = G^{1/2}W^{−1}G^{1/2}), luego 0 ∉ σ(M_G) y el proyector espectral negativo
está bien definido. Nota: el "Gram de Q en la geometría G" es en rigor G^{−1}W (G-autoadjunto);
es similar a M_G vía G^{1/2}, mismo espectro, mismo índice. Bien definido: SÍ.

**Validez en dimensión infinita.** El argumento de congruencia del doc es correcto también en
dim ∞: si M ⊂ K es negativo-definido para ⟨M_Gx,x⟩₀, entonces G^{−1/2}(M) lo es para Q, biyección
que preserva dimensión; el sup de dimensiones de subespacios negativos es κ (H-Π), y coincide con
la dimensión espectral negativa porque M_G es invertible (la compresión al subespacio espectral
positivo es ≥ ε, luego la proyección espectral negativa es inyectiva sobre todo subespacio
negativo-definido). Esto es estándar (Bognár 1974, cap. IV: todas las descomposiciones
fundamentales de un Π_κ tienen la misma parte negativa κ; Azizov–Iokhvidov 1989, cap. 1).
**El teorema es verdadero tal como está enunciado, sin H-26 y sin RH.** No hay error.

**El contenido.** Aquí muere la pieza como "resultado". κ(G) es, por construcción, la inercia de la
forma fija Q leída en la base/geometría G. La ley de inercia de Sylvester dice precisamente que la
inercia de UNA forma no depende de la congruencia con que se la mire. El enunciado "κ(G)=κ para
todo G∈𝕄" es, palabra por palabra, esa ley: no se está probando que una cantidad dinámica se
conserve a lo largo de un flujo, se está observando que una cantidad que NO depende de G es
constante en G. Tres consecuencias adversariales:

1. **"Ley de conservación exacta de toda deformación" es retórica.** Se cumple para curvas
   continuas, discontinuas, y para reasignaciones arbitrarias de G — porque no hay nada que
   conservar: κ(G) nunca fue función de G. Un teorema de conservación dinámico afirmaría que un
   flujo concreto preserva una cantidad que a priori podía variar. Aquí no hay tal a priori.
2. **El no-go "ninguna deformación de la métrica puede reducir κ" es verdadero y vacuo.** κ es un
   invariante de Q sola. Nadie con la definición delante pudo haber esperado reducir n_−(Q)
   cambiando el producto interno con que se la mide. El no-go bloquea una estrategia que no era
   coherente ni como deseo.
3. **"Solo puede saltar en ∂𝕄" no es un teorema.** En ∂𝕄, G^{−1/2} no existe y κ(G) no está
   definido. Lo probado no es "salta en la frontera" sino "la definición caduca en la frontera".
   La "teoría del salto de índice en ∂𝕄" (GAP 166.F) está bien nombrada como problema abierto,
   pero el Doc 166 no aporta sobre ella ni un lema.

**La versión no trivial que el doc NO prueba.** Lo no-trivial en esta área es espectral: p.ej. que
para todo operador Q-autoadjunto en Π_κ el número de pares de autovalores no-reales está acotado
por κ, con subespacios raíz λ↔λ̄ apareados hiperbólicamente (Pontryagin 1944; Iokhvidov–Krein
1956; Krein–Langer 1973), o la clasificación de definitizables (Langer 1982). Eso es teoría
clásica citada, no producto del Doc 166. La aportación propia de 166.9 al programa es una frase de
contabilidad, no un mecanismo. **La "respuesta a la pregunta del director" (la expulsión ES
conservación) confunde dos planos:** la expulsión es un hecho del flujo de Gram (166.13, modelo
finito); la conservación es un hecho de la definición de κ. El segundo no explica el primero: lo
que explica la expulsión es 166.6(ii) (𝔇>0 en el interior) + linealidad del flujo, no Sylvester.

**Veredicto (a): CORRECTO-PERO-VACÍO.**

---

## 2. El Hessiano re-derivado

**Objeto exacto.** 𝔇 (Def. 166.5) es sup de normas: convexo, 1-homogéneo, NO diferenciable — no
tiene Hessiano. Lo que tiene Hessiano es el sustituto 𝔇₂(G) = ½∫e^{−2|t|}‖A_t(G)‖²_HS dt
+ ½‖A_J(G)‖²_HS. Como A_t y A_J son LINEALES en G, 𝔇₂ es una forma cuadrática y su Hessiano es el
operador constante L en todo punto. **Re-derivación del adjunto (chequeo del patrón (iv)):**
⟨A_t(G),M⟩_HS = Tr((U_t^*GU_t−G)^*M) = Tr(G^*(U_tMU_t^*)) − Tr(G^*M) = ⟨G, U_tMU_t^*−M⟩_HS, luego
A_t^*(M) = U_tMU_t^* − M, exactamente como el doc. Nótese que U_t NO es unitario (espectro
no-real), así que U_t^* ≠ U_{−t} y el orden importa: el doc lo hace bien. L = ∫e^{−2|t|}A_t^*A_t dt
+ A_J^*A_J es suma de cuadrados HS genuina: **el cuadrado SÍ es un cuadrado.** Sin error de
conjugación ni de signo.

**¿Respecto de qué producto interno?** Del HS inducido por el FONDO ⟨·,·⟩₀ (RH-libre, fijo), no
de G. No hay dependencia del punto base, no hay circularidad por esa puerta. Correcto.

**Convergencia.** En norma de operadores: ‖A_t‖ ≤ 1+‖U_t‖₀² ≤ C²(1+|t|)^{2d}e^{2b_max|t|}
((H-26)(iii)); el integrando e^{−2|t|}‖A_t‖² es integrable ⟺ 4b_max < 2 ⟺ b_max < ½: la misma
condición que la finitud de 𝔇. PERO en HS: para G genérico en dim ∞, ‖A_t(G)‖_HS = ∞ y 𝔇₂ no está
definida — GAP 166.D, que el doc declara en §4.3. **Hallazgo de presentación:** el Teorema 166.10
(§5.1) y el punto (b) del resumen ejecutivo enuncian "el Hessiano de 𝔇 es L ≥ 0" sin repetir que
(α) es 𝔇₂ y no 𝔇, y (β) la afirmación solo tiene prueba en el modelo finito. Patrón (ii) en el
titular, aunque el cuerpo está etiquetado.

**¿Por qué el test anti-circularidad no podía fallar?** Porque 𝔇₂ se ELIGIÓ cuadrática. Toda
funcional de la forma ½‖T(G)‖² con T lineal tiene Hessiano constante T^*T ≥ 0. La pregunta "¿la
segunda variación es la forma de Weil?" solo era una pregunta viva para una funcional no cuadrática
(p.ej. la segunda variación de 𝔇 restringida a una normalización no lineal, o en el minimizador de
frontera de 166.11 — no calculadas). El "resultado negativo limpio" de 166.10 es un hecho de
diseño, no un descubrimiento sobre el problema. Además, la comparación "L ≠ Q" es de tipos: L actúa
sobre H_h (formas hermitianas), Q sobre K; el propio doc lo dice en la prueba — con lo cual el
enunciado "el Hessiano NO es la forma de Weil" es verdadero en el sentido débil de que ni siquiera
son comparables.

**¿El peso e^{−2|t|} introduce ζ?** No. El peso es un parámetro libre del constructor; no porta
ningún dato de ζ (ni ceros, ni primos). Lo que sí hay es retórica invertida: el doc ELIGE el
exponente 1 (resp. 2) para que la condición de finitud sea "b < ½" y luego anuncia "la franja
crítica ES la región de integrabilidad" (166.6(i)) como si la funcional hubiera descubierto la
franja. Con peso e^{−a|t|}, la finitud es b_max < a/2: la "calibración" es la elección a=1. Es
legítimo como diseño (y la dirección útil es la que usa: Hadamard–de la Vallée Poussin garantiza
la finitud), pero no es contenido: cualquier familia de grupos con crecimiento exponencial acotado
admite un peso exponencial que la hace integrable.

**Veredicto (b): CORRECTO-PERO-VACÍO** (cuadrado genuino, RH-libre, pero positividad automática
por diseño cuadrático; alcance real = modelo finito).

---

## 3. W punto fijo: ¿reformulación de Weil?

**El hecho.** A_t(W) = U_t^*WU_t − W = 0 ∀t ⟺ U_t es Q-unitario. Eso es literalmente la hipótesis
(H-26)(i) — el ítem V.1 del puente de Phase 26, que la memoria del programa registra como NO
probado. Igual A_J(W)=0. Por tanto:

1. **"Incondicionalmente" es falso como adverbio.** El resumen ejecutivo (§0, punto (1)) y la
   interpretación de 166.13 dicen "A_t(W)=0, A_J(W)=0 incondicionalmente" / "sin RH". "Sin RH" es
   correcto; "incondicionalmente" no: es condicional a V.1. El cuerpo del teorema 166.13 sí lista
   "(H-26) restringida al modelo" — la letra pequeña es honesta, el titular no. Es el patrón (iii)
   en su forma más sutil: la hipótesis está declarada en el marco y luego se evapora del lenguaje
   de los resultados ("punto fijo universal", "canónico", "gratis").
2. **El abuso de dominio está controlado.** W con m≥1 es indefinida: W ∉ 𝕄 y W ∉ ∂𝕄 (la frontera
   son semidefinidas positivas). "W es punto fijo del flujo" se refiere a la extensión lineal del
   flujo a todo H_h, y el doc lo dice explícitamente ("como FORMA hermitiana, no necesariamente
   como métrica", 166.13(a)). Sin cargo aquí.
3. **El contenido es el criterio de Weil verbatim.** "RH ⟺ el punto fijo W cae dentro del cono
   𝕄" = "RH ⟺ W ≥ ε > 0" = positividad de la forma de Weil (Weil, *Sur les "formules explicites"
   de la théorie des nombres premiers*, Comm. Sém. Math. Lund 1952; con la uniformidad = GAP
   166.A). El doc declara honestamente que 166.7 es "RH-reescrito", pero presenta la lectura
   dinámica de 166.13(a)+(c) ("el punto crítico existe siempre y es canónico; RH es su pertenencia
   al cono") como la "imagen completa del muro" — es la MISMA frase de Weil con un flujo alrededor.
   Lo único añadido por la dinámica es 166.13(b): ker L = formas apareadas λ↔λ̄ (cálculo correcto:
   e^{it(λ_μ−λ̄_ν)}=1 ∀t ⟹ λ_μ=λ̄_ν o entrada nula). Es una observación de conmutantes estándar
   en teoría de representaciones; correcta, menor.

**Veredicto (c): CORRECTO-PERO-VACÍO, condicional a V.1, con sobreventa adverbial en el titular.**
La trampa de la fase ("reformulación correcta con cero contenido nuevo") se materializa aquí.

---

## 4. φ(b), ℓ(b) y el factor 4 — re-derivación cerrada

### 4.1 φ(b): VERIFICADA

g(s) = e^{−s}(e^{2bs}−1) = e^{(2b−1)s} − e^{−s}, 0<b<½. g'(s)=0 ⟺ (2b−1)e^{(2b−1)s} + e^{−s} = 0
⟺ e^{2bs} = 1/(1−2b) ⟺ s_* = −log(1−2b)/(2b) > 0. Valor: e^{−s_*} = (1−2b)^{1/(2b)} y
e^{2bs_*}−1 = 2b/(1−2b), luego φ(b) = 2b(1−2b)^{1/(2b)−1} = 2b(1−2b)^{(1−2b)/(2b)}. **Coincide.**
Asintóticas: (1−2b)^{1/(2b)} → e^{−1} da φ ~ (2/e)b; b→½⁻ da φ→1; b≥½: g no decae, sup=∞.
Monotonía estricta: el integrando crece estrictamente en b a s fijo. **Todo correcto.** La cadena
de la cota también: ⟨A_t(G)v_j,v_j⟩₀ = (e^{−2b_jt}−1)⟨Gv_j,v_j⟩₀ con el signo de t elegido, y
‖A_t(G)‖₀ ≥ |⟨A_tv_j,v_j⟩|/‖v_j‖². Requiere v_j autovector GENUINO — (H-26)(ii) = V.2, no probado,
correctamente citado en el enunciado. 166.6(ii),(iii) se siguen. **El Teorema 166.6 aguanta tal
como está etiquetado.** Es el resultado con más contenido del documento: una cota inferior
cuantitativa explícita de la incompatibilidad métrica por cada cero off-line.

### 4.2 ℓ(b): VERIFICADA en el modelo

En el modelo normal, U_t^*E_jU_t = |e^{itλ_j}|²E_j = e^{−2b_jt}E_j, luego A_t(E_j) =
(e^{−2b_jt}−1)E_j y, como A_t^*(E_j) lleva el mismo multiplicador, A_t^*A_t(E_j) =
(e^{−2b_jt}−1)²E_j. Integral: con ∫₀^∞ e^{−2t}(e^{2ct}−1)²dt = 1/(2−4c) − 2/(2−2c) + ½ para c=±b,
suma = [1/(2−4b)+1/(2+4b)] − 2[1/(2−2b)+1/(2+2b)] + 1 = 1/(1−4b²) − 2/(1−b²) + 1. **Coincide.**
Taylor: (1+4b²+16b⁴) − (2+2b²+2b⁴) + 1 = 2b² + 14b⁴ + O(b⁶) = 2b²+O(b⁴). ✓ Creciente en (0,½)
(2(1−b²)² ≥ (1−4b²)² allí) y polo en b=½. ✓ Detalle que el doc despacha rápido y es correcto: E_j
solo NO es autovector de L (A_J lo permuta con E_{j'}, el reflejado); el autovector es E_j+E_{j'},
sobre el cual la parte-t actúa con el MISMO ℓ(b) en ambas componentes porque la integral con peso
par es invariante b↦−b. También verifiqué la cadena de Jordan de 166.13(c): con Gv_j=0 y G=G*≥0,
⟨G(w+itv_j), w+itv_j⟩ = ⟨Gw,w⟩ (los cruzados mueren por ⟨Gw,v_j⟩=⟨w,Gv_j⟩=0), la constancia en t
fuerza ⟨Gw,w⟩=0 ⟹ Gw=0; inducción correcta. **El Teorema 166.13 es correcto en el modelo finito.**

### 4.3 El factor 4: NO es un misterio — es gauge. El "eco cuantitativo" muere.

**Lado DBN (A.15).** Modelo de par aislado bajo el flujo de calor: ż_k = Σ_{j≠k} 2/(z_k−z_j)
(Rodgers–Tao 2020, §2; de Bruijn 1950). Para un par conjugado z = x±iy aislado:
ż = 2/(z−z̄) = −i/y ⟹ ẏ = −1/y ⟹ y² = y₀² − 2t, colisión en t = y₀²/2. Con y₀ = b (coordenada
z = γ−ib del cero ½+b+iγ): contribución b²/2 a Λ. **A.15 está bien computada como heurística de
par aislado.** Sin error en ese lado.

**Lado Gram.** ℓ(b) = 2b²+O(b⁴) — correcto (§4.2) — **pero el coeficiente depende del peso.** Con
peso e^{−2a|t|} (a>2b_max arbitrario, igual de admisible: la única restricción estructural es la
integrabilidad), la misma integral da

  ℓ_a(b) = a/(a²−4b²) − 2a/(a²−b²) + 1/a = (2b²/a³) + O(b⁴/a⁵).

Con a=1 sale 2b²; con a=4^{1/3} saldría exactamente b²/2. Además el parámetro temporal s del flujo
Ġ=−LG no tiene identificación canónica con el t de DBN: reescalar s reescala ℓ. **Conclusión: el
"factor 4 de discrepancia" no es un dato a explicar — no existe como invariante.** Lo único
invariante de gauge es el EXPONENTE: ℓ ~ b² y Λ ~ b², primera potencia par permitida por la
simetría γ↦−γ, como el propio [PUENTE 166-E] reconoce ("eco estructural, no identidad") — pero
entonces el veredicto §6 no debió listar "tasa 2b² — eco de escala con Λ=max b²/2" como dividendo
cuantitativo ni el resumen llamarlo "eco cuantitativo". Es paridad, no física compartida.

**Veredicto (d): AGUANTA (condicional a V.2). Veredicto (e): correcto en el modelo; el eco
cuantitativo y el factor 4 quedan ELIMINADOS como contenido.**

---

## 5. La lógica de expulsión del flujo lineal

El mandato sospechaba un non sequitur ("un flujo lineal con L≥0 decae hacia ker L, no expulsa").
Examen: en el modelo finito, G(s) = e^{−sL}G₀ → G_∞ = P_{ker L}G₀ (proyección HS-ortogonal,
descomposición espectral de L, gap espectral finito-dimensional). La "expulsión" es entonces un
corolario, no un mecanismo: (α) si G_∞ es indefinida, λ_min(G(s)) pasa de >0 a <0 y por
continuidad cruza 0 en s_*<∞: la trayectoria SALE de 𝕄 en tiempo finito — válido; (β) si G_∞ ≥ 0,
por 166.13(c) ker G_∞ ⊇ N y G(s) → ∂𝕄 asintóticamente (nunca la alcanza en tiempo finito) —
"hacia" la frontera es la palabra correcta. **La lógica del doc es válida y, de hecho, el doc
mismo la formula así** ("el flujo lineal NO preserva el cono en general, y ése es el contenido").
Sin cargo lógico. Dos matices adversariales:

1. **La causa de la expulsión no es 166.9.** Es la combinación (166.6(ii): 𝔇>0 en el interior) +
   (convergencia lineal a ker L) + (ker L ∩ 𝕄 = ∅ si m≥1). La narrativa "la expulsión es
   conservación de inercia" superpone la tautología (a) a un mecanismo que funciona sin ella.
2. **"Aplasta exactamente las direcciones off-line": ¿reentra ζ en la descripción?** Las
   direcciones aplastadas son las E_j de los autovectores v_j, que existen por (H-26)(ii) — los
   ceros off-line están en la DEFINICIÓN del modelo finito (se ponen a mano como autovalores
   λ_j = γ_j+ib_j). No es circularidad adicional: es la hipótesis declarada del marco. Pero hay
   que decirlo sin eufemismo: TODO el contenido dinámico cuantitativo del documento (166.13) vive
   en un modelo cuyo input son las posiciones de los ceros. "Dinámica RH-libre" significa aquí
   "sin asumir positividad", no "sin datos de ζ". El doc lo deja leer entre líneas (Obs. 166.4,
   GAP 166.D); el resumen lo proclama sin la línea.

**Veredicto (e), parte lógica: AGUANTA en el modelo finito; sin extensión probada a dim ∞
(GAP 166.D declarado).**

---

## 6. Consistencia 166 ↔ 167 y la dualidad con Rodgers–Tao

**¿Contradicción κ-conservado (166) vs κ-disipado (167)?** No. Son flujos sobre variables
distintas: el flujo de Gram mueve G con W FIJA — y κ = n_−(W) no puede cambiar porque nada que
toque a W cambia (esto es de nuevo la lectura deflacionaria de 166.9: la "conservación" es que la
variable dinámica no aparece en la cantidad); DBN mueve la función Ξ_t, luego la forma, luego su
índice puede caer (de Bruijn 1950, Thm 13: la realidad de los ceros es absorbente; Doc 167,
Teorema 2.3: İ = −2κ − D). **Consistentes.** Nota fina: en el lado 167, llamar "κ" al conteo de
pares no-reales de H_t requiere el puente de Phase 26 (κ=2m=neg.ind) que NO está probado; ambos
documentos lo declaran ([PUENTE], Doc 167 §0; Doc 166 §4.2). Coherencia de etiquetado: correcta.

**¿La dualidad (f) es estructura o verbo?** Lo verificable de la tabla 166-DBN:

- "forma móvil/métrica fija vs métrica móvil/forma fija" — cierto como descripción de los dos
  setups. Pero no hay NINGÚN mapa matemático entre los dos problemas variacionales (el propio doc
  lo registra como [DESEO 166.C]). Sin mapa, "dualidad" es una palabra.
- "RH en la frontera en ambos" — formalmente cierto: RH ⟺ Λ=0 (frontera de {Λ≤0}∩{Λ≥0}, Newman
  1976 + Rodgers–Tao 2020) y RH ⟺ el ínfimo 0 de 𝔇 se alcanza (166.11(c)). Pero el segundo
  miembro es el criterio de Weil reescrito (§3 arriba), de modo que la "dualidad" aparea un
  teorema difícil y nuevo (RT) con una reformulación sin contenido. Isomorfismo de FORMA de
  enunciado, sí — el doc usa exactamente esa palabra ("isomorfa en FORMA") en §0, lo cual es
  honesto; la fila de la tabla "la variable dinámica de uno es la cantidad conservada del otro"
  ya no lo es tanto: sugiere una estructura simpléctica/acoplada que nadie construyó, y la mitad
  "conservada" es Sylvester (vacía).
- El único candidato a contenido compartido era el eco cuantitativo 2b² ↔ b²/2 — eliminado en
  §4.3 (gauge).

**Veredicto (f): ANALOGÍA VERBAL honesta en §0, sobre-estructurada en la tabla §4.2; consistencia
166↔167 verificada.**

---

## 7. Cargos menores verificados (sin consecuencias)

- Prop. 166.5′(c): A_t(σG) = J^*A_{−t}(G)J re-derivado con JU_t = U_{−t}J — correcto; el promedio
  J-simétrico mata A_J por convexidad — correcto.
- Prop. 166.7′: U_t^*W = WU_t^{−1} a partir de U_t^*WU_t = W con W invertible — correcto; la
  partición en dos bloques unitarios y Stone/álgebra lineal — correcto. Buena pieza explicativa
  (la versión métrica del muro de D165).
- Prop. 166.2(d): T = G₁^{−1/2}G₂^{1/2}, T^*G₁T = G₂ — correcto.
- Prop. 166.3(a): S₀ = sign(W), WS₀ = |W| ≥ ε — correcto bajo (H-W); la dependencia de (H-W)
  (W acotadamente invertible, GAP 166.A) es el talón de Aquiles de TODA la transferencia al
  objeto aritmético, y está declarada.
- Prop. 166.11: el cambio de producto de fondo para ortogonalizar N ⊕ K₁ altera el valor de 𝔇
  solo por constantes de equivalencia; "inf = 0" sobrevive — correcto, aunque merecía una línea.
- 𝔇₂ con peso e^{−2|t|} vs 𝔇 con e^{−|t|}: consistente (cuadrado del peso para el cuadrado de la
  norma); ambas finitas ⟺ b_max < ½ con (H-26)(iii).

---

## 8. Resumen final

**Veredictos:** (a) 166.9 CORRECTO-PERO-VACÍO (Sylvester re-etiquetado; no es teorema dinámico;
"salto en ∂𝕄" no probado, solo indefinición). (b) Hessiano CORRECTO-PERO-VACÍO (positividad
automática de una funcional elegida cuadrática; cuadrado genuino; prueba solo en modelo finito;
peso = gauge, no puerta de ζ). (c) W punto fijo: CORRECTO pero condicional a V.1 — el
"incondicionalmente" del resumen es sobreventa — y "RH = W en el cono" es el criterio de Weil
verbatim: cero contenido nuevo. (d) 166.6/φ(b) AGUANTA (re-derivada exacta; condicional a V.2;
la mejor pieza del documento). (e) 166.13/ℓ(b) correcto en el modelo y la lógica de expulsión es
válida; pero el coeficiente 2b² es artefacto del peso (ℓ_a ≈ 2b²/a³) y el "factor 4" frente a
A.15 no existe como invariante: el eco cuantitativo queda eliminado, solo sobrevive el exponente
b² forzado por paridad. (f) Dualidad con Rodgers–Tao: analogía de forma de enunciado, sin mapa;
aparea un teorema (RT) con una tautología (166.9) + una reescritura (166.11(c)); consistente con
el Doc 167 (flujos sobre objetos distintos, sin contradicción).

**Tres hallazgos principales:**

1. **Ningún teorema es falso, pero los dividendos se degradan dos niveles.** De los cuatro
   dividendos del veredicto §6 del Doc 166, sobrevive íntegro solo 166.6 (φ(b), condicional a
   V.2). 166.9 es contabilidad (Sylvester), la lectura "punto fijo universal" es Weil 1952 con
   decoración dinámica y condicional a V.1, y el único puente cuantitativo con DBN (2b²↔b²/2) es
   dependiente de gauge. El veredicto correcto del Doc 166 no es B′: es B con UNA cota nueva
   condicional (166.6) y un lenguaje nuevo.
2. **El factor 4 "sin explicar" no es un enigma: es normalización.** Recomputados ambos lados
   en cerrado: la heurística de par aislado de DBN da Λ ~ b²/2 (correcta); ℓ(b) = 2b² es correcta
   PERO con peso e^{−2a|t|} se vuelve 2b²/a³ — el coeficiente no es invariante bajo la libertad
   de gauge del peso ni del tiempo del flujo. Debe tacharse de [PUENTE 166-E] como "dato".
3. **Patrón (iii) en los titulares:** "A_t(W)=0 incondicionalmente" (resumen §0) es exactamente
   (H-26)(i) = V.1 de Phase 26, no probado. El cuerpo del Doc 166 etiqueta bien; el resumen
   ejecutivo y la interpretación de 166.13 hablan como si V.1 fuera teoría general. Lo mismo, en
   grado menor, con el alcance finito-dimensional de 166.10/166.13 (GAP 166.D declarado en §4.3 y
   ausente de los enunciados-titular). Recomendación: erratas de redacción, no de matemática —
   pero en este programa la redacción ES la línea de defensa.

**Referencias.** A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
Comm. Sém. Math. Lund (1952) 252–265. — L.S. Pontryagin, Izv. Akad. Nauk SSSR 8 (1944) 243–280. —
I.S. Iokhvidov, M.G. Krein, Trudy Moskov. Mat. Obshch. 5 (1956). — J. Bognár, *Indefinite Inner
Product Spaces*, Springer 1974 (cap. IV–V). — T.Ya. Azizov, I.S. Iokhvidov, *Linear Operators in
Spaces with an Indefinite Metric*, Wiley 1989 (cap. 1 §8, cap. 2 §2). — M.G. Krein, H. Langer,
Acta Sci. Math. (Szeged) 34 (1973) 191–230. — H. Langer, *Spectral functions of definitizable
operators in Krein spaces*, LNM 948, Springer 1982. — N.G. de Bruijn, Duke Math. J. 17 (1950)
197–226. — C.M. Newman, Proc. AMS 61 (1976) 245–251. — B. Rodgers, T. Tao, Forum Math. Pi 8
(2020) e6. — M. Reed, B. Simon, *Methods of Modern Mathematical Physics I*, 1980. —
[GAP de literatura] No conozco tratamiento publicado de la inercia para familias de simetrías
fundamentales degenerando (coincide con GAP 166.F del Doc 166); la afirmación de novedad del
funcional 𝔇 con peso calibrado no la puedo refutar desde literatura conocida.
