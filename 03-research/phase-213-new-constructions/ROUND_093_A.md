# Una desigualdad de prefijos sin parámetro continuo

Sean p_n los primos en orden creciente, w_n=log p_n, H_n=Σ_{k≤n}w_k y Q_n=Σ_{k≤n}w_k². El signo global equivale a

    B_n = Q_n − H_n log H_n + H_n ≥ 0 eventualmente.

En efecto S(x) de selección 092 es el máximo sobre n≥0 de H_n log x−Q_n (el prefijo vacío da cero): los incrementos son w_n log(x/p_n), que cambian de signo una sola vez. Para cada n≥1, el máximo en x>0 de H_n log x−Q_n−x se alcanza en x=H_n y vale −B_n. Si S(x)≤x eventualmente se puede evaluar en H_n→∞ y deducir B_n≥0, incluso si H_n no está entre p_n y p_(n+1). Recíprocamente cada prefijo con B_n≥0 queda por debajo de x para todo x, y los finitos prefijos iniciales también lo hacen para x suficientemente grande. Aplicar 092.

**Cuánto cuesta retirar la variable x.** Exactamente, para p=p_n,

    B_n = p−S(p) − p[ (H_n/p)log(H_n/p)−H_n/p+1 ].

La corrección que se resta es no negativa, asintótica a (H_n−p)²/(2p) cuando H_n/p→1 con H_n≠p. Así sustituir el máximo del prefijo por su valor en el primo pierde un término explícito de segundo orden.

**Incremento exacto.** B_0=0 y B_n−B_(n−1)=∫_{H_(n−1)}^{H_n}log(p_n/t)dt. Hay incrementos negativos siempre que H_(n−1)≥p_n. Por tanto un intento de demostrar el signo por monotonía requeriría información sobre la posición del primo frente a su masa acumulada. La tarea unilateral es controlar el total firmado de estos incrementos. Esta dualización elemental del criterio primo no prueba tal estimación.
