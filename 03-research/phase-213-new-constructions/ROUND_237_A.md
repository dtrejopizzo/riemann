# Ventanas de tamaño X^(2/3) donde la primera componente ya pasa el techo, incondicionalmente

Sea F la suma coseno de 236 con pesos sobre primos simples. Se tiene sin asumir RH

    limsup F(x)/√x ≥ 0.24,      liminf F(x)/√x ≤ −0.24.

En particular hay enteros n→∞ con |F(n)|≪log n. Más aún, en esa misma sucesión, para 1≤L≤n,

    n^(−2) ∫_n^(n+L) F(x)²dx ≪ L(L+1)² log² n/n².

Tomando L=n^(2/3) se obtiene O(log² n). Esto cumple la escala subpotencia incluso si falla RH: una ventana de esa longitud no puede sustituir a las ventanas de 236 con la misma normalización. No se afirma optimalidad del exponente 2/3. Para L=n^c con c<2/3 el techo obtenido tiende a cero.

**Comparación de dos residuos.** Por 236 ya se conocen bajo fallo de RH excursiones de ambas señales con exponente estrictamente mayor que 1/2. Para abarcar el otro caso suponer RH durante este argumento. Sea P(s)=Σ_p(log p)p^(−s) y M(s)=H(s)P(s), el Mellin unilateral de F. F(x)=O_ε(x^(1/2+ε)) por 235, por lo que la integral converge absolutamente a la derecha de 1/2. Para proseguir hasta los dos puntos fronterizos usar

    P(s)=−ζ'(s)/ζ(s)−P(2s)−Σ_(l≥3)P(ls).

La cola converge localmente para Re s>1/3. En s=1/2 el polo de P(2s) tiene residuo 1/2 porque P(z) tiene residuo uno en z=1. En ρ₁=1/2+iγ₁ ese término es regular, pues ζ no tiene ceros en Re z=1 y 2ρ₁≠1. Por tanto los residuos de M son −H(1/2)/2 en el eje real y −mult(ρ₁)H(ρ₁) en ρ₁.

Si F(x)≥−c√x eventualmente, integrar la función no negativa F(x)+c√x desde ese umbral. Para σ>1/2 el módulo de su Mellin en σ+iγ₁ no supera su Mellin real en σ. Multiplicar por σ−1/2 y pasar al límite da mult(ρ₁)|H(ρ₁)|≤c−H(1/2)/2, pues el prefijo retirado es entero en s. Bajo el supuesto F(x)≤c√x eventualmente, el mismo argumento con c√x−F(x) da mult(ρ₁)|H(ρ₁)|≤c+H(1/2)/2. Ambas conclusiones son imposibles para c=0.24.

**Certificado.** El verificador verify_237.py usa bolas Arb en 1024 puntos medios de [1,2]. Para y^(−1/2+it)cos(2πy) el supremo del módulo de la derivada respecto de y es ≤|−1/2+it|+2π; el error de la regla del punto medio con esa cota es a lo sumo el supremo dividido por 4096. Para la ordenada se calcula en t=14.135 y se agrega 1/200 por la derivada en t de H, de módulo ≤log 2, cubriendo el intervalo certificado 14.13≤γ₁≤14.14 de Z1. Se comprueba |H(1/2)|<0.01, Re H(ρ₁)<−0.16 e Im H(ρ₁)>0.20, de donde |H(ρ₁)|>0.25. El certificado sólo decide el margen de residuos.

**Cruces y ventanas.** La estimación de 236 entre x∈[n,n+1] y n es O(log n); las excursiones dan enteros de ambas señales arbitrariamente lejos y, entre ellos, enteros con |F(n)|≪log n. Desde cada uno, telescopar la misma estimación hasta n+L para dominar el supremo por C(L+1)log n. Integrar el cuadrado da el techo anunciado. Esto prueba existencia de ventanas buenas con un tamaño creciente en las dos alternativas para RH. Las de 236 que sí detectarían el signo tienen longitud X^(1−o(1)), con la condición más precisa sobre h de 231. No se ha construido la sucesión buena a ese tamaño.
