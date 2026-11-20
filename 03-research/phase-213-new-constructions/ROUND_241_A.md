# Prueba discreta con pesos binomiales y sin término continuo

Usar W y H de 240. Para u real definir S(u)=Σ_p(log p)W(log p−u). Poner r=1+floor(t/(log t log log t)), d=h/(2r), 0<h≤1 y log(1/h)/(log t log log t)→λ≥0 finito. Para evitar cualquier alias espectral en la lectura de los datos, en la prueba se usará G=t(log t)^3 y **se fija el paso efectivo** δ=min(d,1/(4G)). Sea E el desplazamiento por δ. Con 2r+1 valores equiespaciados de S formar

    K(t,h)=exp(−t/2) max_{0≤k≤r} |(E−exp(δ))^r S(t+kδ)|.

Entonces log(1+K)/t→max(B−λ,0). El dato es sólo una suma finita sobre primos para cada k; el operador usa pesos binomiales explícitos. Los nodos quedan en [t,t+h]. Para λ=0 el recorte del paso puede concentrarlos en una ventana menor. Siempre r log(1/δ)=λt+o(t).

**Techo.** La media continua exp(u)H(1) se anula exactamente. En la expansión de 240 el error de potencias primas y términos menores cuesta tras la diferencia a lo sumo (1+exp(δ))^r exp(t/2)poly(t)=exp(t/2+o(t)). Para los modos de ceros el multiplicador es (exp(ρδ)−exp(δ))^r, de módulo ≤(δ exp(δ)|ρ−1|)^r por integración sobre el segmento de 1 a ρ. El momento absoluto de H de orden r cuesta exp(O(r log(r+2))) según 240. Esto da el techo exp((1/2+B−λ)t+o(t)) para la parte de ceros.

**Piso cuando λ<B.** Elegir ρ₀, σ como en 240 con 1/2<σ<β₀−λ. Aplicar a la sucesión diferenciada el polinomio adicional

    L(E)=∏_{ρ distinto de ρ₀, Re ρ≥σ, |Im ρ|≤G} (E−exp(ρδ))/(exp(ρ₀δ)−exp(ρδ)),

con un factor por cero distinto. Su grado M≤t^(q+o(1)) con q<1 es menor que r para t grande. Sus coeficientes tienen norma ℓ¹≤exp(o(t)): cada denominador es ≥cδ|ρ−ρ₀|≥c(ρ₀)δ, pues |(ρ−ρ₀)δ|<1/2 y ρ₀ es fijo y aislado. El numerador tiene norma ≤1+exp(δ). Así M log(1/δ)=o(t). L vale uno sobre el modo elegido y elimina los otros modos enumerados. La contribución elegida tiene módulo exp((β₀−λ)t+o(t)), ya que H(ρ₀)≠0 y |exp(ρ₀δ)−exp(δ)|/δ→|ρ₀−1|>0. Los ceros bajos de parte real menor que σ cuestan ≤exp(σt+o(t)) usando las normas de coeficientes de ambos operadores; el error de potencias cuesta ≤exp(t/2+o(t)). La cola de ceros por encima de G lleva el factor exp(−cG/log²G). Todas estas cotas son menores exponencialmente que el término elegido. Como L sólo lee los primeros M+1 términos y tiene norma exp(o(t)), alguno de los residuos observados alcanza exp((β₀−λ)t−o(t)). Tomar supremo sobre β₀. Para λ≥B basta K≥0.

**Uso aritmético.** Fijar λ=0 y, por ejemplo, h=1. Bastaría encontrar inicios arbitrariamente grandes en los que las r+1 sumas binomiales sobre primos sean todas ≤exp(t/2+o(t)) en módulo. El filtro L depende del espectro sólo en la demostración; el test K se calcula sin conocer un solo cero. El máximo simultáneo es esencial en esta prueba. Un cruce por cero de una sola de las sumas no proporciona la cota del bloque. Respecto a 240 se eliminaron el intervalo continuo de observaciones, el ajuste óptimo y la sustracción numérica del principal.

**Simplificación para el objetivo global.** En el caso λ=0 y h=1 alcanza la PRIMERA diferencia, incluso con el mismo exponente exacto B. En efecto, en el techo anterior reemplazar el orden r por 1, conservando r como número de pasos observados. En el piso L sigue teniendo grado ≤r, mientras que el multiplicador del cero elegido tiene módulo comparable a δ=1/(4G)=exp(−o(t)); para todo β₀>1/2 basta elegir 1/2<σ<β₀. El argumento da log(1+exp(−t/2)max_(k≤r)|S(t+(k+1)δ)−exp(δ)S(t+kδ)|)/t→B. Así la estimación pendiente para el signo puede formularse usando sólo diferencias consecutivas de dos conteos con pesos positivos. Por telescopado equivale en exponente a controlar la oscilación en la malla de exp(−kδ)S(t+kδ), pues r=exp(o(t)) y rδ≤1.
