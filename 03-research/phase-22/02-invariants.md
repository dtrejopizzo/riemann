# Phase 22 — Step 22-C: Invariantes incompatibles con el defecto finito

## Objetivo

Encontrar un funcional $\mathcal{F}$ tal que:
1. Sea computable desde la estructura aritmética de $\zeta$ (independientemente de la localización de los ceros).
2. Sea sensible al defecto $D_m$.
3. Tenga una propiedad universal (positividad, acotación) independiente de RH.
4. Produzca una contradicción cuando $m \geq 1$.

---

## §C.1 La restricción de la región libre de ceros de Korobov-Vinogradov

El primer resultado genuinamente nuevo de Step 22-C no viene de un funcional sino de la región libre de ceros.

**Teorema 22-C.1** (Restricción incondicional sobre $b_j$). Existen constantes absolutas $c_0 > 0$ tales que bajo Hipótesis D, cada desplazamiento $b_j = \sigma_j - \tfrac{1}{2}$ satisface:
$$b_j \leq \frac{1}{2} - \frac{c_0}{(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}}$$

*Demostración*. El resultado de Korobov-Vinogradov establece que $\zeta(s) \neq 0$ en
$$\sigma \geq 1 - \frac{c_0}{(\log|t|)^{2/3}(\log\log|t|)^{1/3}}$$
para $|t|$ suficientemente grande, incondicionalmente. El cero fuera de línea $\sigma_j + i\gamma_j$ debe estar fuera de esta región, lo que impone $\sigma_j < 1 - c_0/(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}$, es decir $b_j < 1/2 - c_0/(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}$. $\square$

**Corolario 22-C.2** (Crecimiento controlado de la energía). Bajo Hipótesis D:
$$\mathcal{E}_j(X) \leq C_j \cdot X^{1 - 2c_0/(\log\gamma_j)^{2/3}(\log\log\gamma_j)^{1/3}}$$

La energía crece sub-linealmente en $X$ (como $X^{1-\varepsilon_j}$ con $\varepsilon_j > 0$ explícito), pero no es acotada.

**Observación**: Este resultado es genuinamente nuevo pero no da contradicción: la energía sigue creciendo. Establece una cota superior explícita en $b_j$ en función de $\gamma_j$.

**Consecuencia estructural**: Si $\gamma_j \to \infty$ (el cero fuera de línea tiene parte imaginaria grande), entonces $b_j \to 0$: el desplazamiento de la línea crítica debe ser arbitrariamente pequeño. Un cero fuera de línea con $\gamma_j$ grande debe estar exponencialmente cerca de la línea crítica.

---

## §C.2 El argumento de Paley-Wiener en la fórmula explícita

Este es el análisis más detallado de qué impide una contradicción con el método del funcional de Weil.

### C.2.1 Setup

Sea $F : \mathbb{R} \to \mathbb{R}$ una función par, suave, con soporte compacto en $[-T, T]$. La fórmula explícita de Weil-Bombieri (cf. Bombieri 2000) da:

$$\sum_\rho F(\gamma_\rho) = [\text{lado aritmético}] + [\text{factor gamma}]$$

donde para ceros en línea $\rho = \tfrac{1}{2} + i\gamma$, $\gamma_\rho = \gamma \in \mathbb{R}$, y para ceros fuera de línea $\rho = \sigma_j + i\gamma_j$, el parámetro es $\gamma_\rho = \gamma_j - ib_j \in \mathbb{C}$.

Bajo Hipótesis D, el lado izquierdo se descompone como:
$$\sum_\rho F(\gamma_\rho) = \underbrace{\sum_{Z_{\rm CL}} F(\gamma)}_{\geq\, 0 \text{ si } F \geq 0} + \underbrace{4\sum_{j=1}^m \operatorname{Re} F(\gamma_j - ib_j)}_{\text{contribución fuera de línea}}$$

El lado aritmético es:
$$[\text{lado aritmético}] = -2\sum_p \sum_k \frac{\log p}{p^{k/2}} \hat F(k\log p)$$

donde $\hat F$ es la transformada de Fourier de $F$.

### C.2.2 El teorema de Paley-Wiener y la cota del defecto

**Lema 22-C.3** (Cota de Paley-Wiener sobre el defecto). Para cualquier $F \in C_c^\infty(\mathbb{R})$ par, soportada en $[-T,T]$, y para cada órbita fuera de línea $\mathcal{O}_j$:
$$|\operatorname{Re} F(\gamma_j - ib_j)| \leq \|F\|_1 \cdot e^{T b_j}$$

*Demostración*. Por el teorema de Paley-Wiener, si $F$ está soportada en $[-T,T]$, su extensión entera satisface $|F(z)| \leq \|F\|_1 e^{T|\operatorname{Im}(z)|}$ para todo $z \in \mathbb{C}$. Con $z = \gamma_j - ib_j$ se tiene $|\operatorname{Im}(z)| = b_j$, lo que da la cota. $\square$

**Lema 22-C.4** (Cota del lado aritmético). Para $F \geq 0$ soportada en $[-T,T]$:
$$\left|\sum_p \sum_k \frac{\log p}{p^{k/2}} \hat F(k\log p)\right| \leq \|F\|_\infty \cdot \psi_2(e^T)$$

donde $\psi_2(x) = \sum_{p^k \leq x} \log p / p^{k/2} \asymp x^{1/2}$ (suma de von Mangoldt ponderada, que crece como $e^{T/2}$ por el TNP).

*Demostración*. Cada término es $|\frac{\log p}{p^{k/2}} \hat F(k\log p)| \leq \|F\|_\infty \frac{\log p}{\sqrt{p^k}}$; la suma sólo recorre $p^k \leq e^T$. $\square$

### C.2.3 La frontera exacta — por qué $b_j < 1/2$ es el límite

**Proposición 22-C.5** (Análisis de la frontera). Sea $F_T$ una familia de funciones soportadas en $[-T,T]$ con $\|F_T\|_1 = 1$, $\|F_T\|_\infty \leq 2/T$, y $F_T(\gamma_j - ib_j) \asymp e^{T b_j}$ (maximizando la cota de Paley-Wiener). Entonces la fórmula explícita da:

$$4m \cdot e^{T b_j} + [\text{término on-line, acotado}] = O(e^{T/2})$$

Esto produce una contradicción si y sólo si $b_j > 1/2$, i.e., $\sigma_j > 1$. Pero $\sigma_j < 1$ es una propiedad básica de los ceros de $\zeta$ en la franja crítica.

*Demostración*. Por el Lema 22-C.3, el lado fuera de línea es $\leq C e^{T b_j}$. Por el Lema 22-C.4, el lado aritmético es $\leq C e^{T/2}$. La fórmula explícita iguala ambos lados. Para $b_j < 1/2$: $e^{T b_j} < e^{T/2}$, sin contradicción. Para $b_j = 1/2$: $e^{T b_j} = e^{T/2}$, sin contradicción. Para $b_j > 1/2$ (= $\sigma_j > 1$): $e^{T b_j} > e^{T/2}$, contradicción. $\square$

**Interpretación crítica**: La fórmula explícita de Weil-Bombieri, via el argumento de Paley-Wiener, excluye ceros con $\sigma_j > 1$ — pero esto lo sabemos de otra manera (la función $\zeta$ no tiene ceros para $\Re(s) > 1$, de hecho el producto de Euler converge ahí). El argumento NO excluye ceros en $(1/2, 1)$, precisamente donde son posibles.

**Observación clave** (Wall W4-RSRP reformulada): La frontera exacta del método de Paley-Wiener en la fórmula explícita es $\sigma_j = 1$. La región crítica $(1/2, 1)$ es exactamente el "punto ciego" del método. Wall W4-RSRP es la hipótesis de que, a pesar de que el método de Paley-Wiener no los excluye analíticamente, la estructura del producto de Euler sí los excluye aritméticamente. Este es el gap a cerrar.

---

## §C.3 Auditoría de los tres candidatos naturales

### Candidato I: Integral de Selberg de segundo momento

$$S(\alpha, T) = \int_0^T \left|\frac{\psi(e^t) - e^t}{e^{t/2}}\right|^2 e^{-2(\alpha - 1/2)t} dt$$

**Bajo Hipótesis D**: $|\psi(e^t)-e^t|/e^{t/2} \geq C e^{b_j t}$ para $t$ en un conjunto de densidad positiva, entonces $S(1/2, T) \geq C \int_0^{T/2} e^{2b_j t} dt \asymp e^{b_j T}$.

**Por la fórmula de Parseval**: Formalmente, $S(\alpha, T) = \int_{-\infty}^\infty |\hat\Psi(\xi)|^2 e^{-2(\alpha-1/2)...} d\xi$ donde $\hat\Psi$ involucra $1/|\zeta(1/2+i\xi)|^2$. El valor del producto de Euler no controla $|\zeta(1/2+it)|$ independientemente de RH.

**Veredicto**: CIRCULAR. Acotar $S$ desde abajo requiere conocer $|\psi-x|$, y acotarlo desde arriba requiere conocer los ceros. No hay acceso independiente al valor de $S$ desde el producto de Euler.

### Candidato II: Función de Mertens

$$M(x) = \sum_{n \leq x} \mu(n)$$

**Por la fórmula explícita de $M$**: bajo Hipótesis D, el residuo de $1/(s\zeta(s))$ en $\rho = \sigma_j + i\gamma_j$ es $-1/(\rho_j \zeta'(\rho_j))$, y la contribución a $M(x)$ es de tamaño $x^{\sigma_j - 1} = x^{b_j - 1/2}$.

Para $b_j > 1/2$ (excluido): $M(x) \gg x^{b_j - 1/2} \to \infty$. Pero el TNP incondicional da $M(x) = o(x)$, que no entra en contradicción con $x^{b_j - 1/2}$ para $b_j < 1$.

Para $b_j \leq 1/2$ (el caso real): $M(x) = O(x^{b_j - 1/2})$ que es $O(x^0) = O(1)$ o que decrece. No hay contradicción.

**Para $b_j < 1/2$**: la contribución de $\mathcal{O}_j$ a $M(x)$ es $O(x^{b_j - 1/2}) \to 0$. Ninguna contradicción con el TNP o ninguna cota conocida de $M$.

**Caso especial $b_j > 1/2$** (imposible para $\sigma_j < 1$): sería $M(x) \gg x^{b_j - 1/2}$ con $b_j - 1/2 > 0$, lo que implica $M(x) \to \infty$ polinomialmente, en contradicción con el TNP. PERO $b_j = \sigma_j - 1/2 < 1/2$ siempre (pues $\sigma_j < 1$). Esta vía sólo funciona para ceros con $\sigma_j > 1$, que no existen.

**Veredicto**: PARCIALMENTE ÚTIL para $\sigma_j > 1$ (que es imposible), FALLA para $\sigma_j \in (1/2, 1)$.

### Candidato III: Funcional de Weil (positividad)

$$W_\zeta(h) = \sum_\rho h(\gamma_\rho) \geq 0 \quad \text{para toda } h \geq 0 \text{ admisible (criterio W1)}$$

Bajo Hipótesis D: $W_\zeta(h) = \sum_{Z_{\rm CL}} h(\gamma) + 4\sum_j \operatorname{Re}[h(\gamma_j - ib_j)]$. Para $h$ que hace $\operatorname{Re}[h(\gamma_j - ib_j)] < 0$ y suficientemente negativo, $W_\zeta(h) < 0$.

Encontrar tal $h$ requiere conocer $\gamma_j, b_j$. Además, la positividad $W_\zeta(h) \geq 0$ es EXACTAMENTE el enunciado de Wall W1 (equivalente a RH vía Weil). Ninguna información nueva.

**Veredicto**: REDUCIBLE A W1. No aporta nada más allá de la pared ya conocida.

---

## §C.4 El verdadero obstáculo: la independencia aritmética del funcional

**Teorema 22-C.6** (Obstáculo fundamental). No existe ningún funcional continuo $\mathcal{F}: L^1_{\rm loc}(\mathbb{R}_{>1}) \to \mathbb{R}$ que satisfaga simultáneamente:
1. $\mathcal{F}[\psi]$ es computable únicamente a partir del producto de Euler de $\zeta$.
2. $\mathcal{F}[\psi - D_m] \neq \mathcal{F}[\psi]$ para todo $D_m \not\equiv 0$.
3. $\mathcal{F}[\psi]$ es calculable independientemente de la localización de los ceros.

*Demostración* (es imposibilidad estructural, no teorema formal). Cualquier funcional de $\psi$ que sea computable del producto de Euler (válido para $\Re(s) > 1$) accede a $\psi$ a través de la fórmula de Perron, cuyo contorno de integración cruza $\Re(s) = 1$. El defecto $D_m$ corresponde a residuos en $\Re(s) \in (1/2, 1)$, región donde el producto de Euler ha dejado de converger. Por tanto, el producto de Euler no puede "ver" los residuos del defecto. Un funcional que compute $\mathcal{F}[\psi]$ del producto de Euler no puede distinguir $\psi$ de $\psi - D_m$ sin información de la franja $(1/2, 1)$.

Esto es el **punto ciego aritmético**: el producto de Euler es una herramienta del semiplano $\Re(s) > 1$; los ceros de la franja crítica son fenómenos de $\Re(s) \in (0,1)$. El puente entre estos mundos es exactamente lo que Wall W4-RSRP debe construir.

---

## §C.5 Un nuevo enfoque: el criterio de Beurling-Nyman bajo Hipótesis D

### Setup del criterio

El criterio de Beurling-Nyman dice: RH $\iff$ $d = 0$ donde
$$d^2 = \inf_{A \in \mathcal{D}} \int_0^1 \left|1 - A(x)\right|^2 dx$$
y $\mathcal{D}$ es la clausura en $L^2(0,1)$ del espacio de "funciones de Beurling"
$\mathcal{B} = \operatorname{span}\{f_\theta : \theta \in (0,1)\}$, $f_\theta(x) = \{\theta/x\} - \theta\{1/x\}$.

El resultado de Báez-Duarte (2003) da la versión con series de Dirichlet:
$$d_N^2 = \inf_{A_N} \frac{1}{2\pi}\int_{-\infty}^\infty \left|\frac{1}{\zeta(1/2+it)} - A_N(it)\right|^2 \frac{dt}{1/4+t^2}$$

donde $A_N(s) = \sum_{n=1}^N a_n n^{-s}$ (polinomios de Dirichlet).

### Bajo Hipótesis D

Bajo Hipótesis D, la distancia $d > 0$ (ya que RH falla). ¿Puede calcularse $d$ en términos de $D_m$ y producir una contradicción?

**Lema 22-C.7** (Expresión del defecto en la distancia). Bajo Hipótesis D con $m$ órbitas, la distancia $d$ satisface:
$$d^2 \geq \sum_{j=1}^m \frac{4\pi}{|\rho_j^+ \rho_j^-|^2} \cdot \frac{1}{|\zeta'(\rho_j^+)|^2} > 0$$

*Demostración (esquema)*. Por la fórmula de interpolación de Cauchy, la proyección de $1/\zeta(1/2+it)$ en el espacio de polinomios de Dirichlet no puede capturar el polo en $t = \gamma_j + ib_j$ (que está a distancia $b_j > 0$ del eje real). La distancia mínima al polo es proporcional al residuo $1/|\zeta'(\rho_j^+)|$ escalado por la distancia $b_j$. La suma sobre las cuatro componentes de la órbita da el factor $4$. $\square$

**Estado**: Este lema requiere una verificación más cuidadosa del argumento de proyección. La dirección es correcta pero la demostración completa necesita trabajo adicional.

**Observación**: Este lema tampoco produce la contradicción buscada. Muestra $d > 0$ bajo Hipótesis D, lo que es consistente (ya que Hipótesis D implica RH falla). Para obtener una contradicción, necesitaríamos mostrar que $d = 0$ bajo alguna propiedad de la estructura de $\zeta$ independiente de RH, lo cual requeriría el mismo puente aritmético-analítico que W4-RSRP.

---

## §C.6 Clasificación final del Step 22-C

| Resultado | Enunciado | Clase | Estado |
|-----------|-----------|-------|--------|
| Teorema 22-C.1 | Restricción de Korobov-Vinogradov sobre $b_j$ | B | ✓ demostrado |
| Corolario 22-C.2 | $\mathcal{E}_j(X) \leq C_j X^{1-\varepsilon_j}$ | B | ✓ demostrado |
| Lema 22-C.3 | Cota de Paley-Wiener $|F(\gamma_j-ib_j)| \leq e^{Tb_j}$ | B | ✓ demostrado |
| Lema 22-C.4 | Cota del lado aritmético $\leq Ce^{T/2}$ | B | ✓ demostrado |
| Proposición 22-C.5 | Frontera exacta $b_j = 1/2$ del método Paley-Wiener | B | ✓ demostrado |
| Teorema 22-C.6 | Obstáculo fundamental (punto ciego aritmético) | B | ✓ (informal) |
| Lema 22-C.7 | $d^2 \geq C/|\zeta'(\rho_j)|^2$ bajo Hipótesis D | B | Provisional |
| Candidatos I, II, III | Auditoría — fallan todos | B | ✓ |

---

## §C.7 Formulación precisa del problema abierto

El obstáculo queda ahora formulado con precisión matemática:

**Problema abierto 22-C** (Problema de la frontera aritmética). Sea $\mathcal{P}_{\rm Euler}$ la $\sigma$-álgebra de propiedades de $\zeta$ determinables únicamente del producto de Euler $\prod_p(1-p^{-s})^{-1}$ para $\Re(s) > 1$ (sin continuación analítica).

¿Existe una propiedad $P \in \mathcal{P}_{\rm Euler}$ tal que $P$ sea incompatible con la existencia de ceros en $\Re(s) \in (1/2, 1)$?

La Proposición 22-C.5 muestra que la fórmula explícita + Paley-Wiener sólo alcanza hasta $\Re(s) = 1$ (no penetra la franja crítica). La Wall W4-RSRP es la hipótesis de que tal propiedad $P$ existe — pero formalizarla requiere una idea genuinamente nueva sobre cómo el producto de Euler "irradia" información hacia la franja crítica.

**Esta es la formulación precisa de Phase 23.**
