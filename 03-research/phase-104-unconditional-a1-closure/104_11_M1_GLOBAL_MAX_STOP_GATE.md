# 104_11 — M1 global: energía `max`, cancelación de la Hessiana y stop-gate

**Estado:** la factorización global del núcleo `max` queda cerrada exactamente. El
compensador continuo de `104_10` es la energía del mismo núcleo aplicada a

\[
 d\sigma=d\psi-dx.
\]

Al sumarla al primer término de M1, la componente cuadrática
\(d\psi\times d\psi\) se cancela idénticamente. No queda una forma de Gram que pueda
proporcionar coercividad: queda el funcional lineal original
\(-\int E\tau'\). Por tanto **M1 como mecanismo operatorial global se descarta**. Esto
no refuta la desigualdad buscada para los pesos reales de von Mangoldt; prueba que
demostrarla requiere un input aritmético nuevo que no proviene del núcleo `max` ni de
su compensador.

La Sección 7 registra el sucesor exacto M5: una convolución firmada
Möbius–divisor en el grado Laguerre. No se prueba A1 ni RH.

## 1. Formulación finita

Fíjese \(X>1\), que no sea potencia prima, y una función real
\(w\in C^1([1,X])\). Póngase

\[
 d\mu=\sum_{q_j<X}\ell_j\delta_{q_j},
 \qquad d\nu=\mathbf 1_{[1,X]}(x)\,dx,
 \qquad d\sigma=d\mu-d\nu,
\tag{1}
\]

donde \(q_j\) son las potencias primas y \(\ell_j=\Lambda(q_j)\). Su función
acumulada es

\[
 E(x)=\sigma([1,x])=\psi(x)-x+1
 \qquad(1\le x\le X).
\tag{2}
\]

Defínanse la energía global y el primer término de M1 por

\[
 Q_X(w;\sigma)
 ={1\over2}\iint_{[1,X]^2}
 w(\max\{x,y\})\,d\sigma(x)d\sigma(y),
\tag{3}
\]

\[
 S_X(w;\mu)
 =\int_{[1,X]}(x-1)w(x)\,d\mu(x)
 -{1\over2}\iint_{[1,X]^2}
 w(\max\{x,y\})\,d\mu(x)d\mu(y).
\tag{4}
\]

Para la medida de von Mangoldt, (4) es exactamente

\[
 S_X=\sum_{q_j<X}\ell_jd_jw(q_j),
 \qquad
 d_j=q_j-1-\Psi_{j-1}-{\ell_j\over2},
\tag{5}
\]

porque agrupar la suma doble por su índice máximo da la identidad (8) de
`104_10`.

## 2. Teorema de energía global

**Teorema 1 (el compensador es la energía `max`).** Con las convenciones
anteriores,

\[
 \boxed{
 Q_X(w;\sigma)
 ={1\over2}E(X)^2w(X)
 -{1\over2}\int_1^X E(x)^2w'(x)\,dx.}
\tag{6}
\]

En particular, si \(w=\tau'\), el segundo término de (6) es exactamente el
compensador de (6) en `104_10`, incluido su borde finito.

**Prueba.** La imagen de la medida producto \(\sigma\otimes\sigma\) por
\((x,y)\mapsto\max\{x,y\}\) tiene función acumulada

\[
 (\sigma\otimes\sigma)
 \{(x,y):\max(x,y)\le t\}=E(t)^2.
\]

Esta igualdad incorpora automáticamente las diagonales atómicas. Por tanto

\[
 2Q_X=\int_{[1,X]}w(t)\,d(E(t)^2).
\]

La integración de Stieltjes por partes, usando \(E(1)=0\), prueba (6).
\(\square\)

Hay también una factorización firmada continua:

\[
 \boxed{
 Q_X={w(X)\over2}E(X)^2
 +{1\over2}\int_1^X[-w'(t)]E(t)^2\,dt.}
\tag{7}
\]

Así, cuando \(w(X)\ge0\) y \(-w'\ge0\), (7) sí es una mezcla positiva de
cuadrados de prefijos. Para el peso Laguerre real esas hipótesis no se cumplen
uniformemente.

## 3. Cancelación exacta de la parte cuadrática

**Teorema 2 (colapso global de M1).** Para toda medida finita \(\mu\) en
\([1,X]\), no solamente para la de von Mangoldt,

\[
 \boxed{
 S_X(w;\mu)+Q_X(w;\mu-\nu)
 =-\int_1^X E(x)w(x)\,dx.}
\tag{8}
\]

Por consiguiente, al tomar \(w=\tau'\), (8) es exactamente

\[
 C_{n,\varepsilon}(X)=-\int_1^XE(x)\tau'(x)\,dx.
\tag{9}
\]

**Prueba.** Expándase (3) en sus tres componentes:

\[
 \begin{aligned}
 Q_X={}&{1\over2}\iint w(\max)\,d\mu d\mu
 -\int_{[1,X]}\left(\int_1^Xw(\max\{q,y\})\,dy\right)d\mu(q)\\
 &+{1\over2}\iint_{[1,X]^2}w(\max\{x,y\})\,dxdy.
 \end{aligned}
\tag{10}
\]

Los dos integrales elementales que aparecen aquí son

\[
 \int_1^Xw(\max\{q,y\})\,dy
 =(q-1)w(q)+\int_q^Xw(y)\,dy,
\tag{11}
\]

\[
 {1\over2}\iint_{[1,X]^2}w(\max\{x,y\})\,dxdy
 =\int_1^X(y-1)w(y)\,dy.
\tag{12}
\]

Al sumar (4), el término \(\frac12\iint w(\max)d\mu d\mu\) de (10)
cancela exactamente el término con signo menos de (4). También se cancelan
los términos \((q-1)w(q)\). Por Fubini,

\[
 \int_{[1,X]}\int_q^Xw(y)\,dy\,d\mu(q)
 =\int_1^X\mu([1,y])w(y)\,dy.
\]

La suma restante es

\[
 -\int_1^X\{\mu([1,y])-(y-1)\}w(y)\,dy
 =-\int_1^XE(y)w(y)\,dy,
\]

que prueba (8). \(\square\)

La conclusión operatorial es más fuerte que observar que una integración por
partes vuelve al punto de partida: **la única componente cuadrática aritmética se
cancela antes de estimar**.

## 4. Hessiana nula: no sobrevive coercividad cuadrática

Sea \(\eta\) cualquier medida firmada finita y considérese
\(\mu_t=\mu+t\eta\). En (4), el coeficiente de \(t^2\) es

\[
 -{1\over2}\iint w(\max)\,d\eta d\eta;
\tag{13}
\]

en (3), el coeficiente de \(t^2\) es el opuesto

\[
 +{1\over2}\iint w(\max)\,d\eta d\eta.
\tag{14}
\]

Por tanto

\[
 {d^2\over dt^2}
 \{S_X(w;\mu_t)+Q_X(w;\mu_t-\nu)\}=0.
\tag{15}
\]

El borde de esta cancelación puede verse sin apelar a (8). Si

\[
 F(x)=\eta([1,x]),
\]

el Teorema 1, aplicado a \(\eta\), da exactamente

\[
 \boxed{
 \iint_{[1,X]^2}w(\max\{x,y\})\,d\eta(x)d\eta(y)
 =w(X)F(X)^2-\int_1^X F(x)^2w'(x)\,dx.}
\tag{15a}
\]

La segunda variación de \(S_X\) es el negativo del miembro izquierdo de
(15a). La segunda variación del compensador escrito como en (6) es

\[
 -\int_1^XF(x)^2w'(x)\,dx+w(X)F(X)^2,
\]

su opuesto exacto. En particular, omitir el borde
\(w(X)F(X)^2\) produciría una Hessiana residual espuria. Más aún, (8) da
la identidad afín completa

\[
 \boxed{
 S_X(w;\mu+t\eta)+Q_X(w;\mu+t\eta-\nu)
 =S_X(w;\mu)+Q_X(w;\mu-\nu)
   -t\int_1^XF(x)w(x)\,dx.}
\tag{15b}
\]

No hay términos de orden dos o superior escondidos por la truncación.

Éste es el stop-gate mínimo para una factorización de Gram global:

* factorizar el compensador solo factoriza (14);
* el primer término contiene exactamente (13);
* al mantener ambos acoplados, como exige el plan, no queda una forma cuadrática
  positiva ni negativa;
* cualquier coercividad posterior debe provenir de una propiedad aritmética
  adicional de la medida fija \(d\psi\), no del kernel `max`.

No se afirma que todo posible argumento no lineal sea imposible. Se descarta la
fuente concreta de positividad propuesta por M1.

### 4.1 La alternativa por módulos pierde la escala de manera cuantificada

Tras (15b), tomar módulos ya no estima una energía colectiva: estima el funcional
lineal original. Con \(w=\tau'\) y al retirar el regulador, la cota VK puntual
produce exactamente la carga \(\mathcal B_n\) de `103_56`, ecuación (20). Allí
se probó

\[
 \mathcal B_n\ge
 \exp\!\left({2\over3}n\log n+{1\over3}n\log\log n-O(n)\right),
\tag{15c}
\]

mientras el presupuesto de primera diferencia es
\(\frac12\Delta A_n=O(\log n)\). Por tanto, una vez cancelada la Hessiana,
la salida `valor absoluto + VK` no es solamente inconclusa: pierde una cantidad
superpolinomial frente al presupuesto. La única posibilidad que M1 dejaba viva
era una estimación firmada especial de la medida real; (8) muestra que esa
estimación es de nuevo el funcional de primera diferencia y no una consecuencia
del kernel `max`.

## 5. Inercia exacta del kernel discreto

En puntos ordenados \(x_1<\cdots<x_M\), ponga \(w_j=w(x_j)\) y

\[
 K_{ij}=w_{\max(i,j)},\qquad
 \delta_j=w_j-w_{j+1}\ (j<M),\qquad \delta_M=w_M.
\tag{16}
\]

Si \(v_j=(1,\ldots,1,0,\ldots,0)^T\) tiene sus primeras \(j\) entradas iguales
a uno, entonces

\[
 \boxed{K=\sum_{j=1}^M\delta_jv_jv_j^T.}
\tag{17}
\]

La matriz con columnas \(v_j\) es triangular e invertible. Por la ley de inercia
de Sylvester, la inercia de \(K\) es exactamente la cantidad de signos positivos,
negativos y nulos entre

\[
 w_1-w_2,\ldots,w_{M-1}-w_M,w_M.
\tag{18}
\]

Así, la descomposición de `104_10` no estaba perdiendo una PSD global oculta: (17)
es la factorización maximal del kernel.

Para el peso regulado

\[
 \tau(x)=x^{-a}L_n(\log x),\qquad a=1+\varepsilon,qquad w=\tau',
\]

se tiene

\[
 \tau''(x)=x^{-a-2}
 \{L_n''(u)-(2a+1)L_n'(u)+a(a+1)L_n(u)\},
 \qquad u=\log x.
\tag{19}
\]

En \(x=1\), el factor entre llaves vale

\[
 {n(n-1)\over2}+(2a+1)n+a(a+1)>0.
\tag{20}
\]

Cuando \(u\to\infty\), su término principal es

\[
 a(a+1){(-1)^n\over n!}u^n.
\tag{21}
\]

Para todo \(n\) impar, \(\tau''\) cambia de signo. Luego la mezcla de cuadrados
(7) es indefinida, y el kernel continuo admite discretizaciones finas con ambas
inercias, para infinitos índices del rango objetivo. Esto no afirma, sin una
comprobación adicional, que una discretización prefijada solamente en potencias
primas muestree ambos intervalos de signo. No hace falta esa afirmación: la
cancelación (15a) es exacta también en esos nodos. Incluso antes de cancelar las
Hessianas, no existe una PSD uniforme del kernel continuo.

## 6. Falsificadores en los axiomas exactos

### 6.1 Relajación de medidas positivas

Si se relaja la aritmética fija y se mueve una masa \(W>0\) desde \(b\) hacia
\(a<b\), conservando la masa total, (8) da

\[
 \delta C=W\{\tau(a)-\tau(b)\}.
\tag{22}
\]

Los polinomios Laguerre hacen que (22) tenga ambos signos. Por tanto ningún
argumento que use solamente soporte ordenado, masas positivas y el kernel `max`
puede producir la cota M1. Este falsificador satisface exactamente el nivel
algebraico finito de `104_10`.

### 6.2 Relajación espectral

Si un paso abandona los pesos reales \(\Lambda(p^k)=\log p\) y conserva solo
conjugación y ecuación funcional, se aplica el cuarteto

\[
 8-8\cosh(n\alpha)\cos(n\theta),
\tag{23}
\]

que tiene ambos signos. No se ha usado (23) para refutar un teorema aritmético:
se usa únicamente contra relajaciones que ya dejaron de emplear el nivel 4 de
`104_10`.

## 7. Sucesor M5: convolución Möbius–divisor firmada

El stop-gate anterior deja una estructura exacta todavía no explotada por M1:

\[
 \Lambda=\mu*\log.
\]

Sea \(a=1+\varepsilon>1\), y defínanse

\[
 \mathfrak M_j(a)
 =\sum_{d\ge1}{\mu(d)\over d^a}L_j(\log d),
\qquad
 \mathfrak B_k(a)
 =\sum_{m\ge1}{\log m\over m^a}L_k^{(-1)}(\log m).
\tag{24}
\]

Todas las series son absolutamente convergentes. La fórmula de adición

\[
 L_n(x+y)=\sum_{j=0}^nL_j(x)L_{n-j}^{(-1)}(y)
\tag{25}
\]

y \(\Lambda=\mu*\log\) dan el teorema exacto

\[
 \boxed{
 \sum_{r\ge2}{\Lambda(r)\over r^a}L_n(\log r)
 =\sum_{j=0}^n\mathfrak M_j(a)\mathfrak B_{n-j}(a).}
\tag{26}
\]

No se ha aplicado valor absoluto ni Cauchy en el grado.

Con

\[
 t={z\over1-z},
\]

las funciones generatrices verifican

\[
 \sum_{j\ge0}\mathfrak M_j(a)z^j
 ={1\over1-z}{1\over\zeta(a+t)},
 \qquad
 \sum_{k\ge0}\mathfrak B_k(a)z^k=-\zeta'(a+t).
\tag{27}
\]

Su producto es exactamente la generatriz del lado izquierdo de (26).

El término continuo que debe permanecer emparejado es

\[
 J_{n,\varepsilon}
 =\int_1^\infty x^{-1-\varepsilon}L_n(\log x)\,dx
 ={(\varepsilon-1)^n\over\varepsilon^{n+1}}.
\tag{28}
\]

Por tanto

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{j=0}^n\mathfrak M_j(1+\varepsilon)
                     \mathfrak B_{n-j}(1+\varepsilon)
  -J_{n,\varepsilon}.}
\tag{29}
\]

Los dos términos de (29) divergen por separado cuando
\(\varepsilon\downarrow0\); (29) es una identidad emparejada, no una autorización
para estimarlos separadamente.

Hay una normalización que conserva automáticamente esa colisión. Defínase

\[
 F_\varepsilon(z)
 =(\varepsilon+t)\zeta(1+\varepsilon+t).
\tag{30}
\]

Entonces, usando el germ \(R\) de `103_66`,

\[
 \boxed{
 \sum_{n\ge0}C_{n,\varepsilon}z^n
 =-(1-z)F_\varepsilon(z)^{-1}F_\varepsilon'(z).}
\tag{31}
\]

Si \(F_\varepsilon=\sum f_kz^k\) y
\(F_\varepsilon^{-1}=\sum g_jz^j\), (31) es una convolución firmada explícita
entre los grados de la unidad Euler normalizada y los de su inversa Möbius. La
identidad de Riccati de E70.12 es la derivada de (31); por sí sola no aporta un
signo arquimediano.

El teorema nuevo que M5 tendría que aportar es una estimación **directa de la
convolución completa (29) o (31)** por

\[
 {1\over2}\Delta A_n,
\tag{32}
\]

uniforme antes de tomar \(\varepsilon\downarrow0\). Separar las normas de
\(\mathfrak M\) y \(\mathfrak B\) recrea exactamente la pérdida exponencial de
`103_70`–`103_71` y queda prohibido.

## 8. Decisión

```text
probado:
  el compensador continuo es la energía global del kernel max;
  la identidad M1 es S_X + Q_X con todos los bordes;
  la parte mu x mu se cancela exactamente;
  la Hessiana total respecto de la medida es cero;
  la inercia del kernel max está dada exactamente por sus primeras diferencias;
  el kernel Laguerre es indefinido para todo índice impar;
  la factorización Möbius–divisor firmada (26)--(31).

descartado:
  M1 como fuente global de coercividad o Gram;
  cualquier PSD obtenida factorizando solo uno de los dos términos;
  estimar por separado los dos factores de la convolución de grado.

no probado:
  una desigualdad especial para los pesos reales de von Mangoldt;
  (32), A1 o RH.

sucesor recomendado:
  M5, exclusivamente en la forma acoplada (29) o (31).
```

M3 puede seguir existiendo como reorganización no local de lóbulos, pero el mapa
estacionario no introduce un input aritmético. Después de la cancelación exacta de
M1, M5 es el sucesor con una estructura adicional concreta que todavía no fue
consumida: la inversión Möbius dentro de la convolución de grados.

## Verificación mecánica

`tools/m1_global_hessian_check.py` verifica con `Fraction`, sin punto flotante,
las identidades finitas (6), (8) y (15a). Incluye dos perturbaciones: una de masa
total cero y otra con \(F(X)\ne0\), de modo que un signo incorrecto o la omisión
del borde \(w(X)F(X)^2\) hace fallar el chequeo.
