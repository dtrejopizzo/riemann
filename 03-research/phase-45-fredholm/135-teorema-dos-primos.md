# Doc 135 — El teorema de dos primos: positividad para $F_{p,\alpha}\star F_{q,\alpha'}$ puros

**Programa:** Hipótesis de Riemann — Phase 45: FREDHOLM / primeros teoremas de la categoría $\mathcal{A}rith$.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 131 (la categoría $\mathcal{A}rith$; anillo de Dirichlet $(\mathcal D,\star)$ y Lema 1.7 $L(F\star G)=L(F)+L(G)$; Definición 2.1 de objeto $(a,c,\omega)$ y funcional $W_X$; Prop. 2.8 ($\sigma$, $Q_X$ hermitiana); Definición 4.1 (objeto espectral, fórmula explícita); Teorema 4.4 (órbitas); Teorema 4.9 (fórmula explícita doble); Prop. 6.2 (H desde la línea); Teorema 6.6 (Poisson para factores de Euler); Teorema 6.7 (pureza local); Deseo 6.9 (Conjetura H⁺); Deseo 7.2 (rigidez del límite); §9 (el encargo: el objeto de dos primos)).
**Contrato creativo (Phase 44/45):** **[DEFINICIÓN-NUEVA]** libertad total; **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** con prueba completa, estándar máximo; **[CÁLCULO]** verificado; **[PUENTE]** con estatus declarado; **[DESEO]** lo que se quiere y no se prueba; **[GAP]** lo que falta, nombrado; **[DATO]** literatura citada. La disciplina vive en qué se llama teorema.

**Convenciones (las del Doc 131, fijadas una vez).** $G=\mathbb R_+^*$, $d^*x=dx/x$, tests $f\in C_c^\infty(G)$, Mellin $\hat f(s)=\int_0^\infty f(x)x^{s-1}\,dx$, involución $\tilde f(x)=\overline{f(1/x)}\,x^{-1}$, $\widehat{\tilde f}(s)=\overline{\hat f(1-\bar s)}$, $\sigma(s)=1-\bar s$. Para $f$ dado, escribimos
$$F(t):=f(e^t)\,e^{t/2}\in C_c^\infty(\mathbb R),\qquad
\hat F(\xi):=\int_{\mathbb R}F(t)\,e^{i\xi t}\,dt,$$
de modo que $\hat f(\tfrac12+i\xi)=\hat F(\xi)$ y $\;\|f\|_w^2:=\int_G|f(x)|^2\,x\,d^*x=\|F\|_{L^2(\mathbb R)}^2$.
Para un primo $r$ escribimos $L_r:=\log r$. "Ventana de longitud $2T$" = soporte de $f$ contenido en un intervalo $[\lambda e^{-T},\lambda e^{T}]$ (equivalentemente: $\operatorname{supp}F$ en un intervalo de longitud $2T$; la posición $\lambda$ es libre y, como se verá, irrelevante).

---

## 0. Resumen ejecutivo

Este documento prueba el teorema anunciado en Doc 131 §9. Sin adorno:

1. **(§1)** El producto $\star$ de objetos de Euler en $\mathcal{A}rith$ y su ley de
   composición exacta (Prop. 1.3): bajo la convolución de Dirichlet de las series de
   coeficientes, **los datos de Weil se suman**: $W_{X_1\star X_2}=W_{X_1}+W_{X_2}$.
   El soporte mixto $\{p^aq^b:a,b\ge1\}$ — donde la convolución "mezcla" — **lleva
   masa de Weil exactamente cero** (Lema 1.7 del Doc 131). El miedo a los términos
   cruzados del lado aritmético se disuelve como teorema, no como accidente.

2. **(§2)** El objeto de dos primos $X_{p,q}:=F_{p,\alpha}\star F_{q,\alpha'}$ es
   espectral, hermitiano y admisible, con bloque $(c,\omega)=(0,\,-2\log pq)$ y
   divisor = unión de dos progresiones verticales de períodos
   $2\pi/\log p,\ 2\pi/\log q$ — inconmensurables (Lema 1.5): **no es una retícula**.

3. **(§3) [TEOREMA A]** Si $|\alpha|=\sqrt p$ y $|\alpha'|=\sqrt q$, entonces
   $X_{p,q}$ satisface el Axioma H y su versión doble H₂, con identidad espectral
   exacta $Q_X(f,f)=2\sum_{\Lambda_p}|\hat F|^2+2\sum_{\Lambda_q}|\hat F|^2$.
   **El primer teorema de positividad de Weil con dos primos y períodos
   inconmensurables, sin tocar ζ.** Los términos cruzados entre progresiones no se
   matan en media (Kronecker): **no existen** — el funcional es lineal en el divisor.

4. **(§4) [TEOREMA B]** Recíproca: si $|\alpha|\ne\sqrt p$ o $|\alpha'|\ne\sqrt q$,
   H falla, con test explícito de dos protuberancias. La marea diagonal del segundo
   primo sube la barrera de Ramanujan de $2p^{M/2}$ a $2p^{M/2}(1+L_q/L_p)$, pero
   ninguna marea finita salva la impureza. **Corolario: H es decidible en la
   subcategoría de dos primos y equivale a pureza bilateral** — la extensión exacta
   del Teorema 6.7 del Doc 131.

5. **(§5)** Estructura fina, donde Kronecker sí aparece: gap **exacto**
   $Q_X=2\log(pq)\,\|f\|_w^2$ en ventanas $\le\log\min(p,q)$ (Teorema 5.2); gap
   uniforme $2\log q$ hasta ventana $\log q$, **uniforme (creciente) en el segundo
   primo** — el enunciado del Doc 131 §9 probado; umbral del núcleo en
   $2T=\log(pq)$ (Teorema 5.4, vía Jensen + construcción explícita): la forma es
   definida en ventanas $<\log pq$ y semidefinida con núcleo infinito-dimensional
   más allá. Las casi-colisiones de las dos progresiones (Kronecker/Weyl) impiden
   separación uniforme; con fases triviales, Baker las repele polinomialmente
   (Prop. 5.6). El gap uniforme en ventanas intermedias queda nombrado: GAP-135.A.

6. **(§6) [CÁLCULO]** El juguete $p=2$, $q=3$, $\alpha=\sqrt2$, $\alpha'=\sqrt3$:
   test de Mertens contra el primo 2: mínimo $=\log6-(\log2)^2/\log6\approx1.5236>0$;
   la dirección crítica del primo 2 (donde su cuadrado perfecto se anula) es
   rescatada por la diagonal del 3 con margen $4\log3$; el test doblemente
   adversario da mínimo $=4\log2\log3/\log6\approx1.7000>0$ — **el margen es dos
   veces la media armónica de $\log2$ y $\log3$, uniforme en las alturas $M,N$**;
   el adversario en el punto mixto $8/9$ (casi-colisión de Kronecker) se desacopla:
   no hay coeficiente al cual golpear.

7. **(§7) [TEOREMA A′ + PUENTE]** El argumento es **aditivo, luego trivialmente
   inductivo**: vale verbatim para $n$ primos (Teorema 7.1, margen
   $4\sum_{i<j}L_iL_j/\log P$). La inducción hacia ζ se rompe en cuatro puntos
   localizados (B1–B4): divergencia de la masa diagonal $\omega_y=-2\theta(y)$;
   **divisor del límite ≠ límite de divisores** (la positividad pasa al límite, la
   espectralidad no); el desajuste de peso (los factores locales de ζ son
   $\sigma$-impuros: $c_m=1+p^m$, violación maximal de Ramanujan — la simetría de ζ
   es global, no factor a factor); y el orden de los límites ventana/primos. La
   transmutación vive en B2+B3, no en el paso de positividad.

---

## 1. El producto $\star$ y el objeto de dos primos

### 1.1. La ley de composición de $W$ bajo $\star$

Recordatorio del diccionario del Doc 131 (§1.2, §6.4–6.5). A una serie de Dirichlet
$E(s)=\sum_n b(n)n^{-s}$ con $b(1)=1$ le corresponde el dato discreto
$a:=L(b)=b^{-1}\star Db\in\mathcal D$ (la derivada logarítmica de Dirichlet,
$a\leftrightarrow -\,d/ds\log E$). El objeto de Euler de un primo $F_{p,\alpha}$
(Doc 131, Prop. 6.6′) corresponde al **polinomio local autodual**
$$D_{p,\alpha}(s)\;:=\;(1-\alpha p^{-s})\bigl(1-(p/\bar\alpha)\,p^{-s}\bigr),$$
cuyos coeficientes de Dirichlet están soportados en $\{1,p,p^2\}$, con dato
$a(p^m)=L(b)(p^m)=-L_p\,c_m$, $c_m:=\alpha^m+(p/\bar\alpha)^m$, divisor = ceros de
$D_{p,\alpha}$, y funcional
$$W_{F_{p,\alpha}}(f)\;=\;L_p\sum_{m\in\mathbb Z}c_m\,f(p^m),\qquad
c_{-m}=\bar c_m\,p^{-m},\quad c_0=2.$$
*(El factor $(1-\alpha'q^{-s})$ del encargo es "la mitad" del objeto: la
$\sigma$-estabilidad fuerza el factor espejo $1-(q/\bar\alpha')q^{-s}$; bajo pureza
ambos coinciden y aparece multiplicidad 2. Trabajamos siempre con el objeto
autodual completo.)*

**[DEFINICIÓN-NUEVA 1.1] (producto $\star$ de objetos).** Para objetos
$X_1=(a_1,c^{(1)},\omega_1)$, $X_2=(a_2,c^{(2)},\omega_2)$ de $\mathcal{A}rith$:
$$X_1\star X_2\;:=\;\bigl(a_1+a_2,\;c^{(1)}+c^{(2)},\;\omega_1+\omega_2\bigr).$$
El nombre $\star$ se justifica en la Prop. 1.3: sobre objetos provenientes de series
de Dirichlet, esta operación ES la convolución de Dirichlet de las series de
coeficientes, leída en los datos de Weil.

**[PROPOSICIÓN 1.2] (aditividad de $W$; trivial pero estructural).** Para todo
test $f$: $W_{X_1\star X_2}(f)=W_{X_1}(f)+W_{X_2}(f)$, y
$Q_{X_1\star X_2}(f,f)=Q_{X_1}(f,f)+Q_{X_2}(f,f)$.

*Demostración.* Los tres bloques de la Definición 2.1 del Doc 131 ($D_c$, $P_a$,
$A_\omega$) son lineales en los datos $(a,c,\omega)$. La segunda identidad es la
primera aplicada a $f\star\tilde f$. $\square$

**[PROPOSICIÓN 1.3] (la ley de composición exacta: la convolución de Dirichlet no
mezcla los datos de Weil).** Sean $b_1,b_2\in\mathcal D$ unidades normalizadas con
datos $a_i=L(b_i)$, y sea $b:=b_1\star b_2$ (convolución de Dirichlet — para
factores de Euler de primos distintos, $b$ está soportada en $\{p^aq^b\}$ y mezcla
genuinamente los dos primos). Entonces el dato de Weil de $b$ es
$$L(b_1\star b_2)\;=\;L(b_1)+L(b_2)\;=\;a_1+a_2,$$
es decir: el objeto asociado a $b$ es exactamente $X_1\star X_2$ en el sentido de
la Definición 1.1. En particular, si $a_1$ está soportada en $p^{\mathbb N}$ y
$a_2$ en $q^{\mathbb N}$ con $p\ne q$, el dato del producto está soportado en
$p^{\mathbb N}\sqcup q^{\mathbb N}$: **el soporte mixto $\{p^aq^b:a,b\ge1\}$ de los
coeficientes lleva masa de Weil cero.**

*Demostración.* Es el Lema 1.7 del Doc 131 ($D$ es derivación de
$(\mathcal D,\star)$, luego $L$ es aditiva sobre unidades normalizadas), más la
observación de soportes: $a_1+a_2$ vive en la unión de los soportes, que es
disjunta por factorización única. $\square$

**Observación 1.4 (el miedo a los cruzados, disuelto en el lugar correcto).** El
encargo anticipaba: *"el funcional de Weil del objeto producto no es la suma de los
funcionales — la convolución de Dirichlet mezcla"*. La Prop. 1.3 muestra que la
mezcla ocurre en los **coeficientes** $b(p^aq^b)\ne0$ y desaparece **exactamente**
(no en media, no asintóticamente) en el dato $a=L(b)$, que es lo que $W$ ve. La
identidad responsable es algebraica ($L$ aditiva = derivación logarítmica), no
diofántica: Kronecker no se necesita para el signo. Los términos cruzados entre las
dos progresiones de ceros reaparecerán — pero en la **geometría fina del gap**
(§5), no en la positividad. Esta relocalización es uno de los hallazgos del
documento. Punto de diseño, declarado: si uno definiera el objeto producto poniendo
como dato discreto la convolución $b_1\star b_2$ *cruda* (en el slot $a$), el
objeto resultante no sería de Euler en el sentido del Teorema 1.9 del Doc 131 y
nada de lo que sigue lo tocaría; la Definición 1.1 es la única compatible con el
diccionario objeto ↔ serie.

### 1.2. El objeto de dos primos

**[DEFINICIÓN-NUEVA 1.5] (el objeto de dos primos).** Sean $p\ne q$ primos,
$1<|\alpha|<p$, $1<|\alpha'|<q$. El **objeto de dos primos** es
$$X_{p,q}\;=\;X_{p,q;\alpha,\alpha'}\;:=\;F_{p,\alpha}\star F_{q,\alpha'}
\;=\;\bigl(a,\;0,\;\omega\bigr),$$
con datos explícitos:
- $a(p^m)=-L_p\,c_m$ ($m\ge1$), $a(q^n)=-L_q\,c'_n$ ($n\ge1$), $a=0$ en el resto
  (en particular en todo $p^aq^b$ con $a,b\ge1$, por la Prop. 1.3); aquí
  $c_m=\alpha^m+(p/\bar\alpha)^m$, $c'_n=\alpha'^n+(q/\bar\alpha')^n$;
- $c=0$ (sin bloque polar);
- $\omega\equiv-2\log(pq)$ (constante: par, medible, de crecimiento polinomial —
  admisible), que realiza el átomo diagonal $c_0+c'_0=2+2$ vía la inversión de
  Mellin $f(1)=\tfrac1{2\pi}\int\hat f(\tfrac12+it)\,dt$:
  $-A_\omega(f)=2\log(pq)\,f(1)$.

El funcional, en forma cerrada (suma finita para cada test):
$$\boxed{\;W_{X}(f)\;=\;L_p\sum_{m\in\mathbb Z}c_m\,f(p^m)
\;+\;L_q\sum_{n\in\mathbb Z}c'_n\,f(q^n)\;}$$
donde el término $(m,n)=(0,0)$ se cuenta una sola vez con peso
$c_0L_p+c'_0L_q=2\log(pq)$ (es el bloque $\omega$; los $m\ne0,n\ne0$ son el bloque
discreto $-P_a$ con sus espejos $c_{-m}=\bar c_m p^{-m}$).

**[LEMA 1.6] ($X_{p,q}$ es hermitiano).** $W_{\sigma X}(f)=W_X(f)$ para todo $f$,
i.e. $\overline{W_X(\tilde f)}=W_X(f)$; en consecuencia (Doc 131, Prop. 2.8(c) con
la identidad funcional en lugar de la igualdad de datos) $Q_X(f_1,f_2):=
W_X(f_1\star\tilde f_2)$ es forma hermitiana.

*Demostración.* Por la Prop. 1.2 basta verificarlo por factor. Para $F_{p,\alpha}$:
$\tilde f(p^m)=\overline{f(p^{-m})}\,p^{-m}$, luego
$$\overline{W_F(\tilde f)}=L_p\sum_m\bar c_m\,f(p^{-m})\,p^{-m}
\;\overset{m\mapsto-m}{=}\;L_p\sum_m\bar c_{-m}\,p^{m}\,f(p^{m}),$$
y $\bar c_{-m}\,p^{m}=\overline{\bar c_m p^{-m}}\,p^{m}\cdot 1=c_m$ usando
$c_{-m}=\bar c_m p^{-m}$. Igual para el factor $q$. $\square$

**[LEMA 1.7] (inconmensurabilidad).** $\log p/\log q\notin\mathbb Q$. Más aún: las
progresiones de frecuencias
$$\Lambda_p:=\Bigl\{\tfrac{\phi+2\pi k}{L_p}:k\in\mathbb Z\Bigr\},\qquad
\Lambda_q:=\Bigl\{\tfrac{\phi'+2\pi l}{L_q}:l\in\mathbb Z\Bigr\}$$
(con $\phi:=\arg\alpha$, $\phi':=\arg\alpha'$ fijos) comparten a lo sumo **un**
punto.

*Demostración.* Si $\log p/\log q=a/b$ con $a,b\in\mathbb Z_{\ge1}$, entonces
$p^b=q^a$, imposible por factorización única. Si $\Lambda_p\cap\Lambda_q$ tuviera
dos puntos, la diferencia daría $2\pi k/L_p=2\pi l/L_q$ con $(k,l)\ne(0,0)$, i.e.
$kL_q=lL_p$, i.e. $\log p/\log q=k/l\in\mathbb Q$, contradicción. $\square$

---

## 2. [CÁLCULO] El par espectral: los dos lados de $W_X$

**[PROPOSICIÓN 2.1] (lado de ceros).** Sea $Z_{p,\alpha}:=\{s:p^s=\alpha\}
=\{\log_p\alpha+2\pi ik/L_p\}$ y análogamente $Z_{q,\alpha'}$. El par
$(X_{p,q},\,Z_X)$ con el multiconjunto
$$Z_X\;:=\;\underbrace{Z_{p,\alpha}\sqcup Z_{p,\,p/\bar\alpha}}_{\text{ceros de }D_{p,\alpha}}
\;\sqcup\;\underbrace{Z_{q,\alpha'}\sqcup Z_{q,\,q/\bar\alpha'}}_{\text{ceros de }D_{q,\alpha'}}$$
es un objeto espectral de $\mathcal{A}rith^{EF}$ (Doc 131, Def. 4.1):
$$\sum_{\rho\in Z_X}\hat f(\rho)\;=\;W_X(f)\qquad\forall f\in C_c^\infty(G),$$
con convergencia absoluta, $N_{Z_X}(T)=\tfrac{2}{\pi}\bigl(L_p+L_q\bigr)T+O(1)\ll T$,
y $Z_X$ $\sigma$-estable ($\sigma Z_{p,\alpha}=Z_{p,\,p/\bar\alpha}$).

*Demostración.* La fórmula de Poisson para factores de Euler (Doc 131, Teorema 6.6)
aplicada a cada una de las cuatro progresiones:
$\sum_{Z_{p,\alpha}}\hat f(\rho)=L_p\sum_m\alpha^m f(p^m)$ y
$\sum_{Z_{p,p/\bar\alpha}}\hat f(\rho)=L_p\sum_m(p/\bar\alpha)^m f(p^m)$; la suma
de ambas es $L_p\sum_m c_m f(p^m)$. Igual en $q$. Sumando: el lado derecho es
exactamente la forma cerrada de la Definición 1.5. La densidad: cada progresión
tiene $\#\{|\mathrm{Im}\,\rho|\le T\}=L_rT/\pi+O(1)$. La $\sigma$-estabilidad:
$p^{1-\bar\rho}=p/\overline{p^{\rho}}=p/\bar\alpha$. $\square$

**Geometría del divisor, explícita.**
- En general ($\alpha$ impuro): cuatro progresiones verticales, en
  $\mathrm{Re}=\log_p|\alpha|$ y $1-\log_p|\alpha|$ (período $2\pi/L_p$) y en
  $\mathrm{Re}=\log_q|\alpha'|$ y $1-\log_q|\alpha'|$ (período $2\pi/L_q$).
- Bajo **pureza** $|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$: $\alpha=p/\bar\alpha$, las
  dos progresiones del primo $p$ coinciden; el divisor es
  $$Z_X\;=\;2\cdot\Bigl\{\tfrac12+i\tfrac{\phi+2\pi k}{L_p}\Bigr\}
  \;\sqcup\;2\cdot\Bigl\{\tfrac12+i\tfrac{\phi'+2\pi l}{L_q}\Bigr\}
  \;=\;2\cdot\bigl(\tfrac12+i\Lambda_p\bigr)\sqcup 2\cdot\bigl(\tfrac12+i\Lambda_q\bigr),$$
  dos progresiones sobre la línea crítica con multiplicidad 2 y períodos
  inconmensurables (Lema 1.7), y los coeficientes valen $c_m=2\alpha^m$,
  $|c_m|=2p^{m/2}$ (la igualdad de Ramanujan, el borde exacto de la barrera del
  Doc 131 §6.5).

**Observación 2.2 (esto no es una retícula).** Para un solo primo, el divisor es
una retícula vertical y el objeto es *periódico* (Doc 131, Def. 5.4): toda la
teoría se reduce al círculo $G/p^{\mathbb Z}$. Para dos primos, $\log p$ y
$\log q$ son $\mathbb Q$-linealmente independientes: el grupo generado por
$p^{\mathbb Z}q^{\mathbb Z}$ es denso en $G$ (Kronecker) y no hay cociente compacto
que porte al objeto. Este es exactamente el territorio donde el Doc 125 localizó
G-125.B y donde ni el Teorema 4.4(c) del Doc 131 (divisores finitos) ni el
Teorema 6.7 (una retícula) deciden H. Por eso este teorema es nuevo.

---

## 3. [TEOREMA A] La positividad

**[TEOREMA 3.1] (el teorema de dos primos).** Sean $p\ne q$ primos y
$|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$ (pureza bilateral, fases
$\phi,\phi'$ arbitrarias). Entonces $X=X_{p,q;\alpha,\alpha'}$ satisface el
Axioma H, con identidad espectral exacta: para todo $f\in C_c^\infty(G)$,
$$Q_X(f,f)\;=\;2\sum_{\xi\in\Lambda_p}\bigl|\hat F(\xi)\bigr|^2
\;+\;2\sum_{\xi\in\Lambda_q}\bigl|\hat F(\xi)\bigr|^2\;\ge\;0,$$
con ambas sumas absolutamente convergentes. Satisface además H₂:
$\deg_X(h\star_{G^2}\tilde h)\ge0$ para todo $h\in C_c^\infty(G^2)$.

*Demostración.* Sea $g:=f\star\tilde f$. Por la Prop. 2.1, $(X,Z_X)$ es espectral,
hermitiano (Lema 1.6) y $\sigma$-estable, así que aplica el Teorema 4.4(a) del
Doc 131:
$$Q_X(f,f)=W_X(g)=\sum_{\rho\in Z_X}m_\rho\,\hat f(\rho)\,\overline{\hat f(\sigma\rho)}.$$
Bajo pureza todo $\rho\in Z_X$ tiene $\mathrm{Re}\,\rho=\tfrac12$, luego
$\sigma\rho=\rho$ y cada término es $m_\rho|\hat f(\rho)|^2\ge0$. Con
$\rho=\tfrac12+i\xi$, $\hat f(\rho)=\hat F(\xi)$ y multiplicidades $m_\rho=2$ se
obtiene la identidad del enunciado. (Convergencia absoluta: Paley–Wiener
$|\hat F(\xi)|\ll_N(1+|\xi|)^{-N}$ contra densidad lineal.) Para H₂: el
Teorema 4.9 del Doc 131 da
$\deg_X(h\star\tilde h)=\sum_{\rho_1,\rho_2\in Z_X}\hat h(\rho_1,\rho_2)
\overline{\hat h(\sigma\rho_1,\sigma\rho_2)}=\sum_{\rho_1,\rho_2}
|\hat h(\rho_1,\rho_2)|^2\ge0$ (Prop. 6.2 del Doc 131, que cubre H y H₂ para
divisores en la línea — la hipótesis de densidad polinomial se verificó en 2.1).
$\square$

Equivalentemente, en forma puramente aritmética (sin mencionar el divisor):
$$L_p\sum_{m\in\mathbb Z}c_m\,g(p^m)\;+\;L_q\sum_{n\in\mathbb Z}c'_n\,g(q^n)\;\ge\;0
\qquad\text{para todo }g=f\star\tilde f,$$
con $c_m=2\alpha^m$, $|c_m|=2p^{m/2}$. Este es el enunciado que NO era accesible ni
por bloques finitos ni por periodicidad, y que ahora es teorema.

**Observación 3.2 (dónde habrían estado los cruzados, y por qué no están).** Hay
dos lugares donde un "término cruzado $p$–$q$" podría haber aparecido, y en ambos
la cancelación es **exacta**, no estadística:

1. *Lado aritmético:* la convolución de Dirichlet de los coeficientes carga el
   soporte mixto $p^aq^b$; la masa de Weil ahí es cero por la Prop. 1.3 (identidad
   de derivación, álgebra pura).
2. *Lado espectral:* $W_X$ es **lineal** en el divisor — una sola suma sobre
   $Z_p\sqcup Z_q$, nunca una suma doble. Los productos
   $\hat f(\rho_1)\overline{\hat f(\rho_2)}$ con $\rho_1\in Z_p$, $\rho_2\in Z_q$
   solo aparecen en el funcional de dos variables $\deg_X$, donde la estructura
   producto los factoriza en $|\hat h(\rho_1,\rho_2)|^2$ — de nuevo positivos.

La inconmensurabilidad de $\log p$ y $\log q$ **no se usa** en el Teorema 3.1
(¡vale igual para $q=p$, donde es el caso retícula del Doc 131!). Donde sí se usa,
y de manera esencial, es en: (i) la recíproca (Teorema 4.1: separar los soportes de
los tests adversarios — solo factorización única), y (ii) la estructura fina del
gap (§5: Kronecker/Weyl/Baker). La lección, digna de subrayarse porque corrige la
intuición del encargo: **en la fórmula de Weil, la interferencia entre primos es un
fenómeno del gap, no del signo.**

---

## 4. [TEOREMA B] La recíproca: pureza bilateral necesaria

**[TEOREMA 4.1].** Sean $1<|\alpha|<p$, $1<|\alpha'|<q$. Si $|\alpha|\ne\sqrt p$ o
$|\alpha'|\ne\sqrt q$, entonces $X_{p,q;\alpha,\alpha'}$ **no** satisface H: existe
un test explícito $f$ con $Q_X(f,f)<0$.

*Demostración.* Sin pérdida de generalidad el factor impuro es el de $p$, con
$|\alpha|=p^{1/2+\delta'}$, $\delta'>0$ (si $\delta'<0$, intercambiar
$\alpha\leftrightarrow p/\bar\alpha$, mismo objeto; si el impuro es $q$,
intercambiar los papeles de $p$ y $q$; la pureza o impureza del otro factor es
irrelevante en lo que sigue). Usamos el test de Mertens de dos protuberancias del
Doc 131 §6.5, ahora en presencia del segundo primo.

Sea $M\ge1$ a fijar. Tomamos $u\ge0$ real, $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$
con $\chi$ par, $\operatorname{supp}\chi\subset[-1,1]$, $\int\chi^2=1$, y el test
$$f\;:=\;u+\theta\,u(\cdot/p^{M}),\qquad\theta\in\mathbb C.$$
Sea $g=f\star\tilde f$; $\log\operatorname{supp}g\subset\{0,\pm ML_p\}+[-2\epsilon,2\epsilon]$.

*Elección de $\epsilon$ (separación por factorización única).* Los puntos
muestreados por $W_X$ son $p^m$ y $q^n$. Para que $g(p^m)\ne0$ hace falta
$|mL_p-\kappa|<2\epsilon$ con $\kappa\in\{0,\pm ML_p\}$; con $\epsilon<L_p/4$ eso
fuerza $m\in\{0,\pm M\}$. Para que $g(q^n)\ne0$ hace falta
$|nL_q-\kappa|<2\epsilon$; los candidatos $n$ son finitos
($|n|\le(ML_p+1)/L_q$) y para cada uno con $n\ne0$ la cantidad
$\min(|nL_q|,\,|nL_q\mp ML_p|)$ es **estrictamente positiva** — $q^n\ne1$ y
$q^n\ne p^{\pm M}$ por factorización única (Lema 1.7). Tomamos
$$\epsilon\;<\;\tfrac14\min\Bigl(L_p,\ \min_{0<|n|\le(ML_p+1)/L_q}
\bigl|\,|n|L_q-ML_p\bigr|,\ L_q\Bigr).$$
Entonces el factor $q$ contribuye **solo su término diagonal** $n=0$, con
coeficiente $c'_0=2$ sea cual sea $\alpha'$.

*Los valores de $g$* (cálculo del Doc 131 §6.5, sin cambios):
$$g(1)=\bigl(1+|\theta|^2p^{M}\bigr)(1+O(\epsilon)),\qquad
g(p^{M})=\theta\,(1+O(\epsilon)),\qquad
g(p^{-M})=\bar\theta\,p^{M}(1+O(\epsilon)).$$
Usando $c_{-M}p^{M}=\bar c_M$:
$$Q_X(f,f)=\Bigl[\,2(L_p+L_q)\bigl(1+|\theta|^2p^{M}\bigr)
+2L_p\,\mathrm{Re}\!\bigl(c_M\theta\bigr)\Bigr](1+O(\epsilon)).$$
Elegimos la fase adversaria $\theta=-(\overline{c_M}/|c_M|)\,t$, $t>0$:
$$\frac{Q_X(f,f)}{2(1+O(\epsilon))}
=(L_p+L_q)\bigl(1+p^{M}t^2\bigr)-L_p\,|c_M|\,t,$$
con mínimo en $t^*=L_p|c_M|/\bigl(2(L_p+L_q)p^{M}\bigr)$ de valor
$$(L_p+L_q)\;-\;\frac{L_p^2\,|c_M|^2}{4\,(L_p+L_q)\,p^{M}}\;<\;0
\quad\Longleftrightarrow\quad
|c_M|\;>\;2\,p^{M/2}\Bigl(1+\tfrac{L_q}{L_p}\Bigr).$$
Como $|c_M|\ge p^{M(1/2+\delta')}-p^{M(1/2-\delta')}
=p^{M/2}\bigl(p^{M\delta'}-p^{-M\delta'}\bigr)$ y $\delta'>0$, el cociente
$|c_M|p^{-M/2}\to\infty$: existe $M$ que supera la barrera. Fijar tal $M$, luego
$\epsilon$ (que depende de $M$) para absorber los $O(\epsilon)$:
$Q_X(f,f)<0$. $\square$

**[COROLARIO 4.2] (pureza bilateral: H decidible en la subcategoría de dos
primos).** Para $p\ne q$, $1<|\alpha|<p$, $1<|\alpha'|<q$:
$$X_{p,q;\alpha,\alpha'}\ \text{satisface H}
\quad\Longleftrightarrow\quad
|\alpha|=\sqrt p\ \text{y}\ |\alpha'|=\sqrt q
\quad\Longleftrightarrow\quad
|c_m|\le2p^{m/2}\ \text{y}\ |c'_n|\le2q^{n/2}\ \ \forall m,n\ge1.$$
*(Teoremas 3.1 + 4.1; la segunda equivalencia es la del Doc 131, Teorema 6.7,
factor a factor.)* El Teorema de pureza local se extiende así, exactamente, de una
retícula a dos progresiones inconmensurables. $\square$

**Comentario cuantitativo.** La marea diagonal del segundo primo eleva la barrera
del test de $2p^{M/2}$ a $2p^{M/2}(1+L_q/L_p)$: un primo ajeno **protege**
aditivamente (su masa diagonal se suma) pero no puede comprar la impureza de otro,
porque la violación de Ramanujan crece geométricamente ($p^{M\delta'}$) y la
protección es constante en $M$. En el límite hacia ζ esta es la cuenta que vuelve:
la protección total de todos los primos es $2\theta(y)$, divergente — ver §7.

---

## 5. Estructura fina: gap exacto, núcleo, y donde vive Kronecker

En esta sección la pureza bilateral está siempre en vigor. Por el Teorema 3.1 todo
se reduce al análisis de
$$Q_X(f,f)=2\sum_{\Lambda_p}|\hat F|^2+2\sum_{\Lambda_q}|\hat F|^2 .$$

**[LEMA 5.1] (Parseval de la periodización).** Si $\operatorname{supp}F$ está en un
intervalo de longitud $\le L_r$, entonces
$\sum_{\xi\in\Lambda_r}|\hat F(\xi)|^2=L_r\,\|F\|_{L^2}^2$.

*Demostración.* Sea $F_r(t):=F(t)e^{i\phi_r t/L_r}$ (con $\phi_p=\phi$,
$\phi_q=\phi'$), de modo que $\hat F(\tfrac{\phi_r+2\pi k}{L_r})=\hat F_r(2\pi k/L_r)$.
La periodización $P(t)=\sum_m F_r(t+mL_r)$ tiene coeficientes de Fourier
$\tfrac1{L_r}\hat F_r(2\pi k/L_r)$; Parseval en $[0,L_r]$:
$\sum_k|\hat F_r(2\pi k/L_r)|^2=L_r\int_0^{L_r}|P|^2$. Si el soporte cabe en un
intervalo de longitud $\le L_r$, los trasladados no se superponen y
$\int_0^{L_r}|P|^2=\|F_r\|_2^2=\|F\|_2^2$. $\square$

**[TEOREMA 5.2] (gap exacto en ventana corta; uniforme en el segundo primo).**
Supongamos $p<q$.
(a) Si $f$ tiene soporte en una ventana de longitud $2T\le\log p$, entonces
$$Q_X(f,f)\;=\;2\,\log(pq)\,\|f\|_w^2$$
— identidad exacta: en ventanas cortas la forma es un múltiplo de la identidad
(no hay términos cruzados de ningún tipo).
(b) Si $2T\le\log q$, entonces $Q_X(f,f)\ge2\,\log q\,\|f\|_w^2$.
En particular el gap es **uniforme y creciente en el segundo primo**: para ventana
fija $2T$, todo primo $q\ge e^{2T}$ aporta gap $\ge2\log q$. El enunciado del
Doc 131 §9 ("con gap, uniformemente en el segundo primo") queda probado en este
rango de ventanas.

*Demostración.* (a) Vía espectral: Lema 5.1 en ambas retículas
($2T\le L_p<L_q$): $Q_X=2L_p\|F\|^2+2L_q\|F\|^2=2\log(pq)\,\|f\|_w^2$.
Vía aritmética (chequeo doble, cultura del programa): $g=f\star\tilde f$ tiene
soporte logarítmico en $(-2T,2T)\subset(-L_p,L_p)$ — toca solo $m=n=0$:
$W_X(g)=2(L_p+L_q)\,g(1)$ y $g(1)=\int|f|^2x\,d^*x=\|f\|_w^2$. Coinciden.
(b) Lema 5.1 solo en $\Lambda_q$ y positividad del bloque $p$. $\square$

**[LEMA 5.3] (caracterización del núcleo).** $Q_X(f,f)=0\iff\hat F$ se anula en
$\Lambda_p\cup\Lambda_q\iff$ las dos periodizaciones torcidas
$\sum_mF(t+mL_p)e^{i\phi(t+mL_p)/L_p}$ y su análoga en $q$ son idénticamente
nulas — i.e. $f$ es **invisible para ambos factores de Euler**. *(Inmediato de la
identidad espectral y del Lema 5.1/Fourier.)* $\square$

**[TEOREMA 5.4] (el umbral del núcleo es $\log pq$).**
(a) Si $f\ne0$ tiene soporte en una ventana de longitud $2T<\log(pq)$, entonces
$Q_X(f,f)>0$: la forma es **definida** en toda ventana menor que $\log pq$.
(b) Para todo $2T>\log(pq)$ existe un subespacio de dimensión infinita de tests
soportados en una ventana de longitud $2T$ con $Q_X(f,f)=0$. En particular $Q_X$
es semidefinida y **no hay gap uniforme global** en $C_c^\infty(G)$.

*Demostración.* **(a)** Supongamos $Q_X(f,f)=0$ con $f\ne0$. Si
$\operatorname{supp}F\subset[c-T,c+T]$, sea $G:=F(\cdot+c)$; entonces
$\hat F(\xi)=e^{ic\xi}\hat G(\xi)$ con $e^{ic\xi}$ entera y sin ceros: $\hat F$ y
$\hat G$ tienen los mismos ceros, y $\hat G$ es entera de tipo exponencial $\le T$
($|\hat G(\xi+i\eta)|\le\|G\|_1e^{T|\eta|}$) y acotada en $\mathbb R$ por
$\|G\|_1$. Por el Lema 5.3, $\hat G$ se anula en $\Lambda_p\cup\Lambda_q$. Si
$\hat G\not\equiv0$, sus ceros reales son aislados; elegimos $\xi_0\in\mathbb R$
con $\hat G(\xi_0)\ne0$. Jensen en el disco $|\xi-\xi_0|\le R$ (para casi todo
$R$):
$$\int_0^R\frac{n(r)}{r}\,dr
=\frac1{2\pi}\int_0^{2\pi}\log\bigl|\hat G(\xi_0+Re^{i\vartheta})\bigr|\,d\vartheta
-\log|\hat G(\xi_0)|
\;\le\;\log\|G\|_1+\frac{2TR}{\pi}+C_1,$$
usando $|\hat G(\xi_0+Re^{i\vartheta})|\le\|G\|_1e^{TR|\sin\vartheta|}$ y
$\tfrac1{2\pi}\int_0^{2\pi}|\sin\vartheta|\,d\vartheta=\tfrac2\pi$. Por otro lado
$n(r)$ cuenta al menos los puntos de $\Lambda_p\cup\Lambda_q$ en
$[\xi_0-r,\xi_0+r]$: cada progresión de paso $2\pi/L_r$ aporta $\ge rL_r/\pi-2$, y
la superposición es a lo sumo un punto (Lema 1.7):
$n(r)\ge\frac{(L_p+L_q)}{\pi}\,r-C_0$. Integrando desde un $R_0$ fijo:
$$\frac{L_p+L_q}{\pi}\,(R-R_0)-C_0\log\frac{R}{R_0}
\;\le\;\frac{2TR}{\pi}+O(1)\qquad\forall R,$$
de donde $L_p+L_q\le2T$, contradiciendo $2T<\log pq=L_p+L_q$. Luego
$\hat G\equiv0$ y $f=0$. **(b)** Operadores de diferencia: para
$g\in C_c^\infty(\mathbb R)$ sea
$$(D_r\,g)(t):=g(t)-e^{-i\phi_r}\,g(t-L_r),\qquad
\widehat{D_rg}(\xi)=\bigl(1-e^{i(L_r\xi-\phi_r)}\bigr)\hat g(\xi),$$
que se anula exactamente en $\xi\in\Lambda_r$. Tomar $g$ un bump de ancho
$0<\,2T-\log pq\,<\min(2T-\log pq,\,L_p)$ y $F:=D_pD_qg$: entonces
$\hat F$ se anula en $\Lambda_p\cup\Lambda_q$, $\operatorname{supp}F$ cabe en
longitud $|{\operatorname{supp}g}|+L_p+L_q\le2T$, y $F\ne0$ porque el trasladado
extremo $g(\cdot-L_p-L_q)$ tiene soporte disjunto de los otros tres (dista $L_p$ y
$L_q$ de los vecinos, más que el ancho de $g$). El test
$f(e^t):=F(t)e^{-t/2}$ cumple $Q_X(f,f)=0$, $f\ne0$ (Lema 5.3). La dimensión
infinita: $g\mapsto D_pD_qg$ es inyectiva (multiplicador analítico no nulo en
Fourier) sobre un espacio infinito-dimensional de bumps. $\square$

**Observación 5.5 (lectura).** El núcleo no es patología: son los tests que ningún
factor de Euler ve, y la positividad semidefinida es exactamente lo que H pide. Lo
notable es el umbral **aritmético** $\log(pq)$ = logaritmo del conductor
"ingenuo" del objeto: la forma de dos primos es definida exactamente en ventanas
más cortas que $\log$ (producto de los primos). Para $n$ primos el umbral será
$\log(p_1\cdots p_n)$ (§7) — la ventana de definitud crece con el soporte
aritmético del objeto. Esta es la versión cuantitativa, en esta categoría, del
slogan "más primos = más espectro".

**[PROPOSICIÓN 5.6] (las casi-colisiones y su repulsión diofántica; fases
triviales).** Sean $\alpha=\sqrt p$, $\alpha'=\sqrt q$ ($\phi=\phi'=0$), de modo
que $\Lambda_p=(2\pi/L_p)\mathbb Z$, $\Lambda_q=(2\pi/L_q)\mathbb Z$.
(a) [Kronecker/Weyl] $\inf\{|\xi-\eta|:\xi\in\Lambda_p\setminus0,\ \eta\in
\Lambda_q\setminus0\}=0$: las dos progresiones tienen casi-colisiones a toda
escala — la unión **no es uniformemente separada**.
(b) [Baker, efectivo] Existen $C,\kappa>0$ efectivas (dependientes de $p,q$) tales
que para $\xi=2\pi k/L_p\ne\eta=2\pi l/L_q$ en $[-R,R]$:
$$|\xi-\eta|\;=\;\frac{2\pi}{L_pL_q}\,\bigl|\,k\log q-l\log p\,\bigr|
\;\ge\;C\,R^{-\kappa}.$$

*Demostración.* (a) $|2\pi k/L_p-2\pi l/L_q|=\tfrac{2\pi}{L_pL_q}|kL_q-lL_p|$ y
$\{kL_q/L_p \bmod 1\}$ es denso (Lema 1.7 + Kronecker). (b) Es el teorema de
Baker sobre formas lineales en dos logaritmos [DATO: Baker 1966; forma explícita
en Laurent–Mignotte–Nesterenko 1995]: $|k\log q-l\log p|\ge C'\max(|k|,|l|)^{-\kappa}$
con constantes efectivas; en $[-R,R]$, $|k|\le RL_p/2\pi$, $|l|\le RL_q/2\pi$.
$\square$

**Observación 5.7 (la región intermedia, honesta) + [GAP-135.A].** Entre la
ventana $\log q$ (gap uniforme probado, Teorema 5.2(b)) y la ventana $\log pq$
(definitud sin gap declarado, Teorema 5.4(a)) queda la pregunta:
$$\mu(T):=\inf\bigl\{Q_X(f,f):\ \|f\|_w=1,\ \text{ventana }2T\bigr\}\;>\;0
\quad\text{para }\log q<2T<\log pq\ \text{?}$$
Esto es exactamente la pregunta de la **cota de frame inferior** para el sistema de
exponenciales $\{e^{i\xi t}\}_{\xi\in\Lambda_p\cup\Lambda_q}$ en $L^2$ de un
intervalo de longitud $2T$. La condición necesaria de densidad de
Beurling–Landau se cumple ($\tfrac{L_p+L_q}{2\pi}>\tfrac{2T}{2\pi}$), pero los
teoremas de suficiencia estándar piden separación uniforme — destruida por las
casi-colisiones de 5.6(a). La repulsión de Baker 5.6(b) acota la velocidad de
colisión (polinomial) y es plausible que alcance para $\mu(T)>0$ con pérdida
polinomial en la escala, vía frames de diferencias divididas [DATO: Seip,
*Interpolation and sampling*, AMS Univ. Lecture Ser. 33, cap. 2–3]; con fases
$\phi,\phi'$ genéricas no hay repulsión efectiva conocida. **GAP-135.A:** decidir
$\mu(T)>0$ en la región intermedia, con constante explícita en función de la
medida de irracionalidad de $\log p/\log q$. Subrayado: este gap afecta el
**módulo de positividad**, no el signo — el Teorema 3.1 no depende de él. Acá, y
solo acá, vive Kronecker en este problema.

---

## 6. [CÁLCULO] El juguete completo: $p=2$, $q=3$, $\alpha=\sqrt2$, $\alpha'=\sqrt3$

Datos: $c_m=2\cdot2^{m/2}$, $c'_n=2\cdot3^{n/2}$ (fases triviales),
$L_2=\log2\approx0.6931$, $L_3=\log3\approx1.0986$, $\log6\approx1.7918$.
$$W_X(f)=\log2\sum_m2\cdot2^{m/2}f(2^m)\;+\;\log3\sum_n2\cdot3^{n/2}f(3^n).$$
Todos los tests usan el bump $u$ de §4 ($\chi$ par, $\int\chi^2=1$) y los valores
de $g=f\star\tilde f$ calculados allí; los $O(\epsilon)$ se omiten (se absorben
eligiendo $\epsilon$ chico al final, como en §4).

**6.1. Dos protuberancias contra el primo 2.** $f=u-t\,u(\cdot/2^M)$, $t>0$:
$$\tfrac12\,Q_X=\log6\,(1+2^Mt^2)-\log2\cdot2\cdot2^{M/2}\,t
\;\ge\;\log6-\frac{(\log2)^2}{\log6}\;=\;1.5236\ldots\;>\;0,$$
con mínimo en $t^*=\tfrac{\log2}{\log6}\,2^{-M/2}$, **independiente de $M$**. El
mismo test contra el objeto de un primo $F_{2,\sqrt2}$ solo da
$\tfrac12Q=\log2\,(1-2^{M/2}t)^2\cdot\tfrac{2}{2}$ — más precisamente
$Q_{F_2}=2\log2\,\bigl(1-2^{M/2}t\bigr)^2$: un **cuadrado perfecto que se anula**
en $t=2^{-M/2}$ (la positividad de un primo puro es tan justa como puede ser:
Cauchy–Schwarz exacta, Doc 131 §6.5).

**6.2. La dirección crítica del 2, rescatada por el 3.** En el test crítico
$t=2^{-M/2}$ del punto anterior:
$$Q_X=\underbrace{Q_{F_2}}_{=0}+\;Q_{F_3}=2\log3\,\bigl(1+2^M t^2\bigr)
=2\log3\cdot2=4\log3\approx4.394>0.$$
La diagonal del primo 3 (su $c'_0=2$) llena exactamente el cero del primo 2:
interferencia **constructiva** de masas diagonales. (Consistencia con §5: ese test
vive en ventana $\approx M\log2>\log2$, fuera de la zona de identidad 5.2(a), y su
$Q$ es estrictamente positivo pero no proporcional a $\|f\|_w^2$ — el cuadrado del
factor 2 se anuló.)

**6.3. El test doblemente adversario (tres protuberancias).**
$f=u-t_1\,u(\cdot/2^M)-t_2\,u(\cdot/3^N)$, $t_1,t_2>0$, $M,N\ge1$. Los cocientes de
soportes generan puntos en $\{1,2^{\pm M},3^{\pm N},2^M3^{-N},2^{-M}3^N\}$; por
factorización única y $\epsilon$ chico, $W_X$ muestrea solo $1$, $2^{\pm M}$,
$3^{\pm N}$ (los puntos mixtos NO llevan coeficiente — Prop. 1.3 en acto). Con
$g(1)=1+t_1^22^M+t_2^23^N$, $g(2^M)=-t_1$, $g(3^N)=-t_2$ (y espejos):
$$\tfrac12\,Q_X=\log6\,\bigl(1+2^Mt_1^2+3^Nt_2^2\bigr)
-2\log2\cdot2^{M/2}t_1-2\log3\cdot3^{N/2}t_2.$$
Minimizando por separado ($t_1^*=\tfrac{\log2}{\log6}2^{-M/2}$,
$t_2^*=\tfrac{\log3}{\log6}3^{-N/2}$):
$$\min\;\tfrac12\,Q_X=\log6-\frac{(\log2)^2}{\log6}-\frac{(\log3)^2}{\log6}
=\frac{(\log6)^2-(\log2)^2-(\log3)^2}{\log6}
=\frac{2\log2\,\log3}{\log6},$$
es decir
$$\boxed{\ \min Q_X\;=\;\frac{4\,\log2\,\log3}{\log2+\log3}\;\approx\;1.7000\;>\;0\ }$$
— **dos veces la media armónica de $\log2$ y $\log3$, uniforme en $M,N$**. La
identidad detrás: $(\sum_iL_i)^2-\sum_iL_i^2=2\sum_{i<j}L_iL_j$ — el margen de
positividad contra la familia de Mertens es exactamente el **término cruzado de
las masas diagonales**: los cruzados que la convolución no puso en los
coeficientes reaparecen, con signo positivo, en el cuadrado de la diagonal.
Chequeo de coherencia: con un solo primo el margen es $L_p-L_p^2/L_p=0$ —
recupera el cuadrado perfecto de 6.1. ✓

**6.4. El adversario de Kronecker, desacoplado.** El punto mixto más tentador
cerca de la diagonal: $2^3\cdot3^{-2}=8/9$, $\log(8/9)\approx-0.1178$. Test
$f=u+\theta\,u(\cdot\,\cdot\,(9/8))$ con $\epsilon<\tfrac14|\log(8/9)|$: $g$ vive
en $\log x\in\{0,\pm\log(8/9)\}+[-2\epsilon,2\epsilon]$, y **ningún** $2^m$ ni
$3^n$ con $m,n\ne0$ cae ahí: $Q_X=2\log6\cdot g(1)=2\log6\,(1+\tfrac89|\theta|^2)>0$
para todo $\theta$. La fase adversaria no encuentra coeficiente: las
casi-coincidencias multiplicativas $2^a\approx3^b$ (Kronecker) no acoplan con el
lado aritmético porque la masa de Weil en $2^a3^{-b}$ es **cero** (Prop. 1.3). En
el objeto impuro esta protección no existe a lo largo de la propia progresión del
primo impuro — exactamente la diferencia entre §3 y §4.

**6.5. Ventana corta, verificación numérica de 5.2(a).** $f$ real soportada en
$[1,1.9]$ ($2T=\log1.9<\log2$): los cocientes $y/y'\in(1/1.9,1.9)$ no alcanzan
$2^{\pm1},3^{\pm1}$: $Q_X=2\log6\,\|f\|_w^2$, exacto. Cualquier gaussiana
modulada truncada a esa ventana da lo mismo: en ventana corta el objeto es ciego a
toda estructura del test salvo su norma. ✓

---

## 7. [TEOREMA A′ + PUENTE] La inducción y la localización del muro

### 7.1. El teorema de $n$ primos (la inducción es trivial — eso es información)

**[TEOREMA 7.1].** Sean $p_1<\dots<p_n$ primos, $\alpha_i$ puros
($|\alpha_i|=\sqrt{p_i}$), y $X_S:=F_{p_1,\alpha_1}\star\cdots\star F_{p_n,\alpha_n}
=(\sum_ia_i,\,0,\,-2\log(p_1\cdots p_n))$. Entonces:
(a) $X_S$ satisface H y H₂, con
$Q_{X_S}(f,f)=2\sum_{i}\sum_{\xi\in\Lambda_{p_i}}|\hat F(\xi)|^2\ge0$.
(b) Si algún $\alpha_i$ es impuro, H falla (test de dos protuberancias en $p_i$;
los demás primos aportan solo la diagonal $2\sum_{j\ne i}L_{p_j}$, barrera
$|c^{(i)}_M|>2p_i^{M/2}\bigl(\sum_jL_{p_j}\bigr)/L_{p_i}$, superada para $M$
grande): **H $\iff$ pureza de todos los factores.**
(c) Ventana corta $2T\le\log p_1$: $Q_{X_S}=2\log(p_1\cdots p_n)\|f\|_w^2$ exacta;
umbral del núcleo en $2T=\log(p_1\cdots p_n)$ (definida por debajo, núcleo
infinito-dimensional por encima).
(d) Margen contra la familia de Mertens multi-protuberancia:
$\min Q=\tfrac{4\sum_{i<j}L_{p_i}L_{p_j}}{\sum_iL_{p_i}}$, uniforme en las alturas.

*Demostración.* Verbatim las de §3–§6: (a) aditividad (Prop. 1.2, asociativa por
construcción) + Poisson por factor + divisor en la línea; (b) la prueba de 4.1 con
$L_q\rightsquigarrow\sum_{j\ne i}L_{p_j}$ y la separación por factorización única
($p_i^m\ne$ producto de potencias de los otros — finitos candidatos, $\epsilon$
chico); (c) las de 5.2/5.4 con $n$ progresiones (el conteo de Jensen suma
densidades; la construcción usa $D_{p_1}\cdots D_{p_n}g$); (d) la cuenta de 6.3
con $n$ adversarios. $\square$

**El paso $n\to n+1$ no usa nada de $n$:** el argumento es **aditivo**, no
inductivo en sentido fuerte. Esto es información sobre el muro, no una decepción:
significa que toda la dificultad de RH está en el **límite**, no en ningún paso
finito. Localicemos dónde, con precisión.

### 7.2. [PUENTE] Los cuatro puntos de ruptura hacia ζ

Sea $X_y:=\star_{p\le y}F_{p,\alpha_p}$ (todos puros) y miremos $y\to\infty$.
Declaración previa, sin maquillaje: el límite de los $X_y$ **no es** $\zeta$ — y
entender exactamente por qué es el contenido de este puente.

**B1 (la masa diagonal diverge).** $\omega_y\equiv-2\sum_{p\le y}\log p=-2\theta(y)
\to-\infty$. Para $f$ fija con $f(1)\ne0$, los primos $p>e^{2T}$ (fuera de la
ventana) aportan cada uno $2L_p\,f(1)$: $W_{X_y}(f)=2\theta(y)f(1)+O_f(1)$
**diverge**. El objeto límite no tiene $\omega$ admisible: hay que renormalizar
(restar $2\theta(y)\delta_1$). En ζ, el papel de esa masa diagonal infinita lo
cumple un dato de otro tipo: el bloque polar $[0]+[1]$ más la densidad
arquimediana $\Omega(t)\sim2\log(t/2\pi)$ — **constante divergente en $y$
canjeada por crecimiento en $t$**. Ese canje es la aparición del factor gamma/el
conductor, y no es un paso de la categoría: es la continuación analítica entrando
por la ventana.

**B2 (divisor del límite ≠ límite de divisores; la positividad pasa, la
espectralidad no).** Cada $X_y$ es espectral con divisor = unión de retículas
**sobre la línea crítica** (¡pureza!), $N_{Z_y}(T)\sim\tfrac{2\theta(y)}{\pi}T$.
Si los funcionales renormalizados convergieran a un funcional $W_\infty$, la
positividad $Q_\infty\ge0$ pasaría al límite sin esfuerzo (límite puntual de
formas $\ge0$). Lo que NO pasa al límite es la **fórmula explícita**: la serie de
Dirichlet $\prod_pD_{p,\alpha_p}(s)^{-1}$-style asociada diverge en la banda
crítica, y los ceros de la continuación del producto infinito (si existe) no son
límites de los ceros de los productos parciales — las retículas se densifican
($N(T)/T\to\infty$) y el divisor límite verdadero tiene $N(T)\sim cT\log T$,
otra clase de crecimiento. **La transmutación está aquí: el funtor de comparación
$U$ (Doc 131 §7.2) conmuta con límites en $\mathcal{A}rith$ pero no en
$\mathcal{A}rith^{EF}$.** En la fórmula del programa: la positividad es estable
por límites débiles; la *espectralidad* (existencia del divisor con EF) es
exactamente lo que el límite debe re-probar, y eso es la continuación analítica +
el contorno de Weil — RH-dura.

**B3 (el desajuste de peso: ζ no es el límite de sus propios factores puros).**
Los objetos puros de este documento tienen peso local 1: $|\alpha_p|=\sqrt p$,
simetría $\sigma:s\mapsto1-\bar s$ **factor a factor**. Los factores de Euler de
ζ tienen $\alpha=1$, $|\alpha|=1=\sqrt{p^0}$: peso 0. Leído como objeto de un
primo en nuestra normalización, el factor de ζ tiene $c_m=1+p^m$ — violación
**maximal** de la barrera de Ramanujan $|c_m|\le2p^{m/2}$ (sus ceros locales
viven en $\mathrm{Re}=0$ y $\mathrm{Re}=1$, no en $\tfrac12$): **cada factor de ζ
es $\sigma$-impuro y, aislado, viola H** (Doc 131, Teorema 6.7). La simetría
$s\leftrightarrow1-\bar s$ de ζ no es local: la fabrica la ecuación funcional
global (polo + gamma) — el recentrado del peso $0$ al $\tfrac12$ es un fenómeno
**global**. Consecuencia para la Conjetura H⁺: nuestros objetos puros tienen
término aritmético **constructivo** (los $c_m>0$ entran sumando con la diagonal:
en el slot del objeto, $a(p^m)=-L_pc_m\le0$), mientras que la clase de H⁺ pide
$a\ge0$ ($a=\Lambda$-like): régimen **destructivo**, donde los primos restan y la
positividad debe venir del bloque polar. El Teorema 3.1 es el primer teorema de
dos primos de la categoría, pero vive en el régimen constructivo; **no es
todavía el paso inductivo de H⁺** — es su gemelo especular. (Es exactamente la
dicotomía constructivo/destructivo que el programa ya conocía a nivel de picos y
valles; acá aparece como signo del dato $a$ relativo a la diagonal.)
**[GAP-135.B]:** el primer caso genuino de H⁺: el objeto semilocal
$(\Lambda\cdot1_{\{2^m,3^n\}},\,[0]+[1],\,\omega_{\mathrm{std}})$ — dos primos,
$a\ge0$, bloque polar estándar. Decidir H para ese objeto (es la Conjetura 100.A
del programa en su versión mínima de dos primos; un contraejemplo refutaría H⁺).
Ese es el Doc 136 natural.

**B4 (el orden de los límites ventana/primos).** Los teoremas finitos viven en el
cuadrante "primos $\le y$ fijo, ventana $2T<\log\prod_{p\le y}p=\theta(y)$": la
zona de definitud crece con $y$ (Teorema 7.1(c)) — la dirección es la correcta.
Pero el gap por debajo del umbral es, tras renormalizar la diagonal divergente
(B1), una afirmación sobre $W_{X_y}-2\theta(y)\delta_1$, y la familia de tests
relevante para ζ exige $T\to\infty$ **antes** que $y$ (el criterio de Weil
cuantifica sobre todos los tests de una vez, y los ceros de ζ requieren ventanas
arbitrarias). El enunciado fino que falta es exactamente el Lema de rigidez del
límite (Doc 131, Deseo 7.2): gap $\mu_y(T)$ con control conjunto en $(y,T)$ que
sobreviva a $\lim_T\lim_y\ \ne\ \lim_y\lim_T$. Los Teoremas 5.2/5.4/7.1(c) dan
la primera información cuantitativa real sobre $\mu_y(T)$: identidad exacta en
ventana corta, umbral de núcleo en $\theta(y)$, y la obstrucción diofántica
(GAP-135.A) como único ingrediente faltante en la región intermedia.

**Síntesis del puente.** El paso de positividad es aditivo e indestructible; la
transmutación hacia ζ DEBE ocurrir, y ocurre, en B2 (espectralidad del límite =
continuación analítica) alimentada por B1 (renormalización de la diagonal) y
enmascarada por B3 (el cambio de régimen constructivo→destructivo: ζ no está en
la clausura de los objetos puros de peso 1, sino en la clase H⁺ con polar). Quien
quiera el límite tiene que pagar exactamente ahí — ahora se sabe el precio y la
ventanilla.

---

## 8. El mapa

**Probado [TEOREMA], con prueba completa en este documento:**
- Ley de composición: $W$ aditivo bajo $\star$; masa de Weil cero en el soporte
  mixto $p^aq^b$ (Prop. 1.2–1.3, vía Doc 131 Lema 1.7).
- $X_{p,q}$ hermitiano, admisible, espectral; divisor = dos progresiones
  inconmensurables, no retícula (Lemas 1.6–1.7, Prop. 2.1).
- **Teorema A (3.1):** pureza bilateral $\Rightarrow$ H y H₂, identidad espectral
  exacta — primer teorema de positividad de Weil con dos primos inconmensurables,
  externo a ζ.
- **Teorema B (4.1) y Corolario 4.2:** impureza de cualquier factor $\Rightarrow$
  $\neg$H, con test explícito; H decidible en la subcategoría de dos primos:
  **H $\iff$ pureza bilateral** (barrera corrida a $2p^{M/2}(1+L_q/L_p)$).
- **Estructura fina (5.1–5.4):** identidad $Q=2\log(pq)\|f\|_w^2$ en ventana
  $\le\log\min(p,q)$; gap $2\log q$ hasta $\log q$, uniforme en el segundo primo;
  umbral del núcleo exactamente en $\log(pq)$ (Jensen + construcción); núcleo =
  tests invisibles para ambos factores.
- Repulsión de casi-colisiones por Baker con fases triviales (Prop. 5.6;
  [DATO] Baker/LMN).
- **Teorema A′ (7.1):** todo lo anterior para $n$ primos, con margen de Mertens
  $4\sum_{i<j}L_iL_j/\sum_iL_i$ y umbral de núcleo $\log(p_1\cdots p_n)$.
- [CÁLCULO §6] El juguete $2$–$3$ completo: mínimos $1.5236$, $4\log3$,
  $4\log2\log3/\log6\approx1.7000$; desacople del adversario mixto $8/9$.

**[PUENTE] (estatus declarado):** B1–B4 (§7.2) — la localización del muro: la
positividad pasa al límite, la espectralidad no; ζ no es límite de sus factores
(peso 0 vs 1, régimen destructivo vs constructivo); el canje
$\theta(y)\leftrightarrow\Omega(t)$ es la continuación analítica. Nada de esto
acerca RH; redistribuye la dificultad a un punto nombrado del funtor $U$.

**[DESEO]:** que el margen aditivo $2\sum_{i<j}L_iL_j/\log P$ tenga un análogo
renormalizado que sobreviva a $y\to\infty$ (la forma fuerte del Lema de rigidez,
Doc 131 Deseo 7.2).

**[GAP], nombrados:**
- **GAP-135.A:** gap uniforme en ventanas intermedias
  $\log q<2T<\log pq$ — frames de exponenciales sobre dos progresiones
  inconmensurables; la constante debe depender de la medida de irracionalidad de
  $\log p/\log q$ (Baker da la repulsión; falta el teorema de frame).
- **GAP-135.B:** el objeto semilocal con $a\ge0$ y bloque polar estándar
  (dos primos, régimen destructivo): el primer test genuino de H⁺ y el contenido
  mínimo de la Conjetura 100.A. **Siguiente documento.**

---

## Referencias

**Internas (backward-only):** Doc 131 (categoría $\mathcal{A}rith$: Def. 2.1,
Lema 1.7, Prop. 2.8, Def. 4.1, Teo. 4.4, Teo. 4.9, Prop. 6.2, Teo. 6.6, Teo. 6.7,
Deseo 6.9, Deseo 7.2, §9); Doc 125 (G-125.B: dos primos inconmensurables);
Doc 107 (funcional de Weil de dos variables, núcleo engrosado); Doc 110 (clase
$\mathcal F$, test-accesibilidad); Doc 119 (R-NC/NC2).

**Literatura [DATO]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Comm. Sém. Math. Lund (1952), 252–265.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
  numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233.
- A. Baker, *Linear forms in the logarithms of algebraic numbers*, Mathematika 13
  (1966), 204–216; A. Baker, *Transcendental Number Theory*, CUP 1975.
- M. Laurent, M. Mignotte, Y. Nesterenko, *Formes linéaires en deux logarithmes et
  déterminants d'interpolation*, J. Number Theory 55 (1995), 285–321 (dos
  logaritmos, constantes explícitas).
- R. P. Boas, *Entire Functions*, Academic Press 1954 (tipo exponencial, Jensen,
  densidad de ceros).
- K. Seip, *Interpolation and Sampling in Spaces of Analytic Functions*, AMS Univ.
  Lecture Series 33, 2004 (frames de exponenciales, densidades de
  Beurling–Landau).
- H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, CUP 2007
  (Mertens, $3+4\cos\theta+\cos2\theta$).

*Fin del Documento 135.*
