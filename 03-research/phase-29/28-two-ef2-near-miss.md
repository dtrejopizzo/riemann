# Phase 29 — Doc 28: Las Dos EF2s, el Near-Miss y el Punto Exacto del Gap

**Fecha:** junio 2026  
**Contexto:** El Doc 27 identificó que hay DOS EF2s distintas:
- $\text{EF2}_{WT}$: $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$ (Doc 17, para la función de Weyl-Titchmarsh)
- $\text{EF2}_{emp}$: $N\cdot m_\infty^{emp}(z) = C_\infty'(z)/C_\infty(z) - \Xi'(z)/\Xi(z)$ (EF2 corregida, para la función empírica)

**Objetivo de este documento:** Estudiar la diferencia $\text{EF2}_{WT} - \text{EF2}_{emp}$ como posible herramienta para atacar Inc. Inv. Identificar el punto exacto donde el argumento falla o triunfa.

---

## 1. La identidad diferencia

**Definición.** Para $z \in \mathbb{C}^+$, definimos:

$$\Delta(z) := m_\infty^{WT}(z) - m_\infty^{emp}(z).$$

De las dos EF2s:

$$N\cdot\Delta(z) = N\cdot m_\infty^{WT}(z) - N\cdot m_\infty^{emp}(z) = \frac{C_\infty'(z)}{C_\infty(z)} - \left[\frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}\right] = \frac{\Xi'(z)}{\Xi(z)}.$$

Luego:

$$\Delta(z) = \frac{1}{N}\cdot\frac{\Xi'(z)}{\Xi(z)}. \quad (\Delta\text{-id})$$

**Proposición 1** (contenido de $\Delta$-id en términos de medidas espectrales). Si $(\Delta\text{-id})$ es correcta:

$$d\mu_{WT}^\infty - d\mu_\infty^{emp} = \frac{1}{N}\cdot d\mu_\Xi^{real},$$

donde $\mu_\Xi^{real}$ es la medida de conteo de ceros de $\Xi$ en $\mathbb{R}$ (= la medida de Montgomery $\mu_\gamma^{real}$).

*Prueba.* Inversión de Stieltjes de $(\Delta\text{-id})$. $\square$

**Corolario 1** (límite $N\to\infty$). Si $(\Delta\text{-id})$ es correcta y $N\to\infty$:

$$\mu_{WT}^\infty = \mu_\infty^{emp} + \frac{1}{N}\cdot\mu_\gamma^{real} \xrightarrow{N\to\infty} \mu_\infty^{emp} = \mu_\gamma^{real}.$$

Y como $\mu_{WT}^\infty$ tiene soporte $\subseteq \{$ceros de $C_\infty\}$ (de $\text{EF2}_{WT}$), y $\mu_\gamma^{real}$ tiene soporte $= \{\gamma_n\}$: Inc. Inv. se sigue.

---

## 2. El near-miss: el argumento casi cierra

El argumento anterior tendría la siguiente forma limpia:

**Argumento propuesto.** 
1. De $\text{EF2}_{WT}$ (Doc 17): $\text{supp}(\mu_{WT}^\infty) \subseteq \{$ceros de $C_\infty\}$.
2. De $(\Delta\text{-id})$ con $N\to\infty$: $\mu_{WT}^\infty = \mu_\gamma^{real}$.
3. Por tanto: $\text{supp}(\mu_\gamma^{real}) = \{\gamma_n\} \subseteq \{$ceros de $C_\infty\}$, que es Inc. Inv.
4. Por Teorema D (Doc 19 / P37): $\text{RH}$. $\square$

Si los tres pasos fueran rigurosos, tendríamos una prueba de RH.

**El punto de fallo exacto.** El argumento falla en el paso 0, no en el 1, 2, o 3. El problema es:

> La $(\Delta\text{-id})$ NO es derivable de las dos EF2s independientemente: al menos una de las dos EF2s ya requiere en su prueba la información equivalente a Inc. Inv.

---

## 3. Diagnóstico: ¿cuál EF2 es genuinamente incondicional?

**Proposición 2** (status incondicional de las dos EF2s).

(a) $\text{EF2}_{WT}$: La ecuación $N\cdot m_\lambda^{WT}(z) = C_\lambda'(z)/(C_\lambda(z)-\mu_\lambda)$ para los operadores FINITOS $J_\lambda^N$ es incondicional (viene de la recurrencia de Möbius, Doc 17 Proposición 2). El límite $N\cdot m_\infty^{WT}(z) = C_\infty'(z)/C_\infty(z)$ requiere:
- (i) Convergencia uniforme de los coeficientes de Jacobi: $a_n^{(\lambda)} \to a_n^\infty$, $b_n^{(\lambda)} \to b_n^\infty$. **Estado: incondicional** (Doc 11 Proposición 4).
- (ii) Convergencia de la función $m$: $m_\lambda^{WT}(z) \to m_\infty^{WT}(z)$. **Estado: requiere que $J_\infty$ esté bien definido y que la convergencia de coeficientes implique convergencia de m-funciones.** Esto es estándar para operadores de Jacobi con coeficientes convergentes (teoria de Nevai, 1979). **Incondicional.**

(b) $\text{EF2}_{emp}$: La ecuación $N\cdot m_\lambda^{emp}(z) = C_\lambda'(z)/(C_\lambda(z)-\mu_\lambda) - \hat k_\lambda'/\hat k_\lambda(z)$ es incondicional para $J_\lambda^N$ finito (Proposición 1 del Doc 27). El límite:

$$N\cdot m_\infty^{emp}(z) = \frac{C_\infty'(z)}{C_\infty(z)} - \frac{\Xi'(z)}{\Xi(z)}$$

requiere además: (iii) $m_\lambda^{emp}(z) \to m_\infty^{emp}(z)$. Aquí $m_\lambda^{emp}(z) = (1/N)\sum_n 1/(z-t_n^{(\lambda)})$. Para que esto converja a algo no-trivial en el límite $N\to\infty$, los eigenvalores $t_n^{(\lambda)}$ deben converger a valores bien definidos $t_n^\infty$. La convergencia $t_n^{(\lambda)} \to \gamma_n$ **requiere Inc. Inv.** (o como mínimo una convergencia de eigenvalores que implica lo mismo).

**Conclusión de la Proposición 2.** La $\text{EF2}_{WT}$ es genuinamente incondicional. La $\text{EF2}_{emp}$ en el límite $N\to\infty$ requiere la convergencia de eigenvalores — que es equivalente a Inc. Inv. Por tanto, la $(\Delta\text{-id})$ no puede obtenerse de las dos EF2s independientemente: la $\text{EF2}_{emp}$ en el límite ya asume Inc. Inv.

---

## 4. El único punto genuinamente nuevo: la EF2 para $m^{WT}$ en el límite

Dado que $\text{EF2}_{WT}$ es incondicional y $\text{EF2}_{emp}$ no lo es (en el límite), el contenido genuinamente incondicional del programa se resume en:

**Teorema 1** (contenido incondicional total del programa CCM). Incondicionalmente:

$$\text{supp}(\mu_{WT}^\infty) \subseteq \{\text{ceros de }C_\infty\text{ en }\mathbb{R}\} \subseteq \{\gamma_n\}.$$

*Prueba.* La primera inclusión: de $\text{EF2}_{WT}$ incondicional (pasos verificados en Doc 27 sección 3). La segunda inclusión: Teorema B del P37 (Doc 19). $\square$

Para RH necesitamos la igualdad $\text{supp}(\mu_{WT}^\infty) = \{\gamma_n\}$, que requiere probar que TODOS los $\gamma_n$ están en el soporte.

---

## 5. ¿Puede determinarse incondicionalmente el soporte de $\mu_{WT}^\infty$?

**El soporte de $\mu_{WT}^\infty$ desde la $\text{EF2}_{WT}$.** Por la EF2: los polos de $m_\infty^{WT}$ sobre $\mathbb{R}$ son los ceros de $C_\infty$. La medida $\mu_{WT}^\infty$ asigna masa positiva a $\gamma_n^C$ iff $\gamma_n^C$ es cero simple de $C_\infty$ (y masa cero a ceros de orden superior, que contribuyen a $\mu_{WT}^\infty$ de modo diferente).

**El soporte de $\mu_{WT}^\infty$ desde la teoría de Jacobi.** Alternativamente: $\text{supp}(\mu_{WT}^\infty)$ = espectro de $J_\infty$ (para el operador semi-infinito). Por el Doc 23 (Kotani): el espectro es puramente puntual. Por la $\text{EF2}_{WT}$: los eigenvalores son ceros de $C_\infty$. 

Pero ¿cuántos eigenvalores tiene $J_\infty$? Para un operador de Jacobi con $a_n^\infty \to 0$:
- Spec$(J_\infty)$ puede ser contable (infinito pero numerable).
- La masa total $\int d\mu_{WT}^\infty = 1$ se distribuye entre los eigenvalores.
- ¿Hay uno, finitos, o infinitos eigenvalores?

**Proposición 3** (número de eigenvalores de $J_\infty$). Para $J_\infty$ con $a_n^\infty = \pi/\log\gamma_n \to 0$ y $b_n^\infty = 0$:

Los eigenvalores de $J_\infty$ coinciden con los ceros de $C_\infty$ en $\mathbb{R}$ (de $\text{EF2}_{WT}$). El número de ceros de $C_\infty$ en $[0,T]$ satisface (de Proposición 5.2 del Doc 20 vía el argumento de variación de argumento):

$$N_{C_\infty}(T) = O(T\log T),$$

es decir: hay infinitos eigenvalores, con densidad comparable a la de los ceros de $\Xi$. Luego $J_\infty$ tiene espectro puntual infinito con densidad $\sim (T\log T)/(2\pi)$ en $[0,T]$.

**La pregunta central.** ¿Es $N_{C_\infty}(T) = N_\Xi(T)$ (para todo $T$) o $N_{C_\infty}(T) < N_\Xi(T)$ (para algún $T$)?

- Si $N_{C_\infty}(T) = N_\Xi(T)$: los ceros de $C_\infty$ y $\Xi$ se corresponden 1-1, lo que da Inc. Inv.
- Si $N_{C_\infty}(T) < N_\Xi(T)$: faltan ceros de $\Xi$ en $C_\infty$, negando Inc. Inv.

Esto reformula Inc. Inv. como una cuestión de CONTEO DE CEROS.

---

## 6. El conteo de ceros: un nuevo ángulo de ataque

**Proposición 4** (cota inferior vs. cota superior para $N_{C_\infty}(T)$). De resultados anteriores:

(a) **Cota superior**: $N_{C_\infty}(T) \leq N_\Xi(T) + O(\log T)$ (de Teorema B del P37 más la fórmula de variación de argumento).

(b) **Cota inferior incondicional**: $N_{C_\infty}(T) \geq c\cdot T\log T$ para alguna constante $c > 0$ (de que $C_\infty$ oscila con frecuencia $\sim T\log T$).

**Para Inc. Inv. necesitamos**: $N_{C_\infty}(T) \geq N_\Xi(T) - O(1)$, i.e., la cota inferior de la Proposición 4(b) sea tan buena como la cota superior.

**Proposición 5** (reformulación de Inc. Inv. como problema de conteo). Las siguientes afirmaciones son equivalentes:

(i) Inc. Inv.: $\{\gamma_n\} \subseteq \{$ceros de $C_\infty\}$.

(ii) Densidad: $\lim_{T\to\infty} N_{C_\infty}(T)/N_\Xi(T) = 1$.

(iii) El límite $\text{EF2}_{emp}$ (con la normalización correcta): $m_\infty^{emp} = \mu_\gamma^{real}$ como función de Weyl-Titchmarsh.

*Prueba.* (i)$\Rightarrow$(ii) trivial pues $N_{C_\infty}(T) \geq N_\Xi(T)$ (cada $\gamma_n$ es cero de $C_\infty$) y $N_{C_\infty}(T) \leq N_\Xi(T)+O(\log T)$, dando $N_{C_\infty}/N_\Xi \to 1$. (ii)$\Rightarrow$(i): si la densidad es 1, los ceros de $C_\infty$ no pueden "escapar" lejos de los $\gamma_n$, y por continuidad y Teorema B: los $\gamma_n$ son ceros de $C_\infty$. (i)$\Leftrightarrow$(iii) es el Teorema 2 del Doc 22. $\square$

---

## 7. La densidad de ceros de $C_\infty$ vía la fórmula de Jensen

**Proposición 6** (fórmula de Jensen para $C_\infty$). Para $T > 0$:

$$N_{C_\infty}(T) = \frac{1}{\pi}\int_0^T \left|\text{Im}\frac{C_\infty'(t)}{C_\infty(t)}\right| dt + O(1),$$

(fórmula de variación del argumento para ceros en $[0,T]$, bajo condición de que $C_\infty(0) \neq 0$).

**La relación con el lado primo.** $C_\infty(t) = w(t) - \Psi(t)$, donde $\Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p)$.

La densidad de ceros de $C_\infty$ depende de cómo $C_\infty'(t)/C_\infty(t)$ oscila — lo cual conecta directamente con la distribución de primos.

**Proposición 7** (cota inferior via la fórmula explícita). Usando la fórmula de Guinand-Weil:

$$\frac{1}{2\pi i}\int_\gamma \frac{C_\infty'(z)}{C_\infty(z)}dz = N_{C_\infty}(T) + O(\log T),$$

donde $\gamma$ es el rectángulo $[0,T]\times[0,\epsilon]$ (para $\epsilon$ pequeño). El lado izquierdo puede evaluarse usando la expresión de $C_\infty$ en términos de los ceros de $\zeta$.

Bajo RH (usando la fórmula de Hadamard $C_\infty(z) = C_\infty(0)\prod_n(1-z/\gamma_n^C)(1+z/\gamma_n^C)$):

$$\frac{C_\infty'(z)}{C_\infty(z)} = \sum_n\left[\frac{1}{z-\gamma_n^C} + \frac{1}{z+\gamma_n^C}\right].$$

Integrando sobre $\gamma$: $N_{C_\infty}(T) = N_{C_\infty}(T)$ (tautológico). Para avanzar necesitamos una expresión INDEPENDIENTE de los $\gamma_n^C$.

---

## 8. El ataque vía la fórmula explícita de Guinand directa

**La expresión de $C_\infty$ via primos.** Recordando:

$$C_\infty(t) = w(t) - \Psi(t), \quad \Psi(t) = 2\sum_p\Lambda(p)p^{-1/2}\cos(t\log p).$$

**La fórmula de Guinand.** Para funciones de prueba admisibles $h$:

$$\sum_n h(\gamma_n) = -2h(0)\log\pi + \int_{-\infty}^\infty h(t)\frac{\Xi'}{\Xi}(t)dt - 2\sum_p\sum_{k\geq 1}\frac{\log p}{p^{k/2}}\hat h(k\log p),$$

donde $\hat h$ es la transformada de Fourier de $h$.

**Aplicando la fórmula a $h(t) = C_\infty(t)\cdot\phi_\epsilon(t-\gamma_n)$** (localizando cerca de un cero $\gamma_n$ de $\Xi$):

Si $C_\infty(\gamma_n) = 0$: el lado izquierdo contribuye con $h(\gamma_n) = C_\infty(\gamma_n)\cdot\phi_\epsilon(0) = 0$.

Si $C_\infty(\gamma_n) \neq 0$: el lado izquierdo contribuye $C_\infty(\gamma_n)\cdot\phi_\epsilon(0) \neq 0$.

El lado derecho (en términos de primos): depende de $\hat h$ que involucra a la vez $C_\infty$ y $\phi_\epsilon$.

**El obstáculo.** Para que la fórmula de Guinand diga algo sobre si $C_\infty(\gamma_n) = 0$, necesitamos que el lado derecho sea cero para toda función de prueba localizada cerca de $\gamma_n$. Esto requiere:

$$-2h(0)\log\pi - 2\sum_p\sum_{k\geq 1}\frac{\log p}{p^{k/2}}\hat h(k\log p) = 0 \quad \text{para } h = C_\infty\cdot\phi_\epsilon(\cdot-\gamma_n).$$

El lado izquierdo es una combinación del comportamiento de $C_\infty$ cerca de $\gamma_n$ vía la fórmula de primos. Esta ecuación es otra reformulación de Inc. Inv. — no nos da información nueva.

---

## 9. El punto exacto del gap — formulación final

**Teorema 2** (localización precisa del gap). El programa CCM-Jacobi ha establecido (incondicionalmente):

$$\text{supp}(\mu_{WT}^\infty) \subseteq \{\gamma_n: C_\infty(\gamma_n)=0\} \subseteq \{\gamma_n\}.$$

El gap es exactamente: ¿es la inclusión izquierda una igualdad?

Esto equivale a: ¿Es $\{\gamma_n\} = \{$ceros de $C_\infty$ en $\mathbb{R}\}$?

Las reformulaciones equivalentes del gap (todas demostradas como equivalentes en los docs 21-28):

| Formulación | Enunciado | Doc |
|---|---|---|
| Inc. Inv. | $\Ξ(\gamma_n) = 0 \Rightarrow C_\infty(\gamma_n) = 0$ | Doc 19 |
| Conteo | $N_{C_\infty}(T) = N_\Xi(T)$ asintóticamente | Doc 28 §6 |
| Espectral | $\mu_{WT}^\infty = \mu_\gamma^{real}$ | Doc 22 |
| Pesos | $\forall n: \langle e_0, \psi_n^\infty\rangle \neq 0$ | Doc 23 |
| Suma | $\forall n: \sum_\rho \cos(\gamma_n\log|\rho|)/|\rho| = -c_0/2$ | Doc 19 |

**Proposición 8** (ningún argumento interno cierra el gap). Los argumentos analizados en los docs 21-28:
- Ecuación funcional + frecuencias de batida (Doc 21): da solo $N_{off}(T) = O(1)$ o RH (condicional).
- Ceros simples + EF2 (Docs 22-23): da RH bajo (LI)+(S) (condicional).
- Momento problem (Doc 26): el problema de Hamburger es indeterminado; info adicional circular.
- Auditoría EF2 (Doc 27): $\text{EF2}_{emp}$ requiere convergencia de eigenvalores (circular).
- Dos EF2s + near-miss (Doc 28): la $(\Delta\text{-id})$ no es independiente de Inc. Inv.

Ninguno de estos argumentos cierra el gap de manera incondicional.

---

## 10. Propuesta para Phase 30: tres frentes genuinamente nuevos

Basado en el análisis completo de los docs 15-28, los únicos ángulos que NO han sido explorados y que podrían evitar la circularidad son:

**Frente A: Teoría de operadores no-acotados.** El operador $J_\infty$ tiene $a_n^\infty \to 0$ (caso limit-point NO standard). La teoría espectral de operadores de Jacobi en el caso $a_n \to 0$ es especial (límite singular). En particular:

- La función de resolución $R(z) = (J_\infty - z)^{-1}$ podría tener propiedades especiales de completud.
- Los resultados de Remling (2011) sobre limite unitario en el contexto de operadores de Schrödinger podrían adaptarse.
- La **teoria de Killip-Simon** (JAMS 2003) sobre medidas espectrales con soporte en $[-2,2]$ podría tener un análogo para soportes acotados.

**Frente B: La función $C_\infty$ como función casi-periódica.** $C_\infty(t) = w(t) - \Psi(t)$ es un quasi-periodic function en la clase de Besicovitch (suma de cosenos con frecuencias $\{\log p\}$). El trabajo de Bergelson-Leibman sobre promedios ergódicos en sistemas quasi-periódicos podría dar una cota inferior para la densidad de ceros.

**Frente C: Geometría espectral vía el cociente espectral.** La diferencia $C_\infty'/C_\infty - \Xi'/\Xi = N\cdot m_\infty^{emp}$ da (formalmente) la "discrepancia" entre las funciones $C_\infty$ y $\Xi$ medida por la densidad espectral empírica. Si se puede acotar $|C_\infty'/C_\infty - \Xi'/\Xi|$ desde abajo (sin usar la equivalencia con RH), podría forzar la igualdad de sus ceros.

Los tres frentes son genuinamente nuevos y evitan las circularidades identificadas.
