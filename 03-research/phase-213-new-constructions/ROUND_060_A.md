# Promediar escalas cuartas elimina la condición de libre de cuadrados en cada pendiente

En 059 el término integral de cada pendiente se anuló, pero quedaba un error al contar los enteros libres de cuadrados. Aquí se promedia la **identidad completa sin cortes** en escalas x/k⁴. La descomposición única como cuadrado por libre de cuadrados permite estimar conjuntamente las pendientes de producto reducido hasta

    R=L exp(−δ√log L),     L=√x,     δ>0 fijo.

Su coste es o(L), sumando incluso los módulos de los totales por pendiente. El cambio abandona los rangos individuales de 056 y usa un nuevo criterio equivalente al signo, no una mejora del conteo anterior para el propio peso truncado.

**Identidad exacta.** Usar V de 047, β=ε*ε de 056, b₀ de 059 y y=4x. Para cada x>0 definir Q(x) por la suma de μ(d)μ(m)β(w)V(dmw/y) multiplicada por [log(d/L)+log(m/L)]/2−b₀ sobre todos los índices positivos, sin cortes. Es finita y se anula para x suficientemente pequeño. Si B(x)=4A(x)−4A(2x)+A(4x) de 054, entonces

    Q(x)=B(x)−(log L+b₀) Σ_{j=1,2,4} c_j V(j/y),   (c₁,c₂,c₄)=(1,−4,4).

En efecto μ*β=α, μ*α tiene masas c_j, y (μ log)*1=−Λ por inversión de divisores. Por simetría basta desarrollar el logaritmo del primer índice. El término adicional está soportado en un compacto de x alejado de cero.

**Criterio.** Escribir S(x)=Σ_{k≥1}Q(x/k⁴), suma finita. El signo global equivale a S(j⁴)≤Cj² eventualmente. Si vale el signo, |B(x)|≪√x por 047 y por tanto |S(x)|≪√x usando Σk⁻²<∞. La suma de las correcciones compactas cuesta O(x^(1/4)), pues sólo entran k comparables a x^(1/4).

Para la vuelta unilateral, las dos primeras derivadas logarítmicas de B y B mismo son O(x) en toda la semirrecta positiva por Chebyshev, suavidad y soporte. La corrección compacta satisface las mismas cotas, y Σk⁻⁴ converge. Así se interpola S(exp r)exp(−r/2) con error O(1) entre las muestras de 4log j como en 047. En Re s>1 la Mellin con convención ∫S(x)x^(−s)dx/x es

    ζ(4s)[(2−2^s)² V̂(s)(ζ'/ζ)(s)+E(s)],

con E entera de la corrección compacta. Esto sigue de la serie de Λ por convergencia absoluta y del cambio x=k⁴u; V̂(s)=∫V(t)t^(s−1)dt. La expresión es regular en todo el eje real s>1/2, incluido s=1 por el cero doble. Si S(x)≤C√x eventualmente, Landau aplicado en log x a C√x−S(x) en una cola da holomorfía para Re s>1/2 como en 038. En 1/2<Re s<1 el factor ζ(4s) no se anula y (2−2^s) tampoco. Por 044–047 V̂(s) es el producto del factor del promedio P(s−1/2) con
     
    2b [1−cosh(h(s−1/2))/cosh(hb)]/[b²−(s−1/2)²],

donde b=3/2, h=log16 (integrar los exponenciales de 044). Ambos son no nulos en esta franja. Luego ningún polo de ζ'/ζ allí puede quedar oculto, y se concluye por Weil como en 038. Para una versión bilateral basta en cambio la inversión elemental Q(x)=Σ μ(k) S(x/k⁴) y la cota bilateral de 047–054.

**Qué ocurre en una pendiente.** Sea d=at, m=bt, (a,b)=1, r=ab. Para términos no nulos r es libre de cuadrados. Sea f(u)=(log u−b₀)Σ_w β(w)V(u²w/4), el perfil suave de 059, plano en cero, compacto por arriba y de integral cero. En la escala x/k⁴ aparece f(k²t/T) con T=L/√r. La contribución de la pendiente es exactamente

    μ(r) Σ_n f(n/T) 1_{v_p(n) par para todo p|r}.

En efecto n=k²t con t libre de cuadrados es una descomposición única; la condición sobre sus valuaciones es precisamente (t,r)=1. Esto reemplaza la densidad asintótica de 057 por una identidad discreta.

El indicador es Σ_{h|n, rad(h)|r}(−1)^Ω(h), por suma alternada en cada potencia prima. Extender f por cero a la recta. Poisson e ∫f=0 dan |Σ_l f(l/Z)|≤C Z^σ con una **misma C** para todo 0<σ≤1/2: si Z≥1 basta integración por partes dos veces; para Z pequeño la suma se anula, y el intervalo intermedio es compacto. La suma en l es sobre enteros positivos. Así el total de módulos de pendientes para r≤R es a lo sumo

    C L^σ Σ_{r≤R} 2^ω(r) Σ_{rad(h)|r} h^(−σ)
      ≤ C L^σ R log(2R) ∏_p [1+2/(p(p^σ−1))].

Para la desigualdad, fijar h y escribir r=rad(h)j. Usar 2^ω(r)≤2^ω(h)τ(j) y la suma elemental de τ. El logaritmo del producto es o(1/σ) al tender σ a cero: cada término multiplicado por σ tiende a cero y es ≤2/(p log p), sumable por Chebyshev y sumación parcial. Con σ=δ/(2√log L) resulta una cota L exp(−(δ/2+o(1))√log L), que prueba el enunciado. Para r=1 ya es rápido el decaimiento por Poisson; la nueva diagonal está incluida.

**Alcance.** Sigue faltando la cota superior uniforme O(L) sobre las pendientes con r>R. El promedio no borra polos del puente global; su ventaja demostrada es que sustituye el conteo de t libres de cuadrados por una suma lisa en todos los enteros, con una condición explícita en los primos que dividen r. La inversión por potencias cuadradas y la fórmula de Poisson son conocidas. La comparación es con la representación de 059 antes de promediar, que mantiene un soporte individual más estrecho.
