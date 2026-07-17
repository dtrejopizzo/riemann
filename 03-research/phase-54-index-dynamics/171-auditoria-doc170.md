# Documento 171 — Auditoría adversarial del Doc 170 (visibilidad de segundo orden)

**Programa:** Hipótesis de Riemann — Fase 54 (dinámica del índice)
**Fecha:** 2026-06-11
**Mandato:** destruir los teoremas del Doc 170. Protocolo: re-derivación cerrada de 170.5 (densidad de Selberg verificada contra literatura + layer-cake + ponderado), clasificación de 170.3 (trivial/fino/falso), la cuenta señal/ruido completa de la escala marginal, verificación de 170.8, diccionario con D152.
**Método:** sin numéricos; re-derivación a mano y verificación de literatura (Selberg 1946 verificado vía la literatura secundaria explícita; Ω-results de S(t) citados de memoria con confianza declarada). Fuentes leídas en original: Doc 170 completo, Doc 152 §2.2 (152.E, Teorema 152.2, prueba completa), Doc 141 (Lemas 141.M1/M4/M5, 141.B0, 141.B, Cor. 141.B2, Obs. 3.1, GAP-141.G1 en su enunciado original).

---

## 0. Veredicto por pieza

| pieza | enunciado | veredicto |
|---|---|---|
| (a) [TEOREMA 170.5] + [COR 170.6] | $E(T)\ll T/\log T$; densidad Lehmer $O(1)$; $\sum b_j^2/(\gamma_j(\log\log\gamma_j)^{1+\varepsilon})<\infty$ | **AGUANTA.** Densidad de Selberg verificada contra la literatura (forma y constante exactas); layer-cake re-derivado, constante $32C$ confirmada; ponderado re-derivado, el exponente $1+\varepsilon$ es exactamente el necesario y el reclamado. Una imprecisión menor de literatura (Jutila 1983 mejora la constante ¼ — a favor, no en contra). |
| (b) [TEOREMA 170.3] | $\int h''=0$; media en $\tau$ cero a todo orden | **(1) trivial-correcto; (2) correcto pero trivial (integral completa); el corolario en negrita sobre pesos lentamente variables es FALSO como enunciado literal** (sensibilidad pequeña, no idénticamente nula) — reparable, el mecanismo estratégico sobrevive vía la reducción a ventana única que la propia prueba usa. |
| (c) [PROP 170.2] | espectro de impureza de D152 = ventana de segundo orden | **AGUANTA.** Verificación término a término contra el Doc 152 original (test, corchete, tasa, signo, constante del sesgo): todo coincide. Los signos del propio 170 están bien. |
| (d) [TEOREMA 170.8] | no-go relativo: $I=\infty$ con datos $\varepsilon$-indistinguibles | **AGUANTA como no-go relativo**, con los mismos caveats (declarados) que 141.B2; construcción verificada (divergencia, envolvente, estadísticas verticales probadas — no solo afirmadas); un exponente de decaimiento citado con sloppiness inocua. |
| (e) escala marginal $\Theta(c^2)$ | señal orden uno; "el único bloqueo es GAP-141.G1" | **La cuenta de la SEÑAL es correcta ($\Theta(c^2)$, verificada). El cuadro señal/ruido del §3.4 (DOS bloqueos) es correcto. Pero el [DESEO] del §6 está ROTO como enunciado: identifica GAP-141.G1 con "evaluar $\mathfrak D(h_\tau)$" (solo primos+arquimediano) y lo declara ÚNICO bloqueo — eso omite $F(h_\tau)$ (el mar), que por ventana INDIVIDUAL no admite cota $o(1)$ ni incondicional ni bajo RH ($S(t)$ no acotada). Hallazgo principal de esta auditoría (H1).** |

Erratas nuevas detectadas: E-171.1, E-171.2, E-171.3 (§6 de este doc). Ningún teorema etiquetado [TEOREMA]/[PROP] del 170 muere; muere la frase estratégica final (el DESEO tal como está escrito) y una frase en negrita del 170.3.

---

## 1. [TEOREMA 170.5] — re-derivación completa

### 1.1. La densidad de Selberg: verificación de literatura

El enunciado real de Selberg 1946 (*Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48) es, tal como lo recoge la literatura que lo hace explícito (Simonič, *Explicit zero density estimate for the Riemann zeta-function near the critical line*, J. Math. Anal. Appl. 491 (2020); arXiv:1910.08274):
$$N(\sigma,T)\;\ll\;T^{1-\frac14(\sigma-\frac12)}\log T\qquad\text{uniformemente en }\tfrac12\le\sigma\le1,$$
con $N(\sigma,T)=\#\{\rho:\beta\ge\sigma,\ 0<\gamma\le T\}$ contado con multiplicidad. **Es exactamente la forma que usa el Doc 170 ($c=\tfrac14$, $B=1$), y la misma que el programa ya citaba en el Doc 141 §2.1.** El doc NO usa una forma más fuerte que la real. La uniformidad cerca de $\sigma=\tfrac12$ (donde la cota degenera suavemente a la trivial $T\log T$) es parte del teorema y es lo que el layer-cake necesita. Matiz de literatura: la observación (a) del §4 ("Selberg es lo óptimo conocido cerca de ½") es imprecisa — Jutila (1983, *Zeros of the zeta-function near the critical line*, Studies in Pure Mathematics) mejoró la constante $\tfrac14$; esto solo MEJORA la constante de 170.5 vía la forma general $(A,c,B)$, no toca el enunciado. [Errata menor E-171.3.]

### 1.2. El layer-cake, re-hecho

Identidad: para $b_j\in(0,\tfrac12)$, $b_j^2=\int_0^{1/2}2b\,\mathbf 1_{\{b<b_j\}}db$ — exacta. Y $\#\{j:b_j>b,\ \gamma_j\le T\}=N(\tfrac12+b,T)$: con un representante por cuádruplo en $\{\beta>\tfrac12,\gamma>0\}$, $N(\sigma,T)$ con $\sigma>\tfrac12$ cuenta exactamente uno por cuádruplo (el de $\beta=\tfrac12+b_j\ge\sigma$), con multiplicidad (los $j$ repetidos). La discrepancia $\ge$ vs $>$ es frontera de medida nula en $db$. **Multiplicidad y lados: consistente** — la otra mitad del cuádruplo ($\beta<\tfrac12$) no se cuenta ni en $E$ ni en $N(\sigma,T)$ con $\sigma>\tfrac12$; si se quisiera $E$ sobre todos los ceros, factor 2 absorbido en $\ll$. Entonces
$$E(T)=\int_0^{1/2}2b\,N(\tfrac12+b,T)\,db\le 2CT\log T\int_0^{1/2}b\,e^{-\frac{b}{4}\log T}db\le 2CT\log T\cdot\frac{16}{\log^2T}\int_0^\infty s e^{-s}ds=\frac{32CT}{\log T}.$$
Verificado paso a paso: $T^{1-b/4}=Te^{-(b/4)\log T}$ ✓; sustitución $s=b\log T/4$, $b\,db=(16/\log^2T)s\,ds$ ✓; $\int_0^\infty se^{-s}=1$ ✓. Constante $32C$ ✓. Separación pedida por el protocolo: en $b\le1/\log T$ el integrando es $\le 2b\cdot N(T)\sim 2b\,T\log T$, contribución $\le T\log T\cdot(1/\log T)^2=T/\log T$ ✓; en $b>1/\log T$ la cola exponencial $\int_{1/\log T}^\infty be^{-b\log T/4}db\asymp1/\log^2T$ da de nuevo $T/\log T$ ✓ — **converge a $O(T/\log T)$, no a $T\cdot$log-potencia**. La forma general: $E\le 2AT\log^BT/(c\log T)^{-2}\cdot1=(2A/c^2)T\log^{B-2}T$ ✓ tal como se enuncia. Ingham en $\sigma=\tfrac12+b$: exponente $3(\tfrac12-b)/(\tfrac32-b)=1-\tfrac{2b}{3/2-b}$, i.e. $c\approx\tfrac43$ cerca de ½, $B=5$ → $T\log^3T$ ✓ peor, como dice el doc.

**[TEOREMA 170.5] CERTIFICADO.**

### 1.3. Los corolarios, re-derivados

**170.6.1 (densidad Lehmer).** Bloques diádicos $T_k=2^k$: $\sum_{\gamma\in(T_{k-1},T_k]}(b\log\gamma)^2\le\log^2T_k\,[E(T_k)]\ll T_k\log T_k$; $\sum_{k\le K}T_k\log T_k\asymp T_K\log T_K\asymp T\log T\asymp N(T)$ ✓.

**170.6.2 (ponderado).** Sumación parcial contra $E(t)\ll t/\log t$:
$$\sum_{\gamma_j\le T}\frac{b_j^2}{\gamma_j}=\frac{E(T)}{T}+\int_2^T\frac{E(t)}{t^2}dt\ll\frac1{\log T}+\int_2^T\frac{dt}{t\log t}=\log\log T+O(1)\ ✓.$$
Con peso $u(\gamma)=(\log\log\gamma)^{1+\varepsilon}$: la integral relevante es $\int\frac{dt}{t\log t(\log\log t)^{1+\varepsilon}}$; sustituyendo $v=\log\log t$ ($dv=dt/(t\log t)$) queda $\int v^{-1-\varepsilon}dv<\infty$ **si y solo si el exponente del $\log\log$ es $>1$**. El doc reclama exactamente $1+\varepsilon$ con $\varepsilon>0$ — **el exponente es el correcto y el mínimo posible por esta vía** (con exponente 1 diverge: la advertencia del protocolo era pertinente y el doc la esquiva bien). Término de frontera $E(t)/(tu(t))\to0$ ✓. **[COR 170.6] CERTIFICADO.** (También verificada la lectura geométrica (c): $N(T)\cdot(1/\log T)^2\asymp T/\log T$ ✓; y la comparación ℓ¹: Littlewood da $\sum(\beta-\tfrac12)^+\ll T\log\log T$ [T86 §9.9], de donde solo $E\ll T\log\log T$ — la ruta de densidad es estrictamente mejor ✓.)

---

## 2. [TEOREMA 170.3] — clasificación

**(1)** $\int_{\mathbb R}h''=[h']_{-\infty}^\infty=0$ con $h'\to0$ por Cauchy en la franja + decaimiento ✓; "no existe $h\in\mathcal A$ no constante cóncava en $\mathbb R$" ✓ (cóncava no constante $\to-\infty$). **Trivial-correcto.**

**(2)** La identidad mostrada es para la **integral completa** en $\tau\in\mathbb R$: $\int h(x\pm ib)dx=\int h\,dx$ por Cauchy en el rectángulo (lados verticales $\to0$ por decaimiento uniforme, $b\le\tfrac12<\tfrac12+\varepsilon$ ✓); restar dos veces da $0$ exacto, a todo orden en $b$, resumación incluida. **Correcto — y trivial en el sentido del protocolo: es $(\int h)(1+1-2)=0$.** No hay términos de borde porque no hay truncación.

**El punto fino — donde el enunciado se pasa:** la frase en negrita *"cualquier estadística que sea una media en $\tau$ (con peso lentamente variable) de ventanas trasladadas tiene sensibilidad idénticamente nula a $I$"* es **FALSA como enunciado literal**. Para un peso $w$ no constante (p.ej. gaussiano de escala $T_0$, o truncado suavizado), la media es la evaluación del test compuesto $h\star w$ — como dice la propia prueba — y la huella de segundo orden del compuesto es $-b^2(h''\star w)(\gamma_j)\ne0$ en general: es $O(b^2/T_0^2)$-pequeña (las derivadas las pone $w$), **pequeña, no idénticamente nula**; y con truncación brusca hay además términos de borde del tamaño de los cuádruplos cercanos a los extremos. Dos defectos más del mismo párrafo: (i) $h\star w$ puede salirse de $\mathcal A$ (un $w$ truncado degrada el decaimiento de $-1-\delta$ a $-\delta$); (ii) "se reduce a una sola ventana (§3)" y "sensibilidad idénticamente nula" son afirmaciones distintas — la prueba demuestra la primera, el enunciado proclama la segunda. **Clasificación final: (1) trivial; (2) correcto-trivial para la integral completa; el corolario de pesos lentamente variables: falso como está escrito, verdadero en la forma reparada** "la media con peso de escala $T_0$ tiene sensibilidad $O(b^2/T_0^2)$ por cuádruplo, i.e. se reduce a una ventana única de resolución $1/T_0$, donde aplica §3". La conclusión estratégica (no hay acumulación lineal de señal unisigno) **sobrevive** con la forma reparada. **Reparación R-171.1 obligatoria en el texto si el 170 se propaga.**

---

## 3. La escala marginal (e) — la cuenta señal/ruido completa

### 3.1. La señal: verificada

Convención del doc: $h(r)=\int_{-L}^Lg(u)e^{iru}du$, normalizo $h(0)=\int g\asymp1$ (Fejér: $g\ge0$, $g\asymp1/L$ en el grueso de $[-L,L]$). Entonces $|h''(0)|=\int u^2g\asymp L^2$ ✓ ("$|h''|\asymp L^2h$ en el centro"). Señal por cuádruplo en el centro, sub-resolución: $|\Delta_j|\asymp b_j^2L^2=(b_jL)^2$ ✓. Con $b=c/\log\gamma$ y $L=A\log\gamma$, $A\le2-\varepsilon$ (presupuesto MV): señal $=(cA)^2=\Theta(c^2)$. **La cuenta de potencias de log es correcta: ningún log escondido en la señal.** Amplificación off $e^{bL}=e^{cA}=O(1)$ en esta escala ✓ consistente.

### 3.2. El ruido: la cuenta que el doc hace a medias

Por la identidad 170.1(iii), certificar exige acotar $F(h_\tau)=\int h_\tau\,dS$ además de $\mathfrak D(h_\tau)$. Tres niveles:

1. **Por ventana individual, incondicional:** $|F|=|\int h_\tau'(t)S(t)dt|\le\sup_{t\approx\tau}|S(t)|\cdot\mathrm{TV}(h)$. Para Fejér $\mathrm{TV}(h)=O(1)$ (picos laterales $\asymp k^{-2}$, sumables); Backlund da $|S|\le C\log\tau$. **Cota certificable por ventana: $O(\log\gamma)$ — un factor $\log\gamma$ POR ENCIMA de la señal $\Theta(c^2)$.** A nivel de certificado individual incondicional la señal SÍ está enterrada por un log.
2. **En varianza (media cuadrática sobre $\tau$), incondicional bajo $L\le(2-\varepsilon)\log\tau$:** $F$ = (suma de primos vía fórmula explícita) + liso; Montgomery–Vaughan, diagonal: $\frac1{T_0}\int_0^{T_0}|F|^2d\tau\asymp\sum_n\frac{\Lambda(n)^2}{n}g(\log n)^2\asymp\int_0^Lu\,g(u)^2du\asymp\frac1{L^2}\cdot L^2\asymp1$. **Fluctuación típica $\Theta(1)$ — la afirmación "la ventana contiene $O(1)$ ordenadas y fluctúa $\Theta(1)$" del §3.4 es correcta en este sentido L², y es incondicional** (no requiere Montgomery condicional; lo condicional es la asintótica fina/correlación de pares, no la cota superior de la varianza en este rango de soporte). El protocolo preguntaba si la varianza es $\sim\log T$: no con test suave normalizado ($g\asymp1/L$); sería $\asymp\log$ con ventana brusca de altura 1 — el doc usa la suave, la cuenta está bien.
3. **Por ventana individual, condicional:** ni bajo RH hay $o(1)$: $S(t)=\Omega_\pm\bigl((\log t/\log\log t)^{1/2}\bigr)$ (Montgomery 1977, bajo RH; incondicionalmente hay Ω-results más débiles, Tsang — [confianza alta, citado de memoria: GAP de literatura menor en el exponente incondicional exacto]). **Existen ventanas excepcionales con $|F|\to\infty$: la cota por ventana individual con error $o(1)$ NO existe en ningún mundo.**

### 3.3. Consecuencia: dónde está el error del Doc 170

- El **§3.4 y el §0.3 son correctos**: dos bloqueos, (i) lado primo por ventana (G1) y (ii) estadística cuadrática del mar a resolución. "No enterrada por tamaño" es verdad **en sentido típico/L²** (señal $\Theta(c^2)$ vs fluctuación típica $\Theta(1)$ — mismo orden, sin log de déficit), no por ventana individual (déficit $\log\gamma$ contra la única cota individual certificable, nivel 1 de arriba).
- El **[DESEO] del §6 está roto (HALLAZGO H1):** dice que *"una evaluación incondicional de $\mathfrak D(h_\tau)$ por ventana individual con error $o(1)$ — es GAP-141.G1 — es el ÚNICO bloqueo y cruzarlo daría cotas por ventana sobre $\sum_{\gamma_j\approx\tau}(b_j\log\gamma_j)^2$"*. Dos fallos:
  1. **Atribución interna imprecisa:** el GAP-141.G1 ORIGINAL (Doc 141 §3.3) pide error $o((\delta L)^2)$ de "**arquimediano + primos + mar on-line**" — incluye $F$. El 170 lo recorta a "lado primo"/"$\mathfrak D$" al citarlo. $\mathfrak D$ y G1 no son lo mismo: G1 es estrictamente más fuerte.
  2. **El enunciado del DESEO con $\mathfrak D$ solo es insuficiente:** señal $=\mathfrak D-F$; con $\mathfrak D$ evaluado a $o(1)$ queda $|F|$, que por ventana individual es $O(\log\gamma)$ incondicional y $\Omega(\sqrt{\log/\log\log})$ en ventanas excepcionales incluso bajo RH (3.2.3). **Cruzar el DESEO tal como está escrito NO daría las cotas por ventana prometidas.** Reparación honesta (R-171.2): o (a) reescribir el DESEO con el G1 original (que ya incluye el mar — pero entonces "el único bloqueo" es una tautología: G1 = todo el bloqueo por definición), o (b) degradar la promesa a **casi toda ventana** (en densidad): $\mathfrak D$ con error $o(1)$ por ventana + varianza del mar $\Theta(1)$ (nivel 3.2.2, ¡incondicional en este rango!) darían cotas sobre $\sum(b_j\log\gamma_j)^2$ para el 100% de las ventanas en densidad — que es probablemente lo que la dinámica del índice necesita. La opción (b) es además MÁS optimista que el texto actual: el bloqueo (ii) "correlación de pares condicional" sobra para cotas superiores en casi-toda-ventana, porque la cota superior de la varianza es incondicional (MV); lo condicional es solo la asintótica.
- **Detalle omitido adicional (menor):** la inferencia por ventana de una cota sobre la energía requiere control de los flancos — los cuádruplos vecinos caen en la zona $h''>0$ y contribuyen con el signo opuesto (el unisigno es solo en el núcleo, como el propio §2 explica). Para cotas superiores de la energía del núcleo esto añade un término firmado de cuádruplos a distancia $\lesssim$ unas pocas resoluciones; controlable por la envolvente 170.5 en media pero no por ventana individual. Debe aparecer en cualquier versión reparada del DESEO.

### 3.4. Verificación de los cálculos numéricos del §3 del 170

- **170.4a (silla):** $\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\approx\int_0^\infty e^{u/2-u^2/4T^2}du$: máximo en $u=T^2$, valor $T^2/4$ ✓, anchura gaussiana $\Rightarrow$ total $=2\sqrt\pi\,Te^{T^2/4}(1+o(1))$. **El 170 escribe $\sqrt\pi\,Te^{T^2/4}$: factor 2 perdido, e inconsistente con su propia fuente (D152, prueba de 152.2(c), que da $2\sqrt\pi Te^{T^2/4}$, control de consistencia incluido). Errata E-171.1, inocua** (solo el exponente ¼ es load-bearing; el umbral $\omega=\tfrac14$ y la conclusión "solo el polo" quedan intactos). La lógica $e^{b^2T^2}<e^{T^2/4}$ para todo $b<\tfrac12$ ✓.
- **170.4c (MV):** diagonal $\tfrac12\sum\Lambda(n)^2n^{-1}e^{-(\log n)^2/2T^2}\approx\int ue^{-u^2/2T^2}du\asymp T^2$ ✓. Término de error MV $\sum n|a_n|^2=\sum\Lambda(n)^2e^{-(\log n)^2/2T^2}\approx\int ue^{u-u^2/2T^2}du$: silla en $u=T^2$, valor $T^2/2$, anchura $T$ → $\asymp T^3e^{T^2/2}$, **no $T^2e^{T^2/2}$ como escribe el doc — errata E-171.2, inocua** (bajo $T^2\le(2-\varepsilon)\log T_0$ sigue siendo $\ll T^2T_0$). Exceso de un cuádruplo: $\int T^2e^{2T^2(b^2-(\tau-\gamma)^2)}\cos^2 d\tau\asymp Te^{2b^2T^2}$ ✓; el umbral: $e^{2b^2T^2}\gtrsim TT_0$ con $T^2=(2-\varepsilon)\log T_0$ da $b^2\ge\tfrac1{2(2-\varepsilon)}\to\tfrac14$ ✓. **El umbral ¼ en las tres rutas: verificado.**

---

## 4. [TEOREMA 170.8] — verificación

**Construcción:** $b_j=1/\sqrt{\log(j+2)}$: $\sum b_j^2=\sum1/\log(j+2)=\infty$ ✓ (serie de comparación con $\int dx/\log x$), $b_j\to0$ ✓.

**El mecanismo (altura, no anchura):** la cota usada es exactamente el Lema 141.B (verificado en el original, prueba por Taylor con resto + integración por partes $N$ veces): contribución del cuádruplo $j$ al dato $i$ $\le C_N(F_i)(b_jL_i)^2e^{b_jL_i}(1+\gamma_j)^{-N}$. Con $i$ fijo, $b_j\le1$: $\le C_i'(1+\gamma_j)^{-N}\to0$ **sin tocar $b_j$** ✓ — el punto estructural (en 141.B2 la indistinguibilidad se compraba con $\delta_j\to0$ rápido, incompatible con $I=\infty$; aquí con $\gamma_j\to\infty$, compatible) es correcto y es genuinamente la novedad. Sloppiness inocua: el $(1+\gamma_j)^{-2}$ del 170 presupone $F_i$ de tipo $C_c^\infty$ (donde 141.B da cualquier $N$); para $h\in\mathcal A$ general el decaimiento garantizado del $h''$ por Cauchy es $(1+\gamma)^{-1-\delta}$ — basta igual ($\to0$), la prueba no se inmuta. Versión (1): finitas condiciones por paso, presupuesto $\varepsilon2^{-j}/M$, elegir $\gamma_j$ grande ✓. Versión (2): cabeza $I_0$ + cola absorbida por la métrica ✓.

**Admisibilidad y densidad (el problema del contraejemplo del Doc 144):** un cuádruplo por paso con $\gamma_j$ súper-exponencial añade $O(\log\log T)$ ceros hasta $T$ — RvM intacta a nivel $O(1)$ por ventana; densidades: un cero por bloque $\ll$ toda cota ✓; envolvente: $E(T)=\sum_{j\le J(T)}1/\log(j+2)\ll\log J(T)\ll\log\log\log T=o(T/\log T)$ ✓ (el doc dice $o(T/\log T)$ — correcto con margen absurdo). **"Estadísticas verticales idénticas": PROBADO, no solo afirmado** — $Z$ y $Z^\flat$ comparten ordenadas como multiconjuntos por construcción, y el Lema 141.B0 (verificado en el original: $N(t)$ no refiere a $\beta$ dentro de la banda) convierte eso en identidad de todos los funcionales de ordenadas. ✓

**Alcance:** el teorema es un no-go **relativo a la clase de datos**, y el doc lo declara con la honestidad de la Obs. 3.1 del 141, incluida la restricción nueva real (la versión numerable por-dato-uniforme NO se recupera: las cabezas $j<i$ no son controlables con $b_j$ fijado por la divergencia — declarado ✓). Lo que NO cubre (y no pretende): configuraciones realizables como ceros de una función con producto de Euler (rigidez global), y la aritmética a todos los soportes (G1). **Mismos resquicios que 141.B2, correctamente listados. CERTIFICADO en su alcance declarado.**

---

## 5. Diccionario con D152 — verificación término a término

Cotejado contra el original (`phase-48-audit-and-purity/152-ataque-pureza-rigidez.md`, §2.2):

| ítem | D152 (original) | D170 | ¿coincide? |
|---|---|---|---|
| coordenada off | $t_\rho=\gamma-i\delta$, $\delta=\beta-\tfrac12\in(0,\tfrac12)$ | $\gamma_\rho=\gamma_j-ib_j$, $b_j=\beta_j-\tfrac12$ | ✓ ($b_j\equiv\delta_j$) |
| test | $h_{T,\tau}=e^{-T^2(t-\tau)^2}+e^{-T^2(t+\tau)^2}$, $g=\tfrac1{\sqrt\pi T}e^{-u^2/4T^2}\cos(\tau u)$ | $g=e^{-u^2/4T^2}\cos(\tau u)$, $h_\tau=\sqrt\pi T[\,\cdots]$ | ✓ ($h_\tau=\sqrt\pi T\,h_{T,\tau}$, re-derivada la transformada: $\widehat{e^{-u^2/4T^2}}=2\sqrt\pi Te^{-T^2r^2}$, mitades del coseno ✓) |
| corchete del cuádruplo | $\mathrm{Re}\,e^{-T^2(\gamma-\tau-i\delta)^2}=e^{T^2(\delta^2-(\gamma-\tau)^2)}\cos(2T^2(\gamma-\tau)\delta)$ (152, prueba (iii)) | $2\sqrt\pi Te^{-T^2(\gamma-\tau)^2}[e^{T^2b^2}\cos(2T^2(\gamma-\tau)b)-1]$ | ✓ (re-derivado: $(\gamma-\tau+ib)^2=(\gamma-\tau)^2-b^2+2ib(\gamma-\tau)$; idéntico) |
| tasa exponencial | $\omega(\tau)=\max(0,\max_{|\gamma_j-\tau|<\delta_j}(\delta_j^2-(\gamma_j-\tau)^2))$ [Thm 152.2(a)] | $\tfrac1{T^2}\log|\cdot|\to b_j^2-(\gamma_j-\tau)^2$ | ✓ (con el matiz de que el límite pleno requiere el lema de no-cancelación de Besicovitch de 152 — que 152 probó; el "reproduce exactamente" del 170 es legítimo apoyado en 152, no autónomo) |
| signo del sesgo | ceros entran con $-$ en (152.E); $S_T(\gamma_J)=-2\sqrt\pi m_JTe^{\delta_{\max}^2T^2}(1+o(1))$ [152.2(b)] | "los ceros entran con signo $-$: sesgo negativo permanente $\sim-2\sqrt\pi m_JTe^{\delta^2T^2}$" | ✓ signo y constante |
| señal en el centro | — | $+2\sqrt\pi b^2T^3$ (lado ceros, $\tau=\gamma_j$) | ✓ re-derivado: $2\sqrt\pi T(e^{T^2b^2}-1)\approx2\sqrt\pi b^2T^3$; y coincide con $-b^2\partial_t^2[\sqrt\pi Te^{-T^2(t-\tau)^2}]_{t=\tau}=+2\sqrt\pi b^2T^3$ — la huella $-b^2h''$ de 170.1(ii) con el signo BIEN |
| jurisdicción ¼ | $S_T(0)=2\sqrt\pi Te^{T^2/4}$, $\omega\le\tfrac14$ [152.2(c), 152.4] | umbral $\omega=\tfrac14$ en las tres rutas | ✓ (salvo el factor 2 de E-171.1, que vive solo en 170 §3.1 y no toca el exponente) |

**Signos del propio 170:** verificados de raíz. 170.1(i): el cuádruplo da $h(\gamma\pm ib)+h(-\gamma\pm ib)=2[h(\gamma+ib)+h(\gamma-ib)]$ por paridad, la proyección da $4h(\gamma)$; diferencia $=2\Delta_j$ con el factor 2 externo bien contado ✓. 170.1(ii): $f(b)=2\,\mathrm{Re}\,h(\gamma+ib)$, $f''(0)=-2h''(\gamma)$ → $\Delta_j=-b^2h''(\gamma)+R$, $|R|\le\tfrac1{12}b^4\sup|h^{(4)}|$ (Taylor a orden 4 con $f^{(4)}=2\mathrm{Re}\,h^{(4)}$: $2/24=1/12$ ✓). **La errata E-170.1 (signo del 168) está corregida correctamente en el 170; el 170 no introduce errores de signo nuevos.** [PROP 170.2] CERTIFICADA.

---

## 6. Erratas y reparaciones

- **E-171.1 (170 §3.1(α)):** la cota trivial es $2\sqrt\pi\,Te^{T^2/4}(1+o(1))$, no $\sqrt\pi\,Te^{T^2/4}$ (silla re-hecha; coincide con D152). Inocua: solo el exponente ¼ es load-bearing.
- **E-171.2 (170 §3.3):** el término de error MV es $\sum n|a_n|^2\asymp T^3e^{T^2/2}$, no $T^2e^{T^2/2}$. Inocua bajo la restricción de soporte.
- **E-171.3 (170 §4 Obs. (a)):** "Selberg es lo óptimo conocido cerca de ½" — Jutila (1983) mejoró la constante ¼; solo mejora la constante de 170.5. Cita a añadir.
- **R-171.1 (170 Teorema 170.3(2), frase en negrita):** sustituir "sensibilidad idénticamente nula" por "sensibilidad $O(b^2/T_0^2)$ por cuádruplo para peso de escala $T_0$ (reducción al test compuesto $h\star w$, ventana única de resolución $1/T_0$)"; con peso constante (integral completa) sí es cero exacto.
- **R-171.2 (170 §6 [DESEO] — la reparación obligatoria):** el DESEO tal como está escrito (evaluar $\mathfrak D$ por ventana individual = G1 = único bloqueo) es insuficiente e imprecisamente atribuido (§3.3 de este doc). Forma reparada propuesta: *"evaluación incondicional de $\mathfrak D(h_\tau)$ por ventana con error $o(1)$ (la mitad-primos de GAP-141.G1) daría, combinada con la cota de varianza MV del mar (incondicional a soporte $\le(2-\varepsilon)\log\gamma$), cotas sobre $\sum_{\gamma_j\approx\tau}(b_j\log\gamma_j)^2$ para CASI TODA ventana en densidad — no por ventana individual (imposible: $S$ no acotada en ningún mundo), y con el término firmado de flancos controlado en media por 170.5."* Nótese que la forma reparada es a la vez más débil (casi-toda-ventana) y más fuerte (no necesita correlación de pares condicional para la cota superior) que la original.

---

## 7. Mensaje final

**Veredictos:** (a) 170.5+170.6 **CERTIFICADOS** (densidad de Selberg verificada contra literatura en forma y constante; layer-cake y ponderado re-derivados sin fallo; el exponente $(\log\log)^{1+\varepsilon}$ es exactamente el mínimo correcto). (b) 170.3 **trivial-correcto** en sus dos partes; la extrapolación a pesos lentamente variables es falsa como literal, reparable sin pérdida estratégica. (c) 170.2 **CERTIFICADA** término a término contra D152 (signos del 170 limpios; la corrección E-170.1 del 168 está bien hecha). (d) 170.8 **CERTIFICADO** como no-go relativo en su alcance declarado (la novedad "divergencia comprada con altura" es real). (e) La señal $\Theta(c^2)$ es correcta; el cuadro de dos bloqueos del §3.4 es correcto; **el [DESEO] del §6 está roto y debe repararse (R-171.2)**.

**Tres hallazgos:**
1. **H1 (el único golpe estructural):** el DESEO final identifica GAP-141.G1 con "evaluar $\mathfrak D(h_\tau)$" y lo proclama único bloqueo — pero el G1 original (Doc 141 §3.3) incluye el mar on-line en su término de error, y la pieza $F(h_\tau)$ omitida no admite cota $o(1)$ por ventana individual en NINGÚN mundo ($S$ no acotada, $\Omega(\sqrt{\log/\log\log})$ bajo RH). La promesa "cruzar G1 daría cotas por ventana" es falsa por ventana individual; verdadera (y de hecho con menos hipótesis: la varianza MV es incondicional) por casi-toda-ventana.
2. **H2 (a favor del doc):** 170.5 no solo aguanta — su mecánica es robusta (la forma general $(A,c,B)\mapsto(2A/c^2)T\log^{B-2}T$ verificada significa que toda mejora futura de densidad cerca de ½ se traduce automáticamente); y el ponderado esquiva con el exponente exacto la trampa de convergencia que el protocolo señalaba.
3. **H3 (patrón de la casa):** los tres errores aritméticos encontrados (factor 2 de la silla, potencia de $T$ en el error MV, "óptimo conocido") son todos inocuos pero los dos primeros son del género (i) del patrón histórico (constantes), y E-171.1 contradice la propia fuente interna (D152) que el doc cita — síntoma de re-cálculo sin cotejo. Ninguno toca el umbral ¼ ni la envolvente $T/\log T$.

### Referencias de verificación externa
- Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 — forma exacta $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$ confirmada vía: A. Simonič, *Explicit zero density estimate for the Riemann zeta-function near the critical line*, J. Math. Anal. Appl. 491 (2020) 124303, arXiv:1910.08274 (https://arxiv.org/abs/1910.08274).
- Jutila, M. (1983), *Zeros of the zeta-function near the critical line*, en Studies in Pure Mathematics to the Memory of Paul Turán, Birkhäuser (https://link.springer.com/chapter/10.1007/978-3-0348-5438-2_33) — mejora de la constante de Selberg.
- Montgomery, H.L. (1977), *Extreme values of the Riemann zeta function*, Comment. Math. Helv. 52 — $S(t)=\Omega_\pm((\log t/\log\log t)^{1/2})$ bajo RH [citado de memoria, confianza alta; GAP de literatura menor: el Ω incondicional exacto (Tsang) no re-verificado].
- Docs internos verificados en original: 141 (§2.1, 141.M1/M4/M5, 141.B0, 141.B, 141.B2, Obs. 3.1, GAP-141.G1), 152 (§2.2 completo, 152.E, Teorema 152.2 con prueba).
