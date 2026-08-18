# 104_93 — Energía discreta de Cramér y gate de Selberg de orden variable

**Corrección de prioridad bibliográfica.** La equivalencia (L^2) continua
subyacente entre RH y la energía ponderada de (psi(x)-x) pertenece al
marco clásico de Cramér--Ingham--Titchmarsh. Hasta completar un gate externo
con referencias y numeración exactas, no se reclama novedad para la
equivalencia (3) ni para su transferencia discreta estándar. En cualquier
caso, esta coordenada queda fuera del frente activo: elimina el andamiaje
compacto--cola y vuelve a presentar RH como una energía global.

**Resultado (equivalencia, no demostración de RH).** Defina

\[
 b_n={\Lambda(n)-1\over\log n},\qquad
 B_m=\sum_{2\le n\le m}b_n,
 \tag{1}
\]

y la energía creciente

\[
 \mathcal E(N)=\sum_{m=2}^{N}{B_m^2\over m(m+1)}.
 \tag{2}
\]

Entonces

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \sup_N\mathcal E(N)<\infty
 \quad\Longleftrightarrow\quad
 \mathcal E(N)=N^{o(1)}.}
 \tag{3}
\]

Además, si \(\rho=\beta+i\gamma\) es un cero no trivial con
\(\beta>1/2\), entonces

\[
 \boxed{
 \limsup_{N\to\infty}{\log\mathcal E(N)\over\log N}
 \ge 2\beta-1.}
 \tag{4}
\]

La energía tiene la identidad finita exacta

\[
 \boxed{
 \mathcal E(N)=
 \sum_{r,s\le N}b_rb_s
 \left\{{1\over\max(r,s)}-{1\over N+1}\right\}.}
 \tag{5}
\]

Por tanto el término que habría que acotar no es una convolución de
Selberg: es una covarianza hermítica en la variable cociente, pues

\[
 {1\over\max(r,s)}
 ={1\over\sqrt{rs}}
   \exp\!\left(-{1\over2}|\log(r/s)|\right).
 \tag{6}
\]

La jerarquía de Selberg, incluso permitiendo un orden que varíe, no
proporciona automáticamente (3). Al centrar por el comparador \(1\), su
segundo coeficiente ya tiene ambos signos. Sin centrar, la jerarquía
positiva conserva solamente la coordenada producto \(rs\), y la resta del
comparador devuelve precisamente la forma firmada. Conservar en cambio la
marca \(r/s\) deja como residuo (5), que por (3) tiene fuerza RH.

Éste es un **no-go de la clase de reescrituras Selberg/Vaughan**, no un
teorema de imposibilidad universal. Una desigualdad nueva y específica de
la colocación de los primos ordinarios todavía podría probar
\(\mathcal E(N)=N^{o(1)}\); hacerlo probaría RH. Este documento no prueba
esa desigualdad, Deep-\(\Lambda\), A1 ni RH.

**No duplicación interna.** `E101_090` aísla la covarianza de cociente
para los coeficientes \(\Lambda(n)-1\) con cutoff balanceado, y `104_89`
usa la energía continua de \(J(x)-\mathrm{Li}(x)\) para el gate
BSY. Aquí se cierra la versión discreta exacta (1)--(5), se identifica el
umbral mínimo \(N^{o(1)}\), se obtiene la obstrucción cuantitativa (4), y
se audita contra ella toda la jerarquía centrada de Selberg.

---

## 1. La forma max es exactamente la energía

Extienda \(B_m\) a la función escalonada

\[
 B(x)=B_m\qquad(m\le x<m+1).
 \tag{7}
\]

Entonces

\[
 \int_2^{N+1}{B(x)^2\over x^2}\,dx
 =\sum_{m=2}^{N}B_m^2
   \left({1\over m}-{1\over m+1}\right)
 =\mathcal E(N).
 \tag{8}
\]

Al expandir \(B_m^2\), todas las sumas son finitas y

\[
\begin{aligned}
 \mathcal E(N)
 &=\sum_{r,s\le N}b_rb_s
   \sum_{m=\max(r,s)}^N{1\over m(m+1)}\\
 &=\sum_{r,s\le N}b_rb_s
   \left\{{1\over\max(r,s)}-{1\over N+1}\right\},
\end{aligned}
\tag{9}
\]

que prueba (5). El término \(-(N+1)^{-1}B_N^2\) es el borde móvil; no
puede omitirse antes de tomar el límite.

La identidad (6) muestra las dos geometrías incompatibles:

\[
 \text{Selberg/Dirichlet: }\log(rs)=\log r+\log s,
 \qquad
 \text{Cramér: }|\log(r/s)|=|\log r-\log s|.
 \tag{10}
\]

## 2. RH implica energía finita

Ponga

\[
 J(x)=\sum_{2\le n\le x}{\Lambda(n)\over\log n},
 \qquad
 L_2(x)=\int_2^x{dt\over\log t},
 \qquad
 A(x)=J(x)-L_2(x).
 \tag{11}
\]

La suma parcial de Stieltjes es exacta:

\[
 A(x)={\psi(x)-x\over\log x}
 +\int_2^x{\psi(t)-t\over t\log^2t}\,dt
 +{2\over\log2}.
 \tag{12}
\]

Bajo RH, la cota cuadrática de Cramér da

\[
 \int_Y^{2Y}|\psi(t)-t|^2dt\ll Y^2.
 \tag{13}
\]

En el bloque \([Y,2Y]\), (13) implica

\[
 \int_Y^{2Y}{|\psi(x)-x|^2\over x^2\log^2x}\,dx
 \ll {1\over\log^2Y}.
 \tag{14}
\]

La suma de (14) sobre bloques diádicos converge. Asimismo,
Cauchy--Schwarz en cada bloque da

\[
 \int_2^x{\psi(t)-t\over t\log^2t}\,dt
 =O\!\left({\sqrt x\over\log^2x}\right)+O(1),
 \tag{15}
\]

y por ello el cuadrado de (15), dividido por \(x^2\), también es
integrable. De (12)--(15),

\[
 \int_2^\infty {A(x)^2\over x^2}\,dx<\infty.
 \tag{16}
\]

Falta solamente comparar la integral con el comparador discreto. Como
\(f(x)=1/\log x\) es positivo y decreciente, para todo entero \(m\ge2\),

\[
 0\le
 \sum_{n=2}^m f(n)-\int_2^m f(t)dt
 \le f(2).
 \tag{17}
\]

En efecto, en cada intervalo \([n,n+1]\),
\(f(n+1)\le\int_n^{n+1}f\le f(n)\), y los errores telescopan. Por (1),
\(B(x)\) difiere de \(A(x)\) por una función acotada. Las ecuaciones
(16)--(17) y (8) prueban

\[
 \mathrm {RH}\quad\Longrightarrow\quad
 \sup_N\mathcal E(N)<\infty.
 \tag{18}
\]

## 3. Energía subpolinomial excluye todo cero derecho

Para \(\Re s>1\), defina

\[
 G(s)=\sum_{n\ge2}{\Lambda(n)-1\over\log n}\,n^{-s}.
 \tag{19}
\]

El producto de Euler y la derivación término a término dan

\[
 G(s)=\log\zeta(s)-C(s),
 \qquad
 C(s)=\sum_{n\ge2}{n^{-s}\over\log n},
 \qquad
 C'(s)=1-\zeta(s),
 \tag{20}
\]

y por tanto

\[
 \boxed{G'(s)={\zeta'(s)\over\zeta(s)}+\zeta(s)-1.}
 \tag{21}
\]

Por sumación de Abel,

\[
 G(s)=s\int_2^\infty B(x)x^{-s-1}\,dx.
 \tag{22}
\]

Suponga ahora \(\mathcal E(N)=N^{o(1)}\). Para cada \(\delta>0\), la
sumación por partes aplicada a los incrementos positivos de (2) da

\[
 \int_2^\infty B(x)^2x^{-2-\delta}dx<\infty.
 \tag{23}
\]

Más explícitamente, use
\(\mathcal E(N)\ll_\delta N^{\delta/2}\) y

\[
 \int_m^{m+1}B(x)^2x^{-2-\delta}dx
 \le m^{-\delta}{B_m^2\over m(m+1)}.
\]

La serie resultante converge porque
\(\sum m^{-\delta}d\mathcal E(m)\) converge por Abel.

Fije \(\sigma>1/2\) y elija \(0<\delta<2\sigma-1\). Por
Cauchy--Schwarz,

\[
\begin{aligned}
 \int_2^\infty |B(x)|x^{-\sigma-1}dx
 &\le
 \left(\int_2^\infty B(x)^2x^{-2-\delta}dx\right)^{1/2}
 \left(\int_2^\infty x^{-2\sigma+\delta}dx\right)^{1/2}
 <\infty.
\end{aligned}
\tag{24}
\]

El mismo argumento es uniforme sobre compactos. Así (22) prolonga
\(G\) holomórficamente a \(\Re s>1/2\).

La identidad (21), válida inicialmente en \(\Re s>1\), continúa en el
semiplano perforado por los ceros. Si \(\rho\), \(\Re\rho>1/2\), fuera
un cero de multiplicidad \(m_\rho\), entonces
\(\zeta'/\zeta\) tendría en \(\rho\) un polo simple de residuo
\(m_\rho\), mientras \(G'\) y \(\zeta-1\) serían holomorfas allí. Esto
es imposible. No hay ceros a la derecha de la línea; la ecuación funcional
los excluye también a la izquierda. Esto prueba

\[
 \mathcal E(N)=N^{o(1)}\quad\Longrightarrow\quad\mathrm {RH}.
 \tag{25}
\]

Junto con (18) queda demostrada (3).

### 3.1 Precio cuantitativo de un cero exterior

Suponga que existe un cero con parte real \(\beta>1/2\). Si

\[
 L:=\limsup_{N\to\infty}{\log\mathcal E(N)\over\log N}
 <2\beta-1,
\]

elija \(\alpha\) con \(L<\alpha<2\beta-1\). Entonces
\(\mathcal E(N)=O(N^\alpha)\). La prueba de (23)--(24), ahora con todo
\(\delta>\alpha\), prolonga \(G\) a
\(\Re s>(1+\alpha)/2\), semiplano que contiene al cero dado. La misma
contradicción con (21) prueba (4).

## 4. La identidad centrada de Selberg pierde el signo

Sea \({\bf u}(1)=0\), \({\bf u}(n)=1\) para \(n\ge2\), y ponga

\[
 e=\Lambda-{\bf u},
 \qquad
 (\mathsf D f)(n)=(\log n)f(n).
 \tag{26}
\]

La identidad positiva de Selberg es

\[
 b_{\rm S}=\mathsf D\Lambda+\Lambda*\Lambda\ge0.
 \tag{27}
\]

Al centrarla por el comparador que define (1), se obtiene exactamente

\[
\boxed{
 r:=\mathsf De+e*e
 =b_{\rm S}+2\Lambda-3\log+\tau-2,
}
\tag{28}
\]

para \(n\ge2\), donde \(\tau(n)\) es el número de divisores. En efecto,

\[
 \Lambda*{\bf u}=\log-\Lambda,
 \qquad
 {\bf u}*{\bf u}=\tau-2.
 \tag{29}
\]

El coeficiente centrado ya cambia de signo sobre primos:

\[
 r(p)=\log p\,(\log p-1),
 \qquad r(2)<0<r(3),
 \tag{30}
\]

porque \(2<e<3\). Por tanto (27) no se convierte en una inducción
unilateral para (1).

La jerarquía completa exhibe la misma resta. En \(\Re s>1\), ponga

\[
 H(s)=e^{G(s)}=\zeta(s)e^{-C(s)},
 \qquad
 E(s)=\sum_{n\ge2}e(n)n^{-s}=-{H'(s)\over H(s)}.
 \tag{31}
\]

Defina \(S_1=e\) y

\[
 S_{k+1}=\mathsf D S_k+e*S_k.
 \tag{32}
\]

Una inducción por derivación prueba

\[
 \sum_{n\ge1}{S_k(n)\over n^s}
 =(-1)^k{H^{(k)}(s)\over H(s)}.
 \tag{33}
\]

Para \(k=2\), (33) es precisamente (28). En contraste, la jerarquía
sin centrar, obtenida reemplazando \(e\) por \(\Lambda\), sí tiene
coeficientes no negativos en todos los órdenes; pero al restar el canal
continuo reaparecen (28) y sus iterados. Estimar por separado las piezas
positivas destruye la cancelación polo--primos.

## 5. Por qué variar el orden no crea la energía faltante

Las operaciones \(\mathsf D\) y \(*\) de (27)--(33) producen pesos
polinomiales en \(\log r+\log s\) sobre fibras \(rs=n\). Aumentar el
orden cambia el polinomio, no la aplicación de proyección

\[
 (r,s)\longmapsto rs.
 \tag{34}
\]

La energía (5) necesita, en cambio, la marca \(r/s\). Si se conserva esa
marca antes de aplicar Cauchy--Schwarz, queda exactamente la covarianza
de cociente (5); si se la descarta, ninguna colección de momentos de
\(\log(rs)\) controla por sí sola el kernel (6) como una desigualdad
unilateral. La pérdida de información de la proyección se ve ya en las
dos medidas positivas sobre \(\mathbb R_+^2\)

\[
 \nu_1=\delta_{(0,2)}+\delta_{(2,0)},
 \qquad
 \nu_2=2\delta_{(1,1)}.
 \tag{34a}
\]

Ambas tienen el mismo pushforward \(2\delta_2\) por
\((u,v)\mapsto u+v\), incluso con todos sus momentos, pero integran
\(e^{-|u-v|/2}\) a \(2e^{-1}\) y a \(2\), respectivamente. El testigo
no pretende reemplazar la estructura tensorial del vector Mangoldt;
prueba exactamente que una estimación que primero proyecta una forma
bivariada al canal suma ya no contiene la marca requerida. Invertir la
proyección usando de nuevo todos los coeficientes de Mangoldt restaura el
vector original, pero no aporta una cota. Éste es el mismo muro
producto/cociente probado para el cutoff balanceado en `E101_090`.

Hay un test adicional contra estimaciones diagonales. Para un primo,

\[
 b_p=1-{1\over\log p},
\]

de modo que Mertens implica

\[
 \sum_{p\le N}{b_p^2\over p}\sim\log\log N.
 \tag{35}
\]

La diagonal positiva del primer término de (5) diverge, mientras bajo RH
la suma completa está acotada por (3). Toda prueba mediante valores
absolutos, una diagonal de Montgomery--Vaughan o normas Type I/II separadas
pierde necesariamente la cancelación negativa fuera de la diagonal y el
borde móvil. Una descomposición de Vaughan sigue siendo una identidad
válida, pero su estimación útil tendría que conservar esa cancelación
global; eso vuelve a ser (5), no una consecuencia automática de la
descomposición.

### Alcance del no-go

`104_78` aporta el falsificador de clase exacto. Su monoide libre satisface
renovación unitaria, torres primas de multiplicidad uno, pesos positivos,
ecuación funcional, una ley prima exponencialmente precisa en el grado y
la jerarquía positiva de Selberg en **todo** orden. Sin embargo posee

\[
 \beta_+=\log_6 3>{1\over2}
\]

y densidad Deep igual a \(1/4\). Aplicando la demostración de la
Sección 3 a su función de conteo graduada, su energía centrada análoga no
puede ser subpolinomial y tiene exponente inferior al menos

\[
 2\log_6 3-1>0.
 \tag{36}
\]

El modelo es reticular y no usa la colocación de los enteros ni de los
primos ordinarios. Por ello no contradice (3). Sí prueba que renovación,
positividad y la jerarquía Selberg de orden variable, tomadas como axiomas
abstractos, no implican la energía requerida. El dato que un sucesor debe
usar sigue siendo la colocación literal de los pesos ordinarios
\(\Lambda(m)\).

## 6. Estado lógico

```text
EQUIVALENCIA PROBADA:
  RH <=> sup_N E(N)<infinito <=> E(N)=N^{o(1)}.

IDENTIDADES PROBADAS:
  forma discreta max/quotient (5)--(6);
  identidad Selberg centrada (28);
  jerarquía centrada de orden variable (32)--(33);
  cambio de signo r(2)<0<r(3);
  costo energético de un cero exterior (4).

NO-GO DE CLASE PROBADO:
  positividad de la jerarquía Selberg sin centrar,
  y reescrituras Vaughan/Type I--II estimadas por diagonales separadas
  NO implican energía subpolinomial.

NO DESCARTADO:
  una desigualdad nueva para la covarianza firmada (5) que use la
  colocación exacta de todos los primos ordinarios.

NO PROBADO:
  E(N)=N^{o(1)} incondicionalmente;
  Deep-Lambda, A1 o RH.
```

## 7. Reproducción

Desde el directorio `tools`:

```bash
python3 discrete_cramer_selberg_gate_check.py
```

El checker usa solamente `Fraction`. Verifica (5) para familias racionales
arbitrarias, la telescopía del borde y cotas racionales de la serie
\(\mathrm{arctanh}\,\) que certifican
\(\log2<1<\log3\). No usa valores de \(\zeta\), ceros ni punto flotante.
