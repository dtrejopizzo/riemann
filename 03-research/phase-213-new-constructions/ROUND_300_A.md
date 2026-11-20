# Inversión positiva por dilataciones para la discrepancia impar de la primera fila

Sea C=C₀ de 299 y sea A el mismo sumatorio restringido a enteros impares. Entonces A es una discrepancia explícita entre las clases 1 y 2 módulo 3: a cada entero impar libre de cubos con todos sus primos congruentes con 2 módulo 3 se le da peso positivo 4^ω(n), y se resta el peso de la segunda clase del de la primera. Se incluye el entero 1. En efecto, en cada primo el signo es (−1)^e.

Para todo x≥1 se tienen las identidades absolutamente convergentes

    A(x) = Σ_(j≥2) (j−1)2^(−j) C(2^j x),
    2A(x/2)−A(x) = Σ_(j≥1) 2^(−j) C(2^j x).

En particular, un techo C(v)≤K v^σ para v≥1 y 1/2<σ<1 implica simultáneamente A(x)≤K x^σ q²/(1−q)² y 2A(x/2)−A(x)≤K x^σ q/(1−q), con q=2^(σ−1). No se necesita una cota inferior para C. En sentido directo, la estimación buscada para C equivale exactamente a acotar superiormente la segunda diferencia A(x)−4A(x/2)+4A(x/4).

**Condición de borde que permite invertir.** Separar el factor local en 2 da C(x)=A(x)−4A(x/2)+4A(x/4). Es esencial que A(v)≪_R v/log^R(2v) para cada R fijo. Para verlo, repetir el producto de 294 en t=0 para la serie impar: en p=2 omitir el factor (1−2z)² desde el principio, con z=2^(−s). El factor corrector allí pasa a ser (1+z)²/(1−z)², cuya serie local converge absolutamente en Re s>0. En los demás primos vale la misma cancelación de primer grado que en 294. La hipérbola con dos factores μ y dos factores χ ordinarios da por ello el ahorro afirmado; el argumento también vale para C. En particular no se está dividiendo una estimación por un factor que se anula sobre Re s=1.

Poner a_j=2^(−j)A(2^j x) y d_j=2^(−j)C(2^j x). Entonces d_j=a_j−2a_(j−1)+a_(j−2). A x fijo, a_j y d_j son O_(x,R)((1+j)^(−R)) para j≥1. Sumar la segunda diferencia hacia el infinito una o dos veces da ambas fórmulas sin términos de borde. Los pesos positivos permiten trasladar un techo unilateral. En particular la discrepancia impar demasiado positiva a una escala, o una caída demasiado pronunciada de su valor normalizado entre dos escalas, obligaría a que C violara el techo en alguna dilatación.

**Alcance.** Eliminar 2 permite estudiar una discrepancia de pesos positivos en enteros impares. En el semiplano abierto 1/2<Re s<1 el multiplicador (1−2^(1−s))² nunca se anula: esta inversión conserva exactamente la obstrucción por multiplicidades de la primera fila identificada en 299. Las identidades transfieren un control unilateral y especifican dos posibles falsificadores; aún no demuestran ese control.
