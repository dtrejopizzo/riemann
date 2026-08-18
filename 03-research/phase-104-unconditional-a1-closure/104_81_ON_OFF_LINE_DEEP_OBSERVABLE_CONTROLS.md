# 104_81 — Controles on/off-line del observable profundo

**Resultado.** El observable profundo de 104_75 no se anula por una
tautología de la normalización. Dos pares de controles exactos lo separan:

\[
\begin{array}{c|c|c}
\text{control}&\text{ubicación de ceros}&
\text{densidad logarítmica profunda}\\ \hline
\text{cuarteto crítico}&|w|=1&0\\
\text{cuarteto exterior}&|w|\ne1&1/8\\
\text{Euler reticular }Z_+&\Re\rho=1/2&0\\
\text{Euler reticular }Z_-&\Re\rho\ne1/2&1/4.
\end{array}
\]

El segundo par conserva pesos de Mangoldt no negativos, torres primas
unitarias, producto de Euler y ecuación funcional. Por tanto el detector
distingue correctamente un modelo on-line de uno off-line aun después de
incorporar la aritmética formal.

Esto **no prueba** que el observable sea cero para los pesos ordinarios
\(\Lambda(m)\). Los modelos Euler son reticulares y no satisfacen el PNT
continuo ni el factor Gamma de la zeta de Riemann. El resultado es un
control adversarial del gate, no una prueba de A1 o RH.

---

## 1. El observable abstracto

Para una sucesión real \(\ell=(\ell_n)\), ponga

\[
 {\cal D}_X(\ell):={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\ell_n+\log(n+1)\le-e^{\sqrt X}\}},
 \qquad H_X=\sum_{n\le X}{1\over n}.                    \tag{1}
\]

Si

\[
 F(z)=\prod_{j=1}^{N}\left(1-{z\over a_j}\right),
\]

entonces, en el disco de convergencia,

\[
 -{F'(z)\over F(z)}
 =\sum_{n\ge1}\left(\sum_{j=1}^{N}a_j^{-n}\right)z^{n-1}.
                                                               \tag{2}
\]

El análogo finito del coeficiente de Li es por tanto

\[
 \ell_n=N-\sum_{j=1}^{N}a_j^{-n}.                       \tag{3}
\]

Esta convención tiene exactamente el signo de 104_80: un polo interior
de \(-F'/F\) aporta \(+a^{-n}\) a (2), y por ello \(-a^{-n}\) a
\(\ell_n\).

## 2. Control crítico: el evento nunca ocurre

Tome el multiconjunto

\[
 \{a_j\}=\{i,-i,i,-i\}.
\]

Todos sus puntos están en el círculo unidad y

\[
 \ell_n^{(0)}
 =4-4\cos\left({\pi n\over2}\right)\in\{0,4,8\}.        \tag{4}
\]

Luego

\[
 \boxed{{\cal D}_X(\ell^{(0)})=0\quad\text{para todo }X.} \tag{5}
\]

No se usa una estimación: el indicador de (1) es idénticamente cero.

## 3. Control exterior: densidad exacta \(1/8\)

Fije

\[
 1<R<e^{1/100},\qquad\text{por ejemplo }R={201\over200},
\]

y tome

\[
 \{a_j\}=\{Ri,-Ri,i/R,-i/R\}.
\]

El cuarteto es estable por conjugación e inversión y

\[
 \ell_n^{(R)}
 =4-2(R^n+R^{-n})\cos\left({\pi n\over2}\right).        \tag{6}
\]

Para \(n\) impar vale \(4\); para \(n\equiv2\pmod4\) es positivo; y para
\(4\mid n\),

\[
 \ell_n^{(R)}=4-2(R^n+R^{-n})
             =-(2+o(1))R^n.                            \tag{7}
\]

El evento de (1) comienza, salvo \(O(1)\) grados, en

\[
 n_X={\sqrt X-\log2\over\log R}+O(1).                   \tag{8}
\]

Como solamente sobrevive una clase módulo \(4\),

\[
\begin{aligned}
 \sum_{\substack{n_X\le n\le X\\4\mid n}}{1\over n}
 &= {1\over4}\log {X\over n_X}+O(1)\\
 &= {1\over8}\log X+O(1).
\end{aligned}                                           \tag{9}
\]

Dividiendo por \(H_X=\log X+O(1)\),

\[
 \boxed{\lim_{X\to\infty}{\cal D}_X(\ell^{(R)})={1\over8}.} \tag{10}
\]

La elección \(R<e^{1/100}\) comprueba además el regulador diagonal de la
fase. Si \(\varepsilon_X=e^{-X/100}\) desplaza cada punto en
\(O(\varepsilon_X)\), la perturbación uniforme de los grados \(n\le X\)
es

\[
 O(X\varepsilon_XR^X)
 =\exp\{-(1/100-\log R)X+O(\log X)\}=o(1).              \tag{11}
\]

Así (10) no es un artefacto de haber quitado el regulador. Un valor como
\(R=2\) sirve para el cuarteto no regulado, pero no para este test
diagonal literal.

## 4. Dos controles con producto de Euler positivo

Los cuartetos prueban el signo y la escala. Para verificar que el
observable tampoco depende de haber omitido toda la estructura Euler,
considere primero

\[
 Z_+(T)={1+4T^2\over(1-T)(1-4T)},\qquad T=4^{-s}.       \tag{12}
\]

Usando los polinomios de collares

\[
 M_d(r)={1\over d}\sum_{e\mid d}\mu(e)r^{d/e},
\]

su número de primos formales de grado \(d\) es

\[
 \pi_d^+=M_d(4)+M_d(1)
 +{\bf1}_{2\mid d}M_{d/2}(4)
 -{\bf1}_{4\mid d}M_{d/4}(16).                         \tag{13}
\]

Es un entero no negativo. Para \(4\nmid d\) es inmediato. Para
\(4\mid d\), la interpretación de \(M_q(16)\) como número de collares
aperiódicos da \(M_q(16)\le16^q/q\); junto con la cota elemental inferior,

\[
 M_d(4)\ge {4^d\over d}-2^d,\qquad
 M_{d/4}(16)\le {4\,2^d\over d}
\]

dan no negatividad para \(d\ge4\), y los grados iniciales se comprueban
directamente. La derivada logarítmica es

\[
 \Psi_k^+=4^k+1-(2i)^k-(-2i)^k,                        \tag{14}
\]

y

\[
 Z_+(1/(4T))=Z_+(T).                                    \tag{15}
\]

La función completada correspondiente puede tomarse como

\[
 \Xi_+(s)=4^s+4^{1-s}.                                  \tag{16}
\]

Todos sus ceros satisfacen

\[
 \Re\rho={1\over2},\qquad
 \Im\rho={ (2j+1)\pi\over2\log4}.
\]

El producto canónico par de
\(\cosh((s-\tfrac12)\log4)\) no deja factor exponencial. Al emparejar
conjugados, cada sumando de Li es
\(2(1-\cos(n\theta_j))=|1-e^{in\theta_j}|^2\ge0\).
Además los ceros hasta altura \(n\) son \(O(n)\), y la cola se acota por
\(O(n^2\sum_{j>n}j^{-2})=O(n)\). Por tanto sus coeficientes son
no negativos y \(O(n)\); en particular el evento profundo nunca ocurre:

\[
 \boxed{{\cal D}_X(\lambda^+)=0\quad\text{para todo }X.} \tag{17}
\]

El control off-line es el falsificador completamente probado en 104_78:

\[
 Z_-(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},\qquad T=6^{-s}, \tag{18}
\]

\[
 \pi_d^-=M_d(6)+M_d(1)-M_d(3)-M_d(2)\ge0,\qquad
 \Psi_k^-=6^k+1-3^k-2^k,                               \tag{19}
\]

\[
 Z_-(1/(6T))=Z_-(T).                                    \tag{20}
\]

Su completamiento

\[
 \Xi_-(s)=6^s-5+6^{1-s}
\]

tiene ceros con partes reales \(\log_6 2\) y \(\log_6 3\). La singularidad
dominante produce

\[
 \lambda_n^-=-(1+o(1))
 \left({\log3\over\log2}\right)^n
 \quad(n\ \text{par}),
\]

y 104_78, incluyendo el regulador diagonal, prueba

\[
 \boxed{\lim_{X\to\infty}{\cal D}_X(\lambda^-)={1\over4}.} \tag{21}
\]

## 5. Veredicto

Los controles prueban tres hechos distintos:

1. el observable es exactamente inocuo en el control crítico;
2. un cuarteto off-line genera la cola profunda con densidad positiva y
   el signo previsto por la identidad de 104_80;
3. la misma separación sobrevive en dos sistemas con producto de Euler,
   pesos de Mangoldt positivos y ecuación funcional.

Por tanto queda **falsificada** la posibilidad de que el límite sea cero
por una normalización, un error de signo o una propiedad Euleriana
universal. También queda **validado** el observable como detector.

Lo que permanece abierto es específico: demostrar (17) para la zeta real,
es decir, para la ubicación ordinaria de los pesos \(\Lambda(m)\), su
factor Gamma y su PNT continuo. Hacerlo excluiría los polos interiores de
104_80 y demostraría RH; ninguno de los controles anteriores suministra
esa exclusión.

## Reproducción

Ejecutar desde el directorio tools:

    python3 on_off_line_deep_observable_check.py
