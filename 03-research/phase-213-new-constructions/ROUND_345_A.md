# Qué saldo tienen las primeras filas que sobreviven a la inversión

Sea Y=√X, h=X^(−δ), 0<δ<1/4 fijo. En A_h de 338–344 seleccionar filas con 3Y/5≤d≤7Y/10 y centros 17X/10≤x≤19X/10. En esta banda de **filas completas**, antes del recorte de productos pequeños, su contribución a A_h es exactamente

    Σ_n λ(n) a_Y(n) W_x(n),
    a_Y(n)=Σ_{d|n, 3Y/5≤d≤7Y/10} μ²(d)μ²(n/d),

donde λ(n)=(−1)^Ω(n). En C_h tomar la banda correspondiente a cada escala. Entonces, incluso agrupando ambas escalas por el mismo argumento n del pulso, la suma de módulos de los términos con n impar es ≍ hX, uniformemente en estos centros. Esto supera el presupuesto puntual √(hX) por una potencia. Se mide el coste por módulos de esta representación exacta de la banda, no su saldo firmado.

**Cálculo.** Al primer pulso sólo llegan m con xe^(−h)/d<m≤x/d, luego 2Y<m≤4Y para X grande. En la suma de divisores de m cortada en D=2Y falta exactamente el divisor m; todo divisor propio es ≤m/2. El coeficiente interior es −μ(m). En el segundo pulso se tiene 1<m≤x/(2d)<2Y: la fila es cero por inversión completa. El signo exterior de 338 cancela el signo menos anterior. A producto n=dm fijo se cumple μ(d)μ(m)=λ(n)μ²(d)μ²(m), sin exigir que d y m sean coprimos. Por eso en la primera escala todas las representaciones no nulas de n tienen idéntico signo.

La segunda escala tiene soporte en argumentos 4dm del pulso original. Más precisamente, el coeficiente conjunto es λ(n)a_Y(n)−2·1_{4|n}λ(n/4)a_(Y/2)(n/4), interpretando el segundo sumando sólo cuando procede. Para n impar queda intacto el coeficiente de la primera escala.

**Tamaño uniforme.** Como η≥0 tiene integral positiva, hay un intervalo fijo interior donde η≥c>0. Para cada d impar libre de cuadrados de la banda, ese intervalo selecciona m en un intervalo de longitud comparable a hY dentro de [2Y,4Y]. El recuento de impares libres de cuadrados hasta z es c₁z+O(√z) para c₁>0, por la expansión de μ² en divisores cuadrados impares y recuento de múltiplos impares. Dado que hY/√Y=X^(1/4−δ)→∞, hay ≫hY opciones, uniformemente en d y x. Hay ≫Y opciones de d, dando el piso ≫hX. El techo O(hX) sale contando todos los pares sin restricciones de paridad ni de cuadrados. La agrupación por producto conserva la masa en módulo en los argumentos impares.

**Uso y alcance.** Por Poisson en 338 se puede reponer el recorte de productos pequeños con error O_B(X^(−B)) en el valor firmado de la banda; esto no afirma proximidad de sus coeficientes en variación total. En contraste con las filas de saldo cero de 344, aquí se identifica el observable restante como una suma local de Liouville ponderada por un recuento explícito de divisores equilibrados. Para bajar su coste hay que usar cancelación entre distintos n o con otras bandas. No se deduce un piso para la suma firmada completa.
