# Dos orientaciones: umbral exacto para encender el exponencial reflejado

Fijar a≥1/2 y δ≥0. En [−T,T] formar los dos tests reales
     
    g_±(t)=exp(at) ± exp(−2δT)exp(−at).

Para CADA signo por separado, la no negatividad eventual de W_T(g_±) equivale a |Re ρ−1/2|≤δ para todo cero no trivial. En particular, a δ=0, aun si a=10000, un solo cosh(at) en todas las ventanas grandes ya detecta el signo global; también lo hace un solo sinh(at). Las dos direcciones individualmente positivas de 083 no se pueden juntar gratuitamente. Para δ>0 en la franja declarada hay positividad estricta eventual. Se incluye la igualdad en el borde aun si existen ceros sobre él.

**Cálculo.** Sea z=ρ−1/2, b=Re z, γ=Im z. Escribir D_T=e^(−2aT)W_T(exp(at)) y C_T=e^(−2aT)W_T(exp(at),exp(−at)), con los cortes implícitos. Por 083 y convergencia dominada (cada |b|<1/2), D_T→D=Σ d_z>0, donde d_z=Re[1/(a²−z²)]>0. Para el cruce se multiplica la integral de exp((a+z)t) por sí misma. Así
    
    C_T=J(T)+O_a(exp(−2aT)+exp(−(4a−1)T)),
    J(T)=Σ_z exp(2zT)/(a+z)².

El primer error viene del término constante −2 del cuadrado de 2sinh((a+z)T); el segundo, de la exponencial decreciente. Las series convergen absolutamente para cada T y son reales por conjugación. Por reflexión las dos diagonales son iguales. La energía de g_± multiplicada por exp(−2aT) es (1+exp(−4δT))D_T ±2exp(−2δT)C_T.

**Si se cumple la franja.** Para δ=0 el resultado es la dirección de Weil bajo RH. Para δ>0 sólo los ceros con b=δ pueden sobrevivir en exp(−2δT)J(T), con resto o(1) por dominación. Para esos ceros
    
    |a+z|^(−2)/d_z = [(a−b)²+γ²]/[a²−b²+γ²] ≤ 1.

Aquí basta b≤1/2≤a; si δ≥1/2 la suma de borde es vacía. Por simetría d_z=d_{−conj z}, y el primer par crítico queda fuera de ambas líneas de borde. De ahí 2Σ_{b=δ}|a+z|^(−2)≤D−2/(a²+γ₁²). Para ambos signos el límite inferior de la energía escalada es al menos 2/(a²+γ₁²)>0. Si no hay ceros en el borde positivo, esa energía converge exactamente a D.

**Si falla la franja.** Si cualquiera de las dos energías fuese eventualmente no negativa, la identidad anterior daría un techo unilateral ≪_a exp(2δT) para uno de J o −J. Su Laplace, al principio para Re s>1, es Σ_z (a+z)^(−2)/(s−2z). Se prolonga meromórficamente por convergencia normal fuera de los polos y es regular en el eje real; cada polo en 2z lleva residuo no nulo, también con multiplicidades. Landau aplicado al mayorante menos la función sobre una cola excluye polos en Re s>2δ. Contradicción, sin exigir que la parte real suprema se alcance.

**Tasa sobre la familia explícita.** Sea Δ=sup Re z y tomar δ=0. Para cada una de las dos paridades, sea M_± la parte negativa del cociente W_T(g_±)/||g_±||², tomada en valor absoluto. Se tiene limsup log(1+M_±)/(2T)=Δ. En efecto la norma al cuadrado es comparable a exp(2aT) al crecer T; la serie da el lado superior. Si Δ>0, cualquier cota exponencial con exponente η<Δ para esa parte negativa, con 0≤η, impondría un techo unilateral O(exp(2ηT)) para ±J (según la paridad), contradicción por el mismo argumento. Para Δ=0, RH da M_±=0. No se deduce una tasa inferior para todo T ni se acota desde arriba el mínimo sobre TODO el espacio. En particular Q4 de fase 159 no queda resuelto para ese mínimo.

**Cotejo.** 083 controla por separado las diagonales. La fase 159 G2_B5_R4/R5 ya conecta tasas de negatividad de ventanas con franjas de ceros; 038 y 074 ya usan detección unilateral de polos. Aquí el cruce explícito permite obtener la tasa en ambas direcciones sobre cada una de dos familias prefijadas y pagar el caso crítico del acoplamiento amortiguado con las diagonales. No hay una nueva franja libre de ceros. Cualquier extensión de 084 a orientaciones opuestas con coeficientes libres, incluso con sólo dos términos en todas las ventanas grandes, tendría que resolver el signo global.
