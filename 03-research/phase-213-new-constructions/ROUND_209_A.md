# Perfil de cada cero verificado en una suma finita de primos sin centrar

Con H_u, c_N, M₁ y X_N de 208, definir ahora

    A_N(u)=Σ_{p≤X_N(u)} (log p)/√p · c_N(log p;u),

sólo sobre PRIMOS, sin restar un fondo. Para todo u≥3 fijo, b_N(u)=−2A_N(u)+o_u(1). El error tiende también a cero en cualquier sucesión u_N→u≥3 con u_N≥3. Por ello los criterios de crecimiento de 207–208 siguen válidos para A_N. Además, si 3<u<G−1, x es real fijo y u_N=u exp(x/√N), se obtiene

    lim A_N(u_N) = −m(u) exp(−x²),

donde m(u) es la multiplicidad del cero de ordenada positiva u, o cero si no existe. Para u=3,G−1 con tasa fija vale igualmente el límite −m(u). En particular en la primera ordenada positiva la suma converge a −1 por Z1. La suma cambia de corte y de peso con la tasa; se usa su normalización de 208 sin un factor adicional en N.

**Eliminar el error de truncación.** En la recta |H_u|<1 salvo en ±u. El arquimediano tiende a cero por convergencia dominada con |m(τ)|H_u(τ), y el polar por |H_u(i/2)|<1. En el contorno desplazado a i, |H_u(τ+i)| alcanza M₁(u) sólo en un conjunto finito por la fórmula de 208. Así ∫ |H_u(τ+i)|^N dτ = o(M₁(u)^(N−1)): dividir por esa potencia y aplicar convergencia dominada con |H_u(τ+i)|. En tasas convergentes vale lo mismo pues los cocientes convergen puntualmente a uno sólo en los máximos del límite, y los mayorantes tienen cola común O((1+τ²)⁻¹). Sustituir este prefactor en la cuenta de Chebyshev de 208: incluso en el mismo corte X_N, la suma absoluta de la cola para Λ o para primos solos es o(1).

**Control de Fourier en la recta.** Uniformemente para tasas en un compacto de [3,∞), ||c_N||∞+||c'_N||∞→0 y ||c_N||₁+||c'_N||₁=O(1). Para el supremo usar las integrales de H_u^N y |τ|H_u^N y dominación desde N≥2. Para L¹ usar, para g=H_u^N o g=τH_u^N,

    ||g||₂²≪N^(−1/2),    ||g'||₂²≪N^(1/2).

En coordenada τ/u, los dos máximos ±1 son cuadráticos no degenerados: H_u(u s)=1−[(1−s²)/(1+s²)]². A distancia y pequeña de un máximo se tiene H^N≤exp(−cNy²) y |(H^N)'|≪N|y| exp(−c(N−1)y²), con constantes uniformes en el compacto. Integrando los cuadrados se obtienen las potencias indicadas. Fuera de esas vecindades H≤q<1 y la función racional y sus derivadas permiten dejar dos potencias de H en las integrales para controlar infinito. Plancherel y Cauchy–Schwarz con peso 1+t²/N dan la cota L¹, pues ∫(1+t²/N)⁻¹dt=π√N.

**Cuadrados y potencias superiores.** Para exponentes ≥3 se tiene Σ_pΣ_{j≥3}(log p)p^(−j/2)<∞; su contribución tiende a cero. Para cuadrados, escribir θ(y)=Σ_{p≤y}log p. El integral continuo que aproxima Σ_p(log p)/p c_N(2log p) es ∫₁^∞ c_N(2log y)dy/y=∫₀^∞ c_N(2t)dt=H_u(0)^N/4=0. Integrando por partes contra θ(y)−y, la diferencia está acotada por un extremo O(|c_N(0)|) más

    ∫₀^∞ |θ(exp t)−exp t| exp(−t) [|c_N(2t)|+2|c'_N(2t)|]dt.

El extremo infinito se anula para cada N por el decaimiento de contorno. Por PNT el primer factor tiende a cero en t grande y es acotado en toda la semirrecta. Partir en un compacto fijo y su complemento: el compacto usa los supremos que tienden a cero y el resto las normas L¹ uniformes. El resultado es o(1) sin necesitar tasa de error en el PNT. Esto separa los cuadrados en la suma completa; la estimación anterior para la cola permite volver al corte finito.

**El perfil en tasas conocidas.** En toda tasa verificada del enunciado cada cero no crítico tiene |h_u|<1 por la geometría de 207. Los críticos también salvo en |γ|=u. Para una sucesión de tasas que tiende a u, todos esos términos tienden individualmente a cero al elevar a N: basta una cota estricta en una vecindad para cada cero, y en la cola un mayorante sumable O_u(1/(1+γ²)) para la potencia desde N≥1. Para el par crítico en ±u el valor es exactamente sech²(log(u_N/u)); su potencia N tiende a exp(−x²). Sumar las dos multiplicidades y usar la identidad con −2A_N. Esta recuperación local no prueba el signo para tasas de altura arbitraria.

**Antecedentes.** En 208 el error O(1) permitía estudiar crecimiento exponencial, sin distinguir un límite finito de cero ni retirar los cuadrados. POWER_LOW_TABLE_018 ya cancela términos continuos en otra fila. Aquí la cota L¹ simultánea en el peso y su derivada, el PNT y el corte de contorno al mismo X_N permiten leer una multiplicidad en los primos simples.
