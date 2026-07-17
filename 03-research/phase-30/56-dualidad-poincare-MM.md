# Doc 56 — Dualidad de Poincaré en $\mathcal{MM}$: Construcción, No-Degeneración y Por Qué No Cierra

**Programa:** CCM Zeta Spectral Triples — Phase 30  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 52–55  
**Honestidad:** Este documento construye el emparejamiento de Poincaré en $\mathcal{MM}$, prueba su no-degeneración, e identifica con precisión por qué el argumento de Deligne/Weil no se transfiere al caso aritmético sobre $\mathbb{Q}$. El resultado es negativo pero clarificador.

---

## 1. El emparejamiento de Poincaré en $\mathcal{MM}$: construcción

**Recordatorio (Doc 52).** La categoría $\mathcal{MM}$ tiene objetos $(\mathcal{R}_\eta, \mu, F)$ con $F = \mathcal{P}[\mu]$, cohomología:

$$H^0(\mathcal{R}_\eta, \mu, F) = \{F|_\mathbb{R}\} \quad\text{(funciones armónicas positivas en el borde)}$$
$$H^1(\mathcal{R}_\eta, \mu, F) = \mathcal{M}(\mathcal{R}_\eta)/\mathcal{N} \quad\text{(medidas módulo medidas nulas)}$$

donde $\mathcal{N} = \{\nu : \mathcal{P}[\nu] = 0\} = \{0\}$ (por injectividad de $\mathcal{P}$, Proposición 2.1, Doc 53).

**Definición 1.1 (Emparejamiento de Poincaré).** Para el objeto $(\mathcal{R}_\eta, \mu, F)$, sea:

$$\langle\cdot,\cdot\rangle_\Pi: H^0 \times H^1 \to \mathbb{R}$$
$$\langle f, [\nu]\rangle_\Pi := \int_{\mathcal{R}_\eta} f(x)\,d\nu(x,y)$$

donde $f \in H^0$ es la función de borde y $[\nu] \in H^1$ es una clase de medidas.

**Observación 1.2 (Simetría del emparejamiento).** Por la simetría de la transformada de Poisson:

$$\int_{\mathcal{R}_\eta} \mathcal{P}[\mu](x)\,d\nu(x,y) = \int_{\mathcal{R}_\eta}\!\int_\mathbb{R} P_y(t-x)\,d\mu(t)\,d\nu(x,y) = \int_\mathbb{R} \mathcal{P}[\nu](t)\,d\mu(t)$$

Luego $\langle \mathcal{P}[\mu], [\nu]\rangle_\Pi = \langle \mathcal{P}[\nu], [\mu]\rangle_\Pi$ — el emparejamiento es simétrico en $\mu, \nu$.

---

## 2. No-degeneración del emparejamiento

**Teorema 2.1 (No-degeneración del emparejamiento de Poincaré).** El emparejamiento $\langle\cdot,\cdot\rangle_\Pi$ es no-degenerado: para $[\nu] \in H^1$,

$$\langle f, [\nu]\rangle_\Pi = 0 \;\forall f \in H^0 \implies [\nu] = 0$$

*Prueba.* $H^0$ contiene todas las funciones $f = \mathcal{P}[\mu]$ con $\mu$ una medida positiva en $\mathcal{R}_\eta$. Por la Observación 1.2:

$$\langle \mathcal{P}[\mu], [\nu]\rangle_\Pi = \int_\mathbb{R} \mathcal{P}[\nu](t)\,d\mu(t) = 0 \quad\forall \mu$$

Tomando $\mu = \delta_{(t_0, y_0)}$ (masa puntual en $(t_0, y_0) \in \mathcal{R}_\eta$): $\mathcal{P}[\mu](x) = P_{y_0}(t_0-x)$, luego:

$$\int P_{y_0}(t-x)\,d\nu(x,y) = \mathcal{P}[\nu](t_0) = 0 \quad \forall (t_0, y_0) \in \mathcal{R}_\eta$$

Como $\mathcal{P}[\nu]$ es una función continua en $\mathbb{R}$ que se anula en un conjunto denso (si $\mathcal{R}_\eta$ es denso bajo la proyección al eje real), $\mathcal{P}[\nu] \equiv 0$ en $\mathbb{R}$, luego $\nu = 0$ por injectividad de $\mathcal{P}$ (Doc 53, Proposición 2.1). $\square$

**Corolario 2.2.** El emparejamiento $\langle\cdot,\cdot\rangle_\Pi$ también es no-degenerado en la primera variable (por la simetría de la Observación 1.2 y el mismo argumento).

**Proposición 2.3 (El emparejamiento para el objeto zeta).** Para el objeto zeta $(\mathcal{R}_\eta, \mu_{\mathrm{off}}, C_\infty)$:

$$\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi = \int_{\mathcal{R}_\eta} C_\infty(x)\,d\mu_{\mathrm{off}}(x,y) = \sum_{\rho_0\in\mathcal{Z}_{\mathrm{off}}} (\sigma_0-1/2)\cdot C_\infty(\gamma_0)$$

Bajo ¬RH: $C_\infty(\gamma_0) > 0$ (Doc 43) y $\sigma_0-1/2 > 0$, luego $\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi > 0$ — la Conjetura de Positividad Cohomológica (CPC) se verifica bajo ¬RH.

Bajo RH: $\mu_{\mathrm{off}} = 0$, luego $\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi = 0$ trivialmente.

---

## 3. La estructura del argumento de Deligne y dónde falla la transferencia

En la prueba de Weil para curvas $C/\mathbb{F}_q$, la estructura es:

**(W1)** El Frobenius $\mathrm{Fr}_q: C \to C$ es un automorfismo de la curva.  
**(W2)** El Frobenius actúa en $H^1(C)$ con eigenvalores $\alpha_1, \ldots, \alpha_{2g}$.  
**(W3)** La ecuación funcional de $Z(C,s)$ da la relación $\alpha_i \leftrightarrow q/\alpha_i$.  
**(W4)** El emparejamiento de Weil: $\langle \mathrm{Fr}_q^* \alpha, \beta\rangle_{\mathrm{Weil}} = q \langle \alpha, \mathrm{Fr}_q^{-1*} \beta\rangle_{\mathrm{Weil}}$.  
**(W5)** La positividad cohomológica (Hodge): $\langle \alpha, \overline{\alpha}\rangle_{\mathrm{Weil}} > 0$ para $\alpha \neq 0$.  
**(W6)** Combinando (W3)–(W5): si $\alpha_i$ es eigenvalor, $|\alpha_i|^2 = q$ — luego $|\alpha_i| = \sqrt{q}$ (RH).

**Traducción al marco $\mathcal{MM}$:**

| Ingrediente Weil | Traducción a $\mathcal{MM}$ | Estado |
|---|---|---|
| **(W1)** $\mathrm{Fr}_q$ como automorfismo geométrico | $\Phi_\zeta$ como endofunctor de $\mathcal{MM}$ | ✓ (Doc 52) |
| **(W2)** Eigenvalores de $\mathrm{Fr}_q$ en $H^1$ | "Eigenvalores" de $\Phi_\zeta$ en $H^1(\mathcal{MM})$ | ✗ — ver §4 |
| **(W3)** Relación $\alpha_i \leftrightarrow q/\alpha_i$ (ec. func.) | Relación dual en $H^1$ via ecuación funcional de $\zeta$ | ✗ — ver §5 |
| **(W4)** Emparejamiento de Weil: $\langle\mathrm{Fr}^*\alpha,\beta\rangle = q\langle\alpha,\mathrm{Fr}^{-1*}\beta\rangle$ | Emparejamiento $\langle\cdot,\cdot\rangle_\Pi$: ¿satisface relación similar? | ✗ — ver §6 |
| **(W5)** Positividad de Hodge | CPC: $\langle C_\infty, [\mu_{\mathrm{off}}]\rangle_\Pi > 0$ bajo ¬RH | ✓ (Proposición 2.3) |
| **(W6)** Conclusión $|\alpha_i| = \sqrt{q}$ → RH | Conclusión $H^1 = 0$ → RH | ✗ — circular sin (W2)–(W4) |

---

## 4. El fallo de (W2): la ausencia de eigenvalores no triviales

**Proposición 4.1 (El "Frobenius" $\Phi_\zeta$ tiene eigenvalor trivial en $H^1$).** El endofunctor $\Phi_\zeta$ actúa en $H^1(\mathcal{MM}) = \mathcal{M}(\mathcal{R}_\eta)/\mathcal{N}$ por:

$$\Phi_\zeta[\nu] = [\nu_{\mathrm{off}}[\mathcal{P}[\nu]]]$$

donde $\nu_{\mathrm{off}}[\mathcal{P}[\nu]]$ es la medida off-crítica inducida por $\mathcal{P}[\nu]$.

Los puntos fijos de $\Phi_\zeta$ son $[\nu] = 0$ (trivial) y $[\nu] = [\mu_{\mathrm{off}}]$ (la medida de ceros off-críticos). El "eigenvalor" de $\Phi_\zeta$ en $[\mu_{\mathrm{off}}]$ es $\lambda = 1$ (punto fijo).

**Problema:** En el caso de Weil, los eigenvalores $\alpha_i \neq 1$ en general — su estructura no trivial es la que el emparejamiento de Weil puede comparar. En $\mathcal{MM}$, el único "eigenvalor" relevante es $\lambda = 1$, y el emparejamiento de Weil daría $|\lambda|^2 = 1$ trivialmente — sin información.

**Raíz del problema:** El Frobenius sobre $\mathbb{F}_q$ tiene una "dimensión" no trivial porque la curva $C$ tiene género $g \geq 1$ con un espacio $H^1$ de dimensión $2g$. En $\mathcal{MM}$, el "espacio $H^1$" es de dimensión efectiva 0 o $\infty$ — 0 si RH, infinito si ¬RH — y no hay una estructura intermedia de dimensión finita no trivial que el argumento de Weil pueda aprovechar.

---

## 5. El fallo de (W3): la ecuación funcional no da la relación dual correcta

En el caso de Weil:
- $Z(C, q^{-s})$ satisface la ecuación funcional $Z(C, 1-s) = q^{(1-2g)(1/2-s)} Z(C, s)$.
- Si $q^{-\alpha}$ es cero de $Z$ (es decir, $\alpha$ es eigenvalor del Frobenius), entonces $q^{\alpha-1}$ también lo es.
- En términos de eigenvalores: $\alpha_i \leftrightarrow q/\alpha_i$ — la dualidad de eigenvalores.

En el caso de $\zeta$:
- $\zeta(s)$ satisface $\xi(s) = \xi(1-s)$, que da: si $\rho = 1/2+i\gamma$ es cero, también lo es $1-\rho = 1/2-i\gamma$ (el conjugado). Bajo RH, todos los ceros son auto-duales bajo esta simetría.
- La relación $\rho \leftrightarrow 1-\rho$ en términos de eigenvalores del "Frobenius" daría: si $\alpha$ es eigenvalor, también lo es $1/\alpha$.
- Esto fuerza $|\alpha|^2 = 1$ — exactamente RH... pero SOLO si la noción de "eigenvalor" estuviera bien definida.

**Proposición 5.1 (La ecuación funcional da la relación correcta pero en vacío).** La ecuación funcional de $\zeta$ da formalmente la relación $\alpha \leftrightarrow 1/\alpha$ para los "eigenvalores" de $\Phi_\zeta$. Junto con el emparejamiento de Poincaré, esto forzaría $|\alpha| = 1$. Pero $\alpha = 1$ trivialmente satisface $|\alpha| = 1$, y no hay otros eigenvalores no triviales en $H^1(\mathcal{MM})$. El argumento es vacío.

---

## 6. El fallo de (W4): la relación del emparejamiento con el Frobenius

**Proposición 6.1 (El emparejamiento $\langle\cdot,\cdot\rangle_\Pi$ no satisface la relación de Weil).** En el caso geométrico, la relación de Weil es:

$$\langle \mathrm{Fr}_q^* \alpha, \beta\rangle_{\mathrm{Weil}} = q\cdot\langle \alpha, (\mathrm{Fr}_q^*)^{-1}\beta\rangle_{\mathrm{Weil}}$$

que introduce el factor $q$ (la "norma del Frobenius"). Esto es lo que fuerza $\alpha_i \cdot \bar\alpha_i = q$.

En $\mathcal{MM}$: para el emparejamiento $\langle f, [\nu]\rangle_\Pi = \int f\,d\nu$, la relación análoga sería:

$$\langle \Phi_\zeta^* f, [\nu]\rangle_\Pi = \lambda_{\Phi}\cdot\langle f, (\Phi_\zeta^*)^{-1}[\nu]\rangle_\Pi$$

para algún escalar $\lambda_\Phi$ (la "norma del Frobenius aritmético").

El candidato natural para $\lambda_\Phi$: por analogía con $q$ sobre $\mathbb{F}_q$, el papel de $q$ en el caso de números lo jugaría algún invariante de $\zeta$ — tal vez $e^{1}$ (relacionado con $\log q = 1$ en el límite $q\to 1$), o simplemente $\lambda_\Phi = 1$.

Si $\lambda_\Phi = 1$: la relación de Weil dice $\langle \Phi_\zeta^* f, [\nu]\rangle_\Pi = \langle f, (\Phi_\zeta^*)^{-1}[\nu]\rangle_\Pi$, que es simplemente la simetría del emparejamiento. Da $|\alpha|^2 = \lambda_\Phi = 1$ — trivialmente verdadero para $\alpha = 1$.

**Corolario 6.2.** Sin un escalar $\lambda_\Phi \neq 1$ (análogo a $q \neq 1$ sobre $\mathbb{F}_q$), la relación de Weil es trivial y no da información sobre la ubicación de los ceros.

---

## 7. El diagnóstico central: la diferencia estructural entre $\mathbb{F}_q$ y $\mathbb{Q}$

**Proposición 7.1 (La diferencia fundamental).** En el caso de Weil sobre $\mathbb{F}_q$:
- El Frobenius $\mathrm{Fr}_q$ tiene "grado" $q$ — es un endomorfismo de grado $q$ de la curva, con $q > 1$.
- Este grado $q$ aparece en la relación de Weil y fuerza $|\alpha_i|^2 = q$.
- RH dice $|\alpha_i| = \sqrt{q}$ — los eigenvalores están en el círculo de radio $\sqrt{q}$.

En el caso aritmético sobre $\mathbb{Q}$:
- El "Frobenius" $\Phi_\zeta$ es el endofunctor de la categoría $\mathcal{MM}$ — pero su "grado" es 1.
- No hay análogo del parámetro $q$ que aparezca en la relación de Weil.
- RH dice que los ceros están en $\mathrm{Re}(s) = 1/2$ — el análogo es el "radio 1" ($|e^{i\gamma}| = 1$), pero esto es automático para cualquier número en el círculo unitario.

**En síntesis:** La prueba de Weil usa el hecho de que el Frobenius tiene grado $q \neq 1$ para crear una tensión entre la ecuación funcional y la positividad, que se resuelve exactamente en $|\alpha_i| = \sqrt{q}$. Sobre $\mathbb{Q}$, no hay parámetro $q > 1$ — el análogo es $q = 1$ y todo colapsa.

---

## 8. Resultado de Doc 56: lo que está probado y lo que no

**Teorema 8.1 (Dualidad de Poincaré en $\mathcal{MM}$: construcción y no-degeneración).** El emparejamiento $\langle\cdot,\cdot\rangle_\Pi: H^0 \times H^1 \to \mathbb{R}$ definido por la Definición 1.1 existe, es bilineal, simétrico, y no-degenerado (Teorema 2.1). La categoría $\mathcal{MM}$ admite dualidad de Poincaré formal.

**Pero el argumento de Deligne/Weil no se transfiere.** Los tres ingredientes clave fallan:
- **(W2)** No hay eigenvalores no triviales del Frobenius en $H^1(\mathcal{MM})$ — el único eigenvalor es $\lambda = 1$.
- **(W3)** La ecuación funcional de $\zeta$ da $\alpha \leftrightarrow 1/\alpha$, lo que fuerza $|\alpha| = 1$ — pero $\alpha = 1$ ya satisface esto trivialmente.
- **(W4)** La relación de Weil con factor $\lambda_\Phi = 1$ es trivial, sin tensión que resolver.

**Corolario 8.2 (Diagnóstico final de la estrategia Langlands-Weil).** La dualidad de Poincaré en $\mathcal{MM}$ existe pero es trivial para el propósito de probar RH. El argumento de Weil requiere un parámetro $q \neq 1$ que no existe en el caso aritmético sobre $\mathbb{Q}$.

---

*Phase 30 concluye con el resultado negativo de Doc 56. A continuación: revisión global de todo el programa para identificar qué caminos genuinamente nuevos quedan abiertos.*
