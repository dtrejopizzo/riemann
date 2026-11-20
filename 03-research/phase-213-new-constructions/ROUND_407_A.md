# Quitar un par crítico del promedio conservando pesos positivos

**Estado: PROVED, con revisión independiente de la paridad, la ecuación diferencial y la varianza.**

Fijar γ>0 con ξ(1/2+iγ)=0 verificado, y usar la normalización Φ de 406. El multiplicador

    U(s)=ξ(s)/(1+(s−1/2)²/γ²)

es la transformada bilateral centrada de un núcleo par estrictamente positivo Φ_γ. Tiene igual masa que Φ y su varianza normalizada es exactamente menor en 2/γ². El promedio negativo de 406, incluida la truncación indicada allí, subsiste con Φ_γ. El resultado utiliza un solo par, sin presuponer la ubicación de los demás.

**Construcción real.** Para v≥0 tomar Φ_γ(v)=γ∫₀^∞ Φ(v+t)sin(γt)dt y extender por paridad. Usamos la monotonía estricta clásica de Φ en el semieje positivo; también se deduce de la convexidad de Φ(√t) y su límite cero. [Csordas, Convexity and the Riemann zeta-function](https://web.math.pmf.unizg.hr/glasnik/33.1/33105.pdf). Emparejar dos semiperíodos consecutivos del seno da una integral positiva por la diferencia Φ(v+t)−Φ(v+t+π/γ). La derivada en cero vale −γ²∫₀^∞Φ(t)cos(γt)dt=0 por el cero verificado. Así la extensión par es C² y diferenciando la integral se obtiene Φ_γ''+γ²Φ_γ=γ²Φ en toda la recta. Por la cola doblemente exponencial, integrar por partes demuestra la identidad de transformadas, incluso en los puntos removibles por continuación. En s=1/2 el cociente conserva la masa. Su segunda derivada dividida por dicha masa resta 2/γ² al segundo momento, que coincide con la varianza por paridad.

**Aplicación al pulso.** Tras multiplicar F=1/ζ, el cociente que queda en la integral de 406 es s(s−1)π^(−s/2)Γ(s/2)/(2(1+(s−1/2)²/γ²)). Sus dos posibles polos están en Re s=1/2, estrictamente a la izquierda de α. Sobre α≤Re s≤1+1/L el inverso del denominador cuesta O_γ(b) por la distancia α−1/2≍1/b a los dos polos, y a grandes alturas decae. En la silla real el nuevo factor relativo tiende a uno. Esto conserva el equivalente −ξ(1/2)T₀ sin RH, con la misma dominación de 367. El coste de truncación sigue siendo despreciable por Φ_γ(v)≤γ∫₀^∞Φ(|v|+t)dt y la cota de 406. La reducción cuantificada es en varianza, no en la longitud garantizada de la ventana de 406.

**Registro de revisión.** El [teorema2.1(v) de Csordas](https://hrcak.srce.hr/en/file/12426) afirma directamente la monotonía estricta; su normalización se relaciona con la de406 por Φ(v)=2Φ_Csordas(v/2), así que el signo se conserva. La anulación crítica da ∫₀∞Φ(t)cos(γt)dt=ξ(1/2+iγ)/2=0 y, por tanto, Φ_γ'(0)=0. La ecuación Φ_γ''=γ²(Φ−Φ_γ) hace coincidir las segundas derivadas de la extensión par; por regularidad de la ecuación es incluso suave. Integrar dos veces por partes con el exponente centradow=s−1/2 produce(w²+γ²)U=γ²ξ, confirmando el signo más del denominador. Enw=0 la segunda derivada resta exactamente2ξ(1/2)/γ², es decir2/γ² a la varianza normalizada.

El producto F·U puede conservar polos simples en1/2±iγ, aunque la división sea removible enU. Ambos están estrictamente a la izquierda deα; no se los cruza al bajar desde1+1/L. En esa franja el inverso del denominador es O_γ(b) y sólo produce un factor polinómico absorbible por la pérdida de fase. La cola deΦ_γ y sus primeras derivadas permite la misma truncación de406, a corte congelado.

**Obligación para iterar.** La positividad de Φ_γ está demostrada. Para volver a aplicar el mismo argumento de semiperíodos a otro cero haría falta justificar, por ejemplo, que Φ_γ sigue siendo decreciente en todo el semieje. La fórmula anterior no lo establece. [408](ROUND_408_A.md) resuelve esa obligación para una selección de ceros suficientemente altos, sin demostrar concentración. Tampoco se convierte la negatividad del promedio en negatividad puntual.
