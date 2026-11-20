# Peso fraccionario del carácter trivial

Para \(x\ge1\), sea \(G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x\).
La reducción unilateral requiere \(G(x)\le C_\epsilon x^{1/2+\epsilon}\)
para cada \(\epsilon>0\). El signo depende de la distribución de los primos
a escalas arbitrarias. Lo que sigue comprueba qué información espectral
sobrevive a la sustitución por primos grandes.

Para \(\Re s>1\), integración término a término (absoluta) da
\[
 \int_1^\infty G(x)x^{-s-1}\,dx
 =-\frac{\zeta'(s)}{s(s-1)\zeta(s)}
   -\frac{1}{(s-1)^2}+\frac{1+\gamma}{s-1}.
\]
En efecto la integral de \(x/n-1\) desde \(n\) es \(n^{-s}/[s(s-1)]\).
La expansión de Laurent de \(\zeta\) comprueba la cancelación en 1.
En cada cero no trivial \(\rho\) de multiplicidad \(m\), el residuo
de la continuación es \(-m/[\rho(\rho-1)]\ne0\).

En los enteros, \(\sum_{n\le N}\Lambda(n)\lfloor N/n\rfloor=\log N!\).
Por Stirling, con \(w_N(t)=1-\{N/t\}\),
\[
 G(N)=\gamma N-\sum_{\sqrt N<p\le N}\log p\,w_N(p)+O(\sqrt N\log^2(2N)).
\]
El error incluye los primos pequeños, las potencias de exponente al menos dos
y el resto logarítmico de Stirling; basta \(0\le w_N\le1\).
En el intervalo \([N,N+1]\) la suma de von Mangoldt de la definición de
\(G\) es afín, y el error de interpolación lineal de \(G\) es a lo sumo \(1/(8N)\).

Por consiguiente la extensión escalonada a \(x\) del déficit de primos grandes,
tomando \(N=\lfloor x\rfloor\), difiere de \(G(x)\) en
\(O(\sqrt x\log^2(2x))\): en un intervalo unitario la pendiente de \(G\)
es \(O(\log^2(2x))\) por \(\Lambda(n)\le\log n\).
La transformada de Mellin de esta diferencia es holomorfa en
\(\Re s>1/2\) por convergencia local uniforme. El déficit de primos grandes
tiene por tanto el mismo residuo en cada posible cero a la derecha de la
recta. El corte en \(\sqrt N\) no atenúa ese residuo. La cota unilateral
para el déficit sigue pendiente.
