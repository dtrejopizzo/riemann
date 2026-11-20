# POWER_UNIFORM_STRIP_060 — Contorno uniforme y cono de signo de orden n³ log³n

Estado: PROVED, revisión independiente aprobada en POWER_UNIFORM_STRIP_AUDIT_060.md. Papers intactos.

## 1. Resultados y alcance

Fijar u=63/2. Para n≥1 sea q_n el menor entero q≥1 tal que 2^q≥n+1, y definir

    J(n)=10^12 (n q_n)^3.

Para TODO polinomio real no nulo P de grado<n, TODO entero j≥J(n) y

    F(s)=Q(s)^j P(s)/(s+u)^n, Q(s)=s/(s+u),
    ρ(z)=z^(2j)P(iz)P(−iz)/(u²+z²)^(n+j),

se demuestra

    ∫_R |ρ(x+3i)|dx <2∫_R ρ(x)dx,                      (STRIP3)
    W[F] > ||F||².                                      (CONE)

La constante de STRIP3 es independiente de n y de P. El entero q_n es O(log(n+1)); el umbral es O(n³ log³n). Como q_n≤n, también basta el umbral polinómico más simple j≥10^12 n^6.

No se afirma signo para j<J(n), ni suficiencia de un cono cuadrático para todos los numeradores, ni cierre global. El resultado NECESSITY059 sólo exigía p≥2 para un STRIP uniforme y no contradice este umbral mayor.

## 2. Corpus y diferencia específica

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos HIGHPASS015, JOINT_SCALE016, QUADRATIC/QUADRATIC_EXPLICIT017, INVERSE_COEFFICIENT054 y EFFECTIVE_HIGHPASS054.015 ya ofrece eventualidad a dimensión fija;054 la hace efectiva a dimensión variable pagando una constante D_n muy grande.016 impide uniformizar en n las normas temporales exponenciales separadas; no impide STRIP para la densidad conjunta.

La diferencia nueva es controlar derivadas de una amplitud SIN la fase causal mediante polinomios ortogonales del peso Student exacto. No se utilizan coeficientes monomiales absolutos para el segmento de Taylor. El bound grueso D_n de054 se usa sólo para la COLA de esa serie, con grado de truncación elegido de antemano. Los grados crecen al derivar y se contabilizan explícitamente. No se exponentia una norma de generador restringido a un espacio finito ni se reemplaza globalmente el peso Student por una gaussiana.

## 3. Polinomios ortogonales del peso Student exacto

Sean M=n+j, j≥n+8 y

    w(y)=(1+y²/j)^−M.

El producto escalar es ∫p conjugate(q)w. Todos los momentos necesarios hasta grado n+3 existen, pues M>n+3+1/2. Por Gram–Schmidt sobre1,y,y²,... se obtienen polinomios mónicos p_k, de paridad k.

El operador

    L=−(j+y²)∂²+2(M−1)y∂
      =−w^−1 ∂[(j+y²)w∂]

es simétrico en estos polinomios. Los bordes de integración por partes se anulan por el decaimiento del peso. Preserva el grado y su coeficiente principal es

    λ_k=k(2M−k−1).

La simetría y la ortogonalidad implican Lp_k=λ_k p_k, como en los lemas polinómicos049. Si p_k=y^k+c_k y^(k−2)+..., comparar el coeficiente de grado k−2 da

    c_k=−j k(k−1)/[2(2M−2k+1)].

La recurrencia de tres términos, por ortogonalidad y paridad, es

    y p_k=p_(k+1)+β_k p_(k−1),
    β_k=||p_k||²/||p_(k−1)||²
       =c_k−c_(k+1)
       =j k(2M−k)/[(2M−2k+1)(2M−2k−1)].              (REC)

Para 1≤k≤n+2, j≥n+8 asegura 2M−2k−1≥2j−5≥j y M≤2j. Por tanto

    0<β_k≤4k.

En la base ortonormal, multiplicar por y es la suma de un operador que sube el grado y otro que lo baja, con coeficientes √β. Para cualquier S de grado d≤n+1,

    ||yS||_w≤4√(d+1)||S||_w.                            (MULT)

También, expandir R de grado<n en los eigenpolinomios de L da

    ∫(j+y²)|R′|²w≤λ_(n−1)||R||_w²,
    ||R′||_w²≤3n||R||_w².                              (DER)

No se pierde el factor j de la forma diferencial en este último paso.

## 4. Primera derivada exacta de la amplitud sin fase

Para un polinomio COMPLEJO p de grado<n, definir la función holomorfa en |Imz|<u

    H(z)=z^j p(z)/(u²+z²)^((n+j)/2).

La rama del denominador es la positiva en la recta real; existe en toda la franja porque Re(u²+z²)>0 allí. Poner a=u√j y R(y)=y^(n−1)p(a/y). El cambio τ=a/y sobre ambas semirrectas da

    ||H||_(L²(R))²=a^(1−2n)||R||_w².

Diferenciar y hacer el mismo cambio da exactamente

    ||H′||²=a^(−1−2n)||A_(n,j)R||_w²,
    A_(n,j)R=y²R′+yR−M y³R/(j+y²).                     (GEN)

Esto es la conjugación por el cambio unitario de media densidad: el generador real de traslación es −(y²∂+y)/a. La identidad de normas se verifica en cada semirrecta; los factores constantes de fase o signo allí no afectan la norma.

De MULT aplicado dos veces a R′ y tres veces a R, y de DER,

    ||y²R′||_w≤28(n+2)^(3/2)||R||_w,
    ||yR||_w≤4(n+2)^(3/2)||R||_w,
    ||M y³R/(j+y²)||_w≤128(n+2)^(3/2)||R||_w.

En el último paso M/j≤2. Se obtiene la cota holgada

    ||H′|| ≤ [200(n+2)^(3/2)/(u√j)]||H||,
    j≥n+8.                                             (FIRST)

Es una desigualdad de primera derivada con el peso racional exacto, no una aproximación gaussiana ni una estimación supuesta para la traslación completa.

## 5. Cota gruesa de altura15 para una sola amplitud

Es necesario distinguir una amplitud compleja de la densidad del producto. El bound STRIP054 para un producto genérico NO se identifica sin prueba con ||H(·+15i)||².

Se usa en cambio la evaluación SINGLE de INVERSE_COEFFICIENT054: con H_0=∫|R(y)|²w(y)dy y C_n=9n²9^n,

    |R(Y)|²≤C_n H_0 Σ_(r=0)^(n−1)|Y|^(2r).

Exactamente,

    |H(z)|²=a^(−2n+2)|z|^(2(n+j−1))|R(a/z)|²
                         /|u²+z²|^(n+j).

Para j≥10000n², cada término de SINGLE es una densidad escalar017 de parámetros N′=r+1, k′=j+n−1−r. Su integral sobre Imz=±15 es≤5 veces su integral real. El caso N′=1 fue justificado en EFFECTIVE_HIGHPASS054§3 por WR11 y Cauchy; no se hereda sin prueba de la condición N′≥2.

Los momentos M_r=∫y^(2r)w(y)dy satisfacen ΣM_r≤2n! por054. Las potencias de a se cancelan exactamente como allí. Por tanto, para TODO p complejo de grado<n,

    ||H(·±15i)||²≤D_n||H||²,
    D_n=10C_n n!=10n²9^(n+1)n!.                        (COARSE)

No se separaron las normas temporales causales del problema original. COARSE es una estimación de una amplitud sin fase en frecuencia y se deriva directamente de SINGLE y las diagonales escalares.

## 6. Cauchy en L² y cola de Taylor

Para |η|≤15, escribir N(η)=∫|H(x+iη)|²dx. Diferenciar e integrar por partes produce

    N″(η)=4∫|H′(x+iη)|²dx≥0.

Todos los bordes se anulan por el decaimiento racional; H y sus derivadas son integrables al cuadrado uniformemente en subfranjas cerradas. La convexidad y COARSE en ambos extremos implican N(η)≤D_n N(0), sin exigir coeficientes reales ni simetría de H.

Para ζ complejo con |ζ|≤15, la traslación real de x no cambia la norma; así

    ||H(·+ζ)||≤√D_n||H||.

La aplicación ζ→H(·+ζ) es holomorfa con valores en L² dentro de la franja. Esto puede verificarse directamente con Cauchy puntual y dominación uniforme de la cola |x|→∞. Cauchy y Minkowski dan para cada r≥0

    ||H^(r)||/r!≤√D_n 15^−r||H||.

Por tanto, a altura η=±3, la cola de Taylor desde el índice L cumple

    ||Σ_(r≥L)(iη)^r H^(r)/r!||
      ≤(5/4)√D_n 5^−L||H||.                            (TAYLOR-TAIL)

La convergencia es en L². No se deduce esta cota repitiendo FIRST indefinidamente.

## 7. Segmento finito de Taylor, con grados crecientes controlados

Sea q=q_n y fijar ANTES de estimar

    L=20nq, j≥10^12(nq)^3.

La definición de q da n≤3^q. Usando n!≤n^n, n²≤3^(2q), 10<27 y9^(n+1)=3^(2n+2), se obtiene

    D_n<3^(nq+2q+2n+5)≤3^(10nq).

La última desigualdad vale para todos n,q≥1: su diferencia es9nq−2q−2n−5, mínima en q=1 y allí igual a7(n−1). Así TAYLOR-TAIL es menor que

    (5/4)3^(5nq)5^(−20nq)||H||
      <(5/4)3^(−15nq)||H|| <||H||/100.                 (TAIL-SMALL)

Las primeras derivadas también se controlan sin una dimensión fija ficticia. Si H pertenece a la clase(n,j),

    H′(z)=z^(j−1)[j u²p+z(u²+z²)p′−n z²p]
                         /(u²+z²)^((n+j+2)/2).

El numerador entre corchetes tiene grado≤n+1<n+3. Por tanto H′ pertenece a la clase(n+3,j−1). Tras r derivadas se usa la clase(n+3r,j−r), nunca la original.

Para 0≤r<L, se cumplen j−r≥j/2 y j−r≥n+3r+8. También n+3r+2≤63nq. FIRST en cada paso da un cociente de normas menor que

    200(63nq)^(3/2)√2/(u√j)<1/100.

Por ejemplo √63<8, √2<2 y√j≥10^6(nq)^(3/2) reducen la comparación a201600/31500000<1/100. Se obtiene ||H^(r)||≤100^−r||H|| para r≤L. Luego el segmento de Taylor a altura±3 tiene norma menor o igual que

    Σ_(r=0)^(L−1)(3/100)^r/r! ·||H||
       ≤exp(3/100)||H||≤(100/97)||H||.

Sumar TAIL-SMALL produce

    ||H(·±3i)|| <(100/97+1/100)||H||
                    <(11/10)||H||.                     (AMP3)

Éste es el punto que recupera las cancelaciones del polinomio en norma. La constante grande D_n sólo pagó la cola Taylor, cuyo inicio L crece como n logn; no multiplicó el segmento que determina AMP3.

## 8. Densidad completa y STRIP uniforme

Para el numerador real P del problema, tome p(z)=P(iz) en la definición de H. Sea H#(z)=overline(H(overline z)). Entonces EXACTAMENTE

    ρ(z)=H(z)H#(z).

En la recta, ρ(x)=|H(x)|². En la recta desplazada no se confunde el producto con un cuadrado: Cauchy da

    ∫|ρ(x+3i)|dx
      ≤||H(·+3i)||·||H(·−3i)||
      <(121/100)||H||²<2∫ρ(x)dx.

Esto prueba STRIP3 para todos los numeradores simultáneamente. El mismo argumento incluso permite coeficientes complejos con el producto sesquilineal correspondiente; CONE se enuncia sólo para la clase real requerida.

## 9. Forma completa: ARCH, peine infinito y polar

Desplazar el contorno de la densidad racional, analítica en |Imz|<u, y usar STRIP3 implica

    |c_F(t)|≤2exp(−3|t|)||F||².

Para t<0 se usa la franja inferior. Los bordes verticales tienden a cero por el decaimiento al menos cuadrático de ρ. Por tanto TODO el peine satisface, con Λ(m)≤m,

    |Comb[F]|/||F||²
      ≤4Σ_(m≥2)Λ(m)m^(−7/2)
      ≤4Σ_(m≥2)m^(−5/2)
      ≤7/(3√2)<2.                                       (COMB)

La última suma se limita por su primer término más la integral desde2; no se suma un símbolo infinito de cosenos ni se omiten contactos.

MULT aplicado a R en frecuencia inversa da ∫y²|R|²w≤16n∫|R|²w. Así

    E_F[τ^−2]≤16n/(u²j)≤1/(10000u²),

pues el umbral actual implica j≥160000n. Jensen, Cauchy y el bound del símbolo de017 dan

    ARCH[F]/||F||²
      ≥−(1/2)log Eτ^−2−log(2π)−√(Eτ^−2)−Eτ^−2/2
      ≥log(100u/(2π))−1>4.                              (ARCH)

En efecto π<4, 100u/8>243=3^5>exp5 y la penalización inversa es<1.

El bound POLAR de EFFECTIVE_HIGHPASS054§7 se probó ya para TODOS j≥10000n², sin utilizar su enorme umbral de signo. Por tanto se aplica aquí y da

    |Polar[F]|<||F||².                                  (POLAR)

Combinar ARCH, COMB y POLAR en la MISMA norma demuestra W[F]>(4−2−1)||F||²=||F||², probando CONE.

## 10. Alcance

Se sustituye el corte enorme054 por un cono explícito de crecimiento n³ log³n, válido para TODOS los numeradores de dimensión n. La cota de contorno es uniforme y se obtuvo manteniendo la amplitud sin fase y el producto exacto de la densidad; no se elude016 suponiendo una norma causal ponderada uniforme.

El interior j<J(n) sigue sin decidirse. No se deriva positividad global por las recurrencias016/036, no se afirma un cono uniforme cuadrático para todo P y no se amplía una ventana temporal T del Paper47. No hubo campañas numéricas ni selección de parámetros por autovalores flotantes. Papers intactos.
