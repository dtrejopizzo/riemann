# Doc 150 — Auditoría adversarial de los Docs 144 y 146 (LP-141 / GAP-141.DH)

**Programa:** Hipótesis de Riemann — Phase 48: AUDITORÍA Y PUREZA.
**Fecha:** junio 2026.
**Rol del documento:** auditoría con mandato de matar sobre las piezas load-bearing del Doc 144
(contraejemplo de Hadamard 144.2/144.3; frontera 144.8; reducción 144.4/144.D; cadena de fuerza 144.6)
y del Doc 146 (veredicto GORDOS de GAP-141.DH; implicación para LP-141; "repulsión barata / falta pureza").
Prerrequisitos leídos en fuente COMPLETOS esta sesión: Doc 144, Doc 146, Doc 141 entero, Doc 134
(§3 álgebra/ideal/corona, §4 modelo $\mathfrak W$, §5 Teoremas 5.0–5.5 y 5.5bis, §5.8 M1–M4),
ERRATA E46.4 (Thm 5.3′ corregido: estricta ⟺ $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$,
SIN cláusula de excepción; errata de caso degenerado de 5.2(iv); caveat B.4).

**Contrato:** [VERIFICADO] = re-derivado y sano. [REFUTADO] = contraejemplo o error lógico exhibido, con
prueba. [SOBRE-RECLAMADO] = el soporte prueba un enunciado estrictamente más débil que el enunciado.
[REPARABLE] = corrección concreta dada. [GAP de literatura] = dato no verificable al nivel de página esta
sesión, declarado y NO usado como premisa de ningún veredicto.

---

## 0. Veredicto por pieza

| pieza | veredicto | detalle |
|---|---|---|
| **Prop. 144.2 + Cor. 144.3** (Hadamard adaptado refuta LP-141 ∀ calendario) | **[VERIFICADO]** | orden exactamente 1 ✓; sin factor $e^{A+Bs}$ (paridad lo fuerza a 0) ✓; ecuación funcional y realidad ✓; densidad $\asymp T\log T$ (no $\sim$, ver §1.3 — inofensivo) ✓; cuantificador $\forall a\,\exists F_a$ correcto y el único posible ✓ |
| **Prop. 144.8** ("≥1 gordo" no basta; LP-141 es el mínimo) | **[VERIFICADO]** contra erratas | usa 5.3′/5.4 corregidos, no la versión vieja; matiz declarado en §2.3 sobre el paréntesis "(y estrictamente)" — la pieza load-bearing solo necesita la débil y sobrevive |
| **Prop. 144.1(a)** (LP-134$^{(\psi)}\Rightarrow$LP-141$(a)$ ∀$a\succeq\psi$) | **[REFUTADO tal como está enunciada]** [REPARABLE] | contraejemplo cerrado (§3.2): $\delta_j=1/(2\psi(\gamma_j))$ cumple LP-134$^{(\psi)}$ y viola LP-141$(\psi)$; la invariancia por constantes de la clase $\{C\log\}$ vale para LP-134 (liminf) pero **NO para LP-141** (umbral $\geq1$); forma correcta: LP-134$^{(\psi)}\Rightarrow\exists C:\mathrm{LP\text{-}141}(C\psi)$ |
| **Prop. 144.4** (144.D ⟹ LP-141 ∀$a\succeq\log$, "forma fuerte a calendario log") | **[SOBRE-RECLAMADO]** [REPARABLE] | misma falla: 144.D con constante $c<1$ da LP-141 solo a calendario $\lceil1/c\rceil\log$, con $c=c(F)$ **interna a la función** — reaparece la constante interna al mundo de 141.A/P43 (§3.3); la implicación reparada es válida a nivel de clase |
| **Conjetura 144.D** (buena definición) | **[VERIFICADO]** con observación | bien formada, no circular como conjetura; pero es casi-tautológica respecto de LP-141 (es LP-141 con escala explícita); el contenido real ("rigidez de continuación") sigue siendo mecanismo nombrado, no hipótesis independiente (§3.4) |
| **Cadena 144.6** (Axioma R ≻ LP-134 ≻ LP-141 ≻ LP-142, todas estrictas) | **[SOBRE-RECLAMADO]** [REPARABLE] | el separador de Axioma R ≻ LP-134 está **mal citado** (141.P4(iii) da LP-141⟹̸AxR, que no separa ese eslabón); separador correcto trivial dado en §3.5; el eslabón LP-134 ⟹ LP-141 hereda la falla de 144.1(a); LP-141 ≻ LP-142 ✓ íntegro |
| **Doc 146, veredicto "GORDOS" fuerte** ($\liminf_{\rho\,\mathrm{off}}\delta_\rho>0$, "ni siquiera módulo $\log\gamma$") | **[REFUTADO]** | error lógico liminf/limsup en el uso del Hecho 146.6 (§4.2) + la propia universalidad invocada en §3.2 del Doc 146 fuerza $\liminf\delta_\rho=0$ (Prop. 150.2, prueba por universalidad conjunta + Rouché, §4.3); D–H **NO** satisface la separación de banda ni la "forma más fuerte de LP-134" |
| **Doc 146, enunciado débil** (∃ infinitos gordos = LP-141 para D–H) | **[VERIFICADO]** | sólido e incondicional: infinitos ceros con $\beta>1$ [DH36] ⟹ $\delta_j\geq\tfrac12$ en una subsucesión infinita ⟹ LP-141$(a)$ para todo calendario no acotado (§4.5) |
| **Doc 146, LP-134$^{(\log)}$ para D–H** (caso (b) vs (d) de 144.9) | **ABIERTO** | la pregunta que el Cor. 144.10 realmente encargó ($\liminf\delta_j\log\gamma_j$) NO queda decidida por la literatura cualitativa (§4.6); el Doc 146 contestó otra pregunta (más fuerte) y la contestó mal |
| **Consistencia 144↔146 y "repulsión barata"** | consistentes en LP-141; **la retórica de "repulsión" debe corregirse** | lo barato es la *gordura abundante* (LP-141), NO la *repulsión* (LP-134): el casi-Euler de D–H produce infinitos gordos Y ceros arbitrariamente pegados a la línea (§5) |

---

## 1. Re-derivación del contraejemplo de Hadamard (Prop. 144.2)

### 1.1. Convergencia, orden y género — [VERIFICADO]

Datos: en coordenada $z$ ($s=\tfrac12+iz$), mar real $\pm t_n$, $t_n=n/\log(n+2)$; cuádruplos
$\{\pm z_j,\pm\bar z_j\}$, $z_j=\gamma_j-i\delta_j$, $\gamma_j=2^j$,
$\delta_j=\min(\tfrac14,\,1/(j\,a(2^j)))$;
$$G(z)=\prod_{n}\Bigl(1-\frac{z^2}{t_n^2}\Bigr)\prod_{j}\Bigl(1-\frac{z^2}{z_j^2}\Bigr)\Bigl(1-\frac{z^2}{\bar z_j^2}\Bigr).$$

*Convergencia.* En $w=z^2$ los ceros son $w_n=t_n^2$ y $w_j^{\pm}=z_j^2,\bar z_j^2$. Re-cuento:
$\sum_n t_n^{-2}=\sum_n\log^2(n+2)/n^2<\infty$ ✓; $|z_j|^2\geq\gamma_j^2=4^j$ ⟹
$\sum_j 2|z_j|^{-2}\leq2\sum_j4^{-j}<\infty$ ✓. El producto en $w$ es **canónico de género 0**
($\sum|w_k|^{-1}<\infty$): converge absoluta y localmente uniformemente. ✓

*Orden exactamente 1 (no solo $\leq1$).* Contador en $w$: $n_w(r)=\#\{t_n\leq\sqrt r\}+O(\log r)
\asymp\sqrt r\log r$; exponente de convergencia en $w$ $=\tfrac12$ (en $\tfrac12$ exacto:
$\sum t_n^{-2\lambda}$ converge ⟺ $\lambda>\tfrac12$... más precisamente $\sum_n(\log(n+2)/n)^{2\lambda}$
converge ⟺ $2\lambda>1$). Por Boas [B54, Thm. 2.6.5] (orden de un producto canónico = exponente de
convergencia de sus ceros), $P(w)$ tiene orden $\tfrac12$ en $w$, exacto. Luego $G(z)=P(z^2)$ tiene orden
**exactamente $1$** en $z$. ✓ La cota inferior también se ve directo en $z$: $\sum_n t_n^{-1}=
\sum\log(n+2)/n=\infty$ ⟹ exponente de convergencia $\geq1$ en $z$ ⟹ orden $\geq1$. ✓
Los cuádruplos off aportan contador $O(\log r)$: irrelevantes para el orden. ✓

*Género.* La frase del Doc 144 "producto de género 0 en $w$" es correcta. En $z$, el género de Hadamard
sería 1 (pues $\sum1/|a_k|=\infty$), pero el apareamiento simétrico $(1-z/t)(1+z/t)=(1-z^2/t^2)$ cancela
idénticamente los factores exponenciales $E_1$: el producto en $w$ ES la factorización, sin primarios de
género 1. No hay error.

### 1.2. La ecuación funcional y el factor $e^{A+Bs}$ — [VERIFICADO]

La objeción potencial era: el teorema de Hadamard para orden 1 da $G(z)=e^{A+Bz}\prod E_1(z/a_k)$ — ¿se
puede elegir $B$ compatible con $G(-z)=G(z)$ Y con la realidad en la línea? **La objeción no muerde porque
la construcción no representa una función dada: la DEFINE como el producto par.** $G$ es par por
construcción (todo factor depende de $z^2$), luego $F_a(s):=G(\frac{s-1/2}{i})$ cumple $F_a(1-s)=F_a(s)$
exactamente, sin factor exponencial ($B=0$ forzado por paridad: si $G$ par y $G=e^{A+Bz}\Pi$ con $\Pi$ el
producto par, entonces $e^{Bz}$ par ⟹ $B=0$). Realidad en la línea: cada factor tiene coeficientes reales
en $w$ — los del mar trivialmente; los de cuádruplo,
$(1-w/z_j^2)(1-w/\bar z_j^2)=1-2w\,\Re(z_j^2)/|z_j|^4\cdot|z_j|^4/|z_j|^4\,\dots$ — explícitamente
$1-w\bigl(\tfrac1{z_j^2}+\tfrac1{\bar z_j^2}\bigr)+\tfrac{w^2}{|z_j|^4}$ con
$\tfrac1{z_j^2}+\tfrac1{\bar z_j^2}=2\Re(z_j^2)/|z_j|^4\in\mathbb R$ ✓. Luego $G(\bar z)=\overline{G(z)}$,
$G|_{\mathbb R}\subseteq\mathbb R$, $F_a$ real en $\tfrac12+i\mathbb R$. ✓ Banda:
$|\Im z_j|=\delta_j\leq\tfrac14<\tfrac12$ ✓. El multiconjunto de ceros es invariante bajo $z\mapsto-z$ y
bajo conjugación ✓: la simetría del multiconjunto MÁS la definición-como-producto resuelven la pregunta (ii)
del protocolo sin residuo.

### 1.3. "Densidad tipo ζ" — [VERIFICADO con matiz no portante]

$t_n\leq T\iff n\lesssim T\log T$: $N_{F_a}(T)\asymp T\log T$, mismo ORDEN que Riemann–von Mangoldt pero
con constante $1$, no $\tfrac1{2\pi}$. La Prop. 144.2 enuncia $\asymp$, y eso es lo que prueba: **no hay
sobre-reclamo formal**. Si alguna pieza futura necesitara la asintótica exacta
$N(T)\sim\frac{T}{2\pi}\log\frac T{2\pi}$, basta re-escalar el mar ($t_n$ definido implícitamente por
$\#\{t_m\leq r\}=\lfloor\frac r{2\pi}\log\frac r{2\pi}\rfloor$; las series de convergencia no cambian).
Matiz registrado: "densidad tipo ζ" debe leerse como $\asymp$, no $\sim$.

### 1.4. La calibración $\delta_j=\min(\tfrac14,1/(j\,a(2^j)))$ y el orden de cuantificadores — [VERIFICADO]

*Sub-resolución.* Para los $j$ con $j\,a(2^j)>4$ (todos salvo finitos: $j\,a(2^j)\geq j\to\infty$ incluso
con $a$ acotada): $\delta_j a(\gamma_j)=1/j\to0$ ✓. Los finitos $j$ iniciales con $\delta_j=\tfrac14$
pueden ser gordos ($a(2^j)/4\geq1$ posible) — pero son **finitos**, y LP-141 exige **infinitos** gordos:
$|\mathcal G_a|<\infty$ con $m=\infty$ viola LP-141$(a)$. ✓ (La frase del doc "$|\mathcal G_a|=0$
eventualmente" es ligeramente torpe — lo correcto es "$\mathcal G_a$ finito" — sin consecuencia.)

*Cuantificadores.* La proposición es $\forall a\ \exists F_a$: el calendario se fija PRIMERO y $\delta_j$
usa solo los valores $a(2^j)$ del calendario ya fijado. Ese es exactamente el orden necesario para refutar
LP-141 en la categoría, porque LP-141$(a)$ es un enunciado a calendario fijo y el Cor. 144.3 concluye
**por cada calendario fijo**. El orden inverso ($\exists F\ \forall a$: una sola función con cero gordos a
TODO calendario) es **imposible** — el Teorema 141.A construye el calendario adaptado $a_Z$ que hace gordo
a todo cuádruplo de cualquier configuración — y el Doc 144 NO lo reclama (lo dice bien en §2.2 y en 144.3:
"para cada calendario fijo, un miembro que lo viola"). ✓ El refinamiento sobre 141.R2 (que solo cubría
calendarios sub-exponenciales) es genuino y el cálculo $\delta_j a(\gamma_j)=1/j$ es exacto.

**Veredicto §1: la Prop. 144.2 y el Cor. 144.3 SOBREVIVEN la auditoría íntegros.** El único punto débil de
todo §2 del Doc 144 no está en 144.2 sino en lo que se concluye después con la clase $\{C\log\}$ (§3 abajo).

---

## 2. Prop. 144.8 contra las erratas (E46.4) — [VERIFICADO con matiz]

### 2.1. ¿Usa la versión vieja (falsa) del Thm 5.3?

No. La prueba de 144.8(a) descansa en: (1) un gordo aislado = sección de soporte finito en ventanas
$\in\mathcal J$ (Def. 3.1 del D134: $\mathcal J$ contiene toda sección de soporte finito) — esto es
álgebra del ideal, independiente de 5.3; (2) la cola $\delta_j=e^{-\gamma_j}$ es estrictamente
sub-resolución ⟹ Teorema 5.4 (absorción: $Q-Q^{\mathrm{aut}}\in\mathcal J$); (3)
$\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, positivo. Ninguno de los tres pasos invoca la cláusula de excepción
falsa del viejo 5.3(ii). Contra el 5.3′ corregido (estricta ⟺ $\#\{n:J_n^{\mathrm{vis}}\neq\emptyset\}<\infty$)
la construcción es CONSISTENTE: en el régimen estrictamente sub-resolución de la Def. 4.4 los cuádruplos
con $\theta_j=0$ no pueblan $J_n^{\mathrm{vis}}$, así que solo hay UNA ventana visible (la del gordo
$\gamma_0=10$): finitas ⟹ 5.3′ da estricta. ✓

### 2.2. "Se necesita subsucesión infinita" contra 5.1/5.2 post-erratas

El Teorema 5.1 del D134 (re-leído en fuente) exige subsucesión $j_k$ con $\theta_{j_k}\geq c$ **y
$\gamma_{j_k}\to\infty$**: el punto límite del Lema 3.3 necesita $n_k\to\infty$; un solo gordo (o finitos)
da autovalor negativo solo en finitas ventanas, que la truncación $A^{(N)}\in\mathcal J$ borra
(Lema 3.2). La afirmación de 144.8 es exactamente el mecanismo de 5.1 leído al contrapositivo, y coincide
con la calibración M1 (cosh: $m$ finito ⟹ símbolo estrictamente positivo). La errata 2 de E46.4 (caso
degenerado de 5.2(iv), $\vartheta_n\leq\omega_n$) NO es invocada por 144.8. ✓

### 2.3. El matiz honesto (no portante)

El paréntesis de 144.8(a) "$\sigma(Q)=\sigma(Q^{\mathrm{aut}})$, débilmente **(y estrictamente)** positivo"
depende de modelar la cola $e^{-\gamma_j}$ como estrictamente sub-resolución ($\theta_j=0$, absorbida en
$R_n/C_n$). Si en cambio se modelara como "finos visibles" ($\theta_j>0$, $\theta_j\to0$), el Teorema 5.2 +
5.3′ corregido dan: débil SÍ, **estricta NO** ($0\in\mathrm{spec}$, infinitas ventanas visibles). El
enunciado load-bearing de 144.8(a) — "positividad **débil** + ≥1 gordo es consistente con $m=\infty$" —
sobrevive en AMBAS lecturas, porque la sinergia 141.P3 solo usa la débil. Recomendación cosmética: borrar
el paréntesis "(y estrictamente)" o condicionarlo explícitamente a $\theta_j=0$. Con eso, **144.8(a), (b)
y (c) quedan VERIFICADOS** y la frontera "infinitos gordos, ni más ni menos" (Obs. 144.8bis) es la sombra
fiel del Teorema 5.1.

---

## 3. La reducción 144.4 / Conjetura 144.D — el hallazgo central sobre el Doc 144

### 3.1. Buena definición y no-circularidad de 144.D

Como conjetura, 144.D está bien formada: es un enunciado sobre el multiconjunto de ceros de los miembros de
una categoría (D131-H⁺), del mismo tipo lógico que LP-134/LP-141. No hay circularidad **lógica** (una
conjetura puede mencionar los ceros). Pero hay que decir lo que es: **144.D no es una "propiedad de rigidez
de continuación" independiente que implique LP-141; ES LP-141 con la escala $\log$ explicitada y forma de
subsucesión-liminf, restringida a la categoría Euler.** La "rigidez de continuación cuantitativa" es el
*mecanismo propuesto* (párrafo en cursiva de 144.D), no una hipótesis matemática separada. La Prop. 144.4
es, en consecuencia, una reformulación casi tautológica (su prueba es una línea de re-escalado), y el valor
del §3 del Doc 144 es taxonómico (144.D ≺ 141.E, el frente correcto), no deductivo. El propio doc lo
admite (144.4bis), así que esto es énfasis, no errata. Lo que sigue SÍ es errata.

### 3.2. [REFUTADO] La Prop. 144.1(a) es falsa tal como está enunciada

**Contraejemplo 150.1 [CONTRAEJEMPLO].** Sea $\psi(\gamma)=\log(\gamma+3)$ y la configuración
$Z^*:=\{(\delta_j,\gamma_j)\}_{j\geq1}$ con $\gamma_j=2^j$, $\delta_j:=\dfrac1{2\,\psi(\gamma_j)}$
(admisible: $\delta_j\in(0,\tfrac12)$, finitos por ventana, $m=\infty$). Entonces:
- $\delta_j\,\psi(\gamma_j)=\tfrac12$ para todo $j$: $\liminf=\tfrac12>0$ ⟹ **LP-134$^{(\psi)}$ se cumple**.
- $\mathcal G_\psi=\{j:\delta_j\psi(\gamma_j)\geq1\}=\emptyset$ y $m=\infty$ ⟹ **LP-141$(\psi)$ es FALSO**
  en $Z^*$.

Y $a=\psi$ satisface la hipótesis "$a\succeq\psi$" de 144.1(a). Luego el enunciado
"LP-134$^{(\psi)}\Rightarrow$LP-141$(a)$ para todo $a\succeq\psi$" es **falso** con $a=\psi$. $\square$

*Dónde se rompe la prueba del Doc 144:* la propia demostración de 144.1(a) detecta el problema ("Si $c<1$,
re-escalo el calendario: $a':=\lceil1/c\rceil a$") y luego lo entierra con la frase "como $\{C\log\}$ es UNA
clase de calendario (invariancia por constantes, Obs. 1.1(i) del Doc 141), LP-141 a la clase $\{C\log\}$ se
cumple". Pero la Obs. 1.1(i) del Doc 141 prueba la invariancia por constantes **para LP-134** (el liminf
absorbe $C$ en $c$), y esa invariancia **es FALSA para LP-141**: el umbral "$\delta_j a(\gamma_j)\geq1$" no
absorbe constantes. El contraejemplo 150.1 separa LP-141$(\psi)$ de LP-141$(2\psi)$ (en $Z^*$ con
$\delta_j=1/(2\psi)$: a calendario $2\psi$ todos los cuádruplos son gordos; a calendario $\psi$, ninguno):
**LP-141$(C\log)$ es una familia de enunciados genuinamente distintos en $C$, monótona decreciente en
fuerza** (Obs. 144.0(iii)), no una clase.

**Forma correcta y reparación [REPARABLE]:**
$$\mathrm{LP\text{-}134}^{(\psi)}\ \Longrightarrow\ \mathrm{LP\text{-}141}(a)\quad\text{para todo }a\text{ con }a/\psi\to\infty,
\qquad\text{y}\qquad \mathrm{LP\text{-}134}^{(\psi)}\ \Longrightarrow\ \exists C>0:\ \mathrm{LP\text{-}141}(C\psi),$$
donde $C=\lceil1/c\rceil$ y $c$ es la constante del liminf — **interna a la configuración/función**. La
implicación a calendario FIJO de la misma clase no vale.

### 3.3. Propagación a la Prop. 144.4 — [SOBRE-RECLAMADO]

La Prop. 144.4 afirma: "si vale 144.D, entonces vale LP-141$(a)$ para todo calendario $a\succeq\log$...
De hecho vale la forma fuerte: $m=\infty\Rightarrow$ infinitos gordos a calendario $\log$." Su prueba
construye $a=\lceil1/c\rceil\log$ y aplica monotonía para $a'\succeq a$. Eso establece LP-141$(a')$ solo
para $a'\succeq\lceil1/c\rceil\log$ — **no** para todo $a'\succeq\log$ (p.ej. no para $a'=\log$ mismo si
$c<1$), y la "forma fuerte a calendario $\log$" **no está probada**: con $c<1$, 144.D es consistente con
cero gordos a calendario $\log$ (configuración 150.1 con $\liminf$ de subsucesión $=c=\tfrac12$). Enunciado
reparado:
$$\textbf{144.4′}:\quad \text{144.D}\ \Longrightarrow\ \exists C=C(F)>0:\ \mathrm{LP\text{-}141}(C\log)\ \ \text{y}\ \ \mathrm{LP\text{-}141}(a)\ \forall a\ \text{con } a/\log\to\infty.$$

**Por qué esto NO es cosmético.** La sinergia 141.P3 necesita LP-141$(a)$ y positividad débil del símbolo
$\sigma_a(Q)$ **al mismo calendario $a$**. Con 144.4′, el calendario en que se obtienen los gordos es
$C(F)\log$ con $C(F)$ interna a la función: para cerrar $m<\infty$ haría falta positividad débil del
símbolo a calendario $C(F)\log$ — o, uniformemente, **a toda la familia $\{C\log\}_{C\in\mathbb N}$** (que
por la Prop. 5.5bis(iii) del D134 es una condición decreciente: positividad a calendarios más altos es MÁS
exigente). Es decir: la falla de invariancia reintroduce exactamente la **constante interna al mundo** que
el Teorema 141.A diagnosticó como la trivialización del calendario libre, ahora en miniatura (un factor
constante, no un calendario arbitrario). No mata la ruta — un factor constante sobre la clase $\log$ es
infinitamente más benigno que el calendario adaptado $a_Z$ de 141.A — pero **debe declararse**: la versión
honesta de la ruta es
$$m<\infty\ \Longleftarrow\ \bigl[\sigma_{C\log}(Q)\geq0\ \text{débil }\forall C\in\mathbb N\bigr]\ \wedge\ \text{144.D}.$$
La misma corrección aplica a la Prop. 144.9(b) del Doc 144 ("DH satisface LP-134$^{(\log)}$... a fortiori
LP-141" — a fortiori LP-141$(C\log)$ para algún $C$, no LP-141$(\log)$), y retro-aplica a la Prop.
141.P4(i) del Doc 141, que contiene el mismo paso de re-escalado con el mismo gap ("re-escalando $a$ son
gordos" — re-escalar $a$ cambia el enunciado).

### 3.4. ¿Esconde 144.4 un "para casi todo"?

No. Módulo la reparación de calendario de §3.3, la implicación 144.D ⟹ LP-141$(C\log)$ es exacta, sin
pasos de densidad ni de "casi todo": una subsucesión infinita con $\delta_{j_k}\log\gamma_{j_k}\geq c$ se
convierte literalmente en una subsucesión infinita de gordos a calendario $\lceil1/c\rceil\log$. La
implicación es completa (y por eso mismo, magra: el trabajo está todo en 144.D).

### 3.5. La cadena de fuerza 144.6 — separador mal citado [REPARABLE]

La cadena Axioma R ⟹ LP-134 ⟹ LP-141 ⟹ LP-142 con "ninguna flecha se invierte" cita tres separadores:
144.1(b) (LP-141⟹̸LP-134 ✓ correcto), **Prop. 141.P4(iii) (LP-141⟹̸Axioma R)** y 144.8(a)
(LP-142⟹̸LP-141 ✓ correcto). El segundo NO separa el eslabón que debe separar: la estrictez de
"Axioma R ≻ LP-134" requiere **LP-134 ⟹̸ Axioma R**, y "LP-141⟹̸AxR" no lo implica (LP-134 es más fuerte
que LP-141: podría implicar AxR aunque LP-141 no lo haga). Tal como está citada, la estrictez del PRIMER
eslabón queda sin prueba.

**Separador correcto (trivial) [PROPOSICIÓN 150.3].** La configuración de un solo cuádruplo
$Z_1=\{(\tfrac14,\gamma_0)\}$ (el anti-modelo cosh, M1 del D134) cumple LP-134$^{(\psi)}$ para toda escala
(conjunto de off finito ⟹ $\liminf:=+\infty$, convención de la Def. 141.1) y **viola el Axioma R**
cuantitativo, cuya consecuencia registrada en 141.P4(ii) es "$m\geq1\Rightarrow$ infinitos gordos": aquí
$m=1\geq1$ y los gordos son finitos. $\square$

Además el eslabón LP-134 ⟹ LP-141 de la cadena hereda la falla de 144.1(a) (§3.2): a calendario fijo es
falso; la cadena vale **a nivel de clase** ($\exists C$). Estado final de la cadena tras reparaciones:
$$\text{Axioma R}\ \succ\ \mathrm{LP\text{-}134}^{(\psi)}\ \succ\ \bigl[\exists C:\mathrm{LP\text{-}141}(C\psi)\bigr]\ \succ\ \bigl[\exists C:\mathrm{LP\text{-}142}(C\psi)\bigr],$$
todas estrictas con separadores: 150.3, 144.1(b), 144.8(a). La conclusión estructural del Doc 144 (LP-141
es el pivote mínimo; "≥1 gordo" no basta) **sobrevive intacta** — solo que vive en la clase, no en el
calendario individual.

---

## 4. Doc 146: el punto crítico — ¿$\liminf\delta_\rho>0$ o solo $\exists\infty$ gordos?

### 4.1. Los dos enunciados, separados con precisión

Sobre los ceros off $\rho_j=\beta_j+i\gamma_j$ de D–H, $\delta_j=|\beta_j-\tfrac12|$:

- **(FUERTE)** $\liminf_j\delta_j\geq c>0$: TODOS los off están eventualmente a distancia $\geq c$
  (separación de banda; la forma $\psi\asymp1$ de LP-134, "ni siquiera módulo $\log\gamma$"). Es lo que el
  Doc 146 reclama en el recuadro de §4.1 y en el resumen (punto 1).
- **(DÉBIL)** $\#\{j:\delta_j\geq c\}=\infty$ para algún $c>0$: infinitos gordos. Es TODO lo que LP-141
  necesita (y más: gordos a constante, no solo a calendario).

El soporte del Doc 146 — [DH36] (infinitos ceros con $\beta>1$), el testigo [BS07]
($\delta\approx0.31$ a $\gamma\approx85.7$), y el Hecho 146.6 (densidad $\gg T$ en UNA franja fija
$(\sigma_1,\sigma_2)$, $\sigma_1>\tfrac12$) — prueba el DÉBIL con holgura. **Ninguno de los tres prueba el
FUERTE**, y el paso del Doc 146 que pretende deducirlo es un error lógico puro:

> (Doc 146, §2.3) "el Hecho 146.6 exhibe infinitos ceros con $\delta_j\geq\sigma_1-\tfrac12$ constante.
> Entonces $\liminf_{\rho\ \text{off}}\delta_\rho\geq\sigma_1-\tfrac12>0$."

Un liminf sobre TODOS los off no se acota por abajo exhibiendo una SUBFAMILIA lejana: eso acota el
**limsup**. Para el liminf hay que excluir ceros cercanos a la línea — sobre los cuales el Hecho 146.6 es
mudo. Es exactamente la confusión liminf/limsup que el Doc 144 §1.1(i) erige como "la diferencia atómica
entre LP-134 y LP-141" — cometida por el documento gemelo de la misma fase.

### 4.2. El enunciado FUERTE no solo está sin soporte: es FALSO (módulo universalidad conjunta, teorema publicado)

**Proposición 150.2 [PROPOSICIÓN] (los ceros off de D–H se acercan a la línea: $\liminf_j\delta_j=0$,
con densidad $\gg T$ a cada distancia).** Sea $f=\frac{\sec\theta}2(e^{-i\theta}L_1+e^{i\theta}L_2)$ la
función de D–H (Def. 146.2; $L_1=L(s,\chi)$, $L_2=L(s,\bar\chi)$, $\chi$ carácter complejo primitivo mod 5).
Entonces para todo $\varepsilon\in(0,\tfrac18)$ existen infinitos ceros $\rho$ de $f$ con
$\delta_\rho\in[\tfrac\varepsilon2,\tfrac{3\varepsilon}2]$; de hecho $\gg_\varepsilon T$ de ellos con
$0<\gamma\leq T$. En consecuencia $\liminf_{\rho\ \mathrm{off}}\delta_\rho=0$ y D–H **no** satisface
ninguna separación de banda.

*Demostración.* Sea $\sigma_0:=\tfrac12+\varepsilon$, $r:=\tfrac\varepsilon2$, y el disco
$\overline D:=\{|s-\sigma_0|\leq r\}\subset\{\tfrac12<\Re s<1\}$. Defino los blancos
$$g_2(s):\equiv1,\qquad g_1(s):=-e^{2i\theta}\exp\Bigl(\frac{s-\sigma_0}{r}\Bigr),$$
continuos y **sin ceros** en $\overline D$, holomorfos en su interior. La combinación blanco es
$$h(s):=e^{-i\theta}g_1(s)+e^{i\theta}g_2(s)=e^{i\theta}\Bigl(1-\exp\Bigl(\tfrac{s-\sigma_0}{r}\Bigr)\Bigr),$$
que tiene en $\overline D$ un único cero, simple, en $s=\sigma_0$ (los demás ceros de $1-e^w$ están en
$w\in2\pi i\mathbb Z\setminus\{0\}$, fuera de $|w|\leq1$). Sobre la circunferencia $|s-\sigma_0|=r/2$
(i.e. $|w|=\tfrac12$): $|h|=|1-e^w|\geq m_0>0$ con $m_0:=\min_{|w|=1/2}|1-e^w|$ (constante absoluta;
$m_0\geq1-e^{-1/2}>0.39\cdot e^{-1/2}$... basta $m_0>0$, que vale porque $1-e^w$ no se anula en
$|w|=\tfrac12$ y el mínimo de un módulo continuo positivo sobre un compacto es positivo).

Por el **teorema de universalidad conjunta de Voronin** para $L$-funciones de Dirichlet de caracteres no
equivalentes ($\chi\neq\bar\chi$ mod 5; [V75-joint], forma de libro de texto en [KV92] y [St07, Thm. 1.10]):
el conjunto
$$\mathcal T:=\Bigl\{\tau>0:\ \max_{j=1,2}\ \sup_{|s-\sigma_0|\leq r/2}\bigl|L_j(s+i\tau)-g_j(s)\bigr|<\tfrac{m_0}3\Bigr\}$$
tiene densidad inferior positiva en $[0,T]$. Para $\tau\in\mathcal T$, sobre $|s-\sigma_0|=r/2$:
$$\bigl|\,\bigl(e^{-i\theta}L_1+e^{i\theta}L_2\bigr)(s+i\tau)-h(s)\bigr|\leq|L_1(s+i\tau)-g_1(s)|+|L_2(s+i\tau)-g_2(s)|<\tfrac{2m_0}3<|h(s)|,$$
y por Rouché $e^{-i\theta}L_1+e^{i\theta}L_2$ — luego $f$, que difiere en el factor no nulo
$\tfrac{\sec\theta}2$ — tiene un cero $\rho$ con $|\rho-(\sigma_0+i\tau)|<r/2$, es decir
$\delta_\rho=|\beta_\rho-\tfrac12|\in(\varepsilon-\tfrac\varepsilon4,\,\varepsilon+\tfrac\varepsilon4)
\subset[\tfrac\varepsilon2,\tfrac{3\varepsilon}2]$. Tomando $\tau$'s de $\mathcal T$ separados por
$\geq r=\tfrac\varepsilon2$ (sigue siendo un conjunto de cardinal $\gg_\varepsilon T$ en $[0,T]$ por la
densidad inferior positiva), los ceros obtenidos son distintos: $\gg_\varepsilon T$ ceros con
$\delta_\rho\asymp\varepsilon$ y $0<\gamma\leq T$. Como $\varepsilon$ es arbitrario,
$\liminf\delta_\rho=0$. $\square$

*Estatus de las citas.* La universalidad conjunta de $L(s,\chi_1),\dots,L(s,\chi_k)$ para caracteres
pairwise no equivalentes, en compactos $K$ de la franja $\tfrac12<\Re s<1$ con complemento conexo y blancos
continuos sin ceros en $K$, holomorfos en el interior, con densidad inferior positiva del conjunto de
$\tau$, es un teorema PUBLICADO de Voronin (1975, tesis y artículos; tratamiento de libro:
Karatsuba–Voronin, *The Riemann Zeta-Function*, De Gruyter 1992; Steuding, *Value-Distribution of
L-Functions*, Springer LNM 1877, 2007). El argumento universalidad+Rouché para producir $\gg T$ ceros de
combinaciones lineales en cualquier sub-franja es asimismo estándar y publicado: lo registran
Kaczorowski–Kulas (combinaciones de $L$-funciones, ceros fuera de la línea crítica) y, con cota
bilateral $\asymp T$ para series de Dirichlet con coeficientes periódicos sin Euler,
**Saias–Weingartner, Acta Arith. 140 (2009)**: para tales $f$, el número de ceros con
$\beta\in(\sigma_1,\sigma_2)$, $0<\gamma\leq T$ es $\asymp T$ **para toda** $\tfrac12<\sigma_1<\sigma_2\leq1$
— en particular con $\sigma_1$ arbitrariamente pegado a $\tfrac12$. [GAP de literatura: los enunciados
exactos de Kaczorowski–Kulas y la página precisa de Saias–Weingartner no fueron verificados al nivel de
página esta sesión; la Prop. 150.2 NO depende de ellos — depende solo de la universalidad conjunta de
Voronin, que es libro de texto. Los cito como corroboración independiente.]

*Nota interna decisiva:* el propio Doc 146 §3.2 invoca "universalidad de Voronin vale en toda la franja
crítica derecha $\tfrac12<\sigma<1$" para justificar el régimen de franja — sin advertir que ESA MISMA
universalidad, aplicada con $\sigma_1\downarrow\tfrac12$, produce la Prop. 150.2 y destruye su recuadro.
El argumento del §3.2 del Doc 146 ("eso requeriría que $L_1/L_2\to-e^{2i\theta}$ FORZADAMENTE al acercarse
a la línea, y no hay tal forzamiento — la línea no es especial para el cociente") confunde "no todos los
ceros colapsan a la línea" (cierto, y compatible con infinitos gordos) con "ningún cero se acerca a la
línea" (falso: como la línea no es especial para el cociente, la condición de fase se realiza TAMBIÉN
arbitrariamente cerca de ella — eso es exactamente lo que la universalidad da).

### 4.3. Errores secundarios del §3 del Doc 146 (registrados)

1. **Cálculo 146.A:** invoca "universalidad (Voronin) en cualquier franja $1<\sigma_1<\sigma<\sigma_2$" —
   la universalidad de Voronin vive en $\tfrac12<\sigma<1$, NO en $\sigma>1$. En $\sigma>1$ el mecanismo
   correcto es la casi-periodicidad de Bohr / densidad de Kronecker–Weyl de $(p^{-it})_p$ sobre el toro:
   el cociente $L_1/L_2$ sobre una vertical $\sigma_0>1$ tiene imagen con clausura determinada por los
   factores de Euler, y la condición de fase se realiza solo para $\sigma_0$ en un rango acotado
   ($1<\sigma_0<\sigma^*$): para $\sigma$ grande $|f-1|<1$ término dominante) y NO hay ceros — "cualquier
   franja $1<\sigma_1<\sigma_2$" es falso para $\sigma_1$ grande. La conclusión que el doc necesita
   (infinitos ceros con $\beta>1$) es [DH36] genuino y no se ve afectada.
2. **Resumen punto 3:** "la imagen $\{f(s):\sigma>1\}$ es densa" — falsa ($|f|$ está acotado sobre
   $\sigma\geq\sigma_1>1$); lo correcto es "$0$ pertenece a la clausura de la imagen de verticales
   $1<\sigma_0<\sigma^*$" (Bohr).
3. **§4.1/resumen:** "los ceros off se agrupan cerca de verticales fijas, no cerca de la línea" — la
   primera mitad es verdad PARA UNA SUBFAMILIA; la segunda mitad es falsa (Prop. 150.2: también se agrupan,
   con densidad $\gg T$, cerca de la línea — a CADA distancia $\varepsilon$).

### 4.4. Qué probó realmente el Doc 146, y el veredicto corregido

**[VEREDICTO GAP-141.DH CORREGIDO].**
- **Probado (incondicional, [DH36]):** D–H tiene infinitos ceros off con $\delta_j\geq\tfrac12$ ($\beta>1$).
  En consecuencia, para todo calendario no acotado $a$: $\delta_j a(\gamma_j)\geq\tfrac12 a(\gamma_j)\to\infty$
  sobre esa subsucesión ⟹ infinitos gordos ⟹ **D–H satisface LP-141$(a)$ para todo calendario no acotado**
  (sin la falla de constante de §3.2: aquí $\delta_j$ está acotado por abajo por la constante absoluta
  $\tfrac12$, así que el umbral $\geq1$ se alcanza en cuanto $a\geq2$, eventualmente para todo $a$ no
  acotado). Esto es lo que el programa necesitaba y queda en pie.
- **Refutado (Prop. 150.2):** $\liminf_j\delta_j>0$. D–H **NO** satisface la separación de banda
  ($\psi\asymp1$), ni "todos los off son gordos", ni el recuadro del §4.1 del Doc 146. El inciso
  "$\liminf|\beta-\tfrac12|\psi(\gamma)=+\infty$ para toda escala $\psi\to\infty$" del recuadro es
  igualmente falso tal como está cuantificado (el liminf corre sobre todos los off, incluidos los de la
  Prop. 150.2).
- **Abierto:** LP-134$^{(\log)}$ para D–H, i.e. $\liminf_j\delta_j\log\gamma_j>0$ — la pregunta que el
  Cor. 144.10 del Doc 144 realmente encargó (distinguir caso (b) de caso (d) de 144.9). La Prop. 150.2 da
  ceros con $\delta\asymp\varepsilon$ a alturas de densidad positiva PARA CADA $\varepsilon$ FIJO, pero
  para violar LP-134$^{(\log)}$ haría falta $\delta_\rho=o(1/\log\gamma_\rho)$ a lo largo de una sucesión —
  un régimen $\varepsilon=\varepsilon(T)\to0$ que requiere universalidad EFECTIVA (control del tamaño de la
  primera $\tau$ admisible en función de $\varepsilon$), no disponible en la literatura cualitativa.
  [GAP de literatura: no conozco resultados efectivos de acercamiento $\delta$ vs altura para D–H; no
  afirmo ninguno.]

En la taxonomía de la Prop. 144.9 del Doc 144: los casos (a) ($\inf\delta_j>0$) y (c) (sub-resolución
total) quedan **excluidos** (150.2 mata (a); [DH36] mata (c)); D–H está en (b) o en (d), **indecidido**.
Nótese que (b) y (d) son ambos "lado bueno" para el Cor. 144.10, así que la implicación lógica del Doc 144
("DH consistente con 144.D; no la confirma; el caso (d) sería evidencia de que LP-141 —no LP-134— es el
enunciado correcto") queda viva y sin cambio de signo. Lo que ya se puede decir: **D–H realiza "infinitos
gordos SIN separación de banda"** — la versión $\psi\asymp1$ de la separación LP-141/LP-134 instanciada en
la naturaleza. Si además (d) se confirmara ($\delta\log\gamma\to0$ en una subsucesión), D–H realizaría la
separación en la escala $\log$ misma, el "caso más informativo" de 144.9.

---

## 5. Consistencia 144↔146 y el estado final de "repulsión barata / falta pureza"

### 5.1. ¿Son consistentes "no decide LP-141 para ζ" (144) y "confirma LP-141 como cuasi-modelo" (146)?

Sí, son consistentes como lógica: el Doc 144 habla de **decisión** (DH$\notin$D131-H⁺ ⟹ ningún veredicto
sobre DH refuta ni prueba 144.D/LP-141 en la categoría Euler ni para ζ) y el Doc 146 habla de **evidencia
de caso** (un objeto $m=\infty$ con estructura casi-Euler que cumple LP-141). No hay contradicción formal.
Dos fricciones reales quedan:

1. **El Doc 146 contestó una pregunta distinta de la encargada.** El Cor. 144.10 pidió explícitamente
   "determinar cuál de los cuatro casos (a)/(b)/(c)/(d) ocurre, reportando $\liminf_j\delta_j\log\gamma_j$".
   El Doc 146 reportó (a) —y de hecho algo más fuerte— con soporte que solo da "no-(c)". Tras la
   corrección: el entregable real es "no-(a), no-(c), (b)∨(d) abierto".
2. **La retórica de §5 del Doc 146 sobre-generaliza:** "el frente se desplaza de '¿hay repulsión?'
   (**resuelto a favor en la categoría casi-Euler**)..." — un caso no resuelve una categoría (el propio
   Doc 146 lo reconoce en 4.2.3 y luego lo contradice en §5), y tras la Prop. 150.2 el contenido es el
   OPUESTO: en la categoría casi-Euler la repulsión-de-todos es FALSA (los ceros de D–H se acercan a la
   línea); lo que el caso D–H da es abundancia de gordos.

### 5.2. "Repulsión barata / falta pureza" — corregido

La separación del Doc 146 §4.3 sobrevive, pero con las palabras corregidas, y corregidas en una dirección
que FAVORECE al Doc 144:

- **Lo que el casi-Euler compra barato NO es "repulsión" sino "gordura abundante":** infinitos ceros off a
  distancia macroscópica (los $\beta>1$ de [DH36]). Eso es exactamente el insumo de LP-141, y solo eso.
- **Lo que el casi-Euler NO compra es la repulsión LP-134:** D–H tiene, junto a los gordos, ceros
  arbitrariamente pegados a la línea (Prop. 150.2). La cláusula (a) del §4.3 del Doc 146 ("D–H muestra que
  la repulsión de resolución no requiere Euler genuino... la parte '⟹ gordos' de 141.E es más barata de lo
  conjeturado") debe re-escribirse: *D–H muestra que "infinitos gordos" (LP-141) no requiere Euler genuino;
  y muestra a la vez que el casi-Euler NO da "todos repelidos" (LP-134-banda es falsa en D–H). Si 141.E es
  verdadera, la multiplicatividad genuina es load-bearing precisamente para la mitad que el casi-Euler
  pierde.* Esto **refuerza** la tesis central del Doc 144 (LP-141, no LP-134, es el pivote correcto, y
  144.D —que solo pide la subsucesión gorda— es el frente correcto): la naturaleza provee un objeto que
  separa las dos nociones en la dirección predicha, al menos en la escala $\psi\asymp1$.
- **La mitad "falta pureza" queda intacta:** D–H tiene gordos y $m=\infty$; lo exclusivo del Euler genuino
  sigue siendo el colapso $m\to0$ (pureza), no la gordura. Sin cambios.
- **La tabla de §3.3 del Doc 146** (fila D–H: "posición de los off: $\delta_j\geq\sigma_1-\tfrac12>0$,
  franja fija") debe corregirse a: "subfamilia infinita con $\delta_j\geq\tfrac12$ ($\beta>1$) + ceros con
  $\delta$ arbitrariamente pequeño (densidad $\gg T$ a cada distancia $\varepsilon$); veredicto:
  **LP-141 sí; separación de banda no; LP-134$^{(\log)}$ abierto**". La moraleja "la frontera
  sub-resolución/gordos coincide con la frontera sin-estructura/con-estructura" se degrada a: *la
  estructura (aun aproximada) garantiza la presencia de infinitos gordos; no impide acercamiento a la
  línea.*

### 5.3. Efecto neto sobre el programa

1. La ruta mínima de la mitad Fredholm queda, en su forma honesta:
   $$m<\infty\ \Longleftarrow\ \bigl[\sigma_{C\log}(Q)\ \text{débilmente positivo}\ \forall C\in\mathbb N\bigr]\ \wedge\ \text{144.D},$$
   con el cuantificador en $C$ explícito (consecuencia de §3.2–3.3; antes estaba oculto).
2. GAP-141.DH se re-abre en su mitad fina: el dato pendiente es $\liminf_j\delta_j\log\gamma_j$ para D–H
   (caso (b) vs (d)), que requiere o bien universalidad efectiva, o bien cómputo dirigido tipo [BS07] a
   alturas crecientes en franjas $\delta\asymp1/\log\gamma$. La mitad gruesa (LP-141 para D–H) está
   CERRADA a favor, incondicionalmente.
3. Ningún resultado de esta auditoría toca la Prop. 144.2/144.3 (la puerta analítica sigue cerrada para
   LP-141) ni la Prop. 144.8 (la frontera "infinitos gordos" sigue siendo el pivote).

---

## Mensaje final

**Veredictos.**
- **Doc 144:** Prop. 144.2 + Cor. 144.3 **[VERIFICADO]** (orden 1 exacto vía producto canónico en $w=z^2$ y
  Boas 2.6.5; $e^{A+Bs}$ inexistente por paridad; densidad $\asymp$, no $\sim$ — declarado; cuantificador
  $\forall a\,\exists F_a$ correcto y el único posible). Prop. 144.8 **[VERIFICADO]** contra E46.4 (usa
  5.3′/5.4 corregidos; matiz no portante en "(y estrictamente)"). Prop. 144.1(a) **[REFUTADA tal como está
  enunciada]** y Prop. 144.4 **[SOBRE-RECLAMADA]** — ambas reparables a nivel de clase $\{C\log\}$ con
  constante interna $C(F)$. Cadena 144.6 **[REPARABLE]**: separador del primer eslabón mal citado;
  separador correcto trivial (150.3). Conjetura 144.D bien formada pero casi-tautológica respecto de
  LP-141; la reducción es completa, sin "casi todo" oculto.
- **Doc 146:** veredicto fuerte "GORDOS ($\liminf\delta>0$, ni siquiera módulo $\log\gamma$)"
  **[REFUTADO]** (error liminf/limsup + Prop. 150.2 vía universalidad conjunta de Voronin + Rouché, con
  corroboración Saias–Weingartner). Sobrevive el enunciado débil **[VERIFICADO]**: D–H cumple LP-141 a todo
  calendario no acotado (infinitos $\beta>1$, [DH36]). La pregunta encargada por 144.10
  ($\liminf\delta\log\gamma$: caso (b) vs (d)) queda **ABIERTA**.
- **Consistencia 144↔146:** sin contradicción formal; el Doc 146 contestó una pregunta más fuerte que la
  encargada y la contestó mal; "repulsión barata" debe re-escribirse como "gordura barata, repulsión no" —
  corrección que refuerza la tesis del Doc 144 (LP-141 es el pivote, no LP-134).

**Tres hallazgos principales.**

1. **[REFUTACIÓN — Doc 146] El veredicto fuerte de GAP-141.DH es falso.** El paso "infinitos ceros en una
   franja fija ⟹ $\liminf_{\text{todos los off}}\delta\geq\sigma_1-\tfrac12$" acota un liminf con una
   subfamilia (confusión liminf/limsup — la misma distinción atómica LP-134/LP-141 que el Doc 144
   formaliza). Y no es solo falta de soporte: la universalidad conjunta de Voronin (que el propio Doc 146
   §3.2 invoca) + Rouché dan, para cada $\varepsilon$, $\gg_\varepsilon T$ ceros de D–H con
   $\delta_\rho\asymp\varepsilon$ (Prop. 150.2, prueba cerrada): $\liminf\delta_\rho=0$. Queda en pie lo
   que LP-141 necesita: infinitos gordos ($\beta>1$, [DH36]) — D–H cumple LP-141, no la separación de
   banda; LP-134$^{(\log)}$ para D–H sigue abierto (el dato (b)-vs-(d) que 144.10 pidió no está decidido).
2. **[CONTRAEJEMPLO — Doc 144] La invariancia por constantes de la clase $\{C\log\}$ es falsa para LP-141,
   y con ella caen los enunciados literales de 144.1(a) y de la "forma fuerte" de 144.4.** La configuración
   $\delta_j=1/(2\psi(\gamma_j))$ cumple LP-134$^{(\psi)}$ y viola LP-141$(\psi)$ (Contraejemplo 150.1): el
   liminf absorbe constantes, el umbral "$\geq1$" no. Reparación: LP-134$^{(\psi)}\Rightarrow\exists C:
   \mathrm{LP\text{-}141}(C\psi)$, y 144.D $\Rightarrow\mathrm{LP\text{-}141}(C(F)\log)$ con $C(F)$ interna
   a la función — la constante interna al mundo de 141.A/P43 reaparece (en miniatura) dentro del propio
   pivote, y la sinergia honesta exige positividad débil del símbolo sobre toda la familia
   $\{C\log\}_{C\in\mathbb N}$, no sobre un calendario único.
3. **[REPARACIÓN — Doc 144] La cadena de fuerza 144.6 tiene el primer separador mal citado** (141.P4(iii)
   da LP-141⟹̸Axioma R, que no separa Axioma R ≻ LP-134); el separador correcto es trivial y queda probado
   acá (Prop. 150.3: la configuración cosh de un cuádruplo cumple LP-134 por la convención de finitud y
   viola "$m\geq1\Rightarrow\infty$ gordos"). Con 150.1+150.3 la cadena queda estricta y con separadores
   completos — a nivel de clase de calendario. Las dos piezas estructurales del Doc 144 que el programa
   carga (144.2/144.3: LP-141 es no-analítico para todo calendario; 144.8: "≥1 gordo" no basta, el pivote
   mínimo es "infinitos gordos") sobreviven la auditoría íntegras.

---

## Referencias

**Internas (backward-only):** Doc 144 (Props. 144.1/144.2/144.4/144.6/144.8/144.9, Cor. 144.3/144.10,
Conjetura 144.D, GAP-144.C); Doc 146 (Defs. 146.1/146.2, Hechos 146.3–146.7, Cálculo 146.A, veredicto
§4.1); Doc 141 (Teorema 141.A, Def. 141.1/141.2, Props. 141.P1/P3/P4, 141.R1/R2, Cálculo 141.R3, Conjetura
141.E, GAP-141.DH); Doc 134 (Defs. 3.1/3.6/4.1/4.2/4.4, Lemas 3.2/3.3/5.0, Teoremas 5.1–5.5, Prop. 5.5bis,
§5.8 M1–M2); ERRATA 06-papers/ERRATA.md E46.4 (Thm 5.3′; caso degenerado 5.2(iv); caveat B.4).

**Literatura (publicada, verificable):**
- [B54] R. P. Boas, *Entire Functions*, Academic Press, 1954. (Thm. 2.6.5: orden de un producto canónico =
  exponente de convergencia — usado en §1.1.)
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series* I, II, J. London Math.
  Soc. **11** (1936), 181–185 y 307–312. (Infinitos ceros con $\beta>1$ — soporte del enunciado débil.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. Heath-Brown), Oxford,
  1986, §10.25. (La función D–H, su ecuación funcional, sus ceros off.)
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math.
  Comp. **76** (2007), 2045–2049. (Testigo $\rho^*\approx0.8085+i\,85.699$.)
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66**
  (2011), 221–270. (Panorama; distribución de ceros en $\sigma\geq1$.)
- [V75-joint] S. M. Voronin, universalidad (1975) y universalidad conjunta de $L$-funciones de Dirichlet
  para caracteres no equivalentes; tratamiento de libro en [KV92] y [St07]. (Motor de la Prop. 150.2.)
- [KV92] A. A. Karatsuba, S. M. Voronin, *The Riemann Zeta-Function*, De Gruyter, 1992. (Cap. de
  universalidad; forma citada del teorema conjunto.)
- [St07] J. Steuding, *Value-Distribution of L-Functions*, Springer Lecture Notes in Math. **1877**, 2007.
  (Thm. 1.10 universalidad conjunta; método universalidad+Rouché para ceros de combinaciones.)
- [SW09] E. Saias, A. Weingartner, *Zeros of Dirichlet series with periodic coefficients*, Acta Arith.
  **140** (2009), 335–344. (Ceros $\asymp T$ en toda franja $\tfrac12<\sigma_1<\sigma_2\leq1$ para series
  periódicas sin Euler — corroboración independiente de la Prop. 150.2. [Enunciado citado de memoria;
  verificación al nivel de página pendiente — la Prop. 150.2 no depende de él.])
- J. Kaczorowski, M. Kulas, sobre ceros fuera de la línea crítica de combinaciones lineales de
  $L$-funciones (Monatsh. Math., ca. 2007). [GAP de literatura: referencia exacta no verificada esta
  sesión; citada solo como corroboración, no como premisa.]

*Fin del Doc 150.*
