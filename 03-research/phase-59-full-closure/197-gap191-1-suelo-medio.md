# Documento 197 — [GAP-191.1] a decisión: el suelo del momento molificado en θ∈[½,1], la apuesta del primer momento twisteado, y la calibración exacta de la frontera

**Programa:** Hipótesis de Riemann — Fase 59 (cierre total)
**Fecha:** 2026-06-12
**Mandato:** cerrar [GAP-191.1] (estatus del suelo $c(\theta)\ge1+\delta(\theta)$ en $\theta\in[\tfrac12,1]$) por una de tres salidas: (a) teorema de extensión, (b) barrera-teorema del método, (c) calibración-exacta contra un enunciado estándar. Apuesta central ordenada: el primer momento twisteado por primos, que (si la restricción bilineal no le aplicara) extendería el suelo a todo $\theta<1$.
**Prerrequisitos:** D191 ([LEMA 191.1], [TEOREMA 191.A], [PROP 191.D], §3.2 frontera de rango); D193 (certificación; erratas E-193.1–E-193.4 APLICADAS aquí: el enunciado de 191.A se usa en la forma del auditor D193 §7, el [COR 191.B] en su prueba reparada por persistencia-en-$s\asymp1/\log T$, y la restricción de tasa correcta es $a\lesssim2\theta$).
**Contrato:** [TEOREMA]/[PROP]/[LEMA] solo con prueba completa; [GAP]/[GAP de literatura] declarados; sin numérica; backward-only; honestidad total.

**Coordenadas (de D191, forma D193 §7).** $\varphi(s)=\sum_{n\le X}b_nn^{-s}$, $b_1=1$, $|b_n|\le d_\kappa(n)(\log T)^{A_0}$, $X=T^\theta$. $c(\theta)=\liminf_T\inf_\varphi\frac1T\int_0^T|\zeta\varphi(\tfrac12+it)|^2dt$. [TEOREMA 191.A]: $c(\theta)\ge1+\log\frac{1-\theta-\delta}\theta-\delta$ para $\theta\le\tfrac12-\delta$. (TW$_y$): dominación diagonal de $\int_0^T\zeta\varphi\,\overline D$ para tests $D$ primos de longitud $T^y$, $y>\tfrac12$. $F_0=Z\varphi$ con $Z=\sum_{m\le T}m^{-1/2-it}$ (Hardy–Littlewood, $x=T$), coeficientes $\alpha_N$, $N\le TX$, con $\alpha_p=1$ para $X<p\le T$ ([LEMA 191.1], versión truncada certificada en D193 §1.1(b)).

---

## 0. Resumen ejecutivo y veredicto

1. **La apuesta central MUERE, en un punto preciso y triangulado.** [PROP 197.1]: el "primer momento twisteado" $\int_0^T(\zeta\varphi-1)\overline{D}\,dt$ no es un funcional nuevo — ES la forma bilineal del paso (iv) de 191.A; la linealidad en $\zeta$ no compra nada porque el objeto tiene longitud $TX$, no $T$. La premisa del mandato ("$\int\zeta(\tfrac12+it)n^{-it}dt$ es computable para $n\le T$ sin restricción bilineal") es verdadera **para $\zeta$ sola** y falsa para $\zeta\varphi$: el molificador multiplica la longitud. [PROP 197.2]: tres cómputos independientes (Hilbert ponderada / cota $L^1$ de términos lejanos / momentos shifted por canal $n$ fijo con $hk\le T^{1-\varepsilon}$) reproducen los tres la MISMA ventana observable $p\in(X,\,T^{1-\eta}/X]$ — **vacía exactamente cuando $\theta\ge\tfrac12$**. La frontera no es un artefacto de Montgomery–Vaughan.
2. **Salida (a): NO.** Ninguna extensión del suelo a $\theta>\tfrac12$ se prueba aquí, ni débil. El residuo direccional (canal Gonek/parte $\chi$) se identifica y se muestra que equivale a probar (TW$_y$): no es un rodeo, es la puerta misma.
3. **Salida (b): SÍ, como teorema del pipeline, NO como teorema universal.** [TEOREMA 197.B]: dentro del pipeline $\mathcal P$ (aproximación de $\zeta$ de longitud $\le T$ + extracción diagonal por Hilbert ponderada + Cauchy–Schwarz contra cualquier polinomio test divisor-acotado), el suelo certificable para $\theta\ge\tfrac12$ es exactamente $0$: el conjunto de frecuencias rígidas observables es vacío. La afirmación más fuerte ("NINGÚN método cruza $\theta=\tfrac12$") **no es un teorema** — la cuantificación sobre "métodos" no es un objeto matemático aquí; se declara calibración y se pasa a (c). (Mismo género de honestidad que la tricotomía 190.2: no-go sobre el repertorio, no universal.)
4. **Salida (c): SÍ — calibración-sandwich con ambas implicaciones probadas.** [PROP 197.C] (=191.D, citada): (TW$_y$) $\Rightarrow$ suelo en $\theta<y$. [PROP 197.D] (nueva, dirección inversa parcial): ruptura del suelo en algún $\theta_0\in(\tfrac12,1)$ $\Rightarrow$ falla (TW$_y$) para todo $y>\theta_0$ **y** el valor conjetural de Farmer/la conjetura $\theta=\infty$ falla por un factor $\gg\log T$ en $\theta_0$ (no marginalmente). El suelo en $[\tfrac12,1]$ queda **emparedado entre dos enunciados estándar**: implicado por la extensión de rango bilineal, e implicando (su negación) la refutación catastrófica de la asintótica $1+1/\theta$. La equivalencia exacta con un enunciado único nombrado NO se prueba (y declaro por qué no puede ser la conjetura $\theta=\infty$ tal cual: esa es de optimalidad/techo, el suelo es de cota inferior/clase general). [GAP de literatura 197.L1 = 191.L2: enunciado exacto de Bettin–Gonek.]
5. **Veredicto: [GAP-191.1] CERRADO por (b)+(c) — barrera-del-pipeline + calibración-sandwich ("rango-bilineal-difícil", cota superior de dificultad: Bettin–Gonek/TW; cota inferior: refutar Farmer por factor $\log T$).** No cerrado por (a). La barrera #2 del programa queda: teorema en $\theta<\tfrac12$ (D191/D193), pipeline-sellada y doblemente calibrada en $[\tfrac12,1]$.

---

## 1. La frontera θ=½ reconstruida con exactitud

La prueba de 191.A necesita tres longitudes compatibles: $x$ (aproximación de $\zeta$; Hardy–Littlewood incondicional exige $x\ge T/2\pi$, luego $x=T$ es mínima), $X=T^\theta$ (molificador), $Y$ (test). La extracción diagonal por Hilbert ponderada (forma de D193 E-193.3: pesos $\delta_N^{-1}\asymp N$ compensados por $N^{-1/2}$) da error $(\,xX\,)^{1/2}Y^{1/2}(\log T)^B$; la señal es $T\sum_{X<p\le Y}1/p$. La condición de dominación es
$$xXY\le T^{2-2\eta}\quad\xrightarrow{x=T}\quad XY\le T^{1-2\eta'},$$
y como la rigidez vive solo en $p>X$, el test necesita $Y>X$: ambas juntas fuerzan $X^2<T$, es decir $\theta<\tfrac12$. **La ventana observable de primos rígidos es $(X,\,T^{1-\eta}/X]$, vacía para $\theta\ge\tfrac12$.** Tres agravantes que fijan que esto no es holgura técnica:

- $x$ no puede bajar de $T$ sin perder los $\alpha_p$: la aproximación simétrica ($x=y=\sqrt{t/2\pi}$) corta la diagonal $N=p$ para $p>\sqrt T\,$ — el primo rígido $p>X\ge\sqrt T$ **no aparece** en la parte directa, su huella migra íntegra a la parte $\chi$ (términos swap). Es el mismo muro del cuarto momento molificado y del $\theta<\tfrac47$ de Conrey 1989 (allí la clase restringida de coeficientes permite sumar una parte del swap; para coeficientes generales, nadie sabe).
- El error de Hilbert ponderada es de tipo correcto, no pesimista: $\sum_{N\le TX}|\alpha_N|^2\asymp TX$ salvo logs es la masa real de los coeficientes (no hay cancelación que invocar sin hipótesis: los $\alpha_N$ son arbitrarios dentro de la clase).
- El desplazamiento en $s$ no ayuda (D193 §2, reparación E-193.1): el suelo solo se observa en la ventana $s\lesssim\log\log T/\log T$, y la geometría de longitudes es la misma para todo $s\in[0,\tfrac12]$.

---

## 2. La apuesta central: el primer momento twisteado — desarrollo y muerte

### 2.1. La identidad que mata la esperanza estructural

**[PROP 197.1].** Sea $D(t)=\sum_{X<p\le Y}c_p\,p^{-1/2-it}$ (cualquier $c_p$, divisor-acotados). Entonces el "primer momento twisteado agregado con coeficientes óptimos" del mandato,
$$\mathcal T:=\frac{\big|\frac1T\int_0^T(\zeta\varphi-1)\overline D\,dt\big|^2}{\frac1T\int_0^T|D|^2dt}\;\le\;\frac1T\int_0^T|\zeta\varphi-1|^2dt,$$
es **idéntico término a término** al esquema de 191.A: el numerador es la forma bilineal del paso (iv) y la desigualdad es el Cauchy–Schwarz del paso (ii). En particular, todo lo que el primer momento twisteado puede dar ya está dado por 191.A, con la misma restricción $XY\le T^{1-\eta}$.

*Prueba.* Lectura directa: $\int(\zeta\varphi-1)\overline D=\sum_p\bar c_p\,p^{-1/2}\int(\zeta\varphi-1)p^{it}dt$ — el "twist por $p$" es la fila $p$-ésima de la forma bilineal; la agregación con $c_p$ óptimos (que es $c_p=$ señal, i.e. $c_p\propto1/\sqrt p\cdot$diagonal) ES el test $D$ de 191.A. No hay funcional nuevo. $\square$

**Dónde estaba el error de la intuición del mandato.** "$\int_0^T\zeta(\tfrac12+it)n^{-it}dt$ es computable para $n\le T$ sin restricción bilineal" — VERDADERO: $\zeta$ aproximada tiene longitud $T$ y un solo twist da error $(T\cdot1)^{1/2}\cdot$logs $\ll T^{1/2+\varepsilon}$ contra señal $T/\sqrt n\ge T^{1/2+\varepsilon'}$ para $n\le T^{1-\varepsilon}$. Pero el objeto a twistear no es $\zeta$: es $\zeta\varphi$, de longitud $TX$. La linealidad en $\zeta$ es irrelevante; lo que cuenta es la longitud del producto. El primer momento twisteado de $\zeta\varphi$ por UN solo primo $p$ tiene error $(TX)^{1/2}(\log T)^B=T^{(1+\theta)/2}(\log T)^B$ contra señal $T\cdot p^{-1/2}\cdot p^{-1/2}=T/p$… normalizado como en (ii): señal del twist individual $=T\alpha_p/p=T/p$, y agregando la ganancia de Cauchy–Schwarz se recupera exactamente $\sum_{p\in\text{ventana}}1/p$ — sobre la ventana $(X,T^{1-\eta}/X]$. Vacía para $\theta\ge\tfrac12$. **Punto de muerte exacto: el molificador multiplica la longitud de lo que se twistea; la masa rígida vive en $p>X$ y la observabilidad en $pX\le T^{1-\eta}$; para $\theta\ge\tfrac12$ no existe ningún primo que sea a la vez rígido y observable.**

### 2.2. Triangulación: tres cómputos, una sola frontera

**[PROP 197.2].** La ventana observable $p\in(X,T^{1-\eta}/X]$ del twist individual es reproducida por tres tratamientos independientes del error:

(i) **Hilbert ponderada (MV 1974, Cor. 2)** sobre $F_0\,p^{it}$: error $(\sum_{N\le TX}|\alpha_N|^2)^{1/2}=\,(TX)^{1/2}(\log T)^{B}$; señal $T/p$ tras normalizar: dominación $\iff pX\le T^{1-\eta}$ (salvo logs).

(ii) **Cota $L^1$ de términos lejanos**, sin Hilbert: $\int_0^T(N/p)^{it}dt\ll|\log(N/p)|^{-1}$; los $N$ lejanos aportan $\sum_{N\le TX}|\alpha_N|N^{-1/2}\ll(TX)^{1/2}(\log T)^{B}$ (Cauchy–Schwarz contra la longitud); los $N$ cercanos ($|N-p|\le p$) aportan $\ll p^{1/2}(\log T)^{B'}$ usando $|\log(N/p)|\gg|N-p|/p$ y $|N-p|\ge1$. El término dominante vuelve a ser $(TX)^{1/2}$: misma frontera.

(iii) **Canal $n$ fijo (momentos shifted clásicos):** $\int\zeta\varphi\,p^{it}dt=\sum_{n\le X}b_nn^{-1/2}\int\zeta(\tfrac12+it)(p/n)^{it}dt$, y el momento shifted $\int\zeta(\tfrac12+it)(h/k)^{it}dt$, $(h,k)=1$, está evaluado en la literatura de molificación (lemas de BCHB 1985 / Conrey 1989; el término principal diagonal exige $k\mid h$ — aquí $h=p$, $k=n$: solo $n=1$ aporta señal, $T/\sqrt p\cdot$, consistente con (i)) **en el rango $hk\le T^{1-\varepsilon}$**. Para los canales $n\asymp X$ la condición es $pX\le T^{1-\varepsilon}$: la misma ventana, por tercera vía. $\square$

*Comentario de honestidad sobre (iii):* cito el rango $hk\le T^{1-\varepsilon}$ de los lemas de primer momento shifted de memoria estructural (es el rango en que la parte directa domina); el enunciado fino con la parte $\chi$ evaluada puede llegar más lejos — eso es exactamente §2.3, no un descuido. [GAP de literatura 197.L2: rango exacto de los lemas de primer momento shifted en BCHB 1985.]

### 2.3. El residuo direccional: el canal Gonek ES la puerta (TW), no un rodeo

Queda una dirección genuina que el cómputo (i)–(iii) no cierra: para el **primer** momento, la parte $\chi$ de la ecuación funcional es evaluable término a término (lemas de Gonek 1984 sobre $\int_0^T\chi(1-s)m^{it}dt$: término principal de punto de silla cuando el saddle $t\approx2\pi m$ cae en $[0,T]$). Con la aproximación simétrica, la huella del primo rígido $p>X\ge\sqrt T$ vive íntegra en la parte $\chi$ (§1), en frecuencias $\ell p/n$ con saddles $\le T/2\pi$. ¿Puede esto computar $\int\zeta\varphi\,p^{it}$ para $pX>T$?

Respuesta honesta: **hacerlo equivale a probar (TW$_y$).** El cómputo requerido es la suma sobre $(\ell,n)$, $\ell\le\sqrt T$, $n\le X$, de términos de silla con coeficientes generales $b_n$ — exactamente los términos swap que D191 §3.2 identifica como "del tamaño de la diagonal y nadie sabe sumarlos para coeficientes generales". Para UN twist, Gonek da cada término; lo que no hay es control de la SUMA de errores de fase estacionaria sobre $\asymp\sqrt T\cdot X$ pares con coeficientes arbitrarios — y si se tuviera, uniformemente en $p\le T^y$, eso ES la hipótesis (TW$_y$) (formulada para $\zeta\varphi$ completo, D193 §5). No fabrico el cálculo: lo declaro como la identificación del residuo. **El canal Gonek no rodea la puerta; es la cerradura vista desde el otro lado.** Quien pruebe la sumabilidad del swap para coeficientes generales habrá probado TW y con ella el suelo (191.D) — y, por la misma tecnología, la asintótica del momento molificado largo. No hay atajo de primer orden.

**Cierre de la apuesta (a): MUERTA.** Punto exacto: ventana rígida-observable vacía para $\theta\ge\tfrac12$ (Prop 197.1+197.2); residuo direccional = (TW$_y$) sin rebaja (§2.3). Tampoco una constante pequeña $c_0>0$ se salva: el suelo certificable del pipeline es exactamente $0$ en $\theta\ge\tfrac12$ ([TEOREMA 197.B]).

---

## 3. Salida (b): el teorema del pipeline

**Definición (pipeline $\mathcal P$).** Un argumento de clase $\mathcal P$ produce una cota inferior de $\frac1T\int_0^T|\zeta\varphi-1|^2$ mediante: (1) sustitución de $\zeta$ por una aproximación de Dirichlet de longitud $x\le T$ con error de Hardy–Littlewood incondicional; (2) Cauchy–Schwarz contra un polinomio test $D$ de longitud $Y$ con coeficientes divisor-acotados; (3) evaluación del numerador por diagonal + desigualdad de Hilbert ponderada de MV (sin hipótesis sobre cancelación off-diagonal adicional). Es la clase que contiene a 191.A, 191.C, 191.D-sin-hipótesis y a las cuatro variantes de D191 §3.1.

**[TEOREMA 197.B] (suelo del pipeline en rango largo = cero).** Para todo argumento de clase $\mathcal P$ con $\theta\ge\tfrac12$, la cota inferior certificada es $\le1+o(1)$; es decir, $\mathcal P$ no produce suelo no trivial en $[\tfrac12,1]$.

*Prueba.* La señal del numerador en (3) es la diagonal $T\sum_k\bar c_k\alpha_k/k$ sobre las frecuencias compartidas $k\le\min(xX,Y)$. Descompónla en $k\le X$ y $k>X$. (I) Para $k>X$: la cota diagonal queda dominada por el error de Hilbert $(xX)^{1/2}Y^{1/2}(\log T)^B$ salvo que $XY\le xXY/T\cdot T\le$ … con $x\le T$ la dominación exige $XY\le T^{1-\eta}$ y por tanto $Y\le T^{1-\eta}/X<X$ cuando $\theta\ge\tfrac12$: no hay frecuencia compartida $k>X$ observable — la masa rígida ([LEMA 191.1]) es invisible. (II) Para $k\le X$: $\alpha_k=(1*b)(k)$ con $b$ arbitraria en su soporte; el adversario (el molificador) puede anularla: $b=\mu$ truncada a $[1,X]$ da $(1*b)(k)=\sum_{n\mid k,n\le X}\mu(n)=1_{k=1}$ para todo $k\le X$ — diagonal idénticamente nula en el rango observable salvo $k=1$, que está excluido de $D$ (o aporta el $1$ trivial). Luego para ese $\varphi$ ningún test de clase $\mathcal P$ certifica nada $>1+o(1)$, y el suelo de clase (ínfimo sobre $\varphi$) certificado por $\mathcal P$ es trivial. $\square$

**Honestidad sobre el alcance.** 197.B es un teorema sobre $\mathcal P$, no sobre "todo método": (a) la elección $x\le T$ es intrínseca a Hardy–Littlewood incondicional, pero un método que evalúe la parte $\chi$ (Conrey-$\tfrac47$ para clases restringidas, o TW) sale de $\mathcal P$ por construcción; (b) cotas inferiores por mecanismos no lineales (momentos superiores, resonancia de Soundararajan al revés) no están en $\mathcal P$ — no conozco ninguno que produzca suelos de momento cuadrático, pero su inexistencia no es teorema. La formalización "clase de complejidad bilineal $\le T^{1+\varepsilon}$" del mandato, como cuantificación sobre todos los argumentos posibles, **no es un objeto matemático del que yo sepa probar nada**: lo que es teorema es 197.B; lo demás es calibración — y por eso la salida (c) es obligatoria, no decorativa.

---

## 4. Salida (c): la calibración-sandwich

Primero, por qué la equivalencia exacta con la conjetura $\theta=\infty$ NO puede ser el cierre: la conjetura de Farmer 1993 (y su desarrollo en Bettin–Gonek, [GAP 197.L1=191.L2: enunciados exactos no verificados de memoria; no se usan]) afirma la **asintótica** $\frac1T\int|\zeta\psi_\theta|^2\to1+\tfrac1\theta$ para el molificador estándar largo — un enunciado de TECHO sobre UNA familia. El suelo es una cota INFERIOR sobre TODA la clase. Techo-de-uno y suelo-de-todos no son equivalentes sin un principio de optimalidad que es él mismo conjetural. Lo que SÍ se prueba es el sandwich:

**[PROP 197.C] (suficiencia — citada).** (TW$_y$) $\Rightarrow$ $c(\theta)\ge1+\log(y/\theta)-o(1)$ para $\theta<y$. *Prueba:* [PROP 191.D], certificada en D193 §5. $\square$

**[PROP 197.D] (necesidad parcial — nueva).** Supongamos ruptura del suelo en $\theta_0\in(\tfrac12,1)$: existe una familia $\varphi_T$ de la clase con $c(\theta_0)-1\le\epsilon_T\to0$ (la barrera #2 exige incluso $\epsilon_T\ll1/\log T$). Entonces:
1. **(TW$_y$) es falsa para todo $y>\theta_0$.** *Prueba:* contrapositivo de 197.C: (TW$_y$) daría $c(\theta_0)-1\ge\log(y/\theta_0)-o(1)>0$ constante. $\square$
2. **La asintótica conjetural $1+1/\theta$ falla en $\theta_0$ por factor $\ge(1/\theta_0)/\epsilon_T\to\infty$** (con $\epsilon_T\ll1/\log T$: por factor $\gg\log T$): el ínfimo real está un factor divergente por debajo del valor que la conjetura $\theta=\infty$ asigna como óptimo. *Prueba:* inmediata de las definiciones — la conjetura incluye que $1+1/\theta$ es el valor del molificador óptimo de su clase; $\varphi_T$ está en la clase divisor-acotada y la viola por ese factor. (Si la clase de Farmer fuera estrictamente menor que la divisor-acotada, la conclusión es que el óptimo VERDADERO sobre la clase general traiciona al conjetural por factor $\log T$ — refutación catastrófica igual, fuera de la familia.) $\square$
3. **Estructura de la ruptura:** por la prueba de 191.A leída al revés, los términos swap de $\varphi_T$ deben cancelar la masa diagonal rígida $\sum_{X<p\lesssim T}1/p\asymp\log(1/\theta_0)$ hasta $O(\epsilon_T)$ — una correlación negativa exacta parte-$\chi$/diagonal, uniforme en $T$, sin mecanismo candidato en la literatura (D191 §3.2, sin cambios).

**[CALIBRACIÓN 197.E] (el cierre tipo (c)).** El enunciado "suelo en $[\tfrac12,1]$" queda emparedado:
$$\text{(TW}_y\text{) para }y\to1^-\;\Longrightarrow\;\text{suelo en }[\tfrac12,1)\;\Longrightarrow\;\neg\text{(ruptura)}\;\Longleftarrow\;\text{asintótica }\theta=\infty\text{ con error }o(1/\log T)\text{ en su dirección de optimalidad}.$$
Es decir: probar el suelo es a lo sumo tan difícil como la extensión de rango bilineal (el insumo técnico del programa de momentos molificados largos — Bettin–Gonek), y refutarlo es al menos tan difícil como refutar catastróficamente la conjetura de Farmer. **La barrera #2 en $[\tfrac12,1]$ es, con ambas direcciones probadas: "rango-bilineal-difícil por arriba, Farmer-catastrófico-difícil por abajo."** Esto sustituye la etiqueta provisional "rango-difícil" de D191 §3.2 por una calibración de dos lados. La equivalencia exacta con UN enunciado único queda abierta y es probablemente inalcanzable por la asimetría techo/suelo declarada arriba.

---

## 5. Test anti-circularidad

| Pieza | ¿ζ-libre? | Dónde entra ζ |
|---|---|---|
| [PROP 197.1] identidad | Sí (álgebra lineal de formas bilineales) | — |
| [PROP 197.2] triangulación | No | Solo Hardy–Littlewood incondicional y lemas de momentos shifted (197.L2); sin RH, sin densidades |
| [TEOREMA 197.B] | No (vía HL) | El paso (II) usa $\mu$ truncada — combinatoria, no ceros |
| [PROP 197.D] | Condicional a la hipótesis de ruptura (que es sobre momentos, no sobre ceros) | — |

Ninguna pieza supone nada sobre la posición de los ceros; el documento construye barrera y calibración, compatible con RH y con ¬RH. Ningún enunciado de mejora de $E(T)\ll T/\log T$ se hace ni podría seguirse.

## 6. Veredicto

| Etiqueta | Enunciado | Estatus |
|---|---|---|
| [PROP 197.1] | El primer momento twisteado agregado ≡ forma bilineal de 191.A; no hay funcional nuevo | Probado |
| [PROP 197.2] | Ventana rígida-observable $(X,T^{1-\eta}/X]$ por tres vías; vacía para $\theta\ge\tfrac12$ | Probado (con 197.L2 en la vía (iii)) |
| §2.3 | Canal Gonek/parte $\chi$ ⟺ probar (TW$_y$): residuo identificado, sin rebaja | Argumentado (identificación, no teorema) |
| [TEOREMA 197.B] | Suelo del pipeline $\mathcal P$ en $\theta\ge\tfrac12$ = trivial (testigo: $b=\mu\!\upharpoonright_{[1,X]}$) | **Probado** |
| [PROP 197.C] | (TW$_y$) ⟹ suelo en $\theta<y$ | Citado (191.D/D193) |
| [PROP 197.D] | Ruptura ⟹ ¬(TW$_y$) ∧ refutación de Farmer por factor $\gg\log T$ | **Probado** |
| [CALIBRACIÓN 197.E] | Sandwich de dos lados; "rango-bilineal-difícil / Farmer-catastrófico-difícil" | Calibración (ambas flechas probadas) |

**[GAP-191.1] queda CERRADO por (b)+(c):** no existe extensión del suelo dentro del pipeline (teorema), la apuesta del primer momento twisteado muere en la ventana vacía (punto exacto documentado), y el estatus residual es una calibración de dos lados con ambas implicaciones probadas — el mejor cierre disponible sin probar (TW$_y$), que es matemática estándar abierta ajena al programa.

**GAPs numerados:**
- **[GAP-197.1]** (heredero estrecho de 191.1): probar (TW$_y$) para algún $y>\tfrac12$ — único camino restante a suelo-teorema en rango largo; género: sumar swaps con coeficientes generales (Gonek agregado). Fuera del alcance del programa; si la literatura de momentos largos lo produce, 191.D lo convierte en suelo automáticamente.
- **[GAP de literatura 197.L1]** (=191.L2): enunciados exactos de Bettin–Gonek sobre la conjetura $\theta=\infty$ — necesarios solo para afinar la pata derecha del sandwich antes de publicación externa.
- **[GAP de literatura 197.L2]**: rango exacto ($hk\le T^{1-\varepsilon}$, citado de memoria estructural) de los lemas de primer momento shifted en BCHB 1985 / Conrey 1989. Solo afecta a la vía (iii) de la triangulación; las vías (i)–(ii) son autónomas.

**Dirección sucesora.** El conducto molificador (barrera #2) está terminado como objeto del programa: teorema en $\theta<\tfrac12$, pipeline-cerrado y doblemente calibrado en $[\tfrac12,1]$. El residuo vivo del muro vuelve a ser único: [GAP-180.1] ($\mu_2=o(1)$, género 141.G1), con la tarea de literatura 188.L2 (Fujii, $\int S_1$) como previa.

---

## Referencias

- H. L. Montgomery, R. C. Vaughan, "Hilbert's inequality", *J. London Math. Soc.* (2) 8 (1974). [Forma ponderada (Cor. 2), por E-193.3.]
- R. Balasubramanian, J. B. Conrey, D. R. Heath-Brown, *J. reine angew. Math.* 357 (1985). [Momentos molificados $\theta<\tfrac12$; lemas shifted — 197.L2.]
- J. B. Conrey, *J. reine angew. Math.* 399 (1989). [$\theta<\tfrac47$, clase restringida: el swap sumado parcialmente.]
- S. M. Gonek, "Mean values of the Riemann zeta-function and its derivatives", *Invent. Math.* 75 (1984). [Lemas de primer momento con parte $\chi$; §2.3.]
- D. W. Farmer, "Long mollifiers of the Riemann zeta-function", *Bull. London Math. Soc.* 25 (1993). [Conjetura $\theta=\infty$.]
- S. Bettin, S. M. Gonek, sobre la conjetura $\theta=\infty$. [197.L1: no verificado, no usado.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Oxford 1986. [Thm 4.11.]
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS 2004. [Trasfondo.]

**Documentos internos:** D191 (191.A/C/D, frontera de rango), D193 (certificación, E-193.1–4 aplicadas), D180 (180.3), D188 (R1), D190 (precedente de no-go-sobre-repertorio).
