# Doc 156 — Probe de índice / Maslov: ¿es κ=2m un índice con símbolo RH-libre?

**Programa:** Hipótesis de Riemann — Phase 49: CRUZAR EL MURO.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** probe técnico del **frente principal** declarado en Doc 154. El objeto **NO** es producir
otra equivalencia RH ⟺ X. El objeto es atacar el cruce **valor → inercia** del cuantificador maestro usando el
único mecanismo probado que lo cruza: la teoría del índice (M5 de Doc 154). Pregunta única:
**¿es κ=2m computable por un teorema del índice, y ese símbolo es RH-libre (computable desde los primos) o
codifica RH en secreto?**

**Contrato de etiquetado:** **[DEFINICIÓN-NUEVA]** = libertad total. **[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = con
prueba completa, estándar máximo. **[PUENTE]** = conexión honesta, NO una equivalencia de RH. **[TEST DE ESTRÉS]**
= la guardia anti-círculo, al frente. **[GAP]/[GAP de literatura]/[DESEO]** = declarados sin vergüenza.
**Restricciones:** español; sin numéricos/Python; citas a literatura publicada real.

---

## 0. Resumen ejecutivo y veredicto adelantado

Coloco el veredicto al principio (honestidad: no quiero que el lector lo descubra como sorpresa al final).

> **VEREDICTO: caso (b) — κ ES de tipo índice, pero el símbolo codifica RH, y RH entra en la FREDHOLMICIDAD,
> no en la clase.** Más finamente: el operador autoadjunto $H_C$ en el espacio de Pontryagin $(\mathcal K,Q)$
> sólo es **Fredholm con índice de inercia finito y bien definido** cuando $m<\infty$; el número $\kappa=2m$
> es entonces literalmente un **spectral flow / índice de Maslov** de una familia de lagrangianas, pero la
> **buena-definición de esa familia** (la existencia de un Pontryagin space $\Pi_\kappa$ con $\kappa<\infty$,
> Kreĭn–Langer) **presupone $m<\infty$**, y $m<\infty$ no es verificable desde los primos sin información sobre
> la localización de los ceros. El símbolo aritmético (el lado de Weil $\sum_p \Lambda$) **sí** se computa desde
> los primos —es RH-libre como *valor*— pero la **partición de ese valor en inercia** (el conteo de signos
> negativos = $\kappa$) **no** desciende al cociente módulo compactos sin saber dónde están los ceros. Esto es
> exactamente la **autonomía del valor vs autonomía de la inercia** que P43 Thm 4.2 ya había aislado, ahora
> localizada DENTRO de la maquinaria del índice.

Tres hallazgos etiquetados al final (§7). La estructura: §1 recuerda el puente y nombra el operador; §2 plantea
el índice (Maslov/sf/APS/Toeplitz/Connes–Moscovici); §3 el símbolo y el test de estrés; §4 las cinco herramientas
una por una; §5 el obstáculo localizado; §6 la distinción Fredholmicidad vs clase.

---

## 1. El operador cuya inercia es κ=2m, y su dominio

### 1.1 Recordatorio preciso del teorema-puente (Phase 26)

El teorema-puente (Doc 26-C.2, memoria `project-phase26-bridge`) afirma, bajo Hipótesis D con $\kappa=2m$:

> El operador de escala de Connes $H_C$, visto como operador **$Q$-simétrico** sobre el **espacio de Pontryagin**
> $\mathcal K=(L^2(C_\mathbb Q), Q)$ —$Q$ la forma de Weil— tiene exactamente $\kappa=2m$ autovalores complejos
> $\{b_j+i\gamma_j\}\cup\{-b_j+i\gamma_j\}$, uno por cada cuádruplo de ceros off-line
> $\rho_j=(\tfrac12+b_j)+i\gamma_j$. Corolario: RH ⟺ $\kappa=0$ ⟺ $H_C$ genuinamente autoadjunto en $\mathcal K$.

Aquí $C_\mathbb Q=\mathbb A^\times_\mathbb Q/\mathbb Q^\times$ es el grupo de clases de idèles, $H_C$ es el generador
(no acotado) de la acción de escala (el "$H$" del marco espectral de Connes 1999), y $Q$ es la forma de Weil
realizada como producto interno **indefinido** sobre un subespacio. Los items abiertos V.1–V.4 (V.1: $Q$-simetría;
V.2: caracteres en $\mathcal K$, probablemente isotrópicos; V.3: neg.ind$(H_C)=\kappa$ vía Kreĭn–Langer; V.4: conteo
de la órbita de Klein) siguen **abiertos** — esto es un puente conjetural, lo cito como tal.

### 1.2 Lo que es robusto y lo que no (post-ERRATA de Phase 38/46)

**Robusto (lo uso):** el invariante algebraico **neg.ind$(Q)$** = número de cuadrados negativos de la forma de
Weil en una realización finito-dimensional dada; la superaditividad tensorial neg.ind$(Q_1\otimes Q_2)=p_1q_2+q_1p_2$
(Doc 117, INTACTA, $p_i,q_i\ge1$). **Refutado (NO lo uso):** $W_\lambda\ge0$ (Doc 114), la rama
"$T_\lambda=0\;\forall\lambda\Rightarrow$RH" de P39 que dependía de ello, y todo lo marcado en ERRATA. En particular
**no** afirmo que $\kappa$ sea finito incondicionalmente: bajo $\neg$RH general $\kappa$ puede ser $\infty$
(es la observación de Doc 107(4): "$\kappa(Q_2)$ global $=\infty$ bajo $\neg$RH; el invariante útil es el bloque
relativo"). Esta finitud condicional es, anticipo, **el corazón del obstáculo**.

### 1.3 [DEFINICIÓN-NUEVA 156.1 — el operador autoadjunto candidato y su dominio]

Para tener un objeto sobre el cual hablar de índice necesito un operador **autoadjunto** (no sólo $Q$-simétrico)
en un espacio de Hilbert genuino, no en el Pontryagin. Construyo el candidato canónico de la teoría de Kreĭn–Langer.

Sea $(\mathcal K,Q)$ un espacio de Pontryagin con $\kappa$ cuadrados negativos finitos, i.e. $\mathcal K=\mathcal K_+
\oplus\mathcal K_-$ con $\dim\mathcal K_-=\kappa<\infty$ y $Q=\langle\cdot,\cdot\rangle_+ - \langle\cdot,\cdot\rangle_-$.
Sea $J$ la **simetría fundamental** ($J|_{\mathcal K_\pm}=\pm 1$); entonces $\langle f,g\rangle_J:=Q(Jf,g)$ es el
producto de Hilbert asociado y $H_J:=J H_C$ es **$\langle\cdot,\cdot\rangle_J$-autoadjunto** si $H_C$ es
$Q$-autoadjunto (Bognár, *Indefinite Inner Product Spaces*, Springer 1974, cap. VI; Azizov–Iokhvidov,
*Linear Operators in Spaces with an Indefinite Metric*, Wiley 1989, cap. 2).

**El operador del probe es $H_J=JH_C$, sobre el dominio $\mathrm{dom}(H_C)\subseteq\mathcal K$ con la topología de
Hilbert de $\langle\cdot,\cdot\rangle_J$.** La inercia que llamamos $\kappa$ es $\dim\mathcal K_-=$ dimensión del
subespacio negativo maximal $Q$-definido — un **entero**, candidato a índice.

**Punto técnico no decorativo:** $\kappa<\infty$ es **parte de la definición de espacio de Pontryagin**. Si la forma
de Weil tuviera infinitos cuadrados negativos (lo cual ocurre bajo $\neg$RH con infinitos ceros off-line, Doc 107(4)),
$(\mathcal K,Q)$ es un **espacio de Kreĭn**, no de Pontryagin, $J$ existe pero $\dim\mathcal K_-=\infty$, y el
"número $\kappa$" deja de ser un entero. **Esta es la primera aparición del muro**, y la marco ya: *el objeto
"índice" sólo existe en la categoría Pontryagin, cuya hipótesis definitoria es $m<\infty$.*

---

## 2. El planteo del índice: Maslov / spectral flow / APS / Toeplitz / Connes–Moscovici

El encargo (punto 2) insiste —correctamente— en que para la **inercia de una forma cuadrática** el invariante
natural NO es el índice de Fredholm clásico (Atiyah–Singer dim finita compacta) sino el **índice de Maslov /
spectral flow** de una familia de autoadjuntos o lagrangianas. Desarrollo el planteo.

### 2.1 Por qué Atiyah–Singer clásico NO aplica (cierre rápido, ya visto en Phase 41)

$H_C$ vive en dim $\infty$ (no hay variedad compacta), su flujo es continuo (la acción de escala $\mathbb R$ es un
grupo de Lie de rango 1, no hay simbolo elíptico sobre un cotangente compacto), y el espectro es continuo
(Connes: el espectro de absorción cubre toda la recta crítica). Atiyah–Singer 1968 (Ann. of Math. 87, 484–530;
546–604) requiere elipticidad sobre variedad cerrada — ausente. **Cerrado: A–S clásico no aplica** (coincide con
el veredicto de Phase 41, donde Babaee–Huh obstruye y AHK no aplica).

### 2.2 [DEFINICIÓN-NUEVA 156.2 — κ como spectral flow de una deformación de los ceros]

La idea correcta: $\kappa$ debe ser un **spectral flow**. Construyo la familia.

Sea $\{H_C(t)\}_{t\in[0,1]}$ una familia de operadores $Q_t$-autoadjuntos que interpola entre un operador de
referencia con espectro real (todos los ceros on-line, $t=0$, RH "impuesta artificialmente" como punto base) y el
operador aritmético genuino ($t=1$). El **spectral flow** $\mathrm{sf}\{H_C(t)\}$ cuenta, con signo, el número neto
de autovalores que cruzan el eje real (en el caso Pontryagin: que migran de la parte $Q$-positiva a la $Q$-negativa
del espectro) al recorrer la familia. Por la teoría de Phillips (J. Funct. Anal. / Canad. Math. Bull. 39 (1996)
460–467, "Self-adjoint Fredholm operators and spectral flow") el spectral flow de un lazo de Fredholm autoadjuntos
es un entero homotópicamente invariante.

**El planteo de Phase 28 (Frente B) es exactamente éste:** $\kappa=\mathrm{sf}=\mathrm{Ind}(D_{\mathrm{APS}})+
\eta(T_0)/2$, con la pregunta abierta "¿es $\eta(T_0)=0$ por anticometización de Fourier?". Aquí $D_{\mathrm{APS}}$
es el operador de Dirac suspendido $\partial_t + H_C(t)$ sobre el cilindro $[0,1]\times(\text{base})$ con condiciones
de frontera de Atiyah–Patodi–Singer (Math. Proc. Camb. Phil. Soc. 77 (1975) 43–69), y $\eta(T_0)$ es el invariante
eta del operador de frontera. La fórmula APS:
$$\mathrm{Ind}(D_{\mathrm{APS}}) = \int_{\text{cilindro}}\widehat A\,\mathrm{ch} - \frac{\eta+h}{2}\Big|_{\partial},$$
con el **defecto espectral** $\eta/2$ midiendo precisamente la asimetría que el índice interior no ve.

### 2.3 [DEFINICIÓN-NUEVA 156.3 — κ como índice de Maslov de un par de lagrangianas]

Equivalentemente (Booss-Bavnbek–Wojciechowski, *Elliptic Boundary Problems for Dirac Operators*, Birkhäuser 1993,
caps. 14–17; y Cappell–Lee–Miller, Comm. Pure Appl. Math. 47 (1994) 121–186, sobre la igualdad
spectral flow = índice de Maslov): a la familia $\{H_C(t)\}$ se le asocia una **curva de lagrangianas** $\{L(t)\}$
en un espacio simpléctico (el espacio de datos de Cauchy / el grafo de la resolvente), y
$$\kappa = \mathrm{sf}\{H_C(t)\} = \mathrm{Mas}(L(0),L(1)) = \mu_{\mathrm{Maslov}},$$
el **índice de Maslov** del par, que cuenta intersecciones con el ciclo de Maslov (el lugar donde $L(t)$ deja de
ser transversal a una lagrangiana de referencia). Esta es la conexión con **Conj. 100.A (Maslov semilocal)** de
Phase 35: la conjetura $\mu_{\infty,2}=0$ es precisamente la afirmación de que cierta contribución de Maslov
**de segundo orden** se anula — y D100 encontró el obstáculo $O_{SL}$ = **no-uniformidad en $n$ del control
Weil–Sonine**. Marco la coincidencia: el obstáculo de la ruta Maslov de Phase 35 es de **no-uniformidad**, que es
exactamente el patrón del muro de Doc 154 (PUENTE 154.7: el ángulo $\theta$ degenera, la "constante" depende del
parámetro límite).

### 2.4 La estructura común de los tres planteos

Maslov, spectral flow y APS-eta son **el mismo entero** en presencia de Fredholmicidad (teorema de Cappell–Lee–Miller
+ Phillips): $\mathrm{Mas}=\mathrm{sf}=\mathrm{Ind}(D_{\mathrm{APS}})$ módulo el término de frontera $\eta/2$. Por tanto
no hay que elegir: **si $\kappa$ es un índice, es estos tres a la vez**, y la pregunta del probe se concentra en el
**input común** de los tres: la existencia de la familia $\{H_C(t)\}$ con **extremos Fredholm** y trayectoria de
lagrangianas **bien definida**. Eso me lleva al test de estrés.

---

## 3. El símbolo candidato y el TEST DE ESTRÉS RH (la guardia anti-círculo)

Pongo el test al frente, como ordena el encargo. Si $\kappa$ es un índice, hay una fórmula índice = ∫(símbolo).
El símbolo debe poder leerse desde los **primos** (la presentación aritmética de la forma de Weil).

### 3.1 [DEFINICIÓN-NUEVA 156.4 — el símbolo aritmético candidato]

La forma de Weil, en su presentación explícita (Weil 1952; Bombieri, en *The Riemann Hypothesis*, Clay 2000), es
$$Q(f) = \underbrace{\sum_\rho \widehat f(\rho)}_{\text{ceros}}
= \underbrace{\widehat f(0)+\widehat f(1)}_{\text{polo}}
- \underbrace{\sum_p\sum_{k\ge1}\frac{\log p}{p^{k/2}}\big(f(\log p^k)+f(-\log p^k)\big)}_{\text{primos: } A_{\mathrm{arith}}(f)}
- \underbrace{(\text{término arquimediano }\Gamma)}_{W_\infty(f)}.$$
El **lado aritmético** $A_{\mathrm{arith}}$ está escrito enteramente en términos de $\log p$ y $\Lambda(p^k)=\log p$
— es **manifiestamente computable desde los primos**, sin referencia a la localización de los ceros. Éste es el
**símbolo candidato** del probe: el operador de Toeplitz/convolución $T_g$ cuyo símbolo es la función generadora
$g(x)=\sum_p\sum_k \frac{\log p}{p^{k/2}}\delta_{\pm\log p^k}$ sobre el grupo $\mathbb R$ (lado idélico:
$\prod_p$ local).

### 3.2 [TEST DE ESTRÉS — la pregunta decisiva]

> **¿El símbolo se computa conociendo sólo los primos (RH-libre), o su buena-definición / su clase de K-teoría /
> su invertibilidad fuera del compacto requiere ya saber que los ceros están en la línea?**

Aplico el test en sus tres modos de fallo conocidos.

**(Modo de fallo 1 — Fredholmicidad/invertibilidad en la corona).** El operador es Fredholm ⟺ su símbolo es
**invertible en la corona** (el espacio de símbolos módulo compactos). El símbolo de $T_g$ es, vía transformada de
Mellin/Fourier sobre $C_\mathbb Q$, **la función zeta misma**: el "símbolo de Toeplitz" del lado aritmético es
$\zeta(s)/\zeta(s)$ leído sobre la recta crítica, cuyo **conjunto de ceros** es exactamente el lugar donde el
símbolo se anula. **El símbolo es invertible fuera de un compacto ⟺ los ceros off-line son finitos en número**
($m<\infty$). **FALLA EL TEST EN MODO 1.** El operador deja de ser Fredholm sin $m<\infty$. Esto es decisivo y lo
desarrollo en §5.

**(Modo de fallo 2 — la lagrangiana bien definida sólo bajo RH).** La curva $\{L(t)\}$ del índice de Maslov (156.3)
debe ser una curva en la **grassmanniana de Fredholm-lagrangianas** (Booss-Bavnbek–Wojciechowski cap. 15). Para que
$\mathrm{Mas}$ sea un entero finito, el ciclo de Maslov debe ser cruzado un número **finito** de veces — i.e. la
familia cruza el lugar no-transversal finitas veces. Cada cruce = un cero migrando off-line. **Finitos cruces ⟺
$m<\infty$.** **FALLA EL TEST EN MODO 2 también.** Es el mismo muro que el modo 1, visto en coordenadas simplécticas.

**(Modo de fallo 3 — la clase de K-teoría mal definida).** Éste es el modo MENOS obvio y el más informativo.
Supóngase que aceptamos $m<\infty$ (entramos en la categoría Pontryagin por fiat). Entonces $T_g$ ES Fredholm y
tiene una clase $[\sigma(T_g)]\in K^1(\text{corona})$. **¿Se computa el índice topológico desde esa clase sin saber
$m$?** Aquí el test da un resultado más matizado, que separo en §6: la clase existe, pero su **pairing con el
generador de $K_1$** (el winding number del símbolo $\zeta$ a lo largo de la recta crítica) **es** $-2m$ por el
principio del argumento — y computar ese winding **es** contar los ceros off-line. **El valor del símbolo es
RH-libre; el winding (la inercia) no lo es.**

### 3.3 Veredicto del test de estrés

El símbolo aritmético $A_{\mathrm{arith}}$ pasa el test **como valor** (se computa desde los primos) y **falla el
test como inercia** en los tres modos. Los modos 1 y 2 son el mismo fenómeno (Fredholmicidad ⟺ $m<\infty$); el modo
3 dice que, incluso concedida la Fredholmicidad, el cálculo del índice **es** el conteo de ceros. La distinción
fina entre modo 1/2 (Fredholmicidad) y modo 3 (clase) es la pregunta del encargo punto 5, y la respondo en §6:
**el muro está en la Fredholmicidad** (modos 1/2 son lógicamente anteriores: sin $m<\infty$ no hay siquiera operador
de tipo índice), y el modo 3 muestra que **aun reparando la Fredholmicidad por fiat, el índice es tan duro como RH.**

---

## 4. Las cinco herramientas, una por una: ¿aplica? ¿símbolo? ¿pasa el test?

Recorro las herramientas del encargo punto 4, con cita real, dictamen, símbolo y test.

### 4.1 (a) Atiyah–Singer clásico

- **¿Aplica?** **NO.** Dim $\infty$, sin variedad compacta, espectro continuo (§2.1). Cerrado en Phase 41.
- Ref: Atiyah–Singer, Ann. of Math. 87 (1968) 484–530, 546–604.

### 4.2 (b) Spectral flow + APS

- **¿Aplica?** **Parcialmente, condicional.** La fórmula $\kappa=\mathrm{sf}=\mathrm{Ind}(D_{\mathrm{APS}})+\eta/2$
  (Phillips 1996; APS 1975) es el marco correcto para inercia de familias autoadjuntas.
- **Símbolo:** el operador de frontera $T_0=H_C$ y su invariante $\eta$; el "símbolo" es la fase del espectro de
  $H_C$ sobre la recta crítica.
- **Test de estrés:** **FALLA.** La familia $\{H_C(t)\}$ con extremos Fredholm autoadjuntos **existe sólo si**
  ambos extremos son Fredholm; el extremo aritmético ($t=1$) es Fredholm ⟺ $m<\infty$ (§3.2 modo 1). Además
  Phase 28 dejó **abierto** si $\eta(T_0)=0$, y D28 §08 (resultado final) mostró que el sector aritmético
  $G_\zeta$ —que controla el signo de la segunda variación, pariente del $\eta$— es **incontrolable en
  $\sigma=1/2$ sin RH (Wall A persiste)**. El defecto $\eta/2$ es justamente donde se esconde RH.
- Ref: Phillips, Canad. Math. Bull. 39 (1996) 460–467; APS, Math. Proc. Camb. Phil. Soc. 77 (1975) 43–69.

### 4.3 (b′) Índice de Maslov

- **¿Aplica?** **Parcialmente, condicional** (es el avatar simpléctico del anterior, §2.3).
- **Símbolo:** la curva de lagrangianas $\{L(t)\}$, ciclo de Maslov = lugar de no-transversalidad.
- **Test de estrés:** **FALLA en modo 2** (§3.2): finitud del índice de Maslov ⟺ finitos cruces del ciclo ⟺
  $m<\infty$. Conexión con **Conj. 100.A** de Phase 35: el obstáculo $O_{SL}$ (no-uniformidad en $n$ del control
  Weil–Sonine) es el muro de Doc 154 en coordenadas Maslov. La componente $\mu_{\infty,2}$ (Maslov semilocal de
  segundo orden) es la que codifica RH.
- Ref: Booss-Bavnbek–Wojciechowski, *Elliptic Boundary Problems for Dirac Operators*, Birkhäuser 1993, caps. 14–17;
  Cappell–Lee–Miller, Comm. Pure Appl. Math. 47 (1994) 121–186; Robbin–Salamon, Bull. LMS 27 (1995) 1–33
  (índice de Maslov de curvas de lagrangianas).

### 4.4 (c) Índice de Toeplitz (Boutet de Monvel) sobre el álgebra de Weil–Toeplitz

- **¿Aplica?** **SÍ, formalmente — y es el planteo más nítido.** El álgebra de Weil–Toeplitz $\mathcal W$ del
  Doc 134 (con su ideal de compactos $\mathcal J$) es exactamente el escenario donde un índice de Toeplitz tiene
  sentido: $0\to\mathcal J\to\mathcal W\to\mathcal W/\mathcal J\to 0$, símbolo en la corona $\mathcal W/\mathcal J$.
- **Símbolo:** el símbolo de $T_g$ vive en $\mathcal W/\mathcal J$ y, por la identificación Gram↔Weil
  (Doc 148/151 Prop. 1.1, **EXACTA y SOBREVIVIENTE**), su clase es la del símbolo aritmético sobre el grupo de
  caracteres. Boutet de Monvel (Acta Math. 126 (1971) 11–51, "Boundary problems for pseudo-differential operators";
  y el índice de Toeplitz, Invent. Math. 50 (1979) 249–272): $\mathrm{Ind}(T_\phi)=-\mathrm{winding}(\phi)$ para
  símbolo invertible $\phi$.
- **Test de estrés:** **FALLA en modo 1, y el modo 3 se ilumina aquí.** El símbolo $\phi=$ "lado aritmético leído
  como función sobre la corona" es invertible ⟺ no tiene ceros en la corona ⟺ los ceros off-line son finitos
  ($m<\infty$). Concedido $m<\infty$: $\mathrm{Ind}(T_\phi)=-\mathrm{winding}=-2m$ por el **principio del argumento**
  (el winding de $\zeta$ a lo largo del contorno crítico cuenta ceros menos polos). **El winding ES el conteo de
  ceros.** Confirma exactamente la arquitectura "los ceros viven en la frontera símbolo/compacto" del Doc 134
  (Thm 5.3′ corregido en ERRATA E46.4: positividad estricta del símbolo ⟺ ventanas visibles finitas ⟺ $m<\infty$).
  **Es la herramienta donde el muro se ve con más claridad: símbolo RH-libre como objeto, winding = RH.**
- **[GAP de literatura]:** Boutet de Monvel está para variedades con frontera de dim finita; su extensión al
  álgebra de Weil–Toeplitz sobre $C_\mathbb Q$ (idélica, dim $\infty$) **no está construida** — uso el principio del
  argumento como sustituto morally-correcto, declarándolo.

### 4.5 (d) Fórmula del índice local de Connes–Moscovici

- **¿Aplica?** **Condicional, y es el candidato T5 con "input nuevo" del Doc 154 §5 [GAP].** Connes–Moscovici
  (GAFA 5 (1995) 174–243, "The local index formula in noncommutative geometry") computa el índice de un triple
  espectral $(\mathcal A, H, D)$ vía el **carácter de Chern–Connes** y los residuos de la función zeta del operador
  $|D|$. Si existiera un triple espectral aritmético cuyo $D$ fuese (relacionado con) $H_C$ y cuyo carácter de Chern
  diese $\kappa$, sería el cruce T5 con input aritmético.
- **Símbolo:** los **residuos** $\mathrm{Res}_{s=0}\mathrm{Tr}(a\,|D|^{-s})$ — la función zeta espectral del triple.
- **Test de estrés:** **FALLA, y de la forma más reveladora.** La función zeta espectral de un triple cuyo operador
  es la escala de Connes **ES (esencialmente) $\zeta$ de Riemann** (es el contenido del marco de Connes 1999, Selecta
  Math. 5, 29–106: el lado espectral reproduce la fórmula explícita de Weil). Por tanto el "símbolo" de
  Connes–Moscovici (los residuos de la zeta espectral) **tiene a $\zeta$ literalmente dentro**; pedir que el
  carácter de Chern compute $\kappa$ es pedir los residuos de $\zeta$ en la región crítica = RH. **El input
  (la dimensión-espectral / sumabilidad del triple, i.e. que $|D|^{-s}$ sea de clase traza para $\mathrm{Re}(s)$
  grande) es verificable RH-libre, PERO el carácter de Chern no se evalúa sin la continuación analítica de la zeta
  espectral en la franja crítica** — exactamente el dato que RH gobierna.
- **[GAP de literatura, central]:** un triple espectral $(\mathcal A, H, D)$ finitamente sumable cuyo carácter de
  Chern produzca $\kappa=2m$ desde datos aritméticos **no existe en la literatura**. Esto es **idéntico** al
  [GAP de literatura] del Doc 154 §5 ("la clase cohomológica sobre Spec ℤ que leería inercia, T5 con input
  inexistente") y a la frontera de Phases 40–43. Lo confirmo desde la maquinaria del índice: el hueco no es lógico
  (T5 está bien tipado), es que el **triple espectral con el input correcto no se ha construido**, y los candidatos
  conocidos (Connes 1999; Connes–Consani CCM, arXiv:2511.22755 verificado en D99) **portan $\zeta$ en su métrica**,
  que es la circularidad de Phase 43 (la métrica de polarización porta ζ en la coordenada inercia).

### 4.6 Tabla-resumen del recorrido

| Herramienta | ¿Aplica? | Símbolo | Test de estrés | Modo de fallo |
|---|---|---|---|---|
| (a) Atiyah–Singer | NO | — | — | dim ∞, no compacta |
| (b) sf + APS | condicional | fase de $H_C$, $\eta(T_0)$ | FALLA | familia Fredholm ⟺ $m<\infty$; $\eta$=Wall A |
| (b′) Maslov | condicional | curva de lagrangianas | FALLA | finitos cruces ⟺ $m<\infty$; $O_{SL}$ no-uniforme |
| (c) Toeplitz (BdM) | sí formal | $\phi$ en corona $\mathcal W/\mathcal J$ | FALLA | invertible ⟺ $m<\infty$; winding=RH |
| (d) Connes–Moscovici | condicional [GAP] | residuos de zeta espectral | FALLA | zeta espectral = ζ; Chern=continuación crítica |

**Las cuatro herramientas que "aplican" fallan el test en el mismo punto:** la existencia/Fredholmicidad del objeto
requiere $m<\infty$, y la evaluación del índice (cuando se concede Fredholmicidad) es el conteo de ceros. La
herramienta (d) es la única con un input potencialmente verificable distinto (sumabilidad del triple) — pero el
triple correcto no existe.

---

## 5. El obstáculo localizado: caso (b), y dentro de (b) es FREDHOLMICIDAD

### 5.1 Descarte de (a) y (c) del encargo punto 5

- **No es caso (a)** (κ computable con símbolo RH-libre): los cuatro caminos fallan el test. No hay símbolo
  RH-libre para la inercia. (Y el encargo ordena desconfiar de (a); confirmo que no se da.)
- **No es caso (c)** (κ no es de tipo índice por obstrucción estructural): κ **sí** es de tipo índice — es
  literalmente spectral flow / Maslov / winding de Toeplitz, **bajo $m<\infty$**. No hay obstrucción estructural
  a que sea un índice; el problema es que el índice **codifica** RH. Por eso no es (c).

### 5.2 [TEOREMA 156.5 — la inercia es índice, condicional a Fredholmicidad]

> *Sea $\mathcal W/\mathcal J$ el álgebra de símbolos de Weil–Toeplitz y $\phi$ el símbolo aritmético (156.4).
> Si $\phi$ es invertible en la corona (equivalentemente, si el número $m$ de cuádruplos de ceros off-line es
> finito), entonces $T_\phi$ es Fredholm y*
> $$\kappa = \mathrm{neg.ind}(Q) = -\mathrm{Ind}(T_\phi) = \mathrm{winding}(\phi) = 2m,$$
> *un entero igual al spectral flow de $\{H_C(t)\}$ y al índice de Maslov $\mathrm{Mas}(L(0),L(1))$.*

**Prueba (esquema, con los eslabones que descansan en puente declarados).** (i) Atkinson: $T_\phi$ Fredholm ⟺ $\phi$
invertible módulo $\mathcal J$ — estándar (Douglas, *Banach Algebra Techniques in Operator Theory*, 2ª ed. Springer
1998, cap. 7). (ii) $\phi$ invertible en la corona ⟺ $\phi$ sin ceros en la corona ⟺ los ceros de $\zeta$ que el
símbolo ve (los off-line, los visibles del Doc 134 Thm 5.3′) son finitos ⟺ $m<\infty$ — esto descansa en la
identificación Gram↔Weil (Doc 148/151 Prop. 1.1, exacta) y en la corrección Thm 5.3′ del ERRATA E46.4
[PUENTE, no teorema cerrado: la identificación del lugar de ceros del símbolo con los ceros off-line es la conjetura
de Phase 26/Doc 134]. (iii) $\mathrm{Ind}(T_\phi)=-\mathrm{winding}(\phi)$ — teorema clásico de Toeplitz
(Gohberg–Krein; Boutet de Monvel para el caso pseudo-diferencial), morally extendido al caso idélico [GAP de
literatura §4.4]. (iv) $\mathrm{winding}(\phi)=2m$ por el principio del argumento aplicado al contorno crítico
(cuenta ceros off-line con su multiplicidad simétrica de cuádruplo). (v) La igualdad con sf y Maslov es
Cappell–Lee–Miller + Phillips, bajo Fredholmicidad de los extremos. $\square$ (condicional a $m<\infty$ y a los
PUENTE/GAP declarados).

**Lo que el teorema dice y lo que no.** Dice: **donde el objeto índice existe (categoría Pontryagin, $m<\infty$),
κ ES un índice y vale $2m$.** No dice: que el objeto exista incondicionalmente. La condición $m<\infty$ es la
hipótesis, no la conclusión — y verificarla es RH-duro.

### 5.3 Caso (b) confirmado: el símbolo codifica RH. Localización exacta.

Es el **caso (b)** del encargo. Localizo RH en la maquinaria, según la pregunta fina (encargo punto 5):

> **¿RH entra en la FREDHOLMICIDAD (el operador deja de ser Fredholm sin RH) o en la CLASE del símbolo
> (es Fredholm pero su índice topológico no se computa sin RH)?**

---

## 6. Fredholmicidad vs clase: dónde EXACTAMENTE entra RH

### 6.1 [PROPOSICIÓN 156.6 — RH entra primariamente en la FREDHOLMICIDAD]

> *La obstrucción es de Fredholmicidad: bajo $\neg$RH con $m=\infty$ (infinitos ceros off-line, configuración
> consistente con los teoremas de densidad de Ingham y realizada por Davenport–Heilbronn, cf. ERRATA E48.2),
> el símbolo $\phi$ tiene infinitos ceros en la corona, $T_\phi$ **no es Fredholm**, y el "índice" $\kappa$ no es
> un entero (es $\infty$, Doc 107(4)). El objeto de tipo índice **no existe** fuera de la categoría Pontryagin.*

**Argumento.** Un operador de Toeplitz con símbolo que tiene un punto de acumulación de ceros en la corona no es
Fredholm: su imagen no es cerrada (el espectro esencial contiene $0$). La acumulación de ceros off-line bajo
$\neg$RH general (no se sabe que sean aislados; ERRATA E48.1 punto 4 nombra justamente el escenario
$\beta_n\nearrow\beta^*$ no alcanzado) destruye la Fredholmicidad. $\square$

**Consecuencia interpretativa — la más importante del documento.** El muro NO es "el operador existe pero su índice
es difícil de computar". El muro es **"el operador de tipo índice no existe sin RH"**. En el lenguaje de Doc 154:
$\kappa$ es un invariante T5 (índice, lee la inercia del cociente $E/N(A)$ por 154.8) **sólo cuando el objeto está
en la categoría Fredholm/Pontryagin**, y *entrar en esa categoría es la hipótesis $m<\infty$*, que es RH-dura. El
input verificable del mecanismo M5 —"el símbolo es elíptico/Fredholm"— **no se verifica desde los primos**: la
elipticidad del símbolo aritmético ES la finitud de ceros off-line. Esto **rompe la esperanza** de Doc 154 §6 de
que M5 fuera el canal con input verificable: en el caso aritmético, el input de M5 (Fredholmicidad) **colapsa a la
conclusión**, igual que el input de M2 (positividad). **El índice no escapa a la circularidad de la positividad;
la hereda en su requisito de Fredholmicidad.**

### 6.2 [PROPOSICIÓN 156.7 — concedida la Fredholmicidad, RH reaparece en la CLASE]

> *Aun suponiendo $m<\infty$ por fiat (entrando en Pontryagin), de modo que $T_\phi$ es Fredholm, el cómputo del
> índice topológico $\mathrm{winding}(\phi)=2m$ requiere conocer la localización de los ceros off-line: el winding
> es un funcional de la posición de los ceros, no del valor del símbolo en la corona.*

**Argumento.** Por el principio del argumento, $\mathrm{winding}(\phi)=\frac{1}{2\pi i}\oint d\log\phi$ a lo largo
del contorno crítico, que cuenta ceros encerrados. Dos símbolos con el **mismo valor en la corona** (mismo $\phi$
módulo $\mathcal J$ en el sentido de igualdad de la función-símbolo sobre el cociente) pero con ceros en posiciones
distintas dentro de la franja dan **windings distintos**. El valor del símbolo en la corona (lo RH-libre, computable
de los primos) **no determina** el winding; la posición de los ceros sí. $\square$

**Esto es exactamente P43 Thm 4.2 (autonomía del valor vs inercia), ahora dentro del índice.** El **valor** de la
forma de Weil / del símbolo es position-blind (RH-libre, se computa de $\sum_p\Lambda$); la **inercia** (el winding
= partición del índice) NO es position-blind. Doc 154 PROPOSICIÓN 154.8 decía que la inercia "desciende al cociente
$E/N(A)$"; lo que el probe encuentra es que **desciende sólo cuando el cociente está en la categoría Fredholm, y el
descenso lee la posición** — confirmando que el invariante discreto T5 existe pero su evaluación re-encripta RH.

### 6.3 Síntesis de §6: el muro tiene DOS capas dentro del índice

1. **Capa primaria (Fredholmicidad, Prop. 156.6):** sin $m<\infty$ no hay operador de tipo índice. RH entra como
   **condición de existencia del objeto**. Es la capa decisiva: análoga a "el espectro esencial no es positivo",
   mata el objeto, no sólo su cálculo.
2. **Capa secundaria (clase, Prop. 156.7):** concedido $m<\infty$, el cálculo del índice = winding = conteo de la
   posición de ceros = RH. RH entra como **dificultad del cómputo** del invariante de un objeto que sí existe.

**La capa primaria domina:** RH entra **primero** en la Fredholmicidad. La capa secundaria sólo es accesible tras
conceder lo que RH afirma. Por eso el veredicto es **(b)-Fredholmicidad**: *el operador no existe sin RH*; y como
bonus, *aunque existiera, su índice sería tan duro como RH*. Ambas capas son el mismo muro de Doc 154 (no-uniformidad
del ángulo / autonomía valor-vs-inercia) visto en la maquinaria del índice.

---

## 7. Mensaje final

**Veredicto (a/b/c):** **caso (b)** — κ=2m ES de tipo índice (spectral flow = índice de Maslov = winding del símbolo
de Toeplitz, todos iguales bajo Fredholmicidad, Teorema 156.5), pero **el símbolo codifica RH**.

**Dónde está RH en la maquinaria del índice (la respuesta a la pregunta fina):** **primariamente en la
FREDHOLMICIDAD** (Prop. 156.6): el operador de Toeplitz aritmético $T_\phi$ es Fredholm ⟺ su símbolo es invertible
en la corona ⟺ los ceros off-line son finitos ($m<\infty$) ⟺ se está en la categoría Pontryagin donde "$\kappa$"
es un entero. Sin RH (con $m=\infty$, escenario realizado por Davenport–Heilbronn y consistente con Ingham), **el
objeto de tipo índice no existe**. Secundariamente, **en la CLASE** (Prop. 156.7): concedido $m<\infty$, computar el
índice = winding del símbolo = conteo de la posición de los ceros = RH. La capa primaria domina: **RH es condición
de EXISTENCIA del objeto índice, no sólo de su cálculo.**

**Tres hallazgos:**

- **[TEOREMA 156.5] — κ es un índice genuino DENTRO de la categoría Pontryagin: $\kappa=\mathrm{neg.ind}(Q)=
  -\mathrm{Ind}(T_\phi)=\mathrm{winding}(\phi)=\mathrm{sf}\{H_C(t)\}=\mathrm{Mas}(L(0),L(1))=2m$.** Bajo $m<\infty$
  (y los PUENTE/GAP declarados: identificación Gram↔Weil, extensión idélica de Boutet de Monvel), spectral flow,
  índice de Maslov y winding de Toeplitz son el mismo entero, y vale $2m$ por el principio del argumento. El cruce
  valor→inercia de M5 **sí** opera — pero sólo dentro de la categoría cuya hipótesis definitoria es lo que RH afirma.

- **[PROPOSICIÓN 156.6 + 156.7] — el muro tiene DOS capas dentro del índice, y la primaria es la Fredholmicidad.**
  Capa primaria: sin $m<\infty$ el operador no es Fredholm (símbolo con ceros acumulándose en la corona), $\kappa$
  no es entero, el objeto índice no existe — RH como **condición de existencia**. Capa secundaria: concedida la
  Fredholmicidad, el índice = winding = posición de los ceros — RH como **dificultad de cómputo**. La distinción del
  encargo (Fredholmicidad vs clase) se resuelve **a favor de Fredholmicidad como capa dominante**: el muro es "el
  operador no existe sin RH", reforzado por "y aunque existiera, su índice sería RH-duro".

- **[PROPOSICIÓN 156.6, lectura estratégica] — M5 NO escapa a la circularidad de M2; la hereda en el requisito de
  Fredholmicidad.** Doc 154 §6 conjeturaba que el índice (M5) era el único canal con input *verificable-desde-afuera*
  (la elipticidad del símbolo), a diferencia de la positividad (M2), cuyo input *es* la conclusión. El probe lo
  **refuta para el caso aritmético**: la elipticidad/Fredholmicidad del símbolo de Weil **es** la finitud de ceros
  off-line, que NO es verificable desde los primos sin RH. El input de M5 colapsa a la conclusión exactamente como
  el de M2. **La esperanza de Doc 154 §6/§7 (M5 = el único escape con input verificable) queda localizada y
  acotada: el escape sólo existiría con el [GAP de literatura] de §4.5 — un triple espectral aritmético finitamente
  sumable cuyo carácter de Chern (Connes–Moscovici, GAFA 1995) compute $\kappa$ desde datos que NO porten ζ en su
  métrica. Ese triple no existe en la literatura (Connes 1999 y Connes–Consani CCM portan ζ en la coordenada
  inercia, circularidad de Phase 43).** Es el mismo hueco que el [GAP] de Doc 154 §5, confirmado independientemente
  desde la maquinaria del índice y ahora con su forma precisa: *no es que falte computar un índice; es que falta el
  triple espectral cuyo input de sumabilidad sea RH-libre.*

**[GAP global declarado]:** los eslabones que descansan en puente, no probados aquí: (1) la identificación del lugar
de ceros del símbolo de Weil–Toeplitz con los ceros off-line (conjetura de Phase 26 / Doc 134, PUENTE); (2) la
extensión del teorema del índice de Toeplitz de Boutet de Monvel al álgebra idélica $\mathcal W/\mathcal J$ sobre
$C_\mathbb Q$ ([GAP de literatura]); (3) la existencia de un triple espectral aritmético RH-libre con carácter de
Chern $=\kappa$ ([GAP de literatura, central], idéntico a Doc 154 §5). La verificación del test de estrés se hizo
tres veces (modos 1/2/3, §3.2) y dio FALLA-como-inercia / PASA-como-valor en los tres, consistentemente.

*— Doc 156, Phase 49. No se enunció ninguna equivalencia de RH; el objeto fue el MECANISMO del cruce valor→inercia
y dónde vive RH dentro de él: en la Fredholmicidad del símbolo aritmético.*
