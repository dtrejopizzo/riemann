# 104_76 — Localización en altura de la cola profunda y gate de momentos

**Resultado.** El target aritmético extremadamente débil de `104_75`,

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}\}}
 \longrightarrow0,                                      \tag{1}
\]

no requiere controlar colectivamente todos los ceros. Uniformemente para
\(1\le n\le X\), la contribución de los ceros de altura
\(\gamma>X^{1/4}\) satisface

\[
 \boxed{|\lambda_n^{(>X^{1/4})}|
 \ll X\log(X+2)\exp(\tfrac12\sqrt X).}                  \tag{2}
\]

Por tanto, si todos los ceros con \(0<\gamma\le X^{1/4}\) están en la
recta crítica, entonces, para \(X\) suficientemente grande, el indicador
de (1) es idénticamente cero para **cada** \(n\le X\). En particular, la
cola alta ya tiene margen exponencial \(e^{-\sqrt X/2+O(\log X)}\) respecto
del umbral.

Esto localiza exactamente el hueco: para probar (1) asintóticamente queda
excluir los modos exteriores de altura \(\gamma\le X^{1/4}\) cuando
\(X\to\infty\). Esa obligación recorre todas las alturas y no es un input
incondicional conocido. Un argumento de segundo momento, Markov o Chernoff
no falla por los ceros altos: falla precisamente si no controla este bloque
bajo. El cuarteto exterior fijo muestra que ningún bound que use solo (2)
puede cerrar (1).

Este documento prueba una localización cuantitativa nueva dentro de la fase;
no prueba (1), A1 ni RH.

**No duplicación interna.** `104_63` identifica la energía completa y el
colapso de Parseval/Christoffel--Darboux; `104_70` estudia temperatura
variable; `104_73`, la presión Bernstein; y `104_75`, el gate profundo y la
media lineal de Bessel. Aquí no se introduce otro observable: se demuestra
que el nivel \(e^{\sqrt X}\) localiza toda posible violación en alturas
\(O(X^{1/4})\), con la cola complementaria sumada absolutamente por
cuartetos funcionales.

---

## 1. Cuartetos funcionales y su tamaño

Sea \(\rho=\beta+i\gamma\), con \(\gamma>0\) y
\(1/2\le\beta<1\), un representante de una órbita bajo conjugación y
\(\rho\mapsto1-\rho\). Ponga

\[
 w_\rho=1-{1\over\rho}={\rho-1\over\rho}
           =e^{-a_\rho+i\theta_\rho},\qquad a_\rho\ge0. \tag{3}
\]

Si la órbita tiene cuatro elementos, su contribución al coeficiente de Li
es

\[
 q_n(\rho)
 =4-2\Re\{w_\rho^n+w_\rho^{-n}\}
 =4-4\cosh(na_\rho)\cos(n\theta_\rho).                  \tag{4}
\]

En la recta crítica la órbita tiene dos elementos y la contribución es
la mitad de (4). En particular es no negativa:

\[
 q_n(\tfrac12+i\gamma)/2
 =2\{1-\cos(n\theta_\rho)\}\ge0.                        \tag{5}
\]

La desviación radial posee la cota universal

\[
\begin{aligned}
 e^{2a_\rho}=|w_\rho|^{-2}
 &= {\beta^2+\gamma^2\over(1-\beta)^2+\gamma^2}\\
 &=1+{2\beta-1\over(1-\beta)^2+\gamma^2}
 \le1+{1\over\gamma^2},
\end{aligned}                                            \tag{6}
\]

y por ello

\[
 \boxed{0\le a_\rho\le{1\over2\gamma^2}.}              \tag{7}
\]

De (4) y (7), contando multiplicidades,

\[
 |q_n(\rho)|\le4+4e^{n/(2\gamma^2)}.                     \tag{8}
\]

La desigualdad conserva la amplificación radial que produce una excursión
exterior; no reemplaza \(w_\rho\) por un módulo unitario.

---

## 2. La cola por encima de una altura móvil

Escriba \(N(T)\) para el conteo de ceros con multiplicidad. Solo usaremos
la consecuencia incondicional de Riemann--von Mangoldt

\[
 N(T)\ll T\log(T+2).                                     \tag{9}
\]

Para \(2\le Y\le2X\), parta la suma simétrica por ceros en
\(Y<\gamma\le2X\) y \(\gamma>2X\). La primera parte es finita. Por (8)
y (9), uniformemente para \(n\le X\),

\[
 \sum_{Y<\gamma\le2X}|q_n(\rho)|
 \ll X\log(X+2)\{1+e^{X/(2Y^2)}\}.                      \tag{10}
\]

La parte infinita converge absolutamente después de agrupar por órbitas.
En efecto, si \(\gamma>2X\), entonces
\(|1-w_\rho|=|\rho|^{-1}\le\gamma^{-1}<1/2\), y la serie
de \(\log(1-1/\rho)\) da

\[
 |\theta_\rho|\le {2\over\gamma},qquad
 a_\rho\le {1\over2\gamma^2}.                           \tag{11}
\]

Como \(n|\theta_\rho|\le1\) y \(na_\rho\le1/8\), (4) implica

\[
 |q_n(\rho)|
 \le4\{|1-\cos(n\theta_\rho)|+\cosh(na_\rho)-1\}
 \ll {n^2\over\gamma^2}.                                \tag{12}
\]

La sumación parcial en (9) da

\[
 \sum_{\gamma>T}{m_\rho\over\gamma^2}
 \ll {\log(T+2)\over T},                                \tag{13}
\]

de donde

\[
 \sum_{\gamma>2X}|q_n(\rho)|\ll X\log(X+2).             \tag{14}
\]

La fórmula incondicional de Li por ceros se interpreta con el corte
simétrico en altura. Ese corte contiene cada órbita funcional completa o
no contiene ninguno de sus elementos, porque todos tienen la misma
ordenada en valor absoluto. Para cada (n) fijo, (12)--(13) prueban la
convergencia absoluta de la serie ya agrupada por órbitas; por tanto esta
agrupación no introduce una convención nueva y su suma es precisamente el
coeficiente de Li usual \(\lambda_n\).

Las ecuaciones (10) y (14) prueban el siguiente lema.

**Lema 2.1 (localización uniforme).** Para \(2\le Y\le2X\),

\[
 \boxed{
 \sup_{1\le n\le X}|\lambda_n^{(>Y)}|
 \ll X\log(X+2)\{1+e^{X/(2Y^2)}\}.}                    \tag{15}
\]

La notación \(\lambda_n^{(>Y)}\) significa la suma por órbitas de los
ceros con ordenada positiva mayor que \(Y\). La cota demuestra además que
esa cola no depende de una convención de sumación.

Tomando \(Y=X^{1/4}\) en (15) se obtiene (2). Más generalmente, para el
umbral \(e^{X^\alpha}\), \(0<\alpha<1\), la elección natural es

\[
 Y=X^{(1-\alpha)/2},qquad
 {X\over2Y^2}={1\over2}X^\alpha.                         \tag{16}
\]

Así el exponente \(1/4\) no es accidental: es la escala dual del gate
\(e^{\sqrt X}\).

---

## 3. Consecuencia para los pesos reales \(\Lambda(m)\)

Suponga que todos los ceros con \(0<\gamma\le X^{1/4}\) están en la
recta crítica. Por (5), su contribución a cada \(\lambda_n\) es no
negativa. El Lema 2.1 da entonces, uniformemente para \(n\le X\),

\[
 \lambda_n\ge
 -C X\log(X+2)e^{\sqrt X/2}.                              \tag{17}
\]

Para \(X\) suficientemente grande, el lado de error de (17) es menor que
\(e^{\sqrt X}/2\).

Use ahora la diagonal real de `104_69`--`104_75`,

\[
 \lambda_{n,\varepsilon_X}
 =A_n+p_n(\varepsilon_X)-Q_{n,\varepsilon_X},qquad
 \varepsilon_X=e^{-X/100},                               \tag{18}
\]

para la cual

\[
 \sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|=o(1). \tag{19}
\]

De (17)--(19), también para todo \(n\le X\),

\[
 \lambda_{n,\varepsilon_X}+\log(n+1)>-e^{\sqrt X}.       \tag{20}
\]

Como el evento de (1) equivale exactamente a la desigualdad opuesta en
(20), queda probado:

**Teorema 3.1 (anulación finita del observable profundo).** Existe
\(X_0\) absoluto tal que, si \(X\ge X_0\) y RH está verificada hasta
altura \(X^{1/4}\), entonces el observable de (1) vale exactamente cero.

Este teorema usa los pesos reales \(\Lambda(m)\) en (18), no un competidor
de soporte primo. Pero su hipótesis de altura no puede hacerse
asintótica a partir de una verificación finita fija.

---

## 4. Qué obtiene un ataque de momentos

Ponga

\[
 Z_{n,X}=\{-\lambda_n-\log(n+1)\}_+,qquad S_X=e^{\sqrt X}. \tag{21}
\]

Bajo la hipótesis parcial del Teorema 3.1, (17) implica

\[
 \sup_{n\le X}Z_{n,X}\ll X\log(X+2)e^{\sqrt X/2}.       \tag{22}
\]

Por consiguiente,

\[
 {1\over H_X}\sum_{n\le X}{Z_{n,X}^2\over n}
 \ll X^2\log^2(X+2)e^{\sqrt X}
 =o(e^{2\sqrt X}).                                       \tag{23}
\]

Chebyshev aplicado a (23), junto con el error uniforme (o(1)) de (19),
prueba (1): desplazar el umbral (e^{\sqrt X}) en (o(1)) no altera la
cota de Markov. La ganancia es diagnóstica: el segundo momento ya posee la
escala pedida una vez eliminados los ceros exteriores bajos; los ceros
altos no exigen una cancelación adicional.

Sin esa hipótesis, `104_63` da la identidad exacta de Parseval/CD, pero
acotarla por \(o(e^{2\sqrt X})\) excluiría precisamente un modo bajo
exterior. Lo mismo ocurre con Chernoff a temperatura
\(t_X=e^{-\sqrt X}\): una cota del momento exponencial controla (1), pero
un modo fijo de tasa \(R>1\) hace que ese momento explote en un conjunto de
densidad positiva. No hay una inferencia desde el primer momento lineal de
`104_75` hasta (23).

---

## 5. Falsificador localizado

Tome un cuarteto exterior fijo \(w=e^{-a+i\theta}\), \(a>0\). Su
contribución es

\[
 q_n=4-4\cosh(an)\cos(n\theta).                           \tag{24}
\]

Los retornos de la rotación \(n\theta\) a una vecindad de cero forman un
conjunto sindético de densidad positiva; allí

\[
 q_n\le-c e^{an}.                                        \tag{25}
\]

Para \(n\ge2\sqrt X/a\), (25) cruza el umbral
\(-e^{\sqrt X}\). Eliminar los primeros \(O(\sqrt X)\) grados solo quita
la mitad asintótica de la masa armónica hasta \(X\), de modo que persiste
una densidad logarítmica positiva. En el ejemplo racional \(w=2i\) de
`104_75`, la densidad profunda es exactamente \(1/8\).

Este cuarteto satisface todas las cotas de cola usadas en el Lema 2.1 una
vez que se lo coloca en el bloque bajo. Por tanto (15) no puede, por sí
sola, probar (1): el paso que queda es un teorema aritmético que excluya
esos modos bajos para la zeta real. Esto es una localización del hueco, no
una afirmación de imposibilidad para toda identidad aritmética futura.

---

## 6. Veredicto

**Probado:** la cota radial (7), la suma absoluta de la cola (15), la
escala dual general (16), la anulación del indicador bajo RH parcial hasta
\(X^{1/4}\), y el bound de segundo momento (23) bajo la misma hipótesis.

**Ganancia:** el ataque de gran desviación queda reducido al bloque de
ceros con \(\gamma\le X^{1/4}\). Los ceros por encima de esa altura tienen
margen exponencial suficiente aun tomándolos en valor absoluto por
cuartetos completos.

**No probado:** un control incondicional de ese bloque bajo cuando
\(X\to\infty\), el límite (1), A1 o RH. Una verificación de altura fija
solo da un rango finito, por grande que sea.

---

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 deep_tail_height_localization_check.py
```

El checker verifica la identidad de cuarteto, (7), la cota elemental de la
cola muy alta y la separación exponencial entre (2) y el umbral de (1).
