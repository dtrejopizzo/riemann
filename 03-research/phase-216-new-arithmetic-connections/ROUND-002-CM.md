# ROUND 002 — Barrera de grado para observables CM y revisión de Zhao

28/11/2026. Resultado: un teorema elemental exacto de separación por grado, demostrado abajo. Es un candidato a lema útil para un trabajo; **su prioridad no está establecida y no se presenta como un teorema aritmético original de investigación**. Se revisó el texto completo HTML de Zhao v2 para identificar qué partes del programa ya cubre la literatura. No se auditaron todas sus referencias ni se certifica la prueba de ese artículo.

## 1. Resultado de la revisión de Zhao

En [Zhao, Towards the Colmez Conjecture, 2505.06541v2](https://arxiv.org/html/2505.06541v2), Def. 1.4 y Prop. 2.3–2.4 sitúan las alturas de tipos parciales en el formalismo de funciones CM y pares de inmersiones. Prop. 2.9 calcula correcciones de conductor mediante discriminantes. §3 distingue dos redes para componentes de diferenciales; Th. 4.1 compara sus alturas y períodos. Por tanto, proponer «períodos de tipos parciales con correcciones integrales» sin otra estructura no es nuevo. Su formalismo ya distingue más información que una sola altura global. No dedujimos del artículo un teorema de coste uniforme para nuestro tensor de cuatro factores.

[Zhao 2309.08886, Th. 7.3–7.5](https://arxiv.org/html/2309.08886) ya relaciona fibrados hermitianos y alturas sobre variedades de Shimura cuaterniónicas con correcciones discriminantes. Estos enunciados se revisaron, no sus pruebas completas. Por ello «control integral y arquimediano» también debe especificarse para una comparación nueva concreta, no ofrecerse como novedad genérica.

Este cotejo reduce el objetivo a algo preciso: distinguir la información **linealmente extraíble** del dato de pares de la información de una componente superior de Hodge. No autoriza a afirmar que todos los períodos CM olviden T4. Mantener todas las etiquetas y permitir operaciones no lineales puede recuperar información perdida por la agregación.

## 2. Un teorema exacto de separación por grado

Sea m≥5 y Ω={−1,1}^{Z/m}, con probabilidad uniforme. El punto s∈Ω determina un tipo CM en G=C2×Z/m mediante

\[
\Phi_s(a,i)=\frac{1+(-1)^a s_i}{2}.
\]

La convención de signos puede intercambiar a=0 y a=1 respecto de FRONT01; ninguna correlación cambia. Para un subconjunto R⊂Z/m de cardinal par r>0, definimos

\[
Q_R(s)=\frac1{2m}\sum_{a=0}^1\sum_{i\bmod m}\prod_{j\in R}\Phi_s(a,i+j).
\]

Sea P_{<r} el espacio de funciones en Ω representables por polinomios multilineales de grado menor que r, con norma L² uniforme. Sea a_R el número de traslaciones que preservan R.

**Teorema R2-CM.**

\[
\inf_{P\in P_{<r}}\|Q_R-P\|_2
 =2^{-r}\sqrt{\frac{a_R}{m}}.
\]

El minimizador es la suma de los términos de cardinal par estrictamente menor que r en la expansión

\[
Q_R(s)=\frac{2^{-r}}m\sum_i\sum_{J\subset R,\ |J|\ \mathrm{par}}
\prod_{j\in J}s_{i+j}.
\]

**Prueba.** Expandir cada factor (1+(−1)^a s_{i+j})/2 y sumar sobre a elimina los subconjuntos impares. Los productos χ_U(s)=∏_{u∈U}s_u, para U⊂Z/m, forman una base ortonormal: la media de χ_Uχ_V es cero si U≠V, porque alguna coordenada independiente aparece con exponente impar, y uno si U=V.

Todos los términos salvo J=R tienen grado menor que r. La componente de grado r es

\[
W_R(s)=\frac{2^{-r}}m\sum_i\chi_{i+R}(s).
\]

Hay m/a_R conjuntos distintos i+R y cada uno aparece a_R veces. Por ortogonalidad,

\[
\|W_R\|_2^2=\frac{m}{a_R}\left(\frac{2^{-r}a_R}{m}\right)^2
 =4^{-r}\frac{a_R}{m}.
\]

La descomposición ortogonal prueba simultáneamente el mínimo, su valor y la fórmula del minimizador. □

Para R={0,1,2,3} y m≥5, a_R=1. En efecto, una traslación que preserve el intervalo cíclico debe preservar su único punto de entrada desde el complemento. Así

\[
\inf_{\deg P\le3}\|Q_R-P\|_2=\frac1{16\sqrt m}.
\]

Como Q_R sólo tiene grados 0,2,4, la misma igualdad vale restringiendo a grado ≤2. No es una cota asintótica ni una observación experimental.

Para m=12, el tensor V de FRONT01 satisface h^{4,0}=24Q_R. Por tanto la distancia de su número de Hodge a todos los polinomios de grado ≤3 sobre los 4096 tipos CM de ese campo es exactamente √12/8. Esta norma mide variación sobre tipos CM, no distancia entre períodos ni tamaño de discriminantes.

## 3. Qué operaciones quedan excluidas

Una función de un par de signos s_i,s_j es un polinomio multilineal de grado ≤2. Por ello cualquier suma con coeficientes fijos de contribuciones dependientes de un solo par, incluso con coeficientes reales arbitrarios y dependientes del campo, pertenece a P≤2. El teorema excluye que una suma así coincida con Q_R en todos los tipos.

En particular, para el campo E fijo, cada función A_{Φ_s}(g) es cuadrática en s: es una suma de productos de dos indicadores afines. Aplicar un funcional lineal fijo a A_{Φ_s}, o combinar linealmente sus versiones obtenidas por permutaciones fijas de pares conjugados y cambios fijos de signos, sigue siendo cuadrático. Las alturas globales que se expresan mediante ese formalismo lineal tienen esta limitación. No estamos suponiendo fórmulas de valores L no demostradas para derivar la barrera: la afirmación algebraica es sobre **todo** funcional lineal fijo, cualquiera sea su origen.

El resultado no excluye productos de alturas, selección de índices dependiente del tipo, funciones no lineales de datos etiquetados, ni alturas de otros objetos que ya dependan de cuatro signos. Tampoco prueba que la información de cuarto orden tenga una aplicación analítica nueva.

En particular, «la altura global no determina el tensor» y «la teoría de períodos no determina el tensor» son afirmaciones distintas. Sólo se ha demostrado una barrera específica para grados bajos; el ejemplo homométrico de FRONT01 añade una barrera a cualquier función del dato agregado AΦ para ese par concreto.

## 4. Originalidad: lo que esta ronda descarta

La prueba usa únicamente expansión de Fourier–Walsh y proyección ortogonal; véase [O’Donnell, Analysis of Boolean Functions, capítulo 1](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf). Es el formalismo habitual de funciones booleanas y espacios de polinomios de grado bajo; la cercanía conceptual con Reed–Muller no convierte el resultado en una nueva teoría de códigos. La realización de Q_R como número de Hodge de un tensor CM tampoco es nueva maquinaria. Son aplicaciones explícitas de herramientas existentes.

Una contribución potencial tendría que añadir, por ejemplo, un resultado que relacione la componente W_R con un **defecto integral medible de una comparación geométrica concreta**, demostrando cota superior y ejemplo que la alcance, o que muestre un efecto sobre un observable aritmético que no se reduzca al formalismo lineal CM. Tal enunciado requiere fijar antes redes, comparaciones y normalizaciones; no lo hemos demostrado en esta ronda.

No hay base para titular estos resultados «teorema nuevo de períodos CM». Sí hay un criterio matemático para descartar propuestas débiles: si la supuesta nueva fórmula es una suma de contribuciones de pares con coeficientes fijos, no puede recuperar Q_R. La constante exacta cuantifica cuánto falla, en el modelo uniforme sobre tipos.

## 5. Verificación y cobertura

[experiments/cm_degree_barrier.py](experiments/cm_degree_barrier.py) comprueba exhaustivamente, con fracciones racionales, la identidad y el residuo para m=5,…,12. Esto complementa la demostración para todo m; no la sustituye. El registro de fuentes y consultas de esta ronda está en [bibliography/ROUND-002-CM-SOURCES.md](bibliography/ROUND-002-CM-SOURCES.md).

Esta ronda no produjo una certificación de prioridad ni un teorema original aritmético establecido. Produjo una obstrucción probada, una comparación más precisa con la literatura y un objetivo que evita renombrar resultados clásicos.
