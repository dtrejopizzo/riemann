# 104_10 — M1: núcleo colectivo max(i,j)

**Estado:** preregistro ejecutado; la versión local-PSD de M1 queda descartada con testigos
exactos. La versión global también queda cerrada como mecanismo: `104_11` prueba que el
compensador es la energía del mismo kernel `max` y que las dos Hessianas se cancelan
idénticamente, incluido el borde finito. No se prueba A1 ni RH.

## 1. Meta e implicación

Se fija \(\theta=1/4\). M1 no ataca A1 directamente: intenta probar la condición suficiente
más fuerte

\[
 \Delta D_n\ge0,\qquad D_n=2\lambda_n-A_n,\qquad n\ge149.
\tag{1}
\]

Como \(D_{149}>0\) está certificado en 103_51, (1) implicaría \(D_n>0\) para todo
\(n\ge149\), luego el strong margin \(\lambda_n\ge A_n/2\), A1 con A0 y finalmente RH. La
implicación es correcta, pero 103_59 ya prueba que (1) es estructuralmente más fuerte que RH
para funciones enteras simétricas generales.

## 2. Axiomas e inputs

Cada uso de M1 debe declarar cuál de estos niveles emplea.

**Nivel algebraico finito.**

1. \(q_1<\cdots<q_M\) son números reales \(>1\).
2. \(\ell_j>0\), \(\Psi_j=\sum_{i\le j}\ell_i\), y
   \(d_j=q_j-1-\Psi_{j-1}-\ell_j/2\).
3. \(w_1,\ldots,w_M\) son números reales arbitrarios.

**Nivel aritmético regulado.**

4. \(q_j\) recorre las potencias primas y \(\ell_j=\Lambda(q_j)\).
5. Para \(n\ge0,\varepsilon>0\),
   \[
   \tau(x)=x^{-1-\varepsilon}L_n(\log x),\qquad w(x)=\tau'(x),
   \qquad E(x)=\psi(x)-x+1.
   \tag{2}
   \]
6. Solo se usa PNT para hacer desaparecer el borde al enviar \(X\to\infty\) con
   \(\varepsilon>0\). No se usa la tripla PNT efectiva declarada en 104_01.

El dato especial del nivel 4 no puede sustituirse por «medida atómica positiva»: ésa sería una
relajación estricta y 103_59 ya muestra que el transporte resultante tiene ambos signos.

## 3. Identidad finita regulada, con el borde que faltaba

Sea \(X>1\) que no sea potencia prima, y defínase

\[
 C_{n,\varepsilon}(X):=-\int_1^X E(x)\tau'(x)\,dx,\qquad
 G(X)=\int_1^X E(t)\,dt.
\tag{3}
\]

Póngase

\[
 \mathcal H(X)=\sum_{q_j\le X}\ell_j(q_j-1)-{\psi(X)^2\over2}.
\tag{4}
\]

Como se prueba en 103_67,

\[
 \mathcal H(X)=-G(X)-{E(X)^2\over2},\qquad
 d\mathcal H=\sum_j\ell_jd_j\delta_{q_j}.
\tag{5}
\]

Dos integraciones por partes **en el intervalo finito** dan

\[
 \boxed{
 C_{n,\varepsilon}(X)
 =\sum_{q_j<X}\ell_jd_jw(q_j)
  -{1\over2}\int_1^X E(x)^2\tau''(x)\,dx
  +{1\over2}E(X)^2w(X).}
\tag{6}
\]

*Prueba.* De \(G'=E\),
\[
 C(X)=-G(X)w(X)+\int_1^XG(x)\tau''(x)\,dx.
\]
Insertando \(G=-\mathcal H-E^2/2\) e integrando
\(-\int\mathcal H\tau''\) en sentido de Stieltjes aparece
\(-\mathcal H(X)w(X)+\int w\,d\mathcal H\). Por (5), los dos bordes suman
\(-[G(X)+\mathcal H(X)]w(X)=E(X)^2w(X)/2\), y resulta (6). \(\square\)

El último término de (6) es obligatorio en toda truncación. Para
\(\varepsilon>0\) tiende a cero al enviar \(X\to\infty\), y se recupera la identidad de
103_67:

\[
 C_{n,\varepsilon}
 =\sum_j\ell_jd_jw_j-{1\over2}\int_1^\infty E(x)^2\tau''(x)\,dx.
\tag{7}
\]

Separar los dos términos de (7) y tomar valores absolutos está prohibido: su integración por
partes inversa reconstruye exactamente \(C_{n,\varepsilon}\).

## 4. Identidad max(i,j) y todos los bordes discretos

En el nivel algebraico finito,

\[
 \boxed{
 \sum_{j=1}^M\ell_jd_jw_j
 =\sum_{j=1}^M\ell_j(q_j-1)w_j
  -{1\over2}\sum_{i,j\le M}\ell_i\ell_jw_{\max(i,j)}.}
\tag{8}
\]

Sea
\[
 H_j=\sum_{i\le j}\ell_i(q_i-1)-{\Psi_j^2\over2},\qquad H_0=0.
\tag{9}
\]
Entonces, sin límite implícito,
\[
 \boxed{
 \sum_{j=1}^M\ell_jd_jw_j
 =\sum_{j=1}^{M-1}H_j(w_j-w_{j+1})+H_Mw_M.}
\tag{10}
\]

El término \(H_Mw_M\) es el borde discreto. Escribir solamente
\(\sum H_j(w_j-w_{j+1})\) en un prefijo finito es incorrecto.

### Descomposición exacta por bloques

Sea \(0=m_0<m_1<\cdots<m_B=M\), \(I_b=(m_{b-1},m_b]\),
\[
 P_{b-1}=\sum_{i\le m_{b-1}}\ell_i,\qquad
 L_{b,k}=\sum_{m_{b-1}<i\le k}\ell_i,\qquad L_b=L_{b,m_b}.
\tag{11}
\]
La forma cuadrática de (8) se descompone exactamente como
\[
 \begin{split}
 {1\over2}\sum_{i,j\le M}\ell_i\ell_jw_{\max(i,j)}
 =\sum_{b=1}^B\Bigg\{&
 P_{b-1}\sum_{j\in I_b}\ell_jw_j
 +{w_{m_b}\over2}L_b^2\\
 &+{1\over2}\sum_{k=m_{b-1}+1}^{m_b-1}
 (w_k-w_{k+1})L_{b,k}^2\Bigg\}.
 \end{split}
\tag{12}
\]

*Prueba.* Dentro de un bloque,
\[
 w_{\max(i,j)}
 =w_{m_b}+\sum_{k=\max(i,j)}^{m_b-1}(w_k-w_{k+1}).
\]
Sumar en \(i,j\in I_b\) da los dos últimos términos de (12). Si \(i\) está en un
bloque anterior y \(j\in I_b\), entonces \(w_{\max(i,j)}=w_j\); las dos orientaciones del par
cancelan el factor \(1/2\) y dan el primer término. \(\square\)

Para una sucesión infinita globalmente no creciente con límite \(w_\infty\),
\[
 w_{\max(i,j)}
 =w_\infty+\sum_{k\ge\max(i,j)}(w_k-w_{k+1}).
\tag{13}
\]
Así, la forma es PSD si \(w_\infty\ge0\) y todas las diferencias son no negativas. En el
kernel real \(w=\tau'\), \(w_\infty=0\), pero \(w\) alterna monotonía: (13) no da PSD global.

## 5. No-go exacto para la estrategia local-PSD

La frase «cada bloque decreciente da una forma PSD» omite tres términos que deciden el signo:

1. el rango uno \(w_{m_b}L_b^2/2\), que es negativo si \(w_{m_b}<0\);
2. los términos de cruce
   \(P_{b-1}\sum_{j\in I_b}\ell_jw_j\), sin signo;
3. los bloques crecientes, donde \(w_k-w_{k+1}<0\).

Por (10), conservar juntos el primer momento y la forma max no elimina el problema: los
colapsa al correlador firmado \(H_j(w_j-w_{j+1})\). Y \(H_j\) tampoco tiene signo fijo para
los pesos **reales** de von Mangoldt.

La herramienta tools/m1_cumulative_sign_certificate.py usa solo aritmética racional outward
para los logaritmos de los primos y certifica
\[
 \boxed{H(2969)<-21,\qquad H(3167)>110.}
\tag{14}
\]
Aquí \(H(x)=\sum_{q\le x}\Lambda(q)(q-1)-\psi(x)^2/2\). Por tanto ni una orientación global
de \(H\), ni una orientación global de \(w_j-w_{j+1}\), ni PSD por bloques puede probar (7).

**Veredicto M1-local:** descartado con el testigo (12)–(14). Una suma global entre bloques
podría todavía cancelar, pero eso exige una desigualdad correlacionada nueva; no es
consecuencia de PSD.

## 6. Falsificadores y alcance correcto

### 6.1 Falsificador de relajaciones aritméticas

Si un paso usa solo los axiomas 1–3 (átomos positivos ordenados), se le aplica el movimiento
de una masa \(W\) de \(b\) a \(a<b\) de 103_59:
\[
 \delta C=W\{\tau(a)-\tau(b)\}.
\tag{15}
\]
Para \(n=1\) el kernel tiene un cero explícito y (15) toma ambos signos. Satisface exactamente
los axiomas algebraicos relajados y mata cualquier conclusión basada solo en positividad,
monotonía de la función de conteo o soporte atómico.

### 6.2 Falsificador espectral

Si un paso deja de usar el nivel 4 y usa solo simetría funcional/localización crítica, se
aplica
\[
 X(s)=\left(s-\tfrac12\right)^2+\tfrac14.
\tag{16}
\]
Todos sus ceros están sobre la línea, pero \(\Delta\lambda_2[X]=-2\). Esto mata cualquier
derivación de (1) desde RH o desde cuadrados por cero individual.

El cuarteto off-line
\[
 8-8\cosh(n\alpha)\cos(n\vartheta)
\tag{17}
\]
se usa de igual modo contra pasos que retengan solo conjugación y ecuación funcional.

### 6.3 Límite lógico del requisito «mismos axiomas»

El nivel 4 fija literalmente \(q=p^k\) y \(\ell=\log p\): fija la aritmética de \(\zeta\).
Un «divisor off-line» que satisfaga también ese mismo axioma sería la propia \(\zeta\) con un
cero off-line, cuya existencia es justamente la cuestión. Por eso (17) **no puede exigirse**
francamente como modelo que satisfaga el nivel 4 sin presuponer la negación de RH.

La regla válida es: cada vez que una estimación relaje el nivel 4, debe pasar el falsificador
correspondiente a los axiomas que realmente conserve. Un argumento que use una propiedad
cuantitativa especial de los pesos reales no queda refutado por (15)–(17), pero debe declarar
y demostrar esa propiedad.

## 7. Correlador global: stop-gate posterior

Después del no-go local, quedaba planteado probar directamente y uniformemente
\[
 \limsup_{\varepsilon\downarrow0}
 \left[
 \sum_j H_j(w_j-w_{j+1})
 -{1\over2}\int_1^\infty E(x)^2\tau''(x)\,dx
 \right]
 \le {1\over2}\Delta A_n,\qquad n\ge149,
\tag{18}
\]
con el borde de (6) controlado antes de cada límite.

`104_11`, Teoremas 1--2, identifica el segundo término y su borde con la energía
`max` de \(d\psi-dx\). Al sumarlo al primer término, la componente cuadrática se
cancela exactamente y (18) vuelve a

\[
 -\int_1^\infty E(x)\tau'(x)\,dx\le {1\over2}\Delta A_n.
\]

Por tanto (18) no es una versión global viva de M1: es el objetivo lineal de
primera diferencia sin coercividad residual. Probarlo seguiría siendo suficiente
para A1, pero ya no sería una consecuencia del mecanismo `max`. M1 queda
descartado; el sucesor se registra en `104_11` y se desarrolla separadamente.

## Estado

| ítem | resultado |
|---|---|
| identidad regulada finita con borde | probada, (6) |
| identidad max y borde \(H_Mw_M\) | probada, (8)–(10) |
| bloques, cruces y rango uno | probados, (12) |
| PSD global | falso para el \(w\) oscilatorio |
| signo de \(H\) real | falso, certificado (14) |
| M1 local-PSD | descartado |
| Hessiana global de (18) | nula exactamente, con borde (`104_11`) |
| M1 global | descartado: colapsa al funcional lineal original |
| A1/RH | no probada |
