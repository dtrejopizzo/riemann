# El baricentro queda del lado positivo hasta 10^20

Con Z1–Z3 de P47, C(x)>0 para todo real 3≤x≤10^20. Además C(x)>0.035√x para 10^7≤x≤10^20. El extremo superior es un límite de esta estimación del baricentro y no un radio de soporte de la forma de Weil.

**Separación exacta.** Sea k(v)=(1−v)(3v−1) para 0≤v≤1 y cero para v>1. Poner J_d(y)=ΣΛ(n)k((n/y)^d). Entonces C(x)=J_1(x)−J_2(√x)−R(x), donde R contiene sólo potencias de exponente impar ≥3, con peso log p. En efecto J_2 elimina exactamente una vez todo exponente par. Como k≤1/3,

    R(x)/√x ≤ (2/3)[x^(−1/6)+x^(−3/10)+(log x)/(2 log 2) x^(−5/14)].

Se usó θ(y)≤2y: por inducción θ(n)≤θ(ceil(n/2))+n log 2 mediante el binomio central, suficiente para n≥4, con bases inmediatas. Tras los exponentes 3 y 5 hay a lo sumo log x/(2 log 2) términos. El techo anterior decrece para x≥10^7.

**Fórmula con constantes.** Para d=1,2 y y≥3000 escribir K_d(s)=−1/s+4/(s+d)−3/(s+2d)=2d(s−d)/(s(s+d)(s+2d)). Se tiene

    |J_d(y)−yK_d(1)+Σ_ρ K_d(ρ)y^ρ| < 50.

En efecto integrar la fórmula explícita simétrica de ψ contra −(d/du)k((u/y)^d) en 1<u<y; los valores puntuales de ψ en saltos no afectan. El intercambio puede realizarse con la primitiva de la fórmula explícita, de serie absolutamente convergente en compactos, e integración por partes. Al integrar los términos u y u^ρ/ρ desde cero salen los dos términos mostrados, por integración por partes y k(1)=0. El recorte en [0,1] del principal cuesta ≤20/y. En el término de ceros el recorte suma en módulo a lo sumo Σ_(l=d,2d) |a_l| l y^(−l) Σ_ρ 1/(|ρ||ρ+l|), con a_d=4, a_(2d)=−3. La suma interior es <0.048 por las estimaciones siguientes. La constante −log(2π) de ψ cuesta ≤7 log(2π), por variación del polinomio en [0,1]. El término −log(1−u^(−2))/2 cuesta ≤(10/y)·2 log 2, por la cota de derivada 20/y y la integral desde 1 a infinito. En particular estos presupuestos caben en 50.

**Ceros.** Hasta G=3·10¹² todos están verificados en la línea. Su suma parcial Σ|ρ|^(−2) es <0.047 incluso sin asumir RH por encima de G: en la línea vale 2 Re(1/ρ)=|ρ|^(−2), y todos los demás términos 2 Re(1/ρ) son positivos en la traza de Hadamard 2+γ_E−log(4π). Contamos ambas ordenadas. Desde G, Z3 implica para las ordenadas positivas N(v)≤v log v/(2π) (su error de tamaño ≤log v queda absorbido por el término lineal). Sumación parcial ignorando el extremo negativo da

    Σ_(|γ|>G) |γ|^(−2) ≤4∫_G^∞ N(v)dv/v³ ≤ (2/π)(log G+1)/G < 6.4·10^(−12).

En la línea |K_1(ρ)|≤2/|ρ|² y |K_2(ρ)|≤5/|ρ|² usando |γ|>14. En la cola, |K_1(ρ)|≤2.01/|γ|² y |K_2(ρ)|≤5/|γ|² por la fórmula racional y 0<Re ρ<1. Por tanto un techo para 4/15−C(x)/√x es la suma de

    0.094 + 0.235/x^(1/4) + 6.4·10^(−12)(2.01√x+5) + 100/√x

y el techo de R(x)/√x anterior. Aquí K_1(1)=0 y K_2(1)=−4/15. En [10^7,10^12] evaluar el término creciente en el extremo derecho y los decrecientes en el izquierdo da menos de 0.206. En [10^12,10^20] se obtiene menos de 0.231. Ambos dejan más de 0.035.

**Tramo inicial.** Ejecutar python3 verify_247.py --limit 10000019. El procedimiento de 247 usa sólo cotas enteras de logaritmos para cada extremo y concavidad para el intervalo entre extremos. La ejecución completó 664579 extremos estrictos entre 3 y 10000019. El último primo supera 10^7 y da solapamiento con la fórmula. La barrera para seguir hasta infinito está localizada en el factor √x que multiplica la cola de ceros no verificados.

**Información que daría un contraejemplo aritmético a mayor escala.** Para x≥10^20, si C(x)≤0, existe un cero con G<|γ|≤Y=100√x log x y Re ρ>1/2+log(10^9)/log x. En efecto, si no, en la banda intermedia se puede reemplazar √x por 10^9 en el término 2.01·6.4·10^(−12)√x del presupuesto anterior. En |γ|>Y el reemplazo de G por Y en la sumación parcial cuesta a lo sumo (2.01)(2/π)(log Y+1)/(100 log x)<0.014 en unidades de √x, porque Y≤x/e en este rango. Se conserva el techo global anterior para J_2. Todos los demás términos decrecientes se pueden evaluar ya en 10^12. El coste total es menor que 4/15, contradicción. Este diagnóstico no presupone que se produzca una violación.
