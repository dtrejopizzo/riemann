# Un reparto binomial fijo no reproduce el peso logarítmico con dilataciones positivas

Para 0<y<1 poner K_y(t)=floor(t)−floor(yt)−floor((1−y)t), que vale cero o uno. Permitir cualquier distribución de probabilidad fija de y en (0,1) y escribir K para el promedio. No existe medida positiva ν sobre [1,∞) con ∫K(t/u)dν(u)=log t para todo t≥1 (también imposible casi por doquier).

Para s>1 real, Tonelli y la integración de cada piso dan la transformada de K respecto de dt/t^(s+1) como ζ(s)A(s)/s, con A(s)=1−E[y^s+(1−y)^s]. Es estrictamente positiva. La representación obligaría a

    ∫ u^(−s)dν(u)=1/[s ζ(s) A(s)].

A es holomorfa en Re s>0 por dominación local. En el semieje positivo A sólo se anula en 1 y allí su derivada es la esperanza de −y log y−(1−y)log(1−y), estrictamente positiva. Su cero cancela el polo de ζ en 1. El lado derecho es por tanto regular en todo el eje real positivo (ζ tampoco se anula en 0<s<1). Por Landau para la transformada de una medida positiva en log u, la abscisa de convergencia tendría que ser ≤0. La transformada sería holomorfa en Re s>0, incompatible incluso con el primer cero crítico de ζ: el producto sζ(s)A(s) se anula allí. El argumento no supone RH.

**Fallo local en el reparto simétrico.** Para y=1/2 el núcleo salta por (−1)^(n−1) en n. Si G(t)=ν([1,t]), la inversión de la convolución en divisores fuerza G(t)=Σ_{n≤t}b_n log(t/n), donde b_n=μ(n)+2 b_(n/2) (último término sólo para n par), por la serie de Dirichlet del salto (1−2·2^(−s))ζ(s). Así tG'(t)=Σ_{n≤t}b_n. Los valores acumulados desde n=1 hasta 13 son 1,2,1,3,2,1,0,4,4,3,2,0,−1. La masa requerida es negativa en (13,14). La comprobación sólo usa enteros hasta 13.

**Límite.** Se descarta la representación exacta con distribución del reparto independiente de la escala. Una mayoración con error suficientemente pequeño o una distribución que cambie con la dilatación no está decidida aquí. 098 da una pérdida cuantitativa para pisos sin restas; este núcleo admite una resta pero mantiene cada recuento no negativo.
