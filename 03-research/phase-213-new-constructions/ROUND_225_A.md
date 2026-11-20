# Un modelo sobre celdas logarítmicas con datos enteros y error subexponencial

En 224 la representación por conteos entre cuadrados todavía necesita exponencialmente muchas celdas respecto de k para un orden lineal N=jk. Aquí se obtiene la misma tasa mediante O_j(k) celdas y O_j(k²/log k) enteros. Cada entero se redondea con error absoluto de hasta 1/2. Esto es una reducción del volumen de datos que requiere evaluar la muestra una vez precalculados; no es un algoritmo de tiempo polinómico para obtenerlos desde los primos.

Fijar b>1/2, n entero no negativo y m_n=ceil(b n/log(n+2)). Guardar, para 0≤r≤m_n,

    T_(n,r) = entero más cercano a Σ_(n≤log p<n+1) (log p)/√p · (log p−n)^r.

En particular las celdas y los datos son independientes del orden, de j y de la tasa. Tomar N=jk, U_k=max(4,log log(k+20)), L_N(u)=2N log M₁(u). Para k suficientemente grande, formar

    Y_(k,j) = ∫₃^U_k u^(s_k−1) Σ_(0≤n<floor L_N(u)) Σ_(r=0)^m_n
                 T_(n,r) c_N^(r)(n;u)/r! du.

Entonces limsup log(1+|Y_(k,j)−C_(k,j)|)/k=0 para cada j fijo. En particular el límite ordinario de log(1+|Y|)/k es max(0,Θ−d_j) de 224. Bastaría acotar estas combinaciones de los datos enteros en una subsucesión para cada j en un conjunto no acotado.

**Dos extremos del corte.** En u≥U_k la cota absoluta de 216 con contorno de altura 1/2 da C poly(N) exp(N log M_(1/2)(U_k)); la prueba funciona con el peso de 217 ya que |u^(s_k−1)|≤1. Para j fijo su logaritmo positivo es o(k). En u≤U_k descartar la celda final incompleta cuesta O(u) antes del integral: por el contorno de altura uno, |c_N(log p;u)|≤Cu M₁(u)^N/p y por Chebyshev Σ_(p≥exp(floor L)) (log p)p^(−3/2)≤C exp(−L/2). Esto incluye cualquier átomo en un extremo de corte. El producto M₁(u)^N exp(−L/2) es uno.

**Aproximación en celdas completas.** Para r≤N−1, en la recta real se tiene

    sup_t |c_N^(r)(t;u)| ≤ C u (4u)^r.

En efecto |τ|H_u(τ)≤4u y ∫H_u^(N−r)≤∫H_u=O(u). Todo n usado es O(N), por lo que m_n+1≤N−1 para k grande. El error de redondeo por celda cuesta O(u exp(4u)) por el desarrollo exponencial. La masa real antes de Taylor es O(exp(n/2)) por Chebyshev. El error por Taylor en la celda es así

    O(exp(n/2) u (4u)^(m_n+1)/(m_n+1)!).

Para n≤√k sumar con el techo O(exp(√k/2)U_k exp(4U_k)), por celda, todavía subexponencial. Para √k<n≤O_j(k), la cota factorial m!≥(m/e)^m da logaritmo ≤(1/2−b+o(1))n uniformemente: log(m_n+1)=log n−log log n+O_b(1), mientras log(4U_k)=o(log k). Así los errores en las celdas restantes son sumables y el error total tras el integral es exp(o(k)). El número de momentos es O_j(k²/log k), cada dato requiere O_j(k) bits por el mismo techo de masa, y basta O_j(k³/log k) bits en total. No se requiere almacenar posiciones individuales de los primos en la evaluación.

**Qué se ganó frente a la comparación por conteo.** Las posiciones pueden variar mucho dentro de celdas de ancho uno en logaritmos, pero igualar los momentos anteriores salvo errores acotados basta para transferir el criterio. No se pide que los dos conteos difieran en O_ε(x^(1/2+ε)) en los cortes interiores como en la condición suficiente de 224. El coste se controla por suavidad de los núcleos en órdenes de derivación que crecen. El problema aritmético es la cancelación entre los momentos auténticos. Sus redondeos y el número de bits no establecen esa cancelación.
