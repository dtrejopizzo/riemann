# Precisión crítica de los pesos en los primos reales

La energía de 162 y su versión gaussiana de 166 toleran cualquier error relativo O(p^(−1/2)) en el peso log p. En cambio para cada 1/2<β<1 existen cambios relativos O(p^(β−1)), en los mismos primos y nulos en un prefijo arbitrario, que conservan las estimaciones de conteo y criba de pares de 163–165 pero cuyo promedio gaussiano viola el techo de 166. Es una obstrucción a deducirlo sólo de esas estimaciones. No se infiere un contraejemplo para los pesos exactos.

**Estabilidad.** Si |f(p)−1|≤C p^(−1/2), la diferencia en S(x) es O(√x) por K acotado, p≤exp(A)x y Chebyshev con sumación parcial. La diferencia en F(t) es O(exp(t/2)) por convolución. En ambos criterios bilaterales de energía el techo para un peso implica el del otro por la desigualdad triangular en L². Esto vale sin suponer el techo para ninguno de ellos.

**Perturbación aritmética.** Fijar P grande, 0<ε<1/2 y τ>0, y poner f(p)=1 hasta P, y f(p)=1+εp^(β−1)cos(τ log p) después. Se puede elegir τ por encima de cualquier altura prescrita de modo que ζ(β+iτ)≠0 y B(β+iτ)≠0, al excluir conjuntos discretos. Extender f a una función completamente multiplicativa positiva. Incluso se conserva la identidad de convolución (fΛ)*f=f log, término a término por Σ_{l|n}Λ(l)=log n. Esta es la identidad torcida, distinta del caso exacto f=1.

El cambio en θ(x) es O(x^β) por Chebyshev. Tanto los pares como la diagonal siguen en los mismos primos con pesos positivos comparables, y el peso relativo tiende a uno en los intervalos macroscópicos. Así se mantienen el coeficiente principal de la diagonal y los límites macroscópicos de 162, los casilleros y la criba bilateral de 165 (la cota de productos negativos usa sólo comparabilidad). El techo incondicional de la suma suavizada en 164 también admite una perturbación O(x^β).

**Efecto observable.** Sea D(s)=Σ_p log p p^(−s). Para la suma prima modificada el factor D del Mellin pasa a
    D(s)+(ε/2)[D(s+1−β−iτ)+D(s+1−β+iτ)]+entera,
donde la entera retira el prefijo. En s=β+iτ hay un polo simple de residuo ε/2, pues D tiene residuo uno en 1 y es regular en 1+2iτ por ausencia clásica de ceros en Re s=1. La continuación en los puntos usados sale de −ζ'/ζ quitando las potencias superiores, como en 153. Tanto B como el multiplicador gaussiano son no nulos en ese punto. Si el modelo cumpliera 166, la interpolación allí demostrada implicaría holomorfía del Mellin en Re s>1/2, contradicción. Esto prueba el fallo para el modelo individual sin asumir nada sobre la energía de los pesos originales.

La diferencia respecto de la suma original admite además la expresión incondicional
    S_f(x)−S(x)=ε Re[B(β+iτ)x^(β+iτ)]+o(x^β).
En efecto usar PNT escalado en p/x con perfil t^(β−1+iτ)K(1/t), continuo hasta cero por el decaimiento de 160 y de soporte acotado. La integral es B(β+iτ) por Mellin. El tamaño de la desviación no procede de un cambio en el conjunto de primos ni de un error en el conteo de saltos individuales.

**Decisión de ruta.** El teorema B de R167_102_SIEVE_CONSTRUCTION ya modulaba Λ por un coseno para mostrar límites de la criba. Aquí la amplitud decrece, conserva PNT y un prefijo arbitrario, y se obtiene el fallo específico de 166. Las rondas 135–137 ya construían contramodelos para observables de Möbius; aquí se conserva el soporte primo verdadero y se localiza el umbral de estabilidad de la energía de 162/166. La estimación de criba sobre pares puede cerrar el tamaño del bloque cercano y aun así admitir esta oscilación. Un cierre por esta vía necesita una propiedad que use la normalización aritmética exacta o excluya directamente tales oscilaciones. Este resultado no verifica el techo en ningún bloque adicional de la suma original.
