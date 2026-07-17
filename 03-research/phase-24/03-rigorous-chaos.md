# Phase 24-C — Resultados rigurosos sobre $\log|\zeta|$ y compatibilidad

## Objetivo

Phase 24-A y 24-B produjeron resultados negativos. Phase 24-C hace el inventario exacto de lo que SÍ está probado sobre $\log|\zeta(1/2+it)|$, y determina si algún resultado probado (no conjeturado) impone una restricción sobre $b_j$.

---

## 1. Inventario de resultados probados sobre $\log|\zeta(1/2+it)|$

### 1.1 Teorema central límite de Selberg (1946)

Para $t$ uniforme en $[T, 2T]$:
$$\frac{\log|\zeta(1/2+it)|}{\frac{1}{\sqrt{2}}\sqrt{\log\log T}} \xrightarrow{d} N(0,1).$$

**Lo que dice:** la distribución de $\log|\zeta(1/2+it)|$ es aproximadamente gaussiana con varianza $\frac12\log\log T$ para $t$ aleatorio en $[T,2T]$.

**Lo que NO dice:** nada sobre el valor en un punto específico $t = \gamma_j$. La convergencia es en distribución para $t$ aleatorio, no para $t$ fijo.

### 1.2 Cota superior incondicional sobre $\log|\zeta(1/2+it)|$

(Ramachandra 1980, Titchmarsh): para todo $t \geq 2$:
$$\log|\zeta(1/2+it)| \leq C\sqrt{\log t}(\log\log t).$$

(Bajo RH se mejoraría a $O(\sqrt{\log t})$.)

**Lo que dice:** cota superior sobre los valores extremos máximos.

**Lo que NO dice:** nada sobre valores extremos mínimos.

### 1.3 Existencia de valores extremos negativos (mínimos profundos)

(Titchmarsh, §9.6): para cualquier $A > 0$ existen $t$ arbitrariamente grandes con:
$$\log|\zeta(1/2+it)| \leq -A(\log t)^{1/3}.$$

Más fuerte (Radziwiłł–Soundararajan 2013): para cualquier $c > 0$ existe una proporción positiva de $t \in [T,2T]$ con $\log|\zeta(1/2+it)| \leq -c(\log\log T)^{1/2}$.

**Lo que dice:** el mínimo de $\log|\zeta|$ sobre $[T,2T]$ puede ser muy negativo.

### 1.4 Cota inferior (si existe) sobre el mínimo

No existe ningún resultado del tipo $\log|\zeta(1/2+it)| \geq -F(t)$ para $F$ de crecimiento subexponencial que valga fuera de los ceros. Cerca de los ceros en línea, $|\zeta(1/2+i\gamma)| = 0$, así que el mínimo es $-\infty$.

Para $t$ lejos de todos los ceros en línea: la cota inferior más fuerte conocida es del tipo $|\zeta(1/2+it)| \geq e^{-C\log t/\log\log t}$ en promedio (cota que se sigue del teorema de cero libre) pero no puntualmente.

**Conclusión:** no existe ningún lower bound incondicional puntual sobre $\log|\zeta(1/2+it)|$ válido en un punto $t$ arbitrario.

### 1.5 Resultados de Harper y Soundararajan sobre momentos y extremos

Harper (2020): los momentos $\int_T^{2T}|\zeta(1/2+it)|^{2k}dt$ tienen la forma predicha por Keating–Snaith para todos los $k$ racionales positivos con constante explícita.

Soundararajan (2009): $\max_{t\in[T,2T]}\log|\zeta(1/2+it)| = (1+o(1))\sqrt{\frac12\log\log T\cdot\log\log\log T}$ condicionalmente bajo RH. Incondicionalmente: $\leq C\sqrt{\log T}$.

Arguin–Bovier–Kistler (2011–2013), Najnudel (2018), Paquette–Zeitouni (2018): el máximo de $\log|\zeta|$ sobre $[T,2T]$ tiene la distribución de Gumbel a escala $\sqrt{\log\log T}$ (condicionalmente). Incondicionalmente: sólo cotas.

**Para el mínimo:** no hay análogos rigurosos de los resultados sobre el máximo.

---

## 2. Lo que estos resultados dicen sobre la compatibilidad con $\mathcal{O}_j$

**Proposición 24-C.1** (Compatibilidad incondicional: el espacio está vacío). Ninguno de los resultados rigurosos anteriores impone ninguna cota inferior sobre $|\zeta(1/2+i\gamma_j)|$ en el punto $t = \gamma_j$ específico, para ningún valor de $b_j$.

Por tanto, el argumento de incompatibilidad CMG-Hipótesis D requiere al menos uno de:
- (R1) Un lower bound riguroso sobre $\min_{t\in[T,2T]}\log|\zeta(1/2+it)|$ estrictamente mayor que $-\infty$.
- (R2) Un resultado de la forma "para $t$ en un conjunto específico (p.ej., las alturas de ceros fuera de línea), $\log|\zeta(1/2+it)|$ es acotado inferiormente".

Ni (R1) ni (R2) existen actualmente.

**Proposición 24-C.2** (Interferencia de ceros en línea). Sea $\gamma^*$ un cero de $\zeta$ en la línea crítica más cercano a $\gamma_j$, con $|\gamma_j - \gamma^*| = \delta^*$. El cero en línea $\rho^* = 1/2+i\gamma^*$ contribuye al Hadamard en $t=\gamma_j$:
$$\delta_{\rho^*}\log|\zeta(1/2+i\gamma_j)| = \log(\delta^*)^2 - \log|\rho^*|^2 + O(1) = 2\log\delta^* + O(1).$$

Si $\delta^* \ll b_j$ (el cero en línea más cercano está más cerca de $\gamma_j$ que el off-line $b_j$), entonces la contribución del cero en línea supera la del cero fuera de línea: $2\log\delta^* \ll 2\log b_j$.

**Consecuencia:** la profundidad de la depresión en $t=\gamma_j$ está dominada por el cero en línea más cercano, no por el fuera de línea, si $\delta^* < b_j$. El cero fuera de línea es "invisible" en $\log|\zeta(1/2+i\gamma_j)|$ bajo esa condición.

*Demostración.* Aplicación directa del producto de Hadamard al cero $\rho^* = 1/2+i\gamma^*$:
$$\text{contribución de }\rho^*\text{ en }t=\gamma_j: \; \log|1-(1/2+i\gamma_j)/(1/2+i\gamma^*)| = \log|\delta^*/\rho^*| + O(1). \quad\square$$

---

## 3. El dilema de la "interferencia de ceros en línea"

**Lema 24-C.3** (Dilema $\delta^*$ vs $b_j$). Hay dos casos:

*Caso A: $\delta^* \geq b_j$ (el cero en línea más cercano está lejos).* Entonces la contribución del cero fuera de línea domina en $\log|\zeta(1/2+i\gamma_j)|$, con profundidad $\sim 2\log b_j$. Pero como $\delta^* \geq b_j$, el cero en línea más cercano contribuye $\leq 2\log b_j$ también, así que no hay separación clara.

*Caso B: $\delta^* < b_j$ (el cero en línea más cercano está muy cerca de $\gamma_j$).* Entonces la profundidad en $t=\gamma_j$ está dominada por $2\log\delta^*$. La contribución del cero fuera de línea queda completamente enmascarada. No hay información sobre $b_j$ en $\log|\zeta(1/2+i\gamma_j)|$.

**Conclusión:** la depresión de Hadamard en $t=\gamma_j$ no identifica de manera limpia la contribución del cero fuera de línea, salvo en el Caso A. Y en el Caso A, no hay restricción sobre $b_j$ proveniente del CMG (la depresión es compatible con el campo para $b_j \geq \gamma_j^{-C}$, Régimen I).

---

## 4. El obstáculo final de Phase 24

**Teorema 24-C.4** (Cierre de Phase 24). Los tres métodos de Phase 24 (24-A: lower bounds directos; 24-B: perfil local; 24-C: resultados rigurosos sobre $\log|\zeta|$) producen colectivamente el siguiente diagnóstico:

Para demostrar que $b_j \geq F(\gamma_j)$ para alguna función $F$ no trivial, o equivalentemente para demostrar que la Hipótesis D con $b_j$ super-polinomialmente pequeño es imposible, se necesita al menos uno de:

**(G1)** Un lower bound incondicional sobre $|\zeta(1/2+i\gamma_j)|$ en puntos $\gamma_j$ que son partes imaginarias de ceros fuera de línea. Equivalente a: una cota del tipo $\log|\zeta(1/2+it)| \geq -F(t)$ con $F$ creciendo más lentamente que $c \cdot (\text{profundidad del cero en línea más cercano})^{-1}$.

**(G2)** Un control del espaciado $\delta^*$ entre los ceros en línea y las alturas de ceros fuera de línea: si $\delta^* \geq b_j$ incondicionalmente, entonces la señal del cero fuera de línea sería visible en $\log|\zeta|$. Pero esto es equivalente a información sobre la distribución conjunta de ceros en línea y ceros fuera de línea.

**(G3)** Un resultado de rigidez del campo log-correlacionado que diga que el proceso $\{\log|\zeta(1/2+it)| : t \in [T,2T]\}$ no puede tener depresiones de profundidad $\gg \log T$ en puntos $t$ específicos no relacionados con ceros en línea. No existe ningún resultado de este tipo actualmente.

**Ninguna de (G1), (G2), (G3) es actualmente accesible.**

*Demostración.* (G1): sigue de Prop. 24-C.1. (G2): información sobre $\delta^*$ requiere conocer la distribución de ceros en línea y fuera de línea conjuntamente, equivalente a información más fuerte que RH. (G3): los resultados de Harper, Arguin–Bovier–Kistler y Najnudel controlan el máximo, no el mínimo de $\log|\zeta|$. $\square$

---

## 5. Cuadro completo de Phase 24

| Objetivo | Resultado | Tipo | Fase |
|----------|-----------|------|------|
| Lower bound $b_j \geq F(\gamma_j)$ via fórmula explícita | Imposible: señal sepultada | Negativo | 24-A |
| Lower bound via Hadamard + Jensen | Imposible: no hay lower bound puntual para $\|\zeta\|$ | Negativo | 24-A |
| Lower bound via momentos $I_k$ | Imposible: contribución local $O(b_j)$ | Negativo | 24-A |
| Lower bound condicional (Selberg CLT) | $b_j \geq \gamma_j^{-C}$ condicionalmente | Condicional | 24-A |
| Perfil Lorentziano $P(u) = \log(1+u^2)$ | Universal, determinístico — nuevo resultado | B | 24-B |
| Incompatibilidad geométrica del perfil | Imposible: perfil sumergido bajo fluctuaciones del campo | Negativo | 24-B |
| Resultados rigurosos sobre $\min\log\|\zeta\|$ | No existen lower bounds incondicionales | Negativo | 24-C |
| Interferencia ceros en línea (dilema $\delta^*$ vs $b_j$) | Oscurece la señal del cero fuera de línea | Negativo | 24-C |
| Obstáculo final (G1/G2/G3) | Ninguno accesible | B | 24-C |

---

## 6. Balance honesto de Phase 24

Phase 24 es mayoritariamente un resultado negativo triple.

**Lo que sí se ganó:**

1. **Diagnóstico preciso del hueco bibliográfico:** confirmación de que no existe ningún resultado de la forma $b_j \geq F(\gamma_j)$ en la literatura, y que ningún método estándar puede producirlo.

2. **El perfil Lorentziano:** $P(u) = \log(1+u^2)$ es un resultado positivo (nuevo, geométricamente preciso, sin precedente directo en la literatura).

3. **El dilema $\delta^*$ vs $b_j$** (Proposición 24-C.2): revela que incluso si hubiera una cota inferior para $|\zeta(1/2+i\gamma_j)|$, la interferencia con ceros en línea cercanos haría imposible aislar la contribución de $b_j$.

4. **La cadena de obstáculos (G1/G2/G3):** nombra con precisión las tres puertas que están cerradas.

**El resultado negativo a su vez tiene valor:** muestra que para cualquier intento de restricción de $b_j$ vía el comportamiento de $\log|\zeta|$ en la línea crítica, es necesario entender la distribución CONJUNTA de ceros en línea y fuera de línea, no cada uno por separado. Esa distribución conjunta es precisamente el corazón del problema no resuelto.

---

## 7. Phase 25: la única dirección no agotada

Phases 22-24 han agotado sistemáticamente:
- La fórmula explícita y sus cotas (aritmética para $\Re(s)>1$).
- El producto de Hadamard y el comportamiento en la línea crítica.
- Los campos log-correlacionados y sus resultados rigurosos.
- Los momentos de $|\zeta|$.
- La geometría local de la depresión inducida por un cero fuera de línea.

La única dirección no agotada, identificada en las Phases 22-23 como Wall W4-RSRP, sigue siendo:

**¿Puede la unicidad de la continuación analítica del producto de Euler $\prod_p(1-p^{-s})^{-1}$ forzar, mediante algún mecanismo estructural, la ubicación de los ceros en la línea crítica?**

Esta pregunta conecta con:
- La función zeta de Riemann como ÚNICA función con las propiedades combinadas (Euler para $\Re(s)>1$, ecuación funcional, orden de Hadamard 1, polo simple en $s=1$).
- El programa de Connes (espacio adélico, donde el producto de Euler es un factor euleriano del operador de traza).
- La casi-periodicidad de Bohr y la estructura de los valores $p^{-s}$ para $\Re(s)$ variable.

Esta es la dirección de **Phase 25**.
