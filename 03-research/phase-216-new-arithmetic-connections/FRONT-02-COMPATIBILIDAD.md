# Frente 02 — Coste de realizar simultáneamente correspondencias sobre retículos

Fecha de corte bibliográfico: 28 de noviembre de 2026. Estado: exploración con resultados elementales demostrados; prioridad no establecida. Este documento no certifica RH/GRH ni presupone esa certificación.

La pregunta que sobrevive a la búsqueda de antecedentes es cuantitativa: **¿cuánto cuesta realizar un diagrama de correspondencias aritméticas sobre retículos prescritos, conservando simultáneamente sus identidades de composición?** Existencia racional, determinantes y existencia integral por separado no responden esta pregunta. La posible contribución está en obtener cotas aritméticas uniformes para familias específicas, no en anunciar una teoría nueva de retículos, alturas o edificios.

## 1. Un falso invariante nuevo que hay que descartar

Sea M una matriz de rango r sobre un cuerpo de números K. Sean Δ_B sus menores máximos no nulos. Normalizamos los valores absolutos y los pesos n_v para que la fórmula del producto diga Σ_v n_v log|a|_v=0. Definimos w_v(B)=−n_v log|Δ_B|_v/[K:Q]. Entonces

\[
\min_B\sum_v w_v(B)-\sum_v\min_B w_v(B)
=\frac1{[K:\mathbb Q]}\sum_v n_v\log\max_B|\Delta_B|_v.
\]

Prueba: la primera suma es cero para cada B por la fórmula del producto; la segunda cambia mínimo por máximo al cambiar el signo. El resultado es exactamente la altura proyectiva de las coordenadas de Plücker con la norma máximo. No es una nueva obstrucción local/global. Excluir lugares arquimedianos o modificar las elecciones permitidas cambia la pregunta y exige una definición adicional; no prueba novedad.

## 2. Objeto preciso: perfil integral con un retículo inicial fijado

Sea F un cuerpo discretamente valuado, O su anillo de valoración, π un uniformizante, V=F^d, L₀ un retículo completo y S un conjunto finito de endomorfismos de V. Para palabras w en S, incluida la vacía, ponemos

\[
C_n=\bigcap_{|w|\le n}w^{-1}L_0,
\qquad \kappa(n)=\operatorname{length}_O(L_0/C_n).
\]

Cada C_n es un retículo completo y

\[
C_{n+1}=L_0\cap\bigcap_{T\in S}T^{-1}C_n.
\]

El término «anclado» sólo significa que L₀ es parte del dato. Cambiar S y L₀ simultáneamente por conjugación no cambia κ; cambiar S dejando L₀ fijo puede cambiarlo arbitrariamente. No atribuimos prioridad a esta construcción: pertenece al entorno de subrepresentaciones integrales, cotrayectorias y estabilidad de productos de matrices.

**Lema de certificado finito.** Si C_n=C_{n+1}, C_n es estable bajo S y C_m=C_n para todo m≥n. Si κ(n)≤B para todo n, con B entero, se alcanza tal igualdad para algún n≤B. Si cada palabra satisface wL₀⊂π^(−a)L₀, entonces κ(n)≤da y hay estabilización a más tardar en da.

**Prueba.** La recurrencia convierte la igualdad en T C_n⊂C_n. Cada inclusión estricta de retículos aumenta la longitud al menos en uno, y una igualdad impide cualquier aumento posterior. Finalmente π^aL₀⊂C_n para todo n bajo la hipótesis de denominadores. Estas tres observaciones prueban las afirmaciones.

En particular, C_∞=∩_n C_n es un retículo completo si y sólo si existe un retículo completo estable L⊂L₀. En ese caso C_∞ es el mayor de ellos y minimiza length(L₀/L). En efecto, todo retículo estable está contenido en cada C_n; la cota de longitudes que proporciona L fuerza estabilización. Esto es un criterio elemental, no un teorema de novedad proclamada.

## 3. Determinantes idénticos; incompatibilidad integral ilimitada

Para N≥1 tomamos L₀=O² y

\[
A=\begin{pmatrix}1&\pi^{-N}\\0&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\\pi^{-N}&1\end{pmatrix}.
\]

Ambas matrices y todas sus palabras tienen determinante 1. A preserva Oe₁⊕π^NOe₂; B preserva π^NOe₁⊕Oe₂. Sin embargo, **no existe retículo completo estable bajo ambas**: si existiera, AB tendría matriz integral en una base de él; pero tr(AB)=2+π^(−2N) tiene valoración −2N y no es integral, incluso en característica residual 2.

Más precisamente,

\[
C_n=\pi^{nN}O^2,\qquad \kappa(n)=2nN.
\]

Prueba por inducción. Si C_n=π^(nN)O², las condiciones Ax,Bx∈C_n para x=(x₁,x₂) implican primero x₁,x₂∈π^(nN)O, y después, usando las coordenadas con términos π^(−N), x₁,x₂∈π^((n+1)N)O. La implicación inversa es inmediata. La recurrencia prueba el resultado.

Esto separa el control de covolúmenes del control simultáneo de composiciones. No es un contraejemplo a ningún paper de la serie: para transferirlo habría que identificar exactamente espacios, mapas y retículos de ese paper.

## 4. Ni todas las trazas de ciclos controlan el coste anclado

Con sólo A y el mismo L₀ se tiene

\[
C_n=Oe_1\oplus\pi^NOe_2\quad(n\ge1),\qquad\kappa(n)=N.
\]

La condición Ax∈L₀ fuerza x₂∈π^NO. Es suficiente para todas las potencias porque A^m=I+mπ^(−N)E₁₂ y m∈O. Sin embargo tr(A^m)=2 y det(A^m)=1 para todo m≥0, independientemente de N.

Por tanto es falsa cualquier cota del coste anclado que dependa solamente del rango y de las trazas/determinantes de palabras, aun disponiendo de todas las palabras. Las trazas pueden detectar ciertas obstrucciones a la existencia; no registran la posición del retículo inicial. Una propuesta basada en trazas de ciclos cortos debe incorporar además denominadores respecto de los retículos fijados u otro dato equivalente.

## 5. Versión para mapas rectangulares y pregunta concreta

Para un quiver finito Q, retículos Lᵢ,₀⊂Vᵢ y mapas T_e:Vᵢ→Vⱼ, definimos

\[
C_{i,n+1}=L_{i,0}\cap\bigcap_{e:i\to j}T_e^{-1}C_{j,n},
\qquad \kappa_Q(n)=\sum_i\operatorname{length}(L_{i,0}/C_{i,n}).
\]

El lema de estabilización sigue siendo válido con longitud total. Si Q es acíclico, no hay caminos de longitud mayor que su longitud máxima ℓ y el proceso estabiliza a más tardar en ℓ. Una cadena aislada no presenta la obstrucción de recurrencia del ejemplo A,B. Comparar cadenas exige especificar las flechas adicionales, sus dominios y relaciones; no se puede tratar automáticamente un lift theta rectangular como un automorfismo.

**Problema de investigación F02.** Especificar una familia aritmética de diagramas Q(θ), con twists admisibles θ, retículos de referencia y relaciones de intercambio fijadas. Obtener una cota efectiva del mínimo coste integral simultáneo, con dependencia explícita en rango, longitud del diagrama, denominadores de las flechas y obstrucciones cohomológicas; después controlar la suma de esos costes locales ponderados por log(Nv). La elección de θ debe ser global cuando así lo exige la familia: minimizar separadamente en cada lugar no garantiza un twist global admisible.

Para convertir esto en un teorema nuevo hacen falta: (i) una clase aritmética concreta no cubierta por un resultado existente; (ii) una cota mejor que multiplicar indiscriminadamente todos los denominadores; (iii) prueba de uniformidad en los parámetros que crecen; (iv) un ejemplo donde se alcance o se necesite la pérdida. Un primer caso abordable es un cuadrado de dos composiciones con retículos y normalizaciones determinados, antes de una cadena arbitraria.

## 6. Antecedentes que impiden reclamar novedad general

| Fuente primaria | Qué ya existe y qué obliga a distinguir |
|---|---|
| Khan–Maclagan, [Tropical Vector Bundles, 2405.03505](https://arxiv.org/abs/2405.03505), 2024 | Matroides valuados, fibras tropicales y filtraciones de estabilidad bajo hipótesis. La conexión retículos/matroides/estabilidad no basta como insight nuevo. |
| Kaveh–Manon, [Tropical vector bundles and matroids, 2405.03576](https://arxiv.org/abs/2405.03576), 2024 | Fibrados tóricos tropicales, clases características y descomposición. Hay que comparar construcciones exactas, no nombres. |
| Kashyap–Kaveh–Manon–Tsvelikhovskiy, [A Helly theorem for the Bruhat-Tits building, 2611.17844](https://arxiv.org/abs/2611.17844), 13/11/2026 | Una familia de retículos de rango m tiene base adaptada común si la tiene cada subfamilia de tamaño ≤m+1. Antecedente particularmente reciente dentro del corte pedido. |
| Breuillard, [A Height Gap Theorem…, 0804.1391](https://arxiv.org/abs/0804.1391), 2008; [Annals 2011](https://annals.math.princeton.edu/2011/174-2/p07) | Alturas adélicas de conjuntos de matrices y crecimiento de productos. Una «altura de compatibilidad» sin dato adicional puede ser una reformulación conocida. |
| Breuillard, [On the joint spectral radius, 2103.09089](https://arxiv.org/abs/2103.09089), 2021 | Control del crecimiento de productos; antecedente necesario para cualquier invariante asintótico de κ. |
| Philippe–Essick–Dullerud–Jungers, [Stability of discrete-time switching systems with constrained switching sequences, 1503.06984](https://arxiv.org/abs/1503.06984), 2015 | Productos restringidos por autómatas y multinormas. Añadir un grafo de composiciones tampoco prueba novedad por sí solo. |
| Lee–Voll, [Zeta functions of integral nilpotent quiver representations, 2006.12346](https://arxiv.org/abs/2006.12346), 2020 | Enumeración de subrepresentaciones integrales de quivers. La estructura integral del diagrama tiene antecedentes explícitos. |

La búsqueda verifica colisiones de alcance, no una clasificación exhaustiva de todos los teoremas de esas obras. No se ha establecido ausencia del insight exacto en toda la bibliografía ni en todo arXiv.

## 7. Unión con el frente de obstrucciones superiores

El frente de cup/Massey distingue existencia de una filtración racional de su realización con retículos graduados prescritos. Aquí distinguimos matrices racionales, existencia separada de retículos y coste de un retículo simultáneo. El principio común es **coherencia racional no implica presupuesto integral uniforme**. Son fenómenos diferentes: un ejemplo de álgebra diferencial no demuestra que una representación de Galois realizable tenga ese coste; un ejemplo de matrices tampoco lo demuestra para lifts theta.

La conexión a intentar demostrar, y no simplemente bautizar, es una desigualdad que traduzca exponentes de obstrucciones de extensión en una cota del perfil κ de un diagrama aritmético concreto. Si esa traducción produjera cotas uniformes nuevas, podría sustentar un programa sobre realización integral cuantitativa de correspondencias. Hoy es una pregunta con pruebas piloto y barreras precisas, no una nueva área ya establecida.
