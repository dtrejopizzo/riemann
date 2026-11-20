# Contraprueba para la decorrelación basada sólo en los portadores

Existe una sucesión fija f de valores 0,±1 que coincide con μ en todos los números con hasta tres factores primos distintos, tiene exactamente el mismo soporte libre de cuadrados y puede coincidir en cualquier tabla inicial prescrita. Conserva las cotas de distribución en celdas usadas en 350 y todas las reservas de signos de 351. Sin embargo, para cada δ=1/j, j≥16, X diádico suficientemente grande y H=X^(1−δ), sus dos residuos sobre p,2p y 3p,6p satisfacen

    ∫_[X,2X] R_1(x)R_3(x) dx/x ≫ H² exp(−2√log X).

Así la separación de los portadores y sus signos exactos permiten una correlación de orden H^(2−o(1)). La sucesión de prueba no es multiplicativa.

**Perturbación dispersa.** Fijar Q=3·5·7·11. En cada [N,2N), N potencia de dos por encima de la tabla inicial, hay ≫N múltiplos libres de cuadrados de Q, por el recuento de libres de cuadrados coprimos aplicado a n/Q. Entre ellos uno de los signos de μ ocupa ≫N puntos. Escoger sucesivamente el menor punto disponible de ese signo y dejar una separación de al menos D_N=⌈exp(√log N)⌉. Se obtienen K≫N/D_N puntos y a lo sumo O(1+N/D_N). En ese bloque comparar dos elecciones: mantener μ o invertirla en los K puntos. Las sumas difieren en módulo por 2K; escoger la opción con mayor suma en valor absoluto, fijando el desempate. De este modo |Σ_[N,2N) f|≥K sin presuponer nada acerca del tamaño real de la suma de Möbius en ese bloque. Las decisiones definen una sola f, independiente de las ventanas. Todos los portadores de 351 tienen a lo sumo tres primos distintos, de modo que ninguno ha sido modificado. La multiplicatividad junto con los signos primos y el soporte libre de cuadrados fijaría todos los coeficientes, así que esa hipótesis no se puede atribuir al modelo modificado; si alguna elección dejara f=μ en todos los bloques, las propias cotas inferiores ya se aplicarían a μ. Para garantizar por construcción una discrepancia sin recurrir a esa disyuntiva, en un único bloque finito posterior a la tabla inicial invertir obligatoriamente un múltiplo libre de cuadrados de Q. Esto no afecta a ningún enunciado asintótico.

**Qué conservan las celdas.** En cualquier subintervalo de longitud L dentro de [X/2,3X] hay O(1+L exp(−c√log X)) coeficientes diferentes de μ, ya que se cruzan sólo un número acotado de bloques diádicos. El cambio en todas las sumas parciales dentro de una celda de 350 es por tanto O_A(J/log^A X) para cada A fijo. La construcción de 351 se aplica con los mismos dos tipos de portadores, los mismos signos y la misma cota uniforme |R_i−S_f|≪1+J²/H=o(√H). Las subcolecciones efectivamente elegidas pueden ser distintas de las correspondientes a μ.

**Correlación.** Para X=N, integrar el pulso completo de f en dx/x. Cada n interior cuya traslación cabe entera aporta h∫η veces f(n); sólo O(H+1) enteros en los bordes tienen peso incompleto o provienen de fuera. Así

    ∫ S_f dx/x = h(∫η) Σ_[X,2X) f + O_η(h(H+1)).

Como H=o(X/D_X) para δ fijo, su módulo es ≫H/D_X. Cauchy–Schwarz da ∫ S_f² dx/x ≫H²/D_X². La norma L² de cada R_i−S_f es o(√H), despreciable frente a H/D_X. Expandir el producto cruzado da la cota anunciada.

**Comparación y decisión.** En 330 se conservaron multiplicatividad y signos pero se cambiaron magnitudes primas. Aquí se conservan magnitudes, soporte y valores exactos en ambas familias primas, a costa de modificar la ley multiplicativa. Una estimación de 351 fundada exclusivamente en la disponibilidad de primos, la disjunción y las cotas de distribución usadas para seleccionar los residuos sería falsa. El punto que requiere información adicional son las decisiones de selección que provienen de la μ exacta.
