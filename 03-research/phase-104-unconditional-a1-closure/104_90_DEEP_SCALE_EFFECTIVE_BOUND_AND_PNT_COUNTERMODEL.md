# 104_90 — Cota efectiva de la escala Deep y contra-modelo PNT

**Resultado.** La información incondicional formada por una altura
verificada \(H\), una región libre de ceros de Vinogradov--Korobov y el
conteo efectivo de ceros controla el observable profundo solo hasta

\[
 \boxed{\limsup_{X\to\infty}\mathcal D_X(\lambda)\le{1\over2}.} \tag{1}
\]

No produce el límite cero de 104_75. Con \(H=3\cdot10^{12}\), la misma
estimación hace vacío el evento, salvo la contabilidad de constantes
menores, hasta la escala \(X\asymp4H^4=3.24\cdot10^{50}\). Después queda
asintóticamente sin controlar la mitad de la masa armónica.

Se construye además un contra-modelo explícito que conserva coeficientes
Euler no negativos sobre potencias de primos ordinarios, un PNT continuo
con error de tipo VK, y un completamiento entero con ecuación funcional,
pero tiene ceros fuera de la línea y densidad Deep positiva. El modelo
introduce polos Euler adicionales y cambia los pesos de la torre \(7^k\).
Por tanto no es un contraejemplo a RH ni a los axiomas exactos de la zeta.
Sí prueba que PNT, positividad, soporte primo y una ecuación funcional
amplia no sustituyen los valores literales
\(\Lambda(p^k)=\log p\).

Este documento no prueba Deep-\(\Lambda\), A1 ni RH. Cierra el ataque
basado solo en la escala radial de los ceros y en consecuencias PNT de los
pesos.

---

## 1. Desplazamiento radial sobre una altura verificada

Sea \(\rho=\beta+i\gamma\), \(\gamma>0\), con
\(1/2\le\beta<1\), representante de una órbita funcional. Ponga

\[
 a(\beta,\gamma)
 =\log\left|{\rho\over\rho-1}\right|
 ={1\over2}\log{\beta^2+\gamma^2
                 \over(1-\beta)^2+\gamma^2}.            \tag{2}
\]

Si una región libre de ceros da
\(\beta\le1-\delta(\gamma)\), entonces

\[
 a(\beta,\gamma)
 \le a_{\rm VK}(\gamma)
 :={1\over2}\log\left(
 1+{1-2\delta(\gamma)\over
       \gamma^2+\delta(\gamma)^2}\right).               \tag{3}
\]

Suponga que todos los ceros con \(|\gamma|\le H\) están certificados en
la línea, y defina

\[
 a_H=\sup_{\gamma>H}a_{\rm VK}(\gamma).
\]

La cota universal de 104_76 da

\[
 \boxed{a_H<{1\over2H^2}.}                              \tag{4}
\]

Aunque \(a_H\) sea diminuto, es fijo, y el factor \(e^{a_Hn}\) acaba
superando toda barrera \(e^{o(n)}\).

## 2. Cota efectiva para los coeficientes de Li

El conteo numérico de 103_58, §2, es

\[
 \mathcal N(T)\le25T\log T\qquad(T\ge10),               \tag{5}
\]

donde se cuentan ambos signos de las ordenadas y las multiplicidades.
Para \(n\ge\max(5,H/2)\), parta las órbitas en
\(H<\gamma\le2n\) y \(\gamma>2n\).

En la primera franja hay a lo sumo \(50n\log(2n)\) etiquetas. La identidad
de cuarteto de 104_76 y (3) dan

\[
 |q_n(\rho)|\le4(1+e^{a_Hn}),                            \tag{6}
\]

y un costo total no mayor que

\[
 200n\log(2n)(1+e^{a_Hn}).                               \tag{7}
\]

Para \(\gamma>2n\), la expansión corta de la fase da

\[
 |q_n(\rho)|\le {9n^2\over\gamma^2}.                    \tag{8}
\]

La sumación parcial de (5) implica

\[
 \sum_{|\gamma|>2n}{m_\rho\over\gamma^2}
 \le {25\{\log(2n)+1\}\over n},                         \tag{9}
\]

de modo que la segunda franja cuesta a lo sumo
\(225n\{\log(2n)+1\}\). Los ceros hasta \(H\) contribuyen no
negativamente. Reuniendo y redondeando hacia arriba,

\[
 \boxed{
 \lambda_n\ge
 -500n\{\log(2n)+1\}(1+e^{a_Hn}).}                     \tag{10}
\]

No se ha usado el signo de ningún cero no verificado.

Para \(n<H/2\), todos los ceros no verificados ya están en la franja
\(|\gamma|>2n\). La misma sumación parcial, ahora desde \(H\), da

\[
 \lambda_n\ge
 -{450n^2\{\log H+1\}\over H}.                          \tag{10a}
\]

Este prefijo es finito y su costo crece solo polinomialmente; por ello no
puede cruzar \(-e^{\sqrt X}\) una vez \(X\) es suficientemente grande.

## 3. Consecuencia para el evento profundo

Recuerde

\[
 \mathcal D_X(\lambda)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf1_{\{\lambda_n+\log(n+1)\le-e^{\sqrt X}\}}.    \tag{11}
\]

Para \(X\) suficientemente grande, (10)--(10a) muestran que todo índice
contado en (11) debe satisfacer

\[
 n\ge L_H(X):=
 {\sqrt X-\log[2000X\{\log(2X)+1\}]\over a_H}.          \tag{12}
\]

Si \(L_H(X)>X\), el evento es vacío. En caso contrario,

\[
 \mathcal D_X(\lambda)
 \le {H_X-H_{\lceil L_H(X)\rceil-1}\over H_X}.          \tag{13}
\]

Como \(a_H\) es fijo,

\[
 \log L_H(X)={1\over2}\log X-\log a_H+o(\log X),       \tag{14}
\]

y (1) sigue de (13). La constante \(1/2\) es óptima para la sola
información radial puntual (10): la sucesión adversarial
\(-e^{a_Hn}\) la alcanza. No se afirma que sea óptima dentro de la clase
mucho más rígida de funciones zeta genuinas. Un solo cuarteto exterior
fijo permitido por esos inputs ya produce densidad positiva; eso basta
para probar que no pueden dar el límite cero.

Con \(H=3\cdot10^{12}\), (4) da

\[
 a_H<5.556\cdot10^{-26},
 \qquad L_H(X)\sim1.8\cdot10^{25}\sqrt X.              \tag{15}
\]

El cambio \(L_H(X)\approx X\) ocurre alrededor de
\(X\approx3.24\cdot10^{50}\). Esta es una escala diagnóstica, no un
rango certificado: un umbral literal debe conservar los términos
logarítmicos de (12) y todas las constantes de la región libre elegida.

## 4. Contra-modelo continuo con PNT

Use el modelo reticular exterior de 104_78,

\[
 Z_-(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},
 \qquad Z_-(T)=Z_-\!\left({1\over6T}\right),            \tag{16}
\]

y subordínelo a la torre del primo \(7\):

\[
 T(s)=\sqrt{7\over6}\,7^{-s},
 \qquad W(s)=Z_-(T(s)),
 \qquad F(s)=\zeta(s)W(s).                              \tag{17}
\]

La derivada logarítmica adicional vive solo en \(7^\ell\):

\[
 -{W'(s)\over W(s)}
 =\sum_{\ell\ge1}{b(7^\ell)\over7^{\ell s}},           \tag{18}
\]

\[
 \boxed{
 b(7^\ell)=\log7\left({7\over6}\right)^{\ell/2}
 (6^\ell+1-3^\ell-2^\ell)>0.}                          \tag{19}
\]

La positividad es exacta porque

\[
 6^\ell+1-3^\ell-2^\ell=(3^\ell-1)(2^\ell-1).         \tag{20}
\]

Además,

\[
 \sum_{7^\ell\le x}b(7^\ell)=O(x^\sigma),
 \qquad
 \sigma={\log42\over2\log7}=0.960391\ldots<1.          \tag{21}
\]

Por ello

\[
 \psi_F(x)=x+O\!\left(xe^{-\eta(x)}+x^\sigma\right),   \tag{22}
\]

que conserva asintóticamente un error de tipo VK, tras ajustar el umbral
y la constante.

Escriba

\[
 r(s)={1\over2}+{\log7\over\log6}
                   \left(s-{1\over2}\right).           \tag{23}
\]

Como \(T(s)=6^{-r(s)}\), el completamiento

\[
 \xi(s)\,\Xi_-(r(s)),
 \qquad \Xi_-(r)=6^r-5+6^{1-r},                        \tag{24}
\]

es entero y es invariante bajo \(s\mapsto1-s\). Sus ceros exteriores
tienen partes reales

\[
 \boxed{
 {1\over2}\pm{\log(3/2)\over2\log7}
 =0.395816\ldots,\ 0.604184\ldots.}                    \tag{25}
\]

La secuencia de Li correspondiente tiene, por tanto, excursiones
exponenciales y densidad Deep positiva.

### Alcance preciso

El factor Euler \(W\) tiene polos adicionales en las familias verticales
con partes reales \(\sigma\) y \(1-\sigma\); el factor
\(\Xi_-(r(s))\) los cancela en el completamiento. El modelo tampoco
conserva el factor Gamma exacto ni los valores \(\Lambda(7^\ell)\).
En consecuencia,

\[
 \begin{gathered}
 \text{PNT/VK + pesos no negativos + soporte primo + FE amplia}
 \not\Longrightarrow \mathrm{RH},\\
 \text{pero el modelo no satisface los datos exactos completos de }\zeta.
 \end{gathered}                                         \tag{26}
\]

## 5. Veredicto

La escala \(e^{\sqrt X}\) no vuelve elemental el límite Deep. Solo mueve
la obstrucción a alturas \(\gamma\lesssim X^{1/4}\), como probó 104_76.
Una altura verificada fija deja finalmente la mitad de la masa armónica
sin decidir. Incluso un PNT continuo muy fuerte no elimina un factor
exterior si se permiten cambios positivos en una sola torre prima.

El sucesor, si existe, debe utilizar conjuntamente los valores exactos de
todas las torres ordinarias; ni la escala radial, ni PNT, ni la positividad
de los pesos pueden suministrarlo por separado.

## 6. Reproducción

Desde el directorio tools:

    python3 deep_scale_pnt_countermodel_check.py

El checker verifica la ecuación funcional racional, la factorización
positiva de cada altura añadida, el exponente \(\sigma<1\), las partes
reales exteriores y las escalas numéricas para \(H=3\cdot10^{12}\).
