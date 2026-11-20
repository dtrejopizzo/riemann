# Cuánto del coste de los cuadrados admite un certificado por divisibilidad

Sean 0≤λ≤1, S de 092 y U_λ(x)=S(x)+2λS(√x). Una cobertura con pesos a_n≥0 y coste Σa_n log n debe pagar al menos U_λ si Σ_{p|n}a_n≥log(x/p) para cada p≤x y Σ_{p²|n}a_n≥λlog(x/p²) para cada p²≤x (en ambas sumas se recorre n). La afirmación resulta de la factorización de cada n. Para pesos reales sobre n≤x el mínimo es exactamente U_λ: poner a_(p²)=λlog(x/p²) y a_p=log(x/p)−a_(p²), tomando cero para cuadrados fuera de rango. Todos son no negativos.

Sea D=2+γ_E−log(4π). Para λ<1−D/2 el techo eventual U_λ≤x equivale al signo global. Para λ≥1−(D/2)(1−1/392) ese techo es FALSO incondicionalmente, aun restringido a escalas arbitrariamente tardías. La anchura entre los umbrales es D/784, menor que 0.000060. El extremo inferior λ=1−D/2 queda abierto.

En efecto, sin RH el techo implicaría S≤x y contradice 092. Bajo RH, con x=exp(2T),

    (U_λ(x)−x)/√x = −J(T)−2(1−λ)+o(1),

por 092 y PNT. Bajo esta hipótesis J es casi periódica por convergencia absoluta de su serie con frecuencias reales y |J|≤D. Para el sentido contrario existen T arbitrariamente grandes en que J(T) se acerca a J(0), por aproximación simultánea de un número finito de fases al neutro y control uniforme de la cola. En el neutro,

    −J(0)=Σ (|ρ|^(−2)−½|ρ|^(−4)) > D(1−1/392),

ya que Reρ=1/2, |Imρ|>14 y Σ|ρ|⁻²=D. Esto fuerza excesos ≥c_λ√x en una sucesión si λ alcanza o supera el umbral superior. Sin RH los excesos normalizados de S ya son ilimitados por 092 y 088. El valor crítico como supremo bajo RH es exactamente 1−sup_T(−J(T))/2; el contacto en el borde requeriría controlar el resto.

**Aplicación.** Una cobertura que pague todas las exigencias de los cuadrados además de las primas falla necesariamente a escala raíz. La cobertura óptima anterior utiliza los primos mismos y no da una construcción independiente con coste ≤x. Antecedentes: 039 y 092 calculan el sesgo de cuadrados, 091 usa retornos a la identidad y 097 resuelve un máximo coprimo distinto.

Actualización: [103](ROUND_103_A.md) conserva el término de los cubos y resuelve el contacto tanto en λ* bajo RH como en el umbral explícito inferior.
