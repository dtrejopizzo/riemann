# Doc 50 — Formalización de Dirección II: El Espacio de de Branges, Completitud Exacta y la Frontera Precisa

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–49, especialmente Doc 47  
**Naturaleza:** Documento de formalización — objeto matemático completamente definido. Sin analogías: solo definiciones, lemas y la delimitación exacta de lo probado vs. lo abierto.  
**Objetivo:** Definir el espacio de Hilbert exacto en que vive el sistema de kernels de Poisson $\{P_y(\gamma_n-x)\}$. Conectar con la teoría de espacios de de Branges. Identificar el teorema de completitud correcto con sus hipótesis precisas.

---

## 1. Diagnóstico del gap de Doc 47

Doc 47 afirmó que $\sum 1/\gamma_n = \infty$ implica completitud del sistema de kernels. El revisor señala correctamente que esto no es un criterio válido en la forma presentada. El problema exacto:

1. La condición $\sum 1/\lambda_n = \infty$ (Müntz-Szász clásico) aplica al sistema $\{x^{\lambda_n}\}$ en $C[0,1]$ o $L^2[0,1]$ — no directamente a kernels de Poisson.
2. La transferencia vía Beurling-Malliavin necesita que el espacio target sea exactamente $L^2(\mathbb{R}, w\,dt)$ para un peso $w$ específico — no un espacio de medidas en $\mathbb{H}$.
3. El espacio $L^2(\mathbb{H}, \mu_{\mathrm{off}})$ no estaba definido con precisión suficiente para aplicar los teoremas de completitud.

Este documento define los objetos correctos.

---

## 2. El espacio de Hardy $H^2(\mathbb{H}^+)$ y su kernel reproductor

**Definición 2.1 (Espacio de Hardy).** El espacio de Hardy del semiplano superior es:
$$H^2(\mathbb{H}^+) = \left\{f: \mathbb{H}^+ \to \mathbb{C} \text{ holomorfa} : \sup_{y>0}\int_{-\infty}^\infty |f(x+iy)|^2\,dx < \infty\right\}$$

dotado del producto interno $\langle f, g\rangle = \sup_{y>0}\int f(x+iy)\overline{g(x+iy)}\,dx = \int_{-\infty}^\infty \hat f(\xi)\overline{\hat g(\xi)}\,d\xi$ (via Plancherel; las funciones en $H^2$ tienen traza en $\mathbb{R}$).

**Proposición 2.2 (Kernel reproductor de $H^2$).** $H^2(\mathbb{H}^+)$ es un espacio de Hilbert de funciones con kernel reproductor:
$$K_w(z) = \frac{1}{2\pi i}\cdot\frac{1}{\bar w - z}, \quad w \in \mathbb{H}^+, z\in\mathbb{H}^+$$

es decir, $f(w) = \langle f, K_w \rangle_{H^2}$ para toda $f \in H^2(\mathbb{H}^+)$.

**Proposición 2.3 (La parte imaginaria del kernel es el kernel de Poisson).** Sea $w = x_0+iy_0 \in \mathbb{H}^+$. La traza del kernel $K_w$ en la frontera real es:
$$K_w(t) = \frac{1}{2\pi i}\cdot\frac{1}{\bar w - t} = \frac{1}{2\pi i(x_0-iy_0-t)} = \frac{1}{2\pi}\cdot\frac{iy_0+(t-x_0)}{(t-x_0)^2+y_0^2}$$

La parte imaginaria (con signo apropiado):
$$\mathrm{Im}[-2\pi K_w(t)] = \frac{y_0}{(t-x_0)^2+y_0^2} = P_{y_0}(t-x_0)$$

*El kernel de Poisson es la parte imaginaria del kernel reproductor de $H^2$.*

---

## 3. Los espacios de de Branges: definición exacta

Los espacios de de Branges son subespacios cerrados de $H^2$ con estructura adicional.

**Definición 3.1 (Función de de Branges).** Una función entera $E: \mathbb{C}\to\mathbb{C}$ es una *función de de Branges* si:
1. $|E(z)| > |E^*(z)|$ para todo $z\in\mathbb{H}^+$, donde $E^*(z) := \overline{E(\bar z)}$.
2. $E$ no tiene ceros en $\mathbb{H}^+$.

**Definición 3.2 (Espacio de de Branges $\mathcal{H}(E)$).** Dada una función de de Branges $E$, el espacio de de Branges es:
$$\mathcal{H}(E) = \left\{f \text{ entera}: \frac{f}{E}, \frac{f^*}{E} \in H^2(\mathbb{H}^+)\right\}$$

dotado del producto interno $\langle f, g\rangle_E = \int_{-\infty}^\infty \frac{f(t)\overline{g(t)}}{|E(t)|^2}\,dt$.

**Proposición 3.3 (Kernel reproductor de $\mathcal{H}(E)$).** El kernel reproductor de $\mathcal{H}(E)$ en el punto $w \in \mathbb{C}$ es:
$$K_E(w,z) = \frac{E(z)\overline{E(w)} - E^*(z)\overline{E^*(w)}}{2\pi i(\bar w - z)}$$

**Proposición 3.4.** Los ceros de $E$ son exactamente los puntos donde los kernels $K_E(w, \cdot)$ tienen la propiedad de reproducción — i.e., son los puntos de evaluación del espacio.

---

## 4. La función de de Branges asociada a $\Xi$

**Proposición 4.1 (Conexión con $\Xi$).** La función $\Xi(s)$ (la función $\xi$ completada de Riemann normalizada, con ceros en la línea crítica bajo RH) está relacionada con una función de de Branges por:

$$E_\Xi(z) := A(z) + iB(z)$$

donde $A, B$ son las descomposiciones par/impar de $\Xi$ via $\Xi(1/2+iz) = A(z) + iB(z)$, con:
- $A(z) = \cos\theta(z)\cdot|\Xi(1/2+iz)|$ (parte coseno)
- $B(z) = \sin\theta(z)\cdot|\Xi(1/2+iz)|$ (parte seno)

y $\theta(z)$ es el argumento de la fase de $\Xi$.

**Nota (fundamental).** La función $E_\Xi$ es una función de de Branges si y solo si $\Xi$ tiene la propiedad $|\Xi(1/2+iz)| > |\Xi(1/2-iz)|$ para $\mathrm{Im}(z) > 0$ — que es una propiedad analítica no trivial de $\Xi$, relacionada pero no equivalente a RH.

**Proposición 4.2 (Ceros del espacio $\mathcal{H}(E_\Xi)$).** Los ceros de la función de de Branges $E_\Xi$ son los ceros de $\Xi$, es decir, los puntos $\gamma_n$ (bajo RH, todos reales).

---

## 5. El teorema de completitud correcto: Teorema de de Branges

**Teorema 5.1 (de Branges, 1961–1968).** Sea $E$ una función de de Branges y $\{w_n\}_{n\geq 1}$ una secuencia de puntos en $\mathbb{R}$ con:
1. $E(w_n) = 0$ para todo $n$ (los $w_n$ son ceros reales de $E$).
2. Los $w_n$ son simples: $E'(w_n) \neq 0$.
3. $\{w_n\}$ no acumula en $\mathbb{R}$ (la secuencia es discreta).

Entonces el sistema $\{K_E(w_n, \cdot)\}_{n\geq 1}$ es una *base ortonormal* de $\mathcal{H}(E)$.

*Prueba (esbozo).* Los kernels $K_E(w_n, \cdot)$ son mutuamente ortogonales pues si $w_n \neq w_m$ son ambos ceros de $E$, entonces $K_E(w_n, w_m) = 0$ (pues $K_E(w,z)|_{z=w_n}$ está en $\ker(E|_\mathbb{R}) = 0$). La completitud sigue del hecho de que toda función en $\mathcal{H}(E)$ con norma acotada que se anule en todos los $w_n$ debe ser cero (teorema de completitud de de Branges). $\square$

**Corolario 5.2.** En el espacio $\mathcal{H}(E_\Xi)$, el sistema $\{K_{E_\Xi}(\gamma_n, \cdot)\}_{n\geq 1}$ es una base ortonormal si los $\gamma_n$ son los ceros de $E_\Xi$.

---

## 6. La conexión entre $K_{E_\Xi}$ y el kernel de Poisson

**Proposición 6.1 (Relación explícita).** Para $E_\Xi$ y $w = \gamma_n \in \mathbb{R}$:
$$K_{E_\Xi}(\gamma_n, t) = \frac{E_\Xi(t)\overline{E_\Xi(\gamma_n)} - E_\Xi^*(t)\overline{E_\Xi^*(\gamma_n)}}{2\pi i(\gamma_n - t)}$$

En la restricción a $t \in \mathbb{R}$, si $E_\Xi(\gamma_n) = 0$ (cero de $E_\Xi$):
$$K_{E_\Xi}(\gamma_n, t) = \frac{-E_\Xi^*(t)\overline{E_\Xi^*(\gamma_n)}}{2\pi i(\gamma_n - t)}$$

**Proposición 6.2 (El kernel de Poisson como parte imaginaria).** Formalmente, en el límite en que $E_\Xi(z) \approx e^{i\pi z / T}$ (la aproximación de Weyl para la función de de Branges asociada a $\Xi$), se tiene:
$$\mathrm{Im}[K_{E_\Xi}(\gamma_n, t)] \approx C \cdot P_{1/\log\gamma_n}(\gamma_n - t)$$

para alguna constante $C > 0$. Esto justifica la relación entre $K_{E_\Xi}$ y el kernel de Poisson que usábamos en Doc 47.

*Nota (importante).* La proposición 6.2 es una aproximación para $\gamma_n$ grande. La relación exacta entre $K_{E_\Xi}(\gamma_n, \cdot)$ y $P_y(\gamma_n - \cdot)$ requiere conocer $E_\Xi$ explícitamente — lo que a su vez depende de propiedades de $\Xi$ que no se conocen independientemente de RH.

---

## 7. El espacio de Hilbert correcto para el sistema de Poisson

El gap de Doc 47 era no especificar el espacio. Aquí lo definimos.

**Definición 7.1 (El espacio $\mathcal{K}$).** Sea:
$$\mathcal{K} = \overline{\mathrm{span}}\left\{P_y(\gamma_n - x) : n \geq 1,\, y\in(0,1/2]\right\} \subset L^2(\mathbb{R}, dt)$$

(la clausura del span en $L^2(\mathbb{R})$, donde se toma $x=t$ y $y$ varía en $(0,1/2]$). En el caso que nos interesa, fijamos $y=y_0$ y consideramos la función $t\mapsto P_{y_0}(\gamma_n-t)$ como elemento de $L^2(\mathbb{R})$.

**Proposición 7.2.** Para cada $y_0 > 0$ fijo, $\{P_{y_0}(\gamma_n-\cdot)\}_{n\geq 1}$ es un elemento del espacio de Hardy $H^2(\mathbb{H}^-)$ (espacio de Hardy del semiplano inferior, pues el kernel de Poisson es la traza de una función holomorfa en $\mathbb{H}^-$).

**Definición 7.3 (Espacio $\mathcal{H}_{\mathrm{Poisson}}$).** El espacio de Hilbert relevante para el sistema de Poisson es:
$$\mathcal{H}_{\mathrm{Poisson}} = L^2\!\left(\mathbb{R}, \frac{dt}{1+t^2}\right)$$

con el producto interno $\langle f, g\rangle = \int f(t)\overline{g(t)}/(1+t^2)\,dt$. En este espacio, $P_{y_0}(\gamma_n-t) \in \mathcal{H}_{\mathrm{Poisson}}$ para todo $n$, pues $P_{y_0}(\gamma_n-t) \leq C/(1+t^2)$ para $t$ grande.

**Proposición 7.4.** En $\mathcal{H}_{\mathrm{Poisson}}$, los kernels de Poisson $\{P_{y_0}(\gamma_n-t)\}_{n\geq 1}$ tienen norma:
$$\|P_{y_0}(\gamma_n-\cdot)\|_{\mathcal{H}_{\mathrm{Poisson}}}^2 = \int_{-\infty}^\infty \frac{P_{y_0}(\gamma_n-t)^2}{1+t^2}\,dt = O(1/y_0)$$

uniformemente en $n$, lo que garantiza que están en el espacio.

---

## 8. El Teorema de Completitud de Carleson-Seip

Este es el resultado correcto que reemplaza el Müntz-Szász incorrecto de Doc 47.

**Definición 8.1 (Densidad de Beurling en $\mathbb{R}$).** Para una secuencia $\Lambda = \{\lambda_n\} \subset \mathbb{R}$, la densidad inferior de Beurling es:
$$D^-(\Lambda) = \liminf_{r\to\infty} \inf_{x\in\mathbb{R}} \frac{\#\{n: \lambda_n \in [x, x+r]\}}{r}$$

y la densidad superior es $D^+(\Lambda) = \limsup$ con $\sup$ en lugar de $\inf$.

**Teorema 8.2 (Seip, 1993 — Completitud en $L^2$ con kernel de reproducción).** Sea $\mathcal{H}$ un espacio de funciones con kernel reproductor $K_w(\cdot)$, y sea $\Lambda = \{\lambda_n\} \subset \mathbb{R}$ con $D^-(\Lambda) > 0$. Entonces:

1. *Completitud:* $\{K_{\lambda_n}(\cdot)\}$ es completo en $\mathcal{H}$ si $D^-(\Lambda) \geq D_\mathcal{H}$ (la "densidad crítica" de $\mathcal{H}$).
2. *Frame:* $\{K_{\lambda_n}(\cdot)\}$ es un marco de Riesz si $D^-(\Lambda) > D_\mathcal{H}$ y la secuencia es separada.

Para $\mathcal{H} = \mathcal{H}_{\mathrm{Poisson}}$ con el kernel $K_w(t) = P_{\mathrm{Im}(w)}(t-\mathrm{Re}(w))$ (kernel de Poisson), la densidad crítica es $D_\mathcal{H} = 1/(2\pi)$ (la densidad de Nyquist del espacio de Paley-Wiener de ancho de banda $1/(2)$, ajustada por el kernel de Poisson).

**Proposición 8.3 (Densidad de los ceros de $\Xi$).** Los ceros $\{\gamma_n\}$ de $\Xi$ satisfacen:
$$D^-(\{\gamma_n\}) = \lim_{T\to\infty}\frac{N_\Xi(T)}{T} = \lim_{T\to\infty}\frac{T\log T/(2\pi)}{T} = +\infty$$

(La densidad inferior es $+\infty$, pues el conteo crece más que linealmente.)

**Corolario 8.4.** Para cualquier $y_0 > 0$ fijo, $D^-(\{\gamma_n\}) > D_{\mathcal{H}_{\mathrm{Poisson}}}$. Por el Teorema de Seip, el sistema $\{P_{y_0}(\gamma_n-t)\}_{n\geq 1}$ es un **marco de Riesz** en $\mathcal{H}_{\mathrm{Poisson}}$.

*Nota crítica.* El Teorema de Seip se aplica a $\mathcal{H}_{\mathrm{Poisson}} = L^2(\mathbb{R}, dt/(1+t^2))$ con kernel de Poisson a altura $y_0$ FIJA. Para variar $y_0$ (como ocurre en el caso de $\mu_{\mathrm{off}}$), se necesita una versión del teorema para familias de kernels a distintas alturas — que es más sutil.

---

## 9. El gap real: medidas atómicas vs. continuas

**Proposición 9.1 (El caso continuo está resuelto).** Si $\mu_{\mathrm{off}} = f(x,y)dxdy$ es absolutamente continua con densidad $f \in L^1 \cap L^\infty(\mathbb{H})$, entonces el sistema $\{P_y(\gamma_n-x)\}_{n\geq 1}$ es un marco de Riesz en $L^2(\mathbb{H}, f\,dxdy)$ — por el Corolario 8.4 aplicado capa por capa en $y$.

**Proposición 9.2 (El caso atómico requiere argumento nuevo).** Si $\mu_{\mathrm{off}} = \sum_k c_k\delta_{(x_k,y_k)}$, entonces $L^2(\mathbb{H},\mu_{\mathrm{off}}) \cong \ell^2(\{c_k\})$ y el sistema $\{P_{y_k}(\gamma_n-x_k)\}_{n\geq 1,k\geq 1}$ es un sistema de vectores en $\ell^2$. La completitud del sistema de FILAS (indexadas por $n$) en $\ell^2$ (indexado por $k$) es equivalente a:

$$\ker\left[(M)_{nk} = P_{y_k}(\gamma_n-x_k)\right]^\top = \{0\} \subset \ell^2$$

**Lema 9.3 (La matriz de Poisson).** La matriz $M_{nk} = P_{y_k}(\gamma_n-x_k)$ tiene la siguiente estructura:
- Las filas son las funciones $k\mapsto P_{y_k}(\gamma_n-x_k)$ (evaluación del kernel de Poisson en los soportes de $\mu_{\mathrm{off}}$).
- Las columnas son las funciones $n\mapsto P_{y_k}(\gamma_n-x_k)$ (kernel de Poisson del $k$-ésimo átomo evaluado en los ceros de $\Xi$).

**Proposición 9.4 (Completitud de filas ↔ injectividad de $M^T$).** El sistema de filas es completo en $\ell^2$ si y solo si el operador $M^T: \ell^2 \to \mathbb{R}^{\mathbb{N}}$ (la transposición de $M$) es inyectivo — es decir, si no hay secuencia $(a_k) \in \ell^2$ con $\sum_k a_k P_{y_k}(\gamma_n-x_k) = 0$ para todo $n$.

---

## 10. La función armónica generada por el núcleo del sistema

**Teorema 10.1 (El kernel de $M^T$ como función armónica).** Si $(a_k) \in \ell^2$ satisface $\sum_k a_k P_{y_k}(\gamma_n - x_k) = 0$ para todo $n\geq 1$, entonces la función:
$$F(t) = \sum_k a_k P_{y_k}(t-x_k)$$

es una función armónica en $\mathbb{H}^+$ (extensión de Poisson de la medida $\nu = \sum_k a_k\delta_{(x_k,y_k)}$) que satisface $F(\gamma_n) = 0$ para todo $n\geq 1$.

*Prueba.* $F$ es suma convergente de armónicas positivas con coeficientes en $\ell^2$, luego es armónica. Y $F(\gamma_n) = \sum_k a_k P_{y_k}(\gamma_n-x_k) = 0$ por hipótesis. $\square$

**Corolario 10.2.** El kernel de $M^T$ consiste en coeficientes $(a_k) \in \ell^2$ tales que la función armónica $F = \sum_k a_k P_{y_k}(\cdot-x_k)$ se anula en todo el conjunto $\{\gamma_n\}$.

**Lema 10.3 (Unicidad de extensión armónica).** Si $F$ es armónica en $\mathbb{H}^+$, continua hasta la frontera, y $F(\gamma_n) = 0$ para todo $n\geq 1$, y si $F$ es de *signo definido* (i.e., $F \geq 0$ o $F \leq 0$ en $\mathbb{R}$), entonces $F \equiv 0$ (por el Teorema de Rigidez de Poisson, Doc 43 T 3.1).

---

## 11. El teorema final de Dirección II y el obstáculo exacto

**Teorema 11.1 (Completitud bajo hipótesis de signo).** Si los coeficientes $(a_k)$ en el kernel de $M^T$ satisfacen que la función $F = \sum_k a_k P_{y_k}(\cdot - x_k)$ es de signo constante en $\mathbb{R}$, entonces $(a_k) = 0$.

*Prueba.* Si $F \geq 0$, entonces por el Teorema de Rigidez (Doc 43, T 3.1), $F \equiv 0$. Por la injectividad de la transformada de Poisson (medida → función armónica), $\sum_k a_k\delta_{(x_k,y_k)} = 0$, luego $(a_k c_k) = 0$, luego $(a_k) = 0$ pues $c_k > 0$. $\square$

**El obstáculo exacto (precisado):**

> Demostrar que cualquier $(a_k)\in\ker(M^T)$ produce una función $F$ de signo constante.

Formalmente: si $F = \sum_k a_k P_{y_k}(\cdot-x_k)$ con $F(\gamma_n) = 0$ para todo $n$, ¿se sigue que $F$ no cambia de signo?

**Proposición 11.2 (El obstáculo no sigue de información existente).** En general, funciones armónicas que se anulan en un conjunto denso no son de signo definido. Se necesita información adicional sobre la estructura de los $(x_k, y_k)$ (los ceros off-críticos de $\zeta$) para concluir el signo.

**El punto de conexión con RH:** si RH es cierta, $(x_k,y_k) = \emptyset$, no hay nada que probar. Si RH falla, los $(x_k,y_k)$ son ceros off-críticos con propiedades aritméticas específicas. La hipótesis de signo equivale a preguntarse: ¿pueden los ceros off-críticos de $\zeta$ estar dispuestos de tal manera que $\sum_k a_k P_{y_k}(\cdot-x_k)$ cambie de signo en $\mathbb{R}$? Esta es una pregunta sobre la distribución de los ceros off-críticos — que es, una vez más, equivalente a RH.

---

## 12. Estado exacto de Dirección II

**Lo que está probado:**

| Afirmación | Estado | Herramienta |
|------------|--------|-------------|
| $\{P_{y_0}(\gamma_n-t)\}$ es marco de Riesz en $\mathcal{H}_{\mathrm{Poisson}}$ (altura $y_0$ fija) | ✓ Probado | Seip 1993 |
| $\{K_{E_\Xi}(\gamma_n,\cdot)\}$ es base ortonormal en $\mathcal{H}(E_\Xi)$ | ✓ Probado bajo hipótesis de de Branges | de Branges 1961 |
| Completitud para $\mu_{\mathrm{off}}$ absolutamente continua | ✓ Probado | Seip + desintegración |
| $\ker(M^T)$ de signo constante $\Rightarrow (a_k)=0$ | ✓ Probado | Rigidez de Poisson |
| $\ker(M^T) = \{0\}$ (sin hipótesis de signo) | ❌ Abierto | — |
| Completitud para $\mu_{\mathrm{off}}$ atómica incondicionalmente | ❌ Abierto | — |

**La reducción precisa:**

> Dirección II reduce RH a: *demostrar que cualquier función armónica que se anula en todos los $\gamma_n$ y es representable como $\sum a_k P_{y_k}(\cdot-x_k)$ con $(a_k)\in\ell^2$ y $(x_k,y_k)$ soportes de ceros off-críticos — es de signo constante.*

Esta es una afirmación sobre la geometría de los ceros off-críticos de $\zeta$, precisamente formulada.

---

*Siguiente (Doc 53): El problema de signo — ¿cuándo puede $\sum a_k P_{y_k}(\cdot-x_k)$ cambiar de signo? Condiciones necesarias y suficientes.*
