# Bloques de longitud p^a que conservan el baricentro al perder primos

Fijar 3/4<a<1. Para un primo p poner h=p^a y N=#{r primo:p<r≤p+h}. Sea M(p) el mayor entero 0≤m≤N tal que quitar CUALQUIER conjunto de hasta m de esos primos deja C(y)>0 en TODO p≤y≤p+h. Poner M=0 si ya falla sin quitar nada. Con Θ de 249 se cumple

    limsup_(p primo→∞) log(1+M(p))/log p = min(a,1+Θ−a).

Bajo RH se tiene además, uniformemente al recorrer todos los primos grandes,

    M(p) ∼ p C(p)/(2h log p).

En particular hay incondicionalmente, para cada a fijo, primos arbitrariamente lejanos con bloques enteros positivos que toleran p^(3/2−a−ε) borrados arbitrarios para cualquier ε>0. Por ejemplo a=7/8 da longitud p^(7/8) y permite p^(5/8−ε) borrados. La garantía de 249 para borrar TODOS los nuevos primos alcanzaba incondicionalmente en una subsucesión longitud 0.41p^(3/4).

**Variación del conteo.** Para y cercano a x, la cota de 235 por sumación parcial da C(y)=O_ε(x^(Θ+ε)) y |C'(y)|=O_ε(x^(Θ−1+ε)) entre primos. Para la derivada integrar −u k'(u) contra dθ(xu) y dividir por x. El principal desaparece pues k(1)=0 e ∫₀¹k=0. La continuidad al entrar un primo da la misma cota de incrementos integrados a través de los nodos. Cada primo nuevo r≤y aporta a C(y) una cantidad entre cero y (2+o(1))h log p/p por el peso k(r/y), uniformemente en el bloque.

**Techo para el número de borrados.** Es siempre ≤N≤h+1. Cuando Θ<2a−1, en la primera mitad del bloque hay ≫h/log p primos por 238; cada uno aporta a C(p+h) al menos c h log p/p con c>0 absoluto. Borrar más de O_ε(p^(1+Θ+ε−a)/log p)+1 de ellos basta para hacer C(p+h)≤0 (si ya falla no se requiere ninguno). Para ε suficientemente pequeño hay suficientes candidatos. Esto da el techo anunciado incluyendo la frontera por el límite trivial.

**Piso subsecuencial.** Si Θ>1/2, fijar d<Θ próximo a Θ y ε pequeño con d>Θ−1+a+ε y d>1/2. Por 249 hay x arbitrariamente grandes con C(x)≥x^d. Pasar al siguiente primo p, a distancia O(x^(5/8)) por 238, y recorrer hasta p+h cuesta en conjunto O(x^(a+Θ−1+ε))=o(x^d). Persiste por tanto C(y)≥x^d/2. La cota individual anterior permite borrar floor(p^(min(a,1+d−a)−ε)) primos cualesquiera, y 238 garantiza que hay tantos. Tomar d↑Θ y ε↓0.

**Por qué el coste individual da la constante bajo RH.** De 247 se obtiene C(x)/√x=4/15−Σ K(ρ)exp(i Imρ log x)+o(1), serie absolutamente convergente y por tanto uniformemente continua como función del logaritmo en su parte oscilatoria. Esto implica C(p+v)=C(p)+o(√p) uniformemente para 0≤v≤h, con C(p)≥0.17√p para p grande. Poner m₀=p C(p)/(2h log p). Para cualquier 0<η<1, borrar hasta (1−η)m₀ nodos conserva todo el bloque por el techo individual. Para el recíproco fijar 0<τ<1 con (1+η)(1−τ)>1. Por 238 en (p,p+τh] hay ≫_τ h/log p primos, mucho más que m₀ ya que a>3/4. Cada uno contribuye en p+h al menos (2−o(1))(1−τ)h log p/p. Borrar ceil((1+η)m₀) de esos primos vuelve negativo ese extremo. Como η es arbitrario y m₀→∞, resulta el equivalente y el piso cuando Θ=1/2.

**Consecuencia para el cierre.** Para una sola elección fija de a>3/4, bastaría establecer M(p)≤p^(3/2−a+o(1)) en todos los primos grandes. Tanto a como 1+Θ−a serían estrictamente mayores que 3/2−a si Θ>1/2. Esta cota superior sigue abierta. El resultado incondicional sobre bloques sí conserva los primos auténticos fuera de los borrados y no cubre todos los puntos de partida.

**Evaluación exacta sin buscar entre subconjuntos.** Para p suficientemente grande, quitar los primeros m primos tras p minimiza el conteo simultáneamente en TODOS los puntos y del bloque entre todas las elecciones de hasta m. En efecto, para p<r≤y la derivada respecto de r del peso (log r)k(r/y), multiplicada por y, es k(z)/z+(log r)k'(z), z=r/y. En este tramo z→1 uniformemente, k'(1)=−2 y el término es negativo. Los r aún superiores a y aportan cero. La lista de contribuciones en orden de primo es por tanto no creciente y no negativa. El conteo mínimo se obtiene con un hueco inicial artificial de longitud m en número de primos, seguido de todos los primos restantes sin cambios. Para probar su signo en todo el bloque sólo hay que evaluar los dos extremos y los primos conservados: el argumento de concavidad de y²C(y) de 247 vale para cualquier lista fija. Esto convierte la obligación de acotar M por arriba en la búsqueda de un solo punto que falle después de retirar un prefijo determinado.
