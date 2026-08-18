# 104_77 — Contorno seguro, Cartan--Turán y gate de cola profunda

**Resultado.** Se atacó directamente el criterio profundo de `104_75`,

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le-e^{\sqrt X}\}}\longrightarrow0.
 \tag{1}
\]

El contorno seguro de `104_74` permite separar rigurosamente, grado por
grado, una parte exterior polinómica y una suma finita de residuos
interiores. En la escala de (1), la parte exterior es despreciable:

\[
 \lambda_n=C_{n,n}-Z_n,\qquad
 |C_{n,n}|\ll n^5\log^2n,
 \qquad
 Z_n=\sum_{|w_\rho|<r_n}m_\rho w_\rho^{-n}.              \tag{2}
\]

Por tanto (1) es equivalente, en la dicotomía RH/no-RH, a una cota de
densidad unilateral para \(Z_n\). Esta separación es incondicional y no
supone que la suma esté vacía.

El ataque complejo no cierra esa cota. Jensen mide exactamente la masa de
los mismos polos, mientras Turán fuerza grandes sumas de potencias cuando
alguno existe. Ambos mecanismos tienen el signo opuesto al requerido para
eliminar \(Z_n\). Cartan puede retirar discos que contienen ceros, pero un
solo disco retirado puede contener el polo que produce una densidad positiva
de excursiones profundas; desecharlo pierde precisamente la información que
hay que controlar.

Se añade un falsificador cuantitativo más fuerte que el radial de `104_74`.
El cuarteto \(w=2i\) conserva conjugación y simetría funcional, tiene
coeficientes negativos exponenciales en una clase de densidad \(1/4\), pero
su generatriz continuada es **estrictamente positiva en todo el rayo real**
\(0<r<1\). Luego ni Jensen/Cartan, ni Turán, ni la positividad y el crecimiento
de la continuación sobre el rayo Euler pueden probar (1) sin usar una
desigualdad adicional específica de los pesos reales \(\Lambda(m)\).

El documento prueba una reducción y un no-go para este paquete de análisis
complejo. No prueba (1), A1 ni RH.

---

## 1. El residuo interior es todo el observable profundo

Ponga

\[
 \Phi(z)={\xi(1/(1-z))\over\xi(1)},\qquad
 \mathcal G(z)=z{\Phi'(z)\over\Phi(z)}
              =\sum_{n\ge1}\lambda_nz^n,                \tag{3}
\]

y, para cada cero no trivial \(\rho\),

\[
 w_\rho=1-{1\over\rho}.                                  \tag{4}
\]

El Teorema 4.1 de `104_74` construye, para todo \(N\) grande, un radio

\[
 r_N\in[1-2/N,1-1/N]                                    \tag{5}
\]

que no atraviesa polos y para el cual

\[
 \lambda_n=C_{n,N}-
 \sum_{|w_\rho|<r_N}m_\rho w_\rho^{-n},
 \qquad
 |C_{n,N}|\le K N^5\log^2N\quad(N\le n\le2N),           \tag{6}
\]

con una constante absoluta \(K\). No se ha usado RH. La suma de (6) es
real, porque el conjunto de polos es estable por conjugación.

Tomando \(N=n\) (lo cual es legítimo porque el extremo \(n=N\) pertenece
al rango \(N\le n\le2N\) del Teorema 4.1), defina, para \(n\) bastante
grande,

\[
 Z_n:=\sum_{|w_\rho|<r_n}m_\rho w_\rho^{-n},
 \qquad P_n:=K n^5\log^2n.                              \tag{7}
\]

La suma es finita: para cada \(r_n<1\), la condición
\(|w_\rho|<r_n\) fuerza que \(|\Im\rho|\) esté acotado. Fijamos
\(Z_n:=0\) en el prefijo finito que el teorema no cubre; esta convención no
altera ninguna de las densidades siguientes. A partir del primer índice
cubierto, para \(S_X=e^{\sqrt X}\) y \(n\le X\), (6) da las inclusiones
exactas

\[
 \begin{aligned}
 \{Z_n\ge S_X+P_n+\log(n+1)\}
 &\subseteq
 \{\lambda_n+\log(n+1)\le-S_X\},\\
 \{\lambda_n+\log(n+1)\le-S_X\}
 &\subseteq
 \{Z_n\ge S_X-P_n\}.
 \end{aligned}                                          \tag{8}
\]

En el intervalo \(K_0\sqrt X\le n\le X\), el error
\(P_n+\log(n+1)=e^{o(\sqrt X)}\) es despreciable frente a \(S_X\).
Esto no autoriza a reemplazar indicadores duros por una estimación
Lipschitz. La equivalencia correcta usa la dicotomía de residuos.

### Proposición 1.1 (dicotomía profunda de la suma de residuos)

Las siguientes afirmaciones son equivalentes:

1. RH;
2. la media de (1) tiende a cero;
3. se tiene

   \[
   {1\over H_X}\sum_{n\le X}{1\over n}
   {\bf1}_{\{Z_n\ge e^{\sqrt X}+P_n+\log(n+1)\}}
   \longrightarrow0.                                    \tag{9}
   \]

**Demostración.** Si RH vale, no hay \(w_\rho\) con \(|w_\rho|<1\),
luego \(Z_n=0\) y (9) es idénticamente cero; (1) también lo es por
\(\lambda_n\ge0\).

Si RH es falsa, `104_56` da un módulo dominante \(R>1\), constantes
\(c>0\), \(R_1<R\), y un conjunto sindético \(D\) de densidad natural
\(d>0\) tales que

\[
 \lambda_n=-R^nS(n)+O(n^2R_1^n+n^2),
 \qquad S(n)>c\quad(n\in D).                            \tag{10}
\]

Para \(n\) grande, el radio \(r_n\) contiene todos los polos dominantes.
Comparando (6) y (10), o separando directamente esos polos en (7), se
obtiene

\[
 Z_n\ge {c\over2}R^n\qquad(n\in D)                      \tag{11}
\]

desde un índice fijo. Elija \(K_0>1/\log R\). Para
\(n\in D\cap[K_0\sqrt X,X]\), (11) domina
\(e^{\sqrt X}+P_n+\log(n+1)\). Por sumación parcial,

\[
 {1\over H_X}
 \sum_{\substack{K_0\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                          \tag{12}
\]

Así (9) falla. La equivalencia entre 1 y 2 es el Teorema 2.1 de `104_75`.
\(\square\)

La Proposición 1.1 no es una prueba nueva de RH: identifica exactamente
qué tendría que acotarse después de que el contorno ha retirado todo error
subexponencial.

---

## 2. Jensen convierte la pregunta en anular masa interior

Para \(0<r<1\) que no atraviese un cero, Jensen aplicado a (3) da

\[
 J(r):={1\over2\pi}\int_0^{2\pi}
 \log|\Phi(re^{i\theta})|\,d\theta
 =\sum_{|w_\rho|<r}m_\rho\log{r\over|w_\rho|}\ge0.       \tag{13}
\]

Como \(\Phi(0)=1\), no hay término central. De (13),

\[
 \boxed{
 \mathrm {RH}\quad\Longleftrightarrow\quad
 J(r)=0\ \text{para todo }0<r<1
 \quad\Longleftrightarrow\quad
 \liminf_{r\uparrow1}J(r)=0.}                           \tag{14}
\]

La última equivalencia es rigurosa: si existe un cero interior
\(w_0\) de \(\Phi\) (equivalentemente, un polo de \(\mathcal G\)), entonces,
para todo \(r>|w_0|\),

\[
 J(r)\ge m_0\log{r\over|w_0|}
 \longrightarrow m_0\log{1\over|w_0|}>0.               \tag{15}
\]

Por tanto una ruta Jensen debe probar una **cota superior que tienda a
cero** para la cantidad no negativa (13). Subarmonicidad solo entrega el
signo \(J(r)\ge0\). Las cotas ordinarias de crecimiento de \(\xi\) dan una
cota positiva para \(J(r)\), no la anulación de (15).

Cartan no mejora este punto lógico. Al aplicarlo a un producto truncado,
sus lemas dan cotas inferiores para \(|\Phi|\) fuera de una unión de discos
que cubren los ceros; la suma de radios permitida es un parámetro del lema,
y Jensen aporta el conteo ponderado usado para elegir el truncamiento.
Pero (15) muestra que un solo disco, por pequeño que sea, puede contener el
cero que genera todas las excursiones de (11). Retirar los discos de Cartan
retira exactamente el término \(Z_n\) que aparece en (9).

La pérdida es cuantitativa, no solo lógica. Para \(0<|a|<1\), la función
meromorfa elemental

\[
 f_a(z)={1\over1-z/a}=\sum_{n\ge0}a^{-n}z^n
 \qquad(|z|<|a|)                                        \tag{15a}
\]

tiene coeficientes exponenciales, mientras su característica de Nevanlinna
permanece acotada cuando \(r\uparrow1\): el término de conteo del único
polo es \(N(r,f_a)=\log(r/|a|)\) para \(r>|a|\), y el término de proximidad
es \(O_a(1)\). Así una cota incluso uniforme para la característica de
Nevanlinna es compatible con coeficientes \(|a|^{-n}\). Para recuperar esos
coeficientes hay que añadir explícitamente la parte principal en \(a\), que
es exactamente el sumando de \(Z_n\) en (7).

---

## 3. Turán fuerza la cola mala; no la excluye

Sea \(R>1\) el máximo de \(|w_\rho|^{-1}\) sobre los polos interiores de
\(\mathcal G\) (los ceros interiores de \(\Phi\)) y
escriba los modos dominantes como

\[
 w_j^{-1}=Re^{i\phi_j}\qquad(1\le j\le M).              \tag{16}
\]

El power sum dominante es

\[
 R^nS(n),\qquad S(n)=\sum_{j=1}^M m_j\cos(n\phi_j).      \tag{17}
\]

Los teoremas de sumas de potencias de Turán prueban que una familia no
nula como (17) alcanza tamaño comparable con \(R^n\) en bloques de longitud
controlada por el número de modos. Para el signo real necesario aquí no
hace falta una versión cuantitativa: el cierre compacto del giro
\(n(\phi_1,\ldots,\phi_M)\) contiene el origen, y todo entorno del origen
tiene un conjunto sindético de retornos. En esos retornos,

\[
 S(n)>{1\over2}\sum_{j=1}^Mm_j>0.                       \tag{18}
\]

Las ecuaciones (17)--(18) son precisamente el mecanismo de (11). Así,
Turán confirma que todo polo interior de \(\mathcal G\) produce la cola
profunda con densidad
positiva. Para deducir (9), habría que probar antes que no existe ningún
modo \(|w_j|^{-1}>1\), o que todos sus residuos se anulan. En el logaritmo
derivado los residuos son las multiplicidades positivas \(m_j\), de modo
que no pueden anularse modo por modo.

Éste es el sentido exacto del gate: Turán es un detector eficaz de no-RH,
pero su desigualdad natural es un **minorante de excursiones**, mientras
(9) necesita un mayorante que las elimine.

---

## 4. Falsificador en el rayo real de Euler

El paquete Jensen--Cartan--Turán podría intentar reforzarse usando que, para
\(s>1\), el logaritmo derivado real proviene de los pesos positivos
\(\Lambda(m)\). La positividad o el crecimiento sobre ese único rayo no
controlan los polos complejos.

Considere el cuarteto racional con \(w=2i\) y coeficientes

\[
 q_n=4-2\Re\{w^n+w^{-n}\}.                              \tag{19}
\]

Su generatriz, inicialmente para \(|z|<1/2\), tiene la continuación racional

\[
 \mathcal Q(z)
 ={4z\over1-z}
 -{wz\over1-wz}-{\bar w z\over1-\bar w z}
 -{w^{-1}z\over1-w^{-1}z}
 -{\bar w^{-1}z\over1-\bar w^{-1}z}.                   \tag{20}
\]

Para \(z=r\) real, los términos conjugados de (20) pueden agruparse como
dos partes reales. En todo el rayo \(0<r<1\), (20) es regular y satisface
la identidad exacta

\[
 \boxed{
 \mathcal Q(r)
 ={4r\over1-r}
  +{8r^2\over1+4r^2}
  +{2r^2\over4+r^2}>0.}                                 \tag{21}
\]

Sin embargo, para \(4\mid n\),

\[
 q_n=4-2(2^n+2^{-n})=-2^{n+1}+4+O(2^{-n}),              \tag{22}
\]

y las otras tres clases no tienen una excursión negativa de esa tasa. De
(22),

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{q_n+\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow{1\over8}.}                            \tag{23}
\]

En efecto, los múltiplos de cuatro que cuentan empiezan en
\(n=(1/\log2+o(1))\sqrt X\), y su masa armónica es

\[
 {1\over4}\left(\log X-{1\over2}\log X+O(1)\right)
 ={1\over8}\log X+O(1).                                \tag{24}
\]

El cuarteto no posee el producto de Euler de \(\zeta\), y por eso no refuta
una desigualdad nueva que use la secuencia exacta \(\Lambda(m)\). Sí refuta
la inferencia

\[
 \begin{gathered}
 \text{simetría funcional + conjugación + crecimiento finito}\cr
 \text{+ Jensen/Cartan/Turán + positividad en el rayo real}
 \end{gathered}
 \quad\Longrightarrow\quad\text{cola profunda nula}.   \tag{25}
\]

El detalle clave es que la continuación de (20) es positiva para
\(r>1/2\), pero allí ya no coincide con la suma de su serie de Taylor:
los polos \(z=\pm i/2\) reducen el radio a \(1/2\). Usar la continuación
real como una suma Abel de los coeficientes después de cruzar esos polos
omitiría exactamente los residuos interiores.

---

## 5. Balance y teorema que falta

**Probado incondicionalmente:**

* la reducción segura (6)--(9), sin suponer ausencia de polos;
* la equivalencia escalar Jensen (14);
* que Turán y recurrencia compacta fuerzan, en vez de suprimir, la cola
  profunda producida por un polo;
* el falsificador (21)--(23), que mantiene positivo todo el rayo real.

**No probado:** la cota (9) para los residuos de la \(\zeta\) real, el
criterio aritmético (22a) de `104_75`, A1 o RH.

El input faltante puede escribirse sin contornos:

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}
 \right\}}\longrightarrow0,                            \tag{26}
\]

o, después del contorno seguro, como (9). Cualquiera de las dos
afirmaciones es equivalente a RH; asumir que \(\mathcal G\) es holomorfa
en el disco, que \(J(r)=0\), que \(Z_n=0\), o que el semigrupo Hadamard
tiene radio positivo sería usar esa conclusión circularmente.

La ruta compleja solo puede avanzar si produce desde los pesos exactos
\(\Lambda(m)\) una cota unilateral para (26) que incluya los residuos en
vez de quitarlos mediante discos de Cartan o una hipótesis de holomorfía.

---

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 cartan_turan_deep_tail_check.py
```

El checker verifica la fórmula positiva (21), la identidad de coeficientes
(19)--(20), el signo exponencial (22) y la convergencia numérica de la masa
armónica de (23) hacia \(1/8\).
