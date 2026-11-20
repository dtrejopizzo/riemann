# Una sola cima binomial reproduce la octava y amortigua los átomos pequeños

Para x entero ≥2 tomar n=2x y g(y)=y^(−1/2)(1−cos(2π log(y)/log 2)) en [1,2], extendida por cero. Hay una combinación de filas con este mismo extremo superior, coeficientes de suma cero y variación acotada independientemente de x cuya respuesta R(m) coincide con g(m/x) en todos los enteros x<m≤2x. En la parte inferior satisface

    |R(m)| ≪ (m/x)² dist((2x+1)/m, ℤ),     2≤m≤x.

**Construcción.** Definir A(t)=g((n+1−t)/x) en toda la recta con la extensión indicada. Su soporte es [1,x+1] y ambos extremos valen cero. Para 1≤k≤x tomar a_k=A(k)−A(k+1); la suma telescopa a cero y Σ|a_k|≤∫|g'|. Poner R(m)=Σ a_k c_(n,k)(m). Contando múltiplos en (n−k,n] y restando ⌊k/m⌋ se obtiene, para todo m≥2,

    R(m)=Σ_(j∈ℤ) [A(n+1−jm)−A(jm)].

En efecto, el primer término suma los coeficientes con k≥n+1−jm para cada múltiplo positivo jm≤n; los múltiplos fuera de ese rango dan cero en la fórmula extendida. El segundo usa las colas con k≥jm. Para m>x, m≤2x, sólo sobrevive el primer término con j=1, incluido el extremo m=x+1 donde A(m)=0.

**Error en los átomos pequeños.** Con la transformada de Fourier de fase −2πiξt, |Â(ξ)|≪x min(1,|xξ|^(−3)). En efecto g es C¹, y su derivada segunda por tramos tiene variación finita incluyendo los saltos de borde. Periodizar A con periodo m y evaluar la diferencia entre las fases n+1 y cero. El término constante desaparece; el término de frecuencia l≠0 tiene tamaño a lo sumo m^(−1)|Â(l/m)|·2π|l|dist((n+1)/m,ℤ). Sumar Σ|l|^(−2) prueba la estimación. En particular todos los divisores de 2x+1 tienen respuesta cero. Usando Σ_(m≤y)Λ(m)≪y, el error absoluto sobre todas las potencias primas hasta y≤x es O(y³/x²). Hasta y=x^(5/6) ya cuesta a lo sumo O(√x).

**Dónde persiste un error grande.** Si 2x/3<m<x la respuesta es exactamente g(2m/x)−g((2x+1−m)/x). En r=m/x=1−δ el límite para x→∞ es g(2−2δ)−g(1+δ). Si b=2π/log 2, este último vale (b²/2)(1/√2−1)δ²+O(δ³). Escoger un intervalo fijo de δ positivos suficientemente pequeños, separado de cero. En ese intervalo R(p)≤−c<0 uniformemente para x grande; por el teorema de los números primos Σ log(p)|R(p)| allí es ≫x. La aproximación tiene pues un error absoluto de orden lineal en una franja concreta de primos. Para el objetivo de 262 queda por compensar el error de las escalas intermedias y calibrar la masa continua. La construcción impone los valores de la octava a un extremo determinista y funciona en todos sus enteros; la ley de traslaciones de 266 no se utiliza.
