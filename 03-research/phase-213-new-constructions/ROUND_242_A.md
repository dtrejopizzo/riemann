# Bastan muestras buenas dispersas en el bloque de dos conteos

Tomar S y W de 240–241. Para t grande fijar h=exp(−(log t)²), N=ceil(t²), δ=h/N y n=ceil(t/(log t)²). En los N nodos k=0,...,N−1 medir

    V_k=exp(−t/2)|S(t+(k+1)δ)−exp(δ)S(t+kδ)|.

Si V_(n) es el n-ésimo menor valor (incluyendo empates), entonces

    lim log(1+V_(n))/t = B.

En particular si B>0 y 0<ε<B, en cada bloque suficientemente lejano a lo sumo n−1 nodos satisfacen V_k≤exp((B−ε)t). La colocación de esos nodos es libre. El bloque físico mide aproximadamente X exp(−(log log X)²) con X=exp(t); el soporte de cada peso W conserva su anchura logarítmica fija.

**Máximo del bloque.** La primera diferencia elimina el principal exactamente. El argumento de 241 para el máximo se aplica con este paso: log(1/δ)=O(log²t)=o(t), G=t(log t)³, Gδ=o(1) y M log(1/δ)=o(t) para el M≤t^(q+o(1)) del filtro, q<1. Además M<N. Para cualquier cero fijo β₀>1/2 se puede escoger σ estrictamente entre ambos. El multiplicador de primera diferencia del modo elegido es comparable a δ y conserva su exponente. La misma separación de ceros y potencias de 241 prueba log(1+max V_k)/t→B, incluso para esta elección de h más corta.

**De n nodos al máximo.** Interpolar la función real sin módulo g(v)=S(t+v+δ)−exp(δ)S(t+v) en los n nodos de menor módulo. En [0,h] cada numerador elemental de Lagrange tiene módulo ≤h, y cada separación entre nodos es ≥δ. Por tanto el valor absoluto del interpolante es ≤n N^(n−1)exp(t/2)V_(n), donde log(n N^(n−1))=o(t). Para la derivada de orden n del conteo basta derivar las primeras n cajas de W y reservar otra caja para la norma suprema. Como 1/a_j≤Cj², esto cuesta exp(O(n log(n+2))). Los primos que intervienen cumplen p≤exp(t+1) para t grande y la suma de sus pesos log p es ≤exp(t+O(log t)). El resto real de interpolación es así ≤exp(t+O(n log(n+2)+log t))h^n/n!≤exp(o(t)), uniformemente en el bloque. Tras dividir por exp(t/2), el máximo cuesta a lo sumo exp(o(t))V_(n)+exp(−t/2+o(t)). La desigualdad inversa V_(n)≤max V_k concluye.

**Qué se ganó y qué falta.** Para establecer B=0 basta exhibir en una subsucesión de bloques n nodos cualesquiera de tamaño V_k≤exp(o(t)). Su fracción n/N tiende a cero. La interpolación da estabilidad frente a la elección de posiciones y el resultado de 241 sólo controlaba el máximo. No se ha demostrado la existencia de esos n nodos buenos en bloques arbitrariamente lejanos. Los cruces de 237 son para otra suma y no aportan ese conteo.
