# POWER_STRIP_CUBIC_NECESSITY_064 — Para todos los numeradores, STRIP uniforme exige exponente al menos3

Estado: PROVED/APROBADO, revisión independiente en POWER_STRIP_CUBIC_AUDIT_064.md, incluida la mejora al umbral j≥10^6n. Sólo limitación de un bound absoluto de contorno; no contraejemplo a W ni al signo global. Papers intactos.

## 1. Enunciado cuantitativo y alcance

Fijar u=63/2 y una altura cualquiera0<η<u. Para TODOS los enteros n≥4 y j≥10^6n existe un polinomio REAL no nulo P_(n,j), de grado<n, tal que la densidad completa del test racional causal

    F_(n,j)(s)=s^j P_(n,j)(s)/(s+u)^(n+j),
    ρ_(n,j)(z)=z^(2j)P_(n,j)(iz)P_(n,j)(−iz)/(u²+z²)^(n+j)

satisface

    ∫_R |ρ_(n,j)(x+iη)|dx / ∫_R ρ_(n,j)(x)dx
       ≥1+η²n³/(1152u²j).                              (LOWER)

Por tanto, para ningún C>0 y p<3 puede existir una constante D finita, independiente de n,j y del numerador, que limite ese cociente para TODOS los tests con j≥C n^p. Para verlo basta elegir

    j_n=max{ceil(C n^p),ceil(10^6n)}.

Entonces j_n=o(n³), y LOWER diverge.

La conclusión es sólo una obstrucción a la ESTRATEGIA STRIP absoluta con altura y constante fijas. No afirma W[F]<0, no excluye un cono de signo W de exponente menor y no requiere una afirmación de concentración espectral que no se haya probado. Se construyen los numeradores explícitamente mediante polinomios ortogonales determinados por un peso positivo; no se seleccionan casos por cómputo.

## 2. Antecedentes y diferencia nueva

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos JOINT_SCALE016, QUADRATIC017, STRIP_NECESSITY059 y UNIFORM_STRIP060.059 demuestra, con P=1, que un STRIP uniforme no puede cubrir la escala subcuadrática.060 establece suficiencia para TODOS los numeradores en j≥10^12(nq_n)^3, q_n=ceil(log2(n+1)).

La diferencia actual es que el numerador varía con n,j y utiliza la dirección de mayor grado del peso Student exacto. El generador inverso de traslación tiene una componente cúbica que sale del grado original. Se cuantifica esa componente mediante una proyección ortogonal y se paga el resto racional con una cota explícita. Esto produce la nueva necesidad p≥3, frente a p≥2 para el numerador constante.

No se extrapola el límite gaussiano a colas complejas ni se supone que un pico estrecho implique varianza pequeña. La construcción inicial de paquetes Hermite fue sustituida por esta prueba Student exacta, que basta para el objetivo de contorno. El signo global permanece abierto y las formas y contactos aritméticos no se modifican.

## 3. Peso y recurrencia exactos

Poner M=n+j y

    w(y)=(1+y²/j)^−M.

Sean p_k los polinomios mónicos ortogonales para w, y e_k=p_k/||p_k||_w. El peso es par, de modo que p_k tiene paridad k. Todos los momentos usados hasta grado n+5 existen: M>n+5+1/2 bajo las hipótesis actuales.

La prueba Pearson de060 aplica sin cambios. El operador simétrico

    L=−(j+y²)∂²+2(M−1)y∂

preserva cada grado y tiene eigenvalor λ_k=k(2M−k−1) sobre p_k. Comparar el coeficiente subprincipal en p_k=y^k+c_k y^(k−2)+... da

    c_k=−j k(k−1)/[2(2M−2k+1)].

La recurrencia monic y la ortonormal son, respectivamente,

    yp_k=p_(k+1)+β_k p_(k−1),
    ye_k=√β_(k+1)e_(k+1)+√β_k e_(k−1),
    β_k=j k(2M−k)/[(2M−2k+1)(2M−2k−1)].                (REC)

Estas identidades se deducen de ortogonalidad, paridad y β_k=c_k−c_(k+1); no se presuponen asintóticos de Hermite. Los bordes del operador Pearson se anulan porque el grado máximo está muy por debajo de M−1/2.

Para 1≤k≤n+4, las hipótesis n≥4,j≥10^6n implican

    k≤2n, M≤2j,
    2M−k≥2j,
    2M−2k−1≥2j−9≥j.

Por tanto los denominadores de REC son positivos y

    k/8≤β_k≤4k.                                        (BETA)

El lower usa que su numerador es≥2j²k y el denominador≤(2M)²≤16j². El upper usa numerador≤4j²k y denominador≥j².

## 4. Una componente de grado n+2 que no puede cancelarse

Fijar d=n−1 y tomar

    R=e_d, ||R||_w=1.

El generador exacto de060 es

    A R=y²R′+yR−M y³R/(j+y²).

Reescribirlo sin aproximación:

    A R=y²R′+yR−(M/j)y³R+(M/j)y^5R/(j+y²).              (SPLIT)

Los dos primeros términos tienen grado≤d+1, así que su proyección sobre e_(d+3) es CERO. En y³e_d, el coeficiente de e_(d+3) sólo procede de subir tres veces en REC y vale

    √(β_(d+1)β_(d+2)β_(d+3))
      ≥sqrt(n(n+1)(n+2))/sqrt(8³)>n^(3/2)/24.

Como M/j≥1, ésa es una cota inferior para el módulo de la componente principal en SPLIT antes de pagar su resto.

Para cualquier polinomio S de grado r≤n+3, BETA y la descomposición de multiplicación en sus partes ascendente y descendente dan

    ||yS||_w≤4√(r+1)||S||_w.

Aplicar cinco veces, empezando en grado d, prueba

    ||y^5R||_w≤4^5(n+4)^(5/2).

Además M/j≤2 y j+y²≥j. El resto racional de SPLIT satisface

    ||(M/j)y^5R/(j+y²)||_w
       ≤(2/j)4^5(n+4)^(5/2)
       ≤12288 n^(5/2)/j
       ≤n^(3/2)/48.                                    (REM)

Se usaron n+4≤2n, 2^(5/2)<6 y j≥10^6n≥589824n. Proyectar SPLIT sobre el vector unitario e_(d+3), usar Cauchy para el resto y restar REM da

    ||A R||_w≥n^(3/2)/48.                              (GEN-LOWER)

No se afirma que A preserve el espacio de grado d: precisamente su componente de grado d+3 es el mecanismo del lower.

## 5. Numerador real admisible y amplitud sin fase

Sea a=u√j y definir

    p(z)=(z/a)^d R(a/z),
    P_(n,j)(s)=p(−is).

Como R tiene paridad d, todas las potencias d−r que aparecen en p son PARES y no negativas. Por tanto p es un polinomio real par, no nulo y de grado≤d<n; P_(n,j) también tiene coeficientes reales. No hay numerador complejo inadmisible oculto en esta construcción.

La amplitud sin fase de060 es

    H(z)=z^j p(z)/(u²+z²)^(M/2),

con la rama holomorfa positiva sobre la recta. H es real sobre la recta. El cambio inverso se usa sólo para las normas, tratando las dos semirrectas con sus posibles fases constantes como en060. Se tiene EXACTAMENTE

    ||H||²=a^(1−2n)||R||_w²,
    ||H′||²=a^(−1−2n)||A R||_w².

GEN-LOWER prueba

    ||H′||²/||H||²≥n³/(2304u²j).                       (DER-LOWER)

Además P_(n,j)(iz)=p(z) y P_(n,j)(−iz)=p(−z)=p(z). En consecuencia la densidad del test causal original es

    ρ_(n,j)(z)=H(z)²                                    (DENSITY)

en toda la franja. Esta igualdad usa que p es PAR REAL; no se identifica un producto complejo genérico con un cuadrado.

## 6. Del lower de derivada al contorno absoluto

Para |t|<u, definir N(t)=||H(·+it)||². Como en060, diferenciación e integración por partes dan

    N″(t)=4||H′(·+it)||².

Todas las funciones y sus derivadas decaen en subfranjas cerradas; no hay bordes omitidos. Dado que H es real sobre la recta, N es par y N′(0)=0. La función D(t)=||H′(·+it)||² también es par y convexa, porque

    D″(t)=4||H″(·+it)||²≥0.

Así D(t)≥D(0). Integrar dos veces prueba para 0<η<u

    N(η)≥N(0)+2η²||H′||².

Por DENSITY, ∫|ρ(x+iη)|dx=N(η), mientras ∫ρ(x)dx=N(0). Insertar DER-LOWER da exactamente LOWER.

No se deduce esta desigualdad del signo de W ni de Cauchy–Schwarz en una forma no probada positiva. Es una identidad/convexidad L² ordinaria de una amplitud holomorfa explícita.

## 7. Consecuencia de escala y límite del resultado

Si se pidiera un bound STRIP≤D para TODOS los numeradores y TODOS j≥C n^p con p<3, los tests construidos con j_n=max(ceil(C n^p),ceil(10^6n)) pertenecen a esa clase. Pero j_n=o(n³), así que LOWER tiende a infinito, contradiciendo D finita.

Esto fija exponente necesario al menos3 para este tipo de control ABSOLUTO, mientras060 da suficiencia a orden n³ log³n. No se afirma optimalidad de los factores logarítmicos ni se intenta optimizar constantes.

La obstrucción no prueba W negativa, no descarta mecanismos que conserven cancelación aritmética en vez del módulo de contorno, y no decide el interior escalar suficiente017. La Λ real, el polar y el símbolo permanecen sin cambios. No se ejecutaron campañas numéricas ni cálculos de nuevos casos de signo. Papers intactos.
