# La clase de cocientes primitivos ya tiene toda la tasa absoluta

En la escala h=exp(−am), 0<a<log 4, sea P*_m la suma de 326 con valores absolutos restringida a (n,d)=1. Entonces

    lim (P*_m)^(1/(2m)) = 2 exp(−a/2).

**Conteo en la banda.** Para X entero, H entero entre 1 y X, contar X≤n<2X y d=n+k, 1≤k≤H. Al crecer H y X, la proporción de pares para los cuales nd es libre de cuadrados tiende a

    c = ∏_p (1−1/p)²(1+2/p)>0.

En efecto, para los primos hasta P fijo, tomar el módulo M producto de sus cuadrados. El rectángulo de (n,k) se equidistribuye en clases módulo M en ambas coordenadas, y (n,k)↦(n,n+k) es biyectiva módulo M. En cada primo se permiten dos unidades o exactamente una coordenada divisible por p una sola vez y la otra unidad. Esto da el factor local escrito; el producto converge a un valor positivo pues su factor es 1−3/p²+2/p³. Para p>P los pares con p²|n o p²|d cuestan O(H(X/P+√X)), contando primero el múltiplo del cuadrado hasta 3X y luego hasta H vecinos. Los pares con p|n,d sólo contribuyen si p|k, luego cuestan a lo sumo Σ_(P<p≤H)(2X/p)(H/p) ≪ XH/P. Dividir por XH y hacer crecer primero X,H y después P. Este conteo elemental no requiere uniformidad de la distribución de μ en intervalos cortos particulares.

**Transferencia.** Tomar X=⌈exp(2m)⌉, H=⌊c₀hX⌋ con 0<c₀<1 tan pequeño que K≥1/2 en [−c₀,c₀]. Se tiene H→∞. En todos los pares contados, |μ(n)μ(d)|=1, (n,d)=1, d≤3X y 0<log(d/n)≤c₀h. La suma restringida es por ello ≫ h X² (2m)^(2m)/((m!)²(3X)^3) ≫ h4^m/m por Stirling. El techo procede de 326. En particular, incluso un argumento que consiguiera eliminar exactamente todas las clases con mcd mayor que uno seguiría afrontando la tasa absoluta íntegra en la clase restante. El cálculo deja abierto el signo agregado dentro de esa clase y no impide cancelación entre clases en la energía total.

**Antecedentes en la fase.** 326 usa ocupación en celdas sin imponer coprimalidad; 331 da un techo para la cola de divisores comunes. Aquí el piso persiste tras fijar el mcd exactamente igual a uno. La densidad elemental sólo se usa para obtener esta conclusión sobre la energía.
