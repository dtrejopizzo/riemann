# Criterio con dos factores de tamaño próximo a la raíz

En 048, el coeficiente positivo de los primos depende del centro del logaritmo. En el criterio alternado se puede usar log k a escala y=2x y log(2k) a escala x, porque Σg(k/y)=V(1/y)=0 y análogamente en x. Con cortes físicos coordinados, los integrandos altos se corresponden por dilatación. El factor adicional log K en la cota de cuadratura se absorbe aumentando la constante del corte. En la suma inferior desaparece entonces k=1 y con él todos los primos de la banda. Para n=2p con p primo grande el coeficiente pasa a ser +log 2. Así la obstrucción a sumar partes positivas sigue presente en este centro, aunque los primos ya no aportan.

**Paso adicional.** Se puede eliminar simultáneamente todo k≤√x del criterio, manteniendo el segundo factor m en torno a √x. Se usa el peso fijo V con cotas de Gevrey de orden dos de 047, su inverso g, y la misma función de corte χ. Para x=j⁴ grande poner y=2x, L=floor(√x) y K=A(2L) (log x)² con A constante suficientemente grande. Escribir a(k)=(−1)^(k+1)log k. Para d≤L poner b_d=−(μ*a)(d), donde * es convolución de divisores. Para L<d≤2L poner b_d=λ con

    λ=−(Σ_{d≤L} b_d/d)/(Σ_{L<d≤2L}1/d),

y poner b_d=0 en el resto. Definir c(k)=Σ_{d|k} b_d, y U(k)=1−χ(log(k/K)). Entonces el signo global equivale a que exista C tal que, eventualmente,

    Σ_{L<k<eK} Σ_{a₀ y/k≤m≤B y/k} U(k)[a(k)+c(k)] μ(m)V(km/y) ≤ C√x,

donde [a₀,B]=[1/16,16e]. En esta suma ambos factores son al menos constante por √x/(log x)² y a lo sumo constante por √x (log x)². La cantidad de índices exteriores crece respecto de 048; se gana una cota superior para los dos factores a la vez.

**Coeficientes.** La identidad μ*log=Λ y la parte par de a dan exactamente

    (μ*a)(d)=Λ(d)−2·1_{2|d}(Λ(d/2)+(log 2)1_{d=2}).

De aquí Σ_{d≤L} b_d/d=log 2−Σ_{L/2<n≤L}Λ(n)/n para L≥2. Chebyshev da |λ|=O(1), y Σ|b_d|/d=O(log x). En la banda k<eK, la suma de los módulos de los b_d para d≤L que dividen k es O(log(2k)) por la identidad de divisores. Para L<d≤2L hay a lo sumo k/L divisores porque sus cocientes son distintos. Así los coeficientes a(k)+c(k) son O((log x)²) en el soporte. Para k≤L se anulan exactamente por inversión finita.

**Prueba del traslado.** La suma entera Σ a(k)g(k/y) es 2A(x)−A(2x) con A(x) la discrepancia de 048: el término extra al desplegar la parte par es un múltiplo de V(1/x)=0. Añadir c(k) cuesta exactamente cero, pues para d≤2L se tiene Σ_{d|k}g(k/y)=V(d/y)=0. Resta verificar que la parte superior con 1−U tiene tamaño O(√x).

Para a, separar la malla completa y la par. Las integrales correspondientes se cancelan porque la segunda se toma al doble del paso con coeficiente −2, evaluando toda la función (incluido log k) en la misma variable física. La estimación de 047 cuesta O(y(1+log K)exp(−c√(K/2))) al reemplazar las dos sumas superiores por integrales; el incremento log K se obtiene separando log k=log(k/K)+log K en la prueba de 047.

Para c, la progresión k=dv usa escala y/d y corte K/d en la estimación de 047 sin el logaritmo (sus cotas de derivadas sólo mejoran). El error de suma menos integral es a lo sumo C(y/d)exp(−c√(K/d)), uniforme en d≤2L. Su integral en v es (1/d) veces la misma integral en k para todas las progresiones. Al sumarlas desaparece por Σ b_d/d=0. El error total es O(y log x exp(−c√(K/(2L))))=O(√x) eligiendo A suficientemente grande. Queda la parte inferior del enunciado al desarrollar g, y la equivalencia se sigue de la recuperación de 048.

**Alcance y antecedentes.** Las identidades de Vaughan y sumas bilineales de tipo II ya aparecen en fase 104, 104_93, y en fase 211, ROUND_013_A §3 y REVIEW_009. No se reclama novedad para descomponer por divisores ni para el método de bilineales. El cotejo dirigido distingue el uso de filas exactamente nulas sobre las muestras de 048, con compensación de densidad que cancela la integral de todas las progresiones, para dejar sólo pares de tamaño próximo a √x. La desigualdad firmada sobre esos pares permanece abierta. No se ha obtenido una estimación de tipo II a precisión de raíz.
