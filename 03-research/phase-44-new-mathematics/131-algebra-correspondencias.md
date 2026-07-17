# Doc 131 — El álgebra de correspondencias aritméticas: la categoría 𝒜rith

**Programa:** Hipótesis de Riemann — Phase 44: MATEMÁTICA NUEVA.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 107 (W₂, núcleo engrosado, lado casi-primo autónomo, Teoremas 2.4/4.2/4.4/5.5); Doc 125 (forma de intersección tropical, juguete (1,2), correspondencias Δ_μ, gaps G-125.A/B); Doc 110 (axiomas L1–L6, clase ℱ, Teorema de imposibilidad 4.3, Prop. 4.5); Doc 106 (identidad del índice tensorial).
**Contrato creativo (Phase 44):** **[DEFINICIÓN-NUEVA]** libertad total; **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** probado de verdad, con prueba completa; **[PUENTE]** conexión con ζ/RH con estatus declarado; **[DESEO]** lo que queremos y no probamos; **[DATO]** literatura con cita; **[CONSTRUCCIÓN]** objeto diseñado con estatus declarado. La libertad vive en las definiciones; la disciplina, en qué se llama teorema.

---

## 0. Resumen ejecutivo

Este documento inventa la categoría donde el funcional de Weil de dos variables (Doc 107)
y la forma de intersección del cuadrado (Doc 125) viven nativamente. La jugada central:
la categoría se define sobre **todas** las funciones aritméticas — ζ es UN objeto entre
muchos — de modo que cada teorema es externo a ζ **por construcción** (la cláusula NC2
del test R-NC deja de verificarse a posteriori: está en los axiomas).

Lo que queda probado, sin adorno:

1. **(§1)** El anillo de núcleos de dos variables $(\mathcal{K}_2,\star_2)$ con la
   convolución de Dirichlet doble es un anillo conmutativo local (Teorema 1.4, el
   primer teorema de la categoría), y el anillo de Dirichlet $\mathcal{D}$ es un
   **anillo diferencial** con derivación $a\mapsto a\cdot\log$; la exponencial de
   convolución caracteriza el producto de Euler: $F$ tiene producto de Euler $\iff$
   su derivada logarítmica de Dirichlet está soportada en potencias de primos
   (Teorema 1.9).

2. **(§2–§3)** La categoría $\mathcal{A}rith$: objetos $(a,c,\omega)$ con $a$ función
   aritmética arbitraria; correspondencias = núcleos de dos variables más las
   traslaciones $\Delta_\mu$ del Doc 125, con composición asociativa y unidad
   (Teorema 2.7). El **grado** de una correspondencia es el lado casi-primo: para todo
   objeto, $\deg_X(h_{g,\varphi})$ contiene el bloque
   $\sum_N g(N)\sum_{d\mid N}a(d)\,a(N/d)\,\varphi(d^2/N)$ (Teorema 3.3) — la fórmula
   del Doc 107 con $\Lambda$ reemplazada por una $a$ cualquiera. La involución
   $\rho\mapsto 1-\bar\rho$ es un funtor involutivo $\sigma$ (Prop. 2.9).

3. **(§4)** En la subcategoría espectral $\mathcal{A}rith^{EF}$ (objetos con divisor),
   el **teorema de órbitas** (Teorema 4.4): todo bloque finito $\sigma$-estable del
   divisor produce signatura $(n_{\mathrm{on}}+n_{\mathrm{orb}},\,n_{\mathrm{orb}})$ —
   puntos fijos de $\sigma$ dan direcciones positivas, órbitas libres dan planos
   hiperbólicos. Corolario universal: **el índice negativo nunca excede el positivo**
   ($q\le p$) en ningún objeto de la categoría, y todas las signaturas con $q\le p$
   se realizan (Teorema 4.6, clasificación). La identidad del índice tensorial del
   Doc 106 se importa y se prueba (Teorema 4.8).

4. **(§5)** El **teorema del índice de juguete** del Doc 125 se vuelve teorema de la
   categoría: toda estructura de intersección de rango 3 con género $g$ tiene matriz
   de Gram $\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&2-2g\end{psmallmatrix}$, signatura
   $(1,2)$ y primitivo definido negativo **si y solo si** $g\ge 1$; en $g=0$ la forma
   degenera (Teorema 5.3). La clase de objetos que la realiza: los objetos
   **periódicos** (de un primo), con $g=1$, para coeficientes arbitrarios — la
   signatura del Doc 125 no es de ζ: es del retículo.

5. **(§6) El Axioma H.** Enunciado sin mencionar ceros: $Q_X(f,f):=W_X(f\star\tilde f)
   \ge 0$, con $W_X$ dado por los datos $(a,c,\omega)$. Verificaciones ejecutadas:
   la función constante $1$ **falla** (prueba de tres líneas); toda función
   completamente multiplicativa sin masa polar **falla** (Prop. 6.5, masa diagonal);
   Davenport–Heilbronn **falla en bloques incondicionalmente** (sus ceros off-line
   [DATO] activan el teorema de órbitas). Y el resultado central del documento, el
   **Teorema de pureza local (Teorema 6.7)**: para los objetos de Euler de un primo
   $F_{p,\alpha}$, $H$ vale $\iff |\alpha|=\sqrt p$ — el Axioma H restringido a la
   subcategoría local es **decidible y equivale a pureza de pesos**, con prueba
   completa en ambas direcciones (fórmula de Poisson + test de Mertens de dos
   protuberancias, donde la barrera es exactamente $|c_m|\le 2p^{m/2}$).
   Consecuencia: **el producto de Euler NO implica H** ($F_{p,\alpha}$ con
   $|\alpha|\ne\sqrt p$ tiene Euler y viola H); el discriminador es la pureza, no
   la multiplicatividad.

6. **(§7) [PUENTE]** $H(\zeta_{\mathrm{ob}})\iff$ RH: la dirección RH$\Rightarrow$H es
   el teorema de órbitas (probado acá para toda la categoría); la recíproca es el
   criterio de Weil [DATO]. **RH-equivalente, declarado sin maquillaje.** Lo que la
   categoría redistribuye: (i) H es decidible en las subcategorías local (pureza) y
   de divisor finito; (ii) los axiomas violan **explícitamente** la hipótesis (ii)
   de la Definición 4.2 del Doc 110 (test-accesibilidad): el divisor es dato
   estructural, no incógnita — el Teorema de imposibilidad 4.3 no aplica a los
   funtores de $\mathcal{A}rith^{EF}$, y toda la no-autonomía queda concentrada en
   un único funtor de comparación. (iii) El [DESEO] que queda nombrado: la
   **Conjetura H⁺** ($a\ge 0$ en potencias de primos + hermitiano + bloque polar
   estándar $\Rightarrow$ H) y el **Lema de rigidez del límite** (estabilidad de H
   bajo la filtración de Euler).

7. **(§8)** La renta propia (teoremas independientes de RH): clasificación de
   signaturas alcanzables (q ≤ p, sobreyectiva), pureza local como criterio
   decidible, y la caracterización diferencial del producto de Euler.

---

## 1. El anillo base

### 1.1. El anillo de Dirichlet y el anillo de núcleos

**[DEFINICIÓN-NUEVA 1.1].** $\mathbb{N}^\times := (\mathbb{Z}_{\ge1},\cdot)$, el
monoide multiplicativo (libre conmutativo sobre los primos).
$\mathcal{D} := \{a:\mathbb{N}^\times\to\mathbb{C}\}$ con la convolución de Dirichlet
$(a\star b)(n) = \sum_{de=n} a(d)\,b(e)$.
$\mathcal{K}_2 := \{K:\mathbb{N}^\times\times\mathbb{N}^\times\to\mathbb{C}\}$ con la
**convolución de Dirichlet en dos variables**
$$(K\star_2 L)(m,n) \;:=\; \sum_{m_1m_2=m}\;\sum_{n_1n_2=n} K(m_1,n_1)\,L(m_2,n_2).$$
Ambas sumas son finitas para cada $(m,n)$ (todo entero tiene finitas factorizaciones):
no se impone ninguna condición de soporte ni crecimiento. $\mathcal{K}_2$ es el
álgebra total del monoide $\mathbb{N}^\times\times\mathbb{N}^\times$.

**[TEOREMA 1.2] (estructura de $\mathcal{D}$).** $(\mathcal{D},+,\star)$ es una
$\mathbb{C}$-álgebra conmutativa, asociativa, con unidad $\delta_1$
($\delta_1(1)=1$, $0$ si no), local: $a$ es invertible $\iff a(1)\neq 0$, y el ideal
maximal es $\mathfrak{m} = \{a : a(1)=0\}$.

*Demostración.* Conmutatividad: reindexar $(d,e)\mapsto(e,d)$. Asociatividad:
$((a\star b)\star c)(n) = \sum_{def=n} a(d)b(e)c(f) = (a\star(b\star c))(n)$, una suma
finita simétrica en los tres factores. Unidad: inmediato. Invertibilidad: si
$a(1)\ne0$, definir $b(1)=a(1)^{-1}$ y, por recursión en $n$ ordenado por
divisibilidad, $b(n) = -a(1)^{-1}\sum_{d\mid n,\,d>1}a(d)\,b(n/d)$ (los $n/d$ son
divisores propios, ya definidos); entonces $a\star b=\delta_1$ por construcción.
Si $a(1)=0$: $(a\star b)(1)=a(1)b(1)=0\ne1$ para todo $b$. La localidad: el
complemento de $\mathfrak m$ es exactamente el grupo de unidades. $\square$

**[DATO 1.3].** $(\mathcal{D},\star)$ es además dominio íntegro y de factorización
única (Cashwell–Everett, *The ring of number-theoretic functions*, Pacific J. Math. 9
(1959), 975–985: $\mathcal{D}\cong\mathbb{C}[[x_1,x_2,\dots]]$ vía exponentes de
primos). No load-bearing abajo; se cita por completitud estructural.

**[TEOREMA 1.4] (el primer teorema de la categoría: $\mathcal{K}_2$).**
$(\mathcal{K}_2,+,\star_2)$ es una $\mathbb{C}$-álgebra conmutativa asociativa con
unidad $\delta_{(1,1)}$, local con ideal maximal $\{K:K(1,1)=0\}$. El producto
tensorial $a\otimes b\,(m,n):=a(m)b(n)$ es un morfismo de álgebras
$\mathcal{D}\otimes_{\mathbb{C}}\mathcal{D}\to\mathcal{K}_2$:
$(a\otimes b)\star_2(a'\otimes b') = (a\star a')\otimes(b\star b')$.

*Demostración.* Asociatividad:
$((K\star_2L)\star_2M)(m,n) = \sum_{m_1m_2m_3=m}\sum_{n_1n_2n_3=n}
K(m_1,n_1)L(m_2,n_2)M(m_3,n_3)$, suma finita simétrica; igual para el otro
paréntesis. Conmutatividad y unidad: como en 1.2. Localidad: la misma recursión de
1.2 sobre $\mathbb{N}^\times\times\mathbb{N}^\times$ ordenado por divisibilidad
componente a componente (los divisores propios de $(m,n)$ son finitos y la recursión
está bien fundada porque $\Omega(m)+\Omega(n)$ decrece estrictamente). La identidad
tensorial: expandir ambos lados y reindexar — $\sum_{m_1m_2=m}a(m_1)a'(m_2)\cdot
\sum_{n_1n_2=n}b(n_1)b'(n_2)$. $\square$

**Observación 1.5.** $\star_2$ es la composición "monoidal" de la categoría (la
estructura de anillo de las correspondencias aritméticas discretas); la composición
"de matrices" (correspondencias como operadores) es la de §2.2. Las dos conviven:
$\mathcal{K}_2$ es el álgebra de Hopf-monoide subyacente, §2.2 es la categoría.

### 1.2. La estructura diferencial: el producto de Euler como teorema del anillo

**[DEFINICIÓN-NUEVA 1.6].** La **derivación logarítmica**: $D:\mathcal{D}\to
\mathcal{D}$, $(Da)(n) := a(n)\log n$. Para $F$ unidad normalizada ($F(1)=1$), la
**derivada logarítmica de Dirichlet**: $L(F) := F^{-1}\star DF$. (Para
$F\leftrightarrow\sum F(n)n^{-s}$, $L(F)\leftrightarrow -\,d/ds\,\log$ de la serie;
para $F$ = coeficientes de $\zeta$, $L(F)=\Lambda$.)

**[LEMA 1.7].** $D$ es una derivación de $(\mathcal{D},\star)$:
$D(a\star b) = Da\star b + a\star Db$. En consecuencia $L(F\star G) = L(F)+L(G)$
para unidades normalizadas, y $L(F)=0\iff F=\delta_1$.

*Demostración.* $D(a\star b)(n) = \log n\sum_{de=n}a(d)b(e) =
\sum_{de=n}(\log d+\log e)\,a(d)b(e)$. Aditividad de $L$:
$L(F\star G) = (F\star G)^{-1}\star(DF\star G + F\star DG) = F^{-1}\star DF +
G^{-1}\star DG$. Núcleo: si $L(F)=0$ entonces $DF=0$, i.e. $F(n)\log n=0$ para todo
$n$, i.e. $F(n)=0$ para $n\ge2$; con $F(1)=1$, $F=\delta_1$. $\square$

**[DEFINICIÓN-NUEVA 1.8].** $\exp_\star:\mathfrak m\to 1+\mathfrak m$,
$\exp_\star(g) := \sum_{k\ge0} g^{\star k}/k!$ — bien definida porque
$g^{\star k}(n)=0$ para $k>\Omega(n)$ (cada factor aporta un divisor $>1$): la suma
en cada $n$ es finita.

**[TEOREMA 1.9] (caracterización diferencial del producto de Euler).** Sea $F$
unidad normalizada. Son equivalentes:
(i) $F$ es multiplicativa con producto de Euler: $F(mn)=F(m)F(n)$ para $(m,n)=1$;
(ii) $L(F)$ está soportada en potencias de primos;
(iii) $F = \exp_\star(g)$ con $g$ soportada en potencias de primos.
En tal caso $g(p^k) = L(F)(p^k)/\log p^k$.

*Demostración.* **(iii)$\Rightarrow$(ii):** $D\exp_\star(g) = \exp_\star(g)\star Dg$
(derivar término a término: $D(g^{\star k}) = k\,g^{\star(k-1)}\star Dg$ por el
Lema 1.7 e inducción; las sumas son localmente finitas), luego
$L(\exp_\star g) = Dg$, soportada donde $g$. **(ii)$\Rightarrow$(iii):** dado
$\ell:=L(F)$ soportado en potencias de primos, sea $g(p^k):=\ell(p^k)/(k\log p)$,
$g:=0$ fuera; entonces $L(\exp_\star g) = Dg = \ell = L(F)$, y por el Lema 1.7
$L(F\star(\exp_\star g)^{-1}) = 0$, luego $F=\exp_\star g$. **(iii)$\Rightarrow$(i):**
escribir $g=\sum_p g_p$ (componentes de soporte $p$-ádico disjunto, suma localmente
finita); los $g_p$ conmutan y $g_p\star g_q$ ($p\ne q$) tiene soporte en enteros
mixtos; $\exp_\star(g) = {\star\!\prod}_p \exp_\star(g_p)$ (producto localmente
finito: en cada $n$ solo intervienen los $p\mid n$), y un producto de factores
locales es multiplicativo: $F(mn)$ con $(m,n)=1$ separa los primos de $m$ y de $n$.
**(i)$\Rightarrow$(ii):** si $F$ es multiplicativa, $F = {\star\!\prod}_p F_p$ con
$F_p :=$ restricción de $F$ a $p^{\mathbb{N}}$ (extendida por $0$; la identidad
$F = {\star\!\prod}F_p$ es exactamente la multiplicatividad, evaluada en cada $n$).
Por aditividad de $L$ (extendida a productos localmente finitos: en cada $n$ solo
finitos factores son $\ne\delta_1$), $L(F) = \sum_p L(F_p)$, y cada $L(F_p)$ está
soportada en $p^{\mathbb{N}}$ porque $F_p$, $F_p^{-1}$ y $DF_p$ lo están (subálgebra
cerrada). $\square$

**Observación 1.10 [DATO].** La exponencial de Dirichlet aparece en Rearick,
*Operators on algebras of arithmetic functions*, Duke Math. J. 35 (1968); el
empaquetado "Euler $\iff$ soporte de $L(F)$ en potencias de primos" como teorema del
anillo diferencial es la forma que la categoría necesita en §6.7: **la propiedad
"tener producto de Euler" es una condición de soporte sobre el objeto, visible sin
analiticidad** — es un predicado categórico sobre $a=L(F)$, no sobre la función
analítica $F(s)$.

---

## 2. La categoría $\mathcal{A}rith$

En adelante $G := \mathbb{R}_+^*$ con medida de Haar $d^*x = dx/x$, clase de prueba
$C_c^\infty(G)$, transformada de Mellin $\hat f(s)=\int_0^\infty f(x)x^{s-1}dx$
(entera), e involución $\tilde f(x) := \overline{f(1/x)}\,x^{-1}$, con
$\widehat{\tilde f}(s) = \overline{\hat f(1-\bar s)}$. Convolución multiplicativa
$(f_1\star f_2)(x)=\int_G f_1(y)f_2(x/y)\,d^*y$. Todo como en Doc 107 §1.

### 2.1. Objetos

**[DEFINICIÓN-NUEVA 2.1] (objeto aritmético).** Un objeto de $\mathcal{A}rith$ es una
terna $X=(a,c,\omega)$:
- $a:\mathbb{N}^\times\to\mathbb{C}$ **arbitraria** (el dato discreto; ninguna
  condición de crecimiento: las sumas contra tests de soporte compacto son finitas);
- $c$ = suma formal finita $\sum_j c_j\,[s_j]$, $s_j\in\mathbb{C}$, $c_j\in\mathbb{C}$
  (el **bloque polar**, puntos y pesos arbitrarios);
- $\omega$ = función medible par de crecimiento polinomial sobre $\mathbb{R}$ (el
  **bloque arquimediano**).

El **funcional de Weil del objeto** es, para $f\in C_c^\infty(G)$:
$$W_X(f) \;:=\; \underbrace{\sum_j c_j\,\hat f(s_j)}_{D_c(f)}
\;-\;\underbrace{\sum_{n\ge1}\Bigl[a(n)\,f(n) + \overline{a(n)}\,n^{-1} f(1/n)\Bigr]}_{P_a(f)}
\;-\;\underbrace{\frac{1}{2\pi}\int_{\mathbb{R}}\hat f\!\left(\tfrac12+it\right)\omega(t)\,dt}_{A_\omega(f)}.$$
Todas las sumas son finitas o absolutamente convergentes (soporte compacto +
Paley–Wiener, Doc 107 Lema 1.2). La suma en $n$ arranca en $n=1$: el átomo $a(1)$
(masa en $x=1$) está permitido.

**Ejemplos (el catálogo de trabajo).**
- **$\zeta_{\mathrm{ob}}$:** $a=\Lambda$ (von Mangoldt), $c = [0]+[1]$,
  $\omega=\Omega$ (Doc 107 Def. 1.3). $W_{\zeta_{\mathrm{ob}}} = \mathcal{W}$ del
  Teorema 1.4 del Doc 107.
- **$X_1$ (la función constante):** $a(n)=1\ \forall n$, $c=0$, $\omega=0$.
- **$X_h$ (completamente multiplicativa):** $h:\mathbb{N}^\times\to\{\pm1\}$
  completamente multiplicativa (p.ej. Rademacher aleatoria en los primos);
  $a = h\cdot\Lambda$, $c=0$, $\omega=0$.
- **$F_{p,\alpha}$ (objeto de Euler de un primo):** §6.5; $a(p^m) = -c_m\log p$
  ($m\ge1$) con $c_m=\alpha^m+(p/\bar\alpha)^m$, $c=0$, $\omega\equiv -2\log p$.
- **$X_{DH}$ (Davenport–Heilbronn):** el dato $(a,c,\omega)$ de la función de
  Davenport–Heilbronn (combinación $\tfrac{1-i\kappa}{2}L(s,\chi)+
  \tfrac{1+i\kappa}{2}L(s,\bar\chi)$, $\chi$ el carácter impar mód 5), que tiene
  ecuación funcional pero no producto de Euler [DATO: Davenport–Heilbronn 1936;
  Titchmarsh §10.25]; su $a$ es la sucesión de $-D'/D$, no soportada en potencias
  de primos.
- **Objetos de divisor finito:** cualquier multiconjunto finito
  $Z\subset\mathbb{C}$ define $X_Z := (0, \sum_{\rho\in Z}[\rho], 0)$, con
  $W_{X_Z}(f) = \sum_{\rho\in Z}\hat f(\rho)$. **En la categoría, "cero" y "polo"
  son el mismo tipo de dato con distinto papel** (cf. Doc 107 Obs. 4.1: en el
  objeto doble la separación polo/espectro ya colapsaba; acá se asume desde el
  axioma).

### 2.2. Correspondencias y composición

**[DEFINICIÓN-NUEVA 2.2].** Para objetos $X,Y$, el espacio de correspondencias es
$$\mathrm{Corr}(X,Y) \;:=\; \Bigl\{\,T \;=\; \sum_{\alpha\ \mathrm{finita}}
\lambda_\alpha\,\Delta_{\mu_\alpha} \;+\; T_h \;:\;
\lambda_\alpha\in\mathbb{C},\ \mu_\alpha\in G,\ h\in C_c^\infty(G\times G)\,\Bigr\},$$
operadores sobre $C_c^\infty(G)$: $(\Delta_\mu f)(x) := f(\mu x)$ (la traslación del
Doc 125: el grafo $\{y=\mu x\}$), $(T_h f)(x) := \int_G h(x,y)\,f(y)\,d^*y$. (El
espacio no depende de $X,Y$ — la categoría tiene Hom constante; los objetos pesan
las correspondencias vía el grado de §3. Esa es una elección de diseño: las
correspondencias son **universales**, los números de intersección son **del
objeto**.)

**[LEMA 2.3] (fidelidad del núcleo).** El mapa $(\,(\lambda_\alpha,\mu_\alpha)_\alpha,
h\,)\mapsto T$ es inyectivo: si $T=0$ como operador, entonces todos los
$\lambda_\alpha=0$ y $h=0$.

*Demostración.* Sea $T=\sum\lambda_\alpha\Delta_{\mu_\alpha}+T_h=0$ con
$\mu_\alpha$ distintos. Aplicar a $f_\epsilon$ = aproximación de la identidad en
$x_0\in G$ ($f_\epsilon\ge0$, soporte en $[x_0e^{-\epsilon},x_0e^{\epsilon}]$,
$\int f_\epsilon\,d^*y=1$): $(T_hf_\epsilon)(x)\to h(x,x_0)$ uniformemente sobre
compactos, mientras $(\Delta_\mu f_\epsilon)(x) = f_\epsilon(\mu x)$ está soportada
en $x\in x_0\mu^{-1}e^{\pm\epsilon}$ y tiene masa $L^1_{d^*x}$ igual a 1
concentrándose en el punto $x_0/\mu$. Evaluando $\langle Tf_\epsilon, \phi\rangle$
con $\phi\in C_c^\infty$ soportada lejos de los finitos puntos $x_0/\mu_\alpha$:
queda $\int h(x,x_0)\phi(x)d^*x=0$ para toda tal $\phi$ y todo $x_0$, luego $h=0$
(continuidad). Con $h=0$, tomar $\phi$ = bump en $x_0/\mu_\beta$ que evita los demás
puntos: queda $\lambda_\beta\,\phi$-masa $=0$, luego $\lambda_\beta=0$. $\square$

**[TEOREMA 2.4] (composición).** $\mathrm{Corr}$ es cerrado bajo composición de
operadores, la composición es asociativa, y $\Delta_1=\mathrm{id}$ es la unidad.
Explícitamente:
$$\Delta_\mu\circ\Delta_\nu = \Delta_{\nu\mu}=\Delta_{\mu\nu},\qquad
\Delta_\mu\circ T_h = T_{h(\mu\,\cdot,\,\cdot)},\qquad
T_h\circ\Delta_\mu = T_{h(\cdot,\,\mu^{-1}\cdot)},$$
$$T_h\circ T_k = T_{h\bullet k},\qquad
(h\bullet k)(x,z) := \int_G h(x,y)\,k(y,z)\,d^*y\ \in C_c^\infty(G\times G).$$

*Demostración.* Las cuatro fórmulas: cálculo directo —
$(\Delta_\mu T_h f)(x) = (T_hf)(\mu x) = \int h(\mu x,y)f(y)d^*y$;
$(T_h\Delta_\mu f)(x) = \int h(x,y)f(\mu y)d^*y = \int h(x,\mu^{-1}u)f(u)d^*u$
(invariancia de Haar); $(T_hT_kf)(x) = \int h(x,y)\int k(y,z)f(z)\,d^*z\,d^*y$ y
Fubini (integrandos continuos de soporte compacto) da $T_{h\bullet k}$; $h\bullet k$
es $C^\infty$ (derivación bajo la integral con dominación en compactos) y de soporte
compacto (proyecciones de soportes compactos). Cerradura: los cuatro tipos de
producto caen en $\mathrm{Corr}$. Asociatividad: es composición de operadores sobre
$C_c^\infty(G)$, asociativa por definición; por el Lema 2.3 los núcleos resultantes
están unívocamente determinados, así que la asociatividad vale también a nivel de
núcleos. Unidad: $\Delta_1 f = f$. $\square$

**Observación 2.5 (dónde quedó el Doc 125).** Las $\Delta_\mu$ son exactamente las
correspondencias del flujo de escala del Doc 125 §2.4, ahora con composición exacta
$\Delta_\mu\circ\Delta_\nu=\Delta_{\mu\nu}$ para **todo** $\mu,\nu$ (sin la
restricción $\lambda\lambda'\notin\mathbb{Q}$ de 1502.05580: el precio es trabajar
sobre $G$ completo y no sobre un cociente). La estructura discreta $\mathcal{K}_2$
de §1.1 se inyecta por $K\mapsto$ pesos sobre los puntos $(m,n)$; el puente
continuo↔discreto es el núcleo engrosado de §3.

**[DEFINICIÓN-NUEVA 2.6] (involución de correspondencias).** Para
$h\in C_c^\infty(G^2)$: $\tilde h(x,y) := \overline{h(1/x,1/y)}\,(xy)^{-1}$; para
traslaciones: $\widetilde{\Delta_\mu} := \Delta_{\mu}$ (el grafo $\{y=\mu x\}$ es
estable bajo $(x,y)\mapsto(1/y,1/x)$ — la transpuesta-reflejada). Extensión
antilineal a $\mathrm{Corr}$.

### 2.3. El funtor de involución $\sigma$ y los objetos hermitianos

**[DEFINICIÓN-NUEVA 2.7].** $\sigma:\mathcal{A}rith\to\mathcal{A}rith$:
$$\sigma(a,c,\omega) := \bigl(\bar a,\ \textstyle\sum_j \bar c_j\,[\,1-\bar s_j\,],\ \omega\bigr),
\qquad \sigma(T):=\widetilde{T}.$$

**[PROPOSICIÓN 2.8].** (a) $\sigma^2=\mathrm{id}$. (b) Para todo objeto $X$ y todo
test $f$: $W_{\sigma X}(f) = \overline{W_X(\tilde f)}$. (c) Si $X$ es **hermitiano**
($\sigma X = X$, i.e. $a$ real, $c$ estable bajo $s\mapsto1-\bar s$ con pesos
conjugados, $\omega$ real), entonces
$$Q_X(f_1,f_2) := W_X(f_1\star\tilde f_2)$$
es una forma hermitiana sobre $C_c^\infty(G)$: $Q_X(f_2,f_1)=\overline{Q_X(f_1,f_2)}$.

*Demostración.* (a) Inmediato sobre los datos ($1-\overline{(1-\bar s)}=s$).
(b) Bloque a bloque. Polar: $\widehat{\tilde f}(s)=\overline{\hat f(1-\bar s)}$ da
$\overline{D_c(\tilde f)} = \sum\bar c_j\,\hat f(1-\bar s_j) = D_{\sigma c}(f)$.
Discreto: $\tilde f(n) = \overline{f(1/n)}\,n^{-1}$ y
$n^{-1}\tilde f(1/n) = n^{-1}\overline{f(n)}\cdot n\cdot n^{-1}
= \overline{f(n)}\,n^{-1}$… cálculo directo:
$\overline{P_a(\tilde f)} = \sum_n[\bar a(n)\,\overline{\tilde f(n)} +
a(n)\,n^{-1}\overline{\tilde f(1/n)}]$ con $\overline{\tilde f(n)} = f(1/n)n^{-1}$ y
$\overline{\tilde f(1/n)} = f(n)\cdot n$: queda
$\sum_n[\,a(n)f(n) + \bar a(n)n^{-1}f(1/n)\,]$ con $a\mapsto\bar a$ — exactamente
$P_{\bar a}(f)$. Arquimediano: $\widehat{\tilde f}(\tfrac12+it) =
\overline{\hat f(\tfrac12+it)}$ y $\omega$ par real. (c) De (b) con $\sigma X=X$:
$\overline{Q_X(f_1,f_2)} = \overline{W_X(f_1\star\tilde f_2)} =
W_X(\widetilde{f_1\star\tilde f_2}) = W_X(\tilde f_1\star f_2) = Q_X(f_2,f_1)$,
usando $\widetilde{(u\star v)} = \tilde u\star\tilde v$ y
$\tilde{\tilde u}=u$ (cálculo directo en $G$). $\square$

**Observación 2.9 ($\sigma$ es la involución $\rho\mapsto1-\bar\rho$ como funtor).**
Sobre los objetos espectrales de §4, $\sigma$ actúa sobre el divisor exactamente por
$\rho\mapsto1-\bar\rho$ (Prop. 4.2(b)). El pedido del encargo — "la involución como
funtor" — queda cumplido en el nivel correcto: $\sigma$ está definida sobre **datos
aritméticos**, y la acción sobre ceros es un teorema, no una definición.

---

## 3. El grado de una correspondencia es el lado casi-primo

### 3.1. Núcleos engrosados y el grado

**[DEFINICIÓN-NUEVA 3.1].** Núcleo engrosado (Doc 107 Def. 3.2):
$h_{g,\varphi}(x,y) := g(xy)\,\varphi(x/y)$, $g,\varphi\in C_c^\infty(G)$. Para un
objeto $X$, el **grado** (o traza de intersección) de una correspondencia
$h\in C_c^\infty(G^2)$ es
$$\deg_X(h) \;:=\; (W_X\otimes W_X)(h),$$
donde $W_X\otimes W_X$ se define por la **expansión aritmética de nueve bloques**:
$(D_c-P_a-A_\omega)^{(1)}\otimes(D_c-P_a-A_\omega)^{(2)}$ aplicada a $h$, cada bloque
con la fórmula del Doc 107 §2.3 con $\Lambda\to a$ (más los términos espejo
$\bar a(n)\,n^{-1}$ en $1/n$), $\{0,1\}\to\{s_j\}$ con pesos $c_j$, $\Omega\to\omega$.
Cada bloque es una suma finita o integral absolutamente convergente: **el grado está
definido para TODO objeto de $\mathcal{A}rith$ y no menciona ceros de nada.**

**[PROPOSICIÓN 3.2] (buena definición e iteración).** Para todo $X$ y todo
$h\in C_c^\infty(G^2)$, $\deg_X(h) = W_X^{(1)}[x\mapsto W_X^{(2)}[h(x,\cdot)]]$, y la
rebanada $x\mapsto W_X^{(2)}[h(x,\cdot)]$ está en $C_c^\infty(G)$. En particular
$\deg_X$ es simétrico en el orden de iteración.

*Demostración.* Idéntica al Lema 2.2(a)(c) del Doc 107 con datos generales: el
bloque discreto de la rebanada es una suma finita de evaluaciones
$h(x,n),\,h(x,1/n)$ ($C_c^\infty$ en $x$); el polar, evaluaciones de Mellin
parciales (enteras en $s$, $C_c^\infty$ en $x$ por derivación bajo la integral); el
arquimediano, integral con decaimiento rápido uniforme (Paley–Wiener con parámetro,
Doc 107 Lema 1.2: la prueba usa solo soporte compacto y suavidad, no nada de ζ).
Expandir la iteración da los nueve bloques; la simetría es la simetría manifiesta de
la expansión. $\square$

### 3.2. El teorema casi-primo general

**[TEOREMA 3.3] (el lado casi-primo es el grado, para toda función aritmética).**
Sea $X=(a,c,\omega)$ y $h=h_{g,\varphi}$. El bloque discreto$\times$discreto de
$\deg_X(h)$ es
$$P\!\otimes\!P(h) = \Sigma_{\mathrm{I}}+\Sigma_{\mathrm{II}}+\Sigma_{\mathrm{III}}
+\Sigma_{\mathrm{IV}},\qquad
\boxed{\ \Sigma_{\mathrm{I}} = \sum_{N\ge1} g(N)\,\bigl(a\star_\varphi a\bigr)(N),\quad
(a\star_\varphi a)(N) := \sum_{d\mid N} a(d)\,a(N/d)\,\varphi\!\left(\frac{d^2}{N}\right),}$$
y $\Sigma_{\mathrm{II,III,IV}}$ son las sumas finitas espejo del Doc 107 Teorema 4.2
con $\Lambda(n_i)\to a(n_i)$ o $\overline{a(n_i)}$ según la ranura reflejada y pesos
$n_i^{-1}$ correspondientes. Todas las sumas son finitas (soporte compacto de $g$ y
$\varphi$).

*Demostración.* Sustituir $h(n_1,n_2)=g(n_1n_2)\varphi(n_1/n_2)$ y las tres
evaluaciones reflejadas en el bloque (4) de la expansión; para $\Sigma_{\mathrm I}$,
agrupar por $N=n_1n_2$: la pareja $(n_1,n_2)$ con $n_1n_2=N$ recorre los divisores
$d=n_1$ de $N$, con $n_1/n_2 = d^2/N$. Es el mismo cálculo del Doc 107 Teorema 4.2,
que nunca usó $\Lambda$ más que como coeficiente: la identidad es válida para
$a$ arbitraria. La finitud: solo los $N$ (resp. los $n_1n_2$, etc.) en los soportes
compactos contribuyen. $\square$

**Observación 3.4 (NC2 por construcción — el punto de diseño).** En el Doc 107, la
autonomía del lado casi-primo fue un **hallazgo** (Teorema 4.4: los términos mixtos
se reabsorben). Acá es un **axioma realizado**: $\deg_X$ se define por la expansión
aritmética, para todo objeto; el enunciado "$\deg_X$ no menciona ceros" no se
verifica — es la definición. La sobregeneración del test R-NC (Doc 119, NC2) queda
incorporada: cualquier teorema sobre $\deg$ probado en §4–§6 cuantifica sobre todas
las funciones aritméticas, y ζ entra como el punto $a=\Lambda$. El costo de diseño,
declarado: la igualdad $\deg_X = $ suma doble de ceros es ahora un **teorema con
hipótesis** (§4.7), no una definición — la dificultad no desaparece, cambia de
lugar; §7 hace el balance.

---

## 4. Objetos espectrales: la subcategoría $\mathcal{A}rith^{EF}$

### 4.1. Definición y el funtor de comparación

**[DEFINICIÓN-NUEVA 4.1].** Un **objeto espectral** es un par $(X,Z)$ con
$X\in\mathcal{A}rith$ y $Z$ un multiconjunto numerable de $\mathbb{C}$ (el
**divisor**), con partes reales acotadas y función de conteo
$N_Z(T):=\#\{\rho\in Z:|\mathrm{Im}\,\rho|\le T\} \ll T^{A}$ para algún $A<\infty$,
tal que vale la **fórmula explícita**:
$$\sum_{\rho\in Z}\hat f(\rho) \;=\; W_X(f)\qquad\text{para todo } f\in C_c^\infty(G),$$
con convergencia absoluta del lado izquierdo (automática: Paley–Wiener da
$|\hat f(\rho)|\ll_N(1+|\mathrm{Im}\,\rho|)^{-N}$ uniformemente en bandas, y
$N_Z(T)\ll T^A$; Doc 107 Lema 1.2, mismo argumento). $\mathcal{A}rith^{EF}$ es la
categoría de tales pares; el **funtor de comparación**
$U:\mathcal{A}rith^{EF}\to\mathcal{A}rith$ olvida $Z$.

**[DATO].** $(\zeta_{\mathrm{ob}}, Z_\zeta)$ con $Z_\zeta$ = ceros no triviales de ζ
es un objeto espectral: es el Teorema 1.4 del Doc 107 (Weil 1952). Lo mismo para
toda $L$ de Dirichlet, y para Davenport–Heilbronn (la fórmula explícita de una
combinación lineal de $L$'s con la misma ecuación funcional se obtiene por el mismo
contorno; su divisor es el conjunto de ceros de $D$).

**[PROPOSICIÓN 4.2].** (a) El divisor de un objeto espectral está determinado por
$X$ en el siguiente sentido: si $(X,Z)$ y $(X,Z')$ son espectrales, entonces
$\sum_{Z}\hat f(\rho)=\sum_{Z'}\hat f(\rho)$ para todo $f$. (b) Si $(X,Z)$ es
espectral, $(\sigma X,\,\sigma Z)$ es espectral con
$\sigma Z := \{1-\bar\rho:\rho\in Z\}$. En particular, si $X$ es hermitiano, $Z$ es
$\sigma$-estable como multiconjunto **si** el par espectral con divisor $\sigma Z$
coincide con el de $Z$ en el sentido (a); para los objetos del catálogo (ζ, L de
Dirichlet hermitianas, D–H, $F_{p,\alpha}$) la $\sigma$-estabilidad del divisor vale
con igualdad de multiconjuntos [DATO: ecuación funcional + reflexión de Schwarz].

*Demostración.* (a) Ambos iguales a $W_X(f)$. (b) Por la Prop. 2.8(b):
$W_{\sigma X}(f) = \overline{W_X(\tilde f)} = \overline{\sum_Z\widehat{\tilde f}(\rho)}
= \overline{\sum_Z \overline{\hat f(1-\bar\rho)}} = \sum_{\sigma Z}\hat f(\rho)$;
las cotas de densidad y banda se preservan. $\square$

*(Declaración honesta: no afirmo unicidad puntual del multiconjunto $Z$ a partir del
funcional — la categoría **porta** el divisor como dato, no lo reconstruye; esa es
exactamente la decisión de diseño que §7 discute contra el Doc 110.)*

### 4.2. El lema de evaluación

**[LEMA 4.3] (evaluación).** Sean $s_1,\dots,s_k\in\mathbb{C}$ distintos. El mapa
$\mathrm{ev}:C_c^\infty(G)\to\mathbb{C}^k$, $f\mapsto(\hat f(s_1),\dots,\hat f(s_k))$,
es sobreyectivo.

*Demostración.* Si no, existe $\lambda\ne0$ con $\sum_j\lambda_j\hat f(s_j)=0$ para
todo $f$, i.e. $\int_0^\infty f(x)\bigl[\sum_j\lambda_j x^{s_j-1}\bigr]dx=0$ para
todo $f\in C_c^\infty$; la función continua $\sum_j\lambda_j x^{s_j-1}$ es entonces
idénticamente nula en $(0,\infty)$. Con $x=e^u$: $\sum_j\lambda_j e^{(s_j-1)u}=0$
para todo $u\in\mathbb{R}$; aplicando $(d/du)^m$ en $u=0$:
$\sum_j\lambda_j(s_j-1)^m=0$ para todo $m\ge0$ — un sistema de Vandermonde en los
$k$ valores distintos $s_j-1$, de rango $k$: $\lambda=0$, contradicción. $\square$

### 4.3. El teorema de órbitas: la signatura de todo bloque

**[TEOREMA 4.4] (órbitas y signatura, para toda la categoría).** Sea $(X,Z)$
espectral hermitiano con $Z$ $\sigma$-estable (multiplicidades $m_\rho =
m_{\sigma\rho}\in\mathbb{Z}_{\ge1}$). Entonces:

(a) Para todo $f$: $Q_X(f,f) = \sum_{\rho\in Z} m_\rho\,\hat f(\rho)\,
\overline{\hat f(\sigma\rho)}$ (absolutamente convergente).

(b) Sea $S\subseteq Z$ finito y $\sigma$-estable, $S = S_{\mathrm{on}}\sqcup
S_{\mathrm{orb}}$ con $S_{\mathrm{on}}$ los puntos fijos de $\sigma$ (i.e.
$\mathrm{Re}\,\rho=\tfrac12$) y $S_{\mathrm{orb}}$ unión de $n_{\mathrm{orb}}$
órbitas libres $\{\rho,\sigma\rho\}$. La forma hermitiana de bloque
$$B_S(v,v) := \sum_{\rho\in S} m_\rho\,v_\rho\,\overline{v_{\sigma\rho}},
\qquad v\in\mathbb{C}^S,$$
tiene signatura exactamente
$$\mathrm{sig}(B_S) = \bigl(\,\#S_{\mathrm{on}} + n_{\mathrm{orb}},\ \ n_{\mathrm{orb}}\,\bigr),$$
y por el Lema 4.3 se realiza con rango completo sobre la clase de prueba (el mapa de
evaluación sobre $S$ es sobreyectivo).

(c) Si $Z$ es finito, $\mathrm{sig}(Q_X) = (\#Z_{\mathrm{on}}+n_{\mathrm{orb}},\,
n_{\mathrm{orb}})$ exactamente (como forma sobre $C_c^\infty(G)/\ker$).

*Demostración.* (a) $Q_X(f,f) = W_X(f\star\tilde f) = \sum_Z m_\rho\,
\widehat{f\star\tilde f}(\rho)$ y $\widehat{f\star\tilde f}(\rho) =
\hat f(\rho)\overline{\hat f(1-\bar\rho)} = \hat f(\rho)\overline{\hat f(\sigma\rho)}$.
(b) Descomposición ortogonal por órbitas: para $\rho$ fijo ($\sigma\rho=\rho$), el
término es $m_\rho|v_\rho|^2$: dirección positiva. Para una órbita libre
$\{\rho,\rho'\}$ ($\rho'=\sigma\rho\ne\rho$): los dos términos son
$m(v_\rho\bar v_{\rho'} + v_{\rho'}\bar v_\rho) = 2m\,\mathrm{Re}(v_\rho\bar v_{\rho'})$
— el plano hiperbólico, autovalores $\pm m$: signatura $(1,1)$. Sumando:
$(\#S_{\mathrm{on}}+n_{\mathrm{orb}},\,n_{\mathrm{orb}})$. La realización: por el
Lema 4.3 existe, para cada $v\in\mathbb{C}^S$, un $f$ con $\hat f|_S=v$ (y nada se
exige fuera de $S$). (c) Con $Z$ finito, $Q_X(f,f)=B_Z(\mathrm{ev}f,\mathrm{ev}f)$ y
$\mathrm{ev}$ es sobreyectiva: la forma inducida en el cociente es exactamente
$B_Z$. $\square$

**[COROLARIO 4.5] (la desigualdad universal de la categoría).** Para todo objeto
espectral hermitiano de divisor finito, $\mathrm{sig}(Q_X)=(p,q)$ satisface
$$q \;\le\; p,$$
con igualdad si y solo si el divisor no toca la línea crítica; y $q=0$ si y solo si
$Z\subset\{\mathrm{Re}=\tfrac12\}$. Lo mismo vale bloque a bloque para divisores
infinitos. **A lo sumo la mitad de las direcciones de cualquier bloque son
negativas, para cualquier función aritmética**: es la huella universal de la
involución $\sigma$, no de ζ. $\square$

### 4.4. Realización y clasificación

**[TEOREMA 4.6] (clasificación de signaturas alcanzables).** El mapa
$$\{\text{objetos espectrales hermitianos de divisor finito}\}\ \longrightarrow\
\{(p,q)\in\mathbb{Z}_{\ge0}^2\},\qquad X\mapsto\mathrm{sig}(Q_X),$$
tiene imagen exactamente $\{(p,q): q\le p\}$.

*Demostración.* "$\subseteq$": Corolario 4.5. "$\supseteq$": dados $q\le p$, sea
$Z := \{\tfrac12+i,\dots,\tfrac12+i(p-q)\}\cup\{\tfrac12\pm\delta+i\gamma_j:
j=1..q\}$ (con $\delta\in(0,\tfrac12)$, alturas $\gamma_j$ distintas, y agregando
los conjugados si se quiere realidad — irrelevante para la cuenta: cada cuádruple
agrega órbitas libres y se ajusta el conteo; tomemos la versión mínima con pares
$\{\tfrac12+\delta+i\gamma_j,\ \tfrac12-\delta+i\gamma_j\}$, que ya es
$\sigma$-estable). El objeto $X_Z=(0,\sum_{\rho\in Z}[\rho],0)$ es hermitiano
(el bloque polar es $\sigma$-estable con pesos 1) y espectral con divisor $Z$
(trivialmente: $W_{X_Z}(f)=\sum_Z\hat f(\rho)$ es la definición). Tiene
$\#Z_{\mathrm{on}}=p-q$ puntos fijos y $q$ órbitas libres: signatura
$(p-q+q,\,q)=(p,q)$ por el Teorema 4.4(c). $\square$

**Observación.** La realización usa que en $\mathcal{A}rith$ el bloque polar admite
puntos arbitrarios: los "ceros" de los objetos artificiales son átomos polares. Esto
no es trampa — es el contenido: **la categoría es genuinamente más grande que las
funciones L**, y los teoremas de §4 valen en toda esa amplitud. Lo que distingue a
los objetos de tipo L es la estructura del dato $a$ (§1.2, §6.7), no la signatura.

### 4.5. La identidad del índice tensorial (importación del Doc 106)

**[TEOREMA 4.8] (índice tensorial).** Sean $A$, $B$ formas hermitianas no
degeneradas de signaturas $(p_1,q_1)$, $(p_2,q_2)$ sobre espacios de dimensión
finita $V,W$. Entonces $A\otimes B$ sobre $V\otimes W$ tiene signatura
$$\mathrm{sig}(A\otimes B) = \bigl(p_1p_2+q_1q_2,\ \,p_1q_2+q_1p_2\bigr).$$

*Demostración.* Por Sylvester, hay bases en que $A=\mathrm{diag}(\epsilon_i)$,
$B=\mathrm{diag}(\eta_j)$ con $\epsilon_i,\eta_j\in\{\pm1\}$. En la base
$e_i\otimes f_j$, $A\otimes B = \mathrm{diag}(\epsilon_i\eta_j)$: el número de
productos $+1$ es $p_1p_2+q_1q_2$ y el de $-1$ es $p_1q_2+q_1p_2$. La signatura es
invariante de la forma (ley de inercia). $\square$

**Consecuencia en la categoría.** Para un bloque off de un cuádruple ($m=1$:
signatura $(2,2)$), el cuadrado tensorial tiene índice negativo
$2\cdot2+2\cdot2=8=(4m)^2/2$ — la Prop. 3.5 del Doc 106 y el Teorema 5.5 del
Doc 107 (signatura $(8,8)$), ahora como instancia de un teorema de álgebra lineal
de la categoría, válido para el bloque off de **cualquier** objeto espectral
hermitiano. La realización analítica del cuadrado (el funcional doble sobre núcleos
engrosados, con $\hat g$ en la suma y $\hat\varphi$ en la diferencia) se hereda
del Doc 107 §3 sin cambios: el cálculo del Mellin doble (Teorema 3.4 allí) no usa
ζ.

### 4.6. La fórmula explícita doble para objetos espectrales

**[TEOREMA 4.9].** Si $(X,Z)$ es espectral, para todo $h\in C_c^\infty(G^2)$:
$$\deg_X(h) \;=\; \sum_{\rho_1\in Z}\sum_{\rho_2\in Z}\hat h(\rho_1,\rho_2),$$
con convergencia absoluta de la suma doble.

*Demostración.* Como en Doc 107 Lema 2.2(b): por la Prop. 3.2,
$\deg_X(h) = W_X^{(1)}[F]$ con $F(x)=W_X^{(2)}[h(x,\cdot)]\in C_c^\infty$; aplicando
la fórmula explícita (Def. 4.1) en la variable 1:
$\deg_X(h) = \sum_{\rho_1}\hat F(\rho_1)$, y
$\hat F(\rho_1) = W_X^{(2)}[x_2\mapsto\int h(x_1,x_2)x_1^{\rho_1-1}dx_1] =
\sum_{\rho_2}\hat h(\rho_1,\rho_2)$ — el intercambio
$\int dx_1\leftrightarrow W^{(2)}$ es legítimo bloque a bloque (sumas finitas e
integrales absolutamente convergentes sobre compactos). La convergencia absoluta
doble: Paley–Wiener en dos variables + $N_Z(T)\ll T^A$ en cada factor. $\square$

---

## 5. El índice de juguete como teorema de la categoría

### 5.1. Estructuras de intersección

**[DEFINICIÓN-NUEVA 5.1].** Una **estructura de intersección de rango 3 y género
$g\in\mathbb{R}_{\ge0}$** sobre un objeto $X$ es una forma $\mathbb{R}$-bilineal
simétrica $(\,\cdot\,)$ sobre el retículo $N_X := \mathbb{Z}f_1\oplus\mathbb{Z}f_2
\oplus\mathbb{Z}\Delta$ de clases de correspondencias (fibras y diagonal) con los
axiomas:
**(I1)** $f_1^2=f_2^2=0$; **(I2)** $f_1\!\cdot\!f_2=1$; **(I3)**
$\Delta\!\cdot\!f_1=\Delta\!\cdot\!f_2=1$; **(I4)** $\Delta^2=2-2g$ (adjunción).
*(Las propiedades que el Doc 125 computó en el juguete tropical — §4 allí — son acá
los axiomas; el teorema dice qué fuerzan.)*

**[TEOREMA 5.3] (índice de juguete, general).** Sea $(\,\cdot\,)$ una estructura de
intersección de género $g$ sobre cualquier objeto. Entonces su matriz de Gram en
$(f_1,f_2,\Delta)$ es $G_g=\begin{pmatrix}0&1&1\\1&0&1\\1&1&2-2g\end{pmatrix}$, con
$\det G_g = 2g$, y:

(a) Si $g\ge1$ (de hecho si $g>0$): signatura $(1,2)$; la clase $H=f_1+f_2$ cumple
$H^2=2>0$; y sobre el primitivo $H^\perp$ la forma es **definida negativa**, con
matriz $\mathrm{diag}(-2,-2g)$ en la base $e_1=f_1-f_2$, $e_2=f_1+f_2-\Delta$.

(b) Si $g=0$: la forma es degenerada, con radical generado por $e_2=f_1+f_2-\Delta$
y signatura $(1,1,0)$ (una positiva, una negativa, una nula). **El índice de Hodge
falla exactamente en género 0.**

*Demostración.* Gram: (I1)–(I4). Determinante:
$\det G_g = 0\cdot[0(2-2g)-1] - 1\cdot[(2-2g)-1] + 1\cdot[1-0] = -(1-2g)+1 = 2g$.
(a) $g>0$: $\det>0$; el menor $2\times2$ superior $\begin{psmallmatrix}0&1\\1&0
\end{psmallmatrix}$ tiene determinante $-1<0$, luego la forma es indefinida; una
forma simétrica $3\times3$ real no degenerada con $\det>0$ tiene signatura $(3,0)$ o
$(1,2)$; indefinida $\Rightarrow(1,2)$. $H^2=(1,1,0)G_g(1,1,0)^T = 2$.
Primitivo: $G_gH = (1,1,2)^T$, condición $x_1+x_2+2x_3=0$; base $e_1=(1,-1,0)$,
$e_2=(1,1,-1)$. $G_ge_1 = (-1,1,0)^T$, $e_1^TG_ge_1=-2$;
$G_ge_2 = (0,\,0,\,2g)^T$ (tercera entrada: $1+1-(2-2g)=2g$), $e_2^TG_ge_2 = -2g$;
$e_1^TG_ge_2 = 0$. Forma primitiva $\mathrm{diag}(-2,-2g)$: definida negativa
$\iff g>0$. (b) $g=0$: $G_0e_2 = 0$ (el cálculo de arriba con $g=0$), radical
$\ni e_2$; en el cociente quedan $f_1,f_2$ con forma
$\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$: signatura $(1,1)$. $\square$

### 5.2. Qué clase de objetos la realiza

**[DEFINICIÓN-NUEVA 5.4].** Un objeto $X=(a,c,\omega)$ es **periódico de período
$L$** si su dato discreto vive en una progresión geométrica: $a$ soportada en
$\{p^m\}$ con $L=\log p$ (objetos "de un primo"; más en general, soporte en
$e^{L\mathbb{Z}}$). Su grupo de escala efectivo es $C_L := G/e^{L\mathbb{Z}}$, un
círculo; sus correspondencias efectivas viven en el toro $C_L\times C_L$, con las
clases $f_1$ (horizontal), $f_2$ (vertical), $\Delta=\Delta_1$ y las traslaciones
$\Delta_\mu$ (Doc 125 §2.4).

**[CONSTRUCCIÓN 5.5] (realización en género 1; estatus: importa el cómputo tropical
del Doc 125, verificado allí con doble chequeo).** Para un objeto periódico, la
intersección estable de Allermann–Rau sobre $C_L\times C_L$ (Doc 125 §3.1, [DATO
arXiv:0709.3705]) define una estructura de intersección sobre
$N_X=\langle f_1,f_2,\Delta\rangle$ con (I1)–(I3) y $\Delta^2=0$, i.e. **género
$g=1$** (Doc 125 §4: homología del toro y adjunción tropical coinciden). Por el
Teorema 5.3(a): signatura $(1,2)$, primitivo $\mathrm{diag}(-2,-2)$ definido
negativo. **La signatura $(1,2)$ del Doc 125 no es un hecho sobre ζ ni sobre el
primo $p$: es el teorema 5.3 evaluado en $g=1$, válido para coeficientes $a$
arbitrarios del objeto periódico.** La dependencia de $p$ es solo la escala global
$\log p$ (que no cambia signaturas).

**Observación 5.6 (la traba heredada, declarada).** Lo que NO se importa: (i) el
paso a la red infinita de correspondencias $\Delta_\mu$ (densidad de pendientes,
realidad del número de intersección — G-125.A) y (ii) la persistencia de la
signatura en rango infinito (Babaee–Huh — G-125.B). El Teorema 5.3 es de rango 3;
su valor categórico es separar el contenido (la signatura es consecuencia formal de
(I1)–(I4) con $g\ge1$) del muro (extender (I1)–(I4) a la red completa con dos primos
inconmensurables). El muro queda en §9 como objetivo nombrado.

**Observación 5.7 (género 0 y Spec ℤ).** El RR de Connes–Consani da género 0 para
$\mathrm{Spec}\,\mathbb{Z}$ (Doc 124 §3.3, vía [DATO arXiv:2307.06748]). En la
categoría, el Teorema 5.3(b) dice qué significa eso: **en género 0 la forma de
intersección de rango 3 es degenerada y no hay índice de Hodge que leer.** El
objeto que porta una estructura de intersección útil debe tener género $\ge1$ — los
bloques periódicos lo tienen ($g=1$); el problema de ensamblar los bloques (un
objeto global de género infinito) es la forma categórica del gap MW-5/L6.

---

## 6. El Axioma H

### 6.1. Enunciado

**[DEFINICIÓN-NUEVA 6.1] (Axioma H).** Un objeto hermitiano $X=(a,c,\omega)$
**satisface H** si
$$Q_X(f,f) \;=\; W_X(f\star\tilde f)\;\ge\;0\qquad\text{para todo }f\in C_c^\infty(G).$$
El enunciado usa solo los datos $(a,c,\omega)$: **no menciona ceros de nada** —
$W_X$ es la suma finita/integral de la Definición 2.1. Versión de dos variables
(**H₂**): $\deg_X(h\star_{\!G^2}\tilde h)\ge0$ para todo núcleo engrosado $h$.

**[PROPOSICIÓN 6.2] (H desde la línea; toda la categoría).** Si $(X,Z)$ es
espectral hermitiano con $Z\subset\{\mathrm{Re}\,s=\tfrac12\}$, entonces $X$
satisface H y H₂.

*Demostración.* Teorema 4.4(a): $Q_X(f,f) = \sum_Z m_\rho\hat f(\rho)
\overline{\hat f(\sigma\rho)}$ y $\sigma\rho=\rho$ sobre la línea: $Q_X(f,f) =
\sum m_\rho|\hat f(\rho)|^2\ge0$. Para H₂: Teorema 4.9 con
$\widehat{h\star\tilde h}(\rho_1,\rho_2) = \hat h(\rho_1,\rho_2)
\overline{\hat h(\sigma\rho_1,\sigma\rho_2)} = |\hat h(\rho_1,\rho_2)|^2$. $\square$

**[TEOREMA 6.3] (H por bloques; recíproca incondicional a nivel de bloque).** Si
$(X,Z)$ es espectral hermitiano y $Z$ contiene algún $\rho_0$ con
$\mathrm{Re}\,\rho_0\ne\tfrac12$, entonces **toda** forma de bloque $B_S$ con
$S\supseteq\{\rho_0,\sigma\rho_0\}$ es indefinida (tiene una dirección negativa
realizada sobre la clase de prueba). Es decir: la versión por bloques de H
("$B_S\ge0$ para todo bloque finito $\sigma$-estable") **equivale** a
$Z\subset\{\mathrm{Re}=\tfrac12\}$, incondicionalmente, para todo objeto de
$\mathcal{A}rith^{EF}$.

*Demostración.* Teorema 4.4(b): la órbita libre $\{\rho_0,\sigma\rho_0\}$ aporta un
plano hiperbólico; el Lema 4.3 realiza el vector $(v_{\rho_0},v_{\sigma\rho_0}) =
(1,-1)$, sobre el cual $B = -2m_{\rho_0}<0$. La equivalencia: Prop. 6.2 +
esto. $\square$

*(La relación H $\Rightarrow$ H-por-bloques en general — i.e. que la negatividad de
un bloque se transporte a una negatividad del funcional completo contra la marea
positiva del resto del divisor — es la separación tipo "Hipótesis D" del programa
(P35; Doc 96 Teorema 8.1): probada abajo para divisores de retícula (§6.5) y
finitos; declarada como [PUENTE] en general. Esta honestidad importa en §6.6.)*

### 6.2. Verificación 1: la función constante

**[PROPOSICIÓN 6.4].** $X_1$ ($a\equiv1$, $c=0$, $\omega=0$) **no** satisface H.

*Demostración.* Para $f$ real, $g:=f\star\tilde f$ cumple $g(1/x) =
\overline{g(x)}\,x$ (hermitianidad de $g$: $\tilde g=g$), luego
$n^{-1}g(1/n)=\overline{g(n)}$ y
$Q_{X_1}(f,f) = -\sum_{n\ge1}\bigl[g(n)+\overline{g(n)}\bigr]
= -2\sum_{n\ge1}\mathrm{Re}\,g(n).$
Tomar $f\ge0$ real, $f\not\equiv0$, con soporte en $[\tfrac12,3]$ (ancho mayor que
una octava): $g(n) = \int f(y)\,f(y/n)\,(y/n)\,d^*y\ \ge 0$ para todo $n$, y
$g(1) = \int f(y)^2\,y\,d^*y > 0$. Entonces $Q_{X_1}(f,f)\le -2g(1)<0$. $\square$

### 6.3. Verificación 2: completamente multiplicativas y la masa diagonal

**[PROPOSICIÓN 6.5] (masa diagonal).** Sea $X=(a,0,0)$ hermitiano con $a(1)=0$ y
$a\not\equiv0$. Entonces $X$ no satisface H. En particular, **ningún** objeto
$X_h$ ($a = h\Lambda$, $h$ completamente multiplicativa con valores $\pm1$ —
aleatoria o no) satisface H: la falla es determinista, para toda $h$.

*Demostración.* Sea $n_0\ge2$ mínimo con $a(n_0)\ne0$ ($a$ real por hermitiano).
Tomar $u\ge0$ bump real con soporte en $[e^{-\epsilon},e^{\epsilon}]$,
$\epsilon<\tfrac14\log n_0$ (más pequeño que cualquier separación logarítmica
relevante), y $f := u + \tau\,u(\cdot/n_0)$ con $\tau\in\mathbb{R}$. Entonces
$g=f\star\tilde f$ satisface: $g(n)=0$ salvo para $n$ tal que $\log n$ está a
distancia $<2\epsilon$ de $\{0,\pm\log n_0\}$; los enteros así alcanzados son a lo
sumo $n=1$ y $n=n_0$ (y $1/n_0$, que entra por el término espejo). Cálculo de los
valores (peso $(y/x)$ del núcleo $g(x)=\int f(y)\overline{f(y/x)}(y/x)\,d^*y$):
$g(1) = \int|f|^2y\,d^*y = (1+O(\epsilon)) + \tau^2 n_0(1+O(\epsilon))$, pero el
coeficiente de $g(1)$ es $a(1)=0$: no contribuye. $g(n_0) =
\tau\int u(y/n_0)^2 (y/n_0)\,d^*y = \tau(1+O(\epsilon))$. Entonces
$Q_X(f,f) = -\,a(n_0)\bigl[g(n_0)+\overline{g(n_0)}\bigr] =
-2a(n_0)\tau(1+O(\epsilon))$, y eligiendo el signo de $\tau$ (=$\mathrm{sgn}\,
a(n_0)$, con $|\tau|$ pequeño para que el $O(\epsilon)$ no moleste) se obtiene
$Q_X<0$. Para $X_h$: $a(2)=h(2)\log2\ne0$. $\square$

**Lectura estructural.** H exige **masa positiva en la diagonal** (átomo en $x=1$,
bloque polar o densidad arquimediana): sin ella, cualquier coeficiente discreto no
nulo es una dirección negativa con fase a elección. En ζ, esa masa la ponen los
polos $[0]+[1]$ y $-\Omega$ (la densidad de ceros); en los objetos $F_{p,\alpha}$
de abajo, la pone $\omega\equiv-2\log p$. La positividad de Weil es siempre
"diagonal contra cruzados" — la categoría lo exhibe como dicotomía de datos.

### 6.4. La fórmula de Poisson para factores de Euler

**[TEOREMA 6.6] (fórmula explícita de Poisson, un factor).** Sean $p$ primo,
$L=\log p$, $\alpha\in\mathbb{C}^\times$, y $Z(\alpha) := \{s:p^s=\alpha\} =
\{\log_p\alpha + 2\pi ik/L : k\in\mathbb{Z}\}$ (una progresión vertical). Para todo
$f\in C_c^\infty(G)$:
$$\sum_{\rho\in Z(\alpha)}\hat f(\rho) \;=\; L\sum_{m\in\mathbb{Z}}\alpha^m f(p^m),$$
ambos lados absolutamente convergentes (izquierda: Paley–Wiener; derecha: suma
finita).

*Demostración.* Escribir $\alpha = p^\beta e^{i\phi}$ ($\beta=\log_p|\alpha|$),
$\rho_k = \beta+i(\phi+2\pi k)/L$. Con $x=e^t$ y $F(t) := f(e^t)\,e^{\beta t}
e^{i\phi t/L}\in C_c^\infty(\mathbb{R})$:
$\hat f(\rho_k) = \int F(t)\,e^{2\pi ikt/L}\,dt = \widehat F(2\pi k/L)$.
La fórmula de sumación de Poisson para $F\in C_c^\infty$ [DATO clásico; prueba:
serie de Fourier de la periodización $\sum_m F(t+mL)$, que es finita y $C^\infty$]:
$\sum_k\widehat F(2\pi k/L) = L\sum_m F(mL) = L\sum_m f(p^m)\,p^{\beta m}e^{i\phi m}
= L\sum_m \alpha^m f(p^m)$. $\square$

**[DEFINICIÓN-NUEVA / PROPOSICIÓN 6.6'].** El **objeto de Euler de un primo**
$F_{p,\alpha}$, para $1<|\alpha|<p$: el par espectral con divisor
$Z_F := Z(\alpha)\sqcup Z(p/\bar\alpha)$ y funcional
$$W_F(f) = L\sum_{m\in\mathbb{Z}} c_m\,f(p^m),\qquad c_m := \alpha^m+(p/\bar\alpha)^m.$$
Es un objeto de $\mathcal{A}rith^{EF}$, hermitiano, con datos: $a(p^m) = -L\,c_m$
para $m\ge1$ (y $\bar a$ en los espejos: consistente porque $c_{-m} = \bar c_m\,
p^{-m}$, cálculo directo), $c=0$, y el átomo $m=0$ ($c_0=2$) realizado como bloque
arquimediano $\omega\equiv-2L$ (Mellin inverso: $f(1) = \tfrac1{2\pi}\int
\hat f(\tfrac12+it)\,dt$). El divisor: dos progresiones verticales en
$\mathrm{Re}=\beta$ y $\mathrm{Re}=1-\beta$, $\sigma$-estable
($\sigma Z(\alpha) = Z(p/\bar\alpha)$: $1-\bar\rho$ con $p^{\bar\rho}=\bar\alpha$ da
$p^{1-\bar\rho}=p/\bar\alpha$), densidad lineal. La fórmula explícita es el
Teorema 6.6 sumado sobre los dos factores. Nótese: **$F_{p,\alpha}$ tiene producto
de Euler** en el sentido del Teorema 1.9 (su $a$ está soportada en potencias de un
primo), y su masa diagonal es arquimediana, como en ζ. $\square$

### 6.5. Verificación 3 — el teorema central: pureza local

**[TEOREMA 6.7] (pureza local: H es decidible en la subcategoría de un primo).**
Para $1<|\alpha|<p$:
$$F_{p,\alpha}\ \text{satisface H}\quad\Longleftrightarrow\quad |\alpha|=\sqrt p
\quad\Longleftrightarrow\quad |c_m|\le 2\,p^{m/2}\ \ \forall m\ge1.$$

*Demostración.* **($|\alpha|=\sqrt p\Rightarrow$H):** el divisor cae en
$\mathrm{Re}=\tfrac12$; Prop. 6.2. **(Las dos caracterizaciones de la derecha):**
si $|\alpha|=p^{1/2+\delta'}$, entonces $|c_m|\ge p^{m(1/2+\delta')} -
p^{m(1/2-\delta')} = p^{m/2}(p^{m\delta'}-p^{-m\delta'})$, que excede $2p^{m/2}$
para $m$ grande si $\delta'\ne0$; y si $\delta'=0$, $c_m = 2p^{m/2}
e^{im\phi}\cos(0)$… más precisamente $\alpha=\sqrt p\,e^{i\phi}$ implica
$p/\bar\alpha = \sqrt p\,e^{i\phi}=\alpha$ y $c_m=2\alpha^m$, $|c_m|=2p^{m/2}$.

**($|\alpha|\ne\sqrt p\Rightarrow\neg$H) — el test de Mertens de dos
protuberancias.** Sin pérdida $\delta'>0$ (si no, intercambiar $\alpha
\leftrightarrow p/\bar\alpha$, mismo objeto). Sea $M\ge1$ a fijar, $\epsilon <
L/4$, $u$ = bump real $\ge0$, $u(e^t) = \epsilon^{-1/2}\chi(t/\epsilon)$ con
$\chi$ par, $\int\chi^2=1$. Test: $f := u + \theta\,u(\cdot/p^{M})$ con
$\theta\in\mathbb{C}$. Sea $g=f\star\tilde f$, $g(x) = \int f(y)\overline{f(y/x)}
\,(y/x)\,d^*y$. Por soporte ($\epsilon<L/4$), $g(p^m)=0$ salvo $m\in\{0,\pm M\}$, y:
$$g(1) = \int|f|^2\,y\,d^*y = \bigl(1+|\theta|^2p^{M}\bigr)(1+O(\epsilon)),$$
$$g(p^{M}) = \theta\!\int u(y/p^M)^2\,(y/p^M)\,d^*y = \theta\,(1+O(\epsilon)),
\qquad g(p^{-M}) = \bar\theta\,p^{M}(1+O(\epsilon))$$
(la última: $\int u(y)\overline{\theta u(yp^{M}/p^{M})}\dots$ — cálculo directo, y
consistente con la hermitianidad $g(1/x)=\overline{g(x)}\,x$). Entonces, usando
$c_{-M}\,p^{M} = \bar c_M$:
$$Q_F(f,f) = L\bigl[c_0\,g(1) + c_M\,g(p^M) + c_{-M}\,g(p^{-M})\bigr]
= L\bigl[\,2\bigl(1+|\theta|^2p^{M}\bigr) + 2\,\mathrm{Re}(c_M\theta)\,\bigr]
(1+O(\epsilon)).$$
Elegir $\theta = -\,\overline{c_M}\,t/|c_M|$ con $t>0$:
$Q_F/L = \bigl[\,2 + 2p^{M}t^2 - 2|c_M|\,t\,\bigr](1+O(\epsilon))$. El mínimo en
$t^* = |c_M|/(2p^{M})$ vale $2 - |c_M|^2/(2p^{M})$, que es $<0$ en cuanto
$|c_M| > 2p^{M/2}$ — lo cual ocurre para $M$ suficientemente grande porque
$|c_M|\ge p^{M/2}(p^{M\delta'}-p^{-M\delta'})\to\infty\cdot p^{M/2}$. Fijar tal $M$,
luego $\epsilon$ suficientemente pequeño para absorber los $O(\epsilon)$:
$Q_F(f,f)<0$. $\square$

**Comentarios exactos.** (i) La barrera del test es **exactamente** $|c_m|\le
2p^{m/2}$: la cota de Ramanujan–pureza. En el caso puro la desigualdad
$2|\mathrm{Re}(c_M\theta)|\le 2(1+|\theta|^2p^M)$ es Cauchy–Schwarz exacta
($|c_M|=2p^{M/2}$): la positividad es tan justa como puede ser. (ii) El test es el
mecanismo de Mertens ($3+4\cos\theta+\cos2\theta$, dos frecuencias contra la masa
diagonal) en versión categórica: protuberancia en $1$ = masa diagonal,
protuberancia en $p^M$ con fase adversaria = coeficiente. (iii) **Consecuencia
estructural: el producto de Euler no implica H.** $F_{p,\alpha}$ con
$|\alpha|=p^{0.6}$ tiene producto de Euler (Teorema 1.9), ecuación funcional
(hermitiano), masa diagonal positiva — y viola H. El discriminador de H dentro de
los objetos de Euler es la **pureza de los pesos locales**, no la multiplicatividad.

### 6.6. Verificación 4: Davenport–Heilbronn, y la tensión resuelta

**[DATO].** La función de Davenport–Heilbronn tiene ecuación funcional de tipo
$\zeta$ (hermitiana, $\sigma$-estable) y **ceros fuera de la línea crítica** en
$\tfrac12<\mathrm{Re}\,s<1$ (Davenport–Heilbronn 1936 para ceros en
$\mathrm{Re}\,s>1$; Spira 1968 y Balanzario–Sánchez-Ortiz 2007 exhiben ceros en la
banda crítica fuera de la línea; Titchmarsh §10.25). No tiene producto de Euler
(es combinación lineal de dos $L$'s).

**[PROPOSICIÓN 6.8].** (a) $X_{DH}$ viola la versión por bloques de H
**incondicionalmente**: el Teorema 6.3 aplicado a una órbita libre
$\{\rho_0,1-\bar\rho_0\}$ de su divisor produce un bloque hiperbólico con dirección
negativa realizada sobre la clase de prueba. (b) La violación de H plena
($Q_{DH}(f,f)<0$ para un test explícito) se sigue de (a) más la separación del
bloque contra la marea on-line — el mismo enunciado tipo Hipótesis D que el
programa declara para ζ; estatus: [PUENTE], no probado acá en general (probado
arriba cuando el divisor es de retícula o finito).

*Demostración.* (a) es Teorema 6.3 + [DATO]. (b) es la delimitación honesta de
§6.1. $\square$

**La tensión que el encargo anticipaba, resuelta.** La pregunta era: "si tu Axioma H
vale para D–H, entonces H no puede implicar ceros en línea". Ocurre lo contrario y
es mejor: **H falla para D–H** (a nivel de bloques, incondicionalmente), porque en
esta categoría H *sí* implica ceros en línea para **todos** los objetos espectrales
hermitianos (Teorema 6.3: H-por-bloques $\iff$ divisor en la línea — el criterio de
Weil categorificado, externo a ζ por construcción). La pregunta de contenido se
desplaza entonces a: **¿qué datos aritméticos fuerzan H?** Y ahí la categoría
entrega respuestas con prueba:
- ecuación funcional (hermitiano) **no basta**: D–H;
- producto de Euler + ecuación funcional + masa diagonal **no bastan**:
  $F_{p,\alpha}$ impuro (Teorema 6.7);
- lo que separa los casos H de los no-H en todos los ejemplos decidibles es una
  **positividad/pureza del dato discreto** — en $F_{p,\alpha}$, literalmente
  $|c_m|\le2p^{m/2}$; en ζ, el candidato es $a=\Lambda\ge0$ (los contraejemplos
  $F_{p,\alpha}$ impuros tienen $a$ de signo no constante o compleja; D–H también).

**[DESEO 6.9] (Conjetura H⁺).** *Si $X$ es hermitiano, espectral, con $a\ge0$
soportada en potencias de primos (producto de Euler), bloque polar estándar
($c=[0]+[1]$) y $\omega$ de tipo arquimediano, entonces $X$ satisface H.*
— Implica RH (ζ califica): es RH-dura, no se reclama nada. Su valor es de diseño:
es un enunciado NC2-conforme (cuantifica sobre una clase de datos, no sobre ζ), y
es **falsable dentro de la categoría**: un contraejemplo sería un objeto construible
(p.ej. interferencia de dos primos con $a\ge0$ y un cero off-line). Buscar el
contraejemplo es una tarea concreta de la Phase 44; si no existe, entender por qué
es exactamente el contenido de RH visto desde acá.

---

## 7. [PUENTE] H y RH; la posición frente al Doc 110

### 7.1. El puente, sin maquillaje

**[PUENTE 7.1].** Para el objeto $\zeta_{\mathrm{ob}}$:
$$\mathrm{RH}\ \Longrightarrow\ H(\zeta_{\mathrm{ob}})\quad
\text{(Prop. 6.2, probada acá, instancia del teorema categórico)};$$
$$H(\zeta_{\mathrm{ob}})\ \Longrightarrow\ \mathrm{RH}\quad
\text{[DATO: criterio de Weil; Weil 1952, Bombieri 2000]}.$$
**$H(\zeta_{\mathrm{ob}})$ es RH-equivalente. Declarado.** La categoría no convierte
RH en otra cosa; la pregunta legítima es si **redistribuye** la dificultad.

### 7.2. Qué hipótesis del teorema de imposibilidad violamos (Doc 110)

El Teorema 4.3 del Doc 110 prueba que en la clase $\mathcal{F}$ (índices
$I=\mathrm{neg.ind}(Q|_{V'})$ con $Q$ de tipo fórmula explícita y $V'$
**test-accesible**, Def. 4.2(ii)) los axiomas (L2)+(L3)+(L4) son inconsistentes.
Los axiomas de $\mathcal{A}rith^{EF}$ violan **exactamente la hipótesis (ii)
(test-accesibilidad)**: el divisor $Z$ es un *dato estructural del objeto* — los
bloques $B_S$ están indexados por subconjuntos del divisor, no especificados por
soportes/ventanas de tests. Por eso el Teorema 4.4 (signaturas por bloque, enteras,
finitas a priori — el mecanismo de la Prop. 4.5 del Doc 110: rango finito $\Rightarrow$
inercia legible) convive sin contradicción con el teorema de imposibilidad: no
estamos en $\mathcal{F}$.

El precio, dicho con todas las letras: para ζ, los funtores de $\mathcal{A}rith^{EF}$
presuponen el divisor. **Toda la no-autonomía del programa queda concentrada en un
único lugar: el funtor de comparación $U:\mathcal{A}rith^{EF}\to\mathcal{A}rith$ y
la pregunta de qué objetos de $\mathcal{A}rith$ admiten levantamiento espectral con
divisor en la línea.** H es el criterio (vive abajo, en $\mathcal{A}rith$, sin
ceros); el teorema de órbitas es la obstrucción (vive arriba). La fórmula del
Doc 108 §7.4 ("autonomía del valor ≠ autonomía de la inercia") se convierte en:
*el valor vive en $\mathcal{A}rith$, la inercia en $\mathcal{A}rith^{EF}$, y RH es
una propiedad del funtor $U$ restringido al punto ζ.*

### 7.3. Qué redistribuye la categoría (balance honesto)

**A favor (probado):** (i) H es **decidible** en subcategorías genuinas: divisores
finitos (Teorema 4.4(c)), objetos de un primo (Teorema 6.7: pureza, un criterio
cerrado), y por bloques en todo $\mathcal{A}rith^{EF}$ (Teorema 6.3). (ii) Los
teoremas de estructura (órbitas, $q\le p$, tensorial, juguete $(1,2)$) son externos
a ζ por construcción y sobreviven a cualquier refutación local: son matemática del
marco, no del objetivo. (iii) Los contraejemplos construidos ($F_{p,\alpha}$ impuro)
**prueban** que ciertos atajos (Euler $\Rightarrow$ H) son falsos — la categoría
poda el espacio de estrategias con teoremas, no con heurística.

**En contra (declarado):** (iv) la verificación de H para ζ es el criterio de Weil:
ningún avance directo. (v) El paso bloque$\to$funcional (separación contra la marea
on-line) es Hipótesis D con otro nombre, salvo en las subcategorías resueltas.
(vi) El paso "H para truncados de Euler $\Rightarrow$ H para ζ" choca con la
discontinuidad de signaturas en límites (T2, Doc 119; Babaee–Huh, Doc 125) — el
[DESEO] siguiente lo nombra.

**[DESEO 7.2] (Lema de rigidez del límite).** *Sea $X_S$ la familia de objetos de
Euler truncados (datos $a\cdot 1_{p\le y}$ con bloque polar/arquimediano de ζ —
los objetos semilocales de CCM, Doc 110 §3, leídos en $\mathcal{A}rith$). Si cada
$X_S$ satisface H con gap cuantitativo $\mu_S\ge0$ y los $\deg$-funcionales
convergen a los de $\zeta_{\mathrm{ob}}$, entonces $H(\zeta_{\mathrm{ob}})$.* — El
primer caso (un primo, $p=2$) es la Conjetura 100.A del programa. La aportación de
la categoría: el caso "un primo, sin arquimediano global" YA está resuelto
(Teorema 6.7, pureza con $|c_m|=2p^{m/2}$ en el borde): el primer eslabón
genuinamente nuevo es **dos primos** — el objeto $F_{p,\alpha}\star F_{q,\alpha'}$
con períodos inconmensurables, exactamente donde el Doc 125 localizó G-125.B.

---

## 8. La renta propia: lo que la categoría paga independientemente de RH

Tres teoremas de este documento son matemática nueva o re-fundada que no depende de
RH ni la implica, y se sostienen solos:

1. **[TEOREMA 4.6 + COROLARIO 4.5] (clasificación de signaturas).** Sobre los
   objetos espectrales hermitianos de divisor finito, las signaturas de la forma de
   Weil son exactamente $\{(p,q):q\le p\}$: la desigualdad $q\le p$ ("a lo sumo la
   mitad de la inercia es negativa") es la única restricción universal, y es la
   huella de la involución $\sigma$, válida para cualquier función aritmética. No
   conozco este enunciado formulado así en la literatura; su contenido es que la
   "forma de Weil" es un funtor de clasificación de divisores $\sigma$-simétricos,
   con imagen caracterizada.

2. **[TEOREMA 6.7] (pureza local).** Para los objetos de Euler de un primo, la
   positividad de Weil **equivale a la pureza de los pesos locales**
   ($|\alpha|=\sqrt p$; equivalentemente la cota de Ramanujan $|c_m|\le2p^{m/2}$),
   con prueba elemental completa (Poisson + test de dos protuberancias). Es un
   "teorema de Hodge–Tate de juguete absoluto": en rango local, positividad =
   pureza, decidible. Y su corolario negativo — **el producto de Euler no implica
   positividad de Weil** — poda una intuición persistente del campo con un
   contraejemplo de dos líneas.

3. **[TEOREMA 1.9] (caracterización diferencial del producto de Euler).** "Tener
   producto de Euler" es una condición de soporte sobre la derivada logarítmica en
   el anillo diferencial $(\mathcal{D},\star,D)$ — un predicado algebraico puro,
   sin analiticidad. (Parientes en Rearick 1968 [DATO]; la forma cerrada
   exp/log/soporte con la aplicación categórica es de este documento.)

Menores pero propias: el Teorema 5.3 (el índice de juguete $(1,2)$ como teorema de
estructuras de intersección abstractas, con la degeneración exacta en $g=0$ — que
explica en una línea por qué el género 0 de $\mathrm{Spec}\,\mathbb{Z}$ de CC no
puede portar un índice de Hodge de rango 3), y la Prop. 6.5 (masa diagonal: la
positividad de Weil de cualquier objeto exige masa polar/arquimediana — la
"densidad de ceros" como condición necesaria estructural).

---

## 9. Mapa del marco y el siguiente teorema

**Probado en este documento [TEOREMA]:**
- $\mathcal{K}_2$ anillo conmutativo local; asociatividad de $\star_2$ (1.4);
- anillo diferencial $\mathcal{D}$, $\exp_\star$, Euler $\iff$ soporte PP (1.9);
- categoría de correspondencias con composición asociativa y unidad, fidelidad de
  núcleos (2.3, 2.4); $\sigma$ funtor involutivo, $Q_X$ hermitiana (2.8);
- grado = lado casi-primo para toda función aritmética (3.2, 3.3);
- lema de evaluación (4.3); teorema de órbitas y signatura de bloques (4.4);
  $q\le p$ universal (4.5); clasificación/realización (4.6); índice tensorial (4.8);
  fórmula explícita doble para EF (4.9);
- índice de juguete: $(1,2)$ $\iff g\ge1$, degeneración en $g=0$ (5.3);
- H desde la línea, para toda la categoría (6.2); H-por-bloques $\iff$ divisor en
  línea, incondicional (6.3); fallas de H: constante (6.4), completamente
  multiplicativas/masa diagonal (6.5); fórmula de Poisson–Euler (6.6);
  **pureza local** (6.7).

**[PUENTE] (estatus declarado):** $H(\zeta_{\mathrm{ob}})\iff$RH (mitad probada acá,
mitad criterio de Weil [DATO]); negatividad plena de $Q$ para D–H y para divisores
infinitos generales = separación tipo Hipótesis D (probada solo para divisores
finitos y de retícula); la realización tropical de la estructura de intersección en
objetos periódicos importa el cómputo del Doc 125 [CONSTRUCCIÓN].

**[DESEO]:** Conjetura H⁺ (6.9: $a\ge0$ + Euler + polar estándar $\Rightarrow$ H);
Lema de rigidez del límite (7.2); extensión de la estructura de intersección a dos
primos inconmensurables (G-125.B en versión categórica).

**El siguiente teorema a atacar** — elegido porque es finito, nuevo, y discrimina:
**el objeto de dos primos.** Sea $X_{p,q;\alpha,\alpha'}$ el objeto con dato
$a$ soportado en $\{p^m q^n\}$ dado por la convolución de dos factores de Euler
puros ($|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$). Su funcional es computable por la
fórmula de Poisson en cada factor; su divisor NO es una unión de retículas (los
períodos $\log p,\log q$ son inconmensurables) y su forma $Q$ es el primer caso
donde la positividad no se decide ni por bloques finitos ni por una retícula.
Probar o refutar: *$Q_{X_{p,q}}\ge0$, con gap, uniformemente en el segundo primo.*
Es la Conjetura 100.A reescrita como enunciado interno de $\mathcal{A}rith$ sobre
objetos puros — si la categoría vale lo que promete, este es el lugar donde un
teorema de dos primos puede existir sin tocar ζ; y si falla, el contraejemplo
refutaría H⁺ y enseñaría qué positividad falta. En ambos casos se aprende un
teorema.

---

## Referencias

**Internas (backward-only):** Doc 107 (fórmula de Weil 1–2 variables, núcleo
engrosado, Teoremas 2.4/3.4/4.2/4.4/5.5, Prop. 6.1); Doc 125 (intersección tropical,
$G_{\mathrm{toy}}$, $\Delta_\mu$, G-125.A/B); Doc 110 (L1–L6, clase $\mathcal{F}$,
Teorema 4.3, Prop. 4.5, tabla §5.2); Doc 106 (Prop. 3.5 índice tensorial, Lemas
5.2/5.3); Doc 96 (Teorema 8.1); Doc 108 (valor/inercia); P35 (forma de Weil,
$\kappa=2m$, Hipótesis D); Doc 119 (R-NC, NC1–NC4, T2/T3); Doc 124 (género 0 de
$\mathrm{Spec}\,\mathbb{Z}$).

**Literatura [DATO]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Comm. Sém. Math. Lund (1952), 252–265.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
  numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233 (criterio de Weil:
  positividad $\Rightarrow$ RH).
- C. N. Cashwell, C. J. Everett, *The ring of number-theoretic functions*, Pacific
  J. Math. 9 (1959), 975–985.
- D. Rearick, *Operators on algebras of arithmetic functions*, Duke Math. J. 35
  (1968), 761–766 (exp/log de Dirichlet).
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series I, II*,
  J. London Math. Soc. 11 (1936), 181–185, 307–312. R. Spira, *Some zeros of the
  Titchmarsh counterexample*, Math. Comp. (1968). E. P. Balanzario,
  J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  76 (2007), 2045–2049. E. C. Titchmarsh, *The Theory of the Riemann
  Zeta-Function*, 2.ª ed., §10.25.
- L. Allermann, J. Rau, *First Steps in Tropical Intersection Theory*,
  arXiv:0709.3705. F. Babaee, J. Huh, Duke Math. J. 166 (2017), arXiv:1502.00299
  (vía Doc 125).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. 53, 2004, Cap. 5.

*Fin del Documento 131.*
