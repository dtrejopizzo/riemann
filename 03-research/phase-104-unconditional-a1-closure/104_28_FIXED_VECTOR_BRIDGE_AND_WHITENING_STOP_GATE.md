# 104_28 — Puente de vector fijo y stop-gate del blanqueo arquimediano

**Rol.** Auditar la propuesta de probar el margen proporcional mediante no
alineación del test de Laguerre con el subespacio casi extremal del operador
primo blanqueado. El puente de vector fijo existe y es exacto: el test de Li es
el prefijo de Dirichlet en la base ortonormal de Laguerre del borde. Lo que no
existe en el registro es un puente simultáneo que identifique, en ese mismo
borde, una métrica arquimediana positiva cuya evaluación sea \(A_n\). Por ello
el solapamiento con el autovector superior de las fases 62--69 no es hoy una
cantidad fiel a A1.

Este documento no prueba A1 ni RH. Prueba qué parte de la propuesta es exacta,
qué parte duplica 103_24--103_26, y cuál es la obligación matemática nueva
que habría que satisfacer antes de ejecutar un diagnóstico espectral.

## 1. El puente exacto al prefijo de Dirichlet

Sean

\[
 f_n(x)={\bf1}_{[0,\infty)}(x)L_{n-1}^{(1)}(x),
 \qquad g_n(x)=e^{-x/2}f_n(x),
\]

y

\[
 \phi_k(x)={\bf1}_{[0,\infty)}(x)e^{-x/2}L_k(x).
\]

La ortogonalidad ordinaria de Laguerre da

\[
 \langle\phi_j,\phi_k\rangle_{L^2(0,\infty)}=\delta_{jk}.
\]

La identidad de suma

\[
 \boxed{L_{n-1}^{(1)}(x)=\sum_{k=0}^{n-1}L_k(x)}                 \tag{1}
\]

produce

\[
 \boxed{g_n=\sum_{k=0}^{n-1}\phi_k,
 \qquad [g_n]_{\{\phi_k\}}={\bf1}_n,
 \qquad \|g_n\|_2^2=n.}                                        \tag{2}
\]

Así, el test no es un vector desconocido: es exactamente el prefijo
\((1,\ldots,1)\). La base (2) es la base Laguerre de parámetro
\(y=1/2,t_0=0\); bajo \(s=1/2+iz\), corresponde al punto de borde \(s=1\).
Además, como \(L_k(0)=1\),

\[
 L_{n-1}^{(1)}(x)=K_{n-1}^{\rm Lag}(x,0),
\]

de modo que \(g_n/\sqrt n\) es el estado normalizado del kernel reproductor
en el borde duro \(x=0\), no un vector genérico.

En la base monomial del jet puede escribirse el mismo vector como

\[
 \phi_j^{\rm mon}(x)={(-ix)^j\over j!}e^{-x/2},
 \qquad c_j^{(n)}=i^j{n\choose j+1}\quad(0\le j<n),              \tag{2a}
\]

con la convención \(F_c=\sum_j\overline{c_j}\phi_j^{\rm mon}\). Entonces
\(F_{c^{(n)}}=g_n\).

Por 103_69, si \(h_n=f_n*f_n^\#\), entonces

\[
 \mathcal Lh_n(s)
 =\left(1-\left({s-1\over s}\right)^n\right)
  \left(1-\left({s\over s-1}\right)^n\right),
 \qquad
 \boxed{\mathcal W_\zeta(h_n)=2\lambda_n.}                     \tag{3}
\]

Las ecuaciones (1)--(3) son el puente completo para la **forma total** de
Weil.

Hay una simplificación adicional. Puesto que

\[
 F_n(s)F_n(1-s)=F_n(s)+F_n(1-s),
\]

la unicidad de la transformada da

\[
 \boxed{f_n*f_n^\#=f_n+f_n^\#,
 \qquad (g_n*\widetilde g_n)(a)=g_n(|a|).}                     \tag{3a}
\]

Por tanto, para el semigrupo de traslación \(S_a\),

\[
 \boxed{\langle S_ag_n,g_n\rangle
 =e^{-a/2}L_{n-1}^{(1)}(a).}                                  \tag{3b}
\]

## 2. Polarización Toeplitz exacta del dato escalar

Para cualquier sucesión real \(q_0=0,q_1,q_2,\ldots\), defínase

\[
 t_0(q)=q_1,
 \qquad
 t_m(q)={q_{m+1}-2q_m+q_{m-1}\over2}\quad(m\ge1),               \tag{4}
\]

y \(T_N(q)=[t_{|j-k|}(q)]_{0\le j,k<N}\). Dos sumaciones por
partes dan, sin hipótesis de signo,

\[
 \boxed{{\bf1}_n^*T_n(q){\bf1}_n=q_n.}                          \tag{5}
\]

En particular, tomando \(q=2\lambda-A\), (5) es precisamente la forma
Fejér de 103_24--103_26. Para el margen actual puede tomarse
\(q=r_*\lambda-A\). Por tanto la observación «A1 sólo necesita un vector
fijo» es correcta, pero su polarización Toeplitz natural ya estaba
registrada: el vector fijo es \({\bf1}_n\).

La identidad (3b) también recompone exactamente el lado primo. Para
\(\varepsilon>0\), la expresión

\[
 \mathfrak p_{\Lambda,\varepsilon}[g_n]
 :=\sum_{m\ge2}{\Lambda(m)\over m^{1/2+\varepsilon}}
 \langle(S_{\log m}+S_{\log m}^*)g_n,g_n\rangle                \tag{6a}
\]

es una **forma sobre el rayo \(g_n\)** y satisface

\[
 {1\over2}\mathfrak p_{\Lambda,\varepsilon}[g_n]
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).                                        \tag{6b}
\]

No debe llamarse operador acotado obtenido por suma en norma: el solapamiento
de \(g_n\) aporta el segundo factor \(m^{-1/2}\), indispensable para la
convergencia. Si

\[
 p_n(\varepsilon)
 =n\sum_{k=1}^n{n-1\choose k-1}{(-1)^{k-1}\over k\varepsilon^k},
\]

la fórmula prima--Laguerre da

\[
 A_n-\lambda_n
 =\lim_{\varepsilon\downarrow0}
 \left[{1\over2}\mathfrak p_{\Lambda,\varepsilon}[g_n]
       -p_n(\varepsilon)\right].                               \tag{6c}
\]

Así, la versión rigurosa del cociente propuesto es la cota de **un solo
rayo renormalizado**

\[
 \lambda_n\ge cA_n
 \iff
 \lim_{\varepsilon\downarrow0}
 \left[{1\over2}\mathfrak p_{\Lambda,\varepsilon}[g_n]
       -p_n(\varepsilon)\right]\le(1-c)A_n.                    \tag{6d}
\]

Ésta es exactamente la fórmula prima--Laguerre ya conocida, ahora expresada
como coeficiente diagonal del kernel reproductor en el borde duro. No hay
todavía un operador renormalizado cerrado alrededor de esa forma.

## 3. Por qué no hay un cociente de Rayleigh arquimediano

La condición

\[
 \lambda_n\ge cA_n                                              \tag{7}
\]

es un cociente de dos **números** sobre el vector (2). Para convertirla en
un cociente de Rayleigh y hablar de proyectores espectrales hace falta una
forma positiva \(\mathsf A\) y un operador autoadjunto \(\mathsf P\) tales
que, con la misma normalización y uniformemente en \(n\),

\[
 \langle g_n,\mathsf A g_n\rangle=A_n,
 \qquad
 \langle g_n,\mathsf P g_n\rangle=A_n-\lambda_n.                \tag{8}
\]

Las formas existentes no cumplen simultáneamente (8):

1. El operador de las fases 62--69 está definido en un gauge interior
   \(y>1/2\), usualmente a gran \(t_0\), y usa una separación
   arquimediano/primos distinta. El vector (2) vive exactamente en
   \(y=1/2,t_0=0\), donde el polo de \(\zeta\) exige cancelación Abel antes
   de separar los canales.
2. La proposición de elementos Laguerre del ledger para el gauge interior
   es una diagonalización del término principal de Szegő con un resto
   efectivo; no es una isometría exacta que transporte (7) al borde.
3. La polarización Toeplitz natural de \(A_n\) no es positiva. Su diagonal
   es

   \[
    t_0(A)=A_1=1-\frac12(\gamma+\log4\pi)<0,                    \tag{9}
   \]

   pues \(\gamma>0\) y \(\log(4\pi)>2\). Así \(T_N(A)\) no admite
   \(T_N(A)^{-1/2}\), aunque el escalar
   \({\bf1}_n^*T_n(A){\bf1}_n=A_n\) sea positivo para \(n\ge8\).
4. Blanquear con el Gram de referencia \(G_N>0\) sí es posible, pero entonces
   \(\langle g_n,G_Ng_n\rangle=n\), no \(A_n\asymp(n/2)\log n\).
   Ese cociente mide \(2\lambda_n/n\), cuyo umbral correspondiente a (7)
   crece como \(c\log n\); no es una capa espectral fija próxima a \(1\).

La negatividad (9) es la versión mínima del stop-gate de borde de
103_25: positividad sobre los prefijos no se extiende a positividad de la
polarización, y los prefijos generan todo el espacio de polinomios.

## 4. El diagnóstico de solapamiento que no es lícito ejecutar

No es fiel calcular

\[
 {|\langle g_n,v_{\max}(S\mathcal P_\Lambda S)\rangle|
  \over\|g_n\|}
\]

con el operador interior de las fases 62--69 y leerlo como información
sobre \(\lambda_n/A_n\): ni \(g_n\), ni \(S\), ni el split de (8) han sido
transportados exactamente al mismo gauge.

Incluso después de construir tal transporte, proyectar sólo sobre
\([1-\delta,1]\) sería insuficiente sin un techo espectral previo. Un cero
off-line puede crear espectro por encima de \(1\); ignorar
\((1,\infty)\) eliminaría precisamente el falsificador. El proyector mínimo
que una prueba debería controlar es

\[
 P_{[1-\delta,\infty)},                                         \tag{10}
\]

con su peso espectral, y debe reproducir para un cuarteto off-line el
término

\[
 8-8\cosh(n\alpha)\cos(n\theta).                               \tag{11}
\]

## 5. Sucesor vivo

La no-alineación puede reabrirse sólo después de probar un **teorema de
transferencia al borde**:

* construir para \(\varepsilon>0\) una polarización positiva
  \(\mathsf A_\varepsilon\), el operador aritmético acoplado y el vector
  \(g_{n,\varepsilon}\);
* demostrar que sus dos formas convergen, conjuntamente y con constantes
  uniformes en \(n\), a los dos escalares de (8);
* controlar la masa espectral de \(g_{n,\varepsilon}\) en
  \([1-\delta,\infty)\), no sólo un autovector;
* hacer fallar la estimación para el falsificador (11).

Sin ese teorema, la «no-alineación» no es todavía un mecanismo: es una
reinterpretación espectral de la cota proporcional buscada.

La afirmación heurística de que el cociente primo/arquimediano del vector
real es \(O(n^{-1/2})\) sólo está justificada bajo RH (por la asintótica
condicional de los coeficientes de Li). No puede usarse como input
incondicional para validar el mecanismo.

## Estado

* **Probado:** puente exacto \(g_n\leftrightarrow{\bf1}_n\), identidades
  (3a)--(3b), forma prima-polo renormalizada (6c), identidad Toeplitz (5),
  y stop-gate (9) contra el blanqueo arquimediano natural.
* **Duplicación identificada:** el vector fijo es la forma
  Dirichlet--Fejér ya auditada en 103_24--103_26.
* **No ejecutado deliberadamente:** solapamientos con el operador interior;
  no representan \(\lambda_n/A_n\).
* **Abierto:** una polarización regulada positiva con transferencia uniforme
  al borde, o una cota escalar directa sobre el rayo \(g_n\).

