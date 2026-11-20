# Una sola comparación de paridades, con corte y anchura fijados por x

Sea y(x)=(log x)² para x≥e y g(u)=exp(u/2)φ₁(u). Poner

    S^*(x;z)=Σ_{n sin factores primos ≤z} μ(n) g(log(x/n)).

Se incluye n=1. Entonces **RH equivale a S^*(x;y(x))<0 para todo x suficientemente grande**. Incluso la desigualdad débil ≤0 basta. Entre los libres de cuadrados sin primos pequeños se comparan las masas con número impar y par de primos, sin una etiqueta exterior log p. Se usa el corte exacto y una sola varianza constante.

**Bajo RH.** El cálculo de 367 se aplica con el mismo K y el mismo producto de Euler, pero el factor restante es ahora F(s)=1/ζ(s), en vez de B_z(s). En la silla real F→1/ζ(1/2)<0. La dominación local por la gaussiana, la amortiguación intermedia por primos entre z/2 y z y el techo para F bajo RH son los mismos que en 367. Por tanto S^*∼exp(K(s₀))/(ζ(1/2)√(2πK''(s₀))) al corte z=y(x). En particular es estrictamente negativa eventualmente.

**Extender una desigualdad sin pagar ramas de signos arbitrarios.** Suponer sólo S^*(t;y(t))≤0 para t≥t₀>e. Para x grande y y(x)≤z≤4y(x), cambiar el corte congelado z a w=y(x) por la identidad

    S^*(x;z)=Σ_{d con todos sus primos en (w,z]} S^*(x/d;w).

Incluye potencias y todos los coeficientes de transporte son +1. Procede de la identidad de Euler de 358 y converge absolutamente por decaimiento gaussiano. Al descender, detener los hijos con t<t₀ y, para los demás, repetir sólo si el corte heredado supera y(t). Las hojas grandes con corte correcto son no positivas; una rama con factor 1 termina y cada otro paso reduce la escala por lo menos a la mitad. Para cada D total hay a lo sumo una rama terminal: dada la escala, el factor de ese paso tiene que absorber todas las potencias de D pendientes en la banda de primos recién abierta, que nunca reaparecerá. Esto vale también al detener una hoja pequeña. La profundidad es finita para x fijo; aunque una expansión bilateral tenga infinitos hijos pequeños, sus sumas absolutas convergen.

En las hojas pequeñas |S^*(t;U)|≪_(σ,t₀) t^σ para todo σ>1/2, uniformemente en el conjunto de primos retirados, por el conteo absoluto y el decaimiento gaussiano en t→0. Sumando sus costes, para 1/2<σ<1 resulta

    S^*(x;z) ≤ C x^σ ∏_{p≤z}(1−p^(−σ))^(−1) = x^(σ+o(1)) O(1).

Así sólo el signo en un corte produce un techo unilateral O_η(x^(1/2+η)) en todo el corredor, para cualquier η>0. La elección de μ sin primo exterior es importante: en esta expansión no hay término corrector del otro signo.

**El techo impide todo cero exterior.** Para v=log x fijar z=2v². Convolucionar e^(−u/2)S^*(e^u;z) en u con φ_(av−1)(u−v), como en 367. Se obtiene el promedio difusivo normalizado de los mismos coeficientes sin etiqueta. En |u−v|≤v/5 se puede aplicar el techo anterior con cualquier η>0, con coste superior O(exp(6ηv/5)); fuera de allí el coste absoluto es exponencialmente pequeño para 0<a<1/1000 fijo por la misma cota gaussiana de 367. Por tanto el promedio difusivo sin normalizar tiene techo unilateral x^(1/2+o(1)) en el sentido de cada pérdida positiva fija.

Si existe un cero con β>1/2, elegir uno y tomar a>0 suficientemente pequeño para que Re Φ_a(ρ)>1/2. La prueba de excursiones de 365 se aplica a F(s)E_z(s), con z=2(log x)². Para explicitar el cambio, en un cero de multiplicidad m el polo tiene orden m, y la amplitud en el bloque x=X exp(u) es X^Φ_a(ρ) E_(2(log X)²)(ρ) (log X)^(m−1) veces una constante no nula: la constante es m Φ_a'(ρ)^(m−1)/ζ^(m)(ρ). El control relativo en el círculo de radio 1/log X no cambia; al variar el corte en el bloque se añaden O(log X) candidatos. El contorno de 365 limita el resto y su medida positiva anula los modos complejos. Se obtienen en particular excursiones **positivas** de tamaño X^(M−o(1)) con M>1/2, contradiciendo el techo. Esto concluye la implicación inversa.

**Alcance.** 367 emplea todos los cortes de un corredor y pesa el primo exterior. Aquí no se exige uniformidad en ningún parámetro distinto de x. La estimación unilateral se transporta porque las bandas sucesivas de primos son disjuntas y sus factores de transferencia son positivos. Lo pendiente es una demostración aritmética de la desigualdad eventual de paridades; el equivalente en la silla por sí solo requiere RH al desplazar el contorno.
