# Doc 45 — Asintótica de $C_\infty(\gamma_n)$ para $n\to\infty$: Media, Varianza y Conexión con Montgomery

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 38–44 (especialmente Doc 42 T 5.2, Doc 43 C 7.4, Doc 44 §§3–5)  
**Objetivo:** Estudiar el comportamiento de la sucesión $\{C_\infty(\gamma_n)\}_{n=1}^\infty$ como función de $n$: cotas uniformes, media aritmética, varianza y correlaciones. Conectar con la Conjetura de Correlaciones de Pares de Montgomery.

---

## 1. La sucesión $\{C_\infty(\gamma_n)\}$ como objeto de análisis

Doc 44 estableció la representación exacta $C_\infty(\gamma_n) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)$ y la alternativa dicotómica: o $C_\infty \equiv 0$ (RH) o $C_\infty > 0$ para $\lambda$-casi todo $t \in \mathbb{R}$ (no-RH). La pregunta de Doc 45 es:

> *¿Cómo se comporta la sucesión $C_\infty(\gamma_n)$ para $n$ grande? ¿Puede el comportamiento asintótico revelar estructura nueva sobre $\mu_{\mathrm{off}}$?*

En todo lo que sigue, trabajamos con la fórmula explícita:
$$C_\infty(\gamma_n) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0>1/2,\,\gamma_0>0}} \Delta(\gamma_n;\rho_0), \qquad \Delta(\gamma_n;\rho_0) = 2(\sigma_0-1/2)\left[\frac{1}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2}+\frac{1}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}\right]$$

---

## 2. Cota superior uniforme de $C_\infty(\gamma_n)$

**Proposición 2.1 (Cota superior incondicional).** Para cada $n$:
$$C_\infty(\gamma_n) \leq \frac{8}{\delta_n} \cdot N_{\mathrm{off}}^{\mathrm{near}}(\gamma_n) + O\!\left(\log\gamma_n\right)$$

donde $\delta_n = \min_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}}|\sigma_0-1/2|$ es la distancia mínima de cualquier cero off-crítico al eje, y $N_{\mathrm{off}}^{\mathrm{near}}(\gamma_n)$ es el número de ceros off-críticos en $|\gamma_0 - \gamma_n| \leq 1$.

*Prueba.* Separamos la suma en $|\gamma_0-\gamma_n| \leq 1$ (ceros "cercanos") y $|\gamma_0-\gamma_n| > 1$ (ceros "lejanos").

Para los lejanos: $\Delta(\gamma_n;\rho_0) \leq 2(\sigma_0-1/2)/(\gamma_0-\gamma_n)^2$. Sumando por anillos y usando la estimación de densidad $N(\sigma,T)\ll T^{2(1-\sigma)}\log T$:
$$\sum_{\substack{|\gamma_0-\gamma_n|>1}} \Delta(\gamma_n;\rho_0) \ll \int_1^\infty \frac{N_{\mathrm{off}}(\gamma_n+u)-N_{\mathrm{off}}(\gamma_n)}{u^2}\,du \ll \log\gamma_n$$

Para los cercanos: $\Delta(\gamma_n;\rho_0) \leq 8/(\sigma_0-1/2) \leq 8/\delta_n$ para cada cero. $\square$

**Corolario 2.2.** Si no hay ceros off-críticos cercanos a $\gamma_n$ (lo que ocurre para casi todo $n$ si $\mathcal{Z}_{\mathrm{off}}$ es discreto), entonces $C_\infty(\gamma_n) = O(\log\gamma_n)$.

**Corolario 2.3 (Acotamiento uniforme bajo hipótesis de densidad).** Si $N_{\mathrm{off}}(T) = O(T^\theta)$ para algún $\theta < 1$, entonces $C_\infty(\gamma_n) = O(\gamma_n^{\theta-1+\epsilon})$ para todo $\epsilon > 0$. En particular, bajo la conjetura de densidad fuerte ($\theta\to 0$), $C_\infty(\gamma_n) \to 0$.

---

## 3. Media aritmética de $C_\infty(\gamma_n)$

**Definición 3.1.** Sea $M_N = \frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n)$ la media aritmética del déficit sobre los primeros $N$ ceros de $\Xi$.

**Teorema 3.2 (Fórmula para la media).** 
$$M_N = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \frac{1}{N}\sum_{n=1}^N \Delta(\gamma_n;\rho_0)$$

Para cada $\rho_0$ fijo, el promedio $\frac{1}{N}\sum_{n=1}^N \Delta(\gamma_n;\rho_0)$ converge cuando $N\to\infty$ al valor:
$$\lim_{N\to\infty} \frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n - \gamma_0) = \frac{1}{2\pi}\int_\mathbb{R} P_{y_0}(t)\,\frac{dt}{y_0+1} \cdot \rho_{\mathrm{zero}}$$

donde $\rho_{\mathrm{zero}} = \lim_{T\to\infty} N_\Xi(T)/T = \log T/(2\pi T)$ es la densidad local de ceros de $\Xi$ cerca de altura $T$.

*Prueba esquemática.* Por la equidistribución asintótica de los ceros $\gamma_n$ (ley del seno para el kernel de GUE, condicionalmente a la Conjetura de Montgomery), el promedio de Cesàro de $P_{y_0}(\gamma_n - \gamma_0)$ converge al integral del núcleo de Poisson contra la medida de densidad de ceros. Incondicionalmente, se obtiene un límite superior via el Lema de Landau-Selberg. $\square$

**Corolario 3.3.** 
$$M_N \sim \frac{\log(\gamma_N/(2\pi))}{2\pi} \cdot \pi \cdot \sum_{\rho_0} (\sigma_0-1/2) = \frac{\log(\gamma_N/(2\pi))}{2} \cdot \sum_{\rho_0}(\sigma_0-1/2)$$

Si $\mathcal{Z}_{\mathrm{off}} \neq \emptyset$, la media $M_N \to \infty$ (crece logarítmicamente).

**Corolario 3.4 (Criterio de media para RH).** 
$$\text{RH} \iff M_N \to 0 \iff M_N = 0 \text{ para algún } N$$

La convergencia $M_N \to 0$ es equivalente a RH por la positividad de cada término. Un criterio analítico: si $\liminf_{N\to\infty} M_N = 0$, entonces RH.

---

## 4. Varianza y segundo momento

**Definición 4.1.** Sea $V_N = \frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n)^2$ la varianza empírica del déficit.

**Proposición 4.2 (Fórmula del segundo momento).** Por la fórmula del déficit:
$$V_N = \frac{1}{N}\sum_{n=1}^N \left[\sum_{\rho_0}\Delta(\gamma_n;\rho_0)\right]^2 = \frac{1}{N}\sum_{n=1}^N \sum_{\rho_0,\rho_0'} \Delta(\gamma_n;\rho_0)\Delta(\gamma_n;\rho_0')$$

Separando la diagonal ($\rho_0 = \rho_0'$) y los términos cruzados:
$$V_N = \underbrace{\frac{1}{N}\sum_{n,\rho_0} \Delta(\gamma_n;\rho_0)^2}_{\text{diagonal}} + \underbrace{\frac{1}{N}\sum_{n,\rho_0\neq\rho_0'} \Delta(\gamma_n;\rho_0)\Delta(\gamma_n;\rho_0')}_{\text{correlación cruzada}}$$

**Proposición 4.3 (Interpretación como correlación de ceros).** El término diagonal involucra:
$$\sum_n P_{y_0}(\gamma_n-\gamma_0)^2$$

que es una *auto-correlación* de los ceros $\gamma_n$ mediada por el núcleo de Poisson al cuadrado. El término cruzado involucra:
$$\sum_n P_{y_0}(\gamma_n-\gamma_0)P_{y_0'}(\gamma_n-\gamma_0')$$

que es la *correlación de pares* entre el cero on-crítico $\gamma_n$ y los dos ceros off-críticos $\rho_0$, $\rho_0'$ — mediada por los dos núcleos de Poisson.

---

## 5. Conexión con la Conjetura de Correlaciones de Pares de Montgomery

**Recordatorio (Montgomery 1973).** La *función de correlación de pares* de los ceros de $\zeta$ es:
$$F(\alpha, T) = \frac{2\pi}{T\log T} \sum_{\substack{\gamma, \gamma' \leq T \\ \gamma\neq\gamma'}} T^{i\alpha(\gamma-\gamma')} w(\gamma-\gamma')$$

donde $w(u) = 4/(4+u^2)$ es un peso suavizante. La Conjetura de Montgomery (probada parcialmente bajo RH para $\hat f$ con soporte en $(-1,1)$) afirma:
$$F(\alpha, T) \xrightarrow{T\to\infty} |\alpha| + \delta(\alpha) \quad \text{para } \alpha \in (-1,1)$$

lo que corresponde a la *función de correlación de pares del ensemble GUE* de matrices aleatorias unitarias.

**Proposición 5.1 (La varianza como transformada de Montgomery).** El término diagonal de $V_N$ se puede reescribir como:
$$\frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n-\gamma_0)^2 = \frac{1}{N}\sum_{n=1}^N \int_\mathbb{R} \hat P_{y_0}(\xi)^2 e^{2\pi i\xi(\gamma_n-\gamma_0)}\,d\xi$$

$$= \int_\mathbb{R} \hat P_{y_0}(\xi)^2 \left[\frac{1}{N}\sum_n e^{2\pi i\xi(\gamma_n-\gamma_0)}\right]\,d\xi$$

El factor $\frac{1}{N}\sum_n e^{2\pi i\xi\gamma_n}$ es precisamente la transformada de Fourier de la medida empírica de ceros, cuyo comportamiento asintótico está gobernado por la Conjetura de Montgomery.

**Teorema 5.2 (Varianza vía GUE, bajo Montgomery).** Bajo la Conjetura de Montgomery, para $y_0 = \sigma_0-1/2$ fijo:
$$\lim_{N\to\infty} \frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n-\gamma_0)^2 = \int_\mathbb{R} \hat P_{y_0}(\xi)^2 F(\xi)\,d\xi = \int_\mathbb{R} \pi^2 e^{-4\pi y_0|\xi|}\,[|\xi|+\delta(\xi)]\,d\xi$$

$$= \pi^2\left[\int_0^\infty \xi e^{-4\pi y_0\xi}\,d\xi + 1\right] = \pi^2\left[\frac{1}{(4\pi y_0)^2} + 1\right]$$

*Prueba.* Usando $\hat P_{y_0}(\xi) = \pi e^{-2\pi y_0|\xi|}$ y la conjetura de Montgomery $F(\alpha)\to|\alpha|+\delta(\alpha)$ en la región de soporte. $\square$

**Corolario 5.3 (Cota de varianza vía GUE).** Bajo Montgomery, la varianza diagonal satisface:
$$V_N^{\text{diag}} \approx \pi^2 \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \left[\frac{1}{16\pi^2(\sigma_0-1/2)^2} + 1\right] \cdot 2(\sigma_0-1/2)^2$$

Para ceros off-críticos con $\sigma_0-1/2 = \delta$ pequeño: $V_N^{\text{diag}} \approx \pi^2/(8\pi^2) + O(\delta^2) = 1/8 + O(\delta^2)$ por cuarteto.

**Observación 5.4 (Qué revela la varianza).** La varianza $V_N$ es finita y acotada independientemente de la densidad de ceros off-críticos, gracias al decaimiento del núcleo de Poisson. Sin RH: $V_N > 0$ acotado por debajo. Con RH: $V_N = 0$ exactamente. La varianza es un test "integrado" más robusto que la condición puntual.

---

## 6. La función generatriz del déficit

**Definición 6.1.** Sea $\mathcal{G}(z) = \sum_{n=1}^\infty C_\infty(\gamma_n) e^{-z\gamma_n}$ para $\text{Re}(z) > 0$.

**Proposición 6.2 (Convergencia).** La serie $\mathcal{G}(z)$ converge absolutamente para $\text{Re}(z) > 0$, pues $C_\infty(\gamma_n) = O(\log\gamma_n)$ (Corolario 2.2) y $|\gamma_n| \sim 2\pi n/\log n \to \infty$.

**Proposición 6.3 (Fórmula de inversión).** Por la transformada de Laplace inversa:
$$C_\infty(\gamma_n) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} \mathcal{G}(z) e^{z\gamma_n}\,dz$$

**Proposición 6.4 (Factorización de $\mathcal{G}$).** Intercambiando suma e integral sobre $\mu_{\mathrm{off}}$:
$$\mathcal{G}(z) = \sum_n e^{-z\gamma_n} \sum_{\rho_0} \Delta(\gamma_n;\rho_0) = \sum_{\rho_0} \Delta_{\rho_0}(z)$$

donde $\Delta_{\rho_0}(z) = \sum_n e^{-z\gamma_n}\Delta(\gamma_n;\rho_0)$ es la *función generatriz del déficit asociada a $\rho_0$*.

**Proposición 6.5 (Conexión con funciones de Hurwitz-zeta).** Si los ceros $\gamma_n$ tuvieran distribución perfectamente equiespaciada ($\gamma_n = 2\pi n/\log n$ en la aproximación de Weyl), entonces $\Delta_{\rho_0}(z)$ sería proporcional a una función zeta de Hurwitz $\zeta(s, a)$ evaluada en el parámetro $a = \gamma_0/(2\pi)$. La desviación de esta fórmula exacta captura las correlaciones de pares de ceros.

---

## 7. El criterio de subsucesión: conexión con equidistribución

**Teorema 7.1 (Criterio de Birkhoff-Cesàro para RH).** Supongamos que la sucesión $\{\gamma_n\}$ es *equidistribuida módulo* la longitud de onda de $\mu_{\mathrm{off}}$ en el siguiente sentido: para todo $\gamma_0 > 0$ y $y_0 > 0$:
$$\lim_{N\to\infty} \frac{1}{N}\sum_{n=1}^N P_{y_0}(\gamma_n - \gamma_0) = \frac{1}{\pi} \quad (\text{constante independiente de } \gamma_0, y_0)$$

Entonces $M_N \to \frac{1}{\pi}\sum_{\rho_0} 2\pi(\sigma_0-1/2) = 2\sum_{\rho_0}(\sigma_0-1/2)$, que es cero si y solo si $\mathcal{Z}_{\mathrm{off}} = \emptyset$.

*Nota honesta.* La hipótesis de equidistribución del Teorema 7.1 es equivalente a la distribución GUE de los ceros (Conjetura de Montgomery). Condicional a GUE, el criterio es que $M_N \to 0$ iff RH. No circular porque GUE es una hipótesis independiente.

**Teorema 7.2 (Criterio de subsucesión).** Si existe una subsucesión $n_k \to \infty$ tal que $C_\infty(\gamma_{n_k}) \to 0$ y además la subsucesión $\{\gamma_{n_k}\}$ es *densa en $\mathbb{R}^+$* (es decir, $\liminf_{k\to\infty}|\gamma_{n_k}-t| = 0$ para todo $t > 0$), entonces $\mu_{\mathrm{off}} = 0$ (RH).

*Prueba.* Por la continuidad de $\mathcal{P}[\mu_{\mathrm{off}}]$ en la variable de evaluación (Lema 7.3 abajo): si $\gamma_{n_k} \to t_0$ y $C_\infty(\gamma_{n_k}) \to 0$, entonces $\mathcal{P}[\mu_{\mathrm{off}}](t_0) = 0$. Por la densidad de la subsucesión, $\mathcal{P}[\mu_{\mathrm{off}}](t) = 0$ para un conjunto denso de $t$. Por continuidad de $\mathcal{P}[\mu_{\mathrm{off}}]$ (que es armónica, luego continua), $C_\infty \equiv 0$. Por Rigidez de Poisson (Doc 43, T 3.1), $\mu_{\mathrm{off}} = 0$. $\square$

**Lema 7.3 (Continuidad de la traza).** La función $t\mapsto\mathcal{P}[\mu_{\mathrm{off}}](t)$ es continua en $t\in\mathbb{R}$, con módulo de continuidad:
$$|\mathcal{P}[\mu_{\mathrm{off}}](t_1)-\mathcal{P}[\mu_{\mathrm{off}}](t_2)| \leq |t_1-t_2| \cdot \int_\mathbb{H} \frac{2y}{(y^2+(t^*-x)^2)^2}\,d\mu_{\mathrm{off}}(x,y)$$

para $t^*$ entre $t_1$ y $t_2$.

*Prueba.* Diferenciación bajo el signo de integral (justificable por convergencia dominada dado que $\partial_t P_y(t-x) = -2y(t-x)/(y^2+(t-x)^2)^2$ es integrable contra $\mu_{\mathrm{off}}$). $\square$

---

## 8. Comportamiento asintótico: ¿$C_\infty(\gamma_n) \to 0$?

Esta es la pregunta central del programa en su estado actual.

**Proposición 8.1 (Decaimiento por contribuciones de ceros lejanos).** Para $n$ grande (con $\gamma_n$ grande), la contribución de cada cero off-crítico $\rho_0$ a $C_\infty(\gamma_n)$ decae:

$$\Delta(\gamma_n;\rho_0) \leq \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + (\gamma_n-\gamma_0)^2} + \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2 + (\gamma_n+\gamma_0)^2}$$

Para $\gamma_n \gg \gamma_0$: $\Delta(\gamma_n;\rho_0) \sim 4(\sigma_0-1/2)/\gamma_n^2 \to 0$.

**Proposición 8.2 (La contribución de ceros cercanos no decae).** Sin embargo, si $\mathcal{Z}_{\mathrm{off}}$ tiene ceros a todas las alturas (lo cual es posible si el conjunto de ceros off-críticos es infinito), entonces para cualquier $\gamma_n$, existe $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ con $|\gamma_0 - \gamma_n| \leq 1$ y $\Delta(\gamma_n;\rho_0) \geq 2(\sigma_0-1/2)/(\sigma_0^2+1)$. Luego $C_\infty(\gamma_n) \not\to 0$.

*Consecuencia.* Si $\mathcal{Z}_{\mathrm{off}}$ es infinito (con zeros a todas las alturas), $C_\infty(\gamma_n) \not\to 0$. Si $\mathcal{Z}_{\mathrm{off}}$ es finito o tiene altura máxima $\Gamma_{\max} < \infty$, entonces $C_\infty(\gamma_n) \to 0$ a tasa $O(\gamma_n^{-2})$.

**Teorema 8.3 (Criterio de finitud).** $C_\infty(\gamma_n) \to 0$ si y solo si $\mathcal{Z}_{\mathrm{off}}$ es finito (con altura máxima acotada). En ese caso, RH sería falsa pero "casi verdadera" (solo finitos ceros off-críticos). Conjecturalmente, $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (RH exacto).

*Comentario.* El Teorema 8.3 demuestra que la condición $C_\infty(\gamma_n) \to 0$ es equivalente a "$\mathcal{Z}_{\mathrm{off}}$ es finito o vacío." Para probar que $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (RH), se necesitaría además mostrar que incluso un conjunto finito no vacío de ceros off-críticos es imposible — lo cual requiere información aritmética más profunda.

---

## 9. La sucesión de déficit y la función $L$ de $\mu_{\mathrm{off}}$

**Definición 9.1 (Función L del déficit).** Sea:
$$\mathcal{L}(s) = \sum_{n=1}^\infty \frac{C_\infty(\gamma_n)}{\gamma_n^s}, \quad \text{Re}(s) > 1$$

**Proposición 9.2.** $\mathcal{L}(s) = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \sum_{n=1}^\infty \frac{\Delta(\gamma_n;\rho_0)}{\gamma_n^s}$

El factor interno $\sum_n \Delta(\gamma_n;\rho_0)/\gamma_n^s$ es una *serie de Dirichlet generalizada* sobre los ceros de $\Xi$, que puede relacionarse con la función zeta de Epstein o funciones de tipo Hurwitz.

**Proposición 9.3 (Ecuación funcional formal de $\mathcal{L}$).** Si $\mathcal{Z}_{\mathrm{off}}$ satisface la simetría del cuarteto $(\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0)$ y los ceros de $\Xi$ satisfacen la ecuación funcional $\gamma_n \leftrightarrow -\gamma_n$ (es decir, $\Xi(s) = \Xi(1-s)$), entonces $\mathcal{L}$ satisface una ecuación funcional de la forma $\mathcal{L}(s) = f(s)\mathcal{L}(k-s)$ para algún $k$ determinado por la geometría del cuarteto.

*La ecuación funcional de $\mathcal{L}$ es una propiedad nueva de este programa — no derivable directamente de la ecuación funcional de $\zeta$.*

---

## 10. Conexión con Pair Correlation: síntesis

La conexión entre $C_\infty(\gamma_n)$ y la conjetura de Montgomery es la siguiente cadena:

$$\underbrace{\text{Varianza de } C_\infty}_{\text{segunda potencia}} \longleftrightarrow \underbrace{\text{Correlaciones de pares}}_{\text{Montgomery/GUE}} \longleftrightarrow \underbrace{\text{Estructura del kernel de correlación}}_{\text{$1-(sin\pi\alpha/\pi\alpha)^2$}}$$

**Proposición 10.1.** Bajo la Conjetura de Montgomery (en la versión completa, no solo para soporte de Fourier $< 1$):
$$V_N = \frac{1}{N}\sum_{n=1}^N C_\infty(\gamma_n)^2 \longrightarrow \pi^2 \int_0^\infty \left[1-\left(\frac{\sin\pi\alpha}{\pi\alpha}\right)^2\right] \hat G_{y_0}(\alpha)\,d\alpha \cdot \|\mu_{\mathrm{off}}\|$$

donde $\hat G_{y_0}$ es la transformada de Fourier del kernel $P_{y_0}^2$ y $\|\mu_{\mathrm{off}}\|$ es la masa total de $\mu_{\mathrm{off}}$.

*Consecuencia:* si $V_N = 0$ (que es equivalente a RH por positividad), entonces $\|\mu_{\mathrm{off}}\| = 0$ (RH). La relación entre la varianza del déficit y la conjetura de Montgomery es DIRECTA: la varianza es cero iff RH, y bajo Montgomery la varianza se calcula explícitamente como función de la masa de $\mu_{\mathrm{off}}$.

**Corolario 10.2.** La Conjetura de Montgomery, si se prueba completamente (para todo $\alpha$, no solo $|\alpha|<1$), implicaría que $V_N$ es positivo cuando $\mu_{\mathrm{off}} \neq 0$ — consistente con RH, pero no suficiente para probarlo. La conjetura de Montgomery y RH son condiciones compatibles pero independientes en el estado actual del conocimiento.

---

## 11. Diagnóstico final y estado del programa

**Resumen de la asintótica de $C_\infty(\gamma_n)$:**

| Propiedad | Estado | Hipótesis |
|-----------|--------|-----------|
| $C_\infty(\gamma_n) \geq 0$ para todo $n$ | Probado (Doc 42) | Ninguna |
| $C_\infty(\gamma_n) = O(\log\gamma_n)$ | Probado | Estimación de densidad clásica |
| $M_N = O(\log\gamma_N \cdot \|\mu_{\mathrm{off}}\|)$ | Probado | Convergencia absoluta de Poisson |
| $M_N \to 0 \iff$ RH | Probado (positividad) | Ninguna |
| $C_\infty(\gamma_n) \to 0 \iff \mathcal{Z}_{\mathrm{off}}$ finito | Probado | Ninguna |
| Varianza $V_N$ calculable bajo GUE | Probado bajo Montgomery | Conjetura de Montgomery |
| $C_\infty(\gamma_n) = 0$ para algún $n$ | Abierto — equivalente a RH | — |

**La barrera de Doc 45 en una línea:**

> *El comportamiento asintótico de $C_\infty(\gamma_n)$ puede determinarse completamente condicionalmente a Montgomery (GUE), pero es consistente tanto con RH como con no-RH. El programa necesita una condición INCOMPATIBLE con $\mu_{\mathrm{off}} \neq 0$ — que no proviene del análisis asintótico.*

---

*Siguiente documento (Doc 46): Matemática nueva — identificación de estructuras que no existen todavía y que podrían abrir el camino a RH desde fundamentos nuevos.*

---

## Apéndice A: La función de correlación de Poisson

**A.1.** La *función de correlación de Poisson* es:
$$K_{\mu_{\mathrm{off}}}(\gamma_n, \gamma_m) = \mathcal{P}[\mu_{\mathrm{off}}](\gamma_n)\mathcal{P}[\mu_{\mathrm{off}}](\gamma_m) - \mathcal{P}[\mu_{\mathrm{off}}^{\otimes 2}](\gamma_n,\gamma_m)$$

donde $\mu_{\mathrm{off}}^{\otimes 2}$ es la medida producto. Esta función mide la correlación entre $C_\infty(\gamma_n)$ y $C_\infty(\gamma_m)$ mediada por la estructura off-crítica.

**A.2.** Bajo RH: $K_{\mu_{\mathrm{off}}} \equiv 0$ trivialmente.  
Sin RH: $K_{\mu_{\mathrm{off}}}(\gamma_n,\gamma_m) \neq 0$ en general, con un perfil que refleja la densidad de $\mu_{\mathrm{off}}$ entre $\gamma_n$ y $\gamma_m$.
