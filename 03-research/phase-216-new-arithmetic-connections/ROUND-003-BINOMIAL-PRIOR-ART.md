# Ronda 003 — Antecedentes exactos del retículo binomial

Fecha de corte: 2026-11-28. Objeto revisado: §8–8.1 de ROUND-002-CRYSTALLINE.md. **Dictamen:** el retículo construido es exactamente un dual truncado de un módulo de Iwasawa con acción afín, seguido de un twist. No es sólo una analogía con la teoría clásica. El corolario cristalino formulado con todas las clases adyacentes iguales no se encontró literalmente en los pasajes leídos, pero se obtiene de esa construcción clásica mediante un cálculo de primera superdiagonal y estabilidad tensorial. No hay evidencia suficiente para reclamar originalidad del corolario, y menos aún una nueva área.

## 1. Identificación exacta, incluidos signos y twist

Sea Λ=Z_p[[Z_p]], identificado con Z_p[[T]] enviando la masa de Dirac δ_x a (1+T)^x. Sea I=(T). Para n≥0 ponemos

\[
B_n=\{P\in\mathbb Q_p[t]:\deg P\le n,\ P(\mathbb Z_p)\subset\mathbb Z_p\}.
\]

El emparejamiento entre medidas y funciones da una identificación integral

\[
B_n\simeq\operatorname{Hom}_{\mathbb Z_p}(\Lambda/I^{n+1},\mathbb Z_p).
\tag{1}
\]

No es preciso tomar límites ni estimar factoriales para comprobarla. En efecto, T=δ₁−δ₀ y

\[
\langle T^k,P\rangle=\Delta^kP(0),\qquad
\left\langle T^k,\binom tj\right\rangle=\delta_{kj}\quad(0\le k,j\le n).
\]

Las bases T^k y binom(t,j) son duales. La anulación de las diferencias de orden n+1 identifica el aniquilador de I^{n+1} y demuestra (1).

Ahora sean χ:G→Z_p^× y c:G→Z_p un cociclo, con c(gh)=c(g)+χ(g)c(h). La acción afín

\[
h_g(x)=\chi(g)x-c(g)
\]

es una acción izquierda de G sobre Z_p. Su acción por imagen directa sobre medidas, transportada a series, es

\[
gF(T)=(1+T)^{-c(g)}F\big((1+T)^{\chi(g)}-1\big).
\tag{2}
\]

Los coeficientes son integrales; (2) preserva I^{n+1} y es invertible. La multiplicación por (1+T)^{-c(g)} significa que se trata de un módulo con acción de torsor, no de una acción por automorfismos de álgebras que conserve la unidad.

En el dual contragrediente, (2) actúa como

\[
(gP)(t)=P(h_g^{-1}(t))=P\left(\frac{t+c(g)}{\chi(g)}\right).
\]

Por tanto el retículo de la ronda anterior es exactamente

\[
\boxed{L\simeq\mathbb Z_p(\chi^n)\otimes
(\Lambda/I^{n+1})^\vee}
\tag{3}
\]

para esta acción afín. Bajo (3), binom(t,j) corresponde a X^n binom(Y/X,j). La igualdad de acciones es literal, no solamente igualdad de graduados ni una isogenia.

## 2. Qué parte del enunciado cristalino requiere aún cálculo

La identificación (3) prueba integralidad y compatibilidad con la bandera de grados. Para identificar las clases adyacentes de forma integral, hay que conservar el segundo coeficiente superior de binom(t,j); conocer sólo los graduados no basta. El cálculo da

\[
\operatorname{coeff}_{v_{j-1}}(gv_j)
=\chi(g)^{n-j}\left(c(g)+\frac{j-1}{2}(1-\chi(g))\right).
\]

La diferencia con c es el coborde de −(j−1)/2. Para p impar esa constante es integral, luego cada clase adyacente es [c] en cohomología integral, sin reescalar. Para p=2 no se puede inferir lo mismo del coborde racional; el retículo sigue siendo estable, pero la identificación de clases requiere otro argumento o hipótesis.

Si la extensión racional definida por (χ,c) es cristalina, la representación racional subyacente a L es Sym^n(E) y por ello es cristalina. Se usa «retículo cristalino» en el sentido de retículo estable cuya representación racional es cristalina. No se demuestra una clasificación integral más fuerte de módulos filtrados, ni se impone una polarización adicional.

Así, la aportación de §8 al trabajo local es una comprobación explícita muy útil: anula el presunto coste positivo. Su alcance matemático combina (a) un retículo clásico, (b) el cálculo elemental del coborde y (c) cierre de representaciones cristalinas bajo potencias simétricas. No se ha encontrado una obstrucción nueva.

## 3. Comparación con textos primarios completos

### 3.1. Polinomios de valores enteros y dual de Iwasawa: coincidencia directa

Ehud de Shalit, [Mahler bases and elementary p-adic analysis](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.955.pdf), JTNB 28 (2016), 597–620: §1.1 describe la base binomial de Int(Z_p); §5.1, proposición 5.1, desarrolla el dual de medidas y la transformada de Iwasawa–Mahler. En el caso Z_p, δ_x se transforma en (1+T)^x. Se leyeron esas secciones completas. (1) es su truncación finita, con prueba explícita arriba. El paso de la acción afín a (2) se obtiene aplicando la fórmula a δ_x y extendiendo por continuidad.

### 3.2. Anillos binomiales: ya existe incluso la formulación universal

Kubrak–Shuklin–Zakharov, [Derived binomial rings I: integral Betti cohomology of log schemes, arXiv:2308.01110](https://arxiv.org/abs/2308.01110): se leyó §2.1, en particular la definición de aplicaciones polinomiales por diferencias, los pasajes sobre el dual de Z[A]/I^{n+1}, el lema 2.11 y las observaciones 2.12–2.13. Identifican los polinomios enteros, su racionalización y su conexión con distribuciones de G_m. La numeración corresponde al PDF consultado. El retículo binomial no inaugura esa conexión; está incluido en el marco previo, antes de pasar a la teoría derivada.

### 3.3. Logaritmo integral y torsor: coincide el mecanismo de construcción

Beilinson–Kings–Levin, [Topological polylogarithms and p-adic interpolation of L-values of totally real fields, arXiv:1410.4741](https://arxiv.org/abs/1410.4741), v1: se leyeron §§1.1–1.4. Construyen la completación de un anillo de grupo, sus cocientes por potencias del ideal de aumento, su identificación con Iwasawa y el haz logarítmico a partir de un torsor. En particular, definición 1.1.1, proposición 1.2.2 y proposiciones 1.4.1–1.4.3 suministran el entorno exacto de (2)–(3). Su escenario publicado en esos pasajes es topológico, no el corolario sobre G_K de §8; no se les atribuye ese corolario literal. La construcción de torsor y su representación integral, sin embargo, preceden claramente a nuestra aplicación.

### 3.4. Sharifi: antecedente directo con matrices binomiales y clases de Kummer

Romyar Sharifi, [Massey products and ideal class groups, arXiv:math/0308165](https://arxiv.org/abs/math/0308165), [texto primario](https://www.math.ucla.edu/~sharifi/publ/massey.pdf), §1.2, pp. 4–6: se leyó el pasaje completo. Para caracteres repetidos salvo quizá el último construye entradas superiores κ_{i,j}(h)=binom(χ̃(h),j−i) módulo p^m. Relaciona esas matrices con un cociente del anillo de grupo por una potencia del ideal de aumento y pasa a Kummer y sistemas de definición de productos de Massey. Es un antecedente mucho más directo que la mera existencia de una base de Mahler.

Las hipótesis son diferentes: allí χ:H→Z/p^nZ es un carácter **aditivo**, con la restricción q≤p^{n−m+1}; al pasar a cuerpos se supone que están presentes las raíces de unidad pertinentes. Aquí χ:G_K→Z_p^× es **multiplicativo** y varía la acción ciclotómica o de otro carácter; c es el cociclo de traslación, y la cristalinidad se obtiene por Sym^n. No se pueden borrar esas diferencias para atribuir a Sharifi el corolario exacto. Sí impiden presentar como nueva la conexión binomiales–matrices unipotentes–Kummer–anillo de grupo truncado–Massey.

## 4. Matriz de comparación del enunciado exacto

| Ingrediente de §8 | Coincidencia comprobada | Lo que no se encontró literalmente |
|---|---|---|
| Base binom(t,j) para todos los grados | De Shalit §1.1; marco de Kubrak–Shuklin–Zakharov §2.1 | Nada esencial en la elección del retículo. |
| Acción integral por t↦(t+c)/χ | Consecuencia inmediata de valores enteros; fórmula dual (2) demostrada aquí | Un enunciado etiquetado con exactamente estas variables no fue localizado. |
| Torre de rangos n+1 con acción del torsor | Modelo de anillo de grupo completado/logaritmo integral de Beilinson–Kings–Levin | No se atribuye una realización cristalina concreta a su texto topológico. |
| Matrices binomiales, clases repetidas y Kummer | Sharifi §1.2: fórmula explícita y cociente por ideal de aumento | Sus caracteres aditivos finitos y condiciones sobre raíces de unidad no son la acción cristalina multiplicativa de §8. |
| Todas las clases adyacentes exactamente [c], p impar | Cálculo expreso de coborde integral en §2 de esta nota | No localizado como proposición en los tres textos. |
| Realización cristalina para cualquier n | Consecuencia de la identificación racional con Sym^n(E) | No localizado en esos pasajes como teorema independiente. |
| Clases a_j[c] y división en bloques | Cambio diagonal y suma directa de §8.1 | No se hizo una búsqueda exhaustiva de ese corolario exacto. |

«No localizado literalmente» no significa «nuevo». En este caso hay una reducción explícita al aparato existente. La formulación exacta podría servir como lema explicativo en un artículo, atribuyendo las construcciones básicas; no está justificado presentarla como una conexión hasta ahora desconocida.

## 5. Qué queda fuera de esta reducción

La prueba depende de que las clases formen una sola familia cíclica y que el cociente de caracteres sea común. Clases independientes, cocientes distintos o estructuras adicionales fijadas pueden quedar fuera de (3), pero eso por sí solo no produce un coste positivo. También las construcciones multivariables de anillos binomiales y módulos de Iwasawa ya existen: sustituir una variable por varias sin más no acredita novedad.

Para un siguiente candidato hay que exhibir un enunciado que no se obtenga como subcociente, dual, twist o cambio de retículo de estas construcciones clásicas, y demostrar una cota u obstrucción que sobreviva a todas esas operaciones. Este frente bibliográfico no aporta todavía ese ejemplo.

## 6. Cobertura y consultas reproducibles

Se descargaron los cuatro PDFs de de Shalit, Kubrak–Shuklin–Zakharov, Beilinson–Kings–Levin y Sharifi a archivos temporales y se extrajeron los pasajes completos con pdftotext. La referencia de Sharifi fue aportada por el agente coordinador y luego leída directamente para esta nota. Se consultó también la descripción de Kings, *Degeneration of polylogarithms and special values of L-functions for totally real fields*, Documenta Math. 13 (2008), §2.3, mediante el resultado que reproduce ese pasaje: se usa sólo como pista adicional sobre logaritmo étale integral, no como fundamento de una identidad Galois.

Consultas ejecutadas:

1. `arxiv integral logarithm sheaf integer valued polynomials binomial Iwasawa algebra divided powers`
2. `binomial polynomial lattice affine group symmetric powers integral representations p-adic`
3. `Kings integral polylogarithm logarithm sheaf Iwasawa algebra arxiv`
4. `"Derived binomial rings I" arxiv`
5. `"Mahler" "Iwasawa" "binomial" polynomials measure`
6. `"crystalline" "binomial" "Kummer" representation lattice`
7. `"logarithm sheaf" "crystalline" "symmetric" integral`
8. `"integer-valued" "Galois" "symmetric" polynomials`

Límites: búsqueda dirigida, no examen exhaustivo de arXiv; no revisión completa de todos los artículos sobre logaritmos p-ádicos o extensiones iteradas; no atribución de resultados a snippets sin leer el pasaje correspondiente. Se excluyeron como evidencia independiente resultados que remitían a páginas del propio proyecto riemann. La conclusión fuerte que sí se sostiene es la identidad estructural (3), con prueba y antecedentes precisos.
