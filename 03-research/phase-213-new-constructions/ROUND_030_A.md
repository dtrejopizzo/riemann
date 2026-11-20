# Un perfil de meseta fijo detectaría anchos arbitrariamente grandes

La conclusión refuerza el orden de cuantificadores de 029. El nuevo paso combina 028 con la identidad escalar central de P47 prop:boundary. Para cada F real, par, primitivo, suave, compacto, de masa uno, basta demostrar la desigualdad de la recta de 029 para todos los D suficientemente grandes **dependiendo de F**. Incluso basta demostrar liminf_{D→∞}(recta−Φ)≥0 para cada F. Ambas condiciones son necesarias y suficientes para el signo global.

**Valor central.** Sea C_F^×(D)=a(F,V_DF) para F real suave primitivo cualquiera, y L_F(z) su transformada unilateral, inicialmente para Re z>1/2. Por 028 continúa a lo largo del eje real hasta un entorno del origen. Mostramos L_F(0)=0 para el peine verdadero. La contribución arquimediana a C_F^× es la transformada inversa de m|F̂|², real par e integrable en D por la estimación de núcleo separado de 028. Por inversión de Fourier su integral en la semirrecta vale m(0)M²/2, M=∫F.

Para la parte del peine poner l=log n y c=c_F par. La integral unilateral de c(l−D)+c(l+D), ponderada con exp(−zD), vale

    exp(−zl)P(z) + ∫_{l}^∞ c(v)[exp(−z(v−l))−exp(z(v−l))]dv,
    P(z)=∫ c(v)exp(zv)dv.

El segundo término es entero y desaparece para l mayor que el diámetro de soporte de F. Además vale cero en z=0 incluso en los contactos bajos. Con el signo y el coeficiente de 028, la contribución del peine a L_F(0) es pues −S(1/2)M², donde S es la continuación real de ΣΛ(n)n^(−s) construida en 028. P47 prop:boundary en su valor central da 2S(1/2)=m(0). Es una identidad escalar: para Z=η/(1−2^(1−s)), η(1/2)>0 por los pares de 028; la simetría s↦1−s de π^(−s/2)Γ(s/2)Z(s) da derivada cero en 1/2 y, por derivación logarítmica en ese punto, la igualdad indicada. No se requiere información sobre puntos no reales.

**Residuo.** Sea E_F(D)=a(1_[−D/2,D/2]*F). La identidad del núcleo triangular en 027 da transformada 2L_F(z)/z² en Re z>1/2. Continúa localmente a lo largo del eje real positivo y tiene a lo sumo un polo simple en 0, con residuo r(F)=2L'_F(0). Para F=F₀+εK con soporte en un compacto fijo y ambos perfiles primitivos, r(F) es un polinomio cuadrático en ε real. Esto se sigue por polarización: las identidades cuadráticas de las transformadas en la zona de convergencia persisten por continuación y extracción de residuos.

Si falla el signo, tomar G impar suave compacto primitivo con q=a(G)<0 como en 028, y F₀=G'. Entonces E_{F₀}(D)=2q−2C_G^×(D), de modo que su transformada es 2q/z−2L_G(z). Por tanto r(F₀)=2q<0. Para un K par primitivo suave de masa no nula construido en 029, elegir **una sola vez** ε≠0 suficientemente pequeño. El perfil F₀+εK conserva r<0. Normalizar su masa a uno multiplica el residuo por un factor positivo. F queda fijo en el resto de la prueba.

**Paso del residuo a valores reales de energía.** Vale liminf_{D→∞}E_F(D)≤r(F). En efecto, si eventualmente E_F≥h con h>r(F), la cola de E_F−h es no negativa. Su transformada tiene continuación local sobre el eje positivo y residuo r(F)−h<0 en 0; retirar un intervalo compacto sólo resta una función entera. Por el argumento de Taylor con coeficientes positivos de 028, su integral de Laplace converge en cada z real positivo: una abscisa de convergencia estrictamente positiva contradiría la regularidad allí. Vale entonces lo que da la continuación por unicidad. El producto de esa integral por z es no negativo para z>0 y su límite en 0 sería negativo. Esto prueba la desigualdad de liminf sin identificar en general la integral con su continuación en 0 ni reclamar un límite ordinario en D.

Para el F fijo anterior, S_D(F) de 029 tiende a cero. Así liminf(recta−Φ)=liminf E_F≤r(F)<0 y hay violaciones con margen fijo a anchos arbitrariamente grandes para el mismo perfil. En sentido directo, el signo global da recta−Φ=E_F+S_D(F)≥0 para cada D mayor que el diámetro. La prueba también muestra que r(F)≥0 para todo perfil par primitivo de masa uno es un criterio equivalente: en sentido directo usar liminf E_F≤r(F) y E_F≥0; la construcción anterior da la recíproca. La no negatividad de esos residuos sigue abierta. PROVED tras auditoría matemática independiente.

**Distinción del peso alterado.** Al sustituir Λ por cΛ con c constante, el valor central de la transformada del cruce pasa a (1−c)m(0)M²/2. Para M≠0 y c≠1 aparece en la transformada de la energía un término (1−c)m(0)M²/z². Para el control c=1.1 su coeficiente es positivo. El residuo simple deja entonces de decidir la contradicción usada aquí. Esto identifica una dependencia exacta de la normalización aritmética; no excluye otras modificaciones de pesos que compartan el mismo valor central.

## Control negativo con cualquier número finito de derivadas centrales exactas

Para cada entero fijo m≥0 existen pesos no negativos que difieren de Λ en un conjunto finito de potencias primas, coinciden con su serie continuada S y todas sus primeras m derivadas en 1/2, y dan energía estrictamente negativa al test certificado de BUILD084 (16)–(17). La modificación depende de m. P47/P48 thm:finmod son antecedentes directos; aquí una modificación que iguala exactamente derivadas centrales debe compensar los cambios bajos antes de concluir. No se impone una ley de Euler adicional que ate entre sí los pesos de todas las potencias de un primo.

Primero sumar 0.1Λ(n) para 2≤n≤257; esto reproduce todos los contactos del test de BUILD084 y su energía negativa probada para 1.1Λ. Para j=1,...,m+1 tomar sólo primos p en [exp(jR),exp(jR+1)], con R grande. Sea B_j=Σ_p (log p)/√p en el bloque j. Por PNT para primos, B_j→∞. Para k=0,...,m sea V_kj la media de (log p/R)^k en el bloque con pesos (log p)/(√p B_j). Como j≤log p/R≤j+1/R, V converge a la matriz de Vandermonde (j^k), invertible. Resolver exactamente en los reales

    Σ_j V_kj u_j = − Σ_{2≤n≤257} 0.1Λ(n)n^(−1/2)(log n/R)^k.

El segundo miembro es acotado con m fijo, así u_j=O_m(1). En el bloque j sumar a cada peso (u_j/B_j)log p. Todas las modificaciones relativas remotas tienden a cero y los pesos siguen siendo no negativos. Ningún contacto remoto entra en el soporte del test. Por construcción, la diferencia de series es un polinomio de Dirichlet con derivadas de orden 0,...,m exactamente nulas en 1/2; basta multiplicar la ecuación k por (−R)^k. Queda probado el control sobre el test de la forma original con pesos modificados.

En particular la cancelación central de 030 se conserva, mientras el signo falla para estos pesos. La identidad distingue el control 1.1Λ uniforme, pero aun todos los datos centrales hasta un orden finito prefijado son compatibles con una dirección negativa. Esto no decide el signo de r(F) para Λ; tampoco se construye una modificación única que conserve derivadas de todos los órdenes. PROVED tras auditoría matemática independiente.

## Identificación del residuo con el núcleo de D.52

Usamos g con el signo de (2.1) de 114_d_52_CONTINUOUS_SCREW_KERNEL_PRIMITIVE_BRIDGE, coincidente con (1.3) de Suzuki en la copia local de 2606.09096v3. Para el perfil real primitivo F de 030, c=c_F y M=∫F, se obtiene

    r(F)=2∫_ℝ c(v)g(v)dv + [ (1/2)Σ_{k≥0}(k+1/4)⁻² −16−2S'(1/2) ] M².

Para verificarlo, derivar en cero el término entero de cada contacto bajo de 030. Como P es par, la parte aritmética de r es

    −2M² S'(1/2) + 4 Σ_n Λ(n)/√n ∫_{log n}^∞ (v−log n)c(v)dv.

Por soporte la suma es finita. Es exactamente la contribución de las rampas de D.52 al emparejamiento 2∫cg, más el término central escrito. Para el lado arquimediano, la expansión de m en P47, thm:S(i), usa a=k+1/4 desde k=0. La cuenta del cajón de 027 aplicada a ese símbolo da término constante

    −m(0)∫|v|c(v)dv + (1/2)Σ_{k≥0}a⁻²∫ exp(−2a|v|)c(v)dv

en la energía arquimediana para D grande, después de quitar m(0)M²D; el resto decae exponencialmente. Esta constante es 2L'_arch(0) por la identidad triangular de Laplace. En 2∫cg los mismos términos se acompañan de −(M²/2)Σa⁻² por la constante de Hurwitz–Lerch en (2.1). El término polar de g aporta 16M² pues ∫exp(±v/2)c(v)dv=0 y ∫c=M². Esto fija el ajuste completo, incluso para masa no nula. Todas las series anteriores de términos constantes convergen absolutamente.

El antecedente D.52 (3.6) ya identifica la forma sobre antiderivadas en el sector de masa cero. La fórmula identifica en qué sentido 030 prolonga ese mismo objeto a masa no nula. Reexaminar el signo del emparejamiento bajo el nombre de residuo repetiría el problema de núcleo ya registrado en D.134 sin una desigualdad adicional.
