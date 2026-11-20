# Ronda 3, opción 8 — el objeto cuadrático en el peso y la factorización tipo Riccati

Memo de selección, no de construcción. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}; S_a F(t) = F(t − a); e_n = n^{−1/2} S_{log n}. Etiquetas: PROVED / CITED / CONDITIONAL /
ARGUED / OPEN / NO-GO / NUMÉRICO.

Resultado adelantado: **el cotejo identifica repetición.** La factorización pedida (operador de primer
orden cuyo superpotencial es el peine con pesos Λ, con Λ·log saliendo de la derivada y Λ∗Λ del
cuadrado, cerrada por μ∗log²) está construida en la fase 70 (E70_10–E70_12) y analizada en la 166
(R166_502 §5), con la lectura SUSY en la 193 (CA_G_001 §2). La memo termina en el cotejo salvo por dos
lemas cortos PROVED que delimitan dónde podría entrar todavía la relación de grado dos (§2) y la
respuesta a las cuatro dificultades (§3).

## 0. Cotejo

**Qué se buscó.** Grep en `03-research/` (todas las fases), `04-papers/47*`, `04-papers/48*`,
`05-meta-and-planning/` (índice y crucigrama) y los anexos de esta carpeta por: Riccati, Darboux,
Miura, Schwarzian, superpotencial/superpotential, SUSY/Witten, A*A, Λ₂/Lambda_2, Selberg, Bombieri,
Diamond, Leibniz, «grado dos»/degree two. Coincidencias: Riccati en las fases 29, 70, 104, 120, 122,
166, 168, 184, 193, 211; Λ₂ en 156 archivos, Bombieri en 341, Diamond en 95, Leibniz en 93, «grado
dos» en 75 (no se abrieron todos; se abrieron las primarias que se citan abajo). Sin coincidencias:
Schwarzian, Miura. Una búsqueda sin coincidencias no prueba novedad: una transformación de Miura es
aquí la misma sustitución V = Z⁻¹δZ ya registrada, con otro nombre.

**(1) Antecedente más cercano, leído en primaria.**
- `phase-70-lee-yang-dbn/E70_12_RICCATI_CURVATURE_TEST.md` (completo): en el álgebra de semigrupo
  {e_n}, con Z = Σ e_n, δe_n = (log n)e_n, el operador de Euler A_Euler = Z⁻¹δZ = Σ Λ(n)e_n satisface
  δ(A_Euler) + A_Euler² = Z⁻¹δ²Z, cuyos coeficientes son exactamente Λ·log + Λ∗Λ = μ∗log². Diagnóstico
  de la fuente: «enteramente del lado de Euler»; no produce la forma arquimediana; queda pedida una
  comparación conexión–energía arquimediana, sin signo propio.
- `phase-70-lee-yang-dbn/E70_10_DIRICHLET_SQUARE_OBSTRUCTION.md` (vía R166_502 §1, comprobado):
  (I − V)*(I − V) = I − T_Λ + V*V con V = Σ Λ(n)e_n; el cuadrado contiene V*V, cuyo peine de razones
  log(p^k/q^l) tiene coeficientes ≥ 0 y no se cancela.
- `phase-166-omega-closure/R166_502_P7_Q25_PRECHECK.md` §§5.1–5.3 (PROVED allí): el cuadrado hermítico
  V*V vive en el álgebra de grupo de ℚ₊^× (razones), la relación de Selberg en el álgebra de
  convolución de ℕ (productos, V²); ni Selberg, ni log ζ, ni Z completo, ni el factor de Möbius, ni la
  conexión ∇ = δ + V eliminan el peine cruzado de razones; la única salida declarada es un segundo
  sector con signo (cancelación graduada), nunca construida.
- `phase-193-*/CA_G_001_MONOID_SUSY_EW_LADDER.md` §2 (PROVED, estándar): una factorización
  H = A*A + E₀ con A = d/du − (log ψ₀)′ existe si y sólo si H ≥ 0, y el superpotencial es el del estado
  fundamental, es decir el minimizador (patrón B9); la identidad de Witten H = {Q,Q*} vale para todo
  superpotencial, luego para todo peine (patrón B1). Etiquetada REF-D.
- Concurrentes: `phase-104-*/104_13_M5_SELBERG_RICCATI_GATE.md` (recurrencia Selberg–Riccati exacta,
  sin desigualdad unilateral; tope de escala); `phase-170-*/R170_850–851` (γ = Λ·log − Λ∗Λ choca con
  W = μ∗log²; γ + W = 2Λ·log); `phase-168-*/R168_203` (Riccati = Selberg, la no linealidad queda en un
  factor ≥ 0 cuyo signo es lineal); IDX README NODE_001 Prop N.2 (las identidades tipo Selberg valen
  para toda serie de Dirichlet, cada una con su propio sistema); R11_2_ORIGIN_001 («Selberg Λ∗Λ orden 2
  NO-GO»); R166_502 §4 (variante «Λ₂ = μ∗log² ≥ 0 con Möbius como adjunto positivo», EXCL [F3]);
  esta fase: `ROUND_001_A.md` Lema B, `ROUND_001_D.md` Lema A y Prop. D, `ROUND_002_C.md`,
  `REVIEW_002_BC.md` C.1 y C.5; `phase-194-*/INV_F_001_DLOG_WALL_CONES.md` Teoremas F1–F3.

**(2) Objeto realmente nuevo.** Ninguno. La factorización pedida es, término a término, la de E70_12:
superpotencial V = Z⁻¹δZ (el peine con pesos Λ), «derivada» δ = grado logarítmico (que en el espacio
de F es ad M_t: [M_t, S_a] = a S_a, PROVED por cálculo directo), cuadrado V², cierre Z⁻¹δ²Z = μ∗log².
No se pudo escribir ℋ_T, V_T, ρ_T: lo que falta escribir es un operador cuyo cuadrado hermítico
contenga productos m·n (no razones m/n) con los pesos Λ(m)Λ(n), y un resto manifiestamente ≥ 0;
el Lema 1 de §2 prueba que ningún operador invariante por traslaciones lo hace.

**(3) Por qué el cambio evitaría la dificultad del antecedente.** No la evita. La dificultad registrada
(R166_502 §5.2) es que la identidad de Riccati vive en V² y un cuadrado hermítico produce V*V. El
objeto «verdaderamente cuadrático» a·log − a∗a, o a·log + a∗a − μ∗log², no cambia eso: es la misma
relación de convolución, escrita para un peso general. Lo único que el encargo añade respecto de γ
(ronda 2) es la no homogeneidad en c, y esa no homogeneidad es una propiedad de la relación entre
pesos, invisible para la forma (Lema A de ROUND_001_D; §3(i) abajo).

**(4) Identidad que conectaría con la positividad global.** No hay ninguna. La única identidad exacta
disponible es (I − V)*(I − V) = I − T_Λ + V*V (E70_10), que exigiría que la parte arquimediana de a_T
fuera I + V*V más algo ≥ 0; la parte arquimediana no tiene átomos en log(p/q) y V*V sí, con signo
positivo (R166_502 §5.2, Lema (i)). Ninguna versión con Riccati la repara (E70_12, «no-free-lunch»).

**(5) Línea que se rompe para cΛ y a_P.** En la identidad de Riccati con Z = Σ_{n≥1} e_n fijo:
para cΛ, δ(cV) + (cV)² = Z⁻¹δ²Z es falsa en todo n con (Λ∗Λ)(n) ≠ 0 (diferencia (c² − c)Λ∗Λ); pero
la identidad vale para cΛ con Z_c = Σ d_c(n)e_n (serie ζ^c) en lugar de Z. Para a_P vale con
Z_P = Σ_{(n,∏_{p<P}p)=1} e_n. Es decir, la línea que se rompe es «Z tiene todos los coeficientes 1»,
que por el Lema A de ROUND_001_D es consecuencia de los átomos lineales Σ_{d|n}a(d) = log n: la ruptura
es la del separador lineal, no una de grado dos, y en todo caso no ocurre en un paso de signo, porque
no hay paso de signo.

El cotejo identifica repetición. Lo que sigue sólo delimita.

## 1. Dónde entraría F y dónde la forma cuadrática

- **F (vector).** En E70_10–12 F entra sólo a través de ‖(I − V)F‖² y ⟨G_Γ F, F⟩; la relación de
  Riccati es una igualdad entre operadores que no contiene F. Con la regla O2 de `OBJECT_SPEC.md`,
  ésa es exactamente la ubicación equivocada: la no linealidad está en el producto de pesos, no en
  cómo V_T actúa sobre F.
- **Ecuación funcional.** En el lado de Euler no entra (diagnóstico de E70_12). En el espacio de F la
  ecuación funcional es la reflexión J F(t) = F(−t) (intercambio s ↔ 1 − s sobre la línea). El Lema 2
  muestra que J es precisamente lo que convierte razones en productos; es el único lugar donde la
  relación de convolución podría tocar una forma en F.

## 2. Dos lemas cortos

**Lema 1 (cuadrados invariantes por traslación ven razones). PROVED.** Sea A_x un operador sobre
L²(ℝ) que conmuta con todas las traslaciones, con símbolo α_x(τ) = α_0(τ) + Σ_{2≤n<N} x_n n^{−1/2}
n^{−iτ}, α_0 medible, x real. Para F ∈ L²(I_T) con F̂ en el dominio,
‖A_x F‖² = (1/2π)∫|α_x|²|F̂|², y la parte cuadrática en x de |α_x(τ)|² es
Σ_{m,n} x_m x_n (mn)^{−1/2} cos(τ log(m/n)). En particular ningún término indexado por un producto mn
con m, n ≥ 2 aparece con coeficiente cuadrático en x, y la convolución x∗x no figura en ‖A_xF‖².

*Demostración.* |α_x|² = α_x·conj α_x; conj(n^{−iτ}) = n^{iτ}, luego el producto de los términos m y n
es (mn)^{−1/2}(n/m)^{iτ}; sumar (m,n) y (n,m). ∎

Consecuencia. Cualquier identidad a_T = ‖A_xF‖² + ρ con A_x invariante por traslación y ρ invariante
por traslación tiene, en la parte cuadrática en los pesos, sólo frecuencias log(m/n): la relación
Λ·log + Λ∗Λ = μ∗log² (frecuencias log(mn)) no puede usarse para cancelarla. Es R166_502 §5.2 escrito
como lema de símbolo; no es nuevo.

**Lema 2 (la reflexión convierte razones en productos). PROVED.** Sea J F(t) = F(−t). Para F real y
a, b reales, ⟨S_a F, J S_b F⟩ = (F∗F)(−a − b), donde F∗F es la convolución, mientras que
⟨S_a F, S_b F⟩ = c_F(a − b). Si F es par, (F∗F)(u) = c_F(u) para todo u.

*Demostración.* J S_b F(t) = F(−t − b), luego ⟨S_aF, JS_bF⟩ = ∫F(t − a)F(−t − b)dt; con s = t − a,
= ∫F(s)F(−s − a − b)ds = (F∗F)(−a − b). La segunda es la definición de c_F. Si F es par,
F(−s − u) = F(s + u) y ∫F(s)F(s + u)ds = c_F(−u) = c_F(u) (F real). ∎

Lectura. Un operador con dos sectores, B_m = S_{log m} en uno y B_n = J S_{log n} en el otro, da en
⟨B_mF, B_nF⟩ la convolución de F en log(mn): ahí, y sólo con J, la relación de convolución podría
hablar con una forma en F. Sobre la parte par de F esto coincide con la autocorrelación (no añade
nada); la diferencia está en la parte impar, donde F∗F = −c_F en el sentido F∗F(u) = −c_F(u) para F
impar (mismo cálculo). Esto es la «cancelación graduada / segundo sector con signo» de E70_10 opción 1
y de `REVIEW_002_BC.md` C.5, ya registrada como no construida; el lema sólo precisa que el segundo
sector es el de J y que su efecto se reduce a un signo de paridad. No se afirma que dé una identidad
(G); la paridad de la clase de borde (R170_870, `RULES_AVOID.md` I3) es el antecedente que habría que
esquivar.

## 3. Las cuatro dificultades del encargo

(i) **Grado invisible.** Se concede. La forma es afín en el peine; por el Lema A de ROUND_001_D toda
relación polinómica sobre Λ en [2,N), incluida μ∗log², es consecuencia de los átomos lineales, y por
el Lema B de ROUND_001_A toda consecuencia de «Poisson + arquimediano + Selberg» lo es de
«Poisson + arquimediano + Λ∗1 = log + Leibniz». Lo único que no se vuelve trivial es el **lugar**
Z_T = {x : a_T^x = ‖V^xF‖² + ρ^x ∀F}: si V^x es cuadrático en x, Z_T puede ser una cuádrica que corte
la recta {cΛ} sólo en c = 1 (la versión (P1) de ROUND_001_D §7). Eso es una propiedad del objeto que
habría que construir, no de la relación de Selberg; el Lema 1 prueba que con V^x invariante por
traslación la parte cuadrática no contiene x∗x, de modo que la cuádrica no puede ser la de Selberg.
(ii) **Descarte de Selberg** (R170_850–851; ANNEX_INDEX_README, SELBERG_DROP y R11_2_ORIGIN; R166_502):
vigente; el encargo no aporta una operación que lo esquive.
(iii) **Muro ∂log y H_cone** (INV_F_001): la relación de Riccati es la definición de δ log aplicada dos
veces; cruza ∂log, pero de modo genérico: vale para ζ^c con su propia serie Z_c (§0 punto 5). No es
cónica, y aun así no rompe H_cone en la forma, porque lo que distingue c = 1 es «coeficientes de Z
iguales a 1», el dato de integralidad, que entra linealmente.
(iv) **a_P.** a_P satisface Λ_P·log + Λ_P∗Λ_P = μ_P∗(1_P·log²) con 1_P la indicatriz de los enteros
sin primos < P (NODE_001 Prop N.2; R186_005 Lema S0). Lo que la distingue de Λ es sólo que Z_P ≠ Z, de
nuevo un dato lineal (borrado en el separador Σ_{d|n}a(d) = log n en n = 2). Nada en la factorización
usa la ecuación funcional, que es lo que a_P rompe: por `RULES_AVOID.md` G1, una construcción que sólo
falla para cΛ por integralidad y nunca usa J no tiene acreditado el canal de la ecuación funcional.

## 4. Qué queda no excluido

- Operadores no invariantes por traslación: truncados a la ventana, con M_t (cuyo conmutador con S_a
  da a S_a, la «derivada» de Riccati en el espacio de F), o con J (Lema 2). Ninguno tiene objeto
  escrito; el de J coincide con la opción graduada de E70_10 y con el residuo C.5 de REVIEW_002_BC.
- El residuo de ROUND_002_C (X_p que ven la ventana con diagonal pagada por la forma arquimediana).
- Usos de la relación de grado dos que no pasen por un cuadrado hermítico de pesos (por ejemplo, la
  relación entrando en ρ y no en V). No examinados aquí.
Nada de lo anterior es un NO-GO de la clase «Riccati»: los Lemas 1–2 excluyen sólo el uso de la
relación de convolución dentro de un cuadrado hermítico invariante por traslación.

## Resultado

Sin mecanismo nuevo; repetición de E70_10–12, R166_502 §5 y CA_G_001 §2. Dos lemas PROVED de
delimitación. No lista para construcción.

## Qué se probó

Lema 1 (la parte cuadrática en los pesos de un cuadrado invariante por traslación sólo tiene
frecuencias log(m/n); la convolución x∗x no aparece) — reformulación de R166_502 §5.2. Lema 2 (la
reflexión J convierte autocorrelación en convolución; en F par coinciden, en F impar difieren en un
signo). Identidad [M_t, S_a] = a S_a (el grado logarítmico δ de Riccati es ad M_t).

## Qué falló y por qué

La factorización pedida es la de la fase 70: su identidad de Riccati está en el álgebra de convolución
(productos), el cuadrado hermítico en el de razones (Lema 1), y el superpotencial que la haría exacta
es el del minimizador (CA_G_001 §2). El objeto cuadrático a·log − a∗a no cambia nada de eso: su no
homogeneidad en c es una relación entre pesos, que la forma afín no ve y que se deduce de los átomos
lineales. No se pudo escribir ℋ_T, V_T, ρ_T ni un paso de signo.

## Siguiente paso concreto

Si se quiere seguir en esta zona, la única operación con contenido distinto es la del Lema 2: escribir
explícitamente, para F ∈ P_T descompuesto en partes par e impar, la forma
Σ_{m,n<N} Λ(m)Λ(n)(mn)^{−1/2}[(F∗F)(log mn) − c_F(log mn)] y decidir si la relación
Λ·log + Λ∗Λ = μ∗log² la reescribe en términos que la forma arquimediana pueda pagar en el sector impar;
antes, cotejarlo contra R170_870 (paridad) y E70_10 opción 1. Sin ese objeto escrito no se relanza.
