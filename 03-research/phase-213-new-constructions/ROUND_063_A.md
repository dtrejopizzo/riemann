# Un único promedio para las bandas de toda anchura logarítmica fija

En 062 cada B>2 exigía escoger un orden de diferencias h>B−2. Aquí se fija una única transformación independiente de B. En compensación, el extremo superior de la banda ya no es un múltiplo fijo de Q_p: se incluye una cola en q. No se intercambia un límite h→∞ con la estimación de 062.

**Construcción e inversión.** Fijar 0<a<1, por ejemplo a=1/2. En el disco unidad tomar la rama real positiva sobre (0,1) y escribir

    C(z)=exp(−(1−z)^(−a))=Σ c_j z^j,
    1/C(z)=Σ d_j z^j,      H(x)=Σ_{j≥0} c_j 4^(−j) S(4^j x).

Aquí S es la suma de escalas de 060. La parte real de (1−z)^(−a) es ≥cos(aπ/2)|1−z|^(−a). Así C y sus derivadas se prolongan por cero en z=1 con todos los órdenes nulos; en el resto del círculo son suaves. Por integración por partes en el círculo c_j=O_N((1+j)^(−N)) para todo N. Los d_j son no negativos por expansión de la exponencial de una serie de coeficientes positivos. La cota de Cauchy en radio 1−j^(−1/(1+a)) da d_j≤exp(O(j^(a/(1+a)))).

El signo global equivale a H(j⁴)≤C'√x eventualmente para x=j⁴. Para justificar la inversión se usa la cota clásica incondicional ψ(z)−z=O(z exp(−c√log z)). Por sumación parcial con V de soporte compacto y 060 se obtiene Q(x)=O(x exp(−c'√log x)). Para S partir k≤x^(1/8), donde x/k⁴≥√x, y usar Q(z)=O(z) en el resto. Vale la misma cota para S, con otra constante. Como a/(1+a)<1/2, para cada x>0 la doble suma que resulta de insertar H en Σ_j d_j 4^(−j)H(4^j x) converge absolutamente: los d_j se absorben en exp(−c_x√(i+j)) de S(4^(i+j)x)/4^(i+j) y los c_i son sumables. Por convolución de coeficientes se recupera S(x) exactamente.

Bajo el signo |S(x)|≪√x, luego |H(x)|≪√x. A la inversa, las dos primeras derivadas logarítmicas de H son O(x) como en 060, por Σ|c_j|<∞ y convergencia local uniforme. Por interpolación se extiende la cota superior en las cuartas potencias a toda la cola. En la inversión los coeficientes d_j son positivos y Σd_j 2^(−j)=1/C(1/2)<∞. Por ello H(x)≤C'√x implica la misma cota para S, y vale 060. No se necesita una fórmula de Mellin global para H.

**El perfil en las pendientes.** En cada pendiente se sustituye G(Z) de 061 por J(Z)=Σ_j c_j 4^(−j)G(2^j Z). Se justifica incluso el desarrollo por pendientes a x fijo: la suma de módulos antes de agrupar a escala z es O(z(1+log z)^C) para z grande por soporte, |β|≤τ, las cotas elementales de sumas de divisores y Σk⁻⁴ del promedio en cuartas escalas. Los c_j absorben cualquier potencia de j. En la máscara de cada pendiente los términos con rad(n)|r se pueden reordenar también: para cada j son O(2^j T) enteros y G es acotada.

J y sus derivadas logarítmicas decrecen rápidamente en infinito. En cero, para cada N satisfacen O_N(Z²(1+|log Z|)^(−N)). En efecto G y sus derivadas se anulan para argumentos suficientemente pequeños; si Z<1 se empieza en j≥log₂(1/Z)−O(1) y se suman los pesos 4^(−j)|c_j|. Para Re s<2, su Mellin en la convención de 061 es C(2^(s−2)) por la de G, justificando el intercambio primero por convergencia absoluta. Por dominación al aproximarse s a 2 desde la izquierda y por la planitud de C se obtiene

    ∫₀^∞ J(z) z⁻³ (log z)^n dz = 0     para todo entero n≥0.

El perfil es no nulo por la misma identidad en la franja abierta. No tiene por qué anularse debajo de un umbral fijo; la ausencia de ese umbral permite un cero de todos los órdenes en el borde de convergencia.

**Banda y cota.** Para cada B>2 fijo tomar L=√x, R=L(log L)^B, P=L/√R, P≤p≤2P, Q_p=L²/p³ y todos los primos

    √R ≤ q ≤ Q_p exp((log L)^(1/4)).

La suma firmada en H sobre las cuatro pendientes de cada producto pq en esa banda es o_B(L). En particular la misma H sirve para todo B fijo. El enunciado no es uniforme si B varía con x.

En la expansión de la máscara para T=L/√(pq), los primeros términos son J(T)−J(T/p). Como p<q, los demás tienen módulo total O((T/q)²+(T/p²)²), por |J(z)|≤Cz² y suma de dos series geométricas sobre potencias de p y q. Sumando incluso sobre enteros en todo el rango, el primer error cuesta O(L²/R) usando Σ_{P≤p≤2P}1/p=O(1) y Σ_{q≥√R}q⁻³=O(1/R). El segundo cuesta O(L² P⁻⁴ log L), una potencia fija de log L. Ambos son o(L). Se tiene T≥L^(1/2−o(1)) y el número de pares es L^(1+o(1)), de modo que J(T) da o(L).

Para el término con T/p usar el cambio z=√(Q_p/q) de 062. El peso en q tiene variación acotada independientemente de p por las cotas de J y su derivada. El error del PNT cuantitativo en el extremo superior es ≪ Q_p exp((log L)^(1/4)−c√log L), insignificante tras sumar. Los extremos en z son exp(−(log L)^(1/4)/2) y una cantidad comparable a (log L)^(B/2). Expandir 1/(log Q_p−2log z) a cualquier orden fijo h, con log q comparable a log L en todo el intervalo. Se pueden completar los momentos hasta cero y hasta infinito a coste O_{h,N,B}(log^(−N)L) para cualquier N: en el extremo inferior integrar z⁻¹(1+|log z|)^(−M) y en el superior usar el decrecimiento rápido de J. Todos los momentos completados valen cero. El coste agregado del término principal así tratado es O_{h,B}(R/log^(h+2)L), como en 062. Tomar h>B−2 en la **estimación**; el promedio H permanece fijo.

**Alcance.** Se usa el argumento de inversión unilateral de 062 con un inverso positivo de infinitas dilataciones; el error clásico del PNT, ya usado en el corpus (fase 188, L2_BUILD_009), justifica la inversión. Este resultado controla una banda firmada para cada potencia fija del logaritmo con el mismo criterio. El saldo del complemento sigue abierto.
