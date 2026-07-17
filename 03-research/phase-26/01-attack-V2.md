# Phase 26-A — Ataque directo a V.2: el corazón del puente

**Fecha:** junio 2026
**Tesis:** V.2 no es un ítem de verificación. Es el objetivo principal de Phase 26.

Si V.2 cae, el puente no existe en la forma propuesta.
Si V.2 sobrevive, Phase 26 se convierte en una dirección seria.

---

## 0. La pregunta precisa de V.2

Sea $\rho_j = (1/2 + b_j) + i\gamma_j$ un cero de $\zeta$ fuera de la línea crítica ($b_j > 0$).

**V.2:** Existe un vector $f_j$ en el espacio de Kreĭn $\mathcal{K}$ tal que $H_C f_j = \lambda_j f_j$
con $\lambda_j \in \mathbb{C}$, $\text{Im}(\lambda_j) \neq 0$, y $\lambda_j$ determinado por $\rho_j$.

El candidato natural para $f_j$ es el carácter $f_j(x) = x^{\rho_j - 1/2} = x^{b_j + i\gamma_j}$.

---

## 1. La prueba de estrés: V.2 sin mencionar RH

Antes de conectar con $\zeta$ y $\rho_j$, formulamos la pregunta abstracta:

**Pregunta abstracta (V.2-abs):** Sea $(\mathcal{K}, Q)$ un espacio de Pontryagin con
neg.ind$(Q) = \kappa < \infty$ y sea $T$ un operador $Q$-autoadjunto en $\mathcal{K}$. ¿Tiene
$T$ exactamente $\kappa$ pares de eigenvalores no-reales $\{\mu_j, \bar\mu_j\}$?

**Respuesta conocida:** El teorema espectral de Kreĭn–Langer (1963, 1978) da:

> $T$ tiene **a lo sumo** $\kappa$ pares de eigenvalores no-reales.

La cuenta exacta NO es automática desde la teoría abstracta.

**Consecuencia directa para Phase 26:**

- El puente obtiene la dirección "a lo sumo 2m eigenvalores complejos" de forma automática.
- La dirección "exactamente 2m" requiere estructura específica del operador $H_C$ y del espacio $\mathcal{K}$.

Esta distinción es crucial: la desigualdad abstracta es gratis; la igualdad es el trabajo real.

---

## 2. El teorema de Kreĭn–Langer aplicado a $H_C$

**Teorema 26-A.1** (Kreĭn–Langer, cf. Azizov–Iokhvidov 1989, §2.3). Sea $T$ un operador
$Q$-autoadjunto en un espacio de Pontryagin $(\mathcal{K}, Q)$ con neg.ind$(\mathcal{K}) = \kappa$.
Entonces:

**(i)** El espectro no-real de $T$ consiste en a lo sumo $\kappa$ pares de eigenvalores complejos
$\{\mu_j, \bar\mu_j\}_{j=1}^{r}$ con $r \leq \kappa/2$.

**(ii)** El espectro esencial $\sigma_{ess}(T) \subseteq \mathbb{R}$.

**(iii)** Los eigenvectores asociados a $\mu_j$ y $\bar\mu_j$ son $Q$-ortogonales entre sí y
al espectro real.

**Corolario 26-A.2.** Si el Teorema Puente (Conjetura 26-C.2) se cumple, entonces
automáticamente la cota $r \leq m$ (número de órbitas fuera de línea).

*La dirección difícil es $r \geq m$: que existan AL MENOS $m$ pares de eigenvalores no-reales.*

---

## 3. El obstáculo para "exactamente $\kappa$"

Para probar $r = m$ (igual en lugar de a lo sumo), necesitamos:

**Para cada órbita $j = 1, \ldots, m$:**

Existe $f_j \in \mathcal{K}$ tal que $H_C f_j = \lambda_j f_j$ con $\text{Im}(\lambda_j) \neq 0$.

Este $f_j$ necesita:
1. **Estar en $\mathcal{K}$** (en el espacio de Pontryagin definido por $Q$).
2. **Ser eigenvetor genuino** (no solo generalized eigenfunction, no solo resonancia).
3. **Tener eigenvalor determinado por $\rho_j$** (la conexión con el cero de $\zeta$).

---

## 4. El obstáculo central: los caracteres NO están en $L^2(C_\mathbb{Q})$

El candidato natural $f_j(x) = x^{b_j + i\gamma_j}$ (un carácter de $\mathbb{R}^*_+$) satisface
formalmente:
$$(H_C f_j)(x) = -ix\partial_x(x^{b_j + i\gamma_j}) = -i(b_j + i\gamma_j) x^{b_j + i\gamma_j}
= (\gamma_j - ib_j) f_j(x).$$

Con la convención de Connes donde los ceros en línea aparecen como $\rho - 1/2 = i\gamma$ (puramente
imaginario), el eigenvalor $\lambda_j = \gamma_j - ib_j$ tiene $\text{Im}(\lambda_j) = -b_j \neq 0$.
Consistente.

**Pero $f_j \notin L^2(C_\mathbb{Q})$.**

*Demostración.* Sobre $\mathbb{R}^*_+$ con medida $dx/x$:
$$\|f_j\|_{L^2}^2 = \int_0^\infty |x^{b_j + i\gamma_j}|^2 \frac{dx}{x} = \int_0^\infty x^{2b_j} \frac{dx}{x}
= \int_0^\infty x^{2b_j - 1} dx = \infty.$$

El carácter no tiene decaimiento y no es cuadrado-integrable. $\square$

**Consecuencia:** $f_j$ es una función generalizada (distribución), no un vector de $L^2(C_\mathbb{Q})$.
En la teoría de operadores clásica, esto corresponde a espectro continuo (no eigenvalor).

---

## 5. Dos estrategias de resolución

### Estrategia A: Completado distribucional

Definir $\mathcal{K}$ no como $L^2(C_\mathbb{Q})$ con producto interno $Q$, sino como una extensión distribucional
que incluye los caracteres $f_j$ como vectores (en el sentido de Gel'fand–Shilov: una tripleta
rigged de Hilbert).

*Precisión:* Sea $\Phi \subset L^2(C_\mathbb{Q}) \subset \Phi'$ una tripleta rigged donde:
- $\Phi$ = funciones de prueba con decaimiento rápido sobre $C_\mathbb{Q}$,
- $\Phi'$ = distribuciones temperadas sobre $C_\mathbb{Q}$.

Si $f_j \in \Phi'$, entonces el par $(\Phi, Q)$ puede tener un completado de Pontryagin que incluye a $f_j$.

**Obstáculo:** La forma $Q$ en $\Phi'$ involucra la fórmula de Weil con todos sus términos (suma
sobre ceros + suma sobre primos), y su extensión distribucional necesita regularización cuidadosa.

### Estrategia B: Localización de Weil

No trabajar con $f_j$ como vector global, sino con su "proyección localizada":
$$f_j^{(T_0, \sigma)}(x) = f_j(x) \cdot \phi_{T_0, \sigma}(x)$$
donde $\phi_{T_0, \sigma}$ es una función de corte centrada cerca de $\gamma_j$ (una ventana de
Hermite-Gauss del programa principal).

$f_j^{(T_0, \sigma)} \in L^2(C_\mathbb{Q})$ si $\phi_{T_0, \sigma}$ tiene decaimiento suficiente.

**Pregunta:** ¿Es $f_j^{(T_0, \sigma)}$ un "aproximado de eigenvetor" de $H_C$ con eigenvalor
cerca de $\gamma_j - ib_j$?

Es decir: ¿$(H_C - (\gamma_j - ib_j))f_j^{(T_0, \sigma)} \to 0$ en alguna norma cuando $\sigma \to \infty$?

Esta pregunta conecta Phase 26 con el programa principal (la forma de Weil localizada del arc principal).

---

## 6. Lo que la forma $Q$ dice sobre $f_j$

**Cálculo de $Q(f_j, f_j)$ (formal).** Por definición:
$$Q(f_j, f_j) = \mathcal{W}(f_j * \tilde{f}_j).$$

La convolución de Mellin $f_j * \tilde{f}_j$ tiene transformada de Mellin:
$$\widehat{f_j * \tilde{f}_j}(s) = \hat{f}_j(s) \cdot \hat{\tilde{f}}_j(s).$$

Con $f_j(x) = x^{b_j + i\gamma_j}$:
$$\hat{f}_j(s) = \int_0^\infty x^{b_j+i\gamma_j} x^{s-1} dx.$$
Esta integral diverge (no hay decaimiento). Formalmente, si se regulariza:
$$\hat{f}_j(s) \sim \delta(s - (b_j + i\gamma_j)) \quad (\text{en sentido distribucional}).$$

Entonces:
$$\mathcal{W}(f_j * \tilde{f}_j) \sim \sum_\rho \hat{f}_j(\rho) \hat{\tilde{f}}_j(\rho) \sim \sum_\rho \delta(\rho - (b_j+i\gamma_j)) \cdot \overline{\delta(\rho - (b_j+i\gamma_j))}.$$

El término dominante es $\rho = \rho_j = (1/2+b_j)+i\gamma_j$:

$$Q(f_j, f_j) \sim |\hat{f}_j(\rho_j)|^2 = |\delta(\rho_j - (b_j+i\gamma_j))|^2.$$

El argumento: $\rho_j - (b_j + i\gamma_j) = 1/2 \neq 0$ (no hay cancelación).

**Observación técnica:** El cero de $\zeta$ en $\rho_j$ aparece en la suma $\sum_\rho$ de $\mathcal{W}$,
pero el carácter $f_j$ está centrado en $b_j + i\gamma_j$, que difiere de $\rho_j$ por $1/2$.

En la parametrización de Connes donde el operador de escalado actúa por $s \to s - 1/2$, la
diferencia desaparece. La convención correcta es:

$$f_j(x) = x^{\rho_j - 1/2} = x^{b_j + i\gamma_j} \quad \text{(en la línea central } s = 1/2\text{)}.$$

Con esta convención: $\hat{f}_j(s) \sim \delta(s - \rho_j)$ en la parametrización adélica.

Entonces $\mathcal{W}(f_j * \tilde{f}_j)$ recoge el término $\rho = \rho_j$ de la suma, que es
$|\hat{f}_j(\rho_j)|^2$. Pero $\hat{f}_j(\rho_j) = \int_0^\infty x^{b_j+i\gamma_j} x^{\rho_j-1} dx
= \int_0^\infty x^{\rho_j-1/2+\rho_j-1}dx$ — que diverge.

**Conclusión del cálculo formal:** $Q(f_j, f_j)$ está formalmente divergente. El carácter $f_j$
es un vector **isótropo-distribucional** — no en el sentido $Q(f_j,f_j)=0$, sino en el sentido
de que la forma $Q$ no está bien definida sobre $f_j$ en el espacio $L^2$.

---

## 7. Diagnóstico preciso de la obstaculización

El obstáculo tiene tres capas:

**Capa 1 (fácil):** El teorema de Kreĭn–Langer da "a lo sumo $\kappa$" automáticamente.
No hay nada que demostrar aquí dado que $H_C$ es $Q$-simétrico.

**Capa 2 (difícil):** Para "al menos $\kappa$", necesitamos que los caracteres $f_j$ sean
eigenvectores genuinos de $H_C$ en alguna extensión de $L^2(C_\mathbb{Q})$ que incluya a $f_j$.

**Capa 3 (fundamental):** Los caracteres $f_j$ NO están en $L^2(C_\mathbb{Q})$ y la forma $Q$ no
está bien definida sobre ellos. La extensión distribucional es el problema técnico central.

---

## 8. La reformulación correcta de V.2

La Estrategia A (completado distribucional) sugiere la siguiente reformulación:

**V.2 reformulado:** Sea $\mathcal{K}^+ = (\Phi', Q_{reg})$ la extensión distribucional del
espacio de Pontryagin $\mathcal{K}$, donde $Q_{reg}$ es la regularización de la forma de Weil
sobre distribuciones. Entonces:

**(a)** Los caracteres $f_j = x^{\rho_j - 1/2}$ están en $\mathcal{K}^+$.

**(b)** $H_C f_j = \lambda_j f_j$ en $\mathcal{K}^+$ con $\lambda_j = \gamma_j - ib_j$.

**(c)** $Q_{reg}(f_j, f_j)$ es finito (posiblemente 0, dando un vector isótropo).

Esto requiere:
1. Definir $Q_{reg}$ rigurosamente sobre distribuciones temperadas.
2. Verificar que el completado $\mathcal{K}^+$ hereda el índice de Kreĭn $\kappa$.
3. Calcular $H_C f_j$ y $Q_{reg}(f_j, f_j)$ explícitamente.

---

## 9. La conexión con el arc principal del programa

La Estrategia B (localización) sugiere que V.2 está directamente conectado a los resultados
de v8/v9 del arc principal:

**La forma localizada de Weil** $Q_{T_0, \sigma, J}$ del arc principal es (formalmente) la
compresión de $Q$ a una base de Hermite-Gauss centrada en $T_0 = \gamma_j$, ancho $\sigma$.

Si $\sigma \to \infty$ (base completa), la compresión converge a $Q$ completa.

El eigenvector localizado $f_j^{(T_0, \sigma)}$ debería satisfacer:
$$Q_{T_0, \sigma, J}(f_j^{(T_0,\sigma)}, \cdot) \approx \lambda_j Q_{T_0,\sigma,J}(\cdot, \cdot).$$

Este es precisamente el comportamiento que el arc principal mide numéricamente: la negatividad
$\lambda_{\min}(Q_{T_0, \sigma, J}) < 0$ cuando existe un cero fuera de línea cerca de $T_0$.

**Hipótesis de trabajo:** el eigenvector $f_j$ (en el sentido distribucional) es el límite de
los vectores localizados $f_j^{(T_0, \sigma)}$ cuando $\sigma \to \infty$, y la negatividad de
$\lambda_{\min}(Q_{T_0, \sigma, J})$ es la "huella localizada" del eigenvalor complejo $\lambda_j$
de $H_C$ en $\mathcal{K}^+$.

Esta hipótesis, si se formaliza, conectaría directamente el arc principal y el arc Kreĭn.

---

## 10. Estado y veredicto de V.2

| Componente | Estado |
|---|---|
| "A lo sumo κ eigenvalores no-reales" (Kreĭn–Langer) | **Disponible gratis** si $H_C$ es $Q$-simétrico |
| Candidato a eigenvector $f_j = x^{b_j+i\gamma_j}$ | Candidato identificado; NO en $L^2(C_\mathbb{Q})$ |
| Eigenvalor $\lambda_j = \gamma_j - ib_j$ | Correcto formalmente; requiere convención precisa |
| $Q(f_j, f_j)$ bien definido | Divergente en $L^2$; requiere regularización o extensión |
| "Al menos κ eigenvalores no-reales" | **NO demostrado; requiere completado distribucional** |
| Conexión con arc principal | Hipótesis de trabajo; no formalizada |

**Veredicto:** V.2 NO puede ser clasificado como "ítem técnico de verificación". Es el objetivo
principal de Phase 26-A. Los obstáculos son reales (extensión distribucional de $Q$, no-$L^2$ de $f_j$)
y no son circunvenciones menores.

**El camino más directo a V.2:**

1. Definir la regularización $Q_{reg}$ sobre distribuciones temperadas (siguiendo Weil/Burnol).
2. Verificar que los caracteres $f_j = x^{b_j+i\gamma_j}$ tienen $Q_{reg}(f_j, f_j) < \infty$.
3. Calcular $H_C f_j$ en el sentido distribucional.
4. Si pasos 2–3 son exitosos: V.2 está demostrado para la extensión distribucional.
5. Si paso 2 falla (divergencia): el puente requiere reformulación (Estrategia B — localización).

---

## 11. Qué queda después de V.2

Si V.2 se prueba con la Estrategia A (completado distribucional):

- V.1 ($Q$-simetría de $H_C$) pasa a ser el problema siguiente. También requiere trabajo real.
- V.3 (índice de Kreĭn = κ) es consecuencia del teorema de Kreĭn–Langer + V.2.
- V.4 (cuenta de órbitas) es algebraica una vez que V.2 y V.3 estén disponibles.

Si V.2 falla:

- El puente en la forma del Teorema 26-C.2 es incorrecto.
- Diagnóstico: la conexión Kreĭn ↔ Connes requiere la forma localizada (Estrategia B).
- Reformulación: el arc principal (v8/v9) ES el arc de Pontryagin en versión local.

Ninguno de los dos resultados es un fracaso. Ambos son precisos.
