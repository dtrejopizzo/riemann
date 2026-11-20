# Un corte macroscópico deja el bloque de primos grandes acotado por una constante

Sea R_t(x,y) la suma de b_t(n) para n≤x con un primo >y. Para x suficientemente grande y 0≤t≤1 se puede elegir y en [x/4,x/2] con |R_t(x,y)|≤C absoluto. Sólo se requieren sumas sobre primos y los coeficientes b_t(1), b_t(2), b_t(3) para elegir el corte. Por 292, el signo global equivale a un techo integrado de raíz con pérdida para la parte positiva del bloque restante en esa banda fija. Aquí el error de retirar el bloque grande es O(1). El bloque restante aún contiene casi toda la dificultad aritmética.

**Cálculo en t=0.** Sea π_i la cuenta de primos congruentes con 2 módulo 3. En todo el intervalo indicado, al factorizar n=pm con p>y se tiene m<4, p es único y b₀(3)=0. Por tanto

    R₀(x,y)=−4[π_i(x)−4π_i(x/2)+3π_i(y)].

La expresión entre corchetes en y=x/4 es asintótica a −x/(8 log x) y en y=x/2 a x/(4 log x), por el PNT en progresiones. Eligiendo π_i(y) como el entero más próximo a (4π_i(x/2)−π_i(x))/3 queda de hecho |R₀|≤4, por integridad del numerador. Un primo que alcanza ese rango satisface

    y = x/3 + x log(4/3)/(3 log x) + O(x/log²x).

Para comprobarlo usar π_i(cx)=li(cx)/2+O(x/log⁴x) uniformemente en 1/4≤c≤1/2. Tras extraer x/(2 log x), la combinación de las tres li en la fórmula de R tiene término principal −1+3c y siguiente [1−2(1+log 2)+3c(1−log c)]/log x. El primero obliga a c=1/3+O(1/log x); sustituir en el segundo da log(3/4)/log x. El redondeo de la cuenta en una unidad queda absorbido.

**Persistencia en una banda fija.** Para c=1/4 o 1/2, el PNT en progresiones y sumación parcial para u_p=1−χ(p)cos(t log p) dan, uniformemente en 0≤t≤1,

    R_t(x,cx)=−2x/log x · Σ_(m≤3) b_t(m)(1/m−c)₊ + O(x/log²x).

En t=0 el perfil vale −1/4 y 1/2 respectivamente. En todo [0,1] el segundo perfil es 1/2, y el primero es 3/4+b_t(2)/4+b_t(3)/12≤1/4−cos(log 2)/2<0. Así los signos se conservan con margen en toda esa banda. En cada salto al admitir p en el bloque suave, el cambio en R tiene módulo ≤4Σ_(m≤3)|b_t(m)|≤36. Los extremos de signo opuesto garantizan un valor de módulo ≤18, escogiendo el extremo más próximo a cero del primer salto que lo cruza. La elección es medible por comparaciones finitas. El argumento unilateral de 292 funciona en el interior de cualquier intervalo fijo de longitud positiva, pues allí también se puede localizar el peso que detecta un polo. Por la propiedad 1-Lipschitz de la parte positiva, quitar el bloque R modifica el promedio en O(1).

**Alcance.** La ronda 302 calcula una masa grande para un corte en la raíz, y 295 equilibra el bloque suave mediante otro corte próximo a la raíz. Aquí se equilibra el complemento mismo con saltos de tamaño constante, gracias a que los cofactores sólo pueden ser 1, 2 y 3. Sigue pendiente estimar la suma sobre los enteros con todos sus primos por debajo de este corte.
