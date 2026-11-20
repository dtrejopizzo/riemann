# Cuánta inclusión-exclusión exige el valor de la criba original

Mantener Y, N∼λx^(3/2) y el peso f de la sección de traslaciones de 042. En esta ronda h=0 en todos los módulos. Para n con Y<n≤N escribir r(n)=#{p≤Y:p divide n}. Sea V el valor exacto, es decir, x^(−1/2)Σf(n)1_{r(n)=0}. En V_k sustituir el indicador por Σ_{j=0}^k(−1)^j binom(r(n),j). Para cada constante 0<α<1 y cualquier k entero con k∼α log x/log log x, se cumple

    |V_k−V| = x^(1/2−α+o(1)).

Para k impar, V_k es una cota inferior. Se puede elegir k impar con cualquier α>1/2 menor que uno y obtener un minorante a distancia o(1) del valor original. Para α<1/2 la pérdida diverge en módulo. Estas afirmaciones no fijan el comportamiento de una sucesión particular en el umbral α=1/2.

**Cota superior uniforme.** Para r>0, la suma truncada es (−1)^k binom(r−1,k), con valor cero cuando k≥r. Para r=0 no hay error. En todo el soporte f(n)≥0 para x grande, pues la prueba de positividad de 042 sólo usa n>Y, y f(n)≤log(N)w(n/x). El error tiene por ello un solo signo y su módulo se mayora reemplazando binom(r−1,k) por binom(r,k+1). Este último cuenta los divisores cuadrados-libres de n con k+1 primos distintos ≤Y. Para cualquier d≥1,

    Σ_{m≥1} w(dm/x) ≤ C x/d.

Si d≤x separar en m=x/d y sumar m o m^(−2) en su rama correspondiente. Si d>x la suma es ζ(2)(x/d)². Sumando primero por divisores se deduce

    |V_k−V| ≤ C √x log(N) (Σ_{p≤Y}1/p)^(k+1)/(k+1)!.

La suma de recíprocos es O(log log x); el logaritmo de su potencia es o(log x) para este k. Por Stirling, log((k+1)!)=(α+o(1))log x. Así se obtiene el exponente de la cota superior.

**Cota inferior en la fase cero.** Tomar D el producto de los primeros k+1 primos. Por el teorema de los números primos log D∼k log k y el mayor de sus primos es O(log x), menor que Y. Así D=x^(α+o(1)) y hay (1+o(1))x/D múltiplos suyos en [x,2x]. Todos pertenecen al soporte del peso f para x grande. Allí f(n)=(1−c)(x/n)²log n≳log x y binom(r(n)−1,k)≥1. Sin cancelaciones, estos enteros aportan al error absoluto al menos una constante por √x log x/D. Esto completa la igualdad de exponentes.

**Qué estima el resultado.** V_k se expresa por sumas ordinarias de f sobre múltiplos de productos de a lo sumo k primos de la criba; no interviene un promedio de fases. El coste calculado es el error de truncar esa fórmula concreta, no el error de V respecto de (3/2)√x. Sigue faltando demostrar V_k≥(3/2)√x−O(1) para alguna elección impar de profundidad suficiente. No hay aquí una barrera para otros pesos de criba. R166_601 ya usa inclusión-exclusión de Legendre, y el índice registra la identidad de Selberg como vía ya recorrida; no se ha reabierto esa identidad. Lo específico de este cotejo es el umbral de profundidad a precisión aditiva O(1) para 042.

## ¿Ayuda optimizar los coeficientes del polinomio de conteo?

Con la notación anterior sea L_x(P)=x^(−1/2)Σ_{Y<n≤N} f(n)|1_{r(n)=0}−P(r(n))|. Para cualquier k∼α log x/log log x con 0<α<1,

    inf_{deg P≤k} L_x(P) = x^(1/2−α+o(1)).

El mismo exponente vale restringiendo el ínfimo a minorantes punto a punto. Se permiten coeficientes reales que dependan libremente de x. La aproximación en error absoluto es importante: para polinomios sin restricción de signo no se afirma un límite inferior al error después de cancelar desviaciones positivas y negativas.

**Cada nivel de conteo necesario tiene masa.** Para cada j=0,...,k+1 escribir D_j=∏_{i≤j}p_i, D₀=1. Uniformemente en j, D_j≤x^(α+o(1)) y p_j=O(log x) para j≥1. Se pueden encontrar al menos x^(1−α−o(1)) enteros del soporte con r(n)=j y con f(n)≥x^(−o(1)):

* Si D_j≤x/(2Y), usar n=D_j q para primos x/D_j<q≤2x/D_j. Entonces q>Y y r(n)=j. El número de elecciones es ≫x/(D_j log x).
* En la otra rama j≥1. Poner T=min(Y,x/D_{j−1}) y usar n=D_{j−1}q con q primo en (T/2,T]. Ahora D_{j−1}T=min(D_{j−1}Y,x)>x/(2p_j) o vale x. Por ello T≥x^(1−α−o(1)), q>p_j para x grande y q≤Y. Se obtiene r(n)=j con ≫T/log x elecciones.

Las estimaciones de primos en intervalos de razón dos son uniformes porque el menor extremo usado tiende a infinito. En ambas ramas n está entre x/(C log x) y 2x, por lo que pertenece a (Y,N]. Si n≤x el cociente del corrector c(x/n)² respecto a w(n/x) es c(x/n)³=o(1) uniformemente, usando 042. Si n≥x ese cociente es c=o(1). En todo el intervalo f(n)≫1 para x grande. En consecuencia la masa normalizada de cada nivel j del listado es al menos x^(1/2−α−o(1)).

**Obstrucción algebraica.** La diferencia de orden k+1 de P en los enteros 0,...,k+1 vale cero; para el indicador del nivel cero su módulo vale uno. La suma de los módulos de los coeficientes de esa diferencia vale 2^(k+1). Por tanto en algún nivel j la desviación tiene módulo al menos 2^(−k−1)=x^(−o(1)). Multiplicar por la masa de ese nivel prueba la cota inferior, uniforme en los coeficientes. Para la cota superior se puede elegir el mayor orden impar ≤k en el minorante de Bonferroni de la sección anterior. Su error no cambia de signo y alcanza el exponente indicado.

Así, dentro de la clase que sólo usa el número de factores distintos de la criba, modificar los coeficientes no rebaja el umbral de profundidad de primer orden. La demostración no se aplica a pesos que distingan cuáles primos dividen n, ni controla el valor firmado del minorante de profundidad suficiente.

**Pesos que sí distinguen los primos: una barrera parcial.** Hay además una cota inferior distinta para polinomios de grado ≤k en *todos* los indicadores 1_{p|n}, p≤Y, sin simetría en sus coeficientes. Se pueden tomar multiafines por ser variables booleanas. Para 0<α<3/4 el error ponderado L¹ de cualquiera de estos polinomios es al menos

    x^( min(1/2−α, 3/4−2α) − o(1) ).

En efecto restringir al cubo de los primeros k+1 primos dejando a cero las otras variables. En sus vértices el indicador objetivo es uno sólo en el vértice vacío. La diferencia mixta en las k+1 variables anula cualquier monomio de grado a lo sumo k, y vale ±1 en el objetivo. Algún vértice tiene por tanto error ≥2^(−k−1).

Para *cada* vértice S, sea d el producto de sus primos y T=max(Y,x/d). Tomar n=dq con q primo en (T,2T]. Así el conjunto exacto de pequeños divisores primos es S, incluso en las variables fuera del cubo. Se tiene x≤n≤2 max(x,Yd)≤N para x grande pues d≤x^(α+o(1)) y α<3/4. Hay ≫T/log T elecciones y cada una aporta x^(−1/2)(1−c)(x/n)² log n a la masa del vértice. Como log n≥log T, la masa es ≫x^(3/2)/(d² T). En las dos ramas esto es respectivamente x^(3/2)/(d²Y) o √x/d. El peor de estos órdenes da la cota anunciada. Multiplicar por el error puntual del vértice localizado completa la prueba.

Por tanto incluso ponderar cada intersección según los primos que la integran no permite pérdida acotada cuando α<3/8. Para α≤1/4 el exponente inferior de esta clase coincide con el superior de Bonferroni. Para 3/8≤α<1/2 esta prueba no decide si tales pesos pueden alcanzar pérdida O(1). Estas conclusiones requieren error absoluto o minoración puntual.

## Un minorante más corto que usa la parte del logaritmo sin cribar

Para n en el soporte, calcular

    A(n)=1−[Σ_{p≤Y} ν_p(n) log p]/log n,

donde ν_p cuenta la multiplicidad. Sólo requiere divisiones por los primos de la criba. Es la fracción del logaritmo de n que queda después de retirar esos factores. Satisface 0≤A≤1, vale uno en los enteros libres y cero si todos los primos de n son ≤Y. Multiplicar por A(n) el polinomio truncado de Bonferroni B_k(r)=Σ_{j≤k}(−1)^j binom(r,j), con índice inicial j=0. Para k impar se obtiene un minorante puntual del indicador de coprimalidad. Denotar por W_k el valor al sumarlo con el mismo peso normalizado de 042.

Para 0<α<3/4 y k∼α log x/log log x se cumple exactamente a escala de exponentes

    |W_k−V|=x^(min(1/2−α,3/4−2α)+o(1)).

En particular cualquier α fijo en (3/8,1/2) ya da error o(1), tomando k impar. La modificación usa tanto las valoraciones como el valor de n, por lo que no es un polinomio únicamente en el conteo ni únicamente en los indicadores de pequeños divisores primos.

**Cota superior.** Se conserva la primera cota de 043 porque A≤1 y el indicador se reproduce exactamente cuando r=0. Para la segunda, sólo puede haber error si n es múltiplo de un divisor d cuadrado-libre con k+1 primos ≤Y. Además, A(n)log n=Σ_{q>Y, e≥1, q^e|n} log q. Mayorar el módulo del resto de Bonferroni por binom(r,k+1), expandir ambas sumas y usar f(n)/log n≤(x/n)². Por coprimalidad de d y q, la suma de n⁻² sobre sus múltiplos comunes es ζ(2)/(dq^e)² si se extiende a todos los múltiplos. De ello resulta

    |W_k−V| ≤ ζ(2) x^(3/2) [Σ_{q>Y primo} log(q)/(q²−1)]
                             [Σ_{d|P, ω(d)=k+1} d^(−2)].

El primer corchete es O(1/Y) por Chebyshev y sumación parcial. Cada d del segundo es al menos el producto D de los primeros k+1 primos, que es x^(α+o(1)). Además, la suma de los inversos de esos d es a lo sumo (Σ_{p≤Y}1/p)^(k+1)/(k+1)!=x^(−α+o(1)) como cota superior. El resultado es ≤x^(3/4−2α+o(1)).

**Cota inferior.** Con T=max(Y,x/D) tomar n=Dq para primos T<q≤2T. Entonces r(n)=k+1, el error de B_k tiene módulo uno y A(n)log n=log q. Todos estos enteros pertenecen a [x,N] para x grande por α<3/4. Como los errores tienen un solo signo, su contribución normalizada es ≫x^(3/2)/(D²T), usando que hay ≫T/log T primos en ese intervalo. Esto da el exponente anunciado en ambas ramas de T. El caso crítico α=3/8 no queda decidido para secuencias k dadas sólo a primer orden.

**Qué queda por demostrar.** La modificación evita pérdidas grandes en los enteros compuestos exclusivamente de primos pequeños. Esta ganancia se certifica antes de estimar el valor firmado de W_k. Para concluir el signo sigue haciendo falta W_k≥(3/2)√x−O(1). No se ha probado la optimalidad frente a todos los minorantes que usan valoraciones. Cotejo: la descomposición logarítmica es clásica y se usó en 041; R166_601 trata el cribado por factores pequeños. Lo adicional es el error de su combinación con el truncamiento de 043. Construcción y ambos exponentes auditados independientemente.
