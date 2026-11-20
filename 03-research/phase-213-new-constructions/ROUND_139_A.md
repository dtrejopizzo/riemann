# El borde de Liouville es lineal en la raíz con error uniforme

Para la suma de 138 con f=λ y 1≤x≤D² se tiene incondicionalmente

    S_D(x)=2√x Σ_{a≤D}λ(a)/√a − A(x) + E_D(x),   |E_D(x)|≤2D,
    A(x)=Σ_{r≤x}μ(r) P(√(x/r)),   P(z)=Σ_{ij≤z}1.

En efecto, invertir las dos sumas del borde de 138, donde g es el indicador de cuadrados, da exactamente 2Σ_{a≤D} λ(a) floor(√(x/a)). Sustituir cada suelo por su argumento cuesta a lo sumo dos unidades por índice. La expresión de A se obtiene de μ*g*g por convolución. Así toda la parte de borde que pudiera superar D es una única función de x cuyo coeficiente depende de D.

**Cancelar el coeficiente antes de estimar.** Definir C(x)=A(16x)−4A(4x)+4A(x). Para 16x≤D², la misma combinación aplicada a S_D da −C(x) con error ≤18D. En el interior de C se obtiene la identidad exacta

    C(x)=Σ_{r≤16x} μ(r) J(4√(x/r)),
    J(z)=Σ_{ij≤z}(−1)^(i+j)=P(z)−4P(z/2)+4P(z/4).

La hipérbola de Dirichlet corta esta suma en dos franjas i≤√z o j≤√z, restando el cuadrado contado dos veces. Cada suma alternada interior tiene módulo ≤1, por lo que |J(z)|≤2√z+1 para z≥1. Por tanto todos los r≤x^(1/3) juntos cuestan en valor absoluto O(x^(1/4)Σ_{r≤x^(1/3)}r^(−1/4)+x^(1/3))=O(√x). Esta estimación elemental paga a la vez la parte de borde y las dos sumas de divisores de los r pequeños a escala raíz cuando D es comparable a √x.

**Qué signo bastaría.** Para todo ε>0 una cota superior C(x)≪ε x^(1/2+ε) eventual basta para RH, y bajo RH se cumple incluso en módulo por 138 o por convolución. En efecto en Re s>1 la Mellin de C sobre (0,∞) es

    (16^s−4·4^s+4) ζ(2s)² / [s ζ(s)].

El tramo inferior a 1 tiene soporte alejado de cero y aporta una función entera. El factor de dilatación es (4^s−2)² y no se anula en Re s>1/2. Tampoco se anula ζ(2s) allí. El eje real en esa franja es regular. Landau aplicado a una constante por x^(1/2+ε) menos C excluye polos más a la derecha que 1/2+ε. Por la estimación absoluta anterior basta la cota unilateral para r>x^(1/3).

**Límite de una inducción por dilataciones.** Invirtiendo las dos sumas finitas también se tiene C(x)=Σ_{k≤4√x} b_k M₀(16x/k²), b_k=Σ_{ij=k}(−1)^(i+j). El término k=1 es M₀(16x). A escala raíz una inducción por valores absolutos tendría que pagar |b_k|/k por dilatación. Ya los primos impares tienen b_p=2 y Σ_p 2/p diverge. La mera alternancia dentro de J no produce una contracción absoluta. Queda abierta la cancelación entre dilataciones o, equivalentemente aquí, la estimación del resto sobre r grandes.

**Cotejo.** Los filtros de dilatación y los cortes por hipérbola ya son herramientas del corpus (entre otros 045, 060 y 132); la transferencia general es 138. La observación específica es el borde exacto de λ a error 2D y la elección de un mismo filtro que lo anula y alterna ambas coordenadas del divisor de cuadrados. No se infiere una extensión de la ventana.

Basta comprobar el techo unilateral en x=m². El coeficiente de A en n=rs², con r libre de cuadrados, es μ(r)τ(s) (equivalentemente, en p^j es (−1)^j(floor(j/2)+1) por su factor local). Por ello cada salto es Oε(n^ε). Pasar de m² a cualquier x antes de (m+1)² cuesta Oε(x^(1/2+ε)) para cada una de las tres sumas. El coste absoluto del sector r pequeño ya es O(√x) en todos los x.

Antecedente directo del coeficiente: 054/055 ya emplean ε*ε (ε(n)=(−1)^(n+1)); 057 trabaja con η² en Mellin. El nuevo uso de 139 es el borde de Liouville y el argumento escalado 4√(x/r).
