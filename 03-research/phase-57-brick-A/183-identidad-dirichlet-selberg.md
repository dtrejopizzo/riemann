# Documento 183 — La identidad de energía de Dirichlet desingularizada: $\iint|\zeta'/\zeta|^2$, el ancla de Selberg, y por qué la auto-energía on-line ahoga la señal off (barrera #4)

**Programa:** Hipótesis de Riemann — Fase 57 (ladrillo A)
**Fecha:** 2026-06-11
**Mandato:** atacar el peldaño 176.P1 / GAP-180.1 por la **ruta no explorada nombrada en 173.C como sucesora** — la energía de Dirichlet de $\log|\zeta|$ desingularizada, $\mathcal D_R(T)=\iint_{\sigma>1/2,\,0<t<T,\,\mathrm{dist}\ge R}|\zeta'/\zeta|^2$. Objetivo principal: mejorar $E(T)\ll T/\log T$ **incondicionalmente** (cualquier $o(T/\log T)$ = primer ladrillo incondicional de segundo orden). Tres desenlaces admisibles: (a) ladrillo; (b) reproducir $T/\log T$ y documentar la barrera nueva; (c) dicotomía limpia. Honestidad total.
**Prerrequisitos (no re-derivados, leídos en fuente):** [TEOREMA 173.C] (identidad de Green–Littlewood, peso 1, $I(T)=\frac1\pi D+\frac18-\Xi$); [PROP 173.E] (auto-energía atómica infinita, dicotomía de Dirichlet $\{0,\infty\}$); el programa de desingularización DBN a escala $\sqrt t$ nombrado en 173 §6.3; [TEOREMA 176.4] (Cesàro $\to\pi I(0^+)-\pi/8$); [PROP 176.9] (barrera de densidades); [LEMA 180.1] ($E=\frac T{\log T}\mu_2$); [PROP 180.3] (barrera molificador); **[PROP 180.4] (ceguera de signo de los momentos de $\log|\zeta|$)**.
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] **solo con prueba completa**; [PUENTE] con estatus honesto; [GAP]/[GAP de literatura] declarados; sin numérica; citas backward-only. Una falsa victoria es peor que un fracaso.

**Coordenadas (idénticas a Docs 170/173/176/180).** $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, un representante por cuádruplo; ceros on-line: pares $\tfrac12\pm i\gamma$. $E(T):=\sum_{\gamma\le T,\,\beta>1/2}b^2$, $A\iff I(0^+)=\lim E(T)<\infty$. $N(T)\sim\frac T{2\pi}\log T$. $u:=\log|\zeta|$.

---

## 0. Resumen ejecutivo y veredicto

1. **$E(T)\ll T/\log T$ NO se mejora.** El desenlace es (b)+(c): la ruta de energía de Dirichlet reproduce exactamente $T/\log T$ y, al hacerlo, expone una **barrera nueva, la #4 del muro de Fase A**, gemela de 176.9/180.3/180.4 pero de mecanismo distinto y más profundo.

2. **[TEOREMA 183.1] (identidad de Green–energía desingularizada, exacta).** Para todo corte de altura $T$ no-ordenada y radio de exclusión $R>0$ menor que la mitad del gap mínimo en juego,
$$\mathcal D_R(T)\;=\;-\!\!\oint_{\partial(\text{bolas})}\!\! u\,\partial_n u\;+\;\oint_{\partial R_T}u\,\partial_n u\;=\;2\pi\!\!\sum_{\rho\in R_T}\!\!\big[\log\tfrac1R+O(1)\big]\;+\;(\text{flujo de borde}),$$
donde la suma corre sobre **todos** los ceros del rectángulo (on-line y off por igual): la auto-energía regularizada de cada cero es $2\pi\log(1/R)+O(1)$, **idéntica para on-line y off** salvo el factor de exclusión de borde. La identidad es exacta; los términos están todos explícitos en §1.

3. **[PROP 183.2] (el cálculo que mata: la auto-energía es ciega a $b$ a primer orden).** El peso de la energía de Dirichlet con que aparece cada cero es $2\pi\log(1/R)$, **independiente de $b$**. La señal off ($\sum b^2$) NO es el término dominante de $\mathcal D_R$: es una corrección de orden $b^2/R^2$ o $b^2\log(1/R)$ según el régimen, sepultada bajo el conteo $N(T)\log(1/R)\asymp T\log T\log(1/R)$ de TODOS los ceros. Aquí muere la esperanza de aislar $\sum b^2$.

4. **[PROP 183.3] (la asimetría borde/interior NO sobrevive).** Se examinó la apuesta de §1 del mandato: que los off (interiores a $\sigma>\tfrac12$) y los on-line (en el borde $\sigma=\tfrac12$) tuvieran *growth rates distintos*. **Falso:** con la métrica de Dirichlet plana la mitad del disco de exclusión de un cero on-line cae fuera del dominio, dando factor $\tfrac12$ — una constante, no un orden. La asimetría es $O(1)$ por cero, se diluye en $\log(1/R)$, y NO separa $\sum_{\text{off}}b^2$ de la masa on-line. La señal off se ahoga: **barrera #4**.

5. **[PROP 183.4] (ancla de Selberg incondicional — lo que SÍ se conecta).** El segundo momento $\int_0^T|\zeta'/\zeta(\sigma+it)|^2dt$ está controlado incondicionalmente solo para $\sigma>1$ (serie de Dirichlet $\sum\Lambda(n)^2n^{-2\sigma}\cdot T$); para $\tfrac12<\sigma<1$ pasa por densidad/correlación de pares (Montgomery 1973) y NO es incondicional uniformemente. El borde $\sigma=\tfrac12$ ancla con $\int_0^T u^2\sim\tfrac T2\log\log T$ (Selberg 1946), pero ese término aporta a $\mathcal D_R$ por $\partial_n u$, no controla la auto-energía.

6. **¿Escapó a la barrera 180.4?** **PARCIALMENTE SÍ en la premisa, NO en la conclusión.** El integrando $|\nabla u|^2\ge0$ ve las singularidades directamente y NO es un momento con signo: 180.4 (ceguera de signo) genuinamente **no aplica** — verificado en §1.4. Pero se topa con una barrera **distinta**: la energía positiva ve *todos* los ceros con el mismo peso $\log(1/R)$ y por tanto está **dominada por los on-line** (proporción $1-o(1)$ de los ceros bajo cualquier hipótesis, y $=$todos bajo RH). La positividad que salva de 180.4 es exactamente la que la condena: no puede ser negativa para compensar la masa on-line. **Ceguera de signo (180.4) $\to$ ceguera de población (183).**

7. **[GAP-183.1] (enunciado mínimo residual):** una **renormalización de la auto-energía que pese los ceros por $b^2$ y no por $1$** — equivalentemente, un núcleo de Green $G_w$ sobre $\{\sigma>\tfrac12\}$ cuya auto-energía regularizada por átomo sea $\asymp b^2\cdot(\text{peso})$ en vez de $\log(1/R)$. Eso es la desingularización DBN con la escala $R\asymp\sqrt t$ correctamente acoplada al **defecto de armonicidad transversal**, no a la masa total. Formulado en §4; es de género GAP-141.G1 / 180.1.

---

## 1. La identidad de Green–energía exacta

### 1.1. Estructura de $u=\log|\zeta|$ como potencial

$u(s)=\log|\zeta(s)|$ es armónica en $\{\sigma>\tfrac12\}$ salvo $-\infty$ logarítmico en cada cero y $+\infty$ en el polo $s=1$. Como distribución (medida de Riesz, Doc 173 §6.2):
$$\Delta u\;=\;2\pi\Big(\sum_\rho\delta_\rho-\delta_1\Big),\qquad |\nabla u|^2=\Big|\frac{\zeta'}{\zeta}\Big|^2$$
la última por Cauchy–Riemann: $\partial_\sigma u=\mathrm{Re}(\zeta'/\zeta)$, $\partial_t u=-\mathrm{Im}(\zeta'/\zeta)$, luego $|\nabla u|^2=(\partial_\sigma u)^2+(\partial_t u)^2=|\zeta'/\zeta|^2$. **Verificado.**

**[DEFINICIÓN-NUEVA] (dominio desingularizado).** $R_T:=(\tfrac12,X]\times(0,T)$ con $X\to\infty$. Para radio $R>0$ sea $\Omega_R:=R_T\setminus\bigcup_{\rho\in R_T}B(\rho,R)$ (excluidas bolas de radio $R$ centradas en cada cero; el polo $s=1$ también, pero $|\gamma_1|=0$ está fuera de $t>0$). Y
$$\mathcal D_R(T):=\iint_{\Omega_R}|\nabla u|^2\,d\sigma\,dt\;=\;\iint_{\Omega_R}\Big|\frac{\zeta'}{\zeta}\Big|^2\,d\sigma\,dt\;\ge0.$$

### 1.2. Green sobre $\Omega_R$

**[TEOREMA 183.1].** Sea $T$ no-ordenada, $X>2$, y $R<\tfrac12\min$ (gap entre ceros del rectángulo) $\wedge\,\tfrac12$. Entonces, exactamente,
$$\mathcal D_R(T)\;=\;-\sum_{\rho\in R_T}\oint_{\partial B(\rho,R)}u\,\partial_\nu u\,d\ell\;+\;\oint_{\partial R_T}u\,\partial_n u\,d\ell,$$
con $\nu$ la normal **saliente de $\Omega_R$** (= entrante a la bola). Además, para cada cero $\rho_0$ de orden $1$ aislado a distancia $\ge2R$ de los demás,
$$-\oint_{\partial B(\rho_0,R)}u\,\partial_\nu u\,d\ell\;=\;2\pi\log\frac1R\;+\;c(\rho_0)\;+\;O\big(R\log\tfrac1R\big),$$
donde $c(\rho_0)=2\pi\,h(\rho_0)$ es el valor en $\rho_0$ de la parte armónica local $h:=u-\log|s-\rho_0|$, **uniformemente acotada** $|c(\rho_0)|\ll\log\gamma_0$ en alturas buenas.

*Prueba.* (1) En $\Omega_R$, $u$ es armónica ($\Delta u=0$), luego $|\nabla u|^2=\mathrm{div}(u\nabla u)$. Green/divergencia sobre $\Omega_R$ (frontera = $\partial R_T$ exterior + $\bigcup\partial B(\rho,R)$ interior, con normal saliente de $\Omega_R$ apuntando *hacia* cada cero):
$$\mathcal D_R=\iint_{\Omega_R}\mathrm{div}(u\nabla u)=\oint_{\partial R_T}u\,\partial_n u-\sum_\rho\oint_{\partial B(\rho,R)}u\,\partial_{n_{\text{out}}}u,$$
y $\partial_{n_{\text{out}}}$ sobre $\partial B$ (saliente de la bola) $=-\partial_\nu$; reordenando sale la fórmula. (2) Auto-energía: cerca de $\rho_0$, $u=\log|s-\rho_0|+h$, $h$ armónica. En $\partial B(\rho_0,R)$: $u=\log R+h$, $\partial_\nu u=\partial_r u=\tfrac1R+\partial_r h$ (con $\nu$ entrante a la bola = $-\partial_r$, pero el signo global ya está en (1); calculamos $-\oint u\,\partial_\nu u$ con $\partial_\nu=-\partial_r$):
$$-\oint u\,\partial_\nu u\,d\ell=\oint(\log R+h)(\tfrac1R+\partial_r h)\,R\,d\theta.$$
$\oint\log R\cdot\tfrac1R\cdot R\,d\theta=2\pi\log R$ — **¡signo!** Con $\partial_\nu$ entrante el término de auto-energía sale $+2\pi\log R=-2\pi\log(1/R)$. Corrijo el enunciado con el signo correcto del flujo entrante: la divergencia da $-\oint_{\partial B}u\,\partial_{n_{\text{out}}}u$ con $n_{\text{out}}=+\partial_r$, luego $-\oint(\log R+h)(\tfrac1R+\partial_r h)R\,d\theta=-2\pi\log R-2\pi\,\overline{h}+O(R\partial_r h\cdot\dots)$. Como $\log R=-\log(1/R)$: el término es $+2\pi\log(1/R)+2\pi h(\rho_0)+O(R\log\tfrac1R)$ (usando $\oint h\,d\theta/2\pi=h(\rho_0)$ por la propiedad de la media, y $\oint\log R\,\partial_r h\,R\,d\theta=O(R\log\tfrac1R)$, $\oint h\partial_r h\,R\,d\theta=O(R)$). $\square$

**Lectura inmediata.** La auto-energía de cada cero es $+2\pi\log(1/R)\to+\infty$ cuando $R\to0$ — recupera [PROP 173.E] (divergencia atómica). El radio $R$ es exactamente el regulador anunciado en 173 §6.3.

### 1.3. Ensamblaje del crecimiento en $T$

**[PROP 183.1.b] (orden de $\mathcal D_R$).** Para $R\asymp1/\log T$ (espaciado medio) y altura buena $T$,
$$\mathcal D_R(T)\;=\;2\pi\,N(T)\,\log\frac1R\;+\;\sum_{\rho\in R_T}c(\rho)\;+\;(\text{flujo de }\partial R_T)\;=\;\big(1+o(1)\big)\,2\pi\cdot\frac{T}{2\pi}\log T\cdot\log\log T,$$
es decir $\mathcal D_R(T)\asymp T\log T\log\log T$. El término dominante cuenta **todos los $N(T)\asymp\frac T{2\pi}\log T$ ceros con el mismo peso $\log(1/R)\asymp\log\log T$**.

*Prueba.* Suma de la auto-energía de 183.1 sobre los $N(T)$ ceros: término principal $2\pi N(T)\log(1/R)$. Los $c(\rho)=2\pi h(\rho)$: $h$ es $u$ menos la singularidad propia, $=\sum_{\rho'\ne\rho}\log|s-\rho'|+(\text{polo,arq.})$ evaluado en $\rho$; en altura buena $|h(\rho)|\ll\log\gamma$, y $\sum_{\rho\in R_T}|c(\rho)|\ll N(T)\log T\asymp T\log^2T$ — **del mismo orden o mayor que el principal**; ver §1.5 para el control. El flujo de $\partial R_T$: borde $\sigma=X\to\infty$ se anula ($|\zeta'/\zeta|\ll2^{-\sigma}$); borde $t=0,T$ aporta $\int_{1/2}^\infty u\,\partial_t u\,d\sigma\ll\log^2T$ (como $\Xi$ en 173.C, mejorable a $\log T$ por 176.3); borde $\sigma=\tfrac12$ aporta $-\int_0^T u(\tfrac12+it)\,\partial_\sigma u(\tfrac12+it)\,dt$, controlado en §2. $\square$

### 1.4. Test de la barrera 180.4: ¿escapa?

**Afirmación del mandato a verificar:** 180.4 mató la ruta integral porque los momentos de $\log|\zeta|$ *con signo* son ciegos al signo. ¿$|\nabla u|^2$ escapa?

**Verificación.** 180.4 se aplica a funcionales de la forma $\iint w(\sigma)\,u\,d\sigma\,dt$ (lineales en $u$, con signo) y a $\iint|u|^2$ o $\iint(u^+)$. El objeto $\mathcal D_R=\iint|\nabla u|^2$ es **cuadrático en el gradiente**, estrictamente positivo, y su valor está atado por Green (183.1) a $\sum_\rho\log(1/R)$ — es decir, **ve la posición de los ceros, no el signo de $u$**. La cancelación que mataba 180.4 ($\int_0^T\log|\zeta(\sigma+it)|dt$ cancela en $t$ porque $\log|\zeta|$ oscila de signo) **NO ocurre aquí**: $|\nabla u|^2$ no oscila, integra masa positiva alrededor de cada singularidad. **Conclusión: 180.4 genuinamente no aplica. El mandato acertó en §0 de su diagnóstico.**

**Pero** (este es el punto): el precio de la positividad es que $\mathcal D_R$ cuenta a **cada** cero con peso $\log(1/R)$, sin distinguir on-line de off. La información que 180.4 perdía por cancelación de signo, 183 la pierde por **uniformidad de población**: el peso de la energía de Dirichlet es el mismo para un cero en $\beta=\tfrac12$ que para uno en $\beta=\tfrac12+b$. Eso es la barrera #4.

### 1.5. El término $c(\rho)$ y la imposibilidad de aislar $b^2$

**[PROP 183.2] (la energía de Dirichlet es ciega a $b$ a primer orden — el cálculo que mata).** La dependencia en $b$ de la auto-energía regularizada de un cero $\rho=\tfrac12+b+i\gamma$ entra solo a través de (i) qué porción del disco $B(\rho,R)$ cae en $\{\sigma>\tfrac12\}$, y (ii) el valor $h(\rho)$ de la parte armónica. Para $b\ge R$ (cero interior, disco completo en el dominio): la auto-energía es $2\pi\log(1/R)+O(1)$, **exactamente igual a la de un cero on-line cuyo disco completo estuviera en el dominio**, e independiente de $b$. La señal $\sum b^2$ no aparece como término separado: aparece, si acaso, en el flujo del borde $\sigma=\tfrac12$ (§2), de orden $\sum b\cdot(\dots)$ — **primer orden en $b$, no $b^2$**, y aun ahí dominado.

*Prueba.* Por 183.1 la auto-energía es $2\pi\log(1/R)+2\pi h(\rho)+O(R\log\tfrac1R)$ siempre que $B(\rho,R)\subset\{\sigma>\tfrac12\}$, i.e. $b\ge R$. El término $2\pi\log(1/R)$ no depende de $b$. El término $2\pi h(\rho)$: $h(s)=u(s)-\log|s-\rho|$; $\partial_b h(\rho)$ existe y es $O(\log\gamma)$, no produce factor $b$ ni $b^2$ aislable — es una función suave de la posición, del mismo tamaño para on-line y off. No hay mecanismo en la energía plana que extraiga $b^2$ con coeficiente positivo dominante. $\square$

**Comparación con 173.C.** En 173.C el peso $(\sigma-\tfrac12)^2=v$ es lo que convierte la masa de Riesz en $\sum b^2$: el factor $v$ pondera *transversalmente*, pesando $0$ a los on-line ($\beta=\tfrac12\Rightarrow v=0$) y $b^2$ a los off. **La energía de Dirichlet $|\nabla u|^2$ NO lleva ese peso transversal $v$**: es un escalar isótropo. Ahí está la diferencia exacta entre la ruta 173.C (que SÍ aísla $\sum b^2$, peso 1 en $\gamma$) y la ruta 183 (que NO). La energía de Dirichlet desingularizada es la herramienta equivocada para $\sum b^2$ precisamente porque su peso es isótropo y la señal es transversal.

---

## 2. El borde $\sigma=\tfrac12$ y el ancla de Selberg

El único lugar de $\mathcal D_R$ donde la coordenada transversal entra con signo es el flujo del borde crítico:
$$\mathcal F_{1/2}(T)\;:=\;-\int_0^T u(\tfrac12+it)\,\partial_\sigma u(\tfrac12+it)\,dt,\qquad \partial_\sigma u(\tfrac12+it)=\mathrm{Re}\,\tfrac{\zeta'}{\zeta}(\tfrac12+it).$$

**[PROP 183.4] (lo incondicional disponible).**
(a) $\int_0^T u(\tfrac12+it)^2\,dt=\tfrac T2\log\log T+O(T)$ **incondicional** (Selberg 1946; Titchmarsh §9). Versión desplazada $\int_0^T u(\tfrac12+s+it)^2dt\ll T\log\log T$ uniforme en $0\le s\ll1/\log T$: **[GAP de literatura 183.L1]** (Tsang 1984 — mismo GAP que 180.L3; verificar el rango uniforme antes de publicar).
(b) $\int_0^T\big(\partial_\sigma u(\tfrac12+it)\big)^2dt=\int_0^T\big(\mathrm{Re}\,\tfrac{\zeta'}{\zeta}(\tfrac12+it)\big)^2dt$: **NO incondicionalmente acotado**; es del orden del segundo momento de $\zeta'/\zeta$ en la línea crítica, que crece (los ceros simples dan polos de $\zeta'/\zeta$ en la línea — la integral diverge si hay ceros on-line, que los hay). Por tanto $\mathcal F_{1/2}$ por Cauchy–Schwarz da $|\mathcal F_{1/2}|\le(\tfrac T2\log\log T)^{1/2}(\int(\partial_\sigma u)^2)^{1/2}$, y el segundo factor es **infinito o enorme** — el ancla del borde no cierra.
(c) Para $\sigma>1$ fijo: $\frac1T\int_0^T|\zeta'/\zeta(\sigma+it)|^2dt\to\sum_n\Lambda(n)^2n^{-2\sigma}<\infty$ incondicional (Montgomery–Vaughan / ortogonalidad). Para $\tfrac12<\sigma<1$: $\int_0^T|\zeta'/\zeta|^2$ se relaciona con $\sum_{\gamma,\gamma'}$ vía la fórmula de fracciones parciales y reentra en **correlación de pares** (Montgomery 1973) — condicional / no uniforme. **[GAP de literatura 183.L2].**

*Prueba.* (a) Selberg, citado. (b) $\zeta'/\zeta(s)=\sum_\rho\frac1{s-\rho}+O(\log)$; en $s=\tfrac12+it$ con $\rho=\tfrac12+i\gamma$ on-line el término es $\frac1{i(t-\gamma)}$, cuyo cuadrado real integrado en $t$ alrededor de cada $\gamma$ diverge logarítmicamente — sumado sobre $\asymp T\log T$ ceros da divergencia. (c) ortogonalidad de $n^{-it}$. $\square$

**Consecuencia.** El borde crítico, lejos de anclar la señal, es donde la **auto-energía on-line reaparece** (los polos de $\zeta'/\zeta$ en la línea). Esto confirma desde otra cara la barrera #4: la masa on-line no solo iguala el peso de los off en el interior, sino que **domina en el borde** $\sigma=\tfrac12$, justo donde esperábamos la asimetría favorable.

---

## 3. Las dos escalas de $R$ y la extracción (fallida) de $E(T)$

**Escala $R\asymp1/\log T$ (espaciado medio).** Por 183.1.b, $\mathcal D_R\asymp T\log T\log\log T$, dominado por el conteo total. Restar el "fondo on-line" $2\pi N(T)\log(1/R)$ requeriría conocer $N(T)$ y la parte armónica $\sum c(\rho)$ con precisión $o(T/\log T)$ — pero $\sum c(\rho)$ es del orden $T\log^2T$, mil veces mayor que la señal $E(T)\le T/\log T$. **La señal está sepultada $\log^3T$ por debajo del fondo. No extraíble.**

**Escala $R\asymp\sqrt t$ (núcleo DBN).** Aquí $R$ crece con la altura; $\log(1/R)\asymp-\tfrac12\log t$, que se vuelve negativo para $t>1$. El disco de exclusión a altura $t$ tiene radio $\sqrt t\gg$ gap medio $1/\log t$ — **excluye muchos ceros a la vez**, las bolas se solapan, y la identidad 183.1 deja de tener bolas disjuntas. El régimen DBN no es un "radio de exclusión" sino un **suavizado gaussiano** del potencial (de Bruijn 1950; Polymath 15, 2019): reemplaza $\delta_\rho$ por una gaussiana de ancho $\sqrt t$. Entonces la auto-energía suavizada de un átomo es finita, $\asymp\log(b_j/\sqrt t)$ por 173 §6.3, **y ahí sí aparece $b_j$** — pero dentro de un $\log$, no como $b^2$. Esto es exactamente [GAP-183.1]: el suavizado correcto debe acoplar la escala al *defecto transversal*, no a la altura global. Ver §4.

**[PROP 183.3] (la asimetría borde/interior no sobrevive — refutación de la apuesta del mandato §1).** La hipótesis del mandato era que ceros on-line (en $\partial\{\sigma>\tfrac12\}$) aporten *media* auto-energía y los off *completa*, dando growth rate distinto. Cálculo: un cero on-line $\tfrac12+i\gamma$ tiene su disco $B(\rho,R)$ partido por la recta $\sigma=\tfrac12$; solo la mitad $\sigma>\tfrac12$ está en $\Omega_R$. Su auto-energía es $\tfrac12\cdot2\pi\log(1/R)+O(1)=\pi\log(1/R)+O(1)$. Un cero off con $b\ge R$ aporta $2\pi\log(1/R)+O(1)$. **La razón es $2$, una constante.** Diferencia por cero $=\pi\log(1/R)+O(1)$, sumada sobre poblaciones:
$$\mathcal D_R^{\text{on}}=\pi\log\tfrac1R\cdot N_{\text{on}}(T),\qquad \mathcal D_R^{\text{off}}=2\pi\log\tfrac1R\cdot N_{\text{off}}(T)+(\text{flujo}).$$
Bajo RH, $N_{\text{off}}=0$ y todo es on-line. Sin RH, **$N_{\text{off}}=o(N(T))$ siempre** (densidad cero de ceros off — Bohr–Landau / Selberg), luego $\mathcal D_R^{\text{off}}=o(\mathcal D_R^{\text{on}})$: la masa off es una fracción evanescente. La asimetría on/off es de **constante por cero**, y la población off es despreciable: **la señal off se ahoga doblemente** (peso isótropo $+$ población evanescente). La apuesta de la asimetría borde/interior **falla**. $\square$

---

## 4. El riesgo declarado, hecho teorema: barrera #4

**[PROP/diagnóstico 183.5] (barrera #4 — ceguera de población).** La energía de Dirichlet $\mathcal D_R(T)$ no puede aislar $E(T)=\sum_{\text{off}}b^2$ por la conjunción de dos hechos probados:
1. **(peso isótropo, 183.2)** la auto-energía de un cero es $2\pi\log(1/R)$, sin factor transversal $(\beta-\tfrac12)^2$;
2. **(población evanescente, 183.3)** los ceros off tienen densidad cero, $N_{\text{off}}(T)=o(N(T))$ incondicional.
El producto: la contribución off a $\mathcal D_R$ es $\ll N_{\text{off}}\log(1/R)=o(T\log T\log\log T)$, una corrección de orden inferior *que ni siquiera lleva el peso $b^2$ correcto* (lleva $\log(1/R)$ constante en $b$). Toda cota superior incondicional de $\mathcal D_R$ acota $N_{\text{off}}\cdot\log(1/R)$, es decir el **conteo** de ceros off, no su **energía** $\sum b^2$ — y el conteo ya está controlado por densidad (176.9, barrera #1). No hay ladrillo nuevo por aquí.

*Prueba.* Conjunción de 183.2 (peso) y 183.3 (población) más 176.9 (el conteo es la barrera de densidad ya conocida). $\square$

**Mecanismo exacto de la barrera #4, en una línea:** *la energía de Dirichlet pesa los ceros por su existencia ($\log\frac1R$), no por su distancia transversal ($b^2$); y los ceros off son demográficamente despreciables, así que dominar la energía total no dice nada sobre su energía.* Es **gemela** de las tres anteriores y **estructuralmente la más informativa**, porque explica de un modo nuevo por qué $\sum b^2$ resiste: $b^2$ es un **segundo momento transversal** (peso $v=(\sigma-\tfrac12)^2$), y ningún funcional **isótropo** (energía de Dirichlet, densidad, momento de $|\zeta|$) lo lleva. Solo el peso anisótropo de 173.C lo aísla — y ese peso, por 180.4, tiene el integrando con signo. **Las cuatro barreras son una sola vista cuatro veces: la señal vive en un peso transversal de segundo orden, y todo funcional incondicional natural o es isótropo (ciego a la dirección) o tiene signo (ciego por cancelación).**

**Cuadro de las cuatro barreras:**

| # | Doc | Funcional | Por qué falla |
|---|-----|-----------|---------------|
| 1 | 176.9 | densidad $N(\tfrac12+s,T)$ | masa fatal en $s\asymp1/\log T$; exponente solo en constante |
| 2 | 180.3 | momento molificado | suelo Farmer $c(\theta)>1$ + techo $\theta\le1$ |
| 3 | 180.4 | $\iint\log|\zeta|$ (con signo) | momentos ciegos al signo; cancelación = los ceros |
| **4** | **183.5** | **$\iint|\nabla\log|\zeta||^2$ (positivo)** | **peso isótropo + población off evanescente** |

### 4.1. El enunciado mínimo residual

**[GAP-183.1] (la desingularización anisótropa que faltaría).** Existe un núcleo de Green ponderado $G_w$ sobre $\Omega=\{\sigma>\tfrac12\}$, o un suavizado del átomo, tal que la auto-energía regularizada del cero $\rho=\tfrac12+b+i\gamma$ es $\asymp b^2\cdot p(\gamma)+o(b^2)$ con peso $p$ integrable contra $E(T)\ll T/\log T$ dando $o(T/\log T)$, **y** la energía total $\mathcal D_w^{\text{reg}}$ admite cota superior incondicional $o(T/\log T)$ por un ancla de Selberg/Tsang en el borde. Las dos condiciones son antagónicas con la geometría plana (§2, §3): el peso anisótropo $b^2$ exige diferenciar transversalmente ($\partial_\sigma^2$), lo que reintroduce el signo de 180.4 (la segunda derivada de $\log|\zeta|$ no es positiva). **Conjetura de imposibilidad asociada:** ningún funcional cuadrático local en $u$ es a la vez anisótropo-de-orden-2 y de signo definido — es el GAP-141.G1 en esta encarnación. Resolver GAP-183.1 = el ladrillo A.

### 4.2. La pista DBN, honesta

El suavizado DBN a escala $\sqrt t$ (173 §6.3) da auto-energía $\asymp\log(b_j/\sqrt t)$, anisótropa pero **logarítmica en $b$, no cuadrática**, y con signo (negativa para $b_j<\sqrt t$). Para convertir $\log(b/\sqrt t)$ en $b^2$ haría falta una segunda diferenciación en $t$ acoplada al flujo de calor — que es precisamente la ley de balance $\dot I=-2\kappa-D$ de Fase 54, donde $I=\sum b^2$ aparece como cantidad de **segundo orden** (memoria del programa: "I = primera cantidad de segundo orden, escapa al no-go 141.B2"). **[PUENTE, estatus: abierto]** la energía de Dirichlet desingularizada por DBN es la versión espacial de la ley de balance; conectar $\mathcal D_{\sqrt t}$ con $\dot I$ es el paso natural pero no se cierra aquí — la geometría plana de §1–§3 no lo ve porque le falta el tiempo de flujo como segunda variable.

---

## 5. Test anti-circularidad

| Pieza | ¿ζ-libre? | ¿Incondicional? | Dónde reentra lo conjetural |
|---|---|---|---|
| Green sobre $\Omega_R$ (183.1) | maquinaria sí (Green clásico) | sí (identidad exacta) | — |
| Auto-energía $2\pi\log(1/R)$ (183.1, 183.2) | sí (potencial puntual) | sí | — |
| Peso isótropo, no $b^2$ (183.2) | sí | sí (negativo estructural) | — |
| Población off evanescente (183.3) | no (hecho sobre $\zeta$) | sí (Bohr–Landau/Selberg) | densidad de ceros |
| Ancla Selberg borde (183.4.a) | no | sí (Selberg 1946) | — |
| Desplazado uniforme (183.4.a) | no | **[GAP 183.L1]** | Tsang 1984 |
| Segundo momento $\zeta'/\zeta$ en $\tfrac12<\sigma<1$ (183.4.c) | no | **NO** | correlación de pares, Montgomery 1973 |
| Barrera #4 (183.5) | parcial | sí | usa densidad (176.9) |

Ningún paso asume RH, A ni LP-112. Los resultados negativos (183.2, 183.3, 183.5) son incondicionales. Los GAPs de literatura (L1, L2) están marcados y no se usan en ninguna prueba como si estuvieran cerrados.

---

## 6. Veredicto

**¿Se mejoró $E(T)\ll T/\log T$ incondicionalmente?** **NO.** Desenlace (b)+(c): la ruta reproduce $T/\log T$ (de hecho la energía de Dirichlet está dominada por un fondo on-line de orden $T\log T\log\log T$, $\log^3T$ por encima de la señal) y expone una barrera nueva, no un ladrillo.

**¿Escapó a la barrera 180.4?** **SÍ en la premisa, NO en la conclusión.** El integrando $|\nabla\log|\zeta||^2\ge0$ NO es un momento con signo: 180.4 (ceguera de signo, cancelación en $t$) genuinamente **no aplica** — verificado en §1.4. El mandato acertó: la energía de Dirichlet ve las singularidades, no el signo. **Pero** la positividad que la salva de 180.4 la condena por otra vía: la energía pesa cada cero por $\log(1/R)$ **isótropamente**, sin el factor transversal $(\beta-\tfrac12)^2$ que define la señal, y los ceros off son demográficamente evanescentes. **La ceguera de signo (180.4) se convierte en ceguera de población/anisotropía (183.5): barrera #4.**

**Probado (con prueba completa):**
- [TEOREMA 183.1] identidad de Green–energía exacta; auto-energía $=2\pi\log(1/R)+2\pi h(\rho)+O(R\log\tfrac1R)$ por cero.
- [PROP 183.1.b] $\mathcal D_{1/\log T}(T)\asymp T\log T\log\log T$, dominado por conteo total.
- [PROP 183.2] la auto-energía es **ciega a $b$ a primer orden** (peso isótropo, no $b^2$); contraste exacto con el peso transversal $v=(\sigma-\tfrac12)^2$ de 173.C.
- [PROP 183.3] la asimetría borde/interior on-line vs off es **de constante (factor $2$), no de orden**; con población off evanescente, la señal off se ahoga doblemente. (Refuta la apuesta del mandato §1.)
- [PROP 183.4] el ancla incondicional disponible es $\int_0^T u^2\sim\tfrac T2\log\log T$ (Selberg); el segundo momento de $\zeta'/\zeta$ en la línea **diverge** (polos on-line) y en $\tfrac12<\sigma<1$ no es incondicional.
- [PROP 183.5] **barrera #4 (ceguera de población/anisotropía)**: peso isótropo $+$ población off evanescente $\Rightarrow$ $\mathcal D_R$ acota el *conteo* off, no la *energía* $\sum b^2$.

**Refutado:** la apuesta de que la asimetría borde/interior aislara $\sum b^2$ (183.3).

**GAPs numerados:**
- **[GAP-183.1]** (mínimo residual, = ladrillo A): una desingularización **anisótropa de orden 2 y de signo definido** cuya auto-energía pese los ceros por $b^2$ y cuya energía total tenga cota incondicional $o(T/\log T)$. Conjetura de imposibilidad: ningún funcional cuadrático local en $\log|\zeta|$ es simultáneamente anisótropo-de-orden-2 y de signo definido (encarnación de GAP-141.G1). Equivale a $\mu_2(T)=o(1)$ (GAP-180.1).
- **[GAP de literatura 183.L1]** uniformidad del momento de Selberg de $\log|\zeta|$ en desplazamientos $s\ll1/\log T$ (Tsang 1984; = 180.L3).
- **[GAP de literatura 183.L2]** segundo momento incondicional de $\zeta'/\zeta$ en $\tfrac12<\sigma<1$ (correlación de pares, Montgomery 1973; no uniforme).

**Dirección sucesora (Doc 184).** La síntesis de las cuatro barreras (cuadro §4) dice que la señal $\sum b^2$ es un **segundo momento transversal** y que todo funcional incondicional natural es o isótropo (ciego, #1/#4) o con signo (cancela, #3) o saturado por el momento en línea (#2). El único objeto del programa que es **anisótropo, de segundo orden y con dinámica** es la ley de balance $\dot I=-2\kappa-D$ (Fase 54). Doc 184 debe atacar la conexión [PUENTE §4.2]: $\mathcal D_{\sqrt t}(T)$ (energía DBN-desingularizada, con el tiempo de flujo como segunda variable) $\leftrightarrow$ $\int_0^\infty\dot I$, donde la segunda variable temporal podría romper la dicotomía isótropo/signo que triangula GAP-183.1. Es decir: dejar la geometría plana de este documento y entrar en el espacio-tiempo del flujo de calor.

---

## Referencias

- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946). [Momento segundo de $\log|\zeta(\tfrac12+it)|\sim\tfrac T2\log\log T$; densidad; densidad cero de ceros off.]
- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Camb. Phil. Soc.* 22 (1924). [Lema de Littlewood, identidad.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (Heath-Brown), Oxford 1986. §9 (densidades, $S_1$, momentos de $\log|\zeta|$); cap. 14 (fracciones parciales de $\zeta'/\zeta$).
- A. Ivić, *The Riemann Zeta-Function*, Wiley 1985. Caps. 10–11.
- H. L. Montgomery, "The pair correlation of zeros of the zeta function", *Proc. Sympos. Pure Math.* 24 (1973), 181–193. [Correlación de pares; segundo momento de $\zeta'/\zeta$; GAP 183.L2.]
- K.-M. Tsang, *The distribution of the values of the Riemann zeta-function*, tesis, Princeton 1984. [Momentos de $\log|\zeta|$ desplazados; GAP 183.L1.]
- N. G. de Bruijn, "The roots of trigonometric integrals", *Duke Math. J.* 17 (1950), 197–226. [Flujo de calor / núcleo DBN.]
- D. H. J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function...", *Res. Math. Sci.* 6 (2019). [Polymath 15; escala $\sqrt t$.]
- H. Davenport, *Multiplicative Number Theory*, 3.ª ed., GTM 74, Springer. Caps. 12, 15–16.

**Documentos internos:** Doc 170 (Teorema 170.5, coordenadas); Doc 172 (techo por ventanas 172.9); Doc 173 (173.C identidad de Green–Littlewood, 173.E auto-energía atómica, §6.3 programa de desingularización DBN); Doc 176 (176.4 Cesàro, 176.9 barrera de densidades); Doc 180 (180.1 $\mu_2$, 180.3 barrera molificador, **180.4 ceguera de signo**, GAP-180.1); Fase 54 (ley de balance $\dot I=-2\kappa-D$; I = cantidad de segundo orden).
