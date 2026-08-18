# 104_104 — Jets reales, discos tangentes y gate del bloque de Li

**Estado.** Este documento ataca directamente la propuesta de obtener
bloques consecutivos con \(\lambda_n\ge-1\) a partir de la generatriz real

\[
 \mathcal F(z):=\log\!\left(2\xi\!\left({1\over1-z}\right)\right)
 =\sum_{n\ge1}{\lambda_n\over n}z^n.                 \tag{1}
\]

El resultado no prueba RH. Produce tres conclusiones exactas.

1. RH equivale a una cota de crecimiento de **jets sobre el eje real** de
   \(\mathcal F\). Por tanto el eje real no pierde información.
2. La serie de Euler con los pesos ordinarios \(\Lambda(m)\) prueba esa
   cota solo en el horodisco \(|z-\tfrac12|<\tfrac12\), que corresponde a
   \(\Re s>1\). La parte que falta de los discos tangentes es exactamente
   la continuación a través de la franja crítica, no un error de una
   constante.
3. Ecuación funcional, realidad, positividad sobre \(s>1\), orden uno y
   cualquier argumento **perturbativamente estable** que inspeccione una
   cantidad finita de datos diferenciales reales no bastan: existe un factor
   explícito, arbitrariamente invisible en esos datos, que introduce un
   cuarteto fuera de la línea y excursiones negativas sindéticas. El factor
   no conserva los \(\Lambda(m)\) exactos; conservarlos es imposible por
   unicidad del logaritmo derivado.

Así se descarta una familia precisa de ataques locales. El input que aún
podría cerrar el criterio de bloques debe usar los \(\Lambda(m)\) reales de
forma global y no perturbativamente estable.

---

## 1. Auditoría de no duplicación

`104_17` prueba que la positividad Abel radial de un cuarteto es compatible
con coeficientes exponencialmente negativos. `104_62`, `104_64`, `104_69` y
`104_75` muestran que Fejér, Abel y Fermi no recuperan la media no lineal
desde una resolución radial fija. `104_56` y `104_61` prueban que basta
obtener bloques buenos de longitud no acotada.

`104_84` ya identifica el horodisco Euler, la unicidad desde valores exactos
y un factor polinómico simétrico con un cuarteto off-line. Por tanto ni el
horodisco ni el factor de la §4 se reclaman nuevos aquí. Se reutilizan para
una auditoría más estrecha: el factor se hace cuantitativamente invisible en
norma \(C^J\) y se conecta con las excursiones sindéticas del criterio de
bloques. Los ingredientes nuevos respecto de ese documento son el criterio
de radios tangentes en jets reales, la recurrencia exacta (12)--(13) con
\(\Lambda(m)\), y la localización precisa de qué centros reales ya controla
el horodisco.

Aquí no se vuelve a promediar (1). Se estudia el radio de Taylor de su
**germen en cada punto real** y se determina exactamente qué parte de ese
radio está certificada por la serie de Euler ordinaria.

---

## 2. Un criterio de RH únicamente con jets reales

Para \(0<r<1\), sea \(\mathcal F_r\) el germen de la rama real de (1) en
\(r\), y defina

\[
 \mathscr R(r)^{-1}:=
 \limsup_{k\to\infty}
 \left({|\mathcal F_r^{(k)}(r)|\over k!}\right)^{1/k}. \tag{2}
\]

Por Cauchy--Hadamard, \(\mathscr R(r)\) es el radio de convergencia de ese
germen. Las derivadas de orden positivo no dependen de sumar una constante
\(2\pi i\) a la rama del logaritmo.

**Teorema 2.1 (criterio de discos tangentes).** Son equivalentes:

1. RH;
2. para todo \(r\in(0,1)\),

   \[
    \boxed{\quad
    \limsup_{k\to\infty}
    \left({|\mathcal F_r^{(k)}(r)|\over k!}\right)^{1/k}
    \le {1\over1-r};\quad}                          \tag{3}
   \]

3. (3) vale para todos los racionales \(r\in(0,\tfrac12)\).

**Demostración.** Un cero \(\rho\) de \(\xi\) se transporta a

\[
 z_\rho=1-{1\over\rho}.                              \tag{4}
\]

Además

\[
 |z_\rho|^2-1={1-2\Re\rho\over|\rho|^2}.            \tag{5}
\]

Bajo RH todos los puntos (4) están en \(|z|=1\). Por tanto
\(\mathcal F\) es holomorfa en el disco unidad y el Taylor en \(r\) es
holomorfo al menos en \(D(r,1-r)\). Cauchy--Hadamard da (3).

Recíprocamente, si RH falla, la simetría \(\rho\mapsto1-\rho\) proporciona
un cero con \(\Re\rho>\tfrac12\), y (5) da un \(z_\rho\) dentro del disco
unidad. Para cualquier

\[
 0<r<{1-|z_\rho|^2\over2(1-\Re z_\rho)}              \tag{6}
\]

se tiene \(|z_\rho-r|<1-r\). El logaritmo posee una singularidad en
\(z_\rho\), de modo que
\(\mathscr R(r)\le|z_\rho-r|<1-r\), contradiciendo (3). Puede elegirse
un \(r\) racional menor que el miembro derecho de (6), lo que prueba
también 3 \(\Rightarrow\) 1. \(\square\)

La unión geométrica usada en la prueba es

\[
 \boxed{\quad\mathbb D=\bigcup_{0<r<1}D(r,1-r).\quad} \tag{7}
\]

En efecto,

\[
 |z-r|<1-r
 \iff
 r<{1-|z|^2\over2(1-\Re z)},                        \tag{8}
\]

y el miembro derecho es positivo para cada \(|z|<1\).

**Relación con los bloques.** `104_61` prueba

\[
 \mathrm {RH}
 \iff
 \lambda_n\ge-1\ \hbox{en bloques consecutivos de longitud no acotada}.
                                                               \tag{9}
\]

El Teorema 2.1 es otra formulación del mismo obstáculo: (9) excluye las
excursiones sindéticas de los coeficientes; (3) excluye la singularidad
interior que las genera. El teorema no convierte una cota local conocida
en esos bloques.

---

## 3. Qué entregan exactamente los pesos \(\Lambda(m)\)

Ponga

\[
 s={1\over1-z},\qquad
 \mathcal A(s)=\log(s(s-1))-{s\over2}\log\pi
                 +\log\Gamma(s/2).                 \tag{10}
\]

Para \(\Re s>1\), la identidad de Euler absolutamente convergente es

\[
 \boxed{
 \mathcal F(z)=\mathcal A(s)+
   \sum_{m\ge2}{\Lambda(m)\over\log m}\,m^{-s}.}    \tag{11}
\]

Sea \(\mathscr D=s^2\,d/ds=d/dz\). Si

\[
 P_0(s,L)=1,\qquad
 P_{k+1}(s,L)=s^2(\partial_s-L)P_k(s,L),             \tag{12}
\]

entonces, para cada \(r\in(0,1)\), \(s_r=(1-r)^{-1}\), y cada \(k\)
fijo,

\[
 \boxed{
 \mathcal F^{(k)}(r)=
 \mathscr D^k\mathcal A(s_r)+
 \sum_{m\ge2}{\Lambda(m)\over\log m}\,
 m^{-s_r}P_k(s_r,\log m).}                          \tag{13}
\]

La suma es absolutamente convergente. Ésta es una identidad con los pesos
ordinarios reales, no un modelo.

Sin embargo, su dominio natural en el plano \(z\) es

\[
 \begin{aligned}
 \Omega_E
  &:=\left\{z:\Re{1\over1-z}>1\right\}\\
  &=\boxed{\left\{z:\left|z-{1\over2}\right|<{1\over2}\right\}}.
                                                               \tag{14}
 \end{aligned}

Para \(r\ge\tfrac12\), el disco tangente requerido por (3) satisface

\[
 D(r,1-r)\subset\Omega_E,                            \tag{15}
\]

porque la distancia entre sus centros más su radio es
\((r-\tfrac12)+(1-r)=\tfrac12\). Así, (11) prueba
incondicionalmente (3) para todo \(r\ge\tfrac12\).

Para \(0<r<\tfrac12\), la serie de Euler garantiza directamente solo el
disco \(D(r,r)\subset\Omega_E\), mientras el Teorema 2.1 necesita
\(D(r,1-r)\). En términos de (2), la estimación geométrica disponible es

\[
 \mathscr R(r)^{-1}\le {1\over r},                  \tag{16}
\]

frente a la necesaria

\[
 \mathscr R(r)^{-1}\le {1\over1-r}.                 \tag{17}
\]

La cancelación del polo en \(s=1\) extiende \(\mathcal F\) a través de
\(z=0\), pero extender todos los discos (17) equivale, por el Teorema 2.1,
a RH. Estimar por separado \(\mathcal A\) y la suma de (11) destruye
precisamente esa cancelación.

### 3.1 Traducción exacta de vuelta a \(\lambda_n\)

Cuando el Taylor en \(r>0\) contiene a \(0\) en su disco de convergencia,
la traslación exacta da

\[
 \boxed{
 \lambda_n={1\over(n-1)!}
 \sum_{j\ge0}{(-r)^j\over j!}\,
 \mathcal F^{(n+j)}(r).}                            \tag{18}
\]

En efecto, el miembro derecho es
\(\mathcal F^{(n)}(0)/(n-1)!\). Para \(r\) suficientemente pequeño la
hipótesis vale incondicionalmente, porque \(\xi(1)\ne0\).

La alternancia de (18) es vinculante. Ni \(\Lambda(m)\ge0\) en (13), ni
una cota para un número finito de jets, produce un resto unilateral para
(18). Usar (18) sin controlar esa cola solo vuelve a escribir
\(\lambda_n\); no prueba los bloques (9).

---

## 4. Refinamiento cuantitativo del falsificador de `104_84`

Fije \(\tfrac12<\beta<1\), \(\gamma>0\), y defina

\[
 P_{\beta,\gamma}(s):=
 {\big((s-\beta)^2+\gamma^2\big)
  \big((s-(1-\beta))^2+\gamma^2\big)
  \over
  (\beta^2+\gamma^2)((1-\beta)^2+\gamma^2)}.        \tag{19}
\]

Este factor satisface exactamente

\[
 \begin{gathered}
 P_{\beta,\gamma}(1-s)=P_{\beta,\gamma}(s),\qquad
 P_{\beta,\gamma}(\bar s)=\overline{P_{\beta,\gamma}(s)},\\
 P_{\beta,\gamma}(0)=P_{\beta,\gamma}(1)=1,qquad
 P_{\beta,\gamma}(s)>0\quad(s\in\mathbb R),        \tag{20}
 \end{gathered}

y posee los cuatro ceros

\[
 \beta\pm i\gamma,qquad1-\beta\pm i\gamma.        \tag{21}
\]

Por tanto

\[
 \widetilde\xi_{\beta,\gamma}(s)
 :=\xi(s)P_{\beta,\gamma}(s)                       \tag{22}
\]

conserva la ecuación funcional, la realidad, la positividad en el eje real,
la normalización en \(0,1\) y el orden uno de \(\xi\), pero viola RH.

**Teorema 4.1 (invisibilidad de jets finitos).** Para todo compacto
\(K\subset\mathbb R\), todo \(J\ge0\) y todo \(\varepsilon>0\), puede
elegirse \(\gamma\) de modo que

\[
 \max_{0\le j\le J}\sup_{s\in K}
 \left|{d^j\over ds^j}\log P_{\beta,\gamma}(s)\right|
 <\varepsilon.                                      \tag{23}
\]

**Demostración.** En un compacto fijo,

\[
 \log\big((s-a)^2+\gamma^2\big)
 =2\log\gamma+\log\left(1+{(s-a)^2\over\gamma^2}\right).
                                                               \tag{24}
\]

Después de cancelar las constantes de normalización en (19), (24) y cada
una de sus primeras \(J\) derivadas son \(O_{K,J}(\gamma^{-2})\). \(\square\)

No se trata solo de añadir ceros abstractos. Ponga, para cada cero \(\eta\)
de (19),

\[
 u_\eta={\eta\over\eta-1}.
\]

Si \(u_{\beta+i\gamma}=Re^{i\theta}\), entonces \(R>1\) y el aporte del
factor (19) a los coeficientes de Li es

\[
 \boxed{
 Q_n=4-2(R^n+R^{-n})\cos(n\theta).}                 \tag{25}
\]

Los retornos de \(n\theta\) a un entorno de \(0\) son sindéticos
(periódicos si \(\theta/2\pi\in\mathbb Q\), y sindéticos por minimalidad
de la rotación en caso contrario). En esos retornos, \(Q_n\) es negativo
y exponencial. En particular, las simetrías y todos los datos locales
listados en (20), incluso perturbados menos que cualquier \(\varepsilon\)
finito en (23), son compatibles con la obstrucción exacta que impide los
bloques de `104_61`.

La secuencia total de (22) también tiene excursiones negativas sindéticas:
si la \(\xi\) original ya posee un modo exterior, se aplica el teorema de
modos dominantes de `104_56`; si no lo posee, (25) domina su parte
subexponencial. No se está atribuyendo esa propiedad a la \(\xi\) original,
sino a la completación perturbada (22).

Un testigo racional es \(u=2i\), equivalente a
\(\rho=u/(u-1)=(4-2i)/5\). Entonces

\[
 Q_n=4-2(2^n+2^{-n})\cos{\pi n\over2},              \tag{26}
\]

y \(Q_{4k}<0\) para todo \(k\ge1\): todo bloque de cuatro índices contiene
una excursión negativa.

### 4.1 Interpolación exacta de cualquier familia finita de jets

La cercanía de (23) puede reforzarse a igualdad exacta si solo se retienen
los axiomas cualitativos del eje real. Sean

\[
 \mathcal S=\{s_1,\ldots,s_J\}\subset(1,\infty),
 \qquad K_1,\ldots,K_J\ge0.                          \tag{27}
\]

Ponga \(a_j=s_j-\tfrac12\), elija \(M_0\ge2\) y enteros \(M_j\) con
\(2M_j>K_j\), y defina

\[
 \begin{aligned}
 \mathcal R(s)
  &:=[s(s-1)]^{2M_0}
    \prod_{j=1}^J
    \left((s-\tfrac12)^2-a_j^2\right)^{2M_j},\\
 \mathcal Q_c(s)&:=1+c\mathcal R(s),\qquad c>0.      \tag{28}
 \end{aligned}
\]

**Teorema 4.2 (falsificador de jets finitos exactos).** El factor (28)
satisface

\[
 \begin{gathered}
 \mathcal Q_c(1-s)=\mathcal Q_c(s),\qquad
 \mathcal Q_c(\bar s)=\overline{\mathcal Q_c(s)},\\
 \mathcal Q_c(s)\ge1\quad(s\in\mathbb R),\qquad
 \mathcal Q_c(\tfrac12+iy)>1\quad(y\in\mathbb R),  \tag{29}\\
 {d^k\over ds^k}\log\mathcal Q_c(s_j)=0
 \quad(0\le k\le K_j),                              \tag{30}\\
 \mathcal Q_c(0)=\mathcal Q_c(1)=1.
 \end{gathered}
\]

Para \(c\) suficientemente grande, \(\mathcal Q_c\) tiene un cero
\(\rho_c\) con

\[
 {1\over2}<\Re\rho_c<1,
 \qquad \Im\rho_c\ne0.                              \tag{31}
\]

En consecuencia,
\(\xi(s)\mathcal Q_c(s)\) coincide **exactamente** con \(\xi(s)\) en los
jets logarítmicos prescritos por (27), conserva ecuación funcional,
realidad, positividad real, normalización y orden uno, pero tiene ceros
fuera de la línea.

**Demostración.** Escribiendo \(t=s-\tfrac12\), cada factor de
\(\mathcal R\) es una potencia par de \(t^2-a^2\). Esto prueba la simetría
y \(\mathcal R(s)\ge0\) sobre el eje real. En la línea crítica,
\(t=iy\), todos los \(t^2-a^2\) son reales negativos y sus potencias pares
son positivas; de ahí (29). En \(s_j\), \(\mathcal R\) tiene un cero de
orden al menos \(2M_j\). Como
\(\log(1+c\mathcal R)=c\mathcal R+O(\mathcal R^2)\), sigue (30). El factor
\([s(s-1)]^{2M_0}\) prueba la normalización.

Cerca de \(s=1\), escriba
\(\mathcal R(s)=(s-1)^{2M_0}C(s)\), con \(C(1)>0\). Las raíces de
\(1+c\mathcal R(s)=0\) poseen las expansiones

\[
 s=1+c^{-1/(2M_0)}C(1)^{-1/(2M_0)}
 e^{(2\ell+1)\pi i/(2M_0)}
 +o\!\left(c^{-1/(2M_0)}\right).                    \tag{32}
\]

Elija una fase con coseno negativo y seno no nulo. Para \(c\) grande, la
raíz correspondiente satisface (31). La expansión (32) se obtiene por
Rouché después de la escala
\(s-1=c^{-1/(2M_0)}w\). \(\square\)

La composición \(s=(1-z)^{-1}\) no altera (30): por la regla de la cadena,
los jets en \(z_j=1-1/s_j\) también coinciden hasta orden \(K_j\).

Hay una salvedad esencial. Aunque (28) no tiene ceros sobre el eje real ni
la línea crítica, puede tener otros ceros con \(\Re s>1\). Por tanto el
Teorema 4.2 falsifica deducciones desde **finitos jets reales más axiomas
cualitativos**, pero no una deducción que use la identidad Euler completa en
todo \(\Re s>1\). El factor (19) sí mantiene sus ceros dentro de la franja,
pero allí obtenemos cercanía arbitraria, no igualdad exacta.

### 4.2 Por qué estos falsificadores no suplantan a los primos ordinarios

El factor (19) cambia el logaritmo derivado y no conserva los pesos
\(\Lambda(m)\). Esto no es una limitación reparable por otro factor con los
mismos pesos. Si, para \(\Re s>1\), dos funciones normalizadas satisfacen

\[
 -{Z_1'(s)\over Z_1(s)}
 =\sum_{m\ge2}{\Lambda(m)\over m^s}
 =-{Z_2'(s)\over Z_2(s)},                           \tag{33}
\]

entonces \((\log Z_1-\log Z_2)'=0\). La normalización en
\(\sigma\to+\infty\) da \(Z_1=Z_2\) en \(\Re s>1\), y la unicidad de la
continuación analítica da la misma función global.

Análogamente, igualdad exacta de \(\mathcal F\) y
\(\widetilde{\mathcal F}\) en cualquier intervalo real abierto fuerza
igualdad global de sus gérmenes por el teorema de identidad. La ecuación
(23) afirma cercanía arbitraria, no igualdad. Los valores o jets **infinitos
y exactos** sí contienen toda la información; el falsificador descarta solo
la inferencia local finita y estable.

Por tanto no existe un «cero que no corresponda a un primo» manteniendo
**exactamente** los \(\Lambda(m)\) ordinarios: esos pesos determinan a
\(\zeta\), y con el factor arquimediano estándar fijo determinan a \(\xi\).
Lo que falta demostrar es una propiedad global de esa única continuación,
no descartar un segundo producto con los mismos coeficientes.

---

## 5. Verificación reproducible

`tools/real_jet_tangent_disk_gate_check.py` comprueba:

1. las identidades geométricas (8), (14) y (15) sobre una malla racional;
2. simetría, normalización y positividad de (19);
3. el decaimiento \(O(\gamma^{-2})\) de los jets de orden \(0,1,2\) en un
   compacto real;
4. la fórmula racional (26) y la presencia de una excursión en cada bloque
   de cuatro índices;
5. para un caso de (28), igualdad de jets en los nodos prescritos y ceros
   explícitos fuera de la línea.

El checker verifica álgebra finita y diagnósticos de escala. El criterio de
Cauchy--Hadamard y la unicidad (33) están probados en el texto.

---

## 6. Veredicto

\[
 \boxed{
 \begin{gathered}
 \mathrm {RH}
 \iff
 \mathscr R(r)\ge1-r\quad(0<r<1),\\
 \text{Euler--}\Lambda\text{ prueba esa desigualdad directamente solo en }
 |z-\tfrac12|<\tfrac12,\\
 \text{ningún argumento estable bajo una cantidad finita de jets reales
 puede completar el paso faltante.}
 \end{gathered}}                                    \tag{34}
\]

**Probado:** (3), (13), la geometría del horodisco, (18), los falsificadores
simétricos estable y de jets finitos exactos, y la unicidad con pesos
exactos.

**No probado:** (3) para \(r<\tfrac12\) a partir de los
\(\Lambda(m)\) ordinarios, la existencia de bloques (9), el límite Deep,
A1 o RH.
