# Cortar por la parte libre de cuadrados y una subsuma positiva después de emparejar

En 051 se estimaron filas completas cuando p|m. La restricción sf(km)≤S dependía de m y se dejó sin control firmado. Aquí se factoriza esa restricción para conservar el ahorro uniformemente en S. Se comprueba además qué ocurre al emparejar los índices pares e impares en el caso abierto p∤m.

**Corte uniforme.** En las filas repetidas de 051 con e≥2 poner k=p^e v, m=pw, W=y/(pk) y d=sf(p^(e+1)v). Basta considerar w libre de cuadrados y coprimo a p. Poner b=gcd(w,d). Entonces b|v pues es libre de cuadrados y p∤b. Escribir w=bz. Para cada b|d coprimo a p, los sumandos que le corresponden son exactamente los z libres de cuadrados con gcd(z,pd)=1. Se tiene

    sf(km)=d z/b,   μ(m)=−μ(b)μ(z).

Así sf(km)≤S sólo introduce el extremo superior z≤Sb/d en una suma con peso V(z/(W/b)).

Para justificar la uniformidad, sea D=pd. La suma de μ(n) para n≤u coprimos a D es Σ_h M(u/h), donde h≤u tiene todos sus primos en D. Esto sigue por convolución, comparando el factor en cada potencia prima. En h≤√u aplicar el PNT cuantitativo para M y en h>√u usar M(u/h)=O(u/h). La suma de h^(−1/2) sobre estos enteros es ∏_{q|D}(1−1/√q)^(−1). Este producto cuesta a lo sumo C^(1+ω(v))≤C v^C, porque sólo intervienen p y los primos de v. Como v≤C(log x)², el factor es polilogarítmico. El resto h>√u cuesta O(u^(3/4) v^C). En el soporte del peso se tiene u comparable a W/b, y W/b≫L^(1/2)/(log x)^C por 051. Por tanto la sumación parcial, también con extremo arbitrario, cuesta O_N((W/b)/(log x)^N) para cualquier N, eligiendo un exponente mayor en el PNT. El salto debido al extremo cuesta la misma cota. El número de b posibles es a lo sumo v. La suma en p,e,v de 051 absorbe todos estos factores y da O_A(L/(log x)^A) **uniformemente en S**. La misma estimación vale en cualquier intervalo de sf por diferencia.

En particular, para algún c>0 fijo, la suma original de 050 restringida a sf(km)≤c L/(log x)^4 es O(L) en valor absoluto **después de sumar con los signos originales**. Elegir c menor que la constante del límite inferior de 051 para las filas p∤m. Las filas repetidas de e=1 cuestan O(L) en módulos. Esto permite cortar el propio conjunto de productos, incluso si k admite varias etiquetas, por linealidad. En el extremo de 051 la suma de módulos puede ser mayor.

**Un emparejamiento que sigue necesitando compensación.** Separadamente, restringir la expansión de 051 a la fila de primo 3L<p<4L y agrupar por t=vm. El peso de fila combinado en v es log(p)(1−2·1_{2|v})U(pv); la compensación de 050 vive por debajo de 2L. Para t=q y t=2q, con q primo distinto de p y pq/y o 2pq/y en el soporte fijo de V, q es comparable a L. Los divisores v que contienen q quedan por encima del corte. Los v=1,2 dan U(p)=U(2p)=1 para x grande. La contribución conjunta es por tanto

    Σ_{3L<p<4L} log p Σ_{q primo, q≠p} [2 V(2q/X)−V(q/X)],    X=y/p.

Por PNT cuantitativo y sumación parcial con V fijo, Σ_q V(q/X)=X∫ V(t)/log(Xt) dt+O_N(X/log^N X). En la diferencia anterior la densidad continua es X V(t)[1/log(Xt/2)−1/log(Xt)]; al integrar vale X(log 2)∫V/(log X)²+O(X/(log X)³). Eliminar q=p cuesta O(L) en toda la suma por Chebyshev. Dado que Σ_{3L<p<4L}(log p)/p→log(4/3), la subsuma firmada es asintótica a

    y log(4/3) log(2) (∫V)/(log L)².

Es positiva y supera la tolerancia O(L). No es un contraejemplo global: demuestra que incluso el emparejamiento de estas dos familias exige compensación del resto de la suma. La identidad de divisores y las diferencias finitas tienen antecedentes en 042–043 y en la fase 188; la evaluación aquí concierne al peso y al corte de 049–051. El signo del complemento total sigue abierto.
