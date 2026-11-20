# El signo en cortes logarítmicos fijos detecta cualquier cero exterior

Para t∈[1,2], k>4 fijos y x grande, definir y=x/(log x)^k. Se tiene la equivalencia

    RH ⇔ para cada t∈[1,2] y cada k>4 se cumple eventualmente R_t(x,y)<0.

Basta exigirlo en la sucesión k=4+1/n. No se exige uniformidad del umbral en t ni en n. Si hay un cero exterior, para casi todo t y todo k suficientemente próximo a 4 por arriba hay x arbitrariamente grandes con R_t(x,y)>0. Este converse añade la dirección ausente en el falsificador de 305. La estimación eventual incondicional en estos cortes sigue abierta.

**Dirección bajo RH.** El transporte exacto de 305 vale en toda la banda y 292 da |B_t(v)|≪_σ v^σ para σ>1/2 (aquí B_t es el sumatorio). El cambio desde √x hasta y cuesta O_σ(x(log x)^(−1−k(1−σ))). Elegir σ con k(1−σ)>2. En √x el equivalente de 294 es −2D_t''(1)x/log³x, con D_t''(1)>0, donde D_t es la serie de Dirichlet de b_t. Por tanto ese equivalente se conserva.

**Expansión en la escala móvil.** Escribir z=(log x)^k, L=z^(1/k), F(z)=−L R_t(x,x/z)/(2x) para z suficientemente grande, extendida por cero desde 1 hasta ese umbral. Al sumar primero el primo grande, el PNT en las dos clases, con resto de potencia logarítmica arbitraria y |t|≤2, sustituye los dos extremos por li(x/m)−li(x/z) para cada m≤z, con el factor −2 de la definición de R. La norma Σ_(m≤z)|b_t(m)|/m es O(log^4(2z)); log(x/z) es comparable a L. Para cada entero fijo M se obtiene

    F(z)=Σ_(0≤j<M) z^(−j/k) H_j(z) + O_(M,k)(z^(−M/k)(1+log z)^(M+5)),
    H_j(z)=Σ_(m≤z) b_t(m)[P_j(log m)/m−P_j(log z)/z],
    P_j(u)=Σ_(r=0)^j (j!/r!) u^r.

En efecto expandir L li(x/m)/x en 1/L uniformemente para log m≤log z, y análogamente en el extremo z. El polinomio satisface P_j−P_j'=u^j. En particular H₀ es el perfil J de la frecuencia respectiva. La expansión es de la función firmada, antes de tomar signos.

**Mellin y detección.** Con transformada ∫₁^∞ f(z) z^(−1−s) dz se tiene exactamente

    Mellin(H_j)(s) = (−∂_s)^j [D_t(1+s)/(1+s)] / s.

En efecto H_j(1)=0, su derivada entre enteros es B_t(z)(log z)^j/z² y es continua en cada entero. Integrar por partes, inicialmente en Re s>0. Así cada corrección desplaza sus singularidades hacia la izquierda en j/k. La expansión anterior continúa el Mellin de F meromórficamente en Re s>max(−M/k,−1/2); la modificación compacta sólo añade una función entera. En los puntos reales s>−2/k es regular: D_t es regular en el eje real de esa región y su cero doble en 1 hace removibles los denominadores s+j/k para j=0,1. Para j≥2 esos puntos ya están fuera del intervalo.

Dado un cero exterior ρ de ζ, elegir t tal que D_t tenga polo en ρ; por 292 esto vale para casi todo t. Elegir k>4 con Re ρ−1>−2/k y M>k/2. Entre los puntos ρ+j/k, j entero no negativo, que sean polos de D_t, tomar el más a la derecha, w (la serie es holomorfa a la derecha de 1). En s=w−1, no real, el Mellin de H₀ tiene polo. Todas las correcciones son regulares allí por la elección de w. En consecuencia F tiene un Mellin con singularidad no real a la derecha de −2/k, pese a ser regular en todos los puntos reales de ese tramo. Si F fuera eventualmente de signo fijo, Landau aplicado tras descartar un compacto obligaría al Mellin a converger y ser holomorfo en todo ese semiplano. La contradicción prueba ambas oscilaciones. Incluso restar a F una constante por z^(−2/k) conserva el argumento, pues el polo real añadido queda en la frontera. Esto evita confundir un cruce minúsculo de H₀ con el cambio efectivo de signo en el sumatorio aritmético.

**Fila cero.** El mismo argumento en t=0 usa el cero de orden cuatro de D₀ en 1 y el término negativo de orden x/L⁵ de 302. Detecta cada polo efectivo w de D₀ con Re w>1−4/k en k>8; un cero compartido y cancelado con L puede ser invisible en esa fila. La banda [1,2] en el enunciado principal evita esa salvedad.
