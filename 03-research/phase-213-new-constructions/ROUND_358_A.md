# Reconstrucción sin pérdidas por profundidad para cribas crecientes

Sea T(X) una familia creciente de conjuntos finitos de primos, fijada para cada escala real X≥1/2. Supongamos que para cada σ>1/2 fijo

    ∏_{p∈T(X)}(1−p^(−σ))^(−1) = X^o(1).

En el criterio 353 basta estimar la suma de primos simples cuyo cofactor no es divisible por ningún primo de T(X), con ese único conjunto en cada bloque y la misma norma y anchuras de 357. Esta estimación equivale a RH. No se requiere limitar el número de cambios de T al descender por las escalas.

**Reconstrucción.** Mantener h fijo, y denotar por R_T el observable de 357 con conjunto prohibido T. Empezar con P=Σ μ(d₀)T_{d₀}R_{T(X)}, donde d₀ tiene primos en T(X) y T_d denota dilatación. En un nodo con escala Y y conjunto heredado U⊇T(Y), si coinciden, detenerse; si no, expandir con coeficiente +1 sobre todos los enteros con primos en U menos T(Y), dejando como nuevo conjunto T(Y). Es la identidad local de 357, que vale para cualquier diferencia de conjuntos anidados. Omitir hijos con escala <1/2 porque su bloque no contiene argumentos pm≥2. Un hijo con factor 1 conserva su escala y termina inmediatamente; todo otro hijo reduce la escala al menos a la mitad. El árbol es finito para cada X.

**Unicidad tras la primera elección.** Fijados el producto total D de una rama terminal y su primer factor d₀, el resto del camino, si existe, es único. En un nodo que expande, extraer del cociente aún pendiente **todas las potencias** de los primos pertenecientes a la diferencia de conjuntos que se acaba de abrir. Ése tiene que ser el factor de ese paso: en los pasos posteriores sólo se admiten primos del conjunto menor. Conocido ese factor queda determinada la escala hija. Esto reconstruye también los pasos unitarios y la decisión de parada. Para D fijo, d₀ es un divisor libre de cuadrados, de modo que hay a lo sumo 2^ω(D) ramas. Toda hoja usa el observable prescrito a escala X/D. Se podría reagrupar con signo; la cota no lo necesita.

**Norma.** Sea 1/2<σ<1 y η=σ−1/2. La hipótesis de cota crítica con pérdida η en cada hoja cuesta, en unidades de √(hX), a lo sumo C X^η D^(−σ). En escalas compactas usar conteo de pulsos como en 357, aumentando C. Sumando por D, el multiplicador restante es a lo sumo

    Σ_{D con primos en T(X)} 2^ω(D) D^(−σ)
      = ∏_{p∈T(X)} (1+p^(−σ))/(1−p^(−σ))
      ≤ ∏_{p∈T(X)} (1−p^(−σ))^(−2) = X^o(1).

Tomar η menor que la pérdida pedida y aplicar 353. La dirección bajo RH sigue de una sola convolución positiva para R_{T(X)} en términos de P y de la misma cota de producto. Se trabaja con σ fijo antes de hacer η arbitrariamente pequeño.

**Ejemplos.** Vale para todos los primos hasta (log X)² sin escalones y para cualquier umbral creciente (log X)^(2+o(1)). En efecto Σ_{p≤y}p^(−σ)≪_σ 1+y^(1−σ)=o(log X) en el rango indicado. También pueden añadirse a la vez todos los primos hasta 2X de cualquier conjunto fijo con O(√t) miembros hasta t: por sumación parcial su serie de p^(−σ) converge para σ>1/2. Así la reconstrucción admite ciertas exclusiones de primos mucho mayores que log²X. El antecedente 309 identifica la escala de las normas de Euler; aquí la cota de multiplicidad resuelve el coste de cambios arbitrariamente frecuentes del conjunto en el criterio local.

**Pendiente.** El teorema permite elegir qué primos excluir bajo el presupuesto declarado. No da por sí mismo la estimación crítica para el cofactor que evita esos primos.
