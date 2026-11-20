# El sesgo positivo del producto cribado y un criterio de signo sin barrera

Para el mismo Q_a de 365, z=L², L=log x y a>0 fijo, **la positividad eventual Q_a(x)>0 equivale a la exclusión parabólica de 364**. Por tanto basta probar positividad eventual para a en una sucesión positiva tendiente a cero. Para cada a del rango verificado en 364 el signo es ya estrictamente positivo a toda escala suficientemente grande. Se trata del nuevo observable, no de un aumento de la ventana de soporte de P47.

**Fórmula en el régimen sin ceros prohibidos.** Definir K(s)=LΦ_a(s)+log E_z(s) usando la rama real sobre el eje real y sea s₀ la solución real de K'(s₀)=0 cerca de 1/2. Entonces

    Q_a(x) ∼ [−L/ζ(1/2)] exp(K(s₀))/√(2π K''(s₀)),
    K(s₀)=L/2+(1+log 2+o(1))L/log z,    K''(s₀)∼L log z.

El signo del coeficiente es positivo, pues ζ(1/2)<0 por la serie eta alternada.

**Localización.** Para σ=1/2+c/log z, con c en un compacto fijo, el teorema de los números primos y sumación parcial dan Σ_{p≤z}log p/(p^σ−1)∼2e^(−c)L uniformemente. Los términos de potencias ≥2 cuestan O(log²z) aquí para c≥0. La suma principal se obtiene integrando t^(−σ)dt. Análogamente log E_z(σ)∼2e^(−c)L/log z, y la segunda derivada de log E es ∼2e^(−c)L log z (añadir un factor log p a la primera suma). Como K''>0, el cambio de signo de K'=L(1+a(σ−1/2))−Σlog p/(p^σ−1) da s₀=1/2+(log 2+o(1))/log z. Sustituir en K y K'' da las dos fórmulas.

**Integral en la vertical del punto crítico.** Escribir D_z=E_z B_z con B_z=F'−F(H+L_z), F=1/ζ, H la suma de potencias superiores de 361 y L_z(s)=Σ_{p≤z}log p/p^s. Cerca de t=0 en la escala t=v/√K'', v fijo, L_z(s₀+it)∼L (el cambio relativo es O(|t|log z)), H=O(log z) por su polo simple y F→1/ζ(1/2). Por tanto B_z/L→−1/ζ(1/2). El desarrollo de K en el mismo punto es K(s₀+it)=K(s₀)−v²/2+o(1). En efecto la tercera derivada compleja de log E se acota por O(L(log z)²) sobre la vertical, por su serie absolutamente convergente y sumación parcial.

Para |t|≤1/log z, los términos k=1 de log E dan una pérdida real
Σ p^(−s₀)(1−cos(t log p)) ≫ K''t². Los restantes términos del logaritmo sólo añaden pérdida. En este tramo B_z=O(L), usando la regularidad de F en torno a 1/2 y H=O(log z). Convergencia dominada después del cambio de variable v justifica el equivalente gaussiano con la constante 1/√(2π). Para 1/log z≤|t|≤T fijo, el factor x^Φ aporta pérdida adicional de al menos exp(−aL/(2log²z)) y |E_z(s₀+it)|≤E_z(s₀). En el compacto de alturas el factor B_z es O_a(L^C): los ceros críticos están a distancia al menos s₀−1/2 y los demás ceros del compacto tienen abscisas fijas. Este segundo tramo resulta despreciable respecto del principal.

**Cierre del contorno.** Usar como en 364 una altura T con margen estricto en 1+a(1/4−T²)/2<1/2, evitando ordenadas de ceros. Horizontales y colas son despreciables: el coste del factor de Euler en Re s≥s₀ es exp(o(L)), y el margen en el exponente es fijo. Bajo la exclusión, los polos cruzados tienen Re Φ≤1/2 y Re ρ>1/2. En círculos de radio 1/L alrededor de cada uno, el logaritmo de la cota del producto finito es O_ρ(z^(1−Re ρ+o(1)))=o(L/log z), y los otros factores cuestan a lo sumo una potencia de L. Su número es finito a T fijo. Así todos los residuos juntos cuestan como máximo exp(L/2+o(L/log z)), estrictamente por debajo del sesgo calculado, incluso para Re Φ=1/2. Esto prueba el equivalente y la positividad eventual. Si existe un cero prohibido, 365 ya da valores negativos en cada bloque multiplicativo suficientemente lejano, impidiendo ese signo.

**Diferencia con los pasos anteriores.** 144 obtiene un sesgo para un promedio de Liouville. En este caso el término positivo nace del punto crítico real del producto finito de Euler, cuyo corte cambia con x. 365 exigía comparar con un techo explícito; ahora la sola desigualdad Q_a(x)>0 basta. Aún no se demuestra para a arbitrariamente próximo a cero.
