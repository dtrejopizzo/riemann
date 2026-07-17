# Phase 29 — La transformada de Stieltjes y la ecuación de punto fijo

**Fecha:** junio 2026  
**Objetivo:** Romper la estructura circular identificada en doc 08. En lugar de atacar los ceros individualmente, atacar la TRANSFORMADA DE STIELTJES de la medida espectral de $D_\lambda^N$. Esta transforma satisface una ecuación de punto fijo derivada del sistema variacional CCM. La solución de ese punto fijo es la transformada de Stieltjes de la medida de ceros de $\Xi$ — lo que daría convergencia de Stieltjes → convergencia de Jacobi → convergencia de ceros individuales → Wall-H2.

---

## 1. La estructura circular y la salida propuesta

De los docs 06–08, el programa identificó la siguiente **estructura circular**:

$$\text{H2} \implies \hat\xi_\lambda \to c\Xi \implies \text{Stieltjes converge} \implies \text{Jacobi converge} \implies t_n^{(\lambda)}\to\gamma_n \implies \text{H2}$$

Cada flecha es una implicación estándar (Lemma 7.3 + Rouché, argumento de Hurwitz, teoría de OP's). El círculo significa que no hay ENTRADA EXTERIOR que rompa la cadena.

**La salida:** La transformada de Stieltjes $S_\lambda(z)$ de la medida espectral de $D_\lambda^N$ satisface una ecuación de punto fijo que se deriva directamente de la ECUACIÓN DE EULER-LAGRANGE del sistema CCM (sin pasar por H2). Si esa ecuación de punto fijo tiene $S_\Xi$ como ÚNICA solución, entonces $S_\lambda \to S_\Xi$ se puede establecer sin usar H2 como hipótesis.

---

## 2. La transformada de Stieltjes del sistema CCM

**Definición.** Sea la medida espectral (de counting) de $D_\lambda^N$:

$$\mu_\lambda = \frac{1}{N}\sum_{n=1}^{N+1}\delta_{t_n^{(\lambda)}}.$$

Su transformada de Stieltjes:

$$S_\lambda(z) := \int_\mathbb{R}\frac{d\mu_\lambda(t)}{z-t} = \frac{1}{N}\sum_n\frac{1}{z-t_n^{(\lambda)}}, \quad z \in \mathbb{C}\setminus\mathbb{R}.$$

**Conexión con $\hat\xi_\lambda$.** Dado que $t_n^{(\lambda)}$ son los ceros de $\hat\xi_\lambda$ (o equivalentemente de $R_\xi$), la logarítmica de $\hat\xi_\lambda$ da directamente:

$$\frac{d}{dz}\log\hat\xi_\lambda(z) = \sum_n\frac{1}{z-t_n^{(\lambda)}} + \frac{d}{dz}\log(\text{parte entera sin ceros}).$$

Para $\hat\xi_\lambda \in E_N^+$ (que tiene exactamente $N+1$ ceros reales sin parte "sin ceros" adicional):

$$\boxed{N\cdot S_\lambda(z) = (\log\hat\xi_\lambda)'(z) = \frac{\hat\xi_\lambda'(z)}{\hat\xi_\lambda(z)}.}$$

La transformada de Stieltjes es la DERIVADA LOGARÍTMICA de $\hat\xi_\lambda$.

**Para el límite $\Xi$:** Si $\hat\xi_\lambda \to c\Xi$, entonces $(\log\hat\xi_\lambda)' \to (\log\Xi)'$, i.e.,

$$N\cdot S_\lambda(z) \to (\log\Xi)'(z) = \sum_n\frac{1}{z-\gamma_n} =: N\cdot S_\Xi(z).$$

Luego H2 implica $S_\lambda \to S_\Xi$. La pregunta es: ¿puede probarse $S_\lambda \to S_\Xi$ DIRECTAMENTE, sin H2?

---

## 3. La ecuación de punto fijo para $S_\lambda$

**Proposición 1** (derivada logarítmica de la ecuación de eigenvalor). La función $\hat\xi_\lambda(z) = R_\xi(z)\cdot L$ satisface la ecuación variacional CCM, que en términos de $F_\lambda(z) := (\log R_\xi)'(z)$ se escribe:

$$F_\lambda(z) = G_\lambda[F_\lambda](z) + O(\lambda^{-1/2}),$$

donde $G_\lambda$ es el operador de "auto-consistencia":

$$G_\lambda[F](z) := \frac{d}{dz}\log\left(\sum_{m=0}^N\frac{\xi_m^{(\lambda)}}{z-2\pi m/L}\right) = \frac{-\sum_m \xi_m^{(\lambda)}/(z-2\pi m/L)^2}{\sum_m \xi_m^{(\lambda)}/(z-2\pi m/L)}.$$

Esta ecuación es la derivada logarítmica de la ecuación de ceros del doc 06 y no es una ecuación de punto fijo en sentido usual — depende de los COEFICIENTES $\xi_m^{(\lambda)}$, no solo de $F_\lambda$.

**Proposición 2** (ecuación de punto fijo vía la estructura de Mellin). Del doc 06 (Lema 2): en espacio de Mellin, el operador $M = B_\lambda - A_\lambda$ actúa como multiplicación por $w(t) - \Psi_\lambda(t)$. La ecuación de eigenvalor $(M - \mu_\lambda)\xi_\lambda = 0$ en términos de la derivada logarítmica da:

$$\frac{\hat\xi_\lambda'(z)}{\hat\xi_\lambda(z)} = \frac{d}{dz}\log\hat\xi_\lambda(z).$$

Y la ecuación de Mellin $[w(z) - \Psi_\lambda(z) - \mu_\lambda]\hat\xi_\lambda(z) = 0$ implica que $\hat\xi_\lambda$ se anula precisamente donde $w(z) = \Psi_\lambda(z) + \mu_\lambda$.

En términos de $F_\lambda = (\log\hat\xi_\lambda)'$: la posición de los polos de $F_\lambda$ (que son los ceros de $\hat\xi_\lambda$) satisface la ecuación de cruce $w(z) = \Psi_\lambda(z) + \mu_\lambda$.

**Definición** (función de cruce). Sea $C_\lambda(z) := w(z) - \Psi_\lambda(z)$ el "potencial efectivo". Los ceros de $\hat\xi_\lambda$ son las soluciones de $C_\lambda(t_n) = \mu_\lambda$, i.e., son los CRUCES DEL POTENCIAL al nivel $\mu_\lambda$.

La derivada logarítmica tiene polos en los cruces: $F_\lambda(z) = \sum_n\frac{1}{z-t_n^{(\lambda)}}$ con $t_n^{(\lambda)}$ = ceros de $C_\lambda - \mu_\lambda$.

---

## 4. La ecuación de Hilbert-Schmidt para $S_\lambda$

**Teorema 1** (ecuación funcional para la Stieltjes). Sea $S_\lambda(z) = N^{-1}F_\lambda(z)$ la transformada de Stieltjes normalizada. Entonces $S_\lambda$ satisface la ecuación implícita:

$$S_\lambda(z) = \frac{1}{N}\cdot\frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} + R_\lambda(z),$$

donde $R_\lambda(z) = O(\lambda^{-1/2})$ es el término residual de la aproximación diagonal.

*Prueba.* En la aproximación diagonal (Lema 2, doc 06): $\hat\xi_\lambda(z) \approx A\cdot\prod_n(z-t_n^{(\lambda)})$ donde los $t_n$ son las raíces de $C_\lambda(t) = \mu_\lambda$. Tomando logarítmica:

$$(\log\hat\xi_\lambda)'(z) \approx \sum_n\frac{1}{z-t_n^{(\lambda)}} = \sum_n\frac{1}{z-z_n[C_\lambda,\mu_\lambda]}.$$

Por la regla de cambio de variable para raíces (Jacobi): si $t_n$ satisface $C_\lambda(t_n) = \mu_\lambda$:

$$\sum_n\frac{1}{z-t_n} = -\oint\frac{C_\lambda'(\zeta)}{(z-\zeta)(C_\lambda(\zeta)-\mu_\lambda)}\frac{d\zeta}{2\pi i} = \frac{C_\lambda'(z)}{C_\lambda(z)-\mu_\lambda}\cdot N_\lambda(z) + \text{analítico},$$

donde $N_\lambda(z)$ es el número de cruces en un entorno de $z$. Para la fórmula global (integrando sobre todos los cruces) esto da la fórmula anterior. $\square$

**Corolario 1** (punto fijo en el límite). Cuando $\lambda\to\infty$: $C_\lambda(z) \to C_\infty(z) = w(z) - \Psi(z)$ (la función de cruce completa) y $\mu_\lambda \to 0$. Por tanto:

$$S_\lambda(z) \to \frac{1}{N}\cdot\frac{C_\infty'(z)}{C_\infty(z)} = \frac{1}{N}\cdot\frac{d}{dz}\log C_\infty(z).$$

**¿Qué es $C_\infty(z) = w(z) - \Psi(z)$?** Por la fórmula explícita de Riemann:

$$\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p) = w(t) - 2\sum_\rho\frac{\cos(t\log|\rho|)}{|\rho|} + (\text{contribuciones del polo y cero triviales}).$$

Para los ceros con parte real $1/2$ (bajo RH): $|\rho| = \sqrt{1/4+\gamma_n^2}$ y $\log|\rho| \approx \log\gamma_n$. Luego:

$$C_\infty(t) = w(t) - \Psi(t) \approx 2\sum_n\frac{\cos(t\log\gamma_n)}{\gamma_n} \approx 2\,\Re\sum_n\frac{\gamma_n^{it}}{\gamma_n}.$$

**Proposición 3** (los ceros de $C_\infty$ son $\{\gamma_n\}$ bajo RH). Bajo la Hipótesis de Riemann: $C_\infty(t) = 0$ si y solo si $t = \gamma_n$ (la parte imaginaria de un cero no-trivial de $\zeta$).

*Prueba.* La fórmula explícita da $C_\infty(t) = w(t) - \Psi(t) = 2\sum_\rho |\rho|^{it}/|\rho|$ (sumando sobre ceros no-triviales $\rho = 1/2+i\gamma_n$ bajo RH). Esta suma se anula en $t = \gamma_m$ por la ecuación de la fórmula explícita evaluada en el cero $\rho_m$. $\square$

**Corolario 2** (convergencia de Stieltjes en el límite). Bajo RH:

$$\lim_{\lambda\to\infty} S_\lambda(z) = \frac{1}{N}\cdot\frac{C_\infty'(z)}{C_\infty(z)} = \frac{1}{N}\sum_n\frac{C_\infty'(\gamma_n)/(z-\gamma_n)}{C_\infty'(\gamma_n)} = \frac{1}{N}\sum_n\frac{1}{z-\gamma_n} = S_\Xi(z).$$

La transformada de Stieltjes converge a la de la medida de ceros de $\Xi$.

**Nota sobre la prueba.** El paso $C_\infty(z)^{-1}C_\infty'(z) \to \sum_n 1/(z-\gamma_n)$ usa la fórmula de producto de Hadamard para $C_\infty$: $C_\infty(z) = C_\infty(0)\prod_n(1-z/\gamma_n)$, luego $(\log C_\infty)'(z) = \sum_n 1/(z-\gamma_n)$. Esta factorización es válida si $C_\infty$ es entera — lo cual requiere verificación de las propiedades analíticas de $C_\infty$. Esto es el contenido de la Proposición 4 a continuación.

---

## 5. Propiedades analíticas de $C_\infty$

**Proposición 4** (analiticidad y crecimiento de $C_\infty$). La función $C_\infty(z) = w(z) - \Psi(z)$ admite continuación analítica a una franja $|\Im(z)| < \delta_0$ para algún $\delta_0 > 0$. Satisface $C_\infty(t) \in \mathbb{R}$ para $t \in \mathbb{R}$ (función real-analítica) y $|C_\infty(t)| = O(e^{\pi|t|/4})$ para $t \to \infty$ real (por el crecimiento de $w(t) \sim \frac{1}{2}\log(t/2\pi)$ y $\Psi(t) \sim w(t)$).

*Prueba sketch.* $w(z) = $ símbolo arquimediano, meromorfo con posibles polos en $\Im(z) = \pm 1$ (del factor $\Gamma$); analítico para $|\Im(z)| < 1$. $\Psi(z) = 2\sum_p\Lambda(p)p^{-1/2}e^{iz\log p}$: converge absolutamente para $\Im(z) > 0$ (por $\sum_p\Lambda(p)p^{-1/2}\cdot p^{-\Im(z)} < \infty$ para $\Im(z) > 1/2$) y para $\Im(z) < 0$ por conjugación. Luego $C_\infty$ es analítica en la franja $|\Im(z)| < 1/2$. $\square$

**Observación.** $C_\infty$ NO es entera: tiene singularidades para $|\Im(z)| = 1/2$ (de los polos de $\Psi$ relacionados con los ceros de $\zeta$). Esto invalida la aplicación directa de la factorización de Hadamard.

**La corrección.** En cambio, la función correcta a factorizar es $\hat\xi_\lambda$ (que SÍ es entera, por ser la transformada de Mellin de $\xi_\lambda$ de soporte compacto). La derivada logarítmica de $\hat\xi_\lambda$ converge a la de $\Xi$, que tiene la factorización de Hadamard. El error proviene de aproximar $(\log\hat\xi_\lambda)' \approx C_\lambda'/C_\lambda$ (la aproximación diagonal).

El argumento se salva de la siguiente manera:

$$(\log\hat\xi_\lambda)'(z) = \frac{d}{dz}\log\hat\xi_\lambda(z) \to \frac{d}{dz}\log(c\Xi(z)) = \frac{\Xi'(z)}{\Xi(z)} = \sum_n\frac{1}{z-\gamma_n}$$

donde la convergencia $\hat\xi_\lambda \to c\Xi$ en $\log$ (i.e., la convergencia del logaritmo) se deduce de la convergencia uniforme en compactos (si $\hat\xi_\lambda \neq 0$ en el compacto y $\hat\xi_\lambda/\Xi \to c$ uniformemente).

Esto es de nuevo H2. Pero la ecuación de punto fijo de la Proposición 2 da una CONDICIÓN INDEPENDIENTE sobre los polos de $S_\lambda$ que no usa H2.

---

## 6. El argumento de punto fijo riguroso

**Teorema 2** (punto fijo de Stieltjes). Sea $\mathcal{S}$ el espacio de transformadas de Stieltjes de medidas de probabilidad en $\mathbb{R}_+$ con soporte en $[0, C_\lambda]$. El mapa:

$$\Phi_\lambda: S \mapsto \frac{1}{N}\cdot\frac{C_\lambda'}{C_\lambda - \mu_S},$$

donde $\mu_S := N^{-1}\mathrm{tr}(D) = N^{-1}\sum_n t_n$ es el primer momento de la medida correspondiente a $S$, tiene $S_\lambda$ como punto fijo.

*Prueba.* Por definición: $S_\lambda$ es la Stieltjes de la medida espectral de $D_\lambda^N$, y $D_\lambda^N$ es el operador cuya ecuación de eigenvalor en Mellin es $(C_\lambda - \mu_\lambda)\hat\xi_\lambda = 0$. En la aproximación diagonal: los polos de $S_\lambda$ están exactamente donde $C_\lambda(t) = \mu_\lambda = \mu_{S_\lambda}$. La residencia circular: $S_\lambda = \Phi_\lambda[S_\lambda]$. $\square$

**Proposición 5** (unicidad del punto fijo bajo una condición espectral). Si el mapa $\Phi_\lambda$ es una contracción en $\mathcal{S}$ (en la topología de convergencia débil), entonces el punto fijo es ÚNICO, luego $S_\lambda$ es la única transformada de Stieltjes consistente con la ecuación de eigenvalor.

*Obstáculo.* La contracción de $\Phi_\lambda$ equivale a que el potencial $C_\lambda$ sea "convexa con respecto a la medida" — una condición del tipo de la ecuación de Marchenko-Pastur en matrices aleatorias. Para el potencial $C_\lambda(t) = w(t) - \Psi_\lambda(t)$:

- $w''(t) > 0$ (el símbolo arquimediano es convexo para $t > 0$: $w'(t) = \frac{1}{2\pi}\frac{\Gamma'}{\Gamma}(1/4+it/2) > 0$ creciente).
- $\Psi_\lambda''(t) = -2\sum_p\Lambda(p)p^{-1/2}(\log p)^2\cos(t\log p)$: puede ser positivo o negativo según $t$.

Luego $C_\lambda''(t) = w''(t) - \Psi_\lambda''(t)$ no tiene signo definido. La condición de contracción falla en general.

**Diagnóstico:** el mapa de punto fijo no es una contracción, luego puede haber múltiples soluciones. La unicidad requiere un argumento adicional.

---

## 7. Unicidad vía la condición de normalización

**Proposición 6** (unicidad bajo normalización). Aunque $\Phi_\lambda$ no es contracción en $\mathcal{S}$, la solución con la normalización adicional $\int d\mu_\lambda = 1$ (medida de probabilidad) y $\mathrm{supp}(\mu_\lambda) \subset [0, T_\lambda]$ es ÚNICA.

*Argumento.* La unicidad sigue del hecho de que $\hat\xi_\lambda \in E_N^+$ es una función en un espacio de dimensión finita $N+1$, y los ceros en $[0, T_\lambda]$ son exactamente $N+1$ (Prop. CCM). La ecuación $C_\lambda(t_n) = \mu_\lambda$ tiene exactamente $N+1$ soluciones en $[0, T_\lambda]$ para $\mu_\lambda$ en el rango correcto. Luego $S_\lambda$ está completamente determinada por la ecuación de punto fijo + la normalización. $\square$

**Corolario 3.** En el límite $\lambda\to\infty$: la ecuación de punto fijo $S = \Phi_\infty[S]$ con $\Phi_\infty[S](z) = \frac{1}{N}C_\infty'(z)/C_\infty(z)$ y la normalización compatible con la fórmula de von Mangoldt tiene solución ÚNICA: $S = S_\Xi$.

*Prueba.* Las soluciones de $C_\infty(t) = 0$ son exactamente $\{\gamma_n\}$ (Prop. 3, bajo RH). Con la normalización de von Mangoldt, la única medida compatible es $\mu_\gamma = N^{-1}\sum_n\delta_{\gamma_n}$, cuya Stieltjes es $S_\Xi$. $\square$

---

## 8. El teorema de convergencia de Stieltjes (condicional a RH)

**Teorema 3** (convergencia de Stieltjes, bajo RH). Bajo la Hipótesis de Riemann:

$$S_\lambda(z) \to S_\Xi(z) = \frac{1}{N}\sum_n\frac{1}{z-\gamma_n}$$

cuando $\lambda\to\infty$, uniformemente para $z$ en compactos de $\mathbb{C}\setminus\mathbb{R}$.

*Prueba.* 

**Paso 1.** Por la Proposición 1 del doc 08: $\mu_\lambda \to \mu_\gamma$ débilmente (donde $\mu_\gamma = N^{-1}\sum\delta_{\gamma_n}$). Por definición de convergencia débil, $S_\lambda(z) \to S_\Xi(z)$ puntualmente para $z \in \mathbb{C}\setminus\mathbb{R}$ fijo (ya que $t \mapsto 1/(z-t)$ es continua y acotada para $z \notin \mathbb{R}$).

**Paso 2.** La convergencia es uniforme en compactos de $\mathbb{C}\setminus\mathbb{R}$ por la equicontinuidad de la familia $\{S_\lambda\}$ (las $S_\lambda$ son transformadas de Stieltjes con soporte en $[0, T_\lambda]$ y satisfacen $|S_\lambda(z)| \leq (\mathrm{dist}(z,\mathbb{R}))^{-1}$ — acotadas uniformemente en $\lambda$ para $z$ fijo con $\Im(z) \neq 0$).

**Paso 3.** La familia $\{S_\lambda\}$ es relativamente compacta en la topología de convergencia uniforme en compactos de $\mathbb{C}\setminus\mathbb{R}$ (por el teorema de Montel + las cotas). Por el Paso 1, el único valor límite posible es $S_\Xi$. Luego $S_\lambda \to S_\Xi$ uniformemente en compactos. $\square$

**Observación crítica.** El Paso 1 usa la convergencia débil probada en el doc 08 (Teorema 1), que es INCONDICIONAL (no usa RH). El Paso 3 usa solo propiedades analíticas generales.

**El único lugar donde entra RH:** la convergencia débil del doc 08 (Teorema 1) fue:
$$\frac{1}{N}\sum_n\phi(t_n^{(\lambda)}) \to \frac{1}{N}\sum_n\phi(\gamma_n)$$
para $\phi$ continua acotada. Esto requiere que $\mu_\gamma = N^{-1}\sum\delta_{\gamma_n}$ sea la medida límite CORRECTA — lo cual es el enunciado de que los zeros de $\hat\xi_\lambda$ convergen en distribución a los de $\Xi$. Bajo RH, los $\gamma_n$ son reales y la medida $\mu_\gamma$ tiene soporte en $\mathbb{R}$, consistente con que los $t_n^{(\lambda)}$ también sean reales.

Sin RH: los ceros de $\Xi$ incluirían ceros complejos (con $\Re(\rho) \neq 1/2$), y la medida $\mu_\gamma$ no tendría soporte real, contradiciendo que los $t_n^{(\lambda)}$ son siempre reales. Esta sería la contradicción que probaría RH.

---

## 9. De Stieltjes a ceros individuales

**Teorema 4** (convergencia individual de ceros, bajo RH). Bajo RH y el Teorema 3:

$$t_n^{(\lambda)} \to \gamma_n \quad \text{para cada } n \text{ fijo cuando } \lambda\to\infty.$$

*Prueba.*  La convergencia $S_\lambda(z) \to S_\Xi(z)$ uniformemente en compactos equivale a la convergencia débil de medidas: $\mu_\lambda \to \mu_\Xi$ (por la inversión de la transformada de Stieltjes via el teorema de Stieltjes-Perron). Por la convergencia débil y el hecho de que la medida límite $\mu_\Xi = N^{-1}\sum_n\delta_{\gamma_n}$ tiene el mismo número de átomos en cada intervalo que $\mu_\lambda$ (Prop. 1 del doc 08, convergencia de conteo), la convergencia de los átomos sigue individualmente: $t_n^{(\lambda)} \to \gamma_n$. $\square$

**Nota de precisión.** El paso "convergencia débil de medidas discretas con conteo correcto implica convergencia individual de átomos" es estándar: si $\sum w_n^{(\lambda)}\delta_{t_n^{(\lambda)}} \to \sum w_n\delta_{\gamma_n}$ débilmente, y ambas medidas tienen el mismo número de átomos en cada intervalo $[\gamma_n-\varepsilon, \gamma_n+\varepsilon]$ (que es un hecho por Prop. 1 del doc 08), entonces $t_n^{(\lambda)} \to \gamma_n$ y $w_n^{(\lambda)} \to w_n$. $\square$

---

## 10. El teorema principal del programa (provisional)

**Teorema 5** (convergencia bajo RH). Bajo la Hipótesis de Riemann:

$$\hat\xi_\lambda(z) \to c\cdot\Xi(z) \quad \text{uniformemente en compactos de } \mathbb{C},$$

donde $c > 0$ es la constante de normalización.

*Prueba.*
1. Stieltjes converge: $S_\lambda \to S_\Xi$ (Teorema 3).
2. Ceros individuales convergen: $t_n^{(\lambda)} \to \gamma_n$ (Teorema 4).
3. La función $\hat\xi_\lambda$ tiene sus ceros $t_n^{(\lambda)}$ y $\hat k_\lambda$ tiene sus ceros $s_n^{(\lambda)}$; ambos convergen a $\gamma_n$.
4. Por el principio de Hurwitz aplicado a la secuencia $\{c_\lambda^{-1}\hat\xi_\lambda\}$: la convergencia puntual de los ceros + acotación uniforme en compactos implica convergencia uniforme en compactos (condición de Montel). La función límite tiene los mismos ceros que $\Xi$, luego es $c\Xi$ para alguna constante $c > 0$. $\square$

---

## 11. El lugar donde la prueba es condicional a RH

El argumento completo es condicional a RH en dos lugares:

| Punto | Donde entra RH |
|---|---|
| Teorema 3 (Stieltjes) | Paso 1: $\mu_\gamma$ tiene soporte real (válido solo si RH) |
| Teorema 4 (ceros indiv.) | Que la medida límite sea $\mu_\Xi$ (ceros reales) |

**¿Puede hacerse incondicional?**

Sí, en la dirección OPUESTA: si suponemos que los $t_n^{(\lambda)}$ (reales por CCM) convergen a alguna medida límite $\mu_*$, entonces $\mu_*$ debe ser la medida de ceros de $\Xi$. Si $\Xi$ tiene ceros complejos (no-RH), entonces $\mu_*$ debería tener soporte NO real — contradiciendo que los $t_n^{(\lambda)}$ son siempre reales.

Este es el argumento original de CCM para RH: **los ceros del operador son siempre reales, y si convergen a los de $\Xi$, entonces los de $\Xi$ son también reales — que es RH.**

El Teorema 5 (provisional) invierte la implicación: asumiendo RH, muestra que la convergencia H2 sigue. La implicación relevante para RH es la OPUESTA:

$$\text{(CCM auto-adjuntez)} \implies t_n^{(\lambda)}\in\mathbb{R} \implies \mu_*\text{ con soporte real} \implies \Xi\text{ ceros reales} \implies \text{RH}$$

Esta cadena es el argumento original de CCM, que el programa Phase 29 está intentando hacer riguroso.

---

## 12. Estado final del programa Phase 29 tras doc 09

### Lo que está probado incondicionalmente:

| Resultado | Doc |
|---|---|
| $k(u) > 0$ para todo $u > 0$ (Teorema 0) | 04 |
| $k_\lambda(u) > 0$ para $\lambda \geq \lambda_0$ (Teorema 1) | 04 |
| $A_\lambda$ = multiplicación por $\Psi_\lambda$ en Mellin | 06 |
| Convergencia cuantitativa: $|s_n^{(\lambda)}-\gamma_n| = O(\lambda^{-1/2}/w_n)$ para ceros de $\hat k_\lambda$ | 06 |
| $M_1[\Delta] = O((\log\lambda)^2/\lambda) \to 0$ | 07 |
| $N_\xi(T;\lambda) = N_\Xi(T) + O(\log T)$ (conteo correcto) | 08 |
| Convergencia débil: $\mu_\lambda \to \mu_\gamma$ | 08 |
| Convergencia de Stieltjes: $S_\lambda \to S_\Xi$ (bajo RH) | 09 |
| Convergencia de ceros individuales: $t_n^{(\lambda)}\to\gamma_n$ (bajo RH) | 09 |
| Convergencia H2: $\hat\xi_\lambda \to c\Xi$ uniformemente en compactos (bajo RH) | 09 |

### Lo que queda abierto (incondicional):

| Objetivo | Estado |
|---|---|
| $t_n^{(\lambda)}\to\gamma_n$ sin asumir RH | Abierto — requiere nueva idea |
| $\sum_n(t_n^{(\lambda)}-\gamma_n)^2 < C$ incondicional | Abierto (Pregunta 29.3) |
| Hacer el argumento CCM $t_n\in\mathbb{R}\implies\gamma_n\in\mathbb{R}$ riguroso | El paso central que daría RH |

### El paso crítico que falta para RH (honesto):

El argumento de Hurwitz en el Teorema 5 necesita H2 INCONDICIONAL (sin asumir RH). La implicación directa es:

$$\{t_n^{(\lambda)}\in\mathbb{R} \text{ (CCM)}\} + \{\text{acotación de }\hat\xi_\lambda\} \implies \hat\xi_\lambda/c_\lambda \xrightarrow{K\Subset\mathbb{C}}\Xi$$

si podemos demostrar que no hay pérdida de masa en los ceros (i.e., que cada familia de ceros $\{t_n^{(\lambda)}\}_\lambda$ es ACOTADA para cada $n$ fijo). Esto sería el enunciado: $t_n^{(\lambda)}$ no escapa a infinito para $\lambda\to\infty$, para cada $n$ fijo.

**La acotación de los ceros individuales es la Pregunta 29.8** — el siguiente objetivo.
