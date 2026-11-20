# Traslaciones firmadas sobre un número creciente de anchos de celda

El antecedente 015-A recupera la acumulada en dos franjas. Al superar el ancho de celda se solapan las franjas y el soporte físico de la cola crece. La operación aquí combina reconstrucción desde el extremo derecho y extracción de la masa firmada antes de estimar la oscilación del peine. El cotejo distinguió esta extracción de la cuadratura relativa a la variación total en 013 y de la cota por la norma L¹ de toda la cola en 015.

**Enunciado.** Existe γ>0 tal que, para todo k suficientemente grande, las traslaciones de F_k en cualquier intervalo de longitud γ/√(k log k) generan un espacio en el que la energía es estrictamente positiva para todo vector no nulo. Se admiten medidas complejas finitas y cualquier número de términos. Se usa la normalización de 015.

**Reconstrucción.** Poner w=log(1+1/k), M entero positivo y r=Mw≤1. Trasladar el intervalo a [0,r]. Para la medida ν(ds)=exp(−s/2)μ(ds) extender su acumulada L(u) por cero a la izquierda y por su masa c a la derecha. En variable física la cola b satisface b(k exp u)=d(L(u)−L(u−w)) casi en todas partes. Escribir D=Ub. Para 0<u<r telescopar desde u hasta u+Mw≥r. Para H=L−c en (0,r), Minkowski y dy≥k du sobre el soporte implican

    ||H||₂ ≤ M ||D||₂/(d√k).

La cabeza logarítmica se escribe cF+g, donde F es la cabeza de F_k antes de mezclar. El resto g está en tres tubos de longitud r con coeficientes de salto acotados, así ||g||≤CM||D||/√k. La norma física de b en L¹ es ≤C√M||D||, pues el soporte tiene longitud k(exp(r+w)−1)≤CM para r≤1. Su integral firmada satisface exactamente

    ∫b(y)dy=d∫exp(s)dν(s)=d(c−∫₀ʳ exp(s) H(s)ds).

La primera igualdad integra celdas de longitud exp(s), la segunda es Fubini o integración por partes con los extremos incluidos. En particular el error al sustituir la masa por dc es ≤C M^(3/2)||D||/k.

**Energías propias.** Tomamos M≤√(k/log k), de modo que r→0. En ventana fija a(F)=q(w)>0.15 para k grande, el representante de a(F,·) está acotado en L² y a(g)≥−C||g||² como en 015. Así la energía de cabeza es ≥0.15|c|²−o(1)(|c|²+||D||²). En ventana trasladada fija el soporte de cola tiene longitud r+w→0. Por 010, a(D)≥||D||².

**Cruces.** Entre g y D cada tubo admite O(M) contactos con n comparable a k y pesos O(log k/√k). El valor absoluto de todo este cruce aritmético es ≤ C₁ M²(log k)/k ||D||², con C₁ independiente de k,M. Para cF y D usar S_k(y) de 015. Por PNT S_k(k)=o(1). Para k≤y≤k exp(r+w), cada extremo y/i de las dos bandas de sumación cambia en O(M). Como cada sumando vale O(log k/k), se tiene |S_k(y)−S_k(k)|≤CM log k/k. El término constante de la integral mixta paga sólo la masa firmada calculada arriba. La oscilación paga ||b||₁. En conjunto el cruce está acotado por

    2|c| [ |S_k(k)| (d|c|+CM^(3/2)||D||/k)
                 + CM^(3/2)(log k)||D||/k ].

Es o(1)(|c|²+||D||²) uniformemente en el rango elegido. Para el cruce arquimediano, el núcleo entre cabeza y cola es O(1/k) por 014. La longitud del soporte físico de cabeza es acotada y su norma L¹ es O(|c|+||g||). La estimación precedente de ||b||₁ vuelve a dar un error relativo o(1). Todos los dominios y los pasos a medidas son los de 015, para k fijo.

Elegir M=floor(θ√(k/log k)) con 0<θ≤1 constante tan pequeña que C₁θ²≤1/4. Para k grande resulta a(Y)≥0.07|c|²+||D||²/2. Si c y D se anulan, la reconstrucción obliga a g=0 y por tanto Y=0. Finalmente Mw√(k log k)→θ, así que basta γ=θ/2. El radio tiende a cero, pero su cociente con el radio de 015 tiende a infinito. Sigue pendiente pagar los cruces para separaciones fijas y para el portador global. PROVED tras auditoría matemática independiente.
