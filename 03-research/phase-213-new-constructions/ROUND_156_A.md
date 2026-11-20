# Qué afirmación exacta puede probar un número finito de momentos de divisores

Para j≥1 entero, usar la suma positiva A_j^*(x)=Σ_{m≥1}(log m)^j V(x/m) de 154. Sea C_j(x) la suma de los residuos en s=1 y s=1/2 de x^s H(s)(−ζ'/ζ)(s)(−1)^jζ^(j)(s), con H de 155. Para M fijo son equivalentes:

1. Para cada 1≤j≤M se tiene A_j^*(x)−C_j(x)≤O_j(√x) eventualmente.
2. Todo cero no trivial fuera de la recta crítica tiene multiplicidad estrictamente mayor que M.

En particular el primer momento examina exactamente los ceros simples. La equivalencia identifica el alcance de la prueba potencial; ninguna de las dos condiciones se demuestra para los ceros de ζ en este memo.

**Prueba.** Por convergencia absoluta en Re s>1, el integrando que define C_j es el de la inversión de Mellin de A_j^*. En un cero ρ de orden m el único factor potencialmente singular a la derecha de Re s=0 es la derivada logarítmica, salvo los polos reales ya indicados. Para j<m el factor ζ^(j) se anula y la singularidad es removible. Para j=m el residuo tiene coeficiente (−1)^(j+1)m H(ρ)ζ^(m)(ρ), no nulo si Re ρ>1/2 por el producto de Euler en 2ρ. Cualquier cero fuera de línea tiene un compañero de la misma multiplicidad a la derecha por simetría. Si m≤M, Landau aplicado al techo del momento j=m, restando C_j como en 155, excluye ese polo. Esto prueba 1⇒2.

A la inversa, bajo 2 todos los puntos fuera de línea son removibles para cada j≤M. Desplazar hasta Re s=−1/4 evita la necesidad de cotas de separación a ceros múltiples en el interior de la tira. Sobre esa línea la ecuación funcional y Stirling dan crecimiento polinómico para los factores zeta y sus derivadas de orden fijo, y la derivada logarítmica se controla por reflexión a Re s=5/4. Las horizontales de 151 evitan todas las ordenadas y permiten el desplazamiento. En cero el factor gamma introduce a lo sumo un polo simple de contribución O_j(1). Los términos críticos tienen suma absoluta O_j(√x): H decrece exponencialmente en altura salvo factores polinómicos, ζ^(j) crece polinómicamente y se usa el conteo con multiplicidad. La integral desplazada es O_j(x^(−1/4)). Se obtiene incluso la cota bilateral para el resto.

**Decisión.** La identidad factorial de 155 en d=0 se puede derivar a cualquier orden finito, pero su primer momento introduce el factor (ζ')²/ζ, próximo a las identidades de Selberg ya registradas en el índice. El criterio anterior especifica exactamente qué perdería un intento de cerrar por un número prefijado de derivadas. Sin un control independiente de las multiplicidades fuera de línea, obtener unos pocos momentos no autoriza el paso global. El desplazamiento fijo de 155 retiene la detección sin esa hipótesis. No se propone iterar la tabla de momentos.
