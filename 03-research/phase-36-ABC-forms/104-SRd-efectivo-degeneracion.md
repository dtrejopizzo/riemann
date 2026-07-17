# Doc 104 — SR_d efectivo: la degeneración cuantitativa en d→0

**Phase 36 — Formas A/B/C · junio 2026**
**Autor: David Alejandro Trejo Pizzo**
**Responde: Problema 8.1 (Forma C) de P41 (`06-papers/P41-exhaustion-1d-propagation/main.tex`, §Form C)**
**Insumo principal: Doc 102 (`phase-35-five-fronts/102-bagchi-voronin-auditoria.md`), §§3–6**

---

## 0. Resumen ejecutivo

El Problema 8.1 de P41 plantea una dicotomía: si las constantes de las pruebas
incondicionales de $(\mathrm{SR}_d)$ degeneran exponencialmente ($e^{-c/|d|}$) cuando
$d\to0$, la línea cierra como MW-2 cuantificado; si degeneran polinomialmente en $1/|d|$,
hay tensión genuina con el argumento de Rouché. Este documento resuelve el problema y el
resultado es más fino que ambas ramas: **la dicotomía, tal como está planteada, es falsa
— y la línea cierra igual, por una razón más precisa que cualquiera de las dos ramas.**

Hallazgos:

1. **La densidad límite no degenera.** Existe $d_0(\varepsilon)>0$ tal que para todo
   $0<|d|<d_0(\varepsilon)$ la densidad inferior $\delta(d,\varepsilon)$ de
   $(\mathrm{SR}_d)$ admite una cota inferior $\delta_*(\varepsilon)>0$ **uniforme en
   $d$** (Teorema 4.1, con gap técnico declarado y acotado). Más aún: por debajo de
   $d_0(\varepsilon)$ **toda la teoría diofántica desaparece** — racional, algebraico y
   trascendente se vuelven indistinguibles a precisión $\varepsilon$ (Proposición 3.1).
   Baker y los seis exponenciales solo trabajan en la banda $|d|\ge d_0(\varepsilon)$.
2. **Lo que degenera es la escala, y degenera linealmente.** El primer $T$ a partir del
   cual la densidad positiva es visible satisface $T_0(d,\varepsilon)\asymp
   C(\varepsilon)/|d|$: cota superior por equidistribución efectiva (Teorema 4.1), cota
   inferior $\ge \eta/|d|$ incondicional-estructural y, bajo $\neg$RH con $K$ anclado en
   el cero, genuina (Proposición 4.3). Degradación **polinomial — de hecho lineal — en
   $1/|d|$**: la rama "tensión" de la dicotomía.
3. **Y sin embargo no hay tensión.** El argumento de Rouché no necesita
   $(\mathrm{SR}_d)$ a gran escala: necesita su densidad **dentro de la ventana anclada**
   $J_d=\{\tau: d\tau\approx\gamma_0\}$, de medida $\asymp 1/|d|$ — exactamente la escala
   donde el teorema efectivo aún no entrega nada y donde la copia lenta
   $\zeta(s+id\tau)$ está **congelada**. Ahí el enunciado colapsa a aproximar el objetivo
   fijo $\zeta(\cdot+i\gamma_0)$, que tiene un cero: objetivo prohibido, densidad
   demostrable exactamente $0$ (Módulo 5 de Bagchi, Hurwitz). El gap no es una tasa: es
   el muro binario $0$ vs $>0$.
4. **El gap cuantitativo exacto (Teoremas 5.2–5.3).** Con $\sigma=\beta_0-3\eta$ y
   $\kappa(\sigma)>0$ el exponente del teorema de densidad de ceros
   ($\kappa=(2\sigma-1)^2$ con Carlson; $\kappa=(2\sigma-1)/(2-\sigma)$ con Ingham):
   densidad anclada $\ge c\,|d|^{\kappa'}$ con $\kappa'<\kappa$ para una sucesión
   $d\to0$ **implicaría RH** (Teorema 5.2); pero bajo $\neg$RH la densidad anclada
   verdadera está acotada por $C\,|d|^{\kappa}$ — **el mismo exponente** (Teorema 5.3).
   Lo necesario y lo máximo-posible difieren solo en constantes, y lo demostrable es
   $0$. Mejorar el teorema de densidad de ceros mueve ambos lados a la vez: el
   mecanismo es **auto-bloqueante**. Esto es MW-2 cuantificado.
5. **$d=d(T)$ móvil no esquiva nada (Lema 6.1, complementariedad):** anclar exige
   $|d(T)|\,T=O(1)$ (copia lenta congelada ⟹ colapso a $\mathrm{SR}_0$); equidistribuir
   la copia lenta exige $|d(T)|\,T\to\infty$ (sin ancla ⟹ a lo sumo $o(T)$ ceros, sin
   contradicción). Los dos regímenes son exhaustivos y disjuntos para toda función
   $d(T)$.

**VEREDICTO: RUTA CERRADA** — con la dicotomía de 8.1 corregida: degradación polinomial
(lineal) en la escala, ninguna en la densidad, y cierre limpio porque la cantidad que
Rouché necesita no es ninguna de las dos: es la densidad en la ventana anclada, donde el
muro es binario (Hurwitz), no cuantitativo. §9.

---

## 1. El problema, notación y estado del arte verificado

### 1.1 Enunciados

Para $d\in\mathbb{R}$, $K\subset D(1/2,1)=\{s:1/2<\mathrm{Re}\,s<1\}$ compacto con
complemento conexo y $\varepsilon>0$:

$$(\mathrm{SR}_d)\qquad
\liminf_{T\to\infty}\ \frac1T\,\mathrm{meas}\Big\{\tau\in[0,T]\ :\ \sup_{s\in K}\big|\zeta(s+i\tau)-\zeta(s+id\tau)\big|<\varepsilon\Big\}\ >\ 0.$$

Escribimos $\delta(d,\varepsilon;K)$ para el liminf y $\delta(d,\varepsilon)$ cuando $K$
está fijo. $(\mathrm{SR}_0)=(\mathrm{SR})$ es RH (Bagchi 1987; Doc 102, Teorema 2.2).

### 1.2 Estado del arte (verificado en esta sesión)

- $d$ **algebraico irracional**: $(\mathrm{SR}_d)$ incondicional — Nakamura, *The
  generalized strong recurrence for non-zero rational parameters*, Arch. Math. **95**
  (2010), 549–555 (la parte algebraica), vía universalidad conjunta + **teorema de
  Baker**.
- $d$ **trascendente**: Pańkowski, vía el **teorema de los seis exponenciales**
  (expuesto en Matsumoto, arXiv:1407.4216, §9).
- $d=a/b$ **racional**, $(a,b)=1$, $|a-b|\neq1$: Nakamura–Pańkowski, Arch. Math. **99**
  (2012), 43–47 (corrigendum; verificado vía arXiv:1203.1393: el corrigendum prueba
  $\zeta$ para $|a-b|\neq1$ y $\log\zeta$ para todo $d\neq0$). El caso $|a-b|=1$ fue
  resuelto después por Pańkowski para todo racional $d\neq0,\pm1$ [reportado en fuentes
  secundarias; el paper específico NO VERIFICADO en texto completo].
- **Intervalos cortos**: Garunkštis et al. (Symmetry **17** (2025), art. 2075) muestran
  que la auto-aproximación **en intervalos cortos** con $d=0$ es de nuevo
  RH-equivalente [verificado solo a nivel de abstract; NO VERIFICADO en detalle]. Esto
  es consistente con — y anticipa — el §5.4 de este doc.

**Observación 1.1 (los racionales cerca de $0$ no son problemáticos).** Si $d=a/b$ con
$0<|d|<1/2$ y $(a,b)=1$, entonces $|a|<b/2$, luego $|a-b|>b/2\ge1$. El caso técnico
$|a-b|=1$ (el único que estuvo abierto) **no ocurre en ningún entorno de $d=0$**: para
la pregunta de este documento, el corrigendum de 2012 ya cubre todos los racionales
relevantes. ∎

### 1.3 Qué pide exactamente la Forma C

P41, Problema 8.1: comportamiento de las constantes de las pruebas cuando $d\to0$;
dicotomía $e^{-c/|d|}$ (cierre MW-2) vs polinomial (tensión con Rouché). Las constantes
relevantes son dos, y el primer resultado del doc es que se comportan de manera opuesta:

- $\delta(d,\varepsilon)$ — la densidad inferior (¿se hunde cuando $d\to0$?);
- $T_0(d,\varepsilon)$ — la escala a partir de la cual la densidad es visible
  (equivalentemente, el primer $\tau$ garantizado).

---

## 2. Anatomía de la prueba de $(\mathrm{SR}_d)$: dónde entra $d$ (pregunta i)

### 2.1 Los cinco módulos en versión bivariada

La prueba de $(\mathrm{SR}_d)$ es la maquinaria de Bagchi (Doc 102, §3) corrida sobre el
**par** de shifts. Sea $\Omega=\prod_p\mathbb{T}_p$ el toro de Bohr. El objeto dinámico
es la órbita
$$\tau\ \longmapsto\ \big(\,(p^{-i\tau})_p,\ (p^{-id\tau})_p\,\big)\ \in\ \Omega\times\Omega,$$
con clausura $H_d:=\overline{\{\cdot\}}\le\Omega\times\Omega$, subgrupo cerrado conexo.
Los caracteres de $\Omega\times\Omega$ son pares $(n,m)$ de vectores enteros de soporte
finito indexados por primos, y actúan sobre la órbita por $e^{-i\tau\lambda_{n,m}(d)}$ con

$$\boxed{\ \lambda_{n,m}(d)\ =\ \Lambda_0(n)+d\,S(m),\qquad
\Lambda_0(n)=\sum_p n_p\log p,\quad S(m)=\sum_p m_p\log p.\ }$$

Toda la dependencia en $d$ de la teoría entra por el **espectro de frecuencias**
$\{\lambda_{n,m}(d)\}$ y por el **retículo de relaciones**
$R_d=\{(n,m):\lambda_{n,m}(d)=0\}$, que determina $H_d$ (el anulador de $R_d$).

- **Módulo 1–2 (toro y flujo):** el flujo bivariado es la traslación por el subgrupo
  uniparamétrico de frecuencias $\{\log p\}\cup\{d\log p\}$; es uniquely ergodic sobre
  $H_d$ (rotación de grupo compacto, Walters GTM 79).
- **Módulo 3 (elementos aleatorios):** el par $(\zeta(s,\omega_1),\zeta(s,\omega_2))$
  con $(\omega_1,\omega_2)\sim$ Haar$(H_d)$.
- **Módulo 4 (teorema límite):** las estadísticas empíricas del par de shifts convergen
  a la ley del par aleatorio. Inputs: medias cuadráticas de $\zeta$ en $\sigma>1/2$
  (cada copia por separado, **independientes de $d$** salvo el reescalado de la copia
  lenta, §4) y Birkhoff sobre $H_d$.
- **Módulo 5 (soporte + positividad):** el evento de auto-aproximación tiene
  probabilidad límite positiva. Aquí la situación es **mejor** que en universalidad: el
  objetivo del par es la **diagonal** ("las dos copias cerca una de la otra"), no una
  función externa. El punto $(\omega_0,\omega_0)$ (fases triviales en ambas copias)
  pertenece a $H_d$ para **todo** $d$ (es la órbita en $\tau=0$), y en un entorno de
  $(\omega_0,\omega_0)$ los dos productos de Euler truncados están ambos cerca de
  $\zeta_X(s)$, que **no se anula**. El muro de Hurwitz no se toca — mientras el
  objetivo sea la diagonal y no $\zeta$ misma. (Esta es la razón estructural por la que
  $(\mathrm{SR}_d)$, $d\neq0$, es demostrable y $(\mathrm{SR}_0)$ no: en
  $(\mathrm{SR}_0)$ la segunda copia ES $\zeta$, con sus ceros.)

### 2.2 El papel de cada clase diofántica de $d$

El retículo $R_d$: $(n,m)\in R_d$ $\iff$ $\Lambda_0(n)=-d\,S(m)$.

**(a) $d$ algebraico irracional — Baker.** Una relación con $(n,m)\neq(0,0)$ forzaría
$\sum_p(n_p+d\,m_p)\log p=0$, una combinación lineal de $\{\log p\}$ con coeficientes
algebraicos no todos nulos. Como $\{\log p\}$ es linealmente independiente sobre
$\mathbb{Q}$ (factorización única), el **teorema de Baker** (1966–67: independencia
lineal sobre $\mathbb{Q}$ de logaritmos de algebraicos implica independencia sobre
$\overline{\mathbb{Q}}$) da contradicción. Luego $R_d=0$, $H_d=\Omega\times\Omega$, y el
límite es el **par independiente** $(\zeta(s,\omega_1),\zeta(s,\omega_2))$, Haar
producto.

**(b) $d$ trascendente — seis exponenciales.** La trascendencia NO impide relaciones:
$d=\log3/\log2$ es trascendente (Gelfond–Schneider) y satisface $d\log2-\log3=0$. Lo que
el **teorema de los seis exponenciales** da: el grupo multiplicativo
$G_d=\{r\in\mathbb{Q}_{>0}: r^d\in\mathbb{Q}\}$ tiene rango $\le2$. (Si $r_1,r_2,r_3$
fueran multiplicativamente independientes con $r_j^d\in\mathbb{Q}$: tomar $x_1=1,x_2=d$
— l.i. sobre $\mathbb{Q}$ pues $d\notin\mathbb{Q}$ — e $y_j=\log r_j$ — l.i. por
independencia multiplicativa; los seis números $e^{x_iy_j}\in\{r_j,r_j^d\}$ serían todos
algebraicos, contradiciendo el teorema.) Las relaciones de $R_d$ están confinadas a un
subgrupo de rango $\le2$ de primos "malos" efectivamente finito-generado; la prueba de
Pańkowski excluye esos generadores del juego de fases y trabaja con el resto (el
steering del Módulo 5 solo necesita co-finitos primos). $H_d$ es un subtoro de
codimensión $\le2$ en el sentido de caracteres, que contiene la diagonal en
$(\omega_0,\omega_0)$.

**(c) $d=a/b$ racional — subtoro grande.** $R_d=\{(n,m): b\,\Lambda_0(n)+a\,S(m)=0\}
=\{(n,m)=(-a\,k,\,b\,k)\}$ (usando independencia de $\{\log p\}$): un retículo de rango
infinito pero de **índice grueso $\max(|a|,b)$**: toda relación tiene coeficientes
múltiplos de $(a,b)$. $H_d=\{(\omega^{\,b},\omega^{\,a}):\omega\in\Omega\}$. El par
límite es $(\zeta(s,\omega^b),\zeta(s,\omega^a))$ — **dependiente** — y la positividad
del Módulo 5 requiere navegar la dependencia; ahí vivía la dificultad $|a-b|=1$. Por la
Observación 1.1, irrelevante cerca de $d=0$; además los coeficientes de las relaciones
tienen tamaño $\ge b\ge 1/|d|\to\infty$ — el punto clave del §3.

### 2.3 La estructura de constantes de una versión efectiva

Cualquier efectivización del esquema anterior (no escrita en la literatura para
$\mathrm{SR}_d$; estructura estándar) tiene tres parámetros internos para precisión
$\varepsilon$ sobre $K$:

- $X(\varepsilon)$: truncación de primos — $\zeta_X(s)=\prod_{p\le X}(1-p^{-s})^{-1}$
  (o una versión suavizada) aproxima a $\zeta$ en media cuadrática sobre shifts:
  $\frac1T\int_0^T\sup_K|\zeta(s+i\tau)-\zeta_X(s+i\tau)|^2\,d\tau<\varepsilon_1$ para
  $T\ge T_1(X)$. Incondicional, vía momentos de orden 2 en $\sigma>1/2$;
  **independiente de $d$** (se aplica a cada copia; para la copia lenta, ver §4.1).
- $M(\varepsilon)$: grado máximo de los caracteres del toro finito
  $\mathbb{T}^{2\pi(X)}$ necesarios para resolver el evento (regularización de la
  indicatriz del evento por polinomios trigonométricos).
- equidistribución: sumas de Weyl
  $\big|\frac1T\int_0^Te^{i\lambda_{n,m}(d)\tau}d\tau\big|\le\frac{2}{T\,|\lambda_{n,m}(d)|}$
  para todos los caracteres $0<\max(|n|_\infty,|m|_\infty)\le M$, soporte en $p\le X$,
  $(n,m)\notin R_d$.

**Toda la dependencia en $d$ está en el tercer punto**: cotas inferiores para
$|\lambda_{n,m}(d)|$ (denominadores pequeños) y la estructura de $R_d$. Es exactamente
donde el Problema 8.1 espera encontrar a Baker. La sorpresa es el §3.

---

## 3. El régimen libre de diofantina: $|d|<d_0(\varepsilon)$ (nuevo)

**Proposición 3.1.** *Sean $X\ge2$, $M\ge1$. Definí*
$$d_0(X,M)\ :=\ \frac{e^{-2MX}}{4MX}.$$
*Entonces para todo real $d$ con $0<|d|<d_0(X,M)$ y todo carácter $(n,m)$ con soporte en
$p\le X$, alturas $|n_p|,|m_p|\le M$, $(n,m)\neq(0,0)$:*

*(a) $\lambda_{n,m}(d)\neq0$ — no hay NINGUNA relación visible a precisión $(X,M)$,
cualquiera sea la clase diofántica de $d$;*

*(b) cuantitativamente:*
$$|\lambda_{n,m}(d)|\ \ge\ \begin{cases}
\tfrac12\,e^{-2MX} & \text{si } n\neq0,\\[2pt]
|d|\,\log 2 & \text{si } n=0,\ m\neq0.
\end{cases}$$

*Prueba.* Si $n\neq0$: $\Lambda_0(n)=\log(A/B)$ con $A=\prod_{n_p>0}p^{n_p}$,
$B=\prod_{n_p<0}p^{-n_p}$ enteros coprimos, $A\neq B$ (factorización única),
$\max(A,B)\le\prod_{p\le X}p^{M}=e^{M\theta(X)}\le e^{2MX}$. Por
$|\log(A/B)|\ge|A-B|/\max(A,B)\ge1/\max(A,B)$:
$|\Lambda_0(n)|\ge e^{-2MX}$. Por otro lado
$|d\,S(m)|\le|d|\,M\,\theta(X)\le|d|\cdot2MX<e^{-2MX}/2$ por la definición de $d_0$.
Luego $|\lambda_{n,m}(d)|\ge|\Lambda_0(n)|-|d\,S(m)|\ge\frac12 e^{-2MX}>0$.
Si $n=0,m\neq0$: $\lambda=d\,S(m)$ y $|S(m)|\ge\log2$ (es $\log$ de un racional
$\neq1$ con denominador y numerador $\ge1$, el mínimo es $\log2$). ∎

**Corolario 3.2 (colapso de las clases diofánticas).** Para $|d|<d_0(X(\varepsilon),
M(\varepsilon))=:d_0(\varepsilon)$, la equidistribución finito-dimensional que la prueba
de $(\mathrm{SR}_d)$ necesita a precisión $\varepsilon$ **no usa ningún teorema
diofántico**: ni Baker, ni seis exponenciales, ni el análisis de subtoro racional. Las
relaciones exactas que $d$ racional o $d=\log r_1/\log r_2$ poseen tienen coeficientes
de tamaño $\ge c/(|d|\,X)$ (para $d=a/b$: tamaño $\ge b\ge1/|d|$), invisibles bajo la
truncación $(X,M)$. A precisión fija, **todas las clases de $d$ se comportan igual
cuando $d\to0$**. ∎

**Interpretación.** El Problema 8.1 presupone que la degradación en $d\to0$ viene de la
teoría trascendente (constantes de Baker $C(n)\,h(d)\,\prod\log A_i$). La Proposición
3.1 muestra que no: la teoría trascendente gobierna el régimen $|d|\ge d_0(\varepsilon)$
(fijo, $\varepsilon\to0$), no el régimen $d\to0$ ($\varepsilon$ fijo). En el límite
$d\to0$ la única frecuencia pequeña es la **trivial**: los caracteres puros de la copia
lenta, $\lambda_{0,m}=d\,S(m)$, lineales en $d$. La degradación es **kinemática, no
aritmética**.

### 3.3 El régimen $|d|\ge d_0(\varepsilon)$: donde sí vive Baker (pregunta ii, parte diofántica)

Para completar la respuesta a (i)–(ii) en el régimen complementario (que NO es el límite
$d\to0$, pero el Problema 8.1 pide la traducción):

- **$d=a/b$ racional, o algebraico:** $b\,\lambda_{n,m}(d)=b\,\Lambda_0(n)+a\,S(m)$ es
  una forma lineal en $\{\log p\}_{p\le X}$ con coeficientes enteros de tamaño
  $\le\max(|a|,b)\,M$. Baker–Wüstholz (1993): para una forma lineal no nula
  $\Lambda=\sum_{i=1}^{N} b_i\log\alpha_i$ con $\alpha_i$ algebraicos y $b_i$ enteros,
  $$\log|\Lambda|\ \ge\ -\,C(N,D)\,h'(\alpha_1)\cdots h'(\alpha_N)\,\log B,\qquad
  C(N,D)=18\,(N+1)!\,N^{N+1}(32D)^{N+2}\log(2ND),$$
  con $B=\max|b_i|$, $D$ el grado del cuerpo, $h'$ alturas modificadas. Aquí $N=\pi(X)$,
  $\alpha_i=p_i$, $h'(p)\asymp\log p$, $B\le\max(|a|,b)M\asymp M/|d|$. Resultado:
  $$|\lambda_{n,m}(d)|\ \ge\ \exp\big(-C(\varepsilon)\,\log(M/|d|)\big)\ =\
  c(\varepsilon)\,|d|^{\,C(\varepsilon)},\qquad
  C(\varepsilon)=C(\pi(X),1)\,\textstyle\prod_{p\le X}\log p,$$
  **polinomial en $1/|d|$** con exponente $C(\varepsilon)$ gigantesco
  (super-exponencial en $X(\varepsilon)$) pero independiente de $d$. La degradación
  diofántica, donde existe, es polinomial — nunca $e^{-c/|d|}$.
- **$d$ trascendente:** no hay medida de irracionalidad general; existen $d$
  trascendentes "tipo Liouville-logarítmico" (extremadamente bien aproximables por
  cocientes $\Lambda_0(n)/S(m)$) para los cuales $T_0(d,\varepsilon)$ a $d$ FIJO es
  arbitrariamente grande: la prueba por seis exponenciales es **inefectiva** y no puede
  no serlo uniformemente. Pero de nuevo: para $|d|<d_0(\varepsilon)$ esto es irrelevante
  (Prop. 3.1 es incondicional y uniforme).

---

## 4. La degeneración cuantitativa real (pregunta ii)

### 4.1 Cota superior: el teorema efectivo uniforme

**Teorema 4.1 (estructura efectiva de $\mathrm{SR}_d$ cerca de $d=0$).** *Fijá $K\subset
D(1/2,1)$ compacto con complemento conexo y $\varepsilon>0$. Existen
$d_0(\varepsilon)>0$, $\delta_*(\varepsilon)>0$ y $C(\varepsilon)<\infty$ tales que para
todo real $d$ con $0<|d|<d_0(\varepsilon)$:*

*(a) $\delta(d,\varepsilon)\ \ge\ \delta_*(\varepsilon)$ — **uniforme en $d$**: la
densidad inferior NO tiende a $0$;*

*(b) la densidad es visible desde la escala $C(\varepsilon)/|d|$: para todo
$T\ge C(\varepsilon)/|d|$,*
$$\frac1T\,\mathrm{meas}\big\{\tau\in[0,T]:\ \sup_K|\zeta(s+i\tau)-\zeta(s+id\tau)|<\varepsilon\big\}\ \ge\ \tfrac12\,\delta_*(\varepsilon).$$

*Esquema de prueba (con gaps declarados).* (1) Reducción en media cuadrática: con
$X=X(\varepsilon)$, ambas copias se reemplazan por $\zeta_X$ fuera de un conjunto de
$\tau$ de densidad $<\delta_*/10$; para la copia rápida esto vale para $T\ge
T_1(\varepsilon)$; para la copia lenta, el cambio de variable $u=d\tau$ da
$\frac1T\int_0^T f(d\tau)\,d\tau=\frac1{|d|T}\int_0^{|d|T}f(u)\,du$, de modo que el
mismo input incondicional se aplica en cuanto $|d|T\ge T_1(\varepsilon)$ — primera
fuente del factor $1/|d|$. (2) El evento truncado depende de las $2\pi(X)$ coordenadas
$(p^{-i\tau},p^{-id\tau})_{p\le X}$; se regulariza por polinomios trigonométricos de
grado $\le M(\varepsilon)$ (suavizado del borde del evento). (3) Weyl + Proposición 3.1:
todos los caracteres no triviales tienen
$|\lambda|\ge\min(\frac12e^{-2MX},\,|d|\log2)$, luego las medias empíricas de los
polinomios de grado $\le M$ están a distancia $<\delta_*/10$ de sus medias respecto de
Haar$(\mathbb{T}^{2\pi(X)}\times\mathbb{T}^{2\pi(X)})$ en cuanto
$T\ge C'(\varepsilon)/|d|$ — segunda fuente, y dominante, del factor $1/|d|$. Notar:
por la Prop. 3.1 la medida límite finito-dimensional es **Haar pleno** para TODO
$0<|d|<d_0$, también racional — el subtoro $H_d$ es $(X,M)$-denso. (4) Positividad
$d$-independiente: el evento límite contiene el entorno
$\{(\vec\theta_1,\vec\theta_2):|\theta_{j,p}|<\rho(\varepsilon)\ \forall p\le X\}$ de la
identidad-diagonal, sobre el cual ambos productos truncados distan $<\varepsilon/4$ de
$\zeta_X(s)$ (que no se anula y no necesita anularse: el objetivo es la diagonal, §2.1,
Módulo 5); su medida Haar es $\delta_*(\varepsilon):=\prod_{p\le X}(\rho/\pi)^2>0$, sin
$d$. ∎(esquema)

**GAP TÉCNICO declarado (G4.1):** los pasos (1) y (2) — efectivizar la aproximación en
media cuadrática y la regularización del borde del evento con constantes explícitas —
son estándar pero largos y no están escritos en la literatura para el par
$(\tau,d\tau)$; la afirmación nueva y completamente probada aquí es la **estructura de
la dependencia en $d$**: $d$ entra SOLO por (i) el reescalado $|d|T\ge T_1$ y (ii) las
frecuencias de la Prop. 3.1, ambas lineales en $1/|d|$. Ninguna constante de (1)–(2) ni
la positividad (4) depende de $d$. La cota (a) como teorema completamente formal queda
condicionada a G4.1; la calificamos de rutinaria, no de abierta en sentido fuerte.

### 4.2 Respuesta directa a la pregunta (ii)

- **$\delta(d,\varepsilon)\to0$ cuando $d\to0$? NO.** Es uniformemente positiva en
  $0<|d|<d_0(\varepsilon)$ (Teorema 4.1(a)). La intuición del Problema 8.1 (la densidad
  se hunde con $d$) es falsa: la medida límite ni siquiera cambia con $d$ en ese rango.
- **Primer $\tau$ garantizado:** $\tau(d,\varepsilon)\le C(\varepsilon)/|d|$, y este
  orden es óptimo (§4.3). **Degradación lineal en $1/|d|$** — el extremo más benigno de
  la rama "polinomial" de la dicotomía.
- La no-uniformidad del límite doble queda cuantificada:
  $\lim_{d\to0}\lim_{T\to\infty}$ (= $\delta_*>0$) $\neq$
  $\lim_{T\to\infty}\lim_{d\to0}$ (= densidad de $\mathrm{SR}_0$, RH). El intercambio
  falla exactamente porque el rango útil de $T$ empieza en $C(\varepsilon)/|d|\to\infty$.

### 4.3 Cota inferior para la escala: la linealidad es exacta

**Proposición 4.3 (bajo $\neg$RH, anclando $K$ en el cero, la escala $1/|d|$ es
genuina).** *Supongamos que $\zeta$ tiene un cero $\rho_0=\beta_0+i\gamma_0$ con
$\beta_0>1/2$, $\gamma_0>0$. Sea $\eta>0$ con $\overline B(\rho_0,4\eta)\subset
D(1/2,1)$, $\zeta$ sin otros ceros en $\overline B(\rho_0,4\eta)$, y
$K=\overline B(\rho_0,3\eta)$, $\varepsilon\le\frac14\min_{2\eta\le|w-\rho_0|\le4\eta}|\zeta(w)|$.
Entonces existe $\eta_1>0$ tal que para todo $d\neq0$ y todo $T\le\eta_1/|d|$:*
$$\frac1T\,\mathrm{meas}\big\{\tau\in[0,T]:\sup_K|\zeta(s+i\tau)-\zeta(s+id\tau)|<\varepsilon\big\}
\ \le\ \frac{C_K\,N(\beta_0-3\eta,\,T+\gamma_0+3\eta)}{T}\ =\ o(1)\quad(T\to\infty).$$

*Prueba.* Para $T\le\eta_1/|d|$ y $\tau\in[0,T]$: $|d\tau|\le\eta_1$. Por continuidad
uniforme de $\zeta$ en un entorno compacto de $K$, elegí $\eta_1$ con
$\sup_K|\zeta(s+id\tau)-\zeta(s)|<\varepsilon$ para $|d\tau|\le\eta_1$. Entonces el
evento implica $\sup_K|\zeta(s+i\tau)-\zeta(s)|<2\varepsilon$; como el círculo
$|w-\rho_0|=3\eta$ está contenido en el anillo $2\eta\le|w-\rho_0|\le4\eta$, la elección
de $\varepsilon$ da $2\varepsilon\le\frac12\min_{\partial K}|\zeta|<\min_{\partial K}|\zeta|$,
y por Rouché $\zeta(\cdot+i\tau)$ tiene un cero en
$B(\rho_0,3\eta)$, es decir $\zeta$ tiene un cero con parte real $>\beta_0-3\eta>1/2$ y
altura en $[\tau+\gamma_0-3\eta,\tau+\gamma_0+3\eta]$. Cada cero absorbe $\tau$-medida
$\le6\eta$; el conteo da medida $\le6\eta\,N(\beta_0-3\eta,T+\gamma_0+3\eta)=o(T)$ por
Carlson (Doc 102, Teorema 2.3). ∎

Es decir: con $K$ anclado en el cero hipotético, **por debajo de la escala $\eta_1/|d|$
la densidad es $o(1)$** (el evento colapsa a $\mathrm{SR}_0$ local, prohibido), y por
encima de $C(\varepsilon)/|d|$ es $\ge\delta_*/2$ (Teorema 4.1 — con $K$ y $\varepsilon$
admisibles; notar que el Teorema 4.1 no exige nada sobre ceros). La transición es real y
ocurre en $T\asymp1/|d|$: **la degeneración cuantitativa de $\mathrm{SR}_d$ en $d\to0$
es exactamente lineal en $1/|d|$, ni exponencial ni mejor que lineal.**

---

## 5. El acoplamiento con Rouché: el gap cuantitativo (pregunta iii)

### 5.1 Por qué $(\mathrm{SR}_d)$ global no alimenta el amplificador

El amplificador de Bagchi (Doc 102, §4.2, activo A1) necesita un **ancla**: un disco
fijo alrededor del cero hipotético $\rho_0$ y comparaciones de $\zeta(\cdot+i\tau)$ con
una función que **tenga un cero en ese disco con módulo controlado en el borde**. En
$(\mathrm{SR}_d)$ ambas copias escapan: $\tau\to\infty$ y $d\tau\to\infty$. La copia
lenta solo está cerca del ancla cuando $d\tau\in[\gamma_0-\eta,\gamma_0+\eta]$, i.e.

$$\tau\in J_d:=\Big[\frac{\gamma_0-\eta}{d},\ \frac{\gamma_0+\eta}{d}\Big],
\qquad \mathrm{meas}(J_d)=\frac{2\eta}{d}\quad(d>0\ \text{WLOG}).$$

**Lema 5.1.** La fracción de $[0,T]$ útil para anclar es
$\mathrm{meas}(J_d)/T=2\eta/(dT)\to0$ para $d$ fijo. La densidad positiva global de
$(\mathrm{SR}_d)$ — por grande y uniforme que sea — **no dice nada** sobre la medida del
evento dentro de $J_d$: un liminf sobre $[0,T]$ es compatible con medida cero en
cualquier sub-ventana de densidad nula. ∎

Por eso ni siquiera la versión más fuerte concebible del Teorema 4.1 (constantes
perfectas, $\delta_*$ enorme, $T_0=1/|d|$ exacto) produce tensión: Rouché no consume la
cantidad que el teorema entrega. La pregunta correcta es: ¿qué densidad **dentro de
$J_d$** haría funcionar el argumento?

### 5.2 La suficiencia: el umbral $|d|^{\kappa}$

Notación: para $\sigma\in(1/2,1)$ sea $\kappa(\sigma)>0$ un exponente admisible de
densidad de ceros, i.e. $N(\sigma,T)\ll_\sigma T^{1-\kappa(\sigma)}$. Valores
incondicionales: Carlson (1920) da $\kappa(\sigma)=(2\sigma-1)^2-\epsilon$ (de
$N\ll T^{4\sigma(1-\sigma)+\epsilon}$); Ingham (1940),
$N\ll T^{3(1-\sigma)/(2-\sigma)}\log^5T$, da
$\kappa(\sigma)=\frac{2\sigma-1}{2-\sigma}-\epsilon$.

**Teorema 5.2 (densidad anclada suficiente para RH).** *Supongamos $\neg$RH, con cero
$\rho_0=\beta_0+i\gamma_0$, $\beta_0>1/2$, $\gamma_0>0$. Sean $\eta,K,\varepsilon$ como
en la Proposición 4.3 con además $\eta<(\beta_0-\tfrac12)/4$, y
$\sigma:=\beta_0-3\eta>\tfrac12$. Si existieran $c>0$, $\kappa'<\kappa(\sigma)$ y una
sucesión $d_k\downarrow0$ tales que*
$$\mathrm{meas}\Big\{\tau\in J_{d_k}:\ \sup_{s\in K-i\gamma_0+id_k\tau\ \text{(ver prueba)}}
|\zeta(s+i\tau)-\zeta(s+id_k\tau)|<\varepsilon\Big\}\ \ge\ c\,d_k^{\,\kappa'}\cdot\mathrm{meas}(J_{d_k}),$$
*entonces contradicción con $N(\sigma,T)\ll T^{1-\kappa(\sigma)}$. En consecuencia, una
tal cota — uniforme sobre una sucesión $d\to0$, demostrada incondicionalmente —
implicaría RH.*

*Prueba.* Fijamos $k$, escribimos $d=d_k$, y tomamos el compacto fijo
$K_0=\overline B(\beta_0+i0,3\eta)$ trasladado: para $\tau\in J_d$ pongo
$t:=d\tau\in[\gamma_0-\eta,\gamma_0+\eta]$. La función $w\mapsto\zeta(w)$ tiene su cero
$\rho_0$ a distancia $\le\eta$ del centro $\beta_0+it$ del disco
$B(\beta_0+it,3\eta)$, y su borde cae en el anillo $2\eta\le|w-\rho_0|\le4\eta$, donde
$|\zeta|\ge4\varepsilon$. (Formalmente: el sup en el enunciado es sobre
$s\in\overline B(\beta_0,3\eta)$ evaluando $\zeta(s+id\tau)$ y $\zeta(s+i\tau)$ — un
compacto fijo, el enunciado es legítimo como instancia de auto-aproximación localizada.)
Para cada $\tau$ bueno, sobre $|s-\beta_0|=3\eta$:
$|\zeta(s+i\tau)-\zeta(s+it)|<\varepsilon<|\zeta(s+it)|$, y Rouché da a
$\zeta(\cdot+i\tau)$ al menos un cero en $B(\beta_0,3\eta)$: un cero de $\zeta$ con
parte real $\ge\sigma$ y altura en $[\tau-3\eta,\tau+3\eta]$. La medida buena es
$\ge c\,d^{\kappa'}\cdot\frac{2\eta}{d}$ y cada cero absorbe medida $\le6\eta$:
$$\#\{\text{ceros}\}\ \ge\ \frac{c}{3}\,d^{\,\kappa'-1},\qquad\text{alturas}\ \le\
T':=\frac{\gamma_0+\eta}{d}+3\eta\ \le\ \frac{2\gamma_0}{d}\ \ (d\ \text{chico}).$$
Luego $N(\sigma,T')\ge\frac{c}{3}d^{\kappa'-1}\ge c'\,(T')^{1-\kappa'}$. Pero
$N(\sigma,T')\ll(T')^{1-\kappa(\sigma)}$ y $\kappa'<\kappa(\sigma)$: contradicción para
$k$ grande. ∎

### 5.3 El techo: bajo $\neg$RH la densidad anclada verdadera tiene el MISMO exponente

**Teorema 5.3 (techo incondicional-en-la-ventana).** *Bajo $\neg$RH y con la
configuración del Teorema 5.2, para todo $d>0$ suficientemente chico la densidad anclada
VERDADERA satisface*
$$\frac{1}{\mathrm{meas}(J_d)}\,\mathrm{meas}\Big\{\tau\in J_d:\ \sup_{|s-\beta_0|\le3\eta}
|\zeta(s+i\tau)-\zeta(s+id\tau)|<\varepsilon\Big\}\ \le\ \frac{6\eta\,N(\sigma,2\gamma_0/d)}{2\eta/d}
\ \ll\ d^{\,\kappa(\sigma)}.$$

*Prueba.* El mismo transporte de Rouché de la prueba anterior (que solo usa la cota
inferior de $|\zeta|$ en el anillo, disponible por la elección de $\eta,\varepsilon$):
cada $\tau$ bueno de $J_d$ produce un cero de $\zeta$ con $\mathrm{Re}\ge\sigma$ y
altura $\le2\gamma_0/d$; cada cero absorbe medida $\le6\eta$; aplicar
$N(\sigma,T)\ll T^{1-\kappa(\sigma)}$ con $T=2\gamma_0/d$. ∎

**Corolario 5.4 (el gap cuantitativo, enunciado preciso — esto ES MW-2 cuantificado).**
Definí, para la configuración anclada $(\rho_0,\eta,K,\varepsilon)$:

- $\delta^{\mathrm{anc}}_{\mathrm{nec}}(d)$ := la mínima densidad anclada que produce la
  contradicción del Teorema 5.2: $\delta^{\mathrm{anc}}_{\mathrm{nec}}(d)=d^{\,\kappa(\sigma)-\epsilon}$
  (cualquier $\epsilon>0$, a lo largo de una sucesión $d\to0$);
- $\delta^{\mathrm{anc}}_{\mathrm{ver}}(d)$ := la densidad anclada verdadera bajo
  $\neg$RH: $\delta^{\mathrm{anc}}_{\mathrm{ver}}(d)\ll d^{\,\kappa(\sigma)}$ (Teorema 5.3);
- $\delta^{\mathrm{anc}}_{\mathrm{dem}}(d)$ := la densidad anclada que la maquinaria
  incondicional demuestra: $\delta^{\mathrm{anc}}_{\mathrm{dem}}(d)=0$ (§5.5).

Entonces:
$$\delta^{\mathrm{anc}}_{\mathrm{dem}}\ =\ 0\ \ \ll\ \ \delta^{\mathrm{anc}}_{\mathrm{ver}}\ \ll\ d^{\kappa}
\ \ \approx\ \ \delta^{\mathrm{anc}}_{\mathrm{nec}}=d^{\kappa-\epsilon}.$$

Dos lecturas, ambas exactas:

1. **Auto-bloqueo de exponentes.** Lo necesario ($d^{\kappa-\epsilon}$) y lo máximo
   posible bajo $\neg$RH ($d^{\kappa}$) difieren solo en $\epsilon$: el mismo teorema de
   densidad de ceros que da la contradicción en el Teorema 5.2 acota el insumo en el
   Teorema 5.3. **Cualquier mejora del teorema de densidad** (Ingham→density
   hypothesis→lo que sea: $\kappa$ más grande) **mueve ambos lados simultáneamente**: el
   umbral baja y el techo baja con él. El mecanismo no puede ganarse a sí mismo por
   mejora de $\kappa$. Esto explica estructuralmente por qué ningún refinamiento de
   Carlson/Ingham ha convertido nunca la auto-aproximación en un ataque: el amplificador
   y su insumo son duales respecto del mismo $N(\sigma,T)$.
2. **El gap real es binario.** La distancia operativa no es entre $d^{\kappa-\epsilon}$
   y $d^{\kappa}$ (eso sería "solo constantes"): es entre lo demostrable ($0$ exacto) y
   lo necesario ($>0$). Ver §5.5.

### 5.4 Por qué lo demostrable en la ventana anclada es exactamente cero

Dentro de $J_d$, la copia lenta recorre $d\tau\in[\gamma_0-\eta,\gamma_0+\eta]$: una
ventana de alturas de longitud $2\eta=O(1)$. A escala de su propia equidistribución
(frecuencias $\asymp d\cdot\log p$, períodos $\asymp1/d$), la copia lenta está
**congelada**: en toda la ventana, $\zeta(s+id\tau)=\zeta(s+i\gamma_0)+O(\eta)$
uniformemente en $K$. El enunciado "densidad anclada positiva" es entonces, módulo
$O(\eta)$:

$$\mathrm{meas}\big\{\tau\in J_d:\ \sup_K|\zeta(s+i\tau)-g(s)|<\varepsilon'\big\}\ \ge\ c\cdot\mathrm{meas}(J_d),
\qquad g:=\zeta(\cdot+i\gamma_0),$$

es decir: **universalidad con objetivo fijo $g$ en el intervalo (corto relativo a su
altura) $J_d$ — donde $g$ tiene un cero en $K$.** Este es el objetivo prohibido del
Módulo 5 (Doc 102, §3): por el teorema de soporte + Hurwitz, la densidad límite
demostrable por la maquinaria de Bagchi para objetivos con ceros es **exactamente
$0$** — no "pequeña", no "mal acotada": el objetivo está fuera del soporte de la medida
límite, y la maquinaria da masa cero a todas sus vecindades chicas. (Y el Corolario 2 de
Matsumoto — el propio amplificador — prohíbe que ninguna otra maquinaria dé densidad
positiva sobre $[0,T]$ completo; sobre ventanas cortas no está prohibido que sea
VERDADERO bajo $\neg$RH — Teorema 5.3 permite hasta $d^\kappa$ — pero sí está fuera de
todo método conocido, y probarlo incondicionalmente con exponente $<\kappa$ sería,
por el Teorema 5.2, probar RH.)

La degeneración $d\to0$ de $(\mathrm{SR}_d)$ queda así identificada con precisión:

> **Cuando $d\to0$, las pruebas de $(\mathrm{SR}_d)$ no pierden densidad ni ganan
> constantes malas: pierden el ÚNICO trozo de $\tau$-espacio que el amplificador puede
> consumir.** La información incondicional vive en $\tau\gg C(\varepsilon)/|d|$ (dos
> copias genéricas una respecto de la otra); el ancla vive en $\tau\asymp\gamma_0/|d|$
> (copia lenta congelada = objetivo aritmético fijo con cero). El cociente entre la
> escala entregada y la escala útil es $\ge C(\varepsilon)/\gamma_0\cdot$ (constante),
> $>1$ siempre — y dentro de la escala útil el problema es indistinguible de
> $\mathrm{SR}_0$ local. MW-2 en versión cuantitativa: **la genericidad relativa se
> prueba; la genericidad respecto del punto aritmético congelado es RH** (Doc 102,
> Prop. 7.2, ahora con tasas).

### 5.5 La cascada: el único esquema que esquivaría el ancla, y por qué no arranca

Para exhaustividad (regla del programa: cerrar también las variantes). Una alternativa
al ancla fija: **bootstrapping entre generaciones de ceros.** Bajo $\neg$RH, el cero
$\rho_0$ produce (si hubiera densidad anclada $c$ en $J_d$) $\asymp c\,\eta/(d\,\eta)$
ceros a alturas $\asymp\gamma_0/d$; cada uno de esos serviría de ancla para una ventana
en $\tau\asymp\gamma_0/d^2$, etc. El conteo en la generación $k$:
$N_k\asymp(c/d)^k$ ceros a alturas $T_k\asymp\gamma_0/d^k$, es decir
$$N_k\ \asymp\ T_k^{\,1-\frac{\log(1/c)}{\log(1/d)}}\ =\ T_k^{\,1-o(1)}\quad(d\to0),$$
que aplastaría cualquier $N(\sigma,T)\ll T^{1-\kappa}$. La cascada es aritméticamente
viable — PERO cada generación consume exactamente el mismo insumo prohibido: densidad de
aproximación a un objetivo congelado **con cero** ($\zeta(\cdot+it_1)$, $t_1$ = altura de
un cero de la generación anterior) en una ventana corta. El esquema multiplica el
beneficio del insumo, no lo debilita: la primera generación ya requiere el lema que no
existe. Ninguna versión de la cascada reduce el requisito por debajo de
"objetivo-prohibido en intervalo corto". ∎

**El lema faltante, nombrado (para el mapa del programa):**

> **(LF-104) Universalidad localizada con objetivo prohibido.** Existe
> $\theta\in(0,1)$ tal que: para algún compacto $K$ y $g\in H^c(K)$ CON cero en $K$,
> y para todo $T$ grande, $\mathrm{meas}\{\tau\in[T,T+T^{1-\theta'}]:\sup_K|\zeta(s+i\tau)-g(s)|<\varepsilon\}
> \ge c\,T^{1-\theta'-\theta}$ con $\theta<\kappa(\sigma_K)$, para ventanas posicionadas
> en alturas prescritas.

Por el Teorema 5.2, (LF-104) con $g=\zeta(\cdot+i\gamma_0)$ implica RH; por el Teorema
5.3 su versión genérica está acotada por el mismo exponente; por el Módulo 5 está fuera
del alcance de toda la maquinaria de universalidad. Es la forma "intervalos cortos" del
teorema decisivo I2b cuyo nombre dio Doc 102 §8 — coincide en sustancia con la dirección
que la literatura reciente explora (auto-aproximación en intervalos cortos, Garunkštis
et al. 2025, donde la versión $d=0$ corta es de nuevo RH-equivalente [NO VERIFICADO en
detalle]).

---

## 6. $d=d(T)$ móvil (pregunta iv)

¿Puede una velocidad dependiente de la altura, $d(T)\to0$, recombinar "información a
escala $T$" con "ancla a escala $1/d$"? No, y la razón es una disyunción exhaustiva.

**Lema 6.1 (complementariedad ancla/equidistribución).** *Sea $d(T)\to0$ cualquier
función. Considerá el enunciado $(\mathrm{SR}_{d(T)})$: densidad positiva (o cota
$\rho(T)$) de $\tau\in[0,T]$ con
$\sup_K|\zeta(s+i\tau)-\zeta(s+id(T)\tau)|<\varepsilon$. Hay exactamente dos regímenes:*

*(a) $d(T)\,T\to\infty$ (la copia lenta escapa). Entonces ningún $\tau\le T$ tiene la
copia lenta anclada salvo los de la ventana $J_{d(T)}\cap[0,T]$, de medida
$\le2\eta/d(T)=o(T)$; el número de ceros off-críticos que TODO el evento (anclado o no)
puede certificar vía Rouché a partir del único cero conocido $\rho_0$ es
$\le\frac{2\eta}{6\eta\,d(T)}\cdot(1+o(1))=o(T)$ — sin contradicción con
$N(\sigma,T)=o(T)$, por definición de $o$. Para los $\tau$ fuera de la ventana, el
evento compara dos copias en alturas $\to\infty$ sobre las que no se conoce ningún cero:
cero transferencia.*

*(b) $d(T)\,T=O(1)$ (la copia lenta queda en una ventana acotada $[0,\Lambda]$ de
alturas para todo $\tau\le T$). Entonces $\zeta(s+id(T)\tau)$ recorre el compacto
$\{\zeta(s+iu):u\in[0,\Lambda]\}$: el enunciado es la aproximación de una FAMILIA
COMPACTA FIJA de objetivos aritméticos. Si la familia evita ceros en $K$ (i.e. si
$\zeta\neq0$ en $K+i[0,\Lambda]$ — bajo $\neg$RH falso para $K$ anclado y
$\Lambda\ge\gamma_0$), es universalidad clásica; si contiene el cero, es el objetivo
prohibido: densidad demostrable $0$ (§5.4), y por Carlson la verdadera es $o(1)$
(Proposición 4.3). En ambos casos el contenido es el de $\mathrm{SR}_0$:
no se ganó nada respecto de $d=0$.*

*No hay tercer régimen, y los casos intermedios por sucesiones se reparten entre (a) y
(b) por sub-sucesiones. ∎*

**Ejemplos pedidos.** $d(T)=1/\log T$: régimen (a) — la ventana útil tiene medida
$2\eta\log T=o(T)$; produce a lo sumo $O(\log T)$ ceros: nada. $d(T)=T^{-\theta}$,
$0<\theta<1$: régimen (a); la ventana útil tiene medida $2\eta T^{\theta}$; si la
densidad anclada fuera uniformemente positiva ahí, saldrían $\asymp T^\theta$ ceros
hasta altura $T$, que contradice Ingham en cuanto
$\theta>\frac{3(1-\sigma)}{2-\sigma}$ — un margen real para $\beta_0$ no demasiado cerca
de $1/2$ (e.g. $\beta_0=0.9$: basta $\theta>0.28$). **Pero** la densidad anclada
demostrable es $0$ (§5.4) y la verdadera bajo $\neg$RH está capada por el mismo
exponente (Teorema 5.3 reescalado): el margen es ilusorio — es otra reparametrización
del Corolario 5.4, con $d\leftrightarrow T^{-\theta}$. $d(T)=\gamma_0/T$: régimen (b)
exacto — el enunciado se vuelve literalmente "$\zeta(\cdot+i\tau)$ aproxima
$\zeta(\cdot+iu)$, $u\in[0,\gamma_0]$, con densidad positiva en $[0,T]$", que para la
sub-ventana $u\approx\gamma_0$ es $\mathrm{SR}_0$ anclado: RH-equivalente, densidad
demostrable $0$.

**Punto de ruptura exacto:** el ancla exige que el rango de alturas de la copia lenta
sea $O(1)$ (si no, no contiene establemente al cero $\rho_0$ con control de módulo en el
borde); la equidistribución de la copia lenta — el único insumo que las pruebas
incondicionales saben usar — exige que ese rango tienda a $\infty$ (es la condición
$|d|T\ge T_1(\varepsilon)$ del Teorema 4.1, paso (1), y la condición de Weyl del paso
(3)). Son la negación una de la otra. Ninguna $d(T)$ puede satisfacer ambas; el
parámetro móvil solo redistribuye los $\tau$ entre los dos regímenes estériles.

---

## 7. Síntesis: respuesta al Problema 8.1 y posición en el programa

### 7.1 Tabla-resumen de la degeneración

| Cantidad | Comportamiento en $d\to0$ | Resultado |
|---|---|---|
| Densidad global $\delta(d,\varepsilon)$ | $\ge\delta_*(\varepsilon)>0$ uniforme en $0<|d|<d_0(\varepsilon)$ | Teorema 4.1(a) — NO degenera |
| Escala/primer $\tau$: $T_0(d,\varepsilon)$ | $\asymp C(\varepsilon)/|d|$ — lineal exacto | Teorema 4.1(b) + Proposición 4.3 |
| Input diofántico (Baker/6exp) | irrelevante para $|d|<d_0(\varepsilon)$; en $|d|\ge d_0$: polinomial $|d|^{C(\varepsilon)}$ (racional/algebraico), inefectivo (trascendente) | Prop. 3.1, §3.3 |
| Densidad anclada demostrable | $0$ exacto (objetivo prohibido, Hurwitz) | §5.4 |
| Densidad anclada verdadera bajo $\neg$RH | $\ll|d|^{\kappa(\sigma)}$ | Teorema 5.3 |
| Densidad anclada suficiente para RH | $\ge|d|^{\kappa(\sigma)-\epsilon}$ en una sucesión | Teorema 5.2 |
| $d(T)$ móvil | dos regímenes estériles exhaustivos | Lema 6.1 |

### 7.2 La dicotomía de 8.1, corregida

- La rama "$e^{-c/|d|}$ ⟹ MW-2 cuantificado y cierre" tenía la conclusión correcta con
  la premisa falsa: no hay degradación exponencial en ninguna parte (ni siquiera la
  diofántica lo es: §3.3).
- La rama "polinomial ⟹ tensión genuina con Rouché" tenía la premisa correcta (la
  degradación es polinomial, de hecho lineal, y la densidad ni degenera) con la
  conclusión falsa: no hay tensión, porque Rouché no consume la cantidad global sino la
  anclada, y ahí el muro es **binario** ($0$ demostrable vs $>0$ necesario), no
  cuantitativo. El test de la dicotomía estaba apuntado a la constante equivocada.
- MW-2 cuantificado no es una tasa de degeneración: es el **Corolario 5.4** — la
  identidad de exponentes $\kappa(\sigma)$ entre lo necesario y lo máximo-verdadero
  (auto-bloqueo del amplificador respecto de su propio teorema de densidad), montada
  sobre el cero exacto de lo demostrable (Hurwitz). La versión con tasas de la Prop. 7.2
  del Doc 102.

### 7.3 Activos nuevos para el programa

- **(A1') Refinamiento del activo A1 (Doc 102):** el amplificador Rouché-densidad es
  auto-bloqueante frente a insumos de tipo auto-aproximación: cualquier insumo
  formulable como "densidad de aproximación a un objetivo congelado con cero" tiene
  techo $|d|^{\kappa}$ bajo $\neg$RH con el mismo $\kappa$ que el umbral de
  contradicción (Teoremas 5.2–5.3). Para que A1 dispare alguna vez, su insumo deberá
  venir de una fuente NO mayorizable por $N(\sigma,T)$ — criterio de filtrado nuevo
  para futuras propuestas de recurrencia.
- **(A2') El régimen libre de diofantina (Prop. 3.1):** cerca del punto RH-equivalente
  $d=0$, la familia $\mathrm{SR}_d$ no es un problema de teoría trascendente sino de
  kinemática pura ($T\asymp1/|d|$). Las constantes de Baker, que el corpus citaba como
  el costo de la familia, no son el costo marginal en la frontera.
- **(LF-104)** como el enunciado exacto de lo que falta, en forma de intervalos cortos
  (§5.5), conectado con la literatura 2025.

---

## 8. Gaps declarados

- **G4.1 (rutinario):** la efectivización completa de los pasos (1)–(2) del Teorema 4.1
  (media cuadrática efectiva del par y regularización del borde del evento) no está
  escrita ni aquí ni en la literatura; la estructura de dependencia en $d$ (todo el
  contenido del teorema que este doc usa) está probada. Ninguna conclusión de §§5–7
  depende de G4.1: los Teoremas 5.2, 5.3, la Prop. 4.3 y el Lema 6.1 son
  incondicionales y completos tal como están enunciados.
- La resolución del caso racional $|a-b|=1$ por Pańkowski (todo $d\neq0,\pm1$ racional)
  está citada de fuentes secundarias [NO VERIFICADO en texto completo]; es irrelevante
  para $d\to0$ por la Observación 1.1.
- El paper de intervalos cortos (Symmetry 17 (2025), art. 2075) verificado solo a nivel
  de enunciado/abstract [NO VERIFICADO en detalle].
- La constante de Baker–Wüstholz citada en §3.3 es la forma estándar del teorema de
  1993 (J. reine angew. Math. 442); usada solo ilustrativamente en el régimen
  $|d|\ge d_0(\varepsilon)$, fuera del camino crítico del documento.

---

## 9. VEREDICTO

**RUTA CERRADA.**

**Razón precisa:** la pregunta de Forma C queda respondida en sentido más fuerte que su
propia dicotomía. La degeneración de $(\mathrm{SR}_d)$ en $d\to0$ es **polinomial — de
hecho exactamente lineal: $T_0(d,\varepsilon)\asymp C(\varepsilon)/|d|$ — y la densidad
$\delta(d,\varepsilon)$ no degenera en absoluto** (uniformemente positiva en
$0<|d|<d_0(\varepsilon)$, con todas las clases diofánticas de $d$ colapsadas:
Proposición 3.1, Teorema 4.1). Según la dicotomía de P41 esto debía abrir una "tensión
genuina con Rouché"; no la abre, porque el argumento de Rouché no consume la densidad
global sino la densidad en la ventana anclada $J_d=\{\tau:d\tau\approx\gamma_0\}$, de
medida $\asymp1/|d|$, donde la copia lenta está congelada y el enunciado colapsa a
universalidad con objetivo prohibido ($\zeta(\cdot+i\gamma_0)$, que porta el cero):
densidad demostrable exactamente $0$ (Hurwitz/Módulo 5). El gap cuantitativo exacto es
el Corolario 5.4: lo suficiente para RH es densidad anclada $|d|^{\kappa(\sigma)-\epsilon}$
(Teorema 5.2), lo verdadero bajo $\neg$RH está capado por $|d|^{\kappa(\sigma)}$ con el
**mismo exponente** (Teorema 5.3) — el amplificador es auto-bloqueante respecto de su
propio teorema de densidad de ceros — y lo demostrable es $0$. El muro no es una tasa:
es binario, y es MW-2 con tasas alrededor. El parámetro móvil $d(T)$ no esquiva nada:
anclar y equidistribuir la copia lenta son condiciones complementarias
($|d|T=O(1)$ vs $|d|T\to\infty$) para toda función $d(T)$ (Lema 6.1).

**Lo único que reabriría la línea:** el lema (LF-104) — universalidad localizada en
intervalos cortos con objetivo prohibido y exponente mejor que $\kappa(\sigma)$ — que
por el Teorema 5.2 implica RH, por el Teorema 5.3 está en el borde exacto de lo
consistente, y por el Módulo 5 está fuera de toda la maquinaria de universalidad
existente. No es una dirección de trabajo: es la re-codificación de RH en coordenadas de
intervalos cortos, y queda registrada como tal.

---

## Referencias

**Literatura externa:**
- B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math.
  Hungar. **50** (1987), 227–240.
- K. Matsumoto, *A survey on the theory of universality for zeta and L-functions*,
  arXiv:1407.4216 (2014) — §9 para la familia $\mathrm{SR}_d$ (fórmulas (9.3)–(9.4),
  Thm. 21).
- T. Nakamura, *The generalized strong recurrence for non-zero rational parameters*,
  Arch. Math. **95** (2010), 549–555.
- T. Nakamura, Ł. Pańkowski, *Erratum/corrigendum*, Arch. Math. **99** (2012), 43–47;
  arXiv:1203.1393 (verificado: $\zeta$ para $d=a/b$, $|a-b|\neq1$; $\log\zeta$ para todo
  $d\neq0$; $d=0$ para $\log\zeta$ equivale a RH).
- Ł. Pańkowski, resolución del caso racional restante $d\neq0,\pm1$ [reportado; NO
  VERIFICADO en texto completo].
- R. Garunkštis, *Self-approximation of Dirichlet L-functions*, J. Number Theory **131**
  (2011) / arXiv:1006.1507.
- R. Garunkštis et al., *On self-approximation of the Riemann zeta function in short
  intervals*, Symmetry **17** (2025), art. 2075 [abstract verificado].
- A. Baker, *Linear forms in the logarithms of algebraic numbers I–III*, Mathematika
  13–14 (1966–67); A. Baker, G. Wüstholz, J. reine angew. Math. **442** (1993), 19–62.
- S. Lang, *Introduction to Transcendental Numbers* — teorema de los seis exponenciales.
- F. Carlson (1920); A. E. Ingham (1940) — $N(\sigma,T)\ll T^{4\sigma(1-\sigma)+\epsilon}$,
  $N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}\log^5T$.
- P. Walters, *An Introduction to Ergodic Theory*, Springer GTM 79.

**Docs internos (backward-only):**
- Doc 102 (`phase-35-five-fronts/102-bagchi-voronin-auditoria.md`) — módulos 1–5,
  amplificador A1, Prop. 7.2, familia $\mathrm{SR}_d$, veredicto FAIL I2b.
- P41 (`06-papers/P41-exhaustion-1d-propagation/main.tex`) — Problema 8.1 / Forma C.
- `COMPLETE-PROGRAM-SUMMARY.md` — MW-2, MW-7.

---

*Doc 104 · Phase 36 · junio 2026 · David Alejandro Trejo Pizzo*
