# Doc 125 — Construcción de la forma de intersección sobre el cuadrado del sitio de escala

**Programa:** Hipótesis de Riemann — Phase 41: CONSTRUIR G2.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 80 (Castelnuovo–Severi aritmético: por qué la traza de Jacobi y Markov–Stieltjes no dan la forma; la forma $Q$ semidefinida no distingue medidas); Doc 119 (R-SIG realizaciones (i)/(ii)/(iii); R-LEF; R-PESO; el test R-NC, cláusulas NC1–NC4); Doc 123 (bifurcación C-cok/C-rank; el juguete $C_p\times C_p$; los null elements; C-rank = la norma/número de intersección que falta = G2); Doc 124 (G2 = índice de Hodge sobre el cuadrado, signatura INDEFINIDA $(1,\rho-1)$; la positividad de CC es DEFINIDA, categoría distinta; el ingrediente no existe en el corpus CC).

**Disciplina de etiquetado (regla absoluta, máximo riesgo de falsa victoria):** cada enunciado lleva **[DATO]** (en fuente/probado, con cita exacta), **[CONSTRUCCIÓN]** (objeto que diseño yo — con su estatus: qué asume, qué quedaría por verificar), **[CÁLCULO]** (derivación mía mostrada paso a paso), **[GAP]**, **[CONJETURA]**, **[NO VERIFICADO]**. NUNCA "probado" salvo lo genuinamente probado. El objetivo NO es declarar G2 construido — es construir todo lo construible, computar el juguete honestamente, y aislar el núcleo. **Si la construcción se traba, el punto de traba ES el resultado.**

---

## 0. Resumen ejecutivo

Este documento intenta construir $G_2$, la forma de intersección sobre el cuadrado $X\times X$ del sitio de escala, siguiendo exactamente el template de Weil (índice de Hodge sobre $C\times C$ da RH para curvas). El método: fijar el mecanismo clásico con precisión quirúrgica (§1), definir el cuadrado tropical y sus clases distinguidas (§2), proponer y comparar tres vías para el número de intersección (§3), computar las relaciones de intersección estándar (§4), y —el deliverable central— calcular **explícitamente** la matriz de Gram sobre $\langle f_1,f_2,\Delta\rangle$ en el juguete $C_p\times C_p$ (§5).

**Resultados, sin adorno:**

1. **Vía que funciona para el número de intersección (§3):** la intersección estable de Allermann–Rau / Mikhalkin (fan displacement) **[DATO]** está bien definida sobre el toro tropical $C_p\times C_p$ y da un apareamiento $D\cdot D'$ **simétrico, bilineal sobre $\mathbb{R}$**. Las vías (b) grado del RR y (c) traza del flujo coinciden con ella donde se solapan **[CÁLCULO]**, pero la coincidencia con (c) **es exactamente la fórmula de Lefschetz** y por eso es el punto donde el test R-NC muerde (§6).

2. **El número es REAL, no entero (§3.4, §5.4):** sobre las clases relevantes —las correspondencias del flujo $F_\mu$ con $\mu\notin p^{\mathbb{Q}}$— el grado del 0-ciclo de intersección es genéricamente **real**, no entero. Hay una **sub-red entera** (las correspondencias con $\mu\in p^{\mathbb{Z}}$, las "Frobenius enteras") donde el número es entero; pero esa sub-red es **numerablemente delgada** en el espacio de correspondencias y NO contiene el generador del flujo. **El C-rank de Doc 123 sigue real. NO resuelto.**

3. **La matriz de Gram en $C_p\times C_p$ (§5):** sobre $\langle f_1,f_2,\Delta\rangle$ con las relaciones de §4 reproduce
$$ G=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}\quad(\text{escalada por }(\log p)\text{; con }\Delta^2=2-2g=0\text{ para }g=1). $$
Su signatura es $(1,2)$ **[CÁLCULO]** — es decir $(1,\rho_{\text{toy}}-1)$ con $\rho_{\text{toy}}=3$: **la signatura del índice de Hodge SÍ aparece en el juguete.** Sobre el primitivo (ortogonal al plano amplio $\langle f_1+f_2\rangle$) la forma es **definida negativa** — índice de Hodge OK en este subespacio finito. Esto es alentador y es la pieza más fuerte del documento.

4. **PERO (§5.5):** al añadir una correspondencia $F_\mu$ genérica, la red de clases deja de ser de rango finito (las pendientes en $H_p$ son densas en $\mathbb{R}$, Doc 123 §4.2) y el control de signatura del caso finito **no sobrevive el paso a rango infinito** — es la tensión T2 de Doc 119 (las signaturas no son continuas bajo los límites) y es el fenómeno Babaee–Huh **[DATO]**: existe una superficie tropical cuya forma de intersección **no tiene la signatura del índice de Hodge**. La signatura correcta del juguete finito NO se propaga automáticamente.

5. **El núcleo (§6):** quedan DOS gaps. (G-125.A, real/entero) la integralidad del número de intersección sobre las correspondencias del flujo —sin ella no hay "rango" entero, reaparece Example 6.5 de Yoshitomi. (G-125.B, signatura, el núcleo profundo) que la signatura $(1,\rho-1)$ del juguete finito **persista** sobre la red completa de correspondencias —que es precisamente lo que Babaee–Huh muestra que puede FALLAR tropicalmente. El test R-NC: la positividad eventual NO es geométrica-reutilizable; se reduce a la fórmula de Lefschetz = lado aritmético = circular (FALLA NC3). **El ingrediente de G2 no queda construido; queda aislado con precisión.**

---

## 1. El mecanismo clásico, fijado con precisión quirúrgica

### 1.1. El objeto: $C\times C$ y su Néron–Severi

**[DATO clásico, Hartshorne *Algebraic Geometry* V.1; Mumford *Abelian Varieties*; Bai *Intersection Theory on Surfaces and RH for Curves* (expos. SRCF), confirmado por WebSearch §0].** Sea $C$ una curva proyectiva lisa de género $g$ sobre $\overline{\mathbb{F}_q}$. La superficie $S=C\times C$ tiene grupo de Néron–Severi $\mathrm{NS}(S)$. Tres clases distinguidas:
- $f_1=C\times\{pt\}$ (fibra horizontal, fibra de la primera proyección $p_1$);
- $f_2=\{pt\}\times C$ (fibra vertical, fibra de $p_2$);
- $\Delta\subset C\times C$ (la diagonal).

A ellas se añaden las **correspondencias**: para un morfismo $\phi:C\to C$, su grafo $\Gamma_\phi=\{(x,\phi(x))\}\subset C\times C$. La diagonal es $\Gamma_{\mathrm{id}}$; el grafo del Frobenius geométrico $\Gamma_{\mathrm{Frob}}$ es la correspondencia clave.

### 1.2. Las relaciones de intersección (el cálculo que hay que reproducir)

**[DATO clásico].** La forma de intersección $D\cdot D'$ sobre $\mathrm{NS}(C\times C)$, restringida a $\langle f_1,f_2,\Delta\rangle$:
$$ f_1^2=0,\quad f_2^2=0,\quad f_1\cdot f_2=1,\quad \Delta\cdot f_1=1,\quad \Delta\cdot f_2=1,\quad \Delta^2=2-2g. $$
- $f_1^2=0$: dos fibras horizontales distintas son disjuntas (la fibra se mueve en su clase a una disjunta). Idem $f_2^2=0$.
- $f_1\cdot f_2=1$: una fibra horizontal y una vertical se cortan en el único punto $(pt_1,pt_2)$, transversalmente.
- $\Delta\cdot f_1=1$: la diagonal corta a $C\times\{pt\}$ en el único punto $(pt,pt)$.
- $\Delta^2=2-2g$: por adjunción/auto-intersección, $\Delta^2=\deg(N_{\Delta/S})=\deg(T_C)=2-2g=-\deg K_C$. Equivalentemente $\Delta^2=\chi_{\text{top}}(C)$ (la auto-intersección de la diagonal = característica de Euler topológica, **[DATO]** confirmado por WebSearch §0: "the topological Euler characteristic equals the self-intersection number of the diagonal in the Cartesian product").

La matriz de Gram en la base ordenada $(f_1,f_2,\Delta)$:
$$ G_{\text{clás}}=\begin{pmatrix}0&1&1\\1&0&1\\1&1&2-2g\end{pmatrix}. $$

### 1.3. La signatura y de dónde sale la cota (el corazón de Weil)

**[CÁLCULO] Signatura de $G_{\text{clás}}$.** Determinante: expandiendo,
$$ \det G_{\text{clás}}=0\cdot(0\cdot(2-2g)-1)-1\cdot(1\cdot(2-2g)-1)+1\cdot(1-0)=-(2-2g-1)+1=-(1-2g)+1=2g. $$
Para $g\ge1$, $\det>0$. Traza $=2-2g\le0$. El menor superior-izquierdo $2\times2$ es $\det\begin{pmatrix}0&1\\1&0\end{pmatrix}=-1<0$. Una forma $3\times3$ simétrica con un menor $2\times2$ de determinante $-1$ tiene **al menos una dirección positiva y al menos una negativa** en ese plano; el signo del determinante total ($+$, para $g\ge1$) con traza $\le0$ fuerza signatura $(1,2)$ (una positiva, dos negativas). Es el **índice de Hodge: signatura $(1,\rho-1)$** con la única dirección positiva en el "cono amplio".

**[DATO] El teorema del índice de Hodge** (sobre toda $\mathrm{NS}(S)\otimes\mathbb{R}$, no solo el plano): signatura $(1,\rho-1)$; sobre $(H)^\perp$ (ortogonal a una clase amplia $H$, $H^2>0$) la forma es **definida negativa**.

**[CÁLCULO] La cadena hacia RH.** El plano amplio es $P=\langle f_1,f_2\rangle$ (clase amplia $H=f_1+f_2$, $H^2=2>0$). Para una correspondencia $Z$ de bigrado $(a,b)$, su parte primitiva $Z_0=Z-a\,f_2-b\,f_1$ cumple $Z_0\cdot f_1=Z_0\cdot f_2=0$, es decir $Z_0\in P^\perp$. Índice de Hodge $\Rightarrow Z_0^2\le0$. Esta es la **desigualdad de Castelnuovo–Severi**:
$$ Z^2\le 2\,(Z\cdot f_1)(Z\cdot f_2)\quad\Longleftrightarrow\quad Z_0^2\le0. $$
Aplicada a $Z=\Gamma_{\mathrm{Frob}^n}$ (grafo del Frobenius $n$-ésimo, bigrado $(1,q^n)$, $\Gamma\cdot\Delta=\#C(\mathbb{F}_{q^n})=N_n$) la desigualdad de Cauchy–Schwarz asociada da $|\alpha_i|=\sqrt q$ para los autovalores de Frobenius en $H^1$ — **RH para curvas**.

**[CÁLCULO] Por qué NO es circular** (esto es el quicio, lo subrayo para el test R-NC más adelante): la positividad de partida ($Z_0^2\le0$) es un teorema sobre **TODAS las clases primitivas de la superficie**, probado por geometría de superficies (índice de Hodge = dualidad de Poincaré en $H^2$ + teorema del índice de Sylvester), que **ignora cuál es $C$ y dónde están sus puntos**. La positividad es geométrica, independiente de los autovalores. Eso es lo que el test R-NC (Doc 119 §4.3) llama NC2 (sobregeneración con contenido) + NC4 (en $\neg$RH un autovalor malo da una auto-intersección del signo prohibido, visible sin localizar nada). **Este es el patrón exacto que hay que reproducir tropicalmente — o donde hay que documentar la traba.**

---

## 2. El objeto base y el cuadrado [DATO + CONSTRUCCIÓN]

### 2.1. El sitio de escala como objeto tropical de dimensión 1 [DATO]

**[DATO]** (Connes–Consani *Geometry of the Scaling Site*, arXiv:1603.03191; vía Doc 123 §4.1): el sitio de escala es, en su versión analítica, el cociente $[0,\infty)\rtimes\mathbb{R}_+^*$ / topos del semigrupo de escala; su "bloque elemental" asociado al primo $p$ es
$$ C_p=\mathbb{R}_+^*/p^{\mathbb{Z}},\qquad\text{en la coordenada }u=\log\lambda:\quad C_p=\mathbb{R}/(\log p)\,\mathbb{Z}, $$
un **círculo tropical de período $\log p$**, dimensión 1, **género tropical 1** (un lazo). El haz $\mathcal{O}_p$: funciones periódicas, convexas, afines a trozos, con pendientes en $H_p=\{m/p^n\}\subset\mathbb{Q}$.

**[DATO]** (1603.03191, Thm 5.17): RR tropical de tipo II,
$$ \mathrm{Dim}_{\mathbb{R}}H^0(D)-\mathrm{Dim}_{\mathbb{R}}H^0(-D)=\deg D, $$
con $\mathrm{Dim}_{\mathbb{R}}$ la dimensión continua (límite normalizado $p^{-n}\dim_{\text{top}}$). **NO hay $H^1$ en $C_p$**; su rol lo juega $H^0(-D)$ (la dualidad de Serre tropical).

**[DATO]** (Yoshitomi, arXiv:1001.0448, vía Doc 124 §6.3 punto 1): el RR tropical de Baker–Norine/Gathmann–Kerber/Yoshitomi tiene la forma
$$ r(D)-r(K-D)=\deg D-g+1, $$
con $r(D)=\max\{r\in\mathbb{Z}_{\ge-1}:U(D,r)=\emptyset\}$ el **rango de equivalencia lineal**, definido vía $\mathrm{ord}(f,P)$ — un invariante de la equivalencia lineal **NO visible desde la estructura de módulo** del $H^0$. El **Example 6.5** exhibe $(C,D),(C',D')$ con $H^0$ isomorfos como módulos pero $r(D)=1\ne r(D')=0$ **[DATO]**. Este es el dato que envenena la integralidad del rango (la "raíz" de Doc 123).

**[CÁLCULO] El divisor canónico tropical de $C_p$.** Para una curva tropical $\Gamma$ de género $g$ (primer número de Betti del grafo), el divisor canónico de Baker–Norine es $K=\sum_{v}(\mathrm{val}(v)-2)\,v$, de grado $\deg K=2g-2$. Para $C_p$ visto como un único lazo liso (un círculo, sin vértices de valencia $\ne2$), $g=1$, $\deg K=0$, $K\sim0$. Coherente con el RR de §arriba: $g=1\Rightarrow\deg K=0$.

### 2.2. El género ligado a los ceros [DATO + CONJETURA]

**[DATO]** (Doc 124 §3.3, vía Connes–Consani *Metaphysics of $F_1$*, arXiv:2307.06748, nota 3): la cohomología buscada $H^1(\mathbf{C})$ es de **dimensión infinita** (infinitos ceros de $\zeta$), y el RR que CC tienen para $\overline{\mathrm{Spec}\,\mathbb{Z}}$ da **género 0** para $\mathrm{Spec}\,\mathbb{Z}$ (un objeto de dim 1, género 0). El "género" relevante para el cuadrado no es el de un factor sino el del producto, y ahí (Doc 119 §2.4) la parte impura debe ser finita pero la total infinita.

**[CONJETURA]** El "género tropical" del sitio de escala completo (no del bloque $C_p$) es infinito, indexado por los ceros; el cuadrado hereda el problema de Doc 123: no hay Künneth porque los factores no tienen $H^1$. Trabajo por eso en el bloque $C_p$ (género 1), donde todo es finito y computable, y declaro al final qué sobrevive y qué no al ensamblaje.

### 2.3. El cuadrado $X\times X$ como objeto 2-dimensional [CONSTRUCCIÓN]

**[CONSTRUCCIÓN] (estatus: define el producto, asume conmutación con tropicalización, deja por verificar la categoría exacta).** Defino $X\times X$ en la categoría de **espacios tropicales / $\mathbb{R}_{\max}$-esquemas** como el producto fibrado del topos del sitio de escala consigo mismo sobre $\mathbb{B}$ (extendido a $\mathbb{R}_+^{\max}$), con haz de estructura el producto tensorial idempotente $\mathcal{O}\otimes_{\mathbb{B}}\mathcal{O}$ (secciones = polígonos de Newton bidimensionales).
- **Para el bloque:** $C_p\times C_p=(\mathbb{R}/(\log p)\mathbb{Z})^2$, un **toro tropical bidimensional** de área $(\log p)^2$, con coordenadas $(u,v)$.
- **Divisores (codim 1):** "curvas" tropicales dentro de la superficie — grafos rectos racionales de pendiente en $H_p$, y sus combinaciones balanceadas (ciclos tropicales de codim 1 con pesos enteros).
- **Asume (A0):** que $\otimes_{\mathbb{B}}$ conmuta con tropicalización y envolvente convexa (Paso 1 del Cruce B, Doc 121; **[GAP TÉCNICO]** heredado de Doc 123 §6.1).
- **Por verificar:** que sea liso/sin-singularidad tropical (necesario para que el índice de Hodge tropical de Babaee–Huh/superficies tenga la signatura controlada — §5.5).

### 2.4. Las clases distinguidas [CONSTRUCCIÓN]

En $C_p\times C_p=(\mathbb{R}/(\log p)\mathbb{Z})^2$:
- $f_1=C_p\times\{v_0\}$ (curva horizontal, un círculo "$v=$ const"): ciclo tropical de codim 1, pendiente 0 en la dirección $u$.
- $f_2=\{u_0\}\times C_p$ (curva vertical, "$u=$ const").
- $\Delta=\{u=v\}$ (la diagonal, pendiente 1).
- **Correspondencias** $F_\mu$: el grafo del flujo de escala $F_\mu:C_p\to C_p$, $u\mapsto u+\log\mu$ — es decir $\Delta_\mu=\{v=u+\log\mu\}$, una **traslación de la diagonal**. Para $\mu=p^k$, $F_{p^k}$ es la "Frobenius entera" $k$-ésima (cierra el lazo sobre sí mismo $k$ veces si se compone con la pendiente). Estas son el **análogo de los grafos de Frobenius** $\Gamma_{\mathrm{Frob}^n}$ del §1.

**[CÁLCULO] Observación de bigrado.** $\Delta_\mu$ tiene pendiente $1$ (bigrado $(1,1)$ en el sentido de las proyecciones), igual que $\Delta=\Delta_1$. Las pendientes generales $v=su+c$ con $s\in H_p$ dan correspondencias de "multibigrado" $(1,s)$ — el análogo del bigrado $(1,q^n)$ del Frobenius es la pendiente $s$. **Aquí el flujo es continuo: $\mu\in\mathbb{R}_+^*$, no $\mathbb{Z}$** (R-LEF-FLUJO, Doc 119 §3.4). Esta es la diferencia estructural decisiva con curvas.

---

## 3. El número de intersección — la pieza central (el C-rank) [CONSTRUCCIÓN]

Defino $D\cdot D'$ y evalúo las tres vías candidatas.

### 3.1. Vía (a) — Intersección estable de Allermann–Rau / Mikhalkin

**[DATO]** (Allermann–Rau, arXiv:0709.3705 *First Steps in Tropical Intersection Theory*; Mikhalkin; confirmado WebSearch §0): existe un **producto de intersección estable** de ciclos tropicales con pesos enteros, bien definido como ciclo tropical (sin pasar a equivalencia racional). Dos construcciones equivalentes **[DATO]**: (i) **fan displacement rule** de Mikhalkin —perturbar genéricamente uno de los ciclos y contar las celdas de intersección transversal con multiplicidad = índice de las redes de pesos—; (ii) **reducción a la diagonal + divisores de Cartier** de Allermann–Rau. Coinciden (límite).

**[CONSTRUCCIÓN — definición del apareamiento.] Para dos 1-ciclos tropicales $D,D'$ en el toro $C_p\times C_p$, defino**
$$ D\cdot D' \;:=\; \deg\big(\,\mathrm{st}(D,D')\,\big)\in\mathbb{R}, $$
donde $\mathrm{st}(D,D')$ es la intersección estable (un 0-ciclo tropical = suma formal de puntos con pesos) y $\deg$ suma los pesos. **Multiplicidad en un punto transversal** $P$ donde $D$ tiene dirección primitiva $\xi$ (peso $m$) y $D'$ dirección $\xi'$ (peso $m'$):
$$ \mathrm{mult}_P(D\cdot D')=m\,m'\cdot\big|\det(\xi,\xi')\big|_{\text{índice de red}}, $$
el índice del sublattice $\mathbb{Z}\xi+\mathbb{Z}\xi'$ en la red ambiente.
- **Estatus:** bien definido para 1-ciclos con direcciones racionales (pendientes en $H_p$). **Simétrico, bilineal sobre $\mathbb{R}$** (los pesos pueden ser reales tras la normalización tipo II de Doc 123 §4). **El "$\det$ de índice de red" es la fuente de la integralidad cuando las direcciones son enteras, y de la realidad cuando no.**

### 3.2. Vía (b) — Grado de la restricción del RR

**[CONSTRUCCIÓN].** Para $D'$ una curva tropical irreducible y $D$ un divisor del cuadrado, $D\cdot D'=\deg_{D'}(\mathcal{O}(D)|_{D'})$ = grado del divisor inducido por restricción de $\mathcal{O}(D)$ a $D'$, vía el RR tropical de $D'$ (que es un $C_p$, dim 1, RR tipo II de §2.1). **[CÁLCULO]** Para $D=f_1$, $D'=\Delta$: la restricción de $\mathcal{O}(f_1)$ a la diagonal $\Delta\cong C_p$ es un divisor de grado = número de puntos $\Delta\cap f_1$ contados con multiplicidad = (vía RR) $\deg=1$. Coincide con la vía (a).

**[CÁLCULO] Compatibilidad (a)$\leftrightarrow$(b).** En el toro liso, la intersección estable de $D$ con una curva $D'$ iguala el grado del fibrado restringido, por la fórmula de proyección tropical (Allermann–Rau, push-forward/pull-back). **Coinciden donde ambos están definidos** (curvas irreducibles racionales). ✓

### 3.3. Vía (c) — Traza del flujo (puntos fijos / órbitas periódicas)

**[CONSTRUCCIÓN].** $D\cdot\Delta_\mu$ = número de puntos fijos de la correspondencia $F_\mu$ pesados = el análogo tropical del término de Lefschetz. Para $\Delta_\mu=\{v=u+\log\mu\}$ y $\Delta=\{v=u\}$:
$$ \Delta\cdot\Delta_\mu=\#\{(u,v):v=u\text{ y }v=u+\log\mu\}=\#\{u:\log\mu\equiv0\ (\mathrm{mod}\ \log p)\}. $$
- Si $\mu\in p^{\mathbb{Z}}$ (i.e. $\log\mu=k\log p$): la condición es vacía como ecuación puntual pero los grafos **coinciden** (se solapan a lo largo de todo el círculo) — intersección no transversal; tras perturbación estable (fan displacement) el número es el de auto-intersección $\Delta^2$ ponderado, **órbita periódica de longitud $k\log p$**. Esto reproduce R-LEF-PRIMOS (Doc 119 §3.3): cada primo $p$ aporta la órbita de período $\log p$.
- Si $\mu\notin p^{\mathbb{Q}}$ (genérico, $\log\mu/\log p$ irracional): los dos grafos son traslaciones que se cortan transversalmente en **un punto por celda fundamental**, $\Delta\cdot\Delta_\mu=1$ — pero la **posición** del punto recorre densamente el círculo al variar $\mu$, y al pesar por la medida tipo II la contribución es **real**.

**[CÁLCULO — el dato crítico].** La vía (c) **ES la fórmula de Lefschetz/traza del flujo de Guillemin–Connes** (Doc 119 §3.4 R-LEF-FLUJO, [DATO] Connes Selecta 1999: la traza distribucional del flujo de escala reproduce el lado aritmético de la fórmula explícita, órbitas periódicas de longitud $\log p$). Coincide con (a) en los puntos transversales. **Pero su coincidencia con el lado aritmético es exactamente el punto donde R-NC va a morder (§6.3): la "geometría" (c) ES la fórmula explícita re-empaquetada (tensión T3 de Doc 119).**

### 3.4. La tensión real/entero — el corazón del problema [CÁLCULO]

**Este es el núcleo de Doc 123 (C-rank), tratado con todo cuidado.**

**[CÁLCULO] Cuándo el número es entero.** La multiplicidad $\mathrm{mult}_P=m\,m'|\det(\xi,\xi')|$ es entera **si y solo si** las direcciones $\xi,\xi'$ son vectores de la red entera $\mathbb{Z}^2$ y los pesos $m,m'$ son enteros. Para $f_1,f_2,\Delta$ las direcciones son $(1,0),(0,1),(1,1)$ — **enteras** — y los pesos naturales son 1. **Por eso §4 dará enteros.** Para $\Delta_\mu$ con $\log\mu=k\log p$ ($\mu\in p^{\mathbb{Z}}$): dirección $(1,1)$, entera → entero.

**[CÁLCULO] Cuándo el número es real.** Para $\Delta_\mu$ genérica ($\mu\notin p^{\mathbb{Q}}$), o para una curva con pendiente $s\in H_p$ general: la red de pendientes $H_p=\{m/p^n\}$ es **densa en $\mathbb{R}$** (Doc 123 §4.2). El "$\det$ de índice de red" entre $(1,0)$ y $(1,s)$ es $|s|$, que para $s\in H_p$ es racional pero **no acotado en denominador**; y bajo la normalización tipo II (necesaria para que $\mathrm{Dim}_{\mathbb{R}}$ exista, §2.1) el peso efectivo es **real**. El grado del 0-ciclo de intersección es entonces **un número real genérico**.

**[CONSTRUCCIÓN — la sub-clase entera, y por qué no basta].**
> **Sub-red entera $\mathcal{L}_{\mathbb{Z}}$:** las clases generadas por $\{f_1,f_2,\Delta\}$ y las correspondencias $\Delta_{p^k}$ ($k\in\mathbb{Z}$) — direcciones en $\mathbb{Z}^2$, pesos enteros. **Sobre $\mathcal{L}_{\mathbb{Z}}$ el número de intersección ES entero** (es la red de "Frobenius enteras", el monoide $\mathbb{N}^\times$ actuando, Doc 119 §3.4 versión cómoda).
>
> **Por qué no basta (la traba exacta):** el flujo de escala que R-LEF necesita es **continuo**, $\mu\in\mathbb{R}_+^*$. El **generador infinitesimal** del flujo (el que da el lado espectral $\sum_\rho\hat h(\rho)$, Doc 119 §3.4 punto 3) NO está en $\mathcal{L}_{\mathbb{Z}}$: corresponde a $\mu$ infinitesimalmente cercano a 1, pendiente $1$ pero traslación irracional. La signatura/cota que RH necesita se lee sobre las correspondencias del **flujo continuo**, no sobre la sub-red entera. $\mathcal{L}_{\mathbb{Z}}$ es **numerablemente delgada** y no contiene el objeto que codifica los ceros.

**[CÁLCULO] Veredicto §3.4: el C-rank de Doc 123 sigue REAL.** El número de intersección es entero sobre $\mathcal{L}_{\mathbb{Z}}$ (que reproduce el §4 clásico) pero **real sobre las correspondencias del flujo continuo** (que es donde vive el contenido de RH). Esta es exactamente la dicotomía de Doc 123 §4: el objeto existe, la dimensión/número permanece tipo II / real. **NO resuelto. Es G-125.A.**

---

## 4. Las relaciones de intersección [CÁLCULO]

Computo sobre $\mathcal{L}_{\mathbb{Z}}\supset\langle f_1,f_2,\Delta\rangle$ en $C_p\times C_p$, vía (a) intersección estable. Normalizo el área de la celda fundamental a 1 (absorbo el factor $\log p$ al final).

**$f_1\cdot f_1$ [CÁLCULO]:** $f_1=\{v=v_0\}$, dirección $(1,0)$. Perturbo a $f_1'=\{v=v_0'\}$ con $v_0'\ne v_0$: dos círculos horizontales paralelos, **disjuntos** en el toro. $\Rightarrow f_1^2=0$. ✓ (igual que clásico).

**$f_2\cdot f_2=0$** [CÁLCULO]: idem por simetría. ✓

**$f_1\cdot f_2$ [CÁLCULO]:** $f_1=\{v=v_0\}$ dir $(1,0)$, $f_2=\{u=u_0\}$ dir $(0,1)$. Se cortan en el único punto $(u_0,v_0)$ del toro, transversal, $|\det\begin{pmatrix}1&0\\0&1\end{pmatrix}|=1$. $\Rightarrow f_1\cdot f_2=1$. ✓

**$\Delta\cdot f_1$ [CÁLCULO]:** $\Delta=\{v=u\}$ dir $(1,1)$, $f_1=\{v=v_0\}$ dir $(1,0)$. Corte: $u=v_0$, único punto $(v_0,v_0)$. $|\det\begin{pmatrix}1&1\\1&0\end{pmatrix}|=|-1|=1$. $\Rightarrow\Delta\cdot f_1=1$. ✓

**$\Delta\cdot f_2=1$** [CÁLCULO]: idem. ✓

**$\Delta\cdot\Delta$ [CÁLCULO — la auto-intersección, vía perturbación].** $\Delta=\{v=u\}$. Perturbo a $\Delta'=\{v=u+\epsilon\}$ (traslación, $=\Delta_\mu$ con $\log\mu=\epsilon$ pequeño irracional). $\Delta$ y $\Delta'$ son paralelas (ambas dir $(1,1)$): **no se cortan transversalmente en una recta de $\mathbb{R}^2$**, pero **en el toro** $(\mathbb{R}/(\log p)\mathbb{Z})^2$ la recta $v=u+\epsilon$ se enrolla y corta a $v=u$ en los puntos donde $\epsilon\equiv0\pmod{\log p}$ a lo largo de la dirección transversal. Para una recta de pendiente 1 en el toro cuadrado de lado $L=\log p$: el número de auto-intersecciones de una curva cerrada de clase de homología $(1,1)$ es, por la **forma de intersección del toro** $H_1(T^2)\times H_1(T^2)\to\mathbb{Z}$, $\langle(1,1),(1,1)\rangle=\det\begin{pmatrix}1&1\\1&1\end{pmatrix}=0$.

Pero la auto-intersección **geométrica** (adjunción) debe dar $2-2g$. Para $g=1$ (el toro/círculo $C_p$ tiene género 1): $2-2g=0$. **¡Coinciden! $\Delta^2=0$ para $g=1$.** ✓

**[CÁLCULO — verificación cruzada con adjunción tropical].** La diagonal $\Delta\cong C_p$ es una curva de género 1; su auto-intersección por adjunción tropical es $\Delta^2=-\deg(K_\Delta)=-(2g-2)=2-2g=0$ para $g=1$. Las dos vías (homología del toro vs adjunción) **coinciden**: $\Delta^2=0$. Este es un genuino chequeo de consistencia de la construcción. ✓

**[CÁLCULO] La matriz de Gram del juguete** (base $(f_1,f_2,\Delta)$, $g=1$, factor $\log p$ restaurado al final como escala global positiva que no cambia signatura):
$$ \boxed{\,G_{\text{toy}}=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}\,} $$
Nótese: es $G_{\text{clás}}$ con $2-2g=0$ ($g=1$). **El juguete reproduce exactamente el template clásico en género 1.**

---

## 5. El modelo de juguete $C_p\times C_p$ — la evidencia honesta [CÁLCULO]

### 5.1. Signatura de $G_{\text{toy}}$ [CÁLCULO]

Valores propios de $\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$. Polinomio característico: esta es $J-I$ donde $J$ es la matriz de todos-unos $3\times3$. $J$ tiene autovalores $3,0,0$; luego $J-I$ tiene autovalores $3-1=2$ y $0-1=-1$ (doble):
$$ \mathrm{spec}(G_{\text{toy}})=\{\,2,\,-1,\,-1\,\}. $$
**Signatura $(1,2)$** — una dirección positiva (el autovector $(1,1,1)$, autovalor $+2$), dos negativas. Esto es **exactamente $(1,\rho_{\text{toy}}-1)$** con $\rho_{\text{toy}}=\dim\langle f_1,f_2,\Delta\rangle=3$. **El índice de Hodge aparece en el juguete.** [Coincide con el cálculo clásico §1.3 evaluado en $g=1$: $\det G=2g=2>0$, traza $=0$, signatura $(1,2)$.]

### 5.2. La forma sobre el primitivo [CÁLCULO]

Clase amplia $H=f_1+f_2$ (coordenadas $(1,1,0)$). $H^2=(1,1,0)G_{\text{toy}}(1,1,0)^T=2(f_1\cdot f_2)=2>0$. ✓ amplia.

Primitivo $P^\perp=\{x:x^TG_{\text{toy}}H=0\}$. $G_{\text{toy}}H=G_{\text{toy}}(1,1,0)^T=(1,1,2)^T$. Condición: $x_1+x_2+2x_3=0$. Base del primitivo: $e_1=(1,-1,0)$, $e_2=(1,1,-1)$ (chequeo: $1+1-2=0$ ✓).

Forma restringida:
- $e_1^TGe_1=(1,-1,0)G(1,-1,0)^T$. $G e_1=G(1,-1,0)^T=(0\cdot1+1\cdot(-1)+1\cdot0,\,1\cdot1+0+0,\,1\cdot1-1+0)^T=(-1,1,0)^T$. $e_1\cdot Ge_1=1\cdot(-1)+(-1)(1)+0=-2$.
- $e_2^TGe_2$: $Ge_2=G(1,1,-1)^T=(0+1-1,\,1+0-1,\,1+1+0)^T=(0,0,2)^T$. $e_2\cdot Ge_2=1\cdot0+1\cdot0+(-1)(2)=-2$.
- $e_1^TGe_2$: $e_1\cdot Ge_2=(1,-1,0)\cdot(0,0,2)=0$.

Matriz de la forma en el primitivo: $\begin{pmatrix}-2&0\\0&-2\end{pmatrix}$ — **definida negativa.** ✓✓

**[CÁLCULO] Veredicto §5:** sobre el subespacio finito $\langle f_1,f_2,\Delta\rangle$ del juguete $C_p\times C_p$, la forma de intersección tropical (vía Allermann–Rau) tiene **signatura $(1,2)$**, clase amplia $H=f_1+f_2$ con $H^2=2>0$, y es **definida negativa sobre el primitivo** $(H)^\perp$. **El índice de Hodge se reproduce exactamente en el juguete.** Este es el resultado positivo más fuerte del documento: en el caso más simple, finito, la signatura correcta SÍ aparece.

### 5.3. Añadiendo una correspondencia entera $\Delta_{p}$ [CÁLCULO]

Sea $\Delta_p=\Delta_\mu$ con $\log\mu=\log p$ — pero en el toro de período $\log p$, $\log\mu=\log p\equiv0$, así que $\Delta_p$ es **homóloga a $\Delta$** (misma clase $(1,1)$). En el juguete de un solo bloque, las correspondencias enteras colapsan a la clase de $\Delta$: no agrandan $\rho$. **[CÁLCULO]** Esto refleja que un solo $C_p$ ve solo el primo $p$; para ver la "Frobenius" no trivial hay que ir al **producto sobre varios primos** $C_p\times C_q$ ($p\ne q$), donde $\Delta$ (correspondencia diagonal) y las correspondencias de bigrado mixto SÍ son independientes. Eso agranda $\rho$ pero **mantiene direcciones enteras** mientras los períodos sean conmensurables — y los períodos $\log p,\log q$ son **inconmensurables** ($\log p/\log q\notin\mathbb{Q}$), reintroduciendo la realidad. (Coherente con 1502.05580 / Doc 123 §1.1: composición de correspondencias exacta solo para $\lambda\lambda'\notin\mathbb{Q}$.)

### 5.4. ¿Entero o real? [CÁLCULO — la respuesta del juguete]

**Sobre $\langle f_1,f_2,\Delta\rangle$: ENTERO** (matriz $G_{\text{toy}}$ de entradas $\{0,1\}$, §4). **Sobre las correspondencias del flujo continuo $\Delta_\mu$ ($\mu\notin p^{\mathbb{Q}}$): REAL** (§3.4). La frontera es exactamente $\mathcal{L}_{\mathbb{Z}}$ vs el flujo continuo. **El juguete confirma: hay una sub-clase (finita, entera) donde todo funciona, pero NO es la clase que porta el contenido de RH.**

### 5.5. El paso a rango infinito — donde la signatura puede romperse [CÁLCULO + DATO]

**[CÁLCULO] El problema.** La red completa de correspondencias $\{\Delta_\mu:\mu\in\mathbb{R}_+^*\}\cup\{$pendientes en $H_p\}$ NO es de rango finito: las pendientes son densas en $\mathbb{R}$ (Doc 123 §4.2). El cálculo de §5.1–5.2 (signatura $(1,2)$, primitivo definido negativo) es de un subespacio **finito**. La pregunta de G2 es si la signatura $(1,\rho-1)$ **persiste** sobre toda la red.

**[DATO — el contraejemplo de Babaee–Huh].** (Babaee–Huh, *A tropical approach to a generalized Hodge conjecture for positive currents*, Duke Math. J. 2017, arXiv:1502.00299; confirmado WebSearch §0): **existe una superficie tropical en $\mathbb{R}^4$ cuya forma de intersección NO tiene la signatura correcta del teorema del índice de Hodge.** Concretamente construyen una corriente tropical (clase $(1,1)$ / $(p,p)$) que es fuertemente positiva, cerrada, de clase racional, pero NO aproximable por combinaciones positivas de corrientes de integración — y la obstrucción es precisamente que **la forma de intersección de la superficie tropical subyacente tiene la signatura equivocada** (no $(1,\rho-1)$).

**[CÁLCULO] La consecuencia para G2 — la traba profunda.** Babaee–Huh muestra que **NO es automático** que una superficie tropical tenga índice de Hodge. El índice de Hodge tropical SÍ vale para 2-complejos tropicales **lisos/no-singulares** (WebSearch §0: "Hodge index theorem for the intersection product on a tropical surface ... at most one positive eigenvalue" — para complejos no-singulares, vía la línea de Cartwright/superficies tropicales), pero falla en presencia de singularidades tropicales (que es lo que Babaee–Huh explota). Por tanto:
> La signatura correcta $(1,2)$ del juguete **finito y liso** NO se propaga gratis a la red infinita de correspondencias del cuadrado, porque (i) el paso a rango infinito (densidad de $H_p$) es un límite, y **las signaturas no son continuas bajo límites** (tensión T2 de Doc 119 §6.3); (ii) el cuadrado del sitio de escala podría tener singularidades tropicales (no verificado que sea liso — §2.3 por verificar), y en presencia de singularidades el índice de Hodge **puede fallar** (Babaee–Huh).

**[CÁLCULO] Veredicto §5:** el juguete finito da la signatura correcta $(1,2)$ — evidencia genuinamente positiva. Pero la propagación a la red completa es **exactamente lo que Babaee–Huh muestra que puede fallar tropicalmente**, y depende de (a) lisura del cuadrado (no verificada), (b) que el límite rango-finito→rango-infinito preserve signatura (T2, sin gap conocido). **G-125.B.**

---

## 6. El estatus — qué quedó construido, qué falta [GAP/CONJETURA] + test R-NC

### 6.1. Lo construido (con estatus condicional)

**[CONSTRUCCIÓN, a verificar por expertos, NUNCA [DATO]]:**
1. La **definición del apareamiento** $D\cdot D'=\deg(\mathrm{st}(D,D'))$ vía intersección estable de Allermann–Rau (§3.1), simétrica y bilineal sobre $\mathbb{R}$. **Vía (a) es la que funciona**; coincide con (b) grado-RR donde se solapan; coincide con (c) traza-del-flujo en puntos transversales —pero (c) es la fórmula de Lefschetz (problema R-NC).
2. Las **relaciones de intersección** $f_1^2=f_2^2=0$, $f_1\cdot f_2=\Delta\cdot f_i=1$, $\Delta^2=2-2g$ **reproducidas tropicalmente** en $C_p\times C_p$ (§4), con doble chequeo (homología del toro vs adjunción tropical) para $\Delta^2=0$ en $g=1$. **Genuino, dentro del juguete.**
3. La **matriz de Gram $G_{\text{toy}}$ y su signatura $(1,2)$** con primitivo definido negativo (§5.1–5.2). **El índice de Hodge aparece en el juguete finito.**

### 6.2. Los dos gaps

**[GAP G-125.A — real/entero, el C-rank de Doc 123].** El número de intersección es **entero sobre $\mathcal{L}_{\mathbb{Z}}$** (sub-red de direcciones enteras: $f_1,f_2,\Delta$, Frobenius enteras $\Delta_{p^k}$) pero **real sobre las correspondencias del flujo continuo** $\Delta_\mu$, $\mu\notin p^{\mathbb{Q}}$ (densidad de $H_p$, normalización tipo II). El flujo que porta los ceros (el generador infinitesimal) vive fuera de $\mathcal{L}_{\mathbb{Z}}$. **Sin integralidad sobre las correspondencias del flujo, no hay "rango" entero funtorial; reaparece Example 6.5 de Yoshitomi.** No resuelto.

**[GAP G-125.B — signatura, el núcleo profundo].** Que la signatura $(1,\rho-1)$ del juguete finito **persista** sobre la red completa de correspondencias. Falla potencial por (i) discontinuidad de signaturas en el límite rango-finito→infinito (T2), (ii) **el fenómeno Babaee–Huh** [DATO 1502.00299]: superficies tropicales con signatura de intersección equivocada existen, y el cuadrado del sitio de escala no se ha verificado liso. **El índice de Hodge tropical NO es automático.** Núcleo no resuelto.

### 6.3. El test R-NC aplicado (Doc 119 §4.3)

**[CÁLCULO]** La positividad que G2 eventualmente necesita es $Z_0^2\le0$ sobre el primitivo (Castelnuovo–Severi tropical). ¿Es geométrica (reutilizable, vale para correspondencias generales) o se reduce a RH (circular)?

- **NC1 (externalidad):** la definición de $D\cdot D'$ (intersección estable) y de las clases $f_i,\Delta$ es funtorial desde el sitio, no menciona $\zeta$ ni sus ceros. **PASA.**
- **NC2 (sobregeneración):** ¿$Z_0^2\le0$ vale para TODA correspondencia del cuadrado por un teorema de superficies (como Castelnuovo)? **En el juguete finito SÍ** (es el índice de Hodge de $G_{\text{toy}}$, §5.2, vale para todo vector primitivo). **PASA en el juguete finito.** Pero sobre la red infinita **es exactamente G-125.B, no probado** — y Babaee–Huh dice que puede fallar. **PASA condicionalmente, depende de G-125.B.**
- **NC3 (no-reducción a positividades RH-equivalentes):** aquí muerde. La vía (c) del número de intersección **ES la traza del flujo = fórmula de Lefschetz = lado aritmético de la fórmula explícita** (§3.3, [DATO] Connes 1999). Si la positividad se verifica **vía (c)**, es la positividad de Weil re-empaquetada = MW-1/MW-6 (tensión T3 de Doc 119: "cuanto más explícita la fórmula de trazas, mayor el riesgo de que la geometría sea la fórmula explícita re-empaquetada"). **FALLA NC3 si la positividad pasa por la traza del flujo.** La única salida es verificarla vía (a)/(b) —geometría pura de la superficie— **independientemente** de la traza; pero eso es exactamente G-125.B no resuelto.
- **NC4 (test de dos mundos):** en $\neg$RH, ¿un autovalor de Frobenius malo da una clase con auto-intersección del signo prohibido, visible sin localizar el cero? **En el juguete finito, sí en principio** (un $Z_0^2>0$ violaría el índice de Hodge). Pero como la signatura sobre la red infinita no está controlada (G-125.B), **no se puede certificar la violación sin saber dónde está el cero** — cae en la binariedad inaccesible de Doc 108. **FALLA NC4 mientras G-125.B esté abierto.**

**[CÁLCULO] Veredicto R-NC:** la forma de intersección del juguete **pasa NC1 y NC2 en el caso finito** (genuinamente geométrica ahí). Pero **FALLA NC3 y NC4 sobre la red infinita**: la positividad, evaluada vía la traza del flujo, es la fórmula explícita; evaluada vía geometría pura, es G-125.B no resuelto. **La positividad NO es todavía geométrica-reutilizable en el régimen que importa; o es circular (vía c) o es un gap abierto (vía a/b).**

---

## 7. Síntesis y honestidad

**No declaro G2 construido.** Lo construido es honesto y acotado:

- **La forma de intersección se DEFINE** (vía Allermann–Rau, §3.1), es simétrica y bilineal; las tres vías candidatas coinciden donde se solapan, pero la vía (c) traza-del-flujo es la fórmula de Lefschetz y por eso es el origen de la circularidad (R-NC NC3).
- **La matriz de Gram en $C_p\times C_p$ sale $G_{\text{toy}}=\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}$, signatura $(1,2)$, primitivo definido negativo** (§5): el índice de Hodge **SÍ aparece en el juguete finito**. Reproduce exactamente el template clásico de $C\times C$ evaluado en $g=1$ ($\Delta^2=2-2g=0$), con doble chequeo (homología del toro ↔ adjunción tropical). **Esta es la evidencia positiva más fuerte: en el caso más simple, la signatura correcta emerge.**
- **El número de intersección sale ENTERO sobre la sub-red $\mathcal{L}_{\mathbb{Z}}$ (direcciones enteras: $f_1,f_2,\Delta$, Frobenius enteras) y REAL sobre las correspondencias del flujo continuo** (densidad de $H_p$, tipo II). La sub-clase entera existe pero **es numerablemente delgada y no contiene el generador del flujo** que porta los ceros. **El C-rank de Doc 123 sigue real (G-125.A, no resuelto).**

**El núcleo que queda — DOS gaps precisos:**
1. **(G-125.A) Integralidad sobre las correspondencias del flujo continuo.** Sin ella no hay rango entero funtorial; Example 6.5 reaparece. Es el C-rank de Doc 123, ahora localizado en la frontera $\mathcal{L}_{\mathbb{Z}}$ vs flujo continuo.
2. **(G-125.B, el núcleo profundo) Persistencia de la signatura $(1,\rho-1)$ del juguete finito a la red infinita de correspondencias.** Babaee–Huh **[DATO]** muestra que existen superficies tropicales con signatura de intersección **equivocada**: el índice de Hodge tropical NO es automático. Depende de (a) lisura del cuadrado (sin verificar) y (b) continuidad de la signatura bajo el límite rango-finito→infinito (tensión T2, sin gap conocido).

**El punto de traba ES el resultado:** la forma de intersección se construye y, en el juguete finito y liso, **tiene la signatura del índice de Hodge** — esto es nuevo y alentador, y es más de lo que Doc 124 concluía estaba disponible. Pero el contenido de RH vive sobre las **correspondencias del flujo continuo**, donde (i) el número es real no entero (G-125.A), y (ii) la signatura no está controlada y **puede fallar à la Babaee–Huh** (G-125.B). El test R-NC confirma: la positividad o se verifica vía la traza del flujo (= fórmula explícita, circular, FALLA NC3) o vía geometría pura (= G-125.B, gap abierto). **G2 no queda construido; queda con su núcleo aislado: G-125.B —el índice de Hodge tropical sobre el cuadrado completo, evitando el fenómeno Babaee–Huh— es la pieza que falta, y es matemática nueva, no presente en el corpus.**

---

## Referencias

**Fuente tropical (WebSearch/literatura, junio 2026):**
- L. Allermann, J. Rau, *First Steps in Tropical Intersection Theory*, arXiv:0709.3705 (Math. Z. 264 (2010)) — intersección estable, divisores de Cartier, reducción a la diagonal, push/pull. **[DATO]**
- G. Mikhalkin — fan displacement rule; equivalencia con Allermann–Rau (vía literatura, *On Tropical Intersection Theory* arXiv:2107.12067, Selecta 2022). **[DATO]**
- F. Babaee, J. Huh, *A tropical approach to a generalized Hodge conjecture for positive currents*, Duke Math. J. 166 (2017), arXiv:1502.00299 — **superficie tropical en $\mathbb{R}^4$ con forma de intersección de signatura equivocada (no índice de Hodge)**; corriente fuertemente positiva no aproximable. **[DATO — el contraejemplo central de G-125.B.]**
- Índice de Hodge tropical para 2-complejos no-singulares (línea de superficies tropicales; WebSearch §0). **[DATO]**
- S. Yoshitomi, *Generators of modules in tropical geometry*, arXiv:1001.0448 — Example 6.5: $r(D)$ no invariante de iso de módulos. **[DATO, vía Doc 124 §6.3.]**
- D. Bai, *Intersection Theory on Surfaces and the Riemann Hypothesis for Curves* (expos., SRCF) — template $C\times C$. **[DATO, vía WebSearch; cálculo §1 estándar.]**

**Corpus CC/CCM (vía Docs internos, no re-leído en fuente esta sesión):**
- A. Connes, C. Consani, *Geometry of the Scaling Site*, arXiv:1603.03191 — $C_p$, RR tipo II, $\mathrm{Dim}_{\mathbb{R}}$. **[DATO, vía Doc 123 §4.1.]**
- A. Connes, Selecta Math. 5 (1999) — traza distribucional del flujo de escala = lado aritmético de la fórmula explícita. **[DATO, vía Doc 119 §3.4.]**
- A. Connes, C. Consani, *The Riemann-Roch strategy / Complex lift of the Scaling Site*, arXiv:1805.10501 — el cuadrado como meta, null elements. **[DATO, vía Doc 123 §1.]**

**Internas (backward-only):** Doc 80 (Castelnuovo–Severi aritmético: la forma $Q$ semidefinida no distingue medidas); Doc 119 (R-SIG (i)/(ii)/(iii); R-LEF-FLUJO; R-PESO; R-NC NC1–NC4; tensiones T2/T3); Doc 123 (bifurcación C-cok/C-rank; juguete $C_p\times C_p$; norma de intersección = C-rank = G2); Doc 124 (G2 = índice de Hodge INDEFINIDO $(1,\rho-1)$; positividad CC es DEFINIDA, categoría distinta; ingrediente ausente en corpus).

*Fin del Documento 125.*
