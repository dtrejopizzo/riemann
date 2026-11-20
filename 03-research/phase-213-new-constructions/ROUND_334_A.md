# Separar por máximo común divisor conserva la tasa que detecta los ceros

Sea B_q la energía firmada de 325 restringida a (n,d)=q, **incluida la diagonal** cuando n=d=q. Poner V_m=Σ_q |B_q|. Denotar por Θ el supremo de las abscisas de los ceros no triviales. Si h→0 y log(1/h)=o(m), entonces

    limsup V_m^(1/(2m)) = 1/(3/2−Θ).

Además, en h=exp(−am), RH implica limsup V_m^(1/(2m))≤1 para cada a>0 fijo. La condición para todos los a=1/j implica RH. Así se puede exigir el techo incluso después de tomar módulos por clase exacta. En la equivalencia de techo uno también se puede excluir la diagonal: cambiar cualquiera de las dos variaciones por la otra cuesta a lo sumo Δ_m=O(m^(−1/2)).

**Demostración.** Para pesos |b_q|≤1 escribir b_(n,d)=Σ_{g|n,d}c_g con |c_g|≤τ(g) como en 333. La energía sobre todos los múltiplos de g es una integral de Gram no negativa J_g. Por tanto V_m≤Σ_g τ(g)J_g. Los intercambios a m fijo se justifican por convergencia absoluta: Σ_{g|n,d}τ(g)≤τ(n)^2 y los pesos l_m decaen como n^(−3/2) por un polinomio en log n.

Para cada g libre de cuadrados, la serie de los coeficientes μ(n)1_{g|n} es

    F_g(s)=μ(g)g^(−s) ζ(s)^(−1) ∏_{p|g}(1−p^(−s))^(−1).

Para los demás g se anula idénticamente. La identidad procede primero del semiplano de convergencia absoluta. Tomar 0<r<3/2−Θ y σ=3/2−r. En cada disco de radio r centrado en 3/2+it, el producto finito de inversos cuesta a lo sumo C_(σ,ε) g^ε: para todo primo suficientemente grande (1−p^(−σ))^(−1)≤p^ε, y los primos restantes dan una constante. Aplicar Cauchy como en 325 al coeficiente de orden m de F_g, cuyo módulo al cuadrado integra a J_g contra la densidad W_m. La cota polinómica de 325 para el recíproco de ζ en esos discos da

    J_g ≪ g^(−2σ+2ε) r^(−2m) h^(−2C_r).

Elegir ε<σ−1/2, posible pues Θ≥1/2. La suma con peso τ(g) converge por la serie de ζ². La potencia fija de 1/h tiene raíz de orden 2m tendiente a uno. Luego el techo es 1/r para cada r permitido. El piso procede directamente de V_m≥E_m y de la igualdad de 325.

En la escala exponencial, bajo RH se usa la cota de 326 con exponente arbitrariamente pequeño η>0 en altura en vez de C_r. Para cada r<1 se obtiene un techo r^(−1)exp(aη). Tomar η→0 y luego r→1. El recíproco de la implicación para la sucesión 1/j se sigue otra vez de E_m≤V_m y 326.

**Alcance.** 333 prueba un ahorro incondicional en las clases exactas. Esta identidad muestra que, en la escala de 325, exigir el valor absoluto por clase conserva incluso la tasa exacta que detecta Θ. No proporciona aún el techo incondicional uno.
