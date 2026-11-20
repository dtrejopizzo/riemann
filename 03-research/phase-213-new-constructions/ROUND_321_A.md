# El operador corto es pequeño en media de frecuencias, pero no admite contracción uniforme

En la construcción de 320 distribuir la corrección de densidad como en 049: tomar a(d)=μ(d) para d≤D, a(d)=c para D<d≤2D, con c=−(Σ_(d≤D)μ(d)/d)/(Σ_(D<d≤2D)1/d), y cero después. Así |c|≪log(2D); la prueba de 320 sigue literalmente porque sólo usaba el soporte, la masa armónica cero y Σ|a|≪D log(2D). Con g=1*a y el mismo corte, la acción de la suma intermedia en la función de escala x^s es multiplicar por

    H_X(s)=Σ_(D<n<2N) g(n)(1−ψ(n/N))n^(−s).

La frecuencia Im s es dual de log x; es distinta del parámetro t de los coeficientes aritméticos. Hay tres comportamientos verificables.

**Frecuencia media.** Fijada 1/2<σ<1, el promedio sobre [0,T] de |H_X(σ+iτ)|² converge cuando T→∞, con X fijo, a la suma de cuadrados de los coeficientes ponderados. Integrar los términos cruzados lo prueba directamente. Puesto que |g(n)|≪τ(n)log(2D), esa suma es O_(σ,ε)(D^(1−2σ+ε)) por el techo divisorial y la suma desde D hasta infinito (usar una pérdida menor que 2σ−1). Tiende a cero para X→∞. Es importante distribuir la corrección: un solo coeficiente grande en 2D no da esta prueba.

**Amplificación uniforme.** Para la misma σ y cualquier altura inicial T₀ se tiene sup_(τ>T₀)|H_X(σ+iτ)| ≫_σ N^(1−σ)/log N. En efecto, las frecuencias log p de los primos hasta 2N son racionalmente independientes por factorización única; el teorema de Kronecker para el flujo continuo permite aproximar simultáneamente cualquier elección de fases, también a alturas arbitrariamente grandes. Elegir todas las fases iguales a exp(iθ). El primer coeficiente de Fourier en θ del polinomio resultante sólo recoge los enteros con un único factor primo contado con multiplicidad, es decir, los primos. En 2D<p≤N se tiene g(p)=1 y el corte vale uno. En N<p<2N sigue siendo no negativo, y D<p≤2D cuesta en total O_σ(D^(1−σ)log D). Por el PNT los primos de [N/2,N] aportan ≫N^(1−σ)/log N, que domina ese coste porque N es comparable a D³. El máximo del módulo domina el módulo del coeficiente. Por tanto no hay contracción para todos los modos x^(σ+iτ), aunque el cuadrado medio tienda a cero.

**En una frecuencia fija que corresponde a un cero.** Sea A_D(s)=Σ a(d)d^(−s). Para cada s fijo con 0<Re s<1 y cada K fijo,

    1+H_X(s)=ζ(s)A_D(s)+O_(s,K)((log X)^(−K)).

Para Re s>1 la diferencia es el muestreo con signo de f(v)=ψ(v/N)v^(−s), salvo el signo global de la resta. En Poisson se cancela la integral porque A_D(1)=0. Las integrales de Fourier a frecuencia no nula, expresadas con j integraciones por partes, se continúan a Re s>0 y son localmente uniformes: ||f^(j)||₁≪_(s,j) N^(1−Re s−j) para j≥2. Esto continúa la identidad por unicidad; el polo en 1 del producto es removible. El error total cuesta O_(s,j)(N^(1−Re s−j)D^j log(2D)). Dado que N/D es comparable a (log X)², basta elegir j fijo suficientemente grande. Así, en cualquier cero crítico fijo ρ se tiene H_X(ρ)=−1+O_K((log X)^(−K)). En la recurrencia la muestra principal lleva coeficiente +1, de modo que este modo se cancela hasta todo orden logarítmico.

La aproximación de fases de Bohr ya figura en el índice en otros problemas de operadores. Aquí las tres estimaciones se aplican al mismo símbolo corto que se requería controlar en 320. La segunda impide demostrar el signo mediante una contracción uniforme del operador desnudo; no dice que la entrada aritmética observada por el núcleo positivo tenga peso relevante a las alturas extremas. La tercera explica por qué la recurrencia tolera modos críticos incluso a altura fija. Falta controlar la acción sobre los saldos aritméticos concretos.
