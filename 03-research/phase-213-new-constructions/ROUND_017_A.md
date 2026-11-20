# Absorción del cruce por las dos energías localizadas

Antecedentes 010-A, 012-A y 016-A. Conservamos por separado las energías crecientes de ambos restos. La reconstrucción desde toda la cola de 016-A se sustituye aquí por la observación directa de H en el primer salto de cabeza. El cotejo previo se refiere al alcance local para F_k, sin exclusión de otros mecanismos.

Para algún θ>0 fijo y todo k suficientemente grande, cualquier mezcla no nula de traslaciones de F_k en un intervalo de longitud r=θ/√k tiene energía estrictamente positiva. Admitimos medidas complejas finitas. Usamos Y=cF+g+D, c, H, y b=U⁻¹D como en 016-A, con la medida soportada en [0,r] por traslación. Las identidades de masa de 016-A valen para cualquier r (su demostración por Fubini no usa r/w entero). En el tubo [0,r] del primer salto, separado de los demás para k grande, g(t)=exp(t/2)(log(3/2)−w)H(t) casi en todas partes. Por ello ||H||₂≤C||g||₂. Aquí y abajo las constantes son independientes de θ para 0<θ≤1 y k suficientemente grande según θ.

**Piso local.** En ventana de longitud fija la norma del peine está acotada. Para cualquier vector Z del dominio soportado en un conjunto de longitud total ≤3r, la proporción de su masa Fourier en |τ|≤r^(−1/2) es ≤3√r/π por Cauchy–Schwarz y Plancherel. Fuera de esa banda m(τ)≥(1/2)log(1/r)−O(1) por P47 lem:mbounds. En la banda m tiene cota inferior fija. Se deduce a(Z)≥κ log k ||Z||² para k grande, tomando por ejemplo κ=1/8 ya que r≤1/√k. Vale para g en la ventana fija de cabeza y para D tras trasladarla a una ventana fija: sus soportes tienen respectivamente longitud ≤3r y r+w≤2r. Es importante comprimir el peine en esas ventanas separadas sólo para las dos autoenergías.

**Estimación mixta.** En cada tubo de g, sólo O(1+kr) enteros de tamaño comparable a k contactan con D. La norma de cada traslación es uno y su peso es O(log k/√k). El cruce aritmético entre ambos restos tiene módulo ≤C(θ+k^(−1/2))log k ||g|| ||D||. Elegimos θ>0 de modo que este término se absorba usando a lo sumo la mitad de los dos pisos anteriores para k grande.

La diagonal de F en la cabeza es q(w)>0.15 por BUILD084. El cruce de cF con g cuesta O(|c| ||g||) por el representante L² uniforme de 016. Para el cruce aritmético de cF con D, S_k(k)=o(1) por PNT; en el soporte físico de b la oscilación de S_k es O((1+kr)log k/k) por el conteo en los extremos de banda de 016. El soporte tiene longitud O(1+kr). Por la identidad de masa,
   
    |∫b| ≤ C(|c|+√r||g||),    ||b||₁ ≤ C√(1+kr)||D||.

La parte constante del cruce queda acotada por o(1)|c| (|c|+√r||g||). La parte oscilante cuesta O((1+kr)^(3/2)log k/k)|c| ||D||=o(1)|c| ||D||. El cruce arquimediano de toda la cabeza con la cola cuesta O(√(1+kr)/k)(|c|+||g||)||D|| por el núcleo separado de 014 y la longitud acotada del soporte físico de cabeza.

Finalmente la desigualdad de Young absorbe O(|c| ||g||) gastando menos de 0.05|c|² y un múltiplo fijo de ||g||², que cabe en el piso creciente. Los errores restantes son o(1)(|c|²+||g||²+||D||²). Resulta, para alguna constante c₀>0,

    a(Y) ≥ c₀ [ |c|² + log k (||g||²+||D||²) ].

En particular cualquier Y no nulo tiene energía estrictamente positiva. El radio aún decrece. Para r fijo el conteo crudo produce un coste de orden superior al piso local disponible, y la compensación aritmética adicional sigue abierta. Estado PROVED tras auditoría matemática independiente.
