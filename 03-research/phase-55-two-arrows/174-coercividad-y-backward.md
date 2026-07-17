# Documento 174 — Coercividad, extinción forward y la estructura backward de la rigidez

**Programa:** Hipótesis de Riemann — Fase 55 (dos flechas)
**Fecha:** 2026-06-11
**Mandato:** Problema B del director por la vía dinámica: coercividad (B2), flujo backward, presupuesto de colisiones (B3), Lyapunov/momentos (B1). NO auditar; construir. NO probar RH.
**Prerrequisitos (certificados, no re-derivados):** Doc 167 (ley de balance $\dot I=-2\kappa-D$, $D\ge0$; Thm 2.3 CERTIFICADO por Doc 168), Doc 168 (reparaciones: carta única, Cor 2.5 condicional, lema regalo $H_t|_{i\mathbb R}>0$), Doc 170 (envolvente $E(T)\ll T/\log T$; no-go tasa/total, Thm 170.8), Doc 144 (contraejemplo Hadamard $m=\infty$, $I<\infty$).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] prueba completa o sin etiqueta; [PUENTE] honesto; [GAP] declarado.

---

## 0. Carta única y convenciones (cumpliendo la reparación 2 del Doc 168)

**Carta $H_t$ (Polymath 15) en todo el documento.** $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$, $\partial_tH_t=-\partial_z^2H_t$, $H_0=\tfrac18\Xi(\cdot/2)$. Ceros de $H_0$ = ceros de $\Xi$ dilatados por 2: banda $|\operatorname{Im}z|<1$ (estricta, Hadamard–de la Vallée Poussin), densidad $N(T)=\frac{T}{2\pi}\log\frac{T}{4\pi e}+O(\log T)$. Conversión a carta ζ: $b_\zeta=\beta/2$, $\tau_\zeta=t/4$; la ley de balance es invariante de escala (Doc 168 §2), las constantes no — todas las constantes de este documento son de la carta $H_t$, y al final de cada enunciado relevante se da la versión ζ.

Ceros superiores $z_k=\alpha_k+i\beta_k$, $\beta_k>0$; $\kappa(t)=\#$ceros superiores; $I(t)=\sum_k\beta_k^2$; $M(t)=\max_k\beta_k^2$ (cuando $\kappa<\infty$). Ley certificada (Thm 167-2.3): en intervalos con $\kappa<\infty$ constante y ceros simples,
$$\dot I=-2\kappa-D,\qquad D\ge0\ \text{explícita, término a término}.$$
Inputs duros: [dB] de Bruijn 1950; [N] Newman 1976; [CSV] Csordas–Smith–Varga 1994; [KKL] Ki–Kim–Lee 2009 ($\forall t>0$: finitos ceros no reales); [RT] Rodgers–Tao 2020 ($\Lambda\ge0$); [P15] Polymath 2019. Lema regalo (Doc 168 §3.3): $H_t(i\beta)>0$ para todo $t,\beta$ ⟹ el eje imaginario nunca se toca ⟹ paridad $\kappa\in2\mathbb Z$ sellada en todo el flujo, $\kappa\ge2$ mientras $\kappa>0$.

**Dato estructural que gobierna todo el documento (no se pierde):** "$0<I(0)<\infty$ imposible" es **FALSO** en la clase de Pólya general — existe función de la clase con un solo cuádruplo off (p.ej. $(z^2-w)(z^2-\bar w)e^{-z^2/N}$-tipo, o el contraejemplo de Hadamard del Doc 144 con un solo factor). Toda prueba de la flecha B debe usar la condición inicial aritmética de ζ. Este documento construye el mapa de QUÉ propiedad dinámica puede portarla y QUÉ rutas quedan cerradas.

---

## 1. El mapa forward (B2): la coercividad, resuelta honestamente

### 1.1. $D\ge cI$ es FALSA — el contraejemplo exacto

**[PROP 174.1] (no-coercividad de la disipación).** Para la configuración de un cuádruplo aislado $\{z_1,\bar z_1,-z_1,-\bar z_1\}$, $z_1=\alpha+i\beta$ (sin ceros reales), la disipación de la ley de balance es exactamente
$$D=\frac{4\beta^2}{\alpha^2+\beta^2},\qquad I=2\beta^2,\qquad \frac{D}{I}=\frac{2}{\alpha^2+\beta^2}\;\xrightarrow{\alpha\to\infty}\;0.$$
No existe $c>0$ con $D\ge cI$ en la clase.

*Prueba.* Desde la dinámica: para $z_1$, los vecinos son $\bar z_1$ (conjugado: aporta el $-2$ universal), $-\bar z_1$ (espejo: aporta $0$), $-z_1$ (antípoda). $\dot\beta_1=-2\bigl[\tfrac{2\beta}{4\beta^2}+\tfrac{2\beta}{4|z_1|^2}\bigr]=-\tfrac1\beta-\tfrac{\beta}{|z_1|^2}$. Con dos ceros superiores ($z_1$ y $-\bar z_1$, misma altura): $\dot I=4\beta\dot\beta_1=-4-\tfrac{4\beta^2}{|z_1|^2}$. Como $-2\kappa=-4$, queda $D=4\beta^2/|z_1|^2$. Los términos cruzados $(\beta_k-\beta_l)^2$ de la fórmula del Thm 167-2.3 se anulan (alturas iguales) y los $(\beta_k+\beta_l)^2$ reproducen exactamente el término antípoda — consistencia verificada. $\square$

**Lectura.** El cuádruplo solo casi no disipa por interacción: $D\to0$ a altura grande. La coercividad de la *disipación* es falsa. **Pero la pregunta B2 estaba mal planteada en la variable $D$:** la tasa que importa no es $D$ sino el término cuantizado $-2\kappa$, que es *más fuerte que coercivo*:

### 1.2. Coercividad restaurada por cuantización + banda

**[TEOREMA 174.2] (coercividad exponencial sin $D$).** Sea $J\subset(0,\infty)$ un intervalo con $\kappa<\infty$ y ceros simples c.t.p. (cierto para todo $t>0$ salvo colisiones localmente finitas, [KKL] + reparación 5 del Doc 168). Entonces en $J$:
$$\dot I\;\le\;-\frac{2I}{M(t)}\;\le\;-2I,$$
y en consecuencia $I(t)\le I(t_0)\,e^{-2(t-t_0)}$ y, usando $M(t)\le M(t_0)-2(t-t_0)$ (Lema 174.3 abajo),
$$I(t)\;\le\;I(t_0)\Bigl(1-\frac{2(t-t_0)}{M(t_0)}\Bigr)_+\qquad\text{(extinción lineal exacta en } t_0+M(t_0)/2\text{)}.$$

*Prueba.* $I=\sum\beta_k^2\le\kappa\cdot\max\beta_k^2=\kappa M$, luego $-2\kappa\le-2I/M$; y $M(t)<1$ para $t\ge0$ (banda estricta en $t=0$, no-creciente por el Lema 174.3). $\dot I\le-2\kappa-0\le-2I/M\le-2I$. La integración de $\dot I\le-2I/(M_0-2(t-t_0))$ da $\log I\le\log I_0+\log\frac{M_0-2(t-t_0)}{M_0}$. $\square$

**Resolución de B2, dicha sin adornos:** la desigualdad de Lyapunov $\dot L\le-cL$ con $L\ge cI$ **existe y es $L=I$ misma, con $c=2$** — pero la coercividad NO viene de la disipación por interacción $D$ (falsa, Prop 174.1), sino del producto de dos hechos: (i) cada modo disipa a tasa constante exacta $2$ (cuantización, Thm 167-2.3), (ii) cada modo porta energía $<M\le1$ (banda). *Disipación constante por modo + energía acotada por modo ⟹ tasa exponencial.* En carta ζ: $\dot I_\zeta\le-2I_\zeta/M_\zeta$ con $M_\zeta<1/4$, es decir $\dot I_\zeta\le-8I_\zeta$ en tiempo ζ.

### 1.3. El principio del máximo de la dinámica (la banda de de Bruijn desde las partículas)

**[LEMA 174.3] (principio del máximo; = Thm 13 de [dB], prueba nueva por dinámica).** En un intervalo con $\kappa<\infty$ y ceros simples, $M(t)=\max_k\beta_k(t)^2$ satisface $D^+M\le-2$. En particular $M(t)\le M(t_0)-2(t-t_0)$ y todo cero superior aterriza antes de $t_0+M(t_0)/2$.

*Prueba.* $M$ es máximo de finitas funciones lisas, luego Lipschitz, con $D^+M=\max\{2\beta_k\dot\beta_k:\beta_k^2=M\}$. Para $k$ con $\beta_k$ maximal, en la descomposición de $\dot\beta_k$ (prueba del Thm 167-2.3): el conjugado propio da exactamente $-2$ a $2\beta_k\dot\beta_k$; el antípoda y los ceros reales dan $\le0$; los términos con otros ceros superiores entran como $-4\beta_k(\beta_k-\beta_l)/d^2$ (con $w\in\{z_l,-\bar z_l\}$, $\operatorname{Im}w=\beta_l$) y $-4\beta_k(\beta_k+\beta_l)/d^2$ (con $w\in\{\bar z_l,-z_l\}$): **para el maximal, $\beta_k-\beta_l\ge0$ y $\beta_k+\beta_l>0$, todos $\le0$ sin necesidad de simetrizar.** Suma total $\le-2$. Convergencia: $\kappa<\infty$ + RvM, como en el Thm 167-2.3. $\square$

*Honestidad de literatura:* el enunciado es el teorema de banda decreciente de de Bruijn 1950 (Thm 13: ceros en $|\operatorname{Im}|\le\Delta$ ⟹ en $|\operatorname{Im}|\le\sqrt{\Delta^2-2t}$); lo nuevo es solo la prueba por el sistema de partículas, que además lo localiza (vale cero a cero para el máximo corriente, no solo para el sup global de la clase).

### 1.4. El tiempo de aterrizaje exacto del cuádruplo aislado (la pregunta del director, cerrada)

**[TEOREMA 174.4] (modelo cerrado del cuádruplo: solución exacta).** El sistema de 4 ceros $\{\pm z_1,\pm\bar z_1\}$ bajo $\dot z_k=2\sum_{j\ne k}1/(z_k-z_j)$ es exactamente el flujo del calor backward sobre $H_t(z)=z^4+a(t)z^2+c(t)$, con $\dot a=-12$, $\dot c=-2a$. En la variable $w:=z_1^2$ ($\operatorname{Re}w=\alpha^2-\beta^2$, $\operatorname{Im}w=2\alpha\beta$):
$$\frac{d}{dt}\operatorname{Re}w=6,\qquad \frac{d}{dt}(\operatorname{Im}w)^2=-8\operatorname{Re}w,$$
luego $(\operatorname{Im}w)^2(t)=(\operatorname{Im}w_0)^2-8\operatorname{Re}w_0\,t-24t^2$ y el aterrizaje (cero real doble en $\pm\sqrt{\operatorname{Re}w(t_c)}$, simultáneo por paridad — la forma normal del Thm 167-1.4(2) realizada) ocurre en
$$\boxed{\;t_c\;=\;\frac{-\operatorname{Re}w_0+\sqrt{(\operatorname{Re}w_0)^2+\tfrac32(\operatorname{Im}w_0)^2}}{6}\;=\;\frac{\beta_0^2}{2}-\frac{\beta_0^4}{4\alpha_0^2}+O\Bigl(\frac{\beta_0^6}{\alpha_0^4}\Bigr)\quad(\alpha_0\gg\beta_0).\;}$$

*Prueba.* Para un polinomio mónico, $\dot z_k=H''/H'(z_k)=2\sum_{j\ne k}(z_k-z_j)^{-1}$ ⟺ $\partial_tH=-\partial_z^2H$ (grado 4: $\partial_z^2H=12z^2+2a$, luego $\dot a=-12$, $\dot c=-2a$). $w,\bar w$ son las raíces de $X^2+aX+c$: $\operatorname{Re}w=-a/2$, $(\operatorname{Im}w)^2=c-a^2/4$; derivar. El aterrizaje es $\operatorname{Im}w=0$ (los dos $w$ colisionan en $\operatorname{Re}w(t_c)>0$ y $z^2=\operatorname{Re}w$ da los dos dobles reales $\pm x_0$). Expansión: $\sqrt{R^2+6\alpha^2\beta^2}$ con $R=\alpha^2-\beta^2$. **Verificación cruzada contra la ley certificada:** del modelo, $I=2\beta^2=|w|-\operatorname{Re}w$ y $\dot I=2\operatorname{Re}w/|w|-6=-4-4\beta^2/|z_1|^2$ — coincide exactamente con la Prop 174.1. $\square$

**Respuesta a "¿$t_{\rm aterrizaje}=b^2/4$ exacto?": NO — es $\beta_0^2/2$, no $\beta_0^2/4$.** Para el par conjugado aislado ($H=z^2+c_0-2t$, el modelo del Doc 168 §1): $t_c=\beta_0^2/2$ **exacto**. Para el cuádruplo: $t_c=\beta_0^2/2$ solo asintóticamente ($\alpha\gg\beta$), con corrección **negativa** $-\beta_0^4/4\alpha_0^2$ (la interacción intra-cuádruplo acelera el aterrizaje, consistente con $D>0$). La forma invariante correcta es $t_c=I_0/(2\kappa)\cdot(1+o(1))=I_0/4$ por cuádruplo: el "$b^2/4$" del enunciado del director es correcto **si $b^2$ denota la energía total del cuádruplo $I_0=2\beta_0^2$**, y es falso por factor 2 si denota la altura al cuadrado. En carta ζ: $\tau_c=b_\zeta^2/2$ — el mismo $1/2$, por invariancia de escala.

### 1.5. El teorema de estructura forward

**[TEOREMA 174.5] (extinción forward universal; dónde vive RH).** Para todo $t_0>0$, incondicionalmente:
1. $\kappa(t_0)<\infty$, $I(t_0)<\infty$ [KKL], y mientras $\kappa>0$: $\dot I\le-2\kappa\le-4$ (paridad sellada por el lema regalo) **y** $\dot I\le-2I$ (Thm 174.2): la disipación es constante-por-modo Y exponencial a la vez.
2. Extinción en tiempo finito: $\Lambda\le t_0+\min\bigl\{\tfrac14I(t_0),\;\tfrac12M(t_0)\bigr\}$ (Cor 167-2.4 reparado + Lema 174.3), y cada cuádruplo individual aterriza en tiempo $\lesssim\beta^2/2$ (Thm 174.4; los clusters aterrizan aún antes, §3.2).
3. **Hacia adelante TODO muere, con tasas explícitas y sin hipótesis aritmética.** La única información que el escenario ¬RH puede portar es la condición de frontera en $t\to0^+$: el valor $I(0^+)\in[0,\infty]$ y $\kappa(0^+)\in\{0,2,4,\dots,\infty\}$. **La pregunta de RH vive enteramente en $t=0$ y en $t=0^-$; el semieje $t>0$ es trivial módulo [KKL].**

*Prueba.* (1)–(2): combinación de lo ya probado; la continuidad de $I$ a través de colisiones es la del Cor 167-2.4 (auditada). (3) es la lectura de (1)–(2) + Prop 167-3.2 (la finitud como condición de frontera). $\square$

**Consecuencia conceptual (la corrección de rumbo de esta fase):** la "rigidez" del director NO es un problema de estabilidad forward — forward hay sobreestabilidad universal (extinción en tiempo finito, tasa cuantizada, sin coercividad que probar porque ya está). El problema es de **unicidad/clasificación backward del dato inicial**: qué condiciones iniciales son alcanzables por la aritmética. El resto del documento ataca eso.

---

## 2. El frente backward: despegues, el invariante que falta, y dónde entra la aritmética

### 2.1. Estado certificado del lado $t<0$

Lo único probado (post-auditoría 168): **condicional a** $\kappa<\infty$ y ceros simples c.t.p. en $(t,0)$,
$$I(t)\;\ge\;I(0^+)+4|t|,\qquad\text{y (Thm 174.2 leído backward, si además }M\le\bar M\text{ en }(t,0)\text{)}\quad I(t)\;\ge\;I(0^+)\,e^{2|t|/\bar M}.$$
La versión incondicional NO está probada (KILL parcial del Doc 168: el caso $I<\infty$, $\kappa=\infty$ en $(t,0)$ queda fuera del Thm 167-2.3). [RT] da $\kappa(t)>0$ para todo $t<0$; el lema regalo da $\kappa(t)\ge2$.

### 2.2. La estructura de los despegues: el modelo cerrado invertido y el punto fijo de red

**[CÁLCULO 174.6] (tiempo de despegue del par aislado).** Tiempo-reverso del modelo de par: un par de ceros reales con gap $g$ en $t=0$, aislado, proviene de un par complejo que aterrizó en $t_c=-g^2/8$: en $H=z^2+c_0-2t$ con $c_0=-g^2/4$, los ceros son reales $\pm\sqrt{2t+g^2/4}$ para $t>-g^2/8$ y complejos antes. **Backward, los despegues ocurren en los gaps pequeños con tiempo de despegue $\asymp g^2$** — la forma normal de pliegue (Prop 167-1.6/2.6) leída hacia atrás. [CSV] es la versión aritmética rigurosa de esto en $t=0$: un par de Lehmer (casi-colisión) fuerza $\Lambda\ge$ cota — i.e. *despegue reciente*.

**[PROP 174.7] (la red perfecta es un punto fijo: la densidad NO compra despegues).** $H(z)=\cos z$ evoluciona como $H_t=e^{t}\cos z$: los ceros no se mueven y $\kappa(t)\equiv0$ para **todo** $t\in\mathbb R$, backward incluido.

*Prueba.* $\partial_t(e^t\cos z)=e^t\cos z=-\partial_z^2(e^t\cos z)$. Equivalente desde las partículas: en la red $\{\pi(k+\tfrac12)\}$ la suma simetrizada $\sum'1/(x_k-x_j)$ se cancela por simetría: $\dot x_k=0$. $\square$

**Lectura — el puente aritmético, localizado con precisión.** Una configuración con densidad RvM pero gaps *perfectamente regulares* nunca despega: backward puede vivir real para siempre. Los despegues backward se compran exclusivamente con **fluctuaciones de gaps**. Para ζ, las fluctuaciones son un hecho incondicional (momentos gaussianos de $S(t)$, Selberg 1946 — bloques con exceso de ceros existen, luego gaps estrictamente menores que la media infinitas veces), y su estadística fina (densidad $\sim\delta^3$ de gaps normalizados $\le\delta$) es la predicción GUE, condicional ([M73]); la existencia de infinitos pares de Lehmer es abierta. **Aquí es donde la aritmética entra al flujo backward: por la estadística de gaps de los $\gamma$, no por los primos directamente** — exactamente como anticipaba el mandato, y ahora con el mecanismo aislado (Prop 174.7: sin fluctuación, sin despegue).

**[GAP-174.C] (el dual backward de KKL).** ¿Es $\kappa(t)=\infty$ para todo $t<0$ (para ζ, o bajo RH)? Heurística a favor: a tiempo $|t|$ fijo, el umbral de despegue $g\lesssim\sqrt{8|t|}$ es *absoluto* mientras el gap medio $4\pi/\log\gamma\to0$: a altura suficiente, gaps típicos quedan bajo el umbral. En contra: la Prop 174.7 muestra que el argumento de densidad media es **falaz** (la red no despega: el modelo de par aislado no aplica en régimen denso, donde la repulsión colectiva puede sostener la realidad). El enunciado es genuinamente abierto y es la pregunta estructural correcta sobre el semieje $t<0$: si $\kappa(t)=\infty$ para $t<0$, entonces la cota condicional $I(t)\ge4|t|$ es vacua (con $I(t)=\infty$) y toda la información backward es **local** (por ventanas). Forma decidible más débil: ¿$\kappa(t)\to\infty$ cuando $t\to-\infty$?

### 2.3. El invariante separador: lo que hay, y el enunciado exacto de lo que falta

**Qué distingue backward a RH ($I(0)=0$) de ¬RH con $0<I(0)<\infty$:**

**(a) El invariante monótono que SÍ existe.** Por el Lema 174.3, $\mathfrak B(t):=M(t)+2t$ es no-creciente forward, i.e. **backward $M(t)\ge M(0)+2|t|$**: la altura máxima crece al menos linealmente con pendiente 2 universal. Separación parcial: en el escenario ¬RH-finito, $M(t)\ge b_{\max}^2+2|t|$; bajo RH solo se garantiza $M(t)\ge2|t|$ — el escenario ¬RH lleva un **excedente aditivo $b_{\max}^2$** persistente. Esto es un invariante de comparación genuino pero unilateral: para separar haría falta la cota **superior** bajo RH, y ésa falla:

**(b) Por qué la cota superior falla tal cual (el cálculo del cluster).** Backward, un despegue desde un cluster de $k$ casi-colisiones simultáneas en una ventana $\ll\beta$ crece como $\dot\beta\approx+k/\beta$ (los $k$ conjugados a distancia $\approx2\beta$ suman), i.e. $\beta^2\approx2k|t-t_c|$: la pendiente local de despegue es $2k$, no $2$, con $k$ no acotado para ζ (la multiplicidad de casi-colisión en ventanas de tamaño $\sqrt{|t|}$ crece con la altura por RvM). Una cota $M(t)\le2|t|(1+o(1))$ bajo RH es falsa sin control de clusters.

**[GAP-174.B] (el lema separador que falta — enunciado preciso).** *Sea $Z_0$ una configuración real (RH) en la clase, con densidad RvM y función de concentración de gaps $\nu(\delta,T):=\#\{n\le N(T):g_n\le\delta\}$. ¿Existe $F$, dependiente solo de $\nu$, tal que para $t<0$ (donde la dinámica esté definida) toda componente compleja a tiempo $t$ con progenitor en la ventana $W$ satisface $\beta(t)^2\le F\bigl(|t|,\;\#\{\text{casi-colisiones de }Z_0\text{ en }W\text{ a escala }\sqrt{8|t|}\}\bigr)$, con $F(|t|,k)=2k|t|(1+o(1))$?* Si tal cota vale, el escenario $0<I(0)<\infty$ es backward-detectable como **par huérfano**: a tiempos $|t|\ll b_{\max}^2/(2k_{\rm loc})$, el cuádruplo heredado tiene altura inalcanzable desde cualquier censo local de progenitores (gaps pequeños de la configuración a tiempo $0^+$ tras su aterrizaje). [DEFINICIÓN-NUEva: **par huérfano** = par complejo a tiempo $t<0$ cuya trayectoria forward no aterriza en $(t,0]$; ¬RH con $I<\infty$ ⟺ existen huérfanos a todo $t<0$ pequeño; RH ⟺ todo par backward tiene progenitor (gap) localizado con $g\lesssim\sqrt{8|t|}\cdot\sqrt{k}$.]

**(c) El veredicto honesto sobre la separación: el muro tasa/total reaparece, ahora dinámico.** El flujo es determinista en ambas direcciones (en la clase, los ceros de $H_t$ determinan $H_t$ módulo normalización, y el flujo es invertible mientras la dinámica esté definida): **el backward no añade información — transporta la dicotomía inicial.** Cualquier "invariante backward computable que separe" computa, en $t\to0^-$, exactamente $I(0)$ — y eso es el muro "momento firmado → momento cuadrático" (Doc 167 §5.1) en otra carta. Más fino: lo que el backward sí reorganiza es *quién porta la información*: la **tasa** de crecimiento backward (despegues, pendientes $2k$) está gobernada por la estadística de gaps — certificable en promedio, envolvente tipo Doc 170 — mientras el **total** (el excedente aditivo $b_{\max}^2$, los huérfanos) es exactamente la parte no separable por promedios (Thm 170.8). La dicotomía tasa/total del Doc 170 (Coordenada 2) no era un artefacto de la fórmula explícita: **es una propiedad del flujo.** Lo que sobrevive como programa: el GAP-174.B es un enunciado de dinámica de partículas puro (sin ζ), decidible en principio, y su mitad aritmética (el censo de progenitores de ζ) es estadística de gaps — el objeto correcto para Phase 56.

---

## 3. El presupuesto de colisiones (B3): el teorema del presupuesto y la refutación de la soldadura

### 3.1. El presupuesto exacto

**[TEOREMA 174.8] (presupuesto de vidas).** Supóngase $I(0^+)<\infty$. Sea $\{t_j\}$ el multiconjunto de tiempos de aterrizaje de los cuádruplos en $(0,\Lambda]$ y $\ell_j\le t_j$ la vida (medida de Lebesgue del conjunto de tiempos $>0$ en que el cuádruplo $j$ está off). Entonces
$$\sum_j \ell_j\;=\;\tfrac12\int_0^\Lambda\kappa(t)\,dt\;\le\;\tfrac14\,I(0^+)\;<\;\infty.$$
En particular $I(0^+)<\infty\Rightarrow$ las vidas son $\ell^1$; y la integrabilidad de $\kappa$ en $0^+$ (Prop 167-3.2.2) es la sumabilidad de las vidas. Recíproco falso a priori: $\int\kappa<\infty$ no controla $\int D$.

*Prueba.* $\kappa(t)=\sum_j2\cdot\mathbf 1_{\{j\text{ off en }t\}}$ (cada cuádruplo = 2 modos superiores), luego $\int_0^\Lambda\kappa=2\sum_j\ell_j$. Integrando la ley de balance en $(\varepsilon,\Lambda)$ (válida c.t.p. por [KKL] + finitud local de colisiones, reparación 5 del 168; $I$ continua en colisiones): $I(\varepsilon)=\int_\varepsilon^\Lambda(2\kappa+D)\ge2\int_\varepsilon^\Lambda\kappa$; convergencia monótona en $\varepsilon\to0^+$. $\square$

**Lectura de las dos flechas en una sola moneda:** la flecha "$m<\infty$" es $\kappa\in L^\infty(0^+)$; la flecha "$I(0^+)<\infty$" (GAP 167.A) es $\kappa\in L^1(0^+)$ ⟺ vidas sumables. El presupuesto convierte la energía $\ell^2$ de las alturas en presupuesto $\ell^1$ de tiempos — la moneda de cambio es el exponente Lehmer 2 ($\ell_j\asymp\beta_j^2$, Thm 174.4).

### 3.2. Interferencia de cuádruplos sub-resolución: NO hay auto-obstrucción

**[CÁLCULO 174.9] (el cluster $\ell^2$ colapsa más rápido, no más lento).** $k$ cuádruplos a alturas $\beta_i\approx b$ con separaciones horizontales $w\ll b$ (cluster sub-resolución): para cada cero, los $k$ conjugados (propio + vecinos) están a distancia $\approx2b$ y suman
$$\dot\beta\;\approx\;-\frac{1}{\beta}-\;(k-1)\cdot\frac{2b}{4b^2}\;\approx\;-\frac{k+1}{2b}\quad\Rightarrow\quad \frac{d(b^2)}{dt}\approx-(k+1),\qquad t_{\rm aterrizaje}\approx\frac{b^2}{k+1}.$$
Los términos $(\beta_k-\beta_l)$ entre miembros del cluster son $\approx0$ (alturas iguales) y la repulsión horizontal ($\dot\alpha\sim k/w$) dispersa el cluster sin singularidad: las velocidades son finitas mientras los ceros sean distintos, y las únicas colisiones forward son aterrizajes (las colisiones real–real están excluidas por repulsión: $\dot g=4/g+O(1)>0$ para el gap mínimo). **Conclusión: la acumulación infinita de cuádruplos sub-resolución es dinámicamente consistente** — el cluster acelera su propio aterrizaje (factor $k+1$), holgura adicional en el presupuesto del Thm 174.8, ninguna velocidad infinita, ningún colapso prohibido.

### 3.3. [REFUTACIÓN] "$I<\infty\Rightarrow m<\infty$" es FALSA en la clase — la soldadura dinámica de las dos flechas no existe

El candidato del mandato ("si encuentras una contradicción dinámica para $m=\infty\wedge I<\infty$, habrás probado $I<\infty\Rightarrow m<\infty$") queda **refutado en la clase de Pólya, con contraejemplo**: la configuración de Hadamard del Doc 144 (versión reparada del Doc 168 §5.1, con ceros reales en los puntos RvM exactos y cuádruplos en $\gamma_j=2^j$, $b_j=e^{-\gamma_j}$) tiene $m=\infty$, $I=\sum b_j^2<\infty$, pertenece a $\mathcal C$, **y entra al flujo DBN** (el semigrupo $e^{-t\partial_z^2}$ actúa en orden $<2$). Su dinámica es la del Cálculo 174.9 con clusters triviales ($k=1$, separaciones súper-exponenciales): perfectamente regular, vidas $\ell_j\approx b_j^2/2$ sumabilísimas, presupuesto del Thm 174.8 satisfecho con holgura infinita. **No existe obstrucción dinámica de clase: toda prueba de $I<\infty\Rightarrow m<\infty$ — si la implicación es siquiera verdadera para ζ — debe usar input aritmético más allá de la densidad RvM.** Esto cierra (negativamente, con prueba) la idea B3 en su versión fuerte; lo que la sustituye es el Teorema 174.8 (presupuesto, verdadero e incondicional en su dominio) y la reformulación: las dos flechas no se sueldan en la dinámica; se sueldan — si se sueldan — en la condición inicial (consistente con el dato estructural clave del §0 y con Doc 167 §4c: la finitud es Fredholm, no dinámica).

---

## 4. El sistema de momentos (B1): la jerarquía cerrada hacia abajo

### 4.1. La jerarquía completa

**[TEOREMA 174.10] (jerarquía de momentos pares).** Sea $I_{2n}(t):=\sum_{k\,\rm sup}\beta_k(t)^{2n}$, $n\ge1$ ($I_2=I$). En intervalos con $\kappa<\infty$ y ceros simples:
$$\dot I_{2n}\;=\;-2n\,I_{2n-2}\;-\;D_{2n},\qquad D_{2n}\ge0\ \text{término a término},\qquad(I_0:=\kappa).$$

*Prueba.* $\dot I_{2n}=\sum_k2n\beta_k^{2n-1}\dot\beta_k=-4n\sum_k\sum_{w\ne z_k}\beta_k^{2n-1}\frac{\beta_k-\operatorname{Im}w}{|z_k-w|^2}$. Conjugado propio: $\beta_k^{2n-1}\cdot2\beta_k/4\beta_k^2=\beta_k^{2n-2}/2$, contribución $-2n\beta_k^{2n-2}$ por modo: total $-2n\,I_{2n-2}$. Espejo: $0$. Antípoda y ceros reales: $\le0$. Cruzados, simetrizando $(k,l)+(l,k)$ sobre el mismo denominador (la coincidencia exacta de denominadores del Doc 168 §2.5): $\beta_k^{2n-1}(\beta_k-\beta_l)+\beta_l^{2n-1}(\beta_l-\beta_k)=(\beta_k-\beta_l)(\beta_k^{2n-1}-\beta_l^{2n-1})\ge0$ (factores del mismo signo), y $(\beta_k+\beta_l)(\beta_k^{2n-1}+\beta_l^{2n-1})\ge0$. $\square$

**Verificación en el modelo cerrado:** par aislado $\beta^2=\beta_0^2-2t$: $I_{2n}=(\beta_0^2-2t)^n$, $\dot I_{2n}=-2n(\beta_0^2-2t)^{n-1}=-2nI_{2n-2}$ exacto, $D_{2n}=0$ — la cascada libre se realiza con igualdad.

### 4.2. Corolarios: la familia virial que interpola energía y banda

**[COR 174.11].** En $(t_0,\Lambda)$, con $\kappa\ge2$ (paridad + lema regalo):
1. *(decaimiento acelerado de los momentos altos)* $I_{2n-2}\ge I_{2n}/M\ge I_{2n}$ ⟹ $\dot I_{2n}\le-2n\,I_{2n}$ ⟹ $I_{2n}(t)\le I_{2n}(t_0)e^{-2n(t-t_0)}$: **el perfil $\{\beta_k\}$ se aplana en toda norma $\ell^{2n}$ con tasa $2n$** — la nube pierde primero sus alturas grandes.
2. *(familia virial)* Por media de potencias, $I_{2n-2}\ge\kappa^{1/n}I_{2n}^{(n-1)/n}\ge2^{1/n}I_{2n}^{(n-1)/n}$, luego $\dot I_{2n}\le-2n\,2^{1/n}I_{2n}^{(n-1)/n}$ e integrando:
$$\Lambda\;\le\;t_0+\frac{I_{2n}(t_0)^{1/n}}{2^{1+1/n}}\qquad\text{para todo }n\ge1.$$
$n=1$ recupera $\Lambda\le t_0+I/4$ (Cor 167-2.4 reparado); $n\to\infty$ recupera $\Lambda\le t_0+M/2$ (banda de de Bruijn, Lema 174.3): **la jerarquía interpola exactamente entre el virial de energía y el teorema de banda — son los extremos $n=1$ y $n=\infty$ de una sola familia.**

*Prueba.* (1): $M<1$. (2): $(I_{2n}/\kappa)^{1/n}\le(I_{2n-2}/\kappa)^{1/(n-1)}$ (monotonía de medias de potencias) da la forma usada tras reordenar; la EDO $u'\le-cu^{(n-1)/n}$ da $u^{1/n}$ decreciente a tasa $c/n$, extinción en $nu_0^{1/n}/c$ con $c=2n\cdot2^{1/n}$. $\square$

### 4.3. La entropía (condicional a pequeñez) y el momento ponderado (no cerrado)

**[PROP 174.12] (entropía).** $S(t):=\sum_k\beta_k^2\log(1/\beta_k)$. Si $\sup_k\beta_k\le e^{-3/2}$ en el intervalo, entonces
$$\dot S\;\le\;-2\sum_k\log\frac1{\beta_k}\;+\;\kappa\;\le\;-\kappa\Bigl(\log\frac1{M}-1\Bigr).$$
*Prueba.* $\dot S=\sum\varphi(\beta_k)\dot\beta_k$ con $\varphi(\beta)=2\beta\log(1/\beta)-\beta$. Conjugado propio ($\dot\beta\ni-1/\beta$): $-\sum(2\log(1/\beta_k)-1)$. Los demás términos son $\le0$ si $\varphi\ge0$ (⟸ $\beta\le e^{-1/2}$) y $\varphi$ creciente (⟸ $\varphi'=2\log(1/\beta)-3\ge0$ ⟸ $\beta\le e^{-3/2}$): mismos signos y simetrizaciones que el Thm 174.10 con peso monótono. $\square$
**Uso:** cerca de la extinción ($M\to0$) la entropía disipa a tasa $\kappa\log(1/M)\gg\kappa$: $S$ es el funcional que "ve" la sub-resolución ($\log(1/\beta)\sim\log\log\gamma$ en la escala LP-134) — backward, $S$ crece súper-linealmente respecto de $I$: candidato a peso para el censo de progenitores de §2.3.

**[CÁLCULO 174.13] ($\langle\alpha^2\beta^2\rangle$ no se cierra; valor exacto en el modelo).** $J:=\sum_k\alpha_k^2\beta_k^2$ satisface $\dot J=-2\sum_k\alpha_k^2+(\text{transporte }2\alpha_k\dot\alpha_k\beta_k^2)+(\dots)$, y el transporte involucra $\dot\alpha_k$ (condicionalmente convergente, sin signo): **el sistema no se cierra en momentos verticales puros** — la obstrucción es el flujo horizontal (la expansión del gas: en el cuádruplo cerrado, $d(\alpha^2-\beta^2)/dt=6$, $d(\alpha^2)/dt=4-2\beta^2/|z|^2>0$). En el cuádruplo aislado, exacto: $\alpha^2\beta^2=(\operatorname{Im}w)^2/4$ ⟹ $\boxed{d(\alpha^2\beta^2)/dt=-2(\alpha^2-\beta^2)}$ (Thm 174.4). [GAP-174.D: cerrar $J$ requiere acoplar con el primer momento horizontal del gas real; no lo perseguimos — el contenido de Fase C accesible está en la jerarquía vertical.]

### 4.4. Fase C (clasificación de perfiles): qué dice el sistema de momentos

De la jerarquía + presupuesto: un perfil inicial $\{(\gamma_j,b_j)\}$ es dinámicamente consistente sii (es decir: la dinámica NO clasifica más allá de) — vidas sumables si $I<\infty$ (Thm 174.8), decaimiento $\ell^{2n}$ ordenado (Cor 174.11.1), sin equilibrios con $\kappa>0$ ($\dot I<0$ estricta: **no hay estados estacionarios off-line, ni siquiera metaestables** — la des-excitación es incondicional). Todo lo demás (qué perfiles realiza ζ) es condición inicial: la clasificación de Fase C es aritmética o no es. Con la estadística de gaps real (RvM + fluctuaciones de Selberg) el único acoplamiento probado es el del §2: los perfiles backward-alcanzables desde RH tienen todos sus pares con progenitor; el perfil ¬RH-finito es exactamente el que tiene huérfanos.

---

## 5. Test anti-circularidad

| Objeto | ¿RH-libre? | ¿ζ-libre? | Dónde reentra ζ |
|---|---|---|---|
| Prop 174.1 (no-coercividad), Thm 174.4 (modelo cerrado, $t_c$ exacto) | sí | sí | no reentra |
| Lema 174.3 (máximo), Thm 174.2 (coercividad $\dot I\le-2I$), Thm 174.5 (forward) | sí | sí (clase + [KKL] para el ancla $t_0>0$) | no reentra |
| Thm 174.8 (presupuesto), Thm 174.10 + Cor 174.11 (jerarquía), Prop 174.12 | sí | sí | no reentra |
| Prop 174.7 (red = punto fijo) y Cálculo 174.6 (despegue $-g^2/8$) | sí | sí | no reentra; fija DÓNDE entraría ζ |
| §2.3 separación backward, huérfanos, GAP-174.B | sí | **no** en su mitad aritmética | ζ entra por estadística de gaps ([S46] incondicional; GUE condicional) |
| §3.3 refutación de la soldadura | sí | sí (contraejemplo de clase) | la implicación para ζ queda abierta, no refutada |

Patrón confirmado y afinado respecto del Doc 167: la LEY (ahora: toda la jerarquía, el presupuesto, el máximo) es ζ-libre; la aritmética tiene **un único punto de entrada dinámico identificado: las fluctuaciones de gaps** (Prop 174.7 lo aísla: sin fluctuación no hay despegue). No hay primos en ninguna prueba de este documento.

---

## 6. Veredicto

### Teoremas nuevos
- **[TEOREMA 174.10 + COR 174.11] (jerarquía de momentos):** $\dot I_{2n}=-2nI_{2n-2}-D_{2n}$, $D_{2n}\ge0$, para todo $n\ge1$; decaimiento $e^{-2nt}$ por norma; familia virial $\Lambda\le t_0+I_{2n}^{1/n}/2^{1+1/n}$ que **interpola exactamente entre el virial de energía ($n=1$) y la banda de de Bruijn ($n=\infty$)** — los dos resultados conocidos son los extremos de una sola familia. El mejor teorema del documento.
- **[TEOREMA 174.2 + LEMA 174.3] (B2 resuelta):** $D\ge cI$ es falsa (Prop 174.1, contraejemplo exacto $D/I=2/|z|^2$), pero $\dot I\le-2I/M\le-2I$: la coercividad exponencial existe con $L=I$, $c=2$, por cuantización + banda, no por disipación de interacción. Principio del máximo $D^+M\le-2$ (re-prueba dinámica del Thm 13 de de Bruijn).
- **[TEOREMA 174.8] (presupuesto):** $\sum_j\ell_j\le I(0^+)/4$ — las dos flechas son $\kappa\in L^\infty$ vs $\kappa\in L^1$ en $t\to0^+$, y la moneda de cambio vidas↔energía es el exponente Lehmer 2.
- **[TEOREMA 174.4/174.5] (forward cerrado):** solución exacta del cuádruplo, $t_c=\beta_0^2/2-\beta_0^4/4\alpha_0^2+O(\cdot)$ (respuesta al director: $\beta^2/2$, no $\beta^2/4$; $=I_0/4$ por cuádruplo); estructura forward: extinción universal con tasas explícitas — **la pregunta de RH vive enteramente en $t\le0$**.
- **[PROP 174.7] (punto fijo de red):** la densidad no compra despegues backward; el punto de entrada de la aritmética al flujo son las fluctuaciones de gaps, aislado con prueba.

### Refutaciones y cierres negativos (con prueba)
- **§3.3:** "$I<\infty\Rightarrow m<\infty$" es **falsa en la clase** (contraejemplo de Hadamard reparado, que fluye); la soldadura dinámica de las dos flechas del director no existe — B3 versión fuerte cerrada. Sin auto-obstrucción de clusters $\ell^2$ (Cálculo 174.9: aceleración $b^2/(k+1)$, no colapso prohibido).
- **§2.3(c):** ningún invariante backward computable separa los escenarios sin computar $I(0)$: el flujo backward transporta la dicotomía, no la amplifica selectivamente — **la dicotomía tasa/total del Doc 170 es una propiedad del flujo**, no de la fórmula explícita.

### [GAPs] declarados, con forma de enunciado
- **GAP-174.B (el central):** cota superior de despegue para configuraciones reales: $\beta(t)^2\le2k\,|t|(1+o(1))$ con $k$ = multiplicidad local de casi-colisión de la configuración inicial a escala $\sqrt{8|t|}$. Es un enunciado de dinámica de partículas puro (ζ-libre); con él, ¬RH-con-$I$-finito ⟺ existencia de **pares huérfanos** backward, y la mitad aritmética del puente queda reducida al censo de progenitores = estadística de gaps de ζ.
- **GAP-174.C:** ¿$\kappa(t)=\infty$ para todo $t<0$? (dual backward de KKL; la Prop 174.7 muestra que la densidad no lo decide).
- **GAP-174.D:** cierre del momento ponderado $J=\langle\alpha^2\beta^2\rangle$ (transporte horizontal; no perseguido).

### Referencias
de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226 (Thm 13: banda decreciente). — Newman, C.M. (1976), Proc. AMS 61, 245–251. — Csordas, G., Smith, W., Varga, R.S. (1994), *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10, 107–129. — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306. — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6 (§2: dinámica de ceros). — Polymath, D.H.J. (2019), Res. Math. Sci. 6, 31. — Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 (momentos de $S(t)$, incondicional). — Montgomery, H.L. (1973), Proc. Symp. Pure Math. 24 (correlación de pares, condicional a RH). — **[GAP de literatura]:** la conexión del flujo de ceros con Calogero–Moser racional es folklore (cf. exposiciones de Tao en torno a [RT]); no usamos ningún resultado de esa literatura. La jerarquía $\dot I_{2n}=-2nI_{2n-2}-D_{2n}$ y el presupuesto $\sum\ell_j\le I/4$ no los conocemos enunciados en parte alguna. — Docs internos: 144, 167, 168, 170.
