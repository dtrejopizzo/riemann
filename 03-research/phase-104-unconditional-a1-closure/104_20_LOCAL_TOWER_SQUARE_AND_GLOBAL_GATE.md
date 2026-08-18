# 104_20 — Cuadrado local de torres y gate global sobreviviente

**Rol.** Explotar la fórmula especial de
\(b_u=J_u*J_u\) para combinar una torre prima completa con los tres canales
de `104_19` **antes** de estimar. El resultado es una factorización local
exacta. El cuadrado obtenido es algebraico, no un cuadrado de norma, y los
bloques locales de la sucesión aritmética real tienen ambos signos. Por
tanto muere la estrategia ``signo por torre y suma''. La desigualdad global
del cociclo completo permanece viva y es el frente siguiente.

Este documento no prueba A1 ni RH.

## 1. Operadores de traslación y el canal polar acoplado

Sea

\[
 N=-\partial_x,
 \qquad
 \mathsf A_\varepsilon f(x)
 :=\int_0^\infty e^{-r}f(x+r/\varepsilon)\,dr,
 \qquad
 \mathsf U_\ell f(x):=\int_0^\ell f(x+t)\,dt.       \tag{1}
\]

Como

\[
 (\varepsilon-\partial_x)^{-1}={1\over\varepsilon}
 \mathsf A_\varepsilon,
\]

el factor polar de un solo cociclo actúa sobre la variable Laguerre como

\[
 \mathsf P_{\varepsilon,c}
 :=I-u(\varepsilon-\partial_x)^{-1}
 =I-c\mathsf A_\varepsilon,
 \qquad u=c\varepsilon.                             \tag{2}
\]

Integración por partes en (1) da

\[
 \mathsf A_\varepsilon N
 =\varepsilon(I-\mathsf A_\varepsilon),
\]

y por tanto la forma equivalente

\[
 \boxed{
 \mathsf P_{\varepsilon,c}
 =(1-c)I+{c\over\varepsilon}\mathsf A_\varepsilon N.} \tag{3}
\]

Todos los operadores de (1)--(3) son funciones de traslaciones y
derivadas; conmutan en el espacio de polinomios donde se usarán.

## 2. Segunda diferencia exacta en una torre prima

Fijemos un primo \(p\) y pongamos

\[
 \ell=\log p,
 \qquad \rho=p^{-1-\varepsilon},
 \qquad Q=p^u,
 \qquad (E_\ell f)(x)=f(x+\ell).                   \tag{4}
\]

Con la convención \(a_{-1}=a_{-2}=0\), sea
\(\nabla^2a_k=a_k-2a_{k-1}+a_{k-2}\). La fórmula de `104_19` se refina a

\[
 \boxed{
 b_u(p^k)=\nabla^2\bigl((k+1)Q^k\bigr),
 \qquad k\ge0.}                                     \tag{5}
\]

En consecuencia, para todo polinomio \(f\),

\[
 \boxed{
 \sum_{k\ge0}b_u(p^k)\rho^k f(x+k\ell)
 =\sum_{k\ge0}(k+1)(Q\rho)^k
   (I-\rho E_\ell)^2f(x+k\ell).}                  \tag{6}
\]

La identidad es una sumación discreta exacta: el factor
\((I-\rho E_\ell)^2\) es la imagen operacional de la segunda diferencia
de (5). Las dos series convergen absolutamente porque

\[
 Q\rho=p^{-1-(1-c)\varepsilon}<1.
\]

Además,

\[
 \boxed{
 I-\rho E_\ell=(1-\rho)I+\rho\mathsf U_\ell N,}   \tag{7}
\]

porque \(\mathsf U_\ell N=I-E_\ell\).

## 3. Teorema del cuadrado local acoplado

Los operadores (3) y (7) conmutan. Defínase

\[
 \boxed{
 \mathsf C_{p,\varepsilon,c}
 :=\bigl((1-\rho)I+\rho\mathsf U_\ell N\bigr)
   \bigl((1-c)I+{c\over\varepsilon}
                   \mathsf A_\varepsilon N\bigr).} \tag{8}
\]

**Teorema.** Una torre completa \(p^k\), incluidos los tres canales
polares de `104_19`, satisface

\[
 \boxed{
 \sum_{k\ge0}b_u(p^k)\rho^k
       \mathsf P_{\varepsilon,c}^{2}f(x+k\ell)
 =\sum_{k\ge0}(k+1)(Q\rho)^k
       \mathsf C_{p,\varepsilon,c}^{2}f(x+k\ell).} \tag{9}
\]

*Demostración.* Sustituir (6), conmutar
\(\mathsf P_{\varepsilon,c}^2\) a través de las traslaciones y usar (7)
produce (9). No se separa ninguno de los tres canales. \(\square\)

La medida firmada de `104_19` ha desaparecido dentro de un cuadrado. Pero
\(\mathsf C^2\) no es \(\mathsf C^*\mathsf C\): no define una norma ni tiene
signo sobre polinomios oscilatorios.

## 4. Expansión en Laguerres elevados

Escribamos

\[
 \mathsf C=a_0+a_1N+a_2N^2,                        \tag{10}
\]

donde

\[
\begin{aligned}
 a_0&=(1-\rho)(1-c)I,\\
 a_1&=(1-\rho){c\over\varepsilon}\mathsf A_\varepsilon
      +\rho(1-c)\mathsf U_\ell,\\
 a_2&={\rho c\over\varepsilon}
          \mathsf U_\ell\mathsf A_\varepsilon.
\end{aligned}                                      \tag{11}
\]

Los \(a_j\) son combinaciones positivas de traslaciones y conmutan entre
sí. Como

\[
 N^jL_n=L_{n-j}^{(j)},                              \tag{12}
\]

con la convención de valor cero para \(j>n\), resulta

\[
\boxed{
\begin{aligned}
 \mathsf C^2L_n={}&a_0^2L_n
 +2a_0a_1L_{n-1}^{(1)}
 +(a_1^2+2a_0a_2)L_{n-2}^{(2)}\\
 &+2a_1a_2L_{n-3}^{(3)}
 +a_2^2L_{n-4}^{(4)}.
\end{aligned}}                                      \tag{13}
\]

Todos los pesos operatoriales de (13) son positivos. No obstante, cada
Laguerre elevado conserva oscilaciones. El cuadrado local reorganiza la
cancelación, pero no la convierte en positividad.

## 5. Testigo exacto sobre la sucesión real \(b_u\)

La falta de signo no es solo formal. Considérese una torre \(p^k\) sobre un
fondo \(m\) coprimo con \(p\). Tras integrar la medida Beta del canal Gamma,
el bloque de grado \(n=1\) es, salvo el prefactor positivo
\(b_u(m)m^{-1-\varepsilon}\),

\[
 \boxed{
 K_0M_p\left[
 (1-c)^2(1-\log m-\bar\eta-\ell\mu_p)
 +{2c(1-c)\over\varepsilon}\right],}               \tag{14}
\]

donde

\[
\begin{aligned}
 K_0&=K_u(1+\varepsilon)>0,\\
 M_p&=\left({1-\rho\over1-Q\rho}\right)^2>0,\\
 \mu_p&={2\rho(Q-1)\over(1-\rho)(1-Q\rho)}>0,\\
 \bar\eta&={1\over2}\left[
 \psi\!\left({3+\varepsilon\over2}\right)
 -\psi\!\left({3+\varepsilon-u\over2}\right)
 \right]>0.
\end{aligned}                                      \tag{15}
\]

Aquí \(M_p=\sum_{k\ge0}b_u(p^k)\rho^k\),
\(\mu_p\) es el promedio exacto de \(k\) bajo esos pesos normalizados y
\(\bar\eta\) es el promedio de \(-\frac12\log v\) bajo la medida Beta
normalizada. Por tanto (14) cambia de signo exactamente al cruzar

\[
 \boxed{
 \log m=1-\bar\eta-\ell\mu_p
       +{2c\over(1-c)\varepsilon}.}                 \tag{16}
\]

Fijados \(p\) y \(c\in(0,1)\), existe
\(\varepsilon_0(p,c)>0\) tal que, para
\(0<\varepsilon<\varepsilon_0(p,c)\), el bloque \(m=1\) queda del lado
positivo y todo \(m\) coprimo suficientemente grande queda del lado
negativo. En ese régimen ambos signos ocurren con los pesos aritméticos
**reales** \(b_u\).

Más generalmente, el coeficiente líder en \(\log m\) del bloque de grado
\(n\) es

\[
 \boxed{
 {K_0M_p(1-c)^2\over n!}(-1)^n.}                   \tag{17}
\]

Así, para cada \(n\) par, incluidos todos los pares \(n\ge150\), existen
infinitos fondos coprimos cuyo bloque canónico es positivo. Por tanto el
signo global no puede cerrarse imponiendo signo no positivo a **cada bloque
canónico (14)**. Esto no descarta una renormalización o un reagrupamiento
global entre fondos, incluido el término global \(-1/u\) de (20) en
`104_19`.

## 6. Lo que no muere: el gate global

El testigo anterior **no** refuta el signo de la suma completa. La identidad
global de `104_19` sigue siendo

\[
 g_{n,\varepsilon,c}
 =[z^n]{\mathcal S_{c\varepsilon}(s_\varepsilon(z))-1
              \over c\varepsilon(1-z)},
 \qquad
 g_{n,\varepsilon,c}\longrightarrow-\Delta D_n.   \tag{18}
\]

Por tanto el enunciado, con sus cuantificadores completos,

\[
 \boxed{
 \exists c\in(0,1)\ \ \forall n\ge149:\quad
 \limsup_{\varepsilon\downarrow0}g_{n,\varepsilon,c}\le0} \tag{19}
\]

es, punto a punto, equivalente a \(\Delta D_n\ge0\), porque el límite de
(18) existe. La versión con \(g_{n,\varepsilon,c}\le0\) para
\(0<\varepsilon<\varepsilon_0(n)\) es suficiente; no hace falta un
\(\varepsilon_0\) uniforme en \(n\). Junto con el certificado finito,
cualquiera de esas formas probaría el strong margin y A1.

**Diagnóstico, no teorema.** Una extracción Cauchy/Borwein en `float64`
encontró \(g_{n,\varepsilon,c}<0\) hasta \(n=1200\) para

\[
 (\varepsilon,c)\in
 \{(10^{-3},1/2),(10^{-2},1/2),(10^{-1},1/2),(1,1/2),
   (10^{-1},9/10)\}.
\]

Se reproduce con

```bash
python3 tools/global_cocycle_probe.py --nmax 1200 --samples 32768 \
  --r1 0.99 --r2 0.985
```

No es un intervalo certificado y no entra en ninguna demostración. Su único
uso es direccional: no apareció un contraejemplo a la suma global, aun
cuando (14)--(17) prueban rigurosamente que sus sumandos locales tienen
ambos signos.

## 7. Reformulación global exacta que queda

La factorización (9) expresa el mismo gate global en una coordenada local
más estructurada, pero **no demuestra una reducción de dificultad respecto
de \(\Delta D_n\ge0\)**. La pregunta inequívoca es:

\[
 \boxed{
 \text{¿qué propiedad global de la convolución multiplicativa de todas
 las torres convierte la suma de }\mathsf C_p^2L_n
 \text{ en (19)?}}                                  \tag{20}
\]

Una prueba no puede usar signo torre a torre, signo por fondo, ni una norma
de \(\mathsf C\). Debe conservar las interacciones multiplicativas entre
primos distintos. Ese es ahora el punto activo más estrecho del mecanismo.

`tools/local_tower_square_check.py` verifica con aritmética `Fraction`
ingredientes algebraicos independientes: (3), (5), (7),
\(\mathsf B^2\mathsf P^2=(\mathsf B\mathsf P)^2\) sobre polinomios de prueba
y la recomposición de la fórmula lineal de grado uno a ambos lados de su
umbral; también chequea el coeficiente líder hasta grado ocho. No verifica
las series infinitas completas, (17) para todo grado, (19), A1 ni RH.
