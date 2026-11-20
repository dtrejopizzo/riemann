# Ajuste calibrado incondicional en todos los módulos por encima del corte de raíz

Para N=⌊2x⌋, 2≤U≤N entero, existe una combinación de filas binomiales genuinas, de extremos ≤N, que reproduce g(m/x) para CADA entero m>U hasta N y tiene masa entrópica exactamente xh. Su variación es O((x/U)log²(2N)). En particular, elegir U=⌊√N⌋ cumple simultáneamente todas las ecuaciones de los primos grandes de 271 y la calibración inicial con coste x^(1/2+o(1)).

**Construcción superior.** En la inversión de 261 retener sólo b_j=S_j−S_(j+1) para j>U, con S_j=Σ_d μ(d)g(dj/x). Los coeficientes descartados multiplican F_j(m)=⌊j/m⌋ idénticamente cero para m>U. En cada d contribuyente (d≤N/U), la variación del muestreo de g(dj/x) es a lo sumo Var(g) y sus términos con diferencia no nula tienen j≤N/d. Por suma absoluta se obtienen

    Σ_(j>U)|b_j| ≪ x/U,      Σ_(j>U) j|b_j| ≪ x log(2N).

Agregar F_U con coeficiente β=−Σ_(j>U)j b_j/U. La familia de símbolos queda balanceada, de modo que el promedio cíclico formal de 261 la convierte en filas genuinas con coste ≤2(Σ|b_j|+|β|). Esta conversión conserva el valor de cualquier evaluación lineal de los símbolos.

**Ajuste de la masa sin tocar la interpolación.** Evaluando F_j en j log j, la masa H₀ de la combinación balanceada es Σ_(j>U)j b_j log(j/U). Por la segunda cota su módulo es O(x log²(2N)). Tomar la fila de extremo U y lado ⌊U/2⌋. Su entropía e es ≫U por la fórmula de entropía binaria y porque ⌊U/2⌋/U∈[1/3,1/2]. Todos sus acarreos son cero en m>U. Añadir la fila con coeficiente (xh−H₀)/e da la calibración requerida dentro del coste anunciado.

**Residuo localizado.** Escribiendo λ=(xh−H₀)/e, en m≤U el error exacto (objetivo menos respuesta) es

    r(m)=Σ_(j≤U)b_j⌊j/m⌋ − β⌊U/m⌋ − λ c_(U,⌊U/2⌋)(m).

Aquí los b_j de la suma son los originales de 261. Por encima de U el error se anula incluso en las potencias propias de los primos pequeños. Para U=⌊√N⌋, la variación de 271 queda concentrada en las cadenas hasta U, con cero en su siguiente nivel. Falta probar que esa variación sea de tamaño de raíz, para esta elección o para otra distribución de los coeficientes inferiores que conserve el balance y la masa. La magnitud del coste inicial por sí sola sólo da una cota puntual de tamaño comparable al coste en cada átomo inferior; sumar tales cotas no cierra la prueba. El ajuste calibrado de los módulos grandes sí queda construido incondicionalmente.
