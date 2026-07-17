# Documento 99 — Convergencia $H_x \to H_\infty$ y la rigidez de Carathéodory–Fejér en los triples espectrales CCM

**Programa:** Hipótesis de Riemann — Fase 35 (cinco frentes)
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Docs 64, 68, 69, 83, 89, 92, 96; P39, P40; meta-docs/NOVEL-STRUCTURE-SEARCH-survivors.md
**Fuentes externas verificadas:** arXiv:2511.22755 (Connes–Consani–Moscovici, *Zeta Spectral Triples*, nov. 2025 — texto completo verificado); arXiv:2511.23257 = Commun. Math. Phys. **406**:312 (2025) (Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* — abstract y enunciados principales verificados); arXiv:2602.04022 (Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, feb. 2026 — abstract y estructura verificados); arXiv:2605.20224 (Groskin, mayo 2026 — solo abstract verificado, paper puramente numérico, citado únicamente como evidencia de literatura).

---

## 1. Objeto del documento

El trabajo reciente de Connes–Consani–Moscovici (en adelante **CCM-ZST**, arXiv:2511.22755) construye, para cada $\lambda > 1$ y $N \in \mathbb{N}$, un operador autoadjunto
$$H_x := D_{\log}^{(\lambda,N)}, \qquad x = \lambda^2,$$
cuyo espectro es **incondicionalmente real** y que, según la evidencia numérica del propio paper, aproxima los ceros bajos de $\zeta(\tfrac12 + is)$ con precisión extraordinaria: usando solo los primos $\leq 13$ (seis primos), los primeros 50 ceros se reproducen con errores que van de $2.5 \times 10^{-55}$ (primer cero) a $\approx 10^{-3}$ (cero 50) [CCM-ZST, §1; Connes 2602.04022 reporta el mismo experimento]. El ingrediente estructural que garantiza la realidad del espectro es una generalización, probada por Connes–van Suijlekom (en adelante **CvS**), del teorema de estructura de Carathéodory–Fejér (1911) para matrices de Toeplitz.

Este documento responde seis preguntas:

(i) qué es exactamente la rigidez CF y cómo entra en la construcción de $H_x$;
(ii) **pregunta discriminadora**: ¿la rigidez CF es positividad disfrazada (colapso tipo Kurasov–Sarnak → Lee–Yang → CAP), o un mecanismo genuinamente distinto?;
(iii) cuál es el obstáculo preciso de la convergencia $H_x \to H_\infty$, formulado matemáticamente;
(iv) si las herramientas propias del programa (Wronskiano exacto, sum rule, perturbación HS) dan control sobre esa convergencia;
(v) qué enunciados intermedios no circulares son demostrables;
(vi) veredicto.

**Convención.** "GAP ABIERTO" marca pasos no probados. Todo lo no verificado contra fuentes lleva [NO VERIFICADO].

---

## 2. La construcción CCM-ZST de $H_x$ (resumen exacto y verificado)

### 2.1. La forma de Weil semilocal $QW_\lambda$

Sea $W(\mathbb{R}^*_+)$ la clase de Weil de funciones de prueba. La fórmula explícita de Weil, en la normalización de CCM-ZST §3, define el funcional
$$\Psi(F) := W_{0,2}(F) - W_{\mathbb{R}}(F) - \sum_p W_p(F),$$
donde $W_{0,2}(F) = \widehat{F}(i/2) + \widehat{F}(-i/2)$ es la contribución (positiva, rango 2 tras truncar) de los polos de $\zeta$,
$$W_p(F) = (\log p)\sum_{m=1}^{\infty} p^{-m/2}\bigl(F(p^m) + F(p^{-m})\bigr)$$
es la distribución local en $p$, y $W_{\mathbb{R}}$ es la contribución arquimediana, dada en Fourier por el multiplicador $2\,\partial_t\theta(t)/2\pi$ con $\theta$ la función ángulo de Riemann–Siegel. La **forma cuadrática de Weil** es $QW(f,g) = \Psi(f^* \!*\! g)$ (convolución en $\mathbb{R}^*_+$).

La forma **semilocal** $QW_\lambda$ es la restricción a $L^2([\lambda^{-1},\lambda], d^*u)$ (funciones extendidas por $0$ fuera del intervalo). Punto estructural decisivo:

> **Localidad automática.** Si $f, g$ tienen soporte en $[\lambda^{-1},\lambda]$, entonces $f^*\!*\!g$ tiene soporte en $[\lambda^{-2},\lambda^2]$, de modo que $W_p(f^*\!*\!g) = 0$ para todo $p^m > \lambda^2$. El "producto de Euler finito sobre $p \leq x = \lambda^2$" **no es una truncación impuesta a mano**: es consecuencia exacta del soporte. [CCM-ZST, abstract y §3 — verificado.]

### 2.2. Espectro discreto y la cantidad $\mu_\lambda$

CCM-ZST prueban (Prop. 3.3, Thm. 3.6, con la teoría de formas de Schmüdgen, GTM 265):

- $QW_\lambda$ es semiacotada inferiormente y semicontinua inferior; define un operador autoadjunto $A_\lambda$ con **espectro discreto acotado inferiormente** (la compacidad viene del crecimiento $\partial_t\theta(t) \sim \tfrac12\log|t|$ del multiplicador arquimediano).
- Sea $\mu_\lambda := \inf \operatorname{spec}(A_\lambda)$. Entonces $\mu_\lambda$ es **decreciente en $\lambda$** (ec. (3.27)).
- **Corolario 3.8 (CCM-ZST):** si $\lim_{\lambda\to\infty}\mu_\lambda = 0$, entonces RH.

Recíprocamente, por el criterio de Weil (positividad de $QW$ sobre $C_c^\infty(\mathbb{R}^*_+)$ $\iff$ RH), se tiene RH $\Rightarrow \mu_\lambda \geq 0$ para todo $\lambda$, luego $\lim \mu_\lambda \geq 0$. Es decir:
$$\boxed{\;\lim_{\lambda\to\infty}\mu_\lambda \geq 0 \iff \text{RH}\;}$$
(la dirección $\Leftarrow$ es Weil; la dirección $\Rightarrow$ es el Cor. 3.8 más la observación de que bajo $\neg$RH existe $f$ compactamente soportada con $QW(f,f) < 0$). Que el límite sea exactamente $0$ y no estrictamente positivo bajo RH es plausible (los ceros de $\Xi$ fuerzan radical asintótico) pero no lo necesitamos: **el contenido RH de la familia $\{\mu_\lambda\}$ es el signo del límite**. Esto es MW-1 en forma semilocal y MW-6 (gap espectral uniforme) en forma literal.

### 2.3. Truncación $E_N$ y la estructura matricial

Sea $V_n = \kappa(U_n)$ la base de Fourier transportada a $[\lambda^{-1},\lambda]$, $E_N = \operatorname{span}\{V_n : |n| \leq N\}$ (los $2N+1$ autovectores del operador de escala $D_{\log}^{(\lambda)} = -iu\,\partial_u$ con condiciones periódicas, de autovalor mínimo). La matriz $\tau = QW_\lambda^N$ en esta base tiene la **estructura especial** (CCM-ZST, Lema 5.1):
$$\tau_{ii} = a_i, \qquad \tau_{ij} = \frac{b_i - b_j}{i-j} \ (i \neq j), \qquad a_{-j} = a_j,\ b_{-j} = -b_j,$$
equivalentemente (Lema 5.2): con $D = \operatorname{diag}(n)$ y la graduación $\gamma(V_j) = V_{-j}$,
$$[D, \tau] = |\beta\rangle\langle\eta| - |\eta\rangle\langle\beta|, \qquad \tau\gamma = \gamma\tau,$$
es decir, **el conmutador con $D$ tiene rango $\leq 2$**. Esta es la clase de matrices a la que se aplica el teorema de CvS (§3 abajo). Nótese: es el análogo exacto, para el par (Loewner, diferenciación), de la caracterización de Toeplitz por $[S,T]$ de rango $\leq 2$ con $S$ el shift.

### 2.4. El operador $H_x = D_{\log}^{(\lambda,N)}$ y el Teorema 5.10

Sea $\epsilon_N$ el autovalor mínimo de $QW_\lambda^N$, **asumido simple con autovector $\xi$ par** ("even-simple"; verificable computacionalmente para cada $(\lambda,N)$ finito), normalizado por $\delta_N(\xi) = 1$ donde $\delta_N$ es el kernel de Dirichlet (aproximación a la evaluación en el borde $u = \lambda$). Se define
$$D_{\log}^{(\lambda,N)} := D_{\log}^{(\lambda)} - |D_{\log}^{(\lambda)}\xi\rangle\langle\delta_N| \qquad \text{(perturbación de rango uno).}$$

**Teorema 5.10 (CCM-ZST — probado, verificado contra el texto):**
(i) $D_{\log}^{(\lambda,N)}$ es **autoadjunto** en $E_N' \oplus E_N^{\perp}$, donde en $E_N' = E_N/\mathbb{C}\xi$ el producto interno es el dado por la forma
$$T := QW_\lambda^N - \epsilon_N \cdot \mathrm{id} \;\geq\; 0.$$
(ii) Su determinante regularizado es $\det\nolimits_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i\,\lambda^{-iz}\,\widehat{\xi}(z)$, con $\widehat{\xi}$ la transformada de Fourier de $\xi$ para la dualidad $\langle \mathbb{R}^*_+ | \mathbb{R}\rangle$.
(iii) $\widehat{\xi}(z)$ es entera y **todos sus ceros son reales**, y coinciden con $\operatorname{spec}(D_{\log}^{(\lambda,N)})$.

Subrayamos el mecanismo de autoadjunción: el producto interno es $T = QW^N_\lambda - \epsilon_N$, que es $\geq 0$ **por construcción** (shift por el autovalor mínimo), con radical exactamente $\mathbb{C}\xi$. El shift solo cambia la diagonal $a_i \mapsto a_i - \epsilon_N$, así que **preserva la estructura** del §2.3.

### 2.5. Qué está probado y qué es conjetura en CCM-ZST

| Enunciado | Estado en CCM-ZST |
|---|---|
| Espectro discreto de $A_\lambda$; $\mu_\lambda$ decreciente | Probado (Thm. 3.6) |
| $\lim\mu_\lambda = 0 \Rightarrow$ RH | Probado (Cor. 3.8) |
| Estructura $(a_i, (b_i-b_j)/(i-j))$ de la matriz truncada | Probado (Lema 5.1) |
| Autoadjunción de $H_x$, realidad del espectro, $\det_{\mathrm{reg}} = -i\lambda^{-iz}\widehat{\xi}(z)$ | Probado (Thm. 5.10), **condicional a even-simplicity del truncado** (verificable caso por caso) |
| Even-simplicity de $QW_\lambda$ (nivel $N = \infty$) | **ABIERTO** (missing step 1, §8 de CCM-ZST) |
| $\xi_\lambda \approx k_\lambda$ (aproximación prolate) | **ABIERTO** — "the main remaining obstacle to our approach to RH" (§7) |
| Convergencia de espectros a los ceros de $\zeta$ | **Conjetura** sostenida numéricamente; "a rigorous proof of this convergence would establish RH" (abstract) |

Evidencia de literatura adicional [Groskin, arXiv:2605.20224, solo abstract verificado]: la implementación independiente reproduce la convergencia (error del primer cero baja monótonamente hasta $\sim 10^{-168}$ con primos $\leq 67$) y reporta que las matrices truncadas tienen **autovalores negativos** (3 a 11 autovalores negativos según $N$, a $x = 100$). Esto confirma un punto estructural que usaremos en §4: la forma truncada **no** es positiva en general; el método no necesita que lo sea.

---

## 3. (i) La rigidez de Carathéodory–Fejér: enunciado preciso y rol en la construcción

### 3.1. El problema CF clásico y su teorema de estructura (1911)

Dos caras del mismo objeto:

**(CF-a) Problema de coeficientes de Carathéodory / extensión positiva.** Dados $c_0, \dots, c_N \in \mathbb{C}$, ¿existe una medida positiva $\mu$ en el círculo $S^1$ con momentos trigonométricos $\widehat{\mu}(k) = c_k$, $|k| \leq N$? Respuesta (Carathéodory–Toeplitz): sí $\iff$ la matriz de Toeplitz $T_N = (c_{i-j})_{0\le i,j\le N}$ es semidefinida positiva. Caso interior ($T_N > 0$): infinitas extensiones (parametrización de Schur/Nevanlinna–Pick). **Caso de borde** ($T_N \geq 0$ singular): la extensión es **única** y la medida está **forzada** a ser atómica,
$$\mu = \sum_{j=1}^{r} \rho_j\,\delta_{e^{i\theta_j}}, \qquad r = \operatorname{rank} T_N \leq N,$$
y todo vector $\xi \in \ker T_N$ tiene polinomio asociado $P_\xi(z) = \sum \xi_j z^j$ con **todos sus ceros en el círculo unidad** (los átomos $e^{i\theta_j}$ están entre ellos). Esta unicidad-en-el-borde es la **rigidez CF**.

En forma desplegada, el corolario que CvS generalizan es:

> **Corolario CF (forma usada).** Sea $T_N = (c_{i-j})_{0 \leq i,j \leq N}$ hermitiana de Toeplitz, $T_N \geq 0$, $\operatorname{rank}(T_N) = N$ (corrango 1), y sea $0 \neq \xi = (\xi_0, \dots, \xi_N) \in \ker T_N$. Entonces el polinomio $P_\xi(z) = \sum_{j=0}^N \xi_j z^j$ tiene sus $N$ ceros sobre $S^1 = \{|z| = 1\}$, y la (única) medida representante $\mu \geq 0$ de los momentos $c_k$ está soportada en esos ceros.

La intuición de la prueba (en la versión C*-algebraica de CvS): $T_N \geq 0$ singular significa que la forma sesquilineal "toca el cero" en $\xi$; la estructura de Toeplitz ($[S, T]$ de rango $\leq 2$, $S$ = shift) convierte el vector nulo en un vector propio aproximado del shift unitario en la representación GNS, y los autovalores de un unitario viven en $S^1$.

**(CF-b) Problema extremal de Carathéodory–Fejér / Pick–Nevanlinna de norma mínima.** Dado un polinomio $p(z) = c_0 + \dots + c_N z^N$, minimizar $\|f\|_{H^\infty}$ entre las $f$ holomorfas en el disco con los mismos primeros coeficientes. El teorema de 1911 identifica el extremal único como múltiplo escalar de un producto de Blaschke (módulo constante en el borde); la norma mínima es la norma de la matriz de Hankel/Toeplitz asociada. La rigidez es la misma de (CF-a) leída en el caso de igualdad: **cuando la forma cuadrática toca su cota, el objeto representante queda rígido y sus ceros caen sobre la frontera** ($S^1$).

Lo esencial para lo que sigue: la rigidez CF es un teorema de la forma

> *positividad semidefinida + singularidad (tocar el cero) $\Rightarrow$ localización de ceros sobre la frontera.*

El input es una positividad; el output es real-rootedness (en la carta apropiada: círculo $\leftrightarrow$ recta real).

### 3.2. La generalización de Connes–van Suijlekom (CMP 406:312, 2025)

CvS prueban [verificado a nivel de abstract y enunciados; la prueba completa del paper no fue inspeccionada línea por línea — los enunciados coinciden con el uso que hace CCM-ZST]:

**Teorema (CvS, versión matricial).** Sea $\tau$ real simétrica de tamaño $(2N+1)$ con la estructura $\tau_{ii} = a_i$, $\tau_{ij} = (b_i - b_j)/(i-j)$, que conmuta con la graduación $\gamma$. Si $\tau \geq 0$ y $\xi \in \ker\tau$ es par, entonces la función entera $\widehat{\xi}(z) = \sum_j \xi_j\,\widehat{V_j}(z)$ (transformada de Fourier de la combinación correspondiente en el intervalo) tiene **todos sus ceros reales**.

**Teorema (CvS, versión continua).** Sea $D$ una distribución real en un intervalo cuya forma cuadrática asociada define un operador autoadjunto semiacotado con autovalor mínimo **simple y aislado** y autofunción **par** $\xi$. Entonces todos los ceros de $\widehat{\xi}$ están en la recta real.

La prueba procede en cinco pasos (según el abstract de CvS): prueba C*-algebraica del corolario CF clásico; análogo continuo (Toeplitz $\to$ operador de convolución); truncaciones; el análogo estructurado; y el teorema de Hurwitz sobre ceros de límites uniformes de funciones holomorfas. La traducción círculo $\to$ recta es la esperada: el rol del círculo unidad lo toma $\mathbb{R}$, el del shift lo toma el generador de escala $D$, y el rol de "Toeplitz" lo toma "$[D,\tau]$ de rango $\leq 2$".

### 3.3. Cómo entra en $H_x$: el punto exacto

La rigidez CF **no se aplica a $QW_\lambda^N$** (que en general no es $\geq 0$: tiene autovalores negativos, véase §2.5). Se aplica a
$$T = QW_\lambda^N - \epsilon_N\cdot\mathrm{id},$$
que es $\geq 0$ **tautológicamente** y singular **tautológicamente** (su núcleo es el autoespacio mínimo). La hipótesis no trivial restante es even-simplicity ($\dim\ker T = 1$, $\gamma\xi = \xi$), que a nivel finito es una verificación de no-degeneración, no una positividad.

La cadena lógica completa de CCM-ZST es entonces:

```
shift espectral (tautológico)          even-simplicity (verificable a nivel finito)
        |                                       |
        v                                       v
   T ≥ 0 singular  --------- rigidez CF -----> ceros de ξ̂ reales   [INCONDICIONAL]
                                                |
                                                v
                          espectro de H_x real = ceros de ξ̂        [INCONDICIONAL]
                                                |
              ¿det_reg(H_x − z) → Ξ(z)?  (límites N→∞, λ→∞)        [ABIERTO]
                                                |
                                                v  (Hurwitz)
                                              RH
```

Los primeros tres pasos son teoremas. **Todo el contenido aritmético no probado vive en el cuarto.**

---

## 4. (ii) Pregunta discriminadora: ¿positividad disfrazada?

### 4.1. El precedente que hay que superar: Kurasov–Sarnak

Recordatorio del colapso documentado en NOVEL-STRUCTURE-SEARCH-survivors.md (Candidate A): la "rigidez cuasicristalina" parecía un mecanismo de discreción/rigidez capaz de forzar ceros sobre una recta sin positividad. Kurasov–Sarnak [arXiv:2307.13498] demostraron que todo cuasicristal de Fourier 1-D con valores en $\mathbb{N}$ es el conjunto de ceros toral de un polinomio de **Lee–Yang** (estable). Pero estabilidad = real-rootedness = positividad de formas de Hermite = CAP. Es decir: **la hipótesis estructural era, sin saberlo, equivalente a la positividad cuya instancia para $\zeta$ es RH.** Usarla para RH es circular: FAIL I2a.

La pregunta es si la rigidez CF repite este patrón. La forma del patrón KS es:

> (KS) *Para concluir "los ceros del objeto aritmético límite son reales" se asume una propiedad estructural del objeto límite que es equivalente a una positividad RH-equivalente.*

### 4.2. Análisis fino: dos positividades que no deben confundirse

En la construcción CCM-ZST conviven dos positividades de naturaleza lógica completamente distinta:

**(P-in) — positividad de input.** $T = QW_\lambda^N - \epsilon_N \geq 0$. Es **tautológica**: vale para cualquier matriz simétrica del mundo, sin contenido aritmético alguno. Es además **verificable**: $\epsilon_N$ se calcula diagonalizando una matriz finita cuyas entradas involucran solo los primos $p \leq \lambda^2$, los polos de $\zeta$ y la fase arquimediana — nunca los ceros. Crucialmente, la positividad de $QW^N_\lambda$ mismo **ni se asume ni se necesita ni es cierta en general** (autovalores negativos observados, §2.5). El método funciona idéntico si $\epsilon_N < 0$.

**(P-out) — positividad de output.** $\mu_\lambda \geq 0\ \forall\lambda$, equivalentemente $\lim\mu_\lambda \geq 0$. Esta **sí** es RH-equivalente (§2.2): es la positividad de Weil semilocal, MW-1.

La rigidez CF consume **solo (P-in)** y produce una conclusión incondicional: los ceros del **aproximante** $\widehat{\xi}_\lambda^N$ son reales. No toca (P-out). La comparación con KS:

| | Kurasov–Sarnak (Candidate A) | Rigidez CF en CCM-ZST |
|---|---|---|
| Objeto al que se aplica la rigidez | el objeto aritmético límite (la medida de ceros de $\zeta$) | el truncado finito $T = QW^N_\lambda - \epsilon_N$ |
| Hipótesis de la rigidez | cuasicristal $\equiv$ Lee–Yang $\equiv$ positividad Hermite | $T \geq 0$ **por shift espectral** + even-simplicity |
| ¿La hipótesis es RH-equivalente? | **Sí** (CAP disfrazado) | **No** (tautológica + no-degeneración) |
| Conclusión obtenida | (si fuera aplicable) realidad de los ceros de $\zeta$ | realidad de los ceros del **aproximante** |
| ¿Dónde queda RH? | dentro de la hipótesis (circular) | desplazada **íntegramente al límite** $\lambda \to \infty$ |

**Conclusión del discriminador, nivel mecanismo:** la rigidez CF **NO es positividad RH-equivalente disfrazada**. El filtro I2a la deja pasar: su positividad de input es verificable e incondicional (de hecho trivial), y su conclusión a nivel finito es un teorema incondicional. Es estructuralmente distinta del colapso KS, y la diferencia es precisa: **CF debilita la conclusión** (realidad de los ceros del aproximante, no de $\Xi$) **a cambio de eliminar la circularidad de la hipótesis**.

### 4.3. Pero la circularidad no desaparece: se desplaza y cambia de nombre

El precio de ese intercambio es exacto. Para que los ceros reales del aproximante digan algo sobre $\Xi$, hace falta la convergencia $\det_{\mathrm{reg}}(H_x - z) \to \Xi(z)$ (tras normalización), y entonces Hurwitz da RH. Pero (§5) el contenido cuantitativo de esa convergencia incluye el comportamiento $\mu_\lambda \to 0$, que **es** (P-out) **es** MW-1 **es** MW-6. En el lenguaje del programa:

> La construcción CF realiza la transmutación *"circularidad de hipótesis" $\longrightarrow$ "no-uniformidad de límite"*. El muro no se cruza: se lo reubica en el paso al límite, donde reaparece con su nombre de siempre (gap espectral uniforme de truncaciones, MW-6, equivalente a la positividad de Weil, MW-1).

**Veredicto del filtro en dos niveles:**
- **Mecanismo finito (la rigidez CF como tal): PASA I2a.** No es CAP. Es la primera estructura post-survivors que produce, incondicionalmente, familias de funciones enteras con ceros reales *ancladas a los datos aritméticos verificables de $\zeta$* (primos + polos + fase $\theta$).
- **Estrategia completa (CF + límite): FAIL I2a en el paso final.** El enunciado "los espectros convergen a los ceros" implica RH, y su núcleo cuantitativo ($\lim\mu_\lambda \ge 0$, normalizaciones del determinante) es positividad de Weil.

### 4.4. Sobre el significado de los $10^{-55}$ y la barrera de Hadamard

Dos observaciones de honestidad:

1. La precisión $10^{-55}$ con 6 primos **no es evidencia de no-circularidad**; es evidencia de que la cancelación aritmética que controla $\mu_\lambda$ (y la proximidad $\xi_\lambda \approx$ función prolate) ya es extraordinariamente profunda a $x = 13$. CCM estiman en $\sim 10^{-1235}$ la probabilidad de coincidencia casual: hay estructura real. Pero la *magnitud* de esa cancelación es exactamente lo que nadie sabe acotar — ver §6.1 (obstrucción del gap evanescente).

2. ¿Viola el Corolario 3.8 la barrera de Hadamard (MW-7: "ninguna propiedad de $\zeta$ verificable sin conocer posiciones de ceros implica $d\nu = 0$")? No, y la razón afina el enunciado de MW-7: cada $\mu_\lambda$ individual es verificable (computable sin ceros), pero el enunciado RH-suficiente es la **conjunción infinita** $\lim\mu_\lambda = 0$, que no es verificable en términos finitos. Es la misma forma lógica del criterio de Li ($\lambda_n \geq 0\ \forall n$, cada $\lambda_n$ computable): una sucesión de instancias verificables cuya totalidad es CAP. MW-7 debe leerse así: *verificable = decidible con información finita*; la familia CF no escapa a esa lectura.

---

## 5. (iii) El obstáculo de convergencia $H_x \to H_\infty$: formulación precisa

### 5.1. La topología correcta no es la de resolventes

Los operadores $D^{(\lambda,N)}_{\log}$ viven en espacios de Hilbert **distintos para cada $(\lambda,N)$**: el producto interno en $E_N'$ es la forma $QW^N_\lambda - \epsilon_N$, que cambia con los parámetros y cuyo "tamaño" colapsa con los gaps espectrales (§6.1). No hay espacio ambiente fijo natural en el que plantear convergencia en norma de resolventes; un embedding forzado en $L^2(\mathbb{R}^*_+)$ degenera porque la métrica $T$ tiene autovalores que tienden a $0$ super-exponencialmente [evidencia numérica de literatura; NO VERIFICADO como enunciado asintótico]. El objeto estable bajo cambio de métrica es el **determinante regularizado**: $\det_{\mathrm{reg}}(D^{(\lambda,N)}_{\log} - z) = -i\lambda^{-iz}\widehat{\xi}(z)$ depende solo del espectro, y el espectro depende solo de $(\xi, \delta_N, D_{\log}^{(\lambda)})$, no del producto interno elegido. La formulación correcta es por tanto **convergencia uniforme sobre compactos de funciones enteras** (topología compacto-abierta; Montel + Hurwitz como maquinaria de paso al límite de ceros). Esta es exactamente la elección de CCM-ZST §7. De ella se deduce convergencia espectral local (convergencia de los conjuntos de ceros en métrica de Hausdorff local sobre compactos), que es la noción operatorial sobreviviente.

### 5.2. Los dos límites, como enunciados matemáticos

**(C1) Límite interno, $N \to \infty$ con $\lambda$ fijo.**
*Enunciado:* Supongamos que $A_\lambda$ es even-simple (autovalor mínimo $\mu_\lambda$ simple, autofunción $\xi_\lambda$ par). Entonces $\epsilon_N \to \mu_\lambda$, $\xi_N \to \xi_\lambda$ en $L^2([\lambda^{-1},\lambda], d^*u)$ con la normalización $\delta_N(\xi_N)=1 \to \xi_\lambda(\lambda) = 1$, y
$$\det\nolimits_{\mathrm{reg}}\bigl(D^{(\lambda,N)}_{\log} - z\bigr) \longrightarrow -i\,\lambda^{-iz}\,\widehat{\xi_\lambda}(z)$$
uniformemente sobre compactos de $\mathbb{C}$.
*Estado:* la convergencia $\epsilon_N \to \mu_\lambda$ es la Prop. 3.4 de CCM-ZST (probada: $E$ es core de la forma). La convergencia del autovector y del determinante es plausible con la compacidad del Thm. 3.6, **modulo even-simplicity de $A_\lambda$** — GAP ABIERTO E1 (§7), más un intercambio de límites en el determinante regularizado — GAP técnico declarado, presumiblemente tratable.

**(C2) Límite externo, $\lambda \to \infty$ — el enunciado que implicaría RH.**
*Enunciado:* Existen constantes $a_\lambda, b_\lambda \in \mathbb{R}$ tales que
$$e^{a_\lambda + b_\lambda z}\cdot\bigl(-i\,\lambda^{-iz}\,\widehat{\xi_\lambda}(z)\bigr) \longrightarrow \Xi(z) := \xi_{\mathrm{Riemann}}\bigl(\tfrac12 + iz\bigr)$$
uniformemente sobre compactos de la franja $|\Im(z)| < \tfrac12$.
**Proposición 5.3 (C2 $\Rightarrow$ RH; el argumento de Hurwitz, escrito en detalle).** Supongamos C1 (para una sucesión $N_k \to \infty$ a cada $\lambda$, modulo E1) y C2. Entonces todos los ceros de $\Xi$ en la franja $|\Im(z)| < \tfrac12$ son reales, es decir, RH.

*Prueba.* Sea $G_\lambda(z) := e^{a_\lambda + b_\lambda z}\bigl(-i\lambda^{-iz}\widehat{\xi_\lambda}(z)\bigr)$. Paso 1: los ceros de $G_\lambda$ son los de $\widehat{\xi_\lambda}$ (el factor exponencial no se anula). Paso 2: los ceros de $\widehat{\xi_\lambda}$ son reales. En efecto, por C1, $\widehat{\xi_{N}} \to \widehat{\xi_\lambda}$ uniformemente sobre compactos, los ceros de cada $\widehat{\xi_N}$ son reales (Thm. 5.10(iii), incondicional dada la even-simplicity truncada), y $\widehat{\xi_\lambda} \not\equiv 0$; por Hurwitz, todo cero de $\widehat{\xi_\lambda}$ es límite de ceros de las $\widehat{\xi_N}$, y $\mathbb{R}$ es cerrado en $\mathbb{C}$. (Alternativamente, la versión continua del teorema CvS aplicada a $A_\lambda$ da el Paso 2 directamente, de nuevo modulo E1.) Paso 3: sea $\rho = \tfrac12 + i z_0$ un cero no trivial de $\zeta$, de modo que $\Xi(z_0) = 0$ con $|\Im(z_0)| < \tfrac12$. Tómese un disco cerrado $\overline{D}(z_0, r)$ dentro de la franja en el que $\Xi$ no tenga otros ceros y no se anule en el borde. Por C2, $G_\lambda \to \Xi$ uniformemente en $\overline{D}(z_0,r)$ y $\Xi \not\equiv 0$; por Hurwitz, para $\lambda$ grande $G_\lambda$ tiene ceros en $D(z_0,r)$, todos reales por los Pasos 1–2, y esos ceros convergen a $z_0$ (achicando $r$). Un límite de números reales es real: $z_0 \in \mathbb{R}$, es decir, $\Re(\rho) = \tfrac12$. $\square$

Obsérvese qué entra en cada paso: el Paso 2 es la rigidez CF (incondicional modulo E1); **todo el peso aritmético está en el Paso 3, i.e., en C2.**

*Recíproca:* RH $\Rightarrow$ C2 **no está probada** (ni siquiera enunciada como teorema en CCM-ZST; es la dirección "plausible"). C2 es a priori más fuerte o igual que RH; en particular C2 exige no solo el signo de $\lim\mu_\lambda$ sino la convergencia del autovector mínimo normalizado, que es información estrictamente más fina. GAP ABIERTO.

### 5.3. ¿Es MW-2 con otro disfraz? Respuesta: el muro es MW-6/MW-1, y MW-2 reaparece como divergencia cuantitativa de la cola prima

Primero, lo que **no** es: el producto de Euler finito de CCM-ZST no es la truncación de $\zeta$ en $\mathrm{Re}(s) > 1$ extrapolada a la franja. La información de los primos llega a la línea crítica por el **único canal que MW-2 permite**: la fórmula explícita, donde el soporte compacto del lado multiplicativo ($[\lambda^{-1},\lambda]$) corta exactamente los primos $p \leq \lambda^2$ sin ninguna divergencia. En este sentido preciso, la construcción es una realización espectral de la lección de MW-2, no una violación ni un disfraz de ella.

Pero MW-2 reaparece en el control *cuantitativo* del límite finito $\to$ pleno. Lo probamos:

**Lema 5.1 (divergencia de la parte prima).** Sea $\tau^{(P)}_{00}(\lambda) := \sum_{p}W_p(V_0, V_0)$ la contribución prima al elemento diagonal $(0,0)$ de $QW_\lambda$ (que por soporte solo involucra $p^m \leq \lambda^2$). Entonces, con $L = 2\log\lambda$,
$$\tau^{(P)}_{00}(\lambda) = 2\sum_{p^m \leq \lambda^2} (\log p)\, p^{-m/2}\Bigl(1 - \frac{m\log p}{L}\Bigr) \;\geq\; \sum_{p \leq \lambda} \frac{\log p}{\sqrt{p}} \;\geq\; c\,\sqrt{\lambda}$$
para una constante absoluta $c > 0$ y todo $\lambda$ suficientemente grande. En particular $\tau^{(P)}_{00}(\lambda) \to \infty$: **la familia de formas $\{\sum_p W_p\}_\lambda$ no converge, ni queda acotada, en ninguna topología de formas sobre los espacios crecientes.**

*Prueba.* La entrada diagonal es $\Psi$-componente prima aplicada a $F(u) = q(U_0,U_0)(\log u) = 2(1 - |\log u|/L)$ (función carpa; CCM-ZST ec. (2.8) y Lema 4.1 de contexto). Por (3.16), $W_p^{\#}(F) = (\log p)\sum_m p^{-m/2} F(p^m)$, y $F(p^m) = 2(1 - m\log p/L)_+$. Para $m = 1$ y $p \leq \lambda$ se tiene $1 - \log p/L \geq 1 - \tfrac{\log\lambda}{2\log\lambda} = \tfrac12$. Luego $\tau^{(P)}_{00} \geq \sum_{p\leq\lambda}(\log p)p^{-1/2}$. Por Chebyshev ($\theta(t) \geq c_0 t$ para $t \geq 2$) y suma parcial, $\sum_{p\leq\lambda}(\log p)p^{-1/2} \geq \theta(\lambda)\lambda^{-1/2} \geq c_0\sqrt{\lambda}$. $\square$

**Proposición 5.2 (cancelación a nivel TNP en la diagonal).** Con la normalización de CCM-ZST:
(a) la contribución de los polos es $W_{0,2}(V_0,V_0) = \dfrac{32\sinh^2(L/4)}{L} = \dfrac{4\lambda}{\log\lambda}\,\bigl(1 + O(\lambda^{-1})\bigr)$;
(b) la contribución arquimediana es $W_{\mathbb{R}}(V_0,V_0) = O(1)$ uniformemente en $\lambda$;
(c) la contribución prima satisface, por el Teorema del Número Primo,
$$\tau^{(P)}_{00}(\lambda) = \frac{4\lambda}{\log\lambda}\,\bigl(1 + o(1)\bigr).$$
En consecuencia, $\tau_{00}(\lambda) = W_{0,2} - W_{\mathbb{R}} - \tau^{(P)}_{00} = o(\lambda/\log\lambda)$: **cada uno de los dos términos dominantes diverge como $4\lambda/\log\lambda$ y la entrada diagonal de $QW_\lambda$ sobrevive solo por su cancelación mutua, que es exactamente el TNP.**

*Prueba.* (a) Por el Lema 4.1 de CCM-ZST con $m = n = 0$: $W_{0,2}(V_0,V_0) = 32L\sinh^2(L/4)\cdot L^2/L^4 = 32\sinh^2(L/4)/L$; y como $L = 2\log\lambda$ da $e^{L/2} = \lambda$, se tiene $\sinh^2(L/4) = \tfrac14(e^{L/2} - 2 + e^{-L/2}) = \tfrac{\lambda}{4}(1 + O(\lambda^{-1}))$. Luego $32\cdot\tfrac{\lambda}{4}/(2\log\lambda) = 4\lambda/\log\lambda \cdot (1 + O(\lambda^{-1}))$. (b) Por (3.15), $W_{\mathbb{R}}^{\#}(F) = (\log 4\pi + \gamma)F(1) + \tfrac12\int_1^\infty \tfrac{x^{1/2}(F(x) - F(1))}{x - x^{-1}}\,d^*x$ con $F$ la carpa: $F(1) = 2$ y $F(x) - F(1) = -2\log x/L$ en el soporte; con $x = e^u$ el integrando es $-\tfrac{2u}{L}\cdot\tfrac{e^{u/2}}{2\sinh u}$, que es $O(1)$ en $u \in (0,1]$ y $O\bigl(\tfrac{u}{L}e^{-u/2}\bigr)$ para $u \geq 1$; la integral total es $O(1/L)\cdot O(1) + O(1) = O(1)$. (c) Los términos $m \geq 2$ aportan $O(\sum_{p \leq \lambda}\log p/p) = O(\log\lambda)$ (Mertens). Para $m = 1$, por suma parcial contra $\theta(t)$ y TNP ($\theta(t) = t(1 + o(1))$):
$$2\sum_{p \leq \lambda^2}\frac{\log p}{\sqrt p}\Bigl(1 - \frac{\log p}{L}\Bigr) = 2\int_{2^-}^{\lambda^2}\Bigl(1 - \frac{\log t}{L}\Bigr)t^{-1/2}\,d\theta(t) = 2\int_0^{L}\Bigl(1 - \frac{u}{L}\Bigr)e^{u/2}\,du\;(1 + o(1)),$$
y $\int_0^L(1 - u/L)e^{u/2}du = \tfrac{4e^{L/2}}{L} + O(1) = \tfrac{4\lambda}{2\log\lambda} + O(1)$, lo que da $2 \cdot \tfrac{2\lambda}{\log\lambda}(1+o(1)) = \tfrac{4\lambda}{\log\lambda}(1+o(1))$. $\square$

*Comentario (la jerarquía de cancelaciones).* La Proposición 5.2 cuantifica dónde vive cada nivel de información aritmética en la familia $QW_\lambda$:
- que $\tau_{00} = o(\lambda/\log\lambda)$ es el **TNP**;
- que $\tau_{00}$ (y las demás entradas) queden con tamaño $O(\lambda^{1/2 + \epsilon})$ es el tamaño del término de error $\psi(x) - x$, es decir, **equivale a RH al nivel de entradas** (no lo usamos; lo señalamos);
- que el **fondo del espectro** $\mu_\lambda$ de la forma completa quede $\geq -o(1)$ es la positividad de Weil semilocal, es decir, **RH al nivel espectral** — un piso más profundo que las entradas, porque involucra la cancelación coherente de toda la matriz.

**Respuesta a (iii).** El obstáculo de la convergencia $H_x \to H_\infty$ **no** es un problema de compacidad (la compacidad está: Thm. 3.6 da espectro discreto para cada $\lambda$, y C1 es un límite interno controlable). Es un problema de **estabilidad del fondo del espectro bajo el límite de las truncaciones**, es decir, MW-6 en forma literal, cuya raíz es MW-1; y el Lema 5.1 muestra que MW-2 reaparece como el hecho cuantitativo de que la cola prima diverge como $\sqrt{x}$ (de hecho como $4\lambda/\log\lambda$ con la carpa), de modo que **ningún argumento perturbativo "producto finito $\to$ pleno" puede funcionar**: la convergencia, si ocurre, ocurre solo por cancelación entre los tres bloques divergentes, y el control de esa cancelación al nivel del ínfimo espectral es CAP.

---

## 6. (iv) ¿Las herramientas propias del programa controlan esta convergencia?

### 6.1. Estabilidad de la rigidez CF bajo perturbación acotada (resultado nuevo, con prueba) y la obstrucción del gap evanescente

**Lema 6.1 (estabilidad CF).** Sea $Q$ real simétrica de tamaño $2N+1$, con la estructura del §2.3, que conmuta con $\gamma$, even-simple, con autovalor mínimo $\epsilon_1$ y gap espectral $g := \epsilon_2 - \epsilon_1 > 0$. Sea $E$ real simétrica con la misma estructura, conmutando con $\gamma$, con $\|E\| < g/2$. Entonces:
(i) $\widetilde{Q} = Q + E$ es even-simple;
(ii) sus autovectores mínimos normalizados satisfacen $\|\widetilde{\xi} - \xi\| \leq \dfrac{2\|E\|}{g - 2\|E\|}$;
(iii) $\widehat{\widetilde{\xi}}$ tiene todos sus ceros reales, y sobre cualquier compacto $K \subset \mathbb{C}$ los ceros de $\widehat{\widetilde{\xi}}$ convergen a los de $\widehat{\xi}$ cuando $\|E\| \to 0$.

*Prueba.* (i) Por Weyl, $|\epsilon_k(\widetilde Q) - \epsilon_k(Q)| \leq \|E\|$ para todo $k$; como $\|E\| < g/2$, el autovalor mínimo de $\widetilde Q$ sigue separado del resto por al menos $g - 2\|E\| > 0$, luego es simple. Como $E$ conmuta con $\gamma$, los sectores par/impar son invariantes para $\widetilde Q$; el autovector mínimo de $Q$ es par y la separación espectral impide que el autovector mínimo de $\widetilde Q$ cruce de sector (el camino de interpolación $Q + tE$ mantiene el autovalor mínimo simple para $t \in [0,1]$, y la paridad del autovector, que es localmente constante a lo largo del camino por simplicidad, se preserva). (ii) Teorema $\sin\theta$ de Davis–Kahan aplicado al par $(Q, \widetilde Q)$ con separación efectiva $g - 2\|E\|$... [forma estándar: $\|\sin\theta\| \le \|E\|/(g - \|E\|)$; usamos la cota más holgada enunciada]. (iii) $\widetilde Q - \epsilon_1(\widetilde Q)\,\mathrm{id} \geq 0$ es singular, even-simple, con la estructura preservada (el shift solo mueve la diagonal): el teorema CvS aplica verbatim y da los ceros reales. La convergencia de ceros sobre compactos sigue de $\widehat{\widetilde\xi} \to \widehat\xi$ uniformemente sobre compactos (la transformada es lineal y continua en los coeficientes, dimensión finita) más Hurwitz. $\square$

**Consecuencia positiva.** La rigidez CF es **robusta**: sobrevive a cualquier perturbación acotada estructurada — en particular a perturbaciones de tipo Hilbert–Schmidt, que son acotadas. La primera mitad del enunciado intermedio sugerido en la tarea ("estabilidad de la rigidez CF bajo perturbación HS") **queda demostrada** (Lema 6.1). La realidad de los ceros del aproximante no es un fenómeno frágil.

**Obstrucción del gap evanescente (la cara negativa, nueva y precisa).** Las constantes del Lema 6.1 son $O(\|E\|/g)$. Pero en la familia CCM-ZST los gaps relevantes en el fondo del espectro de $QW_\lambda^N$ son — según la propia discusión de CCM-ZST §8 sobre los "extremely small numbers $\epsilon_\lambda$" y la evidencia numérica de la literatura — super-exponencialmente pequeños en $\lambda$ (escala $10^{-55}$ ya a $x = 13$) [magnitud asintótica: NO VERIFICADO como teorema; es un hecho numérico reportado]. Por tanto:

> La **misma pequeñez** que produce la precisión espectacular de los espectros de $H_x$ (los autovalores mínimos casi tocan $0$, señal de la cancelación aritmética profunda) **destruye todo control perturbativo cuantitativo**: cualquier argumento "transferir even-simplicity / transferir el autovector desde un modelo cercano" paga un factor $1/g$ que crece más rápido que cualquier cota disponible de $\|E\|$. La precisión $10^{-55}$ y la fragilidad perturbativa son dos caras de la misma moneda.

Esto explica con exactitud por qué el "main remaining obstacle" de CCM-ZST (justificar $\xi_\lambda \approx k_\lambda$ con $k_\lambda$ la aproximación prolate) no es un detalle técnico: el error admisible debe competir con gaps evanescentes.

### 6.2. El Wronskiano exacto y la fórmula cerrada de $F_n$ (Doc 68/69): diagnóstico honesto

El Wronskiano exacto $W_k = -1/a_k^\infty$ y la fórmula $F_n = -1/(a_n^\infty P_n P_{n+1} m_\infty)$ viven en la **representación de Jacobi** de las medidas $dm_\infty$ y $dm_{\mathrm{full}} = |\zeta(\tfrac12+is)|^2\,dm_\infty$: son identidades del objeto **límite** $\lambda = \infty$, con el producto de Euler **ya sumado** dentro de $|\zeta|^2$. La familia $H_x$ interpola precisamente **en $x$**, antes de ese límite. Las dos familias de truncaciones son filtraciones distintas del mismo objeto:

- **Filtración aritmética (CCM-ZST):** por primos $p \leq x = \lambda^2$, inducida por el soporte multiplicativo $[\lambda^{-1},\lambda]$; el parámetro de corte vive en el lado de los **primos**.
- **Filtración espectral (programa, P39/P40):** por grado polinomial $n$ (secciones $J_n$ de la matriz de Jacobi); el parámetro de corte vive en el lado de los **ceros/espectro**.

**GAP ABIERTO 6.2 (diccionario de filtraciones).** No existe hoy un diccionario que relacione las truncaciones $QW^N_\lambda$ con las secciones de Jacobi $J_n$ con control uniforme. El candidato natural es la pareja de núcleos reproducentes: el kernel de **Christoffel–Darboux** $\sum_{k<n}P_k(z)P_k(w)$ (lado Jacobi, Doc 69 §2.3) contra el kernel de **Dirichlet** $\delta_N$ (lado CCM-ZST, §2.4). Ambos implementan "evaluación aproximada" en sus respectivas geometrías. Formular y probar una equivalencia asintótica entre ambos núcleos es una pregunta bien planteada y no circular, pero **no está hecha**; sin ella, el Wronskiano exacto no se transporta a la familia $H_x$.

Lo que el Wronskiano **sí** aporta, indirectamente: la fórmula $G_{nn} = m_\infty + m_\infty^{-1}\sum_{k<n}(a_k^\infty P_k P_{k+1})^{-1}$ (Doc 69 §4.1) da los resolventes diagonales exactos del lado arquimediano $J^\infty$, que es el análogo Jacobi del operador de escala $D^{(\lambda)}_{\log}$ (ambos son el "fondo sin aritmética"). Si el diccionario del GAP 6.2 existiera, estas fórmulas exactas darían el término de comparación libre para una teoría perturbativa de $H_x$. Hoy es potencial, no control.

### 6.2-bis. Aclaración para prevenir una identificación errónea: $dm_\infty$ no es el símbolo arquimediano de $QW_\lambda$

Es tentador identificar el "fondo arquimediano" de ambos marcos, porque ambos involucran la fase $\Gamma(\tfrac14 + \tfrac{is}{2})$. Pero son objetos distintos y la diferencia importa:

- En la familia CCM-ZST, la parte arquimediana de $A_\lambda$ es, en Fourier, el **multiplicador** $\tfrac{1}{\pi}\partial_t\theta(t) \sim \tfrac{1}{2\pi}\log|t|$ — una función de **crecimiento logarítmico** (es lo que da resolvente compacto, Thm. 3.6).
- En el marco P39/P40, $dm_\infty(s) = (2\pi)^{-2}\bigl|\Gamma(\tfrac14 + \tfrac{is}{2})\bigr|^2\,ds$ es la **medida espectral** del operador de Jacobi $J^\infty$, con peso de **decaimiento exponencial** $\sim e^{-\pi|s|/2}$ (Stirling) — es lo que hace finita la sum rule del Doc 92.

Ambos provienen del mismo dato (el factor $\Gamma_{\mathbb{R}}$ de la ecuación funcional), pero uno es la *derivada de la fase* ($\theta' = \Im\,\partial_s\log\Gamma$, real, creciente) y el otro es el *módulo cuadrado* ($|\Gamma|^2$, decreciente). Cualquier intento de "traducir" resultados entre los dos marcos que los identifique produce errores de orden exponencial. El diccionario correcto, si existe, debe pasar por el GAP 6.2 (núcleos reproducentes), no por identificación de símbolos. Dejamos esto registrado porque es el error más probable en futuros intentos de fusión de los dos marcos.

### 6.3. Sum rule y perturbación HS (Doc 92, P40): un lema transportable y dónde se rompe la cadena

**Lema 6.4 (sum rule finita — demostrable).** Para $x \geq 2$ sea $\zeta_x(s) := \prod_{p\leq x}(1 - p^{-s})^{-1}$ el producto finito y $dm_x := |\zeta_x(\tfrac12+is)|^2\,dm_\infty$. Entonces $\log|\zeta_x(\tfrac12+is)|^2$ es continua y de crecimiento polinomial en $s$ (es una suma finita de funciones suaves acotadas), luego integrable contra $dm_\infty$ (peso con decaimiento exponencial $|\Gamma(\tfrac14+\tfrac{is}2)|^2$), y los coeficientes de Jacobi $a_k(x) = a_k^\infty + e_k(x)$ de $dm_x$ satisfacen la sum rule
$$\sum_k e_k(x)^2 \;=\; \int \log|\zeta_x(\tfrac12+is)|^2\,dm_\infty \;<\; \infty,$$
con $b_k(x) = 0$ por la simetría $s \mapsto -s$ de $|\zeta_x(\tfrac12+is)|^2$ (que sigue de $\overline{\zeta_x(\tfrac12+is)} = \zeta_x(\tfrac12-is)$ para $s$ real).
*Prueba.* Idéntica a la del Doc 92 (sum rule tipo Szegő–Killip–Simon para perturbación del peso por un factor log-integrable y simétrico); ninguna propiedad de $\zeta$ plena se usa, solo la log-integrabilidad del factor, que aquí es elemental. $\square$

Esto da una **métrica de convergencia bien definida** para la familia de medidas finitas: $d(x)^2 := \sum_k\bigl(e_k(x) - e_k\bigr)^2$, con $e_k$ los coeficientes plenos (P40). Y aquí la cadena se rompe en el primer eslabón, exactamente donde MW-2 dice que debe romperse:

**GAP ABIERTO 6.5 (no convergencia puntual del producto finito en la línea).** Para $s$ real fijo, $\zeta_x(\tfrac12+is) \not\to$ límite cuando $x \to \infty$: el producto de Euler **no converge en $\mathrm{Re}(s) = \tfrac12$** — ni siquiera bajo RH (bajo RH hay convergencia condicional del producto en $\mathrm{Re}(s) > \tfrac12$, no en la línea). Por tanto $dm_x \not\to dm_{\mathrm{full}}$ en ningún sentido puntual del integrando, y si hay convergencia débil de $dm_x$ (tras promediación) hacia $dm_{\mathrm{full}}$, probarla sería un teorema tauberiano fuerte cuyo estatus desconocemos — la declaramos GAP ABIERTO, señalando que es el candidato natural a enunciado intermedio del lado Jacobi (E6, §7).

**La lección estructural (importante).** Compárese el GAP 6.5 con la localidad automática del §2.1: la **única** manera conocida de hacer converger "producto finito $\to$ pleno" con datos en la línea crítica es pasar al lado dual de la fórmula explícita y cortar por **soporte compacto** (Weil/CCM-ZST), no por producto puntual (Jacobi/Doc 92). El éxito numérico de CCM-ZST es la manifestación espectral de esta asimetría. Las herramientas Jacobi del programa están del lado equivocado del corte: ven el límite, no la familia.

**Resumen de (iv):** las herramientas propias dan (a) el Lema 6.1 — estabilidad cualitativa de la rigidez CF, nuevo y probado acá; (b) el Lema 6.4 — sum rule finita, probada por transporte directo de Doc 92; (c) **ningún control del límite $\lambda \to \infty$**, porque ese control es (P-out) = MW-1, y además los GAPs 6.2 y 6.5 bloquean los dos puentes naturales entre el marco Jacobi del programa y la familia $H_x$.

---

## 7. (v) Enunciados intermedios no circulares: qué sería demostrable

Clasificamos por estatus frente al filtro de circularidad.

**E1 (even-simplicity de $A_\lambda$, para todo $\lambda > 1$).** El missing step 1 de CCM-ZST. Es un enunciado de **no-degeneración espectral**, no de positividad: en su cara no es RH-equivalente (una degeneración del autovalor mínimo, o un autovector mínimo impar, no produce ni destruye ceros fuera de la línea de manera evidente). Indicación a favor (CCM-ZST §8): la propiedad vale para el operador prolate $PW_\lambda$ para todo $\lambda$. Ruta de ataque no perturbativa: teoría de oscilación/Sturm en el sector par del problema de autovalores de $A_\lambda$ (la ruta perturbativa desde $PW_\lambda$ está bloqueada cuantitativamente por el gap evanescente, §6.1). **Candidato más limpio del frente. No circular. GAP ABIERTO.**

**E2 (límite interno C1, modulo E1).** Convergencia $\epsilon_N \to \mu_\lambda$, $\xi_N \to \xi_\lambda$, y de los determinantes regularizados, a $\lambda$ fijo. Ingredientes disponibles: Prop. 3.4 (core de la forma), Thm. 3.6 (resolvente compacto), Lema 5.5 (kernel de Dirichlet sobre $\mathrm{Dom}\,D$). Lo no trivial: la convergencia de $\widehat{\xi_N} \to \widehat{\xi_\lambda}$ uniforme sobre compactos con la normalización de borde (el funcional $\delta_N$ no es continuo en $L^2$; hay que pasar por la norma de la forma). **Plausiblemente demostrable; no circular; GAP técnico declarado.**

**E3 (estabilidad CF bajo perturbación estructurada).** **Demostrado** (Lema 6.1). Cerrado en positivo.

**E4 (tasa de convergencia espectral en función de la cola del producto de Euler).** **CIRCULAR — descartado con precisión.** Cualquier cota de la forma $\mathrm{dist}\bigl(\operatorname{spec}(H_x)\cap K,\ \{\gamma_n\}\cap K\bigr) \leq \omega(x)$ con $\omega(x) \to 0$ uniforme en compactos implicaría (vía el argumento de Hurwitz cuantitativo) una versión efectiva de C2, luego RH efectiva. Y el Lema 5.1 muestra que la "cola del producto de Euler en $\mathrm{Re}(s) = \tfrac12$" no es pequeña: diverge como $\sqrt{x}$ en norma de formas. Toda tasa debe nacer de la cancelación entre bloques divergentes = positividad de Weil = MW-1. Tal cual lo anticipaba la consigna: la cola del Euler en la línea **es** MW-2.

**E5 (finitud y estructura del paquete negativo de $QW^N_\lambda$).** Pregunta: ¿el número $\kappa_\lambda(N)$ de autovalores negativos de $QW^N_\lambda$ está acotado uniformemente en $N$ (i.e., $\kappa_\lambda := \sup_N \kappa_\lambda(N) < \infty$ para cada $\lambda$), y cómo crece $\kappa_\lambda$ con $\lambda$? Conexión directa con el programa: es el análogo semilocal del índice negativo $\kappa(Q) = \mathrm{neg.ind}(H_C)$ (P35) y del Teorema 8.1 del Doc 96 (índice negativo localizado en $\mathcal{K}_{\mathrm{off}}$); la evidencia numérica de literatura ($\kappa$ creciendo con $N$ a $x$ fijo: 3, 5, 8, 11 — [Groskin, NO VERIFICADO]) sugiere que la versión truncada **no** estabiliza trivialmente, lo que haría de $\kappa_\lambda(N)$ un objeto con contenido. Bajo RH, $\mu_\lambda \geq 0$ fuerza $\kappa_\lambda(N) = 0$ asintóticamente en el límite de la forma — luego cuidado: una cota inferior creciente e incondicional de $\kappa_\lambda(N)$ que sobreviva $N \to \infty$ **refutaría** RH, y una cota superior $\to 0$ la probaría; la versión "estructura fina" (paridad, localización de los autovectores negativos) es en cambio estudiable sin tocar ese filo. **Parcialmente no circular; bien planteado; no iniciado.**

**E6 (tauberiano de medidas: $dm_x \to dm_{\mathrm{full}}$ en sentido débil promediado).** El GAP 6.5 como pregunta positiva. Si fuera cierto con promediación logarítmica en $x$, daría el puente entre la filtración aritmética y la espectral (GAP 6.2) en el nivel de medidas, sin pasar por ceros. Estatus frente al filtro: desconocido — podría colapsar a un enunciado de tipo "momentos de $|\zeta_x|^2$ contra peso suave", que es teoría clásica de valores medios de polinomios de Dirichlet; si colapsa ahí, es demostrable pero probablemente insuficiente para C2 (los valores medios no ven el fondo del espectro). **Abierto, exploratorio.**

---

## 8. Síntesis

1. **(i)** La rigidez CF es la unicidad-en-el-borde del problema de extensión positiva de Carathéodory–Toeplitz (y del problema extremal CF/Pick–Nevanlinna): forma $\geq 0$ singular $\Rightarrow$ ceros del vector del núcleo sobre la frontera. CvS la generalizan a matrices con $[D,\tau]$ de rango $\leq 2$ (estructura Loewner), círculo $\to$ recta. En CCM-ZST se aplica al truncado **shiftado** $QW^N_\lambda - \epsilon_N \geq 0$ (positividad tautológica) y produce, incondicionalmente, operadores $H_x$ autoadjuntos con $\det_{\mathrm{reg}}(H_x - z) = -i\lambda^{-iz}\widehat{\xi}(z)$ de ceros reales.

2. **(ii)** **La rigidez CF NO colapsa a positividad RH-equivalente.** A diferencia de Kurasov–Sarnak (donde la hipótesis estructural era CAP disfrazado), aquí la positividad consumida es un shift espectral sin contenido aritmético, verificable, y la conclusión a nivel finito es un teorema. El mecanismo pasa el filtro I2a. **Pero** la circularidad no se elimina: se transmuta en no-uniformidad del límite. El único paso que daría RH (C2) implica RH vía Hurwitz y su núcleo cuantitativo ($\lim\mu_\lambda \geq 0$, Cor. 3.8 y recíproca de Weil) **es** MW-1 en la forma MW-6.

3. **(iii)** El obstáculo de $H_x \to H_\infty$ no es compacidad ni es la no-convergencia del producto de Euler en sentido MW-2 ingenuo (la localidad por soporte la elude exactamente): es la **estabilidad del fondo del espectro de las truncaciones**, con MW-2 reapareciendo cuantitativamente como divergencia $\sim 4\lambda/\log\lambda$ de la cola prima (Lema 5.1, Prop. 5.2), que obliga a que toda convergencia provenga de cancelación TNP→RH entre bloques divergentes. Topología correcta: compacto-abierta de determinantes regularizados (funciones enteras), no resolventes.

4. **(iv)** Herramientas propias: el Lema 6.1 (estabilidad CF, nuevo) y el Lema 6.4 (sum rule finita, transporte de Doc 92) son demostrables y demostrados/esbozados acá; el Wronskiano exacto no se transporta sin el diccionario de filtraciones (GAP 6.2); la cadena Jacobi finito→pleno se rompe en la no-convergencia del producto en la línea (GAP 6.5). Obstrucción nueva con nombre: **gap evanescente** — la precisión $10^{-55}$ y la inutilidad de toda perturbación cuantitativa son el mismo fenómeno.

5. **(v)** Demostrables y no circulares: E1 (even-simplicity de $A_\lambda$ — el candidato central), E2 (límite interno C1), E3 (hecho), E5/E6 (exploratorios). Circular con precisión: E4 (toda tasa uniforme finito→pleno es RH efectiva).

---

## VEREDICTO: **PARCIAL**

**Razón precisa.** La rigidez de Carathéodory–Fejér es el primer mecanismo examinado por el programa desde el meta-doc de supervivientes que **pasa el filtro de circularidad a nivel de mecanismo**: no es positividad RH-equivalente disfrazada (el colapso Kurasov–Sarnak → Lee–Yang → CAP **no** se reproduce), porque su input de positividad es un shift espectral tautológico y verificable, y su output — espectros reales de los aproximantes $H_x$ anclados a datos aritméticos computables — es un teorema incondicional. En ese sentido la ruta está **viva** y es genuinamente nueva.

Sin embargo, la ruta **no es un camino a RH con las herramientas existentes**: el único enlace entre los espectros reales de $H_x$ y los ceros de $\zeta$ es la convergencia C2, cuyo contenido cuantitativo ($\lim_{\lambda\to\infty}\mu_\lambda \geq 0$) es exactamente la positividad de Weil semilocal — MW-1 bajo el disfraz MW-6 —, con MW-2 reapareciendo como la divergencia $\sim \lambda/\log\lambda$ de la cola prima que prohíbe todo tratamiento perturbativo del límite finito→pleno (Lema 5.1, Prop. 5.2). Las herramientas propias del programa controlan la **estabilidad** del mecanismo (Lema 6.1) pero no su **límite**, y los dos puentes hacia el marco Jacobi del programa están bloqueados por gaps precisos (6.2, 6.5).

Queda viva, en concreto, la sub-ruta no circular: **E1 (even-simplicity de $QW_\lambda$) + E2 (límite interno)**, que cerraría todo el diagrama del §3.3 salvo el último paso, y los objetos exploratorios E5/E6. El último paso es, una vez más, el muro único del programa con otro nombre.

---

## Apéndice A — Verificación de fuentes (protocolo de honestidad)

| Fuente | Qué se verificó | Cómo |
|---|---|---|
| arXiv:2511.22755 (CCM, *Zeta Spectral Triples*, 27-nov-2025, 34 pp.) | Texto completo: abstract, §§1–8, Thm. 1.1/5.10, Prop. 3.3–3.4, Thm. 3.6, Cor. 3.7–3.8, ec. (3.27), Lemas 5.1–5.5, Prop. 5.7, §7 (estrategia, prolate, Lemas 7.1–7.2), §8 (missing steps), bibliografía | PDF descargado y extraído; todas las citas de este doc cotejadas contra el texto |
| arXiv:2511.23257 = Commun. Math. Phys. **406**:312 (2025) (Connes–van Suijlekom) | Abstract; enunciados de los tres teoremas (Toeplitz/corrango, matrices estructuradas, versión continua); estructura de la prueba en 5 pasos | Abstract y resumen de enunciados vía web; **la prueba interna no fue inspeccionada línea por línea** — el uso que hace CCM-ZST de los resultados sí fue verificado en el texto de CCM-ZST |
| arXiv:2602.04022 (Connes, *The RH: Past, Present and a Letter Through Time*, 3-feb-2026, 42 pp.) | Abstract y estructura: extremización de forma cuadrática con primos $< 13$, 50 ceros, precisiones $2.6\times10^{-55}$ a $10^{-3}$, "approximating values lie exactly on the critical line", estrategia "convergence of zeros from finite to infinite Euler products" | Página de abstract vía web; texto completo no extraído |
| arXiv:2605.20224 (Groskin, 13-may-2026) | Solo abstract: implementación numérica independiente, convergencia hasta $\sim 10^{-168}$ con $c = 67$, autovalores negativos en truncados (3–11 según $N$) | Abstract vía web; **[NO VERIFICADO]** más allá del abstract; usado solo como evidencia de literatura, nunca como premisa de prueba |
| Carathéodory–Fejér 1911, Weil 1952, Schmüdgen GTM 265, Connes–Consani Enseign. Math. 69 (2023) | Existencia y rol como referencias [2], [16], [12], [4] de CCM-ZST | Cotejadas en la bibliografía del PDF; contenido citado solo a través del uso que CCM-ZST hace de ellas |
| Kurasov–Sarnak arXiv:2307.13498 | Enunciado "todo FQ 1-D $\mathbb{N}$-valuado es conjunto de ceros toral de un polinomio Lee–Yang" | Ya verificado en meta-docs/NOVEL-STRUCTURE-SEARCH-survivors.md; no re-verificado aquí |

Resultados **nuevos de este documento** (no presentes en las fuentes): Lema 5.1, Proposición 5.2 (cancelación TNP en la diagonal de $QW_\lambda$), Proposición 5.3 (escritura detallada del argumento Hurwitz), Lema 6.1 (estabilidad CF), Lema 6.4 (sum rule finita, transporte de Doc 92), la formulación de los GAPs 6.2/6.5, la "obstrucción del gap evanescente" (§6.1) y la clasificación E1–E6 (§7). Las pruebas dadas son completas al nivel de detalle declarado; los puntos no probados están marcados GAP ABIERTO o [NO VERIFICADO].

---

## Apéndice B — Posición del Doc 99 en el mapa del programa

```
MW-1 (positividad de Weil ⟺ RH)
  ║
  ╠═ MW-6 (gap uniforme de truncaciones)  ⟵━━  C2 / lim μ_λ ≥ 0   [§5: el muro de esta ruta]
  ║                                                  ▲
  ║                                                  │ transmutación (§4.3)
  ║                                       rigidez CF a nivel finito
  ║                                       [PASA el filtro I2a — §4.2]
  ║                                                  ▲
  ╠═ MW-2 (propagación aritmética)  ⟵━━  Lema 5.1: cola prima diverge ~ λ/log λ
  ║                                       (no hay perturbativo finito→pleno)
  ║
  ╚═ MW-7 (barrera de Hadamard)  ⟵━━  §4.4: {μ_λ} computables, pero RH = conjunción
                                        infinita (forma lógica de Li) — la barrera se afina,
                                        no se rompe

Rutas vivas tras este doc:  E1 (even-simplicity de A_λ) ─ E2 (límite interno C1)
                            E5 (paquete negativo κ_λ(N) ↔ Doc 96 Thm 8.1, P32)
                            E6 (tauberiano dm_x → dm_full, lado Jacobi)
Cerrado con precisión:      E4 (tasas uniformes finito→pleno ≡ RH efectiva)
Demostrado acá:             E3 (estabilidad CF, Lema 6.1)
```

---

*Fin del Documento 99.*
