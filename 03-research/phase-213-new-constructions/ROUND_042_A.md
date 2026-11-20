# Un minorante explícito con un único corrector de criba

En el problema de 041 se puede alcanzar asintóticamente el valor óptimo, con error aditivo o(1), sin elegir coeficientes por cadenas de potencias de primos grandes. Los datos variables usados son sólo divisibilidad por primos pequeños, un producto de Euler finito y el peso w(t)=min(t,t⁻²).

Para x suficientemente grande tomar Y=x^(3/4)/(log x)^(1/8). Llamar libres a los enteros sin divisor primo ≤Y; 1 se incluye en esta clase. Escribir

    Z=Σ_{m libre}m⁻²=ζ(2)∏_{p≤Y}(1−p⁻²),       c=1−1/Z.

Definir b₁=0, y para n>1 libre tomar b_n=w(n/x)−c(x/n)². Para los otros enteros tomar b_n=0. Estos coeficientes son no negativos para x grande. En efecto, 0≤c≤Σ_{p>Y}p⁻²=O(1/(Y log Y)) por el producto de Euler y Chebyshev. En la rama n≥x el factor restante es 1/Z>0. En la rama n<x basta n³≥cx³, que vale ya en n=Y para x grande porque x³/(Y⁴ log Y)→0.

**Identidad exacta de filas.** Para todo entero d>1 no libre, D_d=Σ_{m≥1}b_{dm}=0. Si d>1 es libre, los únicos términos admisibles son los de m libre. Para m>1 se cumple dm>Y²>x, de modo que todos los múltiplos estrictos usan la misma rama cuadrática. Por consiguiente

    D_d=w(d/x)+(x/d)²[(Z−1)−cZ]=w(d/x).

Esto verifica incluso las filas compuestas fuera del soporte de Λ. En particular el minorante sólo pierde las filas de potencias de primos con base p≤Y. El argumento sólo usa el producto de Euler en 2, donde es absolutamente convergente.

**Precisión con soporte infinito.** Por la identidad de divisores y por Tonelli, el valor V=x^(−1/2)Σ b_n log n es el peso completo de las filas p^k con p>Y. El peso descartado de los primos p≤Y es O(Y²/x^(3/2))=O((log x)^(−1/4)). El peso de todos los cuadrados tiende a 2/3 por 039, y los cuadrados con p>Y tienen peso O(x^(3/2)/Y³)=o(1) por sumación parcial. El total de exponentes ≥3 es o(1). En suma, Q(x)−V(x)=2/3+o(1), la misma pérdida asintótica que en el óptimo de 041.

**Precisión con soporte finito.** Truncar b_n a n≤N∼λ x^(3/2), con λ>0 fijo. Por positividad se mantienen todas las restricciones. El valor retirado es exactamente

    x^(3/2) Z⁻¹ Σ_{n>N, n libre} log(n)/n².

Los primos de la cola aportan 1/λ+o(1) por el teorema de los números primos y Z→1. Para acotar los compuestos libres, escribir B=Σ_{p>Y}p⁻² y A=Σ_{p>Y}log(p)/p². Mayorar cada producto de k factores primos por el conteo que usa todas sus ordenaciones da, al sumar log n por sus k factores, un total ≤Σ_{k≥2}k A B^(k−1)=O(AB). Se tiene A=O(1/Y), B=O(1/(Y log Y)). Incluso antes de imponer n>N, la contribución normalizada de estos compuestos es O(x^(3/2)/(Y² log Y))=o(1). Así los pesos explícitos truncados dejan pérdida 2/3+1/λ+o(1), y su valor difiere en o(1) del máximo exacto de 041. No se requiere clasificar como primo o compuesto ningún entero mayor que Y para calcular b_n.

**Alcance.** Se ha eliminado la dependencia explícita de las capacidades de los primos grandes en la *elección* del minorante. Su valor es una suma sobre enteros que pasan la criba, y donde Y<n≤x esos enteros son precisamente primos. Probar una cota inferior (3/2)√x−O(1) para la suma sigue siendo la obligación de signo. La identidad de las filas y el error o(1) no dan por sí mismos tal estimación.

Cotejo y revisión: R166_601_ROUGH_ZETA_JOIN §§1–3 ya registra el producto de Euler de enteros cribados y su conteo por inclusión-exclusión. El aporte de esta ronda es el corrector positivo a esta escala y la comparación de su valor con el óptimo. La identidad, la no negatividad eventual y ambas pérdidas asintóticas recibieron auditoría independiente.

## ¿Se puede estimar el valor por un promedio de traslaciones de la criba?

Fijar N∼λx^(3/2) e Y como arriba. Poner P=∏_{p≤Y}p, ρ=φ(P)/P, y f(n)=log(n)[w(n/x)−c(x/n)²] para Y<n≤N, cero fuera. Para un residuo h uniforme módulo P considerar

    V_h=x^(−1/2) Σ_n f(n) 1_{(n+h,P)=1}.

V₀ es precisamente el valor del minorante truncado de esta ronda. Las otras traslaciones sólo sirven como comparación; no se presume que sean minorantes admisibles. Se tiene

    V₀=(3/2+o(1))√x,     media_h V_h=(2 exp(−γ_E)+o(1))√x,
    var_h V_h=O(log x).

Por tanto, para cada C fijo, la proporción de residuos con V_h≥(3/2)√x−C es O((log x)/x). La misma conclusión vale con umbral V₀−C. La estimación para la fase cero sólo usa aquí el término principal, no el error O(1) que se busca.

**Media.** La media exacta es ρx^(−1/2)Σ f(n). La masa sin criba es (3/2+o(1))x log x, por sumas de Riemann de w, cuya integral es 3/2. Para el paso al intervalo infinito, la suma sobre n>Mx es O(x(log x+log M+1)/M) para M≥1, por comparación integral; el tramo n≤Y=o(x) aporta O(Y²log x/x). El corrector cuesta O(cx²(log Y+1)/Y)=o(x log x). Mertens da ρ log x→(4/3)exp(−γ_E). Para V₀, el teorema de los números primos en Q y la pérdida acotada de 042 dan el término principal indicado. La diferencia entre ambos coeficientes es estrictamente positiva.

**Varianza.** La norma ℓ¹ de f es O(x log x) y su variación total, incluyendo los dos extremos, es O(log x). En la rama inferior n log(n)/x crece hasta log x y el término c x² log(n)/n² decrece desde O(log x), por la elección de Y. En la rama superior (1−c)x² log(n)/n² decrece. Por sumación por partes la transformada discreta de f en una frecuencia t tiene módulo O(log x) min(x,1/dist(t,ℤ)). Para una frecuencia reducida r/d con d|P, el módulo del coeficiente de Fourier normalizado del indicador de coprimalidad es ρ/φ(d): por el teorema chino del resto cada primo que divide el conductor cambia su factor local en la razón 1/(p−1). Parseval omitiendo la frecuencia cero da

    var_h V_h ≪ (ρ² log²x/x) Σ_{d|P,d>1} φ(d)^(−2)
                     Σ_{r=1}^{d−1} min(x,d/min(r,d−r))².

La suma interior es O(dx): si d≤x basta sumar los inversos cuadrados, y si d>x separar en r=d/x usando la simetría. El producto resultante ∏_{p≤Y}(1+p/(p−1)²) es O(ρ⁻¹), por comparación factor a factor con (1−1/p)⁻¹ y convergencia de Σp⁻². Esto da la cota de varianza. La estimación de la proporción sigue de Chebyshev y de la separación de orden √x.

**Decisión.** R166_601 ya distingue entre densidad periódica y conteo de enteros libres cuando log x/log Y permanece acotado. Este cálculo cuantifica el fallo para el objetivo ponderado de 042, incluso al permitir traslaciones: el promedio pierde en el término principal y los valores del tamaño buscado son excepcionales respecto de esa media. Para la fase cero queda abierta la desigualdad con error aditivo O(1). La varianza es una cota para el ensamble de traslaciones, no para el error de la fase cero.

**Cuántos módulos se pueden promediar a la precisión de signo.** Hay una versión parcial que sí conserva el valor hasta O(1). Elegir cualquier subconjunto B de los primos en (Y/2,Y]. Mantener h≡0 en todos los módulos de la criba exteriores a B y promediar h libremente en los de B. Por el teorema chino, la media condicional es

    ρ_B [V₀+o(1)],        ρ_B=∏_{p∈B}(1−1/p),

con error uniforme en la elección de B. En efecto el factor ρ_B sale exactamente al promediar los indicadores locales. Al quitar las restricciones de B del conteo original, los nuevos enteros del soporte Y<n≤N son compuestos (contienen un primo de B menor que n) y todos sus factores son mayores que Y/2. Por ello n>(Y/2)²>x para x grande. Su aportación adicional es no negativa y a lo sumo O(x^(3/2)/(Y² log Y))=o(1), usando el mismo conteo por productos ordenados de la primera parte con corte Y/2. Esto prueba la uniformidad.

Por consiguiente la diferencia entre V₀ y la media condicional es (1−ρ_B)V₀+o(1). Como V₀∼(3/2)√x y los primos de B son comparables a Y, conservar el valor a distancia O(1) equivale exactamente a |B|=O(Y/√x). Para ver ambas direcciones, usar 1−exp(−Σ_{p∈B}1/p)≤1−ρ_B≤Σ_{p∈B}1/p. Con |B|=o(Y/√x) el error tiende a cero. En cambio, al promediar toda la banda, el coste es asintótico a (3/2)√x log(2)/log Y, pues Σ_{Y/2<p≤Y}1/p∼log(2)/log Y por el teorema de los números primos. Es una tolerancia precisa para esta operación; no proporciona la cota inferior del valor que se promedia.
