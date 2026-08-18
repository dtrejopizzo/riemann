# 104_111 — Reducción exacta de Deep al factor de Blaschke

**Resultado.** La auditoría adversarial de 104_75 y 104_76 no encuentra
un fallo que debilite el criterio profundo. La factorización canónica en el
disco identifica exactamente qué mide:

\[
 \boxed{\lambda_n=C_n-Z_n,\qquad C_n=O(n^2\log(n+1)),}   \tag{1}
\]

donde \(Z_n\) es el coeficiente del factor interior formado por los ceros
de \(\zeta\) con parte real mayor que \(1/2\). Para
\(S_X=e^{\sqrt X}\), el observable de 104_75 queda atrapado entre los
eventos \(Z_n\ge(1+o(1))S_X\). Toda la cola profunda está en el factor
interior; los factores arquimediano y exterior tienen tamaño polinómico.

Así,

\[
 \boxed{\Omega_X\longrightarrow0
 \quad\Longleftrightarrow\quad B\equiv1
 \quad\Longleftrightarrow\quad \mathrm{RH}.}            \tag{2}
\]

La igualdad (2) no prueba que \(B\equiv1\). Prueba que el umbral
\(e^{\sqrt X}\), la densidad logarítmica y el regulador diagonal no
eliminan ni amortiguan el contenido RH: aíslan exactamente el factor
interior. El control del módulo en el horodisco Euler y las cotas de
crecimiento theta controlan el factor exterior, pero no anulan \(B\).

Este documento corrige además la justificación expositiva del lift duro en
104_75: un error \(o(1)\) no transporta automáticamente indicadores; las
inclusiones (22b) de ese documento sí lo hacen.

---

## 1. Coordenada de disco y generatriz de Li

Ponga

\[
 F(s)=(s-1)\zeta(s),\qquad
 s=s(z)={1\over1-z},\qquad
 E(z)=F(s(z)).                                           \tag{3}
\]

El disco unidad se transforma en \(\Re s>1/2\), \(z=0\) corresponde a
\(s=1\), y \(E(0)=1\). La completada satisface

\[
 {\xi(s(z))\over\xi(1)}
 =s(z)\pi^{-s(z)/2}\Gamma(s(z)/2)E(z).                  \tag{4}
\]

Con la rama normalizada en cero,

\[
 \log{\xi(s(z))\over\xi(1)}
 =\sum_{n\ge1}{\lambda_n\over n}z^n.                   \tag{5}
\]

Los ceros interiores de \(E\) son

\[
 a_\rho={\rho-1\over\rho},\qquad \Re\rho>{1\over2},
 \qquad |a_\rho|<1.                                    \tag{6}
\]

## 2. Factorización canónica

Fije un entero \(M\) mayor que un exponente de crecimiento polinómico
uniforme de \(F(s)\) en \(\Re s>1/2\). Entonces

\[
 g(z)=(1-z)^M E(z)\in H^\infty(\mathbb D).               \tag{6a}
\]

Como \((1-z)^M\) es exterior, \(E=g/(1-z)^M\) pertenece a la clase de
Smirnov \(N^+\). Su factorización canónica tiene inicialmente la forma

\[
 E(z)=B(z)S(z)O(z).                                      \tag{6b}
\]

La función \(E\) continúa holomórficamente a través de todo arco de
\(\partial\mathbb D\) que no contenga \(1\). Por tanto la medida del factor
interior singular \(S\), si existe, está soportada en \(\{1\}\), y

\[
 S(z)=S_c(z):=\exp\!\left\{-c{1+z\over1-z}\right\},
 \qquad c\ge0.                                          \tag{6c}
\]

La pertenencia a \(N^+\) da
\[
 u(\theta):=\log|E^*(e^{i\theta})|\in L^1(d\theta),
\]
y el factor exterior satisface
\[
 \log|O(r)|=P_r*u=o((1-r)^{-1})\qquad(r\uparrow1).       \tag{6d}
\]
En efecto, \(P_r(\theta)(1-r)\to0\) para casi todo \(\theta\), está
uniformemente acotado por \(2\), y se aplica convergencia dominada a
\(|u|\).

Sobre el radio real, \(s=(1-r)^{-1}\to\infty\) y
\[
 E(r)=(s-1)\zeta(s)\sim s-1,
 \qquad \log|E(r)|=o(s).                                 \tag{6e}
\]
Pero \(\log|B(r)|\le0\),
\(\log|S_c(r)|=-c(1+r)/(1-r)=-2cs+O(1)\), y (6d) es
\(o(s)\). Si \(c>0\), (6b) implicaría
\(\limsup s^{-1}\log|E(r)|\le-2c\), contradiciendo (6e).
Luego \(c=0\): no hay factor interior singular. La factorización es

\[
 E(z)=B(z)O(z),                                         \tag{7}
\]

con \(B\) el producto de Blaschke de los ceros (6), contando
multiplicidades, y \(O\) exterior. Para

\[
 b_a(z)={|a|\over a}{a-z\over1-\bar a z},
 \qquad b_a(0)=|a|,                                     \tag{8}
\]

se tiene, localmente en cero,

\[
 \log{b_a(z)\over b_a(0)}
 =-\sum_{n\ge1}{a^{-n}-\bar a^{\,n}\over n}z^n.         \tag{9}
\]

La condición de Blaschke garantiza la convergencia de los coeficientes
agrupados por conjugación: para \(n\) fijo y \(a=re^{i\theta}\),
\[
 |a^{-n}-\bar a^{\,n}|=r^{-n}-r^n\ll_n1-r.
\]
Defina

\[
 Z_n=\sum_{\Re\rho>1/2}m_\rho
       \left(a_\rho^{-n}-\bar a_\rho^{\,n}\right).      \tag{10}
\]

La suma es real después de agrupar ceros conjugados. De (4)--(10),

\[
 \lambda_n=C_n-Z_n,                                    \tag{11}
\]

donde

\[
 C_n=n[z^n]\left\{
 \log\big(s\pi^{-s/2}\Gamma(s/2)\big)
 +\log{O(z)\over O(0)}\right\}.                        \tag{12}
\]

## 3. El bloque no interior es polinómico

La prueba de \(N^+\) en §2 ya da, sobre el círculo,

\[
 u(\theta)=\log|E(e^{i\theta})|.                        \tag{13}
\]

Para el factor exterior,

\[
 n[z^n]\log{O(z)\over O(0)}=2n\widehat u(n)=O(n).       \tag{14}
\]

El factor arquimediano es analítico en el disco. Sobre
\(|z|=1-1/n\), se tiene \(|s(z)|\le n\); Stirling uniforme en
\(\Re s>1/2\) da

\[
 \left|\log\big(s\pi^{-s/2}\Gamma(s/2)\big)\right|
 =O(n\log(n+1)).                                        \tag{15}
\]

Cauchy en ese círculo, para el cual
\((1-1/n)^{-n}=O(1)\), prueba

\[
 \boxed{C_n=O(n^2\log(n+1)).}                           \tag{16}
\]

No se usó RH ni ausencia de ceros en el borde.

## 4. Sandwich exacto del observable profundo

Sea

\[
 S_X=e^{\sqrt X},\qquad
 \delta_X=\sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|=o(1),
 \qquad \varepsilon_X=e^{-X/100}.                       \tag{17}
\]

Ponga

\[
 \eta_X={\max_{n\le X}|C_n+\log(n+1)|+\delta_X\over S_X}.
                                                                    \tag{18}
\]

Por (16), \(\eta_X\to0\). La identidad

\[
 \lambda_{n,\varepsilon_X}+\log(n+1)
 =C_n-Z_n+\log(n+1)
  +(\lambda_{n,\varepsilon_X}-\lambda_n)                \tag{19}
\]

da, término a término,

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{\mathbf1_{\{Z_n\ge(1+\eta_X)S_X\}}\over n}
 \le\Omega_X\le
 {1\over H_X}\sum_{n\le X}{\mathbf1_{\{Z_n\ge(1-\eta_X)S_X\}}\over n}.}
                                                                    \tag{20}
\]

Ésta es una reducción del observable, no una estimación.

## 5. Por qué (20) conserva exactamente RH

Si \(B\equiv1\), entonces \(Z_n=0\). Por (16), el evento profundo es
vacío para todo \(n\le X\) cuando \(X\) es grande, y \(\Omega_X=0\).

Suponga \(B\not\equiv1\). Como \(|a_\rho|\to1\) cuando
\(|\Im\rho|\to\infty\), existe

\[
 r=\min_\rho|a_\rho|<1,\qquad R=r^{-1}>1,              \tag{21}
\]

y solo finitos ceros alcanzan \(r\). Elija \(q\in(r,1)\) menor que el
módulo de cualquier otro cero interior. La expansión meromorfa de la
derivada de (5), o directamente (9), da

\[
 Z_n=R^nF(n\phi)+O(R_1^n),\qquad1<R_1<R,                \tag{22}
\]

donde \(F\) es una suma finita de cosenos con coeficientes positivos y
\(F(0)>0\). En el grupo compacto

\[
 H=\overline{\{n\phi:n\in\mathbb Z\}},                  \tag{23}
\]

los retornos a un abierto \(\{F>\eta\}\),
\(0<\eta<F(0)\), forman un conjunto sindético \(D\) de densidad natural
\(d>0\). Sobre \(D\), eventualmente,

\[
 Z_n\ge{\eta\over2}R^n.                                 \tag{24}
\]

Si \(K>1/\log R\), (24) supera \((1+\eta_X)S_X\) para
\(n\in D\cap[K\sqrt X,X]\). La sumación parcial da

\[
 {1\over H_X}\sum_{\substack{K\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                           \tag{25}
\]

Por (20), \(\liminf\Omega_X\ge d/2\). Así (2) queda probada.

## 6. El punto exacto que no cierra

El factor interior es invisible para el módulo en la frontera:

\[
 |B(e^{i\theta})|=1\quad\hbox{casi en todas partes}.     \tag{26}
\]

En la coordenada del semiplano, el factor de un cero exterior es

\[
 b_\rho(s)={s-\rho\over s-(1-\bar\rho)},                \tag{27}
\]

y satisface

\[
 \inf_{\Re s\ge1}|b_\rho(s)|={1-\beta\over\beta}>0,
 \qquad \rho=\beta+i\gamma.                              \tag{28}
\]

Por tanto los lower bounds disponibles del producto Euler en
\(\Re s\ge1\) son compatibles con un factor interior no trivial. Para
forzar \(B\equiv1\) haría falta controlar \(1/B\) en todo el disco o
probar que \(|B|=1\) en un punto interior; cualquiera de las dos
afirmaciones excluye ya sus ceros.

La cantidad escalar correspondiente es precisamente el defecto BSY de
104_89:

\[
 -\log|B(0)|
 =\sum_{\Re\rho>1/2}m_\rho\log{1\over|a_\rho|}
 =\int_{\mathbb R}\log|F(1/2+it)|
   {dt\over2\pi(t^2+1/4)}.                              \tag{29}
\]

Probar que (29) vale cero, o probar el límite de (20), son dos formas de
anular el mismo factor interior. Las identidades de Hardy, los filtros de
raíces de unidad, los promedios lineales y los módulos de borde controlan
el factor exterior; no proporcionan una desigualdad que anule \(B\).

## 7. Veredicto

* **Auditado:** la equivalencia Deep de 104_75, la diagonal regulada y
  la localización de 104_76 sobreviven.
* **Corregido:** el lift de un indicador duro usa inclusiones de eventos,
  no solamente la frase «\(o(1)\) frente al umbral».
* **Probado:** toda excursión profunda está en el factor de Blaschke, con
  error \(O(n^2\log n)\), y (20) es exacta.
* **No probado:** \(B\equiv1\), el límite Deep, A1 o RH.

La forma corta del obstáculo restante es

\[
 \boxed{\text{demostrar incondicionalmente que }
 (s-1)\zeta(s)\text{ es exterior en }\Re s>{1\over2}.}
\]

Esto es exactamente RH, no una consecuencia ya obtenida de los pesos
literales de Mangoldt.
