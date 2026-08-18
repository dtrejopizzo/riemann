# 104_19 — Cociclo sin ramas: expansión de tres canales y stop-gate

**Rol.** Auditar el sucesor de `104_18` que incorpora exactamente el
presupuesto Gamma del strong margin. Se obtiene una expansión finita con
coeficientes aritméticos no negativos y medida Beta positiva. El factor
polar, sin embargo, es una combinación firmada de tres canales y el límite
es exactamente \(-\Delta D_n\), el gate de `103_59`.

**Veredicto.** No se obtiene una desigualdad incondicional nueva. Este
documento no prueba A1 ni RH.

## 1. Gate de duplicación interna

El objeto no es nuevo. `103_49`, `103_53` y `103_59` ya definen

\[
 Y(s)={\xi(s)^2\over s\pi^{-s/2}\Gamma(s/2)}
 ={1\over4}s(s-1)^2\pi^{-s/2}\Gamma(s/2)\zeta(s)^2. \tag{1}
\]

`103_59` prueba

\[
 \log{Y((1-z)^{-1})\over Y(1)}
 =\sum_{n\ge1}{D_n\over n}z^n,
 \qquad D_n=2\lambda_n-A_n,                         \tag{2}
\]

y

\[
 s{Y'(s)\over Y(s)}-D_1
 =\sum_{n\ge1}\Delta D_nz^n,\qquad s=(1-z)^{-1}.   \tag{3}
\]

Aquí \(\Delta D_n=D_{n+1}-D_n\).

El cociclo que se ensaya es

\[
 \mathcal S_u(s):={Y(s-u)\over Y(s)}.               \tag{4}
\]

Si \(H_u=F(s-u)/F(s)\), \(F=(s-1)\zeta(s)\), y

\[
 K_u(s):=\pi^{u/2}{\Gamma(1+(s-u)/2)\over\Gamma(1+s/2)}, \tag{5}
\]

entonces

\[
 \boxed{\mathcal S_u(s)=H_u(s)^2K_u(s).}            \tag{6}
\]

Es también el cuadrado del medio-cociclo
\(H_uK_u^{1/2}\) de `104_16` §7.2. La única pregunta nueva es si
mantener \(u=c\varepsilon\) finito preserva una cancelación de tres canales
que el primer jet oculta.

## 2. El canal Euler cuadrático es positivo

Para \(\Re s>1+u\),

\[
 A_u(s)={\zeta(s-u)\over\zeta(s)}
 =\sum_{m\ge1}{J_u(m)\over m^s},\qquad J_u(m)\ge0.  \tag{7}
\]

Póngase

\[
 b_u=J_u*J_u.
\]

Entonces

\[
 \boxed{A_u(s)^2=\sum_{m\ge1}{b_u(m)\over m^s},\qquad b_u(m)\ge0.} \tag{8}
\]

La función \(b_u\) es multiplicativa. Si \(q=p^u\) y \(k\ge1\),

\[
 \boxed{
 b_u(p^k)=2(q-1)q^{k-1}
 +(k-1)(q-1)^2q^{k-2}.}                            \tag{9}
\]

En efecto, \(J_u(p^0)=1\) y
\(J_u(p^j)=(q-1)q^{j-1}\) para \(j\ge1\). Los dos extremos de la
convolución dan el primer término de (9), y los \(k-1\) términos interiores
son todos \((q-1)^2q^{k-2}\).

## 3. El canal Gamma tiene medida Beta positiva

La forma (5) y la integral Beta dan

\[
 K_u(s)={\pi^{u/2}\over\Gamma(u/2)}
 \int_0^1v^{(s-u)/2}(1-v)^{u/2-1}\,dv.             \tag{10}
\]

Fijemos

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z},
 \qquad u=c\varepsilon,\qquad0<c<1,                 \tag{11}
\]

y definamos la medida positiva

\[
 d\nu_{\varepsilon,u}(v)
 ={\pi^{u/2}\over\Gamma(u/2)}
 v^{(1+\varepsilon-u)/2}(1-v)^{u/2-1}\,dv.         \tag{12}
\]

El factor \(v^{z/[2(1-z)]}\) desplaza el argumento Laguerre en
\(-\frac12\log v\). No se pierde ningún signo en este canal.

## 4. Teorema exacto de los tres canales

La parte polar de \(H_u^2\) es

\[
 \left(1-{u\over s-1}\right)^2
 =1-{2u\over s-1}+{u^2\over(s-1)^2}.               \tag{13}
\]

Sean

\[
 d\omega_0(y)=\delta_0(dy),\qquad
 d\omega_1(y)=e^{-\varepsilon y}\,dy,
 \qquad
 d\omega_2(y)=y e^{-\varepsilon y}\,dy,            \tag{14}
\]

y

\[
 \begin{aligned}
 T_{n,j}:={}&\sum_{m\ge1}{b_u(m)\over m^{1+\varepsilon}}
 \int_0^1\int_0^\infty
 L_n\!\left(\log m+y-\tfrac12\log v\right)\\
 &\hspace{42mm}d\omega_j(y)\,d\nu_{\varepsilon,u}(v).
 \end{aligned}                                      \tag{15}
\]

**Teorema.** Para todo \(n\ge0\),

\[
 \boxed{
 [z^n]{\mathcal S_u(s_\varepsilon(z))\over1-z}
 =T_{n,0}-2uT_{n,1}+u^2T_{n,2}.}                   \tag{16}
\]

*Demostración.* La generatriz

\[
 {e^{-xz/(1-z)}\over1-z}=\sum_{n\ge0}L_n(x)z^n    \tag{17}
\]

aplicada a (8) y (10) produce \(T_{n,0}\). Además,

\[
 {1\over\varepsilon+z/(1-z)}
 =\int_0^\infty e^{-\varepsilon y}
 e^{-yz/(1-z)}\,dy,                                 \tag{18}
\]

y la misma identidad con el cuadrado del denominador inserta el factor
\(y\). Multiplicar (17) por (18) desplaza \(L_n(x)\) a \(L_n(x+y)\).
Combinar los tres términos de (13) prueba (16). Todas las series e
integrales convergen absolutamente para \(u<\varepsilon\) y \(z\) en un
entorno suficientemente pequeño del origen. \(\square\)

Cada \(T_{n,j}\) se construye desde medidas positivas, pero \(L_n\) tiene
signo y la combinación \(1,-2u,u^2\) también. La positividad de (8) y (12)
no decide (16).

## 5. Límite exacto: reaparece \(-\Delta D_n\)

Defínase

\[
 {\mathcal S_{c\varepsilon}(s_\varepsilon(z))-1
   \over c\varepsilon(1-z)}
 =\sum_{n\ge0}g_{n,\varepsilon,c}z^n.              \tag{19}
\]

Por (16),

\[
 \boxed{
 g_{n,\varepsilon,c}
 ={T_{n,0}-2uT_{n,1}+u^2T_{n,2}-1\over u}.}         \tag{20}
\]

Solo la combinación completa admite el límite. Como

\[
 {\mathcal S_u(s)-1\over u}\longrightarrow-{Y'(s)\over Y(s)},
\]

las ecuaciones (2)--(3) dan

\[
 \boxed{
 \begin{aligned}
  g_{0,\varepsilon,c}&\longrightarrow-D_1,\\
  g_{n,\varepsilon,c}&\longrightarrow-\Delta D_n,\qquad n\ge1.
 \end{aligned}}                                      \tag{21}
\]

El parámetro \(c\) desaparece. Probar
\(g_{n,\varepsilon,c}\le0\) uniformemente al retirar el regulador probaría
\(\Delta D_n\ge0\), el gate fuerte suficiente para A1 ya registrado en
`103_59`; no es una desigualdad intermedia más débil.

## 6. Stop-gate: el cuadrado polar no es una mezcla positiva

Aunque (13) es no negativo para \(s>1+u\), su transformada inversa de
Laplace en \(t=s-1-\varepsilon\) es

\[
 d\mu_{\varepsilon,u}(y)
 =\delta_0(dy)-2u e^{-\varepsilon y}\,dy
     +u^2y e^{-\varepsilon y}\,dy.                 \tag{22}
\]

Tras \(u=c\varepsilon\) y \(r=\varepsilon y\),

\[
 \boxed{
 d\mu_c(r)=\delta_0(dr)+c(cr-2)e^{-r}\,dr.}         \tag{23}
\]

La densidad continua de (23) es estrictamente negativa en
\(0<r<2/c\) para **todo** \(c>0\). Por tanto el cuadrado real no es una
mezcla Laplace positiva y ningún valor de \(c\) elimina el canal firmado.

La divergencia que la combinación debe cancelar ya aparece en el término
Euler \(m=1\), aun omitiendo Gamma:

\[
 \boxed{
 [z]{1\over1-z}
 \left(1-{u\over\varepsilon+z/(1-z)}\right)^2
 =(1-c)^2+{2c(1-c)\over\varepsilon}.}               \tag{24}
\]

Para \(0<c<1\), (24) diverge como \(\varepsilon^{-1}\). Esto persiste al
reponer Gamma. En efecto, si

\[
 K_0:=K_u(1+\varepsilon),\qquad
 K_1:=[z]K_u(s_\varepsilon(z)),
\]

entonces \(K_0=1+O(\varepsilon)\) y \(K_1=O(\varepsilon)\), porque

\[
 \partial_s\log K_u(s)
 ={1\over2}\left\{\psi(1+(s-u)/2)-\psi(1+s/2)\right\}=O(u).
\]

Por tanto el coeficiente completo del subcanal \(m=1\) es

\[
 K_0\left((1-c)^2+{2c(1-c)\over\varepsilon}\right)
 +K_1(1-c)^2
 ={2c(1-c)\over\varepsilon}+O(1).                  \tag{24a}
\]

Así, separar \(m=1\) de \(m>1\) destruye precisamente la cancelación
que hace finito (21).

## 7. Falsificador global y límite de su alcance

Considérese

\[
 X_a(s)=\xi(s+a)\xi(s-a),\qquad0<a<\tfrac12.        \tag{25}
\]

Satisface \(X_a(1-s)=X_a(s)\) y tiene ceros
\(1/2\pm a+i\gamma\), fuera de la línea de simetría. El producto de sus
cociclos Euler conserva coeficientes Jordan no negativos en el semiplano
de convergencia absoluta; sus cocientes Gamma conservan representaciones
Beta positivas allí.

Sea \(Y_a(s)=Y(s+a)Y(s-a)\) y

\[
 \mathcal S_u^{(a)}(s)={Y_a(s-u)\over Y_a(s)}.       \tag{26}
\]

Si \(0<\varepsilon<a\), un cero de \(Y_a\) con parte real
\(1/2+a\) se transforma mediante

\[
 z={s-1-\varepsilon\over s-\varepsilon}             \tag{27}
\]

en un punto de \(|z|<1\). Para todo \(u\) fuera de un conjunto discreto,
el numerador de (26) no lo cancela; la serie de Taylor correspondiente
tiene radio \(R<1\).

Supóngase que los coeficientes de

\[
 -{\mathcal S_u^{(a)}(s_\varepsilon(z))-1
       \over u(1-z)}                                 \tag{28}
\]

fueran eventualmente no negativos, como exigiría una deducción estructural
del signo \(g_n\le0\). Tras restar un polinomio y dividir por una potencia
de \(z\), el teorema de Pringsheim forzaría una singularidad en el punto
real positivo \(z=R\). No existe: para \(0<z<1\),
\(s_\varepsilon(z)>1\) y los factores completados desplazados son reales,
positivos y no nulos. La singularidad real en \(z=1\) no ayuda, porque
\(R<1\). Aplicar el mismo argumento al negativo de (28) excluye también
eventual no positividad. Como los coeficientes son reales, hay infinitos
positivos e infinitos negativos.

**Alcance exacto.** La serie positiva del factor desplazado converge solo
en un semiplano derecho, no en todo el disco de (27). Por ello este
argumento refuta una continuación del signo basada únicamente en
``Jordan positivo + Beta positiva + ecuación funcional''. No refuta un
teorema aritmético nuevo que use información cuantitativa especial de los
pesos reales de \(\zeta\) dentro de la zona crítica. Para un
\(\varepsilon\) fijo, exigir holomorfía en todo ese disco solo excluye ceros
con \(\Re\rho>1/2+\varepsilon\). Exigirla para **todo**
\(\varepsilon\downarrow0\), con \(u\) genérico para evitar cancelaciones,
y usar la simetría funcional fuerza RH; la contractividad global es un
input aún más fuerte.

## 8. Stop-gate theta ya existente

El carácter cuadrático tampoco rescata positividad término a término en la
representación theta. `103_49` parte del mismo \(Y\) y de los coeficientes
positivos de \(\zeta(s)^2\), pero al transferir el factor
\(s(s-1)^2\) a la densidad aparece

\[
 2x(4x^2-16x+9)e^{-x},                              \tag{29}
\]

que es negativo para

\[
 2-\frac{\sqrt7}{2}<x<2+\frac{\sqrt7}{2}.           \tag{30}
\]

Así, el packaging branch-free no abre una ruta de positividad que el repo
hubiera omitido: (23) es la versión finita de la misma pérdida de signo.

## 9. Veredicto operativo

El ataque produce dos teoremas reutilizables: la expansión (16) y el límite
(21). También demuestra tres obstrucciones:

1. la medida polar es firmada para todo \(c>0\), ecuación (23);
2. separar canales crea divergencias de orden \(\varepsilon^{-1}\),
   ecuación (24);
3. Jordan/Beta/ecuación funcional no fuerzan el signo Cayley, por (25)--(28).

Por tanto se descarta la inferencia inmediata
``Jordan positivo + Beta positiva + cuadrado polar real'' como prueba de
A1. **No** se descarta el cociclo global: un teorema acoplado que explote
una propiedad cuantitativa nueva y exclusiva de \(J_u\), \(b_u\) o
\(\Lambda\) antes de separar los tres canales sigue abierto. `104_20`
desarrolla exactamente esa continuación y localiza su gate global.

El verificador `tools/three_channel_cocycle_check.py` comprueba con
aritmética `Fraction` la fórmula (9), la transformada (23) y el coeficiente
(24). No verifica A1.
