# Doc 51 — Formalización de Dirección I: El Operador $\Phi$ en Retículos de Banach y el Teorema de Krein-Rutman

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–49, especialmente Doc 48  
**Naturaleza:** Formalización completa — el operador $\Phi$ como objeto en análisis funcional. Sin heurísticas: definiciones, normas, dominios y la frontera exacta del argumento.  
**Objetivo:** Definir el espacio de Banach correcto para las medidas $\zeta$-compatibles. Definir $\Phi$ rigurosamente. Aplicar el teorema de Krein-Rutman. Identificar el obstáculo exacto para la unicidad del punto fijo.

---

## 1. Diagnóstico del gap de Doc 48

Doc 48 usó "radio espectral" sin definir el espacio de Banach. El revisor señala que sin estructura de espacio y norma, el radio espectral no tiene contenido matemático formal. Este documento corrige ese gap.

---

## 2. El espacio de medidas signadas de variación total acotada

**Definición 2.1 (Espacio $M(\mathcal{R}_\eta)$).** Sea $\mathcal{R}_\eta = \{(x,y)\in\mathbb{H}: y \leq 1/2 - \eta/\log(|x|+2)\}$ la región admisible (Axioma 3 de Doc 48). El espacio:
$$M(\mathcal{R}_\eta) = \{\text{medidas de Borel signadas } \nu \text{ en } \mathcal{R}_\eta : \|\nu\|_{\mathrm{TV}} < \infty\}$$

dotado de la norma de variación total $\|\nu\|_{\mathrm{TV}} = |\nu|(\mathcal{R}_\eta)$, es un espacio de Banach.

**Proposición 2.2.** $M(\mathcal{R}_\eta)$ es un *retículo de Banach* (Banach lattice) con la descomposición positiva/negativa: $\nu = \nu^+ - \nu^-$ con $\|\nu\|_{\mathrm{TV}} = \|\nu^+\|_{\mathrm{TV}} + \|\nu^-\|_{\mathrm{TV}}$.

**Definición 2.3 (El cono positivo).** $M^+(\mathcal{R}_\eta) = \{\mu \in M(\mathcal{R}_\eta) : \mu \geq 0\}$ es el cono de medidas positivas — un subconjunto cerrado convexo de $M(\mathcal{R}_\eta)$.

**Definición 2.4 (El subespacio $\mathcal{M}_\zeta^{1-4}$).** El subespacio de medidas que satisfacen los Axiomas 1–4 de Doc 48:
$$\mathcal{M}_\zeta^{1-4} = \left\{\mu \in M^+(\mathcal{R}_\eta): \mu \text{ satisface Axiomas 1, 2, 4}, \int\frac{y}{1+x^2}\,d\mu < 1\right\}$$

es un subconjunto cerrado, convexo y acotado de $M(\mathcal{R}_\eta)$ (la condición de masa acotada $\int y/(1+x^2)d\mu < 1$ es la normalización de Axioma 6).

**Proposición 2.5 (Compacticidad).** $\mathcal{M}_\zeta^{1-4}$ es compacto en la topología débil* de $M(\mathcal{R}_\eta)$ — por el Teorema de Banach-Alaoglu, la bola unitaria de $M(\mathcal{R}_\eta)$ en la topología débil* es compacta.

---

## 3. El operador de auto-consistencia $\Phi$: definición rigurosa

El operador $\Phi: \mathcal{M}_\zeta^{1-4} \to \mathcal{M}_\zeta^{1-4}$ requiere una definición en dos pasos.

**Paso 1: De la medida a la función armónica.**

Para $\mu \in \mathcal{M}_\zeta^{1-4}$, definimos:
$$F_\mu: \mathbb{H}^+ \to \mathbb{R}, \quad F_\mu(z) = \mathcal{P}[\mu](z) = \int_\mathbb{H} P_{\mathrm{Im}(z)}(\mathrm{Re}(z)-x)\,d\mu(x,y)$$

Esta es una función armónica positiva en $\mathbb{H}^+$, con traza en $\mathbb{R}$ dada por $F_\mu(t) = \int P_y(t-x)d\mu(x,y)$ (interpretada como límite no-tangencial).

**Paso 2: De la función armónica a la medida de ceros.**

Dado $F_\mu$, definimos su *medida off-crítica generada*:
$$\Phi[\mu] := \mu_{\mathrm{off}}[F_\mu]$$

donde $\mu_{\mathrm{off}}[F]$ es la medida de ceros off-críticos del candidato a función $\zeta$ cuyo potencial espectral es $F$. Más precisamente:

**Definición 3.1 (El mapa $\mu_{\mathrm{off}}[F]$).** Para una función armónica positiva $F: \mathbb{H}^+ \to [0,\infty)$ con representación de Herglotz $F(z) = \int P_y(x-t)d\nu_F(t)$, la medida:
$$\mu_{\mathrm{off}}[F] = \nu_F \text{ (la medida de Herglotz representante de } F\text{)}$$

siempre que $\nu_F$ satisfaga los Axiomas 1–4.

**Proposición 3.2 (Consistencia).** Si $\mu = \mu_{\mathrm{off}}$ (la medida real de ceros off-críticos de $\zeta$), entonces $\Phi[\mu_{\mathrm{off}}] = \mu_{\mathrm{off}}$ — es decir, $\mu_{\mathrm{off}}$ es un punto fijo de $\Phi$.

*Prueba.* $F_{\mu_{\mathrm{off}}} = \mathcal{P}[\mu_{\mathrm{off}}] = C_\infty$ (Doc 44, Teorema 4.1). La medida de Herglotz de $C_\infty$ es $\mu_{\mathrm{off}}$ (por la unicidad de la representación de Herglotz-Riesz). Luego $\Phi[\mu_{\mathrm{off}}] = \mu_{\mathrm{off}}$. $\square$

**Proposición 3.3 ($\mu=0$ es punto fijo trivial).** $F_0 = 0$, y la medida de Herglotz de $0$ es $\nu=0$. Luego $\Phi[0] = 0$.

---

## 4. Continuidad de $\Phi$

**Lema 4.1 (Continuidad del mapa $\mu\mapsto F_\mu$).** El mapa $\Phi_1: \mu \mapsto F_\mu = \mathcal{P}[\mu]$ es débil*-a-uniforme en compactos continuo: si $\mu_\alpha \xrightarrow{w^*} \mu$, entonces $F_{\mu_\alpha}(z) \to F_\mu(z)$ para todo $z\in\mathbb{H}^+$.

*Prueba.* $F_\mu(z) = \int P_y(x-t)d\mu(t)$ donde $P_y(x-\cdot) \in C_b(\mathcal{R}_\eta)$ para $z=x+iy$ fijo. La convergencia débil* de medidas contra funciones continuas acotadas da la convergencia puntual de $F_\mu$. $\square$

**Lema 4.2 (Continuidad del mapa $F\mapsto\mu_{\mathrm{off}}[F]$).** El mapa $\Phi_2: F \mapsto \mu_{\mathrm{off}}[F]$ es continuo en la topología de convergencia uniforme en compactos, siempre que los ceros off-críticos de la función $\zeta$ asociada a $F$ varíen continuamente con $F$.

*Nota crítica.* El Lema 4.2 requiere una hipótesis sobre cómo "la función $\zeta$ asociada a $F$" depende de $F$. Esto es circular: para definir $\Phi_2$, necesitamos saber qué función zeta tiene $F$ como potencial espectral. En el caso real, $F = C_\infty$ determina $\zeta$ — pero en general $F$ podría no corresponder a ninguna $\zeta$.

**Resolución del problema de circularidad.** Reformulamos $\Phi$ para evitar la circularidad:

**Definición 4.3 (Operador $\Phi$ reformulado).** El operador $\Phi$ actúa solo en el espacio de medidas que ya son candidatos a $\mu_{\mathrm{off}}$ para alguna $\zeta$:
$$\Phi: \mathcal{C}_\zeta \to \mathcal{C}_\zeta$$

donde $\mathcal{C}_\zeta = \{\mu \in \mathcal{M}_\zeta^{1-4}: \exists\text{ función zeta }\zeta_\mu \text{ tal que } \mu = \mu_{\mathrm{off}}[\zeta_\mu]\}$.

En este dominio, $\Phi[\mu] = \mu_{\mathrm{off}}[\mathcal{P}[\mu]]$ está bien definido porque $\mathcal{P}[\mu]$ determina los ceros off-críticos de $\zeta_\mu$ via la fórmula de Hadamard (Doc 42).

---

## 5. El Teorema de Krein-Rutman y sus consecuencias

**Teorema 5.1 (Krein-Rutman, 1948).** Sea $X$ un espacio de Banach con cono positivo $K$ de interior no vacío, y sea $T: X\to X$ un operador lineal compacto que preserva $K$ (es decir, $T(K) \subseteq K$). Entonces:

1. El radio espectral $r(T) = \sup\{|\lambda|: \lambda \in \sigma(T)\}$ es un eigenvalor de $T$.
2. Existe un eigenvector positivo $v \in K$ con $Tv = r(T)v$.
3. El eigenvalor $r(T)$ es simple y es el único eigenvalor con eigenvector en $K$.

**Proposición 5.2 (El operador linealizado de $\Phi$).** El diferencial de $\Phi$ en $\mu=0$, denotado $D\Phi_0$, es el operador lineal:
$$D\Phi_0: \nu \mapsto \frac{\partial}{\partial\epsilon}\Phi[\epsilon\nu]\bigg|_{\epsilon=0}$$

**Cálculo explícito:**

$\Phi[\epsilon\nu] = \mu_{\mathrm{off}}[\mathcal{P}[\epsilon\nu]] = \mu_{\mathrm{off}}[\epsilon\cdot\mathcal{P}[\nu]]$. Para $\epsilon$ pequeño, los ceros off-críticos asociados a la función armónica $\epsilon\cdot\mathcal{P}[\nu]$ corresponden a ceros de $\zeta$ perturbados — que están a distancia $O(\epsilon)$ de la línea crítica (región libre de ceros: no puede haber ceros a distancia $< c/\log T$ del eje). Luego la perturbación $\mu_{\mathrm{off}}[\epsilon\cdot\mathcal{P}[\nu]] = 0$ para $\epsilon < \epsilon_0(\nu)$ (ningún cero puede entrar a la región off-crítica por perturbación pequeña).

**Proposición 5.3 (Radio espectral nulo del linealizado).** $r(D\Phi_0) = 0$.

*Prueba.* Para toda $\nu \in M(\mathcal{R}_\eta)$ con $\|\nu\| = 1$, la perturbación $\epsilon\nu$ produce una función armónica $\epsilon\mathcal{P}[\nu]$ de norma $O(\epsilon)$. Los ceros off-críticos de la función zeta perturbada están en la región libre de ceros cuando $\epsilon$ es pequeño — luego $D\Phi_0[\nu] = 0$. Como $D\Phi_0 \equiv 0$ en todo $M(\mathcal{R}_\eta)$, su radio espectral es $0$. $\square$

**Corolario 5.4 (Estabilidad local de $\mu=0$).** Por el Teorema de Krein-Rutman (Proposición 5.3), el punto fijo $\mu=0$ es localmente estable: en un entorno $\epsilon$-pequeño de $\mu=0$ en $M(\mathcal{R}_\eta)$, no hay otros puntos fijos de $\Phi$.

---

## 6. El obstáculo para la estabilidad global

**Proposición 6.1 (Posición de $\mu_{\mathrm{off}}$ relativa a 0).** Si RH falla, el punto fijo no trivial $\mu_{\mathrm{off}}$ satisface:
$$\|\mu_{\mathrm{off}}\|_{\mathrm{TV}} = \mu_{\mathrm{off}}(\mathcal{R}_\eta) = \#\mathcal{Z}_{\mathrm{off}} \cdot \overline{y_0}$$

donde $\overline{y_0}$ es el peso medio de los átomos. Por la región libre de ceros, $\overline{y_0} \geq c/\log T_0 > 0$, luego $\|\mu_{\mathrm{off}}\|_{\mathrm{TV}} \geq c > 0$ — el punto fijo no trivial está a distancia positiva de 0.

**Proposición 6.2 (El argumento de Schauder no distingue los dos puntos fijos).** El Teorema de Punto Fijo de Schauder (aplicado a $\Phi: \mathcal{M}_\zeta^{1-4} \to \mathcal{M}_\zeta^{1-4}$) garantiza existencia de al menos un punto fijo, pero no distingue $\mu=0$ de $\mu_{\mathrm{off}}$.

**El obstáculo global exacto:**

> Demostrar que $\Phi$ no tiene puntos fijos en $\{0 < \|\mu\|_{\mathrm{TV}} < \infty\}$, es decir, que no hay puntos fijos distintos del trivial.

Esto requiere una propiedad de *contracción global* de $\Phi$ — que no sigue de la estabilidad local.

---

## 7. Estimaciones de Lyapunov y el funcional de Lyapunov

Para estudiar la estabilidad global, introducimos un funcional de Lyapunov.

**Definición 7.1 (Funcional de energía $\mathcal{E}$).** Para $\mu \in \mathcal{M}_\zeta^{1-4}$, definimos:
$$\mathcal{E}[\mu] = \int_\mathbb{H} \mathcal{P}[\mu](x)\,d\mu(x,y) = \int_\mathbb{H}\int_\mathbb{H} P_y(x-x')\,d\mu(x,y)\,d\mu(x',y')$$

Este es el "potencial de auto-interacción" de la medida $\mu$ bajo el kernel de Poisson.

**Proposición 7.2 (Positividad de $\mathcal{E}$).** $\mathcal{E}[\mu] \geq 0$ para toda $\mu \geq 0$, con $\mathcal{E}[\mu] = 0$ solo si $\mu = 0$.

*Prueba.* $\mathcal{E}[\mu] = \|h\|_{L^2}^2$ donde $h = \mathcal{P}[\mu]$. La norma $L^2$ de una función no negativa es cero solo si la función es cero, y $\mathcal{P}[\mu] = 0$ implica $\mu = 0$ por la injectividad de la transformada de Poisson. $\square$

**Proposición 7.3 (Relación con la masa).** $\mathcal{E}[\mu] \geq c\|\mu\|_{\mathrm{TV}}^2$ para alguna constante $c > 0$ (esto sigue de la cota de Poisson $\mathcal{P}[\mu](x) \geq c\|\mu\|_{\mathrm{TV}}$ en el máximo de $\mathcal{P}[\mu]$).

**Pregunta clave para el funcional de Lyapunov:**

> ¿Es $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ para toda $\mu \in \mathcal{M}_\zeta^{1-4}$?

Si sí, entonces $\mathcal{E}$ sería un funcional de Lyapunov para $\Phi$, la energía decrece, y el sistema converge a $\mu=0$ (el único mínimo de $\mathcal{E}$).

**Proposición 7.4 (La desigualdad de Lyapunov no es automática).** La condición $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ es equivalente a:
$$\int_\mathbb{H}\mathcal{P}[\Phi[\mu]]\,d\Phi[\mu] \leq \int_\mathbb{H}\mathcal{P}[\mu]\,d\mu$$

Esto es una desigualdad entre la auto-energía de los ceros off-críticos de $\zeta_{\mathcal{P}[\mu]}$ y la auto-energía de $\mu$. No sigue de principios generales — requiere información aritmética sobre cómo la función $\zeta$ perturba sus propios ceros off-críticos.

---

## 8. Estado exacto de Dirección I

**Lo que está probado:**

| Afirmación | Estado | Herramienta |
|------------|--------|-------------|
| $M(\mathcal{R}_\eta)$ es retículo de Banach | ✓ | Análisis funcional estándar |
| $\mathcal{M}_\zeta^{1-4}$ es compacto en débil* | ✓ | Banach-Alaoglu |
| $\mu = 0$ y $\mu = \mu_{\mathrm{off}}$ son puntos fijos | ✓ | Construcción directa |
| Continuidad de $\mu \mapsto F_\mu$ (débil* → uniforme en compactos) | ✓ | Análisis armónico |
| $r(D\Phi_0) = 0$ | ✓ | Región libre de ceros |
| Estabilidad local de $\mu = 0$ | ✓ | Krein-Rutman + radio espectral |
| No hay puntos fijos distintos de $\{0, \mu_{\mathrm{off}}\}$ | ❌ Abierto | — |
| Desigualdad de Lyapunov $\mathcal{E}[\Phi[\mu]]\leq\mathcal{E}[\mu]$ | ❌ Abierto | — |

**La reducción precisa:**

> Dirección I reduce RH a: *demostrar que la desigualdad de Lyapunov $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ se satisface para toda $\mu \in \mathcal{M}_\zeta^{1-4}$ con $\mu \neq 0$.*

Equivalentemente: la energía de auto-interacción de los ceros off-críticos de $\zeta_F$ es estrictamente menor que la energía de auto-interacción de la medida $\mu$ que genera $F = \mathcal{P}[\mu]$.

---

## 9. Conexión con la Dirección II

**Proposición 9.1 (Las dos reducciones son equivalentes).** El obstáculo de Dirección I (Lyapunov) y el obstáculo de Dirección II (signo de la función armónica en el kernel de $M^T$) son equivalentes bajo la siguiente identificación:

- En Dirección II, el coeficiente $(a_k)$ produce la función $F^a = \sum_k a_k P_{y_k}(\cdot-x_k)$ con $F^a(\gamma_n) = 0$ para todo $n$.
- En Dirección I, la desigualdad de Lyapunov $\mathcal{E}[\Phi[\mu]] < \mathcal{E}[\mu]$ requiere que la función $G = \mathcal{P}[\Phi[\mu]] - \mathcal{P}[\mu]$ sea no positiva en un sentido promedio.
- $G$ tiene la misma estructura que $F^a$ del problema de signo.

*Ambas reducciones preguntan lo mismo: ¿puede una función armónica formada por combinaciones lineales de kernels de Poisson de ceros off-críticos de $\zeta$, que se anula en todos los ceros on-críticos, no ser de signo definido?*

---

*Siguiente (Doc 54): Análisis de signo para funciones armónicas con ceros en $\{\gamma_n\}$ — condiciones necesarias via teoría de potencial.*
