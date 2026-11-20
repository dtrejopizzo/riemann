# Un solo corte móvil y una sola desigualdad para la gaussiana difusiva

En 364 tomar exactamente z=(log x)² y escribir Q_a(x) para esa suma. Poner L=log x y b(x)=√x exp(2L/log L), para x grande. Para cada a>0 fijo, las siguientes condiciones son equivalentes:

* Ningún cero ρ con Re ρ>1/2 satisface Re Φ_a(ρ)>1/2.
* Eventualmente Q_a(x)≤b(x).
* Eventualmente −Q_a(x)≤b(x).

Si la exclusión falla, hay un B fijo de modo que, para cada X suficientemente grande, se rebasan **ambos** umbrales en [X,e^B X]. Por tanto basta una sola de las dos desigualdades, con el único corte prescrito, para cada a de una sucesión positiva tendiente a cero. Ésta es una equivalencia, no una prueba de esa desigualdad para parámetros arbitrariamente pequeños.

**Techo explícito en ausencia de violaciones.** Usar el contorno de 364 con T fijo suficientemente grande y sin ordenadas de ceros en sus horizontales. Mover el borde izquierdo a 1/2+1/L. En esa vertical los factores meromorfos de D_z independientes de z cuestan O_a(L^C) para alguna constante fija: en un compacto sólo hay polos de orden finito, la distancia a los de la recta crítica es ≥1/L y los demás tienen distancia positiva para L grande. El posible polo en 1 se trata con la forma regular E_z[(1/ζ)'−(H+L_z)/ζ] de 361, donde H son las potencias superiores y L_z el polinomio primo. H tiene también un polo simple en 1/2, ya incluido en ese coste. Los factores dependientes del corte, en toda Re s≥1/2, cuestan como máximo un polinomio en L por

    ∏_{p≤L²}(1−p^(−1/2))^(−1) = exp((1+o(1))L/log L)

por sumación parcial y el teorema de los números primos. En el borde izquierdo x^ReΦ≤O_a(√x); en horizontales y colas usar 364. Los polos interiores a la derecha de la recta son fijos y tienen Re Φ≤1/2. En círculos de radio 1/L en torno a ellos, los factores meromorfos cuestan una potencia de L y x^ReΦ cambia por factor acotado. Los residuos admiten así el mismo techo. Sumando, |Q_a(x)|≤b(x) eventualmente.

**Los residuos con el corte realmente móvil.** Si falla la exclusión, escoger el contorno fijo de 364 para que su error tenga exponente estrictamente menor que M, el máximo de Re Φ sobre los polos cruzados, con M>1/2. Para x=X exp(u), L₀=log X y u en cualquier intervalo fijo [0,B], sea ρ uno de estos polos, β=Re ρ>1/2 y m su multiplicidad. En el círculo s=ρ+w/L₀, |w|=1, se tiene uniformemente

    E_z(s)=(1+o(1))E_(L₀²)(ρ).

En efecto, el movimiento del corte añade O_B(L₀) enteros de tamaño comparable a L₀², lo que cuesta O_B(L₀^(1−2β)) en el logaritmo. El movimiento de s cuesta O(L₀^(2−2β)log L₀/L₀)=o(1) usando la derivada del logaritmo del producto (basta sumar sobre enteros). El polinomio de primos simples retirados cuesta O(L₀^(2−2β)log L₀)=o(L₀). Así el término −ζ'/ζ aporta −mL₀/w+O(1) y domina en el corchete de 361. Integrando en ese círculo, el residuo es

    X^Φ_a(ρ) exp(uΦ_a(ρ)) E_(L₀²)(ρ) L₀^m [c_ρ+o(1)],

donde c_ρ=−m Φ_a'(ρ)^m/ζ^(m)(ρ)≠0, por extracción del coeficiente en exp(wΦ_a'(ρ)). Este cálculo controla el error **relativo a cada amplitud**, incluso si unas amplitudes son mucho mayores que otras. La norma máxima de las amplitudes es ≥X^(M−o(1)), pues |E_(L₀²)(ρ)|≥X^(−o(1)).

**Por qué se ven los dos signos.** Las frecuencias complejas λ=Φ_a(ρ) son distintas por 364 y tienen parte imaginaria no nula. Para cada pareja conjugada elegir τ=π/|Im λ|. La medida positiva δ₀+exp(−τ Re λ)δ_τ anula el integral de exp(λu) y su conjugado. Convolucionar todas estas medidas con la medida uniforme en [0,1]. Resulta una medida positiva en [0,B], con densidad positiva en un intervalo, que anula todas las funciones del sistema. Por independencia y analiticidad, toda combinación real no nula cambia de signo allí. Por compacidad de los vectores de coeficientes conjugados con máximo módulo uno, tanto su máximo como el máximo de su negativo son ≥c>0, con c independiente del vector. Aplicar esto al desarrollo anterior tras normalizar por la amplitud máxima. Los errores relativos agregados son o(1) y el del contorno también; aparecen valores de ambos signos de módulo ≥X^(M−o(1)). Superan b(x) en ese bloque.

**Alcance y antecedente.** 142–144 ya emplean gaussianas para detectar oscilaciones y 126 registra criterios unilaterales. El paso adicional aquí es permitir el movimiento efectivo del producto de Euler en cada bloque sin congelar el corte y controlar amplitudes relativas para obtener ambas excursiones. Se conserva el rango a≥1/((3·10¹²)²−1/4) de 364. Sigue pendiente la desigualdad unilateral al acercarse a cero.
