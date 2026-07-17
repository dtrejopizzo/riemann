# Doc 91 — Dirección B: Espacio de Pontryagin e índice negativo de $H_C$

**Fecha:** junio 2026  
**Fase:** 34 — Nuevas direcciones  
**Contexto:** Bloqueo de la dirección CCM (barrera de Hadamard, Doc 88–90); exploración de la Dirección B basada en teoría de operadores en espacios de Pontryagin/Kreĭn.  
**Regla absoluta:** No se fabricará ninguna prueba de RH. Si un argumento no cierra, se dirá explícitamente.

---

## Resumen ejecutivo

La Dirección B busca probar $\mathrm{neg.ind}(H_C) = 0$ mediante herramientas de la teoría de operadores en espacios de Pontryagin, sin requerir conocimiento previo de las posiciones de los ceros de $\zeta$. Este documento:

1. Reconstruye rigurosamente el espacio de Pontryagin $(\mathcal{K}, Q)$ y el operador $H_C$ de Phase 26.
2. Revisa los teoremas de Pontryagin, Kreĭn–Langer y Azizov–Iokhvidov relevantes.
3. Analiza la simetría funcional de $\zeta$ como restricción espectral sobre $H_C$.
4. Estudia la semiacotación inferior como ruta al índice negativo cero.
5. Examina el análogo de la función característica de Livsic en espacios de Pontryagin.
6. Formula el obstáculo preciso que bloquea cada ruta.
7. Concluye con una evaluación honesta de si existe una ruta genuinamente nueva.

**Resultado principal del análisis:** Cada ruta conocida en la Dirección B se reduce a una condición equivalente al conocimiento de los ceros de $\zeta$ (directamente o vía la barrera de cuadrado-raíz del Opt-B). La Dirección B no está bloqueada en principio, pero ninguna herramienta estándar de la teoría de Pontryagin/Kreĭn cierra el argumento sin asumir información equivalente a RH.

---

## Parte I — Construcción del espacio de Pontryagin $(\mathcal{K}, Q)$

### Sección 1.1 — El espacio ambiente y la forma de Weil

Sea $\mathcal{S}(\mathbb{R}^*_+)$ el espacio de Schwartz de funciones de prueba sobre $\mathbb{R}^*_+ = (0,\infty)$ con medida multiplicativa $dx/x$. Para $f \in \mathcal{S}(\mathbb{R}^*_+)$ se define la transformada de Mellin:
$$\hat{f}(s) = \int_0^\infty f(x) x^s \frac{dx}{x}, \qquad s \in \mathbb{C}.$$

La **función de completación de $\zeta$** es:
$$\xi(s) = \frac{1}{2} s(s-1) \pi^{-s/2} \Gamma(s/2) \zeta(s),$$
que satisface la ecuación funcional $\xi(s) = \xi(1-s)$ y es entera de orden 1.

**Definición 1.1 (Forma de Weil–Connes).** Para $f, g \in \mathcal{S}(\mathbb{R}^*_+)$, la forma lineal de Weil es:
$$\mathcal{W}(h) = \sum_\rho \hat{h}(\rho) + \hat{h}(0) \left(\frac{1}{2}\log\pi - \frac{\gamma}{2}\right) + \hat{h}(1)\left(\frac{1}{2}\log\pi - \frac{\gamma}{2}\right) - \sum_{p \text{ primo}} \sum_{n=1}^\infty \frac{\log p}{p^{n/2}} \left[ h(p^n) + h(p^{-n}) \right],$$
donde $\rho$ recorre los ceros no triviales de $\zeta$, $\gamma$ es la constante de Euler–Mascheroni, y la suma sobre primos converge condicionalmente en el sentido de Schwartz.

En notación más compacta (cf. Weil 1952, Connes 1999):
$$\mathcal{W}(h) = \sum_{\rho} \hat{h}(\rho) - \sum_p \sum_{n \geq 1} \frac{\log p}{p^{n/2}} \left[h(p^n) + h(p^{-n})\right] + (\text{términos archimedianos}),$$
donde los términos archimedianos provienen del factor gamma.

**Definición 1.2 (Forma cuadrática de Weil).** La forma hermitiana en $\mathcal{S}(\mathbb{R}^*_+)$ es:
$$Q(f, g) = \mathcal{W}(f \star \tilde{g}),$$
donde la convolución multiplicativa es $(f \star g)(x) = \int_0^\infty f(y) g(x/y) dy/y$ y el adjunto multiplicativo es $\tilde{g}(x) = \overline{g(1/x)} / x$.

**Observación 1.3.** La transformada de Mellin de $f \star \tilde{g}$ es $\hat{f}(s) \overline{\hat{g}(\bar{s})}$, de modo que:
$$Q(f,g) = \sum_\rho \hat{f}(\rho) \overline{\hat{g}(\bar\rho)} - \sum_{p,n} \frac{\log p}{p^{n/2}} (f \star \tilde{g})(p^n) + (\text{archim.}).$$

---

### Sección 1.2 — El teorema de Weil y el índice de Kreĭn

El resultado fundamental de Weil (1952) en lenguaje moderno es:

**Teorema 1.4 (Weil 1952, Connes 1999).** $Q(f,f) \geq 0$ para toda $f \in \mathcal{S}(\mathbb{R}^*_+)$ si y solo si la Hipótesis de Riemann es verdadera.

Este teorema convierte la positividad de $Q$ en una reformulación de RH. Nuestro interés es cuantificar el grado de no-positividad cuando RH es desconocida.

**Definición 1.5 (Índice negativo de la forma).** Sea $V$ un espacio vectorial con forma hermitiana $Q$. El **índice negativo** de $Q$ es:
$$\kappa(Q) = \sup \left\{ \dim W : W \subset V, \, Q|_W < 0 \right\},$$
donde $Q|_W < 0$ significa que la forma restringida es definida negativa.

**Proposición 1.6 (Conexión con ceros de $\zeta$).** Si $\zeta$ tiene exactamente $m$ órbitas de ceros fuera de la línea crítica (bajo la simetría $s \mapsto 1-\bar{s}$, cada órbita contiene 4 ceros, pero la ecuación funcional $\xi(s)=\xi(1-s)$ reduce la cuenta a $2m$ pares conjugados), entonces:
$$\kappa(Q) = 2m.$$

En particular, $\kappa(Q) = 0 \iff \text{RH}$.

*Indicación de prueba.* Cada cero $\rho_j = \sigma_j + i\gamma_j$ con $\sigma_j \neq 1/2$ contribuye un par $\{\rho_j, 1-\rho_j\}$ (por la ecuación funcional, con $1-\rho_j = (1-\sigma_j) + i\gamma_j$) y también $\{\bar\rho_j, 1-\bar\rho_j\}$ (por reflexión). La convolución $f_j \star \tilde{f}_j$ tiene transformada de Mellin que toca estos ceros. Un cálculo de residuos (cf. Burnol 2002) muestra que cada par de ceros fuera de línea produce exactamente una dirección negativa de $Q$. La demostración rigurosa requiere el análisis distribucional de $\mathcal{W}$ sobre test functions que aproximan caracteres, y está incompleta en el marco actual de Phase 26 (ver ítem V.2 de Phase 26). $\square$ (parcial)

---

### Sección 1.3 — Construcción del espacio de Pontryagin

Para pasar de la forma $Q$ en $\mathcal{S}(\mathbb{R}^*_+)$ a un espacio de Pontryagin, se necesitan tres pasos.

**Paso 1: El subespacio isotrópico.** Sea $N = \ker Q = \{f \in \mathcal{S} : Q(f,g) = 0 \; \forall g\}$ el subespacio de vectores $Q$-degenerados. Se conjetura (resultado pendiente de Phase 26) que $\dim N < \infty$.

**Paso 2: El espacio cociente.** Sea $\mathcal{S}/N$ el espacio cociente. La forma $Q$ desciende a una forma no-degenerada $\tilde{Q}$ en $\mathcal{S}/N$.

**Paso 3: La completación.** Sea $(\mathcal{K}, Q)$ la completación de $(\mathcal{S}/N, \tilde{Q})$ en el sentido de la topología canónica de un espacio de Pontryagin. Esta completación existe y es única (módulo isometría unitaria) cuando el índice negativo es finito, por el teorema de Iokhvidov–Kreĭn (1956).

**Definición 1.7 (Espacio de Pontryagin de Weil–Connes).** El **espacio de Pontryagin de Weil–Connes** es el par $(\mathcal{K}, Q)$ construido mediante los tres pasos anteriores, con índice negativo:
$$\kappa = \kappa(Q) = \mathrm{neg.ind}(\mathcal{K}).$$

**Advertencia 1.8.** La construcción de $\mathcal{K}$ como espacio de Pontryagin genuino (es decir, la verificación de que el índice negativo es finito, $\kappa < \infty$) es equivalente a que $\zeta$ tenga solo finitos ceros fuera de la línea crítica. Este hecho no está demostrado. Por lo tanto, en todo el documento trabajamos **bajo la hipótesis de trabajo** $\kappa < \infty$ (que es un resultado estrictamente más débil que RH pero también abierto).

---

### Sección 1.4 — El operador $H_C$

**Definición 1.9 (Operador de Connes–Weil).** Sea $C_\mathbb{Q} = \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ el grupo de clases de idèles del cuerpo $\mathbb{Q}$, donde $\mathbb{A}_\mathbb{Q}$ son los adèles. Sea $H = L^2(C_\mathbb{Q}, d\mu)$ con la medida de Haar $d\mu$.

El grupo $\mathbb{R}^*_+$ actúa isométricamente sobre $H$ por:
$$(U_\lambda f)(x) = f(\lambda^{-1} x), \quad \lambda \in \mathbb{R}^*_+, \; f \in H.$$

El **operador de Connes–Weil** $H_C$ es el generador infinitesimal de esta representación unitaria:
$$H_C = \frac{1}{i} \left.\frac{d}{d\lambda}\right|_{\lambda=1} U_\lambda.$$

Sobre funciones diferenciables: $(H_C f)(x) = -i x \partial_x f(x)$ (operador de Euler multiplicado por $-i$).

**Proposición 1.10 (Simetría formal de $H_C$ respecto a $Q$).** Si la acción de $U_\lambda$ preserva $Q$, es decir, $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ para todo $\lambda \in \mathbb{R}^*_+$, entonces $H_C$ es $Q$-simétrico: $Q(H_C f, g) = Q(f, H_C g)$ para $f, g$ en el dominio.

*Demostración.* Derivando $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ en $\lambda = 1$:
$$\frac{d}{d\lambda}\bigg|_{\lambda=1} Q(U_\lambda f, U_\lambda g) = Q\left(\frac{dU_\lambda}{d\lambda}\bigg|_{\lambda=1} f, g\right) + Q\left(f, \frac{dU_\lambda}{d\lambda}\bigg|_{\lambda=1} g\right) = 0.$$
Como $\frac{dU_\lambda}{d\lambda}|_{\lambda=1} = i H_C$, se obtiene $Q(iH_C f, g) + Q(f, iH_C g) = 0$, que es la $Q$-simetría. $\square$

**Estado del ítem V.1 (Phase 26).** La $Q$-invarianza de $U_\lambda$ (y por ende la $Q$-simetría de $H_C$) **no está demostrada**. Requiere verificar que la forma de Weil $\mathcal{W}(f \star \tilde{g})$ es invariante bajo el cambio de variable multiplicativo $f \mapsto U_\lambda f$. El término aritmético de $Q$ transforma los argumentos de evaluación en los primos: $(U_\lambda f \star \widetilde{U_\lambda g})(p^n) = (f \star \tilde{g})(\lambda^{-1} p^n)$, lo cual no es obvio que preserve $Q$.

**Definición 1.11 ($Q$-autoadjunto en $\mathcal{K}$).** Una vez que $\mathcal{K}$ está construido (como espacio de Pontryagin) y $H_C$ está definido densamente en $\mathcal{K}$, se dice que $H_C$ es **$Q$-autoadjunto** si:
1. $Q(H_C f, g) = Q(f, H_C g)$ para $f,g$ en el dominio (simetría), y
2. El operador es maximalmente $Q$-simétrico (no tiene extensiones $Q$-simétricas propias en $\mathcal{K}$).

En la teoría de Pontryagin, la condición (2) es automática para operadores con resolución no vacía, pero requiere verificación en cada caso concreto.

---

## Parte II — Teoremas de Pontryagin, Kreĭn y Langer

### Sección 2.1 — Espacios de Pontryagin: definición y propiedades básicas

**Definición 2.1 (Espacio de Pontryagin).** Un **espacio de Pontryagin de índice $\kappa$**, denotado $\Pi_\kappa$, es un espacio vectorial complejo $\mathcal{K}$ con forma hermitiana $Q$ no-degenerada tal que:
1. $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ (descomposición fundamental), con $\mathcal{K}_+, \mathcal{K}_-$ $Q$-ortogonales,
2. $(\mathcal{K}_+, Q)$ es un espacio de Hilbert,
3. $(\mathcal{K}_-, -Q)$ es un espacio de Hilbert,
4. $\dim \mathcal{K}_- = \kappa < \infty$.

**Teorema 2.2 (Unicidad de la descomposición fundamental, Pontryagin 1944).** En un espacio de Pontryagin $\Pi_\kappa$, toda descomposición fundamental $\mathcal{K} = \mathcal{K}_+ \oplus \mathcal{K}_-$ tiene $\dim \mathcal{K}_- = \kappa$. La descomposición no es única, pero su dimensión negativa sí lo es.

**Teorema 2.3 (Completitud, Iokhvidov–Kreĭn 1956).** Todo espacio de Pontryagin $\Pi_\kappa$ es completo respecto a cualquier norma de Hilbert asociada a una descomposición fundamental. Las diferentes normas son equivalentes.

**Proposición 2.4 (Vectores isótropos en $\Pi_\kappa$).** Un vector $v \in \mathcal{K}$ es **$Q$-isótropo** si $Q(v,v) = 0$. En $\Pi_\kappa$, el subespacio de vectores isótropos no tiene dimensión $> \kappa$. En particular, no existe un subespacio isótropo de dimensión $> \kappa$.

---

### Sección 2.2 — El teorema espectral de Pontryagin

**Teorema 2.5 (Pontryagin 1944).** Sea $T$ un operador $Q$-autoadjunto en $\Pi_\kappa$. Entonces $T$ tiene al menos $\kappa$ valores propios (contados con multiplicidad) cuya parte imaginaria es no nula, o bien tiene un subespacio invariante de dimensión $\kappa$ sobre el cual la forma $Q$ es negativa.

*Nota.* El enunciado original de Pontryagin es en dimensión finita. La generalización a dimensión infinita (espacios de Pontryagin) fue realizada por Kreĭn–Langer (1963, 1978) y Azizov–Iokhvidov (1978, 1989).

**Observación 2.6.** El Teorema 2.5 da una **cota inferior** sobre los valores propios no-reales. En contraste, el teorema que da la cota superior (a lo sumo $\kappa$ pares) también es de Kreĭn–Langer y se enuncia a continuación.

---

### Sección 2.3 — El teorema de Kreĭn–Langer

**Teorema 2.7 (Kreĭn–Langer, 1963; cf. Azizov–Iokhvidov 1989, §2.3).** Sea $T$ un operador $Q$-autoadjunto en un espacio de Pontryagin $\Pi_\kappa$. Entonces:

**(i) Espectro no-real.** El espectro no-real $\sigma(T) \setminus \mathbb{R}$ consiste en a lo sumo $\kappa$ pares de eigenvalores complejos conjugados $\{\mu_j, \bar\mu_j\}_{j=1}^{r}$ con $r \leq \kappa$, cada uno con multiplicidad algebraica finita.

**(ii) Espectro esencial real.** $\sigma_{\mathrm{ess}}(T) \subseteq \mathbb{R}$.

**(iii) $Q$-ortogonalidad espectral.** Los subespacios radiales de eigenvalores complejos distintos son $Q$-ortogonales entre sí y al espacio correspondiente al espectro real.

**(iv) Subespacio $\kappa$-dimensional invariante.** Existe un subespacio $L \subset \mathcal{K}$ con $\dim L = \kappa$, $T$-invariante, sobre el cual $Q|_L \leq 0$ (la forma es no-positiva).

**Corolario 2.8.** En el contexto de la Dirección B: si $H_C$ es $Q$-autoadjunto en $\Pi_\kappa$ con $\kappa = 2m$, entonces tiene a lo sumo $2m$ eigenvalores complejos (en pares conjugados). Esto da la cota $r \leq m$ sobre las órbitas de ceros fuera de línea.

**Observación 2.9 (Asimetría del teorema de Kreĭn–Langer).** El teorema da una cota superior gratuita. La igualdad $r = m$ (que vincula cada cero fuera de línea con un eigenvalor complejo de $H_C$) no se obtiene de la teoría abstracta y requiere estructura específica del operador. Ver ítem V.2 de Phase 26.

---

### Sección 2.4 — El teorema de descomposición de Langer y operadores definitizables

**Definición 2.10 (Operador definitizable).** Un operador $Q$-autoadjunto $T$ en $\Pi_\kappa$ es **definitizable** si existe un polinomio real $p(t) \neq 0$ tal que $Q(p(T)f, f) \geq 0$ para todo $f \in \mathcal{K}$.

**Teorema 2.11 (Langer, 1982).** Todo operador $Q$-autoadjunto con conjunto resolvente no vacío en $\Pi_\kappa$ es definitizable.

**Corolario 2.12.** Si $\rho(H_C) \neq \emptyset$, entonces $H_C$ es definitizable. El polinomio definitizante $p$ está relacionado con los eigenvalores no-reales: su grado es a lo sumo $2r$ donde $r$ es el número de pares de eigenvalores no-reales.

**Observación 2.13 (Relevancia para la Dirección B).** Si $H_C$ fuera definitizable con polinomio definitizante $p(t) = t^2 - c$ para algún $c > 0$, eso significaría $Q((H_C^2 - c)f, f) \geq 0$, lo cual es una condición espectral fuerte. La pregunta es si la estructura aritmética de $H_C$ fuerza algún polinomio definitizante específico.

---

### Sección 2.5 — Condiciones para índice negativo cero

El resultado central que buscamos es: ¿cuándo es $\kappa = 0$?

**Proposición 2.14.** Para un operador $Q$-autoadjunto $T$ en $\Pi_\kappa$, las siguientes condiciones son equivalentes:

*(a)* $\kappa = 0$ (el espacio es un espacio de Hilbert).

*(b)* $Q(f, f) \geq 0$ para todo $f \in \mathcal{K}$ (la forma es semidefinida positiva).

*(c)* $T$ no tiene eigenvalores con parte imaginaria no nula.

*(d)* El subespacio $\kappa$-dimensional invariante del Teorema 2.7(iv) puede tomarse con $Q|_L = 0$ (isótropo) y $L = \{0\}$.

*Demostración.* (a)$\iff$(b) es la definición de espacio de Hilbert entre espacios con forma hermitiana. (b)$\iff$(c): Si $Q \geq 0$ y $Tv = \mu v$ con $\text{Im}(\mu) \neq 0$, entonces por $Q$-autoadjunticidad: $Q(Tv, v) = \mu Q(v,v) = Q(v,Tv) = \bar\mu Q(v,v)$, luego $(\mu - \bar\mu) Q(v,v) = 0$, y como $\mu \neq \bar\mu$ se tiene $Q(v,v)=0$. Pero si $Q \geq 0$ y $Q(v,v) = 0$, entonces $v = 0$ (no hay vectores isótropos en espacio de Hilbert), contradicción. (c)$\Rightarrow$(b): por el teorema espectral, si no hay eigenvalores complejos y el espacio tiene índice $\kappa > 0$, existe el subespacio negativo del Teorema 2.7(iv), que contiene vectores con $Q < 0$. Contradicción con (c) si además usamos que $T$ tiene la propiedad de que en dicho subespacio actúa con eigenvalores reales por (b)... [El argumento completo requiere la teoría espectral de Langer para operadores definitizables. No lo cerramos aquí.] $\square$ (parcial)

**Corolario 2.15 (Clave para la Dirección B).** Para probar $\kappa = 0$ basta demostrar **una** de las siguientes:
- (S1) $Q(f,f) \geq 0$ para todo $f \in \mathcal{K}$ (positividad de Weil — equivalente a RH directamente).
- (S2) $H_C \geq c I$ respecto a $Q$ para algún $c > 0$ (semiacotación inferior uniforme respecto a $Q$).
- (S3) El espectro de $H_C$ está contenido en $\mathbb{R}$ (ausencia de eigenvalores complejos).
- (S4) El sistema de eigenvectores y vectores ciclicos de $H_C$ es $Q$-completo (base de Riesz en $\Pi_\kappa$).

Cada una de estas condiciones se analiza en las Partes III–V.

---

## Parte III — La ecuación funcional como restricción espectral

### Sección 3.1 — La simetría $s \mapsto 1-s$ sobre $H_C$

La ecuación funcional $\xi(s) = \xi(1-s)$ induce una simetría sobre el espectro de $H_C$. Precisamos esta relación.

**Definición 3.1.** Sea $J: \mathcal{K} \to \mathcal{K}$ el operador de **conjugación funcional** definido por:
$$(Jf)(x) = \overline{f(1/x)} / x, \quad x \in \mathbb{R}^*_+.$$

En términos de la transformada de Mellin: $\widehat{Jf}(s) = \overline{\hat{f}(1-\bar{s})}$.

**Proposición 3.2 (Propiedades de $J$).** El operador $J$ satisface:
1. $J^2 = I$ (involución).
2. $Q(Jf, Jg) = Q(f, g)$ (isometría respecto a $Q$, por la simetría $\xi(s) = \xi(1-s)$).
3. $JH_C = (I - H_C)J$ (relación de conmutación entre $J$ y $H_C$).

*Demostración de (3).* Sobre funciones de prueba, si $(H_C f)(x) = -ix\partial_x f(x)$, entonces:
$$(JH_C f)(x) = \overline{(H_C f)(1/x)} / x = \overline{(-i \cdot (1/x) \partial_x|_{x \to 1/x} f(1/x))} / x.$$
Con el cambio $y = 1/x$: $\partial_x f(1/x)|_{x} = -y^2 f'(y)$, luego $(H_C f)(1/x) = -i(1/x)(-x^2 f'(1/x)) = ix f'(1/x)$.
Por lo tanto $(JH_C f)(x) = \overline{ix f'(1/x)} / x = -i f'(1/x) = (H_C Jf)(x) \cdot (-1) + (Jf)(x)$... 

[El cálculo preciso depende de la convención sobre dominios y el peso de la medida. Lo relevante es la afirmación abstracta.] $\square$ (formal)

**Teorema 3.3 (Simetría espectral bajo la ecuación funcional).** Si $\lambda$ es eigenvalor de $H_C$ (en $\mathcal{K}$ o en una extensión distribucional adecuada), entonces $1 - \bar\lambda$ también es eigenvalor de $H_C$. En particular:
- Si $\lambda \in \mathbb{R}$, entonces $1 - \lambda \in \mathbb{R}$ también es eigenvalor.
- Si $\lambda \in \mathbb{C} \setminus \mathbb{R}$, entonces $\{1-\bar\lambda, \bar\lambda, 1-\lambda\}$ son eigenvalores adicionales.

*Demostración.* Si $H_C f = \lambda f$, entonces $H_C (Jf) = J(I - H_C) f = J f - J H_C f = J f - \lambda J f = (1-\lambda) Jf$. Por lo tanto $Jf$ es eigenvector para el eigenvalor $1-\lambda$. Tomando conjugados con la antilinealidad de $J$, se obtiene el eigenvalor $1 - \bar\lambda$. $\square$ (formal, asumiendo la relación (3) de la Proposición 3.2)

**Corolario 3.4 (Implicación para índice negativo).** La simetría espectral implica que los eigenvalores complejos de $H_C$ vienen en órbitas $\{\lambda, \bar\lambda, 1-\lambda, 1-\bar\lambda\}$ de tamaño 4 (cuando todos son distintos), a menos que $\lambda = 1/2$ o $\lambda \in \mathbb{R}$.

En el contexto de los ceros de $\zeta$: si $\rho = 1/2 + b + i\gamma$ es cero fuera de línea ($b \neq 0$), los cuatro elementos de la órbita son $\{1/2+b+i\gamma, 1/2+b-i\gamma, 1/2-b+i\gamma, 1/2-b-i\gamma\}$. En términos de eigenvalores de $H_C$ (con desplazamiento $s \to s - 1/2$): $\{b+i\gamma, b-i\gamma, -b+i\gamma, -b-i\gamma\}$.

Por la ecuación funcional, el índice negativo $\kappa = 2m$ es siempre **par**, y sus eigenvalores complejos vienen en cuartetas.

**Observación 3.5 (Lo que esto no da).** La simetría funcional impone restricciones sobre la forma de los eigenvalores complejos, pero **no implica que no existan**. Para probar $\kappa = 0$ (ausencia de eigenvalores complejos), necesitamos algo más que la simetría.

---

### Sección 3.2 — El subespacio de punto fijo y su relación con la línea crítica

**Proposición 3.6.** El subespacio de punto fijo de $J$ es:
$$\mathcal{K}_J = \{f \in \mathcal{K} : Jf = f\} = \{f : f(x) = \overline{f(1/x)}/x\}.$$

En términos de Mellin: $f \in \mathcal{K}_J$ iff $\hat{f}(s) = \overline{\hat{f}(1-\bar{s})}$, es decir, $\hat{f}$ es "real sobre la línea crítica $\mathrm{Re}(s) = 1/2$".

**Proposición 3.7.** La restricción de $H_C$ a $\mathcal{K}_J$ tiene espectro simétrico respecto a $1/2$ (en el sentido de que $\lambda$ es eigenvalor iff $1-\lambda$ lo es). Sobre la línea crítica, los eigenvalores del tipo $\lambda = 1/2 + i\gamma$ satisfacen $1 - \bar\lambda = 1/2 + i\gamma = \lambda$, de modo que son puntos fijos de la simetría espectral.

**Observación 3.8.** Los ceros de $\zeta$ en la línea crítica, en la parametrización $\rho = 1/2 + i\gamma_n$, corresponden (formalmente) a eigenvalores $\lambda_n = i\gamma_n$ de $H_C$ (con desplazamiento $s \to s - 1/2$), que son **puramente imaginarios**. Esto es consistente con la restricción $\mathrm{Re}(\lambda) = 0$ (o $\mathrm{Re}(\lambda) = 1/2$ sin desplazamiento). La simetría funcional no distingue entre ceros en línea y fuera de línea excepto en el tipo de órbita.

---

## Parte IV — Semiacotación inferior y el obstáculo de la raíz cuadrada

### Sección 4.1 — La condición de semiacotación inferior respecto a $Q$

**Definición 4.1 (Semiacotación inferior).** El operador $H_C$ es **$Q$-semiacotado inferiormente** si existe $c \in \mathbb{R}$ tal que:
$$Q(H_C f, f) \geq c \cdot Q(f, f) \quad \text{para todo } f \in \text{Dom}(H_C) \cap \mathcal{K}_+,$$
donde $\mathcal{K}_+$ es la componente positiva en la descomposición fundamental.

**Nota 4.2.** En un espacio de Pontryagin, la semiacotación inferior "respecto a $Q$" es más sutil que en un espacio de Hilbert, porque $Q$ no es positiva. La condición relevante para forzar $\kappa = 0$ es la semiacotación **respecto a la norma de Hilbert** de la descomposición fundamental, no respecto a $Q$ directamente.

**Proposición 4.3 (Semiacotación y ausencia de eigenvalores no-reales).** Si existe $c > 0$ tal que:
$$Q(H_C f, f) \geq c \quad \text{para todo } f \in \mathcal{K} \text{ con } Q(f,f) = 1,$$
entonces $H_C$ no tiene eigenvalores con $\mathrm{Re}(\lambda) < c$, y en particular no tiene eigenvalores no-reales con $\mathrm{Re}(\lambda) < c$.

*Demostración.* Si $H_C v = \lambda v$, entonces $Q(H_C v, v) = \lambda Q(v,v)$. Si $Q(v,v) = 1$ (normalizando), entonces $\lambda = Q(H_C v, v) \geq c$. Pero si $\lambda$ es complejo, $\lambda = Q(H_C v, v)$ sería real (por $Q$-autoadjunticidad), contradicción con $\lambda \notin \mathbb{R}$.

Más precisamente: para $v$ eigenvector con eigenvalor complejo $\lambda$, $Q(v,v)$ puede ser 0 (vectores isótropos). La condición sobre eigenvalores complejos requiere análisis por separado. $\square$ (parcial)

---

### Sección 4.2 — Conexión con la forma de Weil: la descomposición prima-archimédea

La forma $Q$ en $\mathcal{S}(\mathbb{R}^*_+)$ se descompone como:
$$Q(f,f) = Q_\infty(f,f) - Q_{\mathrm{prim}}(f,f),$$
donde el término archimédeo $Q_\infty$ proviene del factor gamma y es positivo semidefinido (para funciones en el semi-plano adecuado), y el término primo es:
$$Q_{\mathrm{prim}}(f,f) = 2 \sum_{p, n \geq 1} \frac{\log p}{p^{n/2}} \mathrm{Re}(f \star \tilde{f})(p^n).$$

**Proposición 4.4 (Forma archimédea como operador diferencial).** El término archimédeo $Q_\infty(f,f)$ corresponde a la acción del operador:
$$\hat{Q}_\infty(s) = \Omega(s) = \mathrm{Re}\,\psi\left(\frac{s}{2}\right) - \log\pi + \ldots$$
donde $\psi = \Gamma'/\Gamma$. En particular, $\Omega(s) \sim \frac{1}{2}\log|s|$ para $|s| \to \infty$ en la línea crítica.

**El obstáculo central (la barrera de raíz cuadrada).** Para la semiacotación inferior $Q \geq 0$ (equivalente a RH), necesitamos:
$$Q_\infty(f,f) \geq Q_{\mathrm{prim}}(f,f) \quad \forall f.$$

El término primo, a escala $N = e^{1/\varepsilon}$, tiene amplitud:
$$Q_{\mathrm{prim}} \sim 2 \sum_{n \leq N} \frac{\Lambda(n)}{\sqrt{n}} |(f \star \tilde{f})(\log n)| \sim 2\sqrt{N} \cdot \|f\|^2,$$
usando la estimación de Chebyshev $\sum_{n \leq N} \Lambda(n)/\sqrt{n} \sim 2\sqrt{N}$. En contraste, el término archimédeo crece como $\log N$.

**Proposición 4.5 (Barrera de $\sqrt{N}$ vs $\log N$).** La amplitud del término primo crece como $\sqrt{N}$ mientras que la del término archimédeo crece como $\log N$. Por lo tanto, sin cancelación entre los términos oscilatorios de $Q_{\mathrm{prim}}$, la semiacotación inferior $Q \geq 0$ falla.

*Observación 4.6 (La raíz de la dificultad).* La cancelación en $Q_{\mathrm{prim}}$ proviene de los signos oscilatorios de $(f \star \tilde{f})(p^n)$ cuando $f$ tiene transformada de Mellin concentrada en la línea crítica. Esta cancelación es la que codifica la distribución de los ceros de $\zeta$. Por lo tanto:

> La semiacotación inferior $Q \geq 0$ es **equivalente** a RH, y su prueba requiere controlar la cancelación en los términos primos, lo cual es el contenido de RH.

---

### Sección 4.3 — La estrategia de la cola prima (de Opt-B)

En el documento OPTION-B-pontryagin-index-attack.md del programa, se propone una estrategia más débil:

**Estrategia 4.7 (Cota relativa de forma — RFB$_X$).** Para un cutoff $X > 0$, separar $Q_{\mathrm{prim}} = Q_{\mathrm{prim}, \leq X} + Q_{\mathrm{prim}, > X}$. El primer término es de rango finito (finitos primos $\leq X$). Si para algún $X$:
$$|Q_{\mathrm{prim}, > X}(f,f)| \leq a \cdot Q_\infty(f,f) + C \|f\|^2, \quad a < 1,$$
entonces $Q$ es una perturbación de rango finito de una forma semiacotada inferiormente, lo que implica $\kappa < \infty$ (finitos ceros fuera de línea). Esto es más débil que RH pero también abierto.

**Proposición 4.8 (Estado de RFB$_X$).** La constante óptima $a_{\mathrm{tail}}(X) = \sup_f Q_{\mathrm{prim},>X}(f,f) / Q_\infty(f,f)$ satisface:
- $a_{\mathrm{tail}}(X) \leq 1$ (por los resultados N3 del programa, que establecen que el término primo completo no supera al archimédeo en $\ell^\infty$ relativo).
- Si $a_{\mathrm{tail}}(X) < 1$ para algún $X$ finito: $\kappa < \infty$ incondicionalmente.
- Si $a_{\mathrm{tail}}(X) \equiv 1$ para todo $X$: la estrategia no da $\kappa < \infty$.

La pregunta sobre si $a_{\mathrm{tail}}(X) < 1$ o $\equiv 1$ está **abierta** y es cuantitativa, no fácilmente reducible a propiedades conocidas de $\zeta$.

**Conclusión de la Sección 4.** La semiacotación inferior directa es equivalente a RH. La estrategia de la cola prima (RFB$_X$) podría dar $\kappa < \infty$ incondicionalmente, pero la constante $a_{\mathrm{tail}}$ está en el límite crítico $= 1$ según los resultados del programa. **Esta es la dirección más prometedora dentro de la Dirección B para obtener un resultado incondicional más débil que RH.**

---

## Parte V — La función característica de Livsic y su análogo en espacios de Pontryagin

### Sección 5.1 — La función característica de Livsic para operadores en espacios de Hilbert

En la teoría de operadores no autoadjuntos en espacios de Hilbert (Livsic 1946, Brodskii–Livsic 1958), la **función característica** de un operador $T$ con defecto finito es una función matricial analítica $\Theta_T(z)$ que codifica la parte no autoadjunta de $T$ y determina su estructura espectral hasta equivalencia unitaria.

Para un operador $T$ con "parte no autoadjunta de rango uno" (defecto nuclear):
$$\Theta_T(z) = I - 2i K^*(T - zI)^{-1} K,$$
donde $K$ es el operador de defecto. La función $\Theta_T$ satisface:
- $\Theta_T(z)^* \Theta_T(z) = I$ para $z$ en el espectro real de $T$ (isometría en el espectro real).
- Los eigenvalores no-reales de $T$ son los polos de $\Theta_T$.

**Conexión con $\zeta$.** En el contexto de Connes–Burnol, la función $\zeta$ misma (o más precisamente la función $\xi$) actúa como función característica de cierto operador de Dirac asociado a la dispersión adélica (Burnol 2002). Los ceros de $\xi$ corresponden a los polos del resolvente, y la no-autoadjunticidad del operador de Connes se codifica en la "parte dispersiva" de la función característica.

---

### Sección 5.2 — Análogo de la función característica en espacios de Pontryagin

En espacios de Pontryagin, la teoría de la función característica fue desarrollada por Livsic–Yantsevich (1979) y posteriormente por Alpay–Dijksma–Rovnyak–de Snoo (1997) en el contexto de operadores de Pontryagin con defecto.

**Definición 5.1 (Función característica en $\Pi_\kappa$).** Sea $T$ un operador $Q$-simétrico en $\Pi_\kappa$ con espacio de defecto de dimensión $d$. La **función característica** de $T$ es una función matricial analítica $\Theta_T^{(\kappa)}(z)$ de tamaño $d \times d$ con coeficientes racionales en $z$, que satisface:
$$\Theta_T^{(\kappa)}(z)^{[*]} \Theta_T^{(\kappa)}(z) = I$$
para $z$ en el espectro real de $T$, donde ${}^{[*]}$ denota el adjunto respecto a la forma $Q$ en el espacio de defecto.

La función característica en $\Pi_\kappa$ es una función **$J$-unitaria** (unitaria respecto a una forma indefinida), no unitaria ordinaria.

**Proposición 5.2 (Estructura de la función característica en $\Pi_\kappa$).** Las diferencias entre la función característica en $\Pi_\kappa$ y en el espacio de Hilbert son:
1. $\Theta_T^{(\kappa)}$ es una función $J$-unitaria: en lugar de $\Theta^*\Theta = I$, satisface $\Theta^{[*]} \Theta = I$ donde ${}^{[*]}$ involucra la forma indefinida.
2. $\Theta_T^{(\kappa)}$ puede tener polos en el eje real, correspondientes a eigenvalores "reales singulares" del operador.
3. El índice negativo $\kappa$ se refleja en el número de "singularidades indefinidas" de $\Theta_T^{(\kappa)}$.

**Teorema 5.3 (Livsic–Yantsevich, 1979; cf. Alpay et al. 1997).** Para un operador $T$ $Q$-autoadjunto en $\Pi_\kappa$ con espectro discreto:

**(i)** Los eigenvalores no-reales de $T$ son exactamente los polos de $\Theta_T^{(\kappa)}$ en $\mathbb{C} \setminus \mathbb{R}$.

**(ii)** El índice negativo $\kappa$ es igual al número de singularidades indefinidas de $\Theta_T^{(\kappa)}$ en $\mathbb{R}$ (contadas apropiadamente).

**(iii)** Si $\Theta_T^{(\kappa)}$ es analítica en $\mathbb{R}$ (sin singularidades reales), entonces $T$ es autoadjunto en el espacio de Hilbert (i.e., $\kappa = 0$).

---

### Sección 5.3 — Conexión con $\zeta$: la función $\xi$ como función característica

**Conjetura 5.4 (Identificación de Burnol–Connes).** La función:
$$\Theta_{H_C}^{(\kappa)}(z) = \frac{\xi(1/2 + z)}{\xi(1/2 - z)}$$
es (una versión de) la función característica del operador $H_C$ en el espacio de Pontryagin $(\mathcal{K}, Q)$.

*Justificación heurística.* La función $\xi(1/2 + z)/\xi(1/2 - z)$ es:
- Meromorfa en $\mathbb{C}$, con polos en $z = \rho - 1/2$ donde $\rho$ es cero de $\zeta$ fuera de línea (porque $\xi(\rho) = 0$ y $1/2 + z = \rho \Rightarrow z = \rho - 1/2$).
- Satisface $|\Theta_{H_C}^{(\kappa)}(iy)| = 1$ para $y \in \mathbb{R}$ en la línea imaginaria (por la ecuación funcional $|\xi(1/2 + iy)| = |\xi(1/2 - iy)|$ para $y$ real), es decir, es una función Blaschke-tipo en el semiplano derecho.
- Sus polos en $\mathbb{C} \setminus i\mathbb{R}$ corresponden exactamente a los ceros de $\zeta$ fuera de la línea crítica.

Bajo RH, los únicos ceros de $\xi$ tienen $\text{Re}(\rho) = 1/2$, es decir, $\text{Re}(z) = 0$: la función $\Theta_{H_C}^{(\kappa)}(z)$ no tiene polos en $\text{Re}(z) \neq 0$. Por el Teorema 5.3(iii), esto implicaría $\kappa = 0$.

**Proposición 5.5 (Lo que la función característica da y no da).** 
- **Lo que da:** Una conexión directa entre los ceros de $\xi$ y los eigenvalores complejos de $H_C$. Si la identificación de la Conjetura 5.4 es correcta, entonces el programa se reduce a estudiar los polos de $\xi(1/2+z)/\xi(1/2-z)$.
- **Lo que no da:** Un argumento para probar que estos polos están en $i\mathbb{R}$ sin conocer de antemano las posiciones de los ceros de $\zeta$. La función característica es un *reflejo* de la estructura espectral, no una herramienta independiente para determinarla.

**Observación 5.6 (Circularidad).** Demostrar que $\Theta_{H_C}^{(\kappa)}(z)$ es analítica en $\text{Re}(z) \neq 0$ es equivalente a demostrar que los ceros de $\xi$ tienen $\text{Re}(\rho) = 1/2$, que es exactamente RH. La función característica de Livsic no proporciona una palanca independiente para cerrar el argumento.

---

## Parte VI — Formulación del obstáculo preciso

### Sección 6.1 — El mapa de condiciones suficientes

Resumimos las condiciones que implicarían $\kappa = 0$, ordenadas por fuerza:

| Condición | Implica | Estado |
|-----------|---------|--------|
| C1: $Q(f,f) \geq 0$ para todo $f$ | $\kappa = 0$ directamente | Equivalente a RH |
| C2: $H_C \geq c I$ en $\mathcal{K}$ (norma Hilbert) | $\kappa = 0$ (por espectro en $[c, \infty)$) | Equivalente a RH |
| C3: Espectro de $H_C \subset i\mathbb{R}$ | $\kappa = 0$ por Kreĭn–Langer | Reformulación de RH |
| C4: $\Theta_{H_C}$ analítica en $\text{Re}(z) \neq 0$ | $\kappa = 0$ por Teorema 5.3(iii) | Equivalente a RH |
| C5: $a_{\mathrm{tail}}(X) < 1$ para algún $X$ | $\kappa < \infty$ (resultado más débil) | **Abierto, cuantitativo** |
| C6: $H_C$ definitizable con $p(t) = t$ | $\kappa = 0$ directamente | Implica C1 |
| C7: Sistema de eigenvectores completo con autovalores reales | $\kappa = 0$ (por argumento espectral) | Requiere base de Riesz en $\Pi_\kappa$ |

**Observación 6.1.** Las condiciones C1–C4 y C6 son todas directamente equivalentes a RH o la implican de manera que la prueba de la condición requiere tanto trabajo como la prueba de RH misma. La condición C5 es la única que podría dar un resultado incondicional.

---

### Sección 6.2 — Por qué la semiacotación inferior es difícil

**Proposición 6.2.** La semiacotación inferior $Q(f,f) \geq c \|f\|_{\mathcal{K}}^2$ (con $\|\cdot\|_{\mathcal{K}}$ la norma de Hilbert de la descomposición fundamental) es equivalente a RH más la acotación del error en el teorema de los números primos.

*Argumento.* La semiacotación inferior $Q \geq c\|\cdot\|^2$ requiere controlar la diferencia $Q_\infty - Q_{\mathrm{prim}} \geq c\|\cdot\|^2$. El término primo es:
$$Q_{\mathrm{prim}}(f,f) = 2\mathrm{Re} \int_0^\infty \hat{f}(1/2 + it) \overline{\hat{f}(1/2 + it)} \left( \sum_\gamma \delta(t - \gamma) \right) dt,$$
donde $\gamma$ recorre las partes imaginarias de los ceros en línea (bajo RH). El control de esta expresión requiere la distribución de los $\gamma_n$, que es equivalente a RH. $\square$ (esquemático)

---

### Sección 6.3 — El obstáculo de Hadamard en la Dirección B

**Definición 6.3 (Obstáculo de Hadamard en versión B).** Análogamente a la barrera CCM (Doc 88), el **obstáculo de Hadamard en la Dirección B** es:

> Ninguna propiedad de $Q$ o de $H_C$ que sea verificable a partir de propiedades globales de $\zeta$ (como sus propiedades de crecimiento, su ecuación funcional, o su producto de Euler) implica $\mathrm{neg.ind}(H_C) = 0$ sin pasar por el conocimiento de las posiciones de los ceros de $\zeta$ fuera de la línea crítica.

**Proposición 6.4 (Obstáculo en la Dirección B).** Sea $P$ cualquier propiedad de $H_C$ verificable a partir de:
- La ecuación funcional $\xi(s) = \xi(1-s)$,
- El producto de Euler $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ para $\text{Re}(s) > 1$,
- Estimaciones de crecimiento globales de $|\zeta(s)|$ en regiones alejadas de la línea crítica,

y ninguna información sobre las posiciones individuales de los ceros de $\zeta$. Entonces $P$ no implica $\mathrm{neg.ind}(H_C) = 0$.

*Argumento (no riguroso pero convincente).* El obstáculo de Hadamard establece que la positividad de Weil (condición C1) es "estrictamente más fuerte" que todas las propiedades globales verificables de $\zeta$. La Dirección B reformula C1 en términos espectrales de $H_C$, pero la dificultad subyacente persiste: el espectro de $H_C$ en $\Pi_\kappa$ está determinado precisamente por las posiciones de los ceros, y cualquier condición que fuerce el espectro a estar en $i\mathbb{R}$ está esencialmente asumiendo RH. El argumento completo es análogo al de la barrera de Hadamard en la dirección CCM (Doc 88). $\square$ (esquemático)

**Observación 6.5 (La excepción: C5).** La condición C5 ($a_{\mathrm{tail}}(X) < 1$) escapa parcialmente al obstáculo de Hadamard porque implica solo $\kappa < \infty$ (finitos ceros fuera de línea), no $\kappa = 0$ (RH). La barrera de Hadamard en su versión fuerte prohíbe concluir $\kappa = 0$, pero no excluye $\kappa < \infty$. Sin embargo, la constante $a_{\mathrm{tail}}$ está en el valor crítico $= 1$ según los resultados del programa.

---

## Parte VII — Análisis de nuevas rutas potenciales

### Sección 7.1 — Ruta vía la acción del grupo de Galois adélico

**Idea.** El grupo de clases de idèles $C_\mathbb{Q} = \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ tiene una estructura de grupo localmente compacto. La representación de $C_\mathbb{Q}$ en $\mathcal{K}$ podría imponer restricciones sobre los eigenvalores de $H_C$ que vayan más allá de la simetría funcional.

**Proposición 7.1 (La acción del grupo y el espectro).** Si una familia de operadores $\{V_a : a \in C_\mathbb{Q}\}$ actúa unitariamente en $(\mathcal{K}, Q)$ y conmuta con $H_C$, entonces el espectro de $H_C$ es invariante bajo la acción de $C_\mathbb{Q}$ (en algún sentido).

Sin embargo, la acción de $C_\mathbb{Q}$ es precisamente la que define $H_C$ (como generador infinitesimal), de modo que la $C_\mathbb{Q}$-invarianza del espectro es automática y no da información nueva sobre la posición de los eigenvalores.

**Conclusión.** La simetría del grupo $C_\mathbb{Q}$ no es una palanca nueva: está ya incorporada en la definición de $H_C$.

---

### Sección 7.2 — Ruta vía la teoría de representaciones de $\mathrm{GL}(1)$

**Idea.** En la teoría de formas automorfas, los operadores de Hecke actúan sobre espacios de formas modulares y tienen propiedades espectrales relacionadas con la función $L$ de la forma. ¿Puede trasladarse este marco al caso de $\zeta$?

**Para $\mathrm{GL}(1)$ sobre $\mathbb{Q}$**, la función $L$ relevante es $\zeta$ misma. Los operadores de Hecke $T_p$ actúan sobre el espacio de clases de idèles y tienen eigenvalores $p + 1/p$ (para la representación trivial) o $p^{it} + p^{-it}$ (para caracteres). Los eigenvalores de $H_C$ en la línea crítica son $i\gamma_n$ (puramente imaginarios), consistentes con los eigenvalores de los operadores de Hecke.

**Problema.** Para los ceros fuera de línea, los eigenvalores tendrían parte real no nula, lo cual es inconsistente con la interpretación como eigenvalores de operadores de Hecke unitarios. Pero esta inconsistencia **es** RH: los ceros fuera de línea son inconsistentes con la unitariedad de los operadores de Hecke, y la prueba de que no existen es equivalente a probar que $\zeta$ no tiene ceros fuera de la línea crítica.

**Conclusión.** La ruta vía operadores de Hecke es una reformulación de RH, no una nueva palanca.

---

### Sección 7.3 — Ruta vía operadores de Volterra y la integración por partes

**Idea.** En la teoría de operadores de Volterra en espacios de Hilbert, un operador de Volterra tiene espectro puntual vacío (espectro solo en 0). Si $H_C$ pudiera descomponerse como una perturbación compacta de un operador de Volterra, su espectro podría controlarse.

**Definición 7.2.** Una integral de Volterra sobre $\mathbb{R}^*_+$ tiene la forma:
$$(Vf)(x) = \int_0^x f(y) K(x,y) \frac{dy}{y},$$
con núcleo $K$ apropiado. En el caso de la función $\xi$, el núcleo está relacionado con la función de correlación de pares de ceros (Montgomery 1973).

**Proposición 7.3 (Obstrucción).** La descomposición $H_C = H_{\mathrm{Volterra}} + H_{\mathrm{resto}}$ requiere identificar una parte triangular de $H_C$. Pero $H_C = -ix\partial_x$ es un operador diferencial de primer orden, y su triangularidad (en alguna base) equivale a la existencia de funciones propias del operador de Euler — que son exactamente los caracteres $x^s$. Los valores de $s$ para los cuales estos son "admisibles" en $\mathcal{K}$ son los ceros de $\zeta$ fuera de línea. Circularidad nuevamente.

---

### Sección 7.4 — La pregunta de la completitud del sistema de eigenvectores

**Definición 7.3 (Sistema completo).** El sistema de eigenvectores y vectores cíclicos de $H_C$ es **$Q$-completo** en $\mathcal{K}$ si el subespacio cerrado generado por todos los eigenvectores y vectores cíclicos es todo $\mathcal{K}$.

**Teorema 7.4 (Completitud implica autoadjunticidad en $\Pi_\kappa$, bajo hipótesis).** Si el sistema de eigenvectores de un operador $Q$-autoadjunto $T$ en $\Pi_\kappa$ forma una base de Riesz de $\mathcal{K}$ (como espacio de Hilbert), y todos los eigenvalores son reales, entonces $T$ es autoadjunto en el espacio de Hilbert $\mathcal{K}$ y $\kappa = 0$.

*Observación 7.5.* El resultado anterior es circular en el siguiente sentido: la hipótesis de que todos los eigenvalores son reales es equivalente a afirmar que no hay eigenvalores complejos, lo cual es lo que queremos probar.

**Propuesta no-circular.** Una versión no-circular sería: demostrar la completitud del sistema de eigenvectores **sin** asumir que los eigenvalores son reales, y luego deducir de la completitud que no puede haber eigenvalores complejos.

**Proposición 7.6 (Obstrucción a la propuesta no-circular).** En general, un operador $Q$-autoadjunto en $\Pi_\kappa$ con $\kappa > 0$ puede tener un sistema completo de eigenvectores con eigenvalores complejos. La completitud no fuerza los eigenvalores a ser reales. Por lo tanto, la completitud del sistema de eigenvectores no implica $\kappa = 0$ sin hipótesis adicionales sobre los eigenvalores.

---

### Sección 7.5 — La ruta de la perturbación de rango finito

**Idea.** Si $H_C = H_0 + K$ donde $H_0$ es autoadjunto (en el sentido de Hilbert) con $\kappa_0 = 0$, y $K$ es de rango finito, entonces por el teorema de Weyl el espectro esencial no cambia, y el número de eigenvalores complejos de $H_C$ es a lo sumo igual al rango de $K$.

**Proposición 7.7.** Si existe una descomposición $H_C = H_0 + K$ con $H_0$ autoadjunto positivo en un espacio de Hilbert (con la métrica positiva asociada a la descomposición fundamental de $\Pi_\kappa$) y $K$ de rango finito igual a $\kappa$, entonces $\mathrm{neg.ind}(H_C) \leq \kappa$.

*Observación 7.8 (Problema).* La condición de rango de $K$ igual a $\kappa$ es exactamente la afirmación que queremos probar (que el índice negativo es finito y está controlado). No sabemos a priori cuál es el rango de $K$, y determinarlo requiere conocer $\kappa$, que requiere conocer los ceros fuera de línea.

---

### Sección 7.6 — Evaluación: ¿existe una ruta genuinamente nueva?

**Teorema 7.9 (Evaluación de la Dirección B).** No se ha encontrado ninguna ruta en la Dirección B que:
1. Use exclusivamente propiedades de $H_C$ derivables de propiedades globales de $\zeta$ (ecuación funcional, producto de Euler, crecimiento en el plano), Y
2. Implique $\mathrm{neg.ind}(H_C) = 0$.

Las rutas encontradas son:
- **C1–C4:** Equivalentes a RH.
- **C5 (RFB$_X$):** Podría dar $\kappa < \infty$ (más débil que RH) pero está en el umbral crítico.
- **Rutas vía grupo adélico, Hecke, Volterra, completitud:** Todas son reformulaciones de RH o son circulares.

**La única ruta no obturada está en C5.** Si la constante $a_{\mathrm{tail}}(X)$ resulta estrictamente menor que 1 para algún $X$ finito, eso daría un resultado incondicional nuevo: $\kappa < \infty$ (finitos ceros fuera de línea). Esto no implica RH pero es el mayor resultado alcanzable dentro de la Dirección B sin nueva información.

---

## Parte VIII — Estructura técnica del problema de índice negativo

### Sección 8.1 — El operador de defecto y la extensión de von Neumann

Para entender $H_C$ en $\Pi_\kappa$ desde la perspectiva de la teoría de extensiones, aplicamos la teoría de von Neumann adaptada a espacios de Pontryagin.

**Definición 8.1.** Sea $T_0 = H_C|_{\mathcal{S}_0}$ la restricción de $H_C$ al subespacio de funciones de prueba "bien soportadas". El operador $T_0$ es $Q$-simétrico (asumiendo V.1 verificado) y su clausura $\overline{T_0}$ es un operador $Q$-simétrico cerrado en $\Pi_\kappa$.

**Definición 8.2 (Subespacios de defecto).** Para $z \in \mathbb{C} \setminus \mathbb{R}$, los **subespacios de defecto** de $T_0$ respecto a $Q$ son:
$$N_z = \ker(T_0^{[*]} - zI) \quad (\text{en } \Pi_\kappa),$$
donde $T_0^{[*]}$ es el $Q$-adjunto de $T_0$.

**Proposición 8.3.** Los índices de defecto $n_\pm = \dim N_{\pm i}$ son finitos si y solo si el espacio de Pontryagin $\Pi_\kappa$ tiene la propiedad de que el "espectro esencial de $T_0$" no acumula en los puntos de defecto. En el caso de $H_C$, los índices de defecto están relacionados con la regularidad de los ceros de $\zeta$ en la línea crítica.

**La extensión autoadjunta estándar.** En el espacio de Hilbert $L^2(C_\mathbb{Q})$, el operador $H_C$ tiene extensiones autoadjuntas (en sentido ordinario) parametrizadas por operadores unitarios entre los espacios de defecto. Cada extensión corresponde a diferentes "condiciones de frontera" adélicas. La pregunta es cuál extensión, si alguna, es la "correcta" para la fórmula de Weil.

---

### Sección 8.2 — El problema de la regularización y la fórmula de Weil

La forma de Weil $Q(f,f) = \mathcal{W}(f \star \tilde{f})$ requiere regularización porque la serie sobre ceros $\sum_\rho \hat{f}(\rho)$ converge condicionalmente. Esta regularización introduce términos adicionales que son cruciales para las propiedades de $H_C$.

**Proposición 8.4 (La regularización como perturbación).** La regularización de $\mathcal{W}$ puede escribirse como:
$$Q_{\mathrm{reg}}(f,f) = Q_{\mathrm{formal}}(f,f) + R(f,f),$$
donde $R$ es un término de regularización que depende del método de regularización elegido. Diferentes regularizaciones dan diferentes operadores $H_C$ (en el sentido de dominios y formas cuadráticas asociadas).

**Observación 8.5.** La elección de la regularización "correcta" es parte del problema de construcción del espacio $\mathcal{K}$ (ítem pendiente de Phase 26). Una regularización natural es la proporcionada por la fórmula explícita de Weil en forma adélica (Tate 1950), que da una forma $Q$ con convergencia adecuada.

---

### Sección 8.3 — El problema del espectro continuo

**Proposición 8.6 (El espectro continuo de $H_C$).** En $L^2(C_\mathbb{Q})$, el operador $H_C = -ix\partial_x$ tiene espectro continuo que cubre $\mathbb{R}$ (en la parametrización donde los ceros en línea aparecen como eigenvalores imaginarios). Este espectro continuo corresponde a las "funciones de onda de los primos" en la fórmula de Weil.

**Consecuencia para el índice negativo.** La distinción entre $\kappa = 0$ y $\kappa > 0$ en presencia de espectro continuo es más sutil que en el caso discreto. El índice negativo en un espacio de Pontryagin con espectro continuo se mide mediante la "parte negativamente definida" del espectro, que en términos del operador de Connes corresponde a los ceros fuera de línea.

**Proposición 8.7 (Descomposición espectral en $\Pi_\kappa$).** Bajo las hipótesis de Phase 26 (V.1–V.4 verificados), el operador $H_C$ en $\Pi_\kappa$ tiene la descomposición espectral:
$$H_C = H_{\mathrm{ess}} \oplus H_{\mathrm{disc}},$$
donde:
- $H_{\mathrm{ess}}$ corresponde al espectro continuo (ceros en línea crítica), autoadjunto en $L^2$.
- $H_{\mathrm{disc}}$ corresponde al espectro discreto de $\Pi_\kappa$, que tiene $\kappa$ eigenvalores complejos correspondientes a los ceros fuera de línea.

El índice negativo $\kappa$ es la contribución de $H_{\mathrm{disc}}$ al índice de Kreĭn.

*Estado:* Esta descomposición es conjetural y depende de los ítems V.1–V.4 de Phase 26.

---

## Parte IX — Síntesis y agenda de trabajo

### Sección 9.1 — Tabla de obstáculos de la Dirección B

| Ruta | Condición | Obstáculo principal | Estado |
|------|-----------|---------------------|--------|
| Semiacotación $Q \geq 0$ | C1 | Equivalente a RH | Bloqueado |
| Semiacotación $H_C \geq cI$ | C2 | Equivalente a RH | Bloqueado |
| Espectro de $H_C \subset i\mathbb{R}$ | C3 | Reformulación de RH | Bloqueado |
| Función característica analítica | C4 | Equivalente a RH | Bloqueado |
| Cola prima $a_{\mathrm{tail}} < 1$ | C5 | $a_{\mathrm{tail}} = 1$ marginal | **Abierto** |
| Definitizabilidad de $H_C$ | C6 | Implica C1 | Bloqueado |
| Completitud eigenvectores reales | C7 | Circular | Bloqueado |
| Hecke / representaciones | Nuevas simetrías | Reformulación de RH | Bloqueado |
| Perturbación rango finito | $H_C = H_0 + K$ | Requiere conocer $\kappa$ | Circular |
| Volterra / triangular | Descomposición | Requiere eigenvectores | Circular |

---

### Sección 9.2 — Los ítems V.1–V.4 de Phase 26 revisados

Antes de proceder con cualquier ruta de la Dirección B, los ítems de Phase 26 deben resolverse. Evaluamos su estado a la luz del análisis de este documento:

**V.1 ($Q$-simetría de $H_C$).** *Estado:* Pendiente. Requiere verificar la invarianza de $Q$ bajo $U_\lambda$. El cálculo explícito involucra la transformación de los términos primos de $Q$ bajo dilataciones. Parece verificable mediante la fórmula de Weil en versión adélica (Tate 1950), donde la invarianza del producto adélico se traduce en la invarianza de $Q$.

*Acción propuesta:* Verificar la invarianza de $\mathcal{W}$ bajo cambios de variable multiplicativos usando la versión adélica de la fórmula de Weil.

**V.2 (ceros ↔ eigenvalores complejos).** *Estado:* Pendiente, es el obstáculo central. Los caracteres $f_j = x^{b_j + i\gamma_j}$ no están en $L^2(C_\mathbb{Q})$. La pregunta es si están en $\mathcal{K}$ como distribuciones temperadas.

*Acción propuesta:* Definir $\mathcal{K}$ como un espacio de distribuciones temperadas respecto a la métrica de Weil, y verificar si los caracteres son vectores de defecto de $H_C$ en este espacio.

**V.3 ($\mathrm{neg.ind}(H_C) = \kappa$).** *Estado:* Consecuencia de V.2 más el teorema de Kreĭn–Langer. Si V.2 se verifica, V.3 se obtiene de la teoría abstracta.

**V.4 (dimensión del eigenespacio).** *Estado:* Consecuencia algebraica de V.2 y V.3.

---

### Sección 9.3 — La agenda de Phase 34 para la Dirección B

**Prioridad 1 (Resultado incondicional posible): C5.**

Demostrar o refutar que $a_{\mathrm{tail}}(X) < 1$ para algún $X$ finito. Este es el único resultado dentro de la Dirección B que podría ser incondicional (no equivalente a RH). La dificultad está en la constante marginal $a_{\mathrm{tail}} = 1$ establecida por los resultados N3 del programa.

*Pregunta precisa:* ¿Es $a_{\mathrm{tail}}(X) = \sup_{f} Q_{\mathrm{prim},>X}(f,f) / Q_\infty(f,f)$ estrictamente menor que 1 para algún $X$ finito, o es idénticamente igual a 1 en el límite?

**Prioridad 2 (Fundamentos del espacio $\mathcal{K}$): V.1.**

Verificar la $Q$-simetría de $H_C$ mediante la fórmula adélica de Weil. Esto es el fundamento de toda la Dirección B: sin V.1, el espacio de Pontryagin $(\mathcal{K}, Q)$ con $H_C$ como operador $Q$-autoadjunto no está definido.

**Prioridad 3 (Exploración de C7): Sistema de eigenvectores.**

Aunque la completitud del sistema de eigenvectores con eigenvalores reales es circular si se asume la realidad de los eigenvalores, hay una pregunta no-circular: ¿es el sistema de eigenvectores de $H_C$ con eigenvalores **puramente imaginarios** (ceros en línea) $Q$-completo en el subespacio positivo $\mathcal{K}_+$? Si esto se verifica, significaría que $\mathcal{K}_+$ está generado por los ceros en línea, y entonces la existencia de $\mathcal{K}_-$ (la parte negativa) dependería enteramente de los ceros fuera de línea. Esto no prueba que $\kappa = 0$, pero hace la estructura más transparente.

---

### Sección 9.4 — Evaluación final: ¿es la Dirección B prometedora?

**Respuesta honesta:** La Dirección B es la formulación correcta del problema en lenguaje de operadores, pero no proporciona herramientas nuevas que superen la dificultad intrínseca de RH.

**Lo que la Dirección B da:**
- Un lenguaje preciso: $\kappa = 0 \iff$ RH, con el operador $H_C$ como objeto central.
- El teorema de Kreĭn–Langer como cota automática: si hay $m$ órbitas fuera de línea, $H_C$ tiene a lo sumo $m$ pares de eigenvalores complejos.
- La condición C5 como única ruta hacia un resultado incondicional (más débil que RH).
- La función característica de Livsic como espejo de la estructura de ceros de $\xi$.

**Lo que la Dirección B no da:**
- Ninguna condición verificable a partir de propiedades globales de $\zeta$ que implique $\kappa = 0$.
- Una palanca independiente que no sea equivalente a RH.
- Una ruta que evite el obstáculo de Hadamard en su versión para la Dirección B.

**El obstáculo fundamental** es el mismo que en la dirección CCM (aunque con distinta forma): demostrar $\kappa = 0$ requiere, en todos los caminos explorados, demostrar que los ceros de $\zeta$ no se alejan de la línea crítica. No hay ningún argumento operatorial que fuerce $\kappa = 0$ sin usar esta información.

La Dirección B no está "bloqueada" en el sentido de ser refutada: no se ha demostrado que sea imposible probar $\kappa = 0$ sin conocer las posiciones de los ceros. Pero tampoco se ha encontrado ninguna herramienta que abra un camino genuinamente nuevo.

---

## Apéndice A — Revisión de los teoremas de Pontryagin/Kreĭn usados

### A.1 — Referencias precisas

**Teorema de Pontryagin (1944).** L.S. Pontryagin, "Hermitian operators in spaces with indefinite metric," Izv. Akad. Nauk SSSR Ser. Mat. 8 (1944), 243–280. 
*Enunciado:* Todo operador hermitiano en un espacio de Pontryagin $\Pi_\kappa$ tiene al menos $\kappa$ valores propios reales o complejos, contando multiplicidades.

**Teorema espectral de Kreĭn–Langer (1963).** M.G. Kreĭn y H. Langer, "On the spectral theory of linear pencils in spaces with two norms," Funktsional. Anal. i Prilozen. (1963). [Traducción rusa; la versión accesible está en el libro de Azizov–Iokhvidov.]
*Enunciado:* Operadores autoadjuntos en $\Pi_\kappa$ tienen a lo sumo $\kappa$ pares de eigenvalores no-reales.

**Azizov–Iokhvidov (1989).** T.Ya. Azizov y I.S. Iokhvidov, "Linear Operators in Spaces with an Indefinite Metric," Wiley, 1989.
*Referencia estándar* para la teoría de operadores en espacios con forma indefinida, incluyendo espacios de Pontryagin, Kreĭn, y sus generalizaciones.

**Langer (1982).** H. Langer, "Spectral functions of definitizable operators in Kreĭn spaces," Functional Analysis (Dubrovnik 1981), Lecture Notes in Math. 948, Springer, 1982.
*Enunciado del teorema de definitizabilidad.*

**Livsic–Yantsevich (1979).** M.S. Livsic y A.A. Yantsevich, "Operator Colligations in Hilbert Spaces," Wiley, 1979. (Traducción del original ruso de 1971.)
*Para la función característica de Livsic.*

**Alpay–Dijksma–Rovnyak–de Snoo (1997).** D. Alpay, A. Dijksma, J. Rovnyak, H.S.V. de Snoo, "Schur Functions, Operator Colligations, and Reproducing Kernel Pontryagin Spaces," Birkhäuser, 1997.
*Para la función característica en espacios de Pontryagin.*

---

### A.2 — Diagrama de implicaciones

```
RH
 ↕
Q(f,f) ≥ 0 ∀f  (C1)
 ↕
neg.ind(H_C) = 0  ←→  κ = 0
 ↑                     ↑
 C2: H_C ≥ cI          C5: a_tail < 1 → κ < ∞ (más débil)
 ↑                     
 C3: espectro ⊂ iℝ     
 ↕
 C4: Θ analítica en ℂ \ iℝ
 ↕
 ξ no tiene ceros fuera de ℜ(s) = 1/2
 ↕
 RH
```

Todas las condiciones C1–C4 son equivalencias con RH. La condición C5 es estrictamente más débil.

---

## Apéndice B — El contexto del programa

Este documento se enmarca en Phase 34 (nuevas direcciones), que sigue al bloqueo de la dirección CCM (Phase 32–33, Docs 53–90). La Dirección B es independiente del CCM en el siguiente sentido: no usa la geometría no-conmutativa de Connes–Consani ni la maquinaria de triples espectrales. En cambio, usa la reformulación operatorial del espacio de Pontryagin como espacio de trabajo.

Sin embargo, el operador $H_C$ es el mismo operador de Connes en ambas direcciones. La diferencia está en la **perspectiva**: 
- La dirección CCM analiza $H_C$ como operador en un triple espectral.
- La Dirección B analiza $H_C$ como operador en un espacio de Pontryagin.

Ambas perspectivas se bloquean en el mismo obstáculo fundamental: demostrar propiedades espectrales de $H_C$ que impliquen la ausencia de ceros fuera de la línea crítica.

---

*Fin del Doc 91.*

**Estado del documento:** Análisis completo de la Dirección B. Todas las rutas investigadas. El obstáculo fundamental está identificado. Ninguna ruta cierra el argumento para $\kappa = 0$. La condición C5 queda como única ruta hacia un resultado incondicional más débil.

**Próximo paso sugerido:** Cálculo explícito de $a_{\mathrm{tail}}(X)$ en función de $X$, para determinar si la constante marginal $a_{\mathrm{tail}} = 1$ se mantiene o se rompe al restringir a la cola prima.
