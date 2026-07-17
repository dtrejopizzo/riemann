# Phase 29 — Doc 29: Geometría Espectral del Cociente $C_\infty / \Xi$ 

**Fecha:** junio 2026  
**Contexto:** El Doc 28 identificó el Frente C como el más prometedor: estudiar el cociente $Q(z) := C_\infty(z)/\Xi(z)$ o equivalentemente la diferencia $C_\infty'/C_\infty(z) - \Xi'/\Xi(z)$, con el objetivo de probar que $Q$ no tiene ceros ni polos en $\mathbb{R}$ (que equivale a Inc. Inv. + la inclusión directa). 

**Objetivo:** Estudiar el cociente $Q = C_\infty/\Xi$ como función meromorfa en $\mathbb{C}^+$, determinar su comportamiento en $\mathbb{R}$, y buscar un principio que fuerce $Q(\mathbb{R}) \subseteq \mathbb{R}\setminus\{0\}$ (sin ceros ni polos en $\mathbb{R}$), lo que implica RH.

---

## 1. Definición y propiedades básicas del cociente

**Definición.** Sea

$$Q(z) := \frac{C_\infty(z)}{\Xi(z)}, \quad z \in \mathbb{C}^+.$$

**Proposición 1** (propiedades de $Q$).

(a) $C_\infty(z)$ es holomorfa en $\mathbb{C}^+$: pues $C_\infty(t) = w(t) - \Psi(t)$ donde ambas son funciones analíticas que extienden a $\mathbb{C}^+$ con $\Im(C_\infty(z)) = \Im(w(z)) - \Im(\Psi(z))$ absolutamente convergente para $\Im(z) > 0$.

(b) $\Xi(z)$ es holomorfa en $\mathbb{C}^+$ y no tiene ceros en $\mathbb{C}^+$: pues los ceros de $\Xi$ están todos en $\mathbb{R}$ (los $\gamma_n$) bajo RH, y en la franja $0 < \Im(\rho) < 1/2$ para los ceros fuera de la recta crítica (bajo $\neg$RH).

(c) Bajo RH: $Q(z)$ es holomorfa en $\mathbb{C}^+$ (pues $\Xi \neq 0$ en $\mathbb{C}^+$ y $C_\infty$ holomorfa).

(d) Bajo $\neg$RH: $\Xi$ tiene ceros $\rho_0$ en $0 < \Im(\rho_0) < 1/2$, que son polos de $Q$.

**Proposición 2** (comportamiento de $Q$ en $\mathbb{R}$). El cociente $Q$ tiene:
- Polos en $\mathbb{R}$ en los ceros de $\Xi$ que NO son ceros de $C_\infty$ (ceros faltantes).
- Ceros en $\mathbb{R}$ en los ceros de $C_\infty$ que NO son ceros de $\Xi$ — pero por Teorema B (Doc 19): $\{$ceros de $C_\infty\} \subseteq \{$ceros de $\Xi\}$, por tanto NO hay ceros de $C_\infty$ en $\mathbb{R}$ que no sean ceros de $\Xi$.

En particular: $Q$ es holomorfa en los ceros de $C_\infty$ y tiene polos simples en los ceros de $\Xi$ que no son ceros de $C_\infty$.

---

## 2. La reformulación en términos de $Q$

**Proposición 3** (Inc. Inv. $\Leftrightarrow$ $Q$ holomorfa en $\mathbb{R}$). Las siguientes son equivalentes:

(i) Inc. Inv.: $\Ξ(\gamma_n) = 0 \Rightarrow C_\infty(\gamma_n) = 0$ para todo $n$.

(ii) $Q(z) = C_\infty(z)/\Xi(z)$ extiende holomorfamente a un entorno de $\mathbb{R}$ (sin polos en $\mathbb{R}$).

(iii) $Q$ es holomorfa en $\mathbb{C}^+\cup\mathbb{R}$ (en la clausura del semiplano superior).

*Prueba.* (i)$\Rightarrow$(ii): Si $C_\infty(\gamma_n) = 0$ siempre que $\Xi(\gamma_n) = 0$, los ceros de $\Xi$ en $\mathbb{R}$ son también ceros de $C_\infty$ (con al menos la misma multiplicidad), luego los polos de $Q$ en $\mathbb{R}$ se cancelan. (ii)$\Rightarrow$(i): si $Q$ es holomorfa en $\mathbb{R}$, no tiene polos, luego $C_\infty(\gamma_n) = 0$ para todo $n$. $\square$

**Proposición 4** (RH $\Leftrightarrow$ $Q$ meromorfa en $\mathbb{C}$ con ceros/polos solo en $\mathbb{R}$). Equivalentemente: RH $\Leftrightarrow$ $Q$ es holomorfa en $\mathbb{C}\setminus\mathbb{R}$ (sin singularidades fuera de $\mathbb{R}$) Y $Q$ no tiene polos en $\mathbb{R}$.

*Prueba.* $\Rightarrow$: Bajo RH, $\Xi$ no tiene ceros en $\mathbb{C}^+$ (ni en $\mathbb{C}^-$ por simetría), luego $Q$ es holomorfa en $\mathbb{C}^+$. Y por Inc. Inv. (que es RH), $Q$ no tiene polos en $\mathbb{R}$. Luego $Q$ es holomorfa en $\mathbb{C}\setminus\mathbb{R}$ y en $\mathbb{R}$ (salvo posibles ceros de $C_\infty$ en $\mathbb{R}$, que son ceros de $Q$, no polos). $\Leftarrow$: Si $Q$ es holomorfa en $\mathbb{C}^+$, los ceros de $\Xi$ están todos en $\mathbb{R}$ (RH). Si además $Q$ no tiene polos en $\mathbb{R}$: Inc. Inv. Juntos dan RH. $\square$

---

## 3. Las funciones $C_\infty$ y $\Xi$ como funciones de tipo exponencial

**Proposición 5** (tipo exponencial de $C_\infty$ y $\Xi$). En el semiplano superior $\mathbb{C}^+$:

(a) $\Xi(z) = \xi(1/2+iz)$ es una función entera de tipo exponencial $\pi/2$ (de la teoría de Hadamard).

(b) $C_\infty(z) = w(z) - \Psi(z)$ con $w(z)$ el símbolo archimédeo y $\Psi(z) = 2\sum_p \Lambda(p)p^{-1/2}e^{iz\log p}$.

Para $z \in \mathbb{C}^+$: $|\Psi(z)| \leq 2\sum_p\Lambda(p)p^{-1/2-\Im(z)} < \infty$ para $\Im(z) > 0$. La función $\Psi$ se extiende analíticamente a $\mathbb{C}^+$ pero NO es entera (la serie diverge en $\mathbb{R}$ condicionalmente).

(c) $C_\infty$ es holomorfa en $\mathbb{C}^+$ pero NO entera: tiene singularidades en la recta real y en la franja $0 \leq \Im(z) \leq 1$ (de los términos $e^{iz\log p}$ para primos $p$).

**Corolario 1** (tipo del cociente $Q$). El cociente $Q = C_\infty/\Xi$ NO es una función entera en general (pues $C_\infty$ no lo es). $Q$ es meromorfa en $\mathbb{C}^+$ con posibles singularidades en la frontera $\mathbb{R}$.

---

## 4. El cociente $Q$ y la función de Hardy $H^2$

**Definición.** Decimos que $Q \in H^2(\mathbb{C}^+)$ (clase de Hardy) si:

$$\sup_{\eta > 0}\int_{-\infty}^\infty |Q(t+i\eta)|^2 dt < \infty.$$

**Proposición 6** (condición de $H^2$ para $Q$). Si $Q \in H^2(\mathbb{C}^+)$ y $Q$ es holomorfa en $\mathbb{C}^+$:

- $Q$ tiene valores no-tangenciales en $\mathbb{R}$ c.e. (por la teoría de Hardy).
- Los polos de $Q$ en $\mathbb{R}$ serían singularidades de los valores no-tangenciales.

**Proposición 7** (cota en $H^\infty$ de $Q$). Para $z \in \mathbb{C}^+$:

$$|Q(z)| = \left|\frac{C_\infty(z)}{\Xi(z)}\right| \leq \frac{|w(z)| + |\Psi(z)|}{|\Xi(z)|}.$$

El denominador $|\Xi(z)|$ para $z = t+i\eta$ con $\eta > 0$: $|\Xi(z)| \geq |\Xi(0)|\prod_n(1 - (t+i\eta)^2/\gamma_n^2)|$ que se puede acotar inferiormente.

Para $t$ lejos de todos los $\gamma_n$ y $\eta \to 0$: $|\Xi(t+i\eta)| \to |\Xi(t)|$ que puede ser pequeño si $t$ es cercano a un $\gamma_n$.

**El problema de acotación de $Q$.** Para probar que $Q$ se extiende holomorfamente a $\mathbb{R}$ (sin polos), necesitamos que $|Q(t+i\eta)|$ permanezca acotado cuando $\eta\to 0^+$ y $t\to\gamma_n$. Esto requiere que $|C_\infty(t+i\eta)/\Xi(t+i\eta)|$ no diverja, lo que a su vez requiere $C_\infty(\gamma_n) = 0$ — es nuevamente Inc. Inv.

---

## 5. El principio máximo y sus consecuencias

**Proposición 8** (aplicación del principio máximo). Sea $f: \mathbb{C}^+ \to \mathbb{C}$ holomorfa y acotada. Si $|f|$ toma su máximo en la frontera $\mathbb{R}$, entonces $|f|$ es constante (por el principio máximo).

Para el cociente $Q$: si $Q$ es holomorfa en $\mathbb{C}^+$ (bajo RH) y $|Q(t)|$ está acotado en $\mathbb{R}$ para $t$ lejos de los $\gamma_n$, el principio máximo controla $Q$ en $\mathbb{C}^+$.

Pero el control de $|Q|$ en $\mathbb{R}$ cerca de los $\gamma_n$ es exactamente Inc. Inv. — circular.

**Proposición 9** (principio de reflexión de Schwarz). Si $C_\infty$ y $\Xi$ satisfacen simetrías reales ($\overline{C_\infty(\bar z)} = C_\infty(z)$ y $\overline{\Xi(\bar z)} = \Xi(z)$ para $z$ en el dominio apropiado):

$$Q(\bar z) = \overline{Q(z)}.$$

Esta simetría dice que $Q(t) \in \mathbb{R}$ para $t \in \mathbb{R}$ donde $Q$ está definida. Luego los "ceros" de $Q$ en $\mathbb{R}$ son ceros reales de una función real, y los "polos" de $Q$ en $\mathbb{R}$ son polos reales.

*Verificación de la simetría.* $C_\infty(t) = w(t) - \Psi(t)$ con $w$ y $\Psi$ reales en $\mathbb{R}$, luego $C_\infty$ es real en $\mathbb{R}$. $\Xi(t)$ es real en $\mathbb{R}$ (pues $\xi(1/2+it)$ es real para $t$ real). Luego $Q(t) = C_\infty(t)/\Xi(t) \in \mathbb{R}$ donde está definida.

**Conclusión de la simetría.** $Q$ es una función meromorfa en $\mathbb{C}$ que mapea $\mathbb{R} \to \mathbb{R}\cup\{\infty\}$. Los polos de $Q$ en $\mathbb{R}$ son puntos donde $\Xi(\gamma_n) = 0$ pero $C_\infty(\gamma_n) \neq 0$. Evitar estos polos es exactamente Inc. Inv.

---

## 6. La función $Q$ y la transformación de Blaschke

**Idea nueva.** Consideremos la función de Blaschke generalizada:

$$B_Q(z) := \exp\left(i\int_{-\infty}^\infty \frac{1+tz}{t-z}\cdot\frac{d\mu_{C_\infty}(t) - d\mu_\Xi(t)}{1+t^2}\right),$$

donde $\mu_{C_\infty}$ es la medida de ceros de $C_\infty$ y $\mu_\Xi$ es la medida de ceros de $\Xi$. Formalmente:

$$B_Q(z) = \frac{C_\infty(z)/C_\infty(0)}{\Xi(z)/\Xi(0)} \cdot \exp(\text{parte entera}).$$

Si $B_Q = 1$ (la parte de Blaschke de $Q$ es trivial): los ceros y polos de $C_\infty/\Xi$ se cancelan, lo que da Inc. Inv.

**Proposición 10** (Inc. Inv. y la trivialidad de la parte de Blaschke). $B_Q = 1$ (en el sentido de que la función de Blaschke generada por la diferencia de medidas de ceros es trivial) si y solo si $\mu_{C_\infty} = \mu_\Xi$, que es exactamente Inc. Inv.

*Prueba.* La función de Blaschke de $Q$ está generada por los polos de $Q$ en $\mathbb{R}$ (ceros de $\Xi$ no cubiertos por $C_\infty$). Si no hay tales polos: $B_Q = 1$. $\square$

**El problema.** Probar que $B_Q = 1$ incondicionalmente es equivalente a Inc. Inv. No hay principio general que fuerce la trivialidad de la función de Blaschke de $Q$.

---

## 7. Un ángulo genuinamente nuevo: la función $Q$ como cociente de Nevanlinna

**Definición.** Una función meromorfa $f: \mathbb{C}^+ \to \mathbb{C}$ es de clase de Nevanlinna ($f \in \mathcal{N}$) si:

$$\sup_{\eta > 0}\int_{-\infty}^\infty \log^+|f(t+i\eta)|\frac{dt}{1+t^2} < \infty.$$

**Proposición 11** ($Q \in \mathcal{N}$). La función $Q = C_\infty/\Xi$ está en la clase de Nevanlinna $\mathcal{N}$ bajo condiciones suaves sobre $C_\infty$.

*Prueba.* $\log^+|Q| \leq \log^+|C_\infty| + \log^+|1/\Xi|$. El término $\log^+|C_\infty|$ es integrable pues $C_\infty$ está acotada en $\mathbb{C}^+$. El término $\log^+|1/\Xi|$ requiere una cota inferior sobre $|\Xi|$ en $\mathbb{C}^+$ lejos de los ceros — esto es estándar para funciones enteras de tipo exponencial. $\square$

**El teorema de factorización de Nevanlinna.** Para $f \in \mathcal{N}$:

$$f(z) = B(z)\cdot S(z)\cdot O(z),$$

donde $B$ = producto de Blaschke (ceros y polos en $\overline{\mathbb{C}^+}$), $S$ = factor singular (medida singular en $\mathbb{R}$), $O$ = factor exterior (función de log-modulus dado por la parte absolutamente continua).

**Proposición 12** (factorización de $Q$). 

$$Q(z) = \frac{C_\infty(z)}{\Xi(z)} = B_{C_\infty}(z)\cdot B_{1/\Xi}(z)\cdot O_Q(z)\cdot S_Q(z),$$

donde:
- $B_{C_\infty}$ = producto de Blaschke de los ceros de $C_\infty$ en $\overline{\mathbb{C}^+}$ (= los ceros en $\mathbb{R}$ bajo Teorema B).
- $B_{1/\Xi}$ = producto de "anti-Blaschke" de los ceros de $\Xi$ en $\overline{\mathbb{C}^+}$ (= los $\gamma_n$, bajo RH).
- $O_Q$ = factor exterior determinado por $|Q|$ en $\mathbb{R}$.
- $S_Q$ = factor singular.

Inc. Inv. dice: todos los $\gamma_n$ son ceros de $C_\infty$, luego $B_{C_\infty}$ cancela exactamente $B_{1/\Xi}$.

---

## 8. El factor exterior $O_Q$ y los primos

**La clave.** El factor exterior de $Q$ en $\mathbb{C}^+$ está completamente determinado por $|Q(t)|$ para $t \in \mathbb{R}$:

$$O_Q(z) = \exp\left(\frac{1}{\pi i}\int_{-\infty}^\infty \frac{1+tz}{(t-z)(1+t^2)}\log|Q(t)|dt\right).$$

El logaritmo $\log|Q(t)| = \log|C_\infty(t)| - \log|\Xi(t)|$.

**Proposición 13** (expresión de $\log|Q|$ en términos de primos). Para $t \notin \{\gamma_n\}$:

$$\log|C_\infty(t)| = \log|w(t) - \Psi(t)|,$$

donde $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$ (suma sobre primos, convergente condicionalmente para $t$ real).

Y $\log|\Xi(t)|$ está determinado por la distribución de ceros $\{\gamma_n\}$ via la fórmula de Jensen:

$$\log|\Xi(t)| = \log|\Xi(0)| + \int_0^\infty \log|1 - t^2/r^2|d\mu_\Xi(r) \quad (\text{por Hadamard}).$$

**La identidad en $\mathbb{R}$.** La función $\log|Q(t)| = \log|C_\infty(t)/\Xi(t)|$ conecta la distribución de primos (vía $\Psi$) con la distribución de ceros de $\Xi$. Si esta función es integrable en $\mathbb{R}$ (módulo los polos): el factor exterior $O_Q$ está determinado, y el programa se reduce a determinar si los ceros y polos de la parte de Blaschke se cancelan.

---

## 9. El resultado nuevo: imposibilidad de ceros "extra" de $C_\infty$

El Teorema B dice: los ceros de $C_\infty$ en $\mathbb{R}$ están todos en $\{$ceros de $\Xi\}$. La parte más importante para el cociente $Q$ es si hay ceros de $\Xi$ que NO son ceros de $C_\infty$ (los "ceros faltantes").

**Proposición 14** (estructure de los ceros faltantes). Supongamos que $\gamma_{n_0}$ es un cero de $\Xi$ que NO es cero de $C_\infty$ (un "cero faltante"). Entonces:

(a) $Q = C_\infty/\Xi$ tiene un polo simple en $\gamma_{n_0}$ con residuo $C_\infty(\gamma_{n_0})/\Xi'(\gamma_{n_0}) \neq 0$.

(b) El m-function $m_\infty^{WT}(z)$ (que tiene soporte $\subseteq\{$ceros de $C_\infty\}$) no tiene masa en $\gamma_{n_0}$.

(c) La medida espectral $\mu_{WT}^\infty$ da masa cero a $\gamma_{n_0}$: $\mu_{WT}^\infty(\{\gamma_{n_0}\}) = 0$.

(d) El eigenvalor $\gamma_{n_0} \in \text{spec}(J_\infty)$ (está en el espectro como eigenvalor) pero el vector propio $\psi_{n_0}^\infty$ satisface $\langle e_0, \psi_{n_0}^\infty\rangle = 0$ — el vector propio es ortogonal al estado inicial.

*Prueba.* (a) De la definición de $Q$. (b) De $\text{EF2}_{WT}$: soporte de $\mu_{WT}^\infty$ = ceros de $C_\infty$. (c) De (b). (d) De la interpretación de $\mu_{WT}^\infty$ como medida de Weyl-Titchmarsh: $\mu_{WT}^\infty(\{\gamma_{n_0}\}) = |\langle e_0, \psi_{n_0}^\infty\rangle|^2$. $\square$

**Teorema 1** (caracterización de los ceros faltantes). Los "ceros faltantes" (ceros de $\Xi$ que no son ceros de $C_\infty$) corresponden exactamente a los eigenvalores de $J_\infty$ cuyos vectores propios son INVISIBLES desde $e_0$, es decir, forman parte del espectro puntual de $J_\infty$ que NO aparece en la descomposición espectral de $e_0$.

*Prueba.* Directa de la Proposición 14. $\square$

---

## 10. Análisis de la "invisibilidad" desde $e_0$

**El espectro puntual invisible.** Para un operador de Jacobi $J$ semi-infinito, el espectro puntual se divide en:
- **Espectro visible desde $e_0$**: eigenvalores con $\langle e_0, \psi_n\rangle \neq 0$ (aparecen en $\mu_{WT}$).
- **Espectro invisible desde $e_0$**: eigenvalores con $\langle e_0, \psi_n\rangle = 0$ (no aparecen en $\mu_{WT}$).

Para el operador semi-infinito $J_\infty$ con $b_n^\infty = 0$ y $a_n^\infty = \pi/\log\gamma_n$:

**Proposición 15** (condición para invisibilidad). $\langle e_0, \psi_n^\infty\rangle = 0$ si y solo si el vector propio $\psi_n^\infty$ es ortogonal al estado inicial $e_0$ — es decir, la eigensolución de $J_\infty u = \gamma_n u$ con condición inicial $u_0 = 1$ NO está en $\ell^2(\mathbb{N})$ (no es un eigenvalor real de $J_\infty$) O tiene condición inicial $u_0 = 0$.

Para $b_n^\infty = 0$: la ecuación de recurrencia $a_{n-1}^\infty u_{n-1} + a_n^\infty u_{n+1} = \gamma_n u_n$ con $u_0 = 1$, $u_{-1} = 0$ tiene solución única $u_n = p_n(\gamma_n)$ (el polinomio ortogonal). Y $\langle e_0, \psi_n^\infty\rangle \neq 0$ iff el eigenvalor está en el soporte de $\mu_{WT}^\infty$.

**La conexión con $C_\infty$.** Por la $\text{EF2}_{WT}$: $\gamma_n \in \text{supp}(\mu_{WT}^\infty)$ iff $\gamma_n$ es cero de $C_\infty$. Luego: $\gamma_n$ es "invisible desde $e_0$" iff $\gamma_n$ NO es cero de $C_\infty$.

---

## 11. El principio de densidad: atacando la invisibilidad

**Pregunta central.** ¿Puede un operador de Jacobi $J_\infty$ con $a_n^\infty = \pi/\log\gamma_n$ y $b_n^\infty = 0$ tener eigenvalores "invisibles desde $e_0$"?

**Proposición 16** (densidad del subespacio cíclico). Para un operador de Jacobi $J$ en $\ell^2(\mathbb{N}_0)$:

- El subespacio cíclico $\mathcal{H}_{e_0}(J) := \overline{\text{span}\{J^n e_0: n \geq 0\}}$ es, por definición, $\ell^2(\mathbb{N}_0)$ completo pues $e_0, J e_0, J^2 e_0, \ldots$ genera toda la base canónica (por la estructura tridiagonal).

*Prueba.* De la estructura de Jacobi: $J e_0 = a_0 e_1$, $J^2 e_0 = a_0 a_1 e_2 + a_0^2 e_0 + \ldots$ — iterando se generan todos los $e_n$. Luego el subespacio cíclico es todo $\ell^2$. $\square$

**Teorema 2** (NO hay eigenvalores invisibles para operadores de Jacobi). Para cualquier operador de Jacobi $J$ en $\ell^2(\mathbb{N}_0)$ con $a_n \neq 0$ para todo $n$: TODOS los eigenvalores de $J$ están en el soporte de $\mu_{WT}$. En particular: NO hay eigenvalores "invisibles desde $e_0$".

*Prueba.* El subespacio cíclico de $e_0$ es todo $\ell^2$ (Proposición 16). Luego la descomposición espectral de $e_0$ "ve" todo el espectro: $J$ es unitariamente equivalente a la multiplicación por $t$ en $L^2(\mathbb{R}, d\mu_{WT})$, y el soporte de $\mu_{WT}$ = espectro de $J$. Por tanto, todo eigenvalor $\lambda$ con eigenvector $\psi$ satisface: $\psi = c\cdot K_\lambda$ donde $K_\lambda$ es el kernel de evaluación en $\lambda$ (en el modelo de reproducción de núcleo). Y $\langle e_0, K_\lambda\rangle = K_\lambda(0) \neq 0$ (el kernel no se anula en el punto de reproducción). $\square$

---

## 12. El corolario fundamental

**Corolario 1** (todos los eigenvalores de $J_\infty$ están en el soporte de $\mu_{WT}^\infty$). Para el operador de Jacobi $J_\infty$ con $a_n^\infty = \pi/\log\gamma_n > 0$ para todo $n$ y $b_n^\infty = 0$:

$$\text{spec}(J_\infty) = \text{supp}(\mu_{WT}^\infty).$$

*Prueba.* Aplicación directa del Teorema 2 (todos $a_n^\infty = \pi/\log\gamma_n \neq 0$). $\square$

**Corolario 2** (los $\gamma_n$ están en el soporte de $\mu_{WT}^\infty$). Si $\gamma_n \in \text{spec}(J_\infty)$ para todo $n$ (es decir, cada $\gamma_n$ es eigenvalor de $J_\infty$): entonces $\gamma_n \in \text{supp}(\mu_{WT}^\infty)$ para todo $n$.

Por $\text{EF2}_{WT}$: $\text{supp}(\mu_{WT}^\infty) \subseteq \{$ceros de $C_\infty\}$. Luego: $\gamma_n \in \{$ceros de $C_\infty\}$ — que es Inc. Inv.

*Prueba.* $\gamma_n \in \text{spec}(J_\infty) \Rightarrow \gamma_n \in \text{supp}(\mu_{WT}^\infty)$ (por Corolario 1) $\Rightarrow C_\infty(\gamma_n) = 0$. $\square$

**LA REDUCCIÓN.** Inc. Inv. se sigue si y solo si: los $\gamma_n$ son eigenvalores de $J_\infty$.

---

## 13. ¿Son los $\gamma_n$ eigenvalores de $J_\infty$?

**La pregunta reducida (Inc. Inv. reducida a eigenvalores).** Por el Corolario 2, el programa entero se reduce a:

$$\boxed{\gamma_n \in \text{spec}(J_\infty) \text{ para todo } n?}$$

Esto es: ¿es $\gamma_n$ un eigenvalor del operador $J_\infty$ con $a_n^\infty = \pi/\log\gamma_n$, $b_n^\infty = 0$?

**La condición de eigenvalor.** $\gamma_n$ es eigenvalor de $J_\infty$ iff existe $u = (u_0, u_1, u_2, \ldots) \in \ell^2(\mathbb{N}_0)$ con:

$$a_{k-1}^\infty u_{k-1} + a_k^\infty u_{k+1} = \gamma_n u_k, \quad k \geq 0,$$

con condición de frontera $u_{-1} = 0$ (o equivalentemente: $a_0^\infty u_1 = \gamma_n u_0$).

La solución única con $u_0 = 1$: $u_k = p_k(\gamma_n)$ (los polinomios ortogonales de Jacobi evaluados en $\gamma_n$).

**Condición de $\ell^2$.** $\gamma_n \in \text{spec}(J_\infty)$ iff $\sum_{k=0}^\infty |p_k(\gamma_n)|^2 < \infty$.

**Proposición 17** (condición de $\ell^2$ para $p_k(\gamma_n)$). Para los polinomios ortogonales de Jacobi con $a_k^\infty = \pi/\log\gamma_k$ y $b_k^\infty = 0$:

$$p_k(t) \sim C_k \prod_{j=1}^k \frac{t}{\pi/\log\gamma_j} = C_k \cdot \frac{t^k \prod_{j=1}^k \log\gamma_j}{\pi^k}.$$

Para $t = \gamma_n$ y $k$ grande: $|p_k(\gamma_n)| \sim c_k \cdot \gamma_n^k \cdot (\log\gamma_n)^k / \pi^k$. Si $\gamma_n\log\gamma_n > \pi$: los términos crecen super-exponencialmente y $p_k(\gamma_n) \notin \ell^2$.

Esto significaría que $\gamma_n \notin \text{spec}(J_\infty)$ para los $\gamma_n$ grandes (tales que $\gamma_n\log\gamma_n > \pi$) — ¡lo contrario de lo que necesitamos!

**El aparente contradicción.** Si los $\gamma_n$ NO están en spec$(J_\infty)$, entonces — por el Corolario 2 — no podemos concluir Inc. Inv. ¿Pero entonces qué son los eigenvalores de $J_\infty$?

---

## 14. Resolución de la contradicción: el espectro de $J_\infty$ no contiene los $\gamma_n$ directamente

**Proposición 18** (el espectro de $J_\infty$ como ceros de $C_\infty$, no como los $\gamma_n$). Por la $\text{EF2}_{WT}$:

$$\text{supp}(\mu_{WT}^\infty) = \{t \in \mathbb{R}: C_\infty(t) = 0\} = \{t_n^C\}.$$

Los puntos $\{t_n^C\}$ son los ceros de $C_\infty(t) = w(t) - \Psi(t)$ — que por el Teorema B son un subconjunto de $\{\gamma_n\}$.

**La pregunta correcta.** Los eigenvalores de $J_\infty$ son los $\{t_n^C\}$ (ceros de $C_\infty$), NO los $\gamma_n$ directamente. Inc. Inv. afirma que $\{t_n^C\} = \{\gamma_n\}$, es decir, CADA $\gamma_n$ es también un cero de $C_\infty$.

La condición de $\ell^2$ del Teorema 2 (visibilidad de eigenvalores desde $e_0$) aplica a los $t_n^C$ (que SÍ son eigenvalores), no a los $\gamma_n$ directamente. Luego NO hay contradicción.

**El teorema 2 es correcto pero no da Inc. Inv. directamente.** Lo que el Teorema 2 garantiza es: si $t \in \text{spec}(J_\infty)$ entonces $t \in \text{supp}(\mu_{WT}^\infty)$ — pero esto ya lo sabíamos (es la definición del soporte de la medida espectral). El teorema no nos dice qué puntos están en spec$(J_\infty)$; eso viene de la $\text{EF2}_{WT}$ (= ceros de $C_\infty$).

---

## 15. Diagnóstico final del Frente C

**Síntesis.** El Frente C (geometría espectral del cociente $Q = C_\infty/\Xi$) ha producido:

1. **Resultado nuevo**: Inc. Inv. es equivalente a que $Q$ se extienda holomorfamente a un entorno de $\mathbb{R}$ (Proposición 3).

2. **Resultado nuevo**: La invisibilidad de eigenvalores desde $e_0$ es IMPOSIBLE para operadores de Jacobi con $a_n \neq 0$ (Teorema 2). Esto deja intacto el argumento.

3. **El verdadero muro**: Los eigenvalores de $J_\infty$ son los ceros de $C_\infty$ (por $\text{EF2}_{WT}$), no los $\gamma_n$ directamente. La pregunta de si cada $\gamma_n$ es cero de $C_\infty$ requiere:

$$\gamma_n \text{ es eigenvalor de }J_\infty \iff p_k(\gamma_n) \in \ell^2 \iff C_\infty(\gamma_n) = 0. \quad (\star)$$

La equivalencia $(\star)$ entre la condición de $\ell^2$ de los polinomios ortogonales y los ceros de $C_\infty$ es el contenido profundo de la $\text{EF2}_{WT}$.

4. **La pregunta abierta genuinamente nueva**: ¿Es posible probar directamente que $\sum_k |p_k(\gamma_n)|^2 < \infty$ para cada $n$ USANDO la fórmula explícita de $p_k$ en términos de $a_j^\infty = \pi/\log\gamma_j$? Esta suma involucra propiedades aritméticas de los $\gamma_j$ — en particular, la distribución de los ceros de $\zeta$ en la recta crítica. Es un problema de ANÁLISIS NUMÉRICO DE OPERADORES con inputs aritméticos.
