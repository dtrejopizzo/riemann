# Detección local con primos simples después de ajustar una recta

Sea t=log X y 0<h=h(t)≤1 con log(1/h)=o(log t); se incluye h constante. Sea I=[X,Xexp(h)]. Formar únicamente con primos del intervalo

    D(X,h)=inf_(A,C reales) X^(−2)∫_I [Σ_(X<p≤x) log p − A − C(x−X)]² dx.

Entonces log(1+D(X,h))/log X→2B para B de 229. El conteo anterior a X y la pendiente media esperada pueden desconocerse. Por ejemplo vale para h=exp(−√log log X), que tiende a cero. Esto no llega a intervalos de longitud X^(1−ε). Un techo X^o(1) en una subsucesión de estos ajustes locales bastaría para el signo.

**Control cuantitativo del filtro de 230.** Fijar ρ₀=β₀+iγ₀ con β₀>1/2 y σ intermedio. Por Ingham la cola de longitudes del filtro positivo para Re ρ≥σ, |γ|>G, cuesta O(G^(−κ)) con algún κ>0 fijo: por diádicos puede usarse cualquier κ menor que 1−3(1−σ)/(2−σ). Elegir G=max(G₀,(C/h)^(1/κ)) con constantes tales que la cola quepa en h/3 y G>2|γ₀|+2. Entonces G=t^o(1). Reservar en la lista finita de anulaciones también los dos exponentes −ρ₀ y 1−ρ₀. Si M es la longitud de la lista de exponentes distintos no nulos, M=O(G log(2G)+1)=t^o(1). Para todos usar el mismo paso

    l=h/[10(M+1)(G+|ρ₀|+3)].

Así |w l|≤1/2 y |exp(wl)−1|≥c|w|l. La distancia de todos los blancos distintos de cero al origen está acotada inferiormente por una constante que depende de ρ₀, por discreción y las dos adiciones fijas. Los factores finitos de 230 tienen variación ≤C/l y la convolución tiene variación ≤(C/l)^M=exp(o(t)); la suma de sus longitudes es menor que h/3. El producto positivo de cola conserva variación uno. El último factor es una función suave de masa uno reescalada al intervalo (0,h/3). Sus normas hasta dos derivadas cuestan O(h^(−3)), absorbidas en exp(o(t)). El filtro final f_t tiene masa uno, soporte en [0,h], norma L² y normas L¹ de las dos primeras derivadas ≤exp(o(t)). En particular su transformada contra exp(wv) para |Re w|≤1 es O(exp(o(t))/(1+|Im w|²)), uniformemente en w, por partes.

**Lo que se puede retirar del conteo.** Repetir la fórmula explícita de 230 con ese filtro. El error de todos los ceros con β<σ es O(exp(−(β₀−σ)t+o(t))) por el conteo unitario y las dos derivadas. Los términos triviales se controlan igual que en 230. El residuo central sigue siendo −mult(ρ₀)/ρ₀. Al usar masa uno y las anulaciones adicionales, el integral de f_t(v)exp(−ρ₀(t+v)) contra cualquier recta A+C exp(t+v) es exactamente cero, sean cuales sean A,C, incluso si dependen de X. Por Cauchy–Schwarz se obtiene para toda recta, con la misma pérdida exp(o(t)),

    X^(−2)∫_I |ψ(x)−A−Cx|² dx ≥ exp((2β₀−1)t−o(t)).

Aquí se ha usado sólo que dx=x dv y que x/X∈[1,e]. Pasar a θ cambia la norma (raíz del lado izquierdo) en X^o(1) como máximo, pues ψ−θ=O(√X log² X) en I. Para cada β₀>1/2 esa pérdida es despreciable. Restar θ(X) se absorbe en el intercepto. Para el techo tomar la recta que corresponde a restar x de θ(x), usar de nuevo la cota de las potencias y mayorar por una constante por la integral de 229 en una banda mayor. Al aproximar 1/2+B por ceros derechos se obtiene el límite; si B=0 basta el techo y la no negatividad de log(1+D).

**Evaluación en un intervalo finito.** Enumerar los primos interiores y los dos bordes en orden creciente. Entre dos bordes sucesivos a,b el conteo ponderado local vale una constante S. La contribución exacta al objetivo antes de dividir por X² es

    (b−a)[S−A−C((a+b)/2−X)]² + C²(b−a)³/12.

Se suman estas expresiones y se minimiza una cuadrática de dos variables, con matriz definida positiva porque I tiene longitud positiva. No requiere un modelo para el nivel o la pendiente ni primos por debajo de X. La cota para esta suma minimizada no se ha demostrado en ninguna sucesión ilimitada.

**Alcance.** 230 daba soporte arbitrariamente corto fijado de antemano. Aquí el coste de los filtros está cuantificado y permite contraerlo con X. Las dos anulaciones adicionales convierten el criterio en una estimación de irregularidad interior alrededor de la mejor recta local. No se afirma prioridad bibliográfica ni se ha obtenido positividad global.
