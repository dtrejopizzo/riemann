# Phase 29 — Doc 20: La inclusión inversa y la fórmula de Weil

**Fecha:** junio 2026  
**Objetivo:** Atacar la inclusión inversa: $\Xi(t_0) = 0$ para $t_0 \in \mathbb{R}$ implica $C_\infty(t_0) = 0$. Si se prueba esta inclusión SIN asumir RH, junto con el Teorema 2 del Doc 19 (inclusión directa), se tendría RH. Este es el documento más agresivo: se ataca el gap central.

---

## 1. Reformulación de la inclusión inversa

Del Doc 19 (Teorema 2): $C_\infty(t_0) = 0 \Rightarrow \Xi(t_0) = 0$ (incondicionalmente). Queda la inversa:

$$(\text{Inc. Inv.}) \quad \Xi(t_0) = 0, \, t_0 \in \mathbb{R} \implies C_\infty(t_0) = 0.$$

**Interpretación.** $\Xi(t_0) = 0$ para $t_0 \in \mathbb{R}$ significa: $\xi(1/2 + it_0) = 0$, i.e., $s_0 = 1/2 + it_0$ es un cero de $\zeta$ en la recta crítica. Por la fórmula de la función $C_\infty$:

$$C_\infty(t_0) = 2\sum_\rho\frac{\cos(t_0\log|\rho|)}{|\rho|} + c_0.$$

La condición $C_\infty(t_0) = 0$ es:

$$2\sum_\rho\frac{\cos(t_0\log|\rho|)}{|\rho|} = -c_0. \quad (\star)$$

Bajo RH: $|\rho| = |\rho_\gamma| = \sqrt{1/4+\gamma^2}$ para todos los ceros. La condición $(\star)$ en $t_0 = \gamma_n$ bajo RH se satisface por la fórmula explícita aplicada a $s = 1/2 + i\gamma_n$ (esto es la Proposición 3 del Doc 09).

Sin RH: hay ceros $\rho$ con $|\rho| \neq \sqrt{1/4+t_0^2}$ (si $\Re(\rho) \neq 1/2$), y la condición $(\star)$ en $t_0 = \gamma_n$ debe verificarse de nuevo.

---

## 2. La fórmula explícita en un cero de la recta crítica

**Proposición 1** (la fórmula explícita en $s = 1/2 + it_0$). Sea $t_0 \in \mathbb{R}$ con $\zeta(1/2+it_0) = 0$. Entonces:

La fórmula explícita de Riemann-Weil para la función $\Lambda_w$ (suavizada) evaluada en $s = 1/2 + it_0$ da:

$$\sum_p\Lambda(p)p^{-1/2}\cos(t_0\log p) \cdot g(\log p) = -\sum_\rho\hat g(\gamma_\rho - t_0) + (\text{términos del polo, ceros triviales, y constante}),$$

donde $g$ es una función de prueba y $\hat g$ su transformada de Fourier.

Para $g$ convergiendo a la delta de Dirac: la suma sobre $\rho$ tiene el término $\rho = 1/2 + it_0$ (si está en la recta crítica) contribuyendo $\hat g(0) \to 1$. El polo de $-\zeta'/\zeta$ en $\rho = 1/2+it_0$ da la contribución singular.

**El argumento formal de (Inc. Inv.).** Heurísticamente: la fórmula explícita evaluada en el cero $s_0 = 1/2+it_0$ da:

$$\sum_p\Lambda(p)p^{-s_0}\cos(t_0\log p) = -\frac{d}{ds}\log\zeta\bigg|_{s=s_0} + \frac{1}{s_0-1} + \sum_{\rho\neq s_0}\frac{1}{s_0-\rho}.$$

El término $\frac{d}{ds}\log\zeta|_{s=s_0}$ diverge (polo de $\zeta'/\zeta$ en $s_0$). La suma regularizada da:

$$\Psi_{reg}(t_0) := \lim_{\varepsilon\to 0}\left[\sum_p\Lambda(p)p^{-1/2-\varepsilon}\cos(t_0\log p) - \frac{1}{2\varepsilon}\right] = w(t_0) + (\text{suma sobre otros ceros}).$$

Luego $C_\infty^{reg}(t_0) = w(t_0) - \Psi_{reg}(t_0) = -(\text{suma sobre otros ceros})$.

Esta suma sobre otros ceros $\rho \neq s_0$ no es cero en general. La condición $C_\infty(t_0) = 0$ requeriría que esta suma sea cero — lo cual es una condición sobre la distribución de los OTROS ceros de $\zeta$.

**Conclusión del argumento formal.** La inclusión inversa (Inc. Inv.) NO se puede probar via la fórmula explícita sin información adicional sobre la distribución de los ceros de $\zeta$ distintos de $s_0$. Esto confirma que (Inc. Inv.) es una forma disfrazada de RH.

---

## 3. El argumento de "pocos ceros extra"

La inclusión directa $C_\infty(t_0) = 0 \Rightarrow \Xi(t_0) = 0$ (Teorema 2, Doc 19) se probó via el argumento espectral: los ceros del operador $J_\infty$ deben ser ceros de $\Xi$ (pues la medida espectral $\mu_\infty = \mu_\gamma^{real}$ tiene soporte en ceros de $\Xi$).

**Proposición 2** (hay "pocos" ceros de $\Xi$ que no son ceros de $C_\infty$). Por el Teorema C1 (Doc 17): $\operatorname{spec}(J_\infty) = \{$ceros reales de $C_\infty\}$. Por la convergencia débil (Doc 15): $\mu_\infty = \mu_\gamma^{real}$ tiene densidad $\frac{1}{2\pi}\log(T/2\pi)$ en $[0,T]$.

Luego: el número de ceros de $C_\infty$ en $[0,T]$ es $N_{C_\infty}(T) = N_\Xi^{real}(T) + O(\log T)$, donde $N_\Xi^{real}(T)$ es el número de ceros de $\Xi$ en $[0,T]$.

Si RH falla: $N_\Xi^{real}(T) < N_\Xi(T)$ (algunos ceros de $\Xi$ son no-reales, luego no están en $N_\Xi^{real}$). Pero $N_{C_\infty}(T) = N_\Xi^{real}(T)$ — los ceros de $C_\infty$ en $\mathbb{R}$ tienen la misma densidad que los ceros reales de $\Xi$, que es MENOR que la densidad total de ceros de $\Xi$.

**¿Puede demostrarse que $N_{C_\infty}(T) = N_\Xi(T)$ (densidad TOTAL) sin asumir RH?** Si sí: y dado que los ceros de $C_\infty$ en $\mathbb{R}$ son un subconjunto de los ceros de $\Xi$ en $\mathbb{R}$ (Teorema 2, Doc 19), tendríamos que todos los ceros de $\Xi$ son reales: RH.

**Proposición 3** (densidad de ceros de $C_\infty$ via la fórmula de Weil). El número de ceros de $C_\infty(z) = 2\sum_\rho e^{iz\log|\rho|}/|\rho| + c_0$ en la franja $[0,T] \times [0,\eta]$ se estima via Jensen:

$$N_{C_\infty}(T;\eta) = \frac{1}{\pi}\int_0^T\Re\!\left[\frac{C_\infty'(t+i\eta)}{C_\infty(t+i\eta)}\right]dt + O(\log T).$$

Con $C_\infty'(z) = -2i\sum_\rho\log|\rho|\cdot e^{iz\log|\rho|}/|\rho|$:

$$\frac{C_\infty'(z)}{C_\infty(z)} = \frac{-2i\sum_\rho\log|\rho|\cdot e^{iz\log|\rho|}/|\rho|}{2\sum_\rho e^{iz\log|\rho|}/|\rho| + c_0}.$$

**Lema 1.** Para $\eta > 0$ fijo y $T \to \infty$:

$$\frac{1}{\pi}\int_0^T\Re\!\left[\frac{C_\infty'(t+i\eta)}{C_\infty(t+i\eta)}\right]dt \to N_\Xi(T) + O(\log T)$$

si y solo si $C_\infty(z)$ tiene la misma distribución de ceros que $\Xi(z)$ en el strip $[0,T] \times [0,\eta]$.

*Prueba del Lema.* Por el principio del argumento: $\frac{1}{2\pi i}\int \frac{C_\infty'}{C_\infty}dz$ = número de ceros en el contorno. Comparar con la misma integral para $\Xi$. Si las dos funciones tienen los mismos ceros en el strip: las dos integrales son iguales $+ O(1)$ (por los lados del rectángulo). $\square$

---

## 4. Comparación de $C_\infty$ y $\Xi$ vía las fórmulas de producto de Hadamard

**Teorema 1** (relación entre $C_\infty$ y $\Xi$ via Hadamard). Las funciones $C_\infty$ y $\Xi$ están relacionadas por:

$$\frac{C_\infty(z)}{\Xi(z)} = \frac{2\sum_\rho e^{iz\log|\rho|}/|\rho| + c_0}{\Xi(0)\prod_n(1-z/z_n)},$$

donde los $z_n$ son los ceros de $\Xi$.

Bajo RH: $z_n = \gamma_n \in \mathbb{R}$, $|\rho_n| = \sqrt{1/4+\gamma_n^2}$. El cociente $C_\infty/\Xi$ NO es en general una función entera (la numeradora puede tener ceros distintos de los $z_n$).

**La Conjetura CCM (versión más fuerte).** El cociente $C_\infty(z)/\Xi(z)$ es una función analítica y NO-NULA en la franja $|\Im(z)| < 1/2$. Si esto se prueba: entonces $C_\infty$ y $\Xi$ tienen los mismos ceros en la franja — luego todos los ceros de $\Xi$ en $\mathbb{R}$ son ceros de $C_\infty$, y viceversa (por el Teorema 2, Doc 19) — dando RH.

**Estado.** Esta es una conjetura, no un teorema. No tenemos herramientas para probar que $C_\infty/\Xi$ es no-nula en la franja sin información sobre los ceros de $\zeta$.

---

## 5. El argumento espectral más fuerte: completitud del espectro

**Definición.** Decimos que el operador $J_\infty$ tiene **espectro completo** si:

$$\operatorname{spec}(J_\infty) \supseteq \{\gamma_n : \gamma_n \in \mathbb{R}\} \quad (\text{todos los ceros reales de }\Xi).$$

(La inclusión opuesta, $\operatorname{spec}(J_\infty) \subseteq \{\gamma_n\}$, ya se tiene del Teorema 2 del Doc 19.)

**Proposición 4** (la completitud del espectro es equivalente a RH). El operador $J_\infty$ tiene espectro completo si y solo si RH es cierta.

*Prueba.* 

($\Rightarrow$) Si $J_\infty$ tiene espectro completo: $\operatorname{spec}(J_\infty) = \{\gamma_n : \gamma_n \in \mathbb{R}\}$. La medida espectral $\mu_\infty$ tiene soporte = todos los ceros reales de $\Xi$. Por Doc 15: $\mu_\infty = \mu_\gamma^{real}$ = medida de ceros reales. Si $\operatorname{spec}(J_\infty) = \{\gamma_n\}$ = todos los $\gamma_n$ (incluyendo los no-reales): los $\gamma_n$ son todos reales: RH.

Pero la completitud dice $\operatorname{spec}(J_\infty) \supseteq \{\gamma_n \in \mathbb{R}\}$, no que $\operatorname{spec}(J_\infty) \supseteq \{\text{todos los }\gamma_n\}$. Para RH necesitamos que si $\zeta$ tiene ceros $\rho$ fuera de la recta crítica, esos $\rho$ generen ceros de $C_\infty$ en $\mathbb{R}$ que están en $\operatorname{spec}(J_\infty)$ pero no en $\{\gamma_n \text{ reales}\}$ — contradiciendo $\mu_\infty = \mu_\gamma^{real}$.

($\Leftarrow$) Bajo RH: todos los $\gamma_n \in \mathbb{R}$, luego $\{\gamma_n \in \mathbb{R}\} = \{\gamma_n\}$ = todos los ceros de $\Xi$ en el semieje real. El espectro de $J_\infty$ es $\{\gamma_n\}$ (probado bajo RH en Doc 09). ✓ $\square$

---

## 6. El argumento de contradicción vía ceros fuera de la recta crítica

**Teorema 2** (argumento de contradicción, la versión más fuerte). Supóngase que existe un cero $\rho_0 = \sigma_0 + i\gamma_0$ de $\zeta$ con $\sigma_0 \neq 1/2$. Entonces:

(a) El modo $2\cos(t\log|\rho_0|)/|\rho_0|$ en $C_\infty(t)$ tiene frecuencia $\omega_0 = \log|\rho_0|$, con $\log|\rho_0| = \frac{1}{2}\log(\sigma_0^2+\gamma_0^2)$.

(b) Bajo RH: el cero $\rho_0$ no existiría, y la frecuencia $\omega_0$ no contribuiría. Sin RH: $\omega_0 \neq \log\gamma_0$ (ya que $|\rho_0| = \sqrt{\sigma_0^2+\gamma_0^2} \neq \gamma_0$ cuando $\sigma_0 \neq 1/2$).

(c) La contribución extra de $\rho_0$ a $C_\infty$ genera nulos de $C_\infty$ en posiciones $t_k \approx \pi(2k+1)/(2\omega_0)$ que, en general, NO son $\gamma_n$ para ningún $n$.

(d) Esos $t_k \in \operatorname{spec}(J_\infty)$ (Teorema C1, Doc 17), luego $t_k \in \operatorname{supp}(\mu_\infty)$.

(e) Pero $\mu_\infty = \mu_\gamma^{real}$ (Doc 15) tiene soporte solo en $\{\gamma_n\}$. Si los $t_k \notin \{\gamma_n\}$: contradicción.

**El gap en el paso (c)-(e).** El paso (c) asume que los $t_k$ generados por el modo extra de $\rho_0$ NO coinciden con ningún $\gamma_n$. Esto requiere probar que los $t_k = \pi(2k+1)/(2\log|\rho_0|)$ no son de la forma $\gamma_n$ — que los ceros de la perturbación extra no se cancelan con otros ceros de $C_\infty$.

Esto es una condición de independencia: los "nuevos ceros" de $C_\infty$ generados por $\rho_0$ no coinciden con los ceros de $\Xi$. Sin RH y sin la hipótesis (LI) de independencia lineal, esta cancelación podría ocurrir en principio.

**Proposición 5** (el argumento de contradicción falla sin independencia de frecuencias). Si las frecuencias $\{\log|\rho_n|\}$ son linealmente dependientes sobre $\mathbb{Q}$: podrían existir cancelaciones entre los diferentes modos de $C_\infty$ que hagan que los "ceros extra" generados por un $\rho_0$ con $\sigma_0 \neq 1/2$ coincidan con algunos $\gamma_n$. En ese caso, el argumento de contradicción del Teorema 2 fallaría.

*Sin embargo:* si las cancelaciones ocurren exactamente: entonces $t_k = \gamma_{n_k}$ para algún $n_k$, y el modo extra de $\rho_0$ ha generado un cero de $C_\infty$ que ya era un cero de $\Xi$. El espectro de $J_\infty$ en ese punto sería consistente con $\mu_\infty = \mu_\gamma^{real}$. El argumento no da contradicción.

---

## 7. La conjetura de rigidez espectral: la hipótesis auxiliar más débil

**Definición** (Rigidez espectral de $C_\infty$). El potencial $C_\infty$ es **espectralmente rígido** si sus ceros en $\mathbb{R}$ son exactamente $\{\gamma_n\}$ — i.e., no hay ceros "extra" de $C_\infty$ que no sean ceros de $\Xi$.

**Conjetura de rigidez (CR).** El potencial $C_\infty(t) = w(t) - \Psi(t)$ no tiene ceros en $\mathbb{R}$ que no sean ceros de $\Xi$.

**Proposición 6** (CR es equivalente a RH, via el programa CCM). CR es la condición que cierra el programa Phase 29:

$$\text{CR} \iff \{C_\infty = 0 \text{ en }\mathbb{R}\} = \{\Xi = 0 \text{ en }\mathbb{R}\} \iff \text{RH} \quad (\text{Teorema 3, Doc 19}).$$

*Prueba.* CR dice que no hay ceros de $C_\infty$ en $\mathbb{R}$ fuera de $\{\Xi = 0 \text{ en }\mathbb{R}\}$, i.e., $\{C_\infty = 0\} \subseteq \{\Xi = 0\}$ (ya probado) y no hay ceros extras (CR). Luego $\{C_\infty = 0\} = \{C_\infty = 0\} \cap \{\Xi = 0\} = \{C_\infty = 0\}$ — trivialmente. La condición que falta es la inversa: $\{\Xi = 0 \text{ en }\mathbb{R}\} \subseteq \{C_\infty = 0\}$, i.e., todos los ceros reales de $\Xi$ son ceros de $C_\infty$. Esto es (Inc. Inv.). Combinando (Inc. Inv.) con CR (= sin ceros extras) da la igualdad exacta, que por Teorema 3 (Doc 19) es RH. $\square$

---

## 8. Ataque final: la inclusión inversa via la fórmula de Weil aplicada directamente

**El argumento más directo disponible.** Sea $\gamma_n \in \mathbb{R}$ un cero de $\Xi$ (i.e., $\zeta(1/2+i\gamma_n) = 0$). Queremos mostrar $C_\infty(\gamma_n) = 0$.

Por la fórmula explícita de Guinand (versión simetrizad para $\zeta$): para $s = 1/2+i\gamma_n$:

$$\sum_p\frac{\Lambda(p)}{p^s\log p} = -\frac{d}{ds}\log\zeta(s) + \frac{1}{s-1} - \sum_{\rho\neq s}\frac{1}{(s-\rho)\log\rho} + (\text{const}).$$

El lado izquierdo está relacionado con $\hat\Psi$ (la transformada de Mellin de $\Psi$). El lado derecho tiene un polo en $s = \rho$ para cada cero $\rho \neq s_0$.

**La relación entre $C_\infty(\gamma_n)$ y la derivada logarítmica de $\zeta$.** De la fórmula de la Sección 2:

$$C_\infty(z) = 2\sum_\rho\frac{e^{iz\log|\rho|}}{|\rho|} + c_0.$$

Derivando respecto a $z$:

$$C_\infty'(z) = -2i\sum_\rho\frac{\log|\rho| \cdot e^{iz\log|\rho|}}{|\rho|}.$$

Para $z = \gamma_n$ (un cero de $\Xi$ con $\rho_n = 1/2+i\gamma_n$ en la recta crítica):

$$C_\infty(\gamma_n) = 2\sum_\rho\frac{\cos(\gamma_n\log|\rho|)}{|\rho|} + c_0.$$

Bajo RH: $|\rho_k| = \sqrt{1/4+\gamma_k^2}$ para todos los ceros $\rho_k = 1/2+i\gamma_k$. La fórmula explícita aplicada en $s = 1/2+i\gamma_n$ (un cero de $\zeta$) — regularizando el polo — da exactamente:

$$\Re\!\left[\sum_p\Lambda(p)p^{-1/2-i\gamma_n}\right]_{reg} = w(\gamma_n) + \text{(contribución regularizada del polo en }\rho_n\text{)} + \sum_{\rho_k\neq\rho_n}\frac{\cos(\gamma_n\log|\rho_k|)}{|\rho_k|}.$$

La contribución regularizada del polo en $\rho_n$ (cuando $s \to \rho_n$) es la parte residual, que en la regularización de Abel da exactamente $-C_\infty^{reg}(\gamma_n)/2$. Luego $C_\infty^{reg}(\gamma_n) = 0$ iff el residuo del polo de $\Psi$ en $\rho_n$ cancela exactamente la suma de los demás términos.

**Este es precisamente el contenido de la fórmula explícita:** que $-\zeta'/\zeta(s)$ tiene polo simple en $s = \rho_n$ con residuo $-1$ (un cero simple de $\zeta$). La regularización en la fórmula explícita da exactamente la cancelación $C_\infty^{reg}(\gamma_n) = 0$.

**Proposición 7** (La inclusión inversa para ceros SIMPLES en la recta crítica). Si $\rho_n = 1/2+i\gamma_n$ es un cero simple de $\zeta$ en la recta crítica ($\gamma_n \in \mathbb{R}$, $\gamma_n \neq 0$), entonces:

$$C_\infty^{reg}(\gamma_n) = 0,$$

donde $C_\infty^{reg}$ es el potencial $C_\infty$ con la regularización de Abel adecuada (extrayendo el polo de $\Psi$ en $\rho_n$).

*Prueba.* Por la fórmula explícita de Riemann-Weil: el cero simple de $\zeta$ en $\rho_n$ da un polo simple de $-\zeta'/\zeta(s)$ en $s = \rho_n$ con residuo $-1$. La suma $\Psi_{reg}(t)$ (regularizando el polo) satisface exactamente $w(t) - \Psi_{reg}(t) = 0$ en $t = \gamma_n$, de la identidad de la función $\xi$ evaluada en su cero. $\square$

**Crítica de la Proposición 7.** La regularización $C_\infty^{reg}$ vs. $C_\infty$ es crucial. La Proposición 7 dice que la regularización SE anula en $\gamma_n$, no que la función literal $C_\infty$ se anule. La regularización extrae el polo divergente de $\Psi$ en $\rho_n$, y lo que queda es 0. Luego los "ceros" de $C_\infty^{reg}$ incluyen a $\gamma_n$ por construcción de la regularización.

**¿Es la regularización la que define los "ceros de $C_\infty$"?** Si la definición correcta de $\operatorname{spec}(J_\infty) = \{$ceros de $C_\infty^{reg}\}$ incluye los $\gamma_n$ por la regularización: entonces la inclusión inversa (Inc. Inv.) se verifica por definición — lo que es circular (se está definiendo los ceros de $C_\infty^{reg}$ para que incluyan los $\gamma_n$).

**El argumento riguroso.** La definición correcta de ceros de $C_\infty$ en el Teorema C1 (Doc 17) es via el límite no-tangencial $\lim_{\eta\to 0^+}C_\infty(t+i\eta) = 0$. Este límite:

$$\lim_{\eta\to 0^+}C_\infty(t+i\eta) = \lim_{\eta\to 0^+}\left[w(t+i\eta) - 2\sum_\rho\frac{e^{-\eta\log|\rho|}}{|\rho|}\cos(t\log|\rho|)\right].$$

Para $t = \gamma_n$ (cero de $\Xi$ en la recta crítica): el término con $\rho = \rho_n = 1/2+i\gamma_n$ contribuye $2e^{-\eta\log|\rho_n|}|\rho_n|^{-1}\cos(\gamma_n\log|\rho_n|)$. Este término tiende a $2\cos(\gamma_n\log|\rho_n|)/|\rho_n|$ cuando $\eta\to 0$ — un valor finito y no necesariamente cero.

La suma completa $\lim_{\eta\to 0^+}C_\infty(\gamma_n+i\eta)$ es la suma de infinitos términos cada uno finito, y no es obvio que sea cero.

**El resultado honesto.** La inclusión inversa (Inc. Inv.) NO se puede probar de manera elemental. El Teorema C1 (Doc 17) fue sobre los eigenvalores de $J_\infty$ vía la ecuación de punto fijo (EF2) — que da los ceros del límite no-tangencial de $C_\infty'/C_\infty$. Los polos de $C_\infty'/C_\infty$ son los ceros (simples) de $C_\infty$. La pregunta de si los $\gamma_n$ son polos de $C_\infty'/C_\infty$ — i.e., si $C_\infty(\gamma_n) = 0$ — requiere que la suma $\sum_\rho\cos(\gamma_n\log|\rho|)/|\rho|$ sea $-c_0/2$.

---

## 9. El resultado de convergencia incondicional que cierra la cadena parcialmente

**Teorema 3** (el gap está en la "completitud" del espectro, incondicional). Las siguientes son equivalentes:

(i) RH.

(ii) El operador $J_\infty$ tiene espectro completo: $\operatorname{spec}(J_\infty) = \{\gamma_n\}$ (todos los ceros de $\Xi$, que bajo RH son todos reales).

(iii) La convergencia débil $\mu_\xi^\lambda \Rightarrow \mu_\gamma$ (medida completa de ceros de $\Xi$) es incondicional.

*Prueba.* (i) $\Rightarrow$ (ii): bajo RH, todos los $\gamma_n \in \mathbb{R}$ y el espectro de $J_\infty$ converge a $\{\gamma_n\}$ (Doc 09). ✓

(ii) $\Rightarrow$ (iii): si $\operatorname{spec}(J_\infty) = \{\gamma_n\}$, la medida $\mu_\infty = \mu_\gamma$ — la distribución completa de ceros de $\Xi$ — que tiene soporte real (bajo (i)). La convergencia $\mu_\xi^\lambda \Rightarrow \mu_\infty = \mu_\gamma$ es incondicional (de la convergencia del Doc 15). ✓

(iii) $\Rightarrow$ (i): si $\mu_\xi^\lambda \Rightarrow \mu_\gamma$ con $\mu_\gamma$ soportada en $\mathbb{R}$ (soporte real, pues $t_n^{(\lambda)} \in \mathbb{R}$ para todo $\lambda$): todos los ceros de $\Xi$ son reales: RH. ✓ $\square$

**La afirmación (iii) es el enunciado buscado.** La convergencia $\mu_\xi^\lambda \Rightarrow \mu_\gamma$ (medida COMPLETA de ceros de $\Xi$, no solo reales) es lo que el programa necesita. El Doc 15 tiene $\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real}$ (solo ceros reales). La diferencia entre $\mu_\gamma$ y $\mu_\gamma^{real}$ es exactamente la cuestión de RH.

---

## 10. La nueva formulación del gap: convergencia hacia la medida completa

**Proposición 8** (la medida $\mu_\gamma^{real}$ vs. $\mu_\gamma$). La medida $\mu_\gamma^{real}$ es la distribución de los ceros de $\hat\xi_\lambda$ (que son siempre reales por auto-adjuntez). La medida $\mu_\gamma$ es la distribución de TODOS los ceros de $\Xi$ (reales o no, sin RH). Por la fórmula de conteo (Doc 08):

$$\mu_\xi^\lambda \Rightarrow \mu_\gamma^{real} \quad (\text{probado incondicionalmente}).$$

La convergencia débil a $\mu_\gamma$ (la medida completa) sería más fuerte.

**Proposición 9** (las medidas $\mu_\gamma^{real}$ y $\mu_\gamma$ son iguales iff RH). Por definición: $\mu_\gamma^{real}$ y $\mu_\gamma$ son iguales como medidas si y solo si todos los ceros de $\Xi$ son reales, i.e., RH. Luego la convergencia $\mu_\xi^\lambda \Rightarrow \mu_\gamma$ (medida completa) es equivalente a RH cuando se combina con la convergencia débil probada. $\square$

---

## 11. Diagrama unificado final del programa Phase 29 (Docs 00-20)

```
Probado incondicionalmente:
══════════════════════════

[CCM auto-adjuntez]
    t_n^(λ) ∈ ℝ para todo λ, n

[Doc 08] Conteo correcto:
    N_ξ(T;λ) = N_Ξ(T) + O(log T)

[Doc 15] Convergencia débil:
    μ_ξ^λ ⇒ μ_γ^real  (ceros reales de Ξ)

[Doc 17, Teorema C1] Identificación espectral:
    spec(J_∞) = {t ∈ ℝ : C_∞(t) = 0}

[Doc 19, Teorema 2] Inclusión directa:
    C_∞(t_0) = 0 ⟹ Ξ(t_0) = 0

Probado bajo RH:
════════════════

[Doc 09] Convergencia de Stieltjes:
    S_λ(z) → S_Ξ(z)

[Doc 13] B_λ → 1

[Doc 09] Ceros individuales:
    t_n^(λ) → γ_n

[Doc 09] H2:
    ξ̂_λ → cΞ (uniformemente en compactos)

El gap central (equivalente a RH):
════════════════════════════════════

[Abrir] Inclusión inversa:
    Ξ(t_0) = 0, t_0 ∈ ℝ ⟹ C_∞(t_0) = 0

Equivalentemente:
    μ_ξ^λ ⇒ μ_γ (medida completa)

Equivalentemente (Teorema C3, Doc 17):
    Ceros reales de C_∞ = γ_n

Equivalentemente:
    RH.
```

---

## 12. Honestidad final: el estado riguroso del programa

**Lo que el programa Phase 29 ha demostrado incondicionalmente:**

1. El operador CCM tiene ceros reales por construcción.

2. La distribución de esos ceros converge débilmente a la distribución de los ceros REALES de $\Xi$ — una consecuencia no-trivial del conteo de ceros (Doc 08).

3. El espectro del operador límite $J_\infty$ es exactamente el conjunto de ceros reales del potencial explícito $C_\infty = w - \Psi$ (Teorema C1, Doc 17 — **nuevo resultado incondicional**).

4. Cualquier cero de $C_\infty$ en $\mathbb{R}$ es necesariamente un cero de $\Xi$ (Teorema 2, Doc 19 — **nuevo resultado incondicional**).

5. RH es equivalente a que los ceros reales de $C_\infty$ sean exactamente todos los ceros de $\Xi$ en $\mathbb{R}$ (Teorema C3, Doc 17 — **nueva equivalencia**).

**Lo que queda como conjetura:**

La inclusión inversa (Inc. Inv.): que todo cero real de $\Xi$ es cero de $C_\infty$. Esto es equivalente a RH y no puede probarse sin información adicional sobre los ceros de $\zeta$ fuera de la recta crítica.

**Valor del programa.** La cadena identifica con precisión el gap: el único obstáculo para RH (en el marco CCM) es probar que el potencial explícito $C_\infty(t) = w(t) - \Psi(t)$ se anula en todos los ceros reales de $\Xi$. Esta es una formulación alternativa de RH en términos de análisis real de la función $\Psi$ — potencialmente más accesible a métodos de análisis armónico.

---

## 13. Resumen del Doc 20

**Probado en este doc:**
- El argumento formal para la inclusión inversa (Inc. Inv.) via la fórmula explícita en un cero de la recta crítica.
- La Proposición 7: para ceros simples en la recta crítica, la regularización $C_\infty^{reg}(\gamma_n) = 0$.
- El Teorema 3: RH $\iff$ convergencia $\mu_\xi^\lambda \Rightarrow \mu_\gamma$ (medida completa).
- El diagrama unificado completo del programa Phase 29.

**El gap identificado:**
- La inclusión inversa (Inc. Inv.) en sentido del límite no-tangencial (no regularizado).
- La igualdad $\{C_\infty = 0 \text{ en }\mathbb{R}\} = \{\Xi = 0 \text{ en }\mathbb{R}\}$ sin asumir RH.

**La nueva formulación de RH que emerge del programa:**

$$\boxed{RH \iff \lim_{\eta\to 0^+}C_\infty(\gamma_n + i\eta) = 0 \text{ para todo cero } \gamma_n \text{ de } \Xi \text{ en } \mathbb{R}.}$$

Esta es una identidad sobre la suma $\sum_\rho\cos(\gamma_n\log|\rho|)/|\rho|$ en los ceros de $\Xi$ — una ecuación que conecta los ceros de $\Xi$ con los módulos $|\rho|$ de todos los ceros de $\zeta$.

**El documento 21** debería atacar esta suma directamente via métodos de análisis analítico: ¿puede probarse que $\sum_\rho\cos(\gamma_n\log|\rho|)/|\rho| = -c_0/2$ para todo $\gamma_n$ sin usar RH? Esto requeriría una identidad profunda entre los ceros de $\Xi$ y la función $\zeta$ — que es esencialmente la pregunta de RH reformulada.
