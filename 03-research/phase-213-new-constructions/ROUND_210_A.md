# Un promedio cuadrático primo sin parámetro libre mide el desplazamiento relativo máximo

Para el peso y el corte explícitos de 208–209, sea A_N(u)=Σ_{p≤M₁(u)^(2N)}(log p)c_N(log p;u)/√p. Para enteros N≥4 formar el único número no negativo

    E_N=∫₃ᴺ |A_N(u)|² du/u⁴.

Cada E_N usa sólo primos hasta M₁(3)^(2N), pues M₁(u) decrece. Se prueba el límite ordinario

    lim E_N^(1/(2N)) = R_* = 1 + sup_ρ (Re ρ−1/2)²/(Im ρ)².

Si se cumple RH, además E_N→0. Si falla, E_N crece exponencialmente para TODO N suficientemente grande, aunque el exponente puede ser arbitrariamente pequeño según la ubicación del cero. Así bastaría probar que E_N está acotada en una sucesión de enteros no acotada. No se establece esa cota aritmética.

**Control global del error de 209.** Para u≥3 y N≥2 se tiene |b_N(u)+2A_N(u)|≪u log(2u), con constante absoluta, aunque sólo se usa el o(1) de 209 en tasas fijas o en compactos. Por escala H_u(τ)=H₁(τ/u), 0≤H_u≤1 en la recta, el arquimediano cuesta O(u log(2u)), y el polar O(1). En la recta trasladada, ∫|H_u(τ+i)|dτ≪u porque en la variable τ/u la altura es ≤1/3 y el integrando tiene un mayorante integrable independiente de esa altura. El costo de truncar la suma completa de 208 es entonces O(u) por Chebyshev, uniformemente en la tasa y en el corte X_N≥1. Las potencias ≥3 cuestan O(u) por ||c_N||∞≪u. Para los cuadrados, 209 prueba para el perfil de escala unidad ||c_N(·;1)||₁+||c'_N(·;1)||₁≪1 por estimaciones sobre la recta real que no utilizan el contorno a i. Al reescalar, esas normas son O(1) y O(u), respectivamente. Integrar por partes en la suma infinita sobre cuadrados usando θ(x)≪x y el extremo O(u), como en 209, da O(1+u). Su cola de truncación ya se controla por la cota absoluta. Esto prueba la desigualdad uniforme.

**Máximo por cero y techo global.** Con z=δ+iγ, h_u(z)=−4u²z²/(u²−z²)². Maximizando el módulo sobre a=u², la derivada tiene el signo de |z|⁴−a²; el máximo se da en u=|z|>3. Allí h es real POSITIVO e igual a |z|²/γ². Además Σ_ρ |h_u(z)|≪u log(2u). En efecto, |u²−z²|≥u²+γ²−1/4 y |γ|>14; en |γ|≤u cada término es O(1) y en |γ|>u es O(u²/γ²). El conteo Z3 y la suma diádica concluyen. Por ello |b_N|≤C u log(2u) R_*^(N−1). La cota de error anterior y la integrabilidad de log²(2u)/u² controlan el limsup de la raíz por R_*. Bajo RH, 209 y el mismo argumento espectral a cualquier altura dan A_N(u)→0 salvo en el conjunto numerable de ordenadas; convergencia dominada con el indicador de [3,N] prueba E_N→0.

**Piso bajo RH.** En torno a la primera ordenada γ₁, para x fijo en [−1,1] tomar u=γ₁ exp(x/√N). El perfil demostrado en 209 da A_N(u)→−m(γ₁)exp(−x²). Cambiar variables en ese intervalo y aplicar Fatou a las funciones no negativas muestra liminf √N E_N>0. Esta cota inferior local vale también sin RH por Z2. En particular el límite inferior de la raíz es al menos uno.

**Piso si hay un cero fuera de la línea.** En ese caso R_*>1 es alcanzado, porque |δ|≤1/2 y |γ|→∞ en la cola. Fijar un maximizador y u₀=|z|. Los únicos términos que alcanzan R_* en u₀ son los del mismo cuarteto, con sus multiplicidades: se requiere tanto |z|=u₀ como el mismo |δ|/|γ|, que juntos fijan |δ| y |γ|. Todos tienen valor positivo en u₀. Los demás tienen módulo ≤R_*−η con alguna η>0 en una vecindad fija, por decaimiento uniforme en altura y finitud del resto. En |u−u₀|≤c/N, con c>0 suficientemente pequeño e independiente de N, cada término dominante tiene argumento después de elevar a N de módulo ≤π/4 y módulo ≥R_*^N exp(−C c), por derivadas acotadas del logaritmo local. Los restantes contribuyen en suma absoluta O((R_*−η)^(N−1)) por el techo de primer momento. Así b_N≥c'R_*^N en todo ese intervalo para N grande. El error aditivo local es O(1), de modo que E_N≥c''R_*^(2N)/N, y se obtiene el límite afirmado.

**Diferencia de alcance.** 207–208 relacionaban un limsup a tasa fija con intervalos de detección y luego tomaban un supremo en u. Aquí se usa el hecho de que el máximo individual en la tasa es real positivo, evitando cancelaciones para todos los N en un intervalo de longitud comparable a 1/N. Esto da una sola sucesión aritmética finita y un límite ordinario para el desplazamiento RELATIVO. Los argumentos no acotan E_N subexponencialmente sobre los primos verdaderos a escalas ilimitadas.

Con la altura verificada G se obtiene de inmediato 1≤R_*≤1+1/(4G²)=1+1/(3.6·10²⁵). Esa cota procede directamente de Z2 y de la franja crítica y no establece R_*=1. La revisión independiente comprobó la optimización por cero, el aislamiento del cuarteto y el error global con peso integrable.
