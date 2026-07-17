# Phase 26 — El teorema puente: Kreĭn ↔ Connes

**Fecha:** junio 2026
**Objetivo único:** formular con precisión matemática el teorema que identifica el
índice negativo de Kreĭn κ con la no-autoadjunticidad del operador de Connes.

Si el teorema puente no puede escribirse con precisión, Phase 26 no puede comenzar.

---

## 0. Auditoría bibliográfica del puente

**Connes (1999):** "Trace formula in noncommutative geometry and the zeros of the
Riemann zeta function." Establece la fórmula de Weil como una fórmula de trazas del
operador de escalado sobre el espacio de clases adélicas $X = \mathbb{A}_\mathbb{Q}/\mathbb{Q}^*$.

**Connes–Consani (2010, 2014, 2016):** El "sitio de escalado" y la geometría aritmética
del espacio de clases adélicas. Refinamientos de la fórmula de trazas.

**Burnol (2001, 2004):** La fórmula explícita como fórmula de dispersión. El operador de
Connes como operador de Dirac en un sentido funcional.

**Kreĭn–Langer (1978):** Factorización de funciones $\mathfrak{J}$-no-negativas en espacios
de Pontryagin. Teorema espectral para operadores $\mathcal{Q}$-autoadjuntos.

**¿Existe un teorema puente previo?** No en la literatura. Hay citas cruzadas entre los
programas, pero no una identificación precisa del tipo κ(Q) = neg.ind($H_{CW}$).

El trabajo más cercano: Burnol (2002, "On some symmetric Weil explicit formulas") conecta
la positividad de Weil con propiedades espectrales de operadores de Dirac, pero no identifica
el índice de Kreĭn explícitamente.

**Conclusión:** El teorema puente no existe en la literatura. Su formulación es nueva.

---

## 1. Las dos estructuras a conectar

### Estructura A: La forma cuadrática de Weil (lado Kreĭn)

Sea $\mathcal{S}(\mathbb{R}^*_+)$ el espacio de Schwartz de funciones de prueba en $\mathbb{R}^*_+$.
Para $f \in \mathcal{S}(\mathbb{R}^*_+)$, la forma de Weil es:
$$\mathcal{W}(f) = \sum_\rho \hat{f}(\rho) - \hat{f}(0)\log\pi - \hat{f}(1)\log\pi
+ \sum_{p,n} \frac{\log p}{p^{n/2}} f(p^n) + \sum_{p,n}\frac{\log p}{p^{n/2}}f(p^{-n})
+ f(1)\log\pi,$$
donde $\hat{f}$ es la transformada de Mellin de $f$, la suma $\sum_\rho$ recorre todos los ceros
no triviales de $\zeta$, y la suma $\sum_{p,n}$ recorre potencias de primos.

La **forma cuadrática de Weil** es:
$$Q(f, g) := \mathcal{W}(f * \tilde{g}), \qquad \tilde{g}(x) = \overline{g(1/x)} \cdot x^{-1}.$$

**Proposición 26-A.1** (Weil 1952). $Q(f,f) \geq 0$ para toda $f$ admisible
si y sólo si RH es verdadera.

**Definición 26-A.2** (Índice de Kreĭn). El **índice negativo de Kreĭn** κ de $Q$ es el
número máximo de vectores linealmente independientes $\{f_1,\ldots,f_k\}$ tales que la
matriz de Gram $(Q(f_i,f_j))_{i,j}$ es definida negativa:
$$\kappa := \sup \{k : \exists f_1,\ldots,f_k \in \mathcal{S} \text{ con } \det(Q(f_i,f_j)) < 0\}.$$

Bajo Hipótesis D con $m$ órbitas fuera de línea: $\kappa = 2m$ (Papers P32–P33).

### Estructura B: El operador de Connes (lado espectral)

Sea $C_\mathbb{Q} := \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ el grupo de clases de idèles.
Sea $H = L^2(C_\mathbb{Q}, d\mu)$ donde $d\mu$ es la medida de Haar normalizada.

El grupo $\mathbb{R}^*_+$ actúa sobre $C_\mathbb{Q}$ por multiplicación:
$$(U_\lambda f)(x) = f(\lambda^{-1} x), \quad \lambda \in \mathbb{R}^*_+, f \in H.$$

El **operador de Connes–Weil** es el generador infinitesimal de esta representación:
$$H_C := \frac{1}{i}\left.\frac{d}{d\lambda}\right|_{\lambda=1} U_\lambda.$$

Formalmente: $(H_C f)(x) = -i x \frac{d}{dx} f(x)$ (operador de Euler sobre $C_\mathbb{Q}$).

**Estado conocido:** $H_C$ es formalmente simétrico sobre funciones de prueba. Su extensión
autoadjunta en $L^2(C_\mathbb{Q})$ está relacionada con la distribución de los ceros de $\zeta$.
RH ↔ $H_C$ posee una extensión autoadjunta con espectro contenido en $i\mathbb{R}$ (el eje imaginario
en la parametrización de Connes donde los ceros aparecen como $s - 1/2 = i\gamma$).

---

## 2. La forma cuadrática de Weil como producto interno en $H$

**Proposición 26-B.1** (Identificación de Q con un producto interno). Para $f, g \in H$, el
**producto interno de Weil–Connes** es:
$$\langle f, g \rangle_Q := Q(f, g) = \mathcal{W}(f * \tilde{g}).$$

Esto define una forma hermitiana en $H$. Por la Proposición 26-A.1:
- Si RH: $\langle f,f\rangle_Q \geq 0$ — producto interno semidefinido positivo.
- Si Hipótesis D (κ=2m): $\langle f,f\rangle_Q$ tiene exactamente 2m "direcciones negativas" —
  producto interno indefinido con índice negativo κ = 2m.

El espacio $(H, \langle\cdot,\cdot\rangle_Q)$ es formalmente:
- Un **espacio de Hilbert** si RH (estructura positiva).
- Un espacio con forma indefinida de índice negativo κ = 2m si Hipótesis D.

**Advertencia:** que este segundo espacio sea efectivamente un **espacio de Pontryagin** no
está demostrado. Requiere verificar, además de que κ < ∞: (a) no-degeneración (ker$Q$ de
dimensión finita o nula); (b) completitud del espacio cociente $H/\ker Q$; (c) existencia
de una descomposición fundamental $H = H_+ \oplus H_-$ con $H_-$ de dimensión κ.
Estas propiedades son parte de lo que Phase 26 debe establecer.

**Definición 26-B.2** (El espacio de Kreĭn-Connes — condicional). Si $Q$ admite una
completación de Pontryagin de índice κ, se denota $\mathcal{K}$. La existencia de $\mathcal{K}$
es un objetivo de Phase 26, no un punto de partida.

**El operador de Connes $H_C$ en $\mathcal{K}$**: $H_C$ es $Q$-simétrico si $Q(H_C f, g) = Q(f, H_C g)$
para toda $f,g$ en el dominio. ¿Se verifica esta simetría?

**Objetivo 26-B.3** ($Q$-invariancia del escalado — resultado a demostrar). La condición
que haría de $H_C$ un operador $Q$-simétrico es:
$$Q(U_\lambda f, U_\lambda g) = Q(f, g) \quad \forall f, g \in \mathcal{S}, \; \lambda \in \mathbb{R}^*_+.$$

Si esto se cumple, el generador infinitesimal $H_C$ de la representación $(U_\lambda)$ es
automáticamente $Q$-simétrico (argumento estándar: derivar en $\lambda = 1$).

**Por qué no es inmediato.** La forma $Q(f,g) = \mathcal{W}(f*\tilde{g})$ contiene tres tipos
de términos:
- Un término espectral: $\sum_\rho \widehat{f*\tilde{g}}(\rho)$.
- Términos archimedianos: $-\widehat{f*\tilde{g}}(0)\log\pi - \widehat{f*\tilde{g}}(1)\log\pi + \ldots$
- Términos aritmético-primos: $\sum_{p,n} \frac{\log p}{p^{n/2}} (f*\tilde{g})(p^n) + \ldots$

La invariancia $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ bajo $(U_\lambda f)(x) = f(\lambda^{-1}x)$
requiere que cada uno de estos términos sea invariante por separado, o que las variaciones se
cancelen mutuamente. El término aritmético transforma como:
$$(f*\tilde{g})(p^n) \mapsto (U_\lambda f * \widetilde{U_\lambda g})(p^n) = (f*\tilde{g})(\lambda^{-1} p^n),$$
lo que modifica el argumento de evaluación en los primos. La invariancia global no es obvia.

**Estado:** Pendiente de demostración. Constituye un resultado central independiente de
Phase 26, no un corolario de las otras partes. Su prueba requiere la propiedad de
transformación de $\mathcal{W}$ bajo cambio de variable multiplicativo, que se relaciona
con la fórmula de Weil en versión Tate (adélica).

---

## 3. El teorema puente: formulación precisa

**Definición 26-C.1** (Espectro no-real en espacio de Pontryagin). Sea $T$ un operador
$Q$-autoadjunto en un espacio de Pontryagin $(\mathcal{K}, Q)$ con índice negativo κ < ∞.
El teorema espectral de Kreĭn–Langer (1963, 1978; cf. Azizov–Iokhvidov 1989, §2.3) establece:

$T$ tiene **a lo sumo** $\kappa$ pares de valores propios no-reales $\{\lambda_j, \bar\lambda_j\}$
con $\text{Im}(\lambda_j) \neq 0$, y su espectro esencial está en $\mathbb{R}$.

**Nota sobre "a lo sumo" vs. "exactamente":** La cota es $\leq \kappa$, no $= \kappa$.
La igualdad requiere que el operador sea "maximal" en algún sentido, o que la propia
construcción del espacio garantice que cada dirección negativa de $Q$ produce un eigenvalor
complejo. Ésta es precisamente la afirmación no-trivial de V.2.

**Teorema 26-C.2** (El Teorema Puente — Working Conjecture). Bajo Hipótesis D con κ = 2m:

El operador $H_C$ en el espacio de Pontryagin $(\mathcal{K}, Q)$ es $Q$-simétrico y satisface:

**(i)** El espectro esencial de $H_C$ en $\mathcal{K}$ es $i\mathbb{R}$ (el eje imaginario), correspondiente
a los ceros de $\zeta$ en la línea crítica.

**(ii)** El operador $H_C$ tiene exactamente κ = 2m valores propios "complejos" en $\mathcal{K}$
(en el sentido del teorema espectral de Kreĭn–Langer), dados por:
$$\text{Eigenvalores complejos de }H_C = \{b_j + i\gamma_j : j=1,\ldots,m\} \cup \{-b_j + i\gamma_j\}$$
donde $\rho_j = (1/2+b_j)+i\gamma_j$ son los ceros fuera de línea.

**(iii)** La multiplicidad de cada eigenvalor complejo es 1 (ceros simples de $\zeta$, si son simples).

**(iv)** El índice negativo de Kreĭn del operador $H_C$ en $\mathcal{K}$ coincide con el índice
negativo de la forma $Q$: $\text{neg.ind}_Q(H_C) = \kappa = 2m$.

**Corolario 26-C.3.** El Teorema Puente implica:
$$\kappa = 0 \iff H_C \text{ es } Q\text{-autoadjunto con espectro en } i\mathbb{R} \iff \text{RH.}$$

*Equivalencia directa:* RH ↔ κ = 0 (Papers P31–P33) ↔ Q es semidefinido positivo (Weil 1952)
↔ el espacio de Kreĭn $\mathcal{K}$ es un espacio de Hilbert ↔ $H_C$ no tiene eigenvalores complejos
↔ $H_C$ es genuinamente autoadjunto en $H$.

---

## 4. Estado de cada parte del teorema puente

| Parte | Contenido | Estado |
|-------|-----------|--------|
| (i): Espectro esencial = $i\mathbb{R}$ | Zeros en línea ↔ espectro esencial de $H_C$ | Plausible, no riguroso (depende de la realización de $H_C$) |
| (ii): 2m eigenvalores complejos | Zeros fuera de línea ↔ eigenvalores de Kreĭn | **No probado. Esta es la afirmación central.** |
| (iii): Multiplicidad 1 | Zeros simples de $\zeta$ | Implícito, condicional |
| (iv): neg.ind$_Q(H_C)$ = κ | Compatibilidad Kreĭn-Pontryagin | Formal pero no riguroso |

---

## 5. El obstáculo técnico central

**El operador $H_C$ en $L^2(C_\mathbb{Q})$ versus en $\mathcal{K}$.**

En $L^2(C_\mathbb{Q})$ (producto interno positivo), $H_C$ es formalmente simétrico pero su extensión
autoadjunta es problemática: el espacio $C_\mathbb{Q}$ no es compacto, y la fórmula de trazas tiene
divergencias logarítmicas que deben regularizarse.

En $\mathcal{K}$ (producto interno $Q$), el problema se transforma: $Q$ ya incorpora la fórmula de Weil
(que regulariza las divergencias) y $H_C$ puede ser mejor comportado como operador $Q$-simétrico.

**El problema técnico preciso:**

Definir $\mathcal{K}$ como el completado de $\mathcal{S}(\mathbb{R}^*_+)$ respecto a la norma:
$$\|f\|_{\mathcal{K}}^2 = |Q(f,f)| = |\mathcal{W}(f * \tilde{f})|.$$

**Obstáculo:** Si $Q(f,f) = 0$ para $f \neq 0$ (vectores isótropos), la norma degenera.
En un espacio de Pontryagin, los vectores isótropos son $Q$-perpendiculares a sí mismos
pero no necesariamente nulos. El cociente $\mathcal{K}/\text{ker}(Q)$ puede ser el espacio correcto.

**Proposición 26-D.1** (Existencia del espacio de Pontryagin). Si la forma $Q$ tiene rango
finito de degeneración (i.e., ker$(Q)$ es de dimensión finita) y índice negativo finito κ = 2m,
entonces $\mathcal{K}$ es un espacio de Pontryagin de índice κ en el que $H_C$ puede definirse
como operador densamente definido.

*Estado:* Requiere verificar que ker$(Q)$ es de dimensión finita y que $H_C$ preserva el dominio
de $Q$. Esto es parte del trabajo técnico de Phase 26.

---

## 6. La estructura de Phase 26 — corrección de prioridades

**Corrección post-auditoría (junio 2026):** Los cuatro ítems no son equivalentes. V.2 es el
objetivo principal de Phase 26, no un ítem subsidiario de verificación.

La clasificación correcta:

| Ítem | Clasificación real | Dependencia |
|---|---|---|
| V.1 ($Q$-simetría de $H_C$) | Resultado central independiente | — |
| **V.2** (ceros ↔ eigenvalores complejos) | **Objetivo principal de Phase 26** | El puente entero descansa aquí |
| V.3 (neg.ind($H_C$) = κ) | Consecuencia | Depende de V.2 + Kreĭn–Langer |
| V.4 (dimensión del eigenespacio) | Consecuencia algebraica | Depende de V.2 y V.3 |

V.2 no es un "cálculo técnico". Contiene el obstáculo principal: los candidatos a eigenvectors
($f_j = x^{b_j+i\gamma_j}$) no están en $L^2(C_\mathbb{Q})$, y la forma $Q$ no está bien definida
sobre ellos. Requiere una extensión distribucional de $Q$ o una localización. Ver `phase-26/01-attack-V2.md`.

Para que el Teorema Puente sea un objetivo matemático concreto (no solo una idea), se necesita
verificar los siguientes cuatro ítems — con la advertencia de que V.2 es el central:

### Ítem 26-V.1: ¿Es $H_C$ $Q$-simétrico?

Condición: $Q(H_C f, g) = Q(f, H_C g)$ para $f,g$ en un dominio denso.

*Reducción.* Por definición $Q(f,g) = \mathcal{W}(f*\tilde{g})$. Entonces:
$$Q(H_C f, g) = \mathcal{W}((H_C f)*\tilde{g}) \stackrel{?}{=} \mathcal{W}(f*(H_C g)^{\sim}).$$

Si $H_C$ actúa como $(H_C f)(x) = -ix\partial_x f(x)$, entonces $(H_C f)*\tilde{g}(y)$:

Por la convolución de Mellin: $\widehat{H_C f * \tilde{g}}(s) = \hat{H_C f}(s) \cdot \hat{\tilde{g}}(s)$.
Y $\hat{H_C f}(s) = (1/2-s)\hat{f}(s)$ (el operador de Euler en Mellin cambia s a s-1/2 ... ).

Necesito calcular esto explícitamente. La simetría $Q$ depende de la identidad funcional:
$$\sum_\rho [(s-\rho)\hat{f}(s)]|_{s=\rho} \hat{\tilde{g}}(\rho) = \sum_\rho \hat{f}(\rho)[(1-\rho)\hat{\tilde{g}}(1-\rho)]|$$

Esto requiere un cálculo cuidadoso. **Pendiente de verificación.**

### Ítem 26-V.2: ¿Corresponden los eigenvalores complejos de $H_C$ en $\mathcal{K}$ a los ceros fuera de línea?

Si $\rho_j = (1/2+b_j)+i\gamma_j$ es un cero de $\zeta$ fuera de línea, entonces $b_j + i\gamma_j$
debería ser un eigenvalor de $H_C$ en $\mathcal{K}$.

*Verificación directa:* Se necesita encontrar $f_j \in \mathcal{K}$ tal que $H_C f_j = (b_j+i\gamma_j) f_j$.
El candidato natural es $f_j(x) = x^{b_j+i\gamma_j}$ (un carácter de $\mathbb{R}^*_+$). Entonces:
$(H_C f_j)(x) = -ix\partial_x(x^{b_j+i\gamma_j}) = -i(b_j+i\gamma_j)x^{b_j+i\gamma_j} = (b_j+i\gamma_j)(-i)f_j$.

Hay un factor $(-i)$ de diferencia (depende de convenciones: si $H_C = x\partial_x$ vs $-ix\partial_x$).
Con la convención $H_C = -ix\partial_x$: eigenvalor = $-i(b_j+i\gamma_j) = \gamma_j - ib_j$... que tiene
$\text{Im}(\gamma_j-ib_j) = -b_j \neq 0$ (no está en el espectro real), consistente.

**La verificación requiere además:** que $f_j = x^{b_j+i\gamma_j}$ esté en $\mathcal{K}$,
i.e., que $Q(f_j, f_j)$ esté definido y sea finito. Esto involucra:
$$Q(f_j, f_j) = \mathcal{W}(f_j * \tilde{f}_j).$$

La convolución $f_j * \tilde{f}_j$ está relacionada con los valores de $|\zeta|$ en $\rho_j$, que
es 0 (pues $\rho_j$ es un cero). Esto sugiere que $Q(f_j,f_j) = 0$, es decir, $f_j$ es un
vector isótropo. Este es un punto técnico delicado.

**Estado: pendiente, con un cálculo concreto a ejecutar.**

### Ítem 26-V.3: ¿Es el índice negativo de $H_C$ en $\mathcal{K}$ igual a κ?

Por el teorema de Kreĭn–Langer para operadores en espacios de Pontryagin: si $H_C$ es
$Q$-autoadjunto en $\mathcal{K}$ con índice negativo κ, entonces tiene exactamente κ eigenvalores
complejos (en el plano complejo, fuera del eje real, contados con multiplicidad).

La identificación neg.ind$(H_C)$ = κ = neg.ind$(Q)$ = 2m sería el corazón del teorema puente.

**Estado: necesita (i) rigorizar $H_C$ como operador en $\mathcal{K}$, (ii) aplicar el teorema espectral de Kreĭn–Langer.**

### Ítem 26-V.4: ¿Produce el Ítem 26-V.2 un eigenespacio de dimensión correcta?

Para m = 1 (una sola órbita): 4 ceros fuera de línea {ρ₁⁺, ρ̄₁⁺, ρ₁⁻, ρ̄₁⁻}. En la
parametrización por $t$ (donde $t = -i(s-1/2)$): 4 ceros complejos de $H_0$. En $\mathcal{K}$:
2 eigenvalores complejos de $H_C$ (por la simetría $s ↔ 1-s$ de $\xi$, que reduce la cuenta a la mitad).

Dimensión del eigenespacio: 2 (los 2 eigenvalores complejos irreducibles bajo la simetría funcional).

---

## 7. Resultado del análisis: ¿puede escribirse el teorema puente?

**Respuesta: el Teorema Puente es una conjetura matemática coherente, no todavía un objetivo
verificable.**

El Teorema 26-C.2 está formulado como conjetura de trabajo, con las afirmaciones correctamente
identificadas. Pero el programa se reduce a un único problema central:

> **Construir rigurosamente el espacio $\mathcal{K}$ y demostrar la correspondencia espectral de V.2.**

Todo lo demás (V.1, V.3, V.4, la factorización adélica de 26-B) depende de eso.

**Estado honesto de cada componente antes de comenzar 26-A:**

| Componente | Estado real |
|---|---|
| $\mathcal{K}$ como espacio de Pontryagin | **No construido.** Condicional a (a) ker$Q$ finito, (b) completitud, (c) descomposición. |
| $Q(U_\lambda f, U_\lambda g) = Q(f,g)$ | **No demostrado.** Resultado central independiente (V.1 extendido). |
| Eigenvalores complejos = ceros fuera de línea | **No demostrado.** Es V.2; requiere que $f_j \in \mathcal{K}^+$ (extensión distribucional). |
| "Exactamente κ" eigenvalores complejos | Consecuencia de V.2; Kreĭn–Langer da "a lo sumo κ" gratis. |

**El 90% del esfuerzo de Phase 26 debe ir a V.2.** No se avanza a 26-B ni a la parte adélica
hasta que V.2 sobreviva una auditoría funcional completa. Ver `phase-26/01-attack-V2.md`.

---

## 8. Lo que el teorema puente da al programa

Si el Teorema 26-C.2 se prueba:

**Antes del puente:** RH ↔ κ = 0 (Kreĭn) y RH ↔ $H_C$ es autoadjunto (Connes) son dos
reformulaciones de RH, pero en espacios y lenguajes distintos, sin conexión directa.

**Después del puente:** RH ↔ κ(Q) = 0 ↔ neg.ind$(H_C)$ = 0 son la MISMA reformulación
en dos lenguajes, con un diccionario explícito. Esto permite usar herramientas de un programa
en el otro:
- Herramientas Kreĭn (factorización, espectro indefinido) → para estudiar $H_C$.
- Herramientas adélicas (Connes) → para intentar probar κ = 0.

**La hipótesis de trabajo para Phase 26:**

> El espacio adélico $C_\mathbb{Q} = \mathbb{A}_\mathbb{Q}^*/\mathbb{Q}^*$ tiene suficiente estructura aritmética para
> forzar neg.ind$(H_C) = 0$, es decir, para hacer que $H_C$ sea genuinamente autoadjunto.
>
> Esta estructura proviene de la **factorización local-global** del grupo $C_\mathbb{Q}$:
> $C_\mathbb{Q} \cong \prod_p \mathbb{Z}_p^* \times \mathbb{R}^*_+$
> y de la fórmula del producto de la función $\zeta$ que descompone $Q$ en factores locales.

---

## 9. Phase 26 — Estructura de trabajo

Dado que el teorema puente está formulado, Phase 26 procede así:

**26-A:** Verificación de los Ítems V.1–V.4 (cálculos técnicos, semanas de trabajo).

**26-B:** Si los ítems se verifican: buscar herramientas adélicas que impliquen neg.ind = 0.
   - Teorema de clase de campo local/global y su acción sobre $\mathcal{K}$.
   - La factorización euler-local de $Q = \prod_p Q_p$ (si existe).

**26-C:** Si los ítems no se verifican: diagnóstico preciso de por qué el puente falla, y
   reformulación correcta.

**Criterio de éxito de Phase 26:**
> O bien: el Teorema 26-C.2 está probado y el camino hacia RH vía herramientas adélicas
> es claro.
>
> O bien: se prueba que el puente no puede construirse en esta forma, con una razón precisa,
> y se identifica la corrección necesaria.

**Ninguno de los dos es un fracaso:** el primero abre la puerta, el segundo refina la pregunta.
