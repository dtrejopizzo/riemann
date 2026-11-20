# La oscilación máxima tiene escala raíz en una ventana trasladada típica

Para D entero, N=D², tomar el término fuera de diagonal de 134,

    Q(x)=Σ_{k≤N}c_k {x/k},  c_k=Σ_{a,b≤D, a≠b, ab=k}μ(a)μ(b).

Sea s uniforme real en un período común de los suelos fraccionarios, por ejemplo [0,lcm(1,…,N)]. Entonces

    E_s [sup_{0≤u≤v≤N} |Q(s+v)−Q(s+u)|²] ≤ N^(1+o(1)).

Por tanto para cada ε>0 la proporción de traslaciones donde el máximo supera N^(1/2+ε) es ≤N^(−2ε+o(1)). El máximo se toma por ventana entera, no sólo por un par de puntos prefijados. Se aplica a cada corte armónico de 134, pero la identidad que representa Mertens exige la ventana original.

**Estimación de incrementos.** |c_k|≤τ(k)≤N^o(1). La serie L² de {x/k}−1/2 tiene coeficiente −1/(2πi m) en frecuencia m/k, m entero no nulo. Reagrupar las frecuencias racionales iguales en forma irreducible j/q. El coeficiente tiene módulo ≤(2π|j|)⁻¹Σ_{r≤N/q}|c_{qr}|/r ≤N^o(1)/|j|. La ortogonalidad exacta en el período común y |exp(2πijH/q)−1|≤min(2,2π|j|H/q) dan

    E_s |Q(s+H)−Q(s)|² ≤ N^o(1) Σ_{q≤N}min(1,H/q) ≤ H N^o(1)

para 1≤H≤2N. Aquí se ha extendido la suma en j a todos los enteros positivos y negativos no nulos: Σ_{j≥1}min(1,jt)²/j²≪min(1,t).

**Del par de puntos al máximo.** Cubrir por un árbol diádico de longitud 2^ceil(log₂ N). Cada prefijo de longitud entera es suma de a lo sumo una celda de cada nivel. Por Cauchy–Schwarz su incremento al cuadrado queda acotado por O(log N) veces la suma de los cuadrados sobre todas las celdas del árbol. En cada nivel la esperanza es O(N^(1+o(1))) por la cota anterior e invariancia por traslaciones. Para los extremos reales, cada intervalo [s+j,s+j+1] contiene a lo sumo un entero en el interior, y todos los saltos de Q ocurren en enteros. La pendiente entre saltos satisface |Σ c_k/k|≤N^o(1). Así la oscilación adicional dentro de cada celda unitaria se controla por la diferencia de sus extremos más dos veces esa cota de pendiente (los s enteros son nulos en la integral). Esto prueba el enunciado.

**Por qué la traslación no es libre.** La prueba anterior sigue válida al reemplazar μ(a) por cualesquiera coeficientes reales z_a de módulo ≤1. En esa clase la ventana anclada puede tener oscilación ≫D² aun con |Σ z_a/a|≤1/D. Para verlo tomar z_a=1 en [.94D,.95D], añadir −1 en índices consecutivos de [.80D,.82D] hasta cruzar el balance armónico y escoger el más próximo de los dos valores vecinos. Hay suficientes índices por comparación de sus sumas armónicas (sus límites son log(.82/.80)>log(.95/.94)). El residuo es ≤1/(2·.80D)<1/D. El resto de coeficientes es cero. En (.88D²,.91D²] el único múltiplo de productos del soporte que aparece es el primer múltiplo de cada par alto-alto: los productos mixtos y bajo-bajo son menores, y los segundos múltiplos superan D². Los pares altos distintos aportan ≍D² saltos contados con multiplicidad y signo positivo al incremento de la suma de suelos. La pendiente fraccionaria fuera de diagonal vale (Σ z_a/a)²−Σ z_a²/a²=O(1/D). Por tanto el incremento de la suma fraccionaria tiene módulo ≫D². Es un falsificador de la inferencia de traslación para coeficientes acotados y balance armónico pequeño; no reproduce la multiplicatividad de μ.

**Cotejo y alcance.** Las series de Fourier de los dientes, la ortogonalidad de frecuencias racionales y el argumento maximal diádico son clásicos. 134 requiere el anclaje para su identidad de inversión. El cálculo distingue el coste del máximo simultáneo del problema aritmético del anclaje. Falta una estimación para s=0 con los coeficientes verdaderos en una subsucesión de los cruces armónicos.

La misma afirmación maximal vale para traslaciones enteras uniformes módulo el período. Para s=k+t con k entero y 0≤t<1, todos los incrementos de extremos enteros coinciden exactamente con los trasladados por k: Q(k+t+j)=Q(k+j)+tΣ c_l/l. Los extremos reales de la ventana con origen entero sólo añaden a los valores de la rejilla una pendiente de tamaño N^o(1) en cada tramo. Esto evita atribuir el resultado a una aleatorización dentro de la celda unitaria.
