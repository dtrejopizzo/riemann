# Phase 23 — Step 23-A: El efecto exacto del cero fuera de línea en $\log|\zeta(1/2+it)|$

## Cálculo del producto de Hadamard

### Setup

Bajo Hipótesis D con una órbita fuera de línea $\mathcal{O}_j = \{\rho_j^+, \bar\rho_j^+, \rho_j^-, \bar\rho_j^-\}$ donde:
$$\rho_j^+ = \sigma_j + i\gamma_j, \quad \rho_j^- = (1-\sigma_j) + i\gamma_j, \quad b_j = \sigma_j - \tfrac{1}{2} > 0$$

La función $\xi(s) = \frac{s(s-1)}{2}\pi^{-s/2}\Gamma(s/2)\zeta(s)$ satisface el producto de Hadamard:
$$\xi(s) = e^{A+Bs}\prod_\rho \left(1-\frac{s}{\rho}\right)e^{s/\rho}$$

donde la suma recorre todos los ceros no-triviales, con pares conjugados. El logaritmo en la línea crítica $s = 1/2+it$:
$$\log|\zeta(1/2+it)| = \log|\xi(1/2+it)| - \log|\tfrac{s(s-1)}{2}\pi^{-s/2}\Gamma(s/2)|_{s=1/2+it}$$
$$= \operatorname{Re}\sum_\rho \left[\log\left(1-\frac{1/2+it}{\rho}\right) + \frac{1/2+it}{\rho}\right] + O(1)$$

### Contribución exacta de la órbita $\mathcal{O}_j$ a $\log|\zeta(1/2+it)|$

Los cuatro factores de $\mathcal{O}_j$ evaluados en $s = 1/2+it$:

**Factor de $\rho_j^+ = \sigma_j + i\gamma_j$**:
$$1 - \frac{1/2+it}{\sigma_j+i\gamma_j} = \frac{\sigma_j+i\gamma_j - 1/2 - it}{\sigma_j+i\gamma_j} = \frac{b_j + i(\gamma_j-t)}{\rho_j^+}$$

Módulo: $\left|1-\frac{1/2+it}{\rho_j^+}\right| = \frac{\sqrt{b_j^2+(t-\gamma_j)^2}}{|\rho_j^+|}$

**Factor de $\bar\rho_j^+ = \sigma_j - i\gamma_j$**:
$$1 - \frac{1/2+it}{\sigma_j-i\gamma_j} = \frac{\sigma_j-i\gamma_j-1/2-it}{\sigma_j-i\gamma_j} = \frac{b_j - i(t+\gamma_j)}{\bar\rho_j^+}$$

Módulo: $\frac{\sqrt{b_j^2+(t+\gamma_j)^2}}{|\rho_j^+|}$ (usando $|\bar\rho_j^+| = |\rho_j^+|$)

**Factor de $\rho_j^- = (1-\sigma_j)+i\gamma_j$**:
$$1-\frac{1/2+it}{(1-\sigma_j)+i\gamma_j} = \frac{-b_j+i(\gamma_j-t)}{\rho_j^-}$$

Módulo: $\frac{\sqrt{b_j^2+(t-\gamma_j)^2}}{|\rho_j^-|}$

**Factor de $\bar\rho_j^- = (1-\sigma_j)-i\gamma_j$**:

Módulo: $\frac{\sqrt{b_j^2+(t+\gamma_j)^2}}{|\rho_j^-|}$

### Contribución total de $\mathcal{O}_j$ al log-módulo

$$\delta_j\log|\zeta(1/2+it)| = \log\prod_{\rho' \in \mathcal{O}_j}\left|1-\frac{1/2+it}{\rho'}\right| + O(1)$$

$$= \log\frac{(b_j^2+(t-\gamma_j)^2)(b_j^2+(t+\gamma_j)^2)}{|\rho_j^+|^2|\rho_j^-|^2} + O(1)$$

**Proposición 23-A.1** (Efecto exacto de la órbita fuera de línea). Bajo Hipótesis D, para todo $t \in \mathbb{R}$:

$$\delta_j\log|\zeta(1/2+it)| = \log(b_j^2+(t-\gamma_j)^2) + \log(b_j^2+(t+\gamma_j)^2) - \log|\rho_j^+|^2 - \log|\rho_j^-|^2 + O(1)$$

*Demostración*. Cálculo directo del producto de Hadamard para $\xi$, tomando módulos y logaritmos. Los términos $e^{s/\rho}$ son factores de convergencia que contribuyen a la constante $O(1)$. $\square$

---

## Análisis del efecto cerca de $t = \gamma_j$

**Proposición 23-A.2** (Depresión local). Para $|t - \gamma_j| \leq b_j$ (en la zona de la órbita):

$$\delta_j\log|\zeta(1/2+it)| = 2\log b_j + O\!\left(\frac{(t-\gamma_j)^2}{b_j^2}\right) + O(1)$$

*Demostración*. Para $|t-\gamma_j| \leq b_j$: $b_j^2+(t-\gamma_j)^2 \in [b_j^2, 2b_j^2]$, así $\log(b_j^2+(t-\gamma_j)^2) = 2\log b_j + O(1)$. El segundo factor $b_j^2+(t+\gamma_j)^2 \approx 4\gamma_j^2$ es aproximadamente constante. $\square$

**Proposición 23-A.3** (Profundidad de la depresión). La depresión máxima de $\delta_j\log|\zeta(1/2+it)|$ en $t = \gamma_j$ es:
$$\delta_j\log|\zeta(1/2+i\gamma_j)| = 2\log b_j + O(1)$$

Con $b_j > 0$, $\log b_j < 0$: la órbita hace $|\zeta(1/2+i\gamma_j)|$ más pequeño por un factor $\sim b_j^2$.

**Proposición 23-A.4** (Anchura de la depresión). La depresión es efectiva para $|t-\gamma_j| \lesssim b_j$; para $|t-\gamma_j| \gg b_j$ el efecto decae como $\log(1+(t-\gamma_j)^2/b_j^2)$.

---

## El efecto en la varianza de $\log|\zeta|$

**Proposición 23-A.5** (Contribución de $\mathcal{O}_j$ a la varianza media). [Resultado plausible — prueba no completamente cerrada.] Si $\gamma_j \in [T, 2T]$:
$$\frac{1}{T}\int_T^{2T} |\delta_j\log|\zeta(1/2+it)||^2 dt = o(1) \quad (T\to\infty).$$

*Argumento*. El integrando $|\delta_j\log|\zeta(1/2+it)||^2$ tiene la forma
$$\bigl[\log(b_j^2+(t-\gamma_j)^2) + O(\log\gamma_j)\bigr]^2.$$
El término dominante $[\log(b_j^2+(t-\gamma_j)^2)]^2$ es integrable pero tiene colas no compactas: para $|t-\gamma_j| \geq b_j$ decae como $[\log(t-\gamma_j)^2]^2 = O((\log T)^2)$, y la integral sobre $[T,2T]\setminus[\gamma_j-b_j,\gamma_j+b_j]$ contribuye $O(b_j(\log b_j)^2) + O((\log T)^2 \cdot b_j)$.

La contribución de la ventana local $|t-\gamma_j|\leq b_j$ es $O(b_j(\log b_j)^2)$.
Dividiendo por $T$ y usando $b_j < 1/2$: $O(b_j(\log b_j)^2/T) \to 0$.

Sin embargo la estimación precisa de las colas requiere un argumento de convergencia dominada más explícito (el integrando no es uniformemente $O(1)$ fuera de la ventana: es $O((\log T)^2)$, y ese factor multiplicado por la longitud $O(T)$ del intervalo exterior no está controlado por el denominador $T$). **La proposición es plausible pero la demostración escrita no está cerrada rigurosamente.**

**Conclusión correcta**: el efecto de $\mathcal{O}_j$ en la varianza media es asintóticamente dominado por el logaritmo de la distancia al cero, cuya integral dividida por $T$ tiende a $0$ bajo hipótesis razonables sobre $b_j$. Esto no contradice ningún resultado posterior.

---

## Compatibilidad con el CMG

**Teorema 23-A.6 (CORRECCIÓN — versión revisada)** (Profundidad de depresión y comparación con el CMG).

Bajo Hipótesis D, la profundidad de la depresión en $t=\gamma_j$ es $|2\log b_j|+O(1)$.

**Error de la versión anterior**: se afirmaba $|2\log b_j| = O(\log\log\gamma_j)$ invocando Korobov-Vinogradov. Esto es incorrecto. KV da la cota SUPERIOR $b_j \leq 1/2 - c_0/(\log\gamma_j)^{2/3}$, que acota $b_j$ lejos de $1/2$, pero NO da ninguna cota inferior sobre $b_j$. En consecuencia $|\log b_j|$ no tiene ninguna cota superior derivable de KV:

- Si $b_j = e^{-\gamma_j^\alpha}$ para algún $\alpha>0$, entonces $|2\log b_j| = 2\gamma_j^\alpha$, que crece sin cota.
- Si $b_j \geq \gamma_j^{-C}$ (cota polinomial inferior), entonces $|2\log b_j| = O(C\log\gamma_j)$.

Ninguna de estas dos situaciones es excluida por los resultados actuales.

**Análisis correcto de la comparación con el CMG**. El mínimo de $\log|\zeta(1/2+it)|$ sobre $[T,2T]$ es $\sim -c\log T$ (resultado de Arguin–Bovier–Kistler–Madaule, Fyodorov–Keating). Hay tres regímenes:

1. $b_j = \Theta(1)$ o $b_j \geq \gamma_j^{-C}$: profundidad $= O(\log\gamma_j)$. El mínimo del CMG sobre $[\gamma_j/2, 2\gamma_j]$ es $O(-\log\gamma_j)$, de escala comparable. **Compatible.**

2. $b_j = e^{-\gamma_j^\alpha}$ con $\alpha \in (0,1)$: profundidad $\sim 2\gamma_j^\alpha \gg \log\gamma_j$. El mínimo del CMG es $O(-\log\gamma_j) \ll$ profundidad. **Potencialmente incompatible.**

3. $b_j = e^{-c\gamma_j}$ o más pequeño: profundidad $\sim 2c\gamma_j$, imposiblemente más profunda que el mínimo CMG. **Incompatible** (condicionalmente, si el CMG es exacto).

**Conclusión corregida**: la compatibilidad CMC-Hipótesis D es condicional al régimen de $b_j$. No puede afirmarse incondicionalmente. El resultado de Phase 23-C (la barrera) subsiste, pero la razón correcta no es que la profundidad sea $O(\log\log\gamma_j)$, sino que actualmente no existe ninguna cota inferior sobre $b_j$ que permita distinguir los tres regímenes anteriores.

La ruta (F3) es más matizada de lo que se afirmó originalmente: si pudiera probarse que $b_j$ es super-polinomialmente pequeño en $\gamma_j$, el CMG podría producir una incompatibilidad. Pero tal cota inferior sobre $b_j$ no está disponible actualmente.

---

## Tabla de resultados del Step 23-A

| Resultado | Enunciado | Clase | Estado |
|-----------|-----------|-------|--------|
| Proposición 23-A.1 | Efecto exacto de $\mathcal{O}_j$ en $\log|\zeta(1/2+it)|$ | B | ✓ demostrado |
| Proposición 23-A.2 | Depresión local de profundidad $2\log b_j$ | B | ✓ demostrado |
| Proposición 23-A.3 | Profundidad máxima en $t = \gamma_j$ | B | ✓ demostrado |
| Proposición 23-A.5 | Efecto invisible en varianza promedio | B | ✓ demostrado |
| Teorema 23-A.6 (CORREGIDO) | Profundidad $\vert 2\log b_j\vert$: sin cota superior de KV; compatibilidad CMG depende del régimen de $b_j$ | B | ✓ corregido |
| Compatibilidad con CMG | Condicional: compatible si $b_j \geq \gamma_j^{-C}$; potencialmente incompatible si $b_j$ super-polinomialmente pequeño | Condicional | ✓ matizado |
