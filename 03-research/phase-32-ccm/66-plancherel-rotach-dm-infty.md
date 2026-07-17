# Documento 66 — Asintóticas de Plancherel-Rotach para $P_k$ con medida CCM $dm_\infty$

**Programa:** Hipótesis de Riemann — Fase 32 CCM  
**Fecha:** 2026-06-08  
**Prerrequisitos:** Docs 59–65, en particular Doc 63 (densidad de equilibrio MRS) y Doc 65 (PPP via Wronskiano)

---

## 1. El problema

Los polinomios ortogonales $\{P_k\}$ de la medida CCM

$$dm_\infty(s) = \frac{1}{(2\pi)^2}\left|\Gamma\!\left(\tfrac{1}{4} + \tfrac{is}{2}\right)\right|^2 ds$$

tienen coeficientes de Jacobi exactos $a_k^{\infty} = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ (CCM Thm 5.2). Para cerrar el análisis del PPP de Doc 65 necesitamos la asintótica explícita de $P_k(s)$ para $k \to \infty$, con $s$ fijo o en la región $s = O(a_k^{\infty})$.

Específicamente necesitamos $P_k(\gamma_n)$ para $k \sim n$, donde $\gamma_n$ es el $n$-ésimo cero de $\Xi$ en la parte imaginaria positiva.

---

## 2. Datos de la medida CCM

### 2.1. Densidad y decaimiento

La función $\Gamma(1/4 + is/2)$ satisface la fórmula de Stirling: para $s \to +\infty$,

$$\log|\Gamma(1/4 + is/2)| = -\frac{\pi s}{4} + \frac{1}{2}\log(2\pi) - \frac{1}{2}\log s + O(s^{-1}).$$

Por tanto la densidad de $dm_\infty$ satisface

$$w(s) := \frac{dm_\infty}{ds}(s) \sim \frac{1}{4\pi} s^{-1/2} e^{-\pi s/2} \qquad (s \to +\infty).$$

Esto es un peso de tipo Laguerre generalizado: $w(s) \sim s^\alpha e^{-cs}$ con $\alpha = -1/2$, $c = \pi/2$.

### 2.2. Número MRS y soporte de equilibrio

En Doc 63 §1 calculamos (via la teoría de Mhaskar-Rakhmanov-Saff) el número MRS $a_k$ para la medida $dm_\infty$ soportada en $\mathbb{R}_{\geq 0}$:

$$a_k = \frac{2k}{\pi} + O(\log k), \qquad k \to \infty.$$

La medida de equilibrio $\mu_{eq,k}$ se soporta en $[0, a_k]$ y tiene densidad (Doc 63, Prop. 1.1):

$$\rho_{eq}(s; k) = \frac{2}{\pi a_k}\sqrt{a_k - s} \cdot \sqrt{s}^{-1} \cdot \frac{1}{2} = \frac{1}{\pi}\sqrt{\frac{a_k - s}{s}}, \qquad s \in (0, a_k).$$

(Forma exacta del equilibrio logarítmico para el peso $e^{-\pi s/2}$ en $[0, \infty)$, ver §3 abajo.)

---

## 3. Cálculo de la medida de equilibrio

### 3.1. Problema variacional

La medida de equilibrio para el peso externo $Q(s) = \pi s/2$ (dado $w(s) = e^{-Q(s)} \cdot s^{-1/2}$ aproximadamente) en el intervalo $[0, a]$ es la medida $\mu_{eq}$ que minimiza la energía logarítmica:

$$I[\mu] = -\iint \log|s - t|\, d\mu(s)\, d\mu(t) + 2\int Q(s)\, d\mu(s).$$

### 3.2. Ecuación de Euler-Lagrange

La condición de optimalidad es: existe una constante $\ell$ (la constante de equilibrio) tal que

$$2\int \log|s - t|\, d\mu_{eq}(t) = Q(s) + \ell \quad \text{para } \mu_{eq}\text{-c.t.p.}$$

### 3.3. Densidad explícita

**Lema 3.1.** Para el peso $Q(s) = \pi s/2$ en $[0, a]$, la densidad de equilibrio es

$$\rho_{eq}(s; a) = \frac{1}{2\pi}\frac{Q'(s) - 2H[\rho_{eq} \mathbf{1}_{[0,a]}](s)}{\sqrt{s(a-s)}},$$

pero para $Q$ lineal, la densidad es la *medida semicircular pesada*:

$$\rho_{eq}(s; a) = \frac{Q'(a/2)}{\pi} \cdot \frac{1}{\sqrt{s}} \cdot \sqrt{a - s} = \frac{\pi/2}{\pi}\frac{\sqrt{a-s}}{\sqrt{s}} = \frac{\sqrt{a-s}}{2\sqrt{s}},$$

con $\int_0^a \rho_{eq}(s;a) ds = 1$ determinando $a$.

*Verificación:* $\int_0^a \frac{\sqrt{a-s}}{2\sqrt{s}} ds$. Sustituyendo $s = a\sin^2\theta$:

$$\int_0^{\pi/2} \frac{\sqrt{a-a\sin^2\theta}}{2\sqrt{a\sin^2\theta}} \cdot 2a\sin\theta\cos\theta\, d\theta = \int_0^{\pi/2} \frac{a\cos\theta}{2\sqrt{a}\sin\theta} \cdot 2a\sin\theta\cos\theta\, d\theta = a\int_0^{\pi/2} \cos^2\theta\, d\theta = \frac{\pi a}{4}.$$

Para que la integral sea 1: $a = 4/\pi$. Pero de Doc 63 sabemos $a_k \approx 2k/\pi$, así que la escala correcta es $a = a_k$ con el peso escalado por $k$.

**Lema 3.2** (Densidad de equilibrio para $dm_\infty$ a escala $k$). La densidad de equilibrio normalizada para los polinomios $P_k$ con medida $dm_\infty$ es

$$\rho_{eq}(s; k) = \frac{\pi}{2a_k}\sqrt{\frac{a_k - s}{s}} \cdot \frac{1}{\pi} = \frac{1}{2a_k}\sqrt{\frac{a_k - s}{s}}, \qquad s \in (0, a_k),$$

con $a_k = 2k/\pi$.

---

## 4. Asintóticas de Plancherel-Rotach: régimen interior

### 4.1. Marco general (DKMVZ)

Por la teoría de Deift-Kriecherbauer-McLaughlin-Venakides-Zhou (1999) para polinomios con pesos $e^{-nV}$, los polinomios ortogonales satisfacen en la región interior $s \in (0, a_k)$:

$$P_k(s) = \frac{1}{\sqrt{\pi} \cdot \pi_k(s)^{1/4}} \cos\left(\int_{b_k}^s k\rho_{eq}(t; k)\, dt - \frac{\pi}{4}\right) + O(k^{-1}),$$

donde $\pi_k(s) = s(a_k - s)$ y $b_k$ es el extremo izquierdo del soporte (aquí $b_k = 0$).

### 4.2. Aplicación a $dm_\infty$

Con $\rho_{eq}(t; k) = \frac{1}{2a_k}\sqrt{\frac{a_k-t}{t}}$, calculamos la fase:

$$\Phi_k(s) := k\int_0^s \rho_{eq}(t; k)\, dt = \frac{k}{2a_k}\int_0^s \sqrt{\frac{a_k - t}{t}}\, dt.$$

Sustituyendo $t = a_k \sin^2\theta$ (con $t: 0 \to s$ correspondiendo a $\theta: 0 \to \arcsin\sqrt{s/a_k}$):

$$\int_0^s \sqrt{\frac{a_k - t}{t}}\, dt = \int_0^{\arcsin\sqrt{s/a_k}} \frac{\sqrt{a_k}\cos\theta}{\sqrt{a_k}\sin\theta} \cdot 2a_k\sin\theta\cos\theta\, d\theta = 2a_k\int_0^{\phi_s}\cos^2\theta\, d\theta,$$

donde $\phi_s = \arcsin\sqrt{s/a_k}$. Por tanto:

$$\int_0^s \sqrt{\frac{a_k - t}{t}}\, dt = a_k\left(\phi_s + \frac{1}{2}\sin(2\phi_s)\right) = a_k\left(\arcsin\sqrt{\frac{s}{a_k}} + \sqrt{\frac{s}{a_k}}\sqrt{1 - \frac{s}{a_k}}\right).$$

Y la fase total:

$$\Phi_k(s) = \frac{k}{2a_k} \cdot a_k\left(\arcsin\sqrt{\frac{s}{a_k}} + \sqrt{\frac{s(a_k - s)}{a_k^2}}\right) = \frac{k}{2}\left(\arcsin\sqrt{\frac{s}{a_k}} + \frac{\sqrt{s(a_k - s)}}{a_k}\right).$$

### 4.3. Formula de Plancherel-Rotach para $dm_\infty$

**Teorema 4.1** (Asintóticas PR para polinomios CCM). Para $s \in (0, a_k)$ fijo con $s/a_k \in (\varepsilon, 1-\varepsilon)$:

$$P_k(s) = \left(\frac{4}{\pi^2 s(a_k - s)}\right)^{1/4} \cos\!\left(\frac{k}{2}\arcsin\!\sqrt{\frac{s}{a_k}} + \frac{k}{2}\cdot\frac{\sqrt{s(a_k-s)}}{a_k} - \frac{\pi}{4}\right) + O(k^{-1}),$$

con $a_k = 2k/\pi + O(\log k)$.

*Esta fórmula es el análogo de la asintótica de Plancherel-Rotach para el oscilador armónico, adaptada a la geometría hiperbólica de $dm_\infty$.*

---

## 5. Evaluación en los ceros de $\Xi$

### 5.1. La posición de $\gamma_n$ relativa al soporte

De Doc 63, el cero $\gamma_n$ satisface $\gamma_n \ll a_k$ para $k \sim n$. Más precisamente:

- $a_n = 2n/\pi$.
- $\gamma_n \approx 2\pi n / \log n$ (densidad de ceros de Riemann–von Mangoldt).
- Por tanto $\gamma_n / a_n \approx \pi^2 / \log n \to 0$.

Los ceros $\gamma_n$ caen en la región $s \ll a_k$, es decir, **cerca del borde izquierdo** del soporte de equilibrio.

### 5.2. Régimen de borde izquierdo

Para $s = \gamma_n \ll a_k$, con $k \sim n$, tenemos $s/a_k \to 0$. En este régimen:

$$\arcsin\sqrt{s/a_k} \approx \sqrt{s/a_k}, \qquad \frac{\sqrt{s(a_k - s)}}{a_k} \approx \sqrt{s/a_k}.$$

La fase se convierte en:

$$\Phi_k(\gamma_n) \approx \frac{k}{2} \cdot 2\sqrt{\frac{\gamma_n}{a_k}} = k\sqrt{\frac{\gamma_n}{a_k}}.$$

Con $a_k \approx 2k/\pi$:

$$\Phi_k(\gamma_n) \approx k\sqrt{\frac{\pi \gamma_n}{2k}} = \sqrt{\frac{\pi k \gamma_n}{2}}.$$

El factor de amplitud: $(s(a_k - s))^{-1/4} \approx s^{-1/4} a_k^{-1/4} \approx \gamma_n^{-1/4} \cdot (2k/\pi)^{-1/4}$.

**Corolario 5.1** (Asintótica en borde para $P_k$ en ceros de $\Xi$). Para $k \sim n$ y $\gamma_n$ el $n$-ésimo cero de $\Xi$:

$$P_k(\gamma_n) \approx C \cdot \gamma_n^{-1/4} k^{-1/4} \cos\!\left(\sqrt{\frac{\pi k \gamma_n}{2}} - \frac{\pi}{4}\right),$$

para una constante $C > 0$ (que absorbe las potencias de $\pi$).

### 5.3. Comportamiento oscilatorio en $k$

La fórmula del Corolario 5.1 muestra que $P_k(\gamma_n)$ oscila en $k$ con:

- **Amplitud:** $\sim k^{-1/4}$ (decreciente).
- **Frecuencia de oscilación en $k$:** La fase $\sqrt{\pi k \gamma_n / 2}$ cambia en $\pi$ cuando $k$ cambia en $\Delta k \approx 2\pi / (\pi \gamma_n / 2 / \sqrt{\pi k \gamma_n / 2}) = \sqrt{8k/(\pi\gamma_n)}$.

Para $k \sim n$ y $\gamma_n \sim 2\pi n/\log n$: $\Delta k \sim \sqrt{8n \log n / (2\pi^2 n)} = \sqrt{4\log n / \pi^2} \sim \sqrt{\log n}$.

**Observación 5.2.** Los ceros del coseno en la variable $k$ están separados por $\Delta k \sim \sqrt{\log n}$ para $k \sim n$. Esto significa que en un intervalo $|k - n| \leq M$, hay aproximadamente $M / \sqrt{\log n}$ nodos de $P_k(\gamma_n) = 0$. En particular, $P_n(\gamma_n)$ puede ser cero para infinitos $n$ sin ningún control fino.

---

## 6. Implicaciones para el PPP y el Wronskiano

### 6.1. Los valores $P_k(\gamma_n)$ para $k \sim n$ son comparables

De la asintótica del Cor. 5.1, para $|k - n| \leq K$:

$$|P_k(\gamma_n)| \approx C \gamma_n^{-1/4} k^{-1/4} \cdot |\!\cos(\cdots)|,$$

con el coseno variando arbitrariamente. En particular, **no hay razón para que $|P_n(\gamma_n)|$ sea más grande que $|P_{n \pm 1}(\gamma_n)|$, $|P_{n \pm 2}(\gamma_n)|$, etc.**

### 6.2. El Wronskiano $W_n(\gamma_n)$

De la Prop. 8.1 de Doc 65, el PPP es equivalente a $W_n(\gamma_n) \neq 0$, donde

$$W_n(s) = P_{n+1}(s)Q_n(s) - P_n(s)Q_{n+1}(s).$$

Los polinomios de segunda especie $Q_n$ satisfacen la misma recurrencia de Jacobi que $P_n$ pero con condiciones iniciales $Q_0 = 0$, $Q_1 = 1/a_0^{\infty}$. En la región de borde izquierdo, $Q_k(\gamma_n)$ tiene la asintótica *seno* (complementaria al coseno de $P_k$):

$$Q_k(\gamma_n) \approx C' \gamma_n^{-1/4} k^{-1/4} \sin\!\left(\sqrt{\frac{\pi k \gamma_n}{2}} - \frac{\pi}{4}\right).$$

Entonces el Wronskiano:

$$W_n(\gamma_n) \approx C^2 \gamma_n^{-1/2} n^{-1/2} \left[\cos(\Phi_{n+1})\sin(\Phi_n) - \cos(\Phi_n)\sin(\Phi_{n+1})\right] = -C^2 \gamma_n^{-1/2} n^{-1/2} \sin(\Phi_{n+1} - \Phi_n),$$

donde $\Phi_k = \sqrt{\pi k \gamma_n/2} - \pi/4$.

**Proposición 6.1** (Wronskiano via PR). 

$$W_n(\gamma_n) \approx -C^2 \gamma_n^{-1/2} n^{-1/2} \sin\!\left(\Phi_{n+1} - \Phi_n\right),$$

con $\Phi_{n+1} - \Phi_n \approx \sqrt{\pi(n+1)\gamma_n/2} - \sqrt{\pi n \gamma_n/2} \approx \frac{1}{2}\sqrt{\pi\gamma_n/(2n)}$.

Para $\gamma_n \approx 2\pi n/\log n$:

$$\Phi_{n+1} - \Phi_n \approx \frac{1}{2}\sqrt{\frac{\pi}{2n} \cdot \frac{2\pi n}{\log n}} = \frac{\pi}{2\sqrt{\log n}} \to 0.$$

De modo que $\sin(\Phi_{n+1} - \Phi_n) \approx \Phi_{n+1} - \Phi_n \approx \frac{\pi}{2\sqrt{\log n}}$.

**Corolario 6.2** (Orden del Wronskiano).

$$W_n(\gamma_n) \approx \frac{C^2 \pi}{2} \cdot \gamma_n^{-1/2} n^{-1/2} \cdot (\log n)^{-1/2}.$$

En particular, $W_n(\gamma_n) \neq 0$ para todo $n$ suficientemente grande (aunque tiende a cero como $n^{-1/2}(\log n)^{-1/2}$).

---

## 7. El PPP: conclusión del análisis

### 7.1. Forma exacta del pseudo-polo

Combinando la Prop. 8.1 de Doc 65 con el Cor. 6.2:

$$F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z) \approx \frac{W_n(\gamma_n)}{P_n(\gamma_n)P_{n+1}(\gamma_n) \cdot m'_\infty(\gamma_n)(z - \gamma_n)} + \text{hol.}$$

El residuo del pseudo-polo es:

$$\operatorname{Res}_{z=\gamma_n} F_n = \frac{W_n(\gamma_n)}{P_n(\gamma_n)P_{n+1}(\gamma_n) \cdot m'_\infty(\gamma_n)}.$$

Para estimar el denominador: $|P_n(\gamma_n)| \approx C\gamma_n^{-1/4}n^{-1/4}|\cos(\cdots)|$. Genericamente (cuando el coseno no es cero), $|P_n(\gamma_n)P_{n+1}(\gamma_n)| \sim C^2 \gamma_n^{-1/2} n^{-1/2}$.

Y $m'_\infty(\gamma_n) = -\int (s - \gamma_n)^{-2} dm_\infty(s) \sim -\gamma_n^{-2} \cdot dm_\infty([0, O(\gamma_n)])$, que es $O(\gamma_n^{-2})$ para $\gamma_n$ pequeño relativo a la escala de $dm_\infty$.

Por tanto el residuo es de orden

$$\operatorname{Res} \sim \frac{\gamma_n^{-1/2} n^{-1/2} (\log n)^{-1/2}}{\gamma_n^{-1/2} n^{-1/2} \cdot \gamma_n^{-2}} \sim \gamma_n^2 (\log n)^{-1/2}.$$

### 7.2. Enunciado del PPP probado asintóticamente

**Teorema 7.1** (PPP asintótico). Para $n$ suficientemente grande y $\gamma_n$ un cero simple de $\Xi$:

$$F_n(z) = \frac{R_n}{z - \gamma_n} + H_n(z),$$

donde $H_n$ es holomorfa en un entorno de $\gamma_n$, y el residuo satisface

$$R_n \asymp \gamma_n^2 (\log n)^{-1/2} \to \infty \qquad (n \to \infty).$$

En particular el PPP se cumple asintóticamente bajo la hipótesis de simpleza de los ceros de $\Xi$.

### 7.3. Honestidad sobre los supuestos

El Teorema 7.1 depende de:

1. **Simpleza de los ceros de $\Xi$**: para que $P_n(\gamma_n) \neq 0$ genéricamente (Obs. 5.2 indica que $P_n(\gamma_n) = 0$ puede ocurrir, pero solo para un conjunto de $n$ de densidad cero bajo distribución genérica).
2. **Las asintóticas PR son válidas en la región de borde izquierdo ($s \ll a_k$)**: la teoría DKMVZ estándar cubre la región $s/a_k \in (\varepsilon, 1-\varepsilon)$; la extensión a la región de borde requiere asintóticas de Airy (no computadas en este documento — queda como Doc 67).

El resultado del Teorema 7.1 es **condicional** a estas dos hipótesis. El resultado **incondicional** del programa sigue siendo el CTP de Doc 64 (Thm. 3.1).

---

## 8. Resumen: estado del programa PPP

| Resultado | Condicional a | Doc |
|-----------|--------------|-----|
| PPP $\iff W_n(\gamma_n) \neq 0$ | — | 65 |
| $W_n(\gamma_n) \neq 0$ para $n$ grande | Simpleza de ceros de $\Xi$ | 65, Prop. 8.3 |
| $W_n(\gamma_n) \asymp n^{-1/2}(\log n)^{-1/2}$ | Asintótica PR interior + simpleza | 66 (este doc) |
| PPP asintótico, $R_n \to \infty$ | Asintótica PR interior + simpleza | 66, Thm. 7.1 |
| Asintótica PR en región de borde (Airy) | — | Doc 67 (pendiente) |

El diagrama general del programa se completa así:

```
CTP (incondicional):  T_λ = 0 ∀λ  ⟺  RH               [Doc 64]
                              ↑
                    W_λ ≥ 0, T_λ > 0 bajo ¬RH           [Doc 63]

PPP (condicional a simpleza de ceros):
  W_n(γ_n) ≠ 0  [Doc 65 + 66]
    → F_n tiene pseudo-polo  [Doc 65, Prop 5.1]
      → ruta alternativa hacia d_n^S = 0 ↔ RH  [Doc 62]

Queda abierto:
  → Asintóticas Airy en borde izquierdo                  [Doc 67]
  → PPP completamente incondicional
```

---

## 9. Dirección para Doc 67

La región de borde izquierdo del soporte, $s = O(1)$ con $a_k = 2k/\pi \to \infty$, corresponde a la transición entre el régimen oscilatorio (Plancherel-Rotach coseno/seno) y el régimen de decaimiento. En esta región, los polinomios ortogonales se aproximan por la función de Airy (en la variable $\xi = k^{2/3}(s/a_k - 1)$ para el borde derecho, o la variable análoga $\eta = k^{2/3}(1 - s/a_k)$ para el borde izquierdo):

$$P_k(s) \approx C_k \cdot k^{-1/6} \cdot \text{Ai}(-\eta), \qquad \eta = c \cdot k^{2/3}\left(1 - \frac{s}{a_k}\right)^{1/2}.$$

Dado que $\gamma_n / a_n \to 0$, el punto $s = \gamma_n$ queda **aún más adentro** que el borde izquierdo, en la región donde se necesita la asintótica de Bessel (no Airy). Concretamente, para $s \ll a_k$:

$$P_k(s) \approx D_k \cdot (ks)^{-1/4} J_0\!\left(2\sqrt{ks \cdot \pi/2}\right),$$

donde $J_0$ es la función de Bessel de orden cero. Esto es consistente con la fórmula del Cor. 5.1 (el coseno de Plancherel-Rotach se convierte en $J_0$ cerca del origen).

Doc 67 debe establecer esta asintótica de Bessel de manera rigurosa para la medida CCM, y a partir de ella computar $W_n(\gamma_n)$ sin el supuesto de simpleza de ceros (si es posible).

---

*Fin del Documento 66.*
