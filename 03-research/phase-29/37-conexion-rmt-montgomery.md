# Phase 29 — Doc 37: Conexión con la Teoría de Matrices Aleatorias y la Conjetura de Montgomery

**Fecha:** junio 2026  
**Objetivo:** Examinar si la Teoría de Matrices Aleatorias (RMT), específicamente la conjetura de correlación de pares de Montgomery y la estructura GUE de los ceros de $\zeta$, puede aportar evidencia o un camino de demostración para Inc. Inv. y en última instancia RH.

---

## 1. Contexto: el obstáculo de Doc 35 (Dirección D)

En Doc 35 (Dirección D, Szegő/Delocalización) se demostró que:

- Los operadores de Jacobi con $b_n \to \infty$ y $a_n \to 0$ (el régimen de $J_\infty$) genéricamente exhiben LOCALIZACIÓN de eigenvectores.
- La perturbación de primer orden da $|c_n|^2 \approx a_0^2/\gamma_n^2 \to 0$ — exactamente el comportamiento opuesto a la delocalización.
- La condición Inc. Inv. ($|c_n|^2 = 1/N$, equipartición en el límite) requiere una propiedad ARITMÉTICA ESPECIAL de los ceros de $\zeta$, no una propiedad genérica de operadores de Jacobi.

**La pregunta:** ¿Es esa propiedad aritmética especial precisamente la estadística GUE que la RMT predice para los ceros de $\zeta$?

---

## 2. La conjetura de Montgomery (1973)

**Definición 1** (función de correlación de pares). Para $T > 0$ y $f \in S(\mathbb{R})$ (Schwartz), la función de correlación de pares normalizada de los ceros de $\zeta$ en $[0,T]$ es:

$$F(\alpha, T) = \frac{2\pi}{T \log T} \sum_{\substack{0 < \gamma, \gamma' \leq T \\ \gamma \neq \gamma'}} f\!\left(\frac{(\gamma-\gamma')\log T}{2\pi}\right),$$

donde la suma corre sobre pares de ceros $\rho = 1/2 + i\gamma$, $\rho' = 1/2+i\gamma'$ (asumiendo RH implícitamente en esta formulación).

**Conjetura de Montgomery (1973).** Para $f$ con soporte en $(-1,1)$ (conjetura fuerte) o para $\hat f$ con soporte en $(-1,1)$ (versión original):

$$\lim_{T\to\infty} F(\alpha, T) = \int_{-\infty}^\infty f(x)\left[1 - \left(\frac{\sin\pi x}{\pi x}\right)^2\right]dx.$$

La función $1 - (\sin\pi x/\pi x)^2$ es precisamente la función de correlación de pares de los eigenvalores de matrices aleatorias GUE (Gaussian Unitary Ensemble). 

**Nota de honestidad.** La conjetura de Montgomery está:
- PROBADA para $\hat f$ con soporte en $(-1,1)$ (Montgomery 1973, condicional a RH).
- NO PROBADA en general — es una conjetura abierta.
- Apoyada por extensiva evidencia numérica (Odlyzko 1987–2001).

---

## 3. La conexión con operadores de Jacobi y delocalización

**Proposición 1** (correlaciones y eigenvectores). Sea $J_\lambda^N$ el operador de Jacobi de la construcción CCM, con eigenvalores $\{t_n^{(\lambda)}\}_{n=1}^N$ y eigenvectores $\{\mathbf{v}_n^{(\lambda)}\}_{n=1}^N$. El coeficiente $c_n^{(\lambda)} = \langle \mathbf{v}_n^{(\lambda)}, \mathbf{e}_1\rangle$ satisface (de Doc 22):

$$|c_n^{(\lambda)}|^2 = \frac{1}{N} \iff m_\lambda^{WT}(z) = m_\lambda^{emp}(z) \text{ para todo } z.$$

La condición $|c_n^{(\lambda)}|^2 = 1/N$ (equipartición, = delocalización maximal en el sentido del punto $\mathbf{e}_1$) equivale a que la medida espectral centrada en $\mathbf{e}_1$ sea la medida empírica de eigenvalores.

**Proposición 2** (el rol de las correlaciones). Si los eigenvalores $t_n^{(\lambda)}$ tienen la misma estructura de correlación de pares que los ceros de $\zeta$ en la escala de $1/\log T$: entonces, por la universalidad de GUE, los eigenvectores de $J_\lambda^N$ deberían satisfacer la delocalización GOE/GUE.

*Motivación:* Para matrices GUE de tamaño $N \times N$: los eigenvalores tienen estadística de correlación de pares con kernel sinusoidal $1-(\sin\pi x/\pi x)^2$, Y los eigenvectores son uniformemente distribuidos en la esfera unitaria de $\mathbb{C}^N$ (por invarianza unitaria). Esto implica $\mathbb{E}[|c_n|^2] = 1/N$ para todo $n$ — exactamente la equipartición.

---

## 4. El modelo de Jacobi aleatorio: la barrera técnica

La conexión entre RMT y delocalización para $J_\infty$ requiere superar una barrera fundamental.

**El modelo GUE NO es un operador de Jacobi en el sentido de $J_\infty$.** 

El GUE tiene:
- Elementos de la diagonal: $b_n \sim \mathcal{N}(0,1)$ (acotados en promedio, varianza fija).
- Elementos off-diagonal: $a_n \sim \mathcal{N}(0,1)/\sqrt{2}$ (acotados).

El operador $J_\infty$ tiene:
- Elementos de la diagonal: $b_n = \gamma_n \to \infty$ (ILIMITADOS).
- Elementos off-diagonal: $a_n \to 0$ (van a 0).

**Proposición 3** (incompatibilidad de regímenes). La delocalización de eigenvectores de matrices GUE (probada por invarianza unitaria) se aplica al régimen ACOTADO. El operador $J_\infty$ vive en el régimen ILIMITADO. Los teoremas de delocalización del tipo GUE no se aplican directamente.

**Corolario 1** (lo que la analogía RMT NO puede hacer). No existe un teorema en la literatura que asegure: "si el espectro de $J_\infty$ tiene correlaciones GUE, entonces los eigenvectores están delocalizados". Esta implicación es una conjetura no establecida para el régimen $b_n \to \infty$.

---

## 5. El camino hacia RMT: el operador de comparación

**Definición 2** (operador de Jacobi rescalado). Para cada escala $T > 0$, sea $J_\infty^{(T)}$ el operador de Jacobi con los ceros de $\zeta$ en $[0,T]$ rescalados a $[-2,2]$ (escala GUE). En la escala local (de $1/\log T$): los eigenvalores $t_n^{(\lambda)}$ tienen separaciones $\sim 2\pi/\log T$ entre ceros consecutivos.

**Proposición 4** (la escala local y la universalidad). En la escala local:

$$\frac{(t_{n+1}^{(\lambda)} - t_n^{(\lambda)})\log T}{2\pi} \to \text{distribución según estadística de ceros de }\zeta.$$

Si la estadística de ceros de $\zeta$ es GUE (conjetura de Montgomery), en la escala local los ceros son "casi GUE". Para operadores de Jacobi en la escala local con espectro GUE: se esperaría delocalización local.

**PERO:** la delocalización LOCAL (en escala de $1/\log T$) no implica directamente la equipartición GLOBAL $|c_n^{(\lambda)}|^2 = 1/N$ (que requiere delocalización en la escala GLOBAL de $[0,T]$).

---

## 6. El resultado de Montgomery y la función $\hat k_\lambda$

**Proposición 5** (la conjetura de Montgomery como restricción sobre $\hat k_\lambda$). La función $\hat k_\lambda$ del programa CCM es el kernel de Weil discreto — una aproximación del kernel $k_\lambda$ continuo. Sus ceros en $\mathbb{C}^+$ reflejan la estructura de los ceros de $\Xi$ en la región relevante.

La función de correlación de pares de los ceros de $\hat k_\lambda$ en la escala local está relacionada con la función de correlación de pares de los ceros de $\Xi$ (= ceros de $\zeta$ en la línea crítica, bajo RH).

Si la conjetura de Montgomery es verdadera: los ceros de $\hat k_\lambda$ (que aproximan los ceros de $\Xi$) tienen estructura GUE en la escala local. Esto significa que en la vecindad de cualquier cero $\gamma_n$, los ceros de $\hat k_\lambda$ se repelen según la regla GUE: la probabilidad de que dos ceros estén a distancia $s$ decrece como $s^2$ para $s \to 0$ (repulsión cuadrática, nivel GUE = $\beta = 2$).

---

## 7. El argumento heurístico: RMT + CCM → Inc. Inv.

**Argumento heurístico (NO es una prueba).** Suponiendo la conjetura de Montgomery (estructura GUE de los ceros de $\zeta$), el siguiente argumento sugiere que Inc. Inv. podría derivarse:

**Paso 1.** La repulsión GUE implica que en la escala local, los ceros de $\hat k_\lambda$ y los eigenvalores de $J_\lambda^N$ se distribuyen de manera estadísticamente INDISTINGUIBLE (si $J_\lambda^N$ heredara la misma estadística). En particular, la "distancia media" entre los dos conjuntos es $o(1/\log T)$ — los eigenvalores convergen a los ceros de $\hat k_\lambda$ más rápido que la escala de separación.

**Paso 2.** Si los eigenvalores $t_n^{(\lambda)}$ y los ceros de $\hat k_\lambda$ convergen (en el límite $\lambda \to \infty$) al mismo conjunto — los ceros de $\Xi$ — esto es exactamente Inc. Inv.

**Problema con el Paso 2.** El Paso 2 requiere justificar que la convergencia $t_n^{(\lambda)} \to \gamma_n$ es más que "estadística" — que hay una convergencia POINTWISE de cada eigenvalor a su correspondiente cero. La estadística GUE solo da convergencia de la medida empirical (débil), no convergencia puntual.

**Proposición 6** (la brecha entre convergencia estadística y puntual). La convergencia de la medida empírica:

$$\frac{1}{N}\sum_n \delta_{t_n^{(\lambda)}} \xrightarrow{w} \frac{1}{N}\sum_n \delta_{\gamma_n}$$

es un enunciado ESTADÍSTICO que no implica $t_n^{(\lambda)} \to \gamma_n$ para cada $n$ individualmente (esto falla para medidas indeterminadas, como demostró Doc 26 para $\mu_\gamma^{real}$).

---

## 8. La conjetura de Montgomery y los ceros complejos de $C_\lambda - \mu_\lambda$

La auditoría de Doc 36 identificó la pregunta clave:

> ¿Puede probarse que los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ escapan cuando $\lambda \to \infty$?

**Proposición 7** (el aporte de RMT a la pregunta de la franja). Supongamos la conjetura de Montgomery. Los ceros de $\hat k_\lambda$ en la franja $0 < \Im(z) \leq \eta$ convergen (por la analogía RMT y la teoría de determinantes de Fredholm de matrices GUE) a los ceros de $\Xi$ en esa franja.

Bajo RH: no hay ceros de $\Xi$ en la franja → $N_{\hat k_\lambda}^{\text{strip}}(T,\eta) \to 0$.

Por $(C_\lambda')$: $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) \to N_\Xi^{\text{real}}(T)$ (los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja se mantienen en número $N_\Xi(T)$ para cada $\lambda$ finito pero deben escapar al borde de la franja $\Im(z) = \eta$ en el límite).

**La pregunta precisa se transforma.** La RMT (bajo la conjetura de Montgomery) da información sobre los ceros de $\hat k_\lambda$ en la franja, pero la pregunta sobre los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja es INDEPENDIENTE: es una pregunta sobre el POTENCIAL $C_\lambda$, no sobre $\hat k_\lambda$.

---

## 9. La obstrucción fundamental y la nueva pregunta

**Proposición 8** (obstrucción fundamental de la ruta RMT). El aporte de la Teoría de Matrices Aleatorias a la demostración de Inc. Inv. (y RH) enfrenta la siguiente obstrucción:

(a) **RMT describe estadísticas globales.** La conjetura de Montgomery da la estructura de correlación en la escala de separación media ($1/\log T$). Inc. Inv. requiere convergencia PUNTUAL de cada eigenvalor a su cero correspondiente.

(b) **El régimen es incorrecto.** Los teoremas de delocalización para GUE se aplican a matrices acotadas. $J_\infty$ tiene espectro ilimitado y $a_n \to 0$ — un régimen para el que no existen teoremas de delocalización análogos.

(c) **La brecha es un INPUT, no un OUTPUT.** Si se asume RH (todos los ceros en la línea crítica), la conjetura de Montgomery provee la estadística GUE de los ceros. Pero para usar esto para PROBAR RH, se necesitaría demostrar GUE sin asumir RH — y la conjetura de Montgomery ES CONDICIONAL a RH.

**Corolario 2** (el círculo vicioso). La cadena lógica completa es:

$$\text{RH} \Rightarrow \text{Conj. Montgomery (GUE)} \Rightarrow \text{Delocalización de }J_\infty \Rightarrow \text{Inc. Inv.} \Rightarrow \text{RH}.$$

La primera implicación es condicional (Montgomery 1973), las implicaciones intermedias son conjeturas, y la última es el Teorema D de Doc 19. Todo el círculo es circular: no da una nueva prueba de RH sin la hipótesis de entrada.

---

## 10. Lo que RMT aporta genuinamente al programa

A pesar de las obstrucciones, RMT aporta lo siguiente que puede ser UTÍL:

**Aportación A (evidencia heurística fuerte).** La consistencia numérica del espectro de $J_\lambda^N$ con GUE (en escalas locales) proporciona evidencia heurística de que Inc. Inv. es verdadero. Esto no es una prueba pero orienta el programa.

**Aportación B (la pregunta de los ceros de $C_\lambda - \mu_\lambda$ en la franja).** La pregunta que Doc 36 identifica como el nuevo camino — ¿los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja escapan incondicionalmente? — es una pregunta ANALÍTICA sobre el potencial $C_\lambda$, no una pregunta espectral. La RMT no la responde pero identifica lo que se necesita: una prueba de que la función $C_\lambda(z) = \mu_\lambda$ no tiene soluciones complejas en la franja para $\lambda$ grande.

**Aportación C (el teorema de Montgomery como condicional).** Si se demuestra Inc. Inv. por otros medios: el Teorema D (Inc. Inv. $\Rightarrow$ RH, Doc 19) completa la prueba. Y la conjetura de Montgomery daría entonces una descripción precisa de la estadística del espectro de $J_\infty$ — una consecuencia elegante del programa CCM.

**Aportación D (nuevo sub-programa).** Estudiar directamente la distribución de los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$ como función de $\lambda$. Si se puede mostrar que esos ceros se mueven hacia $\Im(z) = \eta$ cuando $\lambda$ crece (con velocidad controlable): eso daría una demostración de que no hay ceros de $C_\infty$ en la franja — que es más débil que RH pero un avance real.

---

## 11. Conclusión: el estado de la Dirección D (actualizada)

**Síntesis de Docs 35 y 37.** La Dirección D (Szegő/Delocalización/RMT) revela:

1. La delocalización de eigenvectores de $J_\infty$ NO es una propiedad genérica (Doc 35): requiere propiedades aritméticas especiales de los ceros de $\zeta$.

2. Las propiedades aritméticas en cuestión son exactamente las que la conjetura de Montgomery predice (GUE) — pero esa conjetura es condicional a RH (Doc 37).

3. La conexión RMT crea un círculo vicioso (Doc 37, Corolario 2) que no permite una prueba nueva.

4. Sin embargo, la ruta no está completamente cerrada: la pregunta de los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja (Doc 36, §9; Doc 37, §8) es una pregunta ANALÍTICA independiente de RMT — y potencialmente atacable.

**Estado de la Dirección D:** Muro profundo identificado. La única apertura genuina es la pregunta analítica de la franja (vía la auditoría de Doc 36, Prop. 10).

---

## 12. Resumen ejecutivo para el Programa

**Después de Docs 32-37 (Fase 30/Fase 29):**

| Dirección | Estado | Bloqueo principal |
|-----------|--------|-------------------|
| A (Weil puntual) | Cerrada | La fórmula de Weil es distribucional, no puntual |
| B (Conteo EF2-emp) | Resuelta (auditoría) | El argumento de Doc 32 era inválido; la pregunta de la franja es nueva |
| C (Phragmén-Lindelöf) | Circular | PL presupone holomorfia de Q |
| D (Szegő/RMT) | Muro profundo | La conjetura de Montgomery es condicional a RH |

**La única apertura no cerrada:** La pregunta de los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja, identificada en Doc 36. Se propone como Fase 31.

---

*Siguiente: Phase 31 — Análisis de los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$.*
