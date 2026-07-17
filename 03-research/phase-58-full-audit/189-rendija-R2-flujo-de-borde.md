# Documento 189 — La rendija R2 a cálculo completo: el flujo de borde $\mathcal F_{1/2}$ es exactamente la moneda de LP-134, y se reabsorbe en la barrera #3

**Programa:** Hipótesis de Riemann — Fase 58 (auditoría total)
**Fecha:** 2026-06-11
**Mandato:** ejecutar el cálculo completo del flujo de borde $\mathcal F_{1/2}(T)=-\int_0^T u(\tfrac12+it)\,\partial_\sigma u(\tfrac12+it)\,dt$, $u=\log|\zeta|$ — el único canal anisótropo de la geometría de Green de D183, despachado allí sin cálculo (E-188.4) y señalado por la auditoría D188 como rendija R2 — y decidir: ¿ruta nueva a una cota de $E(T)$, o reabsorción en barreras conocidas?
**Prerrequisitos (con erratas E-188.x aplicadas):** [THM 183.1] con signo corregido $c(\rho)=-2\pi h(\rho)$ (E-188.2); [183.4.b sustituido] $\int_0^T(\partial_\sigma u)^2\,dt\asymp T\log^2T$ FINITA (E-188.6); [183.1.b degradado] orden de $\mathcal D_R$ indeterminado entre $T\log T\log\log T$ y $T\log^2T$ (E-188.3); [183.3.b refutado] $N_{\rm off}=o(N)$ NO es incondicional (E-188.5); [PROP 180.4] (barrera #3, con E-188.1); [PROP 176.9] (barrera #1); [Thm 170.5] $E(T)\ll T/\log T$.
**Contrato:** [TEOREMA]/[PROP]/[LEMA] solo con prueba completa; sin numérica; backward-only; honestidad total.

**Coordenadas.** $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, un representante por cuádruplo; $E(T)=\sum_{\gamma\le T}b^2$; $J(T):=\sum_{\gamma\le T}b$ (primer momento, Littlewood); **A** $\iff E(T)=O(1)$.

---

## 0. Resumen ejecutivo y veredicto

1. **R2 queda SELLADA, con botín estructural.** El cálculo completo se hizo. Resultado central, exacto:
$$\boxed{\;\mathcal F_{1/2}(T)\;=\;\pi\sum_{\gamma\le T}b\,\log\frac{\gamma}{2\pi}\;+\;O(\log^2T)\;}$$
**El flujo de borde ES, idénticamente, la moneda de LP-134/178.C ($\sum b\log\gamma$) con constante $\pi$.** [TEOREMA 189.2]. Es la primera encarnación analítica (un flujo de Green) de esa moneda en el programa.
2. **El núcleo del flujo es EXACTAMENTE determinista.** $\partial_\sigma u(\tfrac12+it)=\mathrm{Re}\,\tfrac{\zeta'}\zeta(\tfrac12+it)=\tfrac12\mathrm{Re}\,\tfrac{\chi'}\chi(\tfrac12+it)=-\tfrac12\log\tfrac t{2\pi}+O(t^{-2})$, **sin término de ceros alguno**, por la ecuación funcional + reflexión de Schwarz — confirmación total de E-188.6, ahora como identidad y no como cancelación término a término. [LEMA 189.1]. Toda la información de ceros del flujo vive en el factor $u$; el flujo = integral de Littlewood con peso $\tfrac12\log\tfrac t{2\pi}$.
3. **Cota incondicional resultante:** $\sum_{\gamma\le T}b\log\gamma\le(\tfrac1{4\pi}+o(1))\,T\log T\log\log T$ [PROP 189.3] — pero es EXACTAMENTE lo que da sumación por partes sobre Littlewood 1924 ($J(T)\ll T\log\log T$). **El peso $\log t$ no compra nada**: es determinista y monótono, factoriza por bloques diádicos, y cada bloque reentra por Jensen + segundo momento, i.e. por Littlewood. No hay cota nueva.
4. **Mecanismo exacto de reabsorción (barrera #2-bis, [PROP 189.4]):** la anisotropía del borde es de **primer orden** en $b$; su contenido íntegro es $J$ pesada; toda cota de $J$ pesada pasa por $\int_0^Tu(\tfrac12+it)\,dt$ **con signo**, y por la bidireccionalidad de Littlewood ([180.4.b]: identidad, sin tercer término) acotar esa integral con signo ES contar ceros. El flujo reabsorbe en la barrera #3. Coherente con 141.B2 (no-go de primer orden): el flujo escapa a la *premisa* de 141.B2 (no es de integral cero — Littlewood es la excepción clásica, $\int u\ge-O(\log T)$) pero no a su *moraleja*: la positividad de primer orden ya tiene su teorema óptimo-conocido (Littlewood) y el flujo no añade información.
5. **La identidad de Green no despeja nada:** el término $\sum c(\rho)$ (incontrolado bajo $O(T\log^2T)$, E-188.3) ahoga cualquier despeje de $\mathcal F_{1/2}$ desde el volumen; y el flujo ya está mejor acotado directamente (punto 3) que cualquier cosa que Green pueda dar. §4.
6. **Botín:** (i) [TEOREMA 189.2] como pieza de contabilidad permanente — la moneda $\sum b\log\gamma$ tiene representación de flujo, luego cualquier progreso futuro sobre $\int_0^T\log t\cdot\log|\zeta(\tfrac12+it)|\,dt$ con signo se transfiere a LP-134∞ con constante explícita; (ii) positividad esencial $\mathcal F_{1/2}\ge-O(\log^2T)$; (iii) el muro queda escrito como UNA barrera-teorema + un principio (mandato del 188): la señal $\sum b^2$ es de segundo orden transversal, y el único canal anisótropo del objeto de Green es de primer orden.

---

## 1. El objeto exacto: el núcleo del flujo es ciego a los ceros

**[LEMA 189.1] (determinismo de $\partial_\sigma u$ en la línea).** Para todo $t>0$ que no sea ordenada de un cero,
$$\partial_\sigma u(\tfrac12+it)\;=\;\mathrm{Re}\,\frac{\zeta'}\zeta(\tfrac12+it)\;=\;\frac12\,\mathrm{Re}\,\frac{\chi'}\chi(\tfrac12+it)\;=\;-\frac12\log\frac t{2\pi}\;+\;O(t^{-2}),$$
identidad exacta en el paso central: **la parte real de $\zeta'/\zeta$ sobre la línea crítica no contiene término de ceros**.

*Prueba.* (1) $\partial_\sigma u=\mathrm{Re}(\zeta'/\zeta)$ por Cauchy–Riemann ([183.1] §1.1, verificado en D188). (2) Ecuación funcional $\zeta(s)=\chi(s)\zeta(1-s)$, derivada logarítmica:
$$\frac{\zeta'}\zeta(s)\;=\;\frac{\chi'}\chi(s)\;-\;\frac{\zeta'}\zeta(1-s).$$
En $s=\tfrac12+it$: $1-s=\tfrac12-it=\bar s$. Como $\zeta(\bar s)=\overline{\zeta(s)}$ (coeficientes reales, reflexión de Schwarz), $\frac{\zeta'}\zeta(\tfrac12-it)=\overline{\frac{\zeta'}\zeta(\tfrac12+it)}$. Luego
$$\frac{\zeta'}\zeta(\tfrac12+it)+\overline{\frac{\zeta'}\zeta(\tfrac12+it)}\;=\;\frac{\chi'}\chi(\tfrac12+it)\quad\Longrightarrow\quad 2\,\mathrm{Re}\,\frac{\zeta'}\zeta(\tfrac12+it)=\mathrm{Re}\,\frac{\chi'}\chi(\tfrac12+it).$$
(3) Stirling sobre $\chi(s)=2^s\pi^{s-1}\sin(\tfrac{\pi s}2)\Gamma(1-s)$ (Titchmarsh §4.12): $\mathrm{Re}\,\frac{\chi'}\chi(\tfrac12+it)=-\log\tfrac t{2\pi}+O(t^{-2})$, $t\ge1$. $\square$

**Verificación independiente (la cancelación del gemelo, microscopio de E-188.6).** Por fracciones parciales, el término de un cero on-line $\tfrac12+i\gamma'$ es $\mathrm{Re}\,\frac1{i(t-\gamma')}=0$; el par off $(\tfrac12\pm b+i\gamma)$ aporta $\mathrm{Re}\big[\frac1{-b+i\tau}+\frac1{b+i\tau}\big]=\frac{-b}{b^2+\tau^2}+\frac{b}{b^2+\tau^2}=0$ ($\tau=t-\gamma$). La cancelación es **puntual y exacta**, no en media — el Lema la obtiene sin sumas condicionalmente convergentes, vía la ecuación funcional, que es la forma globalmente rigurosa del mismo hecho. Nótese también: $\mathrm{Re}\,\zeta'/\zeta$ se extiende continua a través de cada ordenada (la singularidad vive íntegra en $\mathrm{Im}=−S'$), mientras $u\to-\infty$ logarítmicamente (integrable): $\mathcal F_{1/2}$ es una integral absolutamente convergente, bien definida sin valor principal.

**Lectura.** D183 temía polos del núcleo (prueba falsa de 183.4.b); D188 los desmintió. Aquí queda en limpio lo más fuerte: el núcleo no solo no tiene polos — **no tiene señal**. Es la función determinista $-\tfrac12\log\tfrac t{2\pi}$. La anisotropía del flujo no puede venir del núcleo; viene solo de $u$.

## 2. La identidad del flujo: $\mathcal F_{1/2}$ = Littlewood con peso $\log$

Con la convención de D183 (§2): $\mathcal F_{1/2}(T)=-\int_0^Tu\,\partial_\sigma u\,dt$ (normal saliente de $R_T$ en $\sigma=\tfrac12$ es $-\partial_\sigma$). Por [LEMA 189.1], escribiendo $\omega(t):=\log\tfrac t{2\pi}$:
$$\mathcal F_{1/2}(T)\;=\;\frac12\int_0^T\omega(t)\,\log|\zeta(\tfrac12+it)|\,dt\;+\;O(1),$$
(el $O(t^{-2})$ contra $u$ integra $O(1)$ por integrabilidad local de $u$ y Selberg; el tramo $t\le2\pi e$ es $O(1)$).

**[LEMA 189.2.a] (Littlewood en la línea, forma usada).** $\displaystyle\int_0^T\log|\zeta(\tfrac12+it)|\,dt=2\pi J(T)+O(\log T)$, con $J(T)=\sum_{\gamma\le T}b$ (un sumando por cuádruplo: del cuádruplo, solo $\beta=\tfrac12+b$, $\gamma>0$ tiene $\beta>\tfrac12$). Es el lema de Littlewood en $\sigma_0=\tfrac12$ (Littlewood 1924; Titchmarsh §9.9; misma normalización que [180.4.b]). En particular $\int_0^Tu\,dt\ge-O(\log T)$. *(Citado, no re-derivado: es el [180.4.b] certificado.)*

**[TEOREMA 189.2] (el flujo de borde es la moneda de LP-134).**
$$\mathcal F_{1/2}(T)\;=\;\pi\sum_{\gamma\le T}b\,\log\frac\gamma{2\pi}\;+\;O(\log^2T).$$

*Prueba.* Sea $L(t):=\int_0^tu(\tfrac12+iv)\,dv=2\pi\tilde J(t)+\varepsilon(t)$, $\tilde J(t)=\sum_{\gamma\le t}b$, $|\varepsilon(t)|\ll\log(t+2)$ [LEMA 189.2.a]. Integración por partes ($\omega'(t)=1/t$):
$$\int_0^T\omega\,dL=\omega(T)L(T)-\int_{2\pi}^T\frac{L(t)}t\,dt+O(1)=2\pi\Big[\omega(T)\tilde J(T)-\int_{2\pi}^T\frac{\tilde J(t)}t\,dt\Big]+O(\log^2T),$$
donde el error usa $|\omega(T)\varepsilon(T)|\ll\log^2T$ y $\int^T\frac{|\varepsilon|}t\ll\log^2T$. Intercambiando suma e integral (todo positivo, Tonelli):
$$\omega(T)\tilde J(T)-\int_{2\pi}^T\frac{\tilde J(t)}t\,dt=\sum_{\gamma\le T}b\Big[\omega(T)-\int_{\max(\gamma,2\pi)}^T\frac{dt}t\Big]=\sum_{\gamma\le T}b\,\log\frac{\max(\gamma,2\pi)}{2\pi}=\sum_{\gamma\le T}b\,\log\frac\gamma{2\pi}+O(1)$$
(los ceros con $\gamma<2\pi$: no hay — el primer cero está en $\gamma\approx14$; el ajuste es vacío). Multiplicar por $\tfrac12$. $\square$

**Contraste con el cálculo local (sanidad cruzada con D188 §2.3).** La firma de un cuádruplo en $u$ sobre la línea, respecto de dos ceros on-line en $\gamma$, es $\log\frac{\tau^2+b^2}{\tau^2}\ge0$, con masa $\int_{-\infty}^\infty\log\big(1+\tfrac{b^2}{\tau^2}\big)d\tau=2\pi b$ (clásico: $\int\log(1+b^2/x^2)dx=2\pi b$ por partes + arctan), localizada en $|\tau|\lesssim b$. Pesada por el núcleo $\tfrac12\omega(t)\approx\tfrac12\omega(\gamma)$ (suave en escala $b$): contribución $\pi b\log\tfrac\gamma{2\pi}$ por cuádruplo — **exactamente el sumando de 189.2**. La señal de D188 ("$\asymp b\log t$ por cero off") queda confirmada y promovida a identidad global.

**[COR 189.2.b] (positividad y caso RH).** $\mathcal F_{1/2}(T)\ge-O(\log^2T)$ incondicionalmente; bajo RH, $\mathcal F_{1/2}(T)=O(\log^2T)$. Y **A no controla $\mathcal F_{1/2}$**: por Cauchy–Schwarz $\sum b\log\gamma\le(\sum b^2)^{1/2}(\sum_{\rm off}\log^2\gamma)^{1/2}$, que aun con $E=O(1)$ deja $\ll(N_{\rm off}\log^2T)^{1/2}$ — la moneda $J$-pesada y la moneda $E$ no son comparables sin control de población (consistente con E-188.5).

## 3. El presupuesto incondicional: el peso $\log t$ no compra nada

**[PROP 189.3] (cota incondicional del flujo y de la moneda LP-134).**
$$\mathcal F_{1/2}(T)\;\le\;\Big(\tfrac14+o(1)\Big)\,T\log T\log\log T,\qquad\text{equivalentemente}\qquad\sum_{\gamma\le T}b\log\gamma\;\le\;\Big(\tfrac1{4\pi}+o(1)\Big)\,T\log T\log\log T,$$
**y esta cota coincide (orden y método) con la sumación por partes sobre Littlewood clásico: no es nueva.**

*Prueba.* Por bloques diádicos $[T_k/2,T_k]$, $T_k=T/2^k$: en cada bloque $\omega(t)\le\log\tfrac{T_k}{2\pi}$, y por Jensen (concavidad de $\log$) con el segundo momento $\int_{T_k/2}^{T_k}|\zeta(\tfrac12+it)|^2dt\sim\tfrac{T_k}2\log T_k$ (Hardy–Littlewood 1918):
$$\int_{T_k/2}^{T_k}u\,dt\le\frac{T_k}2\cdot\frac12\log\Big(\frac2{T_k}\int_{T_k/2}^{T_k}|\zeta|^2\Big)=\frac{T_k}4\log\log T_k+O(T_k).$$
Sumando $\sum_k\log T_k\cdot\big[\tfrac{T_k}4\log\log T_k+O(T_k)\big]\le(\tfrac12+o(1))\cdot\tfrac{T}4\cdot\log T\log\log T\cdot 2=(\tfrac14+o(1))T\log T\log\log T$ (serie geométrica en $T_k$; el factor $\log T_k\le\log T$ y $\sum T_k\le2T$ dan la constante con $o(1)$ tras separar $k\le\log\log T$). La equivalencia con la suma es 189.2. *Comparación:* Littlewood clásico es el caso $\omega\equiv1$ del mismo argumento ($J(T)\le(\tfrac1{4\pi}+o(1))T\log\log T$, Littlewood 1924 vía Jensen + segundo momento), y la sumación por partes diádica de Abel sobre $J$ da exactamente $\sum b\log\gamma\ll T\log T\log\log T$ con la misma constante. $\square$

**Por qué el peso no puede comprar.** El único input zeta-dependiente del argumento es, bloque a bloque, $\int u\,dt$ — y el peso $\omega$, al ser **determinista y de variación lenta** ($\omega'/\omega\asymp1/(t\log t)$, constante en cada bloque a error $O(1)$), conmuta con la maquinaria: cualquier funcional $\int W(t)\,u\,dt$ con $W>0$ determinista de variación lenta se descompone diádicamente en copias de Littlewood. Para que un peso ayudara tendría que **anticorrelacionarse con $u$** — i.e., contener información de ceros — y [LEMA 189.1] dice que el único peso que la geometría de Green ofrece (el núcleo $\partial_nu$) es precisamente determinista. La rendija se cierra sobre sí misma: *el mismo teorema que hace al flujo computable (núcleo sin señal) lo hace estéril (peso sin señal).*

**¿Mejorar Littlewood mismo?** Reduciría a acotar $\int_0^Tu\,dt$ (con signo) mejor que $T\log\log T$. Por [180.4.b] (identidad bidireccional, certificada en D188) eso ES acotar $J(T)$: no hay tercer término. Los momentos son ciegos al signo (barrera #3); el CLT de Selberg dice que $|u|$ típico es $\asymp\sqrt{\log\log T}$, luego la media $\le\tfrac12\log\log T$ de Jensen solo es mejorable detectando la cancelación — que es la incógnita. Circularidad limpia, no defecto técnico. *(Mejor de lo posible aquí: bajo la plausible simetría de Selberg, $\int u\,dt=o(T\sqrt{\log\log T})$ "debería" valer; pero probarlo incondicionalmente implicaría $J(T)=o(T\sqrt{\log\log T})$, mejora de Littlewood que la literatura no tiene — calibre de la dificultad, no [GAP] nuestro.)*

## 4. ¿Despeja algo la identidad de Green? No: balance de las tres piezas

Con las correcciones E-188.x, la identidad [183.1] a escala $R\asymp1/\log T$ es
$$\underbrace{\mathcal D_R(T)}_{\text{volumen}}\;=\;\underbrace{2\pi N(T)\log\tfrac1R-2\pi\sum_\rho h(\rho)+O(RN\log\tfrac1R)}_{\text{átomos}}\;+\;\underbrace{\mathcal F_{1/2}(T)}_{\text{borde crítico}}\;+\;\underbrace{O(\log^2T)}_{\text{bordes horizontales}, \sigma=X}.$$
Presupuesto de cada pieza: volumen $\in[c\,T\log T\log\log T,\;C\,T\log^2T]$ con orden exacto indeterminado (E-188.3); átomos: término principal $\asymp T\log T\log\log T$ conocido, pero $\sum h(\rho)$ solo acotado por $O(N\log T)=O(T\log^2T)$ **sin signo ni cancelación probada**; borde: $\mathcal F_{1/2}\ll T\log T\log\log T$ por [PROP 189.3], y $\ge-O(\log^2T)$ por [COR 189.2.b].

**Despeje imposible:** para extraer $\mathcal F_{1/2}$ (y con él $\sum b\log\gamma$) de Green haría falta conocer volumen y $\sum h(\rho)$ con error $o(T\log T\log\log T)$; el desconocimiento de $\sum h(\rho)$ es $O(T\log^2T)$ — un factor $\log T/\log\log T$ POR ENCIMA de la cota directa de 189.3. **Green da, para el flujo, una cota peor que la trivial.** En la otra dirección, usar 189.3 + átomos para acotar $\mathcal D_R$ tampoco aporta: reproduce el encuadre de E-188.3. El sistema tiene una ecuación y dos incógnitas grandes ($\mathcal D_R$, $\sum h$); el flujo es la incógnita pequeña y ya está mejor medido por fuera. Nada que despejar.

## 5. La barrera, enunciada: #2-bis (anisotropía de primer orden)

**[PROP 189.4] (sellado de R2 — mecanismo de reabsorción).** El canal anisótropo de la geometría de Green plana sobre $\{\sigma>\tfrac12\}$ — el flujo del borde crítico — satisface: (i) su núcleo es determinista ([LEMA 189.1]); (ii) su contenido de ceros es exactamente el primer momento pesado $\pi\sum b\log\tfrac\gamma{2\pi}$ ([TEOREMA 189.2]) — **primer orden en $b$, no segundo**; (iii) toda cota superior incondicional suya por las maquinarias existentes se factoriza, vía descomposición diádica del peso determinista, en el problema de Littlewood $\int_0^Tu\,dt$ con signo, que por la identidad [180.4.b] equivale a acotar $J(T)$ — territorio de la barrera #3; (iv) la cota resultante, $T\log T\log\log T$, coincide con la sumación por partes del teorema de Littlewood 1924 y no mejora ni $E(T)\ll T/\log T$ ni $J(T)\ll T\log\log T$ ni la moneda LP-134.

*Prueba.* (i)=189.1, (ii)=189.2, (iii)=§3 (argumento del peso de variación lenta + bidireccionalidad 180.4.b), (iv)=189.3. $\square$

**Relación con 141.B2 y con el muro.** 141.B2 (no-go de primer orden) descarta funcionales lineales de integral cero; Littlewood es la excepción de signo (positividad $\int u\ge-O(\log T)$) y por eso el primer orden SÍ tiene un teorema — pero **uno solo**, el de 1924, y el flujo de borde resulta ser ese teorema con un peso inerte. La taxonomía del muro queda así (mandato del 188 cumplido): **una barrera-teorema** (#1, densidades, 176.9) **+ un principio estructural unificado**: *la señal $\sum b^2$ es segundo momento transversal; los funcionales incondicionales son isótropos (ciegos a dirección: #1, #4-interior), con signo (ciegos por cancelación: #3), saturados en línea (#2, condicional-a-Farmer), o anisótropos-de-primer-orden (este doc: agotados por Littlewood).* La casilla "anisótropo de segundo orden con signo definido" sigue vacía: es GAP-183.1 = GAP-180.1 = género 141.G1, intacto.

## 6. Test anti-circularidad

| Pieza | ¿ζ-libre? | ¿Incondicional? | Notas |
|---|---|---|---|
| [LEMA 189.1] núcleo determinista | no (ec. funcional de ζ) | sí (identidad) | reflexión de Schwarz, sin sumas sobre ceros |
| [TEOREMA 189.2] flujo = moneda | maquinaria sí (Abel) | sí | input: Littlewood 1924 (identidad) |
| [PROP 189.3] cota | no | sí | inputs: Hardy–Littlewood 1918 + Jensen |
| [PROP 189.4] sellado | — | sí | usa 180.4.b certificado; alcance: maquinarias diádico-factorizables (clase formal en (iii), informal en la moraleja — mismo estatus que la barrera #3) |

Ningún paso asume RH, A, LP-112 ni LP-134. Ningún GAP de literatura se usa como cerrado; [PROP 189.3] evita deliberadamente el GAP 180.L3/183.L1 (Tsang) usando solo el segundo momento de $|\zeta|$, no el de $\log|\zeta|$ desplazado.

## 7. Veredicto

**R2: SELLADA — desenlace (b) con botín estructural (c-menor).** No hay cota nueva de $E(T)$, de $J(T)$ ni de $\sum b\log\gamma$: el flujo de borde es la moneda de LP-134 disfrazada de flujo, y su presupuesto es el de Littlewood con peso inerte. El mecanismo de reabsorción está probado, no asertado (la deuda E-188.4 queda saldada con identidad exacta).

**Probado:** [LEMA 189.1] (núcleo determinista, identidad); [TEOREMA 189.2] ($\mathcal F_{1/2}=\pi\sum b\log\tfrac\gamma{2\pi}+O(\log^2T)$); [COR 189.2.b] (positividad; A no controla el flujo); [PROP 189.3] ($\sum b\log\gamma\le(\tfrac1{4\pi}+o(1))T\log T\log\log T$, = Littlewood por partes, no nueva); [PROP 189.4] (barrera #2-bis, sellado de R2).

**GAPs numerados:**
- **[GAP-189.1]** ¿existe un peso $W(t)>0$ NO determinista — construido de datos incondicionales de ζ (p.ej. $|\zeta|^2$ normalizado, momentos locales) — tal que $\int_0^TW\,u\,dt$ acote $J$ pesada mejor que Littlewood sin reentrar por la identidad? La descomposición de §3 solo cubre pesos deterministas de variación lenta; un peso aleatorio-correlacionado escapa formalmente a [PROP 189.4.iii], pero todo candidato examinado (peso $|\zeta|^2$: da el momento $\int|\zeta|^2\log|\zeta|$, territorio de momentos torcidos, mismo suelo) reentra. Estatus: rendija formal de tercera generación, prioridad baja.
- **[GAP de literatura 189.L1]** ¿está la cota $\sum_{\gamma\le T}(\beta-\tfrac12)\log\gamma\ll T\log T\log\log T$ — o una mejora — explícita en la literatura ($S_1$, Fujii)? Es sumación por partes de Littlewood, luego "conocida-en-potencia"; verificar si alguien la mejoró (conectar con 180.L4/188.L2, auditoría Fujii pendiente).

**Dirección sucesora.** Con R2 sellada y R1 (suelo de Farmer, 188.L1) como única rendija formal del muro, el frente vuelve a donde D188 §5 lo dejó: la casilla vacía "anisótropo de orden 2 con signo" (GAP-183.1/180.1/141.G1) y el [PUENTE 183 §4.2] espacio-temporal ($\mathcal D_{\sqrt t}\leftrightarrow\dot I=-2\kappa-D$, Fase 54), que es el único objeto del programa que vive en esa casilla. El subproducto utilizable de este doc para la torre 2: **toda mejora futura de $\int\omega\,u\,dt$ se convierte en mejora de la moneda LP-134∞ con constante $\pi$ exacta** ([TEOREMA 189.2]).

---

## Referencias

- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Camb. Phil. Soc.* 22 (1924). [Lema de Littlewood; $J(T)\ll T\log\log T$.]
- G. H. Hardy, J. E. Littlewood, "Contributions to the theory of the Riemann zeta-function...", *Acta Math.* 41 (1918). [Segundo momento $\sim T\log T$.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Oxford 1986. §4.12 ($\chi$, Stirling); §9.9 (Littlewood, $S_1$).
- A. Selberg, "Contributions...", *Arch. Math. Naturvid.* 48 (1946). [CLT de $\log|\zeta|$ — solo calibratorio aquí.]
- A. Ivić, *The Riemann Zeta-Function*, Wiley 1985.

**Documentos internos:** D170 (Thm 170.5); D173 (173.C); D176 (176.9); D180 (180.4 con E-188.1); D183 (183.1 con E-188.2/3, $\mathcal F_{1/2}$, con E-188.4/5/6); **D188 (auditoría que abrió R2; todas las erratas E-188.x aplicadas)**; Fase 54 (ley de balance); D177/178 (moneda $\sum b\log\gamma$, LP-134∞, confinamiento 178.C).
