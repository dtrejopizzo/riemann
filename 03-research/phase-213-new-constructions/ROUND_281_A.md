# La diagonal de las muestras, incluidas las dos calibraciones, ya cuesta raíz

Para los puntos y de 280 hay coeficientes reales explícitos K_y(d), independientes de μ, tales que con V=x/U y P=log(2N),

    T(y)=Σ_(d≥V) μ(d) K_y(d) + O(P⁶),       Σ_d |K_y(d)|² ≪ U P⁶.

Las series se toman en orden creciente de d. Esto incluye las dos correcciones de masa y balance, aun cuando su definición original en 273 utilizaba todos los d desde 1. Como hay O(P² log P) puntos, la diagonal de la suma de cuadrados completa cumple incondicionalmente O(U P⁹). Queda una condición sobre correlaciones entre enteros distintos, con un núcleo que es una matriz de Gram explícita.

**Correcciones.** Conservar la matriz discreta de 273 dividida por U, centrando la segunda fila por 1+log U, y denotar su inversa por M, de norma O(1). Para S₀(t)=χ(t/U)Σ μ(d)w(dt/x), los dos términos discretos a restar a los objetivos (0,xh) pueden sustituirse por ∫S₀(t)dt y ∫S₀(t)log(t/U)dt con error O(U P²). En efecto Var(S₀)≪x/U, por suma de variaciones; para la segunda coordenada se usa la integral exacta de log(t/U) sobre (j−1,j] que equivale a la diferencia discreta centrada. En las celdas relevantes el logaritmo es O(P). Incluida la división por U, el error en las amplitudes es O(P²).

En el orden de suma por d, las integrales SIN corte de cada copia w(dt/x), contra 1 y log(t/U), ponderadas por μ(d), suman respectivamente 0 y xh. En efecto cada copia da xh/d en la primera, y en la segunda (x/d)∫w(u)log(xu/(dU))du. Se usan Σμ(d)/d=0 y Σμ(d)log(d)/d=−1, obtenidas por el teorema de los números primos con resto clásico, sumación parcial y el valor y derivada de 1/ζ en 1. Este cálculo integra cada copia antes de sumar; no intercambia una integral global con una serie no absolutamente convergente.

Así el vector de amplitudes es Σ μ(d) v_d + O(P²), donde v_d es M aplicado a

    (V/d) ∫ w(u) [1−χ(Vu/d)] (1,log(Vu/d)) du.

Es cero para d<V. Para d≥V su norma es O((V/d)(1+log(d/V))); luego Σ||v_d||²≪V por comparación con la integral escalada. Es esencial retirar el momento completo conocido antes de estimar: los pesos x/(Ud) sin esa cancelación comenzarían en d=1.

**Coeficientes por muestra.** Poner Φ(y)=(Σ_l φ_i(ly/U))_(i=1,2). Por 279 la inversión completa suma cero en la banda. Por tanto

    K_y(d)= Φ(y)·v_d − Σ_(l≤U/y) [1−χ(ly/U)] w(dly/x).

El segundo sumando sólo usa V≤d≤2x/Y y tiene tamaño O(P²); ||Φ(y)||≪P². Hay O(U P²) enteros en el intervalo y V≍U. Esto da la cota cuadrática anunciada y un error de evaluación O(P⁴), absorbido en el enunciado.

**Qué estimación bastaría.** Para el conjunto de muestras prefijado definir G(d,e)=Σ_y K_y(d)K_y(e). Para cada x sumar primero sobre d,e≤L y tomar L→∞. El corte rectangular converge al cuadrado de cada serie convergente, y la diagonal converge absolutamente. Así

    Σ_y |Σ_d μ(d)K_y(d)|²
      = Σ_d μ(d)²G(d,d) + lim_(L→∞) Σ_(d≠e≤L) μ(d)μ(e)G(d,e),

donde en la última suma ambos índices son ≤L. El primer término es O(U P⁹). Junto con 280, RH equivale a que en alguna subsucesión x_j→∞ el término fuera de la diagonal sea ≤x_j^(1/2+o(1)). En efecto la suma de cuadrados controla el máximo, y bajo RH el máximo cumple el techo de cuarto de potencia, incluso a toda escala. Los errores O(P⁶) por muestra no afectan ninguno de los exponentes. El núcleo es positivo semidefinido en cada corte por construcción; la positividad sólo da un piso para la suma fuera de la diagonal, mientras el cierre exige un techo. A diferencia de la bilineal de 049, aquí el núcleo proviene de cuadrados de un conjunto prefijado de muestras y las contribuciones de calibración se controlan en la misma diagonal. El techo para los pares distintos sigue abierto.
