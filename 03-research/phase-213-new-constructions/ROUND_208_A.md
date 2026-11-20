# Suma prima centrada y finita que conserva el crecimiento de la diagonal

Fijar u≥3 y poner H(z)=4u²z²/(u²+z²)², c_N(t)=(2π)⁻¹∫ H(τ)^N exp(iτt)dτ. Definir

    M_a(u)=2/(1+√(1−4a²/u²)),   X_N=M_1(u)^(2N),
    P_N(u)=Σ_{2≤n≤X_N} [Λ(n)−1] n^(−1/2)c_N(log n).

Uniformemente en N≥2 para cada u fijo, b_N(u)=−2P_N(u)+O_u(1), con b_N de 207. Por consiguiente el signo global equivale a que, para toda tasa racional u≥3, limsup_N |P_N(u)|^(1/N)≤1. Se puede pedir equivalentemente que P_N(u) sea acotada en N para cada una de esas tasas: bajo RH lo es por 207 y la identidad anterior. No se ha probado esa cancelación prima para toda tasa.

**Qué se descarta con error acotado.** En la recta 0≤H≤1 y la densidad Fourier normalizada del átomo de 207 es H^N. El arquimediano cuesta O_u(1) por integrabilidad de |m|H. El producto polar se obtiene evaluando la densidad racional en τ=i/2 (con factor 2 del polar) y queda acotado por 2|H(i/2)|^N=O_u(1). Queda −2Σ Λ(n)n⁻¹ᐟ²c_N(log n) por la fórmula prima completa. En |Im z|=a≤1, escribiendo q=(Re z)²+a²,

    |H(z)|=4u²q/[(u²+q)²−4u²a²].

El máximo está en q=√(u⁴−4u²a²), admisible para u≥3, y vale M_a(u). El contorno se puede trasladar a Im z=1 para t≥0 sin cruzar polos; los lados se anulan por decaimiento racional. Así |c_N(t)|≤C_u M_1(u)^(N−1)exp(−t), pues |H(·+i)| es integrable. Por Chebyshev y sumación parcial, Σ_{n>X}(Λ(n)+1)n^(−3/2)≪ X^(−1/2) para X≥1. En X=X_N esto deja un error O_u(1), incluso sin holgura en el exponente. Para u grande log X_N/N=2/u²+O(u⁻⁴).

**Centrar la aritmética.** En la recta |c_N|+|c_N'|≤C_u uniformemente para N≥2 por integrabilidad de (1+|τ|)H². Si g(x)=x^(−1/2)c_N(log x), el error entre Σ_{n≥1}g(n) y ∫₁^∞ g(x)dx es ≤∫₁^∞|g'(x)|dx=O_u(1). El integral es ∫₀^∞ exp(t/2)c_N(t)dt. Por paridad y transformación bilateral a i/2 éste vale H(i/2)^N−∫₀^∞ exp(−t/2)c_N(t)dt, también O_u(1). La igualdad bilateral es legítima por el anterior decaimiento en t, para cada N. Omitir n=1 cuesta O_u(1). Por tanto retirar el término 1 de Λ conserva b_N hasta error acotado.

**Qué mide una superación.** Sea R(u) el máximo de 207 y Q(u)=max(1,limsup |P_N(u)|^(1/N)). Por el error aditivo Q=max(1,R). Se recupera exactamente el mayor desplazamiento horizontal, tomando supremos aunque no haya un cero extremo:

    sup_ρ |Re ρ−1/2| = sup_{u≥3} u √(Q(u)−1)/Q(u).

En efecto |h_u(ρ−1/2)|=|H(γ+iδ)|≤M_|δ|(u), y M_a se invierte por a=u√(M_a−1)/M_a, creciente como función de M_a en [1,2). Para cada cero dado elegir u²=2δ²+√(4δ⁴+|ρ−1/2|⁴), que es ≥9 por la primera altura de Z1. En esa tasa q=|ρ−1/2|² coincide con el maximizador anterior y su término alcanza M_|δ|(u). Se obtienen ambas desigualdades, también bajo RH tomando Q=1. La fórmula no permite omitir el máximo con uno: los errores acotados pueden dominar momentos que decaen.

**Alcance frente a lo anterior.** 017 y 044 ya proporcionan los átomos y sus densidades racionales; 207 da la ley espectral de crecimiento. 208 especifica el corte finito a coste aditivo acotado, la sustracción del fondo 1 y el desplazamiento exacto que mide la tasa de crecimiento. El corte de 014 §7 para numeradores arbitrarios se rige por la escala del bloque completo y no usa esta densidad equilibrada. Aquí la suma aún está firmada y su acotación en toda tasa sigue abierta.

En particular P_N(u)=O_u(1) para cada 3≤u≤G−1 por el sector verificado de 207. La revisión independiente comprobó la optimización sobre el contorno y el costo de la cola por Chebyshev.
