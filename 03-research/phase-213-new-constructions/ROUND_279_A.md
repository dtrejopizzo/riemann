# El exponente exacto de la masa absoluta en la banda

Sea Θ=sup_ρ Re ρ para los ceros no triviales de ζ. Para el peso de 275 y la construcción específica de 274, con A(x) de 277, se tiene

    lim_(x→∞) log A(x)/log x = (1+Θ)/2.

También vale con sólo primos. Por tanto RH equivale a A(x)=x^(3/4+o(1)). El resultado determina la precisión absoluta que se pierde al olvidar los signos. Se evita volver a la reducción bilineal de 049, cuyo obstáculo de cancelación sobre dos factores próximos a √x ya está registrado.

**Piso a toda escala.** Para cualquier cero fijo ρ de parte real β>1/2, repetir la identidad exacta de Mellin de 276. En [0,Y] la cola regularizada es O(N^(−2)) también con y^(β−1), agrandando desde el principio la constante C para cubrir uniformemente 1/2≤β≤1 (en y≤Y se pierde a lo sumo un factor 1+√Y respecto a la estimación para β=1/2, absorbible en el exponente de decay). H(ρ)≠0 por 275. Sigue ∫_Y^U |T| ≫_ρ x^β Y^(1−β). La transferencia relativa de 277 da el mismo piso para A y su versión prima. En Θ=1/2 usar el primer cero como en 276. Tomar primero el límite inferior en x y después el supremo de β. No se necesita uniformidad en la ordenada del cero.

**Techo si Θ<1.** Fijar Θ<θ<1. Por el criterio clásico de Mertens en un semiplano libre de ceros, M(v)=O_θ(v^θ) (se deja margen estricto entre Θ y θ). Para S_*(t)=Σ μ(d)w(dt/x), sumación parcial y la suavidad compacta de w dan

    |S_*(t)| + t|S_*'(t)| ≪_θ (x/t)^θ   (0<t≤2x).

Para la derivada usar la misma cota con el peso u w'(u). Por tanto los coeficientes completos b_j de 261 tienen variación Σ|b_j|≪_θ x^θ al integrar la derivada en t≥1. El ajuste entero de 261 tiene ese mismo orden de coste y es exacto en todos los átomos. Por la fórmula explícita para el peso suave, |J−xh|≪_w x^Θ para x grande (la suma absoluta de |H(ρ)| converge uniformemente sobre la franja por decaimiento vertical). Por Stirling, su entropía completa difiere de xh en O_θ(x^θ log N). El primer momento discreto completo ΣS_*(j) es cero por la exactitud en m=1.

Ahora pasar del perfil completo al perfil cortado χ(t/U)S_*(t) de 273. La variación de los dos momentos discretos es, respectivamente, O_θ(x^θ U^(1−θ)) y O_θ(x^θ U^(1−θ)log N), sumando sobre j≤U. Aplicar la inversa de la matriz normalizada de 273, incluido el centrado de su segunda fila, da amplitudes de los dos correctores O_θ((x/U)^θ log²N). Para y en la banda, la inversión completa satisface Σ_l S_*(ly)=w(y/x)=0 en el argumento real. Por tanto

    T(y)=Σ_(l≤U/y)(S(ly)−S_*(ly)).

Aquí hay O(log²N) sumandos y cada argumento es ≥Y. Las estimaciones anteriores dan sup_banda |T|≪_θ (x/U)^θ log⁶(2N). Por Chebyshev la masa Λ de la banda es O(U), de modo que limsup log A/log x≤(1+θ)/2. Hacer θ↓Θ. Si Θ=1 basta |T|≪U log²(2N) en los átomos por la variación total de las filas y |c|≤1. El límite superior es entonces ≤1, coincidiendo con el inferior.

**Consecuencia para el signo.** Aun bajo RH la masa absoluta tiene exponente exactamente 3/4. El equilibrio relativo de 277 y la cota unilateral de raíz de 275 son de precisiones diferentes. El teorema actual ofrece además un criterio alternativo enteramente en términos de magnitudes: bastaría una cota superior de exponente 3/4 para A. Ese techo incondicional permanece abierto.

**Subsucesión suficiente.** Puesto que el piso forzado por cada cero vale para todo x suficientemente grande, basta exhibir cualquier sucesión x_j→∞ con A(x_j)≤x_j^(3/4+o(1)), aun usando solamente la versión prima de A. Un cero con β>1/2 obligaría a exceder ese techo en todos los términos suficientemente grandes de la sucesión. No se exige densidad positiva ni una estimación entre escalas seleccionadas.
