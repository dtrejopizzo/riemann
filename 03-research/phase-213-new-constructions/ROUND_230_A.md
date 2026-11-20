# La media cuadrática en cualquier intervalo de razón fija detecta el desplazamiento completo

Para cada c>1 fijo, B=sup_ρ |Re ρ−1/2|, se cumple

    lim_(X→∞) log(1+∫_X^(cX) (ψ(x)−x)² dx/x²)/log X = 2B.

El intervalo puede ser [X,2X], o [X,1.01X]. A diferencia de 229 la longitud en logaritmos es constante. Basta un techo X^o(1) en una subsucesión para un solo c fijo. La constante implícita del piso depende del cero escogido y de c; el argumento no permite enviar c a uno con X.

**Un filtro de soporte arbitrariamente corto.** Sea ρ₀=β₀+iγ₀ un cero con β₀>1/2, y fijar 1/2<σ<β₀. Para H=log c construir una función compleja suave f de soporte en [0,H], integral uno, con

    ∫ f(v) exp((ρ−ρ₀)v)dv = 0

para todo valor distinto ρ con Re ρ≥σ. La multiplicidad se contará luego en la fórmula explícita. Usamos la estimación incondicional de Ingham N(σ,T)≪ T^[3(1−σ)/(2−σ)] log⁵T. El exponente es estrictamente menor que uno, por lo que la suma de 1/|γ−γ₀| sobre esos ceros en la cola converge por sumación diádica. Se incluyen ordenadas negativas por simetría.

Para cada cero de la cola tomar h=π/|γ−γ₀| y una probabilidad sobre {0,h} cuyo cociente entre el peso en h y el peso en cero es exp(−(β−β₀)h). Su integral exponencial en ρ−ρ₀ es cero. Tomando la cola suficientemente alta, la suma de los h es menor que H/3. La convolución infinita existe como ley de la suma de variables independientes en esos intervalos: la serie converge absolutamente para cada elección de puntos. Es una probabilidad soportada en [0,H/3]. En cada exponente que se desea anular, todos los productos parciales desde su factor dan cero y el paso al límite vale por soporte compacto.

Quedan finitos ceros con Re ρ≥σ distintos de ρ₀. Para cada w=ρ−ρ₀≠0 elegir h>0 tan corto que la suma de sus longitudes sea menor que H/3 y exp(wh)≠1. La medida (δ_h−exp(wh)δ₀)/(1−exp(wh)) tiene masa uno y anula w, incluso si los dos ceros tienen la misma ordenada. Su variación puede ser grande pero es una constante fija. Convolucionar todos los factores con una función suave de masa uno soportada en (0,H/3). Resulta f con las propiedades indicadas. Su transformada en w decrece como cualquier potencia inversa de 1+|Im w| uniformemente para |Re w|≤1, por integración por partes.

**Extraer un solo residuo en toda banda.** Escribir t=log X, E(x)=ψ(x)−x. Aplicar la fórmula explícita de von Mangoldt en la variable s=t+v contra el test f(v)exp(−ρ₀(t+v)). La identidad distribucional para s>0 es E(exp s)=−Σ_ρ exp(ρs)/ρ−log(2π)−(1/2)log(1−exp(−2s)); el convenio en un salto no influye. Tras suavizar, la suma es absolutamente convergente por el decaimiento anterior y Z3. Todos los ceros a la derecha de σ, incluida la frontera salvo el objetivo, desaparecen. Los restantes contribuyen O_f(exp(−(β₀−σ)t)), al sumar los transformados en valor absoluto. El término constante y los ceros triviales cuestan O_f(exp(−β₀t)). Por tanto

    ∫ f(v) exp(−ρ₀(t+v)) E(exp(t+v))dv → −mult(ρ₀)/ρ₀ ≠ 0.

Cauchy–Schwarz acota el módulo del integral por C_f exp(−(β₀−1/2)t) veces la raíz de ∫_X^(cX) E(x)²dx/x². Se deduce un piso ≥c_(ρ₀,H) X^(2β₀−1) en cada intervalo suficientemente alto. Por simetría se puede aproximar 1/2+B por tales β₀ si B>0, sin suponer que el supremo se alcanza. El techo viene de la inclusión dentro de [(cX)^(1/2),cX] y 229. Si B=0 el piso requerido es trivial por el 1 del enunciado.

**Alcance y antecedentes.** 229 sólo dio bandas de potencias; su argumento de concentración no permitía un intervalo de razón fija. El filtro usa escasez de ceros en cada semiplano estrictamente a la derecha de la línea, no finitud del total de blancos. La estimación de densidad ya consta en la fase 36, documento 104. La prueba no calcula f a partir de primos ni evalúa el techo en bandas diádicas. No se reclama prioridad de esta consecuencia en la teoría de oscilaciones del error primo. [Estimación de densidad utilizada](https://arxiv.org/abs/2507.15184).
