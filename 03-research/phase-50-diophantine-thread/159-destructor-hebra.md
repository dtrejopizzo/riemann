# Doc 159 — Destructor de la hebra diofántica: ¿es la completitud de {p^{iτ}} un cruce RH-libre del muro?

**Programa:** Hipótesis de Riemann — Phase 50: la hebra diofántica.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** ADVERSARIAL. Mandato único: DESTRUIR la esperanza de que la
independencia ℚ-lineal de {log p} (equivalentemente, la completitud/independencia del
sistema {p^{iτ}}) sea un cruce RH-libre del cuantificador maestro de P43 (el muro
promedio→individual / valor→inercia). La fase anterior (Docs 154–157) probó que los cinco
mecanismos clásicos colapsan para la forma de Weil; el Doc 157 (Teorema 157.10, GAP-157.A)
dejó la hebra diofántica como la ÚNICA grieta no cubierta por el no-go tauberiano. Aquí
intento matarla por adelantado, por tres vías independientes.

**Contrato de etiquetado.** **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad aquí o
citado con referencia verificable. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con
estatus honesto. **[GAP]** = declarado. **[GAP de literatura]** = dato no verificado a
nivel de página esta sesión, NO usado como premisa de ningún teorema. Jamás se fabrica una
prueba de RH ni una muerte que no esté. **NADA de numéricos.** Honestidad absoluta: si las
tres vías fallan en matar, lo digo, y entrego el complemento (qué tendría que ser verdad).

**Prerrequisitos leídos en fuente esta sesión:** Doc 157 completo (catálogo tauberiano,
Teorema 157.10, GAP-157.A — la grieta diofántica); Doc 112 completo (LP-112, teorema
límite de Bagchi, soporte S = {no-nulas}∪{0}, independencia ℚ-lineal de {log p} en sus
tres niveles, Lemas 3.1–3.3); Docs 82 y 85 (criterio de Nyman-Beurling-Báez-Duarte, el
diccionario de Mellin interno, completitud incondicional del span lineal vs. densidad
no-lineal de la clase Hadamard-crítica).

---

## 0. Resumen ejecutivo

**La afirmación a destruir (AAD).** *"La completitud/independencia diofántica del sistema
{p^{iτ}} colapsa el defecto de individuación de la forma de Weil sin reintroducir RH"* —
sería un cruce nuevo del muro promedio→individual.

**Estructura del documento.** Primero (§1) fijo qué es exactamente "la completitud de
{p^{iτ}}" y separo dos lecturas que el encargo y la AAD confunden a propósito: la
completitud-Kronecker (incondicional, sobre el toro de valores) y la completitud-cruce (la
que daría individuación). Luego ataco por las tres vías.

1. **(§2) Vía 1 — Circularidad Nyman–Beurling.** Construyo el diccionario de Mellin EXACTO
   entre las dos completitudes. **Resultado: la muerte por circularidad NO se consuma
   limpiamente, pero la vía revela algo decisivo.** El criterio de Nyman–Beurling es una
   completitud en L²(0,1) de las dilataciones de {a/t}, que vía Mellin es una completitud
   en L²(½+iℝ) del sistema {k^{-s}/(...)} — un sistema con frecuencias multiplicativas
   {log k}, k ∈ ℕ, no {log p}. La distinción ℕ vs. primos es real: la completitud de
   Nyman–Beurling es de los ENTEROS (factorización vía Euler ya horneada), y su anulación
   ES RH (Báez-Duarte). El sistema {p^{iτ}} de SOLO primos es lo que genera el toro de
   Kronecker; su completitud lineal es incondicional (Kronecker–Weyl) y NO es la
   completitud de Nyman–Beurling. **Veredicto Vía 1: la circularidad no es directa
   (son sistemas distintos: ℕ vs. primos), pero el puente entre ambos —pasar de la
   completitud de primos a la completitud de enteros— ES el producto de Euler evaluado en
   la línea crítica, que reintroduce ζ. La hebra sobrevive a la circularidad-Mellin
   ingenua, pero queda marcada: separar "primos" de "enteros" cuesta exactamente un
   producto de Euler sobre Re s = ½.**

2. **(§3) Vía 2 — Confinamiento Bohr–Voronin al lado-valor.** Argumento (con prueba
   estructural) que TODO lo que la independencia diofántica produce vive en la σ-álgebra
   generada por los VALORES de ζ (el toro de Kronecker / soporte de Bagchi), y que la
   cuenta de ceros / la inercia NO es medible respecto de esa σ-álgebra. **Resultado:
   MUERTE CASI-CONSUMADA.** Bagchi: la universalidad NO distingue RH de ¬RH (el teorema de
   universalidad de Voronin vale incondicionalmente, igual bajo RH que bajo ¬RH; la
   independencia ℚ-lineal es su único insumo aritmético). El soporte S = {f no-nula}∪{0}
   está determinado por la independencia diofántica SOLA, sin información de ceros. La
   individuación (la posición de UN cero) es un evento de densidad cero invisible a la
   medida límite (Prop. 2.6 de D112). **La hebra diofántica vacía la oscilación de valores
   pero es estructuralmente ciega a la inercia. Esta vía SÍ mata —con una grieta nombrada
   (GAP-159.B): la independencia se usa allí como hecho-ambiente, no como condición
   cuantitativa; el residuo de vida es exactamente la Vía 3.**

3. **(§4) Vía 3 — Reintroducción de ceros (como Beurling–Malliavin en D157).** Verifico la
   dicotomía cualitativo/cuantitativo. **Resultado: MUERTE CONSUMADA para la parte
   cuantitativa.** La completitud CUALITATIVA de {p^{iτ}} es incondicional (Kronecker–Weyl;
   el toro es minimal) pero INÚTIL: da densidad de órbita, no individuación — es
   exactamente el lado-promedio. Toda CUANTIFICACIÓN (una cota efectiva del radio de
   completitud, una velocidad de equidistribución refinada al disco fijo del cero) pasa por
   una densidad efectiva que, vía la fórmula explícita / el teorema de Bagchi, ES la cuenta
   de ceros — exactamente como murió Beurling–Malliavin en el Doc 157 (Prop. 157.7). La
   independencia ℚ-lineal de {log p} es cualitativa por naturaleza (es un enunciado
   sí/no sobre relaciones enteras); su única forma cuantitativa relevante (medidas de
   irracionalidad / discrepancia efectiva del flujo de Kronecker en el disco del cero) NO
   está conectada con los ceros por ningún teorema conocido — y AHÍ, y solo ahí, queda el
   residuo de vida (GAP-159.C).

4. **(§5) VEREDICTO.** **MATAN DOS DE TRES, pero NO de forma que cierre la grieta.** La
   Vía 1 no mata (la circularidad-Mellin es indirecta: ℕ≠primos). La Vía 2 mata la lectura
   "independencia como hecho-ambiente" (confinamiento al lado-valor, vía Bagchi). La Vía 3
   mata toda cuantificación "vía densidad efectiva clásica". **Pero el complemento conjunto
   de las tres muertes deja vivo un objeto preciso y NO vacío:** una condición tauberiana
   espectral que use una propiedad CUANTITATIVA-DIOFÁNTICA de {log p} (discrepancia /
   medida de irracionalidad del flujo de Kronecker en el disco fijo del cero) que NO sea
   función de la densidad de resonancia. La hebra no muere del todo: queda reducida a un
   enunciado diofántico-efectivo cuya conexión (o no-conexión) con los ceros es el
   [GAP de literatura] central. **No fuerzo la tercera muerte: declaro el residuo.**

5. **(§6) Si sobrevive: qué tendría que ser verdad.** Lista del complemento — las cinco
   condiciones precisas que harían de la hebra un cruce genuino.

---

## 1. Qué es "la completitud de {p^{iτ}}" — dos lecturas que hay que separar

La AAD es deliberadamente ambigua entre dos objetos distintos. Separarlos es el primer
acto adversarial, porque la confusión entre ambos es donde una falsa esperanza se esconde.

### 1.1. Lectura A: completitud-Kronecker (sobre el toro de valores)

**[DEFINICIÓN 159.1] (sistema de primos y su toro).** Fijo τ ∈ ℝ. El sistema
$\{p^{i\tau}\}_p = \{e^{i\tau\log p}\}_p$ es una familia de puntos del círculo unidad
indexada por los primos. La independencia ℚ-lineal de $\{\log p\}$ (factorización única,
Doc 112 Lema 2.2 y 3.3) implica, por Kronecker–Weyl, que la órbita
$\tau \mapsto (p^{i\tau})_{p}$ es densa y equidistribuida en el toro infinito-dimensional
$\mathbb{T}^\infty = \prod_p S^1$. Esto es el motor de:
- la casi-periodicidad de Bohr de $\zeta$ en $\sigma > 1$ (donde la serie de Euler
  converge absolutamente: $\zeta(s) = \prod_p(1-p^{-s})^{-1}$ es una función continua del
  punto $(p^{-it})_p$ del toro);
- la universalidad de Voronin / el teorema límite de Bagchi en la franja $\tfrac12<\sigma<1$
  (Doc 112 §2.4): la medida límite $Q$ es la ley del producto de Euler aleatorio
  $\zeta(s,\omega) = \prod_p(1-\omega_p p^{-s})^{-1}$ con $\omega = (\omega_p)$ uniforme en
  $\mathbb{T}^\infty$.

**Estatus de la Lectura A: incondicional, sin contenido de individuación.** Es completitud
en el sentido de "la órbita llena el toro de valores". No dice nada sobre la posición de
los ceros. Es el LADO-VALOR puro (P43 §4). La detallo y la mato en §3.

### 1.2. Lectura B: completitud-cruce (la que daría individuación)

**[DEFINICIÓN 159.2] (completitud-cruce).** La AAD necesita que la completitud/independencia
de $\{p^{i\tau}\}$ implique un enunciado de INDIVIDUACIÓN: que el defecto de Weil
$F_{\mathrm{off}}(h) = \sum_{\rho\text{ off}}\hat h(\cdots)$ sea forzado a cero (o que la
posición de UN cero sea decidible) a partir de la estructura diofántica del sistema de
primos, sin pasar por la fórmula explícita / la densidad de ceros.

**El punto central de todo el documento.** La AAD es la conjetura de que Lectura A ⟹
Lectura B con un puente RH-libre. Las tres vías son tres maneras de probar que ese puente,
o bien no existe (Vía 2: las dos lecturas viven en σ-álgebras distintas, la inercia no es
medible respecto del toro de valores), o bien existe pero reintroduce ζ (Vía 1: el puente
es el producto de Euler), o bien existe solo cualitativamente y morir al cuantificarse
(Vía 3: como Beurling–Malliavin).

---

## 2. Vía 1 — Circularidad Nyman–Beurling: el diccionario de Mellin exacto

### 2.1. El criterio de Nyman–Beurling–Báez-Duarte, recordado con precisión

Recopilo de Doc 82 §1 (verificado allí contra la literatura clásica):

- **[Nyman 1950] / [Beurling 1955].** RH ⟺ $\mathbf{1}_{(0,1)}$ está en el cierre en
  $L^2(0,\infty)$ del span de las dilataciones de la parte fraccionaria
  $r_a(t) = \{a/t\}$, $a\in(0,1)$ (con la restricción $\sum c_k a_k = 0$ para
  cuadrabilidad). [Nym50; Beu55].
- **[Báez-Duarte 2003].** Versión discreta computable: RH ⟺ $\lim_{N\to\infty} d_N^2 = 0$,
  donde $d_N^2 = \inf_{c_k}\int_0^\infty |\mathbf 1_{(0,1)} - \sum_{k\le N} c_k\{k/t\}|^2dt$
  usando solo dilataciones por ENTEROS $k = 1,\dots,N$. [BD03].

**Observación clave (la naturaleza del sistema).** El sistema de Nyman–Beurling–Báez-Duarte
está indexado por los ENTEROS $\{1,2,\dots,N\}$ (las dilataciones $\{k/t\}$). NO por los
primos. Este es el punto que la AAD necesita borrar y que yo voy a sostener.

### 2.2. El diccionario de Mellin, escrito exacto

**[CÁLCULO 159.3] (transformada de Mellin de las dilataciones).** La transformación de
Mellin $\mathcal M: L^2(0,\infty, dt/t) \to L^2(\tfrac12+i\mathbb R, \tfrac{ds}{2\pi})$,
$(\mathcal M f)(s) = \int_0^\infty f(t) t^{-s}\frac{dt}{t}$ (en la línea crítica $s=\tfrac12+i\xi$),
es una isometría (Plancherel para Mellin). De Doc 82 §7.4, la dilatación entera
$r_k(t) = \{k/t\}$ tiene transformada de Mellin (para $\mathrm{Re}\,s\in(0,1)$)
$$\mathcal M[r_k](s) \;=\; -\frac{\zeta(s)}{s}\,k^{-s}, \qquad \mathcal M[\mathbf 1_{(0,1)}](s) = \frac{1}{s}.$$
(El factor $\zeta(s)/s$ sale de $\int_0^\infty\{1/t\}t^{-s}\frac{dt}{t} = -\zeta(s)/s$ para
$0<\mathrm{Re}\,s<1$; la dilatación por $k$ multiplica por $k^{-s}$.)

**[PROPOSICIÓN 159.4] (la completitud de Nyman–Beurling en coordenadas espectrales).**
Vía $\mathcal M$, el criterio de Báez-Duarte es:
$$\mathrm{RH} \iff \frac1s \in \overline{\mathrm{span}}^{L^2(\frac12+i\mathbb R)}
\Bigl\{ \frac{\zeta(s)}{s}\,k^{-s} : k = 1,2,3,\dots \Bigr\}.$$
Equivalentemente, factorizando $\zeta(s)/s$ (no-nula c.t.p. en la línea), RH equivale a que
$\zeta(s)^{-1}$ esté en el cierre del span de las funciones $\{k^{-s}\}_{k\ge1}$ pesado por
$\zeta(s)/s$, i.e. al **sistema de potencias enteras $\{k^{-s} = e^{-s\log k}\}_{k\ge 1}$
con frecuencias $\{\log k\}_{k\ge 1}$.**

*Demostración.* Aplicación directa de la isometría de Mellin al enunciado de Báez-Duarte
(Doc 82, Teorema 1.3 y §7.4); la factorización usa $\zeta(s)\ne 0$ c.t.p. sobre
$\mathrm{Re}\,s = \tfrac12$ (cierto incondicionalmente: los ceros son numerables). $\square$

### 2.3. La distinción ℕ vs. primos — el corazón de la Vía 1

Ahora el acto adversarial decisivo. La AAD quiere que "la completitud de $\{p^{i\tau}\}$"
sea la completitud de Nyman–Beurling. La Prop. 159.4 muestra que el sistema de
Nyman–Beurling tiene frecuencias $\{\log k\}_{k\ge1}$ — **TODOS los enteros**, no solo los
primos. La relación entre los dos sistemas de frecuencias:
$$\{\log k\}_{k\ge1} \;=\; \Bigl\{\, \textstyle\sum_p a_p \log p \;:\; a_p\in\mathbb Z_{\ge0},\ \text{casi todos }0 \,\Bigr\}
\;=\; \mathbb Z_{\ge0}\text{-semigrupo generado por }\{\log p\}_p.$$

**[PROPOSICIÓN 159.5] (los dos sistemas NO son la misma completitud).** El sistema de
frecuencias de Nyman–Beurling $\{\log k\}_{k\ge1}$ es el semigrupo aditivo
multiplicativamente generado por $\{\log p\}_p$. La completitud de $\{e^{-s\log k}\}_{k\ge1}$
(que es RH-equivalente, Prop. 159.4) NO se reduce a la completitud lineal de
$\{e^{-s\log p}\}_p$ (que es la Lectura A, incondicional). Concretamente:
- $\{e^{-s\log p}\}_p = \{p^{-s}\}_p$ son los **generadores**; su span lineal cerrado es
  un objeto incondicional (es el primer "nivel" de la serie de Dirichlet).
- $\{e^{-s\log k}\}_k = \{n^{-s}\}_n$ incluye todos los **productos** $p_1^{a_1}\cdots$;
  reconstruir estos a partir de los primos es exactamente el producto de Euler
  $\sum_n n^{-s} = \prod_p(1-p^{-s})^{-1}$, una identidad sobre $\mathrm{Re}\,s=\tfrac12$
  que involucra $\zeta$.

*Demostración.* Que $\{\log k\}$ es el semigrupo aditivo generado por $\{\log p\}$ es
factorización única. Que el paso del span lineal de los generadores al span lineal de los
productos requiere $\zeta$: la función generatriz que empaqueta $\{n^{-s}\}_n$ a partir de
$\{p^{-s}\}_p$ es $\prod_p(1-p^{-s})^{-1}$, cuya evaluación c.t.p. sobre la línea crítica es
$\zeta(\tfrac12+i\xi)$; un span lineal de los $p^{-s}$ NO contiene los $n^{-s}$ compuestos
salvo que se permita la operación multiplicativa (no-lineal) codificada por Euler. La
completitud de Nyman–Beurling es de los $n^{-s}$, no de los $p^{-s}$. $\square$

### 2.4. El isomorfismo de Mellin "con cuidado" — qué transporta y qué no

El encargo pidió verificar el isomorfismo de Mellin con cuidado. El cuidado consiste en
esto: la transformación de Mellin SÍ lleva dilataciones $t\mapsto t/a$ a multiplicaciones
$a^{-s}$, y por tanto lleva $\{a^{i\tau}\}$ (caracteres del grupo multiplicativo
$(0,\infty)$) a exponenciales $\{e^{-i\tau\log a}\}$. En ese sentido, "dilataciones ↔
caracteres $\{a^{i\tau}\}$" es correcto y es un isomorfismo de grupos. **Pero el sistema
relevante para RH (Nyman–Beurling) usa dilataciones por ENTEROS $a=k$, no por primos.** El
isomorfismo de Mellin es fiel; lo que la AAD desliza es reemplazar "enteros" por "primos"
DESPUÉS del isomorfismo, y ese reemplazo NO es un paso de Mellin: es el producto de Euler.

**[PUENTE 159-A] (dónde aterriza la Vía 1).** La circularidad Nyman–Beurling NO se consuma
de forma directa, porque:
- La completitud RH-equivalente es la de $\{k^{-s}\}_{k\ge1}$ (enteros).
- La completitud incondicional (Lectura A, toro de Kronecker) es la de $\{p^{-s}\}_p$ /
  $\{p^{i\tau}\}_p$ (primos).
- El puente entre ambas es el producto de Euler sobre $\mathrm{Re}\,s=\tfrac12$, que ES
  $\zeta$ — luego cualquier intento de DEDUCIR la completitud-de-enteros (RH) desde la
  completitud-de-primos (incondicional) pasa por evaluar Euler en la línea crítica, donde
  vive el problema entero.

**Veredicto Vía 1: NO MATA por circularidad directa (los sistemas son distintos: ℕ≠primos),
pero deja la hebra marcada.** La hebra no es "trivialmente RH" por ser Nyman–Beurling
disfrazada — porque no lo es: el sistema de primos es estrictamente más pequeño que el de
enteros. Lo que la Vía 1 establece es el costo de pasar de uno a otro: un producto de Euler
sobre la línea crítica. Esto NO es una muerte; es la identificación del peaje. La muerte,
si la hay, tiene que venir de otra vía que muestre que ese peaje es impagable RH-libre.
**[GAP-159.A]:** ¿existe una manera de transportar la completitud-de-primos a una
conclusión de individuación SIN reconstituir los enteros (sin Euler en la línea)? Si la
respuesta es no, la Vía 1 se vuelve muerte; si sí, la hebra esquiva la Vía 1. No lo cierro
aquí.

---

## 3. Vía 2 — Confinamiento Bohr–Voronin al lado-valor

Esta es la vía con más fuerza letal. La tesis: la independencia ℚ-lineal de $\{\log p\}$
produce ÚNICAMENTE estructura sobre la σ-álgebra de los VALORES de $\zeta$ (el toro de
Kronecker / soporte de Bagchi), y la individuación (posición de ceros, inercia) NO es
medible respecto de esa σ-álgebra.

### 3.1. La σ-álgebra de valores y su generación diofántica

**[DEFINICIÓN 159.6] (σ-álgebra de valores).** Sea $D\subset\{\tfrac12<\sigma<1\}$ un disco
compacto. La medida límite de Bagchi $Q$ vive en $H(D)$ (funciones holomorfas con la
topología compacto-abierta). Sea $\Sigma_{\mathrm{val}}$ la σ-álgebra de Borel de $H(D)$
inducida por la ley de $\zeta(s,\omega)=\prod_p(1-\omega_p p^{-s})^{-1}$ con $\omega$
uniforme en $\mathbb T^\infty$. Todo evento sobre los VALORES de $\zeta$ en la franja (que
$\zeta$ esté cerca de una función dada, que tome cierto valor, etc.) es
$\Sigma_{\mathrm{val}}$-medible.

**[PROPOSICIÓN 159.7] (la independencia diofántica genera EXACTAMENTE $\Sigma_{\mathrm{val}}$).**
El único insumo aritmético del teorema límite de Bagchi (Doc 112 §2.4, §3.2) es la
independencia ℚ-lineal de $\{\log p\}$, que da la equidistribución de la órbita
$\tau\mapsto(p^{-i\tau})_p$ en $\mathbb T^\infty$ (Kronecker–Weyl). El soporte de $Q$ es
$$S = \{f\in H(D) : f(s)\ne 0\ \forall s\in D\}\cup\{0\}$$
([Bag81]; [Lau96, Caps. 5–6]; Doc 112 Prop. 2.6). Toda la estructura de $Q$ —su soporte,
sus momentos, la universalidad de Voronin— es función de la independencia diofántica más el
producto de Euler aleatorio; NINGÚN dato sobre la posición de los ceros de $\zeta$ entra en
la construcción de $Q$.

*Demostración.* Es el contenido del teorema de Bagchi tal como se usa en Doc 112: la
medida $Q$ se define por la ley del producto aleatorio, cuyo único insumo es la
independencia de los $\omega_p$ (reflejo de la independencia ℚ-lineal de $\{\log p\}$ vía
Kronecker–Weyl). El soporte $S$ se obtiene por el teorema de Hurwitz aplicado a los
límites de productos de Euler no-nulos. Nada de esto usa dónde están los ceros. $\square$

### 3.2. La inercia NO es $\Sigma_{\mathrm{val}}$-medible

**[PROPOSICIÓN 159.8] (ceguera estructural de la medida de valores a la individuación).**
El evento "ζ tiene un cero off-crítico en el disco $D$" no es decidible a partir de
$Q$, y más fuertemente: el conjunto de $\tau$ que testimonian la individuación (los $\tau$
para los que $\zeta(\cdot+i\tau)|_D$ está cerca de tener un cero off-crítico) tiene
$Q$-medida cero (densidad cero). La universalidad de Voronin vale IDÉNTICA bajo RH y bajo
¬RH.

*Demostración.* (a) Universalidad incondicional: el teorema de universalidad de Voronin
([Vor75]) y el teorema límite de Bagchi son INCONDICIONALES — no asumen RH y su enunciado
no cambia según RH sea verdadera o falsa (este es el punto central de Bagchi, citado en
Doc 112 §0 y la nota de "detector inútil" en §2.4(3)). La medida $Q$ es la misma en ambos
mundos. (b) Densidad cero de los testigos: por la Prop. 2.6 del Doc 112 (Bagchi + Hurwitz +
Portmanteau), bajo H(m) (¬RH con $m$ finito) el conjunto
$A_\varepsilon = \{\tau : \sup_D|\zeta(\cdot+i\tau)-\zeta|\le\varepsilon\}$ tiene densidad
SUPERIOR cero, porque las funciones cerca de $\zeta|_D$ (que tendría un cero off) están
fuera del soporte $S$ (que es no-nulas $\cup\{0\}$). Es decir: la individuación es un evento
$Q$-nulo. (c) Conclusión: un objeto $Q$-nulo no es decidible por ninguna funcional de $Q$;
la individuación es invisible a la σ-álgebra de valores. $\square$

### 3.3. El argumento de confinamiento, destilado

**[TEOREMA 159.9] (confinamiento al lado-valor — la Vía 2 mata la lectura ambiente).**
Sea $\mathsf P$ cualquier propiedad de individuación (forzar $F_{\mathrm{off}}=0$, decidir
la posición de un cero) y sea $\mathsf D$ el uso de la independencia ℚ-lineal de
$\{\log p\}$ como HECHO AMBIENTE (es decir, a través de cualquier funcional de la medida
límite $Q$ / de la órbita de Kronecker / de la universalidad de Voronin). Entonces
$\mathsf D$ no decide $\mathsf P$: toda conclusión obtenible de $\mathsf D$ es
$\Sigma_{\mathrm{val}}$-medible (Prop. 159.7), y $\mathsf P$ no lo es (Prop. 159.8). La
independencia diofántica, leída como estructura del toro de valores, VACÍA la oscilación de
valores (da la universalidad, la casi-periodicidad B², el soporte) pero es estructuralmente
ciega a la inercia.

*Demostración.* Composición de Prop. 159.7 (todo lo que $\mathsf D$ produce factoriza por
$Q$, es $\Sigma_{\mathrm{val}}$-medible) y Prop. 159.8 ($\mathsf P$ es $Q$-nulo / no
$\Sigma_{\mathrm{val}}$-medible). Una funcional medible de $Q$ no puede separar dos mundos
(RH/¬RH) que inducen el mismo $Q$. $\square$

**Veredicto Vía 2: MATA la lectura "independencia como hecho ambiente".** Esta es la lectura
A de §1.1, y es la lectura natural de la AAD ("la independencia diofántica produce el
toro, el toro produce la universalidad, la universalidad colapsa el defecto"). El Teorema
159.9 dice: NO — la universalidad es exactamente lo que NO distingue RH de ¬RH (Bagchi). La
hebra, leída como estructura del toro de Kronecker, está confinada al lado-valor y muere.

**[GAP-159.B] (la grieta que la Vía 2 NO cubre).** El Teorema 159.9 cubre el uso de la
independencia como hecho AMBIENTE (vía la medida $Q$, que es una funcional PROMEDIO en
$\tau$). NO cubre el uso de la independencia como condición CUANTITATIVA-PUNTUAL: una
medida de irracionalidad de $\{\log p\}$, o una cota de discrepancia del flujo de Kronecker
que controle la órbita en una ventana FIJA (el disco del cero), no una media en $\tau$.
Eso es precisamente lo que escapa a $\Sigma_{\mathrm{val}}$ porque NO es una funcional de
$Q$ (que promedia sobre $\tau$). El residuo de vida de la hebra es exactamente la Vía 3.

---

## 4. Vía 3 — Reintroducción de ceros (como Beurling–Malliavin en D157)

La Vía 2 confinó la lectura-ambiente. Queda la lectura cuantitativa-puntual (GAP-159.B).
La Vía 3 prueba la dicotomía: cualitativo = incondicional pero inútil; cuantitativo =
reintroduce los ceros.

### 4.1. La completitud CUALITATIVA: incondicional e inútil

**[PROPOSICIÓN 159.10] (la completitud cualitativa de $\{p^{i\tau}\}$ es incondicional).**
La independencia ℚ-lineal de $\{\log p\}$ (factorización única) implica, por Kronecker–Weyl,
que el flujo $\tau\mapsto(p^{i\tau})_p$ es minimal y equidistribuido en $\mathbb T^\infty$.
En particular el span lineal de $\{p^{i\tau}\}$ es completo en el sentido de Kronecker
(la órbita es densa). Esto es incondicional.

*Demostración.* Doc 112 Lemas 2.2 y 3.3: la independencia es factorización única, y
Kronecker–Weyl da minimalidad y equidistribución. $\square$

**[PROPOSICIÓN 159.11] (pero la completitud cualitativa es inútil para la individuación).**
La densidad de la órbita en $\mathbb T^\infty$ es un enunciado de PROMEDIO (la órbita visita
todo entorno con densidad positiva en $\tau$). Por la Obs. 2.4 / Prop. 2.6 del Doc 112, la
individuación (la bondad en el disco fijo del cero) vive en una coordenada de densidad cero,
invisible al promedio. La completitud cualitativa da exactamente el lado-promedio del
cuantificador maestro; no cruza.

*Demostración.* Es la traducción de la Obs. 2.4 de Doc 112 (la seminorma B² anula los
compactos) y de la Prop. 159.8 (los testigos de individuación son $Q$-nulos) al lenguaje de
órbitas: la densidad de órbita es positiva en $\tau$, pero la condición de individuación se
realiza en un subconjunto de $\tau$ de densidad cero. Densidad de órbita ⇏ presencia en el
subconjunto excepcional. $\square$

**Esto es exactamente la estructura del Doc 157 (T5/LP-152) y del Doc 112 (LP-112).** La
completitud cualitativa es la "candidata viva" que sobrevive como ENUNCIADO pero cuya
verificación de individuación falla. La hebra cualitativa es RH-libre pero inútil.

### 4.2. La completitud CUANTITATIVA: reintroduce los ceros — el paralelo exacto con D157

Para que la hebra CRUCE (no solo sobreviva), necesita una versión CUANTITATIVA: una cota
efectiva de la velocidad de equidistribución / del radio de completitud que sea fina hasta
la escala del disco del cero. Aquí reproduzco la muerte del Doc 157.

**[PROPOSICIÓN 159.12] (la cuantificación clásica reintroduce los ceros, como Beurling–Malliavin).**
Toda cuantificación de la completitud de $\{p^{i\tau}\}$ del tipo "radio de Beurling–Malliavin
/ densidad efectiva del conjunto de frecuencias $\{\log p\}$ suficiente para controlar
$\zeta$ en el disco $D$" reintroduce la cuenta de ceros, por el mismo mecanismo del Doc 157
Prop. 157.7.

*Demostración.* El teorema de Beurling–Malliavin (Doc 157 §3.3; Docs 82–85) cruza
densidad-espectral → control-puntual. La densidad espectral relevante para controlar
$\zeta$ en el disco del cero NO es la densidad cruda de $\{\log p\}$ (esa es incondicional:
$\#\{p\le e^u\}\sim e^u/u$ por PNT), sino la densidad de RESONANCIA — dónde la transformada
de la medida de primos crece, que por la fórmula explícita (Doc 157 identidad 152.E) ES la
densidad de ceros off. Cualquier versión cuantitativa de Beurling–Malliavin sobre las
frecuencias $\{\log p\}$ que sea fina hasta la escala del cero está, por el mismo argumento
de Doc 157, decidiendo la densidad de ceros en esa ventana. Círculo en el input de
Beurling–Malliavin: input (densidad de resonancia) = output (posición de ceros). $\square$

**Esto es la muerte por reintroducción de ceros, idéntica a D157.** Si la cuantificación
que la hebra necesita es de tipo "densidad efectiva del conjunto espectral", está muerta:
es Beurling–Malliavin otra vez, y reintroduce el divisor de $\zeta$.

### 4.3. La rendija: ¿hay una cuantificación diofántica que NO sea densidad de resonancia?

Aquí soy escrupulosamente honesto, porque es donde la muerte podría no consumarse.

La independencia ℚ-lineal de $\{\log p\}$ es un enunciado CUALITATIVO (sí/no sobre la
existencia de relaciones $\sum a_p\log p = 0$ con $a_p\in\mathbb Z$). Su forma cuantitativa
NATURAL no es una densidad de resonancia, sino una **medida de irracionalidad simultánea /
discrepancia del flujo de Kronecker**: cotas del tipo
$$\Bigl\| \sum_p a_p \log p \Bigr\| \;\ge\; \Phi\bigl((|a_p|)_p\bigr) \qquad (\text{distancia al entero más próximo}),$$
que controlan cuán bien la órbita $\tau\mapsto(p^{i\tau})_p$ se aproxima a un punto del toro
en función del tiempo $\tau$ — i.e. la discrepancia efectiva en una ventana de $\tau$.

**[PROPOSICIÓN 159.13] (la cuantificación diofántica genuina NO es, a priori, densidad de
resonancia).** La medida de irracionalidad / discrepancia del flujo de Kronecker de
$\{\log p\}$ es una propiedad de los NÚMEROS $\{\log p\}$ como puntos de $\mathbb R$
(teoría diofántica: aproximación simultánea, formas lineales en logaritmos), NO una
propiedad de la posición de los ceros de $\zeta$. La fórmula explícita / la identidad 152.E
conecta la densidad de RESONANCIA con los ceros, pero NO conecta la densidad de resonancia
con la discrepancia diofántica de $\{\log p\}$: son objetos distintos.

*Estatus.* **[GAP de literatura].** No conozco un teorema que (i) conecte la medida de
irracionalidad de $\{\log p\}$ con la densidad de ceros de $\zeta$, NI (ii) que use la
discrepancia diofántica de $\{\log p\}$ como condición de completitud espectral fina hasta
la escala del disco del cero para forzar individuación. Lo que SÍ está en la literatura:
(a) formas lineales en logaritmos (Baker; transcendencia de $\sum a_p\log p$) — pero esto
da independencia cualitativa y cotas de irracionalidad, no conexión con ceros; (b) la
universalidad/Bagchi usa solo la independencia cualitativa (Vía 2). La conexión que la
hebra necesitaría —discrepancia diofántica de $\{\log p\}$ ⟹ control puntual de $\zeta$ en
el disco del cero, SIN pasar por la densidad de resonancia— es el [GAP de literatura]
central, exactamente GAP-157.A de Doc 157, ahora afilado. NO lo afirmo ni lo refuto.

**Veredicto Vía 3: MATA la cuantificación clásica (densidad efectiva = Beurling–Malliavin =
reintroduce ceros), pero NO mata la cuantificación diofántica genuina (discrepancia /
medida de irracionalidad), cuya conexión con los ceros es desconocida.** La dicotomía
cualitativo-inútil / cuantitativo-reintroduce-ceros se cumple para la cuantificación VÍA
DENSIDAD. La grieta es: existe un tercer tipo de cuantificación (la diofántica-efectiva)
que no es, a priori, una densidad de resonancia. **[GAP-159.C]** = ese tercer tipo.

---

## 5. VEREDICTO

### 5.1. Cuál vía mata

| vía | qué ataca | resultado |
|---|---|---|
| **Vía 1 (Nyman–Beurling)** | circularidad: ¿es la completitud de $\{p^{i\tau}\}$ = Nyman–Beurling disfrazada? | **NO MATA.** El sistema RH-equivalente es de ENTEROS $\{k^{-s}\}$, no de primos $\{p^{-s}\}$; el puente entre ambos es el producto de Euler sobre Re s=½ (PUENTE 159-A). La circularidad es indirecta, no directa. Deja el peaje nombrado (GAP-159.A). |
| **Vía 2 (Bohr–Voronin)** | confinamiento: ¿vive todo lo diofántico en el lado-valor? | **MATA la lectura ambiente** (Teorema 159.9). La independencia como funcional de la medida límite $Q$ es $\Sigma_{\mathrm{val}}$-medible; la inercia es $Q$-nula (Bagchi: universalidad no distingue RH de ¬RH). Grieta: la cuantificación puntual escapa a $Q$ (GAP-159.B). |
| **Vía 3 (reintroducción de ceros)** | dicotomía cualitativo/cuantitativo | **MATA la cuantificación clásica** (Prop. 159.12: densidad efectiva = Beurling–Malliavin = reintroduce ceros, como D157). NO mata la cuantificación diofántica genuina (discrepancia / medida de irracionalidad), conexión con ceros desconocida (GAP-159.C). |

### 5.2. ¿Sobreviven las tres muertes?

**Veredicto preciso: matan DOS de las tres, pero las tres muertes NO se solapan de forma
que cierren la grieta. El complemento conjunto deja vivo UN objeto, no vacío.**

- La Vía 1 establece que la hebra NO es trivialmente RH (no es Nyman–Beurling disfrazada);
  por tanto la hebra es un objeto genuinamente distinto, no una circularidad obvia.
- La Vía 2 mata la lectura de la hebra como estructura del toro de valores (la lectura A,
  la más natural y la que la AAD sugiere). Tras la Vía 2, la única lectura que sobrevive
  es la cuantitativa-puntual (la independencia usada como condición efectiva en una
  ventana fija de $\tau$, no como hecho ambiente promediado).
- La Vía 3 mata la cuantificación-puntual SI ésta es de tipo densidad efectiva
  (Beurling–Malliavin). Pero deja viva la cuantificación de tipo
  diofántico-genuino (discrepancia del flujo de Kronecker / medida de irracionalidad de
  $\{\log p\}$), cuya conexión con los ceros NO está establecida.

**La intersección de los tres complementos es exactamente:**

> Una condición tauberiana espectral que use una propiedad CUANTITATIVA-DIOFÁNTICA de
> $\{\log p\}$ (discrepancia / medida de irracionalidad / aproximación simultánea del flujo
> de Kronecker en el disco fijo del cero) que (i) NO sea una funcional de la medida límite
> $Q$ (escapa a Vía 2), (ii) NO sea una densidad de resonancia (escapa a Vía 3), y (iii)
> NO reconstituya los enteros vía Euler en la línea crítica (escapa a Vía 1).

Este objeto NO es vacío como ESPACIO DE BÚSQUEDA: la medida de irracionalidad de
$\{\log p\}$ existe, es incondicional, y no es ni una funcional de $Q$ ni una densidad de
resonancia ni un producto de Euler. **Lo que es vacío, o no, es la IMPLICACIÓN: que esa
propiedad diofántica fuerce individuación.** Eso es el GAP de literatura central
(GAP-159.C = GAP-157.A afilado).

**No fuerzo la tercera muerte.** Sería deshonesto declarar "muerta" la hebra: he matado las
dos lecturas accesibles (ambiente y densidad-efectiva), pero la lectura
diofántica-efectiva genuina sobrevive porque NO conozco —y declaro no conocer— un teorema
que la conecte con los ceros ni uno que pruebe que no puede conectarse. La hebra está
REDUCIDA a su núcleo más delgado, idéntico al GAP-157.A, y ese núcleo NO está cerrado.

### 5.3. El estatus honesto de la grieta superviviente

La grieta superviviente es la MISMA de la pinza P43 (LP-112 / LP-152) y del GAP-157.A. Las
tres coordenadas independientes —recurrencia (Doc 112), tauberiana (Doc 157), y ahora la
completitud diofántica directa (este documento)— convergen en el mismo punto:
**¿una propiedad cuantitativa-diofántica de $\{\log p\}$ que NO sea ni promedio (funcional
de $Q$) ni densidad de resonancia (Beurling–Malliavin) puede forzar individuación?**

Esto NO es coincidencia: es que el muro tiene un único punto de paso candidato, y las tres
vías de ataque lo cercan sin cerrarlo. La convergencia de tres ataques independientes al
mismo GAP es, en sí, un hallazgo: refuerza que el GAP es real (no un artefacto de una sola
formulación) y que es estrecho (las tres vías matan todo lo que lo rodea).

---

## 6. Si sobrevive: qué tendría que ser verdad (el complemento)

Por mandato del encargo, entrego el complemento preciso: las condiciones que harían de la
hebra un cruce genuino. Cada una es un [GAP] o [DESEO] declarado.

**[CONDICIÓN C1] (existencia de un puente diofántico→individuación).** Tendría que existir
un teorema de la forma: *"si $\{\log p\}$ tiene medida de irracionalidad simultánea
$\le\Phi$ (cota diofántica efectiva, incondicional), entonces $\zeta$ no tiene ceros
off-críticos en el disco $D$"* — i.e. una implicación discrepancia-diofántica ⟹ no-cero,
SIN pasar por la fórmula explícita. Estatus: [GAP de literatura]; no se conoce tal teorema
ni su imposibilidad. Es la negación de la conclusión de la Vía 3.

**[CONDICIÓN C2] (no-factorización por la medida $Q$).** El puente C1 NO debe ser una
funcional de la medida límite de Bagchi $Q$ (de otro modo lo mata la Vía 2). Tendría que
usar la órbita de Kronecker en una ventana FIJA de $\tau$ (la ventana del cero), con
control de discrepancia efectiva, no la medida promediada. Esto es coherente con que la
discrepancia puntual escape a $\Sigma_{\mathrm{val}}$ (GAP-159.B), pero requiere que la
ventana fija contenga información de individuación — exactamente lo que el cuantificador
maestro de P43 declara difícil.

**[CONDICIÓN C3] (no-reconstitución de los enteros).** El puente C1 NO debe reconstituir
$\{n^{-s}\}_n$ a partir de $\{p^{-s}\}_p$ (de otro modo lo mata la Vía 1, vía Euler en la
línea). Tendría que operar con las frecuencias PRIMAS $\{\log p\}$ directamente, sin
formar productos — es decir, sin usar el producto de Euler sobre $\mathrm{Re}\,s=\tfrac12$.
Esto es exigente: la mayoría de los argumentos que ligan $\{p^{i\tau}\}$ con $\zeta$ pasan
por la serie/producto, que reconstituye los enteros.

**[CONDICIÓN C4] (la propiedad diofántica debe ser estrictamente más fina que PNT).** La
densidad cruda de $\{\log p\}$ es incondicional (PNT) y la misma bajo RH y ¬RH (Doc 112
Prop. 4.8(ii)); por tanto el puente C1 NO puede usar solo la densidad cruda. Tendría que
usar una propiedad de aproximación simultánea (medida de irracionalidad) que sí difiera
en su consecuencia espectral — una propiedad fina de $\{\log p\}$ como conjunto diofántico
que no se reduzca a contar primos.

**[CONDICIÓN C5] (selección no-genérica).** Por Prop. 159.8 / 159.11, los testigos de
individuación tienen densidad cero. El puente C1, para funcionar, tendría que ser un
mecanismo de SELECCIÓN NO-GENÉRICA (producir un punto de un conjunto excepcional), o bien
un argumento que evite seleccionar (una desigualdad uniforme que excluya el cero sin
exhibir un $\tau$). La medida de irracionalidad diofántica es del segundo tipo
(uniforme, no selecciona) — esta es la única razón por la que C5 no es inmediatamente
contradictoria con el cuantificador maestro: una cota diofántica uniforme NO selecciona un
$\tau$, controla TODOS. **Si existe una cota de discrepancia uniforme de $\{\log p\}$ que
implique individuación, esquivaría el cuantificador maestro porque no es existencial sino
universal.** Este es el punto más esperanzador del complemento, y el más incierto.

**Síntesis del complemento.** La hebra sobrevive como cruce genuino si y solo si existe una
propiedad diofántica EFECTIVA y UNIFORME de $\{\log p\}$ (no funcional de $Q$, no densidad
de resonancia, no Euler en la línea, más fina que PNT) que implique la ausencia de ceros
off-críticos. Las cinco condiciones C1–C5 son el perfil exacto de tal propiedad. Ninguna
es contradictoria; ninguna está establecida. Es el complemento honesto de tres muertes,
dos de las cuales se consumaron.

---

## Mensaje final

**¿Cuál vía mata?** **MATAN DOS DE TRES, pero NO cierran la grieta.** La Vía 1
(Nyman–Beurling) NO mata: el sistema RH-equivalente es de ENTEROS, no de primos, y el
puente entre ambos es el producto de Euler sobre la línea crítica — la hebra no es
circularidad disfrazada. La Vía 2 (Bohr–Voronin) MATA la lectura ambiente: la independencia
diofántica, leída a través de la medida límite de Bagchi / la universalidad de Voronin, es
$\Sigma_{\mathrm{val}}$-medible y estructuralmente ciega a la inercia (Bagchi: la
universalidad no distingue RH de ¬RH). La Vía 3 (reintroducción de ceros) MATA la
cuantificación clásica (densidad efectiva = Beurling–Malliavin = reintroduce ceros, como
D157), pero NO la cuantificación diofántica genuina. **La hebra NO muere del todo: queda
reducida a su núcleo más delgado —idéntico al GAP-157.A— una propiedad diofántica efectiva
y uniforme de $\{\log p\}$ que escape a las tres muertes. NO fuerzo la tercera muerte;
declaro el residuo.**

**Tres hallazgos:**

1. **[PROPOSICIÓN 159.5 + PUENTE 159-A]** — *La completitud de Nyman–Beurling es de los
   ENTEROS, no de los primos; el puente es Euler en la línea crítica.* La AAD confunde dos
   sistemas distintos: el RH-equivalente $\{k^{-s} = e^{-s\log k}\}_{k\ge1}$ (frecuencias =
   semigrupo aditivo generado por $\{\log p\}$) y el incondicional $\{p^{-s}\}_p$
   (generadores). Mellin es un isomorfismo fiel, pero NO transporta "enteros" a "primos":
   ese paso es el producto de Euler $\prod_p(1-p^{-s})^{-1} = \zeta$ evaluado en
   $\mathrm{Re}\,s=\tfrac12$. La hebra no es circularidad directa; el peaje de separar
   primos de enteros es un producto de Euler sobre la línea, donde vive el problema.

2. **[TEOREMA 159.9 + PROPOSICIÓN 159.8]** — *La independencia diofántica está confinada al
   lado-valor; la inercia es $Q$-nula.* Todo lo que la independencia ℚ-lineal produce como
   hecho ambiente factoriza por la medida límite de Bagchi $Q$ (su único insumo aritmético,
   Prop. 159.7) y es $\Sigma_{\mathrm{val}}$-medible. Pero la universalidad de Voronin es
   incondicional —idéntica bajo RH y ¬RH (Bagchi)— y los testigos de individuación tienen
   $Q$-medida cero (Prop. 2.6 de D112). La hebra, leída como estructura del toro de
   Kronecker, vacía la oscilación de valores pero es estructuralmente ciega a la inercia.
   Esta es la muerte más limpia: la lectura natural de la AAD muere por confinamiento.

3. **[PROPOSICIÓN 159.12 + 159.13 + GAP-159.C]** — *La cuantificación se bifurca: densidad
   reintroduce ceros, diofántica-genuina no está conectada.* Toda cuantificación de la
   completitud vía densidad efectiva es Beurling–Malliavin y reintroduce la cuenta de ceros
   (idéntico a D157 Prop. 157.7: densidad de resonancia = densidad de ceros off). PERO la
   cuantificación natural de la independencia diofántica NO es una densidad — es una medida
   de irracionalidad / discrepancia del flujo de Kronecker, un objeto de teoría diofántica
   pura (formas lineales en logaritmos) cuya conexión con los ceros de $\zeta$ es un
   [GAP de literatura]. La supervivencia de la hebra depende enteramente de si existe un
   puente discrepancia-diofántica ⟹ individuación que sea uniforme (no selecciona un $\tau$,
   esquivando el cuantificador maestro por la puerta universal en vez de la existencial) —
   las cinco condiciones C1–C5 del §6 son su perfil exacto.

---

## Referencias

**Internas (backward-only):** Doc 157 (catálogo tauberiano T1–T5, Teorema 157.10 no-go
local, Prop. 157.7 densidad de resonancia = ceros, GAP-157.A grieta diofántica, identidad
152.E); Doc 112 (LP-112, teorema límite de Bagchi y soporte S = {no-nulas}∪{0},
Prop. 2.6 densidad cero de testigos, independencia ℚ-lineal en tres niveles, Lemas 2.2/3.1–3.3,
Davenport–Heilbronn); Docs 82 y 85 (criterio Nyman–Beurling–Báez-Duarte, diccionario de
Mellin $\mathcal M[\{k/t\}] = -\zeta(s)k^{-s}/s$, completitud incondicional del span lineal
vs. densidad de la clase no-lineal); P43 (Principio 3.1, cuantificador maestro
genérico/excepcional, §4 valor/inercia).

**Literatura (publicada, verificable salvo marca):**
- [Nym50] B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain
  Function Spaces*, Tesis, Univ. de Uppsala, 1950. (Criterio de completitud para RH en
  $L^2(0,1)$.)
- [Beu55] A. Beurling, *A closure problem related to the Riemann zeta-function*, Proc. Nat.
  Acad. Sci. USA 41 (1955), 312–314. (Reformulación en $H^2$; RH ⟺ $\mathbf 1_{(0,1)}$ en
  el cierre de las dilataciones de $\{1/t\}$.)
- [BD03] L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann
  hypothesis*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat.
  Appl. 14 (2003), 5–11. (Versión discreta con dilataciones enteras; RH ⟺ $d_N^2\to0$.)
- [Bag81] B. Bagchi, *The statistical behaviour and universality properties of the Riemann
  zeta-function and other allied Dirichlet series*, Tesis, Indian Statistical Institute,
  Calcuta, 1981. (Teorema límite funcional incondicional en $H(D)$; soporte de la medida
  límite; la universalidad NO distingue RH de ¬RH.)
- [Bag87] B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta
  Math. Hungar. 50 (1987), 227–240. (Recurrencia fuerte ⟺ RH.)
- [Vor75] S. M. Voronin, *Theorem on the "universality" of the Riemann zeta-function*, Izv.
  Akad. Nauk SSSR Ser. Mat. 39 (1975), 475–486. (Universalidad de Voronin; incondicional.)
- [Lau96] A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, Dordrecht,
  1996. (Caps. 5–6: teorema límite en $H(D)$ y soporte $S = \{f\text{ sin ceros}\}\cup\{0\}$;
  exposición estándar del aparato de Bagchi.)
- [BM62] A. Beurling, P. Malliavin, *On Fourier transforms of measures with compact
  support*, Acta Math. 107 (1962), 291–309. (Cuasi-analiticidad; rigidez de medidas.)
- [BM67] A. Beurling, P. Malliavin, *On the closure of characters and the zeros of entire
  functions*, Acta Math. 118 (1967), 79–93. (Radio de Beurling–Malliavin; completitud de
  exponenciales ⟺ densidad efectiva del conjunto de frecuencias.)
- [Boh18] H. Bohr, *Zur Theorie der allgemeinen Dirichletschen Reihen*, Math. Ann. 79
  (1918), 136–156. (Casi-periodicidad uniforme de series de Dirichlet en convergencia
  absoluta — el toro de Kronecker en $\sigma>1$.)
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev.
  D. R. Heath-Brown), Oxford Univ. Press, 1986. (Plancherel para Mellin; valor medio
  cuadrático.)
- [Wey16] H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Math. Ann. 77 (1916),
  313–352. (Equidistribución; Kronecker–Weyl en el toro.)

*Fin del Documento 159.*
</content>
</invoke>
