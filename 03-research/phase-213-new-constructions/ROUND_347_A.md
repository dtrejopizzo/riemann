# Emparejamiento entre productos impares distintos en el observable completo

Para X grande y Y=X^(1/3) existen a<b impares libres de cuadrados en [Y,3Y] con μ(a)=−μ(b) y b−a≤Y^(1/4). Elegir una sola pareja por X, independiente de x. En todos los centros X≤x≤2X y con h=X^(−δ), 0<δ≤1/16 fijo, seleccionar los productos at y bt para t impar libre de cuadrados y (t,ab)=1. En el observable completo C_h de 342 esta familia tiene masa absoluta al menos X^(2/3−δ−o(1)), pero su contribución firmada conjunta cuesta O_η(X^(5/12))=o(√(Xh)) uniformemente. Se trata de enteros distintos incluso después de reunir todas las representaciones de cada producto.

**Existencia de los dos factores.** En intervalos (y,y+J] con Y≤y≤2Y y J=Y^(1/4), la media en y de la cantidad de impares libres de cuadrados es ≫J, por integración y su densidad positiva en el intervalo largo. Como el máximo es O(J), una proporción positiva de centros tiene ≫J tales enteros. Por la cota maximal sobre progresiones de 329 y 333, fuera de un conjunto de proporción o(1) la suma de μ sobre la progresión de impares del intervalo es o(J). El umbral 1/6+ε queda estrictamente por debajo de 1/4. Algún centro cumple ambas condiciones y contiene los dos signos. [Insumo de intervalos cortos, §1.1](https://arxiv.org/html/2411.05770v1)

**Identidad de signos y coste.** Sobre impares, el coeficiente completo de C_h es μ(n). En cada pareja μ(at)=−μ(bt); las dos clases de productos son disjuntas ya que si at=bu entonces b/(a,b)>1 divide t, contradiciendo la coprimalidad. En cada clase por separado tampoco hay repeticiones. Su suma firmada vale

    μ(a) Σ_t μ(t)[W_x(at)−W_x(bt)]

con las restricciones anteriores. La diferencia de pesos cuesta a lo sumo ‖η'‖∞ log(b/a)/h. Como log(b/a)≪Y^(−3/4)=X^(−1/4)≪h, la unión de los dos soportes contiene O(1+hX/Y) enteros t. De aquí sale O(X/Y · Y^(−3/4))=O(X^(5/12)). Este paso ni siquiera requiere cancelación entre los t.

**Masa retirada.** Basta contar productos at con η acotada por debajo en un subintervalo. El rango de t tiene longitud comparable a hX/Y. El recuento de 341 con Q=2ab tiene término principal de densidad c_Q=ζ(2)^(−1)∏_{p|Q}p/(p+1)≥X^(−o(1)) (por ejemplo c_Q≥ζ(2)^(−1)/τ(Q)). El error O(τ(Q)√(X/Y)) es X^(1/3+o(1)). Resulta el piso anunciado. Para δ≤1/16 la masa supera por una potencia a √(Xh), mientras que el saldo queda estrictamente por debajo.

**Límite.** 346 cancela representaciones del mismo n. Aquí se cancela en familias de n diferentes con los coeficientes verdaderos del observable completo. Una sola pareja de factores sólo cubre O(hX/Y) muestras por centro. Para sumar muchas familias se necesitan clases disjuntas o una contabilidad de sus intersecciones, además de controlar el saldo acumulado y los productos sin cubrir. No se infiere el signo global.
