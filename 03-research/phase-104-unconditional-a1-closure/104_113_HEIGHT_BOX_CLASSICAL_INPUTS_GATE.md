# 104_113 — Gate de inputs clásicos para la caja profunda

**Pregunta.** Una vez que `104_112` reduce el límite Deep a excluir la caja

\[
 R_X=\left\{\rho=\beta+i\gamma:\ 0<\gamma\lesssim X^{1/4},\quad
 \beta-\frac12\gtrsim \gamma^2X^{-1/2}\right\},
\]

¿pueden cerrarla una región libre de ceros clásica, un teorema de densidad,
una verificación finita de ceros, o una combinación de esos inputs?

**Resultado.** No como inputs autónomos. Con \(T=X^{1/4}\), la caja es

\[
 R_T=\left\{\rho:\ 0<\gamma\lesssim T,\quad
 \beta-\frac12\gtrsim{\gamma^2\over T^2}\right\}.        \tag{1}
\]

Su frontera toca \(\Re s=1/2\) en todo régimen
\(\gamma=o(T)\). Excluir \(R_T\) para todo \(T\) equivale, al dejar
\(T\to\infty\) con \(\gamma\) fijo, a excluir cada cero con
\(\beta>1/2\). Por eso los inputs que no prueban ausencia exacta en la
línea crítica no tienen dónde ganar:

1. Las regiones libres de ceros conocidas excluyen solo una vecindad de
   \(\Re s=1\), dirección transversal equivocada.
2. Los teoremas de densidad acotan cuántos ceros hay con
   \(\beta\ge\sigma\); no convierten una cota de conteo en cero ceros para
   \(\sigma=1/2+o(1)\).
3. Una verificación hasta altura \(H\) solo excluye la caja para
   \(X\lesssim H^4\), no asintóticamente.

Este documento no prueba ni refuta \(R_X=\varnothing\) para la zeta. Cierra
la ruta de usar inputs clásicos como sustituto del mecanismo aritmético
literal.

---

## 1. Forma \(T\)-escalada de la caja

La escala \(Y=X^{1/4}\) de `104_76` y `104_112` no es decorativa. Si
\(T=X^{1/4}\), entonces \(X^{-1/2}=T^{-2}\), y la caja se convierte en
(1). Para un cero fijo \(\rho=\beta+i\gamma\), \(\beta>1/2\), la condición
\[
 \beta-\frac12\gtrsim{\gamma^2\over T^2}
\]
vale para todo \(T\) suficientemente grande. Por tanto una prueba
uniforme de \(R_T=\varnothing\) para \(T\to\infty\) es ya una prueba de
que no existe ningún cero con \(\beta>1/2\). Por simetría funcional, eso
es RH.

La debilidad del detector profundo está en que, para cada \(T\), solo mira
alturas \(\gamma\lesssim T\) y exige una precisión radial
\(\gamma^2/T^2\). Pero esa precisión tiende a cero para cada cero fijo. No
hay margen permanente entre la caja y la línea crítica.

## 2. Regiones libres de ceros

Una región libre de Vinogradov--Korobov/Mossinghoff--Trudgian--Yang tiene
la forma

\[
 \beta\le1-\Delta(\gamma),
 \qquad
 \Delta(\gamma)\asymp(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}
\]

en el rango correspondiente. Esto excluye una franja pegada a
\(\Re s=1\). La caja (1), en cambio, contiene puntos con
\[
 \beta=\frac12+C{\gamma^2\over T^2}.
\]

Si \(\gamma=o(T)\), esos puntos están arbitrariamente cerca de la línea
crítica y muy lejos de la frontera \(\Re s=1-\Delta(\gamma)\). La región
libre clásica no interactúa con esa parte de la caja. En el borde
\(\gamma\asymp T\), la caja pide excluir desplazamientos de tamaño
constante desde \(1/2\); la región libre sigue sin llegar a esa escala
salvo cerca de \(1\).

Conclusión: una región libre clásica puede reducir la cota radial
adversarial de `104_90`, pero no puede hacer \(R_T\) vacío.

## 3. Teoremas de densidad

Un teorema típico de densidad da

\[
 N(\sigma,T)
 =\#\{\rho:\beta\ge\sigma,\ 0<\gamma\le T\}
 \le C\,T^{A(1-\sigma)}(\log T)^B .                    \tag{2}
\]

Para excluir la caja haría falta una afirmación de tipo
\[
 N\!\left({1\over2}+c{\gamma^2\over T^2};\ \gamma\hbox{ local}\right)=0
\]
en cada subrango de altura. Incluso si se reemplaza \(\gamma\) por un
subrango dyádico \(\Gamma<\gamma\le2\Gamma\), (2) en
\(\sigma=1/2+c\Gamma^2/T^2\) da un lado derecho de tamaño positivo, y en
los regímenes \(\Gamma=o(T)\) enorme:

\[
 T^{A(1/2-c\Gamma^2/T^2)}(\log T)^B .
\]

Un upper bound mayor que uno no excluye un solo cero. Pero un solo cero en
la caja dispara el detector profundo en un conjunto sindético de grados.
Este es el desajuste exacto: densidad controla conteo agregado; Deep exige
ausencia individual.

## 4. Verificación finita

Si RH está verificada hasta altura \(H\), entonces la caja queda vacía
para todo \(X\) con \(X^{1/4}\le H\). Es decir, se obtiene un rango

\[
 X\le H^4 .                                             \tag{3}
\]

Con \(H=3\cdot10^{12}\), esto explica la escala diagnóstica
\(\asymp8.1\cdot10^{49}\) para el borde puro \(X^{1/4}=H\), y las
constantes de `104_90` desplazan el cruce práctico hacia
\(\asymp4H^4\). Pero ningún \(H<\infty\) toca el límite
\(X\to\infty\). Los ceros que importan después de esa escala son
precisamente los inmediatamente por encima de la altura verificada, no una
cola remota que se pueda sumar absolutamente.

La verificación finita es, por tanto, un test de consistencia y un rango
certificado finito. No es una sustitución asintótica de la exclusión de
\(R_T\).

## 5. Consecuencia

La caja profunda deja una sola clase de sucesores: una desigualdad que use
los pesos ordinarios literales \(\Lambda(p^k)=\log p\), el soporte real de
los primos y el completamiento exacto de Riemann para excluir polos
interiores. Debe fallar para los modelos de `104_78`, `104_81`, `104_90` y
`104_91`, porque todos ellos conservan paquetes amplios de positividad,
PNT o simetría funcional y aun así tienen ceros exteriores.

En particular, no hay progreso parcial en mejorar una cota de densidad
positiva, ni en extender una altura verificada finita, salvo como evidencia
computacional. El objetivo que queda es exactamente \(R_T=\varnothing\)
para todo \(T\), con una prueba aritmética no reducible a conteo.
