# Documento 81 — Positividad de $L(z)$ sobre la circunferencia unidad y la reformulación via el disco

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM (Camino 2)
**Fecha:** 2026-06-09
**Prerrequisitos:** Docs 75, 78, 79

---

## Resumen

Este documento desarrolla con rigor el Camino 2 del programa: la función $L(z) = \log\xi(z/(z-1))$ y la condición de positividad sobre la circunferencia unidad $|z| = 1$. En §1 se establece la geometría exacta de la transformación de Möbius $\tau(z) = z/(z-1)$ y se identifica sin ambigüedad qué regiones del plano $s$ corresponden al interior, la frontera y el exterior del disco unitario. En §2 se estudia la función $F(z) = \xi(z/(z-1))$ y se demuestra que RH es equivalente a la ausencia de ceros de $F$ en el interior del disco (Proposición 2.1). En §3 se analiza la condición de positividad $\mathrm{Re}[L(e^{i\theta})] \geq 0$ y se muestra que es necesariamente falsa en los ceros de $\xi$ sobre la recta crítica; el enfoque de positividad en la frontera no puede funcionar directamente. En §4 se formula la condición correcta de Nevanlinna-Herglotz en el interior del disco, y se establece su equivalencia con RH vía la función de Carathéodory (Proposición 4.2). En §5 se desarrolla la conexión con los polinomios ortogonales en la circunferencia unidad (OPUC) y los coeficientes de Schur, señalando con precisión qué parte del formalismo de OPUC es automática y qué parte requiere nueva entrada. En §6 se examina si alguna propiedad de $\xi$ independiente de la posición de sus ceros puede forzar la no-anulación en el disco. La conclusión honesta es que la reformulación vía el disco es exacta y elegante, pero la prueba de la condición de no-ceros es equivalente a RH y no se obtiene de manera gratuita.

---

## §1. Geometría de la transformación $\tau(z) = z/(z-1)$

### 1.1. Descripción básica

Sea $\tau : \hat{\mathbb{C}} \to \hat{\mathbb{C}}$ la transformación de Möbius definida por
$$\tau(z) = \frac{z}{z-1}.$$
Sus valores en puntos especiales: $\tau(0) = 0$, $\tau(1/2) = -1$, $\tau(\infty) = 1$, $\tau(2) = 2$, y $\tau(1) = \infty$ (polo simple). La inversa es $\tau^{-1}(s) = s/(s-1)$, es decir, $\tau$ es una involución: $\tau \circ \tau = \mathrm{id}$.

### 1.2. Imagen del disco unitario

**Proposición 1.1.** *La transformación $\tau$ establece una biyección analítica entre:*
- *$\{|z| < 1\} \longleftrightarrow \{\mathrm{Re}(s) < 1/2\}$,*
- *$\{|z| = 1,\, z \neq 1\} \longleftrightarrow \{\mathrm{Re}(s) = 1/2\}$,*
- *$\{|z| > 1\} \longleftrightarrow \{\mathrm{Re}(s) > 1/2\}$.*

*Demostración.* Sea $s = \tau(z)$. Entonces $z = \tau(s) = s/(s-1)$, y por tanto $|z| < 1 \iff |s/(s-1)| < 1 \iff |s| < |s-1|$. Escribiendo $s = \sigma + it$, la condición $|s| < |s-1|$ es $\sigma^2 + t^2 < (\sigma-1)^2 + t^2$, es decir, $\sigma^2 < \sigma^2 - 2\sigma + 1$, es decir, $2\sigma < 1$, es decir, $\sigma < 1/2$. Las otras dos afirmaciones se deducen de manera análoga. $\square$

**Corolario 1.2.** *Si $\rho = \sigma + i\gamma$ es un cero no trivial de $\xi$, entonces $z_\rho = \tau(\rho) = \rho/(\rho-1)$ satisface:*
- *$|z_\rho| < 1$ si y solo si $\sigma < 1/2$,*
- *$|z_\rho| = 1$ si y solo si $\sigma = 1/2$ (i.e., $\rho$ está en la recta crítica),*
- *$|z_\rho| > 1$ si y solo si $\sigma > 1/2$.*

### 1.3. Parametrización de la recta crítica

Para $s = 1/2 + it$ con $t \in \mathbb{R}$, el punto correspondiente en la circunferencia unidad es
$$z(t) = \tau(1/2+it) = \frac{1/2+it}{it-1/2} = -\frac{1/2+it}{1/2-it} = -e^{2i\arctan(2t)}.$$
Cuando $t$ recorre $\mathbb{R}$, $\arctan(2t)$ recorre $(-\pi/2, \pi/2)$, así que $2\arctan(2t)$ recorre $(-\pi, \pi)$. Por tanto, $z(t)$ recorre el arco $\{e^{i\theta} : \theta \in (0, 2\pi)\} = \{|z|=1\} \setminus \{1\}$ (es decir, la circunferencia unidad menos el punto $z = 1$, que correspondería a $t \to \pm\infty$, i.e., $s \to 1/2 \pm i\infty$).

### 1.4. Simetría de $\tau$ bajo la ecuación funcional

La ecuación funcional $\xi(s) = \xi(1-s)$ en coordenadas del disco: si $s = \tau(z)$, entonces $1 - s = 1 - z/(z-1) = -1/(z-1)$, de modo que $\xi(\tau(z)) = \xi(-1/(z-1))$. La función $F(z) = \xi(z/(z-1))$ satisface así
$$F(z) = \xi\!\left(\frac{-1}{z-1}\right).$$
En particular, si $z_0$ es cero de $F$, también lo es $z_1 = 1 - 1/\tau(z_0) = \ldots$; la simetría de los ceros de $\xi$ se refleja en una simetría de los ceros de $F$ respecto a la circunferencia unidad.

---

## §2. La función $F(z) = \xi(z/(z-1))$ y la equivalencia con RH

### 2.1. Analiticidad de $F$

La función $\xi$ es entera de orden 1, y la transformación $\tau(z) = z/(z-1)$ es analítica en $\mathbb{C} \setminus \{1\}$. En el disco unitario cerrado $\{|z| \leq 1\}$, el punto $z = 1$ está en la frontera (solo accesible como límite desde el interior), y $\tau(z) \to \infty$ cuando $z \to 1$. Puesto que $\xi(s) \to \infty$ cuando $s \to \infty$ (de hecho $|\xi(s)| \to \infty$ por el factor $\Gamma$), la función $F(z)$ no tiene límite finito cuando $z \to 1$ desde el interior del disco.

En consecuencia, $F$ es analítica en el disco abierto $\{|z| < 1\}$ (ya que $\xi$ es entera y $\tau$ es analítica en $|z| < 1$, donde $\tau(z)$ toma valores en $\mathrm{Re}(s) < 1/2$, región libre de singularidades de $\xi$). La función $F$ no se extiende continuamente al punto $z = 1$ de la frontera, pero sí a todos los demás puntos de $|z| = 1$.

### 2.2. Los ceros de $F$ en relación con RH

Los ceros de $F$ en el disco abierto $\{|z| < 1\}$ corresponden exactamente a los ceros de $\xi$ en $\{\mathrm{Re}(s) < 1/2\}$. Por la ecuación funcional $\xi(s) = \xi(1-s)$, si $\rho$ es un cero de $\xi$ con $\mathrm{Re}(\rho) > 1/2$, entonces $1-\rho$ es un cero con $\mathrm{Re}(1-\rho) < 1/2$. Por tanto, los ceros de $\xi$ en $\{\mathrm{Re}(s) < 1/2\}$ están en biyección con los ceros en $\{\mathrm{Re}(s) > 1/2\}$: ningún cero en $\{\mathrm{Re}(s) < 1/2\}$ es equivalente a ningún cero en $\{\mathrm{Re}(s) > 1/2\}$.

**Proposición 2.1.** *Las siguientes condiciones son equivalentes:*

*(i) Hipótesis de Riemann: todos los ceros no triviales de $\zeta$ (equivalentemente, de $\xi$) tienen parte real $1/2$.*

*(ii) La función $F(z) = \xi(z/(z-1))$ no tiene ceros en el disco abierto $\{|z| < 1\}$.*

*(iii) La función $F$ no tiene ceros en la región $\{|z| > 1\}$ (i.e., en $\{\mathrm{Re}(s) > 1/2\}$).*

*Nota: (ii) y (iii) son equivalentes por la ecuación funcional.*

*Demostración.* Por el Corolario 1.2, los ceros de $F$ en $|z| < 1$ corresponden exactamente a los ceros de $\xi$ en $\mathrm{Re}(s) < 1/2$. Por la ecuación funcional, $\xi$ no tiene ceros en $\mathrm{Re}(s) < 1/2$ si y solo si no los tiene en $\mathrm{Re}(s) > 1/2$, lo que equivale a que todos sus ceros estén en $\mathrm{Re}(s) = 1/2$, es decir, (i). $\square$

---

## §3. La condición de positividad en la frontera y su fracaso

### 3.1. La condición $\mathrm{Re}[L(e^{i\theta})] \geq 0$

Definimos $L(z) = \log F(z)$ con una rama de logaritmo apropiada. En la circunferencia unidad, $z = e^{i\theta}$ corresponde (mediante $\tau$) al punto $s = \tau(e^{i\theta})$, que tiene $\mathrm{Re}(s) = 1/2$ (Proposición 1.1). Por tanto,
$$\mathrm{Re}[L(e^{i\theta})] = \log|F(e^{i\theta})| = \log|\xi(\tau(e^{i\theta}))| = \log|\xi(1/2 + it_\theta)|$$
donde $t_\theta$ es el valor de $t$ tal que $\tau(e^{i\theta}) = 1/2 + it_\theta$.

La condición $\mathrm{Re}[L(e^{i\theta})] \geq 0$ para todo $\theta$ sería equivalente a $|\xi(1/2 + it)| \geq 1$ para todo $t \in \mathbb{R}$.

### 3.2. Fracaso de la condición en los ceros de $\xi$

La función $\xi(1/2+it)$ tiene infinitos ceros reales $t = \gamma_n > 0$ (los imaginarios de los ceros de Riemann sobre la recta crítica, cuya existencia y densidad son conocidas). En cada cero $\gamma_n$, $\xi(1/2+i\gamma_n) = 0$, y por tanto $|\xi(1/2+i\gamma_n)| = 0$, lo que da
$$\mathrm{Re}[L(e^{i\theta_n})] = \log 0 = -\infty,$$
donde $\theta_n = 2\pi + 2\arctan(2\gamma_n)$ (o el ángulo correspondiente a $z_n = \tau(\rho_n)$).

**Proposición 3.1.** *La condición $\mathrm{Re}[L(e^{i\theta})] \geq 0$ para todo $\theta$ es necesariamente falsa. En particular, es falsa en cada $\theta_n$ correspondiente a un cero de $\xi$ en la recta crítica (incondicionalmente, sin asumir ni negar RH).*

**Conclusión.** El enfoque de demostrar RH mediante la positividad de la parte real de $L$ en la circunferencia unidad no puede funcionar: esta positividad es falsa independientemente de RH. La presencia de ceros de $\xi$ exactamente sobre $|z| = 1$ (que es precisamente lo que RH predice) garantiza que $L$ no puede ser continua en la frontera, mucho menos no-negativa.

---

## §4. La condición correcta: no-ceros en el interior del disco

### 4.1. Reformulación via la función $L$ en el interior

La condición correcta de Nevanlinna no es sobre la frontera sino sobre el interior del disco:

**Proposición 4.1.** *Si $F$ no tiene ceros en $\{|z| < 1\}$, entonces $L(z) = \log F(z)$ está bien definida como función analítica en $\{|z| < 1\}$, y $F(z) = e^{L(z)}$ en el disco.*

Obsérvese que no se afirma que $\mathrm{Re}[L(z)] \geq 0$ en el interior; se afirma solo que $L$ es analítica (es decir, que $F$ es sin ceros). La positividad de $\mathrm{Re}[L]$ en el interior sería la condición mucho más fuerte $|F(z)| \geq 1$ para $|z| < 1$, que no es consecuencia de RH.

### 4.2. La función de Carathéodory asociada

Sea $dm_{\xi}$ la medida (positiva, de Borel) en la circunferencia unidad definida por
$$dm_{\xi}(e^{i\theta}) = |\xi(1/2 + it_\theta)|^2 \cdot \left|\frac{dt}{d\theta}\right| d\theta,$$
donde $t_\theta$ es la parametrización de la recta crítica introducida en §1.3. La función de Carathéodory de esta medida es
$$C_\xi(z) = \int_{|w|=1} \frac{w+z}{w-z}\, dm_{\xi}(w), \qquad |z| < 1.$$
Por el teorema de Herglotz, $\mathrm{Re}[C_\xi(z)] \geq 0$ para todo $|z| < 1$ incondicionalmente, ya que $dm_{\xi}$ es una medida positiva.

Sin embargo, la función de Carathéodory $C_\xi$ no coincide con $L(z) = \log F(z)$; son objetos distintos.

**Proposición 4.2.** *RH es equivalente a que $F(z)$ no tenga ceros en $\{|z| < 1\}$. Esta condición de no-ceros es una condición de tipo "clase de Nevanlinna" sobre $F$ en el disco, pero no es equivalente a ninguna condición de positividad simple de $\mathrm{Re}[L(z)]$ en el interior del disco.*

*Demostración.* La equivalencia con RH es la Proposición 2.1. Para la segunda parte: la condición $\mathrm{Re}[L(z)] \geq 0$ en $|z|<1$ equivaldría a $|F(z)| \geq 1$ en el disco, que es mucho más fuerte que la no-anulación. Basta notar que $|F(0)| = |\xi(0)| = 1/2 < 1$, lo que refuta $|F(z)| \geq 1$ en $z = 0$ incondicionalmente. $\square$

---

## §5. Conexión con los polinomios ortogonales en la circunferencia unidad (OPUC)

### 5.1. El formalismo de Schur-Simon

Los polinomios ortogonales en la circunferencia unidad (OPUC) asociados a una medida positiva $d\mu$ en $\{|z|=1\}$ satisfacen la recursión de Szegő con coeficientes de reflexión (coeficientes de Schur) $\alpha_k \in \mathbb{C}$. La condición de admisibilidad OPUC es siempre $|\alpha_k| \leq 1$; la condición $|\alpha_k| < 1$ estrictamente equivale a que la medida sea absolutamente continua con densidad estrictamente positiva a.e.

**Observación 5.1.** Para la medida $d\mu = dm_\xi$ definida en §4.2, los coeficientes de Schur $\alpha_k$ satisfacen automáticamente $|\alpha_k| \leq 1$. Que sean estrictamente menores que 1 equivale a que $|\xi(1/2+it)| > 0$ para casi todo $t$, lo cual es cierto incondicionalmente (los ceros de $\xi$ son un conjunto discreto, de medida cero).

**Por tanto, la condición $|\alpha_k| < 1$ es automática y no implica RH.**

### 5.2. La distinción correcta: polos versus ceros

La equivalencia relevante en OPUC no es sobre los coeficientes de Schur de la medida $dm_\xi$, sino sobre la función de Schur (o función de Carathéodory) de la medida y la localización de sus polos en el disco. Pero los polos de la función de Carathéodory de $dm_\xi$ corresponden a masa puntual en la circunferencia (posibles ceros de $\xi$ en la recta crítica con multiplicidad infinita), no a los ceros de $F$ en el interior del disco. El formalismo OPUC no captura directamente la condición de no-ceros de $F$.

### 5.3. Lo que falta

Para conectar OPUC con RH de manera no circular, sería necesario identificar una medida $d\mu$ natural para la cual:

(a) Los coeficientes de Schur $\alpha_k$ estén relacionados de manera concreta y calculable con la función $F(z)$ o con los ceros de $\xi$.

(b) La condición $|\alpha_k| < 1$ (u otra condición sobre los $\alpha_k$) sea equivalente, de manera no trivial, a la no-anulación de $F$ en el disco.

Hasta la fecha, tal identificación no ha sido establecida en este programa.

---

## §6. Propiedades de $\xi$ independientes de la posición de sus ceros

### 6.1. La pregunta

¿Existe alguna propiedad de $\xi$ que sea verificable sin conocer la posición de sus ceros y que implique la no-anulación de $F$ en $\{|z|<1\}$?

### 6.2. Propiedades conocidas de $\xi$

La función $\xi$ satisface las siguientes propiedades conocidas incondicionalmente:
- Es entera de orden 1.
- Satisface $\xi(s) = \xi(1-s)$ (ecuación funcional).
- Tiene el producto de Hadamard $\xi(s) = \xi(0) \prod_\rho (1 - s/\rho) e^{s/\rho}$, donde el producto corre sobre todos los ceros no triviales $\rho$ y converge absolutamente.
- $\xi(s) > 0$ para $s$ real, $0 < s < 1$ (en la "franja crítica" real).
- El argumento $S(T) = (1/\pi)\arg\xi(1/2+iT)$ satisface $S(T) = O(\log T)$.
- Los ceros son simétricos respecto a $s = 1/2$ y respecto a $\mathbb{R}$ (ya que $\xi$ es real en la recta real).

### 6.3. Por qué no bastan para forzar la no-anulación en el disco

Todas estas propiedades son compatibles con la existencia de ceros de $\xi$ fuera de la recta crítica (asumiendo que RH sea falsa). En particular:
- El producto de Hadamard tiene el mismo aspecto formal con o sin ceros off-critical; la no-anulación en $\mathrm{Re}(s) < 1/2$ (equivalentemente, de $F$ en $|z|<1$) no se deduce de la forma del producto.
- La ecuación funcional simetría los ceros respecto a la recta $\mathrm{Re}(s) = 1/2$ pero no los fuerza a estar sobre ella.
- El crecimiento (orden 1, género 1) es compatible con ceros distribuidos arbitrariamente en la franja $0 < \mathrm{Re}(s) < 1$.

**Proposición 6.1.** *Ninguna de las propiedades listadas en §6.2 implica individualmente (ni en combinación, hasta donde se conoce) que $F(z)$ no tenga ceros en $\{|z| < 1\}$.*

### 6.4. Una posible vía: ecuaciones diferenciales o funcionales de $F$

Si $F(z)$ satisfaciera una ecuación diferencial ordinaria de primer orden sin puntos singulares en $\{|z| \leq 1\}$ que forzara a las soluciones a ser no-nulas, o una ecuación funcional de contracción en el disco, podría deducirse la no-anulación sin referencia directa a los ceros de $\xi$. Sin embargo:

- La función $\xi(s)$ no satisface ninguna ecuación diferencial lineal de coeficientes polinomiales (a diferencia de las funciones hipergométricas o las funciones de Bessel). Esto es consecuencia de que $\xi$ no es una función de tipo $D$-módulo algebraico.

- La ecuación funcional $\xi(s) = \xi(1-s)$ se traduce, en términos de $F$, en $F(z) = F(\tau'(z))$ para cierta involucion $\tau'$ del disco, pero esta simetría no restringe la localización de ceros más allá de lo establecido en §2.

La búsqueda de tal ecuación diferencial o funcional para $F$ constituye una dirección abierta para la Fase 35.

---

## §7. El obstáculo central: circularidad de la reformulación

### 7.1. La reformulación exacta

La Proposición 2.1 establece con exactitud:
$$\text{RH} \iff F(z) = \xi(z/(z-1)) \text{ no tiene ceros en } \{|z| < 1\}.$$
Esta equivalencia es exacta, sin pérdida de información y sin hipótesis adicionales. Es una reformulación completamente fiel de RH.

### 7.2. El círculo vicioso

Para probar la no-anulación de $F$ en el disco $\{|z|<1\}$ se necesita controlar la posición de los ceros de $\xi$ en $\{\mathrm{Re}(s) < 1/2\}$, lo cual es precisamente RH. No existe, hasta la fecha, ningún argumento que pruebe la no-anulación de $F$ en $\{|z|<1\}$ sin probar esencialmente RH.

Más precisamente: cualquier argumento que demostrara que $F$ no tiene ceros en $\{|z|<1\}$ sería por construcción una demostración de RH, pero un argumento que lo demostrara mediante propiedades "más simples" o "más accesibles" de $F$ constituiría un avance real. El obstáculo no es la circularidad lógica (toda demostración de RH es en ese sentido circular), sino la ausencia de propiedades de $F$ que sean (a) verificables sin conocer los ceros, y (b) suficientes para la no-anulación.

### 7.3. Comparación con los Caminos 1 y 3

El Camino 1 (OPUC-Jacobi) reformula RH como la condición $a_k^{full} = a_k^\infty$ para todo $k$; análogamente, esto es exacto pero no se sabe demostrar. El Camino 3 (DBN-CCM) reformula RH como $T_\lambda = 0$ para todo $\lambda$; también exacto, pero la cancelación requerida parece necesitar información sobre los ceros. El Camino 2 se suma a esta lista: reformulaciones exactas, sin progreso hacia una prueba.

---

## §8. Síntesis y preguntas abiertas para la Fase 35

### 8.1. Imagen limpia del Camino 2

El Camino 2 produce la siguiente estructura:

- $F(z) = \xi(z/(z-1))$ es analítica en $\{|z| < 1\}$.
- $F(0) = \xi(0) = 1/2$ (en particular, $|F(0)| = 1/2 < 1$).
- Los ceros de $F$ en $|z|=1$ corresponden exactamente a los ceros de $\xi$ en la recta crítica (bajo RH, todos los ceros están aquí).
- RH $\iff$ $F$ no tiene ceros en $\{|z| < 1\}$ (Proposición 2.1).
- La condición de positividad $\mathrm{Re}[L(e^{i\theta})] \geq 0$ en la frontera es incorrecta (Proposición 3.1).
- La condición de Herglotz $\mathrm{Re}[C_\xi(z)] \geq 0$ en el interior es automática (§4.2) y no implica RH.
- Los coeficientes de Schur de $dm_\xi$ son automáticamente en el disco unitario cerrado (§5.1) y no implican RH.

### 8.2. Preguntas abiertas

**P1.** ¿Satisface $F(z)$ alguna ecuación diferencial o funcional cuyas soluciones sean automáticamente sin ceros en el disco, como consecuencia de la estructura de $\xi$?

**P2.** ¿Existe una medida $d\mu$ en la circunferencia unidad, construida a partir de $\xi$ sin referencia explícita a sus ceros, tal que la función de Carathéodory de $d\mu$ esté directamente relacionada con $F$ y capture la condición de no-anulación?

**P3.** ¿El producto de Hadamard de $\xi$, al ser transferido al disco mediante $\tau$, da un producto de Blaschke finito o infinito cuya convergencia imponga restricciones sobre la localización de sus factores?

**P4.** La condición de Li, $\lambda_n \geq 0$ para todo $n$, es equivalente a RH y está relacionada con las derivadas de $L(z)$ en $z=0$ (ver Docs 75, 78). ¿Puede la no-negatividad de los $\lambda_n$ deducirse de propiedades de $F$ en el disco sin pasar por la posición de los ceros?

Estas cuatro preguntas definen el espacio de trabajo del Camino 2 en la Fase 35.

---

## Apéndice: Verificación de la Proposición 1.1

Para mayor claridad, damos la verificación directa de que $|z| < 1 \implies \mathrm{Re}(\tau(z)) < 1/2$.

Sea $z = x+iy \in \mathbb{C}$ con $|z| < 1$, es decir, $x^2 + y^2 < 1$. Calculamos:
$$\tau(z) = \frac{z}{z-1} = \frac{(x+iy)}{(x-1)+iy} = \frac{(x+iy)\overline{((x-1)+iy)}}{|(x-1)+iy|^2} = \frac{(x+iy)((x-1)-iy)}{(x-1)^2+y^2}.$$
El numerador real es $x(x-1) + y^2 = x^2 - x + y^2$. Por tanto,
$$\mathrm{Re}(\tau(z)) = \frac{x^2 + y^2 - x}{(x-1)^2 + y^2}.$$
La condición $\mathrm{Re}(\tau(z)) < 1/2$ equivale a $2(x^2 + y^2 - x) < (x-1)^2 + y^2$, es decir, $2x^2 + 2y^2 - 2x < x^2 - 2x + 1 + y^2$, es decir, $x^2 + y^2 < 1$. Esto es exactamente la condición $|z| < 1$. $\square$

---

*Doc 81 completado. Próximo: Fase 35, exploración de las Preguntas P1–P4.*
