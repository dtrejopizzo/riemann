# Un contramodelo multiplicativo conserva los signos y todos los ahorros polinómicos

Fijar una ventana cualquiera 0<a<log 4 y cualquier corte inicial P₀. Hay una función multiplicativa real f que coincide con μ en n≤P₀, tiene exactamente sus mismos signos y ceros en todos los enteros, y cumple los ahorros de toda potencia de la ronda 329 con sus propios coeficientes. Sin embargo, para la energía definida como en 325 reemplazando μ por f,

    limsup E_(m,f)[exp(−am)]^(1/(2m)) > 1.

Por tanto no se puede ascender desde todos los ahorros de orden fijo hasta el objetivo exponencial invocando únicamente multiplicatividad, patrón exacto de signos y ceros, o los datos de una tabla inicial arbitraria.

**Construcción.** Elegir 0<δ<min(1/4,exp(−a/2)−1/2). Para un P≥P₀ poner

    f(n)=μ(n) ∏_(p|n; p>P) (1−p^(−δ)).

En los primos la perturbación máxima es ≤P^(−δ) y su norma armónica es ≤Σ_(n>P)n^(−1−δ), ambas arbitrariamente pequeñas. Aun fuera de la tabla se mantienen el soporte y la paridad que determina cada signo. En todo bloque [Y,2Y] grande, Σ|f(n)|≫Y al escoger P suficientemente grande: la pérdida respecto a μ² está acotada por Σ_(p>P)p^(−δ)⌊2Y/p⌋, mientras hay asintóticamente Y/ζ(2) libres de cuadrados.

**El defecto que crece exponencialmente.** Para Re s>1 la serie de f es ζ(s)^(−1) por el producto de 1+p^(−δ)p^(−s)/(1−p^(−s)) sobre p>P. Extraer ζ(s+δ) del producto. En s=β=1−δ queda una corrección localmente holomorfa y no nula: los términos de primer grado se cancelan para p>P, los errores cuestan O(p^(−2Re s−δ)+p^(−2Re s−2δ)), y los factores pequeños ajustados son unidades en β. Como ζ(β) es finita y no nula, la serie continuada tiene un polo simple en β. Repetir la prueba de radio de Taylor de 326 para los centros 3/2+it en un intervalo alrededor de cero: la densidad de alturas allí es ≫exp(−am). Por tanto la tasa es al menos exp(−a/2)/(1/2+δ)>1, sin hipótesis sobre ζ. No se afirma que la serie de la verdadera μ tenga ese polo.

**Por qué sobreviven las estimaciones de intervalos.** Escribir f=μ*k, con k multiplicativa no negativa, k(p^e)=p^(−δ) para p>P y e≥1, y cero en potencias de los otros primos. El producto anterior da Σ k(d)/d^(1−δ/2)<∞. En los bloques centrales [Y,2Y] de 329, para cada a' fijo en (0,log 4], h=exp(−a'm)m^b y b fijo, tomar H=ceil(4hY). Allí H≥Y^0.22 para m grande. Tras abrir la convolución, para d≤Y^ν con ν>0 fijo suficientemente pequeño, la longitud H/d aún supera (Y/d)^(1/6+ε) con margen fijo. El máximo de una suma de μ sobre subintervalos de ((x−H)/d,x/d] tiene media en x∈[Y,2Y] acotada por O_A((H/d)(log Y)^(−A)), por el resultado escalar citado en 329 y la cota trivial en el conjunto excepcional. Las constantes son uniformes en esos d; el cambio de escala multiplica la longitud del conjunto excepcional por d. Sumar con k(d)/H cuesta O_A((log Y)^(−A)).

Para d>Y^ν usar módulos y Fubini: el promedio en x del número de múltiplos de d en (x−H,x] es ≤(H/Y)⌊2Y/d⌋≤2H/d. La cola normalizada cuesta O(Y^(−νδ/2)). Así el máximo normalizado para f tiene media L¹ con ahorro de toda potencia de log Y. Como |f|≤1, también su segundo momento tiene ese ahorro. La sumación parcial y las colas gamma de 329 pasan sin cambio, dando

    E_(m,f)[h]=Δ_(m,f)+O_(A,a',b,δ,P)(h binom(2m,m)m^(−A))

para cada A fijo. Para a'<log 4 la masa absoluta sigue siendo ≫ h4^m/m por el argumento de ocupación ponderado de 326 y Σ_[Y,2Y]|f(n)|≫Y; la diagonal cuesta O(m^(−1/2)). Por ende también E_(m,f)/P_(m,f) decrece más deprisa que cada potencia inversa fija. El insumo de intervalos es el mismo teorema escalar ya utilizado. [Fuente, §1.1](https://arxiv.org/html/2411.05770v1)

**Consecuencia para la ruta.** Esta obstrucción opera incluso si se preservan todos los productos de signos de pares. Para excluirla hay que usar información de la función exacta, por ejemplo que el factor de Euler es exactamente 1−p^(−s) en cada primo y no sólo una aproximación armónicamente pequeña a él. El contramodelo no impide que una estimación específica de esos factores cierre el signo.

**Tamaño del defecto en la identidad de inversión.** Para el contramodelo anterior sea D(n)=Σ_{d|n}f(d), β=1−δ. Para μ este observable es exactamente cero para n>1. Aquí D es multiplicativa, con D(p^k)=p^(−δ) para p>P y k≥1, y D(p^k)=0 para p≤P. Para cada β/2<σ<β resulta

    Σ_{n≤X}D(n) = C_P X^β/β + O_(P,δ,σ)(X^σ),   C_P>0.

En efecto, la serie de D es ζ(s+δ)U(s). Con x=p^(−s), y=p^(−δ), el factor de U es 1−yx para p≤P y 1+(y−y²)x²/(1−x) para p>P. Los coeficientes u de U son absolutamente sumables con peso n^(−σ) pues 2σ+δ>1. Convolucionar con n^(−δ) y usar Σ_{k≤v}k^(−δ)=v^β/β+O_δ(1) para v≥1. Tanto la suma parcial de |u| en el error como la cola al completar U(β) cuestan O(X^σ) después de incluir sus respectivos pesos. Así C_P=U(β). Los factores pequeños en β dan exactamente ∏_{p≤P}(1−1/p); el producto de los grandes tiende a uno por convergencia absoluta. En particular C_P es asintótico a e^(−γ)/log P para P→∞ a δ fijo por el producto de Mertens. La estimación en X es para P fijo.

Esta fórmula distingue el contramodelo por una suma elemental de divisores y mide cuánto lo oculta una tabla inicial larga. Para μ el defecto se anula idénticamente; queda pendiente una desigualdad que aproveche esa anulación en la energía de pares de 326.
