# Documento 177 — GAP-174.B decidido: la constante de Hermite del despegue, la cota global de energía y la lógica forward de aterrizajes

**Programa:** Hipótesis de Riemann — Fase 55 (dos flechas)
**Fecha:** 2026-06-11
**Mandato:** decidir GAP-174.B (Doc 174 §2.3): ¿el despegue backward satisface $\beta(t)^2\le 2k|t|(1+o(1))$ con $k$ = multiplicidad local de casi-colisión a escala $\sqrt{8|t|}$? Construir/decidir; no auditar.
**Prerrequisitos (certificados, no re-derivados):** Doc 167 (ley de balance $\dot I=-2\kappa-D$, $D\ge0$ explícita término a término, Thm 2.3; pliegue Prop 2.6), Doc 174 (modelo cerrado del cuádruplo Thm 174.4; principio del máximo Lema 174.3; red perfecta = punto fijo Prop 174.7; refutación de "$I<\infty\Rightarrow m<\infty$" en la clase §3.3; enunciado de GAP-174.B §2.3), Doc 144 (contraejemplo Hadamard).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] prueba completa o sin etiqueta; [GAP] declarado. Sin numéricos: todo en forma cerrada o asintótica con control de errores.

---

## 0. Convenciones

Carta $H_t$ (Polymath 15): $\partial_tH_t=-\partial_z^2H_t$, equivalentemente $H_{t}=e^{-(t-t_0)\partial_z^2}H_{t_0}$. Para $f$ entera de orden $<2$ el operador $e^{s\partial_z^2}$ ($s>0$) es la convolución gaussiana
$$\bigl(e^{s\partial_z^2}f\bigr)(z)=\frac{1}{\sqrt{4\pi s}}\int_{\mathbb R}f(z+y)\,e^{-y^2/4s}\,dy=\mathbb E\bigl[f(z+\sqrt{2s}\,Z)\bigr],\quad Z\sim N(0,1),$$
(de Bruijn 1950 §2), de modo que la evolución **backward en $t$** de $H_{t_0}$ es la **gaussiana hacia "adelante"**: $H_t=e^{\sigma\partial_z^2}H_{t_0}$ con $\sigma:=t_0-t>0$. Dinámica de ceros simples: $\dot z_k=2\sum'_{j\ne k}(z_k-z_j)^{-1}$ en $t$; en tiempo backward $\sigma$ los signos se invierten. Ceros superiores $z_k=\alpha_k+i\beta_k$, $\beta_k>0$; $I=\sum\beta_k^2$. Densidad local $\rho$ = ceros por unidad de longitud en la ventana ($\rho\asymp\frac1\pi\log\gamma$ para ζ en carta $H$).

**Invariancia de escala de la constante de despegue.** Bajo $z\mapsto\lambda z$, $t\mapsto\lambda^2t$ la dinámica es invariante y $\beta^2/|t|$ es invariante: toda constante $c$ en una ley $\beta^2=c\,|t|$ es la misma en carta $H$ y en carta ζ ($b_\zeta=\beta/2$, $\tau_\zeta=t/4$). Las constantes de este documento no necesitan conversión.

**Convención de multiplicidad.** Trabajamos con $n$ := **número de ceros del cluster progenitor** (los ceros reales que colapsan backward). El enunciado del GAP-174.B usa $k$ ambiguamente ($k$ conjugados en §2.3(b) del Doc 174, i.e. $n=2k$; o $k=n-1$ si se calibra con el par $n=2$, $k=1$). Decidimos en la variable limpia $n$ y traducimos al final: **en cualquiera de las dos lecturas, la constante $2k$ queda refutada para $n\ge3$.**

---

## 1. El modelo local exacto: el colapso es Hermite y la constante es $c(n)=4\,h_{\max}(n)^2$

### 1.1. El despegue múltiple en forma cerrada

**[TEOREMA 177.1] (despegue múltiple exacto; la solución autosimilar de Hermite).** Sea $H_{t_{\rm col}}(z)=(z-x_0)^n$ localmente (colisión backward de $n$ ceros reales en $x_0$ a tiempo $t_{\rm col}$; el caso aislado puro). Entonces para $\sigma=t_{\rm col}-t>0$ (backward),
$$H_t(z)\;=\;e^{\sigma\partial_z^2}(z-x_0)^n\;=\;(-\sigma)^{n/2}\,H_n\!\Bigl(\frac{z-x_0}{2\sqrt{-\sigma}}\Bigr)\qquad\text{(rama formal; identidad polinomial exacta)},$$
con $H_n$ el polinomio de Hermite de los físicos, y los ceros son **exactamente**
$$z_j(t)\;=\;x_0+2i\sqrt{\sigma}\,h_j,\qquad j=1,\dots,n,$$
donde $h_1<\dots<h_n$ son los ceros (reales, simétricos) de $H_n$. Es decir: el cluster despega **verticalmente, apilado sobre la recta $\operatorname{Re}z=x_0$**, en $\lfloor n/2\rfloor$ pares conjugados a alturas $2\sqrt\sigma\,h_j$ (más un cero que permanece real si $n$ es impar), con perfil autosimilar $\propto\sqrt\sigma$. En particular
$$\boxed{\;\beta_{\max}(t)^2\;=\;c(n)\,\sigma,\qquad c(n):=4\,h_{\max}(n)^2\;}$$
donde $h_{\max}(n)$ es el mayor cero de $H_n$. Forward ($t>t_{\rm col}$) la misma identidad da los $n$ ceros **reales** $x_0+2\sqrt{t-t_{\rm col}}\,h_j$: el aterrizaje del cluster crea el abanico de Hermite real.

*Prueba.* La identidad de semigrupo: por reescalado $z=\lambda u$, $\partial_z=\lambda^{-1}\partial_u$, y la identidad clásica $e^{-\partial_x^2/4}x^n=2^{-n}H_n(x)$ (equivalente a la fórmula de Rodrigues vía transformada de Weierstrass; Szegő 1939, (5.5.7)), se obtiene $e^{s\partial_z^2}z^n=(-s)^{n/2}H_n\bigl(z/(2\sqrt{-s})\bigr)$ para todo $s\in\mathbb C$ (ambos lados son polinomios en $z$ cuyos coeficientes son polinomios en $s$: la identidad para $s<0$ se extiende algebraicamente; verificación directa: $n=2$ da $z^2+2s$, $n=3$ da $z^3+6sz$, ceros $0,\pm i\sqrt{6\sigma}$ con $s=\sigma>0$ ✓). Los ceros de $H_n(w)$ son reales y simples; con $w=(z-x_0)/(2\sqrt{-\sigma})=(z-x_0)/(2i\sqrt\sigma)$, $H_n(w)=0\iff z=x_0+2i\sqrt\sigma h_j$. $\square$

**Verificación cruzada (momento de potencias).** Para la dinámica backward de un polinomio de grado $n$: $\frac{d}{d\sigma}\sum_kz_k^2=-2\sum_k\sum_{j\ne k}\frac{z_k\cdot 2}{z_k-z_j}\cdot\frac12\dots$ — limpio: $\sum_k z_k\dot z_k\big|_{\rm backward}=-2\sum_{k\ne j}\frac{z_k}{z_k-z_j}=-2\cdot\binom n2$ (simetrizando $z_k/(z_k-z_j)+z_j/(z_j-z_k)=1$), luego $\frac{d}{d\sigma}\sum z_k^2=-2n(n-1)$. En el modelo: $\sum_jz_j^2=-4\sigma\sum_jh_j^2=-4\sigma\cdot\frac{n(n-1)}2=-2n(n-1)\sigma$ ✓ (la suma de cuadrados de los ceros de $H_n$ es $n(n-1)/2$, del coeficiente subprincipal de $H_n$). Consistencia exacta.

### 1.2. La constante exacta: tabla y asintótica

$$c(2)=2,\qquad c(3)=6,\qquad c(4)=2\,(3+\sqrt6)\approx10.90,\qquad c(5)=2\,(5+\sqrt{10})\approx16.32,$$
(de $H_2=4x^2-2$, $H_3=8x^3-12x$, $H_4=16x^4-48x^2+12$, $H_5=32x^5-160x^3+120x$). Asintótica (Plancherel–Rotach 1929; Szegő 1939 §6.32): $h_{\max}(n)=\sqrt{2n+1}+2^{-1/3}(2n+1)^{-1/6}a_1+o(n^{-1/6})$ con $a_1\approx-2.3381$ el primer cero de Airy, luego
$$\boxed{\;c(n)\;=\;8n+4-2^{8/3}|a_1|\,(2n+1)^{1/3}+O(n^{-1/3})\;=\;8n\,\bigl(1+O(n^{-2/3})\bigr).\;}$$
La convergencia a $8n$ es lenta ($c(n)/n=1,2,2.72,3.26,\dots\to8$), pero la **cota** $c(n)\le 8n+4$ vale para todo $n$ (pues $h_{\max}(n)<\sqrt{2n+1}$, cota clásica de los ceros de Hermite).

### 1.3. REFUTACIÓN de la constante $2k$ del enunciado original

**[PROP 177.2] (la constante del GAP-174.B es falsa para $n\ge3$).** En la lectura $k=n-1$ (calibrada con el par: $n=2$, $k=1$, $\beta^2=2\sigma$ ✓), el tridente $n=3$ da exactamente $\beta^2=6\sigma>2k\sigma=4\sigma$. En la lectura $n=2k$ del Doc 174 §2.3(b), el cuarteto $n=4$ ($k=2$) da $\beta_{\max}^2=(6+2\sqrt6)\sigma\approx10.90\,\sigma>4\sigma$. Asintóticamente la constante verdadera es $\sim8n$ ($=16k$ en la lectura $n=2k$): **factor 8 sobre la conjeturada**. $\square$ (Es el Teorema 177.1 con la tabla de §1.2.)

**Por qué falló la heurística del Doc 174 §2.3(b).** Aquella contaba solo los $k$ conjugados a distancia $\approx2\beta$ (cada uno aportando $\lesssim1/\beta$ a $\dot\beta$), **suponiendo los $k$ pares a la misma altura**. El despegue real es apilado a alturas distintas ($2\sqrt\sigma h_j$, $h_j$ distintos), y backward **los ceros del mismo lado empujan hacia arriba al de arriba** (el signo de la atracción forward se invierte; álgebra exacta en §2.3). El cero superior está en el borde del semicírculo del gas de Hermite y recibe el empuje coherente de todo el cluster: eso produce $8n$, no $2n$. La estructura del enunciado (lineal en $|t|$, lineal en la multiplicidad) **sobrevive**; la constante se corrige.

### 1.4. El modelo con resto: control de errores

**[PROP 177.3] (estabilidad del modelo).** Sea $H_{t_{\rm col}}=(z-x_0)^nG(z)$ con $G$ entera de orden $<2$, $G$ sin ceros en $|z-x_0|\le d$ y $|G'/G|\le C_G/d$ en $|z-x_0|\le d/2$ (en la clase, $C_G/d\lesssim\rho$ por RvM, con $\rho$ la densidad local más el término del gas lejano). Entonces para $\sqrt\sigma\,\sqrt n\ll d$ los $n$ ceros de $H_t$ próximos a $x_0$ están a distancia $O\bigl(\sqrt{n\sigma}\cdot\frac{\sqrt{n\sigma}}{d}\bigr)$ de los del modelo $x_0+2i\sqrt\sigma h_j$; en particular
$$\beta_{\max}(t)^2\;=\;c(n)\,\sigma\,\Bigl(1+O\bigl(\tfrac{\sqrt{n\sigma}}{d}\bigr)\Bigr).$$

*Prueba (esquema completo).* Representación gaussiana: $H_t(x_0+\zeta)=\mathbb E\bigl[(\zeta+\sqrt{2\sigma}Z)^n\,G(x_0+\zeta+\sqrt{2\sigma}Z)\bigr]$. En la escala $|\zeta|\le A\sqrt{n\sigma}$, escribir $G(x_0+\cdot)=G(x_0)\,(1+r(\cdot))$ con $|r(y)|\le C|y|/d$ en $|y|\le d/2$; la cola gaussiana $|y|>d/2$ contribuye $O(e^{-cd^2/(n\sigma)})$ relativo (aquí entra orden $<2$ para dominar $G$ en la cola). Entonces $H_t(x_0+\zeta)=G(x_0)\bigl[P_\sigma(\zeta)+E(\zeta)\bigr]$ con $P_\sigma=e^{\sigma\partial^2}\zeta^n$ y $|E|\le C'\frac{\sqrt{n\sigma}}{d}\max_{|\zeta'|\asymp|\zeta|}|P_\sigma|$ sobre circunferencias que evitan los ceros de $P_\sigma$ a distancia $\gtrsim\sqrt\sigma$ (los ceros de Hermite reescalados están $\sqrt\sigma$-separados salvo el factor de densidad local del semicírculo, $\sqrt\sigma/\sqrt n$ en el bulk — tomar circunferencias adaptadas). Rouché da la biyección de ceros con el desplazamiento anunciado. $\square$

---

## 2. Las tres obstrucciones globales

### 2.1. (i) El mar lejano: el empuje vertical es absolutamente convergente y $O(\rho)$

**[LEMA 177.4] (cota del mar).** Sea $z=\alpha+i\beta$ un cero superior y $S\subset Z$ los ceros a distancia $\ge D$ de $z$, con densidad RvM local $\rho$ y banda $|\operatorname{Im}|\le1$. La contribución de $S$ a $d\beta/d\sigma$ es, en valor absoluto,
$$\Bigl|2\sum_{w\in S}\frac{\beta-\operatorname{Im}w}{|z-w|^2}\Bigr|\;\le\;C\,(\beta+1)\,\frac{\rho}{D}\,\bigl(1+O(\tfrac1{\rho D})\bigr),$$
y si $S$ es **todo** el mar real ($D\downarrow0$ excluyendo el cluster): $\le C\rho$ uniformemente en $\beta$.

*Prueba.* La parte imaginaria de $\sum 1/(z-w)$ es absolutamente convergente bajo RvM (numerador acotado por $\beta+1$, denominador $\ge\max(D,|{\alpha-\operatorname{Re}w}|)^2$): $\sum_{|x-\alpha|\ge D}\frac{\beta+1}{(x-\alpha)^2}\approx(\beta+1)\rho\int_D^\infty\frac{ds}{s^2}=(\beta+1)\frac\rho D$ (la corrección por crecimiento logarítmico de la densidad se absorbe en $C$). Para el mar completo: $\sum_x\frac{\beta}{(\alpha-x)^2+\beta^2}\le\rho\bigl(\#\{|x-\alpha|\le\beta\}\cdot\frac1\beta\cdot\frac1\rho+\int_\beta^\infty\frac{\beta\,ds}{s^2}\bigr)\le C\rho$. $\square$

**Lectura.** El mar lejano aporta a $\frac{d}{d\sigma}\beta^2$ a lo sumo $C\rho\beta$: integrado, una corrección **multiplicativa** $1+O(\rho\sqrt{c(n)\sigma})$ sobre la ley local. Es inocuo exactamente en el rango $\sigma\ll1/(n\rho^2)$ — para ζ a altura $\gamma$: $|t|\ll(n\log^2\gamma)^{-1}$. Fuera de ese rango la ventana $\sqrt{8|t|}$ contiene $\gtrsim\rho\sqrt{|t|}$ ceros y la multiplicidad corriente $n(t)$ crece: el enunciado correcto es local-en-$|t|$ con $n=n(t)$ (§2.2).

### 2.2. (ii) Fusión backward de clusters: $n$ debe ser la multiplicidad a escala corriente — y la forma cuadrática de la cota la hace monótona bajo fusión

Backward, dos clusters a distancia $\Delta$ interactúan apreciablemente cuando $\sqrt{n\sigma}\gtrsim\Delta$: a partir de ahí cuentan como uno ($n_{\rm tot}=n_1+n_2$). Esto **no rompe** el enunciado, por dos hechos:

1. **La definición correcta es a escala corriente**: $n(t):=\#\{\text{ceros en la ventana de radio }A\sqrt{c(n)\,|t|}\text{ alrededor del par}\}$ (autoconsistente por dyadic pigeonhole: existe el menor radio admisible). Así estaba ya en el enunciado del GAP-174.B ("a escala $\sqrt{8|t|}$"); aquí se confirma que es forzoso, no opcional.
2. **Superaditividad**: cualquier cota de la forma $\beta_{\max}^2\le G(n)\,\sigma$ con $G$ superaditiva ($G(n_1)+G(n_2)\le G(n_1+n_2)$) se pega monótonamente a través de una fusión en $\sigma_*$: $I_{\rm tot}(\sigma)\le\sum_iG(n_i)\sigma_*+G(n_{\rm tot})(\sigma-\sigma_*)\le G(n_{\rm tot})\,\sigma$. Tanto $G(n)=c(n)\approx8n$ como la $G(n)=2n^2$ del Teorema 177.6 son superaditivas. La fusión está cuantitativamente realizada en el modelo exacto de §2.3: dos pares apilados convergen asintóticamente a la ley del 4-cluster, $c(4)\sigma$.

### 2.3. (iii) El apilamiento: álgebra exacta, solución cerrada, y el "robo" cuantificado

**El álgebra pedida.** Dos pares a la misma abscisa $\gamma$, alturas $0<\beta_1<\beta_2$ (ceros $\gamma\pm i\beta_1$, $\gamma\pm i\beta_2$; los espejos en $-\gamma$ aportan $O(\gamma^{-2})$, ignorados). Velocidad del cero superior $z=\gamma+i\beta_2$ backward:
$$\frac{d\beta_2}{d\sigma}\;=\;2\Bigl[\frac1{\beta_2-\beta_1}+\frac1{\beta_2+\beta_1}+\frac1{2\beta_2}\Bigr]\;>\;0:$$
el término $\frac2{\beta_2-\beta_1}$ es el del cero **del mismo lado** inmediatamente inferior: forward lo atrae hacia abajo, **backward lo lanza hacia arriba**, casi-singularmente si están apilados cerca. *El apilamiento acelera la subida.* La pregunta es si rompe la linealidad o excede la ley del cluster fusionado. Respuesta: no — el sistema es exactamente soluble:

**[PROP 177.5] (cuarteto apilado, solución cerrada).** El cuarteto vertical $\{\gamma\pm i\beta_1,\gamma\pm i\beta_2\}$ permanece vertical (paridad del polinomio local $w^4+aw^2+c$ en $w=z-\gamma$, coeficientes reales, preservada por el calor) y, con $S=\beta_1^2+\beta_2^2$, $P=\beta_1^2\beta_2^2$:
$$\frac{dS}{d\sigma}=12,\qquad\frac{dP}{d\sigma}=2S\qquad\Longrightarrow\qquad S=S_0+12\sigma,\quad P=P_0+2S_0\sigma+12\sigma^2,$$
$$\beta_{2}^2(\sigma)\;=\;\tfrac12\Bigl(S+\sqrt{S^2-4P}\Bigr),\qquad (S^2-4P)'=16S>0.$$
Consecuencias exactas: (a) el discriminante crece — los dos pares **se separan** backward, nunca se fusionan en altura; (b) asintóticamente $\beta_2^2=(6+2\sqrt6)\,\sigma\,(1+o(1))=c(4)\,\sigma\,(1+o(1))$: el par superior realiza **exactamente** la ley de Hermite del cluster fusionado $n=4$, sea cual sea el dato inicial; (c) el "robo de energía" es real y está cuantificado: del presupuesto total $dS/d\sigma=12$, el par de arriba toma asintóticamente la fracción $\frac{6+2\sqrt6}{12}=\frac{3+\sqrt6}{6}\approx90.8\%$ y el de abajo $(6-2\sqrt6)\sigma\approx9.2\%$; (d) **cota incondicional en todo tiempo**: $\beta_2^2\le S\le S_0+12\sigma$ — nunca por encima de la ley aditiva del cluster total.

*Prueba.* Es el Thm 174.4 con ambas raíces $w$-cuadráticas reales negativas ($w_i=-\beta_i^2$), leído backward: $a'=12$, $c'=2a$; $S=a$, $P=c$. La verticalidad: $e^{\sigma\partial^2}$ preserva coeficientes reales y paridad en $w$. (b): $S\sim12\sigma$, $P\sim12\sigma^2$, $\sqrt{S^2-4P}\sim\sqrt{96}\,\sigma$, $\beta_2^2\sim(6+2\sqrt6)\sigma=2(3+\sqrt6)\sigma=4h_{\max}(4)^2\sigma$ ✓. $\square$

**Veredicto sobre (iii):** el apilamiento empuja **hacia arriba** backward (la cuenta de signos pedida), acelera la subida del par superior por encima de su ley individual $2\sigma$, **pero no por encima de la ley del cluster fusionado** $c(n_{\rm tot})\sigma$ — y en el modelo exacto la satura. El lema no necesita hipótesis de separación entre pares *del mismo cluster* (el apilamiento ya está dentro de la constante de Hermite); necesita separación solo entre el cluster y el resto, que es la definición a escala corriente de §2.2. El censo de progenitores no cambia de naturaleza: cambia la constante ($8n$, no $2k$).

---

## 3. Del modelo al teorema global: la cota de energía incondicional

Lo que se puede probar hoy sin la extremalidad de Hermite es la versión **cuadrática en $n$, lineal en $\sigma$** — suficiente para toda la lógica de huérfanos.

**[TEOREMA 177.6] (cota universal de subida, término a término).** Sea $J\ni\sigma$ un intervalo backward en que la dinámica está definida, con ceros simples, y sea $W$ un cluster admisible: $n=2\kappa_W+r_W$ ceros ($\kappa_W$ pares superiores, $r_W$ reales) en un disco de radio $r_W^{\rm geo}$, con los demás ceros (incl. el cluster espejo) a distancia $\ge D$ y densidad exterior RvM $\rho$. Sea $I_W=\sum_{k\in W,\,\beta_k>0}\beta_k^2$. Entonces
$$\frac{dI_W}{d\sigma}\;\le\;2\kappa_W\bigl(4\kappa_W+2r_W-3\bigr)\;+\;C\rho\,\frac{I_W+\sqrt{\kappa_WI_W}}{D}\;\le\;2n^2+C\rho\,\frac{I_W+\sqrt{nI_W}}{D},$$
y mientras $C\rho(\sqrt{n^2\sigma}+1)\sigma/D\le\varepsilon$:
$$\boxed{\;\beta_{\max}(\sigma)^2\;\le\;I_W(\sigma)\;\le\;\bigl(I_W(0)+2n^2\sigma\bigr)\,(1+C\varepsilon).\;}$$

*Prueba.* Es la ley de balance del Thm 167-2.3 restringida a $W$ y leída backward, acotando cada bloque por su alineamiento vertical: $\frac{dI_W}{d\sigma}=4\sum_{k\in W\uparrow}\sum_{w\ne z_k}\frac{\beta_k(\beta_k-\operatorname{Im}w)}{|z_k-w|^2}$. (1) Conjugado propio: $+2$ por modo, total $2\kappa_W$. (2) Cruzados dentro de $W$, simetrizando pares ordenados como en 167-2.3: cada uno de los cuatro términos es $\frac{(\beta_k\mp\beta_l)^2}{d^2}\le1$ porque la distancia correspondiente domina la diferencia/suma vertical ($|z_k-z_l|\ge|\beta_k-\beta_l|$, $|z_k-\bar z_l|\ge\beta_k+\beta_l$, etc.): total $\le8\kappa_W(\kappa_W-1)$. (3) Reales de $W$: $4\beta_k^2/|z_k-x|^2\le4$ cada uno: $\le4\kappa_Wr_W$. Suma interna: $2\kappa_W+8\kappa_W(\kappa_W-1)+4\kappa_Wr_W=2\kappa_W(4\kappa_W+2r_W-3)\le2\kappa_W(2n-3)\le2n^2$ (usando $2\kappa_W\le n$). (4) Exterior (mar, espejo, antípoda): Lema 177.4 por cero superior, $4\beta_k\cdot C(\beta_k+1)\rho/D$, sumado $\le C\rho(I_W+\sqrt{\kappa_WI_W})/D$ (Cauchy–Schwarz). Grönwall con el término pequeño da el recuadro. $\square$

**Calibración de la holgura.** El colapso monomial realiza $\frac{dI_W}{d\sigma}=n(n-1)$ exactamente (§1.1, mitad superior del momento $2n(n-1)$): la cota $2n^2$ pierde como mucho un factor $\approx2$ **en la energía**; en la **altura máxima** la verdad conjetural es $c(n)\approx8n$ (lineal), y la cota probada $2n^2$ es cuadrática porque permite que toda la energía del cluster se concentre en un par. Cerrar ese hueco es:

**[GAP-177.A] (extremalidad de Hermite — el resto preciso de GAP-174.B).** *Para todo cluster admisible de $n$ ceros (geometría inicial arbitraria con $I_W(0)=0$, i.e. todos reales en una ventana de ancho $w_0$), ¿vale $\beta_{\max}(\sigma)^2\le c(n)\,\sigma\,(1+O(w_0/\sqrt\sigma)+o(1))$ con $c(n)=4h_{\max}(n)^2$, i.e. el colapso monomial (= perfil de Hermite, único despegue autosimilar) es extremal para la altura máxima?* Evidencia: (a) exacto y saturado en $n\le4$ vertical (Prop 177.5(b,d)); (b) el perfil de Hermite es el equilibrio del gas log en potencial cuadrático — el reescalado autosimilar del flujo — y los demás datos convergen a él tras el transitorio; (c) la cota cuadrática probada lo implica salvo constante para $n$ acotado. No tenemos prueba para $n\ge5$ general (la dificultad: un dato inicial sesgado podría sobrecargar transitoriamente el par superior; la Prop 177.5(d) lo excluye en el caso vertical $n=4$ vía $\beta_2^2\le S$, y el análogo $\beta_{\max}^2\le I_W\le n(n-1)\sigma$ del momento exacto solo vale si $\sum\alpha^2$ no crece — el transporte horizontal no se cierra, GAP-174.D).

---

## 4. La lógica forward: aterrizajes, casi-dobles y el lema mínimo sobre $g(t)$

### 4.1. Re-derivación limpia de la cadena temporal (corrigiendo la dirección)

Un par no-real presente en $t=0$ a altura $b$ (escenario ¬RH): su historia **backward** lo tiene más alto ($M(t)\ge b^2+2|t|$, Lema 174.3 invertido) — el lema de despegue acota a sus *competidores* (los pares con progenitor), no a él: así se detecta el huérfano (§5). Su futuro **forward** es un aterrizaje en $t_c\in(0,\Lambda]$, y por el Teorema 177.6 leído desde el aterrizaje: $b^2=\beta(0)^2\le I_W(0)\le2n^2t_c\,(1+C\varepsilon)$, i.e.
$$t_c\;\ge\;\frac{b^2}{2n^2}\,(1-C\varepsilon),\qquad\text{y por el Lema 174.3:}\quad t_c\le\tfrac12 M(0).$$
**Cada aterrizaje crea un casi-doble real**: por el pliegue (Prop 167-2.6 / 167-1.6), para $t>t_c$ el gap recién nacido es $g(t)=\Theta(\sqrt{t-t_c})$ (constante $2\sqrt2$ en el caso aislado, Cálculo 174.6 invertido). Esta es la dirección **más fuerte** que el backward: no necesita la estadística completa de gaps de ζ, sino solo cotas inferiores de gaps de $H_t$ para $t>0$ — territorio donde [KKL] da teoremas incondicionales.

### 4.2. Qué da KKL y qué falta — el lema mínimo

**Estado de literatura (honesto).** [KKL 2009] prueban, para cada $t>0$ **fijo**: $H_t$ tiene finitos ceros no reales, y los ceros reales son eventualmente simples; además (es el insumo que Rodgers–Tao describen en su introducción) los ceros reales de $H_t$ se vuelven asintóticamente regulares — localmente como progresión aritmética con el espaciado medio — a alturas suficientemente grandes *dependiendo de $t$*. [RT 2020] explotan el reverso: si $\Lambda<0$, los ceros de ζ serían asintóticamente localmente equiespaciados, contradiciendo estimaciones incondicionales de fluctuación de conteo. **[GAP de literatura]:** no conocemos en [KKL], [P15] ni [RT] una forma *cuantitativa y uniforme en $t\to0^+$* del tipo "gap normalizado $\ge g(t)$ a alturas $\ge\Gamma(t)$ con $g,\Gamma$ explícitas". Ese es exactamente el hueco, y lo nombramos:

**[LEMA-MÍNIMO 177.B] (KKL cuantitativo en la esquina $t\to0^+$; no probado aquí).** *Existen $\theta\in(0,\tfrac12)$ y $c>0$ tales que, para la $H_t$ aritmética y todo $t\in(0,1)$: todo gap consecutivo de ceros reales de $H_t$ a altura $\gamma\ge\Gamma(t):=\exp\bigl(t^{-(1/2-\theta)}\bigr)$ satisface $g_{\rm norm}:=g\cdot\frac{\log\gamma}{4\pi}\ge c\,t^{\theta}$.*

**Plausibilidad estructural (por qué $\theta<1/2$ es la frontera natural):** el tiempo de relajación difusiva del gap local es $\asymp(\text{espaciado medio})^2=(4\pi/\log\gamma)^2$; el lema pide regularización solo cuando $t\gg(\log\gamma)^{-2}\iff\gamma\le\exp(t^{-1/2})$ — i.e. **estrictamente dentro del régimen donde el calor ya tuvo tiempo de actuar**. El umbral $\Gamma(t)=\exp(t^{-(1/2-\theta)})$ está por debajo de $\exp(t^{-1/2})$: el lema es la forma cuantitativa de "los gaps relajan difusivamente", el mismo mecanismo que [P15] usa numéricamente y [RT] usan en $t<0$. No es un enunciado sobre ζ en $t=0$: es dinámica de $H_t$ en el interior, el lado bueno.

### 4.3. El teorema condicional: la patología solo acumula en la frontera, y la esquina se cierra con LP-134

**[TEOREMA 177.7] (condicional al Lema 177.B; "los aterrizajes solo acumulan en $t=0^+$", cuantificado).** Supóngase el Lema 177.B. Entonces todo aterrizaje en $(t_c,\gamma_c)$ con $t_c\in(0,1)$ cumple $\gamma_c\le\exp\bigl(C\,t_c^{-(1/2-\theta)}\bigr)$. En consecuencia: (1) para todo $\varepsilon>0$, los aterrizajes en $[\varepsilon,\Lambda]$ ocurren en la región acotada $\gamma\le\exp(C\varepsilon^{-(1/2-\theta)})$ — los aterrizajes **solo pueden acumular en $t=0^+$** (en tiempos interiores ya lo prohibía [KKL]; lo nuevo es la cota explícita de altura); (2) si $m=\infty$, los infinitos cuádruplos $(b_j,\gamma_j)$ tienen $t_j\to0^+$, $\gamma_j\ge\exp(c\,t_j^{-(1/2-\theta)})$ y, vía el Teorema 177.6 forward con $n_j\le C\rho(\gamma_j)\sqrt{n_jt_j}$ (multiplicidad a escala corriente, i.e. $n_j\le C\sqrt{t_j}\log\gamma_j$ salvo $n_j\le 2$),
$$b_j^2\;\le\;2n_j^2\,t_j\,(1+o(1))\;\le\;C\,t_j^{2}\log^2\gamma_j\;\le\;C\,(\log\gamma_j)^{2-\frac{4}{1-2\theta}},\qquad\frac{4}{1-2\theta}>4,$$
es decir $b_j\le(\log\gamma_j)^{-1-\eta}$ con $\eta=\eta(\theta)>0$: **la patología vive en la esquina $(t,b)\to(0,0)$ con alturas superexponenciales y alturas-off polilogarítmicamente pequeñas, por debajo de la escala $1/\log\gamma$.**

*Prueba.* Aterrizaje en $(t_c,\gamma_c)$: por el pliegue, para $\delta\in(0,t_c]$ el gap normalizado en $t_c+\delta$ a altura $\gamma_c$ es $\le C\sqrt\delta\,\log\gamma_c$. Si $\gamma_c\ge\Gamma(t_c)$ ($\ge\Gamma(t_c+\delta)$, $\Gamma$ decreciente en $t$), el lema exige $C\sqrt\delta\log\gamma_c\ge c(t_c+\delta)^\theta$ para todo $\delta\le t_c$; con $\delta=t_c$: $\log\gamma_c\ge c't_c^{\theta-1/2}$, i.e. $\gamma_c\ge\exp(c't_c^{-(1/2-\theta)})$ — pero entonces tomando $\delta\to0^+$: $C\sqrt\delta\log\gamma_c\ge ct_c^\theta$ falla para $\delta<(ct_c^\theta/C\log\gamma_c)^2>0$: contradicción **salvo** $\gamma_c<\Gamma(t_c)$. Luego todo aterrizaje tiene $\gamma_c<\Gamma(t_c)=\exp(t_c^{-(1/2-\theta)})$… y al revés, si $\gamma_c<\Gamma(t_c)$ no hay restricción: la cota válida es $\gamma_c\le\Gamma(t_c)$, que es (1). [Nota de signo: el lema prohíbe gaps pequeños *por encima* de $\Gamma$; el aterrizaje crea gaps arbitrariamente pequeños justo después de $t_c$; por tanto el sitio del aterrizaje está *por debajo* de $\Gamma(t_c)$.] Para (2): $m=\infty$ con [KKL] ($\kappa(\varepsilon)<\infty$ $\forall\varepsilon$) fuerza $t_j\to0^+$; si además $\gamma_j\to\infty$ (a alturas acotadas solo caben finitos cuádruplos, por finitud local), la cadena con $t_j\ge\Gamma^{-1}$-dual: $\gamma_j\le\exp(t_j^{-(1/2-\theta)})$ da $t_j\le(\log\gamma_j)^{-\frac{2}{1-2\theta}}$, y la cota de despegue forward ($b_j^2\le2n_j^2t_j$, Teorema 177.6 desde el aterrizaje, válida en el rango del mar lejano: $t_j\ll(n_j\log^2\gamma_j)^{-1}$, que la propia cadena garantiza a posteriori) con $n_j\le\max(2,C\sqrt{t_j}\log\gamma_j)$ da el exponente. $\square$

**Doble consistencia obligada (¿por qué no contradice la refutación del Doc 174 §3.3?).** El contraejemplo de Hadamard ($m=\infty$, $I<\infty$; $\gamma_j=2^j$, $b_j=e^{-\gamma_j}$, $t_j\approx b_j^2/2$) tiene $\log\gamma_j=j\log2$ mientras $\exp(t_j^{-(1/2-\theta)})$ es una torre gigantesca: sus aterrizajes ocurren **muy por debajo** del umbral $\Gamma(t_j)$ — el Lema 177.B no los prohíbe (es consistente con la clase ✓), y sus $b_j=e^{-\gamma_j}\ll(\log\gamma_j)^{-1-\eta}$ satisfacen holgadamente la esquina del Teorema 177.7 ✓. Y nótese: el contraejemplo **viola LP-134** ($b_j\log\gamma_j\to0$). Esto muestra que las dos piezas siguientes son ambas necesarias y que el corte está bien hecho:

**[COR 177.8] (cierre condicional de la mitad de finitud).** *Lema 177.B ($\theta<\tfrac12$) $\;\wedge\;$ LP-134 ($\liminf b\cdot\log\gamma>0$ sobre cuádruplos de ζ) $\;\Longrightarrow\;m<\infty$.* En efecto: si $m=\infty$, el Teorema 177.7(2) da $b_j\log\gamma_j\le(\log\gamma_j)^{-\eta}\to0$, contradiciendo LP-134 para $j$ grande. $\square$

**Lectura honesta del Cor 177.8.** No es una prueba de $m<\infty$: LP-134 es una repulsión conjetural (y el Lema 177.B está abierto). Es la **soldadura nueva**: la mitad dinámica (177.B: gaps de $H_t$ en el interior, $t>0$, donde hay teoremas) + la mitad aritmética mínima (LP-134: repulsión del eje en $t=0$) implican finitud. Comparado con el estado pre-177: la mitad aritmética se redujo de "estadística completa de gaps de ζ" a **una sola repulsión polilogarítmica**, y la dinámica que falta es un enunciado de regularización difusiva de $H_t$, no de ζ. Esto es estrictamente mejor que el censo backward del Doc 174 (que necesitaba la función de concentración $\nu(\delta,T)$ entera).

---

## 5. El teorema de huérfanos (con la constante corregida)

**[DEFINICIÓN-NUEVA 177.9] (huérfano, cuantitativo).** Un par no-real a tiempo $t<0$ con altura $\beta$ y multiplicidad a escala corriente $n(t)$ es **huérfano de orden $\varepsilon$** si $\beta^2>(1+\varepsilon)\,2n(t)^2\,|t|$. (Con GAP-177.A probado, la constante mejora a $c(n(t))\approx 8n(t)$.)

**[TEOREMA 177.10] (dicotomía de huérfanos; condicional solo a la hipótesis de separación del Thm 177.6 en el tramo $(t,0)$).**
1. **(RH ⟹ sin huérfanos.)** Si $Z_0$ es real y en $(t,0)$ la dinámica backward está definida con clusters admisibles (separación a escala corriente, §2.2), todo par no-real a tiempo $t$ despegó de un cluster progenitor de $n(t)$ ceros reales en su ventana y satisface $\beta(t)^2\le2n(t)^2|t|\,(1+C\varepsilon)$: no hay huérfanos de orden $>C\varepsilon$. El progenitor es localizable: un grupo de gaps con $g\lesssim\sqrt{2n^2|t|}$ en la configuración real.
2. **(¬RH-finito ⟹ huérfanos en todo $t\to0^-$.)** Si $0<I(0)<\infty$ con $m\ge1$ cuádruplos heredados de alturas $b_j$, entonces para $|t|<\dfrac{b_{\max}^2}{4\,n(t)^2}$ el cuádruplo más alto es huérfano de orden $\ge1$: su altura backward cumple $\beta(t)^2\ge b_{\max}^2>2\,n(t)^2|t|\cdot2$, inalcanzable desde cualquier progenitor local. Como $n(t)\le\max(2,C\rho\sqrt{|t|})$, la ventana de detección es $|t|\lesssim\min\bigl(b_{\max}^2,\;\rho^{-2}\bigr)$: no vacía.
3. En consecuencia, módulo la hipótesis de separación: **¬RH-con-$I$-finito $\iff$ existen huérfanos a todo $t<0$ suficientemente pequeño**, y la mitad aritmética del puente backward es el censo de progenitores = función de concentración de gaps $\nu(\delta,T)$ de la configuración real — con el umbral corregido $\delta\asymp\sqrt{2n^2|t|}$ (no $\sqrt{8|t|}$: el censo debe contar **clusters ponderados cuadráticamente**, no gaps individuales).

*Prueba.* (1) es el Teorema 177.6 con $I_W(t^*)=0$ en el despegue $t^*\in(t,0)$, más fusión monótona (§2.2). (2): $\beta_{\max}(t)^2\ge\beta_{\max}(0)^2=b_{\max}^2$ no vale cero a cero (alturas individuales no monótonas), pero sí para el máximo: $M(t)\ge M(0)+2|t|\ge b_{\max}^2$ (Lema 174.3 backward); el portador de $M$ es el huérfano. (3): juntar (1)+(2) con la definición. $\square$

**Qué cambia respecto del Doc 174 §2.3:** la lógica sobrevive intacta; cambian (a) la constante del umbral ($2n^2$ probado; $8n$ conjetural-Hermite; nunca $2k$), (b) la escala de la ventana del censo, (c) y — lo más importante — la **ruta forward del §4 es estrictamente más económica** que este censo backward: requiere de la aritmética solo LP-134 en vez de $\nu(\delta,T)$ completa. El backward queda como caracterización conceptual (qué *es* ¬RH-finito dinámicamente: huérfanos); el forward como ruta de prueba.

---

## 6. Test anti-circularidad

| Objeto | ¿RH-libre? | ¿ζ-libre? | Dónde reentra ζ |
|---|---|---|---|
| Thm 177.1 (Hermite exacto, $c(n)$), Prop 177.2 (refutación de $2k$), Prop 177.5 (apilamiento cerrado) | sí | sí | no reentra |
| Lema 177.4 (mar), Thm 177.6 (cota $2n^2$), Thm 177.10 (huérfanos) | sí | sí (clase + RvM) | no reentra |
| Thm 177.7 / Cor 177.8 | sí | **no**: Lema 177.B es sobre la $H_t$ aritmética; LP-134 es ζ | ζ entra por (i) regularización difusiva de $H_t$ en $t>0$ y (ii) repulsión LP-134 en $t=0$ — dos entradas separadas y mínimas |
| GAP-177.A (extremalidad de Hermite) | sí | sí | no reentra; es dinámica de partículas pura |

Sin primos en ninguna prueba. El patrón de los Docs 167/174 se mantiene: la ley es ζ-libre; la aritmética entra por la condición inicial — y este documento la reduce a su forma mínima conocida (LP-134 + un lema de interior).

---

## 7. Veredicto

**GAP-174.B: REFUTADO en su constante, PROBADO-PARCIAL en su estructura.**

1. **[TEOREMA 177.1 + PROP 177.2] (modelo local resuelto; refutación de la constante).** El despegue múltiple desde una casi-colisión de $n$ ceros reales es exactamente autosimilar-Hermite: alturas $2\sqrt{|t-t_{\rm col}|}\,h_j$, $h_j$ = ceros de $H_n$, y $\beta_{\max}^2=c(n)|t-t_{\rm col}|$ con $c(n)=4h_{\max}(n)^2=8n+4-2^{8/3}|a_1|(2n+1)^{1/3}+O(n^{-1/3})$; tabla exacta $c(2)=2$, $c(3)=6$, $c(4)=2(3+\sqrt6)$, $c(5)=2(5+\sqrt{10})$. La constante $2k$ del enunciado original es falsa desde $n=3$ (factor asintótico 8): la heurística del Doc 174 ignoraba que backward los ceros del mismo lado empujan hacia arriba (apilamiento).
2. **[TEOREMA 177.6 + PROP 177.5] (cota global probada, con hipótesis de separación a escala corriente).** Incondicionalmente en la clase: $\beta_{\max}(\sigma)^2\le I_W(\sigma)\le2n^2\sigma(1+C\varepsilon)$ para clusters admisibles, con fusión backward monótona (superaditividad) y mar lejano controlado ($O(\rho)$, absolutamente convergente). El apilamiento acelera pero nunca excede la ley del cluster fusionado (solución cerrada del cuarteto vertical: el par superior roba el $90.8\%$ de la energía y satura exactamente $c(4)\sigma$). Queda **[GAP-177.A]**: bajar de $2n^2$ a $c(n)\approx8n$ en general (extremalidad de Hermite) — deseable pero **no necesario** para la lógica de huérfanos ni para el Cor 177.8.
3. **[TEOREMA 177.10] (huérfanos, cerrado módulo separación):** ¬RH-con-$I$-finito ⟺ pares huérfanos backward, con umbral $2n(t)^2|t|$ y censo de progenitores cuadráticamente ponderado.
4. **[TEOREMA 177.7 + COR 177.8] (el hallazgo de mayor valor: la ruta forward es más fuerte).** Cada aterrizaje crea un casi-doble del lado real; con el **[LEMA-MÍNIMO 177.B]** (KKL cuantitativo: gaps normalizados de $H_t\ge ct^\theta$, $\theta<\tfrac12$, a alturas $\ge\exp(t^{-(1/2-\theta)})$ — exactamente el régimen de relajación difusiva, [GAP de literatura]: no localizado en KKL/P15/RT), los aterrizajes solo acumulan en $t=0^+$ con alturas superexponenciales y $b_j\le(\log\gamma_j)^{-1-\eta}$; y **177.B $\wedge$ LP-134 $\Rightarrow m<\infty$**. La mitad aritmética del puente baja de "estadística completa de gaps de ζ" a "una repulsión polilogarítmica del eje (LP-134)". Doble consistencia verificada contra el contraejemplo del Doc 144/174 (viola LP-134 y vive bajo el umbral $\Gamma$: ambas piezas necesarias, ninguna redundante).

**Dirección para Phase 56:** (a) atacar el Lema 177.B con las técnicas de [RT §2]/[P15] (relajación local del gas en $t>0$, uniforme en la esquina difusiva) — es dinámica de $H_t$, no aritmética de ζ; (b) GAP-177.A por desigualdad de reordenamiento sobre el gas log (extremalidad del equilibrio de Hermite); (c) revisar si LP-134 admite una forma en promedio suficiente para el Cor 177.8 (el argumento usa solo $j$ grande a lo largo de la sucesión de cuádruplos: bastaría LP-134 en densidad 1).

### Referencias
de Bruijn, N.G. (1950), *The roots of trigonometric integrals*, Duke Math. J. 17, 197–226 (§2: representación gaussiana; Thm 13: banda decreciente). — Csordas, G., Smith, W., Varga, R.S. (1994), *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10, 107–129 (casi-dobles en $t=0$ ⟹ cotas inferiores de Λ: la versión aritmética estática del pliegue forward). — Ki, H., Kim, Y.-O., Lee, J. (2009), *On the de Bruijn–Newman constant*, Adv. Math. 222, 281–306 (Λ<1/2; $\forall t>0$ finitos ceros no reales, eventualmente reales y simples; regularización asintótica del espaciado para $t>0$ fijo — **la uniformidad cuantitativa en $t\to0^+$ que pide el Lema 177.B no está enunciada allí hasta donde sabemos: [GAP de literatura]**). — Rodgers, B., Tao, T. (2020), *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8, e6 (Λ≥0 vía: $\Lambda<0$ forzaría equiespaciado local de los ceros de ζ, contra estimaciones incondicionales de fluctuación). — Polymath, D.H.J. (2019), Res. Math. Sci. 6, 31. — Szegő, G. (1939), *Orthogonal Polynomials*, AMS Colloq. Publ. 23 ((5.5.7); §6.32: cotas y asintótica Plancherel–Rotach de los ceros de Hermite). — Plancherel, M., Rotach, W. (1929), Comment. Math. Helv. 1, 227–254. — La identidad "calor sobre polinomios = movimiento Calogero racional de raíces" y la autosimilaridad de Hermite son folklore (cf. exposiciones de Tao en torno a [RT]); el uso aquí (constante de despegue $c(n)$, cuarteto apilado cerrado, cota término a término $2n^2$, soldadura 177.B∧LP-134⟹m<∞) no lo conocemos publicado. — Docs internos: 144, 167, 168, 170, 174.
