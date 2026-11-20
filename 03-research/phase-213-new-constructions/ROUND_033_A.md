# Límite del defecto normalizado en las matrices completas de celdas

Cotejo: 212-75 y 031 dan recuperación de perfiles; P47 lem:compact usa una ventana logarítmica fija. Aquí la ventana logarítmica crece, pero la norma de saltos proporciona compactidad tras escalar el extremo físico derecho a uno. El error uniforme de 032 permite quitar después el corte aritmético. No se afirma una tasa en el tamaño discreto.

Sea H=N+1 y β_N el defecto definido en 031. Existe el límite finito Γ=lim β_N/N. Para L fijo, sea X la completación de C_c^∞(0,1) en I(u)^(1/2), I(u)=∫₀¹ x|u'(x)|²dx; X₀ impone ∫u=0. Con h_L el símbolo polar corregido de 032, definir B_L(u)=∫h_L(t)|widehat(Uu)(t)|² dt/(2π), extendiendo u por cero fuera de (0,1). Entonces

    Γ_L = sup {−B_L(u): u∈X₀, I(u)≤1},   |Γ−Γ_L|≤C/(√(1+log L)).

En particular el signo equivale a Γ=0 por 031. Sobre X₀ la fórmula de B_L es la de Fourier; no requiere interpretar el momento inverso de u, que puede divergir.

**Espacio y reparación.** Para funciones suaves |u(x)|²≤I(u)log(1/x) por integración desde 1. Por ello X se inyecta en L² (la identificación de la derivada se verifica en cada compacto interior). Además ||(Uu)'||²=∫|u/2+xu'|²dx≤C I(u). Ambas cotas pasan por completación. Para L fijo, h_L es continuo, acotado inferiormente y O_L(1+log(2+|t|)), de modo que B_L es continua en X. El momento ordinario es continuo. Los perfiles suaves de momento ordinario cero son densos en X₀: reparar cualquier aproximación con un bump fijo de integral uno.

También se pueden imponer los dos momentos en esa aproximación. Para un perfil suave fijo con momento ordinario cero y momento inverso m, elegir η suave en (−2,−1) de integral uno, y v_R(x)=R⁻¹η(log(x)/R). Su momento inverso vale uno, I(v_R)=R⁻³∫|η'|² y su momento ordinario t_R tiende a cero. Con un corrector fijo k de momento ordinario uno e inverso cero (usar dos bumps separados), v_R−t_R k mantiene momento inverso uno y tiene momento ordinario cero. Restar m veces esta función cuesta o(1) en X para el perfil fijado. Aplicar esta reparación después de cada aproximación, eligiendo R según su m, da densidad primitiva en X₀.

**Corte L fijo.** Sea Γ_{N,L} el supremo de −a_L en los tests primitivos de N celdas con HJ≤1, incluido el cero. Escalar cada test al intervalo (0,1) por u(x)=√H f(Hx); esto es una traslación para U, así que su energía híbrida es B_L(u). Los escalones aún no pertenecen necesariamente a X. Interpolar linealmente sus valores u_j=√H f(j) en j/H para j=0,...,H, con u_0=u_H=0. El interpolante v satisface

    I(v)=Σ_{j=1}^H (j−1/2)|u_j−u_{j−1}|² ≤ HJ,
    ||v−u||²= (1/(3H))Σ_{j=1}^H |u_j−u_{j−1}|² ≤1/(3H).

Cada v pertenece a X por aproximación H¹₀(0,1). Su bola unitaria es relativamente compacta en L²: en [δ,1] usar la cota H¹ y en (0,δ) integrar log(1/x). Extraer para interpolantes casi óptimos convergencia débil en X y fuerte en L² a un límite u_* de X₀ con I≤1. El momento ordinario pasa desde los escalones. Por unitariedad también convergen fuertemente los transformados de los escalones en L². Restar una cota inferior constante de h_L y aplicar semicontinuidad de su integral no negativa da B_L(u_*)≤liminf B_L(u). Así limsup Γ_{N,L}≤Γ_L, incluyendo u_*=0.

Para la otra dirección, usar densidad de perfiles primitivos suaves y continuidad de B_L en X. Muestrear cada uno en la malla 1/H y reparar ambos momentos como en 031: en el soporte compacto interior la convergencia en norma de forma y HJ→I son las de las sumas de Riemann de 031 con K=H y b=1. El soporte interior deja libre la celda inicial. Escalar las amplitudes si HJ>1 cuesta un factor que tiende a uno cuando I≤1. Luego Γ_{N,L}→Γ_L.

**Retirada del corte.** Por 032, |β_N/H−Γ_{N,L}|≤C/√(1+log L) uniformemente en N. La sucesión β_N/H es acotada por 032; sus límites superior e inferior difieren a lo sumo en 2C/√(1+log L) para cada L. Esto prueba convergencia, H/N→1 y la cota anunciada. La compacidad no determina el valor del límite. PROVED tras auditoría matemática independiente.

## Error de una aproximación finita al óptimo continuo

Para L fijo se puede encerrar Γ_L por ambos lados con una matriz finita. Galerkin es conocido en P47 y 212-83; la estimación aquí usa la geometría degenerada de X, con malla más fina junto al origen. Para M≥2, tomar nodos y_j=(j/M)², j=1,...,M−1, y el espacio V generado por

    k_y(x)=−log(max(x,y)),    k_*(x)=1−x.

Estas funciones pertenecen a X: son constantes o acotadas cerca de cero y se pueden cortar allí mediante una transición lineal en log x de longitud creciente con coste I tendente a cero; cerca de 1 tienen traza cero. Suavizar después en el interior. En el producto de energía, k_y representa evaluación en y, por integración de −u' desde y hasta 1. La función k_* representa ∫u por partes. Las identidades pasan del núcleo suave a X. Así la proyección ortogonal P en V conserva los valores nodales y la media ordinaria. Es contractiva en I.

Sea Γ_{L,M} el supremo que define Γ_L restringido a V∩X₀. Vale

    0 ≤ Γ_L−Γ_{L,M} ≤ 6 c_L/M,    c_L=10+2 Σ_{n≤L}Λ(n)/√n +4√L.

En efecto |h_L(t)|≤c_L√(1+t²) por 032 y P47 lem:mbounds (m creciente en |t|, m(0)>−6 y la cota superior de mbounds para |t|≥1). Para e=u−Pu en cada intervalo (a,b) de la malla, e(b)=0 incluyendo b=1. Por Cauchy–Schwarz, ∫_a^b |e|²≤I_interval(e)∫_a^b log(b/x)dx. La primera celda tiene integral 1/M²; en las demás log(b/x)≤(b−x)/a da integral ≤(b−a)²/(2a)≤9/(2M²). Por tanto ||e||₂≤3√I(e)/(√2 M). Por partes en el núcleo suave y por continuidad, ||(Uu)'||²=∫x²|u'|²dx−||u||²/4. Así ||Uu||_{H¹}≤√(7/4)√I(u). En la diferencia de formas, aplicar el multiplicador h_L a Uu y a U(Pu) en los dos cruces contra Ue. Plancherel, las dos contracciones y 3√(7/2)<6 dan la cota sobre toda la bola unitaria. El orden de los supremos da el lado inferior.

Para montar la matriz, con s=1/2+it y la convención de Fourier de P47, las transformadas de Uk_y y Uk_* son (1−y^s)/s² y 1/[s(s+1)], por integración directa. El Gram de energía tiene entradas k_y(z), 1−y y 1/2 para nodos, cruces con k_* y diagonal de k_*, respectivamente. Se impone el momento por ortogonalidad a k_* y se incluye el valor cero al maximizar. Las entradas de B_L son las integrales reales o hermitianas de los productos de esas transformadas contra h_L dt/(2π). Con 032 se obtiene una cota adicional C/√(1+log L) para la retirada del corte. No se ha evaluado numéricamente Γ ni fijado una constante numérica para ese segundo error. PROVED tras auditoría matemática independiente.

## Retirada exacta del corte en cada matriz de 033

Sean L≥M² y u∈V∩X₀. En [0,1/M²] se tiene u(x)=A+Dx. Escribiendo m₁(u)=∫₀¹ y u(y)dy, se obtiene

    B∞(u)−B_L(u)=−2 Re(D conj(m₁(u))) [−ζ′(2)/ζ(2)−Σ_{n≤L}Λ(n)/n²−1/L].

Aquí B∞ denota el límite de los híbridos. Para probar la identidad basta restar los símbolos de dos cortes finitos K>L. El contacto físico para t∈(L,K] vale ∫conj(u(y))u(y/t)dy=D conj(m₁(u))/t porque ∫u=0. Así queda la diferencia de la suma de Λ(n)/n² y la integral de dt/t² en (L,K]. Ambas convergen absolutamente al retirar K. La corrección matricial tiene rango a lo sumo dos por polarización.

Hay además una elección densa de vectores para los que la corrección desaparece. Para M=2^j usar sólo los k_y de los nodos, con media cero. Cada combinación es constante junto a cero, luego D=0. La unión de los espacios antes de imponer la media es densa en X porque un vector ortogonal se anula en todos los nodos, densos en (0,1), y es continuo localmente. Para obtener densidad en X₀ corregir la media con k_{1/4}, de integral 3/4 y presente en todas las mallas. La forma límite es continua en X₀ por la cota de diferencias de cortes de 032 transferida primero a perfiles primitivos suaves mediante muestreo de 031 y luego por densidad. En consecuencia basta la semidefinitud de estas matrices con L=M² para todo j. La cota 6c_L/M anterior corresponde al espacio que incluye k_*.

El soporte compacto de tests en coordenada logarítmica ya elimina contactos en P47. Aquí el soporte puede llegar hasta x=0 y la anulación procede del valor constante y la media cero. Esta identidad permite evaluar exactamente la contribución de la cola en cada compresión. La desigualdad simultánea en j queda abierta. PROVED tras auditoría independiente.

## ¿Permite la cola nula aplicar directamente las ventanas primitivas?

La transformación de Hardy v(x)=u(x)−x⁻¹∫₀ˣu convierte cada perfil nodal constante en (0,a) y de media cero en un perfil soportado en [a,1]. Con U(s)=∫₀¹u(x)x^(s−1)dx y V la misma transformada de v, Fubini en 0<Re s<1 da V=sU/(s−1). El multiplicador tiene módulo uno sobre la recta media, por lo que conserva toda la autocorrelación logarítmica.

Sin embargo, hay una obstrucción ya prevista por P47, eq:Kprim y rem:Kprim. Tomar a=1/16, b=1/4, u=(1−b)k_a−(1−a)k_b, de media cero. Su valor inicial es A=(9/8)log 2. Usando la transformada nodal anterior, U′(1)=−(9/32)log 2. Por tanto V(0)=−A, V(1)=U′(1), y el producto es 81(log 2)²/256. Si un perfil compacto primitivo con transformada W tuviera la misma autocorrelación, los productos enteros V(s)conj(V(1−conj(s))) y W(s)conj(W(1−conj(s))) coincidirían en la recta media y por identidad en s=0. Allí el segundo se anula por los momentos primitivos. Esto impide el transporte exacto para ese vector, incluso ensanchando el intervalo. El producto puede anularse en otros vectores.

Cotejo: el factor unimodular ya figura en G2_B10_R5 y fase 104; el argumento de momentos está en P47. Se registra el test explícito para evitar reabrir esa vía como mecanismo de signo. PROVED tras auditoría independiente.

### Distancia a sumas de ventanas primitivas de anchura acotada

Sea K la autocorrelación logarítmica del ejemplo anterior y S cualquier combinación lineal real de partes reales de autocorrelaciones primitivas compactas, con soporte de cada autocorrelación en [−D,D], D≥log 16. También se admite su clausura en L² para D fijo. P47 eq:Kprim da para S los momentos nulos contra g₀(r)=cosh(r/2) y g₁(r)=r sinh(r/2). Es lineal y ambos funcionales son continuos sobre este intervalo. Para K, sean p=81(log 2)²/256 y q=∫g₁K. Son independientes de D: K está soportada en [−log 16,log 16]. El primer valor es el producto de momentos ya calculado, por la transformada bilateral de la autocorrelación.

Proyectando K−S sobre los dos pesos se obtiene

    ||K−S||₂² ≥ p²/G₀₀ + (q−pG₀₁/G₀₀)²/(G₁₁−G₀₁²/G₀₀).

Por integración directa G₀₀=D+sinh D, G₀₁=D cosh D−sinh D y G₁₁=(D²+2)sinh D−2D cosh D−D³/3. Son las entradas del Gram de g₀,g₁. Su determinante es positivo por independencia. Al crecer D, G₀₁/G₀₀=D−1+o(1) y G₁₁−G₀₁²/G₀₀ es asintótico a exp(D)/2. La raíz del lado derecho es por tanto asintótica a √2 p D exp(−D/2).

Esto descarta aproximar K en L² mediante mezclas de ventanas primitivas de anchura acotada, incluso si se permiten coeficientes firmados. Para ventanas crecientes sólo da un coste necesario. La distancia es entre autocorrelaciones y no acota el signo ni el error de una sola energía. Es una consecuencia cuantitativa de los momentos ya registrados en P47. PROVED tras auditoría independiente.

### Identificación de la matriz con la forma completa en su ventana

Sea u una combinación de los k_y sin k_* y de media cero. Denotar por v su transformado de Hardy anterior, por a=M⁻² el primer nodo y por F(r)=exp(r/2)v(exp r) el perfil logarítmico. La siguiente identidad identifica el problema matricial entero, incluidos sus términos polares:

    B∞(u)=W(F),    supp F ⊂ [log a,0].

En cada celda u=α log x+β, de modo que v=α−C/x con una constante C propia de la celda. Es continuo y se anula en ambos extremos del intervalo [a,1]. El mapa es inyectivo por la conservación del módulo de Mellin. El espacio nodal de media cero tiene dimensión M−2, igual al número de nodos interiores de [a,1]. Por tanto v recorre *todo* el espacio continuo afín por tramos en 1/x con esos nodos y valores extremos nulos.

Para verificar la energía, escribir c para la autocorrelación logarítmica común. Los contactos de primos coinciden por la igualdad de c. La diferencia entre los multiplicadores m♯ y m en 032 aporta 2∫₀^∞exp(−r/2) Re c(r)dr, pues la transformada inversa de 1/(1/4+t²) es exp(−|r|/2). La densidad continua integrada hasta el último contacto aporta 2∫₀^∞exp(r/2) Re c(r)dr por el cambio x=exp r y el soporte de c. La suma es 4∫₀^∞cosh(r/2) Re c(r)dr=2 Re(A(F)conj(B(F))), exactamente el término polar de P47. Se puede centrar la ventana mediante traslación, con semiancho T=log M.

Esta identificación permite importar una cota para W sobre la ventana correspondiente. Una cota dada sólo en el sector primitivo requiere una hipótesis adicional sobre el perfil. La identidad también explica la dificultad al crecer M: se está discretizando directamente W en ventanas crecientes. No aporta una desigualdad uniforme nueva. PROVED tras auditoría independiente.

Antecedente exacto de la igualdad energética para perfiles compactos: P47, rem:polarelim-full. La identificación específica de 033 consiste en determinar el espacio completo de elementos finitos que produce el mapa de Hardy. 018 recuperaba W con dos correctores en ventanas ampliadas y 212-75 ya proporcionaba otro portador denso.
