# POWER_CONFLUENT_BRIDGE_REVIEW_014 — Revisión independiente breve

Estado: APROBADO. Se revisó POWER_CONFLUENT_BRIDGE_014 desde sus fórmulas; no se requiere corrección matemática.

1. **Convención compleja.** Para el producto habitual H¹ lineal en h y antilineal en el test, los tests y^k e^-ay son reales cuando a>0. Así J^(k)(a)=0 es exactamente su ortogonalidad, con factor (-1)^k, aunque J se prolongue holomórficamente de forma bilineal en z. No debe conjugarse z dentro de J; el texto correctamente no lo hace.

2. **Integración por partes.** h∈H¹ tiene traza h(0). Su representante es continuo y acotado, y e^-zy h(y) tiende a cero para Re z>0. La igualdad ∫h'e^-zy=−h(0)+zH(z) tiene los signos correctos. Por tanto J=(1−z²)H+zh(0), y evaluar z=1 fuerza h(0)=0; no queda condición Robin oculta. La unicidad Fourier en una vertical aplica porque e^-cy h∈L¹∩L².

3. **Norma fuerte.** Si e^eta y f∈H¹, entonces f∈H¹ por multiplicación acotada. La extensión cero a H^s(R),0<s<1/2, admite salto en0 y es continua. Esa norma domina el peso logarítmico de m. El peso eta>1/2 controla ambos momentos y la suma infinita del peine por estimaciones bilineales. No se usa solo densidad L².

4. **Paso al signo.** La positividad de cada bloque implica la de su unión creciente. Cada test compacto trasladado pertenece al espacio ponderado y se aproxima en esa norma fuerte; continuidad de la forma basta. No se necesita ningún margen uniforme en el grado. La traslación conserva la forma completa, pues A y B reciben factores recíprocos. Se pasa primero la positividad de W a todos los tests y dominios de ventana; después se restringe al subespacio primitivo. No se exigen aproximantes primitivos en la construcción.

5. **Confluencia exterior.** La matriz triangular de derivadas de zeta(a)e^(-(a−1/2)y) tiene diagonal (-1)^k zeta(a), no nula para a>1. Identifica exactamente todos los grados confluentes sin presuponer positividad por entradas.

La suficiencia demostrada corresponde a TODOS los bloques completos y términos cruzados, no a una cadena de diagonales ni a familias de grado acotado. Los certificados actuales no completan esa obligación.
