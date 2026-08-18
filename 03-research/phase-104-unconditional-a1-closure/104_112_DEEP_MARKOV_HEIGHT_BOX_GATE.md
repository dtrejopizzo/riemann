# 104_112 — Caja de altura profunda y gate de Markov sin holgura

**Pregunta.** ¿La forma profunda de `104_75`--`104_76` deja una holgura
real que pueda explotarse mediante Markov, promedios en \(n\), o una cota
de densidad positiva pequeña?

**Resultado.** No. La relajación profunda sí es más débil que A1, pero su
media logarítmica no contiene un margen intermedio. Para un cero exterior
\(\rho=\beta+i\gamma\), \(\beta>1/2\), ponga

\[
 w_\rho={\rho-1\over\rho}=e^{-a_\rho+i\theta_\rho},\qquad
 a_\rho={1\over2}\log {|\rho|^2\over|\rho-1|^2}>0 .
\]

El cuarteto funcional aporta a \(\lambda_n\)

\[
 q_n(\rho)=4-4\cosh(na_\rho)\cos(n\theta_\rho).          \tag{1}
\]

Con el umbral profundo \(S_X=e^{\sqrt X}\), un retorno
\(\cos(n\theta_\rho)\ge1/2\) y \(n\in[X/2,X]\) fuerza
\[
 q_n(\rho)\le 4-e^{na_\rho}.
\]
Por tanto el detector profundo se dispara tan pronto como
\[
 a_\rho>2X^{-1/2}+O(X^{-1}\log X).                       \tag{2}
\]

Como
\[
 a_\rho={2\beta-1\over 2\gamma^2+O(1)}
 \qquad(\gamma\to\infty,\ \beta\hbox{ fijo}),             \tag{3}
\]
la caja equivalente del obstáculo es, salvo constantes absolutas,

\[
 \boxed{
 R_X=\left\{\rho:\ 0<\gamma\lesssim X^{1/4},\quad
 \beta-{1\over2}\gtrsim \gamma^2X^{-1/2}\right\}.}        \tag{4}
\]

Así, `104_75`--`104_76` no transforman RH en una estimación promedio
suave: transforman RH en una familia de regiones libres de ceros cuya
frontera toca \(\Re s=1/2\) cuando \(X\to\infty\). Un solo cero en (4)
produce una excursión profunda sobre un conjunto sindético de densidad
logarítmica positiva.

Este documento cierra tres rutas:

1. un Markov sobre la parte positiva de la suma de bajos ceros;
2. cualquier intento de mejorar solamente una constante
   \(\limsup\Omega_X\le c\), con \(c>0\);
3. el uso de verificación finita de ceros como sustituto asintótico.

No prueba el límite profundo, A1 ni RH. Prueba que esta coordenada ya no
tiene slack cuantitativo oculto: o se excluyen ceros en la caja \(R_X\), o
el detector falla.

---

## 1. La caja \(R_X\)

La ecuación (1) es la misma de `104_76`. Si
\(\cos(n\theta_\rho)\ge1/2\), entonces

\[
 q_n(\rho)\le4-2\cosh(na_\rho)\le4-e^{na_\rho}.          \tag{5}
\]

En el observable profundo se permite el error subexponencial de los
factores no interiores (`104_111`) y la cola alta (`104_76`). Ambos son
\(\exp(o(\sqrt X))\) o menores frente a \(S_X=e^{\sqrt X}\). Por tanto,
en el rango \(n\in[X/2,X]\), la condición suficiente y necesaria a escala
exponencial para que un cuarteto fijo pueda activar el detector es

\[
 {X\over2}a_\rho\ge\sqrt X+o(\sqrt X),                  \tag{6}
\]

que es (2).

Por otro lado,

\[
 e^{2a_\rho}
={\beta^2+\gamma^2\over(1-\beta)^2+\gamma^2}
=1+{2\beta-1\over(1-\beta)^2+\gamma^2}.                 \tag{7}
\]

Cuando \(0<\beta-1/2\le1/2\),
\[
 {2\beta-1\over 2(\gamma^2+1)}
 \le a_\rho
 \le {2\beta-1\over 2\gamma^2}.                         \tag{8}
\]

Las constantes de (8) no importan para el gate: combinadas con (2)
dicen exactamente que la frontera pedida tiene forma
\[
 \beta-{1\over2}\asymp\gamma^2X^{-1/2}.                  \tag{9}
\]

Además, la cota universal de `104_76`,
\[
 a_\rho\le {1\over2\gamma^2},                            \tag{10}
\]
implica que ningún cero con
\(\gamma\gg X^{1/4}\) puede producir por sí solo una excursión de tamaño
\(e^{\sqrt X}\) en grados \(n\le X\). Esto recupera la escala
\(\gamma\le X^{1/4}\) de `104_76` desde el lado contrario: la escala no es
artefacto de la prueba de cola, sino la escala exacta del detector.

## 2. Markov exacto, sin ganancia

Sea \(Y=X^{1/4}\), y escriba \(D_n(Y)\) para la parte de bajos ceros con
el signo orientado de modo que un cuarteto exterior con
\(\cos(n\theta_\rho)\ge1/2\) contribuya positivamente a \(D_n(Y)\).
En la línea crítica, cada órbita contribuye a \(\lambda_n\) una cantidad
no negativa; por tanto \(D_n(Y)\le0\) para todo \(n\) si todos los ceros
bajos están en la línea.

Si existe un cuarteto exterior en la caja (4), los retornos
\(\cos(n\theta_\rho)\ge1/2\) forman un conjunto sindético. En cualquier
intervalo \([X/2,X]\), su masa armónica tiene una cota inferior positiva,
y en esos retornos

\[
 D_n(Y)_+\ge e^{na_\rho}-O(N(Y)).                       \tag{11}
\]

Como
\[
 N(X^{1/4})\asymp X^{1/4}\log X,                         \tag{12}
\]
se obtiene

\[
 \sum_{n\le X}{D_n(Y)_+\over n}
 \gg e^{Xa_\rho/2}-O(X^{1/4}\log X).                    \tag{13}
\]

La cota de Markov que querría probar el límite profundo tendría escala
\[
 e^{\sqrt X}H_X.                                        \tag{14}
\]

Las ecuaciones (13)--(14) muestran que no hay régimen intermedio: bajo RH
la suma positiva es cero; con un cero exterior suficientemente dentro de
la caja crece más que el umbral. Markov no pierde nada, y por eso no gana
nada. Cualquier promedio en \(n\) que conserve las excursiones profundas
vuelve a pedir la exclusión punto a punto de (4).

## 3. Constantes positivas de densidad no sirven

`104_56` ya registra que, en el modelo abstracto de fases de Fejér, la
densidad mala forzada por un cero exterior puede hacerse arbitrariamente
pequeña. Por tanto ningún enunciado de la forma

\[
 \limsup_{X\to\infty}\Omega_X\le c
 \qquad(c>0)                                            \tag{15}
\]

puede ser un paso parcial hacia RH. Para excluir todos los ceros
exteriores hace falta el límite \(c=0\). Mejorar \(1/2\) a \(1/8\), o a
cualquier constante positiva, no descarta los contraejemplos de fase
dominante ya construidos.

La forma correcta del target profundo es entonces:

\[
 \boxed{\Omega_X\to0}
 \quad\Longleftrightarrow\quad
 \boxed{\hbox{no hay ceros en }R_X\hbox{ para }X\to\infty}
 \quad\Longleftrightarrow\quad
 \mathrm{RH}.                                           \tag{16}
\]

La primera equivalencia es operacional: (4) da la única ventana en la que
el detector puede fallar después de `104_76` y `104_111`. La segunda es el
hecho de que, para cualquier cero fijo con \(\beta>1/2\), existe \(X\)
suficientemente grande tal que cae dentro de \(R_X\).

## 4. Consecuencia estratégica

La vía profunda sigue siendo válida como criterio, pero no reduce el paso
final a una estimación de primer momento, segundo momento, Markov,
Chernoff, ni a una constante de densidad positiva. El siguiente mecanismo,
si existe, debe ser una desigualdad de exclusión de ceros en la caja
\(R_X\) usando los primos ordinarios literales y el completamiento de
Riemann. Debe fallar para los modelos Euler exteriores de `104_78`,
`104_81`, `104_90` y `104_91`; de lo contrario no distingue la zeta real.
