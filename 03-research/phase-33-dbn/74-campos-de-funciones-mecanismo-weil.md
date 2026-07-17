# Documento 74 — El mecanismo de Weil: analogía campos de funciones ↔ números

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 64, 70, 71, 72, 73

---

## Resumen

El criterio CTP de este programa establece: RH $\iff T_\lambda = 0$ para todo $\lambda > 0$. En el caso de curvas proyectivas lisas $C/\mathbb{F}_q$, la hipótesis de Riemann es un teorema (Weil 1948). Mostramos que $T_\lambda^C = 0$ se verifica trivialmente como consecuencia directa del teorema de Weil: dado que todos los ceros de $Z_C$ son críticos, la diferencia de medidas es cero. El documento identifica los tres pilares del mecanismo de Weil —Frobenius, dualidad de Poincaré, positividad— y formula la pregunta de importación: ¿qué operador sobre el mundo de números juega el papel del Frobenius?

---

## §1. Función zeta de curvas y la hipótesis de Riemann de Weil

### 1.1. Configuración

Sea $q = p^r$ una potencia de primo, y sea $C$ una curva proyectiva, lisa, geométricamente irreducible definida sobre $\mathbb{F}_q$. Para cada $n \geq 1$, sea $N_n = \#C(\mathbb{F}_{q^n})$ el número de puntos racionales sobre la extensión de grado $n$.

**Definición 1.1 (Función zeta de Weil).** La función zeta de la curva $C/\mathbb{F}_q$ es la serie formal:

$$Z_C(u) = \exp\!\left(\sum_{n=1}^{\infty} N_n \frac{u^n}{n}\right) \in \mathbb{Q}[[u]].$$

**Proposición 1.2 (Weil 1948, racionalidad).** $Z_C(u)$ es una función racional de la forma

$$Z_C(u) = \frac{P_C(u)}{(1-u)(1-qu)},$$

donde $P_C(u) \in \mathbb{Z}[u]$ es un polinomio de grado $2g$, siendo $g = g(C)$ el género de $C$.

*Demostración.* Véase Weil [W48], también Bombieri [B74]. Se utiliza la fórmula de Lefschetz para la extensión de Frobenius. $\square$

**Proposición 1.3 (Ecuación funcional).** $Z_C$ satisface la ecuación funcional:

$$Z_C(1/(qu)) = q^{1-g} u^{2-2g} Z_C(u).$$

En términos de $P_C$: si $\alpha_1, \ldots, \alpha_{2g}$ son las raíces de $P_C$ (contadas con multiplicidad), entonces los $\alpha_j$ se agrupan en pares $\{\alpha_j, q/\alpha_j\}$.

**Teorema 1.4 (Hipótesis de Riemann para curvas, Weil 1948).** Para cada raíz $\alpha_j$ de $P_C(u)$,

$$|\alpha_j| = q^{1/2}.$$

Equivalentemente, los ceros de $Z_C(u)$ (como función meromorfa en $u \in \mathbb{C}$) que provienen de $P_C$ tienen todos módulo exactamente $q^{-1/2}$.

*Observación.* El enunciado usual se formula en términos de la variable $s$ mediante la sustitución $u = q^{-s}$: los ceros de $s \mapsto Z_C(q^{-s})$ satisfacen $\operatorname{Re}(s) = 1/2$, en perfecta analogía con la conjetura de Riemann para $\zeta(s)$.

### 1.2. El polinomio $L_C(u) = P_C(u)$ vía cohomología $\ell$-ádica

Fijemos $\ell \neq p$ un primo. La clave del teorema de Weil es la interpretación cohomológica:

$$P_C(u) = \det\!\bigl(1 - u \cdot \mathrm{Fr}_q \mid H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)\bigr),$$

donde $\mathrm{Fr}_q : \bar{C} \to \bar{C}$ es el morfismo de Frobenius geométrico ($x \mapsto x^q$ en coordenadas afines) y $H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)$ es la primera cohomología étale $\ell$-ádica de la curva base-cambiada a $\overline{\mathbb{F}_q}$.

Las raíces $\alpha_j$ de $P_C$ son precisamente los autovalores del operador $\mathrm{Fr}_q^*$ actuando sobre $H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)$, que es un $\mathbb{Q}_\ell$-espacio vectorial de dimensión $2g$.

---

## §2. La medida espectral $dm_C$ y la traza de discrepancia

### 2.1. Medidas en el formalismo CCM

Recordamos el formalismo de los documentos previos. La medida archimediana es:

$$dm_\infty(s) = (2\pi)^{-2}\,|\Gamma(1/4 + is/2)|^2\,ds,$$

con polinomios ortogonales $\{P_k\}_{k \geq 0}$ (normalizados en $L^2(dm_\infty)$) y coeficientes de Jacobi:

$$a_k^\infty = \tfrac{1}{2}\sqrt{(2k+1)(2k+2)}.$$

El kernel de Abel asociado al parámetro $\lambda > 0$ es:

$$W_\lambda(s) = \sum_{n=0}^{N(\lambda)} (a_n^\infty)^2\bigl(|P_{n+1}(s)|^2 - |P_n(s)|^2\bigr),$$

donde $N(\lambda) = \max\{n : \gamma_n \leq \lambda\}$. Este kernel satisface $W_\lambda(s) \geq 0$ para todo $s \in \mathbb{R}$.

### 2.2. Adaptación al caso de campos de funciones

La función $s \mapsto Z_C(q^{-1/2-is})$ es la traslación de $Z_C$ a la recta crítica (variable $s$ real). Sus ceros en $s$ son exactamente los $s_j$ tales que $q^{-1/2-is_j} = \alpha_j^{-1}$, i.e., $s_j = -\frac{1}{i}(1/2 - \log_q|\alpha_j| + i\arg(\alpha_j)/\log q)$.

**Definición 2.1 (Medida espectral de $C$).** La medida espectral completa asociada a $C$ es:

$$dm_C(s) = dm_\infty(s) \cdot |Z_C(q^{-1/2-is})|^2.$$

Esta medida puede no ser de masa total finita en general; para los propósitos del formalismo CCM nos interesa su cociente con la medida "on-critical" análoga.

**Definición 2.2 (Versión on-critical).** Sea $Z_{C,\text{on}}$ la función obtenida de $Z_C$ reemplazando cada cero $u_j = \alpha_j^{-1}$ de módulo $|u_j|$ por $q^{-1/2} e^{i\arg(u_j)}$ (es decir, proyectando al círculo $|u| = q^{-1/2}$). Definimos:

$$dm_{C,\text{on}}(s) = dm_\infty(s) \cdot |Z_{C,\text{on}}(q^{-1/2-is})|^2.$$

**Definición 2.3 (Traza de discrepancia para $C$).** Para $\lambda > 0$, la traza de discrepancia del modelo de campos de funciones es:

$$T_\lambda^C = \int_{\mathbb{R}} W_\lambda(s)\,\bigl(dm_C(s) - dm_{C,\text{on}}(s)\bigr).$$

---

## §3. $T_\lambda^C = 0$ como consecuencia inmediata del teorema de Weil

### 3.1. El teorema central de esta sección

**Teorema 3.1.** Para toda curva proyectiva lisa $C/\mathbb{F}_q$ y todo $\lambda > 0$,

$$T_\lambda^C = 0.$$

*Demostración.* Por el Teorema 1.4 (hipótesis de Riemann de Weil), todos los ceros de $Z_C(u)$ provenientes de $P_C$ satisfacen $|\alpha_j^{-1}| = q^{-1/2}$. Por tanto, cada cero $u_j = \alpha_j^{-1}$ de $Z_C$ ya se encuentra sobre el círculo $|u| = q^{-1/2}$. La operación de "proyección on-critical" no modifica ningún cero. Luego:

$$Z_{C,\text{on}} = Z_C \quad \text{como funciones meromorfas},$$

de donde $|Z_{C,\text{on}}(q^{-1/2-is})|^2 = |Z_C(q^{-1/2-is})|^2$ para todo $s \in \mathbb{R}$. Esto implica:

$$dm_C(s) = dm_{C,\text{on}}(s) \quad dm_\infty\text{-c.t.p.},$$

y por tanto el integrando de $T_\lambda^C$ es idénticamente cero. La integral es cero para todo $\lambda > 0$. $\square$

### 3.2. Comparación con el caso de números

El criterio CTP del programa establece (Doc 64, Thm. 3.1):

$$\text{RH para } \zeta \iff T_\lambda = 0 \;\text{ para todo } \lambda > 0.$$

El Teorema 3.1 es el análogo exacto con $\zeta$ reemplazada por $Z_C$: la condición $T_\lambda^C = 0$ es equivalente a RH para $C$, y RH para $C$ es un teorema. La diferencia fundamental es que en el caso de números la dirección $\Rightarrow$ (RH $\Rightarrow T_\lambda = 0$) es inmediata y la dirección $\Leftarrow$ también está probada, pero nadie sabe demostrar RH. En el caso de curvas, el trabajo lo hace el Teorema de Weil.

---

## §4. El mecanismo: Frobenius, dualidad de Poincaré, positividad

El Teorema de Weil no es trivial. Su demostración (completada por Weil y clarificada por Grothendieck-Deligne) reposa sobre tres pilares. Los identificamos con precisión porque buscaremos su análogo en el mundo de números.

### 4.1. Pilar I: El operador de Frobenius

**Definición 4.1.** El morfismo de Frobenius geométrico $\mathrm{Fr}_q : \bar{C} \to \bar{C}$ actúa sobre la cohomología $\ell$-ádica:

$$\mathrm{Fr}_q^* : H^i_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \to H^i_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell), \quad i = 0, 1, 2.$$

Los ceros de $Z_C$ son los recíprocos de los autovalores del operador $\mathrm{Fr}_q^*|_{H^1}$.

**Punto crucial:** Los autovalores del Frobenius son algebraicos y sus módulos son accesibles porque $\mathrm{Fr}_q$ es un operador *concreto y definido* sobre un espacio cohomológico de dimensión finita $2g$. El problema de Riemann es que no existe un operador análogo definido para $\zeta$.

### 4.2. Pilar II: La dualidad de Poincaré

Sobre la curva $C$ de dimensión $1$ (curva proyectiva), la dualidad de Poincaré proporciona un emparejamiento perfecto:

$$H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \times H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \to H^2_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell(-1).$$

En términos de autovalores: si $\alpha$ es autovalor de $\mathrm{Fr}_q^*|_{H^1}$, entonces $q/\alpha$ también lo es. Esto empareja los autovalores en pares $(\alpha, q/\alpha)$ bajo la involución $\alpha \mapsto q/\alpha$.

**Consecuencia para los módulos:** Si $|\alpha| = r$, entonces $|q/\alpha| = q/r$. Para que el par $\{\alpha, q/\alpha\}$ sea consistente con la ecuación funcional (que fuerza la simetría $u \mapsto 1/(qu)$), se necesita que el producto de módulos sea $r \cdot (q/r) = q$. Esto no fuerza aún $r = q^{1/2}$; la dualidad impone la simetría funcional pero no la positividad.

### 4.3. Pilar III: La positividad (el argumento decisivo)

La positividad es el corazón del argumento. Existen dos aproximaciones:

**Aproximación de Weil (1948):** Weil utilizó la teoría de correspondencias en la variedad producto $C \times C$ sobre $\mathbb{F}_q$. La forma de intersección sobre divisores de $C \times C$ es positiva definida en cierto sentido (la desigualdad de Castelnuovo-Severi), y esto fuerza $|\alpha_j| = q^{1/2}$.

Concretamente, sea $\Gamma \subset C \times C$ el grafo del Frobenius. La autointersección $(\Gamma \cdot \Gamma)$ es $q + 2 - N_1$, y la desigualdad de Hodge implica:

$$N_1 \leq q + 1 + 2g\sqrt{q},$$

que a su vez implica que los $\alpha_j$ no pueden tener $|\alpha_j| > q^{1/2}$ ni $|\alpha_j| < q^{1/2}$ (usando la ecuación funcional para las dos direcciones).

**Aproximación de Deligne (1974, Weil II):** Para variedades de dimensión superior, Deligne probó la pureza de los autovalores del Frobenius usando la teoría de haces perversos y el teorema de Lefschetz difícil. El argumento de positividad se convierte en el de la positividad de la forma de intersección en cohomología primitiva.

**Proposición 4.2 (Positividad fuerza criticidad).** Sea $V = H^1_{\text{ét}}(\bar{C}, \mathbb{Q}_\ell)$ con la forma bilineal $\langle \cdot, \cdot \rangle$ inducida por la dualidad de Poincaré y el emparejamiento de Weil. Entonces $\langle v, \mathrm{Fr}_q^* v\rangle > 0$ para todo $v \neq 0$ (en una versión apropiada sobre $\mathbb{R}$), y esto implica $|\alpha_j| = q^{1/2}$.

*Esquema de demostración.* La positividad de la forma $v \mapsto \langle v, \mathrm{Fr}_q^* v \rangle$ (esencialmente la positividad del número de intersección $(\Gamma \cdot {}^t\Gamma)$ en $C \times C$, donde ${}^t\Gamma$ es el grafo del Frobenius transpuesto) junto con la dualidad $\alpha \mapsto q/\alpha$ fuerza que todos los autovalores estén en el círculo unitario rescalado $|\alpha| = q^{1/2}$. Si existiera $|\alpha| < q^{1/2}$, por la dualidad existiría $|q/\alpha| > q^{1/2}$, y la forma cuadrática asociada tendría signo indefinido, contradiciendo la positividad. $\square$

### 4.4. Síntesis del mecanismo

El mecanismo de Weil puede resumirse en el diagrama lógico:

$$\underbrace{\text{Frobenius concreto sobre }H^1}_{\text{Pilar I}} + \underbrace{\text{Dualidad de Poincaré}}_{\text{Pilar II}} + \underbrace{\text{Positividad de la intersección}}_{\text{Pilar III}} \implies |\alpha_j| = q^{1/2} \implies T_\lambda^C = 0.$$

La pregunta de importación al caso de números es: ¿existe un análogo de cada uno de estos tres pilares para la función zeta de Riemann?

---

## §5. La pregunta de importación al caso de números

### 5.1. El problema de Hilbert-Pólya

**Conjetura 5.1 (Hilbert-Pólya).** Existe un operador autoadjunto $H$ actuando sobre algún espacio de Hilbert $\mathcal{H}$ tal que el espectro de $H$ es el conjunto $\{t_n\}$ de las partes imaginarias de los ceros de $\zeta(1/2 + it)$.

Si la conjetura de Hilbert-Pólya fuera verdad, la autoadjunción de $H$ forzaría que los $t_n$ son reales, es decir, que los ceros de $\zeta$ están sobre la recta crítica. Esto sería el análogo del Pilar I (Frobenius = operador concreto con autovalores = ceros) más una versión del Pilar III (autoadjunción = positividad).

### 5.2. El formalismo CCM como candidato

El programa CCM (Connes-Consani-Moscovici 2024) propone el operador de Jacobi $J^{full}$ actuando sobre $\ell^2(\mathbb{N})$ como candidato natural para el operador de Hilbert-Pólya.

**Definición 5.2 (Operador de Jacobi completo).** Dado los polinomios ortogonales $\{Q_k\}$ asociados a la medida $dm_{full}(s) = dm_\infty(s) \cdot |\zeta(1/2+is)|^2$, el operador de Jacobi $J^{full}$ es el operador tridiagonal simétrico:

$$J^{full} e_k = a_k^{full} e_{k+1} + b_k^{full} e_k + a_{k-1}^{full} e_{k-1},$$

donde $a_k^{full}, b_k^{full}$ son los coeficientes de Jacobi de la medida $dm_{full}$.

El operador $J^\infty$ correspondiente a $dm_\infty$ tiene coeficientes $a_k^\infty = \frac{1}{2}\sqrt{(2k+1)(2k+2)}$ exactos (de la representación metaplética).

**Observación 5.3.** El operador $J^{full}$ está completamente determinado por el espectro de $\zeta$ (todos los ceros de $\zeta$ están codificados en $dm_{full}$ vía el producto de Hadamard), y formalmente sus autovalores generalizados deberían estar relacionados con el soporte espectral de $dm_{full}$.

### 5.3. El análogo del Frobenius

En el mundo de curvas, el Frobenius $\mathrm{Fr}_q$ es el morfismo "elevar a la $q$-potencia", que es un endomorfismo definido geométricamente. En el mundo de números, el análogo más cercano es el operador de desplazamiento aritmético. Los candidatos en la literatura son:

1. **El operador de Connes (1999):** Un operador sobre el espacio de adeles que actúa como multiplicación por valores del idele de la clase, y cuyo espectro está relacionado con los ceros de $\zeta$ vía la fórmula de trazas de Weil. El "tiempo" adélico hace el papel del Frobenius.

2. **El laplaciano de Pólya-Hilbert (Odlyzko-Schönhage-Berry-Keating):** El operador $H = -d^2/dx^2 + x^2$ desplazado, cuyo espectro aproxima la distribución local de los ceros de $\zeta$ pero no los ceros exactos.

3. **El operador de Jacobi $J^{full}$ (programa CCM):** El operador tridiagonal mencionado en Definición 5.2, que codifica toda la información espectral de $\zeta$.

**Cuestión abierta 5.4.** ¿Existe un operador $\Phi$ sobre un espacio cohomológico bien definido tal que:
- Los autovalores de $\Phi$ son exactamente los $e^{it_n}$ (o directamente los $t_n$)?
- Existe una forma bilineal $\langle \cdot, \cdot \rangle$ sobre dicho espacio que satisfaga un análogo de la dualidad de Poincaré?
- La positividad de $\langle v, \Phi v \rangle$ fuerza que los autovalores de $\Phi$ estén sobre el círculo unitario (equivalente a RH)?

---

## §6. ¿Existe un operador de Frobenius en el mundo CCM?

### 6.1. Reformulación en términos de coeficientes de Jacobi

El formalismo CCM traduce la pregunta del Frobenius a una pregunta sobre los coeficientes de Jacobi. Esto se establece así:

**Proposición 6.1.** La condición $T_\lambda = 0$ para todo $\lambda > 0$ es equivalente a:

$$dm_{full} = dm_{full,on} \quad \text{como medidas en } \mathbb{R},$$

que a su vez (por unicidad de los coeficientes de Jacobi) es equivalente a:

$$a_k^{full} = a_k^{full,on} \quad \text{para todo } k \geq 0.$$

*Demostración.* Dos medidas tienen los mismos polinomios ortogonales (y por tanto los mismos coeficientes de Jacobi) si y solo si son iguales como medidas (teorema de unicidad de la medida espectral para operadores de Jacobi simétricos). La equivalencia con $T_\lambda = 0$ para todo $\lambda$ proviene del Teorema 3.1 de Doc 64. $\square$

**Corolario 6.2.** RH es equivalente a la igualdad de coeficientes de Jacobi:

$$\text{RH} \iff a_k^{full} = a_k^{full,on} \quad \forall k \geq 0.$$

### 6.2. La positividad en el mundo CCM

El análogo del Pilar III (positividad de la forma de intersección) debería ser una afirmación sobre el operador de Jacobi. Identificamos la formulación natural:

**Definición 6.3 (Forma cuadrática de Jacobi).** Sea $J = J^{full}$ el operador de Jacobi de $dm_{full}$, con coeficientes $a_k^{full}, b_k^{full}$. Definimos la forma cuadrática:

$$Q_{J}(v) = \langle v, J v \rangle_{\ell^2} = \sum_{k \geq 0} b_k^{full} |v_k|^2 + 2\sum_{k \geq 0} a_k^{full} \operatorname{Re}(v_k \bar{v}_{k+1}).$$

Si $J$ fuera el análogo del Frobenius, la condición de positividad sería: $Q_J(v) > 0$ para todo $v \neq 0$ en un espacio apropiado.

**Observación 6.4.** En el caso de campos de funciones, la positividad de $\langle v, \mathrm{Fr}_q^* v \rangle$ proviene de la interpretación geométrica (número de puntos de la curva, que es un entero no negativo). En el mundo de números, la positividad análoga tendría que provenir de una propiedad intrínseca de $dm_{full}$, como la completa monotonicidad o la positividad de ciertos determinantes de Hankel.

### 6.3. El análogo de la dualidad de Poincaré

En el caso de curvas, la dualidad de Poincaré se manifiesta como la simetría $\alpha \mapsto q/\alpha$ de los autovalores del Frobenius. En el caso de $\zeta$, la ecuación funcional $\xi(s) = \xi(1-s)$ (donde $\xi(s) = s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$) impone la simetría:

$$\rho \text{ es cero de } \zeta \implies 1-\rho \text{ es cero de } \zeta.$$

Esto es el análogo de $\alpha \mapsto q/\alpha$ bajo la correspondencia $\alpha = q^{1-\rho}$.

**Proposición 6.5 (Dualidad CCM).** La ecuación funcional de $\xi$ induce sobre los coeficientes de Jacobi de $dm_{full}$ la simetría:

$$b_k^{full} = 0 \quad \text{para todo } k \geq 0$$

(los coeficientes diagonales son nulos), pues la medida $dm_{full}$ es simétrica: $dm_{full}(-s) = dm_{full}(s)$.

*Demostración.* La simetría $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$ (que sigue de la ecuación funcional) implica que $dm_{full}$ es una medida par en $s$. Los polinomios ortogonales de una medida par son alternadamente pares e impares, lo que fuerza $b_k = 0$ para todo $k$. $\square$

**Corolario 6.6.** Los coeficientes de Jacobi de $dm_{full}$ se reducen a los coeficientes fuera de diagonal $\{a_k^{full}\}_{k \geq 0}$. La condición RH $\iff a_k^{full} = a_k^{full,on}$ involucra solo esta familia.

### 6.4. La pregunta concreta

Los tres pilares del mecanismo de Weil se traducen al mundo CCM de la siguiente manera:

| Pilar (curvas) | Objeto (curvas) | Análogo propuesto (números, CCM) |
|---|---|---|
| Frobenius | $\mathrm{Fr}_q^* : H^1 \to H^1$ | Operador de Jacobi $J^{full}$ sobre $\ell^2(\mathbb{N})$ |
| Dualidad de Poincaré | Simetría $\alpha \mapsto q/\alpha$ | Ecuación funcional $\rho \mapsto 1-\rho$ (Prop. 6.5) |
| Positividad | $\langle v, \mathrm{Fr}_q^* v \rangle > 0$ | $a_k^{full} > 0$ y ¿alguna desigualdad de tipo Turán? |

La pregunta concreta que emerge es:

**Cuestión abierta 6.7 (El análogo del argumento de positividad).** ¿Existe una propiedad de positividad intrínseca de los coeficientes $a_k^{full}$ (análoga a la positividad de la forma de intersección de Weil) que implique $a_k^{full} = a_k^{full,on}$ para todo $k$?

Una formulación más precisa: en el caso de curvas, la positividad dice que el número de puntos $N_n = \#C(\mathbb{F}_{q^n})$ es un entero no negativo. En el caso de números, los análogos de $N_n$ son los coeficientes aritméticos $\sum_{m \leq x} \Lambda(m)$ (función de von Mangoldt integrada), que son positivos pero cuya positividad no fuerza directamente RH.

---

## §7. Conclusiones y conjeturas

### 7.1. Lo que está demostrado

**Resumen de resultados probados en este documento:**

1. (Teorema 3.1) Para toda curva $C/\mathbb{F}_q$, $T_\lambda^C = 0$ para todo $\lambda > 0$, como consecuencia directa del Teorema de Weil.

2. (Proposición 6.1) En el caso de números, $T_\lambda = 0$ para todo $\lambda \iff a_k^{full} = a_k^{full,on}$ para todo $k$.

3. (Proposición 6.5) Los coeficientes diagonales $b_k^{full} = 0$ para todo $k$ (consecuencia de la ecuación funcional). RH se reduce a la igualdad de los coeficientes $a_k^{full}$.

### 7.2. El obstáculo fundamental

La diferencia cualitativa entre el caso de curvas y el caso de números es la siguiente:

**En el caso de curvas:** El Frobenius $\mathrm{Fr}_q$ es un operador explícito (elevación a la $q$-potencia) actuando sobre un espacio de dimensión *finita* $2g$. La positividad de la forma de intersección es una afirmación sobre un número finito de autovalores, y puede establecerse mediante cuentas algebraicas en la variedad $C \times C$.

**En el caso de números:** No existe un operador explícito sobre un espacio de dimensión finita cuyos autovalores sean los ceros de $\zeta$. El espacio de Hilbert natural ($L^2$ de algún espacio de adeles o el espacio de Jacobi $\ell^2(\mathbb{N})$) es de dimensión infinita, y la positividad de la forma cuadrática correspondiente no es evidente.

### 7.3. Conjeturas para la fase siguiente

**Conjetura 7.1 (Frobenius aritmético).** Existe un operador $\Phi_{ar}$ sobre un espacio de Hilbert $\mathcal{H}_{ar}$ (a definir) con las propiedades siguientes:
- $\mathrm{spec}(\Phi_{ar}) = \{e^{it_n} : t_n \in \mathbb{R},\; \zeta(1/2+it_n) = 0\}$.
- Existe una forma bilineal $\langle \cdot, \cdot \rangle_{ar}$ sobre $\mathcal{H}_{ar}$ que es el análogo de la dualidad de Poincaré, consistente con la ecuación funcional de $\xi$.
- La positividad de $v \mapsto \langle v, \Phi_{ar} v \rangle_{ar}$ implica que $\mathrm{spec}(\Phi_{ar}) \subset S^1$, equivalente a RH.

**Conjetura 7.2 (Identificación CCM).** El operador de Jacobi $J^{full,on}$ (asociado a $dm_{full,on}$) es el candidato natural para el operador de Frobenius aritmético de la Conjetura 7.1. Más precisamente:
- El espacio de Hilbert es $\ell^2(\mathbb{N})$.
- La forma bilineal es $\langle e_j, e_k \rangle_{ar} = \delta_{j+k, 2K}$ para algún $K$ (que implementa la simetría $j \leftrightarrow 2K-j$ análoga a $\rho \leftrightarrow 1-\rho$).
- La condición de positividad se traduce en $a_k^{full,on} > a_k^\infty$ para todo $k$ (hipótesis de crecimiento de coeficientes de Jacobi bajo el efecto de los ceros de $\zeta$).

**Conjetura 7.3 (Criterio de positividad de Jacobi).** La condición $a_k^{full} = a_k^{full,on}$ para todo $k$ es equivalente a la siguiente afirmación de positividad: para todo $N \geq 1$ y todo vector finito $v = (v_0, \ldots, v_N) \in \mathbb{R}^{N+1}$,

$$\sum_{j,k=0}^{N} v_j v_k \int_{\mathbb{R}} Q_j(s) Q_k(s)\, dm_{full}(s) \geq 0,$$

donde $\{Q_k\}$ son los polinomios de $dm_{full,on}$. Esta afirmación es la positividad del "operador de comparación" entre las dos medidas, y sería el análogo directo de la positividad de la forma de intersección de Weil.

### 7.4. La lección de la analogía

La analogía campos de funciones / números, vista a través del cristal CCM, sugiere que el obstáculo para probar RH no es tanto la falta de una fórmula adecuada (el criterio $T_\lambda = 0$ ya existe), sino la falta de un objeto geométrico concreto (el Frobenius) cuya mera existencia y propiedades formales (dualidad + positividad) fuercen la criticidad de los ceros.

El programa para la Fase 34 es por tanto: identificar si los coeficientes $a_k^{full}$ satisfacen alguna desigualdad de tipo "positividad" que pueda establecerse sin asumir RH, y que a su vez fuerce $T_\lambda = 0$.

---

## Referencias

- [W48] A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*, Hermann, Paris, 1948.
- [B74] E. Bombieri, *Counting points on curves over finite fields (d'après S. A. Stepanov)*, Séminaire Bourbaki, 1974.
- [D74] P. Deligne, *La conjecture de Weil I*, Publ. Math. IHÉS 43 (1974), 273–307.
- [C99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999), 29–106.
- [CCM24] A. Connes, C. Consani, H. Moscovici, *Spectral triples and zeta functions*, preprint, 2024.
- [Docs 64, 70–73] Documentos internos del programa, Fase 32–33.

---

*Fin del Documento 74.*
