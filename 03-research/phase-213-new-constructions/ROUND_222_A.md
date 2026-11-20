# Una escala de estabilidad para la muestra prima

Sean dos sistemas de pesos sobre los primos y D(x) la diferencia de sus sumas acumuladas de pesos logarítmicos. Por ejemplo, para los pesos relativos λ_p y μ_p, D(x)=Σ_(p≤x)(λ_p−μ_p)log p. Formar ΔC_k con la diferencia de pesos en 217. Si para algún A≥0 se cumple

    limsup_(x→∞) log(1+|D(x)|/√x)/(log x)^(2/3) ≤ A,

entonces

    limsup_(k→∞) log(1+|ΔC_k|)/k ≤ 4 A^(3/2)/(9√3).

En particular el error de conteo √x exp(o((log x)^(2/3))) preserva las cotas subexponenciales de la muestra tanto globalmente como en cualquier subsucesión. 221 descarta esa conclusión para un error √x · x^o(1) genérico. Aquí se demuestra un techo suficiente con constante explícita; no se afirma optimalidad sobre los primos.

**Traslado de contorno uniforme.** Escribir N=k², L=log x, y fijar U≥3. Para el observable restringido a U≤u≤N y 0≤a≤1/2, 208 y el contorno de Fourier dan

    |c_N(L;u)|+|∂_L c_N(L;u)| ≤ C (u+u²) exp(N m_U(a)−aL),
    m_U(a)=log M_a(U)=a²/U²+O_U(a⁴).

En efecto se extrae el supremo de |H_u|^(N−2) sobre la recta trasladada; la integral restante de (1+|τ+ia|)|H_u(τ+ia)|² es O(u+u²) por escala y a/u≤1/6. M_a≥1 decrece en u. El corte superior L_X=2N log M₁(u) es O(N), uniformemente en u.

Para ΔA_N(u) integrar por partes x^(−1/2)c_N(log x;u) contra dD(x) desde 1 hasta X inclusive. La aportación del borde en X y la integral en L quedan dominadas por un polinomio en N multiplicado por el supremo, para 0≤L≤C N, de

    exp((A+η)L^(2/3) + inf_(0≤a≤1/2)[N m_U(a)−aL]).

Se permite una constante dependiente de η>0 que cubre los x acotados. La elección de a varía con L DESPUÉS de derivar el núcleo: se estima ∂_L c_N en cada contorno y no se deriva la envolvente optimizada. Los factores u+u² se absorben en el polinomio pues u≤N. En u integrar con el módulo de u^(−√k+ik−1), de integral acotada. La misma estimación rige para ΔC_k restringido a U≤u≤N.

**Optimización.** Para ε>0 fijar a₀∈(0,1/2) tan pequeño que m_U(a)≤(1+ε)a²/U² en [0,a₀]. Cuando L≤2(1+ε)a₀N/U², usar a=U²L/(2(1+ε)N). El exponente queda dominado por

    (A+η)L^(2/3) − U²L²/(4(1+ε)N).

El máximo sobre L≥0, por la sustitución z=L^(2/3), es 4√(1+ε)(A+η)^(3/2)√N/(3√3 U). En el tramo restante usar a=a₀: N m_U(a₀)−a₀L≤−a₀L/2 y L tiene orden N o mayor, de modo que la aportación es exponencialmente pequeña en N. Los prefactores polinómicos cuestan o(k) en el logaritmo. Enviar ε,η a cero y tomar U=3. Para A>0, el máximo del mayorante gaussiano está en L de orden k^(3/2). Es una escala del mayorante y no una afirmación de saturación.

**Consecuencias comprobables.** (i) Las dos perturbaciones de 221 que programan respectivamente cero y exp(k) sobre los mismos órdenes deben diferir en su conteo en una cuantía que satisface

    limsup log(1+|D(x)|/√x)/(log x)^(2/3) ≥ (9√3/4)^(2/3).

Si el limsup es infinito la afirmación es automática; si es finito se aplica el teorema. (ii) Si A es finito y para cada U fijo el aporte de la diferencia en [3,U] es subexponencial en la MISMA subsucesión, la diferencia completa es subexponencial allí: el techo del complemento es 4 A^(3/2)/(3√3 U), y se puede enviar U a infinito tras tomar el limsup. (iii) El argumento vale para diferencias de medidas localmente finitas por la misma integración de Stieltjes. Aplicarlo al modelo continuo exige verificar la hipótesis sobre θ(x)−x; con cualquier A finito esa hipótesis ya implica la cota O_ε(x^(1/2+ε)) y cae bajo la obstrucción clásica de 219. El resultado de estabilidad no estima el error auténtico θ(x)−x.
