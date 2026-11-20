# Umbral de los pesos en el divisor común

Con las clases B_q de 334, incluida la diagonal, fijar 0<κ<1 y poner V_m(κ)=Σ q^κ |B_q|. En las anchuras h→0 con log(1/h)=o(m),

    limsup V_m(κ)^(1/(2m)) = max{1/(3/2−Θ), 1/(1−κ/2)}.

En particular ningún peso q^κ con κ>0 arbitrariamente pequeño conserva bajo RH el techo uno. En cambio todo peso fijo 1≤w(q)≪_ε q^ε para cada ε>0 conserva exactamente la tasa de 334, por comparación y haciendo κ→0. Esto incluye pérdidas fijas por potencias del número de divisores.

**Techo.** El argumento dual de 334 con |b(q)|≤q^κ da |(μ*b)(g)|≤g^κτ(g). En los discos de radio r basta por ello exigir σ=3/2−r>max{Θ,(1+κ)/2}. La suma de los Gram J_g con esos pesos converge por la cota de 334, tomando 2ε<2σ−1−κ. La pérdida por la altura es subexponencial. Los intercambios también son absolutos a orden fijo: fuera de diagonal se usa 331 con Σ g^(κ−2)τ(g)<∞; en la diagonal el peso total por n es ≤n^κτ(n)^2, sumable contra l_m(n)^2. Se obtiene el techo al llevar r a su extremo.

**Piso aritmético.** Además de V_m(κ)≥V_m(0), elegir b(q)=q^κ. Su inversión c(g)=g^κ∏_{p|g}(1−p^(−κ)) es positiva. Así V_m(κ)≥Σ c(g)J_g. En el Gram de los múltiplos de un primo p la muestra n=p tiene soporte disjunto de las de 2p,3p,… cuando h<log 2. Su contribución individual vale l_m(p)^2 por K(0)=1 y el Gram restante es no negativo. Por tanto

    V_m(κ) ≥ Σ_p (p^κ−1) l_m(p)^2.

Tomar X=exp(2m/(2−κ)). El teorema de los números primos da ≫X/log X primos entre X y 2X. Ese bloque aporta ≫ X^(κ−2)(log X)^(2m)/((log X)(m!)²). Por Stirling su raíz de orden 2m tiene límite inferior al menos 2/(2−κ). El piso sólo necesita h<log 2 y también rige en las ventanas exponenciales de 326. Bajo RH en esas ventanas se obtiene el techo correspondiente por el mismo argumento de 334 con exponente de altura arbitrariamente pequeño.

**Uso para el cierre.** Una prueba por clases puede absorber pérdidas subpolinómicas en q a nivel de la tasa. Si paga una potencia fija de q sobre las clases completas, la primera muestra de cada progresión prima ya impide el techo uno. Para clases con la diagonal sustraída este piso no se ha demostrado.
