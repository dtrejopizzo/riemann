# 104_60 — Criterio no lineal de barrera en el grado

**Resultado.** El criterio sindético de `104_56` permite debilitar mucho
más el frente que «\(D_n>0\) en densidad uno». Sea

\[
 D_n:=4\lambda_n-A_n,
 \qquad A_n>0\quad(n\ge150),                         \tag{1}
\]

y sea \(b_n>0\) cualquier escala subexponencial:

\[
 \log b_n=o(n).                                      \tag{2}
\]

Entonces RH equivale a que las excursiones profundas
\(D_n\le-b_n\) tengan densidad inferior cero. Equivale incluso a encontrar
**una** sucesión de intervalos consecutivos, cada vez más largos y más
lejanos, en los que desaparezca en promedio la barrera saturada

\[
 \boxed{
 H_{n,b}:={(-D_n)_+\over b_n+(-D_n)_+}.}             \tag{3}
\]

Esto no prueba que la barrera real tienda a cero y, por tanto, no prueba
RH. Sí cambia rigurosamente el teorema aritmético que bastaría probar: ya
no hace falta obtener signo, margen proporcional ni siquiera una cota
polinómica para cada grado. Basta excluir, en promedio local, una densidad
positiva de excursiones negativas mayores que una escala tan grande como

\[
 b_n=\exp\!\left({n\over\log\log(n+e^e)}\right).     \tag{4}
\]

La construcción es no lineal, unilateral y saturada. Queda fuera tanto de
las medias lineales de `104_17` como de la clasificación de identidades
polinómicas aditivas de `104_53`.

---

## 1. Input dominante y por qué la escala puede ser casi exponencial

El Teorema 3.1 de `104_56` prueba lo siguiente. Si RH es falsa, existen
\(R>1\), \(c>0\), un entero \(L\ge1\), un conjunto sindético
\(\mathcal S\subset\mathbb N\) con huecos a lo sumo \(L\), y \(n_0\),
tales que

\[
 \boxed{
 D_n\le-cR^n\qquad(n\in\mathcal S,\ n\ge n_0).}    \tag{5}
\]

En efecto, allí se prueba
\(\lambda_n\le-c_0R^n\) sobre un conjunto de retornos sindético; como
\(A_n=O(n\log n)\), (5) sigue reduciendo \(c_0\) y aumentando \(n_0\).

Si (2) vale y \(a=\log R>0\), entonces, para \(n\) suficientemente grande,

\[
 b_n\le e^{an/2},\qquad {cR^n\over b_n}\longrightarrow\infty. \tag{6}
\]

Ésta es la ganancia conceptual: una falsedad de RH no produce solo una
violación pequeña de (1), sino excursiones de tasa exponencial fija en un
conjunto con huecos acotados. Cualquier barrera de tasa \(o(n)\) termina
siendo despreciable frente a ellas.

---

## 2. Criterio de excursiones profundas

Para \(E_b:=\{n\ge150:D_n\le-b_n\}\), escriba

\[
 \underline d(E_b)
 :=\liminf_{N\to\infty}{1\over N}\#(E_b\cap[1,N]). \tag{7}
\]

**Teorema 2.1 (corolario de densidad inferior de los modos
Bombieri--Lagarias).** Para toda
sucesión positiva \(b_n\) que satisfaga (2), son equivalentes:

1. RH;
2. \(\underline d(E_b)=0\);
3. existen intervalos enteros consecutivos \(I_j\), con
   \(\min I_j\to\infty\) y \(|I_j|\to\infty\), tales que

   \[
   {1\over|I_j|}\#(E_b\cap I_j)\longrightarrow0.    \tag{8}
   \]

**Demostración.** Bajo RH,
\(\lambda_n=A_n+O(\sqrt n\log n)\), de modo que
\(D_n=3A_n+O(\sqrt n\log n)>0\) para todo \(n\) suficientemente grande.
Así \(E_b\) es finito y se cumplen 2 y 3.

Suponga ahora que RH es falsa. Por (5)--(6), después de aumentar \(n_0\),

\[
 \mathcal S\cap[n_0,\infty)\subset E_b.             \tag{9}
\]

Todo intervalo de \(L\) enteros contiene un elemento de \(\mathcal S\).
Por tanto

\[
 \#(E_b\cap[M+1,M+H])\ge {H\over L}-2             \tag{10}
\]

para \(M\ge n_0\). La ecuación (10) da
\(\underline d(E_b)\ge1/L>0\) y prohíbe (8) para cualquier sucesión de
intervalos con longitud tendiendo a infinito. \(\square\)

La condición 2 es notablemente más débil que densidad natural cero: solo
pide una subsucesión de escalas iniciales donde la proporción se acerque a
cero. La condición 3 es todavía más local: permite elegir los intervalos.
La sindeticidad de la obstrucción es lo que vuelve suficientes estas
relajaciones.

---

## 3. Barrera saturada: una media no lineal equivalente a RH

Defina \(H_{n,b}\) por (3). Se tiene

\[
 0\le H_{n,b}<1,\qquad
 H_{n,b}=0\iff D_n\ge0.                             \tag{11}
\]

Sin embargo no exigiremos que cada sumando se anule.

**Teorema 3.1 (barrera no lineal de intervalos).** Fijada cualquier
escala (2), son equivalentes:

1. RH;
2. \(\displaystyle
   \liminf_{N\to\infty}{1\over N}\sum_{n=150}^NH_{n,b}=0\);
3. existen intervalos \(I_j\) como en el Teorema 2.1 tales que

   \[
   \boxed{
   {1\over|I_j|}\sum_{n\in I_j}H_{n,b}\longrightarrow0.} \tag{12}
   \]

**Demostración.** Bajo RH, (11) es cero eventualmente. Si RH es falsa,
(5)--(6) dan, uniformemente para \(n\in\mathcal S\) y \(n\to\infty\),

\[
 H_{n,b}\ge {cR^n\over b_n+cR^n}\longrightarrow1. \tag{13}
\]

Luego \(H_{n,b}\ge1/2\) sobre la cola de \(\mathcal S\). Combinando esto
con (10), toda media sobre un intervalo largo y lejano tiene límite
inferior al menos \(1/(2L)\). Lo mismo vale para las medias iniciales.
Esto contradice 2 o 3. \(\square\)

El teorema sigue válido si (3) se reemplaza por cualquier función de
saturación \(\Phi((-D_n)_+/b_n)\) con
\(\Phi(0)=0\) y \(\Phi(x)\to\ell>0\) cuando \(x\to\infty\).

Una versión suave es logística. Si

\[
 \mathcal L_{n,\tau}:={1\over1+\exp(\tau D_n/b_n)}, \tag{14}
\]

entonces RH equivale a la existencia de intervalos \(I_j\) como arriba y
números \(\tau_j\to\infty\) para los cuales la media de
\(\mathcal L_{n,\tau_j}\) sobre \(I_j\) tiende a cero. Bajo RH,
\(D_n/b_n\) puede tender a cero si \(b_n\) es enorme, por lo que en esta
formulación se debe escoger \(\tau_j\) después del intervalo, por ejemplo
de modo que
\(\tau_j\min_{n\in I_j}D_n/b_n\to\infty\). Esta elección existe porque
el mínimo es positivo en una cola. Bajo no-RH, (13) fuerza la logística a
uno sobre el conjunto sindético, cualquiera sea \(\tau_j\ge1\).

La barrera racional (3) es preferible: no contiene ese cuantificador
auxiliar y ya entrega la equivalencia exacta.

---

## 4. Traducción al bloque aritmético real

Para evitar la colisión histórica de la letra \(B_n\), ponga

\[
 \mathscr P_n:=A_n-\lambda_n.                       \tag{15}
\]

Éste es el funcional prima--Laguerre completo, con polo, Gamma, potencias
primas y bordes recompuestos antes de estimar. De (1),

\[
 -D_n=4\mathscr P_n-3A_n.                           \tag{16}
\]

El nuevo teorema aritmético suficiente puede enunciarse sin ceros:

> **Frontera 104_60.** Para alguna sucesión \(b_n=e^{o(n)}\), construir
> intervalos enteros \(I_j\) con
> \(\min I_j,|I_j|\to\infty\) y probar
> \[
> \boxed{
> {1\over|I_j|}\sum_{n\in I_j}
> {\bigl(4\mathscr P_n-3A_n\bigr)_+
>  \over
>  b_n+\bigl(4\mathscr P_n-3A_n\bigr)_+}
> \longrightarrow0.}                               \tag{17}
> \]

Por el Teorema 3.1, (17) prueba RH. A diferencia del frente anterior, (17)
permite simultáneamente:

* grados malos, incluso una proporción que no se controle a priori;
* déficits polinómicos o subexponenciales frecuentes;
* ausencia de una cota uniforme coeficiente a coeficiente;
* una escala \(b_n\) casi exponencial como (4).

Solo prohíbe que excursiones de tasa exponencial fija ocupen una densidad
local positiva. Ésa es exactamente la firma que deja cualquier cero fuera
de la línea.

La identidad de capa

\[
 {x_+\over1+x_+}
 =\int_0^\infty{\mathbf1_{\{x>t\}}\over(1+t)^2}\,dt \tag{18}
\]

muestra que (17) es una cota integrada para las densidades de excedencia

\[
 4\mathscr P_n-3A_n>t b_n.                         \tag{19}
\]

Así, una vía real hacia (17) sería una desigualdad de gran desviación
**unilateral en el índice \(n\)** para el funcional primo completo. No
basta una media lineal de \(\mathscr P_n\).

---

## 5. Auditoría contra `104_17` y `104_53`

### 5.1 No es Abel--Fejér ni una ventana lineal

`104_17` prueba que sumas iniciales, medias triangulares y positividad Abel
pueden ocultar coeficientes exponencialmente negativos. La operación (3)
hace lo contrario:

1. elimina la parte positiva, que no puede compensar un fallo;
2. divide por la amplitud para que un único pico enorme no sustituya una
   densidad de picos;
3. promedia solo después de esas dos operaciones.

Por ello no puede recuperarse desde una media lineal. Reemplazar (3) por
\(( -D_n)_+\) daría un criterio válido pero mucho más fuerte: perdería la
saturación y volvería a pagar la amplitud exponencial que el criterio de
densidad no necesita.

### 5.2 No es una identidad polinómica aditiva

`104_53` clasifica polinomios en momentos que son aditivos dentro de un
grado fijo. La aplicación

\[
 x\longmapsto{x_+\over b+x_+}                      \tag{20}
\]

no es polinómica, no es aditiva y se aplica a la secuencia de grados
después de recomponer exactamente \(\mathscr P_n\). Ningún polinomio puede
reproducir (20) en toda la recta: (20) se anula en una semirrecta y se
satura en la otra. Aproximarla en un compacto tampoco controla el
falsificador, cuyo argumento crece como \(R^n\).

Esto coloca (17) fuera del teorema de clasificación. No significa que
`104_53` suministre (17): la desigualdad aritmética unilateral sigue
completamente abierta.

### 5.3 Jensen no recupera el signo

La barrera es plana para \(x\le0\) y cóncava para \(x>0\), con un cambio de
pendiente en cero. No es globalmente convexa ni globalmente cóncava. Por
eso no hay una transferencia de Jensen desde
\(\sum_{n\in I}\mathscr P_n\). Esta falta es necesaria: una cota obtenida
solo de la primera media volvería a caer en `104_17`.

---

## 6. Falsificador off-line exacto

Use el cuarteto racional de `104_17`, para el cual

\[
 w=2i,\qquad
 Q_n=4-2\operatorname {Re}(w^n+w^{-n}),\qquad
 D_n^{\mathcal O}=4Q_n.                            \tag{21}
\]

Entonces

\[
 D_n^{\mathcal O}<0\iff n\equiv0\pmod4,            \tag{22}
\]

y, en esa clase,

\[
 -D_n^{\mathcal O}\asymp2^n.                       \tag{23}
\]

Para cualquier \(b_n=e^{o(n)}\), la barrera correspondiente tiende a uno
en \(n\equiv0\pmod4\) y vale cero en las otras tres clases. Por tanto

\[
 \boxed{
 {1\over N}\sum_{n\le N}
 {(-D_n^{\mathcal O})_+\over
  b_n+(-D_n^{\mathcal O})_+}\longrightarrow{1\over4}.} \tag{24}
\]

El mecanismo no «prueba» el objetivo para el divisor off-line: lo rechaza
con densidad exacta \(1/4\). En particular pasa el falsificador que las
medias Abel positivas de `104_17` no pasan.

---

## 7. Qué se obtuvo y qué sigue abierto

Queda probado:

1. el margen positivo grado a grado puede reemplazarse por la ausencia en
   densidad inferior de excursiones más profundas que **cualquier** escala
   subexponencial prefijada;
2. basta una sucesión de intervalos buenos, no toda la semirrecta;
3. la barrera saturada (17) es un criterio exacto, no lineal, que pasa el
   cuarteto off-line y no pertenece a las familias descartadas por
   `104_17` o `104_53`.

No queda probado:

\[
 \text{la estimación aritmética (17) para los pesos reales }\Lambda(m).
\]

Ése es ahora un frente estrictamente más débil que A1 grado a grado. El
objeto nuevo no es otra identidad positiva: es una gran desviación
unilateral, saturada y local en el grado, aplicada al funcional primo
completo antes de permitir cualquier compensación entre signos.

## 8. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 nonlinear_degree_barrier_check.py
```

El checker usa `Fraction`. Verifica (21)--(24) para el cuarteto racional,
la clase mala módulo cuatro y cotas exactas de la barrera con normalización
polinómica. No certifica (17) para la zeta.
