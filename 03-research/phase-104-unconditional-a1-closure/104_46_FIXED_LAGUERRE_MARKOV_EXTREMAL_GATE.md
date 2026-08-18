# 104_46 — El vector Laguerre fijo es casi extremal para el transporte divisor

**Estado.** Se atacó exactamente la posibilidad que `104_44` había dejado
abierta: una brecha del operador divisor no sobre todos los vectores, sino
sólo sobre

\[
 f_{n,s}(d)=L_{n-1}^{(1)}(s\log d),\qquad s>1,
\tag{1}
\]

después de retirar su media von Mangoldt. El resultado es negativo y más
fuerte que el gate operatorial de `104_44`. Para todo \(s>1\) suficientemente
próximo a \(1\), la propia sucesión (1) es casi extremal:

\[
 \boxed{
 {\|\mathsf T_s(f_{n,s}-\mathbb E_{\nu_s}f_{n,s})\|_{L^2(\Pi_s)}^2
  \over
  \|f_{n,s}-\mathbb E_{\nu_s}f_{n,s}\|_{L^2(\nu_s)}^2}
 \longrightarrow1.}
\tag{2}
\]

La razón no es un primo excepcional fijo. Bajo la medida cuadrática del
polinomio de grado \(n-1\), el divisor von Mangoldt es, con probabilidad
asintótica uno, un primo enorme; al multiplicarlo por un cofactor zeta fijo,
ese primo sigue siendo recuperable como el factor primo mayor del producto.
La esperanza condicional pierde entonces una proporción \(o(1)\) de la
energía del vector exacto.

El comparador continuo polo--Gamma hace lo contrario. Para el mismo
polinomio no escalado, su cociente centrado tiende a cero. Por tanto no existe
una transferencia de coercividad Gamma al canal aritmético, ni siquiera sobre
el único rayo que interesa. Además, ambos cocientes centrados son ciegos a la
diferencia de medias firmada que vale \(B_n=A_n-\lambda_n\). Esto descarta el
mecanismo

> «probar no-alineación del vector Laguerre mediante el transporte Markov y
> compararla con la contracción Gamma».

No se descarta una identidad lineal firmada que estime directamente las
medias. Esa identidad sería precisamente el nuevo teorema aritmético
unilateral aún faltante. No se prueba \(B_n\le(1501/2002)A_n\), A1 ni RH.

## 1. Auditoría vinculante

`104_28` identifica el test de Li con el prefijo de Laguerre
\(g_n=\sum_{j<n}\phi_j\), pero demuestra que la no-alineación en un operador
interior no se transporta automáticamente al borde. `104_30` construye una
referencia positiva de bandera que evalúa \(A_n\), aunque su estimación de
filas vuelve a pedir las segundas diferencias firmadas de \(A_n-\lambda_n\).
`104_42` permite todo precondicionador positivo dependiente del grado y prueba
que su óptimo es el módulo del momento que se quería acotar. Finalmente,
`104_44` construye el transporte canónico asociado a
\(\Lambda*1=\log\), prueba que su norma en media cero es uno mediante
\(e_p\), y deja expresamente abierta una brecha para el vector (1).

Este documento cierra sólo esa última apertura. No usa una suma triangular de
grados, no cambia de escala el polinomio y no separa primos de potencias primas
en la identidad final. La separación por exponentes se usa únicamente para
probar el teorema asintótico de casi extremalidad.

## 2. Transporte y cociente específico

Con la notación de `104_44`,

\[
 \mathcal L_s=-{\zeta'(s)\over\zeta(s)},\qquad
 \nu_s(d)={\Lambda(d)d^{-s}\over\mathcal L_s},\qquad
 \Pi_s(N)={ (\log N)N^{-s}\over-\zeta'(s)},
\tag{3}
\]

y

\[
 (\mathsf T_sh)(N)={1\over\log N}
       \sum_{d\mid N}\Lambda(d)h(d).
\tag{4}
\]

Sea \(r=n-1\),

\[
 F_r(x)=L_r^{(1)}(sx),\qquad
 \mu_{r,s}=\mathbb E_{\nu_s}F_r(\log D),\qquad
 \widetilde F_r=F_r-\mu_{r,s}.
\tag{5}
\]

Definimos

\[
 Q_r(s)={\|\mathsf T_s\widetilde F_r\|_{L^2(\Pi_s)}^2
              \over
              \|\widetilde F_r\|_{L^2(\nu_s)}^2}.
\tag{6}
\]

Jensen da \(0\le Q_r(s)\le1\). El punto es que el extremo superior sí se
alcanza asintóticamente sobre (5).

## 3. Lema de saddle primo

La siguiente forma del lema es suficiente. El intervalo de \(s\) no necesita
ser optimizado: el argumento de Phase 104 lleva después \(s\downarrow1\).

**Lema 3.1 (dominación del exponente primo).** Existe \(s_0>1\) tal que, para
cada \(s\in(1,s_0)\), al tender \(r\to\infty\),

\[
 \begin{aligned}
 \mathcal L_s\,\mathrm{Var}_{\nu_s}(F_r)
 &=(1+o_s(1))M_r,\\
 M_r&:=\sum_{p\ \mathrm{primo}}{\log p\over p^s}
             \bigl(F_r(\log p)-\mu_{r,s}\bigr)^2,
 \end{aligned}
\tag{7}
\]

y la medida de probabilidad proporcional a los sumandos de \(M_r\) escapa a
infinito. Más precisamente, para cada \(R>0\),

\[
 {1\over M_r}\sum_{\substack{p\ \mathrm{primo}\\\log p\le R}}
 {\log p\over p^s}
 \bigl(F_r(\log p)-\mu_{r,s}\bigr)^2\longrightarrow0.
\tag{8}
\]

Para todo conjunto finito de enteros \(k\), uniformemente en ese conjunto,

\[
\begin{aligned}
 &\sum_{p>K}{(\log p+\log k)\over p^s}
 \left[
 {\log p\,F_r(\log p)+C_{r,k}\over\log p+\log k}
 -\mu_{r,s}\right]^2\\
 &\hspace{35mm}=(1+o_s(1))M_r,
 \qquad
 C_{r,k}:=\sum_{d\mid k}\Lambda(d)F_r(\log d).
\end{aligned}
\tag{9}
\]

**Prueba.** Se dan los detalles de escala porque son los que impiden usar el
comparador continuo. Para \(c>0\), ponga

\[
 I_r(c)=\int_0^\infty e^{-cx}F_r(x)^2\,dx,
 \qquad \beta={s\over c}.
\tag{10}
\]

La dilatación de Laguerre y
\(L_r^{(1)}=\sum_{k=0}^rL_k\) producen la expansión exacta

\[
 F_r(x)=\sum_{j=0}^r a_{rj}(\beta)L_j(cx),
\tag{11}
\]

con

\[
 \sum_{r\ge j}a_{rj}(\beta)z^r
 ={\beta^jz^j\over
   (1-z)(1+(\beta-1)z)^{j+1}}.
\tag{12}
\]

Por ortogonalidad ordinaria,

\[
 \boxed{cI_r(c)=\sum_{j=0}^ra_{rj}(\beta)^2.}
\tag{13}
\]

Las sumas binomiales de (12), o equivalentemente Parseval aplicado a
(11), dan

\[
 \lim_{r\to\infty}I_r(c)^{1/(2r)}
 =2\beta-1={2s-c\over c}.
\tag{14}
\]

Para claridad, el límite superior sale de
\(\sum_j|a_{rj}|\le C_\beta(2\beta-1)^r\). Cuando \(\beta>2\), los
coeficientes alternan con el signo \((-1)^{r-j}\) y

\[
 \sum_j|a_{rj}|=
 { (2\beta-1)^{r+1}+(-1)^r\over2\beta};
\tag{15}
\]

entonces \(\|a_r\|_1/\sqrt{r+1}\le\|a_r\|_2\le\|a_r\|_1\)
da también el límite inferior. Esto basta para el exponente \(a=1\);
para \(a\ge2\) sólo se necesita el límite superior.

La transferencia a primos requiere uniformidad porque el saddle se mueve con
\(r\). La detallamos. Para \(a\ge1\), ponga

\[
 S_{r,a}:=\sum_p{\log p\over p^{as}}F_r(a\log p)^2.
\tag{16}
\]

Con \(x=a\log p\), su forma de Stieltjes es

\[
 S_{r,a}=\int_0^\infty e^{-sx}F_r(x)^2
                 \,d\vartheta(e^{x/a}),
\qquad
 {1\over a}I_r\!\left(s-{1\over a}\right)
 =\int_0^\infty e^{-sx}F_r(x)^2\,d(e^{x/a}).
\tag{16a}
\]

Sea \(c_a=s-1/a>0\). La medida de probabilidad con densidad proporcional a
\(e^{-c_ax}F_r(x)^2\) se concentra en un intervalo móvil
\([\delta_ar,C_ar]\). Esto se deduce sin una asintótica puntual de Laguerre:
para \(0<t<c_a\), Markov aplicado a \(e^{\pm t x}\), (10) y (14) dan

\[
 \begin{aligned}
 \Pr(x\le\delta r)&\le e^{t\delta r}{I_r(c_a+t)\over I_r(c_a)},\\
 \Pr(x\ge Cr)&\le e^{-tCr}{I_r(c_a-t)\over I_r(c_a)}.
 \end{aligned}
\tag{16b}
\]

Primero se fija \(t\), y después \(\delta_a>0\) pequeño y \(C_a<\infty\)
grande; (14) hace ambos lados \(O(e^{-\eta_ar})\). En ese intervalo
\(x/a\asymp r\) para cada \(a\) fijo. La forma efectiva de la PNT

\[
 \vartheta(e^u)=e^u+O\!\left(e^u
 e^{-c_0u^{3/5}(\log u)^{-1/5}}\right)
\tag{16c}
\]

es por tanto uniforme en todo el saddle: su error relativo es
\(O(e^{-c_ar^{3/5}(\log r)^{-1/5}})\). Para convertir esto en una
afirmación uniforme sobre el peso, subdivida
\([\delta_ar,C_ar]\) en intervalos de longitud \(h_r=r^{-A}\). Para \(A\)
fijo, (16c) da, uniformemente en todas esas celdas,

\[
 \vartheta(e^{(x+h_r)/a})-\vartheta(e^{x/a})
 ={e^{x/a}h_r\over a}\,(1+o_{s,a}(1)),
\tag{16d}
\]

porque el error de (16c), dividido por \(h_r\), todavía tiende a cero. No
hace falta una cota puntual del polinomio. Derivando (11) y usando
\((L_j)'=-\sum_{k<j}L_k\), la matriz de derivación en la base ortogonal
tiene sumas de prefijos; Cauchy da

\[
 \int_0^\infty e^{-c_ax}|F_r'(x)|^2dx
 \le c_a^2r^2 I_r(c_a).
\tag{16e}
\]

Otra aplicación de Cauchy--Schwarz da entonces

\[
 \int_{\delta_ar}^{C_ar}
 \left|{d\over dx}\{e^{-c_ax}F_r(x)^2\}\right|dx
 \le(c_a+2c_ar)I_r(c_a).
\tag{16f}
\]

Se elige, por ejemplo, \(A=4\). Las sumas superior
y inferior de Darboux difieren entonces en \(o(I_r(c_a))\), y (16d) convierte
cualquiera de ellas en la integral principal. Las dos colas ya son
\(O(e^{-\eta_ar})I_r(c_a)\): para la medida prima esto se sigue de
\(\vartheta(y)\le Cy\), integración por partes y (16e), aplicando (16b)
tanto a \(F_r\) como a su derivada (que tiene grado \(r-1\) y la misma
localización lineal). Por tanto, para todo \(a\) fijo,

\[
 S_{r,a}={1+o_{s,a}(1)\over a}
 I_r\!\left(s-{1\over a}\right).
\tag{16g}
\]

Por (14), esto da

\[
 \lim_{r\to\infty}S_{r,a}^{1/(2r)}
 ={as+1\over as-1},
\tag{17}
\]

para cada \(a\) fijo; sólo usaremos esta igualdad para \(a=1\).
El mismo argumento, o (16b) con \(R\) fijo, prueba (8). No se requiere
uniformidad en \(s\).

No se intercambia ahora un límite con la suma infinita en \(a\). Para tratar
simultáneamente todas las potencias superiores, defina

\[
 \Theta_{\ge2}(e^X)
 :=\sum_{\substack{p^a\le e^X\\a\ge2}}\log p.
\tag{17a}
\]

La cota de Chebyshev \(\vartheta(y)\le C y\) da

\[
 \Theta_{\ge2}(e^X)
 \le C e^{X/2}+C\sum_{3\le a\le X/\log2}e^{X/a}
 \le C' e^{X/2}.
\tag{17b}
\]

Integración por partes, (16e) y (17b) implican de manera uniforme

\[
 \sum_{a\ge2}S_{r,a}
 \le C_s(1+r)I_r\!\left(s-{1\over2}\right).
\tag{17c}
\]

La base de (14) decrece estrictamente con \(c\). Comparando (17c) con
(16g) para \(a=1\), se obtiene, sin falta de uniformidad,

\[
 \sum_{a\ge2}S_{r,a}=o_s(S_{r,1}).
\tag{18}
\]

Así (18) incluye de una vez todas las potencias primas, no una truncación.

Queda retirar la media. Su función generatriz exacta es

\[
 \sum_{r\ge0}z^r
 \sum_{m\ge2}{\Lambda(m)\over m^s}F_r(\log m)
 ={1\over(1-z)^2}\,
 \mathcal L\!\left({s\over1-z}\right).
\tag{19}
\]

Para \(s\) suficientemente próximo a uno, el polo de \(\mathcal L\) en
\(1\), que corresponde a \(z=1-s\), es la singularidad más cercana al
origen. En consecuencia

\[
 |\mu_{r,s}|^2=o_s(S_{r,1}).
\tag{20}
\]

También puede verse la separación de bases en el modelo principal:

\[
 \int_0^\infty e^{-(s-1)x}F_r(x)\,dx
 ={1\over s}\left\{1+{(-1)^r\over(s-1)^{r+1}}\right\},
\tag{21}
\]

mientras (14) tiene base \((s+1)/(s-1)\). Las restantes singularidades
de (19) están a distancia fija del polo y no alteran (20) al reducir
\(s_0\), si es necesario.

Las ecuaciones (18)--(20) prueban (7). Para (9), escriba
\(x=\log p,c=\log k\). Cuando \(p>K\),

\[
 (\mathsf T_sF_r)(pk)
 ={xF_r(x)+C_{r,k}\over x+c}.
\tag{22}
\]

Después de restar \(\mu_{r,s}\), el numerador es

\[
 x(F_r(x)-\mu_{r,s})+C_{r,k}-c\mu_{r,s}.
\tag{23}
\]

Por (8), \(x/(x+c)\to1\) en la medida cuadrática de los primos. Para
\(k\) fijo, la cota clásica
\(|L_r^{(1)}(y)|\le(r+1)e^{y/2}\) muestra que
\(C_{r,k}=O_{s,k}(r)\); (20) y Cauchy eliminan los dos últimos términos
de (23). Esto prueba (9). \(\square\)

## 4. El vector fijo alcanza la norma uno

**Teorema 4.1 (casi extremalidad Laguerre).** Para cada
\(s\in(1,s_0)\),

\[
 \boxed{\lim_{r\to\infty}Q_r(s)=1.}
\tag{24}
\]

**Prueba.** Fijemos \(K\). Los enteros

\[
 N=pk,\qquad 1\le k\le K,\quad p>K\text{ primo},
\tag{25}
\]

tienen representación única de esta forma: \(p\) es el único factor primo
de \(N\) mayor que \(K\). Al restringir la norma de salida a los estados
(25), usar (9) y \(-\zeta'(s)=\mathcal L_s\zeta(s)\), se obtiene

\[
 \begin{aligned}
 \|\mathsf T_s\widetilde F_r\|_{L^2(\Pi_s)}^2
 &\ge {1+o_s(1)\over\mathcal L_s\zeta(s)}
       \sum_{k=1}^K{k^{-s}}M_r.
 \end{aligned}
\tag{26}
\]

Por (7),

\[
 \liminf_{r\to\infty}Q_r(s)
 \ge {\sum_{k=1}^Kk^{-s}\over\zeta(s)}.
\tag{27}
\]

Haciendo \(K\to\infty\), el lado derecho tiende a uno. Jensen da el
límite superior uno. \(\square\)

Ésta es una obstrucción sobre el vector real, no sobre funciones test
artificiales. También cuantifica el mecanismo: para todo \(K\), el defecto
asintótico es a lo sumo la masa zeta de los cofactores \(k>K\); no existe una
constante positiva uniforme en el grado.

## 5. El comparador Gamma tiene el comportamiento opuesto

Sea \(\varepsilon=s-1\), \(X\sim\mathrm{Exp}(\varepsilon)\),
\(U\sim\Gamma(2,\varepsilon)\), y

\[
 (\mathsf C_\varepsilon h)(u)={1\over u}\int_0^u h(x)\,dx.
\tag{28}
\]

Ponga \(\beta=s/\varepsilon\) y use los coeficientes (12) con
\(c=\varepsilon\). Como

\[
 F_r(x)=\sum_{j=0}^ra_{rj}(\beta)L_j(\varepsilon x),
\tag{29}
\]

la constante \(a_{r0}\) es exactamente la media. Las identidades

\[
 \mathsf C_\varepsilon L_j(\varepsilon x)
 ={1\over j+1}L_j^{(1)}(\varepsilon u)
\tag{30}
\]

y las dos ortogonalidades dan el cociente exacto

\[
 \boxed{
 Q_r^\Gamma(s)
 ={\displaystyle\sum_{j=1}^r{a_{rj}(\beta)^2\over j+1}
   \over
   \displaystyle\sum_{j=1}^ra_{rj}(\beta)^2}.}
\tag{31}
\]

Para todo \(J\) fijo, (12) implica

\[
 {\sum_{j=1}^Ja_{rj}(\beta)^2
  \over\sum_{j=1}^ra_{rj}(\beta)^2}\longrightarrow0;
\tag{32}
\]

el denominador contiene \(a_{rr}^2=\beta^{2r}\), mientras cada índice fijo
tiene base estrictamente menor que \(\beta\). Separando (31) en
\(j\le J\) y \(j>J\), y después haciendo \(J\to\infty\), se obtiene

\[
 \boxed{Q_r^\Gamma(s)\longrightarrow0.}
\tag{33}
\]

Así la coercividad del continuo no sólo deja de transferirse: el cociente
continuo tiende a cero mientras el aritmético tiende a uno.

## 6. La diferencia firmada vive en las medias, no en los cocientes

La combinación completa de `104_44` es

\[
 \mathcal B_{n,s}
 =s\left\{\mathcal L_s\,\mathbb E_{\nu_s}f_{n,s}
 -{1\over\varepsilon}\mathbb E_{\mathrm{Exp}(\varepsilon)}f_{n,s}
 \right\},
 \qquad
 \lim_{s\downarrow1}\mathcal B_{n,s}=B_n.
\tag{34}
\]

Los cocientes (6) y (31) sólo ven los vectores después de retirar por
separado esas dos medias. Hay una prueba algebraica de que no contienen el
signo de (34). Para cualquier constante real \(c\),

\[
 Q_r(s;F_r+c)=Q_r(s;F_r),\qquad
 Q_r^\Gamma(s;F_r+c)=Q_r^\Gamma(s;F_r),
\tag{35}
\]

pero

\[
 \boxed{
 \mathcal B_s[F_r+c]-\mathcal B_s[F_r]
 =sc\left(\mathcal L_s-{1\over\varepsilon}\right).}
\tag{36}
\]

El factor entre paréntesis no es cero y tiende a \(-\gamma\). Por tanto los
dos cocientes pueden permanecer idénticos mientras la forma firmada cruza
cualquier umbral al variar \(c\). Para el polinomio real \(c\) está fijado,
pero recuperarlo no basta: la media aritmética restante en (34) es justamente
el momento unilateral que se quería demostrar. La recentralización lo ha
eliminado, no estimado.

## 7. Falsificador off-line

El argumento de las Secciones 3--6 usa la factorización Euler real; no se
aplica automáticamente a un divisor de ceros prescrito. El gate relevante
aparece al intentar continuar (34) al borde y olvidar residuos. Para el
cuarteto con \(e^\alpha=2\) y \(\theta=0\), el aporte es exactamente

\[
 \lambda_n^{\rm off}
 =8-8\cosh(n\log2)
 =8-4(2^n+2^{-n})<0.
\tag{37}
\]

Una transferencia de los cocientes centrados que concluyera una cota
unilateral sin conservar (37) estaría falsada. El archivo de comprobación
verifica (37) con racionales; no usa aproximaciones de ceros.

## 8. Decisión

```text
probado incondicionalmente:
  el saddle cuadrático del vector no escalado está dominado por primos;
  todas las potencias p^a, a>=2, son exponencialmente menores allí;
  Q_r(s) -> 1 para el vector Laguerre aritmético centrado;
  Q_r^Gamma(s) -> 0, con cociente diagonal exacto;
  ambos cocientes son ciegos a la diferencia firmada de medias.

descartado:
  no-alineación uniforme del vector fijo mediante T_s;
  transferir la coercividad del comparador Gamma al canal von Mangoldt;
  deducir B_n de cocientes centrados o defectos de Jensen.

permanece abierto:
  una cota lineal unilateral directa para la diferencia de medias (34),
  conservando sus residuos al llevar s al borde;
  B_n <= (1501/2002) A_n, A1 y RH.
```

`tools/fixed_laguerre_markov_extremal_check.py` comprueba con `Fraction` la
expansión (11)--(13), el cociente Gamma (31), la ceguera por traslación
(35)--(36), la fila exacta (22) y el falsificador (37). Los cocientes impresos
son diagnósticos derivados de enteros exactos; ningún enunciado usa coma
flotante.
