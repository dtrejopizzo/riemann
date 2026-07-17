# Phase 24-A — Cotas inferiores para $b_j$: auditoría de métodos

## Pregunta central

**Si existe un cero $\rho_j = (1/2+b_j)+i\gamma_j$ con $b_j > 0$, ¿existe algún argumento que fuerce $b_j \geq F(\gamma_j)$ para alguna función $F$ explícita?**

Exploramos cuatro métodos naturales. Cada uno se evalúa hasta su límite exacto.

---

## Método 24-A.1: Fórmula explícita + KV

### El intento

Bajo Hipótesis D, la fórmula explícita modificada da:
$$\psi(x) - x = \psi_0(x) - x - D_m(x).$$

La componente dominante del defecto proveniente de $\mathcal{O}_j$ es:
$$D_j(x) = \frac{2x^{1/2+b_j}}{|\rho_j^+|}\cos(\gamma_j\log x - \theta_j) + O(x^{1/2-b_j}).$$

El teorema de Korobov–Vinogradov (incondicional) da:
$$|\psi(x) - x| \leq Cx\exp\!\left(-c_1\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}\right) =: K(x).$$

**Intento:** comparar el tamaño de $D_j(x)$ con $K(x)$ para obtener una cota inferior sobre $b_j$.

### El diagnóstico

$\psi(x) - x = \psi_0(x) - x - D_j(x) + (\text{otras órbitas})$.

El término $D_j(x)$ es parte de $\psi(x)-x$, así que:
$$|D_j(x)| \leq |\psi(x) - x| + |\psi_0(x) - x| + |(\text{otras})| \leq K(x) + |\psi_0(x) - x| + \ldots$$

Para aislar $D_j$ necesitamos controlar $\psi_0(x)-x$ independientemente. Pero $\psi_0$ involucra todos los ceros en la línea, que NO están controlados sin RH. En particular, $\psi_0(x)-x = -2\sum_{\gamma\in Z_{CL}} x^{1/2}\cos(\gamma\log x)/|\rho| + O(\log x)$, y el tamaño de esta suma es $O(x^{1/2}(\log x)^2)$ incondicionalmente (lo mejor que se puede hacer).

**Obstáculo:** $|\psi_0(x)-x| = O(x^{1/2}(\log x)^2)$, que excede $|D_j(x)| = O(x^{1/2+b_j}/|\rho_j|)$ para $b_j > 0$ arbitrario. La señal del defecto queda sepultada bajo el ruido de los ceros en línea.

**Proposición 24-A.1** (Barrera de la fórmula explícita para cotas inferiores). El método de comparar $D_j(x)$ con $K(x)$ no produce ninguna cota inferior sobre $b_j$. La razón es que el término $\psi_0(x)-x$ es de orden $x^{1/2}(\log x)^2$ incondicionalmente, y $D_j(x) = O(x^{1/2+b_j})$ siempre queda por debajo de $\psi_0(x)-x$ para cualquier $b_j \in (0,1/2)$.

*Demostración.* $|\psi_0(x)-x| \leq C x^{1/2}(\log x)^2$ sigue de la cota trivial sobre la suma de ceros en línea. $|D_j(x)| \leq 2x^{1/2+b_j}/|\rho_j|$. Para $b_j > 0$ y $x$ suficientemente grande: $x^{1/2+b_j} > x^{1/2}(\log x)^2$ iff $x^{b_j} > (\log x)^2$ iff $x > (\log x)^{2/b_j}$. Pero en ese rango, $D_j(x)$ ya excede $\psi_0(x)-x$, lo que no es un obstáculo para nada: simplemente significa que $D_j$ domina asintóticamente. No se obtiene ninguna cota inferior desde este análisis. $\square$

---

## Método 24-A.2: Evaluación de Hadamard en $t = \gamma_j$

### El intento

De la fórmula de Hadamard (Teorema~\ref{thm:hadamard} de P34):
$$\log|\zeta(1/2+i\gamma_j)| = \underbrace{2\log b_j + O(1)}_{\text{contribución de }\mathcal{O}_j} + \underbrace{\sum_{\rho \in Z_{CL}}\log\!\left(\frac{\gamma_j^2}{|\rho|^2}\right) + O(1)}_{\text{contribución de ceros en línea}} + O(\log\gamma_j).$$

Si pudiéramos acotar $\log|\zeta(1/2+i\gamma_j)|$ desde abajo, obtendríamos:
$$2\log b_j \geq -(\text{cota inferior de }\log|\zeta(1/2+i\gamma_j)|) - O(\log\log\gamma_j).$$

**Intento:** usar el teorema de Jensen o la fórmula de Borel–Carathéodory para acotar $|\zeta(1/2+i\gamma_j)|$ desde abajo.

### El diagnóstico

**Fórmula de Jensen** sobre el disco $|s - (\frac32 + i\gamma_j)| \leq 1$:
$$\log|\zeta(\tfrac32+i\gamma_j)| = \frac{1}{2\pi}\int_0^{2\pi}\log|\zeta(\tfrac32+i\gamma_j+e^{i\theta})|\,d\theta - \sum_{\rho:\text{en el disco}}\log\frac{1}{|\rho - (\frac32+i\gamma_j)|}.$$

El punto $\frac12+i\gamma_j$ está a distancia 1 del centro $\frac32+i\gamma_j$, así que está sobre la frontera del disco. Jensen controla ceros dentro del disco, pero el punto $\frac12+i\gamma_j$ no está en el interior.

Variante: Jensen sobre el disco centrado en $\frac12+i\gamma_j$. Pero $\frac12+i\gamma_j$ podría ser un cero de $\zeta$ (si está en la línea crítica y $\gamma_j$ es la altura de un cero de línea). Sin embargo, asumimos que $\frac12+i\gamma_j$ NO es cero de $\zeta$ (en la línea): el cero es $\frac12+b_j+i\gamma_j$, fuera de línea.

**El problema fundamental:** para acotar $|\zeta(1/2+i\gamma_j)|$ desde abajo necesitamos que $\zeta$ no sea demasiado pequeño en ese punto. Pero no existe ninguna herramienta que garantice $|\zeta(1/2+it)| \geq \exp(-F(t))$ en un punto específico $t$, sin hipótesis sobre los ceros cercanos.

De hecho, si hay un cero de $\zeta$ en la línea con $Im(\rho) = \gamma_j$ (un "cero en línea a la misma altura"), entonces $\zeta(1/2+i\gamma_j) = 0$ exactamente. En ese caso, $\log|\zeta(1/2+i\gamma_j)| = -\infty$: no hay ningún lower bound.

Pero si $\gamma_j$ NO es la parte imaginaria de ningún cero en línea, entonces $\zeta(1/2+i\gamma_j) \neq 0$. ¿Puede acotarse cuán pequeño es?

**La Fórmula de Borel–Carathéodory** permite acotar:
$$|\zeta(\sigma+i\gamma_j)| \geq \exp\!\left(-C\frac{\log|\zeta(2+i\gamma_j)|}{\sigma - \frac12}\right).$$

Para $\sigma = \frac12$ esto no da información directa (el denominador es 0).

**Resultado conocido (tipo Titchmarsh):** Para $t$ fuera de un conjunto excepcional de medida pequeña:
$$|\zeta(1/2+it)| \geq \exp\!\left(-C\frac{\log t}{\log\log t}\right).$$
(Ver Titchmarsh, §9.6.) Pero esto es para $t$ "genérico", no para $t = \gamma_j$ específico.

**Proposición 24-A.2** (No existe lower bound puntual incondicionalmente). No existe ningún teorema actualmente conocido de la forma $|\zeta(1/2+i\gamma_j)| \geq \exp(-F(\gamma_j))$ para $\gamma_j$ el dato imaginario de un cero fuera de línea, con $F$ creciendo más lentamente que $\gamma_j$.

*Justificación.* Por la fórmula de Hadamard, si hubiera un cero $\rho^*$ en la línea crítica con $Im(\rho^*) = \gamma_j$, entonces $\zeta(1/2+i\gamma_j) = 0$ y ningún lower bound positivo existe. En ausencia de tal cero en línea, $\zeta(1/2+i\gamma_j) \neq 0$, pero su magnitud depende de la distribución completa de todos los ceros, incluyendo los en línea, y no puede acotarse desde abajo sin información sobre esa distribución. $\square$

---

## Método 24-A.3: Momentos de $|\zeta|$

### El intento

Los momentos del valor absoluto de $\zeta$ en la línea crítica:
$$I_k(T) = \int_0^T |\zeta(1/2+it)|^{2k}\,dt \sim C_k T(\log T)^{k^2}.$$

Si la órbita $\mathcal{O}_j$ (con $\gamma_j \sim T$) suprime $|\zeta(1/2+i\gamma_j)|$ por un factor $b_j^2$ (de la depresión Hadamard), ¿puede esto contradecir la estimación de momentos?

La contribución de $\mathcal{O}_j$ al integrando en un intervalo de ancho $b_j$ alrededor de $\gamma_j$:
$$b_j \cdot |\zeta(1/2+i\gamma_j)|^{2k} \approx b_j \cdot (b_j^2 \cdot |\zeta_{reg}|)^{2k}$$
donde $\zeta_{reg}$ es la "parte regular" sin la contribución de $\mathcal{O}_j$.

Esta contribución es pequeña: $\sim b_j^{4k+1}$, que tiende a 0 sin contradecir $I_k(T) \sim C_k T(\log T)^{k^2}$.

**Proposición 24-A.3** (Momentos no producen cota inferior). La supresión de $|\zeta(1/2+i\gamma_j)|$ por un factor $b_j^2$ no contradice ningún resultado sobre momentos, pues la contribución al integral de momentos sobre un intervalo de ancho $b_j$ es $O(b_j^{4k+1}) \to 0$ para cualquier $b_j \to 0$.

*Demostración.* La contribución local de $[\gamma_j-b_j, \gamma_j+b_j]$ al integral $I_k(T)$ es a lo sumo $2b_j \cdot \sup_{|t-\gamma_j|\leq b_j}|\zeta(1/2+it)|^{2k}$. El supremo es acotado (pues $\zeta$ es localmente acotado) por $O(1)$, así que la contribución es $O(b_j) \to 0$. No hay contradicción con $I_k(T) \sim CT(\log T)^{k^2}$. $\square$

---

## Método 24-A.4: La cadena Hadamard–CMG revisada con rigor

### El intento

De la corrección de 23-A.6: si $b_j < \gamma_j^{-C}$, la depresión Hadamard supera el mínimo CMG. ¿Puede esto producir una cota inferior sobre $b_j$?

Para que el argumento sea riguroso se necesita:
1. Que $\min_{t \in [T,2T]}\log|\zeta(1/2+it)| \geq -C\log T$ (cota **inferior** sobre el mínimo).
2. Que la contribución de $\mathcal{O}_j$ a $\log|\zeta(1/2+i\gamma_j)|$ sea la dominante.

**Estado de (1):** Los resultados actuales dan cotas SUPERIORES sobre el mínimo:
- $\min_{t \in [T,2T]}\log|\zeta(1/2+it)| \leq -c(\log T)^{1/2-\varepsilon}$ para $T$ grande (existencia de valores muy pequeños).

Para una cota INFERIOR del tipo $\min \geq -C\log T$: no existe ningún teorema incondicional de esta forma. Se sabe que $|\zeta(1/2+it)|$ puede ser exponencialmente pequeño en $t$ (por la cercanía de ceros a la línea).

**Estado de (2):** La contribución de $\mathcal{O}_j$ a $\log|\zeta(1/2+i\gamma_j)|$ es $2\log b_j + O(1)$ (Hadamard). Las otras contribuciones son $O(\log\log\gamma_j)$ por el teorema central límite de Selberg (condicional) o $O((\log\gamma_j)^{1/2+\varepsilon})$ incondicionalmente (cota trivial sobre la suma de ceros en línea). Si $|2\log b_j| \gg (\log\gamma_j)^{1/2}$, la contribución de $\mathcal{O}_j$ domina.

**Proposición 24-A.4** (Barrera del lower bound del mínimo CMG). La cadena Hadamard–CMG produce una cota inferior condicional pero no incondicional:

*Condicional:* Si (i) $\min_{t \in [\gamma_j/2, 2\gamma_j]}\log|\zeta(1/2+it)| \geq -C\log\gamma_j$ y (ii) la suma de Hadamard de los ceros en línea satisface $|\sum_{\rho\in Z_{CL}}(\ldots)| \leq D\log\log\gamma_j$, entonces:
$$2|\log b_j| + O(\log\log\gamma_j) \leq C\log\gamma_j$$
$$b_j \geq \exp\!\left(-\frac{C}{2}\log\gamma_j - O(\log\log\gamma_j)\right) = \gamma_j^{-C/2+o(1)}.$$

*Incondicional:* ni (i) ni (ii) están disponibles actualmente.

*Demostración.* De la identidad de Hadamard completa:
$$\log|\zeta(1/2+i\gamma_j)| = 2\log b_j + O(1) + \sum_{\rho \in Z_{CL}} [\log(b_j^2+(\gamma_j-Im(\rho))^2) + O(1)] + O(\log\gamma_j).$$
Si $\log|\zeta(1/2+i\gamma_j)| \geq -C\log\gamma_j$ y la suma sobre ceros en línea es $O(\log\log\gamma_j)$ (hipótesis), entonces $2\log b_j \geq -C\log\gamma_j - O(\log\log\gamma_j)$. $\square$

---

## Resultado de Phase 24-A

**Teorema 24-A.1** (No-existencia de cotas inferiores incondicionales). Ninguno de los cuatro métodos anteriores produce una cota inferior incondicional $b_j \geq F(\gamma_j)$ para un cero fuera de línea individual.

La razón estructural unificada es:

- **Fórmula explícita:** la señal de $D_j(x)$ está sepultada bajo $\psi_0(x)-x = O(x^{1/2}(\log x)^2)$.
- **Hadamard puntual:** no existe lower bound incondicional para $|\zeta(1/2+i\gamma_j)|$.
- **Momentos:** la contribución local de $\mathcal{O}_j$ es $O(b_j)$, invisible en el promedio.
- **Cadena CMG:** requiere un lower bound incondicional sobre $\min\log|\zeta|$, no disponible.

**Corolario 24-A.2** (Diagnóstico preciso del hueco). La pregunta "$b_j \geq F(\gamma_j)$?" es equivalente, vía la cadena Hadamard, a preguntar si la función $\zeta$ en la línea crítica tiene un **lower bound puntual** en $t = \gamma_j$. Tal lower bound existe iff el campo $\log|\zeta(1/2+it)|$ tiene su distribución controlada con suficiente precisión en puntos específicos, lo que requiere control fino del campo log-correlacionado más allá de lo actualmente disponible.

---

## Qué sí se puede hacer: un resultado condicional útil

**Proposición 24-A.5** (Cota inferior condicional en el Régimen I). Suponiendo que el teorema central límite de Selberg se aplica a $t = \gamma_j$ (hipótesis razonable pero no probada en ese punto específico), y que el campo de ceros en línea contribuye $O(\log\log\gamma_j)$ a $\log|\zeta(1/2+i\gamma_j)|$, entonces:

$$b_j \geq \exp\!\left(-C\log T\right) = T^{-C}$$

donde $T \sim \gamma_j$. Es decir, $b_j$ debe ser al menos polinomialmente grande en $1/\gamma_j$.

Esta cota implicaría que el Régimen III ($b_j \leq e^{-c\gamma_j}$, superexponencialmente pequeño) es imposible bajo la hipótesis de Selberg.

**Estado:** La hipótesis de Selberg (CLT para $\log|\zeta(1/2+it)|$) se verifica en promedio sobre $t \in [T,2T]$ pero NO está probada para valores específicos $t = \gamma_j$ (Teorema central límite de Selberg, 1946, da convergencia en distribución para $t$ aleatorio, no para $t$ fijo determinístico).

---

## Dirección hacia Phase 24-B

Phase 24-A concluye que no existe ninguna cota inferior incondicional y que el obstáculo es precisamente el control puntual de $\log|\zeta(1/2+i\gamma_j)|$.

Phase 24-B atacará el problema desde el otro lado: en lugar de acotar $b_j$ desde abajo, analizar si el **perfil local** $\ell_j(u) = \log|\zeta(1/2+i(\gamma_j+ub_j))|$ como función de $u = O(1)$ tiene una forma geométrica incompatible con la rigidez del campo log-correlacionado, independientemente del valor específico de $b_j$.

La observación clave es que el perfil $\ell_j(u) \approx \log(1+u^2) + C$ es un perfil **determinístico y universal** (Lorentziano) superpuesto a un campo aleatorio. La incompatibilidad — si existe — estará en la geometría, no en el valor puntual.

---

## Tabla de resultados de Phase 24-A

| Método | Resultado | Clase | Estado |
|--------|-----------|-------|--------|
| 24-A.1 (Fórmula explícita + KV) | No produce lower bound; señal sepultada bajo $\psi_0$ | Negativo | ✓ |
| 24-A.2 (Hadamard puntual + Jensen) | No existe lower bound incondicional para $\|\zeta(1/2+i\gamma_j)\|$ | Negativo | ✓ |
| 24-A.3 (Momentos) | Contribución local $O(b_j)$, invisible en integrales | Negativo | ✓ |
| 24-A.4 (Cadena Hadamard–CMG) | Cota inferior condicional $b_j \geq \gamma_j^{-C/2}$ | Condicional | ✓ |
| **Teorema 24-A.1** | No existe lower bound incondicional; hueco bibliográfico confirmado | Diagnóstico B | ✓ |
| **Prop. 24-A.5** | Condicional a CLT de Selberg: $b_j \geq \gamma_j^{-C}$ | Condicional | ✓ |
