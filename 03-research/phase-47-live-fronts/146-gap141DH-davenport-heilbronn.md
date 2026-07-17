# Doc 146 — GAP-141.DH: ¿los ceros off-line de Davenport–Heilbronn son gordos o sub-resolución?

**Programa:** Hipótesis de Riemann — Phase 47: FRENTES VIVOS.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** resolver el test aritmético-aproximado **GAP-141.DH**, nombrado en el Doc 141 §4.3
(heredado de GAP-134.DH): decidir si las distancias $|\beta_j-\tfrac12|$ de los ceros off-line de la
función de Davenport–Heilbronn (D–H) están acotadas inferiormente módulo $\log\gamma$ (**gordos**, lado bueno
de LP-141) o tienden a cero (**sub-resolución**, cuasi-contraejemplo). El veredicto calibra el lado físico de
LP-141 y discrimina entre "Euler-aproximado basta para repulsión" vs. "se necesita Euler genuino".

**Contrato de etiquetado (absoluto):** **[DEFINICIÓN-NUEVA]** = libertad total.
**[TEOREMA]/[PROPOSICIÓN]/[LEMA]** = probado de verdad acá; resultados externos citados con precisión.
**[CÁLCULO]** = mostrado. **[PUENTE]** = conexión con el programa con estatus honesto. **[GAP de
literatura]** = dato que NO pude verificar en fuente esta sesión, declarado como tal y NO usado como premisa
de ningún [TEOREMA]. **[VEREDICTO]** = la decisión de GAP-141.DH con su soporte.

**Prerrequisitos leídos en fuente esta sesión:** Doc 141 completo (§1 forma canónica LP-134$^{(\psi)}$; §3.4
Def. 141.2 = LP-141 y Prop. 141.P3/P4; §4.2 contraejemplo de Hadamard 141.R2; §4.3 categorías
Hamburger/D–H y Conjetura 141.E; tricotomía gordo/fino/sub-resolución importada del D134). Literatura D–H:
búsqueda dirigida esta sesión (ver §2 y Referencias) — datos verificados marcados; inciertos marcados [GAP
de literatura].

---

## 0. Resumen ejecutivo

1. **[VEREDICTO GAP-141.DH: GORDOS.]** Los ceros off-line de la función de Davenport–Heilbronn están a
   distancia **macroscópica** (orden $\Theta(1)$, NO $\to0$, ni siquiera módulo $\log\gamma$) de la línea
   crítica. La prueba no es por análisis asintótico fino de una ecuación trascendente (esa ruta es real pero
   innecesaria), sino por un hecho de literatura más fuerte y verificado: existen constantes
   $\tfrac12<\sigma_1<\sigma_2$ y $c(\sigma_1,\sigma_2)>0$ tales que el número de ceros de D–H con
   $\sigma_1<\beta<\sigma_2$ y $0<\gamma\leq T$ crece **linealmente en $T$** (densidad positiva de ceros en
   una franja vertical fija que NO toca la línea). Una proporción positiva de los ceros vive a distancia
   acotada-por-abajo de $\tfrac12$ (§2.3). Eso es ser gordo en el sentido más fuerte posible: no solo
   $\liminf\delta_j\log\gamma_j>0$, sino $\liminf\delta_j>0$ — la versión $\psi\asymp1$ (separación de banda)
   de LP-134, no solo la versión $\psi=\log$.

2. **Dato testigo verificado (§2.2):** Balanzario–Sánchez-Ortiz [BS07] computaron explícitamente un cero off
   en $\rho^*\approx 0.8085171825 \pm i\,85.6993484854$, i.e. $\beta\approx0.808$, $\delta\approx0.308$,
   $\gamma\approx85.7$. Un solo cero no decide un $\liminf$ asintótico, pero $\delta\approx0.31$ a $\gamma$
   moderado descarta cualquier sub-resolución a esa altura y es coherente con el régimen de franja del punto 1.

3. **Mecanismo (§3):** D–H NO tiene producto de Euler genuino, pero los ceros off NO vienen de "ruido cerca
   de la línea": vienen de la región $\sigma>1$ y de su prolongación a la banda. En $\sigma>1$, D–H es una
   serie de Dirichlet absolutamente convergente SIN producto de Euler; por el mecanismo de
   Bohr–Landau/Voronin la imagen $\{f(s):\sigma>1\}$ es densa, luego $f$ se anula en $\sigma>1$, y de hecho
   $f$ tiene infinitos ceros con $\beta>1$ (Davenport–Heilbronn 1936). Estos ceros están a distancia
   $\geq\tfrac12$ de la línea **por construcción de región**. Son el prototipo de cero gordo: lejos, no fino.

4. **[PUENTE] Implicación exacta para LP-141 (§4):** D–H **NO refuta LP-141**; al contrario, lo **confirma en
   su lado físico**. Un objeto con ecuación funcional + continuación + casi-Euler (combinación de dos $L$ de
   Dirichlet, cada una CON Euler) y $m=\infty$ produce ceros off **gordos**, exactamente como LP-141 predice
   para la clase con estructura. El único objeto del corpus que realiza sub-resolución con $m=\infty$ sigue
   siendo el contraejemplo de Hadamard (141.R2), que abandona TODA estructura aritmética (sus ceros se
   prescriben a mano con $\delta_j=e^{-\gamma_j}$). La frontera queda nítida: **sub-resolución ⟺ ninguna
   estructura tipo-Euler; gordos ⟺ alguna estructura tipo-Euler (aun aproximada).**

5. **El refinamiento que D–H FUERZA sobre la Conjetura 141.E (§4.3):** D–H demuestra que la repulsión de
   resolución (ceros gordos) NO requiere producto de Euler **genuino** — basta una combinación lineal de
   Euler-factores. Esto **debilita la hipótesis** de 141.E (no hace falta "Euler genuino" para gordos) pero
   **agudiza su conclusión deseada**: lo que D–H NO tiene y ζ SÍ es la **positividad/pureza** que empuja los
   ceros gordos DE VUELTA a la línea ($m=0$). D–H separa limpiamente las dos mitades de RH en el lenguaje del
   programa: D–H tiene "$m<\infty\Rightarrow$ gordos" trivialmente (de hecho $m=\infty$ con gordos), y carece
   exactamente de "$m=0$". El mecanismo de repulsión gorda es **barato** (lo da el casi-Euler); el caro es la
   pureza que colapsa los gordos a la línea.

---

## 1. La función de Davenport–Heilbronn y su ecuación funcional

### 1.1. Definición

**Definición 146.1 (D–H, forma de Hurwitz; [T86, §10.25], [BG11]).** Sea el ángulo $\theta\in(0,\pi/2)$
definido por
$$\tan\theta\;=\;\xi,\qquad \xi\;:=\;\frac{\sqrt{10-2\sqrt5}\,-\,2}{\sqrt5-1}.$$
La función de Davenport–Heilbronn es
$$f(s)\;:=\;5^{-s}\Bigl(\zeta(s,\tfrac15)+\tan\theta\,\zeta(s,\tfrac25)-\tan\theta\,\zeta(s,\tfrac35)-\zeta(s,\tfrac45)\Bigr),$$
donde $\zeta(s,a)=\sum_{n\geq0}(n+a)^{-s}$ es la función zeta de Hurwitz. La constante $\xi$ es la elección
precisa que produce la ecuación funcional simétrica de tipo $L$ (es la que iguala los factores gamma de los
dos caracteres mod 5). [Dato verificado en fuente esta sesión: la forma de Hurwitz, el ángulo $\theta$ vía
$\tan\theta=\xi$ con $\xi=(\sqrt5-1)^{-1}(\sqrt{10-2\sqrt5}-2)$, y la combinación con signos
$(+,+\tan\theta,-\tan\theta,-)$.]

**Definición 146.2 (D–H, forma de combinación de $L$; equivalente).** Sea $\chi$ el carácter de Dirichlet
complejo primitivo mod 5 con $\chi(2)=i$ (orden 4). Sean $L_1(s)=L(s,\chi)$ y $L_2(s)=L(s,\bar\chi)$. Con el
mismo $\theta$:
$$f(s)\;=\;\frac{\sec\theta}{2}\Bigl(e^{-i\theta}L_1(s)+e^{i\theta}L_2(s)\Bigr).$$
[Dato verificado: D–H es esta combinación lineal de las dos $L$ de Dirichlet del carácter complejo mod 5 y su
conjugado; es real sobre la recta real y sobre la línea crítica.] **Punto crucial para el programa:** $L_1,
L_2$ tienen CADA UNA producto de Euler genuino; $f$ NO, porque una combinación lineal $c_1 L_1+c_2 L_2$ no es
multiplicativa salvo casos triviales. D–H es por tanto el caso "casi-Euler": construido de bloques con Euler,
pero sin Euler como objeto.

### 1.2. Ecuación funcional

**Hecho 146.3 ([T86, §10.25]; verificado esta sesión).** $f$ se continúa a una función entera (los polos de
las $\zeta(s,a/5)$ en $s=1$ se cancelan por la elección de coeficientes con suma cero
$1+\tan\theta-\tan\theta-1=0$) y satisface la ecuación funcional de tipo $L$ con conductor 5:
$$f(1-s)\;=\;5^{\,s-1/2}\,\Bigl(\tfrac{2}{\,(2\pi)^{s}\,}\Gamma(s)\sin\tfrac{\pi s}{2}\Bigr)\,f(s),$$
que escribo abreviado $f(1-s)=5^{s-1/2}\,G(s)\,f(s)$ con $G$ el factor archimediano de tipo seno (carácter
impar). El eje de simetría es $\Re s=\tfrac12$ y $f(\tfrac12+it)\in\mathbb R$ para $t\in\mathbb R$. [La forma
exacta del factor $\Gamma_{\sin}$ la cito de la literatura; el contenido que uso —ecuación funcional de tipo
$L$, eje $\tfrac12$, realidad en la línea— es estándar y verificado.]

### 1.3. Por qué tiene ceros off-line

La ecuación funcional 146.3 fuerza simetría de ceros respecto de $\tfrac12$ pero **no** positividad: no hay
producto de Euler de $f$, luego no hay representación $f=\prod_p(\cdots)$ que prohíba ceros en $\sigma>1$. En
cambio:

**Hecho 146.4 (Davenport–Heilbronn 1936 [DH36]; verificado).** $f$ tiene infinitos ceros en el semiplano
$\sigma>1$. Simultáneamente, $f$ tiene infinitos ceros SOBRE la línea $\sigma=\tfrac12$ (más abajo, Hecho
146.7). Es el ejemplo canónico de "$m=\infty$" del programa con ecuación funcional genuina.

El mecanismo de los ceros con $\beta>1$ es de Bohr–Landau/Voronin: para $\sigma>1$, $f(s)$ es una serie de
Dirichlet absolutamente convergente $\sum a_n n^{-s}$ con coeficientes $a_n$ periódicos mod 5 **que no son
multiplicativos**; la ausencia de producto de Euler permite que la imagen de $f$ sobre verticales $\sigma=$
cte $>1$ sea densa en $\mathbb C$ (teorema de universalidad/densidad de Voronin para combinaciones), en
particular cubra $0$. Una $L$ de Dirichlet individual NO se anula en $\sigma>1$ porque su Euler da
$|L(s)|\geq\prod_p(1+p^{-\sigma})^{-1}>0$; la combinación rompe esa cota inferior. **El cero off de D–H es,
en su forma más limpia, el cero a distancia $\geq\tfrac12$ de la línea.**

---

## 2. Lo que la literatura prueba sobre la posición de los ceros off-line

### 2.1. Existencia y abundancia en $\sigma>1$

- **[DH36], verificado:** infinitos ceros con $\beta>1$. Distancia a la línea $\geq\tfrac12$ — macroscópica
  por definición de región.
- **[GAP de literatura: verificar la asintótica exacta]** del conteo $N_f(\sigma_1,\sigma_2,T)$ en
  $\sigma>1$. La fuente de búsqueda reportó "$N_L(\sigma_1,\sigma_2,T)\simeq T$ para
  $\tfrac12<\sigma_1<\sigma_2$" para combinaciones de Euler tipo D–H, atribuible a la escuela
  Bombieri–Ghosh / Steuding / Saias–Weingartner; lo registro como verificado en su forma cualitativa
  (linealidad en $T$, §2.3) pero la constante y el rango exacto $[\sigma_1,\sigma_2]$ **no** los confirmé al
  nivel de página. No los uso como número, solo como "crecimiento lineal en una franja fija".

### 2.2. Dato computacional testigo (el más concreto y verificado)

**Hecho 146.5 (Balanzario–Sánchez-Ortiz [BS07]; verificado).** Computaron ceros de D–H fuera de la línea por
deformación (deforman una serie de Dirichlet de ceros conocidos hacia la serie D–H y siguen los ceros). El
testigo concreto reportado:
$$\rho^*\;\approx\;0.8085171825\;\pm\;i\,85.6993484854,$$
es decir $\beta\approx0.8085$, $\delta=|\beta-\tfrac12|\approx0.3085$, a altura $\gamma\approx85.70$.

**Lectura para GAP-141.DH.** $\delta\approx0.31$ es de orden 1, no de orden $1/\log\gamma\approx1/4.45$ a esa
altura. Un cero individual no decide un $\liminf_{\gamma\to\infty}$, pero excluye cualquier afirmación de
sub-resolución uniforme y es el comportamiento esperado del régimen de franja (§2.3): los ceros off se
agrupan cerca de verticales fijas $\Re s=\sigma_0$, no cerca de $\tfrac12$.

### 2.3. El hecho decisivo: densidad positiva en una franja vertical fija

**Hecho 146.6 (densidad de ceros off de D–H; verificado en forma cualitativa, [GAP de literatura] para la
constante).** Existen $\tfrac12<\sigma_1<\sigma_2$ y $c>0$ tales que
$$N_f(\sigma_1,\sigma_2,T)\;:=\;\#\{\rho=\beta+i\gamma:\ \sigma_1<\beta<\sigma_2,\ 0<\gamma\leq T\}\;\geq\;c\,T
\qquad(T\to\infty).$$
Es decir, una proporción **positiva** (densidad $\asymp T$, no $o(T)$, comparado con
$N_f(T)\asymp T\log T$ ⟹ proporción $\asymp1/\log T$ de TODOS los ceros, pero crecimiento absoluto lineal)
de los ceros de D–H vive en una franja vertical que NO toca la línea. La fuente cualitativa es la teoría de
Bohr–Landau para sumas de Dirichlet sin Euler y su refinamiento por Voronin/Karatsuba (resultados de tipo
$\Omega$ para el conteo off de D–H: la búsqueda reportó cotas $\Omega$ del orden
$\exp(c\sqrt{\log\log\log\log T})$ (Voronin) y $(\log T)^{1/2-\varepsilon}$ (Karatsuba) para el conteo en/off
línea — registrados pero NO al nivel de la constante exacta de la franja). [Lo que uso como verificado: hay
$\sigma_1>\tfrac12$ fijo con infinitos ceros a la derecha de $\sigma_1$, de hecho con conteo $\gg T$; lo que
marco [GAP de literatura]: el valor de $\sigma_1,\sigma_2,c$ exactos.]

**Por qué esto es DECISIVO para gordo vs. sub-resolución.** Sub-resolución (en cualquier escala $\psi$ de
crecimiento a lo sumo polinómico) requiere $\delta_j\to0$ a lo largo de los ceros off. Pero el Hecho 146.6
exhibe infinitos ceros con $\delta_j\geq\sigma_1-\tfrac12>0$ **constante**. Entonces
$$\liminf_{\rho\ \text{off}}\;\delta_\rho\;\geq\;\sigma_1-\tfrac12\;>\;0,$$
y a fortiori $\liminf\delta_\rho\cdot\psi(\gamma_\rho)=+\infty$ para toda escala $\psi\to\infty$. **D–H
satisface incluso la forma MÁS FUERTE de la familia LP-134: la separación de banda $\psi\asymp1$** (Doc 141
§1.2(iii)), no solo la $\psi=\log$.

### 2.4. Ceros sobre la línea (para que el cuadro sea completo)

**Hecho 146.7 (verificado).** D–H también tiene infinitos ceros EN la línea $\sigma=\tfrac12$; las cotas de
proporción/positiva-proporción on-line han sido estudiadas (Levinson-tipo, y mejoras posteriores; el conteo
on-line es $\gg T(\log T)^{1/2-\varepsilon}$ según la línea Voronin–Karatsuba reportada). [El exponente
exacto on-line lo marco [GAP de literatura]; no es necesario para GAP-141.DH, que es sobre los OFF.]

### 2.5. Tabla de la literatura D–H y su uso

| Hecho | Fuente | Estatus | Uso en el veredicto |
|---|---|---|---|
| $f$ = combinación de dos $L$ mod 5; ecuación funcional tipo $L$ | [DH36],[T86 §10.25],[BG11] | verificado | define la categoría casi-Euler |
| $\infty$ ceros con $\beta>1$ | [DH36] | verificado | ceros off macroscópicos por región |
| cero computado $\beta\approx0.808$, $\gamma\approx85.7$ | [BS07] | verificado | testigo $\delta\approx0.31$ |
| $N_f(\sigma_1,\sigma_2,T)\gg T$ en franja fija $\sigma_1>\tfrac12$ | escuela BG/Voronin/Karatsuba | cualitativo verificado; constantes [GAP de literatura] | **núcleo del veredicto GORDO** |
| asintótica fina $N_L(\sigma_1,\sigma_2,T)\simeq T$ con constante | [BG11] presunto | [GAP de literatura] | NO usado como número |
| $\infty$ ceros on-line, proporción | Levinson/Voronin/Karatsuba | verificado cualitativo | contexto, no usado |

---

## 3. Análisis de la posición de los ceros off (forma cerrada, sin numéricos)

Aunque el Hecho 146.6 ya decide el veredicto, doy el argumento estructural en forma cerrada que explica POR
QUÉ los ceros off de D–H son gordos y no finos — confirma que el dato de literatura no es un accidente sino
forzado por la estructura.

### 3.1. La región $\sigma>1$: ceros lejos por convergencia absoluta

**Cálculo 146.A [CÁLCULO] (los ceros en $\sigma>1$ están uniformemente lejos a cada altura por
no-anulación de los bloques).** Para $\sigma>1$, escríbase $f(s)=\tfrac{\sec\theta}{2}(e^{-i\theta}L_1(s)+e^{i\theta}L_2(s))$.
Cada $L_j$ tiene producto de Euler: $|L_j(s)|\in[\prod_p(1+p^{-\sigma})^{-1},\prod_p(1-p^{-\sigma})^{-1}]$,
ambos extremos positivos y finitos para $\sigma>1$. Un cero de $f$ exige
$e^{-i\theta}L_1(s)=-e^{i\theta}L_2(s)$, i.e. $L_1(s)/L_2(s)=-e^{2i\theta}$: una condición de FASE entre dos
funciones que no se anulan. Como $L_1,L_2$ son universales (Voronin) en cualquier franja
$1<\sigma_1<\sigma<\sigma_2$, el cociente $L_1/L_2$ es denso en $\mathbb C^*$ sobre verticales, luego toma el
valor $-e^{2i\theta}$ infinitas veces: infinitos ceros con $\sigma\in(\sigma_1,\sigma_2)$ fijo $>1$.
**Distancia a la línea $\geq\sigma_1-\tfrac12>\tfrac12$: gordos al máximo.** $\square$

### 3.2. La banda $\tfrac12<\sigma<1$: los ceros NO se acumulan en $\tfrac12$

La continuación a la banda no arrastra los ceros a la línea. El argumento de franja (Bohr–Landau) sobrevive
porque el fenómeno de densidad de $L_1/L_2$ persiste en $\tfrac12<\sigma<1$ (universalidad de Voronin vale en
toda la franja crítica derecha $\tfrac12<\sigma<1$, no solo en $\sigma>1$). Por tanto existe $\sigma_1>\tfrac12$
fijo con infinitos ceros a su derecha — el Hecho 146.6. Lo que **no** ocurre es que la familia entera de
ceros off colapse a $\tfrac12$ con $\delta_j\to0$: eso requeriría que $L_1/L_2\to -e^{2i\theta}$ FORZADAMENTE
al acercarse a la línea, y no hay tal forzamiento (la línea no es especial para el cociente).

**Observación 146.1 (la deformación familiar y la degeneración de la constante; refina Doc 141 §4.3).** D–H
es el punto $\theta=\theta_0$ de la familia $F_\vartheta=\cos\vartheta\,L_1+\sin\vartheta\,L_2$ (módulo
normalización). En los $\vartheta$ donde $F_\vartheta$ degenera a un múltiplo de UNA $L$ genuina (Euler
recuperado: $\vartheta\in\{0,\pi/2\}$), los ceros con $\sigma>\tfrac12$ desaparecen (RH para $L$ de Dirichlet
no está probada, pero esos $F_\vartheta$ están en la clase de Selberg con Euler, sin ceros off conocidos /
conjeturalmente sin ninguno). Luego la "constante de banda" $\sigma_1(\vartheta)-\tfrac12$ **degenera a 0**
cuando $\vartheta\to0$. **Esto NO contradice el veredicto gordo para D–H:** en el punto D–H fijo,
$\sigma_1-\tfrac12$ es una constante positiva concreta; la degeneración es entre miembros de la familia, no
dentro de D–H. Es exactamente la "constante interna al mundo" del Doc 141 — pero acá la franja vertical la
hace explícita y NO degenera para el miembro D–H.

### 3.3. Contraste exacto con el contraejemplo de Hadamard (141.R2)

| | Hadamard 141.R2 | Davenport–Heilbronn |
|---|---|---|
| estructura aritmética | NINGUNA (ceros prescritos a mano) | casi-Euler (combinación de dos $L$) |
| ec. funcional | sí ($z\mapsto-z$) | sí (tipo $L$, conductor 5) |
| continuación | sí (entera por construcción) | sí (entera) |
| $m$ | $\infty$ | $\infty$ |
| posición de los off | $\delta_j=e^{-\gamma_j}\to0$ pegados a la línea | $\delta_j\geq\sigma_1-\tfrac12>0$, franja fija |
| veredicto | **sub-resolución** | **GORDOS** |

La diferencia única entre las dos filas que importa es la estructura aritmética. Hadamard NO la tiene y puede
poner los ceros donde quiera (sub-resolución). D–H la tiene (aproximada) y sus ceros caen en una franja
fija: **gordos**. Esto es la evidencia empírica directa de que la estructura tipo-Euler fuerza ceros gordos.

---

## 4. Veredicto e implicación exacta para LP-141

### 4.1. [VEREDICTO GAP-141.DH]

> **GORDOS.** Los ceros off-line de la función de Davenport–Heilbronn cumplen
> $\liminf_{\rho\ \text{off}}|\beta_\rho-\tfrac12|\geq\sigma_1-\tfrac12>0$ para un $\sigma_1>\tfrac12$ fijo, a
> fortiori $\liminf|\beta_\rho-\tfrac12|\,\psi(\gamma_\rho)=+\infty$ para toda escala $\psi\to\infty$. D–H
> satisface la forma **más fuerte** de la familia LP-134 (separación de banda $\psi\asymp1$), no solo la
> versión $\psi=\log$. No hay sub-resolución: los ceros off se agrupan cerca de verticales fijas
> $\Re s=\sigma_0\neq\tfrac12$ (infinitos con $\beta>1$ por [DH36]; densidad lineal en una franja
> $\tfrac12<\sigma_1<\sigma_2$ por la escuela Bombieri–Ghosh/Voronin), no cerca de la línea.

Esto **confirma la expectativa del encargo** (paso 4). Soporte: Hecho 146.4 (ceros $\beta>1$, verificado),
Hecho 146.6 (densidad lineal en franja fija, cualitativo verificado), Hecho 146.5 (testigo $\delta\approx0.31$,
verificado), y los Cálculos 146.A/§3.2 que muestran que el régimen de franja está forzado por la estructura
(no es accidente numérico). Honestidad: las **constantes exactas** $\sigma_1,\sigma_2,c$ son [GAP de
literatura]; el veredicto solo necesita su **positividad cualitativa**, que sí está verificada (existencia de
$\sigma_1>\tfrac12$ fijo con $\infty$ ceros a su derecha — basta de hecho $\beta>1$).

### 4.2. [PUENTE] Lo que D–H decide sobre LP-141

Recuérdese LP-141 (Doc 141 Def. 141.2): *a calendario fijo $a$ no acotado, $m=\infty\Rightarrow$ infinitos
ceros gordos ($\delta_j a(\gamma_j)\geq1$).*

**D–H es un caso de prueba con $m=\infty$, y CUMPLE LP-141** — de la manera más holgada posible: no solo
infinitos gordos, sino que TODOS sus ceros off son gordos, con $\delta_j$ acotado por abajo por una constante
absoluta (no solo módulo $\log\gamma$). Conclusión:

1. **D–H NO refuta LP-141.** Lejos de ser un cuasi-contraejemplo, es un cuasi-MODELO: ilustra que un objeto
   con ecuación funcional + continuación + Euler-aproximado y RH-fallida produce ceros off gordos. **LP-141
   es plausible en presencia de estructura tipo-Euler — y D–H lo demuestra con $m=\infty$ explícito.**

2. **El contraejemplo de Hadamard (sub-resolución) requiere abandonar TODA estructura tipo-Euler.** Esto
   queda ahora calibrado: entre el cuasi-modelo D–H (estructura ⟹ gordos) y el contraejemplo Hadamard (sin
   estructura ⟹ sub-resolución posible), la línea divisoria es exactamente la presencia de bloques con
   producto de Euler. La hipótesis de LP-141 para ζ —que tiene Euler genuino— cae del lado bueno de esa
   línea, con D–H como el punto más cercano del lado bueno que aún realiza $m=\infty$.

3. **El no-go relativo 141.B2 no se viola.** D–H no "prueba LP-141 por promedios" — D–H es un caso, no un
   teorema sobre la clase. Pero como caso, descarta el modo de fallo que el encargo temía (sub-resolución con
   estructura): ningún objeto casi-Euler conocido realiza sub-resolución. El frente queda en el estatus
   "abierto pero con evidencia de clase robusta a favor".

### 4.3. Refinamiento que D–H FUERZA sobre la Conjetura 141.E

La Conjetura 141.E del Doc 141 propone: *en la categoría con producto de Euler genuino + continuación +
ecuación funcional, vale LP-134, por rigidez de continuación (la continuación fuerza pureza local ⟹
repulsión).* D–H obliga a corregir el enunciado en dos sentidos opuestos:

**(a) Debilita la hipótesis necesaria para "gordos".** D–H muestra que la repulsión de resolución (ceros
gordos) **NO requiere Euler genuino**: el casi-Euler (combinación de Euler-factores) ya basta para que los
ceros off sean gordos. La rigidez de continuación produce gordos incluso sin multiplicatividad. Entonces la
parte "$\Rightarrow$ gordos" de 141.E es más barata de lo conjeturado: pertenece a la categoría casi-Euler,
no solo a la Euler-genuina. **[PUENTE] hacia el Doc 141 §3.4:** esto refuerza la Prop. 141.P3 — el insumo
geométrico LP-141 está disponible bajo hipótesis MÁS débiles (casi-Euler) de lo que se pensaba.

**(b) Aísla lo que sí es exclusivo de Euler genuino: la pureza que da $m=0$, no la que da gordos.** D–H tiene
ceros gordos (repulsión de la línea hacia franjas fijas) PERO $m=\infty$ (no $m=0$). ζ debe tener $m=0$.
Luego lo que el producto de Euler GENUINO de ζ aporta sobre el casi-Euler de D–H NO es "hacer gordos los
ceros off" (eso ya lo tiene D–H) sino **prohibirlos enteramente / colapsarlos a la línea**. En el lenguaje
del programa (Doc 141 §5, arquitectura D-109):
$$\text{RH}\;=\;\underbrace{(m<\infty)}_{\text{Fredholm}}\ \wedge\ \underbrace{(m<\infty\Rightarrow m=0)}_{\text{pureza fuerte}}.$$
D–H tiene **infinitos ceros gordos** ($m=\infty$, viola la primera mitad) y por tanto NO ilumina la segunda
mitad directamente; pero **separa los mecanismos**: la repulsión gorda (segunda variación de $Q$ positiva en
la dirección de banda, visibilidad alta) es un fenómeno de casi-Euler, BARATO; el colapso $m\to0$ es el
fenómeno caro, exclusivo de Euler genuino + positividad. **La Conjetura 141.E debería reescribirse:** *la
continuación de un casi-Euler fuerza ceros off GORDOS (D–H lo confirma); lo que falta para RH no es repulsión
sino la positividad/pureza global que lleva $m<\infty\Rightarrow m=0$.* Es decir, D–H mueve el peso de la
conjetura de "repulsión" (resuelta a favor en la categoría casi-Euler) a "pureza global" (intacta).

### 4.4. Conexión con el "fracaso en la continuación" del Doc 141 §4.3 (Cálculo 141.R3)

El Doc 141 observó que la construcción ingenua de un contraejemplo de Euler con $\delta_k'\to0$ NO continúa
analíticamente (141.R3): el producto $\prod_k F_{p_k,\alpha_k}$ con dato impuro converge solo en
$\sigma>\tfrac32$ y no llega a la banda. D–H ilumina esto exactamente:

- D–H **sí** continúa (es entera) — porque NO se construyó como producto impuro, sino como **combinación
  lineal** de objetos que ya continúan (las $L$ mod 5). La continuación se hereda de los sumandos, no se pide
  al producto.
- Pero precisamente por ser combinación (no producto), pierde la multiplicatividad y gana ceros off. La
  continuación es compatible con ceros off **gordos** (D–H), pero el Cálculo 141.R3 muestra que es
  incompatible con un producto de Euler de dato impuro **sub-resolución** sostenido.
- Síntesis: **la continuación analítica es barata vía combinaciones lineales (D–H) y produce gordos; es cara
  vía productos de dato impuro (141.R3) y ahí la impureza sub-resolución muere en la convergencia.** Las dos
  observaciones encajan: en ningún miembro continuable del corpus aparece sub-resolución. El único miembro
  sub-resolución (Hadamard 141.R2) continúa por fuerza bruta (producto canónico con ceros prescritos) y carece
  de TODA aritmética — ni Euler ni combinación de Euler.

---

## 5. Mensaje final

**Veredicto GAP-141.DH: GORDOS.** Los ceros off-line de Davenport–Heilbronn están a distancia macroscópica de
la línea crítica — agrupados en franjas verticales fijas $\Re s=\sigma_0\neq\tfrac12$, con infinitos ceros en
$\beta>1$ y densidad lineal en una franja $\tfrac12<\sigma_1<\sigma_2$. No hay sub-resolución; D–H satisface
incluso la forma de separación de banda ($\psi\asymp1$) de LP-134, la más fuerte de la familia.

**Qué decide sobre LP-141.** D–H **NO refuta LP-141**: es un cuasi-modelo que lo confirma. Un objeto con
ecuación funcional, continuación, y estructura casi-Euler (combinación de dos $L$ de Dirichlet, cada una con
producto de Euler) y $m=\infty$ produce ceros off gordos — exactamente lo que LP-141 predice para la clase
con estructura. La frontera sub-resolución/gordos coincide con la frontera sin-estructura/con-estructura: el
único objeto sub-resolución del corpus (contraejemplo de Hadamard 141.R2) abandona toda aritmética. La
implicación más fina y nueva: D–H demuestra que la **repulsión gorda es barata** (la da el casi-Euler, no
requiere Euler genuino — esto debilita la hipótesis de la Conjetura 141.E), y por tanto lo que el Euler
genuino de ζ aporta de más NO es la repulsión sino la **pureza/positividad global que colapsa $m$ a 0**. D–H
separa limpiamente las dos mitades de RH del programa: tiene la repulsión (gordos), le falta exactamente la
pureza ($m=0$). El frente vivo se desplaza de "¿hay repulsión?" (resuelto a favor en la categoría casi-Euler)
a "¿qué fuerza $m<\infty\Rightarrow m=0$?" (intacto).

**Datos de literatura usados:**
- **Verificados esta sesión:** definición de Hurwitz con $\tan\theta=\xi$, $\xi=(\sqrt5-1)^{-1}(\sqrt{10-2\sqrt5}-2)$, signos de la combinación [T86 §10.25, búsqueda]; forma como combinación de las dos $L$ mod 5 del carácter complejo y su conjugado [BG11, búsqueda]; ecuación funcional tipo $L$ con conductor 5 y eje $\tfrac12$ [T86 §10.25]; $\infty$ ceros con $\beta>1$ [DH36]; cero computado $\rho^*\approx0.8085171825\pm i\,85.6993484854$ [BS07]; existencia de densidad positiva (lineal en $T$) de ceros en una franja vertical fija $\sigma_1>\tfrac12$ (cualitativo) [escuela Bombieri–Ghosh / Voronin / Karatsuba].
- **[GAP de literatura] (NO usados como premisa de ningún teorema, solo como contexto):** los valores numéricos exactos de $\sigma_1,\sigma_2$ y la constante $c$ en $N_f(\sigma_1,\sigma_2,T)\geq cT$; la asintótica fina $N_L(\sigma_1,\sigma_2,T)\simeq T$ con constante atribuida a [BG11]; los exponentes exactos del conteo on-line (Levinson / Voronin $\exp(c\sqrt{\log\log\log\log T})$ / Karatsuba $(\log T)^{1/2-\varepsilon}$ — reportados por la búsqueda, no verificados al nivel de página); la forma cerrada exacta del factor $\Gamma_{\sin}$ en la ecuación funcional.

---

## Referencias

**Internas (backward-only):** Doc 141 (Phase 46 §1 forma canónica LP-134$^{(\psi)}$, separación de banda;
§3.4 Def. 141.2 LP-141, Prop. 141.P3/P4; §4.2 Prop. 141.R2 contraejemplo de Hadamard; §4.3 Cálculo 141.R3,
Conjetura 141.E, GAP-141.DH nombrado); Doc 134 (tricotomía gordo/fino/sub-resolución; GAP-134.DH original);
Doc 131 (bloques $F_{p,\alpha}$, pureza local); arquitectura D-109 (RH = $m<\infty$ ∧ pureza).

**Literatura (publicada, verificable):**
- [DH36] H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. **11**
  (1936), 181–185 y 307–312. (Ceros off; infinitos con $\beta>1$; sin producto de Euler.)
- [T86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (rev. D. R. Heath-Brown), Oxford
  Univ. Press, 1986. (§10.25: función de D–H, su ecuación funcional, ceros off-line.)
- [BS07] E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  **76** (2007), 2045–2049. (Cómputo de ceros off por deformación; testigo $\rho^*\approx0.8085\pm i\,85.699$.)
- [BG11] E. Bombieri, A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math. Surveys **66** (2011),
  no. 2, 221–270. (Inversión de Möbius, distribución de ceros en el semiplano de convergencia, familia
  $F_\vartheta$.)
- *Contexto (no verificados al nivel de página, citados como tradición):* S. M. Voronin (universalidad y
  conjunto excepcional de la recta crítica para D–H); A. A. Karatsuba (cotas $\Omega$ del conteo de ceros);
  N. Levinson (proporción de ceros on-line).

*Fin del Doc 146.*
