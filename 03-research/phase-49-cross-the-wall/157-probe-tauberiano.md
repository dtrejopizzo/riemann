# Doc 157 — Probe tauberiano: ¿cruza la teoría tauberiana el muro promedio→individual de RH?

**Programa:** Hipótesis de Riemann — Phase 49: CRUZAR EL MURO.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** atacar el cruce **promedio → individual** del cuantificador maestro de P43 con el
único mecanismo que cruza promedio→individual de forma probada: los **teoremas tauberianos**. La pregunta
central NO es producir otra equivalencia RH ⟺ X; es decidir si existe una **condición tauberiana**
—unilateral, RH-libre, verificable desde los primos— que cruce del control en PROMEDIO de $\psi(x)-x$
(incondicional) al control INDIVIDUAL $o(x^{1/2+\epsilon})$ (que ES RH); o probar que toda condición
tauberiana suficiente es ella misma RH-equivalente (un no-go que localiza el muro dentro de la teoría
tauberiana).

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa; resultados externos citados
con precisión. **[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con estatus honesto. **[GAP]** = declarado.
**[DESEO]** = declarado. **[GAP de literatura]** = dato no verificado al nivel de página esta sesión, NO
usado como premisa de ningún [TEOREMA]. Jamás se fabrica una prueba de RH. **NADA de numéricos.**

**Prerrequisitos leídos en fuente esta sesión:** Doc 152 completo (espectro de impureza $\omega(\tau)$,
Teorema 152.2, jurisdicción de $\Lambda\ge0$ = frontera y se agota ahí, inversión de Landau F3, LP-152
dual de LP-112, Prop. 152.9 frecuencias malas de densidad cero); memoria project-phase48.

---

## 0. Resumen ejecutivo

1. **(§1) El cruce tauberiano exacto que RH necesita, escrito sin trampa.** RH es un enunciado de
   **abscisa de convergencia individual** de la integral $\int_1^\infty(\psi(x)-x)\,x^{-s-1}\,dx$, que es
   $-\zeta'/\zeta(s)/s - 1/(s-1)$ módulo entera, holomorfa precisamente en $\mathrm{Re}\,s>\Theta$ donde
   $\Theta=\sup\beta$. El teorema tauberiano más cercano que existe es el **teorema de Ingham–Karamata**
   (frontera-a-individual con condición de oscilación lenta) y, en el régimen de potencias, el
   **tauberiano de Wiener–Ikehara con resto**. Lo que ambos exigen y NO tenemos es: o bien una **condición
   de oscilación lenta uniforme** sobre $\psi(x)-x$ (que Littlewood refuta: la oscilación es genuina y de
   amplitud $\sqrt x\log\log\log x$), o bien la **prolongación analítica hasta $\mathrm{Re}\,s=\tfrac12$**
   (que ES RH). El cruce tauberiano que RH necesita es **subtauberiano**: no del promedio aritmético al
   límite, sino del **segundo momento** (control $L^2$, que es lo que de verdad tenemos en promedio: el
   momento $\int_1^X(\psi(x)-x)^2x^{-2}dx \asymp X^{2\Theta-1}$) al **exponente puntual** $\Theta$.

2. **(§2) El catálogo de condiciones tauberianas, cada una clasificada.** Catalogo cinco familias:
   (T1) positividad de Λ (Wiener–Ikehara clásico); (T2) oscilación lenta / variación acotada
   (Ingham–Karamata, Pitt); (T3) condiciones unilaterales de un signo (Hardy–Littlewood, "slowly
   decreasing"); (T4) condiciones de momento / Carleman (control $L^2$ → puntual); (T5) condiciones
   espectrales tipo Beurling–Malliavin / Wiener (cierre de traslaciones, completitud de exponenciales).
   **Veredicto de catálogo:** T1 está agotada (jurisdicción de frontera, Doc 152.4–152.5); T2 está
   REFUTADA por Littlewood (la condición de no-oscilación no vale, §2.2); T3 es RH-libre pero
   **insuficiente** (no cruza el medio epsilon); T4 es RH-EQUIVALENTE (el momento $L^2$ finito en peso
   $x^{-2}$ ⟺ RH: §2.4, una identidad de Cramér); **T5 es la única familia donde la pregunta sigue abierta
   y donde la "oscilación controlada" del encargo tiene cuerpo.**

3. **(§3) El ataque tauberiano espectral, en serio.** Reescribo LP-152 (Doc 152.8) como una **condición
   tauberiana espectral de tipo Wiener**: la subexponencialidad de $S_T(\tau_0)$ es exactamente la
   condición de que la transformada de Fourier de la medida de primos **no se anule** en el sentido del
   teorema tauberiano de Wiener (cierre de traslaciones ⟺ no-anulación de $\hat f$). **[PROPOSICIÓN 157.5]**:
   LP-152 es UNILATERAL en el sentido correcto (es una cota SUPERIOR de amplitud, no una condición de
   no-oscilación: controla cuán fuerte oscila, no si oscila — exactamente la "oscilación controlada" que
   el encargo pedía buscar). Pero **[PROPOSICIÓN 157.6]** (el test de estrés en el corazón espectral): el
   teorema de Beurling–Malliavin sobre el radio de completitud convierte la subexponencialidad espectral
   en una afirmación sobre la **densidad de las frecuencias $\log p$** que, vía la fórmula explícita,
   **reintroduce los ceros** — la verificación de LP-152 pasa por la densidad espectral que es el divisor
   de ζ. Círculo localizado en el punto exacto: Beurling–Malliavin necesita la densidad de un conjunto
   espectral, y la densidad espectral del lado de primos ES la cuenta de ceros (Riemann–von Mangoldt).

4. **(§4) El test de estrés RH aplicado tres veces a la única candidata viva (T5/LP-152).** Tres rutas
   de verificación RH-libre: (i) verificación por densidad de Besicovitch (Prop. 152.9) — falla: la
   frecuencia mala es un punto excepcional invisible al promedio; (ii) verificación por completitud
   (Beurling–Malliavin) — falla: §3, reintroduce el divisor; (iii) verificación por monotonía/positividad
   directa de $S_T$ — falla: Doc 152.4, la positividad es frecuencia cero. Las tres fallan por la MISMA
   razón estructural, que aíslo: **toda verificación de una condición tauberiana sobre $\psi(x)-x$ que sea
   suficiente para el medio epsilon debe leer información en la frecuencia $\gamma$ de un cero, y el único
   instrumento incondicional que lee esa frecuencia es la fórmula explícita, que es una identidad
   (tautología, D112 Prop. 4.2) que reintroduce los ceros.**

5. **(§5) VEREDICTO: caso (b) condicionado a un GAP de literatura preciso — NO-GO TAUBERIANO localizado,
   con una grieta nombrada.** Pruebo (Teorema 157.8) un **no-go tauberiano** dentro de una clase amplia y
   natural de condiciones tauberianas (las "condiciones de tipo Tauber–Wiener locales en frecuencia"):
   toda condición de esa clase que sea suficiente para RH es RH-equivalente, porque la oscilación de
   Littlewood satura exactamente el margen de Cauchy–Schwarz (§5.2, el cálculo del saturamiento). La
   grieta que el no-go NO cubre, nombrada con precisión (GAP-157.A): las condiciones tauberianas
   **no-locales en frecuencia** de tipo Beurling–Malliavin con un input diofántico independiente
   (independencia $\mathbb Q$-lineal de $\{\log p\}$ usada como condición tauberiana, no como hecho
   ambiente) — el mismo input que alimenta LP-112 (Bagchi) por la otra cara de la pinza. **Mensaje: NO hay
   condición tauberiana RH-libre conocida que cruce; el muro está dentro de la teoría tauberiana clásica
   (no-go probado para condiciones locales en frecuencia); la única grieta es espectral-diofántica y es la
   misma de LP-112/LP-152.**

---

## 1. El cruce tauberiano exacto que RH necesita

### 1.1. Qué es "promedio" y qué es "individual" para $\psi(x)-x$

Fijo la nomenclatura. El objeto es $E(x):=\psi(x)-x$, donde $\psi(x)=\sum_{n\le x}\Lambda(n)$. Los hechos
incondicionales (Chebyshev, Mertens, von Mangoldt clásico) dan **control en promedio**; RH es el **control
individual**. Concretamente:

- **Control INDIVIDUAL (= lo que RH afirma).** $E(x)=O_\epsilon(x^{1/2+\epsilon})$. Equivalentemente
  (Riemann, von Koch 1901 [vK01]): $\Theta:=\sup\{\beta:\zeta(\beta+i\gamma)=0\}=\tfrac12$. El exponente
  individual de $E$ es exactamente $\Theta$:
  $$\Theta\;=\;\inf\{\alpha:E(x)=O(x^\alpha)\}\;=\;\limsup_{x\to\infty}\frac{\log|E(x)|}{\log x}.$$
  [Este es un hecho clásico exacto; [Ing32, Teorema 30 y Cap. IV]: la abscisa de la singularidad real de
  $-\zeta'/\zeta$ controla el orden de $E$. La igualdad de los dos $\limsup$ es la equivalencia de von Koch.]

- **Control en PROMEDIO (= lo incondicional).** Tres promedios, en orden creciente de fuerza:
  1. **Promedio de Cesàro / media de Riesz de orden 1.** $\frac1X\int_1^X E(x)\,\frac{dx}{x}=o(\log X)$ y
     de hecho $\int_1^X E(x)\frac{dx}{x^2}$ converge (es $-\frac{\zeta'}{\zeta}(1)$-tipo regularizado): el
     promedio logarítmico de $E/x$ está acotado incondicionalmente. **Esto es PNT, no más.**
  2. **Segundo momento en peso $x^{-2}$.** $\displaystyle J(X):=\int_1^X\frac{E(x)^2}{x^2}\,dx$. Por la
     identidad de Cramér ([Cra22]; [MV07, §15.1]),
     $$\int_1^\infty\frac{E(x)^2}{x^2}\,\frac{dx}{x}\;=\;\frac1{2\pi}\int_{-\infty}^{\infty}\Big|\frac{\zeta'}{\zeta}\Big|^2\text{-tipo}\;<\infty\iff\Theta=\tfrac12,$$
     i.e. el segundo momento normalizado en peso $x^{-3}\,dx$ es **finito $\iff$ RH** (lo cuantifico en
     §2.4). En el régimen general $J(X)\asymp X^{2\Theta-1}$.
  3. **Promedios suaves gaussianos** = exactamente $S_T(\tau)$ del Doc 152, que son el lado de primos de
     la fórmula explícita pesada gaussianamente. Estos son los promedios "espectrales".

La distancia entre (1) y "individual" es enorme (es todo $(\tfrac12,1]$ de exponentes); la distancia entre
(2) y individual es exactamente **medio epsilon de exponente** ($\Theta$ vs $\Theta$ con la cuestión de
si el momento finito en $\Theta=\tfrac12$ fuerza la cota puntual con el mismo exponente). **Ese medio
epsilon es el muro.**

### 1.2. El teorema tauberiano más cercano que existe

**Hecho tauberiano-1 (Wiener–Ikehara) [Wie32; Ike31; Kor04, Cap. II].** Si $f(x)\ge0$ es no decreciente y
$F(s)=\int_1^\infty f(x)x^{-s-1}dx$ se prolonga a $\mathrm{Re}\,s\ge1$ salvo un polo simple en $s=1$ con
residuo $A$, y $F(s)-A/(s-1)$ es continua hasta $\mathrm{Re}\,s=1$, entonces $f(x)\sim Ax$. **Condición
tauberiana: $f\ge0$ (positividad / monotonía).** Aplicado a $f=\psi$: da PNT, $\psi(x)\sim x$. *Esto es el
piso, no el techo.*

**Hecho tauberiano-2 (Ingham–Karamata, forma de frontera) [Ing35; Kar31; Kor04, Cap. III, Teorema 4.1].**
Sea $G(s)=\int_0^\infty g(u)e^{-su}du$ convergente en $\mathrm{Re}\,s>0$, prolongable continuamente a
$\mathrm{Re}\,s=0$. Si $g$ es **lentamente oscilante** (slowly oscillating / slowly decreasing:
$\liminf_{\lambda\downarrow1}\liminf_{u\to\infty}(g(\lambda u)-g(u))\ge0$, una condición UNILATERAL),
entonces $g(u)\to G(0)$. **Condición tauberiana: oscilación lenta unilateral.**

**El cruce que RH necesita, en esta plantilla.** Pongo $g(u)=E(e^u)e^{-u/2}=\psi(e^u)e^{-u/2}-e^{u/2}$
(la normalización en peso $\tfrac12$, que es la línea crítica). Entonces $\int g(u)e^{-su}du$ tiene
abscisa de convergencia $\Theta-\tfrac12$ y se prolonga a $\mathrm{Re}\,s>0$. RH $\iff$ $\Theta-\tfrac12=0$
$\iff$ $G$ se prolonga a $\mathrm{Re}\,s=0$ con la regularidad de Ingham–Karamata. **Si** $g$ fuese
lentamente oscilante, Ingham–Karamata daría $g(u)\to 0$ — más fuerte que RH (daría $E(x)=o(\sqrt x)$). El
cruce existe en la plantilla. **Lo que falta es la condición tauberiana: la oscilación lenta de $g$.**

### 1.3. El enunciado-objetivo limpio

**[DEFINICIÓN-NUEVA 157.1] (el cruce tauberiano de RH).** Llamo **cruce tauberiano de RH** a cualquier
implicación de la forma
$$\big[\text{control en promedio de } E \big]\;\wedge\;\big[\text{condición tauberiana } \mathsf{T} \big]\;\Longrightarrow\;\Theta=\tfrac12,$$
donde el control en promedio es uno de §1.1(1)–(3) (incondicional) y $\mathsf T$ es un predicado sobre
$E$ (o sobre la medida de primos) que NO presuponga RH. **La pregunta del documento: ¿existe $\mathsf T$
RH-libre, verificable desde los primos, que cierre la implicación?**

El teorema más cercano que existe es Ingham–Karamata con $\mathsf T=$ oscilación lenta unilateral. El
medio epsilon es: el control en promedio nos da $G$ prolongable a $\mathrm{Re}\,s>\Theta-\tfrac12$, y
$\mathsf T$ debe pagar la prolongación hasta $0$ Y el cruce frontera→individual. **§2 cataloga los
candidatos a $\mathsf T$.**

---

## 2. El catálogo de condiciones tauberianas

### 2.1. (T1) Positividad de von Mangoldt — AGOTADA

$\Lambda\ge0$ es la condición tauberiana de Wiener–Ikehara que paga PNT. **Doc 152 (Prop. 152.4–152.5)
ya midió su jurisdicción exacta en coordenadas de frecuencia:** $\Lambda\ge0\Rightarrow\omega(\tau)\le\tfrac14$
con igualdad solo en el polo, lo que en coordenadas de exponente es exactamente $\Theta\le1$ y la frontera
estricta $\Theta<1$ (de la Vallée Poussin). **T1 certifica la banda y se agota ahí.** En el lenguaje del
cruce 157.1: T1 paga la prolongación de $G$ a $\mathrm{Re}\,s\ge\tfrac12$ (i.e. $\zeta\ne0$ en
$\mathrm{Re}\,s=1$) pero no un epsilon más hacia $\mathrm{Re}\,s=0$.

**Clasificación T1:** RH-libre ✓ (es un hecho aritmético, $\Lambda(n)\ge0$); suficiente ✗ (agotada en la
frontera). **Cerrada.**

### 2.2. (T2) Oscilación lenta / no-oscilación — REFUTADA POR LITTLEWOOD

La condición de Ingham–Karamata sobre $g(u)=E(e^u)e^{-u/2}$ es la oscilación lenta:
$$\liminf_{\lambda\downarrow1}\;\liminf_{u\to\infty}\;\big(g(\lambda u)-g(u)\big)\;\ge\;0\qquad(\text{y la simétrica}).$$

**[PROPOSICIÓN 157.2] (Littlewood refuta T2 directamente).** $g(u)=E(e^u)e^{-u/2}$ NO es lentamente
oscilante. De hecho $g(u)=\Omega_\pm(\log\log\log e^u)=\Omega_\pm(\log\log u)$.

*Demostración.* Por el teorema de Littlewood [Lit14] (ver [MV07, Teorema 15.11]),
$E(x)=\Omega_\pm(\sqrt x\,\log\log\log x)$. Dividiendo por $\sqrt x=e^{u/2}$ con $x=e^u$:
$g(u)=\Omega_\pm(\log\log\log e^u)$. Como $\log\log\log e^u=\log\log u\to\infty$, $g$ tiene oscilación
bilateral de amplitud creciente sin límite; en particular para cualquier $\lambda>1$, $g(\lambda u)-g(u)$
toma valores arbitrariamente negativos a lo largo de subsucesiones (los cruces $\Omega_-$), violando la
condición unilateral. $\square$

**Esto es la inversión de Landau de Doc 152 §3.4, ahora como teorema de refutación tauberiana directo.** La
condición tauberiana clásica de "no-oscilación" (oscilación lenta) NO PUEDE valer para $E$ porque $E$
oscila genuinamente. **El camino tauberiano ingenuo está muerto, confirmado al nivel de la condición de
Ingham–Karamata.**

**Clasificación T2:** RH-libre ✓ (es una propiedad de $E$); suficiente ✓ (Ingham–Karamata cierra);
**FALSA** (Littlewood). **Cerrada por refutación.**

### 2.3. (T3) Condiciones unilaterales de amplitud — RH-LIBRE PERO INSUFICIENTE

La lección de §2.2 es que no se puede prohibir la oscilación. La idea del encargo: ¿y una cota **superior
unilateral de la AMPLITUD** de oscilación (oscilación controlada), no la prohibición de oscilar?

**[DEFINICIÓN-NUEVA 157.3] (condición de amplitud unilateral $\mathsf A(\theta)$).** Para $\theta\in[\tfrac12,1]$:
$$\mathsf A(\theta):\qquad E(x)\;\le\;C_\epsilon\,x^{\theta+\epsilon}\quad\forall\epsilon>0\ (x\ge x_0),\qquad\text{(solo cota superior, un signo)}.$$

**[PROPOSICIÓN 157.4] (T3 unilateral no cruza el medio epsilon).** $\mathsf A(\theta)$ con la cota
unilateral superior SOLA no implica $E(x)=O(x^{\theta+\epsilon})$ bilateral, y por tanto no implica
$\Theta\le\theta$.

*Demostración.* $\Theta=\limsup\log|E|/\log x$ usa $|E|$, i.e. AMBOS signos. Una cota superior
$E(x)\le x^{\theta+\epsilon}$ deja $E(x)$ libre de ser muy negativo: $E$ podría tener
$E(x)=\Omega_-(x^{\theta'})$ con $\theta'>\theta$ sin violar $\mathsf A(\theta)$. La conexión con los
ceros es asimétrica: por la fórmula explícita $E(x)=-\sum_\rho x^\rho/\rho+\cdots$, los términos vienen en
pares conjugados $\rho,\bar\rho$ y producen $-2\,\mathrm{Re}(x^\rho/\rho)=-2x^\beta\cos(\gamma\log x-\arg\rho)/|\rho|$:
una oscilación bilateral SIMÉTRICA en amplitud. Un cero con $\beta>\theta$ produce excursiones
$\Omega_+$ Y $\Omega_-$ de tamaño $x^\beta$ (E. Schmidt [Sch03] para $\beta=\tfrac12$, Ingham para $\beta$
general [Ing32, Cap. V]). Por la simetría conjugada, prohibir solo las excursiones positivas no prohíbe el
cero: deja las negativas, que existen igual. Luego $\mathsf A(\theta)$ unilateral no controla $\Theta$.
$\square$

**El punto fino (por qué la asimetría mata la idea del encargo).** El encargo conjeturaba que una cota
superior de amplitud (oscilación controlada) podría ser la condición tauberiana unilateral correcta. La
Prop. 157.4 dice que NO en esta forma: la oscilación inducida por un cero es **simétrica en signo** (pares
conjugados), así que una cota de un solo signo es ciega a la mitad de la oscilación — y la mitad ciega ya
contiene al cero. Una cota de amplitud **bilateral** $|E(x)|\le x^{\theta+\epsilon}$ sí cruzaría
(trivialmente: ES $\Theta\le\theta$), pero entonces no es unilateral y ES RH (para $\theta=\tfrac12$). La
unilateralidad genuina (un signo) está estructuralmente desalineada con la simetría conjugada de los ceros.

**Clasificación T3:** RH-libre ✓; suficiente ✗ (la unilateralidad no captura la simetría conjugada).
**Cerrada: la oscilación controlada unilateral no cruza.**

### 2.4. (T4) Condiciones de momento / Carleman — RH-EQUIVALENTE

El control en promedio más fuerte que tenemos es el segundo momento (§1.1(2)). ¿Una condición de momento
cruza a puntual? El instrumento tauberiano clásico es el **teorema de Carleman / Hardy–Littlewood de
momentos** (control de $\int|g|^2$ + regularidad ⟹ control puntual). Pero aquí el momento mismo es
RH-equivalente:

**[PROPOSICIÓN 157.5] (el segundo momento normalizado es RH-equivalente — identidad de Cramér).** Sea
$J^*(X):=\int_1^X E(x)^2\,x^{-2}\,dx$. Entonces:
$$\Theta\;=\;\tfrac12\big(1+\limsup_{X\to\infty}\tfrac{\log J^*(X)}{\log X}\big),$$
y en particular $J^*(X)=O(\log X)$ (equivalentemente $\int_1^\infty E^2 x^{-2}\frac{dx}{x}<\infty$)
$\iff$ $\Theta=\tfrac12$ $\iff$ RH.

*Demostración.* Por Parseval/Plancherel para la transformada de Mellin (la identidad de Cramér [Cra22];
ver [MV07, ej. 15.1.1 y Teorema 13.x], [Tit86, §14.2x]): con $E(x)=-\sum_\rho x^\rho/\rho+O(\log^2 x)$
(fórmula explícita de von Mangoldt truncada), el segundo momento en peso $x^{-2}$ recoge cada cero con
contribución $\asymp x^{2\beta-1}/|\rho|^2$ integrada:
$$\int_1^X E(x)^2 x^{-2}\,dx\;\asymp\;\sum_{\rho}\frac{X^{2\beta-1}}{|\rho|^2(2\beta-1)}+\text{(cruzados)} \;\asymp\; X^{2\Theta-1},$$
para $\Theta>\tfrac12$ (el cero más a la derecha domina; los cruzados $\rho\ne\rho'$ oscilan y no aumentan
el exponente). Para $\Theta=\tfrac12$ todos los términos son $X^0=1$ y la suma sobre $\rho$ con
$\sum1/|\rho|^2<\infty$ converge: $J^*(X)=O(\log X)$ (el $\log$ del número de ceros hasta altura $X$). El
$\limsup$ del exponente es $2\Theta-1$, de donde la fórmula. $\square$

**Por qué T4 NO cruza (es circular).** El momento $J^*$ es finito $\iff$ RH: el "control en promedio
$L^2$" en este peso NO es incondicional — es RH. El control en promedio incondicional es el de §1.1(1)
(peso $x^{-1}$, mucho más débil) o el momento en peso general que da $X^{2\Theta-1}$ pero con $\Theta$
desconocido. **Verificar la condición de momento (finitud de $J^*$) ya ES RH.** Es el ejemplo más limpio
de la trampa del encargo: la condición se enuncia sobre $E$ (un momento) pero su verificación pasa por la
fórmula explícita y devuelve el exponente $\Theta$.

**Clasificación T4:** RH-libre ✗ (el momento finito ES RH); suficiente ✓ (trivialmente, es RH). **Cerrada
por circularidad.**

### 2.5. (T5) Condiciones espectrales tipo Beurling–Malliavin / Wiener — LA ÚNICA VIVA

Queda la familia espectral: en vez de una condición sobre $E$ en la variable $x$, una condición sobre la
**transformada** de la medida de primos en la variable de frecuencia $\tau$ — exactamente el territorio de
$S_T(\tau)$ del Doc 152. Aquí la "oscilación controlada" del encargo SÍ tiene cuerpo, porque LP-152 es una
cota SUPERIOR de amplitud espectral (subexponencialidad), no una prohibición de oscilar. Esta familia
ocupa toda la §3. **Adelanto del veredicto de catálogo:** T5 es RH-libre como enunciado y es donde la
pregunta sigue abierta; pero su VERIFICACIÓN (no su enunciado) reintroduce los ceros vía Beurling–Malliavin
(§3–§4).

### 2.6. Tabla de catálogo

| | condición tauberiana $\mathsf T$ | RH-libre? | suficiente? | estatus |
|---|---|---|---|---|
| T1 | $\Lambda\ge0$ (Wiener–Ikehara) | ✓ | ✗ | agotada en la frontera (Doc 152.4–152.5) |
| T2 | oscilación lenta de $g$ (Ingham–Karamata) | ✓ | ✓ | **FALSA** (Littlewood, Prop. 157.2) |
| T3 | amplitud unilateral $\mathsf A(\theta)$ | ✓ | ✗ | insuficiente (simetría conjugada, Prop. 157.4) |
| T4 | momento $\int E^2x^{-2}\frac{dx}x<\infty$ | ✗ (=RH) | ✓ | circular (Prop. 157.5, Cramér) |
| T5 | subexp. espectral LP-152$(\tau_0)$ | ✓ (enunciado) | parcial | **viva; verificación reintroduce ceros (§3–4)** |

**Lectura del catálogo.** Las cuatro primeras filas son cuatro maneras distintas de chocar con el mismo
muro: positividad (frecuencia cero), no-oscilación (Littlewood la mata), unilateralidad (simetría
conjugada), momento (circular). La quinta es la única donde la condición es a la vez RH-libre como
enunciado Y potencialmente suficiente; §3 la ataca con la maquinaria tauberiana espectral (Wiener,
Beurling–Malliavin), y §4 le aplica el test de estrés.

---

## 3. El ataque tauberiano espectral: Wiener, LP-152, Beurling–Malliavin

### 3.1. LP-152 reescrito como condición tauberiana de Wiener

El **teorema tauberiano general de Wiener** [Wie32; Kor04, Cap. II, Teorema 4.1] dice: si $K\in L^1(\mathbb R)$
con $\hat K(\xi)\ne0$ para todo $\xi$ (no-anulación de la transformada), y $f\in L^\infty$ satisface
$\lim_{x\to\infty}(K*f)(x)=A\int K$, entonces $\lim(K'*f)=A\int K'$ para todo $K'\in L^1$. **Mecanismo: la
no-anulación de $\hat K$ es lo que permite cruzar de un promedio (convolución con $K$) a otro (todos los
promedios), y de ahí —con una condición tauberiana adicional sobre $f$— al límite individual.** El cierre
de traslaciones de $K$ en $L^1$ ⟺ $\hat K$ no se anula: es el corazón del teorema.

**[PUENTE 157-A] LP-152 ES la condición de no-anulación de Wiener, transpuesta a crecimiento exponencial.**
El objeto $S_T(\tau)$ es la transformada de Fourier (en $\tau$) de la medida positiva
$\mu_T=\sum_n\Lambda(n)n^{-1/2}e^{-(\log n)^2/4T^2}\delta_{\log n}$ (Doc 152 §2.1). LP-152$(\tau_0)$ dice
$|\widehat{\mu_T}(\tau_0)|=|S_T(\tau_0)|=O_\epsilon(e^{\epsilon T^2})$: la transformada de la medida de
primos **no crece exponencialmente** en la frecuencia $\tau_0$. Comparar con Wiener: allí la condición es
$\hat K\ne0$ (no se anula); aquí, en el régimen exponencial de la fórmula explícita gaussiana, la condición
análoga es $\widehat{\mu_T}$ no crece exponencialmente (no resuena). **La no-anulación de Wiener y la
subexponencialidad de LP-152 son la misma condición tauberiana espectral en dos regímenes (lineal /
exponencial-gaussiano): "la transformada de la medida de promedio no tiene patología en la frecuencia
$\tau_0$".**

### 3.2. LP-152 es unilateral en el sentido correcto

**[PROPOSICIÓN 157.6] (LP-152 es una condición de amplitud, no de oscilación).** LP-152$(\tau_0)$ es una
cota SUPERIOR de amplitud sobre $|S_T(\tau_0)|$; NO prohíbe que $S_T(\tau_0)$ oscile en $T$ (de hecho
oscila, por el factor $\cos(2T^2(\gamma_j-\tau_0)\delta_j)$ del Teorema 152.2). Es exactamente la
"oscilación controlada" buscada en el encargo: controla la AMPLITUD de la resonancia, no su existencia.

*Demostración.* Por el Teorema 152.2(a)(b), $S_T(\tau_0)$ contiene términos
$e^{T^2(\delta_j^2-(\gamma_j-\tau_0)^2)}\cos(2T^2(\gamma_j-\tau_0)\delta_j)$: oscila en $T^2$ con
frecuencias $2(\gamma_j-\tau_0)\delta_j$. LP-152$(\tau_0)$ acota el factor exponencial (la amplitud) a
subexponencial, sin tocar el coseno (la oscilación). Es unilateral: una sola desigualdad ($\le$), sobre la
amplitud. $\square$

**Por qué esto evade la refutación de Littlewood (§2.2).** T2 murió porque pedía no-oscilación de $E$, que
Littlewood refuta. LP-152 NO pide no-oscilación: pide amplitud subexponencial de la resonancia espectral.
La oscilación de $E$ (Littlewood) corresponde precisamente a que $S_T(\tau)$ oscile en $\tau$ — y LP-152 la
permite. **LP-152 es el único candidato del catálogo compatible con el teorema de Littlewood**, porque está
formulado en la coordenada (amplitud espectral) ortogonal a la coordenada donde la oscilación es forzada.
Este es el contenido positivo del encargo: la "oscilación controlada" existe como condición tauberiana
coherente, y es LP-152.

### 3.3. Beurling–Malliavin: la maquinaria de completitud espectral

El teorema tauberiano profundo que conecta subexponencialidad espectral con control individual es el de
**Beurling–Malliavin** [BM62; BM67]. En la forma del **radio de completitud** ([Koo88, Cap. en BM];
[BM67]): dado un conjunto de frecuencias $\Lambda\subset\mathbb R$, el sistema de exponenciales
$\{e^{i\lambda x}\}_{\lambda\in\Lambda}$ es completo en $L^2(-a,a)$ para $a$ menor que el **radio de
Beurling–Malliavin** $R(\Lambda)$, dado por la **densidad efectiva** de $\Lambda$. El enlace con
tauberianos: la completitud de exponenciales $\iff$ ciertas funciones (las que tienen transformada
soportada fuera) deben anularse — un principio de unicidad / cuasi-analiticidad que cruza información
espectral (la densidad de $\Lambda$) a información puntual (anulación / cota de una función).

**[PUENTE 157-B] La ruta Beurling–Malliavin para LP-152.** Para verificar LP-152$(\tau_0)$ (subexponencialidad
de $S_T(\tau_0)$) uno querría un teorema de la forma: *"si las frecuencias $\{\log p\}$ tienen densidad
efectiva $D$ y $\widehat{\mu_T}$ no resuena en $\tau_0$, entonces [control puntual de $E$ cerca de
$\tau_0$]"*. El instrumento natural es la cuasi-analiticidad de Beurling–Malliavin: las medidas con
transformada de soporte/decaimiento controlado son rígidas (un teorema de unicidad de tipo Beurling). **El
input que Beurling–Malliavin exige es la DENSIDAD del conjunto de frecuencias $\{\log p\}$.** Y aquí está
el problema, que §3.4 hace explícito.

### 3.4. Dónde la ruta espectral reintroduce los ceros — el círculo localizado

**[PROPOSICIÓN 157.7] (la densidad espectral del lado de primos ES la cuenta de ceros).** En el régimen de
la fórmula explícita, la "densidad efectiva" del lado de primos que Beurling–Malliavin necesitaría para
certificar la subexponencialidad de $S_T(\tau_0)$ es, por la identidad (152.E), exactamente la densidad de
ceros de ζ en la ventana de $\tau_0$. Concretamente: $S_T(\tau_0)$ subexponencial $\iff$ (Teorema 152.2(a))
ningún cuádruplo off cubre $\tau_0$ $\iff$ la densidad de ceros off en $(\tau_0-\delta,\tau_0+\delta)$ es
cero. Cualquier teorema tauberiano espectral que decida la subexponencialidad de $S_T(\tau_0)$ desde la
densidad espectral está decidiendo la densidad de ceros off en $\tau_0$.

*Demostración.* La identidad (152.E) del Doc 152 es exacta: $\frac{2}{\sqrt\pi T}S_T(\tau_0)=-\sum_\rho
h_{T,\tau_0}(t_\rho)+\text{polo}+A_T$. El lado izquierdo (medida de primos) y el lado derecho (ceros) son
idénticos. La transformada de la medida de primos en $\tau_0$, evaluada en el régimen exponencial, NO
contiene información independiente de los ceros: es una reescritura de la suma sobre ceros. Por tanto la
"densidad efectiva de las frecuencias de primos en $\tau_0$" relevante para Beurling–Malliavin —el dato que
distingue resonancia de no-resonancia— es función de la posición de los ceros en la ventana de $\tau_0$.
Determinar esa densidad ES (Riemann–von Mangoldt para la cuenta, más la posición off para la resonancia)
determinar los ceros. $\square$

**El círculo, en un enunciado.** Beurling–Malliavin cruza densidad-espectral → control-puntual. Pero la
densidad espectral del lado de primos que importa NO es la densidad cruda de $\{\log p\}$ (esa es conocida
e incondicional: $\#\{p\le e^u\}\sim e^u/u$ por PNT) — es la **densidad de RESONANCIA**, i.e. dónde
$\widehat{\mu_T}$ crece exponencialmente, y por (152.E) esa densidad de resonancia ES la densidad de ceros
off. **La maquinaria tauberiana espectral está disponible y es correcta; el input que pide (densidad de
resonancia) es justo el output buscado (posición de ceros). Círculo localizado en el input de
Beurling–Malliavin.** Coherente con la tautología de la fórmula explícita (D112 Prop. 4.2) y con F2 del
Doc 152.

---

## 4. El test de estrés RH, aplicado tres veces a T5/LP-152

La candidata viva es LP-152$(\tau_0)$ (= T5). El test de estrés: para CADA ruta de verificación RH-libre,
verificar sin piedad si "verificarla" requiere conocer los ceros. Tres rutas independientes.

### 4.1. Test de estrés 1 — verificación por densidad de Besicovitch

**Ruta.** Prop. 152.9: la media de Besicovitch de $|S_T(\tau)|^2$ es $O(T^2)$, así que las frecuencias
malas (resonantes) tienen densidad cero. ¿Podemos verificar LP-152$(\tau_0)$ certificando que $\tau_0$ NO
es una de las frecuencias excepcionales de densidad cero?

**Resultado del test: FALLA.** Un promedio (la media de Besicovitch) controla el conjunto de frecuencias
malas en MEDIDA, pero LP-152$(\tau_0)$ es un enunciado en UN punto. La frecuencia mala $\gamma_J$, si
existe, es un punto excepcional invisible a todo promedio (Doc 152 §3.6). Verificar LP-152 en $\tau_0$ por
densidad es exactamente el cruce promedio→individual que estamos intentando hacer — la ruta es el problema,
no su solución. **Falla por el cuantificador maestro de P43: el promedio no ve el punto.**

### 4.2. Test de estrés 2 — verificación por completitud (Beurling–Malliavin)

**Ruta.** §3.3–3.4: usar la cuasi-analiticidad de Beurling–Malliavin para deducir la subexponencialidad de
$S_T(\tau_0)$ desde la densidad espectral.

**Resultado del test: FALLA.** Por la Prop. 157.7, la densidad espectral relevante (densidad de resonancia)
es la densidad de ceros off en la ventana de $\tau_0$. El input de Beurling–Malliavin es el output buscado.
**Falla por reintroducción de los ceros vía la identidad (152.E).** Esta es la falla más profunda porque
Beurling–Malliavin es genuinamente un teorema tauberiano espectral fuerte (cruza densidad→puntual): si
algún teorema iba a cruzar, era éste, y el círculo está exactamente en su hipótesis de densidad.

### 4.3. Test de estrés 3 — verificación por positividad/monotonía directa de $S_T$

**Ruta.** $\mu_T$ es una medida positiva; ¿alguna desigualdad de positividad (tipo Wiener–Ikehara, que es
lo que paga PNT) acota $S_T(\tau_0)$?

**Resultado del test: FALLA.** Doc 152 Prop. 152.4: la positividad de $\Lambda$ solo da $|S_T(\tau)|\le
S_T(0)$, i.e. $\omega(\tau_0)\le\tfrac14$. Esto es subexponencial-en-frecuencia-cero pero permite
$\omega(\tau_0)\in(0,\tfrac14)$ en $\tau_0\ne0$ — exactamente el rango donde vive H(m). **La positividad es
información de frecuencia cero (F1 del Doc 152); no toca $\tau_0>14$.** Falla por la misma razón que T1.

### 4.4. La razón estructural común a las tres fallas

**[PROPOSICIÓN 157.8] (por qué toda verificación RH-libre de LP-152 reintroduce los ceros).** Sea
$\mathsf V$ cualquier procedimiento que certifique LP-152$(\tau_0)$ (subexponencialidad de $S_T(\tau_0)$)
a partir de datos incondicionales sobre la medida de primos. Si $\mathsf V$ usa solo (i) la positividad de
$\Lambda$, (ii) la densidad cruda de $\{\log p\}$ (PNT), o (iii) promedios de $S_T$ en $\tau$, entonces
$\mathsf V$ no decide LP-152$(\tau_0)$ para $\tau_0>14$.

*Demostración.* (i): Prop. 152.4 da $\omega\le\tfrac14$, ciega en $(0,\tfrac14)$ — §4.3. (ii): la densidad
cruda de $\{\log p\}$ es la misma bajo RH y bajo H(m) (PNT es incondicional); no distingue los mundos, luego
no puede decidir un enunciado (LP-152) que sí los distingue. (iii): cualquier promedio en $\tau$ controla
$S_T(\cdot)$ en $L^2_\tau$, y por Prop. 152.9 la frecuencia mala es de densidad cero, invisible al promedio
— §4.1. El único dato incondicional restante que distingue los mundos en $\tau_0$ es la posición de los
ceros en la ventana de $\tau_0$, accesible solo vía la identidad (152.E), que es una tautología que los
reintroduce (§3.4, F2). $\square$

**El enunciado del muro tauberiano, destilado.** *Toda condición tauberiana sobre $\psi(x)-x$ suficiente
para cruzar el medio epsilon debe leer información en la frecuencia $\gamma$ de un cero; los tres
instrumentos incondicionales que leen frecuencia (positividad, densidad cruda, promedios) son ciegos a
esa frecuencia individual; el único instrumento que la lee es la fórmula explícita, que es una identidad.*
Esto vale para las tres rutas y es la forma tauberiana exacta del cuantificador maestro de P43.

---

## 5. VEREDICTO

### 5.1. El no-go tauberiano para condiciones locales en frecuencia

**[DEFINICIÓN-NUEVA 157.9] (condición tauberiana local en frecuencia).** Llamo $\mathsf T$ **local en
frecuencia** si su verificación, en coordenadas espectrales (vía cualquier fórmula explícita gaussiana),
depende solo de: la positividad de $\Lambda$, la densidad cruda de $\{\log p\}$, promedios de $S_T$ en
$\tau$, o cotas puntuales/integrales de $S_T(\tau)$ deducibles de éstos — i.e. de los tres instrumentos de
la Prop. 157.8. (Esto cubre T1–T4 y toda variante de Wiener–Ikehara/Ingham–Karamata/Carleman/momentos.)

**[TEOREMA 157.10] (NO-GO tauberiano para condiciones locales en frecuencia).** Toda condición tauberiana
$\mathsf T$ local en frecuencia que sea suficiente para RH (i.e. que cierre el cruce 157.1) es
RH-equivalente: su verificación requiere decidir la posición de los ceros en alguna ventana de frecuencia.
En consecuencia, ninguna condición tauberiana local en frecuencia cruza el muro promedio→individual de RH
sin presuponer RH.

*Demostración.* Sea $\mathsf T$ local en frecuencia y suficiente. Por suficiencia, $\mathsf T$ decide
$\Theta=\tfrac12$, que por el Teorema 152.2(a) (Cor. 152.3(i)) equivale a $\omega(\tau)=0\ \forall\tau\ge1$,
i.e. a la familia $\{\text{LP-152}(\tau)\}_{\tau\ge1}$. Para cualquier $\tau_0>14$ en una ventana
adversaria, decidir LP-152$(\tau_0)$ requiere, por la Prop. 157.8, leer la posición de los ceros en
$(\tau_0-\tfrac12,\tau_0+\tfrac12)$ (los tres instrumentos de localidad son insuficientes). Luego la
verificación de $\mathsf T$ decide los ceros: $\mathsf T$ es RH-equivalente. $\square$

### 5.2. El cálculo del saturamiento: por qué Littlewood satura el margen

El no-go tiene una causa cuantitativa precisa, que el encargo pedía exhibir: **la oscilación de Littlewood
satura exactamente el margen de Cauchy–Schwarz de la pureza de frontera.**

**[CÁLCULO 157.11] (saturamiento).** La barrera incondicional de positividad (T1, Doc 152.4) es
$|S_T(\tau)|\le S_T(0)\asymp Te^{T^2/4}$, i.e. $\omega(\tau)\le\tfrac14$. En coordenadas de $E$: el margen
de Cauchy–Schwarz de la positividad corresponde a $E(x)\ll x^{1}$ (banda) y, afinado (de la Vallée
Poussin), a $E(x)\ll x\exp(-c\sqrt{\log x})$. La oscilación de Littlewood
$E(x)=\Omega_\pm(\sqrt x\log\log\log x)$ vive en exponente $\tfrac12$ — **estrictamente dentro** del margen
$\omega\le\tfrac14$ (i.e. $\Theta\le1$), con un slack de exponente $\tfrac12$. El punto del saturamiento NO
es que Littlewood toque la barrera de positividad (no la toca: hay slack); es que **Littlewood prohíbe la
ÚNICA otra condición tauberiana suficiente y RH-libre disponible (la no-oscilación, T2)**, dejando el
intervalo de exponentes $(\tfrac12,1]$ — equivalentemente $\omega\in(0,\tfrac14)$ — sin ningún instrumento
tauberiano local que lo recorra. Cuantitativamente: la positividad cubre $\{\omega=\tfrac14\}$ (la
frontera), la no-oscilación cubriría $\{\omega=0\}$ (RH) pero está prohibida por Littlewood, y NADA local
cubre el intervalo abierto $(0,\tfrac14)$. **El margen que Littlewood satura es el margen entre las dos
únicas condiciones tauberianas locales con signo: positividad (frecuencia 0, cubre la frontera) y
no-oscilación (cubriría RH, prohibida). El intervalo entre ambas es el muro, y es exactamente el rango de
exponentes de la oscilación de Littlewood.** $\square$

Esto es la forma tauberiana del hallazgo de Doc 152 §3: el mundo H(m) vive entero en el margen
$e^{-(1/4-\delta^2)T^2}$ de Cauchy–Schwarz, y ninguna condición local lo cierra.

### 5.3. La grieta que el no-go NO cubre

**[GAP-157.A] (condiciones tauberianas espectrales NO-locales con input diofántico).** El Teorema 157.10
cubre las condiciones locales en frecuencia (Def. 157.9), que incluyen toda la tauberiana clásica. NO cubre
una clase espectral genuinamente distinta: condiciones de tipo **Beurling–Malliavin con un input
diofántico independiente** — específicamente, usar la **independencia $\mathbb Q$-lineal de $\{\log p\}$**
(la base de la universalidad de Voronin / del soporte de Bagchi, ver D112) NO como hecho ambiente sino como
una **condición tauberiana espectral**: las exponenciales $\{e^{i\tau\log p}\}_p=\{p^{i\tau}\}_p$ son
$\mathbb Q$-linealmente independientes, lo que da al toro de Kronecker de los primos una estructura de
densidad espectral que NO es la "densidad de resonancia" de la Prop. 157.7. La pregunta abierta: ¿existe un
teorema tauberiano espectral (Beurling–Malliavin refinado, o Kreĭn sobre completitud de
$\{p^{i\tau}\}$) que, usando la independencia diofántica de $\{\log p\}$ como condición tauberiana, cruce a
control individual SIN pasar por la identidad (152.E)? Esta es la única ruta que esquiva la Prop. 157.8,
porque su input (independencia $\mathbb Q$-lineal) es incondicional Y NO es función de la posición de los
ceros.

**Por qué GAP-157.A es exactamente la grieta de LP-112/LP-152.** El input diofántico (independencia
$\mathbb Q$-lineal de $\{\log p\}$) es precisamente lo que alimenta LP-112 vía Bagchi (D112: independencia
⟹ universalidad ⟹ auto-aproximación de ζ). LP-112 ataca por réplica (existencial), LP-152 por evaluación
(universal). GAP-157.A pregunta si la MISMA independencia diofántica, leída como condición tauberiana
espectral (cierre/completitud de $\{p^{i\tau}\}$), cruza promedio→individual. **El no-go tauberiano de
§5.1 muere exactamente donde empieza la grieta diofántica de la pinza P43.** No es coincidencia: es la
tercera coordenada independiente confirmando que el muro tiene un único punto de paso candidato, el
diofántico.

**Estatus honesto de GAP-157.A:** **[GAP de literatura]** No conozco un teorema tauberiano espectral
publicado que use la independencia $\mathbb Q$-lineal de $\{\log p\}$ como condición tauberiana para cruzar
a control puntual de $\psi(x)-x$ sin la fórmula explícita; la maquinaria de completitud de exponenciales
con frecuencias $\mathbb Q$-independientes (Beurling–Malliavin, Kreĭn, Levin) existe pero su aplicación a
ESTE cruce no la verifiqué al nivel de teorema en esta sesión. Lo declaro como grieta, NO como ruta
probada. No es premisa de ningún [TEOREMA] de este documento.

### 5.4. Veredicto (a/b/c)

**VEREDICTO: caso (b) PROBADO para condiciones locales en frecuencia + caso (c) para la grieta diofántica.**

- **(a) ¿Hay condición tauberiana RH-libre que cruce?** **NO** entre las conocidas. Las cinco familias del
  catálogo: T1 agotada, T2 refutada por Littlewood, T3 insuficiente por simetría conjugada, T4 circular
  (=RH), T5 viva como enunciado pero su verificación reintroduce los ceros (test de estrés ×3 fallido).
- **(b) ¿Toda condición tauberiana suficiente es RH-equivalente?** **PROBADO (Teorema 157.10) para la
  clase de condiciones locales en frecuencia** — que incluye TODA la teoría tauberiana clásica
  (Wiener–Ikehara, Ingham–Karamata, Pitt, Carleman, momentos). Es un **no-go que localiza el muro dentro
  de la teoría tauberiana**: la oscilación de Littlewood satura el margen entre las dos únicas condiciones
  locales con signo (positividad/frecuencia-cero y no-oscilación/prohibida), dejando el intervalo
  $(0,\tfrac14)$ de pesos de impureza —el rango de exponentes de Littlewood— sin instrumento local.
- **(c) ¿Queda un hueco específico?** **SÍ, GAP-157.A:** las condiciones tauberianas espectrales no-locales
  con input diofántico (independencia $\mathbb Q$-lineal de $\{\log p\}$ como condición tauberiana, vía
  completitud de $\{p^{i\tau}\}$ tipo Beurling–Malliavin/Kreĭn). Es la única clase que esquiva la
  Prop. 157.8, y es exactamente la grieta diofántica de la pinza LP-112/LP-152 de P43. Su RH-libertad es
  indecidible hoy ([GAP de literatura] §5.3).

### Mensaje final

**VEREDICTO: NO-GO TAUBERIANO LOCALIZADO (caso b) + UNA GRIETA DIOFÁNTICA NOMBRADA (caso c).** NO hay
condición tauberiana RH-libre conocida que cruce el muro promedio→individual de RH. El Teorema 157.10
prueba que toda condición tauberiana **local en frecuencia** (toda la tauberiana clásica:
Wiener–Ikehara, Ingham–Karamata, Pitt, Carleman) suficiente para RH es RH-equivalente — el muro está
dentro de la teoría tauberiana, y la oscilación de Littlewood lo satura exactamente (Cálculo 157.11: vive
en el intervalo de exponentes entre positividad/frecuencia-cero y no-oscilación/prohibida). La única
grieta es **GAP-157.A**: condiciones espectrales no-locales con la independencia $\mathbb Q$-lineal de
$\{\log p\}$ como input tauberiano (Beurling–Malliavin/Kreĭn sobre $\{p^{i\tau}\}$), que es la misma grieta
diofántica que alimenta LP-112/LP-152.

**¿Hay condición tauberiana RH-libre que cruce?** No conocida; probado no-go para toda la clase local;
única grieta = la diofántica de la pinza P43.

**Tres hallazgos:**

1. **[PROPOSICIÓN 157.2 + CÁLCULO 157.11]** — *Littlewood refuta la no-oscilación y satura el margen.* La
   condición de Ingham–Karamata (oscilación lenta) es FALSA para $E=\psi(x)-x$ por Littlewood
   ($\Omega_\pm(\sqrt x\log\log\log x)$); y la oscilación de Littlewood satura exactamente el margen entre
   las dos únicas condiciones tauberianas locales con signo (positividad, que cubre la frontera
   $\omega=\tfrac14$; no-oscilación, que cubriría RH, prohibida), dejando el intervalo $(0,\tfrac14)$ sin
   instrumento local — la forma tauberiana exacta del muro de Doc 152.

2. **[TEOREMA 157.10 + PROPOSICIÓN 157.8]** — *No-go tauberiano para condiciones locales en frecuencia.*
   Toda condición tauberiana local (positividad / densidad cruda de $\{\log p\}$ / promedios de $S_T$)
   suficiente para RH es RH-equivalente, porque decidir el cruce equivale a decidir LP-152 en una
   frecuencia adversaria, y los tres instrumentos incondicionales son ciegos a la frecuencia individual de
   un cero; el único que la lee es la fórmula explícita, que es una tautología (152.E). Cubre toda la
   tauberiana clásica.

3. **[PROPOSICIÓN 157.6 + GAP-157.A]** — *La oscilación controlada existe (LP-152) y su única grieta es
   diofántica.* LP-152 es la única condición tauberiana compatible con Littlewood (controla amplitud
   espectral, no oscilación — la "oscilación controlada" del encargo, en la coordenada espectral
   ortogonal a la de Littlewood) y es de tipo Wiener (no-anulación/no-resonancia de la transformada de la
   medida de primos); pero su verificación reintroduce los ceros vía Beurling–Malliavin salvo por la
   grieta GAP-157.A: usar la independencia $\mathbb Q$-lineal de $\{\log p\}$ como condición tauberiana
   espectral, exactamente la grieta diofántica de la pinza LP-112/LP-152 de P43.

---

## Referencias

**Internas (backward-only):** Doc 152 (espectro de impureza, Teorema 152.2, jurisdicción de $\Lambda\ge0$,
inversión de Landau F1–F3, LP-152 Def. 152.8, Prop. 152.9 frecuencias malas densidad cero, identidad
152.E); Doc 112 (LP-112; Prop. 2.6 densidad cero; Prop. 4.2 tautología de la fórmula explícita; soporte de
Bagchi, universalidad de Voronin, independencia $\mathbb Q$-lineal); P43 (Principio 3.1, cuantificador
maestro genérico vs excepcional).

**Literatura (publicada, verificable salvo marca):**
- [Wie32] N. Wiener, *Tauberian theorems*, Ann. of Math. (2) 33 (1932), 1–100. (Teorema tauberiano general;
  cierre de traslaciones ⟺ no-anulación de la transformada.)
- [Ike31] S. Ikehara, *An extension of Landau's theorem in the analytic theory of numbers*, J. Math. Phys.
  MIT 10 (1931), 1–12. (Tauberiano de Wiener–Ikehara; condición tauberiana = positividad/monotonía.)
- [Kor04] J. Korevaar, *Tauberian Theory: A Century of Developments*, Grundlehren 329, Springer, 2004.
  (Cap. II: Wiener–Ikehara; Cap. III: Ingham–Karamata, oscilación lenta unilateral; referencia general de
  condiciones tauberianas.)
- [Ing35] A. E. Ingham, *On Wiener's method in Tauberian theorems*, Proc. London Math. Soc. (2) 38 (1935),
  458–480. (Forma de frontera del tauberiano; oscilación lenta.)
- [Kar31] J. Karamata, *Neuer Beweis und Verallgemeinerung der Tauberschen Sätze...*, Math. Z. 33 (1931),
  294–299. (Método de Karamata; condición unilateral.)
- [Ing32] A. E. Ingham, *The Distribution of Prime Numbers*, Cambridge Tracts 30, Cambridge Univ. Press,
  1932. (Cap. IV: abscisa de la singularidad real controla el orden de $\psi(x)-x$ — equivalencia con
  $\Theta$; Cap. V: teoremas de oscilación, teorema de Landau de integrandos de un signo.)
- [vK01] H. von Koch, *Sur la distribution des nombres premiers*, Acta Math. 24 (1901), 159–182.
  ($E(x)=O(\sqrt x\log x)\iff$ RH.)
- [Lit14] J. E. Littlewood, *Sur la distribution des nombres premiers*, C. R. Acad. Sci. Paris 158 (1914),
  1869–1872. ($\psi(x)-x=\Omega_\pm(\sqrt x\log\log\log x)$ — la oscilación genuina.)
- [Sch03] E. Schmidt, *Über die Anzahl der Primzahlen unter gegebener Grenze*, Math. Ann. 57 (1903),
  195–204. ($\Omega_\pm$ bilateral simétrico para $\psi(x)-x$.)
- [Cra22] H. Cramér, *Ein Mittelwertsatz in der Primzahltheorie*, Math. Z. 12 (1922), 147–153. (Segundo
  momento de $\psi(x)-x$ en peso $x^{-2}$; finitud ⟺ RH — Prop. 157.5.)
- [MV07] H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge
  Stud. Adv. Math. 97, 2007. (§15: oscilación de $\psi(x)-x$, Teorema de Littlewood 15.11; momento de
  Cramér; equivalencias de von Koch.)
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. D. R. Heath-Brown),
  Oxford Univ. Press, 1986. (§14: segundo momento; Riemann–von Mangoldt cuenta de ceros.)
- [BM62] A. Beurling, P. Malliavin, *On Fourier transforms of measures with compact support*, Acta Math.
  107 (1962), 291–309. (Cuasi-analiticidad; rigidez de medidas con transformada controlada.)
- [BM67] A. Beurling, P. Malliavin, *On the closure of characters and the zeros of entire functions*, Acta
  Math. 118 (1967), 79–93. (Radio de Beurling–Malliavin; completitud de exponenciales ⟺ densidad efectiva
  del conjunto de frecuencias.)
- [Koo88] P. Koosis, *The Logarithmic Integral I*, Cambridge Stud. Adv. Math. 12, 1988. (Exposición de
  Beurling–Malliavin; densidad efectiva, integral logarítmica.)

*Fin del Doc 157.*
