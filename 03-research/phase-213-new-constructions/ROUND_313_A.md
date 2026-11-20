# Signo negativo con un hueco creciente y pesos positivos fuera del hueco

Fijar 0<θ<1/2, A>0 y una frecuencia t no excepcional de 312 en [1,2]. Para cada x grande poner L=log x y D=floor(exp(L^θ)). Existen pesos explícitos no negativos v_x(n), congelados en la ventana de observación, con v_x(1)=1 y v_x(n)=0 para 2≤n≤D. Si U_x(X)=Σ_(n≤X)v_x(n)B_t(X/n), entonces para φ y δ=L^(−A) de 312,

    ∫ φ(u) U_x(x(1+δu)) du ≤ −c_t √x / L^(3/2).

Además |U_x(X)|≪_ε x^(1/2+ε) para x≤X≤2x. A diferencia de 312 se permite crecer el hueco, y se modifican los pesos más allá de él. La desigualdad es para la media suavizada completa.

**Filtro positivo.** Elegir enteros N₁,N₂ en (D,C_t D] cuyas fases exp(−it log N_j) estén respectivamente cerca de exp(2πi/3) y exp(4πi/3). Se puede redondear hacia arriba una solución real de cada fase entre 2D y 2D exp(2π/t), con error angular O_t(1/D). Hay coeficientes a,b positivos y acotados uniformemente (resolviendo dos ecuaciones reales) con 1+a exp(−it log N₁)+b exp(−it log N₂)=0. Entonces

    P(s)=1+a√N₁ N₁^(−s)+b√N₂ N₂^(−s)

se anula en ambos puntos 1/2±it. Tomar m=ceil(K log D/log L), K fijo suficientemente grande según θ. Definir v_x por su serie igual a la de w_D de 310 multiplicada por P^m. La convolución conserva positividad, coeficiente inicial y hueco. Para cualquier σ>1/2 la norma de P^m en esa recta es (1+O_t(D^(1/2−σ)))^m=O_(t,σ)(1), de modo que la cota puntual sigue por 310 y D=x^o(1).

**El corte real conserva su signo.** Separar el factor h_D P^m del integrando de 312. En s=1/2−v real, 0≤v≤η=c/log D, el salto del factor de rama real aporta signo negativo con la orientación de 312; el factor analítico base es positivo y acotado por debajo para x grande, por continuidad y la elección de t. También Wδ es real positivo, P≥1 y h_D>0. Hay incluso un piso uniforme h_D(s)≫√D/log D en ese tramo. En la representación de Bernoulli de 312, cada primo D/2<p≤D sólo interviene en el sumando −X_p porque ningún múltiplo suyo distinto de p es ≤D. Esas variables son independientes del resto; la esperanza del cuadrado domina la suma de sus varianzas. Cada varianza es ≫D^(−1/2) en el tramo y hay ≫D/log D primos. Integrar sólo 0<v<1/L en este corte negativo da una contribución de módulo ≫_t √x L^(−3/2), con el resto del corte del mismo signo.

**Control de ambos cortes no reales.** Por 310 en Re s=1/2 la norma absoluta de h_D es O(D²), y su soporte es ≤D⁴. Al desplazarse v a la izquierda se pierde a lo sumo D^(4v). Por la anulación de P y la desigualdad e^u−1≤u e^u, en cada corte

    |P(1/2±it−v)| ≤ C_t v log(C_t D) exp(v log(C_t D)).

La discontinuidad restante cuesta O_t(v^(3/4)) por 312. Como (m+4)log(C_t D)=o(L), la exponencial adicional es absorbida por exp(−Lv/2). Integrando y usando la cota factorial de Γ(m+7/4), ambos cortes juntos cuestan a lo sumo

    O_t(√x D² L^(−7/4) (C_t(m+2)log(C_tD)/L)^m).

El logaritmo del último factor entre paréntesis es ≤−(1−2θ+o(1))log L. Escoger K>4/(1−2θ) absorbe D² con margen. Así el error es o(√x L^(−3/2)).

**Uniformidad del contorno.** Llevar primero el contorno infinito a 1/2+1/L como en 312, ahora con polinomios finitos para cada x. Truncar en T=D. En esa recta los nuevos factores cuestan O(D² C_t^m); el resto crece a lo sumo polinómicamente en L y la altura. La caída (1+δ|Im s|)^(−N) del núcleo, con N fijo suficientemente grande, absorbe todo eso en la cola. Usar la región sin ceros con borde 1/2−η. Para 0≤v≤η, los polinomios cuestan como máximo D² C_t^m exp((m+4)v log(C_tD)), y esta última exponencial se absorbe de nuevo en x^(−v/2). El resto en el contorno exterior cuesta una potencia fija de T y L, como en 312. En el borde izquierdo la ganancia exp(−ηL/2) domina cualquier potencia fija de D porque θ<1/2. En los bordes horizontales aumentar N absorbe esas potencias de D. Todo el contorno exterior es o(√x L^(−3/2)). Esto prueba la desigualdad con el signo del corte real.

La cancelación de los puntos no reales se obtiene mediante dilataciones enteras positivas mayores que D, sin reinsertar escalas vecinas de la muestra principal. Para deducir el signo global todavía faltaría una cota inferior para el saldo de las demás muestras, y pasar del promedio local a la cota unilateral puntual requerida por 292.
