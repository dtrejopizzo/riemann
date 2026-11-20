# Muestreo cuadrático del numerador: hasta 4096 polos reales sin restricciones adicionales

Para n≤4096, v_j>1/2 cualesquiera con multiplicidad y F(s)=P(s)/∏(s+v_j), grado P<n, la forma completa del dato causal cumple

    W(F) ≥ exp(−330000) ||f||₂².

Aquí f es la inversa de Laplace de F. El margen uniforme es deliberadamente conservador. Se usa la suma exacta sobre ceros de 201, Z2 hasta G=3·10¹² y el conteo Z3. La conclusión abarca numeradores complejos.

**Equivalencia de muestreo en cada banda.** Poner n₀=4096, H=1200000000, t=n₀²/H<0.014. En I=(A,A+H], A≥G, para cualquier polinomio complejo p de grado <n₀, sea ||p|| su norma L²(I,dx). Entonces

    l log A ||p||² ≤ Σ_{γ∈I}|p(γ)|² ≤ h log A ||p||²,
    l=0.14−6t>0.056,  h=0.17+6t<0.254.

La suma cuenta multiplicidades. En la base Legendre ortonormal trasladada al intervalo, la suma de cuadrados de sus valores en cada extremo es t. La norma de derivación es ≤2t: en [−1,1] su norma Hilbert–Schmidt cuadrada es Σ_{k<n₀}(2k+1)k(k+1)/2<n₀⁴ por ∫(P'_k)²=k(k+1), que se obtiene expandiendo la derivada en Legendre de paridad opuesta por ortogonalidad e integración por partes. Reescalar por 2/H. Integrar |p|² por partes en el resto de Z3 cuesta ≤log A por la suma de los dos valores de extremo y la variación de |p|², en total ≤6t log A||p||². El resto de Z3 tiene supremo ≤log A y el derivado del término principal está entre 0.14 log A y 0.17 log A como en 201. Se toman valores laterales derechos para el convenio indicado. Por simetría vale la misma estimación en el semieje negativo usando t' = |γ| como variable.

**Diferencia en norma sobre las ordenadas.** Tomar p(t')=P(±it'). Al desplazar el argumento de P por un número real δ_γ con |δ_γ|≤1/2, Taylor y la desigualdad triangular de ℓ² dan una diferencia de norma ≤√(h log A)(exp(t)−1)||p||. En efecto aplicar la cota superior de muestreo a cada derivada y usar ||p^(k)||≤(2t)^k||p||. No se supone que δ_γ sea constante. Para D(s)=∏(s+v_j), el cociente D(±it')/D(±it'+δ_γ) dista de uno a lo sumo b=(1−1/(2G))^(−n₀)−1<10⁻⁸. La razón entre el máximo y mínimo de |D| en I es ≤exp(n₀H/G). Comparando con el vector no desplazado X_γ=F(iγ), ambas desviaciones X_γ^±−X_γ en ℓ² tienen norma ≤e||X||, con

    e ≤ exp(n₀H/G) √(h/l) [(1+b)(exp(t)−1)+b] < 0.16.

Así la suma real de productos de los dos vectores es ≥(1−2e−e²)||X||²>0.65||X||². Usando la cota inferior de muestreo y la razón del denominador una vez más, esto supera 0.01∫_I |F(±ix)|²dx porque 0.65 l log(G) exp(−2n₀H/G)>0.01. Sumar en las bandas altas y conservar la no negatividad bajo G por Z2.

**Piso global en norma.** Comparar el intervalo bajo [−G,G] con I=[G,G+H] en la variable de ordenadas. En la coordenada de Legendre |x|≤1+4G/H≤10001. Por recurrencia |P_k(x)|≤(2·10001+1)^k para los polinomios de Legendre normalizados en 1. Cauchy–Schwarz en la expansión ortonormal da sup_[−G,G]|P(i·)|≤(n₀/√H)21000^n₀||P(i·)||_{L²(I)}. Además max_I|D|/min_[−G,G]|D|≤(7·10¹²)^n₀ por v_j≥1/2. Por tanto el cociente de la energía baja respecto de la energía alta es a lo sumo C=(2G n₀²/H)(21000·7·10¹²)^(2n₀) con log C<325000. El piso sigue de 0.01/(1+C) y Plancherel con factor 1/(2π).

**Escala del método.** A cualquier orden n, en bandas que comienzan desde max(3·10¹²,100n³), tomar H=80n²; entonces t=1/80 y nH/A≤0.8. Las mismas dos cotas de muestreo y Taylor prueban signo de cada banda alta (n/(2A) es diminuto y H/A≤0.001 para A en este rango: para n pequeño usar A≥3·10¹² y para n≥800 usar A≥100n³). Sólo se deduce signo de toda la forma si también se controla la parte baja hasta esa altura. No se presupone verificación adicional. El avance frente a 201 es el control relativo en norma de muestreo para todos los numeradores y sus derivadas, no una optimización del máximo en un subintervalo. La obstrucción de interpolación de 201 sigue vigente cuando se fija una banda y se deja crecer el orden sin límite.

**Auditoría independiente.** Se verificó el término de discrepancia 6t, la aplicación de Taylor con desplazamientos variables, el factor del denominador, la extrapolación y la normalización de Plancherel. La cota calculada para e es <0.155.
