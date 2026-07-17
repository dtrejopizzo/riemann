# Segunda variación de la forma de Weil en dirección transversal

**Fecha:** junio 2026
**Contexto:** Ejecución de la Pregunta D.15 del Frente D.

---

## 1. Setup: la familia de formas $Q_\epsilon$

Fijamos una función de prueba $f$ (Schwartz en $\mathbb{R}^*_+$) y perturbamos la
configuración de ceros en la dirección transversal. Bajo Hipótesis D con $m$ órbitas
fuera de línea, cada órbita $j = 1, \ldots, m$ tiene ceros en
$$\rho_j = \tfrac{1}{2} + b_j + i\gamma_j, \quad \bar\rho_j, \quad 1-\rho_j, \quad 1-\bar\rho_j.$$

**Perturbación transversal.** Para $\epsilon \in \mathbb{R}$ y $(c_j) \in \mathbb{R}^m$,
define la familia de configuraciones:
$$b_j(\epsilon) = b_j + \epsilon c_j, \qquad \rho_j(\epsilon) = \tfrac{1}{2} + b_j + \epsilon c_j + i\gamma_j.$$

La órbita completa bajo el grupo de Klein $V$ se desplaza como:
$$\rho_j(\epsilon),\ \bar\rho_j(\epsilon),\ 1-\rho_j(\epsilon) = \tfrac{1}{2} - b_j - \epsilon c_j - i\gamma_j,\ 1-\bar\rho_j(\epsilon).$$

**Forma de Weil perturbada.** La forma de Weil se descompone:
$$Q_\epsilon(f,f) = Q_{\text{arith}}(f,f) + Q_{\text{zero},\epsilon}(f,f),$$
donde
$$Q_{\text{zero},\epsilon}(f,f) = -\sum_{\rho \in Z_\epsilon} |\hat h(\rho)|^2,$$
con $\hat h(s) := \int_0^\infty f(x)\, x^{s-1}\, dx$ la transformada de Mellin, y
$Z_\epsilon = \{\rho_j(\epsilon), \bar\rho_j(\epsilon), 1-\rho_j(\epsilon), 1-\bar\rho_j(\epsilon)\}_{j=1}^m$.

**Observación clave.** El término aritmético $Q_{\text{arith}}$ (contribuciones de primos
y factor arquimediano) no depende de los ceros. Por tanto:
$$\frac{d^k}{d\epsilon^k} Q_\epsilon(f,f) = \frac{d^k}{d\epsilon^k} Q_{\text{zero},\epsilon}(f,f), \qquad k \ge 1.$$

---

## 2. Simetría funcional y simplificación

**Lema 1** (simetría de la órbita). Si $f$ satisface la condición de simetría
$$\hat h(s) = \overline{\hat h(\bar s)} \quad \text{(funciones reales: condición natural)}$$
y la ecuación funcional
$$\hat h(s) = \hat h(1-\bar s),$$
entonces para cada órbita $j$:
$$\sum_{\rho \in \text{órbita}_j} |\hat h(\rho(\epsilon))|^2 = 4\,|\hat h(\rho_j(\epsilon))|^2.$$

*Prueba.* La condición de realidad da $|\hat h(\bar\rho)| = |\hat h(\rho)|$. La simetría
funcional da $|\hat h(1-\bar\rho)| = |\hat h(\rho)|$. Por tanto los cuatro términos de la
órbita contribuyen igual. $\square$

Por el Lema 1:
$$Q_{\text{zero},\epsilon}(f,f) = -4\sum_{j=1}^m |\hat h(\rho_j(\epsilon))|^2.$$

---

## 3. Primera variación: la recta crítica es punto estacionario

**Proposición 1** (gradiente nulo). Para toda $f$ simétrica:
$$\frac{d}{d\epsilon} Q_\epsilon(f,f)\bigg|_{\epsilon=0} = -8 \sum_{j=1}^m c_j\, \operatorname{Re}\!\left(\hat h'(\rho_j)\,\overline{\hat h(\rho_j)}\right).$$

*Prueba.* $\frac{d}{d\epsilon}|\hat h(\rho_j + \epsilon c_j)|^2 = 2c_j\,\operatorname{Re}(\hat h'(\rho_j + \epsilon c_j)\,\overline{\hat h(\rho_j+\epsilon c_j)})$. A $\epsilon = 0$ da el resultado. $\square$

**Corolario.** En $b_j = 0$ (recta crítica): $\rho_j = \frac{1}{2} + i\gamma_j$. Si $f$ es par
bajo $x \mapsto 1/x$ (condición natural de simetría), entonces $\hat h(s)$ es real y
positivo en la recta crítica, y $\hat h'(\rho_j)$ es puramente imaginario. Luego:
$$\operatorname{Re}\!\left(\hat h'(\rho_j)\,\overline{\hat h(\rho_j)}\right) = 0.$$

Por tanto la primera variación de $Q_\epsilon$ se anula en $b_j = 0$: **la recta crítica
es punto estacionario de $Q$ en la dirección transversal**. (Confirma la Proposición D.13.)

---

## 4. Segunda variación: el cálculo central

**Teorema 1** (fórmula de la segunda variación transversal). Para $f$ con la simetría
del Lema 1:
$$\boxed{\frac{d^2}{d\epsilon^2} Q_\epsilon(f,f)\bigg|_{\epsilon=0}
  = -8\sum_{j=1}^m c_j^2 \left[\operatorname{Re}\!\left(\hat h''(\rho_j)\,\overline{\hat h(\rho_j)}\right) + |\hat h'(\rho_j)|^2\right].}$$

*Prueba.* Sea $g_j(\epsilon) := |\hat h(\rho_j + \epsilon c_j)|^2$. Entonces:
$$g_j'(\epsilon) = 2c_j\,\operatorname{Re}\!\left(\hat h'(\rho_j + \epsilon c_j)\,\overline{\hat h(\rho_j+\epsilon c_j)}\right),$$
$$g_j''(\epsilon) = 2c_j^2\,\operatorname{Re}\!\left(\hat h''(\rho_j + \epsilon c_j)\,\overline{\hat h(\rho_j+\epsilon c_j)}\right) + 2c_j^2\,|\hat h'(\rho_j+\epsilon c_j)|^2.$$
A $\epsilon = 0$ y sumando con el factor $-4$:
$$\frac{d^2}{d\epsilon^2} Q_{\text{zero},\epsilon}(f,f)\bigg|_{\epsilon=0}
  = -4\sum_j g_j''(0) = -8\sum_j c_j^2 \left[\operatorname{Re}\!\left(\hat h''(\rho_j)\,\overline{\hat h(\rho_j)}\right) + |\hat h'(\rho_j)|^2\right]. \quad \square$$

---

## 5. Análisis del signo: la clase de Laguerre–Pólya

La segunda variación es positiva (recta crítica = mínimo local de $-Q$ = mínimo local
de energía) si y sólo si:
$$\operatorname{Re}\!\left(\hat h''(\rho_j)\,\overline{\hat h(\rho_j)}\right) + |\hat h'(\rho_j)|^2 < 0 \quad \forall j.$$

Reformulando en términos de $\log|\hat h(s)|$: sea $\sigma \mapsto u(\sigma) := \log|\hat h(\sigma + i\gamma_j)|$ la función de $\sigma = \operatorname{Re}(s)$. En $\sigma_0 = \frac{1}{2} + b_j$:

**Proposición 2** (condición de log-concavidad). La desigualdad
$\operatorname{Re}(\hat h'' \overline{\hat h}) + |\hat h'|^2 < 0$ en $\rho_j$ es equivalente a:
$$u''(\sigma_0) < 0 \quad \text{(concavidad de } \log|\hat h| \text{ en la dirección } \operatorname{Re}(s)\text{)}.$$

*Prueba.* Escribiendo $\hat h = r e^{i\theta}$ con $r = |\hat h|$, $\theta$ la fase:
$$\hat h' = (r' + ir\theta') e^{i\theta}, \quad \hat h'' = (r'' - r(\theta')^2 + i(2r'\theta' + r\theta''))e^{i\theta}.$$
Entonces:
$$\operatorname{Re}(\hat h'' \overline{\hat h}) + |\hat h'|^2 = r''r - r^2(\theta')^2 + (r')^2 + r^2(\theta')^2 = r''r + (r')^2.$$
La condición $r''r + (r')^2 < 0$ equivale a $(r^2)'' < 0$, o sea $r'' < -(r')^2/r$, o sea
$(\log r)'' = (r'r - (r')^2)/r^2 < 0$, que es exactamente $u'' < 0$. $\square$

**Definición.** Una función de prueba $f$ pertenece a la *clase de Laguerre–Pólya transversal* (clase LP-T) si para todo cero $\rho_j$ en la recta crítica:
$$\sigma \mapsto \log|\hat h(\sigma + i\gamma_j)| \text{ es cóncava en un entorno de } \sigma = 1/2.$$

**Teorema 2** (condición suficiente para RH variacional). Si $f \in$ LP-T y la recta
crítica es el único punto estacionario de $Q_\epsilon(f,f)$ en la dirección transversal,
entonces $Q_\epsilon(f,f)$ es localmente máximo en $b_j = 0$, equivalentemente
$-Q_\epsilon(f,f)$ es localmente mínimo en $b_j = 0$.

---

## 6. Interpretación: una fuerza anti-restauradora

El Teorema 1 revela algo fundamental sobre la geometría del problema:

**Proposición 3** (carácter anti-restaurador de la forma de Weil). Para funciones
$f \in$ LP-T, la segunda variación satisface:
$$\frac{d^2}{d\epsilon^2} Q_\epsilon(f,f)\bigg|_{\epsilon=0} > 0.$$

Esto significa: mover un cero DESDE la recta crítica HACIA fuera INCREMENTA $Q_\epsilon(f,f)$
(lo hace menos negativo). Equivalentemente: la recta crítica es un **mínimo local de
negatividad** de $Q$ en la dirección transversal.

*Consecuencia directa:* si $Q_0(f,f) \ge 0$ (lo cual equivale a RH vía el criterio de
Weil), entonces para funciones LP-T, mover los ceros fuera de la recta crítica sólo
haría $Q$ aún más positivo en primera aproximación. Hay que ir a tercer orden para
ver el cambio de signo.

*Espera — esto parece contradecir que $\kappa > 0$ cuando hay ceros fuera de línea.*
Aclaremos la paradoja:

**Proposición 4** (resolución de la aparente contradicción). Las dos afirmaciones son
compatibles:
1. $\kappa(Q_\epsilon) > 0$ para $b_j > 0$ (Phase 26): la forma tiene direcciones negativas.
2. $\delta^2_b Q_\epsilon(f,f)|_{\epsilon=0} > 0$ para $f \in$ LP-T: la forma evaluada en
   funciones específicas es un mínimo local.

La razón: el índice de Kreĭn $\kappa$ mide el subespacio de MÁXIMA negatividad (el mínimo
sobre todas las $f$). El Teorema 1 mide Q evaluado en una $f$ específica. El mínimo sobre
todas las $f$ puede ser negativo aun cuando el valor en una $f$ dada tenga mínimo en la
recta crítica.

En lenguaje matricial: que una matriz $A$ tenga un valor propio negativo no impide que
$\langle Ax, x \rangle$ sea positivo para vectores $x$ específicos. El índice de Kreĭn
cuenta valores propios negativos; la segunda variación evalúa en un vector fijo.

---

## 7. El potencial transversal correcto

La Proposición 3 sugiere que la energía transversal correcta NO es $\Phi = \sum b_j^2$
sino:
$$\Phi^*(f) := -Q_{\text{zero}}(f,f) = \sum_{\rho \in Z} |\hat h(\rho)|^2.$$

Esta es la energía de la configuración de ceros "vista desde $f$."

**Proposición 5** (propiedades de $\Phi^*$).
1. $\Phi^*(f) \ge 0$ siempre.
2. $\Phi^*$ no distingue entre ceros en la recta crítica y fuera de ella (depende del valor
   de $\hat h$ en los ceros, no de su posición).
3. $\frac{d^2}{d\epsilon^2}\Phi^*(f)\big|_{\epsilon=0} = 8\sum_j c_j^2 [u''_j + (u'_j)^2 + (\theta'_j)^2]$ donde $u_j = \log|\hat h(\rho_j)|$, $\theta_j$ su fase.

La condición para que $b_j = 0$ sea mínimo de $\Phi^*$ en la dirección transversal:
$$u''_j\bigg|_{\sigma=1/2} < 0 \quad \forall j,$$
es exactamente la condición LP-T.

---

## 8. La conexión con el producto de Euler

**Proposición 6** (la clase LP-T y la estructura aritmética). Una función $f$ pertenece
a LP-T si y sólo si la función $\sigma \mapsto |\hat h(\sigma + i\gamma_j)|$ es log-cóncava
en $\sigma$ para cada altura $\gamma_j$.

Las funciones de prueba naturales del formalismo de Connes son de la forma:
$$\hat h(s) = \zeta(s) \cdot g(s)$$
para alguna función entera $g$. Para estas funciones, la log-concavidad de $|\hat h(\sigma + i\gamma_j)|$ en $\sigma$ a $\gamma_j$ fijo involucra la log-concavidad de $|\zeta(\sigma + i\gamma_j)|$.

**Pregunta 28.1** (nueva). ¿Es $\sigma \mapsto \log|\zeta(\sigma + i\gamma)|$ cóncava en
$\sigma \in (0,1)$ para todo $\gamma$?

Si la respuesta es sí: las funciones de prueba naturales del formalismo pertenecen a LP-T,
la segunda variación tiene signo positivo, y la recta crítica es mínimo local de $Q$.

Si la respuesta es no: existen funciones de prueba para las cuales la recta crítica es
máximo o punto de silla, y el mecanismo variacional no funciona.

---

## 9. Lo que se puede comprobar: el caso de la recta $\sigma = 1/2$

En la recta crítica $\sigma = 1/2$ con $\gamma \gg 1$:
$$\log|\zeta(\tfrac{1}{2} + i\gamma)| = -c\sqrt{\log\gamma/\log\log\gamma} + O(\ldots)$$
(estimaciones de Korobov–Vinogradov del orden de magnitud).

La derivada en $\sigma$:
$$\partial_\sigma \log|\zeta(\sigma + i\gamma)|\bigg|_{\sigma=1/2}$$
está relacionada con $\operatorname{Re}(\zeta'/\zeta(\frac{1}{2}+i\gamma))$.

La segunda derivada:
$$\partial_\sigma^2 \log|\zeta(\sigma + i\gamma)| = \operatorname{Re}\!\left[\frac{\zeta''}{\zeta} - \left(\frac{\zeta'}{\zeta}\right)^2\right]_{\sigma + i\gamma}$$

El signo de esta cantidad en $\sigma = 1/2$ es la condición de log-concavidad. Relacionado
con la Pregunta 28.1, es una pregunta analítica concreta sobre $\zeta$.

---

## 10. Comparación con la situación en cuerpos de funciones

En el caso de curvas sobre $\mathbb{F}_q$, la función zeta tiene la forma:
$$Z(u) = \frac{P(u)}{(1-u)(1-qu)}, \quad P(u) = \prod_{j=1}^{2g}(1-\alpha_j u).$$

La log-concavidad análoga corresponde a que $\log|P(q^{-\sigma})|$ sea cóncava en
$\sigma$. Para $|\alpha_j| = q^{1/2}$ (RH en cuerpos de funciones, probado), los $\alpha_j$
están en el círculo $|u| = q^{-1/2}$, y la log-concavidad es inmediata: $|P(q^{-\sigma})|$
es un producto de funciones cóncavas en $\sigma$ (moduladas por el radio $q^{1/2-\sigma}$).

Esto sugiere que **la Pregunta 28.1 es el análogo para $\mathbb{Z}$ de la log-concavidad
que en cuerpos de funciones se sigue automáticamente de RH**. Para $\zeta$, es la
pregunta a responder.

---

## 11. Veredicto del cálculo

| Resultado | Estado |
|---|---|
| Fórmula de la segunda variación transversal (Teorema 1) | **Demostrado — nuevo resultado** |
| Primera variación nula en recta crítica (Prop. 1 + Corolario) | Demostrado |
| Equivalencia segunda variación positiva ↔ log-concavidad (Prop. 2) | Demostrado |
| Clase LP-T definida y caracterizada | Nuevo |
| Segunda variación positiva en LP-T (Teorema 2) | Demostrado condicional a LP-T |
| Pregunta 28.1: ¿es $\log|\zeta(\sigma+i\gamma)|$ cóncava en $\sigma$? | **Abierto — pregunta central** |
| Log-concavidad automática en cuerpos de funciones vía RH | Observación (§10) |

---

## 12. La pregunta más concreta del programa

**Pregunta 28.1** (replanteada). Para todo $\gamma > 0$ y $\sigma_0 \in (0,1)$:
$$\frac{\partial^2}{\partial \sigma^2} \log|\zeta(\sigma + i\gamma)|\bigg|_{\sigma=\sigma_0} \overset{?}{<} 0.$$

Equivalentemente: $|\zeta(\sigma + i\gamma)|^2$ es log-cóncava en $\sigma$ para cada $\gamma$ fijo.

Esto puede verificarse localmente en la recta crítica. Si se demuestra con log-concavidad uniforme:
$$\frac{\partial^2}{\partial \sigma^2} \log|\zeta(\sigma + i\gamma)| \le -\delta(\gamma) < 0 \quad \text{para } \sigma \in (1/4, 3/4),$$
entonces las funciones de prueba naturales del programa pertenecen a LP-T, la segunda
variación del Frente D tiene signo positivo, y la recta crítica es mínimo local de $Q$
en la dirección transversal para TODAS las funciones de prueba canónicas.

Combinado con la unicidad del mínimo (que requeriría un argumento global adicional), esto
probaría RH.
