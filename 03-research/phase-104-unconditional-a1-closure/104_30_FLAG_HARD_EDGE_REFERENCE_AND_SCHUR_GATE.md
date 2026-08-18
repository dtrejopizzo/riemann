# 104_30 — Referencia positiva de bandera y gate espectral hard-edge

**Rol.** Construir la forma prima--polo regulada que falta en 104_28,
polarizarla exactamente en la base de Laguerre y buscar una referencia
positiva que evalúe \(A_n\) sobre todos los rayos \(g_n\), \(n\ge150\).

La construcción existe. La referencia positiva es una forma diagonal de
bandera, no el canal arquimediano local. Produce un cociente espectral exacto
en toda sección finita y permite ejecutar el diagnóstico de masa espectral
en el gauge correcto. El diagnóstico es favorable hasta \(N=500\), pero no
es un certificado. Las cotas directas de Gershgorin--Schur pierden la
cancelación antes de ese punto y, en forma analítica, requieren controlar
precisamente las segundas diferencias de \(A_n-\lambda_n\).

Este documento no prueba A1 ni RH.

## 1. Forma prima--polo regulada

Sean

\[
 \phi_k(x)={\bf1}_{x\ge0}e^{-x/2}L_k(x),
 \qquad
 g_n=\sum_{k=0}^{n-1}\phi_k,
\]

y sea

\[
 (S_a h)(x)={\bf1}_{x\ge a}h(x-a).
\]

Polarizamos el semigrupo mediante

\[
 \mathsf B_a(g,h)
 ={1\over2}\left(
   \langle S_ag,h\rangle+\langle g,S_ah\rangle
 \right).                                                     \tag{1}
\]

Para \(\varepsilon>0\), pongamos
\(\alpha=\frac12-\varepsilon\) y definamos

\[
 \boxed{
 \mathsf Q_\varepsilon(g,h)
 =\sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}}
       \mathsf B_{\log m}(g,h)
  -\int_0^\infty e^{\alpha a}\mathsf B_a(g,h)\,da.}            \tag{2}
\]

La combinación (2), no sus dos términos después de retirar el regulador, es
el objeto correcto. La identidad de 104_28

\[
 \langle S_ag_n,g_n\rangle
 =e^{-a/2}L_{n-1}^{(1)}(a)                                    \tag{3}
\]

da

\[
 \begin{aligned}
 \mathsf Q_\varepsilon[g_n]
 =P_{n,\varepsilon}
 :={}&\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       L_{n-1}^{(1)}(\log m)\\
 &-\int_0^\infty e^{-\varepsilon a}
       L_{n-1}^{(1)}(a)\,da .
 \end{aligned}                                                 \tag{4}
\]

La fórmula prima--Laguerre prueba

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}P_{n,\varepsilon}
 =B_n:=A_n-\lambda_n.}                                        \tag{5}
\]

El segundo término de (4) es exactamente

\[
 p_n(\varepsilon)
 =n\sum_{j=1}^n
   {n-1\choose j-1}{(-1)^{j-1}\over j\varepsilon^j}.           \tag{6}
\]

### 1.1 Cierre para regulador fijo

Para

\[
 \mathcal H_\eta=L^2((0,\infty),e^{2\eta x}dx),
 \qquad
 \alpha<\eta<{1\over2},
\]

se tiene

\[
 |\mathsf B_a(g,h)|
 \le e^{-\eta a}\|g\|_\eta\|h\|_\eta.                          \tag{7}
\]

Escribiendo

\[
 \delta=\eta-\alpha\in(0,\varepsilon),
\]

la ecuación (7) prueba que \(\mathsf Q_\varepsilon\) es una forma
simétrica acotada, por tanto cerrada, y

\[
 \|\mathsf Q_\varepsilon\|
 \le -{\zeta'\over\zeta}(1+\delta)+{1\over\delta}.              \tag{8}
\]

No hay transferencia uniforme obtenida de (8): el intervalo admisible para
\(\eta\) colapsa cuando \(\varepsilon\downarrow0\). Además,
\(\|g_n\|_\eta^2\) tiene escala

\[
 \binom{2n-2}{n-1}
 [\,2(\varepsilon-\delta)\,]^{-(2n-1)},                        \tag{9}
\]

y optimizar por separado (8)--(9) produce una pérdida de orden
\(n\varepsilon^{-2n}\). Ésta es otra forma de la cancelación Abel que no
puede separarse.

## 2. La forma regulada es indefinida

La positividad global buscada en 104_28 no existe ni siquiera antes de tomar
el límite. Sea

\[
 u_\delta=\delta^{-1/2}{\bf1}_{[0,\delta]},
 \qquad
 0<\delta<\log2.
\]

No hay solapamiento primo y

\[
 \mathsf Q_\varepsilon[u_\delta]
 =-I_0,
 \qquad
 I_0={e^{\alpha\delta}-1-\alpha\delta
          \over\delta\alpha^2}>0,                              \tag{10}
\]

con el valor continuo \(I_0=\delta/2\) cuando \(\alpha=0\).

Ahora sea \(L=\log2\) y

\[
 v_\delta={u_\delta+S_Lu_\delta\over\sqrt2},
 \qquad
 \delta<\min(\log2,\log(3/2)).
\]

Sólo el átomo \(m=2\) solapa las dos cajas, y

\[
 \mathsf Q_\varepsilon[v_\delta]
 ={\log2\over2^{3/2+\varepsilon}}-I_0-I_L,
 \qquad
 I_L={e^{\alpha L}\bigl(\cosh(\alpha\delta)-1\bigr)
          \over\delta\alpha^2}.                               \tag{11}
\]

Como \(I_0+I_L=O_\varepsilon(\delta)\), la expresión (11) es
positiva para \(\delta\) suficientemente pequeño. Las ecuaciones
(10)--(11) prueban que \(\mathsf Q_\varepsilon\) es indefinida para todo
\(\varepsilon>0\). Se descarta así una referencia obtenida declarando
positivo el canal prima--polo.

## 3. Matriz Toeplitz exacta y límite algebraico

La identidad de traslación de Laguerre es

\[
 \langle S_a\phi_j,\phi_k\rangle
 =
 \begin{cases}
 e^{-a/2}L_{k-j}^{(-1)}(a),&k\ge j,\\
 0,&k<j.
 \end{cases}                                                   \tag{12}
\]

Por tanto (2) es Toeplitz en toda sección finita:

\[
 \mathsf Q_\varepsilon(\phi_j,\phi_k)
 =q_{|j-k|}(\varepsilon),                                     \tag{13}
\]

donde

\[
 \boxed{
 q_0(\varepsilon)
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
   -{1\over\varepsilon}
 =-{\zeta'\over\zeta}(1+\varepsilon)-{1\over\varepsilon}}      \tag{14}
\]

y, para \(d\ge1\),

\[
 \boxed{
 q_d(\varepsilon)
 ={1\over2}\left[
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       L_d^{(-1)}(\log m)-I_d(\varepsilon)
 \right],}                                                     \tag{15}
\]

\[
 \boxed{
 I_d(\varepsilon)
 =\int_0^\infty e^{-\varepsilon a}L_d^{(-1)}(a)\,da
 ={(-1)^d(1-\varepsilon)^{d-1}\over\varepsilon^{d+1}}.}        \tag{16}
\]

La función generatriz

\[
 \sum_{d\ge0}L_d^{(-1)}(a)t^d
 =\exp\left(-{at\over1-t}\right)
\]

prueba (16). Si \(F(s)=-\zeta'(s)/\zeta(s)\), la suma prima de
(15) también puede escribirse, sin truncación, como

\[
 \sum_{j=1}^d
 {1\over j!}{d-1\choose j-1}F^{(j)}(1+\varepsilon).            \tag{17}
\]

Las divergencias de (16) y (17) se cancelan sólo en su diferencia.

De (4) y (13),

\[
 P_{n,\varepsilon}
 =nq_0(\varepsilon)
  +2\sum_{d=1}^{n-1}(n-d)q_d(\varepsilon).                    \tag{18}
\]

Pongamos \(B_0=0\). La inversión triangular de (18) y (5) da el
límite entrada por entrada

\[
 \boxed{
 q_0=B_1=-\gamma,
 \qquad
 q_d={B_{d+1}-2B_d+B_{d-1}\over2}\quad(d\ge1).}                \tag{19}
\]

La forma
\(\mathsf Q_0=[q_{|j-k|}]\) queda así definida en el espacio algebraico
de sucesiones de soporte finito. No se afirma que sea cerrable en
\(L^2(0,\infty)\), ni que (8) sobreviva al límite.

## 4. Referencia positiva que evalúa \(A_n\)

Fijemos \(M=150\) y usemos la base ortogonal, no normalizada,

\[
 b_0=g_M,
 \qquad
 b_r=\phi_{M+r-1}\quad(r\ge1).                                \tag{20}
\]

Para

\[
 v=a_0g_M+\sum_{k\ge M}a_k\phi_k
\]

definimos la forma diagonal de bandera

\[
 \boxed{
 \mathsf A_{\rm flag}[v]
 =A_M|a_0|^2
  +\sum_{k\ge M}(A_{k+1}-A_k)|a_k|^2.}                        \tag{21}
\]

Esta forma es positiva y cerrada en su dominio diagonal. En efecto,
\(A_M>0\), y si

\[
 \Delta A_n=A_{n+1}-A_n,
\]

entonces

\[
 \Delta^2 A_n
 :=A_{n+2}-2A_{n+1}+A_n
 =\sum_{\substack{r\ge1\\r\ {\rm impar}}}
   {(1-1/r)^n\over r^2}>0.                                   \tag{22}
\]

Así \(\Delta A_n\) es creciente. El valor positivo en el umbral finito
implica \(\Delta A_k>0\) para \(k\ge M\).

Como

\[
 g_n=g_M+\sum_{k=M}^{n-1}\phi_k
 \qquad(n\ge M),                                               \tag{23}
\]

el telescopado da

\[
 \boxed{\mathsf A_{\rm flag}[g_n]=A_n.}                        \tag{24}
\]

La construcción (21) resuelve el problema de tipo encontrado en 104_28,
pero debe leerse con cuidado: es una referencia no local fabricada a partir
de la sucesión \(A_n\). No identifica el canal Gamma--polo con una forma
positiva y no produce por sí sola ninguna desigualdad para
\(\mathsf Q_0\).

## 5. Matriz exacta en la base de bandera

En la sección

\[
 \mathcal V_{M,N}
 =\operatorname{span}\{g_M,\phi_M,\ldots,\phi_{N-1}\},         \tag{25}
\]

la matriz de \(\mathsf A_{\rm flag}\) es

\[
 D_{M,N}
 =\operatorname{diag}
   (A_M,\Delta A_M,\ldots,\Delta A_{N-1})>0.                  \tag{26}
\]

La matriz de \(\mathsf Q_0\) queda completamente explícita. Para
\(M\le k,l<N\),

\[
 \begin{aligned}
 \mathsf Q_0(g_M,g_M)&=B_M,\\
 \mathsf Q_0(\phi_k,\phi_l)&=q_{|k-l|},\\
 \mathsf Q_0(g_M,\phi_k)
 &=s_k:=\sum_{d=k-M+1}^{k}q_d\\
 &={1\over2}\left[
     (B_{k+1}-B_k)
     -(B_{k-M+1}-B_{k-M})
   \right].
 \end{aligned}                                                 \tag{27}
\]

**Chequeo de índices de (27).** Para \(k=M\), la suma es
\(\sum_{d=1}^{M}q_d\), y el segundo incremento del último renglón es
\(B_1-B_0\). Para \(k=M+r\), los índices son
\(d=r+1,\ldots,M+r\). Por tanto no falta ni sobra el término \(q_0\).

Las mismas ecuaciones valen para \(\varepsilon>0\), reemplazando \(B_n\)
por \(P_{n,\varepsilon}\).

Definimos la matriz blanqueada

\[
 \boxed{
 K_{M,N}=D_{M,N}^{-1/2}Q_{M,N}D_{M,N}^{-1/2}.}                 \tag{28}
\]

Si \(x_n=(1,\ldots,1,0,\ldots,0)\) son las coordenadas de (23), el
vector unitario correcto es

\[
 u_n={D_{M,N}^{1/2}x_n\over\sqrt{A_n}},                        \tag{29}
\]

y

\[
 \boxed{
 \|u_n\|^2=1,
 \qquad
 \langle u_n,K_{M,N}u_n\rangle
 ={B_n\over A_n}
 =1-{\lambda_n\over A_n}.}                                    \tag{30}
\]

Así \(\lambda_n\ge cA_n\) equivale a que el promedio espectral específico
de \(u_n\) sea a lo sumo \(1-c\). Para el enunciado scale-free basta
algún \(c>1/4\). La elección \(c=501/2002\) de 104_26 pide el techo
exacto

\[
 1-c={1501\over2002}=0.7497502497\ldots,
\]

levemente menor que \(3/4\).

Controlar sólo la masa en \([3/4,\infty)\) no basta sin un control de la
cola espectral: la igualdad relevante es el primer momento completo de
(30). El diagnóstico registra por ello masa, momento excedente y
expectativa.

## 6. Diagnóstico reproducible

El archivo **tools/flag_hard_edge_spectrum.py** usa
**lambda_arch** y dos extracciones Cauchy/FFT de **li_lambda**. Verifica
para cada \(M\le n\le N\) las identidades (24), (27) y (30),
diagonaliza (28) y calcula la masa espectral de cada \(u_n\) en
\([3/4,\infty)\). Se reproduce con

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 flag_hard_edge_spectrum.py --nmax 500 \
      --sections 200 250 300 350 400 500

Resultados de doble precisión, no certificados:

| \(N\) | \(\lambda_{\min}(K)\) | \(\lambda_{\max}(K)\) | Gershgorin sup. | Schur ponderado |
|---:|---:|---:|---:|---:|
| 200 | \(-0.363476\) | \(0.033546\) | \(0.118739\) | \(0.711902\) |
| 250 | \(-0.363476\) | \(0.066179\) | \(0.279405\) | \(0.763377\) |
| 300 | \(-0.363476\) | \(0.091360\) | \(0.497693\) | \(0.821868\) |
| 350 | \(-0.363476\) | \(0.108870\) | \(0.726895\) | \(0.898923\) |
| 400 | \(-0.363477\) | \(0.125661\) | \(0.924004\) | \(1.000074\) |
| 500 | \(-0.363479\) | \(0.166149\) | \(1.193387\) | \(1.207775\) |

En \(N=500\), la discrepancia máxima entre radios \(0.985\) y
\(0.975\) en los \(\lambda_n\) fue \(5.1\cdot10^{-9}\); la
discrepancia máxima entre autovalores fue \(4.2\cdot10^{-12}\).
No apareció espectro en \([3/4,\infty)\), de modo que la masa de todos
los \(u_n\) allí fue cero.

Esto es evidencia de que el vector fijo no está cerca del umbral en ese
rango. No es evidencia asintótica y no certifica ningún enunciado sobre
todo \(n\): ambos radios comparten la evaluación de Borwein, la FFT y
la aritmética **float64**.

## 7. Gate de Gershgorin y Schur

Con

\[
 a_0=A_M,
 \qquad
 a_k=\Delta A_k\quad(M\le k<N),
\]

los extremos superiores de Gershgorin son

\[
 \begin{aligned}
 G_0
 &={B_M\over A_M}
   +\sum_{k=M}^{N-1}{|s_k|\over\sqrt{A_M\Delta A_k}},\\
 G_k
 &={q_0\over\Delta A_k}
   +{|s_k|\over\sqrt{A_M\Delta A_k}}\\
 &\quad
   +\sum_{\substack{M\le l<N\\l\ne k}}
       {|q_{|k-l|}|\over\sqrt{\Delta A_k\Delta A_l}}.
 \end{aligned}                                                 \tag{31}
\]

**Chequeo de índices de (31).** El índice \(k\) etiqueta la fila
\(\phi_k\), \(M\le k<N\). Su diagonal es
\(q_{|k-k|}/\Delta A_k=q_0/\Delta A_k\); el término \(s_k\) es la
única entrada contra \(g_M\); y la suma sobre \(l\ne k\) contiene
exactamente las restantes filas \(\phi_l\). No hay doble conteo.

Con pesos de Schur \(w_i=\sqrt{a_i}\), la cota se simplifica a

\[
 \begin{aligned}
 S_0
 &={|B_M|+\sum_{k=M}^{N-1}|s_k|\over A_M},\\
 S_k
 &={|s_k|+|q_0|
       +\sum_{\substack{M\le l<N\\l\ne k}}|q_{|k-l|}|
       \over\Delta A_k}.
 \end{aligned}                                                 \tag{32}
\]

Para evitar una ambigüedad de índices, definamos la segunda diferencia
centrada

\[
 \nabla_c^2 B_d:=B_{d+1}-2B_d+B_{d-1}\qquad(d\ge1).
\]

El coeficiente aritmético exacto requerido por (31)--(32) es

\[
 \boxed{
 q_d={1\over2}\nabla_c^2(A-\lambda)_d
 ={1\over2}\nabla_c^2A_d
  -{1\over2}\nabla_c^2\lambda_d.}                              \tag{33}
\]

Por tanto una prueba mediante (31) o (32) necesita una cota firmada o
sumable para las segundas diferencias centradas de \(\lambda_n\), o una
estimación directa de la diferencia prima--polo en (15). Sustituirla por
valores absolutos elimina la interferencia que A1 necesita.

El diagnóstico hace visible la pérdida: Gershgorin ya supera \(3/4\)
entre \(N=350\) y \(N=400\), y Schur lo hace antes, mientras el
autovalor superior observado sigue por debajo de \(0.13\). La cota de
filas no captura la cancelación matricial ni siquiera en el rango de
prueba.

## Estado

* **Probado:** forma regulada cerrada para \(\varepsilon>0\),
  indefinición explícita, matriz Toeplitz (14)--(18), límite algebraico
  (19), referencia positiva de bandera (21)--(24) y matriz blanqueada
  exacta (27)--(30).
* **Verificado diagnósticamente:** todas las identidades hasta \(N=500\),
  estabilidad entre dos radios y ausencia de espectro por encima de
  \(3/4\) en esas secciones.
* **Descartado como estimación directa:** filas absolutas de
  Gershgorin--Schur; pierden el margen antes de \(N=400\).
* **No probado:** control uniforme de \(K_{M,N}\), no alineación
  espectral uniforme de \(u_n\), A1 y RH.
* **Coeficiente mínimo restante:** una estimación no absoluta para
  \(q_d=\frac12\nabla_c^2(A-\lambda)_d\), reteniendo la cancelación
  conjunta de (15), o una estimación directa del primer momento (30)
  sobre la familia fija \(u_n\).
