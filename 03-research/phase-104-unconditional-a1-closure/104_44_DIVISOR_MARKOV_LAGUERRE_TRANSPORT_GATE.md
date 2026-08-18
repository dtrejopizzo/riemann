# 104_44 — Transporte divisor–Markov y gate de escala Laguerre

**Estado.** La identidad exacta

\[
 \Lambda*1=\log
\tag{1}
\]

sí define un transporte multiplicativo positivo que conserva conjuntamente
todos los primos, todas sus potencias y la fase del test. Si \(N\) se elige con
peso \((\log N)N^{-s}\), el divisor \(D\mid N\) elegido con probabilidad
\(\Lambda(D)/\log N\) tiene exactamente la ley von Mangoldt, y el cociente
\(N/D\) es independiente con ley zeta. La fórmula de adición de Laguerre da
entonces una convolución exacta en el grado, sin desigualdad triangular.

El transporte, sin embargo, no aporta la coercividad proporcional que falta:

1. su contracción de Markov tiene brecha espectral exactamente cero, aun en el
   subespacio de media cero;
2. invertir la convolución exacta en el grado es precisamente inversión de
   Möbius, ya auditada en `104_12`;
3. el análogo continuo polo–Gamma contrae el grado \(r\) por
   \(1/\sqrt{r+1}\), pero solamente en la base escalada
   \(L_r((s-1)x)\); expresar el kernel no escalado de A1 en esa base tiene
   carga absoluta \((2/(s-1)-1)^r\), que para \(s-1=1/n\) es
   \(\exp((1+o(1))n\log n)\).

Por tanto queda descartado como mecanismo autónomo el siguiente argumento:
«usar (1), contracción de esperanza condicional y la adición de Laguerre para
obtener una cota proporcional». Una estimación especial sobre el **vector fijo
no escalado**, sin invertir positivamente ni separar los grados, seguiría siendo
matemática nueva; el transporte no la refuta, pero tampoco la suministra. No se
prueba \(B_n\le(1501/2002)A_n\), A1 ni RH.

## 1. Auditoría de no duplicación

`103_70` aplica Vaughan/Heath--Brown y prueba que las variables de
factorización entran en la fase solo por la suma de sus logaritmos. También
registra la adición de Laguerre, pero no la interpreta como una desintegración
de probabilidad.

`104_12` usa la identidad dual \(\Lambda=\mu*\log\), obtiene la convolución
firmada en el grado y descarta un adjunto positivo para Möbius. `104_13` prueba
que Selberg--Riccati pierde la colisión polo--primos si se estima por piezas.
`104_35` y `104_38` conservan el canal primo--polo y demuestran que el cuadrado
Selberg canónico se cancela exactamente o deja diagonal negativa.

Lo nuevo aquí es más estrecho:

* la desintegración Markov canónica asociada a \(\Lambda*1=\log\);
* su análogo continuo exacto como partición uniforme de una Gamma(2);
* la demostración de brecha cero mediante átomos en primos reales;
* la cuantificación exacta del costo de cambiar de la escala natural
  \((s-1)x\) a la escala Laguerre de A1.

No se reabre Vaughan, no se postula positividad de Möbius y no se usa un
cuadrado Selberg.

## 2. Desintegración multiplicativa exacta

Fijemos \(s>1\) y escribamos

\[
 Z_s=\zeta(s),\qquad
 \mathcal L_s=-{\zeta'(s)\over\zeta(s)}
             =\sum_{d\ge2}{\Lambda(d)\over d^s}.
\tag{2}
\]

Definamos dos probabilidades

\[
 \nu_s(d)={\Lambda(d)d^{-s}\over\mathcal L_s},\qquad
 \eta_s(k)={k^{-s}\over Z_s}.
\tag{3}
\]

Sean \(D\sim\nu_s\), \(K\sim\eta_s\) independientes y \(N=DK\).

**Teorema 2.1 (transporte divisor–Markov).** La ley de \(N\) es

\[
 \boxed{
 \Pi_s(N)={ (\log N)N^{-s}\over-\zeta'(s)}}
 \qquad(N\ge2),
\tag{4}
\]

y su desintegración inversa es

\[
 \boxed{
 \mathbb P_s(D=d\mid N)
 ={\Lambda(d)\over\log N}\,\mathbf1_{d\mid N}.}
\tag{5}
\]

**Prueba.** Para cada \(N\ge2\), (1) da

\[
\begin{aligned}
 \mathbb P(DK=N)
 &=\sum_{d\mid N}{\Lambda(d)d^{-s}\over\mathcal L_s}
                  {(N/d)^{-s}\over Z_s}\\
 &={N^{-s}\over\mathcal L_sZ_s}\sum_{d\mid N}\Lambda(d)
 ={(\log N)N^{-s}\over-\zeta'(s)}.
\end{aligned}
\]

Dividir la masa conjunta por (4) prueba (5). \(\square\)

El operador divisor y su adjunto multiplicativo son

\[
 (\mathsf T_sf)(N)
 ={1\over\log N}\sum_{d\mid N}\Lambda(d)f(d),
\tag{6}
\]

\[
 (\mathsf P_sF)(d)
 ={1\over Z_s}\sum_{k\ge1}{F(dk)\over k^s}.
\tag{7}
\]

Por construcción,

\[
 \langle \mathsf T_sf,F\rangle_{L^2(\Pi_s)}
 =\langle f,\mathsf P_sF\rangle_{L^2(\nu_s)},
 \qquad \mathsf T_s1=\mathsf P_s1=1,
\tag{8}
\]

y Jensen da

\[
 \boxed{
 \|\mathsf T_sf\|_{L^2(\Pi_s)}
 \le\|f\|_{L^2(\nu_s)}.}
\tag{9}
\]

Esta es una contracción genuina que usa los pesos canónicos completos; la
cuestión decisiva es si contiene una brecha estricta.

## 3. La brecha de Markov es exactamente cero

Sea \(p\) primo y

\[
 e_p(d)=\mathbf1_{d=p},\qquad
 q_p=\nu_s(p)={ (\log p)p^{-s}\over\mathcal L_s}.
\tag{10}
\]

De (6),

\[
 (\mathsf T_se_p)(N)
 ={\log p\over\log N}\mathbf1_{p\mid N}.
\tag{11}
\]

Una suma directa usando (4) da

\[
 {\|\mathsf T_se_p\|_{L^2(\Pi_s)}^2
  \over\|e_p\|_{L^2(\nu_s)}^2}
 =R_p(s):={1\over Z_s}\sum_{k\ge1}{k^{-s}\log p
                              \over\log p+\log k}.
\tag{12}
\]

Cada sumando de (12) está entre cero y \(k^{-s}/Z_s\), y para \(k\) fijo
su factor logarítmico tiende a uno cuando \(p\to\infty\). Por convergencia
dominada,

\[
 \boxed{\lim_{p\to\infty}R_p(s)=1.}
\tag{13}
\]

Esto también ocurre después de retirar las constantes. En efecto, para

\[
 f_p=e_p-q_p
\]

se tiene \(\langle f_p,1\rangle_{\nu_s}=0\) y

\[
 {\|\mathsf T_sf_p\|_2^2\over\|f_p\|_2^2}
 ={R_p(s)-q_p\over1-q_p}\longrightarrow1,
\tag{14}
\]

porque \(q_p\to0\). Junto con (9), esto prueba

\[
 \boxed{
 \|\mathsf T_s\|_{L^2_0(\nu_s)\to L^2_0(\Pi_s)}=1.}
\tag{15}
\]

Por tanto no existe \(\delta_s>0\) tal que

\[
 \|\mathsf T_sf\|_2^2
 \le(1-\delta_s)\|f\|_2^2
 \qquad(f\perp1).
\tag{16}
\]

El testigo usa primos verdaderos y el peso exacto \(\log p\); no es una
perturbación de la medida aritmética. La razón geométrica es que la fila
condicional de un padre primo es determinista.

La ecuación (15) descarta una brecha en la **coordenada operatorial**. No
descarta que una sucesión especial de vectores tenga un cociente menor que
uno; tal afirmación tendría que demostrarse directamente para esa sucesión.

## 4. Adición de Laguerre sin triángulos

Para \(j\ge0\), póngase

\[
 p_j(s)=\sum_{d\ge2}{\Lambda(d)\over d^s}L_j(\log d),
 \qquad
 z_j(s)=\sum_{k\ge1}{1\over k^s}L_j(\log k),
\tag{17}
\]

y

\[
 b_N(s)=\sum_{m\ge2}{\log m\over m^s}
                         L_N^{(1)}(\log m).
\tag{18}
\]

Todas las series convergen absolutamente. La fórmula

\[
 L_N^{(1)}(x+y)=\sum_{j=0}^NL_j(x)L_{N-j}(y)
\tag{19}
\]

y la ley conjunta de la Sección 2 dan, sin módulos,

\[
 \boxed{b_N(s)=\sum_{j=0}^Np_j(s)z_{N-j}(s).}
\tag{20}
\]

Con \(t=z/(1-z)\), (20) equivale a

\[
 { -\zeta'(s+t)\over(1-z)^2}
 =\left{{\mathcal L(s+t)\over1-z}\right}
  \left{{\zeta(s+t)\over1-z}\right}.
\tag{21}
\]

Esta es exactamente \(-\zeta'=\mathcal L\zeta\). Despejar los momentos
von Mangoldt en (20) exige dividir por la segunda llave de (21), es decir,
introducir \(1/\zeta\). Coeficiente a coeficiente esto es la inversión
Möbius de `104_12`, no un inverso Markov positivo. Mantener (20) completa
preserva todos los signos, pero entonces una cota para su factor
\(p_j\) sigue siendo el nuevo input buscado.

## 5. Análogo continuo: dónde sí aparece la coercividad

Sea \(\varepsilon=s-1>0\). El análogo del polo toma \(X,Y\) independientes
con ley exponencial

\[
 \varepsilon e^{-\varepsilon x}\,dx,
\]

y pone \(U=X+Y\). Entonces \(U\) tiene densidad

\[
 \varepsilon^2u e^{-\varepsilon u}\,du,
\tag{22}
\]

y \(X\mid U=u\) es uniforme en \([0,u]\). Por tanto

\[
 (\mathsf C_\varepsilon f)(u)={1\over u}\int_0^u f(x)\,dx
\tag{23}
\]

es el análogo exacto de (6).

Para el grado escalado

\[
 f_r(x)=L_r(\varepsilon x),
\]

la identidad integral de Laguerre da

\[
 \boxed{
 (\mathsf C_\varepsilon f_r)(u)
 ={1\over r+1}L_r^{(1)}(\varepsilon u).}
\tag{24}
\]

Las ortogonalidades de Laguerre implican

\[
 \|f_r\|_{L^2(\mathrm{Exp}(\varepsilon))}^2=1,
 \qquad
 \|\mathsf C_\varepsilon f_r\|_{L^2(\Gamma(2,\varepsilon))}^2
 ={1\over r+1}.
\tag{25}
\]

Así el continuo posee exactamente la coercividad por grado que uno querría
transportar. El problema es que A1 no usa \(L_r(\varepsilon x)\), sino el
grado no escalado \(L_r(x)\). El test asociado satisface
\(L_{n-1}^{(1)}=\sum_{r=0}^{n-1}L_r\); por eso el problema de escala ya está
presente en cada componente ordinaria. No se afirma que puedan estimarse
esas componentes por separado: hacerlo sería precisamente perder su
cancelación relativa.

### 5.1 Forma firmada conjunta con el polo

El transporte discreto y el continuo pueden combinarse antes de estimar.
Para \(n\ge1\), defina el mismo canal completo de `104_41`, ahora con
\(s=1+\varepsilon\):

\[
\begin{aligned}
 \mathcal B_{n,s}:={}&s\sum_{m\ge2}{\Lambda(m)\over m^s}
       L_{n-1}^{(1)}(s\log m)\\
 &-s\int_1^\infty y^{-s}L_{n-1}^{(1)}(s\log y)\,dy .
\end{aligned}
\tag{25a}
\]

Poniendo \(f_{n,s}(x)=L_{n-1}^{(1)}(sx)\), las dos desintegraciones dan la
identidad exacta

\[
 \boxed{
 \mathcal B_{n,s}
 =s\left\{
  \mathcal L_s\,\mathbb E_{\Pi_s}[\mathsf T_sf_{n,s}]
  -{1\over\varepsilon}
       \mathbb E_{\Gamma(2,\varepsilon)}
                    [\mathsf C_\varepsilon f_{n,s}]
 \right\}.}
\tag{25b}
\]

En efecto, las esperanzas condicionales de (25b) recuperan respectivamente
\(\mathbb E_{\nu_s}f_{n,s}\) y
\(\mathbb E_{\mathrm{Exp}(\varepsilon)}f_{n,s}\); la segunda integral de
(25a), tras \(y=e^x\), es
\(\varepsilon^{-1}\mathbb E_{\mathrm{Exp}(\varepsilon)}f_{n,s}\).
Por `104_41`,

\[
 \lim_{s\downarrow1}\mathcal B_{n,s}=B_n=A_n-\lambda_n.
\tag{25c}
\]

Las ecuaciones (25a)--(25c) conservan en una sola resta primos, potencias
primas, polo y fase. No autorizan a estimar las dos esperanzas por separado:
ambas tienen términos divergentes cuando \(\varepsilon\downarrow0\), y la
finitud está en su colisión firmada. La contracción (9) actúa dentro de la
primera probabilidad y (25) dentro de la segunda; no compara sus medias con
el signo requerido.

## 6. El cambio de escala cuesta \(\exp(n\log n)\)

La fórmula de dilatación exacta es

\[
 \boxed{
 L_r(\beta x)=\sum_{j=0}^r{r\choose j}
       \beta^j(1-\beta)^{r-j}L_j(x).}
\tag{26}
\]

Tomando \(x=\varepsilon u\) y \(\beta=1/\varepsilon\), se obtiene

\[
 L_r(u)=\sum_{j=0}^r{r\choose j}
 \varepsilon^{-j}(1-\varepsilon^{-1})^{r-j}
 L_j(\varepsilon u).
\tag{27}
\]

Para \(0<\varepsilon<1\), la carga absoluta de (27) es exactamente

\[
 \boxed{
 \sum_{j=0}^r{r\choose j}\varepsilon^{-j}
       |1-\varepsilon^{-1}|^{r-j}
 =\left({2\over\varepsilon}-1\right)^r.}
\tag{28}
\]

En la elección diagonal natural \(\varepsilon=1/n\), \(r=n-1\),

\[
 (2n-1)^{n-1}=\exp\{(1+o(1))n\log n\}.
\tag{29}
\]

Aplicar (25) grado por grado y sumar magnitudes pierde por (29) exactamente
la escala que A1 necesita cancelar. Si no se toman magnitudes, los
coeficientes alternados de (27) deben conservarse completos; al recombinarlos
se vuelve a \(L_r(u)\) y no se ha obtenido una desigualdad. Ésta es la versión
Markov del stop-gate de colisión de `104_13`.

## 7. Falsificador off-line y alcance lógico

El cuarteto off-line no satisface por sí solo (1) con los pesos aritméticos
canónicos; por eso una desigualdad futura que use de verdad la desintegración
(5) no tiene por qué transferirse al cuarteto. Pero las únicas desigualdades
automáticas obtenidas aquí son (9) y Jensen, y (15) prueba que carecen de
margen incluso antes de llegar al nivel espectral. No «demuestran» una cota
para el cuarteto ni para la aritmética real.

Si se intenta trasladar la contracción desde (s>1) al borde mediante una
continuación que olvida (5), reaparecen exactamente los residuos off-line de
`104_41`; allí el cuarteto es el falsificador vinculante. Por tanto este
transporte no evade el gate de residuos.

## 8. Decisión

```text
probado incondicionalmente:
  desintegración multiplicativa exacta (4)--(5);
  adjunción y contracción Markov (8)--(9);
  brecha espectral cero, incluso en media cero (12)--(15);
  convolución Laguerre exacta sin triángulos (20);
  análogo continuo Gamma y contracción 1/sqrt(r+1) (24)--(25);
  costo exacto (2/epsilon-1)^r del cambio a la escala A1 (28).

descartado:
  una brecha operatorial uniforme del transporte divisor;
  inversión positiva de la convolución en el grado;
  transferir la coercividad Gamma grado a grado mediante triángulos;
  usar el transporte como cierre autónomo de la cota proporcional.

permanece abierto:
  una estimación unilateral específica para el vector Laguerre no escalado,
  conservando completa la suma alternada (27), el bloque Gamma y los bordes;
  B_n <= (1501/2002) A_n, A1 y RH.
```

`tools/divisor_markov_laguerre_check.py` verifica con `Fraction` la identidad
divisor, la fórmula de adición, el operador continuo (24) y la dilatación
(26)--(28). No usa ceros de zeta ni punto flotante.
