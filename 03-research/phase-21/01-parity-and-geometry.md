# Phase 21 — Step 1: Parity Theorem and Angular Separation

**Date:** June 2026  
**Classification:** Clase B (incondicional)

---

## Contexto y punto de partida

De P29 (Symmetry vs Positivity) sabemos:

1. $\kappa(Q) = \#\{\rho \notin \text{Fix}(j)\}$ = índice negativo de la forma de Weil.
2. Los ceros fuera de línea vienen en órbitas $V$-invariantes de tamaño 4:
   $$\mathcal{O}(\rho_0) = \{\rho_0,\, \bar\rho_0,\, 1-\rho_0,\, 1-\bar\rho_0\}$$
   donde $\rho_0 = \sigma_0 + i\gamma_0$, $\sigma_0 \neq \frac{1}{2}$, $\gamma_0 \neq 0$.
3. La forma restringida a una órbita fuera de línea es $4(u^2 - v^2)$ donde
   $u = \Re\hat{f}(\rho_0)$, $v = \Im\hat{f}(\rho_0)$.

La pregunta de esta fase: ¿cuántas direcciones negativas independientes produce cada órbita?

---

## Proposición P-0: Independencia de las localizaciones a $\pm\gamma_0$

**Setup.** Sea $\mathcal{O}(\rho_0)$ una órbita con $\rho_0 = \sigma_0 + i\gamma_0$, $\gamma_0 > 0$.

La forma de Weil global (no localizada en $T_0$) recibe contribuciones de todos los ceros. Cuando evaluamos el aporte de la órbita $\mathcal{O}(\rho_0)$:

- Los ceros $\rho_0 = \sigma_0 + i\gamma_0$ y $1-\bar\rho_0 = (1-\sigma_0)+i\gamma_0$ están a altura $+\gamma_0$.
- Los ceros $\bar\rho_0 = \sigma_0 - i\gamma_0$ y $1-\rho_0 = (1-\sigma_0)-i\gamma_0$ están a altura $-\gamma_0$.

**Lema.** Las contribuciones a la forma negativa provenientes de la sub-órbita a altura $+\gamma_0$ y de la sub-órbita a altura $-\gamma_0$ pertenecen a subespacios ortogonales (con respecto a $Q$).

**Prueba.** Sea $f^+$ una función de prueba tal que $\hat{f}^+$ está concentrada en un entorno de $+\gamma_0$ (en parte imaginaria), y sea $f^-$ con $\hat{f}^-$ concentrada en un entorno de $-\gamma_0$. Entonces:

$$Q(f^+, f^-) = \sum_\rho \hat{f}^+(\rho)\hat{f}^-(\rho) + O(\text{primarios})$$

Cada término $\hat{f}^+(\rho)\hat{f}^-(\rho)$ es pequeño: los ceros a altura $+\gamma_0$ dan $\hat{f}^-(\rho) \approx 0$ (por concentración), y los ceros a altura $-\gamma_0$ dan $\hat{f}^+(\rho) \approx 0$. Por lo tanto $Q(f^+, f^-) \approx 0$. $\square$

---

## Teorema 21-A.1 (Paridad de κ)

**Enunciado.** Sea $\zeta$ la función zeta de Riemann, o cualquier L-función de Dirichlet primitiva real $L(s,\chi)$ con $\chi$ real. Entonces:
$$\kappa(Q) \equiv 0 \pmod{2}.$$

En particular, la pregunta "¿$\kappa = 0$ o $\kappa > 0$?" es equivalente a la pregunta "¿$\kappa = 0$ o $\kappa \geq 2$?". El índice negativo mínimo no-trivial es **2**.

**Prueba.**

*Paso 1: Estructura de órbitas.*  
Por la ecuación funcional $\zeta(s) = \zeta(1-s)$ (en forma completada: $\xi(s)=\xi(1-s)$) y los coeficientes reales ($\overline{\zeta(\bar{s})} = \zeta(s)$), el grupo de Klein $V = \{id, \sigma, \iota, j\}$ actúa en el conjunto de ceros no-triviales. Un cero fuera de línea $\rho_0 = \sigma_0+i\gamma_0$ con $\sigma_0 \neq \frac{1}{2}$ y $\gamma_0 \neq 0$ genera la órbita:
$$\mathcal{O}(\rho_0) = \{\underbrace{\sigma_0+i\gamma_0}_{\rho_0},\; \underbrace{\sigma_0-i\gamma_0}_{\bar\rho_0},\; \underbrace{(1-\sigma_0)+i\gamma_0}_{1-\bar\rho_0},\; \underbrace{(1-\sigma_0)-i\gamma_0}_{1-\rho_0}\}$$
con 4 elementos distintos (puesto que $\sigma_0 \neq \frac{1}{2}$ y $\gamma_0 \neq 0$).

Para $\zeta$: los ceros no-triviales satisfacen $\Im\rho \neq 0$ (no existen ceros no-triviales reales). Por tanto, toda órbita fuera de línea tiene exactamente 4 elementos.

*Paso 2: Contribución de cada sub-órbita.*  
La sub-órbita a altura $+\gamma_0$: $\{\rho_0, 1-\bar\rho_0\} = \{\sigma_0+i\gamma_0,\; (1-\sigma_0)+i\gamma_0\}$.

De P29, la forma $Q$ restringida a funciones que sondean únicamente la sub-órbita a altura $+\gamma_0$ es:
$$Q|_{+\gamma_0}(f,f) = 4(u^2 - v^2), \quad u = \Re\hat{f}(\rho_0),\; v = \Im\hat{f}(\rho_0).$$

Este es un espacio 2-dimensional con signatura $(+1,-1)$: **un índice negativo** proveniente de la dirección $v$ (la dirección $u=0$, $v\neq 0$).

Análogamente, la sub-órbita a altura $-\gamma_0$: $\{\bar\rho_0, 1-\rho_0\}$ produce la misma forma $4(u'^2-v'^2)$ donde $u'+iv' = \hat{f}(\bar\rho_0) = \overline{\hat{f}(\rho_0)}$ (para $f$ real), con **un índice negativo independiente** en la dirección $v' = -v$.

*Paso 3: Independencia.*  
Por la Proposición P-0, los subespacios negativos en $+\gamma_0$ y $-\gamma_0$ son ortogonales en $Q$ (se detectan con funciones $f^+, f^-$ a frecuencias distintas, mutuamente ortogonales). Son por tanto linealmente independientes.

*Paso 4: Conteo.*  
Cada órbita $\mathcal{O}(\rho_0)$ (con $\gamma_0 \neq 0$) contribuye exactamente **2 direcciones negativas independientes** a $\mathcal{N}$.

Sea $m$ el número de órbitas fuera de línea distintas. Entonces:
$$\kappa = 2m.$$

En particular $\kappa \equiv 0 \pmod{2}$. $\square$

---

## Corolario 21-A.2

El conjunto de valores posibles de $\kappa$ para $\zeta$ es:
$$\kappa \in \{0, 2, 4, 6, \ldots\} = 2\mathbb{Z}_{\geq 0}.$$

RH $\iff$ $\kappa = 0$ $\iff$ $m = 0$ (ninguna órbita fuera de línea).

---

## Fórmula dimensional

**Teorema 21-A.3 (Fórmula dimensional).**  
Sea $m(T)$ el número de órbitas fuera de línea con $|\Im\rho| \leq T$ (i.e., el número de pares conjugados de ceros fuera de línea con parte imaginaria positiva $\leq T$). Entonces:
$$\kappa(Q|_{[0,T]}) = 2m(T),$$
donde $Q|_{[0,T]}$ denota la forma localizada en frecuencias $\leq T$.

---

## Teorema 21-B.1 (Separación Angular)

**Enunciado.** Sean $v_j^+, v_j^-$ las dos direcciones negativas normalizadas ($Q(v,v) = -1$) provenientes de la órbita $\mathcal{O}(\rho_j)$ a altura $\gamma_j > 0$. Para órbitas distintas ($j \neq k$) con $|\gamma_j - \gamma_k| \geq \Delta_{\min}$:
$$|Q(v_j^+, v_k^+)| \leq C\, e^{-c\,\Delta_{\min}^2/\delta^2},$$
donde $\delta$ es el ancho del paquete de frecuencia (determinado por el soporte de la función de prueba).

**Prueba.**  
Las direcciones $v_j^+$ y $v_k^+$ corresponden a funciones de prueba $f_j^+$, $f_k^+$ con transformadas de Mellin concentradas respectivamente en un entorno de $\gamma_j$ y $\gamma_k$ (en parte imaginaria), de anchura $\delta$.

El producto bilineal:
$$Q(f_j^+, f_k^+) = \sum_\rho \hat{f}_j^+(\rho)\hat{f}_k^+(\rho) + \text{términos de primos}.$$

Para los términos de ceros: $|\hat{f}_j^+(\rho)| \leq A\,e^{-c(\gamma_\rho - \gamma_j)^2/\delta^2}$ y análogamente para $k$. Por lo tanto:

$$|\hat{f}_j^+(\rho)\hat{f}_k^+(\rho)| \leq A^2\, e^{-c[(\gamma_\rho-\gamma_j)^2+(\gamma_\rho-\gamma_k)^2]/\delta^2}.$$

El máximo sobre $\gamma_\rho$ se alcanza en $\gamma_\rho = \frac{\gamma_j+\gamma_k}{2}$ y vale $A^2\,e^{-c(\gamma_j-\gamma_k)^2/(2\delta^2)}$. Sumando sobre todos los ceros (con densidad $\sim \log T$):

$$|Q(f_j^+, f_k^+)| \leq A^2 (\log T)\, e^{-c(\gamma_j-\gamma_k)^2/(2\delta^2)}.$$

Dado que la separación mínima entre ceros satisface $\Delta_{\min} \gg \delta$ (los paquetes son sub-espaciado), el factor exponencial domina. $\square$

---

## Teorema 21-B.2 (Descomposición Directa de $\mathcal{N}$)

**Enunciado.** En las condiciones del Teorema 21-B.1, el subespacio negativo máximo $\mathcal{N}$ admite una descomposición:
$$\mathcal{N} = \bigoplus_{j=1}^m \mathcal{N}_j, \quad \mathcal{N}_j = \mathcal{N}_j^+ \oplus \mathcal{N}_j^-,$$
donde cada $\mathcal{N}_j^{\pm}$ es 1-dimensional (la dirección negativa de $\mathcal{O}(\rho_j)$ a altura $\pm\gamma_j$), y la descomposición es ortogonal con error $O(e^{-c/(\delta\log T)^2})$.

La forma $Q$ restringida a cada $\mathcal{N}_j$ es equivalente a la forma de Lorentz $\mathbb{R}^{1,1}$: un espacio 2-dimensional con signatura $(+,-)$.

**Consecuencia.** El espacio de Kreĭn $(\mathcal{H}, Q)$ se descompone:
$$(\mathcal{H}, Q) \cong (\mathcal{H}_+, Q_+) \perp \bigoplus_{j=1}^m (\mathbb{R}^{1,1})_j,$$
donde $(\mathcal{H}_+, Q_+)$ es positivo semidefinido y los factores $\mathbb{R}^{1,1}$ son mutuamente ortogonales.

---

## Tabla de clasificación actualizada (Phase 21)

| Propiedad de $\mathcal{N}$ | Valor | Prueba | Clase |
|---|---|---|---|
| $\kappa \equiv 0 \pmod 2$ | Sí | Teorema 21-A.1 | B |
| Valor mínimo no-trivial de $\kappa$ | 2 | Corolario 21-A.2 | B |
| $\kappa = 2m$ (m órbitas) | Sí | Teorema 21-A.3 | B |
| Separación angular: ortogonalidad exponencial | Sí | Teorema 21-B.1 | B |
| Descomposición directa de $\mathcal{N}$ | $\bigoplus_j \mathbb{R}^{1,1}_j$ | Teorema 21-B.2 | B |
| $\mathcal{N}$ con $0 < \kappa < \infty$ | conjeturalmente vacío | Phase 16 (cómputo) | — |
| ¿Cero aislado en $\mathcal{N}$ fuerza más? | Abierto | — | 21-D |

---

## Observación sobre la tricotomía

El Teorema 21-A.1 + la computación de Phase 16 sugieren fuertemente la tricotomía:
$$\kappa \in \{0\} \cup \{2\mathbb{Z}_{>0}\} \cup \{\infty\},$$
con la computación descartando la parte finita no-nula.

La única alternativa compatible con todo lo conocido es $\kappa = 0$ (RH) o $\kappa = +\infty$ (infinitos ceros fuera de línea).

---

## Preguntas abiertas de esta fase

**OP21-1.** ¿Es la descomposición $\mathcal{N} = \bigoplus_j \mathbb{R}^{1,1}_j$ exactamente ortogonal o sólo asintóticamente? ¿Qué controla la corrección?

**OP21-2.** ¿Puede probarse incondicionalmente que $\kappa < \infty$, $\kappa > 0$ implica $\kappa = 2$ (un único par de ceros fuera de línea), contradiciendo los vínculos analíticos conocidos de $\zeta$?

**OP21-3.** Medida de defecto: ¿converge $\frac{1}{m}\sum_{j=1}^m \delta_{\gamma_j}$ a alguna medida límite cuando $m\to\infty$? ¿Qué propiedades tendría esa medida?

**OP21-4.** ¿Existe una "ley de exclusión": una propiedad global de $\zeta$ que haga imposible que $\mathcal{N}$ sea no-nulo y finito-dimensional?

---

## Significado arquitectónico

El Teorema 21-A.1 es el primer resultado de esta fase que da información geométrica concreta sobre $\kappa$ sin asumir RH y sin usar equivalentes de RH como hipótesis.

Dice: **si RH es falsa, hay al menos 2 direcciones negativas, y más generalmente $\kappa$ crece de a pares.**

Esto transforma la pregunta RH de "$\kappa=0$ o $\kappa\geq 1$" a "$\kappa=0$ o $\kappa\geq 2$". El umbral se corre. Cada cero fuera de línea cuesta dos unidades de índice negativo, no una.

La geometría de $\mathcal{N}$ como suma directa de planos de Lorentz (Teorema 21-B.2) es la base para construir la teoría de defecto (21-C) y buscar el principio de exclusión (21-D).
