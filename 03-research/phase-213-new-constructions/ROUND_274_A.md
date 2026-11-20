# Una banda de razón logarítmica al cuadrado para el ajuste binomial calibrado

Existe un peso fijo w≥0 de soporte [1,2] para el cual el criterio calibrado de 262 sigue siendo equivalente al signo global. Con N=⌊2x⌋ y U=⌊√N⌋, hay un ajuste incondicional de masa exacta y variación O(√N log²(2N)) que satisface todas las ecuaciones excepto, posiblemente, las de los átomos

    U/(C log²(2N)) < q ≤ U

para cierta constante absoluta C. Por encima de U la igualdad vale incluso en cada entero. Aquí se reutiliza el suavizado de 047; la conclusión adicional concierne al ajuste exacto en potencias primas de 271–273.

**Peso y criterio.** Sea L=log 2 y f la densidad de la convolución de las uniformes en [0,L/(j(j+1))], j≥1. Poner w(y)=y^(−1/2)f(log y) para y>0. Su Mellin H(s) es el producto de los factores (exp(l_j z)−1)/(l_j z), con z=s−1/2. Es distinto de cero para Re z>0, por convergencia normal de las desviaciones de uno y ausencia de factores nulos allí. El argumento de 262 se aplica con h=H(1). Un ajuste calibrado de coste x^(1/2+o(1)) implica por Stirling y Mellin ausencia de ceros a la derecha de 1/2. Recíprocamente, bajo RH la inversión de 261 cuesta x^(1/2+o(1)) por sumación parcial con Mertens y la derivada suave del peso. El defecto de calibración se corrige con la relación de 262 porque la fórmula explícita para el peso suave da ΣΛ(m)w(m/x)−xh=O_w(√x) bajo RH (decaimiento rápido de H en la franja). Se usa el criterio de ajuste calibrado; no se traslada el margen numérico del peso coseno de 257.

**Control de derivadas a todos los órdenes.** Al derivar las primeras k uniformes una vez, cada derivada tiene norma de medida 2/l_j. La siguiente uniforme tiene densidad acotada por 1/l_(k+1), y la cola tiene masa uno. Por tanto ||f^(k)||∞≤C₀^(k+1)(k!)², absorbiendo los factores polinomiales en C₀. La misma cota vale para w: en [1,2] los coeficientes de Taylor de log(y+t)−log y en t son ≤1 en módulo. En la fórmula de composición hasta orden k, la potencia de grado j del incremento aporta en grado k a lo sumo binom(k−1,j−1). Al multiplicar por f^(j)/j! y por k! resulta la cota indicada, también tras multiplicar por y^(−1/2). Todos los extremos son planos. Se obtienen los dos correctores φ_i de 273 por reescala de f y el corte χ integrando otra copia reescalada. Todos satisfacen cotas del mismo tipo.

**Cuadratura.** Usar S de 273 con w y estos correctores. El argumento de los momentos discretos da |A|+|B|≪(x/U)log²(2N). Para todo k≥0,

    ||S^(k)||₁ ≤ x log²(2N) C₁^(k+1)(k!)² U^(−k).

En efecto, en cada término χ(t/U)w(dt/x) sólo intervienen d≤4x/U, con intervalo de integración de longitud ≤2x/d. En la regla de Leibniz, las escalas de derivación son ≤4/U y binom(k,i)(i!)²((k−i)!)²≤(k!)². Sumar x/d y añadir los correctores prueba la cota. Para el coste inicial se retiene la estimación de variación O((x/U)log²(2N)) de 273.

Integrando k veces por partes y eligiendo k proporcional a √(U|ξ|) con constante suficientemente pequeña, se obtiene |Ŝ(ξ)|≪x log²(2N) exp(−c√(U|ξ|)). Para 1≤m≤U la suma en frecuencias l/m con l≠0 satisface la misma cota exponencial con c menor: para A=√(U/m)≥1 se tiene Σ_(l≥1)exp(−c A√l)≪exp(−cA/2). La suma exacta en m=1 es cero, así que la integral de S también está acotada por O(x log²(2N) exp(−c'√U)). Por periodización,

    |R(m)| ≪ (x/m) log²(2N) exp(−c'√(U/m)).

Para m≤U/(C log²(2N)) tomar C suficientemente grande: el error es O(N^(−3)) por módulo. Como el objetivo allí es cero, la reparación exacta de cadenas de 271 y la recalibración fija cuestan o(1), sin alterar m>U. Queda abierta la variación de la reparación en la banda indicada; que ambos extremos sean N^(1/2+o(1)) no acota su coste. El umbral mejorado concierne a este peso suave fijo, no al coseno original.
