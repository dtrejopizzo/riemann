# En los propios primos de la banda el error absoluto supera el presupuesto de raíz

Para el ajuste concreto de 274–275, sean U=⌊√N⌋ e Y=U/(C log²(2N)), tomando C suficientemente grande en la construcción. Para todo x suficientemente grande se cumple incondicionalmente

    Σ_(Y<p≤U) log(p) |R(p)| ≫ N^(3/4)/log(2N).

La constante depende del peso fijo. En particular un argumento que mayore el escalar firmado de 275 sumando el módulo de cada término no puede alcanzar la cota buscada para esta construcción.

**Momento forzado de la respuesta continua.** Antes de la reparación puntual escribir T(y)=Σ_(l≥1) S(ly) para y real positivo, con S de 274. En los enteros de la banda coincide exactamente con R: todas las filas de reparación tienen extremos ≤Y o ≤6. Para y>U vale T(y)=w(y/x) incluso fuera de los enteros, por inversión finita de Möbius en el argumento real. Escribir I=∫S. La cuadratura de 274 en y=1 da |I|≪x log²(2N)exp(−c√U); para 0<y≤Y la misma periodización da |T(y)−I/y|≪x log²(2N)y^(−1)exp(−c√(U/y)). Agrandando C, su integral con peso y^(−1/2) hasta Y es O(N^(−2)), como se ve poniendo z=√(U/y).

Para Re s>1 la transformada de T es ζ(s)∫S(t)t^(s−1)dt, por cambio de variable en cada sumando. La prolongación al sustraer I/y en (0,U) añade el término I U^(s−1)/(s−1) a la transformada de la diferencia. Evaluar en ρ=1/2+iγ₁, el primer cero crítico conocido. Los términos que contienen I en [Y,U] y en la prolongación son O(N^(−2)). Resulta

    ∫_Y^U T(y)y^(ρ−1)dy = −x^ρ H(ρ)+O(N^(−2)).

Aquí H(ρ)≠0: para la primera ordenada entre 14 y 15, λγ₁ log(2)/2 está estrictamente entre π y 2π, y los factores de uniformes de anchura total 10^(−6)log 2 tampoco tienen un cero allí. Su producto converge a un valor no nulo. Como |y^(ρ−1)|≤1/√Y, obtenemos ∫_Y^U |T(y)|dy ≫ √(xY). La identidad de Mellin es clásica; lo que se necesita además es pasar el piso a las muestras primas efectivas.

**Transferencia a primos sin asumir RH.** Para t≥U/4 la fórmula de 274 da |S'''(t)|≪x log²(2N)/t⁴. En la parte de inversión sólo hay O(x/t) índices d activos, todos con d/x≤2/t; las derivadas del corte contribuyen en t comparable con U. Los correctores también viven en esa escala y tienen amplitud O(x log²(2N)/U). Para t<U/4 la función es cero. Sumando l³|S'''(ly)| y usando l≤2x/y se obtiene |T'''(y)|≪x log³(2N)/y⁴ para y∈[Y,U].

Partir [Y,U] en celdas de longitudes entre H₀=U^(7/10) y 2H₀. En cada celda elegir tres subintervalos interiores de longitud un décimo de la celda, con separación al menos otro décimo. Cada subintervalo tiene masa prima Σlog p ≫H₀ uniformemente por 238, pues H₀/U^(5/8)→∞ y H₀/Y→0. En cada uno elegir un primo que minimice |T(p)|. Interpolar cuadráticamente T en esos tres primos. En toda la celda los coeficientes de Lagrange son O(1) por la separación, y el resto es O(H₀³ sup|T'''|). Tras integrar y sumar, las contribuciones de los nodos cuestan a lo sumo una constante por la suma ponderada de |T(p)| en toda la banda. El error total es

    O(U H₀³ x log³(2N)/Y⁴) = O(U^(11/10) log¹¹(2N)) = o(√(xY)).

Esto prueba la cota en los propios primos. El resultado estudia el tamaño absoluto para este ajuste; deja abierta la cota inferior unilateral del escalar E(x). Tampoco impone la misma obstrucción a combinaciones sin la interpolación continua usada aquí.
