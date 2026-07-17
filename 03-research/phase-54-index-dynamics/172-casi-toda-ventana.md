# Documento 172 — Casi-toda-ventana: ¿detección, mejora directa, o colapso en densidad?

**Programa:** Hipótesis de Riemann — Fase 54 (dinámica del índice)
**Fecha:** 2026-06-11
**Mandato:** decidir cuál de los tres enunciados candidatos (I detección / II mejora directa / III colapso) de la formulación casi-toda-ventana (reparación R-171.2 del auditor) es teorema. Prerrequisitos leídos en fuente: Doc 170 completo (Prop 170.1, Thm 170.3, Cálculos 170.4, Thm 170.5, Thm 170.8), Doc 171 completo (H1, R-171.2, E-171.1/2/3, §3.2 niveles de ruido).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] prueba completa o sin etiqueta; [CÁLCULO] mostrado; [PUENTE] honesto; [GAP]/[DESEO] declarados. Falsa victoria peor que fracaso.

**Coordenadas (idénticas al 170).** Cero off $\rho=\tfrac12+b_j+i\gamma_j$, un representante por cuádruplo; $E(T)=\sum_{\gamma_j\le T}b_j^2$; clase admisible $\mathcal A$ y fórmula de Weil como en 170 (cabecera). $S(t)$, $\bar N$, $Z^\flat$ como allí.

**Test fijo de trabajo (Fejér).** $g(u)=\tfrac1L\max(0,1-|u|/L)$ (par, soporte $[-L,L]$, $g\ge0$), de modo que
$$h(r)=\int_{-L}^{L}g(u)e^{iru}\,du=\Bigl(\frac{\sin(Lr/2)}{Lr/2}\Bigr)^{2}\ \ge 0,\qquad h(0)=1,\quad h''(0)=-\tfrac{L^2}{6},\quad |h(x)|,|h''(x)|\ll\frac1{1+x^2}\ (x\gtrsim 1/L\text{, con }|h''|\ll L^2\text{ en el núcleo}).$$
$h$ entera (soporte compacto de $g$), en la franja $|\operatorname{Im}z|\le\tfrac12$: $|h(x+iy)|\ll e^{L|y|}/(1+(Lx)^2)$ — está en $\mathcal A$ con $\delta=1$. Ventana en $\tau$: $h_\tau(t)=h(t-\tau)+h(t+\tau)$, $g_\tau(u)=2g(u)\cos(\tau u)$. Señal: $\Sigma(\tau):=\sum_{Z}h_\tau(\gamma_\rho)-\sum_{Z^\flat}h_\tau(\gamma_\rho)=2\sum_j\Delta_j(h_\tau)$; identidad 170.1(iii): $\Sigma(\tau)=\mathfrak D(\tau)-F(\tau)$, con $\mathfrak D(\tau):=\mathfrak D(h_\tau)$ (primos+polo+arquimediano) y $F(\tau):=\int h_\tau\,dS$. Por cuádruplo a escala LP-134 ($b=c_0/\log\gamma$, $L=A\log\gamma$): señal en el centro $2b^2|h''|(1+o(1))=\tfrac{(c_0A)^2}{3}(1+o(1))=\Theta(c_0^2)$ — el hecho marginal del 170 §3.4, intacto.

---

## 0. Resumen ejecutivo y veredicto

**VEREDICTO: (III), en forma refinada y con prueba — colapso sobre el objetivo $E$, no-colapso de formulación.**

1. **(II) REFUTADA con teorema [TEOREMA 172.2, el momento clavado]:** el segundo momento del sesgo de von Mangoldt sobre ventanas NO es una cota: es una **identidad universal de primos**. Montgomery–Vaughan lo clava por los dos lados: $\frac1{T_0}\int_{T_0}^{2T_0}\mathfrak D(\tau)^2d\tau=\tfrac23+o(1)$ (test Fejér, $A\le1$) — el mismo número en todo mundo, con o sin ceros off. Un estadístico de valor forzado no acota nada: el canal de información hacia $E$ es exactamente cero. La mejora $E\ll T/\log^{1+\delta}T$ es además **imposible por esta vía en cualquier mundo** (techo estructural, §3.4): el suelo de ruido por ventana es $\Theta(1)$ y la tasa de cambio señal↔energía convierte cualquier estadística de ventanas en a lo sumo $E\ll T/\log T$ = 170.5.
2. **(I) REFUTADA incondicionalmente [PROP 172.6]:** dos configuraciones la matan — (a) la progresión aritmética (ceguera EXACTA: $E\asymp T/\log T$ con $\Sigma\equiv0$ para TODO test admisible de soporte $A<1$, por Poisson); (b) la energía que cabalga el mar ($b_j$ constante sobre ordenadas realistas: el sesgo se vuelve un funcional del mar deformado un factor relativo $O(c_0^2)$ — indistinguible dentro de la incertidumbre-de-constantes de la varianza del mar). La contrapositiva ("sin sesgo ⟹ $E=o(T/\log T)$") muere con (a). La versión condicional sobrevive pero CAPADA: incluso con correlación de pares, el techo es $E\ll T/\log T$ — reproduce 170.5, nunca lo mejora.
3. **Lo que SÍ es teorema nuevo:** [TEOREMA 172.4] $\int_{T_0}^{2T_0}\Sigma(\tau)^2d\tau\ll T_0$ incondicional (MV + Fujii) — el segundo momento de la señal de segundo orden es finito por ventana típica. Y **NO es consecuencia de los teoremas de densidad** (una configuración densidad-consistente lo viola con $T_0\log T_0$, §4.2): es una cota de **espectro de potencia de la medida de energía** a frecuencias de resolución — un eje que la densidad no ve. Pero es **ortogonal a $E$**: no lo acota (cancelación) ni lo necesita.
4. **El signo:** compra una FORMULACIÓN que la densidad no puede expresar (el estadístico muestreado-en-centros, = el sesgo permanente de D152, separa configuraciones que todos los teoremas de densidad tratan igual — [PROP 172.8]) pero no compra CERTIFICACIÓN: su evaluación es una suma doble sobre ceros = correlación de pares = el muro viejo. No-colapso de formulación, colapso de certificación.
5. **Corrección de presupuesto [E-172.1]:** el límite MV para soporte duro es $L\le\log T_0$ ($A\le1$), **no** $(2-\varepsilon)\log T_0$ como dicen 170 §3.4 y 171 §3.2.2 — la cifra $2-\varepsilon$ pertenece al test gaussiano ($T^2\le(2-\varepsilon)\log T_0$, resolución $\asymp(\log T_0)^{-1/2}$, otra escala). La señal marginal sigue siendo $\Theta(c_0^2)$ — nada estratégico cambia, pero la constante sí.

**El frente casi-toda-ventana queda CERRADO** con: un teorema de imposibilidad (172.2+172.6+172.7), un certificado nuevo no-densidad (172.4–172.5), y la identidad estructural que explica el cierre: **la envolvente de Selberg $T/\log T$ ES el suelo de ruido de ventanas leído en energía** — (nº de ventanas $\asymp T\log T$) × (cuanto mínimo de energía detectable por ventana $\asymp1/\log^2T$) $=T/\log T$. Densidad y ventanas son dos cómputos del mismo suelo; por eso ni se mejoran ni se contradicen.

---

## 1. Hipótesis exactas y el presupuesto corregido

### 1.1. Montgomery–Vaughan, forma exacta usada

**(Hilbert generalizado, [MV74, Thm. 2 y Cor. 3]).** Si $\lambda_1<\dots<\lambda_N$ son reales con $\delta_n=\min_{m\ne n}|\lambda_n-\lambda_m|$, entonces $\bigl|\sum_{m\ne n}\frac{a_m\bar a_n}{\lambda_m-\lambda_n}\bigr|\le\frac{3\pi}{2}\sum_n\frac{|a_n|^2}{\delta_n}$. Consecuencia (la forma valor-medio): para $a_n$ complejos con soporte finito,
$$\int_{T_0}^{2T_0}\Bigl|\sum_{n\ge2}a_n n^{-i\tau}\Bigr|^2d\tau\;=\;\sum_n|a_n|^2\,\bigl(T_0+\theta\,O(n)\bigr),\qquad|\theta|\le1\ \text{(dos lados, incondicional)},$$
porque $\lambda_n=\log n$ tiene $\delta_n\asymp1/n$. Hipótesis verificadas para nuestro uso: $a_n=\frac{\Lambda(n)}{\sqrt n}g(\log n)$ real $\ge0$, soporte $2\le n\le e^L$ finito ✓; frecuencias distintas ✓. **Nota:** es una identidad de dos lados — esto es lo que clava (no solo acota) el momento en §2.

### 1.2. [LEMA 172.1] (presupuesto de soporte duro — corrección E-172.1)

*Sea $a_n=\frac{\Lambda(n)}{\sqrt n}g(\log n)$ con el test Fejér de soporte $L=A\log T_0$. Entonces:*
$$D:=\sum_n|a_n|^2=\int_0^Lu\,g(u)^2du+o(1)=\tfrac1{12}+o(1),\qquad \sum_n n|a_n|^2\asymp \frac{e^{L}}{L^{3}},$$
*y el error MV relativo al término principal $T_0D$ es $O(T_0^{A-1}/\log^3T_0)$: **admisible si y solo si $A\le1$** (con $A=1$ sobra un $\log^{-3}$). Para momentos cuartos (cuadrado del polinomio, longitud $e^{2L}$): $A\le\tfrac12$.*

*Prueba.* Diagonal: $\Lambda(n)^2=\Lambda(n)\log n$ salvo potencias de primos ($O(e^{L/2})$ términos de tamaño $O(L^2e^{-L}\cdot L^{-2})$, total $o(1)$); por PNT con error clásico y sumación parcial, $\sum_{n\le x}\frac{\Lambda(n)\log n}{n}=\tfrac12\log^2x+O(\log x)$, de donde $\sum\frac{\Lambda(n)^2}{n}g(\log n)^2=\int_0^Lu\,g(u)^2du\,(1+o(1))$; con el triángulo $\int_0^Lu\cdot\tfrac1{L^2}(1-u/L)^2du=\int_0^1s(1-s)^2ds=\tfrac1{12}$. Error: $\sum\Lambda(n)^2g(\log n)^2\asymp\int_0^Lue^u\tfrac{(1-u/L)^2}{L^2}du$; con $u=L-s$ el integrando es $\asymp e^{L}e^{-s}s^2/L^3$, integral $\asymp e^L/L^3$. Cociente contra $T_0D\asymp T_0$: $T_0^{A-1}/\log^3T_0$. $\square$

**[E-172.1, errata a registrar]:** Doc 170 §3.4 ("$L=(2-\varepsilon)\log\gamma$, $n\le\gamma^{2-\varepsilon}$, el límite MV") y Doc 171 §3.2.2 ("incondicional bajo $L\le(2-\varepsilon)\log\tau$") **confunden dos escalas**. En el test gaussiano la restricción $T^2\le(2-\varepsilon)\log T_0$ vive en resolución $(\log T_0)^{-1/2}$, y el grueso de su polinomio está en $n\le e^{O(T)}=e^{O(\sqrt{\log T_0})}$ — el $2$ viene de la cola cuadrática del peso, no de longitud real $T_0^2$. Para soporte duro a resolución $1/\log T_0$ (la escala marginal), el grueso está en $n\asymp T_0^A$ y MV exige $A\le1$: con $A\in(1,2)$ la cota de varianza se degrada a $O(T_0^{A-1})$ por ventana — inútil; y nada mejor que MV existe ahí (longitudes $>T_0$ = territorio de correlación de pares, $|\alpha|>1$, conjetural incluso bajo RH). **Consecuencia benigna:** la señal marginal es $\tfrac13(c_0A)^2$ con $A\le1$ en vez de $A\le2$ — sigue $\Theta(c_0^2)$; todas las conclusiones de escala del 170 §3.4 sobreviven con constante menor.

### 1.3. [LEMA 172.3] (varianza del mar por ventana, incondicional)

*Con el test Fejér, $L=A\log T_0$, $A\le1$:* $\displaystyle\frac1{T_0}\int_{T_0}^{2T_0}F(\tau)^2\,d\tau\;\ll\;1.$

*Prueba.* $\int h'(v)\,dv=0$, luego $F(\tau)=\int h_\tau\,dS=-\int h'(v)\,[S(\tau+v)-S(\tau)]\,dv+(\text{término espejo})$, con $|h'(v)|\ll L/(1+(Lv)^2)$, $\|h'\|_1=O(1)$. Minkowski integral en $L^2(d\tau)$:
$$\|F\|_{L^2[T_0,2T_0]}\le\int|h'(v)|\;\bigl\|S(\cdot+v)-S(\cdot)\bigr\|_{L^2[T_0,2T_0]}\,dv.$$
Para $|v|\le1$: el teorema de Fujii (método de Selberg; incondicional) $\int_0^{T}\bigl(S(t+v)-S(t)\bigr)^2dt\ll T\log(2+|v|\log T)$ da, con $w=Lv$, $\int_{|w|\le L}\frac{\sqrt{\log(2+|w|\frac{\log T_0}{L})}}{1+w^2}dw=O(1)$ (pues $\log T_0/L=1/A=O(1)$ y $\sqrt{\log(2+w)}/(1+w^2)$ es integrable). Para $|v|>1$: $\|S(\cdot+v)-S(\cdot)\|_{L^2}\ll\sqrt{T_0\log\log T_0}$ por Selberg ($\int_0^T S^2\ll T\log\log T$, [S46], incondicional), y $\int_{|v|>1}|h'(v)|dv\ll1/L$: contribución $\ll\sqrt{T_0\log\log T_0}/\log T_0=o(\sqrt{T_0})$. Término espejo ($h(t+\tau)$, $t,\tau>0$): $|h(t+\tau)|\ll(L\tau)^{-2}$, contribución $O(T_0^{-2}\log T_0)$ trivial. Total $\ll\sqrt{T_0}$. $\square$

**Hipótesis de las fuentes, verificadas:** MV74 — solo frecuencias distintas y $\ell^2$ finito ✓. Selberg [S46] momentos de $S$ — incondicional ✓. Fujii — el enunciado usado es la **cota superior** de la varianza de incrementos, incondicional (método de Selberg); la **asintótica con constante** en el rango $v\asymp1/\log T$ es equivalente a correlación de pares (Goldston–Montgomery [GM87], condicional — no la usamos). **[GAP de literatura, menor y declarado]:** locus exacto — Fujii, Bull. AMS 81 (1975) 139–142 y Trans. AMS (1974); citado con confianza alta; la cota inferior $\gg T$ de esa varianza a resolución NO la conozco incondicional (relevante en §3.2: juega a favor de la imposibilidad, no en contra).

---

## 2. Candidato (II) de punta a punta: el momento clavado

### 2.1. [CÁLCULO 172.C1] El sesgo por ventana es un polinomio de Dirichlet puro

$\mathfrak D(\tau)=h_\tau(\tfrac i2)+h_\tau(-\tfrac i2)-4\operatorname{Re}P(\tau)+[\text{arq}]$, con $P(\tau)=\sum_n a_nn^{-i\tau}$, $a_n=\frac{\Lambda(n)}{\sqrt n}g(\log n)$ (el 4: $g_\tau=2g\cos(\tau u)$ y el $2$ de Weil). Polo: $|h_\tau(\pm\tfrac i2)|\le|h(\tau\pm\tfrac i2)|+|h(-\tau\pm\tfrac i2)|\ll e^{L/2}/(L\tau)^2\ll T_0^{A/2-2}=o(1)$ ✓. Arquimediano: $\frac1{2\pi}\int h_\tau\Omega-\int h_\tau d\bar N=O(\int h_\tau(r)(1+r^2)^{-1}dr)=O(T_0^{-2})$ ✓ (Stirling, como en 170 cabecera). Luego $\mathfrak D(\tau)=-4\operatorname{Re}P(\tau)+o(1)$ uniforme en $[T_0,2T_0]$.

### 2.2. [TEOREMA 172.2] (el momento clavado — refutación de (II))

*Incondicionalmente, con el test Fejér y $L=A\log T_0$, $A\le1$:*
$$\frac1{T_0}\int_{T_0}^{2T_0}\mathfrak D(\tau)^2\,d\tau\;=\;8\sum_n\frac{\Lambda(n)^2}{n}\,g(\log n)^2\;+\;o(1)\;=\;\frac23+o(1).$$
*El valor es una identidad de primos: no depende de la configuración de ceros en ningún sentido — es el mismo número si RH es cierta, si es falsa, o si $E(T)$ satura su envolvente. En particular, el segundo momento del sesgo no acota $\sum(\text{señales})^2$, no acota $E(T)$, y no puede dar $E\ll T/\log^{1+\delta}T$: **el candidato (II) es vacío, no falso-por-poco: su lado izquierdo no contiene información**.*

*Prueba.* $\mathfrak D^2=16(\operatorname{Re}P)^2+o(1)\cdot O(|P|)+o(1)$ y $(\operatorname{Re}P)^2=\tfrac12|P|^2+\tfrac12\operatorname{Re}(P^2)$.
(i) $\int_{T_0}^{2T_0}|P|^2=D\,T_0(1+O(T_0^{A-1}\log^{-3}))$ por MV **en sus dos lados** (Lema 172.1) — aquí es donde el valor queda clavado y no solo acotado.
(ii) $P(\tau)^2=\sum_{N}c_NN^{-i\tau}$ con frecuencias $\log N\ge\log4>0$; $|\int_{T_0}^{2T_0}N^{-i\tau}d\tau|\le2/\log N\le2/\log4$, luego $|\int\operatorname{Re}P^2|\le\tfrac2{\log4}\bigl(\sum_na_n\bigr)^2\ll e^{L}/L^2=T_0^{A}/\log^2T_0=o(T_0)$ para $A\le1$.
(iii) Términos cruzados con el $o(1)$ del polo/arquimediano: $\ll o(1)\cdot\sqrt{T_0\cdot\int|P|^2}=o(T_0)$. Diagonal $8D=\tfrac23$ por el Lema 172.1. $\square$

### 2.3. Por qué (II) no es reparable dentro del marco

La esperanza de (II) era: lado de primos computable $\Rightarrow$ cota sobre señales $\Rightarrow$ cota sobre $E$. La cadena real es: $\Sigma=\mathfrak D-F$, luego la identidad clavada dice
$$\int(\Sigma+F)^2=\bigl(\tfrac23+o(1)\bigr)T_0\qquad\textbf{(presupuesto total fijo)},$$
es decir: el momento del sesgo mide **señal + mar juntos**, y su valor está fijado de antemano. Extraer $\int\Sigma^2$ exige conocer $\int F^2$ y $\int\Sigma F$ con precisión de constantes — exactamente la varianza del mar a resolución (= correlación de pares en $|\alpha|\le A$, condicional [M73], y de hecho el rango $|\alpha|\le1$ de Montgomery coincide con nuestro presupuesto $A\le1$: la frontera incondicional y la condicional se tocan en el mismo sitio — no es casualidad, es el mismo polinomio de Dirichlet). Incondicionalmente solo hay $\Theta(1)$ de dos lados con constantes que no casan: la resta del término esperado **no es incondicional**, respondiendo la pregunta del mandato. Y aun con la resta (§3.4): techo $E\ll T/\log T$. **(II) cerrado.**

---

## 3. Candidato (I): detección, las dos configuraciones que la matan, y el papel del signo

### 3.1. [TEOREMA 172.4] (el certificado positivo: la señal en media cuadrática)

*Incondicionalmente, con el test Fejér, $L=A\log T_0$, $A\le1$:*
$$\int_{T_0}^{2T_0}\Sigma(\tau)^2\,d\tau\;\ll\;T_0,\qquad \Sigma(\tau)=\sum_{Z}h_\tau-\sum_{Z^\flat}h_\tau .$$

*Prueba.* $\|\Sigma\|_{L^2}\le\|\mathfrak D\|_{L^2}+\|F\|_{L^2}\ll\sqrt{T_0}$ por el Teorema 172.2 y el Lema 172.3. $\square$

**[PROP 172.5] (lectura espectral).** Para un bloque diádico de cuádruplos $\{(\gamma_j,b_j):\gamma_j\in(T_0,2T_0]\}$ y la señal idealizada de bloque $\Sigma_{bl}(\tau)=2\sum_{j\in bl}\phi_{b_j}(\gamma_j-\tau)$, con $\phi_b(x):=2\operatorname{Re}h(x+ib)-2h(x)=2\int_{-L}^{L}g(\xi)\bigl[\cosh(b\xi)-1\bigr]\cos(x\xi)\,d\xi$:
$$\int_{\mathbb R}\Sigma_{bl}(\tau)^2\,d\tau\;=\;\frac{8}{2\pi}\int_{-L}^{L}g(\xi)^2\,\bigl|G(\xi)\bigr|^2\,d\xi,\qquad G(\xi):=2\pi\sum_{j}\bigl(\cosh(b_j\xi)-1\bigr)e^{i\gamma_j\xi}$$
(Plancherel; $\hat\phi_b(\xi)=4\pi g(\xi)(\cosh(b\xi)-1)$, calculado arriba con $g$ par). La diferencia entre $\Sigma$ y $\Sigma_{bl}$ en $[T_0,2T_0]$ es la fuga inter-bloque, $O\bigl(\sum_{\gamma_j\notin(T_0/2,4T_0]}b_j^2/(1+L^2(\gamma_j-\tau)^2)\bigr)$, controlada en $L^2$ por la envolvente 170.5 — pérdida $o(T_0)$. **Lectura:** 172.4 es una cota incondicional sobre el **espectro de potencia de la medida de energía** $\sum_j(\cosh(b_j\cdot)-1)\delta_{\gamma_j}$ en las frecuencias de resolución $|\xi|\le A\log T_0$, con coeficientes POSITIVOS ($\cosh-1\ge0$). Es un eje ortogonal a los conteos $N(\sigma,T)$ (el eje "masa total"; §4.2 prueba la no-implicación). El signo de la huella vive aquí como positividad de coeficientes — pero extraer la diagonal $\sum_j(\cosh(b_j\xi)-1)^2$ de $|G|^2$ exigiría rango de $\xi$ $\gg$ (gap medio)$^{-1}=\log T_0/2\pi$, y el presupuesto da $|\xi|\le A\log T_0$ con $A\le1$: el solapamiento es $2\pi A=O(1)$ — **constante contra constante otra vez**: la diagonal no se separa, coherente con las cancelaciones de 3.2.

### 3.2. [PROP 172.6] (las dos configuraciones: (I) no es teorema incondicional)

**(a) Ceguera exacta (progresión aritmética).** Sea $Z_{ap}$ la configuración con ordenadas $\gamma_k$ en progresión local de paso $d(\gamma)=2\pi/\log\gamma$ (densidad RvM exacta) y TODOS los ceros off a $b_k=c_0/\log\gamma_k$, con $c_0>0$ constante absoluta respetando la densidad de Selberg ($c_0\le4\log C_S$ basta: $N(\tfrac12+c_0/\log T,T)=N(T)\le C_ST\log T\,e^{-c_0/4}$ ✓). Entonces $E(T)\asymp c_0^2\,T/\log T$ — **envolvente 170.5 saturada salvo constante** — y sin embargo, para TODO test admisible de soporte $L'=A'\log T_0$ con $A'<1$ y todo $\tau\in[T_0,2T_0]$:
$$\Sigma(\tau)\;=\;O(T_0^{-1}\log T_0)\qquad\textit{(cero salvo bordes)}.$$
*Prueba.* Poisson sobre la progresión local: $\sum_k\phi_b(\tau-kd)=\frac1d\sum_{m\in\mathbb Z}\hat\phi_b\bigl(\tfrac{2\pi m}{d}\bigr)e^{2\pi im\tau/d}$; las frecuencias duales son $m\log T_0$ y $\operatorname{supp}\hat\phi_b\subset[-A'\log T_0,A'\log T_0]$ con $A'<1$: solo sobrevive $m=0$, y $\hat\phi_b(0)=4\pi g(0)(\cosh0-1)=0$. Truncación y variación lenta de $d(\gamma)$: colas $\ll b^2\sum_{|\gamma_k-\tau|>T_0/2}(\gamma_k-\tau)^{-2}\ll T_0^{-1}\log T_0$. $\square$
**Consecuencias:** (I) es falso en la clase de configuraciones (sesgo CERO en toda ventana, energía saturante), y su contrapositiva ("segundo momento del sesgo pequeño $\Rightarrow E=o(T/\log T)$") también. **Honestidad:** $Z_{ap}$ tiene mar rígido ($S=O(1)$), incompatible con $\int S^2\sim\frac{T}{2\pi^2}\log\log T$ de Selberg para ζ — mata teoremas configuracionales (el género 170.8/141.B2), no describe ζ. Para ζ, (b):

**(b) Energía que cabalga el mar.** Sea $Z_{rid}$: ordenadas = un mar realista arbitrario (p.ej. las de ζ, con todos sus momentos de Selberg), y $b_j\equiv c_0/\log\gamma_j$ en todas. De nuevo $E\asymp c_0^2T/\log T$. Entonces
$$\Sigma(\tau)=\int\phi_b(t-\tau)\,dN^\flat(t)=\underbrace{\int\phi_b\,d\bar N}_{=\;\frac{\log(\tau/2\pi)}{2\pi}\hat\phi_b(0)+O(T_0^{-1})\;=\;O(T_0^{-1})}+\;\int\phi_b(t-\tau)\,dS(t),$$
es decir: **la señal entera es un funcional del mar** (de nuevo $\hat\phi_b(0)=0$ mata el término liso). Y el dato observable por ventana queda $\mathfrak D(\tau)=\Sigma+F=\int\bigl[2\operatorname{Re}h(\cdot+ib)-h\bigr](t-\tau)\,dS(t)$: el MISMO tipo de funcional del mar que en el mundo on-line ($\mathfrak D=\int h\,dS$), con núcleo deformado en factor relativo $O\bigl((bL)^2\bigr)=O(c_0^2A^2)$. Toda estadística cuadrática de ventanas difiere entre $Z_{rid}$ ($E\asymp T/\log T$) y el mundo on-line ($E=0$) en un factor $1+O(c_0^2)$ **multiplicando la varianza del mar, cuyo valor incondicional solo se conoce a $\Theta(1)$ de dos lados con constantes que no casan** (Lema 172.3 da $\ll$; el $\gg$ ni se conoce — GAP §1.3). Indistinguibles dentro de la clase de certificados {cotas con constantes absolutas sobre estadísticas de ventanas}. $\square$

**Veredicto (I):** no es teorema incondicional, ni en la clase configuracional (muerte exacta por (a)) ni para ζ (indistinguibilidad por (b), más que la cota inferior de la varianza del mar a resolución es ella misma desconocida). El mecanismo es nuevo respecto del primer orden: no es integral-cero de la señal (la señal típica de $Z_{rid}$ es $\Theta(c_0^2)$, ¡visible!) — es que **la señal es indistinguible DEL ruido, no menor que él**: vive en el mismo funcional del mar, deformándolo multiplicativamente. Detección = conocer la varianza del mar con precisión de constantes = correlación de pares.

### 3.3. El papel del signo: qué compra y qué no

**[PROP 172.8] (el estadístico firmado está fuera de los teoremas de densidad).** El estadístico muestreado-en-ordenadas $\mathcal B(T):=\frac1{N(T)}\sum_{\gamma\le T}\Sigma(h_\gamma)$ (= la versión integrada del sesgo permanente de D152, unisigno porque muestrea los NÚCLEOS, donde $-h''>0$) **separa pares de configuraciones que satisfacen las mismas cotas de densidad con las mismas constantes**: tómese $Z_1$ = cuádruplos centrados en ordenadas del mar (núcleos muestreados: $\mathcal B\asymp c_0^2\cdot$proporción) y $Z_2$ = los mismos multiconjuntos $\{b_j\}$, $\{\gamma_j\}$ desplazados media resolución respecto de los puntos de muestreo (flancos muestreados: $\mathcal B$ de signo opuesto o nulo). Idénticos marginales — toda cota envolvente de densidad les dice lo mismo — distinto $\mathcal B$. *Los teoremas de densidad constriñen los marginales de $(b,\gamma)$; el estadístico firmado mide la CORRELACIÓN entre posiciones off y puntos de muestreo — un grado de libertad que la densidad no ve.* $\square$

**[PUENTE honesto — por qué eso no se certifica]:** evaluar $\mathcal B$ exige $\sum_{\gamma\le T}\mathfrak D(h_\gamma)$ y $\sum_{\gamma\le T}F(h_\gamma)$: sumas dobles sobre ceros del tipo $\sum_{\gamma,\gamma'}w(\gamma-\gamma')$ y sumas de Landau $\sum_\gamma n^{i\gamma}$ — exactamente la correlación de pares de Montgomery [M73] (condicional a RH en $|\alpha|\le1$, conjetural más allá) y fórmulas de Landau/Gonek con errores que a esta resolución valen lo que la propia correlación. **Respuesta a la pregunta del mandato: el signo compra una formulación que la densidad no puede expresar (no-colapso de formulación — por eso (I)/(II) no eran reducibles "trivialmente" a densidad y hubo que probar el colapso; la advertencia (iv) era correcta), pero su evaluación reconduce al muro viejo: no compra certificación.** El primer orden nunca tuvo ni la formulación; el segundo orden la tiene y la deja a un paso del mismo muro — esa es la medida exacta del progreso.

### 3.4. [PROP 172.7] (el techo estructural: ni condicionalmente se mejora 170.5)

*Supóngase concedido TODO lo condicional: la asintótica fina de la varianza del mar (correlación de pares en $|\alpha|\le2A$) y la evaluación por ventana del lado primo (GAP-141.G1 entero, mar incluido). Entonces lo máximo que la estadística de ventanas a resolución $1/L$ puede certificar sobre la energía es $E(T)\ll T/\log T$ — la envolvente 170.5, jamás $T/\log^{1+\delta}T$.*

*Prueba.* (i) Suelo: incluso con todo concedido, lo certificable por ventana es $|\Sigma(\tau)|\le M(\tau)$ con $\frac1{T_0}\int M^2\ll1$ — el suelo $\Theta(1)$ no es epistémico: bajo RH-y-GUE el mar REALMENTE fluctúa $\Theta(1)$ por ventana a resolución (la asintótica de Fujii/GM87, $\asymp\log(2+v\log T)$, vale $\Theta(1)$ en $v\asymp1/\log T$); ningún refinamiento de hipótesis lo baja. (ii) Tasa de cambio: un cuádruplo a escala $c$ produce señal $\asymp c^2$ portando energía $c^2/\log^2T$; invertir "señal por ventana $\le\Theta(1)$" da energía $\le\Theta(1/\log^2T)$ por ventana — **el cuanto de resolución**. (iii) Total: nº de ventanas disjuntas a resolución $\asymp T_0L\asymp T\log T$; energía certificable $\le T\log T\cdot O(1/\log^2T)=O(T/\log T)$. Y eso en el caso MEJOR (sin cancelación núcleo/flanco entre cuádruplos, que solo empeora la inversión). $\square$

**Identidad estructural (la moraleja del frente):** $\;T/\log T=\underbrace{T\log T}_{\text{nº ventanas}}\times\underbrace{\log^{-2}T}_{\text{cuanto}}$. La envolvente de Selberg (densidad, Teorema 170.5) y el suelo de ruido de ventanas son **el mismo número calculado por dos rutas**: la densidad lo obtiene del amontonamiento de Bohr–Landau–Selberg; las ventanas, de la fluctuación $\Theta(1)$ del mar por celda de resolución. Por eso casi-toda-ventana ni mejora ni empeora a la densidad sobre $E$: computa el mismo suelo.

---

## 4. (III): colapso sobre $E$, no-colapso de formulación — el cierre

### 4.1. [TEOREMA 172.9] (colapso sobre el objetivo)

*Toda cota sobre $E(T)$ certificable con el paquete casi-toda-ventana incondicional —{identidad de Weil por ventana, MV (Lema 172.1), momentos de $S$ de Selberg/Fujii, positividad/Cauchy–Schwarz}— está implicada por los teoremas de densidad; concretamente, el paquete no certifica ninguna cota $E(T)\le\varepsilon T/\log T$ con $\varepsilon$ menor que una constante absoluta, ni distingue $E=0$ de $E\asymp T/\log T$.*

*Prueba.* Las configuraciones de la Prop 172.6 satisfacen todas las salidas del paquete con las mismas constantes ($Z_{ap}$: exactamente las del mundo on-line, señal nula; $Z_{rid}$: dentro del factor $1+O(c_0^2)$ de una varianza solo conocida a constantes), tienen $E\asymp T/\log T$, y el techo 172.7 acota lo concedible incluso añadiendo los inputs condicionales. La única cota sobre $E$ que el paquete reproduce es la envolvente, que es 170.5 = densidad. $\square$

### 4.2. [PROP 172.10] (no-colapso: 172.4 NO es un teorema de densidad)

*Existe una configuración $Z_{cl}$ consistente con todas las cotas de densidad conocidas (Selberg incluido), con RvM y $S=O(\log)$, tal que $\int_{T_0}^{2T_0}\Sigma^2\,d\tau\gg T_0\log T_0$. Por tanto el Teorema 172.4 ($\ll T_0$, que para ζ es incondicional vía primos+Fujii) no es consecuencia de los teoremas de densidad: el frente produce al menos un certificado genuinamente nuevo.*

*Prueba.* [CÁLCULO] $Z_{cl}$: racimos de $m=\epsilon\log T_0$ cuádruplos a distancia mutua $\le1/L$, cada uno con $b=c/\log T_0$, un racimo por unidad de altura en $(T_0,2T_0]$. Consistencia: $m$ ceros extra en un intervalo de longitud $1/L$ cuesta un salto de $S$ de tamaño $\epsilon\log T_0$ — dentro de Backlund para $\epsilon$ pequeño ✓; nivel de densidad: $T_0m=\epsilon T_0\log T_0$ ceros a altura $b=c/\log$: Selberg permite $C_ST_0\log T_0e^{-c/4}$ ✓ para $\epsilon\le C_Se^{-c/4}$; energía $E=\epsilon c^2T_0/\log T_0$ dentro de la envolvente ✓. Señal: en el núcleo de cada racimo los $\Delta_j$ se SUMAN (mismo signo, misma celda): $\Sigma\asymp mc^2\cdot\tfrac13A^2$ sobre anchura $\asymp1/L$; los flancos de racimos distintos (separación $\ge1$) aportan $O(\sum_{k\ge1}b^2m/k^2)=O(1)$ por ventana — no cancelan el núcleo. Total: $\int\Sigma^2\gtrsim T_0\cdot(mc^2)^2/L\asymp\epsilon^2c^4\,T_0\log T_0$. $\square$

**Lectura conjunta 172.9+172.10:** como medidores de $E$, ventanas $\subseteq$ densidad (colapso); como productores de certificados, son **incomparables**: 172.4 (espectro de potencia de la energía a frecuencias de resolución, con la positividad $\cosh-1\ge0$ incorporada) constriñe el eje de CORRELACIÓN/agrupamiento de la energía, que la densidad no ve — pero ese eje es ortogonal a la masa total $E$ (la cancelación de 172.6a lo prueba: espectro nulo, masa saturante). El enunciado (III) del mandato es teorema en su mitad relevante (todo lo que ventanas certifica SOBRE $E$ ya lo da densidad) y falso en su literal absoluto (no todo lo que ventanas certifica es densidad integrada) — la diferencia es exactamente 172.4, y exactamente no toca a RH.

### 4.3. Qué queda abierto (sin desear de más)

El único resquicio sigue siendo el de siempre, ahora con su forma final: **evaluación aritmética por ventana mejor que MV** — computar $\mathfrak D(\tau)$ ventana a ventana con error $o(1)$ usando la aritmética real de los primos (no solo su diagonal en media), MÁS la cota de varianza del mar (ya incondicional, Lema 172.3), daría cotas en casi-toda-ventana sobre $\sum_{\gamma_j\approx\tau}(b_j\log\gamma_j)^2$ — la forma reparada R-171.2, que este documento confirma como bien planteada pero cuya mitad-primos es GAP-141.G1: el muro viejo, sin rebaja. Ninguna formulación de promedio lo esquiva (172.9). No se declara DESEO nuevo: el de R-171.2 es el correcto y queda como único.

---

## 5. Veredicto final

**(III) es el teorema** — colapso sobre $E$ con techo estructural (172.7: la envolvente de Selberg ES el suelo de ruido de ventanas; identidad nº-ventanas × cuanto), probado contra los dos rescates posibles: (II) muere por el momento clavado (172.2: el segundo momento del sesgo es una identidad universal de primos, $\tfrac23+o(1)$, ciega a los ceros — ni siquiera es una cota), y (I) muere incondicionalmente por las dos configuraciones (172.6: ceguera exacta por Poisson; energía que cabalga el mar = deformación multiplicativa indistinguible a constantes), quedando solo como enunciado correlación-de-pares-completo y aun así capado por 172.7. **El signo compra formulación, no certificación** (172.8 + PUENTE): el estadístico firmado muestreado-en-centros está genuinamente fuera del alcance expresivo de la densidad — por eso el colapso NO era trivial y hubo que probarlo — pero su evaluación ES correlación de pares. Botín del frente al cerrarse: el certificado nuevo 172.4–172.5 (espectro de potencia de la energía $\ll T$ a frecuencias de resolución, incondicional, no-densidad por 172.10) y la corrección de presupuesto E-172.1 ($A\le1$, no $2-\varepsilon$).

### Erratas
- **E-172.1 (Doc 170 §3.4 y Doc 171 §3.2.2):** el presupuesto MV para tests de soporte duro es $L\le\log T_0$ ($A\le1$), no $(2-\varepsilon)\log$; la cifra $2-\varepsilon$ pertenece al test gaussiano ($T^2\le(2-\varepsilon)\log T_0$, resolución $(\log T_0)^{-1/2}$, grueso del polinomio en $n\le e^{O(\sqrt{\log T_0})}$). Inocua para la estrategia (señal sigue $\Theta(c^2)$), no para las constantes. Registrar en 06-papers/ERRATA.md si se propaga.

### Referencias
Montgomery, H.L., Vaughan, R.C. (1974), *Hilbert's inequality*, J. London Math. Soc. (2) 8, 73–82 — desigualdad de Hilbert generalizada y teorema de valor medio (incondicional, dos lados). — Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 — densidad y momentos de $S(t)$ (incondicionales). — Fujii, A. (1975), *On the distribution of the zeros of the Riemann zeta function in short intervals*, Bull. Amer. Math. Soc. 81, 139–142 — varianza de $S(t+h)-S(t)$, cota superior incondicional por el método de Selberg [confianza alta; locus exacto: GAP de literatura menor declarado en §1.3]. — Montgomery, H.L. (1973), *The pair correlation of zeros of the zeta function*, Proc. Symp. Pure Math. 24 — condicional a RH, $|\alpha|\le1$. — Goldston, D.A., Montgomery, H.L. (1987), *Pair correlation of zeros and primes in short intervals*, en Analytic Number Theory and Diophantine Problems, Birkhäuser — equivalencia varianza-de-incrementos ↔ correlación de pares (condicional; citada solo como tal). — Backlund, R. (1918), Acta Math. 41 — $S(t)\ll\log t$. — Jutila, M. (1983), en Studies in Pure Mathematics, Birkhäuser — mejora de la constante de Selberg (vía E-171.3). — Docs internos: 141 (GAP-141.G1, 141.B0/B/B2, 141.M1/M5), 152 (espectro de impureza), 167 (GAP 167.A), 168, 170, 171 (R-171.2, H1).
