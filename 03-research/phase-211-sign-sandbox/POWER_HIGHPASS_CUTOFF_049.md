# POWER_HIGHPASS_CUTOFF_049 — Corte efectivo J=32 para E2 sobre Q^j V12

Estado: BORRADOR SUPERADO por POWER_CENTERED_CUTOFF_049 (corte14) y POWER_R12_TRANSPORT_049 (segmento1..13 y transporte uniforme). No registrar este corte32 como resultado adicional. Papers intactos.

## Antecedentes y diferencia

Consultados índice ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D, buscando Jacobi, momentos inversos y highpass; revisados JOINT_SCALE016, GEOMETRIC_TRANSFER015 y R12_ENDPOINT048. Las coordenadas Beta/Jacobi y la positividad eventual ya estaban probadas. La diferencia es una cota inversa uniforme explícita, con corte J=32 para todos los numeradores de V12, en lugar de un límite sin índice efectivo.

Fijar u=63/2, Q(s)=s/(s+u), q=|Q(iτ)|²=τ²/(u²+τ²). Para F∈V12 no nulo y j≥32 se demuestra

    ∫τ^−2 |Q^jF|² / ∫|Q^jF|² ≤ 2/u²=8/3969<1/400.    (INV)

Las integrales espectrales llevan el mismo factor1/(2π), que cancela.

## Lemma polinómico ponderado, con prueba

Sea w(q)=q^α(1−q)^β, α>0, β>−1, y p un polinomio real o complejo de grado≤m. Escriba R=∫[(1−q)/q]|p|²w/∫|p|²w. Entonces

    αR ≤ β+1+2sqrt(m(m+α+β+1)R).                       (JAC)

Primero, la energía satisface ∫q(1−q)|p′|²w≤m(m+α+β+1)∫|p|²w. Prueba elemental: el operador

    Lp=−w^−1 (q(1−q)wp′)′

preserva los polinomios de grado≤r y tiene coeficiente principal r(r+α+β+1) sobre q^r. La integración por partes lo hace simétrico (el flujo q^(α+1)(1−q)^(β+1) se anula en ambos extremos). Aplicando Gram–Schmidt a1,q,...,q^m, cada polinomio ortogonal es autovector: su imagen menos el coeficiente principal por sí mismo tiene menor grado y es ortogonal a todos esos grados. La energía es por tanto la suma de cuadrados de coordenadas por estos autovalores crecientes. Esto prueba la cota sin importar un teorema espectral externo.

Por otra integración por partes, ahora de q^α(1−q)^(β+1)|p|², cuyos extremos también se anulan,

    αR = β+1 − 2 Re∫(1−q)p′ conjugate(p)w / ∫|p|²w.

Cauchy, con factores q(1−q)|p′|² y (1−q)|p|²/q, da JAC.

## Aplicación simultánea a todos los numeradores

La base Laguerre048 convierte F en E_0(iτ)P(z), degP≤11, z=(iτ−u)/(iτ+u) en el círculo. La medida |E_0|²dτ/(2π) es uniforme en el círculo; q=(2+z+z̄)/4. Separar P(e^{iθ})=A(cosθ)+sinθ B(cosθ), permitiendo coeficientes complejos. Al integrar cualquier peso dependiente sólo de cosθ, el término cruzado es impar y se anula. Así basta aplicar JAC a dos sectores no negativos:

- par: α=j−1/2, β=−1/2, m=11;
- impar: α=j+1/2, β=1/2, m=10.

El factor sin²θ=4q(1−q) explica exactamente el cambio de peso del segundo sector. Los grados menores se incluyen rellenando coeficientes nulos.

Para el sector par, en R=2 se tiene

    (2j−3/2)² > 88(j+11),    j≥32.

Para el impar,

    (2j−1/2)² > 80(j+12),    j≥32.

Ambos lados izquierdos son positivos. Las diferencias en j=32 son respectivamente489/4 y2049/4; sus derivadas son positivas desde32. La función αR−(β+1)−2sqrt(λR) tiene una sola raíz positiva, por ser cuadrática en sqrt(R). Las desigualdades anteriores sitúan esa raíz debajo de2, y JAC implica R<2. Las mezclas de los dos sectores conservan esa cota. Finalmente τ^−2=u^−2(1−q)/q, demostrando INV.

## Dominación de la forma parcial E2 y obligación finita restante

Usar la cota elemental del símbolo de017,

    m(τ) ≥ log|τ|−log(2π)−1/|τ|−1/(2τ²).

Jensen aplicada a log(τ^−2), y Cauchy, dan para la probabilidad espectral normalizada

    ARCH ≥ −(1/2)log Eτ^−2−log(2π)−sqrt(Eτ^−2)−Eτ^−2/2
         > log(10/π)−41/800 > 11/10.

La última desigualdad sigue de π<22/7 y log(35/11)>921/800, que se comprueba mediante una suma positiva de atanh con argumento12/23. El contacto2 tiene valor absoluto menor que sqrt(2)log2<1 veces la norma.

Para el polar,048 prueba |Polar[Q^jF]|/||Q^jF||²≤(9/62)^j PB12. Aquí PB12<3: cada banda polar satisface

    |p_k| ≤ (63/992)[(32/31)^11+1] < 1/5, 0≤k≤11.

En efecto (1+1/31)^12≤1/(1−12/31)=31/19<2, por comparación de coeficientes binomiales con la serie geométrica. La suma de fila es menor que12/5<3. Por tanto3(9/62)^j<1/1000 para j≥32. Se concluye

    E2[Q^jF] > (99/1000)||Q^jF||²,  j≥32, F∈V12\{0}. (TAIL)

Este es un corte efectivo uniforme, no sólo eventualidad. GEOMETRIC_TRANSFER015 reduce ahora el transporte R12 a comprobar E2−c norma² sobre Q^jV12 para j=1,...,31, con c=1/2500. El índice1 está certificado048. No se ha probado aquí el signo de los otros treinta bloques; TAIL no lo implica. No se declara R12 uniforme ni se ha efectuado un barrido de tasas u órdenes.
