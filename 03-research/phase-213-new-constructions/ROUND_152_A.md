# Deriva de los cuadrados en la corrección impar

En 150–151 sea K(t) la inversa bilateral de B(1/2+s), con contorno inicial Re s>1/2. La contribución a E de las potencias p² tiene una deriva lineal de coeficiente −a/2>0. En particular retirar todos los exponentes mayores que uno como error acotado alteraría el criterio. Para el peso compacto de 107 los cuadrados aportaban una constante después de normalizar. Aquí el núcleo tiende a una constante en una semirrecta.

**Identidad aritmética.** Definir
    P(T)=Σ_p (log p)/√p K(T−log p).
El signo global equivale a la existencia de C tal que, eventualmente,

    P(T) ≥ −aT/2 − C.

Para verlo escribir ξ=Jζ, con J(z)=z(z−1)π^(−z/2)Γ(z/2)/2. Sobre Re z>1, separar Bξ'/ξ en BJ'/J y Bζ'/ζ. La serie de Dirichlet absolutamente convergente del segundo factor e inversión dan exactamente
    E(T)=A(T)−Σ_{p,k≥1} (log p)p^(−k/2) K(T−k log p),
donde A es la inversa de BJ'/J. Se puede invertir término a término por el decaimiento gamma. El polo de J'/J en z=1 queda cancelado por B(1)=0. Al mover a Re z=1/4 sólo se cruza z=1/2, dando A(T)=a(J'/J)(1/2)+O(exp(−T/4)). Para K mover a Re z=−1/2 da K(t)=a+O(exp(−t/2)) para t≥0, incluyendo el residuo en z=0. A la izquierda basta mover a Re s=2 para K(t)=O(exp(2t)). En particular K está acotado y es continuo. Todo esto es incondicional.

**Potencias.** La suma sobre k≥3 converge al valor constante aΣ_{p,k≥3}(log p)p^(−k/2) por convergencia dominada. Para k=2 introducir r(t)=K(t)−a·1_{t≥0}. Con Y=exp(T/2) la suma de cuadrados antes de su signo menos es
    a Σ_{p≤Y}(log p)/p + Σ_p (log p)/p r(2 log(Y/p)).
La primera suma vale a log Y+O(1) por el teorema de Mertens. La segunda está uniformemente acotada: por Chebyshev, cada banda e^j≤p<e^(j+1) aporta masa Σ(log p)/p=O(1), y |r| tiene decaimiento exponencial por ambos lados. Por tanto E(T)=−P(T)−aT/2+O(1). El promedio par de 150 está acotado para T≥0 por 151 y ε es positivo fijo, lo que prueba la equivalencia. La pendiente en el minorante de P es positiva porque a<0.

**Por qué falla la aproximación por densidad continua.** Sustituir (log p) por la medida du sobre (0,∞) en P produce exp(T/2)∫exp(−v/2)K(v)dv=exp(T/2)B(1)=0. Usar el intervalo [2,∞) sólo modifica O(1) por acotación de K. Por tanto esa sustitución pierde precisamente un término que debe crecer al menos linealmente en T. La necesidad de capturar este exceso en los primos simples es una obstrucción al argumento por densidad, no una prueba de que el minorante se cumpla.
