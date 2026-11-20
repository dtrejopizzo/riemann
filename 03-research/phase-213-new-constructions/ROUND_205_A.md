# Un cono completo en la tabla escalar y 10¹⁵ filas enteras

En POWER_SCALAR_BRIDGE_017 fijar u=63/2 y F(s)=s^k/(s+u)^(N+k), N≥1, k≥0 enteros. Para la forma completa W se prueba:

1. W(f)>0 para TODO N si k≤10¹⁹N.
2. W(f)>0 para TODO k si N≤10¹⁵.

No hay un límite en el grado total N+k del primer enunciado. La segunda conclusión completa filas de la tabla suficiente de 017; no afirma positividad de todo numerador del mismo grado.

**Costo de la cola sin una estimación de grado.** Usar la identidad espectral de 201, válida para cada F de grado finito. Escribir G=3·10¹². En los dos puntos s=±δ+iγ de cada término, |δ|≤1/2 y |s+u|²−|s|²=u²+2u Re s≥u(u−1)>0. Así |F(s)|≤|γ|^(−N) independientemente de k. Para N≥2 la suma absoluta de toda la cola |γ|>G es <10¹⁷ G^(−2N). En efecto en las bandas diádicas B<|γ|≤2B con B=2^jG, Z3 por resta de extremos da menos de 2B log(2B) ceros contando ambos signos (la derivada principal es ≤log(2B)/(2π) y ambos errores por extremo son ≤log(2B)). Pagando B^(−2N) y sumando, el factor después de extraer G^(−2N) es ≤2G Σ_{j≥0}2^(−3j)log(2^(j+1)G)<10¹⁷.

**Un cuadrado verificado paga todo ese costo.** Por Z3 hay al menos una ordenada t₀∈[G/2,0.51G]: el incremento principal es ≥0.01G·log(G/(4π))/(2π), y la pérdida en los dos errores es ≤2 log G. Por Z2 su contribución es |F(it₀)|², y todas las demás hasta G son no negativas. Exactamente

    |F(it₀)|²=t₀^(−2N)(1+u²/t₀²)^(−N−k)
            ≥G^(−2N) exp[2N log(1/0.51)−4u²(N+k)/G²].

Si k≤10¹⁹N, el exponente es >1.3N, por los valores declarados de u y G. Para N≥100 se tiene exp(1.3N)>10¹⁷. La desigualdad resultante es estricta para la forma completa. No se localiza un cero concreto más allá de Z2 ni se supone el signo individual de la cola.

**Empalme.** Para 2≤N<100 y k<10000N², el grado de denominador N+k es <10⁸; por 204 el bloque completo es positivo. Para k≥10000N² y N≥2, POWER_QUADRATIC_EXPLICIT_017 demuestra directamente el signo del átomo (resumido en POWER_STATE_018). N=1 ya está cubierto para todo k por POWER. Esto completa el primer enunciado. Cuando N≤10¹⁵ se cumple 10000N²≤10¹⁹N, y los dos conos cubren todos los enteros k. La mejora no procede de extrapolar filas consecutivas.

**Región que queda.** Para cerrar el puente por estos dos conos bastaría demostrar signo para N>10¹⁵ y 10¹⁹N<k<10000N². Otros resultados del corpus ya cubren parte de esa región, por ejemplo POWER_SUBQUADRATIC_COROLLARY_048 en su rango asintótico. Las constantes del nuevo cono son deliberadamente conservadoras. La cota absoluta de cola por sí sola deja de ser informativa cuando el amortiguamiento de (1+u²/t₀²)^(−k) vence la ventaja (G/t₀)^(2N). No se deduce un piso relativo uniforme al crecer los índices.
