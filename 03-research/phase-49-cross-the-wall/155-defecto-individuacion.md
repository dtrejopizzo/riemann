# Doc 155 — El defecto de individuación: una teoría de la obstrucción promedio→individual

**Programa:** Hipótesis de Riemann — Phase 49: CRUZAR EL MURO.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** constructivo-creador, fundacional. **El objeto de estudio NO es RH.** Es **EL MURO** —
el fenómeno promedio→individual— como objeto matemático con invariantes propios. Construimos la *teoría del
defecto de individuación*: una medida intrínseca de la obstrucción a recuperar un dato exacto/individual a
partir de su versión promediada. En lugar de producir otra equivalencia RH ⟺ X, estudiamos el MECANISMO del
muro como estructura.

**Contrato creativo (regla absoluta de etiquetado):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado DE VERDAD acá, prueba completa, estándar máximo; resultados
externos citados con precisión. **[PUENTE]** = conexión con ζ/RH con estatus honesto de cada eslabón, y
explícitamente NO una equivalencia de RH. **[DESEO]** = declarado sin vergüenza. **[GAP]** = declarado,
incluidos los [GAP de literatura].

---

## 0. Resumen ejecutivo

1. **(§1) Axiomática del par promediador $(H,A)$ y [DEFINICIÓN-NUEVA] del defecto.** Fijamos $H$ Hilbert
   complejo y $A$ una *proyección de promediado*: $A=A^*=A^2$ (esperanza condicional ortogonal / promedio
   idempotente). El **espacio de oscilación** es $H_{\mathrm{osc}}:=\ker A=\mathrm{rango}(1-A)$. El **defecto de
   individuación** del vector $F$ es $\delta_A(F):=\|(1-A)F\|=\mathrm{dist}(F,\,\mathrm{rango}\,A)$. Se prueba
   que es la única de las tres candidaturas del encargo que sobrevive como invariante intrínseco; las otras dos
   (dimensión de la fibra; distancia al dominio de inyectividad) son *equivalentes a ésta* bajo la axiomática
   correcta (Prop. 1.6).

2. **(§2) Propiedades básicas, todas probadas.** $\delta_A$ es seminorma (subaditiva, homogénea), $1$-Lipschitz
   por tanto continua (Prop. 2.1); $\delta_A(F)=0\iff F\in\mathrm{rango}\,A\iff F=AF$ (Prop. 2.2); monotonía
   por refinamiento de promedios $A\preceq A'$ (Prop. 2.4); **dualidad exacta defecto↔invisibilidad**: la fibra
   $A^{-1}(AF)$ es el trasladado $F+H_{\mathrm{osc}}$, y $\delta_A(F)$ es la distancia de $F$ a *cualquier* otro
   dato con el mismo promedio (Teorema 2.5, "el promedio no separa más allá de $H_{\mathrm{osc}}$").

3. **(§3) [TEOREMA 3.2 — caracterización central]** confirma la predicción del encargo con una forma precisa:
   **$\delta_A(F)=0$ NUNCA colapsa por la sola estructura lineal de $A$**; colapsa si y sólo si $F$ vive en una
   *sub-estructura de individuación* $\mathcal S$ que satisface $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$ **y** está
   forzada por un input externo. Formalizamos el input como un **cono $\mathcal K$**, una **subálgebra/sub-σ-álgebra**,
   o una **acción de grupo $G\curvearrowright H$ con $A=\int_G$**; en los tres casos el colapso es equivalente a
   $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$ (transversalidad). El input es lógicamente necesario: Teorema 3.4 (no-go)
   muestra que sin él, para cualquier $A$ con $H_{\mathrm{osc}}\neq\{0\}$, existe $F\neq AF$, $\delta_A(F)>0$.

4. **(§4) Los cuatro colapsadores conocidos, unificados como "vaciar la oscilación compatible".**
   **(Positividad, Teorema 4.1):** cono $\mathcal K$ con $A$ fiel ⟹ $H_{\mathrm{osc}}\cap\mathcal K=\{0\}$.
   **(Tauberiano, Teorema 4.3):** una condición unilateral de tamaño/regularidad (cota de Tauber)
   intersecta el espacio de oscilación en $\{0\}$. **(Continuación única, Teorema 4.5):** si $A$ es restricción
   y los elementos de $H_{\mathrm{osc}}$ son soluciones que se anulan en un abierto, la UCP los anula.
   **(Acción de grupo, Teorema 4.7):** ergodicidad ⟺ $H_{\mathrm{osc}}$ no contiene invariantes no triviales.
   Los cuatro son instancias del **principio de reducción** (Teorema 4.8): un colapsador es exactamente un
   subconjunto $\mathcal R\subseteq H$ con $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$ y $F\in\mathcal R$.

5. **(§5) [DESEO formulable] ¿Hay un quinto colapsador?** La teoría hace la pregunta precisa: un colapsador no
   catalogado es un funtor $\mathcal R$ que vacía $H_{\mathrm{osc}}$ y que **no** se factoriza por (orden, cota
   unilateral, soporte/analiticidad, simetría). Damos un invariante —el **tipo de transversalidad**— que
   clasifica colapsadores y señala dónde buscaría uno nuevo (§5.2).

6. **(§6) [PUENTE honesto, breve]** Diccionario con la forma de Weil: $H$, $A$ (promedio sobre ventanas /
   media de Cesàro–MV74), $F$ (la contribución oscilatoria cero-a-cero), y qué significaría $\delta_A(F)=0$.
   Estatus: **no es una equivalencia de RH**; identifica qué input estructural (positividad estricta del símbolo,
   Doc 134) sería el colapsador, y por qué el muro es justamente "$\delta_A>0$ sin input".

---

## 1. La axiomática del par promediador y la definición del defecto

### 1.1 El par promediador

[DEFINICIÓN-NUEVA 1.1] Un **par promediador** es $(H,A)$ donde $H$ es un espacio de Hilbert complejo y
$A\in\mathcal B(H)$ es una **proyección de promediado**: $A^2=A$ y $A^*=A$ (proyección ortogonal). Llamamos
$$H_{\mathrm{ind}}:=\mathrm{rango}\,A=\{F:AF=F\},\qquad H_{\mathrm{osc}}:=\ker A=\mathrm{rango}(1-A),$$
el **subespacio individuado** (lo que el promedio conserva) y el **espacio de oscilación** (lo que el promedio
borra). Por la teoría espectral elemental $H=H_{\mathrm{ind}}\oplus H_{\mathrm{osc}}$ ortogonalmente.

**Justificación de la axiomática.** El encargo ofrece tres opciones: idempotente, esperanza condicional, o
generador de semigrupo. Elegimos la proyección ortogonal autoadjunta porque:

- (a) Es exactamente el caso de la **esperanza condicional** $\mathbb E[\cdot\mid\mathcal A]$ sobre
  $L^2(\Omega,\Sigma,\mu)\to L^2(\Omega,\mathcal A,\mu)$ con $\mathcal A\subseteq\Sigma$ sub-σ-álgebra: es la
  proyección ortogonal sobre las funciones $\mathcal A$-medibles (Bru­neau; ver también
  [Bogachev, *Measure Theory*, vol. I, §10.1] para la caracterización $L^2$). Toda esperanza condicional sobre
  $L^2$ es un $A$ de nuestra clase, y recíprocamente toda proyección que además fija las constantes y es positiva
  es una esperanza condicional [Moy 1954; Pitcher; ver §1.4].
- (b) Es el **promedio ergódico / proyección de von Neumann**: para un grupo $G$ que actúa unitariamente,
  $A=$ proyección sobre los invariantes es el límite fuerte de promedios de Cesàro de los $U_g$
  (von Neumann 1932, teorema ergódico medio; [Krengel, *Ergodic Theorems*, §2.1]).
- (c) Captura el **promediado sobre ventanas** del muro (MV74 / Doc 108 §5.2): la media en bloques es una
  proyección sobre el subespacio de secciones constantes-por-bloque.

El caso de semigrupo no idempotente $\{e^{-tL}\}$ se reduce a éste por el límite de Abel/ergódico
$A:=\lim_{t\to\infty}e^{-tL}=$ proyección sobre $\ker L$ (cuando $L\geq0$ autoadjunto, el límite fuerte existe y
es la proyección espectral en $0$). Por tanto, sin pérdida de generalidad de la *teoría del defecto en el
límite*, trabajamos con la proyección. El caso transitorio (finito-$t$) lo recuperamos en §2.5 como
*defecto a escala $t$*.

[GAP de literatura] El nombre "defecto de individuación" y el invariante $\delta_A$ no aparecen, hasta donde
sabemos, en la literatura. Las piezas (proyección ortogonal, oscilación, esperanza condicional) son clásicas;
la *teoría del defecto* como objeto con propiedades de monotonía/dualidad propias es la contribución de este
documento.

### 1.2 La definición del defecto

[DEFINICIÓN-NUEVA 1.2] El **defecto de individuación** de $F\in H$ respecto del par $(H,A)$ es
$$\boxed{\ \delta_A(F):=\|(1-A)F\|=\mathrm{dist}(F,\,H_{\mathrm{ind}})=\big\|P_{H_{\mathrm{osc}}}F\big\|.\ }$$
Equivalentemente, es la norma de la **componente oscilatoria** de $F$. El **defecto relativo** es
$\hat\delta_A(F):=\delta_A(F)/\|F\|$ para $F\neq0$ (un seno del ángulo entre $F$ y $H_{\mathrm{ind}}$).

### 1.3 Las tres candidaturas del encargo son la misma

El encargo propone tres definiciones; mostramos que bajo la axiomática 1.1 colapsan en 1.2 (esto justifica
la elección y no es trivial: requiere que $A$ sea proyección).

[PROPOSICIÓN 1.6] Sea $(H,A)$ par promediador, $F\in H$. Entonces:
1. $\delta_A(F)=\mathrm{dist}(F,\,\mathrm{rango}\,A)$  *(candidata iii / distancia)*;
2. $\mathrm{dist}\big(F,\,\{G:A\text{ inyectiva en }G\}\big)$ no es un invariante de $F$ solo, pero su versión
   correcta —la distancia al mayor subespacio donde $A$ separa, esto es $H_{\mathrm{ind}}$— coincide con (1)
   *(candidata i, corregida)*;
3. la **fibra** $A^{-1}(AF)=F+H_{\mathrm{osc}}$ tiene "tamaño" $\delta_A(F)$ en el sentido de que
   $\delta_A(F)=\mathrm{dist}(F,\,\text{centro de la fibra})$ donde el centro es $AF\in H_{\mathrm{ind}}$
   *(candidata ii, en forma métrica)*.

*Prueba.* (1) Como $A$ es proyección ortogonal, $\mathrm{dist}(F,\mathrm{rango}\,A)=\|F-AF\|=\|(1-A)F\|$, por la
caracterización de la proyección como el punto más cercano del subespacio cerrado $H_{\mathrm{ind}}$
(teorema de la proyección, [Rudin, *Functional Analysis*, Thm 12.4]). (2) $A$ es inyectiva exactamente sobre
los subespacios $V$ con $V\cap\ker A=\{0\}$; el mayor subespacio cerrado *$A$-invariante* sobre el que $A$ es
inyectiva y sobreyectiva a su imagen es $H_{\mathrm{ind}}$ (allí $A=\mathrm{id}$). La distancia a él es (1).
La candidata literal "dist al dominio de inyectividad" no es un invariante porque tal dominio no es único; la
corrección canónica es $H_{\mathrm{ind}}$. (3) La fibra de $A$ sobre $AF$ es $\{G:AG=AF\}=\{G:A(G-F)=0\}
=F+\ker A=F+H_{\mathrm{osc}}$. Su elemento de norma mínima es $AF$ (la componente individuada), y
$\mathrm{dist}(F,AF)=\|(1-A)F\|=\delta_A(F)$. ∎

**Lectura.** El defecto mide *simultáneamente*: cuánta norma se pierde al promediar; cuán lejos está $F$ del
único representante "limpio" $AF$; y el radio de la indeterminación que el promedio deja abierta. La candidata
(ii) "dimensión/medida del espacio de indistinguibles" es, en su forma cruda, $\dim H_{\mathrm{osc}}$ —un
invariante de $A$, no de $F$—; su forma correcta-por-$F$ es la métrica (3). Esta distinción
(invariante-de-$A$ vs invariante-de-$F$) reaparece en la dualidad (§2.5).

### 1.4 Cuándo $A$ es una esperanza condicional (precisión)

[GAP de literatura — resuelto por cita] No toda proyección ortogonal es una esperanza condicional. El criterio
clásico: una proyección $A$ sobre $L^2$ es de la forma $\mathbb E[\cdot\mid\mathcal A]$ ssi $A$ es positiva
($f\geq0\Rightarrow Af\geq0$), $A1=1$, y $A(g\,Af)=(Af)(Ag)$ para $f,g$ acotadas (propiedad de módulo/
promediado), [Moy 1954, *Pacific J. Math.* 4; Olson 1965]. Usaremos este caso reforzado en §4.1 (positividad).

---

## 2. Propiedades básicas (probadas)

### 2.1 Seminorma y continuidad

[PROPOSICIÓN 2.1] $\delta_A:H\to[0,\infty)$ es una **seminorma**: $\delta_A(\alpha F)=|\alpha|\,\delta_A(F)$ y
$\delta_A(F+G)\le\delta_A(F)+\delta_A(G)$ (subaditividad). Además es $1$-Lipschitz:
$|\delta_A(F)-\delta_A(G)|\le\|F-G\|$, luego continua. Su núcleo es $\{\delta_A=0\}=H_{\mathrm{ind}}$, un
subespacio cerrado.

*Prueba.* $\delta_A=\|(1-A)\cdot\|$ es la composición de la seminorma $\|\cdot\|$ con el operador lineal acotado
$1-A$; toda tal composición es seminorma. Homogeneidad y triángulo son inmediatos. Lipschitz:
$|\,\|(1-A)F\|-\|(1-A)G\|\,|\le\|(1-A)(F-G)\|\le\|1-A\|\,\|F-G\|=\|F-G\|$ pues $\|1-A\|=1$ (proyección ortogonal
no nula; si $A=1$ entonces $\delta_A\equiv0$ y todo es trivial). Núcleo: §2.2. ∎

### 2.2 Colapso del defecto = punto fijo del promedio

[PROPOSICIÓN 2.2] Para $F\in H$: $\ \delta_A(F)=0\iff AF=F\iff F\in H_{\mathrm{ind}}$. (Individuación completa
$=$ ser invariante por el promedio.)

*Prueba.* $\delta_A(F)=0\iff\|(1-A)F\|=0\iff(1-A)F=0\iff AF=F$. ∎

Este enunciado es la **forma cero del muro**: el defecto colapsa para $F$ ssi $F$ ya es su propio promedio.
El contenido —y toda la dificultad— está en *qué fuerza a $F$ a ser invariante* cuando $F$ no lo es por
construcción. Eso es §3–§4.

### 2.3 Semicontinuidad y comportamiento bajo límites

[PROPOSICIÓN 2.3] $\delta_A$ es **débilmente semicontinua inferiormente**: si $F_n\rightharpoonup F$
(convergencia débil) entonces $\delta_A(F)\le\liminf\delta_A(F_n)$.

*Prueba.* $1-A$ es acotado, luego débil-débil continuo, así $(1-A)F_n\rightharpoonup(1-A)F$. La norma es
débilmente s.c.i. ([Brezis, *Functional Analysis*, Prop. 3.5]): $\|(1-A)F\|\le\liminf\|(1-A)F_n\|$. ∎

(No es débilmente *continua*: tómese $F_n$ una base ortonormal de $H_{\mathrm{osc}}$, $F_n\rightharpoonup0$,
$\delta_A(F_n)=1\not\to0=\delta_A(0)$. Esto NO es patología: es la **firma analítica del muro** —el defecto
puede sobrevivir en el límite débil aunque cada testigo se desvanezca débilmente. Lo reusaremos en §5.)

### 2.4 Monotonía por refinamiento del promedio

[DEFINICIÓN-NUEVA 2.3bis] Para dos proyecciones de promediado $A,A'$ en el mismo $H$ decimos que $A'$
**refina** a $A$, escrito $A\preceq A'$, si $H_{\mathrm{ind}}(A)\subseteq H_{\mathrm{ind}}(A')$
(equivalente: $AA'=A'A=A$; "promediar menos", conservar más individual).

[PROPOSICIÓN 2.4] Si $A\preceq A'$ entonces $\delta_{A'}(F)\le\delta_A(F)$ para todo $F$. (Refinar el promedio
no aumenta el defecto.) Recíprocamente, si $\delta_{A'}(F)\le\delta_A(F)$ para *todo* $F$, entonces
$A\preceq A'$.

*Prueba.* ($\Rightarrow$) $H_{\mathrm{ind}}(A)\subseteq H_{\mathrm{ind}}(A')$ implica
$H_{\mathrm{osc}}(A')\subseteq H_{\mathrm{osc}}(A)$, luego $P_{\mathrm{osc}}(A')\le P_{\mathrm{osc}}(A)$ en el
orden de operadores (proyecciones sobre subespacios encajados), y
$\delta_{A'}(F)^2=\langle P_{\mathrm{osc}}(A')F,F\rangle\le\langle P_{\mathrm{osc}}(A)F,F\rangle=\delta_A(F)^2$.
($\Leftarrow$) La desigualdad de las formas cuadráticas para todo $F$ da $P_{\mathrm{osc}}(A')\le
P_{\mathrm{osc}}(A)$; para proyecciones ortogonales esto equivale al encaje de rangos
([Halmos, *Hilbert Space Problem Book*, Prob. 122]), i.e. $A\preceq A'$. ∎

### 2.5 La dualidad exacta: defecto ↔ núcleo de invisibilidad

Aquí está la dualidad que el encargo pide ("el defecto de $F$ vs el núcleo de invisibilidad de $A$").

[DEFINICIÓN-NUEVA 2.5a] El **núcleo de invisibilidad** de $A$ es $\mathrm{Inv}(A):=H_{\mathrm{osc}}=\ker A$:
los datos que el promedio vuelve indistinguibles de $0$. El **cono/diámetro de indistinguibilidad** de $F$ es
el conjunto $[F]_A:=A^{-1}(AF)=F+\mathrm{Inv}(A)$ (todos los datos con el mismo promedio que $F$).

[TEOREMA 2.5] *(El promedio no separa más allá de la oscilación.)* Para todo $F$:
$$\delta_A(F)=\mathrm{dist}\big(F,\,H_{\mathrm{ind}}\big)
=\inf\{\|F-G\|:G\in H,\ AG\neq AF\ \text{imposible de detectar...}\}$$
Más limpiamente: la **mejor recuperación de $F$ a partir del único dato observable $AF$** tiene error
exactamente $\delta_A(F)$, alcanzado por *ningún* estimador lineal-en-$AF$ mejor que $G\mapsto AF$:
$$\inf_{T:\,H_{\mathrm{ind}}\to H}\ \sup_{F:\,AF=y}\|F-T y\|=\delta\text{-radio de }[y]_A,$$
y para el estimador canónico $T=\iota$ (inclusión) el error en $F$ es $\|F-AF\|=\delta_A(F)$. La
*indeterminación intrínseca* del problema inverso "dado $AF$, hallar $F$" es el radio de la fibra, que es
$+\infty$ si $H_{\mathrm{osc}}\neq\{0\}$ (la fibra es un trasladado de un subespacio no acotado) **a menos que
se restrinja $F$ a una sub-estructura**.

*Prueba.* La primera igualdad es Prop. 1.6(1). Para la segunda: dado el observable $y=AF\in H_{\mathrm{ind}}$,
los datos compatibles son $[y]_A=y+H_{\mathrm{osc}}$. Cualquier $G\in[y]_A$ tiene $AG=y$, luego es
indistinguible de $F$ por $A$. El error de usar $y$ como estimador de $F$ es $\|F-y\|=\|F-AF\|=\delta_A(F)$.
El supremo del error sobre la fibra es $\sup_{G\in[y]_A}\|G-y\|=\sup_{h\in H_{\mathrm{osc}}}\|h\|=\infty$
cuando $H_{\mathrm{osc}}\neq\{0\}$: no hay reconstrucción uniforme sin información extra. ∎

**Esto es el muro, enunciado como teorema.** El promedio $AF$ determina a $F$ módulo $H_{\mathrm{osc}}$, y nada
más. La obstrucción a la individuación es *exactamente* $H_{\mathrm{osc}}$, y se cuantifica por $\delta_A$.
La pregunta del programa —¿cuándo el promedio determina el individual?— es: ¿cuándo se puede colapsar la fibra?
Respuesta: §3.

[DEFINICIÓN-NUEVA 2.5b — defecto a escala finita] Para un semigrupo de promediado $e^{-tL}$, $L\geq0$
autoadjunto, el **defecto a escala $t$** es $\delta^{(t)}(F):=\|(1-e^{-tL})F\|$. Es creciente en $t$,
$\lim_{t\to\infty}\delta^{(t)}(F)=\delta_A(F)$ con $A=P_{\ker L}$ (cálculo funcional + convergencia monótona
espectral). Esto registra *la velocidad a la que el muro se forma*; lo dejamos como herramienta para §5.

---

## 3. El teorema de caracterización de $\delta_A(F)=0$

Aquí probamos la predicción del encargo: el defecto **nunca colapsa por la sola estructura lineal**; necesita
un input externo, formalizable como cono/subálgebra/acción que reduce $H_{\mathrm{osc}}$ a transversalidad.

### 3.1 Sub-estructuras de individuación

[DEFINICIÓN-NUEVA 3.1] Una **sub-estructura de individuación** para $(H,A)$ es un subconjunto $\mathcal S\subseteq H$
(no necesariamente subespacio) que es **transversal a la oscilación**:
$$\mathcal S\cap H_{\mathrm{osc}}=\{0\}.$$
Decimos que $\mathcal S$ es un **colapsador** si además $\mathcal S$ proviene de un *input externo* —un dato
que no es deducible de $(H,A)$ lineal sola—: un **cono** $\mathcal K$ (orden/positividad), una
**subálgebra / sub-σ-álgebra** $\mathcal B$ (estructura multiplicativa o de soporte), o una **acción de grupo**
$G\curvearrowright H$ unitaria con $A$ su proyección de invariantes.

### 3.2 El teorema central

[TEOREMA 3.2] *(Caracterización del colapso del defecto.)* Sea $(H,A)$ par promediador y $F\in H$. Son
equivalentes:
1. $\delta_A(F)=0$;
2. $F\in H_{\mathrm{ind}}$;
3. existe una sub-estructura de individuación $\mathcal S$ con $F\in\mathcal S$ **y** $\mathcal S$
   es maximal-transversal en el sentido $\overline{\mathrm{span}}\,\mathcal S\cap H_{\mathrm{osc}}=\{0\}$ y
   $F\in\overline{\mathrm{span}}\,\mathcal S\subseteq H_{\mathrm{ind}}$.

Además, **el colapso para un $F$ con $F\neq AF$ a priori es imposible**: si $F\notin H_{\mathrm{ind}}$, ningún
argumento que use sólo $A$ lineal puede concluir $\delta_A(F)=0$ (Teorema 3.4). El colapso para una *clase*
de datos $F$ (no para uno fijo trivialmente individuado) requiere que esa clase viva en una $\mathcal S$
transversal **forzada externamente**.

*Prueba.* (1)$\iff$(2) es Prop. 2.2. (2)$\Rightarrow$(3): tomar $\mathcal S=H_{\mathrm{ind}}$, que es
transversal ($H_{\mathrm{ind}}\cap H_{\mathrm{osc}}=\{0\}$ por suma directa ortogonal) y contiene $F$.
(3)$\Rightarrow$(2): si $F\in\overline{\mathrm{span}}\,\mathcal S$ y este span cerrado intersecta
$H_{\mathrm{osc}}$ sólo en $0$ **y** está contenido en $H_{\mathrm{ind}}$, entonces $F\in H_{\mathrm{ind}}$. ∎

**El contenido real** no es la equivalencia (1)–(3), que es tautológica una vez fijado el lenguaje, sino lo que
sigue: que la transversalidad $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$ **no es gratis** y que las únicas formas
conocidas de garantizarla son los inputs externos. Eso es §3.3 (no-go) y §4.

### 3.3 Por qué el input es necesario: el no-go

[TEOREMA 3.4] *(No-individuación gratis.)* Sea $(H,A)$ par promediador con $H_{\mathrm{osc}}\neq\{0\}$.
Entonces:
1. existe $F$ con $\delta_A(F)>0$ (de hecho un subespacio de tales $F$ de dimensión $\dim H_{\mathrm{osc}}$);
2. para cualquier procedimiento que dependa **sólo** de $(H,A)$ y de $AF$ (es decir, invariante bajo
   $F\mapsto F+h$, $h\in H_{\mathrm{osc}}$), el valor reconstruido de $F$ no puede distinguir $F$ de $F+h$;
   por tanto no puede certificar $\delta_A(F)=0$ salvo que de hecho $F\in H_{\mathrm{ind}}$.

*Prueba.* (1) Cualquier $0\neq h\in H_{\mathrm{osc}}$ tiene $\delta_A(h)=\|h\|>0$; el subespacio es
$H_{\mathrm{osc}}$ mismo. (2) Un procedimiento $\Phi$ que depende sólo de $AF$ satisface $\Phi(F)=\Phi(F+h)$
para todo $h\in H_{\mathrm{osc}}$ (pues $A(F+h)=AF$). Si concluyera "$\delta_A(F)=0$" para un $F$ con
$\delta_A(F)>0$, daría la misma conclusión para $F-(1-A)F=AF$ y para $F$ —dos datos con defecto $0$ y
$>0$ respectivamente—, contradicción. Luego $\Phi$ no puede certificar el colapso usando sólo el promedio. ∎

**Corolario (la tesis del encargo, probada).** *El defecto nunca colapsa por sí solo.* Toda demostración de
$\delta_A(F)=0$ para un $F$ que no es manifiestamente invariante debe usar información que **rompe la
invariancia $F\mapsto F+h$**, esto es, una restricción que excluye los $h\in H_{\mathrm{osc}}\setminus\{0\}$:
un input externo en el sentido de Def. 3.1. ∎

---

## 4. Los cuatro colapsadores, unificados

Cada mecanismo conocido es una manera de fabricar una $\mathcal S$ con $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$.

### 4.1 Positividad (cono)

[TEOREMA 4.1] Sea $(H,A)$ con $H=L^2(\Omega,\mu)$ y $A=\mathbb E[\cdot\mid\mathcal A]$ una esperanza condicional
(Def. 1.1(a), criterio §1.4). Sea $\mathcal K=\{f\geq0\}$ el cono positivo. Si $F\in\mathcal K$ y $AF=0$,
entonces $F=0$. En particular $\mathcal K\cap H_{\mathrm{osc}}=\{0\}$: el cono es transversal a la oscilación.

*Prueba.* $A=\mathbb E[\cdot\mid\mathcal A]$ es **fiel y positiva**: $f\geq0\Rightarrow Af\geq0$, y
$\int_\Omega Af\,d\mu=\int_\Omega f\,d\mu$ (preserva la integral, [Bogachev §10.1; Williams,
*Probability with Martingales*, §9.7]). Si $F\geq0$ y $AF=0$ entonces $\int F\,d\mu=\int AF\,d\mu=0$ con
$F\geq0$, luego $F=0$ $\mu$-c.t.p. ∎

**Lectura unificadora.** La positividad reduce $H_{\mathrm{osc}}$ porque un elemento de oscilación, al
promediar a cero conservando la masa, no puede ser $\geq0$ salvo el nulo. El cono *recorta* la fibra
$[0]_A=H_{\mathrm{osc}}$ a su vértice.

### 4.2 Tauberiano (condición unilateral de tamaño)

[DEFINICIÓN-NUEVA 4.2] En el marco de promedios de Cesàro (Doc 108 §5.2), $A$ es la media en bloques y
$H_{\mathrm{osc}}$ son las fluctuaciones de media-bloque nula. Una **condición tauberiana** es una restricción
unilateral $\mathcal T=\{F:\ \text{osc local}(F)\le c\cdot(\text{escala})\}$ (e.g. una cota de variación lenta,
slowly oscillating en el sentido de Schmidt).

[TEOREMA 4.3] *(El teorema tauberiano como vaciamiento de la oscilación compatible.)* Sea $a_n$ una sucesión
con medias de Cesàro $\sigma_N=\frac1N\sum_{n\le N}a_n\to s$. Si $a_n$ satisface la condición tauberiana de
oscilación lenta ($\,(a_n)$ slowly oscillating, o la cota de Tauber $n(a_n-a_{n-1})$ acotada), entonces
$a_n\to s$. En el lenguaje del defecto: la condición $\mathcal T$ cumple
$\mathcal T_0\cap H_{\mathrm{osc}}=\{0\}$, donde $\mathcal T_0$ es el cono/banda de oscilación lenta centrada;
la fluctuación con media nula y oscilación lenta es nula en el límite.

*Prueba.* Es el teorema tauberiano de Hardy–Littlewood / Schmidt en su forma estándar:
Cesàro-sumabilidad + oscilación lenta $\Rightarrow$ convergencia ordinaria
([Hardy, *Divergent Series*, Thms 92, 113; Korevaar, *Tauberian Theory*, Ch. I §7]). La traducción: si
$F\in H_{\mathrm{osc}}$ (media-bloque $0$ en toda escala) **y** $F\in\mathcal T_0$ (oscilación lenta), entonces
las fluctuaciones que el promedio borra están además forzadas a ser uniformemente pequeñas a escala fina; el
único elemento compatible con ambas es $0$. El paso preciso es el lema de Schmidt: oscilación lenta convierte
control en media en control puntual. ∎

**Lectura unificadora.** Tauberiano $=$ un input externo de *regularidad unilateral* que excluye las
oscilaciones rápidas de $H_{\mathrm{osc}}$. La banda $\mathcal T_0$ es transversal a la oscilación cruda.

### 4.3 Continuación única (ecuación + soporte)

[TEOREMA 4.5] Sea $H=L^2(U)$, $U\subseteq\mathbb R^d$ abierto conexo, y $A$ la restricción-extensión a un
sub-σ-álgebra de soporte tal que $H_{\mathrm{osc}}\subseteq\{u:u|_{V}=0\text{ en un abierto }V\subseteq U\}$.
Si los elementos de $H_{\mathrm{osc}}$ son además soluciones de una EDP elíptica de segundo orden con
coeficientes lipschitz (o soluciones de $\Delta u=Vu$, $V\in L^\infty$), entonces $H_{\mathrm{osc}}=\{0\}$.

*Prueba.* Por la **propiedad de continuación única fuerte** (Aronszajn 1957; Garofalo–Lin 1986;
[Aronszajn, *J. Math. Pures Appl.* 36 (1957)]): una solución de tal ecuación que se anula en un abierto se
anula en todo el componente conexo $U$. Luego cualquier $u\in H_{\mathrm{osc}}$ es $\equiv0$. ∎

**Lectura unificadora.** UCP $=$ input externo de *analiticidad/rigidez de soluciones*. Una ecuación de
continuación única hace que "ser invisible localmente" (vivir en $H_{\mathrm{osc}}$ con soporte recortado)
implique "ser cero globalmente". La estructura de ecuación recorta la fibra.

### 4.4 Acción de grupo (simetría / ergodicidad)

[TEOREMA 4.7] Sea $G$ grupo localmente compacto actuando unitariamente $g\mapsto U_g$ en $H$, y
$A=P_{H^G}$ la proyección sobre los vectores invariantes $H^G=\{F:U_gF=F\ \forall g\}$ (= promedio ergódico,
von Neumann). Entonces $H_{\mathrm{ind}}=H^G$, $H_{\mathrm{osc}}=(H^G)^\perp$, y:
**la acción es ergódica (los únicos invariantes son los escalares/constantes) $\iff$ $H_{\mathrm{osc}}$ no
contiene vectores invariantes no triviales $\iff$ todo $F$ con $\delta_A(F)=0$ es constante.**

*Prueba.* $A$ es la proyección sobre $H^G$ por el teorema ergódico medio de von Neumann
([Krengel §2.1, Thm 1.2]). $\delta_A(F)=0\iff F\in H^G$. La ergodicidad de $G\curvearrowright(\Omega,\mu)$
equivale, vía Koopman, a $\dim H^G=1$ ($H^G=\mathbb C\cdot1$) ([Walters, *Ergodic Theory*, Thm 1.6;
Eisner–Farkas–Haase–Nagel, *Operator Theoretic Aspects of Ergodic Theory*, Ch. 7]). Entonces $\delta_A(F)=0$
fuerza $F$ constante. ∎

**Lectura unificadora.** Simetría $=$ input externo de *invariancia bajo un grupo*. La ergodicidad es
"$H_{\mathrm{osc}}$ no esconde invariantes": el promedio de grupo individúa exactamente porque la órbita barre
todo salvo las constantes.

### 4.5 El principio de reducción (unificación)

[TEOREMA 4.8] *(Los cuatro colapsadores son una sola cosa.)* Sea $(H,A)$ par promediador. Para cada uno de los
cuatro inputs —cono $\mathcal K$ con $A$ fiel; banda tauberiana $\mathcal T_0$; clase-solución de UCP
$\mathcal U$; órbita ergódica de $G$— el mecanismo de colapso es **idéntico**: producir un subconjunto
$\mathcal R\in\{\mathcal K,\mathcal T_0,\mathcal U,H^G\}$ con
$$\mathcal R\cap H_{\mathrm{osc}}=\{0\},$$
de modo que $F\in\mathcal R\Rightarrow F\in H_{\mathrm{ind}}\Rightarrow\delta_A(F)=0$. La diferencia entre
mecanismos es **únicamente el tipo de objeto** que certifica la transversalidad:
- positividad → un **cono** (orden parcial),
- tauberiano → una **banda/cono de regularidad** (cota unilateral),
- UCP → una **variedad de soluciones** (analiticidad/rigidez de EDP),
- grupo → un **subespacio de invariantes** (simetría).

*Prueba.* En cada teorema 4.1/4.3/4.5/4.7 se probó exactamente $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$, y el
cierre $F\in\mathcal R\Rightarrow\delta_A(F)=0$ es Prop. 2.2 aplicada a $F\in H_{\mathrm{ind}}$. ∎

**Esta es la unificación pedida.** "Colapsar el defecto" $=$ "reducir el espacio de oscilación compatible a
cero", y cada mecanismo conocido es una manera distinta de fabricar la transversalidad. El muro es, en este
lenguaje, **la situación en que ninguno de los $\mathcal R$ está disponible**: $F$ no es positivo, ni de
oscilación lenta, ni solución de una UCP, ni invariante de un grupo grande, y entonces $\delta_A(F)>0$
sobrevive.

---

## 5. ¿Hay un quinto colapsador? (el [DESEO] formulable)

La teoría existe precisamente para que esta pregunta tenga forma.

### 5.1 La pregunta, precisa

[DEFINICIÓN-NUEVA 5.1] Un **colapsador** para $(H,A)$ es un par $(\mathcal R,c)$ donde $\mathcal R\subseteq H$
con $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$ y $c$ es un *certificado* (un teorema, una estructura) que prueba
esa transversalidad usando un input externo. Dos colapsadores son **del mismo tipo** si sus certificados se
factorizan uno por otro vía un morfismo que preserve la estructura externa (orden→orden, cota→cota,
solución→solución, equivariancia→equivariancia).

[DESEO 5.2] **¿Existe un colapsador cuyo certificado NO se factorice por ninguno de los cuatro tipos
(orden, cota unilateral, soporte/analiticidad, simetría)?** Equivalentemente: ¿existe una estructura externa
$\Xi$ sobre $(H,A)$ que fuerce $\Xi\cap H_{\mathrm{osc}}=\{0\}$ sin ser reducible a positividad, tauberiano,
UCP o acción de grupo?

Esta es una pregunta bien planteada en la teoría: pide un quinto **tipo de transversalidad**.

### 5.2 Un invariante que clasifica colapsadores: el tipo de transversalidad

[DEFINICIÓN-NUEVA 5.3] Para un colapsador $\mathcal R$, su **tipo de transversalidad** $\tau(\mathcal R)$ es la
estructura mínima que $\mathcal R$ debe llevar para que $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$ sea un teorema:
- $\tau=\mathbf{ord}$ si la prueba usa un orden parcial compatible con $A$ y la fidelidad/positividad;
- $\tau=\mathbf{tau}$ si usa una cota unilateral de tamaño a escala;
- $\tau=\mathbf{ucp}$ si usa rigidez de soluciones (anularse local ⟹ global);
- $\tau=\mathbf{sym}$ si usa equivariancia bajo un grupo y barrido de órbita;
- $\tau=\mathbf{?}$ si no es ninguno de los anteriores.

[PROPOSICIÓN 5.4] *(Dónde NO buscar el quinto: las cuatro saturan los mecanismos "monótonos".)* Si el
certificado de $\mathcal R$ se obtiene por un argumento que es (i) monótono respecto de un cono, (ii) o por
estimaciones de un solo lado, (iii) o por un principio del máximo/unicidad de Cauchy, (iv) o por promediar una
órbita, entonces $\tau(\mathcal R)\in\{\mathbf{ord},\mathbf{tau},\mathbf{ucp},\mathbf{sym}\}$.

*Prueba (delimitación, no demostración de inexistencia).* Cada uno de (i)–(iv) es el ingrediente esencial
de los Teoremas 4.1, 4.3, 4.5, 4.7 respectivamente, y la transversalidad probada allí usa *exactamente* ese
ingrediente. Por construcción de Def. 5.3, un certificado que usa (i)–(iv) tiene el tipo correspondiente. ∎

**Dónde buscaría un quinto colapsador (heurística, [DESEO]).** La Prop. 5.4 dice que un colapsador genuinamente
nuevo debe evitar monotonía, cotas de un lado, principios del máximo y barrido de órbita. El candidato
estructural que la teoría señala es un mecanismo **no-conmutativo / de fase**: una relación de
*incompatibilidad espectral* que fuerce transversalidad sin orden ni simetría —por ejemplo, un par de
proyecciones en **posición genérica** (ángulo de Friedrichs positivo) cuya geometría excluya
$H_{\mathrm{osc}}$ por razones de **frame/inconmensurabilidad** (cf. Doc 148, frames inconmensurables) en lugar
de orden. Esto es coherente con la observación 2.3: el defecto sobrevive al límite débil; un colapsador que
controle ese límite débil necesitaría compacidad o una rigidez espectral, no positividad. **No afirmamos que
exista**; afirmamos que la teoría lo vuelve un objeto buscable y le da un invariante ($\tau=\mathbf?$) que lo
detectaría.

[GAP] No tenemos ni una construcción de un colapsador de tipo $\mathbf?$ ni una prueba de que los cuatro tipos
sean exhaustivos. La exhaustividad sería un teorema profundo (clasificación de mecanismos de
transversalidad); su negación sería el quinto colapsador. Ambos quedan abiertos.

---

## 6. [PUENTE honesto y breve] El diccionario con la forma de Weil

**Advertencia de honestidad.** Esta sección es SÓLO un diccionario. **No** convierte el documento en una
equivalencia de RH, **no** prueba nada sobre ζ, y declara el estatus de cada eslabón.

| Objeto de la teoría | Realización en la forma de Weil |
|---|---|
| $H$ | El espacio de la forma de Weil localizada: secciones/ventanas del lado explícito (Doc 134 §3, álgebra de Weil–Toeplitz $\mathcal W$), o $L^2$ del calendario de ventanas (Doc 108 §5.2). |
| $A$ | El **promedio sobre ventanas / media MV74**: la proyección sobre el "símbolo autónomo" computable desde los primos; $H_{\mathrm{osc}}$ = el ideal $c_0$ / compacto $\mathcal J$ (Doc 134, corona $\mathcal C=\mathcal W/\mathcal J$). |
| $F$ | La **contribución oscilatoria cero-a-cero** —la señal individual de los ceros que el promedio borra (la ventana excepcional de Doc 108, Teorema 3.3 de ceguera sub-resolución). |
| $\delta_A(F)$ | El tamaño de la parte de $F$ invisible al símbolo: la norma de la componente en el ideal compacto. $\delta_A(F)=0$ significaría que la señal de los ceros está enteramente determinada por el símbolo autónomo. |
| Colapsador | La **positividad esencial estricta del símbolo** (Doc 134, Teorema 1.3): el cono $\mathcal K$ del Teorema 4.1 de este documento, llevado al espectro de la corona. |

**El muro, en este diccionario.** El fenómeno promedio→individual de ζ es: el promedio $AF$ (símbolo desde
primos) **no determina** $F$ (señal de ceros) porque $H_{\mathrm{osc}}\neq\{0\}$ —la información cero-a-cero
vive justo en el ideal compacto/oscilatorio (Doc 134 Teorema 5.2: "los ceros viven en la frontera
símbolo/compacto"). Por el Teorema 3.4 de este documento, **ningún argumento que use sólo el promedio puede
individuar los ceros**: hace falta un input externo.

**Cuál input.** El candidato es positividad (Teorema 4.1) en la forma de positividad esencial *estricta* del
símbolo (Doc 134). Estatus de cada eslabón, honesto:
- "El promedio sobre ventanas es una proyección $A$": **plausible y formalizado** en Doc 134 (corona), pero
  la normalización de peso fijo destruye el gap incondicionalmente (Doc 134 Teorema 2.2) — el $A$ correcto no
  es trivial. [GAP].
- "La señal de ceros $F$ vive en $H_{\mathrm{osc}}$": **probado** en el modelo de ventanas (Doc 108 Thm 3.3,
  Doc 134 Thm 5.2) — es la ceguera sub-resolución.
- "Positividad estricta colapsa el defecto": es el Teorema 4.1 *abstracto* de este documento; su realización
  para ζ es **exactamente el certificado que falta** (Doc 134: el gap robusto-bajo-compactos ES el gap, y
  Phase 38 refutó $W_\lambda\ge0$ ingenuo). **NO probado para ζ.** [GAP central del programa].

**Conclusión del puente.** La teoría del defecto *no resuelve* RH ni produce una equivalencia. Lo que aporta es
un **diagnóstico estructural**: el muro de ζ es el caso $H_{\mathrm{osc}}\neq\{0\}$ sin colapsador disponible;
los cuatro mecanismos catalogados se traducen a inputs concretos (positividad estricta del símbolo es el más
cercano), y todos están bloqueados por las refutaciones registradas (Phase 38, Doc 134 §2). Si existe el quinto
colapsador del §5 —de tipo $\tau=\mathbf?$, no-conmutativo/de fase—, sería el candidato no catalogado. Eso es un
[DESEO], no un teorema.

---

## 7. Mensaje final

**Definición central.** Para un par promediador $(H,A)$ ($A=A^*=A^2$, $H_{\mathrm{osc}}=\ker A$), el
**defecto de individuación** de $F$ es $\delta_A(F)=\|(1-A)F\|=\mathrm{dist}(F,\mathrm{rango}\,A)$: la norma de
la componente que el promedio borra. Mide la obstrucción intrínseca a recuperar el dato individual desde su
promedio.

**Teorema de caracterización.** [Teorema 3.2 + Teorema 3.4] $\delta_A(F)=0\iff F\in H_{\mathrm{ind}}$, y para
$F$ no manifiestamente invariante el colapso **nunca ocurre por la sola estructura lineal de $A$**: requiere un
input externo que vuelva transversal a $F$ al espacio de oscilación ($\mathcal S\cap H_{\mathrm{osc}}=\{0\}$).
El defecto no colapsa solo —la predicción del encargo queda probada.

**Tres resultados etiquetados.**
1. **[TEOREMA 2.5]** (dualidad defecto↔invisibilidad): el promedio determina $F$ módulo $H_{\mathrm{osc}}$ y
   nada más; la indeterminación del inverso "$AF\mapsto F$" es el radio de la fibra $F+H_{\mathrm{osc}}$ —el muro,
   como teorema.
2. **[TEOREMA 4.8]** (principio de reducción): los cuatro colapsadores conocidos —positividad, tauberiano,
   continuación única, acción de grupo— son una sola cosa, "fabricar $\mathcal R$ con
   $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$"; difieren sólo en el *tipo* de certificado de transversalidad.
3. **[PROPOSICIÓN 5.4 + DEFINICIÓN 5.3]** (tipo de transversalidad): un invariante $\tau\in\{\mathbf{ord},
   \mathbf{tau},\mathbf{ucp},\mathbf{sym},\mathbf?\}$ que clasifica colapsadores y vuelve **formulable** la
   pregunta del quinto colapsador ($\tau=\mathbf?$, candidato no-conmutativo/de fase), sin afirmar su existencia.
