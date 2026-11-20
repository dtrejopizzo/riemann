# Bandas elegidas por un cruce armónico de Möbius

Sea H_D=Σ_{d≤D}μ(d)/d. Hay una sucesión incondicional de enteros D→∞, seleccionables con aritmética racional por |H_D|≤1/D. En *cada una* de las bandas [D,D²] así elegidas, la deriva lineal de la fórmula cuadrática exacta para los incrementos de Mertens tiene módulo ≤1 en todos los subintervalos. La diagonal de esa fórmula cuesta a lo sumo D. Queda controlar las diferencias de un único término fuera de diagonal.

**Existencia del corte.** Para H(x)=H_floor(x), la Mellin unilateral ∫₁∞H(x)x^(−s−1)dx es 1/[sζ(1+s)] en Re s>0. El origen es removible, y el segmento real (−1,∞) es regular (ζ no tiene ceros reales entre 0 y 1). Un cero no trivial ρ da un polo en ρ−1, con parte real mayor que −1. Si H tuviera signo constante débil desde algún punto, Landau, tras retirar un segmento finito y cambiar signo si procede, exigiría una singularidad real en la abscisa. Dicha abscisa es ≤0 y ≥Reρ−1 por el polo. Contradicción. Hay, pues, ambos signos arbitrariamente lejos. Si se pasa por cero ya se cumple la cota; si se cambia directamente de signo, el valor después del salto tiene módulo ≤1/D por el tamaño del salto. No se postula frecuencia de esos cruces.

**Identidad local.** Sean M₀(x)=Σ_{a≤x}μ(a), g=μ·1_{a≤D}, e=μ−g. Por convolución de Dirichlet, μ=2g−g*g*1+e*e*1, porque μ*1 es la unidad convolutiva. El último término sólo tiene soporte a partir de (D+1)². Para D≤u≤v≤D² el incremento de 2g es cero y queda exactamente

    M₀(v)−M₀(u)=−(v−u)H_D² + Q_D(v)−Q_D(u),
    Q_D(x)=Σ_{a,b≤D} μ(a)μ(b){x/(ab)}.

Los extremos pueden ser reales. La parte diagonal de la diferencia de Q_D cuesta ≤Σ_{a≤D}μ(a)²≤D; la cota vale simultáneamente en todos los subintervalos. En los cruces anteriores la deriva cuesta ≤D²H_D²≤1. Por tanto el supremo de los módulos de los incrementos del término fuera de diagonal y L(D,D²) difieren a lo sumo D+1.

**Blanco que sigue abierto.** Por 133 bastaría, en una subsucesión de estos cruces, una cota D^(1+o(1)) para el supremo de las diferencias fuera de diagonal. Bajo RH la cota vale en todos los cruces por la identidad y el techo clásico de Mertens. El mero hecho de cruzar controla una sola suma lineal de los μ y no da la cancelación cuadrática requerida. Para Θ>1/2, 133 implica que en todos los cruces grandes el supremo fuera de diagonal tiene exponente 2Θ+o(1) en D; la deriva y la diagonal no podrían generar ese exceso.

**Cotejo.** La identidad de inversión truncada, los suelos y el argumento de Landau son ingredientes clásicos; véanse también R162_801 para el registro factorial y 129–132 para las compensaciones de momentos. Lo que se usa aquí es la elección efectiva de la banda de 133 mediante cruces de H_D para pagar simultáneamente toda la deriva de la identidad de dos factores. Es una sucesión con esa propiedad parcial, no una sucesión ya demostrada de bandas con todos los incrementos pequeños.
