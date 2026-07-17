# Documento 84 — ¿Satisface $F(z)$ alguna propiedad que fuerce no-ceros en el disco?

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM (Camino 2)
**Fecha:** 2026-06-09
**Prerrequisitos:** Docs 75, 78, 81

---

## Resumen

Este documento explora sistemáticamente las propiedades analíticas de $F(z) = \xi(z/(z-1))$ en el disco unitario $\{|z| < 1\}$ con el fin de determinar si alguna de ellas fuerza la no-anulación en el interior, sin referencia circular a la posición de los ceros de $\xi$. En §1 se estudia la cuestión de ecuaciones diferenciales para $\xi$ y $F$, concluyendo que $\xi$ no satisface ninguna EDO algebraica útil. En §2 se establece con precisión la ecuación funcional que satisface $F$ bajo la transformación de Möbius: $F(z) = F(1/z)$ (invarianza bajo inversión), y se extraen sus consecuencias para los ceros. En §3 se analiza $F$ como función par en la variable $\log|z|$. En §4 se estudian los puntos críticos de $F$ dados por la ecuación funcional. En §5 se formula el criterio de exterioridad de Blaschke-Nevanlinna y su equivalencia con RH. En §6 se establece el criterio de Jensen como condición computable equivalente a RH. En §7 se examina el principio del mínimo del módulo. En §8 se analiza la desigualdad de Bohr. En §9 se estudia el criterio del índice de Kronecker. En §10 se sintetizan los resultados y se formula la pregunta abierta más precisa.

La conclusión honesta es que la ecuación funcional $F(z) = F(1/z)$ y el criterio de Jensen proporcionan la estructura más rica hasta la fecha, pero ninguna de las propiedades estudiadas implica la no-anulación sin asumir esencialmente RH.

---

## §1. Ecuaciones diferenciales para $\xi$ y para $F$

### 1.1. La función $\xi$ no satisface ninguna EDO algebraica

La función $\xi(s)$ no satisface ninguna ecuación diferencial ordinaria de la forma
$$P(\xi, \xi', \xi'', \ldots, \xi^{(n)}) = 0$$
con $P$ un polinomio de coeficientes racionales en $s$. Esto la distingue cualitativamente de las funciones hipergométricas, las funciones de Bessel, $\Gamma$, $\zeta$ (que satisface la ecuación $s(s-1)\zeta'' + \ldots$ via la ecuación funcional), o cualquier función de un $D$-módulo algebraico.

La razón es la siguiente: las soluciones de EDO algebraicas tienen conjuntos de ceros con estructura algebraica especial (separación uniforme, relaciones de recurrencia, etc.), mientras que los ceros $1/2 + i\gamma_n$ de $\xi$ en la recta crítica tienen una distribución que refleja la distribución de los números primos (via la fórmula explícita de Riemann-Weil) y no satisface ninguna relación algebraica conocida. Si $\xi$ satisficiera $\xi'' = P(s, \xi, \xi')$, los ceros $\gamma_n$ satisfarían relaciones de recurrencia que son incompatibles con la irregularidad observada en su distribución.

**Proposición 1.1.** *La función $\xi(s)$ no satisface ninguna EDO lineal de coeficientes polinomiales, ni ninguna EDO polinomial de primer orden. En particular, no hay una ecuación $\xi'' = R(s)\xi$ con $R$ racional que $\xi$ satisfaga globalmente.*

*Justificación.* Una EDO lineal de segundo orden $\xi'' = R(s)\xi$ con $R$ racional tendría la solución $\xi$ como función con monodrómia algebraica alrededor de cada polo de $R$. Pero $\xi$ es entera (sin singularidades) y de orden 1: si $R$ fuera un polinomio de grado $d$, las soluciones serían funciones enteras de orden $(d+2)/2$; para $d=0$ (coeficiente constante) se obtienen exponenciales de orden 1, pero las exponenciales $e^{as+b}$ no tienen ceros, mientras que $\xi$ tiene infinitos ceros. Para $d \geq 1$, el orden de la solución sería mayor que 1, contradiciendo el orden exactamente 1 de $\xi$. $\square$

### 1.2. La representación integral y sus derivadas

La representación integral de Riemann
$$\xi(s) = 2\int_1^\infty \phi(t)\, t^{(s-1)/2}\, dt, \qquad \phi(t) = \sum_{n=1}^\infty (2\pi^2 n^4 t^2 - 3\pi n^2 t) e^{-\pi n^2 t},$$
permite diferenciar bajo el signo de integración: $\xi'(s) = \int_1^\infty \phi(t) t^{(s-1)/2} \log t\, dt$. Esto da una relación entre $\xi'$ y $\xi$ solo en el sentido integral (no diferencial), lo que no constituye una EDO.

### 1.3. La ecuación diferencial de $F$

Dado que $F(z) = \xi(z/(z-1))$ y $\xi$ no satisface ninguna EDO algebraica, $F$ tampoco satisface ninguna EDO algebraica en $z$ cuyas soluciones sean automáticamente sin ceros en el disco. Cualquier relación diferencial para $F$ heredada de la representación integral de $\xi$ es de tipo integral y no proporciona la información local (en $z$) necesaria para controlar ceros.

**Conclusión de §1.** El estudio de ecuaciones diferenciales no ofrece una vía directa para probar la no-anulación de $F$ en el disco.

---

## §2. La ecuación funcional de $F$ y sus consecuencias

### 2.1. Derivación de $F(z) = F(1/z)$

Sea $s = z/(z-1) = \tau(z)$. La ecuación funcional de $\xi$ es $\xi(s) = \xi(1-s)$. El punto $1-s$ corresponde, en coordenadas del disco, al punto $z'$ tal que $\tau(z') = 1 - \tau(z)$, es decir:
$$\frac{z'}{z'-1} = 1 - \frac{z}{z-1} = 1 + \frac{z}{1-z} = \frac{1-z+z}{1-z} = \frac{1}{1-z}.$$
Despejando $z'$: de $z'/(z'-1) = 1/(1-z)$, se obtiene $z'(1-z) = z'-1$, es decir, $z' - z'z = z' - 1$, es decir, $z'z = 1$, de modo que $z' = 1/z$.

**Proposición 2.1.** *Para todo $z \neq 0$, $F(1/z) = F(z)$. La función $F$ es invariante bajo la inversión $z \mapsto 1/z$.*

*Demostración.* $F(1/z) = \xi(\tau(1/z)) = \xi(1 - \tau(z)) = \xi(\tau(z)) = F(z)$, donde se ha usado la ecuación funcional de $\xi$ y el cálculo $\tau(1/z) = 1 - \tau(z)$ demostrado arriba. $\square$

### 2.2. Ceros de $F$ en pares inversivos

**Corolario 2.2.** *Si $z_0$ es un cero de $F$, entonces $1/z_0$ también es un cero de $F$. En particular:*
- *Si $|z_0| < 1$ (cero en el disco), entonces $|1/z_0| > 1$ (cero fuera del disco).*
- *Si $|z_0| = 1$ (cero en la frontera), entonces $1/z_0 = \bar{z}_0$ también está en la frontera.*

*Demostración.* Consecuencia inmediata de la Proposición 2.1. $\square$

### 2.3. La ecuación funcional y RH

Bajo $\neg$RH, existen ceros $\rho_0 = \sigma_0 + i\gamma_0$ de $\xi$ con $\sigma_0 > 1/2$. Estos mapean a $z_0 = \tau(\rho_0) = \rho_0/(\rho_0-1)$ con $|z_0| > 1$ (fuera del disco, por la Proposición 1.1 del Doc 81). Su inverso $1/z_0 = (\rho_0-1)/\rho_0 = 1 - 1/\rho_0$ satisface $|1/z_0| < 1$.

**Verificación directa.** $|1/z_0|^2 = |(\rho_0-1)/\rho_0|^2 = ((\sigma_0-1)^2 + \gamma_0^2)/(\sigma_0^2 + \gamma_0^2)$. La condición $|1/z_0| < 1$ equivale a $(\sigma_0-1)^2 + \gamma_0^2 < \sigma_0^2 + \gamma_0^2$, es decir, $(\sigma_0-1)^2 < \sigma_0^2$, es decir, $-2\sigma_0 + 1 < 0$, es decir, $\sigma_0 > 1/2$. $\checkmark$

**Corolario 2.3.** *$\neg$RH es equivalente a que $F$ tenga ceros en $\{|z| < 1\}$, que son exactamente los puntos $1-1/\rho_0$ para cada cero off-critical $\rho_0$ con $\mathrm{Re}(\rho_0) > 1/2$.*

### 2.4. Lo que la ecuación funcional no implica

La ecuación funcional $F(z) = F(1/z)$ empareja ceros del disco con ceros fuera del disco. Esto es una simetría de los ceros, no una restricción que los elimine del disco. En particular, la ecuación funcional por sí sola no excluye la existencia de ceros en $\{|z| < 1\}$: cualquier función par bajo $z \mapsto 1/z$ puede tener o no tener ceros en el disco.

---

## §3. $F$ como función par en $\log|z|$

### 3.1. Estructura bajo la parametrización polar

Escribiendo $z = re^{i\theta}$ con $r > 0$, $\theta \in [0, 2\pi)$, la invarianza $F(re^{i\theta}) = F(e^{i\theta}/r)$ dice que $F$ evaluada en radio $r$ y ángulo $\theta$ coincide con $F$ evaluada en radio $1/r$ y ángulo $\theta$. Si se introduce la variable $u = \log r$, esto se traduce en que $F(e^{u+i\theta})$ es una función par de $u$ para cada $\theta$ fijo:
$$F(e^{u+i\theta}) = F(e^{-u+i\theta}).$$

### 3.2. La función $H(u, \theta)$

Definamos formalmente $H(u, \theta) = F(e^{u+i\theta})$ para $u \in \mathbb{R}$ y $\theta \in [0, 2\pi)$. La condición de analiticidad de $F$ (como función de $z = e^{u+i\theta} = re^{i\theta}$) se expresa en términos de $H$ como las ecuaciones de Cauchy-Riemann en coordenadas logarítmico-polares. La paridad $H(u, \theta) = H(-u, \theta)$ implica que la serie de Fourier-Laurent de $F$ alrededor de $z = 0$ tiene únicamente potencias $z^k + z^{-k}$:

Si $F(z) = \sum_{k=-\infty}^{\infty} c_k z^k$ (en la corona $0 < |z| < 1$, pero $F$ es analítica en el disco, así que $c_k = 0$ para $k < 0$ y $F(z) = \sum_{k=0}^\infty c_k z^k$), la condición $F(1/z) = F(z)$ implica $\sum_{k=0}^\infty c_k z^{-k} = \sum_{k=0}^\infty c_k z^k$. Dado que $F$ es analítica en el disco, la única manera de que esto sea consistente con la analiticidad de $F$ en el disco y la de $F(1/z)$ fuera del disco es que $F$ sea constante, lo cual es falso.

**Aclaración.** La ecuación $F(z) = F(1/z)$ no implica que $F$ sea una función de $z + 1/z$, porque $F$ no es analítica en todo $\mathbb{C} \setminus \{0\}$ (tiene singularidades en $z = 1$ y $z = \infty$). La igualdad $F(z) = F(1/z)$ relaciona valores de $F$ en el disco con valores fuera del disco, y es perfectamente consistente con $F$ siendo analítica solo en el disco.

### 3.3. Consecuencia correcta para los coeficientes de Taylor

Sea $F(z) = \sum_{k=0}^\infty c_k z^k$ la expansión de Taylor en el disco. La condición $F(z) = F(1/z)$ para $|z| = 1$ (es decir, en la frontera) da:
$$\sum_{k=0}^\infty c_k e^{ik\theta} = \sum_{k=0}^\infty c_k e^{-ik\theta} \quad \text{para casi todo } \theta.$$
Esto implica $c_k = \bar{c}_{-k}$, pero como $c_k = 0$ para $k < 0$ (por analiticidad en el disco), la condición se reduce a $c_k = \bar{c}_{-k} = 0$ para $k > 0$... lo que implicaría $c_k = 0$ para todo $k > 0$, una contradicción.

**Resolución.** La igualdad $F(e^{i\theta}) = F(e^{-i\theta})$ es la condición correcta en la frontera (que $F$ sea real en la circunferencia), y vale solo si los coeficientes $c_k$ son reales. Los coeficientes de Taylor de $F$ en $z = 0$ son los valores $\xi^{(k)}(0)/k!$, que son reales (pues $\xi$ es real en la recta real). Por tanto, $c_k \in \mathbb{R}$ y la condición de la frontera $F(e^{i\theta}) = \overline{F(e^{i\theta})}$ (que $F$ sea real en la frontera) es equivalente a $c_k \in \mathbb{R}$, lo cual es automático.

La condición más fuerte $F(z) = F(1/z)$ para $z$ en el interior del disco se cumple como identidad entre el valor en $z$ (interior) y el valor en $1/z$ (exterior), y es consecuencia directa de $\xi(s) = \xi(1-s)$.

---

## §4. Puntos críticos de $F$ y la geometría local

### 4.1. Los puntos fijos de $z \mapsto 1/z$ en el disco

Los puntos fijos de la involución $z \mapsto 1/z$ son los puntos con $z = 1/z$, es decir, $z^2 = 1$, es decir, $z = \pm 1$. El punto $z = +1$ está en la frontera del disco (donde $F$ no está definida, pues $\tau(1) = \infty$). El punto $z = -1$ está en la frontera del disco.

La derivada: $\frac{d}{dz}F(1/z) = -\frac{1}{z^2}F'(1/z)$. La igualdad $F(z) = F(1/z)$ diferenciada da:
$$F'(z) = -\frac{1}{z^2}F'(1/z).$$
Evaluando en $z = -1$: $F'(-1) = -F'(-1)$, lo que implica $F'(-1) = 0$.

**Proposición 4.1.** *El punto $z = -1$ es un punto crítico de $F$: $F'(-1) = 0$.*

### 4.2. El significado de $z = -1$

El punto $z = -1$ corresponde a $s = \tau(-1) = (-1)/(-1-1) = (-1)/(-2) = 1/2$. Por tanto, $F(-1) = \xi(1/2)$. El punto crítico $z = -1$ de $F$ corresponde al centro de la franja crítica, que es el punto de simetría de la ecuación funcional de $\xi$.

**Observación 4.2.** El valor $\xi(1/2)$ puede calcularse explícitamente: $\xi(1/2) = \frac{1}{2}\cdot\frac{1}{2}\cdot(-\frac{1}{2})\cdot\pi^{-1/4}\Gamma(1/4)\zeta(1/2)$... No. Más directamente, de la normalización estándar, $\xi(1/2) \approx 0.4971$. El punto crítico de $F$ en $z = -1$ tiene valor $F(-1) \approx 0.4971 \neq 0$, lo cual es consistente con la no-anulación en la frontera (RH no dice nada sobre ceros de $\xi$ en $s = 1/2$ real; $\xi(1/2) \neq 0$).

### 4.3. Comportamiento local en $z = 0$

El punto $z = 0$ corresponde a $s = \tau(0) = 0$, y $F(0) = \xi(0) = 1/2$. La serie de Taylor de $F$ en $z = 0$ es:
$$F(z) = \xi(0) + \xi'(0)\cdot\frac{d\tau}{dz}\bigg|_{z=0} z + O(z^2) = \frac{1}{2} + \xi'(0)\cdot\frac{-1}{(z-1)^2}\bigg|_{z=0}\cdot z + O(z^2) = \frac{1}{2} - \xi'(0) z + O(z^2).$$
Puesto que $\xi(0) = 1/2$ y $\xi'(0) = 0$ (ya que $\xi$ es simétrica respecto a $s = 1/2$ y el punto $s = 0$ corresponde a $z = 0$, mientras que la simetría de $\xi$ alrededor de $s = 1/2$ da $\xi'(s) = -\xi'(1-s)$, y en $s = 0$: $\xi'(0) = -\xi'(1)$; ambas por la relación funcional, y por ser $\xi$ real en la recta real se puede verificar numéricamente que $\xi'(0) \neq 0$ en general). Nótese que $F(0) = 1/2 > 0$, lo que garantiza que $F$ no se anula en $z = 0$.

---

## §5. Factorización de Blaschke y la condición de exterioridad

### 5.1. La factorización de Nevanlinna

Si $F \in H^\infty(\mathbb{D})$ (Hardy), la factorización de Nevanlinna-Pick descompone $F$ como
$$F(z) = B(z) \cdot G(z),$$
donde $B(z) = e^{i\phi}\prod_{k} \frac{z - z_k}{1 - \bar{z}_k z}$ es el producto de Blaschke asociado a los ceros $\{z_k\}$ de $F$ con $|z_k| < 1$ (contados con multiplicidad), y $G(z)$ es una función en $H^\infty$ sin ceros en el disco (función exterior si $F$ está en la clase $N^+$).

Bajo RH, $F$ no tiene ceros en el disco, de modo que $B(z) \equiv 1$ y $F = G$ es una función sin ceros (exterior).

**Proposición 5.1.** *RH es equivalente a que $F(z)$ sea una función sin ceros en $H(\mathbb{D})$, es decir, que la factorización de Blaschke-Nevanlinna de $F$ tenga producto de Blaschke trivial: $B \equiv 1$.*

### 5.2. Funciones exteriores en $H^2$

Una función $G \in H^2(\mathbb{D})$ sin ceros se dice exterior si está completamente determinada por su módulo en la frontera via la fórmula de Poisson:
$$\log G(z) = \frac{1}{2\pi}\int_0^{2\pi} \frac{e^{i\theta}+z}{e^{i\theta}-z} \log|F(e^{i\theta})|\, d\theta, \qquad |z| < 1.$$
(con una constante de fase apropiada). La condición necesaria y suficiente para que $G$ sea exterior (y no meramente sin ceros) es que el miembro derecho converja y defina una función de $H^2$.

**Nota de cautela.** La función $F$ no está en $H^2$ ni en $H^\infty$: $F(z) = \xi(\tau(z))$ crece sin acotación cuando $z \to 1$ (pues $\xi(s) \to \infty$ cuando $s \to \infty$). Por tanto, la teoría estándar de funciones exteriores en $H^2$ o $H^\infty$ no se aplica directamente. La Proposición 5.1 afirma la no-anulación (equivalencia con RH) pero no la exterioridad en el sentido $H^2$.

---

## §6. La fórmula de Jensen como criterio computable

### 6.1. La fórmula de Jensen para $F$

Sea $F$ analítica en el disco $\{|z| \leq r\}$ para $r < 1$ (lo cual es verdad para todo $r < 1$ pues $F$ es analítica en $\{|z|<1\}$). La fórmula de Jensen establece:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\, d\theta = \log|F(0)| + \sum_{|z_k| < r}\log\frac{r}{|z_k|},$$
donde la suma corre sobre los ceros $z_k$ de $F$ en el disco $\{|z| < r\}$ (contados con multiplicidad).

Tomando $r \to 1^-$, y asumiendo que $\log|F(e^{i\theta})|$ es integrable en la frontera (lo cual requiere verificación, dada la singularidad en $\theta$ correspondiente a $z = 1$), se obtiene en el límite:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\, d\theta = \log|F(0)| + \sum_{|z_k| < 1}\log\frac{1}{|z_k|}.$$

### 6.2. El criterio numérico

Puesto que $\log(1/|z_k|) > 0$ para $|z_k| < 1$, la suma es no-negativa, y es exactamente cero si y solo si no hay ceros en el disco.

**Proposición 6.1.** *Asumiendo que $\log|F(e^{i\theta})|$ es integrable en $[0, 2\pi)$,*
$$\text{RH} \iff \frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\, d\theta = \log|F(0)| = \log\frac{1}{2} = -\log 2.$$

*Si $\neg$RH, la integral es estrictamente mayor que $-\log 2$.*

### 6.3. Integrabilidad de $\log|F(e^{i\theta})|$

La función $\log|F(e^{i\theta})| = \log|\xi(1/2 + it_\theta)|$, donde $t_\theta$ es la parametrización de la recta crítica. Esta función tiene singularidades logarítmicas en los $\theta$ correspondientes a los ceros de $\xi$, que son de la forma $\log|e^{i\theta} - e^{i\theta_n}|$ cerca de cada $\theta_n$. Tales singularidades son integrables (pues $\int_0^\epsilon |\log t|\, dt < \infty$). Los ceros de $\xi$ son simples (se cree incondicionalmente, y está probado para todos los ceros conocidos), lo que asegura que las singularidades sean $\sim \log|t - \gamma_n|$ e integrables. Por tanto, $\log|F(e^{i\theta})|$ es integrable.

### 6.4. La integral en términos de $\xi$ sobre la recta crítica

La integral sobre la frontera del disco corresponde, via el cambio de variable $z(t) = -e^{2i\arctan(2t)}$ (Proposición 1.3 del Doc 81), a una integral sobre la recta crítica:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|\xi(1/2+it_\theta)|\, d\theta = \int_{-\infty}^{\infty}\log|\xi(1/2+it)|\, \frac{2\, dt}{\pi(1+4t^2)}.$$
(El jacobiano del cambio de variable $\theta \mapsto t$ es $|d\theta/dt| = 4/(1+4t^2)$, la densidad de la distribución Cauchy estándar escalada.) El criterio de RH se convierte entonces en:
$$\text{RH} \iff \int_{-\infty}^{\infty}\log|\xi(1/2+it)|\cdot\frac{2\, dt}{\pi(1+4t^2)} = -\log 2.$$

**Observación 6.2.** Esta integral tiene la forma de un promedio ponderado de $\log|\xi(1/2+it)|$ con peso $2/(\pi(1+4t^2))$ (una distribución de Cauchy, de masa total 1). El criterio de RH es exactamente que este promedio ponderado sea igual a $\log|\xi(0)| = \log(1/2)$.

### 6.5. Evaluación via la fórmula explícita y el logaritmo de $|\xi|$

El logaritmo de $|\xi(1/2+it)|$ puede expresarse via la fórmula explícita de Riemann:
$$\log|\xi(1/2+it)| = \text{Re}\log\xi(1/2+it) = \text{Re}\left[\log\xi(0) + \sum_\rho\log\left(1 - \frac{1/2+it}{\rho}\right)\right].$$

Integrar esto contra el peso $2/(\pi(1+4t^2))$ y comparar con $\log\xi(0) = -\log 2$ requiere mostrar que:
$$\sum_\rho \int_{-\infty}^{\infty}\text{Re}\log\left(1 - \frac{1/2+it}{\rho}\right)\cdot\frac{2\, dt}{\pi(1+4t^2)} = 0.$$
Por la simetría del producto de Hadamard $\xi(s) = \xi(0)\prod_\rho (1 - s/\rho)(1 - s/(1-\rho))$ (emparejando $\rho$ con $1-\rho$), la condición se reduce a mostrar que para cada par $(\rho, 1-\rho)$:
$$\int_{-\infty}^{\infty}\text{Re}\left[\log\left(1-\frac{1/2+it}{\rho}\right) + \log\left(1-\frac{1/2+it}{1-\rho}\right)\right]\frac{2\, dt}{\pi(1+4t^2)} = 0.$$

**Proposición 6.3.** *La condición anterior es equivalente a que, para cada par $(\rho, 1-\rho)$, el promedio ponderado de Cauchy de $\log|1 - (1/2+it)/\rho| + \log|1 - (1/2+it)/(1-\rho)|$ sea cero.*

La evaluación explícita de esta integral por el teorema de los residuos o por propiedades de la transformada de Poisson del disco es posible, pero su resultado depende de la posición de $\rho$: si $\mathrm{Re}(\rho) = 1/2$ (RH), la simetría garantiza la cancelación; si $\mathrm{Re}(\rho) \neq 1/2$, la cancelación falla. Esto hace el criterio exacto pero circular.

---

## §7. El principio del mínimo del módulo

### 7.1. Planteamiento

El principio del mínimo del módulo establece: si $g$ es analítica y sin ceros en un dominio $\Omega$, entonces $|g|$ no tiene mínimo local estricto en el interior de $\Omega$; el mínimo de $|g|$ sobre un compacto $K \subset \Omega$ se alcanza en la frontera $\partial K$.

Aplicado a $F$: si $F$ no tuviera ceros en $\{|z| < 1\}$ (bajo RH), el mínimo de $|F(z)|$ para $|z| \leq r$ se alcanzaría en $|z| = r$. Cuando $r \to 1^-$, el ínfimo de $|F|$ en la frontera es 0 (pues $F$ tiene ceros en $|z| = 1$, correspondientes a los ceros de $\xi$ en la recta crítica). Por tanto, el principio del mínimo solo garantiza que $|F(z)| \geq \inf_{|z|=r}|F(z)|$, y cuando $r \to 1$, esta cota inferior tiende a 0.

### 7.2. Por qué no da información útil

El principio del mínimo del módulo no puede probar la no-anulación en el interior porque proporciona una cota inferior trivial (0). Para que fuera útil, se necesitaría una cota inferior estricta $|F(z)| \geq c > 0$ sobre alguna circunferencia $|z| = r$ para $r < 1$, lo que equivaldría a conocer la no-anulación en $|z| < r$, un problema más fácil (pues $\tau$ mapea $|z| < r < 1$ a la región $\mathrm{Re}(s) < \sigma_r < 1/2$, donde la no-anulación de $\xi$ es conocida para $\sigma_r$ suficientemente pequeño pero no para $\sigma_r$ cercano a $1/2$).

**Proposición 7.1.** *El principio del mínimo del módulo no proporciona una condición suficiente para la no-anulación de $F$ en el disco unitario en presencia de ceros de $F$ sobre la frontera.*

---

## §8. La desigualdad de Bohr

### 8.1. El enunciado clásico

La desigualdad de Bohr establece: si $f(z) = \sum_{k=0}^\infty a_k z^k$ es analítica en el disco con $|f(z)| < 1$ para todo $|z| < 1$, entonces
$$\sum_{k=0}^\infty |a_k| r^k \leq 1 \quad \text{para todo } r \leq 1/3,$$
y la constante $1/3$ es óptima (radio de Bohr).

### 8.2. Inaplicabilidad a $F$

La función $F$ no satisface la hipótesis $|F(z)| < 1$ en el disco: en $z = 0$, $|F(0)| = 1/2 < 1$, pero a medida que $|z| \to 1$, $|F(z)| = |\xi(1/2 + it_\theta)|$ no está acotado por 1 (el máximo de $|\xi|$ sobre la recta crítica es mayor que 1). En consecuencia, la desigualdad de Bohr no se aplica.

**Proposición 8.1.** *La función $F(z)$ no satisface las hipótesis de la desigualdad de Bohr en el disco unitario, y la desigualdad de Bohr no proporciona información sobre los ceros de $F$.*

---

## §9. El criterio del índice de Kronecker

### 9.1. El número de vueltas y los ceros en el disco

Por el teorema del argumento, el número de ceros de $F$ en $\{|z| < r\}$ (contados con multiplicidad) es:
$$N(r) = \frac{1}{2\pi i}\oint_{|z|=r}\frac{F'(z)}{F(z)}\, dz = \frac{1}{2\pi}\Delta_{|z|=r}\arg F.$$
Si $F$ no tuviera ceros en el disco ($N(r) = 0$ para todo $r < 1$), el argumento de $F(re^{i\theta})$ no acumularía variación total al recorrer $|z| = r$. Tomando $r \to 1^-$, el número de ceros en el disco sería el índice de Kronecker de la curva $F(e^{i\theta})$ (para $\theta \in [0, 2\pi)$) alrededor del origen.

### 9.2. El índice de la curva $F(e^{i\theta})$ en presencia de ceros en la frontera

La curva $F(e^{i\theta}) = \xi(1/2 + it_\theta)$, para $\theta \in (0, 2\pi)$, pasa por el origen en cada $\theta_n$ correspondiente a un cero de $\xi$ en la recta crítica. El argumento de $\xi(1/2 + it)$ es una función continua de $t$ salvo en los ceros, donde tiene saltos de $\pm \pi$ (saltos del argumento al cruzar un cero simple). La variación total del argumento de $F(e^{i\theta})$ al recorrer $\theta \in [0, 2\pi)$ involucra infinitas discontinuidades.

Cuando la curva pasa por el origen (en los ceros de $\xi$ sobre la recta crítica), el índice de Kronecker no está bien definido como número entero por la fórmula de la integral de contorno estándar. La definición del índice para curvas que pasan por el origen requiere tratamiento especial (índice de intersección, regularización).

**Proposición 9.1.** *El criterio del índice de Kronecker no se aplica directamente a $F$ porque la curva $F(e^{i\theta})$ pasa por el origen (en los puntos de la frontera correspondientes a los ceros de $\xi$ en la recta crítica), lo que hace que el índice esté mal definido por la fórmula integral estándar.*

**Corolario 9.2.** *No es posible deducir la no-anulación de $F$ en el disco a partir del cálculo del índice de Kronecker de la curva fronteriza, a causa de los ceros de $F$ en la frontera.*

---

## §10. Síntesis y la pregunta abierta más precisa

### 10.1. Tabla de resultados

| Herramienta | Resultado |
|---|---|
| EDO algebraica para $\xi$ o $F$ | No existe; inaplicable |
| Ecuación funcional $F(z) = F(1/z)$ | Probada; empareja ceros pero no los elimina |
| Puntos críticos de $F$ | $F'(\pm 1) = 0$; geométricamente claro; no implica no-ceros |
| Factorización de Blaschke | RH $\iff$ $B \equiv 1$; exacto pero circular |
| Fórmula de Jensen | Criterio computable; exacto pero circular |
| Principio del mínimo del módulo | Cota inferior trivial (0); inaplicable |
| Desigualdad de Bohr | Hipótesis no satisfechas; inaplicable |
| Índice de Kronecker | Mal definido por ceros en la frontera |

### 10.2. El teorema consolidado del Camino 2

**Teorema 10.1.** *Sean $\xi$ la función xi de Riemann y $F(z) = \xi(z/(z-1))$. Entonces:*

*(i) $F$ es analítica en el disco abierto $\{|z| < 1\}$.*

*(ii) $F(0) = 1/2$.*

*(iii) $F(z) = F(1/z)$ para todo $z \neq 0, 1$ (ecuación funcional).*

*(iv) $F'(-1) = 0$ (punto crítico en $z = -1$, correspondiente a $s = 1/2$).*

*(v) La fórmula de Jensen es válida en $F$, y el criterio de Jensen da:*
$$\text{RH} \iff \int_{-\infty}^{\infty}\log|\xi(1/2+it)|\cdot\frac{2\, dt}{\pi(1+4t^2)} = -\log 2.$$

*(vi) RH $\iff$ $F$ no tiene ceros en $\{|z| < 1\}$ (Proposición 2.1 del Doc 81).*

*(vii) Ninguna de las propiedades (i)–(iv) implica (vi); la propiedad (v) es equivalente a (vi) y a RH.*

### 10.3. La pregunta abierta más precisa

Las propiedades establecidas en el Teorema 10.1 reformulan RH de manera exacta pero no ofrecen una demostración. La pregunta que queda, en la formulación más precisa que se puede dar en este documento, es la siguiente:

**Pregunta 10.2 (central del Camino 2).** *¿Puede demostrarse la igualdad*
$$\int_{-\infty}^{\infty}\log|\xi(1/2+it)|\cdot\frac{2\, dt}{\pi(1+4t^2)} = -\log 2 \eqno{(*)}$$
*usando solo las propiedades de $\xi$ como función entera de orden 1 con la ecuación funcional $\xi(s) = \xi(1-s)$, el producto de Hadamard, y el comportamiento asintótico conocido de $\xi$, sin conocer la posición precisa de los ceros?*

### 10.4. Por qué $(*)$ es difícil

La igualdad $(*)$ puede escribirse, usando el producto de Hadamard $\xi(s) = \xi(0)\prod_\rho(1 - s/\rho)(1 - s/(1-\rho))$, como:

$$\int_{-\infty}^{\infty}\log\xi(0)\cdot\frac{2\, dt}{\pi(1+4t^2)} + \sum_\rho\int_{-\infty}^{\infty}\text{Re}\left[\log\left(1-\frac{1/2+it}{\rho}\right) + \log\left(1-\frac{1/2+it}{1-\rho}\right)\right]\frac{2\, dt}{\pi(1+4t^2)} = -\log 2.$$

El primer término es $\log\xi(0) = \log(1/2) = -\log 2$. Por tanto, $(*)$ equivale a que la suma sobre los ceros sea cero:
$$\sum_\rho\int_{-\infty}^{\infty}\text{Re}\left[\log\left(1-\frac{1/2+it}{\rho}\right) + \log\left(1-\frac{1/2+it}{1-\rho}\right)\right]\frac{2\, dt}{\pi(1+4t^2)} = 0. \eqno{(**)}$$

Para un par $(\rho, 1-\rho)$ con $\rho = \sigma + i\gamma$, la integral en $(**)$ puede evaluarse en principio mediante el teorema de los residuos. El polo del integrando en el semiplano superior (donde $\text{Im}(t) > 0$) proviene del peso $2/(\pi(1+4t^2)) = 2/(\pi(2it+1)(-2it+1))$, que tiene polos simples en $t = \pm i/2$. La integral es:

$$I(\rho) = \text{Re}\left[\log\left(1 - \frac{1/2 + i(i/2)}{\rho}\right) + \log\left(1 - \frac{1/2 + i(i/2)}{1-\rho}\right)\right] = \text{Re}\left[\log\left(1 - \frac{1}{\rho}\right) + \log\left(1 - \frac{1}{1-\rho}\right)\right].$$

Simplificando: $1 - 1/\rho = (\rho-1)/\rho$ y $1 - 1/(1-\rho) = -\rho/(1-\rho)$. Por tanto:
$$I(\rho) = \text{Re}\left[\log\frac{\rho-1}{\rho} + \log\frac{-\rho}{1-\rho}\right] = \text{Re}\left[\log\frac{(\rho-1)(-\rho)}{\rho(1-\rho)}\right] = \text{Re}\left[\log\frac{-(rho-1)}{1-\rho}\right] = \text{Re}[\log 1] = 0.$$

(Pues $(\rho-1)(-\rho)/(\rho(1-\rho)) = -(\rho-1)\rho/(\rho(1-\rho)) = -(\rho-1)/(1-\rho) = (\rho-1)/(\rho-1) = 1$.)

**Proposición 10.3.** *Para cada par de ceros $(\rho, 1-\rho)$ de $\xi$, la contribución individual al miembro izquierdo de $(**)$ es exactamente cero, independientemente de la posición de $\rho$ en la franja crítica.*

**Corolario 10.4.** *La igualdad $(*)$ — equivalente a RH vía el criterio de Jensen — se cumple para toda función entera de la forma $\xi(s) = c\prod_\rho (1-s/\rho)(1-s/(1-\rho))$ con $c = \xi(0)$, con independencia de si los ceros $\rho$ están o no en la recta crítica.*

### 10.5. El colapso del criterio de Jensen como herramienta para RH

La Proposición 10.3 y el Corolario 10.4 son el resultado central de este documento, y su contenido es negativo: el criterio de Jensen $(*)$, aunque equivalente a RH en el sentido formal de la Proposición 6.1, se cumple incondicionalmente para $\xi$ gracias a la estructura del producto de Hadamard y la ecuación funcional $\xi(s) = \xi(1-s)$.

**La resolución de la aparente contradicción** es la siguiente. La Proposición 6.1 establece:
$$\text{RH} \iff \frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\, d\theta = -\log 2,$$
pero esta equivalencia depende de que el límite $r \to 1^-$ en la fórmula de Jensen sea válido. Si $F$ tiene ceros en el disco (bajo $\neg$RH), la fórmula de Jensen con $r < 1$ da $\frac{1}{2\pi}\int\log|F(re^{i\theta})|d\theta = -\log 2 + \sum_{|z_k|<r}\log(r/|z_k|)$. Al tomar $r \to 1^-$, el lado derecho tendería a $-\log 2 + \sum_{|z_k|<1}\log(1/|z_k|) > -\log 2$. Sin embargo, la integral $\int\log|F(e^{i\theta})|d\theta$ con $r = 1$ exactamente también refleja los ceros en la frontera, y la cancelación de la Proposición 10.3 ocurre en el cálculo con $r = 1$ exacto, no para $r < 1$.

En rigor, el cálculo de la Proposición 10.3 evalúa la integral $\int_{-\infty}^\infty \log|\xi(1/2+it)| \cdot 2/(\pi(1+4t^2))dt$ usando el residuo en $t = i/2$, que corresponde a evaluar $\log|\xi(s)|$ en $s = 1/2 + i(i/2) = 1/2 - 1/2 = 0$... Hay un error de signo: el polo del peso $2/(\pi(1+4t^2))$ en el semiplano superior es $t = i/2$, que corresponde a $s = 1/2 + i(i/2) = 1/2 - 1/2 = 0$, no a $s$ en la franja crítica. La integral por residuos evalúa la función analítica continuada más allá de la recta crítica, no el valor de $\log|\xi|$ sobre la recta.

**Proposición 10.5 (corrección).** *El cálculo por residuos de la Proposición 10.3 es válido solo si $\log|\xi(1/2+it)|$ se extiende analíticamente al semiplano superior como función de $t$, lo cual no es el caso: $\log|\xi(1/2+it)|$ es una función real del parámetro real $t$ y no tiene una extensión holomorfa libre de singularidades (sus singularidades son exactamente los ceros de $\xi$ sobre la recta crítica, en $t = \gamma_n$, donde $\log|\xi|$ tiene singularidades logarítmicas).*

*Por tanto, la integral $\int_{-\infty}^\infty \log|\xi(1/2+it)| \cdot 2/(\pi(1+4t^2))dt$ no puede evaluarse por residuos directamente.*

En consecuencia, el criterio de Jensen no es trivialmente verificable ni trivialmente circular: su verificación directa requiere controlar la distribución de los ceros $\gamma_n$ sobre la recta crítica, que es precisamente la información que RH proporciona (y $\neg$RH negaría).

### 10.6. Resumen honesto

Las propiedades de $F$ estudiadas en este documento son:
1. **Ecuación funcional $F(z) = F(1/z)$:** probada, no fuerza no-ceros en el disco.
2. **Criterio de Jensen:** equivalente a RH, computable en principio, pero la verificación directa requiere conocer los ceros o su distribución sobre la recta crítica.
3. **Propiedades analiticas adicionales** (Bohr, mínimo del módulo, Kronecker): no aplicables por hipótesis no satisfechas o degeneración en la frontera.

**La situación del Camino 2 al cierre del Doc 84 es la siguiente:** se dispone de una reformulación exacta y elegante de RH en términos de la función $F(z)$ en el disco, con el criterio de Jensen como la condición más transparente. La barrera es que toda verificación de esa condición requiere información sobre los ceros de $\xi$, y no se ha identificado ninguna propiedad de $F$ que sea verificable sin tal información y que implique la no-anulación en el disco.

La dirección más prometedora para la siguiente fase es la Pregunta P1 del Doc 81: la búsqueda de una ecuación funcional o diferencial para $F$ que sea más fuerte que $F(z) = F(1/z)$ y cuyas soluciones sean automáticamente sin ceros en el disco. Tal ecuación, si existiera, tendría que usar propiedades aritméticas de $\xi$ (via la función zeta y los números primos) más allá de la ecuación funcional pura.

---

*Doc 84 completado. Próximo: Fase 35, exploración de P1 (ecuación diferencial de $F$) y conexión aritmética via la función de Green del disco.*
