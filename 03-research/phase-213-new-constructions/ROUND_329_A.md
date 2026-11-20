# Ahorro de toda potencia en la energía central de Möbius

Con la notación de 325–328, para cada a fijo en (0,log 4] y b real fijo, tomar h=exp(−am)m^b. Entonces, para **cada A>0 fijo**,

    E_m[h] = Δ_m + O_(a,b,A,η)( h binom(2m,m) m^(−A) ).

En particular E_m[4^(−m)m^b]∼Δ_m para todo b fijo, y para todo 0<a<log 4 el cociente E_m(a)/P_m(a) es O_(a,A,η)(m^(−A)) a cualquier orden fijo. La restricción b<1/50 de 328 provenía de la estimación usada, no del peso del problema.

**Qué estimación externa entra.** En la introducción de *Higher uniformity of arithmetic functions in short intervals II*, Matomäki, Radziwiłł, Shao, Tao y Teräväinen enuncian la cota maximal en casi todos los intervalos de longitud H≥Y^(1/6+ε) y especifican expresamente su versión para μ. Para cada A, la suma de μ sobre cualquier subintervalo de (y,y+H] cuesta O(H log^(−A)Y) salvo en un conjunto de y de medida O_(ε,A)(Y log^(−A)Y) en el bloque diádico. Sólo usamos subintervalos contiguos, contenidos en el máximo sobre progresiones. Se trata de la estimación escalar de la introducción, no del umbral 1/3 para nilsecuencias generales. [Enunciado (1.5) y párrafo sobre Möbius en la versión arXiv](https://arxiv.org/html/2411.05770v1) · [Versión publicada, fórmula (1.6)](https://doi.org/10.1007/s00222-026-01408-6)

**La longitud real excede el umbral.** Tomar como zona central 1.8m≤log x≤2.2m. En un bloque diádico [Y,2Y] que la intersecta poner H=ceil(4hY), constante en el bloque. Uniformemente allí,

    (log H)/(log Y) ≥ 1−(log 4)/1.8−o(1) > 0.22.

Por tanto cabe, por ejemplo, el margen 1/6+1/30. También H/Y→0 y, para cada a fijo positivo, H≤Y^(1−ε') para algún ε'>0. Ajustar ε al menor de los márgenes si es preciso. Toda muestra no nula del suavizado en 327 está en (x−H,x]. Al aplicar el teorema con y=x−H se cubre el rango desplazado con un número acotado de bloques diádicos. La excepcionalidad sigue midiéndose respecto de x porque el corrimiento H es constante.

En el soporte, el peso η(log(x/n)/h) l_m(n)/l_m(x) tiene variación total O_η(1): la variación de η es fija por monotonía del cambio de variable y la derivada logarítmica de l_m respecto a log n es m/log n−3/2, acotada. Por sumación parcial la cota maximal del insumo pasa al peso. Al normalizar por hx, la suma local ponderada cuesta O_A(m^(−A)) fuera del conjunto excepcional, y O(1) en todo el bloque. Por tanto su media cuadrática cuesta O_A(m^(−A)), incluidos los puntos excepcionales. Las constantes son uniformes en los bloques centrales para m grande.

**Integración y límites.** Repetir la integral de Gram de 327 con el peso h x l_m(x)² dx; su variación en razón dentro de cada bloque central está acotada. La contribución central es O_A(h binom(2m,m)m^(−A)). La diagonal contenida en esa zona es exponencialmente pequeña respecto de 1/√m, pues se concentra en log n cercano a m. Fuera de la zona central la masa absoluta de los pares distintos cuesta O(h binom(2m,m) exp(−c m)), por la cola gamma del peso de vecinos de 328. Esto también cubre los dos bordes ensanchados en h. Puesto que h binom(2m,m) es al menos una potencia fija de m por debajo de 1/√m en todo el rango enunciado, se absorbe la diagonal central en el error. Se obtiene la fórmula. Para a<log 4 la diagonal es además exponencialmente menor que P_m(a), y 327 da el cociente anunciado.

No hay control de las constantes cuando A crece con m. En particular, estas estimaciones no dan una reducción fija de la tasa exponencial en a=1/j. Esa reducción es la que exige el criterio global; sigue abierta.
