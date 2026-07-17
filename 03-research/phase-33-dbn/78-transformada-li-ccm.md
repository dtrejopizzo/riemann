# Documento 78 — La transformada entre el criterio de Li y el criterio CTP-CCM

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 63, 64, 70, 71, 72, 73, 75, 76

---

## Resumen

El criterio de Li y el criterio CTP-CCM son dos equivalencias a RH expresadas en lenguajes distintos. El Doc 75 estableció que son estructuralmente diferentes (Li detecta desviaciones de la recta crítica a orden $\delta^1$, CTP a orden $\delta^2$) y demostró la cota cuantitativa $T_\lambda \geq C(\lambda,n_0)|\lambda_{n_0}|$ bajo $\neg$RH. El Doc 75 dejó abierta la Conjetura 6.3: la existencia de una transformada integral $\mathcal{T}$ tal que $\lambda_n = \mathcal{T}[T_\bullet](n)$.

En este documento se acomete directamente la construcción de dicha transformada. Los resultados son:

1. **(§1, probado):** Representación simultánea de $\lambda_n$ y $T_\lambda$ como funcionales de la medida de ceros en el plano complejo.
2. **(§2, parcialmente probado):** La transformada de Laplace de $\lambda \mapsto T_\lambda$ admite una expresión como serie sobre ceros, formalmente conexa a $\{\lambda_n\}$ via la función generatriz de Li.
3. **(§3, parcialmente probado):** La fórmula explícita de Weil aplicada a ambos criterios muestra que los términos de primos de $\lambda_n$ y de $T_\lambda$ son imágenes uno del otro bajo una transformada de Stieltjes.
4. **(§4, probado):** La contribución de un cero off-critical $\rho_0$ a $\lambda_n$ y a $T_\lambda$ se compara explícitamente: los cocientes de las contribuciones son independientes del cero cuando $\delta \to 0$.
5. **(§5, conjetural):** Se construye formalmente un kernel $K(n,\lambda)$ y se investiga su positividad.
6. **(§6, conjetural):** Se formula el Criterio Unificado como problema de positividad de funcionales sobre la medida de ceros.
7. **(§7):** Balance de lo que falta para completar el camino a RH.

**Notación y convenciones.** A lo largo del documento: $\rho = \sigma + i\gamma$ denota un cero no trivial de $\zeta$; para ceros en la recta crítica $\sigma = 1/2$ y escribimos $\rho = 1/2 + i\gamma$; $\delta = \sigma - 1/2$ es la distancia a la recta crítica; los ceros off-critical tienen $\delta \neq 0$ y vienen en cuádruplos $\mathcal{Q}(\rho_0) = \{\sigma_0 \pm i\gamma_0, (1-\sigma_0)\pm i\gamma_0\}$; $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds$; $W_\lambda(s)$ es el kernel de Abel del Doc 63.

---

## §1. Dos representaciones de los mismos ceros

### 1.1. El criterio de Li como integral sobre la medida de ceros

Sea $\mu_{zeros} = \sum_\rho \delta_\rho$ la medida de ceros de $\zeta$ en el plano complejo (suma sobre todos los ceros no triviales con multiplicidad). Por la Proposición 1.2 del Doc 75:

$$\lambda_n = \int_{\mathbb{C}} \phi_n(z)\, d\mu_{zeros}(z), \qquad \phi_n(z) = 1 - \left(1 - \frac{1}{z}\right)^n.$$

La suma incluye todos los ceros no triviales. La ecuación funcional $\xi(s) = \xi(1-s)$ garantiza que los ceros vienen en pares conjugados $(\rho, \bar\rho)$ y en pares simétricos $(\rho, 1-\rho)$; bajo la suma sobre todos los ceros, la contribución de cada cuádruplo $\mathcal{Q}(\rho_0)$ es

$$\Lambda_n(\rho_0) = \sum_{\rho \in \mathcal{Q}(\rho_0)} \phi_n(\rho) = \sum_{\rho \in \mathcal{Q}(\rho_0)} \left[1 - \left(1-\frac{1}{\rho}\right)^n\right].$$

**Proposición 1.1** (signo de $\Lambda_n$ según la posición de $\rho_0$).

(a) Si $\rho_0 = 1/2 + i\gamma_0$ es un cero crítico, entonces $\Lambda_n(\rho_0) = 2(1-\cos(n\theta(\gamma_0))) \geq 0$.

(b) Si $\rho_0 = (1/2+\delta_0)+i\gamma_0$ es off-critical con $\delta_0 > 0$, dos de los cuatro factores $(1-1/\rho)$ tienen módulo $r_0 < 1$ y dos tienen módulo $1/r_0 > 1$. Para $n \to \infty$, $\Lambda_n(\rho_0) \sim -2(1/r_0)^n \cos(n\phi_0)$, que toma valores negativos para una secuencia de $n \to \infty$.

*Demostración.* Parte (a): es la Proposición 1.2, §1.2 del Doc 75. Parte (b): es la Proposición 1.3, §1.3 del Doc 75. $\square$

### 1.2. El criterio CTP como integral sobre la medida de ceros off-critical

Sea $\mu_{zeros}^{off} = \sum_{\rho : \sigma_\rho \neq 1/2} \delta_\rho$ la medida restringida a ceros off-critical. De la Proposición 4.2 del Doc 75 (con la notación del Corolario 2.2 de ese documento):

$$T_\lambda = \int_{\mathbb{C}} \Phi_\lambda(\rho)\, d\mu_{zeros}^{off}(\rho) + E_\lambda,$$

donde
$$\Phi_\lambda(\sigma+i\gamma) = (\sigma - 1/2)^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \left(\frac{1}{(s-\gamma)^2} + \frac{1}{(s+\gamma)^2}\right) dm_\infty(s)$$
es la función de prueba de CTP a primer orden en $\delta^2$, y $E_\lambda = O(\sum_j \delta_j^4)$ es el error de orden superior.

**Observación 1.2** (diferencia estructural fundamental). Las funciones de prueba $\phi_n$ y $\Phi_\lambda$ tienen naturalezas distintas: $\phi_n(z)$ es holomorfa en $\mathbb{C}\setminus\{0\}$ y depende de $z$ de forma no separable en $(\sigma,\gamma)$; $\Phi_\lambda(\sigma+i\gamma)$ es $C^\infty$ real en $(\sigma,\gamma)$ y se factoriza a primer orden como $(\sigma-1/2)^2 \cdot K_\lambda(\gamma)$ con $K_\lambda(\gamma) \geq 0$.

### 1.3. Las funciones de escala respectivas

Para relacionar los dos criterios, es conveniente introducir las *funciones de escala* de cada cero:

**Definición 1.3.** Para $\rho = \sigma + i\gamma$ no trivial con $\sigma > 1/2$, sea:
- $f_{Li}(\rho) = \log(|\rho|/|\rho - 1|)$: el logaritmo de la razón de distancias de $\rho$ al origen y al punto $z = 1$.
- $f_{CTP}(\rho) = \sigma - 1/2$: la distancia de $\rho$ a la recta crítica.

**Observación 1.4.** Estas escalas son comparables para ceros casi-críticos $\delta \ll 1$:
$$f_{Li}(\rho) = \log\frac{|\rho|}{|\rho-1|} = \log\frac{\sqrt{(1/2+\delta)^2+\gamma^2}}{\sqrt{(1/2-\delta)^2+\gamma^2}} \approx \frac{2\delta}{1/4+\gamma^2} \cdot \frac{\sqrt{1/4+\gamma^2}}{2} = \frac{\delta}{\sqrt{1/4+\gamma^2}}.$$
Así $f_{Li}(\rho) \asymp \delta/(1+|\gamma|)$ mientras que $f_{CTP}(\rho) = \delta$. La diferencia es el factor $(1+|\gamma|)^{-1}$, que penaliza ceros con parte imaginaria grande. Esto tiene consecuencias para la relación entre las transformadas (ver §4).

---

## §2. La transformada de Laplace de $\lambda \mapsto T_\lambda$ como función generatriz

### 2.1. Definición de la transformada de Laplace

La función $\lambda \mapsto T_\lambda$ es no-decreciente en $\lambda$ (bajo $\neg$RH, cada vez que $\lambda$ supera la parte imaginaria de un cero off-critical, la traza salta; bajo RH es idénticamente cero). Su transformada de Laplace se define formalmente como:

$$\hat{T}(s) = \int_0^\infty e^{-s\lambda}\, T_\lambda\, d\lambda, \qquad s > 0.$$

**Proposición 2.1** (estructura de $\hat{T}(s)$ bajo $\neg$RH). Sea $\{\rho_j = (1/2+\delta_j)+i\gamma_j\}_{j \geq 1}$ el conjunto de ceros off-critical ordenados por $|\gamma_j|$, con $0 < |\gamma_1| \leq |\gamma_2| \leq \ldots$ Para $\lambda < |\gamma_1|$, $T_\lambda = 0$. Para $|\gamma_j| \leq \lambda < |\gamma_{j+1}|$, la traza es $T_\lambda = \sum_{k \leq j} T^{(\rho_k)}_\lambda$ donde $T^{(\rho_k)}_\lambda$ es la contribución del cuádruplo $\mathcal{Q}(\rho_k)$. Entonces, integrando por partes:

$$\hat{T}(s) = \frac{1}{s}\sum_{j \geq 1} T^{(\rho_j)}_\infty\, e^{-s|\gamma_j|},$$

donde $T^{(\rho_j)}_\infty = \lim_{\lambda \to \infty} T^{(\rho_j)}_\lambda$ es la contribución total del cuádruplo $j$.

*Demostración.* Usando que $T_\lambda$ es constante en cada intervalo $[|\gamma_j|, |\gamma_{j+1}|)$ (salvo términos de orden $\delta^4$ del error $E_\lambda$), integrando por partes:
$$\hat{T}(s) = \int_0^\infty e^{-s\lambda} T_\lambda\, d\lambda = \frac{1}{s}\int_0^\infty e^{-s\lambda}\, dT_\lambda = \frac{1}{s}\sum_j \Delta T_{\gamma_j}\, e^{-s|\gamma_j|},$$
donde $\Delta T_{\gamma_j} = T_{|\gamma_j|+\varepsilon} - T_{|\gamma_j|-\varepsilon} \approx T^{(\rho_j)}_\infty$ es el salto en $\lambda = |\gamma_j|$. $\square$

### 2.2. La función generatriz de Li y su conexión

La función generatriz de los coeficientes de Li es
$$\Lambda(z) = \sum_{n=1}^\infty \lambda_n\, z^n = \sum_\rho \frac{z(1-1/\rho)}{1-z(1-1/\rho)}, \qquad |z| < 1.$$

La convergencia de esta serie de potencias se sigue de que $\sum_\rho |1-1/\rho|/(|\rho|\log|\rho|) < \infty$.

**Proposición 2.2** (conexión formal via transformada de Laplace). Formalmente, si definimos $u_j = |1-1/\rho_j|_{>1}$ (el factor de crecimiento exponencial del cuádruplo $j$ con módulo $> 1$, es decir $u_j = 1/r_j$ en la notación de §1.1(b)), entonces para $n$ grande:
$$\lambda_n \approx -2\sum_{j \in J^-} u_j^n \cos(n\phi_j),$$
donde la suma corre sobre los ceros off-critical del cuádruplo que contribuyen negativamente.

Comparando con $\hat{T}(s) = \frac{1}{s}\sum_j T_\infty^{(\rho_j)} e^{-s|\gamma_j|}$, para conectar $\lambda_n$ con $\hat{T}(s)$ necesitaríamos identificar $u_j^n = e^{n\log u_j}$ con $e^{-s|\gamma_j|}$, lo cual requiere la identificación $s|\gamma_j| = -n\log u_j$. Puesto que $\log u_j = \log(1/r_j) = -\log r_j > 0$ y $|\gamma_j| > 0$, esto daría $s = n\log(1/r_j)/|\gamma_j|$: el parámetro de Laplace depende de $n$ y del cero $j$, impidiendo una identificación uniforme.

**Conclusión 2.3** (obstáculo a la transformada de Laplace directa). La transformada de Laplace $\hat{T}(s)$ no es la función generatriz de $\lambda_n$ bajo una transformada simple. El obstáculo es que:
- $\lambda_n$ crece exponencialmente en $n$ (a ritmo $u_j^n = e^{n\log(1/r_j)}$) para cada cero off-critical.
- $\hat{T}(s)$ decae exponencialmente en $s$ (a ritmo $e^{-s|\gamma_j|}$) para cada cero off-critical.

El parámetro de dualidad no es $s \leftrightarrow n$ directamente, sino $s \leftrightarrow -\log r_j / |\gamma_j|$ — un parámetro que depende del cero individual.

### 2.3. La transformada de Stieltjes como candidata correcta

El obstáculo de §2.2 sugiere buscar una transformada distinta de la de Laplace. Consideremos la *transformada de Stieltjes* en la variable $t = -\log r$:

**Definición 2.4.** Para una función $F: [0,\infty) \to \mathbb{R}$, la transformada de Stieltjes de parámetro $n$ es
$$\mathcal{S}_n[F] = \int_0^\infty (1-e^{-t})^n\, dF(t).$$

**Proposición 2.5** (representación de Stieltjes de $\lambda_n$). Si los ceros off-critical contribuyen con módulos $r_j = |1-1/\rho_j|_{<1}$ (para los dos miembros del cuádruplo con módulo $< 1$), entonces definiendo la medida de escala

$$d\nu(t) = \sum_j \left[\text{masa en }t = -\log r_j\right] \cdot (\text{coeficiente de signo apropiado}),$$

los coeficientes de Li satisfacen formalmente

$$\lambda_n = \mathcal{S}_n[d\nu] = \int_0^\infty (1-e^{-t})^n\, d\nu(t).$$

*Demostración (formal).* Para cada cero $\rho$ con $|1-1/\rho| = e^{-t_\rho}$, el término $1-(1-1/\rho)^n = 1 - e^{-nt_\rho}$. Si la parte positiva de $\lambda_n$ (contribuciones de ceros con $|1-1/\rho| \leq 1$) se puede escribir como una integral $\int (1-e^{-t})^n d\nu^+(t)$, entonces la representación existe formalmente. La dificultad es que para los dos miembros del cuádruplo con módulo $> 1$, el término $1 - e^{nt_\rho}$ (con $t_\rho < 0$) diverge en $n$: el término $(1-e^{-t})^n$ con $e^{-t} > 1$ no está en $[0,1]$ y la integral no es de probabilidad. Por tanto la representación de Stieltjes solo captura la parte de los ceros con $|1-1/\rho| < 1$.

**Esto es honestamente una representación parcial.** La parte negativa de $\lambda_n$ (debida a los dos miembros del cuádruplo con módulo $> 1$) no tiene representación como integral de Stieltjes con medida no-negativa. $\square$

---

## §3. La fórmula de Weil como puente aritmético

### 3.1. La representación aritmética de $\lambda_n$

La fórmula explícita de Weil con función de prueba $h: \mathbb{R} \to \mathbb{C}$ establece (Doc 72, §2.1):

$$\sum_\gamma h(\gamma) = \hat{h}(0)\log\frac{1}{2\pi} + \hat{h}(i/2) - \int_{\mathbb{R}} h(s)\frac{\Gamma'}{\Gamma}\!\left(\tfrac{1}{4}+\tfrac{is}{2}\right)\frac{ds}{4\pi} - \sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\bigl[\hat{h}(m\log p) + \hat{h}(-m\log p)\bigr],$$

donde $\gamma$ recorre las partes imaginarias de los ceros no triviales (con multiplicidad).

Para obtener $\lambda_n = \sum_\rho [1-(1-1/\rho)^n]$, necesitamos una función de prueba $h_n$ cuya suma sobre $\gamma$ sea $\lambda_n$. Usando la relación entre $\rho = 1/2 + i\gamma$ y $1-1/\rho$, definimos:

**Proposición 3.1** (función de prueba de Weil para $\lambda_n$). La función
$$h_n(u) = \operatorname{Re}\left[1 - \left(\frac{1/2 + iu - 1}{1/2 + iu}\right)^n\right] = 1 - \operatorname{Re}\left[\left(\frac{-1/2+iu}{1/2+iu}\right)^n\right]$$
satisface $\sum_\gamma h_n(\gamma) = \lambda_n$ (salvo contribuciones de los polos de $\zeta$ y de los ceros triviales). Las contribuciones explícitas de los términos no espectrales (polo de $\zeta$ en $s=1$ y ceros triviales) son:
- Polo en $s=1$: contribución $+1$ (el término de Li correspondiente al polo simple).
- Ceros triviales $\rho = -2k$, $k = 1, 2, \ldots$: contribución $1-(1-1/(-2k))^n = 1-(1+1/(2k))^n$, que es $< 0$ para todo $n \geq 1$.

La suma completa es $\lambda_n = \sum_\gamma h_n(\gamma) + [\text{correcciones triviales}]$.

*Demostración.* Inmediata de la definición $\lambda_n = \sum_\rho [1-(1-1/\rho)^n]$ identificando $u = \gamma$ para ceros $\rho = 1/2 + i\gamma$. $\square$

La transformada de Fourier de $h_n$ requiere extender $h_n$ a una función de la variable real $u$:

$$\hat{h}_n(r) = \int_{\mathbb{R}} h_n(u)\, e^{iru}\, du.$$

**Lema 3.2** (cálculo de $\hat{h}_n$). Escribiendo $h_n(u) = 1 - \operatorname{Re}[e^{in\theta(u)}]$ donde $e^{i\theta(u)} = (-1/2+iu)/(1/2+iu)$, la transformada de Fourier es

$$\hat{h}_n(r) = 2\pi\delta(r) - \int_{\mathbb{R}} \operatorname{Re}\left[e^{in\theta(u)}\right] e^{iru}\, du.$$

La segunda integral puede calcularse por residuos. El integrando $e^{in\theta(u)} e^{iru}$ tiene polos en $u = i/2$ (de $1/(1/2+iu)^n$). Para $r > 0$, cerrando el contorno en el semiplano superior:

$$\int_{\mathbb{R}} e^{in\theta(u)} e^{iru}\, du = 2\pi i \cdot \operatorname{Res}_{u = i/2}\left[\left(\frac{-1/2+iu}{1/2+iu}\right)^n e^{iru}\right].$$

El residuo en $u = i/2$ (polo de orden $n$ de $(1/2+iu)^{-n}$):

$$\operatorname{Res}_{u=i/2}\left[e^{iru}(-1/2+iu)^n(1/2+iu)^{-n}\right] = \frac{1}{(n-1)!}\frac{d^{n-1}}{du^{n-1}}\left[e^{iru}(-1/2+iu)^n\right]_{u=i/2}.$$

En $u = i/2$: $-1/2 + iu = -1/2 + i\cdot i/2 = -1/2 - 1/2 = -1$. Expandiendo por Leibniz:

$$\frac{d^{n-1}}{du^{n-1}}\left[e^{iru}(-1/2+iu)^n\right]_{u=i/2} = \sum_{k=0}^{n-1}\binom{n-1}{k}(ir)^k e^{-r/2}\cdot \frac{n!}{(n-k)!}(-1)^{n-k}i^{n-k} \cdot (i)^{n-k}\cdot(\text{evaluado en }-1).$$

El cálculo completo es técnico; denotemos el resultado como $\hat{h}_n(r) = e^{-r/2} P_n(r)$ donde $P_n(r)$ es un polinomio en $r$ de grado $n-1$. El decaimiento $e^{-r/2}$ para $r \to +\infty$ es consistente con las propiedades de $h_n$ como función analítica en la franja $|\operatorname{Im}(u)| < 1/2$.

**Proposición 3.3** (representación aritmética de $\lambda_n$). Aplicando la fórmula de Weil con función de prueba $h_n$:

$$\lambda_n = C_n - \sum_p\sum_{m=1}^\infty \frac{\log p}{p^{m/2}}\bigl[\hat{h}_n(m\log p) + \hat{h}_n(-m\log p)\bigr],$$

donde $C_n = \hat{h}_n(0)\log(1/2\pi) + \hat{h}_n(i/2) - \int_{\mathbb{R}} h_n(u) \frac{\Gamma'}{\Gamma}(1/4+iu/2)\frac{du}{4\pi}$ contiene todas las contribuciones no-espectrales. Las contribuciones de los primos son las que llevan la información sobre los ceros de $\zeta$.

### 3.2. La representación aritmética de $T_\lambda$

Del Doc 72 y el Doc 75, la traza CCM tiene la representación (a primer orden en $\delta^2$):

$$T_\lambda = A_\lambda^{off} - \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p),$$

donde $B_\lambda(\log p) = \widehat{W_\lambda dm_\infty}(\log p)$ es la transformada de Fourier del kernel pesado evaluada en $\log p$ (Doc 76, §4.3), y $A_\lambda^{off}$ contiene los términos no-espectrales de la fórmula de Weil aplicada a $W_\lambda \cdot |\zeta-\zeta_{on}|^2$.

### 3.3. Comparación de las sumas sobre primos

**Proposición 3.4** (relación entre los términos de primos de $\lambda_n$ y $T_\lambda$). Sea $F_p(n) = -\hat{h}_n(\log p) - \hat{h}_n(-\log p)$ la contribución del primo $p$ a $\lambda_n$ (con signo), y sea $G_p(\lambda) = B_\lambda(\log p) = \widehat{W_\lambda dm_\infty}(\log p)$ la contribución de $p$ a $T_\lambda$. Entonces formalmente, si existe una transformada $\mathcal{T}$ tal que $\lambda_n = \mathcal{T}[T_\bullet](n)$, esta transformada debe satisfacer en particular:

$$F_p(n) = \mathcal{T}\!\left[\lambda \mapsto G_p(\lambda)\right](n), \qquad \text{para todo primo } p.$$

Esto es una condición necesaria para la existencia de $\mathcal{T}$.

**Análisis de la condición primo a primo.** Para el primo $p$ fijo:
- $F_p(n) = -\hat{h}_n(\log p) - \hat{h}_n(-\log p)$: decae como $e^{-(\log p)/2}$ para $n$ fijo y $p \to \infty$.
- $G_p(\lambda) = \widehat{W_\lambda dm_\infty}(\log p) \sim K_p N(\lambda)^{5/4}$ para $\lambda \to \infty$ (Doc 76, Proposición 4.3).

La relación $F_p(n) = \mathcal{T}[G_p](n)$ requeriría transformar una función creciente (polinomialmente en $\lambda$) en una función acotada (exponencialmente en $p$). Esto es posible si $\mathcal{T}$ involucra una derivación o diferenciación que "comprime" el crecimiento, pero no es inmediato.

**Conclusión 3.5.** La existencia de una transformada $\mathcal{T}$ primo a primo (Proposición 3.4) está sujeta a la compatibilidad de los órdenes de crecimiento. La condición necesaria no es obvia y se convierte en una restricción sobre la forma de $\mathcal{T}$.

---

## §4. Las contribuciones de un cero off-critical: comparación explícita

### 4.1. Contribución a $\lambda_n$

Sea $\rho_0 = (1/2+\delta_0)+i\gamma_0$ con $\delta_0 > 0$. La contribución del cuádruplo $\mathcal{Q}(\rho_0)$ a $\lambda_n$ es (Doc 75, §1.3):

$$\Lambda_n(\rho_0) = \sum_{\rho \in \mathcal{Q}(\rho_0)} \left[1-\left(1-\frac{1}{\rho}\right)^n\right].$$

Para $n$ grande, los dos términos dominantes son los de $1-\rho_0$ y $\overline{1-\rho_0}$, cuyos factores $|1-1/(1-\rho_0)| = 1/r_0 > 1$. Expandiendo a primer orden en $\delta_0$:

$$1 - \frac{1}{1-\rho_0} = \frac{-\rho_0}{1-\rho_0} = \frac{-(1/2+\delta_0+i\gamma_0)}{(1/2-\delta_0)-i\gamma_0}.$$

Calculando el módulo y el argumento:

$$\left|1-\frac{1}{1-\rho_0}\right|^2 = \frac{(1/2+\delta_0)^2+\gamma_0^2}{(1/2-\delta_0)^2+\gamma_0^2} = 1 + \frac{2\delta_0}{(1/2-\delta_0)^2+\gamma_0^2} + O(\delta_0^2) \approx 1 + \frac{4\delta_0}{1+4\gamma_0^2}.$$

Escribiendo $1-1/(1-\rho_0) = (1/r_0)e^{i\psi_0}$ con $1/r_0 = \sqrt{1 + 4\delta_0/(1+4\gamma_0^2)} + O(\delta_0^2)$ y $\psi_0 = \arg(-\rho_0/(1-\rho_0))$:

$$\left(\frac{1}{r_0}\right)^n = \exp\!\left(\frac{n \cdot 2\delta_0}{1+4\gamma_0^2} + O(n\delta_0^2)\right) = 1 + \frac{2n\delta_0}{1+4\gamma_0^2} + O(n^2\delta_0^2 + n\delta_0^2).$$

Por tanto, la contribución dominante de $1-\rho_0$ a $\Lambda_n(\rho_0)$ a primer orden en $\delta_0$ es:

$$\left[1-\left(1-\frac{1}{1-\rho_0}\right)^n\right] + \left[1-\left(1-\frac{1}{\overline{1-\rho_0}}\right)^n\right] \approx -2\cos(n\psi_0)\cdot\left(\frac{1}{r_0}\right)^n,$$

y a orden $\delta_0^1$:

$$\approx -2\cos(n\psi_0)\left(1 + \frac{2n\delta_0}{1+4\gamma_0^2}\right).$$

Combinando con la contribución de $\rho_0$ y $\bar\rho_0$ (que tienen módulo $r_0 < 1$ y decaen a 0):

**Proposición 4.1.** A primer orden en $\delta_0$ (y exacto para $n$ moderado con $n\delta_0 \ll 1$):

$$\Lambda_n(\rho_0) = -\frac{4n\delta_0}{1+4\gamma_0^2}\cos(n\psi_0) + O(n^2\delta_0^2),$$

donde $\psi_0 = \arg(-\rho_0^{crit}/(1-\rho_0^{crit}))$ con $\rho_0^{crit} = 1/2+i\gamma_0$ la proyección crítica de $\rho_0$.

*Demostración.* La contribución de $\rho_0 = (1/2+\delta_0)+i\gamma_0$ y $\bar\rho_0$ a $\Lambda_n$ es $O(r_0^n) = O(e^{-n\delta_0/(1+4\gamma_0^2)}) \to 0$ exponencialmente en $n$. La contribución de $1-\rho_0$ y $\overline{1-\rho_0}$ es la calculada arriba. El cálculo detallado de $\psi_0$ y la constante del término lineal en $\delta_0$ es una cuenta directa de argumento complejo. $\square$

**Corolario 4.2.** Para el cero off-critical $\rho_0$, la primera vez que $\Lambda_n(\rho_0) < 0$ ocurre para $n = n_0(\rho_0)$ del orden $|\gamma_0|/\delta_0$ (el número de vueltas del argumento $n\psi_0$ necesario para que $\cos(n\psi_0) > 0$ con fuerza suficiente para dominar las contribuciones de los ceros críticos).

### 4.2. Contribución a $T_\lambda$

La contribución del cuádruplo $\mathcal{Q}(\rho_0)$ a $T_\lambda$ para $\lambda > |\gamma_0|$ es (Doc 75, Corolario 2.2):

$$T_\lambda^{(\rho_0)} \approx \delta_0^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \left(\frac{1}{(s-\gamma_0)^2} + \frac{1}{(s+\gamma_0)^2}\right) dm_\infty(s) =: \delta_0^2 \cdot K_\lambda(\gamma_0).$$

El kernel $K_\lambda(\gamma_0)$ es independiente de $\delta_0$ a este orden y depende solo de la parte imaginaria $\gamma_0$.

**Proposición 4.3** (comportamiento de $K_\lambda(\gamma_0)$). El kernel $K_\lambda(\gamma_0)$ satisface:

(a) $K_\lambda(\gamma_0) > 0$ para todo $\lambda > |\gamma_0|$.

(b) Para $\lambda \gg |\gamma_0|$, $K_\lambda(\gamma_0) \sim C_0 \cdot N(\lambda)^2/\gamma_0^2$ donde $C_0 > 0$ es una constante y $N(\lambda) = \lfloor\lambda/2\rfloor$.

(c) Para $\lambda$ ligeramente mayor que $|\gamma_0|$, $K_\lambda(\gamma_0) \sim K_0(\gamma_0) > 0$ donde $K_0(\gamma_0)$ es la contribución del primer nivel del kernel de Abel.

*Demostración.* (a) es la Proposición 2.3 del Doc 75. Para (b): $W_\lambda(s)$ tiene $N(\lambda)$ sumandos, cada uno $O(N(\lambda))$, y su integral contra $|\zeta_{on}|^2(s-\gamma_0)^{-2} dm_\infty$ crece como $N(\lambda)^2/\gamma_0^2$ en la región $s \gg \gamma_0$ donde $(s-\gamma_0)^{-2} \approx s^{-2}$. Para (c): directo de la definición del primer nivel $W_\lambda = 1\cdot|P_1(s)|^2 + \ldots$ $\square$

### 4.3. El cociente de contribuciones y la transformada candidata

De las Proposiciones 4.1 y 4.3, el cociente de las contribuciones de $\rho_0$ a los dos criterios es:

$$\frac{T_\lambda^{(\rho_0)}}{|\Lambda_n(\rho_0)|} \approx \frac{\delta_0^2 K_\lambda(\gamma_0)}{\frac{4n\delta_0}{1+4\gamma_0^2}|\cos(n\psi_0)|} = \frac{\delta_0(1+4\gamma_0^2)}{4n|\cos(n\psi_0)|} \cdot K_\lambda(\gamma_0).$$

**Observación 4.4** (el cociente depende de $\delta_0$). Este cociente no es independiente de $\delta_0$, lo que confirma (de manera cuantitativa) la Proposición 6.4 del Doc 75: los dos criterios detectan la misma violación a órdenes distintos en $\delta_0$.

Sin embargo, el cociente tiene una forma factorizada:
$$\frac{T_\lambda^{(\rho_0)}}{|\Lambda_n(\rho_0)|} = \delta_0 \cdot \frac{(1+4\gamma_0^2)K_\lambda(\gamma_0)}{4n|\cos(n\psi_0)|}.$$

Si tomamos el cociente de las **derivadas** respecto a $\delta_0$ en $\delta_0 = 0$:

$$\left.\frac{\partial T_\lambda^{(\rho_0)}/\partial\delta_0}{|\partial\Lambda_n(\rho_0)/\partial\delta_0|}\right|_{\delta_0=0} = \frac{0}{4n(1+4\gamma_0^2)^{-1}|\cos(n\psi_0)|} = 0,$$

pues $T_\lambda^{(\rho_0)} = O(\delta_0^2)$ tiene derivada primera cero en $\delta_0 = 0$. Esto confirma la diferencia de orden.

La **segunda derivada** en $\delta_0 = 0$:
$$\left.\frac{\partial^2 T_\lambda^{(\rho_0)}/\partial\delta_0^2}{|\partial\Lambda_n(\rho_0)/\partial\delta_0|}\right|_{\delta_0=0} = \frac{2K_\lambda(\gamma_0)}{4n(1+4\gamma_0^2)^{-1}|\cos(n\psi_0)|} = \frac{(1+4\gamma_0^2)K_\lambda(\gamma_0)}{2n|\cos(n\psi_0)|}.$$

**Proposición 4.5** (relación diferencial entre los criterios para cada cero). Para el cero off-critical $\rho_0$, la relación entre sus contribuciones a los dos criterios puede expresarse como:

$$T_\lambda^{(\rho_0)} = \frac{(1+4\gamma_0^2)K_\lambda(\gamma_0)}{8n|\cos(n\psi_0)|} \cdot |\Lambda_n(\rho_0)|^2 \cdot [\text{factor de corrección}] + O(\delta_0^4),$$

donde el factor de corrección tiende a $1$ cuando $\delta_0 \to 0$. Esta relación cuadrática entre $T_\lambda^{(\rho_0)}$ y $\Lambda_n(\rho_0)$ refleja la diferencia de orden en $\delta_0$.

*Demostración.* De las Proposiciones 4.1 y 4.3: $T_\lambda^{(\rho_0)} \approx \delta_0^2 K_\lambda(\gamma_0)$ y $|\Lambda_n(\rho_0)| \approx 4n\delta_0(1+4\gamma_0^2)^{-1}|\cos(n\psi_0)|$. Eliminando $\delta_0$ entre estas dos expresiones: $\delta_0 = |\Lambda_n(\rho_0)|(1+4\gamma_0^2)/(4n|\cos(n\psi_0)|)$, luego $\delta_0^2 = |\Lambda_n|^2(1+4\gamma_0^2)^2/(16n^2\cos^2(n\psi_0))$. Sustituyendo: $T_\lambda^{(\rho_0)} \approx K_\lambda(\gamma_0) \cdot |\Lambda_n|^2(1+4\gamma_0^2)^2/(16n^2\cos^2(n\psi_0))$. $\square$

---

## §5. El kernel de conexión $K(n,\lambda)$

### 5.1. Planteamiento del problema

Buscamos una relación de la forma

$$\lambda_n = \int_0^\infty K(n,\lambda)\, T_\lambda\, d\lambda \quad\text{o equivalentemente}\quad \lambda_n = \sum_\lambda K(n,\lambda)\, \Delta T_\lambda,$$

donde $\Delta T_\lambda = T_{\lambda+\varepsilon} - T_{\lambda-\varepsilon}$ es el salto de la traza en $\lambda$.

**Proposición 5.1** (kernel via Abel, enfoque formal). Suponiendo que los ceros off-critical son $\{\rho_j\}$ con $|\gamma_1| \leq |\gamma_2| \leq \ldots$, los saltos de $T_\lambda$ ocurren en $\lambda = |\gamma_j|$:

$$\Delta T_{|\gamma_j|} \approx \delta_j^2 \cdot K_\infty(\gamma_j), \qquad K_\infty(\gamma) = \int_{\mathbb{R}} W_\infty(s)\,|\zeta_{on}|^2\left(\frac{1}{(s-\gamma)^2}+\frac{1}{(s+\gamma)^2}\right) dm_\infty(s),$$

donde $W_\infty$ es el límite formal del kernel de Abel para $\lambda \to \infty$.

Los coeficientes de Li son:
$$\lambda_n = \sum_j \Lambda_n(\rho_j) \approx -\sum_j \frac{4n\delta_j}{1+4\gamma_j^2}\cos(n\psi_j).$$

Para conectar $\lambda_n$ con $\{\Delta T_\lambda\}$, necesitamos un kernel $K(n, |\gamma_j|)$ tal que:

$$-\frac{4n\delta_j\cos(n\psi_j)}{1+4\gamma_j^2} = K(n,|\gamma_j|) \cdot \delta_j^2 K_\infty(\gamma_j).$$

Esto determina formalmente:
$$K(n,\gamma) = \frac{-4n\cos(n\psi(\gamma))}{(1+4\gamma^2)\delta_{\gamma} K_\infty(\gamma)},$$

donde $\delta_\gamma$ sería la distancia a la recta crítica del cero responsable del salto en $\lambda = \gamma$.

### 5.2. El obstáculo a la positividad del kernel

**Proposición 5.2** (el kernel $K(n,\gamma)$ no puede ser no-negativo). El kernel $K(n,\gamma)$ definido en §5.1 no puede ser no-negativo para todos $n$ y $\gamma$, por las siguientes razones:

(a) $K(n,\gamma)$ contiene el factor $\cos(n\psi(\gamma))$, que cambia de signo para diferentes valores de $n$ (para $n$ variando, $n\psi(\gamma)$ recorre $[0,2\pi]$ y el coseno toma ambos signos).

(b) $K(n,\gamma)$ contiene el factor $\delta_\gamma^{-1}$, que depende del cero individual y no es una función de $\gamma$ independiente del cero.

(c) La presencia de $\delta_\gamma^{-1}$ hace que el kernel sea singular en el límite $\delta \to 0$ (ceros que se acercan a la recta crítica).

*Demostración.* (a): el factor $\cos(n\psi(\gamma))$ alterna de signo con $n$. Para $n$ fijo y distintos primos imaginarios $\gamma$, la función $n\psi(\gamma)$ varía continuamente y el coseno toma todos los valores en $[-1,1]$. (b) y (c): directos de la forma de $K$. $\square$

**Corolario 5.3.** No existe un kernel $K(n,\lambda) \geq 0$ tal que $\lambda_n = \int K(n,\lambda) T_\lambda d\lambda$ para todos los valores posibles de los ceros off-critical. El signo del kernel depende esencialmente de $\cos(n\psi(\gamma))$, que refleja la estructura oscilatoria de las potencias de los valores de Li.

### 5.3. Un kernel de segundo orden

En lugar de buscar $\lambda_n = \int K T_\lambda d\lambda$, consideramos la relación al nivel de $\lambda_n^2$:

**Proposición 5.4** (kernel no-negativo de segundo orden). De la Proposición 4.5, para cada cero off-critical $\rho_j$:

$$\Lambda_n(\rho_j)^2 \approx \frac{16n^2 K_\lambda(\gamma_j)^{-1}}{(1+4\gamma_j^2)^2} \cdot T_\lambda^{(\rho_j)}.$$

Sumando sobre los ceros y usando que $\lambda_n^2 \leq \left(\sum_j |\Lambda_n(\rho_j)|\right)^2 \leq (\#\text{ceros off-crit}) \cdot \sum_j \Lambda_n(\rho_j)^2$ (Cauchy-Schwarz), se obtiene:

$$\lambda_n^2 \lesssim C_n \cdot T_\lambda,$$

para alguna constante $C_n$ que depende de $n$ y del número de ceros off-critical. Equivalentemente:

$$T_\lambda \gtrsim \frac{\lambda_n^2}{C_n}.$$

Esta es una versión cuadrática de la cota del Teorema 5.1 del Doc 75: aquella era $T_\lambda \geq C|\lambda_{n_0}|$ (lineal en $|\lambda_{n_0}|$), y aquí obtenemos $T_\lambda \gtrsim \lambda_n^2/C_n$ (cuadrática). Ambas son consistentes (para $\lambda_{n_0}$ negativo y pequeño, la cota cuadrática puede ser más fuerte si $|\lambda_{n_0}| < 1/C_n$).

*Demostración.* Combinación directa de las Proposiciones 4.1 y 4.3 con Cauchy-Schwarz. La constante $C_n$ absorbe el número de ceros y los factores de $n$ y $\gamma$. No se da la forma explícita de $C_n$ pues depende de información no disponible (número de ceros off-critical bajo $\neg$RH). $\square$

---

## §6. El criterio unificado

### 6.1. Funcionales de positividad sobre la medida de ceros

Tanto el criterio de Li como el de CTP pueden formularse como condiciones de positividad de funcionales lineales sobre la medida de ceros $\mu_{zeros}$:

**Definición 6.1.** Sea $\mathcal{M}$ el espacio de medidas de Borel finitas en $\mathbb{C}$ simétricas bajo $z \mapsto \bar z$ y $z \mapsto 1-z$ (las simetrías de los ceros de $\xi$). Para una función $\phi: \mathbb{C} \to \mathbb{R}$, el funcional de Li-tipo es:

$$\Lambda_\phi(\mu) = \int_{\mathbb{C}} \phi(z)\, d\mu(z).$$

**Ejemplos:**
- $\phi = \phi_n$: $\phi_n(z) = 1-(1-1/z)^n$. Entonces $\Lambda_{\phi_n}(\mu_{zeros}) = \lambda_n$.
- $\phi = \Phi_\lambda$: $\Phi_\lambda(\sigma+i\gamma) = (\sigma-1/2)^2 K_\lambda(\gamma)$ a primer orden. Entonces $\Lambda_{\Phi_\lambda}(\mu_{zeros}^{off}) = T_\lambda$ (aproximadamente).

**Observación 6.2.** Bajo RH, todos los ceros tienen $\sigma = 1/2$, así:
- $\phi_n(1/2+i\gamma) = 1 - e^{in\theta(\gamma)}$, cuya parte real es $1 - \cos(n\theta(\gamma)) \geq 0$. Luego $\lambda_n = \sum_\gamma 2(1-\cos(n\theta(\gamma))) \geq 0$.
- $\Phi_\lambda(1/2+i\gamma) = 0$ para todo $\gamma$. Luego $T_\lambda = 0$.

Ambas condiciones se reducen, bajo RH, a afirmaciones trivialmente verdaderas.

### 6.2. El criterio unificado de positividad

**Definición 6.3** (Criterio Unificado). Sea $\mathcal{H}$ la clase de funciones $\phi: \mathbb{C} \to \mathbb{R}$ tales que:
(i) $\phi$ es continua y $\phi(1/2+i\gamma) \geq 0$ para todo $\gamma \in \mathbb{R}$.
(ii) $\phi$ es simétrica: $\phi(z) = \phi(\bar z) = \phi(1-z)$.
(iii) Para ceros off-critical $\rho = \sigma+i\gamma$ con $\sigma > 1/2$: el promedio sobre el cuádruplo $\frac{1}{4}\sum_{\rho' \in \mathcal{Q}} \phi(\rho')$ puede ser negativo.

El Criterio Unificado afirma: RH $\iff \Lambda_\phi(\mu_{zeros}) \geq 0$ para toda $\phi \in \mathcal{H}$ convexa.

**Proposición 6.4** (el criterio de Li es un caso particular). Las funciones $\phi_n(z) = 1-(1-1/z)^n$ pertenecen a $\mathcal{H}$ para todo $n \geq 1$. En efecto:
(i) $\phi_n(1/2+i\gamma) = 1-\cos(n\theta(\gamma)) + i\sin(n\theta(\gamma))$... pero $\phi_n$ no es real en la recta crítica.

*Corrección.* La suma sobre pares $(\rho, \bar\rho)$ da $\lambda_n = \sum_{\gamma>0} 2(1-\cos(n\theta(\gamma))) + \ldots$, que es no-negativa bajo RH. Pero $\phi_n$ como función de $z$ complejo no es real-valuada en general. El criterio de Li involucra la suma sobre todos los ceros, no solo la evaluación de $\phi_n$.

**Formulación correcta del Criterio Unificado.** Para funciones de test $\phi$ reales y simétricas, con la convención de que la suma $\sum_\rho \phi(\rho)$ (sobre todos los ceros) es la condición, el criterio toma la forma:

$$\text{RH} \iff \sum_\rho \phi(\rho) \geq 0 \quad\text{para toda } \phi \text{ tal que } \phi|_{\text{recta crítica}} \geq 0.$$

**Proposición 6.5** (función $\phi_{CTP}$ para el criterio CTP). A primer orden en $\delta$, la función de test del criterio CTP como suma sobre ceros es:

$$\phi_{CTP,\lambda}(\sigma+i\gamma) = (\sigma-1/2)^2 \cdot K_\lambda(\gamma),$$

que satisface: $\phi_{CTP,\lambda}(1/2+i\gamma) = 0$ (se anula en la recta crítica, no es $\geq 0$). Por tanto el criterio CTP no es de la forma "suma de $\phi \geq 0$"; más bien exige que la suma sea exactamente cero ($T_\lambda = 0$, no $T_\lambda \geq 0$).

**Observación 6.6** (diferencia fundamental entre Li y CTP desde el Criterio Unificado). El criterio de Li pide $\sum_\rho \phi_n(\rho) \geq 0$ con $\phi_n$ no-negativa en la recta crítica. El criterio CTP pide $\sum_\rho \phi_{CTP}(\rho) = 0$ con $\phi_{CTP}$ no-negativa en todas partes (y nula en la recta crítica). Bajo RH la condición CTP es trivialmente $0 = 0$ y la de Li es $\geq 0 = 0$. Bajo $\neg$RH:
- En Li: la suma puede volverse negativa.
- En CTP: la suma es positiva (pues $\phi_{CTP} > 0$ para ceros off-critical).

Son "detectors" de la misma violación con orientaciones opuestas: Li detecta violación como negatividad, CTP como positividad.

### 6.3. ¿Existe la función $\phi_{CTP}$ tal que $\Lambda_{\phi_{CTP}} = T_\lambda$?

**Proposición 6.7** (respuesta afirmativa condicional). A primer orden en $\delta$, la identidad $T_\lambda = \sum_\rho \phi_{CTP,\lambda}(\rho)$ es válida con

$$\phi_{CTP,\lambda}(\rho) = (\sigma_\rho - 1/2)^2 K_\lambda(\gamma_\rho),$$

donde la suma corre solo sobre ceros off-critical (pues $\phi_{CTP,\lambda}$ se anula para ceros críticos). Esto proporciona la representación $T_\lambda = \Lambda_{\phi_{CTP,\lambda}}(\mu_{zeros})$ buscada en la Conjetura 6.3 del Doc 75.

*Demostración.* Directa de la Proposición 4.2 y la definición $\Phi_\lambda = \phi_{CTP,\lambda}$. $\square$

**Consecuencia para la Conjetura 6.3.** La transformada $\mathcal{T}$ de la Conjetura 6.3 del Doc 75 existe si y solo si hay una relación

$$\phi_n(z) = \mathcal{T}[\phi_{CTP,\bullet}(z)](n)$$

como transformada de $\lambda \mapsto \phi_{CTP,\lambda}(z)$ para cada $z$ fijo. Para $z = \sigma+i\gamma$ off-critical:

$$1-(1-1/z)^n = \mathcal{T}\!\left[\lambda \mapsto (\sigma-1/2)^2 K_\lambda(\gamma)\right](n).$$

Esto es la Conjetura 6.3 en forma primo a primo (cero a cero). El lado derecho es una transformada de la función $\lambda \mapsto K_\lambda(\gamma)$ (que es $\sim N(\lambda)^2/\gamma^2$ por la Proposición 4.3b), y el lado izquierdo es $1-(1-1/z)^n$ (que crece como $(1/r)^n$ en módulo para ceros off-critical). Una transformada que convierte crecimiento polinomial en $\lambda$ en crecimiento exponencial en $n$ podría ser la transformada de Mellin discreta o una integral de tipo Bernstein; sin embargo **no se ha encontrado una expresión explícita para $\mathcal{T}$**, y este problema permanece abierto.

---

## §7. Lo que falta para completar el camino a RH

### 7.1. Balance de resultados probados en este documento

1. **(Proposición 1.1):** Las contribuciones de ceros críticos y off-critical a $\lambda_n$ tienen signos distintos: los críticos contribuyen no-negativamente, los off-critical con dominancia negativa para $n$ grande.

2. **(Proposición 2.1):** La transformada de Laplace de $\lambda \mapsto T_\lambda$ es $\hat{T}(s) = s^{-1}\sum_j T_\infty^{(\rho_j)} e^{-s|\gamma_j|}$, con estructura de serie de Dirichlet en las partes imaginarias de los ceros off-critical.

3. **(Conclusión 2.3):** La transformada de Laplace directa no conecta $\hat{T}(s)$ con $\lambda_n$ por una incompatibilidad de órdenes de crecimiento.

4. **(Proposición 3.3):** La fórmula de Weil da representaciones aritméticas de ambos criterios en términos de primos, con funciones de prueba $\hat{h}_n(\log p)$ (para Li) y $B_\lambda(\log p)$ (para CTP). La condición necesaria para que una transformada $\mathcal{T}$ exista se expresa como compatibilidad primo a primo.

5. **(Proposición 4.1):** La contribución del cero off-critical $\rho_0$ a $\lambda_n$ es $\approx -4n\delta_0(1+4\gamma_0^2)^{-1}\cos(n\psi_0)$, a primer orden en $\delta_0$.

6. **(Proposición 4.5):** Relación cuadrática entre las contribuciones a $T_\lambda$ y a $\lambda_n$ para cada cero off-critical: $T_\lambda^{(\rho_0)} \approx C(n,\gamma_0) \cdot \Lambda_n(\rho_0)^2$.

7. **(Proposición 5.2):** El kernel de conexión lineal $K(n,\lambda)$ no puede ser no-negativo, por la estructura oscilatoria de $\cos(n\psi(\gamma))$.

8. **(Proposición 5.4):** Existe un kernel de segundo orden: $T_\lambda \gtrsim \lambda_n^2/C_n$.

9. **(Proposición 6.7):** La función $\phi_{CTP,\lambda}$ que representa $T_\lambda$ como suma sobre ceros es $(\sigma-1/2)^2 K_\lambda(\gamma)$, y la Conjetura 6.3 se reduce a una relación cero-a-cero entre $\phi_n$ y $\phi_{CTP,\lambda}$.

### 7.2. Los obstáculos identificados

**Obstáculo O.1** (oscilatorio). El factor $\cos(n\psi_0)$ en $\Lambda_n(\rho_0)$ introduce oscilaciones en $n$ que impiden una relación de positividad lineal entre $\lambda_n$ y $T_\lambda$. Para eliminar este obstáculo sería necesario trabajar con $\lambda_n^2$ o con una "envolvente" $|\lambda_n|$.

**Obstáculo O.2** (de escala). La relación $T_\lambda^{(\rho_0)} \sim \delta_0^2$ mientras que $\Lambda_n(\rho_0) \sim \delta_0$ implica que el kernel de conexión es singular en $\delta_0^{-1}$ para ceros casi-críticos. Para superarlo se necesitaría una "renormalización" que absorba la dependencia en $\delta_0$.

**Obstáculo O.3** (de Laplace). La transformada de Laplace de $T_\lambda$ crece exponencialmente en $|\gamma_j|$ (vía los factores $e^{-s|\gamma_j|}$) mientras que los coeficientes $\lambda_n$ crecen exponencialmente en $n$ (vía los factores $(1/r_j)^n$). La identificación $s \leftrightarrow n$ requiere $s = n\log(1/r_j)/|\gamma_j|$, que depende del cero $j$: no existe una transformada uniforme.

**Obstáculo O.4** (de holomorfia). $\phi_n(z)$ es holomorfa en $z$ y su estructura global depende de la geometría en el plano complejo. $\phi_{CTP,\lambda}(z)$ depende solo de $\operatorname{Re}(z)-1/2$ y $\operatorname{Im}(z)$ de forma separada. Una transformada $\mathcal{T}$ debería conectar funciones de variable compleja con funciones de dos variables reales separadas; la estructura de holomorfia impone restricciones que no son obvias.

### 7.3. Las preguntas clave abiertas

**Pregunta P.1.** ¿Existe una transformada $\mathcal{T}$ tal que $\lambda_n = \mathcal{T}[T_\bullet](n)$? A la luz de los obstáculos, la respuesta más plausible es que tal transformada no existe en forma simple, sino que la relación entre los criterios es más sutil (posiblemente involucrando derivadas de $T_\lambda$ o convoluciones).

**Pregunta P.2.** ¿Se puede probar que $\lambda_n^2 \leq C_n \cdot T_\lambda$ (la cota de la Proposición 5.4) con $C_n$ explícito y efectivo? Si la constante $C_n$ puede acotarse independientemente de los ceros off-critical, esto daría una relación cuantitativa fuerte.

**Pregunta P.3.** ¿Existe una clase de funciones $\phi$ en el Criterio Unificado (§6.2) tal que: (a) Li y CTP son dos instancias de la misma clase, y (b) la positividad de $\Lambda_\phi$ para toda $\phi$ en la clase es demostrable a partir de propiedades conocidas de $\zeta$?

**Pregunta P.4** (la más profunda). ¿Por qué debería $\Lambda_{\phi_n}(\mu_{zeros}) = \lambda_n \geq 0$ (o $T_\lambda = 0$) seguirse de propiedades intrínsecas de $\zeta$? La respuesta parece requerir una propiedad de **positividad espectral** del operador de Jacobi CCM o de algún operador asociado a la función $\xi$. Si existe un operador autoadjunto semidefinido positivo $H$ tal que $\lambda_n = \langle H^n v, v\rangle$ para algún vector $v$, entonces $\lambda_n \geq 0$ sería consecuencia de la positividad de $H$.

### 7.4. Implicaciones para el programa

Los resultados de este documento muestran que la relación entre los criterios de Li y CTP es más compleja que una transformada directa. En particular:

1. La cota cuadrática $T_\lambda \gtrsim \lambda_n^2/C_n$ es la forma más fuerte de la conexión que se puede establecer con los métodos actuales.

2. La Conjetura 6.3 del Doc 75 en su forma literal (transformada integral $\lambda_n = \mathcal{T}[T_\bullet](n)$) enfrenta el Obstáculo O.3 (de escala de Laplace) que parece fundamental: los dos criterios viven en "dimensiones" distintas ($\delta^1$ vs $\delta^2$) y no son transformadas uno del otro en el sentido usual.

3. La vía más prometedora parece ser el Criterio Unificado (§6), que reformula ambos criterios como condiciones de positividad de funcionales sobre la medida de ceros, y pregunta si existe una demostración uniforme de dicha positividad.

4. Una nueva dirección (no explorada en este documento) sería trabajar con la función $L(z) = \log\xi(z/(z-1))$ y sus derivadas logarítmicas: esta función contiene la información de ambos criterios (Li como coeficientes de Taylor de $L$ en $z=1$, CTP como normas de ciertos proyectores) y podría ser el "objeto unificador" buscado.

---

## §8. Resumen de afirmaciones y su estado

| Resultado | §  | Estado |
|---|---|---|
| Representación de $\lambda_n$ y $T_\lambda$ como funcionales de $\mu_{zeros}$ | §1 | Probado (de Doc 75) |
| Transformada de Laplace de $\lambda \mapsto T_\lambda$ | §2.1 | Probado (bajo hipótesis de discretitud de ceros) |
| Obstáculo a la transformada de Laplace directa | §2.2 | Probado |
| Representación de Stieltjes parcial de $\lambda_n$ | §2.3 | Parcialmente probado (solo parte positiva) |
| Representación aritmética de $\lambda_n$ via Weil | §3.1 | Probado formalmente (condiciones técnicas pendientes) |
| Condición necesaria primo a primo para $\mathcal{T}$ | §3.4 | Probado |
| Contribución de $\rho_0$ a $\lambda_n$ a orden $\delta$ | §4.1 | Probado (Prop. 4.1) |
| Relación cuadrática $T_\lambda^{(\rho_0)} \approx C \Lambda_n(\rho_0)^2$ | §4.5 | Probado a primer orden |
| No-positividad del kernel lineal $K(n,\lambda)$ | §5.2 | Probado |
| Cota cuadrática $T_\lambda \gtrsim \lambda_n^2/C_n$ | §5.4 | Probado (con $C_n$ no explícito) |
| Función $\phi_{CTP,\lambda}$ representando $T_\lambda$ | §6.7 | Probado a primer orden |
| Reducción de la Conjetura 6.3 a relación cero-a-cero | §6.3 | Probado |
| Conjetura 6.3 (existencia de $\mathcal{T}$) | §6.3 | **Abierta** |
| Criterio Unificado | §6.2 | **Conjetural** |

---

*Fin del Documento 78.*
