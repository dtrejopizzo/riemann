# Coste óptimo para comprimir universalmente a un número fijo de extremos

Fijar r≥1. Entre todas las listas de hasta r+1 extremos binomiales ≤N, el mínimo del peor coste para reproducir una sola fila arbitraria en todos los módulos enteros es de orden N^(1/r), con constantes que pueden depender de r. Se permite optimizar la lista de nuevo para cada N, y usar coeficientes reales. Para la cota inferior basta una fila con dos lados iguales si la lista incluye N.

**Precisión del modelo.** El coste es la suma de los valores absolutos de los coeficientes, infinito si la fila carece de representación. La reproducción formal de 269 y la reproducción en todos los módulos dan el mismo problema: la matriz (⌊j/m⌋) para j,m=1,…,N es triangular de diagonal uno. La coordenada m=1 de cada fila es automáticamente cero. Una lista que omite N falla en m=N para cualquier fila no degenerada de extremo N.

**Certificado para cualquier lista.** Escribir la lista como N,n₁,…,n_r, repitiendo N si faltan extremos. Para N suficientemente grande poner Q=⌊(N/32)^(1/r)⌋. Entre los Q^r+1 vectores de partes fraccionarias de j(n₁,…,n_r)/N, para 0≤j≤Q^r, dos caen en una misma caja de la partición en Q^r cubos de lado 1/Q. La diferencia de sus índices da 1≤l≤N/32 con dist(l n_i/N,ℤ)≤1/Q para todo i.

Evaluar los símbolos formales en F_j=sin(2πlj/N). Para un extremo permitido n reducir θ=2πln/N módulo 2π al representante de menor módulo. Entonces |θ|≤2π/Q y para cualquier reparto de fase u=2πlk/N se tiene

    |F_n−F_k−F_(n−k)| = |sin θ−sin u−sin(θ−u)| ≤ 2|θ|.

En cambio elegir k como el entero más próximo a N/(4l). Tiene 1≤2k≤N y |u−π/2|≤π/32. En particular |sin(2u)−2sin u|≥2cos(π/32)−sin(π/16)>1. La fila con extremo 2k y lados k necesita por tanto variación ≥Q/(4π). El certificado se construye a partir de los extremos, antes de elegir sus coeficientes.

**Techo coincidente.** Tomar en 269 la base b=⌊(N/2)^(1/r)⌋+1. Como b^r>N/2, se usan a lo sumo r desplazamientos distintos y N. Cada k≤N/2 tiene a lo sumo r cifras y el coste es ≤4r(b−1). Las dos cotas fijan el exponente exacto para todo r fijo.

**Decisión para el problema del signo.** Con tres extremos óptimamente elegidos, la peor pérdida universal ya es de orden √N. Una lista de tamaño fijo nunca ofrece pérdida N^o(1) para un procedimiento que sustituya cada fila y conserve todos los módulos. Esto delimita el uso de la compresión de 269: para un número fijo de extremos y pérdida subpotencial habrá que explotar el objetivo concreto de 262, la libertad en los compuestos o cancelaciones entre filas. El funcional sinusoidal usado aquí actúa sobre todos los símbolos y no se ha representado por las restricciones de potencias primas y entropía. No se deduce un piso de este tamaño para el peso g.
