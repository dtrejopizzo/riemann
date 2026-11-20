# Límite de energía para una mezcla suave fija de traslaciones de BUILD084

Cotejo: 106_47 §2, lema 2, contiene la cuadratura móvil de primos. La aplicación aquí trata la energía completa de una mezcla ligada, incluidos el peine y el símbolo arquimediano. Frente a los restos libres de 213-11, la cola tiene una forma límite tras reescalar, y el momento inverso de la cabeza límite paga el término continuo del peine.

Fijar una densidad compleja μ suave de soporte compacto en [0,δ]. Sea Y_k=∫ μ(s)V_s F_k ds. Escribir en la variable física Y_k=U(A_k+D_k), donde Uf(t)=exp(t/2)f(exp t). Por la fórmula de BUILD084, A_k es la mezcla física de la cabeza de f_k y converge, con todas sus derivadas en un compacto común de (0,∞), a A, la misma mezcla de b1_[1,2)−a1_[2,3). Esto resulta integrando μ(s)exp(−s/2) sobre intervalos de extremos logarítmicos. En particular ∫A(x) dx/x=0, ya que b log 2−a log(3/2)=0 y el momento inverso es invariante bajo x↦exp(−s)x.

En la cola se tiene D_k(x)=k⁻¹ G_k(x/k), con

    G_k(y)=kd ∫_[log y−w, log y] μ(s)exp(−s/2)ds,     w=log(1+1/k).

Como kw→1, converge con todas las derivadas a G(y)=d μ(log y)y^(−1/2) en un compacto común de (0,∞), y se extiende por cero fuera de él. Por ello UD_k=k^(−1/2)V_(log k) UG_k. Su autoenergía completa es O(1/k), por covariancia y acotación de la forma en estos perfiles suaves de soporte fijo. Su cruce arquimediano con UA_k es O(k^(−1/2)) por Cauchy–Schwarz con el peso |m| y acotación uniforme de las normas ponderadas. La energía de UA_k converge a la de UA por la misma regularidad y ventana fija.

Para k grande sólo hay un sentido posible de contacto entre los dos soportes. El cruce del peine que se resta es

    2 Re k⁻¹ Σ_n Λ(n) Φ_k(n/k),    Φ_k(v)=∫ conjugado(A_k(x)) G_k(vx) dx.

En efecto la correlación logarítmica aporta √n que cancela el denominador del peine. Las Φ_k convergen uniformemente a Φ(v)=∫ conjugado(A(x)) G(vx)dx y tienen soporte compacto común en (0,∞). La cota de Chebyshev permite cambiar Φ_k por Φ con error o(1). Por el teorema de los números primos en su forma de cuadratura, k⁻¹ Σ_n Λ(n)Φ(n/k)→∫Φ(v)dv. Por Fubini este límite es (∫conjugado(A(x))dx/x)(∫G(y)dy)=0. En consecuencia a(Y_k)→a(UA).

**Consecuencia para el signo.** La cabeza inicial tiene energía q(0)>0.15 por BUILD084. Elegir δ₀>0 según 213-10-A para esa cabeza. En la prueba de aquel resultado, el menor autovalor de la matriz de dos por dos es estrictamente positivo. Como ||cF+g||²≤2 max(1,||F||²)(|c|²+||g||²), la forma domina una constante positiva por la norma cuadrada en todo el espacio generado. La cota pasa a la mezcla integral UA por sumas de Riemann en la norma con peso 1+|m| (continuidad de la traslación y soporte en ventana fija). Para μ no nula, UA tampoco se anula: su transformada es el producto de las transformadas enteras de dos funciones compactas no nulas. Luego, para cada μ suave no nula soportada en [0,δ₀], el límite es estrictamente positivo y existe k₀(μ) tal que a(Y_k)>0 para todo k≥k₀(μ).

La prueba usa PNT sólo para un test límite fijo. Sigue abierta la uniformidad del umbral en μ y el signo global. PROVED, incluida la consecuencia de signo, tras revisión matemática independiente.
