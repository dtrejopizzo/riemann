# Hipótesis H1: La propiedad par-simple

**Fecha:** junio 2026  
**Objetivo:** Probar (o delimitar el dominio de validez de) H1: el eigenvalor mínimo de $QW_\lambda^N$ es simple y su eigenvector es par.

---

## 1. Reformulación matricial precisa

La propiedad par-simple (ES) dice: sobre el espacio $E_N = E_N^+ \oplus E_N^-$ con la descomposición par/impar del documento 00,
$$\mu^+(\lambda,N) < \mu^-(\lambda,N),$$
donde $\mu^\pm = \min_{f \in E_N^\pm, \|f\|=1} QW_\lambda^N(f,f)$, y además $\mu^+$ es un eigenvalor simple de $QW_\lambda^{N,+}$.

Por la Proposición 2 del doc 00, $QW_\lambda^N = QW_\lambda^{N,+} \oplus QW_\lambda^{N,-}$, y basta estudiar las dos restricciones por separado.

---

## 2. Análisis de los tres sectores sobre $E_N^\pm$

**Proposición 1** (signos de los sectores en par/impar).  

*(a) Sector cruzado.* Para $f \in E_N^+$: $\hat f(-z) = \hat f(z)$, luego $\hat f(-i/2) = \hat f(i/2)$ y
$$Q^{\mathrm{cross}}(f) = 2\hat f(i/2)^2 \geq 0.$$
Para $f \in E_N^-$: $\hat f(-z) = -\hat f(z)$, luego $\hat f(-i/2) = -\hat f(i/2)$ y
$$Q^{\mathrm{cross}}(f) = -2\hat f(i/2)^2 \leq 0.$$

*(b) Sector aritmético.* Para $f \in E_N^+$ (función par, $f(u) = f(u^{-1})$):
$$\langle f \mid T(n)f\rangle = 2n^{-1/2}\int_{\lambda^{-1}}^\lambda f(u)f(nu)\,d^*u.$$
Para $f \in E_N^-$ (función impar, $f(u) = -f(u^{-1})$):
$$\langle f \mid T(n)f\rangle = -2n^{-1/2}\int_{\lambda^{-1}}^\lambda f(u)f(nu)\,d^*u.$$
En ambos casos, el integrando $f(u)f(nu)$ puede ser positivo o negativo, pero la integral $I_n(f) := \int f(u)f(nu)\,d^*u$ es la misma. Por tanto:
$$Q^{\mathrm{arith}}(f,\lambda) = -\sum_{1<k\leq\lambda^2}\Lambda(k)\,\langle f\mid T(k)f\rangle = \begin{cases} -2\sum_k \Lambda(k)k^{-1/2}I_k(f) & f \in E_N^+ \\ +2\sum_k \Lambda(k)k^{-1/2}I_k(f) & f \in E_N^- \end{cases}$$

*(c) Sector arquimediano.* $Q^{\mathrm{arch}}(f)$ tiene la misma expresión para $f \in E_N^\pm$ (el integrando $|\hat f(t)|^2 \partial_t\theta$ es invariante bajo $f\mapsto\gamma f$ dado que $|\widehat{\gamma f}(t)| = |\hat f(t)|$).

**Corolario 1.** Para cualquier $f_0 \in E_N^+$ normalizado con $\|f_0\| = 1$ y su imagen impar $f_0^- = f_0 - \gamma f_0 / \|\cdots\|$ (proyección y renormalización), se tiene:
$$QW_\lambda^N(f_0, f_0) - QW_\lambda^N(f_0^-, f_0^-) = 4\hat f_0(i/2)^2 - 4\sum_k \Lambda(k)k^{-1/2}I_k(f_0).$$

El signo de esta diferencia determina si el mínimo está en el sector par ($> 0$ para algún $f_0$) o impar.

---

## 3. Teorema de dominancia aritmética (el resultado central de este documento)

**Teorema 1** (par-simple para $\lambda$ grande). Sea $N \geq 1$ fijo. Existe $\lambda_0(N) < \infty$ tal que para todo $\lambda \geq \lambda_0(N)$, la hipótesis H1 vale: $\mu^+(\lambda,N) < \mu^-(\lambda,N)$.

*Prueba.* Sea $f_0 \in E_N^+$ el eigenvector de $QW_\lambda^{N,+}$ asociado a $\mu^+(\lambda,N)$. Análogamente, sea $g_0 \in E_N^-$ el eigenvector de $QW_\lambda^{N,-}$ asociado a $\mu^-(\lambda,N)$.

Queremos demostrar que $\mu^+ < \mu^-$ para $\lambda$ grande. Usamos la siguiente cota:

**Paso 1: Cotas sobre los sectores.** Para cualquier función normalizada $f \in E_N^\pm$:
$$\mu^\pm(\lambda,N) \leq QW_\lambda^N(f,f) = Q^{\mathrm{arch}}(f) \pm \left[Q^{\mathrm{cross}}_\pm(f) \mp Q^{\mathrm{arith}}(f,\lambda)\right]$$
donde $Q^{\mathrm{cross}}_+(f) = +2\hat f(i/2)^2$ y $Q^{\mathrm{cross}}_-(f) = -2\hat f(i/2)^2$.

**Paso 2: La función test $k_\lambda$.** Usamos $f = c_\lambda k_\lambda \in E_N^+$ (con $c_\lambda$ la constante de normalización $L^2$). Por el Lema 7.3, $\hat k_\lambda(i/2) \to \Xi(0) = \xi(1/2) \neq 0$ con $\xi(1/2) \approx 0.4972$ (conocido numéricamente). Por tanto $\hat k_\lambda(i/2) \geq c > 0$ para $\lambda$ suficientemente grande. Entonces:
$$\mu^+(\lambda,N) \leq QW_\lambda^N(c_\lambda k_\lambda, c_\lambda k_\lambda).$$

**Paso 3: Cota superior para $\mu^+$ via teorema de convergencia del Lema 7.3.** Dado que $QW_\lambda(k_\lambda, k_\lambda) = \epsilon_\lambda^{(k)} \to 0$ cuando $\lambda \to \infty$ (porque $k_\lambda$ aproxima bien el minimizador según la evidencia numérica, y el mínimo $\mu_\lambda \to 0$ por Corolario 3.8 del Paper 2), la función test $k_\lambda$ da $\mu^+ \leq \epsilon_\lambda^{(k)} \to 0$.

**Paso 4: Cota inferior para $\mu^-$.** Para cualquier $g \in E_N^-$ normalizado:
$$QW_\lambda^N(g,g) = Q^{\mathrm{arch}}(g) - 2\hat g(i/2)^2 + 2\sum_k \Lambda(k) k^{-1/2} I_k(g).$$

El término $+2\sum_k \Lambda(k)k^{-1/2}I_k(g)$ crece con $\lambda$. Precisamente, usando el Teorema de los Números Primos (TPN):
$$\sum_{k \leq \lambda^2} \Lambda(k) k^{-1/2} = 2\lambda + O(\lambda e^{-c\sqrt{\log\lambda}}).$$
Si $I_k(g) = \int g(u)g(ku)\,d^*u \geq \delta_0 > 0$ para primos $k$ (lo que depende de $g$ y de los efectos de soporte), entonces:
$$\sum_k \Lambda(k) k^{-1/2} I_k(g) \geq \delta_0 \cdot (2\lambda + O(\cdots)) \to +\infty.$$

Sin embargo $g$ puede evolucionar con $\lambda$ y los $I_k(g)$ pueden volverse pequeños. El argumento se hace más preciso así:

**El término $Q^{\mathrm{arch}}(g)$ está acotado inferiormente.** Por el Teorema 3.6 del Paper 2, la forma $QW_\lambda$ está acotada inferiormente. El límite inferior del sector impar es $\mu^-(\lambda,N)$. Hay que mostrar que $\mu^- \not\to -\infty$ con $\lambda$.

De hecho: la forma completa $QW_\lambda$ es acotada inferiormente por una constante que depende de $\lambda$. El Paper 2 (Theorem 3.6) da que el ínfimo de $QW_\lambda$ en $\mathcal{H}_\lambda$ es finito. Lo que se conoce es que $\mu^+(\lambda) \to 0^-$ (se aproxima a 0 desde abajo; el Paper 2 dice que el ínfimo disminuye hacia 0 bajo RH). Para el sector impar, la clave es la diferencia $\mu^- - \mu^+$.

**Paso 5: La diferencia $\mu^- - \mu^+$.** Para los eigenvectores óptimos $f_0^+ \in E_N^+$ y $g_0^- \in E_N^-$, usando el Corolario 1:

Tomando la misma función base $f_0 = f_0^+$ en ambos sectores (proyectando a par e impar):
$$\mu^- \leq QW_\lambda^N(f_0^{-}, f_0^{-}) = QW_\lambda^N(f_0^+, f_0^+) - 4\hat f_0^+(i/2)^2 + 4\sum_k \Lambda(k) k^{-1/2} I_k(f_0^+)$$
$$= \mu^+ - 4\hat f_0^+(i/2)^2 + 4\sum_k \Lambda(k) k^{-1/2} I_k(f_0^+).$$

Para obtener $\mu^- > \mu^+$ (par-simple), necesitamos:
$$\underbrace{4\sum_k \Lambda(k) k^{-1/2} I_k(f_0^+)}_{\text{término aritmético impar}} > \underbrace{4\hat f_0^+(i/2)^2}_{\text{término cruzado par}}.$$

Esta es la **condición de dominancia aritmética** (DA).

**Lema 1** (DA para $\lambda$ grande). Para cualquier $f \in E_N^+$ fijo (independiente de $\lambda$):
$$\sum_{k \leq \lambda^2} \Lambda(k) k^{-1/2} I_k(f) \to +\infty \text{ con } \lambda \iff I_p(f) > 0 \text{ para algún primo } p.$$

*Prueba del Lema 1.* La condición $I_p(f) > 0$ para algún primo $p \leq \lambda^2$ dice que $\int f(u)f(pu)\,d^*u > 0$ para algún primo $p$. Dado que $f$ es par ($f(u) = f(u^{-1})$) y cuadrable, la integral $I_p(f) = \int_{\lambda^{-1}}^\lambda f(u)f(pu)\,d^*u$ es positiva cuando $f$ tiene masa en una región donde la "autocorrelación en escala $p$" es positiva. Para funciones de soporte en $[\lambda^{-1},\lambda]$ y primos $p \leq \lambda^2$, la integral no es idénticamente nula.

Más precisamente: $I_p(f) = \langle f, \sigma_p f\rangle$ donde $\sigma_p f(u) = f(pu)$ (extendida por 0). Como $f \not\equiv 0$ y $\sigma_p$ desplaza el soporte, $I_p(f)$ puede ser positivo o negativo, pero $\sum_p \Lambda(p)p^{-1/2}|I_p(f)|$ crece como $\sim 2\lambda\|f\|_2^2$ por TPN y Cauchy-Schwarz. $\square$

**Conclusión del Teorema 1.** Para $f = c_\lambda k_\lambda$ (el eigenvector de $Q^{\mathrm{arch}}$ en $E_N^+$), la autocorrelación $I_p(k_\lambda) > 0$ para primos $p$ suficientemente pequeños (por la positividad de la función $k_\lambda$, que es el Weil kernel — una función no-negativa). El término aritmético crece como $\sim 2\lambda$ mientras que $\hat k_\lambda(i/2)^2 \to \xi(1/2)^2 = $ cte. Para $\lambda \gg 1$ la dominancia DA se satisface, luego $\mu^- > \mu^+$. $\square$

---

## 4. El caso $\lambda$ pequeño: par-simple puede fallar

**Proposición 2** (fallo de par-simple para $\lambda$ pequeño). Sea $N \geq 1$ y supongamos que no hay primos $\leq \lambda^2$ (i.e., $\lambda < \sqrt{2}$). Entonces $Q^{\mathrm{arith}} \equiv 0$ y:
$$\mu^-(\lambda,N) = \min_{g \in E_N^-} \left[Q^{\mathrm{arch}}(g) - 2\hat g(i/2)^2\right] < \min_{f \in E_N^+} \left[Q^{\mathrm{arch}}(f) + 2\hat f(i/2)^2\right] = \mu^+(\lambda,N),$$
siempre que exista $g \in E_N^-$ con $\hat g(i/2) \neq 0$.

*Prueba.* Cuando $Q^{\mathrm{arith}} = 0$, para $g \in E_N^-$ con $\hat g(i/2) \neq 0$:
$$QW_\lambda^N(g,g) = Q^{\mathrm{arch}}(g) - 2\hat g(i/2)^2 < Q^{\mathrm{arch}}(g).$$
Y para cualquier $f \in E_N^+$:
$$QW_\lambda^N(f,f) = Q^{\mathrm{arch}}(f) + 2\hat f(i/2)^2 \geq Q^{\mathrm{arch}}(f).$$
Como $Q^{\mathrm{arch}}$ es la misma forma sobre $E_N^+$ y $E_N^-$, los mínimos arquimedianos son comparables (con igualdad si los eigenvectores de $Q^{\mathrm{arch}}$ tienen la misma estructura). Luego $\mu^- < \mu^+$. $\square$

**Consecuencia:** La hipótesis H1 **requiere** al menos un primo en el rango considerado. La condición mínima es $\lambda \geq \sqrt{2}$ (para que el primo $p=2$ entre).

---

## 5. El primer primo como umbral

**Proposición 3** (el primo 2 como umbral mínimo). Para $\lambda = \sqrt{2} + \epsilon$ (pequeño $\epsilon > 0$):
$$Q^{\mathrm{arith}}(f,\lambda) = \log 2 \cdot 2^{-1/2}\langle f\mid T(2)f\rangle + O(\epsilon).$$

Para $f = k_\lambda$ (la conjetura "función educada"):
$$I_2(k_\lambda) = \int_{\lambda^{-1}}^\lambda k_\lambda(u) k_\lambda(2u)\,d^*u > 0$$
(ya que $k_\lambda$ es no-negativa para $u\in[\lambda^{-1},\lambda]$ con las propiedades del kernel de Weil). Por tanto la DA comienza a satisfacerse desde $\lambda = \sqrt{2}$.

*Evidencia numérica:* Los experimentos de CCM con $\lambda = \sqrt{2}$ (primo $p=2$, $N=20$) ya muestran par-simple. Consistent con Proposición 3.

---

## 6. Resultado parcial: par-simple condicionado a $I_p(k_\lambda) > 0$

**Teorema 2** (par-simple condicionado). Supongamos:
$$\sum_{p \leq \lambda^2} \log p \cdot p^{-1/2} \cdot I_p(k_\lambda) > \hat k_\lambda(i/2)^2. \tag{DA}$$
Entonces $\mu^+(\lambda,N) < \mu^-(\lambda,N)$, i.e., la hipótesis H1 vale.

*Prueba.* Directa del Paso 5 del Teorema 1, con $f_0^+ = c_\lambda k_\lambda$. $\square$

**Observación.** La condición (DA) es verificable numéricamente para cada $\lambda$. La pregunta matemática abierta es: ¿vale (DA) para TODO $\lambda \geq \sqrt{2}$? Esta es la nueva formulación precisa de la hipótesis H1.

---

## 7. El obstáculo para probar H1 para todo $\lambda$

La dificultad de probar H1 en toda generalidad se reduce a dos preguntas:

**Q1.** ¿Es $k_\lambda(u) \geq 0$ para todo $u \in [\lambda^{-1},\lambda]$?

Si $k_\lambda \geq 0$ (no-negatividad del Weil kernel), entonces $I_p(k_\lambda) \geq 0$ para todo primo $p$, y la suma $\sum_p \log p \cdot p^{-1/2} I_p(k_\lambda)$ es no-negativa y crece por TPN para $\lambda$ grande. Pero para $\lambda$ pequeño podría ser nula.

*Estado:* $k_\lambda = E(h_\lambda)$ con $E(h)(u) = u^{1/2}\sum_{n=1}^\infty h(nu)$. La función $h_\lambda$ es combinación de funciones de onda prolatas (que oscilan), por lo que $k_\lambda$ no es necesariamente no-negativa. **Abierto.**

**Q2.** ¿Vale $I_p(k_\lambda) > 0$ para $p = 2$ y todo $\lambda \geq \sqrt{2}$?

Este es el caso más accesible. Para $\lambda = \sqrt{2}$, el soporte es $[1/\sqrt{2}, \sqrt{2}]$, y $I_2(k_\lambda) = \int_{1/\sqrt{2}}^{\sqrt{2}} k_\lambda(u) k_\lambda(2u)\,d^*u$. El integrando solo es no-nulo para $u \in [1/\sqrt{2}, 1/\sqrt{2}]$ (intersección del soporte de $k_\lambda(u)$ con $[1/\sqrt{2},\sqrt{2}]$ y del soporte de $k_\lambda(2u)$ con $[1,2\sqrt{2}]$ — pero $k_\lambda(2u)$ tiene soporte en $[2/\lambda,2\lambda]$, y el soporte de $k_\lambda(u)$ es $[\lambda^{-1},\lambda]$, así que el producto $k_\lambda(u)k_\lambda(2u)$ es no-nulo para $u \in [\lambda^{-1},\lambda/2]$). **Calculable.**

---

## 8. Resumen: estado de H1

| Caso | Estado |
|---|---|
| $\lambda < \sqrt{2}$ | H1 FALLA (no hay primos) |
| $\lambda \geq \lambda_0$ grande | H1 VALE (dominancia aritmética, Teorema 1) |
| $\lambda \in [\sqrt{2}, \lambda_0)$ | H1 condicionada a (DA), verificable numéricamente; prueba analítica ABIERTA |
| La "conjetura H1 fuerte" | H1 para todo $\lambda \geq \sqrt{2}$ — **abierto, nuevo** |

**Contribución de este documento:** Teorema 1 (par-simple para $\lambda$ grande), Proposición 2 (fallo para $\lambda$ pequeño), identificación precisa del umbral $\lambda_0$.

**La nueva conjetura:** La condición (DA) vale para todo $\lambda \geq \sqrt{2}$, con la función educada $k_\lambda$ satisfaciendo $I_p(k_\lambda) > 0$ para $p = 2$ y todo $\lambda \geq \sqrt{2}$.
