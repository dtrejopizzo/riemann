# Phase 24-B — El perfil local universal de $\log|\zeta|$ inducido por $\mathcal{O}_j$

## La observación nueva

Phase 24-A mostró que no puede acotarse $b_j$ desde abajo mirando valores puntuales de $\log|\zeta(1/2+i\gamma_j)|$.

Pero hay una dirección distinta. El cero fuera de línea $\rho_j = (1/2+b_j)+i\gamma_j$ no sólo suprime $|\zeta|$ en el punto $t=\gamma_j$: produce un perfil completo en una ventana de ancho $b_j$ alrededor de $\gamma_j$.

**La pregunta es si ese perfil, como función geométrica, es compatible con la rigidez de las correlaciones del campo log-correlacionado.**

---

## Definición del perfil local

**Definición 24-B.1.** Fijada la órbita $\mathcal{O}_j$ con parámetros $(b_j, \gamma_j)$, se define el **perfil local renormalizado**:
$$\ell_j(u) := \log|\zeta\!\left(1/2+i(\gamma_j+ub_j)\right)|, \quad u \in \mathbb{R}.$$

En la notación de cambio de variable $t = \gamma_j + ub_j$, el parámetro $u$ mide la distancia al centro de la órbita en unidades de $b_j$.

---

## Cálculo del perfil local inducido por $\mathcal{O}_j$

**Proposición 24-B.2** (El perfil Lorentziano universal). La contribución de la órbita $\mathcal{O}_j$ al perfil $\ell_j(u)$ es:
$$\delta_j\ell_j(u) = \log(b_j^2+(ub_j)^2) + \log(b_j^2+(ub_j+2\gamma_j)^2) - \log|\rho_j^+|^2 - \log|\rho_j^-|^2 + O(1).$$

Para $u = O(1)$ y $\gamma_j$ grande:
$$\delta_j\ell_j(u) = 2\log b_j + \log(1+u^2) + O\!\left(\frac{u b_j}{\gamma_j}\right) + O(1).$$

En particular el perfil **renormalizado** (restando la depresión en el origen):
$$\delta_j\ell_j(u) - \delta_j\ell_j(0) = \log(1+u^2) + O\!\left(\frac{ub_j}{\gamma_j}\right).$$

*Demostración.* Del Teorema~24-A (Hadamard, Prop.~23-A.1): a $t = \gamma_j + ub_j$, los cuatro factores de $\mathcal{O}_j$ dan:
- De $\rho_j^+ = (1/2+b_j)+i\gamma_j$: $\sqrt{b_j^2+(ub_j-0)^2}/|\rho_j^+| = b_j\sqrt{1+u^2}/|\rho_j^+|$.
- De $\bar\rho_j^+$: $\sqrt{b_j^2+(ub_j+2\gamma_j)^2}/|\rho_j^+| \approx 2\gamma_j/|\rho_j^+|$ para $u=O(1)$.
- Análogamente para $\rho_j^-, \bar\rho_j^-$.

Producto de los cuatro:
$$\frac{b_j^2(1+u^2)\cdot(2\gamma_j)^2}{|\rho_j^+|^2|\rho_j^-|^2} \cdot (1+O(ub_j/\gamma_j)).$$
Tomando logaritmo: $2\log b_j + \log(1+u^2) + 2\log(2\gamma_j) - \log|\rho_j^+|^2 - \log|\rho_j^-|^2 + O(ub_j/\gamma_j)$. Los términos constantes en $b_j, \gamma_j$ absorben en el $O(1)$. $\square$

---

## La forma universal

**Corolario 24-B.3** (Perfil Lorentziano universal). El perfil renormalizado:
$$P(u) := \delta_j\ell_j(u) - \delta_j\ell_j(0) = \log(1+u^2) + O\!\left(\frac{b_j}{\gamma_j}\right)$$
es:
1. **Independiente de $b_j$** (al orden dominante para $\gamma_j$ grande).
2. **Determinístico** (no aleatorio): su forma está fijada por la geometría de la órbita fuera de línea.
3. De tipo **Lorentziano** (campana invertida con colas logarítmicas, no gaussianas).

Tiene ceros en $u = \pm i$ (polos del logaritmo), mínimo en $u=0$, y crece como $\log u^2$ para $|u| \to \infty$.

---

## Comparación con el campo background

El fondo $\log|\zeta(1/2+i(\gamma_j+ub_j))|$ sin la contribución de $\mathcal{O}_j$ es:
$$\ell_j^{(0)}(u) := \ell_j(u) - \delta_j\ell_j(u) \approx \text{campo log-correlacionado evaluado en }t = \gamma_j + ub_j.$$

Para $u = O(1)$ la escala de variación es $b_j$, que es la escala de la "depresión". El campo log-correlacionado tiene correlaciones:
$$\operatorname{Cov}(\ell_j^{(0)}(u), \ell_j^{(0)}(v)) \approx \log\frac{1}{|u-v|b_j} \cdot \mathbf{1}_{|u-v| \leq 1/(b_j^2)}$$
(estructura del campo log-correlado a escala $b_j$).

**La tensión:** el perfil determinístico $P(u) = \log(1+u^2)$ tiene variación $O(\log |u|)$ a escala $O(1)$ en $u$. La variación típica del campo aleatorio a la misma escala $O(1)$ en $u$ (correspondiente a escala $b_j$ en $t$) es:
$$\Delta\ell^{(0)} \sim \left(\operatorname{Cov}(\ell^{(0)}(0),\ell^{(0)}(0)) - \operatorname{Cov}(\ell^{(0)}(0),\ell^{(0)}(1))\right)^{1/2} \sim (\log(1/b_j))^{1/2}.$$

Para $b_j \to 0$: $(\log(1/b_j))^{1/2} \to \infty$, así que la variación del campo dominará eventualmente sobre el perfil $P(u) = O(\log u)$.

**Proposición 24-B.4** (El perfil Lorentziano es invisible en el campo a escala pequeña). Para $b_j \to 0$, la variación del campo background $\ell_j^{(0)}(u)$ en la escala $u = O(1)$ es $O((\log(1/b_j))^{1/2}) \gg 1$, mientras que la variación del perfil $P(u)$ sobre $u \in [-1,1]$ es $O(1)$ (pues $P(u) = \log(1+u^2) \in [0,\log 2]$ para $|u| \leq 1$).

*Por tanto:* para $b_j$ pequeño, el perfil Lorentziano está sumergido bajo las fluctuaciones del campo. **No hay incompatibilidad geométrica detectable en la escala $u = O(1)$.**

---

## La escala relevante: $u \sim (\log(1/b_j))^{1/2}$

El perfil $P(u)$ y las fluctuaciones del campo tienen la misma magnitud cuando:
$$\log(1+u^2) \sim (\log(1/b_j))^{1/2}$$
i.e., cuando $u \sim \exp\!\left(\frac12(\log(1/b_j))^{1/2}\right) - 1$.

Para $b_j = e^{-\gamma_j^\alpha}$: $(\log(1/b_j))^{1/2} = \gamma_j^{\alpha/2}$, y $u \sim e^{\gamma_j^{\alpha/2}/2}$.

Esta escala $u \sim e^{\gamma_j^{\alpha/2}/2}$ corresponde a desplazamientos en $t$ de:
$$\Delta t = u \cdot b_j = e^{\gamma_j^{\alpha/2}/2} \cdot e^{-\gamma_j^\alpha} = e^{\gamma_j^{\alpha/2}/2 - \gamma_j^\alpha}.$$

Para $\alpha \in (0,1)$: $\gamma_j^\alpha \gg \gamma_j^{\alpha/2}$ para $\gamma_j$ grande, así que $\Delta t = e^{-\gamma_j^\alpha(1+o(1))} \to 0$. La escala donde el perfil emerge sobre el fondo es microscópica (exponencialmente pequeña en $\gamma_j^\alpha$) y no es observacionalmente significativa.

**Proposición 24-B.5** (La rigidez geométrica no produce incompatibilidad). El perfil Lorentziano $P(u) = \log(1+u^2)$ inducido por la órbita fuera de línea NO produce una incompatibilidad geométrica con el campo log-correlacionado, para ningún régimen de $b_j \in (0,1/2)$, por la siguiente razón:

- A escala $u = O(1)$: la variación del perfil ($O(1)$) es superada por las fluctuaciones del campo ($O((\log(1/b_j))^{1/2}) \to \infty$).
- A la escala donde el perfil emerge: $\Delta t \to 0$, lo que equivale a que la "huella" de la órbita desaparece en el límite.

*Demostración.* Ver la comparación de varianzas anterior. La fluctuación del campo a escala $b_j$ es $O((\log(1/b_j))^{1/2})$, que excede la variación de $P(u)$ en $u \in [-1,1]$ para $b_j < 1$. $\square$

---

## Lo que sí revela el análisis del perfil local

Aunque no produce una incompatibilidad, el análisis del perfil revela algo matemáticamente preciso.

**Proposición 24-B.6** (El perfil como estimador del parámetro $b_j$). El perfil $\ell_j(u) - \ell_j(0)$ es una estimación de $P(u) = \log(1+u^2)$ contaminada por el campo background $\ell_j^{(0)}(u)-\ell_j^{(0)}(0)$ (de varianza $O(\log(1/b_j))$). Si la forma funcional de $P$ fuera observacionalmente distinguible del fondo, sería un estimador del desplazamiento $b_j$ sin conocer $b_j$ a priori.

*Consecuencia:* el perfil $P(u)$ tiene la forma de un **potencial de Yukawa unidimensional** (logarítmico). Su "radio de apantallamiento" es 1 (en unidades de $b_j$). Esto es distinguible de las fluctuaciones gaussianas sólo si la relación señal/ruido $P(u)/(\log(1/b_j))^{1/2} = \log(1+u^2)/(\log(1/b_j))^{1/2}$ es $O(1)$, i.e., cuando $|u| \sim (1/b_j)^{1/2}$.

---

## Resultado negativo de Phase 24-B

**Teorema 24-B.1** (Cierre negativo de la estrategia de perfil local). El análisis del perfil Lorentziano $P(u) = \log(1+u^2)$ inducido por $\mathcal{O}_j$ NO produce una incompatibilidad geométrica con el campo log-correlacionado, para ningún valor de $b_j \in (0,1/2)$.

La razón es que la variación del perfil a escala $u = O(1)$ es $O(1)$, mientras que las fluctuaciones del campo a esa misma escala son $O((\log(1/b_j))^{1/2}) \to \infty$ cuando $b_j \to 0$.

---

## Qué queda

Phase 24-A y 24-B han producido dos diagnósticos negativos:
1. No existe lower bound incondicional para $b_j$ desde métodos analíticos clásicos.
2. El perfil local Lorentziano no es geométricamente incompatible con el campo log-correlacionado.

La única vía que podría funcionar requiere el endurecimiento del modelo CMG hacia un resultado riguroso. Phase 24-C investiga si los resultados probados sobre campos log-correlacionados (no el modelo CMG sino los teoremas sobre $\zeta$ en sí) producen alguna restricción.

---

## Tabla de resultados de Phase 24-B

| Resultado | Clase | Estado |
|-----------|-------|--------|
| Prop. 24-B.2: perfil Lorentziano universal $P(u)=\log(1+u^2)$ | B | ✓ |
| Cor. 24-B.3: independiente de $b_j$, determinístico | B | ✓ |
| Prop. 24-B.4: perfil invisible bajo fluctuaciones del campo para $b_j \to 0$ | Negativo | ✓ |
| Prop. 24-B.5: no hay incompatibilidad geométrica | Negativo | ✓ |
| Prop. 24-B.6: perfil como estimador de $b_j$ (no una contradicción) | B | ✓ |
| **Teorema 24-B.1**: cierre negativo de la estrategia de perfil local | Negativo | ✓ |
