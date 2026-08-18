# 104_65 — Gate de filtros locales y detector logarítmico de tasa

**Pregunta.** ¿Puede obtenerse un bloque consecutivo, arbitrariamente
largo, en el que

\[
 \lambda_n\geq-1,                                           \tag{1}
\]

controlando primero medias móviles, diferencias finitas o una generatriz
local de los coeficientes?

**Veredicto.** No mediante un filtro lineal finito fijo. Si RH es falsa,
todo filtro cuya función de transferencia no anule los modos exteriores
máximos conserva excursiones negativas exponenciales sobre un conjunto
sindético. Esto incluye todas las diferencias finitas de orden fijo y todas
las medias móviles uniformes de longitud fija. Si el filtro sí anula el modo,
puede borrar por completo el falsificador: para el cuarteto \(w=2i\),
\(E^2+4\) deja una sucesión estrictamente positiva aunque la original sea
negativa en cada cuarto índice.

Se construye además un detector acotado de **tasa exponencial negativa**,

\[
 \Psi_{V,n}(x)=\min\!\left\{V,{1\over n}\log\max(1,-x)\right\},
                                                               \tag{2}
\]

cuya media logarítmica tiene límite inferior cero si y solo si RH. A
diferencia de la logística de `104_61`--`104_64`, (2) no necesita resolver
una microfrecuencia \(e^{-cn}\): mide directamente la tasa \(c\). Pero su
representación prima--Laguerre conserva intacta la cancelación de parte
finita; separar polo y primos vuelve a costar \(\log(1/\varepsilon)\).

Este documento prueba un no-go cuantitativo y una coordenada exacta. No
prueba (1), A1 ni RH.

---

## 1. Auditoría lógica y falsificador obligatorio

La dirección correcta es

\[
 \boxed{
 \text{bloques de (1) de longitud no acotada}
 \ \Longrightarrow\ \mathrm{RH}.}                          \tag{3}
\]

Bajo RH, (1) vale en toda la semirrecta porque \(\lambda_n\geq0\). Si RH
es falsa, `104_56`, Teorema 3.1, produce un conjunto sindético en el que
\(\lambda_n\leq-cR^n\), con \(R>1\). Por ello (1) falla al menos una vez
en todo intervalo suficientemente largo. La ocurrencia de los bloques no
es una firma de falsedad de RH, sino un criterio suficiente para su verdad.

Todo mecanismo local ensayado aquí debe rechazar el cuarteto racional

\[
 w=2i,\qquad
 Q_n=4-2\operatorname {Re}(w^n+w^{-n}).                    \tag{4}
\]

Para \(n\equiv0\pmod4\),

\[
 Q_n=4-2(2^n+2^{-n})<-1\qquad(n\geq4),                    \tag{5}
\]

mientras en las otras tres clases \(Q_n\geq4\). No existe, pues, un
bloque bueno de longitud cuatro en la cola de (4).

---

## 2. Teorema de rigidez bajo filtros locales

Sea \(E\) el desplazamiento \((Ea)_n=a_{n+1}\), y sea

\[
 P(z)=\sum_{h=0}^Jp_hz^h\in\mathbb R[z],\qquad
 (P(E)a)_n=\sum_{h=0}^Jp_ha_{n+h}.                          \tag{6}
\]

Suponga que RH es falsa. Use la descomposición dominante de `104_56` y
agrupe conjugados y multiplicidades. Existen \(R>1\), \(1<R_1<R\),
ángulos no nulos \(\phi_1,\ldots,\phi_K\), multiplicidades
\(m_j>0\), y una constante \(C_0\), tales que

\[
 \lambda_n=C_0-2R^n\operatorname {Re}
 \sum_{j=1}^Km_je^{in\phi_j}
 +O(n^2R_1^n+n^2).                                          \tag{7}
\]

Aquí se han combinado los caracteres iguales; dos ángulos opuestos
pertenecen al mismo par real. Ponga

\[
 u_j=Re^{i\phi_j},\qquad
 F_P(x)=2\operatorname {Re}
 \sum_{j=1}^Km_jP(u_j)e^{ix_j}.                             \tag{8}
\]

Aplicar (6) a (7) da exactamente

\[
 \boxed{
 (P(E)\lambda)_n=C_0P(1)-R^nF_P(n\phi)
 +O_P(n^2R_1^n+n^2).}                                      \tag{9}
\]

**Teorema 2.1 (dicotomía filtro--modo).** Se cumple una de las dos
alternativas siguientes:

1. \(P(u_j)=0\) para cada modo exterior máximo;
2. existen \(c_P>0\), \(n_P\) y un conjunto sindético
   \(D_P\subset\mathbb N\), de densidad natural positiva, tales que

   \[
    (P(E)\lambda)_n\leq-c_PR^n
    \qquad(n\in D_P,\ n\geq n_P).                          \tag{10}
   \]

**Demostración.** Sea

\[
 H=\overline{\{n\phi:n\in\mathbb Z\}}\subset\mathbb T^K.
\]

Los caracteres distintos de un grupo compacto son linealmente
independientes. Como los conjugados ya fueron agrupados, \(F_P\) es
idénticamente cero en \(H\) exactamente cuando todos los coeficientes
\(P(u_j)\) se anulan. Si no se anulan todos, \(F_P\) es una función real
continua no nula. Cada carácter de (8) es no trivial —los ceros no
triviales tienen ordenada no nula—, de modo que la integral de Haar de
\(F_P\) es cero. Por tanto \(F_P\) toma algún valor positivo.

Elija \(\eta>0\) tal que

\[
 U=\{x\in H:F_P(x)>2\eta\}
\]

sea no vacío y su frontera tenga medida de Haar cero. Los retornos de la
rotación mínima a \(U\) tienen densidad natural positiva y forman un
conjunto sindético, por el mismo argumento compacto de `104_56`, §3. En
ese conjunto, (9) y \(R_1<R\) dan, después de aumentar el umbral,

\[
 (P(E)\lambda)_n\leq-\eta R^n.
\]

Esto prueba (10), con \(c_P=\eta\). \(\square\)

La primera alternativa no es una ganancia: el filtro ha incorporado como
ceros precisamente los modos que debía detectar. Si quedan otros modos
exteriores, se repite el argumento con el siguiente módulo. Anularlos todos
requiere conocer un divisor off-line finito que la aritmética no entrega.

### 2.1 Diferencias y medias móviles

Para una diferencia fija de orden \(k\),

\[
 P(z)=(z-1)^k.                                               \tag{11}
\]

Su único cero es \(1\), luego no anula ningún \(|u_j|>1\). Para la media
móvil uniforme de longitud \(J+1\),

\[
 P_J(z)={1+z+\cdots+z^J\over J+1}.                          \tag{12}
\]

Todos sus ceros están en \(|z|=1\), así que tampoco anula un modo exterior.
Más aún, si \(|u|=R>1\),

\[
 |P_J(u)|={|u^{J+1}-1|\over(J+1)|u-1|}
 \geq {R^{J+1}-1\over(J+1)(R+1)}.                           \tag{12a}
\]

Así una ventana más larga no amortigua el modo exterior: a módulo fijo lo
amplifica exponencialmente, aunque puede cambiar su fase.
El Teorema 2.1 implica, para cada \(k,J\) fijo:

\[
\boxed{
\begin{aligned}
 \mathrm {RH}\quad\Longleftrightarrow\quad&
 \Delta^k\lambda_n\geq-e^{\sqrt n}
 \text{ en bloques de longitud no acotada},\tag{13a}\\
 \mathrm {RH}\quad\Longleftrightarrow\quad&
 {1\over J+1}\sum_{h=0}^J\lambda_{n+h}\geq-1
 \text{ en bloques de longitud no acotada}.\tag{13b}
\end{aligned}}
\]

Bajo RH, \(\lambda_n=O(n\log n)\), de modo que toda combinación finita
\(\Delta^k\lambda_n\) es \(O_k(n\log n)\) y satisface la barrera
subexponencial de (13a). En (13b), RH hace no negativo cada sumando. Las
direcciones hacia RH siguen de (10): bajo no-RH la excursión filtrada de
tasa \(R^n\) vence \(e^{\sqrt n}\) y toda constante sobre un conjunto
sindético. No se pone la barrera \(-1\) en (13a), porque la positividad de
\(\lambda_n\) no da signo a sus diferencias finitas.

En particular, ni diferenciar ni promediar reduce la tasa \(R\). Solo
multiplica su amplitud por \(P(u_j)\).

### 2.2 La generatriz conserva el mismo polo

Sea

\[
 G(z)=\sum_{n\geq1}\lambda_nz^n.
\]

Salvo un polinomio de borde,

\[
 \sum_{n\geq1}(P(E)\lambda)_nz^n=P(z^{-1})G(z).             \tag{14}
\]

Si \(z_0=u_j^{-1}\) es un polo interior producido por un modo máximo, su
residuo en (14) queda multiplicado por \(P(u_j)\). Por tanto el radio de
convergencia no mejora salvo anulación exacta. Las cotas de Cauchy para la
generatriz filtrada enfrentan el mismo polo que las de `104_63`; no fabrican
los bloques de (1).

---

## 3. Un aniquilador que pasa de largo el cuarteto

La alternativa de anulación es un fallo real, no una formalidad. En (4),
tome

\[
 P(z)=z^2+4.                                                 \tag{15}
\]

Como \(P(2i)=P(-2i)=0\), los dos modos exteriores desaparecen y

\[
\begin{aligned}
 (P(E)Q)_n
 &=Q_{n+2}+4Q_n\\
 &=20-{15\over2}\operatorname {Re}(w^{-n}).                \tag{16}
\end{aligned}
\]

De aquí

\[
 \boxed{(P(E)Q)_n\geq20-{15\over2^{n+1}}>0\qquad(n\geq1),} \tag{17}
\]

aunque (5) impide bloques buenos de longitud cuatro para \(Q_n\).

Más generalmente, para cualquier \(P\in\mathbb R[z]\),

\[
 \boxed{
 (P(E)Q)_n=4P(1)-2\operatorname {Re}
 \{w^nP(w)+w^{-n}P(w^{-1})\}.}                              \tag{18}
\]

Si \(P(w)\ne0\), una de las cuatro clases módulo cuatro hace positiva
\(\operatorname {Re}(i^nP(w))\). En esa clase, (18) satisface

\[
 (P(E)Q)_n\leq-c_P2^n                                      \tag{19}
\]

para todo \(n\) suficientemente grande, con

\[
 c_P=\max\{|\operatorname {Re}P(2i)|,
             |\operatorname {Im}P(2i)|\}>0                 \tag{20}
\]

después de reducir la constante por un factor fijo. El conjunto de (19)
tiene densidad \(1/4\) y huecos a lo sumo cuatro. Si \(P(w)=0\), (16)
muestra que el filtro puede resultar estrictamente positivo. Éste es el
testigo cuantitativo de la dicotomía del Teorema 2.1.

---

## 4. Detector logarítmico de la tasa negativa

Fije \(V>0\) y defina (2). Es una función continua, acotada entre \(0\) y
\(V\), y se anula exactamente cuando \(x\geq-1\). Posee la identidad de
capa

\[
 \boxed{
 \Psi_{V,n}(x)=\int_0^V
 {\bf1}_{\{x<-e^{nv}\}}\,dv.}                              \tag{21}
\]

La tasa puntual \(n^{-1}\log(1+\lambda_n^-)\) ya aparece en `104_61`,
(9). Lo nuevo de esta sección es solo su truncación acotada, su promedio
logarítmico y la identidad de gran desviación (21); no se reclama un nuevo
criterio de ceros independiente de Bombieri--Lagarias.

Con \(H_X=\sum_{n\leq X}1/n\), ponga

\[
 \boxed{
 \mathfrak R_V(X)={1\over H_X}
 \sum_{n\leq X}{\Psi_{V,n}(\lambda_n)\over n}.}            \tag{22}
\]

**Teorema 4.1 (criterio de tasa logarítmica).** Para cada \(V>0\),

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak R_V(X)=0.}                 \tag{23}
\]

**Demostración.** Bajo RH, \(\lambda_n\geq0\), luego (22) es cero para
todo \(X\). Si RH es falsa, `104_56` da \(R>1\), \(c>0\) y un conjunto
sindético \(D\) de densidad natural y logarítmica \(d>0\) tal que
\(\lambda_n\leq-cR^n\) en \(D\). Ponga \(a=\log R\). Para \(n\) grande
en \(D\),

\[
 {1\over n}\log(-\lambda_n)\geq {a\over2}.
\]

Así

\[
 \liminf_{X\to\infty}\mathfrak R_V(X)
 \geq d\min\!\left(V,{a\over2}\right)>0,                  \tag{24}
\]

contradiciendo el segundo miembro de (23). \(\square\)

Para el cuarteto (4), las tres clases no negativas no contribuyen y

\[
 {1\over n}\log(-Q_n)\longrightarrow\log2
 \qquad(4\mid n).
\]

Por tanto

\[
 \boxed{
 \mathfrak R_V^{\mathcal O}(X)\longrightarrow
 {1\over4}\min(V,\log2).}                                  \tag{25}
\]

La variable \(v\) de (21) es la tasa diagonal de `104_62`, pero aquí no se
introduce una transformada oscilatoria. La afirmación que faltaría probar
es la gran desviación unilateral

\[
 {1\over H_X}\sum_{n\leq X}{1\over n}
 {\bf1}_{\{\lambda_n<-e^{nv}\}}\longrightarrow0
 \quad\text{para casi todo }v\in(0,V),                    \tag{26}
\]

o directamente la integral (22). El Teorema 4.1 muestra que (26) sigue
teniendo fuerza RH; no la demuestra.

---

## 5. Forma aritmética emparejada y gate del regulador

Use la convención de `104_61`:

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 ={}&A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 ={}&\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}&\longrightarrow\lambda_n.
\end{aligned}                                               \tag{27}
\]

Como la suma exterior de (22) es finita y \(\Psi_{V,n}\) es continua,

\[
\boxed{
 \mathfrak R_V(X)=\lim_{\varepsilon\downarrow0}{1\over H_X}
 \sum_{n\leq X}{1\over n}
 \Psi_{V,n}\!\left(A_n+p_n(\varepsilon)
 -\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right).}                             \tag{28}
\]

La fórmula (28) conserva polo, bloque arquimediano, primos y potencias
primas hasta después de aplicar el detector.

La concavidad de la raíz o del logaritmo no permite separarlos. Para \(n\)
fijo, `104_63`, (20), da

\[
\begin{aligned}
 p_n(\varepsilon)
 &=(-1)^{n-1}\varepsilon^{-n}(1+O_n(\varepsilon)),\\
 Q_{n,\varepsilon}
 &=p_n(\varepsilon)+A_n-\lambda_n+o(1).                    \tag{29}
\end{aligned}
\]

Por consiguiente,

\[
 {1\over n}\log(1+|p_n(\varepsilon)|)
 =\log{1\over\varepsilon}+o_n(1),\qquad
 {1\over n}\log(1+|Q_{n,\varepsilon}|)
 =\log{1\over\varepsilon}+o_n(1).                         \tag{30}
\]

El miembro emparejado de (28) tiene límite finito, pero cualquier
triángulo aplicado antes de emparejar introduce una tasa que diverge como
\(\log(1/\varepsilon)\). En la coordenada de raíces, la misma pérdida es

\[
 |p_n(\varepsilon)|^{1/n},
 |Q_{n,\varepsilon}|^{1/n}\sim\varepsilon^{-1}.             \tag{31}
\]

Esto cierra el ataque elemental «subaditividad de la raíz \(n\)-ésima».
No es un no-go para una desigualdad nueva aplicada directamente a la parte
finita emparejada de (28).

---

## 6. Balance

**Probado.** La dicotomía general (9)--(10), su especialización a
diferencias y medias móviles, la conservación del polo en la generatriz,
el aniquilador exacto (16)--(17), el criterio de tasa (21)--(24), el valor
off-line (25) y el gate de regulador (29)--(31).

**Descartado como atajo.** Cualquier número fijo de diferencias; cualquier
media móvil de longitud fija; estimar la generatriz filtrada en vez de la
original; o separar la raíz/logaritmo del polo y la suma de Mangoldt.

**Frente que sobrevive.** Una desigualdad de gran desviación para la parte
finita **emparejada** de (28), suficiente para (26), o una construcción
directa de bloques de (1). A diferencia de Fermi, el detector (22) ya está
en la escala exponencial correcta y no paga microfrecuencia; a diferencia
de una energía \(H^2\), está acotado y unilateral. No se obtuvo la cota
aritmética.

**No probado.** La existencia de un solo bloque nuevo para los coeficientes
reales más allá de los rangos certificados, el límite cero de (22), A1 o
RH.

---

## 7. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 local_filter_long_block_check.py
```

El checker usa `Fraction` y enteros gaussianos racionales. Verifica (4)--
(5), la identidad de filtro (18), el aniquilador (16)--(17), la ausencia de
ceros exteriores de (11)--(12) en el test \(w=2i\), y las excursiones
periódicas de los filtros no aniquiladores. El Teorema 2.1 y los límites
logarítmicos se prueban en el texto; no se certifican por muestreo.
