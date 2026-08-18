# 104_74 — Semigrupo Hadamard, fórmula Jensen--logística y gate de residuos interiores

**Resultado.** La razón de presiones de `104_72` sí admite una
representación compleja exacta. No es, sin embargo, un funcional ordinario
de la generatriz de Li: aparece después de aplicar a sus coeficientes un
**exponencial de Hadamard**.

Sea

\[
 \mathcal G(z)
 :=z{d\over dz}\log {\xi(1/(1-z))\over\xi(1)}
 =\sum_{n\geq1}\lambda_nz^n.                              \tag{1}
\]

Si \(\odot\) denota el producto coeficiente a coeficiente, entonces,
formalmente,

\[
 \mathcal U_t(z)
 :=\mathrm{Exp}_{\odot}(-t\mathcal G)(z)
 =\sum_{k\geq0}{(-t)^k\over k!}\mathcal G^{\odot k}(z)
 =\sum_{n\geq1}e^{-t\lambda_n}z^n.                       \tag{2}
\]

Esta serie tiene una dicotomía sin zona intermedia:

\[
 \boxed{
 \mathrm {RH}\Longrightarrow \mathcal U_t\text{ es entera de orden }2/t,
 \qquad
 \neg\mathrm {RH}\Longrightarrow
 R(\mathcal U_t)=0.}                                      \tag{3}
\]

En particular, para cualquier \(t>0\), que (2) tenga radio positivo ya es
equivalente a RH.

Para las actividades reales

\[
 z_n={e^{-\lambda_n}\over n+1},\qquad
 D_L(\omega)=\prod_{n\in I_L}(1+\omega z_n),qquad
 I_L=\{L^2,\ldots,L^2+L-1\},                              \tag{4}
\]

la presión acotada satisface simultáneamente

\[
 e^{\tau G_L}={D_L(1)\over D_L(e^{-\tau})}                \tag{5}
\]

y una fórmula Jensen--logística exacta. Si

\[
 J_L(R)={1\over2\pi}\int_0^{2\pi}
          \log|D_L(Re^{i\theta})|\,d\theta,
 \qquad
 \kappa(v)={e^v\over(1+e^v)^2},                           \tag{6}
\]

entonces

\[
 \boxed{
 G_L={1\over\tau}\int_{-\infty}^{\infty}\kappa(v)
 \{J_L(e^{-v})-J_L(e^{-v-\tau})\}\,dv.}                 \tag{7}
\]

La forma \(\log X\) posee una representación subarmónica análoga mediante
la derivada radial de un potencial de Jensen ponderado.

La ganancia es conceptual y exacta: la presión cuenta, con un suavizado
logístico, ceros de \(D_L\) que cruzan anillos concéntricos. Pero (3)
localiza el gate. Construir analíticamente esos determinantes desde
\(\mathcal G\) exige que el semigrupo de Hadamard exista en algún disco; esa
sola existencia ya excluye todos los polos interiores de la generatriz de
Li.

Se prueba además un no-go cuantitativo. En el cuarteto racional
\(w=2i\), cualquier truncación de (2) a \(K_n=o(2^n)\) potencias de
Hadamard pierde una proporción \(1-o(1)\) de la actividad en la clase mala.
Si el truncamiento es par crea además una actividad falsa en la clase
positiva; si es impar pierde la positividad requerida por Jensen. Para
aproximar las actividades en ambas clases hay que alcanzar
\(K_n\asymp2^n\).

Finalmente, un contorno seguro incondicional separa

\[
 \lambda_n=C_{n,N}-
 \sum_{|w_\rho|<r_N}m_\rho w_\rho^{-n},qquad
 C_{n,N}\ll N^5\log^2N\quad(N\le n\le2N).                \tag{8}
\]

Por tanto toda tasa exponencial queda en la suma finita de residuos
interiores. Jensen, Poisson y las cotas de crecimiento controlan la parte
de contorno; no eliminan esa suma. El documento obtiene una representación
exacta y un gate nuevo, no una prueba de \(G_L\to0\), A1 o RH.

---

## 1. Auditoría de no duplicación

Los antecedentes internos más cercanos son:

* `104_33`, que prueba una fórmula frontera--residuos para el primer momento
  prima--polo;
* `104_62`, que observa que en la escala crítica todos los poderes de
  Hadamard son de orden uno, pero no construye el semigrupo coeficiente a
  coeficiente;
* `104_63`, que estudia la energía lineal \(H^2\) de \(\mathcal G\);
* `104_68`--`104_73`, que construyen las actividades, la razón de presiones
  y sus representaciones probabilísticas o de Bernstein.

Lo nuevo aquí es la combinación de cuatro hechos:

1. la dicotomía radio cero/función entera para
   \(\mathrm{Exp}_\odot(-t\mathcal G)\);
2. la representación exacta de la presión como mezcla de incrementos de
   Jensen;
3. un contorno seguro común a un bloque diádico, con parte exterior
   polinómica;
4. el costo exponencial exacto de truncar el exponencial de Hadamard en el
   falsificador.

No se reclama novedad para la fórmula de Jensen, para el producto de
Hadamard ni para el cálculo de residuos por separado. La aportación es su
aplicación conjunta al detector acotado de Phase 104.

---

## 2. El semigrupo de Hadamard de la generatriz de Li

Para dos series formales sin término constante,

\[
 f(z)=\sum_{n\ge1}f_nz^n,\qquad
 g(z)=\sum_{n\ge1}g_nz^n,
\]

escriba

\[
 (f\odot g)(z)=\sum_{n\ge1}f_ng_nz^n.                    \tag{9}
\]

El elemento unidad de esta álgebra es

\[
 \mathbf1_\odot(z)={z\over1-z}=\sum_{n\ge1}z^n.         \tag{10}
\]

Adopte \(\mathcal G^{\odot0}=\mathbf1_\odot\). Entonces la igualdad
(2) es rigurosa como identidad formal: para cada coeficiente fijo, la suma
en \(k\) es la serie exponencial ordinaria

\[
 \sum_{k\ge0}{(-t)^k\lambda_n^k\over k!}=e^{-t\lambda_n}.
\]

Además

\[
 \mathcal U_t\odot\mathcal U_s=\mathcal U_{t+s},
 \qquad
 \partial_t\mathcal U_t=-\mathcal G\odot\mathcal U_t,
 \qquad
 \mathcal U_0=\mathbf1_\odot.                            \tag{11}
\]

Es un semigrupo diagonal formal. La cuestión analítica es si
\(\mathcal U_t\) define siquiera un germen holomorfo no trivial.

### Teorema 2.1 (dicotomía instantánea)

Para cada \(t>0\), son equivalentes:

1. RH;
2. \(\mathcal U_t\) tiene radio de convergencia positivo;
3. \(\mathcal U_t\) es entera.

Bajo estas condiciones su orden como función entera es exactamente
\(2/t\).

**Demostración.** Bajo RH, el teorema de Lagarias usado en `104_02` da

\[
 \lambda_n={1\over2}n\log n+O(n).                         \tag{12}
\]

Por tanto

\[
 \log {1\over e^{-t\lambda_n}}
 ={t\over2}n\log n+O_t(n).                               \tag{13}
\]

El criterio de Cauchy--Hadamard muestra que el radio es infinito. La
fórmula clásica para el orden de una función entera
\(F(z)=\sum a_nz^n\),

\[
 \mathrm{ord}\,F
 =\limsup_{n\to\infty}{n\log n\over\log(1/|a_n|)},       \tag{14}
\]

aplicada a (13), da \(2/t\).

Si RH es falsa, `104_56` produce \(c>0\), \(R>1\) y un conjunto
sindético infinito \(D\) tal que

\[
 \lambda_n\le-cR^n\qquad(n\in D).                        \tag{15}
\]

En esa subsucesión,

\[
 \left(e^{-t\lambda_n}\right)^{1/n}
 \ge\exp\!\left({tcR^n\over n}\right)\longrightarrow\infty.
 \tag{16}
\]

Luego el radio de (2) es cero. Esto prueba las equivalencias. \(\square\)

La actividad usada por la presión es el coeficiente de

\[
 \mathcal Z_t(z)
 :=\sum_{n\ge1}{e^{-t\lambda_n}\over(n+1)^t}z^n.          \tag{17}
\]

El factor polinómico \((n+1)^{-t}\) no cambia la dicotomía ni el orden.
En particular,

\[
 \boxed{\mathrm {RH}\Longleftrightarrow
 R\!\left(\sum_{n\ge1}{e^{-\lambda_n}\over n+1}z^n\right)>0.}
 \tag{18}
\]

La dirección no-RH de (18) es mucho más fuerte que una singularidad dentro
del disco: no queda ningún disco de convergencia.

---

## 3. Determinante finito y representación Jensen--logística

Ponga

\[
 x_n=\lambda_n+\log(n+1),\qquad z_n=e^{-x_n}>0.           \tag{19}
\]

El polinomio \(D_L\) de (4) es el determinante de la compresión diagonal

\[
 D_L(\omega)
 =\det_{\ell^2(I_L)}
 \left(I+\omega\mathrm{diag}(z_n)_{n\in I_L}\right).
 \tag{20}
\]

La identidad (5) es inmediata de `104_72`:

\[
 \tau G_L
 =\sum_{n\in I_L}\log{1+z_n\over1+e^{-\tau}z_n}.
 \tag{21}
\]

Todos los ceros de \(D_L\) son reales negativos, en
\(-z_n^{-1}\). Jensen da, para todo \(R>0\),

\[
 \boxed{
 J_L(R)=\sum_{n\in I_L}\log^+(Rz_n).}                    \tag{22}
\]

Defina el detector duro

\[
 h_\tau(x)
 :={1\over\tau}\int_0^\tau\mathbf1_{\{x+s<0\}}\,ds
 =\begin{cases}
 0,&x\ge0,\\
 -x/\tau,&-\tau<x<0,\\
 1,&x\le-\tau.
 \end{cases}                                              \tag{23}
\]

Las ecuaciones (19) y (22) dan exactamente

\[
 {J_L(R)-J_L(e^{-\tau}R)\over\tau}
 =\sum_{n\in I_L}h_\tau(x_n-\log R).                     \tag{24}
\]

Sea \(V\) una variable logística estándar, con densidad

\[
 \kappa(v)={e^v\over(1+e^v)^2},
 \qquad
 \mathbb P(V<-y)={1\over1+e^y}.                          \tag{25}
\]

Entonces, por Tonelli,

\[
\begin{aligned}
 \mathbb E h_\tau(x+V)
 &={1\over\tau}\int_0^\tau
   \mathbb P(V<-x-s)\,ds\\
 &={1\over\tau}\int_0^\tau{ds\over1+e^{x+s}}
 =g_\tau(x).                                             \tag{26}
\end{aligned}
\]

Sustituir \(R=e^{-v}\) en (24) y promediar con (25) prueba (7).
No hay aproximación ni límite en esta identidad.

### 3.1 El criterio duro de anillos

Ponga

\[
 H_L={J_L(1)-J_L(e^{-\tau})\over\tau}
 =\sum_{n\in I_L}h_\tau(x_n).                            \tag{27}
\]

Bajo RH, \(x_n\ge\log(n+1)>0\), de modo que \(H_L=0\) para todo
\(L\). Bajo no-RH, el conjunto sindético de (15) aporta
\(h_\tau(x_n)=1\) en una proporción positiva de cada bloque grande. Por
consiguiente,

\[
 \boxed{
 \mathrm {RH}\Longleftrightarrow H_L\longrightarrow0,}
 \qquad
 \neg\mathrm {RH}\Longrightarrow
 \liminf_{L\to\infty}{H_L\over L}>0.                   \tag{28}
\]

Geométricamente, \(H_L\) mide los ceros de \(D_L\) que están dentro del
disco unidad o atraviesan el anillo
\(e^{-\tau}<|\omega|<1\), con peso lineal en el logaritmo del radio.

### 3.2 La forma \(\log X\) como potencial subarmónico

Para \(X\ge1\), defina

\[
 J_X^{\log}(R)
 :=\sum_{n\le X}{1\over n}\log^+(Rz_n).                  \tag{29}
\]

Es la media circular del potencial subarmónico finito

\[
 \omega\longmapsto
 \sum_{n\le X}{1\over n}\log|1+\omega z_n|.
\]

Para casi todo \(R>0\),

\[
 {d\over d\log R}J_X^{\log}(R)
 =\sum_{\substack{n\le X\\Rz_n>1}}{1\over n}
 =:\mathcal N_X^{\log}(R).                              \tag{30}
\]

Usando (25) directamente,

\[
\boxed{
 \mathfrak F(X)
 ={1\over H_X}\int_{-\infty}^{\infty}
 \kappa(v)\,\mathcal N_X^{\log}(e^{-v})\,dv.}           \tag{31}
\]

Así la forma finita de `104_69` es exactamente una masa radial de Riesz
suavizada. Probar que (31) tiende a cero equivale a probar que la masa
ponderada de ceros de los determinantes de actividad escapa a todo anillo
logístico fijo.

---

## 4. Contorno seguro y separación exacta de residuos

La función

\[
 \Phi(z)={\xi(1/(1-z))\over\xi(1)}                        \tag{32}
\]

es holomorfa en \(\mathbb D\), pero puede tener ceros allí. Su derivada
logarítmica ponderada es \(\mathcal G\) de (1). Para un cero no trivial
\(\rho\), ponga

\[
 w_\rho=1-{1\over\rho}.                                  \tag{33}
\]

En \(w_\rho\), \(\mathcal G\) tiene residuo \(m_\rho w_\rho\).
Para un radio \(r<1\) que no pase por un cero, defina

\[
 C_n(r)={1\over2\pi i}\int_{|z|=r}
 {\mathcal G(z)\over z^{n+1}}\,dz.                       \tag{34}
\]

El teorema de residuos da el signo exacto

\[
 \boxed{
 \lambda_n=C_n(r)-
 \sum_{|w_\rho|<r}m_\rho w_\rho^{-n}.}                  \tag{35}
\]

Solo aparecen ceros con \(\Re\rho>1/2\), porque

\[
 |w_\rho|^2
 =1+{1-2\Re\rho\over|\rho|^2}.                          \tag{36}
\]

### Teorema 4.1 (radio seguro común a un bloque)

Para todo \(N\) suficientemente grande existe

\[
 r_N\in[1-2/N,1-1/N]                                     \tag{37}
\]

tal que, uniformemente para \(N\le n\le2N\),

\[
 \boxed{|C_n(r_N)|\ll N^5\log^2N.}                       \tag{38}
\]

La constante implícita es absoluta.

**Demostración.** Use los límites incondicionales estándar

\[
 N_\zeta(T)\ll T\log(T+2),\qquad
 \sum_{|\Im\rho|>T}{m_\rho\over|\rho|^2}
 \ll{\log(T+2)\over T}.                                 \tag{39}
\]

Sea \(K_N\) el número de ceros con \(|\Im\rho|\le2N\), contando
multiplicidad, y ponga

\[
 \delta_N={1\over4N(K_N+1)}\gg{1\over N^2\log N}.       \tag{40}
\]

Al quitar de (37) los intervalos de radio \(\delta_N\) centrados en los
\(|w_\rho|\) correspondientes, se elimina longitud menor que
\(1/(2N)\). Queda un \(r_N\) cuya circunferencia está a distancia al
menos \(\delta_N\) de todos esos polos.

Si \(|\Im\rho|>2N\) y \(|w_\rho|<1\), (36) da

\[
 1-|w_\rho|\le {1\over|\Im\rho|^2}<{1\over4N^2};        \tag{41}
\]

su distancia a (37) es \(\gg1/N\). Los ceros críticos o izquierdos
tienen \(|w_\rho|\ge1\) y satisfacen la misma conclusión. Por tanto

\[
 \mathrm{dist}(|z|=r_N,\{w_\rho\})\ge\delta_N.   \tag{42}
\]

Sobre el círculo, \(s=(1-z)^{-1}\) satisface \(|s|\le N\). Además

\[
 |s-\rho|
 ={|z-w_\rho|\,|\rho|\over|1-z|}
 \gg\delta_N.                                            \tag{43}
\]

El producto canónico de \(\xi\) da

\[
 {\xi'\over\xi}(s)
 =B+\sum_\rho m_\rho
 \left({1\over s-\rho}+{1\over\rho}\right).           \tag{44}
\]

Los ceros con \(|\Im\rho|\le2N\) aportan
\(O(K_N/\delta_N)=O(N^3\log^2N)\). En la cola,
\(|s-\rho|\ge |\Im\rho|-|\Im s|\ge|\Im\rho|/2\); escribir el sumando como
\(s/[\rho(s-\rho)]\) y usar (39) da \(O(\log N)\). Luego

\[
 \sup_{|z|=r_N}\left|{\xi'\over\xi}(s(z))\right|
 \ll N^3\log^2N.                                        \tag{45}
\]

Como

\[
 \mathcal G(z)={z\over(1-z)^2}{\xi'\over\xi}(s(z)),
\]

el supremo de \(|\mathcal G|\) es \(O(N^5\log^2N)\).
Finalmente, \(r_N^{-n}=O(1)\) para \(n\le2N\), y (34) prueba
(38). \(\square\)

Combinar (35) y (38) da (8). El contorno exterior es siempre
subexponencial en el grado del bloque. Toda excursión de tasa fija proviene
de la suma finita

\[
 Z_{n,N}:=\sum_{|w_\rho|<r_N}m_\rho w_\rho^{-n}.          \tag{46}
\]

Una cota de módulo para el contorno no determina el signo de (46).

---

## 5. Qué ve Jensen de \(\xi\), y qué no ve

Aplicado directamente a (32), Jensen da

\[
 \boxed{
 {1\over2\pi}\int_0^{2\pi}\log|\Phi(re^{i\theta})|\,d\theta
 =\sum_{|w_\rho|<r}m_\rho\log{r\over|w_\rho|}\ge0.}     \tag{47}
\]

Por tanto RH equivale a que el miembro izquierdo sea cero para cada
\(r<1\). La subarmonicidad entrega automáticamente el signo opuesto al que
haría falta para concluir esa anulación: produce (47), no una cota superior
por cero. Las cotas de crecimiento de \(\xi\) controlan el tamaño del
miembro izquierdo, pero una cota positiva no excluye una masa interior
finita.

La media radial tampoco contiene las fases necesarias para cuantificar la
presión. Esto se ve dentro de la clase de divisores que conserva ecuación
funcional y conjugación. Fije \(0<r<1\), \(a=re^{i\vartheta}\), y ponga

\[
 \rho_a={1\over1-a},\qquad
 X_a(s)=\prod_{\eta\in
 \{\rho_a,\bar\rho_a,1-\rho_a,1-\bar\rho_a\}}(s-\eta).
 \tag{48}
\]

El polinomio es real y satisface \(X_a(1-s)=X_a(s)\). Dentro del disco,
\(X_a(1/(1-z))/X_a(1)\) tiene exactamente los ceros \(a,\bar a\). Por
ello todas sus medias de Jensen son

\[
 \boxed{J_a(R)=2\log^+(R/r)\qquad(0<R<1),}               \tag{49}
\]

independientemente de \(\vartheta\). En cambio sus coeficientes de Li son

\[
 Q_n^{(a)}=4-2(r^n+r^{-n})\cos(n\vartheta).               \tag{50}
\]

Con \(r=3/4\), las elecciones \(\vartheta=\pi/2\) y
\(\vartheta=\pi/3\) tienen exactamente el mismo dato (49), pero

\[
 {G_L^{(\pi/2)}\over L}\longrightarrow{1\over4},
 \qquad
 {G_L^{(\pi/3)}\over L}\longrightarrow{1\over2}.        \tag{51}
\]

En el primer caso \(\cos(n\vartheta)>0\) en una clase de cuatro; en el
segundo, en tres clases de seis. Sobre esas clases (50) tiende
exponencialmente a \(-\infty\), y en las restantes no contribuye a la
presión.

La ecuación (51) no dice que Jensen sea incapaz de detectar un cero
interior: (47) lo detecta. Dice que una estimación radial no controla la
densidad ni la fase que aparece en (7). Para probar RH por (47) habría que
probar directamente que su masa no negativa es cero; eso es ya la ausencia
de todos los \(w_\rho\) interiores.

---

## 6. Gate cuantitativo de truncación Hadamard

Defina el truncamiento formal

\[
 \mathcal U_{t,K}(z)
 :=\sum_{k=0}^K{(-t)^k\over k!}\mathcal G^{\odot k}(z).
 \tag{52}
\]

Su coeficiente de grado \(n\) es el polinomio de Taylor

\[
 [z^n]\mathcal U_{t,K}
 =\sum_{k=0}^K{(-t\lambda_n)^k\over k!}.                  \tag{53}
\]

Use el cuarteto racional

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\}.          \tag{54}
\]

Para \(4\mid n\), escriba

\[
 Y_n=-Q_n=2(2^n+2^{-n})-4\ge2^n.                         \tag{55}
\]

Si \(K\le tY_n/2\), entonces

\[
\begin{aligned}
 {\sum_{k=0}^K(tY_n)^k/k!\over e^{tY_n}}
 &=\mathbb P\{\mathrm{Pois}(tY_n)\le K\}\\
 &\le e^{-tY_n/8}.                                       \tag{56}
\end{aligned}
\]

La última desigualdad es la cota de Chernoff con desviación \(1/2\).
Por tanto una truncación con \(K_n=o(2^n)\) pierde una fracción
\(1-o(1)\) de la actividad verdadera \(e^{-Q_n}=e^{Y_n}\) en toda la
clase mala.

En la clase \(n\equiv2\pmod4\), ponga
\(Y_n^+=Q_n=4+2(2^n+2^{-n})\). Si \(K=o(Y_n^+)\), el último término de
(53) domina:

\[
 \sum_{k=0}^K{(-tY_n^+)^k\over k!}
 =(-1)^K{(tY_n^+)^K\over K!}{1+o(1)\}.                  \tag{57}
\]

En efecto, la suma de los cocientes absolutos de todos los términos
anteriores respecto del último está acotada por

\[
 \sum_{j\ge1}\left({K\over tY_n^+}\right)^j=o(1).       \tag{58}
\]

Así:

* si \(K\) es par, el truncamiento crea una actividad positiva enorme en
  relación con la verdadera también en la clase donde esta tiende a cero
  (y, si \(K\to\infty\), enorme también en valor absoluto);
* si \(K\) es impar, esa actividad se vuelve negativa y el polinomio
  determinante pierde la geometría de ceros reales negativos usada por
  Jensen.

Para aproximar las actividades verdaderas con error relativo menor que una
constante fija en ambas clases es necesario alcanzar

\[
 \boxed{K_n\gg2^n.}                                      \tag{59}
\]

Esta escala es también suficiente, salvo una constante que depende de
\(t\). En la clase mala, truncar \(e^x\) después de \(K\ge2x\)
términos deja una cola relativa de Poisson exponencialmente pequeña. En
la clase positiva, el resto de Taylor y

\[
 {e^x x^{K+1}\over(K+1)!}
 \le e^x\left({ex\over K+1}\right)^{K+1}
\]

muestran, por ejemplo, que \(K+1\ge4x\) da error relativo
exponencialmente pequeño. Como en ambas clases \(x\asymp_t2^n\), el
costo de una aproximación Taylor directa es \(\Theta_t(2^n)\).

En una ventana \(n\asymp L^2\), el número de poderes de Hadamard requerido
es \(\exp(\Theta(L^2))\). Esto cierra los truncamientos fijos,
polinómicos y, en general, \(e^{o(n)}\). No descarta una identidad no
perturbativa para el semigrupo completo.

---

## 7. Veredicto

**Probado.** La dicotomía de radio (3), el determinante (5), la fórmula
Jensen--logística (7), el potencial \(\log X\) (31), el contorno seguro
(35)--(38), la fórmula radial de Jensen (47), el falsificador de fase
(49)--(51) y el gate exponencial de truncación (56)--(59).

**Ganancia.** El observable acotado tiene una interpretación compleja
precisa: es una media logística de masas de Jensen de determinantes finitos.
Toda la tasa exponencial de los coeficientes queda además separada en los
residuos interiores, mientras el contorno puede hacerse polinómico sobre
bloques completos.

**No-go.** La construcción de los determinantes a partir de la generatriz
de Li requiere el exponencial de Hadamard completo. La existencia analítica
de ese semigrupo ya equivale a RH, y ninguna truncación de orden
subexponencial pasa el cuarteto. Jensen aplicado directamente a \(\xi\)
convierte el problema en anular su masa interior no negativa, sin aportar
esa anulación.

**Frente que sobrevive.** Una identidad no perturbativa, específica de los
pesos reales \(\Lambda(m)\), que controle directamente el determinante
finito (20) o la diferencia completa prima--polo antes de formar sus
actividades. No puede provenir de un número subexponencial de poderes de
Hadamard ni de una cota radial de módulo.

**No probado.** \(G_L\to0\), \(\mathfrak F(X)\to0\), A1 o RH.

---

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 hadamard_jensen_pressure_check.py
```

El checker verifica la identidad de semigrupo en grados finitos, Jensen
para determinantes con actividades positivas, la mezcla logística (7), las
densidades \(1/4\) y \(1/2\) de (51), y las escalas de truncación del
cuarteto. El Teorema 4.1 y las equivalencias asintóticas se prueban en el
texto; no se certifican mediante muestreo.
