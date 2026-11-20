# Una banda de frecuencia de ancho uno detecta el ángulo extremo sin conocerlo

Para A_N de 210 y B_N(t)=∫₃ᴺ A_N(u)u^(−5/2+it)du de 214, definir

    J_N = (∫_[√N,√N+1] |B_N(t)|²dt)^(1/2).

Entonces lim log(1+J_N)/√N = Θ = max_ρ arctan(|Re ρ−1/2|/|Im ρ|). Si Θ=0 se tiene incluso J_N→0 por 210 y Plancherel. Si Θ>0, para N suficientemente grande hay cotas bilaterales

    c exp(Θ√N)/√N ≤ J_N ≤ C exp(Θ√N)/√N.

Las constantes pueden depender de los ceros extremos. En particular basta encontrar una subsucesión no acotada con log(1+J_N)=o(√N). El ancho y el centro de la banda son explícitos e independientes de la altura de cualquier contraejemplo. 214 sólo localizaba la tasa exponencial en N: su techo de raíz N-ésima uno en esta banda es compatible con el presente criterio.

**Por qué la suma espectral no se cancela en toda la banda.** En la notación de 214 tomar t positivo, σ=−3/2. Si Θ>0, sólo un conjunto finito de w tiene arg w=−Θ, porque |arg w|→0 en altura. El resto tiene arg w≥−Θ+η para alguna η>0. Por convergencia absoluta en σ,

    exp(−Θt) Z(σ+it) = Σ_j d_j exp(it log r_j) + O(exp(−ηt)),

donde los r_j son los módulos distintos de los w extremos y d_j=m_j r_j^σ exp(−iσΘ) incorpora su multiplicidad. Ninguno se anula. La matriz de Gram en [0,1] de las exponenciales con frecuencias log r_j es definida positiva: una combinación nula en el intervalo tiene todas sus derivadas en cero nulas y Vandermonde da coeficientes nulos. Tras trasladar el intervalo a [T,T+1] los coeficientes adquieren sólo fases. Por tanto la norma L² del polinomio trigonométrico allí está entre dos constantes positivas independientes de T. La diferencia exponencial anterior, de norma o(1), conserva el piso. Resulta ||Z|| sobre ese intervalo comparable a exp(ΘT).

**Normalización y transferencia.** Para t=√N+d con 0≤d≤1 la fórmula beta de 214 da uniformemente

    |K_N(σ+it)|=(1+o(1))√(π/N) exp(−1/4).

En la expansión uniforme de Stirling usada allí se tiene y=t/(2N), log(1+y²)−2y arctan y=−y²+O(y⁴), Ny²→1/4 y Ny⁴→0. La constante se obtiene de K_N(0)=4^N Γ(N)^2/(2Γ(2N)). Por la comparación L² global de 214, las normas de 2B_N y K_N Z en la banda difieren a lo sumo en O(1). Para Θ>0 el piso espectral tiende a infinito y domina ese error. Para Θ=0 basta usar ∫|B_N|²dt=2πE_N→0. Se obtienen todas las afirmaciones.

**La estimación aritmética exacta que falta.** Con W_N(u)=A_N(u)u^(−5/2), integrar primero en la frecuencia da la identidad real

    J_N²=∫₃ᴺ∫₃ᴺ W_N(u) W_N(v) cos((√N+1/2)log(u/v)) sinc(log(u/v)/2) du dv,

con sinc(x)=sin(x)/x y sinc(0)=1. La finitud de las sumas y del intervalo autoriza Fubini, y la parte imaginaria se anula por simetría. El signo equivaldría a un techo exp(o(√N)) para esta única cuadrática en una subsucesión. Acotar la expresión por valores absolutos pierde la oscilación de log(u/v); el argumento espectral no proporciona la estimación prima.

**Una sola muestra por orden cuadrado.** También se puede prescindir de la integración en frecuencia si se conserva un limsup. Sea D_k=B_(k²)(k), k≥2 entero. Entonces

    limsup_k log(1+|D_k|)/k=Θ.

La comparación de 214 es también puntual con error aditivo O(1), uniforme en N,t: las cotas sobre b_N+2·1_[3,N]A_N de su último apartado son integrables contra u^(−5/2)du (en cero Cu², en infinito Cu log(2u)). Bajo RH incluso D_k→0 por 209 y dominación para A_N usando 210. Si Θ>0, en el desarrollo espectral anterior P(k)=Σ d_j exp(ik log r_j) tiene media cuadrática entera estrictamente positiva. En efecto agrupar las frecuencias iguales módulo 2π: los d_j comparten fase y por tanto cada coeficiente agrupado es no nulo. El promedio en k de |P(k)|² tiende a la suma de los módulos cuadrados agrupados por la fórmula de la serie geométrica. Como P está acotado, existe un conjunto de enteros de densidad inferior positiva donde |P(k)|≥c>0. En él se tiene |D_k|≥c' exp(Θk)/k eventualmente, y la cota superior correspondiente vale en toda la cola. No se concluye un piso para cada k. Esto da una obligación alternativa: basta demostrar que la única muestra aritmética D_k tiene crecimiento subexponencial en k para TODOS los k grandes.
