# Dominio impar incondicional en un rango creciente de capas

Sea S^*(x;z) el pulso de paridad de 368, L=log x y u=L/log z. Para x suficientemente grande hay **signo negativo incondicional**, uniformemente en

    2 ≤ u ≤ L^(1/4),   es decir,   exp(L^(3/4)) ≤ z ≤ √x.

Es el mismo peso gaussiano fijo y el mismo coeficiente de Möbius. El corte final z=L² corresponde a u=L/(2 log L), fuera del rango. La regla de signo del modelo continuo es exactamente la derivada de la función clásica de Dickman; el punto aquí es controlar el error aritmético del pulso al crecer el número de capas.

**Cálculo continuo.** Escribir f(t)=1_{t≥1}/t. Al reemplazar cada primo por la medida dq/log q y poner t=log q/log z, ésta se transforma en z^t f(t)dt. El producto de k factores da la densidad z^t f^{*k}(t)/k!, con signo (−1)^k, en la variable del producto. Para t finito la serie D(t) de densidades con signo es finita porque f tiene soporte en [1,∞). Si ρ(t)=1+∫₀^t D(v)dv, la simetría de las k copias da t f^{*k}=k(tf)*f^{*(k−1)}, con f^{*0} masa unidad en cero. Por tanto ρ=1 en [0,1] y

    t D(t)=−ρ(t−1)   para t>1.

La identidad tρ(t)=∫_{t−1}^t ρ(v)dv para t≥1 sigue por derivación y continuidad en 1. Impide un primer cero, luego ρ>0 y decrece. También ρ(t)≥ρ(t−1/2)/(2t), integrando sólo la primera mitad. Iterar muestra ρ(t)≥exp(−C(t+1)log(t+2)). Así la suma de capas continua tiene signo negativo en todo t>1, incluso donde una capa individual no determina el signo.

**Transferencia desde los primos.** Sea g(w)=exp(w/2)φ₁(w). Truncar el pulso real en n≤x² cuesta O(x exp(−cL²)) por el decaimiento gaussiano, agrupando por intervalos logarítmicos unitarios. El término n=1 también es de ese orden. Los enteros restantes tienen k≤K=⌊2u⌋ factores >z. Escribir la suma sobre primos ordenados y dividir por k!, retirando por ahora la exigencia de primos distintos. El error en n≤x² es O(xL/z): cada entero repetido tiene peso combinatorio ≤1 y algún p²|n con p>z, mientras g(log(x/n))≤C x/n. Sumar armónicamente primero los múltiplos de p². Completar los sumatorios de cada primo hasta B≥x² con log B=2L+O(1), aun cuando el producto supere x², cuesta a lo sumo la cola gaussiana anterior, ya que el peso 1/k! de las ordenaciones de cada entero suma ≤1.

Elegir log B como primer extremo ≥2L de una malla en log q de paso Δ=exp(−L^(1/3)) iniciada en log z. El teorema clásico de los primos con error O(q exp(−c√log q)) da, en cada celda, el número de primos igual a la integral dq/log q con error relativo O(exp(−c' L^(1/3))). En efecto log q≥L^(3/4), y al dividir por la masa de la celda sólo se pierde O((log q)/Δ). En una caja de k celdas el logaritmo del peso g varía O((1+KL)KΔ), por su derivada logarítmica. Por positividad, reemplazar las medidas en cada capa tiene entonces error relativo O(exp(−c'' L^(1/3))) para sus masas sin signo. No se multiplica el error por el número de cajas: se suman cotas relativas contra las masas. La masa aritmética total sin signo es O(x), por comparación con todos los enteros y suma gaussiana; por tanto el error firmado total es O(x exp(−c'' L^(1/3))).

En la integral resultante, para t≤2u los cortes individuales q≤B y k≤K no afectan a la densidad D(t). Para t>2u el coste es O(x exp(−c L²)u), pues z^t g(L−t log z) tiene ese techo sin el factor u y la masa de las convoluciones truncadas sin el factor z^t es ≤exp(∫₁^{log B/log z}dv/v)=O(u). En [1,2u] la densidad firmada es negativa. Basta integrar sobre u≤t≤u+1/log z: allí z^t≥x, g está acotada inferiormente, y la fórmula para D da una contribución en módulo al menos

    (x/log z) exp(−C(u+1) log(u+2)).

Para u≤L^(1/4) este piso domina todos los errores anteriores. Así se obtiene el signo para los enteros auténticos sin ninguna hipótesis sobre RH.

**Límite cuantitativo.** En el corte objetivo u=L/(2 log L), el desequilibrio continuo puede ser muchísimo menor que la precisión relativa de la sustitución por dq/log q. La positividad de ρ sola no justifica el signo discreto allí. Se necesita controlar la diferencia firmada entre capas o encontrar una recurrencia discreta que preserve la desigualdad.
