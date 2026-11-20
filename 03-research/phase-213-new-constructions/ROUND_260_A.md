# Qué parte de un binomial llega a los átomos primos de la octava

Fijar K≥2. Para n≤Kx y 1≤k≤n/2 enteros, sea c(m)=⌊n/m⌋−⌊k/m⌋−⌊(n−k)/m⌋. Definir la fracción real de la factorización que cae dentro de la octava por

    r(x,n,k) = [Σ_(x<m≤2x) Λ(m)c(m)] / log binom(n,k).

Para toda sucesión con x→∞ y k→∞, limsup r≤1/(2 log 2). La constante se alcanza como límite al tomar n=2k=2x entero par. Si k/n→0 y k→∞, la fracción tiende a cero. Esta vez se pesan los átomos reales de las potencias primas, no las longitudes de las bandas continuas. La restricción en la escala superior Kx es parte del teorema.

**Repartos macroscópicos.** Si n≤x la contribución local es cero. En n>x, si k/n se mantiene separado de cero, el núcleo en [x,2x] tiene O_K(1) saltos, pues n/m≤K. La estimación ψ(y)=y+o(x) uniforme allí muestra que el numerador difiere de la integral ordinaria en o_K(x), incluso si las bandas se mueven. Los convenios de extremos sólo cuestan O_K(log x). Stirling da para el denominador n E(k/n)+O(log n), con la entropía de 258, que es de orden x en este caso. Aplicar 258 y, para la igualdad límite, su ejemplo simétrico y el PNT.

**Repartos que se estrechan.** Supongamos x<n≤Kx y k=o(n). Por factorización del numerador factorial n(n−1)…(n−k+1), el numerador de r queda acotado por la suma, sobre j≤K, de Λ(m) para m en (x,2x]∩((n−k)/j,n/j]. Además binom(n,k)≥(n/k)^k por el producto de las razones (n−i)/(k−i).

Si k≥n^(7/10), cada intervalo sin recortar tiene longitud k/j y extremo comparable a n, con K fijo. Por el PNT de intervalos de 238 su masa prima es O_K(k); el aporte de potencias propias es O_K(√n log² n)=o(k). Así r≪_K 1/log(n/k)→0.

Si k≤n^(7/10), fijar un primorial Q. En cada intervalo de longitud ≤k/j, la cantidad de enteros coprimos con Q es ≤(k/j)φ(Q)/Q+O(Q) por periodicidad. Entre los no coprimos sólo aportan potencias de los primos divisores de Q; en (x,2x] hay a lo sumo una potencia de cada uno. Acotando el peso por log(2x) y dividiendo por k log(n/k)≥0.3k log n, queda limsup r≪_K φ(Q)/Q para k→∞. El producto de Euler permite hacer esta última razón arbitrariamente pequeña. Los dos casos y la extracción de subsucesiones prueban la uniformidad secuencial afirmada.

**Coste mínimo para eludir la barrera sobre los primos.** Permitir en cada x una mezcla positiva de binomiales de argumentos enteros hasta Kx, con suma de coeficientes B(x) y coste total L(x)=Σ a_i log binom(n_i,k_i). Para cada ε>0 existen k₀ y x₀ tales que r≤1/(2 log 2)+ε si k_i≥k₀ y x≥x₀, por el resultado secuencial. Los binomiales restantes cuestan en total a lo sumo k₀ B(x) log(Kx), por simetría del reparto. De ahí:

    masa atómica local ≤ (1/(2 log 2)+ε)L(x) + k₀ B(x)log(Kx).

Si la mezcla mayoriza g(p/x) de 257 tan sólo en los primos x<p≤2x, su masa local es al menos xh+o(x) por el PNT y sumación parcial, con h=∫g. Incluso esa condición puramente aritmética fuerza liminf L(x)/(xh)≥2 log 2 cuando B(x)=o(x/log x). Más cuantitativamente, ahorrar una fracción fija η>0, es decir L(x)≤(2 log 2−η)xh, obliga a B(x)≥c_(K,η)x/log x para x grande; elegir ε suficientemente pequeño en la desigualdad anterior.

El orden de coeficientes es óptimo: para cada primo x<p≤2x usar binom(p,1)=p con coeficiente g(p/x). Su acarreo en m≥2 vale uno exactamente si m divide p. Así reproduce el peso en cada primo y no carga ninguna potencia propia, con B(x)∼xh/log x y L(x)=Σg(p/x)log p∼xh. Esta construcción vuelve a pagar exactamente la suma que se busca acotar; no da por sí misma un margen de raíz.

**Distinción.** 258 dejaba expresamente abierta la transferencia de su cota geométrica a los átomos. Aquí ésta se prueba para presupuestos sublineales en x/log x y se localiza un mecanismo que rompe la cota al alcanzar esa escala. 259 permite restas; la barrera atómica demostrada aquí se refiere a coeficientes positivos. No trata argumentos mayores que un múltiplo fijo de x.
