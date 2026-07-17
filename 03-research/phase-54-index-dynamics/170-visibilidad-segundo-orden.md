# Documento 170 — Visibilidad de segundo orden: ¿es certificable I(0⁺) por herramientas de promedio incondicionales?

**Programa:** Hipótesis de Riemann — Fase 54 (dinámica del índice)
**Fecha:** 2026-06-11
**Mandato:** decidir UNA pregunta: ¿la cantidad de segundo orden $I(0^+)=\sum_j b_j^2$ (o cotas superiores sobre ella, incluso solo la finitud $\ell^2$, GAP 167.A) es certificable por herramientas de promedio incondicionales, o el muro cuadrático la mata igual que el de primer orden (no-go 141.B2)?
**Prerrequisitos leídos en fuente:** Doc 167 (§3 GAP 167.A, §5 tabla ζ-libre y matiz "firmado→cuadrático"), Doc 168 (§5.2 hallazgo de segundo orden y advertencia), Doc 141 completo (Lemas 141.B0/141.B, Cor. 141.B2, Cálculos 141.M1–M5, GAP-141.G1), memoria de Phase 48 (D152, espectro de impureza).
**Contrato:** [DEFINICIÓN-NUEVA] libre; [TEOREMA]/[PROP]/[LEMA] prueba completa o sin etiqueta; [CÁLCULO] mostrado; [PUENTE] honesto; [GAP]/[DESEO] declarados. Falsa victoria peor que fracaso.

**Coordenadas.** Trabajamos en coordenadas de ζ: cero off $\rho=\tfrac12+b_j+i\gamma_j$, $b_j\in(0,\tfrac12)$, $\gamma_j>0$, un representante por cuádruplo $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$. $I(0):=\sum_j b_j^2$ (mitad superior; en la carta $H_t$ de Polymath 15 la energía es $4\sum_j b_j^2$ — factor de la dilatación por 2, Doc 168 KILL-2; aquí todo en carta ζ, sin mezclas). Para un test $h$ y un cero escribimos $h(\gamma_\rho)$ con $\gamma_\rho=\gamma_j-ib_j$ (convención $\rho=\tfrac12+i\gamma_\rho$).

**Clase admisible $\mathcal A$.** $h:\mathbb R\to\mathbb R$ par, que se extiende holomorfa a $|\operatorname{Im}z|\le\tfrac12+\varepsilon$ con $|h(z)|\le C(1+|\operatorname{Re}z|)^{-1-\delta}$ uniformemente en la franja, y $g(u):=\frac1{2\pi}\int_{\mathbb R}h(r)e^{-iru}\,dr$ (par, real). Es la clase de la fórmula explícita de Weil [W52; IK04, Thm. 5.12]:
$$\sum_{\rho}h(\gamma_\rho)\;=\;h(\tfrac i2)+h(-\tfrac i2)\;-\;2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n)\;+\;\frac1{2\pi}\int_{\mathbb R}h(r)\,\Omega(r)\,dr,$$
con $\Omega(r)=\operatorname{Re}\frac{\Gamma'}{\Gamma}(\tfrac14+\tfrac{ir}2)-\log\pi$ (Stirling: $\Omega(r)=\log\frac{|r|}{2\pi}+O((1+r^2)^{-1})$).

---

## 0. Resumen ejecutivo y veredicto

**VEREDICTO: (C), parcial, con el corte exacto en la escala de resolución $b\cdot\log\gamma$ y en la dicotomía tasa/total.**

1. **Certificable incondicionalmente (probado aquí, §4):** la versión truncada-con-tasa de GAP 167.A. **[TEOREMA 170.5]** $E(T):=\sum_{\gamma_j\le T}b_j^2\ \ll\ T/\log T$ (densidad de Selberg + capas). **[COR 170.6]** la energía en unidades de Lehmer tiene densidad acotada por cero, $\frac1{N(T)}\sum_{\gamma_j\le T}(b_j\log\gamma_j)^2=O(1)$, y la suma total ponderada $\sum_j b_j^2/\bigl(\gamma_j(\log\log\gamma_j)^{1+\varepsilon}\bigr)$ **converge**. Es el primer certificado incondicional sobre una cantidad de segundo orden RH-relevante del programa — pero es una **envolvente de crecimiento**, no decide $I(0^+)$.
2. **No certificable (probado aquí, §2–§3, §4.3):** (a) la media en $\tau$ de la señal de segundo orden es **exactamente cero a todo orden en $b$** ([TEOREMA 170.3], desplazamiento de contorno) — el mecanismo integral-cero de 141.M5/141.B2 **reaparece en segundo orden**, no en la señal puntual sino en el promedio de traslaciones y en el peso ($\int h''=0$ para todo test admisible; **no existe test admisible con $h''$ de signo constante**); (b) las tres rutas de certificación por ventana (puntual, lineal, cuadrática) tienen el **mismo umbral incondicional $\omega=\tfrac14$** = el polo = la jurisdicción exacta de D152 ([CÁLCULOS 170.4]); (c) $I(0^+)<\infty$ no es separable por datos de promedio ([TEOREMA 170.8], sucesor de 141.B2: configuración con $I=\infty$ y datos $\varepsilon$-indistinguibles).
3. **La escala marginal (§3.4, el hecho nuevo que vindica al auditor del 168):** con tests de soporte máximo evaluable $L\asymp\log\gamma$, la señal de segundo orden de un cuádruplo a la escala LP-134 ($b=c/\log\gamma$) es $\Theta(c^2)$ — **orden uno, no sub-resolución**: a diferencia del primer orden (señal idénticamente promediada a cero), el segundo orden NO está enterrado por tamaño. Lo que bloquea la certificación en la escala marginal es exclusivamente (i) la evaluación incondicional del lado primo por ventana individual (= GAP-141.G1, el muro viejo) y (ii) la estadística cuadrática del mar a resolución $\asymp1$ (= correlación de pares de Montgomery, condicional a RH). El muro de segundo orden es real pero es **el mismo muro viejo reubicado**, no uno nuevo.

---

## 1. La huella de segundo orden exacta

### 1.1. La identidad, con el signo correcto

**[PROP 170.1] (huella exacta).** Sea $h\in\mathcal A$ y sea $Z$ la configuración de ceros de ζ, $Z^\flat$ su proyección a la línea (ordenadas idénticas). Entonces:

(i) *(descomposición espectral)* $\displaystyle\sum_{\rho\in Z}h(\gamma_\rho)-\sum_{\rho\in Z^\flat}h(\gamma_\rho)\;=\;2\sum_j\Delta_j(h),\qquad \Delta_j(h):=2\operatorname{Re}h(\gamma_j+ib_j)-2h(\gamma_j),$
(el factor 2 externo: los dos lados $\pm\gamma_j$ del cuádruplo, $h$ par; $2\operatorname{Re}h(\gamma_j+ib_j)=h(\gamma_j+ib_j)+h(\gamma_j-ib_j)$ por reflexión de Schwarz, $h$ real en $\mathbb R$).

(ii) *(desarrollo)* $\displaystyle \Delta_j(h)\;=\;-\,b_j^2\,h''(\gamma_j)\;+\;R_j,\qquad |R_j|\;\le\;\tfrac1{12}\,b_j^4\sup_{|y|\le b_j}\bigl|h^{(4)}(\gamma_j+iy)\bigr|,$
y de hecho $\Delta_j(h)=2\sum_{k\ge1}\frac{(-1)^k b_j^{2k}}{(2k)!}h^{(2k)}(\gamma_j)$ (serie convergente, $h$ holomorfa en la franja). **Nota de signo:** la huella es $-\sum_j b_j^2h''(\gamma_j)$, no $+$; el enunciado del Doc 168 §5.2 tiene el signo cambiado (errata E-170.1, §6; inocua allí). Para un test con pico en $\gamma_j$ ($h''(\gamma_j)<0$) el lado de ceros tiene **exceso positivo** respecto del mundo proyectado.

(iii) *(el funcional de primos que la iguala)* Con $N^\flat(t)$ el conteo de ordenadas, $\bar N(t)=\frac t{2\pi}\log\frac t{2\pi e}+\frac78$ y $S(t)=N^\flat(t)-\bar N(t)+O(1/t)$ (Riemann–von Mangoldt, [T86, Thm. 9.4]; idéntica en $Z$ y $Z^\flat$, Lema 141.B0):
$$\boxed{\;-2\sum_j b_j^2\,h''(\gamma_j)\;+\;2\sum_j R_j\;=\;\underbrace{h(\tfrac i2)+h(-\tfrac i2)-2\sum_n\frac{\Lambda(n)}{\sqrt n}g(\log n)+\Bigl[\tfrac1{2\pi}\!\int h\,\Omega-\!\int h\,d\bar N\Bigr]}_{=:\ \mathfrak D(h)\ \text{(sesgo de von Mangoldt vs. predicción RvM — computable)}}\;-\;\underbrace{\int h\,dS}_{=:\ F(h)\ \text{(fluctuación del mar)}}\;}$$

*Prueba.* (i): contar el cuádruplo contra su proyección. (ii): $f(b):=2\operatorname{Re}h(\gamma+ib)$ es par y real-analítica; Taylor con resto integral en $b^2$; la cota de $R_j$ por Cauchy en el segmento. (iii): fórmula de Weil para $Z$ (exacta) menos $\sum_{Z^\flat}h=\int h\,dN^\flat=\int h\,d\bar N+\int h\,dS+O(\|h\|_\infty)$ pequeño. $\square$

**Lectura.** La huella de segundo orden de $I$ es el **sesgo de la suma de primos respecto de la predicción lisa RvM, módulo la fluctuación del mar $F(h)$**. Todo certificado debe separar tres números: $\mathfrak D(h)$ (computable solo trivialmente sin RH), $F(h)$ (estadística de ordenadas — σ-ciega pero desconocida), y la señal. Esta es la estructura exacta sobre la que operan §2–§3.

### 1.2. El espectro de impureza de D152 ES la ventana de segundo orden

**[PROP 170.2] (comparación término a término con D152).** Tómese $g(u)=e^{-u^2/4T^2}\cos(\tau u)$, i.e. el test del espectro de impureza $S_T(\tau)=\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\cos(\tau\log n)$. Entonces $h_\tau(t)=\sqrt\pi\,T\bigl[e^{-T^2(t-\tau)^2}+e^{-T^2(t+\tau)^2}\bigr]$ y la contribución de un cuádruplo $(\gamma_j,b_j)$, término núcleo, es **exactamente**
$$2\operatorname{Re}h_\tau(\gamma_j+ib_j)-2h_\tau(\gamma_j)\;=\;2\sqrt\pi\,T\,e^{-T^2(\gamma_j-\tau)^2}\Bigl[e^{T^2 b_j^2}\cos\bigl(2T^2(\gamma_j-\tau)b_j\bigr)-1\Bigr].$$
En consecuencia:
1. *(régimen sub-resolución $b_jT\le1$)* el corchete es $-b_j^2\,\partial_t^2\bigl[\sqrt\pi Te^{-T^2(t-\tau)^2}\bigr]_{t=\gamma_j}/(\sqrt\pi T e^{-T^2(\gamma_j-\tau)^2})\cdot(1+O(b^2T^2))$: la huella de la Prop. 170.1 al orden principal — en $\tau=\gamma_j$, $+2\sqrt\pi\,b_j^2T^3$ del lado ceros, sesgo **negativo** en $S_T$ (los ceros entran con signo $-$): el sesgo permanente de D152.
2. *(régimen súper-resolución $b_jT\gg1$)* el factor $e^{T^2b_j^2}$ es la **resumación completa** de la serie de (ii) de la Prop. 170.1 (la gaussiana suma su Taylor exactamente), y la tasa exponencial $\frac1{T^2}\log|\cdot|\to b_j^2-(\gamma_j-\tau)^2$ reproduce **exactamente** el peso de impureza $\omega(\tau)=\max\bigl(0,\max_j(b_j^2-(\gamma_j-\tau)^2)\bigr)$ del Teorema 152.2.

**Respuesta a la pregunta de la memoria de Phase 48: SÍ — el espectro de impureza es la ventana de segundo orden, resumada.** El peso ω cuadrático en $\delta_j$ no es coincidencia: es la huella $b^2h''$ del exponente Lehmer = 2, vista a súper-resolución; el sesgo negativo permanente $\sim-2\sqrt\pi\,m_JTe^{\delta^2T^2}$ es la firma de $I>0$ leída desde los primos. D152 y el GAP 167.A son **el mismo objeto** en dos regímenes del mismo test. (Y por eso la jurisdicción $\omega\le\tfrac14$ de D152 reaparecerá como umbral en §3.)

---

## 2. El ataque "firmado→cuadrático": el test cóncavo muere globalmente, sobrevive localmente

La esperanza del mandato: elegir $h$ con $h''$ de signo fijo donde importa, para que $-\sum b_j^2h''(\gamma_j)$ sea unisigno y un promedio la acumule mientras el ruido se cancela. El siguiente teorema mide exactamente cuánto de esa esperanza existe.

**[TEOREMA 170.3] (integral-cero de segundo orden — el sucesor estructural de 141.M5).** Sea $h\in\mathcal A$.
1. $\displaystyle\int_{\mathbb R}h''(t)\,dt=0$ y por tanto $\int(h'')_+=\int(h'')_-$: **el peso de segundo orden de todo test admisible es un perfil de media exactamente nula.** En particular no existe $h\in\mathcal A$ no constante con $h''$ de signo constante en $\mathbb R$ (también directamente: una función cóncava no constante en $\mathbb R$ tiende a $-\infty$ en algún extremo — incompatible con el decaimiento).
2. *(ceguera exacta de los promedios lineales de traslaciones, a TODO orden en $b$)* Para todo $0<b\le\tfrac12$ y todo $\gamma$:
$$\int_{\mathbb R}\Bigl[h\bigl(\gamma+ib-\tau\bigr)+h\bigl(\gamma-ib-\tau\bigr)-2h\bigl(\gamma-\tau\bigr)\Bigr]\,d\tau\;=\;0\qquad\textbf{exactamente}.$$
En consecuencia, **cualquier estadística que sea una media en $\tau$ (con peso lentamente variable) de ventanas trasladadas de un test fijo tiene sensibilidad idénticamente nula a $I$** — no $O(b^4)$: cero, a todo orden, incluida la resumación exponencial.

*Prueba.* (1): $h'\to0$ en $\pm\infty$ (decaimiento en la franja + Cauchy para $h'$). (2): $\int_{\mathbb R}h(x+ib)\,dx=\int_{\mathbb R}h(x)\,dx$ por el teorema de Cauchy en el rectángulo $[-R,R]\times[0,b]$ (lados verticales $\to0$ por el decaimiento uniforme en la franja, $b\le\tfrac12<\tfrac12+\varepsilon$); restar dos veces la misma integral. Para peso $w$ lentamente variable, $w$-media de traslaciones = evaluación del test compuesto $h\star w$, que es de nuevo un test fijo: se reduce a una sola ventana (§3). $\square$

**Veredicto del ataque del §5.1 del Doc 167 sobre GAP 167.A: el ataque se confirma, pero con el mecanismo desplazado.** La obstrucción "firmado→cuadrático" no mata la señal puntual (que es unisigno en el núcleo de la ventana — eso es real y nuevo respecto del primer orden); mata la **acumulación**: la señal de segundo orden es unisigno *localmente* pero de media *globalmente* nula en $\tau$ — los flancos ($h''>0$ fuera del núcleo, con masa exactamente igual por (1)) compensan el núcleo con exactitud de teorema. La ruta "señal unisigno se acumula linealmente, ruido se cancela" **no existe**: la acumulación lineal cancela la señal, no el ruido. Toda acumulación que preserve el signo es cuadrática en la ventana — y paga el precio del §3.3.

---

## 3. Señal/ruido: las tres rutas y el umbral común ¼

Fijamos la ventana gaussiana de la Prop. 170.2 (los cálculos con tests de soporte compacto tipo Fejér/Beurling–Selberg dan el mismo cuadro; §3.4 los usa donde son mejores). Normalizamos por la altura del pico $\sqrt\pi T$: señal por cuádruplo en el centro $s_j=2(e^{b_j^2T^2}-1)$ ($\approx2b_j^2T^2$ sub-resolución).

### 3.1. [CÁLCULO 170.4a] Ruta puntual (una ventana, certificación individual)

Para certificar una cota superior de $s_j$ vía la identidad de la Prop. 170.1(iii) hay que acotar por arriba $\mathfrak D(h_\tau)$ y $|F(h_\\tau)|$. Incondicionalmente: (α) la suma de primos solo admite la cota trivial $\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\le(1+o(1))\sqrt\pi\,T\,e^{T^2/4}$ (punto de silla $u=T^2$ del exponente $u/2-u^2/4T^2$, valor $T^2/4$); (β) $|S(t)|\le C\log t$ (Backlund, incondicional) da $|F|\le C'T\log\tau$ — y nada mejor por ventana individual. La cota trivial (α), normalizada, es $e^{T^2/4}$; la señal resumada máxima es $e^{b^2T^2}$ con $b<\tfrac12$, es decir $e^{b^2T^2}<e^{T^2/4}$ **siempre**: la cota trivial nunca certifica nada por debajo de $\omega=\tfrac14$. Es exactamente la jurisdicción de Λ≥0 de D152 (Props. 152.4–152.7), re-derivada: **el único certificado puntual incondicional es $\omega\le\tfrac14$, alcanzado solo por el polo.**

### 3.2. [CÁLCULO 170.4b] Ruta lineal (promedio en τ)

Muerta con exactitud por el Teorema 170.3(2): sensibilidad cero a todo orden. (Verificación independiente en la forma cerrada de la Prop. 170.2: $\int_{\mathbb R}e^{-T^2(x^2-b^2)}\cos(2T^2xb)\,dx=\frac{\sqrt\pi}T$, idéntico al valor on-line $\int e^{-T^2x^2}dx$ — la amplificación $e^{T^2b^2}$ y la oscilación del coseno se cancelan exactamente.)

### 3.3. [CÁLCULO 170.4c] Ruta cuadrática (segundo momento en τ)

Lo incondicional: por el teorema de valor medio de Montgomery–Vaughan [MV74], para $T^2\le(2-\varepsilon)\log T_0$,
$$\int_0^{T_0}\bigl|S_T(\tau)\bigr|^2d\tau\;=\;\Bigl(\tfrac12\sum_n\frac{\Lambda(n)^2}{n}e^{-(\log n)^2/2T^2}\Bigr)\,T_0\,(1+o(1))\;=\;c\,T^2\,T_0\,(1+o(1)),$$
(diagonal $\asymp T^2$; error $\sum_n n|a_n|^2\asymp T^2e^{T^2/2}\ll T^2T_0$ exactamente bajo la restricción de soporte $T^2\le(2-\varepsilon)\log T_0$ — el presupuesto clásico). Esto **fija el total** incondicionalmente. Pero el total = mar + impureza, y la estadística cuadrática del mar solo (la varianza de conteo de ordenadas a resolución $1/T$ con $T^2\asymp\log T_0$, i.e. la correlación de pares $F(\alpha)$ en $|\alpha|\asymp1$) es **incondicionalmente desconocida a orden principal**: el teorema de Montgomery [M73] es condicional a RH, y las variantes incondicionales (Goldston–Montgomery [GM87]) no la determinan. (Los momentos incondicionales de $S(t)$ de Selberg [S46] son estadísticas de rango largo — frecuencias $\alpha=o(1)$ — y no fijan la varianza a resolución.) Por tanto el mar puede absorber, dentro de la incertidumbre $\Theta(T^2T_0)$, cualquier exceso unisigno de impureza menor: un cuádruplo aporta exceso $\asymp T(e^{b^2T^2}-1)^2$ (más un término cruzado firmado aún mayor), y supera la incertidumbre del mar solo si $e^{2b^2T^2}\gtrsim T\,T_0$, i.e. $b^2\ge\tfrac14(1+o(1))$: **otra vez el polo, $\omega=\tfrac14$.**

**Síntesis de 170.4a–c:** tres rutas independientes, el mismo umbral. La jurisdicción $\omega\le\tfrac14$ de D152 es **óptima dentro de la clase de promedios incondicionales**; por debajo de ¼ ningún promedio certifica nada sobre una ventana.

### 3.4. [CÁLCULO 170.4d] La escala marginal: dónde queda exactamente la sub-resolución

Tests de soporte compacto: $g$ soportada en $[-L,L]$ (Fejér/Beurling–Selberg), resolución $1/L$, $|h''(\text{centro})|\asymp L^2h(\text{centro})$, amplificación off $\le e^{b_jL}$. Señal normalizada por cuádruplo en el centro: $\asymp(b_jL)^2$ (sub-resolución $b_jL\le1$). El soporte máximo con lado primo dentro del presupuesto incondicional de evaluación en media es $L=(2-\varepsilon)\log\gamma$ ($n\le\gamma^{2-\varepsilon}$, el límite MV; más allá, ni en media). Entonces, en la **escala LP-134** $b_j=c/\log\gamma_j$:
$$\text{señal}\;\asymp\;(b_jL)^2\;=\;\bigl(c\,(2-\varepsilon)\bigr)^2\;=\;\Theta(c^2)\;=\;\Theta(1).$$
El ruido por ventana: a resolución $1/L\asymp1/(2\log\gamma)$ — más fina que el gap medio $2\pi/\log\gamma$ — la ventana contiene $O(1)$ ordenadas, y su fluctuación (presencia/ausencia de un cero) es $\Theta(1)$. **Conclusión de escala, en tres franjas:**

| escala | señal por ventana óptima | estado |
|---|---|---|
| $b\log\gamma\to\infty$ | $\to\infty$ (resumación $e^{bL}$) | visible; y de hecho la densidad la **cuenta** (Lema 141.M1: exactamente su umbral de no-trivialidad) — es la franja del §4 |
| $b\log\gamma\asymp1$ | $\Theta(c^2)$ vs. mar $\Theta(1)$ | **marginal: NO enterrada por tamaño.** Bloqueada solo por (i) evaluación del lado primo por ventana individual con error $o(1)$ = **GAP-141.G1** (Conj. 108-N, el muro viejo), y (ii) varianza del mar a resolución = correlación de pares, condicional a RH |
| $b\log\gamma\to0$ | $\to0$ | enterrada en TODA ventana evaluable; solo tests de soporte $\gg\log\gamma$ la verían (no evaluables; es el territorio de la Rigidez 153.M′, soporte super-logarítmico) |

**Esto cuantifica y confirma el hallazgo del auditor (Doc 168):** el muro de segundo orden es genuinamente **distinto y más débil** que el de primer orden. En primer orden la señal era idénticamente nula en promedio y de tamaño $O(\delta a)$ individual; en segundo orden la señal a escala crítica es $\Theta(1)$ por ventana — no hay déficit de tamaño. Pero el muro no se cruza: se **reconduce** — certificar exige o bien evaluación por ventana individual (GAP-141.G1) o bien la estadística cuadrática del mar (RH-condicional). El círculo de §3.3 del Doc 141 se cierra también en segundo orden: *la cantidad cuadrática, atacada con análisis, reconduce a la mitad vieja del muro.* Ninguna puerta lateral — pero, a diferencia del primer orden, ya no es un no-go de integral-cero de la señal: es un no-go de *evaluación*.

---

## 4. El cálculo de densidad: lo que SÍ es teorema incondicional

Aquí está el lado positivo del veredicto. Las herramientas de densidad son las únicas σ-sensibles por encima de la resolución (Lema 141.M1), y la ℓ²-truncada es exactamente una integral monótona de los conteos $N(\sigma,T)$ — del lado bueno.

**[TEOREMA 170.5] (envolvente incondicional de la energía de inestabilidad truncada).** Incondicionalmente,
$$E(T)\;:=\;\sum_{0<\gamma_j\le T}\Bigl(\beta_j-\tfrac12\Bigr)^2\;\ll\;\frac{T}{\log T}.$$
Más en general, cualquier teorema de densidad de la forma $N(\sigma,T)\le A\,T^{1-c(\sigma-1/2)}\log^B T$ ($\tfrac12\le\sigma\le1$) da $E(T)\le\frac{2A}{c^2}\,T\log^{B-2}T\,(1+o(1))$.

*Prueba.* Capas (layer-cake): $b_j^2=\int_0^{1/2}2b\,\mathbf 1_{\{b<b_j\}}\,db$, luego $E(T)=\int_0^{1/2}2b\,N(\tfrac12+b,\,T)\,db$ (frontera de medida nula). Con el teorema de densidad de Selberg [S46], $N(\tfrac12+b,T)\le C\,T^{1-b/4}\log T=CT\log T\,e^{-(b/4)\log T}$ uniforme en $b\in[0,\tfrac12]$:
$$E(T)\;\le\;2CT\log T\int_0^{1/2}b\,e^{-b\log T/4}\,db\;\le\;2CT\log T\cdot\frac{16}{\log^2T}\int_0^\infty s\,e^{-s}\,ds\;=\;\frac{32\,C\,T}{\log T}.$$
La forma general: idéntica con $(A,c,B)$. $\square$

**Observaciones.** (a) Cerca de $\sigma=\tfrac12$ Selberg ($c=\tfrac14$, $B=1$) es lo óptimo conocido; Ingham [I40] ($T^{3(1-\sigma)/(2-\sigma)}\log^5T$: $c=\tfrac43$ pero $B=5$) y Huxley [H72] están optimizados lejos de la línea y dan $T\log^3T$ — peor. (b) La cota trivial es $E(T)\le\tfrac14N(T)\asymp T\log T$: la ganancia es $\log^2T$. (c) **Lectura geométrica:** $T/\log T$ es exactamente la energía de una configuración con el 100% de los ceros a distancia $\asymp1/\log\gamma$ — la envolvente dice que la energía total se comporta *como si todos los ceros estuvieran a escala de resolución*, la versión ℓ² del amontonamiento de Bohr–Landau/Selberg (Prop. 141.M2). (d) Comparación con la ruta ℓ¹ clásica: el lema de Littlewood + Jensen dan $\sum_{\gamma\le T}(\beta-\tfrac12)^+\ll T\log\log T$ ([L24]; [T86, §9.9]) y de ahí solo $E(T)\ll T\log\log T$ — la ruta de densidad es estrictamente mejor para la ℓ². **[GAP de literatura]:** la cota $E(T)\ll T/\log T$ es un corolario inmediato de [S46] y debería ser folklore; no conocemos referencia que la enuncie como tal.

**[COR 170.6] (formas normalizadas y convergentes).** Incondicionalmente:
1. *(densidad de energía de Lehmer acotada)* $\displaystyle\sum_{\gamma_j\le T}\bigl(b_j\log\gamma_j\bigr)^2\;\ll\;T\log T\;\asymp\;N(T)$: en las unidades en que el exponente Lehmer es 2, la energía media de inestabilidad por cero es $O(1)$.
2. $\displaystyle\sum_{\gamma_j\le T}\frac{b_j^2}{\gamma_j}\;\ll\;\log\log T$, y para todo $\varepsilon>0$: $\displaystyle\sum_{j}\frac{b_j^2}{\gamma_j\,(\log\log\gamma_j)^{1+\varepsilon}}\;<\;\infty$ — **una versión total ponderada de GAP 167.A es teorema**, con el peso exacto dictado por la envolvente.

*Prueba.* (1): bloques diádicos $T_k=2^k$: $\sum_{\gamma\in(T_{k-1},T_k]}(b\log\gamma)^2\le\log^2T_k\,E(T_k)\ll T_k\log T_k$; sumar. (2): sumación parcial contra $E(t)\ll t/\log t$: $\int_2^T t^{-1}dE=E(T)/T+\int_2^TE(t)t^{-2}dt\ll1/\log T+\int_2^T\frac{dt}{t\log t}=\log\log T+O(1)$; para el peso $u(t)=(\log\log t)^{1+\varepsilon}$, $\int\frac{dt}{t\log t\,u(t)}<\infty$. $\square$

### 4.3. Lo que la densidad NO puede dar: la finitud total

**[PROP 170.7] (GAP 167.A está fuera del alcance de promedios — cuantificado).**
1. *(consistencia de $I=\infty$)* Para todo $b_0\in(0,\tfrac12)$ fijo, la configuración con un cuádruplo a distancia $b_0$ en cada altura $\gamma_k=2^k$ por encima de la verificación numérica ($3\cdot10^{12}$, [PT21]) es consistente con **todo** lo incondicional conocido: densidades (un cero por bloque diádico $\ll$ cualquier cota), región libre de ceros (Vinogradov–Korobov solo excluye $b\ge\tfrac12-c/(\log\gamma)^{2/3}(\log\log\gamma)^{1/3}$ — tómese $b_0<\tfrac12$ fijo), estadísticas verticales (Lema 141.B0), y la envolvente del Teorema 170.5 ($E(T)\ll\log T$ aquí). Tiene $I=\sum b_0^2=\infty$. **Ni siquiera la parte gorda $\sum_{b_j\ge b_0}b_j^2$ es certificablemente finita para ningún $b_0<\tfrac12$.**
2. *(qué exigiría la ruta de densidad)* La convergencia de $\sum_jb_j^2$ vía conteos exige $N(\tfrac12+b_0,T)=O_{b_0}(1)$ cuando $T\to\infty$ para cada $b_0>0$ — **semibandas asintóticamente libres de ceros** — mientras toda la tecnología conocida da exponentes $T^{a}$ con $a>0$ para todo $\sigma<1$ (la frontera VK está a distancia $o(1)$ de $\sigma=1$, no de $\sigma=\tfrac12+b_0$).
3. *(el contenido individual de GAP 167.A, destilado)* $I(0^+)<\infty\implies\forall b_0>0:\ \#\{j:b_j\ge b_0\}<\infty$ — **finitud por semibandas**, i.e. "$m<\infty$ en cada semibanda $b\ge b_0$" más la sumabilidad cerca de la línea. GAP 167.A está más cerca de $m<\infty$ de lo que su forma ℓ² sugería: su contenido detrás de la envolvente certificable es exactamente un enunciado de cuantificador individual.

*Prueba.* (1) verificación directa contra cada ítem de la tabla §2.6 del Doc 141. (2): $\sum_kb_0^2\,[N(\tfrac12+b_0,2^{k+1})-N(\tfrac12+b_0,2^k)]<\infty$ exige que la sucesión $N(\tfrac12+b_0,2^k)$ sea acotada. (3): los términos $\ge b_0^2$ de una serie convergente son finitos. $\square$

**Nota sobre Cramér y $\psi(x)-x$:** el segundo momento $\int_1^X(\psi(x)-x)^2x^{-2}dx\sim c\log X$ es **condicional a RH** (Cramér 1921 [C21]); incondicionalmente, una cota superior del segundo momento de $\psi$ ya implicaría densidad/Θ fuera de alcance (un solo cero con $\beta$ aporta $\gg x^{2\beta}$ a la media cuadrática). La diagonal del segundo momento ve $\sum x^{2b_j-1}|\rho_j|^{-2}$: amplificación exponencial $e^{2b_jL}$ con $L=\log x$ — la misma estructura de ventana del §3, mismo umbral, ninguna palanca nueva. No usable.

---

## 5. El no-go relativo de segundo orden (el sucesor de 141.B2)

**[TEOREMA 170.8] (la finitud ℓ² no es separable por datos de promedio).**
1. *(versión finita, limpia)* Sea $\mathcal F=\{F_1,\dots,F_M\}$ cualquier familia **finita** de tests admisibles fijada de antemano, y $\varepsilon>0$. Existe una configuración admisible $Z$ con $I(Z)=\sum_jb_j^2=\infty$ (de hecho con $b_j\to0$) tal que $|\sum_{\rho\in Z}h_{F_i}(\gamma_\rho)-\sum_{\rho\in Z^\flat}h_{F_i}(\gamma_\rho)|\le\varepsilon$ para todo $i\le M$, y $Z$, $Z^\flat$ tienen estadísticas verticales idénticas (Lema 141.B0) y respetan la envolvente del Teorema 170.5. Ningún argumento cuya entrada sean finitos datos de Weil + estadísticas de ordenadas puede probar $I(0^+)<\infty$.
2. *(versión numerable, métrica ponderada)* Para $\{F_i\}_{i\in\mathbb N}$ numerable y la métrica $d(\mathcal D,\mathcal D')=\sum_i2^{-i}\min(1,|\mathcal D_i-\mathcal D'_i|)$: existe $Z$ con $I(Z)=\infty$ y $d(\mathcal D(Z),\mathcal D(Z^\flat))\le\varepsilon$.

*Prueba.* Tómese $b_j:=1/\sqrt{\log(j+2)}$ (luego $\sum_jb_j^2=\sum1/\log(j+2)=\infty$, $b_j\to0$) y $\gamma_j$ inductivamente crecientes. Por el Lema 141.B (con $N=2$), la contribución del cuádruplo $j$ al dato $i$ es $\le C_2(F_i)\,(b_jL_i)^2e^{b_jL_i}(1+\gamma_j)^{-2}\le C'_i\,(1+\gamma_j)^{-2}$, que $\to0$ cuando $\gamma_j\to\infty$ **sin tocar $b_j$** — a diferencia de 141.B2, donde la indistinguibilidad se compraba encogiendo $\delta_j$, aquí se compra solo con altura, y por eso la divergencia de $\sum b_j^2$ es compatible. (1): finitas condiciones por paso ($i\le M$), cada una con presupuesto $\varepsilon2^{-j}/M$: elegir $\gamma_j$ suficientemente grande. (2): dado $\varepsilon$, fijar $I_0$ con $\sum_{i>I_0}2^{-i}\le\varepsilon/2$ y aplicar (1) a $\{F_i\}_{i\le I_0}$ con presupuesto $\varepsilon/2$; los datos $i>I_0$ quedan absorbidos por la métrica. La envolvente: un cuádruplo por paso con $\gamma_j$ súper-exponencial da $E(T)=o(T/\log T)$. $\square$

**Honestidad sobre el alcance, como en Obs. 3.1 del 141:** es un no-go **relativo a la clase de datos**, con una restricción adicional respecto de 141.B2: la versión por-dato-uniforme con familia numerable no se recupera (las cabezas finitas $j<i$ no son controlables con $b_j$ fijado por la divergencia); las dos versiones enunciadas cubren todo argumento efectivo (finitos datos, o módulo uniforme de dependencia en los datos). No excluye argumentos que usen la aritmética real de ζ a todos los soportes simultáneamente (GAP-141.G1) ni rigidez global de la clase de Euler — exactamente los mismos dos resquicios que en primer orden.

**Moraleja estructural (la diferencia con 141.B2, dicha sin adornos):** en primer orden la invisibilidad era de la *señal* (integral cero por cuádruplo, Cálculo 141.M5); en segundo orden la señal es robusta (Θ(1) en la escala marginal, §3.4) y la inseparabilidad es del *valor total*: la divergencia de $\sum b_j^2$ puede esconderse en alturas arbitrariamente grandes a tasa arbitrariamente lenta, por debajo de cualquier envolvente. Tasa certificable, total no — ese es el corte.

---

## 6. Veredicto final

**Sobre la pregunta única del mandato: (C) — parcial, con corte exacto en dos coordenadas independientes.**

**Coordenada 1 (escala, por ventana):** certificable ⟺ por encima de la resolución.
- $b\log\gamma\to\infty$: contable por densidad (única tecnología σ-sensible superviviente; Lema 141.M1 marca exactamente este umbral).
- $b\log\gamma\asymp1$: señal $\Theta(1)$ por ventana de soporte $L\asymp\log\gamma$ — **no enterrada** (el hallazgo a favor: el muro de sub-resolución que el Doc 168 temía no es de tamaño); certificación bloqueada por evaluación-por-ventana (GAP-141.G1) y por la varianza del mar a resolución (Montgomery, condicional). Umbral incondicional de certificación por ventana: $\omega=\tfrac14$ en las tres rutas (puntual/lineal/cuadrática) — la jurisdicción de D152 es óptima.
- $b\log\gamma\to0$: enterrada en toda ventana evaluable.

**Coordenada 2 (tasa vs. total):** la envolvente de crecimiento es teorema ([TEOREMA 170.5–COR 170.6]); el valor total $I(0^+)$ (incluso $<\infty$) es inseparable por promedios ([TEOREMA 170.8]) y su contenido residual es individual (finitud por semibandas, [PROP 170.7.3]).

**GAP 167.A queda así:** NO certificable con herramientas de promedio incondicionales — confirmando el ataque §5.1 del Doc 167 pero con el mecanismo corregido (la cancelación no está en la señal sino en la media de traslaciones, [TEOREMA 170.3]); su versión ponderada $\sum b_j^2/(\gamma_j(\log\log\gamma_j)^{1+\varepsilon})<\infty$ y su envolvente $E(T)\ll T/\log T$ son teoremas incondicionales; su contenido no-certificable es exactamente "$m<\infty$ por semibanda" — la mitad Fredholm otra vez, ahora medida con precisión.

**[DESEO declarado, el único hueco con forma de enunciado:]** una evaluación incondicional de $\mathfrak D(h_\tau)$ (Prop. 170.1(iii)) por ventana individual a soporte $L\asymp\log\gamma$ con error $o(1)$ — es GAP-141.G1/Conj. 108-N. En segundo orden ese es el ÚNICO bloqueo en la escala marginal; en primer orden ni siquiera eso bastaba (la señal era nula). Es la formulación más débil conocida del muro en la que cruzarlo daría algo (cotas por ventana sobre $\sum_{j:\gamma_j\approx\tau}(b_j\log\gamma_j)^2$).

### Erratas
- **E-170.1 (Doc 168 §5.2):** la huella es $\Delta_j=-b_j^2h''(\gamma_j)+O(b_j^4)$ (signo menos); el enunciado "$\sum_jb_j^2h''(\gamma_j)$" tiene el signo cambiado. Inocuo para las conclusiones del 168 (solo usa tamaño y orden). Registrar en 06-papers/ERRATA.md si se propaga.

### Referencias
Weil, A. (1952), *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund. — Iwaniec, H., Kowalski, E. (2004), *Analytic Number Theory*, AMS Colloq. 53, Thm. 5.12. — Selberg, A. (1946), *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. 48 (teorema de densidad $N(\sigma,T)\ll T^{1-(\sigma-1/2)/4}\log T$; momentos de $S(t)$). — Littlewood, J.E. (1924), *On the zeros of the Riemann zeta-function*, Proc. Camb. Phil. Soc. 22 (lema de Littlewood; $\int_0^TS$). — Titchmarsh, E.C. (1986), *The Theory of the Riemann Zeta-Function*, 2ª ed. (Heath-Brown), §9. — Ingham, A.E. (1940), *On the estimation of $N(\sigma,T)$*, Quart. J. Math. 11. — Huxley, M.N. (1972), *On the difference between consecutive primes*, Invent. Math. 15. — Montgomery, H.L. (1973), *The pair correlation of zeros of the zeta function*, Proc. Symp. Pure Math. 24 (condicional a RH). — Goldston, D.A., Montgomery, H.L. (1987), *Pair correlation of zeros and primes in short intervals*, en Analytic Number Theory and Dioph. Probl. — Montgomery, H.L., Vaughan, R.C. (1974), *Hilbert's inequality*, J. London Math. Soc. 8 (teorema de valor medio). — Cramér, H. (1921), *Ein Mittelwertsatz in der Primzahltheorie*, Math. Z. 12 (**condicional a RH** — citado solo como tal). — Bohr, H., Landau, E. (1914), C. R. Acad. Sci. Paris 158. — Backlund, R. (1918), *Über die Nullstellen der Riemannschen Zetafunktion*, Acta Math. 41 ($S(t)\ll\log t$). — Platt, D., Trudgian, T. (2021), *The Riemann hypothesis is true up to $3\cdot10^{12}$*, Bull. LMS 53. — Docs internos: 134, 141, 152 (Phase 48), 167, 168.
