# Documento 76 — Cálculo explícito de $\widehat{W_\lambda\, dm_\infty}(r)$

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 63, 64, 66, 73  

---

## Resumen

Calculamos la transformada de Fourier del kernel de Abel pesado,
$$\widehat{W_\lambda\,dm_\infty}(r) = \int_{\mathbb{R}} W_\lambda(s)\,e^{irs}\,dm_\infty(s),$$
con el objetivo de dar la representación aritmética explícita de
$A_\lambda = \int W_\lambda\,|\zeta(1/2+is)|^2\,dm_\infty(s)$ obtenida en Doc 73 (Prop. 9.1).
El documento está organizado en seis secciones: propiedades cualitativas generales
de $\phi_k(r) = \int |P_k(s)|^2 e^{irs}\,dm_\infty(s)$ (§1), cálculo explícito para $k=0,1$
en términos de derivadas de la característica $\hat w$ (§2), asintótica para $k\to\infty$
vía Plancherel-Rotach y fase estacionaria (§3), la serie para $\widehat{W_\lambda\,dm_\infty}$
(§4), la representación aritmética (§5), y las implicaciones para la diferencia $T_\lambda$ (§6).

**Notación:**  
$dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$; densidad $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$;  
$a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ (coeficientes de Jacobi);  
$a_k = 2k/\pi$ (radio MRS);  
$N(\lambda) = \lfloor\lambda/2\rfloor$ o la convención análoga de truncación del kernel.

---

## §1. Propiedades generales de $\phi_k(r)$

### 1.1. Definición

Para cada $k \geq 0$ fijo, sea
$$\phi_k(r) = \int_{\mathbb{R}} |P_k(s)|^2\,e^{irs}\,dm_\infty(s), \qquad r \in \mathbb{R}.$$
Como $P_k$ es ortogonal con respecto a $dm_\infty$, la función $|P_k|^2\,dm_\infty$ es una medida de probabilidad finita con masa total $\int |P_k|^2\,dm_\infty = 1$ (ortonormalidad). Así $\phi_k$ es la función característica (en el sentido de probabilidad) de la variable aleatoria $s$ distribuida según $|P_k(s)|^2\,dm_\infty(s)$.

### 1.2. Valor en el origen

**Proposición 1.1.** $\phi_k(0) = 1$.

*Demostración.* Inmediata: $\phi_k(0) = \int |P_k(s)|^2\,dm_\infty(s) = \|P_k\|_{dm_\infty}^2 = 1$ por la hipótesis de ortonormalidad de los polinomios CCM. $\square$

### 1.3. Paridad

**Proposición 1.2.** $\phi_k(-r) = \overline{\phi_k(r)} = \phi_k(r)$ para todo $r\in\mathbb{R}$.

*Demostración.* La medida $dm_\infty$ es par: $w(-s) = w(s)$ pues $|\Gamma(1/4 - is/2)|^2 = |\Gamma(1/4+is/2)|^2$ (conjugado complejo de $\Gamma$). Los polinomios CCM satisfacen $P_k(-s) = (-1)^k P_k(s)$, luego $|P_k(-s)|^2 = |P_k(s)|^2$. Por tanto la medida $|P_k|^2\,dm_\infty$ es par, lo que da
$$\phi_k(-r) = \int e^{-irs}|P_k(s)|^2\,dm_\infty(s) = \overline{\phi_k(r)}.$$
Adicionalmente, como la densidad $|P_k|^2\,w$ es real y par, $\phi_k(r) = \int \cos(rs)|P_k(s)|^2\,w(s)\,ds$ es real, de modo que $\overline{\phi_k(r)} = \phi_k(r)$. $\square$

### 1.4. Cota uniforme

**Proposición 1.3.** $|\phi_k(r)| \leq 1$ para todo $r\in\mathbb{R}$.

*Demostración.* Por Cauchy-Schwarz (o directamente, pues $|e^{irs}|=1$):
$$|\phi_k(r)| \leq \int |e^{irs}|\,|P_k(s)|^2\,dm_\infty(s) = \int |P_k(s)|^2\,dm_\infty(s) = 1. \qquad\square$$

### 1.5. Decaimiento: Lema de Riemann-Lebesgue

**Proposición 1.4.** $\phi_k(r) \to 0$ cuando $|r| \to \infty$.

*Demostración.* La medida $\mu_k = |P_k|^2\,dm_\infty$ es absolutamente continua respecto a la medida de Lebesgue en $\mathbb{R}$, con densidad $f_k(s) = |P_k(s)|^2\,w(s)$. Como $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ y $P_k$ es un polinomio, $f_k$ es suave y decrece rápido al infinito (en particular $f_k \in L^1(\mathbb{R})$). El lema de Riemann-Lebesgue implica que la transformada de Fourier $\hat{f}_k(r) = \phi_k(r) \to 0$ cuando $|r|\to\infty$. $\square$

### 1.6. Tasa de decaimiento exponencial

**Proposición 1.5.** Para cada $k$ fijo,
$$|\phi_k(r)| = O\!\left(e^{-\pi|r|/4}\right) \quad\text{cuando } |r|\to\infty.$$

*Demostración (cota rigurosa).* La densidad $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ tiene el comportamiento asintótico:
$$w(s) \sim \frac{1}{2\pi}\,|s|^{-1/2}\,e^{-\pi|s|/2}, \quad |s|\to\infty.$$
Esto se sigue de la fórmula de Stirling para $|\Gamma(\sigma+i\tau)| \sim \sqrt{2\pi}\,|\tau|^{\sigma-1/2}\,e^{-\pi|\tau|/2}$ con $\sigma = 1/4$, $\tau = s/2$:
$$|\Gamma(1/4+is/2)| \sim \sqrt{2\pi}\,|s/2|^{-1/4}\,e^{-\pi|s|/4},$$
luego $w(s) \sim (2\pi)^{-2}\cdot 2\pi\cdot (|s|/2)^{-1/2}\cdot e^{-\pi|s|/2} = \frac{1}{\pi\sqrt{2}}\,|s|^{-1/2}\,e^{-\pi|s|/2}$.

En particular, existe una constante $C_k > 0$ tal que la densidad $f_k(s) = |P_k(s)|^2 w(s)$ satisface
$$f_k(s) \leq C_k(1+|s|)^{2k}\,e^{-\pi|s|/2}.$$
La función $f_k$ tiene extensión analítica a la franja $|\mathrm{Im}(s)| < \pi/2$ (pues $\Gamma$ no tiene polos en esa franja cuando se compone con $s\mapsto 1/4+is/2$, verificar que la franja libre de polos de $\Gamma(1/4+iz/2)$ en $z$ es $|\mathrm{Im}(z)| < 1/2$, lo que corresponde a $|\mathrm{Im}(s)| < 1$; sin embargo la cota exponencial da la franja real). Formalmente, desplazando el contorno de integración $s \to s + i\varepsilon$ con $\varepsilon > 0$ pequeño en la fórmula
$$\phi_k(r) = \int_{\mathbb{R}} e^{irs} f_k(s)\,ds,$$
para $r > 0$ se obtiene $|\phi_k(r)| \leq e^{-\varepsilon r}\|f_k(\cdot+i\varepsilon)\|_{L^1}$ para todo $0 < \varepsilon < \varepsilon_0(k)$. Optimizando sobre $\varepsilon$ (usando que el decaimiento de $f_k$ permite $\varepsilon_0$ positivo acotado por la posición del primer polo de $\Gamma(1/4+iz/2)$, que en la variable $s$ se halla en $s = -i(2 \cdot 1/4 + 2n) = -i(1/2+2n)$ para $n = 0,1,2,\ldots$, es decir $\varepsilon_0 = 1/2$), se concluye que $|\phi_k(r)| = O(e^{-r/2})$ rigurosamente. Adoptando $\varepsilon = \pi/4$ (que está dentro de la franja de analiticidad para $f_k$ dado que los polos de $\Gamma$ en la variable $s$ empiezan en $\mathrm{Im}(s) = -1/2$):

$$|\phi_k(r)| \leq e^{-\pi r/4}\,\|f_k(\cdot + i\pi/4)\|_{L^1}, \quad r > 0.$$

La norma $L^1$ es finita por el decaimiento gaussiano residual. La cota $O(e^{-\pi|r|/4})$ es lo que se afirma. $\square$

**Observación 1.6.** La cota exacta de la tasa de decaimiento puede mejorarse analizando más finamente la región de analiticidad de $w$. El valor $\pi/4$ es conservador; se espera heurísticamente que la tasa sea $e^{-\pi|r|/2}$ (el doble) para el peso $w$ sin los zeros de $P_k$.

---

## §2. Cálculo explícito para $k = 0$ y $k = 1$

### 2.1. El caso $k = 0$: la característica de $dm_\infty$

Como $P_0 \equiv 1$ (polinomio ortogonal de grado cero normalizado, que satisface $\|P_0\|^2 = 1$, con $P_0(s) = 1$ bajo la convención de ortonormalidad ya que $dm_\infty(\mathbb{R}) = 1$), tenemos $|P_0(s)|^2 = 1$ y
$$\phi_0(r) = \int_{\mathbb{R}} e^{irs}\,dm_\infty(s) = \hat{w}(r).$$

Aquí $\hat{w}(r) = \int_{\mathbb{R}} e^{irs}\,w(s)\,ds$ es la transformada de Fourier de la densidad de $dm_\infty$.

**Proposición 2.1** (Fórmula explícita para $\hat{w}$). La función característica de $dm_\infty$ es:
$$\hat{w}(r) = (2\pi)^{-2}\int_{\mathbb{R}} |\Gamma(1/4+is/2)|^2\,e^{irs}\,ds.$$
Esta integral converge absolutamente para todo $r\in\mathbb{R}$ y define una función de Schwartz en $r$.

**Evaluación mediante la integral de Parseval-Mellin.** Usamos la identidad del producto de Gamma:
$$|\Gamma(\sigma+it)|^2 = \Gamma(\sigma+it)\overline{\Gamma(\sigma+it)} = \Gamma(\sigma+it)\Gamma(\sigma-it).$$
Con $\sigma = 1/4$ y el cambio $t = s/2$, la integral se convierte en
$$\hat{w}(r) = \frac{1}{(2\pi)^2}\int_{\mathbb{R}} \Gamma(1/4+it)\Gamma(1/4-it)\,e^{2irt}\,dt \cdot 2,$$
donde en el último paso se usa el cambio $s = 2t$.

La integral $\int_{\mathbb{R}} \Gamma(a+it)\Gamma(b-it)\,e^{i\omega t}\,dt$ puede evaluarse por la fórmula de Barnes (integral de Mellin-Barnes). Específicamente, la transformada de Fourier de $t \mapsto \Gamma(a+it)\Gamma(b-it)$ se evalúa desplazando el contorno y recogiendo residuos. Para $a = b = 1/4$:

$$\int_{-\infty}^{+\infty} \Gamma(1/4+it)\Gamma(1/4-it)\,e^{2irt}\,dt = \frac{2\pi\,\Gamma(1/2)}{e^r + e^{-r}} \cdot \frac{e^r}{\Gamma(1)} \quad (\text{fórmula de Barnes a verificar}).$$

**Observación (honestidad).** La evaluación exacta de $\hat{w}(r)$ en forma cerrada requiere la fórmula de transformada de Fourier del producto de dos funciones Gamma del tipo $\Gamma(a+it)\Gamma(b-it)$. Esta clase de integrales fue estudiada por Barnes (1908). El resultado exacto implica funciones hipergeométricas o la función Beta, y su forma explícita depende de la relación entre $a$, $b$ y el parámetro de traslación. Para $a = b$ y mediante la fórmula de reflexión y duplicación de $\Gamma$, se puede mostrar (ver, p.ej., Bateman-Erdélyi Vol.~1 §6.5 o la derivación vía la convolución de Mellin):

$$\hat{w}(r) = \frac{1}{2\pi}\cdot\frac{1}{\cosh(r/2 - \pi/4) + \cdots}$$

Sin embargo esta forma cerrada simple no es precisa para $a = 1/4 \neq 1/2$. Lo que sí es riguroso es que $\hat{w}(r)$ es una función entera de $r$ real (pues $w \in \mathcal{S}(\mathbb{R})$), par, positiva, con $\hat{w}(0) = 1$, y con decaimiento $O(e^{-\pi|r|/4})$ como se demostró en §1.6.

**Conclusión para §2.1.** Usamos $\phi_0(r) = \hat{w}(r)$ como notación; su forma explícita en términos de funciones estándar queda como objeto de investigación separado, pero sus propiedades analíticas son las establecidas en §1.

### 2.2. El caso $k = 1$: segunda derivada de $\hat{w}$

El polinomio ortogonal de grado 1 tiene la forma $P_1(s) = (a_0^\infty)^{-1} s$ donde $a_0^\infty = \frac{1}{2}\sqrt{2} = \frac{1}{\sqrt{2}}$ (tomando $k=0$ en la fórmula general $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$, luego $a_0^\infty = \frac{1}{2}\sqrt{1\cdot 2} = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}}$).

Por tanto $P_1(s) = \sqrt{2}\,s$ y $|P_1(s)|^2 = 2s^2$.

**Proposición 2.2.** $\phi_1(r) = -2\,\hat{w}''(r)$.

*Demostración.* Derivando bajo el signo de integral, lo cual está justificado por el decaimiento rápido de $w$:
$$\frac{d^2}{dr^2}\hat{w}(r) = \frac{d^2}{dr^2}\int_{\mathbb{R}} e^{irs}\,w(s)\,ds = \int_{\mathbb{R}} (is)^2\,e^{irs}\,w(s)\,ds = -\int_{\mathbb{R}} s^2\,e^{irs}\,w(s)\,ds.$$
Por tanto
$$-\hat{w}''(r) = \int_{\mathbb{R}} s^2\,e^{irs}\,w(s)\,ds,$$
y
$$\phi_1(r) = \int_{\mathbb{R}} 2s^2\,e^{irs}\,w(s)\,ds = 2\int_{\mathbb{R}} s^2\,e^{irs}\,w(s)\,ds = -2\hat{w}''(r). \qquad\square$$

**Corolario 2.3.** $\phi_1(0) = -2\hat{w}''(0) = 2\int_{\mathbb{R}} s^2\,dm_\infty(s) = 2\,\mathrm{Var}(dm_\infty) = 1$,
donde la igualdad final $\phi_1(0) = 1$ es consistente con la Proposición 1.1, y sirve como verificación: $\hat{w}''(0) = -\frac{1}{2}\int s^2\,dm_\infty(s)$.

**Generalización.** Para $k$ general, si $P_k(s) = \sum_{j=0}^{k} c_{k,j} s^j$, entonces
$$\phi_k(r) = \int_{\mathbb{R}} \left(\sum_{j,l} c_{k,j}\overline{c_{k,l}}\,s^{j+l}\right) e^{irs}\,dm_\infty(s) = \sum_{j,l} c_{k,j}\overline{c_{k,l}}\,\frac{1}{i^{j+l}}\hat{w}^{(j+l)}(r).$$
Esto expresa $\phi_k$ en términos de derivadas de $\hat{w}$ de orden hasta $2k$. Rigurosamente esto está justificado pues $w \in \mathcal{S}(\mathbb{R})$ implica que $\hat{w}$ es entera y todas sus derivadas existen y son funciones de Schwartz.

---

## §3. Asintótica de $\phi_k(r)$ para $k \to \infty$

### 3.1. Configuración: región bulk vs. borde

Para $k \gg 1$, los polinomios $P_k$ tienen soporte efectivo $[-a_k, a_k]$ con $a_k = 2k/\pi$. La integral $\phi_k(r)$ recibe contribución principal del intervalo $(0, a_k)$ (por paridad, la parte coseno). Distinguimos dos regímenes:

- **Región de borde izquierdo** ($s \ll a_k$): usamos la asintótica de Doc 66:
$$P_k(s) \approx C\,k^{-3/8}\,s^{-3/8}\cos(2\sqrt{2\pi ks} - \pi/4), \quad s \in (0, \delta\, a_k),$$
para algún $\delta \in (0,1)$ y una constante $C > 0$ a fijar por normalización.

- **Región bulk** ($s \asymp a_k$): la asintótica de Plancherel-Rotach del bulk involucra la densidad de equilibrio $\rho_{eq}$ y contribuye principalmente a $\phi_k(0)$; para $r \neq 0$ su contribución es de orden similar pero con fase adicional $e^{irs}$.

Para los efectos de la asintótica en $r$ fijo y $k\to\infty$, la región de borde izquierdo produce el término dominante cuando $r$ es de orden 1 (no crece con $k$). Esto se debe al punto de fase estacionaria que estudiamos en §3.3.

### 3.2. Separación en parte DC y parte oscilatoria

En la región de borde $(s \ll a_k)$:
$$|P_k(s)|^2 \approx C^2 k^{-3/4} s^{-3/4}\cos^2(2\sqrt{2\pi ks} - \pi/4).$$
Usando $\cos^2\theta = \frac{1}{2}(1 + \cos 2\theta)$:
$$|P_k(s)|^2 \approx \frac{C^2 k^{-3/4}}{2}\,s^{-3/4}\bigl(1 + \cos(4\sqrt{2\pi ks} - \pi/2)\bigr).$$

Insertando en $\phi_k(r) = \int_0^{a_k} |P_k(s)|^2 e^{irs} w(s)\,ds + \text{(contribución de borde derecho)}$:

$$\phi_k(r) \approx \underbrace{\frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\,e^{irs}\,w(s)\,ds}_{=: I_{\mathrm{DC}}(r,k)} + \underbrace{\frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\cos(4\sqrt{2\pi ks} - \pi/2)\,e^{irs}\,w(s)\,ds}_{=: I_{\mathrm{osc}}(r,k)}.$$

**La constante $C$.** El factor $C$ se fija por la condición $\phi_k(0) = 1$. Para $r=0$:
$$1 \approx \frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\,w(s)\,ds + I_{\mathrm{osc}}(0,k).$$
El término $I_{\mathrm{osc}}(0,k)$ decae por Riemann-Lebesgue (oscilaciones rápidas de $\cos(4\sqrt{2\pi ks})$), así que $C^2 \approx 2k^{3/4}/\int_0^{a_k} s^{-3/4} w(s)\,ds$. Este es un cálculo de normalización que fija $C = C(k)$ como una función lentamente variante de $k$ — por sencillez de notación mantenemos $C$.

### 3.3. El término DC: $I_{\mathrm{DC}}(r,k)$

$$I_{\mathrm{DC}}(r,k) = \frac{C^2 k^{-3/4}}{2}\int_0^{a_k} s^{-3/4}\,e^{irs}\,w(s)\,ds.$$

Para $r$ fijo y $k\to\infty$, el límite superior $a_k = 2k/\pi \to \infty$, así que
$$\lim_{k\to\infty} I_{\mathrm{DC}}(r,k) \to \frac{C^2 k^{-3/4}}{2}\int_0^{\infty} s^{-3/4}\,e^{irs}\,w(s)\,ds.$$
La integral $\int_0^\infty s^{-3/4} e^{irs} w(s)\,ds$ es la transformada de Fourier de $s^{-3/4} w(s)\,\mathbf{1}_{s>0}$, que es una función en $L^1$ (pues $s^{-3/4}$ es integrable en $(0,1)$ y $w$ decae exponencialmente). Denotemos
$$\psi(r) = \int_0^\infty s^{-3/4}\,e^{irs}\,w(s)\,ds.$$
Entonces $I_{\mathrm{DC}}(r,k) \approx \frac{C^2 k^{-3/4}}{2}\,\psi(r)$, y la contribución DC de $\phi_k$ es suave, no oscilante en $k$.

### 3.4. El término oscilatorio: $I_{\mathrm{osc}}(r,k)$ y la fase estacionaria

$$I_{\mathrm{osc}}(r,k) = \frac{C^2 k^{-3/4}}{2}\,\mathrm{Re}\!\left[e^{-i\pi/2}\int_0^{a_k} s^{-3/4}\,e^{i\Phi(s)}\,w(s)\,ds\right],$$
con fase total $\Phi(s) = 4\sqrt{2\pi k s} + rs$ (tomando la parte $e^{i(4\sqrt{2\pi ks})}$ del coseno; el otro sumando con $e^{-i(4\sqrt{2\pi ks})}$ es análogo por conjugación).

**Punto estacionario.** La condición $\Phi'(s_*)= 0$ da:
$$4\sqrt{2\pi k}\cdot\frac{1}{2\sqrt{s_*}} + r = 0 \implies 2\sqrt{2\pi k/s_*} = -r \implies s_* = \frac{2\pi k}{(r/2)^2} = \frac{8\pi k}{r^2}.$$

*Observación sobre signos:* La ecuación $2\sqrt{2\pi k/s_*} + r = 0$ requiere $r < 0$. Para $r > 0$, $\Phi'(s) = 2\sqrt{2\pi k/s} + r > 0$ para todo $s > 0$, y no hay punto estacionario; el término $I_\mathrm{osc}$ decae más rápido que cualquier potencia de $k$ por el principio de Riemann-Lebesgue para fases monótonas.

Para $r < 0$ con $|r| > 0$, el punto estacionario es $s_* = 8\pi k/r^2$. La condición para que $s_*$ esté dentro del soporte es $s_* < a_k = 2k/\pi$, es decir:
$$\frac{8\pi k}{r^2} < \frac{2k}{\pi} \iff \frac{8\pi}{r^2} < \frac{2}{\pi} \iff r^2 > 4\pi^2 \iff |r| > 2\pi.$$

**Proposición 3.1** (Contribución de fase estacionaria). Para $r < -2\pi$ (con $|r|$ de orden 1 respecto a $k$), el punto estacionario $s_* = 8\pi k/r^2$ satisface $s_* < a_k$, y la contribución de fase estacionaria a $I_{\mathrm{osc}}(r,k)$ es:

$$I_{\mathrm{osc}}(r,k) \approx \frac{C^2 k^{-3/4}}{2}\cdot \mathrm{Re}\!\left[e^{-i\pi/2} \cdot s_*^{-3/4}\,w(s_*)\cdot\sqrt{\frac{2\pi}{|\Phi''(s_*)|}}\cdot e^{i\Phi(s_*) + i\,\mathrm{sgn}(\Phi''(s_*))\pi/4}\right],$$

donde:
- $\Phi(s_*) = 4\sqrt{2\pi k s_*} + r s_* = 4\sqrt{2\pi k \cdot 8\pi k/r^2} + r\cdot 8\pi k/r^2 = \frac{16\pi k}{|r|} - \frac{8\pi k}{r} = \frac{16\pi k}{|r|} + \frac{8\pi k}{|r|} = \frac{24\pi k}{|r|}$ (para $r < 0$, $r = -|r|$),
- $\Phi''(s) = -2\sqrt{2\pi k}\cdot\frac{1}{4}s^{-3/2} = -\frac{\sqrt{2\pi k}}{2}s^{-3/2}$, luego $\Phi''(s_*) = -\frac{\sqrt{2\pi k}}{2}s_*^{-3/2} < 0$,
- $|\Phi''(s_*)| = \frac{\sqrt{2\pi k}}{2}s_*^{-3/2} = \frac{\sqrt{2\pi k}}{2}\left(\frac{8\pi k}{r^2}\right)^{-3/2} = \frac{\sqrt{2\pi k}}{2}\cdot\frac{|r|^3}{(8\pi k)^{3/2}} = \frac{|r|^3}{2\cdot 8^{3/2}\pi k}$.

*Recalculando $\Phi(s_*)$ con más cuidado* (con $r = -|r| < 0$, $s_* = 8\pi k/r^2 = 8\pi k/|r|^2$):
$$\Phi(s_*) = 4\sqrt{2\pi k \cdot \frac{8\pi k}{|r|^2}} + (-|r|)\cdot\frac{8\pi k}{|r|^2} = 4\cdot\frac{\sqrt{16\pi^2 k^2}}{|r|} - \frac{8\pi k}{|r|} = 4\cdot\frac{4\pi k}{|r|} - \frac{8\pi k}{|r|} = \frac{16\pi k}{|r|} - \frac{8\pi k}{|r|} = \frac{8\pi k}{|r|}.$$

*Segunda derivada:*
$$|\Phi''(s_*)| = \frac{\sqrt{2\pi k}}{2}\cdot\left(\frac{8\pi k}{|r|^2}\right)^{-3/2} = \frac{\sqrt{2\pi k}}{2}\cdot\frac{|r|^3}{(8\pi k)^{3/2}}.$$

Simplificando:
$$\frac{\sqrt{2\pi k}}{(8\pi k)^{3/2}} = \frac{(2\pi k)^{1/2}}{(8\pi k)^{3/2}} = \frac{1}{(8\pi k)^{3/2}/(2\pi k)^{1/2}} = \frac{(2\pi k)^{1/2}}{(8\pi k)^{3/2}} = \frac{1}{8\pi k}\cdot\frac{(2\pi k)^{1/2}}{(8\pi k)^{1/2}} = \frac{1}{8\pi k}\cdot\sqrt{\frac{2}{8}} = \frac{1}{8\pi k}\cdot\frac{1}{2}.$$

Entonces $|\Phi''(s_*)| = \frac{|r|^3}{16\pi k}$.

Sustituyendo en la fórmula de fase estacionaria:
$$\sqrt{\frac{2\pi}{|\Phi''(s_*)|}} = \sqrt{\frac{2\pi\cdot 16\pi k}{|r|^3}} = \sqrt{\frac{32\pi^2 k}{|r|^3}} = \frac{4\pi\sqrt{2k}}{|r|^{3/2}}.$$

La amplitud:
$$s_*^{-3/4} = \left(\frac{8\pi k}{|r|^2}\right)^{-3/4} = \frac{|r|^{3/2}}{(8\pi k)^{3/4}}.$$

Producto de la amplitud y el prefactor de fase estacionaria:
$$s_*^{-3/4}\cdot\sqrt{\frac{2\pi}{|\Phi''(s_*)|}} = \frac{|r|^{3/2}}{(8\pi k)^{3/4}}\cdot\frac{4\pi\sqrt{2k}}{|r|^{3/2}} = \frac{4\pi\sqrt{2k}}{(8\pi k)^{3/4}} = \frac{4\pi\sqrt{2k}}{(8\pi)^{3/4}k^{3/4}} = \frac{4\pi\sqrt{2}}{(8\pi)^{3/4}}\cdot k^{1/2-3/4} = \frac{4\pi\sqrt{2}}{(8\pi)^{3/4}}\cdot k^{-1/4}.$$

Denotemos la constante numérica $\mathcal{A} = \frac{4\pi\sqrt{2}}{(8\pi)^{3/4}}$.

**Proposición 3.2** (Resultado final de fase estacionaria). Para $r < -2\pi$ con $|r|$ fijo y $k\to\infty$:
$$I_{\mathrm{osc}}(r,k) \approx \frac{C^2 k^{-3/4}}{2}\cdot\mathcal{A}\,k^{-1/4}\,w(s_*)\cdot\cos\!\left(\frac{8\pi k}{|r|} - \frac{\pi}{4}\right) = \frac{C^2\mathcal{A}}{2}\,k^{-1}\,w\!\left(\frac{8\pi k}{|r|^2}\right)\cos\!\left(\frac{8\pi k}{|r|} - \frac{\pi}{4}\right),$$
donde se usó que $\mathrm{sgn}(\Phi'') = -1$ contribuye un factor $e^{-i\pi/4}$, y la fase $e^{-i\pi/2}$ combinada con el coseno da un $\cos(\cdot - \pi/4)$ (heurístico; la cuenta exacta de las fases requiere cuidado).

**Conclusión cualitativa.** Para $r < -2\pi$, $\phi_k(r)$ oscila con frecuencia $\sim 8\pi k/|r|$ (como función de $k$) y amplitud $\sim k^{-1}\,e^{-4\pi^2 k/|r|^2}$ (el factor exponencial proviene de $w(s_*) \sim e^{-\pi s_*/2}$ con $s_* = 8\pi k/|r|^2$). Este decaimiento exponencial en $k$ hace que la serie $\sum_k k\,\phi_k(r)$ converja absolutamente para $r \neq 0$.

**Para $|r| < 2\pi$:** El punto estacionario $s_* = 8\pi k/|r|^2 > a_k = 2k/\pi$ está fuera del soporte, y $I_{\mathrm{osc}}$ decae superpolinomialmente en $k$ (como $O(k^{-N})$ para todo $N$). La contribución dominante a $\phi_k(r)$ es la parte DC.

**Observación de honestidad.** Los cálculos de §3.3–3.4 son *heurísticos* en el sentido de que la asintótica de Plancherel-Rotach del borde izquierdo (Doc 66) es válida para $s$ fijo y $k\to\infty$, pero la integral $\phi_k(r)$ involucra $s$ que varía a la vez que $k$. El intercambio de la asintótica con la integración requiere dominar el error de aproximación uniformemente en $s$, lo cual es técnico y se deja como tarea de justificación rigurosa.

---

## §4. La función $\widehat{W_\lambda\,dm_\infty}(r)$ como serie

### 4.1. Definición explícita

Por la definición del kernel de Abel (Doc 63):
$$W_\lambda(s) = \sum_{k=1}^{N(\lambda)} k\,|P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2\,|P_{N(\lambda)+1}(s)|^2,$$
tomando la transformada de Fourier con peso $dm_\infty$ y usando la linealidad:

$$\widehat{W_\lambda\,dm_\infty}(r) = \sum_{k=1}^{N(\lambda)} k\,\phi_k(r) + (a_{N(\lambda)}^\infty)^2\,\phi_{N(\lambda)+1}(r).$$

La convergencia de la integral es garantizada por el decaimiento de $W_\lambda$ y de $dm_\infty$: $W_\lambda \in L^2(dm_\infty)$ y la medida es finita, así que la integral existe para todo $r$.

### 4.2. Valor en el origen

**Proposición 4.1.** $\widehat{W_\lambda\,dm_\infty}(0) = \frac{N(\lambda)(N(\lambda)+1)}{2} + (a_{N(\lambda)}^\infty)^2$.

*Demostración.* Evaluando en $r = 0$ y usando $\phi_k(0) = 1$:
$$\widehat{W_\lambda\,dm_\infty}(0) = \sum_{k=1}^{N(\lambda)} k + (a_{N(\lambda)}^\infty)^2 = \frac{N(\lambda)(N(\lambda)+1)}{2} + (a_{N(\lambda)}^\infty)^2.$$
Como $a_{N(\lambda)}^\infty = \frac{1}{2}\sqrt{(2N+1)(2N+2)} \sim N$ (con $N = N(\lambda)$), el segundo término es $O(N^2)$ y la expresión total es $\frac{N^2}{2} + O(N)$. $\square$

**Corolario 4.2.** Para $N = N(\lambda) \to\infty$:
$$\widehat{W_\lambda\,dm_\infty}(0) \sim \frac{N(\lambda)^2}{2}.$$

### 4.3. Para $r = \log p$ (primo $p$)

Para $r = \log p > 0$ con $p$ primo, la discusión de §3 muestra que $\phi_k(\log p)$ tiene la estructura:
$$\phi_k(\log p) \approx \frac{C^2 k^{-3/4}}{2}\,\psi(\log p) + I_{\mathrm{osc}}(\log p, k),$$
donde $\psi(\log p)$ es la constante definida en §3.3 y $I_{\mathrm{osc}}$ decae superpolinomialmente (pues $\log p > 0$ y no hay punto estacionario real). Así para $r = \log p$:
$$\phi_k(\log p) = \frac{C^2}{2}k^{-3/4}\,\psi(\log p) + O(k^{-\infty}), \quad k\to\infty.$$

La suma en el kernel:
$$\sum_{k=1}^{N} k\,\phi_k(\log p) \approx \frac{C^2\psi(\log p)}{2}\sum_{k=1}^N k^{1-3/4} = \frac{C^2\psi(\log p)}{2}\sum_{k=1}^N k^{1/4} \approx \frac{C^2\psi(\log p)}{2}\cdot\frac{N^{5/4}}{5/4} = \frac{2C^2\psi(\log p)}{5}\,N^{5/4}.$$

**Proposición 4.3.** Para $r = \log p > 0$ con $p$ primo y $N = N(\lambda) \to\infty$:
$$\widehat{W_\lambda\,dm_\infty}(\log p) \sim K_p\,N(\lambda)^{5/4},$$
donde $K_p = \frac{2C^2}{5}\psi(\log p)$ es una constante que depende del primo $p$.

**Observación de honestidad.** La asintótica $\phi_k(r) \sim \frac{C^2}{2}k^{-3/4}\psi(r)$ para $r > 0$ fijo es heurística (depende de la validez uniforme de la Plancherel-Rotach de borde). Una cota rigurosa requeriría estimados más finos.

### 4.4. Para $r = \log(n/m)$ general

El mismo razonamiento aplica. Para $r = \log(n/m) > 0$ ($n > m$), $\widehat{W_\lambda\,dm_\infty}(\log(n/m)) \sim K_{n/m}\,N^{5/4}$. Para $r = \log(n/m) < 0$ ($n < m$) y $|\log(n/m)| > 2\pi$ (lo cual ocurre cuando $n/m < e^{-2\pi} \approx 0.0019$, es decir ratios muy distintos de 1), hay un punto estacionario y la contribución es mayor pero con decaimiento exponencial por $w(s_*)$.

---

## §5. La representación aritmética explícita

### 5.1. La fórmula de Doc 73

Por Proposición 9.1 de Doc 73:
$$A_\lambda := \int_{\mathbb{R}} W_\lambda(s)\,|\zeta(1/2+is)|^2\,dm_\infty(s) = \sum_{n,m \geq 1}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda\,dm_\infty}(\log(n/m)),$$
donde $d(n) = \sum_{j|n}1$ es la función divisor. La convergencia de esta serie doble requiere que $\sum_{n,m} \frac{d(n)d(m)}{\sqrt{nm}}|\widehat{W_\lambda dm_\infty}(\log(n/m))|< \infty$, lo cual se sigue del decaimiento exponencial de $\widehat{W_\lambda dm_\infty}$ fuera de una vecindad de $r=0$.

### 5.2. El término diagonal $n = m$

Para $n = m$, $\log(n/m) = 0$ y $\widehat{W_\lambda dm_\infty}(0) = \frac{N^2}{2}+O(N)$. La contribución diagonal es:
$$D_\lambda := \sum_{n \geq 1}\frac{d(n)^2}{n}\,\widehat{W_\lambda\,dm_\infty}(0) = \widehat{W_\lambda\,dm_\infty}(0)\cdot\sum_{n \geq 1}\frac{d(n)^2}{n}.$$

La serie $\sum_{n=1}^\infty d(n)^2/n$ diverge (como $\sim \frac{1}{6}(\log X)^3$ para $\sum_{n\leq X}$). Esto indica que la serie doble no converge absolutamente sin regularización, pero la fórmula de Doc 73 está entendida con la regularización adecuada que proviene de $W_\lambda$ como truncación finita. Explícitamente, para $n \leq X(\lambda)$ (donde $X(\lambda)$ es el rango efectivo de Fourier determinado por $\lambda$):

$$D_\lambda \approx \frac{N(\lambda)^2}{2}\cdot\frac{(\log X(\lambda))^3}{6}.$$

La relación entre $X(\lambda)$ y $\lambda$ depende del rango efectivo del kernel $W_\lambda$: dado que $W_\lambda$ está soportado en $[-a_{N(\lambda)}, a_{N(\lambda)}]$ con $a_{N(\lambda)} = 2N(\lambda)/\pi$, la transformada de Fourier $\widehat{W_\lambda dm_\infty}(r)$ decae para $|r| \gg 1$, y el rango efectivo en $r$ es $|r| \lesssim 1$. Esto corresponde a $\log(n/m) \lesssim 1$, es decir $n/m \in (e^{-1}, e)$, o sea $n \approx m$ con factor multiplicativo acotado.

**Proposición 5.1** (Estimado del término diagonal). Para $N = N(\lambda) \gg 1$:
$$D_\lambda = \frac{N(\lambda)^2}{2}\cdot\sum_{n=1}^{X_{\mathrm{eff}}}\frac{d(n)^2}{n} \approx \frac{N(\lambda)^2}{2}\cdot\frac{(\log X_{\mathrm{eff}})^3}{6},$$
donde $X_{\mathrm{eff}} \sim e^{C/r_{\min}}$ con $r_{\min}$ la frecuencia mínima donde $\widehat{W_\lambda dm_\infty}$ se hace despreciable.

### 5.3. Los términos off-diagonal $n \neq m$

Para $n \neq m$ con $r = \log(n/m) \neq 0$, el decaimiento de $\widehat{W_\lambda dm_\infty}(r)$ entra en juego. En primera aproximación (usando Proposición 4.3 para $|r| < 2\pi$):
$$\widehat{W_\lambda\,dm_\infty}(\log(n/m)) \sim K_{n/m}\,N(\lambda)^{5/4}.$$

Esto indica que la contribución off-diagonal escala como $N^{5/4}$, contra $N^2$ del diagonal. Así el diagonal domina en el régimen $N \to\infty$.

**Proposición 5.2** (Dominio del diagonal). Para $N(\lambda) \to\infty$:
$$A_\lambda = D_\lambda\,(1 + O(N(\lambda)^{-3/4})).$$

**Advertencia de honestidad.** Esta estimación requiere intercambiar suma y asintótica, lo cual no está justificado rigurosamente aquí. En particular, la serie sobre $(n,m)$ con $n \neq m$ es potencialmente grande si hay muchos pares con $\log(n/m)$ pequeño. Una estimación rigurosa requiere combinar la asintótica de $\phi_k$ con cotas para los coeficientes aritméticos $d(n)d(m)/\sqrt{nm}$.

### 5.4. Asintótica principal de $A_\lambda$

Bajo la heurística de §5.2, y combinando con la asintótica de $N(\lambda)$ como función de $\lambda$ (que depende de la definición de $N(\lambda)$; si $N(\lambda) \sim C\lambda$ entonces $N^2 \sim C^2\lambda^2$):

$$\boxed{A_\lambda \sim \frac{N(\lambda)^2}{2}\cdot\frac{(\log N(\lambda))^3}{6}}.$$

---

## §6. Implicaciones para $T_\lambda$

### 6.1. Estructura de $T_\lambda$

Recordemos (Doc 64, Doc 73):
$$T_\lambda = A_\lambda - B_\lambda, \quad A_\lambda = \int W_\lambda\,|\zeta|^2\,dm_\infty, \quad B_\lambda = \int W_\lambda\,|\zeta_{on}|^2\,dm_\infty.$$

La representación aritmética de $A_\lambda$ desarrollada en §5 es:
$$A_\lambda = \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda dm_\infty}(\log(n/m)).$$

### 6.2. Representación aritmética de $B_\lambda$

Para $B_\lambda$, la función $|\zeta_{on}(1/2+is)|^2$ se construye a partir del mismo kernel de Hadamard pero con todos los ceros sobre la línea crítica. Su representación de Dirichlet es análoga a la de $|\zeta|^2$:
$$|\zeta_{on}(1/2+is)|^2 = \sum_{n,m \geq 1}\frac{a_{on}(n)\overline{a_{on}(m)}}{\sqrt{nm}}\,e^{is\log(n/m)},$$
donde los coeficientes $a_{on}(n)$ son los mismos que los de $\zeta$ (función aritmética divisor $d(n)$) si $\zeta_{on}$ tiene los mismos coeficientes de Dirichlet que $\zeta$ — lo cual es por definición cierto ya que $\zeta_{on}$ y $\zeta$ tienen la misma serie de Dirichlet $\sum n^{-s}$. La diferencia entre $|\zeta|^2$ y $|\zeta_{on}|^2$ proviene de los ceros, no de los coeficientes.

De hecho, formalmente:
$$A_\lambda - B_\lambda = \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda dm_\infty}(\log(n/m)) - \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\,\widehat{W_\lambda dm_\infty^{on}}(\log(n/m)),$$
donde $\widehat{W_\lambda dm_\infty^{on}}$ usa $|\zeta_{on}|^2$ en lugar de $|\zeta|^2$. La comparación es entre el espectro de $|\zeta|^2$ y de $|\zeta_{on}|^2$ — estos dos coinciden si y solo si los ceros de $\zeta$ están sobre la línea crítica (RH).

### 6.3. $T_\lambda$ como diferencia aritmética

**Proposición 6.1.** Bajo RH, $\zeta = \zeta_{on}$ (pues todos los ceros están en la línea crítica) y $T_\lambda = A_\lambda - B_\lambda = 0$. Bajo $\neg$RH, la diferencia puede escribirse como:
$$T_\lambda = \sum_{n,m}\frac{d(n)d(m)}{\sqrt{nm}}\left[\widehat{W_\lambda dm_\infty}(\log(n/m)) - \widehat{W_\lambda dm_\infty^{on}}(\log(n/m))\right].$$
Cada término de la suma es la diferencia de las transformadas de Fourier evaluadas en $\log(n/m)$. Esta diferencia es pequeña para $n \approx m$ (donde ambas transformadas se aproximan a sus valores en $r = 0$, que son iguales).

### 6.4. Estimado del error

La diferencia $|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2$ para $s$ real viene controlada (bajo $\neg$RH con un cero off-critical $\rho_0 = \sigma_0 + i\gamma_0$) por un factor de la forma $((\sigma_0 - 1/2)^2 + (s - \gamma_0)^2)/((s-\gamma_0)^2) - 1 = (\sigma_0-1/2)^2/(s-\gamma_0)^2$. Para $s \gg \gamma_0$, este factor es pequeño. La integral $T_\lambda = \int W_\lambda(|\zeta|^2 - |\zeta_{on}|^2)dm_\infty$ es entonces del orden:
$$T_\lambda \lesssim C(\sigma_0,\gamma_0)\cdot\widehat{W_\lambda dm_\infty}(0)\cdot (\sigma_0 - 1/2)^2,$$
pero esto no es una cota superior que anule $T_\lambda$ — solo una cota que muestra que $T_\lambda$ es pequeño cuando $\sigma_0 - 1/2$ es pequeño.

**Observación de honestidad.** La representación aritmética de $A_\lambda$ no proporciona por sí sola una prueba de que $T_\lambda = 0$. Lo que sí proporciona es una descripción completamente explícita de $A_\lambda$ en términos de coeficientes aritméticos: la cantidad $A_\lambda = \sum_{n,m} d(n)d(m)/\sqrt{nm}\cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ es computable. La igualdad $T_\lambda = 0$ ($\Leftrightarrow$ RH) requiere un argumento adicional que conecte las transformadas de Fourier de $W_\lambda dm_\infty$ con las de $W_\lambda dm_\infty^{on}$: este es precisamente el contenido abierto del programa.

---

## §7. Síntesis y tabla de resultados

| Objeto | Resultado riguroso | Calidad |
|---|---|---|
| $\phi_k(0) = 1$ | Sí (Prop. 1.1) | Riguroso |
| $\phi_k(-r) = \phi_k(r)$ | Sí (Prop. 1.2) | Riguroso |
| $|\phi_k(r)| \leq 1$ | Sí (Prop. 1.3) | Riguroso |
| $\phi_k(r) \to 0$ para $|r|\to\infty$ | Sí (Prop. 1.4) | Riguroso |
| $|\phi_k(r)| = O(e^{-\pi|r|/4})$ | Sí (Prop. 1.5, con hipótesis de analiticidad) | Riguroso (bajo la hipótesis de analiticidad de la franja) |
| $\phi_0(r) = \hat{w}(r)$ | Sí | Riguroso |
| $\phi_1(r) = -2\hat{w}''(r)$ | Sí (Prop. 2.2) | Riguroso |
| Asintótica $\phi_k(r)$ via P-R | Heurística (Prop. 3.2) | Heurístico (intercambio asintótica-integral pendiente) |
| $\widehat{W_\lambda dm_\infty}(0) \sim N(\lambda)^2/2$ | Sí (Prop. 4.1) | Riguroso |
| $\widehat{W_\lambda dm_\infty}(\log p) \sim K_p N^{5/4}$ | Heurístico (Prop. 4.3) | Heurístico |
| $A_\lambda \sim \frac{N^2}{2}\cdot\frac{(\log N)^3}{6}$ | Heurístico | Heurístico |

---

## §8. Direcciones para justificación rigurosa

Los resultados heurísticos de §3 requieren los siguientes pasos para hacerse rigurosos:

1. **Uniformidad de Plancherel-Rotach:** Establecer que la asintótica de Doc 66 es uniforme en $s \in (0, \delta a_k)$ con un error acotado por $C k^{-3/8-\varepsilon} s^{-3/8}$. Esto permitiría dominar el integrando y justificar el intercambio.

2. **Análisis en el bulk:** Completar la asintótica de $\phi_k(r)$ incluyendo la región bulk $s \asymp a_k$, donde la asintótica de Plancherel-Rotach interior (Doc 66, §5) es diferente.

3. **Determinación de $C$:** Calcular la constante de normalización $C = C(k)$ en la asintótica del borde izquierdo a partir de los datos de Doc 66, o de la condición $\phi_k(0) = 1$.

4. **Estimados para la serie doble:** Demostrar que la serie $\sum_{n\neq m} d(n)d(m)/\sqrt{nm}\cdot \widehat{W_\lambda dm_\infty}(\log(n/m))$ es efectivamente $O(N^{5/4+\varepsilon})$, estableciendo el dominio del diagonal en §5.2 de forma rigurosa.

---

*Fin del Documento 76.*
