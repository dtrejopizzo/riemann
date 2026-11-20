# Interpolación calibrada a ambos lados de una banda de módulos

Con N=⌊2x⌋, U=⌊√N⌋ e Y=⌊N^(1/3)⌋, existe incondicionalmente una combinación de variación O(√N log³(2N)) con entropía xh, exacta en todos los enteros m>U y en todas las potencias primas q≤Y. Basta considerar N grande. La construcción mantiene el peso g de 257.

**Dos momentos discretos.** Sea χ suave, cero hasta 1/2 y uno desde 1. Para t>0 formar S₀(t)=χ(t/U)Σ_d μ(d)g(dt/x), con extensión cero a t≤0. Añadir Aφ₁(t/U)+Bφ₂(t/U), con φ_i suaves no negativas de integral uno, soportadas respectivamente dentro de (1/4,1/3) y (2/3,3/4). Llamar S a la suma. Para w_j=j log j−(j−1)log(j−1), imponer exactamente

    Σ_j S(j)=0,      Σ_j S(j) w_j=xh       (j≥1).

Al restar (log U+1) veces la primera fila a la segunda, las columnas de los dos correctores, divididas por U, convergen a (1,∫φ_i(v)log v dv). Los soportes separados dan límites distintos en la segunda componente, por lo que la inversa de la matriz normalizada está acotada. Como |S₀(j)|≪x/j para U/2≤j≤N y w_j=O(log(2N)), se obtiene |A|+|B|≪(x/U)log²(2N).

**Coste y entropía.** Tomar b_j=S(j)−S(j+1), 1≤j≤N. Por telescopía los momentos son Σ_j j b_j=0 y Σ_j (j log j)b_j=xh. El promedio cíclico de 261 convierte Σ b_j F_j en filas a coste ≤2Σ|b_j|. Cada sumando de S₀ tiene variación O(1) por la regla del producto y sólo intervienen d≤4x/U. Los correctores dan por tanto coste total O((x/U)log²(2N)). La respuesta es R(m)=Σ_(l≥1)S(lm). Para m>U el muestreo sólo ve la inversión original y da g(m/x) exactamente.

**Amortiguación inferior.** La derivada tercera de S, como medida, tiene variación total K≪(x/U³)log²(2N). Para verlo, en el término con escala d/x la derivada tercera de g tiene norma de medida O((d/x)²) tras reescalar, ya que g es C¹ y g'' tiene variación acotada. La suma sobre d≤4x/U es O(x/U³). En los términos donde se deriva χ al menos una vez, la integración es en un intervalo de longitud O(U); cada derivada de orden i≤2 de la copia de g está acotada por O((d/x)^i). Por término cuesta O(U^(−2)) y hay O(x/U) términos. Cada corrector cuesta O((|A|+|B|)/U²) en conjunto.

Por periodización de S, con |Ŝ(ξ)|≪K/|ξ|³, se tiene |R(m)−m^(−1)∫S|≪Km². La primera condición discreta da R(1)=0, de donde |∫S|≪K. En consecuencia |R(m)|≪Km² también para los módulos bajos. El objetivo allí vale cero.

**Reparación que conserva ambos extremos.** Poner r(q)=−R(q) en potencias primas q≤Y y cero en los niveles superiores de cada cadena. Aplicar las diferencias consecutivas de 271. Cuestan ≤2Σ_(q≤Y)|r(q)|≪KY³, aun sumando sobre todos los enteros, y cada fila añadida tiene extremo ≤Y. El cambio de entropía es O(KY³ log(2N)); la relación fija de 262 lo corrige con coste del mismo orden sin afectar ningún átomo primo, ni ningún módulo mayor que U para N grande. Con los cortes anunciados resulta el presupuesto de raíz. Quedan únicamente las ecuaciones en las potencias primas Y<q≤U. El ajuste simultáneo en ambos extremos procede de la suavidad y de los dos momentos discretos; el coste de 272 solo no daba control sobre el residuo inferior.
