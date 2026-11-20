# Exponente exacto de la oscilación local de Mertens en cada banda de potencias

Para h>0 fijo, B=Z^(1+h), sea L(Z,B)=max_{Z≤u≤v≤B}|Σ_{u<d≤v}μ(d)|. Entonces, sin suponer RH,

    lim_{Z→∞} log(1+L(Z,B))/log B = Θ = sup Reρ.

En particular, para cerrar el signo bastaría exhibir una sucesión no acotada de bandas con algún h fijo donde L(Z,B)≤B^(1/2+o(1)). Es suficiente controlar las variaciones de Mertens en esos intervalos, con un nivel de partida desconocido en cada uno. La identidad no asegura que esa sucesión exista.

**El testigo de 132 aparece en cada vecindad logarítmica.** Conservar un peso fijo w* de 132 elegido para detectar un cero con parte real arbitrariamente próxima a Θ, y escribir G*(s)=∫t^s w*(t)dt. Para X grande, su promedio de ψ(Xt)−Xt es

    J(log X)=−Σ_ρ G*(ρ)X^ρ/ρ + O(1).

En efecto por Perron suavizado se integra (−ζ'/ζ)(s)G*(s)X^s/s inicialmente entre 1 y 2 en parte real. La identidad se obtiene también por inversión de Mellin del peso de cola W. Trasladar a Re s=−1/4: G* es holomorfa en la tira por el comportamiento O(t) en cero y el decaimiento en infinito, y dos integraciones por partes logarítmicas dan O((1+|Im s|)^−2) uniformemente en esa tira cerrada. Usar alturas buenas de la fórmula explícita y la ecuación funcional en el borde izquierdo. El residuo en 1 y el término Xt se anulan por G*(1)=0; el origen es regular en el integrando por G*(0)=0. Se obtiene incluso error O(X^(−1/4)). La multiplicidad de cada cero multiplica el residuo correspondiente. La serie es absolutamente convergente.

Para todo η<Θ suficientemente próximo a Θ, cada intervalo [(1−q)T,(1+q)T] con q>0 pequeño fijo y T grande contiene t con |J(t)|≥exp((Θ−e)T), donde e>0 puede fijarse de antemano eligiendo η suficientemente próximo a Θ y q suficientemente pequeño. Para precisarlo, aplicar el lema gaussiano de 115 a z=ρ−1/2 si Θ>1/2. Elegir un cero con Reρ>Θ−e/4, un peso que lo detecte y una tasa d<Reρ−1/2 con d>Θ−1/2−e/2. Al desnormalizar se pierde a lo sumo qT/2 en el exponente. Para Θ=1/2 la serie normalizada es trigonométrica absolutamente convergente con un coeficiente no nulo. Su media cuadrática en cualquier intervalo de longitud que tiende a infinito converge, uniformemente en el origen, a la suma de cuadrados de sus coeficientes: truncar uniformemente la serie e integrar los términos cruzados finitos. Por tanto en cada intervalo hay módulo acotado inferiormente por una constante positiva. Esto cubre también Θ=1/2.

**Margen del error.** En 131–132 se puede elegir r tan grande que la cola alta cueste O(X^(1/3)) para el δ escogido, usando (1+2r)δ>2/3 con desigualdad estricta para absorber logaritmos. El extremo inferior cuesta O(X^(1/3)), y el coste factorial sin correctores es O(D²/X)=O(X^(1/3)). Así el error total queda por debajo de X^(2/5) eventualmente. Esto permite usar el argumento de producto también cuando Θ=1/2; un simple o(√X) no alcanzaría para esa inferencia. Se escoge primero δ,r, luego el cero y n.

**Colocar toda la suma local dentro de la banda dada.** Para un pequeño τ>0 tomar T=(3/2)(1−τ)log B. Elegir τ,q,δ pequeños en ese orden con

    (1−τ)(1+q)<1,
    (1−τ)(1−q)(1−3δ/2)>1/(1+h).

Así para todo t del intervalo, X=exp t tiene [κ X^(2/3−δ), floor(X^(2/3))] dentro de [Z,B] para B grande, por margen estricto. En el testigo anterior aplicar 132 y P≪ε X^((1/3+δ)(Θ+ε)). Se obtiene

    log(1+L(Z,B)) ≥ T[Θ−e−(1+q)(1/3+δ)(Θ+ε)−o(1)].

La pérdida X^(2/5) es despreciable para parámetros suficientemente pequeños incluso en Θ=1/2. Dividir por log B y dejar que τ,q,δ,e,ε tiendan a cero respetando los márgenes prueba liminf≥Θ. El limsup≤Θ es la cota clásica de Mertens usada en 132. La conclusión se refiere a todo Z grande para cada precisión fija, con constantes que pueden depender de esa precisión.

**Antecedentes y límite.** El detector en cada vecindad es 115; la cota de producto local viene de 132. La conclusión sobre incrementos de Möbius en todas las bandas usa ambos y la mejora cuantitativa del error de 131 para el caso crítico. La coincidencia en módulo de 132 por sí sola no da una contradicción: aquí se explica por qué las excursiones de Mertens pueden encontrarse en bandas prescritas sin información sobre los signos conjuntos.
