# Residuos de soporte primo prescrito y un criterio cruzado sin diagonal

En 350 se puede exigir que todo entero no emparejado tenga una de las dos formas qp, 2qp, con p primo grande. Aquí q se fija de antemano y puede ser 1 o cualquier primo impar ≤(log X)^B para un B fijo. Para q=1 el signo restante es negativo en los primos y positivo en sus dobles; para q primo impar se invierten ambos signos. No se cambia ningún coeficiente de μ: sólo se elige qué enteros borrar del conjunto emparejado.

**Reservas.** Para cada forma y en cada cuarto exterior de una celda de longitud J=⌊X^(2/3)⌋, el número de candidatos es ≫ J/(q log X). En efecto, para p se cuenta un intervalo de longitud comparable a J/q con extremo comparable a X/q. Esa longitud supera (X/q)^(3/5) para X grande, uniformemente para los q indicados. El teorema de primos que ya se usa en 348 da la cota inferior; p supera a todos los primos q admisibles. [Guth y Maynard, teorema sobre intervalos cortos](https://arxiv.org/html/2405.20552v1)

Hacer ambas correcciones de 350 utilizando exclusivamente esos candidatos. Eliminar el desequilibrio de cantidad usa O_A(J/(log X)^A) del signo sobrante. Luego el desequilibrio de posición cuesta O_A(J²/(log X)^A), pues cada muestra retirada mueve el momento en ≤J. Cada pareja correctora de los cuartos opuestos compensa al menos J/2−O(1) y mantiene la cantidad equilibrada. Usar A>B+3 para verificar que no se agota ninguna reserva, incluso tras el primer borrado. Detenerse con primer momento en módulo ≤J. La prueba de Taylor de 350 da entonces, para el pulso residual R_q,

    |S_h(x)−R_q(x)| ≪_η 1+J²/H =: O_η(E),

uniformemente en q y x. Las decisiones pueden fijarse escogiendo en cada paso los menores índices admisibles. La selección se hace separadamente para cada q: se obtienen representaciones alternativas del mismo observable.

**Disjunción y prueba cruzada.** Para q≠r las muestras no emparejadas en las dos representaciones son disjuntas. Su único factor primo grande p determina por división el cofactor, que pertenece a {q,2q} o a {r,2r}; esos conjuntos son disjuntos. En particular podemos elegir q=1 y r=3 sin dependencia de X. Sean L=∫_[X,2X] S_h² dx/x y C=∫_[X,2X] R_1 R_3 dx/x. Entonces

    |C−L| ≪ E√L + E².

Se obtiene expandiendo R_i=S_h+(R_i−S_h) y usando Cauchy–Schwarz en una medida de masa log 2. Como E=o(√H), el techo unilateral C≪_(δ,ε) H X^ε implica L≪_(δ,ε) H X^ε por la desigualdad cuadrática, y L bajo el mismo techo implica la cota para C. Para cada δ=1/j, j≥16, el criterio de 337 equivale así a estimar **un producto cruzado sin términos con el mismo entero**, con soportes en primos y sus dobles por un lado, triples y séxtuplos de primos por otro.

**Qué se ha localizado y qué falta.** La ausencia de diagonal es exacta. Las subcolecciones de primos seleccionadas dependen de los desequilibrios de μ en la celda. Un teorema que cuente todos los primos del intervalo proporciona las reservas y no estima automáticamente la correlación de estas subcolecciones. El techo de raíz y el signo global siguen abiertos.
