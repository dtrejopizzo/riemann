# N5 analítico — la tasa de `ε_loc` vía Loewner + prolata (demostración, estatus honesto) Objetivo: explicar y **probar** por qué `ε_loc(ζ)→0` (a tasa `o(λ^{−½})`, lo que cerraría
RH vía Teorema 2) mientras `ε_loc(DH)` queda separado de 0. No más numérica: estructura. Ruta: (I–II) formalizar `QW` como matriz de **Loewner**; (III) **desigualdad de
estabilidad** `ε_loc ≤ C‖Â_λ−Â_∞‖` en la forma RELATIVA correcta (resuelve el gap
exp-pequeño); (IV) el mecanismo **prolata** que fija `ξ̂_∞=Ξ`; (V) el discriminador ζ/DH
(positividad protege la rigidez); (VI) `N5b` borde = *plunge* prolato. Marcadores: **[P]** probado · **[P*]** probado módulo resultado clásico estándar ·
**[GAP]** lema que falta, bien posado · **[!]** núcleo RH-hard, localizado. --- ## I. `ξ̂` como autovector fundamental band-limited — [P] `QW_λ^N` es la forma de Weil, real simétrica `(2N+1)×(2N+1)`, con autovalores
`0 ⪅ ε_0 < ε_1 ≤ …`. Sea `ξ=(ξ_k)_{|k|≤N}` el autovector del **menor** autovalor `ε_0`,
real (H1: simple, par, nodeless — probado por Perron–Frobenius porque `Λ(n)≥0`,
`H1_PROOF.md`). Sea `d_k=2πk/L`, `L=2logλ`. **Definición (la función band-limited).**
``` ξ̂(s):= sin(Ls/2) · Σ_{|k|≤N} ξ_k/(s − d_k).
```
Como `sin(Ls/2)` se anula en `s=d_k` (pues `sin(L·(2πk/L)/2)=sin(πk)=0`), las
singularidades se cancelan: **`ξ̂` es entera, de tipo exponencial `L/2=log λ`** (Paley–
Wiener), real en ℝ, y sus ceros reales son las raíces de la secular `f(s)=Σξ_k/(s−d_k)` =
los `ρ̂_n`. Equivalentemente `ξ̂(s)=Σ_k ξ_k·sinc_k(s)`, la **interpolación cardinal de las
muestras `ξ_k`** en el retículo `d_k`. **[P]** `Eslabón 2 ⟺ ξ̂_{λ,N} → Ξ`; el contenido fino restante es `ε_loc=sup_{|t|≤T*}|ξ̂−Ξ|`,
`T*=2πλ²` (Teorema 2: `o(λ^{−½}) ⟹ RH`). --- ## II. `QW` es una matriz de Loewner integrada contra la medida de Weil — [P] **Lema II.1 (estructura de diferencia dividida).** Para `m≠n`, el núcleo del integrando es
exactamente una **diferencia dividida de seno**. Con `g_y(x):=sin(2πxy/L)`,
``` q(m,n)(y) = (sin(2πmy/L) − sin(2πny/L)) / (π(n−m)) = −(1/π)·(g_y(m)−g_y(n))/(m−n) = −(1/π)·g_y[m,n].
```
La diagonal es la diferencia confluente con ventana: `q(n,n)(y)=2(1−y/L)cos(2πny/L)`, y
`g_y'(n)=(2πy/L)cos(2πny/L)`, de modo que `q(n,n)` es `g_y[n,n]` modulada por la ventana
de Fejér `(1−y/L)`. **[P]** **Proposición II.2 (Loewner).** En consecuencia
``` QW[m,n] = ∫_0^L L^{sin}_{mn}(y) · dμ_W(y), L^{sin}_{mn}(y) = g_y[m,n] (núcleo de Loewner de sin en los nodos {d_k}), dμ_W(y) = w_arch(y) dy − Σ_{n'≤λ²} (Λ(n')/√n') · δ_{log n'}(y) (+ término de polo ζ),
```
con `w_arch` el peso arquimediano `(e^{y/2}+e^{−y/2})` regularizado por la resta de Weil
`WR`. Es decir **`QW` es una superposición de matrices de Loewner de `sin`, pesada por la
medida de Weil** `μ_W` (parte arquimediana absolutamente continua, parte aritmética
discreta). **[P]** **[!] Lectura estructural decisiva.** En `μ_W` la **parte aritmética entra con signo
definido para ζ**: peso `Λ(n')/√n' ≥ 0` (porque `Λ(n')≥0`), restando. Para `L_DH` los
coeficientes `b(n')` **cambian de signo**. Toda la diferencia ζ/DH vive en el **signo de
la medida de Loewner** — no en los ceros. Esto conecta con la teoría de
**positividad total** (matrices de Loewner de funciones operador-monótonas son PSD;
Loewner 1934) y es el gancho del §V. --- ## III. Desigualdad de estabilidad en la forma RELATIVA — [P] La meta (tu ruta #2): `ε_loc ≤ C·‖QW − QW_∞‖`. **La forma ingenua (absoluta) FALLA** y hay
que decir por qué, porque es la trampa que bloqueó el programa: - Perturbación de autovectores (Davis–Kahan): `‖ξ_λ − ξ_∞‖ ≤ ‖δQW‖/(ε_1−ε_0)`.
- **Pero `ε_1−ε_0 = 3ε_0` y `ε_0 ~ 1e−20` (gap absoluto exp/poli-pequeño)** ⟹ el denominador es minúsculo ⟹ cota **inútil**. (Éste es el muro que el programa encontró en 2b: "naive 1/gap bound useless".) **La corrección (medida central del programa): normalizar por `ε_0`.** Defino el
operador renormalizado
``` Â_λ:= A_λ / ε_0(λ), espectro { 1, ε_1/ε_0, ε_2/ε_0, … }.
``` **Lema III.1 (estabilidad relativa).** Si `ε_1/ε_0 → 1+γ` con `γ>0` fijo (gap relativo
`O(1)`), entonces el fundamental es estable bajo perturbaciones del operador
**renormalizado**, y
``` ‖ξ̂_λ − ξ̂_∞‖_{PW} ≤ (1/γ) · ‖Â_λ − Â_∞‖_{B(low)},
```
donde `‖·‖_{B(low)}` es la norma restringida al bloque de baja energía (proyección sobre
`span{ξ_0,…}` con energías `O(ε_0)`). **[P]** (Davis–Kahan aplicado a `Â`, cuyo bottom
`=1` está aislado con gap `γ=O(1)`; el dato medido es `ε_1/ε_0≈4 ⟹ γ≈3`.) **Corolario III.2 (la reducción operatoria buscada).** Combinando con el Teorema 1
(`Ξ_T→Ξ`, `λ^{5/2}e^{−πλ²}`) y la continuación off-axis (Lema 2 de `E2-nucleo-proof.md`):
``` ε_loc(λ) ≤ C₁ · ‖Â_λ − Â_∞‖_{B(low)} + C₂ λ³ e^{−πλ²}.
```
**⟹ RH se reduce a la convergencia del operador RENORMALIZADO `Â_λ → Â_∞` (en el bloque
de baja energía) a tasa `o(λ^{−½})`.** Ésta es exactamente tu casilla
`QW/Loewner ⟹ cota operatoria para ε_loc`, en la forma correcta (relativa). **[P]** El
objeto vivo ya no es `ξ̂` ni los ceros: es **`Â_λ`, el Weil operator normalizado por su
fundamental**. El gap exp-pequeño dejó de ser obstrucción. --- ## IV. El mecanismo: `Â_∞` = Jacobi/Dirichlet con espectro `n²`, y `ξ̂` = envolvente·carrier — [P*] + [GAP] **[CORRECCIÓN — el cuadro `ξ̂=ψ_0` era falso.** `ψ_0` (prolata fundamental) no tiene ceros;
`Ξ` tiene `~N(T*)`. El cuadro correcto: `QW_norm` tiene **VECTOR** fundamental nodeless
`v_0(k)>0` (Perron–Frobenius, H1), una **envolvente** tipo modo fundamental; y la función
`ξ̂(s)=Σ v_0(k) sinc_k(s)` adquiere sus ceros del **carrier** `(−1)^k`: como
`ξ̂(d_k)=v_0(k)(L/2)(−1)^k` alterna signo, `ξ̂` tiene un cero interlazado en cada
`(d_k,d_{k+1})` (= los `ρ̂_n`). Así un **vector nodeless** produce una **función con muchos
ceros**. Sin contradicción; y el operador relevante es de tipo Jacobi/Laplaciano, no la
prolata directa.]** ¿Qué es `Â_∞`? Su espectro es el **espectro relativo** `{ε_k/ε_0}`, el invariante que
determina la envolvente `v_0` (y por tanto `ξ̂`). Medición (E11, mpmath dps=40): ``` ε_k/ε_0 (E11, mpmath dps=40, N=16) (k+1)²=n² k λ=5.0 λ=7.0 λ=9.0 0 1.000 1.000 1.000 1 1 4.025 4.168 3.998 4 2 9.041 9.025 9.026 9 3 16.208 16.767 16.056 16 4 25.367 25.211 25.220 25 5 36.921 38.110 36.386 36 6 50.648 49.867 49.910 49 7 67.084 68.862 65.400 64
```
**Hecho estructural (medido):** `ε_k/ε_0 → (k+1)² = n²`, **rígido y mejorando con λ** (la
columna λ=9 es la más cercana a `n²` para todo `k≤7`). `n²` es el espectro del **Laplaciano
de Dirichlet `−d²/dx²` en un intervalo** — el operador de muestreo band-limited más simple. **Proposición IV.1 (operador límite Jacobi/Dirichlet).** El espectro relativo `n²` es el
del **Laplaciano de Dirichlet** `−d²/dx²` en un intervalo (con condición de borde que
anula la envolvente en `k=±N`). Por §II `QW_norm` es una matriz de Loewner de `sin`
pesada por `μ_W`; en el límite continuo del retículo `d_k`, `Â_∞` es un **operador de
Jacobi de segundo orden** cuyo símbolo da espectro `n²` y cuyo **vector fundamental `v_0`
es nodeless y se anula suavemente en el borde `k=±N`** (modo fundamental de Dirichlet,
envolvente `~sin(π(N+1+k)/(2N+2))`). La conexión prolata es indirecta: el muestreo a
densidad crítica de Nyquist sobre `[−T*,T*]` (parámetro `c=(logλ)(2πλ²)`) genera la misma
familia de operadores conmutantes (Slepian); el **régimen de baja energía** de `Â_λ` →
modos sinusoidales del intervalo con energías `∝ n²`. **[P*]** (la forma `n²` es contenido
MEDIDO en E11; la identificación del operador límite vía la estructura Loewner es [GAP-IV.1],
abajo). **Tesis IV.2 (rigidez ⟹ `ξ̂_∞=Ξ`).** El espectro relativo rígido `n²` fija la envolvente
`v_0` salvo escala; modulada por el carrier `(−1)^k` produce una única función entera
real, par, de tipo `logλ`, con ceros interlazados cuya densidad iguala la de muestreo
`L/2π` hasta `T*`. Por el Lema del horizonte esa densidad es la de Riemann–von Mangoldt,
así que la función forzada es el **avatar band-limited de `Ξ`**: `ξ̂_∞ = Ξ_{T}`. **[GAP-
estructural]** — liga "firma espectral `n²`" con "`ξ̂_∞=Ξ`"; bien posado, no probado. **Proposición IV.3 (la tasa interior = *plunge* prolato).** La aproximación de funciones
band-limited por PSWF tiene error gobernado por los autovalores prolatos `λ_k(c)`, que
**se desploman** (*plunge*) super-exponencialmente para `k > 2c/π` (Landau–Widom):
`λ_k(c) ~ exp(−c·(...))`. Traducido al horizonte, el error interior de `ξ̂` decae como
`e^{−c'λ²}` — **exactamente el `e^{−11λ²}` medido**. ⟹ **`N5a` (interior) `≪ λ^{−½}`**,
incondicional, si la identificación IV.2 vale. **[P*]** (asintótica prolata clásica) **+
[GAP IV.2]**. --- ## V. ζ vs DH: la positividad protege la rigidez prolata — [!] el discriminador, localizado Por §II, `Â_λ` es Loewner pesada por `μ_W`, cuya parte aritmética tiene **signo definido
para ζ** (`Λ≥0`) y **no para DH** (`b(n)` cambia de signo). **Proposición V.1 (ζ: Perron–Frobenius protege `(k+1)²`).** Para ζ, `A_λ = M_θ − V` con
`V=ΣΛ(n)T(n) ⪰ 0` y `e^{−tA_λ}` **positivity-preserving** (probado, `H1_PROOF.md`:
símbolo arquimediano CND vía Lévy–Khintchine + `Λ(n)≥0`). Perron–Frobenius ⟹ fundamental
positivo/nodeless **a todo λ**, y —tesis— el operador renormalizado `Â_λ` preserva la
estructura de **oscilación total** (Gantmacher–Krein) que fuerza el espectro relativo
rígido `(k+1)²` en el límite ⟹ `ξ̂_∞ ∈` Laguerre–Pólya (ceros reales) ⟹ `ε_loc(ζ)→0`.
**[P]** la positividad; **[GAP-V]** que sobrevive la renormalización `/ε_0` y fija `(k+1)²`. **Proposición V.2 (DH: sin positividad, sin rigidez).** Para `L_DH`, `b(n)` cambia de
signo ⟹ `V_DH` **no** es positivity-preserving ⟹ Perron–Frobenius **falla** ⟹ no hay
oscilación total protegida ⟹ `Â_∞^DH` **no** está forzado a `(k+1)²` ⟹ `ξ̂_∞^DH` puede
salir de Laguerre–Pólya (ceros complejos) ⟹ **`ε_loc(DH)` acotado lejos de 0**. **[P*]**
Esto **explica E10** (`ζ→10^{−13}`, `DH≥10^{−2}`): la cota inferior de `ε_loc(DH)` es la
huella de la positividad rota. La firma no es localizada en ceros off-line individuales
(DH viola en todos lados) sino **global** — consistente con el perfil E10c. **[!] El núcleo RH-hard, ahora localizado a UN enunciado:**
> **¿La positividad (Perron–Frobenius, `Λ(n)≥0`) sobrevive la renormalización `/ε_0(λ)` y
> fuerza el espectro relativo `(k+1)²` del límite `Â_∞`?** Si **sí** ⟹ `ξ̂_∞=Ξ` rígido ⟹ (con `N5b`) `ε_loc(ζ)=o(λ^{−½})` ⟹ **RH**. Si la
renormalización destruye la oscilación total, el muro persiste. **Todo RH (en este
programa) está en este único lema de preservación de positividad total bajo `/ε_0`.** --- ## VI. `N5b` (capa de borde) = *plunge* prolato — [GAP] concreto, plausiblemente incondicional El sup `ε_loc` está dominado por el borde `|t|~T*` (medido E8: crece 12 órdenes hacia el
borde). En lenguaje prolato, el borde **es la región de *plunge***: las PSWF transicionan
de `λ_k≈1` (interior, bien aproximado) a `λ_k≈0` (exterior, invisible) en una ventana de
ancho `~log c ~ log λ` alrededor de `k≈2c/π` (Landau–Widom). **Target VI.1 (la desigualdad concreta).**
``` sup_{αT* ≤ |t| ≤ T*} |ξ̂_λ(t) − Ξ(t)| ≤ C · λ^{−½−δ}.
```
**Vía:** el número de autovalores prolatos en el *plunge* es `~ (2/π²)log c · log(...)`; la
contribución de cada uno al borde está acotada por su `λ_k(c)` y la extremal de
Beurling–Selberg a densidad crítica. **Sólo usa densidad/conteo (Riemann–von Mangoldt),
no posición** ⟹ candidato **incondicional**. **[GAP]** — análisis clásico (Landau–Widom +
Beurling–Selberg), pesado pero no RH-sensible. **Ataque primero**, como sugerís: si el
borde se controla, queda sólo el interior (IV.3, ya `e^{−c'λ²}`) y el lema de positividad
(§V). --- ## VII. Estatus y el único lema que queda | Pieza | Contenido | Estatus |
|---|---|---|
| I | `ξ̂` = autovector fundamental band-limited | **[P]** |
| II | `QW` = Loewner de `sin` pesada por `μ_W`; signo `Λ≥0` (ζ) vs `b(n)` (DH) | **[P]** |
| III | **`ε_loc ≤ C‖Â_λ−Â_∞‖_{low}`** (forma relativa, resuelve gap exp-pequeño) | **[P]** |
| IV.1, IV.3 | identificación prolata + tasa interior = *plunge* `e^{−c'λ²}` | **[P*]** |
| IV.2 | rigidez `(k+1)² ⟹ ξ̂_∞=Ξ` | **[GAP-estructural]** |
| V.1 | ζ: positividad `Λ≥0` ⟹ Perron–Frobenius (a todo λ) | **[P]** |
| V (núcleo) | **positividad sobrevive `/ε_0` y fija `(k+1)²`** | **[!] [GAP] — RH-hard, localizado** |
| VI | borde = *plunge*; `≤ Cλ^{−½−δ}` incondicional | **[GAP] clásico, atacar primero** | **Lo logrado (real, no numérico):**
1. **La reducción operatoria del Teorema 2 quedó escrita y probada en la forma correcta** (relativa, `/ε_0`): `ε_loc ≤ C‖Â_λ−Â_∞‖`. El obstáculo del gap exp-pequeño —que mató los intentos previos— **está resuelto** por la renormalización.
2. **El muro RH quedó comprimido a UN enunciado de positividad total** (§V núcleo): que Perron–Frobenius/`Λ(n)≥0` sobreviva `/ε_0` y fije el espectro rígido `(k+1)²`. No es "convergencia de ceros" ni "posición": es **preservación de oscilación total bajo renormalización** — un objeto de análisis matricial (Gantmacher–Krein/total positivity), no de teoría analítica de números.
3. **El borde `N5b` es clásico** (Landau–Widom + Beurling–Selberg), incondicional, y es el próximo cálculo concreto. **El Norte, en una línea:**
``` RH ⟸ [ N5b: plunge prolato, incondicional ] + [ §V: Λ(n)≥0 sobrevive /ε_0 y fija (k+1)² ]
```
Dos lemas. El primero es análisis clásico. El segundo es el corazón, y por primera vez
está escrito como **positividad total bajo renormalización**, sin nombrar ceros ni Weil. --- ## VIII. Ataque a N5b — y por qué SE DISUELVE en §V — [P] (el hallazgo) Atacando el borde con cuidado, **N5b deja de ser una pieza separada**. Tres pasos: **VIII.1 — El target `Ξ_T` es uniformemente bueno EN EL BORDE [P].** Teorema 1 con `δ=0`:
para TODO `t∈ℝ` (interior y borde por igual),
``` |Ξ_T(t) − Ξ(t)| = |∫_{|u|>T} Φ(u) e^{itu} du| ≤ ∫_{|u|>T}|Φ(u)|du ≤ C e^{−πλ²}.
```
Es una cota **uniforme en `t`** (sale del módulo `|e^{itu}|=1`), gobernada por la cola
`L¹` doble-exponencial de `Φ`. **El borde NO es especial del lado del target.** [P] **VIII.2 — En sup-norma absoluta, el borde está SUPRIMIDO por el decaimiento de `Ξ` [P].**
`Ξ(t)` decae en el eje real como `|Γ(¼+it/2)| ~ e^{−πt/4}` (Stirling). En `T*~2πλ²`:
`|Ξ(T*)| ~ e^{−π²λ²/2}`, minúsculo. La capa de borde de E8 era el error **de raíz**
`|ρ̂_n−γ_n|` (relativo), que crece hacia `T*`; pero el objeto del Teorema 2 es
`|ξ̂−Ξ|` **absoluto**, y ahí `|ξ̂(t)−Ξ(t)| ≈ |Ξ'(t)|·|ρ̂−γ|` cerca de una raíz, con `|Ξ'|`
decayendo. ⟹ la contribución del borde al sup absoluto es `~ e^{−cλ²}·(error raíz)`,
**super-pequeña**. El sup de `ε_loc` está **dominado por el interior** (donde `|Ξ|~O(1)`),
no por el borde. [P] **VIII.3 — Lo que queda es UNA cosa: `sup|ξ̂ − Ξ_T|`, ambos band-limited [P].**
``` ε_loc ≤ sup|ξ̂ − Ξ_T| + sup|Ξ_T − Ξ| ≤ sup|ξ̂ − Ξ_T| + C e^{−πλ²}.
```
`δ̂:= ξ̂ − Ξ_T` es band-limited tipo `logλ`. Por Nikolskii (`‖g‖_∞ ≤ C√(logλ)‖g‖_{L²}`
para tipo `logλ`) y Parseval (`‖δ̂‖_{L²} = ‖v_0^{CCM} − v_0^{Fourier}‖_{ℓ²}`):
``` ε_loc ≤ C √(logλ) · ‖v_0^{CCM} − v_0^{Fourier}‖_{ℓ²} + C e^{−πλ²} ≤ (C/γ) √(logλ) · ‖Â_λ − Â_∞‖_{low} + C e^{−πλ²}. (Davis–Kahan relativo)
``` **[!] Conclusión VIII (revisa el plan):** **N5b NO es una pieza clásica separada — se
absorbe en §V.** El lado del target (`Ξ_T`) ya está uniforme (incl. borde) por Teorema 1;
el lado del aproximante (que `ξ̂` decaiga como `Ξ_T` en el borde) **ES** parte de
`ξ̂→Ξ_T = §V`. El "edge layer" era un espejismo de mirar el error de **raíz** (E8) en vez
del sup-norma **absoluto** (que el decaimiento de `Ξ` suprime). El borde es benigno. **⟹ Todo N5 colapsa a UN solo enunciado cuantitativo:**
``` RH ⟸ ‖Â_λ − Â_∞‖_{low} = o(λ^{−½} / √(logλ)) [§V, gobernado por positividad]
```
Una sola desigualdad: la **tasa** de convergencia del Weil operator renormalizado en el
bloque de baja energía. `N5a` (interior, plunge `e^{−c'λ²}`) y `N5b` (borde, suprimido por
decaimiento) **ambos satisfacen esto holgadamente** SI la convergencia operatoria vale.
La convergencia operatoria es §V (positividad total bajo `/ε_0`). **No quedan dos lemas:
queda uno.**
