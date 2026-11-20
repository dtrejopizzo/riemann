# Pérdida del mayorante de Poisson bajo dilatación de celdas

Antecedentes 212-59, 212-75 y 212-76. La operación adicional consiste en barrer al círculo la medida radial del bloque Hankel H y conservar exactamente el peine. El cotejo independiente habilitó comprobar la condición suficiente resultante. Usamos la matriz completa M=K−H/2 de 212-59. Si P(z)=Σα_j z^j, entonces H[P]=∫₀^∞ w(x)|P(exp(−x))|² dx, con w(x)=((1−exp(−x))/x)². Escribimos M[P] para la energía completa de las celdas.

Sea J[P] la misma integral con |P(r)|² reemplazado por la media de |P(z)|² respecto de la probabilidad de Poisson de r=exp(−x) en el círculo. J−H es la integral de la varianza por la fórmula de Poisson. El criterio suficiente propuesto sería K≥J/2. Demostramos que para cualquier perfil de celdas primitivo fijo no nulo su defecto normalizado tiende a menos infinito bajo réplica entera.

Para el entero q≥1 la réplica tiene polinomio P_q(z)=(1+⋯+z^(q−1))P(z^q). Corresponde a f_q(u)=f(u/q). En variable logarítmica es una traslación de F multiplicada por √q. Conserva los momentos nulos y M[P_q]=q M[P], con ||P_q||²=q||P||² en la norma de coeficientes. Además, al evaluar en exp(−x) el factor geométrico cancela exactamente el denominador geométrico de w: w(x)|P_q(exp(−x))|²=q² w(qx)|P(exp(−qx))|². Así H[P_q]=qH[P] y K[P_q]=qK[P].

Con dz la probabilidad angular uniforme, J[P_q]=∫|P_q(z)|² S(z) dz, donde S(z)=∫₀^∞ w(x)(1−exp(−2x))/|z−exp(−x)|² dx por Tonelli. La masa de S es finita por integrabilidad de w. Cuando z→1 el límite inferior de S es infinito por Fatou: en z=1 el integrando es w(x)(1+exp(−x))/(1−exp(−x)), equivalente a 2/x en cero.

Las medidas |P_q|² dz/q tienen masa ||P||² por ortogonalidad. Fuera de cualquier arco fijo alrededor de 1, |P_q(z)|≤2 sup|P|/|1−z|, por lo que la masa exterior tiende a cero. Para cada L positivo elegimos un arco donde S≥L. Resulta liminf J[P_q]/q≥L||P||² para todo L, y por tanto J[P_q]/q→∞. Concluye (K[P_q]−J[P_q]/2)/||P_q||²→−∞. El test f_3 de BUILD_084 permite realizar la obstrucción partiendo de una energía física estrictamente positiva.

Alcance: queda descartado pagar todo el mayorante barrido con K. La varianza recuperada en la identidad exacta es esencial a esta escala. El signo de M en el portador completo sigue abierto. Estado PROVED para esta obstrucción. La revisión independiente comprobó las escalas, la varianza y la concentración incluso cuando P(1)=0.
