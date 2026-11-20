# Bandas favorables probadas para μ y un falsificador multiplicativo del salto de longitud

Para B,A>0 fijos y H=√X(log X)^B, el máximo de |Σ μ(n)| sobre todos los prefijos de (x,x+H] es ≤√X/(log X)^A para casi todos los inicios x∈[X,2X]. En efecto, es el teorema 1.1(i) de Matomäki, Radziwiłł, Shao, Tao y Teräväinen con la función constante uno y ahorro logarítmico A+B; su norma maximal incluye todos los subintervalos e incluso todas las progresiones. El conjunto excepcional tiene medida O_(A,B)(X/(log X)^(A+B)). Es un resultado externo aplicado al umbral de 285. [Teorema 1.1(i) y definición (1.4)](https://doi.org/10.1007/s00222-026-01408-6).

**El obstáculo al ensamblaje.** Hay una sola función multiplicativa f con |f(n)|=μ²(n), que puede coincidir con μ hasta cualquier umbral inicial prescrito, con ambas propiedades:

* En H=√X(log X)^B, el máximo anterior incluso sobre progresiones es ≤√X/(log X)^A salvo en un conjunto de medida O_(A,B)(X/log^A X), para todo A,B fijos.
* En CADA banda grande [X,Xexp(h)] de 285, la excursión máxima desde X es ≥X^(3/4−o(1)).

Por tanto las ventanas cortas favorables, su frecuencia y la multiplicatividad con soporte exactamente libre de cuadrados no bastan como únicos insumos para construir la subsucesión larga. A diferencia de 137, se conservan las cotas maximales de casi todos los intervalos y el fallo se impone en cada banda larga, para la propia suma parcial.

**Elección de los primos.** Poner β=3/4. A partir del umbral inicial, recorrer los primos acumulando p^(β−1); incluir un primo en S cuando aumenta la parte entera del acumulado. Se tiene #S(≤z)−Σ_(p≤z)p^(β−1)=O(1), con constante que admite el umbral. Invertir el signo de μ en los primos de S, extender multiplicativamente en los libres de cuadrados y poner cero en los demás. Entonces f=μ*b, donde b es no negativa con factores de Euler (1+p^(−s))/(1−p^(−s)) en S y uno fuera. Σ b(d)/d^η converge para η>β por el recuento #S(≤z)≪z^β.

**Transferencia en intervalos cortos.** Cortar la convolución en d≤Z=log^K X. Para cada d en ese rango aplicar el teorema citado en escala X/d, longitud H/d (entre (X/d)^(1/3+ε) y (X/d)^(1−ε) con ε fijo pequeño), con ahorro R arbitrariamente grande. La preimagen de una progresión al imponer d|n es una progresión o el vacío. La unión de excepciones mide O(ZX/log^R X) y la contribución buena cuesta O(H log^(−R)X Σ b(d)/d). Para d>Z la integral sobre los inicios de la suma de módulos es O(HX Σ_(d>Z)b(d)/d), por conteo de múltiplos hasta 3X. La cola es O_η(Z^(η−1)) para β<η<1. Primero elegir K y después R suficientemente grandes y aplicar Markov. Se puede gastar una potencia logarítmica adicional para absorber las constantes. Esto da la primera propiedad.

**Polo que obliga a fallar en las bandas largas.** En Re s>1 la serie de f se factoriza como

    ζ(s+1−β)² H₀(s)/ζ(s).

H₀ es holomorfa y no nula en Re s>1/2. Para verlo tomar el logaritmo del producto de b y restar 2log ζ(s+1−β). Los términos de primer grado dan 2Σ_p(1_S(p)−p^(β−1))p^(−s), holomorfo para Re s>0 por la discrepancia acumulada acotada. Los grados restantes convergen absolutamente para Re s>1/2, tanto en los factores de S como en la zeta desplazada. En particular la serie prolongada tiene un polo DOBLE real en β, pues ζ(β) es finita y distinta de cero.

El crecimiento permite usar el contorno de 285, también para las bandas que se estrechan. Para 1/2<σ₁<σ₂<β, en σ₁≤Re s≤2 la suma de primeros grados hasta R=(2+|Im s|)^(1/β) cuesta O(R^(β−σ₁)) por suma absoluta y recuento; su cola cuesta O((1+|s|)R^(−σ₁)) por sumación parcial. Así |H₀(s)|≤exp(C(2+|Im s|)^κ) con κ=1−σ₁/β<1/2. La zeta desplazada crece a lo sumo polinómicamente en la franja a altura grande. Construir el filtro de 285 tomando como objetivo el polo real β y anulando con multiplicidad los ceros de ζ de parte real ≥σ₁. Multiplicar su transformada por s−β deja un residuo fijo distinto de cero. La cota adicional exp(C|τ|^κ) se absorbe en la mitad del decaimiento Gevrey exp(−c√(h|τ|)), a coste exp(O(h^(−κ/(1−2κ)))); éste es exp(o(log X)) en el rango de 285. El mismo desplazamiento da una suma ponderada igual a c₀ X^β+O(X^σ₂ exp(o(log X))), c₀≠0. Por sumación parcial se obtiene la segunda propiedad. Este falsificador conserva la ley de tamaños y la multiplicatividad; cambia la identidad exacta μ*1=δ.
