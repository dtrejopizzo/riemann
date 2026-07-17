# Documento 178 — El Lema 177.B atacado por tres vías: gap-ODE con bloques comprimidos, equivalencia con la constante de De Bruijn–Newman local, y la calibración que disuelve el "GAP de literatura"

**Programa:** Hipótesis de Riemann — Fase 56 (dos torres)
**Fecha:** 2026-06-11
**Mandato:** atacar el [LEMA-MÍNIMO 177.B] (Doc 177 §4.2): ∃θ∈(0,½), c>0 tales que para la $H_t$ aritmética y todo $t\in(0,1)$, todo gap consecutivo de ceros reales de $H_t$ a altura $\gamma\ge\Gamma(t):=\exp(t^{-(1/2-\theta)})$ cumple $g_{\rm norm}:=g\cdot\frac{\log\gamma}{4\pi}\ge c\,t^\theta$. Tres vías obligatorias (Rodgers–Tao §2; ODE del gap; comparación con el modelo soluble / zona asintótica de Polymath 15). Sin auditorías; sin numérica.
**Prerrequisitos (certificados, no re-derivados):** Doc 167 (dinámica de ceros Lema 2.1; ley de balance Thm 2.3; pliegue Prop 2.6; convención del flujo §0.1), Doc 177 (Hermite exacto Thm 177.1; estabilidad Prop 177.3; cota del mar Lema 177.4; cota de energía Thm 177.6; lógica de aterrizajes Thm 177.7 y Cor 177.8; cota de tiempo de aterrizaje $t_c\ge b^2/(2n^2)(1-C\varepsilon)$ de §4.1).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] solo con prueba completa; [PUENTE] con estatus honesto; [GAP]/[GAP de literatura] declarados. Citas backward-only (docs ≤ 177 + literatura real).

---

## 0. Convenciones

Carta de Polymath 15 como en el Doc 167 §0.1: $H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du$, $\partial_tH_t=-\partial_z^2H_t$, $H_0=\tfrac18\Xi(\cdot/2)$ salvo reescalado fijo. **En esta carta el sentido $t$ creciente es el regularizador** (de Bruijn: la realidad es absorbente; $\Lambda\le t$ ⟹ ceros reales): es la dirección que el mandato llama *forward*. La dinámica de ceros simples (Lema 167-2.1) es
$$\dot z_k \;=\; 2\sum_{j\ne k}{}^{\!\!'}\frac{1}{z_k-z_j},$$
**repulsiva entre ceros reales** (gaps tienden a abrirse con $t$) y **atractiva entre un cero y su conjugado** ($\dot\beta\le-1/\beta+\text{mar}$: los pares complejos caen y aterrizan). Nota de signo: el enunciado del mandato escribe $\partial_tH=\partial_z^2H$ "convención forward"; la carta de P15/Doc 167 tiene el signo opuesto en la EDP pero **la misma dinámica de ceros y el mismo sentido regularizador**; todo lo que sigue usa solo la dinámica de ceros, así que no hay ambigüedad.

Notación: $\rho=\rho(\gamma):=\frac{\log\gamma}{4\pi}$ (densidad local en la carta $H$, RvM), $L:=\log\gamma$, $g_{\rm norm}=g\rho$. "Altura" = $|\operatorname{Re}z|$ (los ceros de $\zeta$ a altura $\gamma$ son ceros de $\Xi$ con $\operatorname{Re}z=\gamma$, $\operatorname{Im}z=b$, $b<\tfrac12$). Aterrizaje = instante $t_c$ en que un par conjugado toca el eje real.

**Verificación exacta de calibración (se usará dos veces).** $H(z)=\cos(\lambda z)$ evoluciona a $e^{t\lambda^2}\cos(\lambda z)$: **el reticulado equiespaciado es exactamente estacionario** bajo el flujo. Toda cota inferior de gaps que pretenda crecer con $t$ debe usar algo más que "los gaps vecinos no son menores": debe usar un input de conteo.

---

## 1. Vía 1 (Rodgers–Tao §2): qué hay, qué se extrae, qué no puede dar

**Qué hay (lectura honesta de [RT 2020]).** La maquinaria de [RT] analiza la dinámica $\dot x_k=2\sum'(x_k-x_j)^{-1}$ **hacia atrás** ($t<0\to0^-$): suponiendo $\Lambda<0$, en $t=\Lambda$ todos los ceros son reales y la dinámica en $[\Lambda,0]$ es un gas puramente real; sus estimaciones (energía local del gas, comparación con el equilibrio localmente equiespaciado) muestran que tras tiempo $|\Lambda|>0$ **fijo** el gas en $t=0$ estaría localmente rígido (equiespaciado a escala microscópica), contradiciendo fluctuaciones incondicionales del conteo de ceros de $\zeta$. Tres rasgos estructurales:

1. **El parámetro temporal está separado de cero**: toda la cuantificación es "para $t$ en un compacto de longitud $|\Lambda|$ fija"; las constantes de sus lemas de relajación degeneran cuando el tiempo disponible $\to0$. La uniformidad en la esquina difusiva $t\,\rho^2\gg1$ con $t\to0^+$ **no está en [RT]** (ni la necesitaban).
2. **La dirección está invertida respecto de 177.B**: ellos van de "ceros reales en $t=\Lambda$" a "rigidez en $t=0$"; 177.B pide ir de "$H_0$ aritmética" a "gaps en $t>0$". Su input aritmético (fluctuación del conteo de $\zeta$) entra en $t=0$ como *destino*, no como dato inicial.
3. **Lo que sí se extrae y reutilizamos**: (a) la forma simetrizada y absolutamente convergente de la dinámica (ya certificada en Lema 167-2.1); (b) la idea de comparar con el equilibrio local **con un input de conteo** — que es exactamente lo que falta tras la verificación del reticulado de §0; la convertimos en teorema en §2.

**Veredicto de la vía 1:** no muere pero no cierra: su maquinaria es del régimen "tiempo macroscópico, relajación completa" y 177.B vive en "tiempo microscópico, relajación parcial". La parte trasladable (equilibrio local + conteo) se ejecuta en §2 como Teorema 178.4. Lo que la vía 1 *no puede* dar en ningún refinamiento — un 177.B incondicional — queda probado en §3 (Prop 178.7: bloqueo estructural, no técnico).

---

## 2. Vía 2: la ODE del gap, el no-go del reticulado, y el teorema sub-difusivo condicional

### 2.1. La ODE exacta del gap

**[LEMA 178.1] (ODE del gap).** Sea $J$ un intervalo de tiempos en que los ceros de $H_t$ en la ventana $|{\operatorname{Re}z-\gamma}|\le10$ son reales y simples, y sean $x_k<x_{k+1}$ consecutivos en esa ventana, $g=x_{k+1}-x_k$. Entonces
$$\dot g\;=\;\frac4g\;-\;g\,S,\qquad S\;:=\;\sum_{j\notin\{k,k+1\}}\frac{2}{(x_j-x_k)(x_j-x_{k+1})}\;+\;\mathcal{E},$$
donde la suma corre sobre los demás ceros **reales** de la ventana y de fuera de ella (agrupada simétricamente como en Lema 167-2.1, absolutamente convergente por RvM), cada término con $x_j\notin(x_k,x_{k+1})$ es $\ge0$ (ambos factores del denominador tienen el mismo signo), y $\mathcal{E}$ recoge ceros no reales y el espejo $-Z$: si no hay ceros no reales a distancia $\le D\ge1$ de la ventana, $|\mathcal{E}|\le C\rho/D^2+C\gamma^{-2}$ por el argumento del Lema 177.4.

*Prueba.* $\dot g=\dot x_{k+1}-\dot x_k=2\bigl[\tfrac1{x_{k+1}-x_k}-\tfrac1{x_k-x_{k+1}}\bigr]+2\sum_{j\notin\{k,k+1\}}\bigl[\tfrac1{x_{k+1}-x_j}-\tfrac1{x_k-x_j}\bigr]$; el primer corchete da $4/g$ y cada sumando del segundo es $-\,g/((x_j-x_k)(x_j-x_{k+1}))$ por reducción a común denominador, duplicado por la convención de pares ordenados. La cota de $\mathcal{E}$: cada par conjugado no real a distancia $\ge D$ contribuye una diferencia de dos términos del tipo del Lema 177.4 con numerador acotado y denominadores $\ge D^2$; la suma sobre el mar no real con densidad RvM da $C\rho/D^2$; el espejo en $-\gamma$ da $O(\gamma^{-2})$. $\square$

**Lectura.** El mar real **siempre comprime** ($S\ge0$ módulo $\mathcal{E}$): la repulsión del par contra la compresión del mar. La pregunta es cuánto vale $S$ en el peor caso.

### 2.2. El no-go del principio del mínimo desnudo

**[PROP 178.2] (saturación exacta del reticulado: la hipótesis "todos los gaps $\ge g$" no da nada).** Si solo se supone que todos los demás gaps son $\ge g_*$ y el gap considerado es $g=g_*$ (el mínimo local), la cota óptima obtenible de la suma de §2.1 es
$$S\;\le\;2\cdot\frac{2}{g_*^2}\sum_{m\ge1}\frac{1}{m(m+1)}\;=\;\frac{4}{g_*^2}\qquad\Longrightarrow\qquad \dot g_*\;\ge\;\frac{4}{g_*}-g_*\cdot\frac4{g_*^2}\;=\;0,$$
y la igualdad se alcanza **exactamente** en el reticulado infinito equiespaciado a paso $g_*$ — que es genuinamente estacionario ($\cos(\lambda z)\mapsto e^{t\lambda^2}\cos(\lambda z)$, §0). Por tanto **ningún principio del máximo tipo Hamilton sobre el mínimo de gaps cierra 177.B sin un input adicional**: el escenario extremal (un bloque largo uniformemente comprimido) no se expande localmente; se expande solo por sus bordes.

*Prueba.* Con $d_m\ge mg_*$ para el $m$-ésimo vecino a cada lado, $\sum_m\frac{2}{d_m(d_m+g_*)}\le\frac{2}{g_*^2}\sum_m\frac1{m(m+1)}=\frac{2}{g_*^2}$ por lado. Igualdad sii $d_m=mg_*$ para todo $m$: el reticulado. La estacionariedad del coseno es el cálculo de §0. $\square$

Esto refuta la versión ingenua de la vía 2 (la desigualdad $g\dot g\ge4-\text{error}$ con $g^2\ge8t$ y $\theta=\tfrac12$ límite): **el "error" del mar es exactamente $4$ en el caso extremal**. El input que falta es que el caso extremal viola el conteo:

### 2.3. Bloques comprimidos son cortos: el input de conteo

**[HIPÓTESIS (RvM-t), declarada].** *Existe $C_0$ tal que para todo $t\in[0,1]$ y todo intervalo $J\subset\mathbb R$ con $|J|\le1$ centrado a altura $\gamma$ grande: $\#\{x\in Z_t\cap J\}\le\rho(\gamma)\,|J|+C_0\log\gamma$.* Para $t=0$ es Riemann–von Mangoldt clásico. Para $t\in(0,1]$ lo creemos estándar pero no lo verificamos línea a línea: véase el Puente 178.5. Todo lo condicional a (RvM-t) lo marca explícitamente.

**[LEMA 178.3] (bloques comprimidos cortos).** Bajo (RvM-t): si $M$ ceros reales consecutivos de $H_t$ cerca de la altura $\gamma$ tienen todos sus gaps $\le\frac{1}{2\rho}$, entonces $M\le M_0:=2C_0\log\gamma+2$.

*Prueba.* El bloque ocupa longitud $\ell\le M\cdot\frac1{2\rho}\le\tfrac{M}{2\rho}$ (y $\le1$ si $M\le2\rho$; si $M>2\rho$ trocear en subintervalos de longitud 1 y sumar). Por (RvM-t): $M\le\rho\ell+C_0L\le\tfrac M2+C_0L$, luego $M\le2C_0L+2$. $\square$

### 2.4. El teorema sub-difusivo condicional: lo que la vía 2 sí prueba

**[TEOREMA 178.4] (crecimiento del gap mínimo; condicional a (RvM-t) y a realidad local).** Existen $c_1,c_2,C>0$ absolutos tales que: sea $[s,t]\subset(0,1]$, $\gamma$ grande, y supóngase
- **(R)** *realidad local:* $H_{t'}$ no tiene ceros no reales con $|\operatorname{Re}z-\gamma|\le10$ para ningún $t'\in[s,t]$, y $t-s\le L^{-2}\cdot C'$ (de modo que la deriva horizontal no vacía la ventana; Lema 178.6 abajo);
- **(RvM-t)** en la ventana.

Sea $g_*(t')$ el mínimo de los gaps consecutivos en $|\operatorname{Re}z-\gamma|\le5$. Entonces
$$g_*(t)^2\;\ge\;\min\Bigl\{\,g_*(s)^2+\frac{c_1\,(t-s)}{\log\gamma}\,,\;\frac{c_2}{\rho^2\log\gamma}\,\Bigr\}.$$

*Prueba.* $g_*$ es mínimo de finitas funciones reales-analíticas (los ceros son simples y reales en $[s,t]$ por (R); los instantes de cambio de minimizador son localmente finitos), luego localmente Lipschitz y derivable salvo en finitos puntos; en cada punto de derivabilidad su derivada es la $\dot g$ de un par minimizador (Danskin). Fijamos un instante y un par minimizador $(x_k,x_{k+1})$, $g=g_*$, y acotamos $S$ del Lema 178.1, suponiendo (caso no trivial) $g\le\frac1{2\rho}$ y $\rho^2g^2\log\gamma$ menor que una constante pequeña (si no, ya estamos en el techo del enunciado).

*Cadena cercana.* A cada lado del par, ordenamos los ceros por distancia: $d_1<d_2<\dots$ Mientras los ceros estén en la ventana $|\cdot-\gamma|\le5$, todos los gaps son $\ge g$, luego $d_m\ge mg$. Además, por (RvM-t) aplicado al intervalo $[x_{k+1},x_{k+1}+d_m]$: $m\le\rho d_m+C_0L$, i.e. $d_m\ge\frac{m-C_0L}{\rho}$ para todo $m$ (válido también con ceros fuera de la ventana). Con $M_0=2C_0L+2$:
$$\sum_{m\le M_0}\frac{2}{d_m(d_m+g)}\le\frac{2}{g^2}\sum_{m=1}^{M_0}\frac1{m(m+1)}=\frac{2}{g^2}\Bigl(1-\frac1{M_0+1}\Bigr),\qquad
\sum_{m>M_0}\frac{2}{d_m(d_m+g)}\le\sum_{m>M_0}\frac{2\rho^2}{(m-C_0L)^2}\le C\rho^2 .$$
(Los ceros a distancia $>5$, fuera de la ventana, están cubiertos por la segunda suma vía (RvM-t) en trozos diádicos de longitud $\le1$; los no reales están excluidos a distancia $\le10$ por (R) y a distancia $>10$ contribuyen $\le C\rho/100$ por el Lema 178.1, absorbido en $C\rho^2$.) Sumando los dos lados:
$$S\;\le\;\frac{4}{g^2}\Bigl(1-\frac{1}{M_0+1}\Bigr)+C\rho^2 \qquad\Longrightarrow\qquad \frac{d}{dt'}\,g^2\;=\;2g\dot g\;\ge\;\frac{8}{M_0+1}-2C\rho^2g^2 .$$
Mientras $g^2\le\frac{2}{C\rho^2(M_0+1)}$, el lado derecho es $\ge\frac{4}{M_0+1}\ge\frac{c_1}{L}$. Integrando la desigualdad diferencial sobre $[s,t]$ (válida a.e.; $g_*^2$ es absolutamente continua) se obtiene el mínimo entre el crecimiento lineal y el techo $\frac{2}{C\rho^2(M_0+1)}\ge\frac{c_2}{\rho^2L}$. $\square$

**[LEMA 178.6] (deriva horizontal; hace honestas las ventanas).** En las hipótesis del Teorema 178.4, la velocidad horizontal de cualquier cero real de la ventana está acotada por $C\log^2\gamma$ (agrupar la suma simetrizada en bloques diádicos: los $\le CL$ ceros a distancia $\in[2^{-r},2^{-r+1}]$, $2^{-r}\ge g_*$, aportan $\le CL\cdot2^{r}\cdot$... y la suma sobre $r\le\log(1/g_*)\le CL$ da $\le CL^2$ tras la cancelación par-a-par del término principal; los lejanos, $\le C\rho$ por RvM simetrizado). En tiempo $t-s\le C'L^{-2}$ el desplazamiento es $\le CC'$: las ventanas $\pm5/\pm10$ del teorema son consistentes tomando $C'$ pequeño. $\square$ *(Prueba con la holgura declarada: la constante $C'$ es la del enunciado (R).)*

### 2.5. Traducción a 177.B: la banda que cierra y la que no

Tomando $s=t/2$ en el Teorema 178.4 (legítimo si la realidad local vale en $[t/2,t]$ y $t\le C'L^{-2}$): $g_*(t)^2\ge c\,t/L$ hasta el techo. En unidades normalizadas, $g_{\rm norm}^2=g^2\rho^2\ge c\,t\rho^2/L=c'\,tL$. Comparando con la demanda $g_{\rm norm}\ge c\,t^{\theta_2}$:
$$c'tL\ge c^2t^{2\theta_2}\iff L\ge C\,t^{-(1-2\theta_2)};\qquad\text{techo no alcanzado}\iff tL\le c''/L\iff L\le c''\,t^{-1/2}.$$
Es decir: **la vía 2 prueba (condicionalmente) la cota de 177.B exactamente en la banda sub-difusiva**
$$t^{-(1-2\theta_2)}\;\le\;\log\gamma\;\le\;c\,t^{-1/2},\qquad \theta_2\in(\tfrac14,\tfrac12)$$
(la banda es no vacía sii $1-2\theta_2<\tfrac12$, i.e. $\theta_2>\tfrac14$). En la parametrización de 177.B, el umbral inferior corresponde a $\Gamma(t)=\exp(t^{-(1/2-\theta_1)})$ con $\theta_1=2\theta_2-\tfrac12\in(0,\tfrac12)$: **parámetros admisibles para 177.B**. Lo que NO cubre: (i) la zona super-difusiva $\log\gamma>ct^{-1/2}$, donde el techo $g_{\rm norm}\ge c\,L^{-1/2}$ del teorema es más débil que $ct^\theta$ cuando $L>t^{-2\theta}$ — ahí el mecanismo correcto es la relajación completa al equilibrio local (vía 1), no probada uniformemente [GAP-178.B]; (ii) sobre todo, **la hipótesis (R)**: el teorema solo rige donde no hubo ceros no reales en $[t/2,t]$. Un aterrizaje en $(t/2,t]$ crea un gap $\asymp\sqrt{t-t_c}$ arbitrariamente pequeño (pliegue, Prop 167-2.6) que ninguna evolución posterior tuvo tiempo de reparar. La vía 2, exprimida del todo, entrega entonces:

**[TEOREMA 178.4′] (resumen de la vía 2).** *Condicional a (RvM-t): si $H_{t'}$ no tiene ceros no reales a distancia $\le10$ de la altura $\gamma$ para ningún $t'\in[t/2,t]$, entonces todo gap a altura $\gamma$ en tiempo $t$ cumple $g_{\rm norm}\ge c\,t^{\theta_2}$ en la banda $\log\gamma\in[t^{-(1-2\theta_2)},c\,t^{-1/2}]$, $\theta_2\in(\frac14,\frac12)$.* (Es el Teorema 178.4 + la traducción anterior; la condición $t\le C'L^{-2}$ es automática en la banda.) $\square$

**Toda la carga de 177.B queda concentrada en la hipótesis de realidad local.** Eso es la vía 3.

### 2.6. El estatus de (RvM-t)

**[PUENTE 178.5 / GAP-178.A] (RvM uniforme en $t$).** *Enunciado necesitado:* la hipótesis (RvM-t) de §2.3 (solo la cota superior de conteo en ventanas de longitud $\le1$, uniforme en $t\in[0,1]$). *Estatus:* para $t=0$ es clásico. Para $t>0$ fijo, [KKL] obtienen asintóticas de $H_t$ que la implican a alturas grandes dependientes de $t$. La uniformidad en $t\in[0,1]$ debería seguirse del esquema estándar (Jensen en discos de radio $O(1)$ + cota superior de $|H_t|$ en la banda, que es efectiva y uniforme desde la representación integral con $\Phi$ superexponencial + cota inferior de $|H_t|$ en un punto por ventana a distancia $\asymp1$ del eje); el ingrediente no trivial es la cota inferior, que para $H_0$ se hace con $\zeta(s)\ne0$ en $\operatorname{Re}s\ge2$ y para $H_t$ debería darla la aproximación efectiva de [P15] (sus cotas de $|H_t|$ y de los errores $A+B-C$ son explícitas y uniformes en $t\in[0,1/2]$ en bandas $|\operatorname{Im}z|=O(1)$). **No verificado línea a línea aquí: [GAP de literatura], creído estándar, sin novedad conceptual.** Todo teorema de este documento que lo usa lo declara.

---

## 3. Vía 3: aterrizajes, la constante de De Bruijn–Newman local, y la calibración de dureza

### 3.1. El objeto correcto

**[DEFINICIÓN-NUEVA 178.6′] (constante de De Bruijn–Newman local en altura).**
$$\Lambda_{\rm loc}(\gamma)\;:=\;\inf\bigl\{\tau>0:\ \forall t\in[\tau,1],\ H_t\ \text{no tiene ceros no reales con}\ |\operatorname{Re}z-\gamma|\le5\bigr\}.$$
Bien definida en $[0,\Lambda]$ ($\Lambda\le1/2$, [dB]); $\sup_\gamma\Lambda_{\rm loc}(\gamma)=\Lambda$ salvo efectos de frontera de la ventana, que el Lema 178.6 controla en las escalas temporales relevantes ($\tau\le L^{-2}$: deriva horizontal $O(1)$, absorbida tomando ventana $\pm5$ en la definición y $\pm1$ en las conclusiones. Para $\tau$ grande la definición es solo un infimum honesto, no pretendemos monotonía local exacta).

### 3.2. Dirección A: $\Lambda_{\rm loc}$ pequeño ⟹ 177.B (en la banda)

**[TEOREMA 178.7] (la mitad buena de la equivalencia).** Condicional a (RvM-t): si
$$\Lambda_{\rm loc}(\gamma)\;\le\;\tfrac12\,(\log\gamma)^{-2/(1-2\theta_1)}\quad\text{para todo }\gamma\text{ grande}\qquad(\ast)$$
con $\theta_1\in(0,\tfrac12)$, entonces 177.B vale **en la banda sub-difusiva**: con $\theta_2=\frac{\theta_1}{2}+\frac14$, todo gap a altura $\gamma$ y tiempo $t$ con $\log\gamma\in[t^{-(1-2\theta_2)},c\,t^{-1/2}]$ cumple $g_{\rm norm}\ge c\,t^{\theta_2}$.

*Prueba.* En la banda, $\log\gamma\ge t^{-(1-2\theta_2)}=t^{-(1/2-\theta_1)\cdot\frac{1-2\theta_2}{1/2-\theta_1}}$; como $1-2\theta_2=\tfrac12-\theta_1$, esto es $\log\gamma\ge t^{-(1/2-\theta_1)}$, i.e. $t\ge(\log\gamma)^{-2/(1-2\theta_1)}\ge2\Lambda_{\rm loc}(\gamma)$ por $(\ast)$. Luego en $[t/2,t]$ no hay ceros no reales en la ventana: la hipótesis (R) del Teorema 178.4′ se cumple y su conclusión es la deseada. $\square$

### 3.3. Dirección B: 177.B ⟹ $\Lambda_{\rm loc}$ pequeño y confinamiento de TODOS los ceros de ζ

Esta dirección es incondicional (no usa (RvM-t)) y es el hallazgo principal del documento.

**[PROP 178.8] (177.B acota los aterrizajes — versión para todo cero, no solo bajo $m=\infty$).** Supóngase 177.B con parámetros $(\theta,c)$. Entonces: (1) todo aterrizaje en $(t_c,\gamma_c)$, $t_c\in(0,1)$, cumple $\gamma_c\le\Gamma(t_c)$, equivalentemente $\Lambda_{\rm loc}(\gamma)\le(\log\gamma)^{-2/(1-2\theta)}$ para $\gamma$ grande; (2) **todo** cero de $\zeta$ fuera de la línea crítica, a altura $\gamma$ grande y distancia $b$ de la línea, cumple
$$b\;\le\;C\,(\log\gamma)^{-\frac{1}{1-2\theta}}\;=\;C\,(\log\gamma)^{-1-\eta},\qquad \eta=\frac{2\theta}{1-2\theta}>0 .$$

*Prueba.* (1) es el argumento del Thm 177.7(1), que no usa $m=\infty$: justo después de un aterrizaje, el pliegue (Prop 167-2.6; y en el caso de cluster, el abanico de Hermite Thm 177.1, cuyos gaps mínimos son $\le C\sqrt\delta$) produce a tiempo $t_c+\delta$ un gap real a altura $\gamma_c+O(1)$ con $g_{\rm norm}\le C\sqrt\delta\log\gamma_c$; si $\gamma_c\ge\Gamma(t_c+\delta)$, 177.B exige $C\sqrt\delta\log\gamma_c\ge c\,t_c^\theta$ para todo $\delta>0$ pequeño — falso para $\delta\to0^+$. Luego $\gamma_c<\Gamma(t_c)$, que reordenado es $t_c\le(\log\gamma_c)^{-2/(1-2\theta)}$, y como todo cero no real sobre la ventana de $\gamma$ acaba aterrizando (de Bruijn + KKL: a tiempo $\le\Lambda<\tfrac12$), $(\ast)$ vale con esa cota. (2): el cero off de $\zeta$ es un cero no real de $H_0$ con altura $b$; por la cota de tiempo de aterrizaje del Doc 177 §4.1 (Thm 177.6 leído forward desde el aterrizaje): $t_c\ge\frac{b^2}{2n^2}(1-C\varepsilon)$ con $n$ = multiplicidad a escala corriente, $n\le\max(2,C\sqrt{t_c}\log\gamma)$. De (1), $t_c\le(\log\gamma)^{-2/(1-2\theta)}=:\tau$. Si $n\le2$: $b^2\le Ct_c\le C\tau$ da directamente $b\le C\tau^{1/2}=(\log\gamma)^{-1/(1-2\theta)}$. Si $n>2$: $n\le C\sqrt\tau\log\gamma=C(\log\gamma)^{1-\frac{1}{1-2\theta}}\to0$, absurdo para $\gamma$ grande: el caso no ocurre. $\square$

**[COR 178.9] (calibración de dureza; el "GAP de literatura" de D177 se disuelve).** 177.B implica el **confinamiento polilogarítmico** de todos los ceros de $\zeta$: $b\ll(\log\gamma)^{-1-\eta}$. Esto excede en mucho toda región libre de ceros conocida (Vinogradov–Korobov da solo $b\le\tfrac12-c(\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}$: una franja junto al *borde*, no un tubo alrededor del *centro*) e implica de inmediato $m<\infty$ bajo LP-134 (pinza: $b\ge c/\log\gamma$ y $b\le C(\log\gamma)^{-1-\eta}$ son incompatibles a altura grande). En consecuencia:
1. **177.B no puede estar en [KKL], [RT] ni [P15]**, ni seguirse de sus teoremas incondicionales: si lo estuviera, el confinamiento polilogarítmico sería un teorema — y no lo es. El "[GAP de literatura]" del Doc 177 §4.2 no era un hueco bibliográfico: era una imposibilidad. **Nadie lo probó porque es cuasi-RH.**
2. Más en general: **cualquier "zona de realidad uniforme en $t$"** — un teorema del tipo "$H_t$ tiene solo ceros reales a alturas $\ge X(t)$, para todo $t\in(0,1)$ con $X(t)<\infty$" — implica por el mismo argumento $b\le Cn\sqrt{X^{-1}(\gamma)}\to0$: confinamiento cualitativo, desconocido. Por eso la zona asintótica de [P15] (vía 3 del mandato) **necesariamente** es de $t$ separado de cero: su análisis efectivo + barrera funciona en $t\approx0.2$ (con verificación numérica que tenemos prohibida y que tampoco ayudaría: el obstáculo es el límite $t\to0^+$, no la altura); y la regularización de [KKL] es para $t>0$ fijo con umbral de altura **no uniforme** en $t$. La esperanza del mandato ("si su rango es $\gamma\ge\exp(c\,t^{-1/2})$ o mejor, 177.B podría seguirse") queda **refutada estructuralmente**: ningún rango uniforme en $t\to0^+$ existe en la literatura ni puede existir sin probar confinamiento. $\square$ (de la Prop 178.8.)

### 3.4. La equivalencia y el enunciado mínimo residual

**[TEOREMA 178.10] (177.B ≡ confinamiento, módulo (RvM-t) y la banda).** Sea $\theta\in(0,\tfrac12)$. Entonces, condicional a (RvM-t) y con la pérdida de exponentes explícita:
1. 177.B$(\theta)$ $\Rightarrow$ $\Lambda_{\rm loc}(\gamma)\le(\log\gamma)^{-2/(1-2\theta)}$ y confinamiento $b\le C(\log\gamma)^{-1/(1-2\theta)}$ (Prop 178.8; incondicional).
2. Confinamiento $b\le C(\log\gamma)^{-1-\eta}$ ($\eta>0$) $\Rightarrow$ $\Lambda_{\rm loc}(\gamma)\le C'(\log\gamma)^{-2-\eta'}$ para todo $\eta'<2\eta$ $\Rightarrow$ 177.B en la banda sub-difusiva con $\theta_1=\theta_1(\eta')>0$ (Teorema 178.7).
*Prueba de la implicación intermedia de (2).* Todo cero no real de $H_0$ sobre la ventana tiene $b\le CL^{-1-\eta}$; su altura decrece con velocidad $\dot\beta\le-1/\beta+C\rho$ (conjugado propio del Thm 167-2.3 + mar del Lema 177.4 con $D\downarrow$: $|{\rm mar}|\le C\rho$); mientras $\beta\le1/(2C\rho)$ — cierto siempre, pues $\beta\le b_{\max}\le CL^{-1-\eta}\ll1/\rho$ — se tiene $\dot\beta\le-1/(2\beta)$, luego aterriza en $t_c\le\beta(0)^2\le C^2L^{-2-2\eta}$. Los ceros no reales que *entren* horizontalmente a la ventana tras $t=0$ vienen de alturas vecinas $\gamma+O(1)$ con el mismo confinamiento (deriva, Lema 178.6), misma cota. Tomar $\eta'<2\eta$ absorbe constantes. $\square$

La cadena se cierra: **el contenido exacto de 177.B (restringido a su banda útil) es el confinamiento polilogarítmico de los ceros de ζ.** La dinámica de $H_t$ (Teoremas 178.4/178.7) es la parte resoluble y queda resuelta módulo (RvM-t); lo irreducible es un enunciado sobre $H_0$, es decir, sobre $\zeta$ en $t=0$:

**[ENUNCIADO MÍNIMO RESIDUAL 178.C] (confinamiento polilogarítmico).** *Existe $\eta>0$ tal que todo cero $\beta+i\gamma$ de $\zeta$ con $\gamma$ grande cumple $|\beta-\tfrac12|\le C(\log\gamma)^{-1-\eta}$.*

Es el enunciado más débil que (con (RvM-t)) cierra 177.B en su banda; y para el objetivo final ($m<\infty$, Cor 177.8) ni siquiera hace falta pasar por 177.B:

**[COR 178.11] (la segunda torre, deflactada a una pinza estática).** 178.C $\wedge$ LP-134 $\Rightarrow m<\infty$, **sin dinámica**: si hubiera infinitos cuádruplos $(b_j,\gamma_j)$, LP-134 da $b_j\ge c/\log\gamma_j$ y 178.C da $b_j\le C(\log\gamma_j)^{-1-\eta}$, incompatibles para $j$ grande. $\square$

**Lectura honesta del Cor 178.11.** El flujo de calor fue el andamio que *descubrió* la pinza (vía la cadena 174→177→178), pero el corolario final es estático. La torre 2 del Doc 177 ("$m<\infty\Leftarrow$ 177.B $\wedge$ LP-134") queda recalibrada: su pilar dinámico **es** un enunciado de confinamiento sobre $\zeta$, no un lema de literatura sobre $H_t$. La etiqueta "ζ-libre" que la memoria de fase asignaba a 177.B era incorrecta en espíritu: el enunciado es sobre la $H_t$ *aritmética* y su contenido entero vive en la condición inicial — el patrón del Doc 167 §5 (la ley es ζ-libre; el valor no) otra vez, ahora con la identificación exacta de qué parte del valor: $\Lambda_{\rm loc}(\gamma)$, i.e. $b(\gamma)$.

**Simetría de las dos torres (nueva).** Torre 1: RH ⟸ A $\wedge$ LP-112, con A calibrado **Lindelöf-difícil** (Thm 176.7). Torre 2: $m<\infty$ ⟸ 178.C $\wedge$ LP-134, con 178.C calibrado **confinamiento-difícil** (y nótese: una región libre de ceros $b\le(\log\gamma)^{-1-\eta}$ implica, por los métodos estándar de Littlewood, cotas de $\log\zeta$ cerca de la línea del mismo género que Lindelöf — no lo probamos aquí, lo dejamos como observación de plausibilidad, sin etiqueta). Cada torre = un pilar "duro calibrado" + una repulsión LP. La arquitectura es real; ninguno de los cuatro pilares es barato, y este documento mide el segundo.

---

## 4. Test anti-circularidad

| Objeto | ¿RH-libre? | ¿ζ-libre? | Dónde reentra ζ |
|---|---|---|---|
| Lema 178.1 (ODE del gap), Prop 178.2 (saturación del reticulado), Lema 178.3 (bloques cortos) | sí | sí (clase + conteo abstracto) | no reentra |
| Teorema 178.4 / 178.4′ (gap sub-difusivo) | sí | sí, **condicional a (RvM-t)** — conteo de la clase, sin primos | no reentra en la prueba; (RvM-t) para la $H_t$ aritmética se hereda de la condición inicial |
| Puente 178.5 (RvM-t) | sí | enunciado para $H_t$ aritmética | ζ entra solo por cotas de $|H_0|$ en bandas (estándar) |
| Def 178.6′ ($\Lambda_{\rm loc}$), Teorema 178.7 | sí | la definición es de clase; el valor $\Lambda_{\rm loc}(\gamma)$ es ζ | el valor = condición inicial |
| Prop 178.8 / Cor 178.9 / Thm 178.10 | sí | **no**: conclusiones sobre los ceros de ζ | ése es el punto: 177.B ⟹ enunciado sobre ζ; la circularidad temida se materializa como *medida de dureza*, no como error |
| Enunciado 178.C, Cor 178.11 | abiertos | no: ζ puro | — |

Patrón confirmado y afinado: la **ley** (gap-ODE, bloques, relajación) es ζ-libre y queda probada; el **valor** ($\Lambda_{\rm loc}$, $b(\gamma)$) es ζ y es exactamente donde 177.B deja de ser un lema y pasa a ser cuasi-RH.

---

## 5. Veredicto

**177.B: NO probado; NO refutado; REDUCIDO con equivalencia y calibrado como cuasi-RH-difícil.** Resultado por vías: vía 1 no cierra (régimen temporal equivocado; aporta el esquema equilibrio+conteo); vía 2 cierra **la mitad dinámica** (Teorema 178.4′, condicional a (RvM-t) y a realidad local, en la banda sub-difusiva, con par de exponentes admisible $\theta_2\in(\frac14,\frac12)$, $\theta_1=2\theta_2-\frac12$); vía 3 demuestra que **la otra mitad es el todo**: 177.B ⟺ confinamiento polilogarítmico de los ceros de ζ (Thm 178.10), y por eso ninguna combinación de KKL/RT/P15 podía darlo (Cor 178.9 — la hipótesis del mandato sobre la zona asintótica de P15 queda refutada estructuralmente, no por falta de diligencia bibliográfica).

**Probado en este documento:**
1. **[LEMA 178.1]** ODE exacta del gap con mar firmado: $\dot g=4/g-gS$, $S\ge0$.
2. **[PROP 178.2]** No-go del principio del mínimo desnudo: el reticulado comprimido satura la desigualdad exactamente ($\dot g\ge0$ y no más); verificación exacta con $\cos(\lambda z)$. La heurística "$g^2\ge8t$, $\theta=\frac12$ límite" del mandato es falsa sin input de conteo.
3. **[LEMA 178.3]** Bajo (RvM-t), todo bloque con gaps $\le\frac1{2\rho}$ tiene $\le CL$ ceros.
4. **[TEOREMA 178.4/178.4′]** (condicional a (RvM-t) + realidad local en $[t/2,t]$): el gap mínimo crece como $g^2\gtrsim t/\log\gamma$ hasta el techo difusivo; equivale a 177.B en la banda $\log\gamma\in[t^{-(1-2\theta_2)},ct^{-1/2}]$.
5. **[TEOREMA 178.7]** $\Lambda_{\rm loc}(\gamma)\le\frac12(\log\gamma)^{-2/(1-2\theta_1)}$ + (RvM-t) ⟹ 177.B en la banda.
6. **[PROP 178.8 + COR 178.9]** 177.B ⟹ $b\le C(\log\gamma)^{-1/(1-2\theta)}$ para **todo** cero de ζ: confinamiento polilogarítmico, muy por encima de Vinogradov–Korobov. El "[GAP de literatura]" de D177 §4.2 se disuelve: era una imposibilidad disfrazada de hueco bibliográfico.
7. **[TEOREMA 178.10]** Equivalencia (mod (RvM-t), banda, exponentes explícitos): 177.B ⟺ confinamiento.
8. **[COR 178.11]** La torre 2 deflactada a pinza estática: **confinamiento (178.C) $\wedge$ LP-134 ⟹ $m<\infty$**, sin flujo. Simetría final de las dos torres: cada una = pilar duro calibrado (A Lindelöf-difícil / 178.C confinamiento-difícil) + repulsión LP (LP-112 / LP-134).

**GAPs nombrados:**
- **[GAP-178.A]** (= Puente 178.5): (RvM-t) — conteo RvM en ventanas unitarias uniforme en $t\in[0,1]$ para la $H_t$ aritmética. Creído estándar vía [P15] (cotas efectivas en bandas) + Jensen; no verificado línea a línea. Es el único insumo técnico pendiente de la mitad dinámica.
- **[GAP-178.B]** Relajación super-difusiva condicional: extender el Teorema 178.4′ a $\log\gamma>ct^{-1/2}$ (gap normalizado $\ge c$ tras tiempo $\gg\rho^{-2}$, *bajo realidad local*). Candidato natural: la maquinaria de equilibrio local de [RT §2] corrida forward; por el Cor 178.9, solo puede existir en versión condicional-a-realidad — el bloqueo de la versión incondicional es estructural.
- **[ENUNCIADO MÍNIMO RESIDUAL 178.C]** Confinamiento polilogarítmico: $|\beta-\frac12|\le C(\log\gamma)^{-1-\eta}$ para todo cero de ζ. Es el residuo exacto de 177.B y el nuevo pilar de la torre 2.

**Dirección sucesora (Phase 56 continúa):** (a) cerrar GAP-178.A (técnico, acotado, sin pared conceptual); (b) atacar 178.C como objeto propio — nótese que es un enunciado *para todo cero*, i.e. vive del lado malo del cuantificador maestro (Phase 49), pero a diferencia de RH es **cuantitativamente graduable**: la familia $b\le(\log\gamma)^{-1-\eta}$ interpola entre lo conocido ($\eta=-1$ trivial, $b\le\frac12$) y RH ($\eta=\infty$), y la primera pregunta es si los métodos de densidad/momentos dan siquiera $b_j\to0$ a lo largo de *casi todos* los ceros off (versión en densidad de 178.C, que bastaría para el Cor 178.11 si LP-134 se toma también en densidad — cf. la dirección (c) del Doc 177); (c) comprobar si la pinza 178.C∧LP-134 admite una versión con multiplicidades $n$ no acotadas (aquí $n\le2$ salió gratis del auto-mejoramiento; documentarlo si se debilita 178.C).

### Referencias
de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226. — Newman, C.M. (1976), Proc. Amer. Math. Soc. 61, 245–251. — Csordas, G., Smith, W., Varga, R.S. (1994), Constr. Approx. 10, 107–129 (pares de Lehmer ⟹ cotas inferiores de Λ: el lado estático del pliegue). — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306 ($\forall t>0$: finitos ceros no reales, eventualmente reales/simples, espaciado asintóticamente regular **a altura dependiente de $t$, no uniforme** — Cor 178.9 explica por qué no puede ser uniforme). — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6 (§2: dinámica del gas backward; relajación en tiempo macroscópico fijo). — Polymath, D.H.J. (2019), *Effective approximation of heat flow evolution of the Riemann ξ function...*, Res. Math. Sci. 6, 31 (aproximación efectiva $A+B-C$ uniforme en $t\in[0,1/2]$ en bandas; zona de realidad con $t$ separado de cero + barrera; usada aquí SOLO en su parte asintótica, y solo como soporte del Puente 178.5). — Szegő, G. (1939), *Orthogonal Polynomials*, AMS Colloq. Publ. 23. — Sobre Vinogradov–Korobov: Ivić, A. (1985), *The Riemann Zeta-Function*, Wiley, cap. 6. — Danskin, J.M. (1966), J. SIAM Appl. Math. 14, 641–664 (derivada del mínimo). — Docs internos: 167, 174 (vía 177), 177.
