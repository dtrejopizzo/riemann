# ROUND_003_9 — Selección: métrica no local de la realización theta

Memo de selección, no de construcción. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}. Fuentes de la 211 citadas como HY (`POWER_HYPERBOLIC_MODEL_GRAM.md`), GS
(`POWER_GRAM_SLICES_OBSTRUCTION.md`), CONE001 (`POWER_CONE_001.md`), BRIDGE002 (`POWER_BRIDGE_002.md`).
Etiquetas: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

## Cotejo

### Búsqueda realizada

- Lectura primaria entera: HY §§1–5 y §§12.2–12.7; CONE001 §§1–2; BRIDGE002 §6;
  `ROUND_001_L.md` §§1–4 (por líneas citadas), `ROUND_003_4.md`, `OBJECT_SPEC.md`, `RULES_AVOID.md`,
  `LEDGER.md`, `README.md`; README de la fase 209; `ANNEX_211_GRAM_HYPERBOLIC.md` §§0–1;
  `phase-114-closing-the-four-rows/114_d_139_THETA_PAIR_METRIC_NO_GO.md` §0 y §1 inicial.
- grep en `03-research/` (todas las fases), `04-papers/47*`, `04-papers/48*`,
  `05-meta-and-planning/` por: «Kontorovich», «Lebedev», «métrica no local», «metrica no local»,
  «nonlocal metric», «entrelaz», «intertwin», «Stieltjes», «Herglotz», «traza que represente»,
  «Green positivo». Sin coincidencias para Kontorovich/Lebedev y para «métrica no local» como frase.
  «nonlocal metric» sólo en D.139 (fases 114/116, mismo archivo). «Green positivo» sólo en HY, en
  sus ecos del grid/crucigrama/índice y en `POWER_GREEN_PAIR_TP2_SCOPE_111.md` (no abierto entero).
  «Stieltjes» en la fase 206 (NODE_001: integral de Stieltjes contra d(ψ − t), otro sentido).
  «Herglotz» en las fases 136–137 (matriz-Herglotz de una resolvente comprimida, otro objeto).
- GS §§17–19 los conozco sólo por el anexo `ANNEX_211_GRAM_HYPERBOLIC.md` §0 y por `RULES_AVOID.md`
  D9, D14, D16; no los releí en primaria. LINK_014 de la 209 sólo por su enunciado (Teorema 3 y
  estado, l. 151–173). La ausencia de coincidencias no prueba novedad; la §2 muestra además que no
  la hay en la clase examinada.

### (1) Antecedente más cercano

- HY §§4–5 (PROVED para el modelo φ_a = e^{−a cosh 2t}): M_a(u)/u = ½Tr(H + u²/4)^{−1} con
  H = −D_r² + a²e^{2r} positivo e independiente de u (REP); de ahí la identidad de resolventes
  (uR_u + vR_v)/(u+v) = (H + uv/4)R_uR_v y la suma de cuadrados GRAM para todos los tamaños.
- HY §12.6 (PROVED como realización): espacio ℋ = L²((0,∞), sech(πω/2)dω) ⊕ ℝ³, Q(v), C, D, B̄, h,
  con ⟨Y_ν(2π), h⟩ = Z(2ν) y la ecuación fuerte Y_rr = (b² + ν²)Y + 2DY_r + (−C + 2bB̄)Y.
- HY §12.7 (NO-GO con clase PROVED): no hay métrica local, acotada, estrictamente positiva M(r) con
  M′ = −DM − MD y −C + D² + 2bB̄ simétrico en M(r).
- `ROUND_001_L.md` Teorema 2.1, Cor. 2.2, Prop. 4.2 (PROVED relativo a Herglotz–Riesz, Pick y
  Blaschke, CITED): la escalera K_ij = (L(32+i)+L(32+j))/(63+i+j) es PSD en todos los tamaños si y
  sólo si M es real-positiva en Π = {Re u > 0}, y entonces M = Σ_k r_k·2u/(u² + τ_k²), r_k ≥ 0. El
  índice (README l. 1791, «núcleo real de tipo Pick») y la propia memo registran esta positividad de
  tipo Herglotz como **reformulación del objetivo**.
- D.139 (fase 114): para el par theta (LD, L) en coordenada logarítmica, toda métrica positiva
  invariante por traslación definida en todo el dominio es nula (el vector theta está en el núcleo
  de C = ∂_x + φ′ y su transformada no se anula en casi todo punto). Excluye métricas globales de
  convolución antes de cortar los momentos de Tate; no excluye métricas no invariantes.
- Fase 209: CONSTRUCTOR_001 (NO-GO de J + C compacto), 005 (núcleo SPD −R_α), 011 (mapa
  Mellin–Gauss continuo a un núcleo positivo; la forma inducida no coincide con Q_T: la alta
  frecuencia corregida separa), 012–014 (dominaciones uniformes; LINK_014: toda combinación fija no
  negativa AκG + Bκvv* + CΠ con el mismo a_d tiene |Q|/E → 0), 016 (positividad sólo en la imagen no
  amplía el cono). Ninguno es una métrica de la realización theta; todos fallan en el enlace con la
  forma, no en la positividad del núcleo auxiliar.

### (2) El objeto, escrito

La realización (HY §12.6) y lo que la métrica debería dar se escriben en §1. La «métrica 𝒢» que la
regla del dueño pide explicitar se formaliza en §2 como la clase 𝒞_G de identidades de Green de tipo
REP (las únicas que, en el antecedente HY §§4–5, producen GRAM). El Lema 2 prueba que en esa clase
los datos observables de 𝒢 (la medida espectral de H vista desde la observación) están
**determinados** por M y son exactamente sus datos de Herglotz; su positividad es la escalera
completa. No hay ℋ_T, V_T ni ρ_T nuevos que escribir: la solución canónica es el espacio de la medida
de borde de M, cuyo signo es el objetivo.

### (3) ¿Esquiva la dificultad del antecedente?

No. La dificultad de HY §12.7 es local (la ecuación métrica fuerza exponentes incompatibles). Pasar
a métricas no locales o no acotadas evita esa prueba concreta, pero el Lema 2 muestra que cualquier
métrica, local o no, que produzca una identidad de tipo REP tiene sus datos observables fijados y su
positividad equivale a la real-positividad de M, ya registrada como reformulación. La no localidad no
cambia lo que hay que firmar.

### (4) Conexión con la positividad global

Cadena exacta (sin margen): identidad REP con 𝒢 ⪰ 0 ⟹ K_M PSD en todos los tamaños (Lema 2(a),
PROVED) ⟹ escalera de BRIDGE002 §6 PSD ⟹ no negatividad de la forma sobre todos los tests suaves
compactos, en particular sobre P_T para todo T (BRIDGE002 §6, PROVED allí). La recíproca hasta
«existe 𝒢 ⪰ 0 en 𝒞_G» también vale (Lema 2(b)). La conexión existe, pero es una equivalencia con la
escalera: no es una desigualdad intermedia.

### (5) Líneas de ruptura para cΛ y a_P

Λ entra en 𝒢 sólo a través de M, linealmente (§3): L_c(a) = L(a) − (c − 1)Σ_n Λ(n)n^{−a} y
L_P(a) = L(a) + Σ_{p<P}Σ_{k≥1}(log p)p^{−ka}. La línea que se rompe es r_k ≥ 0 en la
representación de Herglotz de M_c o M_P, es decir, la positividad de la medida de borde: la misma
afirmación que se quiere probar (211 LEDGER C43: la ventana en c se cierra en c = 1 por ambos lados).
No hay paso de signo intermedio que falle: punto (5) sin respuesta. La candidata no está lista para
construcción.

## 1. La realización theta y la ecuación de la métrica

**1.1 Objetos (HY §12.6, PROVED allí).** ℋ = L²((0,∞), ρ(ω)dω) ⊕ ℝ³, ρ(ω) = sech(πω/2),
λ_j = j + ¼; Q(v) = (cos ωv, cosh λ_0v, cosh λ_1v, cosh λ_2v); C multiplicación por −ω² y λ_j²;
D multiplicación por d(ω) = 1 + ω coth(πω/2) + (15/2)cosh(πω/2)/cosh(2πω) y masas (−29/4, −23/4, −9/4);
B̄ la clausura de BQ(v) = sinh v Q′(v) + cosh v DQ(v) sobre S = span{Q(v)}; h ∈ ℋ con
⟨Q(v), h⟩ = q_θ(v) = Φ(v/2)e^{2π cosh v}. Para b = e^r > 0,

    Y_ν(b) = ∫_0^∞ e^{−b cosh v} cosh(νv) Q(v) dv,
    Y_rr = (b² + ν²)Y + 2D Y_r + (−C + 2bB̄)Y,
    ⟨Y_ν(2π), h⟩ = ∫_0^∞ Φ(v/2)cosh(νv)dv = Z(2ν).

**Observación 1.2 (PROVED, una línea).** La observación sólo lee la rebanada b = 2π: el factor
e^{2π cosh v} de q_θ cancela exactamente el núcleo e^{−2π cosh v}. La variable de escala r y su
ecuación son andamiaje; la observación de cualquier otra rebanada b ≠ 2π no es Z. Una métrica en r
sólo sirve si su identidad de Green, evaluada en b = 2π, reproduce M = Z′/Z.

**1.3 Qué debería cumplir la métrica (traducción del antecedente).** En el modelo, la identidad que
da GRAM es REP: M(u)/u = ½Tr(H + u²/4)^{−1} con H ⪰ 0 independiente de u, obtenida de la ecuación
de Wronskiano (y_x² z_x′)′ = y_x² y de la simetría de −D² + a²e^{2r} en L²(dr). Para la realización
theta la condición necesaria local es la de HY §12.7 (M′ = −DM − MD y simetría de E en M(r)), excluida
allí para M local acotada. Una métrica no local es una forma 𝒢 ⪰ 0 sobre funciones de r con valores
en ℋ (núcleo 𝒢(r, s)) en la que L = −∂_r² + 2D∂_r + b²I + E(b) sea simétrico con condiciones de borde
compatibles con h; su función de Green G_ν daría, por el argumento del Wronskiano, una identidad de
la forma

    (REP-𝒢)   M(u) = βu + u⟨g, (H + u²)^{−1} g⟩_𝒦,   H ⪰ 0 independiente de u, β ≥ 0,

con 𝒦 el completado de (funciones, 𝒢), H el operador asociado a L y g el vector de borde dado por h
(reescalando u ↦ u/2 si se quiere la normalización de HY). Que la simetría de L en 𝒢 implique
(REP-𝒢) es ARGUED (es el cálculo de HY §§3–4 con ⟨·,·⟩ sustituido por 𝒢; no lo escribo porque el
Lema 2 hace innecesaria su forma exacta). Lo que sigue clasifica (REP-𝒢) directamente, sin pasar por
L ni por r.

## 2. La métrica queda determinada y su positividad es el objetivo

**Clase 𝒞_G.** Ternas (𝒦, H, g) y β ≥ 0, con 𝒦 un Hilbert real cualquiera (cualquier dimensión,
cualquier origen: local, no local, no acotado), H autoadjunto ⪰ 0 en 𝒦, g ∈ 𝒦, tales que
(REP-𝒢) vale para u en un conjunto X ⊂ (0,∞) de unicidad para funciones holomorfas en Π (por
ejemplo la escalera 31.5 + ℕ de BRIDGE002 §6, que es de unicidad por ROUND_001_L Lema 1.3, o un
intervalo). Aquí M(u) = L(u + ½) con L de CONE001 §1:

    L(a) = 1/a + 1/(a−1) − (log π)/2 + ψ(a/2)/2 + ζ′(a)/ζ(a),   ζ′/ζ(a) = −Σ_n Λ(n)n^{−a}.

M es meromorfa en ℂ e impar (Z(u) = C∫Φ(t)cosh(ut)dt es par y entera, CONE001 §2).

**Lema 2 (circularidad en 𝒞_G).**

(a) (PROVED) Si (𝒦, H, g, β) ∈ 𝒞_G, entonces K_M(u,v) = [M(u)+M(v)]/(u+v) es PSD en todo subconjunto
finito de X, con la suma de cuadrados explícita

    Σ_ij c_i c_j K_M(u_i,u_j) = β(Σc_i)² + ‖H^{1/2}Σ_i c_iR_ig‖² + ‖Σ_i c_iu_iR_ig‖²,
    R_i = (H + u_i²)^{−1}.

(b) (PROVED relativo a `ROUND_001_L.md` Teorema 2.1 y Prop. 4.2, que a su vez son PROVED relativos a
los clásicos C1–C3 citados allí) Recíprocamente, si K_M es PSD en todo subconjunto finito de X,
existe (𝒦, H, g) ∈ 𝒞_G con β = 0: 𝒦 = ℓ², H = diag(τ_k²), g_k = (2r_k)^{1/2}.

(c) (PROVED relativo a la unicidad de la medida en la representación de Herglotz–Riesz y a la
inversión de Stieltjes, CITED) Para toda (𝒦, H, g, β) ∈ 𝒞_G, β = lim_{u→∞} M(u)/u y la medida
espectral μ_g de H en g (μ_g(E) = ⟨g, 1_E(H)g⟩) están determinadas por M. La única libertad es la
equivalencia unitaria sobre el subespacio cíclico de g y el complemento ortogonal, que no interviene.

(d) (PROVED, de (a)–(c)) En consecuencia, para la realización theta, existe una métrica 𝒢 —local o
no, acotada o no— cuya identidad de Green sea de tipo (REP-𝒢), si y sólo si la escalera de BRIDGE002
§6 es PSD en todos los tamaños; y entonces la parte observable de 𝒢 es canónica: la medida μ_g es la
medida de borde de M, atómica, con masas r_k y posiciones τ_k² (ROUND_001_L Prop. 4.2). La
positividad de 𝒢 en 𝒞_G es literalmente la positividad de esa escalera.

*Demostración.* (a) Para u, v > 0 las resolventes conmutan y
uR_u + vR_v = R_uR_v[u(H + v²) + v(H + u²)] = (u + v)R_uR_v(H + uv). Luego
K_M(u,v) = β + ⟨g, (H + uv)R_uR_vg⟩ = β + ⟨H^{1/2}R_ug, H^{1/2}R_vg⟩ + uv⟨R_ug, R_vg⟩, usando que
R_u, R_v, H^{1/2} son autoadjuntos y conmutan y que R_ug ∈ Dom(H) (H^{1/2}R_u acotado). Cada sumando
es un núcleo de Gram; la forma cuadrática es la escrita.

(b) Por ROUND_001_L Teorema 2.1 hay F real-positiva en Π con F = M en X. M es meromorfa en ℂ y F
holomorfa en Π; X tiene un punto de acumulación en Π o es de unicidad, así que M = F en Π (en el
caso de la escalera, la unicidad es la de ROUND_001_L Lema 1.3 aplicada a M − F, que es meromorfa de
crecimiento controlado en Π: es exactamente el paso usado allí en Cor. 2.2). Por Prop. 4.2,
M(u) = Σ_k r_k·2u/(u² + τ_k²), r_k ≥ 0, sin término lineal. Con H = diag(τ_k²) y g_k = (2r_k)^{1/2},
u⟨g, (H + u²)^{−1}g⟩ = Σ_k 2r_ku/(τ_k² + u²) = M(u); g ∈ ℓ² porque Σ r_k/(1 + τ_k²) < ∞ (finitud de
M(1)).

(c) De (REP-𝒢), M(u)/u = β + ∫ dμ_g(λ)/(λ + u²) en X, y ambos lados son meromorfos/holomorfos en
Π; luego la igualdad vale en Π, y en particular s ↦ ∫dμ_g(λ)/(λ + s) queda determinada para s > 0,
con β = lim M(u)/u (convergencia dominada: ∫dμ_g/(λ+u²) → 0 si μ_g es finita, lo es porque
g ∈ 𝒦). La transformada de Stieltjes de una medida positiva finita en [0,∞) determina la medida
(inversión de Stieltjes, CITED). La medida espectral determina H|_{cíclico de g} hasta equivalencia
unitaria (teorema espectral, CITED).

(d) Junta (a), (b), (c) con BRIDGE002 §6 (la escalera es K_M sobre X = 31.5 + ℕ, desplazando
a = u + ½). ∎

**Clase y alcance del lema (NO-GO de circularidad con clase, PROVED en los términos anteriores).**
Clase: toda identidad de Green que represente M en la forma (REP-𝒢), con operador positivo
independiente de u, sobre cualquier Hilbert. En esta clase la «métrica no local» no es un objeto
libre: es la representación de Herglotz de M, cuya positividad está registrada como reformulación del
objetivo (IDX README l. 1791; ROUND_001_L l. 27). Resolver la ecuación de entrelazamiento por Mellin o
por cualquier otra transformada produce, si produce algo, esa misma medida.

**Corolario 2.1 (variante con resto, PROVED relativo a ROUND_001_L Teorema 3.1).** Si se pide sólo
M = M_𝒢 + F con M_𝒢 de tipo (REP-𝒢) no nula y F real-positiva (un «resto controlado» positivo), la
medida de M_𝒢 queda dominada por la de M, que bajo esa hipótesis es atómica (es literalmente la
rigidez R-comp de `OBJECT_SPEC.md` §3 con M0 = M_𝒢/ε). No hay métrica de 𝒞_G que pague una parte del
signo y deje un resto positivo independiente: su medida tiene que estar dentro de la de M.

**Observación 2.2 (involución modular; ARGUED).** La simetría θ(1/t) = √t θ(t) da Φ par, Z par y M
impar. En el Lema 2 esa paridad ya está consumida: es lo que hace que la medida de Herglotz sea
simétrica y que (REP-𝒢) dependa de u². Una factorización 𝒢 = 𝒥*𝒥 con 𝒥 la involución no aporta signo:
toda 𝒢 ⪰ 0 es un cuadrado, y la paridad la comparte cualquier Φ par (cualquier dato con ecuación
funcional del mismo tipo, por ejemplo Davenport–Heilbronn en la normalización correspondiente), de
modo que un argumento que sólo use la involución no tiene línea que se rompa en ese falsificador.
No lo desarrollo como lema.

**Observación 2.3 (núcleo explícito tipo Kontorovich–Lebedev; PROVED como cuenta, sin signo).** En el
modelo, y_x(r) = K_{√x}(ae^r) con K_ν la función de Macdonald (∫_0^∞e^{−b cosh v}cosh(νv)dv = K_ν(b),
CITED), y el operador H es diagonalizable por una transformada de esa familia con densidad de
Plancherel positiva. Esa positividad es universal (no depende de Φ) y por el Lema 2(c) no puede ser
la métrica: la métrica está fijada por M. Una «función explícita» (cociente de Gammas, theta, su
transformada) cuya positividad fuese la de 𝒢 tendría que codificar μ_g, es decir la escalera.

## 3. Dónde entra Λ

Integralidad: Φ = Σ_n n^{−1/2}h(t + log n) tiene coeficiente 1 en cada n (en la forma modal, 1 sobre
los cuadrados de la theta). Producto de Euler: Σ_{d|n}Λ(d) = log n es exactamente la identidad que
convierte la derivada logarítmica de Σn^{−a} en −ΣΛ(n)n^{−a}. Así Λ aparece en M, de forma lineal y
explícita, por ζ′/ζ en L (CONE001 §1, PROVED allí). En 𝒞_G, por el Lema 2(c), μ_g es la medida de
borde de M, que depende linealmente de M; la única no linealidad es g_k = (2r_k)^{1/2}, que no añade
información. La cláusula O10 se cumple formalmente (se trabaja del lado de Λ), pero sin mecanismo:
el cruce de la derivada logarítmica está en la definición de M, no en un paso de signo.

Para cΛ: M_c(u) = M(u) − (c − 1)Σ_nΛ(n)n^{−(u+½)} (ARGUED que BRIDGE002 §6 se transporta con la
inversa de Dirichlet de los coeficientes de cΛ en lugar de μ; CONE001 §1 da el término del peine
proporcional a c). Para a_P: M_P(u) = M(u) + Σ_{p<P}Σ_k (log p)p^{−k(u+½)}. En ambos casos la línea
que falla del Lema 2 es la existencia de (𝒦, H, g) con μ_g ≥ 0, es decir (b): exactamente la
positividad de la escalera del modelo alterado. No hay otra línea.

## 4. Inventario de núcleos no locales ya probados (sólo lo pertinente)

- 211, modelo hiperbólico (HY §§4–5): Green positivo de todos los órdenes, PROVED; sin transferencia
  (§6–7: mezclas y convoluciones positivas no transfieren; §§9–12.4: flujo de escala, prefactores,
  derivas escalares, excluidos en sus clases).
- 211, HY §12.7: métrica local acotada, NO-GO. GS §2.3: factorización Hankel traslacional de A
  excluida. GS §4.3: referencias G0, H0 no PSD. GS §§17–19 (por el anexo): suma de cuadrados
  resonante con margen, comparación Off contra E_y refutada (pares k, k+1), grafo térmico y Q_B; ningún
  núcleo que represente A con resto controlado.
- 114 D.139: métrica traslacional global del par theta, nula.
- 209: núcleos positivos auxiliares (005, 011) sin enlace con la forma; dominaciones fijas (012–014)
  fallan con |Q|/E → 0; 016 no amplía el cono. Fallo común: el núcleo positivo no ve el signo de la
  forma; la identificación con la forma pierde la parte que lleva el signo.

## Resultado

Sin mecanismo nuevo, con una pieza de NO-GO de circularidad con clase (PROVED en los términos del
Lema 2, relativo a ROUND_001_L y a clásicos CITED). La «métrica no local» de la realización theta,
dentro de la clase de identidades de Green de tipo REP (operador positivo independiente de u, cualquier
Hilbert, local o no), queda determinada por M en su parte observable, y su positividad es la escalera
de BRIDGE002 §6, ya registrada como reformulación. La candidata no pasa la puerta de selección.

## Qué se probó

- Lema 2(a): REP-𝒢 ⟹ K_M PSD con suma de cuadrados explícita (PROVED).
- Lema 2(b)–(d): recíproca, unicidad de los datos observables y equivalencia con la escalera (PROVED
  relativo a ROUND_001_L Teorema 2.1, Prop. 4.2 y a Herglotz–Riesz/Stieltjes CITED).
- Corolario 2.1: una métrica de 𝒞_G con resto real-positivo cae en la rigidez R-comp (PROVED relativo
  a ROUND_001_L Teorema 3.1).
- Observación 1.2: la realización §12.6 sólo observa la rebanada b = 2π (PROVED, cuenta directa).

## Qué falló y por qué

- La métrica no aparece como objeto libre: en 𝒞_G sus datos son los de Herglotz de M; resolver el
  entrelazamiento (por Mellin o por otra vía) no puede dar otra cosa. Circularidad, no imposibilidad
  del signo.
- La involución modular y las densidades de Plancherel explícitas son universales o compartidas por
  falsificadores con ecuación funcional; no llevan la línea de ruptura (ARGUED).
- Punto (5): para cΛ y a_P lo único que falla es la positividad de la medida de borde, que es el
  objetivo alterado.

Queda NO excluido:
1. Identidades de Green que no sean de tipo REP: operador dependiente de u de forma no resolvente,
   formas indefinidas (Kreĭn) con vector neutro no radical (`ROUND_003_4.md` §3, punto 1), o
   identidades sobre A(t,s) que no pasen por M y usen una estructura que el Lema 2 no ve (por
   ejemplo, construir los vectores de Gram de A desde operaciones aritméticas con verificación
   algebraica, como HY §5 en el modelo). Esto último es el propio (G) sobre la escalera, sin objeto.
2. Métricas no locales que den (REP-𝒢) sólo para una parte de M con un resto que no sea
   real-positivo (fuera del Corolario 2.1).
3. Realizaciones distintas de §12.6 (otras Q, otras observaciones no continuas).

## Siguiente paso concreto

No relanzar la «métrica no local de la realización theta» en la clase REP: anotar el Lema 2 junto a
la entrada de reserva de métricas no locales (memoria de selecciones y `RULES_AVOID.md` D15) como
circularidad con clase. Una reapertura tendría que salir de la clase 𝒞_G: escribir una identidad que
represente A o K_M con un operador que dependa de u de forma no resolvente, o con métrica indefinida,
y señalar la línea que se rompe para cΛ y a_P antes de cualquier derivación.
