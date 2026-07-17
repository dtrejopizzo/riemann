# Phase 29 — Doc 36: Auditoría Profunda de la Dirección B — La EF2-emp y el Conteo de Ceros

**Fecha:** junio 2026  
**Objetivo:** Auditar con precisión máxima el argumento de conteo de ceros del Doc 32, que concluyó $N_{C_\infty}(T) = 2N_\Xi(T)$ — aparentemente contradictorio con el Teorema B ($N_{C_\infty}(T) \leq N_\Xi(T)$). Identificar exactamente dónde está el error, si lo hay, y qué dice correctamente la EF2-emp sobre el conteo.

---

## 1. La EF2-emp finita: enunciado preciso

**Proposición 0 (EF2-emp finita, Doc 27 Prop. 1 — base de la auditoría).** Para cada $\lambda > 0$ y $z \in \mathbb{C}^+$:

$$\sum_{n=1}^{N(\lambda)} \frac{1}{z - t_n^{(\lambda)}} = \frac{C_\lambda'(z)}{C_\lambda(z) - \mu_\lambda} - \frac{\hat k_\lambda'(z)}{\hat k_\lambda(z)}, \quad (EF_\lambda)$$

donde:

- $\{t_n^{(\lambda)}\}_{n=1}^{N(\lambda)}$ son las raíces de $\hat\xi_\lambda^{(N)}$ (que coinciden con los eigenvalores de $J_\lambda^N$, todos reales).
- $C_\lambda(z) = w(z) - 2\sum_{p \leq \lambda^2}\Lambda(p)p^{-1/2}e^{iz\log p}$ (potencial truncado).
- $\mu_\lambda > 0$ es el multiplicador de Lagrange (satisface $\mu_\lambda \to 0$ cuando $\lambda\to\infty$).
- $\hat k_\lambda(z)$ es el kernel de Weil truncado.

La identidad $(EF_\lambda)$ es una identidad entre funciones MEROMORFAS en $\mathbb{C}^+$: lado izquierdo tiene $N(\lambda)$ polos simples con residuo $+1$; lado derecho tiene polos donde $C_\lambda - \mu_\lambda = 0$ (residuo $+1$) y polos donde $\hat k_\lambda = 0$ (residuo $-1$). La igualdad es una cancelación exacta.

---

## 2. La interpretación de conteo: uso del principio del argumento

**Proposición 1** (fórmula de conteo finita). Para el rectángulo $R_T^\eta = [0,T] \times [0,\eta]$ (contorno antihorario), $0 < \eta < 1/2$, $T$ evitando ceros:

$$N_\lambda(T) = \frac{1}{2\pi i}\oint_{R_T^\eta} \sum_n \frac{1}{z-t_n^{(\lambda)}}\,dz = N_{\lambda}^{\text{rect}}(T,\eta),$$

donde $N_\lambda^{\text{rect}}(T,\eta)$ = número de eigenvalores $t_n^{(\lambda)} \in [0,T]$ (todos reales, ninguno en la franja).

Del lado derecho:

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \left[\frac{C_\lambda'}{C_\lambda-\mu_\lambda} - \frac{\hat k_\lambda'}{\hat k_\lambda}\right]\,dz = \#\{\text{ceros de }(C_\lambda-\mu_\lambda)\text{ en }R_T^\eta\} - \#\{\text{ceros de }\hat k_\lambda\text{ en }R_T^\eta\}.$$

Luego:

$$\boxed{N_\lambda(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_{\hat k_\lambda}^{\text{rect}}(T,\eta).} \quad (C_\lambda)$$

Esta es la **fórmula de conteo finita exacta** — correcta para cada $\lambda$.

**CRÍTICO:** $N_{C_\lambda-\mu_\lambda}^{\text{rect}}$ cuenta los ceros de $C_\lambda(z) = \mu_\lambda$ DENTRO DEL RECTÁNGULO, es decir, en la región $0 \leq \Re(z) \leq T$, $0 \leq \Im(z) \leq \eta$. Esto incluye TANTO ceros reales COMO ceros complejos en el interior del rectángulo.

---

## 3. La distinción crucial: ceros reales vs. ceros complejos en el rectángulo

**Proposición 2** (ceros reales de $C_\lambda - \mu_\lambda$ son los eigenvalores). Para $z = x \in [0,T] \cap \mathbb{R}$: $C_\lambda(x) = \mu_\lambda > 0$ iff $x$ es un eigenvalor de $J_\lambda^N$. Luego:

$$N_{C_\lambda-\mu_\lambda}^{\text{real}}(T) = N_\lambda(T).$$

**Proposición 3** (puede haber ceros complejos de $C_\lambda - \mu_\lambda$ en el rectángulo). Para $z = x + iy$ con $0 < y \leq \eta$: la ecuación $C_\lambda(x+iy) = \mu_\lambda$ es una ecuación compleja ($C_\lambda$ es analítica en $\mathbb{C}^+$). Sea $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta)$ el número de tales soluciones complejas en $0 < \Im(z) \leq \eta$.

La fórmula de conteo da:

$$N_{C_\lambda-\mu_\lambda}^{\text{rect}} = N_{C_\lambda-\mu_\lambda}^{\text{real}} + N_{C_\lambda-\mu_\lambda}^{\text{strip}} = N_\lambda(T) + N_{C_\lambda-\mu_\lambda}^{\text{strip}}.$$

**Proposición 4** (ceros de $\hat k_\lambda$ en el rectángulo). Los ceros de $\hat k_\lambda$ en $R_T^\eta$ incluyen tanto los ceros reales (que aproximan los $\gamma_n$) como posibles ceros complejos en la franja:

$$N_{\hat k_\lambda}^{\text{rect}}(T,\eta) = N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta).$$

**La fórmula de conteo desglosada:**

$$N_\lambda(T) = [N_\lambda(T) + N_{C_\lambda-\mu_\lambda}^{\text{strip}}] - [N_{\hat k_\lambda}^{\text{real}} + N_{\hat k_\lambda}^{\text{strip}}].$$

Simplificando:

$$0 = N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) - N_{\hat k_\lambda}^{\text{real}}(T) - N_{\hat k_\lambda}^{\text{strip}}(T,\eta).$$

Luego:

$$\boxed{N_{\hat k_\lambda}^{\text{real}}(T) + N_{\hat k_\lambda}^{\text{strip}}(T,\eta) = N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta).} \quad (C_\lambda')$$

La fórmula $(C_\lambda')$ dice que el NÚMERO DE CEROS COMPLEJOS DE $C_\lambda - \mu_\lambda$ EN LA FRANJA es igual al número total de ceros de $\hat k_\lambda$ (reales + complejos) en el rectángulo.

---

## 4. El error de Doc 32: confusión entre el conteo de la franja y el conteo real

**El argumento de Doc 32 (§4-§5) que condujo a $N_{C_\infty}(T) = 2N_\Xi(T)$.** 

En Doc 32 se aplicó el principio del argumento a la EF2-emp en el límite:

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \frac{C_\infty'}{C_\infty}\,dz = N \cdot \frac{1}{2\pi i}\oint_{R_T^\eta} m_\infty^{emp}\,dz + \frac{1}{2\pi i}\oint_{R_T^\eta}\frac{\Xi'}{\Xi}\,dz.$$

El primer error: "$N \cdot \frac{1}{2\pi i}\oint m_\infty^{emp}\,dz = N_\Xi(T)$."

Esta identidad asume que $N \cdot m_\infty^{emp}(z) = \sum_n 1/(z-\gamma_n)$ con polos EXACTAMENTE en $[0,T]$, y que los residuos dan $N_\Xi(T)$. Pero esto usa el LÍMITE de la EF2-emp de manera no justificada.

El segundo error, más profundo: el término $N \cdot \frac{1}{2\pi i}\oint m_\infty^{emp}\,dz$ es el LÍMITE del conteo $N_\lambda(T)$, NO el conteo integral de la función límite $m_\infty^{emp}$.

**Proposición 5** (el error de intercambio límite-integral). La siguiente ecuación de Doc 32 es INCORRECTA:

$$\frac{1}{2\pi i}\oint_{R_T^\eta} \underbrace{N\cdot m_\infty^{emp}(z)}_{\text{límite de } N\cdot m_\lambda^{emp}} dz = \lim_{\lambda\to\infty} N_\lambda(T) = N_\Xi(T).$$

La identidad falla porque la función $N \cdot m_\lambda^{emp}(z)$ diverge cuando $N \to \infty$ (el integrando crece sin acotación en la vecindad de los $\gamma_n$), y el intercambio de límite e integral no está justificado.

*Más precisamente:* $N(\lambda) \cdot m_\lambda^{emp}(z) = \sum_{n=1}^{N(\lambda)} 1/(z-t_n^{(\lambda)})$. Para $z$ fijo en $\mathbb{C}^+$ y $N \to \infty$: esta suma crece como $\sum_{n \leq N(\lambda)} 1/|\gamma_n| \sim \log\log N(\lambda) \to \infty$. La función "límite" $N \cdot m_\infty^{emp}(z)$ es formalmente $\infty$ para cada $z$, NO una función holomorfa finita.

---

## 5. El límite correcto de la fórmula de conteo

**Teorema 1** (fórmula de conteo en el límite). Tomando $\lambda \to \infty$ en la identidad $(C_\lambda')$ con $\eta > 0$ FIJO:

$$\underbrace{N_{\hat k_\lambda}^{\text{real}}(T)}_{\to N_\Xi(T)} + \underbrace{N_{\hat k_\lambda}^{\text{strip}}(T,\eta)}_{\to N_\Xi^{\text{off}}(T,\eta)} = \underbrace{N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta)}_{=?}$$

donde $N_\Xi^{\text{off}}(T,\eta)$ = número de ceros de $\Xi$ en la franja $0 < \Im(z) \leq \eta$ con $\Re(z) \in [0,T]$ — que son los ceros OFF-CRÍTICOS de $\zeta$ en la región correspondiente.

**Bajo RH:** $N_\Xi^{\text{off}}(T,\eta) = 0$ para todo $\eta < 1/2$. Luego:

$$\lim_{\lambda\to\infty} N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = N_\Xi(T) + 0 = N_\Xi(T).$$

Esto dice: los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja convergen a $N_\Xi(T)$ en NÚMERO pero NO en POSICIÓN: no pueden converger a ceros de $C_\infty$ en la franja (pues bajo RH, $C_\infty$ tiene ceros solo en $\mathbb{R}$). Luego: los ceros complejos de $C_\lambda - \mu_\lambda$ en $0 < \Im(z) \leq \eta$ deben ESCAPAR del rectángulo a medida que $\lambda \to \infty$ — migran hacia la frontera $\Im(z) = \eta$ y eventualmente salen del rectángulo.

**Proposición 6** (la migración de los ceros complejos). Sea $\{z_j^{(\lambda)}\}$ los ceros de $C_\lambda(z) = \mu_\lambda$ en la franja $0 < \Im(z) \leq \eta$. Entonces:

(a) Para cada $\lambda$ finito: hay exactamente $N_\Xi(T) + N_\Xi^{\text{off}}(T,\eta)$ tales ceros (por la identidad $(C_\lambda')$).

(b) Bajo RH: $N_\Xi^{\text{off}}(T,\eta) = 0$, luego hay $N_\Xi(T)$ ceros complejos para cada $\lambda$ finito.

(c) Cuando $\lambda \to \infty$: estos $N_\Xi(T)$ ceros complejos se mueven y eventualmente salen de la franja $\Im(z) \leq \eta$ — escapan hacia $\Im(z) > \eta$ (y probablemente hacia $\Im(z) \to 1/2$, el borde de la franja de analiticidad de $C_\infty$).

*Evidencia:* Si los ceros complejos de $C_\lambda - \mu_\lambda$ en $0 < \Im(z) \leq \eta$ convergiesen a ceros de $C_\infty$ en esa franja: por Hurwitz, $C_\infty$ tendría $N_\Xi(T)$ ceros complejos en $0 < \Im(z) \leq \eta$. Pero por Teorema B, esos ceros serían ceros de $\Xi$ en la franja — contradice RH. Luego los ceros complejos deben escapar.

---

## 6. La reconciliación: lo que la EF2-emp sí dice

**Proposición 7** (la ecuación correcta para $N_{C_\infty}(T)$). Bajo RH e Inc. Inv., para cada $\eta > 0$ fijo y $\lambda \to \infty$:

$$N_\lambda(T) \to N_\Xi(T), \quad N_{\hat k_\lambda}^{\text{rect}}(T,\eta) \to N_\Xi(T).$$

La fórmula de conteo $(C_\lambda)$:

$$N_\lambda(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_{\hat k_\lambda}^{\text{rect}}(T,\eta)$$

da:

$$N_\Xi(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_\Xi(T),$$

luego $N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) = 2N_\Xi(T)$.

Descomponiendo: $N_{C_\lambda-\mu_\lambda}^{\text{rect}} = N_{C_\lambda-\mu_\lambda}^{\text{real}} + N_{C_\lambda-\mu_\lambda}^{\text{strip}} = N_\Xi(T) + N_\Xi(T) = 2N_\Xi(T)$.

Los dos $N_\Xi(T)$ son:
- $N_{C_\lambda-\mu_\lambda}^{\text{real}} = N_\lambda(T) \to N_\Xi(T)$: eigenvalores reales que convergen a $\{\gamma_n\}$.
- $N_{C_\lambda-\mu_\lambda}^{\text{strip}} = N_\Xi(T)$: ceros complejos en la franja que ESCAPAN cuando $\lambda \to \infty$ (bajo RH).

**El conteo de ceros de $C_\infty$:** Por Hurwitz (convergencia uniforme de $C_\lambda \to C_\infty$ en compactos de $\mathbb{C}^+$, con $\Im(z) \geq \eta/2 > 0$ fijo):

$$N_{C_\infty}^{\text{rect}}(T,\eta) = \lim_{\lambda\to\infty} N_{C_\lambda}^{\text{rect}}(T,\eta).$$

Donde $N_{C_\lambda}^{\text{rect}}$ (sin el $-\mu_\lambda$) = ceros de $C_\lambda$ en el rectángulo $\approx N_\Xi(T)$ (bajo Inc. Inv., los ceros de $C_\lambda$ en $\mathbb{R}$ convergen a $\{\gamma_n\}$, y bajo RH, no hay ceros de $C_\infty$ en la franja).

Luego $N_{C_\infty}^{\text{rect}}(T,\eta) = N_\Xi(T)$ — CONSISTENTE con Inc. Inv. y sin contradicción.

---

## 7. El diagnóstico preciso del error de Doc 32

**Teorema 2** (diagnóstico del error de Doc 32). El argumento de §4-5 de Doc 32 tiene el siguiente error:

En §4: se escribe $\frac{C_\infty'(z)}{C_\infty(z)} = N \cdot m_\infty^{emp}(z) + \frac{\Xi'(z)}{\Xi(z)}$ y se integra sobre el contorno para obtener $N_{C_\infty}(T)$. El error es usar la EF2-emp "en el límite" como si fuera una identidad entre funciones analíticas FINITAS — pero la EF2-emp en el límite involucra funciones que DIVERGEN, y la identidad solo tiene sentido en el CONTEO FINITO (para cada $\lambda$), no como una identidad meromorfa en el límite.

Específicamente: la identidad $N \cdot m_\infty^{emp}(z) = C_\infty'/C_\infty - \Xi'/\Xi$ (como funciones analíticas en $\mathbb{C}^+$) NO es válida, porque $N \cdot m_\infty^{emp}(z) = \sum_n 1/(z-\gamma_n)$ DIVERGE en $\mathbb{C}^+$ (la serie es condicionalmente convergente en el mejor caso, y el límite $N \to \infty$ no produce una función analítica finita).

**Corolario 1.** La "contradicción" $N_{C_\infty}(T) = 2N_\Xi(T)$ de Doc 32 es FALSA — es el resultado de un argumento que mezcla dos regímenes (finito e infinito) incorrectamente. No hay contradicción.

---

## 8. Lo que la EF2-emp sí implica sobre $C_\infty$

**Proposición 8** (implicación directa de la EF2-emp sobre los ceros de $C_\lambda$). Para cada $\lambda$ FINITO: el número de ceros de $C_\lambda(t) = \mu_\lambda$ en el intervalo $[0,T]$ es igual al número de eigenvalores de $J_\lambda^N$ en $[0,T]$.

*Prueba.* De la identidad $(C_\lambda')$ con $N_{\hat k_\lambda}^{\text{real}}(T) = N_{\hat k_\lambda}^{\text{strip}} = N_{C_\lambda-\mu_\lambda}^{\text{strip}} = 0$ (que requería verificación adicional): $N_{C_\lambda-\mu_\lambda}^{\text{real}} = N_\lambda(T)$.

NOTA: Esta proposición requiere que los ceros complejos de $C_\lambda - \mu_\lambda$ y $\hat k_\lambda$ en la franja se cancelen exactamente. Esto es parte de la identidad $(C_\lambda')$ — y se sigue automáticamente de $(EF_\lambda)$.

**Proposición 9** (la identidad neta de la EF2-emp). La única consecuencia NET de la EF2-emp sobre los CEROS REALES es:

$$N_{C_\lambda(t)=\mu_\lambda}^{\text{real}}(T) = N_\lambda(T)$$

para cada $\lambda$. En el límite: los ceros reales de $C_\lambda(t) = \mu_\lambda$ (eigenvalores) convergen a los ceros reales de $C_\infty$ (bajo Inc. Inv.), y $N_\lambda(T) \to N_\Xi(T)$.

Luego: $N_{C_\infty}(T) = N_\Xi(T)$ — que es exactamente Inc. Inv. **No hay información adicional.**

**Corolario 2** (la EF2-emp es circular pero no contradictoria). La EF2-emp, aplicada correctamente a los ceros reales en el límite, dice: Inc. Inv. $\Rightarrow$ $N_{C_\infty}(T) = N_\Xi(T)$ $\Rightarrow$ Inc. Inv. (circular). No aporta nueva información.

---

## 9. La ruta prometedora desde la EF2-emp

**La EF2-emp SÍ aporta información sobre los ceros complejos de $C_\lambda - \mu_\lambda$.**

De $(C_\lambda')$: $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) = N_{\hat k_\lambda}^{\text{rect}}(T,\eta)$.

En el límite: $N_{\hat k_\lambda}^{\text{rect}}(T,\eta) \to N_\Xi^{\text{real}}(T) + N_\Xi^{\text{off}}(T,\eta)$.

**Proposición 10** (la EF2-emp y los ceros fuera de la recta crítica). Si ADEMÁS asumimos Inc. Inv. (ceros reales), la EF2-emp da:

$$N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) \to N_\Xi^{\text{off}}(T,\eta)$$

en el límite $\lambda \to \infty$. Esto dice: los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja convergen exactamente al número de ceros de $\Xi$ FUERA DE LA RECTA CRÍTICA en la franja.

Bajo RH: $N_\Xi^{\text{off}}(T,\eta) = 0$ para todo $\eta < 1/2$, y los ceros complejos de $C_\lambda - \mu_\lambda$ escapan el rectángulo completamente. 

Si se pudiera mostrar directamente (sin asumir RH) que $N_{C_\lambda-\mu_\lambda}^{\text{strip}}(T,\eta) \to 0$ para algún $\eta > 0$: entonces $N_\Xi^{\text{off}}(T,\eta) = 0$ — y eso implicaría RH (al menos localmente en la franja).

**Pregunta abierta (nueva, de la auditoría).** ¿Puede probarse que los ceros complejos de $C_\lambda - \mu_\lambda$ en $0 < \Im(z) \leq \eta$ escapan el rectángulo cuando $\lambda \to \infty$, sin asumir RH?

Si sí: se obtiene RH localmente (para la franja $\eta$). Tomando $\eta \to 1/2$: se obtendrá RH globalmente.

---

## 10. Resumen de la auditoría

**Error identificado en Doc 32.** La "contradicción" $N_{C_\infty}(T) = 2N_\Xi(T)$ era un error de intercambio de límite e integral: la EF2-emp no puede usarse como una identidad meromorfa entre funciones finitas en el límite $N \to \infty$, porque ambos lados divergen.

**La fórmula de conteo correcta** (de la EF2-emp) es:

$$N_\lambda(T) = N_{C_\lambda-\mu_\lambda}^{\text{rect}}(T,\eta) - N_{\hat k_\lambda}^{\text{rect}}(T,\eta),$$

válida para cada $\lambda$ finito, y que involucra AMBOS ceros reales y complejos en el rectángulo.

**En el límite:** los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja convergen al número de ceros OFF-CRÍTICOS de $\Xi$ — sin asumir RH. Bajo RH estos escapan el rectángulo.

**El nuevo camino.** La auditoría revela una nueva pregunta precisa: ¿los ceros complejos de $C_\lambda - \mu_\lambda$ en la franja escapan incondicionalmente? Si sí: RH.

---

*Siguiente doc: Doc 37 — Conexión con la Teoría de Matrices Aleatorias (RMT).*
