# Separación de las frecuencias que exige 184

Para N grande, sea μ la probabilidad en los primos de [N,eN] proporcional a log p, U=log(p/N) y φ(t)=Eμ exp(itU). Hay constantes absolutas c,C>0 con esta propiedad: fijados 0<α<1 y 0<ε<c(1−α)², si |φ(t)| y |φ(t')| son ≥1−ε, entonces

    |t−t'|≤C√ε   o   |t−t'|>N^α.

El umbral de N puede depender de α. Las alturas individuales son arbitrarias. En 184, escogiendo primero D suficientemente grande, esto excluye diferencias intermedias entre dos candidatos para el mismo bloque. Persiste la posibilidad de un pico aislado.

**Diferencia de fases.** Cada variable unitaria exp(itU) de media de módulo ≥1−ε dista en L² a lo sumo √(2ε) de una constante de módulo uno. Para el producto de una y la conjugada de la otra la distancia a la constante producto es ≤2√(2ε). Tomando parte real, |φ(t−t')|≥1−4ε.

**Frecuencia moderada.** Para 1≤s≤N^α y cualquier arco angular de semiancho η<1 fijo, la condición exp(is log(x/N)) en el arco corta [N,eN] en O(1+s) intervalos. Cada uno tiene longitud ≤2eηN/s por la regla de la cadena, también si toca un borde. Se pueden mayorar por intervalos de longitud H=ceil(2eηN/s)+2. La desigualdad clásica de Brun–Titchmarsh en módulo uno da O(H/log H) primos por intervalo; la constante es absoluta. Para N grande según η y α se tiene log H≥(1−α)log(N)/2. Multiplicando por log(eN) y dividiendo por la masa total (e−1+o(1))N, obtenemos probabilidad ≤C₀η/(1−α). Aquí sH=O(ηN) uniformemente, para N suficientemente grande. Tomar η=c₀(1−α) con c₀ absoluto pequeño deja al menos la mitad de la masa fuera de cualquier arco así. Centrar en el argumento de φ(s) da 1−|φ(s)|≥(1−cos η)/2≥c₁(1−α)².

**Frecuencia baja.** Para |s|≤1 y U' copia independiente, 1−|φ(s)|²=E[1−cos(s(U−U'))]≥c₂s² Var(U). Por PNT, U converge en ley a la densidad e^u/(e−1) en [0,1], de varianza positiva. Estas dos cotas y la diferencia de fases demuestran la separación.

**Forma local del pico.** Si φ(t)=|φ(t)|z, |z|=1, entonces |φ(t+s)−zφ(s)|≤√(2ε) para todo s por Cauchy–Schwarz. Para s en un compacto, φ(s) converge uniformemente a (exp(1+is)−1)/((e−1)(1+is)), por PNT y equicontinuidad. Esto identifica el perfil cerca de un candidato, con error O(√ε)+o(1).

181 estimaba la medida total de un conjunto excepcional para el peine global. Aquí la separación se deduce para dos frecuencias del promedio casi máximo de un mismo bloque y sin restricción sobre su altura absoluta. Brun–Titchmarsh ya figura entre las herramientas de R163_602; se aplica aquí a los intervalos de preimagen de un arco para la frecuencia diferencia. La prueba requiere masa de todos los primos y no se aplica a los pesos arbitrarios de 185.
