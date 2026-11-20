# Un mismo peso para el signo unilateral en la octava y el residuo firmado de la banda

Sea L=log 2, λ=1−10^(−6). En la coordenada logarítmica tomar la densidad (1−cos(2πv/L))/L en [0,L], contraerla por el factor λ conservando integral uno, y convolucionarla con la densidad de uniformes de 274 contraída a [0,(1−λ)L] y normalizada a masa uno. Llamar f a la densidad obtenida, w(y)=y^(−1/2)f(log y), h=∫w(y)dy. Es positiva en (1,2), de masa logarítmica H(1/2)=1. El soporte sigue siendo [1,2]. Su Mellin no se anula para Re s>1/2 por las fórmulas de producto de 257 y 274. La convolución conserva las cotas de derivadas de orden Gevrey dos del segundo factor con constantes fijas, posiblemente grandes. Así 274 aplica a w con su propia constante C.

**Presupuesto unilateral.** En la línea crítica poner t=γL/2. El módulo de la transformada es ≤|F(λt)|, con F(t)=sin(t)/[t(1−t²/π²)], por la fórmula de 257 y porque el otro factor es una transformada de probabilidad. Para v≥4.7 se tiene |F'(v)|≤100/v³: escribir F=−π² sin(v)/[v³(1−π²/v²)] y derivar, usando 1−π²/v²>0.55. Para todos los ceros bajo RH, λ|t|>4.7 por la primera ordenada >14. Por el valor medio el coste adicional por cero es ≤100(1−λ)/(λ³t²). La traza de 248/257 da Σγ^(−2)<0.048 bajo RH (multiplicar la cota 0.047 para Σ|ρ|^(−2) por 1+1/(4·14²)). Con la cota 0.471 de 257 resulta Σ|H(ρ)|<0.472. La fórmula explícita para Λ da un error espectral ≤0.472√x más o(√x). La contribución de los cuadrados de primos, por el teorema de los números primos con el peso fijo w(u²), es (√x/2)H(1/2)+o(√x). Las demás potencias propias son no negativas. Por tanto bajo RH

    liminf [xh−Σ_p log(p)w(p/x)]/√x ≥ 0.028.

A la inversa, el signo eventual del numerador implica RH por el argumento de Landau de 257 y la ausencia de ceros de H en el semiplano abierto. Aquí el margen es asintótico bajo RH; no se ha recalculado el rango finito de 257.

**Reducción a un escalar unilateral.** Tomar el ajuste concreto R de 274 para este peso, después de la reparación inferior y la calibración, con U=⌊√N⌋, N=⌊2x⌋. Definir

    E(x)=Σ_(U/(C log²(2N))<q≤U) Λ(q) R(q).

Entonces RH equivale a que para cada ε>0 exista C_ε con E(x)≥−C_ε x^(1/2+ε) para todo x suficientemente grande. Basta un solo lado; no se impone exactitud en ningún átomo adicional.

En efecto, con J(x)=ΣΛ(m)w(m/x), la identidad exacta es J(x)+E(x)=Σ a_(n,k)log binom(n,k), porque el objetivo vale cero en la banda y se reproduce en los otros átomos. La calibración y Stirling dan J(x)−xh=−E(x)+O(√x log³(2x)). Bajo RH se tiene J(x)−xh=O_w(√x), lo que prueba la necesidad. En sentido inverso, la cota inferior de E da una cota superior de J(x)−xh a todo exponente σ>1/2. Si existiera un cero ρ a la derecha, elegir 1/2<σ<Re ρ. La función eventualmente no negativa Kx^σ−(J(x)−xh) tiene Mellin con un polo en ρ por H(ρ)≠0, pero es analítica en todos los puntos reales mayores que σ: el polo principal de ζ se cancela en 1 y ζ no tiene ceros reales allí. Esto contradice el teorema de Landau sobre la abscisa de convergencia de un Mellin de signo eventual. La cota unilateral de E continúa abierta. Esta equivalencia permite que errores en diferentes primos de la banda se compensen por completo.
