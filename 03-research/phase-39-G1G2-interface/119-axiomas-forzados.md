# Doc 119 — Los axiomas forzados: derivación hacia atrás de los requisitos de la cohomología buscada

**Programa:** Hipótesis de Riemann — Phase 39, interfaz G1↔G2
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** roadmap-rh (nodos G1–G4, rutas A/B, especificación S1–S3, Thm. rank-sensitivity, Milestone ms:spec); P44 (dicotomía condicional, Problema L8, anti-Siegel); Doc 110 (axiomas L1–L6 del lector de inercia; Teorema 4.3 de imposibilidad en ℱ; Prop. 4.5 rango finito ⟹ Newton; §5.2 medición de CC contra L1–L6); Doc 118 (rigidez de momentos: Carleman + Hardy; Teorema 5.3; el modelo de "qué rigidez sí cierra"); Doc 108 (valor vs inercia; binariedad por ventana); Doc 105 (Thm. 5.5: divergencia de Mertens del libro mayor; frontera de la clase de Weil); Doc 100 (positividad arquimediana; lema de agotamiento); Doc 99 (formas semilocales QW_λ, localidad automática); Doc 72 (libro mayor de Weil); P43 (cuantificador maestro); P35 (κ(Q)=2m).

**Regla absoluta de esta fase (disciplina de etiquetado):** cada enunciado lleva UNA de tres etiquetas. **[REQUISITO]** = propiedad que la cohomología buscada DEBE tener, con la derivación de por qué es forzada. **[CONJETURA]** = algo que creemos pero no derivamos. **[DATO]** = hecho probado (del lado analítico del programa, con cita interna backward-only, o de literatura real verificable). NUNCA se escribe "probado" sobre nada geométrico nuevo. Lo no verificado en literatura se marca [NO VERIFICADO]. Sin numéricos.

---

## 0. Resumen ejecutivo

Este documento deriva, **desde la conclusión hacia la construcción** (G4 → G3 → G2 → G1),
la lista mínima de axiomas que una teoría cohomológica $H$ sobre (el cuadrado de)
$\mathrm{Spec}\,\mathbb{Z}$ debe satisfacer para que el roadmap corra. El método es el del
ingeniero inverso: en cada nodo se pregunta *qué falla exactamente sin el axioma*, y la
respuesta se ancla en un teorema ya probado del lado analítico del programa. La lista:

| axioma | una línea |
|---|---|
| **R-SIG** | $H$ lleva una graduación de pesos con signatura entera asociada; sin ella, "finitud" ni siquiera es enunciable (§2.3) |
| **R-FIN** | la parte de peso *impuro* de $H^1$ tiene dimensión finita acotada a priori por datos del sitio, y esa dimensión acota $\kappa(Q)=2m$ (§2.2, §2.5) |
| **R-LEF** | un flujo $F$ sobre $H$ cuya traza distribucional reproduce término a término la fórmula explícita: polo (R-LEF-POLO), primos como órbitas de longitud $\log p$ (R-LEF-PRIMOS), regularización arquimediana (R-LEF-REG) (§3) |
| **R-PESO** | el invariante de peso de cada clase es computable desde $H$, no desde la posición del cero; "pesos $=1/2$" debe SEGUIRSE de una positividad geométrica (§4) |
| **R-NC** | test de no-circularidad en cuatro cláusulas (NC1–NC4): la contribución central del documento; hace falsable cualquier candidata a estructura de pesos (§4.3) |
| **R-TRZ** | las trazas son evaluables contra una clase de tests con margen $\varepsilon$ estricto dentro de la clase de Weil, y la reconstrucción Newton exige R-FIN *antes* (§5) |

**Orden de dependencias derivado (hallazgo principal del método hacia atrás):**
$$\text{R-SIG} \;\prec\; \text{R-FIN} \;\prec\; \text{R-LEF} \;\prec\; \text{R-TRZ},
\qquad \text{con R-PESO/R-NC transversales a R-SIG.}$$
La finitud (G4) **presupone** la estructura de pesos (G2): no se puede enunciar "la parte
impura es finito-dimensional" sin haber definido "impuro". Esto confirma desde el lado
geométrico el orden del roadmap (el muro G2 está *aguas arriba* de la finitud) y explica
por qué treinta y siete fases de "pureza sin finitud" y de "finitud sin pesos" fallaron
ambas.

**Tensiones detectadas (§6.3):** T1 (finitud vs flujo continuo: una traza de matriz finita
es analítica real y no puede tener el soporte singular en $\{\log p^k\}$ — la finitud NO
puede ser de todo $H^1$); T2 (regularización arquimediana vs signatura: las signaturas no
son continuas bajo los límites que la regularización exige); T3 (acceso aritmético vs
no-circularidad: cuanto más explícita la fórmula de trazas, mayor el riesgo de que la
"geometría" sea la fórmula explícita re-empaquetada); T4 (flujo $\mathbb{R}_+^*$ vs
integralidad de pesos: en char $p$ la cuantización de pesos es gratis, aquí es un axioma
extra sin análogo).

---

## 1. Método: derivación hacia atrás

**[DATO]** El roadmap (roadmap-rh, §6–§7) establece la cadena
G1 (cohomología finito-dimensional sobre el cuadrado del sitio) → G2 (estructura de
pesos/signatura) → G3 (Lefschetz = fórmula explícita) → G4 (cota a priori
$\kappa(Q)=2m<\infty$) → Finitud → {Ruta A: dicotomía probada en P44, Thm. 2.2 / Ruta B:
lectura Newton}. La especificación S1–S3 (roadmap, Milestone ms:spec) fija qué debe
entregar la geometría: S1 finitud de una *signatura* (no de una característica de Euler),
S2 acceso aritmético a las trazas, S3 sin deuda de uniformidad.

La derivación hacia atrás invierte la lectura: se parte de lo que G4 debe producir
(un entero $\kappa(Q)=2m$ acotado a priori — [DATO] P35: $\kappa(Q)=2m$ en el espacio
de Pontryagin) y se pregunta, nodo por nodo, qué estructura sobre $H$ es *forzada* —
es decir, qué teorema ya probado del programa muestra que su negación hace fallar el nodo.
El criterio de "forzado" es estricto: un axioma entra como [REQUISITO] solo si existe un
[DATO] (teorema del programa o de literatura) que documenta el modo de falla sin él.
Lo que se cree necesario pero no se deriva queda como [CONJETURA].

**Convención sobre el objeto.** Escribimos $H=\bigoplus_i H^i$ para la teoría buscada
sobre el cuadrado del sitio (el análogo de $H^\bullet(C\times C)$), sin presuponer su
categoría (espacios vectoriales, módulos sobre $\mathbb{R}_{\max}$, espacios de Hilbert
con forma indefinida). Los axiomas se formulan de modo agnóstico a la categoría; cuando
una realización concreta exige más, se dice.

---

## 2. DESDE G4: los requisitos de finitud

### 2.1. Qué debe producir G4

G4 debe entregar: **$\kappa(Q)=2m<\infty$, a priori** — antes de localizar cero alguno,
sin límite finito→pleno (S3). Tres datos del programa fijan el perfil exacto de lo que
"a priori" significa:

**[DATO]** (roadmap, Thm. rank-sensitivity; Doc 110, Prop. 4.5). En rango finito
*conocido a priori* $n$, la inercia $(p,q)$ de una forma hermitiana $Q$ está determinada
por las $n$ trazas de potencias $\mathrm{tr}(Q^j)$, $j=1,\dots,n$ (identidades de Newton
+ Jacobi–Frobenius via formas de Hankel; [Gan59, Vol. 2, Cap. X]). En rango infinito las
trazas no determinan la signatura: el número de autovalores negativos no es función
continua de las trazas.

**[DATO]** (Doc 110, Teorema 4.3). En la clase ℱ de funcionales cuadráticos aritméticos
con compresiones test-accesibles, los axiomas (L2 autonomía del valor) + (L3 detección de
inercia) + (L4 estabilidad sin peaje RH) son inconsistentes: todo índice sub-resolución es
0 incondicionalmente (no detecta), y todo índice de resolución o es RH-de-peaje o usa las
posiciones de los ceros. *Estatus declarado allí: teorema para las realizaciones del
programa, esquema para la clase axiomática.*

**[DATO]** (P44, §3; roadmap, Obs. anti-Siegel). No hay mecanismo de repulsión tipo
Siegel para cuádruplos off-críticos: los costes de dos cuádruplos se *suman* en todo
funcional de conteo del programa (excluir $m=2$ es más difícil que excluir $m=1$), y el
presupuesto local arquimediano crece como $\log\gamma$. La finitud no vendrá de análisis.

### 2.2. R-FIN-1, versión ingenua, y por qué es insuficiente tal cual

**[REQUISITO] R-FIN-1 (forma cruda).** $H$ debe asignar a la "superficie" (el cuadrado
del sitio) un objeto cuya dimensión/característica acote $\kappa(Q)$:
$$\kappa(Q) \;\leq\; C\cdot\dim(\text{algo de } H), \qquad C \text{ absoluto},$$
con el "algo" computable funtorialmente del sitio, sin input de posiciones de ceros.

*Derivación de por qué es forzado:* sin una cota de rango a priori, la Prop. 4.5 del
Doc 110 no se aplica y el Teorema 4.3 del Doc 110 sí: cualquier intento de leer
$\kappa(Q)$ desde funcionales cuadráticos aritméticos en rango infinito cae en la
dicotomía sub-resolución/resolución. **[DATO]** (Doc 110, Obs. 5.3) la Forma B del
programa fue exactamente "el método de Deligne menos la finitud" y murió por eso: la
amplificación tensorial $\kappa(\psi^{\otimes k})=\tfrac12(4m)^k$ no gana en rango
infinito porque el denominador de comparación (el mar on×on) crece al mismo ritmo;
en Deligne gana porque $\dim H^i$ está clavada.

Pero R-FIN-1 tal cual NO basta:

**[DATO]** (Doc 110, §5.2, fila L6; roadmap, S1). Una característica de Euler — una
*diferencia de dimensiones*, un VALOR — no determina signaturas en rango infinito; el
Riemann–Roch tropical de Connes–Consani ya produce características de Euler enteras
([CC-Scaling 2016/2017], verificado en Docs 99/100) y eso no acerca a $m$ en nada: ningún
invariante del sitio se ha conectado con $\kappa(Q)$. El requisito real es de *signatura*.

**[DATO]** (Doc 108, §7.4, citado vía Doc 110 §4.2). Autonomía del valor ≠ autonomía de
la inercia: el lado aritmético computa el total de la ventana, no la partición en bloques
on/off. La cota que se necesita es de la parte *off* — y "off" es un atributo de peso.

### 2.3. R-SIG: la signatura exige una graduación de pesos — y la finitud es de un graduado

**[REQUISITO] R-SIG.** $H$ lleva una graduación (o al menos una filtración finita)
$$H^i \;=\; \bigoplus_{w} \mathrm{gr}^W_w H^i \qquad \text{(o } W_\bullet H^i \text{ filtración)},$$
estable bajo la dinámica de G3, junto con una estructura adicional que asigne a cada
graduado una **signatura entera** — no solo una dimensión. La finitud de R-FIN es la del
graduado *relevante*, no la de $H$ total (§2.5).

*Derivación de por qué es forzado, con precisión:* el objeto final es $\kappa(Q)$, un
índice negativo — un dato de *inercia*. Una dimensión es un cardinal; una inercia es un
cardinal **con signo**. Para que un invariante de $H$ acote una inercia, $H$ debe poseer
la estructura mínima que produce signos. Hay exactamente tres realizaciones clásicas de
"estructura que produce una signatura", y conviene compararlas porque exigen cosas
distintas:

**(i) Una forma bilineal/hermitiana con involución.** Datos: un emparejamiento
$\langle\cdot,\cdot\rangle: H^i\times H^{2d-i}\to H^{2d}(\cong \text{objeto trivial})$
(dualidad de Poincaré) más una involución (un análogo del operador estrella o de la
conjugación) que lo convierta en forma hermitiana sobre $H^i$. La signatura es la del
par $(H^i,\langle\cdot,\cdot\rangle)$. *Exige:* dualidad de Poincaré en $H$ (clase de
cohomología fundamental de la superficie), no-degeneración, y — para que la signatura sea
estable — dimensión finita del soporte de la parte indefinida. Es la realización más
cercana al lado analítico: **[DATO]** (P35) la forma de Weil $Q$ ya vive en un espacio de
Pontryagin $(K,Q)$ con $\kappa(Q)=2m$; el requisito es que $H$ reproduzca ese par
funtorialmente.

**(ii) Una bigradación de Hodge $(p,q)$ con simetría.** Datos: $H^i\otimes\mathbb{C}
=\bigoplus_{p+q=i}H^{p,q}$ con $\overline{H^{p,q}}=H^{q,p}$. La signatura sale de las
relaciones bilineales de Hodge–Riemann: la forma $\langle x,\Lambda$-primitivo$\rangle$
es definida en cada pieza $(p,q)$ con signo $i^{p-q}(-1)^{\dots}$ explícito. *Exige:*
una teoría de clases de Lefschetz (operador $L$ de corte hiperplano, primitividad —
es decir, una polarización), además de la bigradación. Es la estructura del índice de
Hodge: la positividad viene de la geometría de la polarización. **[DATO]** (literatura)
en el caso de superficies sobre cuerpos finitos, la desigualdad de Castelnuovo–Severi
(índice de Hodge en el grupo de Néron–Severi de $C\times C$) es lo que Weil usó
[Wei48; Mattuck–Tate 1958, Abh. Math. Sem. Univ. Hamburg 22, 295–299; Grothendieck,
*Sur une note de Mattuck–Tate*, J. reine angew. Math. 200 (1958), 208–215].

**(iii) Una acción de Frobenius con valores absolutos.** Datos: un endomorfismo $F$
cuyos autovalores $\alpha$ sobre $H^i$ tienen $|\alpha|$ bien definido (números de Weil);
el "peso" de $\alpha$ es $w=2\log_q|\alpha|$. La signatura/partición sale del espectro:
puro de peso $i$ = todos los $|\alpha|=q^{i/2}$. *Exige:* que los autovalores sean
números algebraicos con valores absolutos independientes del encaje (integralidad +
producto de pesos en tensores), y la finitud de $\dim H^i$ para que el espectro sea
discreto y la partición tenga sentido. **[DATO]** (literatura) ésta es la realización
de Deligne [Del74, *La conjecture de Weil. I*, Publ. Math. IHÉS 43, 273–307; Weil II:
Publ. Math. IHÉS 52 (1980), 137–252]; la consistencia entre cohomologías de Weil
distintas la da [Katz–Messing, Invent. Math. 23 (1974), 73–77].

**Comparación y mínimo común.** Las tres realizaciones comparten un núcleo: *una
descomposición de $H$ estable bajo la dinámica, indexada por un invariante real $w$, tal
que (a) $w$ es aditivo en productos tensoriales, (b) la dualidad de Poincaré aparea $w$
con $2d-w$ (simetría de pesos), y (c) hay un criterio interno — forma, polarización o
valor absoluto — que decide la pertenencia de una clase a su pieza sin input externo.*
Ese núcleo es la **versión mínima de R-SIG**. La versión cómoda es (ii)+(iii)
simultáneas: una bigradación polarizada con Frobenius compatible (la situación de las
conjeturas estándar [Gro69, *Standard conjectures on algebraic cycles*, Bombay 1968;
Ser60, *Analogues kählériens…*, Ann. of Math. 71, 392–394]).

**Sobre qué exige cada una en el sitio aritmético** — donde el "Frobenius" es un flujo
$\mathbb{R}_+^*$ (Doc 110, §5.1): en (iii) los "autovalores" son los del *generador*
del flujo, y el peso natural es $w=2\,\mathrm{Re}(\text{autovalor del generador})$;
nada lo cuantiza a enteros (tensión T4, §6.3). En (i) y (ii) la integralidad del peso
viene de la graduación misma, no de la dinámica: por eso **la versión mínima de R-SIG
para $\mathrm{Spec}\,\mathbb{Z}$ debe tomar la graduación (no el espectro del flujo)
como dato primitivo**, con el flujo actuando *dentro* de cada graduado. Esto es un
[REQUISITO] derivado: si el peso se *definiera* como parte real del espectro del
generador, el peso de la clase asociada a un cero $\rho$ sería $2\beta$ — la posición
del cero — y R-PESO(a) (§4.1) se violaría por circularidad inmediata.

### 2.4. ¿Finitud de $\dim H$ total o de un graduado?

Aquí la derivación hacia atrás produce su corrección más importante a la intuición
del template.

**[DATO]** (clásico; [Tit86, §9.4]) $\zeta$ tiene infinitos ceros no triviales
($N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi e}$). **[DATO]** (literatura) en toda
realización espectral conocida de los ceros — la de Connes sobre el espacio de clases
de adeles [Connes, *Trace formula in noncommutative geometry and the zeros of the
Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106] y la versión de Meyer
[Meyer, Duke Math. J. 127 (2005), 519–595] [NO VERIFICADO el dato editorial exacto de
Meyer] — el espacio que porta los ceros es de dimensión infinita.

Consecuencia forzada: **el análogo de $H^1$ para $\mathrm{Spec}\,\mathbb{Z}$ NO puede
ser finito-dimensional.** En el template de cuerpos de funciones, $\dim H^1=2g$ es finito
porque la curva tiene finitos ceros; aquí el "lado de ceros" es infinito. La analogía
"$\dim H^1=2g$" del roadmap debe leerse, con esta precisión, así:

**[REQUISITO] R-FIN (forma definitiva).** Con la graduación de R-SIG en mano:
$$\dim\Bigl(\bigoplus_{w\neq 1}\mathrm{gr}^W_w H^1\Bigr) \;<\;\infty,
\qquad\text{acotada a priori por datos del sitio},$$
y la cota acota $\kappa(Q)$: cada clase impura aporta una dirección negativa
contable. Es decir: **finitud de la parte IMPURA (peso $\neq 1$) de $H^1$, no de $H^1$
total.** La parte pura (peso 1) puede — debe — ser de dimensión infinita: porta los
infinitos ceros críticos.

*Derivación:* (α) la infinitud de ceros hace imposible $\dim H^1<\infty$ (arriba);
(β) lo que $\kappa(Q)=2m$ cuenta es exactamente los cuádruplos off-críticos
([DATO] P35), i.e. las clases que una estructura de pesos marcaría como impuras;
(γ) la maquinaria Newton (Doc 110, Prop. 4.5) solo necesita rango finito del *bloque
indefinido*: la inercia de una forma con parte positiva infinito-dimensional y parte
negativa de rango $\leq N$ conocido se determina con finitas trazas *relativas* —
trazas del bloque comprimido, no del total. La finitud total no solo es imposible:
es innecesaria.

**Observación (consecuencia estructural).** R-FIN, en su forma definitiva, **no es
enunciable sin R-SIG**: "parte impura" presupone "peso". El orden de dependencias es
$$\text{R-SIG} \;\prec\; \text{R-FIN}.$$
Esto es notable porque invierte la pedagogía del template (en char $p$ uno aprende
"primero finitud, después pureza") y a la vez la confirma en su sentido profundo: en
char $p$ la finitud de $\dim H^1$ es enunciable sin pesos *porque la parte pura también
es finita*; sobre $\mathrm{Spec}\,\mathbb{Z}$ ese lujo no existe. El muro G2 (la
estructura de pesos) está aguas arriba de TODO, incluida la propia formulación de la
finitud. El roadmap ya colocaba a G2 antes que G4 en la cadena; esta derivación muestra
que la colocación no es opcional.

**[CONJETURA]** La realización correcta de "parte impura finita" es: el par de Pontryagin
$(K,Q)$ de P35 es la realización analítica de
$(\mathrm{gr}^W H^1, \text{forma de dualidad})$, con los $2m$ vectores negativos de $Q$
correspondiendo a una base de $\bigoplus_{w\neq1}\mathrm{gr}^W_w H^1$. Creemos esto
(es la lectura natural del puente P35 + Phase 26), pero no lo derivamos: nada fuerza
a que la *única* fuente de direcciones negativas sean clases impuras de $H^1$ (podrían
contribuir $H^0/H^2$ anómalos). Queda como conjetura de interfaz.

### 2.5. Versión mínima vs versión cómoda de R-FIN

- **Mínima:** existe un subcociente $V\subset H^1$ de dimensión finita, definido
  funtorialmente (sin posiciones de ceros), tal que (a) toda clase impura cae en $V$, y
  (b) $\dim V$ es computable de datos del sitio. No se exige conocer $\dim V$
  exactamente: basta una cota efectiva $\dim V\leq N_0$ (S3 exige que $N_0$ no provenga
  de un límite finito→pleno).
- **Cómoda:** una sucesión exacta de pesos $0\to W_{<1}H^1\to H^1\to \mathrm{gr}^W_{\geq1}\to0$
  con $W_{\text{impuro}}$ de dimensión finita *calculada* (el análogo de $2g$), más
  semisimplicidad de la acción del flujo sobre el graduado.
- **Prueba de fuego:** una candidata $H$ satisface R-FIN si y solo si produce un entero
  $N_0$ por un cómputo del sitio (grados de divisores tropicales, característica de
  Euler de un haz concreto, etc.) ACOMPAÑADO de un teorema "toda dirección negativa de
  $Q$ proviene de $V$" cuya prueba no mencione ceros. Si el "acompañamiento" falta, se
  tiene una característica de Euler más — el estado actual de CC ([DATO] Doc 110, §5.2).

---

## 3. DESDE G3: los requisitos de la fórmula de trazas

### 3.1. R-LEF: el enunciado global

**[REQUISITO] R-LEF.** Existe una dinámica $F$ sobre $H$ — endomorfismo, correspondencia,
o flujo a un parámetro — tal que una suma alternada de trazas reproduce EXACTAMENTE el
lado aritmético de la fórmula explícita de Weil. En la forma de flujo (la relevante para
el sitio, §3.4), para toda función test $h$ en la clase admisible (§5.1):
$$\sum_{i}(-1)^i\,\mathrm{Tr}\Bigl(\int_0^\infty h(u)\,F_u^*\big|_{H^i}\,d^*u\Bigr)
\;=\; \widehat h(\tfrac{i}{2})+\widehat h(-\tfrac{i}{2})
\;-\;\sum_p\sum_{k\geq1}\frac{\log p}{p^{k/2}}\,h(p^k)
\;-\;(\text{término arquimediano}),$$
con las trazas del lado izquierdo entendidas en sentido distribucional, y el lado derecho
el de la fórmula explícita en la normalización del programa ([DATO] Doc 72, Thm. 4.1:
$T_\lambda=A^{off}_\lambda-\sum_p(\log p/\sqrt p)B_\lambda(\log p)+$ arquim., con el
estatus corregido por Doc 105, §3.3 abajo).

*Derivación de por qué es forzado:* G4 necesita leer $\kappa(Q)$ desde trazas
aritméticamente autónomas (S2). **[DATO]** (roadmap, Thm. rank-sensitivity, "Why this is
the whole point") los datos aritméticos autónomos fijan los VALORES de los funcionales de
la fórmula explícita; si las trazas de $F$ sobre $H$ no coinciden EXACTAMENTE con esos
valores, las trazas de $H$ no son autónomas y el axioma L2 del lector de inercia
(Doc 110, Def. 4.1) falla: el invariante dejaría de ser computable sin ceros. La
exactitud no es estética: una identidad "salvo término de error" reintroduce un límite
finito→pleno y viola S3 ([DATO] roadmap: todo límite uniforme de ese tipo en la categoría
analítica es RH-equivalente; Doc 99, transmutación E4, citado vía Doc 105 §7).

Desglosamos término a término qué parte de $H$ debe producir cada bloque.

### 3.2. R-LEF-POLO: el término del polo y los $H^0/H^2$ triviales

En curvas sobre $\mathbb{F}_q$, la fórmula de Lefschetz da
$\#C(\mathbb{F}_{q^k}) = q^k - \sum\alpha_i^k + 1$: los términos $q^k$ y $1$ vienen de
$H^2$ y $H^0$ (pesos 2 y 0, unidimensionales), y son el análogo exacto del término del
polo $\widehat h(\pm i/2)$ de la fórmula explícita (el polo de $\zeta$ en $s=1$ y el
"polo" en $s=0$ de la completación).

**[REQUISITO] R-LEF-POLO.** $H^0$ y $H^2$ (del objeto-curva; sus análogos en el cuadrado)
son de rango UNO, puros de pesos $0$ y $2$, y el flujo actúa sobre ellos con los
caracteres triviales: trivial en $H^0$, el carácter de escala (módulo) en $H^2$. Su
contribución a la traza debe ser exactamente $\widehat h(-i/2)+\widehat h(i/2)$.

*Derivación:* el lado aritmético de la fórmula explícita contiene esos dos términos
incondicionalmente ([DATO] Weil 1952; Doc 72); si $H^0/H^2$ no los produjeran, la
diferencia tendría que salir de $H^1$, es decir, de los ceros — pero entonces el lado
espectral contendría términos sin cero asociado, y la identificación "clases de
$H^1\leftrightarrow$ ceros" (necesaria para que $\kappa$ cuente cuádruplos, §2.4) se
rompe. *Versión mínima:* dos caracteres distinguidos en la traza, con la normalización
correcta. *Análogo en cuerpos de funciones:* $q^k+1$; allí la unidimensionalidad de
$H^0,H^2$ es un teorema (conexidad + dualidad). *Prueba de fuego:* calcular la traza del
flujo sobre los candidatos a $H^0,H^2$ del sitio y comparar con $\widehat h(\pm i/2)$ —
un cómputo finito, sin ceros. **[DATO]** (Doc 100, §4, vía CC Selecta 27 (2021)): el
término arquimediano + polar de la fórmula de Weil ya tiene realización operatorial
positiva en soporte $(1/2,2)$; es el único bloque donde la candidata CC ya pasó una
prueba de fuego parcial.

### 3.3. R-LEF-PRIMOS: trazas locales y la advertencia de la divergencia

El término de primos es una suma sobre lugares finitos. La estructura local en char $p$
es: por cada punto cerrado $x$, el Frobenius local contribuye $\deg(x)$ cuando
$k\equiv0\ (\mathrm{mod}\deg x)$. La descomposición local de la fórmula explícita es el
análogo: una distribución por lugar ($W_p$ de Weil), y la global es su suma.

**[REQUISITO] R-LEF-PRIMOS.** Para cada primo $p$ existe una estructura local en $H$
(un "Frobenius en $p$": la monodromía local del flujo en la órbita correspondiente, o la
fibra de la correspondencia sobre el punto $p$ del sitio) cuya traza local reproduce la
distribución $W_p$ de Weil: $f\mapsto(\log p)\sum_{k\geq1}p^{-k/2}f(p^k)$ (más el término
de inversión $f(p^{-k})$ según normalización). Y — la parte no negociable — **la suma
global de trazas locales debe converger en el mismo sentido regularizado en que la
fórmula explícita converge, no término a término en valor absoluto.**

**[DATO]** (Doc 105, Teorema 5.5 + Obs. 5.6). En la normalización ingenua del programa
(función test $h_{\lambda_0}=W_{\lambda_0}w$, exactamente en la frontera de la clase de
Weil: analítica solo en $|\mathrm{Im}\,s|<1/2$, decaimiento de Fourier exactamente
$e^{-r/2}$), la suma de primos **diverge marginalmente** como
$\tfrac{5\sqrt2}{8}\log X$ (tipo Mertens): la descomposición
$T_\lambda=A^{off}_\lambda-\sum_p(\log p/\sqrt p)B_\lambda(\log p)$ del Doc 72 es
*estrictamente formal* y requiere el apareamiento con el bloque arquimediano divergente
ANTES de sumar. **[DATO]** (Doc 99, Lema 5.1, citado vía Doc 105): la cola prima
$\sum_{p\leq\lambda}\log p/\sqrt p\gtrsim\sqrt\lambda$ para la función carpa — mismo
fenómeno, otra test.

**[REQUISITO] R-LEF-REG (regularización arquimediana).** El término arquimediano de la
traza no es un sumando más: es el **contrapeso regularizador** del bloque de primos. La
teoría $H$ debe realizar el lugar arquimediano como una contribución local del mismo tipo
que las $p$-ádicas (la órbita "de longitud infinitesimal" / el punto en el infinito del
sitio), con la identidad de traza válida solo para el apareamiento conjunto. *Versión
mínima:* la identidad R-LEF se enuncia para la suma total regularizada (valor principal
de Weil en el lugar arquimediano, [DATO] Weil 1952; Doc 100 §5: la aditividad por lugares
del lado geométrico es incondicional). *Versión cómoda:* cada lugar produce una
distribución local bien definida y la suma converge en la topología de la clase de tests
de §5.1 con margen $\varepsilon$. *Qué falla sin él:* [DATO] Doc 105 — los "incrementos
por primo" no son incrementos de ninguna cantidad convergente; cualquier lectura
término a término (monotonía, signos por paso) es ilegítima (el test de signo de la
Forma A falló exactamente así).

*Análogo en cuerpos de funciones:* NO HAY análogo de esta dificultad — la suma sobre
puntos cerrados de grado acotado es finita para cada $k$. La regularización arquimediana
es un requisito genuinamente nuevo de $\mathrm{Spec}\,\mathbb{Z}$, y alimenta la tensión
T2 (§6.3).

### 3.4. R-LEF-FLUJO: ¿endomorfismo o semigrupo? Qué cambia con el flujo continuo

En char $p$, $F$ es un endomorfismo genuino y la variable de Lefschetz es $k\in\mathbb{N}$
(iteradas). En el sitio aritmético/de escala, **[DATO]** (Doc 110, §5.1; CC 2014/2016,
verificado allí) el "Frobenius" es el flujo de escala: una acción de
$\mathbb{R}_+^*$, no de $\mathbb{Z}$. La derivación de qué cambia:

1. **La suma sobre $k$ se vuelve integral sobre el tiempo.** En lugar de
   $\sum_k h_k\,\mathrm{tr}(F^k)$ se evalúa
   $\mathrm{Tr}\bigl(\int h(u)F_u\,d^*u\bigr)$ contra tests $h$ sobre el grupo
   $\mathbb{R}_+^*$: la fórmula de trazas es una identidad de distribuciones sobre el
   tiempo, no una sucesión de números. Consecuencia para la Ruta B: "finitas trazas"
   significa "trazas contra finitas tests" (§5.2).

2. **Los puntos fijos se vuelven órbitas periódicas de longitud $\log p$.** El conteo de
   puntos fijos de $F^k$ se reemplaza por la suma sobre órbitas periódicas del flujo, cada
   primo $p$ aportando la órbita de período $\log p$ (y sus múltiplos $k\log p$), con la
   contribución pesada por $1/|1-p^{k}|$-tipo (el determinante transverso). **[DATO]**
   (literatura) ésta es exactamente la traza distribucional de Guillemin para flujos
   [V. Guillemin, *Lectures on the spectral theory of elliptic operators*, Duke Math. J.
   44 (1977), 485–517], y su instancia aritmética es el teorema de Connes: la traza
   distribucional del flujo de escala sobre el espacio de clases de adeles reproduce el
   lado aritmético de la fórmula explícita de Weil, con las órbitas periódicas de longitud
   $\log p$ [Connes, Selecta Math. (N.S.) 5 (1999), 29–106]. El programa de Deninger
   formula el mismo desideratum en lenguaje de sistemas dinámicos foliados [Deninger,
   *Some analogies between number theory and dynamical systems on foliated spaces*,
   Doc. Math., Extra Vol. ICM I (1998), 163–186].

3. **El lado espectral cambia de "autovalores de $F$" a "espectro del generador".** Para
   un endomorfismo, los ceros aparecen como autovalores $\alpha$ con $|\alpha|=q^{1/2}$;
   para un flujo, aparecen como autovalores $\rho$ del generador infinitesimal
   (el lado espectral es $\sum_\rho \widehat h(\rho)$ en la recta/banda crítica). La
   condición de pureza "$|\alpha|=q^{w/2}$" se traduce en
   "$\mathrm{Re}(\rho)=w/2$" — que es literalmente la posición del cero. **Consecuencia
   forzada (alimenta R-PESO):** con flujo continuo, la pureza NO puede definirse
   espectralmente sin circularidad; debe definirse por la graduación (§2.3) y luego
   DEMOSTRARSE que el espectro del generador en $\mathrm{gr}^W_w$ tiene parte real $w/2$.
   En char $p$ ambas definiciones coinciden trivialmente; aquí separarlas es obligatorio.

4. **No hay potencias tensoriales del tiempo.** El truco de Deligne usa $F$ actuando en
   potencias tensoriales con pesos multiplicativos ($\alpha^{\otimes k}$, peso $kw$). Para
   un flujo, el análogo existe (el flujo producto sobre $H^{\otimes k}$) y los pesos de
   R-SIG deben ser aditivos bajo $\otimes$ (núcleo común de §2.3, cláusula (a)) para que
   la amplificación tenga sentido. **[DATO]** (Doc 106, identidad tensorial, citado vía
   Doc 110 Obs. 5.3): el programa ya verificó que la amplificación tensorial es
   *formalmente* transplantable; lo que faltó fue la finitud — coherente con el orden
   R-SIG ≺ R-FIN ≺ amplificación.

**[REQUISITO] R-LEF-FLUJO (síntesis).** Basta un flujo (semigrupo continuo); no se exige
un endomorfismo discreto. Pero entonces la teoría debe incluir: (a) traza distribucional
tipo Guillemin como *definición* del lado de trazas; (b) la graduación de pesos como dato
independiente del espectro del generador; (c) compatibilidad tensorial de pesos. *Versión
cómoda:* un endomorfismo discreto auxiliar (un "Frobenius entero" — p.ej. la acción de
cada $p\in\mathbb{N}^\times$ por separado, que en el sitio aritmético existe: el monoide
$\mathbb{N}^{\times}$ actúa; [DATO] CC 2014, verificado en Doc 110 §5.1) cuyas iteradas
discretas refinen el flujo. *Prueba de fuego:* la identidad de traza debe ser un teorema
para la candidata $H$ con AMBOS lados computados independientemente — el izquierdo desde
la geometría de $H$, el derecho desde Weil — y no una definición del lado izquierdo como
"lo que dé el derecho" (si es definición, G3 es vacuo y toda la carga pasa a G2 sin
ganancia).

---

## 4. DESDE G2: el requisito central R-PESO y el test de no-circularidad

### 4.1. R-PESO(a): el invariante debe computarse desde $H$, no desde $\rho$

**[REQUISITO] R-PESO(a).** La estructura de pesos asigna a cada clase
$c_\rho\in H^1$ (la clase asociada a un cero $\rho$ vía R-LEF) un invariante
$w(c_\rho)\in\mathbb{Z}$ (o $\tfrac12\mathbb{Z}$, según normalización) **computable desde
la estructura interna de $H$** — pertenencia a un graduado, signo bajo la forma de
dualidad, grado de una clase algebraica que la corta — y NO desde la posición de $\rho$.

*Derivación de por qué es forzado:* si $w(c_\rho)$ se definiera como $2\,\mathrm{Re}(\rho)$
(la única definición disponible sin estructura nueva), entonces "todos los pesos son 1"
sería *literalmente* RH, re-enunciada: cero contenido nuevo. **[DATO]** (Doc 108, §7.4,
vía Doc 110): la partición on/off no es test-accesible — todo funcional cuadrático
aritmético que la compute usa posiciones. **[DATO]** (Doc 110, Teorema 4.3(b)): en
régimen de resolución, o el invariante es RH-de-peaje o usa posiciones. R-PESO(a) es
exactamente la exigencia de salir de la clase ℱ: el invariante debe vivir en una
categoría donde la pertenencia a un graduado sea decidible por la geometría
(funtorialidad, clases algebraicas, formas de intersección), que es lo que ℱ no tiene.

### 4.2. R-PESO(b): "pesos = 1/2" debe seguirse de una positividad geométrica

**[REQUISITO] R-PESO(b).** La afirmación de pureza — toda clase de $H^1$ asociada a un
cero tiene peso 1 (equivalentemente, espectro del generador con parte real $1/2$;
normalización: peso $w$ ⟺ parte real $w/2$) — debe ser un TEOREMA cuya prueba use una
propiedad geométrica de $H$, de uno de los dos tipos con precedente:

- **(b-i) Positividad de una forma de intersección (vía Hodge index / Castelnuovo).**
  Una desigualdad sobre clases en el cuadrado — para toda correspondencia
  $Z\subset X\times X$, una cota tipo $\sigma(Z\cdot Z')\leq$ términos de grados — de la
  que la cota de pesos se sigue por el argumento de Weil aplicado a la correspondencia
  gráfica del flujo. **[DATO]** (literatura) Weil 1948 [Wei48]; la forma moderna:
  positividad de Castelnuovo en $\mathrm{NS}(C\times C)$.
- **(b-ii) Pureza por amplificación tensorial (vía Deligne/Rankin).** Una cota burda
  unilateral en potencias tensoriales pares + finitud uniforme del rango ⟹ cota fina al
  extraer raíces $2k$-ésimas. **[DATO]** (Del74). **[DATO]** (Doc 110, Obs. 5.3): el
  mecanismo requiere R-FIN como insumo previo — denominador clavado — y el programa ya
  comprobó en carne propia (Forma B) que sin R-FIN se invierte el resultado.

*Derivación de por qué "insertarla a mano" está prohibido:* si la pureza se postula como
axioma de $H$ (en vez de teorema), entonces la cadena G1→G4 prueba "RH suponiendo una
estructura cuya existencia implica RH": el contenido se evapora. La distinción
teorema/axioma aquí es exactamente la distinción entre las conjeturas estándar (que en
char $p$ siguen abiertas pero la pureza se probó por otra vía, (b-ii)) y la pureza misma.
**[DATO]** (P43, cuantificador maestro, citado vía P44 §1 y Doc 110 §1): toda propiedad
verificable sin posiciones de ceros que implique RH debe provenir de una estructura
EXTERNA a $\zeta$; el inventario completo de propiedades internas (analíticas,
espectrales, combinatorias) está catalogado y ninguna cruza.

### 4.3. R-NC: el test de no-circularidad (la contribución central de este documento)

Lo anterior se destila en un test operativo. Cualquier propuesta futura de estructura de
pesos $(H,W,F,\langle\cdot,\cdot\rangle)$ para el sitio debe someterse a las cuatro
cláusulas; fallar una cualquiera la descalifica como cruce del muro (puede seguir siendo
matemática valiosa — pero no es G2).

**[REQUISITO] R-NC (test de no-circularidad).** Sea $P$ la propiedad geométrica de la
que se pretende deducir la pureza (la positividad de (b-i), o la cota burda + finitud de
(b-ii)). El test:

> **NC1 (externalidad de la definición).** La definición de $W$ y de $P$ no menciona
> $\zeta$, sus ceros, ni ninguna función/medida/operador cuyo espectro o soporte singular
> codifique las posiciones de los ceros. Se permite mencionar primos, adeles, el sitio y
> sus haces. *Discriminador concreto:* sustituyase, en la definición, la fórmula
> explícita por la de una $L$-función arbitraria del mismo tipo (o por la de los
> contraejemplos sin producto de Euler de P44 §2.3 — [DATO] Doc 111, Prop. 2.2: toda
> $m$ finito es realizable en la clase de orden 1 con ecuación funcional). Si la
> definición de $W$ no sobrevive a la sustitución (no se deja formular), es interna a
> $\zeta$: FALLA.
>
> **NC2 (sobregeneración).** $P$ se demuestra para una clase de objetos del sitio
> ESTRICTAMENTE mayor que la que codifica $\zeta$ — todas las correspondencias, todos los
> divisores, todos los haces de una categoría — por un método uniforme (deformación,
> especialización, inducción geométrica). *Modelo:* Castelnuovo vale para TODO divisor de
> $C\times C$, no solo para la gráfica de Frobenius; la desigualdad es un teorema de
> superficies que ignora qué curva es. Si $P$ solo es verificable para el objeto
> específico que codifica $\zeta$ (la correspondencia gráfica del flujo), entonces
> $P$ es un enunciado sobre $\zeta$ con disfraz: FALLA.
>
> **NC3 (no-reducción a positividades RH-equivalentes catalogadas).** La verificación de
> $P$ en cualquier truncamiento/degeneración no debe ser lógicamente equivalente a un
> ítem del catálogo de positividades RH-equivalentes del programa: positividad de Weil
> global (MW-1), su uniformización semilocal $\lim\mu_\lambda\geq0$ (MW-6; [DATO]
> Doc 99 §2.2 vía Doc 110 §3), constancia de $\Delta_n$ para todo $n$ ([DATO] Doc 118,
> Thm. 5.6 — RH-equivalente exacto), $T_\lambda=0\ \forall\lambda$, cota uniforme de
> índice por ventana ([DATO] Doc 108, Prop. 2.5 vía Doc 110 Thm. 4.3(b)). *Operativa:*
> el proponente debe exhibir la cadena $P\Rightarrow$ pureza y verificar que ningún
> eslabón intermedio figura en NO-GO-LIST (MW-1…MW-7) ni es interderivable con uno que
> figure por las equivalencias ya probadas del programa. Si $P$, restringida al objeto
> que codifica $\zeta$, ES una de esas positividades, no se cruzó el muro: se lo
> renombró. FALLA.
>
> **NC4 (test de los dos mundos).** En el mundo $\neg$RH (con un cuádruplo off-crítico
> hipotético), la propiedad $P$ debe ser FALSA por una razón computable desde $H$ sin
> localizar el cuádruplo: la clase impura debe producir una violación de $P$ visible en
> la estructura (un vector de norma negativa donde $P$ exige positividad, una clase de
> intersección prohibida), de modo que $P\Rightarrow$ pureza sea una implicación con
> contenido en ambos mundos. Si para decidir si $P$ falla en el mundo $\neg$RH hay que
> saber DÓNDE está el cero (la situación de [DATO] Doc 108: binariedad inaccesible),
> entonces $P$ no individuó nada: FALLA.

**Estado de la candidata existente contra R-NC.** La única estructura parcial disponible
(positividades arquimediana y semilocales de CC 2021–2024, [DATO] verificado en Doc 100):
pasa NC1 (la construcción es funtorial desde adeles/sitio), pasa parcialmente NC2 (la
positividad arquimediana vale para toda test de soporte en $(1/2,2)$ — sobregenera), y
FALLA hoy NC3 en el paso global: la uniformización en $\lambda$ de sus positividades
semilocales es MW-6 ([DATO] Doc 100, Obstáculo O_SL; Doc 110 §5.2 fila L4). Esto no
refuta el programa CC: mide exactamente cuánto falta y dónde — que es para lo que sirve
el test.

**Observación (por qué R-NC es falsable y no retórico).** Cada cláusula es una
verificación sintáctica o una reducción a catálogo finito: NC1 es una inspección de la
definición; NC2 exige exhibir la clase de objetos y el método uniforme; NC3 es un chequeo
contra una lista cerrada (NO-GO-LIST + los RH-equivalentes probados, todos con cita);
NC4 exige un certificado estructural de violación en el mundo adversarial. Una propuesta
puede PASAR el test y aun así fracasar (el test es necesario, no suficiente — no
garantiza que $P$ sea demostrable); lo que el test impide es declarar victoria con una
reformulación. **[DATO]** (P43 vía P44): el cuantificador maestro garantiza que algo así
era necesario: toda propiedad interna a $\zeta$ que implique pesos $=1/2$ es
RH-equivalente o más fuerte; la externalidad (NC1–NC2) es el único espacio lógico
restante.

**[CONJETURA]** El test R-NC es además *suficiente* en el sentido débil siguiente: una
estructura $(H,W,F)$ que pase NC1–NC4 y satisfaga R-SIG+R-FIN+R-LEF no puede ser una
reformulación de RH (su consistencia relativa no implica RH por sí sola). No lo
derivamos: la frontera exacta entre "estructura externa cuya existencia implica RH" y
"reformulación" es sutil (la existencia de CUALQUIER cohomología de Weil con pureza
implica RH — el punto es que la *construcción* aporte un mecanismo de prueba, como la
geometría de $C\times C$ lo aportó). Declaramos la zona gris en vez de taparla.

---

## 5. DESDE la Ruta B: requisitos de acceso aritmético a las trazas

### 5.1. R-TRZ-1: la clase de tests mínima

La Ruta B (roadmap, §7) necesita EVALUAR las trazas. La fórmula explícita las da — pero
solo contra tests admisibles, y el programa ya pagó por aprender dónde está el borde:

**[DATO]** (Weil 1952; normalización del programa en Doc 72/Doc 100). La fórmula
explícita vale para tests $h$ pares con transformada analítica en una banda
$|\mathrm{Im}\,s|\leq 1/2+\varepsilon$ y decaimiento adecuado; el lado de primos converge
absolutamente cuando $\widehat h(r)\ll e^{-(1/2+\varepsilon)|r|}$.

**[DATO]** (Doc 105, Thm. 5.5 + Obs. 5.6). La test natural del marco CCM
($W_{\lambda_0}w$) está en la FRONTERA exacta ($\varepsilon=0$: polos del peso $w$ en
$\pm i/2$, decaimiento $e^{-r/2}$ justo) y su serie de primos diverge como Mertens. La
lección, ya pagada: trabajar en la frontera de la clase destruye la lectura por términos.

**[REQUISITO] R-TRZ-1.** La identidad de trazas R-LEF debe ser válida — con ambos lados
absolutamente convergentes o canónicamente regularizados — sobre una clase de tests
$\mathcal{T}$ que satisfaga: (a) margen estricto: $\mathcal{T}\subset\{\,h:\widehat h(r)
\ll e^{-(1/2+\varepsilon)|r|}\ \text{para algún }\varepsilon>0\,\}$ (interior de la clase
de Weil, no su frontera); (b) riqueza suficiente para separar momentos: $\mathcal{T}$
contiene una familia numerable $\{h_n\}$ cuyos lados espectrales generan (en el sentido
del Lema 5.2 del Doc 118: triangularidad sobre los polinomios pares, o un sustituto
denso). *Derivación de (a):* sin margen, [DATO] Doc 105 — divergencia, lectura por
términos ilegítima. *Derivación de (b):* es la condición bajo la cual la maquinaria de
rigidez que SÍ cerró ([DATO] Doc 118, Teorema 5.3: la única medida positiva con
$\int\mathcal{P}_n^2\,d\nu$ constante es $c\,m_\infty$, por Carleman) tiene tracción:
la rigidez de momentos necesita que la familia de funcionales anulados genere todos los
polinomios pares — el gap G-118.1 (bloques de ordenadas coincidentes) muestra qué pasa
cuando faltan dimensiones: la rigidez no se aplica. La clase mínima es, pues, *numerable,
generadora y con margen*; la clase cómoda es un espacio tipo Schwartz de la banda
$|\mathrm{Im}\,s|\leq 1$ cerrado bajo los cómputos del programa.

### 5.2. R-TRZ-2: el orden de dependencias — la finitud va ANTES

**[REQUISITO] R-TRZ-2.** La reconstrucción Newton de la Ruta B presupone R-FIN:
el dato de entrada del mecanismo ([DATO] Doc 110, Prop. 4.5; roadmap Thm.
rank-sensitivity) es "$Q$ tiene rango (del bloque indefinido) $\leq N_0$ CONOCIDO".
Las trazas solas, sin la cota de rango, no determinan nada: **[DATO]** (roadmap, prueba
del Thm. rank-sensitivity) en rango infinito las trazas de un operador autoadjunto no
determinan su medida espectral salvo determinación de momentos, y nunca determinan el
número de autovalores negativos de forma estable. El orden lógico es por tanto
inamovible:
$$\underbrace{\text{R-SIG}}_{\text{definir "impuro"}}
\;\prec\;\underbrace{\text{R-FIN}}_{\text{cota } N_0}
\;\prec\;\underbrace{\text{R-LEF + R-TRZ-1}}_{\text{evaluar } \mathrm{tr}_1,\dots,\mathrm{tr}_{N_0}}
\;\prec\;\underbrace{\text{Newton/Hankel}}_{\text{leer } \kappa(Q)=2m}
\;\prec\;\text{Ruta B: } m=0.$$
Además, en forma de flujo (R-LEF-FLUJO), "las $N_0$ trazas" son trazas contra $N_0$
tests concretas de $\mathcal{T}$ del bloque comprimido: la Ruta B exige que la
compresión al bloque impuro sea ella misma funtorial (otra cara de R-PESO(a): si
comprimir requiere posiciones, Newton recibe trazas que no puede tener).

**Nota sobre la fuerza relativa.** La Ruta B requiere un G3 más fuerte que la Ruta A
([DATO] roadmap, §7 Route B: "potentially stronger than what G3 needs for Route A"):
para la Ruta A basta que R-LEF produzca la cota $m<\infty$; para la B hace falta evaluar
trazas del bloque con precisión suficiente para distinguir $N_0$ enteros. La versión
mínima del paquete R-TRZ es por tanto la de la Ruta A (existencia + cota), y la cómoda
la de la B (evaluación efectiva). Ambas comparten R-TRZ-1/R-TRZ-2.

### 5.3. El modelo de rigidez que sí cierra, como calibre

**[DATO]** (Doc 118, Teorema 5.6). El criterio reparado del programa — RH ⟺
$\int\kappa_n\,d\nu=0\ \forall n$ — se probó por rigidez de momentos: Carleman
(determinación, $\sum 1/a_n^\infty=\infty$ exacto) + completitud triangular de
$\{\mathcal{P}_n^2\}$ + Hardy. Su lección para R-TRZ, en una línea: **lo que convirtió
una familia numerable de identidades en un teorema fue una RIGIDEZ de unicidad
(determinación de momentos), no una positividad.** El análogo cohomológico: las trazas
$\{\mathrm{tr}(h_n)\}$ determinarán el bloque impuro si el problema de momentos asociado
al bloque es determinado — automático en rango finito (R-FIN), que es otra forma de ver
por qué R-FIN precede. Y la advertencia simétrica ([DATO] Doc 118, §6.2.3 y §9): sin
finitud, ninguna subfamilia finita de identidades basta — el cuantificador universal en
$n$ es irreductible; con finitud, $N_0$ identidades bastan. La frontera
finito/infinito-numerable de Doc 118 es exactamente la frontera G4/no-G4.

---

## 6. SÍNTESIS

### 6.1. La tabla de axiomas

| axioma | versión mínima | qué falla sin él [DATO] | análogo en cuerpos de funciones | prueba de fuego |
|---|---|---|---|---|
| **R-SIG** | descomposición $W$-graduada estable bajo $F$, pesos aditivos en $\otimes$, dualidad $w\leftrightarrow 2d-w$, criterio interno de pertenencia | sin signatura, solo valores: característica de Euler no determina inercia [Doc 110 Thm. 4.3, §5.2 L6; roadmap S1] | pesos de Frobenius: $|\alpha|=q^{w/2}$, automático del endomorfismo | exhibir el criterio interno y verificar que NO es "Re del espectro del generador" (si lo es, circularidad: §2.3) |
| **R-FIN** | $\dim\bigl(\text{parte impura de }H^1\bigr)\leq N_0$ con $N_0$ de un cómputo del sitio; acota $\kappa(Q)$ | Newton no aplica; amplificación tensorial se invierte (Forma B) [Doc 110 Prop. 4.5 + Obs. 5.3; P44 Probl. L8]; sin R-SIG ni siquiera es enunciable (§2.4) | $\dim H^1=2g$ — pero AQUÍ la parte pura es infinita: la finitud es del graduado impuro, no del total | el entero $N_0$ debe salir de un cómputo sin ceros + teorema "toda dirección negativa de $Q$ viene de ahí"; una char. de Euler sola no pasa |
| **R-LEF-POLO** | dos caracteres distinguidos ($H^0,H^2$ de rango 1, pesos 0 y 2) que dan $\widehat h(\pm i/2)$ | el lado espectral contendría términos sin cero asociado: la identificación clases↔ceros se rompe (§3.2) | $q^k+1$ en $\#C(\mathbb{F}_{q^k})$ | cómputo finito: traza del flujo en los candidatos vs $\widehat h(\pm i/2)$ [parcial ya pasado: Doc 100 §4, CC 2021] |
| **R-LEF-PRIMOS** | traza local por primo = distribución $W_p$ de Weil; órbita periódica de longitud $\log p$ | sin estructura local, la suma global es un postulado; término a término no converge [Doc 105 Thm. 5.5] | Frobenius local en cada punto cerrado; suma finita por cada $k$ | computar la traza local en UN primo desde la geometría y comparar con $W_p$ (la Conjetura 100.A es la versión positividad; aquí basta la identidad) |
| **R-LEF-REG** | identidad de trazas para la suma total regularizada (primos + arquimediano apareados antes de sumar) | lecturas por término ilegítimas; el "libro mayor" es serie divergente reordenable [Doc 105 Thm. 5.5, Obs. 5.6; Doc 99 Lema 5.1] | SIN análogo (sumas finitas en char $p$): requisito nuevo de Spec ℤ | exhibir la clase de tests donde ambos lados convergen y verificar margen $\varepsilon>0$ (R-TRZ-1(a)) |
| **R-LEF-FLUJO** | traza distribucional de Guillemin como definición del lado dinámico; graduación independiente del espectro | si el peso se define por el espectro del flujo, peso = posición del cero: circularidad (§3.4.3) | $k\in\mathbb{Z}$ vs $t\in\mathbb{R}_+^*$; allí pureza espectral y graduada coinciden gratis | la identidad debe ser teorema con ambos lados computados por separado, no definición de un lado |
| **R-PESO(a)** | $w(c_\rho)$ computable desde $H$ (graduado/forma/clase algebraica), nunca desde $\rho$ | es la clase ℱ otra vez: o RH-de-peaje o usa posiciones [Doc 110 Thm. 4.3(b); Doc 108 §7.4] | pertenencia a $H^i$ con $i$ fijo: funtorial | aplicar NC1 a la definición de $w$ |
| **R-PESO(b)** | pureza = TEOREMA desde positividad geométrica (Castelnuovo-tipo) o amplificación (Deligne-tipo, exige R-FIN antes) | pureza postulada ⟹ la cadena prueba "RH suponiendo algo que implica RH" [P43 vía P44; Doc 110 Obs. 5.3] | Wei48 (índice de Hodge) / Del74 (Rankin) | el test R-NC completo |
| **R-NC** | NC1 externalidad + NC2 sobregeneración + NC3 no-reducción a catálogo MW + NC4 dos mundos | sin el test, toda propuesta puede ser una reformulación con disfraz; falsa victoria [P43; NO-GO-LIST] | Castelnuovo lo pasa: teorema de superficies, válido para todo divisor, previo a toda zeta | el test ES la prueba de fuego; es sintáctico/por catálogo, ejecutable sobre cualquier propuesta escrita |
| **R-TRZ-1** | clase $\mathcal{T}$ de tests numerable, generadora, con margen $\varepsilon>0$ dentro de la clase de Weil | frontera ⟹ divergencia de Mertens [Doc 105]; sin riqueza generadora ⟹ la rigidez no aplica [Doc 118, gap G-118.1] | cualquier $k$ sirve: no hay clase de tests (la variable es discreta) | verificar decaimiento $e^{-(1/2+\varepsilon)|r|}$ y triangularidad generadora de $\{h_n\}$ |
| **R-TRZ-2** | orden: R-SIG ≺ R-FIN ≺ R-LEF/R-TRZ-1 ≺ Newton ≺ $m=0$; compresión al bloque impuro funtorial | trazas sin cota de rango no determinan signaturas [roadmap Thm. rank; Doc 110 Prop. 4.5 por contraste] | Lefschetz da $\#C(\mathbb{F}_{q^k})$; con $2g$ conocido, finitos $k$ bastan | comprobar que ningún paso del plan de lectura usa una traza antes de tener la cota $N_0$ |

### 6.2. Lo que la tabla dice del estado actual

Contra la candidata existente (programa CC, medido en [DATO] Doc 110 §5.2): R-LEF-POLO
parcialmente verificado (arquimediano, CC 2021); R-LEF-FLUJO con la mitad dinámica hecha
(la traza de Connes 1999 ES la identidad R-LEF en la realización de adeles — pero sobre
un espacio sin R-SIG ni R-FIN); R-SIG, R-FIN, R-PESO: ausentes; R-NC: no aplicable aún
(no hay propuesta de $W$ que someter). El agujero exacto sigue siendo el que Doc 110
nombró (L6 + positividad), ahora con la precisión nueva de §2.4: **lo finito no es
$H^1$ — es su parte impura — y eso hace a R-SIG lógicamente anterior a todo.**

### 6.3. Tensiones entre axiomas (donde una construcción puede ser imposible)

Declararlas es parte de la honestidad: si alguna tensión es una contradicción, la
especificación es vacía y el roadmap muere en G1–G2. No afirmamos que lo sean; afirmamos
que toda propuesta debe resolverlas explícitamente.

**T1 (R-FIN vs R-LEF-FLUJO): la finitud no puede portar la traza.** Derivación: si $A$
es el generador de un flujo sobre un espacio de dimensión finita $N$, entonces
$\mathrm{tr}(e^{uA})=\sum_{i\leq N}e^{u\lambda_i}$ es una función real-analítica de $u$;
pero el lado aritmético de R-LEF tiene soporte singular distribucional en
$\{k\log p\}$ (deltas en las longitudes de órbita — [DATO] Connes 1999; Guillemin 1977).
Una suma finita de exponenciales no tiene soporte singular: **un $H$ finito-dimensional
no puede satisfacer R-LEF.** Resolución forzada (coherente con §2.4): el portador de la
traza ($H^1$ completo, infinito-dimensional, parte pura incluida) y el portador de la
finitud (el graduado impuro) son DISTINTOS. La traza es distribucional sobre el grande;
la signatura es algebraica sobre el chico; R-SIG es el puente. Toda propuesta debe
exhibir los dos espacios y el puente — y la compresión del grande al chico debe ser
funtorial (R-TRZ-2).

**T2 (R-LEF-REG vs R-SIG): las signaturas no sobreviven límites de regularización sin
gap.** La regularización arquimediana define los objetos globales como límites
(apareamiento de dos divergencias, [DATO] Doc 105); pero **[DATO]** (Doc 110, Prop.
3.4(c), vía [Phi96]): el flujo espectral — y con él toda signatura — no es continuo bajo
convergencia de resolventes sin gap espectral uniforme; y **[DATO]** (Doc 108, binariedad,
vía Doc 110 Thm. 4.3(b)): los índices por ventana saltan de 0 a $\asymp m\log T$ sin
valores intermedios. Tensión: la signatura de R-SIG debe definirse ANTES del límite
regularizador (sobre el objeto algebraico/geométrico) y demostrarse compatible con él
— no leerse del límite. Una propuesta que defina su forma de intersección como "límite
regularizado de formas truncadas" recae en S3 (deuda de uniformidad) y debe rechazarse
por la prueba de fuego de R-FIN.

**T3 (R-TRZ vs R-NC): el acceso aritmético coquetea con la circularidad.** Cuanto más
fuerte el G3 (Ruta B: evaluación efectiva de trazas), más cerca está la estructura de ser
"la fórmula explícita con otro nombre" — y NC3 existe precisamente porque el programa
probó que las reformulaciones de positividad de la fórmula explícita son RH-equivalentes
en el umbral ([DATO] NO-GO-LIST MW-1/MW-6; Doc 118 §9: el criterio reparado es
reformulación, barrera de Hadamard intacta). La resolución no es renunciar a R-TRZ sino
repartir: la IDENTIDAD de trazas puede (debe) coincidir con la fórmula explícita
(R-LEF es exactitud); lo que tiene que ser externo es la ESTRUCTURA que produce la cota
de pesos (R-PESO/R-NC). El peligro señalable: una propuesta donde el mismo objeto
cumple ambos roles sin separación verificable. NC2 es el detector.

**T4 (flujo $\mathbb{R}_+^*$ vs integralidad de pesos): la cuantización no es gratis.**
En char $p$, los pesos son enteros porque $q^{\mathbb{Z}}$ es discreto: la dinámica
cuantiza sola. Con flujo continuo no hay cuantización espectral; la integralidad del peso
debe venir de la graduación (R-SIG como dato primitivo, §2.3) — es decir, de la
estructura de la categoría de coeficientes sobre el sitio (rango de haces, grados de
divisores tropicales: los enteros que el sitio SÍ tiene, [DATO] Doc 110 §5.2 fila L1).
Tensión con R-PESO(b): la positividad geométrica debe forzar "el espectro del generador
en $\mathrm{gr}^W_1$ tiene parte real exactamente $1/2$" — un enunciado de rigidez
espectral continua sin precedente en el template (allí es automático). Es la cara
G2 de la diferencia $\mathbb{Z}$ vs $\mathbb{R}$, y el lugar donde la analogía con
cuerpos de funciones es más delgada. **[CONJETURA]** La resolución pasa por la
semisimplicidad + dualidad: si la forma de dualidad de R-SIG es no-degenerada sobre
$\mathrm{gr}^W_1$ y el flujo la preserva, el espectro del generador es simétrico respecto
de $\mathrm{Re}=1/2$ por la ecuación funcional geométrica, y la positividad (R-PESO(b))
excluiría las parejas fuera del eje. Es exactamente el esquema de Weil — pero su
transplante al caso continuo no está derivado aquí: conjetura de interfaz, señalada como
el primer problema concreto de la Phase 39.

### 6.4. Cierre

Ningún enunciado geométrico nuevo se ha probado en este documento. Lo que se ha hecho es
forzar, desde teoremas ya probados del lado analítico (roadmap Thm. rank-sensitivity,
Doc 110 Thm. 4.3 y Prop. 4.5, Doc 105 Thm. 5.5, Doc 118 Thm. 5.6, P35, P44), la forma
exacta del objeto que falta: una teoría $H$ con pesos primero (R-SIG), finitud del bloque
impuro después (R-FIN), traza de flujo exacta y regularizada (R-LEF-*), pureza como
teorema externo (R-PESO) testeable por R-NC, y acceso aritmético ordenado (R-TRZ). Las
cuatro tensiones de §6.3 son los puntos donde la especificación puede resultar
incoherente; resolverlas — o probar que no se resuelven — es trabajo de G1↔G2, no de
este documento. Una falsa victoria es peor que un fracaso: por eso la contribución
central no es ningún axioma sino el test R-NC, que convierte "¿es esto un avance o una
reformulación?" en una pregunta decidible por inspección y catálogo.

---

## Referencias

**Internas (backward-only):** roadmap-rh (S1–S3, Milestone ms:spec, Thm. rank-sensitivity,
nodos G1–G4, Rutas A/B); P44 (Thm. 2.2 dicotomía, Probl. 3.1 = L8, §3 anti-Siegel);
P43 (cuantificador maestro, §4 valor/inercia — citado vía P44 y Doc 110); P35
(κ(Q)=2m); Doc 118 (Lema 2.3 Carleman, Thm. 5.3 rigidez, Thm. 5.6 criterio reparado,
gap G-118.1, §6.2.3, §9); Doc 110 (Def. 4.1 axiomas L1–L6, Thm. 4.3, Prop. 4.5, Cor. 4.6,
Obs. 5.3, §5.2, Prop. 3.4); Doc 108 (§7.4, Prop. 2.5, binariedad — citado vía Doc 110);
Doc 105 (Thm. 5.5 divergencia de Mertens, Obs. 5.6 frontera de la clase de Weil, §7);
Doc 100 (positividad arquimediana §4, aditividad por lugares §5, Obstáculo O_SL,
Conjetura 100.A); Doc 99 (QW_λ, localidad automática, Lema 5.1, E4 — citado vía
Docs 100/105/110); Doc 72 (libro mayor de Weil, Thm. 4.1); Doc 111 (Prop. 2.2 —
citado vía P44); NO-GO-LIST (MW-1…MW-7).

**Literatura (verificable):**
- [Connes99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the
  Riemann zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106.
- [Del74] P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974), 273–307;
  *La conjecture de Weil. II*, Publ. Math. IHÉS 52 (1980), 137–252.
- [Den98] C. Deninger, *Some analogies between number theory and dynamical systems on
  foliated spaces*, Doc. Math., Extra Vol. ICM Berlin I (1998), 163–186.
- [Gan59] F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Cap. X.
- [Gro58] A. Grothendieck, *Sur une note de Mattuck–Tate*, J. reine angew. Math. 200
  (1958), 208–215.
- [Gro69] A. Grothendieck, *Standard conjectures on algebraic cycles*, en Algebraic
  Geometry (Bombay Colloquium 1968), Oxford Univ. Press, 1969, 193–199.
- [Gui77] V. Guillemin, *Lectures on the spectral theory of elliptic operators*, Duke
  Math. J. 44 (1977), 485–517 (traza distribucional de flujos; la fuente que Connes99
  cita para el lado dinámico).
- [KM74] N. Katz, W. Messing, *Some consequences of the Riemann hypothesis for
  varieties over finite fields*, Invent. Math. 23 (1974), 73–77.
- [MT58] A. Mattuck, J. Tate, *On the inequality of Castelnuovo–Severi*, Abh. Math.
  Sem. Univ. Hamburg 22 (1958), 295–299.
- [Mey05] R. Meyer, *On a representation of the idele class group related to primes and
  zeros of L-functions*, Duke Math. J. 127 (2005), 519–595 [NO VERIFICADO el dato
  editorial exacto].
- [Phi96] J. Phillips, *Self-adjoint Fredholm operators and spectral flow*, Canad. Math.
  Bull. 39 (1996), 460–467 (citado vía Doc 110).
- [Ser60] J.-P. Serre, *Analogues kählériens de certaines conjectures de Weil*, Ann. of
  Math. 71 (1960), 392–394.
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed., Oxford,
  1986.
- [Wei48] A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*,
  Hermann, Paris, 1948.
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Comm. Sém. Math. Lund (1952), 252–265.
- Connes–Consani (sitio aritmético/de escala, RR tropical, positividades 2021–2024) y
  Connes–Consani–Moscovici (ZST): citados con los datos verificados en Docs 99/100/110.

*Fin del Doc 119.*
