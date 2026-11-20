# Coste inevitable de tomar módulos en una vertical del producto neutralizado

**Estado: PROVED, con revisión independiente de la uniformidad en todas las verticales σ≥1/2.**

Para z=L² y cualquiera de los dos cortes y de 387, sea D(s)=∏_{z<p≤y}(1−p^(−s)). Definir el mayorante por valor absoluto de la integral de Mellin

    M(σ)=x^σ exp((σ−1/2)²/2) ∫ exp(−t²/2)|D(σ+it)| dt / (2π).

Entonces inf_{σ≥1/2} M(σ)=x^(1+o(1)). En σ=1/2 hay incluso una banda de anchura ≍1/log y con log |D|≫√y/log y. La orientación y el signo del verdadero pulso se pierden antes de alcanzar escala de raíz en este mayorante.

**Verticales próximas a uno o a su derecha.** Para una normal estándar T, la media del logaritmo del módulo vale exactamente

    E log |D(σ+iT)|=−Σ_{z<p≤y}Σ_{k≥1} p^(−kσ) exp(−(k log p)²/2)/k.

Es o(1) en módulo uniformemente para σ≥1/2, por comparación con la serie convergente sobre enteros n>z. Jensen da M(σ)≫x^σ. Para σ≥1−40 log L/L resulta M(σ)≫x/L^40.

**Verticales más a la izquierda.** Poner b=log y∼L/2, d=1−σ≥40 log L/L y tomar 0.95π/b≤t≤1.05π/b. En y^(3/4)≤p≤y tenemos cos(t log p)≤−c, y por ello log|1−p^(−σ−it)|≥c' p^(−σ). Sólo con p∈[y/2,y] se obtiene ≫y^d/b por el PNT. Los primos menores podrían restar a lo sumo O(Σ_{z<p≤y^(3/4)}p^(−σ))≪y^(3d/4) log b por Mertens, puesto que p^(−σ)≤p^(−1)y^(3d/4). El cociente de este coste por el piso tiende a cero uniformemente pues b log b exp(−bd/4)=o(1). Así log |D|≫y^d/b en toda la banda. Incluso en el extremo d mínimo este piso supera L² para x grande, compensando de sobra el ancho y el descenso de x^σ.

Finalmente M(1)≪x exp(Σ_{p≤y}1/p)≪x log y. Los dos extremos prueban el exponente del ínfimo. El resultado vale para estos productos con signo menos en cada factor: la pérdida de módulo en el producto inverso de 370 tenía orientación distinta. Esta obstrucción atañe al mayorante absoluto de verticales enteras con σ≥1/2; deja disponibles la fase del integrando, agrupaciones aritméticas y contornos no verticales.

**Registro de revisión.** La expansión logarítmica es uniformemente sumable para σ≥1/2, pues p^(−σ)≤z^(−1/2)<1; después de promediar la gaussiana queda dominada por la cola de Σ_{n>z} n^(−1/2)exp(−(log n)²/2)=o(1), incluyendo las potencias primas. Con la normalización de M, Jensen da M(σ)≥(1+o(1))x^σ exp((σ−1/2)²/2)/sqrt(2π), por lo que cubre también σ arbitrariamente grande. En el tramo izquierdo d∈[40log L/L,1/2], se tiene bd≥(20−o(1))log L: el cociente negativo es O(L log L·L^(−5+o(1)))=o(1) uniformemente, y el piso y^d/b≥L^(19−o(1)) supera L² con margen. La banda tiene anchura≍1/b y peso gaussiano separado de0; su contribución vence uniformemente cualquier descenso de x^σ para σ≥1/2. En consecuencia x/L^40≪inf M≪xL, que implica exactamente la afirmación de exponente, sin afirmar una constante asintótica para el ínfimo.
