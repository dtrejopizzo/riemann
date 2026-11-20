# Ley exacta del fondo con una penalización de derivadas que puede tender a cero

Para s>0 fijo añadir a W_T la energía ε_T ∫ |ξ|^(2s)|F̂(ξ)|² dξ/(2π) de la extensión por cero, tomando tests suaves compactos unitarios y el ínfimo (también en el espacio primitivo). Sean M_(W,s,ε) y M_(A,s,ε) las partes negativas de esos ínfimos. Para cualquier 0<ε_T≤1 tal que log(1+log(1/ε_T))=o(T),

    lim log(1+M_(W,s,ε)(T))/(2T) = lim log(1+M_(A,s,ε)(T))/(2T) = Δ.

No se impone condición de densidad local adicional a los ceros. Se admite por ejemplo ε_T=exp(−exp(√T)). La no negatividad eventual de cualquiera de estas formas penalizadas equivale al signo global de la forma original, pues RH da positividad y Δ>0 da crecimiento de ambas partes negativas.

**Techo.** El conteo clásico por intervalo unitario da D₂(y)≪log(2+|y|). La parte de tira y multiplicación de 117 para κ=1, antes de imponer el presupuesto arquimediano, da para cualquier test unitario −W_T(F)≤B_T ∫log(2+|ξ|)|F̂|² dξ/(2π), B_T=C(1+T)^6 exp(2ΔT), C≥1. Al restar la penalización, basta maximizar en r≥0 la función B_T log(2+r)−ε_T r^(2s). Para r≥1 usar log(2+r)≤log 3+log r y maximizar en r^(2s) explícitamente; para r≤1 basta log 3. Resulta a lo sumo C_s B_T[1+log(B_T/ε_T)]. Su exponente superior es Δ por la hipótesis de ε_T.

**Piso.** Para cada η<Δ elegir exponente intermedio η'<Δ mayor que η. Los testigos primitivos de 115 se construyen sumando dos traslaciones de un mismo perfil suave Pg fijado para η'. Su norma L² es fija cuando los soportes son disjuntos, y su seminorma homogénea H^s es a lo sumo dos veces la del perfil por invariancia por traslación. El coste adicional tras normalización es O_(s,g)(1), independientemente de T. En cada ventana grande se conserva la profundidad ≥exp(2ηT) para η≥0. La forma completa incluye los mismos testigos. Cuando Δ=0, RH da que las partes negativas son cero.

**Condición necesaria para una tasa mayor en la forma original.** Por Jensen, en cualquier test unitario de seminorma cuadrática H_s finita, ∫log(2+|ξ|)|F̂|² dξ/(2π)≤C_s[1+log(1+H_s)]. Si −W_T(F)≥exp(2(Δ+η)T) con η>0, necesariamente log(1+H_s)≳_s exp(2ηT)/(1+T)^6 en esa sucesión. La regularidad local en T de 077 para s<1/2 no proporciona una cota de este tamaño al crecer T. El teorema cierra la tasa del problema penalizado; retirar ε_T a T fijo por densidad no autoriza intercambiar ese límite con T→∞ ni da la cota superior sin penalización.
