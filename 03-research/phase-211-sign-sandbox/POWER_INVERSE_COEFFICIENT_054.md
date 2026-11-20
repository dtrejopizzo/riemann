# POWER_INVERSE_COEFFICIENT_054 — Condicionamiento efectivo en frecuencia inversa

Estado: PROVED lema de coeficientes/evaluación compleja, revisión independiente aprobada en POWER_INVERSE_COEFFICIENT_AUDIT_054.md. El paso posterior de contorno y corte se desarrolla en POWER_EFFECTIVE_HIGHPASS_054.md; este memo conserva separada su prueba inicial. Papers intactos.

## 1. Antecedentes y diferencia explícita

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; revisados HIGHPASS015, JOINT_SCALE016, INTERIOR017/WRN, QUADRATIC_EXPLICIT017§6 y los cortes de momentos049/053.015 ya demuestra eventual positividad uniforme a dimensión fija mediante un límite de Gram y Riemann–Lebesgue; no se repite esa eventualidad como resultado nuevo.016 refuta normas temporales exponenciales uniformes en dimensión y017 controla sólo numeradores monomiales.

El objeto cambiado es el polinomio de FRECUENCIA INVERSA reescalada. Su norma admite una cota elemental en un intervalo fijo que da una constante explícita dependiente sólo de la dimensión, para TODOS los numeradores y TODOS j≥n. No se invierte una Gram monomial dependiente de j ni se supone una constante ponderada independiente de n. Es una desigualdad efectiva de coeficientes, no todavía el signo de W.

## 2. Cambio exacto y norma

Fijar u>0, n≥1, entero j≥n, Q(s)=s/(s+u), y F0(s)=P(s)/(s+u)^n con gradoP<n. Poner

    a=u sqrt(j),
    R(y)=y^(n−1)P(ia/y),
    w_(n,j)(y)=(1+y²/j)^−(n+j),
    D_(n,j)[R]=∫_R |R(y)|² w_(n,j)(y)dy.

R es un polinomio complejo de grado≤n−1; las potencias de y eliminan exactamente los denominadores. Para cada j el cambio de coeficientes es invertible. El lema siguiente cubre TODOS los R, aunque el R asociado a un P fijo dependa de j.

Con la convención de Fourier y Plancherel del corpus, el cambio τ=a/y, sobre ambas semirrectas, da

    ||Q^jF0||²=a^(1−2n)D_(n,j)[R]/(2π).                (NORM)

En efecto |P(iτ)|²=|τ/a|^(2n−2)|R(a/τ)|², y

    τ^(2j)|P(iτ)|²/(u²+τ²)^(n+j)dτ
      =a^(1−2n)|R(y)|²(1+y²/j)^−(n+j)dy,

con la orientación tratada por el valor absoluto del jacobiano. No falta un factor2: D integra toda la recta.

## 3. Desigualdad uniforme y efectiva

Escribir R(y)=Σ_(r=0)^(n−1)c_r y^r y fijar

    C_n=9n²9^n.

Entonces, para TODOS los polinomios complejos R y TODOS j≥n,

    (Σ|c_r|)² ≤ C_n D_(n,j)[R].                         (COEFF)

Prueba. En |y|≤1, log(1+y²/j)≤y²/j y (n+j)/j≤2. Así w≥exp(−2), y

    ∫_(-1)^1|R|²≤exp(2)D_(n,j)[R].

Sean L_k los polinomios de Legendre normalizados por L_0=1,L_1=y. Su recurrencia

    (k+1)L_(k+1)=(2k+1)yL_k−kL_(k−1)

implica por inducción ||coef(L_k)||_1≤3^k: el paso se domina por2·3^k+3^(k−1)≤3^(k+1). La ortogonalidad elemental ∫_(-1)^1L_kL_l=2δ_kl/(2k+1) puede obtenerse directamente de Rodrigues e integración por partes, incluidos los bordes anulados por(1−y²)^k.

Expandir R=Σb_kL_k. Cauchy da

    Σ|c_r| ≤ Σ|b_k|3^k
       ≤ (∫_(-1)^1|R|²)^(1/2)
           [Σ_(k=0)^(n−1)(2k+1)9^k/2]^(1/2).

La suma está acotada por n²9^(n−1), por comparar cada uno de sus n términos con(2n−1)9^(n−1)/2. Finalmente exp(2)<9, y por tanto ya basta n²9^nD en COEFF; la constante declarada C_n, más amplia por un factor9, es válida también en n=1. Esto prueba la desigualdad sin un límite ni un eigenvalor no cuantificado.

## 4. Evaluación compleja y producto real de la densidad

Para cualquier z complejo,

    |R(z)|² ≤ C_nD_(n,j)[R]·max(1,|z|^(2n−2)),
    |R(z)R(−z)| ≤ C_nD_(n,j)[R]·max(1,|z|^(2n−2)).     (EVAL)

Ambas siguen de |R(z)|≤(Σ|c_r|)max(1,|z|^(n−1)); los argumentos z y−z tienen el mismo módulo.

Para P REAL, la densidad analítica completa del átomo filtrado es

    ρ(z)=z^(2j)P(iz)P(−iz)/(u²+z²)^(n+j)
        =(−1)^(n−1)a^(−2n+2)
          z^(2(j+n−1))R(a/z)R(−a/z)/(u²+z²)^(n+j).   (DENSITY)

El factor(−1)^(n−1) es esencial en esta identidad. En y real,

    R(y)R(−y)=(−1)^(n−1)|R(y)|²,

así que DENSITY coincide con la densidad espectral no negativa sobre la recta. EVAL permite tomar el módulo sobre un contorno complejo conservando el producto completo, sin sustituirlo por dos normas temporales crecientes en n.

## 5. Paso de contorno separado del lema probado

EVAL es un condicionamiento explícito y uniforme. Por sí sola no paga la integral desplazada: el factor max(1,|a/z|^(2n−2)) y el denominador racional deben integrarse, conservando los momentos de la misma norma NORM. Tampoco se puede sumar una cota de autocorrelación que decaiga sólo como1/logq: el peine infinito exige una cola summable justificada.

Una continuación concreta a revisar es reemplazar max por Σ_(r=0)^(n−1)|a/z|^(2r). Cada término de DENSITY corresponde a una densidad monomial017 con N'=r+1 y k'=j+n−1−r. Para j≥10000n² todos los términos con N'≥2 quedan en el cono del bound de contorno017. El extremo N'=1 debe justificarse separadamente; no se extiende una condición N'≥2 sin prueba. Luego se requieren cotas explícitas de los momentos ∫y^(2r)w_(n,j)dy antes de concluir un costo de contorno dependiente sólo de n.

Este memo prueba sólo COEFF/EVAL, con una constante efectiva, que elimina la obligación de estimar una Gram mal condicionada dependiente de j. La continuación ya desarrollada se encuentra separadamente en POWER_EFFECTIVE_HIGHPASS_054.md, incluyendo el extremo N'=1 y los momentos de normalización; no se atribuye esa conclusión a COEFF sin esos pasos adicionales.
