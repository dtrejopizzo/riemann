# Un mismo conteo suavizado con ajuste creciente en dos escalas casi lineales

Fijar una sola densidad W: convolución de las probabilidades uniformes en [0,1/(10j²)] para todos los j≥1. Sea H(s)=∫W(v)exp(sv)dv y formar con los primos auténticos

    A(t)=Σ_p (log p) W(log p−t) − exp(t) H(1).

Es una suma local finita. Fijar m=floor(t/(log t log log t)) para t grande y medir

    D(t,h)=exp(−t) inf_(deg P≤m) ∫₀ʰ |A(t+v)−P(v)|²dv,

sobre polinomios reales en v. Para el MISMO W y el MISMO grado m(t) se obtienen:

1. Si 0<h≤1 y log(1/h)=o(log t), entonces log(1+D(t,h))/t→2B.
2. Si h=exp(−log t log log t), se tiene D(t,h)≤exp(−t+o(t)) para TODO t grande sin hipótesis.

Con X=exp(t), la segunda longitud física es X(exp(h)−1)∼X/(log X)^(log log log X), de orden X^(1−o(1)). Por tanto incluso la descripción «ventana de longitud X^(1−o(1)) con error pequeño» no basta para este ajuste; importa cuánto vale h. Este observable suavizado y su ajuste de grado creciente son distintos del coseno sin ajuste de 238.

**Núcleo fijo.** Las longitudes a_j=1/(10j²) son sumables y dan una probabilidad de soporte compacto en [0,1/5]. Para controlar la derivada de orden r, derivar los primeros r factores (variación ≤2/a_j cada uno), acotar en supremo el siguiente por 1/a_(r+1) y dejar las demás probabilidades sin derivar. Sale ||W^(r)||∞≤C^(r+1)((r+1)!)². Derivar un factor adicional justifica los representantes suaves. Además H(s)=∏(exp(sa_j)−1)/(sa_j) no se anula para Re s>0: ningún factor se anula y la cola difiere de uno por una sucesión absolutamente sumable a s fijo. El principal continuo de la suma prima es exactamente exp(t)H(1).

**Por qué sigue detectando ceros tras retirar tantos coeficientes.** Si B>0 fijar β₀=Re ρ₀>1/2 y σ entre 1/2 y β₀. Construir como en 231 un filtro base de masa uno soportado en [0,h/2], anulando los otros ceros de β≥σ en ρ−ρ₀. Sus normas hasta dos derivadas cuestan exp(o(t)) en el régimen 1. Convolucionar además m+1 copias de

    (δ_l−exp(−ρ₀ l)δ₀)/(1−exp(−ρ₀ l)),    l=h/[4(m+1)].

Cada una tiene masa uno, variación O_(ρ₀)(1/l) para t grande y cero en −ρ₀. El coste total nuevo es exp(O(m log((m+1)/h)))=exp(o(t)). El filtro final f_t conserva masa, soporte dentro de [0,h] y la cota exp(o(t)) para sus normas de orden ≤2 y su norma L². Su transformada tiene un cero de orden ≥m+1 en −ρ₀. Por derivación esto da ∫f_t(v) exp(−ρ₀v)P(v)dv=0 para TODOS los polinomios de grado ≤m, incluidos los elegidos a partir de los datos.

Aplicar la fórmula explícita para dψ como en 236. La convolución logarítmica por W multiplica el término de cada cero por H(ρ), uniformemente acotado en la tira. El principal se ha restado. El filtro en v, con el factor exp(−ρ₀(t+v)), deja −mult(ρ₀)H(ρ₀)≠0. Los ceros β<σ cuestan exp(−(β₀−σ)t+o(t)) por partes dos veces y Z3. Los términos triviales y las potencias primas superiores también desaparecen tras la normalización: estas últimas cuestan antes del filtro O(exp(t/2)poly(t)) por soporte fijo y acotación de W. Cauchy–Schwarz, uniformemente en P, da D(t,h)≥exp((2β₀−1)t−o(t)). Para el techo tomar P=0 y usar θ(x)−x=O_ε(x^(1/2+B+ε)) de 235 por partes con el W fijo. Esto incluye B=0 y concluye 1 sin suponer que el supremo se alcance.

**Cota directa en las ventanas buenas.** En [t,t+1], Chebyshev sobre el soporte fijo da para cada r la cota |A^(r)|≤exp(t) C^(r+1)((r+1)!)², aumentando C por el principal restado. Tomar como P el Taylor en t de orden m. El logaritmo del supremo del error en [0,h] es ≤ t+(m+1)log h+O((m+1)log(m+2)). Para el h del apartado 2, (m+1)log(1/h)=t+o(t) y m log m=o(t). El error es ≤exp(o(t)), luego D≤exp(−t+o(t)). Es una cota de aproximación por suavidad, no una demostración de cancelación de los primos en la primera escala.

**Parámetro opcional.** En ambas cuentas se puede sustituir log log t por cualquier ω(t)→∞ con ω(t)log t=o(t), usando m=floor(t/(ω(t)log t)) y h=t^(−ω(t)) en 2. La prueba de 1 se mantiene para h=t^(−o(1)). Cada elección fija una regla de grado para ambos enunciados; no se cambia de regla después de examinar los datos. La zona intermedia, en particular h=t^(−c) con c>0 fijo para la detección de cualquier desplazamiento por este argumento, no queda resuelta.
