# Ronda 16, memo C: positividad por reflexión, desigualdades de correlación y dominación gaussiana como fuente del signo

Resumen. Se pasaron por la puerta tres fuentes de signo de la mecánica estadística que no son «suma de
cuadrados con pesos positivos»: (a) positividad por reflexión de Osterwalder–Schrader (OS) con
reconstrucción por matriz de transferencia; (b) GKS, Griffiths, Ginibre, FKG, cuatro funciones y Lee–Yang
sobre el retículo de divisores; (c) dominación gaussiana y cotas infrarrojas. Las tres son **repetición**,
leídas en primaria. La descomposición par/impar `a_T = D ± R` que propone la asignación es, literalmente, el
Lema 1 de `phase-193-creation-campaign/CA_A_007_SEED_TRIAGE_HOMOTOPY_TRIPLES_RP.md` §3. La no negatividad
de `R` (la mitad de Hankel) es falsa para todo peine con un átomo (Teorema 2, mismo archivo, PROVED). Según la
regla del filtro, el memo no construye. Tampoco encontré una idea vecina que pueda defender (§4).

Lectura en primaria: `CA_A_007_SEED_TRIAGE_HOMOTOPY_TRIPLES_RP.md` §§3–5 y `CA_A_007_REVIEW.md`
(encabezado y fila del Lema 1); `phase-200-sign-object/K1_OSG_001.md` §1b y la entrada propuesta para el índice;
`phase-6-osterwalder-schrader-reflection/README.md` y `M-OS-2-S2-local-REFUTATION.md` §2;
`CA_J_000_SEEDS.md`, filas J6 y J7; índice `README.md`, frente J de la fase 193;
`RULES_AVOID.md` M3, M5, W4 e Y; `ROUND_009_G3.md`, fila 17; grid, entrada 52;
`ANNEX_PHASE_193_LABELS.md`, J6 y J7. Grep en `03-research` y `05-meta-and-planning` de «reflection positiv»,
«Osterwalder», «chessboard», «GKS», «FKG», «Lee–Yang», «four functions», «infrared», «Gaussian domination»,
«dominación gaussiana» y «Fröhlich». Los aciertos pertinentes son los anteriores; los demás usan esas palabras
de paso. No releí `CA_J_001` ni `CA_J_002` completos: su contenido se toma del índice y del grid
(lectura indirecta).

## 0. Filtro de cuatro puntos

1. **Antecedente más cercano.**
   - (a) `CA_A_007` §3. Lema 1: para `F = f + Θf` con `f` en `(0,T)`, `𝔞(F) = 2𝔞(f) + 2H_K(f)`, con
     `H_K(f) = ∬ f(t)f(s)K(t+s)` y `K` el núcleo de ventana (parte arquimediana menos el peine
     `Σ (v_n/2)δ_{±log n}`): «RP is the Hankel half of the Toeplitz form». Teorema 2: `H_K` no es `≥ 0` en
     `(0,T)` si `T > ½ log n_0` para algún átomo `n_0`. La reflexión en el borde `x = T` es `K1_OSG_001`
     (NO-GO; es el Teorema 2 conjugado por una traslación). La reflexión multiplicativa `n ↦ 1/n` es la
     simetrización por la ecuación funcional (`CA_A_007` §3, último párrafo; L2_026, NG-D4). La positividad
     por lugar es la fase 6, S2.1 (`G_p` indefinida).
   - (b) Frente J de la fase 193 (`CA_J_002`, Teorema 1.3). El ciclo aditivo `m → m+1 → … → 2m`, cerrado
     por la arista multiplicativa `(m, 2m)`, está frustrado, así que ningún gauge `±1` vuelve ferromagnético
     a `𝔸_M`. Eso deja sin entrada a GKS, Ginibre, GHS, Lebowitz y FK. En FKG, la clase de igualdad sobre el
     retículo de divisores son los vectores de producto de Euler (`CA_E_001`), así que FKG es ciega. Lee–Yang
     y Rayleigh fuerte están en M3/M5 y en `INV_M_001`.
   - (c) `CA_J_000`, fila J7: «DISCARD: requires RP ⇒ dies with J6».
2. **Objeto nuevo propuesto por la asignación.** Hay tres afirmaciones. Primero, el espectro de
   «transferencia» de la parte arquimediana. Segundo, que el peine entre como una interacción de la forma
   `−Σ(θA_i)A_i` que preserve RP. Tercero, una cota infrarroja «interacción ≤ parte libre», uniforme en `T`.
3. **¿Evita la dificultad del antecedente?** No, en ninguno de los tres casos.
   - La primera afirmación es correcta pero no es nueva (§1). Además es ciega: sólo usa la parte arquimediana,
     que es la misma en los tres controles.
   - La segunda choca con el Teorema 2 (§2).
   - La tercera presupone RP, o bien es el enunciado mismo (§3).
4. **Enlace global.** El único enlace que se escribe es `𝔞_T(f) ≥ |H_K(f)|` sobre los dos sectores de
   paridad. Es la positividad de `a_T` restringida a pares e impares, es decir, la forma misma (J3). No hay
   una desigualdad nueva.

Por la regla del filtro, la construcción se detiene aquí.

## 1. El núcleo arquimediano es completamente monótono (correcto, conocido, ciego)

**Observación 1 (PROVED; elemental).** Para `u > 0`, `1/(2 sinh(u/2)) = Σ_{k≥0} e^{−(k+½)u}` y
`1/(2 cosh(u/2)) = Σ_{k≥0} (−1)^k e^{−(k+½)u}`. Sumando,
`K(u) = 2 Σ_{j≥0} e^{−(2j+½)u}`: es la transformada de Laplace de la medida positiva `2Σ_j δ_{2j+½}`. Por
lo tanto `H_{K_arch}(f) = 2 Σ_j |∫ f(t) e^{−(2j+½)t} dt|² ≥ 0`. Esto es RP de la parte arquimediana,
con «energías» `2j+½`.

No es nuevo. `K1_OSG_001` construye exactamente el «CM Hankel square of the poles of Γ_ℝ». Además, por el
Lema K (`RULES_AVOID` W4), la positividad que sale de una medida positiva vale para todo peso: es ciega en
`c = 2`, al borrar una potencia de primo y para Beurling. Una prueba de RP que sólo use esto no ve el peine.

## 2. El peine como interacción que preserva RP: falsificado por el Teorema 2

En el sector par la forma es `2𝔞_T(f) + 2H_K(f)` y en el impar `2𝔞_T(f) − 2H_K(f)` (Lema 1 de `CA_A_007`
aplicado a `f ± Θf`; PROVED allí). Con `D = 2𝔞_T(f)` y `R = 2H_K(f)`, el esquema OS pedía `R ≥ 0`. La
contribución del peine a `R` es `−Σ_n (v_n/2) ∫ f(t) f(log n − t) dt`: una forma de Hankel de núcleo
`−Σ (v_n/2) δ(t + s − log n)`. Por el criterio de Widom–Bernstein, un núcleo de Hankel `h(t+s)` es `≥ 0` sobre
una semirrecta si y sólo si `h` es la transformada de Laplace de una medida positiva (CITED). Un peine de
deltas con signo negativo no lo es. El Teorema 2 de `CA_A_007` da la prueba directa, también en ventana
finita: `f_ε` concentrada en `½ log n_0` da `H_K(f_ε) → −v_{n_0}/2`, porque la parte continua contribuye
`O(ε)`.

Sobre la forma `−Σ(θA_i)A_i`: en OS, una interacción preserva RP cuando entra en el peso de Boltzmann como
`exp(+Σ(θA_i)A_i)`. Al nivel cuadrático eso es sumar a `R` un término de la forma `+Σ|⟨A_i, f⟩|²`. En `a_T`,
el peine entra con el signo opuesto (`−v_n c_F`), justamente el que destruye RP. Ninguna elección de
reflexión lo arregla:
- la traslación del centro es el caso de `K1_OSG_001`;
- la inversión `n ↦ 1/n` es la ecuación funcional (NG-D4);
- las reflexiones por primo `θ_p` son el tablero de `CA_J_001`, que fuerza `𝖡` constante con dos primos.

**Controles.** El Teorema 2 vale para todo peine con un átomo, incluidos `2Λ`, el peine con un borrado y
Beurling. RP es falsa en los cuatro casos. No falla en «el paso que se rompe en `c = 2`»; falla en todas
partes. Por eso no es un mecanismo de signo (Lema T).

**Dominancia en los dos sectores.** La exigencia `𝔞_T(f) ≥ |H_K(f)|` (Toeplitz domina a Hankel) es una
cota de tipo Cauchy–Schwarz de OS. Sin RP no hay Cauchy–Schwarz para `⟨θ·,·⟩`. Como enunciado, es
`a_T ≥ 0` en cada sector de paridad, donde `P_T` impone una sola condición por sector (`∫F cosh(t/2) = 0` en el
par, `∫F sinh(t/2) = 0` en el impar). Es la reducción por paridad ya conocida (thm:parityschur, `CA_A_007`
§2), luego J3. La matriz Toeplitz−Hankel de la fase 205 es esa misma forma en coordenadas, no una fuente de
signo. Ese archivo no se releyó: lectura indirecta, por la memoria del proyecto.

## 3. Dominación gaussiana y cotas infrarrojas

La dominación gaussiana de Fröhlich–Simon–Spencer (CITED) deduce `Z(h) ≤ Z(0)` de RP mediante el tablero,
y de ahí una cota infrarroja. Sin RP del objeto completo no hay entrada: así se descartó J7. El formato de
llegada, «parte de primos ≤ Arch» uniforme en `T`, es `a_T ≥ 0` para todo `T`. Escrito sin RP, es el
enunciado mismo (J3), no una herramienta.

## 4. Idea vecina

Busqué una variante que cambie la clase de métodos y no sólo la reflexión. No la encontré. Las
posibilidades revisadas fueron:
- RP con un núcleo de Hankel `h` que dependa de `Λ` de forma no lineal. Para tener RP, `h` debería ser de
  Laplace positivo, y entonces sería ciego por el Lema K.
- Positividad «condicional»: RP sólo sobre el subespacio ortogonal a los modos `δ_{log n}`. Es el borde o
  el portador con condiciones adicionales, el caso de `K1_OSG_001` (i), donde el hueco sólo protege
  productos.
- Una reflexión no lineal en `F`. No conozco una teoría de reconstrucción OS para ella, y no la invento sin
  mecanismo.

En lugar de proponer algo sin mecanismo, lo registro como ausencia. Siguen sin excluir, según `RULES_AVOID`
X e Y: la positividad de Hadamard que acople primos mediante `m ≈ kn` y el potencial `V(x,F)` convexo sólo
para el peso verdadero. Este memo no los ataca.

## 5. Estado

- (a) OS/RP con reconstrucción por transferencia: **repetición** (`CA_A_007` §3, `K1_OSG_001`, fase 6, `CA_J_001`).
  La no negatividad de la mitad de Hankel con el peine es **NO-GO** (PROVED allí, para todo peine con un átomo).
- (b) GKS, Griffiths, Ginibre, FKG, cuatro funciones y Lee–Yang: **repetición** (frente J de la fase 193,
  `CA_J_002`, `CA_E_001`, M3).
- (c) Dominación gaussiana y cotas infrarrojas: **repetición** (J7). Sin RP, el formato de llegada es J3.
- Observación 1 (núcleo `K` completamente monótono, exponentes `2j+½`): PROVED, pero ya está en `K1_OSG_001`
  y es ciega.
- Nada nuevo para anotar en el índice como ruta cerrada.
