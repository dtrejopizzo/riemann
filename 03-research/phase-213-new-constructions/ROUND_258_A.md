# Pérdida óptima de los acarreos binomiales positivos en una octava

Para a,b>0 poner c(y)=⌊(a+b)/y⌋−⌊a/y⌋−⌊b/y⌋. Es el acarreo que recibe una potencia prima y en un coeficiente binomial de argumentos enteros. En cualquier octava I=[x,2x],

    ∫_I c(y)dy ≤ [1/(2 log 2)] ∫₀^∞ c(y)dy.

La constante 0.7213475… es óptima. Vale para cada núcleo individual, así que también para mezclas positivas en las que el reparto, la escala y los coeficientes se elijan conjuntamente en función de x. Admite acarreos multinomiales, por descomposición telescópica de un multinomio en binomios.

**Masa total.** Reescalar a+b=1, escribir λ=min(a,b)/(a+b)≤1/2 e I=[u,2u] en estas unidades. El núcleo vale cero o uno y se anula para y>1. Su integral es la entropía E(λ)=−λ log λ−(1−λ)log(1−λ): integrar cada piso desde ε usando ∫_ε^∞⌊t/y⌋dy=t Σ_(k≤t/ε)1/k−ε⌊t/ε⌋ y pasar al límite en la diferencia. Además λ/E(λ) es creciente, pues E−λE'=−log(1−λ)>0, y E es creciente en (0,1/2].

**Masa dentro de la octava.** Cuando u≤λ basta la longitud u. Para u>λ el acarreo es la suma de los indicadores de ((1−λ)/k,1/k], k≥1, salvo extremos irrelevantes. Si además u>1/3 sólo pueden intervenir k=1,2. La contribución conjunta tiene longitud a lo sumo λ: al duplicar la parte capturada de la banda k=2 se desplaza a la banda k=1 fuera del interior de [u,2u]. Si u≤1/3 siempre se dispone de la cota de longitud 1/3. Por tanto la masa es ≤max(λ,1/3).

Para λ≥1/3 esto da masa/E≤λ/E≤1/(2 log 2). Para 1/4≤λ≤1/3 se usa (1/3)/E(1/4)<1/(2 log 2). Falta λ≤1/4. Si u>λ, sólo intervienen (1−λ)/(2u)<k≤1/u, y el cociente de los extremos del intervalo de índices es ≤8/3. Si m es el menor índice, todos son <3m y sus longitudes suman a lo sumo λΣ_(k=m)^(3m−1)1/k≤3λ/2. Esta suma armónica decrece en m, porque al pasar de m a m+1 se pierde 1/m y se ganan tres términos cuya suma es menor. También vale la cota 3λ/2 si u≤λ. Como (3/2)(1/4)/E(1/4)<1/(2 log 2), queda demostrado el techo universal. En λ=u=1/2 se captura exactamente la longitud 1/2 y la masa total es log 2.

**Coste para el presupuesto de 257.** Para cualquier mezcla positiva B de estos acarreos, integrar fuera de I cuesta al menos κ veces lo integrado dentro, κ=2 log 2−1. Si g_x(y)=g(y/x) es el peso positivo de 257, con h=∫g, cualquier mayorante puntual B≥g_x en I cuesta al menos (1+κ)xh en masa total. Incluso sin mayoración, ||B−g_x||₁≥κxh: si A es su masa interior, el coste es ≥|A−xh|+κA. La constante es óptima para la clase de blancos positivos en una octava, por el indicador de la octava del caso simétrico. Para una representación firmada B_+−B_−=g_x con masas finitas, la parte negativa debe pagar al menos κxh: la fuga de B_+ se cancela fuera y su masa interior ya es ≥xh.

Por tanto obtener el presupuesto xh+O(√x) mediante mayoración positiva punto a punto y uso del coste factorial total es imposible aun con repartos adaptativos. Sigue disponible una estrategia que controle aritméticamente y reste los aportes exteriores; la barrera cuantifica lo que esa resta debe recuperar. El enunciado se refiere a integrales en la variable continua de potencia prima. No impone ese coste a una desigualdad que se justifique sólo en los primos con otra información aritmética.

**Antecedente.** Selección 099 descartó representar log t exactamente con dilataciones positivas de una distribución fija de repartos y dejó abierta la mayoración adaptativa. Aquí se resuelve la cuestión local de coste para cualquier blanco positivo soportado en una octava por un argumento geométrico sin ceros de ζ. La desigualdad original de 257 permanece abierta.
