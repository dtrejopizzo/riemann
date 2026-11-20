# Un conjunto explícito de extremos basta para toda la representación calibrada

Fijar N≥2 y una base entera b≥2. Bastan los extremos N y N−b^i para 1≤b^i≤N/2 (i empieza en cero). Cualquier fila binomial de extremo n≤N y lado menor k se reproduce por una combinación entera de filas con esos extremos de variación ≤4s_b(k), donde s_b cuenta la suma de las cifras. La identidad vale simultáneamente para todos los módulos y conserva la masa de entropía de 262.

**Traslación elemental.** Trabajar en el grupo abeliano libre sobre F₁,…,F_N con F₀=0. Poner C(u,v)=F_u−F_v−F_(u−v), incluidas las particiones con lado cero que dan el vector cero. Para d≤j≤N, restar las dos filas que comparten el lado N−j. Directamente,

    F_j−F_(j−d) = F_N−F_(N−d) + C(N−d,N−j)−C(N,N−j).

Escribir k como lista d₁,…,d_s de potencias de b, repitiendo cada una tantas veces como indica su cifra. Con u_i=d₁+…+d_i, telescopar primero los incrementos que terminan en n−k+u_i y después los que terminan en u_i. Al restar, las dos sumas de F_N−F_(N−d_i) se cancelan término a término. Queda exactamente C(n,k), con a lo sumo cuatro filas de signo ±1 por incremento. Cada partición es válida porque ambos puntos finales están entre d_i y N. Los lados que excedan la mitad pueden sustituirse por sus complementos.

**Calibración y coste.** Evaluar los símbolos F_j en ⌊j/m⌋ da los acarreos para cada m. Evaluarlos en j log j, con valor cero en j=0, conserva exactamente la entropía, incluso para familias firmadas. Si W_c es el mínimo de 262 y W_c^(b) el mínimo con los extremos aquí prescritos, se obtiene

    W_c ≤ W_c^(b) ≤ 4 (b−1)(1+log_b N) W_c.

Así, con base dos toda la condición equivalente al signo global de 262 se puede imponer sobre O(log N) extremos pagando a lo sumo O(log N) en variación. Con b=⌈exp(√log N)⌉ quedan O(√log N) extremos y el coste adicional es N^o(1), que también preserva el presupuesto x^(1/2+o(1)). Más generalmente se puede tomar b=⌈N^(1/L)⌉ para cualquier L=L(N)→∞ con L≤log N: bastan L+2 extremos y el factor es O((L+1)(N^(1/L)+1))=N^o(1).

**Relación con el cierre.** 261 construía una representación a partir de la inversión en todos los enteros; 268 excluía concentrar todos los extremos en una banda estrecha a coste de raíz. Aquí la identidad se aplica después de cualquier ajuste, incluido uno que sólo prescribe las potencias primas y calibra la masa. La localización en estas escalas dispersas ya no es una hipótesis que deba justificarse. Sigue abierta la cota de raíz del coste mínimo dentro de ellas.
