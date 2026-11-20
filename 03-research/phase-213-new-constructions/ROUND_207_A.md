# Una sola diagonal de POWER con tasa variable: intervalo exacto de detección

Usar únicamente F(s)=s^N/(s+u)^(2N), N≥1. Para u>1/2 poner b_N(u)=(4u²)^N W(f). El signo global del paper 47 equivale a cualquiera de estas obligaciones: para cada tasa racional u>1/2, (i) limsup_N |b_N(u)|^(1/N)≤1, o (ii) W(f)≥0 para todo N suficientemente grande (umbral dependiente de u). La primera condición admite cotas subexponenciales, aun sin determinar el signo de cada momento. La tasa debe variar: no se afirma suficiencia de la diagonal a tasa fija.

**Geometría exacta.** Para z=ρ−1/2=δ+iγ definir h_u(z)=−4u²z²/(u²−z²)². La identidad 201 da b_N=Σ_ρ h_u(z)^N, y

    limsup_N |b_N(u)|^(1/N) = max_ρ |h_u(z)|.

En efecto Σ|h_u|<∞ por Z3. Los h no nulos tienden a cero en altura; la función generadora Σ_{N≥1} b_N t^(N−1)=Σ h_u/(1−th_u) es meromorfa, por convergencia local fuera de los polos. En cada polo coincidente los residuos valen −1 por copia y se suman. Cauchy–Hadamard da el máximo indicado.

La identidad |u²−z²|²−4u²|z|²=(u²−|z|²)²−4u²δ² implica que |h_u(z)|>1 exactamente para

    sqrt(γ²+2δ²)−|δ| < u < sqrt(γ²+2δ²)+|δ|.

Para δ=0 el intervalo es vacío. Por tanto el conjunto abierto de tasas de crecimiento superunitario es exactamente la unión de esos intervalos. Cada cero fuera de la línea produce uno de longitud 2|δ|, a alturas mayores que 14 por Z1. Contiene racionales. Bajo RH todos los h están en (0,1], los momentos son positivos y están acotados para cada u fijo. Esto demuestra la equivalencia (i). Como corolario local, si se prueba (i) en cada nodo de una malla de paso d, todo intervalo de detección enteramente contenido en la zona cubierta tiene |δ|≤d/2.

**Equivalencia usando únicamente signo eventual.** Elegir un compacto de longitud positiva en el interior de cualquier intervalo de detección. El máximo es >1 con holgura uniforme y sólo finitos ceros compiten allí. Poner x=−z² y a=u². Las magnitudes 4a|x|/|a+x|² son funciones racionales reales de a. Si dos coinciden idénticamente, comparar los coeficientes de a² y a después de multiplicar denominadores da |x|=|y| y Re x=Re y, luego sólo difieren por conjugación. Fuera de finitos empates hay un único par dominante salvo multiplicidades. No proviene de la línea crítica. El valor 4ax/(a+x)² de ese par es no real salvo a=|x|: su parte imaginaria tiene el signo de Im(x)(a²−|x|²). Elegir una tasa racional interior evitando esas excepciones. El término dominante es 2m |h|^N cos(N arg h); el resto es exponencialmente menor por la separación y Σ|h|<∞. El coseno vale ≤−1/2 infinitas veces, por periodicidad o densidad. La sucesión presenta infinitos signos negativos en esa tasa fija. Esto demuestra (ii).

**Parte ya cubierta sin hipótesis nuevas.** Por Z2, para 1/2<u≤G−1, G=3·10¹², ninguna banda de detección contiene u (su extremo inferior es ≥|γ|−1/2). Así los b_N son acotados en N a cada una de esas tasas. Se tiene además signo eventual para 1/2<u≤G−1000. Z3 asegura un cero crítico t₀ entre G−500 y G−200 por resta del conteo, cuyo término principal crece más que los dos errores. Para q=|z|²≥G², q₀=t₀² y u≤t₀,

    1/|h_u(z)|−1/h_u(it₀)
    =(q−q₀)(1−u⁴/(q q₀))/(4u²)−δ²/q
    ≥ [(q−q₀)²/(4u²)−δ²]/q >0.

La desigualdad final usa q−q₀>u y |δ|≤1/2. Por decaimiento en altura hay una brecha estricta para cada tasa fija entre el máximo no verificado y la contribución de t₀. El cuadrado crítico termina dominando toda la cola; el umbral en N puede depender de u. No se infiere negatividad en ningún punto para los datos verdaderos.

**Antecedentes y objetivo abierto.** POWER_REFLECTION_TEST_044 descarta eliminar el sector antisimétrico a tasa fija mediante reflexión de densidades. Aquí se varía u y se usa directamente el espectro completo; no se aplica esa reflexión. 206 exponía un par dominante variando la pendiente. La nueva diagonal tiene un solo índice y el intervalo de detección se calcula exactamente. Demostrar crecimiento subexponencial de b_N(u) para todas las tasas racionales arbitrariamente altas sigue siendo una obligación equivalente al signo global.
