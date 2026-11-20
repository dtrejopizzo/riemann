# POWER_TATE_CHAIN_009 — Identidad exacta de toda la suma para la cadena Tate

Estado: PROVED identidades y reducción escalar de la familia; OPEN su signo para todos los órdenes. No se afirma una nueva prueba de convexidad. Papers intactos.

## 1. Antecedentes y razón explícita

Leídos las reglas del proyecto, POWER_PRIME_PATTERN_FALSIFIER_008/STATE008 y las entradas del índice: Euler/Möbius/N_018; PROOF_L_SHARP_E/J (colapso Λ*1=log y momentos); A_MU_FACTORIZATION/AUDIT200 (convexidad transversal no automática); LEMMA_F_HALFLINE (contraejemplo a convexidad uniforme). Consultados el grid parte3 (Laguerre/integrales de fluctuación) y el crucigrama según POWER_BRIDGE_002. R5 del inventario abierto registra E_gamma, con criticidad y fracaso de bounds uniformes genéricos.

La diferencia limitada aquí es evaluar una familia uniparamétrica MUY específica, de numerador fijo s²−1/4 y denominadores (s+31.5)^n. No se relanza convexidad de todas las colas ni se atribuye signo a una identidad de Euler. La pregunta pedida permite también una reducción exacta que identifique la estadística firmada restante; eso es lo que se obtiene.

## 2. Tres núcleos gamma, sin expandir un polinomio enorme

Fije u=63/2, a=u²−1/4=992. Para n>=1 defina

    g_n(y)=y^(n−1)e^-uy/(n−1)! ·1_(y>0),
    C_n(t)=c_gn(t),
    ghat_n(tau)=(u−i tau)^-n.

Para n>=3 escriba f_n=(∂²−1/4)g_n; para evitar cualquier regularidad de borde en las formas puede tomarse n>=4, que incluye el caso008. Sus dos momentos polares se anulan y su transformada de Laplace es (s²−1/4)/(s+u)^n.

La identidad de Fourier

    (tau²+1/4)²/(tau²+u²)^n
       =a²/(tau²+u²)^n−2a/(tau²+u²)^(n−1)
                       +1/(tau²+u²)^(n−2)

da exactamente, para todo t real,

    c_fn(t)=a² C_n(t)−2a C_(n−1)(t)+C_(n−2)(t).          (G)

Cada C_j es positiva. La autocorrelación firmada relevante es, sin embargo, una segunda diferencia de TRES núcleos positivos; no tiene signo impuesto por la positividad individual. Esta identidad conserva todas las cancelaciones sin imprimir los n coeficientes Laguerre.

Por integración gamma, para t>=0,

    C_n(t)=e^-ut/Γ(n)² Σ(j=0..n−1) β_nj t^j,
    β_nj=binom(n−1,j)Γ(2n−1−j)/(2u)^(2n−1−j)>0.         (CG)

Todas las series aritméticas siguientes convergen absolutamente: u+1/2=32 y los polinomios son finitos para cada n.

## 3. La suma sobre TODOS los contactos como estadística escalar explícita

Defina

    I_n(u)=(1/2pi)∫_R m(tau)(tau²+u²)^-n d tau,
    J_n(u)=2Σ(m>=2)Lambda(m)m^-1/2 C_n(log m)>0.

La parte arquimediana se calcula sin referencia espectral adicional por

    I_1(u)=[psi((u+1/2)/2)−log pi]/(2u),
    I_n(u)=−[2u(n−1)]^-1 ∂_u I_(n−1)(u).

Si D(s)=Σ(m>=2)Lambda(m)m^-s=−zeta'(s)/zeta(s), s>1, entonces CG da

    J_n(u)=2/Γ(n)² Σ(j=0..n−1)β_nj (−1)^j D^(j)(u+1/2). (J)

Es la suma completa, no un truncamiento ni una expansión asintótica. Los términos de J por separado son positivos, pero la combinación de tres órdenes impuesta por G tiene coeficientes a²,−2a,1.

Los momentos de g_n son (u−1/2)^-n y (u+1/2)^-n. Por tanto

    W[g_n]=I_n−J_n+2a^-n.

Ponga q_n=a^n W[g_n]=a^n(I_n−J_n)+2. Aplicando la linealidad de la distribución de Weil en la autocorrelación a G,

    W[f_n]=a^(2−n)[q_n−2q_(n−1)+q_(n−2)].              (CHAIN)

Las contribuciones polares se cancelan exactamente: 2−4+2=0 tras la normalización. Este es un resultado para toda la familia, independiente de cualquier cómputo de coeficientes grandes.

**Objetivo escalar preciso restante:** demostrar convexidad discreta de la sucesión explícita q_n para todos n>=4. CHAIN no demuestra esa convexidad. La sucesión mezcla la contribución gamma I_n con la estadística aritmética J_n completa.

## 4. Qué hace exactamente Λ*1=log y qué no hace

La identidad de Euler para s>1 es

    D(s) zeta(s)=Σ(m>=1)(log m)m^-s=−zeta'(s).

Diferenciar j veces expresa los números de J como una recurrencia triangular entre sumas positivas. De forma explícita, con H_j(s)=ΣLambda(m)(log m)^j m^-s y Z_j(s)=Σ(log m)^j m^-s,

    Σ(r=0..j)binom(j,r) H_r(s) Z_(j−r)(s)=Z_(j+1)(s).

Despejar H_j requiere RESTAR todos los términos r<j; resolver de una vez introduce los signos de Möbius. Así Euler identifica exactamente los valores aritméticos y permite cálculos, pero no transforma automáticamente la segunda diferencia de CHAIN en una suma positiva. Este punto coincide con los antecedentes Euler/Möbius citados; no se presenta como descubrimiento de una nueva barrera.

Ni la positividad H_j>0, ni la logconvexidad ordinaria de Z_j, ni la positividad de C_n justifican el signo de Δ²q_n: las tres combinaciones firmadas permanecen. No se afirma que sea imposible encontrar una identidad positiva más precisa para este dato; aquí no se la ha construido.

## 5. Relación exacta con el test008 y con E_gamma

El test008 es un múltiplo de f_n con n=2^17. Su obligación TAIL es CHAIN escrita separando los contactos m<=1024 del resto, conservando la misma autocorrelación G. Las fórmulas J/CHAIN suman formal y absolutamente toda esa cola, pero aún dejan su valor y signo en una combinación de derivadas de D en 32.

La densidad espectral normalizada de f_n es proporcional a (tau²+1/4)²/(tau²+u²)^n y se concentra en tau=0 al crecer n; sus momentos beta lo demuestran directamente. Esto la coloca en el régimen de paquetes concentrantes a frecuencia cero relacionado con el residuo E_gamma del inventario. No es un control uniforme de todos los paquetes ni una nueva desigualdad Chebyshev: solo es una familia gamma concreta, con fórmula de todos sus órdenes. Los problemas ya registrados no aportan la convexidad discreta específica de q_n; tampoco su criticidad prueba que dicha convexidad sea falsa.

## 6. Desigualdad finita válida para toda la cadena: ARCH empeora estrictamente

Sea p_n la densidad espectral normalizada de f_n y E_n su esperanza. Entonces

    p_(n+1)(tau)=w(tau)p_n(tau)/E_n w,
    w(tau)=1/(u²+tau²).

Por tanto, para la energía arquimediana normalizada alpha_n=E_n m,

    alpha_(n+1)−alpha_n=Cov_n(m,w)/E_n w<0.              (MON)

El símbolo m es estrictamente creciente en |tau| y w estrictamente decreciente. El signo estricto de la covarianza se prueba integrando [m(x)−m(y)][w(x)−w(y)]/2 contra p_n(x)p_n(y). La densidad no es puntual. Así MON es una desigualdad finita de TODOS los órdenes, no una observación asintótica. Su límite es m(0), por las fórmulas beta y concentración.

Una estimación cuantitativa adicional conserva explícitamente n. Para n>=7, los momentos beta de §008 dan

    E_n tau² ≤u²/n+24u^4/n²+240u^6/n³.

Si n>=64u², el lado derecho es <2u²/n. Usando la cota m(tau)≤m(0)+17tau² ya demostrada en008,

    alpha_n <m(0)+34u²/n,
    c_fn(t)/||f_n||² >1−u²t²/n.

En particular, si n>=64u² y n>=2u²(log R)², cada contacto primo-potencia m<=R perjudica el signo con autocorrelación al menos ||f_n||²/2. Es una versión uniforme y explícita del cálculo008 para cualquier segmento finito. Recupera el mecanismo ya conocido de negatividad de sub-combs; no se presenta como nueva ruta al signo completo. La reparación debe venir de contactos que escapan con n.

No se obtiene una desigualdad de una dirección para la energía COMPLETA: cambiar n multiplica también cada cos(tau log m), función no monótona. El término de covarianza del peine conserva ambos signos. Por eso MON no implica monotonía ni completa monotonía de q_n. La positividad de D y de sus derivadas alternadas tampoco da, por sí sola, esas propiedades de q_n, que incorpora la parte gamma y una combinación firmada de órdenes.

## 7. Por qué el signo de esta familia sola no cerraría todos los tests

Cada miembro individual tiene la expresión temporal

    f_n(y)=y^(n−3)e^-uy/Γ(n)
        ·[(n−1)(n−2)−2u(n−1)y+a y²], y>0.

Tiene como máximo dos cambios de signo. Los múltiplos escalares de miembros individuales no son densos en el conjunto de tests reales: un test que alterna signo con amplitud fija en cuatro intervalos disjuntos no se puede aproximar en L² por funciones con a lo sumo dos cambios. Si los intervalos tienen longitud positiva, todo aproximante deja un error L² uniforme en al menos uno.

Esto no afirma que su ENVOLVENTE lineal sea pequeña; las combinaciones y sus términos cruzados son otro problema. Probar W[f_n]>=0 para cada n solo prueba diagonales de una familia; no prueba W[Σc_n f_n]>=0. El puente de densidad de POWER_BRIDGE_002 requiere positividad de todas esas combinaciones, que no se deduce de convexidad escalar de q_n.

## Resultado y alcance

Se obtuvo una identidad cerrada de tres núcleos gamma y una única sucesión escalar explícita que conservan TODA la suma aritmética y la anulación Tate. No se obtuvo signo de todos los n. El residuo nuevo en su detalle es Δ²[a^n(I_n−J_n)]>=0 para esta cadena fija, no convexidad transversal universal. Cualquier siguiente intento debe aportar una desigualdad para esta combinación firmada; repetir Λ*1=log, positividad de derivadas individuales o convexidad genérica no completa la prueba.
