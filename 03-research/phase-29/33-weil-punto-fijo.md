# Phase 29 — Doc 33: Dirección A — La Fórmula Explícita como Ecuación de Punto Fijo

**Fecha:** junio 2026  
**Dirección:** A (auto-referencia de la fórmula explícita)  
**Objetivo:** Investigar si la fórmula de Guinand-Weil, evaluada en los ceros de $\Xi$, implica $C_\infty(\gamma_n) = 0$ incondicionalmente — es decir, si la estructura auto-referencial de la fórmula explícita fuerza Inc. Inv.

---

## 1. La estructura auto-referencial del programa CCM

**El ciclo.** La construcción CCM produce el operador $J_\infty$ cuyos coeficientes de Jacobi son:

$$b_n^\infty = \gamma_n, \quad a_n^\infty = \frac{\pi}{\log\gamma_n},$$

donde $\{\gamma_n\}$ son las partes imaginarias de los ceros de $\zeta$ sobre la recta crítica. Los eigenvalores de $J_\infty$ son los ceros de $C_\infty$, que a su vez deben ser (si Inc. Inv.) los mismos $\{\gamma_n\}$.

Esto es una **ecuación de punto fijo**: los ceros de $\zeta$ (input de $J_\infty$) = eigenvalores de $J_\infty$ (output).

**Pregunta principal.** ¿Existe un argumento que force esta ecuación de punto fijo sin asumir Inc. Inv. a priori?

---

## 2. La fórmula de Guinand-Weil

**La fórmula (forma de Barner).** Para toda función de prueba $h: \mathbb{R} \to \mathbb{C}$ en la clase de Schwartz $\mathcal{S}(\mathbb{R})$:

$$\sum_\rho h\!\left(\frac{\gamma_\rho}{2\pi}\right) = \hat h(0)\log\pi - \frac{1}{2}\hat h(0)\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}\right) + \int_{-\infty}^\infty h(t)\,\frac{d}{dt}\log\!\left|\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right|\,dt$$
$$- \sum_{p \text{ primo}}\sum_{k\geq 1} \frac{\Lambda(p^k)}{p^{k/2}}\!\left[h\!\left(\frac{\log p^k}{2\pi}\right)+h\!\left(-\frac{\log p^k}{2\pi}\right)\right],$$

donde la suma izquierda recorre todos los ceros no-triviales $\rho$ de $\zeta$ (con $\gamma_\rho = \Im(\rho)$), y $\Lambda$ es la función de von Mangoldt.

Esta es una identidad entre sumas sobre CEROS y sumas sobre PRIMOS.

---

## 3. Evaluación en un cero: intento de la función delta

**Función de prueba localizada.** Formalmente: sea $h_\varepsilon(t) = \phi_\varepsilon(t - \gamma_m/(2\pi))$ donde $\phi_\varepsilon$ es una aproximación a la delta en $t=0$, concentrada en $\varepsilon\to 0$.

En el límite $\varepsilon \to 0$: $h_\varepsilon \to \delta(\cdot - \gamma_m/(2\pi))$, de modo que:

- Lado izquierdo: $\sum_\rho h_\varepsilon(\gamma_\rho/(2\pi)) \to \sum_\rho \delta(\gamma_\rho/(2\pi) - \gamma_m/(2\pi)) = \sum_\rho \delta((\gamma_\rho - \gamma_m)/(2\pi))$.

  Si los $\gamma_n$ son simples (ningún cero repetido): el único término no nulo es el de $\gamma_\rho = \gamma_m$, que da $2\pi \cdot 1$ (si $\rho_m = 1/2 + i\gamma_m$ es un cero simple) más su conjugado $\bar\rho_m = 1/2 - i\gamma_m$ que da otro $2\pi$.

  Total izquierdo (bajo RH): $2 \cdot 2\pi = 4\pi$ (si asumimos $\gamma_m > 0$; el cero y su conjugado).

- Lado derecho: $[\text{términos de }w] - [\text{términos de primos}] = w(\gamma_m) - \Psi(\gamma_m)$.

**La identidad delta:** $4\pi = w(\gamma_m) - \Psi(\gamma_m) = C_\infty(\gamma_m) + [\text{términos de normalización}]$.

Esto daría $C_\infty(\gamma_m) = $ constante $\neq 0$ — NO cero.

**El problema.** La función delta no está en la clase de Schwartz: la fórmula de Weil requiere $h \in \mathcal{S}(\mathbb{R})$ (decaimiento rápido y suavidad). Con $h_\varepsilon \to \delta$, los términos del lado derecho DIVERGEN a medida que $\varepsilon \to 0$. En particular:

$$\sum_{p,k} \frac{\Lambda(p^k)}{p^{k/2}} h_\varepsilon\!\left(\frac{\log p^k}{2\pi}\right) \sim \sum_{p,k} \frac{\Lambda(p^k)}{p^{k/2}} \phi_\varepsilon\!\left(\frac{\log p^k}{2\pi} - \frac{\gamma_m}{2\pi}\right) \to \infty,$$

ya que el número de primos $p^k$ con $\log p^k \approx \gamma_m$ (en la ventana $[0,2\pi]$) crece con $\varepsilon^{-1}$.

**Conclusión (negativa).** La evaluación en una delta no es admisible: la fórmula de Weil diverge para funciones de prueba no-Schwartz.

---

## 4. Funciones de prueba admisibles localizadas en $\gamma_m$

**Clase de sustitutos.** En lugar de $\delta(\cdot - \gamma_m)$, se usan funciones de prueba de ancho $\varepsilon > 0$:

$$h_\varepsilon(t) = \varepsilon^{-1}\phi\!\left(\frac{t-\gamma_m/(2\pi)}{\varepsilon}\right),$$

con $\phi \in \mathcal{S}(\mathbb{R})$, $\int \phi = 1$, $\operatorname{supp}\phi \subset [-1,1]$.

**Proposición 1** (la fórmula de Weil a escala $\varepsilon$). Para $h_\varepsilon$ como arriba:

$$\text{Lado izquierdo:} \quad \sum_\rho \varepsilon^{-1}\phi\!\left(\frac{\gamma_\rho - \gamma_m}{2\pi\varepsilon}\right) = \varepsilon^{-1}\phi(0) + \sum_{\rho \neq \rho_m} \varepsilon^{-1}\phi\!\left(\frac{\gamma_\rho - \gamma_m}{2\pi\varepsilon}\right).$$

Para $\varepsilon$ pequeño: solo el cero $\rho_m = 1/2+i\gamma_m$ (y su conjugado) contribuyen significativamente. La suma da $\approx \varepsilon^{-1}[\phi(0) + \phi(0)] = 2\varepsilon^{-1}\phi(0)$.

**Proposición 2** (el lado derecho en la escala $\varepsilon$). El lado derecho tiene dos contribuciones:

1. Término arquimediano: $\int h_\varepsilon(t)\frac{d}{dt}\log|\Gamma(\ldots)|\,dt \approx \frac{d}{dt}\log|\Gamma(\tfrac{1}{4}+\tfrac{it}{2})||_{t=\gamma_m} = w(\gamma_m) + O(\varepsilon)$ (por suavidad de $w$).

2. Términos de primos: $\sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\varepsilon^{-1}\phi\!\left(\frac{\log p^k/(2\pi) - \gamma_m/(2\pi)}{\varepsilon}\right)$.

   Esta es la suma de $\varepsilon^{-1}\phi((\log p^k - \gamma_m)/(2\pi\varepsilon))$ sobre todos los primos $p^k$. En el límite $\varepsilon \to 0$: se comporta como una distribución aplicada al "espectro primo" $\{\log p^k\}$.

**La identidad en el límite $\varepsilon \to 0$.**

$$2\varepsilon^{-1}\phi(0) \approx w(\gamma_m) - \varepsilon^{-1}\int_{-\infty}^\infty \phi(u)\,d\Psi_\varepsilon(\gamma_m + 2\pi\varepsilon u),$$

donde $\Psi_\varepsilon$ es la función primo suavizada a escala $\varepsilon$.

Los dos términos de orden $\varepsilon^{-1}$ deben igualarse. Si la parte prima $\varepsilon^{-1}\int\phi(u)\,d\Psi_\varepsilon = 2\varepsilon^{-1}\phi(0) + \Psi_\varepsilon'(\gamma_m) + O(\varepsilon)$, entonces:

$$0 = w(\gamma_m) - \Psi_\varepsilon'(\gamma_m) + O(\varepsilon).$$

Tomando $\varepsilon \to 0$: $C_\infty(\gamma_m) = w(\gamma_m) - \Psi'_0(\gamma_m) = 0$?

---

## 5. El obstáculo: la derivada distribucional de $\Psi$

**Definición.** Para $\varepsilon > 0$:

$$\Psi_\varepsilon'(t) := \frac{d}{d t}\!\left[\sum_{p,k} \frac{\Lambda(p^k)}{p^{k/2}} \varepsilon^{-1}\hat\phi\!\left(\frac{(t-\log p^k)}{2\pi\varepsilon}\right)\right] = \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\cdot\frac{-1}{2\pi\varepsilon^2}\phi'\!\left(\frac{t-\log p^k}{2\pi\varepsilon}\right).$$

Cuando $\varepsilon \to 0$: $\Psi_\varepsilon'(t) \to \frac{d}{dt}[$ distribución $]$.

**Proposición 3** (la derivada de $\Psi$ en distribución). La derivada distribucional de $\Psi(t) = 2\sum_{p,k}\Lambda(p^k)p^{-k/2}\cos(t\log p^k)$ es:

$$\Psi'(t) = -2\sum_{p,k}\Lambda(p^k)p^{-k/2}\log(p^k)\sin(t\log p^k).$$

Esta serie TAMBIÉN diverge (los términos son $\Lambda(p^k)\log(p^k)p^{-k/2} = (\log p^k)^2 p^{-k/2}$, que no es absolutamente sumable).

**El resultado negativo.** La condición $w(\gamma_m) - \Psi_\varepsilon'(\gamma_m) = 0$ en el límite $\varepsilon \to 0$ involucra la derivada distribucional de $\Psi$, que no está bien definida como función. El límite $\varepsilon \to 0$ no puede tomarse directamente.

---

## 6. La fórmula de Weil como identidad de distribuciones

**Reinterpretación.** La fórmula de Weil no dice que $C_\infty(\gamma_m) = 0$ para un $\gamma_m$ específico. Dice que la DISTRIBUCIÓN $\sum_\rho \delta(\gamma - \gamma_\rho)$ (medida espectral de los ceros de $\zeta$) es igual a una distribución expresada en términos de primos.

La condición $C_\infty(\gamma_m) = 0$ es una afirmación PUNTUAL sobre $C_\infty$, mientras que la fórmula de Weil es una identidad entre distribuciones integrales.

**Teorema 1** (lo que da la fórmula de Weil). La fórmula de Weil establece:

$$\sum_\rho \langle f, \delta_{\gamma_\rho}\rangle = \langle f, w'\rangle - \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\left[f(\log p^k) + f(-\log p^k)\right]$$

para toda $f \in \mathcal{S}(\mathbb{R})$. Esto es:

$$\mu_\gamma = w' - d\Psi \quad \text{en sentido distribucional},$$

donde $\mu_\gamma = \sum_\rho \delta_{\gamma_\rho}$ y $d\Psi = \sum_{p,k}\Lambda(p^k)p^{-k/2}[\delta_{\log p^k} + \delta_{-\log p^k}]$ (medida de Dirac sobre los logaritmos de las potencias de primos).

**Lo que NO dice.** La fórmula de Weil establece $d\mu_\gamma = w' - d\Psi$ distributionalmente, pero NO dice que $w(\gamma_m) - \Psi(\gamma_m) = 0$ para cada $\gamma_m$ individual. Son objetos de diferente naturaleza: $w'$ es la derivada de una función suave, $d\Psi$ es una medida discreta, y la diferencia es una distribución.

---

## 7. El punto fijo desde la perspectiva funcional

**Definición del operador de iteración.** Sea $\mathcal{F}: \{\text{conjuntos de } \mathbb{R}\} \to \{\text{conjuntos de } \mathbb{R}\}$ el operador:

$$\mathcal{F}(\mathcal{Z}) := \{t \in \mathbb{R}: C_\infty^{\mathcal{Z}}(t) = 0\},$$

donde $C_\infty^{\mathcal{Z}}(t) = w(t) - 2\sum_\rho \cos(t\log|\rho|)/|\rho|$ y la suma es sobre los ceros $\rho$ de $\zeta$ cuyas partes imaginarias son $\mathcal{Z}$.

Un punto fijo de $\mathcal{F}$ es un conjunto $\mathcal{Z}^*$ tal que $\mathcal{F}(\mathcal{Z}^*) = \mathcal{Z}^*$.

**La ecuación de punto fijo explícita.** $\mathcal{Z}^* = \{\gamma_n\}$ si y solo si: para cada $n$,

$$C_\infty^{\{\gamma_n\}}(\gamma_n) = w(\gamma_n) - 2\sum_m \frac{\cos(\gamma_n\log|\rho_m|)}{|\rho_m|} = 0,$$

donde $\rho_m = 1/2 + i\gamma_m$ (bajo RH) o $\rho_m = \sigma_m + i\gamma_m$ (en general).

**Proposición 4** (la ecuación de punto fijo es Inc. Inv.). El conjunto $\{\gamma_n\}$ es punto fijo de $\mathcal{F}$ si y solo si Inc. Inv. es cierta.

*Prueba.* Directo de la definición: $\mathcal{F}(\{\gamma_n\}) = \{\gamma_n\}$ iff cada $\gamma_n$ es cero de $C_\infty^{\{\gamma_n\}} = C_\infty$. Pero $\{C_\infty=0\} \subseteq \{\gamma_n\}$ (Teorema B, Doc 19), así que la igualdad de conjuntos requiere que cada $\gamma_n$ sea un cero de $C_\infty$, que es exactamente Inc. Inv. $\square$

---

## 8. Existencia y unicidad del punto fijo

**Proposición 5** (existencia trivial). El conjunto vacío $\mathcal{Z}^* = \emptyset$ es un punto fijo trivial de $\mathcal{F}$ (vacuamente: ningún $\gamma_n$ que satisfacer la condición de cero). El punto fijo interesante es $\mathcal{Z}^* = \{\gamma_n\}$ — el conjunto de ceros de $\Xi$.

**Proposición 6** (la unicidad como vía de ataque). Si $\mathcal{F}$ tiene un ÚNICO punto fijo no-vacío: y si la fórmula de Weil implica que las partes imaginarias de los ceros de $\zeta$ forman un punto fijo de $\mathcal{F}$, entonces ese punto fijo es $\{\gamma_n\}$.

**El obstáculo para la unicidad.** Para mostrar unicidad del punto fijo de $\mathcal{F}$, se necesita:

(a) $\mathcal{F}$ es una contracción (en alguna métrica adecuada sobre conjuntos discretos de $\mathbb{R}$).

(b) O: $\mathcal{F}$ tiene estructura monotona (preserva el orden de los conjuntos) y tiene punto fijo superior/inferior.

Ninguna de estas propiedades es obvia para $\mathcal{F}$ como está definido.

---

## 9. La fórmula de Weil y la ecuación de auto-consistencia

**Proposición 7** (auto-consistencia de la fórmula de Weil). La fórmula de Weil, cuando se specializa a $h(t) = e^{ist}$ (función exponencial en la "variable $t$"), da:

$$\sum_\rho e^{is\gamma_\rho} = \hat w(s) - \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}}\left[e^{is\log p^k} + e^{-is\log p^k}\right] \cdot(\text{factor de escala}).$$

La condición $C_\infty(\gamma_m) = 0$ se escribiría como:

$$w(\gamma_m) = \sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2}} \cdot 2\cos(\gamma_m\log p^k).$$

Pero por la fórmula explícita (válida para $s = 1/2+i\gamma_m$ cero de $\zeta$):

$$\sum_{p,k}\frac{\Lambda(p^k)}{p^{k/2+i\gamma_m}} = \sum_\rho \frac{1}{\gamma_m - \gamma_\rho + [\text{términos del polo/triviales}]}.$$

Esto relaciona el lado primo en $t=\gamma_m$ con una suma sobre TODOS los ceros $\rho$ (un "coupling" global).

**Teorema 2** (lo que sí puede probarse). Bajo la hipótesis de que los ceros de $\zeta$ son SIMPLES y que la parte prima de la fórmula explícita converge absolutamente en $s = 1/2 + i\gamma_m$:

$$C_\infty(\gamma_m) = \text{Res}_{s=\rho_m}\!\left(-\frac{\zeta'}{\zeta}(s)\right) \cdot f(\gamma_m) = 1 \cdot f(\gamma_m),$$

donde $f(\gamma_m)$ es un factor que depende de la normalización. Si $f(\gamma_m) = 0$: entonces $C_\infty(\gamma_m) = 0$ — Inc. Inv. sería consecuencia.

**El problema.** El residuo $\text{Res}_{s=\rho_m}(-\zeta'/\zeta(s)) = 1$ (para cero simple de $\zeta$), que es NO CERO. El factor $f(\gamma_m)$ mide si la contribución del residuo CANCEL algún otro término. Sin información sobre $f$, no puede concluirse.

---

## 10. Intento via la fórmula de Hadamard para $\Xi$

**La factorización de Hadamard de $\Xi$.** La función completa $\Xi(z) = \Xi(0)\prod_n(1-z/\gamma_n)(1+z/\gamma_n)$ (ceros simples sobre $\mathbb{R}$ bajo RH). Su derivada logarítmica:

$$\frac{\Xi'(z)}{\Xi(z)} = \sum_n\left(\frac{1}{z-\gamma_n} + \frac{1}{z+\gamma_n}\right).$$

**La factorización de Hadamard de $C_\infty$.** Por el Teorema B (Doc 19): $\{C_\infty=0\} \subseteq \{\Xi=0\} = \{\pm\gamma_n\}$. Si denotamos por $\{\pm\alpha_j\}$ los ceros de $C_\infty$ (un subconjunto de $\{\pm\gamma_n\}$), entonces:

$$C_\infty(z) = C_\infty(0)\prod_j\left(1-\frac{z}{\alpha_j}\right)\!\left(1+\frac{z}{\alpha_j}\right) \cdot e^{Q(z)},$$

donde $Q(z)$ es una función entera de orden $\leq 1$ (factor exponencial de Hadamard).

**Inc. Inv. $\Leftrightarrow$ $\{\alpha_j\} = \{\gamma_n\}$ (todos los ceros de $\Xi$).**

**Proposición 8** (la razón $C_\infty/\Xi^{2q}$). Si $C_\infty(z) = K\cdot\Xi(z)^{2q}\cdot e^{Q(z)}$ para algún entero $q \geq 1$: los ceros de $C_\infty$ son los mismos que los de $\Xi$ (con multiplicidad $2q$), y la inclusión directa $\{C_\infty=0\} \subseteq \{\Xi=0\}$ es satisfecha con igualdad. Esto daría Inc. Inv. si $q \geq 1$.

**El obstáculo.** Probar que $C_\infty/\Xi^{2q}$ es entera (o que tiene la forma $Ke^{Q}$) sin asumir Inc. Inv. requiere información sobre el CRECIMIENTO de $C_\infty$ en el plano complejo, que a su vez requiere información sobre los zeros de $\Xi$ (circular).

---

## 11. Conclusión de la Dirección A

**Resultado positivo.** La estructura de punto fijo está identificada: Inc. Inv. $\Leftrightarrow$ $\{\gamma_n\}$ es punto fijo de $\mathcal{F}$ (Proposición 4).

**Resultado negativo.** La fórmula de Weil NO puede evaluarse en $t = \gamma_m$ puntualmente (diverge). La fórmula da información INTEGRAL sobre la distribución de los $\gamma_n$, no puntual.

**El obstáculo central.** La fórmula de Weil dice que la DISTRIBUCIÓN de los ceros $\gamma_n$ es consistente con la distribución de los primos. Pero no dice que cada $\gamma_n$ individual sea un cero de $C_\infty$. La información integral (global) no implica la información puntual (local).

**Analogía clarificadora.** La ley de los grandes números dice que la media de $n$ variables aleatorias converge a la media. Pero no dice nada sobre el valor de cada variable individual. La fórmula de Weil es análoga: relaciona la MEDIA de los $\gamma_n$ (en algún sentido espectral) con la MEDIA de los primos, pero no dice nada sobre cada $\gamma_n$ individualmente.

**La vía más prometedora de A.** Para recuperar información puntual desde la fórmula distribucional: se necesita un "principio de separación" que diga que si la distribución de los $\gamma_n$ coincide exactamente con la distribución de los ceros de $C_\infty$, entonces los conjuntos son iguales. Esto requiere las medidas espectral (de $J_\infty$) y la de $\Xi$ sean la misma medida (no solo que tengan los mismos momentos). Este es precisamente el contenido de la hipótesis de determinacy del Doc 26, que resultó ser INDETERMINADA para $\mu_\gamma^{real}$.

**Conexión con Doc 26.** El problema del momento para $\mu_\gamma^{real}$ es indeterminado (Doc 26), lo que significa que la información integral (momentos) NO determina la medida puntualmente. Esto explica por qué el camino "fórmula de Weil $\Rightarrow$ punto fijo $\Rightarrow$ Inc. Inv." no puede completarse: se necesita más que momentos.

---

*Siguiente doc: Doc 34 — Dirección C: Phragmén-Lindelöf para el Cociente $Q$.*
