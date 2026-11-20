# Un único coseno al variar el intervalo, y una subsucesión de falsos negativos

Para x≥1 sea F(x)=Σ_(x<p≤2x)(log p) cos(2πp/x), sólo sobre primos. Poner t=log X, 0<h(t)≤1 con log(1/h)=o(log t) y

    J(X,h)=X⁻²∫_X^(X exp h) F(x)² dx.

Entonces log(1+J(X,h))/log X→2B. A diferencia de 235 la frecuencia y la componente real son fijas. Lo que se controla en una subsucesión es la energía cuando el inicio del intervalo se mueve, no una muestra sola. De hecho, si falla RH existen infinitos enteros n con |F(n)|≪log n, además de excursiones de ambos signos mayores que n^(1/2+δ) para algún δ>0. Así una prueba que sólo encuentre un valor pequeño por escala elegida no distinguiría un fallo del signo.

**El coseno conserva los polos relevantes.** Su multiplicador H(s)=∫₁² y^(s−1)cos(2πy)dy es entero y H(1)=0. Para 1/2≤Re s≤1, dos integraciones por partes, usando que la derivada del coseno se anula en ambos bordes, dan

    |s H(s)−(2^s−1)| ≤ 16π²/|s+1|.

Como |2^s−1|≥√2−1, H no se anula en esa tira para |Im s|≥400. Todos los ceros a la derecha de la línea están por encima de ese umbral en altura absoluta por Z2 de 47. Así no se necesita elegir un armónico que dependa del cero.

**Promedio ordinario.** Fijar ρ₀ con β₀>1/2 y σ entre 1/2 y β₀. Usar el f_t de 231 en [0,h], de masa uno, que elimina todos los otros ceros con β≥σ y tiene normas hasta dos derivadas exp(o(t)). Aplicado a la suma análoga F_ψ de potencias primas, el funcional ∫ f_t(v)exp(−ρ₀(t+v))F_ψ(exp(t+v))dv da

    −mult(ρ₀)H(ρ₀) + O(exp(−(β₀−σ)t+o(t))).

En efecto en la fórmula explícita para dψ la integral sobre la ventana [x,2x] contra el coseno multiplica cada término −x^ρ por H(ρ); la densidad dx da xH(1)=0. Es legítimo hacer el cálculo distribucional: integrar primero en v suaviza los dos bordes del coseno truncado, y la transformada del test es el producto de H por la transformada de f_t desplazada. Esta última tiene decaimiento cuadrático uniforme salvo el factor exp(o(t)), mientras H está acotada en la tira crítica por su integral. Ello permite sumar absolutamente con Z3. Los términos triviales de la fórmula explícita cuestan O(exp(−β₀t+o(t))) o menos. Retirar las potencias superiores cuesta O(exp((1/2−β₀)t+o(t))) tras normalizar. El límite no nulo y Cauchy–Schwarz implican J(X,h)≥X^(2β₀−1−o(1)). Para el techo usar θ(y)−y=O_ε(y^(1/2+B+ε)) de 235 y sumación parcial en una ventana diádica; el continuo da cero y el coste de la derivada del coseno es O(1). Tomar el supremo sobre β₀, con el piso trivial si B=0.

**Obstrucción a usar datos puntuales.** Para Re s>1 el Mellin unilateral de F es exactamente H(s)Σ_p(log p)p^(−s), por x∈[p/2,p] y p≥2. En Re s>1/2 la serie prima continúa como −ζ'/ζ(s) menos la serie absolutamente convergente de potencias de orden ≥2. El producto es regular en todo punto real de ese semiplano: la singularidad en 1 se cancela y no hay ceros reales allí. Tiene un polo en cada cero derecho por el cálculo de H. Sea 1/2<a<β₀. Si F(x)≤x^a eventualmente, el Mellin de x^a−F(x), tras retirar un prefijo compacto, es el de una función no negativa y meromorfa en el semiplano considerado. Landau obliga a una singularidad real en la abscisa de convergencia, que es ≥β₀ por el polo no real y finita por Chebyshev. Allí la expresión 1/(s−a)−H(s)Σ_p(log p)p^(−s) es regular. Contradicción. El mismo argumento para x^a+F(x) da la otra excursión. La conclusión vale arbitrariamente lejos con ambos signos.

En x∈[n,n+1] las entradas y salidas cuestan O(log n) por conteo de enteros en los bordes; el cambio de las fases restantes cuesta O(1) por Chebyshev y la cota O(1/n) para la derivada de cada fase. Por ello hay también excursiones enteras de ambos signos (reduciendo ligeramente a) y |F(n+1)−F(n)|≪log n. Cada cruce entre signos da un entero con |F(n)|≪log n. Esto no garantiza una muestra pequeña en cada intervalo de anchura prefijada ni que el entero sea primo.

**Decisión.** El promediado sobre inicios en 236 y la búsqueda en varios armónicos en 235 son dos maneras distintas de evitar cancelaciones. En la primera, el problema restante es un techo X^o(1) para J(X,h) en alguna sucesión de VENTANAS. No usar una subsucesión puntual pequeña de F como sustituto.
