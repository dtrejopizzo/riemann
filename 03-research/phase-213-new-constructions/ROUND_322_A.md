# Contracción uniforme del multiplicador observado en una franja explícita

En 320–321 tomar ahora L=log X, D=⌊exp(√L)⌋, N=C₀DL², corrección distribuida y C₀ suficientemente grande. El criterio de 320 sigue válido: D=x^o(1) en el bloque, y en la estimación de Poisson de orden ⌈L⌉ el cociente DL²/N permanece constante. Esta elección sacrifica la longitud polilogarítmica de la banda. El multiplicador efectivo en el modo x^s es

    K_X(s)=H_X(s) ∫ exp(su)dν_>(u).

Existen c,b>0 tales que, incondicionalmente, para X grande,

    sup_(1−b/√log D ≤ Re s ≤ 1) |K_X(s)| ≤ exp(−c√log D).

La cota es simultánea a todas las alturas. Además RH equivale a sup_(τ real)|K_X(σ+iτ)|→0 para cada σ fija en (1/2,1). La contracción demostrada sin hipótesis sólo ocupa una franja decreciente junto a 1. Se controla la acción en modos individuales; no se está iterando una norma sobre observaciones dependientes de la escala.

**Alturas altas.** Sea J=⌈L⌉. En |τ|≥L² cada uno de los primeros J factores uniformes de la cola (índices J+1,…,2J) tiene |τ|l_i acotado inferiormente por una constante positiva. Por la fórmula del seno cardinal, su transformada característica tiene módulo ≤r<1. Incluir el factor exp(σu) modifica cada factor en O(l_i) para 1/2≤σ≤1. El resto de la cola cuesta ≤exp(1). Así el filtro cuesta O(exp(−c₁L)). El polinomio H cuesta a lo sumo exp(O(log D)) en toda la franja, por los módulos de sus coeficientes. El producto a esas alturas es exponencialmente pequeño.

**Alturas restantes.** Para |τ|≤L² y 1/2≤σ≤1 se tiene

    1+H_X(s)=ζ(s)A_D(s)+O(exp(−c₂L)),    A_D(s)=Σ_d a(d)d^(−s).

Usar la continuación de la fórmula de Poisson de 321 para f(v)=ψ(v/N)v^(−s). Con j=⌈L⌉, la norma L¹ de f^(j) es ≤N^(1−σ−j)[C(j²+|τ|+1)]^j. En [N,2N] se aplica Leibniz, usando las cotas de orden dos de 320 sobre ψ; fuera de ese intervalo se integra directamente la derivada de v^(−s). La contribución de los modos no nulos, tras sumar d, es por tanto ≤N^(1−σ) O(log(2D)) [C' D(L²+|τ|)/N]^j, suficiente al escoger C₀. La integral principal se cancela antes de continuar en s; en 1 el producto ζA_D es regular.

**La recta 1.** Por la cota clásica de Mertens M(v)≪v exp(−c₃√log v) y sumación parcial, la cola a partir de D de Σ μ(n)n^(−1−iτ) y la de su primera derivada son O((1+|τ|)(log(2D))^C exp(−c₃'√log D)). Estas series dan el valor y la derivada del recíproco de ζ en la recta por límite desde la derecha. La corrección distribuida tiene coeficiente del mismo orden exponencial por el caso τ=0 y Σ μ(n)/n=0. Con |τ|≤L² se absorben los factores polilogarítmicos en el exponente. Así A_D−1/ζ y su primera derivada cuestan O(exp(−c₄√log D)) allí. En s=1 la diferencia vale exactamente cero; para |τ|≤1 esto paga el polo simple al multiplicar por ζ. Para 1≤|τ|≤L² basta |ζ(1+iτ)|≪log(2+|τ|) por sumación de Euler. Se obtiene el techo anunciado en la recta 1. Tres rectas de Hadamard para K_X entre 1/2 y 1, con el techo bruto exp(C log D) en 1/2, conserva una ganancia exponencial hasta distancia b/√log D si b es suficientemente pequeño.

**Alcance hasta la recta crítica.** Bajo RH, M(v)≪_η v^(1/2+η). Para σ>1/2 fija, la misma sumación parcial da A_D−1/ζ=O_(σ,η)((1+|τ|)D^(1/2+η−σ)) al elegir 0<η<σ−1/2; la corrección en D<d≤2D satisface también ese techo. En |τ|≤L² los factores de altura, incluido el crecimiento polinómico de ζ en esa recta, son D^o(1). En el resto rige el filtro de alturas altas, y por tanto el supremo tiende a cero. Recíprocamente, un cero exterior fijo ρ daría H_X(ρ)=−1+o(1) por la aproximación de alturas bajas. La probabilidad ν_> tiene soporte que se contrae a cero, de modo que K_X(ρ)→−1, contradiciendo la afirmación en σ=Re ρ. El caso de un cero crítico conocido da también ese límite en el borde 1/2. La ampliación del techo incondicional a cada recta interior permanece abierta.
