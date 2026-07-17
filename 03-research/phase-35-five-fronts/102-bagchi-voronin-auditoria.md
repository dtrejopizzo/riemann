# Doc 102 — Auditoría del criterio de Bagchi: recurrencia fuerte y universalidad de Voronin

**Phase 35 — Cinco frentes · junio 2026**
**Autor: David Alejandro Trejo Pizzo**
**Estado: auditoría completa — mecanismo pasado por el discriminador D0 (I1, I2a, I2b, I3, I4)**

---

## 0. Resumen ejecutivo

Este documento cierra una laguna explícita del programa: la "universalidad" fue auditada
únicamente en el sentido GUE / matrices aleatorias (gap-universality, FAIL I1/I3 en
`meta-docs/DISCRIMINATOR-hardening-phase-A.md`). La **universalidad de Voronin** —la
auto-aproximación de $\zeta$ en la franja $1/2<\mathrm{Re}(s)<1$— y el **criterio de
Bagchi** (RH $\iff$ recurrencia fuerte de $\zeta$) nunca pasaron por el discriminador.
Son objetos distintos de la estadística GUE: viven en dinámica topológica y teoría
ergódica, no en estadística espectral.

Resultados de la auditoría:

1. La dirección difícil del criterio de Bagchi (recurrencia $\Rightarrow$ RH) contiene un
   **mecanismo de amplificación** (Rouché + densidad de ceros incondicional) que **no es
   una positividad**: es el único mecanismo del corpus que convierte UN cero off-crítico
   en una contradicción con un teorema incondicional. El mecanismo en sí es no-circular.
2. La circularidad no desaparece: se **reubica en la premisa**. La recurrencia fuerte es
   RH-equivalente (Teorema de Bagchi), y su única vía de prueba conocida (universalidad)
   exige que la función objetivo sea no nula — exactamente la información que falta.
3. **Hallazgo principal (pregunta iv):** la obstrucción "órbita individual vs. órbita
   genérica" del marco ergódico de Bagchi **NO** es una falla de unicidad ergódica (el
   flujo de Kronecker en el toro de Bohr es minimal y únicamente ergódico, y el punto
   aritmético $\omega_0$ **es recurrente en el toro, incondicionalmente**). La obstrucción
   es la **divergencia de la observable de Euler sobre la órbita aritmética**: la
   pertenencia de la órbita de $\omega_0$ al conjunto de convergencia de la observable es
   ella misma RH-equivalente (Proposición 7.2). Esto identifica la obstrucción ergódica
   con **MW-2** (muro de propagación aritmética) palabra por palabra, y su verificación
   con **MW-7** (barrera de Hadamard).
4. Discriminador: **I1 ✅ · I2a ◐ · I2b ❌ · I3 ✅ · I4 ✅ → FAIL I2b**, el mismo perfil
   que Connes (estructura independiente real, sin teorema decisivo).

**VEREDICTO: RUTA CERRADA** como vía de prueba — con un activo trasladable registrado
(§9): el amplificador Rouché-densidad, único mecanismo no-CAP e individual-resolving del
corpus.

---

## 1. Posición en el programa: la laguna que este doc cierra

La tabla adversarial de `DISCRIMINATOR-hardening-phase-A.md` audita ~30 programas. Las
entradas "RMT (Katz–Sarnak, CFKRS)" y "Montgomery pair correlation" cubren la
universalidad en sentido *estadístico-espectral* (FAIL I1/I3: estadística, no aritmética,
agregada). La auditoría de Phase 24/25 (`phase-25/01-audit-classical.md`) tocó dos
mecanismos vecinos:

- **Mecanismo 9 (casi-periodicidad de Bohr):** veredicto "Dead end — no da información
  sobre $b_j$". La casi-periodicidad muestra que un cero off-crítico "reaparece
  aproximadamente" para $T$ arbitrariamente grandes, pero sin cota inferior sobre $b_j$.
- **Mecanismo 4 (Deuring–Heilbronn):** veredicto "Dead end — región espectral equivocada"
  (repulsión cerca de $\mathrm{Re}(s)=1$, alimentada por el producto de Euler cerca de 1).

Ninguna de las dos entradas es el criterio de Bagchi. El criterio de Bagchi es más fuerte
que la casi-periodicidad cualitativa del Mecanismo 9 en dos puntos decisivos: (a) la
recurrencia es **con densidad inferior positiva** (no solo "$T$ arbitrariamente grandes"),
y (b) la dirección recursiva usa esa densidad para **chocar contra un teorema
incondicional** ($N(\sigma,T)=o(T)$), cosa que la casi-periodicidad sola no logra. La
pregunta de si esto pasa I2a quedó sin formular. Este doc la formula y la responde.

---

## 2. Enunciados verificados (literatura)

Todos los enunciados de esta sección fueron verificados contra el survey de Matsumoto
(*A survey on the theory of universality for zeta and L-functions*, arXiv:1407.4216,
2014; texto completo consultado), que a su vez expone con cuidado el contenido de la
tesis no publicada de Bagchi. Notación de Matsumoto: $D(a,b)=\{s:a<\sigma<b\}$;
$H^c(K)$ = funciones continuas en $K$, holomorfas en el interior; $H_0^c(K)\subset
H^c(K)$ = las que además **no se anulan en $K$**.

### 2.1 Voronin 1975 — forma original (disco)

**Teorema (Voronin 1975).** *Sea $K(r)$ el disco cerrado de centro $3/4$ y radio $r$,
con $0<r<1/4$. Para toda $f\in H_0^c(K(r))$ y todo $\varepsilon>0$ existe $\tau>0$ tal que*
$$\max_{s\in K(r)}\,|\zeta(s+i\tau)-f(s)|<\varepsilon.$$

*Referencia:* S. M. Voronin, "Theorem on the 'universality' of the Riemann
zeta-function", Izv. Akad. Nauk SSSR Ser. Mat. **39** (1975), 475–486; trad. inglesa
Math. USSR-Izv. **9** (1975), 443–453. La prueba original ya contiene (implícitamente)
que el conjunto de tales $\tau$ tiene densidad inferior positiva.

### 2.2 Forma moderna (franja; Bagchi, Reich, Gonek)

**Teorema 2.1 (universalidad, forma moderna; Matsumoto Thm. 1).** *Sea $K$ un compacto
de $D(1/2,1)$ con complemento conexo, $f\in H_0^c(K)$, $\varepsilon>0$. Entonces*
$$\liminf_{T\to\infty}\ \frac{1}{T}\,\mathrm{meas}\Big\{\tau\in[0,T]\ :\ \sup_{s\in K}|\zeta(s+i\tau)-f(s)|<\varepsilon\Big\}\;>\;0.$$

Tres pruebas conocidas: Voronin (reordenamiento de Pecherskiĭ en espacios de Hilbert),
Good/Gonek, y la prueba probabilística de Bagchi (tesis 1981) — §3.

### 2.3 Bagchi 1981/1987 — recurrencia fuerte

**Definición.** $\zeta$ es **fuertemente recurrente** en $D(1/2,1)$ si para todo compacto
$K\subset D(1/2,1)$ con complemento conexo y todo $\varepsilon>0$:
$$(\mathrm{SR})\qquad \liminf_{T\to\infty}\ \frac{1}{T}\,\mathrm{meas}\Big\{\tau\in[0,T]\ :\ \sup_{s\in K}|\zeta(s+i\tau)-\zeta(s)|<\varepsilon\Big\}\;>\;0.$$

**Teorema 2.2 (Bagchi; Matsumoto Thm. 20).** *RH es verdadera $\iff$ (SR) vale en
$D(1/2,1)$.*

*Referencias:* B. Bagchi, *The statistical behaviour and universality properties of the
Riemann zeta-function and other allied Dirichlet series*, tesis, Indian Statistical
Institute, Calcuta, 1981 (no publicada; contenido expuesto en el libro de Laurinčikas
1996 y en Matsumoto §1, §9); B. Bagchi, "Recurrence in topological dynamics and the
Riemann hypothesis", Acta Math. Hungar. **50** (1987), 227–240 (la formulación
dinámico-topológica; el enunciado RH $\iff$ (SR) verificado vía fuentes secundarias;
el texto completo del paper de 1987 no fue accesible — los detalles internos específicos
de ese paper que cito van marcados). Extensiones: el propio Bagchi a $L$-funciones de
Dirichlet; R. Steuding a zetas de Beurling.

### 2.4 El input incondicional del lado de densidad

**Teorema 2.3 (densidad de ceros, incondicional).** *Para $\sigma>1/2$ fijo,
$N(\sigma,T)=\#\{\rho:\zeta(\rho)=0,\ \mathrm{Re}\,\rho\ge\sigma,\ 0\le\mathrm{Im}\,\rho\le T\}=o(T)$.*

Esto NO requiere RH. Carlson (1920): $N(\sigma,T)\ll T^{4\sigma(1-\sigma)+\varepsilon}$,
y $4\sigma(1-\sigma)<1$ para $\sigma>1/2$; Ingham (1940) mejora el exponente. El
precursor cualitativo es Bohr–Landau (1914). Matsumoto cita exactamente esta forma
($N(T;\sigma_1,\sigma_2;\zeta)=o(T)$) como el ingrediente que mata la universalidad
fuerte de $\zeta$ (su Corolario 2).

---

## 3. La maquinaria de la prueba de universalidad (prueba de Bagchi)

Para localizar dónde se rompe todo, hay que tener los cinco módulos de la prueba a la
vista. Seguimos la arquitectura de Bagchi (expuesta en Laurinčikas 1996, Steuding LNM
1877 cap. 5, Matsumoto §1).

**Módulo 1 — el toro de Bohr.** $\Omega=\prod_p \mathbb{T}_p$, producto de círculos
unitarios indexados por los **primos**, compacto, con medida de Haar $m_H$. Un punto
$\omega=(\omega(p))_p$ es una elección de fase por primo ("carácter generalizado").

**Módulo 2 — el flujo de Kronecker.** $T_\tau(\omega)=(p^{-i\tau}\omega(p))_p$. Los
caracteres no triviales de $\Omega$ son productos finitos $\prod_p\omega(p)^{n_p}$, sobre
los que el flujo actúa por $e^{-i\tau\sum_p n_p\log p}$. Como $\{\log p\}_p$ es
**linealmente independiente sobre $\mathbb{Q}$** (= factorización única en $\mathbb{Z}$),
$\sum n_p\log p\neq0$ para todo carácter no trivial: el flujo es **ergódico** respecto de
$m_H$. Este es el input aritmético real de toda la teoría.

**Módulo 3 — el elemento aleatorio.** Para $\omega\in\Omega$ y $s\in D(1/2,1)$:
$$\zeta(s,\omega)=\prod_p\big(1-\omega(p)\,p^{-s}\big)^{-1}.$$
Para $m_H$-casi todo $\omega$, el producto converge en $H(D(1/2,1))$ (topología compacta-
abierta). La razón: las variables $\omega(p)$ son independientes con $\mathbb{E}[\omega(p)]=0$,
y la serie aleatoria $\sum_p\omega(p)p^{-s}$ converge c.s. para $\sigma>1/2$ (tres series
de Kolmogorov / martingala $L^2$, $\sum_p p^{-2\sigma}<\infty$). **La aleatorización
restaura el producto de Euler en la franja** — esto será central en §7.

**Módulo 4 — teorema límite funcional (incondicional).** Las distribuciones empíricas de
los shifts, $P_T(A)=\frac1T\mathrm{meas}\{\tau\in[0,T]:\zeta(\cdot+i\tau)|_D\in A\}$,
convergen débilmente en $H(D)$ a la ley $P_\zeta$ de $\zeta(\cdot,\omega)$. La prueba usa:
aproximación de $\zeta$ por productos/series absolutamente convergentes regularizados, la
ergodicidad del Módulo 2 vía el **teorema de Birkhoff–Khinchin** (Matsumoto §10 lo señala
como el punto ergódico exacto de la prueba de Bagchi), y estimaciones de media cuadrática
de $\zeta$ en $\sigma>1/2$ — todas incondicionales.

**Módulo 5 — teorema de soporte + Mergelyan + densidad positiva.** El soporte de
$P_\zeta$ en $H(D)$ es
$$S=\{f\in H(D)\ :\ f(s)\neq0\ \forall s\in D\}\cup\{0\}.$$
La densidad ("cada $f$ no nula es alcanzable") viene de la independencia lineal de
$\{\log p\}$ vía Kronecker–Weyl: las fases $\omega(p)$ pueden orientarse para aproximar
cualquier $\log f$ dado (lema de densidad $L^2$ / reordenamiento de Pecherskiĭ en la
prueba de Voronin). El cierre ("nada con ceros está en el soporte") es **el teorema de
Hurwitz**: un límite en $H(D)$ de funciones holomorfas sin ceros es sin ceros o
idénticamente nulo — y cada producto parcial $\prod_{p\le X}(1-\omega(p)p^{-s})^{-1}$ no
se anula. Mergelyan reduce compactos $K$ con complemento conexo a polinomios. Finalmente,
$f\in\mathrm{supp}\,P_\zeta$ + convergencia débil $\Rightarrow$ toda vecindad de $f$ tiene
masa límite positiva $\Rightarrow$ densidad inferior positiva de $\tau$. ∎

**Dónde entra la no-anulación de la función objetivo — con precisión quirúrgica:** en el
Módulo 5 y solo ahí. La prueba aproxima $\log f$ por $\log$ de productos de Euler
truncados aleatorios; si $f$ tiene un cero en $K$, $\log f$ no existe en $K$, y por
Hurwitz $f\notin S=\mathrm{supp}\,P_\zeta$: la masa límite de toda vecindad
suficientemente pequeña de $f$ es **cero**. La maquinaria no se degrada gradualmente:
da exactamente densidad nula para objetivos con ceros. (Esto es consistente, no
contradictorio, con la dirección Rouché de §4.2.)

---

## 4. Las dos direcciones del Teorema de Bagchi (pregunta i)

### 4.1 RH $\Rightarrow$ recurrencia fuerte

Bajo RH, $\zeta$ es holomorfa y **no nula** en $D(1/2,1)$ (el polo $s=1$ está fuera; los
ceros críticos están en el borde $\sigma=1/2$, fuera del abierto). Entonces, para todo
compacto $K\subset D(1/2,1)$ con complemento conexo, $\zeta|_K\in H_0^c(K)$: la propia
$\zeta$ es un objetivo admisible del Teorema 2.1. Aplicándolo con $f=\zeta$ se obtiene
(SR). ∎

Obsérvese la asimetría lógica: esta dirección consume la universalidad (incondicional)
más **un solo bit condicional** — "$\zeta\in H_0^c(K)$", es decir, no-anulación, es decir,
RH misma. RH no se usa en ninguna estimación: se usa únicamente como certificado de
admisibilidad del objetivo.

### 4.2 Recurrencia fuerte $\Rightarrow$ RH (la dirección difícil)

Supongamos (SR) y, por contradicción, un cero $\rho_0=\beta_0+i\gamma_0$ con
$\beta_0>1/2$. Elegimos $\delta>0$ pequeño tal que el disco cerrado
$\bar B(\rho_0,\delta)\subset D(1/2,1)$ y $\zeta$ no tenga otros ceros en él, y tomamos
$$\varepsilon\ :=\ \tfrac12\min_{|s-\rho_0|=\delta}|\zeta(s)|\ >\ 0.$$
Por (SR) aplicada a $K=\bar B(\rho_0,\delta)$, el conjunto
$A_\varepsilon=\{\tau:\sup_{s\in K}|\zeta(s+i\tau)-\zeta(s)|<\varepsilon\}$ tiene densidad
inferior positiva $c>0$. Para cada $\tau\in A_\varepsilon$, sobre el círculo
$|s-\rho_0|=\delta$:
$$|\zeta(s+i\tau)-\zeta(s)|\ <\ \varepsilon\ <\ \min_{|s-\rho_0|=\delta}|\zeta(s)|\ \le\ |\zeta(s)|,$$
y por el **teorema de Rouché**, $\zeta(\cdot+i\tau)$ tiene en $B(\rho_0,\delta)$ tantos
ceros como $\zeta$: al menos uno. Es decir, $\zeta$ tiene un cero en
$B(\rho_0+i\tau,\delta)$, con $\mathrm{Re}>\beta_0-\delta>1/2$.

Cuántos ceros produce esto: $A_\varepsilon\cap[0,T]$ tiene medida $\ge cT$ para $T$
grande; un cero dado puede ser contado por los $\tau$ de un intervalo de longitud
$\le2\delta$; luego
$$N\big(\beta_0-\delta,\ T+\delta\big)\ \ge\ \frac{cT}{2\delta}\ \gg\ T.$$
Esto contradice $N(\sigma,T)=o(T)$ para $\sigma=\beta_0-\delta>1/2$ (Teorema 2.3,
**incondicional**). Luego no hay cero off-crítico. ∎

(El mismo esqueleto prueba el Teorema 11 de Matsumoto: "universalidad fuerte
$\Rightarrow N\ge CT$ ceros", y su Corolario 2: $\zeta$ **no puede** ser fuertemente
universal — no puede aproximar objetivos con ceros — precisamente por $N(\sigma,T)=o(T)$.)

### 4.3 Observación de localización (nueva, menor)

Para refutar **un** cero hipotético $\rho_0$ no se necesita (SR) completa: basta UNA
instancia — el compacto $K=\bar B(\rho_0,\delta)$ y el $\varepsilon(\rho_0,\delta)$
concreto de §4.2. La premisa mínima del amplificador es puntual, no uniforme. Esto no
ayuda a probarla (sigue dependiendo del cero hipotético, que no conocemos), pero importa
para el discriminador: el mecanismo es **individual-resolving** (I3 ✅), una rareza
absoluta en el corpus.

---

## 5. El mecanismo de amplificación bajo la lupa (pregunta ii)

### 5.1 Qué es y por qué no es una positividad

El paso §4.2 tiene una estructura única en todo el corpus auditado:

> **Amplificación:** una propiedad de recurrencia (densidad positiva de auto-retornos)
> **replica** un único cero off-crítico en una familia de $\gg T$ ceros off-críticos, y
> la familia choca contra una cota de densidad **incondicional**.

Compárese con el inventario de mecanismos del programa:

- **No es CAP.** No hay forma cuadrática, no hay center-definiteness, no hay
  "$\lambda_{\min}\ge0$ equivalente a RH". La contradicción es de **conteo**: $\gg T$
  contra $o(T)$. El input que produce la contradicción (Carlson/Ingham) es un teorema
  real, incondicional, del lado correcto.
- **No es el patrón MW-4** (signo equivocado): no se necesita cota superior de
  positividad alguna; la densidad de ceros es exactamente el tipo de cota que las
  herramientas incondicionales SÍ saben dar (FAIL I3 en su uso directo — "density, not
  absence" — pero aquí la densidad se usa como *techo* contra el cual estrellar la
  amplificación, no como detector de ausencia).
- **Inversión de Deuring–Heilbronn.** D–H (auditado, Mecanismo 4 de Phase 25) es
  *repulsión*: un cero excepcional cerca de $\mathrm{Re}(s)=1$ **expulsa** a los demás; el
  motor es el producto de Euler cerca de 1 y no alcanza la franja (muro de Paley–Wiener,
  Phases 22–23). Bagchi es *replicación*: un cero off-crítico, dado el insumo de
  recurrencia, **multiplica** copias de sí mismo dentro de la franja. D–H consume un
  cero hipotético y produce una restricción condicional sobre otros ceros; Bagchi consume
  un cero hipotético MÁS recurrencia y produce una **contradicción absoluta**. Son los
  dos únicos mecanismos "dinámicos sobre ceros individuales" del corpus, y tienen
  direcciones opuestas. D–H falló por región espectral; el amplificador de Bagchi opera
  exactamente en la región correcta, $D(1/2,1)$.

**Respuesta directa a la pregunta (ii):** sí, es el único mecanismo del corpus que
convierte teoremas de densidad-cero en una contradicción, y el mecanismo *aislado* no
falla I2a: usa dos inputs genuinos e incondicionales (equidistribución de Kronecker–Weyl
en la maquinaria que produciría la premisa; Carlson/Ingham en el techo). Pero un
mecanismo no es un criterio.

### 5.2 Dónde quedó la circularidad: relocalizada, no eliminada

El Teorema 2.2 dice que la premisa (SR) es **equivalente** a RH. Entonces el esquema
completo es:

$$\underbrace{(\mathrm{SR})}_{\text{RH-equivalente}}\ \xRightarrow{\ \text{amplificador (no circular)}\ }\ \mathrm{RH}.$$

La situación es estructuralmente idéntica a la de Connes en la tabla de Phase A: una
maquinaria independiente real (allí el espacio de clases de adeles; aquí la dinámica de
Bohr–Kronecker con su input de factorización única) que ejecuta todo el trabajo **excepto
el último paso**, y el último paso — probar (SR), allí probar la positividad de Weil — re-
encodea RH. La diferencia con un FAIL I2a puro (Li, Báez-Duarte, etc.) es que aquí el
trabajo no-circular es masivo y produce teoremas incondicionales colaterales (§6.3). La
clasificación correcta es por tanto **FAIL I2b**, no FAIL I2a: existe input independiente
(I2a ◐/✅), falta el teorema decisivo que supla la premisa.

---

## 6. ¿Se puede probar la recurrencia fuerte sin RH? (pregunta iii)

### 6.1 El punto exacto de ruptura

Por §3, la única obstrucción es la admisibilidad del objetivo: $\zeta\in H_0^c(K)$. La
prueba de universalidad se rompe en el Módulo 5 si el objetivo tiene un cero, y se rompe
de forma binaria (densidad exactamente nula, por Hurwitz + soporte). No hay versión
"degradada" de la prueba que dé densidad positiva para objetivos con ceros pequeños: el
Corolario 2 de Matsumoto (vía el propio amplificador de §4.2 contra $N(\sigma,T)=o(T)$)
**prohíbe** que exista tal versión. La maquinaria es así *exactamente autoconsistente*:
prueba (SR) si y solo si se le certifica la no-anulación de $\zeta$, y la no-anulación de
$\zeta$ es RH. No hay holgura.

### 6.2 Test MW-7 (barrera de Hadamard): ¿(SR) es verificable sin conocer posiciones de ceros?

**No.** En las dos direcciones:

- (SR) $\Rightarrow$ no hay ceros off-críticos (§4.2): verificar (SR) implica localizar
  ceros (negativamente). A la inversa, por §4.1, certificar (SR) por la única vía
  conocida exige certificar antes la no-anulación en la franja. La propiedad "(SR)" es
  una propiedad de $\zeta$ cuya verificación **es** un control de posiciones de ceros:
  Rouché funciona en ambas direcciones — la cercanía $|\zeta(s+i\tau)-\zeta(s)|<\varepsilon$
  en un disco transporta la estructura de ceros del disco. En el lenguaje de MW-7: la
  recurrencia fuerte NO es una propiedad de $\zeta$ "verificable sin conocer posiciones
  de ceros"; es una codificación dinámica de las posiciones de ceros. MW-7 aplica.

### 6.3 ¿Está el conjunto de $\tau$ recurrentes controlado por estructura aritmética accesible? La familia $d$ y el punto diagonal

Aquí está el material más informativo de la literatura, porque mide *hasta dónde* llega
el input aritmético incondicional. Considérese la auto-aproximación a dos velocidades
(Matsumoto §9, fórmula (9.3)):
$$(\mathrm{SR}_d)\qquad \liminf_{T\to\infty}\frac1T\,\mathrm{meas}\Big\{\tau\in[0,T]:\sup_{s\in K}|\zeta(s+i\tau)-\zeta(s+i d\tau)|<\varepsilon\Big\}>0.$$
Nótese que $(\mathrm{SR}_0)=(\mathrm{SR})$ = RH (Teorema 2.2). Estado verificado
(Matsumoto Thm. 21 y alrededores):

- **$d$ irracional algebraico:** $(\mathrm{SR}_d)$ vale incondicionalmente (Nakamura
  2010, Arch. Math. 95) — vía universalidad conjunta, usando que
  $\{\log p^{d_j}\}$ es linealmente independiente sobre $\mathbb{Q}$ por el **teorema de
  Baker** (formas lineales en logaritmos).
- **$d$ irracional trascendente:** $(\mathrm{SR}_d)$ vale (Pańkowski, vía el **teorema de
  los seis exponenciales**).
- **$d=a/b$ racional no nulo, $(a,b)=1$, $|a-b|\neq1$:** $(\mathrm{SR}_d)$ vale
  (Garunkštis; Nakamura; corrección Nakamura–Pańkowski, Arch. Math. 99 (2012)).
- **$\log\zeta$ en lugar de $\zeta$:** la variante (9.4) vale **para todo $d\neq0$**; y
  si valiera en $d=0$ implicaría RH.

Es decir: la estructura aritmética accesible incondicionalmente (independencia de
$\{\log p\}$, Baker, seis exponenciales — ¡teoría de números trascendente real, input I2a
genuino!) controla el conjunto de $\tau$ recurrentes para **toda** velocidad relativa
$d\neq0$ (salvo el caso racional $|a-b|=1$, técnico), y se detiene **exactamente** en el
punto diagonal $d=0$, que es RH. La razón estructural: para $d\neq0$ las dos copias
$\zeta(s+i\tau)$, $\zeta(s+id\tau)$ recorren el toro con velocidades distintas y hay
equidistribución *relativa* que explotar — las fases relativas $p^{-i(1-d)\tau}$
equidistribuyen, y la independencia sobre $\mathbb{Q}$ del sistema conjunto
$\{\log p,\,d\log p\}$ se certifica con Baker o los seis exponenciales. En $d=0$ el
desplazamiento relativo es idénticamente cero: no queda ninguna equidistribución relativa
disponible, y el problema colapsa a la posición **absoluta** del punto aritmético en el
toro (§7). El límite $d\to0$ no transfiere nada: la densidad positiva de
$(\mathrm{SR}_d)$ para $d\neq0$ compara dos puntos *genéricos uno respecto del otro*,
mientras que $(\mathrm{SR}_0)$ exige que el punto aritmético sea genérico *respecto de sí
mismo* — la no-uniformidad exacta es la del Módulo 5: el objetivo límite $\zeta$ cae
fuera del soporte $S$ en cuanto tiene un cero.

**Conclusión de (iii):** la recurrencia fuerte no es demostrable sin RH por la maquinaria
existente, y la frontera de lo demostrable está cartografiada con precisión inusual: toda
la familia $(\mathrm{SR}_d)_{d\neq0}$ es incondicional; el único punto que falta es el
diagonal, y es equivalente a RH. El input aritmético real llega literalmente hasta la
frontera del problema.

---

## 7. Las palancas ergódicas y la identificación de la obstrucción (pregunta iv — contenido principal)

### 7.1 Lo que la dinámica da gratis (incondicional)

Fijamos el sistema $(\Omega,m_H,(T_\tau))$ del §3. Hechos clásicos, todos incondicionales:

**(E1) Ergodicidad** del flujo de Kronecker (Módulo 2; factorización única).

**(E2) Minimalidad y unicidad ergódica.** La órbita del elemento neutro,
$\{(p^{-i\tau})_p:\tau\in\mathbb{R}\}$, es densa en $\Omega$: en cada subtoro finito
$\prod_{p\le X}\mathbb{T}_p$ esto es Kronecker–Weyl (independencia de $\{\log p\}_{p\le X}$),
y $\Omega$ es el límite inverso. Una traslación de grupo compacto con un subgrupo
uniparamétrico denso es **minimal** y **únicamente ergódica** (teorema clásico de
rotaciones de grupos compactos; Walters, *An Introduction to Ergodic Theory*, cap. 6).
En particular:

**(E3) TODO punto de $\Omega$ es uniformemente recurrente.** En un sistema minimal sobre
compacto, cada punto es casi-periódico en el sentido de Birkhoff: para todo entorno $U$
de $\omega$, el conjunto $\{\tau:T_\tau\omega\in U\}$ es relativamente denso (sindético),
en particular de densidad inferior positiva. **Esto incluye al punto aritmético**
$\omega_0=(1,1,1,\dots)$ (todas las fases triviales — el punto que corresponde a $\zeta$
misma).

Subráyese: la recurrencia de la órbita aritmética **en el toro** no es el problema. Es un
hecho incondicional y cuantitativo (es la casi-periodicidad de Kronecker–Weyl, el
Mecanismo 9 de Phase 25 en su forma correcta). Si la obstrucción de Bagchi fuera "órbita
individual vs. genérica" en el sentido del teorema ergódico puntual — convergencia c.s.
sin control en puntos específicos por falta de unicidad ergódica — entonces (E2) la
resolvería: hay unicidad ergódica, y para **observables continuas** la convergencia de
promedios y las propiedades de retorno valen en TODOS los puntos, no solo c.s. La
obstrucción tiene que estar en otra parte. Está en la observable.

### 7.2 La observable de Euler y su singularidad aritmética

La conexión entre la dinámica abstracta y $\zeta$ es la **observable de Euler**
$$\Phi:\Omega\ \dashrightarrow\ H(D(1/2,1)),\qquad \Phi(\omega)=\zeta(\cdot,\omega)=\prod_p(1-\omega(p)\,p^{-\cdot})^{-1},$$
definida solo donde el producto converge. Propiedades:

- $\Phi$ está definida en un conjunto $\Omega_{\mathrm{conv}}$ con $m_H(\Omega_{\mathrm{conv}})=1$
  (Módulo 3), invariante bajo el flujo.
- $\Phi$ **no admite versión continua** en $\Omega$: es un límite c.s./$L^2$ de funciones
  continuas (los productos parciales), no un límite uniforme; sobre la franja la serie
  $\sum_p\omega(p)p^{-s}$ no converge absolutamente y su convergencia depende de
  cancelaciones de fases específicas de $\omega$.
- Sobre la órbita aritmética, $\Phi(T_\tau\omega_0)$ es formalmente el producto de Euler
  de $\zeta(s+i\tau)$ — el objeto que, según MW-2, **no converge** (no está disponible)
  en la franja.

La identificación exacta es la siguiente.

**Proposición 7.2 (la pertenencia de la órbita aritmética al dominio de la observable es
RH-equivalente).** *Son equivalentes:*
*(a) RH;*
*(b) la serie $\sum_p p^{-s}$ converge para todo $s$ con $\sigma>1/2$;*
*(c) la órbita aritmética $\{T_\tau\omega_0\}_{\tau\in\mathbb{R}}$ está contenida en
$\Omega_{\mathrm{conv}}$, y allí $\Phi(T_\tau\omega_0)=\zeta(\cdot+i\tau)$.*

*Esquema de prueba.* (a)$\Rightarrow$(b): bajo RH, $\pi(x)=\mathrm{Li}(x)+O(x^{1/2}\log x)$,
y suma parcial de Abel da convergencia de $\sum_p p^{-s}$ para $\sigma>1/2$; como
$\log\zeta(s)=\sum_p p^{-s}+E(s)$ con $E(s)=\sum_p\sum_{k\ge2}p^{-ks}/k$ absolutamente
convergente para $\sigma>1/2$, el producto converge a $\zeta(s)$ (clásico; cf. Titchmarsh,
*The Theory of the Riemann Zeta-Function*, cap. XIV). (b)$\Rightarrow$(a): si
$\sum_p p^{-s}$ converge en todo punto de $\sigma>1/2$, define allí una función holomorfa
(teoría de series de Dirichlet: convergencia en $s_0$ da convergencia local uniforme en
$\sigma>\sigma_0$ dentro de ángulos de Stolz; convergencia en todos los puntos da
holomorfía en toda la franja) que coincide con $\log\zeta-E$ en $\sigma>1$; entonces
$\log\zeta$ se continúa holomorfamente a $\sigma>1/2$, luego $\zeta$ no tiene ceros allí:
RH. (b)$\iff$(c): la convergencia del producto en $\omega=T_\tau\omega_0$ es la
convergencia de $\sum_p p^{-(s+i\tau)}$, que recorre los mismos puntos de la franja. ∎

**Corolario 7.3 (forma ergódica de MW-2).** El conjunto de divergencia
$\Omega\setminus\Omega_{\mathrm{conv}}$ es un conjunto $m_H$-nulo, invariante bajo el
flujo, y la pregunta "¿la órbita aritmética está fuera de él?" es exactamente RH. Bajo
$\neg$RH la órbita aritmética entera vive en el conjunto excepcional nulo; bajo RH vive
en el conjunto bueno. **La aritmética no puede certificarse genérica.**

### 7.3 El diagnóstico: ¿MW-2 disfrazado o una obstrucción ergódica nueva?

Ahora podemos responder la pregunta (iv) con precisión. Hay tres candidatos a "la
obstrucción" y los dos primeros se descartan:

1. **¿Falta de recurrencia del punto aritmético en el toro?** No: (E3) — $\omega_0$ es
   uniformemente recurrente, incondicionalmente.
2. **¿Falla tipo "teorema ergódico puntual sin unicidad ergódica" (órbita individual no
   controlada por la medida)?** No: (E2) — el sistema ES únicamente ergódico y minimal.
   Para observables continuas, unicidad ergódica da control en *todo* punto. La
   dicotomía "c.s. vs. punto específico" no es, por sí sola, la barrera.
3. **La observable $\Phi$ no es continua, y su dominio de definición excluye (bajo
   $\neg$RH) precisamente la órbita aritmética.** Esta es la obstrucción real, por la
   Proposición 7.2. La cadena que falla es:
   $$\underbrace{T_\tau\omega_0\ \text{vuelve cerca de}\ \omega_0}_{\text{incondicional (E3)}}\ \not\Rightarrow\ \underbrace{\Phi(T_\tau\omega_0)\ \text{vuelve cerca de}\ \Phi(\omega_0)}_{\text{= (SR) = RH}},$$
   porque trasladar la cercanía en $\Omega$ a cercanía en $H(D)$ requiere que $\Phi$ sea
   continua en $\omega_0$ a lo largo de la órbita — y la continuidad de la observable de
   Euler en el punto aritmético de la franja es, otra vez, la propagación del producto de
   Euler a $\sigma\in(1/2,1)$: **MW-2**.

**Dictamen (iv): la obstrucción es MW-2, exactamente y sin residuo.** El enunciado de
MW-2 en el resumen del programa ("el producto de Euler es válido solo para $\mathrm{Re}(s)>1$;
la información aritmética no se propaga a la franja crítica; los ceros son objetos
globales") se traduce término a término:

| MW-2 (lenguaje analítico) | Lenguaje ergódico (este doc) |
|---|---|
| el producto de Euler no converge en la franja | $\omega_0\notin\Omega_{\mathrm{conv}}$ (bajo $\neg$RH); $\Phi$ no definida/continua en la órbita aritmética |
| la aleatorización/promedios sí ven la aritmética | $m_H(\Omega_{\mathrm{conv}})=1$; teorema límite funcional incondicional (Módulo 4) |
| los ceros son objetos globales, ningún primo posee un cero | los ceros de $\zeta(\cdot,\omega)$ no existen c.s. (soporte $S$); aparecen solo en el punto excepcional global $\omega_0$, no en ninguna coordenada $p$ |
| la información de $\sigma>1$ no se propaga a la franja | la identificación $\Phi(T_\tau\omega_0)=\zeta(\cdot+i\tau)$ vale en $\sigma>1$ y su extensión a la franja es RH (Prop. 7.2) |

Y la conexión con MW-7 cierra el triángulo: *verificar* la recurrencia de la órbita
individual equivale (Rouché, §6.2) a controlar posiciones de ceros — la barrera de
Hadamard. La categoría ergódica no ofrece una formulación donde Hadamard no aplica; ofrece
la formulación más nítida que el programa posee de POR QUÉ aplica: **el teorema ergódico
(incluso con unicidad ergódica y minimalidad) controla órbitas a través de observables
continuas; la única observable que conecta el toro con $\zeta$ tiene su singularidad
exactamente en el punto aritmético, y quitarla de ahí es RH.**

### 7.4 Reformulación sintética (para el mapa del programa)

> Bajo $\neg$RH, $\zeta$ es un punto que **no pertenece al soporte de su propia
> estadística de shifts**: el teorema límite de Bagchi (incondicional) dice que la órbita
> $\{\zeta(\cdot+i\tau)\}$ equidistribuye hacia una ley $P_\zeta$ cuyo soporte son
> funciones sin ceros; si $\zeta$ tiene un cero off-crítico, $\zeta$ está fuera de ese
> soporte, y su órbita la visita con densidad nula (aunque la visita: $\tau=0$, y los
> retornos de casi-periodicidad cualitativa del Mecanismo 9). RH dice exactamente que
> $\zeta$ es un punto **genérico de su propia dinámica**. La barrera de Hadamard, en
> ergódico: *no hay forma de certificar la genericidad del punto aritmético sin conocer
> sus ceros, porque "ser genérico" ES "no tener ceros".*

---

## 8. El discriminador (pregunta v)

Aplicamos D0 con la división I2 → I2a ∧ I2b de Phase A. Objeto auditado: **el criterio de
Bagchi como ruta a RH** (= probar (SR) por la vía dinámico-ergódica y concluir por el
amplificador).

**I1 — prime-distinguishing: ✅.** Todo el aparato está indexado por primos: el toro
$\Omega=\prod_p\mathbb{T}_p$, el flujo con frecuencias $\{\log p\}$, la ergodicidad ES la
independencia lineal de $\{\log p\}$ sobre $\mathbb{Q}$ (factorización única). La
identidad de los primos (no solo sus conteos) es portadora: Baker y los seis
exponenciales (§6.3) distinguen relaciones multiplicativas finas entre primos.

**I2a — input independiente: ◐ (existe, y hace trabajo real, pero no llega al punto).**
El input no reconstruible desde $\zeta$/fórmula explícita existe: (1) independencia
lineal de $\{\log p\}$ + Kronecker–Weyl; (2) la estructura de grupo compacto de Bohr con
Haar y su unicidad ergódica; (3) teoría trascendente (Baker, seis exponenciales). Este
input produce teoremas incondicionales no triviales: la universalidad misma (Thm. 2.1),
toda la familia $(\mathrm{SR}_d)_{d\neq0}$ (§6.3), la variante $\log\zeta$ para $d\neq0$.
Pero en el punto requerido ($d=0$ / objetivo $=\zeta$), la propiedad que queda por probar
re-encodea las posiciones de los ceros (§6.2, §7.3): el input independiente se agota
exactamente en la frontera. No es el ❌ rotundo de Li/Báez-Duarte (donde no hay input
independiente en absoluto); es el ◐ de "estructura real que no alcanza", como
Berry–Keating en la tabla de Phase A.

**I2b — teorema decisivo que supla la restricción: ❌.** El teorema decisivo necesario
tiene nombre exacto: *"la órbita aritmética $\{T_\tau\omega_0\}$ es $\Phi$-recurrente"*,
equivalentemente *"$\omega_0$ es un punto genérico de la observable de Euler"*,
equivalentemente (Prop. 7.2) la convergencia de $\sum_p p^{-s}$ en la franja. No existe
tal teorema; por la Proposición 7.2 es RH-equivalente, así que ningún teorema de la
maquinaria dinámica (que controla observables continuas / clases c.s.) puede suministrarlo
sin input nuevo. Mismo perfil que Connes: la geometría/dinámica hace todo menos el último
paso, y el último paso es la re-codificación.

**I3 — individual-resolving: ✅.** Rareza notable (§4.3): el amplificador resuelve ceros
individuales — UN cero hipotético produce la contradicción; la señal es $O(1)$ (el mínimo
de $|\zeta|$ en un círculo fijo) y no un agregado/momento/densidad usado como detector.
De los ~30 programas de la tabla de Phase A, solo los PASS completos y los FAIL-I2 "de
élite" (Weil, Hilbert–Pólya, Connes, de Branges, Lee–Yang) tienen I3 ✅; ningún otro
mecanismo del corpus convierte el I3 en contradicción contra un teorema incondicional.

**I4 — arithmetic-aware: ✅.** Nada del aparato sobrevive a una deformación
aritmética-ciega: cambiar $\{\log p\}$ por frecuencias racionalmente dependientes mata la
ergodicidad (Módulo 2) y la universalidad entera. La factorización única es el motor, no
decoración.

### Fila para la tabla de Phase A

| Program | I1 | I2a | I2b | I3 | I4 | D0 verdict | Known outcome | Match? |
|---|---|---|---|---|---|---|---|---|
| **Bagchi strong recurrence / Voronin universality** | ✅ | ◐ | ❌ | ✅ | ✅ | **FAIL I2b** | criterio RH-equivalente; (SR$_d$) probado $\forall d\neq0$, abierto solo en $d=0$ | ✅ (perfil Connes: estructura real, falta el teorema decisivo) |

**Dictamen del discriminador:** FAIL I2b. No es un FAIL I2a puro (hay input independiente
genuino que produce teoremas incondicionales hasta la frontera exacta del problema), y no
es CAP (no hay positividad en ninguna parte del mecanismo). Es el segundo ejemplo limpio
del programa — tras Connes — del patrón "estructura independiente sin teorema decisivo", y
el primero de naturaleza **dinámico-ergódica**.

---

## 9. Activo trasladable (registro honesto)

Aunque la ruta se cierra, la auditoría deja un activo preciso que el programa no tenía
inventariado:

**(A1) El amplificador Rouché-densidad.** Esquema: [recurrencia con densidad positiva en
un disco alrededor de un cero hipotético] + [$N(\sigma,T)=o(T)$ incondicional]
$\Rightarrow$ contradicción. Es no-CAP, individual-resolving (I3 ✅), y su premisa mínima
es *puntual* (§4.3): bastaría producir, para cada cero hipotético $\rho_0$, densidad
positiva de auto-retornos en UN disco con UN $\varepsilon$ concreto. Cualquier mecanismo
futuro del programa que produzca recurrencia — de cualquier fuente, no necesariamente la
universalidad — enchufaría aquí y cerraría RH. El amplificador queda registrado como el
único "consumidor final" no circular conocido de propiedades de recurrencia.

**(A2) La medida exacta de la frontera.** La familia $(\mathrm{SR}_d)$: todo $d\neq0$
incondicional (Baker / seis exponenciales / racional con $|a-b|\neq1$), $d=0$
$\iff$ RH. Ningún otro frente del programa tiene la frontera de lo incondicional
cartografiada con un solo punto faltante y parametrizado.

**(A3) La forma ergódica de MW-2/MW-7 (Prop. 7.2, Cor. 7.3, tabla §7.3).** Reutilizable
como test rápido: cualquier propuesta futura de sabor dinámico (flujos en toros adélicos,
casi-períodos, compactificaciones de Bohr) debe responder primero "¿la observable que
conecta la dinámica con $\zeta$ es continua en el punto aritmético?" — si no, MW-2 aplica
y el control ergódico (aunque haya unicidad ergódica) no se transfiere.

**Gaps declarados de este documento:**
- El texto completo de Bagchi 1987 (Acta Math. Hungar. 50) no fue accesible; el enunciado
  RH $\iff$ (SR) y las referencias bibliográficas fueron verificados vía Matsumoto
  (arXiv:1407.4216, texto completo consultado) y fuentes secundarias. El marco
  dinámico-topológico interno específico del paper de 1987 (qué noción exacta de
  recurrencia de Birkhoff usa Bagchi allí) está reconstruido aquí desde el survey y debe
  considerarse [NO VERIFICADO en el original].
- La numeración interna de teoremas del libro de Steuding (*Value-distribution of
  L-functions*, Springer LNM 1877) y de Laurinčikas (1996) no fue verificada contra los
  textos; los contenidos citados (teorema de soporte, teorema límite) son estándar y
  están confirmados por Matsumoto y por la literatura de auto-aproximación.
- La Proposición 7.2 es una reorganización de hechos clásicos (Titchmarsh cap. XIV +
  teoría de series de Dirichlet); la dirección (b)$\Rightarrow$(a) requiere convergencia
  en *todos* los puntos de la franja, como está enunciado — convergencia en un solo punto
  solo da holomorfía a su derecha. No se reclama novedad, solo la identificación con el
  lenguaje ergódico.

---

## 10. VEREDICTO

**RUTA CERRADA.**

**Razón precisa:** el criterio de Bagchi tiene la estructura [premisa RH-equivalente] →
[amplificador no circular] → [RH]. El amplificador (Rouché + Carlson/Ingham) es genuino,
no-CAP e individual-resolving — pasa I1, I3, I4 — pero la premisa (recurrencia fuerte)
solo es alcanzable por la maquinaria de universalidad, que exige certificar la
no-anulación de $\zeta$ en la franja: RH misma. El discriminador da **FAIL I2b**: existe
input independiente real (independencia de $\{\log p\}$, dinámica de Bohr–Kronecker,
teoría trascendente — produce incondicionalmente toda la familia $(\mathrm{SR}_d)_{d\neq0}$),
pero el teorema decisivo faltante ("la órbita aritmética es $\Phi$-recurrente" /
"$\omega_0$ es punto genérico de la observable de Euler") es RH-equivalente
(Proposición 7.2).

**Respuesta a la pregunta (vi):** la categoría ergódica NO ofrece una formulación donde
la barrera de Hadamard deja de aplicar. La obstrucción "órbita individual vs. genérica"
**ES** MW-2 en lenguaje ergódico — y la identificación es más precisa de lo esperado:
no falla la recurrencia del punto aritmético en el toro (incondicional, por minimalidad),
ni falla la unicidad ergódica (el flujo de Kronecker la tiene); falla la **continuidad de
la observable de Euler en el punto aritmético**, y esa continuidad es literalmente "el
producto de Euler se propaga a la franja" (MW-2), cuya verificación es "conocer las
posiciones de los ceros" (MW-7). Los tres muros son la misma piedra vista desde análisis,
medida y dinámica. Lo que la categoría ergódica sí aporta es la formulación más nítida
del programa de esa piedra (Cor. 7.3: *bajo $\neg$RH la órbita aritmética entera vive en
el conjunto excepcional de medida nula de su propia dinámica*), más un activo no circular
nuevo: el amplificador Rouché-densidad (§9, A1), único consumidor final conocido de
recurrencia que produce RH sin positividad.

---

## Referencias

**Literatura externa (verificada):**
- S. M. Voronin, *Theorem on the "universality" of the Riemann zeta-function*, Izv. Akad.
  Nauk SSSR Ser. Mat. **39** (1975), 475–486; Math. USSR-Izv. **9** (1975), 443–453.
- B. Bagchi, *The statistical behaviour and universality properties of the Riemann
  zeta-function and other allied Dirichlet series*, tesis doctoral, Indian Statistical
  Institute, Calcuta, 1981.
- B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math.
  Hungar. **50** (1987), 227–240.
- K. Matsumoto, *A survey on the theory of universality for zeta and L-functions*,
  arXiv:1407.4216 (2014) — fuente principal de los enunciados (Thms. 1, 11, 20, 21;
  Cor. 2; §§1, 9, 10, 18; texto completo consultado).
- J. Steuding, *Value-distribution of L-functions*, Springer Lecture Notes in
  Mathematics 1877, 2007.
- A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996.
- F. Carlson (1920); A. E. Ingham (1940) — estimaciones de densidad de ceros,
  $N(\sigma,T)=o(T)$ para $\sigma>1/2$; precursor: H. Bohr y E. Landau (1914).
- T. Nakamura, Arch. Math. **95** (2010), 549–555; T. Nakamura y Ł. Pańkowski, Arch.
  Math. **99** (2012), 43–47 (erratum); R. Garunkštis, *Self-approximation of Dirichlet
  L-functions*, J. Number Theory (2010) — la familia $(\mathrm{SR}_d)$.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2ª ed., cap. XIV.
- P. Walters, *An Introduction to Ergodic Theory*, Springer GTM 79 — unicidad ergódica de
  rotaciones de grupos compactos.

**Docs internos del programa (backward-only):**
- `meta-docs/DISCRIMINATOR-hardening-phase-A.md` — criterios I1, I2a, I2b, I3, I4; tabla.
- `meta-docs/DISCRIMINATOR-independent-input-filter.md` — D0, H0, calibración.
- `phase-25/01-audit-classical.md` — Mecanismo 4 (Deuring–Heilbronn), Mecanismo 9
  (casi-periodicidad de Bohr).
- `COMPLETE-PROGRAM-SUMMARY.md` — MW-1…MW-7; barrera de Hadamard (Doc 89); P39, P40.
- Doc 89 (síntesis $d\nu$); P39 (RH $\iff T_\lambda=0$); P40 (tres caminos).

---

*Doc 102 · Phase 35 · junio 2026 · David Alejandro Trejo Pizzo*
