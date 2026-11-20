# Anchura de las excepciones de paridad en la escala logarítmica

**Estado: PROVED, con revisión independiente de las celdas de corte, el caso Θ=1 y las dos consecuencias integradas.**

Usamos S(x) y Θ de 372. Si Θ>1/2, para cada η>0 y cada signo e=±1 existen v arbitrariamente grandes e intervalos I⊂[v−1,v+1] de longitud ≥exp(−ηv) donde e S(exp w)>exp((Θ−η)v) en todo I. El corte es el exacto w², incluso al lado de un salto.

**Prueba.** Elegir 0<δ<min(η/5,(Θ−1/2)/2). Por 372 hay v→∞ con e S(exp v)>exp((Θ−δ)v). Para un corte congelado z=v² y |w−v|≤1 tenemos

    |∂_w S^*(exp w;z)| ≪δ exp((Θ+δ)v).

Si Θ<1, se usa una vertical fija Θ<σ<min(Θ+δ,1) como en 372. Derivar introduce sólo s en la integral, absorbido por la gaussiana; el coste E_z(σ)=exp(o(v)) es uniforme. Si Θ=1 se puede sumar en módulo la derivada del peso, acotando |g'| por una gaussiana más ancha con el mismo factor exp(u/2); la suma diádica cuesta O(exp w). La cota de derivada también vale si se mantiene el conjunto de primos correspondiente a v² en ambos lados de v.

Los posibles saltos están en los puntos √p, p primo; basta usar la partición más fina por √n, n entero. La celda [√floor(v²),√(floor(v²)+1)) que incluye v tiene longitud asintótica a 1/(2v). En al menos un sentido desde v queda una distancia ≥1/(5v) hasta su borde; si v es extremo izquierdo se toma el lado derecho, pues el corte incluye los primos p≤v² y es constante a su derecha. Sobre ese lado el conjunto de primos retirados coincide exactamente con el de v. El intervalo cerrado de longitud exp(−3δv) cabe estrictamente antes del siguiente borde para v grande y la variación es Oδ(exp((Θ−2δ)v)), despreciable frente al valor inicial. El resultado sigue por la elección de δ.

**Dos consecuencias.** La integral de max(S(x),0) dx/x^(3/2) desde e hasta infinito es finita si y sólo si RH. Bajo RH, 368 anula el integrando eventualmente. Si Θ>1/2, escoger 2η<Θ−1/2 en el resultado anterior: un solo intervalo aporta al menos exp((Θ−1/2−2η)v−1), sin límite.

Incluso se pueden ignorar las amplitudes. Sea B={x≥e:S(x)>0}. Para cualquier ε>0 fijo, RH equivale a la finitud de ∫_B x^(ε−1)dx. Bajo la alternativa, elegir η<ε y un intervalo del signo positivo; su contribución es ≥exp((ε−η)v−ε). Esto no implica divergencia de la medida logarítmica ∫_B dx/x.

292 integra una parte positiva en un parámetro auxiliar. Aquí se estima la longitud de intervalos de una sola variable con corte discontinuo y se puede integrar únicamente la indicadora del signo. Queda abierta una estimación aritmética de esa medida. La revisión independiente comprobó que el argumento de Θ=1 usa sólo la suma absoluta de |g'|, sin necesitar una vertical a la derecha de Θ dentro de la franja. En las consecuencias integradas no hace falta seleccionar intervalos disjuntos: la masa de un solo intervalo tiende a infinito, lo que ya contradice la finitud de la integral total. Bajo RH las integrales sobre el compacto inicial son finitas por convergencia uniforme de la suma gaussiana. Deducción dependiente de 368 y 372.
