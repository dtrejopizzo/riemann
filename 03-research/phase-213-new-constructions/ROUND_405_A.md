# Cuánto pierde el producto de Euler en las alturas verificadas y superiores

**Estado: PROVED, con revisión independiente de las celdas, el PNT corto y el uso de la altura verificada.**

Sea G≥2 fijo tal que todos los ceros con |γ|≤G+1 están verificados en la recta crítica (por ejemplo G=10^6 con los datos de 175). En 404 se puede tomar cualquier constante

    0<η<1−1/(2G)

en el umbral β−γ²/(2L)>α+δ+η/b. El ahorro del grupo eliminado sigue siendo O(T₀ exp(−c L/b)), con c dependiente del margen elegido. El efecto procede de una estimación oscilatoria del producto, no de una nueva verificación de ceros.

**Aproximación uniforme por una integral corta en escala logarítmica.** Para α≤σ≤1+1/L, G≤|t|≤2√L+1, se tiene

    log|E_z(σ+it)| ≤ [1/(2|t|)+o(1)] L/b

con error aditivo uniforme en las dos variables. Las potencias segundas y superiores cuestan O(b) pues α≥1/2. Para las primeras, poner P=z^(9/10): el tramo p≤P cuesta O(z^(0.45)) por suma incluso sobre enteros. En [P,z] sustituir los primos por dq/log q. En efecto, dividir en celdas de longitud logarítmica Δ comparable a 1/(b(1+|t|)), ajustando todas las celdas para alcanzar ambos extremos. La fase y el peso relativo varían en O(1/b) en cada celda. Si la celda comienza en q, su longitud ordinaria es ≍qΔ≫q^0.70, pues |t|≤O(z^(1/4)) y q≥z^0.9. El PNT corto utilizado en 367 (exponente 17/30 más margen) da conteo relativo 1+o(1) uniforme allí; se aplica a celdas completas, sin exigir cancelación de sus errores. El error total es o(L/b), ya que la masa absoluta de la integral para σ≥α está acotada por (1+o(1))L/b. [Guth y Maynard, corolario 1.3](https://arxiv.org/abs/2405.20552)

Con w=1−σ−it y v=log q la integral es ∫_(0.9b)^b exp(wv)dv/v. Integrar por partes con primitiva exp(wv)/w. El borde superior cuesta como máximo z^(1−α)/(|t|b)=(1/2+o(1))L/(|t|b). El inferior es O(z^0.45/(|t|b)); el resto es O(L/(|t|b²)), dominando exp((1−σ)v) por exp((1−α)v). Esto prueba la estimación.

**Aplicación al contorno.** En 404 usar el tramo vertical común hasta |t|=G y hacer allí los conectores. El compacto del conector queda a distancia ≳1/b de los ceros verificados en la recta, incluso si su extremo tiene ordenada de cero. En las alas nuevas, incluido el conector, el coste logarítmico respecto de x^α es ≤δL+ηL/b+O(1), después de la gaussiana; el coste del producto es ≤(1/(2G)+o(1))L/b. El producto real en el punto de silla aporta (1+o(1))L/b. El margen estricto absorbe la longitud, √K'' y el recíproco de ζ en bordes seguros como en 403–404. El mismo argumento controla las alas verticales viejas. No se pierden polos entre 1 y G porque σ₀>1/2. Por ejemplo G=10^6 permite η=0.999999. No hay afirmación con η=1 ni con un error relativo uniforme al variar G. El grupo que excede la parábola sigue sin cota unilateral.

**Registro de revisión.** La menor longitud de celda es q/[O(b)z^(1/4)] con q≥z^(9/10), por tanto es al menos q^(13/18)/O(b)≫q^0.70. El [corolario1.3 de Guth–Maynard](https://arxiv.org/html/2405.20552v1) usa el rango q^(17/30+ε)≤longitud≤q^0.99; por ejemplo ε=1/10 deja umbral2/3<0.70. Si una celda supera q^0.99 se subdivide en piezas de longitudes entre q^0.70 y q^0.90 y se reúnen sus conteos positivos. La malla logarítmica ajustada tiene todas sus celdas comparables aΔ, sin resto terminal corto. La variación de fase y peso aporta O(1/b) relativo a la masa absoluta y el PNT aporta o(1), uniformes; al sumar no se multiplica ese error por el número de celdas. La integración por partes posterior da un error aditivo uniformeo(L/b), no un error relativo a1/|t| cuando t crece.

La hipótesis verificada cubre G+1, lo que protege los conectores y los ceros vecinos. El ejemplo G=10^6 está muy por debajo de3·10^12, la altura verificada de [Platt–Trudgian](https://arxiv.org/abs/2004.09765) usada comoZ2 en175. G se fija antes de hacer x→∞. El margen disponible es exactamente1−η−1/(2G)>0, y permite elegir el ahorro exponencial después de fijarη yG; no se pasa al extremoη=1 ni aG variable.
