# Los pares que comparten un divisor grande ya cumplen la cota de raíz

Con el núcleo de Gram G(d,e) de 281, para 1≤H≤V=x/U se tiene

    |lim_(L→∞) Σ_(d,e≤L; mcd(d,e)≥H) μ(d)μ(e)G(d,e)|
       ≪ (V²/H) log^C(2N)

con C absoluto. En particular, fijar H=V exp(−√log(2N)). Toda esa parte, incluida la diagonal, cuesta x^(1/2+o(1)) incondicionalmente. Los dos índices pueden ser arbitrariamente grandes por la cola de calibración de 281. La cota usa cancelación en esa cola.

**Una progresión de múltiplos en la variable de Möbius.** Fijar una muestra y y escribir B_h(L)=Σ_(h|d≤L) μ(d)K_y(d). Uniformemente en L y en h≥1,

    |B_h(L)| ≪ (V/h) log^C(2Nh).

En efecto, hasta M=max(4V,2x/Y) cada coeficiente está acotado por O(log²(2N)) por 281. Hay a lo sumo M/h múltiplos y M≪V log²(2N). Por encima de M la parte local desaparece y, como χ(Vu/d)=0 para 1≤u≤2, la fórmula de calibración es exactamente K_y(d)=(V/d)(α_y+β_y log(d/V)), con |α_y|+|β_y|≪log²(2N).

Si h no es libre de cuadrados, la suma es cero. En otro caso usar μ(hj)=μ(h)μ(j)1_((j,h)=1). Las sumas parciales de μ(j)1_((j,h)=1)/j y de la misma sucesión multiplicada por log j están acotadas, respectivamente, por O(log(2h)) y O(log²(2h)), independientemente del punto final. Para verlo, la sucesión restringida es la convolución de μ con la indicatriz de enteros cuyos factores primos dividen h. Las dos sumas parciales irrestrictas están uniformemente acotadas por su convergencia, recordada en 281. En la convolución, la suma de 1/r sobre esos enteros es ∏_(p|h)(1−1/p)^(−1)≤ζ(2)Σ_(r|rad h)1/r≪log(2h). Para el peso log r se multiplica por Σ_(p|h)log(p)/(p−1)≤log h. Esto prueba la estimación uniforme, aplicable también a diferencias de sumas parciales, y la convergencia al enviar L a infinito por convergencia dominada en r.

**Proyección por máximo común divisor.** En un corte finito el aporte de una sola muestra con mcd(d,e)=g vale exactamente Σ_(t≤L/g) μ(t) B_(gt)(L)² por inversión de divisores. Por tanto el módulo de la suma sobre g≥H cuesta a lo sumo

    V² Σ_(g≥H,t≥1) log^C(2Ngt)/(g²t²) ≪ (V²/H)log^C(2NH),

absorbiendo exponentes logarítmicos en C. La última estimación sigue por bloques diádicos en g/H y t. El mismo mayorante sumable, para x fijo, permite pasar al límite rectangular por convergencia dominada. Sumar sobre las O(log²N log log N) muestras sólo cambia C.

**Residuo.** Para H elegido arriba, los términos restantes tienen mcd(d,e)<H. Puesto que los dos índices con coeficiente no nulo son ≥V, las dos partes coprimas d/mcd(d,e) y e/mcd(d,e) superan exp(√log(2N)). La cota unilateral de 281 se necesita ya sólo para ese conjunto. La diagonal está completamente en la parte resuelta. El descarte de 050 se refería a una bilineal diferente y usaba la parte libre de cuadrados del producto. Aquí la proyección en múltiplos conserva las dos colas infinitas de calibración y controla su contribución conjunta con signo. Falta estimar los pares cuyo divisor común es menor que H.
