# Separación del coste de los huecos y una identidad con pesos sólo en primos

Usar I=(X,Y], Y=X exp h, L=Y−X y la normalización X⁻² de 231. Se obtienen un techo incondicional para la parte cúbica de los huecos y una segunda evaluación local, en la que cada primo se compara con su posición predicha por el rango acumulado. Esta última evaluación da el mismo criterio de subsucesión sin calcular un ajuste por mínimos cuadrados.

**Huecos.** Partir el intervalo en los tramos sin primos, incluidos los fragmentos de los bordes. Sea l su longitud, z su punto medio medido desde X y S la masa prima local acumulada en su interior. Sea D_mid el mínimo en A,C de X⁻²Σ l(S−A−Cz)². Por 231 la función objetivo exacta agrega C²Σ l³/(12X²). El teorema de Peck y Maynard da Σ_(p_n≤eX)(p_(n+1)−p_n)²≪_ε X^(5/4+ε). Los fragmentos están contenidos en los huecos de esa suma (el hueco que contiene ambos extremos se cuenta una vez). Por tanto Σ l³≤(Σ l²)^(3/2)≪_ε X^(15/8+ε). La identidad de varianza de los puntos medios es Σ l(z−L/2)²=(L³−Σ l³)/12≥L³/24 para X grande, pues L=X^(1−o(1)). En la recta de regresión de puntos medios la pendiente es covarianza dividida por varianza. Su numerador en sumas sin normalizar cuesta O(M L²), M=Σ_(X<p≤Y)log p, y M/L=O(log X) por conteo de enteros. Evaluar el funcional exacto en este minimizador da

    0 ≤ D(X,h)−D_mid(X,h) ≪_ε X^(−1/8+ε).

Esto controla íntegramente el término de variación dentro de huecos, aun cuando se reajusta la pendiente. Queda el error acumulado de las posiciones de los puntos medios. [Teorema del segundo momento de los huecos](https://arxiv.org/abs/1201.1787).

**Identidad de rango en los primos.** Para una alternativa que ni siquiera usa l como peso, ordenar p_i en I, w_i=log p_i y T_i=Σ_(j<i) w_j+w_i/2. Fijar la recta entre los dos extremos del conteo local, de pendiente c=M/L. Entonces, para M>0, con R(x)=Σ_(X<p≤x)log p−c(x−X),

    X⁻² ∫_X^Y R(x)² dx =
       1/(cX²) Σ_i w_i [T_i−c(p_i−X)]² + 1/(12cX²) Σ_i w_i³.

En efecto R empieza y termina en cero. Entre saltos d(R³)/dx=−3cR²; en cada salto la diferencia de los dos cubos es 3w_i[T_i−c(p_i−X)]²+w_i³/4. Sumar da la identidad, incluso si Y es primo. El último sumando es ≤L log²(Y)/(12X²) incondicionalmente. En la escala admitida por 231, M∼L por el PNT cuantitativo ya empleado en 213, ya que h≥(log X)^(−o(1)) y el error O(X exp(−c'√log X)) es o(L).

**Una obligación sin ajuste ni datos exteriores.** Bastaría que la primera suma normalizada del lado derecho fuera X^o(1) en una subsucesión. El error de esta recta domina el mínimo de 231, y su segundo término siempre tiende a cero. Recíprocamente bajo RH el error ordinario θ(x)−x es O(√X log² X) en I por von Koch; al restar su interpolación lineal entre los bordes el supremo cuesta a lo sumo el doble. Luego el integral normalizado cuesta O((L/X)log⁴ X) y la condición es también necesaria. Equivalente, puede usarse la media ponderada del cuadrado de la distancia de cada primo al punto X+T_i/c, con el factor c w_i/X² en la suma. Los dos términos descartables están probados; ni el teorema de huecos ni la identidad de cubos acotan esa desviación acumulada de los rangos.
