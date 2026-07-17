# Doc 138 — Auditoría adversarial del teorema de dos primos (Doc 135 / P48)

**Programa:** Hipótesis de Riemann — Phase 46: auditoría y ataques.
**Fecha:** junio 2026.
**Objeto auditado:** Doc 135 (`phase-45-fredholm/135-teorema-dos-primos.md`) y paper P48
(`06-papers/P48-weil-positivity-finite-primes/main.tex`).
**Protocolo:** re-derivación en forma cerrada de todas las identidades centrales, sin
numéricos; búsqueda activa de errores de signo, hipótesis implícitas, casos degenerados
y novedad falsa. Precedente que motiva la dureza: W_λ≥0 sobrevivió meses hasta el error
de signo de Doc 63 §7.1 (Phase 38).

---

## 0. Veredicto en una línea

**SOBREVIVE CON ERRATAS — las pruebas son correctas, pero el núcleo (Teoremas A/B y la
aditividad) NO ES NUEVO en sustancia: es la dirección trivial del criterio de Weil
aplicada a un divisor colocado en la línea crítica POR HIPÓTESIS, más la aditividad de
la derivada logarítmica de un producto (clásica). Lo único con sustancia potencialmente
nueva es la estructura fina (§5: umbral de núcleo, GAP-135.A), que el propio paper deja
abierta.**

Desglose: ningún error de signo encontrado; ninguna hipótesis implícita fatal; cuatro
erratas localizadas (§5 abajo); una contradicción interna de *framing* (Obs. 2.2 vs.
Obs. 3.2) que desinfla la justificación de novedad del propio documento.

---

## 1. Re-derivación de la identidad de cruzados $L(F\star G)=L(F)+L(G)$

### 1.1. La identidad, verificada desde cero

Definiciones exactas del paper (Def. 2.1 / Lemma 2.2 de P48; Doc 131 Lema 1.7,
verificado que existe tal como se cita): $\mathcal D=\{a:\mathbb Z_{\ge1}\to\mathbb C\}$
con $(a\star b)(n)=\sum_{de=n}a(d)b(e)$; $(Da)(n)=a(n)\log n$; para unidad normalizada
$F$ ($F(1)=1$), $L(F)=F^{-1}\star DF$.

**Derivación.** $D(a\star b)(n)=\log n\sum_{de=n}a(d)b(e)
=\sum_{de=n}(\log d+\log e)a(d)b(e)=(Da\star b)(n)+(a\star Db)(n)$ — solo usa
$\log(de)=\log d+\log e$. Con conmutatividad y $(F\star G)^{-1}=F^{-1}\star G^{-1}$:
$L(F\star G)=F^{-1}\star G^{-1}\star(DF\star G+F\star DG)=L(F)+L(G)$. **Correcto.**
La identidad es álgebra pura; ninguna cancelación diofántica disfrazada.

### 1.2. Los tres casos degenerados pedidos por el protocolo

- **$n=1$.** $DF(1)=F(1)\log 1=0$, luego $L(F)(1)=F^{-1}(1)\,DF(1)=0$ siempre. El dato
  discreto $a$ **no tiene masa en $n=1$**; el átomo diagonal $c_0L_p+c'_0L_q=2\log(pq)$
  vive en el slot $\omega$ (Def. 1.5 del Doc 135), que es aditivo trivialmente
  ($\omega_1+\omega_2=-2\log p-2\log q$). No hay doble conteo: en la fórmula en caja de
  Def. 1.5, el término $m=0$ del bloque $p$ aporta $2L_pf(1)$ y el $n=0$ del bloque $q$
  aporta $2L_qf(1)$; la suma ES el átomo $\omega$ contado una vez. **Consistente.**
- **Potencias $p^aq^b$ con $a$ o $b=0$.** Son potencias puras $p^a$ o $q^b$; las porta
  el $a_i$ correspondiente, sin colisión ($p^a=q^b$ con $a,b\ge1$ es imposible por
  factorización única; con $a=b=0$ es el caso $n=1$ ya tratado). **Correcto.**
- **¿Se omitió el término diagonal/arquimediano?** No se omitió: se trató (slot
  $\omega$ constante, aditivo). Pero hay que decirlo con todas las letras: **estos
  objetos no tienen factor gamma ni bloque polar** — su "término arquimediano" es una
  constante negativa que realiza el átomo diagonal y nada más. Eso es internamente
  consistente (la fórmula explícita de un polinomio de Dirichlet es Poisson puro, sin
  contorno), y el paper lo confiesa en B1/B3. No es un error; es la razón por la que el
  teorema es fácil (ver §4).

### 1.3. Soporte disjunto y dónde está realmente el contenido

Si $F$ está soportada en $p^{\mathbb N}$, la recursión triangular de $F^{-1}$ solo
involucra divisores, luego $F^{-1}$ y $DF$ y por tanto $L(F)$ viven en
$p^{\mathbb N}$. Entonces $a_1+a_2$ vive en $p^{\mathbb N_{\ge1}}\sqcup
q^{\mathbb N_{\ge1}}$, disjunto por factorización única: la masa de Weil en
$\{p^aq^b:a,b\ge1\}$ es exactamente cero. **Correcto.** Pero nótese qué se probó: que
la derivada logarítmica de un producto es la suma de las derivadas logarítmicas — i.e.
que la fórmula explícita de $E_1E_2$ es la suma de las fórmulas explícitas. Esto es el
mecanismo estándar por el cual la fórmula explícita de $\zeta=\prod_p(1-p^{-s})^{-1}$
es una suma sobre primos. **No hay milagro de cancelación: hay linealidad.** El
Doc 135 lo admite ("trivial pero estructural", Prop. 1.2) y a la vez lo vende como
"el miedo a los cruzados, disuelto" — es lo segundo lo que sobra.

**Verificaciones laterales hechas y aprobadas:** el Lema de Poisson (lem:poisson):
con $F(t)=f(e^t)e^{bt}e^{i\phi t/L_p}$, $\hat f(\rho_k)=\hat F(2\pi k/L_p)$ y Poisson
clásico da $\sum_k\hat F(2\pi k/L_p)=L_p\sum_mF(mL_p)=L_p\sum_m\beta^mf(p^m)$ ✓.
La relación espejo: $c_{-m}=\alpha^{-m}+(\bar\alpha/p)^m=\bar c_mp^{-m}$ ✓ (vale para
todo $\alpha$, sin pureza). Hermiticidad (Lema 1.6 / lem:herm): el cambio $m\mapsto-m$
y $\bar c_{-m}p^m=c_m$ cierran ✓. Bajo pureza $|\alpha|^2=p\Rightarrow
p/\bar\alpha=\alpha$, $c_m=2\alpha^m$, divisor con multiplicidad 2 sobre
$\mathrm{Re}=\tfrac12$, y cada término de $Q$ es $2|\hat F(\xi)|^2$ ✓.

---

## 2. Re-cómputo del juguete $p=2$, $q=3$, en forma cerrada

Todo re-derivado a mano desde $g=f\star\tilde f$, $g(x)=\int f(xz)\overline{f(z)}\,z\,d^*z$.

### 2.1. Los valores de $g$ (sin tomar nada del doc)

Con $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$: $\|u\|_w^2=1+O(\epsilon)$;
$\|u(\cdot/p^M)\|_w^2=p^M(1+O(\epsilon))$ (sustitución $x=p^My$). Para
$f=u-t_1u(\cdot/2^M)-t_2u(\cdot/3^N)$:
$g(1)=\|f\|_w^2=1+t_1^22^M+t_2^23^N$, $g(2^M)=-t_1$, $g(3^N)=-t_2$,
$g(2^{-M})=-t_12^M$, $g(3^{-N})=-t_23^N$ (todo $\times(1+O(\epsilon))$). ✓ Coincide.

### 2.2. El funcional y los espejos

$W_X(g)$: diagonal $2(\log2+\log3)g(1)=2\log6\,g(1)$. Términos $m=\pm M$:
$L_2[c_Mg(2^M)+c_{-M}g(2^{-M})]=L_2(-t_1)[2\cdot2^{M/2}+2\cdot2^{-M/2}\cdot2^M]
=-4\log2\cdot2^{M/2}t_1$. Igual en $q$. Luego
$$\tfrac12Q_X=\log6\,(1+2^Mt_1^2+3^Nt_2^2)-2\log2\cdot2^{M/2}t_1-2\log3\cdot3^{N/2}t_2.$$
✓ Idéntico a 6.3 del doc y §4.3(3) del paper.

### 2.3. Los mínimos

- $t_1^*=\tfrac{\log2}{\log6}2^{-M/2}$, $t_2^*=\tfrac{\log3}{\log6}3^{-N/2}$ ✓
  (independientes de $M,N$ en el valor).
- Test simple (6.1): $\log6-(\log2)^2/\log6=1.52361\ldots$ ✓ (re-computado:
  $1.791759-0.480453/1.791759$).
- Test doble (6.3): $\log6-\tfrac{(\log2)^2+(\log3)^2}{\log6}
  =\tfrac{(\log6)^2-(\log2)^2-(\log3)^2}{\log6}=\tfrac{2\log2\log3}{\log6}$, luego
  $\min Q_X=\tfrac{4\log2\log3}{\log2+\log3}=1.70005\ldots$ ✓. Dos veces la media
  armónica ✓. Identidad $(\sum L_i)^2-\sum L_i^2=2\sum_{i<j}L_iL_j$ ✓; el chequeo de
  un primo da margen $0$ = cuadrado perfecto $Q_{F_2}=2\log2(1-2^{M/2}t)^2$ ✓
  (re-derivado: $\log2[2(1+2^Mt^2)-4\cdot2^{M/2}t]$).
- Rescate de la dirección crítica (6.2): en $t=2^{-M/2}$, $Q_{F_3}=2\log3\cdot
  g(1)\cdot c_0'/2\cdot\ldots$ — limpio: $L_3c'_0g(1)=\log3\cdot2\cdot2=4\log3$ ✓.
- Adversario mixto (6.4): $2^3\cdot3^{-2}=8/9$, $\log(8/9)=-0.1178$ ✓; ningún $2^m,3^n$
  ($m,n\ne0$) cae en $\{0,\pm\log(8/9)\}+[-2\epsilon,2\epsilon]$ para
  $\epsilon<\tfrac14|\log(8/9)|$ ✓.

### 2.4. ATAQUE: ¿es ese mínimo "el mínimo" y es uniforme?

Dos observaciones que el lector apresurado puede malinterpretar, aunque el texto no
mienta:

1. **El 1.700 NO es un gap espectral.** Es el mínimo sobre la familia de Mertens de
   2 parámetros con normalización "primera protuberancia = 1" — no con
   $\|f\|_w=1$. El ínfimo de $Q_X$ sobre $\|f\|_w=1$ en ventanas largas es **cero**
   (núcleo infinito-dimensional, Teorema 5.4(b) del propio doc). En la normalización
   $\|f\|_w=1$, el valor en el óptimo es $Q/\|f\|_w^2=1.700/1.5256=1.114$, y
   tomando la familia con $M,N$ tales que la ventana exceda $\log6$ se puede bajar
   hacia $0$ con otros tests. El abstract de P48 dice "adversarial Mertens test;
   minimum $\approx1.700$" — defendible, pero la frase del Doc 135 §0 ("el margen es
   dos veces la media armónica…, uniforme en las alturas") invita a leer un gap que no
   existe. Recomendación: una frase explícita "mínimo sobre la familia de Mertens, no
   gap en norma $\|\cdot\|_w$" junto al resultado en caja.
2. **La uniformidad en $M,N$ es real pero $\epsilon$ no es uniforme:** la separación
   $\min_{n}||n|L_3-ML_2|$ decrece polinomialmente en $M$ (Baker), luego
   $\epsilon=\epsilon(M,N)$ debe encogerse. Como $\epsilon$ se elige por test y el
   valor límite no depende de $\epsilon$, la cota es correcta como ínfimo; no hay
   error, pero la dependencia $\epsilon(M,N)$ debería declararse (en §4 del doc se
   declara; en §6 se hereda tácitamente).

**La clase de tests es la correcta** ($C_c^\infty(G)$ complejos, forma
$Q(f,f)=W(f\star\tilde f)$, hermitiana por Lema 1.6): coincide con la del criterio de
Weil estándar. Sin trampa de clase.

---

## 3. Auditoría de la aditividad (Teorema 7.1)

### 3.1. ¿Pares consecutivos o todos los pares?

No hay inducción que auditar en (a): $Q_{X_S}=\sum_iQ_{F_{p_i}}$ es **lineal $n$-aria**
(Prop. 1.2 iterada; $\star$ asociativo por construcción sobre los slots
$(a,c,\omega)$, y la aditividad de $L$ es para productos finitos arbitrarios). Los
cruzados de **cada** par son cero por el mismo argumento de soportes (los soportes
$p_i^{\mathbb N_{\ge1}}$ son disjuntos dos a dos por factorización única). No se usa
ningún orden ni ningún paso $n\to n+1$. **Correcto** — y el documento mismo lo subraya
("el paso $n\to n+1$ no usa nada de $n$"), que es la confesión clave para §4.

### 3.2. ¿Se encoge la clase de tests al añadir primos?

En (a), no: la positividad es sobre todo $C_c^\infty(G)$, para todo $n$. En (b)
(recíproca), el test depende de $n$ solo vía $\epsilon$: la separación
"$p_i^m\ne$ producto de potencias de los otros" involucra finitos candidatos y la
cota $|c_M^{(i)}|>2p_i^{M/2}(\sum_jL_{p_j})/L_{p_i}$ se supera porque la violación de
Ramanujan crece geométricamente en $M$ mientras la barrera es constante en $M$.
Re-derivado desde el caso de dos primos (re-computado en §1.3: mínimo
$(L_p+L_q)-L_p^2|c_M|^2/(4(L_p+L_q)p^M)<0\iff|c_M|>2p^{M/2}(1+L_q/L_p)$ ✓; la
generalización sustituye $L_p+L_q\rightsquigarrow\sum_jL_{p_j}$ ✓). **Correcto.**

### 3.3. (c) y (d), verificados

(c) El argumento de Jensen: tipo exponencial $\le T$ + ceros en $n$ progresiones de
densidad total $(\sum L_i)/\pi$ fuerza $\sum L_i\le2T$ — constante
$\tfrac1{2\pi}\int_0^{2\pi}|\sin\vartheta|d\vartheta=\tfrac2\pi$ ✓, conteo por
progresión $\ge rL_i/\pi-2$ ✓, solapamiento $\le$ un punto por par (Lema 1.7) — para
$n$ progresiones el solapamiento total es $O_n(1)$, absorbido en $C_0$ ✓. La
construcción del núcleo $F=D_{p_1}\cdots D_{p_n}g$: soporte
$|\mathrm{supp}\,g|+\sum L_i\le2T$ ✓, $F\ne0$ porque el trasladado extremo
$g(\cdot-\sum L_i)$ dista $\ge\min_iL_i$ > ancho de $g$ de sus vecinos ✓.
(d) es §2.3 con $n$ sumandos ✓.

**Conclusión del frente 3: la aditividad es inatacable precisamente porque no afirma
nada no lineal.** El teorema de $n$ primos es $n$ copias del teorema de un primo
(Doc 131, Teo. 6.7) pegadas con linealidad. Eso desplaza todo el peso a la pregunta de
novedad.

---

## 4. Novedad vs. literatura: el ataque que sí conecta

### 4.1. Qué es realmente el Teorema A

Despojado de la categoría $\mathcal Arith$: sea
$E_S(s)=\prod_{i}(1-\alpha_ip_i^{-s})(1-(p_i/\bar\alpha_i)p_i^{-s})$, un **polinomio de
Dirichlet** finito. Su fórmula explícita (Poisson, sin continuación analítica, sin
contorno, sin gamma) dice $\sum_{\rho:E_S(\rho)=0}\hat f(\rho)=W_{X_S}(f)$. El
Teorema A dice: si todos los ceros de $E_S$ están en $\mathrm{Re}=\tfrac12$ (que es
EXACTAMENTE la hipótesis de pureza $|\alpha_i|=\sqrt{p_i}$ — pureza no es una condición
aritmética profunda aquí: es colocar los ceros en la línea por fiat), entonces
$Q(f,f)=\sum_\rho|\hat f(\rho)|^2\ge0$.

Esto es la **dirección trivial del criterio de Weil**: "ceros en la línea $\Rightarrow$
positividad término a término" — el mecanismo está en Weil 1952 y explícito en
Bombieri 2000 (la forma $\sum_\rho m_\rho\hat f(\rho)\overline{\hat f(1-\bar\rho)}$ es
suma de módulos cuadrados cuando $\mathrm{Re}\,\rho=\tfrac12$; cf. también Doc 131,
Prop. 6.2, que es la misma observación en versión categórica y que el Teorema 3.1
**cita como su paso final**). La única otra pieza es §1: la fórmula explícita de un
producto es la suma de las fórmulas explícitas — la aditividad de
$-\tfrac{d}{ds}\log$, clásica desde Euler.

### 4.2. El caso conocido disfrazado

Un factor puro $(1-\alpha p^{-s})(1-\bar\alpha p^{-s})$ con $|\alpha|=\sqrt p$ y
$\alpha+\bar\alpha\in\mathbb Z$ es el numerador de la función zeta de una curva
elíptica sobre $\mathbb F_p$ (en general, factores de Frobenius de peso 1 donde RH
local **es** Hasse–Weil). La positividad de la fórmula explícita para funciones zeta
de cuerpos de funciones — donde RH es teorema — es exactamente el contexto del propio
artículo de Weil de 1952 (que trata el caso de cuerpos de funciones junto al de
números). El "objeto de $n$ primos" es un producto de tales factores para primos
distintos, y su positividad es la suma de las positividades locales. **Nadie publicó
"Weil positivity for finite systems of primes" como teorema porque es un corolario de
una línea de la fórmula explícita para polinomios de Dirichlet con ceros en la
línea.** La comparación honesta:

- *vs. positividad para L-funciones de grado finito con RH conocida* (cuerpos de
  funciones, Weil 1952): es ese resultado, restringido a productos de factores
  locales, re-empaquetado.
- *vs. fórmulas explícitas truncadas / Bombieri 2000*: Bombieri analiza la forma
  cuadrática de Weil de $\zeta$ (régimen destructivo, $a=\Lambda\ge0$, con polar y
  gamma); P48 vive en el régimen constructivo sin polar ni gamma — el régimen donde
  no hay nada que probar una vez los ceros están en la línea. P48 lo admite en B3.
- *vs. Bombieri–Lagarias / Li / Coffey*: no aplica directamente (criterio de Li =
  positividad de $\lambda_n$ para $\zeta$; aquí no hay $\zeta$); no hay solapamiento,
  pero tampoco rescate de novedad por ese lado.
- *vs. Fejér / positividad trigonométrica*: el test de Mertens del Teorema B es
  literalmente el mecanismo $3+4\cos\theta+\cos2\theta$ (el paper lo cita, MV 2007);
  la recíproca "impuro $\Rightarrow\neg H$" es la versión local del argumento clásico
  de que la positividad falla con ceros fuera de la línea, ya presente como
  Teorema 6.7 del Doc 131 para un primo. Lo único nuevo del Teorema B es el corrimiento
  de barrera $2p^{M/2}\to2p^{M/2}(1+L_q/L_p)$: correcto, elemental, y de interés menor.

### 4.3. La contradicción interna de framing (esto debe corregirse)

La Observación 2.2 del Doc 135 justifica la novedad así: "no es retícula… ni el
Teorema 4.4(c) ni el 6.7 deciden H. **Por eso este teorema es nuevo**." Pero la
Observación 3.2 (y el Remark 2.7 del paper) confiesa: "la inconmensurabilidad de
$\log p$ y $\log q$ **no se usa** en el Teorema 3.1 (¡vale igual para $q=p$!)". Ambas
no pueden sostener la misma tesis: si la positividad es lineal en el divisor y
término a término, el "territorio no-retícula" nunca se pisa para el signo — la
dificultad que la Obs. 2.2 invoca como fuente de novedad es exactamente la que la
prueba esquiva por linealidad. La afirmación del abstract ("the first unconditional
Weil-positivity theorem… genuinely off the lattice") hereda este problema: el teorema
no supera el régimen no-periódico; lo rodea. **La frase de prioridad debe retirarse o
degradarse a "primera formulación explícita en esta categoría".**

### 4.4. Lo que sí tiene sustancia (y queda abierto o es estándar-adyacente)

- **Teorema 5.4 (umbral de núcleo $\log(p_1\cdots p_n)$):** correcto (re-derivado).
  Pero es, en lenguaje de análisis armónico, el enunciado de
  completitud/muestreo para la unión de $n$ progresiones aritméticas en
  $L^2$ de un intervalo: densidad de Beurling > tipo $\Rightarrow$ unicidad — técnica
  estándar (Boas/Levinson; el doc cita Boas 1954 correctamente). La formulación
  aritmética ("el umbral es el logaritmo del conductor ingenuo") es elegante y
  posiblemente la observación citable del paper.
- **GAP-135.A (cota de frame inferior para
  $\{e^{i\xi t}\}_{\xi\in\Lambda_p\cup\Lambda_q}$, región intermedia):** esta es la
  única pregunta genuinamente difícil del documento, y está **declarada abierta**.
  Nota adversarial: uniones de progresiones inconmensurables y sus propiedades de
  frame/muestreo son territorio activamente estudiado (Seip; Olevskii–Ulanovskii,
  muestreo universal; Lyubarskii–Seip sobre secuencias interpolantes completas); antes
  de invertir en GAP-135.A, revisar esa literatura — es plausible que la respuesta (o
  un contraejemplo con fases genéricas) ya exista en forma de teorema de frames.
- **B1–B4:** bien enunciados y honestos; B2 (la positividad pasa al límite, la
  espectralidad no) y B3 (los factores de $\zeta$ son maximalmente impuros:
  $c_m=1+p^m$; la simetría de $\zeta$ es global) son correctos y son precisamente la
  admisión de que el teorema finito vive en el régimen donde no hay obstáculo. B1-B4
  no esconden trivialidad: **la exponen** — el problema es que el título y el abstract
  no la exponen con la misma claridad.

### 4.5. Sobre "H ⟺ pureza bilateral" (Cor. 4.2)

Correcto y verificado, pero hay que decir qué es: la pureza ES "ceros en la línea"
para estos objetos, de modo que el corolario dice "la forma de Weil del objeto es
PSD ⟺ sus ceros están en la línea" — la equivalencia de Weil para objetos donde ambas
direcciones son elementales. La dirección no trivial de la equivalencia de Weil para
$\zeta$ (positividad $\Rightarrow$ RH) requiere el contorno y la continuación; aquí la
recíproca se hace con un test de dos protuberancias porque el objeto es un polinomio.
Decidibilidad ≠ profundidad.

---

## 5. Erratas y correcciones requeridas en P48 / Doc 135

Ningún error matemático sustantivo. Erratas y correcciones de alcance, en orden de
importancia:

1. **[P48, §6 (B3) — cita fuera de alcance]** B3 afirma "each factor of $\zeta$ …
   violates $H$ (Theorem~\ref{thm:local})", con $\alpha=1$, $|\alpha|=1$. Pero
   thm:local está enunciado para $1<|\alpha|<p$; $|\alpha|=1$ está **fuera del rango**
   (igual que $|\alpha|=p$, el espejo). La prueba del test de Mertens se extiende sin
   cambios a $|c_M|=1+p^M>2p^{M/2}\cdot(\text{barrera})$, pero tal como está escrito
   la cita es inválida. Corrección mínima: extender thm:local/Teorema 4.1 a
   $1\le|\alpha|\le p$ (la prueba ya lo cubre con $\delta'=\pm\tfrac12$) o añadir una
   línea en B3. Lo mismo aplica al Doc 135 §7.2 B3 (cita Doc 131 Teo. 6.7, mismo rango).
2. **[Doc 135, Teorema 5.4(b) — condición de ancho corrupta]** "bump de ancho
   $0<\,2T-\log pq\,<\min(2T-\log pq,\,L_p)$" es incoherente (un número no es menor
   que el mínimo de sí mismo). Debe decir: ancho $w$ con $0<w<\min(2T-\log pq,\,L_p)$.
   El paper (thm:thresh(b)) ya lo tiene bien; corregir el doc.
3. **[Doc 135, §6.1 — línea garbled]** "solo da $\tfrac12Q=\log2\,(1-2^{M/2}t)^2\cdot
   \tfrac{2}{2}$ — más precisamente…": el factor $\cdot\tfrac22$ es ruido tipográfico;
   la fórmula final $Q_{F_2}=2\log2(1-2^{M/2}t)^2$ es la correcta (re-verificada).
   Borrar la primera mitad de la frase.
4. **[P48, Lemma 3.4 (lem:herm) — cadena algebraica garbled]** La línea
   "$\bar c_{-m}p^m=\overline{(\bar c_m p^{-m})}\,p^m\cdot p^{-m}\cdot p^{m}=c_m$"
   contiene factores espurios $p^{-m}\cdot p^m$. La cadena correcta:
   $c_{-m}=\bar c_mp^{-m}\Rightarrow\bar c_{-m}=c_mp^{-m}\Rightarrow\bar c_{-m}p^m=c_m$.
   El resultado es correcto; la exhibición no.
5. **[Framing, P48 abstract + Doc 135 Obs. 2.2 — reclamo de novedad]** Retirar o
   degradar "the first unconditional Weil-positivity theorem for a finite system of
   distinct primes with incommensurable periods": (i) contradice la propia
   Obs. 3.2/Remark 2.7 (la inconmensurabilidad no se usa en la positividad); (ii) el
   contenido es la dirección trivial del criterio de Weil para polinomios de Dirichlet
   con ceros en la línea + aditividad de derivadas logarítmicas, ambas clásicas
   (Weil 1952; Bombieri 2000); (iii) la versión "pureza local" de un primo ya era
   Doc 131 Teo. 6.7, y el paso a $n$ primos es lineal. Reformulación sugerida:
   "una formulación categórica explícita, con estructura fina cuantitativa
   (umbral de núcleo, gap de ventana corta) que no encontramos enunciada en la
   literatura" — defendible; "first positivity theorem" no lo es.
6. **[Doc 135 §0.6 / §6.3 — etiqueta del mínimo]** Añadir junto al resultado en caja:
   "mínimo sobre la familia de Mertens (normalización del primer bump), no gap
   espectral; el ínfimo de $Q_X$ en $\|f\|_w=1$ sobre ventanas largas es $0$
   (Teo. 5.4(b))". Evita la lectura-gap que el precedente W_λ≥0 enseña a temer.
7. **[Menor, consistencia doc/paper]** El Doc 135 prueba H₂ (Teorema 3.1, vía Doc 131
   Teo. 4.9); el paper omite H₂ por completo. Decisión legítima (autocontención), pero
   el resumen del programa no debe citar "P48 prueba H y H₂": H₂ solo está en el doc,
   condicionada a Doc 131.

**Sin hallazgos:** signos (todos re-derivados: espejos $c_{-m}=\bar c_mp^{-m}$,
barrera de Mertens, mínimos del juguete, Parseval de la periodización con su constante
$L_r$, conteo de Jensen con $\tfrac2\pi$); normalizaciones doc↔paper (idénticas:
$\hat f(\tfrac12+i\xi)=\hat F(\xi)$, $\|f\|_w^2=\|F\|_2^2$, $W$ y $c_m$ coinciden);
clase de tests (estándar, sin encogimiento); convergencias (Paley–Wiener vs densidad
lineal, correcto).

---

## 6. Conclusión

El teorema sobrevive como matemática: no encontré el error de signo que buscaba, y
busqué donde el precedente (Doc 63 §7.1) enseña a buscar — espejos, sumas de Abel
implícitas en los pesos $c_{-m}p^m$, dobles conteos del átomo diagonal. No hay tal
error: la estructura es demasiado lineal para esconder uno. Esa misma linealidad es la
sentencia sobre la novedad: **el teorema es correcto porque no afirma nada que no sea
la suma de positividades locales término a término sobre un divisor colocado en la
línea por hipótesis.** El valor real del documento está en lo que declara no saber
(GAP-135.A, GAP-135.B/Doc 136) y en la honestidad de B1–B4 — que deberían promoverse
de "sección de alcance" a tesis del paper, con el reclamo de prioridad retirado.

*Fin del Documento 138.*
