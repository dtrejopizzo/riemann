# Dónde se compensa el término positivo de 052 en las filas 3L<p<4L

Fijar el peso de orden dos y K de 049–052. En las filas marcadas por un primo 3L<p<4L, escribir t=vm, X=y/p, J=K/p comparable a (log L)². Con ε(v)=(−1)^(v+1), el peso es log p·ε(v)U(pv)μ(m)V(t/X). La compensación en primos de 050 no interviene. En las fórmulas se excluye p|m a coste O(L) por 051.

Sea H la suma en estas filas sobre los t con un primo q>√t, y F la suma sobre su complemento. Entonces, con C=log(4/3) log(2) ∫V>0,

    H = C y/(log L)² + O(y/(log L)³),
    F = −C y/(log L)² + O(y/(log L)³).

Más aún, H+F=O_N(y/(log L)^N) para cada N fijo. Esta última cota sigue siendo mayor que la precisión exigida O(L) a gran escala.

**Cálculo de H.** Existe una única escritura t=dq con q primo y q>d. En el soporte q≫√L, de modo que un v múltiplo de q no puede satisfacer U(pv)≠0. Así v|d y μ(t/v)=−μ(d/v). Si q=p, entonces d=O(1) en el soporte y el coste total de esa exclusión es O(L). Tampoco p puede dividir d pues d≪√L. Reemplazar por uno el corte en el coeficiente −Σ_{v|d}ε(v)U(pv)μ(d/v) da exactamente −1_{d=1}+2·1_{d=2}, por inversión de divisores. Ese valor ya fue evaluado en 052. Falta controlar uniformemente el coste del reemplazo para todos los d, que ahora pueden crecer como √L.

Sea d=hv. Por PNT cuantitativo y sumación parcial, la suma en q>hv de V(qhv/X) puede sustituirse por su integral con densidad 1/log q. Su error es O_N(X/[hv(log L)^N]), pues en el soporte efectivo q es comparable a X/(hv) y q≫√L. El extremo móvil q>hv se admite en la sumación parcial. Sólo interviene hv≪√L; por las dos sumas armónicas se pierden a lo sumo dos potencias de log L. En la integral poner s=qhv/X. La condición q>hv da v<B=√(Xs)/h. Para s en el soporte fijo de V la corrección, con su signo global omitido al acotarla, tiene la forma

    X ∫ V(s) Σ_h μ(h)/h Σ_{v<B} ε(v) f(v) ds,
    f(v)=[U(pv)−1]/[v log(Xs/(hv))].

La suma interior es cero para B≤J. Para B>J se tiene log(Xs/(hv))≫log L, y f se anula hasta J. En [J,B], |f(B)|≪1/(B log L), |f'(v)|≪1/(v² log L), |f''(v)|≪1/(v³ log L); las derivadas del corte sólo intervienen en v comparable a J. La suma alternada está acotada por C(1/B+1/J²)/log L. Para verlo, desplazar dos veces en un entero la suma con signos alternados: cuatro veces la suma es la suma alternada de segundas diferencias más términos de borde. Las segundas diferencias cuestan a lo sumo una constante por ∫|f''| y los bordes finales O(1/(B log L)); los iniciales se anulan al extender f por cero. El mismo argumento vale para B no entero.

Al sumar 1/h para h≤√(Xs)/J, el término 1/B cuesta O(1/J) y el término 1/J² cuesta O(log L/J²). Por tanto el error por p es O(X/(log L)³). Sumando log p en 3L<p<4L se obtiene O(y/(log L)³). El término principal y su constante son los de 052, usando también PNT cuantitativo para la suma exterior.

**Cálculo del complemento.** En toda la fila sumar primero en m. Para cada v≤eJ, la escala de m es X/v≫L/(log L)². El PNT cuantitativo para μ, con el peso suave fijo V, da O_N(X/[v(log L)^N]) uniformemente. Sumar v y p cuesta una suma armónica en v y Σ(log p)/p=O(1); aumentar N absorbe esa pérdida. La eventual exclusión p|m cuesta O(L). Así se obtiene la estimación de H+F y, restando H, la de F.

**Alcance.** El término positivo de 052 se compensa, al orden principal, dentro del propio intervalo de primos marcados, por cofactores que tienen todos sus primos ≤√t. La descomposición por el mayor primo es clásica. La estimación nueva respecto de 052 es que admitir todos los d<q altera el cálculo sólo en O(y/log³L), y esto identifica la clase que suministra el término negativo. Queda abierta la precisión de raíz de la suma total.

**Precisión de raíz en este bloque.** Para un primo marcado 3L<p<4L, la suma sin U es Σ_v ε(v)g(pv/y)=V(p/y)−2V(2p/y)=0. La parte alta tiene integral cero al combinar las progresiones de paso uno y dos. Por 047 su módulo es ≤C(y/p)exp(−c√(K/(2p))). Sumando log p y fijando suficientemente grande la constante de K, el bloque completo, antes de excluir p|m, es o(L). Si m=pw, el soporte obliga a vw=O(1), de modo que U(pv)=1 y p∤w para x grande. En cada producto vw la convolución ε*μ es δ₁−2δ₂. Así la contribución con p|m es exactamente Σ_p log p [−V(p²/y)+2V(2p²/y)] en este bloque. En la notación anterior,

    H+F = C₁ L+o(L),    C₁=∫₃⁴[V(u²/2)−2V(u²)]du > 0.

La equivalencia asintótica sigue de PNT y sumación parcial. Para el signo, en e≤t≤16 el sombrero promediado de 047 vale c[64P(3/2)t⁻²−P(−3/2)t/64], con c=64/4097 y P(z)=∫exp(zv)dν(v). Es la rama superior de 044 a lo largo de todo el promedio. Se obtiene C₁=c[(74/81)P(3/2)+(37/128)P(−3/2)]. Esta estimación usa el mecanismo de cuadratura de 049 en la paridad de las filas, en lugar de estimar primero la suma en m.
