# Ensanchar el filtro con reparación local: ganancia logarítmica y barrera semiprima

Conservar Q,δ,κ,N de 288. Para r>1 definir L(r) como la suma de 2^(−ω(r))Wδ(log(a/b)) sobre pares ordenados coprimos distintos con ab=r; poner L(1)=0. Para todo n libre de cuadrados se tiene exactamente

    Q(n)−μ(n)=Σ_(mr=n) μ(m)L(r),     Σ_(d|n) Q(d)=1_(n=1)+L(n).

La segunda fórmula invierte la primera sólo dentro de los divisores del entero libre de cuadrados. Todo L(r) activo tiene r>N/κ², pues |a−b|≥1 y |a−b|√(N/r)<κ. Así todos los signos μ(m) de la corrección pueden obtenerse con m<κ².

**Mayorante reparado.** En enteros libres de cuadrados añadir a Q(n) las cantidades L(r) con mr=n y μ(m)=−1; en los demás conservar cero. El resultado Q⁺ mayoriza a μ y a Q punto por punto. Para 1≤κ≤N^(1/4) se obtiene

    Σ_(n≤N)|Q(n)−μ(n)|,  Σ_(n≤N)(Q⁺(n)−μ(n))
       ≪ κ √N log(2κ)/(log(2N))^(3/4).

En particular κ=(log N)^(3/4)/log log N permite una anchura creciente y un coste absoluto O(√N) en todos los subintervalos. Para el criterio de 287 ya no hace falta restringir la anchura al primer cambio de signo.

**Demostración del techo.** Sumar los módulos de los términos de la primera identidad, incluso antes de agrupar por n. Para cada m≤κ² y diferencia entera 1≤h<κ/√m queda una suma sobre a≤A=√(N/m), b=a+h. Por coprimalidad y libertad de cuadrados, el peso es el producto de μ²(a)2^(−ω(a)) y la misma función en a+h. Retirar las restricciones restantes y aplicar Cauchy–Schwarz. Como h≤A y A≥N^(1/4), la suma cuesta O(A/(log N)^(3/4)), uniformemente en h.

Para verificar la estimación elemental utilizada, sea g(j)=μ²(j)4^(−ω(j)). Por descomposición de log j en primos, Σ_(j≤t)g(j)log j ≤(1/4)Σ_(u≤t)g(u)θ(t/u)≪t Σ_(u≤t)g(u)/u. El producto de Euler finito y la estimación de Mertens para los recíprocos primos acotan el último factor por O((log(2t))^(1/4)). Separar j≤√t y dividir por log(√t) en el resto da Σg(j)≪t/(log(2t))^(3/4). Finalmente sumar los h y usar Σ_(m≤κ²)1/m≪log(2κ); un factor dos cuenta ambas orientaciones.

**Barrera incondicional.** Para C log N≤κ≤N^(1/4), con C suficientemente grande, ya sobre productos n=pq de dos primos distintos se tiene

    Σ_(n=pq≤N) (Q(n)−μ(n)) ≫ κ √N/(log N)².

Para esos enteros la única factorización no trivial que puede estar cerca del equilibrio es (p,q) y su inversa: la partición (1,pq) está fuera de soporte y los divisores primos de n no tienen factorizaciones cercanas (δ<log 2). Por eso no hay compensación negativa en ningún semiprimo con primos distintos. Dividir [.6√N,.8√N] en O(√N/κ) cajas de longitud ≤κ/10 y comparable con κ. El PNT da ≫√N/log N primos en total. Cauchy–Schwarz aplicado a sus ocupaciones y la identidad para el número de pares distintos dan ≫κ√N/log²N pares dentro de la misma caja para C grande. Para cada uno log(q/p)≤κ/(6√N) y Wδ≥1/2 para N grande. La corrección es por tanto ≥1/4. Cada entero producido es distinto salvo el orden de sus dos factores.

En particular κ=N^α con 0<α≤1/4 hace imposible que un procedimiento que sólo AÑADA términos a Q para mayorar μ tenga exceso total N^(1/2+o(1)). Esta barrera no descarta una corrección que también disminuya Q en productos identificados. Tampoco prueba un techo unilateral para la suma de Q⁺. El dato nuevo frente a 288 es el presupuesto cuantitativo en una anchura creciente y la obstrucción aritmética independiente del signo en los otros enteros.
