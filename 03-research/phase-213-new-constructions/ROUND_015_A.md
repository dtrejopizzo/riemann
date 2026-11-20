# Todos los coeficientes firmados en la escala de la celda lejana

Antecedentes 213-10 a 014 y BUILD084. La operación nueva recupera la primitiva de los coeficientes en dos franjas complementarias de la cola. Esto hace el error relativo a la norma de la cola aun con cancelaciones arbitrarias. Usamos PNT para un test de cabeza fijo por tramos, conservando toda la cola. Se cotejó el mecanismo antes de desarrollarlo.

**Enunciado.** Existe k₀ tal que para cada k≥k₀ la energía completa es estrictamente positiva para toda combinación no nula de traslaciones de F_k en un intervalo de longitud w=log(1+1/k). Se admiten medidas complejas finitas de coeficientes. Todos los desplazamientos se pueden trasladar simultáneamente para tomar el intervalo [0,w].

**Recuperación en dos franjas.** Denotar por μ la medida, por ν(ds)=exp(−s/2)μ(ds), por c su masa total y por L(u)=ν([0,u]) su acumulada, 0<u<w. En variable física la cola b, en y=k exp(u) y y=k exp(w+u), tiene respectivamente valores dL(u) y d(c−L(u)), salvo puntos de salto irrelevantes. Sea D=Ub. Integrando en dy,

    ||D||² ≥ d² k ∫₀ʷ (|L|²+|c−L|²)du.

Como kw está acotado inferiormente para k≥3, |c|≤C||D||. La cabeza en coordenadas logarítmicas es cF+g donde F es la cabeza original de F_k. Por 012-A el resto g está en los tres tubos de saltos de ancho w y está construido con H=L−c en (0,w). Luego ||g||≤C||D||/√k. Si ||D||=0 entonces c=0 y g=0, luego toda la mezcla es cero. Estas cotas son independientes de la variación total de μ.

**Energías propias.** En la ventana fija de cabeza el peine es acotado y m tiene una cota inferior, así a(g)≥−C||g||². El funcional de cruce con F tiene representante L² de norma uniformemente acotada: F es combinación acotada de dos perfiles fijos BV, a los que se aplica 010-A. La diagonal a(F)=q(w)>0 para k grande por BUILD084. Por ello a(cF+g)≥−C||D||²/√k. Como el soporte logarítmico de D tiene longitud 2w, el piso de ventana fija de 010-A, tras trasladar, da a(D)≥||D||² para k grande. Las integrales de traslaciones contra medidas se toman en el dominio por continuidad en norma de forma en una ventana fija para cada k.

**Cruces mixtos.** Cada uno de los tres tubos de g sólo contacta con D para log n en un intervalo de longitud ≤3w situado a log k+O(1). Éste contiene O(1) índices enteros n tras exponenciar. El coste aritmético total entre g y D es O((log k)/√k)||g|| ||D||=o(||D||²).

Para el peine entre la cabeza original F=Uf y D, escribir la integral mixta como el emparejamiento físico de b(y) con

    S_k(y)=Σ_n (Λ(n)/n) f(y/n),     k≤y≤k exp(2w).

El factor 2 y la parte real del cruce completo se incluyen al acotar por 2|c| ||b||₁ sup|S_k|. Para i=1,2 las celdas [i,i+1) seleccionan y/(i+1)<n≤y/i. La sumación parcial de ψ(x)=x+o(x) da en cada banda ΣΛ(n)/n=log((i+1)/i)+o(1), uniformemente en ese rango de y (extremos comparables a k). Los coeficientes de f están acotados y su momento inverso es −dw. Así sup|S_k|=o(1). El soporte físico de b tiene longitud k(exp(2w)−1)=2+1/k. Por tanto ||b||₁≤C||D|| y el coste mixto es o(||D||²).

Finalmente el núcleo arquimediano físico entre cabeza y cola es O(1/k) por separación, como en 014-A. Los soportes físicos tienen longitud acotada y las normas L² son O(||D||), así que este último cruce es O(||D||²/k). La fórmula fuera de diagonal pasa a medidas por aproximación de las integrales de traslaciones en norma de forma para cada k.

Se concluye a(Y)≥(1−o(1))||D||², uniformemente en los coeficientes. El radio explícito w decrece con k. El resultado deja abierta la positividad de toda combinación firmada en un radio fijo independiente de k, y la de la ventana completa. Estado PROVED tras revisión independiente.
