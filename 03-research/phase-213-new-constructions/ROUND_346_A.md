# Compensación entre bandas en dos familias de productos impares

Mantener la banda, los centros y 0<δ<1/4 de 345, antes del recorte. Entre los aportes en módulo de la banda en productos impares, la fracción que corresponde a productos con algún divisor cuadrado primo tiende, uniformemente en el centro, a

    1 − ∏_{p>2} (1−1/(p+1)²) > 0.

Las demás filas cancelan **exactamente** el coeficiente entero de la banda en cada uno de esos productos. Además, sobre productos impares libres de cuadrados, otras filas cancelan multiplicidades sobrantes de masa total ≫hX. Son dos compensaciones disjuntas de orden hX; ambas son internas al mismo producto n una vez reunidas las bandas.

**Identidad.** En el observable completo C_h, un n impar sólo proviene del pulso S_h(x), por lo que su coeficiente es μ(n). Según 345, la banda aporta λ(n)a_Y(n). Si n no es libre de cuadrados, el complemento tiene coeficiente −λ(n)a_Y(n). Si n es libre de cuadrados y a_Y(n)≥1, tiene coeficiente −λ(n)(a_Y(n)−1). Estas identidades sobre el complemento preceden al recorte por Poisson; ese recorte sólo se controla en valor firmado.

**Fracción en la primera familia.** La masa cuenta pares d,m impares libres de cuadrados con peso W_x(dm); su producto es libre de cuadrados exactamente cuando (d,m)=1. Fijado d, por 341 y sumación parcial la suma sobre m impares libres de cuadrados coprimos a d vale

    c₂ ∏_{p|d} p/(p+1) · (hx/d) ∫η(v)e^(−hv)dv + O(τ(2d)√Y)

para d impar libre de cuadrados, donde c₂ es la densidad de impares libres de cuadrados. Sin restricción de coprimalidad se omite el producto. Los errores totales son O(Y^(3/2+o(1)))=o(hX). El cociente de los términos principales es la media del producto sobre d impares libres de cuadrados en [0.6Y,0.7Y], con peso 1/d. En esta población, para cada conjunto finito de primos impares los sucesos p|d tienen densidades conjuntas independientes de parámetros 1/(p+1), por el teorema chino del resto y la criba de cuadrados. El peso 1/d preserva las densidades por sumación parcial. Sustituir el producto por el truncado en p≤P cuesta en la media O(Σ_{p>P}p^(−2)): por 1−∏(1−u_p)≤Σu_p y el conteo de múltiplos de p hasta Y. Así el cociente para productos libres de cuadrados tiende al producto anunciado y el complemento da la fracción del enunciado.

**Productos libres de cuadrados con dos representaciones.** Tomar d=17v en [0.605Y,0.615Y] y m=19w. Exigir que v,w sean impares libres de cuadrados, coprimos entre sí y con 17·19. Entonces n=17·19·v·w es libre de cuadrados y también admite el divisor 19v en la banda porque 19d/17∈[0.6Y,0.7Y]. Estos dos divisores son distintos. Hay ≫hX de tales pares contando el peso: se aplica el cálculo anterior a v y w con el argumento del pulso 323vw y excluyendo además los dos primos fijos. Las longitudes de las variables cambian por constantes, el producto de densidades sigue siendo positivo y el error vuelve a ser O(Y^(3/2+o(1))). Por cada n con a=a_Y(n)≥2 la multiplicidad sobrante a−1 es al menos a/2, suficiente incluso cuando hay más de dos divisores en la banda.

**Alcance.** 345 mostraba que agrupar sólo las filas seleccionadas por producto no reducía la masa impar. Aquí se mide una parte que sí desaparece al combinarlas con las demás filas. El coeficiente superviviente para cada producto impar libre de cuadrados sigue siendo μ(n); las identidades no dan una estimación de su suma local. La ventana de positividad no cambia.
