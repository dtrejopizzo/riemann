# Una banda de Möbius de razón tendiente a uno basta para detectar un cero exterior

Sea t=log X, 0<h=h(X)≤1 con log(1/h)=o(log t). Poner

    D(X,h)=max_(X≤u≤X exp(h)) |Σ_(X<n≤u) μ(n)|.

Entonces lim log(1+D(X,h)²/X)/log X=2Θ−1. Basta una subsucesión en la que D(X,h)≤X^(1/2+o(1)) para cerrar el signo. Por ejemplo se puede tomar h=exp(−√log log X). En 133 la banda de Mertens era [X,X^(1+δ)]; en 231 se alcanzó este rango de longitudes para primos. Para Möbius hay que aislar polos del recíproco, con sus multiplicidades y sin suponer cotas de 1/ζ' en sus ceros.

**Cota superior.** Si Θ<1, usar M(v)≪_θ v^θ para cada Θ<θ<1. Si Θ=1 basta el número de sumandos. En Θ=1/2 la expresión normalizada tiene límite cero. El argumento no afirma en ese caso un piso para D de tamaño √X en cada ventana.

**Filtro para el recíproco.** Fijar ρ₀ con β₀>1/2, de multiplicidad m, y elegir 1/2<σ₁<σ₂<β₀. Construir como en 230–231 una medida compleja de soporte en [0,2h/3], masa uno y momentos nulos en e^((ρ−ρ₀)v) para los demás ceros con Re ρ≥σ₁. Repetir el factor de cada cero tantas veces como su multiplicidad, lo cual da ceros del orden requerido en la transformada entera. La estimación de Ingham cuenta multiplicidades. Para |γ|>G usar los factores positivos de 230; una altura G≪(1+1/h)^C suficientemente grande deja suma de longitudes <h/3. Para la lista finita, de tamaño O(G log(2G)), usar los factores de paso corto de 231: el soporte cuesta ≤h/3 y la variación total es exp(o(t)), porque G=t^o(1). El objetivo queda normalizado a uno.

Convolucionar con una densidad suave Gevrey dos de masa uno en [0,h/3], usando una reescala de 274. Llamar f a la densidad obtenida y F(s)=∫f(v)e^((s−ρ₀)v)dv. Usar finalmente

    Φ(s)=(s−ρ₀)^(m−1) F(s).

Esto reduce a simple el polo objetivo, con residuo fijo m!/ζ^(m)(ρ₀) en Φ/ζ. Multiplicar por ese polinomio se realiza por derivadas de orden fijo de f con signo apropiado, sin ampliar el soporte. Así Φ es la transformada de Mellin de un peso suave W sobre [1,exp h]; ||W||∞+Var(W)≤exp(o(t)). En toda franja real fija alrededor de [σ₁,2] se tiene

    |Φ(s)| ≤ exp(o(t)) (1+|s|)^(m−1) exp(−c√(h |Im s|)).

Aquí se separa el factor de convolución Gevrey al estimar la transformada; multiplicarlo por e^((Re s−ρ₀)v) sólo cambia las constantes en una franja fija. Las pérdidas por las derivadas fijas al reescalar son potencias de 1/h=t^o(1).

**Paso de contorno.** Para Σ μ(n)W(n/X) partir de la recta 2 con integrando X^s Φ(s)/ζ(s). Desplazar a un camino por tramos en la franja [σ₁,σ₂]. En cada banda horizontal de altura comparable con uno hay O(log(2+|Im s|)) ordenadas de ceros en su vecindad de tamaño fijo. Se pueden escoger bordes horizontales dentro de intervalos de longitud 1/4 en torno a alturas enteras, apartados de todas esas ordenadas en ≫1/log(2+|Im s|). Entre dos bordes consecutivos elegir la coordenada vertical en [σ₁,σ₂] apartada en la misma escala de las partes reales de todos los ceros próximos. Unir los tramos por los bordes elegidos. En altura acotada se escogen bordes sin ceros por discreción.

Sobre esos tramos y los cierres horizontales hasta 2, |1/ζ(s)|≤exp(C log²(3+|Im s|)). En efecto, la fórmula local de ζ'/ζ como suma de 1/(s−ρ) sobre |γ−Im s|≤1 con error O(log(3+|Im s|)), integrada en parte real desde 2, da el logaritmo del módulo como suma de log-distancias con error O(log(3+|Im s|)). Se puede pasar al límite desde alturas vecinas si la horizontal de integración pasa por un cero. En los puntos del camino todas las distancias son ≫1/log(3+|Im s|). Esta estimación sólo se utiliza para alturas grandes.

El coste de integrarla contra el decaimiento Gevrey es exp(o(t)) uniformemente en el h permitido. Para verlo poner b=log(3+1/h) y dividir las alturas en bloques diádicos; con z=h|Im s| la parte log² es O(b²+log²(3+z)), y exp(−c√z) domina todos los factores en z. El coste restante es exp(O(b²)) por una potencia de 1/h, admisible. Los cierres horizontales se anulan al infinito para cada X. Todos los polos cruzados salvo el objetivo son removibles por el filtro; no hay que sumar sus residuos individuales. Resulta

    Σ μ(n)W(n/X) = X^ρ₀ m!/ζ^(m)(ρ₀) + O(X^σ₂ exp(o(t))).

Por sumación parcial en el soporte su módulo es ≤D(X,h) exp(o(t)). Se deduce liminf log(1+D²/X)/log X≥2β₀−1. Tomar el supremo sobre los ceros exteriores termina la prueba.

**Obligación aritmética.** El criterio sólo exige controlar las sumas parciales ordinarias dentro de una banda y no requiere el valor de M(X), la matriz de Gram ni un cruce auxiliar. No demuestra la existencia de las bandas con techo de raíz. El paso nuevo frente a 231 es el control del recíproco a lo largo del camino y la normalización del polo múltiple con coste uniforme en la anchura.
