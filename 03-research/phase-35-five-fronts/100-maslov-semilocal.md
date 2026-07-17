# Doc 100 — Índice de Maslov semilocal: el primer paso falsable de $\mathbf{C}_D^B$

**Programa:** Hipótesis de Riemann — Fase 35, Cinco Frentes
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Docs 91, 94, 96, 98; Paper P35; Phase 27 (docs 00–03); literatura Connes–Consani verificada vía web (junio 2026)
**Regla absoluta:** ninguna prueba se fabrica. Cada paso es o bien una demostración, o bien un enunciado de la literatura con referencia verificada, o bien un GAP declarado con precisión. Los enunciados de la literatura que no pudieron verificarse en su fuente se marcan [NO VERIFICADO].

---

## Resumen ejecutivo

El Doc 96 formuló la Conjetura $\mathbf{C}_D$ (índice de Maslov adélico): $\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p = 2\kappa$, con contribuciones locales nulas, como única ruta de la Dirección B no claramente circular. Su obstáculo declarado era que requiere una teoría local de $H_C$ sobre $\mathbb{Q}_p$ que no existe. Este documento explora una alternativa: **no** desarrollar esa teoría local, sino anclar $\mathbf{C}_D^B$ en el único teorema de positividad de Weil incondicional que existe en la literatura — el teorema **semilocal/arquimediano de Connes–Consani** (Selecta Math. 2021) — y en su infraestructura semilocal posterior (Connes–Consani, J. Number Theory 2021; Connes–Consani–Moscovici, Ann. Funct. Anal. 2024).

**Resultados del documento:**

1. (§2) Se enuncia con precisión, verificado contra las fuentes, qué prueba Connes–Consani: positividad de la **forma de Weil completa** restringida al subespacio de funciones de prueba con soporte en $(1/2, 2)$ — subespacio sobre el cual la forma completa **coincide exactamente** con el término arquimediano $W_\infty$, porque el soporte mata todos los términos primos. No es una positividad local truncada: la dicotomía de la pregunta (i) se disuelve por coincidencia exacta en la ventana.

2. (§3) Se define el índice de Maslov semilocal $\mu_S$ rigurosamente como índice negativo de la forma de Weil del programa (Doc 91, Def. 1.2) restringida a la filtración de ventanas $\mathcal{D}_n$, con un lema de agotamiento **demostrado**: $\kappa(Q) = \lim_n \kappa(Q|_{\mathcal{D}_n})$. La interpretación como flujo espectral (cruces de un camino de formas) se da con sus gaps técnicos declarados.

3. (§4) $\mu_{\{\infty\}} = 0$ es un **teorema incondicional** (Yoshida 1992 por cómputo; Connes–Consani 2021 por mecanismo operatorial). La trampa de la pregunta (iii) se responde: como enunciado de índice es trivial dada la positividad; el contenido nuevo es el **mecanismo** (compresión al espacio de Sonine: positividad por construcción + discrepancia compacta), y ese mecanismo tiene contraparte semilocal probada para todo $S$ finito (CCM 2024).

4. (§5) El punto técnico crítico de la propuesta se **verifica y se refuta**: el espacio de funciones de prueba de CC **no se achica** al crecer $S$ — crece (soporte en $[1/n, n]$, $n \to \infty$). La obstrucción real a $S \to$ todos los lugares es otra, y es **nueva** respecto de MW-2/Phase 27: no es la no-factorización del lado de ceros (irrelevante aquí, porque el lado geométrico de la fórmula explícita es aditivo por lugares incondicionalmente), sino la **no-uniformidad en $n$ del control operatorial de la discrepancia Weil−Sonine**, donde la barrera $\sqrt{n}$ vs $\log n$ (Doc 91, Prop. 4.5) reaparece ventana a ventana. Se formula como Obstáculo $\mathbf{O}_{SL}$ con tres componentes.

5. (§6) Consecuencia para $\mathbf{C}_D^B$: la forma **aditiva** de la conjetura ($\mu = \mu_\infty + \sum_p \mu_p$) queda descartada como formulación (el índice no es aditivo y la descomposición local del lado de ceros fue refutada en Phase 27); la forma correcta es por **incrementos de filtración**, y su primer caso ($S = \{\infty\}$) está probado. Queda el primer paso falsable: **Conjetura 100.A** ($\mu_{\{\infty,2\}} = 0$), una desigualdad explícita con un solo término primo, abierta, con toda la infraestructura operatorial ya construida en la literatura.

6. (§7) **VEREDICTO: PARCIAL** — ruta viva en su primer tramo (S pequeño, falsable, con mecanismo no circular probado en el caso base), sin mecanismo conocido para el tramo uniforme $n \to \infty$.

---

## §1. Marco: lo que este documento toma del programa

### 1.1 La forma de Weil y el índice $\kappa$

Del Doc 91 (Defs. 1.1, 1.2, 1.5): para $f, g \in \mathcal{S}(\mathbb{R}^*_+)$, con $\hat f(s) = \int_0^\infty f(x) x^s \, dx/x$ (Mellin), $\tilde g(x) = \overline{g(1/x)}/x$, $(f \star g)(x) = \int_0^\infty f(y) g(x/y)\, dy/y$:

$$Q(f, g) = \mathcal{W}(f \star \tilde g), \qquad Q[f] = \mathcal{Z}[f] - \mathcal{P}[f] + \mathcal{A}[f],$$

donde $\mathcal{Z}$ es la contribución de ceros, $\mathcal{P}$ la prima, $\mathcal{A}$ la arquimediana (Doc 94, §1). El índice negativo es $\kappa(Q) = \sup\{\dim W : Q|_W < 0\}$; el Teorema de Weil (1952) da RH $\iff \kappa(Q) = 0$; bajo la Hipótesis D con $m$ órbitas off-críticas, $\kappa(Q) = 2m$ (P35, Teorema kappa-2m, vía P32–P33).

### 1.2 El estado de la Dirección B

- Doc 91: las condiciones C1–C4, C6, C7 son equivalentes a RH o circulares; C5 (cola prima) es la única no obturada y está en el umbral crítico $a_{\mathrm{tail}} = 1$.
- Doc 94: la brecha $\kappa < \infty \to \kappa = 0$ (Conjetura $\mathbf{C}_B$) no tiene argumento en la literatura.
- Doc 96: Teorema 8.1 — bajo $\kappa < \infty$, el índice negativo está localizado en $\mathcal{K}_{\mathrm{off}}$; Conjetura $\mathbf{C}_D$ (índice de Maslov adélico) con la advertencia explícita de que el punto (iii) ($\mu_p = 0$ local) es el más cuestionable, y de que falta la teoría local de $H_C$ en $\mathbb{Q}_p$.
- Phase 27 (doc 02-C-wall-analysis): **el término primo de $Q$ SÍ factoriza por lugares; el término de ceros NO factoriza** (Proposición 27-C.1, Wall A). Toda descomposición $Q = Q_\infty + \sum_p Q_p$ del lado espectral requiere el sitio aritmético inacabado de Connes–Consani (MW-5).
- Doc 98 (§7): en el modelo de juguete de un cuádruplo off-crítico, el flujo espectral del cruce $\delta: 0 \to \delta_0$ es $-2$ y $|\mu| = 2 = \kappa$, con gaps de regularidad declarados. Es la única instancia computada de la identidad Maslov–Krein del programa.

### 1.3 Los muros relevantes

MW-2 (el producto de Euler vive en $\mathrm{Re}(s) > 1$; los ceros son globales); MW-3 (no hay Hasse–Minkowski en dimensión infinita); MW-5 (la factorización de $Q$ por lugares requiere cohomología aritmética inexistente); MW-4 / barrera $\sqrt{N}$ vs $\log N$ (Doc 91, Prop. 4.5): el término primo crece como $\sqrt{N}$ contra $\log N$ del arquimediano, y la positividad requiere cancelación oscilatoria que es el contenido de RH.

La propuesta de este documento: el marco semilocal de Connes–Consani es **la única región conocida donde MW-4 tiene una excepción probada**, y hay que medir con precisión qué se puede extraer de esa excepción para $\mathbf{C}_D^B$.

---

## §2. El teorema semilocal de Connes–Consani: enunciados verificados

Todo lo que sigue en esta sección fue verificado directamente contra las fuentes (arXiv:2006.13771, texto completo; arXiv:2310.18423 v2, texto completo de la introducción y §4; arXiv:2008.10974, abstract y datos de publicación) en junio de 2026.

### 2.1 El criterio de Weil en la normalización CC

**Fórmula explícita (CC 2021, ec. (1)).** Para una clase precisa de funciones de prueba $f$ sobre $\mathbb{R}^*_+$, con $\tilde f(s) := \int_0^\infty f(x) x^{s-1} dx$:
$$\tilde f(0) - \sum_{\rho \in Z} \tilde f(\rho) + \tilde f(1) = \sum_v \mathcal{W}_v(f),$$
donde $Z$ es el multiconjunto de ceros no triviales de $\zeta$ y la suma derecha recorre los lugares de $\mathbb{Q}$ ($v = \infty, 2, 3, 5, \ldots$). El lado derecho es el **lado geométrico**: $\mathcal{W}_p$ concentra los términos $\log p \cdot p^{-k/2}[f(p^k) + f(p^{-k})]$ y $\mathcal{W}_\infty$ el término del factor gamma (valor principal en $x = 1$).

**Criterio (CC 2021, ec. (2)).** Para **cualquier** conjunto finito $F \subset \mathbb{C}$ con $F \supset \{0, 1\}$ y $F \cap Z = \emptyset$:
$$\mathrm{RH} \iff \sum_v \mathcal{W}_v(g * \tilde g^\sharp) \leq 0 \quad \forall g \in C_c^\infty(\mathbb{R}^*_+) \text{ con } \tilde g(z) = 0 \;\forall z \in F,$$
donde $g^\sharp(x) = x^{-1} g(x^{-1})$, $\bar g(x) = \overline{g(x)}$. Dos observaciones cruciales, ambas textuales en CC:

(a) La condición de anulación en $F$ es legítima **solo si se sabe que $F$ no contiene ceros** ($F \cap Z = \emptyset$). Esto reaparecerá en §5 como componente de la obstrucción.

(b) *"The key point being that the right-hand side of the explicit formula, when evaluated on a test function $f$ with compact support, involves only finitely many primes"* (CC 2021, Introducción). La RH, que es sobre la distribución asintótica de los primos, admite una formulación equivalente que involucra **finitos primos por vez**.

**Lema 2.0 (diccionario de convenciones CC $\leftrightarrow$ programa).** Sea $g \in C_c^\infty(\mathbb{R}^*_+)$ con $\hat g(0) = \hat g(1) = 0$ (Mellin en los polos; en la normalización de Fourier multiplicativa de CC, anulación en $\pm i/2$ tras el corrimiento unitario $\Delta^{1/2}f(x) = x^{1/2}f(x)$). Entonces:
$$Q(g, g) \;=\; \sum_{\rho \in Z} \hat g(\rho)\, \overline{\hat g(1 - \bar\rho)} \;=\; -\sum_v \mathcal{W}_v(g * \tilde g^\sharp).$$

*Demostración.* La transformada de Mellin de $h = g \star \tilde g$ es $\hat h(s) = \hat g(s) \overline{\hat g(1 - \bar s)}$ (Doc 91, Obs. 1.3, con la involución $\tilde g$ del programa, que coincide con $\tilde g^\sharp = \bar g^\sharp$ de CC). La fórmula explícita en la forma CC (ec. (1)) aplicada a $h$ da $\tilde h(0) - \sum_\rho \tilde h(\rho) + \tilde h(1) = \sum_v \mathcal{W}_v(h)$ con $\tilde h(s) = \hat h(s)$ en la traducción de variables; las condiciones $\hat g(0) = \hat g(1) = 0$ anulan $\tilde h(0)$ y $\tilde h(1)$, de donde $\sum_\rho \hat h(\rho) = -\sum_v \mathcal{W}_v(h)$. El lado izquierdo es $\mathcal{Z}[g]$ en la notación del Doc 94, que sobre el subespacio con condiciones de polos coincide con $Q(g,g)$ (la fórmula $Q = \mathcal{Z} - \mathcal{P} + \mathcal{A}$ del Doc 94 es precisamente la fórmula explícita escrita del lado espectral; igualar ambas escrituras de $\mathcal{W}(h)$ produce la identidad). $\square$

En el lugar arquimediano CC escriben $W_\infty := -W_{\mathbb{R}}$, de modo que la desigualdad de Weil toma la forma $W_\infty(f) \geq 0$. **Convención para todo el documento:** usamos $Q \geq 0$ (programa) y traducimos vía el Lema 2.0 sin más comentario. Obsérvese que el lema exhibe ya el rasgo que explota toda la estrategia: bajo las condiciones de polos, $Q(g,g)$ — un objeto espectral (suma sobre ceros) — es **igual** a menos el lado geométrico, que es una suma de términos locales explícitos. La positividad se puede atacar enteramente del lado geométrico, donde la aditividad por lugares es un hecho trivial y no un problema abierto (contraste con Phase 27, §5.3).

### 2.2 El marco semilocal y la propiedad $P(n)$

**Marco semilocal (Connes 1999, Selecta Math. 5; CCM 2024, §4).** Para $S$ finito de lugares con $\infty \in S$: el anillo de adeles semilocales es $\mathbb{A}_S = \prod_{v \in S} \mathbb{Q}_v$; el espacio de clases de adeles semilocal es $X_S = \mathbb{A}_S / \Gamma$, con $\Gamma = \{\pm p_1^{n_1} \cdots p_k^{n_k} : p_j \in S \setminus \{\infty\}, n_j \in \mathbb{Z}\} \subset \mathrm{GL}_1(\mathbb{A}_S)$; el grupo de clases de ideles semilocal $C_S = \mathrm{GL}_1(\mathbb{A}_S)/\Gamma$ actúa sobre $X_S$. La fórmula de trazas semilocal de Connes (1999) — que es un **teorema**, a diferencia de la global, que es equivalente a RH — calcula la traza de la acción de escala sobre $L^2(X_S)$ con cutoff y produce exactamente $\sum_{v \in S} \mathcal{W}_v$.

**La propiedad $P(n)$ (CCM 2024, Introducción, textual).** *"There exists a property $P(n)$, involving only the Euler factors for primes smaller than $n$, and whose validity for all $n$ is equivalent to RH. This is derived from Weil's positivity criterion which involves the quadratic form $Q_n$ defined using the Riemann–Weil explicit formula applied to test functions with support in the compact symmetric interval $[\frac{1}{n}, n]$."*

Es decir: la restricción de soporte $\mathrm{supp}(f) \subset [1/n, n]$ anula $f(p^k)$ y $f(p^{-k})$ para todo $p^k > n$, de modo que el lado geométrico **completo** evaluado en $f$ coincide con el lado geométrico **semilocal** $\sum_{v \in S(n)} \mathcal{W}_v(f)$, donde $S(n) = \{\infty\} \cup \{p : p \leq n\}$ (solo entran las potencias $p^k \leq n$; CCM escriben "primes smaller than $n$"). En CC 2021 (Introducción) la misma condición se escribe $\mathrm{Supp}(f) \subset (p^{-1}, p)$ para el conjunto de lugares $\{\infty, 2, 3, \ldots, p\}$.

### 2.3 El teorema arquimediano (el caso base, probado)

**Desigualdad de Weil arquimediana (enunciado en CC 2021, p. 2; probado por Yoshida 1992).** *Para toda $f$ suave, definida positiva, con soporte en el intervalo $(1/2, 2)$ y cuya transformada de Fourier (multiplicativa) se anula en $\pm i/2$, se tiene $W_\infty(f) \geq 0$, donde $W_\infty := -W_{\mathbb{R}}$.*

CC atribuyen la primera prueba a H. Yoshida (*On Hermitian forms attached to zeta functions*, Adv. Stud. Pure Math. 21 (1992), 281–325), "reduciéndola a un cómputo explícito". La anulación en $\pm i/2$ de la transformada de Fourier multiplicativa corresponde, en Mellin, a la anulación en los polos $s = 0, 1$; como $\zeta(s) \neq 0$ en $s = 0, 1$ dentro de la clase relevante, la condición es admisible en el criterio (2).

**Teorema 1 de CC 2021 (textual, traducido).** *Sea $g \in C_c^\infty(\mathbb{R}^*_+)$ con soporte en $[2^{-1/2}, 2^{1/2}]$ y transformada de Fourier anulándose en $i/2$ y en $0$. Entonces:*
$$W_\infty(g * g^*) \geq \mathrm{Tr}(\vartheta(g)\, \mathbf{S}\, \vartheta(g)^*) \geq 0,$$
*donde $\vartheta$ es la acción de escala de $\mathbb{R}^*_+$ en $L^2(\mathbb{R})^{\mathrm{ev}}$ y $\mathbf{S}$ es la proyección ortogonal sobre el complemento del rango de $\mathcal{P}_1 \vee \widehat{\mathcal{P}}_1$ (proyecciones de cutoff en espacio de fase, parámetro $\Lambda = 1$): el espacio de **Sonine** (funciones pares que, junto con su transformada de Fourier, se anulan idénticamente en $[-1, 1]$; Sonin 1880, Burnol 2002, de Branges).*

**Teorema 6.11 de CC 2021.** Existe una constante finita $c$, con $13 < c < 17$, tal que para toda $g \in C_c^\infty([2^{-1/2}, 2^{1/2}])$ con $\hat g(i/2) = 0$:
$$W_\infty(g * g^*) \geq \mathrm{Tr}(\vartheta(g)\, \mathbf{S}\, \vartheta(g)^*) - c\, |\hat g(0)|^2.$$

**Corolario 2 de CC 2021.** $c|\hat g(0)|^2 + \sum_{s \in Z} \hat g(s) \overline{\hat g(\bar s)} \geq \mathrm{Tr}(\vartheta(g) \mathbf{S} \vartheta(g)^*)$; en palabras de CC, la traza de Sonine requiere, además de los ceros de $\zeta$, una contribución adicional (irrelevante para RH) sobre la línea crítica entre los dos primeros ceros $\sim 1/2 \pm 14.1347 i$, *"como si se multiplicara $\zeta(z)$ por $(z - 1/2)^{17}$"*.

**Teorema 3 de CC 2021 (la discrepancia es un infinitesimal).** Para toda $f \in C_c^\infty(\mathbb{R}^*_+)$:
$$\mathrm{Tr}(\vartheta(f)\mathbf{S}) = W_\infty(f) + \int f(\rho)\, \epsilon(\rho)\, d^*\rho,$$
con $\epsilon(\rho) = \sum_n \frac{\lambda(n)}{\sqrt{1 - \lambda(n)^2}} \langle \xi_n \mid \vartheta(\rho^{-1}) \zeta_n \rangle$ expresada en funciones esferoidales prolatas ($\lambda(n)$ los autovalores prolatos). El operador asociado a la discrepancia Weil−Sonine es **compacto** (un infinitesimal del cálculo cuantizado).

**Esqueleto de la prueba CC (verificado en la Introducción y §§1–6 de la fuente; se registra porque es el molde que un ataque a 100.A debe replicar):**

1. *Geometrización (CC §1).* La fórmula local arquimediana se escribe $W_\infty(f) = -\frac12 \mathrm{Tr}(\hat f\, u^* \,\textit{đ}u)$, con $u = u_\infty$ el unitario de la transformada de Fourier compuesta con la inversión (multiplicación por $e^{2i\theta(s)}$, $\theta$ la función angular de Riemann–Siegel) y $\textit{đ}u$ su diferencial cuantizado. El núcleo de Schwartz de la acción de escala se descompone en dos "cuadrados" $\Delta$ (pequeño) y $\Sigma$ (grande) del primer cuadrante.
2. *Aislamiento de la obstrucción (CC §2).* La obstrucción a la positividad local es exactamente la contribución del cuadrado pequeño $\Delta$; se aísla en la función "trace-remainder" $\delta(\rho)$, dada explícitamente por $\delta(\rho) = 2\rho^{1/2}\big(\frac{\mathrm{Si}(2\pi(1+\rho))}{2\pi(1+\rho)} + \frac{\mathrm{Si}(2\pi(\rho-1))}{2\pi(\rho-1)}\big)$ para $\rho \geq 1$, y el funcional $L(f) = D(f) + W_\infty(f)$ con $D(f) = \int f(\rho^{-1})\delta(\rho) d^*\rho$ resulta **positivo sin restricción de soporte** (CC, Prop. 2.2). Toda la dificultad queda empaquetada en la negatividad esencial de $D$.
3. *Condiciones de polos (CC §3).* Imponer $\hat f(\pm i/2) = 0$ equivale a reemplazar $\delta$ por $Q\delta$ con $Q = -(\rho\partial_\rho)^2 + \frac14$; el salto de $\delta'$ en $\rho = 1$ genera $-2\,\underline{\delta}_1$ y el operador asociado a $D \circ Q$ en $L^2(\sqrt I, d^*\rho)$ se descompone como $-2\,\mathrm{Id} + K$ con $K$ compacto de clase Hilbert–Schmidt: $D$ es esencialmente negativo en soporte compacto fijo, módulo finitas condiciones lineales.
4. *Compresión de Sonine (CC §4).* La identidad $\delta(\rho) = \mathrm{Tr}(\vartheta_m(\rho^{-1}) \widehat{\mathcal{P}}_1 \mathcal{P}_1)$ liga el cuadrado $\Delta$ con el par de proyecciones de cutoff; la descomposición en componentes irreducibles de la representación del grupo diedral infinito $\mathbb{Z} \rtimes \mathbb{Z}/2$ generado por $(\mathcal{P}_1, \widehat{\mathcal{P}}_1)$ "muda" $\Delta$ dentro de $\Sigma$, dejando como resto exactamente el espacio de Sonine (donde la representación es trivial) — de ahí el Teorema 3.
5. *Control Toeplitz (CC §§5–6).* El funcional $E \circ Q$ asociado a $\epsilon(\rho)$ se descompone como $-2\epsilon'(1^+)(\mathrm{Id} - K)$ con $K$ compacto; en la ventana $I = [1/2, 2]$ se discretiza $\mathbb{R}^*_+$ por $q^{\mathbb{Z}}$, $q \to 1^+$, se identifica $K_q$ como matriz de Toeplitz, se constata que tiene **un único autovalor $> 1$**, y se condiciona en esa única dirección (más cercanas) para obtener $\mathrm{Id} - K > 0$ — de ahí el Teorema 6.11 con $13 < c < 17$. CC señalan que el paso $q \to 1^+$ está alineado con la filosofía $\mathbb{F}_q \to \mathbb{F}_1$ y con la técnica de Toeplitz usada para RH sobre cuerpos de funciones (Hallouin–Perret 2019).

El paso 5 es el **único** paso de la prueba que es específico de la ventana $[1/2, 2]$ y que no tiene hoy análogo para ventanas mayores; los pasos 1–4 tienen contraparte semilocal probada o estructuralmente disponible (§2.5).

### 2.4 Respuesta a la pregunta (i): ¿forma completa restringida o forma local truncada?

**Proposición 2.1 (coincidencia exacta en la ventana).** Sea $f$ con $\mathrm{supp}(f) \subset (1/2, 2)$. Entonces el lado geométrico completo y el truncado al lugar $\infty$ coinciden término a término:
$$\sum_v \mathcal{W}_v(f) = \mathcal{W}_\infty(f),$$
porque $f(p^{\pm k}) = 0$ para todo primo $p$ y todo $k \geq 1$ (la menor potencia de primo es $2 \notin (1/2,2)$... más precisamente $2 \geq 2 > \sup \mathrm{supp}(f)$ cuando el soporte es el intervalo abierto $(1/2,2)$). $\square$

**Consecuencia.** La dicotomía de la pregunta (i) — "¿positividad de la forma de Weil COMPLETA restringida a un subespacio, o positividad de una forma LOCAL truncada?" — **se disuelve**: en la ventana $(1/2, 2)$ ambas cosas son la misma. El Teorema 1 de CC es, simultáneamente:

- positividad de la **forma de Weil completa** $Q$ del programa restringida al subespacio $\{g : \mathrm{supp}\, g \subset [2^{-1/2}, 2^{1/2}],\ \hat g(\text{polos}) = 0\}$ — un enunciado RH-relevante genuino (es el caso $n = 2$ de la familia $P(n)$ cuya totalidad equivale a RH), y
- positividad del término local arquimediano $W_\infty$ sobre ese subespacio.

Esto es exactamente lo que lo hace valioso para $\mathbf{C}_D^B$: es una positividad **incondicional de la forma global** en un subespacio no trivial, con un **mecanismo** (no un cómputo accidental): la positividad es la traza de un operador positivo por construcción ($\vartheta(g)\mathbf{S}\vartheta(g)^* \geq 0$), y todo lo que separa $Q$ de esa traza es un infinitesimal compacto más un defecto de rango finito acotado ($c < 17$) en una dirección certificadamente no-cero ($s = 1/2$; $\zeta(1/2) \neq 0$).

### 2.5 La infraestructura semilocal posterior (verificada)

**(a) Funciones cuasi-internas (CC, *Quasi-inner functions and local factors*, J. Number Theory 226 (2021), 139–167; arXiv:2008.10974).** El producto de cocientes de factores locales sobre un conjunto finito de lugares de $\mathbb{Q}$ (incluido $\infty$) es una función **cuasi-interna** a la izquierda de la línea crítica; la parte fuera de diagonal de la multiplicación por tal función, en la descomposición $L^2(\text{línea crítica}) = H^2 \oplus (H^2)^\perp$, es un operador **compacto**. CC presentan esto explícitamente como *"los prerrequisitos analíticos para tratar la positividad de Weil en el caso semilocal"*.

**(b) Estabilidad del espacio de Sonine semilocal (CCM, *Zeta zeros and prolate wave operators*, Ann. Funct. Anal. 15 (2024); arXiv:2310.18423).**

- *Teorema 1 (CCM §4):* para $S$ finito con $\infty \in S$, la transformada canónica identifica $L^2(X_S)^{K_S}$ con $L^2(\mathbb{R}, dm_S)$, donde la medida es $dm_S(s) = \big|\prod_{v \in S} L_v(\tfrac12 - is)\big|^2 ds$ ($L_v$ los factores locales de Euler); el diccionario con el lugar arquimediano es la multiplicación por $\prod_{p \in S \setminus \{\infty\}} L_p(\tfrac12 - is)$.
- *Teorema 2 (CCM §4, textual, traducido):* *"Sea $S$ finito con $\infty \in S$ y $\lambda > 0$. Entonces el mapa $\theta_S$ induce un isomorfismo hilbertiano de los espacios de Sonine $\theta_S : \mathbf{S}_\lambda(\mathbb{R}, e_\infty) \to \mathbf{S}_\lambda(X_S, \alpha)$."* Es decir: el reservorio de positividad (el espacio de Sonine) **es estable bajo el crecimiento de $S$** — no se degenera ni se vacía al añadir lugares finitos.
- *Estado de la positividad semilocal en CCM 2024 (textual, traducido):* *"Esperamos que el uso de tales herramientas operatoriales en el caso semilocal abra un camino para tratar la positividad de Weil como en [CC 2021]. De hecho, el aspecto operatorial del presente trabajo provee una estrategia más precisa para abordar la positividad de Weil semilocal, comparando el funcional de traza asociado al operador — automáticamente positivo para un operador autoadjunto — con el funcional de Weil."* — Es decir: para $|S| \geq 2$ la positividad es **estrategia declarada, no teorema**.

**(c) [NO VERIFICADO].** No se encontró, en las búsquedas realizadas (junio 2026), ninguna publicación de Connes–Consani(–Moscovici) ni de terceros que pruebe $P(n)$ para algún $n > 2$ (esto es, la positividad semilocal con al menos un lugar finito). Tampoco pudo verificarse si el cómputo de Yoshida (1992) cubre ventanas mayores que $(1/2, 2)$. Ambos puntos se tratan como abiertos.

---

## §3. El índice de Maslov semilocal $\mu_S$: definición rigurosa

### 3.1 La filtración de ventanas

**Definición 3.1 (ventanas y subespacios admisibles).** Para $n \geq 2$ real:
$$\mathcal{D}_n := \{g \in C_c^\infty(\mathbb{R}^*_+) : \mathrm{supp}(g) \subset [n^{-1/2}, n^{1/2}]\}, \qquad \mathcal{D}_n^0 := \{g \in \mathcal{D}_n : \hat g(0) = \hat g(1) = 0\},$$
donde $\hat g$ es la transformada de Mellin y las condiciones $\hat g(0) = \hat g(1) = 0$ son las anulaciones en los polos requeridas por el criterio de Weil (en la normalización CC: anulación de la transformada de Fourier multiplicativa en $\pm i/2$). Nótese que $g \in \mathcal{D}_n \Rightarrow \mathrm{supp}(g \star \tilde g) \subset [1/n, n]$.

**Lema 3.2 (contenido aritmético finito de la ventana).** Para $g \in \mathcal{D}_n$, la forma de Weil del programa satisface:
$$Q(g, g) = \mathcal{Z}[g] - \sum_{p^k \leq n} \frac{\log p}{p^{k/2}} \big[(g \star \tilde g)(p^k) + (g \star \tilde g)(p^{-k})\big] + \mathcal{A}[g],$$
es decir, el término primo solo involucra las potencias de primos $p^k \leq n$. En particular, sobre $\mathcal{D}_n^0$, $Q$ coincide con $-\sum_{v \in S(n)} \mathcal{W}_v(g * \tilde g^\sharp)$, donde $S(n) = \{\infty\} \cup \{p : p \leq n\}$.

*Demostración.* Inmediata del soporte: $(g \star \tilde g)(x) = 0$ para $x \notin [1/n, n]$, y las potencias de primos en $[1/n, n]$ son exactamente $\{p^{\pm k} : p^k \leq n\}$. La identificación con el lado geométrico semilocal es la fórmula explícita con los términos de polos anulados por las condiciones de $\mathcal{D}_n^0$. $\square$

**Definición 3.3 (forma semilocal e índice de Maslov semilocal).** El parámetro primario es la ventana $n$, no el conjunto de lugares (porque distintas $n$ con el mismo conjunto de primos visibles dan formas distintas — ver Obs. 3.6). Definimos
$$Q_n := Q\big|_{\mathcal{D}_n^0}, \qquad \boxed{\mu(n) := \kappa(Q_n) = \sup\{\dim W : W \subset \mathcal{D}_n^0,\ Q|_W < 0\}}.$$
Para $S$ finito de lugares con $\infty \in S$ de la forma $S = S(n)$, escribimos $\mu_S := \mu(q_S^-) = \sup\{\mu(n) : S(n) = S\}$, donde $q_S$ es la menor potencia de primo cuyo primo no pertenece a $S$ o que excede la ventana correspondiente; $\mu_S$ es notación de conveniencia para "el índice justo antes de que entre el siguiente dato aritmético".

**Lema 3.4 (monotonía y agotamiento).** La función $n \mapsto \mu(n)$ es monótona no decreciente, y
$$\kappa\big(Q|_{\{g \in C_c^\infty:\ \hat g(0) = \hat g(1) = 0\}}\big) = \lim_{n \to \infty} \mu(n) = \sup_n \mu(n).$$

*Demostración.* Monotonía: $\mathcal{D}_n^0 \subset \mathcal{D}_{n'}^0$ para $n \leq n'$, y el índice negativo de una restricción no supera el de la forma ambiente. Agotamiento: si $W \subset C_c^\infty$ es un subespacio de dimensión finita $k$ con $Q|_W < 0$ y las condiciones de polos, tómese una base $g_1, \ldots, g_k$; la unión de sus soportes es compacta en $\mathbb{R}^*_+$, luego contenida en $[n^{-1/2}, n^{1/2}]$ para algún $n$ finito; entonces $W \subset \mathcal{D}_n^0$ y $\mu(n) \geq k$. Recíprocamente cada $\mu(n) \leq \kappa$. $\square$

**Observación 3.5 (el índice con y sin condiciones de polos).** El índice del programa $\kappa(Q)$ se define sobre $\mathcal{S}(\mathbb{R}^*_+)$ sin condiciones (Doc 91, Def. 1.5). Si $W$ es negativo de dimensión $k$ sin condiciones, $W \cap \{\hat g(0) = \hat g(1) = 0\}$ es negativo de dimensión $\geq k - 2$. Por tanto el índice con condiciones difiere del de $\kappa(Q)$ en a lo sumo 2, y bajo la Hipótesis D ambos detectan los mismos ceros off-críticos: la cadena RH $\iff \kappa(Q) = 0 \iff \mu(n) = 0\ \forall n$ es válida (la última equivalencia es el Lema 3.4 más el criterio (2) de CC, que está formulado exactamente sobre el subespacio con condiciones). En particular:

$$\boxed{\mathrm{RH} \iff \mu(n) = 0 \text{ para todo } n \geq 2 \iff \text{la familia } P(n) \text{ de CCM vale para todo } n.}$$

**Observación 3.6 (densificación dentro de un mismo $S$).** Entre dos potencias de primos consecutivas, $\mu(n)$ puede en principio crecer (el dominio crece y el término arquimediano ve la ventana mayor) sin que entren nuevos primos. La filtración fina es por $n$ continuo; la indexación por $S$ es la lectura "por lugares". Esto ya muestra que la aritmética de la filtración no es puramente "un primo por paso": las potencias $4 = 2^2, 8 = 2^3, 9 = 3^2, \ldots$ refinan los pasos del mismo lugar.

### 3.2 Lectura como flujo espectral (camino de formas y cruces)

**Construcción 3.7 (el camino de formas en espacio fijo).** Sea $V_\tau$, $\tau \geq 1$, el reescalamiento de Mellin $(V_\tau g)(x) := g(x^{1/\tau})$, que satisface $\widehat{V_\tau g}(s) = \tau\, \hat g(\tau s)$ y mapea $\mathcal{D}_2 \to \mathcal{D}_{2^\tau}$ biyectivamente. El pullback $Q^{(\tau)} := Q(V_\tau \cdot, V_\tau \cdot)$ es un camino de formas hermitianas sobre el espacio fijo $\mathcal{D}_2$, con $\kappa(Q^{(\tau)}) = \mu(2^\tau)$ módulo el ajuste de las condiciones de polos (la anulación $\hat g(1) = 0$ no es $V_\tau$-invariante: $\widehat{V_\tau g}(1) = \tau \hat g(\tau)$; las dos condiciones se transportan a dos condiciones lineales que se mueven con $\tau$). El **índice de Maslov semilocal como flujo espectral** es el conteo neto de cruces por cero de los autovalores de los operadores de forma asociados a $Q^{(\tau)}$ a lo largo de $\tau \in [1, T]$, en el sentido de Robbin–Salamon (*The Maslov index for paths*, Topology 32 (1993), 827–844), aplicado a la realificación simpléctica de la Construcción 3.4 del Doc 96.

**Definición 3.7-bis (forma de cruce, sentido Robbin–Salamon).** Si $\tau_0$ es un instante con $N_{\tau_0} := \ker Q^{(\tau_0)} \neq 0$ (cruce), la **forma de cruce** es la forma hermitiana sobre $N_{\tau_0}$:
$$\Gamma(\tau_0)[u] := \frac{d}{d\tau}\Big|_{\tau = \tau_0} Q^{(\tau)}(u, u), \qquad u \in N_{\tau_0}.$$
El cruce es **regular** si $\Gamma(\tau_0)$ es no-degenerada, y su contribución al índice de Maslov del camino es $\mathrm{sign}\,\Gamma(\tau_0)$ (Robbin–Salamon 1993, Teorema 2.3 en el caso de dimensión finita). En nuestro contexto, la derivada $\frac{d}{d\tau} Q^{(\tau)}(u,u)$ tiene una expresión concreta: derivar la ventana produce (i) el término de borde arquimediano (derivada del valor principal de $\mathcal{W}_\infty$ contra la dilatación, computable del factor gamma) y (ii) términos de Dirac aritméticos $-\frac{\log p}{p^{k/2}}\big[\delta(\text{entrada de } p^k)\big]$ cada vez que una potencia de primo cruza el borde $x = n^{\pm 1}$ de la ventana: **la derivada del camino de formas es exactamente la entrada secuencial de los datos aritméticos**. Esta es la versión precisa, dentro del programa, de la intuición del Doc 96 (Obs. 3.11) de que el índice de Maslov "podría descomponerse por lugares": no se descompone el índice — se descompone la *derivada del camino*.

**GAP 3.8 (declarado).** La Construcción 3.7 requiere, para ser un flujo espectral genuino: (a) una completación hilbertiana de referencia de $\mathcal{D}_2$ en la que cada $Q^{(\tau)}$ sea representable por un operador autoadjunto acotado (o de forma relativamente acotada) — el candidato natural es $L^2(\sqrt{I}, d^*\rho)$ usado por CC en su análisis Toeplitz, pero la representabilidad de la parte $\mathcal{Z}$ no está establecida; (b) regularidad del camino $\tau \mapsto Q^{(\tau)}$ (continuidad en norma de las formas; los términos de Dirac de 3.7-bis la rompen en los instantes aritméticos, donde habría que trabajar con saltos regularizados); (c) no-degeneración de las formas de cruce. Ninguno de los tres puntos está establecido en general en el programa; en el modelo de juguete del Doc 98 (§7), (a)–(c) se verificaron a mano para el cruce del cuádruplo y el flujo resultó $= -2 = -\kappa$. **Para este documento, la definición operativa de $\mu(n)$ es la de la Definición 3.3 (índice de la restricción), que es incondicionalmente rigurosa; la lectura de flujo espectral es interpretativa hasta que se cierre el GAP 3.8.**

**Tabla 3.9 (los primeros pasos de la filtración).** Orden de entrada de los datos aritméticos en la ventana $[1/n, n]$:

| rango de $n$ | potencias visibles | $S(n)$ | peso del término entrante |
|---|---|---|---|
| $[1, 2)$ | ninguna | $\{\infty\}$ | — (ventana puramente arquimediana) |
| $[2, 3)$ | $2$ | $\{\infty, 2\}$ | $\log 2 / \sqrt{2}$ |
| $[3, 4)$ | $2, 3$ | $\{\infty, 2, 3\}$ | $\log 3 / \sqrt{3}$ |
| $[4, 5)$ | $2, 3, 4$ | $\{\infty, 2, 3\}$ | $\log 2 / 2$ (potencia $2^2$, mismo lugar) |
| $[5, 7)$ | $2, 3, 4, 5$ | $\{\infty, 2, 3, 5\}$ | $\log 5 / \sqrt{5}$ |
| $[7, 8)$ | $\ldots, 7$ | $\{\infty, 2, 3, 5, 7\}$ | $\log 7 / \sqrt{7}$ |
| $[8, 9)$ | $\ldots, 8$ | ídem | $\log 2 / 2\sqrt{2}$ (potencia $2^3$) |

$\mu(2) = 0$ es el Teorema 4.1; todo lo demás de la columna izquierda hacia abajo es territorio abierto. La fila $[2,3)$ es la Conjetura 100.A (§6.2).

**Observación 3.10 (dónde cruza un cero off-crítico).** Si $\rho_0 = 1/2 + b + i\gamma$ es un cero off-crítico, el Lema 3.4 garantiza que existe un umbral finito $n(\rho_0) := \min\{n : \mu(n) \geq 1\} < \infty$: la dirección negativa asociada a $\rho_0$ (Doc 91, Prop. 1.6) **entra en la filtración a escala finita**. La estructura Maslov localiza así la negación de RH en eventos de cruce a escala finita. No se conoce ninguna cota efectiva superior de $n(\rho_0)$ en términos de $(b, \gamma)$; la formulamos como pregunta:

**Pregunta 100.Q1 (umbral de cruce efectivo).** ¿Existe una función explícita $N(b, \gamma)$ tal que todo cero off-crítico $\rho = 1/2 + b + i\gamma$ fuerza $\mu(N(b,\gamma)) \geq 1$? Una respuesta afirmativa haría de cada $P(n)$ probado una **región de exclusión efectiva** para ceros off-críticos (análoga a las verificaciones numéricas de altura $T$, pero en la variable conjugada). Estado: abierta; ni siquiera se conoce la forma cualitativa de $N$.

---

## §4. ¿La positividad de CC implica $\mu_S = 0$? (pregunta iii)

### 4.1 El caso base: teorema

**Teorema 4.1 ($\mu_{\{\infty\}} = 0$, incondicional).** $\mu(n) = 0$ para todo $n \leq 2$. Es decir: la forma de Weil completa del programa es semidefinida positiva sobre $\mathcal{D}_2^0$.

*Demostración.* Sea $g \in \mathcal{D}_2^0$. Por el Lema 3.2 con $n = 2$ y soporte en el abierto: si $\mathrm{supp}(g) \subset (2^{-1/2}, 2^{1/2})$, entonces $\mathrm{supp}(g \star \tilde g) \subset (1/2, 2)$ y no hay términos primos; $Q(g,g) = -\mathcal{W}_\infty(g * \tilde g^\sharp) = W_\infty(g * g^*) \geq 0$ por la desigualdad de Weil arquimediana (Yoshida 1992; enunciado verificado en CC 2021, p. 2, con las condiciones de anulación en $\pm i/2$ que son exactamente las de $\mathcal{D}_2^0$). El caso de soporte en el cerrado se obtiene por aproximación (las evaluaciones $f(2), f(1/2)$ en el borde se controlan por continuidad con funciones de corte; los puntos de borde tienen contribución límite nula para aproximaciones internas). Si existiera $W \subset \mathcal{D}_2^0$ con $Q|_W < 0$, cualquier $g \in W \setminus \{0\}$ violaría lo anterior. $\square$

**Observación 4.2 (qué prueba el mecanismo de CC y qué prueba Yoshida).** La prueba de Yoshida es un cómputo explícito; cubre $\mathcal{D}_2^0$ completo. La prueba operatorial de CC (Teorema 1) requiere además $\hat g(1/2) = 0$ (anulación de Fourier en $0$, es decir Mellin en el centro $s = 1/2$); sin esa condición, su Teorema 6.11 deja el defecto $-c|\hat g(0)|^2$ con $13 < c < 17$. Por el argumento de codimensión (como en Obs. 3.5), el mecanismo CC por sí solo da $\mu(2) \leq 1$; combinado con Yoshida, $\mu(2) = 0$. El punto $s = 1/2$ es certificadamente no-cero ($\zeta(1/2) \neq 0$, valor conocido), así que el condicionamiento es legítimo en el criterio (2).

### 4.2 La trampa de la pregunta (iii), respondida

**Sí, $\mu_{\{\infty\}} = 0$ se sigue trivialmente de la positividad** (un subespacio donde la forma es $\geq 0$ tiene índice negativo $0$; no hay contenido lógico adicional). El contenido no trivial está en otra parte, y conviene separarlo con precisión:

**(a) Contenido del teorema mismo.** $P(2)$ es el primer eslabón de una familia cuya totalidad es RH. Un eslabón solo no acota ningún cero (un cero off-crítico de parte imaginaria enorme tiene umbral de cruce $n(\rho_0)$ presumiblemente enorme). Valor directo para $\kappa$: nulo. Esto hay que decirlo sin eufemismos.

**(b) Contenido del mecanismo (lo que importa para $\mathbf{C}_D^B$).** La identidad estructural de CC:
$$Q_n(g,g) = \underbrace{\mathrm{Tr}(\vartheta(g)\, \mathbf{S}\, \vartheta(g)^*)}_{\geq\, 0 \text{ por construcción}} + \underbrace{\big(\text{discrepancia}\big)}_{\text{infinitesimal compacto} + \text{rango finito condicionable}}$$
realiza la positividad como **traza de la acción de escala comprimida al espacio de Sonine** — un objeto definido sin referencia alguna a los ceros de $\zeta$. Esto es exactamente el tipo de "mecanismo de anulación local con chance de propagarse" que pedía la pregunta (iii), por tres razones verificadas:

1. La compresión de Sonine existe **para todo $S$ finito** y es estable: CCM 2024, Teorema 2 ($\theta_S$ isomorfismo hilbertiano de espacios de Sonine). El reservorio de positividad no se agota al añadir lugares.
2. El diccionario espectral semilocal es canónico: la medida $dm_S = |\prod_{v \in S} L_v(\tfrac12 - is)|^2 ds$ (CCM 2024, Teorema 1) — los factores de Euler de $S$ entran como **peso espectral**, no como producto infinito; MW-2 no se invoca.
3. Los prerrequisitos analíticos de compacidad para $|S| \geq 2$ están probados: las funciones cuasi-internas de CC (JNT 2021) dan que la obstrucción off-diagonal de los factores locales es compacta — el análogo semilocal de "la discrepancia es un infinitesimal".

**(c) Lo que el mecanismo NO da todavía.** La pieza que en el caso $S = \{\infty\}$ cierra la prueba — el control Toeplitz cuantitativo de la discrepancia, con su defecto de rango finito $c < 17$ y su única dirección de condicionamiento — **no tiene análogo probado para ningún $S$ con un lugar finito** [NO VERIFICADO que exista a junio 2026; CCM 2024 lo declara estrategia]. La positividad por construcción de la traza comprimida es gratuita en todo $S$; la afirmación con contenido es que *Weil $\geq$ Sonine módulo condicionamiento finito legítimo*, y eso solo está probado en la ventana $(1/2, 2)$.

### 4.3 El mecanismo CC frente al Obstáculo $\mathbf{O}_D$ (Doc 96, §8.1)

El Obstáculo $\mathbf{O}_D$ afirma: toda condición sobre $H_C$ que implique $\kappa = 0$ requiere información sobre las posiciones de los ceros, no derivable de ecuación funcional + producto de Euler + crecimiento. ¿Cómo convive esto con el Teorema 4.1, que prueba una positividad genuina de $Q$ sin información alguna sobre ceros?

**Análisis.** No hay contradicción, y la frontera exacta es instructiva:

1. El Teorema 4.1 no implica $\kappa = 0$: implica $\mu(2) = 0$, y $\kappa = \sup_n \mu(n)$ (Lema 3.4). $\mathbf{O}_D$ prohíbe la conclusión global, no la ventanal. La excepción CC delimita el alcance de $\mathbf{O}_D$ **desde adentro**: la frontera del obstáculo no pasa entre "propiedades globales" y "posiciones de ceros", como sugería la formulación del Doc 96, sino entre **ventanas sin masa prima** ($n \leq 2$: positividad demostrable por análisis puro) y **ventanas con masa prima** ($n > 2$: cada paso requiere cancelación aritmética). Esta reformulación de $\mathbf{O}_D$ es estrictamente más precisa que la del Doc 96 y debería sustituirla en el mapa de muros del programa.

2. Los insumos del mecanismo CC son: análisis armónico en $L^2(\mathbb{R})^{\mathrm{ev}}$, el par de proyecciones de cutoff, las funciones prolatas (Slepian–Pollak), teoría de Toeplitz, y la **no-anulación certificada de $\zeta$ en un punto** ($s = 1/2$). Ninguno toca posiciones de ceros. Pero el output también respeta escrupulosamente el límite de $\mathbf{O}_D$: el Corolario 2 de CC dice que la traza de Sonine exige, además de los ceros, una contribución extra en la línea crítica ("como multiplicar $\zeta$ por $(z - 1/2)^{17}$") — el mecanismo "ve" los ceros solo como familia de evaluaciones $\sum_{s \in Z} |\hat g(s)|^2$, nunca individualmente.

3. Hay un punto genuinamente nuevo respecto del diagnóstico del Doc 96 (Conclusiones, ítem sobre el producto de Euler): el Lema 2.8 del Doc 96 mostró que la positividad **no** se sigue de la ausencia de ceros en la región de Euler (subespacio $\mathcal{H}_{>1}$, soporte espectral en $\mathrm{Re}(s) > 1$). El Teorema 4.1 muestra que sí se sigue en el subespacio dual (soporte **físico** en la ventana $(1/2,2)$, sin restricción espectral). La asimetría es exacta: localizar en la variable de Mellin (Doc 96, Ángulo 2) no controla el término primo, que es una suma de evaluaciones físicas; localizar en la variable física (CC) lo aniquila. La lección retrospectiva para el programa: el Ángulo 2 del Doc 96 eligió el lado equivocado de la transformada.

**Conclusión de §4.** La positividad CC implica $\mu_{\{\infty\}} = 0$ (trivialmente, Teorema 4.1); el contenido nuevo para el programa no es ese índice nulo sino (a) la **descomposición traza-positiva + infinitesimal**, disponible como esqueleto probado en todo nivel $S$ de la filtración y a la que solo le falta el estimador cuantitativo por nivel, y (b) la **redelimitación del Obstáculo $\mathbf{O}_D$** (§4.3, punto 1): la frontera del obstáculo es la masa prima de la ventana, no la dicotomía global/local. La pregunta del programa pasa a ser: ¿el estimador es uniformizable en $n$? Esa es la obstrucción de §5.

---

## §5. La obstrucción exacta a $S \to$ todos los lugares (pregunta iv)

### 5.1 Verificación del punto técnico crítico: el espacio de test functions NO se achica

La propuesta de esta exploración conjeturaba que "el espacio de test functions de CC se achica al crecer $S$" como posible obstrucción. **La verificación da lo contrario.** Textualmente:

- CC 2021 (Introducción): la positividad semilocal se busca *"para funciones $f$ que cumplen la condición de soporte $\mathrm{Supp}(f) \subset (p^{-1}, p)$"* para el conjunto de lugares $\{\infty, 2, 3, \ldots, p\}$: el soporte permitido **crece** con $S$.
- CCM 2024 (Introducción): $Q_n$ se define sobre funciones *"con soporte en el intervalo compacto simétrico $[\frac1n, n]$"*, y RH equivale a la validez de $P(n)$ **para todo** $n$: la filtración es creciente y agota $C_c^\infty(\mathbb{R}^*_+)$ (nuestro Lema 3.4).

La dirección del enunciado es la opuesta a la temida, y es la buena: si el espacio se achicara, la familia de positividades semilocales no podría equivaler a RH. Queda refutada esa versión del obstáculo. La obstrucción real tiene otra estructura, que formulamos ahora.

### 5.2 El obstáculo $\mathbf{O}_{SL}$

**Obstáculo $\mathbf{O}_{SL}$ (tres componentes).** La extensión del teorema CC de $S = \{\infty\}$ a la familia completa $\{P(n) : n \geq 2\}$ enfrenta exactamente lo siguiente:

**$\mathbf{O}_{SL}$.1 (carga prima creciente en la ventana — MW-4 por ventanas).** Sobre $\mathcal{D}_n^0$, la forma es $Q_n = \mathcal{A}_n - \mathcal{P}_n$ (sin término $\mathcal{Z}$ del lado geométrico). El tamaño bruto del término primo en la ventana se cuantifica:

**Lema 5.0 (masa prima de la ventana).** $\displaystyle M(n) := \sum_{p^k \leq n} \frac{\log p}{p^{k/2}} = (2 + o(1))\sqrt{n}, \qquad n \to \infty.$

*Demostración.* $M(n) = \sum_{m \leq n} \Lambda(m) m^{-1/2}$ con $\Lambda$ la función de von Mangoldt. Por suma parcial con $\psi(x) = \sum_{m \leq x} \Lambda(m)$:
$$M(n) = \frac{\psi(n)}{\sqrt n} + \frac{1}{2}\int_2^n \frac{\psi(t)}{t^{3/2}}\, dt,$$
y el teorema de los números primos $\psi(t) = (1 + o(1))t$ (de hecho basta Chebyshev para el orden) da $M(n) = (1 + o(1))\sqrt n + (1 + o(1))\int_2^n \tfrac{dt}{2\sqrt t} \cdot \ldots = (1+o(1))\sqrt n + (1 + o(1))(\sqrt n - \sqrt 2) = (2 + o(1))\sqrt n$. $\square$

Contra esto, el término arquimediano sobre la misma ventana crece como $\log n$ (el peso $\Omega(s) \sim \frac12 \log |s|$ del Doc 91, Prop. 4.4, integrado contra funciones de banda $\sim \log n$). La positividad de $Q_n$ para $n$ grande requiere por tanto que la cancelación oscilatoria de los signos de $(g \star \tilde g)(p^k)$ reduzca la contribución prima efectiva de $\sqrt n$ a $O(\log n)$ — que es el contenido aritmético de RH en la ventana. **El marco semilocal no disuelve la barrera $\sqrt{N}$ vs $\log N$ (Doc 91, Prop. 4.5): la rebana.** Cada $P(n)$ es un enunciado con datos aritméticos finitos (los $p^k \leq n$) más el lugar arquimediano; la barrera completa reaparece como divergencia del desbalance al recorrer la familia. Lo que cambia — y no es poco — es el tipo lógico del problema: de una positividad global única a una sucesión numerable de positividades, cada una con contenido aritmético finito. En el caso base $n = 2$ se tiene $M(2) = \log 2/\sqrt 2$ pero la ventana abierta lo excluye: $M(2^-) = 0$ — la positividad probada por CC vive en la única ventana con masa prima **exactamente nula**. Esta observación es la semilla del escenario pesimista del §6.2.

**$\mathbf{O}_{SL}$.2 (no-uniformidad del control de la discrepancia — el corazón del obstáculo).** El esquema de prueba CC en cada nivel es: $Q_n = T_n + R_n$, con $T_n = \mathrm{Tr}(\vartheta(g)\mathbf{S}_n \vartheta(g)^*) \geq 0$ canónico (y $\mathbf{S}_n$ estable en $n$, CCM Teorema 2) y $R_n$ la discrepancia. En $n = 2$, $R_n$ se controló con: (i) compacidad (Teorema 3 CC), (ii) análisis Toeplitz en el límite $q \to 1^+$, (iii) un defecto de rango finito con constante $13 < c < 17$ y **una** dirección de condicionamiento. No existe (a junio 2026) el análogo de (ii)–(iii) para ningún $n > 2$, y no existe ningún principio que controle el crecimiento en $n$ de:
$$c(n) := \text{defecto óptimo de rango finito}, \qquad d(n) := \text{número de direcciones de condicionamiento necesarias}.$$
Si $d(n)$ crece sin control (por ejemplo, proporcionalmente al número de ceros "visibles" en la resolución $\log n$ de la ventana, que crece como $e^{c\sqrt{\cdot}}$... no hay siquiera una conjetura cuantitativa en la literatura), el método produce positividad solo en subespacios de codimensión creciente, lo cual **no** implica $\mu(n) = 0$ sino solo $\mu(n) \leq d(n)$ — una cota que no tiende a $0$. La comparación honesta: $\mu(n) \leq d(n)$ con $d(n) \to \infty$ tendría exactamente el mismo estatus que C5/$a_{\mathrm{tail}}$ del Doc 91: estructura correcta, constante en el umbral inútil.

**$\mathbf{O}_{SL}$.3 (legitimidad aritmética del condicionamiento).** El criterio (2) de CC solo permite imponer anulaciones $\hat g|_F = 0$ con $F \cap Z = \emptyset$: cada dirección de condicionamiento debe estar certificada como **no-cero de $\zeta$**. En $n = 2$ la dirección es $s = 1/2$ y $\zeta(1/2) \neq 0$ es un hecho verificado. Para $n$ general, las direcciones de condicionamiento las dicta el espectro del operador Toeplitz límite — un dato analítico no elegido por el demostrador — y no hay garantía a priori de que correspondan a puntos certificables. Ahora bien, este componente es **estructuralmente más débil** que los muros del programa: la no-anulación de $\zeta$ en un punto dado fuera de los ceros es verificable (es una desigualdad estricta en un valor concreto, decidible numéricamente con error riguroso), a diferencia de la información "posiciones de todos los ceros" que bloquea las rutas C1–C4 (Doc 91). $\mathbf{O}_{SL}$.3 introduce una dependencia de verificaciones puntuales finitas por nivel — molesta, no fatal.

**Enunciado sintético del obstáculo.** *La estrategia semilocal reduce RH a la familia numerable $\{P(n)\}$ con $P(2)$ probado. El mecanismo de Sonine provee en cada nivel una descomposición con parte positiva canónica estable (CCM 2024) y discrepancia compacta (CC JNT 2021), pero el control cuantitativo de la discrepancia — el único paso donde se decide la positividad — está probado solo en $n = 2$, no se conoce para ningún $n > 2$, y no existe mecanismo de uniformidad en $n$; la parte de la discrepancia que crece con $n$ es exactamente el término primo de amplitud $\sqrt{n}$ contra $\log n$ del arquimediano. La obstrucción es de tipo cuantitativo-uniforme (una sucesión de constantes por controlar), no de tipo estructural-algebraico (no falta ningún objeto).*

### 5.3 ¿Es la misma obstrucción que MW-2 / Phase 27? No — y la diferencia es informativa

**Proposición 5.1 (la obstrucción semilocal es disjunta de la de Phase 27).** La obstrucción de Phase 27 (Proposición 27-C.1, Wall A) es: el término de **ceros** $\mathcal{Z}[f] = \sum_\rho \hat f(\rho)$ no admite descomposición $\sum_v \mathcal{Z}_v$ por lugares; la factorización de $Q$ del lado espectral requiere la cohomología aritmética inexistente (MW-5). La estrategia semilocal **no descompone jamás el lado de ceros**: trabaja exclusivamente con el lado geométrico de la fórmula explícita, que es aditivo por lugares **incondicionalmente** (es una suma $\sum_v \mathcal{W}_v$ término a término — el mismo hecho que Phase 27 registró como "el término primo SÍ factoriza"), y localiza por **soporte de la función de prueba**, no por factorización del funcional. En consecuencia:

- MW-2 (producto de Euler solo en $\mathrm{Re}(s) > 1$) no se invoca: los factores de Euler de $S$ entran como datos algebraicos finitos (el peso $|\prod_{v \in S} L_v|^2$ sobre la línea crítica, CCM Teorema 1), sin producto infinito ni continuación.
- MW-3 (no Hasse–Minkowski infinito-dimensional) no se invoca: no hay paso local-a-global de positividades; hay **exhaución** (Lema 3.4): la positividad global es el supremo de las positividades en ventanas, no su producto.
- MW-5 no se invoca: ninguna factorización de $Q$ se postula.

El precio de evitar los tres muros es $\mathbf{O}_{SL}$.1–2: la uniformidad en la ventana. $\square$ (la proposición es un cotejo de definiciones; su contenido es la tabla siguiente)

| | Phase 27 (factorización) | Semilocal (filtración) |
|---|---|---|
| Objeto descompuesto | $Q$ entera (lado espectral) | dominio de $Q$ (ventanas de soporte) |
| Qué factoriza | requiere $\mathcal{Z} = \sum_v \mathcal{Z}_v$: **FALSO** (27-C.1) | lado geométrico $\sum_v \mathcal{W}_v$: **trivialmente cierto** |
| Paso crítico | local $\Rightarrow$ global (MW-3/MW-5) | uniformidad en $n$ de constantes ($\mathbf{O}_{SL}$.2) |
| Estado del caso base | sin caso base | $P(2)$ **probado** (Yoshida/CC) |
| Tipo de obstrucción | estructural (falta el objeto) | cuantitativa (faltan las cotas) |

**Observación 5.2 (lo que esto enseña sobre $\mathbf{C}_D$).** El Doc 96 (Conjetura $\mathbf{C}_D$, evaluación honesta) señalaba como punto más cuestionable el (iii): "la no-nulidad del factor local no implica que la contribución local al índice de Maslov sea cero". El análisis semilocal lo confirma y lo precisa: no existe "contribución local al índice" porque el índice no es aditivo por lugares (la negatividad de $Q_n$ es un fenómeno de interferencia entre el arquimediano y **todos** los primos de la ventana a la vez). Lo que sí existe, y es el sustituto correcto, son los **incrementos de filtración** $\mu(n') - \mu(n) \geq 0$.

---

## §6. Consecuencias para $\mathbf{C}_D^B$ y el enunciado intermedio falsable (pregunta v)

### 6.1 Reformulación de $\mathbf{C}_D^B$: de suma local a filtración

**Lo que el caso semilocal refuta de la formulación original.** $\mathbf{C}_D$ (Doc 96, §8.2) postulaba $\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p$ con $\mu_p = 0$ por la no-anulación del factor local. Esa aditividad presupone una descomposición por lugares del objeto cuyo índice se mide, es decir, la factorización que Phase 27 refutó para el lado de ceros. En la única realización rigurosa disponible (la semilocal), el índice **no se descompone**: se filtra.

**Lo que el caso semilocal confirma del patrón.** El patrón "contribuciones locales nulas" sobrevive en forma de incrementos: RH $\iff$ todos los incrementos de la filtración son nulos, y el **incremento basal** (de la ventana vacía a la ventana $(1/2,2)$, puramente arquimediana) **es nulo por teorema**. Es la primera componente de $\mathbf{C}_D^B$ que pasa de conjetura a teorema, en la formulación corregida:

**Conjetura $\mathbf{C}_D^{SL}$ (reformulación filtrada de $\mathbf{C}_D^B$).** Para todo $n \geq 2$: $\mu(n) = 0$. Equivalentemente (Lema 3.4 + criterio CC): RH. Estructura fina: $\mu(2) = 0$ [**TEOREMA** — Teorema 4.1]; para cada potencia de primo $q$, el incremento al pasar la ventana por $q$ es nulo [ABIERTO para todo $q \geq 2$].

Nótese la honestidad de la equivalencia: $\mathbf{C}_D^{SL}$ **es** RH, no un enunciado más débil. Su valor no es lógico sino estructural: aísla el primer incremento no probado como enunciado autónomo con todos los objetos definidos y un mecanismo de prueba candidato (el de CC) cuya infraestructura semilocal ya existe.

### 6.2 El primer paso falsable

**Conjetura 100.A ($\mu_{\{\infty, 2\}} = 0$; el caso $P(n)$, $2 < n \leq 3$).** Para toda $g \in C_c^\infty(\mathbb{R}^*_+)$ con $\mathrm{supp}(g) \subset (3^{-1/2}, 3^{1/2})$ y $\hat g(0) = \hat g(1) = 0$ (Mellin en los polos), se tiene
$$W_\infty(g * g^*) \;\geq\; \frac{\log 2}{\sqrt{2}} \Big[ (g \star \tilde g)(2) + (g \star \tilde g)(1/2) \Big],$$
es decir $Q(g, g) \geq 0$, donde el lado derecho es el **único** término primo visible en la ventana $(1/3, 3)$ (la única potencia de primo en $(1, 3)$ es $2$; nótese $4 = 2^2 > 3$ y $3 \notin (1/3,3)$ abierto). Versión condicionada admisible (estilo CC): la misma desigualdad módulo anulaciones adicionales $\hat g|_{F'} = 0$ con $F'$ finito explícito de puntos certificados no-ceros de $\zeta$.

**Estado.** Abierta. [NO VERIFICADO que exista prueba publicada a junio 2026; CCM 2024 declara la positividad semilocal como estrategia.] Es el enunciado falsable más pequeño que distingue la ruta semilocal de una repetición del caso arquimediano:

- Si es **verdadera y demostrable con el mecanismo CC** (compresión de Sonine en $L^2(X_{\{\infty,2\}})$, medida $|L_2 L_\infty|^2 ds$, discrepancia compacta vía cuasi-internas, control Toeplitz con defecto finito): el patrón de $\mathbf{C}_D^{SL}$ queda confirmado en el primer incremento con contenido aritmético genuino (un primo real interfiriendo con el arquimediano), y la pregunta se desplaza a la uniformidad ($\mathbf{O}_{SL}$.2) con un dato nuevo: el comportamiento de $c(n), d(n)$ en el primer paso.
- Si es **falsa**: $\zeta$ tiene un cero off-crítico con umbral de cruce $n(\rho) \leq 3$ — RH es falsa, con violación detectable en la ventana $(1/3, 3)$. (Nadie espera esto; el punto es que la conjetura tiene contenido empírico inmediato.)
- Si es **verdadera pero el mecanismo CC no la alcanza** (por ejemplo, si el defecto de condicionamiento explota ya con un primo): se aprende que la excepción arquimediana a MW-4 era un fenómeno de ventana sin primos — es decir, que la positividad probada por CC vivía precisamente del hecho de que en $(1/2,2)$ **no hay aritmética** — y la ruta semilocal hacia $\mathbf{C}_D^B$ queda severamente degradada. Este es el escenario que el programa debe poder detectar: la Conjetura 100.A es el experimento que lo decide.

**Observación 6.1 (qué NO se puede hacer con numéricos en este programa).** La regla del documento excluye exploración numérica; pero se registra que el escenario tercero es en principio decidible por métodos operatoriales puros: el análogo del operador $K$ de CC §6 en la ventana $(1/3,3)$ es un objeto Toeplitz concreto cuya norma decide el asunto. Su análisis es el contenido técnico del "primer paso".

**Programa 100.B (ataque a la Conjetura 100.A por el molde CC; pasos con sus incógnitas).** Siguiendo el esqueleto del §2.3 con $S = \{\infty, 2\}$:

- **(B1) Marco.** $X_S = (\mathbb{R} \times \mathbb{Q}_2)/2^{\mathbb{Z}}$ (con $\Gamma = \{\pm 2^k\}$), $L^2(X_S)^{K_S} \cong L^2(\mathbb{R}, dm_S)$ con $dm_S(s) = |L_2(\tfrac12 - is)|^2\, |L_\infty(\tfrac12 - is)|^2\, ds$, $L_2(z) = (1 - 2^{-z})^{-1}$, $L_\infty(z) = \pi^{-z/2}\Gamma(z/2)$ (CCM 2024, Teorema 1). *Probado.*
- **(B2) Reservorio.** Espacio de Sonine semilocal $\mathbf{S}_\lambda(X_S, \alpha) \cong \mathbf{S}_\lambda(\mathbb{R}, e_\infty)$ (CCM 2024, Teorema 2): la compresión $\mathrm{Tr}(\vartheta_S(g)\, \mathbf{S}_S\, \vartheta_S(g)^*) \geq 0$ existe y es positiva por construcción. *Probado.*
- **(B3) Discrepancia.** Definir $\epsilon_S(\rho)$ por la identidad $\mathrm{Tr}(\vartheta_S(f)\mathbf{S}_S) = (W_\infty + W_2)(f) + \int f \epsilon_S\, d^*\rho$ y probar que el operador asociado es compacto. Insumo disponible: la cuasi-internidad de $L_2 \cdot L_\infty$-cocientes con obstrucción off-diagonal compacta (CC JNT 2021). *Estructuralmente disponible; la identidad de traza semilocal análoga al Teorema 3 de CC no está escrita en la literatura.* GAP.
- **(B4) Polos y salto.** Análogo de $Q\delta$: el peso $|L_2|^2$ es suave y periódico en $s$ (período $2\pi/\log 2$); el salto en $\rho = 1$ del término arquimediano debería persistir y los nuevos saltos aritméticos aparecen en $\rho = 2^{\pm 1}$ — exactamente los puntos donde la Tabla 3.9 registra la entrada del dato $\log 2/\sqrt 2$. *No escrito; es un cálculo de valor principal concreto.* GAP.
- **(B5) Toeplitz en $(1/3, 3)$.** El análogo de $K_q$ adquiere, además del símbolo arquimediano, un término de rango estructural proveniente de $W_2$ (un coseno en la variable $s \log 2$, por la periodicidad del factor local). Preguntas decisivas: ¿cuántos autovalores $> 1$? ¿las direcciones de condicionamiento corresponden a puntos certificables no-ceros? *Completamente abierto; es la incógnita $d(3)$ del Obstáculo $\mathbf{O}_{SL}$.2.* GAP central.

El Programa 100.B no es una prueba ni un esbozo de prueba: es la lista exhaustiva de lo que falta, con la separación probado / disponible / GAP. Si (B3)–(B5) se cierran, la Conjetura 100.A queda probada y el patrón de $\mathbf{C}_D^{SL}$ confirmado en su primer incremento aritmético. Si (B5) se cierra en negativo (proliferación de direcciones no certificables), el escenario tercero del §6.2 queda establecido.

### 6.3 Subproductos para las otras piezas de la Dirección B

**(a) Para el Teorema 8.1 del Doc 96 (localización del índice en $\mathcal{K}_{\mathrm{off}}$).** La filtración $\mu(n)$ es compatible con la descomposición $\mathcal{K} = \mathcal{K}_{\mathrm{crit}} \oplus_Q \mathcal{K}_{\mathrm{off}}$: bajo Hipótesis D, las direcciones negativas viven en $\mathcal{K}_{\mathrm{off}}$ (dimensión $2m$) y cada una tiene umbral de entrada finito en la filtración (Obs. 3.10). El par (Teorema 8.1, Lema 3.4) da: $\kappa = \lim \mu(n)$ con todos los cruces producidos por $\mathcal{K}_{\mathrm{off}}$ — la imagen Maslov del Doc 96 (Conjetura 3.10) se realiza parcialmente: no como identidad conjetural $\mu = 2\kappa$ de una familia de lagrangianos $\{L_\theta\}$, sino como identidad **probada** de una filtración de índices (Lema 3.4), que es más pobre (no es un invariante topológico de camino cerrado) pero incondicional.

**(b) Para V.1 (P35).** En el marco semilocal de CCM la acción de escala es unitaria en $L^2(X_S)$ y la fórmula de trazas semilocal es un teorema: la patología de V.1 (¿$Q(U_\lambda f, U_\lambda g) = Q(f,g)$?) no aparece **dentro de una ventana fija** porque allí $Q$ se computa por la fórmula explícita contra el lado geométrico semilocal, y la acción de escala mueve la ventana ($U_\lambda \mathcal{D}_n \neq \mathcal{D}_n$). Esto sugiere que la versión correcta de V.1 es *filtrada*: invarianza de la familia $\{Q_n\}$ bajo el reescalamiento $V_\tau$ de la Construcción 3.7, no invarianza de cada $Q_n$ bajo $U_\lambda$. No se desarrolla aquí; se registra como dirección para el cierre de V.1.

**(c) Para C5/$a_{\mathrm{tail}}$ (Docs 91, 94).** La filtración semilocal y la cola prima son duales: C5 corta los primos **grandes** de la forma global; la ventana semilocal corta los primos grandes **por soporte**. La diferencia decisiva: la ventana corta exactamente (Lema 3.2: contribución nula, no pequeña), por eso el caso base semilocal es un teorema mientras que C5 quedó en el umbral $a_{\mathrm{tail}} = 1$. El costo se paga en el otro extremo: C5 intentaba un solo enunciado global; la filtración necesita infinitos enunciados.

**(d) Para la Propuesta 7.2 del Doc 96 (torsión por factores locales).** El Doc 96 (§7.2) propuso estudiar los cocientes de factores locales $\Theta_p(z) = (1 - p^{-1/2 - z})/(1 - p^{-1/2 + z})$, observó que $|\Theta_p(it)| = 1$ en la línea pero que $|\Theta_p(\sigma + it)|$ no es trivial para $\sigma \neq 0$, y dejó el cálculo inconcluso (Lema 7.3, marcado "el cálculo se complica"). La verificación de la literatura cierra ese hilo: el objeto correcto es exactamente el que CC estudian en *Quasi-inner functions and local factors* (JNT 2021) — los productos $\prod_{v \in S} L_v$-cocientes son **cuasi-internos a la izquierda de la línea crítica**, y la parte que les falta para ser internos (la obstrucción a la contractividad estricta que el Doc 96 buscaba para la disipatividad del Ángulo 1) es un **operador compacto**. Es decir: la torsión por factores locales no produce disipatividad (Doc 96, Corolario 1.13, sigue en pie) pero sí produce *compacidad de la discrepancia*, que es precisamente el insumo que el mecanismo semilocal necesita. La Propuesta 7.2 del Doc 96 queda así absorbida — con mejora — por la ruta de este documento.

**(e) Sobre la observación final del Doc 96 (Obs. 7.4).** El Doc 96 observó que $|\Theta| = 1$ global es "un resultado de cancelación entre los factores locales, no una propiedad de cada factor". El marco semilocal da la versión cuantitativa correcta de esa intuición: en la medida $dm_S = |\prod_{v \in S} L_v(\tfrac12 - is)|^2 ds$ de CCM, los factores locales entran como peso del espacio de Hilbert, y al crecer $S$ el peso converge (formalmente) a $|\zeta_{\text{completa}}|^2$ sobre la línea — la cancelación global es el límite de pesos semilocales bien definidos. Ninguna afirmación de convergencia se usa en este documento (el límite es exactamente lo que está fuera de alcance, $\mathbf{O}_{SL}$.2); se registra la coherencia estructural.

---

## §7. VEREDICTO

**PARCIAL.**

**Razón precisa, en cuatro cláusulas:**

1. **Lo probado (vivo).** El primer eslabón de la ruta es un teorema incondicional ajeno al programa y verificado en fuente: la forma de Weil completa es positiva en la ventana $(1/2, 2)$ ($\mu_{\{\infty\}} = 0$; Yoshida 1992, mecanismo Connes–Consani, Selecta Math. 2021), y constituye la única excepción probada al patrón MW-4 que conoce el programa. La infraestructura para los eslabones siguientes existe y está probada: estabilidad del espacio de Sonine semilocal para todo $S$ finito (CCM, Ann. Funct. Anal. 2024, Teorema 2), diccionario espectral con peso $|\prod_{v\in S} L_v|^2$ (ibid., Teorema 1), compacidad de la obstrucción de los factores locales (CC, J. Number Theory 2021). La reformulación filtrada $\mathbf{C}_D^{SL}$ corrige la formulación aditiva del Doc 96 (insostenible tras Phase 27) y deja un primer paso falsable, autónomo y bien planteado: la Conjetura 100.A ($\mu_{\{\infty,2\}} = 0$, un solo término primo contra el arquimediano).

2. **Lo refutado.** El punto técnico temido — que el espacio de funciones de prueba se achique al crecer $S$ — es falso: el soporte permitido crece como $[1/n, n]$ y agota todo $C_c^\infty$ (verificado textualmente en CC 2021 y CCM 2024; Lema 3.4 de este documento). También queda descartada la lectura aditiva "$\mu = \mu_\infty + \sum_p \mu_p$ con $\mu_p$ locales": el índice no es aditivo por lugares y no necesita serlo.

3. **Lo abierto (la obstrucción nueva).** La extensión $S \to$ todos los lugares falla hoy en $\mathbf{O}_{SL}$: ningún $P(n)$ con $n > 2$ está probado, y no existe mecanismo de uniformidad en $n$ para el control cuantitativo de la discrepancia Weil−Sonine (defecto $c(n)$, condicionamiento $d(n)$), donde la barrera $\sqrt{n}$ vs $\log n$ del programa reaparece rebanada por ventanas. Es una obstrucción **cuantitativa** (faltan cotas), no **estructural** (no falta ningún objeto), y es disjunta de MW-2/MW-3/MW-5 y de la no-factorización de Phase 27 (Proposición 5.1). Que sea cuantitativa no la hace menor: tiene exactamente la forma de las obstrucciones en las que el programa ya encalló una vez (C5, umbral $a_{\mathrm{tail}} = 1$).

4. **Por qué PARCIAL y no RUTA VIVA ni RUTA CERRADA.** No es RUTA CERRADA: el caso base está probado con un mecanismo no circular, el primer paso nuevo (100.A) es falsable con objetos ya construidos, y ninguna de las tres componentes de $\mathbf{O}_{SL}$ es un teorema de imposibilidad. No es RUTA VIVA plena: la ruta completa exige infinitos eslabones con constantes no uniformizadas, el eslabón $n > 2$ más simple lleva abierto desde 2020 en manos de los propios autores del mecanismo, y si la positividad arquimediana resultara depender esencialmente de la ausencia de aritmética en la ventana basal (escenario tercero de §6.2), el aporte de la excepción CC a $\mathbf{C}_D^B$ se reduciría a cero. La decisión entre estos dos destinos está concentrada en un único enunciado: la Conjetura 100.A. Hasta que se resuelva, el estado honesto es PARCIAL.

**Acción siguiente propuesta para el programa:** atacar la Conjetura 100.A por el esquema CC: (i) escribir la compresión de Sonine en $L^2(X_{\{\infty,2\}})$ con la medida $|L_2(\tfrac12 - is)|^2 |\Gamma_{\mathbb{R}}|^2 ds$; (ii) identificar el operador de discrepancia y su parte Toeplitz en la ventana $(1/3,3)$; (iii) determinar si el defecto de condicionamiento permanece finito y en puntos certificables. Cualquiera de los tres pasos que falle, falla informativamente.

---

## Apéndice A — Procedencia de las verificaciones (junio 2026)

Para cumplir la regla de citas del programa, se registra qué se verificó y cómo:

1. **arXiv:2006.13771** (CC, *Weil positivity and trace formula, the archimedean place*): PDF completo descargado y leído en sus páginas 1–8 (abstract, introducción, Teorema 1, Corolario 2, Teorema 3, esquema de §§1–6) y 55–57 (bibliografía completa). Los enunciados citados en §2.3 son transcripciones directas. La publicación en Selecta Math. (N.S.) 27 (2021) se verificó contra la página de Springer (DOI s00029-021-00689-4).
2. **arXiv:2310.18423 v2** (CCM, *Zeta zeros and prolate wave operators*): PDF completo descargado y leído en sus páginas 1–6 (abstract, introducción completa, enunciados de los Teoremas 1 y 2 del §4, definición de $X_S$, $\Gamma$, $dm_S$). Las citas textuales del §2.2 y §2.5(b) provienen de esas páginas. Publicación en Ann. Funct. Anal. 15 (2024) verificada por búsqueda.
3. **arXiv:2008.10974** (CC, *Quasi-inner functions and local factors*): verificado por abstract y datos de publicación (J. Number Theory 226 (2021), 139–167). El enunciado fino de sus teoremas internos **no** fue leído en fuente; el uso que se hace aquí (compacidad off-diagonal, "prerrequisitos analíticos para la positividad semilocal") se limita a lo afirmado en el abstract y en la página de publicaciones del autor. Cualquier uso más fino en trabajos futuros del programa exige lectura directa.
4. **Yoshida 1992**: citado a través de CC 2021 (referencia [34] de su bibliografía, verificada en la página 57 del PDF: Adv. Stud. Pure Math. 21, 281–325). La fuente primaria no fue consultada; el alcance exacto del cómputo de Yoshida (¿solo $(1/2,2)$ o ventanas mayores?) queda [NO VERIFICADO].
5. **Búsquedas negativas**: búsquedas web (junio 2026) por pruebas de positividad semilocal con lugares finitos ($P(n)$, $n > 2$) no arrojaron ninguna publicación. Una búsqueda negativa no es una prueba de inexistencia; el estado "abierto" de 100.A es la mejor información disponible, no un hecho establecido.
6. **Connes 1999** (Selecta Math. 5, fórmula de trazas semilocal): no releído en fuente para este documento; se usa a través de su recepción en CC 2021/CCM 2024, que lo citan como [11]/[7] respectivamente y reconstruyen el marco semilocal completo en los pasajes leídos.

---

## Referencias

**Literatura externa (verificada en fuente, junio 2026):**

- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952), 252–265.
- N. Y. Sonin, *Recherches sur les fonctions cylindriques et le développement des fonctions continues en séries*, Math. Ann. 16 (1880), 1–80.
- H. Yoshida, *On Hermitian forms attached to zeta functions*, en: Zeta Functions in Geometry (Tokyo, 1990), Adv. Stud. Pure Math. 21, Kinokuniya, Tokyo (1992), 281–325. [Citado en CC 2021 como la primera prueba de la desigualdad arquimediana en la ventana $(1/2,2)$.]
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. [Fórmula de trazas semilocal: teorema.]
- J.-F. Burnol, *Sur les espaces de Sonine associés par de Branges à la transformation de Fourier*, C. R. Acad. Sci. Paris, Ser. I 335 (2002), 689–692.
- A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Math. (N.S.) 27 (2021), art. 77; arXiv:2006.13771. [Teorema 1, Teorema 6.11, Corolario 2, Teorema 3, criterio (2), condición de soporte semilocal: verificados textualmente.]
- A. Connes, C. Consani, *Quasi-inner functions and local factors*, J. Number Theory 226 (2021), 139–167; arXiv:2008.10974. [Compacidad off-diagonal de productos de cocientes de factores locales sobre $S$ finito.]
- A. Connes, C. Consani, *Spectral triples and ζ-cycles*, arXiv:2106.01715. [Contexto; no usado en pasos críticos.]
- A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators*, Ann. Funct. Anal. 15 (2024), art. 70; arXiv:2310.18423 (v2, mayo 2024). [Propiedad $P(n)$; marco $X_S$; Teorema 1 (medida $dm_S$); Teorema 2 (estabilidad del Sonine semilocal); estado de la positividad semilocal como estrategia: verificados textualmente.]
- J. Robbin, D. Salamon, *The Maslov index for paths*, Topology 32 (1993), 827–844.
- M. G. Kreĭn, H. Langer; T. Ya. Azizov, I. S. Iokhvidov: como en Doc 91, Apéndice A.

**Documentos del programa:**

- Doc 91 — Espacio de Pontryagin $(\mathcal{K}, Q)$, índice $\kappa$, condiciones C1–C7, barrera $\sqrt{N}$ vs $\log N$ (Prop. 4.5).
- Doc 94 — Condición C5, cola prima, Conjetura $\mathbf{C}_B$.
- Doc 96 — Ángulo 3 (Maslov), Teorema 8.1 (localización en $\mathcal{K}_{\mathrm{off}}$), Conjetura $\mathbf{C}_D$, Obstáculo $\mathbf{O}_D$.
- Doc 98 — Test de juguete: flujo espectral $= -2 = -\kappa$ para un cuádruplo off-crítico (§7).
- Phase 27, docs 00–03 — Proposición 27-C.1: el término primo factoriza, el término de ceros no.
- Paper P35 — Bridge theorem $\kappa(Q) = \mathrm{neg.ind}(H_C)$, programa V.1–V.4, Hipótesis D.

---

*Fin del Doc 100. Estado: análisis completo del frente semilocal. Caso base probado (externo), primer paso falsable formulado (Conjetura 100.A), obstáculo $\mathbf{O}_{SL}$ nombrado con tres componentes. Veredicto: PARCIAL.*
