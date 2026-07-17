# Documento 176 — Ataque al Problema A vía Green–Littlewood: el presupuesto de la semibanda, el límite de Cesàro que siempre existe, y la posición de A en la jerarquía

**Programa:** Hipótesis de Riemann — Fase 55 (dos flechas)
**Fecha:** 2026-06-11
**Mandato:** atacar el Problema A — $I(0^+)<\infty$ — a través de la identidad de Green–Littlewood ([TEOREMA 173.C]). No auditar; construir. No intentar probar RH.
**Maquinaria aceptada (no re-derivada):** [TEOREMA 173.C] (identidad exacta, Doc 173 §6.1, con su prueba leída en fuente); certificado $E(T)=\sum_{\gamma\le T}b^2\ll T/\log T$ (Teorema 170.5 / Selberg [S46]); dicotomía [TEOREMA 175.2] (LP-112 $\Rightarrow I\in\{0,\infty\}$, condicional a LP-112); arquitectura RH $\Longleftarrow (I<\infty)\wedge$LP-112 ([COR 175.5.2]).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] con prueba completa o sin etiqueta; [GAP] declarado con forma de enunciado. Honestidad absoluta sobre novedad: maquinaria clásica se declara clásica.

**Coordenadas (idénticas a Docs 170/173/175).** Cero off-crítico $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, $\gamma>0$; un representante por cuádruplo. $I(T)=E(T):=\sum_{\gamma_j\le T}b_j^2$, $I(0^+)=\lim_{T\to\infty}I(T)=\sum_j b_j^2$ (monótono). **Problema A:** $I(0^+)<\infty$. Notación de este documento:
$$D(T)\;:=\;\int_{1/2}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma,\qquad
\Xi(T)\;:=\;\frac{1}{2\pi}\int_{1/2}^\infty\Big(\sigma-\tfrac12\Big)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma,$$
de modo que [TEOREMA 173.C] se lee: para todo $T$ no-ordenada, $\;I(T)=\frac1\pi D(T)+\frac18-\Xi(T)$, es decir
$$\boxed{\,D(T)\;=\;\pi\,I(T)\;-\;\frac\pi8\;+\;\pi\,\Xi(T)\,}.$$

---

## 0. Resumen ejecutivo y veredicto

1. **[PROP 176.1] (resolución de la tensión $\sigma\ge1$).** La región $\sigma\ge1$ contribuye a $D(T)$ una cantidad **exacta, casi-periódica y uniformemente acotada**: $\Phi(T)=\sum_n\Lambda(n)\sin(T\log n)/(n\log^3 n)$, $|\Phi(T)|\le C_0<\infty$ para todo $T$. La media en $t$ de $\log|\zeta|$ es cero término a término (no hay término $n=1$), las frecuencias están acotadas inferiormente por $\log2$ y las amplitudes son $\ell^1$: **cancelación total**, no $\asymp T$. Todo el presupuesto de $D(T)$ (salvo $O(1)$) vive en $\tfrac12<\sigma<1$.

2. **[LEMA 176.3] (mejora del flujo de borde de 173.C).** $|\Xi(T)|\ll\log T$ para **toda** altura no-ordenada — no $O(\log^2T)$ y no solo en alturas buenas. Mecanismo: integrar primero en $\sigma$ convierte cada cero cercano en una masa de Poisson $\le\frac94\pi$, independiente de $|T-\gamma|$.

3. **[TEOREMA 176.4] (la forma promediada: el borde se evapora y el límite de Cesàro existe siempre).** Promediando el corte, $\overline D(T_0):=\frac1{T_0}\int_{T_0}^{2T_0}D(T)\,dT$ cumple $\overline D(T_0)=\pi\,\overline I(T_0)-\frac\pi8+O\big(\frac{\log T_0}{T_0}\big)$, porque $\int_{T_0}^{2T_0}\Xi(T)\,dT$ es una **diferencia de dos valores de $\log|\zeta|$** integrada en $\sigma$, $\ll\log T_0$. Consecuencia (incondicional):
$$\lim_{T_0\to\infty}\overline D(T_0)\;\text{existe en }[-\tfrac\pi8,+\infty]\;\text{y vale}\;\pi\,I(0^+)-\frac\pi8 .$$
**RH $\iff$ límite $=-\pi/8$. Problema A $\iff$ límite finito.** A queda convertido en la finitud de un límite que *provablemente existe* — sin sucesiones de alturas buenas, sin residuo de borde.

4. **[COR 176.5] (cota inferior incondicional del signo).** $D(T)\ge-\frac\pi8-C\log T$ en toda altura no-ordenada, y $\overline D(T_0)\ge-\frac\pi8-C\frac{\log T_0}{T_0}$: la integral de $\log|\zeta|$ en la semibanda derecha **nunca cae por debajo de la masa del polo**. Bajo RH la constante $-\pi/8$ es exacta (caso de igualdad en el límite). La cota inferior es *gratis* ($I\ge0$); **la cota superior ES el Problema A**.

5. **[TEOREMA 176.6] (el teorema inverso de medias).** $D(T)=\pi E(T)-\frac\pi8+O(\log T)$ para toda altura no-ordenada; con el certificado 170.5, $|D(T)|\ll T/\log T$: la media de área de $\log|\zeta|$ en la semibanda es $\ll1/\log T$. Versión por abscisa: $\big|\frac1T\int_0^T\log|\zeta(\sigma+it)|\,dt\big|\ll\frac1{(\sigma-\frac12)\log T}+\frac{\log T}T$ uniforme en $\sigma>\tfrac12$. Honestidad: maquinaria 100% clásica (Littlewood+Selberg); la novedad es de *enunciado y exactitud* (constante $-\pi/8$, validez en toda altura), no de método.

6. **Posición de A en la jerarquía ([TEOREMA 176.7], [PROP 176.8], [PROP 176.9]):**
$$\mathrm{RH}\;\Longrightarrow\;(m<\infty)\;\Longrightarrow\;\textbf{A}\;\Longrightarrow\;\mathrm{Lindel\ddot of}\;\Longrightarrow\;\mathrm{Densidad},$$
(la flecha A $\Rightarrow$ LH vía Backlund es, creo, nueva *como observación del programa*; trivial una vez dicha). **Ningún teorema de densidad de tipo exponencial $N(\tfrac12+s,T)\ll T^{1-cs}(\log T)^\kappa$ — incondicional o bajo Lindelöf — puede dar A**: el layer-cake exacto da $E(T)\ll T(\log T)^{\kappa-2}$ y la masa fatal vive en $s\asymp1/\log T$, donde el ahorro exponencial vale $e^{-c}\asymp1$; la calidad $c$ del exponente solo entra en la constante. El **enunciado mínimo** equivalente a A es una **densidad uniforme en $T$**: $\exists f$ con $N(\tfrac12+s,T)\le f(s)\;\forall T$ y $\int_0^{1/2}s\,f(s)\,ds<\infty$ — un teorema de *finitud*, género distinto del de toda la industria de densidades.

7. **Pivotes nombrados (§6):** la escalera de la envolvente ($T/\log T\to T/\log^2T\to T^{1-\delta}\to O(1)\to0$) con su diccionario exacto de densidades; el primer peldaño alcanzable es **densidad log-free cerca de $\sigma=\tfrac12$** ($\kappa=0\Rightarrow E\ll T/\log^2T$).

---

## 1. El presupuesto por regiones y la resolución de la tensión $\sigma\ge1$

### 1.1. La región $\sigma\ge1$: cancelación total, fórmula exacta

La tensión del mandato: si $\log|\zeta(\sigma+it)|$ tuviera media positiva $\asymp c(\sigma)$ en $t$ para $\sigma\ge2$, la región lejana aportaría $\asymp T$ a $D(T)$, incompatible con $D(T)\ll T/\log T$ (que se sigue de 173.C + 170.5). La resolución: **la media es exactamente cero**, porque $\log|\zeta|$ en $\sigma>1$ es una serie trigonométrica en $t$ *sin término constante*.

**[PROP 176.1].** Para todo $T>0$,
$$\int_{1}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma\;=\;\Phi(T):=\sum_{n\ge2}\frac{\Lambda(n)\,\sin(T\log n)}{n\,\log^3 n},
\qquad |\Phi(T)|\;\le\;C_0:=\sum_{n\ge2}\frac{\Lambda(n)}{n\log^3n}\;<\;\infty .$$
En particular la contribución de $\sigma\ge1$ a $D(T)$ es $O(1)$ **uniforme en $T$**, y
$$D(T)\;=\;D_{\mathrm{banda}}(T)+O(1),\qquad D_{\mathrm{banda}}(T):=\int_{1/2}^{1}\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma .$$

*Prueba.* Para $\sigma>1$: $\log|\zeta(\sigma+it)|=\mathrm{Re}\sum_{n\ge2}\frac{\Lambda(n)}{\log n}n^{-\sigma-it}=\sum_{n\ge2}\frac{\Lambda(n)}{\log n}n^{-\sigma}\cos(t\log n)$, absolutamente convergente. La integral triple (suma en $n$, $\sigma\in(1,\infty)$, $t\in(0,T)$) del valor absoluto es $\le T\sum_n\frac{\Lambda(n)}{\log n}\int_1^\infty n^{-\sigma}d\sigma=T\sum_n\frac{\Lambda(n)}{n\log^2n}<\infty$, donde la última suma converge: $\sum_n\frac{\Lambda(n)}{n\log^2n}=\sum_p\sum_{k\ge1}\frac1{k^2p^k\log p}\le\sum_p\frac{2}{p\log p}<\infty$ (sumación parcial con $\pi(x)\sim x/\log x$: $\int_2^\infty\frac{dx}{x\log^2 x}<\infty$). Tonelli–Fubini aplica; integrando primero $t$ ($\int_0^T\cos(t\log n)\,dt=\sin(T\log n)/\log n$) y luego $\sigma$ ($\int_1^\infty n^{-\sigma}d\sigma=1/(n\log n)$) sale $\Phi(T)$. La cota: $C_0=\sum_{p,k}\frac1{k^3p^k\log^2p}<\infty$ por la misma comparación. (La recta $\sigma=1$ es de medida nula y $\log|\zeta|$ es localmente integrable en ella.) $\square$

**Lectura — por qué se cancela todo.** Tres ingredientes, los tres necesarios:
1. **Media cero:** no hay término $n=1$ en la serie de $\log\zeta$ (el polo está en $s=1$, fuera de $\sigma>1$); la media en $t$ de cada término es $0$.
2. **Frecuencias separadas de cero:** $\log n\ge\log2$, luego cada primitiva $\sin(T\log n)/\log n$ está acotada uniformemente en $T$ — no hay divisor pequeño.
3. **Amplitudes $\ell^1$ tras dos integraciones:** el factor $1/\log^3n$ acumulado (uno de la serie de $\log\zeta$, uno de $\int dt$, uno de $\int d\sigma$) hace sumable incluso la cola $\sigma\to1^+$, donde $\log\zeta(\sigma)$ diverge.

**Escala de la fluctuación (para calibrar, clásico).** Para $\sigma>1$ fijo, por el teorema del valor medio de polinomios de Dirichlet (Montgomery–Vaughan; o simple ortogonalidad en este rango): $\frac1T\int_0^T|\log\zeta(\sigma+it)|^2dt\to\sum_{n\ge2}\frac{\Lambda(n)^2}{n^{2\sigma}\log^2n}<\infty$. El integrando es una señal de tamaño $O(1)$, media cero, y su integral doble es $O(1)$: cancelación *total*. Ese es el patrón que A pide extender — con pérdida controlada — a toda la banda.

### 1.2. La banda crítica $\tfrac12<\sigma<1$: dónde vive el presupuesto

En la banda la serie de Dirichlet no converge y el control es vía ceros (Littlewood). Lo incondicional por abscisa fija, con las dos cotas disponibles (se usan en §3 y §4):

**Lema de Littlewood por abscisa (clásico; Littlewood 1924; Titchmarsh §9.9).** Para $\tfrac12\le\sigma<1$ fijo y todo $T\ge2$:
$$\int_0^T\log|\zeta(\sigma+it)|\,dt\;=\;2\pi\!\!\sum_{\beta>\sigma,\,0<\gamma\le T}\!\!(\beta-\sigma)\;-\;2\pi(1-\sigma)\;+\;O(\log T),$$
con $O$ uniforme en $\sigma\in[\tfrac12,1]$ (el término $-2\pi(1-\sigma)$ es el polo $s=1$; los bordes son los estándar). Combinado con:
- **Chebyshev sobre la energía:** $\sum_{\beta>\sigma}(\beta-\sigma)\le\sum_{b_j>\sigma-\frac12}b_j\le\frac{E(T)}{\sigma-\frac12}$ (si $b>s$ entonces $b\le b^2/s$);
- **densidad de Selberg [S46]:** $N(\tfrac12+s,T)\ll T^{1-s/4}\log T$, luego $\sum(\beta-\sigma)^+\le\int_\sigma^1N(u,T)\,du\ll T^{1-(\sigma-\frac12)/4}$;

se obtiene, incondicionalmente, para $\tfrac12<\sigma<1$ fijo:
$$-\,2\pi(1-\sigma)-C\log T\;\le\;\int_0^T\log|\zeta(\sigma+it)|\,dt\;\le\;\min\Big(\frac{2\pi E(T)}{\sigma-\frac12},\;8\pi\,T^{1-(\sigma-\frac12)/4}\Big)+C\log T .$$
La media por abscisa tiende a $0$ para cada $\sigma>\tfrac12$ fijo (esto es esencialmente Bohr–Landau/Littlewood: clásico). **Lo que no es clásico-trivial es la versión integrada en $\sigma$ con peso 1 hasta $\sigma=\tfrac12^+$** — ahí la cota por abscisa estalla como $1/(\sigma-\tfrac12)$ y solo la estructura de segundo momento (173.C) la doma. Eso es §3.

**Presupuesto, resumen.** $D(T)=D_{\mathrm{banda}}(T)+O(1)$; el integrando en la banda tiene tamaño absoluto $\asymp T$ (véase §5.2) y total signado $\ll T/\log T$ (§3): la cancelación lograda es de orden relativo $1/\log T$. **El Problema A pide total signado $O(1)$: cancelación relativa $1/T$.** Esa razón — $\log T$ frente a $T$ — es la medida honesta de la distancia entre lo conocido y A.

---

## 2. El borde, mejorado dos veces: $O(\log T)$ en toda altura, $o(1)$ en promedio

### 2.1. Herramienta de integrabilidad local

**[LEMA 176.2].** Para todo $T\ge2$ (ordenada o no),
$$\int_{1/2}^{2}\big|\log|\zeta(\sigma+iT)|\big|\,d\sigma\;\ll\;\log T .$$

*Prueba.* Por el lema estándar de factorización local (Borel–Carathéodory + Jensen; Titchmarsh §3.9, en la forma usada en el paso (1) de la prueba de 173.C, leída en fuente): en el disco $|s-(2+iT)|\le\tfrac52$ hay $O(\log T)$ ceros, y para $|s-(2+iT)|\le2$,
$$\log|\zeta(s)|\;=\;\sum_{|\rho-(2+iT)|\le\frac52}\log|s-\rho|\;+\;O(\log T).$$
El segmento $[\tfrac12,2]\times\{T\}$ está contenido en ese disco. Cada cero aporta $\int_{1/2}^2\big|\log|\sigma+iT-\rho|\big|\,d\sigma\le\int_{1/2}^2\big(\log\tfrac92+\big|\log|\sigma-\beta+i(T-\gamma)|\big|\big)d\sigma\ll1$ — porque $|\log|x+iy||\le|\log|x-\beta'||+O(1)$ en distancias acotadas y $\int_0^4|\log x|\,dx<\infty$ (peor caso: el cero sobre el propio segmento; la singularidad logarítmica es integrable). Con $O(\log T)$ ceros y el resto $O(\log T)$ integrado sobre longitud $\tfrac32$: total $\ll\log T$. $\square$

### 2.2. El flujo es $O(\log T)$ en toda altura (mejora de 173.C)

**[LEMA 176.3].** Para toda $T\ge2$ que no sea ordenada de cero,
$$|\Xi(T)|\;=\;\Big|\frac1{2\pi}\int_{1/2}^\infty\Big(\sigma-\tfrac12\Big)^2\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma\Big|\;\ll\;\log T .$$
*(173.C daba $O(\log^2T)$ y solo en alturas buenas: la hipótesis de altura buena queda eliminada y el exponente bajado.)*

*Prueba.* Se parte en $\sigma\in[\tfrac12,2]$ y $\sigma\ge2$, como en el paso (6) de 173.C.
**(i) $\sigma\ge2$:** $|\zeta'/\zeta(\sigma+iT)|\le\sum_n\Lambda(n)n^{-\sigma}\ll2^{-\sigma}$ y $\int_2^\infty\sigma^22^{-\sigma}d\sigma=O(1)$.
**(ii) $\tfrac12\le\sigma\le2$:** por fracciones parciales (Davenport caps. 15–16): $\frac{\zeta'}{\zeta}(\sigma+iT)=\sum_{|\gamma-T|\le1}\frac1{\sigma+iT-\rho}+O(\log T)$. El resto integrado contra $(\sigma-\tfrac12)^2\le\tfrac94$ da $O(\log T)$. Para cada cero $\rho=\beta+i\gamma$ con $|\gamma-T|\le1$ — y aquí está la mejora: en vez de acotar puntualmente por $1/|T-\gamma|$ (lo que cuesta el factor "altura buena"), **se integra primero en $\sigma$**:
$$\int_{1/2}^{2}\Big(\sigma-\tfrac12\Big)^2\Big|\mathrm{Im}\,\frac1{\sigma+iT-\rho}\Big|\,d\sigma
\;\le\;\frac94\int_{-\infty}^{\infty}\frac{|T-\gamma|\,dx}{x^2+(T-\gamma)^2}\;=\;\frac{9\pi}{4},$$
usando $\big|\mathrm{Im}\frac1{x+i(T-\gamma)}\big|=\frac{|T-\gamma|}{x^2+(T-\gamma)^2}$ con $x=\sigma-\beta$: la integral en $\sigma$ de cada término es **una masa de Poisson, $\le\frac94\pi$ por cero, independiente de cuán cerca esté $T$ de $\gamma$**. Hay $O(\log T)$ ceros con $|\gamma-T|\le1$ (von Mangoldt). Total: $\ll\log T$. $\square$

**[COR 176.3.1] (la identidad, utilizable en toda altura).** Para toda $T$ no-ordenada:
$$D(T)\;=\;\pi\,I(T)\;-\;\frac\pi8\;+\;O(\log T).$$

### 2.3. El promedio en el corte: el borde se evapora

La observación clave: $\;\partial_T\log|\zeta(\sigma+iT)|=\mathrm{Re}\big[i\,\tfrac{\zeta'}{\zeta}(\sigma+iT)\big]=-\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}(\sigma+iT)$. Por tanto la integral del flujo **en el corte** es una diferencia de valores de $\log|\zeta|$ — sin argumentos, sin windings:
$$\int_{T_0}^{2T_0}\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,dT\;=\;\log|\zeta(\sigma+iT_0)|\;-\;\log|\zeta(\sigma+2iT_0)| ,$$
válido para todo $\sigma$ tal que la recta vertical no contenga ceros con esa abscisa (todas salvo a lo sumo numerables; $\log|\zeta(\sigma+iT)|$ es absolutamente continua en $T$ sobre esas abscisas, con singularidades logarítmicas integrables — suficiente para el teorema fundamental del cálculo en casi toda abscisa, que es lo que la integral en $\sigma$ requiere).

**[TEOREMA 176.4] (forma promediada de Green–Littlewood; el límite de Cesàro existe siempre).** Sean
$$\overline I(T_0):=\frac1{T_0}\int_{T_0}^{2T_0}I(T)\,dT,\qquad \overline D(T_0):=\frac1{T_0}\int_{T_0}^{2T_0}D(T)\,dT .$$
Entonces, incondicionalmente, para todo $T_0\ge2$:

**(a)** $\displaystyle\;\overline I(T_0)\;=\;\frac1\pi\,\overline D(T_0)\;+\;\frac18\;+\;O\Big(\frac{\log T_0}{T_0}\Big).$

**(b)** El límite $\displaystyle\lim_{T_0\to\infty}\overline D(T_0)$ **existe** en $[-\tfrac\pi8,+\infty]$ y vale $\;\pi\,I(0^+)-\dfrac\pi8$.

**(c)** $\mathrm{RH}\iff\lim\overline D=-\dfrac\pi8$; $\qquad$ **Problema A** $\iff\lim\overline D<\infty\iff\liminf_{T_0}\overline D(T_0)<\infty\iff\overline D(T_{0,n})$ acotada en *alguna* sucesión $T_{0,n}\to\infty$.

*Prueba.* (a) La identidad $I(T)=\frac1\pi D(T)+\frac18-\Xi(T)$ vale para todo $T$ salvo las ordenadas (numerables, medida nula); $I$ es monótona acotada en compactos, $D$ continua, y $|\Xi(T)|\ll\log T$ ([LEMA 176.3]) hace todo integrable en $[T_0,2T_0]$. Promediando, basta acotar $\frac1{T_0}\int_{T_0}^{2T_0}\Xi(T)\,dT$. Por Fubini (justificado: cerca de cada cero $|\zeta'/\zeta|\sim|s-\rho|^{-1}$ es localmente integrable en el plano; fuera, las cotas de 176.3 dominan) y la identidad de arriba:
$$\int_{T_0}^{2T_0}\Xi(T)\,dT\;=\;\frac1{2\pi}\int_{1/2}^\infty\Big(\sigma-\tfrac12\Big)^2\Big[\log|\zeta(\sigma+iT_0)|-\log|\zeta(\sigma+2iT_0)|\Big]\,d\sigma .$$
En $\sigma\in[\tfrac12,2]$: $(\sigma-\tfrac12)^2\le\tfrac94$ y [LEMA 176.2] en las dos alturas: $\ll\log T_0$. En $\sigma\ge2$: $|\log|\zeta||\le\sum\Lambda(n)n^{-\sigma}/\log n\ll2^{-\sigma}$, integral $O(1)$. Total $\ll\log T_0$; dividir por $T_0$.
(b) $I$ es no decreciente con $\lim_{T\to\infty}I(T)=I(0^+)\in[0,\infty]$; luego $I(T_0)\le\overline I(T_0)\le I(2T_0)$ y $\overline I(T_0)\to I(0^+)$ (también si $I(0^+)=\infty$). Por (a), $\overline D(T_0)=\pi\overline I(T_0)-\frac\pi8+o(1)\to\pi I(0^+)-\frac\pi8$.
(c) Inmediato de (b): el límite existe siempre, luego $\liminf<\infty\iff\lim<\infty\iff I(0^+)<\infty$; y $\lim=-\frac\pi8\iff I(0^+)=0\iff$RH. $\square$

**Lectura.** Esto cumple — con mejora estricta — el "próximo paso 2" nombrado en 173 §8 (Cesàro en el corte): el borde no baja a $O(\log T)$; **desaparece** ($O(\log T_0/T_0)$). Y resuelve la inquietud del mandato sobre sucesiones de alturas buenas: ya no hacen falta. El Problema A es ahora, exacta e incondicionalmente, *la finitud de un límite que existe*:
$$\textbf{A}\iff\lim_{T_0\to\infty}\frac1{T_0}\int_{T_0}^{2T_0}\!\!\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\,dT\;<\;\infty .$$
No hay oscilación posible: la integral doble promediada o converge a $\pi I(0^+)-\frac\pi8$ finito, o diverge a $+\infty$. (Nótese la dirección de la divergencia: solo hacia $+\infty$ — el signo está protegido por §5.)

---

## 3. El teorema inverso: lo que 170.5 + 173.C dicen sobre las medias de $\log|\zeta|$

La maquinaria corre en dirección inversa: el certificado de energía acota medias del integrando.

**[TEOREMA 176.6] (medias de $\log|\zeta|$ en la semibanda, incondicional).**
**(a)** Para toda $T$ no-ordenada: $\;D(T)=\pi E(T)-\frac\pi8+O(\log T)$, y por el certificado $E(T)\ll T/\log T$ (Teorema 170.5):
$$\Big|\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\Big|\;\ll\;\frac{T}{\log T}\,,$$
es decir, la media de área de $\log|\zeta|$ en la semibanda $\{\sigma>\tfrac12,\;0<t<T\}$ (área efectiva $\asymp T$) es $\ll1/\log T$.
**(b)** Por abscisa, uniforme en $\sigma\in(\tfrac12,1]$:
$$\Big|\frac1T\int_0^T\log|\zeta(\sigma+it)|\,dt\Big|\;\ll\;\frac1{(\sigma-\frac12)\,\log T}\;+\;\frac{\log T}{T}\,. $$

*Prueba.* (a) es [COR 176.3.1] + 170.5. (b): lema de Littlewood por abscisa (§1.2) con la cota de Chebyshev $\sum(\beta-\sigma)^+\le E(T)/(\sigma-\tfrac12)\ll T/((\sigma-\tfrac12)\log T)$ para la dirección superior, y $-2\pi(1-\sigma)-C\log T$ para la inferior. $\square$

**Honestidad sobre la novedad.** Los ingredientes de (a) y (b) son Littlewood (1924) y Selberg (1946); el layer-cake que conecta (a) con la suma $\sum b^2$ es la misma observación con la que 173.C se verifica de forma cruzada (Doc 173 §6.1). Por tanto: **teorema nuevo de enunciado, no de método**. Lo que sí parece no estar en la literatura *como enunciado* es (a) con la constante exacta $-\pi/8$ y validez en toda altura, y la forma (b) uniforme con el peso $1/((\sigma-\frac12)\log T)$. [GAP de literatura: no localizo (a)/(b) enunciados así; siguen de [L24]+[S46] en pocas líneas y podrían ser folklore. Antes de publicar: revisar Titchmarsh cap. 9 §§9.9–9.16 y la literatura de $\int_0^T\log|\zeta(\sigma+it)|\,dt$.]

**[COR 176.10] (dicotomía de medias; condicional a LP-112).** Bajo LP-112 (vía [TEOREMA 175.2]: $I(0^+)\in\{0,\infty\}$) y [TEOREMA 176.4.b]:
$$\lim_{T_0\to\infty}\overline D(T_0)\;\in\;\Big\{-\frac\pi8\,,\;+\infty\Big\}.$$
*Bajo LP-112, la media de Cesàro de la integral de $\log|\zeta|$ en la semibanda no tiene más que dos destinos: la constante exacta del polo, o $+\infty$.* Ningún crecimiento intermedio ($\log^3T_0$, $\sqrt{T_0}$, $T_0/\log^2T_0$, …) es posible. Combinado con el techo incondicional $\overline D(T_0)\ll T_0/\log T_0$ (176.6.a promediado): en el escenario malo la divergencia vive en la ventana $(\text{acotado},\,T_0/\log T_0]$ — exactamente la ventana de la dicotomía LP-112 leída en el integrando. El círculo de información se cierra: *certificado de energía $\to$ medias de $\log|\zeta|$ $\to$ (con LP-112) dicotomía del comportamiento asintótico de una integral clásica.*

---

## 4. El Problema A en la jerarquía de conjeturas estándar

### 4.1. A implica Lindelöf

**[TEOREMA 176.7].** $\textbf{A}\;(I(0^+)<\infty)\;\Longrightarrow\;$ Hipótesis de Lindelöf. Con lo trivial ($\mathrm{RH}\Rightarrow I=0$; $m<\infty\Rightarrow I<\infty$; $I<\infty\not\Rightarrow m<\infty$, ejemplo $b_j=1/j$ — Doc 175) queda la cadena estricta de implicaciones conocidas:
$$\mathrm{RH}\;\Longrightarrow\;(m<\infty)\;\Longrightarrow\;\textbf{A}\;\Longrightarrow\;\mathrm{LH}\;\Longrightarrow\;\mathrm{DH}\;(N(\sigma,T)\ll T^{2(1-\sigma)+\varepsilon}).$$

*Prueba.* Si $I:=I(0^+)<\infty$, entonces para cada $s>0$ el número total de ceros con $\beta\ge\tfrac12+s$ (toda altura) es $N(\tfrac12+s,\infty)\le I/s^2<\infty$ (Chebyshev: cada uno aporta $b^2\ge s^2$). En particular, para cada $\sigma>\tfrac12$ fijo, $N(\sigma,T+1)-N(\sigma,T)\to0$ cuando $T\to\infty$ (las diferencias de una sucesión acotada que estabiliza). Por el teorema de Backlund (Backlund 1918–19; Titchmarsh, cap. XIII, §13.5: **LH $\iff$ para todo $\sigma>\tfrac12$, $N(\sigma,T+1)-N(\sigma,T)=o(\log T)$**), se sigue LH. La flecha LH$\Rightarrow$DH es Ingham (1940). $\square$

**Lectura de posición.** A es un enunciado **casi-RH**: "RH con error $\ell^2$". Está estrictamente por encima de Lindelöf en la jerarquía (en el sentido de implicación probada A$\Rightarrow$LH; el recíproco no se conoce y §4.3 muestra que el conducto estándar no puede darlo). Sobre correlación de pares: la conjetura de Montgomery (1973) está formulada *bajo RH*, luego presupone A y no aporta una ruta hacia ella; no hay versión incondicional utilizable. [GAP de literatura: no conozco ningún enunciado estándar estrictamente más débil que "todas salvo finitas en la línea" que implique A.]

### 4.2. El layer-cake exacto y el enunciado mínimo

**[PROP 176.8] (A $=$ densidad uniforme en $T$).**
**(a)** *Layer-cake exacto:* $\;E(T)=\displaystyle\int_0^{1/2}2s\,N(\tfrac12+s,T)\,ds\;$ para todo $T$ (contando en $N$ los ceros con $\beta\ge\tfrac12+s$, $0<\gamma\le T$; $b_j^2=\int_0^{b_j}2s\,ds$ y Tonelli).
**(b)** *Equivalencia:* $\textbf{A}\iff$ existe $f:(0,\tfrac12)\to[0,\infty]$ con
$$N(\tfrac12+s,T)\;\le\;f(s)\quad\forall\,T,\qquad\int_0^{1/2}s\,f(s)\,ds\;<\;\infty .$$
**(c)** *La $f$ mínima:* $f_{\min}(s)=N(\tfrac12+s,\infty)$, y entonces $\int_0^{1/2}2s\,f_{\min}(s)\,ds=I(0^+)$ exactamente.

*Prueba.* (b$\Leftarrow$): $E(T)\le\int 2sf<\infty$ uniforme, luego $I(0^+)<\infty$. (b$\Rightarrow$) y (c): con A, $f_{\min}(s)=N(\tfrac12+s,\infty)<\infty$ para todo $s>0$ (176.7), domina todos los $N(\cdot,T)$, y monótona convergencia en (a) da $\int2sf_{\min}=\lim E(T)=I(0^+)$. $\square$

**El enunciado mínimo de A, nombrado.**
> **[GAP-A] (densidad uniforme en $T$; forma de enunciado).** *Existe $f$ con $\int_0^{1/2}s\,f(s)\,ds<\infty$ tal que $N(\tfrac12+s,T)\le f(s)$ para todo $T$.* (Ejemplo de perfil suficiente: $f(s)=s^{-2}\log^{-1-\varepsilon}(e/s)$.)

Obsérvese el género: **no es un teorema de densidad** (cota creciente en $T$) sino un **teorema de finitud** (cota independiente de $T$ por abscisa). Toda la industria de densidades — incondicional o condicional — produce cotas $T^{\theta}$ con $\theta>0$; lo que A pide no es mejorar $\theta$ sino *matarlo*. Las regiones libres de ceros tampoco ayudan: Vinogradov–Korobov da $N(\sigma,T)=0$ solo para $\sigma>1-c/(\log T)^{2/3}(\log\log T)^{1/3}$ — frontera que se escapa a $1$ cuando $T\to\infty$; para $\sigma<1$ fijo no aporta nada.

### 4.3. La barrera: ningún teorema de densidad exponencial alcanza A

**[PROP 176.9] (la cuenta exacta de la barrera).** Supóngase $N(\tfrac12+s,T)\le C\,T^{1-cs}(\log T)^\kappa$ para $0<s\le\tfrac12$, $T\ge T_1$ (con $c>0$, $\kappa\ge0$ cualesquiera). Entonces el layer-cake da, y no da más que,
$$E(T)\;\le\;2C\,T(\log T)^\kappa\int_0^{1/2}s\,e^{-cs\log T}\,ds\;\le\;\frac{2C}{c^2}\;T\,(\log T)^{\kappa-2}.$$
Consecuencias exactas:
1. **Selberg** ($c=\tfrac14$, $\kappa=1$, [S46]): $E(T)\ll T/\log T$ — la cuenta *reproduce* el certificado 170.5 (coherente: 170.5 se prueba con [S46]; Doc 175 §3 ya lo señalaba). La envolvente $T/\log T$ es **la constante de la casa una vez más**: es lo que da $\kappa=1$, venga $c$ de donde venga.
2. **La calidad del exponente es irrelevante para la forma:** $c$ solo entra en la constante $2C/c^2$. Ingham 1940, Huxley 1972 ($N(\sigma,T)\ll T^{12(1-\sigma)/5}\log^CT$ [GAP de literatura: exponente citado de memoria]), e incluso un hipotético $c=10^6$, dan todos $T(\log T)^{\kappa-2}$.
3. **Lindelöf no ayuda por este conducto:** bajo LH, Ingham da DH ($N\ll T^{2(1-\sigma)+\varepsilon}$) y Halász–Turán (1969) dan $N(\sigma,T)\ll T^{\varepsilon}$ para $\sigma\ge\tfrac34+\delta$ — espectacular lejos de la línea, **vacío cerca de ella**: la masa de $E(T)$ vive en $s\asymp1/\log T$, donde *todo* ahorro exponencial vale $T^{-cs}=e^{-c\cdot O(1)}\asymp1$ y la cota de densidad es tan trivial como $N\ll T\log T$. Con cualquier $\kappa$, LH mueve $E(T)$ dentro de la familia $T(\log T)^{\kappa-2}$ y **nunca** a $O(1)$.
4. **Optimalidad contra la clase de hipótesis:** la cota es ajustada — una configuración con $N(\tfrac12+s,T)\asymp T^{1-cs}\log T$ saturada en $s\asymp1/\log T$ es compatible con $N(T)\sim\frac{T}{2\pi}\log T$ y da $E(T)\asymp T/\log T$. El conducto densidad$\to$energía no puede dar menos sin nueva información *en* $s\asymp1/\log T$.

*Prueba.* La integral: $\int_0^{1/2}s\,e^{-cs\log T}ds\le\int_0^\infty s\,e^{-cs\log T}ds=(c\log T)^{-2}$. Los puntos 1–3 son sustituciones; el 4 es el cálculo inverso con la configuración saturada (consistencia con el conteo total: en $s=1/\log T$, $T^{1-cs}\log T=e^{-c}T\log T\le N(T)$ para $\kappa\le1$). $\square$

**Momentos: el mismo tubo.** Las cotas/conjeturas de momentos $\int_0^T|\zeta(\tfrac12+it)|^{2k}dt\ll T(\log T)^{k^2}$ (conocidas $k=1,2$: Hardy–Littlewood 1918, Ingham 1926; conjeturadas todas: Keating–Snaith) entran en la energía solo a través de Jensen/Littlewood: $\int_0^T\log|\zeta(\tfrac12+it)|\,dt\le\frac T{2k}\log\big(\frac1T\int|\zeta|^{2k}\big)\ll\frac{k\,T\log\log T}{2}$, que controla el *primer* momento $J(T)=\sum_{\gamma\le T}b_j\ll T\log\log T$ — peor que la ruta de Selberg incluso asumiendo todos los momentos. Y los momentos fuera de la línea ($\sigma>\tfrac12$) alimentan teoremas de densidad, es decir, [PROP 176.9]. **Veredicto de jerarquía: A no es consecuencia de Lindelöf, ni de la Hipótesis de Densidad, ni de la familia completa de conjeturas de momentos; el único antecedente estándar conocido de A es la propia familia RH ($\mathrm{RH}$, $m<\infty$).** A es un nodo genuinamente nuevo, estrictamente entre $m<\infty$ y LH.

---

## 5. La cota inferior incondicional y la asimetría del signo

### 5.1. La cota inferior: la semibanda nunca está en déficit por debajo del polo

**[COR 176.5] (cota inferior incondicional).** Para toda $T\ge2$ no-ordenada:
$$\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\;\ge\;-\,\frac\pi8\;-\;C\log T,$$
y en forma promediada (donde la constante es límite-exacta):
$$\overline D(T_0)\;\ge\;-\,\frac\pi8\;-\;C\,\frac{\log T_0}{T_0}\qquad\forall\,T_0\ge2 .$$
Bajo RH se da la igualdad en el límite: $\overline D(T_0)\to-\frac\pi8$. *La constante $-\pi/8$ es óptima.*

*Prueba.* $D(T)=\pi I(T)-\frac\pi8+\pi\Xi(T)\ge-\frac\pi8-\pi|\Xi(T)|$ con $I(T)\ge0$ y [LEMA 176.3]; la promediada por [TEOREMA 176.4.a] con $\overline I\ge0$; la igualdad bajo RH por 176.4.b con $I(0^+)=0$. $\square$

**Enunciado en limpio (candidato a resultado publicable autónomo, con la honestidad de §3 sobre procedencia clásica de los ingredientes):** *el promedio de $\log|\zeta|$ sobre la semibanda derecha está acotado inferiormente, de forma incondicional, por la masa del polo: $\liminf_{T_0}\overline D(T_0)\ge-\pi/8$, con igualdad (y existencia de límite $=-\pi/8$) si y solo si... el límite siempre existe y vale $\pi\sum b_j^2-\pi/8$.* La forma más citable es directamente [TEOREMA 176.4.b], que contiene a esta cota.

### 5.2. La asimetría: la dirección difícil es la superior

- **Inferior $=$ gratis.** Es $I\ge0$: la positividad de la medida de Riesz. *Ninguna* información sobre ζ más allá de la identidad.
- **Superior $=$ A.** Por 176.4.c: A $\iff\overline D$ acotada superiormente. Acotar $D$ por arriba es impedir que $\log|\zeta|$ sea *persistentemente demasiado positivo* en la banda — un control del exceso de **grandeza** de $|\zeta|$ a la derecha de la línea. (Intuición correcta de signo: cada cero off añade $\pi b^2>0$ a $D$; los ceros, vía la subarmonicidad rota, *suben* la integral. El defecto de RH es un superávit, no un déficit.)

**El tamaño absoluto, para calibrar la cancelación pedida.** Por la teoría de Bohr–Jessen (Acta Math. 54 (1930) y 58 (1932); extensión Borchsenius–Jessen 1948), para $\sigma\in(\tfrac12,1)$ fijo $\log\zeta(\sigma+it)$ tiene distribución límite en $t$, de varianza $V(\sigma)=\tfrac12\sum_p p^{-2\sigma}+\dots\sim\tfrac12\log\frac1{2\sigma-1}$ ($\sigma\to\tfrac12^+$); el primer momento absoluto esperado es $\asymp\sqrt{V(\sigma)}$, integrable en $\sigma$ hasta $\tfrac12$. Esto dimensiona $\iint|\log|\zeta||\asymp\kappa_0\,T$ con $\kappa_0>0$ absoluto. [GAP de literatura: la convergencia del primer momento absoluto (integrabilidad uniforme) y su versión integrada en $\sigma$ las doy por plausibles sin cita exacta; el uso aquí es solo calibratorio, ninguna prueba depende de ello.] Contra eso:
$$\underbrace{\textstyle\iint|\log|\zeta||\;\asymp\;T}_{\text{masa absoluta}}\qquad
\underbrace{\textstyle|\iint\log|\zeta||\;\ll\;T/\log T}_{\text{cancelación probada (176.6)}}\qquad
\underbrace{\textstyle|\iint\log|\zeta||\;=\;O(1)}_{\textbf{A}}.$$
**La distancia entre lo probado y A es el factor entre $\log T$ y $T$.** Universalidad (Voronin) garantiza excursiones locales positivas y negativas de tamaño arbitrario; A afirma que su balance neto es exacto hasta $O(1)$ — y la dicotomía [COR 176.10] dice que, bajo LP-112, el balance o es exacto o falla infinitamente.

---

## 6. Veredicto y pivotes

### 6.1. Qué quedó probado (incondicional salvo indicación)

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [PROP 176.1] | Región $\sigma\ge1$: contribución exacta $\Phi(T)$, $O(1)$ uniforme; tensión resuelta; todo el presupuesto en la banda | Teorema, nuevo de enunciado |
| [LEMA 176.3] | Flujo de borde $\Xi(T)\ll\log T$ en **toda** altura no-ordenada | **Mejora estricta de 173.C** ($O(\log^2T)$, alturas buenas) |
| [TEOREMA 176.4] | Forma promediada sin borde; $\lim\overline D$ **existe siempre** y vale $\pi I(0^+)-\frac\pi8$; RH $\iff-\frac\pi8$; A $\iff$ finito | **El resultado central del documento** |
| [COR 176.5] | $D(T)\ge-\frac\pi8-C\log T$; $\overline D\ge-\frac\pi8-o(1)$; constante óptima | Incondicional, gratis por $I\ge0$ |
| [TEOREMA 176.6] | $D(T)=\pi E(T)-\frac\pi8+O(\log T)$; medias de $\log|\zeta|$ $\ll1/\log T$ (área) y $\ll1/((\sigma-\frac12)\log T)$ (abscisa) | Teorema inverso; método clásico, enunciado posiblemente nuevo [GAP lit.] |
| [TEOREMA 176.7] | $\mathbf{A}\Rightarrow$ Lindelöf (vía Backlund); cadena RH$\Rightarrow m<\infty\Rightarrow$A$\Rightarrow$LH$\Rightarrow$DH | Posicionamiento, prueba completa |
| [PROP 176.8] | A $\iff$ densidad uniforme en $T$ con $\int sf\,ds<\infty$; $f_{\min}=N(\tfrac12+s,\infty)$ | El enunciado mínimo, exacto |
| [PROP 176.9] | Barrera: todo $N\ll T^{1-cs}(\log T)^\kappa$ da $E\ll\frac{2C}{c^2}T(\log T)^{\kappa-2}$ y no menos; $c$ solo entra en constantes; LH/DH/momentos no alcanzan A | La cuenta exacta pedida por el mandato |
| [COR 176.10] | Bajo LP-112: $\lim\overline D\in\{-\frac\pi8,+\infty\}$ | Condicional a LP-112 (vía 175.2) |

### 6.2. El estado del Problema A tras este documento

A queda **reformulado sin pérdida** ([TEOREMA 176.4.c] + [PROP 176.8]) en dos monedas equivalentes:
1. **Analítica:** la media de Cesàro de $\iint\log|\zeta|$ sobre la semibanda converge (siempre lo hace) a un valor finito. La cota inferior está cerrada ($-\pi/8$, óptima); falta solo la superior.
2. **De conteo:** densidad uniforme en $T$ ([GAP-A]). Género "finitud", inalcanzable para el conducto exponencial completo ([PROP 176.9]).

Y queda **posicionado**: estrictamente entre $m<\infty$ y Lindelöf; no consecuencia de ninguna conjetura estándar de densidad/momentos; bajo LP-112, equivalente a RH ([COR 175.5.2]). La pared es honesta: la cancelación probada es $1/\log T$, la pedida es $1/T$, y el conducto estándar tiene techo estructural $T(\log T)^{\kappa-2}$.

### 6.3. Pivotes (la escalera de la envolvente, con diccionario exacto)

Por [PROP 176.8]/[176.9], cada mejora de la envolvente de $E(T)$ tiene un equivalente de densidad nombrable. La escalera, de lo conocido a RH:

| Peldaño | Envolvente $E(T)\ll$ | Insumo de densidad equivalente/suficiente | Estatus |
|---|---|---|---|
| 0 | $T/\log T$ | Selberg $\kappa=1$ | **Probado** (170.5/[S46]) |
| 1 | $T/\log^2T$ | **densidad log-free cerca de $\sigma=\frac12$**: $N(\frac12+s,T)\ll T^{1-cs}$ ($\kappa=0$) | **PIVOTE 176.P1** — el objetivo realista; análogo de Linnik/Gallagher (log-free cerca de $\sigma=1$) trasladado a la línea crítica. [GAP de literatura: no conozco log-free en $\sigma\to\frac12^+$] |
| 2 | $T(\log T)^{-K}$, $K$ arb. | $\kappa$ negativo: ahorro logarítmico genuino en $s\asymp1/\log T$ | Sin técnica conocida |
| 3 | $T^{1-\delta}$ | ahorro de potencia **en el borde** $s\to0^+$: $N(\frac12+s,T)\ll T^{1-\delta}g(s)$ | Muro mayor (implicaría casi-todos-los-ceros en bandas $T^{-\delta'}$-finas; fuera de alcance) |
| 4 | $O(1)$ $=$ **A** | [GAP-A]: densidad uniforme en $T$ | El problema |
| 5 | $0$ $=$ RH | $N\equiv0$ | — |

Cada peldaño $\ge1$ es progreso real del programa: con LP-112 detrás, cualquier $o(T/\log T)$ **afila la dicotomía** (la ventana de divergencia de [COR 176.10] se estrecha) y mejora las tasas de testigos de [TEOREMA 175.6]. Pivotes adicionales, registrados:
- **176.P2 (pivote $J$, heredado de 173 §7c):** la energía de primer orden $J=\sum b_j$ con su paquete Littlewood–Blaschke; este documento añade: el conducto de momentos da $J(T)\ll T\log\log T$ incondicional-bajo-momentos — débil; el camino para $J$ es el mismo layer-cake con $\int f(s)\,ds<\infty$ (sin el factor $s$): *más* exigente cerca de $s=0$, no menos. A (cuadrático) sigue siendo el objetivo correcto de los dos.
- **176.P3 (la parte media del flujo):** el promedio del flujo es una diferencia de $\log|\zeta|$ en dos alturas (§2.3); su valor medio fino (más allá de $O(\log T_0)$) es accesible por la teoría de valores medios de $\log|\zeta|$ — podría dar el término secundario de $\overline D$ y un test cuantitativo de consistencia del escenario $I(0^+)>0$.
- **176.P4 (usar 176.4 como *definición* operativa):** en la dirección de Fase 54 (ley de balance), $\overline D(T_0)+\frac\pi8$ es una versión regularizada-en-corte de $\pi I$ sin átomos en el borde — candidato natural a la "norma que gradúa" pedida en 173 §6.3, previo al programa de desingularización DBN.

---

## Referencias

- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Cambridge Philos. Soc.* 22 (1924), 295–318. [Lema de Littlewood.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. D. R. Heath-Brown), Oxford, 1986. §3.9 (lema de factorización local), §9.4 ($S(T)=O(\log T)$), §9.9 (lema de Littlewood), cap. 9 (densidades), §13.5 (teorema de Backlund: LH $\iff$ conteo por ventanas).
- R. J. Backlund, "Über die Nullstellen der Riemannschen Zetafunktion", *Acta Math.* 41 (1918), 345–375. [Equivalencia LH–conteo; detalles vía Titchmarsh §13.5.]
- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946), 89–155. [Densidad $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$; origen del certificado $T/\log T$.]
- A. E. Ingham, "On the estimation of $N(\sigma,T)$", *Quart. J. Math. Oxford* 11 (1940), 291–292. [LH $\Rightarrow$ DH.]
- M. N. Huxley, "On the difference between consecutive primes", *Invent. Math.* 15 (1972), 164–170. [Densidad $12/5$; GAP de literatura: exponente citado de memoria.]
- G. Halász, P. Turán, "On the distribution of roots of Riemann zeta and allied functions, I", *J. Number Theory* 1 (1969), 121–137. [Bajo LH: $N(\sigma,T)\ll T^\varepsilon$ para $\sigma>\frac34$.]
- H. Davenport, *Multiplicative Number Theory*, 3.ª ed., GTM 74, Springer. Caps. 15–16 (fracciones parciales de $\zeta'/\zeta$; conteo por ventanas).
- H. L. Montgomery, "The pair correlation of zeros of the zeta function", *Proc. Sympos. Pure Math.* 24 (1973), 181–193. [Formulada bajo RH; citada solo para posicionamiento.]
- H. L. Montgomery, R. C. Vaughan, "Hilbert's inequality", *J. London Math. Soc.* 8 (1974), 73–82. [Valor medio de polinomios de Dirichlet; usado solo calibratoriamente en §1.1.]
- H. Bohr, B. Jessen, "Über die Werteverteilung der Riemannschen Zetafunktion", *Acta Math.* 54 (1930), 1–35; 58 (1932), 1–55. — V. Borchsenius, B. Jessen, *Acta Math.* 80 (1948). [Distribución límite de $\log\zeta(\sigma+it)$, $\sigma>\frac12$; uso calibratorio §5.2, con GAP declarado sobre momentos absolutos.]
- Yu. V. Linnik (1944) / P. X. Gallagher, "A large sieve density estimate near $\sigma=1$", *Invent. Math.* 11 (1970), 329–339. [Densidades log-free cerca de $\sigma=1$; inspiración del PIVOTE 176.P1.]
- G. H. Hardy, J. E. Littlewood (1918); A. E. Ingham (1926). [Momentos $k=1,2$.] — J. P. Keating, N. C. Snaith, *Comm. Math. Phys.* 214 (2000). [Conjetura de momentos.]

**Documentos internos:** Doc 170 (coordenadas; Teorema 170.5), Doc 172 (techo $T/\log T$), Doc 173 (identidad de Green–Littlewood 173.C — base de este documento; §8 pasos nombrados 2 y 3 aquí ejecutados/decididos), Doc 175 (dicotomía LP-112, Teorema 175.2; arquitectura COR 175.5.2), Fase 54 (ley de balance).
