# El promedio sobre direcciones modulares cumple el techo; la paridad obstruye trasladarlo a la dirección original

Tomar q primo impar y los primos q<p≤2q con pesos w_p=log p, M=Σw_p. En la dirección a∈{1,…,q−1} colocar el peso w_p en la coordenada y_p={a(p−q)/q} del círculo de longitud uno. Poner R_a(y)=Σ_(y_p≤y)w_p−My y

    V_a=(1/q)∫₀¹ |R_a(y)−∫₀¹ R_a|²dy.

En a=1 ésta es la recta de pendiente de extremos del intervalo [q,2q] con intercepto optimizado, en la normalización de 231. Bajo RH es O(log⁴ q) por von Koch. Si falla RH, 231 da liminf log(1+V₁)/log q≥2B pues ajustar también la pendiente sólo disminuye el error. Por tanto una subsucesión de q primos con V₁=q^o(1) bastaría.

**Fourier exacto y parte ya controlada.** Escribir S(m)=Σ w_p exp(2πim(p−q)/q). La derivada periódica de R_a es el peine de masas menos Mdy; sus modos no nulos tienen coeficientes de módulo |S(am)|. Parseval tras quitar la media y agrupar los enteros congruentes módulo q da

    V_a=M²/(12q³)+(1/(4q³)) Σ_(m=1)^(q−1) |S(am)|² / sin²(πm/q).

Se usó Σ_(k≡m mod q)1/k²=(π/q)²csc²(πm/q), obtenible de la expansión parcial de la cotangente. Por ortogonalidad discreta Σ_(m=0)^(q−1)|S(am)|²=qΣ w_p² para cualquier a≠0; los residuos son distintos. Los términos con min(m,q−m)≥√q aportan O(log q) UNIFORMEMENTE EN a, ya que csc²(πm/q)≪q allí y Σw_p²≪q log q por Chebyshev. El término de múltiplos de q es O(1/q). En consecuencia, en la dirección verdadera sólo es necesario el techo q^o(1) para el bloque de frecuencias 1≤m≤√q, con cada |S(m)|² dividido por qm² (constantes absolutas por simetría y seno).

**Qué cancelación se obtiene para los primos sin RH.** Promediar a sobre todos los residuos no nulos. Para cada m≠0, am recorre exactamente los mismos residuos. Usando Σ csc²(πm/q)=(q²−1)/3, se obtiene

    media_a V_a=M²/(12q³)+(q+1)(qΣw_p²−M²)/(12q³) ∼ (log q)/12.

Aquí M∼q y Σw_p²∼q log q por PNT. La identidad trigonométrica se obtiene tomando el término constante en la fórmula de suma de cotangentes derivada cerca del origen. Por Markov, por ejemplo, la fracción con V_a>exp(√log q) tiende a cero. No se permutan pesos independientemente: basta el grupo de q−1 multiplicadores del mismo conjunto de primos.

**Un obstáculo aritmético para usar el promedio.** Si b es un entero par con 2≤b<q y a=b⁻¹ módulo q, el modo m=b/2 verifica am≡2⁻¹ mod q. Puesto que p y q son impares, p−q es par y el coeficiente S(2⁻¹) es exactamente Σw_p exp(πi(p−q)/q). La medida q⁻¹Σw_p δ_((p−q)/q) converge a Lebesgue en [0,1] por PNT, por lo que |S(2⁻¹)|/q→|∫₀¹exp(πiy)dy|=2/π. Por la fórmula exacta,

    V_(b⁻¹) ≳ q/b²

con constante uniforme en todos esos b. Para b=2 ya es de orden al menos q, aunque el promedio sea logarítmico. Más aún, para cualquier inverso b de a con 1≤b<q se tiene V₁≤b²V_a: en el término de |S(n)|² se usa |sin(πbn/q)|≤b|sin(πn/q)| y la contribución constante es la misma. Bastaría así un buen multiplicador con inverso b=q^o(1), pero para TODOS los inversos pares de ese tamaño la cota de paridad bloquea esta transferencia. El promedio global no garantiza un buen inverso pequeño impar. No se demuestra la cota para la dirección verdadera.

**Antecedente.** 220 promediaba excursiones al variar el orden del detector, y 232 aislaba un error de rango. El promedio presente es finito y exacto a cada q, y su obstrucción viene de una frecuencia identificada por paridad en los primos auténticos.
