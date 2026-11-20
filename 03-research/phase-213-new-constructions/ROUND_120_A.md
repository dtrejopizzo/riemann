# Cuántos datos de la matriz par bastan en cada ventana

Para la matriz completa A en la base ortonormal de 119 bastan la diagonal y la primera fila: todos los términos restantes se recuperan exactamente, con amplificación a lo sumo polinómica en N=ceil(T³). El signo global equivale a que estos 2N−1 datos, en valor absoluto y con un techo común, sean exp(o(T)) o menores a lo largo de alguna sucesión T→∞. Bajo RH cumplen incluso una cota polinómica. La vuelta usa la matriz completa y no necesita positividad de las entradas.

**Identidad.** Poner a_j=(j+1/2)π/T, d_j=a_j², c_j=2(−1)^j a_j/√T, z=ρ−1/2. La transformada bilateral del coseno normalizado evaluada en z es c_j cosh(Tz)/(d_j+z²), con extensión continua en ±ia_j. Para i≠j, la fórmula de Weil polarizada (transformadas pares) y las fracciones parciales dan

    A_ij=c_i c_j (H_i−H_j)/(d_j−d_i),
    H_i=Σ_z cosh²(Tz)/(d_i+z²).

Para T fijo hay convergencia absoluta por O_T(1/γ²). En una coincidencia z=±ia_i el sumando de H_i se prolonga por cero porque el numerador tiene cero doble; en el producto cruzado la otra transformada se anula. La diagonal se conserva como dato separado. La fórmula de Weil es válida para estos modos H¹₀ por alisado, o directamente por decaimiento cuadrático de su transformada en cada franja y aproximación por convolución compacta.

Definir U_0=0, U_j=(d_j−d_0)A_0j/(c_0 c_j). Entonces A_ij=c_i c_j(U_j−U_i)/(d_j−d_i). El coeficiente de A_0j tiene módulo |c_i/c_0|·|(d_j−d_0)/(d_j−d_i)|, y análogamente para A_0i. El primero es ≤(2N+1)N² porque d_j−d_i=(π/T)²(j−i)(j+i+1) y d_j−d_0=(π/T)²j(j+1). Así la norma matricial es O(N⁴) por el máximo de los 2N−1 datos para N≥2.

**Necesidad de la cota absoluta.** Bajo RH, W(F)=Σγ|F̂(γ)|² para F unitario en esta base. Por subarmonicidad en discos de radio 1/(2T), el conteo local O(log(2+|γ|)) y la tira |σ|≤1/(2T), esta suma es ≪T²∫_tira∫ log(2+|ξ|)|(exp(σt)F)^∧(ξ)|²dξ dσ. Para estos modos ∥F'∥≤πN/T, y la extensión por cero está en H¹. El producto exponencial en el soporte tiene norma H¹≪1+N/T, de modo que el lado derecho es polinómico en T. Esto da por polarización o por la norma positiva la cota común de los datos. Recíprocamente, con el techo subexponencial supuesto, el coste O(N⁴) sigue siendo subexponencial, incluso para el mínimo en valor absoluto. 119 excluye Δ>0.

**Cotejo.** Las diferencias divididas y objetos de Loewner ya están en el corpus (entre otros R166_103A y la ruta POWER). Aquí no se trata la etiqueta Loewner como mecanismo de signo: la aplicación es la recuperación cuantitativa de esta matriz Dirichlet por una fila y la diagonal, junto con el criterio secuencial de 119. Las fórmulas de H_i por ceros pueden tener términos exponenciales sin RH; aún falta acotar los datos por la fórmula aritmética.

**Antecedente directo confirmado.** En el propio paper 47, lema `combsine` (main.tex, línea 6469), la combinación de dos cocientes para el peine en una paridad se simplifica a [a_i D_T(a_j)−a_j D_T(a_i)]/[T(a_i²−a_j²)]. Ya tiene la estructura que permite recuperar el peine por una fila fuera de la diagonal. Lo añadido en 120 corresponde a la forma completa, el coste de reconstrucción y el uso secuencial de 119.
