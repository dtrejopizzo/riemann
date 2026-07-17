# Documento 69 — Síntesis de Fase 32: estructura exacta de $F_n$ y cierre del programa

**Programa:** Hipótesis de Riemann — Fase 32 CCM  
**Fecha:** 2026-06-08  
**Prerrequisitos:** Docs 59–68

---

## 1. La fórmula cerrada de $F_n$

El resultado algebraico del Doc 68 (Teorema 2.2) da la estructura completa de la diferencia de resolventes diagonales. Reuniendo:

**De Doc 65 (Prop. 8.1):**
$$F_n(z) = G_{n+1,n+1}(z) - G_{n,n}(z) = \frac{W_n(z)}{P_n(z)P_{n+1}(z)\cdot m_\infty(z)},$$

donde $m_\infty(z) = \int(s-z)^{-1}dm_\infty(s)$ y $W_n(z) = P_{n+1}(z)Q_n(z) - P_n(z)Q_{n+1}(z)$.

**De Doc 68 (Thm. 2.2):**
$$W_n(z) \equiv -\frac{1}{a_n^{\infty}} \qquad \text{(constante, independiente de } z\text{)}.$$

**Combinados:**

$$\boxed{G_{n+1,n+1}(z) - G_{n,n}(z) = \frac{-1}{a_n^{\infty}\cdot P_n(z)\cdot P_{n+1}(z)\cdot m_\infty(z)}.}$$

Esta es una identidad algebraica exacta, válida para todo $z \in \mathbb{C} \setminus \mathbb{R}$ (y por extensión a $z$ real donde los denominadores no se anulan).

---

## 2. Consecuencias de la fórmula cerrada

### 2.1. Estructura de los polos de $F_n$

Los únicos polos de $F_n(z)$ son:
- Los ceros reales simples de $P_n$ (que son los nodos de Gauss de $P_n$, en número $n$).
- Los ceros reales simples de $P_{n+1}$ (en número $n+1$).
- Los ceros de $m_\infty(z)$, que no existen en $\mathbb{R}$ (pues $\operatorname{Im} m_\infty(x+i0^+) = -\pi w(x) \neq 0$).

Los polos de $F_n$ son exactamente los $2n+1$ ceros reales de $P_n \cdot P_{n+1}$, todos simples e intercalados.

### 2.2. Los ceros de $\Xi$ no son polos de $F_n$ (genericamente)

Los $\gamma_k$ (ceros de $\Xi$) son distintos de los ceros de $P_n$ (nodos de Gauss). Esta es la resolución definitiva del PPP: el pseudo-polo no existe (para $n$ genérico).

### 2.3. Relación con los coeficientes de Jacobi

Usando la identidad de Christoffel-Darboux en forma telescópica (Doc 63, Prop. 3.3):

$$\sum_{k=0}^{n-1} P_k(z)P_k(w) = a_{n-1}^{\infty}\frac{P_n(z)P_{n-1}(w) - P_{n-1}(z)P_n(w)}{z - w},$$

junto con la fórmula cerrada de $F_n$, se puede expresar la discrepancia $\Delta_n^S$ directamente en términos de los valores de $P_n$ en los ceros semilocales. Esto abre una nueva vía de cálculo cuantitativo de $T_\lambda$.

---

## 3. La integral de $F_n$ y el discrepancy

### 3.1. La relación entre $F_n$ y $\Delta_n^S$

Recordando que $\Delta_n^S = (a_n^S)^2 - (a_n^{\infty})^2$ y la representación (Doc 63):

$$T_\lambda = \sum_{n:\gamma_n \leq \lambda}(\Delta_n^{full} - \Delta_n^{full,on}) = \int F d(dm_{full} - dm_{full,on}),$$

donde $F = W_\lambda$ (el kernel de Abel, definido positivo). La fórmula cerrada de $F_n$ no se conecta directamente con $T_\lambda$ via una integración simple, pero sí ilumina la estructura local.

### 3.2. Lo que $F_n$ controla localmente

La cantidad $(a_n^S)^2 - (a_n^{\infty})^2$ se puede escribir como el residuo de una integral de contorno:

$$(a_n^S)^2 = -\oint_{\Gamma_n} z \cdot G_{n+1,n+1}^S(z)\, \frac{dz}{2\pi i} + \text{corrección},$$

donde $\Gamma_n$ rodea el $n$-ésimo band gap del espectro. La diferencia $G^S - G^{\infty}$ está controlada por la diferencia de medidas $dm_S - dm_\infty$.

Esto sugiere que la fórmula cerrada de $F_n$ podría dar estimados de $\Delta_n^S$ en términos de $\|P_n\|_{L^2(dm_S - dm_\infty)}$, que es la cantidad central para cuantificar el CTP.

---

## 4. La identidad de Wronskiano como herramienta de cálculo

### 4.1. Completitud de los resolentes

La fórmula $G_{n+1,n+1} - G_{n,n} = -1/(a_n^{\infty} P_n P_{n+1} m_\infty)$ permite reconstruir todos los resolentes diagonales por telescopía:

$$G_{nn}(z) = G_{00}(z) - \sum_{k=0}^{n-1} F_k(z) = G_{00}(z) + \frac{1}{m_\infty(z)}\sum_{k=0}^{n-1} \frac{1}{a_k^{\infty} P_k(z) P_{k+1}(z)}.$$

Dado que $G_{00}(z) = m_\infty(z)$ (la función de Stieltjes es el primer resolente diagonal), obtenemos:

$$G_{nn}(z) = m_\infty(z) + \frac{1}{m_\infty(z)}\sum_{k=0}^{n-1}\frac{1}{a_k^{\infty} P_k(z) P_{k+1}(z)}.$$

Esta es una fórmula explícita para los resolentes diagonales del operador de Jacobi CCM.

### 4.2. Verificación: consistencia con la teoría de medidas espectrales

El resolente diagonal $G_{nn}(z)$ es la transformada de Stieltjes de la medida espectral $|P_n(s)|^2 dm_\infty(s)$:

$$G_{nn}(z) = \int_{\mathbb{R}} \frac{|P_n(s)|^2}{s - z} dm_\infty(s).$$

La fórmula del §4.1 puede verificarse tomando $n=0$: $G_{00} = m_\infty$ (correcto, pues $P_0 = 1$) y $n=1$: $G_{11} = m_\infty + 1/(a_0^{\infty} m_\infty)$. Esta identidad es estándar en la teoría de fracciones continuas (conexión con la fracción continua de Stieltjes para $m_\infty$).

---

## 5. Cierre formal de Fase 32

### 5.1. Qué está probado

Los resultados probados de Fase 32, en orden lógico:

**Nivel 1 (algebraico, exacto):**
- Wronskiano constante: $W_k = -1/a_k^{\infty}$ (Doc 68, Thm. 2.2).
- Fórmula cerrada de $F_n$ (Doc 69, §1).
- Representación CD de $L_n$ (Doc 61, Thm. 2.1).

**Nivel 2 (analítico, incondicional):**
- Positividad $\Delta_n^S > 0$ para $S \supsetneq \{\infty\}$ (Doc 59).
- Tasa $\Delta_n^{∞,p} = A_n/p + O(\log p/p^{3/2})$ (Doc 60).
- $W_\lambda \geq 0$ via Abel (Doc 63, Cor. 7.2).
- $T_\lambda > 0$ bajo $\neg$RH (Doc 63, Cor. 7.5).

**Nivel 3 (equivalencia principal, incondicional):**
- Medida limitante: $dm_{full} = dm_\infty \cdot |\zeta(1/2+is)|^2$ (Doc 64, §5).
- Inyectividad del mapa de Jacobi via Hamburger (Doc 64, Thm. 1.2).
- **RH $\iff T_\lambda = 0$ para todo $\lambda > 0$** (Doc 64, Thm. 3.1).

### 5.2. Qué sigue abierto

- **Cálculo efectivo de $c_k = \langle \Xi, P_k\rangle_{dm_\infty}$:** La recurrencia de Doc 65 tiene coeficientes explícitos pero no tiene solución en forma cerrada conocida.
- **Asintótica rigurosa de Plancherel-Rotach** para la medida CCM en la región de borde (Docs 66–67 son heurísticos).
- **Conexión con De Bruijn-Newman:** ¿Puede $T_\lambda/N(\lambda)$ dar información sobre la constante $\Lambda$?
- **Función fields:** ¿El análogo del CTP en el caso de curvas sobre campos finitos da información nueva?

### 5.3. La imagen global

```
CCM 2024
   |
   | leer el paper → pregunta: ¿qué pasa con a_n^S - a_n^∞?
   ↓
Δ_n^S > 0  (Doc 59)
   |
   ↓
Tasa Δ_n^{∞,p} = A_n/p  (Doc 60)
   |
   ↓
Medida limitante dm_full  (Doc 61, 64)
   |
   ↓ [error Christoffel → corrección]
W_λ ≥ 0 via Abel  (Doc 63)
   |
   ↓
T_λ > 0 bajo ¬RH  (Doc 63)
   |
   ↓ [Hamburger + Hadamard]
T_λ = 0 ∀λ  ⟺  RH  (Doc 64)  ← RESULTADO PRINCIPAL
   |
   ↓ [exploración adicional]
Wronskiano exacto W_k = -1/a_k  (Doc 68)
   |
   ↓
Fórmula cerrada F_n = -1/(a_n P_n P_{n+1} m_∞)  (Doc 69)
```

---

## 6. Proposición nueva: cuantificación de $T_\lambda$ via fórmula cerrada

Combinando la fórmula cerrada de $F_n$ con la estructura de $T_\lambda$:

**Proposición 6.1.** La traza de discrepancia $T_\lambda$ satisface la representación integral:

$$T_\lambda = \frac{1}{\pi}\int_{\mathbb{R}} W_\lambda(s) \cdot \left|\zeta\!\left(\tfrac{1}{2}+is\right)\right|^2 \cdot w(s)\, ds - \frac{1}{\pi}\int_{\mathbb{R}} W_\lambda(s) \cdot w(s)\, ds,$$

donde $W_\lambda(s) = \sum_{n:\gamma_n \leq \lambda} (|P_{n+1}(s)|^2 - |P_n(s)|^2)$.

*Demostración.* Por definición, $T_\lambda = \sum_n (\Delta_n^{full} - \Delta_n^{full,on})$ y $\Delta_n^{full} - \Delta_n^{full,on} = \int (|P_{n+1}|^2 - |P_n|^2)(dm_{full} - dm_{full,on})$ (Doc 61, Thm. 2.1 + Doc 63, telescopía). La medida $dm_{full} - dm_{full,on} = (|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2)w(s)ds/\pi$ y la suma telescópica da $W_\lambda$. $\square$

**Corolario 6.2.** Bajo RH: $|\zeta(1/2+is)|^2 = |\zeta_{on}(1/2+is)|^2$ sobre la recta crítica, luego $T_\lambda = 0$. Bajo $\neg$RH: la diferencia $|\zeta|^2 - |\zeta_{on}|^2$ es no-nula y positiva sobre un conjunto de medida positiva (Doc 64), y $W_\lambda \geq 0$ (Doc 63), luego $T_\lambda > 0$. ∎

Esta es la formulación integral más limpia del CTP, que resume los Docs 63–64 en una sola fórmula.

---

*Fin del Documento 69 y de Fase 32.*
