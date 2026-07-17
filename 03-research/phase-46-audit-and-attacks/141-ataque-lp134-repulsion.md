# Doc 141 — Ataque a LP-134 (repulsión de resolución): formalización, mapa, intento de prueba, intento de refutación

**Programa:** Hipótesis de Riemann — Phase 46: AUDITORÍA Y ATAQUES.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** ataque frontal al lema LP-134 del Doc 134 §7.2 — la mitad NUEVA del muro de
uniformidad. El encargo: formalizarlo, mapearlo contra la literatura, intentar probarlo incondicionalmente,
intentar refutarlo, y dar veredicto con consecuencias exactas para la sinergia del D134.

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa; resultados externos citados con
precisión. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con ζ/RH con estatus honesto. **[GAP]** =
declarado. **[DESEO]** = declarado.

**Prerrequisitos leídos en fuente esta sesión:** Doc 134 completo (en particular §4: visibilidad
$\theta_j\asymp\min(1,\delta_j a(\gamma_j))^\kappa$ y (V1)–(V2); §5: tricotomía gordos/finos/sub-resolución,
Teoremas 5.1–5.5, Prop. 5.5bis; §7.2: enunciado semi-formal de LP-134; §7.3: Teorema 7.2 y las dos rutas;
§5.8 M2–M3: DH y $F_{p,\alpha}$).

---

## 0. Resumen ejecutivo

1. **(§1) La formalización descubre un defecto en el enunciado semi-formal: tal como está escrito en D134
   §7.2 ("existe un calendario $a$ y $c>0$..."), LP-134 es TRIVIALMENTE VERDADERO** para toda configuración
   admisible — el calendario adaptado a los ceros siempre existe ([TEOREMA 141.A]). El contenido entero del
   lema vive en fijar el calendario POR ADELANTADO en una clase definible. La forma correcta y canónica es
   $$\textbf{LP-134}:\qquad \liminf_{\rho\ \mathrm{off}}\ \bigl|\beta_\rho-\tfrac12\bigr|\cdot\log\gamma_\rho\;>\;0$$
   (con $\liminf:=+\infty$ si hay finitos ceros off). Jerarquía probada:
   $\mathrm{RH}\Rightarrow m<\infty\Rightarrow\mathrm{LP\text{-}134}$, ambas flechas estrictas como
   implicaciones de mundos: **LP-134 es el enunciado individual MÁS DÉBIL de toda la jerarquía del
   programa** — y aun así, §3 muestra que sigue detrás del muro.

2. **(§2) Mapa exacto contra la literatura.** (a) Toda la tecnología de densidad (Selberg 1946, Jutila)
   muere EXACTAMENTE en la escala $\delta\asymp1/\log T$: no-trivialidad ⟺ $\delta\log T\to\infty$ ([LEMA
   141.M1]). (b) Peor: lo incondicional prueba lo CONTRARIO de una repulsión — el 100% de los ceros (en
   densidad) vive DENTRO del tubo de resolución $|\beta-\tfrac12|\leq\psi(\gamma)/\log\gamma$, $\forall\psi\to\infty$
   ([PROPOSICIÓN 141.M2], clásica). (c) Las estadísticas verticales ($S(t)$, momentos de Selberg,
   $N(T+h)-N(T)$, gaps de Littlewood) son IDÉNTICAMENTE ciegas a LP-134: dependen solo de las ordenadas
   ([LEMA 141.B0]). (d) La repulsión tipo Deuring–Heilbronn no se transpone: la palanca de positividad de
   Landau es idénticamente nula en la línea crítica por la ecuación funcional ([CÁLCULO 141.M4]), y la señal
   de segundo orden de un cuádruplo es un perfil de ancho $\delta$ con INTEGRAL TOTAL CERO ([CÁLCULO
   141.M5]): invisible exactamente — no aproximadamente — para todo promedio más grueso que $\delta$.

3. **(§3) Intento de prueba: FRACASA, y el fracaso es un teorema relativo.** [LEMA 141.B] (ceguera universal
   de la fórmula explícita): un test de soporte $e^{\pm L}$ distingue un cuádruplo a distancia $\delta$ de su
   proyección a la línea en a lo sumo $O((\delta L)^2)$ por unidad de masa. [COROLARIO 141.B2 — no-go
   relativo]: ninguna familia numerable de evaluaciones de funcionales de soporte polinomial
   ($L\ll\log\gamma$) separa los mundos LP-134 de los mundos ¬LP-134 — la premisa del encargo ("LP-134 es un
   enunciado de promedio local, del lado bueno del cuantificador maestro") es **FALSA**: LP-134 cuantifica
   sobre ceros individuales y está del lado individual del muro. El residuo exacto: [GAP-141.G1]. Lo que sí
   se prueba: la forma mínima **LP-141** ("$m=\infty\Rightarrow$ infinitos gordos") basta para la sinergia
   ([PROPOSICIÓN 141.P3]) y tiene DOS fuentes posibles (repulsión o replicación) — es el pivote real.

4. **(§4) Intento de refutación.** Para ζ: imposible incondicionalmente (refutar LP-134 exhibe infinitos
   ceros off — refuta RH; [PROPOSICIÓN 141.R1]); los mundos violadores son consistentes con todo lo conocido
   por encima de la altura de verificación. En la categoría analítica (entera, orden 1, ecuación funcional,
   real en la línea): **LP-134 ES FALSO** — contraejemplo de Hadamard explícito con $m=\infty$ y
   $\delta_j=e^{-\gamma_j}$ ([PROPOSICIÓN 141.R2, prueba completa]). En la categoría con producto de Euler:
   la construcción ingenua (producto de $F_{p_k,\alpha_k}$ con $\delta_k'\to0$) NO continúa analíticamente
   ([CÁLCULO 141.R3]) — la continuación del producto de Euler emerge como el candidato a MECANISMO de
   repulsión ([CONJETURA 141.E]).

5. **(§5) VEREDICTO: ABIERTO-CON-MAPA.** LP-134 no es demostrable con herramientas de promedio (no-go
   relativo), no es refutable sin refutar RH, es falso sin aritmética, y su única evidencia positiva es la
   rigidez de continuación de la clase de Euler. Para la sinergia del D134: la ruta 2 (estricta ∧ LP-134) NO
   es más barata que la ruta 1 (débil ∧ LP-112) — pero el pivote mínimo LP-141 reorganiza el tablero.

---

## 1. Formalización de LP-134

### 1.1. El enunciado semi-formal y su defecto

El Doc 134 §7.2 enuncia: *"Existe un calendario $a(\cdot)$ (p.ej. $a(\gamma)=C\log\gamma$, la resolución
natural) y $c>0$ tales que todo cero no trivial $\rho=\tfrac12+\delta+i\gamma$ de $\zeta$ con $\delta\neq0$
cumple $|\delta|\geq c/a(\gamma)$."*

Con el cuantificador $\exists a$ corriendo sobre TODOS los calendarios (funciones no decrecientes
$[2,\infty)\to[1,\infty)$, Def. 3.6 del D134), esto es trivialmente verdadero:

**Teorema 141.A [TEOREMA] (trivialización del calendario libre).** Sea $Z=\{(\delta_j,\gamma_j)\}_{j\in J}$
cualquier configuración admisible (Def. 4.1 del D134: $\delta_j\in(0,\tfrac12)$, finitos $j$ por ventana,
$\gamma_j\to\infty$ si $|J|=\infty$) — en particular, el conjunto de ceros off de cualquier función con
finitos ceros por altura acotada. Entonces existe un calendario $a_Z$ (no decreciente) con
$\delta_j\,a_Z(\gamma_j)\geq1$ para todo $j$. En consecuencia, el enunciado de §7.2 del D134, leído con
$\exists a$ libre, vale para TODA configuración — incluidas todas las que violan el propósito del lema — y
no tiene contenido.

*Demostración.* Para $n\geq2$ sea $\varepsilon_n:=\min\{\delta_j:\ \gamma_j\leq n\}$ (mínimo sobre un
conjunto finito; $:=1$ si es vacío). La sucesión $(\varepsilon_n)$ es no creciente y estrictamente positiva.
Defino $a_Z(\gamma):=1/\varepsilon_{\lceil\gamma\rceil}$: no decreciente. Para cada $j$, con
$n:=\lceil\gamma_j\rceil\geq\gamma_j$: $\delta_j\geq\varepsilon_n$ (pues $\gamma_j\leq n$), luego
$\delta_j\,a_Z(\gamma_j)=\delta_j/\varepsilon_n\geq1$. $\square$

**Observación 1.1 (por qué la trivialidad es fatal para el uso).** El teorema condicional del D134 §7.2
("bajo LP-134, positividad estricta del símbolo a UN calendario ⟺ $m<\infty$") necesita que el calendario
del símbolo y el de LP-134 sean EL MISMO, y que el certificado de positividad sea producible sin conocer los
ceros. El calendario $a_Z$ de 141.A depende de $Z$ — es la "constante interna al mundo" de P43/D112 §2.6,
reapareciendo en el cuantificador del calendario, exactamente como la Prop. 5.5bis(ii) del D134 anticipaba
("la sucesión depende de $Z$"). Lo que la Prop. 5.5bis no registró es que esto hace al enunciado literal de
§7.2 **verdadero y vacío a la vez**. La formalización correcta DEBE fijar el calendario en una clase
definible por adelantado.

### 1.2. La forma canónica

**Definición 141.1 [DEFINICIÓN-NUEVA] (LP-134, forma canónica; y la escala generalizada).** Para una función
$F$ con ceros $\{\rho=\beta+i\gamma\}$ en la banda crítica (finitos por altura acotada), y para una **escala
de resolución** fija $\psi:[2,\infty)\to[1,\infty)$ no decreciente:
$$\mathbf{LP\text{-}134}^{(\psi)}(F):\qquad
\liminf_{\substack{\rho\ \text{cero de }F\\ \beta\neq1/2,\ \gamma\to\infty}}\ \bigl|\beta-\tfrac12\bigr|\cdot\psi(\gamma)\;>\;0,$$
con la convención $\liminf:=+\infty$ sobre conjuntos finitos o vacíos. **LP-134 a secas** es
$\mathrm{LP\text{-}134}^{(\log)}$: $\psi(\gamma)=\log(\gamma+3)$, la resolución natural (espaciamiento medio
de ceros $\asymp2\pi/\log\gamma$; presupuesto de soporte de la tecnología de promedios, §2).

Tres observaciones de rutina que fijan la flexibilidad del enunciado:

(i) **Invariancia por constantes:** $\mathrm{LP\text{-}134}^{(C\log)}=\mathrm{LP\text{-}134}^{(\log)}$ para
todo $C>0$ (el $\liminf$ absorbe $C$ en $c$). La clase $\{C\log\gamma\}$ es UN enunciado.

(ii) **Cofinitud gratis:** exceptuar finitos ceros no cambia nada: cada cero off tiene $\delta>0$, así que
un $\liminf>0$ sobre una cola se extiende a todo el conjunto bajando $c$ (esto usa solo finitud por altura).

(iii) **Monotonía en la escala:** $\psi_1\leq\psi_2$ (eventualmente) $\Rightarrow$
$\mathrm{LP\text{-}134}^{(\psi_1)}\Rightarrow\mathrm{LP\text{-}134}^{(\psi_2)}$. En particular, la versión a
escala acotada ($\psi\asymp1$) es la **separación uniforme** ("existe una banda
$0<|\beta-\tfrac12|<c$ libre de ceros" — quasi-RH de banda), la más fuerte de la familia; la versión
$\psi=\log$ es la relevante para la sinergia; versiones $\psi\gg\log$ son más débiles y alimentan símbolos a
calendarios donde nada es computable (§2 del mapa).

### 1.3. Posición exacta en la jerarquía del programa

**Proposición 141.P1 [PROPOSICIÓN] (jerarquía).** Como enunciados sobre una configuración/función fija:
$$\mathrm{RH}\ (m=0)\;\Longrightarrow\;m<\infty\;\Longrightarrow\;\mathrm{LP\text{-}134}^{(\psi)}\ \text{para
toda escala no decreciente }\psi\geq1,$$
y ninguna flecha se invierte en la clase de configuraciones admisibles.

*Demostración.* La primera flecha es la definición de $m$ (número de ceros off). La segunda: si
$m<\infty$, el conjunto de ceros off es finito y cada $\delta_j>0$, luego
$\liminf=+\infty$ por la convención (o, con la forma $\exists c$: tómese
$c:=\min_j\delta_j\psi(\gamma_j)>0$). No-inversión: (a) una configuración con un solo cuádruplo en
$\delta=\tfrac14$ tiene $m=4\neq0$: viola RH, cumple $m<\infty$; (b) la configuración
$\{(\tfrac14,\,2^j)\}_{j\geq1}$ tiene $m=\infty$ y
$\delta_j\psi(\gamma_j)=\tfrac14\psi(2^j)\geq\tfrac14$: cumple $\mathrm{LP\text{-}134}^{(\psi)}$, viola
$m<\infty$. $\square$

**Observación 1.2 (la lectura que orienta el ataque).** LP-134 es el enunciado **más débil de toda la
jerarquía individual del programa**: más débil que RH, más débil que $m<\infty$ (¡el objetivo Fredholm
mismo!), más débil que la separación uniforme. Si NI SIQUIERA este enunciado es accesible a las herramientas
de promedio (§3 probará que no lo es, relativamente a una clase de datos precisa), la medición del muro es la
más afilada disponible: el muro no empieza en $m=0$, ni en $m<\infty$; empieza en el primer enunciado
INDIVIDUAL sobre ceros, por débil que sea su conclusión. Y nótese la forma lógica: LP-134 es
$\forall\rho\,(\beta=\tfrac12\ \vee\ |\beta-\tfrac12|\geq c/\log\gamma)$ — un $\forall$-individual con
disyunción, la MISMA forma lógica de RH con conclusión relajada. La premisa del encargo ("LP-134 es un
enunciado de PROMEDIO LOCAL") es incorrecta tal cual: no hay promedio en el cuantificador. Lo que es de
promedio local es la *evidencia* que uno querría usar; el enunciado es individual. §3 hace de esta
observación un no-go relativo.

---

## 2. Mapa exacto contra lo conocido incondicionalmente

### 2.1. Densidad de ceros: muere exactamente en la escala de resolución

El teorema de densidad relevante cerca de la línea es el de Selberg [S46]:
$N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$ uniformemente en $\tfrac12\leq\sigma\leq1$, donde
$N(\sigma,T):=\#\{\rho:\beta\geq\sigma,\ 0<\gamma\leq T\}$. (Jutila [J77] y la escuela de densidad mejoran
los exponentes cerca de $\sigma=1$ — irrelevante acá: LP-134 vive pegado a $\sigma=\tfrac12$.)

**Lema 141.M1 [LEMA] (umbral exacto de no-trivialidad).** Sea $\delta(T)=\psi(T)/\log T$ con $\psi\geq0$.
El teorema de Selberg da $N(\tfrac12+\delta(T),T)=o(N(T))$ **si y solo si** $\psi(T)\to\infty$; para
$\psi$ acotada la cota es $\gg T\log T\asymp N(T)$: trivial.

*Demostración.* $T^{-\frac14\delta(T)}=e^{-\frac14\delta(T)\log T}=e^{-\psi(T)/4}$. Entonces
$N(\tfrac12+\delta(T),T)\ll e^{-\psi(T)/4}\,T\log T$ y $N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi}$
(Riemann–von Mangoldt, [T86, Thm. 9.4]): el cociente es $\ll e^{-\psi(T)/4}$, que tiende a $0$ exactamente
cuando $\psi\to\infty$. Si $\psi\leq C$: la cota es $\geq e^{-C/4}T\log T$, comparable al total. $\square$

Es decir: **la tecnología de densidad se vuelve trivial exactamente en la escala $1/\log T$ donde LP-134
enuncia su repulsión.** No es que las cotas sean débiles ahí: es que no dicen nada en absoluto. LP-134 vive
en el punto exacto donde toda la escuela de densidad (Selberg, Ingham, Jutila, Huxley) apaga la luz.

### 2.2. Peor que silencio: lo incondicional prueba el AMONTONAMIENTO en el tubo

**Proposición 141.M2 [PROPOSICIÓN] (clásica: el 100% de los ceros vive en el tubo de resolución).** Para
toda $\psi(T)\to\infty$, la proporción de ceros con $0<\gamma\leq T$ y
$|\beta-\tfrac12|>\psi(T)/\log T$ tiende a $0$. Incondicionalmente, casi todo cero (en densidad) satisface
$|\beta-\tfrac12|\leq\psi(\gamma)/\log\gamma$.

*Demostración.* Lema 141.M1 más simetría $\beta\leftrightarrow1-\beta$ de los ceros (ecuación funcional).
Es el refinamiento por Selberg del teorema de Bohr–Landau [BL14] (casi todos los ceros en
$|\beta-\tfrac12|<\epsilon$ fijo) a la escala $1/\log T$; véase [T86, §9.15 y notas]. $\square$

La situación es entonces la peor posible para una repulsión: el tubo
$\{|\beta-\tfrac12|<\psi/\log\gamma\}$ — la región que LP-134 declara libre de ceros off — es donde se
amontona el 100% de los ceros. LP-134 afirma que, dentro del tubo donde vive todo, la parte real es
EXACTAMENTE $\tfrac12$. Lo incondicional prueba el amontonamiento hacia el tubo y es estructuralmente mudo
sobre su interior. LP-134 no está "entre dos resultados conocidos": está estrictamente más allá del borde
donde todos los resultados conocidos de tipo σ se vuelven triviales, y del lado opuesto al único fenómeno
probado (amontonamiento, no repulsión).

### 2.3. Las estadísticas verticales son IDÉNTICAMENTE ciegas

**Lema 141.B0 [LEMA] (ceguera exacta de las estadísticas de ordenadas).** Sea $Z$ una configuración de ceros
y $Z^\flat$ su **proyección a la línea** (cada cero $\beta+i\gamma$ reemplazado por $\tfrac12+i\gamma$, con
multiplicidad). Entonces $N(t)$ es idéntica para $Z$ y $Z^\flat$ en todo $t$ que no sea ordenada de cero, y
por la fórmula de Riemann–von Mangoldt ($N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi}-\frac{t}{2\pi}+\frac78+S(t)+O(1/t)$,
[T86, Thm. 9.4], válida con $S$ definida por variación del argumento y la misma forma en ambos mundos) la
función $S(t)$ difiere entre los dos mundos en $O(1/t)$ fuera de las ordenadas. En consecuencia: **todos los
momentos de $S(t)$ (Selberg [S46]: $\int_0^T S^{2k}\sim c_k T(\log\log T)^k$), todas las varianzas de
$N(t+h)-N(t)$, y todos los teoremas de gaps de ordenadas (Littlewood [L24]:
$\gamma_{n+1}-\gamma_n\ll1/\log\log\log\gamma_n$) toman exactamente los mismos valores asintóticos en $Z$ y
en $Z^\flat$** — son funcionales de las ordenadas, ciegos a la coordenada $\beta$ por construcción.

*Demostración.* $N(t)$ cuenta ceros en el rectángulo $0<\Im s<t$, $0<\Re s<1$, sin referencia a $\beta$
dentro de la banda: las ordenadas de $Z$ y $Z^\flat$ coinciden como multiconjuntos por definición de la
proyección, luego $N$ coincide salvo en los saltos. La fórmula de R–vM expresa $S(t)=N(t)-(\text{término
liso universal})+O(1/t)$, con el término liso dependiendo solo del factor $\Gamma$ (idéntico). Toda
estadística construida sobre $S$ o sobre las ordenadas hereda la coincidencia. $\square$

Esto liquida de una vez la mitad de la caja de herramientas del paso 3 del encargo: **momentos de $S(t)$ y
$N(T+h)-N(T)$ no pueden probar LP-134 ni ninguna forma debilitada de él** — no por falta de precisión, sino
por ceguera estructural exacta. Las herramientas con sensibilidad en σ son solo: densidad (muerta en la
escala, §2.1), y la fórmula explícita con tests fuera de la línea (§2.4 y §3).

Sobre la correlación de pares: el teorema de Montgomery [M73] para $F(\alpha,T)$ en $|\alpha|<1$ es
**condicional a RH** (la escritura $\rho=\tfrac12+i\gamma$ es parte de la prueba); las variantes
incondicionales del método (Goldston–Montgomery [GM87] y derivadas) cargan cada cero con pesos del tipo
$x^{\beta-1/2}$, $x\leq T^{O(1)}$: para un cero con $\delta\log T\to0$ el peso es
$x^{\delta}=e^{\delta\log x}\to1$ — la misma ceguera sub-resolución de §3, en su encarnación clásica. No hay
repulsión de pares incondicional con sensibilidad en σ por debajo de $1/\log T$.

### 2.4. Por qué no hay Deuring–Heilbronn en la línea crítica: la palanca nula

La única repulsión de ceros genuinamente probada en la teoría es la de tipo Deuring–Heilbronn/Linnik: un
cero excepcional (real, cerca de $s=1$) repele a los demás. Su motor es la **palanca de positividad de
Landau**: para $\sigma>1$ (y por extensión cerca de $1$),
$-\Re\frac{\zeta'}{\zeta}(\sigma+it)=\sum_{n}\Lambda(n)n^{-\sigma}\cos(t\log n)\ \text{acotada por la fila
en }t=0$, y cada cero aporta $\Re\frac1{s-\rho}=\frac{\sigma-\beta}{|s-\rho|^2}\geq0$: términos de UN signo,
que compiten por un presupuesto positivo finito — de ahí la repulsión. ¿Se transpone a la línea?

**Cálculo 141.M4 [CÁLCULO] (la palanca de primer orden es idénticamente nula en la línea).** Sea
$\frac{\xi'}{\xi}(s)=B+\sum_\rho\bigl(\frac1{s-\rho}+\frac1\rho\bigr)$ (Hadamard). Tómese $s=\tfrac12+it$ y
un par de ceros simétrico por la ecuación funcional, $\rho=\tfrac12+\delta+i\gamma$ y
$\rho'=1-\bar\rho|_{\text{misma altura}}=\tfrac12-\delta+i\gamma$. Con $u:=t-\gamma$:
$$\Re\Bigl[\frac1{s-\rho}+\frac1{s-\rho'}\Bigr]
=\Re\Bigl[\frac1{-\delta+iu}+\frac1{\delta+iu}\Bigr]
=\frac{-\delta}{\delta^2+u^2}+\frac{\delta}{\delta^2+u^2}=0\qquad\text{para TODO }t.$$
La contribución de primer orden de cada par simétrico a $\Re\frac{\xi'}{\xi}$ sobre la línea es
exactamente cero — consistente con que $\Re\frac{\xi'}{\xi}(\tfrac12+it)\equiv0$ entre ceros (ξ real en la
línea). **No existe el análogo en $\tfrac12$ de la desigualdad de un signo de Landau en $1$: la ecuación
funcional hace de la línea un eje de simetría, y las configuraciones simétricas son equilibrios de primer
orden.** Toda detección debe ser de segundo orden en $\delta$. $\square$

**Cálculo 141.M5 [CÁLCULO] (la señal de segundo orden tiene integral total CERO).** El segundo orden es
$\partial_\sigma\Re\frac{\xi'}{\xi}(\sigma+it)\big|_{\sigma=1/2}=\Re\bigl(\tfrac{\xi'}{\xi}\bigr)'(\tfrac12+it)
=-\Re\sum_\rho\frac1{(s-\rho)^2}$. La contribución del par simétrico, con $u=t-\gamma$:
$$-\Re\Bigl[\frac1{(-\delta+iu)^2}+\frac1{(\delta+iu)^2}\Bigr]
=-\,\frac{2\delta^2-2u^2}{(u^2+\delta^2)^2}
=\frac{2(u^2-\delta^2)}{(u^2+\delta^2)^2}=:\,\Sigma_\delta(u).$$
El perfil $\Sigma_\delta$ cambia de signo exactamente en $|u|=\delta$ (ancho de la señal $=\delta$, la
distancia del cero a la línea) y
$$\int_{-\infty}^{\infty}\Sigma_\delta(u)\,du
=2\Bigl[\frac{-u}{u^2+\delta^2}\Bigr]_{-\infty}^{\infty}=0$$
(primitiva exacta: $\frac{d}{du}\frac{-u}{u^2+\delta^2}=\frac{u^2-\delta^2}{(u^2+\delta^2)^2}$). **La señal
de segundo orden de un cuádruplo off es un perfil de media exactamente nula y ancho $\delta$:** cualquier
promedio en $t$ a resolución $h\gg\delta$ no la atenúa — la CANCELA idénticamente al orden principal. Para
verla hace falta resolución $h\lesssim\delta$ en $t$, i.e. tests de soporte $e^{1/\delta}$: super-polinomial
en $\gamma$ cuando $\delta=o(1/\log\gamma)$. $\square$

Este par de cálculos es la razón estructural, en coordenadas clásicas, de por qué la repulsión-desde-$1$
existe y la repulsión-desde-$\tfrac12$ no se sabe probar: en $1$ hay palanca de primer orden con signo; en
$\tfrac12$ el primer orden es cero por simetría y el segundo orden es de media nula. Coincide exactamente
con (V1) del D134 (Cálculo 4.3) — y lo refuerza: no solo la señal es $O(\delta a)$ pequeña; su promedio
grueso es CERO.

### 2.5. Valiron–Landau: la repulsión de resolución es GRATIS en la dirección equivocada

**Lema 141.M3 [LEMA] (repulsión horizontal trivial — el contraste).** Para todo $T\geq2$ existe
$\tau\in[T,T+1]$ con $\min_\rho|\tau-\gamma_\rho|\geq c/\log T$ ($c>0$ absoluta).

*Demostración.* $N(T+1)-N(T)\leq C\log T$ ([T86, Thm. 9.2], incondicional). Los entornos de radio
$r:=1/(4C\log T)$ alrededor de las $\leq C\log T$ ordenadas en $[T,T+1]$ cubren medida $\leq\tfrac12<1$:
existe $\tau$ fuera de todos. $\square$

Éste es el mecanismo de selección de líneas horizontales de Landau/Valiron (usado en toda prueba de la
fórmula explícita; cf. [T86, §9.7]): **la repulsión a escala $1/\log T$ respecto de una línea horizontal
GENÉRICA es un pigeonhole trivial.** LP-134 pide lo mismo respecto de UNA línea vertical fija — y ahí no hay
familia de medida positiva sobre la que promediar: la línea crítica es única y máximamente no-genérica (la
Prop. 141.M2 dice que carga el 100% de los ceros). El contraste localiza el contenido de LP-134: es un
enunciado de genericidad métrica para un objeto que es el menos genérico de toda la banda.

### 2.6. Síntesis del mapa

| herramienta | sensibilidad a LP-134 | razón |
|---|---|---|
| momentos de $S(t)$, $N(T+h)-N(T)$, gaps de Littlewood | **cero exacta** | Lema 141.B0: solo ordenadas |
| densidad (Selberg/Jutila/Ingham) | trivial en la escala | Lema 141.M1: umbral $\delta\log T\to\infty$ |
| Bohr–Landau/Selberg (casi todos cerca de la línea) | sentido CONTRARIO | Prop. 141.M2: amontonamiento al tubo |
| correlación de pares | condicional a RH; incondicional ciega | pesos $x^{\beta-1/2}\to1$ sub-resolución |
| Deuring–Heilbronn / Linnik | no se transpone | Cálculo 141.M4: palanca nula por la ecuación funcional |
| Valiron–Landau (selección de líneas) | dirección equivocada | Lema 141.M3: pigeonhole solo en $t$ |
| verificación numérica (Platt–Trudgian [PT21]: RH hasta $3\cdot10^{12}$) | finita | LP-134 solo se decide en $\gamma\to\infty$ |

**Conclusión del mapa: LP-134 no se sigue de nada conocido, no está "entre" dos resultados conocidos, y la
totalidad de la tecnología incondicional o es exactamente ciega, o muere en la escala, o empuja en sentido
contrario.** Es un enunciado genuinamente nuevo — eso confirma al D134 — pero §3 muestra que su forma lógica
lo pone del lado individual del muro, contra la esperanza del encargo.

---

## 3. Intento de prueba incondicional

### 3.1. El plan y la primera baja

El plan del encargo: fórmula explícita con tests de Fejér/Selberg, momentos de $S(t)$, conteos cortos
$N(T+h)-N(T)$ — herramientas de promedio local. La primera baja es inmediata: por el Lema 141.B0, los
momentos de $S$ y los conteos cortos son idénticamente ciegos. Queda una sola familia con sensibilidad σ: la
fórmula explícita evaluada fuera de la línea, i.e. los funcionales de Weil
$$W[f]\;:=\;\sum_\rho h_f(\rho)\;=\;\widehat{f}\,\text{(lado arquimediano)}\;-\;\sum_{p,k}\frac{\log p}{p^{k/2}}\bigl(f(p^k)+f(p^{-k})\bigr),
\qquad h_f(s)=\int_{-L}^{L}f(e^u)e^{(s-\frac12)u}e^{u/2}\,du,$$
con $\mathrm{supp}\,f\subseteq[e^{-L},e^{L}]$ (escribo $F(u):=f(e^u)e^{u/2}$). El parámetro $L$ es el
presupuesto de soporte — el calendario del D134 en coordenadas clásicas.

### 3.2. La ceguera universal, con prueba

**Lema 141.B [LEMA] (ceguera sub-resolución de la fórmula explícita; versión clásica de D134 Teo. 5.4).**
Sea $F\in C_c^\infty([-L,L])$ y $h=h_F$ como arriba. Sea $Z$ una configuración que contiene el cuádruplo
$\{\tfrac12\pm\delta\pm i\gamma\}$ y $Z^\flat$ la misma configuración con ese cuádruplo proyectado (dos
ceros dobles en $\tfrac12\pm i\gamma$). Entonces, para todo $N\geq0$,
$$\Bigl|\,\sum_{\rho\in Z}h(\rho)-\sum_{\rho\in Z^\flat}h(\rho)\Bigr|
\;\leq\;2\,\delta^2\sup_{|x|\leq\delta}\bigl(|h''(\tfrac12+x+i\gamma)|+|h''(\tfrac12+x-i\gamma)|\bigr)
\;\leq\;C_N(F)\,\frac{(\delta L)^2\,e^{\delta L}}{(1+\gamma)^N}.$$

*Demostración.* La diferencia es $[g(\delta)+g(-\delta)-2g(0)]+[\tilde g(\delta)+\tilde g(-\delta)-2\tilde
g(0)]$ con $g(x):=h(\tfrac12+x+i\gamma)$, $\tilde g(x):=h(\tfrac12+x-i\gamma)$, holomorfas. Por Taylor con
resto integral, $|g(\delta)+g(-\delta)-2g(0)|=\bigl|\int_0^\delta(\delta-x)[g''(x)+g''(-x)]dx\bigr|\leq
\delta^2\sup_{|x|\leq\delta}|g''|$. Para la segunda cota: $h''(s)=\int_{-L}^{L}u^2F(u)e^{(s-\frac12)u}du$;
integrando por partes $N$ veces en $u$ (bordes nulos por soporte compacto y suavidad),
$(s-\tfrac12)^Nh''(s)=(-1)^N\int(\partial_u)^N[u^2F(u)]\,e^{(s-\frac12)u}du$, luego
$|h''(\tfrac12+x+i\gamma)|\leq e^{|x|L}\,\|(u^2F)^{(N)}\|_{L^1}\,(x^2+\gamma^2)^{-N/2}$. Con $|x|\leq\delta$
y $\sup u^2\leq L^2$ absorbido en $C_N(F)$ (nótese que $\|(u^2F)^{(N)}\|_1\leq C\,L^2$ módulo normalización
de $F$): se obtiene la cota enunciada. $\square$

**Corolario 141.B2 [TEOREMA] (no-go relativo: LP-134 no es separable por datos de resolución polinomial).**
Sea $\mathcal F=\{F_i\}_{i\in\mathbb N}$ cualquier familia numerable de tests suaves, $F_i$ de soporte
$[-L_i,L_i]$, y sea $\mathcal D(Z):=\bigl(\sum_{\rho\in Z}h_{F_i}(\rho)\bigr)_{i\in\mathbb N}$ el dato de
Weil de la configuración $Z$, junto con todas las estadísticas verticales (Lema 141.B0) y el símbolo
$\sigma_a(Q)$ a cualquier calendario fijo $a$ con la propiedad de que cada $F_i$ y $a$ son sub-lineales
respecto de la sucesión que se construye. Entonces para todo $\varepsilon>0$ existe una configuración
$Z_\varepsilon$ con:

(i) $Z_\varepsilon$ **viola** $\mathrm{LP\text{-}134}^{(\psi)}$ para toda escala $\psi$ de crecimiento a lo
sumo exponencial fijado de antemano, con $m=\infty$;
(ii) $|\mathcal D(Z_\varepsilon)_i-\mathcal D(\emptyset)_i|\leq\varepsilon\,2^{-i}$ para todo $i$ (dato de
Weil $\varepsilon$-indistinguible del mundo RH), las estadísticas verticales idénticas a las de un mundo con
los mismos $\gamma$ en la línea, y $\sigma_a(Q^{Z_\varepsilon})=\sigma_a(Q^{\mathrm{aut}})$ en la corona
(D134, Teo. 5.4).

En consecuencia, **ningún argumento cuya entrada sean (a) valores de funcionales de Weil de una familia
numerable de soportes fijados de antemano, (b) estadísticas de ordenadas, (c) el símbolo a calendario fijo —
es decir, la totalidad de las "herramientas promedio" del paso 3 del encargo — puede probar LP-134 ni
ninguna debilitación suya que excluya a $Z_\varepsilon$:** todo tal argumento, siendo válido sobre la clase
de configuraciones con esos datos, sería válido en $Z_\varepsilon$, donde la conclusión es falsa.

*Demostración.* Construcción por diagonalización. Elijo $\gamma_j:=\max(2^j,\,j+\text{ordenada que evite
colisiones})$ y $\delta_j>0$ tan pequeño que: (1) $\delta_j\,\psi(\gamma_j)\leq1/j$ para la escala $\psi$
fijada (posible: $\psi(\gamma_j)$ es un número, $\delta_j$ libre); (2) por el Lema 141.B, la contribución
del cuádruplo $j$ al funcional $i$-ésimo es $\leq\varepsilon 2^{-i-j-1}$ para todo $i\leq j$ (finitas
condiciones, cada una satisfecha por $\delta_j$ pequeño pues la cota de 141.B es $O(\delta_j^2)$ con
constantes que dependen solo de $F_i,\gamma_j$); para $i>j$ uso la cota con decaimiento
$(1+\gamma_j)^{-N}$ sumable. Sumando sobre $j$: la discrepancia total del dato $i$ es
$\leq\varepsilon2^{-i}$. (3) $\delta_j\,a(\gamma_j)\to0$, de modo que D134 Teo. 5.4 aplica y el símbolo
coincide con el autónomo. La violación de LP-134$^{(\psi)}$: $\liminf\delta_j\psi(\gamma_j)=0$ por (1), con
$m=\infty$. Las estadísticas verticales: Lema 141.B0. $\square$

**Observación 3.1 (qué dice y qué no dice el no-go — honestidad sobre su alcance).** El Corolario 141.B2 es
un no-go **relativo a una clase de datos**, no un teorema de indemostrabilidad absoluta. No excluye: (a)
argumentos que usen la aritmética REAL de ζ a todos los soportes simultáneamente (la identidad de la fórmula
explícita es válida para todo $L$; lo que no existe es su *evaluación* incondicional con error que supere a
la señal $(\delta L)^2$ — ese es exactamente [GAP-141.G1]); (b) argumentos de rigidez global (Hamburger-tipo,
§4.3) que usen que los ceros son los de UNA función con producto de Euler, no una configuración abstracta.
Lo que sí establece: **LP-134 no es un enunciado de promedio local.** La premisa del encargo — "el punto
entero de LP-134 es que es un enunciado de PROMEDIO LOCAL, del lado bueno del cuantificador maestro" — queda
refutada: LP-134 cuantifica individualmente sobre ceros, su señal por cero es de tamaño $O((\delta L)^2)$ y
de media nula (Cálculo 141.M5), y los promedios la cancelan en vez de acumularla. El muro que D134 partió en
dos no dejó a LP-134 del lado bueno: lo dejó como la MITAD GEOMÉTRICA del mismo muro — más débil que
$m<\infty$ (Prop. 141.P1), no equivalente a RH (correcto en D134), pero del mismo lado del cuantificador.

### 3.3. [GAP] El residuo exacto

**[GAP-141.G1 — la estimación que falta, nombrada con precisión].** Para probar LP-134 por la vía analítica
haría falta: *una evaluación de la fórmula explícita en UNA ventana individual a altura $\gamma$, con tests
de soporte $L=L(\gamma)$, cuyo término de error (arquimediano + primos + mar on-line) sea
$o\bigl((\delta L)^2\bigr)$ uniformemente para el $\delta$ que se quiere excluir* — i.e., control individual
(no en media) del déficit casi-primo por ventana. Con $L\asymp\log\gamma$ y $\delta\asymp c/\log\gamma$ la
señal es $\asymp c^2$: HARÍA FALTA el déficit por ventana individual con error $o(1)$ — exactamente la
Conjetura 108-N / la uniformidad de ventanas, el muro viejo (D134 Teo. 6.1, Cor. 6.2). El círculo se cierra:
**la mitad nueva del muro, atacada con análisis, reconduce a la mitad vieja.** No hay puerta lateral
analítica.

### 3.4. Lo que sí se prueba: la forma mínima LP-141 y la reorganización de la sinergia

El intento de prueba deja un dividendo estructural: la sinergia del D134 no necesita LP-134 entero.

**Definición 141.2 [DEFINICIÓN-NUEVA] (LP-141, la forma mínima).** A calendario fijo $a$ no acotado:
$$\mathbf{LP\text{-}141}(a):\qquad m=\infty\ \Longrightarrow\ \#\{j:\ \delta_j\,a(\gamma_j)\geq1\}=\infty$$
("si hay infinitos ceros off, no pueden ser todos salvo finitos sub-resolución: infinitos son gordos").

**Proposición 141.P3 [PROPOSICIÓN] (LP-141 basta para la mitad Fredholm; en el modelo $\mathfrak W$ del
D134 con (S1)–(S3) y (V2)).** Si vale LP-141$(a)$ y el símbolo $\sigma_a(Q)$ es **débilmente** positivo
($\mathrm{spec}\subseteq[0,\infty)$), entonces $m<\infty$.

*Demostración.* Si $m=\infty$, LP-141 da infinitos gordos; por (V2) tienen visibilidad $\theta_j\geq c_0$;
por D134 Teorema 5.1, $\mathrm{spec}(\sigma_a(Q))\cap(-\infty,-c_0/2]\neq\emptyset$ — contradice la
positividad débil. $\square$

**Proposición 141.P4 [PROPOSICIÓN] (posición de LP-141).**
(i) $\mathrm{LP\text{-}134}^{(\psi)}\Rightarrow\mathrm{LP\text{-}141}(a)$ para todo calendario $a\succeq\psi$
(si todo cero off cumple $\delta_j\psi(\gamma_j)\geq c$, los infinitos ceros off de un mundo $m=\infty$
cumplen $\delta_j a(\gamma_j)\geq c$ eventualmente, y re-escalando $a$ son gordos).
(ii) El Axioma R cuantitativo (D134 Teo. 7.2 = LP-112 con conservación de $\delta_0/2$) implica
$\mathrm{LP\text{-}141}(a)$ para todo $a$ no acotado — de hecho implica lo más fuerte
"$m\geq1\Rightarrow$ infinitos gordos".
(iii) LP-141 no implica LP-134 (configuración: un cuádruplo gordo replicado con $\delta$ fijo MÁS una
sucesión sub-resolución — cumple LP-141, viola LP-134) ni implica el Axioma R.

*Demostración.* (i) y (iii): directas de las definiciones, con las configuraciones indicadas. (ii) es D134
Teorema 7.2, primera mitad: las réplicas tienen $\delta_k'\geq\delta_0/2$ y
$\delta_k'a(\gamma_0+\tau_k)\to\infty$. $\square$

**Observación 3.2 (la reorganización).** El pivote real de la sinergia es LP-141, estrictamente más débil
que SUS DOS padres: la repulsión (LP-134) y la replicación (LP-112/Axioma R). Tiene dos fuentes
independientes posibles, y con él la ruta Fredholm queda:
$$\text{positividad DÉBIL del símbolo a un calendario no acotado}\ \wedge\ \mathrm{LP\text{-}141}\ \Longrightarrow\ m<\infty,$$
con la pieza de positividad rebajada a débil (no estricta: 5.1 viola incluso la débil) y la pieza geométrica
rebajada de LP-134 a LP-141. Es la versión mínima demostrable-condicionada de la mitad Fredholm de D-109. El
no-go 141.B2 aplica también a LP-141 (la configuración $Z_\varepsilon$ lo viola y es indistinguible), así
que LP-141 tampoco es de promedio — pero al tener dos fuentes, ataca por dos frentes: cualquier progreso en
LP-112 (frente dinámico, D112) o en repulsión de clase (frente aritmético, §4.3) lo alimenta.

---

## 4. Intento de refutación

### 4.1. Para ζ misma: refutar LP-134 es refutar RH

**Proposición 141.R1 [PROPOSICIÓN].** Toda refutación incondicional de LP-134 (para ζ) refuta RH. Toda
prueba incondicional de LP-134 está implicada por una prueba de RH (Prop. 141.P1) pero no la implica. En
particular LP-134 es **falsable solo en mundos ¬RH**: su contenido es exclusivamente una afirmación sobre el
modo de fallo de RH ("si RH falla, falla visiblemente"), vacua bajo RH.

*Demostración.* Refutar LP-134 exhibe una sucesión infinita de ceros con $\beta\neq\tfrac12$ — ceros fuera
de la línea: ¬RH. La segunda afirmación es 141.P1. $\square$

**Consistencia del mundo violador con todo lo conocido [discusión honesta].** ¿Hay configuraciones
compatibles con todo lo probado/computado que violen LP-134? Sí, y el mapa de §2 lo certifica pieza por
pieza: tómese el mundo $Z_\varepsilon$ del Corolario 141.B2 implantado por encima de la altura de
verificación numérica ($3\cdot10^{12}$, Platt–Trudgian [PT21]), con $\delta_j=1/\log^2\gamma_j$. Conteo
$N(T)$: idéntico (proyección preserva ordenadas). Densidad: los $\delta_j$ están bajo el umbral de 141.M1 —
ninguna cota de densidad lo ve. Momentos de $S$, gaps: ciegos (141.B0). Positividad de Weil verificada
históricamente: solo se ha testeado con soportes acotados — discrepancia $O((\delta_jL)^2)$ minúscula
(141.B). Correlación de pares incondicional: pesos $\to1$. **Nada de lo conocido excluye que el mundo real
sea el violador.** Y a la inversa, la heurística de borde pesa CONTRA la plausibilidad de LP-134: el teorema
de Rodgers–Tao [RT20] ($\Lambda\geq0$: la constante de De Bruijn–Newman es no negativa) dice que ζ está en
la frontera exacta del régimen "ceros apenas reales" — "RH, si es cierta, es apenas cierta". El modo de fallo
natural de RH es el modo "apenas falsa": cuádruplos con $\delta$ minúsculo — exactamente el estrato que
LP-134 prohíbe. Los pares de Lehmer (mínimos locales anómalamente pequeños de $|Z(t)|$; Csordas–Smith–Varga
[CSV94] los usaron para cotas inferiores de $\Lambda$ pre-[RT20]) son la sombra numérica real de ese
estrato: configuraciones on-line a distancia $o(1)$ de volverse cuádruplos sub-resolución. LP-134 afirma que
esa frontera, rozada infinitas veces (los Lehmer pairs ocurren), no se cruza nunca o se cruza con margen
$\geq c/\log\gamma$. No conozco ni mecanismo ni evidencia a favor, salvo la rigidez de clase de §4.3.

### 4.2. En la categoría analítica: LP-134 ES FALSO (contraejemplo con prueba)

**Proposición 141.R2 [PROPOSICIÓN] (contraejemplo de Hadamard).** Existe una función entera $F$ de orden
$1$, con $F(s)=F(1-s)$, real en la línea crítica ($F(\tfrac12+it)\in\mathbb R$ para $t\in\mathbb R$), con
todos sus ceros en la banda $|\Re s-\tfrac12|<\tfrac12$, con conteo de ceros
$N_F(T)\asymp T\log T$, y con infinitos cuádruplos off $\{\tfrac12\pm\delta_j\pm i\gamma_j\}$ donde
$$\gamma_j=2^j,\qquad \delta_j=e^{-\gamma_j}:$$
$m=\infty$ y $\delta_j\,\psi(\gamma_j)\to0$ para TODA escala $\psi(\gamma)\leq e^{\gamma/2}$ — $F$ viola
$\mathrm{LP\text{-}134}^{(\psi)}$ para toda escala sub-exponencial, en particular para toda la clase
$\{C\log\gamma\}$ y todo polinomio.

*Demostración.* Coordenada $z$: $s=\tfrac12+iz$, de modo que la ecuación funcional $s\mapsto1-s$ es
$z\mapsto-z$ y la línea crítica es $z\in\mathbb R$. Ceros prescritos en $z$: (a) pares reales $\pm t_n$ con
$t_n:=n/\log(n+2)$ ($n\geq1$), que dan conteo $\#\{t_n\leq r\}\asymp r\log r$; (b) cuádruplos
$\{\pm z_j,\pm\bar z_j\}$ con $z_j:=\gamma_j-i\delta_j$ (que corresponden a
$s=\tfrac12\pm\delta_j\pm i\gamma_j$). Defino
$$G(z):=\prod_{n\geq1}\Bigl(1-\frac{z^2}{t_n^2}\Bigr)\ \cdot\ \prod_{j\geq1}\Bigl(1-\frac{z^2}{z_j^2}\Bigr)\Bigl(1-\frac{z^2}{\bar z_j^2}\Bigr).$$
*Convergencia:* en la variable $w=z^2$ los ceros son $w_n=t_n^2$ y $w_j=z_j^2,\bar z_j^2$;
$\sum_n t_n^{-2}=\sum_n\log^2(n+2)/n^2<\infty$ y $\sum_j|z_j|^{-2}\leq\sum_j4^{-j}<\infty$: el producto de
género $0$ en $w$ converge absoluta y localmente uniformemente; $G$ es entera y par en $z$.
*Ecuación funcional:* $G(-z)=G(z)$ por paridad ⟹ $F(s):=G\bigl(\tfrac{s-1/2}{i}\bigr)$ cumple $F(1-s)=F(s)$.
*Realidad en la línea:* los factores tienen coeficientes reales en $z^2$ ($t_n^2$ real; los cuádruplos
aparecen con $z_j^2$ y $\bar z_j^2$ apareados: $(1-w/z_j^2)(1-w/\bar z_j^2)$ tiene coeficientes reales), luego
$G(\bar z)=\overline{G(z)}$ y $G|_{\mathbb R}\subseteq\mathbb R$: $F$ real en $\tfrac12+i\mathbb R$.
*Orden:* el contador de módulos de ceros en $z$ es $n_G(r)\asymp r\log r$, luego el exponente de
convergencia es $1$ y, para productos canónicos, orden $=$ exponente de convergencia $=1$ [B54, Thm. 2.6.5].
*Banda:* $|\Im z_j|=\delta_j<\tfrac12$ ✓. *Violación:* $\delta_j\psi(\gamma_j)=e^{-\gamma_j}\psi(\gamma_j)\to0$
si $\psi(\gamma)\leq e^{\gamma/2}$. $\square$

**Corolario 141.R2b [COROLARIO] (LP-134 es aritmético o no es).** LP-134 no es un teorema de la clase
analítica (entera + orden 1 + ecuación funcional + realidad en la línea + densidad de ceros de tipo ζ):
141.R2 da un miembro que lo viola maximalmente. **Toda prueba de LP-134 debe usar el lado aritmético**
(producto de Euler / coeficientes / fórmula explícita con primos), no solo la estructura de ξ como función
entera de la clase de Pólya. (Compárese: es el análogo-LP-134 de los anti-modelos cosh de D111/D112, que
realizan $m$ finito en la clase analítica; acá se realiza "$m=\infty$ sub-resolución".) $\square$

### 4.3. En la categoría de Euler: el intento de construcción FRACASA, y el fracaso señala el mecanismo

Siguiendo el Deseo 9.D2 del D134: ¿se puede construir un objeto CON producto de Euler que viole la
repulsión? El candidato obvio, con los bloques $F_{p,\alpha}$ del Doc 131 (Teo. 6.7: dato local impuro
$|\alpha_k|=p_k^{1/2+\delta_k'}$ produce divisor en $\Re s=\tfrac12+\delta_k'$):

**Cálculo 141.R3 [CÁLCULO] (la construcción ingenua no continúa).** Tómense primos $p_1<p_2<\cdots$ y datos
impuros $\delta_k'\downarrow0$, y fórmese el producto de Euler
$D(s):=\prod_k\bigl(1-\alpha_kp_k^{-s}\bigr)^{-1}\bigl(1-\bar\alpha_kp_k^{-s}\bigr)^{-1}$,
$|\alpha_k|=p_k^{1/2+\delta_k'}$. El factor $k$ tiene sus polos/ceros en la vertical
$\Re s=\tfrac12+\delta_k'$: el divisor agregado violaría LP-134 con $m=\infty$. Pero: (a) el producto
converge solo en $\Re s>\tfrac32$ (pues $|\alpha_kp_k^{-s}|=p_k^{1/2+\delta_k'-\sigma}$ y
$\sum_kp_k^{1/2-\sigma}<\infty$ exige $\sigma>\tfrac32$); (b) las verticales objetivo están en
$\Re s\approx\tfrac12$, fuera de la región de convergencia: para que el divisor EXISTA hace falta
continuación analítica hasta la banda crítica más una ecuación funcional, y nada en la construcción la
provee; (c) el recíproco $\prod_k(1-\alpha_kp_k^{-s})$ tampoco: converge en $\sigma>\tfrac32$ y no más allá
sin milagro. La obstrucción no es técnica sino estructural: **la continuación analítica acopla los datos
locales entre sí** — es una condición global sobre la familia $\{\alpha_k\}$, y los ejemplos continuables
conocidos (caracteres, formas automorfas) tienen TODOS dato puro ($|\alpha|=\sqrt p$: $\delta'=0$). $\square$

Dos rigideces conocidas delimitan el fenómeno por arriba y por abajo:

- **Hamburger [H21]:** una serie de Dirichlet con la ecuación funcional exacta de ζ (y regularidad mínima)
  ES un múltiplo de ζ. En la clase más estrecha no hay NINGÚN objeto distinto de ζ: LP-134 ahí es
  exactamente LP-134 para ζ — la falsación en la categoría estricta es tan difícil como ¬RH.
- **Davenport–Heilbronn [DH36]:** sin producto de Euler (combinación lineal de dos $L$ mod 5), la
  continuación + ecuación funcional se consiguen y los ceros off existen — infinitos, incluso con
  $\beta>1$. Los cómputos de sus ceros en la banda ([BS07]; panorama en [BG11]) muestran ceros off a
  distancias macroscópicas de la línea; **si** sus $\delta_j$ están acotados inferiormente (GAP-134.DH del
  D134, heredado acá como **[GAP-141.DH]**: dato plausible, no verificado en fuente esta sesión), DH
  satisface LP-134 con repulsión genuina — el único objeto $m=\infty$ del corpus calibraría el lado BUENO.
  Obsérvese además la deformación: DH es un punto de una familia $F_\theta=\cos\theta\,L_1+\sin\theta\,L_2$;
  en los valores de $\theta$ donde $F_\theta$ degenera a una $L$ genuina (clase de Selberg), los ceros off
  deben migrar a la línea (Hurwitz), así que $\inf_j\delta_j(\theta)\to0$ cuando $\theta\to\theta_0$ — la
  familia realiza "repulsión con constante degenerante": LP-134 miembro a miembro con $c(\theta)$ no
  uniforme. Otra vez constantes internas al mundo, ahora en una familia real.

**Conjetura 141.E [DESEO/CONJETURA — el mecanismo, nombrado].** *En la categoría D131-H⁺ (producto de Euler
con dato local hermitiano positivo + continuación + ecuación funcional; a fortiori en la clase de Selberg),
vale LP-134; el mecanismo no es positividad (la palanca es nula: Cálculo 141.M4) sino **rigidez de
continuación**: la continuación analítica de un producto de Euler fuerza pureza asintótica del dato local
(diccionario M3 del D134: pureza = sub-resolución local a todo calendario), y la impureza $\delta'$
necesaria para un cero off a distancia $\delta'$ es detectable en el dato local a soporte $\asymp1/\delta'$
(D131 Teo. 6.7: $|c_m|>2p^{m/2}$ recién en $m\gtrsim1/\delta'$) — un cero off sub-resolución global
requeriría impureza local sub-resolución sostenida, y la continuación la prohíbe.* Estatus: conjetura;
evidencia: el fracaso estructural de 141.R3 (la única vía de construcción muere exactamente en la
continuación), Hamburger, y la ausencia total de miembros de la clase de Selberg con ceros off conocidos.
Tarea concreta heredada y afinada de 9.D2: probar que en la categoría D131 la continuación + Euler implica
$\liminf\delta_j\log\gamma_j>0$, O construir el contraejemplo continuable. Es el primer enunciado del
programa donde la continuación analítica — y no la positividad — es el motor propuesto de la repulsión.

### 4.4. Veredicto del intento de refutación

LP-134 **sobrevive** la falsación: (a) para ζ es infalsable sin refutar RH (141.R1); (b) en la categoría
analítica cae (141.R2), pero eso no lo refuta para ζ — lo reclasifica como enunciado aritmético; (c) en la
categoría de Euler el intento de contraejemplo fracasa por una obstrucción estructural (141.R3) que es, en
sí misma, la mejor evidencia A FAVOR de LP-134 que produjo esta sesión. La situación de falsabilidad es
asimétrica y debe decirse con precisión: LP-134 es falsable EN LA CATEGORÍA (y la categoría analítica
efectivamente lo falsa), pero la instancia ζ solo es decidible junto con RH o por la vía de clase 141.E.

---

## 5. Veredicto y consecuencias para la sinergia del D134

### VEREDICTO: **ABIERTO-CON-MAPA** (con dos piezas PROBADAS y una premisa del encargo REFUTADA)

**No probado:** LP-134 no se probó incondicionalmente — y el Corolario 141.B2 muestra que no puede probarse
con las herramientas del paso 3 del encargo (fórmula explícita a soporte polinomial, momentos de $S$,
conteos cortos): la premisa "LP-134 es un enunciado de promedio local, del lado bueno del cuantificador
maestro" es **falsa**; LP-134 es $\forall$-individual sobre ceros, su señal por cero es $O((\delta L)^2)$ y
de media exactamente nula, y el ataque analítico reconduce a la uniformidad de ventanas (GAP-141.G1 = muro
viejo). **No refutado:** infalsable para ζ sin refutar RH; el contraejemplo existe en la categoría analítica
(141.R2, probado) pero la categoría de Euler lo resiste por rigidez de continuación (141.R3).

**Posición final en el mapa:** $\mathrm{RH}\Rightarrow m<\infty\Rightarrow\mathrm{LP\text{-}134}\Rightarrow
\mathrm{LP\text{-}141}$, todas estrictas; vacuo bajo RH; contenido = "el fallo de RH es visible"; vive
exactamente en el punto donde muere la densidad ($\delta\log T\asymp1$, Lema 141.M1), en sentido contrario
al único fenómeno probado (amontonamiento al tubo, Prop. 141.M2), sin palanca de primer orden (Cálculo
141.M4) y con señal de segundo orden de media nula (Cálculo 141.M5); falso sin aritmética (141.R2); abierto
con mecanismo candidato nombrado en la categoría de Euler (Conjetura 141.E).

**Para la sinergia del D134 (§7.3):** (1) La ruta 2 ("símbolo estricto ∧ LP-134") pierde su ventaja
esperada: LP-134 no es más barato que LP-112 en clase de cuantificador — ambos son individuales y el no-go
141.B2 los cubre por igual. (2) La ganancia real es el pivote mínimo **LP-141** (Def. 141.2): estrictamente
más débil que LP-134 Y que el Axioma R, suficiente con positividad **débil** del símbolo para $m<\infty$
(Prop. 141.P3), y alimentable desde dos frentes independientes (replicación dinámica D112 o repulsión de
clase 141.E). La arquitectura D-109 afinada queda:
$$m<\infty\ \Longleftarrow\ \bigl[\sigma_a(Q)\geq0\ \text{débil, $a$ no acotado}\bigr]\ \wedge\ \mathrm{LP\text{-}141}(a),
\qquad \mathrm{LP\text{-}141}\ \Longleftarrow\ \mathrm{LP\text{-}112}\ \ \text{ó}\ \ \mathrm{LP\text{-}134}.$$
(3) El frente nuevo que esta sesión abre no es analítico sino **algebraico-aritmético**: la Conjetura 141.E
(continuación de productos de Euler ⟹ repulsión de resolución), con la tarea 9.D2 del D134 afinada a un
mecanismo concreto y un primer test finito: decidir GAP-141.DH (¿los $\delta_j$ de Davenport–Heilbronn están
acotados inferiormente? — chequeo bibliográfico/numérico finito sobre [BS07]/[BG11]).

**Los tres resultados principales de la sesión:**
1. **[TEOREMA 141.A + Def. 141.1 + Prop. 141.P1]** — formalización: el enunciado semi-formal del D134 es
   trivialmente verdadero con calendario libre; la forma con contenido es
   $\liminf|\beta-\tfrac12|\log\gamma>0$ a escala fijada; y LP-134 es el enunciado individual más débil de
   la jerarquía: $\mathrm{RH}\Rightarrow m<\infty\Rightarrow\mathrm{LP\text{-}134}$, estrictas.
2. **[TEOREMA 141.B2 (con Lemas 141.B0/141.B y Cálculos 141.M4/M5)]** — no-go relativo: ninguna familia
   numerable de datos de resolución polinomial (fórmula explícita, estadísticas verticales, símbolo a
   calendario fijo) separa LP-134 de su negación; la señal es de media exactamente nula; LP-134 está del
   lado individual del muro — la premisa del encargo queda refutada y el residuo es GAP-141.G1 = el muro
   viejo.
3. **[PROPOSICIÓN 141.R2 + CÁLCULO 141.R3 + CONJETURA 141.E]** — refutación estratificada: LP-134 es FALSO
   en la categoría analítica (contraejemplo de Hadamard explícito, prueba completa), el contraejemplo de
   Euler fracasa exactamente en la continuación analítica, y la rigidez de continuación queda nombrada como
   el único mecanismo candidato de repulsión — el primer motor no-de-positividad propuesto en el programa.

---

## Referencias

**Internas (backward-only):** Doc 134 (§3 corona; §4 modelo $\mathfrak W$, visibilidad (V1)–(V2); Teoremas
5.1–5.5, Prop. 5.5bis, Obs. 5.5ter; §6 computabilidad; §7.2 LP-134 semi-formal; Teo. 7.2; §5.8 M2–M3;
GAP-134.DH, Deseo 9.D2); Doc 132 (Teorema D, defecto $2m$; §8.2(c)); Doc 131 (Teo. 6.7 pureza local,
barrera $|c_m|\leq2p^{m/2}$; Deseo 6.9 H⁺); Doc 112 (LP-112, mecanismo Rouché, §2.6 constantes internas);
Doc 111 (Obs. 2.4, anti-modelos cosh); Doc 108 (Teo. 3.3 ceguera; §5.2 MV74; Conjetura 108-N; Teo. 4.3);
D70 ($\Lambda$ como tiempo de anulación); P43 (cuantificador maestro).

**Literatura (publicada, verificable):**
- [BL14] H. Bohr, E. Landau, *Ein Satz über Dirichletsche Reihen mit Anwendung auf die ζ-Funktion und die
  L-Funktionen*, Rend. Circ. Mat. Palermo **37** (1914), 269–272. (Casi todos los ceros cerca de la línea.)
- [L24] J. E. Littlewood, *On the zeros of the Riemann zeta-function*, Proc. Cambridge Philos. Soc. **22**
  (1924), 295–318. (Gaps entre ordenadas.)
- [H21] H. Hamburger, *Über die Riemannsche Funktionalgleichung der ξ-Funktion*, Math. Z. **10** (1921),
  240–254. (Rigidez: la ecuación funcional de ζ caracteriza a ζ.)
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. **11**
  (1936), 181–185 y 307–312. (Ceros off sin producto de Euler.)
- [S46] A. Selberg, *Contributions to the theory of the Riemann zeta-function*, Arch. Math. Naturvid. **48**
  (1946), 89–155. (Densidad $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$; momentos de $S(t)$.)
- [M73] H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math.
  **24**, AMS (1973), 181–193. (Condicional a RH.)
- [J77] M. Jutila, *Zero-density estimates for L-functions*, Acta Arith. **32** (1977), 55–62.
- [GM87] D. A. Goldston, H. L. Montgomery, *Pair correlation of zeros and primes in short intervals*, en
  Analytic Number Theory and Diophantine Problems, Birkhäuser (1987), 183–203.
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (Thm. 9.2: $N(T+1)-N(T)=O(\log T)$; Thm. 9.4: Riemann–von Mangoldt; §9.7
  selección de líneas tipo Valiron–Landau; §9.15 densidad cerca de la línea.)
- [B54] R. P. Boas, *Entire Functions*, Academic Press, 1954. (Orden de productos canónicos, Thm. 2.6.5.)
- [CSV94] G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and
  the Riemann hypothesis*, Constr. Approx. **10** (1994), 107–129.
- [RT20] B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi **8** (2020),
  e6. (Λ ≥ 0: "RH, si es cierta, es apenas cierta".)
- [PT21] D. Platt, T. Trudgian, *The Riemann hypothesis is true up to* $3\cdot10^{12}$, Bull. London Math.
  Soc. **53** (2021), 792–797.
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  **76** (2007), 2045–2049.
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66**
  (2011), 221–270.
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004. (Cap. 5: ceros por
  ventana; contexto de densidad.)

*Fin del Doc 141.*
