# Compensación firmada en la banda de semiprimos de 061

Sean S(x), f, G y u* los de 060–061; L=√x. Para un entero fijo h≥0, aplicar h veces la diferencia que envía S(x) a 4S(x)−S(4x). Escribir S_h para el resultado. En las pendientes cambia G(Z) por G_h(Z)=(4−D₂)^h G(Z), con D₂G(Z)=G(2Z).

**Criterio conservado.** El signo global equivale a S_h(j⁴)≤C√x eventualmente, x=j⁴. Si vale el signo cada término es O_h(√x) en valor absoluto. Recíprocamente S=o(x), pues Q=o(x) por PNT y la corrección compacta de 060, y Σ_k Q(x/k⁴)/x tiende a cero por dominación por C/k⁴. Lo mismo vale para cualquier número fijo de diferencias. El puente de interpolación de 060 vale también para sus traslaciones logarítmicas. Si 4H(x)−H(4x)≤M√x en toda la cola y H=o(x), iterar hacia 4^n x da H(x)≤M√x/(4−2). Repetir devuelve la cota superior de 060. Se elige h una sola vez.

**Banda que incluye todos los segundos primos de la resonancia.** Para B₀>2 fijo, poner R=L(log L)^B₀, P=L/√R y Q_p=L²/p³. Considerar los productos de dos primos en

    P≤p≤2P,      √R≤q≤C_h Q_p,

con C_h>(2^h u*)² fijo. Cada producto cuenta cuatro pendientes ordenadas. Sea W_h la suma firmada de todas ellas en S_h. Se obtiene

    |W_h| ≪_{h,B₀} R/(log L)^(h+2).

Así, si h>B₀−2, **la banda entera aporta o(L)** al criterio equivalente. El intervalo en q es esencial; recortar las dos familias de 061 por separado no justifica esta estimación.

En efecto T=L/√(pq) tiende a infinito como potencia de L en toda la banda; q/T y p²/T tienden uniformemente a infinito. En la expansión por valuaciones sólo intervienen 1,p, también después de las h dilataciones. La pendiente vale G_h(T)−G_h(√(Q_p/q)); el primer término cuesta menos que cualquier potencia inversa de L, incluso tras sumar. La función G_h es lisa, nula bajo un umbral fijo y decrece rápidamente junto con sus derivadas en el infinito (Poisson aplicado a las derivadas logarítmicas del perfil de integral cero).

Para el segundo término, PNT cuantitativo y sumación parcial sustituyen la suma sobre q por la integral con densidad 1/log q a error O_N(Q_p/log^N L), uniforme en p: el peso tiene variación total acotada, y q≥√R. Tras poner z=√(Q_p/q) la integral es

    2Q_p ∫_{1/√C_h}^{√(Q_p/√R)} G_h(z) z⁻³/(log Q_p−2log z) dz.

La Mellin de G_h, en la convención de 061, es (4−2^s)^h ζ(s)∫f(u)u^(s−1)du. Sus derivadas de órdenes 0,...,h−1 en s=2 son cero. Expandir el denominador hasta esos h términos: log Q_p y log q son comparables a log L en todo el intervalo, por lo que el resto integrado es O_h(1/log^(h+1)L) gracias al momento absoluto finito con |log z|^h. El extremo inferior queda bajo el soporte y el superior es comparable a (log L)^(B₀/2); completar cada momento hasta infinito cuesta una potencia inversa arbitraria de log L. Para h=0 basta la cota directa por 1/log L. El coste por p es O(Q_p/log^(h+1)L); por PNT Σ_{P≤p≤2P} Q_p≪ R/log L. Las dos familias de signos de 061 pueden construirse también para cada G_h fijo: es no nulo por su Mellin y su momento en −2 sigue siendo cero.

**Signo en el representante original.** Para h=0 hay además una asintótica, incluyendo las cuatro pendientes,

    W₀ ∼ −3 M_G(2) R/[log P · log(L²/P³)],    M_G(2)=∫G(z)z⁻³dz>0.

El primer término de la expansión integral vale 2Q_p M_G(2)/log Q_p. La suma de p⁻³ en [P,2P] es asintótica a 3/(8P² log P), y log Q_p=log(L²/P³)+O(1). Para comprobar el signo, escribir I(z)=2^(z−1)V̂(z/2)η(z/2)² como en 057. Se tiene M_G(2)=ζ(2) I(2)[I'(2)/I(2)−b₀]. La derivada logarítmica en s=1 de V̂ es al menos 1−(16/255)log16: el factor de promediado P de 047 aporta al menos su media 1/2 (la inclinación exponencial positiva aumenta la media), y la derivada logarítmica del sombrero de 060 es 1/2−(16/255)log16. En η se obtiene η'(1)/η(1)=γ_E−(log2)/2 por la expansión de ζ en 1; en 1/2 la ecuación funcional da γ_E/2+π/4+(log π)/2−(1/2+√2)log2. Por tanto

    I'(2)/I(2)−b₀ ≥ 1/4+γ_E/2−π/4−(log π)/2+(√2−32/255)log2 > 0

(incluso usando γ_E>0.57, π<22/7, log π<1.15, √2>1.41 y log2>0.69). La banda original tiene así un saldo negativo mayor en módulo que L; su signo favorece una estimación superior, aunque no paga su coste en una estimación bilateral.

**Alcance.** Las diferencias de dilataciones y la recuperación unilateral ya aparecen en 054. La operación específica es imponer ceros de momentos en s=2 a la función de la resonancia de dos primos, y verificar la precisión de raíz para todo el intervalo de q. Para cada B₀ se usa un orden fijo; no se toma un límite en h. Los demás rangos de primos y las demás factorizaciones siguen sin estimación global.
