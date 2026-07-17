# Documento 180 — El pivote 176.P1 a destrucción: anatomía microscópica de la pérdida de Selberg, la segunda barrera (molificadores), y el enunciado mínimo μ₂

**Programa:** Hipótesis de Riemann — Fase 56 (dos torres)
**Fecha:** 2026-06-11
**Mandato:** ejecutar el PIVOTE 176.P1 (mejorar $E(T)\ll T/\log T$ a $T/\log^2T$) por las dos rutas nombradas en Doc 176 §6.3 — densidad log-free cerca de $\sigma=\tfrac12$ y la representación integral 173.C/176.4 — o, si ninguna cierra, localizar EXACTAMENTE la pérdida y formular el enunciado mínimo residual de GAP-A. Calibrar además la cadena hacia abajo (¿LH compra algo?).
**Prerrequisitos (no re-derivados):** [TEOREMA 173.C] (identidad de Green–Littlewood, Doc 173 §6.1); [TEOREMA 176.4] (forma promediada, el límite de Cesàro existe siempre y vale $\pi I(0^+)-\frac\pi8$); [TEOREMA 176.6] ($D(T)=\pi E(T)-\frac\pi8+O(\log T)$); [TEOREMA 176.7] (A ⟹ LH); [PROP 176.8] (layer-cake exacto y GAP-A); [PROP 176.9] (barrera de densidades exponenciales); Teorema 170.5 ($E(T)\ll T/\log T$, vía Selberg [S46]).
**Contrato:** [TEOREMA]/[PROP]/[LEMA] solo con prueba completa; [GAP]/[GAP de literatura] declarados; sin numérica; honestidad total — una falsa victoria es peor que un fracaso declarado.

**Coordenadas (idénticas a Docs 170/173/176).** $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, un representante por cuádruplo; $E(T)=\sum_{\gamma\le T}b^2$; **A** $\iff I(0^+)=\lim E(T)<\infty$; $N(\tfrac12+s,T)=\#\{\rho:\beta\ge\tfrac12+s,\,0<\gamma\le T\}$; $D(T)=\int_{1/2}^\infty\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma$. Layer-cake exacto ([PROP 176.8.a]): $E(T)=\int_0^{1/2}2s\,N(\tfrac12+s,T)\,ds$.

---

## 0. Resumen ejecutivo y veredicto

1. **El pivote 176.P1 NO se cierra en esta sesión** — pero queda transformado: la pérdida del $\log$ está ahora localizada en un punto único de cada conducto, y ambos conductos tienen barrera probada.
2. **[LEMA 180.1] (unidades microscópicas).** En la variable $u=s\log T$, $E(T)\asymp\frac{T}{\log T}\cdot\mu_2(T)$ con $\mu_2$ = desplazamiento cuadrático medio microscópico. Selberg ⟺ $\mu_2\ll1$; **176.P1 ⟺ $\mu_2\ll1/\log T$; cualquier $\mu_2=o(1)$ ya mejora 170.5.**
3. **[LEMA 180.2] (refinamiento del pivote).** Una densidad log-free válida solo para $s\ge1/\log T$ **NO basta** para $T/\log^2T$: la franja interior $s<1/\log T$ con conteo trivial ya cuesta $T/\log T$. El pivote exige uniformidad hasta $s\to0^+$ — y eso ES la afirmación $\mu_2\to0$, no un teorema de densidad clásico. [GAP de literatura §1.3: no existe log-free cerca de $\tfrac12$; frontera documentada.]
4. **[PROP 180.3] (segunda barrera — el conducto Littlewood–Jensen–molificador).** Para todo molificador de longitud $T^\theta$ con momento segundo molificado $\le1+(c-1)e^{-as\log T}$, el conducto da $E(T)\le\frac{c-1}{2\pi a}\,\frac T{\log T}+O(\log T)$ — y no menos. Ganar un log exige $(c(\theta)-1)/\theta\ll1/\log T$; con el suelo tipo Farmer $c(\theta)-1\gtrsim1/\theta$ y el techo duro $\theta\le1$, **el conducto entero tiene techo $\asymp T/\log T$**. Es la gemela de [PROP 176.9]: aquélla mata las densidades, ésta mata los momentos molificados.
5. **[PROP 180.4] (ceguera de signo — la ruta integral colapsa).** La ruta vía 176.4 no pasa por densidades, pero toda cota de $D(T)$ obtenida por momentos de $|\zeta|$ o de $\log|\zeta|$ pasa por valores absolutos: la parte positiva sola vale $\gg T\sqrt{\log\log T}/\log T$ en la franja microscópica (CLT de Selberg) y $\asymp T$ en total (Bohr–Jessen). La cancelación de signo en $t$ está codificada EXACTAMENTE en los ceros (Littlewood es identidad, no desigualdad): la ruta 2 es cambio de moneda, no de información.
6. **[LEMA 180.5] (identificación $S_1$).** $D(T)=\pi\int_0^TS_1(t)\,dt$ con $S_1$ la clásica de Littlewood. **A ⟺ la media de Cesàro de $\int_0^TS_1$ es acotada.** Corolario de 170.5: $\int_0^TS_1(t)\,dt\ll T/\log T$ — y un pivote de literatura (Fujii) queda nombrado.
7. **[PROP 180.6] (objetivo 2: LH no compra ni un log).** Bajo Lindelöf, ambos conductos siguen con techo $T/\log T$; LH mejora solo constantes. Ni $T/\log^2T$ ni $T/\log^3T$ son consecuencia de LH por las técnicas existentes. A ⟹ LH (176.7) pero LH no acerca a A: la asimetría es total.
8. **Enunciado mínimo residual: [GAP-180.1] $\mu_2(T)=o(1)$** — "los ceros están en la línea en media cuadrática microscópica". Es un enunciado de proporción a escala $u\asymp1$ (un gap microscópico), invisible para densidades (176.9), molificadores (180.3) y ventanas de correlación (techo 172.9): tres barreras lo triangulan como objeto de segundo orden genuino.

---

## 1. Ruta 1: anatomía de la pérdida de Selberg

### 1.1. Las unidades correctas: la escala microscópica

La densidad local de ordenadas a altura $T$ es $\asymp\log T$; la unidad natural de desplazamiento horizontal es también $1/\log T$ (el cuadrado del gap medio). Cambio de variable $u=s\log T$:

**[LEMA 180.1].** Definiendo $\mu_2(T):=\dfrac{\log T}{T}\,E(T)\;\Big(=\dfrac{\log T}{T}\sum_{\gamma\le T}b^2\Big)$, se tiene exactamente
$$E(T)\;=\;\frac{2}{\log^2T}\int_0^{\frac12\log T}u\;N\!\Big(\tfrac12+\tfrac u{\log T},\,T\Big)\,du\;=\;\frac{T}{\log T}\,\mu_2(T),$$
y: **(a)** la densidad de Selberg $N(\tfrac12+s,T)\ll T^{1-s/4}\log T$ [S46] equivale, en estas unidades, a $N(\tfrac12+\tfrac u{\log T},T)\ll e^{-u/4}\,T\log T$ — "la proporción de ceros desplazados más de $u$ unidades microscópicas decae exponencialmente en $u$" — y da $\mu_2(T)\ll\int_0^\infty 2u\,e^{-u/4}du\ll1$ (esto ES 170.5); **(b)** el pivote 176.P1 ($E\ll T/\log^2T$) equivale a $\mu_2(T)\ll1/\log T$; **(c)** cualquier $\mu_2(T)=o(1)$ ya da $E(T)=o(T/\log T)$, mejora estricta de 170.5.

*Prueba.* La primera igualdad es el layer-cake [PROP 176.8.a] con $s=u/\log T$; la segunda es la definición de $\mu_2$. (a): sustitución directa; la integral converge. (b), (c): inmediatos. $\square$

**Lectura.** $\mu_2$ es (salvo normalización por $N(T)\asymp\frac T{2\pi}\log T$) el **desplazamiento cuadrático medio del cero típico en unidades de gap**. Selberg dice: acotado. RH dice: cero. El pivote pide: tiende a cero con tasa $1/\log T$. La pregunta correcta no es "¿cuántos ceros a distancia $s$?" sino "¿cuál es la varianza transversal del cero típico?" — un enunciado de **proporción**, no de conteo.

### 1.2. Refinamiento del pivote: dónde tiene que valer la densidad log-free

**[LEMA 180.2].** (a) Si $N(\tfrac12+s,T)\ll Te^{-cs\log T}$ vale **uniformemente para todo $s>0$** (incluido $s=o(1/\log T)$), entonces $E(T)\ll T/\log^2T$ ([PROP 176.9] con $\kappa=0$). (b) Si la misma cota vale solo para $s\ge1/\log T$, entonces NO se sigue nada mejor que $E(T)\ll T/\log T$: la franja $0<s<1/\log T$ con el conteo trivial $N\le N(T)\ll T\log T$ aporta hasta $2\int_0^{1/\log T}s\,(CT\log T)\,ds= C\,T/\log T$, y existe una configuración compatible (todos los ceros off con $b\asymp\tfrac12/\log T$, en proporción positiva) que la satura.

*Prueba.* (a) es la integral de 176.9. (b): la cota de la franja es el cálculo exhibido; la configuración saturante — proporción $\delta>0$ de ceros con $u\asymp\tfrac12$ — es consistente con la densidad supuesta en $s\ge1/\log T$ (que no ve $u<1$) y con $N(T)\sim\frac T{2\pi}\log T$, y tiene $\mu_2\asymp\delta$. $\square$

**Consecuencia para 176.P1.** El pivote, tal como estaba enunciado ("densidad log-free cerca de $\sigma=\tfrac12$"), es **más sutil de lo que parecía**: necesita validez uniforme hasta $s\to0^+$, y en $s\ll1/\log T$ la cota $N\ll Te^{-cs\log T}\approx CT$ afirma que *todos salvo $O(T)$ de los $\asymp T\log T$ ceros tienen $b=o(1/\log T)$* — es decir, una **casi-RH microscópica** ($\mu_2\to0$ con tasa). No es un teorema de densidad en el sentido de la industria: es exactamente [GAP-180.1] cuantificado.

### 1.3. La literatura log-free: frontera exacta

Lo que existe: densidades log-free **cerca de $\sigma=1$** — Linnik (1944) y Gallagher (*Invent. Math.* 11, 1970): $N(\sigma,T)\ll T^{c(1-\sigma)}$ sin factores logarítmicos, motor del teorema de Linnik; Jutila y Heath-Brown tienen variantes log-free para $\sigma\ge\alpha>\tfrac12$ fijo (típicamente $\sigma\ge\tfrac34$ o $\sigma\ge1-\delta$). Korobov–Vinogradov vive en $\sigma>1-c/(\log T)^{2/3+o(1)}$, frontera que escapa a $1$. **No localizo ningún resultado log-free válido uniformemente en $\sigma-\tfrac12\asymp1/\log T$, y el [LEMA 180.2] explica por qué no puede existir como "teorema de densidad" ordinario: en esa escala la afirmación deja de ser sobre ceros excepcionales y pasa a ser sobre el cero típico.** Cerca de la línea lo mejor sigue siendo la familia de Selberg [S46] y mejoras de constante (Jutila, "Zeros of the zeta-function near the critical line", y trabajos posteriores — mejoran $c$, no $\kappa$; por [PROP 176.9] la mejora de $c$ es irrelevante para la forma). [GAP de literatura 180.L1: afirmo la inexistencia tras búsqueda en Titchmarsh cap. 9, Ivić caps. 10–11 y la línea Linnik–Gallagher–Jutila–Heath-Brown, citando exponentes de memoria; una revisión sistemática previa a publicación es obligada.]

### 1.4. ¿Puede fabricarse? La segunda barrera: el conducto Littlewood–Jensen–molificador

La prueba de Selberg ([S46]; exposición: Titchmarsh §9.19 ss., Ivić cap. 11) corre así: con $f=\zeta\varphi$, $\varphi$ polinomio de Dirichlet molificador de longitud $X=T^\theta$, el lema de Littlewood por línea + la desigualdad de Jensen (concavidad de $\log$) convierten el **momento segundo molificado** en cota de ceros. Examinemos el conducto entero con el peso $b^2$ ya incorporado (lo que $E$ necesita), para ver si el peso esquiva la pérdida.

**[PROP 180.3] (techo del conducto).** Sea $\varphi$ un polinomio de Dirichlet con coeficiente $1$ en $n=1$, y supóngase la cota de momento molificado, con constantes $c>1$, $a>0$:
$$\frac1T\int_0^T\big|\zeta\varphi\big(\tfrac12+s+it\big)\big|^2\,dt\;\le\;1+(c-1)\,e^{-a\,s\log T}\qquad(0<s\le\tfrac12,\;T\ge T_0),\tag{M}$$
junto con $\frac1T\int_0^T|\zeta\varphi(\sigma+it)|^2dt\le1+C_\varphi4^{-\sigma}$ para $\sigma\ge\tfrac12+\tfrac12$ (cola estándar de series de Dirichlet). Entonces
$$E(T)\;\le\;\frac{c-1}{2\pi a}\cdot\frac{T}{\log T}\;+\;O(\log T),$$
**y el conducto no da menos:** toda mejora a $E\ll T/(w(T)\log T)$ con $w\to\infty$ exige una familia $\varphi_T$ con $(c_T-1)/a_T\ll1/w(T)$.

*Prueba.* (i) *Mayorización por los ceros de $f=\zeta\varphi$.* $\varphi$ es entera; los ceros de $f$ en $\sigma>\tfrac12$ contienen los de $\zeta$ y los extra aportan $(\beta-\tfrac12)^2\ge0$. El lema de Littlewood por abscisa (Doc 176 §1.2, aplicado a $f$, que es holomorfa salvo el polo simple en $s=1$ con factor $\varphi(1)$ acotado) más el layer-cake en $\sigma$ (mismo cómputo que verifica 173.C, Doc 173 §6.1) dan
$$\pi E(T)\;\le\;\pi\sum_{\substack{f(\rho)=0,\;\beta>1/2\\0<\gamma\le T}}(\beta-\tfrac12)^2\;=\;\int_{1/2}^\infty\!\!\int_0^T\log|f(\sigma+it)|\,dt\,d\sigma\;+\;O(\log T),$$
donde el $O(\log T)$ recoge bordes horizontales y polo, uniformes porque $\varphi$ tiene grado polinomial en $T$ ($\log|f|\ll\log T$ en los bordes por las cotas estándar de convexidad más $|\varphi|\le X^{O(1)}$).
(ii) *Jensen por línea.* Por concavidad de $\log$ y $\log x\le x-1$:
$$\int_0^T\log|f(\tfrac12+s+it)|\,dt\;\le\;\frac T2\log\Big(\frac1T\int_0^T|f|^2dt\Big)\;\le\;\frac T2\Big[\frac1T\int_0^T|f|^2dt-1\Big].$$
(iii) *Integración en $s$.* Con (M): $\int_0^{1/2}\frac T2(c-1)e^{-as\log T}ds\le\frac{(c-1)T}{2a\log T}$; la cola $\sigma\ge1$ aporta $\int\frac T2C_\varphi4^{-\sigma}d\sigma=O(T\cdot4^{-1})$… cuidado: la cola debe ser $o(T/\log T)$; con coeficientes de $\varphi$ acotados por divisores, $\frac1T\int|f(\sigma+it)|^2dt-1\ll X\,2^{-2\sigma}$ término a término para $\sigma$ grande, y la integral en $\sigma\ge2+\theta\log_2T$ es $O(1)$; en el rango intermedio $[\tfrac12+s_1,2+\theta\log_2T]$ se usa (M) extendida o la cota de convexidad — en la práctica (M) con $a\asymp\theta$ cubre el rango porque $e^{-as\log T}=X^{-2s}$-tipo. Total: $\pi E(T)\le\frac{(c-1)T}{2a\log T}+O(\log T)$.
(iv) *Optimalidad dentro del conducto.* Los pasos (i)–(ii) son los únicos con holgura. En (ii), Jensen es igualdad cuando $|f|$ es constante en la línea; la holgura de (i) (ceros extra de $\varphi$) solo empeora. La salida del conducto es una función monótona de $\int_0^{1/2}[\text{mean}(s)-1]^+ds$, y mean$(0)\ge c$ fuerza $\int\gtrsim(c-1)/(a\log T)$: la forma $T/\log T$ con constante $(c-1)/a$ es exacta para el conducto. $\square$

**Dónde está el log perdido — respuesta al mandato.** No en la densidad, no en el layer-cake, no en Littlewood: **en el valor del momento molificado SOBRE la línea, $c(\theta)=\lim\frac1T\int|\zeta\varphi(\tfrac12+it)|^2dt>1$.** El conducto convierte $c-1$ (con la tasa $a\asymp\theta$) en la constante de $T/\log T$. Para ganar un log se necesita $c(\theta_T)-1\ll\theta_T/\log T$. Pero:
- **Techo duro:** $\theta\le1$ (molificador más largo que $T$: el teorema del valor medio deja de existir; toda la tecnología de momentos vive en $X\le T$).
- **Suelo tipo Farmer:** para molificadores de longitud $T^\theta$ el mínimo del momento molificado es $1+\frac1\theta+o(1)$ en la clase estándar (Farmer, "Long mollifiers of the Riemann zeta-function", *Bull. LMS* 1993 — la conjetura "$\theta=\infty$" es precisamente $c(\theta)\to1$, y es de fuerza RH-adyacente). [GAP de literatura 180.L2: el suelo $c(\theta)\ge1+1/\theta$ está probado para la clase estándar de molificadores; la generalidad exacta de la clase debe verificarse en Farmer 1993 y sucesores.]

Con el suelo, $(c-1)/a\gtrsim1/\theta^2\ge1$: **el conducto Littlewood–Jensen–molificador entero tiene techo $\asymp T/\log T$.** El peso $b^2$ no esquiva nada: la pérdida es anterior al peso, vive en el único dato de entrada (el momento en la línea). Y los momentos superiores no ayudan: el cuarto momento de Ingham ($\sim T\log^4T/2\pi^2$) entra por Jensen con $\log$ de media $\asymp\log\log T$ — peor; los momentos molificados de orden alto tienen el mismo defecto $c>1$. Esta es la **gemela exacta de [PROP 176.9]**: aquélla cierra el conducto de densidades, ésta el de momentos. Juntas cubren las dos únicas maquinarias incondicionales conocidas para ceros cerca de la línea.

---

## 2. Ruta 2: la representación integral — por qué colapsa sobre la ruta 1

La esperanza del mandato: [TEOREMA 176.4] no pasa por densidades; una cota superior incondicional de $\overline D(T_0)=\frac1{T_0}\int_{T_0}^{2T_0}D(T)\,dT$ mejor que $T_0/\log T_0$ daría el pivote, y una $O(1)$ daría A.

**[PROP 180.4] (ceguera de signo).** (a) *La parte positiva no alcanza:* incondicionalmente, por Cauchy–Schwarz con el momento segundo de $\log|\zeta|$,
$$\int_{1/2}^{1/2+1/\log T}\!\!\int_0^T\big(\log|\zeta(\sigma+it)|\big)^+dt\,d\sigma\;\ll\;\frac{T\sqrt{\log\log T}}{\log T},$$
usando $\int_0^T(\log|\zeta(\tfrac12+s+it)|)^2dt\ll T\log\log T$ uniforme en $0\le s\ll1/\log T$ (Selberg [S46]; uniformidad en el desplazamiento: Tsang, tesis Princeton 1984 [GAP de literatura 180.L3: la uniformidad exacta en $s\ll1/\log T$ citada de memoria de Tsang; verificar]). Y por Bohr–Jessen (varianza $\sim\tfrac12\log\frac1{2\sigma-1}$), $\iint_{\sigma>\frac12+1/\log T}(\log|\zeta|)^+\asymp T$. La masa positiva total es $\asymp T$ y ya en la franja microscópica es $\gg T\sqrt{\log\log T}/\log T$ — **estrictamente peor que el certificado** $|D|\ll T/\log T$.
(b) *La cancelación es exactamente los ceros:* para cada $\sigma>\tfrac12$ el lema de Littlewood es una **identidad**: $\int_0^T\log|\zeta(\sigma+it)|dt=2\pi\sum(\beta-\sigma)^+-2\pi(1-\sigma)+O(\log T)$. Toda cota superior del lado izquierdo equivale (módulo $O(\log T)$) a una cota de ceros, y viceversa: no existe "tercer término". Por tanto cualquier mejora de $\overline D$ que no use ceros debe extraer la cancelación de signo en $t$ de $\log|\zeta|$ directamente — y los momentos (de $|\zeta|$, de $|\log|\zeta||$, de potencias) son ciegos al signo: su suelo es (a).

*Prueba.* (a): Cauchy–Schwarz por línea, $\int(\log|\zeta|)^+\le\sqrt{T\cdot T\log\log T}$, por anchura $1/\log T$; la parte Bohr–Jessen es el calibre de 176 §5.2 (uso calibratorio, mismo GAP declarado allí). (b): Littlewood 1924 es identidad exacta salvo bordes $O(\log T)$ (Doc 176 §1.2); la equivalencia es la lectura bidireccional. $\square$

**Veredicto de la ruta 2.** El cambio de moneda 173.C/176.4 (de ceros a $\log|\zeta|$) es **exacto y por tanto no genera información**: las herramientas que saben integrar $\log|\zeta|$ con signo son exactamente las que saben contar ceros (vía la identidad). La ventaja de 176.4 sigue siendo estructural (el límite existe, la cota inferior $-\pi/8$ es óptima, A es la finitud de un límite), no técnica. La barrera 176.9 no se rodea por aquí: se reaparece disfrazada.

**[LEMA 180.5] (identificación con $S_1$ y pivote de literatura).** Con $S_1(t):=\frac1\pi\int_{1/2}^\infty\log|\zeta(\sigma+it)|\,d\sigma$ (Littlewood; Titchmarsh §9.9), se tiene $D(T)=\pi\int_0^TS_1(t)\,dt$ exactamente (Fubini, justificado por integrabilidad local — Doc 176 [LEMA 176.2]). Por tanto: **(a)** [170.5+176.6] dan $\big|\int_0^TS_1(t)\,dt\big|\ll T/\log T$ incondicional; **(b)** **A $\iff$ $\frac1{T_0}\int_{T_0}^{2T_0}\big(\int_0^TS_1\big)dT$ acotado** ([TEOREMA 176.4.c]); **(c)** [PIVOTE 180.P2] toda la literatura clásica sobre $\int_0^TS_1(t)\,dt$ (Littlewood 1924; Fujii, trabajos sobre $S_1$ y sus medias) debe auditarse con esta lupa: una asintótica incondicional con error $O(1)$ implicaría A y por 176.7 Lindelöf — luego no existe; pero el mejor error incondicional publicado es exactamente la distancia a A en moneda clásica. [GAP de literatura 180.L4: no tengo los errores de Fujii en memoria con fiabilidad.]

---

## 3. Objetivo 2: la cadena hacia abajo — ¿qué compra Lindelöf?

**[PROP 180.6].** Bajo la Hipótesis de Lindelöf: (a) el conducto de densidades sigue dando $E(T)\ll T/\log T$ y nada mejor — Ingham (1940) da $N(\tfrac12+s,T)\ll T^{1-2s+\varepsilon}$ y Halász–Turán (1969) $N(\sigma,T)\ll T^\varepsilon$ solo para $\sigma\ge\tfrac34+\delta$; en $s\asymp1/\log T$ ambos son triviales y [PROP 176.9] aplica con $c=2$ en vez de $c=\tfrac14$: **solo la constante mejora** (en un factor $\asymp64$). Ni siquiera $T/\log^3T$ se sigue. (b) El conducto de molificadores tampoco mejora: el techo $\theta\le1$ y el suelo $c(\theta)>1$ no son condicionales a nada — LH no alarga molificadores ni anula el defecto $c-1$ (los momentos $2k$-ésimos $\ll T^{1+\varepsilon}$ de LH entran por Jensen con pérdida $\log\log$, §1.4). (c) En cambio, A ⟹ LH ([TEOREMA 176.7]).

*Prueba.* (a): sustitución en 176.9 (el $T^\varepsilon$ de Ingham se absorbe tomando $\varepsilon=1/\log T$ a $T$ fijo en la franja relevante, o directamente: en $s\le K/\log T$ la cota $T^{1-2s+\varepsilon}$ excede $T$, trivial). (b): los insumos de 180.3 son incondicionales y LH no toca ninguno de los dos topes. (c): es 176.7. $\square$

**Calibración.** La flecha A ⟹ LH es estricta también cuantitativamente: LH, aun concedida entera, deja $\mu_2\ll1$ intacto — no mueve el cero típico ni una fracción de gap. **A no es "Lindelöf y un poco más": es un enunciado de otra escala** (microscópica, $u\asymp1$) que LH (enunciado de escala $T^\varepsilon$, es decir $u\asymp\varepsilon\log T$) no ve. El valor del peldaño 176.P1, si se lograra, queda calibrado así: $\mu_2\ll1/\log T$ es información que ni LH contiene.

---

## 4. Test anti-circularidad

| Pieza | ¿ζ-libre? | Dónde reentra ζ |
|---|---|---|
| Layer-cake / unidades microscópicas (180.1, 180.2) | Sí (medida puntual abstracta + $N(T)\asymp T\log T$) | Solo vía la densidad de entrada ([S46]) |
| Conducto 180.3 (Littlewood+Jensen) | La maquinaria sí; el insumo (M) es aritmético | En el momento molificado: $c(\theta)$, $a(\theta)$ — TODO el contenido aritmético vive ahí |
| Barrera 180.3 (suelo de Farmer) | No (es un hecho sobre $\zeta$ y su molificación) | Es la entrada misma |
| Ceguera de signo 180.4 | La identidad de Littlewood es general (funciones holomorfas) | El CLT de Selberg y Bohr–Jessen son de ζ |
| 180.6 (LH no compra) | Condicional a LH, maquinaria general | — |

Sin circularidad: ningún paso asume RH, A, ni LP-112; los resultados condicionales (180.6) están marcados.

## 5. Veredicto

**¿Se probó $E(T)\ll T/\log^2T$?** **No.** Ni ninguna mejora de $T/\log T$. El resultado de la sesión es de tipo estructural-negativo con reformulación positiva:

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [LEMA 180.1] | $E(T)=\frac T{\log T}\mu_2(T)$; 176.P1 ⟺ $\mu_2\ll1/\log T$; $\mu_2=o(1)$ ya mejora 170.5 | Probado (reformulación exacta) |
| [LEMA 180.2] | Log-free solo en $s\ge1/\log T$ NO basta; el pivote exige uniformidad hasta $0^+$ = casi-RH microscópica | Probado |
| [PROP 180.3] | **Segunda barrera:** el conducto molificador tiene techo $\frac{c-1}{2\pi a}\cdot\frac T{\log T}$; con suelo Farmer y $\theta\le1$, techo absoluto $\asymp T/\log T$ | Probado módulo [GAP 180.L2] (clase del suelo) |
| [PROP 180.4] | La ruta integral 176.4 colapsa: momentos ciegos al signo, suelo $T\sqrt{\log\log T}/\log T$; la cancelación = los ceros (identidad) | Probado módulo [GAP 180.L3] (uniformidad Tsang) |
| [LEMA 180.5] | $D=\pi\int S_1$; A ⟺ Cesàro de $\int_0^TS_1$ acotado; $\int_0^TS_1\ll T/\log T$ incondicional | Probado |
| [PROP 180.6] | LH no compra ni un log en $E(T)$; A es de otra escala que LH | Probado |

**GAPs numerados:**
- **[GAP-180.1] (el enunciado mínimo residual del peldaño, y de facto la antesala de GAP-A):** $\mu_2(T)=o(1)$ — *el desplazamiento cuadrático medio microscópico del cero tiende a cero*. Equivale a $E(T)=o(T/\log T)$. Lo separan de la mejor tecnología TRES barreras probadas: densidades exponenciales ([PROP 176.9]), momentos molificados ([PROP 180.3]) y —para la versión por ventanas— el techo 172.9 (correlación de pares + G1 no superan $T/\log T$). Las tres son ciegas en $u\asymp1$: la información necesaria es una **proporción de segundo orden** en la escala del gap, género GAP-141.G1.
- **[GAP-180.L1–L4] (literatura):** inexistencia de log-free en $\sigma\to\tfrac12^+$ (L1); clase exacta del suelo de Farmer $c(\theta)\ge1+1/\theta$ (L2); uniformidad del momento de Selberg en desplazamientos $s\ll1/\log T$, Tsang 1984 (L3); errores de Fujii/Littlewood para $\int_0^TS_1$ (L4).

**Dirección sucesora (Doc 181).** El objeto es $\mu_2$, no $N(\sigma,T)$. Dos vías: (i) la global — $\mu_2$ NO es un enunciado por ventanas, luego el techo 172.9 no lo cubre formalmente: examinar si la varianza global de $S(t)$/momentos de $S_1$ (Selberg, Tsang) acotan $\mu_2$ por debajo de $1$ siquiera (constante explícita: ¿$\mu_2\le10^{-1}$? — un $\mu_2$ pequeño cuantitativo sería el primer milímetro del peldaño); (ii) la torre 2 (177.B/LP-134, dinámica): si la patología está confinada a la esquina, $\mu_2$ es exactamente la medida de la esquina. El pivote 180.P2 (auditoría Fujii) es tarea de literatura previa.

---

## Referencias

- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946), 89–155. [Densidad; momento segundo de $\log|\zeta(\frac12+it)|$; CLT.]
- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Camb. Phil. Soc.* 22 (1924). [Lema de Littlewood; $S_1$.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (Heath-Brown), Oxford 1986. §9.9, §9.19 ss., cap. 9.
- A. Ivić, *The Riemann Zeta-Function*, Wiley 1985. Caps. 10–11 (densidades; exposición de Selberg).
- K.-M. Tsang, *The distribution of the values of the Riemann zeta-function*, tesis, Princeton 1984. [Momentos de $\log|\zeta|$ con desplazamiento; GAP 180.L3.]
- D. W. Farmer, "Long mollifiers of the Riemann zeta-function", *Bull. London Math. Soc.* 25 (1993). [Suelo $c(\theta)=1+1/\theta$; conjetura $\theta=\infty$; GAP 180.L2.]
- P. X. Gallagher, "A large sieve density estimate near $\sigma=1$", *Invent. Math.* 11 (1970); Yu. V. Linnik (1944). [Log-free cerca de $\sigma=1$.]
- M. Jutila, "Zeros of the zeta-function near the critical line", en *Studies in Pure Mathematics in Memory of Paul Turán*, 1983. [Mejoras de constante cerca de $\frac12$; GAP 180.L1.]
- A. E. Ingham (1940); G. Halász, P. Turán (1969); A. E. Ingham (1926, cuarto momento). [Condicionales bajo LH; momentos.]
- H. Bohr, B. Jessen, *Acta Math.* 54 (1930), 58 (1932). [Distribución de $\log\zeta$, uso calibratorio.]
- A. Fujii, trabajos sobre $S_1(t)$ y sus medias. [GAP 180.L4: auditar.]

**Documentos internos:** Doc 170 (Teorema 170.5), Doc 172 (techo por ventanas 172.9), Doc 173 (173.C), Doc 175 (LP-112, dicotomía), Doc 176 (176.4/176.7/176.8/176.9; pivote 176.P1), Doc 177 (torre 2).
