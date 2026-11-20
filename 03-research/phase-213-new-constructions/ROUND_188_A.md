# El error lineal del test 187 se realiza con ambos signos

Con las convenciones de 187 y κ>0 fijo, hay frecuencias Γ_+ y Γ_− en [2G,3G] tales que |S_X(Γ_±)|/√X=o(T) y

    min_θ W_T(f_θ) − [log Γ_± − |S_X(Γ_±)|/√X] = ±(2+o(1))T.

Así, buscar el signo residual mediante un reemplazo uniforme del error O(T) por o(T) falla incluso en la banda prescrita y para el peine de ζ. Los ejemplos construidos tienen margen principal positivo grande.

**Corrección firmada.** El solapamiento exacto de 187 da para la diferencia anterior, uniformemente en Γ,

    −(4/B) Re Σ_{n≤Z}Λ(n)(1/n−1/Z)n^{iΓ} + O(1),  Z=e^T.

En efecto, la parte interna es independiente de θ y las dos sustituciones en la parte cruzada cuestan O(1) en total. Polos y diferencia del arquimediano respecto de log Γ cuestan O(1). Los términos de potencias no primas de la suma interna son O(1) absolutamente por convergencia. El término 1/Z cuesta O(1) por Chebyshev. La masa de los primos en el peso log p/p hasta Z es (1+o(1))T por PNT, así que 2 es asimismo el mejor coeficiente principal posible para el error uniforme.

**Elección de la frecuencia.** Tomar Y=Z/T³ y K=floor(T). Para σ∈{−1,1}, usar R(t) de 185 sobre todos los primos p≤Y con coeficientes locales σ^r b_r. La suma de cuadrados de coeficientes es uno, y la longitud L de R satisface log L≤K ψ(Y)=O(Z/T²)=o(log G). El cuadrado de la suma de módulos de coeficientes es ≤L. Usar la probabilidad en [2G,3G] proporcional a |R|². Su constante normalizadora, en la medida dt/G, es 1+o(1). Como en 185, la esperanza de σ Re p^{it} es cos(π/(K+1))+o(1) uniformemente para p≤Y. Los errores de diagonal en estos promedios son O(YL²/G). Por no negatividad y Markov,

    Σ_{p≤Y}(log p/p)(1−σ Re p^{it})=o(T)

con probabilidad tendente a uno (escoger un umbral o(T) mayor que la esperanza por un factor divergente). Entre Y y Z la masa es O(log T) por Chebyshev y sumación parcial. Se obtiene la corrección firmada −(2σ+o(1))T.

**La suma cruzada en la misma frecuencia.** En S_X los primos p≤Y cuestan O(Y log X)=o(√X). La masa en potencias de orden ≥2 hasta x es O(√x) por Chebyshev para cuadrados y O(x^(1/3)log²x) para las demás. Integrando contra dx/x, su contribución al peso de Riesz es O(√X). Para los primos p>Y usar el segundo momento de H(t)=Σ_{Y<p≤X}(log p)log(X/p)p^{it} contra la misma probabilidad. La diagonal de |RH|² consta sólo de coincidencias idénticas por factorización única, pues los índices de R son Y-lisos. Su masa es Σ_{p≤X,p>Y}(log p)²log²(X/p)=O(X log X), por Chebyshev en franjas con j≤log(X/p)<j+1 y suma de (j+1)² exp(−j). El error de la integral fuera de la diagonal es O((LX)L X²/G)=o(1), por separación de logaritmos de enteros hasta LX y Σ_p(log p)log(X/p)=O(X). En particular |H(t)|≤√X T^(3/4) con probabilidad tendente a uno. La intersección con el evento anterior tiene probabilidad positiva para T grande, lo que prueba ambas afirmaciones simultáneas.

**Alcance.** Se usan el resonador ya conocido de 185 y la identidad de 187. La obstrucción adicional es una realización dentro de la banda del coeficiente óptimo de la corrección y su independencia, en este ejemplo, de un valor grande de la suma cruzada. La demostración no dice que la misma corrección sea posible *condicionada a* |S_X|/X próximo a κ.

Se revisó independientemente la corrección, la longitud del resonador, la diagonal del segundo momento y la selección simultánea de frecuencia.
