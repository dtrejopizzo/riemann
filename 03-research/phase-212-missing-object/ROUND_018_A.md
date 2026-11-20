# Ronda 18, memo A: representación de estado fundamental con `φ` de signo variable para el reparto local en `T ∈ (0.60, 0.69)`

Notación de `common7`: `a_T = Arch − Σ_n v_n c_F(log n)`, `Arch(F) = ∫_I W F² + ¼∬_{I×I} K(|t−s|)(F(t)−F(s))²`,
`I = [−T, T]`, `P_T = {∫F e^{±t/2} = 0}`, `e_±(t) = e^{±t/2}`. Reparto DIR: `q_p = ∫W_pF² + ¼∬θ_pK(ΔF)² − Π_p`.

**Objetivo de esta ronda, declarado como LOCAL.** El encargo relaja el punto (4) del filtro: se busca la primera
prueba por mecanismo (no por certificado matricial) de `a_T ⪰ 0` sobre `P_T` en un `T` por encima del umbral
arquimediano. Nada de lo que sigue tiene, ni se afirma que tenga, consecuencia para la positividad en todo `T`.

**Veredicto.** No se obtuvo reparto explícito ni prueba. El mecanismo sugerido (estado fundamental de signo
variable que vuelve positivo el cuadrado del contacto) tiene el signo al revés (§2), y toda representación de
estado fundamental con todos sus términos manifiestamente `≥ 0` es imposible en cualquier `T ∈ [0.2, 0.75]` por
una cuenta a mano (§3). La variante que usa `P_T` mediante términos de Lagrange falla numéricamente por mucho (§4).

## 0. Filtro

**(1) Antecedente más cercano.** `ROUND_007_A.md` §1 Lema 1.1 (identidad de estado fundamental por contacto,
`φ > 0`) y §2 Teorema 2.1 (clase 𝒢: contactos acotados por potenciales `V_p ≥ 0`; NO-GO relativo a P47 cor:Tarch,
`RULES_AVOID` Q1). La propia memo deja abierto (§2, «Lo que 𝒢 no cubre») el caso de `V_p` de signo variable.
Además `phase-211-sign-sandbox/ROUND_005_D.md` Teor. 2.1 (estado fundamental global `h_T`), `INV_N_001` §1 (`φ ≡ 1`),
`ROUND_017_A.md` / `RULES_AVOID` AA (muro del reparto por primo, `T_DIR ≈ 0.697`), `ROUND_006` §§7–10.
Grep de «Allegretto», «Piepenbrink», «Doob», «Perron», «estocástic» en `03-research` y el índice: sólo usos
laterales (p. ej. `R184_003` l. 102, paridad del modo fundamental); ninguna representación de estado
fundamental de signo variable para `a_T`.

**(2) Lo nuevo.** Que `φ` cambie de signo, de modo que el potencial `V_p` inducido tenga signo variable: es el
hueco declarado abierto en `ROUND_007_A` §2.

**(3) Por qué esquivaría el antecedente.** El Teorema 2.1 de `ROUND_007_A` usa sólo `ΣV_p ≥ 0`; con `φ` de signo
variable `V_p` no es `≥ 0` y el argumento no se aplica.

**(4) Conexión.** Relajado por el encargo: objetivo local en un solo `T`.

El resultado del cotejo es que (3) no se sostiene (§§2–3): el cambio de signo de `φ` no esquiva el obstáculo,
lo invierte.

## 1. Identidad de estado fundamental general (PROVED, elemental)

Sea `Q(F) = ∫U F² − ½∬M(t,s)F(t)F(s)` con `M` medida simétrica `≥ 0` fuera de la diagonal (para `q_p`:
`M = θ_pK + v_n(δ_{s=t−log n} + δ_{s=t+log n})` sobre los contactos de `p`, más la parte diagonal absorbida en `U`).
Sea `φ` real con `φ ≠ 0` c.t.p. y `f = F/φ`. Entonces, para toda `F ∈ L²(I)`,

    Q(F) = ∫ (Qφ/φ) F² + ¼∬ M(t,s) φ(t)φ(s) (f(t) − f(s))²,     Qφ := Uφ − ½Mφ.        (1.1)

*Prueba.* `−½∬Mφφ f(t)f(s) = ¼∬Mφφ(f(t)−f(s))² − ½∬Mφφ f(t)²` (simetría), y `½∬M(t,s)φ(t)φ(s)f(t)² =
∫F²·(½Mφ)/φ`. □

Con `φ > 0` y `M ≥ 0` es el criterio de Allegretto–Piepenbrink; el Lema 1.1 de `ROUND_007_A` es el caso de un solo
contacto.

## 2. Corrección de signo (PROVED por (1.1))

En (1.1) el coeficiente del cuadrado del contacto es `¼ v_n φ(t)φ(t − log n)`, **con el signo de `φφ`**. El
contacto es una tasa de salto *positiva* (`M ≥ 0`: favorece `F(t) = F(t − log n)`), no negativa. Si `φ` cambia de
signo entre las dos zonas extremas `L_p`, `R_p`, el cuadrado del contacto queda con signo **negativo**, al revés de
lo que suponía la línea sugerida. Lo mismo ocurre con todo par `(t, s)` del núcleo con `θ_p > 0` y
`φ(t)φ(s) < 0`. Si se descarta ese cuadrado, se obtiene `Π_p ≥ ∫V_pF²`, una cota *inferior* del contacto, que no
sirve para `q_p ⪰ 0`.

## 3. NO-GO a mano de toda representación manifiesta válida en `L²(I)` (PROVED)

**Lema 3.1.** Para `0.2 ≤ T ≤ 0.75`, `a_T(1) < 0`. En concreto

    a_T(1) ≤ ∫_I W ≤ 2T [ C_0 + 1 + log(2/T) + π/2 + T²/(72(1 − T²/12)) ],

y en `T = 0.65` el corchete es `≤ −1.67`, luego `a_T(1) ≤ −2.17`.

*Prueba.* El término de núcleo se anula en las constantes y `c_1(u) = 2T − u ≥ 0`, luego `a_T(1) ≤ ∫W`. Se tiene
`∫_I W = 2T·C_0 + ∫_0^{2T}(π − G(u))du` y `π − G(u) = −log tanh(u/4) + 2 arctan e^{−u/2}`. Se usan tres
desigualdades: `2 arctan e^{−u/2} ≤ π/2`; `tanh x ≥ x(1 − x²/3)` para `x ≥ 0`; y `−log(1 − y) ≤ y/(1 − y)`.
Con ellas `π − G(u) ≤ −log(u/4) + (u²/48)/(1 − u²/48) + π/2`. Al integrar:
`∫_0^{2T} −log(u/4) du = 2T(1 + log(2/T))` y `∫_0^{2T} u²/48 du ≤ (2T)³/144`, con denominador
`≥ 1 − T²/12`. Para la constante: `C_0 = ψ(¼) − log π = −γ − π/2 − 3 log 2 − log π = −5.3721…` (teorema de
Gauss del digamma, CITED, clásico). En `T = 0.65` los sumandos son `−5.3721 + 2.1240 + 1.5708 + 0.0061 = −1.6712`.
Para `T ∈ [0.2, 0.75]` el corchete es creciente en `T`, salvo por `log(2/T)`, que decrece. Por eso conviene
acotarlo en `T = 0.2`: `−5.3721 + 1 + 2.3026 + 1.5708 + 0.0006 = −0.498 < 0`. □

**Corolario 3.2.** Para `T ∈ [0.2, 0.75]` no existe ninguna identidad `a_T = Σ_p q_p` en la que cada `q_p` esté
escrito como en (1.1), con cualquier `φ_p` (de cualquier signo, `≠ 0` c.t.p.), `θ_p ≥ 0` y `W_p`, y en la que todos
los términos sean `≥ 0`. *Prueba:* (1.1) vale en todo `L²(I)`, y daría `a_T(1) ≥ 0`, contra el Lema 3.1. □

La misma prueba vale para toda representación «suma de cuadrados más potencial `≥ 0`» que valga en `L²(I)` sin usar
`P_T`. Es elemental, no usa P47 cor:Tarch y cubre el hueco de signo variable de `ROUND_007_A` §2 en la parte en que
se conserva el cuadrado. No cubre cotas `Π_p ⪯ M_{V_p}` que valgan **sólo** sobre `P_T`. No depende del peso:
vale igual con `c = 2`, sin una potencia de primo o con peso de tipo Beurling. Es un cierre de clase, no un
falsificador de un paso nombrado.

**Consecuencia.** Toda prueba local debe usar las restricciones `∫F e_± = 0`, es decir contener términos que se
anulen sobre `P_T`, como los de Lagrange `2⟨F,e_±⟩⟨F,g_±⟩`, o un término que no sea manifiestamente `≥ 0`.

## 4. Estado fundamental tras modificación de Lagrange (NUMÉRICO)

Modelo de Nyström: `n` nodos de punto medio, el contacto interpolado linealmente y `K` sin la diagonal. Este modelo
grueso da un fondo `a|P_T` de `+4.8·10⁻⁸` en `T = 0.62` con `n = 160`. Su error, del orden de `10⁻⁶`, sólo sirve
para orientarse. Script: `scratchpad/r18.py` y `r18s.py`, temporales.

- **Clase de Perron con Lagrange.** `Q' = a_T + e_+⊗g_+ + g_+⊗e_+ + e_−⊗g_− + g_−⊗e_−`, con `g_±` libres
  (coinciden con `a_T` sobre `P_T`). Se exige que el núcleo fuera de la diagonal sea `≤ 0` (matriz Z, que admite
  representación (1.1) con `φ > 0`) y se maximiza `τ` con `Q' ⪰ τ`. Resultados:
  `τ = −0.28` en `T = 0.5` (`n = 100`), donde `a_T ≻ 0` sobre `P_T` (fondo `7·10⁻⁵`), y
  `τ = −0.80` en `T = 0.62` (`n = 40, 60, 70`, estable). Falla por varios órdenes de magnitud respecto del fondo,
  ya bajo el umbral. Lectura (ARGUED): una modificación de rango dos con núcleo acotado no compensa el defecto
  `a_T(1)/2T ≈ −2.5` sin crear acoplamientos positivos.
- **Gauge de signatura.** Se toma `σ = signo` del autovector de fondo de `a|P_T` y se pide que `Q'` conjugado por
  `diag σ` sea Z. El problema es infactible (`T = 0.62`, `n = 60`).
  **Lema 4.1 (PROVED si `g_±` es acotada cerca de los nodos).** Si `σ` cambia de signo en un punto interior `t_0`,
  la condición Z obliga a `L(t,s) ≤ −½K(|t−s|)` para los pares `t < t_0 < s` (con `L` la parte de Lagrange).
  Como `K(u) ≥ 1/u`, esto exige `L → −∞`, imposible para `e_± g_±` acotados. Para `g ∈ L²` general: ARGUED.
- **Estructura nodal** (`T = 0.62, 0.65, 0.68`). El autovector de fondo de `a|P_T` es par, con patrón `+ − +` y
  nodos en `≈ ±0.2`. Tiene el **mismo** signo en las dos zonas extremas `L_3 = [−T, T − log 3]` y
  `R_3 = [−T + log 3, T]`, así que los pares del contacto de 3 tienen `φφ > 0`. Para el contacto de 2 los signos son
  mixtos. La forma «impar a través de las zonas extremas» que suponía el encargo no se observa.

## 5. Qué rompe, qué queda, y qué haría falta

- No hay fórmula de `θ_p`, `W_p`. No se probó `q_p ⪰ 0` en ningún `T`.
- La desigualdad que falta tiene una forma precisa. Toda prueba local por encima de `T*` debe contener un
  ingrediente que no sea de Perron y que use `P_T`: una desigualdad de tipo Poincaré o Wirtinger restringida,
  `¼∬K(ΔF)² + ∫W F² ≥ μ_T ‖F‖² − (términos que se anulan sobre P_T)` con `μ_T` explícito, que la parte manifiesta
  no puede suplir (§3). Un candidato honesto sería esa desigualdad con constante explícita para el núcleo `K` en
  la ventana, usada por primo. Su relación con el certificado de P47 (thm:index, cor:Tarch) es directa: P47 la
  obtiene por intervalos. Hacerla a mano no se intentó en esta ronda.
- Controles (informativos): el Corolario 3.2 es ciego al peso (vale igual en `c = 2`, con 3 borrado o con 2
  borrado), como corresponde a un NO-GO de clase. La parte numérica de §4 no se repitió con controles.
- Lo que pasa en `T ≈ 0.697` no interviene: la clase muere antes, en todo `T ≥ 0.2`.

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | Identidad (1.1) para `φ` de cualquier signo | PROVED |
| 2 | El cuadrado del contacto lleva el signo de `φ(t)φ(t−log n)`: el signo variable lo vuelve negativo | PROVED |
| 3 | Lema 3.1: `a_T(1) < 0` en `[0.2, 0.75]`, con cota explícita | PROVED (con `ψ(¼)` CITED) |
| 4 | Corolario 3.2: ninguna representación manifiesta válida en `L²(I)` | PROVED |
| 5 | Clase de Perron con Lagrange: `τ = −0.28` (0.5), `−0.80` (0.62) | NUMÉRICO |
| 6 | Lema 4.1, gauge de signatura con nodo interior | PROVED (`g` acotada); ARGUED (general) |
| 7 | Estructura nodal del fondo (par, `+ − +`, nodos `≈ ±0.2`) | NUMÉRICO (modelo grueso) |
| 8 | Reparto explícito o prueba local por mecanismo | OPEN |
