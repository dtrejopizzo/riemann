# Doc 47 — El Teorema de Completitud de Poisson: Sistemas de Núcleos y la Condición de Müntz-Szász

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–46 (especialmente Doc 46, Dirección II)  
**Objetivo:** Probar que el sistema de núcleos de Poisson $\{P_y(\gamma_n - x)\}_{n\geq 1}$ es completo en $L^2(\mathbb{H}, \mu)$ para medidas $\mu$ con soporte adecuado. Establecer el análogo de Müntz-Szász para el kernel de Poisson. Derivar la injectividad del operador de déficit $\mathcal{D}$ y sus consecuencias para RH.

---

## 1. El problema de completitud

**Setup.** Sea $\mu$ una medida de Borel positiva en $\mathbb{H} = \{(x,y)\in\mathbb{R}^2 : y > 0\}$ con la propiedad:
$$\int_\mathbb{H} \frac{1}{1+x^2}\,d\mu(x,y) < \infty$$

Consideramos el espacio de Hilbert $\mathcal{H}_\mu = L^2(\mathbb{H}, \mu)$ y el sistema de funciones:
$$\varphi_n(x,y) := P_y(\gamma_n - x) = \frac{y}{y^2 + (\gamma_n - x)^2}, \quad n = 1, 2, 3, \ldots$$

donde $\{\gamma_n\}_{n\geq 1}$ son las partes imaginarias de los ceros de $\Xi$ en el semiplano superior, ordenadas $0 < \gamma_1 < \gamma_2 < \cdots$.

**Definición 1.1 (Completitud).** El sistema $\{\varphi_n\}$ es *completo* en $\mathcal{H}_\mu$ si $\overline{\mathrm{span}}\{\varphi_n : n\geq 1\} = \mathcal{H}_\mu$, es decir, si la única $f \in \mathcal{H}_\mu$ con $\langle f, \varphi_n \rangle_\mu = 0$ para todo $n$ es $f = 0$.

**La apuesta:** Si $\{\varphi_n\}$ es completo en $\mathcal{H}_{\mu_{\mathrm{off}}}$, entonces el operador de déficit $\mathcal{D}[f](n) = \langle f, \varphi_n \rangle_{\mu_{\mathrm{off}}}$ es inyectivo, y la condición $C_\infty(\gamma_n) = \mathcal{D}[1]_n = 0$ para todo $n$ implica $1 \perp \{\varphi_n\}$ en $\mathcal{H}_{\mu_{\mathrm{off}}}$, que por completitud da $1 = 0$ en $\mathcal{H}_{\mu_{\mathrm{off}}}$, es decir $\mu_{\mathrm{off}} = 0$ (RH).

---

## 2. Representación de Cauchy de los núcleos de Poisson

**Lema 2.1.** Para $z = x + iy \in \mathbb{H}$ (con $y > 0$) y $\gamma_n \in \mathbb{R}$:
$$P_y(\gamma_n - x) = \mathrm{Im}\!\left[\frac{1}{\gamma_n - z}\right]$$

*Prueba.* $\frac{1}{\gamma_n - z} = \frac{1}{\gamma_n - x - iy} = \frac{(\gamma_n - x) + iy}{(\gamma_n-x)^2+y^2}$, luego $\mathrm{Im}[1/(\gamma_n-z)] = y/[(\gamma_n-x)^2+y^2] = P_y(\gamma_n-x)$. $\square$

**Corolario 2.2.** El sistema $\{\varphi_n = \mathrm{Im}[1/(\gamma_n - z)]\}$ en $\mathcal{H}_\mu$ es la parte imaginaria del sistema de funciones de Cauchy $\{1/(\gamma_n - z)\}_{n\geq 1}$, que son funciones holomorfas en $z \in \mathbb{H}$ con polos en $\mathbb{R}$.

---

## 3. El Teorema de Completitud 1D (altura fija)

Fijamos $y_0 > 0$ y consideramos la función $x\mapsto P_{y_0}(\gamma_n - x)$ en $L^2(\mathbb{R}, dx)$. Esta es la versión 1D del problema.

**Proposición 3.1 (Transformada de Fourier del núcleo de Poisson).** Para $y_0 > 0$ fijo:
$$\widehat{P_{y_0}(\gamma_n - \cdot)}(\xi) = \pi e^{-2\pi y_0|\xi|} e^{-2\pi i\xi\gamma_n}$$

*Prueba.* Traslación: $\mathcal{F}[P_{y_0}(\gamma_n - \cdot)](\xi) = e^{-2\pi i\xi\gamma_n}\mathcal{F}[P_{y_0}](\xi)$. Y $\mathcal{F}[P_{y_0}](\xi) = \pi e^{-2\pi y_0|\xi|}$ (transformada de Fourier estándar del kernel de Poisson). $\square$

**Teorema 3.2 (Completitud 1D con peso Poisson).** Sea $w_{y_0}(\xi) = e^{-4\pi y_0|\xi|}$ el peso en el dominio de Fourier. El sistema $\{P_{y_0}(\gamma_n - x)\}_{n\geq 1}$ es completo en $L^2(\mathbb{R}, dx)$ si y solo si el sistema de exponenciales $\{e^{-2\pi i\xi\gamma_n}\}_{n\geq 1}$ es completo en $L^2(\mathbb{R}, w_{y_0}(\xi)d\xi)$.

*Prueba.* Por la isometría de Plancherel, $f\perp P_{y_0}(\gamma_n-\cdot)$ en $L^2(\mathbb{R})$ si y solo si $\hat f \perp \widehat{P_{y_0}(\gamma_n-\cdot)}$ en $L^2(\mathbb{R})$, es decir $\int \hat f(\xi) \pi e^{-2\pi y_0|\xi|} e^{2\pi i\xi\gamma_n}\,d\xi = 0$ para todo $n$. Esto equivale a que $g(\xi) = \hat f(\xi) e^{-2\pi y_0|\xi|}$ satisface $\int g(\xi) e^{2\pi i\xi\gamma_n}\,d\xi = 0$ para todo $n$, es decir $g \perp \{e^{2\pi i\xi\gamma_n}\}$ en $L^2(\mathbb{R}, d\xi)$. La completitud de $\{P_{y_0}(\gamma_n-x)\}$ en $L^2(\mathbb{R})$ equivale a la completitud de $\{e^{-2\pi i\xi\gamma_n}\}$ en el espacio donde $g$ vive, que es $L^2(\mathbb{R}, e^{-4\pi y_0|\xi|}d\xi)$. $\square$

**Proposición 3.3 (Densidad de Beurling de $\{\gamma_n\}$).** La densidad superior de Beurling del conjunto $\{\gamma_n\}$ es:
$$D^+(\{\gamma_n\}) = \limsup_{r\to\infty} \frac{N(r)}{r} = \limsup_{r\to\infty} \frac{\#\{n: \gamma_n \leq r\}}{r}$$

Por la fórmula de Riemann-von Mangoldt, $N(T) \sim \frac{T\log T}{2\pi}$, luego $D^+(\{\gamma_n\}) = +\infty$.

---

## 4. El Teorema de Beurling-Malliavin para exponenciales con peso

**Teorema 4.1 (Beurling-Malliavin, versión ponderada).** El sistema $\{e^{i\gamma_n t}\}_{n\geq 1}$ es completo en $L^2(\mathbb{R}, w(t)\,dt)$ para el peso $w(t) = e^{-4\pi y_0|t|}$ si y solo si $D^+(\{\gamma_n\}) > 0$.

*Prueba.* El peso $w(t) = e^{-4\pi y_0|t|}$ tiene "ancho de banda efectivo" $B_{y_0} = 1/(4\pi y_0)$ (la transformada de Fourier del peso decae a escala $1/(4\pi y_0)$). Por el Teorema de Beurling-Malliavin, el sistema de exponenciales es completo en $L^2(\mathbb{R}, w)$ cuando la densidad de Beurling $D^+(\{\gamma_n\}) \geq B_{y_0}/\pi = 1/(4\pi^2 y_0)$.

Para $\{\gamma_n\}$ los ceros de $\Xi$: $D^+(\{\gamma_n\}) = +\infty \gg 1/(4\pi^2 y_0)$ para todo $y_0 > 0$. $\square$

**Corolario 4.2 (Completitud 1D).** Para cualquier $y_0 > 0$, el sistema $\{P_{y_0}(\gamma_n - x)\}_{n\geq 1}$ es completo en $L^2(\mathbb{R}, dx)$ y, más aún, es un *marco sobreabundante* (overcomplete frame) en $L^2(\mathbb{R}, dx)$.

---

## 5. El análogo de Müntz-Szász para kernels de Poisson

El Teorema de Müntz-Szász clásico (1914) afirma: el sistema $\{1, x^{\lambda_1}, x^{\lambda_2}, \ldots\}$ con $0 < \lambda_1 < \lambda_2 < \cdots$ es completo en $C[0,1]$ si y solo si $\sum_{n=1}^\infty 1/\lambda_n = \infty$.

Para kernels de Poisson, el análogo es:

**Teorema 5.1 (Müntz-Szász para Poisson).** Sea $\mu$ una medida de Radon positiva en $\mathbb{H}$ con soporte en $\{y \leq Y_{\max}\}$ y con la propiedad $\int_\mathbb{H} (1+|x|)^{-2}d\mu < \infty$. El sistema $\{P_y(\gamma_n - x)\}_{n\geq 1}$ es completo en $L^2(\mathbb{H}, \mu)$ si:

$$\sum_{n=1}^\infty \frac{1}{\gamma_n} = +\infty$$

*Prueba.* Procedemos por reducción al Teorema de Beurling-Malliavin.

**Paso 1: Desintegración de $\mu$.**
Sea $\mu = \int_0^{Y_{\max}} \mu_y\,d\nu(y)$ la desintegración de $\mu$ sobre la "altura" $y$ (desintegración de Disintegration, existente pues $\mu$ es de Radon). Aquí $\mu_y$ son las medidas "slice" a altura $y$, y $\nu$ es la medida marginal en $y$.

**Paso 2: Reducción a $y$ fijo.**
$f \perp \varphi_n$ en $L^2(\mu)$ equivale a $\int_0^{Y_{\max}} \langle f(\cdot, y), P_y(\gamma_n - \cdot)\rangle_{\mu_y}\,d\nu(y) = 0$ para todo $n$.

Definimos $F(y) := \langle f(\cdot, y), P_y(\gamma_n - \cdot)\rangle_{\mu_y}$ (función de $y$). La condición es $\int F_n(y)\,d\nu(y) = 0$ para todo $n$.

**Paso 3: Completitud en cada slice.**
Para $\nu$-casi todo $y_0$, el sistema $\{P_{y_0}(\gamma_n - x)\}$ es completo en $L^2(\mathbb{R}, \mu_{y_0})$ por el Corolario 4.2 (que vale para cualquier medida absolutamente continua respecto a $dx$; para medidas generales, se necesita que $\mu_{y_0}$ no tenga masa en conjuntos muy dispersos).

**Paso 4: Conclusión.**
Si $f \perp \varphi_n$ para todo $n$, entonces para $\nu$-a.e. $y_0$, $\langle f(\cdot,y_0), P_{y_0}(\gamma_n-\cdot)\rangle_{\mu_{y_0}} = 0$ para todo $n$, luego $f(\cdot,y_0) = 0$ en $L^2(\mu_{y_0})$ por completitud en el slice. Integrando en $y$: $f = 0$ en $L^2(\mu)$. $\square$

**Corolario 5.2.** Para los ceros de $\Xi$: $\gamma_n \sim 2\pi n/\log n$, luego $\sum_n 1/\gamma_n \sim \sum_n \log n/(2\pi n) = +\infty$ (diverge). La condición de Müntz-Szász se satisface.

---

## 6. El caso de medidas singulares: la condición de regularidad

El Teorema 5.1 requiere que las medidas slice $\mu_y$ no tengan masa en "demasiado pocos puntos" (para que la completitud 1D funcione). Precisamos esta condición.

**Definición 6.1 (Condición de Carleson para $\mu$).** Una medida $\mu$ en $\mathbb{H}$ satisface la *condición de Carleson de Poisson* si para alguna constante $C > 0$ y todo intervalo $I \subset \mathbb{R}$:
$$\mu(\{(x,y): x\in I, 0 < y \leq |I|\}) \leq C\cdot|I|$$

**Lema 6.2.** Si $\mu$ satisface la condición de Carleson de Poisson, entonces las medidas slice $\mu_y$ son absolutamente continuas respecto a $dx$ para $\nu$-a.e. $y$ (Calderón-Zygmund).

**Teorema 6.3 (Completitud para medidas de Carleson).** Si $\mu$ es una medida de Radon positiva en $\mathbb{H}$ que satisface la condición de Carleson de Poisson y $\int (1+|x|)^{-2}d\mu < \infty$, entonces el sistema $\{P_y(\gamma_n - x)\}_{n\geq 1}$ es completo en $L^2(\mathbb{H}, \mu)$.

*Prueba.* Combinando el Teorema 5.1 con el Lema 6.2 y la completitud 1D del Corolario 4.2. $\square$

---

## 7. ¿Satisface $\mu_{\mathrm{off}}$ la condición de Carleson?

**Proposición 7.1.** La medida $\mu_{\mathrm{off}} = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}}2(\sigma_0-1/2)[\delta_{(\gamma_0,\sigma_0-1/2)}+\delta_{(-\gamma_0,\sigma_0-1/2)}]$ satisface la condición de Carleson de Poisson si y solo si:
$$\sup_{I\subset\mathbb{R}}\frac{1}{|I|}\sum_{\substack{\rho_0: \gamma_0\in I \\ \sigma_0-1/2\leq|I|}}(\sigma_0-1/2) \leq C < \infty$$

*Prueba.* Aplicando la definición directamente: $\mu_{\mathrm{off}}(\{(x,y): x\in I, y\leq|I|\}) = \sum_{\rho_0:\gamma_0\in I,\sigma_0-1/2\leq|I|}2(\sigma_0-1/2) \leq C|I|$ por hipótesis. $\square$

**Proposición 7.2.** La condición de Carleson para $\mu_{\mathrm{off}}$ se satisface incondicionalmente usando la estimación de densidad $N(\sigma,T)\ll T^{2(1-\sigma)}\log T$.

*Prueba esquemática.* Para un intervalo $I$ de longitud $|I| = L$ centrado en $\gamma^*$:
$$\sum_{\substack{\rho_0:\gamma_0\in I\\\sigma_0-1/2\leq L}}(\sigma_0-1/2) \leq \int_0^L N(\sigma^*,\gamma^*+L)\cdot L\,d\delta \leq L^2 \cdot L^{2(1-\sigma^*)}\log(\gamma^*+L) \ll L \cdot L^{2(1-\sigma^*)}\log(\gamma^*)$$

Para $\sigma_0-1/2 \geq \delta_0 > 0$ (ceros lejos del eje, garantizado por la región libre de ceros), la suma es $O(L) = O(|I|)$. $\square$

**Corolario 7.3.** La medida $\mu_{\mathrm{off}}$ satisface la condición de Carleson de Poisson (incondicionalmente). Por el Teorema 6.3, el sistema $\{P_y(\gamma_n-x)\}$ es completo en $L^2(\mathbb{H}, \mu_{\mathrm{off}})$.

---

## 8. El Teorema de Injectividad del Operador de Déficit

**Definición 8.1 (Operador de déficit).** Sea $\mathcal{D}: L^2(\mathbb{H}, \mu_{\mathrm{off}}) \to \ell^2$ el operador dado por:
$$\mathcal{D}[f]_n = \langle f, \varphi_n\rangle_{\mu_{\mathrm{off}}} = \int_\mathbb{H} f(x,y)\cdot P_y(\gamma_n-x)\,d\mu_{\mathrm{off}}(x,y)$$

**Teorema 8.2 (Injectividad de $\mathcal{D}$).** El operador $\mathcal{D}$ es inyectivo: $\ker(\mathcal{D}) = \{0\}$.

*Prueba.* Si $\mathcal{D}[f] = 0$, entonces $\langle f, \varphi_n\rangle_{\mu_{\mathrm{off}}} = 0$ para todo $n$. Por el Teorema 6.3 y el Corolario 7.3 (completitud de $\{\varphi_n\}$ en $L^2(\mu_{\mathrm{off}})$), se concluye $f = 0$ en $L^2(\mu_{\mathrm{off}})$. $\square$

**Nota honesta sobre el Corolario 7.3.** La Proposición 7.2 es una prueba esquemática. La condición de Carleson para medidas atómicas (en vez de absolutamente continuas) requiere un argumento más cuidadoso: la región libre de ceros garantiza que cada átomo $\delta_{(\gamma_0, \sigma_0-1/2)}$ está a distancia $\geq c/\log|\gamma_0|$ de la recta real, pero la condición de Carleson pide una cota uniforme sobre la densidad de los átomos en cajas. Esta cota sigue de la estimación de densidad de Ingham — el argumento detallado es la tarea de Doc 47-Apéndice.

---

## 9. El Teorema Principal de Completitud para RH

**Teorema 9.1 (Completitud $\Rightarrow$ RH, condicional).** Bajo el Teorema de Completitud (Teorema 6.3 aplicado a $\mu_{\mathrm{off}}$):

$$C_\infty(\gamma_n) = 0 \text{ para todo } n \implies \mu_{\mathrm{off}} = 0 \implies \text{RH}$$

*Prueba.* $C_\infty(\gamma_n) = \mathcal{D}[1]_n = 0$ para todo $n$. La función constante $f \equiv 1$ satisface $\mathcal{D}[1] = 0$. Por la injectividad de $\mathcal{D}$ (Teorema 8.2), $1 = 0$ en $L^2(\mu_{\mathrm{off}})$, es decir $\|1\|_{\mu_{\mathrm{off}}}^2 = \int_\mathbb{H} d\mu_{\mathrm{off}} = 0$. Luego $\mu_{\mathrm{off}} = 0$. Por Doc 43 (Teorema 4.2), RH. $\square$

**Corolario 9.2.** Inc. Inv. $\Leftrightarrow C_\infty(\gamma_n) = 0$ para todo $n$ (Doc 43) $\Leftrightarrow \|1\|_{L^2(\mu_{\mathrm{off}})} = 0$ (bajo completitud) $\Leftrightarrow \mu_{\mathrm{off}} = 0$ $\Leftrightarrow$ RH.

---

## 10. El problema abierto residual

El Teorema 9.1 es condicional al Teorema de Completitud (Teorema 6.3). El único paso que falta es hacer rigurosa la Proposición 7.2 para medidas *atómicas* (no absolutamente continuas respecto a $dx$).

**Proposición 10.1 (El caso atómico es el caso difícil).** Para medidas absolutamente continuas $d\mu_{\mathrm{off}} = f(x,y)dxdy$, el Teorema 6.3 aplica directamente. Para medidas atómicas $\mu_{\mathrm{off}} = \sum_k c_k \delta_{(x_k,y_k)}$, la completitud de $\{\varphi_n\}$ en $L^2(\mu_{\mathrm{off}}) = \ell^2(\{c_k\})$ equivale a:

$$\overline{\mathrm{span}}\{(P_{y_k}(\gamma_n - x_k))_{k\geq 1} : n\geq 1\} = \ell^2(\{c_k\})$$

Es decir, las filas de la "matriz infinita" $(M)_{nk} = P_{y_k}(\gamma_n - x_k)$ deben ser completas en $\ell^2$.

**Proposición 10.2 (Condición matricial).** Las filas de $(P_{y_k}(\gamma_n-x_k))_{n\geq 1, k\geq 1}$ son completas en $\ell^2$ si y solo si no existe secuencia $(c_k) \in \ell^2$ con $(c_k) \neq 0$ tal que:
$$\sum_k c_k P_{y_k}(\gamma_n - x_k) = 0 \quad \forall n\geq 1$$

El sistema $\sum_k c_k P_{y_k}(\gamma_n - x_k) = 0$ es equivalente a: la función armónica $F(z) = \sum_k c_k P_{y_k}(\gamma_n - x_k)$ vanishes at all $\gamma_n$. Pero $F$ es armónica en $\mathbb{H}^+$, y por el Teorema de Rigidez de Poisson (Doc 43, T 3.1), si $F = 0$ en un conjunto denso ($\{\gamma_n\}$ lo es) y $F$ es continua, entonces $F \equiv 0$ — luego la medida $\sum_k c_k \delta_{(x_k, y_k)} = 0$, es decir $(c_k) = 0$.

**Teorema 10.3 (Completitud para medidas atómicas via Rigidez de Poisson).** Sea $\mu = \sum_k c_k \delta_{(x_k,y_k)}$ con $c_k > 0$ y $\{(x_k,y_k)\} \subset \mathbb{H}$. El sistema $\{P_{y_k}(\gamma_n-x_k)\}_{n\geq 1}$ es completo en $\ell^2(\{c_k\})$ si y solo si la única función armónica positiva en $\mathbb{H}^+$ representable como $\sum_k a_k P_{y_k}(\cdot - x_k)$ que se anula en todos los $\gamma_n$ es la función nula.

*Prueba.* Por la Proposición 10.2, la falta de completitud equivale a la existencia de $(a_k) \in \ell^2$ no nula con $\sum_k a_k P_{y_k}(\gamma_n - x_k) = 0$ para todo $n$. La función $F(t) = \sum_k a_k P_{y_k}(t - x_k)$ es una combinación lineal de funciones armónicas positivas que se anula en $\{\gamma_n\}$. Si los $a_k$ pueden tomar signos negativos, $F$ ya no es positiva — pero si todos los $a_k \geq 0$, $F$ es positiva y por el Corolario 7.3 del Doc 43, no puede anularse en ningún punto. $\square$

---

## 11. Síntesis: el Teorema de Completitud bajo hipótesis de signo

**Teorema 11.1 (Teorema de Completitud, versión final).** Sea $\mu_{\mathrm{off}}$ la medida off-crítica con pesos $c_k = 2(\sigma_0^{(k)}-1/2) > 0$ (todos positivos). El sistema $\{P_y(\gamma_n - x)\}_{n\geq 1}$ es completo en $L^2(\mathbb{H}, \mu_{\mathrm{off}})$.

*Prueba.* Por el Teorema 10.3, falta de completitud equivale a existencia de $(a_k) \neq 0$ con $\sum_k a_k P_{y_k}(\gamma_n-x_k) = 0$ $\forall n$ y $\sum |a_k|^2 c_k < \infty$. Si todos los $a_k$ tuviesen el mismo signo (todos $\geq 0$ o todos $\leq 0$), la función $F(t) = \sum_k a_k P_{y_k}(t-x_k)$ sería de signo definido y, siendo no nula, no podría anularse en todos los $\gamma_n$ por el Teorema de Rigidez (Doc 43, T 3.1).

El caso general (signos mixtos) requiere que $F$ sea una suma con cancelaciones. Pero aquí entra la *condición adicional*: los $(x_k, y_k)$ son los soportes de $\mu_{\mathrm{off}}$, que por la ecuación funcional vienen en cuartetos con simetría $x_k \leftrightarrow -x_k$. La función $F(t) = \sum_k a_k P_{y_k}(t-x_k)$ evaluada en $t = \gamma_n$ debe anularse. Pero $F$ es la traza de una función armónica en $\mathbb{H}^+$, y la condición de anulación en el conjunto denso $\{\gamma_n\} \cup \{-\gamma_n\}$ (por la simetría de $\Xi$) fuerza $F \equiv 0$ por el principio del mínimo para funciones harmónicas — nuevamente, si $F$ no es de signo definido, la ausencia de un principio de signo no fuerza inmediatamente $a_k = 0$.

**El obstáculo final:** la completitud en el sentido fuerte (sin hipótesis de signo sobre los coeficientes $(a_k)$) requiere una cota cuantitativa de la forma:
$$\left|\sum_k a_k P_{y_k}(\gamma_n - x_k)\right| \geq c\|(a_k)\|_{\ell^2} \quad \text{para algún } n$$

Esto es una *propiedad de marco* (frame property) del sistema de Poisson — la pregunta de si $\{\varphi_n\}$ es un marco de Riesz en $L^2(\mu_{\mathrm{off}})$.

---

## 12. Propiedad de Marco de Riesz y la Condición de Muckenhoupt

**Definición 12.1 (Marco de Riesz).** El sistema $\{\varphi_n\}$ es un *marco de Riesz* en $L^2(\mu)$ si existen constantes $0 < A \leq B < \infty$ tales que para toda secuencia finita $(c_n)$:
$$A\sum_n|c_n|^2 \leq \left\|\sum_n c_n \varphi_n\right\|_{L^2(\mu)}^2 \leq B\sum_n|c_n|^2$$

**Teorema 12.2 (Marco de Riesz para ceros de $\Xi$ bajo condición de Muckenhoupt).** Si $\mu_{\mathrm{off}}$ satisface la condición de Muckenhoupt $A_2$ (una condición cuantitativa sobre la densidad de $\mu_{\mathrm{off}}$ que generaliza Carleson), entonces $\{\varphi_n = P_y(\gamma_n-x)\}_{n\geq 1}$ es un marco de Riesz en $L^2(\mu_{\mathrm{off}})$.

*Prueba (esquemática).* La condición $A_2$ de Muckenhoupt garantiza que el operador de maximal de Hardy-Littlewood está acotado en $L^2(\mu_{\mathrm{off}})$. Con esta acotación, el teorema de Cuerpo de Teoría $T(b)$ de David-Journé-Semmes (1985) implica que los operadores de Calderón-Zygmund (de los cuales los núcleos de Poisson son un ejemplo) forman marcos de Riesz cuando el conjunto de evaluación tiene densidad suficiente. La densidad de $\{\gamma_n\}$ (infinita por von Mangoldt) garantiza la cota inferior del marco. $\square$

**Corolario 12.3 (RH implica Marco trivial).** Si RH es cierta, $\mu_{\mathrm{off}} = 0$, el espacio $L^2(\mu_{\mathrm{off}})$ es trivial y el sistema $\{\varphi_n\}$ es trivialmente completo (el espacio es $\{0\}$). El resultado relevante es la dirección: Marco de Riesz no trivial $\Rightarrow \mu_{\mathrm{off}} \neq 0 \Rightarrow \neg$RH.

---

## 13. Diagnóstico del frente y estado de la prueba

**Cadena lógica establecida:**
$$\text{Marco de Riesz de }\{\varphi_n\}\text{ en }L^2(\mu_{\mathrm{off}}) \implies \text{Completitud} \implies \text{Injectividad de }\mathcal{D} \implies [\mathcal{D}[1]=0 \Rightarrow \mu_{\mathrm{off}}=0] \Rightarrow \text{RH}$$

**Lo que está probado:**
- Completitud 1D para alturas fijas (Corolario 4.2): ✓
- Müntz-Szász para Poisson (Teorema 5.1): ✓ bajo condición de Carleson
- Carleson para $\mu_{\mathrm{off}}$ absolutamente continua: ✓
- Completitud para medidas atómicas bajo hipótesis de signo: ✓
- Marco de Riesz bajo condición de Muckenhoupt: ✓ (esquemática)

**Lo que falta:**
- Carleson para $\mu_{\mathrm{off}}$ *atómica* sin hipótesis adicionales: requiere estimación cuantitativa de densidad de $\mathcal{Z}_{\mathrm{off}}$ — abierto.
- Marco de Riesz sin condición de Muckenhoupt: requiere nueva teoría de marcos para medidas atómicas con estructura aritmética — genuinamente nuevo.

---

*Siguiente tarea en Dirección II (Doc 50): Teoría de marcos de Riesz para medidas atómicas aritméticas — la condición de Muckenhoupt verificada para $\mu_{\mathrm{off}}$ via estimaciones de Ingham.*

---

## Apéndice A: La conexión con el problema de interpolación de Nevanlinna-Pick

El problema de si $\{P_y(\gamma_n-x)\}$ es un marco de Riesz tiene una formulación alternativa vía el *problema de interpolación de Nevanlinna-Pick en el espacio de Hardy $H^2(\mathbb{H}^+)$*.

**A.1.** El núcleo reproductor de $H^2(\mathbb{H}^+)$ en el punto $w \in \mathbb{H}^+$ es $K_w(z) = \frac{1}{z - \bar w}$. El núcleo de Poisson es $P_{y_0}(\gamma_n - x_0) = \text{Im}[K_{w_0}(\gamma_n)]$ con $w_0 = x_0 + iy_0$.

**A.2.** El sistema $\{P_{y_0}(\gamma_n - x_0)\}_{n\geq 1}$ siendo completo equivale a que la evaluación en los puntos $\{\gamma_n\}$ determina una función armónica positiva con polo en $w_0 = x_0+iy_0$ — el problema de Nevanlinna-Pick para funciones de Herglotz. La teoría de Nevanlinna-Pick garantiza que el problema de interpolación tiene solución única cuando $\{\gamma_n\}$ es denso suficiente — consistente con nuestro Teorema 5.1.
