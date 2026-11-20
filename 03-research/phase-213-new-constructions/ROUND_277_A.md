# Los dos signos de la banda se equilibran con un error relativo cuantificado

Para la combinación concreta de 275–276 sea A(x)=Σ_(Y<q≤U)Λ(q)|R(q)| y E(x) la misma suma con R(q). Incondicionalmente, con Ω(U)=(log U/log log U)^(1/3), existe c>0 tal que para todo x suficientemente grande

    |E(x)| ≪ exp(−c Ω(U)) A(x).

El resultado también vale al restringir ambas sumas a primos. En particular las masas positiva y negativa (tomadas ambas en magnitud) son cada una (1/2+o(1))A(x), aunque la masa absoluta supera el piso de 276. La cota se refiere a un error relativo.

**La integral firmada ya cumple el presupuesto.** Con I=∫S, el valor en s=1 de la transformada de T(y)−(I/y)1_(0,U)(y) es ∫S(t)log t dt+(γ_E−log U)I, por el término constante de ζ(s)∫S(t)t^(s−1)dt−I U^(s−1)/(s−1). Como en 276, la parte y<Y de la integral regularizada y todos los términos con I entre Y y U son O(N^(−2)), y por encima de U se integra el peso objetivo con resultado xh. Además, el ajuste de momentos de 273 da xh=Σ S(j)∫_(j−1)^j(1+log t)dt. Sustituir S(j) por S(t) cuesta O(log(2N) Var(S))=O(U log³(2N)): se aplica la variación en cada intervalo, y el soporte de S comienza en U/4. La integral incluye también la última celda de extremo ⌈2x⌉, con muestra cero si rebasa N. En consecuencia

    |∫_Y^U T(y)dy| ≪ U log³(2N).

**De la integral a la masa aritmética con error relativo.** Usar las celdas de 276, de longitud h entre U^(7/10) y 2U^(7/10). Sea ν la medida ΣΛ(q)δ_q o sólo su parte prima. En cada prefijo (a,a+v] de cada celda, la discrepancia |ν((a,a+v])−v| es O(h exp(−cΩ(U))) uniformemente. Para primos se aplica 238 por encima de a^(5/8), y por debajo sirve O((U^(5/8)+1)log U). Para las potencias propias, para cada exponente j≥2 dos j-ésimas potencias consecutivas en la banda están separadas por ≫√Y, por el teorema del valor medio. Hay O(log U) exponentes y los pesos son ≤log U, de modo que basta añadir O((1+h/√Y)log²U).

Tomar en cada celda el polinomio de Taylor P de T de orden dos en el extremo izquierdo. Para F=P y para F=|P|, por partes el error al pasar de dy a ν está acotado por la discrepancia de prefijos multiplicada por |F(a+h)|+Var(F). Esta última cantidad es ≪h^(−1)∫|P|: reescalar al intervalo unidad y usar equivalencia de normas en el espacio de polinomios de grado ≤2, y Var(|P|)≤Var(P). Resulta un coste O(exp(−cΩ(U))∫|P|) por celda. Reemplazar P por T, tanto en la integral como en la suma aritmética, cuesta en total O(U^(11/10)log¹¹(2N)), por la cota de la tercera derivada de 276 y ν(celda)≪h. También ||T|−|P||≤|T−P|.

Por 276, L₁=∫_Y^U |T| ≫ U^(3/2)/log(2N). El coste de Taylor y el tamaño de la integral firmada son O(exp(−cΩ(U)) L₁), disminuyendo c si hace falta. Así la masa aritmética absoluta es L₁(1+O(exp(−cΩ(U)))) y la firmada tiene módulo O(exp(−cΩ(U)) L₁). En la banda R(q)=T(q), lo que concluye la prueba.

**Escala que falta.** La equivalencia de 275 requiere E(x)≥−C_ε x^(1/2+ε) para cada ε>0. El ahorro relativo aquí probado es subpotencial, mientras A(x)≥c N^(3/4)/log(2N). Para obtener la conclusión a partir de una cota bilateral relativa haría falta al menos un ahorro de potencia en esa escala. Una cota unilateral absoluta aún puede aprovechar información adicional sobre cuál de las dos masas domina.
