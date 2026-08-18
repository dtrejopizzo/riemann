# 104_87 — Sección finita de Nyman, inversión de `max` y cola de Möbius

**Resultado.** La identidad de inversión divisora sí da una cancelación
exacta para el residual de Nyman construido con los coeficientes de Möbius:
el residual se anula en todo el intervalo macroscópico \((1/N,1]\). Su
norma completa queda concentrada en \((0,1/N]\), donde admite una serie
positiva exacta. En el primer bloque de esa serie aparece, sin pérdidas, un
incremento centrado de la función de Mertens.

Más precisamente, si

\[
 g_N=\sum_{k\le N}{\mu(k)\over k},\qquad
 b_{k,N}=\mu(k)-Ng_N\mathbf 1_{\{k=N\}},                 \tag{1}
\]

entonces \(\sum_{k\le N}b_{k,N}/k=0\) y el residual

\[
 \mathcal R_N(x)=1+\sum_{k\le N}b_{k,N}
       \left\{{1\over kx}\right\}                       \tag{2}
\]

satisface

\[
 \boxed{\mathcal R_N(x)=0\quad(1/N<x\le1).}             \tag{3}
\]

Poniendo

\[
 R_N(m)=1-\sum_{k\le N}b_{k,N}\left\lfloor{m\over k}\right\rfloor,
                                                                    \tag{4}
\]

se tiene la identidad de norma

\[
 \boxed{
 d_N^2:=\int_0^1|\mathcal R_N(x)|^2\,dx
 =\sum_{m=N}^{\infty}{R_N(m)^2\over m(m+1)}.}           \tag{5}
\]

En particular, si \(M(y)=\sum_{k\le y}\mu(k)\), entonces

\[
 \boxed{R_N(m)=M(m)-M(N)+Ng_N\quad(N\le m<2N)}          \tag{6}
\]

y por tanto

\[
 \boxed{
 d_N^2\ge {1\over4N^2}\sum_{m=N}^{2N-1}
 \{M(m)-M(N)+Ng_N\}^2.}                                \tag{7}
\]

Así, la convergencia de este aproximante explícito exigiría la condición
necesaria

\[
 \sum_{m=N}^{2N-1}\{M(m)-M(N)+Ng_N\}^2=o(N^2),         \tag{8}
\]

es decir, tamaño cuadrático medio \(o(\sqrt N)\) en el primer bloque.
PNT/Vinogradov--Korobov no alcanza esa escala. La inversión tridiagonal del
kernel \(1/\max(m,n)\) no mejora (5): es exactamente la operación que
convierte los coeficientes del Dirichlet residual en las sumas parciales
\(R_N(m)\).

El documento no afirma que (8) sea suficiente, ni que falle para los
Möbius ordinarios. Prueba que la telescopía divisora, por sí sola, no da la
cota superior que cerraría Nyman. Para coeficientes optimizados, demostrar
que el ínfimo de las normas tiende a cero sigue siendo el criterio de
Nyman--Báez-Duarte y, por tanto, RH. No se prueba Deep-\(\Lambda\), A1 ni
RH.

---

## 1. Forma de pisos para un polinomio de Dirichlet

Sea

\[
 A(s)=\sum_{k\le N}{a_k\over k^s},\qquad
 \sum_{k\le N}{a_k\over k}=0.                           \tag{9}
\]

El residual de Hardy--Nyman es

\[
 f_A(s)={1-\zeta(s)A(s)\over s}.                        \tag{10}
\]

La transformada de Mellin de

\[
 \mathcal R_A(x)=1+\sum_{k\le N}a_k
       \left\{{1\over kx}\right\},\qquad 0<x<1,       \tag{11}
\]

es (10). En efecto, para \(\Re s>1\),

\[
 \int_0^1\left\{{1\over kx}\right\}x^{s-1}\,dx
 ={1\over k(s-1)}-{\zeta(s)\over sk^s},                \tag{12}
\]

y el primer término se cancela al sumar por (9). La identidad se prolonga
al espacio de Hardy por continuidad.

Si \(m\le1/x<m+1\), (9) convierte (11) en

\[
 \mathcal R_A(x)=R_A(m),\qquad
 R_A(m):=1-\sum_{k\le N}a_k\left\lfloor{m\over k}\right\rfloor.
                                                                    \tag{13}
\]

Por consiguiente,

\[
 \boxed{
 \|f_A\|_{H^2}^2=\|\mathcal R_A\|_{L^2(0,1)}^2
 =\sum_{m\ge1}{|R_A(m)|^2\over m(m+1)}.}               \tag{14}
\]

La última igualdad usa solamente que
\((1/(m+1),1/m]\) tiene longitud \(1/[m(m+1)]\).

## 2. La elección Möbius y la cancelación del prefijo

La elección (1) satisface la restricción (9). Para \(m<N\), el corrector
en \(k=N\) no contribuye y la inversión de Möbius da

\[
 \sum_{k\le N}b_{k,N}\left\lfloor{m\over k}\right\rfloor
 =\sum_{k\le m}\mu(k)\left\lfloor{m\over k}\right\rfloor
 =1.                                                     \tag{15}
\]

Esto prueba (3). Para \(m\ge N\), (4) se escribe

\[
 R_N(m)=1-\sum_{k\le N}\mu(k)\left\lfloor{m\over k}\right\rfloor
 +Ng_N\left\lfloor{m\over N}\right\rfloor.           \tag{16}
\]

Si \(N\le m<2N\), el último piso vale uno. Al restar de la identidad
completa

\[
 \sum_{k\le m}\mu(k)\left\lfloor{m\over k}\right\rfloor=1,        \tag{17}
\]

los términos con \(N<k\le m\) tienen piso uno. Luego

\[
 R_N(m)=\sum_{N<k\le m}\mu(k)+Ng_N
       =M(m)-M(N)+Ng_N,                                 \tag{18}
\]

que prueba (6). Como \(m(m+1)<4N^2\) en ese bloque, (5) implica (7).

## 3. El kernel `max` y su inversa exacta

Sea \(r=(r_1,\ldots,r_M)^T\), \(S_j=\sum_{m\le j}r_m\), y

\[
 K_M(i,j)={1\over\max(i,j)}.                            \tag{19}
\]

Partiendo \((0,1]\) en intervalos recíprocos se obtiene

\[
 r^TK_Mr
 =\sum_{j=1}^{M-1}{S_j^2\over j(j+1)}+{S_M^2\over M}. \tag{20}
\]

En particular, \(K_M^{-1}\) es tridiagonal:

\[
 (K_M^{-1})_{j,j}=
 \begin{cases}2j^2,&j<M,\\ M^2,&j=M,\end{cases}
 \qquad
 (K_M^{-1})_{j,j+1}=(K_M^{-1})_{j+1,j}=-j(j+1),         \tag{21}
\]

y las demás entradas son cero. La inversión no crea una reserva: (20)
muestra que solo cambia entre los incrementos \(r_j\) y sus primitivas
\(S_j\).

Para el residual de (10), los coeficientes de Dirichlet son

\[
 r_A(m)=\mathbf1_{\{m=1\}}-
        \sum_{\substack{k\le N\\k\mid m}}a_k,         \tag{22}
\]

y su suma parcial es precisamente (13). Así, el límite de (20) es (14).
No queda un término de borde omitido por pasar a la inversa tridiagonal.

## 4. Escala del input que falta

De PNT con región libre de ceros de tipo Vinogradov--Korobov se obtiene,
para alguna constante efectiva \(c>0\),

\[
 M(x),\;xg_x
 \ll x\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}.     \tag{23}
\]

Aplicar (23) término a término en (7) solo produce la escala

\[
 N\exp\{-2c(\log N)^{3/5}(\log\log N)^{-1/5}\},        \tag{24}
\]

que no tiende a cero. Esto no demuestra que el miembro izquierdo de (7)
sea grande: demuestra que el input PNT puntual no certifica (8).

Para coeficientes arbitrarios sujetos a (9), un cero
\(\rho=\beta+i\gamma\), \(\beta>1/2\), impone por evaluación de Hardy

\[
 \|f_A\|_{H^2}^2\ge {2\beta-1\over|\rho|^2}.           \tag{25}
\]

Por tanto una construcción de coeficientes con \(\liminf\|f_A\|=0\)
excluiría todos los ceros derechos y probaría RH. Las ecuaciones
(3)--(8) son una localización exacta de ese problema para el truncado
Möbius; no constituyen tal construcción.
