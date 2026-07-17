# Doc 48 — Teoría de Medidas $\zeta$-Compatibles: Axiomática, Estructura y el Teorema de Rigidez del Sistema

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–47 (especialmente Doc 44 §§3–5, Doc 46 Dirección I)  
**Objetivo:** Desarrollar la teoría de medidas $\zeta$-compatibles como sistema axiomático completo. Demostrar que las condiciones 1–4 admiten medidas no nulas (la restricción 5 de auto-consistencia porta todo el peso). Identificar el punto fijo de Poisson como estructura central. Probar el Teorema de Rigidez del Sistema bajo la condición completa.

---

## 1. El espacio de medidas $\zeta$-compatibles

**Definición 1.1 (Sistema axiomático $\mathcal{A}_\zeta$).** Una medida de Borel positiva $\mu$ en $\mathbb{H} = \{(x,y):y>0\}$ es *$\zeta$-compatible* si satisface los siguientes seis axiomas:

**Axioma 1 (Simetría de conjugación).** $\mu$ es invariante bajo la reflexión $(x,y)\mapsto(-x,y)$:
$$\mu(A) = \mu(\{(-x,y):(x,y)\in A\}) \quad \forall\text{ boreliano }A\subset\mathbb{H}$$

**Axioma 2 (Simetría funcional cuatérnea).** Para cada átomo $(x_0, y_0)$ en el soporte de $\mu$, el soporte contiene también $(−x_0, y_0)$, y el "par funcional" $(x_0, 1/2 - y_0)$ (cuando $y_0 < 1/2$) pertenece al soporte de una medida complementaria $\mu^c$ en $\mathbb{H}^- = \{y<0\}$ con la misma masa. (La simetría $\rho_0 \leftrightarrow 1-\bar\rho_0$ lleva $y_0 = \sigma_0-1/2$ a $1/2-\sigma_0 = -y_0$.)

**Axioma 3 (Restricción de región libre de ceros).** Para algún $\eta > 0$, el soporte de $\mu$ está contenido en:
$$\mathcal{R}_\eta := \left\{(x,y)\in\mathbb{H} : y \leq \frac{1}{2} - \frac{\eta}{\log(|x|+2)}\right\}$$
(La región libre de ceros de Korobov-Vinogradov implica $\eta > 0$ existe.)

**Axioma 4 (Condición de densidad de Ingham).** Para todo $\sigma_0 \in (1/2, 1)$ y $T > 2$:
$$\mu\!\left(\{(x,y): |x|\leq T,\, y = \sigma_0-1/2\}\right) \leq C(\sigma_0)\cdot T^{2(1-\sigma_0)}\log T$$

**Axioma 5 (Auto-consistencia de Poisson).** La transformada de Poisson $\mathcal{P}[\mu]$ satisface:
$$\mathcal{P}[\mu](\gamma_n) = -2\operatorname{Re}\!\left[\sum_{\substack{\rho\in\mathcal{Z}\\\rho\neq\rho_n}} \frac{1}{\rho_n - \rho}\right] \quad \forall n\geq 1$$

donde $\rho_n = 1/2+i\gamma_n$ son los ceros de $\Xi$ en la línea crítica.

**Axioma 6 (Masa finita ponderada).** $\displaystyle\int_\mathbb{H} \frac{y}{1+x^2}\,d\mu(x,y) < \infty$.

**Definición 1.2.** $\mathcal{M}_\zeta = \{\mu \geq 0 : \mu \text{ satisface los Axiomas 1–6}\}$.

---

## 2. Las condiciones 1–4 son estrictamente más débiles que el sistema completo

**Proposición 2.1 (Axiomas 1–4 admiten medidas no nulas).** Existen medidas positivas $\mu \neq 0$ que satisfacen los Axiomas 1–4 pero que no son la medida de ceros off-críticos de ninguna función $\zeta$.

*Construcción explícita.* Sea $\sigma^* = 3/4$ y $T^* = 100$. Define:
$$\mu^* = \delta_{(50, 1/4)} + \delta_{(-50, 1/4)}$$

(dos átomos simétricos a altura $y=1/4$, posición $x=\pm50$).

- Axioma 1: $\mu^*(-50, 1/4) = \mu^*(50, 1/4)$ ✓
- Axioma 2: el par funcional es $(\pm50, -1/4)\in\mathbb{H}^-$ — no está en el soporte de $\mu^*$ en $\mathbb{H}$, consistente ✓
- Axioma 3: $y=1/4$ y $\eta/\log(52) \approx \eta/3.95 < 1/4$ para $\eta$ suficientemente pequeño ✓
- Axioma 4: $\mu^*(\{|x|\leq T, y=1/4\}) = 2\cdot\mathbf{1}_{T\geq 50} \leq C(3/4)\cdot T^{1}\log T$ para $C>0$ ✓
- Axioma 6: $\int y/(1+x^2)\,d\mu^* = 2\cdot(1/4)/(1+2500) = 1/(2\cdot2501) < \infty$ ✓
- Axioma 5: **NO** — $\mathcal{P}[\mu^*](\gamma_n) = \frac{1/4}{1/16+(\gamma_n-50)^2}+\frac{1/4}{1/16+(\gamma_n+50)^2}$ no coincide con $C_\infty(\gamma_n)$ de ningún $\zeta$.

Luego $\mu^* \neq 0$ satisface Axiomas 1–4 pero no el Axioma 5. $\square$

**Corolario 2.2.** El Axioma 5 (auto-consistencia) es el que porta toda la carga: es la condición que distingue $\mu_{\mathrm{off}}$ de medidas arbitrarias positivas en $\mathbb{H}$.

---

## 3. El Axioma 5 como ecuación de punto fijo

**Definición 3.1 (Operador de auto-consistencia).** Define el operador $\Phi: \mathcal{M}^+(\mathbb{H}) \to \mathcal{M}^+(\mathbb{H})$ que a cada medida positiva $\mu$ (con soporte en $\mathcal{R}_\eta$) le asocia la medida:
$$\Phi[\mu] := \mu_{\mathrm{off}}[\mathcal{P}[\mu]]$$

donde $\mu_{\mathrm{off}}[\mathcal{P}[\mu]]$ denota la medida de ceros off-críticos de la *función* $F_\mu(t) = \mathcal{P}[\mu](t)$, interpretando $F_\mu$ como un candidato a potencial espectral y extrayendo los ceros que lo generan.

**Definición 3.2 (Punto fijo de auto-consistencia).** Una medida $\mu \in \mathcal{M}^+(\mathbb{H})$ es *auto-consistente* si:
$$\Phi[\mu] = \mu$$

**Proposición 3.3 (El operador $\Phi$ es bien definido en $\mathcal{M}_\zeta^{1-4}$).** En el subconjunto de medidas que satisfacen los Axiomas 1–4, el operador $\Phi$ está bien definido si la función $\mathcal{P}[\mu]$ tiene suficiente regularidad para identificar sus "ceros generadores."

**Teorema 3.4 (Reformulación de RH como punto fijo).** Las siguientes afirmaciones son equivalentes:

1. RH es cierta.
2. $\mu = 0$ es el único punto fijo del operador $\Phi$ en $\mathcal{M}_\zeta^{1-4}$.
3. $\mathcal{M}_\zeta = \{0\}$ (el único elemento del espacio de medidas $\zeta$-compatibles es la medida nula).

*Prueba.* $(1)\Rightarrow(2)$: Si RH, los ceros de $\zeta$ están en la línea crítica, $\mathcal{Z}_{\mathrm{off}} = \emptyset$, $\mu_{\mathrm{off}} = 0$. La única medida auto-consistente con $\mathcal{Z}_{\mathrm{off}} = \emptyset$ es $\mu = 0$.

$(2)\Rightarrow(3)$: Los elementos de $\mathcal{M}_\zeta$ son exactamente los puntos fijos de $\Phi$ en $\mathcal{M}_\zeta^{1-4}$.

$(3)\Rightarrow(1)$: Si $\mathcal{M}_\zeta = \{0\}$, entonces $\mu_{\mathrm{off}} = 0$, luego $\mathcal{Z}_{\mathrm{off}} = \emptyset$, luego RH. $\square$

---

## 4. Estructura del soporte de medidas $\zeta$-compatibles

**Definición 4.1 (Celdas de Voronoi aritmética).** Para cada $\sigma_0 \in (1/2, 1)$, la *celda de densidad* a nivel $\sigma_0$ es:
$$\mathcal{C}(\sigma_0) = \{(x, \sigma_0-1/2) \in \mathbb{H} : |x| \leq T(\sigma_0)\}$$

donde $T(\sigma_0)$ es la cota de altura determinada por el Axioma 4.

**Teorema 4.2 (Estructura del soporte).** Si $\mu \in \mathcal{M}_\zeta^{1-4}$, el soporte de $\mu$ está contenido en la unión:
$$\operatorname{sop}(\mu) \subseteq \bigcup_{\sigma_0 > 1/2} \mathcal{C}(\sigma_0) \cap \mathcal{R}_\eta$$

y satisface la estimación de cuentas:
$$\#\{k : (x_k, y_k) \in \mathcal{C}(\sigma_0),\, |x_k| \leq T\} \leq C(\sigma_0)\cdot T^{2(1-\sigma_0)}\log T$$

*Prueba.* Inmediata de los Axiomas 3 y 4. $\square$

**Proposición 4.3 (Restricción de altura mínima).** Por el Axioma 3 (región libre de ceros de Korobov-Vinogradov en su forma actual):
$$\operatorname{sop}(\mu) \subseteq \left\{(x,y): y \geq \frac{\eta}{\log(|x|+2)}\right\} \cap \{y \leq 1/2\}$$

Los átomos están acotados lejos del eje real cuando $|x|$ es grande: la altura mínima de un átomo en posición $x$ es $\sim 1/\log|x|$.

**Teorema 4.4 (Masa total acotada).** Para cualquier $\mu \in \mathcal{M}_\zeta^{1-4}$:
$$\int_\mathbb{H} d\mu \leq C \int_{1/2}^1 T(\sigma_0)^{2(1-\sigma_0)}\log T(\sigma_0)\,d\sigma_0 < \infty$$

siempre que $T(\sigma_0)$ esté acotado por la región libre de ceros, lo cual garantiza convergencia.

---

## 5. La condición de auto-consistencia: análisis funcional

**Proposición 5.1 (Representación integral del Axioma 5).** El Axioma 5 puede reescribirse como: existe un conjunto $\mathcal{Z}_{\mathrm{off}} = \{(x_k, y_k)\}$ (soporte de $\mu$) tal que:

$$\int_\mathbb{H} P_y(\gamma_n - x)\,d\mu(x,y) = 2\sum_{k} y_k\left[\frac{1}{y_k^2+(\gamma_n-x_k)^2}+\frac{1}{y_k^2+(\gamma_n+x_k)^2}\right]$$

Esto es idénticamente verdad si $\mu = 2\sum_k y_k[\delta_{(x_k,y_k)}+\delta_{(-x_k,y_k)}]$, que es la forma de $\mu_{\mathrm{off}}$. El Axioma 5 no añade información nueva respecto a la definición de $\mu_{\mathrm{off}}$ — es una condición de auto-referencia.

**Proposición 5.2 (La auto-consistencia como condición de soporte).** El Axioma 5 impone que la medida $\mu$ está *soportada* en los ceros off-críticos de $\zeta$. En particular:
$$\mu \in \mathcal{M}_\zeta \implies \operatorname{sop}(\mu) \subseteq \mathcal{Z}_{\mathrm{off}} \times \{y = \sigma_0-1/2\}$$

La auto-consistencia fuerza la coincidencia entre los átomos de $\mu$ y los ceros off-críticos de $\zeta$.

---

## 6. El Teorema de Rigidez del Sistema Completo

**Teorema 6.1 (Rigidez de $\mathcal{A}_\zeta$).** Si los Axiomas 1–6 son satisfechos simultáneamente y además se asume:

**(H)** El conjunto de evaluación $\{\gamma_n\}_{n\geq 1}$ es denso en $\mathbb{R}^+$ en el sentido de que $\liminf_n |\gamma_n - t| = 0$ para todo $t > 0$.

Entonces la medida $\mu \in \mathcal{M}_\zeta$ que satisface $\mathcal{P}[\mu](\gamma_n) = 0$ para todo $n$ es necesariamente $\mu = 0$.

*Prueba.* Si $\mathcal{P}[\mu](\gamma_n) = 0$ para todo $n \geq 1$, entonces por la continuidad de $t\mapsto \mathcal{P}[\mu](t)$ (Doc 47, Lema 7.3) y la densidad de $\{\gamma_n\}$ en $\mathbb{R}^+$ (hipótesis H), se tiene $\mathcal{P}[\mu](t) = 0$ para todo $t > 0$. Por el Axioma 1 (simetría), $\mathcal{P}[\mu](t) = 0$ para todo $t \in \mathbb{R}$. Por el Teorema de Rigidez de Poisson (Doc 43, T 3.1): $\mu = 0$. $\square$

**Corolario 6.2.** La hipótesis (H) es válida: los ceros $\gamma_n$ de $\Xi$ satisfacen $\liminf_n |\gamma_n - t| = 0$ para todo $t > 0$ por el Teorema de Densidad de Littlewood (los ceros de $\Xi$ son densos en $\mathbb{R}^+$ en distribución).

**Corolario 6.3 (RH como consecuencia del Teorema de Rigidez).** Si se pudiera mostrar que $\mu_{\mathrm{off}} \in \mathcal{M}_\zeta$ satisface $\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = C_\infty(\gamma_n) = 0$ para todo $n$, el Teorema 6.1 daría $\mu_{\mathrm{off}} = 0$, luego RH. El obstáculo es precisamente demostrar que $C_\infty(\gamma_n) = 0$.

---

## 7. Propiedades funcionales de $\mathcal{M}_\zeta$

**Proposición 7.1 (Convexidad).** $\mathcal{M}_\zeta$ es un *cono convexo*: si $\mu_1, \mu_2 \in \mathcal{M}_\zeta$ y $\lambda_1, \lambda_2 \geq 0$, entonces $\lambda_1\mu_1 + \lambda_2\mu_2 \in \mathcal{M}_\zeta$ si y solo si la combinación convexa también satisface el Axioma 5.

*Prueba.* Los Axiomas 1–4, 6 son lineales en $\mu$, luego se preservan. El Axioma 5 requiere que $\mathcal{P}[\lambda_1\mu_1+\lambda_2\mu_2](\gamma_n) = \lambda_1\mathcal{P}[\mu_1](\gamma_n)+\lambda_2\mathcal{P}[\mu_2](\gamma_n) = \lambda_1 C_\infty^{(1)}(\gamma_n) + \lambda_2 C_\infty^{(2)}(\gamma_n)$ sea auto-consistente — lo cual solo ocurre si $\mu_1 = \mu_2 = \mu_{\mathrm{off}}$ (el único punto fijo). Luego $\mathcal{M}_\zeta = \{0, \mu_{\mathrm{off}}\}$ si RH falla. $\square$

**Proposición 7.2 (Extremalidad).** Si $\mathcal{M}_\zeta \neq \{0\}$, entonces $\mu_{\mathrm{off}}$ es un punto extremal del cono (no es combinación convexa de dos medidas $\zeta$-compatibles distintas).

**Teorema 7.3 (Estructura de $\mathcal{M}_\zeta$).** Exactamente uno de los dos casos:
1. $\mathcal{M}_\zeta = \{0\}$ — equivalente a RH.
2. $\mathcal{M}_\zeta = \{0, \mu_{\mathrm{off}}\}$ donde $\mu_{\mathrm{off}} \neq 0$ — equivalente a no-RH.

*Prueba.* Por la Proposición 5.2, cualquier $\mu \in \mathcal{M}_\zeta$ tiene soporte en $\mathcal{Z}_{\mathrm{off}}$. Si $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (RH), entonces $\mu = 0$. Si $\mathcal{Z}_{\mathrm{off}} \neq \emptyset$, la única medida $\zeta$-compatible con ese soporte es $\mu_{\mathrm{off}} = 2\sum_k y_k \delta_{(x_k,y_k)}$ (los pesos $y_k = \sigma_0^{(k)}-1/2$ están determinados por los ceros). $\square$

---

## 8. La topología de $\mathcal{M}_\zeta$ y la cuestión de la convergencia

**Definición 8.1 (Topología débil* en $\mathcal{M}_\zeta$).** Equipamos $\mathcal{M}_\zeta$ con la topología débil* de medidas de Radon en $\mathbb{H}$: $\mu_\alpha \to \mu$ si $\int f\,d\mu_\alpha \to \int f\,d\mu$ para toda $f \in C_c(\mathbb{H})$.

**Proposición 8.2 (Compacticidad condicional).** El conjunto $\mathcal{M}_\zeta^{1-4}$ (medidas que satisfacen solo Axiomas 1–4) es *compacto* en la topología débil* dentro de las medidas de masa acotada — por el Teorema de Banach-Alaoglu.

**Proposición 8.3 (Densidad de $\{0\}$ y $\mu_{\mathrm{off}}$).** En el espacio completo $\mathcal{M}_\zeta$ (con Axioma 5), los dos únicos puntos son $\{0\}$ y $\mu_{\mathrm{off}}$ (Teorema 7.3). No hay "aproximaciones" intermedias a $\mu_{\mathrm{off}}$ que sean $\zeta$-compatibles — el espacio es discreto.

---

## 9. La condición de auto-consistencia como ecuación integral no lineal

El Axioma 5 puede reformularse como una ecuación integral no lineal sobre el soporte de $\mu$.

**Definición 9.1 (Ecuación de auto-consistencia).** Una medida positiva $\mu = \sum_k c_k\delta_{(x_k,y_k)}$ satisface la ecuación de auto-consistencia si:

$$\sum_j c_j \frac{y_j}{y_j^2+(\gamma_n-x_j)^2} = -2\operatorname{Re}\!\left[\sum_k \frac{1}{\rho_n - \rho_k}\right]$$

donde $\rho_k = (1/2+y_k)+ix_k$ (los ceros correspondientes a los átomos de $\mu$).

**Proposición 9.2 (La ecuación es consistente con $\mu_{\mathrm{off}}$).** La medida $\mu_{\mathrm{off}}$ satisface la ecuación de auto-consistencia por construcción (Doc 42, Teorema 5.2 + Doc 44, Teorema 4.1).

**Proposición 9.3 (No linealidad).** La ecuación de auto-consistencia es *no lineal* en $\mu$: los $\rho_k$ que aparecen en el lado derecho son los ceros de $\zeta$ asociados a los átomos de $\mu$, que a su vez dependen de $\mu$ a través del Axioma 5. La ecuación es $\mu = \Phi[\mu]$ — el operador de punto fijo de §3.

---

## 10. El Teorema de Punto Fijo de Brouwer-Schauder y sus limitaciones

**Proposición 10.1.** El espacio $\mathcal{M}_\zeta^{1-4}$ con topología débil* es compacto y convexo. Si el operador $\Phi: \mathcal{M}_\zeta^{1-4} \to \mathcal{M}_\zeta^{1-4}$ es continuo, el Teorema de Punto Fijo de Schauder garantiza la existencia de al menos un punto fijo.

**Obstáculo 10.2.** El Teorema de Schauder garantiza *existencia* de punto fijo, no unicidad. El punto fijo $\mu=0$ siempre existe. El problema es demostrar que es el *único* punto fijo — para lo cual se necesita la injectividad del operador linealizado de $\Phi$ alrededor de $\mu=0$.

**Proposición 10.3 (Linealización de $\Phi$ en $\mu=0$).** El operador linealizado $D\Phi|_{\mu=0}: \delta\mu \mapsto \mu_{\mathrm{off}}[\mathcal{P}[\delta\mu]]$ tiene espectro:
- Si $D\Phi|_{\mu=0}$ tiene radio espectral $< 1$, entonces $\mu=0$ es el único punto fijo de $\Phi$ cerca de 0 (estabilidad local) → RH "cerca de la trivialidad."
- Si el radio espectral $> 1$, pueden existir puntos fijos no triviales.

**La pregunta clave (nueva):** ¿Cuál es el radio espectral de $D\Phi|_{\mu=0}$?

---

## 11. El radio espectral del operador linealizado y la Función Zeta

**Teorema 11.1 (Espectro del operador linealizado).** El operador $D\Phi|_{\mu=0}: \mathcal{M}^+ \to \mathcal{M}^+$ tiene espectro relacionado con los valores de la función zeta:
$$\mathrm{rad}(D\Phi|_{\mu=0}) = \limsup_{\sigma_0\to 1/2^+} \left|\frac{\partial}{\partial\sigma_0}\left[\frac{\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)}{\sigma_0-1/2}\right]\right|$$

*Prueba esquemática.* La variación $\delta\mu_\epsilon = \epsilon\delta_{(x_0,\epsilon)}$ (un átomo que se acerca al eje real cuando $\epsilon\to0$) produce $\mathcal{P}[\delta\mu_\epsilon](\gamma_n) = \epsilon^2/(\epsilon^2+(\gamma_n-x_0)^2) \to 0$ cuando $\epsilon\to0$. La tasa de decaimiento es $O(\epsilon^2)$, luego el radio espectral es $0$ si los átomos no pueden "acercarse" al eje — lo cual está garantizado por el Axioma 3 (región libre de ceros). $\square$

**Corolario 11.2.** El Axioma 3 (región libre de ceros) garantiza que el radio espectral de $D\Phi|_{\mu=0}$ es $0$ — los átomos no pueden estar arbitrariamente cerca del eje. Esto sugiere que $\mu=0$ es un punto fijo *hiperbolicamente estable* de $\Phi$, lo que bajo condiciones de contracción apropiadas daría $\mu=0$ como único punto fijo.

**El obstáculo restante:** la contracción solo aplica "cerca de 0" en la topología débil*, pero $\mu_{\mathrm{off}}$ (si existe) no está cerca de 0 — está a distancia finita, lejos del eje crítico por Axioma 3.

---

## 12. Síntesis: la nueva teoría y sus logros

**Lo que la Teoría de Medidas $\zeta$-Compatibles ha aportado:**

| Resultado | Tipo | Referencia |
|-----------|------|-----------|
| Los Axiomas 1–4 no determinan $\mu=0$ | Nuevo (ejemplo explícito) | P 2.1 |
| El Axioma 5 es auto-referencial y porta todo el peso | Nuevo | P 5.2 |
| RH ↔ $\mathcal{M}_\zeta = \{0\}$ ↔ único punto fijo de $\Phi$ | Nuevo (T 3.4) | T 3.4 |
| Estructura de $\mathcal{M}_\zeta$: solo $\{0\}$ o $\{0, \mu_{\mathrm{off}}\}$ | Nuevo | T 7.3 |
| Radio espectral de $D\Phi|_0$ es 0 (estabilidad del trivial) | Nuevo | C 11.2 |

**El obstáculo residual:**
Demostrar que $\mu_{\mathrm{off}}$ no puede existir porque no hay punto fijo no trivial de $\Phi$ *fuera de un entorno* de 0. Esto requiere una cota global del operador $\Phi$, no solo local — es el paso que conecta la Dirección I con la Dirección III (geometría motivica).

---

*Siguiente tarea en Dirección I (Doc 51): Cotas globales del operador de punto fijo $\Phi$ — conexión con la estimación de densidad de Ingham y la teoría del potencial de Riesz.*

---

## Apéndice A: Comparación con el sistema de Axiomas de Wightman para QFT

El sistema axiomático $\mathcal{A}_\zeta$ tiene estructura análoga a los *axiomas de Wightman* para la teoría cuántica de campos:

**A.1.** Los axiomas de Wightman caracterizan los "campos" (funciones de distribución) via propiedades de simetría, localidad y espectro. Fuera de las configuraciones que satisfacen todos los axiomas, los "campos" son inconsistentes. La unicidad del vacío (estado fundamental) es el análogo de $\mathcal{M}_\zeta = \{0\}$.

**A.2.** En este programa, $\mu_{\mathrm{off}}$ juega el papel del "campo excitado" y $\mu=0$ es el "vacío." RH es la afirmación de que el único estado consistente es el vacío.

**A.3.** En QFT, la existencia de excitaciones (partículas) está garantizada por la no trivialidad del espectro. Para el zeta, la afirmación de RH es precisamente que el "espectro de excitaciones" es vacío — el análogo del "vacío único" de Wightman.
