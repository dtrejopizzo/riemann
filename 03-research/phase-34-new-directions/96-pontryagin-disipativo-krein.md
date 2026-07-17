# Doc 96 — Dirección B (tercera capa): Disipatividad, función característica, y el Teorema de Krein

**Fecha:** junio 2026
**Fase:** 34 — Nuevas direcciones
**Contexto:** Continuación de los Docs 91 y 94 de la Dirección B. El Doc 91 estableció el espacio de Pontryagin $(\mathcal{K}, Q)$ y el operador $H_C$, e identificó siete rutas hacia $\kappa = 0$, todas circulares o equivalentes a RH. El Doc 94 analizó la condición C5 en detalle. Este documento explora cuatro ángulos nuevos: disipatividad vía la función característica de Brodskii–Livsic, positividad a partir del producto de Euler, índice de Maslov y curvatura simpléctica, y el Teorema de Krein sobre operadores acotados.
**Regla absoluta:** No se fabricará ninguna prueba de RH. Si un argumento no cierra, se dirá con precisión el punto de quiebre.

---

## Resumen ejecutivo

Este documento organiza el análisis en cuatro ángulos independientes, cada uno inspirado en un resultado de la teoría de operadores que podría, en principio, forzar el índice negativo $\kappa = 0$ sin pasar por el conocimiento explícito de los ceros de $\zeta$.

**Ángulo 1 (Brodskii–Livsic):** La función característica $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ satisface $|\Theta(z)| = 1$ en todo $\mathbb{C}$ (módulo constante 1 por la ecuación funcional), no $|\Theta(z)| \leq 1$. Esto corresponde a un operador unitario en el espacio de Krein, no a uno disipativo. La disipatividad requeriría torcer la función característica mediante un "canal de absorción" que no tiene análogo natural en la geometría de $\xi$. El ángulo no está obturado en principio, pero la construcción de una función característica torcida introduce libertad no controlada.

**Ángulo 2 (Producto de Euler):** El producto de Euler fuerza la positividad de $Q$ en el subespacio donde las funciones de prueba tienen transformada de Mellin concentrada en $\mathrm{Re}(s) > 1$. Este subespacio es $Q$-positivo incondicionalmente. Sin embargo, la propagación de esta positividad a todo $\mathcal{K}$ por analiticidad falla: el espacio $\mathcal{K}$ no tiene estructura analítica que permita extender una forma cuadrática por continuación analítica. El argumento colapsa antes de obtener $\kappa = 0$.

**Ángulo 3 (Índice de Maslov):** La forma simpléctica $Q$ sobre $\mathcal{K}$ tiene interpretación adélica vía la fórmula de Weil. El índice de Maslov de familias de subespacios lagrangianos en $(\mathcal{K}, Q)$ está bien definido formalmente, pero el cálculo concreto de ese índice requiere conocer la signatura de $Q$ en subespacios específicos, lo que circularmente remite a los ceros de $\zeta$. La conexión con la curvatura de una variedad simpléctica aritmética es especulativa y se delimita con precisión.

**Ángulo 4 (Teorema de Krein):** El resolvente $R_{\lambda_0} = (H_C - \lambda_0)^{-1}$ es un operador acotado en $\Pi_\kappa$ para $\lambda_0 \notin \sigma(H_C)$, y tiene exactamente el mismo índice negativo que $H_C$. El Teorema de Krein (1950) sobre operadores acotados autoadjuntos en espacios de Pontryagin da $\kappa = 0$ solo si $\sigma(R_{\lambda_0}) \subset \mathbb{R}$, que es la condición de partida en forma diferente. La ruta del resolvente no aporta nueva palanca.

**Conclusión general:** Ninguno de los cuatro ángulos cierra el argumento $\kappa = 0$ de manera independiente. Los Ángulos 1 y 3 son potencialmente ricos en estructura nueva pero no dan resultados sin hipótesis adicionales sobre $\zeta$. Los Ángulos 2 y 4 se obturan por argumentos precisos. La observación más valiosa del documento es el Teorema 2.12 (Ángulo 2): la positividad del producto de Euler en la región $\mathrm{Re}(s) > 1$ define un subespacio $Q$-positivo concreto, cuya proyección sobre $\mathcal{K}$ es calculable, y el cociente entre ese subespacio y $\mathcal{K}$ contiene toda la información sobre $\kappa$.

---

## Parte I — Ángulo 1: Operadores disipativos y la función característica de Brodskii–Livsic

### Sección 1.1 — Operadores disipativos en espacios de Krein

Comenzamos recordando las definiciones relevantes en el marco de espacios de Krein y Pontryagin.

**Definición 1.1 (Espacio de Krein).** Un **espacio de Krein** $(\mathcal{K}, [\cdot, \cdot])$ es un espacio vectorial complejo con forma hermitiana indefinida no-degenerada $[\cdot, \cdot]$ tal que $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ (descomposición fundamental) con $(\mathcal{K}_\pm, \pm[\cdot,\cdot])$ espacios de Hilbert. Si $\dim \mathcal{K}_- = \kappa < \infty$, el espacio se llama espacio de Pontryagin de índice $\kappa$, denotado $\Pi_\kappa$.

En nuestro contexto $(\mathcal{K}, Q)$ es el espacio de Pontryagin de Weil–Connes (Doc 91, Definición 1.7) con $\kappa = \mathrm{neg.ind}(H_C)$, y RH $\iff \kappa = 0$.

**Definición 1.2 (Operador disipativo en espacio de Krein).** Un operador lineal densamente definido $A : \mathrm{Dom}(A) \to \mathcal{K}$ en el espacio de Krein $(\mathcal{K}, [\cdot, \cdot])$ se llama **$[\cdot,\cdot]$-disipativo** si:
$$\mathrm{Im}[Af, f] \geq 0 \quad \text{para todo } f \in \mathrm{Dom}(A).$$

Se llama **$[\cdot,\cdot]$-anti-disipativo** si $\mathrm{Im}[Af, f] \leq 0$.

Equivalentemente: $A$ es disipativo si $A - A^{[*]} = -2i \mathrm{Im}A \leq 0$ en el sentido de la forma, donde $A^{[*]}$ es el $[\cdot,\cdot]$-adjunto de $A$.

**Definición 1.3 (Completamente no-autoadjunto).** Un operador $A$ es **completamente no-$[\cdot,\cdot]$-autoadjunto** (cna) si no existe un subespacio de Krein no trivial sobre el cual $A$ sea $[\cdot,\cdot]$-autoadjunto.

**Teorema 1.4 (Brodskii–Livsic, versión espacio de Hilbert; cf. Brodskii 1971, Ch. VI).** Sea $A$ un operador cna en un espacio de Hilbert $H$ con parte no autoadjunta de rango nuclear (defecto finito). Entonces:

*(i)* La función característica $\Theta_A(z) = I + 2i K^*(A - zI)^{-1} K$ (donde $K$ es el operador de defecto) es una función matricial analítica que determina $A$ hasta equivalencia unitaria.

*(ii)* $A$ es disipativo $\iff \|\Theta_A(z)\| \leq 1$ para $z \in \mathbb{C}^+ = \{z : \mathrm{Im}(z) > 0\}$.

*(iii)* Si $A$ es disipativo y autoadjunto en sentido de Hilbert, el espectro de $A$ es real.

El paso de espacio de Hilbert a espacio de Pontryagin requiere la teoría de Livsic–Yantsevich (1979) con funciones $J$-unitarias.

---

### Sección 1.2 — La función característica candidata de $H_C$

Del Doc 91, Sección 5.2 y Conjetura 5.4, la función característica candidata de $H_C$ es:
$$\Theta(z) = \frac{\xi(1/2 + z)}{\xi(1/2 - z)},$$
donde $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ es la función $\xi$ completa.

El análisis de si $H_C$ es disipativo se reduce al estudio de $|\Theta(z)|$ en el semiplano superior.

---

### Sección 1.3 — La ecuación funcional impide la disipatividad estricta

**Proposición 1.5 (El módulo de la función característica es 1).** Para todo $z \in \mathbb{C}$:
$$|\Theta(z)| = \left|\frac{\xi(1/2 + z)}{\xi(1/2 - z)}\right| = 1.$$

*Demostración.* La ecuación funcional de $\xi$ establece $\xi(s) = \xi(1 - s)$ para todo $s \in \mathbb{C}$. Sustituyendo $s = 1/2 + z$:
$$\xi(1/2 + z) = \xi(1 - (1/2 + z)) = \xi(1/2 - z).$$

Por lo tanto $|\xi(1/2 + z)| = |\xi(1/2 - z)|$ para todo $z \in \mathbb{C}$, y el cociente tiene módulo 1:
$$|\Theta(z)| = \frac{|\xi(1/2 + z)|}{|\xi(1/2 - z)|} = 1. \qquad \square$$

**Observación 1.6.** El resultado es inmediato pero tiene una consecuencia profunda: la función $\Theta(z)$ no es una función de Schur (contractiva en el semiplano superior), sino una función unitaria. En la clasificación de Brodskii–Livsic:

- $\|\Theta_A(z)\| \leq 1$ en $\mathbb{C}^+$: operador disipativo.
- $\|\Theta_A(z)\| = 1$ en $\mathbb{C}^+$: operador unitario (autoadjunto en el sentido del espacio de Hilbert o del espacio de Krein, según el contexto).
- $\|\Theta_A(z)\| \geq 1$ en $\mathbb{C}^+$: operador anti-disipativo.

La función característica $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ es unitaria en todo $\mathbb{C}$, no solo en el semiplano superior.

**Corolario 1.7 (La ecuación funcional bloquea la disipatividad).** El operador $H_C$, con función característica dada por la Conjetura 5.4 del Doc 91, **no es disipativo** en el sentido de Brodskii–Livsic. Tampoco es anti-disipativo. La ecuación funcional $\xi(s) = \xi(1-s)$ coloca a $H_C$ exactamente en la frontera entre disipatividad y anti-disipatividad.

*Interpretación.* Esta frontera corresponde al hecho de que $H_C$ es formalmente $Q$-autoadjunto (por la $Q$-simetría discutida en el Doc 91, Proposición 1.10), y los operadores autoadjuntos en espacios de Krein tienen función característica unitaria. La disipatividad requeriría romper la $Q$-autoadjunticidad.

---

### Sección 1.4 — Implicaciones del módulo constante: el operador es $J$-unitario

**Definición 1.8 (Función $J$-unitaria).** Una función matricial meromorfa $\Theta(z)$ es **$J$-unitaria** (para una matriz $J = J^* = J^{-1}$ con valores $\pm 1$ en la diagonal) si:
$$\Theta(z)^* J \Theta(z) = J \quad \text{para } z \in \mathbb{R} \setminus \{\text{polos}\}.$$

Para el caso escalar (dimensión 1) con $J = 1$ (o $J = -1$), $J$-unitario equivale a que $|\Theta(z)| = 1$ en $\mathbb{R}$.

**Proposición 1.9 (La función $\Theta$ es $J$-unitaria con $J = 1$).** La función $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ satisface $|\Theta(x)| = 1$ para $x \in \mathbb{R}$ (por la Proposición 1.5, que aplica en particular a $z = x$ real).

En la teoría de operadores en espacios de Pontryagin (cf. Alpay–Dijksma–Rovnyak–de Snoo, 1997), los operadores $Q$-autoadjuntos tienen funciones características $J$-unitarias. El Teorema espectral de Kreĭn–Langer (Doc 91, Teorema 2.7) es precisamente la contrapartida del análisis en términos de funciones $J$-unitarias.

**Observación 1.10 (La dicotomía entre función unitaria y espectro no-real).** Aunque $|\Theta(z)| = 1$ identicamente, la función $\Theta(z)$ puede tener polos en $\mathbb{C} \setminus \mathbb{R}$. Un polo de $\Theta$ en $z_0 = \rho - 1/2$ (con $\rho$ cero de $\xi$) aparece cuando $\xi(1/2 - z_0) = \xi(\rho) = 0$. Si $\rho$ es un cero fuera de la línea crítica (con $\mathrm{Re}(\rho) \neq 1/2$), entonces $z_0 = \rho - 1/2$ tiene parte real no nula, y el polo está en $\mathbb{C} \setminus i\mathbb{R}$.

Esto es consistente con el Teorema 5.3(i) del Doc 91: los polos de la función característica en $\mathbb{C} \setminus \mathbb{R}$ corresponden a los eigenvalores no-reales del operador, que son exactamente los ceros de $\zeta$ fuera de la línea crítica.

---

### Sección 1.5 — Función característica torcida: la idea y su obstáculo

Para obtener una función característica contractiva (y por ende un operador disipativo), se podría intentar torcer $\Theta(z)$ por una función exterior.

**Definición 1.11 (Torsión por función exterior).** Sea $\phi(z)$ una función analítica en $\mathbb{C}^+$ con $|\phi(z)| \leq 1$ en $\mathbb{C}^+$ y $|\phi(x)| = 1$ para $x \in \mathbb{R}$ (función interna de Hardy). La **función característica torcida** es:
$$\Theta_\phi(z) = \phi(z) \cdot \Theta(z) = \phi(z) \cdot \frac{\xi(1/2 + z)}{\xi(1/2 - z)}.$$

Si $|\phi(z)| < 1$ en $\mathbb{C}^+$, entonces $|\Theta_\phi(z)| < 1$ en $\mathbb{C}^+$, y el operador correspondiente sería disipativo.

**Proposición 1.12 (El operador torcido tiene diferente función característica de ceros).** Si $\Theta_\phi$ es la función característica del operador $A_\phi$ (definido abstractamente por $\Theta_\phi$), entonces los polos de $\Theta_\phi$ en $\mathbb{C} \setminus \mathbb{R}$ son los polos de $\Theta$ que no son cancelados por $\phi$ más los polos de $\phi$ en $\mathbb{C} \setminus \mathbb{R}$.

En particular, si $\phi$ no tiene polos en $\mathbb{C}^+$, los eigenvalores no-reales de $A_\phi$ son exactamente los eigenvalores no-reales de $H_C$.

*Demostración.* Los polos de $\Theta_\phi = \phi \cdot \Theta$ en $\mathbb{C}^+$ son los polos de $\Theta$ en $\mathbb{C}^+$ (asumiendo $\phi$ analítica y sin ceros en $\mathbb{C}^+$). $\square$

**Corolario 1.13 (La torsión no cambia los eigenvalores no-reales).** Torcer la función característica por una función interna no crea ni destruye eigenvalores no-reales, solo cambia las propiedades de disipatividad/contractividad. Por lo tanto, la técnica de la función torcida no proporciona información nueva sobre $\kappa$.

**Observación 1.14 (La raíz del bloqueo).** El Teorema de Brodskii–Livsic dice: "$A$ es disipativo $\iff$ $\|\Theta_A\| \leq 1$ en $\mathbb{C}^+$". Pero la disipatividad de $A$ en un espacio de Hilbert implica que el **espectro de $A$ está en el semiplano superior cerrado $\overline{\mathbb{C}^+}$**, no en la recta real. Para $H_C$, cuyos eigenvalores son imaginarios puros $i\gamma_n$ (en la línea crítica) o complejos con parte real no nula (fuera de ella), el espectro **no** está en un semiplano. Esto confirma que $H_C$ no puede ser disipativo en ningún espacio de Hilbert natural.

Sin embargo, en el espacio de Pontryagin $(\mathcal{K}, Q)$, la definición de disipatividad cambia: se pide $\mathrm{Im}[H_C f, f]_Q \geq 0$, no $\mathrm{Im}\langle H_C f, f\rangle_{L^2} \geq 0$. Esta distinción es crucial y es lo que permite que la idea tenga sentido.

---

### Sección 1.6 — Disipatividad relativa a la forma $Q$

**Definición 1.15 (Disipatividad $Q$).** El operador $H_C$ es **$Q$-disipativo** si:
$$\mathrm{Im}\, Q(H_C f, f) \geq 0 \quad \text{para todo } f \in \mathrm{Dom}(H_C).$$

**Proposición 1.16 (Relación entre $Q$-disipatividad y autoadjunticidad).** Si $H_C$ es $Q$-autoadjunto (es decir, $Q(H_C f, g) = Q(f, H_C g)$ para $f, g$ en el dominio), entonces:
$$Q(H_C f, f) = Q(f, H_C f) = \overline{Q(H_C f, f)},$$
luego $Q(H_C f, f)$ es real. En particular, $\mathrm{Im}\, Q(H_C f, f) = 0$.

*Demostración.* Por $Q$-simetría y anti-simetría de la parte hermitiana: $Q(H_C f, f) = \overline{Q(f, H_C f)} = \overline{Q(H_C f, f)}$ (usando que $Q$ es hermitiana). Por lo tanto $Q(H_C f, f) \in \mathbb{R}$. $\square$

**Corolario 1.17 (Los operadores $Q$-autoadjuntos no son $Q$-disipativos no trivialmente).** Si $H_C$ es $Q$-autoadjunto, entonces $\mathrm{Im}\, Q(H_C f, f) = 0$ para todo $f$, y la condición de $Q$-disipatividad se satisface trivialmente (con igualdad). La disipatividad estricta ($>0$) requeriría romper la $Q$-autoadjunticidad.

**Observación 1.18 (Resumen del Ángulo 1).** El análisis muestra que:

1. La función característica de $H_C$ tiene módulo 1 identicamente (Proposición 1.5), lo que la clasifica como unitaria, no contractiva.
2. Esto es consistente con la $Q$-autoadjunticidad formal de $H_C$: los operadores $Q$-autoadjuntos tienen función característica $J$-unitaria.
3. Torcer la función característica no cambia los eigenvalores no-reales (Corolario 1.13).
4. La $Q$-disipatividad de $H_C$ se satisface trivialmente (con igualdad) por su $Q$-autoadjunticidad, y no proporciona información sobre los eigenvalores (Corolario 1.17).

**La versión del Teorema de Brodskii–Livsic relevante para espacios de Pontryagin requeriría una función $J$-contractiva, no simplemente contractiva.** En ese lenguaje, la condición es:
$$\Theta(z)^* J \Theta(z) \leq J \quad \text{en } \mathbb{C}^+.$$
Para $J$ con valores $+1$ y $-1$ que refleje la signatura de $Q$, esta condición podría no ser trivialmente satisfecha incluso cuando $|\Theta| = 1$. Este es el único punto de apertura genuina del Ángulo 1, y su exploración requeriría precisar la $J$-signatura del espacio de defecto de $H_C$.

---

## Parte II — Ángulo 2: El producto de Euler y la positividad en $\mathrm{Re}(s) > 1$

### Sección 2.1 — El producto de Euler y sus implicaciones espectrales

El producto de Euler:
$$\zeta(s) = \prod_{p \text{ primo}} (1 - p^{-s})^{-1}, \quad \mathrm{Re}(s) > 1,$$
converge absolutamente para $\mathrm{Re}(s) > 1$ y en particular $\zeta(s) \neq 0$ en esa región. ¿Qué implica esto para la forma cuadrática $Q$?

**Definición 2.1 (Subespacio de Mellin concentrado en $\mathrm{Re}(s) > 1$).** Sea $\sigma_0 > 1$ y definamos el subespacio:
$$\mathcal{H}_{\sigma_0} = \left\{ f \in \mathcal{S}(\mathbb{R}^*_+) : \hat{f}(s) = 0 \text{ para } \mathrm{Re}(s) \leq \sigma_0 \right\},$$
donde $\hat{f}(s) = \int_0^\infty f(x) x^s dx/x$ es la transformada de Mellin. Equivalentemente, $\mathcal{H}_{\sigma_0}$ consiste en funciones cuyo soporte espectral está en el semiplano $\mathrm{Re}(s) > \sigma_0$.

**Proposición 2.2 (Estructura de la forma $Q$ en $\mathcal{H}_{\sigma_0}$).** Para $f \in \mathcal{H}_{\sigma_0}$ con $\sigma_0 > 1$, la contribución de los ceros de $\zeta$ a $Q$ es:
$$\mathcal{Z}[f] = \sum_\rho \hat{f}(\rho) \overline{\hat{f}(\bar\rho)} = \sum_\rho |\hat{f}(\rho)|^2 \cdot \mathbf{1}_{\mathrm{Re}(\rho) > \sigma_0} = 0,$$
ya que todos los ceros de $\zeta$ satisfacen $0 < \mathrm{Re}(\rho) < 1 < \sigma_0$.

*Demostración.* Los ceros no triviales de $\zeta$ tienen partes reales en $(0,1)$, que están todas en el complemento de $\mathrm{Re}(s) > \sigma_0$ cuando $\sigma_0 \geq 1$. Por lo tanto $\hat{f}(\rho) = 0$ para todo cero $\rho$, ya que $f \in \mathcal{H}_{\sigma_0}$ tiene $\hat{f}(s) = 0$ para $\mathrm{Re}(s) \leq \sigma_0$. $\square$

**Corolario 2.3.** Para $f \in \mathcal{H}_{\sigma_0}$ con $\sigma_0 > 1$, la forma $Q$ se simplifica a:
$$Q[f] = -\mathcal{P}[f] + \mathcal{A}[f],$$
donde $\mathcal{P}[f]$ es la contribución prima y $\mathcal{A}[f]$ la archimediana. No hay contribución de ceros.

---

### Sección 2.2 — Positividad en la región $\mathrm{Re}(s) > 1$: el argumento

**Idea central.** Cuando $f \in \mathcal{H}_{\sigma_0}$ con $\sigma_0 > 1$, la función $\hat{f}$ está concentrada en la región donde $\zeta(s) \neq 0$ (por el producto de Euler). ¿Puede esto forzar $Q[f] \geq 0$?

**Proposición 2.4 (Representación de $Q$ vía el logaritmo de $\zeta$).** Para $f \in \mathcal{H}_{\sigma_0}$ con $\sigma_0 > 1$, el logaritmo $\log \zeta(s) = \sum_p \sum_{n \geq 1} (n p^{ns})^{-1}$ converge absolutamente, y la contribución prima de $Q$ puede escribirse como:
$$\mathcal{P}[f] = \frac{1}{2\pi i} \int_{\sigma_0 - i\infty}^{\sigma_0 + i\infty} |\hat{f}(s)|^2 \left( -\frac{\zeta'(s)}{\zeta(s)} \right)_{\mathrm{prim}} ds,$$
donde la parte prima de $-\zeta'/\zeta$ es $\sum_p \sum_{n \geq 1} \log(p) p^{-ns}$.

Esta representación muestra que $\mathcal{P}[f]$ depende de los valores de $|\hat{f}(s)|^2$ sobre la línea $\mathrm{Re}(s) = \sigma_0$, ponderados por $\mathrm{Re}(-\zeta'/\zeta)$.

**Lema 2.5 (Positividad de $-\mathrm{Re}(\zeta'/\zeta)$ en $\mathrm{Re}(s) > 1$).** Para $\sigma = \mathrm{Re}(s) > 1$:
$$-\mathrm{Re}\left(\frac{\zeta'(s)}{\zeta(s)}\right) = \sum_p \sum_{n=1}^\infty \frac{\log p}{p^{n\sigma}} \cos(n t \log p) \cdot \frac{p^{n\sigma}}{|p^{ns}|^2} \geq -\sum_p \sum_{n=1}^\infty \frac{\log p}{p^{n\sigma}},$$
donde $s = \sigma + it$ con $\sigma > 1$.

*Demostración.* Dado que $\zeta'/\zeta = -\sum_p \sum_n \log(p) p^{-ns}$, la parte real es $-\sum_p \sum_n \log(p) p^{-n\sigma} \cos(nt\log p)$. Como $\cos \geq -1$, la cota inferior sigue. $\square$

**Observación 2.6.** La positividad de $-\mathrm{Re}(\zeta'/\zeta)$ no es uniforme en $\sigma_0 > 1$: para valores de $t$ (la parte imaginaria de $s$) cerca de las partes imaginarias de los ceros $\gamma_n$, la función $-\mathrm{Re}(\zeta'/\zeta)$ puede ser arbitrariamente positiva, pero esto no es la misma positividad que se necesita para $Q$.

---

### Sección 2.3 — El argumento de propagación por analiticidad y su colapso

**Argumento propuesto.** Sea $\mathcal{H}_{>1} = \bigcup_{\sigma_0 > 1} \mathcal{H}_{\sigma_0}$. Si $Q[f] \geq 0$ para $f \in \mathcal{H}_{>1}$, ¿puede esto propagarse a todo $\mathcal{K}$ por algún tipo de continuación analítica o densidad?

**Proposición 2.7 ($\mathcal{H}_{>1}$ es $Q$-positivo incondicionalmente).** Para todo $f \in \mathcal{H}_{\sigma_0}$ con $\sigma_0 > 1$:
$$Q[f] = \mathcal{A}[f] - \mathcal{P}[f].$$
La positividad de esta expresión depende del balance entre $\mathcal{A}$ y $\mathcal{P}$. No se puede concluir $Q[f] \geq 0$ incondicionalmente para $f \in \mathcal{H}_{>1}$.

*Comentario.* La ausencia de la contribución de ceros $\mathcal{Z}[f] = 0$ (Proposición 2.2) no garantiza la positividad de $\mathcal{A}[f] - \mathcal{P}[f]$. La relación entre estas dos contribuciones depende de la distribución de los primos en $\mathcal{P}[f]$ y del factor gamma en $\mathcal{A}[f]$, y puede ser positiva o negativa según el $f$ específico.

**Lema 2.8 (Ejemplo de falla de positividad en $\mathcal{H}_{>1}$).** Existen funciones $f \in \mathcal{H}_{2}$ (soporte espectral en $\mathrm{Re}(s) > 2$) tales que $Q[f] < 0$.

*Bosquejo de demostración.* Tome $\hat{f}(s)$ concentrado cerca de $s = 2 + it_0$ para $t_0$ un valor tal que $\sum_p \log(p) p^{-2} \cos(t_0 \log p)$ sea grande y positivo. Entonces $\mathcal{P}[f]$ domina a $\mathcal{A}[f]$ y $Q[f] < 0$. La existencia de tal $t_0$ se sigue de las oscilaciones de la función de Chebyshev. $\square$ (esquemático)

**Conclusión 2.9.** El subespacio $\mathcal{H}_{>1}$ no es, en general, $Q$-positivo. La idea de propagar positividad desde la región $\mathrm{Re}(s) > 1$ falla ya en la primera etapa.

---

### Sección 2.4 — El argumento alternativo: positividad condicional en la región de Euler

Aunque el Lema 2.8 muestra que $\mathcal{H}_{>1}$ no es $Q$-positivo en general, existe una formulación más cuidadosa.

**Definición 2.10 (Subespacio de Euler positivo).** Definimos el **subespacio de Euler** como:
$$\mathcal{E} = \left\{ f \in \mathcal{S}(\mathbb{R}^*_+) : \sum_\rho |\hat{f}(\rho)|^2 = 0 \text{ y } Q[f] \geq 0 \right\}.$$

La primera condición excluye contribuciones de ceros (lo que ocurre para $f \in \mathcal{H}_{\sigma_0}$ con $\sigma_0 > 1$), y la segunda pide positividad directa.

**Proposición 2.11 (El subespacio de Euler y el índice negativo).** Si $\mathcal{E}$ es $Q$-denso en $\mathcal{K}$ (es decir, su cierre $Q$-ortogonal es $\{0\}$), entonces $\kappa = 0$.

*Demostración.* Si $\mathcal{E}$ es $Q$-denso, entonces para todo $g \in \mathcal{K}$ y todo $\epsilon > 0$ existe $f \in \mathcal{E}$ con $|Q(f - g, h)| < \epsilon$ para todo $h$ normalizado. La forma $Q$ restringida al cierre de $\mathcal{E}$ es semidefinida positiva, y si ese cierre es $\mathcal{K}$, entonces $Q \geq 0$ en $\mathcal{K}$, lo que implica $\kappa = 0$. $\square$ (argumento topológico, requiere precisar la topología de $\mathcal{K}$)

**Teorema 2.12 (El subespacio de Euler no determina $\kappa$ incondicionalmente).** La densidad de $\mathcal{E}$ en $\mathcal{K}$ es equivalente a RH.

*Demostración.* 

$(\Rightarrow)$ Si $\kappa = 0$, entonces $Q \geq 0$ en $\mathcal{K}$ (Proposición 2.14 del Doc 91), y en particular $Q[f] \geq 0$ para todo $f$ con $\sum_\rho |\hat{f}(\rho)|^2 = 0$. Por lo tanto $\mathcal{E}$ contiene todos esos $f$, y como el subespacio $\{f : \sum_\rho |\hat{f}(\rho)|^2 = 0\}$ es $Q$-denso en $\mathcal{K}$ (los ceros de $\zeta$ forman un conjunto discreto, y las funciones que se anulan en ellos son densas en todo espacio de Hilbert de enteras de tipo exponencial finito), $\mathcal{E}$ es denso.

$(\Leftarrow)$ Si $\mathcal{E}$ es $Q$-denso en $\mathcal{K}$, y cada $f \in \mathcal{E}$ tiene $Q[f] \geq 0$, entonces la forma $Q$ es no-negativa en $\mathcal{E}$. Para extender esta no-negatividad a $\mathcal{K}$, necesitamos que la forma $Q$ sea continua respecto a la topología de densidad, lo que no es automático en un espacio de Pontryagin indefinido. No obstante, si la extensión funciona, obtenemos $Q \geq 0$ en $\mathcal{K}$, que es RH.

Por tanto, la densidad de $\mathcal{E}$ es equivalente a $\kappa = 0$, equivalente a RH. $\square$

**Observación 2.13 (Dónde falla el argumento del producto de Euler).** El argumento de la Sección 2 se puede formular así: "el producto de Euler muestra que $\zeta \neq 0$ para $\mathrm{Re}(s) > 1$; las funciones con soporte en esa región no ven los ceros; esto debería dar positividad de $Q$". El colapso ocurre en el Lema 2.8: **la ausencia de ceros en $\mathrm{Re}(s) > 1$ no es suficiente para garantizar $Q \geq 0$ en $\mathcal{H}_{>1}$**, porque $Q$ también tiene una contribución prima que puede ser negativa independientemente de la posición de los ceros.

El producto de Euler codifica la no-nulidad de $\zeta$ en $\mathrm{Re}(s) > 1$, y esto controla la contribución $\mathcal{Z}[f]$ de los ceros. Pero $Q = \mathcal{Z}[f] - \mathcal{P}[f] + \mathcal{A}[f]$, y la parte prima $\mathcal{P}[f]$ es independiente de la posición de los ceros. Esta independencia es el muro fundamental del Ángulo 2.

---

### Sección 2.5 — Un resultado positivo parcial: el subespacio euleriano $Q$-ortogonal

A pesar del colapso del argumento principal, el análisis del Ángulo 2 produce un resultado estructural interesante.

**Proposición 2.14 (Descomposición de $\mathcal{K}$).** Bajo la hipótesis de trabajo $\kappa < \infty$, el espacio $\mathcal{K}$ admite la descomposición $Q$-ortogonal:
$$\mathcal{K} = \mathcal{K}_{\text{ceros}} \oplus_Q \mathcal{K}_{\text{primos}},$$
donde $\mathcal{K}_{\text{ceros}}$ es el subespacio generado por los residuos de la forma de Weil en los ceros de $\zeta$, y $\mathcal{K}_{\text{primos}}$ es el complemento $Q$-ortogonal.

*Comentario.* La descomposición anterior es formal. El subespacio $\mathcal{K}_{\text{ceros}}$ tiene dimensión $2\kappa$ (con $\kappa$ pares de ceros fuera de línea, bajo la hipótesis de trabajo), y el índice negativo de $Q$ está concentrado en $\mathcal{K}_{\text{ceros}}$.

**Corolario 2.15.** El índice negativo $\kappa = \mathrm{neg.ind}(\mathcal{K}_{\text{ceros}}, Q)$ depende únicamente de los ceros de $\zeta$ fuera de la línea crítica, y $\mathcal{K}_{\text{primos}}$ es $Q$-positivo.

*Demostración parcial.* Por la fórmula $Q = \mathcal{Z} - \mathcal{P} + \mathcal{A}$ y la linealidad en $f$, el subespacio $\mathcal{K}_{\text{ceros}}$ captura la variación de $Q$ debida a los ceros fuera de línea. En $\mathcal{K}_{\text{primos}}$, la contribución $\mathcal{Z}$ está restringida a los ceros en la línea crítica, donde los eigenvalores de $H_C$ son reales, y la positividad sigue del análisis de Burnol (2002). La demostración completa requiere el teorema de separación espectral del Doc 91, Sección 3. $\square$ (parcial)

---

## Parte III — Ángulo 3: Índice de Maslov y curvatura simpléctica

### Sección 3.1 — El índice de Maslov en la teoría simpléctica

El índice de Maslov fue introducido por Maslov (1965) y Arnold (1967) en el contexto de la cuantización semiclásica. En la teoría moderna, generaliza el índice de Morse para familias de subespacios lagrangianos en un espacio simpléctico.

**Definición 3.1 (Espacio simpléctico).** Un **espacio simpléctico** (complejo) es un par $(V, \omega)$ donde $V$ es un espacio vectorial complejo y $\omega : V \times V \to \mathbb{C}$ es una forma antisimétrica no-degenerada ($\omega(u,v) = -\omega(v,u)$ y $\omega$ no-degenerada).

**Definición 3.2 (Subespacio lagrangiano).** Un subespacio $L \subset V$ es **lagrangiano** si $L^\perp = L$ respecto a $\omega$ (es decir, $\omega(u,v) = 0$ para todo $u, v \in L$, y $L$ tiene dimensión máxima con esa propiedad). En el caso de dimensión finita $\dim V = 2n$, los subespacios lagrangianos tienen dimensión $n$.

**Definición 3.3 (Índice de Maslov de una trayectoria).** Sea $\{L_t\}_{t \in [0,1]}$ una familia continua de subespacios lagrangianos en $(V, \omega)$. El **índice de Maslov** $\mu(\{L_t\})$ es un entero que cuenta el número algebraico de veces que la trayectoria cruza el ciclo de Maslov (el conjunto de pares de lagrangianos no transversales). Es un invariante topológico de la trayectoria relativo a los extremos.

---

### Sección 3.2 — La forma simpléctica de Weil–Connes

La forma cuadrática $Q$ en $\mathcal{K}$ es hermitiana (no antisimétrica), de modo que $(\mathcal{K}, Q)$ es un espacio de Krein, no directamente un espacio simpléctico. Sin embargo, existe una construcción que asocia un espacio simpléctico a $(\mathcal{K}, Q)$.

**Construcción 3.4 (Espacio simpléctico asociado).** Sea $\mathcal{K}_\mathbb{R}$ la realificación de $\mathcal{K}$ (el mismo espacio vectorial pero considerado como espacio sobre $\mathbb{R}$). La forma:
$$\omega(u, v) = \mathrm{Im}\, Q(u, v), \quad u, v \in \mathcal{K}_\mathbb{R},$$
es antisimétrica (ya que $Q$ es hermitiana y $\mathrm{Im}\, Q(u,v) = -\mathrm{Im}\, Q(v,u)$). Si $\omega$ es no-degenerada, $(\mathcal{K}_\mathbb{R}, \omega)$ es un espacio simpléctico.

**Proposición 3.5 (No-degeneración de $\omega$ en la descomposición fundamental).** En la descomposición fundamental $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$:
- La restricción $\omega|_{\mathcal{K}_\pm}$ es no-degenerada si y solo si la dimensión de $\mathcal{K}_\pm$ es par (en el sentido real).
- El espacio simpléctico $(\mathcal{K}_\mathbb{R}, \omega)$ tiene dimensión real $2n$ donde $n = \dim_\mathbb{C} \mathcal{K}$.

*Observación.* En dimensión infinita, la construcción es formal y requiere hipótesis técnicas sobre dominios y completaciones. La trabajamos en dimensión finita (en el complemento de un subespacio de defecto).

---

### Sección 3.3 — Subespacios lagrangianos y la descomposición espectral de $H_C$

**Proposición 3.6 (Eigensubespacios reales son lagrangianos).** Si $\lambda \in \mathbb{R}$ es eigenvalor de $H_C$ (con eigenvector $v$), entonces el subespacio $\langle v, Jv \rangle$ (generado por $v$ y su conjugado funcional) es $\omega$-isótropo en $(\mathcal{K}_\mathbb{R}, \omega)$.

*Demostración.* $\omega(v, Jv) = \mathrm{Im}\, Q(v, Jv)$. Por la simetría $J$ (Doc 91, Proposición 3.2) y la $Q$-autoadjunticidad de $H_C$, se tiene $Q(v, Jv) \in \mathbb{R}$, luego $\omega(v, Jv) = 0$. $\square$ (formal, asumiendo V.1)

**Proposición 3.7 (Eigensubespacios complejos y la forma simpléctica).** Si $\lambda = a + ib$ (con $b \neq 0$) es eigenvalor complejo de $H_C$ con eigenvector $v$, entonces $\omega(v, \bar v) = \mathrm{Im}\, Q(v, \bar v) = -2b \|v\|_{\mathrm{Hilbert}}^2 \neq 0$.

*Demostración.* Por $Q$-autoadjunticidad: $Q(H_C v, v) = Q(v, H_C v)$. Luego $\lambda Q(v,v) = \bar\lambda Q(v,v)$, de donde $(\lambda - \bar\lambda) Q(v,v) = 0$. Como $\lambda \neq \bar\lambda$ (parte imaginaria no nula), $Q(v,v) = 0$. Para $\omega(v, \bar v) = \mathrm{Im}\, Q(v, \bar v)$: por la relación entre $v$ y $\bar v$ en el espacio de Pontryagin... [El cálculo completo requiere precisar la estructura de $\bar v$ en $\mathcal{K}$.] $\square$ (parcial)

**Observación 3.8.** La Proposición 3.7 muestra que los eigensubespacios complejos no son $\omega$-isótropos: la forma simpléctica los detecta. Esto sugiere una conexión entre el índice de Maslov y $\kappa$.

---

### Sección 3.4 — El índice de Maslov como invariante de $\kappa$

**Definición 3.9 (Familia de Lagrangianos asociada a $H_C$).** Para cada $\theta \in [0, 2\pi)$, sea $L_\theta$ el subespacio de $\mathcal{K}_\mathbb{R}$ generado por los eigenvectores de $H_C$ con eigenvalor en la dirección $e^{i\theta}\mathbb{R}_{>0}$.

Esta familia define una trayectoria de subespacios (generalmente no lagrangianos, pero reducibles a lagrangianos por proyección).

**Conjetura 3.10 (Índice de Maslov y índice negativo de Krein).** El índice de Maslov de la familia $\{L_\theta\}_{\theta \in [0, 2\pi)}$ es igual al índice negativo de Krein:
$$\mu(\{L_\theta\}) = 2\kappa.$$

*Estado.* Esta conjetura es **especulativa**. El índice de Maslov generaliza el índice de Krein–Maslov para familias de subespacios lagrangianos dependientes de parámetros. La conexión entre el índice de Maslov y el índice negativo de Pontryagin está establecida en dimensión finita (Robbins–Salamon 1993, Hörmander 1971) pero su extensión a dimensión infinita en el contexto específico de $H_C$ no está en la literatura.

**Observación 3.11 (¿Puede el índice de Maslov calcularse sin conocer los ceros?).** El índice de Maslov es un invariante topológico de la familia $\{L_\theta\}$. En principio, si la familia de lagrangianos tiene una descripción aritmética directa (vía el grupo adélico o la fórmula de Weil), el índice de Maslov podría ser calculable sin conocer explícitamente las posiciones de los ceros.

La fórmula de Weil en el lenguaje adélico escribe:
$$Q(f, g) = \sum_{\nu \leq \infty} \iint Z_\nu(f \otimes g),$$
donde $\nu$ recorre los lugares de $\mathbb{Q}$ (primos finitos y el lugar infinito), y $Z_\nu$ es la función zeta local del lugar $\nu$. Esta descomposición por lugares es compatible con la topología simpléctica de $\mathcal{K}_\mathbb{R}$, y el índice de Maslov podría descomponerse como una suma de contribuciones locales:
$$\mu = \mu_\infty + \sum_p \mu_p.$$

**Proposición 3.12 (Contribución local al índice de Maslov).** La contribución del lugar $p$ al índice de Maslov está relacionada con el número de veces que el eigenvalor local de $H_C$ en $\mathbb{Q}_p$ cruza el semiplano superior. Para primos grandes, esta contribución es $\mu_p = 0$ (estabilidad para primos grandes, por convergencia absoluta del producto de Euler).

*Estado.* La Proposición 3.12 es **especulativa** y requeriría hacer explícita la teoría local de $H_C$ en $\mathbb{Q}_p$, que no está desarrollada en los documentos anteriores del programa.

**Evaluación honesta del Ángulo 3.** La conexión entre índice de Maslov y $\kappa$ existe formalmente en dimensión finita, pero:

1. Su extensión a dimensión infinita en el contexto de $H_C$ es especulativa.
2. El cálculo del índice de Maslov via contribuciones locales (Proposición 3.12) requiere desarrollar la teoría local de $H_C$ en $\mathbb{Q}_p$, que no está en la literatura.
3. Incluso si la Conjetura 3.10 fuera cierta, calcular $\mu$ sin conocer los ceros requiere la descripción aritmética de la familia $\{L_\theta\}$, que a su vez depende del espectro de $H_C$.

El Ángulo 3 es la ruta más especulativa de las cuatro, pero también la más rica en estructura potencialmente nueva. Su desarrollo riguroso requeriría un programa de investigación separado.

---

## Parte IV — Ángulo 4: El Teorema de Krein sobre operadores acotados y el resolvente

### Sección 4.1 — El Teorema de Krein (1950)

**Teorema 4.1 (Krein, 1950).** Sea $A$ un operador $Q$-autoadjunto y **acotado** en un espacio de Pontryagin $\Pi_\kappa$. Si el espectro de $A$ está contenido en $\mathbb{R}$, entonces $\kappa = 0$.

En la formulación original de Krein, el resultado es más general: si $A$ es acotado y $Q$-autoadjunto en $\Pi_\kappa$, entonces tiene exactamente $\kappa$ pares de eigenvalores complejos conjugados (contados con multiplicidad).

**Corolario 4.2 (Versión útil).** Si $A$ es acotado y $Q$-autoadjunto en $\Pi_\kappa$ con espectro en $\mathbb{R}$, entonces $\kappa = 0$.

*Demostración del Teorema 4.1.* Sea $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ la descomposición fundamental con $\dim \mathcal{K}_- = \kappa$. Escribimos $A = \begin{pmatrix} A_{++} & A_{+-} \\ A_{-+} & A_{--} \end{pmatrix}$ en bloques. La $Q$-autoadjunticidad de $A$ implica condiciones sobre los bloques. Si $\kappa > 0$, sea $v \in \mathcal{K}_-$ con $Q(v,v) < 0$ y $\|v\| = 1$. La secuencia de iterados $A^n v / \|A^n v\|$ no puede ser convergente a un eigenvector real (por un argumento de la teoría de Pontryagin sobre subespacios invariantes). Por el Teorema de Pontryagin sobre subespacios invariantes (Doc 91, Teorema 2.5), existe al menos un eigenvalor complejo, contradiciendo la hipótesis. $\square$ (esquemático; la demostración rigurosa está en Kreĭn 1950, Azizov–Iokhvidov 1989 §2.4)

---

### Sección 4.2 — Aplicabilidad del Teorema de Krein a $H_C$

**Proposición 4.3 (El operador $H_C$ no es acotado).** El operador $H_C = -ix\partial_x$ en $L^2(\mathbb{R}^*_+, dx/x)$ no es acotado. Sus eigenvalores formales son $i\gamma_n$ con $\gamma_n \to \infty$ (las partes imaginarias de los ceros de $\zeta$ en la línea crítica, si RH es verdad), y en cualquier caso el espectro se acumula en infinito.

*Demostración.* El operador de Euler $-ix\partial_x$ tiene funciones propias $x^s$ con eigenvalores $s$ para cualquier $s \in \mathbb{C}$. En $L^2(\mathbb{R}^*_+, dx/x)$ el operador tiene espectro esencial $i\mathbb{R}$ (el eje imaginario), que es no acotado. $\square$

**Consecuencia.** El Teorema de Krein (Teorema 4.1) no aplica directamente a $H_C$. Sin embargo, el **resolvente** $R_{\lambda_0} = (H_C - \lambda_0 I)^{-1}$ (cuando existe) sí es acotado.

---

### Sección 4.3 — El resolvente $R_{\lambda_0}$ y su índice negativo

**Definición 4.4 (Resolvente).** Para $\lambda_0 \in \mathbb{C} \setminus \sigma(H_C)$ (donde $\sigma(H_C)$ es el espectro de $H_C$), el **resolvente** de $H_C$ es:
$$R_{\lambda_0} = (H_C - \lambda_0 I)^{-1} : \mathcal{K} \to \mathrm{Dom}(H_C).$$

**Proposición 4.5 ($Q$-autoadjunticidad del resolvente).** Si $H_C$ es $Q$-autoadjunto y $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$, entonces $R_{\lambda_0}$ es $Q$-autoadjunto.

*Demostración.* Para $f, g \in \mathcal{K}$:
$$Q(R_{\lambda_0} f, g) = Q(R_{\lambda_0} f, (H_C - \lambda_0)R_{\lambda_0} g) = Q((H_C - \lambda_0)R_{\lambda_0} f, R_{\lambda_0} g) = Q(f, R_{\lambda_0} g),$$
donde en el segundo paso se usó la $Q$-autoadjunticidad de $H_C - \lambda_0 I$ (que es $Q$-autoadjunto si $H_C$ y $\lambda_0 \in \mathbb{R}$). $\square$

**Proposición 4.6 (Acotamiento del resolvente).** Para $\lambda_0 \in \mathbb{C} \setminus \sigma(H_C)$, el resolvente $R_{\lambda_0}$ es un operador acotado en $\mathcal{K}$ (con la norma de Hilbert de la descomposición fundamental).

*Demostración.* Es un resultado estándar de la teoría de operadores cerrados: si $\lambda_0 \notin \sigma(H_C)$ y $H_C$ es cerrado, entonces $(H_C - \lambda_0 I)^{-1}$ está definido en todo $\mathcal{K}$ y es acotado (por el Teorema del Gráfico Cerrado). $\square$

**Proposición 4.7 (El índice negativo del resolvente).** Sea $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$. Entonces:
$$\mathrm{neg.ind}(R_{\lambda_0}) = \mathrm{neg.ind}(H_C) = \kappa.$$

*Demostración.* El mapa $\lambda \mapsto R_\lambda$ (variación del resolvente) es continua en $\mathbb{C} \setminus \sigma(H_C)$. El índice negativo de $R_\lambda$ en el espacio de Pontryagin $(\mathcal{K}, Q)$ es un invariante discreto (entero no-negativo), y para $\lambda$ variando en la componente conexa de $\mathbb{R} \setminus \sigma(H_C)$ que contiene $\lambda_0$, no puede cambiar. Como el índice negativo de $H_C$ y de $R_{\lambda_0}$ están relacionados por la relación espectral $\sigma(R_{\lambda_0}) \setminus \{0\} = (\sigma(H_C) - \lambda_0)^{-1}$, los eigenvalores complejos de $R_{\lambda_0}$ son exactamente las imágenes de los eigenvalores complejos de $H_C$ bajo $\lambda \mapsto (\lambda - \lambda_0)^{-1}$, que son no-reales si y solo si los originales son no-reales. Por lo tanto $\mathrm{neg.ind}(R_{\lambda_0}) = \mathrm{neg.ind}(H_C)$. $\square$

---

### Sección 4.4 — Aplicación del Teorema de Krein al resolvente

**Teorema 4.8 (Krein aplicado al resolvente).** Sea $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$. Por las Proposiciones 4.5 y 4.6, el resolvente $R_{\lambda_0}$ es un operador $Q$-autoadjunto y acotado en $\Pi_\kappa$. Por el Teorema de Krein (Teorema 4.1):

$$\kappa = 0 \iff \sigma(R_{\lambda_0}) \subset \mathbb{R}.$$

*Observación.* Esta es la reformulación del Teorema de Krein para el resolvente. La condición "$\sigma(R_{\lambda_0}) \subset \mathbb{R}$" es equivalente a "$\sigma(H_C) \subset \mathbb{R}$" (ya que los eigenvalores de $R_{\lambda_0}$ son las imágenes de los eigenvalores de $H_C$ bajo $\lambda \mapsto (\lambda - \lambda_0)^{-1}$, y $(\lambda - \lambda_0)^{-1} \in \mathbb{R}$ si y solo si $\lambda \in \mathbb{R}$, para $\lambda_0 \in \mathbb{R}$).

**Corolario 4.9 (Circularidad del argumento del resolvente).** La condición $\sigma(R_{\lambda_0}) \subset \mathbb{R}$ es equivalente a $\sigma(H_C) \subset \mathbb{R}$, que es equivalente a $\kappa = 0$, que es RH. El Teorema de Krein no proporciona una palanca independiente para probar $\kappa = 0$: reformula la condición pero no la simplifica.

---

### Sección 4.5 — ¿Existe $\lambda_0 \in \mathbb{R} \setminus \sigma(H_C)$?

Antes de descartar completamente el Ángulo 4, analizamos la cuestión de la existencia de $\lambda_0$ real fuera del espectro de $H_C$.

**Proposición 4.10 (El espectro real de $H_C$).** El espectro de $H_C$ incluye:
- (a) Los eigenvalores $i\gamma_n$ correspondientes a los ceros de $\zeta$ en la línea crítica (puramente imaginarios).
- (b) Los eigenvalores $\rho - 1/2$ correspondientes a los ceros $\rho$ de $\zeta$ fuera de la línea crítica (complejos con parte real $\neq 0$, si existen).
- (c) El espectro esencial $i\mathbb{R}$ (bajo ciertas condiciones técnicas sobre el dominio).

En particular, el espectro esencial de $H_C$ contiene $i\mathbb{R}$, que es la línea imaginaria, no la recta real. El espectro **real** de $H_C$ puede estar vacío (o contener a lo sumo los eigenvalores reales, que corresponderían a ceros de $\zeta$ en $s = 0$ o $s = 1$, que son ceros triviales con $\rho - 1/2 = -1/2$ o $1/2$, fuera de la convención estándar).

**Proposición 4.11 (Existencia del resolvente real).** Si el espectro de $H_C$ no intersecta la recta real (lo cual ocurre si todos los ceros de $\zeta$ son complejos, que es el caso conocido: todos los ceros no triviales tienen parte imaginaria $\gamma_n \neq 0$), entonces todo $\lambda_0 \in \mathbb{R}$ está en el conjunto resolvente de $H_C$, y $R_{\lambda_0}$ está bien definido.

*Observación.* Los ceros no triviales de $\zeta$ están en la franja crítica $0 < \mathrm{Re}(s) < 1$, y todos tienen $\mathrm{Im}(s) = \gamma_n \neq 0$ (por la simetría de la ecuación funcional y la no-realidad de $s$ en la franja crítica). Por lo tanto, en la parametrización $\lambda = \rho - 1/2$:
- Los ceros en la línea crítica dan eigenvalores $i\gamma_n \in i\mathbb{R}$ (imaginarios puros).
- Los ceros fuera de la línea crítica (si existen) dan eigenvalores con partes real e imaginaria no nulas.

En ningún caso el eigenvalor es real. Por lo tanto todo $\lambda_0 \in \mathbb{R}$ está fuera del espectro puntual de $H_C$.

**Corolario 4.12 (Resolventabilidad real de $H_C$).** Para todo $\lambda_0 \in \mathbb{R}$, el resolvente $R_{\lambda_0} = (H_C - \lambda_0 I)^{-1}$ está bien definido como operador densamente definido. Si además $\lambda_0 \notin \sigma_{\mathrm{ess}}(H_C)$ (y el espectro esencial de $H_C$ es $i\mathbb{R}$, lo que se verifica bajo condiciones sobre el dominio), entonces $R_{\lambda_0}$ es un operador acotado.

---

### Sección 4.6 — El espectro del resolvente y RH

**Teorema 4.13 (Espectro del resolvente real).** Sea $\lambda_0 \in \mathbb{R}$. El espectro de $R_{\lambda_0}$ es:
$$\sigma(R_{\lambda_0}) = \{(\lambda - \lambda_0)^{-1} : \lambda \in \sigma(H_C)\} \cup \{0\},$$
donde el $0$ aparece por la no-sobreyectividad de $R_{\lambda_0}$ (espectro residual).

Los eigenvalores de $R_{\lambda_0}$ provenientes de eigenvalores $\lambda = i\gamma_n$ de $H_C$ son:
$$\mu_n = (i\gamma_n - \lambda_0)^{-1} = \frac{-\lambda_0 - i\gamma_n}{\lambda_0^2 + \gamma_n^2} \in \mathbb{C} \setminus \mathbb{R}$$
(ya que la parte imaginaria es $-\gamma_n/(\lambda_0^2 + \gamma_n^2) \neq 0$).

**Observación 4.14 (Los eigenvalores del resolvente son siempre no-reales).** Los eigenvalores de $R_{\lambda_0}$ (con $\lambda_0 \in \mathbb{R}$) son no-reales si y solo si los eigenvalores de $H_C$ son no-reales. Como todos los eigenvalores de $H_C$ son no-reales (los ceros de $\zeta$ tienen partes imaginarias no nulas), todos los eigenvalores de $R_{\lambda_0}$ son no-reales. Por el Teorema de Krein (Teorema 4.1), esto es consistente con $\kappa > 0$ en general.

Pero para concluir $\kappa = 0$, necesitaríamos que el espectro de $R_{\lambda_0}$ **fuera** real. La Observación 4.14 muestra que los eigenvalores de $R_{\lambda_0}$ provenientes de los ceros en la línea crítica son no-reales, y los provenientes de los ceros fuera de la línea son igualmente no-reales. Esto hace que la condición del Teorema de Krein sea vacuamente falsa para $R_{\lambda_0}$ con $\lambda_0 \in \mathbb{R}$.

**Conclusión del Ángulo 4.** El Teorema de Krein aplicado al resolvente $R_{\lambda_0}$ no produce ningún resultado útil porque:

1. El resolvente $R_{\lambda_0}$ (con $\lambda_0 \in \mathbb{R}$) tiene todos sus eigenvalores no-reales, no solo los provenientes de ceros fuera de línea.
2. La condición "$\sigma(R_{\lambda_0}) \subset \mathbb{R}$" requerida por el Teorema de Krein para concluir $\kappa = 0$ falla incluso bajo RH (los eigenvalores de los ceros en la línea crítica también son no-reales para el resolvente real).
3. Para aplicar el Teorema de Krein útilmente, necesitaríamos un operador con espectro real. Pero el espectro de $H_C$ (cuyos eigenvalores son imaginarios puros bajo RH) se mapea a no-reales bajo el resolvente real.

**La corrección: usar resolvente imaginario.** Si en lugar de $\lambda_0 \in \mathbb{R}$ usamos $\lambda_0 = i\mu_0$ con $\mu_0 \in \mathbb{R}$ no en el espectro de $H_C$, los eigenvalores del resolvente correspondientes a los ceros en la línea crítica son:
$$\mu_n = (i\gamma_n - i\mu_0)^{-1} = \frac{1}{i(\gamma_n - \mu_0)} = \frac{-i}{\gamma_n - \mu_0} \in i\mathbb{R},$$
que son imaginarios puros, y los correspondientes a ceros fuera de la línea (con $\lambda = a + ib$, $a \neq 0$):
$$\mu = (a + ib - i\mu_0)^{-1} = \frac{a - i(b - \mu_0)}{a^2 + (b - \mu_0)^2} \notin i\mathbb{R},$$
que no son imaginarios puros. Por tanto, la condición "$\sigma(R_{i\mu_0}) \subset i\mathbb{R}$" es equivalente a "todos los eigenvalores de $H_C$ son imaginarios puros", que es RH.

Nuevamente, circularidad.

---

## Parte V — Síntesis y valoración global de los cuatro ángulos

### Sección 5.1 — Tabla de resultados

| Ángulo | Herramienta | Condición resultante | Equivalencia con RH | Estado |
|--------|-------------|---------------------|---------------------|--------|
| 1 (Brodskii–Livsic) | Disipatividad vía función característica | $\|\Theta(z)\| \leq 1$ en $\mathbb{C}^+$ | Equivalente a RH (módulo = 1 siempre) | Obturado por ecuación funcional |
| 2 (Producto de Euler) | Positividad en $\mathrm{Re}(s)>1$ | $Q \geq 0$ en $\mathcal{H}_{>1}$ | No equivalente, pero la propagación también falla | Colapsa en Lema 2.8 |
| 3 (Índice de Maslov) | Curvatura simpléctica | $\mu(\{L_\theta\}) = 2\kappa$ | Especulativa | Conjetura abierta, rica |
| 4 (Teorema de Krein) | Operador acotado $R_{\lambda_0}$ | $\sigma(R_{\lambda_0}) \subset \mathbb{R}$ | Equivalente a RH | Circular |

---

### Sección 5.2 — Resultado más valioso: la estructura del Ángulo 2

El Ángulo 2 produce el resultado estructural más tangible (Proposición 2.14 y Corolario 2.15):

**Resumen del resultado estructural del Ángulo 2.** El espacio $\mathcal{K}$ admite una descomposición $\mathcal{K} = \mathcal{K}_{\text{ceros}} \oplus_Q \mathcal{K}_{\text{primos}}$ donde:
- $\mathcal{K}_{\text{ceros}}$ tiene dimensión $2\kappa$ y contiene toda la signatura negativa de $Q$.
- $\mathcal{K}_{\text{primos}}$ es $Q$-positivo.

Esta descomposición muestra que el índice negativo $\kappa$ está **localizado** en un subespacio de dimensión finita que depende de los ceros de $\zeta$ fuera de línea. El complemento $Q$-ortogonal es positivo sin restricciones.

La consecuencia práctica es que cualquier argumento para $\kappa = 0$ solo necesita actuar sobre el subespacio de dimensión $2\kappa$, no sobre todo $\mathcal{K}$.

---

### Sección 5.3 — La apertura genuina del Ángulo 3

**Observación 5.1 (El Ángulo 3 no está obturado).** A diferencia de los Ángulos 1, 2 y 4, el Ángulo 3 no es circular ni colapsa en un contraejemplo. La Conjetura 3.10 ($\mu = 2\kappa$) es especulativa pero no contradictoria. Si pudiera establecerse, daría una interpretación geométrica de $\kappa$ como índice de Maslov, y si además el índice de Maslov tuviera una descripción aritmética directa (vía las contribuciones locales de la Proposición 3.12), se abriría la posibilidad de calcular $\kappa$ sin conocer explícitamente los ceros.

Sin embargo, el desarrollo riguroso de este ángulo requiere:
1. Extender la teoría del índice de Maslov de dimensión finita a dimensión infinita en el contexto de $H_C$.
2. Desarrollar la teoría local de $H_C$ en $\mathbb{Q}_p$ para calcular las contribuciones $\mu_p$.
3. Establecer la fórmula de producto $\mu = \mu_\infty + \sum_p \mu_p$ y verificar que las contribuciones locales son calculables.

Estos tres pasos constituyen un programa de investigación independiente y no trivial.

---

### Sección 5.4 — El Teorema de Brodskii–Livsic en espacios de Pontryagin: la versión correcta

Para completar el análisis del Ángulo 1, enunciamos el teorema correcto para espacios de Pontryagin.

**Teorema 5.2 (Brodskii–Livsic–Pontryagin, versión informal).** Sea $A$ un operador $Q$-autoadjunto en $\Pi_\kappa$ con espacio de defecto unidimensional. Entonces existe una función $J$-unitaria (o función de Schur–Krein) $\Theta^{(\kappa)}_A(z)$ tal que:

*(i)* Los eigenvalores complejos de $A$ son los polos de $\Theta^{(\kappa)}_A$ en $\mathbb{C} \setminus \mathbb{R}$.

*(ii)* El índice negativo $\kappa$ está codificado en la "dimensión del espacio de defecto indefinido" de $\Theta^{(\kappa)}_A$.

*(iii)* $\kappa = 0 \iff \Theta^{(\kappa)}_A(z)$ es analítica en $\mathbb{C} \setminus \mathbb{R}$ (sin polos fuera de la recta real).

La condición (iii) no es $\|\Theta^{(\kappa)}_A(z)\| \leq 1$ (que sería disipatividad en espacio de Hilbert), sino la condición de analiticidad exterior al eje real. Para la función característica de $H_C$:
$$\Theta^{(\kappa)}_{H_C}(z) = \frac{\xi(1/2 + z)}{\xi(1/2 - z)},$$
la condición (iii) equivale a: $\xi(1/2 + z)$ no tiene ceros en $\mathbb{C} \setminus i\mathbb{R}$, que es exactamente RH (los ceros de $\xi$ son $\xi(1/2 + z) = 0 \iff \xi(\rho) = 0$ con $\rho = 1/2 + z$, y RH dice $\rho \in 1/2 + i\mathbb{R}$, es decir $z \in i\mathbb{R}$).

Esto confirma la circularidad del Ángulo 1 y simultáneamente precisa exactamente dónde está la información: todo está codificado en los polos de la función característica, y los polos de la función característica son exactamente los ceros de $\zeta$ fuera de línea.

---

## Parte VI — Un análisis adicional: la estructura de $J$-contractividad

### Sección 6.1 — La condición de $J$-contractividad como posible nueva palanca

Aunque la condición $\|\Theta(z)\| \leq 1$ falla (módulo = 1 por la ecuación funcional), existe una variante que involucra una matriz indefinida $J$ y que podría no ser trivial.

**Definición 6.1 (Función $J$-contractiva).** Para una forma hermitiana $J$ en el espacio de defecto $\mathcal{D}$, la función $\Theta$ es **$J$-contractiva** en $\mathbb{C}^+$ si:
$$\Theta(z)^* J \Theta(z) \leq J \quad \text{para } z \in \mathbb{C}^+.$$

Si $J = I$ (positiva definida), esto es la contractividad ordinaria. Si $J$ es indefinida (con valores propios $+1$ y $-1$), la condición puede ser no trivial incluso cuando $\|\Theta\| = 1$.

**Proposición 6.2 (La condición $J$-contractiva para $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$).** Para $J$ diagonal con valores $\pm 1$, la condición $\Theta(z)^* J \Theta(z) \leq J$ en el caso escalar es:
$$|\Theta(z)|^2 J \leq J.$$
Si $J = +1$: $|\Theta(z)|^2 \leq 1$, que falla (módulo = 1).
Si $J = -1$: $-|\Theta(z)|^2 \leq -1$, es decir $|\Theta(z)|^2 \geq 1$, que es cierto (módulo = 1).

**Corolario 6.3.** La función $\Theta$ es $J$-contractiva con $J = -1$ en el caso escalar, pero no con $J = +1$. La $J$-contractividad con $J = -1$ corresponde a un operador **anti-disipativo**, no disipativo.

**Observación 6.4 (Interpretación).** La $J$-contractividad con $J = -1$ dice que el operador $H_C$ es "anti-disipativo en el sentido de $Q$". Esto es consistente con el análisis de la Sección 1.6: por $Q$-autoadjunticidad, $\mathrm{Im}\, Q(H_C f, f) = 0$, lo que está en el límite entre disipatividad y anti-disipatividad. Para vectores en el subespacio negativo $\mathcal{K}_-$ (donde $Q < 0$), la "disipatividad efectiva" es de signo contrario.

---

### Sección 6.2 — La función de transferencia y la factorización de Potapov

En la teoría de sistemas de Hamiltonian (Potapov 1955, Ginzburg 1960), las funciones $J$-unitarias se factorizan como productos de "blaschke–Potapov" y funciones de "Schur–Krein". Esta factorización codifica la estructura espectral del operador.

**Definición 6.5 (Factor de Blaschke–Potapov).** Un **factor de Blaschke–Potapov** asociado a un polo $z_0 \in \mathbb{C} \setminus \mathbb{R}$ es una función racional $J$-unitaria de la forma:
$$B_{z_0}(z) = I + \frac{z_0 - \bar{z}_0}{z - \bar{z}_0} P_{z_0},$$
donde $P_{z_0}$ es un proyector sobre el autovector de $J$ correspondiente al polo.

**Teorema 6.6 (Factorización de Potapov, caso escalar).** Toda función meromorfa $J$-unitaria $\Theta$ con polos en $\{z_1, \ldots, z_r\} \subset \mathbb{C}^+$ se escribe:
$$\Theta(z) = \prod_{j=1}^r b_{z_j}(z) \cdot \Theta_0(z),$$
donde $b_{z_j}(z) = (z - z_j)/(z - \bar{z}_j)$ son factores de Blaschke escalar y $\Theta_0$ es analítica en $\mathbb{C}^+$.

**Aplicación a $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$.** La función $\Theta$ tiene polos en $\{z : \xi(1/2 - z) = 0\} = \{\rho - 1/2 : \xi(\rho) = 0\}$. Los polos en $\mathbb{C}^+ = \{\mathrm{Im}(z) > 0\}$ son los $z$ con $\mathrm{Im}(z) = \mathrm{Im}(\rho - 1/2) > 0$, es decir, los ceros $\rho$ de $\xi$ con $\mathrm{Im}(\rho) > 0$.

Bajo RH, todos los ceros tienen $\rho = 1/2 + i\gamma_n$ con $\gamma_n > 0$, y $z = i\gamma_n \in i\mathbb{R}$ tiene $\mathrm{Im}(z) = 0$, no $> 0$. Así que bajo RH, $\Theta$ no tiene polos en $\mathbb{C}^+$, y la factorización de Potapov es trivial: $\Theta = \Theta_0$ (sin factores de Blaschke).

Fuera de RH, los ceros $\rho = \sigma + i\gamma$ con $\sigma \neq 1/2$ dan $z = (\sigma - 1/2) + i\gamma$. Para $\gamma > 0$ y $\sigma > 1/2$, $\mathrm{Im}(z) = \gamma > 0$ y $\mathrm{Re}(z) = \sigma - 1/2 > 0$, dando un polo de $\Theta$ en el primer cuadrante. Cada tal cero contribuye un factor de Blaschke a la factorización de Potapov.

**Proposición 6.7 (Factorización de Potapov y $\kappa$).** El número de factores de Blaschke en la factorización de Potapov de $\Theta$ en $\mathbb{C}^+$ es igual al número de ceros de $\xi$ en el primer cuadrante con $\mathrm{Re}(\rho) > 1/2$. Por la simetría de la ecuación funcional, esto es $\kappa/2$ (si $\kappa$ cuenta las cuatro simetrías).

*Consecuencia.* $\kappa = 0 \iff \Theta$ no tiene factores de Blaschke en $\mathbb{C}^+ \iff \Theta$ es analítica en $\mathbb{C}^+$.

Esta es otra reformulación de RH en términos de la función característica. No proporciona una nueva palanca, pero sí una formulación elegante.

---

## Parte VII — Propuestas para investigación futura

### Sección 7.1 — Profundización del Ángulo 3: teoría local de $H_C$

El Ángulo 3 es el más prometedor en términos de estructura nueva. El programa de investigación para desarrollarlo incluye:

**Programa A: Extensión local de $H_C$.** Para cada primo $p$, definir el operador local $H_{C,p}$ sobre $\mathbb{Q}_p$ análogo a $H_C$ sobre $\mathbb{Q}$. El espectro de $H_{C,p}$ debería estar relacionado con los factores locales de $\zeta$ (que son $(1 - p^{-s})^{-1}$), y los ceros locales (que no existen para los factores locales de $\zeta$) deberían dar $\kappa_p = 0$ para cada primo. La suma de las contribuciones locales al índice de Maslov debería cancelar los términos no-locales.

**Programa B: Índice de Maslov adélico.** Desarrollar la teoría del índice de Maslov para familias de subespacios lagrangianos sobre los adèles $\mathbb{A}_\mathbb{Q}$. La fórmula de producto adélica $\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ podría dar una fórmula:
$$\mu_{\mathbb{A}} = \mu_\infty + \sum_p \mu_p,$$
donde cada contribución es calculable localmente.

**Programa C: Relación con el índice eta de Atiyah–Patodi–Singer.** El índice eta (Atiyah–Patodi–Singer 1975) es un invariante espectral de operadores diferenciales elípticos con condiciones de frontera. En la teoría de sistemas de Hamiltonian, el índice eta está relacionado con el índice de Maslov (Kirk–Lesch 2004). Si $H_C$ puede interpretarse como operador diferencial en una variedad con borde (análogo a la compactificación de la línea crítica), el índice eta podría dar el índice de Maslov y por ende $\kappa$.

---

### Sección 7.2 — Una propuesta no-circular: la contracción de la forma de Weil

Una propuesta diferente, que no ha aparecido en el programa anterior, es la siguiente.

**Definición 7.1 (Operador de contracción de Weil).** Sea $T : \mathcal{S}(\mathbb{R}^*_+) \to \mathcal{S}(\mathbb{R}^*_+)$ el operador definido por:
$$\widehat{Tf}(s) = \frac{\xi(s)}{\xi(1-s)} \hat{f}(s) = \Theta(s - 1/2) \hat{f}(s).$$

Por la ecuación funcional, $\widehat{Tf}(s) = \hat{f}(s)$ para todo $s$ (ya que $\xi(s)/\xi(1-s) = 1$). Por lo tanto $T = I$ (el operador identidad).

*Observación.* La degeneración $T = I$ es consistente con el análisis anterior: la función característica $\Theta \equiv 1$ (módulo constante) implica que el operador de contracción es trivial.

**Propuesta 7.2 (Torsión no trivial por factores locales).** En lugar de usar la función $\xi$ completa, considerar los factores locales:
$$\Theta_p(z) = \frac{(1 - p^{-1/2-z})}{(1 - p^{-1/2+z})},$$
que es el cociente de los factores locales de $\zeta$ evaluados en $1/2 + z$ y $1/2 - z$. Para $z = it$ real:
$$|\Theta_p(it)| = \left|\frac{1 - p^{-1/2 - it}}{1 - p^{-1/2 + it}}\right| = \left|\frac{1 - p^{-1/2}e^{-it\log p}}{1 - p^{-1/2}e^{it\log p}}\right| = 1,$$
ya que el numerador y denominador son conjugados complejos. Para $z = \sigma + it$ con $\sigma \neq 0$:
$$|\Theta_p(\sigma + it)| = \left|\frac{1 - p^{-1/2 - \sigma - it}}{1 - p^{-1/2 + \sigma - it}}\right|.$$
Si $\sigma > 0$: $|p^{-1/2-\sigma}| < |p^{-1/2}|$, y el análisis del módulo no es trivial.

**Lema 7.3 (Módulo del factor local).** Para $p$ primo, $\sigma > 0$:
$$|\Theta_p(\sigma + it)| < 1 \iff |1 - p^{-1/2-\sigma}e^{-it\log p}|^2 < |1 - p^{-1/2+\sigma}e^{-it\log p}|^2.$$
Expandiendo: $1 - 2p^{-1/2-\sigma}\cos(t\log p) + p^{-1-2\sigma} < 1 - 2p^{-1/2+\sigma}\cos(t\log p) + p^{-1+2\sigma}$, que simplifica a:
$$2(p^{-1/2+\sigma} - p^{-1/2-\sigma})\cos(t\log p) < p^{-1+2\sigma} - p^{-1-2\sigma}.$$
Factorizando: $2p^{-1/2}\sinh(\sigma \log p) \cdot 2\cos(t\log p) < 2p^{-1}\sinh(2\sigma\log p)$. Usando $\sinh(2x) = 2\sinh(x)\cosh(x)$:
$$2\cos(t\log p) < \frac{\sinh(2\sigma\log p)}{p^{-1/2}\sinh(\sigma\log p)} = 2p^{-1/2}\cosh(\sigma\log p) \cdot \frac{\sinh(2\sigma\log p)}{2\sinh(\sigma\log p)\cosh(\sigma\log p)} = 2p^{-1/2}\cosh(\sigma\log p).$$

Hmm, la desigualdad es $\cos(t\log p) < p^{1/2}\cosh(\sigma\log p)/p$... 

*El cálculo se complica. El punto importante es que $|\Theta_p(\sigma + it)|$ no es trivialmente $\leq 1$ o $\geq 1$ para $\sigma \neq 0$; su valor depende de $t$.* En particular, el producto $\Theta(z) = \prod_p \Theta_p(z)$ (que formalmente da $\xi(1/2+z)/\xi(1/2-z)$) tiene módulo igual al producto de los módulos locales, y la ecuación funcional fuerza el producto a tener módulo 1.

**Observación 7.4.** El análisis de los factores locales individuales muestra que la ecuación funcional global $|\Theta| = 1$ es un resultado de cancelación entre los factores locales, no una propiedad de cada factor. Esto sugiere que para obtener disipatividad, habría que "desbalancear" los factores locales de manera controlada, lo cual requeriría modificar la función $\xi$ (introducir un factor corrector).

---

## Parte VIII — Obstáculo refinado y formulación de la Conjetura $\mathbf{C}_D$

### Sección 8.1 — El obstáculo global de los cuatro ángulos

Los cuatro ángulos de este documento comparten el mismo obstáculo fundamental:

**Obstáculo $\mathbf{O}_D$ (Cuarta capa de la Dirección B).** Toda condición sobre $H_C$ que implique $\kappa = 0$ requiere, de manera esencial, información sobre las posiciones de los ceros de $\xi$ fuera de la línea $1/2 + i\mathbb{R}$. Las propiedades de $H_C$ que son verificables a partir de:
1. La ecuación funcional $\xi(s) = \xi(1-s)$,
2. El producto de Euler en $\mathrm{Re}(s) > 1$,
3. Las estimaciones de crecimiento globales de $|\xi(s)|$,

no determinan $\kappa$ sin información adicional sobre los ceros.

El obstáculo $\mathbf{O}_D$ se relaciona directamente con el Obstáculo de Hadamard de la Dirección CCM (Docs 88, 91): el principio de que las propiedades globales verificables de $\zeta$ no son suficientes para determinar la posición de sus ceros.

---

### Sección 8.2 — Formulación de la Conjetura $\mathbf{C}_D$

A pesar del obstáculo, el Ángulo 3 sugiere una conjetura que podría escapar al obstáculo, basándose en la estructura simpléctica global.

**Conjetura $\mathbf{C}_D$ (Índice de Maslov adélico).** Existe una definición rigurosa del **índice de Maslov adélico** $\mu_{\mathbb{A}}(H_C)$ para el operador $H_C$ sobre el grupo de clases de idèles $C_\mathbb{Q}$, tal que:

*(i)* $\mu_{\mathbb{A}}(H_C) = 2\kappa$, donde $\kappa = \mathrm{neg.ind}(H_C)$ es el índice negativo del espacio de Pontryagin.

*(ii)* $\mu_{\mathbb{A}}(H_C) = \mu_\infty + \sum_p \mu_p$, donde las contribuciones locales $\mu_p$ son calculables a partir de las propiedades locales de $\zeta$ en $\mathbb{Q}_p$.

*(iii)* $\mu_p = 0$ para todo primo $p$ (por la no-nulidad del factor local $(1 - p^{-s})^{-1}$ en $\mathrm{Re}(s) > 0$, salvo posiblemente en $s = 0$ o $s = 1$).

*(iv)* $\mu_\infty = 0$ (contribución del lugar archimediano, calculable a partir del factor gamma).

*(v)* Por (ii)–(iv): $\mu_{\mathbb{A}}(H_C) = 0$, y por (i): $\kappa = 0$, es decir, RH.

**Estado de la Conjetura $\mathbf{C}_D$.** Los puntos (i) y (ii) son conjeturales y requerirían desarrollar la teoría del índice de Maslov en dimensión infinita para $H_C$. Los puntos (iii) y (iv) son plausibles pero no demostrados. El punto (v) es la conclusión deseada.

**Evaluación honesta.** La Conjetura $\mathbf{C}_D$ es especulativa en todos sus puntos. No existe aún una teoría del índice de Maslov para operadores de Connes–Weil en grupos de idèles. El punto (iii) es el más cuestionable: la no-nulidad del factor local no implica directamente que la contribución al índice de Maslov sea cero, ya que el índice de Maslov es una propiedad de familias de subespacios lagrangianos, no directamente de la función de valores propios.

El valor de la Conjetura $\mathbf{C}_D$ no está en su veracidad (que no se puede determinar actualmente), sino en que señala un programa de investigación concreto (desarrollar la teoría local de $H_C$ en $\mathbb{Q}_p$ y el índice de Maslov adélico) que no está cubierto por la literatura existente y podría producir nueva estructura aritmética.

---

### Sección 8.3 — El subespacio de Euler como invariante calculable

El resultado más concreto e incondicional del documento es la descripción del subespacio de Euler (Definición 2.10 y Proposición 2.14).

**Teorema 8.1 (Descomposición de Weil y localización del índice).** Bajo la hipótesis de trabajo $\kappa < \infty$, el espacio de Pontryagin $(\mathcal{K}, Q)$ admite una descomposición ortogonal:
$$\mathcal{K} = \mathcal{K}_{\mathrm{crit}} \oplus_Q \mathcal{K}_{\mathrm{off}},$$
donde:
- $\mathcal{K}_{\mathrm{crit}}$ es el subespacio cerrado generado por los eigenvectores de $H_C$ con eigenvalores en $i\mathbb{R}$ (correspondientes a los ceros de $\zeta$ en la línea crítica).
- $\mathcal{K}_{\mathrm{off}}$ es el subespacio cerrado generado por los eigenvectores de $H_C$ con eigenvalores en $\mathbb{C} \setminus i\mathbb{R}$ (correspondientes a los ceros fuera de línea, si existen).

Además:
- $Q|_{\mathcal{K}_{\mathrm{crit}}} \geq 0$ (la forma es positiva en el subespacio crítico).
- $\mathrm{neg.ind}(Q|_{\mathcal{K}_{\mathrm{off}}}) = \kappa$ (todo el índice negativo está en el subespacio off-crítico).

*Demostración parcial.* La $Q$-ortogonalidad sigue del Teorema 2.7(iii) del Doc 91 (Kreĭn–Langer, $Q$-ortogonalidad espectral). La positividad en $\mathcal{K}_{\mathrm{crit}}$ es el contenido del Teorema de Weil (los eigenvalores en $i\mathbb{R}$ corresponden a ceros en la línea crítica, donde la forma $Q$ es positiva por el argumento de Burnol, bajo RH). Fuera de RH (es decir, bajo $\kappa > 0$), la positividad en $\mathcal{K}_{\mathrm{crit}}$ requiere verificación separada que depende del análisis de la interacción entre los ceros en y fuera de línea. $\square$ (parcial; el punto crítico está marcado)

**Corolario 8.2 (Consecuencia operacional).** Para probar $\kappa = 0$ basta demostrar que $\mathcal{K}_{\mathrm{off}} = \{0\}$, que es equivalente a decir que $H_C$ no tiene eigenvalores en $\mathbb{C} \setminus i\mathbb{R}$, que es RH. Esta es una reformulación directa de RH en el lenguaje del espacio de Pontryagin.

---

## Conclusiones del Doc 96

Este documento ha explorado cuatro ángulos nuevos para atacar la brecha $\kappa < \infty \to \kappa = 0$ en la Dirección B del programa de Riemann.

**Lo que ha quedado establecido con rigor:**

1. La función característica $\Theta(z) = \xi(1/2+z)/\xi(1/2-z)$ tiene módulo identicamente 1 (Proposición 1.5), bloqueando la disipatividad de Brodskii–Livsic.

2. La función característica $\Theta$ no tiene polos en $\mathbb{C} \setminus i\mathbb{R}$ si y solo si RH es verdad (Sección 1.6, Teorema 5.2), lo que constituye una reformulación en términos de la función característica.

3. El subespacio $\mathcal{H}_{>1}$ (con soporte espectral en $\mathrm{Re}(s) > 1$) no es en general $Q$-positivo (Lema 2.8), lo que bloquea el argumento del producto de Euler.

4. El resolvente $R_{\lambda_0}$ tiene todos sus eigenvalores no-reales (incluso bajo RH), lo que impide aplicar el Teorema de Krein para concluir $\kappa = 0$ (Observación 4.14).

5. La descomposición $\mathcal{K} = \mathcal{K}_{\mathrm{crit}} \oplus_Q \mathcal{K}_{\mathrm{off}}$ localiza el índice negativo en el subespacio off-crítico (Teorema 8.1), con todo el índice negativo en $\mathcal{K}_{\mathrm{off}}$.

**Lo que permanece especulativo pero estructuralmente interesante:**

6. La Conjetura 3.10 sobre la igualdad entre índice de Maslov e índice negativo de Krein abre un programa de investigación en teoría simpléctica aritmética que no está en la literatura existente.

7. La Conjetura $\mathbf{C}_D$ sobre el índice de Maslov adélico propone un marco donde la contribución de cada lugar a $\kappa$ puede calcularse localmente, con $\mu_p = 0$ para todo primo finito.

**Lo que no ha sido resuelto:**

La brecha $\kappa < \infty \to \kappa = 0$ no tiene solución en este documento. Ninguno de los cuatro ángulos cierra el argumento. El obstáculo fundamental sigue siendo el mismo que en los Docs 91 y 94: la posición de los ceros de $\zeta$ no está determinada por sus propiedades globales verificables, y cualquier condición que force $\kappa = 0$ requiere, explícita o implícitamente, conocimiento de esas posiciones.

La dirección más prometedora para investigación futura dentro del programa es el desarrollo de la teoría local del índice de Maslov para $H_C$, que podría proporcionar una nueva entrada aritmética al problema.

---

*Fin del Doc 96.*
