# Doc 120 — Inventario en fuente de la maquinaria Connes–Consani(–Moscovici)

**Phase 39 — Interfaz G1↔G2. Junio 2026. Autor: David Alejandro Trejo Pizzo.**

---

## §0. Propósito, método y disciplina de etiquetado

Este documento cataloga, leyendo en fuente (arXiv), **qué estructuras existen hoy** en el
programa Connes–Consani(–Moscovici) [en adelante CC / CCM], con enunciados precisos, para
medirlas después contra el "shopping list" del roadmap del programa
(`06-papers/roadmap-rh/roadmap-rh.tex`): los nodos **G1** (cohomología finito-dimensional
sobre el cuadrado del sitio de escala), **G2** (estructura de peso/signatura — *the wall*),
**G3** (fórmula de Lefschetz = fórmula explícita), **G4** (cota a priori
$\kappa(Q) = 2m < \infty$), y la especificación **S1–S3** (finitud de *signatura*, no de
característica de Euler; trazas aritméticas autónomas; incondicionalidad).

**Disciplina de etiquetado (regla absoluta de este documento):**

- **[VERIFICADO]** — leído en fuente en esta sesión (junio 2026), vía arXiv
  (página abs, ar5iv o HTML del paper), con cita exacta de paper y sección/teorema.
  *Caveat metodológico declarado:* la lectura se hizo mediante extracción asistida del
  texto fuente; las citas textuales reproducidas abajo provienen del texto del paper tal
  como fue extraído. Los números de teorema y los enunciados se reportan tal como
  aparecen en la fuente extraída.
- **[VERIFICADO previo — Doc 100]** — verificado contra fuente completa en la sesión de
  Doc 100 (junio 2026), reutilizado aquí con su cita original.
- **[NO VERIFICADO]** — de memoria, de fuente secundaria, o no encontrado en fuente en
  esta sesión.
- **[INTERPRETACIÓN]** — lectura mía/del programa; **no** es afirmación de CC.

**Fuentes leídas en esta sesión** (todas accedidas junio 2026):

| arXiv | Título exacto | Estado |
|---|---|---|
| 1405.4527 | *The Arithmetic Site* | abs leído |
| 1502.05580 | *Geometry of the arithmetic site* | abs + texto completo (ar5iv) |
| 1507.05818 | *The Scaling Site* | abs leído |
| 1603.03191 | *Geometry of the scaling site* | abs + texto completo (ar5iv) |
| 1509.05576 | *An essay on the Riemann Hypothesis* (Connes solo) | texto (ar5iv), pasajes sobre la estrategia RR |
| 1805.10501 | *The Riemann-Roch strategy, Complex lift of the Scaling Site* | texto (ar5iv) |
| 2205.01391 | *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$* | abs + texto (ar5iv) |
| 2306.00456 | *Riemann-Roch for the ring $\mathbb Z$* | abs + texto (ar5iv) |
| 2602.15941 | *On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$* | texto (arXiv HTML v1) |
| 2006.13771 | *Weil positivity and Trace formula, the archimedean place* | abs + texto (ar5iv); además Doc 100 |
| 2310.18423 | *Zeta zeros and prolate wave operators* (CCM) | abs; texto verificado en Doc 100 |
| 2511.22755 | *Zeta Spectral Triples* (CCM) | abs + texto (arXiv HTML v1) |
| 2602.04022 | *The Riemann Hypothesis: Past, Present and a Letter Through Time* (Connes) | abs + texto (arXiv HTML v1) |
| 2008.10974 | *Quasi-inner functions and local factors* | [VERIFICADO previo — Doc 100] |

Correcciones a las referencias del encargo: la positividad semilocal **no** está en
2310.18423 (ese es el paper de operadores prolatos semilocales, y la positividad para
$|S|\ge 2$ sigue siendo estrategia declarada, no teorema — ver §4 y §5);
"Riemann-Roch for Spec Z̄" es **arXiv:2205.01391** (v2 marzo 2023, publicado — la
búsqueda devuelve la versión de journal en Bull. Sci. Math. vía ScienceDirect
[NO VERIFICADO el dato bibliográfico exacto del journal]); hay un segundo paper
**arXiv:2306.00456** que mejora la fórmula; "On the Jacobian of Spec Z̄" **existe**:
**arXiv:2602.15941**, febrero 2026. La "carta" de Connes es **arXiv:2602.04022**
(sometida al Journal of Open Mathematical Problems el 19-09-2025, posteada 03-02-2026).

---

## §1. Pieza 1 — EL SITIO ARITMÉTICO

### 1.1 Referencias verificadas

- A. Connes, C. Consani, *The Arithmetic Site*, arXiv:1405.4527 (mayo 2014; nota CRAS).
  **[VERIFICADO]** (abs).
- A. Connes, C. Consani, *Geometry of the arithmetic site*, arXiv:1502.05580
  (febrero 2015; Adv. Math. según memoria del programa [NO VERIFICADO el dato de journal
  en esta sesión — la página abs no lo lista]). **[VERIFICADO]** (texto completo).

### 1.2 Objetos definidos

1. **El topos $\widehat{\mathbb N^\times}$**: el topos de conjuntos con acción del
   monoide multiplicativo $\mathbb N^\times$ de enteros positivos no nulos (functores
   $\mathbb N^\times \to \mathfrak{Sets}$). **[VERIFICADO]** (1502.05580, abstract:
   *"The underlying topological space of the arithmetic site is the topos of functors
   from the multiplicative semigroup of non-zero natural numbers to the category of
   sets"*).
2. **El haz de estructura $\mathbb Z_{\max} := (\mathbb Z \cup \{-\infty\}, \max, +)$**,
   semianillo de característica 1 (los "enteros tropicales"), con $\mathbb N^\times$
   actuando por **endomorfismos de Frobenius** $\mathrm{Fr}_n(x) = nx$. **[VERIFICADO]**
   (1502.05580, Definición 3.1, textual: *"The arithmetic site
   $(\widehat{\mathbb N^\times}, \mathbb Z_{\max})$ is the topos
   $\widehat{\mathbb N^\times}$ endowed with the structure sheaf
   $\mathcal O := \mathbb Z_{\max}$ viewed as a semiring in the topos using the action
   of $\mathbb N^\times$ by the Frobenius endomorphisms"*).
3. **El semicuerpo $\mathbb R_+^{\max}$** (reales tropicales) con su grupo de
   automorfismos de Frobenius $\mathrm{Fr}_\lambda$, $\lambda \in \mathbb R_+^*$.
   **[VERIFICADO]** (ibid., Teorema 1.1 y abstract).

### 1.3 Teoremas principales

- **Teorema (puntos sobre $\mathbb R_+^{\max}$).** Textual (1502.05580, Theorem 1.1):
  *"The set of points of the arithmetic site over $\mathbb R_+^{\max}$ coincides with
  the quotient of $\mathbb A_{\mathbb Q}/\mathbb Q^\times$ by the action of
  $\hat{\mathbb Z}^\times$. The action of the Frobenius automorphisms
  $\mathrm{Fr}_\lambda$ of $\mathbb R_+^{\max}$ on these points corresponds to the
  action of the idèle class group."* **[VERIFICADO]**.
  Es decir: los puntos del objeto combinatorio numerable
  $(\widehat{\mathbb N^\times}, \mathbb Z_{\max})$ sobre el semicuerpo tropical
  **son** el espacio de clases de adeles módulo el compacto maximal, y el flujo de
  escala (la acción de $\mathbb R_+^* \subset C_{\mathbb Q}$ cuyo espectro de puntos
  fijos da los ceros de $\zeta$ en la traza de Connes 1999) **es** Frobenius.
- **Teorema (semigrupo de correspondencias de Frobenius).** Textual (1502.05580,
  Theorem 1.2 / §6): existen correspondencias $\Psi(\lambda)$, $\lambda \in \mathbb R_+^*$,
  subvariedades del cuadrado del sitio, tales que *"for
  $\lambda, \lambda' \in \mathbb R_+^\times$ such that $\lambda\lambda' \notin \mathbb Q$,
  one has $\Psi(\lambda) \circ \Psi(\lambda') = \Psi(\lambda\lambda')$."*
  **[VERIFICADO]**. Nótese la condición $\lambda\lambda' \notin \mathbb Q$: la ley de
  composición es la esperada **solo genéricamente**; en valores racionales hay un
  fenómeno de discontinuidad ("the law of composition... holds unconditionally only up
  to a subtlety" — paráfrasis; el enunciado exacto condicionado es el citado).
  Coincide con lo registrado en Doc 106 §3.3 **[VERIFICADO previo — Doc 106]**.
- **El cuadrado del sitio aparece ya aquí**: el cuadrado no reducido lleva haz de
  estructura $\mathbb Z_{\min} \otimes_{\mathbb B} \mathbb Z_{\min}$, y en el cuadrado
  reducido las secciones son **polígonos de Newton** con operaciones de envolvente
  convexa. Y (1502.05580, Proposition 6.11, textual): *"The points of the square of the
  arithmetic site over $\mathbb R_+^{\max}$ coincide with the product of the points of
  the arithmetic site over $\mathbb R_+^{\max}$."* **[VERIFICADO]**. Ver §6.

### 1.4 Lo que NO está

- Ninguna cohomología del sitio (ni $H^0$ ni $H^1$ de haces sobre
  $\widehat{\mathbb N^\times}$) se define en estos papers. **[VERIFICADO — evidente del
  enunciado: los papers definen topos, haz, puntos y correspondencias; no hay teoría
  cohomológica]**.
- Ninguna forma bilineal, apareamiento o teoría de intersección sobre el cuadrado: las
  $\Psi(\lambda)$ se componen pero no se intersecan. **[VERIFICADO — evidente]**.
- La ley de composición de Frobenius en valores racionales no es exacta (condición
  $\lambda\lambda' \notin \mathbb Q$). **[VERIFICADO]**.

---

## §2. Pieza 2 — EL SITIO DE ESCALA

### 2.1 Referencias verificadas

- A. Connes, C. Consani, *The Scaling Site*, arXiv:1507.05818 (julio 2015; nota CRAS).
  **[VERIFICADO]** (abs).
- A. Connes, C. Consani, *Geometry of the scaling site*, arXiv:1603.03191 (marzo 2016;
  Selecta Math. según memoria [NO VERIFICADO journal]). **[VERIFICADO]** (texto).

### 2.2 Objetos definidos

1. **El sitio de escala** $\mathscr S = ([0,\infty) \rtimes \mathbb N^\times, \mathcal O)$:
   extensión de escalares del sitio aritmético de $\mathbb B$ a $\mathbb R_+^{\max}$;
   topos semi-producto de la semirrecta euclídea por la acción multiplicativa de
   $\mathbb N^\times$. Haz de estructura: *"convex, piecewise affine functions with
   integral slopes"*, con valores en $\mathbb R_{\max}$ (suma = max, producto = +).
   **[VERIFICADO]** (1603.03191, abstract y §2).
2. **Puntos** = de nuevo el espacio de clases de adeles
   $\mathbb A_{\mathbb Q}/\mathbb Q^\times$ módulo $\hat{\mathbb Z}^\times$, que ahora
   **hereda estructura de curva tropical** del topos. **[VERIFICADO]** (abstract).
3. **Las órbitas periódicas $C_p = \mathbb R_+^*/p^{\mathbb Z}$**, una por cada primo
   $p$: círculos cuasi-tropicales, análogos en característica 1 de la uniformización de
   Jacobi $E = \mathbb C^*/q^{\mathbb Z}$ de curvas elípticas. Haz $\mathcal O_p$:
   funciones periódicas $f(p\lambda) = f(\lambda)$, convexas, afines a trozos, con
   pendientes en $H_p \subset \mathbb Q$ (racionales con denominador potencia de $p$).
   **[VERIFICADO]** (1603.03191, §3; 1507.05818 abstract).
4. **Divisores de Cartier sobre $C_p$**, grado real, funciones theta. **[VERIFICADO]**.

### 2.3 Teoremas principales

- **Grupo de clases de divisores** (1603.03191, Theorem 5.6 en la numeración del texto
  extraído): el par (grado, característica torsional) induce un isomorfismo
  $$\mathrm{Div}(C_p)/\mathcal P \;\xrightarrow{\;(\deg,\chi)\;}\; \mathbb R \times \mathbb Z/(p-1)\mathbb Z.$$
  **[VERIFICADO]**. En 1507.05818 (abstract) lo enuncian como: las órbitas periódicas
  dan análogos de curvas elípticas *"whose Jacobians are cyclic groups of order $p-1$"*
  — i.e. $J(C_p) = (\mathrm{Div}^0/\mathcal P) \cong \mathbb Z/(p-1)\mathbb Z$.
  **[VERIFICADO]** (abs). El grado es **real**, no entero (refleja $H_p$).
- **Funciones theta** (1603.03191, §5): se construye
  $\theta(\lambda) = \sum_{m\ge 0} (0 \vee (1 - p^m \lambda)) + \sum_{m\ge 1} (0 \vee (p^{-m}\lambda - 1))$
  (suma tropical infinita, no producto), y (Theorem 5.12 del texto extraído) toda
  función racional sobre $C_p$ se expresa en combinaciones finitas de thetas
  $\Theta(h,\mu)$ más términos lineales y constantes. **[VERIFICADO]**.
- **Riemann–Roch tropical sobre $C_p$** — ver Pieza 3, §3.1.

### 2.4 ¿Qué juega el rol de género?

- **No hay término de género en su fórmula RR sobre $C_p$** (ver §3.1): la fórmula es
  exactamente $\dim_{\mathbb R} H^0(D) - \dim_{\mathbb R} H^0(-D) = \deg D$.
  **[VERIFICADO]** (1603.03191, Theorem 5.17 del texto extraído).
- **[INTERPRETACIÓN]**: la forma de la fórmula es la de una curva **elíptica**
  ($g = 1$, $K = 0$): en una curva elíptica clásica
  $\ell(D) - \ell(K - D) = \deg D$ con $K = 0$, de modo que el sustituto de la dualidad
  de Serre aquí es la involución $D \mapsto -D = K - D$ con **divisor canónico
  trivial**. Esto es consistente con la analogía declarada de CC ($C_p$ como análogo de
  $\mathbb C^*/q^{\mathbb Z}$) y con $J(C_p)$ finito cíclico (análogo de los puntos de
  una elíptica sobre $\mathbb F_p$... de hecho $|J(C_p)| = p - 1 = $ número de puntos de
  $\mathbb G_m(\mathbb F_p)$ — lo que sugiere más bien género "multiplicativo").
  CC **no** llaman a esto dualidad de Serre en este paper. **[VERIFICADO que el paper
  no desarrolla dualidad de Serre ni apareamientos bilineales — evidente del texto]**.

### 2.5 Lo que NO está

- Cohomología $H^1$ de haces: el RR usa solo $H^0$ y la involución $D \mapsto -D$.
- Teoría de intersección sobre $C_p \times C_p$ o sobre $\mathscr S \times \mathscr S$.
- Ningún apareamiento bilineal. **[VERIFICADO — evidente]**.
- Lo abierto declarado (abstract/Introducción): extender la geometría de característica 1
  hasta capturar la función zeta completa; trasplantar la prueba de RH de cuerpos de
  funciones. **[VERIFICADO]** (paráfrasis del texto extraído).

---

## §3. Pieza 3 — RIEMANN–ROCH: tropical, absoluto, y el Jacobiano de 2026

Esta es la pieza donde el encargo pedía precisión máxima. Hay **cuatro** teoremas RR
distintos en el corpus CC, de naturaleza creciente:

### 3.1 RR tropical sobre la órbita periódica $C_p$ (1603.03191)

- **Cohomologías**: solo $H^0(D) := \{f$ racional $: D + (f) \ge 0\}$ (módulo
  idempotente, no espacio vectorial). **No hay $H^1$**: su rol lo juega $H^0(-D)$.
- **Dimensión**: **continua, real-valuada**, definida como límite normalizado
  $$\mathrm{Dim}_{\mathbb R}(H^0(D)) := \lim_{n\to\infty} p^{-n} \dim_{\mathrm{top}}(H^0(D)^{(p^n)}),$$
  textual del paper (filtración por las pendientes $p^{-n}$). CC mismos señalan la
  analogía con la **dimensión continua de von Neumann tipo II**. **[VERIFICADO]**
  (1603.03191, §5; la analogía tipo II está en el texto).
- **Fórmula** (Theorem 5.17, textual): *"$\mathrm{Dim}_{\mathbb R}(H^0(D)) -
  \mathrm{Dim}_{\mathbb R}(H^0(-D)) = \deg(D), \;\forall D \in \mathrm{Div}(C_p)$."*
  **[VERIFICADO]**. $\chi = \deg$, sin término de género, grados y dimensiones reales.
- **Lo que NO está**: dualidad de Serre con dualizante no trivial; enteros (todo es
  real-valuado — exactamente lo que S1/G2 del roadmap diagnostica como insuficiente:
  *averages, not integers*). **[VERIFICADO — evidente]** + **[INTERPRETACIÓN]** la
  lectura S1.

### 3.2 RR para $\overline{\mathrm{Spec}\,\mathbb Z}$ sobre $\mathbb S[\pm 1]$ (arXiv:2205.01391, v2 2023)

El salto cualitativo: dimensiones **enteras** y **dualidad de Serre genuina**.

- **Base absoluta**: $\mathbb S[\pm 1]$, semianillo esférico $\{0, \pm 1\}$, formalizado
  con **$\Gamma$-anillos de Segal** (functores $\Gamma^{op} \to \mathfrak{Sets}_*$);
  apoyado en su teoría previa de "universal arithmetic over the sphere spectrum".
  **[VERIFICADO]** (abstract textual: *"Both the definitions of the cohomologies and of
  their dimensions rely on a universal arithmetic theory over the sphere spectrum that
  we had previously introduced using Segal's Gamma rings"*).
- **$H^0(D)$**: para $D$ divisor de Arakelov con parte arquimediana $a$, el
  $\mathbb S[\pm 1]$-módulo $\|H\mathbb Z\|_{e^a}$ — textual: *"associates to a finite
  pointed set $X$ the $\mathbb Z$-valued divisors $\sum_i n_i x_i$... fulfilling
  $\sum_i |n_i| \le e^a$"*; es el **núcleo** del morfismo
  $\psi: H\mathbb Q \times H\mathcal O(D) \to H\mathbb A_{\mathbb Q}$ (paralelo exacto
  de la prueba adélica de Weil para cuerpos de funciones). **[VERIFICADO]**.
- **$H^1(D)$**: el **conúcleo** de $\psi$, definido como **$\mathbb S$-módulo con
  tolerancia** (pareja $(H\mathbb A_{\mathbb Q}, \mathcal R)$ con
  $\mathcal R_k := \{(x,y) : x - y \in \mathrm{Image}\,\psi(k_+)\}$), vía Dold–Kan
  aplicado al complejo corto $\psi$. **[VERIFICADO]**. *Este es el primer $H^1$ que CC
  logran definir en todo el programa* — compárese con el obstáculo declarado en
  1805.10501 (§6.3 abajo). **[INTERPRETACIÓN]** la comparación; **[VERIFICADO]** ambos
  extremos.
- **Dimensión entera**: $\dim_{\mathbb S[\pm1]} H^0(D)$ := mínimo número de
  **generadores lineales** (con coeficientes en $\{-1,0,1\}$ y control de la norma
  $\sum |\alpha(f) f| \le e^a$); análogo con la relación de tolerancia para $H^1$.
  **[VERIFICADO]**.
- **Fórmula RR** (Theorem 1.1, textual del texto extraído):
  $$\dim_{\mathbb S[\pm1]} H^0(D) - \dim_{\mathbb S[\pm1]} H^1(D) = \big\lceil \deg' D + \log' 2 \big\rceil' - \mathbb 1_L,$$
  con $\deg' = \deg/\log 3$, $\log' 2 = \log 2/\log 3$, $\lceil\cdot\rceil'$ la
  extensión impar de la función techo, y $\mathbb 1_L$ una función característica de un
  conjunto excepcional $L$ (unión numerable de intervalos
  $(\log'(3^k/2), \log'((3^k{+}1)/2))$). **[VERIFICADO]**.
- **DUALIDAD DE SERRE — existe y es un teorema** (Theorem 1.2, textual):
  $$H^0(K - D) \simeq \overline{\mathrm{Hom}}_{\Gamma \mathcal T_*}\big(H^1(D),\, U(1)_{1/4}\big),$$
  con **divisor canónico $K = -2\{2\}$** ($\deg K = -2\log 2$) y **módulo dualizante
  $U(1)_{1/4} = H^1(K)$**. La dualidad *"derives from Pontryagin duality for tolerance
  $\mathbb S[\pm1]$-modules"* (Proposition 5.2), *"paralleling Weil's adelic
  construction for function fields"* (abstract: *"including the use of Pontryagin
  duality"*). **[VERIFICADO]**.
- **Respuesta directa a la pregunta del encargo (¿hay forma bilineal/apareamiento?):**
  SÍ existe un apareamiento en su teoría: el apareamiento de **dualidad de Pontryagin**
  $H^1(D) \times H^0(K-D) \to U(1)$ subyacente al Teorema 1.2. Es un apareamiento de
  dualidad **perfecto entre espacios distintos** ($H^1$ contra $H^0$ del divisor
  dual), **no** una forma bilineal simétrica sobre un mismo espacio, y **no** trae
  asociada noción alguna de signatura/índice. **[VERIFICADO]** el teorema;
  **[INTERPRETACIÓN]** la clasificación respecto de G2.

### 3.3 RR para el anillo $\mathbb Z$ sobre $\mathbb S$ (arXiv:2306.00456, junio 2023)

- Trabajar sobre la base absoluta $\mathbb S$ (la versión categórica del espectro
  esférico) en vez de $\mathbb S[\pm 1]$ **mejora** la fórmula: el término excepcional
  desaparece — textual: *"The term $\mathbb 1_L$ involving the exceptional set $L$ in
  the earlier formula is now eliminated."* **[VERIFICADO]**.
- **Fórmula** (Theorem 1.1, textual): $\dim_{\mathbb S} H^0(D) - \dim_{\mathbb S} H^1(D)
  = \lceil \deg_2 D \rceil' + 1$, con $\deg_2 = \deg/\log 2$. Para $\deg_2 D \ge 0$:
  $H^1 = 0$ y $\dim H^0 = \lceil \deg_2 D \rceil + 1$. **[VERIFICADO]**.
- **Analogía de género declarada por ellos**, textual: *"(1.1) displays a perfect
  analogy with the Riemann-Roch formula holding for curves of genus 0."* Es decir:
  según CC, $\overline{\mathrm{Spec}\,\mathbb Z}$ sobre $\mathbb S$ se comporta como
  **una curva de género 0** ($\chi = \deg + 1$), con $\mathbb Z = \mathbb S[X]$,
  "$1+1 = X + X^2$" con generador $-2$, y $K = -2\{2\}$ de grado entero
  $\deg_2 K = -2$ (como $K_{\mathbb P^1}$). **[VERIFICADO]** (las dos citas y el dato
  de $K$); la lectura "$\{2\}$ juega el rol del punto al infinito de $\mathbb P^1$" es
  **[INTERPRETACIÓN]**.
- **$H^1$ explícito**: $H^1(D) \simeq (U(1), d)_\lambda$ con $U(1) = \mathbb R/\mathbb Z$
  metrizado y $\lambda = e^{\deg D}$; $\dim_{\mathbb S} U(1)_\lambda = m$ si
  $2^{-m-1} \le \lambda < 2^{-m}$ (Proposition 4.2 del texto extraído). **[VERIFICADO]**.
- **Lo que NO está**: el texto extraído no contiene un enunciado de dualidad de Serre
  separado en este paper (la dualidad es la del paper 2205.01391); no hay mención del
  cuadrado ni de dimensión 2 como paso siguiente declarado. **[VERIFICADO — con el
  caveat de extracción]**.

### 3.4 El Jacobiano de $\overline{\mathrm{Spec}\,\mathbb Z}$ (arXiv:2602.15941, febrero 2026)

**El paper existe** — confirmado en fuente (arXiv HTML v1) y en la lista de
publicaciones de Consani (math.jhu.edu/~kc/Publ2026.pdf). **[VERIFICADO]**.

- **Abstract** (textual, según fuente): *"We interpret the structure of the adele class
  space of the rationals—and specifically its Riemann sector—as the natural monoidal
  extension of the Picard group of the arithmetic curve $\overline{\mathrm{Spec}\,\mathbb Z}$.
  We identify the elements of this space with torsion-free rank-1 abelian groups $L$
  endowed with rigidifying data."* **[VERIFICADO]**.
- **Objetos**: el **monoide de Picard** $\mathrm{Pic}(\overline{\mathrm{Spec}\,\mathbb Z})$
  = moduli de $(L, \|\cdot\|)$ con $L$ abeliano libre de torsión de rango 1 y
  $\|\cdot\|$ **semi**-norma sobre $L \otimes \mathbb R$ (extiende los fibrados de
  línea metrizados de Arakelov **permitiendo degeneración de la norma**); el
  **Jacobiano aritmético** = cociente por la acción de escala $\mathbb R_+^\times$;
  el **sector de Riemann** $X_{\mathbb Q} = \mathbb Q^\times \backslash \mathbb A /
  \hat{\mathbb Z}^\times$. **[VERIFICADO]**.
- **Teorema 1.1** (textual según fuente): la asignación $a \mapsto (L_a, \|\cdot\|_a)$
  induce *"a canonical monoid isomorphism
  $X_{\mathbb Q} \cong \mathrm{Pic}(\overline{\mathrm{Spec}\,\mathbb Z})$"*; con
  realización explícita $L_a = \{q \in \mathbb Q : a_f q \in \hat{\mathbb Z}\}$,
  $\|v\|_a = |a_\infty| |v|$ (Theorem 3.4 del texto extraído). Hay además una
  uniformización (Theorem 1.4): isomorfismo de monoides entre el monoide adélico
  $Y_{\mathbb Q}$ y el moduli de divisores aritméticos **enmarcados** $(L, \xi, \tau)$,
  con el producto de adeles = producto tensorial de marcos. **[VERIFICADO]**.
- **Realización espectral** (§9 del paper): la acción de traslación del grupo de clases
  de ideles $C_{\mathbb Q}$ sobre $\widetilde{\mathrm{Pic}}$ produce una fórmula de
  trazas tipo Lefschetz cuyas contribuciones se localizan en órbitas periódicas;
  queda un término divergente $2h(1)\log\lambda$ en la fórmula semilocal cuyo
  tratamiento riguroso está pendiente (§9.3). **[VERIFICADO]** (según texto extraído).
- **Frase clave de cierre** (textual según fuente): el paso de grupos de Picard a
  **monoides** *"is not merely a generalization. Rather, it is a necessary step for
  incorporating boundary and singular phenomena into the geometric framework—precisely
  the features required for the spectral realization."* **[VERIFICADO]**.
- **Lo que NO está** (verificado por búsqueda en el texto extraído): **ninguna mención**
  de teoría de intersección, cuadrado del sitio, índice de Hodge, positividad de Weil,
  ni de RH como objetivo directo del paper. **[VERIFICADO — con caveat de extracción]**.

### 3.5 Síntesis de la Pieza 3 para la interfaz G1↔G2

**[INTERPRETACIÓN]** (mía, para el programa): el corpus RR de CC tiene hoy una
**bifurcación de virtudes sin intersección**: (i) el RR tropical (3.1) vive sobre el
sitio de escala — el portador natural de G1 — pero con dimensiones **reales** (tipo II)
y sin $H^1$ ni dualidad; (ii) el RR absoluto (3.2–3.3) tiene **enteros, $H^1$, divisor
canónico y dualidad de Serre/Pontryagin** — exactamente el tipo de estructura que G2
pide — pero vive sobre $\overline{\mathrm{Spec}\,\mathbb Z}$ en dimensión 1, **no**
sobre el cuadrado, y su dualidad es un apareamiento de dualidad (perfecto,
$H^1 \times H^0 \to U(1)$), no una forma con signatura. El paper del Jacobiano (3.4) es
el puente declarado entre el lado adélico-espectral y el lado Picard-geométrico, en
dimensión 1. **Nadie ha cruzado todavía "RR absoluto" con "cuadrado".**

---

## §4. Pieza 4 — POSITIVIDAD DE WEIL

### 4.1 Referencias verificadas

- A. Connes, C. Consani, *Weil positivity and Trace formula, the archimedean place*,
  arXiv:2006.13771; Selecta Math. 27, 77 (2021). **[VERIFICADO]** (abs + texto;
  además texto completo en Doc 100).
- A. Connes, C. Consani, *Quasi-inner functions and local factors*, J. Number Theory
  226 (2021) 139–167; arXiv:2008.10974. **[VERIFICADO previo — Doc 100]**.
- CCM, *Zeta zeros and prolate wave operators*, Ann. Funct. Anal. 15 (2024);
  arXiv:2310.18423. **[VERIFICADO]** (abs; texto en Doc 100). — **Este paper NO prueba
  positividad semilocal**; es la infraestructura prolata semilocal.

### 4.2 Qué positividad exacta prueban

- **Teorema 1 de CC 2021** (textual según fuente): para funciones de prueba
  $g \in C_c^\infty([2^{-1/2}, 2^{1/2}])$ (soporte en la ventana $(1/2,2)$ tras
  convolución, i.e. un solo lugar arquimediano visible) con $\hat g(i/2) = \hat g(0) = 0$:
  $$W_\infty(g * g^*) \;\ge\; \mathrm{Tr}\big(\vartheta(g)\,\mathbf S\,\vartheta(g)^*\big) \;\ge\; 0,$$
  donde $\vartheta$ es la acción de escala sobre $L^2(\mathbb R)^{\mathrm{ev}}$ y
  $\mathbf S$ la proyección sobre el **espacio de Sonine** (complemento ortogonal del
  rango de las proyecciones de cutoff $\mathcal P_1 \vee \widehat{\mathcal P}_1$,
  parámetro $\Lambda = 1$). **[VERIFICADO]** (coincide con lo verificado en Doc 100 §2).
- **Forma cuantitativa** (Theorem 6.11 según texto extraído): existe $c$ finito,
  $13 < c < 17$, con $W_\infty(g * g^*) \ge \mathrm{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)
  - c\,|\hat g(0)|^2$ — una **única dirección de condicionamiento** $\hat g(0)$ con
  defecto de rango finito. La frase de CC sobre la contribución extra en la línea
  crítica: *"as if one would multiply $\zeta(z)$ by $(z - 1/2)^{17}$"*. **[VERIFICADO]**
  (+ Doc 100, Corolario 2).
- **Método**: (i) fórmula de trazas semilocal de Connes 1999 (teorema incondicional);
  (ii) compresión de la acción de escala al espacio de Sonine — positividad **por
  construcción** (es una traza $\mathrm{Tr}(T \cdot T^*)$); (iii) la discrepancia
  Weil−Sonine expresada en **funciones esferoidales prolatas** y controlada con
  **matrices de Toeplitz hermitianas**; (iv) la representación del grupo diedral
  infinito $\mathbb Z \rtimes \mathbb Z/2$ generada por $(\mathcal P_1,
  \widehat{\mathcal P}_1)$. **[VERIFICADO]** (abstract textual + Doc 100 §2.4).

### 4.3 Qué dicen ELLOS de la extensión global/semilocal

- Abstract de 2006.13771, textual: *"All the ingredients and tools used above make
  sense in the general semi-local case, where Weil positivity implies RH."*
  **[VERIFICADO]**.
- Introducción, textual (según fuente): *"It is thus natural to implement this
  fundamental positivity in the semi-local framework applied to the finite set of
  places $\{\infty, 2, 3, \ldots, p\}$"* — con la condición de soporte
  $\mathrm{Supp}(f) \subset (p^{-1}, p)$, que **crece** con el conjunto de lugares
  (verificado en Doc 100 §5: la versión "el espacio de prueba se achica" del obstáculo
  quedó refutada). **[VERIFICADO]**.
- CCM 2024 (textual, Doc 100 §2.5b): la positividad semilocal para $|S| \ge 2$ es
  **estrategia declarada, no teorema**: *"We expect that the use of such operator
  theoretic tools in the semilocal case will open a way to treat Weil positivity as in
  [CC 2021]..."*. **[VERIFICADO previo — Doc 100]**.
- **No existe a junio 2026**, en lo buscado, prueba de positividad semilocal con algún
  lugar finito ($P(n)$, $n > 2$ en la notación del Doc 100). **[NO VERIFICADO que
  exista; búsqueda negativa en esta sesión y en Doc 100]**.

### 4.4 Conexión declarada por ellos con el cuadrado (¡cita clave!)

En 2006.13771 (introducción, textual según fuente): el enfoque geométrico
*"unveiled a novel geometric landscape still in development for an **intersection
theory of divisors (on the square of the Scaling Site)**"*. **[VERIFICADO]**. Es la
declaración explícita de CC de que su propio teorema de positividad arquimediana es,
en su lectura, un fragmento de la teoría de intersección sobre el cuadrado que no
existe todavía. Ver §6.

---

## §5. Pieza 5 — TRIPLES ESPECTRALES ZETA

### 5.1 Referencias verificadas

- CCM, *Zeta zeros and prolate wave operators*, arXiv:2310.18423, Ann. Funct. Anal. 15
  (2024). **[VERIFICADO]** (abs): *"We integrate in the framework of the semilocal
  trace formula two recent discoveries on the spectral realization of the zeros of the
  Riemann zeta function by introducing a semilocal analogue of the prolate wave
  operator."*
- CCM, *Zeta Spectral Triples*, arXiv:2511.22755 (27 noviembre 2025; *"to appear in EMS
  Lecture Notes... Applications of Noncommutative Geometry..."*). **[VERIFICADO]**
  (abs + texto HTML).
- A. Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*,
  arXiv:2602.04022 (3 febrero 2026; sometido al Journal of Open Mathematical Problems
  19-09-2025). **[VERIFICADO]** (abs + texto HTML). La referencia del encargo era
  correcta.

### 5.2 Qué operadores construyen (2511.22755)

- **El operador**: $D_{\log}^{(\lambda,N)}$, **perturbación de rango uno** del operador
  de escala $D_{\log}^{(\lambda)} = -i u\,\partial_u$ sobre
  $L^2([\lambda^{-1}, \lambda], d^*u)$ con condiciones de borde periódicas (espectro
  libre $2\pi n/L$, $L = 2\log\lambda$). **[VERIFICADO]**.
- **El insumo aritmético**: la forma cuadrática de Weil $QW_\lambda$ (polarización de
  la fórmula explícita: $W_\infty$ + $\sum_p W_p$ + términos de polos $W_{0,2}$)
  restringida a subespacios finito-dimensionales $E_N$; textual: *"the construction
  only involves the Euler products over the primes $p \le x = \lambda^2$."*
  **[VERIFICADO]**.
- **Estructura de la matriz truncada** (relevante para Pieza 7): en la base $\{V_n\}$,
  $\tau_{ii} = a_i$, $\tau_{ij} = (b_i - b_j)/(i - j)$ para $i \ne j$, con
  $a_{-j} = a_j$, $b_{-j} = -b_j$; la autoadjunción de la perturbación de rango uno se
  garantiza con *"the extension... of the classical Carathéodory–Fejér theorem for
  Toeplitz matrices"*. **[VERIFICADO]**.

### 5.3 Qué prueban vs qué observan (2511.22755)

- **Probado** (Theorem 1.1 según texto extraído): (i) $D_{\log}^{(\lambda,N)}$ es
  autoadjunto en $E_N' \oplus E_N^\perp$ con el producto interno
  $QW_\lambda^N - \epsilon_N\langle\cdot|\cdot\rangle$; (ii) el determinante
  regularizado es $\det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i \lambda^{-iz}
  \widehat{\xi}(z)$ con $\xi$ el autovector minimal; (iii) $\widehat{\xi}(z)$ es
  **entera con todos sus ceros reales**, y esos ceros son el espectro.
  **[VERIFICADO]**. — Es decir: lo que está probado es que los ceros aproximantes
  están **exactamente en la línea crítica** (autoadjunción real), para cada
  $(\lambda, N)$ finito.
- **Observado, no probado**: que esos espectros convergen a los ceros de $\zeta$.
  Con primos $\le 13$: primeros 50 ceros con error entre $2.5 \times 10^{-55}$ y
  $10^{-3}$; textual: *"The probability of achieving such precise approximations by
  chance is approximately $10^{-1235}$."* **[VERIFICADO]**.

### 5.4 Lo abierto declarado por ellos

- Textual (2511.22755): *"Establishing this convergence rigorously would amount to a
  proof of the Riemann Hypothesis."* **[VERIFICADO]**.
- El obstáculo principal nombrado (§7 del paper, textual): *"Justifying rigorously this
  step is the main remaining obstacle to our approach to RH"* — el paso es que la
  "educated guess" $k_\lambda$ (deformación de autofunciones **prolatas** vía el
  operador $PW_\lambda = -\partial_x[(\lambda^2 - x^2)\partial_x] + (2\pi\lambda x)^2$)
  aproxime rigurosamente al autovector minimal $\xi_\lambda$ de $QW_\lambda$.
  **[VERIFICADO]**.
- Estrategia secundaria declarada: convergencia de los determinantes regularizados
  normalizados hacia la función $\Xi$ de Riemann (con Hurwitz para transferir los
  ceros). **[VERIFICADO]**.
- Sobre el rol de "CF" del encargo: en el texto extraído de 2511.22755 **no aparece
  mención de fracciones continuas**; si el encargo se refería a Carathéodory–Fejér,
  ese rol sí está (autoadjunción vía Toeplitz). **[VERIFICADO — búsqueda negativa con
  caveat de extracción]**.
- En 2602.04022 (Connes solo), la "carta a Riemann" extremiza la forma cuadrática de
  Weil con primos $< 13$ con matemática del siglo XIX; **prueba** que los valores
  aproximantes caen exactamente en la línea crítica (textual: *"we prove a general
  result that these approximating values lie exactly on the critical line"*); y
  concluye, textual: *"While the numerical evidence in support of this is
  overwhelming, evidence alone is not a proof"* y *"It is of course possible that a
  complete proof along these lines may encounter serious obstacles."* Propone como
  camino la convergencia de ceros de productos de Euler finitos a infinitos vía
  fórmulas de trazas, destacando que la ventaja del espacio semilocal $Y_S$ frente al
  adélico completo es **de teoría de la medida**. **[VERIFICADO]**.

### 5.5 [INTERPRETACIÓN] para el programa

La línea "zeta spectral triples" es la encarnación operatorial de la **Ruta A/analítica**
del roadmap, no de la espina G1–G4: produce autoadjunción (= línea crítica) por
construcción en cada nivel finito y desplaza TODO el contenido de RH a un enunciado de
convergencia/perturbación — estructuralmente isomorfo al obstáculo $\mathbf O_{SL}$
(no-uniformidad en $n$) ya catalogado en Doc 100 §5. No aporta por sí misma la
estructura de peso/signatura de G2; aporta, eso sí, la **forma cuadrática truncada
explícita** $QW_\lambda^N$ con su estructura Toeplitz-más-rango-finito (ver §7).

---

## §6. Pieza 6 — EL CUADRADO: lo que ellos han escrito sobre $C \times C$ aritmético

Esta es la pieza central para G1↔G2. Cronología de declaraciones explícitas de CC:

### 6.1 El cuadrado del sitio aritmético (1502.05580, 2015)

Existe como topos semi-anillado: el cuadrado no reducido con haz
$\mathbb Z_{\min} \otimes_{\mathbb B} \mathbb Z_{\min}$, el reducido con secciones =
**polígonos de Newton** (operaciones de envolvente convexa); sus puntos sobre
$\mathbb R_+^{\max}$ son el producto de los puntos del sitio (Prop. 6.11); y las
correspondencias de Frobenius $\Psi(\lambda)$ viven en él como subvariedades, con
composición exacta solo para $\lambda\lambda' \notin \mathbb Q$. **[VERIFICADO]** (§1.3).
**Lo que falta en 2015**: cualquier teoría de divisores, intersección o cohomología
sobre ese cuadrado. **[VERIFICADO — evidente]**.

### 6.2 El diagnóstico del *Essay* de Connes (1509.05576, 2015)

- Connes describe **tres estrategias** hacia RH, textual (según fuente): (1) *"based on
  Riemannian spaces and Selberg's work on the trace formula"*; (2) *"based on algebraic
  geometry and the Riemann-Roch theorem"*; (3) *"based on the development of a suitable
  'Weil cohomology', the role of Segal's $\Gamma$-rings"*. **[VERIFICADO]**.
- Sobre la prueba modelo (Weil vía Mattuck–Tate/Grothendieck): aplica un lema de
  positividad a la forma cuadrática $\mathfrak s(D, D') = D \cdot D'$ sobre
  $C \times C$, y el rol de RR es, textual: *"if $D.D > 0$ then after a suitable
  rescaling... one gets $\ell(nD) > 1$"* — RR como **productor de secciones** que
  alimenta el índice de Hodge. **[VERIFICADO]** (pasajes según fuente).
- Diagnóstico de Connes, textual: *"it is highly desirable to find a geometric
  framework for the Riemann zeta function itself, in which the Hasse-Weil formula, the
  geometric interpretation of the explicit formulas, the Frobenius correspondences...
  all make sense"* y — crucial en honestidad — *"It is yet unclear if this is the
  right set-up for the final Riemann-Roch step."* **[VERIFICADO]**.

### 6.3 *The Riemann-Roch strategy* (1805.10501, 2018) — la declaración más explícita

- Objetivo declarado, textual: *"adapting in characteristic zero Weil's proof, of RH in
  positive characteristic, following the ideas of Mattuck-Tate and Grothendieck."*
  **[VERIFICADO]**.
- **El obstáculo nombrado por ellos**, textual: *"However, in the process to formulate
  a Riemann-Roch theorem on the square of the Scaling Site one faces a substantial
  difficulty"* — y la dificultad es **$H^1$ en característica 1**: *"The problem, which
  is still open at this time, has to do with an appropriate definition of the sheaf
  cohomology (as idempotent monoid) $H^1$... when applied to Čech covers, the presence
  of the null elements creates unwanted contributions to the cohomology which so far we
  are unable to handle."* **[VERIFICADO]**. — Este es SU diagnóstico de qué falta:
  no la positividad, no la fórmula de trazas, sino **la cohomología $H^1$ idempotente
  sobre el cuadrado**, bloqueada por los elementos nulos en los recubrimientos de Čech.
- **Su respuesta táctica**: el **descenso tropical** — textual: *"deduce existence
  results in characteristic one from available Riemann-Roch theorems in complex
  geometry"*, vía funciones casi-periódicas (Bohr–Jessen–Tornehave): toda función
  convexa es tropicalización de una función analítica casi-periódica. Y la construcción
  del **levantamiento complejo** del espacio de clases de adeles:
  $\mathcal C_{\mathbb Q} = \mathbb Q^\times \backslash (G \times \mathbb A_{\mathbb Q})$,
  interpretado como moduli de curvas elípticas con estructura triangular
  ($\mathbb Q$-redes parabólicas), relación de equivalencia generada por **isogenias**,
  foliación por hojas complejas 1-dimensionales. **[VERIFICADO]**.
- **[INTERPRETACIÓN]**: nótese la inversión estratégica: en vez de construir RR en el
  cuadrado tropical, lo esquivan levantando a $\mathbb C$ y descendiendo existencia.
  A junio 2026 no hay continuación publicada que complete ni el RR en dimensión 2
  tropical ni el RR sobre el levantamiento complejo (búsqueda negativa). **[NO
  VERIFICADO que exista continuación]**.

### 6.4 El estado 2020–2026

- 2006.13771 (2021): la cita de §4.4 — la positividad arquimediana se presenta como
  parte de *"a novel geometric landscape still in development for an intersection
  theory of divisors (on the square of the Scaling Site)"*. **[VERIFICADO]**. O sea:
  para CC, **su teorema de positividad ES el germen analítico del índice de Hodge del
  cuadrado** — pero la teoría de intersección como tal sigue "in development".
- 2205.01391/2306.00456 (2022–23): resuelven $H^1$ **en dimensión 1** sobre la base
  absoluta ($\Gamma$-anillos + tolerancia + Dold–Kan), con dualidad. **[VERIFICADO]**.
  **[INTERPRETACIÓN]**: es plausible leer este desarrollo como su ataque al obstáculo
  de 1805.10501 por la vía de cambiar de base (de semianillos idempotentes a
  $\mathbb S$-módulos), donde el problema de los "null elements" de Čech se domestica
  con tolerancias; pero CC no enuncian esa conexión explícitamente en los textos
  leídos. **[NO VERIFICADO como afirmación de ellos]**.
- 2602.15941 (2026): Picard/Jacobiano de $\overline{\mathrm{Spec}\,\mathbb Z}$ en
  dimensión 1, sin mención del cuadrado ni de intersección. **[VERIFICADO]**.
- **Conclusión de la Pieza 6**: a junio 2026, **no existe en el corpus CC publicado**:
  RR sobre el cuadrado del sitio de escala; teoría de intersección de divisores sobre
  el cuadrado (solo anunciada como "in development" en 2021); análogo del índice de
  Hodge/Castelnuovo; forma de intersección con signatura. El obstáculo auto-declarado
  (1805.10501) es $H^1$ idempotente en dimensión 2; su herramienta nueva (tolerancia
  sobre $\mathbb S$) lo resuelve por ahora solo en dimensión 1. **[VERIFICADO el
  negativo dentro de lo leído/buscado]**.

---

## §7. Pieza 7 — HALLAZGOS LATERALES relevantes a pesos/signaturas/formas

1. **La dualidad de Pontryagin con tolerancia** (2205.01391, Prop. 5.2 + Thm 1.2):
   único apareamiento de dualidad genuino del corpus; dualizante $U(1)_{1/4} = H^1(K)$,
   $K = -2\{2\}$. **[VERIFICADO]**. **[INTERPRETACIÓN]**: para G2 importa porque una
   forma de intersección con signatura sobre el cuadrado debería, en cualquier
   formalización, inducir en la diagonal una dualidad de este tipo; CC ya tienen el
   "lado diagonal" en dimensión 1. La dirección inversa (de dualidad a signatura) es
   exactamente lo que NO está.
2. **Dimensión continua tipo II vs dimensión entera**: la coexistencia en el mismo
   corpus de $\mathrm{Dim}_{\mathbb R}$ (límite normalizado $p^{-n}\dim_{\mathrm{top}}$,
   1603.03191) y $\dim_{\mathbb S}$ (mínimo de generadores con tolerancia, 2306.00456)
   es estructuralmente la transición "promedios → enteros" que el roadmap llama el muro
   G2. CC la han cruzado **en dimensión 1, para dimensiones de cohomología** — no para
   signaturas. **[VERIFICADO ambos extremos; INTERPRETACIÓN la lectura]**.
3. **La estructura fina de la forma de Weil truncada** (2511.22755): matriz
   $\tau_{ij} = (b_i - b_j)/(i-j)$ fuera de la diagonal (tipo **Pick/Loewner**, no
   Toeplitz puro) más diagonal $a_i$; paridades $a_{-j} = a_j$, $b_{-j} = -b_j$.
   **[VERIFICADO]**. **[INTERPRETACIÓN]**: las matrices de Loewner son la maquinaria
   clásica de **monotonía de operadores e índices de inercia**; que la forma de Weil
   truncada sea exactamente de ese tipo es un dato potencialmente directo para el
   cómputo de $\kappa(Q)$ ventana a ventana (conexión con Doc 91/100) que CC usan solo
   para autoadjunción, no para signatura.
4. **Positividad lower-bounded, no definida** (2511.22755, Prop. 3.3 según texto):
   $QW_\lambda$ es **acotada por abajo** y semicontinua — CCM trabajan
   sistemáticamente con "lower bounded + perturbación compacta/finita", nunca con
   formas definidas. **[VERIFICADO]**. Es exactamente el régimen
   $\kappa(Q) < \infty$ del programa (S1), sin que ellos nombren jamás el índice
   negativo como invariante. **[INTERPRETACIÓN]**.
5. **El paso grupo → monoide** (2602.15941): la insistencia de CC en que Picard debe
   ser **monoide** (semi-normas degeneradas, fenómenos de borde) *"precisely the
   features required for the spectral realization"*. **[VERIFICADO]**.
   **[INTERPRETACIÓN]**: los fenómenos de borde/degeneración son donde viven los
   índices de inercia en familias de formas (cruces de autovalores = degeneración de
   la norma); el lenguaje monoidal de CC podría ser el receptáculo natural de un
   flujo espectral, cosa que ellos no dicen.
6. **Frobenius no amplifica**: sobre $(\mathcal K, Q)$ las correspondencias de
   Frobenius actúan por isometrías (Doc 106, Prop. 3.10) — el Frobenius del sitio
   mide, no genera, el defecto. **[VERIFICADO previo — Doc 106, resultado del
   programa, no de CC]**.
7. **Búsqueda negativa de "signature"**: en ninguno de los textos leídos en esta
   sesión aparece la palabra signatura/índice de inercia como invariante de sus
   teorías (la única estructura de signo es positividad/lower-boundedness).
   **[VERIFICADO — negativo, con caveat de extracción]**.

---

## §8. Mapeo contra el shopping list G1–G4 / S1–S3

| Nodo | Lo que CC tienen hoy (verificado) | Lo que falta (declarado por ellos o evidente) |
|---|---|---|
| **G1** (cohomología finito-dim. sobre el cuadrado) | El cuadrado existe como topos semi-anillado (1502.05580 §6); RR tropical en dim 1 (1603.03191); $H^0, H^1$ + dim enteras en dim 1 absoluta (2205.01391, 2306.00456) | $H^1$ idempotente en dim 2: obstáculo auto-declarado (1805.10501, "null elements" en Čech); ninguna cohomología sobre el cuadrado |
| **G2** (peso/signatura) | Dualidad de Serre/Pontryagin en dim 1 (Thm 1.2 de 2205.01391); dimensiones enteras; positividad arquimediana con defecto finito $c < 17$ (2006.13771) | Ninguna forma de intersección, ningún índice de Hodge, ninguna noción de signatura en todo el corpus; la "intersection theory on the square" declarada *in development* desde 2021 sin publicación posterior |
| **G3** (Lefschetz = fórmula explícita) | Fórmula de trazas semilocal (teorema, Connes 1999); acción de $C_{\mathbb Q}$ sobre $\widetilde{\mathrm{Pic}}$ con localización en órbitas periódicas (2602.15941 §9) | El caso global es equivalente a RH, no un teorema; término divergente $2h(1)\log\lambda$ pendiente (2602.15941 §9.3) |
| **G4** ($\kappa(Q) = 2m < \infty$ a priori) | Régimen "lower bounded + rango finito" probado solo en la ventana $(1/2,2)$, un lugar | Sin mecanismo de uniformidad en la ventana (Obstáculo $\mathbf O_{SL}$, Doc 100); CC ni formulan el índice negativo como objetivo |
| **S1** (signatura, no Euler) | — | Exactamente el hueco: todo su RR produce características de Euler (enteras en dim 1), nunca signaturas |
| **S2** (trazas autónomas) | Fórmula explícita de Weil + traza semilocal (teoremas) | La evaluación cohomológica de las trazas |
| **S3** (incondicionalidad) | CC 2021 es incondicional en su ventana | Todo lo demás condicional o numérico |

**[INTERPRETACIÓN] — las tres lecturas operativas para Phase 39:**

1. **El hueco G2 es real y es exactamente donde CC se detienen.** Tienen dualidad
   (apareamiento perfecto $H^1 \times H^0 \to U(1)$) pero ninguna forma bilineal sobre
   un solo espacio con índice de inercia. La interfaz G1↔G2 debería preguntar: ¿qué
   condición sobre una teoría en el cuadrado hace que la dualidad de Pontryagin de la
   diagonal se refine a una forma de intersección con signatura? CC no lo preguntan.
2. **Su diagnóstico del cuadrado es cohomológico, no analítico**: el bloqueo nombrado
   es $H^1$ en Čech idempotente (1805.10501), y su progreso 2022–23 (tolerancia sobre
   $\mathbb S$) lo resuelve en dim 1. Si esa técnica se extiende al cuadrado, G1 se
   movería; G2 seguiría abierto porque ni en dim 1 hay signatura.
3. **La positividad de Weil de 2021 es, según ellos mismos, el germen de la teoría de
   intersección del cuadrado** ("novel geometric landscape still in development for an
   intersection theory of divisors (on the square of the Scaling Site)"). Para el
   programa esto legitima leer $\kappa(Q)$ (índice negativo de la forma de Weil) como
   el invariante que la forma de intersección debería calcular — la identificación
   $\kappa(Q) = $ defecto de índice de Hodge es consistente con su lenguaje, pero es
   nuestra, no de ellos.

---

## §9. Qué NO pude verificar en esta sesión

- Datos bibliográficos de journal de 1502.05580 (¿Adv. Math.?), 1603.03191
  (¿Selecta?), 2205.01391 (la búsqueda apunta a un artículo en ScienceDirect/Bull.
  Sci. Math. pero no leí la página del journal). **[NO VERIFICADO]**.
- 1405.4527 y 1507.05818: solo abstracts en esta sesión (los teoremas finos se
  verificaron en las versiones largas 1502.05580 y 1603.03191).
- El texto completo de 2310.18423 más allá de lo verificado en Doc 100 (Teoremas 1 y 2
  semilocales: medida $dm_S = |\prod_{v\in S} L_v(\frac12 - is)|^2 ds$ y estabilidad
  del espacio de Sonine $\theta_S$). **[VERIFICADO previo — Doc 100]**.
- Si existe alguna continuación publicada de 1805.10501 (RR en el cuadrado, tropical o
  complejo-levantado): búsqueda negativa, que no es prueba de inexistencia.
  **[NO VERIFICADO]**.
- El survey de Consani *On the notion of geometry over $\mathbb F_1$* y entrevistas
  técnicas: no leídos en esta sesión; las declaraciones sobre el cuadrado se
  verificaron en fuentes primarias (1509.05576, 1805.10501, 2006.13771), que son más
  fuertes. **[NO VERIFICADO el survey]**.
- La numeración exacta de algunos teoremas citados (p.ej. "Theorem 5.6/5.12/5.17" de
  1603.03191, "Theorem 6.11" de 2006.13771, "Proposition 4.2" de 2306.00456) proviene
  del texto extraído; el enunciado es fiel pero la numeración debería re-confirmarse
  contra el PDF antes de citarla en un paper. **[VERIFICADO con caveat]**.

---

*Fin del Doc 120.*
