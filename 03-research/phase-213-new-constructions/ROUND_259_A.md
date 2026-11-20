# Restas binomiales para la octava: construcción y coste necesario

Sea g el peso con soporte [1,2] de 257. Para B≥1, sea E(B) el ínfimo del error en L¹(dy) al aproximar g por sumas finitas de acarreos de 258, de cualquier reparto y escala positivos, ahora con coeficientes reales cuya suma de valores absolutos es ≤B. Se obtienen:

* Incondicionalmente c/B≤E(B)≪exp(−c'√log B) para B grande.
* RH equivale a poder obtener E(B)≤B^(−1+o(1)). Si existe un cero ρ con parte real β>1/2, necesariamente E(B)≥c_ρ B^(−(1−β)/β).
* Hay una fórmula explícita de aproximación por acarreos con signo que, antes de discretizar la mezcla, reproduce EXACTAMENTE el peso para todo y≥v, con un parámetro de corte 0<v<1. La fuga queda íntegramente en (0,v).

**Obstrucción para coeficientes firmados.** El Mellin de un acarreo de escala u y reparto λ es u^s ζ(s)[1−λ^s−(1−λ)^s]/s para Re s>0 por 099 y continuación (el acarreo está acotado con soporte superior finito). Por tanto toda suma finita tiene Mellin cero en ρ. Su error e tiene norma suprema ≤B+||g||∞. Para 0<β<1 integrar |e| contra y^(β−1), peso decreciente, cuesta a lo sumo ||e||∞^(1−β)||e||₁^β/β (concentrar la masa en el intervalo inicial a altura máxima). Así |H(ρ)| está acotado por esa cantidad. H de 257 nunca se anula fuera de la línea y H(1/2+iγ₁)≠0 por 14.13<γ₁<14.14 y su fórmula explícita. Esto da ambas cotas inferiores.

**Inversa que no introduce ceros de reparto.** Promediar λ uniformemente en [0,1] a escala uno y llamar U(y) al acarreo resultante. Se obtiene Mellin ζ(s)(s−1)/[s(s+1)], pues ∫λ^s dλ=1/(s+1). La masa de U es 1/2. Definir

    f(u)=−u g'(u)+2g(u)+(2/u)∫_u^∞g(v)dv,
    a(u)=Σ_(n≤2/u) μ(n) f(nu).

En Re s>1 el Mellin de f es H(s)[s+2+2/(s−1)] y el de a es el anterior dividido por ζ(s). El producto con el Mellin de U es H(s), por lo que

    g(y)=∫₀² a(u) U(y/u) du/u.

Fubini aquí se justifica con peso y^(σ−1), σ>1, a partir de la serie absolutamente mayorada de μ. La igualdad por unicidad de Mellin también vale punto a punto: en y>0 sólo interviene u≥y; las discontinuidades del piso se sitúan en un conjunto nulo de u para cada y fijo y la integral es continua por dominación local.

**Control de la construcción.** Para u<1, escribir X=1/u. La parte con n<X es 2hX Σ_(n<X) μ(n)/n, con h=∫g. La parte X≤n≤2X se acota por sumación parcial, ya que f tiene variación acotada en [1,2]. Usar la cota clásica incondicional M(X)≪X exp(−c√log X) para M(X)=Σ_(n≤X)μ(n), y Σμ(n)/n=0. Integrar por partes en la cola de esta última suma (reduciendo c) da |a(u)|≪u^(−1)exp(−c'√log(1/u)). Bajo RH la cota clásica M(X)≪_ε X^(1/2+ε) da |a(u)|≪_ε u^(−1/2−ε).

Cortar la integral en u≥v tiene coste de coeficientes B_v=∫_v²|a(u)|du/u y error L¹ a lo sumo (1/2)∫₀^v|a(u)|du, por la masa de U a escala u. La cola es exactamente cero en y≥v salvo posibles extremos de integración de medida nula. La mezcla truncada se aproxima, con error L¹ arbitrariamente pequeño y sin aumentar B_v, por sumas finitas: el acarreo depende continuamente en L¹ de ambos parámetros en el compacto [v,2]×[0,1], por convergencia dominada fuera de los saltos; separar partes positivas y negativas de la medida. Con v=B^(−1/2) la cota incondicional anterior deja B_v≤B para B grande y da el techo anunciado. Bajo RH el coste es O_ε(v^(−1/2−ε)) y el error O_ε(v^(1/2−ε)); eliminando v y dejando ε arbitrario se obtiene el exponente −1+o(1). La obstrucción en los ceros da la recíproca.

**Identidad aritmética adicional.** En escala física x, con v=2/x y x>2, la mezcla continua truncada reproduce todos los términos en potencias primas m≥2. Con L(t)=log(⌊t⌋!)−(2/t)∫₀ᵗlog(⌊r⌋!)dr se obtiene exactamente Σ_m Λ(m)g(m/x)=∫_(2/x)^2 a(u)L(xu)du/u por la factorización de los factoriales. Las cotas L¹ para aproximar por sumas finitas son cotas continuas y por sí solas no autorizan a discretizar esa identidad en los átomos. La vía sigue necesitando un control de cancelación: la estimación de Mertens a escala de raíz usada para alcanzar el exponente óptimo ya depende de RH.

**Cotejo.** 099 ya identifica el multiplicador de Mellin para repartos promediados; 129–134 ya usan inversión de Möbius en identidades factoriales. Lo adicional es la tasa de aproximación para el peso diádico positivo concreto, con coste en variación total de coeficientes, obstrucción cuantitativa en cada cero y una construcción que alcanza el exponente crítico bajo RH. 258 excluía la mayoración positiva de coste casi exacto, incluso con repartos variables.
