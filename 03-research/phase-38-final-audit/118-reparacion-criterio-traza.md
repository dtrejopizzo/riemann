# Documento 118 — Reparación del criterio de traza: rigidez de momentos en lugar de positividad del kernel

**Programa:** Hipótesis de Riemann — Fase 38 (auditoría final)
**Fecha:** junio 2026
**Rol:** reparación post-refutación — mandato: reparar el teorema central del marco CCM (P39, Thm. `thm:main`, dirección $T_\lambda=0\ \forall\lambda \Rightarrow$ RH) tras la refutación del Doc 114, o declararlo irreparable con el gap exacto.
**Prerrequisitos:** Doc 114 (refutación de $W_\lambda\geq0$), Doc 63, Doc 83 ($d\nu\geq0$), Doc 89, P39, P40, P43, D72.

---

## Veredicto anticipado

**CRITERIO REPARADO** — en su forma por-índice (la familia $\{\int\kappa_n\,d\nu=0\}_{n\geq0}$), con prueba completa, incondicional, y por una vía nueva que **no usa** $W_\lambda\geq0$ ni ninguna asintótica de Christoffel:

$$\boxed{\;\text{RH}\iff \int_{\mathbb{R}}\kappa_n(s)\,d\nu(s)=0\ \ \text{para todo } n\geq 0\;}$$

donde $\kappa_n=(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$ y $d\nu=dm_{\rm full}-dm_{\rm full,on}\geq0$. El mecanismo de la prueba es la **rigidez del problema de momentos de Hamburger**: la condición de Carleman para $dm_\infty$ — la misma propiedad que *mata* el Cor. 1.2 del Doc 63 ($K_n\to\pi/2$ es falso) — es exactamente la que *repara* el criterio. La única medida positiva finita $\nu$ con $\int|\mathcal{P}_n|^2\,d\nu$ constante en $n$ es $\nu=c\,m_\infty$; y $c=0$ se sigue del teorema de Hardy (existen ceros críticos) más la continuidad de las densidades.

Dos salvedades quedan **declaradas** (no escondidas):

1. **(Bloques)** La forma-$\lambda$ literal de P39 ("$T_\lambda=0\ \forall\lambda$") sólo recupera la familia por-índice cuando las ordenadas $\{\gamma_n\}$ son dos a dos distintas. Bajo ¬RH hay coincidencias *automáticas* (cada par $\beta+i\gamma,\,1-\beta+i\gamma$ comparte ordenada), de modo que la forma-$\lambda$ entrega sólo sumas por bloques; la implicación "forma-$\lambda$ $\Rightarrow$ RH" queda abierta (gap preciso en §5.6). La forma por-índice es la formulación correcta del criterio y es la que la cadena CCM (P39 ítem (iii), D72 por-$n$) realmente produce.
2. **(Linealizado vs. exacto)** El objeto reparado es la traza *linealizada* $T_\lambda:=\int W_\lambda\,d\nu$ (la definición que el Doc 114 §5 declaró vinculante). La versión con discrepancias de Jacobi exactas, $\Delta_n^{\rm full}=\Delta_n^{\rm full,on}\ \forall n\iff$ RH, también es verdadera — por determinación de $m_{\rm full}$, y esa parte de P39 ya era esencialmente correcta (§5.7). Lo que el presente documento repara es el eslabón que la auditoría dejó sin demostración: que la familia *linealizada* también caracteriza RH.

---

## §0. Qué estaba roto y qué hay disponible

El Doc 114 probó: $\int W_\lambda\,dm_\infty=0$ exactamente, luego $W_\lambda$ toma valores negativos en abiertos (en los ceros de $\mathcal{P}_{N+1}$, $W_\lambda\leq-\tfrac12$), y la dirección $T_\lambda=0\ \forall\lambda\Rightarrow$ RH de P39 quedó sin demostración. Lo que sobrevive y usaremos como insumos:

- **(I-1)** $d\nu=(|\zeta|^2-|\zeta_{\rm on}|^2)\,dm_\infty\geq0$, incondicional (Doc 83, Cor. 1.2–1.3; ratificado por Doc 114 §7).
- **(I-2)** $d\nu=0\iff$ RH (Doc 89 cond. 2 / P39 Prop. `prop:full_measure`; ratificado por Doc 114 §7).
- **(I-3)** La identidad vinculante $T_\lambda=\int W_\lambda\,d\nu$ con $W_\lambda=\sum_{\gamma_n\leq\lambda}\kappa_n$ (Doc 114 §5: ésta es la definición que hace válida la representación integral; la adoptamos como *definición* de $T_\lambda$).
- **(I-4)** Los coeficientes exactos $a_n^\infty=\tfrac12\sqrt{(2n+1)(2n+2)}$ (CCM, axioma importado; P39 Def. 2.1).
- **(I-5)** La observación telescópica del Doc 114 §8.2: $T_\lambda=0\ \forall\lambda$ (con ordenadas separadas) $\Rightarrow\int\kappa_n\,d\nu=0\ \forall n\Rightarrow\Delta_n:=\int|\mathcal{P}_n|^2\,d\nu$ constante en $n$.

Notación fija: $dm_\infty(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}{2})|^2\,ds=:w(s)\,ds$; $\{\mathcal{P}_n\}$ ortonormales respecto de $dm_\infty$ ($\int\mathcal{P}_m\mathcal{P}_n\,dm_\infty=\delta_{mn}$), coeficiente líder positivo; $\tilde g(s):=|\zeta(\tfrac12+is)|^2-|\zeta_{\rm on}(\tfrac12+is)|^2\geq0$, de modo que $d\nu=\tilde g\,dm_\infty=\tilde g\,w\,ds$.

---

## §1. Normalizaciones y una identificación exacta nueva

### 1.1. La masa total de $dm_\infty$ (corrección a P39)

**Lema 1.1.** $\displaystyle m_\infty(\mathbb{R})=\int_{\mathbb{R}}dm_\infty=\frac{1}{\sqrt{2\pi}}$, y por tanto $\mathcal{P}_0\equiv(2\pi)^{1/4}$ (no $\mathcal{P}_0\equiv1$).

*Demostración.* Sea $f(x)=e^{-e^x}e^{x/4}$. Con $u=e^x$, $\widehat f(t)=\int_{\mathbb{R}}f(x)e^{-itx}\,dx=\int_0^\infty e^{-u}u^{1/4-it}\,\tfrac{du}{u}=\Gamma(\tfrac14-it)$. Por Parseval ($\int|\widehat f|^2=2\pi\int|f|^2$):
$$\int_{\mathbb{R}}\bigl|\Gamma(\tfrac14+it)\bigr|^2dt=2\pi\int_0^\infty e^{-2u}u^{-1/2}\,du=2\pi\,\Gamma(\tfrac12)\,2^{-1/2}=\pi\sqrt{2\pi}.$$
Con $t=s/2$: $m_\infty(\mathbb{R})=(2\pi)^{-2}\cdot 2\cdot\pi\sqrt{2\pi}=(2\pi)^{-1/2}$. Como $\int\mathcal{P}_0^2\,dm_\infty=1$ y $\mathcal{P}_0$ es constante, $\mathcal{P}_0=(2\pi)^{1/4}$. $\square$

**Verificación de consistencia.** El mismo método (Parseval con $f'=(\tfrac14-e^x)f$) da $\int t^2|\Gamma(\tfrac14+it)|^2dt=2\pi\cdot\tfrac{\sqrt\pi}{8\sqrt2}$, de donde $\mu_2/\mu_0=\int s^2dm_\infty/\int dm_\infty=\tfrac12=(a_0^\infty)^2=\tfrac{1\cdot2}{4}$ ✓. La afirmación de P39 ("a probability measure") es un error inocuo de normalización; **no** afecta a los $a_n^\infty$ (invariantes por reescalado de la masa), pero sí a la constante en $\Delta_0$: con $\mathcal{P}_0^2=\sqrt{2\pi}$,
$$\Delta_0=\int\mathcal{P}_0^2\,d\nu=\sqrt{2\pi}\;\nu(\mathbb{R}).$$

### 1.2. Los $\mathcal{P}_n$ son polinomios de Meixner–Pollaczek

**Proposición 1.2 (identificación exacta).** Sea $P_n^{(\lambda)}(x;\phi)$ la familia de Meixner–Pollaczek [KLS, §9.7], ortogonal en $\mathbb{R}$ respecto del peso $e^{(2\phi-\pi)x}|\Gamma(\lambda+ix)|^2$. Entonces los ortonormales CCM son exactamente los ortonormales de Meixner–Pollaczek con
$$\lambda=\tfrac14,\qquad \phi=\tfrac{\pi}{2},\qquad x=\tfrac{s}{2}.$$

*Demostración.* Para $\phi=\pi/2$ el peso es $|\Gamma(\tfrac14+ix)|^2=|\Gamma(\tfrac14+\tfrac{is}{2})|^2$ ✓ (mismo peso que $dm_\infty$, módulo constante). La recurrencia de Meixner–Pollaczek en $\phi=\pi/2$ es $(n+1)P_{n+1}=2xP_n-(n+2\lambda-1)P_{n-1}$ [KLS, ec. (9.7.3)]. Pasando a la forma mónica ($k_n=2^n/n!$) se obtiene $x\,\tilde p_n=\tilde p_{n+1}+\tfrac{n(n+2\lambda-1)}{4}\tilde p_{n-1}$, es decir, coeficientes de Jacobi ortonormales en $x$ acoplando $n\leftrightarrow n+1$:
$$a_n^{\rm MP}=\tfrac12\sqrt{(n+1)(n+2\lambda)}.$$
La recurrencia CCM $s\,\mathcal{P}_n=a_n^\infty\mathcal{P}_{n+1}+a_{n-1}^\infty\mathcal{P}_{n-1}$ en la variable $x=s/2$ tiene acoplamiento $a_n^\infty/2=\tfrac12\sqrt{(n+\tfrac12)(n+1)}$. Igualando: $n+2\lambda=n+\tfrac12\iff\lambda=\tfrac14$ ✓, y ambas familias tienen $b_n=0$ (medidas pares). Dos medidas positivas con los mismos coeficientes de Jacobi y problema de momentos **determinado** (Teorema 3.1 abajo) coinciden módulo normalización. $\square$

**Observación 1.3.** Esta identificación es nueva en el programa y tiene dos usos: (a) certifica de forma independiente los $a_n^\infty$ de CCM contra una tabla clásica [KLS]; (b) pone a disposición la literatura asintótica de Meixner–Pollaczek para cualquier refinamiento cuantitativo futuro. **No** la necesitamos para el teorema central de este documento.

---

## §2. Finitud de $\nu$ y de todos sus momentos

Éste era el primer punto delicado señalado en el encargo: si $\nu(\mathbb{R})=\infty$, $\Delta_0=\infty$ y todo el esquema colapsa. La respuesta es limpia y no requiere $N(\sigma,T)$:

**Proposición 2.1 (finitud de todos los momentos, incondicional).** Para todo $k\geq0$:
$$\mu_{2k}(\nu):=\int_{\mathbb{R}}s^{2k}\,d\nu(s)\;\leq\;\int_{\mathbb{R}}s^{2k}\,|\zeta(\tfrac12+is)|^2\,dm_\infty(s)\;<\;\infty.$$
En particular $\nu(\mathbb{R})<\infty$ y todas las integrales $\Delta_n=\int|\mathcal{P}_n|^2d\nu$ son finitas.

*Demostración.* La primera desigualdad es $0\leq\tilde g\leq|\zeta|^2$ puntual (Doc 83, Cor. 1.2: $|\zeta_{\rm on}|^2\leq|\zeta|^2$, luego $\tilde g=|\zeta|^2-|\zeta_{\rm on}|^2\leq|\zeta|^2$). Para la segunda: por convexidad $|\zeta(\tfrac12+it)|\ll(1+|t|)^{1/4+\varepsilon}$ [Ti86, cap. V] — cualquier cota polinomial sirve — y por Stirling $|\Gamma(\tfrac14+\tfrac{is}{2})|^2\leq C(1+|s|)^{-1/2}e^{-\pi|s|/2}$ [Ti86, §4.42], de modo que el integrando está dominado por $C\,s^{2k}(1+|s|)^{1/2+2\varepsilon}e^{-\pi|s|/2}$, integrable. $\square$

**Observación 2.2.** El argumento esquiva por completo la discusión "¿es $\sum_j\delta_j^2K(\gamma_j)$ finita bajo ¬RH con infinitos cuádruplos?": no hace falta sumar sobre ceros, porque $\tilde g\leq|\zeta|^2$ da la dominación global de una vez. La masa de $\nu$ es finita **sea cual sea** la configuración de ceros off-críticos. (Lo que *no* es finito en general es $\int\tilde g(s)\,ds$ — la masa *sin* el peso $w$ —; véase §4.3. La distinción es exactamente la que decide qué rutas analíticas cierran y cuáles no.)

**Lema 2.3 (crecimiento de momentos y Carleman para toda la familia).** Con $\mu_{2k}(\sigma)$ los momentos de cualquiera de las medidas $\sigma\in\{m_\infty,\ m_{\rm full},\ m_{\rm full,on},\ \nu\}$:
$$\mu_{2k}(\sigma)\;\leq\;C_\varepsilon\int_0^\infty s^{2k+1/2+2\varepsilon}e^{-\pi s/2}\,ds\;\leq\;C'_\varepsilon\,\Gamma(2k+2)\Bigl(\tfrac{2}{\pi}\Bigr)^{2k},$$
de donde $\mu_{2k}(\sigma)^{1/(2k)}\leq C''\,k$ y por tanto $\sum_k\mu_{2k}(\sigma)^{-1/(2k)}=\infty$: **todas** estas medidas satisfacen la condición de Carleman y sus problemas de momentos de Hamburger son determinados [Ak65, cap. 2; Si98, §1 y §4].

---

## §3. La tensión Carleman vs. Doc 63 Cor. 1.2 — resolución

Éste es el corazón conceptual. El encargo detectó una contradicción aparente: el Doc 63 Cor. 1.2 afirma $K_n(\gamma_n,\gamma_n)\to\pi/2$ (¡la suma $\sum_k|\mathcal{P}_k(x)|^2$ *convergería*!), mientras que la teoría de momentos dice que para medidas determinadas sin átomos esa suma debe diverger. La teoría de momentos gana.

**Teorema 3.1 (determinación, exacta e incondicional).** El problema de momentos de $dm_\infty$ es determinado. Más aún, vale el criterio de Carleman en forma de Jacobi con los coeficientes exactos:
$$\sum_{n\geq0}\frac{1}{a_n^\infty}=\sum_{n\geq0}\frac{2}{\sqrt{(2n+1)(2n+2)}}\;\geq\;\sum_{n\geq0}\frac{1}{n+1}=\infty,$$
y $\sum 1/a_n=\infty$ implica que la matriz de Jacobi es esencialmente autoadjunta y el problema es determinado [Ak65, cap. 1, Addenda; Si98, Cor. 3.3 y discusión del criterio de Carleman; Be68].

**Teorema 3.2 ($K_n(x,x)\to\infty$ en todo punto).** Para todo $x\in\mathbb{R}$ fijo:
$$K_n(x,x)=\sum_{k=0}^{n}\mathcal{P}_k(x)^2\;\longrightarrow\;\infty,\qquad \lambda_n(x)=\frac{1}{K_n(x,x)}\longrightarrow 0.$$

*Demostración.* Para medidas determinadas, la función de Christoffel converge a la masa puntual: $\lim_n\lambda_n(x)=\mu(\{x\})$ para todo $x\in\mathbb{R}$ [Ak65, cap. 2; Si98, §4: en el caso determinado, $\sum_k\mathcal{P}_k(x)^2<\infty$ si y sólo si $x$ es autovalor del único operador de Jacobi autoadjunto, i.e. un átomo de la medida espectral — y la masa del átomo es $(\sum_k\mathcal{P}_k(x)^2)^{-1}$]. La medida $dm_\infty=w\,ds$ es absolutamente continua, sin átomos; luego $\lambda_n(x)\to0$ y $K_n(x,x)\to\infty$ para **todo** $x$. $\square$

**Corolario 3.3 (refutación del Doc 63, Cor. 1.2, y de P39, Prop. `prop:christoffel`).** Las afirmaciones "$K_n(\gamma_n,\gamma_n)\to\pi/2$" y "$\lambda_n(\gamma_n)\to2/\pi$" son **falsas**. Con ellas caen:
- P39, Prop. `prop:christoffel` (mismo enunciado).
- P39, Cor. `cor:T_positive` (su prueba usa "$K_m(s,s)\approx\pi/2$ en el bulk" *y* la forma espuria `eq:abel`; doblemente inválida).
- La discusión cuantitativa de la C.P.-O. del Doc 63 §2 en la medida en que usa el valor $2/\pi$ como escala (la conclusión cualitativa "la localidad falla" se mantiene, ahora con más razón).

**Diagnóstico del error.** El Doc 63 §1 comete dos errores independientes:
1. Usa la densidad arcoseno $\rho_n^{\rm eq}(s)=\tfrac{n}{\pi a_n\sqrt{1-(s/a_n)^2}}$, que es la medida de equilibrio del intervalo **sin campo externo** (caso Chebyshev, o límite $\alpha\to\infty$ de Freud). Para un peso con decaimiento exponencial *lineal* ($Q(s)\asymp|s|$, "$\alpha=1$"), la densidad límite correcta es de tipo Ullman con **singularidad logarítmica en el origen**: para coeficientes de recurrencia con crecimiento lineal $a_n\sim cn$, la distribución contraída de ceros de $\mathcal{P}_n$ es $\int_0^1\omega_{[-2ct,2ct]}\,dt$, cuya densidad en $x$ diverge como $\tfrac{1}{2\pi c}\log\tfrac{1}{|x|}$ cuando $x\to0$ [KvA99; vA87]. No hay "densidad $\approx$ constante" en el bulk cerca del origen.
2. Omite el factor del peso en la asintótica de Christoffel: en los regímenes donde la asintótica vale, $\lambda_n(x)\approx w(x)/\rho_n(x)$, no $1/\rho_n(x)$ [LL01; Si11, cap. 3; To00].

Con ambos corregidos, la predicción consistente con la teoría es
$$K_n(x,x)\;\asymp\;\frac{\log n}{w(x)}\cdot C(x)\qquad(x\ \text{fijo},\ n\to\infty),$$
divergencia *logarítmica* — coherente con que Carleman valga "justo" ($\sum1/a_n\sim\sum1/n$, divergencia logarítmica: el peso $e^{-\pi|s|/2}$ está exactamente en la frontera de determinación, como $e^{-|x|}$). **[Estatus: la divergencia $K_n\to\infty$ es teorema (3.2); la tasa $\log n$ es la predicción de la teoría de equilibrio vía [KvA99] y no se usa en nada de lo que sigue — se consigna como NO VERIFICADO en el sentido de que no damos prueba de la tasa.]**

**Conclusión de la tensión.** No hay medida indeterminada aquí (eso ocurriría con decaimiento $e^{-|s|^\alpha}$, $\alpha<1$); estamos en el caso determinado-frontera. El Doc 63 Cor. 1.2 era el segundo error estructural del mismo documento (la auditoría 114 ya había encontrado que §7.1 contradice §3.2). La ironía técnica: **la determinación, que destruye la "escala de Christoffel $\pi/2$", es exactamente el mecanismo que repara el criterio** (§5).

---

## §4. La ruta analítica "$\Delta_n\to0$": por qué NO cierra tal como se propuso

El encargo proponía: probar $\Delta_n\to0$ para *cualquier* medida finita no-negativa $\nu$, y concluir de $\Delta_n=$ const que la constante es $0$. Esa ruta, literalmente, es **falsa**, y conviene dejar constancia exacta de por qué — porque el modo en que falla señala la reparación correcta.

### 4.1. Contraejemplo a "$\Delta_n\to0$ para toda medida finita"

**Observación 4.1.** Tómese $\nu=m_\infty$ (finita, no-negativa, par, con todos los momentos). Entonces $\Delta_n=\int|\mathcal{P}_n|^2\,dm_\infty=1$ para todo $n$: constante y **no** tiende a $0$. Por tanto ningún teorema de la forma "$\nu$ finita $\Rightarrow\int|\mathcal{P}_n|^2d\nu\to0$" puede ser cierto, y ninguna asintótica de Plancherel–Rotach puede probarlo. La masa de $\nu$ puede viajar con el soporte efectivo de $\mathcal{P}_n$.

### 4.2. Qué versión analítica sí sería verdadera (y por qué no alcanza)

Si la densidad sin peso $g:=\tilde g=d\nu/(w\,ds)$ fuera integrable Lebesgue, $g\in L^1(ds)$, y si valiera la cota de supremo $\|\mathcal{P}_n^2w\|_{L^\infty(\mathbb{R})}\to0$ (para pesos de Freud con $a_n\asymp n$ la predicción de borde tipo Airy es $\asymp n^{-2/3}$; para el peso exacto Meixner–Pollaczek esto es plausible pero **NO VERIFICADO** en la literatura disponible), entonces
$$\Delta_n=\int\mathcal{P}_n^2\,w\,g\,ds\leq\|\mathcal{P}_n^2w\|_\infty\|g\|_{L^1}\to0,$$
y el criterio cerraría por esta vía *bajo esas dos hipótesis*. Pero:

**Proposición 4.2 ($g\in L^1(ds)$ no es incondicional).** $\int_{\mathbb{R}}\tilde g(s)\,ds<\infty$ se cumple si el número de ceros off-críticos es finito (entonces, lejos de las finitas ordenadas, $R-1\asymp C/s^2$ y $\tilde g\ll s^{-3/2+\varepsilon}$), pero bajo ¬RH con infinitos cuádruplos la suma de contribuciones locales $\sim\sum_j\delta_j^2\,|\zeta_{\rm on}'(\tfrac12+i\gamma_j)|^2$ no está controlada por ninguna cota incondicional disponible ($\sum_j\delta_j^2/\gamma_j^2<\infty$ no lo da; las densidades de ceros tampoco: casi todos los ceros podrían estar apenas fuera de la línea). En el escenario adversarial, $\int_{|s|\leq T}\tilde g\,ds$ puede crecer como $T\,{\rm polylog}\,T$.

De modo que la ruta analítica sólo da un teorema **condicional** ("finitos ceros off-críticos quedan excluidos"), con una hipótesis técnica adicional pendiente. Registrarla tiene valor (§5.6 la subsume), pero no repara el criterio.

### 4.3. La pista que sí sirve: la identidad de Cesàro es *exacta*

La versión Cesàro de la constancia no es una asintótica sino una identidad algebraica:
$$\int_{\mathbb{R}}K_n(s,s)\,d\nu(s)=\sum_{k=0}^{n}\Delta_k=(n+1)\,c\qquad\text{si }\Delta_k\equiv c.$$
No hay que estimar nada: hay que preguntarse qué medidas pueden satisfacer *todas* esas identidades a la vez. Eso convierte el problema analítico en un problema de **momentos** — y los problemas de momentos determinados tienen rigidez. Es la observación que cierra todo, y es puramente algebraica:

---

## §5. El teorema reparado

### 5.1. Constancia de $\Delta_n$ (insumo telescópico)

**Lema 5.1.** Si $\int\kappa_n\,d\nu=0$ para todo $n\geq0$, entonces $\Delta_n=\Delta_0=\sqrt{2\pi}\,\nu(\mathbb{R})=:c$ para todo $n$.

*Demostración.* $\int\kappa_n\,d\nu=(a_n^\infty)^2(\Delta_{n+1}-\Delta_n)$ y $a_n^\infty>0$. Inducción. Todas las integrales son finitas por la Prop. 2.1. El valor de $\Delta_0$ es el Lema 1.1. $\square$

### 5.2. Los cuadrados $\{\mathcal{P}_n^2\}$ son base triangular de los polinomios pares

**Lema 5.2.** Para cada $k\geq0$, $\;{\rm span}\{\mathcal{P}_0^2,\mathcal{P}_1^2,\dots,\mathcal{P}_k^2\}=\{\text{polinomios pares de grado}\leq2k\}$.

*Demostración.* Como $dm_\infty$ es par, $\mathcal{P}_n(-s)=(-1)^n\mathcal{P}_n(s)$ [Sz75, §2.3], luego cada $\mathcal{P}_n^2$ es un polinomio par, de grado exactamente $2n$ (coeficiente líder $\kappa_n^2>0$). Los $k+1$ polinomios $\mathcal{P}_0^2,\dots,\mathcal{P}_k^2$ tienen grados $0,2,\dots,2k$ distintos: son linealmente independientes en un espacio de dimensión $k+1$, luego lo generan, con matriz de cambio triangular. $\square$

### 5.3. Rigidez: la constancia identifica $\nu$ con $c\,m_\infty$

**Teorema 5.3 (rigidez de momentos).** Sea $\nu$ una medida de Borel no-negativa sobre $\mathbb{R}$, par, con todos los momentos finitos, tal que
$$\int_{\mathbb{R}}\mathcal{P}_n(s)^2\,d\nu(s)=c\qquad\text{para todo }n\geq0,$$
con $c=\sqrt{2\pi}\,\nu(\mathbb{R})$ como arriba (en general, $c=\Delta_0$). Entonces
$$\nu\;=\;c\cdot m_\infty\quad\text{como medidas de Borel.}$$

*Demostración.* (i) *Igualdad sobre todos los polinomios.* Por ortonormalidad, $\int\mathcal{P}_n^2\,dm_\infty=1$ para todo $n$; por hipótesis, $\int\mathcal{P}_n^2\,d\nu=c=c\cdot1$. Luego las dos medidas $\nu$ y $c\,m_\infty$ asignan la misma integral a cada $\mathcal{P}_n^2$, y por linealidad y el Lema 5.2, a **todo polinomio par**. Para polinomios impares ambas integrales son $0$ (ambas medidas son pares; $\nu$ es par porque $|\zeta(\tfrac12+is)|^2$ y $|\zeta_{\rm on}(\tfrac12+is)|^2$ lo son, por la ecuación funcional, y $m_\infty$ lo es). Conclusión: $\mu_j(\nu)=c\,\mu_j(m_\infty)$ para todo $j\geq0$.

(ii) *Determinación.* Si $c=0$: $\nu(\mathbb{R})=\mu_0(\nu)=0$, luego $\nu=0=c\,m_\infty$ y terminamos. Si $c>0$: la sucesión $(c\,\mu_j(m_\infty))_j$ satisface Carleman, pues $(c\,\mu_{2k})^{-1/(2k)}=c^{-1/(2k)}\mu_{2k}^{-1/(2k)}$ y $c^{-1/(2k)}\to1$, de modo que la divergencia de $\sum\mu_{2k}^{-1/(2k)}$ (Lema 2.3) la hereda. Una sucesión de Carleman es determinada [Ak65; Si98]: admite **una única** medida positiva representante. Tanto $\nu$ como $c\,m_\infty$ son medidas positivas con esa sucesión de momentos; luego $\nu=c\,m_\infty$. $\square$

**Observación 5.4 (dónde quedó respondida la objeción de la auditoría).** El Doc 114 §8.2 objetó, correctamente: "una medida positiva cuya densidad sea ortogonal a todos los $|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2$ no es automáticamente nula". Exacto: no es nula — es **proporcional a $m_\infty$**. El argumento nuevo que faltaba es la rigidez 5.3. Y nótese qué hace el trabajo: la *determinación* de $m_\infty$ (Carleman con los $a_n^\infty$ exactos de CCM, insumo metapléctico (I-4)). La no-negatividad de $\nu$ (Doc 83) entra en (ii): la unicidad de Carleman es para medidas *positivas*; sin $d\nu\geq0$ el paso fallaría (los problemas de momentos no son rígidos para medidas signadas).

### 5.4. La constante es cero: ceros críticos existen

**Lema 5.5 ($c=0$).** Si $\nu=c\,m_\infty$ con $\nu=\tilde g\,m_\infty$ y $\tilde g$ continua, entonces $\tilde g\equiv c$ en $\mathbb{R}$, y $c=0$.

*Demostración.* (i) $\tilde g$ es continua: $|\zeta(\tfrac12+is)|^2$ es continua; $\xi_{\rm on}$ es entera (producto canónico de género 1 sobre los ceros proyectados $\tfrac12\pm i\gamma_j$, convergente porque $\sum_j(\tfrac14+\gamma_j^2)^{-1}<\infty$ [Ti86, §9.6]; cf. Doc 83 §1.1) y el factor gamma $\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)$ no se anula en la recta crítica, luego $|\zeta_{\rm on}(\tfrac12+is)|^2$ es continua.

(ii) Las dos medidas $\nu$ y $c\,m_\infty$ son absolutamente continuas con densidades de Lebesgue continuas $\tilde g\,w$ y $c\,w$; iguales como medidas $\Rightarrow$ densidades iguales c.t.p. $\Rightarrow$ iguales en todo punto (continuidad). Como $w(s)=(2\pi)^{-2}|\Gamma(\tfrac14+\tfrac{is}{2})|^2>0$ para **todo** $s$ ($\Gamma$ no tiene ceros), se cancela: $\tilde g(s)=c$ para todo $s\in\mathbb{R}$.

(iii) Por el teorema de Hardy [Ha14; Ti86, Thm. 10.2] existen (infinitos) ceros de $\zeta$ **sobre** la recta crítica; sea $\gamma_*$ la ordenada de uno de ellos. Entonces $|\zeta(\tfrac12+i\gamma_*)|^2=0$, y también $|\zeta_{\rm on}(\tfrac12+i\gamma_*)|^2=0$ (los ceros críticos se proyectan sobre sí mismos: son ceros de $\xi_{\rm on}$ por construcción). Luego $c=\tilde g(\gamma_*)=0-0=0$. $\square$

### 5.5. El criterio reparado

**Teorema 5.6 (criterio de traza, reparado).** Con $d\nu=dm_{\rm full}-dm_{\rm full,on}\geq0$ y $\kappa_n=(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$, son equivalentes:

  (i) RH;
  (ii') $\displaystyle\int_{\mathbb{R}}\kappa_n\,d\nu=0$ para todo $n\geq0$;
  (ii'') $\Delta_n=\int|\mathcal{P}_n|^2\,d\nu$ es constante en $n$.

*Demostración.* (i)$\Rightarrow$(ii')$\,$: bajo RH, $\zeta_{\rm on}=\zeta$, $d\nu=0$ (insumo I-2), todas las integrales son $0$. (ii')$\iff$(ii''): Lema 5.1 (y trivialmente al revés, multiplicando por $(a_n^\infty)^2$). (ii'')$\Rightarrow$(i): por la Prop. 2.1 los momentos de $\nu$ son finitos; $\nu\geq0$ y par; por el Teorema 5.3, $\nu=c\,m_\infty$; por el Lema 5.5, $c=0$, luego $\nu=0$; por el insumo (I-2) (Doc 89 / Doc 83: $\tilde g\equiv0\Rightarrow R\equiv1\Rightarrow$ cada factor $1+\delta_j^2/(u-\gamma_j)^2\equiv1\Rightarrow\delta_j=0\ \forall j$), RH. $\square$

**Qué NO usa la prueba.** Ni $W_\lambda\geq0$ (falso), ni la forma de Abel espuria, ni la escala de Christoffel (falsa), ni PPP (genéricamente falso), ni localidad, ni ninguna asintótica de $\mathcal{P}_n$. Usa: ortonormalidad, paridad, telescopía, Carleman, Hardy, y $d\nu\geq0$. Todos los insumos están auditados o son clásicos.

**Comparación con la conclusión original.** P39 afirmaba RH $\iff T_\lambda=0\ \forall\lambda$. El criterio reparado tiene la **misma conclusión con la familia por-índice**, que es la información que los saltos de $\{T_\lambda\}_\lambda$ pretendían codificar. La relación exacta entre ambas formas es la salvedad siguiente.

### 5.6. Salvedad 1: la forma-$\lambda$ y los bloques de ordenadas coincidentes

**Proposición 5.7.** Sea $T_\lambda:=\int W_\lambda\,d\nu$ (definición vinculante, insumo I-3), con $W_\lambda=\sum_{\gamma_n\leq\lambda}\kappa_n$ y $\{\gamma_n\}$ la lista de ordenadas de los ceros de $\xi$ **con multiplicidad**, en orden no decreciente.

(a) Si las $\gamma_n$ son dos a dos distintas, entonces $T_\lambda=0\ \forall\lambda\iff$ (ii') $\iff$ RH.

(b) Bajo ¬RH las $\gamma_n$ **nunca** son dos a dos distintas: cada cero off-crítico $\rho=\beta+i\gamma$ viene acompañado de $1-\bar\rho=(1-\beta)+i\gamma$ con la **misma** ordenada, de modo que $\gamma$ aparece (al menos) dos veces en la lista. En ese caso $T_\lambda=0\ \forall\lambda$ sólo entrega las sumas por bloques
$$\sum_{n\in B_i}(a_n^\infty)^2(\Delta_{n+1}-\Delta_n)=0\qquad\text{para cada bloque }B_i\text{ de ordenadas iguales},$$
que no fuerzan la constancia de $\Delta_n$ (un parámetro libre por bloque).

*Demostración.* (a) Los saltos de $\lambda\mapsto T_\lambda$ en los puntos $\gamma$ distintos recuperan cada $\int\kappa_n\,d\nu$ individualmente; aplíquese el Teorema 5.6. (b) Inspección de la ecuación funcional $\xi(s)=\xi(1-s)$ y de la definición de $W_\lambda$: al cruzar $\lambda=\gamma$ entran a la suma *todos* los $n$ del bloque a la vez. $\square$

**Gap declarado (G-118.1).** La implicación "$T_\lambda=0\ \forall\lambda\Rightarrow$ RH" **en la forma-$\lambda$ literal** queda sin demostración cuando hay bloques, es decir, exactamente en el escenario ¬RH que se quiere excluir. Lo que se obtiene en ese escenario es: $\Delta_n$ constante salvo derivas a través de los bloques, con $\Delta_{n+1}-\Delta_n$ ligados dentro de cada bloque por los pesos $(a_n^\infty)^2$. La rigidez 5.3 no se aplica porque la familia de funcionales anulados ya no genera todos los polinomios pares (faltan tantas dimensiones como bloques). **Recomendación normativa:** enunciar el criterio del programa en la forma por-índice (ii')/(ii'') — que es además la forma que P39 ya listaba como ítem (iii) y la que D72 computa término a término — y tratar la forma-$\lambda$ como corolario válido bajo separación de ordenadas. Nada del contenido aritmético se pierde con este cambio.

### 5.7. Salvedad 2: linealizado vs. exacto

El presente documento repara el criterio para la traza **linealizada** $T_\lambda=\int W_\lambda\,d\nu$, i.e. la familia $\int\kappa_n\,d\nu=L_n[\tilde g]$ (P39, Thm. `thm:CD`). La identificación de $\int\kappa_n\,d\nu$ con la discrepancia de Jacobi *exacta* $\Delta_n^{\rm full}-\Delta_n^{\rm full,on}=(a_n^{\rm full})^2-(a_n^{\rm full,on})^2$ es una linealización (primer orden en la perturbación de momentos; el propio Doc 63 §3 la llama "exacta (primer orden)" — una contradicción de términos que conviene corregir). Para el criterio exacto no hace falta nada de este documento:

**Observación 5.8 (el criterio exacto ya era correcto).** RH $\iff(a_n^{\rm full})^2=(a_n^{\rm full,on})^2\ \forall n$: la dirección $\Leftarrow$ es determinación de $m_{\rm full}$ y $m_{\rm full,on}$ (ambas Carleman, Lema 2.3: dos medidas determinadas con los mismos coeficientes de Jacobi y la misma masa coinciden) más el argumento de Hadamard de P39 ((iii)$\Rightarrow$(i), que la auditoría no objetó); la dirección $\Rightarrow$ es trivial. Cuidado con un punto fino: los coeficientes de Jacobi no ven la masa total; la igualdad de masas $m_{\rm full}(\mathbb{R})=m_{\rm full,on}(\mathbb{R})$ debe añadirse como condición $n=-1$ o normalizarse — bajo ¬RH, de hecho, $m_{\rm full}(\mathbb{R})>m_{\rm full,on}(\mathbb{R})$ por el Doc 83, así que la condición de masa ya es un detector. (Esto de paso refuta el Lema 4.1 del Doc 63, que afirmaba "ambas medidas tienen la misma masa total por construcción": falso — contradice el Cor. 1.3 del Doc 83 salvo bajo RH. Tercera inconsistencia interna del Doc 63.)

---

## §6. Qué contenido tiene el criterio reparado (y cuál era espurio)

### 6.1. El colapso trivial que el encargo anticipó

Con el kernel de Christoffel–Darboux $K_N(s,s)=\sum_{k\leq N}|\mathcal{P}_k|^2\geq0$ se puede definir $\widetilde T_N:=\int K_N\,d\nu=\sum_{k\leq N}\Delta_k$. Como cada $\Delta_k\geq0$ y $\Delta_0=\sqrt{2\pi}\,\nu(\mathbb{R})$:
$$\widetilde T_N=0\ \text{para un solo }N\iff\nu(\mathbb{R})=0\iff\text{RH}.$$
Cierto — y **trivial**: es la tautología "$\nu=0\iff$ RH" disfrazada, disponible desde el Doc 83 sin polinomio alguno. Si la reparación hubiera terminado ahí, el criterio habría muerto por vacuidad. No es el caso:

### 6.2. El contenido no trivial del criterio reparado

1. **Rigidez (Teorema 5.3).** "La única medida positiva finita con $\int\mathcal{P}_n^2\,d\nu$ constante es $c\,m_\infty$" es un teorema de unicidad genuino sobre el problema de momentos de la medida CCM, que usa de manera esencial el insumo metapléctico ($a_n^\infty$ exactos $\Rightarrow$ Carleman exacto). No es tautológico: la familia $\{\kappa_n\}$ tiene media nula contra $dm_\infty$ ($\int W_\lambda\,dm_\infty=0$, Doc 114 §1), así que el criterio no "ve" la masa de $\nu$ por positividad — la ve por **completitud** de los cuadrados $\{\mathcal{P}_n^2\}$ junto con la determinación. El kernel indefinido no era un defecto fatal sino la señal de que el mecanismo correcto nunca fue la positividad.
2. **Computabilidad aritmética (D72).** Cada $\int\kappa_n\,d\nu=L_n[\tilde g]$ admite la lectura por la fórmula explícita de Weil con función de prueba $h_n=\kappa_n\,w/(a_n^\infty)^2$ (par, decaimiento más que suficiente; la validez de la fórmula no requiere ningún signo de $h_n$). La familia reparada es entonces una familia de identidades aritméticas ceros/primos indexada por $n$ — el contenido que el programa buscaba. Véase §8.3.
3. **Sin versión de un solo índice.** El afilado del Doc 103 ("un solo $\lambda_0$ basta") está muerto y **no es resucitable** en esta vía: finitos funcionales $\int\kappa_n\,d\nu=0$ son finitas condiciones lineales sobre $\nu$, que medidas positivas no nulas pueden satisfacer (los $\kappa_n$ son indefinidos). La cuantificación universal en $n$ es esencial — coherente con el "master quantifier" de P43: el criterio reparado vuelve a ser una inversión de cuantificador (toda la familia, no un promedio finito).

### 6.3. Qué se perdió

- $T_\lambda\geq0$ y "$T_\lambda\to+\infty$ bajo ¬RH" (P39 Cor. `cor:T_positive`): perdidos. Bajo ¬RH hoy sólo se sabe que **no todos** los $\int\kappa_n\,d\nu$ se anulan; su signo individual es indefinido y no hay cota inferior cuantitativa.
- Toda lectura de "positividad detectora" (CTP como *positividad*): el invariante reparado detecta ¬RH por *no-anulación*, no por signo.
- La cadena Fourier del Doc 76 y el kernel cerrado de P40/P42 (ledger L6): heredan la forma espuria; deben recalcularse con la forma correcta del Doc 114 §3 (en particular $\widehat{W_\lambda dm_\infty}(0)=0$).

---

## §7. Auditoría de la "ruta Poisson" (Doc 63, §6)

La auditoría 114 dejó esta ruta como "único soporte alternativo concebible" de $T_\lambda\geq0$. Veredicto: **CAE**, por tres razones independientes.

1. **Su premisa está refutada.** La Prop. 6.1 del Doc 63 deriva $\Delta_n^{\rm full}-\Delta_n^{\rm full,on}\geq0$ *asumiendo el PPP* ($F_n(z)=c_n/(z-\gamma_n)+R_n$, $c_n>0$). El propio programa probó después (D68–D69; P39, Thm. `thm:wronskian` y Cor. `cor:ppp_exact`) que $F_n=-1/(a_n^\infty\mathcal{P}_n\mathcal{P}_{n+1}m_\infty)$ es **holomorfa** en $\gamma_n$ salvo coincidencia exacta de $\gamma_n$ con un nodo de Gauss: el PPP exacto es genéricamente falso. Premisa muerta, conclusión sin soporte.
2. **El "resto" nunca se controló.** Aun concediendo una forma asintótica de PPP, la Prop. 6.1 escribe "$=c_n'\,C_\infty(\gamma_n)+\text{resto}$" sin cota alguna del resto; como $C_\infty(\gamma_n)$ puede ser arbitrariamente pequeño (ceros off-críticos lejanos), ningún signo se sigue.
3. **Contradicción interna doble.** (a) La conclusión "$\Delta_n^{\rm full}-\Delta_n^{\rm full,on}\geq0$ para cada $n$" contradice la Obs. 2.2 del mismo documento ($\kappa_n$ indefinido + $d\nu\geq0$ $\Rightarrow$ signo término a término indefinido), como ya señaló el Doc 114 §8.3. (b) El Lema 4.1 del Doc 63 ("misma masa total") contradice el Doc 83 (bajo ¬RH, $\nu(\mathbb{R})>0$): véase Obs. 5.8. El §6 del Doc 63 debe retirarse íntegro.

Con esto, **ningún** camino hacia "$T_\lambda\geq0$" sobrevive en el corpus — y ninguno hace falta: el Teorema 5.6 reemplaza la positividad por rigidez.

---

## §8. Impacto

### 8.1. P39 (`06-papers/P39-ccm-trace-criterion/main.tex`)

| Ítem | Estado post-118 |
|---|---|
| `prop:positivity`, `thm:rate`, `cor:mertens`, `thm:CD`, `rem:oscillation` | Sobreviven (no tocados por 114 ni por 118) |
| `prop:christoffel` ($\lambda_n(\gamma_n)\to2/\pi$, $K_n\to\pi/2$) | **RETIRAR — FALSO** (Cor. 3.3; nuevo daño detectado por este documento) |
| `thm:Wpos`, `eq:abel` | RETIRAR (Doc 114) |
| `thm:main` | **Reemplazar la prueba**: (i)$\iff$(iii) vía Obs. 5.8 (con la condición de masa explícita); (i)$\iff$(ii',ii'') vía Teorema 5.6; la forma-$\lambda$ (ii) sólo bajo separación de ordenadas (Prop. 5.7, gap G-118.1) |
| `cor:T_positive` (crecimiento $T_\lambda\gtrsim N(\lambda)$) | **RETIRAR** (usa `eq:abel` *y* `prop:christoffel`, ambas falsas) |
| `prop:no_exact_pcn`, `thm:wronskian`, `prop:Fn_closed`, `cor:ppp_exact` | Sobreviven |
| Abstract y §"Summary": ítems 5 (escala $2/\pi$), 7, 8, 10 | Corregir/retirar; ítem 9 (la equivalencia) se mantiene con el enunciado por-índice y la prueba nueva |
| "dm_∞ is a probability measure" | Corregir: $m_\infty(\mathbb{R})=(2\pi)^{-1/2}$ (Lema 1.1) |

### 8.2. P40 (`P40-three-paths-dnu`)

- **Path I**: $d\nu\geq0$ sobrevive (Doc 83). La cota "$T_\lambda\geq2\sum_j\delta_j^2K_\lambda(\gamma_j)>0$" y todo uso de $W_\lambda>0$ (abstract; sec1-3 líneas 31, 59–60, 82; sec6-7 Teorema de síntesis, equivalencia (2)$\iff$(4) y líneas 142–148, 177, 252–255, 485–490): **retirar**; la equivalencia (2)$\iff$(4) del teorema de síntesis puede re-probarse con el Teorema 5.6 sustituyendo la forma-$\lambda$ por la forma por-índice.
- **Path II** (Jensen, $F(z)=\xi(z/(z-1))$): independiente de $W_\lambda$; sobrevive.
- **Path III**: la completitud "en $L^2(W_\lambda\,dm_\infty)$" está mal planteada ($W_\lambda\,dm_\infty$ no es una medida positiva): reformular con $|W_\lambda|\,dm_\infty$ o con $K_N\,dm_\infty$; la parte DBN ($\Lambda\geq0$ [RT20], $\Lambda=0\iff$ RH) sobrevive.
- La "Hadamard barrier" como conclusión estructural no cambia: el criterio reparado sigue requiriendo conocer $\nu$ (las posiciones de los ceros) para evaluarse.

### 8.3. D72 (fórmula aritmética de la traza)

La fórmula explícita de Weil con $h_\lambda=W_\lambda\,w/\pi$ es una **identidad** válida tal cual: la fórmula de Weil exige paridad, analiticidad en la franja y decaimiento de la función de prueba, **no** positividad. Sobrevive con dos cambios de estatus: (a) toda inferencia de signo a partir de ella queda retirada; (b) la versión útil es ahora por-índice: $h_n=\kappa_n\,w/(a_n^\infty)^2$, una identidad aritmética por cada $n$, cuya anulación simultánea es RH (Teorema 5.6). D72 pasa de "fórmula de un invariante positivo" a "lado aritmético del criterio reparado". Cualquier pasaje de D72 que haya usado la forma de Abel espuria de $W_\lambda$ para computar (en lugar de la definición) debe revisarse contra la forma correcta del Doc 114 §3.

### 8.4. P43 — ledger L1–L8

- **L1** ($d\nu\geq0$): sobrevive.
- **L2** (criterio de escala única, $W_\lambda>0$ $\Rightarrow$ un solo $\lambda_0$ basta): **MUERTO** (Doc 114 + §6.2.3: no resucitable). Sustituir por el criterio reparado: "RH $\iff\int\kappa_n\,d\nu=0\ \forall n$, por rigidez de momentos" — con cuantificador universal esencial, lo que de hecho *refuerza* la tesis del master quantifier de P43.
- **L3, L4, L5** (índice tensorial, realización del cuadrado tensorial, positividad sub-resolución): independientes de $W_\lambda$; no afectados por 114/118 (L3 sujeto a su propia auditoría, Doc 117).
- **L6** (kernel cerrado $B_{\lambda_0}$, sech$^{1/2}$): **recalcular** — se derivó vía la cadena Fourier del Doc 76, refutada en bloque (Doc 114 §8.4). Hasta recálculo, no citable.
- **L7** (ocho reformulaciones de $d\nu$, Doc 89 + puente P35): las reformulaciones basadas directamente en $d\nu$ sobreviven; las que pasan por "$T_\lambda=0$ con $W_\lambda>0$" deben remitirse al Teorema 5.6; P35 independiente.
- **L8** (objetivo de densidad de cuádruplos): independiente; sobrevive.

### 8.5. P44 y otros

P44 (arquitectura de dos lemas: $m<\infty$ + rigidez secuencial LP-112) no usa $W_\lambda$ ni $T_\lambda\geq0$: **no afectado**. Nota positiva para su ledger: el Teorema 5.6 es un resultado incondicional nuevo del tipo que P44 cataloga (una rigidez que convierte una familia numerable de identidades en RH). Doc 103: permanece retirado íntegro (salvo Lema 2.1). Doc 76: recalcular. P41: los usos del "colapso a un punto" siguen retirados (Doc 114 §8.6) y no son recuperables (§6.2.3).

---

## §9. Veredicto final

**CRITERIO REPARADO.**

- La dirección que la auditoría 114 dejó sin demostración queda probada, incondicionalmente, en la forma por-índice: $\int\kappa_n\,d\nu=0\ \forall n\Rightarrow\nu=c\,m_\infty$ (rigidez de momentos, Carleman con los $a_n^\infty$ exactos de CCM) $\Rightarrow c=0$ (Hardy + continuidad) $\Rightarrow\nu=0\Rightarrow$ RH. Misma conclusión que P39 perseguía, vía nueva, sin $W_\lambda\geq0$.
- La tensión Carleman vs. Doc 63 Cor. 1.2 se resuelve **contra** el Doc 63: $dm_\infty$ es determinada ($\sum1/a_n^\infty=\infty$, exacto), es absolutamente continua, luego $K_n(x,x)\to\infty$ en todo punto; "$K_n(\gamma_n,\gamma_n)\to\pi/2$" es falso (errores: densidad arcoseno en lugar de Ullman-$\alpha{=}1$ con singularidad logarítmica, y peso omitido). Caen además P39 `prop:christoffel` y `cor:T_positive`.
- La ruta analítica "$\Delta_n\to0$ para toda medida finita" propuesta en el encargo es falsa tal cual ($\nu=m_\infty$, $\Delta_n\equiv1$); su núcleo correcto era algebraico, no asintótico.
- La ruta Poisson del Doc 63 §6 cae (PPP genéricamente falso + resto sin cota + dos contradicciones internas, incluida la masa total del Lema 4.1 contra el Doc 83).
- Gaps declarados: **(G-118.1)** la forma-$\lambda$ literal ("$T_\lambda=0\ \forall\lambda$") sólo implica la familia por-índice bajo separación de ordenadas, que ¬RH viola automáticamente (pares $\beta,1-\beta$); la forma por-índice es la formulación normativa del criterio. **(G-118.2)** El criterio reparado es sobre la traza linealizada $T_\lambda:=\int W_\lambda\,d\nu$; la versión con coeficientes de Jacobi exactos es un criterio correcto pero distinto (Obs. 5.8, vía determinación de $m_{\rm full}$, con la condición de masa explícita).

El criterio sigue siendo una *reformulación* de RH, no un avance hacia su prueba: evaluar $\int\kappa_n\,d\nu$ exige las posiciones de los ceros (barrera de Hadamard intacta, master quantifier intacto: cuantificador universal en $n$ irreductible). Pero la reformulación vuelve a estar **demostrada**, que es lo que estaba roto.

---

## §10. Tabla de veredictos

| Enunciado | Veredicto |
|---|---|
| RH $\iff\int\kappa_n\,d\nu=0\ \forall n$ (forma por-índice) | **PROBADO** (Teorema 5.6; rigidez de momentos + Hardy) |
| RH $\iff\Delta_n=\int\mathcal{P}_n^2\,d\nu$ constante en $n$ | **PROBADO** (equivalente a lo anterior) |
| RH $\iff T_\lambda=0\ \forall\lambda$ (forma-$\lambda$ literal) | Probado bajo separación de ordenadas; **GAP G-118.1** en general (¬RH crea bloques automáticos) |
| RH $\iff(a_n^{\rm full})^2=(a_n^{\rm full,on})^2\ \forall n$ + igualdad de masas (criterio exacto) | **PROBADO** (Obs. 5.8; ya esencialmente en P39 (iii)$\Rightarrow$(i)) |
| $\nu(\mathbb{R})<\infty$ y todos los momentos de $\nu$ finitos | **PROBADO**, incondicional (Prop. 2.1) |
| $dm_\infty$ determinada (Carleman, $\sum1/a_n^\infty=\infty$ exacto) | **PROBADO** (Teorema 3.1) |
| Doc 63 Cor. 1.2 / P39 `prop:christoffel` ($K_n(\gamma_n,\gamma_n)\to\pi/2$) | **REFUTADO** ($K_n(x,x)\to\infty$ en todo punto, Teorema 3.2) |
| P39 `cor:T_positive` ($T_\lambda\gtrsim N(\lambda)$ bajo ¬RH) | **RETIRADO** (doble dependencia de enunciados falsos) |
| "$\Delta_n\to0$ para toda medida finita $\nu\geq0$" (ruta propuesta) | **FALSO** (contraejemplo $\nu=m_\infty$, Obs. 4.1) |
| Ruta Poisson, Doc 63 §6 | **CAE** (premisa PPP refutada; resto sin cota; 2 contradicciones internas) |
| Doc 63 Lema 4.1 ("misma masa total") | **REFUTADO** (contradice Doc 83 bajo ¬RH) |
| $\mathcal{P}_n=$ Meixner–Pollaczek $(\lambda{=}\tfrac14,\phi{=}\tfrac\pi2)$, $x=s/2$ | **PROBADO** (Prop. 1.2) |
| $m_\infty(\mathbb{R})=(2\pi)^{-1/2}$; $\mathcal{P}_0=(2\pi)^{1/4}$; $\Delta_0=\sqrt{2\pi}\,\nu(\mathbb{R})$ | **PROBADO** (Lema 1.1; corrige "probability measure" de P39) |
| Afilado a un solo índice/escala (Doc 103 §4) | **NO RESUCITABLE** por esta vía (§6.2.3) |
| D72 (fórmula de Weil para la traza) | Sobrevive como identidad; reinterpretada por-índice (§8.3) |
| P43 ledger: L1, L3–L5, L7 (parcial), L8 | Sobreviven |
| P43 ledger: L2 | **MUERTO**; sustituir por el criterio reparado |
| P43 ledger: L6 | **RECALCULAR** (hereda Doc 76) |

---

## Apéndice A. Verificaciones de sanidad del Teorema 5.6

La auditoría 114 demostró que los errores del programa sobreviven cuando nadie rehace los cálculos en grado bajo. Aplicamos el estándar al teorema nuevo.

**A.1. La rigidez en grado bajo.** Con $\mathcal{P}_0=(2\pi)^{1/4}$, $\mathcal{P}_1=(2\pi)^{1/4}\sqrt2\,s$, $\mathcal{P}_2=(2\pi)^{1/4}\sqrt{\tfrac23}(s^2-\tfrac12)$ (recurrencia con $a_0=\tfrac{1}{\sqrt2}$, $a_1=\sqrt3$; los del Doc 114 §4 multiplicados por la normalización del Lema 1.1 — el factor común $(2\pi)^{1/4}$ no altera ninguna conclusión de la auditoría, que trabajó con $\mathcal{P}_0\equiv1$ por la convención de masa unitaria de P39). Supongamos $\Delta_0=\Delta_1=\Delta_2=c$ para una medida par $\nu\geq0$:
- $\Delta_0=c$: $\sqrt{2\pi}\,\mu_0(\nu)=c$;
- $\Delta_1=c$: $2\sqrt{2\pi}\,\mu_2(\nu)=c$, luego $\mu_2(\nu)=\tfrac12\mu_0(\nu)=c\,\mu_2(m_\infty)/\!\sqrt{2\pi}\cdot\sqrt{2\pi}$ — consistente con $\mu_2(m_\infty)/\mu_0(m_\infty)=\tfrac12$ (§1.1);
- $\Delta_2=c$: $\tfrac23\sqrt{2\pi}\,(\mu_4-\mu_2+\tfrac14\mu_0)(\nu)=c$, que con las dos anteriores despeja $\mu_4(\nu)$ y reproduce $\mu_4(\nu)/\mu_0(\nu)=\mu_4(m_\infty)/\mu_0(m_\infty)$ (usando $(a_0a_1)^2$-momentos de la recurrencia: $\mu_4/\mu_0=(a_0^2)(a_0^2+a_1^2)=\tfrac12\cdot\tfrac72=\tfrac74$).

El patrón triangular del Lema 5.2 es visible: cada $\Delta_k=c$ nuevo despeja exactamente el momento $\mu_{2k}(\nu)$ y lo iguala a $c\,\mu_{2k}(m_\infty)/\!\sqrt{2\pi}\cdot\sqrt{2\pi}$; ninguna condición es redundante y ninguna sobra.

**A.2. Por qué $\nu=m_\infty$ no contradice el criterio.** El contraejemplo de la Obs. 4.1 ($\nu=m_\infty$, $\Delta_n\equiv1$) satisface (ii'') con $c=1\neq0$ — y el Teorema 5.3 da, correctamente, $\nu=c\,m_\infty$ con $c\neq0$. La conclusión RH **no** se sigue para esa $\nu$, ni debe: $m_\infty$ no es de la forma $\tilde g\,m_\infty$ con $\tilde g=|\zeta|^2-|\zeta_{\rm on}|^2$, porque $\tilde g\equiv1$ exigiría $|\zeta(\tfrac12+i\gamma_*)|^2-|\zeta_{\rm on}(\tfrac12+i\gamma_*)|^2=1$ en un cero crítico $\gamma_*$, donde ambos términos se anulan. El Lema 5.5 es exactamente el eslabón que usa la *aritmeticidad* de $\nu$ (que su densidad se anula en los ceros críticos), y es el único lugar de toda la prueba donde entra $\zeta$. La división del trabajo es nítida: teoría de momentos $\Rightarrow$ "$\nu$ es un múltiplo de $m_\infty$"; teorema de Hardy $\Rightarrow$ "el múltiplo es cero".

**A.3. Chequeo de la media nula.** El criterio reparado respeta la identidad gratis del Doc 114 §1: $\int\kappa_n\,dm_\infty=0$, de modo que la familia (ii') se anula idénticamente cuando $\nu$ se reemplaza por $m_\infty$ — coherente con A.2: la familia no distingue $\nu=0$ de $\nu=c\,m_\infty$; quien distingue es Hardy.

---

## Apéndice B. La contabilidad diádica completa de la ruta analítica (§4.2)

Registramos el cálculo que muestra por qué ninguna cota de envolvente de Plancherel–Rotach puede dar $\Delta_n\to0$ sin $g\in L^1(ds)$, para que la ruta no se reintente sin la hipótesis.

Partición en intervalos unitarios $[m,m+1]$, $0\leq m\lesssim Cn$ (más allá de $C n$ con $C$ grande, la región exterior al intervalo MRS contribuye $O(e^{-cn})$: el polinomio crece como $e^{2n\,U(s/a_n)}$ pero el peso $w^{1/2}$ sobrante decae más rápido para $C$ grande, y $\int w^{1/2}\tilde g\,ds<\infty$ por la Prop. 2.1 con $\varepsilon$-margen). En el bulk:

- envolvente esperada: $\sup_{[m,m+1]}\mathcal{P}_n^2\,w\;\lesssim\;\dfrac{1+\log(n/m)}{n}$ (densidad Ullman-$\alpha{=}1$, §3), con pico de borde $\asymp n^{-2/3}$ en $m\asymp a_n$;
- masa local de $\nu$ sin peso: $\int_m^{m+1}\tilde g\,ds\leq\sup_{[m,m+1]}|\zeta|^2\leq e^{C\log m/\log\log m}=m^{o(1)}$ en el peor caso puntual, pero con la única cota *acumulada* incondicional $\int_0^T\tilde g\,ds$ posiblemente $\asymp T\,{\rm polylog}\,T$ bajo ¬RH adversarial (casi todos los ceros apenas off-críticos: $\sum\delta_j^2/\gamma_j^2<\infty$ lo permite incluso con $\delta_j\asymp\tfrac12-\tfrac{c}{\log\gamma_j}$, pues $\gamma_j\sim2\pi j/\log j$ hace $\sum\gamma_j^{-2}<\infty$).

Entonces $\Delta_n\lesssim\sum_{m\leq Cn}\tfrac{1+\log(n/m)}{n}\int_m^{m+1}\tilde g\,ds$, dominado por $m\asymp n$: $\asymp\tfrac1n\int_0^{Cn}\tilde g\,ds\asymp{\rm polylog}(n)$ en el peor caso — acotado lejos de $0$ no se garantiza, y $\to0$ sólo si $\int_0^T\tilde g\,ds=o(T)$. Los factores $e^{\pm\pi m/2}$ del peso se cancelan exactamente (la envolvente $\mathcal{P}_n^2w$ es plana en el bulk): no hay decaimiento exponencial que explotar. **Conclusión:** la obstrucción de la ruta analítica es la posible masa Lebesgue lineal de $\tilde g$, no la falta de asintóticas; por eso la reparación tenía que ser algebraica.

**Subproducto rescatable (cota de crecimiento condicional).** Si en el futuro se prueba la cota estándar de Christoffel $\lambda_n(x)\leq C\,\tfrac{a_n}{n}\,w(x)$ para $|x|\leq\tfrac12 a_n$ con el peso exacto (es la dirección *fácil*, por polinomio de prueba [LL01; To00]; queda como tarea técnica, **NO VERIFICADA** aquí para el peso Meixner–Pollaczek), entonces de (ii'') y la identidad de Cesàro §4.3 se sigue incondicionalmente
$$\int_{|s|\leq T}\bigl(|\zeta|^2-|\zeta_{\rm on}|^2\bigr)(s)\,ds\;\leq\;C'\,c\,T\qquad\forall T>0,$$
una restricción lineal nueva sobre la masa Lebesgue de la discrepancia bajo la hipótesis del criterio. Tras el Teorema 5.6 es redundante para el criterio mismo ($c=0$), pero la registramos porque sobreviviría en la variante por bloques (Apéndice C), donde el teorema no cierra.

---

## Apéndice C. El escenario de bloques (gap G-118.1) en detalle

Bajo ¬RH con cuádruplos $\{\beta_j\pm i\gamma_j,\,1-\beta_j\pm i\gamma_j\}$, la lista de ordenadas positivas contiene cada $\gamma_j$ con multiplicidad $\geq2$. Supóngase $T_\lambda=0\ \forall\lambda$ (forma-$\lambda$) y sea $B=\{n_0,n_0+1\}$ un bloque de tamaño 2. Con $u_n=(a_n^\infty)^2$ y $d_n=\Delta_{n+1}-\Delta_n$:
$$u_{n_0}d_{n_0}+u_{n_0+1}d_{n_0+1}=0,\qquad d_n=0\ \text{para }n\ \text{fuera de los bloques}.$$
La deriva neta de $\Delta$ a través del bloque es
$$d_{n_0}+d_{n_0+1}=d_{n_0}\Bigl(1-\frac{u_{n_0}}{u_{n_0+1}}\Bigr)=d_{n_0}\cdot\frac{2n_0+\tfrac52}{(a_{n_0+1}^\infty)^2}\;\asymp\;\frac{2\,d_{n_0}}{n_0},$$
un parámetro libre por bloque. Las constancias parciales entre bloques siguen valiendo, así que $\nu$ queda restringida a un subespacio afín de codimensión "número de ordenadas distintas" dentro del espacio de momentos — exactamente *una* dimensión libre por cuádruplo. Lo que falta para cerrar: o bien (a) una condición adicional del marco que fije esas dimensiones (candidata natural: la condición de masa $n=-1$ de la Obs. 5.8, que da una ecuación global, insuficiente para infinitos bloques pero suficiente para **un** cuádruplo si además $d_{n_0}$ tuviera signo conocido — no lo tiene), o bien (b) probar que la forma aritmética de $\nu$ es incompatible con cualquier elección no nula de las derivas (problema abierto, de tipo "densidad de $\{\mathcal{P}_n^2\}_{n\notin B}$ en $L^1(\nu)$" — para medidas determinadas hay resultados de densidad de polinomios en $L^p$ [Si98, §6] pero el subespacio aquí omite grados, y la pregunta es genuinamente distinta). **Caso particular cerrado:** si todos los bloques tienen tamaño 1 — i.e. si ninguna ordenada se repite, lo que bajo ¬RH exigiría $\beta_j=1-\beta_j$, imposible con $\beta_j\neq\tfrac12$ — no hay gap; por eso el gap es exactamente coextensivo con ¬RH y la forma-$\lambda$ no puede repararse por este camino sin idea nueva. La formulación normativa por-índice (Teorema 5.6) lo esquiva por completo.

Obsérvese además que el gap de bloques **no** infecta la dirección ya válida: bajo RH no hay bloques que importen ($d\nu=0$ anula todo), y la equivalencia del Teorema 5.6 es incondicional porque su hipótesis (ii') se formula por índice, no por altura.

---

## Apéndice D. Detalle de la conversión mónica en la Prop. 1.2

De $(n+1)P_{n+1}=2xP_n-(n+2\lambda-1)P_{n-1}$ [KLS (9.7.3) con $\phi=\pi/2$]: el coeficiente líder cumple $k_{n+1}=\tfrac{2}{n+1}k_n$, luego $k_n=2^n/n!$ y $\tilde p_n:=\tfrac{n!}{2^n}P_n$ es mónico. Sustituyendo,
$$x\,\tilde p_n=\frac{n!}{2^n}\,xP_n=\frac{n!}{2^n}\Bigl[\frac{n+1}{2}P_{n+1}+\frac{n+2\lambda-1}{2}P_{n-1}\Bigr]=\tilde p_{n+1}+\frac{n(n+2\lambda-1)}{4}\,\tilde p_{n-1},$$
de donde el cuadrado del coeficiente ortonormal que acopla $n-1\leftrightarrow n$ es $c_n=\tfrac{n(n+2\lambda-1)}{4}$, i.e. (acoplando $n\leftrightarrow n+1$) $a_n^{\rm MP}=\tfrac12\sqrt{(n+1)(n+2\lambda)}$, como se usó. Para $\lambda=\tfrac14$: $a_n^{\rm MP}=\tfrac12\sqrt{(n+1)(n+\tfrac12)}=a_n^\infty/2$ ✓ (la mitad exacta, por el cambio de variable $x=s/2$). La integral de normalización $\int_{\mathbb{R}}|\Gamma(\tfrac14+ix)|^2dx=\pi\sqrt{2\pi}$ del Lema 1.1 coincide con la fórmula de norma de [KLS] en $n=0$, $\lambda=\tfrac14$, $\phi=\tfrac{\pi}{2}$.

---

## Referencias

- [Ak65] N. I. Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver & Boyd, 1965. (Determinación; Carleman; $\lim\lambda_n(x)=\mu(\{x\})$ en el caso determinado.)
- [Be68] Yu. M. Berezanskii, *Expansions in Eigenfunctions of Selfadjoint Operators*, AMS Transl. Math. Monogr. 17, 1968. (Criterio $\sum1/a_n=\infty\Rightarrow$ autoadjunción esencial de la matriz de Jacobi.)
- [Ha14] G. H. Hardy, *Sur les zéros de la fonction $\zeta(s)$ de Riemann*, C. R. Acad. Sci. Paris **158** (1914), 1012–1014.
- [KLS] R. Koekoek, P. A. Lesky, R. F. Swarttouw, *Hypergeometric Orthogonal Polynomials and Their $q$-Analogues*, Springer, 2010, §9.7 (Meixner–Pollaczek).
- [KvA99] A. B. J. Kuijlaars, W. Van Assche, *The asymptotic zero distribution of orthogonal polynomials with varying recurrence coefficients*, J. Approx. Theory **99** (1999), 167–197.
- [LL01] A. L. Levin, D. S. Lubinsky, *Orthogonal Polynomials for Exponential Weights*, Springer, 2001. (Funciones de Christoffel para pesos exponenciales; el factor $w(x)$ y la escala $a_n/n$.)
- [MS84] H. N. Mhaskar, E. B. Saff, *Extremal problems for polynomials with exponential weights*, Trans. Amer. Math. Soc. **285** (1984), 203–234.
- [RT20] B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, Forum Math. Pi **8** (2020), e6.
- [Si98] B. Simon, *The classical moment problem as a self-adjoint finite difference operator*, Adv. Math. **137** (1998), 82–203.
- [Si11] B. Simon, *Szegő's Theorem and Its Descendants*, Princeton Univ. Press, 2011.
- [Sz75] G. Szegő, *Orthogonal Polynomials*, 4.ª ed., AMS Colloq. Publ. 23, 1975. (§2.3: paridad; cap. 3: ceros, entrelazamiento.)
- [Ti86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. Heath-Brown), Oxford, 1986. (Cap. V: convexidad; §4.42: Stirling; §9.6: $\sum\gamma^{-2}<\infty$; Thm. 10.2: Hardy.)
- [To00] V. Totik, *Asymptotics for Christoffel functions for general measures on the real line*, J. Anal. Math. **81** (2000), 283–303.
- [vA87] W. Van Assche, *Asymptotics for Orthogonal Polynomials*, Lecture Notes in Math. 1265, Springer, 1987. (Distribuciones de ceros tipo Ullman para crecimiento lineal de coeficientes.)
- Documentos internos: Doc 61–63, 68–72, 76, 83, 89, 103, 114; papers P35, P39–P44.

---

*Fin del Documento 118.*
