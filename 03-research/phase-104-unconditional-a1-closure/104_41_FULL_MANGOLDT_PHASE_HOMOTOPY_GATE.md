# 104_41 — Fase Euler completa y gate de homotopía con residuos

**Estado.** Se atacó directamente la combinación completa

\[
 M_\Lambda(s):={1\over s-1}+{\zeta'(s)\over\zeta(s)}
 ={d\over ds}\log\{(s-1)\zeta(s)\},                         \tag{1}
\]

sin separar primos simples, potencias primas ni polo. En el semiplano
Euler se obtiene una identidad que conserva toda la fase y una cota
unilateral genuina, uniforme en el grado:

\[
 \boxed{|\mathcal B_{n,a}|\le3n\qquad(a\ge4).}               \tag{2}
\]

La cota no usa módulos dentro de \(M_\Lambda\): integra la fase exacta de
\((s-1)\zeta(s)\). El intento falla al transportar (2) hasta \(a=1\).
La homotopía del círculo Euler a la línea crítica cruza exactamente los
ceros con parte real \(>1/2\), y el defecto es exactamente la suma firmada
de residuos de `104_33`, no un término de error estimable por la fase de
frontera. Un cuarteto recíproco racional deja **idéntica la fase completa**
en la línea crítica y cambia el momento en una cantidad exponencial.

Por tanto queda descartado el siguiente mecanismo: «acotar la fase completa
en un semiplano de convergencia de Euler y transferir la cota a \(a=1\) por
una homotopía sin un teorema separado sobre los residuos». No se descarta
una desigualdad aritmética nueva que use específicamente los pesos reales
\(\Lambda(m)\) para controlar conjuntamente esos residuos. Este documento
no prueba A1 ni RH.

## 1. Auditoría de no duplicación y signo

Póngase

\[
 F(s)=(s-1)\zeta(s),\qquad B_n=A_n-\lambda_n.                \tag{3}
\]

Las identidades de `phase-102/140--141`, `103_66` y `104_03` ya implican

\[
 B_n=-{1\over2\pi i}\oint M_\Lambda(s)
              \left({s\over s-1}\right)^n ds,              \tag{4}
\]

en un círculo pequeño canónico alrededor de \(s=1\). La mera identidad de
contorno no es nueva. Tampoco lo es reemplazarla por el símbolo de Cayley:
`104_33` prueba que la frontera sola omite los residuos interiores.

Lo nuevo de este ataque es cuantitativo: (2) demuestra que el estimador de
fase sí es fuerte antes de mover el contorno y localiza todo su fracaso en
el cruce de residuos. El signo de (4) es vinculante. Como

\[
 \lambda_n=A_n+\lambda_n^{\rm prime},
\]

se tiene \(B_n=-\lambda_n^{\rm prime}\); por tanto \(M_\Lambda\) aparece
con signo negativo en la forma de \(B_n\).

Hay una segunda identidad que no se contará como avance independiente.
Sea \(G(z)=\log F((1-z)^{-1})\) y \(q=1-a^{-1}\). Siempre que \(q\)
pertenezca al disco de Taylor de \(G\), la composición
\(G_a(z)=G(q+z/a)\) da

\[
 \mathcal B_{n,a}=a^{-n}\sum_{k\ge n}
 {k-1\choose n-1}q^{k-n}B_k.                              \tag{4a}
\]

Es una cola Abel positiva, no una inversión unilateral. Usarla para
recuperar \(B_n\) repetiría exactamente el stop-gate Tauberiano de
`104_17`; además un cero transformado dentro de \(|z|\le q\) invalida
la expansión antes de que pueda ocultarse como error. No se usa (4a) en
la prueba de (2).

## 2. Regularización completa en un semiplano Euler

Sea

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x){\bf1}_{x\ge0},
 \qquad
 \widehat g_n(t)=1-
 \left({-1/2+it\over1/2+it}\right)^n,                      \tag{5}
\]

y escribamos

\[
 W_n(t)=|\widehat g_n(t)|^2.                                \tag{6}
\]

Para \(a>1\), la serie prima y la integral siguientes convergen
absolutamente. Definimos la forma completa prima--polo, con el signo de
\(B_n\), por

\[
\begin{aligned}
 \mathcal B_{n,a}:={}&a\sum_{m\ge2}{\Lambda(m)\over m^a}
       L_{n-1}^{(1)}(a\log m)\\
 &-a\int_1^\infty y^{-a}L_{n-1}^{(1)}(a\log y)\,dy .        \tag{7}
\end{aligned}
\]

La fórmula de Euler y la generatriz de Laguerre dan simultáneamente

\[
 \boxed{
 \mathcal B_{n,a}
 =-n[z^n]\log F\!\left({a\over1-z}\right).}                \tag{8}
\]

La fórmula de coeficientes (8) continúa \(\mathcal B_{n,a}\) desde el
dominio Euler a un entorno de \(a=1\). Al retirar el regulador en esa
continuación conjunta,

\[
 \boxed{B_n=\lim_{a\downarrow1}\mathcal B_{n,a}.}           \tag{9}
\]

La serie de (7) converge directamente para todo \(a>1\). La realización de
semigrupo que sigue requiere \(a>2\); (9) no afirma que sus canales
separados tengan límite al bajar hasta \(a=1\).

La realización por el semigrupo contractivo de `104_36`, ahora con
\(d\psi\) en vez de \(d\theta\), da la identidad de Plancherel

\[
 \boxed{
 \mathcal B_{n,a}
 =-{a\over2\pi}\int_{\mathbb R}W_n(t)
 \Re M_\Lambda\!\left(a(1/2+it)\right)dt .}                \tag{10}
\]

En (10) el polo y todos los \(p^k\) están combinados **antes** de tomar la
parte real. No aparece \(|M_\Lambda|\).

## 3. Identidad exacta de fase

Para \(a>2\), \(F\) no se anula en la recta
\(s=a(1/2+it)\). Sea

\[
 \vartheta_a(t)=\arg F\!\left(a(1/2+it)\right)              \tag{11}
\]

la rama continua fijada por \(\vartheta_a(0)=0\). Como

\[
 {d\over dt}\vartheta_a(t)
 =a\Re M_\Lambda\!\left(a(1/2+it)\right),                 \tag{12}
\]

(10) se vuelve

\[
 \mathcal B_{n,a}
 =-{1\over2\pi}\int_{\mathbb R}W_n(t)\,d\vartheta_a(t).
                                                                    \tag{13}
\]

Para \(a\ge4\), la fase es acotada. En efecto,
\(\Re(s-1)\ge1\), luego \(|\arg(s-1)|<\pi/2\). Además

\[
 |\zeta(s)-1|
 \le\zeta(2)-1
 <{2\over3}<\sin{\pi\over4}.                              \tag{14}
\]

La segunda desigualdad puede probarse sin evaluar \(\pi\):

\[
 \sum_{m=2}^\infty {1\over m^2}
 <{1\over4}+{1\over9}+{1\over16}+{1\over25}
   +\int_5^\infty{x^{-2}}dx
 ={2389\over3600}<{2\over3}.                              \tag{15}
\]

El disco \(|z-1|<2/3\) visto desde el origen tiene abertura menor que
\(\pi/4\). Por tanto

\[
 \boxed{|\vartheta_a(t)|<{3\pi\over4}\qquad(a\ge4).}      \tag{16}
\]

Resta calcular exactamente la variación del test. En \(t>0\), escriba

\[
 {-1/2+it\over1/2+it}=e^{i\theta(t)},qquad
 \theta(0)=\pi,\qquad\theta(\infty)=0.
\]

Entonces

\[
 W_n(t)=2-2\cos(n\theta(t)).                                \tag{17}
\]

Como \(W_n\) es par,

\[
\begin{aligned}
 \operatorname{TV}_{\mathbb R}(W_n)
 &=2\int_0^\pi 2n|\sin(n\theta)|\,d\theta\\
 &=8n.                                                       \tag{18}
\end{aligned}
\]

Los términos de borde en la integración por partes de (13) se anulan,
porque \(W_n(t)=O_n(t^{-2})\). De (13), (16) y (18),

\[
 |\mathcal B_{n,a}|
 \le {1\over2\pi}{3\pi\over4}\,8n
 =3n,                                                        \tag{19}
\]

que prueba (2). Ésta es una cota de fase, no una cota de módulo.

## 4. Dónde se rompe la homotopía

En la coordenada de (8), un cero no trivial \(\rho=\beta+i\gamma\)
aparece en

\[
 z_{\rho,a}=1-{a\over\rho}.                                \tag{20}
\]

La distancia al círculo de Hardy satisface la identidad exacta

\[
 \boxed{
 |z_{\rho,a}|^2-1
 ={a(a-2\beta)\over|\rho|^2}.}                             \tag{21}
\]

Al bajar \(a\) desde \(4\) hasta \(1\):

* un cero con \(\beta>1/2\) cruza \(|z|=1\) en \(a=2\beta>1\);
* un cero crítico solo alcanza la frontera en \(a=1\);
* un cero con \(\beta<1/2\) no entra antes del extremo.

El germen (8) continúa siendo una cantidad bien definida; lo que deja de
ser válido es la representación por una frontera holomorfa sin defectos.
Aplicando la deformación meromorfa correcta de `104_33` se obtiene

\[
 \boxed{
 B_n=\mathcal P_n+
 \sum_{\Re\rho>1/2}
 {m_\rho\,\mathcal F_n(w_\rho)\over\rho(\rho-1)},
 \qquad w_\rho=1-{1\over\rho}.}                            \tag{22}
\]

Aquí
\(\mathcal P_n:=\mathcal I_n^\partial(-M_\Lambda\circ s)\) es el
momento radial de frontera de `104_33`; mediante (12)--(13) es el momento
de la derivada distribucional de la fase, incluidos los ceros críticos, y

\[
 \mathcal F_n(w)
 =n+\sum_{d=1}^{n-1}(n-d)(w^d+w^{-d}).                      \tag{23}
\]

La serie de residuos de (22) converge absolutamente para \(n\) fijo. La
ecuación (22) muestra que transportar (19) no cuesta una constante de
contorno: cuesta exactamente la suma que detecta ceros a la derecha. Una
estimación de esa suma suficientemente fuerte para

\[
 B_n\le {1501\over2002}A_n                                  \tag{24}
\]

es el teorema RH-strength que se buscaba, no una consecuencia de (19).

## 5. Falsificador: misma fase crítica, residuo exponencial

Sea

\[
 w={i\over2},\qquad
 \rho={1\over1-w}={4+2i\over5},                             \tag{25}
\]

y complete la órbita

\[
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\},
 \qquad Q_\rho(s)=\prod_{\eta\in\mathcal O(\rho)}(s-\eta).
                                                                    \tag{26}
\]

Si \(s=1/2+it\), \(\delta=\Re\rho-1/2\) y
\(\gamma=\Im\rho\), entonces

\[
 \boxed{
 Q_\rho(1/2+it)
 =\{(t-\gamma)^2+\delta^2\}
  \{(t+\gamma)^2+\delta^2\}>0.}                            \tag{27}
\]

Por consiguiente multiplicar \(F\) por \(Q_\rho^M\) no cambia la fase en
la línea crítica (sí multiplica el módulo por un factor positivo):

\[
 \arg\{F(1/2+it)Q_\rho(1/2+it)^M\}
 =\arg F(1/2+it).                                           \tag{28}
\]

Sin embargo, los dos residuos derechos cambian \(B_n\) en

\[
 -M Q_n,\qquad
 Q_n=4-2\Re(w^n+w^{-n}).                                    \tag{29}
\]

Para \(n=152\),

\[
 \boxed{
 -Q_{152}=2(2^{152}+2^{-152})-4>0,}                         \tag{30}
\]

y la multiplicidad \(M\) derrota cualquier techo proporcional fijo sin
alterar (28). El cuarteto no conserva el producto de Euler positivo de
\(\zeta\), de modo que (30) no refuta una desigualdad específica para los
pesos reales \(\Lambda(m)\). Sí prueba que la fase crítica y la homotopía
analítica, por sí solas, no suministran esa desigualdad.

El mismo testigo pasa el gate de cruce: \(2\Re\rho=8/5\), de modo que sus
polos entran estrictamente durante el trayecto \(4\downarrow1\).

## 6. Decisión

```text
probado:
  identidad completa Mangoldt+polo con el signo de B_n;
  representación exacta mediante la fase de (s-1)zeta(s);
  TV(W_n)=8n;
  cota phase-preserving |B_{n,a}|<=3n para a>=4;
  ley exacta de cruce |1-a/rho|^2-1=a(a-2Re rho)/|rho|^2;
  defecto final igual a la suma firmada de residuos de 104_33;
  cuarteto racional con fase crítica idéntica y residuo exponencial.

descartado:
  transferir la cota fuerte del semiplano Euler a a=1 sin controlar
  explícitamente los residuos interiores;
  cualquier argumento que use solo la fase o el símbolo de frontera,
  aun conservándolos complejos en vez de tomar módulos.

sobrevive:
  una desigualdad aritmética específica de los pesos exactos Lambda(m)
  que acople el momento de frontera con la suma de residuos y pruebe (24).

no probado:
  (24), A1 o RH.
```

## 7. Verificación reproducible

El archivo `tools/full_mangoldt_phase_homotopy_gate_check.py` usa solamente
`Fraction` y racionales gaussianos para comprobar:

1. la cota racional de (15);
2. el conteo exacto que da \(\operatorname{TV}(W_n)=8n\);
3. la identidad de cruce (21) para el cuarteto (25);
4. la positividad exacta de (27) sobre una malla racional;
5. el residuo exponencial (30).

Se reproduce con

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 full_mangoldt_phase_homotopy_gate_check.py
