# Hasta dónde se pueden retirar las pendientes sumando sus módulos

En 060 el promedio en cuartas escalas transformó cada pendiente de producto reducido r en una suma entera con una máscara de valuaciones. Escribir u*=2√B, el extremo superior del soporte de f, y

    G(Z)=Σ_{n≥1} f(n/Z),     T=L/√r.

G es cero para Z<1/u*, y es O_N(Z^(−N)) para Z grande por Poisson, suavidad de f e integral cero. La pendiente vale exactamente μ(r)Σ_{rad(h)|r}(−1)^Ω(h)G(T/h) para r libre de cuadrados.

**Pendientes sin primos que intervengan en la máscara.** Si todos los primos de r superan u*T, sólo contribuye h=1. Por tanto estas pendientes para r≤x^(1−ε) suman o(L) en módulos para cualquier ε fijo positivo menor que uno: T≥x^(ε/2) y hay a lo sumo O(x log x) pendientes ordenadas hasta x. En particular quedan cubiertas todas las pendientes de producto reducido primo en ese rango: los primos por debajo del umbral de 060 están ya controlados en módulo, y por encima p>u*L/√p para x grande.

**Dos primos cambian el comportamiento.** Para cada δ>0 fijo y R=L(log L)^(2+δ), hay dos subconjuntos de pendientes con producto de dos primos y r comparable a R. En uno, todos los totales de pendiente son positivos y su suma es ≫δ L(log L)^δ. En el otro son negativos y el módulo de su suma cumple la misma cota. Aquí los módulos se toman después de todas las cancelaciones internas de 060.

En efecto, G toma ambos signos. En Re s>1 su Mellin con convención Z^(−s)dZ/Z vale ζ(s)∫f(u)u^(s−1)du. La integral de la izquierda es entera por el soporte inferior y el decrecimiento rápido; la continuación a s=−2 da ∫Z G(Z)dZ=0 por el cero trivial ζ(−2)=0. G no es idénticamente cero: la inversión finita en cada Z recupera f(1/Z) de los G(Z/n), y f es no nula por el valor de V en el interior cerca de su extremo superior, donde en F sólo aparece w=1. Así existen intervalos fijos 0<z₁<z₂ donde G está separado de cero con cada signo.

Tomar primos p en un intervalo fijo de razón dos a escala L/√R, y para cada p todos los primos q tales que

    L²/(z₂² p³) ≤ q ≤ L²/(z₁² p³).

Entonces z₁≤T/p≤z₂ con r=pq, p<q, y r comparable a R. Uniformemente q>u*T porque q/T crece como (R/L)²; también p²>u*T y T→∞. Los únicos h que pueden contribuir son 1 y p. Cada pendiente tiene valor G(T)−G(T/p), de signo opuesto al del intervalo elegido y de módulo acotado inferiormente. Por PNT en los intervalos de razón fija hay ≫R/(log L)² pares distintos: p y q tienen escalas L/√R y R^(3/2)/L respectivamente. Podría tomarse una sola pendiente por par. El resultado prueba un límite para retirar todos esos productos por la suma de módulos de sus pendientes, no una afirmación de signo acerca de toda la banda de semiprimos.

**Alcance.** El exponente crítico para el método absoluto de 060 es 1/2 en x: controla todos los productos hasta L exp(−δ√log L), y falla ya en un rango de orden L(log L)^(2+δ). Persiste una brecha entre ambos umbrales. Los primos por sí solos no producen esta obstrucción. El argumento del momento negativo de una suma de dilataciones tiene antecedente en 045. Aquí se aplica al perfil centrado y a la máscara par de 060 para construir dos familias de semiprimos con signos opuestos.

**Extensión cuantitativa para la máscara inactiva.** Se puede llegar a r≤c₀x/(log x)^8 con c₀ fijo suficientemente pequeño. Detallamos la regularidad necesaria. En F(u)=Σ_{ij}ε(i)ε(j)V(i j u²/4), para u pequeño las cajas de 055 cumplen IJ comparable a u⁻² y su coordenada larga M es ≥c/u. Aplicar primero j₀ derivadas logarítmicas en u y luego n derivadas ordinarias en la coordenada larga. El coste en norma suprema es como máximo C^(j₀+n+1)(j₀! n!)² M^(−n): en coordenadas logarítmicas el argumento es una suma y se usa (j₀+n)!≤2^(j₀+n)j₀! n!, con Leibniz y las particiones de Gevrey de 055. La conversión a derivadas ordinarias en la coordenada larga se justifica con los coeficientes de factorial descendente de 047. Alternar en esa coordenada y optimizar n comparable a √M da, tras contar los términos y las cajas,

    |(u∂_u)^j₀ F(u)| ≤ C^(j₀+1)(j₀!)² exp(−c'/√u)     (0<u≤1).

Reducir c' absorbe los factores polinómicos en 1/u. Lejos de cero sólo interviene una cantidad acotada de sumandos. Multiplicar por log u−b₀ y convertir a derivadas ordinarias de orden j cuesta además u^(−j); su producto con exp(−c''/√u) se acota por C^(j+1)(j!)². Por tanto f extendida por cero es de Gevrey de orden cuatro. En Poisson se anula la frecuencia cero, y la optimización del orden de integración por partes da |G(T)|≤C T exp(−c T^(1/4)) para T≥1. Si r≤c₀x/(log x)^8 entonces T≥(log x)^4/√c₀. Elegir c₀ pequeño hace que el ahorro absorba las O(x log x) pendientes, con total o(L), siempre que cada primo de r sea mayor que u*T.
