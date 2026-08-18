# 104_16 — Cociclo de Jordan: jerarquía positiva y pérdida exacta del signo

**Estado.** El cociclo

\[
 A_u(s):={\zeta(s-u)\over\zeta(s)}
 =\sum_{m\ge1}{J_u(m)\over m^s}
\]

extiende la identidad de conexión de E70.11 y la identidad de Riccati de
E70.12 a una jerarquía completa de funciones aritméticas no negativas
\(\mu*\log^k\). Éste es un hecho exacto y útil. Sin embargo, al mantener
acoplado el polo, la jerarquía positiva se convierte en una **diferencia** de
dos jerarquías positivas. Su primer jet es exactamente el funcional regulado
\(C_{n,\varepsilon}\) de `104_12`, y sus coeficientes de Cayley ya tienen ambos
signos en \(n=1,6\), con certificado racional.

Por tanto muere la implicación propuesta

\[
 \text{positividad Jordan en el semiplano real}
 \quad\Longrightarrow\quad
 \text{signo/convexidad de los coeficientes Cayley--Laguerre}.
\]

Además, la región donde la serie de Dirichlet conserva esa positividad se
contrae antes del límite crítico \(\varepsilon\downarrow0\). Prolongar el
cociclo como una función holomorfa o contractiva en todo el disco de Cayley
reintroduce exactamente la localización de los ceros. No se prueba A1 ni RH.

## 1. Auditoría interna de no duplicación

Una búsqueda literal en las fases 1--104 de

```text
zeta(s-u)/zeta(s),  ζ(s-u)/ζ(s),  J_u,  Jordan totient
```

no da ocurrencias. Sí existen los dos primeros jets y su representación:

* E70.11 prueba \(\mu*\log=\Lambda\) y
  \(Z^{-1}\delta Z=V_\Lambda\);
* E70.12 prueba
  \(\mu*\log^2=\Lambda\log+\Lambda*\Lambda\);
* E83.004 realiza el primer jet por shifts truncados;
* `104_12` obtiene su pullback Laguerre y la convolución en el grado.

Así, el cociclo completo no estaba escrito en el repositorio, pero sus jets
\(k=1,2\) y el obstáculo Euler--Gamma ya estaban identificados. La función
\(J_k(n)=n^k\prod_{p\mid n}(1-p^{-k})\) es el totiente clásico de Jordan; por
ejemplo, Moree--Saad Eddin--Sedunova--Suzuki, *Jordan totient quotients*,
[arXiv:1810.04742](https://arxiv.org/abs/1810.04742), usa esa definición. No
se reclama novedad bibliográfica para (1)--(4). La afirmación de no
duplicación es solamente interna y se refiere a la combinación cociclo
continuo--emparejamiento polar--pullback Laguerre.

## 2. Teorema de la jerarquía positiva

Para \(u\ge0\) y \(\Re s>1+u\), la inversión de Möbius da

\[
 \boxed{
 A_u(s)={\zeta(s-u)\over\zeta(s)}
 =\sum_{m\ge1}{J_u(m)\over m^s},\qquad
 J_u(m)=\sum_{d\mid m}\mu(d)(m/d)^u.}
 \tag{1}
\]

Si \(m=\prod_{p^a\parallel m}p^a\), entonces

\[
 J_u(m)=m^u\prod_{p\mid m}(1-p^{-u})
 =\prod_{p^a\parallel m}
   \left(e^{a u\log p}-e^{(a-1)u\log p}\right)\ge0.
 \tag{2}
\]

Más aún, cada factor de (2) tiene serie de Taylor con coeficientes no
negativos, pues su coeficiente de orden \(r\) es

\[
 { (a\log p)^r-((a-1)\log p)^r\over r!}\ge0.
 \tag{3}
\]

Por multiplicación de series se obtiene, para todo \(k\ge0\),

\[
 \boxed{
 j_k(m):=\left.\partial_u^kJ_u(m)\right|_{u=0}
 =\sum_{d\mid m}\mu(d)\log^k(m/d)
 =(\mu*\log^k)(m)\ge0.}
 \tag{4}
\]

Para \(m>1\), el valor es cero si \(k<\omega(m)\) y estrictamente positivo si
\(k\ge\omega(m)\). En la región de convergencia absoluta,

\[
 D_k(s):=\left.\partial_u^kA_u(s)\right|_{u=0}
 ={(-1)^k\zeta^{(k)}(s)\over\zeta(s)}
 =\sum_{m\ge1}{j_k(m)\over m^s}\ge0.
 \tag{5}
\]

El cociclo satisface también la ley exacta

\[
 A_{u+v}(s)=A_u(s)A_v(s-u).
 \tag{6}
\]

Las ecuaciones (4)--(5) contienen E70.11 en \(k=1\) y E70.12 en \(k=2\),
pero ahora para todos los órdenes.

## 3. El polo emparejado convierte positividad en una diferencia

El modelo polar con la misma traslación es

\[
 A_u^0(s):={s-1\over s-u-1}.
 \tag{7}
\]

Poniendo \(F(s)=(s-1)\zeta(s)\), el cociente emparejado es

\[
 \boxed{
 H_u(s):={A_u(s)\over A_u^0(s)}
 ={F(s-u)\over F(s)}.}
 \tag{8}
\]

Ésta es la normalización que no separa dos cantidades divergentes en
\(s=1\). Como

\[
 H_u(s)=\left(1-{u\over s-1}\right)A_u(s),
\]

sus jets son

\[
 \boxed{
 Q_k(s):=\left.\partial_u^kH_u(s)\right|_{u=0}
 =D_k(s)-{k\over s-1}D_{k-1}(s)
 ={(-1)^kF^{(k)}(s)\over F(s)}.}
 \tag{9}
\]

Por tanto (4) no da un signo para el objeto emparejado: (9) resta dos series
positivas del mismo orden crítico.

La pérdida se ve incluso en el punto regular \(s=1\). Con la convención

\[
 \zeta(1+t)={1\over t}+\sum_{r\ge0}{(-1)^r\gamma_r\over r!}t^r,
\]

se tiene

\[
 \boxed{Q_k(1)=-k\gamma_{k-1}.}
 \tag{10}
\]

Los primeros cuatro signos certificados son

\[
 Q_1(1)<0,\qquad Q_2(1)>0,\qquad Q_3(1)>0,\qquad Q_4(1)<0.
 \tag{11}
\]

En particular, el cociente polo--Euler no es completamente monótono ni
absolutamente monótono en la variable de traslación en el borde crítico. La
positividad de todos los \(j_k(m)\) fue consumida por la colisión con el polo.

## 4. Pullback Cayley--Laguerre exacto

Fijemos \(\varepsilon>0\) y

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z}.
 \tag{12}
\]

Para \(0\le u<\varepsilon\) y \(z\) suficientemente pequeño, la fórmula
generatriz de Laguerre da

\[
 {A_u(s_\varepsilon(z))\over1-z}
 =\sum_{n\ge0}\left{
   \sum_{m\ge1}{J_u(m)\over m^{1+\varepsilon}}
          L_n(\log m)\right}z^n.
 \tag{13}
\]

Para el polo,

\[
 {A_u^0(s_\varepsilon(z))\over1-z}
 ={1\over1-z}+{u\over1-z}{1\over\varepsilon-u+z/(1-z)},
 \tag{14}
\]

y por

\[
 \int_0^\infty e^{-q x}L_n(x)\,dx
 ={(q-1)^n\over q^{n+1}},
\]

su coeficiente de grado \(n\) es

\[
 1+u{(\varepsilon-u-1)^n\over(\varepsilon-u)^{n+1}}.
 \tag{15}
\]

Derivando (13)--(15) en \(u=0\), y usando que
\(A_0=A_0^0=H_0=1\), se obtiene

\[
 \boxed{
 {1\over1-z}\left.\partial_uH_u(s_\varepsilon(z))\right|_{u=0}
 =\sum_{n\ge0}C_{n,\varepsilon}z^n,}
 \tag{16}
\]

donde

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}L_n(\log m)
 -{(\varepsilon-1)^n\over\varepsilon^{n+1}}.}
 \tag{17}
\]

Éste es exactamente el costo regulado de `104_12`, ecuación (8). El cociclo
completo no reemplaza el gate: su primer jet **es** el gate.

## 5. Stop-gate racional en grados 1 y 6

El límite emparejado de (17) existe y `103_59` prueba

\[
 C_n:=\lim_{\varepsilon\downarrow0}C_{n,\varepsilon}
 =\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime}.
 \tag{18}
\]

El verificador `tools/jordan_cocycle_sign_gate.py`, reutilizando los intervalos
racionales de Phase 102, certifica

\[
\begin{aligned}
 C_1&\in[-0.389669432061167636009309,
          -0.389669432061167636009308],\\
 C_6&\in[\phantom{-}0.008107486973374973910460,
          \phantom{-}0.008107486973374973910461].
\end{aligned}
\tag{19}
\]

Luego el primer jet de Cayley tiene ambos signos. Esto refuta exactamente
cualquiera de las inferencias

\[
 H_u(s)\le1\text{ en un rayo real}
 \Longrightarrow [z^n](1-z)^{-1}\partial_uH_u|_0\le0,
\]

o la misma flecha con el signo opuesto. El orden puntual en \(s\) y el orden
coeficiente a coeficiente después de Cayley son órdenes distintos. La
oscilación no aparece recién en una cota asintótica: ya está certificada en
los grados \(1\) y \(6\).

La desigualdad que M6 necesitaría sigue siendo

\[
 C_n\le{1\over2}\Delta A_n,
 \tag{20}
\]

equivalente al gate fuerte \(\Delta D_n\ge0\) de `103_59`. Ni (4), ni una
desigualdad real para (8), ni una convexidad en \(u\) implican (20) después de
la extracción firmada (16).

## 6. Falsificador estructural con jerarquía Jordan completa

La pérdida de signo no es una peculiaridad numérica de los primeros grados.
Para \(a>0\), considérese

\[
 X_a(s)=\xi(s+a)\xi(s-a).
 \tag{21}
\]

Es una función entera real y satisface

\[
 X_a(1-s)=X_a(s).
 \tag{22}
\]

Todo cero conocido \(\frac12+i\gamma\) de \(\xi\) produce ceros de \(X_a\) en
\(\frac12-a+i\gamma\) y \(\frac12+a+i\gamma\). Por tanto \(X_a\) tiene ceros
fuera de su línea de simetría para todo \(a>0\).

Sin embargo, su parte Euler

\[
 Z_a(s)=\zeta(s+a)\zeta(s-a)
\]

posee pesos logarítmicos estrictamente positivos:

\[
 -{Z_a'\over Z_a}(s)
 =\sum_{m\ge2}{2\Lambda(m)\cosh(a\log m)\over m^s},
 \tag{23}
\]

y su cociclo es el producto de dos cociclos Jordan,

\[
 {Z_a(s-u)\over Z_a(s)}=A_u(s+a)A_u(s-a).
 \tag{24}
\]

En \(\Re s>1+a+u\), el coeficiente de \(r^{-s}\) en (24) es

\[
 \sum_{mn=r}J_u(m)J_u(n)m^{-a}n^a\ge0.
 \tag{25}
\]

La normalización polar correcta tampoco rompe el ejemplo. Es

\[
 A^0_{u,a}(s)=
 {s+a-1\over s+a-u-1}{s-a-1\over s-a-u-1}.
 \tag{26}
\]

Con

\[
 F_a(s)=(s+a-1)(s-a-1)Z_a(s),
\]

el cociente emparejado vuelve a ser

\[
 {Z_a(s-u)/Z_a(s)\over A^0_{u,a}(s)}
 ={F_a(s-u)\over F_a(s)}.
 \tag{27}
\]

Así, **jerarquía Jordan completa, coeficientes Euler positivos, pesos
von-Mangoldt positivos, conjugación y ecuación funcional** coexisten con ceros
off-line. Cualquier argumento que solo use esas propiedades también se
aplicaría a \(X_a\) y es falso. Un mecanismo válido para zeta debe emplear una
propiedad cuantitativa adicional de los pesos reales \(\Lambda(p^k)=\log p\),
no solamente su pertenencia al cono Jordan.

## 7. Completar con Gamma produce un criterio equivalente a RH

Podría intentarse reparar la falta de una comparación Euler--Gamma pasando al
cociclo completado

\[
 \Theta_u(s):={\xi(s-u)\over\xi(s)}=K_u(s)H_u(s),
 \qquad
 K_u(s)={s-u\over s}\,\pi^{u/2}
 {\Gamma((s-u)/2)\over\Gamma(s/2)}.
 \tag{28}
\]

El factor completado sí aporta una geometría exacta. Sobre

\[
 \Re s={1+u\over2}
 \tag{29}
\]

se tiene \(s-u=1-\bar s\), y por ecuación funcional y reflexión de Schwarz,

\[
 \xi(s-u)=\xi(1-\bar s)=\xi(\bar s)=\overline{\xi(s)}.
 \tag{30}
\]

Luego \(|\Theta_u(s)|=1\) en los puntos donde el cociente está definido (con
extensión removible en los ceros comunes). Pero la contractividad interior no
es una desigualdad nueva:

**Teorema (gate Schur completado).** Para \(u>0\), sea

\[
 {\cal H}_u=\{s:\Re s>(1+u)/2\}.
 \tag{31}
\]

RH implica que \(\Theta_u\) es holomorfa y
\(|\Theta_u(s)|\le1\) en \({\cal H}_u\), para todo \(u>0\). Recíprocamente,
basta que exista una sucesión \(u_j\downarrow0\) para la cual cada
\(\Theta_{u_j}\) sea holomorfa en \({\cal H}_{u_j}\). Entonces RH. Por tanto
la propiedad Schur para la familia completada es equivalente a RH.

**Prueba de la dirección RH.** Escribamos

\[
 \Xi(w)=\xi(1/2+w),\qquad c=u/2,qquad
 w=s-(1+u)/2.
\]

Bajo RH, el producto par convergente es

\[
 \Xi(w)=\Xi(0)\prod_{\gamma>0}\left(1+{w^2\over\gamma^2}\right),
 \tag{32}
\]

con multiplicidades. Además,

\[
 \Theta_u(s)={\Xi(w-c)\over\Xi(w+c)}
 =\prod_{\gamma>0}
 {w-c-i\gamma\over w+c-i\gamma}
 {w-c+i\gamma\over w+c+i\gamma}.
 \tag{33}
\]

Si \(\Re w>0\), cada factor tiene módulo menor o igual que uno porque

\[
 |w+c\mp i\gamma|^2-|w-c\mp i\gamma|^2
 =4c\Re w>0.
 \tag{34}
\]

El producto da la contractividad.

**Prueba del converso.** Si \(\rho\) fuera un cero con
\(\Re\rho>1/2\), para todo \(j\) suficientemente grande se tendría

\[
 0<u_j<2\Re\rho-1.
 \tag{35}
\]

Si el polo en \(\rho\in{\cal H}_{u_j}\) se cancelara para todos esos índices,
entonces \(\xi(\rho-u_j)=0\) daría una sucesión de ceros distintos acumulada
en \(\rho\), imposible para una función entera no nula. Para algún \(j\),
\(\Theta_{u_j}\) tiene un polo en \({\cal H}_{u_j}\), contradicción. No hay
ceros a la derecha de la línea crítica, y la simetría
\(\rho\mapsto1-\bar\rho\) excluye también los de la izquierda. \(\square\)

Así, agregar exactamente el factor Gamma que faltaba en (9) restaura
unitariedad de borde, pero la propiedad interior necesaria ya contiene RH.
Usarla para deducir A1 sería circular. El factor Euler aislado tiene
positividad de coeficientes sin control de borde; el factor completado tiene
el borde correcto, pero su contractividad es el problema entero.

### 7.1. Hasta dónde llegan las cotas radiales no circulares

Las dos piezas sí admiten cotas separadas en el semiplano de convergencia.
Por (1),

\[
 |A_u(\sigma+it)|\le A_u(\sigma)
 \qquad(\sigma>1+u).
 \tag{36}
\]

Además, la forma equivalente de \(K_u\) es

\[
 K_u(s)=\pi^{u/2}{\Gamma((s-u)/2+1)\over\Gamma(s/2+1)}
 ={\pi^{u/2}\over\Gamma(u/2)}
 \int_0^1x^{(s-u)/2}(1-x)^{u/2-1}\,dx,
 \tag{37}
\]

de modo que \(|K_u(\sigma+it)|\le K_u(\sigma)\) cuando
\(\sigma>u-2\). Éstas son desigualdades genuinas y no usan ceros.

No dan automáticamente una cota para \(\Theta_u=K_uH_u\), porque

\[
 H_u(s)=\left(1-{u\over s-1}\right)A_u(s)
 \tag{38}
\]

y, para \(\sigma>1+u\),

\[
 \left|1-{u\over\sigma-1+it}\right|
 \ge 1-{u\over\sigma-1}.
 \tag{39}
\]

El factor polar se mueve en la dirección opuesta a la comparación radial.
Hace falta otra cancelación para combinar (36)--(39); aun si se obtuviera en
el semiplano seguro \(\Re s>1+u\), extenderla hasta \({\cal H}_u\) volvería
al gate Schur anterior.

### 7.2. El presupuesto Gamma exacto vuelve a ser \(\Delta D_n\)

La mitad de completación que corresponde al strong margin tampoco deja una
desigualdad intermedia. Defínase, como germen en \(u=0\),

\[
 B_u(s)=H_u(s)K_u(s)^{1/2}.
 \tag{40}
\]

En la coordenada crítica \(s=(1-z)^{-1}\), las identidades generatrices de
las partes prima y arquimediana son

\[
 \log{F((1-z)^{-1})\over F(1)}
   =\sum_{n\ge1}{\lambda_n^{\rm prime}\over n}z^n,
 \qquad
 \log{Q((1-z)^{-1})\over Q(1)}
   =\sum_{n\ge1}{A_n\over n}z^n,
\]

donde \(Q=\xi/F\). Derivar en \(z\) y multiplicar por \(-(1-z)\)
convierte cada sucesión en el negativo de su primera diferencia. Como
\((1-z)^{-1}\partial_u\{G(s-u)/G(s)\}_{u=0}=-sG'(s)/G(s)\), se obtiene, para
\(n\ge1\),

\[
\begin{aligned}
 [z^n]{1\over1-z}\left.\partial_uH_u\right|_0
   &=C_n=-\Delta\lambda_n^{\rm prime},\\
 [z^n]{1\over1-z}\left.\partial_uK_u\right|_0
   &=-\Delta A_n.
\end{aligned}
\tag{41}
\]

Como \(H_0=K_0=1\), se sigue exactamente

\[
 \boxed{
 [z^n]{1\over1-z}\left.\partial_uB_u\right|_0
 =C_n-{1\over2}\Delta A_n
 =-{1\over2}\Delta D_n.}
 \tag{42}
\]

Por tanto la cota coeficiente a coeficiente que M6 necesitaría para cerrar el
presupuesto Gamma es literalmente \(\Delta D_n\ge0\), el mismo gate de
`103_59`. La raíz cuadrada en (40) no es una factorización positiva global:
solo es el germen algebraico que asigna media contribución arquimediana.
Contractividad Schur tampoco impone el signo individual de los coeficientes
de (42), y en este caso obtenerla globalmente ya equivale a RH.

## 8. El dominio positivo no alcanza el borde crítico

La expansión aritmética positiva (1) requiere

\[
 \Re s>1+u.
\tag{43}
\]

En el centro de (12), \(s=1+\varepsilon\); por tanto un \(u>0\) fijo solo es
admisible mientras \(u<\varepsilon\). No existe un entorno fijo en la variable
de cociclo que conserve la representación positiva cuando
\(\varepsilon\downarrow0\). Los jets en \(u=0\) sí existen para cada
\(\varepsilon>0\), pero el paso al borde exige exactamente la cancelación
polo--primos de (17), donde el signo ya se perdió.

La continuación meromorfa tampoco es un atajo libre. En \(\varepsilon=0\), un
cero \(\rho\) del denominador \(F(s)\) se transforma en

\[
 z_\rho={\rho-1\over\rho}=1-{1\over\rho}.
\tag{44}
\]

Y

\[
 |z_\rho|<1\quad\Longleftrightarrow\quad\Re\rho>{1\over2}.
\tag{45}
\]

Para \(u\) genérico, \(F(\rho-u)\ne0\), de modo que el polo no se cancela en
\(H_u\). En el regulador \(\varepsilon>0\), el punto es

\[
 z_{\rho,\varepsilon}
 ={\rho-1-\varepsilon\over\rho-\varepsilon},
 \qquad
 |z_{\rho,\varepsilon}|<1
 \Longleftrightarrow
 \Re\rho>{1\over2}+\varepsilon.
\tag{46}
\]

Así, una prolongación holomorfa uniforme del cociclo a todo el disco crítico
excluye precisamente los ceros a la derecha de la línea crítica. Usar esa
prolongación para justificar un teorema de coeficientes sería circular.

## 9. Alcance exacto del stop-gate

Queda probado:

1. la jerarquía aritmética \(\mu*\log^k\ge0\) para todo \(k\);
2. su ley de cociclo y su pullback Cayley--Laguerre exacto;
3. que el emparejamiento con el polo convierte esa positividad en la
   diferencia (9);
4. que el primer jet coincide con \(C_{n,\varepsilon}\);
5. con aritmética racional, que ese jet tiene ambos signos;
6. que el dominio de positividad de Dirichlet no sobrevive al límite crítico;
7. que la holomorfía uniforme del cociclo en el disco es sensible exactamente
   a ceros off-line.
8. que la jerarquía Jordan completa y la ecuación funcional admiten el
   falsificador explícito \(X_a\).
9. que completar el cociclo produce una familia Schur equivalente a RH, no
   una cota independiente.

Queda descartado:

```text
J_u >= 0 / mu*log^k >= 0
    -> orden real del cociclo
    -> signo o convexidad coeficiente a coeficiente en Cayley
    -> A1.
```

No queda descartada toda identidad imaginable que use simultáneamente varios
valores de \(u\), pero para ser un mecanismo nuevo deberá producir (20) sin
invocar holomorfía/contractividad en el disco y sin volver a enunciar el mismo
gate. El cociclo de Jordan, por sí solo, es una coordenada positiva del lado
Euler; no aporta la comparación Euler--Gamma que ya faltaba en E70.12.

## 10. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 jordan_cocycle_sign_gate.py
```

Todos los signos de (11) y (19) se deciden con `Fraction` sobre intervalos
decimales outward; no interviene punto flotante.
