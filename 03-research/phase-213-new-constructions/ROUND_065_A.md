# Suma sobre filas con el corte pq ≥ L

Usamos el representante H y el perfil J de 063. Es una extensión de 064 por suma en el primo menor. Sean h=(log L)^κ con el mismo 0<κ<a/(1+a), Y=√L, P₀=Y exp(−h/2), Q=L²/p³. Para cada primo p≥P₀ incluir todos los primos q>p con L/p≤q≤QL^(1/4). Escribir F_p para la suma de sus contribuciones de pendiente (una por pareja, las cuatro ordenaciones tienen igual valor). Entonces Σ_p |F_p|=O(L/log L). Se permiten subconjuntos arbitrarios de filas enteras. Los pares de una fila conservan sus signos.

**Para P₀≤p≤Y.** La suma de Q es O(L exp(h)) incluso sobre enteros. En la prueba de 064 siguen valiendo uniformemente las cotas por PNT, el integral de Mellin completo y la cola z<L^(−1/8), porque log Q y log q son comparables a log L. El resto de la densidad cuesta O(QY^(−1/4)). En conjunto estos términos son o(L/log L). El extremo superior en z ahora es Y/p≥1. La cola de la integral desde ese extremo cuesta O_N(Q(p/Y)^N), por decaimiento rápido. Para N=4, sumar esta cota da O(Σ_{p≤Y} p)=O(L/log L) por Chebyshev. La posible igualdad q=p en el corte p=Y afecta a lo sumo una evaluación acotada del perfil principal.

La máscara exacta se descompone como en 064. El resto de valuaciones ligado a q cuesta en conjunto
    Σ_{p≤Y} (L²/p) Σ_{q≥L/p} q^(−3) ≪ Σ_{p≤Y} p ≪ L/log L.
En la suma interior basta usar enteros. El ligado a p² cuesta O(L² P₀^(−4) log L)=O(exp(2h) log L). El término J(T) tiene T≥p L^(−1/8) y contribución despreciable por decaimiento rápido y cantidad polinómica de pares.

**Para p>Y.** La fila sólo puede existir si p<L^(9/16). Aquí Q≤p. El término principal puede incluso sumarse en módulo sobre q. En cada intervalo U≤q<2U con U=2^i p, la cota en cero de 064 da O(Q exp(−c(log(U/Q))^b)) para la suma, b=a/(1+a), también contando enteros. Sumar en i da O(Q), pues U/Q≥2^i. Chebyshev en bloques diádicos da Σ_{p>Y} Q≪L²/(Y² log Y). El resto ligado a q cuesta O(L² Σ_{p>Y}p^(−3)), del mismo orden. El ligado a p² y J(T) ya cumplen las estimaciones anteriores, extendiendo la suma de p^(−5) a infinito. Esto termina la cota.

La contribución cercana a p=Y se paga con la cantidad de primos, sin exigir que el extremo z=Y/p crezca. El argumento cubre desde P₀ hasta el último primo que admite la fila y sustituye la frontera fija inferior en q por pq≥L. Para p mucho menor que P₀, el coste prefactor L²/P₀² del argumento de Mellin ya no queda absorbido por el ahorro demostrado. También siguen fuera los q más allá del corte superior y las máscaras de más factores.
