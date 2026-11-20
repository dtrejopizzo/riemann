# Banda de semiprimos con anchura superlogarítmica

Afinación cuantitativa de 063, con el mismo promedio. Fijar 0<a<1, b=a/(1+a), 0<κ<b. Con L=√x, h=(log L)^κ, R=L exp(h), P=L/√R, Q=L²/p³, tomar P≤p≤2P y todos los primos √R≤q≤Q L^(1/4). La contribución firmada de estas pendientes a H es o(L). R parametriza la resonancia, no acota el producto pq. El extremo superior en q también cambia respecto a 063.

En el círculo, C(exp(it)) admite cerca de cada t real pequeño no nulo un disco complejo de radio ε|t| en el cual su módulo es ≤exp(−c|t|^(−a)): escoger ε de modo que a veces el valor absoluto del argumento de 1−exp(it') sea estrictamente menor que π/2 con margen uniforme. Cauchy y optimización en |t| acotan su derivada de orden n por A^(n+1)(n!)^(1+1/a), también en el resto del círculo por analiticidad. Integración por partes n veces y elección n≈δ j^b dan |c_j|≤A exp(−c j^b). En 063 la suma para J(z) empieza en j≥log₂(1/z)−O(1); así J y su primera derivada logarítmica son O(z² exp(−c|log z|^b)) en cero y rápidamente decrecientes en infinito.

En la fórmula de 060 para r=pq, T=L/√(pq), separar J(T)−J(T/p). El resto cuesta O((T/q)²+(T/p²)²) por |J(v)|≪v² y dos series geométricas. Aun sumando sobre enteros, el coste total es O(L exp(−h)+exp(2h)log L), usando Σ_{q≥√R}q^(−3)≪1/R y Σ_{p≥P}p^(−5)≪P^(−4). T≥p/L^(1/8) y el número de pares es polinómico, luego J(T) aporta o(L).

Para el término J(√(Q/q)), en cada intervalo diádico de q≈U la norma suprema más variación del peso es O(min(1,Q/U)). Sumación parcial y PNT cuantitativo permiten reemplazar la suma prima por la integral con densidad 1/log q con error O(Q log L exp(−c√log L)) por p. Es esencial usar el peso en cada intervalo.

Escribir 1/log q=∫₀^(1/4) q^(−s)ds+q^(−1/4)/log q. El resto aporta O(Q R^(−1/8)) por integrabilidad de |J(z)|z^(−3). Para el primer término poner z=√(Q/q); completar la integral en z da 2Q∫₀^(1/4) Q^(−s) M_J(2−2s)ds en la convención de 063. La cola z<L^(−1/8) cuesta O(Q exp(−c(log L)^b)), por la cota en cero y z^(2s)≤1. La cola z>√(Q/√R) cuesta O_N(Q exp(−Nh/2)) para cualquier N fijo por decaimiento rápido. En la integral completa M_G es acotada en [3/2,2] y C(2^(−2s))≤exp(−c s^(−a)); minimizar s log Q+c s^(−a) da O(Q exp(−c'(log Q)^b)). Al sumar en p se tiene ΣQ≪L exp(h) y log Q≈log L. Todas las cotas son o(L) tomando N>2. Las cuatro pendientes ordenadas por par sólo multiplican el coste por una constante.

Se controla la suma firmada de filas completas en q. La estimación no decide el complemento ni amplía T.
