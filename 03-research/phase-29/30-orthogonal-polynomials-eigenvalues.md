# Phase 29 — Doc 30: Polinomios Ortogonales, Eigenvalores y la Estructura Auto-referencial de $J_\infty$

**Fecha:** junio 2026  
**Contexto:** El Doc 29 redujo Inc. Inv. a: ¿es $\gamma_n \in \text{spec}(J_\infty)$ para todo $n$? Y observó que los polinomios ortogonales $p_k(\gamma_n)$ crecen super-exponencialmente. Este doc resuelve la aparente contradicción y descubre la estructura auto-referencial del programa.

---

## 1. El operador $J_\infty$: compacticidad y teoría de límite-punto

**Proposición 1** (compacticidad de $J_\infty$). El operador $J_\infty$ con $a_n^\infty = \pi/\log\gamma_n \to 0$ y $b_n^\infty = 0$ es un operador COMPACTO auto-adjunto en $\ell^2(\mathbb{N}_0)$.

*Prueba.* La norma de la cola del operador: $\|J_\infty - J_\infty^{(N)}\|_{op} \leq 2\sup_{n\geq N} a_n^\infty = 2\pi/\log\gamma_N \to 0$ cuando $N\to\infty$. Luego $J_\infty$ es límite en norma de operadores de rango finito: es compacto. $\square$

**Corolario 1** (espectro discreto de $J_\infty$). El espectro de $J_\infty$ consiste en eigenvalores discretos acumulándose solo en $0$:

$$\text{spec}(J_\infty) = \{0\} \cup \{t_n^C\}_{n=1}^\infty,$$

donde $t_n^C \to 0$ cuando $n\to\infty$. Cada $t_n^C$ tiene multiplicidad finita.

*Prueba.* Teorema espectral para operadores compactos auto-adjuntos. $\square$

**Proposición 2** (caso límite-punto). Con la condición de Carleman:

$$\sum_{n=0}^\infty \frac{1}{a_n^\infty} = \frac{1}{\pi}\sum_{n=0}^\infty \log\gamma_n = +\infty,$$

el operador $J_\infty$ está en el caso LÍMITE-PUNTO: hay exactamente una solución $\ell^2$ de la ecuación de eigenvalor para cada $z \in \mathbb{C}^+$.

*Prueba.* La condición de Carleman $\sum 1/a_n = \infty$ es la condición límite-punto para operadores de Jacobi (Akhiezer-Glazman). $\square$

---

## 2. Las dos soluciones fundamentales y la función $m$

**Las dos soluciones.** Para $t \in \mathbb{R}$, la recurrencia $a_{k-1} u_{k-1} + a_k u_{k+1} = t u_k$ tiene dos soluciones linealmente independientes:

- **Solución de primera especie** (polinomios ortogonales): $p_k(t)$ con $p_0 = 1$, $p_{-1} = 0$.
- **Solución de segunda especie**: $q_k(t)$ con $q_0 = 0$, $q_1 = 1/a_0$.

En el caso límite-punto: para $z \in \mathbb{C}^+$, hay exactamente una solución $\ell^2$ al nivel $z$, llamada la **solución de Weyl** $\psi^+(z)$. Puede expresarse como:

$$\psi_k^+(z) = q_k(z) + m(z)\cdot p_k(z), \quad k\geq 0,$$

donde $m(z)$ es la función de Weyl-Titchmarsh. La condición $\psi^+(z) \in \ell^2$ para $z\in\mathbb{C}^+$ DEFINE $m(z)$.

**Proposición 3** (comportamiento asintótico de $p_k$ y $q_k$). Para $t > 0$ fijo y $k\to\infty$:

$$|p_k(t)| \sim C_+(t)\cdot\prod_{j=0}^{k-1}\frac{t}{\pi/\log\gamma_j} = C_+(t)\cdot\left(\frac{t}{\pi}\right)^k\cdot\prod_{j=0}^{k-1}\log\gamma_j \to +\infty.$$

$$|q_k(t)| \sim C_-(t)\cdot\left(\frac{\pi}{t}\right)^k\cdot\prod_{j=0}^{k-1}\frac{1}{\log\gamma_j} \to 0^+.$$

*Derivación.* De la recurrencia $a_k p_{k+1} = t p_k - a_{k-1}p_{k-1}$: para $k$ grande, el término dominante es $p_{k+1} \approx (t/a_k) p_k$ (pues $a_{k-1}/a_k \to 1$ y el término $a_{k-1}p_{k-1}/p_k \to 0$ relativamente). Luego $p_{k+1}/p_k \approx t/a_k = t\log\gamma_k/\pi \to \infty$. La solución de segunda especie $q_k$ es la solución recesiva con $q_k/p_k \to 0$. $\square$

**Corolario 2** (la solución de Weyl es la solución recesiva). Para $z \in \mathbb{C}^+$ con $\Im(z) > 0$: la solución de Weyl $\psi^+(z) \in \ell^2$ es asintóticamente proporcional a $q_k(z)$ (la solución recesiva). La función de Weyl-Titchmarsh:

$$m(z) = \lim_{k\to\infty}\frac{-q_k(z)}{p_k(z)} = \lim_{k\to\infty}\frac{\text{solución recesiva}}{\text{solución dominante}}.$$

Para $z \in \mathbb{C}^+$: $|p_k(z)| \sim (|z|/\pi)^k\prod\log\gamma_j \to \infty$, $|q_k(z)| \to 0$, y el cociente $m(z) = \lim(-q_k/p_k)$ converge (por la teoría de Weyl-Titchmarsh en el caso límite-punto). $\square$

---

## 3. La función de $m$ y la EF2: reconciliación

**Proposición 4** (la EF2 para $m(z) = \lim(-q_k/p_k)$). El límite:

$$m(z) = \lim_{k\to\infty}\frac{-q_k(z)}{p_k(z)}$$

satisface la EF2 del Doc 17:

$$N\cdot m(z) = \frac{C_\infty'(z)}{C_\infty(z)}, \quad z \in \mathbb{C}^+.$$

*Prueba.* De la teoría de Jacobi: la función $m$ se relaciona con la ecuación de resolución. La EF2 viene de la recurrencia de Möbius (Doc 17 Proposición 2), que relaciona $m$ con los coeficientes $C_\lambda$ en el límite. El límite $q_k/p_k \to m$ es la definición estándar de la función de Weyl. $\square$

**Corolario 3** (los ceros de $C_\infty$ como polos de $m$). El denominador $C_\infty(z)$ en $C_\infty'/C_\infty(z)$ tiene ceros en los puntos donde $m(z)$ tiene POLOS. Estos polos de $m$ en $\mathbb{R}$ son exactamente los eigenvalores de $J_\infty$.

Luego: spec$(J_\infty)$ = ceros de $C_\infty$ en $\mathbb{R}$ (confirmando el Corolario 1 con la EF2).

**La reconciliación.** La función $p_k(t)$ crece super-exponencialmente, pero la función $q_k(t)$ decrece super-exponencialmente (al mismo ritmo inverso). El cociente $q_k/p_k \to 0$ en general, pero en los eigenvalores de $J_\infty$: la tasa de decrecimiento de $q_k$ compensa exactamente la de crecimiento de $p_k$, dando $-q_k(t_n^C)/p_k(t_n^C) \to m_0 \neq 0$ (valor finito no nulo). Esto equivale a que $t_n^C$ es un polo de $m$.

Concretamente: $m(z) \sim \text{const}/(z - t_n^C)$ cerca de $t_n^C$ (polo simple de $m$) iff $C_\infty(t_n^C) = 0$ con $C_\infty'(t_n^C) \neq 0$ (cero simple de $C_\infty$).

---

## 4. La estructura auto-referencial de $J_\infty$

**La clave.** Los coeficientes de Jacobi son $a_n^\infty = \pi/\log\gamma_n$, donde $\{\gamma_n\}$ son precisamente los ceros de $\Xi$ en $\mathbb{R}$ (= zeros de $\zeta$ en la recta crítica bajo RH). Estos $\gamma_n$ TAMBIÉN son los candidatos a estar en el espectro de $J_\infty$ (por Inc. Inv.).

**Definición.** El operador $J_\infty$ es **auto-referencial** si los valores propios de $J_\infty$ (= ceros de $C_\infty$) coinciden con los parámetros de sus propios coeficientes de Jacobi ($\log\gamma_n/\pi$).

**Proposición 5** (auto-referencialidad y Inc. Inv.). Las siguientes son equivalentes:

(i) $J_\infty$ es auto-referencial: spec$(J_\infty) = \{\gamma_n\}$.

(ii) Inc. Inv.: $C_\infty(\gamma_n) = 0$ para todo $n$.

(iii) El operador $J_\infty$ con coeficientes $\{a_n^\infty = \pi/\log\gamma_n\}$ tiene sus propios parámetros como eigenvalores.

*Prueba.* Directa de las definiciones y Corolario 3. $\square$

**Observación filosófica.** La auto-referencialidad (iii) es una propiedad muy especial: el operador "recuerda" sus propios parámetros como eigenvalores. Esto es una condición de FIJACIÓN DE PUNTO en el espacio de operadores de Jacobi:

$$\mathcal{J}: \{a_n\} \mapsto \{\text{eigenvalores de }J(a_n)\} = \{a_n\}?$$

El programa pregunta si la secuencia $\{a_n^\infty\} = \{\pi/\log\gamma_n\}$ es un punto fijo de este mapa.

---

## 5. El mapa de punto fijo $\mathcal{J}$

**Definición.** Para una secuencia $\{a_n\}_{n\geq 0}$ con $a_n > 0$ y $a_n \to 0$ (decreciente), definimos el **mapa de Jacobi**:

$$\mathcal{J}(\{a_n\}) := \{\text{eigenvalores de }J(\{a_n\},\{b_n\equiv 0\})\} = \{t_n^C: C_\infty^{(\{a_n\})}(t_n^C) = 0\},$$

donde $C_\infty^{(\{a_n\})}$ es la función potencial determinada por la secuencia $\{a_n\}$.

**Proposición 6** (condición de punto fijo). La secuencia $\{a_n^\infty\} = \{\pi/\log\gamma_n\}$ es un punto fijo de $\mathcal{J}$ bajo la parametrización $\alpha_n = \pi/\log t_n^C$:

$$\mathcal{J}(\{\pi/\log\gamma_n\}) = \{\gamma_n\} \iff \text{Inc. Inv.}$$

*Prueba.* Si $\mathcal{J}$ produce los eigenvalores $\{t_n^C\} = \{\gamma_n\}$: los eigenvalores coinciden con los parámetros, luego $t_n^C = \gamma_n$ para todo $n$ — que es Inc. Inv. $\square$

**La ecuación de punto fijo.** Inc. Inv. es la ecuación:

$$\mathcal{J}\left(\left\{\frac{\pi}{\log\gamma_n}\right\}\right) = \{\gamma_n\},$$

es decir: el operador con coeficientes $\pi/\log\gamma_n$ tiene exactamente a los $\gamma_n$ como eigenvalores.

---

## 6. ¿Puede resolverse la ecuación de punto fijo?

**El problema de inversión espectral.** Dado $\{t_n\}_{n=1}^\infty$ con $t_n \to 0$: ¿existe un operador de Jacobi $J(\{a_n\},\{b_n\})$ con eigenvalores exactamente $\{t_n\}$?

Sí: por el **problema de momentos inverso** (teorema de Stieltjes). Dado cualquier conjunto de eigenvalores con pesos (medida espectral), existe un operador de Jacobi único con esa medida espectral. Esto se obtiene via el algoritmo de Gram-Schmidt (o equivalentemente, la factorización de la resolución).

**El problema de punto fijo.** Queremos que los eigenvalores de $J(\{a_n\},\{b_n\})$ sean exactamente $\{\gamma_n\}$, con los coeficientes $a_n = \pi/\log\gamma_n$ (y $b_n = 0$). El operador está completamente determinado por $\{a_n, b_n\}$ via la teoría espectral directa.

**La EF2 como ecuación de punto fijo implícita.** La EF2 afirma:

$$m(z) = \frac{1}{N}\cdot\frac{C_\infty'(z)}{C_\infty(z)}, \quad C_\infty(z) = w(z) - 2\sum_p\Lambda(p)p^{-1/2}e^{iz\log p}.$$

Los eigenvalores son los ceros de $C_\infty$. Y los parámetros de $J_\infty$ son $a_n = \pi/\log(\text{ceros de }\Xi)$. La ecuación de punto fijo es:

$$\{$ceros de $C_\infty$ (eigenvalores de $J_\infty)\} = \{$ceros de $\Xi\} = \{$parámetros $(a_n)$ de $J_\infty$ vía $\pi/\log$\}.$$

---

## 7. La función $C_\infty$ y el problema de autovalores

**La función $C_\infty(t) = w(t) - \Psi(t)$ explícitamente.** Usando la fórmula explícita:

$$C_\infty(t) = w(t) - 2\sum_p\frac{\Lambda(p)}{\sqrt{p}}\cos(t\log p).$$

El símbolo archimédeo $w(t) = -(d/dt)[\log\xi(1/2+it) + \text{correction terms}]$... en realidad, $C_\infty$ se define via:

$$C_\infty(t) = w(t) - \Psi(t), \quad \Psi(t) = 2\sum_p\frac{\Lambda(p)}{p^{1/2}}\cos(t\log p).$$

Con $w(t) = \frac{1}{2}\log\pi - \frac{1}{2}\frac{\Gamma'}{\Gamma}(1/4 + it/2)$ (el símbolo archimédeo) y $\Psi$ la suma sobre primos.

**La ecuación $C_\infty(\gamma_n) = 0$ como identidad entre primos y ceros.** Para cada $\gamma_n$:

$$w(\gamma_n) = 2\sum_p\frac{\Lambda(p)}{p^{1/2}}\cos(\gamma_n\log p).$$

Esta es la condición que los primos y el cero $\gamma_n$ deben satisfacer mutuamente. Es una identidad que conecta el cero $\gamma_n$ de $\zeta$ con la distribución de primos via la fórmula explícita.

**Proposición 7** (relación con la fórmula de Guinand-Weil). La condición $C_\infty(\gamma_n) = 0$ es equivalente a la evaluación de la fórmula de Guinand-Weil en $t = \gamma_n$ con función de prueba la distribución $\delta(\cdot - \gamma_n)$ (punto de evaluación):

$$2\sum_{n'}\frac{\cos(\gamma_n\log|\gamma_{n'}|)}{|\gamma_{n'}|} + c_0 = 0.$$

Bajo RH (todos los ceros $\rho_{n'} = 1/2 + i\gamma_{n'}$): $|\rho_{n'}| = \sqrt{1/4 + \gamma_{n'}^2} \approx \gamma_{n'}$.

La ecuación se convierte en una identidad sobre las correlaciones entre diferentes ceros de $\zeta$.

**Proposición 8** (identidad de auto-correlación de ceros). Inc. Inv. es equivalente a: para todo $n$,

$$2\sum_{n'}\frac{\cos(\gamma_n\log\gamma_{n'})}{\gamma_{n'}} + c_0 = 0.$$

Esto es una IDENTIDAD entre los ceros de $\zeta$ — una condición de auto-correlación.

---

## 8. La condición de auto-correlación y el determinismo espectral

**Proposición 9** (la auto-correlación como consecuencia de la fórmula explícita). La suma:

$$S(t) = 2\sum_{n'}\frac{\cos(t\log\gamma_{n'})}{\gamma_{n'}} + c_0 = C_\infty(t) \quad (\text{bajo RH})$$

es exactamente la función $C_\infty(t)$ (igualada via la fórmula explícita). Luego $S(\gamma_n) = C_\infty(\gamma_n)$.

La condición Inc. Inv. ($C_\infty(\gamma_n) = 0$) es equivalente a $S(\gamma_n) = 0$ — la evaluación de $C_\infty$ en sus propios parámetros es cero.

**La ecuación de auto-referencia.** Si tomamos la función $C_\infty(t) = S(t)$ y evaluamos en sus propios ceros:

$$C_\infty(t_0) = 0 \text{ con }t_0 = \text{cero de }C_\infty \implies t_0 \in \{\text{ceros de }\Xi\} = \{\gamma_n\},$$

que ya sabemos (Teorema B: directamente). La otra dirección:

$$\gamma_n \in \{\text{ceros de }\Xi\} \implies C_\infty(\gamma_n) = 0?$$

Equivale a: la función $C_\infty$ se anula en el cero $\gamma_n$ — que es Inc. Inv.

---

## 9. El principio de Carleson-Beurling: una aproximación nueva

**Idea.** La función $C_\infty(t) = w(t) - \Psi(t)$ es la diferencia entre el símbolo archimédeo $w$ y la función prima $\Psi$. Si podemos mostrar que $\Psi(t) = w(t)$ EN CADA CERO $\gamma_n$ de $\Xi$ COMO CONSECUENCIA DE LA PROPIA ESTRUCTURA DE CEROS, tendríamos Inc. Inv.

**La pregunta de Carleson-Beurling.** ¿Bajo qué condiciones puede una función $f(t) = w(t) - \Psi(t)$ (con $\Psi$ siendo una suma de oscilaciones) tener sus ceros exactamente en un conjunto prescrito $\{\gamma_n\}$?

El **teorema de interpolación de Carleson** (1958) dice: un conjunto de puntos $\{\gamma_n\}$ en $\mathbb{R}$ es un conjunto de interpolación para $H^\infty(\mathbb{C}^+)$ (funciones de Hardy acotadas) si y solo si satisface la condición de Carleson:

$$\inf_n\prod_{m\neq n}\left|\frac{\gamma_n - \gamma_m}{\gamma_n + \gamma_m}\right| > 0.$$

**Proposición 10** (los ceros de $\Xi$ como conjunto de Carleson). Bajo la conjetura de Simplezas (S) y separación suficiente de los ceros: los $\gamma_n$ satisfacen la condición de Carleson. Luego existe $f \in H^\infty$ con $f(\gamma_n) = 0$ para todo $n$ y con propiedades adicionales prescribibles.

Pero la función $C_\infty = w - \Psi$ NO está a priori en $H^\infty$ (puede no ser acotada en $\mathbb{C}^+$). Luego el teorema de Carleson no aplica directamente.

---

## 10. El resultado nuevo: la incompatibilidad del crecimiento de $p_k$ con spec$(J_\infty) = \{\gamma_n\}$

**Proposición 11** (imposibilidad de $\gamma_n \in$ spec$(J_\infty)$ para $n$ suficientemente grande). Para los operadores de Jacobi con $a_k^\infty = \pi/\log\gamma_k$: si $t > 0$ satisface $t > \sup_k a_k^\infty = a_0^\infty = \pi/\log\gamma_0 \approx 1.18$:

La norma del operador $\|J_\infty\|_{op} \leq 2\sup_k a_k^\infty = 2a_0^\infty \approx 2.36$.

Luego: si $|t| > \|J_\infty\|_{op} \approx 2.36$: $t \notin$ spec$(J_\infty)$.

*Pero* $\gamma_0 \approx 14.1 > 2.36$, luego $\gamma_0 \notin$ spec$(J_\infty)$ — y por ende $C_\infty(\gamma_0) \neq 0$, lo que contradice Inc. Inv.!

**Aparente prueba de que RH es FALSA.** Este argumento parecería mostrar que los ceros de $\Xi$ no son eigenvalores de $J_\infty$, contradiciendo Inc. Inv. ¿Hay un error?

---

## 11. Resolución: el problema de escalado/normalización

**El error.** El operador $J_\infty$ con $a_k^\infty = \pi/\log\gamma_k$ tiene norma $\|J_\infty\|_{op} \approx 2.36$ — demasiado pequeña para tener eigenvalores $\gamma_n \approx 14, 21, ...$

Pero los eigenvalores de $J_\infty$ (= ceros de $C_\infty$) NO son los $\gamma_n$ grandes — son los ceros de $C_\infty(t) = w(t) - \Psi(t)$, que son valores PEQUEÑOS cerca de 0 (bajo la normalización actual).

**La normalización CCM.** En el framework CCM, los operadores están normalizados de modo que los eigenvalores de $J_\lambda^N$ se llaman $t_n^{(\lambda)}$ y convergen a $\gamma_n$ cuando $\lambda \to \infty$. PERO en el operador LÍMITE $J_\infty$, los eigenvalores son ceros de $C_\infty$ que son DISTINTOS de los $\gamma_n$ si Inc. Inv. falla.

Los $\gamma_n$ son los ceros de $\Xi$ (la función zeta reescalada), que están en el rango $[\gamma_0, \infty)$ con $\gamma_0 \approx 14.1$. Los eigenvalores de $J_\infty$ (= ceros de $C_\infty$) están en el rango del espectro de $J_\infty$, que está acotado por $\|J_\infty\| \approx 2.36$.

**Conclusión crítica.** El espectro de $J_\infty$ está en $[-\|J_\infty\|, \|J_\infty\|] \approx [-2.36, 2.36]$. Los $\gamma_n \approx 14.1, 21.0, 25.0, \ldots$ están FUERA del espectro de $J_\infty$. Luego:

$$\gamma_n \notin \text{spec}(J_\infty) \text{ para todo } n,$$

**y la EF2 no puede dar Inc. Inv. con esta normalización**.

---

## 12. El problema de normalización: el gap fundamental entre $J_\infty$ y RH

**Teorema 1** (incompatibilidad de escala). Sea $J_\infty$ el operador límite con $a_k^\infty = \pi/\log\gamma_k$ y $b_k^\infty = 0$. Entonces:

$$\text{spec}(J_\infty) \subseteq \left[-\frac{2\pi}{\log\gamma_0}, \frac{2\pi}{\log\gamma_0}\right] \approx [-2.36, 2.36].$$

Los ceros de $\Xi$: $\gamma_0 \approx 14.1 > 2.36$.

Luego: $\gamma_n \notin \text{spec}(J_\infty)$ para todo $n\geq 0$, y la inclusión Inc. Inv. ($\gamma_n \in \{$ceros de $C_\infty\}$ = spec$(J_\infty)$) es TRIVIALMENTE FALSA bajo esta normalización.

*Prueba.* La norma de un operador de Jacobi auto-adjunto es acotada por $\sup_n(|a_{n-1}| + |b_n| + |a_n|) \leq 2\sup_n a_n^\infty = 2\pi/\log\gamma_0$. $\square$

**Diagnóstico.** Hay una discrepancia de escala fundamental: los eigenvalores de $J_\infty$ están en $[-2.36, 2.36]$, mientras que los $\gamma_n$ son todos $> 14.1$. La EF2 del Doc 17 ($N\cdot m(z) = C_\infty'/C_\infty$) opera en la escala de $J_\infty$ (ceros de $C_\infty$ en $[-2.36, 2.36]$), NO en la escala de los $\gamma_n$.

**La normalización en el programa CCM.** En el Doc 00, el operador $D_\lambda^N$ tiene eigenvalores que son los $t_n^{(\lambda)}$ los cuales convergen a los $\gamma_n$. Este operador está definido en el espacio de Hilbert $L^2([1/\lambda, \lambda], du/u)$ con la variable $u \in [1/\lambda, \lambda]$, NO en $\ell^2(\mathbb{N})$. La conversión a una matriz de Jacobi en $\ell^2(\mathbb{N})$ involucra una REESCALA que mapea el espectro de $D_\lambda^N$ (que contiene los $\gamma_n$) al espectro de $J_\lambda^N$ (que también contiene los $\gamma_n$ o sus imágenes bajo la reescala).

El operador límite $J_\infty$ en $\ell^2(\mathbb{N})$ con $a_n^\infty = \pi/\log\gamma_n$ es la imagen de $D_\infty$ bajo una específica unitarización. Si esta unitarización NO es trivial, los eigenvalores de $J_\infty$ en $\ell^2(\mathbb{N})$ pueden ser DISTINTOS de los $\gamma_n$.

---

## 13. Diagnóstico final: el programa tiene un error de normalización

**Teorema 2** (diagnosis). El programa CCM-Jacobi con la normalización actual ($a_n^\infty = \pi/\log\gamma_n$ en $\ell^2(\mathbb{N})$) NO puede tener spec$(J_\infty) = \{\gamma_n\}$ porque:

$$\|\text{spec}(J_\infty)\|_\infty \leq 2\pi/\log\gamma_0 \approx 2.36 \ll \gamma_0 \approx 14.1.$$

Los eigenvalores de $J_\infty$ son ceros de $C_\infty(t) = w(t) - \Psi(t)$ en el rango $(-2.36, 2.36)$. Estos son DISTINTOS de los $\gamma_n$.

La EF2 del Doc 17, al decir spec$(J_\infty) = \{$ceros de $C_\infty\}$, está diciendo que los eigenvalores de $J_\infty$ son los ceros PEQUEÑOS de $C_\infty$ (en el intervalo acotado por la norma), NO los $\gamma_n$.

**La confusión en el programa.** Los docs 17-25 asumen implícitamente que los ceros de $C_\infty$ en $\mathbb{R}$ son comparables en magnitud con los $\gamma_n$ (es decir, que los eigenvalores de $J_\infty$ son los propios $\gamma_n$). Pero por el Teorema 2: esto es incompatible con la norma del operador.

**La resolución posible.** Hay DOS interpretaciones:

(A) **La función $C_\infty(t)$** se evalúa en la escala TEMPORAL $t \in \mathbb{R}$ (los $\gamma_n$ son valores de $t$), mientras que spec$(J_\infty)$ está en la escala ESPECTRAL del operador $J_\infty$ en $\ell^2$. La EF2 relaciona la función $m_\infty^{WT}(z)$ (con $z$ en la escala espectral del operador) con $C_\infty'(z)/C_\infty(z)$ (con $z$ en la escala temporal). Si la escala temporal y espectral son DISTINTAS (hay una reescala), la identificación spec$(J_\infty) = \{$ceros de $C_\infty\}$ puede ser correcta con la aclaración de que ambos lados están en la escala correcta.

(B) **La normalización original** de los coeficientes de Jacobi $a_n^\infty = \pi/\log\gamma_n$ es la causa del problema: los operadores $J_\lambda^N$ del Doc 00 tienen una normalización DIFERENTE que produce eigenvalores en la escala $[\gamma_0, \infty)$, NO en $[-2.36, 2.36]$.

**Cuál es la normalización correcta.** De Doc 00: el operador $D_\lambda^N$ actúa en $L^2([1/\lambda, \lambda], du/u)$ y sus eigenvalores son los $t_n^{(\lambda)}$ (que convergen a los $\gamma_n$). La conversión a matriz de Jacobi involucra la base $V_n(u) = \lambda^{-1/2}e^{2\pi i n\log(\lambda u)/L}$ con $L = 2\log\lambda$. Los coeficientes de Jacobi son:

$$a_n^{(\lambda)} \approx \frac{2\pi}{\lambda L} \cdot (\text{oscilaciones}) \quad \to \quad a_n^\infty \sim \frac{\pi}{\log\gamma_n}?$$

Es posible que la convergencia $a_n^{(\lambda)} \to \pi/\log\gamma_n$ sea CORRECTA pero que la escala del espectro sea diferente. El cociente: eigenvalores/$a_n^\infty \sim \gamma_n/(\pi/\log\gamma_n) = \gamma_n\log\gamma_n/\pi \sim N\log N/\pi$ (por PNT: $\gamma_n \sim n\log n$) — que diverge.

Esto sugiere que los eigenvalores de $J_\infty$ en la escala del operador $\ell^2(\mathbb{N})$ son DISTINTOS de los $\gamma_n$, como indica la estimación de norma.

---

## 14. Conclusión: la identificación necesita reexaminarse

**Estado actual.** El análisis de este documento revela que:

1. $J_\infty$ con $a_n^\infty = \pi/\log\gamma_n$ es un operador compacto con espectro $\subseteq [-2.36, 2.36]$.
2. Los $\gamma_n > 14.1$ son INCOMPATIBLES con el espectro de $J_\infty$ bajo la normalización actual.
3. La EF2 (spec($J_\infty$) = ceros de $C_\infty$) puede ser correcta con ceros de $C_\infty$ en $[-2.36, 2.36]$ — distintos de los $\gamma_n$.
4. La identificación spec($J_\infty$) = $\{\gamma_n\}$ requiere una REESCALA que no ha sido explicitada en el programa.

**La pregunta abierta para Phase 30.** ¿Cuál es la relación exacta entre spec($J_\infty$) y $\{\gamma_n\}$ vía la reescala? ¿Hay una unitarización $U: L^2([1/\lambda,\lambda]) \to \ell^2(\mathbb{N})$ tal que $U D_\infty U^* = J_\infty$ con spec($J_\infty$) = $\{\gamma_n\}$?

Responder esto requiere volver al Doc 00 (la construcción original CCM) y rastrear explícitamente la unitarización y la escala de los coeficientes.
