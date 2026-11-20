# Norma del cruce después de cancelar dentro de las ternas

El índice, selección posterior al control conjunto 212-84, ya describe las ternas y la agrupación de bordes por divisibilidad. Las coordenadas de saltos (XXXI) también aíslan el borde. Aquí se cuantifica una operación pendiente en ese antecedente: la norma del cruce entre dos bandas en el subespacio de paquetes disjuntos. La obstrucción 023-A aplica el módulo antes de la cancelación.

Sean K,R enteros, K≥1 y R≥4. En las celdas de [K,2K) cualquier vector u; en [RK,2RK) ternas disjuntas de celdas consecutivas. En cada terna P=[j,j+3) elegir un vector unitario e_P con suma cero y momento inverso cero. Para w=Σ t_P e_P se cumple ||w||=||t||. Con la matriz física M de BUILD084, hay una constante absoluta tal que

    |u* M w| ≤ C sqrt(log(2RK)/R) ||u|| ||w||.

Para el peine, comprimir las columnas contra los e_P antes de tomar módulos. En la fila i, cada n que contribuye cumple R/2<n<2R (los extremos con igualdad tampoco afectan). El intervalo [ni,n(i+1)) intersecta parcialmente a lo sumo dos ternas; cada suma parcial tiene módulo ≤√3. Las ternas completas pagan cero. La suma absoluta de fila es por tanto O(Σ_{R/2≤n≤2R}Λ(n)/n)=O(1) por Chebyshev. En la columna de inicio j, un extremo del intervalo debe coincidir con j+1 o j+2. Para cada uno de estos enteros m sólo intervienen divisores n de m, con a lo sumo dos opciones de i. La suma absoluta de columna es O((log(j+1)+log(j+2))/R), por Σ_{n|m}Λ(n)=log m. Schur rectangular da la cota indicada.

El bloque arquimediano separado tiene entradas O(1/(RK)) por BUILD084 (3), dado que la distancia física es al menos RK/2. Su norma de Hilbert–Schmidt es O(1/√R) aun antes de comprimir las columnas. Ambas cotas conservan libertad total en la cabeza. Sólo se usó suma cero en las ternas; el momento inverso permite escogerlas primitivas. La estimación no controla la componente de la cola que tiene medias por terna arbitrarias. Lema revisado independientemente.

## Consecuencia en todas las escalas de una cola

Cotejo independiente adicional con P47 lem:ext-hf (umbral dependiente de ventana), 212-83 y la selección de ternas posterior a BUILD084. Sean N_k=3·2^k para k entero no negativo. Partir [N_k,2N_k) en ternas disjuntas consecutivas. Para k≥k₀ y toda combinación finita w de los paquetes primitivos anteriores, escribimos w_k para la parte en esa banda. Existen constantes absolutas y k₀ suficientemente grande tales que

    a(Uw) ≥ (1/2) Σ_{k≥k₀} log(N_k) ||w_k||².

Las bandas cubren la cola y las ternas de esta partición tienen soporte disjunto incluso al cambiar de banda. Para el bloque arquimediano, la diagonal de BUILD084 es log j+O(1) de modo uniforme. El resto fuera de diagonal tiene norma O(1) al actuar de coeficientes de paquetes a celdas. En efecto, en la fila i y terna iniciada en j con |i−j|≥5, restar la entrada de su primera celda de las otras dos no altera el producto. La fórmula integral para h de BUILD084 da |h(m+1)−h(m)|≤1/m² para m≥1. Aplicada a h(i+j) y h(|i−j|−1), da una entrada comprimida O((1+|i−j|)⁻²); para |i−j|<5 las entradas fuera de diagonal están uniformemente acotadas y se pone cero en la diagonal del resto. Esta mayoración tiene sumas uniformes por filas y columnas. Schur y la isometría de síntesis pagan O(||w||²).

Para el peine dentro de una banda o entre bandas vecinas sólo hay n≤4. Para cada n una fila de la matriz orientada tiene a lo sumo n contactos y una columna a lo sumo uno. Así el bloque y su traspuesto tienen norma O(1) antes de comprimir. Para l≥k+2 usar el lema del peine anterior con R=2^(l−k), K=N_k. Al normalizar cada banda por el peso sqrt(log N_k), la norma de ese bloque dividido por sqrt(log N_k log N_l) es a lo sumo

    C 2^(−(l−k)/2) / sqrt(log N_k),

pues log(2N_l)/log N_l está acotado. Por simetría el mismo mayorante usa min(k,l) y |k−l| para el otro triángulo. En la matriz escalar de normas de bloques normalizados, ambas sumas por filas y columnas están acotadas por C/sqrt(log N_{k₀}) por la serie geométrica; las tres diagonales cercanas cuestan O(1/log N_{k₀}). Aplicar Schur a la sucesión sqrt(log N_k)||w_k|| controla el peine completo. La diagonal domina los dos errores para k₀ grande, y da el enunciado.

El corte es existencial. El límite superior del soporte y la cantidad de bandas son libres. El argumento admite un múltiplo fijo del peine aumentando el corte, de modo que localizar el signo para los pesos verdaderos aún requiere controlar los modos complementarios y sus cruces. PROVED tras revisión matemática independiente de la consecuencia multiescala.
