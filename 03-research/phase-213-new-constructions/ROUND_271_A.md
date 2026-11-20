# Reparación por cadenas: sólo los primos mayores que √N requieren interpolación

Para N=⌊2x⌋≥6 usar el ajuste calibrado de 262. Exigir a una combinación provisional a la igualdad con g(m/x) sólo en los primos p>√N hasta N. Para cada p≤√N definir r_(p,j)=g(p^j/x)−R_a(p^j) para 1≤j≤J_p=⌊log N/log p⌋ y r_(p,J_p+1)=0. Escribir

    D=Σ_(p,j) |r_(p,j)−r_(p,j+1)|,
    B=xh−Σ a_(n,k)e(n,k)−Σ_(p,j) r_(p,j) log p.

El ínfimo de ||a||₁+D+|B| sobre tales combinaciones es comparable a W_c(x) con constantes absolutas. En particular, una familia de coste x^(1/2+o(1)) calibrada a ese mismo orden y con errores uniformemente acotados en todas las potencias de los primos pequeños basta para probar el signo global. También basta el control agregado D≤x^(1/2+o(1)) bajo la misma calibración inicial.

**Reparación exacta.** Añadir la fila binom(p^j,1) con multiplicador d_(p,j)=r_(p,j)−r_(p,j+1). Sobre un módulo q su acarreo es 1_(q|p^j). Por telescopía, la reparación vale exactamente r_(p,i) en p^i y cero en las cadenas de otros primos. La variación añadida es D. La masa entrópica de esa fila es log(p^j)+(p^j−1)log(1+1/(p^j−1)), cuya diferencia con j log p está entre 0 y 1. Como Σ_j j d_(p,j)=Σ_j r_(p,j), el error de calibración que queda tiene módulo ≤|B|+D. Corregirlo por la relación nula fija de 262 con coste a lo sumo una constante absoluta por unidad. A la inversa, todo ajuste calibrado exacto ya tiene D=B=0. Esto demuestra la comparación en ambas direcciones.

**Presupuesto.** Si |r_(p,j)|≤M uniformemente, entonces D≪M√N/log N: hay O(√N/log N) primos y cuadrados de primos en estas cadenas, y O(N^(1/3) log N) niveles superiores. Además Σ_(p,j) log p ≪√N por la cota de Chebyshev y el mismo recuento de potencias superiores. Por tanto la corrección escalar inicial cambia en O(M√N). Para errores sin cota puntual, la telescopía anterior da |Σ r_(p,j)log p|≤D log N, suficiente si D ya tiene tamaño de raíz con pérdida subpotencial. La comparación con B retiene las cancelaciones de ese término a escala finita.

**Qué falta construir.** Para x grande los primos √N<p≤x deben reproducir cero, además de acertar en x<p≤N. La construcción de 267 controla uniformemente la respuesta pequeña, pero su error en una franja de primos de tamaño proporcional a x viola precisamente estas ecuaciones restantes. El procedimiento anterior elimina todas las condiciones de interpolación exacta en cuadrados, cubos y demás potencias propias, bajo el presupuesto explícito de variación en las cadenas; conserva la condición global de masa. La obstrucción universal de 270 no controla esta construcción específica.
