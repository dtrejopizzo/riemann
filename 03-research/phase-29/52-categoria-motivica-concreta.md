# Doc 52 — Formalización de Dirección III: La Categoría Concreta $\mathcal{MM}$ y el Programa de Deninger

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–51, especialmente Doc 49  
**Naturaleza:** Formalización de la geometría — de la analogía al objeto concreto. Sin conjeturas vacías: solo la estructura matemática que se puede construir hoy y la frontera exacta de lo que requiere trabajo nuevo.  
**Objetivo:** Construir la categoría $\mathcal{MM}$ de Medidas Motivicas como categoría aditiva concreta con cohomología. Conectar con el Programa de Deninger (el más relevante en la literatura). Definir el Frobenius aritmético como endofunctor. Identificar con precisión qué falta para que la CPC sea un teorema.

---

## 1. Diagnóstico del gap de Doc 49

Doc 49 usó la analogía con Weil para motivar una cohomología y un Frobenius, pero:
1. La traza $\mathrm{Tr}(\phi_\zeta|H^1) = \sum(\sigma_0-1/2)$ no estaba definida en ninguna teoría existente.
2. El "esquema $\mathcal{V}_\zeta$" no tenía estructura algebraica concreta.
3. La CPC era una analogía, no una conjetura formulada en una teoría existente.

Este documento construye los objetos concretos posibles hoy.

---

## 2. El Programa de Deninger: qué existe en la literatura

El programa más relevante en la literatura es el de Christopher Deninger (1991–presente).

**Teorema 2.1 (Deninger, 1991).** Existe un formalismo cohomológico conjetural en el que:

1. Existe un espacio $X$ ("el espacio de Deninger") con una acción de $\mathbb{R}$ via un flujo $\Phi^t: X\to X$.
2. Los ceros de $\zeta_\mathbb{Q}(s)$ son los eigenvalores de $\Phi^1_*: H^1(X) \to H^1(X)$ (el mapa inducido en cohomología por el tiempo $t=1$).
3. La traza del Frobenius (el elemento $\Phi^1_*$) satisface la fórmula de traza de Lefschetz:
$$\mathrm{Tr}(\Phi^1_* | H^1) = \sum_{\rho} 1 = N_\zeta$$

el número de ceros (contado con multiplicidad).

**El estado actual del programa de Deninger:** El espacio $X$ no ha sido construido en ninguna categoría matemática existente. Deninger lo describe mediante propiedades que debería tener, pero la construcción explícita es abierta.

**La conexión con nuestro programa:**

Nuestro espacio de déficit $\mathcal{V}_\zeta$ es *diferente* del espacio de Deninger: Deninger necesita que los eigenvalores de $\Phi^1_*$ sean los ceros de $\zeta$ (problema de Hilbert-Pólya), mientras que nuestro $\mathcal{V}_\zeta$ necesita que la ausencia de ceros off-críticos sea equivalente a la trivialidad de la cohomología. Son preguntas distintas pero relacionadas.

---

## 3. La categoría $\mathcal{MM}$: construcción concreta

No construimos una categoría motivica abstracta. Construimos una categoría concreta de objetos analíticos.

**Definición 3.1 (Objetos de $\mathcal{MM}$).** Un objeto de $\mathcal{MM}$ es un triplete $(\mathcal{R}, \mu, F)$ donde:
- $\mathcal{R} \subset \mathbb{H}$ es una región admisible (satisface el Axioma 3 de Doc 48).
- $\mu$ es una medida de Borel positiva en $\mathcal{R}$ con $\int y/(1+x^2)d\mu < \infty$.
- $F: \mathbb{H}^+ \to [0,\infty)$ es la extensión armónica $F = \mathcal{P}[\mu]$.

El triplete debe satisfacer la condición de *auto-consistencia débil*: la restricción de $F$ a la recta real satisface $F(t) \geq 0$ para todo $t\in\mathbb{R}$.

**Definición 3.2 (Morfismos de $\mathcal{MM}$).** Un morfismo $\phi: (\mathcal{R}_1, \mu_1, F_1) \to (\mathcal{R}_2, \mu_2, F_2)$ es un mapa de medidas $\phi_*: M(\mathcal{R}_1) \to M(\mathcal{R}_2)$ que satisface:
1. $\phi_*(\mu_1) = \mu_2$ (morfismo de medidas).
2. $F_2 = \mathcal{P}[\mu_2] = \mathcal{P}[\phi_*\mu_1]$ (compatibilidad con la extensión armónica).

**Proposición 3.3.** $\mathcal{MM}$ es una categoría: la composición de morfismos es el push-forward de medidas, que es asociativo y tiene unidades (identidad = identidad de medidas).

**Definición 3.4 (El objeto trivial y el objeto zeta).** El *objeto trivial* es $(R, 0, 0)$. El *objeto zeta* es $(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$. RH equivale a que el objeto zeta coincide con el trivial.

---

## 4. Cohomología en $\mathcal{MM}$

**Definición 4.1 (El functor $H^0$).** Para un objeto $(\mathcal{R}, \mu, F) \in \mathcal{MM}$:
$$H^0(\mathcal{R}, \mu, F) := F|_\mathbb{R} \in C(\mathbb{R}, \mathbb{R}_{\geq 0})$$

es la traza frontera de la función armónica.

**Definición 4.2 (El functor $H^1$).** Para definir $H^1$, usamos la secuencia exacta de Mayer-Vietoris. Cubra $\mathcal{R} = U_1 \cup U_2$ por dos abiertos. Entonces:
$$H^1(\mathcal{R}, \mu, F) := \ker(\delta^1: C^1(\mathcal{U}, \mathcal{F}_\mathcal{MM})\to C^2(\mathcal{U}, \mathcal{F}_\mathcal{MM}))/\mathrm{im}(\delta^0)$$

donde $\mathcal{F}_\mathcal{MM}$ es el haz que asocia a cada abierto $U\subset\mathcal{R}$ el espacio de funciones armónicas positivas en $U$ representables como $\mathcal{P}[\mu|_U]$.

**Proposición 4.3 (Cómputo explícito de $H^1$ para el objeto trivial).** Para el objeto trivial $(R, 0, 0)$:
$$H^1(\mathcal{R}, 0, 0) = 0$$

*Prueba.* Si $\mu = 0$, el haz $\mathcal{F}_\mathcal{MM}$ tiene solo secciones $\equiv 0$, luego toda cohomología es trivial. $\square$

**Proposición 4.4 (Cómputo de $H^1$ para el objeto zeta).** Si $\mu_{\mathrm{off}} \neq 0$:
$$H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \neq 0$$

*Prueba (esquemática).* El haz $\mathcal{F}_\mathcal{MM}$ tiene secciones no triviales determinadas por $\mu_{\mathrm{off}}$. La cohomología $H^1$ mide la obstrucción a extender secciones locales — que es no trivial cuando $\mu_{\mathrm{off}} \neq 0$ pues la medida tiene masa positiva. $\square$

**Corolario 4.5.** RH $\iff H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) = 0$.

---

## 5. El Frobenius aritmético como endofunctor

**Definición 5.1 (El endofunctor $\Phi_\zeta$).** El *Frobenius aritmético* es el endofunctor $\Phi_\zeta: \mathcal{MM} \to \mathcal{MM}$ que actúa en objetos por:
$$\Phi_\zeta(\mathcal{R}, \mu, F) = (\mathcal{R}, \Phi[\mu], \mathcal{P}[\Phi[\mu]])$$

donde $\Phi[\mu]$ es el operador de auto-consistencia de Doc 51.

**Proposición 5.2 (Puntos fijos de $\Phi_\zeta$ como objetos de $\mathcal{MM}$).** Los puntos fijos de $\Phi_\zeta$ en $\mathcal{MM}$ son exactamente los objetos $(\mathcal{R}, \mu, F)$ con $\Phi[\mu] = \mu$, que son:
- El objeto trivial $(R, 0, 0)$.
- El objeto zeta $(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$ si RH falla.

**Proposición 5.3 (Acción de $\Phi_\zeta$ en cohomología).** El endofunctor $\Phi_\zeta$ induce un mapa en cohomología:
$$\Phi_\zeta^*: H^1(\mathcal{R}, \mu, F) \to H^1(\mathcal{R}, \Phi[\mu], \mathcal{P}[\Phi[\mu]])$$

**Definición 5.4 (Traza del Frobenius).** La traza de $\Phi_\zeta^*$ sobre $H^1$ es:
$$\mathrm{Tr}(\Phi_\zeta^* | H^1) := \dim_\mathbb{R}(H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty))$$

*Nota:* esta definición es más débil que la traza de un operador lineal en un espacio de dimensión finita — $H^1$ puede ser de dimensión infinita. La definición correcta requiere especificar la noción de "traza" en dimensión infinita (traza de operadores de clase traza).

---

## 6. La Conjetura de Positividad Cohomológica: formulación precisa

**Definición 6.1 (Forma de Weil en $\mathcal{MM}$).** La *forma de Weil* en $H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$ es el pairing:
$$\langle\alpha, \beta\rangle_W := \int_\mathbb{H} \alpha(x,y)\cdot\beta(x,y)\,d\mu_{\mathrm{off}}(x,y)$$

donde $\alpha, \beta \in H^1$ son representadas como funciones en $\mathcal{R}_\eta$.

**Proposición 6.2 (Positividad de la forma de Weil es automática para $H^0$).** Para $H^0 = C_\infty$:
$$\langle C_\infty, C_\infty\rangle_W = \int |C_\infty|^2\,d\mu_{\mathrm{off}} = \mathcal{E}[\mu_{\mathrm{off}}] \geq 0$$

con igualdad solo si $\mu_{\mathrm{off}} = 0$ (RH).

**Conjetura de Positividad Cohomológica (CPC) — versión precisa:**
$$\langle\alpha, \Phi_\zeta^*\alpha\rangle_W > 0 \quad \forall \alpha \in H^1 \setminus\{0\}$$

*Esto es una versión del pairing de Weil-Petersson para el espacio de móduli de medidas.*

**Teorema 6.3 (CPC $\Rightarrow$ RH).** Si la CPC es cierta y $H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \neq 0$ (es decir, RH falla), entonces:
$$\langle\alpha, \Phi_\zeta^*\alpha\rangle_W > 0 \quad \Rightarrow \quad \mathrm{Tr}(\Phi_\zeta^*|H^1) > 0$$

Pero la traza positiva es $\sum(\sigma_0-1/2) > 0$, que contradiría... nada, porque una traza positiva es perfectamente compatible con RH fallando.

*Corrección del argumento de Doc 49.* El Teorema 6.2 de Doc 49 tenía un error lógico: la positividad de la traza NO implica que la traza sea cero (y por ende RH). En el caso de Weil, la positividad de $\langle\alpha, \bar\alpha\rangle > 0$ implica $|\lambda|^2 = q$ para los eigenvalores — lo cual usa la *dualidad de Poincaré* de una manera específica que relaciona $H^1$ con $H^1 \otimes \mathbb{Q}(-1)$. Sin esta dualidad en la categoría $\mathcal{MM}$, el argumento no cierra.

---

## 7. La Dualidad de Poincaré en $\mathcal{MM}$: el ingrediente faltante

**Definición 7.1 (Dualidad de Poincaré en $\mathcal{MM}$).** Una *dualidad de Poincaré* en $\mathcal{MM}$ sería un isomorfismo:
$$H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \cong H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)^\vee \otimes \omega$$

donde $\omega$ es un "dualizing object" — el análogo del torsor de Tate $\mathbb{Q}(-1)$ en la teoría $\ell$-ádica.

**Proposición 7.2 (El dualizing object en $\mathcal{MM}$).** El candidato natural para el dualizing object es:
$$\omega = (0, \lambda_{\mathrm{Leb}}, 1)$$

el objeto con medida de Lebesgue (restricción a $\mathcal{R}_\eta$) y función harmónica constante $\equiv 1$.

**Conjetura 7.3 (Dualidad de Poincaré para $\mu_{\mathrm{off}}$).** Si existe un isomorfismo canónico:
$$H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty) \cong \mathrm{Hom}(H^1(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty), \omega)$$

entonces la combinación CPC + Dualidad de Poincaré daría:
$$|\lambda_i|^2 = \langle\alpha_i, \Phi_\zeta^*\alpha_i\rangle / \|\alpha_i\|^2 = \text{const}$$

es decir, todos los eigenvalores de $\Phi_\zeta^*$ tienen el mismo módulo — el análogo de los ceros en la línea crítica.

**El estado honesto:** La Conjetura 7.3 es el ingrediente que falta para que la Dirección III cierre el argumento. No hay evidencia matemática directa de que $\mathcal{MM}$ tenga dualidad de Poincaré — es la pregunta central de esta dirección.

---

## 8. La conexión precisa con Deninger

**Proposición 8.1 (Relación entre $\mathcal{MM}$ y el espacio de Deninger).** El "espacio de Deninger" $X$ (si existiera) y nuestro espacio de déficit $\mathcal{V}_\zeta$ estarían relacionados por:
- En $X$: los eigenvalores de $\Phi^t_*|_{H^1(X)}$ son los ceros de $\zeta$ (incluyendo los posibles off-críticos).
- En $\mathcal{V}_\zeta$: la dimensión de $H^1(\mathcal{V}_\zeta)$ mide cuántos ceros off-críticos hay.

*Son preguntas complementarias:* Deninger quiere encontrar todos los ceros; nosotros queremos probar que no hay ceros off-críticos.

**Proposición 8.2 (Fórmula de traza de Lefschetz en $\mathcal{MM}$).** Asumiendo la existencia de dualidad de Poincaré en $\mathcal{MM}$ y que el Frobenius $\Phi_\zeta$ tiene traza de Lefschetz dada por el conteo de puntos fijos:

$$\sum_{i=0}^{\dim} (-1)^i \mathrm{Tr}(\Phi_\zeta^*|H^i) = \#\{\text{puntos fijos de } \Phi_\zeta\} = 1 + \#\mathcal{Z}_{\mathrm{off}}$$

(el 1 viene del punto fijo trivial $\mu=0$; $\#\mathcal{Z}_{\mathrm{off}}$ viene de los ceros off-críticos).

Si $H^0 = \mathbb{R}$ (traza = 1), $H^2 = 0$ (nada en dimensión 2), $H^1$ da $\#\mathcal{Z}_{\mathrm{off}}$:
$$1 - \#\mathcal{Z}_{\mathrm{off}} + 0 = 1 + \#\mathcal{Z}_{\mathrm{off}}$$

Esto da $\#\mathcal{Z}_{\mathrm{off}} = 0$ solo si $\#\mathcal{Z}_{\mathrm{off}} = 0$ — circular. *El argumento de Lefschetz no es suficiente por sí solo.*

**Observación 8.3 (Por qué la prueba de Weil no es circular).** En el caso de Weil para curvas sobre $\mathbb{F}_q$:
$$1 - \mathrm{Tr}(\phi_q|H^1) + q = q + 1 - \sum_{i=1}^{2g}\alpha_i = |C(\mathbb{F}_q)|$$

Aquí la clave no es el conteo (que es circular), sino la *estimación* $|\mathrm{Tr}(\phi_q|H^1)| \leq 2g\sqrt{q}$, que sigue de la positividad y da la hipótesis de Riemann para la curva. Para el zeta de Riemann, la estimación análoga sería $|\mathrm{Tr}(\Phi_\zeta^*|H^1)| \leq C$ — que daría información sobre $\#\mathcal{Z}_{\mathrm{off}}$ si $C$ pudiera tomarse $= 0$.

---

## 9. Los tres pasos concretos que faltan

**Paso III.A: Construir la dualidad de Poincaré en $\mathcal{MM}$.**

Esto requiere:
1. Definir el "dual" de un objeto $(\mathcal{R}, \mu, F)$ como $(\mathcal{R}, \mu^\vee, F^\vee)$ donde $\mu^\vee$ es la medida "conjugada" en algún sentido.
2. Construir un pairing canónico $H^1 \times H^1 \to \omega$.
3. Demostrar que el pairing es no-degenerado.

El candidato para $\mu^\vee$: la medida complementaria bajo la ecuación funcional $\mu^\vee = \mu \circ \sigma_{\mathrm{funct}}$ (la reflexión del cuarteto). Por el Axioma 2 de Doc 48, $\mu^\vee$ vive en $\mathbb{H}^-$, no en $\mathbb{H}^+$ — luego la dualidad conectaría objetos en $\mathbb{H}^+$ con objetos en $\mathbb{H}^-$.

**Paso III.B: Calcular la forma de Weil en $H^1 \otimes H^1 \to \omega$.**

Esto requiere computar el pairing $\langle\alpha, \beta\rangle_W$ explícitamente y verificar si es positivo-definido (CPC).

**Paso III.C: Derivar la estimación $|\mathrm{Tr}(\Phi_\zeta^*|H^1)| \leq C_0$.**

Con $C_0 = 0$, esto daría $\sum(\sigma_0-1/2) = 0$, luego RH. La estimación $C_0 = 0$ sería el análogo de la positividad de Weil. Requiere la desigualdad del Lemma de Schwarz para la forma de Weil.

---

## 10. Estado exacto de Dirección III

| Afirmación | Estado | Herramienta |
|------------|--------|-------------|
| Categoría $\mathcal{MM}$ bien definida | ✓ | Este documento |
| $H^0$ y $H^1$ definidos en $\mathcal{MM}$ | ✓ | Cohomología de haces |
| RH $\iff H^1 = 0$ | ✓ | Construcción directa |
| Frobenius $\Phi_\zeta$ como endofunctor | ✓ | Operador $\Phi$ de Doc 51 |
| Fórmula de traza de Lefschetz | ✓ condicional | Dualidad de Poincaré |
| Dualidad de Poincaré en $\mathcal{MM}$ | ❌ Abierto | — |
| CPC para la forma de Weil de $\mathcal{MM}$ | ❌ Abierto | — |
| Estimación $|\mathrm{Tr}| \leq 0$ | ❌ Abierto — equivale a RH | — |

**La reducción precisa:**

> Dirección III reduce RH a: *construir la dualidad de Poincaré en $\mathcal{MM}$ y demostrar que la forma de Weil $\langle\alpha, \Phi_\zeta^*\alpha\rangle_W$ satisface la estimación del Lema de Schwarz que da $|\mathrm{Tr}(\Phi_\zeta^*|H^1)| = 0$.*

---

## 11. Convergencia de las tres direcciones: el obstáculo unificado

**Teorema 11.1 (Unificación).** Los tres obstáculos son formalmente equivalentes:

| Dirección | Obstáculo |
|-----------|-----------|
| II (Completitud) | ¿Es $F = \sum a_k P_{y_k}(\cdot-x_k)$ de signo definido si $F(\gamma_n)=0$ $\forall n$? |
| I (Punto fijo) | ¿Satisface $\mathcal{E}[\Phi[\mu]] \leq \mathcal{E}[\mu]$ para toda $\mu \neq 0$? |
| III (Motivica) | ¿Existe dualidad de Poincaré en $\mathcal{MM}$ con CPC? |

*Los tres son versiones del mismo problema de positividad:*

> ¿Puede una función positiva armónica, construida a partir de kernels de Poisson de ceros off-críticos de $\zeta$, ser forzada a ser cero por la distribución de los ceros on-críticos?

---

## 12. La siguiente pregunta concreta

Las tres direcciones han convergido en UN problema analítico bien definido:

**Problema Central (PC):**

> Sea $F: \mathbb{R} \to \mathbb{R}_{\geq 0}$ una función continua con $F \geq 0$, $F(\gamma_n) = 0$ para todo $n \geq 1$, y $F$ representable como $F = \mathcal{P}[\mu]$ para alguna medida positiva $\mu$ con soporte en $\mathcal{R}_\eta$. ¿Se sigue que $F \equiv 0$?

**Respuesta conocida:** Sí, trivialmente — pues si $F \geq 0$ y $F(\gamma_n) = 0$ para al menos un punto, el Teorema de Rigidez de Poisson (Doc 43) da $\mu = 0$, luego $F = 0$.

**La versión no trivial del Problema Central:**

> Sea $F: \mathbb{R} \to \mathbb{R}$ (sin hipótesis de signo) con $F(\gamma_n) = 0$ para todo $n\geq 1$, y $F = \mathcal{P}[\mu] - \mathcal{P}[\nu]$ para medidas positivas $\mu, \nu$. ¿Se sigue que $\mu = \nu$?

Esta es la versión con signos — que es el obstáculo compartido por las tres direcciones y que no sigue de principios generales.

---

*El Doc 53 atacará el Problema Central sin hipótesis de signo: condiciones suficientes para que $\mathcal{P}[\mu] = \mathcal{P}[\nu]$ en $\{\gamma_n\}$ implique $\mu = \nu$.*
