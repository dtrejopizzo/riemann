# El criterio pendiente como una suma finita alternada

Antecedentes: 047 deja una integral impropia y una suma corta. El peso de paridad ya figura entre las combinaciones de residuos en fase 188, L2_BUILD_030 §3, y en fase 211, CORRECTION_RESIDUE_BALANCE_031. Aquí se hace coincidir el corte físico en dos escalas para cancelar la integral y se recupera la cota unilateral por iteración hacia escalas mayores.

Con V,g,χ de 047 definir A(x)=x∫V−Σ_n Λ(n)V(n/x) y β(y)=[1−χ(log y)]log y. Para x=j⁴ elegir K como en 047, por ejemplo K=C₀(log x)² con la primera construcción. La positividad global equivale a la existencia de C tal que eventualmente

    Σ_{k<2eK} (−1)^(k+1) β(k/(2K)) g(k/(2x)) ≤ C√x.

Vale también el corte afinado de 047 con su peso correspondiente. Cada g(t)=Σ_{m≤16e/t}μ(m)V(mt) es una suma finita.

**Cancelación.** Aplicar 047 con el corte K en x y el corte 2K en 2x. El segundo corte también da error O(√x) por la estimación de orden q de 047, aumentando si hace falta la constante inicial de K. Para la función inferior F(u)=g(u/x)β(u/K), la de la segunda escala es F(u/2). Su integral es exactamente dos veces la primera. Así 2A(x)−A(2x) es, salvo O(√x) bilateral, la suma sobre todos los k de F(k/2) menos dos veces la suma sobre los índices pares de F(k/2). Resulta la expresión alternada del enunciado.

**Recuperación.** Bajo el signo |A(x)|≤C√x por 047. En sentido inverso escribir D(r)=exp(−r/2)A(exp r); la diferencia normalizada es 2D(r)−√2 D(r+log 2). Por 047 su segunda derivada es O(exp(r/2)), por lo que una cota superior en las muestras j⁴ se extiende a todo x grande por interpolación con error O(1). Luego A(x)≤A(2x)/2+C√x/2. Por el teorema de los números primos A(y)=o(y), usando sumación parcial con el peso fijo V. Al iterar, 2^(−N)A(2^N x) tiende a cero y la suma de errores está acotada por C√x/[2(1−1/√2)]. Aplicar 047.

**Dónde se necesita cancelación.** Expandiendo g, el coeficiente de V(n/(2x)) es Σ_{k|n, k<2eK}(−1)^(k+1)β(k/(2K))μ(n/k). Para cada primo n dentro de la banda y suficientemente grande x, sólo contribuye k=1 y el coeficiente vale log(2K). En un subintervalo fijo del interior donde V≥η>0, estos términos solos suman ≫ x log(2K)/log x por PNT, superior a √x. Esto descarta estimar la suma por su parte positiva término a término después de agrupar por n. La compensación con los compuestos queda abierta. No es un contraejemplo al criterio.
