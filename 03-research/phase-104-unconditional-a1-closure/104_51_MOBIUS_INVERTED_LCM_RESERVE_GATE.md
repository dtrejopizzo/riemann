# 104_51 — Inversión Möbius del kernel `lcm` y gate de reserva

**Resultado.** El kernel de Gram no normalizado asociado a las dos marcas
de `104_50`,

\[
 K_s(d,e)=\zeta(s)\mathrm{lcm}(d,e)^{-s},
 \qquad s>1,                                               \tag{1}
\]

admite una inversión Möbius exacta en sus dos variables. En todo poset
divisor finito, si \(Z\) es la matriz zeta, \(M=Z^{-1}\) su matriz de
Möbius y \(W\) la diagonal de las masas de los enteros padres, entonces

\[
 \boxed{K=Z^{T}WZ,\qquad M^{T}KM=W.}                       \tag{2}
\]

Por tanto la inversión no deja una reserva entre torres: elimina **todas**
las correlaciones y deja solamente la energía diagonal. Comparar la energía
antes y después de invertir tampoco produce una desigualdad. La diferencia

\[
 \mathscr R_W(v)=\|Zv\|_W^2-\|v\|_W^2                    \tag{3}
\]

es indefinida ya en la torre mínima
\(\{1,p,p^2\}\). Para el vector von Mangoldt--Laguerre

\[
 v(p^k)=(\log p)L_{n-1}^{(1)}(k\log p)
\]

la reserva de **cutoff de una torre** conserva exactamente la fase. En grado
\(n=2\), esa contribución local es positiva para la torre de \(2\) y negativa
para la torre de \(5\). En el rango objetivo, \(n=151\), es positiva en
\(p=2\) y negativa en \(p=7\). Más generalmente, como función continua de
la posición de una torre, posee ambos signos para todo \(n\ge2\).

Esta afirmación local no se confunde con la forma zeta infinita: los padres
que quedan fuera de \(\{1,p,p^2\}\) aportan términos adicionales. La forma
infinita también es indefinida, pero requiere otro testigo. En
\(s=2,p=2\), el vector abstracto \((a,b)=(1,-1)\), soportado en
\(\{2,4\}\), da exactamente \((3\zeta(2)-5)/16<0\), mientras
\((1,0)\) da signo positivo. No se obtuvo aquí ambos signos de la forma
infinita sobre el **vector Laguerre fijo**.

El inverso simple \(M\) sí distingue a zeta del falsificador
\(\zeta(s+c)\zeta(s-c)\): para éste el selector condicionado contiene los
coeficientes del cofactor y no es uniforme. Pero la distinción no aporta un
signo, porque (3) ya falla para los pesos reales de zeta. Si se polariza la
diagonal para volver a una forma lineal, se obtiene una diferencia de dos
cuadrados sin orientación; si después se exige aditividad, el Teorema
`104_53` fuerza el retorno a los cumulantes de una torre y a
\(B_n=A_n-\lambda_n\).

Así queda descartado el mecanismo estrecho

```text
Palm de dos marcas + inversión Möbius doble
+ positividad de la diagonal resultante
=> reserva proporcional orientada para el vector Laguerre.
```

No queda descartada una desigualdad no aditiva específica del grado que
compare dos de las energías **antes** de la congruencia y que falle para el
selector desplazado. Este documento no prueba

\[
 B_n\le {1501\over2002}A_n\quad(n\ge150),                 \tag{4}
\]

ni A1 ni RH.

## 0. Auditoría respecto de `104_12`, `104_50` y `104_53`

`104_50` construye el Palm de segundo orden y escribe el kernel `lcm`,
pero no lo invierte. `104_52` toma su parte conectada y demuestra que los
pares entre torres distintas se cancelan. Aquí no se vuelve a contar ninguno
de esos resultados: se aplica la inversión de incidencia al kernel **no
centrado** y se decide si su diagonal deja una reserva de orden.

La congruencia (2) tampoco contradice el Teorema 1 de `104_12`. Allí se
descarta una métrica positiva fija con \(M=Z^\dagger\). Aquí no se identifica
el inverso con el adjunto: \(K=Z^TWZ\) es el Gram creado por \(Z\), y
\(M^TKM=W\) es solamente el cambio inverso de coordenadas. Precisamente por
eso no implica \(K\succeq W\) ni \(K\preceq W\), como prueba la Sección 3.

Finalmente, `104_53` clasifica las recomposiciones aditivas después de tomar
momentos. El contenido nuevo y estrecho de este documento es que tampoco
queda una reserva automática si se evita primero la proyección conectada y
se invierte directamente la forma cuadrática completa.

## 1. El kernel `lcm` es un Gram divisor

Sea \({\cal D}\) un conjunto finito cerrado por divisores. Indexamos filas
y columnas por \({\cal D}\) y ponemos

\[
 Z_{m,d}={\bf1}_{d\mid m},\qquad
 W=\mathrm{diag}(w_m:m\in{\cal D}),\qquad w_m>0.  \tag{5}
\]

Para dos funciones \(a,b\) sobre \({\cal D}\), su renovación divisora es

\[
 (Za)(m)=\sum_{d\mid m}a(d).                              \tag{6}
\]

La forma cuadrática de dos marcas vale

\[
 \begin{aligned}
 \langle Za,Zb\rangle_W
 &=\sum_{m\in{\cal D}}w_m
       \sum_{d\mid m}\sum_{e\mid m}a(d)b(e)\\
 &=\sum_{d,e\in{\cal D}}a(d)b(e)
       \sum_{\substack{m\in{\cal D}\\[d,e]\mid m}}w_m.
                                                               \tag{7}
 \end{aligned}
\]

Luego, con

\[
 K_{d,e}:=\sum_{\substack{m\in{\cal D}\\[d,e]\mid m}}w_m,
                                                               \tag{8}
\]

se tiene \(K=Z^TWZ\). Si se quita el cutoff y \(w_m=m^{-s}\),
convergencia absoluta da

\[
 K_{d,e}=\sum_{[d,e]\mid m}m^{-s}
 =\zeta(s)[d,e]^{-s},                                    \tag{9}
\]

El kernel probabilístico de `104_50`, ecuación (14), es
\([d,e]^{-s}\); (9) es exactamente \(\zeta(s)\) veces ese kernel porque
aquí no se dividió la suma de padres por la normalización \(\zeta(s)\).

Equivalentemente, si

\[
 \widehat W_s=\zeta(s)^{-1}W_s,\qquad
 \widehat K_s=\zeta(s)^{-1}K_s,
\]

entonces el kernel probabilístico y su congruencia son

\[
 \boxed{\widehat K_s(d,e)=[d,e]^{-s},\qquad
 M^T\widehat K_sM=\widehat W_s.}                          \tag{9a}
\]

La normalización multiplica simultáneamente las dos energías por el
escalar positivo \(\zeta(s)^{-1}\), de modo que no cambia ningún signo.

La matriz de inversión de incidencia es

\[
 M_{m,d}=\mu(m/d){\bf1}_{d\mid m},\qquad ZM=MZ=I.        \tag{10}
\]

Por consiguiente

\[
 M^TKM=M^TZ^TWZM=(ZM)^TW(ZM)=W,                          \tag{11}
\]

lo que prueba (2). La conclusión es exacta: una doble inversión del kernel
no puede dejar simultáneamente una diagonal positiva y una correlación
residual entre primos distintos. La primera es todo lo que queda después de
cancelar la segunda.

## 2. Aplicación a la renovación unitaria

Para un test \(f\), defina

\[
 v_f(d)=\Lambda(d)f(\log d),\qquad
 J_f(m)=\sum_{d\mid m}\Lambda(d)f(\log d).               \tag{12}
\]

Entonces \(J_f=Zv_f\), y (7)--(9) dan

\[
 \sum_{m\ge1}{J_f(m)J_g(m)\over m^s}
 =\zeta(s)\sum_{d,e\ge2}{\Lambda(d)\Lambda(e)
 f(\log d)g(\log e)\over[d,e]^s}.                        \tag{13}
\]

La inversión \(v_f=MJ_f\) utiliza de manera completa
\(\Lambda*1=\log\). Pero sustituirla en (13) solo recupera

\[
 \langle J_f,J_g\rangle_W
 =\langle v_f,Kv_g\rangle;
\]

no aparece una tercera forma. En particular, la diagonal de (11) contiene
\(\Lambda(d)^2f(\log d)g(\log d)\), mientras que el funcional que define
\(B_n\) es lineal en \(\Lambda(d)\). Para regresar a una forma lineal hay
que polarizar contra un ancla \(u\):

\[
 4\langle v,u\rangle_W
 =\|v+u\|_W^2-\|v-u\|_W^2.                               \tag{14}
\]

La ecuación (14) recupera la orientación que se busca únicamente como una
diferencia de dos energías positivas. La positividad de cada energía no
decide el signo de su diferencia.

## 3. La supuesta reserva: cutoff finito y kernel infinito

Considere el poset divisor

\[
 {\cal D}=\{1,p,p^2\}
\]

y un vector \(v=(0,a,b)^T\). Entonces

\[
 Zv=(0,a,a+b)^T,
\]

de modo que, para cualquier diagonal positiva \(W\),

\[
 \boxed{
 \mathscr R_W(v)
 =w_{p^2}\{(a+b)^2-b^2\}
 =w_{p^2}(a^2+2ab).}                                     \tag{15}
\]

Con \((a,b)=(1,0)\), (15) es positiva; con
\((a,b)=(1,-1)\), es negativa. Por tanto ni \(K-W\succeq0\) ni
\(W-K\succeq0\) uniformemente sobre los cutoffs finitos, aun restringiendo
a vectores nulos en \(1\). Este es un testigo de tres puntos, independiente
de toda estimación analítica.

Para evitar extrapolar ese cálculo al kernel infinito, calculemos este
último por separado. Con \(v\) soportado en \(p,p^2\), (1) y la diagonal
\(W_s(m,m)=m^{-s}\) dan

\[
\boxed{
 \begin{aligned}
 \mathscr R_s^{\infty}(a,b)={}&
 (\zeta(s)-1)p^{-s}a^2+2\zeta(s)p^{-2s}ab\\
 &+(\zeta(s)-1)p^{-2s}b^2.
 \end{aligned}}                                           \tag{15a}
\]

En \(s=2,p=2\), \((a,b)=(1,0)\) hace (15a) positiva. Para
\((a,b)=(1,-1)\),

\[
 \mathscr R_2^{\infty}(1,-1)={3\zeta(2)-5\over16}<0.      \tag{15b}
\]

La desigualdad es elemental y no usa una evaluación decimal:

\[
 \zeta(2)<1+{1\over4}+{1\over9}+{1\over16}+{1\over25}
                  +\int_5^\infty x^{-2}\,dx
 ={5989\over3600}<{5\over3}.                              \tag{15c}
\]

Así, la forma zeta infinita también carece de orden operatorial universal.
Las ecuaciones (15a)--(15c) no afirman todavía nada sobre el vector fijo
Laguerre.

Ahora use el vector real de A1,

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 a=(\log p)P_n(\log p),\quad
 b=(\log p)P_n(2\log p).                                 \tag{16}
\]

La reserva de cutoff de esa torre es exactamente

\[
 \boxed{
 w_{p^2}(\log p)^2P_n(x)
 \{P_n(x)+2P_n(2x)\},\qquad x=\log p.}                  \tag{17}
\]

No se ha reemplazado una potencia superior ni tomado el módulo del
Laguerre. En \(n=2\), \(P_2(x)=2-x\), y (17) tiene el signo de

\[
 (2-x)(6-5x).                                             \tag{18}
\]

Las cotas elementales

\[
 {1\over2}<\log2<1,\qquad {3\over2}<\log5<{5\over3}    \tag{19}
\]

muestran que (18) es positiva para \(p=2\) y negativa para \(p=5\).
Las desigualdades (19), por ejemplo, siguen de
\(8/3<e<11/4\), certificado directamente por la serie de \(e\).

La obstrucción local alcanza directamente el rango objetivo.
El checker encierra \(\log2\) y \(\log7=3\log2-\log(8/7)\) mediante la
serie racional de \(\mathrm{atanh}\,\), y evalúa \(P_{151}\) por
Horner intervalar con `Fraction`. Certifica

\[
\begin{array}{c|c|c}
p&P_{151}(\log p)\{P_{151}(\log p)+2P_{151}(2\log p)\}
&\text{signo}\\ \hline
2&[9.59561939937104,\,9.59561939937106]&+\\
7&[-6.33518557015695,\,-6.33518557015693]&-
\end{array}                                                \tag{20}
\]

Los decimales de (20) son solo una presentación de intervalos racionales:
las aserciones del checker son \(q_{\rm low}>0\) y \(q_{\rm high}<0\).
Así, la **reserva local de cutoff** falla en ambas direcciones sobre el
vector fijo real de \(n=151\), sin alterar
\(\Lambda(p^k)=\log p\). No se deduce de (20) que la forma infinita
completa tenga esos signos sobre el mismo vector; esa afirmación se retira.

El cambio de signo no es especial del grado dos. Sea \(r_n\) el mayor cero
de \(P_n\), que es simple. Para \(x<r_n\) suficientemente próximo a
\(r_n\), \(P_n(x)\) tiene signo opuesto al coeficiente líder, mientras
\(P_n(2x)\) tiene el signo del coeficiente líder. Así (17), como función de
una posición continua de torre, es negativa. Para \(x>r_n\) suficientemente
grande, tanto \(P_n(x)\) como \(P_n(2x)\), y por tanto también
\(P_n(x)+2P_n(2x)\), tienen el signo del coeficiente líder; (17) es
positiva. Esto prueba ambos signos de la geometría exacta para todo
\(n\ge2\). El testigo con
primos reales en (19) basta para descartar un orden operatorial universal;
no pretende descartar una desigualdad especial aún desconocida solo para
los grados \(n\ge150\).

## 4. El polo se diagonaliza del mismo modo

El comparador continuo de (9) es el operador de Volterra

\[
 (Vh)(x)=\int_0^xh(y)\,dy
\]

en \(L^2(e^{-\varepsilon x}dx)\). Su kernel de Gram es

\[
 K_0(y,z)=\int_{\max(y,z)}^\infty e^{-\varepsilon x}dx
 ={e^{-\varepsilon\max(y,z)}\over\varepsilon}.           \tag{21}
\]

La derivada es el inverso de \(V\) sobre su dominio natural, y por tanto
diagonaliza (21) exactamente igual que Möbius diagonaliza (9). Restar los
dos canales después de invertir produce una diferencia de energías
diagonales, no una energía positiva conjunta. El canal Gamma de A1 es otra
diagonal explícita, pero (2) no da una comparación entre esas tres
diagonales.

Esto localiza el fallo sin separar el polo en la identidad original: la
inversión es compatible con ambos canales, pero no orienta su resta. Una
cota que comparase directamente esas diagonales sobre \(P_n\) sería un
teorema adicional, no una consecuencia de la incidencia de Möbius.

## 5. Falsificador desplazado y tricotomía de cierre

Para

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c)
\]

la renovación condicionada en \(p^a\) es, con la notación de `104_49`,

\[
 \pi_{a,c}(k)
 ={(r^k+r^{-k})b_{a-k}(r)\over a b_a(r)},
 \qquad r=p^c.                                            \tag{22}
\]

En \(a=2\),

\[
 \pi_{2,c}(1)={1\over2}+{1\over2b_2(r)},\qquad
 \pi_{2,c}(2)={1\over2}-{1\over2b_2(r)}.                \tag{23}
\]

Así la matriz de renovación condicionada desplazada no es la matriz de
incidencia unitaria \(Z\), y el inverso simple
\(M\) de (10) no la deshace. La congruencia (2) usa una propiedad real que
el falsificador no posee. Sin embargo, no demuestra el margen: la reserva
propuesta es indefinida como orden operatorial tanto en cutoffs finitos,
por (15), como para el kernel zeta infinito, por (15a)--(15c). El test fijo
(20) refuta solamente la versión local de torre.

Después de la inversión solo quedan tres opciones:

1. conservar la diagonal cuadrática: se pierde la orientación lineal;
2. polarizarla: se obtiene la diferencia no orientada (14);
3. recomponer un observable aditivo: por `104_53`, se vuelve a una
   combinación de cumulantes de una torre y, para el Laguerre, a
   \(\mathcal B_{n,s}\to B_n\).

Ninguna de las tres opciones aporta la reserva
\((1501/2002)A_n-B_n\). El único sucesor compatible con este gate es una
desigualdad no aditiva, dependiente del vector \(P_n\), aplicada **antes**
de la congruencia y con un término explícito que domine el canal
Euler--polo--Gamma. No se construyó tal desigualdad aquí.

## 6. Reproducción

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 mobius_inverted_lcm_reserve_gate_check.py
```

El checker usa solo enteros y `Fraction`. Verifica la factorización Gram,
la inversión doble con y sin normalización, los dos signos de la reserva en
la torre mínima, el testigo infinito (15b)--(15c), los testigos Laguerre
racionales en \(n=2\) y \(n=151\), y la no uniformidad racional del
selector desplazado.
