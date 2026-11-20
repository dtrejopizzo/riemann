# Kernel Gram por traslación: identidad uniforme y obstrucción de las capas

Estado: **PROVED como identidad y obstrucción de una clase de certificados; deduplicación dirigida independiente confirmada; auditoría literal final root/casos/mapa aprobada.** Prueba matemática revisada por root/casos. Sin cómputos nuevos y sin modificar papers. El resultado NO decide el signo del kernel integral completo ni el de W para la Phi real.

**Auditoría independiente adicional:** fresh_global leyó literalmente §§2.1–2.2,8–8.3 y los addenda y emitió PASS matemático: constantes, dominios de transformada, cotas de cola y alcances de índices. Se corrigió el resumen de reparaciones de cola para distinguir Phi_M (todo M>=1) de Q_M (M suficientemente grande). Esta auditoría no añade positividad real.

## 1. Consulta y objeto que cambia

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README.md y los catálogos03/04, el grid R162_2300_MASTER_GRID.md y CROSSWORD-TO-D.md; cotejados POWER_THETA_SCHUR_DENSITY_075, POWER_RECIPROCAL_PFAFFIANS_083, POWER_GREEN_PAIR_TP2_SCOPE_111 y POWER_REAL_SECOND_PAIR_AND_TP2_112. Búsquedas dirigidas: slices/capas PSD, t+s+2r, Lyapunov, CND/conditionally negative y Gram/doble integral. La revisión independiente dirigida de mapa confirma que no encontró la fórmula literal. El marco Gram/Pólya es clásico; la ausencia en esta búsqueda no se presenta como novedad mundial.

075 conserva una cancelación para obtener una densidad positiva, pero no un Gram de tamaño arbitrario.083 factoriza todos los tamaños y deja una obligación de signo de Pfaffianos.111 muestra que monotonías individuales, incluso monotonía completa paramétrica, no prueban TP2.112 prueba TP2 para la familia REAL, sin afirmar TP de todos los órdenes. La prueba siguiente intenta evitar esa herencia no demostrada mediante un único kernel de dos variables, cuya representación positiva, si existiese, pagaría simultáneamente todos los tamaños.

El CND de C9/ROUND_003_B pertenece a la métrica de exponentes primos; no es el kernel diferencial que aparece aquí. El fallo real del kernel Volterra bruto105 tampoco es la presente obstrucción: cambian el operador, la variable auxiliar y la condición necesaria refutada. No se afirma novedad absoluta del procedimiento de integración ni de los criterios Gram.

**Antecedente público localizado posteriormente (2026-11-06).** Dylan Suvlu, borrador de24septiembre2026, [Theta correlations and a causal range criterion for the Weil form, §3, (18)–(23)](https://dsuvlu.github.io/weil-form-operators/paper/theta-correlations-causal-range.pdf), contiene este mismo kernel normalizado. Cotejo algebraico root/new_structural_sign PASS; no se afirma publicación arbitrada ni auditoría integral del manuscrito. Si Z0=integral_R Phi y p=Phi/Z0, su j(x,y) satisface EXACTAMENTE j=A/Z0²: poner tau=(x+y)/2,delta=(x-y)/2; p(v+delta)p(v-delta) es par en v, lo que permite cambiar el extremo |tau| por tau, y después v=tau+r. Su respuesta logarítmica coincide con M de esta nota. El manuscrito distingue positividad puntual del acoplamiento y positividad de su forma; deja esta última abierta. Es antecedente directo de la representación, no una prueba del signo ni una identificación automática de RES-SOS§17 o del certificado§19.9 con resultados ajenos. La búsqueda dirigida previa no lo había localizado; no debe atribuirse novedad a A ni a este puente por esa ausencia.

## 2. Kernel exacto y convergencia de su transformada

Sea phi una función par positiva y suave. Para esta sección basta una cota gaussiana

    phi(t)<=C exp(-N t^2), N>0,

y decaimiento suficiente de phi' para las derivaciones e integraciones por partes. La Phi real tiene estas cotas, para cada N>0, por sus supercolas; el modelo cuártico de la sección4 también satisface las condiciones con algún N>0. Definir

    Z(u)=integral_R exp(ut)phi(t)dt,
    A(t,s)=integral_0^infinito
               (t+s+2r)phi(t+r)phi(s+r)dr.             (A)

El factor t+s+2r puede cambiar de signo. Su integral es, sin embargo, positiva. Escribir

    tau=(t+s)/2, delta=(t-s)/2,
    P_delta(sigma)=phi(sigma+delta)phi(sigma-delta).

P_delta es par en sigma. Por tanto

    A(t,s)=integral_tau^infinito 2sigma P_delta(sigma)dsigma
          =integral_|tau|^infinito 2sigma P_delta(sigma)dsigma>0.

Esta cancelación es anterior a cualquier estimación absoluta. La segunda expresión y la cota gaussiana dan

    0<A(t,s)<=C^2 exp(-2N delta^2)
                    integral_|tau|^infinito 2sigma exp(-2N sigma^2)dsigma
              =[C^2/(2N)]exp[-N(t^2+s^2)].             (DOM)

En consecuencia, para todos u,v complejos, la doble transformada de A converge absolutamente, y todas sus derivadas en u,v están dominadas uniformemente sobre compactos. No se invierte el orden de una integral condicional.

El operador partial_t+partial_s es partial_tau. El teorema fundamental del cálculo en la primera integral de A prueba

    (partial_t+partial_s)A(t,s)=-(t+s)phi(t)phi(s).

Integrar por partes contra exp(ut+vs), con DOM y las supercolas en los bordes, da

    (u+v) integral_R^2 exp(ut+vs)A(t,s)dt ds
       =Z'(u)Z(v)+Z(u)Z'(v).                          (LT)

No hay factor2 adicional. Para u+v!=0 se puede dividir; en u+v=0 la integral proporciona la continuación removible. Todas las funciones de LT son enteras.

Para u,v>0 y M=Z'/Z resulta

    [M(u)+M(v)]/(u+v)
       =[integral_R^2 exp(ut+vs)A(t,s)dt ds]/[Z(u)Z(v)].

Si A fuese un kernel PSD, esta fórmula produciría el Gram de todos los bloques finitos del kernel de M. Para justificar el uso de exponenciales no compactas, truncarlas primero; DOM permite pasar al límite en cada forma cuadrática finita. Esto es una suficiencia precisa, NO una prueba de PSD de A real.

### 2.1. Recíproca bajo DOM: los exponentes de un intervalo abierto bastan

**PROVED, revisión literal independiente root/casos; cotejo dirigido mapa.** La búsqueda no encontró esta recíproca literal en las fuentes cotejadas. Es una precisión del puente temporal, no una nueva desigualdad de signo. Sea I cualquier intervalo abierto no vacío contenido en (0,infinito). Bajo las hipótesis de§2, A es PSD en toda R si y sólo si el kernel K_M es PSD para todos los conjuntos finitos de nodos en I.

La suficiencia de A ya está probada. Para la recíproca, poner w(t)=exp(-N t²) y H=L²(R,w(t)dt). DOM implica continuidad bilineal de la forma temporal:

    |integral A(t,s)f(t)conjugado(g(s))dt ds|
       <=[C²/(2N)](integral w) ||f||_H ||g||_H.

El span de e^(ut), con u recorriendo I, es denso en H. En efecto, si h es ortogonal a todos ellos, J(z)=integral h(t)w(t)exp(zt)dt es entera por Cauchy–Schwarz y dominación gaussiana, también para sus derivadas en compactos. J se anula en I, luego en todo el plano. En z=i tau es la transformada Fourier de h w, que es integrable por Cauchy–Schwarz. Unicidad Fourier (o convolución gaussiana seguida de aproximación de la identidad) da h w=0 y h=0.

LT y Z(u)>0 muestran que PSD de K_M en I da no negatividad de la forma temporal sobre ese span. Densidad y continuidad la extienden a H. Para nodos temporales t_i y coeficientes c_i arbitrarios, aproximar sum_i c_i delta_(t_i) por bumps suaves compactos de masa c_i. Cada bump pertenece a H; continuidad de A en los compactos permite pasar al límite de sus valores cuadráticos y da sum_ij c_i conjugado(c_j)A(t_i,t_j)>=0. No se requiere que las normas de los bumps permanezcan acotadas.

No se afirma densidad de una escalera discreta de exponentes bajo una mera cota gaussiana. Tampoco basta ningún tamaño fijo de matrices: la hipótesis usa todos los tamaños dentro de I. Para la Phi real, esto identifica exactamente el alcance del objetivo temporal sin demostrarlo. Para el modelo hiperbólico, el Gram de todos los órdenes ya demostrado en POWER_HYPERBOLIC_MODEL_GRAM sí implica ahora PSD de su A completo; ello no se transfiere a la Phi real.

### 2.2. Para la Phi real, positividad temporal local implica global

**PROVED, revisión independiente root/casos; cotejo dirigido mapa.** No se halló esta formulación literal en las fuentes cotejadas; no se atribuye novedad mundial al principio de continuación de kernels analíticos. Esta precisión corrige la cautela anterior de que probar A PSD en la semirrecta positiva dejaría necesariamente una obligación independiente sobre sus bloques cruzados: para la Phi real, la analiticidad permite recuperar esos cruces. La hipótesis sigue siendo PSD en TODOS los tamaños, no positividad de entradas ni de un número fijo de menores.

La serie theta que define Phi converge holomórficamente en |Im z|<pi/4. En cada compacto de ese strip, Re(exp(2z)) tiene una cota inferior positiva multiplicada por exp(2Re z). Por ello, en la integral que define A(t,s), la cola en r está dominada uniformemente en compactos del producto de strips por un polinomio en r,exp(2r) multiplicado por exp(-c exp(2r)), c>0. La serie theta y la integral dan una función A conjuntamente holomorfa en

    |Im t|<pi/4, |Im s|<pi/4.

Suponga ahora que A es PSD sobre algún intervalo real abierto no vacío I. Fijar 0<rho<pi/4, por ejemplo rho=pi/8. Si un conjunto E ya es PSD y contiene un intervalo alrededor de c, las matrices mixtas formadas por puntos arbitrarios de E y derivadas de evaluación de órdenes0,...,m en c son PSD. En efecto, cada derivada se aproxima por diferencias finitas de evaluaciones dentro de ese intervalo; las matrices aproximantes son congruencias de matrices PSD de puntos de E y su límite conserva PSD.

Para cualquier punto nuevo x con |x-c|<rho, reemplazar formalmente su evaluación por

    T_m(x)=sum_(j=0)^m (x-c)^j partial^j delta_c/j!.

Toda matriz conjunta de puntos viejos y estos T_m(x) es PSD por el paso anterior. La serie Taylor doble de A en el bidisco de centro(c,c) converge absolutamente para los puntos nuevos; la serie simple de A(t,y), con y un punto viejo fijo, hace lo mismo para los cruces. Al enviar m a infinito se obtiene exactamente la matriz de A en los puntos viejos y nuevos. Así E unido con(c-rho,c+rho) sigue siendo PSD.

Partiendo de I y eligiendo centros interiores cerca de los extremos, el radio fijo permite extender sucesivamente a intervalos que cubren toda R. Se concluye que, para A real, PSD en CUALQUIER intervalo temporal abierto equivale a PSD global. No es necesario controlar aparte los cruces A(t,-s) una vez demostrada esa hipótesis local de todos los tamaños. La separación por raíces cuadradas discutida posteriormente no prueba tal hipótesis: su resto sigue sin cota firmada.

Esta continuación sólo cambia el alcance del puente; no da una factorización, no prueba ningún menor real nuevo y no amplía T. Combinada con§2.1, identifica las formulaciones locales y globales sin sustituir la obligación de signo.

### 2.3. Restricción de la factorización Hankel traslacional; antecedente clásico

**PROVED como restricción de representación, revisión root/fresh_global.** No se atribuye novedad al mecanismo: [Blower, Integrable operators and the squares of Hankel operators](https://eprints.lancs.ac.uk/id/eprint/615/1/integrablepaper.pdf), Theorem1.2 y(1.15)–(1.16), obtiene factorizaciones bajo hipótesis concretas de ODE y signo. Su§2.5,(2.14), exhibe el mismo obstáculo por el factor x+y para funciones de cilindro parabólico. La presente aplicación permite un espacio de Hilbert auxiliar arbitrario.

El A de§2, con phi positiva, no admite en t,s>0 una representación

    A(t,s)=integral_0^infinito <h(t+r),h(s+r)>_H dr,  (HANKEL)

con h medible e integrales diagonales finitas. En efecto, para delta>0, restar la misma representación trasladada da

    A(t,s)-A(t+delta,s+delta)
       =integral_0^delta <h(t+r),h(s+r)>_H dr,

un kernel PSD. Dividir por delta y usar la derivabilidad del A conocido obliga a que -(partial_t+partial_s)A=(t+s)phi(t)phi(s) sea PSD. En dos puntos distintos t,s su determinante es

    -(t-s)²phi(t)²phi(s)²<0,

contradicción. No se deriva h ni se impone regularidad adicional. El argumento excluye(HANKEL) en las variables originales; no excluye PSD de A, una representación Gram general, otras coordenadas o una transformación adicional. Tampoco contradice una expresión como suma de dos productos de operadores de Hankel. Es una precisión del alcance de una herramienta clásica, no una prueba de signo ni una nueva obstrucción general.

## 3. Descomposición en capas y certificado suficiente

En la segunda integral de A hacer v=sigma^2-tau^2. El jacobiano es dv=2sigma dsigma y se obtiene exactamente

    A(t,s)=integral_0^infinito S_v(t,s)dv,
    S_v(t,s)=phi(sqrt(tau^2+v)+delta)
                   phi(sqrt(tau^2+v)-delta).           (SLICE)

Cada capa es positiva punto a punto y simétrica en t,s. Esas dos propiedades NO implican PSD. Si S_v fuese PSD para todo v>=0, entonces A lo sería: para cualquier número de nodos y coeficientes reales, integrar su forma cuadrática no negativa. Las integrales de las entradas son finitas por DOM. El mismo argumento cubre coeficientes complejos por separación de partes reales e imaginarias.

Se llama **clase de certificados por capas positivas** únicamente a esta condición S_v PSD para TODOS v>=0 y TODOS conjuntos finitos de nodos reales. La sección5 refuta esa condición para la Phi real. No refuta otras representaciones positivas del mismo A.

## 4. Un modelo integrable donde las capas sí son Gram

Tomar phi(t)=exp(-a t^4-b t^2), con a>0 y b real; también se permite a=0,b>0. La expansión exacta de las potencias da

    S_v(t,s)=phi(t)phi(s)
       *exp[-2av^2-2bv-4av(t^2+s^2)]*exp(4avts).     (QUARTIC)

Para v>=0, el último factor es un kernel PSD porque

    exp(4avts)=sum_(n>=0) [(4av)^n/n!] t^n s^n.

En cada conjunto finito de nodos la serie es absolutamente convergente y su forma cuadrática es una suma de cuadrados con coeficientes no negativos. Los otros factores de QUARTIC son un escalar positivo y una congruencia diagonal positiva. Así TODAS las capas son PSD y también A. El argumento no extrapola esta propiedad desde la clase cuártica a la theta real.

### 4.1. El logaritmo condicionalmente positivo exige más que el Gram cuártico

**PROVED para el modelo, no para Phi.** Construcción root, revisión algebraica independiente theta_joint y cotejo dirigido mapa (2026-11-05). No se halló esta aplicación literal en las fuentes cotejadas. El criterio clásico considerado aquí es CPD de log A: para todo conjunto finito y coeficientes reales de suma cero, sum c_i c_j log A(t_i,t_j)>=0. Equivale a PSD del logaritmo anclado B(t,s)=log A(t,s)-log A(t,0)-log A(0,s)+log A(0,0). Si B es PSD, la serie exponencial y el producto de Schur hacen exp(B) PSD; una congruencia diagonal recupera A. Así sería suficiente para todos los órdenes. Normalizar A por su diagonal no cambia CPD del logaritmo. No se está pidiendo CND de las capas de§5.

Esta condición adicional falla incluso para el modelo positivo de§4 con b=0. En efecto,

    A(t,s)=exp[-a(t^4+s^4)] Z(4a(t²-ts+s²)),
    Z(c)=integral_0^infinito exp(-2av²-cv)dv, a>0.

Sea V la variable positiva con densidad proporcional a exp(-2av²). La expansión de log Z alrededor de0 tiene coeficientes (-1)^k kappa_k(V)/k!. Sus momentos, calculados por integrales gaussianas, dan

    kappa_5(V)=(2sqrt(a))^(-5)sqrt(2/pi)
                  *[3-40/pi+96/pi²] < 0.

El signo no requiere aproximación numérica: 3x²-40x+96 decrece en [314159/100000,314160/100000], intervalo que contiene pi, y su valor en el extremo izquierdo es -548368157/10^10. Como el coeficiente de t^5s^5 en (t²-ts+s²)^5 es -51,

    [t^5s^5]log A=(51/120)(4a)^5 kappa_5(V)<0.

Tomar los seis nodos t_j=jh, j=0,...,5, con c_j=(-1)^(5-j)binom(5,j). Su suma es cero y anulan todas las potencias de grado menor que5. Por analiticidad, la forma de log A en estos coeficientes es h^10(5!)²[t^5s^5]log A+o(h^10), negativa para h>0 suficientemente pequeño. Por tanto log A no es CPD aunque A y todas sus capas sean PSD. Esto descarta inferir el criterio logarítmico de esas propiedades generales; NO refuta log A para la Phi real ni la positividad real.

**Diagnóstico real separado, NUMÉRICO, no certificado:** casos evaluó una sola matriz anclada en los nodos {0,1/4,1/2,1,2}, con ancla0, 60 dígitos, diez modos theta y cuadratura normalizada en r de0 a2. Los cuatro autovalores aproximados fueron 0.000708516447944, 0.0271085148761, 0.329726647588 y 2.85506271832. No se encerraron rigurosamente errores de truncación/cuadratura. Este diagnóstico no falsifica la candidata, pero tampoco prueba CPD ni autoriza extrapolar tamaños. No se emprendió una búsqueda de nodos.

Para t,s>0 puede escribirse exactamente, con q=t+s+2r, p=-Phi'/Phi y probabilidad mu proporcional a q Phi(t+r)Phi(s+r)dr,

    partial_t partial_s log A
      = Cov_mu(p(t+r),p(s+r))
        - Cov_mu(1/q,p(t+r)+p(s+r)) - (E_mu[1/q])².

El último término es negativo y mu depende de ambos nodos: la notación de covarianza no constituye un Gram. Sigue faltando una estimación específica que pruebe el criterio para theta. No hay nueva cobertura de signo ni ventana T.

**Segundo diagnóstico real, puntual y NUMÉRICO (2026-11-05):** se examinó únicamente el coeficiente [t^5s^5]log A en el origen, motivado por el falsificador cuártico anterior. Con Phi_i=Phi^(i), los coeficientes exactos son

    a_ij = 1/(i!j!) integral_0^infinito
           [2r Phi_i(r)Phi_j(r)
            +i Phi_(i-1)(r)Phi_j(r)+j Phi_i(r)Phi_(j-1)(r)]dr,

omitiendo los términos de índice negativo. La paridad anula i+j impar; por eso, para extraer t^5s^5 de log(A/A00), basta la expansión log(1+z) hasta z^5 en el álgebra truncada i,j<=5. Casos calculó las doce integrales simétricas independientes con grado total par, derivadas analíticas hasta5, diez modos theta, 70 dígitos y paneles fijos en r de0 a2. Resultado aproximado: A00=0.01006067751793984255436 y [t^5s^5]log A=+1.90430357842542673366828848575517. La derivada mixta correspondiente multiplica por (5!)². No hay enclosure de los errores de cola/cuadratura: no es certificado de signo. La cancelación entre los cinco términos de la expansión fue retenida. No se buscaron otros órdenes ni otros bloques. Este test no reproduce el falsificador cuártico en theta y no prueba CPD, ni siquiera todos los menores locales.

**Decisión de alcance:** los dos diagnósticos reales no refutan el criterio, pero no aportan la estimación uniforme faltante. No se justifica iniciar una tabla de órdenes ni extrapolar desde estos valores. La condición real queda OPEN, sin nueva positividad W/T.

**Actualización, 2026-11-06: tests diagonales complejos en las cúspides alternante y par positivos eventualmente (PROVED).** Cálculo global_restart_checked/root; auditoría matemática independiente arithmetic_fresh_candidate PASS y revisión root PASS para ambos mecanismos. El cotejo dirigido de fórmula y locus en índices, grid, crucigrama y fuentes phase209/211 no localizó antecedente literal; se combinan herramientas ya registradas, sin reclamar prioridad. Para z=x+iy, x>=0, 0<y<pi/4, definir

    F=A(z,bar z)=2 integral_x^infinito v|Phi(v+iy)|²dv>0,
    b=|Phi(z)|², L=integral_x^infinito |Phi(v+iy)|²dv,
    J=integral_x^infinito v|Phi'(v+iy)|²dv,
    K=integral_x^infinito v Phi'(v+iy)conjugado(Phi(v+iy))dv,
    D=(F/2)J-|K|²>=0.

La última desigualdad es Cauchy–Schwarz con peso v. Los bordes superexponenciales y la integración por partes dan Re K=-(xb+L)/2, partial_t A=L+2K y partial_t partial_s A=2J-b en(z,bar z). Por tanto, para H=partial_t partial_s log A, definido localmente allí porque F>0,

    F² H(z,bar z)=F(2J-b)-|L+2K|²=4D+L²+2xbL-Fb,
    D=(F/2) min_(a complejo) integral_x^infinito
                                     v|Phi'(v+iy)-a Phi(v+iy)|²dv.

La segunda identidad es la proyección ortogonal sobre la recta COMPLEJA generada por Phi en L²(v dv); su mínimo es J-|K|²/(F/2).

**Cúspide alternante, x=0.** Poner epsilon=cos(2y), h=log(2)/2. Las cotas theta COMPLETAS SMALL/LARGE y la cota gaussiana global de «Cúspides modulares» en POWER_GLOBAL_ROUTE_REVIEW dan L>=c epsilon^(-4), integrando LARGE en[h,h+epsilon]; F<=C epsilon^(-5), integrando la cota global desde0; y b<=C epsilon^(-N)exp(-a/epsilon), con constantes positivas y N fijo. Luego F²H>=c²epsilon^(-8)-C epsilon^(-N-5)exp(-a/epsilon)>0 para epsilon suficientemente pequeño.

**Cúspide par, x=h: se acota el defecto de proyección, no el integral total.** Para 0<=u<=1, w=exp(2(h+epsilon u+iy))=2i+zeta satisface zeta=2epsilon(1+2iu)+O(epsilon²), con resto C1 uniforme. Poisson completo da theta(2i+zeta)=zeta^(-1/2)+R(zeta). En este segmento Re(1/zeta)>=c/epsilon; R y sus derivadas hasta orden3 están acotadas por una potencia fija de epsilon^(-1) por exp(-c'/epsilon). Esto se prueba diferenciando la serie de modos duales no nulos: cada derivada sólo añade potencias de sus índices y de zeta^(-1), absorbidas al extraer parte de la exponencial gaussiana. Con Phi=w^(5/4)[w theta''+(3/2)theta'], el principal es (3/4)(2i)w^(5/4)zeta^(-5/2), por cancelación exacta del término zeta^(-3/2). Así existe C0 distinto de0 tal que

    Phi(h+epsilon u+iy)=C0 epsilon^(-5/2) f_epsilon(u),
    f_epsilon -> f(u)=(1+2iu)^(-5/2) en C1([0,1]).

El mínimo m(f)=min_(beta complejo) integral_0^1|f'-beta f|²du es positivo y continuo bajo esta convergencia, por su fórmula de proyección y porque integral|f|²>0. Más precisamente, con I0=integral_0^1|f|²<=1,

    m(f)=(1/(2I0)) integral_0^1 integral_0^1
                       |f'(u)f(v)-f(u)f'(v)|²du dv,
    |f'(u)f(v)-f(u)f'(v)|²
        =100(u-v)²[(1+4u²)(1+4v²)]^(-7/2),
    m(f)>=100/(2*6*5^7)=1/9375.

Se usa integral integral(u-v)²=1/6. Eventualmente m(f_epsilon)>=1/18750 y |f_epsilon(0)|²<=2. Restringir el integral del mínimo global a[h,h+epsilon], usar v>=h y sustituir beta=epsilon a conserva el mínimo sobre TODOS los escalares complejos; resulta

    min_(a complejo) integral_h^infinito v|Phi'-a Phi|²dv
        >=h|C0|² epsilon^(-6)/18750,
    b<=2|C0|² epsilon^(-5),
    F²H>=4D-Fb
        >=F|C0|² epsilon^(-6)[h/9375-2epsilon]>0

para epsilon suficientemente pequeño. No se necesita cota superior de F ni excluir contribuciones de otras cúspides. No se fija un umbral numérico: la convergencia C1 aporta un intervalo eventual, no cuantificado aquí.

**Alcance.** Sólo estos dos tests necesarios PASAN: CPD de log A y signo global siguen OPEN, sin nueva ruta ni cobertura W/T. No se supone no anulación fuera de estas diagonales ni se usa una asintótica del integral total a partir del perfil de una sola cúspide; en particular no se atribuye al H completo el coeficiente local7/16. Sin cómputos ni cambios en papers.

**Límite de la extensión por proyección conjunta (PROVED, misma actualización).** Cálculo global_restart_checked/root; auditoría independiente arithmetic_fresh_candidate PASS y root PASS. Cotejo dirigido en los tres índices y corpus sin antecedente literal localizado; E73_025§7/E73_030 regularizan otra proyección Cauchy mediante coordenadas Hermite, y R164_401/491 usan cocientes incrementales para densidad. La herramienta de diferencias finitas es clásica. Fijar PRIMERO z0=h+iy dentro del strip, próximo a la cúspide par con Phi(z0)!=0, un intervalo compacto I=[0,ell],ell>0, y un peso positivo continuo fijo w. En L²(I,w du), poner f0(u)=Phi(z0+u), f_eta(u)=Phi(z0+eta+u), y P_eta la proyección sobre su span COMPLEJO. Para eta=i tau, tau real no nulo suficientemente pequeño, ambos nodos conservan parte real h. La cota C2 uniforme de Phi en el compacto interior del strip da

    ||f0'-(f_eta-f0)/eta||=O(|eta|),
    R_00=||(I-P_eta)f0'||²=O(|eta|²),
    R_ij=<(I-P_eta)f_i',(I-P_eta)f_j'>, i,j en{0,eta}.

Con b_i=f_i(0), B=bb*, se tiene B_00=|Phi(z0)|²>0 fijo. Luego NO existe c>0 independiente de eta tal que R>=cB para todos estos pares: basta evaluar en el primer vector coordenado. No hace falta independencia de f0,f_eta ni suponer A PSD. Incluso si c depende de z0,I,w, la uniformidad en la separación falla. Sólo se excluye ESTE pago del borde por ESTE residual; no c(eta), renormalizaciones dependientes de separación, otros términos de la identidad escalar, otras matrices de borde/proyección ni enfoques Gram generales. CPD y signo global siguen OPEN. Además, probar únicamente S=A^(odot2) odot H PSD no prueba H PSD: la división entrada a entrada por A² no preserva positividad en general. Sin nueva ruta, cómputos ni papers editados.

**Promedio horizontal completo en una banda fija (PROVED, 2026-11-06).** Propuesta root, cálculo global_restart_checked y joint_sign_fresh_review; auditorías independientes arithmetic_fresh_candidate PASS y root PASS. El cotejo dirigido en los tres índices y corpus no localizó esta estimación literal; GLOBAL ya tenía lower local epsilon^-4 y upper horizontal epsilon^-5. La diferencia es conservar TODOS los modos y estimar sus cruces oscilatorios integrados, sin aislar una cúspide. Con epsilon=cos(2y) bajando a0, sigma=sin(2y), definir

    B_y=integral_2^4 [log(t)/(2t)] |Phi((log t)/2+iy)|²dt.

Entonces, con c_*=315(log2)²/(512sqrt2)>0,

    epsilon^(9/2) B_y -> c_*,
    A(iy,-iy)>=B_y>=c epsilon^(-9/2)

para epsilon suficientemente pequeño y algún c>0. El equivalente se afirma SÓLO para B_y, no para A completo.

**Cruces y sumas infinitas.** La fórmula modal exacta es

    Phi((log t)/2+iy)
      =2pi² t^(9/4) exp(9iy/2) S_4(t)
         -3pi t^(5/4) exp(5iy/2) S_2(t),
    S_j(t)=sum_(n>=1) n^j exp[-pi t(epsilon+i sigma)n²].

Para cada epsilon>0 fijo, las series, los productos dobles y las derivadas de amplitud siguientes convergen absolutamente y uniformemente en t∈[2,4]. Así se integra y diferencia primero con sumas absolutamente convergentes. Para n!=m, poner Q=n²+m², d=n²-m² y a_nm(t)=[log(t)/(2t)]t^(9/2)exp(-pi epsilon t Q). Integrar por partes contra exp(-i pi sigma d t), con sigma>=1/2 eventualmente, da

    |integral_2^4 a_nm(t)exp(-i pi sigma d t)dt|
        <=C exp(-pi epsilon Q)/|d|.

En efecto, el término de borde y el integral de |a_nm'| se acotan por C(1+epsilon Q)exp(-2pi epsilon Q); el factor adicional se absorbe en la mitad de la exponencial. Como n4m4/(n²-m²)<=n7/(n-m) para n>m, TODOS los cruces del término S_4 tienen suma absoluta

    <=C sum_(n>=1) n7(1+log n)exp(-pi epsilon n²)
    <=C epsilon^(-4)[1+log(1/epsilon)]
     =o(epsilon^(-9/2)).

La segunda cota sigue de log n<=log(1/epsilon)/2+n sqrt(epsilon) y las cotas gaussianas para sumas de potencias. No se desechan casi resonancias: sus fases exactas se integran en esta banda fija.

**Diagonal y constante.** Para f_t(s)=s8 exp(-2pi t s²) y q=sqrt(epsilon),

    epsilon^(9/2) sum_(n>=1)n8 exp(-2pi epsilon t n²)
       =q sum_(n>=1) f_t(nq)
       -> integral_0^infinito f_t(s)ds
        =Gamma(9/2)/[2(2pi t)^(9/2)]

uniformemente en t∈[2,4]. El error de la suma Riemann está acotado por q integral|f_t'|=O(q), uniforme en ese compacto. Usando Gamma(9/2)=105sqrt(pi)/16, el factor4pi4t^(9/2) reduce el límite diagonal a105/(128sqrt2); integrar el peso log(t)/(2t) aporta3(log2)²/4 y da c_*. La norma L² ponderada del término principal es O(epsilon^(-9/4)); la cota gaussiana absoluta sum n²exp(-pi epsilon t n²)<=C epsilon^(-3/2) da norma O(epsilon^(-3/2)) para el término inferior. Su cuadrado es O(epsilon^-3) y su cruce con el principal es O(epsilon^(-15/4)), por Cauchy–Schwarz, ambos o(epsilon^(-9/2)). Esto completa el equivalente de B_y con la serie theta completa, sin cómputos.

**Una cúspide aislada no aproxima el integral completo.** Para h=log2/2 y cada c0>0 FIJO, el Poisson local completo anterior acota |Phi(v+iy)|<=C_(c0)epsilon^(-5/2) en h<=v<=h+c0 epsilon. Por tanto

    integral_h^(h+c0 epsilon) 2v|Phi(v+iy)|²dv
       =O_(c0)(epsilon^-4),
    [ese integral]/A(iy,-iy)=O_(c0)(sqrt(epsilon))->0.

Sólo se afirma este segmento de la cúspide par h, con ancho c0 epsilon y c0 fijo. No se extrapola a bandas de cúspides arbitrarias ni se deduce una asíntota de A total o de H. El resultado controla parte positiva de un integral horizontal completo; no prueba CPD, PSD de A, signo global ni nueva cobertura W/T. Sin nueva ruta ni cambios en papers.

El equivalente del A completo para las escalas enteras fijas se demuestra después en§16 mediante un argumento adicional sobre TODO t>=1; no se infiere del equivalente de B_y.

### 4.2. El kernel theta completo no es log-supermodular en toda la semirrecta

**PROVED, revisión independiente root/theta_joint/casos; deduplicación dirigida mapa (2026-11-05).** Esto refuta una propiedad de entradas, no la positividad matricial. Para cualquier compacto K contenido en (0,infinito), uniformemente en s en K, cuando t tiende a infinito,

    H(t,s)=partial_t partial_s log A(t,s)
           =-1/(t+s)²+O_K(exp(-2t)) < 0

para t suficientemente grande. Por tanto A no es TP2 en toda la semirrecta positiva. La diferencia frente§5 es esencial: aquí se conserva el INTEGRAL theta completo; no se refutan sólo sus capas. Los TP2 de073/112 conciernen a otros kernels.

**Prueba con error diferenciado.** Poner Y=pi exp(2t), u=t+s, p=-Phi'/Phi. La primera moda da exactamente

    Phi(t)=2pi² exp(9t/2) exp(-Y)(1-3/(2Y))(1+R(Y)),

con R y sus derivadas logarítmicas hasta cualquier orden fijo acotadas por un polinomio en Y multiplicado por exp(-3Y), para Y grande. Esto se obtiene término a término de la serie theta: los modos n>=2 tienen el factor exp[-(n²-1)Y], y sus derivadas sólo añaden potencias de n y Y. Introducir v=Y(exp(2r)-1) y r=log(1+v/Y)/2. Entonces

    A(t,s)/(Phi(t)Phi(s))=[u J(Y,s)+K_1(Y,s)]/(2Y),
    J=integral_0^infinito exp(-v)(1+v/Y)^(5/4)
          B_Y(v) Phi(s+r)/Phi(s) dv,
    K_1=integral_0^infinito exp(-v)(1+v/Y)^(5/4)
          B_Y(v) Phi(s+r)/Phi(s) log(1+v/Y) dv,
    B_Y(v)=[(1-3/(2(Y+v)))/(1-3/(2Y))]
            *[(1+R(Y+v))/(1+R(Y))].

El exponente5/4 incluye el Jacobiano; no se omite la suma de modos restantes. Taylor en v/Y da

    J=1+(5/4-p(s)/2)/Y+O_K(Y^-2),
    K_1=1/Y+O_K(Y^-2).

Estos restos conservan el orden bajo (Y partial_Y)^j partial_s^k con j+k<=2. Para justificarlo, derivar primero los integrandos en el dominio fijo v>=0. En v<=sqrt(Y), Taylor con resto de las funciones suaves (incluida Phi cerca de K) produce cotas por C_K(1+v)^m/Y² para algún m fijo, integrables contra exp(-v), también después de esas derivadas. Los factores racionales de B son regulares para Y grande y sus correcciones empiezan en orden v/Y²; la corrección theta es exponencialmente menor. En v>=sqrt(Y), Phi y sus derivadas de orden fijo están acotadas en la semirrecta que comienza en min K, mientras min_K Phi>0. Las derivadas de r tienen crecimiento acotado, y los otros factores tienen a lo sumo crecimiento polinómico en v y Y. Por exp(-v), las integrales de esa cola, después de derivar, son O_K(Y^-N) para cada N fijo. No se deriva una aproximación meramente puntual ni se descartan términos de un corte móvil.

En consecuencia, con resto también diferenciado,

    log A=log Phi(t)+log Phi(s)+log u-log(2Y)
           +(5/4-p(s)/2+1/u)/Y+O_K(Y^-2).

Derivar una vez en cada variable da, más precisamente,

    H(t,s)=-1/u²
       +[p'(s)+2/u²+2/u³]/Y+O_K(Y^-2).

La primera contribución domina porque s queda en un compacto y Y crece exponencialmente. Esto prueba el signo negativo anunciado. Por continuidad, alrededor de uno de esos pares existen pequeños incrementos h,k>0 tales que

    A(t,s)A(t+h,s+k)-A(t,s+k)A(t+h,s)<0.

Son menores RECTANGULARES con conjuntos de filas y columnas diferentes, no menores principales de una matriz Gram. La desigualdad descarta TP2/log-supermodularidad global y, para H, una representación mediante productos de funciones todas no negativas. **NO descarta un Gram de funciones firmadas, PSD de H, CPD de log A ni PSD de A.** La candidata de§4.1 sigue OPEN. No hay nueva positividad W/T ni modificación de papers.

### 4.3. El modelo principal de cola tampoco es una referencia PSD

**PROVED, root/casos/theta_joint; cotejo dirigido mapa (2026-11-05).** Es un corolario del principio de continuación de§2.2 aplicado a dos objetos explícitos distintos. Definir

    G0(t,s)=(t+s)/(exp(2t)+exp(2s)),
    H0(t,s)=sech²(t-s)-1/(t+s)², t,s>0.

Ni G0 ni H0 es PSD en todos los tamaños sobre NINGÚN intervalo abierto no vacío contenido en (0,infinito). Esto incluye toda cola, por lejos que empiece. No es un falsificador de A ni de H reales.

Para G0, el denominador no se anula en el producto de strips |Im t|,|Im s|<pi/4: ambas exponenciales tienen parte real positiva. Si G0 fuese PSD en un intervalo, las diferencias finitas y series de Taylor de§2.2 lo extenderían por pasos de radio fijo a toda la recta real. Pero G0(t,t)=t exp(-2t)<0 para t<0, contradicción.

Para H0, fijar cualquier compacto [a,b] de la semirrecta positiva que conecte el intervalo supuesto con t*=1/4. Con radio rho<min(a/4,pi/8), ni t+s ni cosh(t-s) se anulan en los bidiscos y los dominios mixtos necesarios. El mismo argumento de puntos antiguos más jets propaga PSD a lo largo del compacto. Esto contradice H0(1/4,1/4)=-3. No se intenta alcanzar0 con un radio fijo; el punto contradictorio es estrictamente positivo. En la semirrecta positiva se cumple exactamente H0=partial_t partial_s log G0.

**Relación con la theta completa.** Fijar x,y en un compacto y poner t=L+x,s=L+y, L grande. Escribir Yt=pi exp(2t), Ys=pi exp(2s), E=Yt+Ys y u=t+s. El cambio v=E(exp(2r)-1), con h=v/E, conserva todos los modos y da

    A/(Phi(t)Phi(s))=(1/(2E)) integral_0^infinito exp(-v)
          [u+log(1+h)](1+h)^(7/2) B_t(v)B_s(v)dv,

con B_j=[(1-3/(2Yj(1+h)))/(1-3/(2Yj))]·[(1+R(Yj(1+h)))/(1+R(Yj))], usando el R theta de§4.2. Ahora Yt,Ys son comparables a E. La expansión, con restos estables bajo las derivadas t,s de orden total hasta2, es

    A/(Phi(t)Phi(s))=u/(2E)
       *[1+(7/2+1/u)/E+O(E^-2)].

La justificación es la de§4.2: derivación previa en el dominio fijo de integración, Taylor en v<=sqrt(E) y control exponencial de la cola. Los factores B_t B_s contribuyen sólo O((1+v)^m/E²), aparte de las correcciones theta exponenciales. En consecuencia,

    A(t,s)=[Phi(t)Phi(s)/(2pi)]G0(t,s)[1+O(exp(-2L))],
    H(t,s)=H0(t,s)+O(exp(-2L)),

uniformemente para x,y en ese compacto. La primera igualdad incluye una congruencia diagonal positiva. Las estimaciones de entradas, aunque diferenciadas, NO permiten trasladar la indefinición de G0/H0 al kernel real: el tamaño del bloque y el vector negativo del modelo no están controlados uniformemente con L.

**Consecuencia para el método.** No procede usar G0 o H0 como referencia PSD de una prueba perturbativa de todos los órdenes. Tampoco puede cumplirse un sándwich simétrico (1-epsilon)H0 <= H <= (1+epsilon)H0 en orden de formas, con epsilon>0: sumando las dos diferencias PSD se obtendría 2epsilon H0 PSD, que es falso; idéntico argumento para el modelo directo después de congruencia. Una cota unilateral respecto de un modelo indefinido no cierra el signo sin pagar sus direcciones negativas. No se excluyen otras referencias positivas ni una compensación firmada exacta. La positividad real y el criterio logarítmico permanecen OPEN; sin nuevo signo W/T.

## 5. Condición necesaria infinitesimal y fallo para la Phi real

Poner V=-log phi y f=V'. Elegir nodos positivos, de modo que tau>0. En v=0,

    S_0(t,s)=phi(t)phi(s),
    B_v(t,s)=S_v(t,s)/[phi(t)phi(s)],
    B_0(t,s)=1,
    partial_v B_v(t,s)|_(v=0)
           =-[f(t)+f(s)]/(t+s)=-K_f(t,s).             (JET)

Para t=s la fórmula es K_f(t,t)=f(t)/t. No se necesitan nodos con t+s=0. Para cada conjunto finito de nodos, la suavidad da una expansión de primer orden con resto o(v).

Si todas las capas fuesen PSD, para todo vector c con sum_i c_i=0 se tendría

    0<=c^T B_v c=-v c^T K_f c+o(v),

y, dividiendo por v>0 y pasando al límite,

    c^T K_f c<=0.                                    (CND)

Esta es sólo una condición necesaria. A continuación se construye una violación exacta de ella bajo una hipótesis de crecimiento específica.

Fijar dos números 0<alpha<beta y añadir un tercer nodo R>beta. Escribir k_ij=K_f(t_i,t_j), t=(alpha,beta,R), y definir

    Q_ab=k11+k22-2k12,
    Q_bR=k22+k33-2k23,
    B=k13-k12-k23+k22.

Para c=(1,-1-epsilon,epsilon), cuya suma es0,

    c^T K_f c=Q_ab+2epsilon B+epsilon^2 Q_bR.          (TRIPLE)

Suponer ahora f(R)/R^3->+infinito. Las constantes que involucran sólo alpha,beta son fijas. De las fórmulas de las entradas se obtiene

    B/[f(R)/R^2]->beta-alpha,
    Q_bR/[f(R)/R]->-1.                               (ASYM)

Por ejemplo, la parte dominante de B es

    f(R)[1/(R+alpha)-1/(R+beta)]
      =(beta-alpha)f(R)/[(R+alpha)(R+beta)],

y la de Q_bR es f(R)[1/R-2/(R+beta)]. Los demás términos son constantes o O(1/R), insignificantes en esas escalas. Así, para R suficientemente grande pero FINITO, Q_bR<0 y B>0. Elegir exactamente

    epsilon=-B/Q_bR>0.

Entonces TRIPLE vale Q_ab+B^2/(-Q_bR), y

    [B^2/(-Q_bR)]/[f(R)/R^3]->(beta-alpha)^2>0.

El valor es positivo para algún R finito. Esto contradice CND.

Para traducir la contradicción a una capa concreta, fijar esos nodos y ese vector c. Si Q=c^T K_f c>0, JET implica c^T B_v c=-vQ+o(v)<0 para todo v>0 suficientemente pequeño. Con d_i=c_i/phi(t_i) se tiene d^T S_v d=c^T B_v c<0. Por tanto existe una capa FINITA, en tres nodos reales positivos, que no es PSD. No se ha calculado R ni v ni se requiere hacerlo.

La Phi REAL satisface la hipótesis: la cola auditada de POWER_MIXED_VOLTERRA_OBSTRUCTION_105, sección4, da

    f(R)=V'(R)=2pi exp(2R)+O(1), R->infinito.

En particular f(R)/R^3->+infinito. La obstrucción se aplica al dato real, usando su crecimiento específico, sin invocar ninguna clase genérica descartada en074/101/111.

## 6. Alcance exacto

Quedan probadas la identidad LT, la suficiencia uniforme de las capas PSD, el modelo cuártico y la imposibilidad de que TODAS las capas de la Phi real sean PSD. La desigualdad negativa hallada pertenece a una capa S_v; NO es una desigualdad negativa para su integral A, ni para un bloque del kernel de M, ni para W.

Una suma o integral de kernels indefinidos puede ser PSD. La presente obstrucción no excluye cancelación entre capas, un reordenamiento firmado, otro Gram ni una desigualdad conjunta específica de las capas reales. Tampoco amplía una dimensión finita o una ventana temporal del signo conocido.

Finalmente, la diagonal del kernel completo es

    A(t,t)=integral_t^infinito 2u phi(u)^2du,

no J(t)=integral_t^infinito u phi(u)du del CORE. La entrada opuesta es

    A(t,-t)=integral_0^infinito 2r phi(r+t)phi(r-t)dr.

No se infiere el signo de su menor a partir del fallo de una capa. Esta nota no contiene un falsificador de PSD del kernel integral completo.


## 7. Hipótesis genéricas y operaciones positivas

**PROVED, consecuencias analíticas sin nuevos cómputos.**074 tiene V(t)=g(t²) con g polinómica convexa, coeficientes no negativos y todas sus derivadas no negativas; satisface V'''(t)>0 para t>0 pero su kernel transformado3 es indefinido. Por LT su A tampoco es PSD. Es un corolario del falsificador existente, no un falsificador real theta.

Las mezclas positivas no conservan A PSD. Para dos gaussianas centradas normalizadas distintas, Z(u)=C1 exp(v1 u²/2)+C2 exp(v2 u²/2), C_i,v_i>0. N=M/u es el promedio inclinado de v_i y N'=u Var_u(v)>0. Luego uM'>M, contrario al criterio001§3. El menor de nodos u,u+h tiene coeficiente de h² igual a [M²-u²M'²]/(4u⁴)<0. Por LT, A no es PSD para esa mezcla, aunque cada gaussiana pertenece al modelo positivo de§4.

Convolución sí conserva el kernel transformado: Z=Z1Z2 implica M=M1+M2, suma de kernels PSD. Pero una convolución con un factor exp(-at⁴-bt²) no nulo y otro factor positivo con masa en un compacto tiene cota inferior c exp(-C(1+|t|⁴)). Una mezcla positiva no nula de tales factores también: se restringe la medida de parámetros a una caja acotada de masa positiva y finita. Esto excluye esas representaciones exactas de Phi real, por su supercola. No excluye otros factores ni mezclas firmadas.

La identidad de integración por partes con B(t,s)=(t+s)/(f(t)+f(s)), f=V', conserva una corrección: A=B Phi(t)Phi(s)+integral_0^infinito (partial_t+partial_s)B(t+r,s+r)Phi(t+r)Phi(s+r)dr, donde esté definida y los bordes se anulen. No puede certificarse haciendo PSD ambos términos: en la diagonal positiva, (partial_t+partial_s)B=(f-tf')/f²<0, consecuencia de073. Es una obstrucción a ese descarte, no al balance conjunto.

Tampoco basta un operador positivo que represente tPhi. La misma mezcla gaussiana tiene transformada Fourier H=Σ A_i exp(-omega²/(4a_i))>0. El multiplicador b0=-H'/(omega H), removible en0, es promedio de 1/(2a_i), y define un operador acotado autoadjunto positivo que satisface Bop(-Phi')=tPhi. Para h suave compacto y F(r)=integral h(t)Phi(t+r)dt, Fubini da Q_A(h)=-2 Re integral_0^infinito Bop F'(r) conjugado(F(r))dr. La positividad del operador no controla esta forma sobre la semirrecta, y A ya es indefinido en este ejemplo. No se requiere aplicar la derivada a la función cortada por la semirrecta.

La búsqueda dirigida de hazard, cocientes y Lyapunov en índices/corpus encontró103_42/43 y073, de objetos de curvatura/pares, sin duplicado literal de esta integración por partes. El fallo diagonal es consecuencia inmediata073 y no se presenta como herramienta nueva. PSD del A REAL sigue OPEN.


### 7.1. Convolución gaussiana: recíproca por un nodo que tiende a infinito

**PROVED como equivalencia de signo, revisión root/casos y cotejo dirigido mapa.** La preservación por convolución de§7 ya era conocida. Se añade una recíproca bajo una condición de decaimiento del kernel que sí cumple la Phi real. No es el flujo que multiplica la densidad por exp(lambda t²), ni la representación gaussiana de los tests gamma.

**Lema de rango uno.** Sea K un kernel real simétrico en(0,infinito) tal que, para cada u fijo,

    K(u,R)->0,   K(R,R)->0   cuando R->infinito.

Para cualquier b>=0, K+b es PSD en todos los bloques finitos si y sólo si K lo es. La suficiencia es inmediata. Para la necesidad, si un bloque U=(u_i) y un vector c dan q=sum c_i c_j K(u_i,u_j)<0, añadir un nodo R mayor que todos los u_i y el coeficiente d=-sum c_i. La contribución constante b se anula exactamente, y la nueva forma vale

    q+2d sum_i c_i K(u_i,R)+d²K(R,R) -> q<0.

Para R suficientemente grande contradice PSD de K+b. La prueba utiliza todos los tamaños y nodos arbitrariamente grandes; no establece una equivalencia en tamaño fijo o en un rango acotado de nodos.

**Condición verificada para Phi.** Sea F(u)=log(Z(u)/Z(0)), con u>=0. Positividad y paridad de Phi dan F>=0 y M=F'>=0; F es convexa. Para todo N>0, Phi(t)<=C_N exp(-Nt²), de donde F(u)<=u²/(4N)+D_N. Por convexidad,

    0<=M(u)/u <=[F(2u)-F(u)]/u² <=1/N+D_N/u².

Como N es arbitrario, M(u)/u->0. Así K(u,v)=(M(u)+M(v))/(u+v) cumple las dos condiciones del lema.

**Aplicación.** Sea G_sigma la gaussiana centrada normalizada de varianza sigma², sigma>0. Su convolución temporal con Phi tiene

    Z_sigma(u)=exp(sigma²u²/2)Z(u),
    M_sigma(u)=M(u)+sigma²u,
    K_sigma(u,v)=K(u,v)+sigma².

Por tanto K_sigma es PSD en todos los órdenes para UNA varianza sigma² fija si y sólo si K lo es. Multiplicar G_sigma*Phi por exp(-sigma²/8) conserva además el momento Z(1/2)=1/4; esa constante no modifica M_sigma ni K_sigma. La paridad y la positividad puntual se conservan.

**Obligación restante.** Una prueba independiente del signo de una sola densidad suavizada cerraría el signo del kernel original. Aquí no se obtiene tal prueba. Tampoco se puede suponer que suavizar convierte un kernel globalmente indefinido en uno PSD: el lema lo impide en esta clase. Esto no descarta usar la equivalencia para encontrar una representación más manejable, ni excluye otras convoluciones. No hay nueva positividad de W, ventanaT o modificación de papers.

## 8. Ningún modo theta individual proporciona un Gram local de todos los órdenes

**PROVED, revisión matemática independiente root/casos; cotejo dirigido mapa.** El antecedente modal103_47/48 ya contiene la traslación siguiente; no se presenta como nueva. La diferencia respecto de la mera identidad de cruces es un falsificador de la positividad de cada kernel modal, seguido de su alcance LOCAL mediante§2.2. Sin cálculos numéricos ni prioridad bibliográfica afirmada.

Escribir

    h(x)=pi exp(5x/2)[2pi exp(2x)-3]exp(-pi exp(2x)),
    Phi_n(t)=n^(-1/2)h(t+log n),
    A_n(t,s)=integral_0^infinito
                (t+s+2r)Phi_n(t+r)Phi_n(s+r)dr.

No se aplica a Phi_n la cancelación par de§2: cada modo individual NO es par. Se tiene exactamente

    A_n(t,t)=(2/n)integral_(t+log n)^infinito
                         (x-log n)h(x)^2 dx.

La masa H=integral_R h(x)^2 dx y su primer momento absoluto son finitos. Demostraremos que m=H^(-1)integral xh(x)^2 dx<0. Así

    lim_(t→-infinito) A_n(t,t)=(2H/n)(m-log n)<0

para TODOS los enteros n>=1, incluido el primer modo.

Prueba elemental del momento. Poner z=2pi exp(2x), alpha=5/2. Salvo una constante positiva, h(x)^2dx=z^(alpha-1)(z-3)^2exp(-z)dz. Definir

    I_alpha=integral_0^infinito z^(alpha-1)exp(-z)dz,
    J_alpha=integral_0^infinito log(z)z^(alpha-1)exp(-z)dz.

Integrar por partes da I_(alpha+1)=alpha I_alpha y J_(alpha+1)=alpha J_alpha+I_alpha. En alpha=5/2,

    I_(alpha+2)-6I_(alpha+1)+9I_alpha=(11/4)I_alpha,
    J_(alpha+2)-6J_(alpha+1)+9J_alpha=(11/4)J_alpha.

En la segunda igualdad el término adicional es (2alpha+1-6)I_alpha=0. Como x=(log z-log(2pi))/2,

    m=(1/2)[J_alpha/I_alpha-log(2pi)].

Jensen estricto para log bajo la probabilidad z^(alpha-1)exp(-z)dz/I_alpha da J_alpha/I_alpha<log(alpha), pues su media es alpha. Por tanto m<(1/2)log(5/(4pi))<0. Esto verifica el signo sin estimar una serie ni truncar la aritmética.

Cada A_n es conjuntamente holomorfo en el producto de strips |Im t|,|Im s|<pi/4: para r→infinito se aplica el mismo dominio de convergencia exponencial de§2.2; no se exige paridad ni positividad de h. El principio de propagación analítica, que sólo usa esa holomorfía, muestra que A_n NO puede ser PSD de todos los tamaños en ningún intervalo real abierto. De lo contrario sería PSD global y contradice la diagonal negativa recién probada. En particular, esto vale en intervalos positivos donde Phi_n es positiva y A_n tiene diagonal positiva. No se obtiene un tamaño explícito del menor negativo local ni se lanza una campaña para encontrarlo.

Alcance: queda descartado certificar el kernel completo mediante Grams separados de cada modo theta, aun empezando en una cola temporal. No se refuta A de la Phi real: A incluye todos los pares de modos n,m, no sólo sum_n A_n, y su simetría global permite cancelaciones ausentes en cada modo. Tampoco se descarta una estimación conjunta ni un reagrupamiento distinto con sus cruces controlados.


### 8.1. El prefijo theta completo también falla: se conservan todos sus cruces

**PROVED para todo prefijo suficientemente grande, revisión independiente root/casos y cotejo dirigido mapa.** Cambio frente a§8: Phi_M=sum_(n=1)^M Phi_n se introduce COMPLETA en la definición de A; se incluyen todos los pares n,m<=M. Los antecedentes de colas correlacionadas103_47/48 y truncación Euler no son esta afirmación sobre el cuadrado de un prefijo theta. No se calcula un umbral M ni se inicia una campaña.

Definir f_M(x)=M^(-1/2)Phi_M(x-log M). Con a_x=pi exp(2x),

    f_M(x)=pi exp(5x/2)(1/M)sum_(n=1)^M
       (n/M)^2[2a_x(n/M)^2-3]exp[-a_x(n/M)^2].

Para x fijo es una suma Riemann. Como la derivada de z³exp(-a_x z²) es z²[3-2a_x z²]exp(-a_x z²),

    f_M(x)→F(x)=-pi exp(5x/2)exp[-pi exp(2x)].

Es necesario controlar la masa que se mueve con M, no sólo este límite puntual. Para x<=0, a_x<=pi y la suma anterior da |f_M(x)|<=C exp(5x/2), uniformemente en M. Para x>=0 poner lambda=a_x/M². Entonces

    |f_M(x)|<=3pi exp(5x/2)M^(-3)
                 sum_(n>=1)n²(1+lambda n²)exp(-lambda n²).

En v∈[n-1/2,n], n²<=4v², 1+lambda n²<=4(1+lambda v²) y exp(-lambda n²)<=exp(-lambda v²). Integrando sobre esos intervalos disjuntos de longitud1/2,

    sum_(n>=1)n²(1+lambda n²)exp(-lambda n²)
      <=32 integral_0^infinito v²(1+lambda v²)exp(-lambda v²)dv
      =C0 lambda^(-3/2).

Así |f_M(x)|<=C1 exp(-x/2) para x>=0. Ambos mayorantes tienen cuadrado integrable con peso1+|x|. Convergencia dominada prueba f_M→F en L²((1+|x|)dx), de donde

    H_M=integral f_M²→H=integral F²>0,
    J_M=integral x f_M²→J=integral x F².

La identidad de cambio de variable es exacta:

    integral_R t Phi_M(t)^2dt=M[J_M-log(M)H_M],
    [integral t Phi_M²]/[M log M]→-H<0.

Por tanto ese momento es negativo para TODO M suficientemente grande. Para cada tal M,

    lim_(t→-infinito) A_[Phi_M](t,t)
          =2 integral_R x Phi_M(x)^2dx<0.

La finitud del momento absoluto se sigue también directamente de las colas de la suma finita. A_[Phi_M] es holomorfo en los mismos strips que cada modo;§2.2 implica que NO es PSD de todos los tamaños en ningún intervalo real abierto. La falta de paridad del prefijo impide usar la cancelación de§2, pero no afecta al principio analítico.

El fallo no desaparece al incluir los cruces dentro del prefijo. La masa cuadrática del prefijo es M H_M~M H y se desplaza hacia t=-log M; por eso la convergencia de la serie theta en compactos no es convergencia de estos prefijos en la norma global ponderada por1+|t|. La Phi infinita es par y su primer momento cuadrático vale0, sin contradicción. Este resultado descarta una prueba por prefijos theta eventualmente PSD; no descarta una estimación conjunta con la cola omitida, una reorganización distinta ni el signo del kernel real completo. No prueba una cota positiva ni amplía T.


**Fortalecimiento: el descarte vale para TODO M>=1.** Revisión independiente root/casos, con cotejo dirigido de antecedentes. La asintótica anterior describe el defecto de masa, pero no hace falta para excluir prefijos pequeños. Sustituir z=pi exp(2t) en la transformada de h da, para u>-5/2,

    Z_h(u)=C(u)(u-1/2),
    C(u)=(1/2)pi^(-u/2-1/4)Gamma(u/2+5/4)>0.

Por la traslación de cada modo,

    Z_[Phi_M](u)=(u-1/2)H_M(u),
    H_M(u)=C(u)sum_(n=1)^M n^(-u-1/2)>0.

H_M es C¹ cerca de1/2. Por tanto, para u<1/2 suficientemente próximo y aún positivo, Z_[Phi_M](u)<0 mientras su derivada H_M(u)+(u-1/2)H_M'(u)>0. Son signos de una fórmula explícita del aproximante; no se utiliza un argumento sobre ceros.

LT también vale aquí sin paridad. Para phi=Phi_M, poner B(t)=[integral_t^infinito(1+x²)phi(x)^2dx]^(1/2). La desigualdad (x+y)²<=(1+x²)(1+y²) y Cauchy–Schwarz dan |A_phi(t,s)|<=B(t)B(s). B es acotada a izquierda y tiene supercola a derecha; así integral exp(ut)B(t)dt es finita para cada u>0. Esta cota y las colas de phi justifican la transformada doble, la integración por partes en LT y la truncación del test exponencial. En el u elegido,

    integral integral exp[u(t+s)]A_[Phi_M](t,s)dt ds
                       =Z_[Phi_M](u)Z_[Phi_M]'(u)/u<0.

Luego A_[Phi_M] no es PSD para ningún M>=1, y la continuación analítica excluye PSD en cualquier intervalo abierto. Esto amplía también a TODO M el descarte de reparaciones que mantengan intacta una cola derecha del prefijo bruto. El alcance de Q_M en§8.2 sigue siendo eventual; no se cambia por esta prueba.

### 8.2. Añadir la cola continua mejora la convergencia, pero no restaura PSD

**PROVED, revisión independiente root/casos y cotejo mapa.** Se cambia el aproximante de§8.1: ahora

    Q_M(t)=Phi_M(t)+pi M³exp(5t/2)exp[-pi M²exp(2t)].

El segundo término es exactamente integral_M^infinito Phi_n(t)dn, tratando n como variable real. No se presenta como nueva la operación Euler–Maclaurin. El resultado específico es que Q_M→Phi en L²((1+|t|)dt), pero su kernel temporal sigue sin ser PSD para todo M suficientemente grande. Se conservan los cruces de la corrección con el prefijo y con la Phi real.

Poner E_M=Q_M-Phi y g_x(z)=z^(-1/2)h(x+log z). La identidad exacta de la cola es

    E_M(x-log M)=sqrt(M)[integral_1^infinito g_x(z)dz
                           -(1/M)sum_(n>M)g_x(n/M)].

La regla de trapecios con paso1/M, sumada sobre la semirrecta, da

    E_M(x-log M)=h(x)/(2sqrt(M))+R_M(x),
    |R_M(x)|<=G(x)/(8M^(3/2)),
    G(x)=integral_1^infinito |g_x''(z)|dz.              (TRAP)

La cota elemental se obtiene integrando el resto contra el kernel cuadrático de cada celda, cuya altura es a lo sumo1/(8M²). Los bordes en infinito se anulan.

Para verificar que la cota sirve globalmente, escribir H(v)=v²(2pi v²-3)exp(-pi v²). Entonces g_x(z)=pi exp(x/2)H(exp(x)z), y

    G(x)=pi exp(3x/2)integral_(exp x)^infinito |H''(v)|dv.

Así G(x)<=C exp(3x/2) a izquierda y posee una cola doble exponencial a derecha. En particular h y G pertenecen a L²((1+|x|)dx). TRAP y el cambio t=x-log M dan la convergencia ponderada anunciada y

    integral t E_M(t)^2dt
      =-[||h||²/(4M)]log M+O(1/M+log M/M²).           (ERR-MOM)

Falta pagar los cruces, que no se eliminan por declarar pequeño E_M. Para cualquier alpha>0 existe C_alpha con |h(x)|<=C_alpha exp(-alpha x) para todo x: su cola derecha es doble exponencial y su cola izquierda decae. Las supercolas de Phi implican por ello

    integral |t|Phi(t)|h(t+log M)|dt=O_alpha(M^(-alpha)).

La contribución cruzada del borde principal de TRAP es entonces O(M^(-3/2)), tomando alpha=1. Por Cauchy–Schwarz ponderada, la del resto es O(M^(-3/2)sqrt(1+log M)); se puede usar la cota más floja O(M^(-3/2)log M) para M>=2. Como Phi es par, integral tPhi(t)^2dt=0. Se obtiene

    integral t Q_M(t)^2dt
      =-[||h||²/(4M)]log M
           +O(1/M+log M/M^(3/2))<0                  (Q-MOM)

para M suficientemente grande. No se necesita calcular un umbral.

Cada Q_M es holomorfa en el strip y tiene momentos cuadrados absolutos finitos. El límite diagonal de su A es dos veces Q-MOM;§2.2 vuelve a excluir PSD en cualquier intervalo temporal abierto. A diferencia del prefijo bruto, aquí el defecto negativo tiende a0 y sí hay convergencia global de densidades: eso no prueba que la aproximación conserve el signo, ni decide el del límite. Se descarta exactamente esta primera corrección continua como fuente de aproximantes eventualmentePSD, no otras correcciones ni un control conjunto diferente. Sin datos nuevos ni modificaciones de papers.


### 8.3. Simetrizar el prefijo corregido tampoco restaura PSD

**PROVED para TODO M>=1, revisión independiente root/casos y cotejo dirigido mapa.** Cambia otra hipótesis: S_M(t)=[Q_M(t)+Q_M(-t)]/2 es par, de modo que el momento impar usado en§8.2 ahora se anula exactamente. La prueba siguiente usa la forma cuadrática transformada completa, no vuelve a aplicar aquel falsificador. Ningún argumento sobre ceros es necesario.

Sea C=pi^(-1/4)Gamma(5/4)/4>0. Sustitución z=pi exp(2t) e integración por partes dan integral h=-C y la integral de la corrección continua de Q_M es2C sqrt(M). Así

    integral S_M=integral Q_M
       =C[2sqrt(M)-sum_(n=1)^M n^(-1/2)]>=C>0,

pues sum n^(-1/2)<=1+integral_1^M x^(-1/2)dx=2sqrt(M)-1. Por otro lado, expandir los exponentes en la cola izquierda da

    Q_M(t)=-[pi M(3M+1)/2]exp(5t/2)+O_M(exp(9t/2)).

Se usó exactamente sum_(n=1)^M n²=M(M+1)(2M+1)/6. La cola derecha de Q_M es doble exponencial. Por tanto

    S_M(t)=-D_M exp(-5|t|/2)+O_M(exp(-9|t|/2)),
    D_M=pi M(3M+1)/4>0.

Su transformada Z_M(u)=integral exp(ut)S_M(t)dt existe para |Re u|<5/2, satisface Z_M(0)>0 y

    Z_M(u)=-D_M/(5/2-u)+O_M(1)→-infinito,
                   u→(5/2) desde abajo.

Elegir el primer punto positivo donde Z_M alcanza el nivel Z_M(0)/2. En el intervalo anterior Z_M es positiva; el teorema del valor medio da un punto u>0 con Z_M(u)>0 y Z_M'(u)<0. Esto sólo usa un nivel estrictamente positivo, no información sobre ceros.

Hay que justificar LT para estas colas, que no son gaussianas. Para cualquier S par con |S(t)|<=C0 exp(-beta|t|), la cancelación par en la integral de A sigue siendo válida aunque S tenga signo variable. Con tau=(t+s)/2 y d=(t-s)/2,

    |A_S(t,s)|<=C0² integral_|tau|^infinito
                       2sigma exp[-2beta max(sigma,|d|)]dsigma
       <=C_beta(1+t²+s²)exp[-beta(|t|+|s|)].

Esto prueba convergencia absoluta e integración por partes en LT para |Re u|,|Re v|<beta. Aplicar beta=5/2 al punto anterior produce

    integral_R² exp[u(t+s)]A_[S_M](t,s)dt ds
                       =Z_M(u)Z_M'(u)/u<0.

Truncar las exponenciales conserva el valor negativo para un corte suficientemente grande por convergencia dominada. Aproximar la integral compacta por sumas da una matriz finita negativa: A_[S_M] no es PSD. Su integral es conjuntamente holomorfa en los mismos strips (la cola en r es ahora exponencial, uniforme en compactos), por lo que§2.2 excluye PSD en cualquier intervalo temporal abierto.

La simetrización conserva la convergencia ponderada a Phi de§8.2 y elimina su momento impar, pero introduce colas negativas en ambos extremos; no proporciona aproximantes positivos, para ningún M>=1. No refuta A_[Phi], cuyas colas son positivas y doble exponenciales. Tampoco excluye otras correcciones que preserven simultáneamente paridad y estructura de colas. No hay nueva positividad ni ventana T.


**Alcance común de§§8–8.3: reparar sólo la izquierda no cambia el test negativo.** Revisión root/casos. Si una densidad psi coincide con f en [R,infinito), entonces A_psi(t,s)=A_f(t,s) para t,s>=R, directamente porque r>=0 en la integral. El menor negativo de A_f en(R,R+1) se conserva exactamente. No se requiere analiticidad de psi, sólo que su integral exista en esos nodos. Por tanto reflejar o suavizar cerca del origen, manteniendo intacta una cola derecha de los aproximantes excluidos, no los repara: todos los modos, todos los S_M y todos los Phi_M están cubiertos (M>=1 en los dos últimos casos); para Q_M el resultado vale para M suficientemente grande. No se excluyen correcciones que alteren la cola derecha, aunque sean pequeñas; tampoco se conoce un tamaño fijo universal del menor negativo. Es una consecuencia de los resultados anteriores, no un nuevo mecanismo ni una obstrucción para la Phi completa.


**Extensión del descarte modal a cortes suaves de soporte infinito.** Revisión root/casos y cotejo mapa, sin antecedente literal encontrado. Sean w_n>=0, no todos nulos, con sum_n w_n n²<infinito, y phi_w(t)=sum_n w_n Phi_n(t). Esta condición incluye w_n=exp(-epsilon n²), epsilon>0, y los cortes finitos, pero NO los pesos reales completos w_n=1. El cambio frente al prefijo es permitir una suma infinita suavizada conservando todos sus cruces; no es calor en la variable temporal ni truncación de un producto Euler.

La cota global |h(x)|<=C exp(5x/2) controla la cola izquierda de phi_w por C exp(5t/2)sum w_n n². A derecha se absorbe el factor polinómico en exp(-pi n² exp(2t)), obteniendo C exp(5t/2)exp[-(pi/2)exp(2t)]sum w_n n². En substrips compactos del strip |Im t|<pi/4 se obtienen las mismas cotas con constantes positivas modificadas; los factores adicionales de las derivadas se absorben en la exponencial. Hay convergencia normal y el A asociado es conjuntamente holomorfo.

Para u>0, Fubini absoluto da

    Z_[phi_w](u)=(u-1/2)H_w(u),
    H_w(u)=C(u)sum_n w_n n^(-u-1/2)>0,

con C(u) como en el fortalecimiento de§8.1. H_w es C¹ cerca de1/2: el factor log n de la derivada queda dominado por la hipótesis sum w_n n²<infinito. Así Z<0 y Z'>0 inmediatamente a la izquierda de1/2. La cota B de§8.1 legitima LT y la truncación del test, dando un valor cuadrático negativo ZZ'/u. Por§2.2, A_[phi_w] no es PSD en ningún intervalo abierto.

Quedan excluidos estos cortes suaves como aproximantes positivos, aun cuando al retirar la regularización converjan en compactos a Phi. No se extiende la factorización/intercambio al peso w_n=1 bajo estas hipótesis; tampoco se descartan regularizaciones diferentes que conserven la compensación completa. No hay resultado negativo sobre A_[Phi] ni nueva ventanaT.

### 8.4. Un momento exponencial cancelado excluye PSD; cortes del producto de Jacobi

**PROVED, clase y momento explícitos.** Revisión matemática independiente root/casos; cotejo dirigido de antecedentes por mapa. Los apartados anteriores usan signos de pesos o coeficientes concretos. Aquí se permite una densidad firmada y se aísla el motivo común: un momento exponencial nulo. La aplicación a polinomios en exp(-pi exp(2t)) incluye coeficientes firmados y los cortes del producto de Jacobi, no sólo prefijos de modos cuadrados. No se afirma prioridad mundial ni se recurre a información externa sobre el signo objetivo.

**Lema.** Sea phi real, continua y no idénticamente nula. Suponga, para alguna eta>0, decaimiento O(exp(eta t)) a izquierda y decaimiento más rápido que cualquier exponencial a derecha. Sea c>0 tal que

    Z(c)=integral_R exp(ct)phi(t)dt=0.                 (CANCEL)

Entonces A_phi(t,s)=integral_0^infinito(t+s+2r)phi(t+r)phi(s+r)dr no es PSD en toda la recta. Si además A_phi es conjuntamente holomorfa en un producto de strips de anchura positiva, no es PSD en ningún intervalo real abierto no vacío.

**Prueba.** Para u,v>0, hacer x=t+r,y=s+r dentro de la integral triple da, con convergencia absoluta,

    integral_R² exp(ut+vs)A_phi(t,s)dt ds
       =[Z'(u)Z(v)+Z(u)Z'(v)]/(u+v).                 (LT-CANCEL)

En efecto, el valor absoluto antes de integrar en r está acotado por exp(-(u+v)r) multiplicado por

    (integral |x|exp(ux)|phi(x)|dx)(integral exp(vy)|phi(y)|dy)
      +(integral exp(ux)|phi(x)|dx)(integral |y|exp(vy)|phi(y)|dy),

que es finito por las colas supuestas. No se necesita paridad ni signo puntual de phi. Si A_phi fuese PSD, aproximar las integrales compactas por sumas finitas y retirar el corte mediante esta cota daría Z(u)Z'(u)/u>=0 para todo u>0. Así (Z(u)²)' >=0. Como Z(c)²=0, necesariamente Z(u)=0 para todo 0<u<c.

Esto fuerza phi=0: Z es holomorfa en Re u>-eta por las mismas cotas; la identidad en un intervalo implica identidad en ese semiplano, y en una recta vertical interior es la transformada de Fourier de una densidad integrable exp(u0 t)phi(t). Su unicidad da la contradicción. De manera equivalente, algún u0 en(0,c) satisface Z(u0)²>0, y el valor medio aplicado entre u0 y c produce un u con Z(u)Z'(u)<0. LT-CANCEL y truncación dan un test cuadrático negativo; sumas de Riemann dan un bloque finito negativo. La última afirmación del lema sigue de la continuación analítica PSD de§2.2.

**Aplicación polinómica.** Sea P un polinomio real no constante, q(t)=exp(-pi exp(2t)), y defina

    F_P(t)=exp(t/2)P(q(t)),
    phi_P(t)=(D²-1/4)F_P(t)/4.

Si P(q)=p0+sum_(k>=1)p_k q^k, una diferenciación exacta da

    phi_P=(1/2)sum_(k>=1)p_k Phi_[sqrt(k)],
    Phi_[b](t)=pi b² exp(5t/2)(2pi b²exp(2t)-3)
                  exp(-pi b²exp(2t)).

El término p0 desaparece; la escala menor con coeficiente no nulo domina la cola derecha, así que phi_P no es idénticamente nula. La cola izquierda es O(exp(5t/2)), la derecha es superexponencial y A_phiP es holomorfa en |Im t|,|Im s|<pi/4. El momento requerido se obtiene conservando los bordes:

    integral_R exp(t/2)phi_P(t)dt
      =(1/4)[exp(t/2)(F_P'(t)-F_P(t)/2)]_-infinito^infinito=0.

En ambos extremos el borde es -2pi exp(3t)q(t)P'(q(t)) y tiende a0. No se presupone integrabilidad de F_P, que puede crecer a derecha. El lema con c=1/2 prueba que A_phiP falla PSD en cualquier intervalo real abierto.

**Producto de Jacobi.** La identidad clásica theta_3(0,q)=prod_(n>=1)(1-q^(2n))(1+q^(2n-1))² está en [DLMF20.5.3](https://dlmf.nist.gov/20.5.E3). Para cada J>=1, su corte

    P_J(q)=prod_(n=1)^J(1-q^(2n))(1+q^(2n-1))²

es un polinomio real no constante, por lo que el resultado anterior se aplica. Incluye TODOS los cruces de sus coeficientes firmados, aunque cada factor del producto sea positivo para0<q<1. J=0 produce la densidad nula y queda fuera del enunciado.

**Alcance.** No se puede pasar CANCEL al producto infinito mediante convergencia en compactos: para la Phi completa, positiva, integral exp(t/2)Phi(t)dt es estrictamente positiva. El descarte no es una refutación de su núcleo ni de una reorganización que conserve el momento completo. Sí impide usar estos cortes polinómicos como aproximantes PSD. No se ha obtenido una desigualdad para el producto completo, una nueva ventanaT ni una prueba global; papers intactos.

### 8.5. Simetrizar los cortes de Jacobi: corolario del criterio de pares

**PROVED para todo J>=1, revisión root/casos y cotejo mapa.** El criterio de pares procede de CONE001§3; no se presenta como principio nuevo. La aplicación siguiente no apareció en las fuentes cotejadas. A diferencia de§8.4 se restaura la paridad; a diferencia de§8.3 la cola resultante es POSITIVA y el test negativo requiere dos nodos, no una diagonal negativa.

Con P_J y phi_PJ de§8.4, sea S_J(t)=[phi_PJ(t)+phi_PJ(-t)]/2. Al tender q a1 desde abajo,

    P_J(q)=8^J J!(1-q)^J[1+O(1-q)].

Así, para beta=2J+1/2 y A_J=8^J J!pi^J, la cola izquierda de F_PJ es A_J exp(beta t)[1+O(exp(2t))]. Diferenciar esta expansión convergente y usar la supercola derecha da

    S_J(t)=D_J exp(-beta|t|)+O(exp(-(beta+2)|t|)),
    D_J=A_J(beta²-1/4)/8>0.                          (SJ-TAIL)

En particular, para u<beta próximo a beta, la transformada Z de S_J satisface

    Z(u)=D_J/(beta-u)+O(1),
    Z'(u)=D_J/(beta-u)²+O(1),
    M(u)=Z'(u)/Z(u)=1/(beta-u)+O(1).

Los restos y sus derivadas provienen de integrales convergentes en una vecindad de beta después de separar la cola principal. Z(u)>0 en ese tramo. Para u1=beta-epsilon y u2=beta-2epsilon, ambos positivos si epsilon es suficientemente pequeña, el kernel K(u,v)=(M(u)+M(v))/(u+v) cumple

    epsilon [K(ui,uj)] -> (1/(2beta)) [[2,3/2],[3/2,1]],
    epsilon² det[K(ui,uj)] -> -1/(16beta²)<0.

Este cálculo hace explícito el fallo del criterio de dos puntos de001. LT-CANCEL se justifica aquí por los momentos absolutos finitos para 0<u,v<beta; la misma sustitución y cota triple de§8.4 son válidas en ese intervalo. Multiplicar la matriz K por los factores positivos Z(ui)Z(uj) conserva el signo negativo del determinante. Truncar los tests exponenciales y aproximar por sumas finitas produce un bloque negativo de A_[S_J].

S_J es holomorfa en |Im t|<pi/4. La cola en la integral de A_[S_J] decae exponencialmente en r, uniformemente en compactos del producto de strips, por(SJ-TAIL) y las expresiones finitas de§8.4. Por§2.2, A_[S_J] no es PSD en ningún intervalo real abierto no vacío.

La conclusión excluye esta simetrización para todos J>=1. No se afirma positividad puntual global de S_J; sólo su cola positiva, suficiente para el argumento. No afecta a la Phi completa, de supercola, ni a reparaciones que cambien estas colas. Sin cómputos nuevos, ampliaciónT o cambios en papers.

### 8.6. Pesos n^(-delta): incluso una amortiguación arbitrariamente débil falla

**PROVED para todo delta real distinto de0, revisión root/casos y deduplicación dirigida mapa.** Se conserva la suma infinita completa y todos sus cruces:

    phi_delta(t)=sum_(n>=1)n^(-delta)Phi_n(t).

El addendum de cortes suaves anterior sólo cubría esta familia para delta>3 mediante sum w_n n²<infinito. Aquí se elimina esa restricción, incluidos delta positivos arbitrariamente pequeños y delta negativos. No se asume paridad de phi_delta ni una cota gaussiana a izquierda; esas hipótesis no están disponibles en esta deformación.

**Transformada en su dominio absoluto.** Con h de§8 y Phi_n(t)=n^(-1/2)h(t+log n), sustitución y Fubini absoluto dan

    Z_delta(u)=C(u)(u-1/2)sum_(n>=1)n^(-u-1/2-delta),
    C(u)=(1/2)pi^(-u/2-1/4)Gamma(u/2+5/4),
    u>max(-5/2,1/2-delta).                            (DELTA-LT)

La integral absoluta del átomo h converge para u>-5/2; tras escalar, la serie absoluta tiene exactamente el peso n^(-u-1/2-delta). Para el primer momento absoluto se añade como mucho un factor 1+log n, que también suma estrictamente dentro del dominio. C(u)>0 para u>0. Por tanto la identidad LT-CANCEL de§8.4, demostrada por Fubini en la integral triple, es válida aquí para

    u,v>max(0,1/2-delta).

No se aplica el lema de§8.4 fuera de sus hipótesis de cola: se usa directamente su identidad integral, con los momentos absolutos que acabamos de justificar.

**Caso delta>0.** Cerca de u=1/2, H_delta(u)=C(u)sum n^(-u-1/2-delta) es positiva y C¹. Como Z_delta=(u-1/2)H_delta, hay puntos u<1/2 dentro del dominio donde Z_delta<0 y Z_delta'>0. Así Z_delta Z_delta'/u<0.

**Caso delta<0.** Poner c=1/2-delta>1/2. Para p>1 próximo a1,

    sum_(n>=1)n^(-p)=1/(p-1)+R(p),

con R y R' acotadas cerca de1. Esto se prueba sin información adicional sobre la serie: restar sum_n integral_n^(n+1)x^(-p)dx; la serie de diferencias y su derivada convergen uniformemente en una vecindad de p=1, por cotas O((1+log n)n^(-p-1)). Insertar p=u+1/2+delta en(DELTA-LT) da, cuando u baja a c desde arriba,

    Z_delta(u)=D/(u-c)+O(1),
    Z_delta'(u)=-D/(u-c)²+O(1),
    D=C(c)(-delta)>0.

De nuevo Z_delta Z_delta'/u<0 para u suficientemente próximo a c. El resto derivado es acotado porque C es suave y R es C¹; se conserva el término constante que resulta de expandir C(u)(u-1/2).

**Del test al kernel local.** En ambos casos LT da un test exponencial negativo para A_[phi_delta]. Convergencia absoluta permite truncarlo y pasar a una matriz finita negativa. La serie modal converge normalmente en compactos de |Im t|<pi/4 para cualquier delta real; su cola derecha es superexponencial uniformemente en esos compactos, pues exp(-b n²exp(2r)) absorbe cualquier potencia fija de n. La integral de A es conjuntamente holomorfa en el producto de strips. Por§2.2, A_[phi_delta] no es PSD en ningún intervalo real abierto no vacío.

**Discontinuidad del momento y alcance.** Para todo delta>0, Z_delta(1/2)=0; para delta=0, la cancelación del factor u-1/2 con el término 1/(u-1/2) de la serie da Z_Phi(1/2)=C(1/2)=1/4. Aunque phi_delta converge a Phi en compactos cuando delta tiende a0,

    integral_R exp(t/2)|phi_delta(t)-Phi(t)|dt>=1/4

para todo delta>0. Por tanto convergencia local y amortiguación débil de cada modo no conservan este momento. El caso delta=0 queda completamente fuera del descarte. No se prueba signo negativo de A_[Phi] o W, ni se excluyen otras regularizaciones que mantengan la compensación completa. No hay nuevos cálculos, coberturaT o modificaciones de papers.

### 8.7. Perturbaciones positivas, pares y analíticas con error relativo arbitrariamente pequeño

**PROVED, root/casos/theta_joint; cotejo dirigido mapa (2026-11-05).** Para todo epsilon>0 existe una densidad psi estrictamente positiva, par y holomorfa en |Im t|<pi/4, tal que

    sup_(t real) |psi(t)/Phi(t)-1| < epsilon,
    psi(t)/Phi(t) -> 1 cuando |t| -> infinito,

pero A_psi NO es PSD. De hecho falla PSD en todo intervalo real abierto no vacío. Se conservan las supercolas reales de Phi y cualquier número finito de términos de su expansión relativa en exp(-2|t|). No se conservan los momentos exactamente ni la estructura aritmética modal. Esto no decide el signo de A_Phi: demuestra que la cercanía relativa de densidades, incluso en esta clase regular, no garantiza el signo del kernel perturbado.

**Antecedente y diferencia.** §§8.1–8.3 ya descartan los prefijos Phi_M y establecen localidad de cola, pero sus aproximantes globales anteriores perdían positividad, paridad o las colas. La construcción siguiente conserva positividad y paridad, obtiene error RELATIVO uniforme y recupera analiticidad por mollificación de ese error, no de la densidad. La convolución aquí no se usa como operación preservante de signo.

**1. Reparación suave positiva.** Fijar chi par C∞, 0<=chi<=1, igual a0 en |t|<=1/2 y a1 en |t|>=1. Para t>=0, todos los modos Phi_n(t) son positivos. Con y=pi exp(2t)>=pi>3,

    Phi_n(t)/Phi_1(t)
      = n²(2n²y-3)/(2y-3) exp[-(n²-1)y]
      <=2n^4 exp[-pi(n²-1)].

Poner h_M(t)=chi(t) sum_(n>M)Phi_n(|t|)/Phi(t) y psi_M=Phi(1-h_M). Cerca de0 h_M es idénticamente cero, de modo que la reflexión no introduce pérdida de suavidad. Entonces h_M es par, suave, integrable y

    0<=h_M<=epsilon_M:=2 sum_(n>M)n^4 exp[-pi(n²-1)]
       <=4(M+1)^4 exp[-pi((M+1)²-1)] ->0.

La última cota usa que la razón sucesiva de los sumandos es a lo sumo16 exp(-3pi)<1/2. Para M grande, epsilon_M<1. La densidad psi_M es estrictamente positiva y par; coincide con Phi_M en t>=1. Por§8.1 y localidad de cola, hay nodos finitos t_i en(1,2) y coeficientes reales c_i con

    sum_ij c_i c_j A_(psi_M)(t_i,t_j)<0.

El tamaño del bloque puede depender de M y no se estima.

**2. Recuperar analiticidad sin perder el bloque negativo.** Sea gamma_sigma la gaussiana normalizada de varianza sigma² y g_sigma=h_M*gamma_sigma. En la recta, g_sigma es par y0<=g_sigma<=epsilon_M. Además es entera, pues para z=x+iy,

    |g_sigma(z)|<=epsilon_M exp[y²/(2sigma²)],

y las derivadas de la gaussiana justifican diferenciación uniforme en compactos. Como h_M pertenece a C0(R), g_sigma->h_M uniformemente cuando sigma baja a0. Definir

    psi_(M,sigma)=Phi(1-g_sigma).

Es positiva, par y holomorfa en el strip de Phi, con error relativo<=epsilon_M. Fijar el bloque negativo del paso1 ANTES de elegir sigma. Si delta_sigma=||g_sigma-h_M||_infinito, para esos nodos positivos

    |A_(psi_(M,sigma))(t_i,t_j)-A_(psi_M)(t_i,t_j)|
      <=2 delta_sigma A_Phi(t_i,t_j) ->0.

Esto sólo usa positividad puntual de Phi y de t_i+t_j+2r; NO supone PSD de A_Phi. La forma cuadrática negativa persiste para sigma suficientemente pequeño. Escogiendo primero M grande y luego sigma pequeño se obtiene el enunciado.

**3. Colas y alcance.** Para cada B>0, la razón modal de h_M satisface h_M(t)<=C_B exp(-B|t|). La convolución gaussiana conserva esa cota con otra constante, por la desigualdad |t-r|>=|t|-|r| y la integrabilidad de exp(B|r|)gamma_sigma(r). Así g_sigma=o(exp(-N|t|)) para cada N fijo, y psi_(M,sigma)/Phi->1 con todas las correcciones exponenciales finitas declaradas. No se conservan los términos modales de escala doble exponencial. En substrips fijos g_sigma está acotada por la cota compleja anterior; por tanto la integral de A_(psi_(M,sigma)) es conjuntamente holomorfa como en§2.2. Ese principio de continuación transporta su fallo PSD a cualquier intervalo abierto.

Al tomar M→infinito y escoger para cada M un sigma_M suficientemente pequeño como en el paso2, el error relativo también implica convergencia en L²(w(t)dt) para cada peso FIJO con integral w Phi² finita, incluidos pesos exponenciales y gaussianos. No se afirma cercanía uniforme en una norma de strip complejo o de todos los jets: las constantes complejas pueden crecer cuando sigma disminuye. Tampoco se imponen las desigualdades adicionales073/077/112 ni momentos exactos. El resultado excluye una garantía de positividad basada únicamente en error relativo pequeño, paridad, positividad de la densidad y estas colas. No excluye una comparación firmada en norma de formas ni un uso de la estructura theta exacta. Sin nuevas evaluaciones numéricas, signo W/T ni modificaciones de papers.

### 8.8. Se puede conservar cualquier familia finita de momentos independientes

**PROVED, construcción root y revisión independiente casos; cotejo dirigido mapa (2026-11-05).** Se fortalece§8.7: fijar pesos reales pares continuos w_1,...,w_d, linealmente independientes al restringirlos a(-1,1), tales que integral Phi|w_i| sea finita. Para todo epsilon>0 existe psi con todas las propiedades de§8.7 y A_psi no PSD, que además cumple EXACTAMENTE

    integral_R w_i(t)psi(t)dt = integral_R w_i(t)Phi(t)dt, i=1,...,d.

Los pesos y su número se fijan ANTES de elegir el aproximante. Las constantes de construcción dependen de esa familia. Por ejemplo se pueden preservar normalización, una lista finita de momentos polinomiales pares y valores/derivadas de la transformada en una lista finita de parámetros, tomando una base de los pesos analíticos correspondientes. No se exige ni se obtiene preservación de una familia infinita.

**1. Corrección suave sin alterar la cola que contiene el test negativo.** Definir L_i(f)=integral Phi(t)w_i(t)f(t)dt. Es un funcional continuo para la norma uniforme, con constante integral Phi|w_i|. Existen funciones pares suaves b_1,...,b_d, compactamente soportadas en(-1,1), para las cuales la matriz B_ij=L_i(b_j) es invertible. En efecto, por independencia se pueden elegir x_j en(0,1) con matriz [w_i(x_j)] invertible; si no, los vectores de evaluación generarían un subespacio propio y habría una combinación de los w_i idénticamente nula. Bumps pares alrededor de ±x_j, normalizados con Phi, aproximan esa matriz y conservan su invertibilidad.

Usar h_M de§8.7, d_(M,i)=L_i(h_M), a_M=B^(-1)d_M y

    p_M=-h_M+sum_j a_(M,j)b_j.

Entonces L_i(p_M)=0, ||p_M||_infinito<=C_w epsilon_M→0 y p_M=-h_M para |t|>=1. La densidad Phi(1+p_M) es positiva para M grande y coincide con Phi_M en t>=1. Tiene por tanto un bloque finito negativo de A, con nodos en(1,2). Elegir primero M de modo que ||p_M||<min(epsilon/4,1/4), y fijar ese bloque. La corrección es firmada; no se presupone que los a_j tengan un solo signo.

**2. Analiticidad y momentos exactos simultáneamente.** Mollificar por la misma gaussiana:

    p_(M,sigma)=p_M*gamma_sigma,
    b_(j,sigma)=b_j*gamma_sigma,
    B_(sigma,ij)=L_i(b_(j,sigma)),
    r_(sigma,i)=L_i(p_(M,sigma)).

La convergencia uniforme de las aproximaciones de la identidad y continuidad de L_i implican B_sigma→B y r_sigma→0. Para sigma pequeño B_sigma es invertible. Poner

    c_sigma=-B_sigma^(-1)r_sigma,
    q_sigma=p_(M,sigma)+sum_j c_(sigma,j)b_(j,sigma),
    psi=Phi(1+q_sigma).

Se tiene L_i(q_sigma)=0 EXACTAMENTE, c_sigma→0 y q_sigma→p_M uniformemente. Por tanto, al disminuir sigma, psi sigue siendo positiva y su error relativo es menor que epsilon. Para el bloque fijado, si ||p_M|| y ||q_sigma|| son <=1/2, la diferencia de entradas de A está acotada por 3||q_sigma-p_M||_infinito A_Phi(t_i,t_j); así persiste su forma cuadrática negativa. El factor2 de§8.7 no se reutiliza, pues ahora las correcciones pueden tener ambos signos. Las convoluciones son enteras y pares como en§8.7, incluso para p_M firmado usando su norma absoluta en las cotas. También decaen más rápido que cualquier exponencial fija, de modo que se conservan el cociente de colas y las expansiones relativas declaradas allí. La holomorfía de A y su fallo en cualquier intervalo se justifican como en§8.7.

**Consecuencia para comprobaciones finitas del kernel.** Dados parámetros positivos distintos u_1,...,u_m, tomar como pesos cosh(u_i t) y t sinh(u_i t). Son funciones pares analíticas linealmente independientes: una combinación nula sería una suma de exponenciales con prefactores lineales; ordenar los u_i y enviar t a infinito elimina sucesivamente ambos coeficientes del mayor exponente. Para densidades pares estos momentos son precisamente Z(u_i) y Z'(u_i). Así psi puede tener EXACTAMENTE los mismos valores de

    K(u_i,u_j)=[Z'(u_i)/Z(u_i)+Z'(u_j)/Z(u_j)]/(u_i+u_j)

que Phi en cualquier colección FINITA de bloques previamente elegidos, y sin embargo A_psi no ser PSD. Bajo las colas de§8.7, el puente§2.1 también implica fallo de K_psi en algún otro bloque. No se ha dado un contraejemplo a K_Phi. Este argumento por sí solo no garantiza preservar las familias infinitas de dos, tres o cuatro generadores. El control adicional de§8.9 sí conserva hasta cuatro en el dominio admisible.

Esto va más allá del contramodelo abstracto de018 y de§8.7: aquí hay una densidad positiva, par y analítica arbitrariamente cercana a Phi con datos finitos exactos y colas compatibles. No se conserva la identidad theta completa, el peine aritmético ni todas las desigualdades estructurales073/077/112. No se concluye que todo método basado en identidades exactas sea imposible. Se excluye una garantía universal basada sólo en esos datos finitos, cercanía relativa y regularidad. Sin nuevos cálculos, signo W/T ni cambios en papers.

### 8.9. Estabilidad de TODOS los bloques admisibles de orden hasta cuatro

**PROVED, construcción preservador/root, auditoría independiente casos y cotejo dirigido mapa (2026-11-05).** Se utilizan los resultados certificados084/085; no se ejecutaron nuevos cálculos. Definir

    ||h||_20=sup_(t real) exp(20|t|)|h(t)|.

Existe delta_*>0 tal que toda densidad par positiva psi=Phi(1+h) con ||h||_20<delta_* tiene K_psi PD en TODOS los bloques de hasta cuatro nodos distintos u_i>1/2. Las repeticiones se agrupan y dan PSD. El umbral es existencial, no un nuevo valor certificado.

La diferencia frente§8.8 es un control uniforme de los jets de Z que entran en los numeradores escalares085, incluso cuando los nodos confluyen o escapan. No se supone un margen uniforme de autovalores de las matrices.

**1. Error ponderado y jets.** Poner delta=||h||_20<=1/2 y Delta Z=Z_psi-Z_Phi. Para j<=4, usar |t|^j<=C_j exp(4|t|). Para u grande,

    |Delta Z^(j)(u)|
      <=C_j delta integral Phi(t)exp(ut-16|t|)dt
      <=C_j delta Z_Phi(u-16).

La última desigualdad también vale para t<0. El lower M_Phi(s)>=(1/2)log s-C de084 implica, desde un U fijo suficientemente grande (puede elegirse U>256),

    Z_Phi(u-16)/Z_Phi(u)
      =exp[-integral_(u-16)^u M_Phi(s)ds] <=C u^-8.

Las fórmulas aritméticas084 de M y sus primeras tres derivadas dan Z_Phi^(j)/Z_Phi=O((1+log u)^j), j<=4, mediante las identidades de derivación exponencial. Además 1-delta<=Z_psi/Z_Phi<=1+delta. Aplicar las fórmulas de derivadas logarítmicas hasta orden4 da

    |M_psi^(k)-M_Phi^(k)|
       <=C delta u^-8(1+log u)^4, k=0,...,3.

No se deriva una notación O: se estiman las expresiones algebraicas de los jets. Las constantes son independientes de h para delta<=1/2. En cada compacto u∈[1/2,U], la continuidad de los mismos jets, con cota lineal en delta, sigue de integrabilidad de Phi(t)|t|^j exp(U|t|).

**2. Numeradores estrictos.** Para c=M, D=uM', E=u²M'', F=u³M''',085 define

    N_R=3c²+c(-6D-6E-2F)+3D²+6DE+2DF-3E²,
    N_S=3c²+c(6D+6E+2F)-9D²-6DE+2DF-3E².

Son polinomios cuadráticos. El paso1 y c=O(log u), D,E,F=O(1) para Phi implican

    |Delta N_R|+|Delta N_S|
        <=C delta u^-5(1+log u)^5

para u>=U.084 prueba N_R>1/4 y N_S>19/4 para Phi en u>=127.5. En [1/2,U],085 junto con084 da mínimos estrictamente positivos. Elegir delta_* suficientemente pequeño preserva ambos signos para TODO u>=1/2.

**3. Signos inferiores sin asumir073 para psi.** Para x=u², poner R=u/M_psi(u), S=uM_psi(u). Por positividad y paridad, M_psi(u)>0 para u>0. Las identidades084 dan

    T_R=2R'R'''-3(R'')²=N_R/(16M_psi^4 u^6)>0,
    T_S=2S'S'''-3(S'')²=N_S/(16u^6)>0,

con derivadas en x. Las asintóticas heredadas son M_psi=(1/2)log(u/(2pi))+O(1/u), uM_psi'→1/2 y u²M_psi''→-1/2. De ellas, R',S'>0 en la cola y R'',S''→0. T_f>0 impide f'=0, por lo que el signo positivo de la cola se conserva en todo x>=1/4. Entonces f'''>0; como f'' crece estrictamente hacia0, es negativa.

No se invoca BASE073 ni se supone M_psi''<0. Los Pfaffianos de dos nodos083 son positivos por crecimiento; los de tres son -det[1,x_i,f(x_i)]/producto_(i<j)(u_i+u_j), positivos por concavidad estricta. Para cuatro aplica Rolle084 con f'>0,f''<0,T_f>0.083 y Sylvester dan todos los bloques PD de órdenes<=4.

**4. Aplicación a los aproximantes negativos.** En el soporte activo del cutoff de§8.7, |t|>=1/2. Para n>=2, la función exp[20t-pi(n²-1)exp(2t)] decrece desde1/2. Por tanto

    ||h_M||_20
      <=2 exp(10) sum_(n>M)n^4 exp[-pi e(n²-1)] ->0.

Las correcciones compactas de momentos de§8.8 tienen norma20 finita y coeficientes que tienden a0. La mollificación cumple

    ||p*gamma_sigma||_20
      <=E exp(20|G_sigma|)||p||_20
      <=2 exp(200)||p||_20, 0<sigma<=1.

También converge a p en esta norma cuando exp(20|t|)p(t) pertenece a C0: las traslaciones son continuas en norma20, y el mayorante exp(20|r|) controla la integral gaussiana. Tanto p_M como los bumps de§8.8 cumplen esa condición. Así las correcciones posteriores de momentos, con coeficientes que tienden a0, permiten q_sigma→p_M en norma20. Elegir primero M grande y luego sigma pequeño impone simultáneamente la vecindad delta_*, los momentos exactos, cualquier precisión relativa deseada y la persistencia del bloque negativo fijado.

**Conclusión.** Existen densidades positivas, pares y analíticas, arbitrariamente próximas a Phi en norma relativa ponderada20, que conservan TODOS los bloques admisibles de hasta cuatro generadores, cualquier familia finita de momentos de§8.8 y las colas de§8.7, pero cuyo A y K completo NO son PSD. Por§2.1 existe un bloque negativo de K con u>1/2; necesariamente tiene más de cuatro nodos distintos.

No se conserva la identidad aritmética theta, ni se refuta K_Phi. El argumento de§8.9 por sí solo no garantiza preservar TODOS los trece generadores de053; ese punto se trata en§8.10. No se afirma preservar las desigualdades077/112. Esta conclusión distingue claramente los cuatro órdenes continuos de la obligación global: ni esos órdenes, ni esta proximidad y los datos finitos exactos, la fuerzan por sí solos en la clase declarada. No es una ampliación del signo real ni de T. Papers intactos.

### 8.10. Control relativo uniforme y conservación de los trece polos altos

**PROVED, construcción root/preservador, auditoría independiente casos y cotejo dirigido de antecedentes mapa (2026-11-05).** El lema siguiente controla la forma relativa a la Gram de Cauchy, no sólo sus entradas. Evita un bound que degenere cuando los nodos confluyen o se separan mucho.

**Lema de interpolación contractiva.** Fijar a>0 y n. Sea mu real suave en[a,infinito), tal que

    F(z)=mu(a(1+z)/(1-z))

se extienda a C^(n-1)[0,1]. Para cualquier conjunto de hasta n tasas u_i>=a y coeficientes complejos c_i,

    |sum_ij c_i conjugado(c_j)[mu(u_i)+mu(u_j)]/(u_i+u_j)|
      <=2 B_n sum_ij c_i conjugado(c_j)/(u_i+u_j),
    B_n=sum_(j=0)^(n-1) (2^j/j!) ||F^(j)||_infinito.

La misma cota vale para los límites confluyentes, interpretados como derivadas paramétricas del kernel y exponenciales por polinomios.

Prueba. En E=span{exp(-u_i r)}, con la norma L²(0,infinito), A=-D_r conserva E y

    2 Re<Af,f>=|f(0)|²>=0.

A+a es invertible. La identidad

    ||(A+a)v||²-||(A-a)v||²=4a Re<Av,v>>=0

hace Q=(A-a)(A+a)^(-1) una contracción. Sus autovalores z_i=(u_i-a)/(u_i+a) pertenecen a[0,1). Interpolar F mediante Newton: los coeficientes de diferencias divididas de orden j están acotados por ||F^(j)||/j!, y cada factor Q-z_iI tiene norma<=2. Por ello el polinomio interpolante P, de grado<=n-1, cumple ||P(Q)||<=B_n. Además P(Q)exp(-u_i r)=mu(u_i)exp(-u_i r). Para f=sum c_i exp(-u_i r), la forma de la izquierda es 2Re<P(Q)f,f>, mientras la Gram de la derecha es ||f||². Esto demuestra la cota sin suponer que mu sea holomorfa en toda una semirrecta compleja. Repetir nodos se trata por interpolación de Hermite o límites de diferencias finitas; la constante es uniforme y las tasas pueden confluir unilateralmente en a. Así quedan incluidos todos los numeradores de los espacios racionales correspondientes.

**Aplicación a mu=M_psi-M_Phi.** Escribir psi=Phi(1+h), par positiva, y delta=||h||_100=sup exp(100|t|)|h(t)|<=1/2. Para j<=13, |t|^j<=C_j exp(4|t|), por lo que

    |Delta Z^(j)(u)|/Z_Phi(u)
      <=C_j delta Z_Phi(u-96)/Z_Phi(u)
      <=C_j' delta u^-48

para u suficientemente grande. La segunda cota procede de integrar el lower M_Phi(s)>=(1/2)log s-C de084 sobre[u-96,u]. En compactos todos esos momentos tienen cotas lineales en delta.

Para controlar los momentos normalizados de Phi sin necesitar fórmulas aritméticas de orden13, poner alpha=1/log u. El upper M_Phi(s)=O(log u) en[u-alpha,u+alpha] da

    E_u exp(alpha|t|)
       <=[Z_Phi(u+alpha)+Z_Phi(u-alpha)]/Z_Phi(u)<=C.

Por tanto E_u|t|^j<=C j!(log u)^j. Las fórmulas algebraicas de derivación logarítmica hasta orden13 y Z_psi/Z_Phi∈[1/2,3/2] implican

    |Delta M^(k)(u)|
       <=C delta u^-48(1+log u)^13, k=0,...,12.

No se derivan restos asintóticos. Fijar a=63/2. En las derivadas hasta orden12 de F(z)=Delta M(a(1+z)/(1-z)), la regla de la cadena introduce a lo sumo factores C_a u^24. Así todas esas derivadas tienden a0 al llegar a z=1, se extienden continuamente y

    ||F||_(C12[0,1])<=C delta.

El lema con n=13 prueba, para TODAS las tasas u_i>=63/2, con multiplicidades permitidas,

    |Q_psi[f]-Q_Phi[f]|<=C_13 delta ||f||².

Aquí Q_psi se DEFINE por el kernel K_psi y sus límites confluyentes. Para Phi, CONE001§1 identifica Q_Phi exactamente con la forma W sobre esas exponenciales; sus coeficientes temporales incluyen las congruencias correspondientes cuando se parte de los datos rho. No se está atribuyendo a psi una identidad aritmética de Weil no demostrada.

FULL_THIRTEEN053 prueba W[f]>||f||²/4000 para todos los trece polos>=63/2 y numeradores de grado<13. Elegir delta suficientemente pequeño para C_13 delta<1/8000 da

    Q_psi[f]>||f||²/8000

en TODA esa familia. Es una consecuencia analítica del certificado existente, sin nuevas verificaciones numéricas. No se calcula un delta efectivo.

**Compatibilidad con los aproximantes negativos.** Para M suficientemente grande, la misma monotonía usada en§8.9 da

    ||h_M||_100
      <=2 exp(50) sum_(n>M)n^4 exp[-pi e(n²-1)] ->0.

Las correcciones compactas de momentos tienen norma100 finita y coeficientes que tienden a0. Para sigma<=1, la convolución gaussiana tiene norma ponderada a lo sumo2 exp(5000); también aproxima la identidad para las funciones usadas, pues exp(100|t|)p_M(t) pertenece a C0. Por tanto§8.8 puede realizarse con norma100 arbitrariamente pequeña, sin perder momentos exactos ni el bloque negativo fijado. Como ||h||_20<=||h||_100, también se conserva la conclusión global de orden4 de§8.9.

En consecuencia, hay aproximantes positivos, pares y analíticos, arbitrariamente cercanos a Phi, que conservan simultáneamente TODOS los bloques admisibles de hasta cuatro generadores, TODOS los trece polos de tasas>=63/2 (incluso confluyentes), los momentos finitos preasignados y las colas de§8.7, y aun así NO tienen kernel global PSD. Por§2.1 hay un bloque negativo en cualquier intervalo abierto de tasas contenido en(63/2,infinito); tiene necesariamente más de trece nodos distintos.

No se conserva la identidad theta aritmética completa, ni se refuta K_Phi. Tampoco se conserva por este argumento una familia de dimensiones sin cota: B_n y la regularidad ponderada requerida dependen de n. El lema sí aporta una herramienta de control uniforme a dimensión fija; no un cierre global ni una ampliación de T. Papers intactos.

### 8.11. Ningún margen positivo de Cauchy puede ser uniforme en todos los órdenes

**PROVED, root/casos/preservador; cotejo dirigido mapa (2026-11-06).** Corolario del principio de continuación de§2.2. Sea M real analítica en(0,infinito), con M(u)=O(u) cuando u baja a0. Para cualquier c>0 y cualquier intervalo abierto no vacío I contenido en(0,infinito), el kernel

    F_c(u,v)=[M(u)+M(v)-c]/(u+v)
            =K_M(u,v)-c G(u,v), G(u,v)=1/(u+v),

NO es PSD en todos los conjuntos finitos de nodos de I. No se supone que K_M sea PSD.

**Prueba.** Suponga PSD en I. En cada compacto positivo, la analiticidad real de M da una prolongación holomorfa a un vecindario complejo; el denominador u+v tampoco se anula en vecindarios suficientemente pequeños. El argumento de matrices mixtas de evaluaciones y jets de§2.2, seguido de Taylor, permite propagar PSD desde I hasta cualquier punto positivo a lo largo de un compacto que los conecte. Los radios se eligen uniformes en ese compacto; no se intenta llegar a0 con radio fijo. Para un u*>0 suficientemente pequeño, sin embargo,

    F_c(u*,u*)=M(u*)/u*-c/(2u*)<0,

pues el primer término está acotado. Esta diagonal negativa contradice la positividad propagada.

Para la Phi real, Z(u)>0 en la recta y sus momentos exponenciales son finitos; M=Z'/Z es real analítica y, por paridad,

    M(u)=[integral t²Phi(t)dt / integral Phi(t)dt] u+O(u³).

Por tanto el corolario se aplica al kernel REAL completo. También se aplica al modelo hiperbólico par. En la norma de exponenciales de§8.10, significa que para todo c>0 y todo I admisible existen una combinación finita no nula f con tasas en I y un bloque tales que Q_Phi[f]<c||f||². No se afirma que ese valor sea negativo ni que tenga una cota inferior ya probada. Si además se demostrase PSD global, el ínfimo de esos cocientes sería exactamente0.

**Consecuencia para el programa.** El margen1/4000 de053 y el margen estable de§8.10 no pueden extenderse con una constante positiva fija a dimensión arbitraria, incluso si todas las tasas quedan en un intervalo alto. Si I está dentro de(63/2,infinito) y c<1/4000, el test del corolario necesariamente necesita más de trece tasas distintas: los órdenes inferiores tienen el margen053. Esto no refuta el objetivo de no negatividad sin margen, ni los teoremas a dimensión fija.

La revisión del cálculo funcional tampoco permite desplazar gratuitamente el semiplano: aunque las tasas u_i sean>=a, A-a no es accretivo en general. Para f(r)=exp(-ar)-exp(-br), b>a, se tiene f(0)=0 y Re<(A-a)f,f>=-a||f||²<0. Por ello controlar una función sólo en Re u>=a no autoriza aplicar una cota de contracciones al Cayley de A-a. Una cota absoluta dimension-free de error, aun si existiese, tampoco aporta por sí sola la compensación relativa a un modelo sin margen uniforme. No se ha construido tal compensación; no nueva positividad W/T ni cambios en papers.


## 9. Positividad estricta de todos los pares temporales por convexidad en los cuadrados

**PROVED**, root; auditoría matemática independiente arithmetic_fresh_candidate PASS. Cotejo dirigido diagonal_gauge_dedup sin antecedente literal localizado en índices y primarias consultadas, no exhaustivo ni afirmación de prioridad mundial. Se combinan V'''(x)>0, x>0, probada para la theta completa en POWER_THETA_TWO_COPY_073 y sus certificados, y SLICE de§3. No se atribuye novedad al principio elemental de convexidad. No es el teorema de pares de potencias073: los nodos aquí son variables temporales reales arbitrarias.

Sea V=-logPhi, par y real-analítica. Para x>0,

    xV''(x)-V'(x)=integral_0^x rV'''(r)dr>0.

La constante en0 es cero por paridad. Para G(u)=V(sqrt(u)), u>=0,

    G''(u)=[sqrt(u)V''(sqrt(u))-V'(sqrt(u))]/(4u^(3/2))>0

cuando u>0. La analiticidad par de V permite extender G regularmente a0. Así G es estrictamente convexa en[0,infinito); no se necesita asumir V''(0)>0.

Fijar t!=s reales y v>0. Poner m=(t+s)/2, delta=(t-s)/2 y

    a=sqrt(m²+v)+delta, b=sqrt(m²+v)-delta,
    x=t²+v, y=s²+v.

Entonces a²+b²=x+y, mientras

    |a²-b²|=4|delta|sqrt(m²+v)>4|delta*m|=|x-y|.

Todos estos cuadrados son no negativos, incluso cuando a o b sea negativo. Para una suma fija S, la función G(S/2+r)+G(S/2-r) crece estrictamente con r>=0 dentro de su dominio: su derivada es G'(S/2+r)-G'(S/2-r)>0 para r>0. Por tanto

    V(a)+V(b)=G(a²)+G(b²)>G(t²+v)+G(s²+v).

Usando SLICE y las diagonales S_v(t,t)=Phi(sqrt(t²+v))² se obtiene

    S_v(t,s)^2<S_v(t,t)S_v(s,s), v>0,t!=s.          (PAIR-SLICE)

Las diagonales son estrictamente positivas, luego toda matriz de dos nodos distintos de S_v es definida positiva. Para v=0, S_0(t,s)=Phi(t)Phi(s), y la matriz es sólo semidefinida positiva de rango uno.

Para cualquier vector no nulo c de dos coeficientes, c* S_v c>0 para TODO v>0. Integrar la forma cuadrática usando A=integral S_v dv y la integrabilidad de entradas ya demostrada en§2 prueba

    [A(t_i,t_j)]_(i,j=1,2) es definida positiva si t_1!=t_2.

En particular 0<A(t,s)<sqrt(A(t,t)A(s,s)) para todo par real distinto. No se deduce esta conclusión únicamente de positividad de entradas.

**Alcance y patrón exacto.** Las capas en la variable v son PSD en todos los bloques de tamaño uno y dos, pero§5 ya demuestra que una capa theta real tiene un bloque de tres nodos positivos no PSD. Tres es por tanto el tamaño mínimo posible de un falsificador de ESA descomposición por capas. Las capas crudas en r de§2.3 son otro objeto y sí fallan en tamaño dos; no hay contradicción. El integral A tiene todos sus pares positivos, pero su signo a todos los órdenes sigue OPEN: integrar capas indefinidas puede compensarlas, sin una cota conjunta probada. No hay nueva cobertura W ni ampliación de T; el puente global no permite identificar tamaños finitos entre los dos kernels. Sin nuevos cálculos ni cambios en papers.


## 10. Compensación real demostrada en triples temporales simétricos

**PROVED**, root; auditoría matemática arithmetic_fresh_candidate PASS; cotejo dirigido diagonal_gauge_dedup sin antecedente literal localizado en índices y primarias. Se usan073 y§§4.3,5,9; no se presenta como nuevo el principio de que una integral puede compensar capas indefinidas. La diferencia es probar AMBOS signos para la theta real en LOS MISMOS nodos (-R,0,R). El refinamiento analítico siguiente fija R>=8 tanto para la positividad del integral como para la existencia de capas inicialmente negativas; no cuantifica su intervalo v_R ni afirma uniformidad en R. Sin cambios en papers.

**Positividad del integral completo.** Por simetría y paridad conjunta, su matriz es

    [[d,c,b],[c,d0,c],[b,c,d]],
    d=A(R,R), d0=A(0,0), b=A(-R,R), c=A(R,0).

Todos son positivos. En el sector antisimétrico, el autovalor es d-b>0 por§9. En la base ortonormal del sector simétrico, el bloque es [[d+b,sqrt(2)c],[sqrt(2)c,d0]]. Basta probar c²/d->0.

Poner Y=pi exp(2R), P=Phi(R) y B=sup_(x real)Phi(x)<infinito. La expansión theta completa da p(x)=-Phi'(x)/Phi(x)>=pi exp(2x) para x suficientemente grande. Así, para R grande y r>=0,

    Phi(R+r)<=P exp(-Yr).

La fórmula de A y la cota Phi(r)<=B implican

    0<c<=BP integral_0^infinito (R+2r)exp(-Yr)dr
         =BP(R/Y+2/Y²).

Por§4.3, d/P²~R/(2Y), de modo que d>=RP²/(4Y) eventualmente. Por tanto

    c²/d<=4B²(Y/R)(R/Y+2/Y²)²->0.

Como d0 es constante positiva y b>0, para R grande se cumple d0(d+b)>2c². Ambos sectores son definidos positivos: toda la matriz de tres nodos es SPD. Este argumento sólo usa bounds de cola y la positividad de pares; no necesita una asintótica diferenciada del cruce c.

**Refinamiento del mismo resultado: el integral es SPD para TODO R>=8.** No se abre otra ruta ni se usa un barrido. Por§12, p>0 en la semirrecta, luego B=sup Phi=Phi(0). Para f(x)=x(2x-3)exp(-x), f'(x)=(-2x²+7x-3)exp(-x)<0 si x>3. Como pi>3 y exp(3)>20 (Taylor racional positivo, también usado en088),

    B=sum_(n>=1)f(pi n²)
      <18 sum_(n>=1)n^4/20^(n²)<=450/499<1.

La razón consecutiva del majorante es<=16/20³=1/500. Se incluyen todos los modos.

Para R>=1,088 da p(R+r)>2Y_r-6>=Y_r>=Y, con Y_r=Y exp(2r)>21. Así la cota anterior c<=BP(R/Y+2/Y²) vale ya en toda esa región. Para obtener una cota inferior explícita de d, restringir su integral a0<=r<=1/(4Y). Allí

    p(R+r)<2Y exp(1/(2Y))+1<3Y.

La última desigualdad sigue de exp(x)<=1/(1-x), 0<=x<1, y Y>21. Por tanto Phi(R+r)>=P exp(-3Yr), y

    d>=2R P² integral_0^(1/(4Y)) exp(-6Yr)dr
      =R P²[1-exp(-3/2)]/(3Y)>R P²/(4Y),

pues exp(3/2)>4 por su Taylor positivo hasta grado3.

En0<=r<=1/16 todos los modos theta son positivos y Phi>=Phi_1>9/256: en efecto pi>3, 2pi exp(2r)-3>3, pi exp(2r)<4exp(1/8)<5 y exp(5)<256, usando exp(1/8)<8/7 y e<3. Luego

    d0=integral_0^infinito 2r Phi(r)²dr>81/2^24.

Si RY>=40, las cotas de c y d implican

    2c²/d<8B²(R/Y)[1+2/(RY)]²<9B²R/Y<=9R/Y.

Para TODO R>=8 se cumple RY>40; además R/Y decrece para R>=8. Usando pi>3 y exp(2)>7,

    9R/Y<=72/[pi exp(16)]<24/7^8<81/2^24<d0.

La comparación racional central equivale a402653184<466948881. Se obtiene 2c²<d0*d<d0(d+b), y d-b>0 por§9. Ambos sectores son por tanto SPD para TODO R>=8. No se cubren triples arbitrarios, R intermedios o todos los órdenes.

**Capas inicialmente negativas en esos mismos nodos.** Normalizar B_v(t,s)=S_v(t,s)/(Phi(t)Phi(s)). Aquí B_0 es el kernel constante1. Para p=V' impar analítica,

    partial_v B_v(t,s)|_(v=0)=-(p(t)+p(s))/(t+s).

Los valores removibles son -p'(R) en(-R,R) y -p'(0) en(0,0). Se justifican también expandiendo V(R+sqrt(v))+V(R-sqrt(v)) y 2V(sqrt(v)); la paridad elimina las potencias impares de sqrt(v).

Para eta=(1,-2,1), de suma cero, el cálculo en(-R,0,R) da

    eta^T B_v eta=-v Q_R+o(v),
    Q_R=2p'(R)-6p(R)/R+4p'(0).

Las cotas completas de088 dan p'(R)>4Y-1 y p(R)<2Y+1 para R>=1;§12 prueba p'(0)>0. Así, para TODO R>=8,

    Q_R>(8-12/R)Y-2-6/R+4p'(0)
       >(13/2)Y-11/4>0.

Para cada R>=8, eta^T B_v eta<0 cuando v>0 es suficientemente pequeño. El vector en la capa original es

    w_R=(1/P,-2/Phi(0),1/P),
    w_R^T S_v w_R<0 para 0<v<v_R

con algún v_R>0; no se afirma uniformidad en R de ese intervalo.

**Compensación efectiva, alcance limitado.** Para TODO R>=8 y ese mismo vector w_R, la positividad del bloque integral demuestra

    integral_0^infinito w_R^T S_v w_R dv=w_R^T A w_R>0,

aunque el integrando es negativo en(0,v_R). Las entradas son integrables, así que la parte positiva fuera de ese intervalo supera estrictamente su pérdida. Es una desigualdad conjunta probada para esta familia concreta, no una cota de compensación uniforme sobre todos los nodos, tamaños o vectores. No son triples de potencias080; son triples temporales. No se deduce positividad global, ampliación W/T ni una inducción en dimensión. Sin cálculos numéricos.


## 11. La expansión de Andréief completamente emparejada conserva signos negativos

**PROVED**, positive_identity_attempt/root; auditoría independiente arithmetic_fresh_candidate PASS; cotejo dirigido diagonal_gauge_dedup sin duplicado literal localizado en índices y primarias, sin afirmación exhaustiva ni de prioridad mundial. Se prueba una limitación puntual de la expansión siguiente, no el signo negativo de su integral. La diferencia frente§2.3 es agrupar las ocho elecciones del determinante completo de orden tres, antes de pedir signo, en lugar de pedir PSD de cada capa cruda.

Fijar tres nodos temporales distintos t1<t2<t3, positivos, y definir vectores columna

    f_i(r)=Phi(t_i+r), g_i(r)=(t_i+r)Phi(t_i+r),
    u_0=f, u_1=g.

Entonces A_ij=integral_0^infinito[g_i(r)f_j(r)+f_i(r)g_j(r)]dr. Andréief en el espacio producto (0,infinito) times {0,1}, con medida Lebesgue y conteo, da exactamente

    det[A_ij]=(1/6)integral_(0,infinito)^3 S(r1,r2,r3)dr1dr2dr3,
    S=sum_(epsilon in {0,1}^3)
       det[u_(epsilon_j)(r_j)] det[u_(1-epsilon_j)(r_j)].

Todos los intercambios son absolutamente convergentes por las supercolas de Phi y el crecimiento lineal añadido en g. El principio de Andréief es clásico; no se atribuye novedad a esta identidad.

Poner r1=r2=r>0, r3=r+h. Las elecciones con epsilon1=epsilon2 se anulan; las otras cuatro dan

    S(r,r,r+h)=-4 det[g(r),f(r),f(r+h)]
                    times det[g(r),f(r),g(r+h)].

Sean x_i=t_i+r y p=-Phi'/Phi. Puesto que f'=-pf y g'=(1-xp)f, Taylor y las diferencias divididas dan

    det[g,f,f_h]=h C p[x1,x2,x3]+O(h²),
    det[g,f,g_h]=h C (xp)[x1,x2,x3]+O(h²),
    C=product_i Phi(x_i) product_(i<j)(x_j-x_i)>0.

Los signos se comprueban por det[x,1,-p]=det[1,x,p] y det[x,1,1-xp]=det[1,x,xp]. Elegir r suficientemente grande: las expansiones diferenciadas theta completas prueban p''>0 y (xp)''=2p'+xp''>0 en el intervalo que contiene los tres x_i. Ambas diferencias divididas son entonces positivas. Para h>0 suficientemente pequeño se obtiene S(r,r,r+h)<0. Aunque r1=r2 es un conjunto de medida cero, continuidad y r>0 permiten perturbar hasta una región ABIERTA con 0<r1<r2<r3 donde S<0.

**Alcance.** Queda refutada únicamente la positividad puntual de ESTE integrando, incluso después de sumar todas sus elecciones. No se prueba det A negativo ni se excluye compensación entre regiones de integración, otro emparejamiento no local o un Gram distinto. No se promueve una identidad de determinantes a una desigualdad. El intento no produce nueva positividad W/T; sin cálculos ni cambios en papers.


## 12. Recíproco del potencial: criterio de momentos y cola explícita

**PROVED como identidad, implicación suficiente, cota exterior y cierre compacto por certificado Arb.** Constructor positive_identity_attempt/root; auditoría independiente arithmetic_fresh_candidate PASS (identidad con bordes, cola y revisión estática del certificado compacto); reproducción independiente root FULL PASS, exit0 y mismo SHA256. Consulta dirigida previa de índices, grid, crucigrama y073/086/088/103_43. El objeto es p(r)=V'(r), NO M=Z'/Z: la concavidad de sqrt(lambda)/M(sqrt(lambda)) de086 no prueba la condición siguiente. No se afirma prioridad mundial.

Poner u=r², G(u)=V(sqrt(u)), a(u)=2G'(u)=p(r)/r, w=exp(-2G), y E la esperanza de densidad w/integral(w). Sean H=integral_0^infinito r Phi², J=integral r(Phi')², K=integral r(Phi'')². Entonces integral(w)=2H y

    J/H=E[u a²]=E[a+u a'],
    K/H=E[(u a²-a-2u a')²],
    (HK-J²)/H²=Var(a+u a')+E[u²(2a'²-a a'')].

La última identidad resulta de integrar por partes con ua, u²a³ y u²aa'. En cero, a es regular por analiticidad par y los factores u,u² anulan los bordes. En infinito, las supercolas theta y las expansiones diferenciadas justifican integrabilidad y desaparición de los bordes. No se omite un término de borde de la integración original en r.

Si a>0 y (1/a)''>=0 en TODA la semirrecta, entonces 2a'²-aa''=a³(1/a)''>=0 y HK>=J². La igualdad obligaría a a+ua' constante; regularidad en cero fuerza a constante. Para la theta, a'>0 por§9; el certificado compacto siguiente completa además la condición global estricta.

**Cola explícita probada.** Escribir q(u)=1/a(u)=r/p(r). Derivación directa da

    q''(u)=N/(4r³p³),
    N=2r²p'²-r²pp''-rpp'-p².

Para r>=1, Y=pi exp(2r)>21. El primer modo satisface

    p1=2Y-9/2-6/(2Y-3),
    p1'=4Y+24Y/(2Y-3)²,
    p1''=8Y-48Y(2Y+3)/(2Y-3)³.

POWER_THETA_DENSITY_OUTER_088§§3–4 controla la cola COMPLETA y da errores menores que eta<1 en p,p',p''. En consecuencia

    0<p<2Y+1, 4Y-1<p'<4Y+2, p''<8Y+1.

Sustituir con los signos correctos (no se necesita p''>0) produce

    N>r²(16Y²-26Y+1)-r(8Y²+8Y+2)-(4Y²+4Y+1)
      >=r²(4Y²-38Y-2)>2r²Y²>0.

Se usa r>=1 y 2Y²-38Y-2>0 para Y>21. Así q''(u)>0 para TODO u>=1.

**Historia del gate.** En el origen el test de convexidad, si V''(0)>0, es 10V^(4)(0)²-3V''(0)V^(6)(0)>=0; no se deduce de V'''>0. Diagnósticos mpmath60 con20modos en el origen y r=1/4,1/2,3/4,1,3/2 dieron signo favorable, pero NO fueron certificados y no se usan en la prueba siguiente.

### 12.1. Cierre compacto con theta completa y paridad exacta

**PROVED por certificado de bolas Arb, 2026-11-06.** Fuente reproducible: `tools/power_temporal_reciprocal_compact_verify.py`; salida constructor exit0/FULL PASS en `tools/power_temporal_reciprocal_compact_verify.log`. SHA256 del script: `498e199ae7bb52f7fedeef02847a1b8642a635b76bb036212259bc2f875e93fa`. Python-flint0.9.0, precisión512bits. Parámetros fijos:16modos theta, grado40 y256paneles en el origen;8192paneles y Taylor grado24/cap28 en el resto. No se ejecutó búsqueda de parámetros. La primera evaluación directa de intervalos del resto fue inconclusa por dependencia; se sustituyó por el polinomio entero siguiente. El grado16 dejó un resto absoluto excesivo cerca de r=1; el bound Cauchy a priori fijó grado24 antes de ejecutar la versión final, conservando malla y precisión.

**Origen, sin cocientes temporales singulares.** La función par COMPLETA define f(u)=Phi(sqrt(u)), holomorfa para |u|<=1/16, con |f|<1000 por089§2. Su Taylor hasta grado40 se obtiene de los coeficientes pares de Phi en cero. No se supone paridad del prefijo de16modos: primero se encierran TODOS los jets de la serie completa y luego se usa la paridad de Phi. En |z|<=1/4, la cola modal tiene módulo menor que

    epsilon_O=304*17^4/4^289.

Cauchy da error epsilon_O*4^j en cada coeficiente temporal de orden j; los coeficientes impares completos incluyen0. Para las derivadas de órdenes j=0,...,3 del Taylor de f, en0<=u<=1/64 el resto completo está acotado por

    2000*(41!/(41-j)!)*16^41*(1/64)^(41-j).

Se usa |[u^k]f|<=1000*16^k y la razón consecutiva del majorante, menor que1/2. Los256paneles de ancho1/16384 certifican f>0, f'<0 y

    L3=f''' f²-3f''f'f+2f'^3>2/5.

La salida guarda el lower más preciso, mayor que0.40639. Como a=-2f'/f, se concluye a>0 y a''=-2L3/f³<0; por tanto (1/a)''>0 en TODO0<=u<=1/64, incluidos ambos bordes.

**Resto, polinomio entero y errores absolutos controlados.** En r∈[1/8,1], escribir F=Phi(r) y sus derivadas temporales. La identidad exacta es

    T=N F³=-r²F'²F''+2r²F F''²-r²F F'F'''
              +rF'^3-rF F'F''-F F'².

En cada disco |z-r|<=1/64, Re exp(2z)>1, |exp(2z)|<9 y |exp(5z/2)|<16. Así |Phi_m(z)|<4800m^4*8^(-m²), |Phi(z)|<10000 y la cola después de16modos está acotada por

    epsilon_R=9600*17^4/8^289.

La razón consecutiva del majorante modal es menor que1/2. Cauchy da error epsilon_R*64^j en cada coeficiente Taylor temporal. Se incluyen esos errores ANTES de formar T. Para |z-r|<=1/128, |Phi^(j)(z)|<=Pj=10000*j!*128^j, j<=3, y |z|<2. Sustituir en el polinomio exacto da

    |T|<=4(P1²P2+2P0P2²+P0P1P3)
            +2(P1³+P0P1P2)+P0P1²<10^24.

Los8192paneles tienen semiancho h=7/131072, de modo que128h=7/1024. El resto después de grado24 es, uniformemente,

    REM_R=10^24*(7/1024)^25/(1-7/1024)<10^(-30).

Cada panel certifica T(center) menos la suma de módulos de los términos Taylor no constantes y REM_R estrictamente positivo. El lower común de la salida es mayor que10^(-17). Se cubren las celdas CERRADAS y los extremos1/8,1; no se infiere el signo de puntos muestreados.

**Denominadores y ensamblaje.** El origen también certifica a(0)=V''(0)>0.073 prueba V'''>0 en toda la semirrecta, luego V''(r)>V''(0)>0 y p(r)>0 para TODO r>0 por p(0)=0. Así a>0 globalmente. Phi>0, T>0 y la fórmula de N prueban q''>0 en1/64<=u<=1. El origen cubre0<=u<=1/64; la cola de§12 cubre u>=1. Se obtiene

    a(u)>0 y q''(u)>0 para TODO u>=0,
    HK>J².

La estrictitud de momentos resulta directamente de la identidad de§12: u²(2a'²-aa'')=u²a³q'' es positiva para u>0 y la densidad w es positiva. Los bordes e integrabilidad ya justificados allí permanecen válidos.

### 12.2. Consecuencia local para triples temporales simétricos

Para los d,b,c,d0 de§10, poner B=Phi(0)Phi''(0). Taylor bajo las integrales completas, paridad y supercolas dan

    d0=2H,
    c=2H-J R²+(K-B)R^4/12+O(R^6),
    d+b=4H-4J R²+(4K-B)R^4/3+O(R^6),
    D(R)=d0(d+b)-2c²=2(HK-J²)R^4+O(R^6).

Los términos B conservan los bordes en cero y cancelan exactamente en D. En particular se usan integral Phi Phi'''=-B e integral r Phi Phi''''=K+B; no se descartan esos bordes. La identidad integral simetrizada del intento anterior proporciona también D/d0=R^4(K-J²/H)+O(R^6).

Como HK>J², existe R0>0 tal que D(R)>0 para TODO0<R<R0. El otro sector tiene d-b>0 por§9. Por tanto A en los tres nodos(-R,0,R) es SPD para TODO R positivo suficientemente pequeño. No se cuantifica R0 ni se certifica un intervalo por búsqueda. Junto a§10 se tienen familias pequeñas y grandes; NO se cubren todos los R intermedios, triples arbitrarios ni todos los órdenes. No hay cierre del signo global, nueva cobertura W/T ni cambios en papers.


### 12.3. Alcance frente al falsificador074 y a la positividad por capas

Cotejo y cálculo arithmetic_fresh_candidate, revisados por root; consecuencias de fórmulas existentes, no prueba de suficiencia global. En074, n=999999 y a(u)=A[1+(u/4)^n]. Derivar q=1/a da

    q''(u)=n*4^(-n)*u^(n-2)*[(n+1)(u/4)^n-(n-1)]
             /[A(1+(u/4)^n)^3]<0 para0<u<=1.

Por tanto el falsificador074 NO satisface la nueva hipótesis de§12: no puede invocarse para refutar suficiencia de esa hipótesis adicional. Esto no demuestra dicha suficiencia.

Como contraste explícito, V(r)=r²/2+r⁴/4+epsilon*r⁶/6, 0<epsilon<=1, cumple a=1+u+epsilon*u², a'>0 y

    a³ q''=2(1-epsilon)+6epsilon*u+6epsilon²*u²>0, u>0.

Sin embargo V'(R)/R³ tiende a infinito, por lo que el falsificador de capas de§5 se aplica: la nueva condición no hace positivas todas las capas S_v. No se obtuvo un falsificador ni una prueba global del INTEGRAL A para esta familia; el caso cuártico epsilon=0 de§4 no autoriza extrapolar. La revisión constructiva tampoco produjo una cota del déficit integral D(R) para todo R a partir de q convexa. Los R intermedios y todos los órdenes permanecen OPEN.


## 13. La convexidad recíproca tampoco basta para todos los órdenes

**PROVED, clase genérica declarada.** Construcción arithmetic_fresh_candidate/root, revisión independiente de estabilidad positive_identity_attempt. Consulta previa de los tres índices y§§8.7–8.9,12. Diferencia: el error relativo se controla ahora en C6, lo que conserva la nueva desigualdad diferencial GLOBAL, no sólo datos finitos. No se refuta la Phi real ni se conserva su identidad aritmética completa.

Existen densidades psi positivas, pares, holomorfas en el strip de Phi y arbitrariamente cercanas a Phi en error relativo C6, con las colas relativas de§8.7, que satisfacen

    V_psi'''(r)>0 para r>0,
    a_psi(u)=V_psi'(sqrt(u))/sqrt(u)>0,
    (1/a_psi)''(u)>0 para u>=0,

pero cuyo A_psi NO es PSD. El tamaño de un bloque negativo no se especifica. Estas densidades sí satisfacen HK>J² y positividad de triples temporales simétricos pequeños por§12; no hay contradicción entre esas conclusiones finitas y el fallo global.

**1. El corte relativo de§8.7 es pequeño también en derivadas.** Con el mismo cutoff par fijo chi, n>=2, x=pi exp(2t)>=pi e para t>=1/2, poner r_n=Phi_n/Phi_1. La fórmula modal explícita y D=2x partial_x dan, para0<=j<=6,

    |D^j r_n(t)|<=C_j n^(4+2j)(1+x)^j exp[-(n²-1)x].

Los factores racionales sólo tienen denominadores 2x-3, separados de cero. Las series de esos bounds convergen uniformemente en x>=pi e. Por tanto 1+sum_(n>=2)r_n y sus primeras seis derivadas están acotadas, el denominador es>=1 y las derivadas de su inverso están acotadas. Así

    h_M=chi * [sum_(n>M)r_n]/[1+sum_(n>=2)r_n]

satisface, para cada B>=0 fijo,

    ||h_M||_(B,6):=max_(j<=6) sup_t exp(B|t|)|D^j h_M(t)|
       <=C_B sum_(n>M)n^16 exp[-(n²-1)pi e/2] ->0.

Se absorben los factores polinómicos de x y exp(Bt)=(x/pi)^(B/2) contra la mitad del exponencial. Las derivadas del cutoff sólo cambian C_B; h_M es cero cerca del origen. No se afirma control uniforme en todos los órdenes de derivación.

**2. Estabilidad de las desigualdades diferenciales.** Para psi=Phi exp(-E), E par con ||E||C6<=delta, poner beta(u)=E'(r)/r, u=r². Las identidades integrales para una función par dan en0<=u<=1

    |beta|<=delta, |beta'|<=delta/6, |beta''|<=delta/60.

Por ejemplo beta=integral_0^1 E''(tr)dt; derivar usando paridad y el teorema fundamental del cálculo da beta'=(1/2)integral_0^1 t² integral_0^1 E^(4)(str)dsdt, y beta''=(1/4)integral t⁴ s² E^(6)(vstr)dvd sdt. Los coeficientes resultan de integrar esos pesos. Por§12, a y S=2a'²-aa'' tienen mínimos estrictamente positivos en[0,1]. La perturbación a+beta conserva ambos si delta es suficientemente pequeño.

En r>=1,088 da |p|,|p'|,|p''|<=128Y, Y=pi exp(2r)>21, y§12 da N>2r²Y². Para delta<=1 los segmentos de jets perturbados quedan acotados por129Y. La suma de los módulos de las tres derivadas parciales del polinomio N respecto de p,p',p'' es<=1290r²Y. Luego

    |N_psi-N|<=1290delta r²Y.

Tomar delta<=1/100 conserva N_psi>r²Y²>0 y p_psi>0, pues p>2Y-6. Esto completa la estabilidad global de a>0 y q''>0.

También se conserva V'''>0:073 certifica V^(4)>=m4>0 cerca de0, mientras |E'''(r)|<=delta r por paridad. En un compacto separado de0 hay un mínimo positivo de V'''; en la cola V'''~8Y tiende a infinito. Reducir delta conserva los tres tramos. Por tanto a_psi'>0 también sigue de la misma identidad usada en§9.

**3. Analiticidad y bloque negativo, en el orden correcto.** Tomar g=h_M*gamma_sigma con0<sigma<=1. Las derivadas conmutan con la convolución y

    ||g||_(B,6)<=||h_M||_(B,6) integral exp(B|z|)gamma_sigma(z)dz.

El factor es acotado uniformemente para sigma<=1. Además0<=g<=epsilon_M, y E=-log(1-g) es pequeño en C6 cuando M es grande. Elegir PRIMERO M que asegure la estabilidad anterior para todos esos sigma. La densidad suave Phi(1-h_M) coincide con el prefijo Phi_M en t>=1;§8.7 proporciona un bloque negativo finito con nodos en(1,2). Elegir DESPUÉS sigma suficientemente pequeño para conservar ese bloque mediante la convergencia uniforme g->h_M y el bound de entradas2||g-h_M||infinito A_Phi de§8.7. La densidad final psi=Phi(1-g) es par, positiva y analítica; conserva las colas declaradas y todas las desigualdades diferenciales anteriores.

**Alcance.** Queda refutada la suficiencia global de esta clase de hipótesis diferenciales, incluso junto a cercanía relativa C6 y las colas indicadas. No se descarta un argumento que use la estructura theta completa, una compensación adicional específica, ni la investigación de triples intermedios de la Phi real. No nueva ventana W/T, ningún cambio en papers y ningún cómputo nuevo.


## 14. El recíproco temporal no admite la representación Laplace positiva propuesta

**PROVED, root/arithmetic_fresh_candidate; revisión matemática independiente.** Consulta dirigida de índices, grid y crucigrama por diagonal_gauge_dedup sin antecedente literal localizado:086 concierne al recíproco de M,111 a monotonía en otro parámetro, y los descartes HCM a otra densidad. La cuestión nueva es q(u)=sqrt(u)/V'(sqrt(u)) de§12, no el signo del kernel original. El argumento sólo usa theta, Poisson, una suma de Gauss finita y unicidad analítica; no usa ninguna equivalencia externa del problema del signo.

**Enunciado.** q, definida para u>0, no tiene extensión holomorfa a TODO Re u>0. En particular no existe una medida positiva mu en[0,infinito) tal que

    q(u)=integral exp(-us)dmu(s), u>0.

La finitud de esa integral para cada u>0 implicaría holomorfía en el semiplano: en un compacto Re u>=a>0 se dominan todas las derivadas por una constante por exp(-as/2), integrable. No se necesita suponer de antemano masa total finita.

**1. Identidad sin denominadores.** Si Q fuese esa extensión, en el dominio convexo

    D={z=x+iy: x>|y|, |y|<pi/4}

se tendría Q(z²)Phi'(z)+zPhi(z)=0. Ambos términos son holomorfos y la igualdad vale en el eje real positivo por§12. La unicidad analítica la extiende a D. No se divide por Phi' en ese dominio.

**2. Cúspides racionales y coeficiente no nulo.** Para cada m>=3 impar, tomar tau_m=16+2/m, w0=i tau_m y w=w0+delta, delta>0. La descomposición por residuos módulo m y Poisson dan exactamente

    theta(w0+delta)=delta^(-1/2)/m
       *sum_(nu entero) exp[-pi nu²/(m²delta)] G_m(nu),
    G_m(nu)=sum_(j mod m) exp[-2pi i j²/m+2pi i nu j/m].

El término16 no cambia la fase. Si G_m=G_m(0), entonces |G_m|²=m: al expandir el cuadrado, cambiar variables a=j-k,b=j+k módulo m es invertible y la suma es sum_(a,b)exp(-2pi i ab/m)=m. Por tanto G_m no es nulo. Para cada m fijo,

    theta(w0+delta)=(G_m/m)delta^(-1/2)+resto.

El resto y sus primeras tres derivadas son O_m(delta^(-N)exp(-c_m/delta)) para algún N y c_m>0. Se obtiene diferenciando la serie de nu!=0: sólo aparecen potencias de nu y delta^(-1), dominadas por una parte de la exponencial gaussiana. No se requiere uniformidad en m.

**3. Límite del recíproco y contradicción.** Con z=(1/2)Log w en la rama del primer cuadrante,

    Phi(z)=w^(5/4)[w theta''(w)+(3/2)theta'(w)].

Los términos algebraicos de orden delta^(-3/2) cancelan exactamente. Así

    Phi(z)=(3G_m/(4m))w0 w^(5/4)delta^(-5/2)+resto,
    Phi'(z)/Phi(z)=-5w0/delta+O_m(1).

El control del resto diferenciado justifica ambos equivalentes; los términos principales son no nulos. La identidad del paso1 fuerza

    Q(z²)=-zPhi(z)/Phi'(z) ->0 cuando delta baja a0.

Estos z pertenecen a D y convergen a z_m=(log tau_m)/2+i pi/4. Además Re(z_m²)>0, pues (log tau_m)/2>log4>1>pi/4. Por continuidad de la extensión hipotética, Q(z_m²)=0 para todo m impar. Los puntos z_m² son distintos y convergen al punto interior (log4+i pi/4)² del semiplano. Unicidad analítica fuerza Q idénticamente nula allí, contrario a q(u)>0 en el eje real. Esto prueba el enunciado.

**Alcance del test de momentos.** Antes de esta prueba se evaluaron los coeficientes de q de órdenes0,...,39 usando los jets COMPLETOS ya encerrados en el certificado de§12 (grado40 de Phi(sqrt u)); todos sus signos alternados son estrictamente positivos. No se usa ese test en la prueba ni se lo extrapola. El descarte sólo concierne a la representación positiva propuesta de q y a su extensión holomorfa; no refuta q''>0, HK>J², los triples positivos ni A_Phi. No nuevaW/T ni cambios en papers.


## 15. G convexa no basta ni para los triples temporales simétricos

**PROVED por contramodelo elemental.** Constructor positive_identity_attempt, revisión root/arithmetic_fresh_candidate PASS. Consulta dirigida de índices, grid, crucigrama y074/101 sin este falsificador temporal literal localizado. Diferencia: se decide la suficiencia de G convexa para el bloque(-R,0,R), no un bloque del kernel de exponentes ni todos los órdenes a la vez.

Tomar exactamente epsilon=1/1000 y

    phi(r)=exp(-r²/2-epsilon*r⁶/6),
    G(u)=u/2+epsilon*u³/6, u=r².

G'>0, G''=epsilon*u>0 para u>0 y V'''(r)=20epsilon*r³>0 para r>0. La densidad es par, positiva y entera; sus supercolas justifican todos los bordes y derivaciones de§12. En particular sus pares temporales son SPD por§9.

Con a=1+epsilon*u², w=exp(-u-epsilon*u³/3), Z=integral_0^infinito w y E la esperanza normalizada, la identidad de§12 da

    Delta=(HK-J²)/H²
      =-2epsilon E[u²]+epsilon²(15E[u⁴]-9E[u²]²).

Definir I_j=integral u^j w. La desigualdad elemental exp(-x)>=1-x y las integrales factoriales dan

    I_2>=2!-epsilon*5!/3=2-40epsilon=49/25,
    I_4<=4!=24.

Descartar sólo el término no positivo de Delta produce

    Delta<=(epsilon/Z)[-2I_2+15epsilon I_4]
         <=-89/(25000Z)<0.

Por la expansión de§12.2, el determinante del sector simétrico satisface D(R)=2(HK-J²)R⁴+O(R⁶)<0 para TODO R>0 suficientemente pequeño. Así la matriz temporal de tres nodos(-R,0,R) es indefinida. No se requiere buscar ni evaluar numéricamente R.

Este potencial no satisface la convexidad recíproca nueva: q(u)=1/(1+epsilon*u²) tiene q''(0)=-2epsilon<0. El resultado no contradice§12 para la theta real ni refuta los triples de potencias080. Tampoco dice que q convexa baste para triples arbitrarios. Se descarta únicamente la suficiencia de G convexa (incluso acompañada de V'''>0) para los triples temporales simétricos. Sin cómputos, nuevaW/T ni cambios en papers.


## 16. Equivalente del kernel completo en escalas enteras fijas

**PROVED, 2026-11-06.** Construcción root/joint_sign_fresh_review, cálculo y verificación independiente global_restart_checked; auditoría matemática independiente arithmetic_fresh_candidate PASS y root PASS, incluidos prefactores y corolario. Consultados las reglas del proyecto, los tres índices y las primarias pertinentes; cotejo dirigido sin antecedente literal localizado para el equivalente de A siguiente. Los Grams aritméticos de phase209 [CONSTRUCTOR_005](../phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) y [AUDIT_005](../phase-209-nonlocal-kernel/AUDIT_005.md) son antecedentes explícitos: el kernel gcd y su positividad son clásicos, no nuevos. La diferencia es identificar aquí el principal del A REAL COMPLETO, con sus casi resonancias controladas, no sustituir A por un Gram aritmético favorable. El promedio de banda de§4.1 es antecedente del método oscilatorio; por sí solo no daba este equivalente sobre toda la semirrecta.

### 16.1. Enunciado y fórmula exacta

Sean k,l enteros positivos FIJOS, z_k=(log k)/2+iy, epsilon=cos(2y) bajando a0 y L=log(1/epsilon). Definir rho(k,l)=0 si k,l no tienen la misma parte libre de cuadrados. Si k=d a²,l=d b² con d libre de cuadrados, poner

    rho(k,l)=gcd(a,b)/sqrt(ab).

Entonces

    A(z_k,conjugado(z_l))
      =[105/(512sqrt2)] rho(k,l) epsilon^(-9/2) L²
         +O_(k,l)(epsilon^(-9/2) L).                 (INT-ASYM)

El resto es complejo en general; sus constantes dependen de k,l. No se afirma uniformidad en esos enteros, el número de nodos o su separación.

Para sigma=sin(2y), t=exp(2r)>=1 y c_kl=(log k+log l)/2, la representación exacta conserva el factor temporal:

    A(z_k,conjugado(z_l))
       =integral_1^infinito w_kl(t) Phi_k(t) conjugado(Phi_l(t))dt,
    w_kl(t)=[log t+c_kl]/(2t),
    Phi_k(t)=Phi((log(kt))/2+iy)=U_k(t)+V_k(t),
    U_k(t)=2pi²(kt)^(9/4)exp(9iy/2)
                   sum_(n>=1)n4 exp[-pi(epsilon+i sigma)kt n²],
    V_k(t)=-3pi(kt)^(5/4)exp(5iy/2)
                   sum_(n>=1)n² exp[-pi(epsilon+i sigma)kt n²].

Para epsilon>0 fijo, las series y sus productos son absolutamente integrables en t>=1 con este peso; la exponencial gaussiana domina todos los factores polinomiales y logarítmicos. Así Fubini y las diferenciaciones de amplitudes siguientes se justifican antes de tomar epsilon a0. El producto principal tiene el prefactor EXACTO

    4pi4(kl)^(9/4) sum_(n,m>=1)n4m4
       integral_1^infinito w_kl(t)t^(9/2)
          exp[-pi epsilon t(kn²+lm²)]
          exp[-i pi sigma t(kn²-lm²)]dt.             (MAIN)

### 16.2. Casi resonancias: control elemental también para aproximaciones cuadráticas

Con prima indicando kn²!=lm², se prueba para TODO delta>0

    S_delta=sum' n4m4 exp[-delta(kn²+lm²)]/|kn²-lm²|
       <=C_(k,l) delta^-4 log(2+1/delta).            (NEAR)

Para verlo, descomponer en cajas diádicas max(n,m) comparable a N. Fuera de una región donde sqrt(k)n y sqrt(l)m son comparables, el denominador es>=c_(k,l)N²; la suma de numeradores es O(N10), y el bloque es O(N8). En la región comparable, poner alpha=sqrt(k/l); el denominador es comparable a N|alpha n-m|.

Si alpha es irracional, la integridad de kq²-lp² implica |alpha q-p|>=c_(k,l)/q para el entero p más próximo y q>=1. Los residuos alpha n de una caja de longitud O(N) están por tanto separados en el círculo al menos c_(k,l)/N y también a esa distancia de0. Ordenar sus distancias a los enteros da sum_n dist(alpha n,Z)^(-1)<=C_(k,l)N log(2N). Los m más próximos aportan O(log(2N)) a la suma de denominadores inversos de la caja; los demás m aportan lo mismo por la suma armónica de sus distancias. Al multiplicar por n4m4<=C N8, se obtiene O(N8 log(2N)). Si alpha es racional, las distancias no nulas tienen un denominador fijo; se omiten sólo las resonancias exactas y la misma cota armónica basta. Esto conserva, en particular, las aproximaciones con |kn²-lm²| pequeño y no nulo.

Sumar O(N8 log(2N))exp(-c delta N²) sobre N diádico prueba (NEAR) para delta<=1. Para delta>=1, extraer parte de la exponencial da S_delta<=C exp(-c delta)<=C' delta^-4, que completa la fórmula para todo delta.

En t∈[T,2T], T=2^j>=1, integrar por partes contra la fase de (MAIN). Con Q=kn²+lm² y d_nm=kn²-lm² distinto de0, el borde y la derivada de la amplitud se acotan por

    C_(k,l) T^(7/2)(1+log T)
         (1+epsilon T Q)exp(-pi epsilon T Q).

El factor adicional se absorbe en parte de la exponencial. Como sigma>=1/2 eventualmente, el integral oscilatorio es<=C T^(7/2)(1+log T)exp(-c epsilon T Q)/|d_nm|. Aplicar (NEAR) con delta=c epsilon T y sumar todos los T da para TODOS los pares no resonantes de (MAIN)

    <=C_(k,l) epsilon^-4
        sum_(T=2^j) T^(-1/2)(1+log T)log(2+1/(epsilon T))
    <=C'_(k,l) epsilon^-4 log(2+1/epsilon).          (OFF)

La suma diádica T^(-1/2)(1+log T) converge. No se ha usado una cota uniforme para razones reales arbitrarias ni se han borrado casi resonancias.

### 16.3. Resonancias exactas y constante del equivalente

Si k,l no comparten parte libre de cuadrados, no hay resonancias exactas. En el otro caso, escribir k=d a²,l=d b²,g=gcd(a,b). Todas las resonancias son

    n=(b/g)j, m=(a/g)j, j>=1,
    kn²=lm²=Lambda j², Lambda=d(ab/g)²,
    (kl)^(9/4)n4m4=(kl)^(1/4)(Lambda j²)^4,
    (kl)^(1/4)/sqrt(Lambda)=rho(k,l).

Poner F(s)=s^(9/2)sum_(j>=1)j8 exp(-2pi s j²). El mismo argumento Riemann uniforme de§4.1 da

    F(s)=F0+O(sqrt s), s bajando a0,
    F0=Gamma(9/2)/[2(2pi)^(9/2)],
    F(s)<=C s^(9/2)exp(-c s), s>=1.

El aporte resonante completo es exactamente

    4pi4 rho(k,l) epsilon^(-9/2)
       integral_1^infinito [log t+c_kl]/(2t) F(epsilon Lambda t)dt.

Con s=epsilon Lambda t, sustituir F por F0 en epsilon Lambda<=s<=1 produce F0 log²(1/epsilon)/4+O_(k,l)(L). El error O(sqrt s) se integra contra [log(s/(epsilon Lambda))+c_kl]/s y es O_(k,l)(L); la cola s>=1 también es O_(k,l)(L) por su decaimiento exponencial. Los cambios constantes log Lambda y c_kl sólo afectan ese resto. Como

    4pi4 F0=105/(128sqrt2),

se obtiene el coeficiente105 rho(k,l)/(512sqrt2) de(INT-ASYM).

### 16.4. Términos inferiores, corolario y alcance

Las cotas gaussianas absolutas, válidas para todo t>=1, dan

    |U_k(t)|<=C_k epsilon^(-5/2)t^(-1/4),
    |V_k(t)|<=C_k epsilon^(-3/2)t^(-1/4).

El peso w_kl(t)t^(-1/2) es integrable en[1,infinito). Por tanto las normas L²(w_kl dt) de U_k,V_k son O_(k,l)(epsilon^(-5/2)) y O_(k,l)(epsilon^(-3/2)). Cauchy–Schwarz acota los cruces U_k conjugado(V_l), V_k conjugado(U_l) por O_(k,l)(epsilon^-4), y el producto inferior por O_(k,l)(epsilon^-3). Junto con(OFF), quedan absorbidos en el resto O_(k,l)(epsilon^(-9/2)L). No se supone previamente que A sea PSD.

**Corolario para una lista fija.** Para cualquier lista finita FIJA de enteros positivos distintos k_i, la matriz [rho(k_i,k_j)] es definida positiva. Las partes libres de cuadrados distintas dan bloques separados. Dentro de cada bloque, la congruencia por sqrt(a_i) produce [gcd(a_i,a_j)]. La identidad CLÁSICA gcd(a,b)=sum_(q|a,q|b)phi(q), con phi(q)>0, da un Gram de incidencias de divisores; sobre los a_i distintos ordenados, las columnas q=a_i forman una matriz triangular con diagonal1. Así el Gram es definido positivo. Esta identidad y la positividad aritmética no se presentan como nuevas.

En consecuencia, para cada tal lista, el bloque Hermitiano complejo [A(z_(k_i),conjugado(z_(k_j)))] es definido positivo cuando epsilon es suficientemente pequeño: al dividir por epsilon^(-9/2)L² se obtiene [105/(512sqrt2)]rho+O_lista(1/L), cuyo límite tiene mínimo autovalor positivo. El umbral DEPENDE de la lista; no hay uniformidad en dimensión ni enteros ni se certifica un valor numérico del umbral. Los enteros repetidos sólo duplican nodos y no dan definitud estricta.

El resultado identifica un principal aritmético del kernel original completo y prueba este corolario de bloques COMPLEJOS fijos. No demuestra PSD de A en una ventana real, CPD de log A, positividad de H, una comparación relativa uniforme de todos los órdenes ni el signo global. No se confunde con el kernel renormalizado de phase209 ni se transfiere su norma al portador del paper. Sin campañas, datos numéricos, nueva cobertura W/T ni cambios en papers.

### 16.5. El comparador rho no da dominación uniforme ni tras normalizar la diagonal

**PROVED, misma fecha y entrada.** Propuesta root, cálculo global_restart_checked; auditoría independiente arithmetic_fresh_candidate PASS y root PASS. Cotejo dirigido en los tres índices y corpus phase209/211 sin antecedente literal localizado para este límite de enteros consecutivos. El antecedente de§4.3 estudia otra cola con variables reales; aquí se fija PRIMERO y∈(0,pi/4), por tanto epsilon=cos2y>0 y sigma=sin2y, y DESPUÉS se hace k tender a infinito con l=k+1. No se intercambia ese orden con(INT-ASYM).

Poner x_k=(log k)/2, u=x_k+x_l y E=epsilon(k+l)+i sigma(k-l). Para k,l en{k,k+1}, la serie theta COMPLETA, normalizada por su primer modo, da uniformemente en r>=0, con s=exp(2r)-1,

    Phi(z_k+r)/Phi(z_k)
      =(1+s)^(9/4)exp[-pi k exp(2iy)s] B_k(s),
    B_k(s)=1+O_y(1/k)+O_y(exp(-3pi epsilon k)).

En efecto, el cociente del factor racional del primer modo es [1-a_k/(1+s)]/[1-a_k], a_k=3/[2pi k exp(2iy)], y difiere de1 en O(1/k) uniformemente. La cola relativa completa se acota por C_y sum_(n>=2)n4 exp[-pi(n²-1)epsilon k(1+s)]<=C'_y exp(-3pi epsilon k). Para k suficientemente grande, esos factores muestran también Phi(z_k)!=0. Con D_kl(s)=B_k(s)conjugado(B_l(s)), se obtiene exactamente

    A(z_k,conjugado(z_l))/[Phi(z_k)conjugado(Phi(z_l))]
       =(1/2)integral_0^infinito [u+log(1+s)](1+s)^(7/2)
                           exp(-pi E s) D_kl(s)ds.

Aquí D_kl=1+O_y(1/k) uniformemente y Re E es comparable a k para y fijo. La amplitud sin D es u+O((u+1)s(1+s)^(7/2)); integrar el error contra exp(-pi Re E s) da O_y((u+1)/k²). Así

    A(z_k,conjugado(z_l))/[Phi(z_k)conjugado(Phi(z_l))]
       =u/(2pi E) [1+O_y(1/k)],
    A(z_k,conjugado(z_k))/|Phi(z_k)|²
       =x_k/(2pi epsilon k) [1+O_y(1/k)].

Las diagonales de A son positivas por su integral horizontal. Definir el bloque normalizado C_y(k,l)=A(z_k,conjugado(z_l))/sqrt(A(z_k,conjugado(z_k))A(z_l,conjugado(z_l))). Para l=k+1, las fórmulas anteriores implican

    |C_y(k,k+1)|
       =[epsilon sqrt(k(k+1))(x_k+x_(k+1))
          /(sqrt(x_k x_(k+1)) |epsilon(2k+1)-i sigma|)]
            *[1+O_y(1/k)] ->1.

Pero rho(k,k+1)=0: si compartieran parte libre de cuadrados, 1=d(b²-a²), imposible para a,b positivos. El bloque rho es por tanto I_2, mientras el mínimo autovalor del bloque C_y es 1-|C_y(k,k+1)| y tiende a0. Para CUALQUIER y fijo como arriba no existe c_y>0 tal que C_y>=c_y rho sobre todos los bloques enteros, aunque c_y dependa de y. Asimismo sup_(k,l)|C_y(k,l)-rho(k,l)|>=1 para cada y fijo; en particular no hay aproximación uniforme o(1) a rho cuando epsilon baja a0.

Sólo se descartan estas dos afirmaciones sobre el comparador rho CON ESTA normalización diagonal. No se prueba un valor negativo de A, no se supone A PSD y no se excluyen otros modelos, pesos o compensaciones. El equivalente para nodos fijos de§16.1 y su corolario permanecen válidos; el límite de escape demuestra por qué no se extienden uniformemente en los enteros. No se afirma aquí un régimen conjunto variable de epsilon,k ni una ley de transición. Signo global OPEN; sin nueva ruta, cómputos, cobertura W/T ni cambios en papers.


## 17. Suma de cuadrados exacta para la parte resonante completa

**PROVED, 2026-11-06.** Construcción root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría matemática independiente arithmetic_fresh_candidate PASS y root PASS para la identidad SOS, su positividad estricta y el antecedente de una frecuencia individual. Leídos las reglas del proyecto, los tres índices, POWER_SIGNED_MEAN_019 con su auditoría y phase209 CONSTRUCTOR_005/AUDIT_005; cotejo dirigido sin esta identidad literal localizada. Las herramientas de divisores, factoriales y sumas de cuadrados son conocidas. La diferencia es conservar la parte resonante EXACTA del kernel A y construir una SOS que acopla frecuencias distintas mediante cambio de escala. No se invierte una media por Möbius como en019 ni se sustituye el objeto por el Gram renormalizado de209.

Fijar y real con |y|<pi/4, incluido y=0; poner a_y=exp(2iy), epsilon=cos(2y)>0 y z_k=(log k)/2+iy para k entero positivo. En la expansión modal exacta de§16, definir R_res como la contribución de TODOS los pares con kn²=lm², manteniendo el integral completo t>=1 y los dos términos del polinomio modal. La contribución restante de A contiene kn²!=lm². Para fijar las normalizaciones, poner

    h_lambda(t)=pi(lambda t)^(5/4)(2pi a_y lambda t-3)
                         exp(5iy/2)exp(-pi a_y lambda t),
    Phi((log(kt))/2+iy)=sum_(n>=1)n^(-1/2)h_(kn²)(t),
    H(u)=|h_u(1)|²
        =pi²u^(5/2)|2pi a_y u-3|²exp(-2pi epsilon u),
    I_lambda=lambda^(-1/2)integral_lambda^infinito H(u)/(2u)du,
    J_lambda=lambda^(-1/2)integral_lambda^infinito
                                      log(u/lambda)H(u)/(2u)du.

Para lambda>=1, H(u)>0 en u>=lambda, pues 2pi u>3; por tanto I_lambda,J_lambda>0. Todo el argumento usa epsilon>0 fijo, sin aproximación de borde.

**Cotejo bibliográfico posterior (2026-11-06).** La representación de una forma de grafo mediante diferencias al cuadrado y potencial tiene antecedente general en Keller–Pinchover–Pogorzelski, [Criticality theory for Schrödinger operators on graphs, §4.2](https://arxiv.org/html/1708.09664#S4.SS2). Alexeev et al., [Primitive sets and von Mangoldt chains, Ejemplo2.4 y§10.1](https://arxiv.org/html/2605.00301v1#S10.SS1), emplean la cadena P(q→q/m)=Lambda(m)/log q. Para cada d, el peso nu_d(q)=I_(dq²)log q, q>=2, reproduce exactamente las conductancias Lambda(m)I_(dq²) de la SOS siguiente; q=1 es el extremo absorbente. Abreviando I_q=I_(dq²), J_q=J_(dq²), su potencial es D_q=J_q+log(d)I_q+Out_q−In_q, con Out_q=log(q)I_q e In_q=sum_(m>=2)Lambda(m)I_(qm). No se transfiere la subinvariancia de los pesos distintos del artículo: D_q>0 se prueba aquí por las cotas siguientes. No se atribuye novedad a completar cuadrados, al grafo divisor ni a la identidad factorial. La búsqueda dirigida root/fresh_global no localizó el mismo teorema con estos pesos theta y esta cota de D_q; eso NO establece prioridad mundial. La cadena no estima los productos de perfiles de frecuencias distintas del resto no resonante;§17.6 sigue aplicándose. Esta comparación bibliográfica no añade signo ni un método de cierre.

### 17.1. Una frecuencia individual puede ser indefinida

En los nodos k=1,4, la frecuencia comun lambda=4 corresponde a n=2,m=1. Su matriz, usando I_4,J_4 recién definidos, es exactamente

    [[J_4, sqrt2(J_4+log2 I_4)],
     [sqrt2(J_4+log2 I_4), 2(J_4+2log2 I_4)]],
    det=-2(log2)² I_4²<0.

Este descarte de positividad por cada frecuencia NO se aplica a la suma de todas ellas. La construcción siguiente demuestra precisamente compensación entre frecuencias; no exige que cada bloque resonante individual sea PSD.

### 17.2. Transformación divisorial directa e identidad SOS

Las resonancias sólo acoplan enteros con la misma parte libre de cuadrados. Fijar uno de esos grupos k=d a², con d libre de cuadrados, y coeficientes complejos c_a de soporte FINITO. Abreviar I_q=I_(dq²), J_q=J_(dq²), y definir

    f_q=sum_(a|q)sqrt(a)c_a,
    g_q=sum_(a|q)sqrt(a)log(a)c_a.

La frecuencia lambda=dq² recibe exactamente los índices a|q, con n=q/a. El factor n^(-1/2)=sqrt(a/q) y el cambio u=lambda t, con sqrt(d)/sqrt(lambda)=1/q, dan

    R_res[c]/sqrt(d)
       =sum_(q>=1)[(J_q+log(d)I_q)|f_q|²
                               +2I_q Re(g_q conjugado(f_q))].

La identidad elemental sum_(m|r)Lambda(m)=log r da DIRECTAMENTE

    g_q=log(q)f_q-sum_(m|q,m>=2)Lambda(m)f_(q/m).

Completar los cuadrados y reindexar los términos de |f_(q/m)|² produce la identidad exacta

    R_res[c]/sqrt(d)
       =sum_(q>=1) D_q |f_q|²
          +sum_(q>=1)sum_(m|q,m>=2)
                     Lambda(m)I_q |f_q-f_(q/m)|²,             (RES-SOS)
    D_q=J_q+[log d+log q]I_q
                    -sum_(m>=2)Lambda(m)I_(qm).

Para comprobar factores y orientación: los cuadrados aportan log(q)I_q a la diagonal q por sum_(m|q)Lambda(m)=log q, y aportan sum_(m>=2)Lambda(m)I_(qm) al reindexar la otra diagonal. El resto es exactamente D_q, mientras el cruce es -2Lambda(m)I_q Re(f_q conjugado(f_(q/m))). No se han eliminado términos firmados ni introducido una inversión Möbius.

### 17.3. El coeficiente diagonal D_q es estrictamente positivo

Con lambda=dq², cambiar escala en cada I_(qm) y aplicar Tonelli a sus sumandos no negativos da

    D_q=lambda^(-1/2)integral_lambda^infinito H(u)/(2u)
       *[log u-log q
          -sum_(2<=m<=sqrt(u/lambda))Lambda(m)/m]du.          (DIAG)

Para X>1, N=floor X, la identidad factorial y floor(X/m)>=X/(2m), m<=X, implican

    log(N!)=sum_(m<=X)Lambda(m)floor(X/m)
       >=(X/2)sum_(2<=m<=X)Lambda(m)/m,
    sum_(2<=m<=X)Lambda(m)/m
       <=2log(N!)/X<2log X.

La última desigualdad es estricta para TODO X>1, incluyendo 1<X<2: log(N!)<Xlog X. Para u>lambda, tomar X=sqrt(u/lambda). El corchete de(DIAG) es estrictamente mayor que

    log u-log q-log(u/lambda)=log d+log q>=0.

Como H(u)>0 en u>=lambda, se concluye D_q>0 para TODOS d,q>=1. También vale cuando d=q=1: la cota inferior constante es entonces0, pero el corchete es estrictamente positivo en todo u>lambda.

### 17.4. Convergencia, definitud y alcance

Para epsilon>0 fijo, I_(dq²),J_(dq²) se acotan por un polinomio en q por exp(-c_y d q²); esto sigue directamente del polinomio por gaussiana de H. Los f_q,g_q son acotados porque c tiene soporte finito. En particular las expresiones previas convergen absolutamente. Para los cuadrados de(RES-SOS), basta sum_(m|q)Lambda(m)=log q y el acotamiento de f. La suma reindexada de diagonales entrantes también converge, pues sum_q sum_(m>=2)Lambda(m)I_(qm)=sum_r log(r)I_r<infinito. Estas cotas justifican las expansiones de cuadrados y todas las reindexaciones; las sumas modales originales son asimismo absolutamente integrables para epsilon>0 fijo.

Los pesos de(RES-SOS) son no negativos y D_q es estrictamente positivo. Si c no es nulo, elegir a0 mínimo con c_(a0)!=0; sus divisores propios tienen coeficiente0, luego f_(a0)=sqrt(a0)c_(a0)!=0. La primera suma es por tanto estrictamente positiva. Sumar los grupos libres de cuadrados, que no se acoplan en R_res, prueba que R_res es un kernel DEFINIDO POSITIVO sobre CUALQUIER conjunto finito de enteros positivos distintos k, para CADA y real con |y|<pi/4, incluido0. No hay restricción de tamaño ni un umbral dependiente de la lista para ESTA parte exacta. Los índices repetidos se agrupan y sólo dan semidefinitud como representación redundante.

El cambio u=lambda t y la transformación divisorial directa acoplan frecuencias lambda distintas, cada una potencialmente indefinida. Por eso la prueba evita exigir PSD de las capas o de cada frecuencia; no borra la estructura aritmética. El resultado tampoco contradice§16.5: R_res es la parte resonante exacta, no el comparador límite rho ni una dominación de A por él.

**Alcance del signo obtenido.** Se demuestra todos los órdenes de R_res sobre los índices ENTEROS positivos k. NO se demuestra todos los nodos reales del kernel A ni el signo de la contribución kn²!=lm². Sigue faltando un control conjunto de esa contribución no resonante. El puente posterior de§18 elimina la obligación adicional de pasar del A COMPLETO entero a todos los nodos reales; no transfiere por separado R_res ni prueba el signo faltante. No se infiere A PSD, CPD, positividad del kernel partial_t partial_s log A, una ventana nueva W/T ni cierre global. Sin campañas, datos numéricos, archivos auxiliares ni cambios en papers.

### 17.5. Cota uniforme en la energía divisorial exacta

**PROVED, misma fecha y entrada.** Refinamiento root/joint_sign_fresh_review; verificación independiente global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Para TODOS d,q>=1 y TODOS 0<epsilon<=1 de la familia anterior,

    D_q>=c_* I_q,
    c_*=(log2/3)*(4pi-3)²exp(-6pi)
                /[(4pi+3)²+(4pi-3)²exp(-6pi)]>0.             (UNIF-D)

Si dq>=2, la prueba de§17.3 ya da D_q>=log(dq)I_q>=log2 I_q, más fuerte. Sólo falta d=q=1,lambda=1. Para X>=2 y N=floor X, al menos floor(N/2) factores de N!/N^N son<=1/2; por tanto

    N!<=N^N 2^(-floor(N/2)),
    sum_(2<=m<=X)Lambda(m)/m
       <=2log(N!)/X
       <=2log X-[2floor(N/2)/X]log2
       <=2log X-log2/3.

Se usó 2floor(N/2)>=N-1 y (N-1)/X>(N-1)/(N+1)>=1/3. En el corchete de(DIAG) para d=q=1, poner X=sqrt u. Para u>=4 la cota anterior da un lower beta=log2/3. Para 2<=u<4 la suma está vacía y el corchete es log u>=log2. Así ese mismo lower beta vale en TODO u>=2; en[1,2] el corchete es no negativo por§17.3.

Escribir C para la masa de H(u)/(2u) en[1,2] y T para su masa en[2,infinito). Como |a_y|=1 y 0<epsilon<=1,

    C<=C_max=pi²sqrt2(4pi+3)²,
    T>=integral_2^3 H(u)/(2u)du
       >=T_min=pi²sqrt2(4pi-3)²exp(-6pi).

La primera cota usa u^(3/2)<=2sqrt2, |2pi a_yu-3|<=4pi+3 y exp(-2pi epsilon u)<=1. La segunda usa u^(3/2)>=2sqrt2, |2pi a_yu-3|>=4pi-3 y exp(-2pi epsilon u)>=exp(-6pi) en[2,3]. Por tanto

    D_1>=beta T,
    D_1/I_1>=beta T/(C+T)
              >=beta T_min/(C_max+T_min)=c_*.

Esto completa(UNIF-D). Para un vector finito sobre los enteros k, separar k=d a² y poner f_(d,q)=sum_(a|q)sqrt(a)c_(d a²). La identidad(RES-SOS) implica

    R_res[c]>=c_* E_y[c],
    E_y[c]=sum_(d libre de cuadrados)sqrt(d)
                    sum_(q>=1) I_(dq²)|f_(d,q)|².            (DIV-LOWER)

La constante c_* es uniforme en epsilon,d,q y tamaño del soporte, pero E_y conserva los pesos EXACTOS I_(dq²), que dependen de epsilon y de los índices. No es un margen uniforme respecto de la norma euclídea de los coeficientes ni una comparación para A completo. El término no resonante sigue sin controlar. El puente posterior de§18 transfiere la eventual positividad del A COMPLETO entero a todos los nodos reales; no transfiere por separado esta cota resonante ni añade una ventana W/T o cierre global. Sin cómputos, nueva ruta o cambios en papers.

### 17.6. La energía E_y no domina el daño no resonante uniformemente

**PROVED, misma fecha y entrada.** Propuesta root, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS para los límites y alcances siguientes, incluida la extensión a y=0. Consultados los tres índices,§16.5 y§17.5; cotejo dirigido sin antecedente literal localizado para Off_y/E_y. Fijar PRIMERO y∈[0,pi/4) y DESPUÉS k tender a infinito. Abreviar A_y(k,l)=A(z_k,conjugado(z_l)) y Off_y=A_y-R_res,y, sin asignar signo a ninguna de las dos matrices completas.

Para un solo índice k=d a², las diagonales exactas de(DIV-LOWER) y de la parte resonante son

    e_k=E_y[delta_k]=sqrt(k)sum_(n>=1)I_(kn²),
    r_k=R_res,y(k,k)
       =sqrt(k)sum_(n>=1)[J_(kn²)+log(k)I_(kn²)].

El cambio u=lambda+s en los integrales de I,J, con y fijo, da

    I_lambda=H(lambda)/[4pi epsilon lambda^(3/2)]
                       *[1+O_y(1/lambda)],
    J_lambda/I_lambda=O_y(1/lambda),
    sum_(n>=2)I_(kn²)/I_k=O_y(exp(-6pi epsilon k)).

Estas cotas no derivan un resto asintótico: se escribe H(u)/(2u)=p_y(u)exp(-2pi epsilon u), con p_y(u) comparable a u^(7/2) y derivada logarítmica O_y(1/u) para u grande. Tras u=lambda+s, el cociente p_y(lambda+s)/p_y(lambda) tiene error acotado por C_y s(1+s)^M/lambda; se integra contra exp(-2pi epsilon s). Para J se usa log(1+s/lambda)<=s/lambda. La cola en n se acota por C_y sum_(n>=2)n6 exp[-2pi epsilon k(n²-1)], que da la última fórmula. En particular

    r_k/e_k=log k+O_y(1/k).

La cola theta COMPLETA de§16.5 es O_y(exp(-3pi epsilon k)) relativa al primer modo, uniformemente en r>=0. Su contribución a A_y(k,k) respecto del cuadrado de ese modo tiene ese mismo error relativo, pues el peso diagonal es positivo. La cola de cuadrados de modos en r_k tiene error relativo O_y(exp(-6pi epsilon k)). Por tanto

    Off_y(k,k)/e_k=O_y(log k exp(-3pi epsilon k))->0,
    A_y(k,k)/e_k=log k+o(1).

Los enteros consecutivos k,l=k+1 tienen distintas partes libres de cuadrados. Así E_y y R_res,y tienen cruce0 en ese par, mientras Off_y(k,l)=A_y(k,l). La correlación de§16.5, con error O_y(1/k), implica

    |A_y(k,k+1)|/sqrt(e_k e_(k+1))=log k+o(1).

En y=0 no se invoca§16.5 fuera de su enunciado: su prueba de extremo se aplica directamente con epsilon=1,sigma=0,E=k+l>0. La cola completa sigue siendo O(exp(-3pi k)), y la misma integral D_kl da A_0(k,l)/[Phi(x_k)Phi(x_l)]=(x_k+x_l)/[2pi(k+l)]*(1+O(1/k)). Esto prueba también la correlación necesaria en y=0. Allí A_0(k,l)>0 y pueden elegirse los coeficientes reales con signos(+,-).

Elegir c^(k) con dos entradas de módulos (2e_k)^(-1/2),(2e_(k+1))^(-1/2) y fase que haga negativo el cruce de A_y. Entonces

    E_y[c^(k)]=1,
    Off_y[c^(k)]
       =(1/2)[Off_y(k,k)/e_k+Off_y(k+1,k+1)/e_(k+1)]
             -|A_y(k,k+1)|/sqrt(e_k e_(k+1))
       =-log k+o(1)->-infinito,
    R_res,y[c^(k)]=log k+o(1),
    A_y[c^(k)]=o(1),
    A_y[c^(k)]/R_res,y[c^(k)]->0.

No existe C_y finito tal que Off_y>=-C_y E_y sobre todos los bloques enteros. Tampoco existe delta_y>0 con A_y>=delta_y R_res,y uniformemente, o equivalentemente Off_y>=-(1-delta_y)R_res,y. Ambas constantes podrían depender de y y aun así fallan ya en estos pares, INCLUIDO y=0. Esto limita el pago mediante el margen E_y y la perturbación estrictamente menor que R_res; NO prueba A negativo ni decide la desigualdad crítica Off_y>=-R_res,y. En y=0 los pares reales son SPD por§9 y estos vectores tienen A_0[c^(k)]>0, aunque su cociente con R_res,0 tienda a0. La SOS de§17 y su lower(DIV-LOWER) siguen válidos. Sin nuevo principio general de imposibilidad, ruta, cómputos, ventana W/T ni papers editados.

### 17.7. La cota logarítmica escalar falla también en el portador theta exacto

**PROVED, misma fecha y entrada.** Construcción root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Cotejo previo: phase199 [PROOF_L_SHARP_C_001§4, Prop4.2](../phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_C_001.md) ya demuestra no acotación del mapa directo de dilataciones en L²; [PROOF_L_SHARP_E_001§3, Rem3.1](../phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_E_001.md) ya contiene el operador de peine mediante el conmutador divisorial. [BRIDGE002§3](POWER_BRIDGE_002.md) usa aproximación C1 por polinomios, [AUDIT_L_SHARP_1§2.4](../phase-199-frontier-pattern/proof-L-sharp/AUDIT_L_SHARP_1.md) usa inversión Möbius compacta en otro mapa y019§§3–5 conserva el límite de invertir medias. No se presenta la no acotación de dilataciones como principio nuevo. La diferencia acotada es comprobar ESTA desigualdad cuadrática con peso logarítmico sobre agregados theta EXACTOS, usando densidad en una norma donde el operador sí es continuo.

Aquí y=0, t>=1. Definir T_mF(t)=F(mt), de modo que T_m²F(t)=F(m²t), y

    C=sum_(m>=2) Lambda(m)m^(-1/2) T_m²,
    Theta_k(t)=Phi((log(kt))/2), k entero positivo,
    Q_C(F)=integral_1^infinito (CF)(t)conjugado(F(t))dt/(2t),
    W(F)=integral_1^infinito (1+log t)|F(t)|²dt/(2t).

NO existe M finito tal que |Q_C(F)|<=M W(F) para todos los F de la envolvente compleja FINITA de los Theta_k.

**Continuidad en una norma fuerte y densidad del portador.** Para 0<gamma<2pi, usar el espacio EXPONENCIAL

    H_gamma=L²([1,infinito), exp(gamma t)dt/t).

No es un peso de potencia. El cambio u=m²t da

    ||T_m²F||_(H_gamma)²
       =integral_(m²)^infinito exp(gamma u/m²)|F(u)|²du/u
       <=exp[-gamma(m²-1)]||F||_(H_gamma)².

Luego C es acotado en H_gamma, pues sum_(m>=2)Lambda(m)m^(-1/2)exp[-gamma(m²-1)/2] converge. Q_C y W son formas continuas en H_gamma; para W se usa 1+log t<=C_gamma exp(gamma t). Los Theta_k pertenecen a ese espacio por su cola gaussiana completa.

Poner h(u)=pi u^(5/4)(2pi u-3)exp(-pi u). La expansión theta y su inversión, convergentes absolutamente en H_gamma, son

    Theta_k(t)=sum_(n>=1)n^(-1/2)h(kn²t),
    h(kt)=sum_(n>=1)mu(n)n^(-1/2)Theta_(kn²)(t).

La convergencia en norma se sigue de los bounds polinomiales por exp(-c_gamma kn²) para las normas de esos sumandos; también justifica reagrupar la inversión por sum_(n|j)mu(n). Así la clausura del span theta contiene cada h(kt).

Para G suave de soporte compacto en[1,infinito), poner g(t)=G(t)/(pi t^(5/4)) y

    L=-2t(d/dt)-3,
    P(t)=(1/2)t^(-3/2)integral_t^infinito s^(1/2)g(s)ds.

Entonces LP=g y P es suave y nula para t suficientemente grande. Con x=exp(-pi t), Q(x)=P(t)/x es suave en[0,exp(-pi)] y nula cerca de0. Aproximar Q en C1 por polinomios Q_N da

    pi t^(5/4)L[xQ_N(x)] -> G en H_gamma.

Cada aproximante es una combinación FINITA de h(kt): para el monomio x^k, pi t^(5/4)Lx^k=k^(-5/4)h(kt), k>=1. El error está acotado por C eta_N t^(5/4)(1+t)exp(-pi t), con eta_N->0, integrable en H_gamma porque gamma<2pi. La densidad de funciones suaves compactas completa la prueba de que el span theta finito es denso en H_gamma. No se confunde esta norma con el espacio B de BRIDGE002 ni con el mapa compacto de phase199.

**Contradicción con mesetas reales.** Una cota |Q_C|<=M W válida en el span theta se extendería por esas dos continuidades a TODO H_gamma. Para R>1, el test F_R=1_[1,R] pertenece a H_gamma y da exactamente

    Q_C(F_R)=(1/2)sum_(2<=m<=sqrt R)
                       Lambda(m)m^(-1/2)log(R/m²),
    W(F_R)=(1/2)log R+(1/4)(log R)².

Para R grande, restringir la suma no negativa a m<=R^(1/4) da Q_C(F_R)>=(log R/4)sum_(m<=R^(1/4))Lambda(m)/sqrt m. La cota elemental psi(X)>=cX para X grande implica que esto es>=c'R^(1/8)log R. Puede obtenerse dicha cota sin datos externos: para N=floor(X/2), psi(X)>=log binom(2N,N)>=2Nlog2-log(2N+1), comparando las valuaciones en primos del binomio con las potencias primas hasta2N. También sum_(m<=X)Lambda(m)/sqrt m>=psi(X)/sqrt X. Por tanto Q_C(F_R)/W(F_R) tiende a infinito.

El orden es fijar R, aproximar F_R en H_gamma por agregados theta y pasar la hipotética desigualdad al límite; DESPUÉS hacer R tender a infinito. No se necesita aproximación uniforme en R ni se afirma que F_R sea ya un agregado finito. Esto refuta sólo esta cota escalar logarítmica del operador C sobre el portador theta declarado. No controla el resto no resonante por R_res, no demuestra A negativo ni altera el signo objetivo; no certifica ventana W/T. Sin nueva ruta, campañas, archivos auxiliares ni cambios en papers.

### 17.8. Los resolventes conjugados no son todos acretivos en la métrica física

**PROVED, misma fecha y entrada.** Construcción root/joint_sign_fresh_review; verificación independiente global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Cotejo dirigido en los tres índices y corpus sin este ejemplo literal localizado. Antecedentes: [phase199 E§3, Rem3.1](../phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_E_001.md) y [phase188 N_BUILD_007](../phase-188-closing-D/N_BUILD_007_CONE_ORDER_ON_A_T.md)/[N_BUILD_018](../phase-188-closing-D/N_BUILD_018_LINEAR_CENTRE_REDUCES_TO_OMEGA_MU.md) tratan operadores de peine, otros núcleos y órdenes de cono; no prueban acretividad de ESTA conjugación en ESTA métrica. No se propone una imposibilidad general de métodos de resolventes.

En t>=1, poner

    T=pi t^(5/4)[-2t(d/dt)-3], A0=-d/dt,
    (R_s f)(t)=integral_t^infinito exp[-s(u-t)]f(u)du, s>0,
    T^(-1)F(t)=(1/(2pi))t^(-3/2)
                           integral_t^infinito u^(-3/4)F(u)du,
    Rtilde_s=T R_s T^(-1).

La inversa es la solución con lim_(t->infinito) t^(3/2)P(t)=0, condición que excluye la solución homogénea P(t)=constante*t^(-3/2); el peso correcto es u^(-3/4). Se usa el producto físico integral f conjugado(g)dt/(2t), no el de H_gamma. Para f∈C_c^infinito((1,infinito)), integración por partes sin bordes da exactamente

    q=Re<T A0 f,Tf>_fis
      =(pi²/2)[7 integral_1^infinito t^(5/2)|f'|²dt
                      -(9/2)integral_1^infinito t^(1/2)|f|²dt].

Con f(t)=t^(-3/4)u(log t), u suave de soporte compacto en(0,infinito), esto es

    q=(pi²/2)[7 integral|u'|²dx-(9/16)integral|u|²dx].

Elegir un bump real no nulo u_R(x)=chi(x/R), chi∈C_c^infinito((1,2)), hace q<0 para R suficientemente grande: las dos integrales escalan como R^(-1) y R. Fijar entonces 0<s<-q/||Tf||_fis² y v=T(A0+s)f. La identidad R_s(A0+s)f=f implica

    Rtilde_s v=Tf,
    Re<Rtilde_s v,v>_fis=q+s||Tf||_fis²<0.             (RES-NEG)

**Transferencia al span theta finito.** No basta densidad en una norma donde el operador sea discontinuo. Usar exactamente H_gamma exponencial de§17.7, 0<gamma<2pi. La fórmula integral de la conjugación es

    Rtilde_s F(t)=t^(3/4)integral_t^infinito v^(-3/4)F(v)dv
      -(1/2)t^(5/4)(2st+3)
          *integral_t^infinito exp[-s(u-t)]u^(-3/2)
                       integral_u^infinito v^(-3/4)F(v)dv du.

Se obtiene sustituyendo T^(-1) y derivando R_s, primero para datos suaves compactos, donde todos los intercambios son absolutos. La conjugación unitaria U_gamma F(t)=exp(gamma t/2)t^(-1/2)F(t) lleva H_gamma a L²(dt). Con r=v-t>=0, los módulos de los núcleos transformados de los dos términos se acotan respectivamente por

    exp(-gamma r/2),
    (s+3/2)r exp(-gamma r/2).

Para el segundo se usa integral_t^v exp[-s(u-t)]u^(-3/2)du<=r t^(-3/2), junto con (t/v)^(1/4)<=1 y t>=1. La cota de convolución por la norma L1 de esos núcleos da

    ||Rtilde_s||_(H_gamma -> H_gamma)
        <=2/gamma+4(s+3/2)/gamma².

Así la fórmula define una extensión acotada, que coincide con la conjugación también sobre los agregados theta suaves con decaimiento exponencial. Su forma cuadrática física es continua en H_gamma. Aproximar el v real de(RES-NEG) por agregados theta FINITOS reales, mediante la densidad de§17.7, conserva la desigualdad estrictamente negativa. Por tanto existe también un agregado theta finito con Re<Rtilde_s F,F>_fis<0; no se afirma que v mismo sea ya uno de ellos.

**Alcance.** Se refuta sólo la afirmación de que TODOS estos Rtilde_s sean acretivos en el producto físico sobre el portador declarado. La representación integral pertinente del logaritmo contiene MENOS R_s; por tanto(RES-NEG) NO es un falsificador de positividad del logaritmo conjugado. No excluye el método de resolventes completo, otro producto interno ni un balance conjunto con C; no prueba A negativo, un control del término no resonante o el signo global. Sin nueva ruta, cómputos, archivos auxiliares, cobertura W/T ni cambios en papers.


## 18. El A completo sobre escalas enteras basta para todos los nodos reales

**PROVED, 2026-11-06.** Construcción independiente root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Consultados las reglas del proyecto, los tres índices y corpus; cotejo dirigido sin este puente literal localizado. [BRIDGE002§3](POWER_BRIDGE_002.md) ya usa aproximación polinómica C1 en una variable exponencial; [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md) y [SCALAR_BRIDGE017](POWER_SCALAR_BRIDGE_017.md) transfieren otras familias racionales. La densidad de§17.7 controla F en H_gamma, pero NO por sí sola el segundo término G de la forma completa. Aquí se aproxima simultáneamente el par(F,G), usando una norma de dos derivadas antes de aplicar el operador logarítmico y C. No se atribuye novedad al instrumento polinómico ni a la inversión Möbius.

**Enunciado.** Para la Phi real, son equivalentes:

1. A(.5log k,.5log l) es PSD para TODOS los bloques finitos de enteros positivos k,l.
2. A(x,z) es PSD para TODOS los bloques finitos de nodos reales x,z.

La segunda afirmación implica la primera por restricción. Para la dirección restante se conserva el A COMPLETO en y=0, incluidos todos los pares de frecuencias diferentes.

### 18.1. Identidad de grafo para toda escala positiva

Para t>=1 y kappa>0 definir

    P_kappa(t)=kappa^(5/4)sum_(n>=1)n² exp(-pi kappa n²t),
    Theta_kappa(t)=Phi(.5log(kappa t)),
    T=pi t^(5/4)(-2tD-3),
    Lg P(t)=integral_0^infinito
                    [exp(-pi r)P(t)-P(t+r)]dr/r,
    F(P)=TP,   G(P)=(1/2)T Lg P-C TP,
    (CF)(t)=sum_(m>=2)Lambda(m)/sqrt(m) F(m²t).

Frullani sobre cada exponencial da Lg[exp(-pi b t)]=log b exp(-pi b t). Las series de P_kappa y sus derivadas convergen absolutamente con colas gaussianas, también con factores log n. Por tanto

    F(P_kappa)=Theta_kappa,
    G(P_kappa)=(1/2)log(kappa)Theta_kappa.           (GRAPH)

En efecto, el término adicional de (1/2)T Lg P_kappa tiene coeficiente log n en el modo n. En C Theta_kappa el cambio n=mj produce exactamente sum_(m|n)Lambda(m)=log n, que lo cancela. No se suprimen modos ni se estima su signo por separado.

Si P=sum_i c_i P_(kappa_i), x_i=.5log kappa_i, el cambio t=exp(2r) en A da exactamente

    sum_ij c_i conjugado(c_j) A(x_i,x_j)
      =integral_1^infinito
          [log t |F(P)|²+2Re(G(P)conjugado(F(P)))]dt/(2t).
                                                        (A-GRAPH)

### 18.2. Continuidad que conserva ambos términos

Fijar una lista FINITA de kappa_i>0 y elegir

    0<a<pi min(1,min_i kappa_i),  0<gamma<2a,
    ||P||_(a,2)=max_(0<=j<=2) sup_(t>=1) exp(at)|P^(j)(t)|.

Partir Lg en r<1 y r>=1. Para j=0,1, el numerador pequeño es a lo sumo r(pi+1)exp(-at)||P||_(a,2); el grande se domina por exp(-at)[exp(-pi r)+exp(-ar)]||P||_(a,2). Esto justifica derivar bajo la integral y prueba

    ||Lg P||_(a,1)<=C_a||P||_(a,2),
    C_a=pi+1+exp(-pi)/pi+exp(-a)/a.

Así |TP(t)|<=5pi t^(9/4)exp(-at)||P||_(a,2), y la misma cota con factor C_a vale para T Lg P. La integral de t^(7/2)exp[-(2a-gamma)t] sobre[1,infinito) es finita. Junto con C acotado en H_gamma=L²(exp(gamma t)dt/t) por§17.7, resulta continuidad

    P en B_a² -> (F(P),G(P)) en H_gamma x H_gamma.

El peso 1+log t está dominado por una constante por exp(gamma t). Cauchy–Schwarz prueba que la forma del lado derecho de(A-GRAPH) es continua en ese par de normas. No se presupone PSD de A.

### 18.3. Aproximación por escalas enteras en la norma de grafo

Cada target P=sum_i c_i P_(kappa_i) tiene exp(at)P^(j)(t)->0 para j=0,1,2. Cortarlo suavemente en t grande lo aproxima en B_a²: las derivadas del corte se controlan y las colas ponderadas tienden a cero. Este paso se afirma para ESTOS targets, no para cualquier elemento de B_a².

Para el corte suave P_c, poner x=exp(-pi t) y Q(x)=P_c(t)/x. Q se prolonga suavemente por cero cerca de x=0 en[0,exp(-pi)]. Aproximar Q en C² por polinomios Q_N: aproximar Q'' uniformemente e integrar dos veces ajustando Q(0),Q'(0). Entonces P_N(t)=x Q_N(x) es una combinación FINITA de exp(-pi k t), k entero positivo, y

    |D^j(P_N-P_c)(t)|<=C eta_N exp(-pi t),
    j=0,1,2,  eta_N->0.

Como a<pi, hay convergencia B_a². Para levantar cada exponencial usar la identidad exacta

    exp(-pi k t)=k^(-5/4)
          sum_(n>=1)mu(n)/sqrt(n) P_(kn²)(t).       (MOB-P)

Al expandir P_(kn²), el coeficiente del modo j es j² sum_(n|j)mu(n), que sólo conserva j=1. La serie es ABSOLUTA en B_a², pues para K>=1

    ||P_K||_(a,2)<=C_a' K^(13/4)exp(-pi K)

por las cotas gaussianas de las series de n²,n4,n6 y a<pi. Truncar(MOB-P) produce combinaciones FINITAS de P_k enteros. Una selección sucesiva de corte, polinomio y truncaciones da P_l en span FINITO de los P_k enteros con P_l->P en B_a². En particular convergen simultáneamente F(P_l),G(P_l) en H_gamma.

### 18.4. Transferencia de la desigualdad y alcance

Bajo la hipótesis1, la forma(A-GRAPH) es no negativa para cada P_l entero. Por continuidad lo es para cualquier lista finita de kappa_i>0 y coeficientes complejos. Como x_i=.5log kappa_i recorre TODA R, se prueba2.

Así no queda una puerta de transferencia adicional entre el A COMPLETO sobre todos los enteros y el A real global. Combinado con§2 y los puentes K de [CONE001](POWER_CONE_001.md)/[BRIDGE002](POWER_BRIDGE_002.md), probar ese signo entero completo es suficiente para el objetivo declarado; la recíproca para el objetivo lambda_A(T)>=0 para TODOS T se verifica posteriormente en§18.9; no se identifica ningún mínimo a T fijo. La SOS de§17 sólo firma R_res: el control conjunto de la parte no resonante, o directamente el signo completo entero, sigue OPEN. No se transfiere por separado R_res ni se obtiene nueva ventana W/T, positividad global o cambio en papers.


### 18.5. La conjugación T no conserva tasas positivas de salto

**PROVED, alcance específico.** Root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Cotejados los tres índices y [106_31](../phase-106-global-modular-star-audit/106_31_FULL_KERNEL_DOOB_VARIANCE_IDENTITY.md), [ROUND005D](ROUND_005_D.md) y [L2_BUILD008](../phase-188-closing-D/L2_BUILD_008_GROUND_STATE_AND_T0.md): éstos tratan otras formas, transformaciones de ground state y métricas, sin esta conjugación T ni el núcleo siguiente. No se encontró el enunciado literal en ese cotejo.

Escribir D_(m²)P(t)=P(m²t) y

    B=Lg-2sum_(m>=2)Lambda(m)m² D_(m²),  p=P_1>0.

Por la misma identidad modal sum_(m|n)Lambda(m)=log n de(GRAPH), Bp=0. Para P=pf con f suave de soporte compacto en[1,infinito), sin exigir f(1)=0, antes de aplicar T existe la identidad exacta de tasas positivas

    B(pf)(t)=integral_0^infinito
                    p(t+r)[f(t)-f(t+r)]dr/r
       +2sum_(m>=2)Lambda(m)m²p(m²t)[f(t)-f(m²t)].

Esto no asegura su conservación tras la conjugación diferencial. Definir U_rP(t)=P(t+r). Sustituir la inversa terminal ponderada de§17.8 y derivar da

    (T U_r T^-1 F)(t)=(t/(t+r))^(9/4)F(t+r)
       -(3/2)r t^(5/4)(t+r)^(-5/2)
                         integral_(t+r)^infinito v^(-3/4)F(v)dv.

Para F suave con soporte separado de t, el término local de Lg no contribuye y los intercambios son absolutos. Integrar el segundo término en r, usando

    (3/2)integral_0^(v-t)(t+r)^(-5/2)dr
                       =t^(-3/2)-v^(-3/2),

y combinarlo con el traslado produce el núcleo respecto de dv

    (T Lg T^-1 F)(t)=integral_t^infinito K(t,v)F(v)dv,
    K(t,v)=t^(-1/4)v^(-3/4)
                    -t^(5/4)v^(-5/4)/(v-t).        (JUMP-K)

Esta fórmula se usa sólo para soportes separados, sin imponer una renormalización diagonal. Con w=v/t,

    K(t,v)=t^-1 w^(-5/4)[sqrt(w)-1/(w-1)]>0
                       cuando 2<w<3.

Además T[m²D_(m²)]T^-1=m^(-1/2)D_(m²), luego TBT^-1=T Lg T^-1-2C. Elegir t0=2 y F>=0 suave no nula, de soporte compacto en(9/2,11/2). Entonces F es cero cerca de2 y CF(2)=0, pues 2m²>=8 para m>=2. Por(JUMP-K),

    (TBT^-1F)(2)=integral_(9/2)^(11/2)K(2,v)F(v)dv>0.

Fijar la convención de la representación que se refuta:

    (JF)(t)=integral[F(t)-F(v)]nu_t(dv)+V(t)F(t),
    nu_t>=0,

con V local finito. Para este test F(2)=0, cualquier operador de esa clase satisface JF(2)<=0; el killing local no cambia ese valor. Por tanto TBT^-1 NO admite esa representación de tasas positivas sobre el portador suave declarado. Conjugar además por Theta_1(t)=Phi(.5log t)>0 tampoco cambia el signo fuera de la diagonal: usar el test F/Theta_1. Todo se conserva en t>=1; no se elimina el borde inferior.

**Alcance.** Sólo falla el atajo de conservar tasas positivas DESPUÉS de T (también tras esa conjugación positiva). No se demuestra negatividad de la forma cuadrática Q o A, ni una imposibilidad para toda transformación Doob, otra métrica o el tratamiento conjunto del operador. El signo completo entero y, por§18, real global sigue OPEN. Sin nueva ruta, campañas, archivos auxiliares, ventana W/T ni cambios en papers.


### 18.6. El borde complejo de§16 no da un principio mínimo directo

**PROVED, alcance específico.** Propuesta root, verificaciones independientes global_restart_checked/arithmetic_fresh_candidate PASS y root PASS. Leídos los tres índices,§§2.2,16 y [OUTER088](POWER_THETA_DENSITY_OUTER_088.md); cotejo dirigido sin transporte literal resuelto localizado. Para desplazamientos reales fijos x_i, poner

    A_ij(x,y)=integral_x^infinito w_ij(s)P_ij(s,y)ds,
    w_ij(s)=x_i+x_j+2s,
    P_ij(s,y)=Phi(x_i+s+iy)conjugado(Phi(x_j+s+iy)).

En |y|<pi/4, las supercolas permiten todas las derivaciones y eliminan los bordes en infinito. Con Delta=partial_x²+partial_y², integrar por partes conservando el borde inferior da exactamente

    Delta A_ij(x,y)
      =4integral_x^infinito w_ij(s)
          Phi'(x_i+s+iy)conjugado(Phi'(x_j+s+iy))ds
         -4P_ij(x,y).                              (PDE-A)

No se asigna signo matricial a esta fuente. Sí se refuta la superarmonicidad requerida por un principio mínimo directo: tomar x_i=x_j=0,y=0,x>=1. Escribir Y(s)=pi exp(2s), p(s)=-Phi'(s)/Phi(s). La fórmula del primer modo y las cotas de cola completa de088 dan p(s)>2Y(s)-6>Y(s) para s>=1 (Y>21). Por tanto

    I=integral_x^infinito 2s p(s)²Phi(s)²ds
      >Y(x)integral_x^infinito 2s p(s)Phi(s)²ds
      =Y(x)[xPhi(x)²+integral_x^infinito Phi(s)²ds]
      >Phi(x)².

Aquí se usó (Phi²)'=-2pPhi², con el borde xPhi(x)² retenido y la cola en infinito nula; xY(x)>1. Así Delta A_ii(x,0)=4[I-Phi(x)²]>0. La función diagonal no es armónica ni superarmónica en ese dominio, y la positividad cerca de y=pi/4 de§16 no puede transportarse a y=0 mediante ese principio mínimo sin otra estimación.

**Alcance.** El umbral de§16 depende de cada bloque fijo; no aporta por sí solo PSD conjunta en un intervalo real abierto, que es la hipótesis de la continuación de§2.2. Esta identidad y este test no prueban una fuente matricial indefinida, Q/A negativo ni una imposibilidad para toda PDE u otro transporte. Sólo falla la premisa de superarmonicidad del atajo declarado; signo conjunto global OPEN. Sin nueva ruta, cómputos, archivos auxiliares, W/T ni papers.


### 18.7. Toda cola entera basta; ningún observable finito sostiene un margen positivo

**PROVED, extensión del puente.** Root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Consultados los tres índices,§18.3 y [DESCENT_AUDIT016§§8–9](POWER_DESCENT_AUDIT_016.md), además de [BRIDGE002§3](POWER_BRIDGE_002.md). El antecedente016 ya prueba densidad de cada cola de otra familia racional y la insuficiencia del signo de sus diagonales para W4; aquí cambian el portador exacto P_k, la norma del grafo completo de A y la conclusión sobre minorantes. No se atribuye novedad al mecanismo abstracto de colas densas.

Fijar un entero K>=1. Para los targets P=sum_i c_i P_(kappa_i) y los parámetros a,gamma de§18.2, se puede efectuar§18.3 usando SÓLO índices k>=K. Tras el corte P_c, escribir

    x=exp(-pi t),  Q(x)=P_c(t)/x^K.

Q es suave y cero cerca de x=0. Aproximarlo en C² por polinomios Q_N da x^KQ_N(x), combinación finita de exp(-pi k t) con k>=K, y errores de derivadas de órdenes0,1,2 acotados por C_K eta_N exp(-pi Kt). Como a<pi<=pi K, convergen en B_a². La inversión(MOB-P) sólo introduce índices kn²>=K y sigue siendo absoluta en esa norma. Por tanto span{P_k:k>=K} aproxima cada target de§18 en B_a² y en el grafo(F,G). No se afirma densidad de compactos en todo B_a² ni uniformidad de las constantes en K.

En particular, PSD de TODOS los bloques de CUALQUIER cola fija k>=K equivale a PSD del A real global, por el mismo paso de continuidad de§18.4. Esto conserva la obligación sobre TODOS los tamaños, no sólo las diagonales tardías.

**Completar un prefijo con energía tendiendo a cero.** Abreviar A_0[c]=sum_kl c_k conjugado(c_l)A(.5log k,.5log l), con soporte finito. Fijar J y cualesquiera c_1,...,c_J. Aplicar la densidad de la cola k>J al target -sum_(k<=J)c_k P_k. Se obtienen completaciones c^(n), todas de soporte finito, con ese MISMO prefijo, tales que

    sum_k c_k^(n)P_k ->0 en B_a²,
    A_0[c^(n)] ->0.                                (TAIL-ZERO)

No se presupone PSD para esta convergencia. Si A_0 fuese PSD, el ínfimo sobre las completaciones de cada prefijo sería exactamente0; sin esa hipótesis no se asigna signo a dicho ínfimo.

Si ell es cualquier funcional lineal no nulo FINITAMENTE soportado sobre los coeficientes, elegir J que contenga su soporte y un prefijo con ell(c)=1. Las colas no lo alteran. Por(TAIL-ZERO), es imposible

    A_0[c]>=delta |ell(c)|² para todos c finitos,
    con delta>0.                                   (NO-FIN-MARGIN)

Por consiguiente, tampoco existe un minorante no trivial sum_k w_k|c_k|² con TODOS w_k>=0 y alguno estrictamente positivo, aunque los pesos decaigan arbitrariamente. La misma razón excluye minorantes diagonales con pesos NO NEGATIVOS sobre los observables divisoriales finitodependientes de§17: f_(d,q) sólo usa índices d a²<=dq², a|q. Basta fijar un prefijo que haga no nulo un observable cuyo peso sea positivo. No se identifican esos f_(d,q) con otras coordenadas d_lambda; basta su dependencia finita.

Como corolario del mismo(NO-FIN-MARGIN), se excluye una identidad ÚNICA compatible para TODOS los soportes

    A_0[c]=sum_alpha w_alpha|ell_alpha(c)|²,
    w_alpha>=0,

con algún sumando no nulo y TODOS los ell_alpha de soporte finito, aunque sus tamaños no tengan cota uniforme: cada sumando positivo sería por sí solo el minorante ya prohibido. Esto NO excluye factorizar cada bloque principal finito por separado; esas factorizaciones no constituyen la identidad única sobre todo el portador. [FIXED_BLOCK_ASSEMBLY](POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md) ya excluye ensamblajes de tamaños uniformemente acotados para otro kernel; aquí la obstrucción afecta a cualquier observable local fijo de esta identidad global.

**Alcance.** Resultado para el A COMPLETO en y=0, no una extensión automática a todo y complejo. Refuta márgenes positivos sobre observables de soporte finito y sus energías diagonales no negativas; no excluye energías de observables globales continuos ni sumas de cuadrados no diagonales que los conserven. No prueba A negativo ni el signo global, que sigue OPEN. Sin nueva ruta, cómputos, archivos auxiliares, W/T ni cambios en papers.


### 18.8. Ningún momento exponencial real individual da un minorante positivo

**PROVED, corolario específico.** Root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Cotejados los tres índices,§§8.4,18, [BRIDGE002](POWER_BRIDGE_002.md), [106_31](../phase-106-global-modular-star-audit/106_31_FULL_KERNEL_DOOB_VARIANCE_IDENTITY.md), [ROUND005D](ROUND_005_D.md) y [106_36](../phase-106-global-modular-star-audit/106_36_JOINT_COMPLEMENT_AND_EXPANDER_GATE.md), sin este enunciado literal localizado. Las identidades de capacidad/varianza y continuidad anteriores tienen otros objetos;§8.4 altera la densidad y cancela un momento, mientras aquí se conserva la Phi exacta y se refuta un minorante de rango uno.

Para sigma REAL fijo y coeficientes finitos definir

    ell_sigma(c)=integral_0^infinito exp(sigma u)
                     sum_k c_k Phi(.5log k+u)du
                =(1/2)integral_1^infinito F(t)t^(sigma/2)dt/t.

Este funcional es continuo en H_gamma para todo gamma>0, pues Cauchy–Schwarz da

    |ell_sigma(F)|²<=(1/4)||F||_(H_gamma)²
                         integral_1^infinito t^(sigma-1)exp(-gamma t)dt,

con integral finita. Si A_0[c]>=delta|ell_sigma(c)|² para TODOS los c finitos y algún delta>0, la aproximación del grafo de§18 conservaría también ell_sigma, transfiriendo la desigualdad a cualquier nodo real x. Tomar x=-R, definir F_x(t)=Phi(x+.5log t)=Theta_(exp(2x))(t), y usar la paridad positiva de Phi:

    A(-R,-R)=d(R)=2integral_R^infinito sPhi(s)²ds,
    ell_sigma(F_(-R))
       =exp(sigma R)integral_(-R)^infinito exp(sigma s)Phi(s)ds
       ~Z_sigma exp(sigma R),
    Z_sigma=integral_(-infinito)^infinito exp(sigma s)Phi(s)ds>0.

Las supercolas de Phi dan d(R)exp(CR)->0 para TODO C real fijo. Por ello

    A(-R,-R)/|ell_sigma(F_(-R))|² ->0,

contradiciendo cualquier delta>0. Esto vale incluso para sigma<0, cuando el momento del nodo también tiende a0: d(R) decrece más rápido que toda exponencial.

**Alcance.** Sólo se excluyen minorantes positivos por un momento exponencial REAL individual del portador exacto. No se excluyen momentos firmados generales, combinaciones con cancelaciones u observables globales distintos, ni se demuestra A negativo. No se afirma ningún resultado para sigma complejo ni un test espectral. Signo global OPEN, sin nueva ruta, cómputos, archivos auxiliares, W/T ni papers.


### 18.9. Equivalencia del objetivo para todas las ventanas y restricciones primitivas exactas

**PROVED como alcance, no como signo.** Root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Releídos las reglas del proyecto, los tres índices, las definiciones eq:form, eq:W y eq:target del [Paper47](../../04-papers/47-row-d-dual-certificates/main.tex), [BRIDGE002](POWER_BRIDGE_002.md), [CONFLUENT_BRIDGE014§3](POWER_CONFLUENT_BRIDGE_014.md) y el lema YA probado en [GLOBAL, Comparaciones primitivas](POWER_GLOBAL_ROUTE_REVIEW.md). El nuevo alcance es aplicar ese lema a D=M_Phi mismo y verificar el paso desde las ventanas primitivas a sus mezclas causales; no se presenta un principio analítico nuevo ni una prueba de positividad.

Son equivalentes los siguientes objetivos globales:

1. lambda_A(T)>=0 para TODO T>0, con los dos momentos Tate y el dominio logarítmico declarados en Paper47.
2. K_(M_Phi)(u,v)=[M_Phi(u)+M_Phi(v)]/(u+v) es PSD en todos los tamaños.
3. A es PSD sobre todos los nodos reales.
4. A(.5log k,.5log l) es PSD sobre todos los bloques de enteros positivos; equivalentemente, sobre todos los bloques de cualquier cola fija de éstos.

Las equivalencias2–3 y3–4 son§§2.1,18,18.7. La implicación2=>1 es la suficiencia de CONE001/BRIDGE002, conservando la forma completa antes de restringir al subespacio primitivo.

**Recíproca1=>2 sin cambiar de problema.** Usar la mezcla causal

    f(r)=sum_i d_i exp(-u_i r),  r>=0, u_i>1/2,
    sum_i d_i/(u_i-1/2)=sum_i d_i/(u_i+1/2)=0.

Ésta es la función física causal que entra en W, no una identificación automática con el dato exterior h=Zrho de otra convención. Elegir 1/2<eta<min_i u_i. Cortar f suavemente sólo en infinito converge en H_eta de014. Los dos errores de momentos tienden a0. Elegir dos bumps suaves fijos interiores de la semirrecta, con matriz de momentos exp(±r/2) invertible, y corregir esos errores mediante coeficientes que tienden a0. Resultan funciones causales compactas f_R, EXACTAMENTE primitivas y convergentes a f en H_eta.

No se exige f_R(0)=0. La extensión por cero de H¹ en la semirrecta pertenece continuamente a H^s(R) para0<s<1/2, incluso con ese salto, y por tanto al dominio logarítmico del Paper47. Trasladar cada soporte compacto dentro de algún I_T conserva los dos momentos nulos y W; sobre primitivos W=a_T. La hipótesis1 da W[f_R]>=0. Continuidad014 permite pasar al límite: W[f]>=0.

La identidad CONE001 es W[f]=sum_ij d_i conjugado(d_j)K_(M_Phi)(u_i,u_j). Se ha probado por tanto PSD de K sobre TODOS los bloques sujetos a esas dos restricciones. M_Phi=Z'/Z es impar y real-analítica en toda R porque Phi es par y Z es estrictamente positiva sobre R. Aplicar el lema de GLOBAL con c=1/2,D=M_Phi: congruencia por u²-c², dos anclas, continuación analítica y filas nulas en±c convierten esa positividad restringida en PSD completa. Esto prueba1=>2.

**Las restricciones en el grafo P son dos condiciones, no tres.** Para cualquier P del portador de§18, integración por partes con la cola nula da exactamente

    ell_sigma(TP)=pi P(1)
       +pi(sigma/2-1/4)integral_1^infinito
                                      t^(sigma/2+1/4)P(t)dt.

Aquí ell_sigma es el momento físico de§18.8. En particular

    ell_(1/2)(TP)=pi P(1),
    ell_(-1/2)(TP)=pi P(1)-(pi/2)integral_1^infinito P(t)dt.

Así los dos momentos Tate equivalen EXACTAMENTE a P(1)=0 e integral_1^infinito P=0. NO imponen P'(1)=0. La preimagen de L2_BUILD008 es otra transformación; sus condiciones de borde no se importan a T.

**Completaciones primitivas con prefijo arbitrario.** El resultado(TAIL-ZERO) de§18.7 permanece válido si se exige que CADA completación sea exactamente primitiva. Para verlo, la aplicación de los dos momentos tiene rango2 sobre los P suaves compactos en[1,infinito): un bump que toca1 con P(1)!=0 y otro interior con integral no nula dan rango2 por la fórmula anterior. Dos bumps sólo interiores no servirían, pues ambos tendrían P(1)=0.

La prueba de densidad de cada cola de§18.7 aproxima también esos dos compactos directamente. Los momentos son continuos en B_a², por lo que se pueden elegir dos vectores FIJOS de soporte finito en la cola cuya matriz de momentos sea invertible. Aproximar -P_prefijo por esa cola; los dos momentos del total tienden a0. Corregirlos con aquellos dos vectores fijos y coeficientes tendiendo a0 impone ambos momentos EXACTAMENTE sin cambiar el prefijo ni la convergencia del grafo a0. Por continuidad, A_0 de las completaciones tiende a0.

En consecuencia, la exclusión de minorantes finitamente soportados y SOS locales compatibles de§18.7 sigue válida sobre el subespacio primitivo. En cambio§18.8 para sigma=±1/2 es allí vacuo porque esos momentos son cero; para otros sigma NO se transfiere automáticamente su falsificador no primitivo.

**Alcance.** Todas las equivalencias anteriores incluyen el cuantificador PARA TODO T y todos los tamaños. No identifican mínimos completos/primitivos ni formularios de una ventana T fija. Son equivalencias internas del problema explícito declarado; no se usa ningún enunciado externo ni se prueba el signo de cualquiera de los objetivos equivalentes. Global OPEN; sin nueva ventana W/T, cómputos, archivos auxiliares ni cambios en papers.


## 19. Primer polinomio térmico primitivo: signo completo de un vector fijo

**PROVED, 2026-11-06.** Construcción fresh_global/root; auditoría matemática independiente arithmetic_fresh_candidate FULLPASS y verificación de root de los factores, la partición de la cola y la corrección del parámetro. Consultados las reglas del proyecto, README de ROUTES-TRIED-INDEX, grid maestro y crucigrama; cotejo dirigido del corpus sin la familia literal siguiente localizada. Antecedentes: el grafo completo de§18, sus restricciones primitivas exactas de§18.9 y la identidad de tasas anterior a T de§18.5. E101_061 trata polinomios de interpolación nodal, no estos polinomios en el tiempo térmico. Las familias gamma/Laguerre físicas previas y las inclinaciones exponenciales no son esta familia.

La diferencia concreta es conservar p=P_1 EXACTO y multiplicarlo por un polinomio real en t, donde t=exp(2r), permitiendo ambos signos. No se trunca la densidad theta para definir el vector. Se firma únicamente el primer vector primitivo de esa familia; este cálculo de signo no afirma una recurrencia positiva entre sus grados. La densidad suficiente de la familia se prueba por separado en§19.8; no se deduce del signo de este vector. Las estimaciones siguientes conservan todas las contribuciones theta y primas mediante cotas de sus colas infinitas. La prueba no necesita un valor decimal de la forma.

### 19.1. Vector, parámetros y restricciones exactas

Para t>=1 poner

    p(t)=sum_(n>=1) n² exp(-pi n²t),
    S_j=sum_(n>=1) n^(-j)exp(-pi n²),
    a=1+(2/pi)S_4/S_2,
    R(t)=(t-1)(t-a),   P(t)=p(t)R(t).

Son series completas, absolutamente convergentes con todas las derivadas usadas. Integrar cada exponencial da

    integral_1^infinito (t-1)p(t)dt=pi^(-2)S_2,
    integral_1^infinito t(t-1)p(t)dt
         =pi^(-2)S_2+2pi^(-3)S_4.

Así a es exactamente la media de t para el peso positivo w(t)=(t-1)p(t), y a>1. El polinomio t-a es el primer polinomio ortogonal no constante para ese peso. Se tienen

    P(1)=0,   integral_1^infinito P(t)dt=0.

Por§18.9, éstos son precisamente los dos momentos Tate de F=TP; no se añade P'(1)=0. La función P y sus derivadas tienen decaimiento exponencial, por lo que pertenecen a los dominios de grafo usados aquí.

Usar, como en§18,

    T=pi t^(5/4)(-2tD-3),
    B=Lg-2sum_(m>=2)Lambda(m)m²D_(m²),
    Q(P)=integral_1^infinito
           [log(t)|TP(t)|²+Re(TBP(t)conjugado(TP(t)))]dt/(2t)
         =Q_log(P)+Q_B(P).

La identidad Bp=0 conserva la cancelación aritmética completa. Además Q_log(P)>=0, simplemente porque t>=1. Se probará Q_B(P)>1/2000.

### 19.2. Expansión exacta de B y normalización modal

Para j=1,2 definir

    D_j(n)=sum_(m|n,m>=2)Lambda(m)(m^(2j)-1).

En particular D_j(1)=0 y

    0<=D_j(n)<=n^(2j)log n,

por sum_(m|n)Lambda(m)=log n. Aplicar§18.5 a R, o expandir las diferencias R(t)-R(t+r) y R(t)-R(m²t), da exactamente

    BP=(a+1-2t)U_1-U_2+2(a+1)tV_1-2t²V_2,
    U_1=pi^(-1)sum_n exp(-pi n²t),
    U_2=pi^(-2)sum_n n^(-2)exp(-pi n²t),
    V_j=sum_n n²D_j(n)exp(-pi n²t).

La fórmula de V_j conserva todos los pares de divisores: reindexar n=mk en la suma inicial por m y k produce el factor n²D_j(n). Equivalentemente,

    BP(t)=sum_(n>=1)exp(-pi n²t)L_n(t),
    L_n(t)=(a+1-2t)/pi-1/(pi²n²)
             +2n²(a+1)tD_1(n)-2n²t²D_2(n).

Poner

    H_n=(2pi n²t-3)R-2tR',
    J_n=(2pi n²t-3)L_n-2tL_n'.

Entonces las dos expansiones, con sus factores distintos, son

    TP=pi t^(5/4)sum_n n²exp(-pi n²t)H_n,
    TBP=pi t^(5/4)sum_n exp(-pi n²t)J_n.

Por tanto

    Q_B(P)=(pi²/2)sum_(n,m>=1)n²
        integral_1^infinito t^(3/2)exp[-pi(n²+m²)t]H_n(t)J_m(t)dt.
                                                        (POLY-QB)

No se introduce un segundo factor m² en J_m. Las cotas polinomiales de D_j y las exponenciales justifican absolutamente esta doble serie, las derivaciones y las integraciones siguientes.

### 19.3. El modo principal y un lower elemental

Escribir a_0=1+2/pi. Primero evaluar sólo el término (n,m)=(1,1) de(POLY-QB) en a=a_0, denotado Q_(B,11)(a_0). Con x=t-1 se obtiene

    H_1=2pi x³+(2pi-11)x²+(10/pi-8)x+4/pi,
    J_1=-4x²+(12/pi-4)x+6/pi-3/pi².

Para I_r=integral_1^infinito t^(r+3/2)exp(-2pi t)dt, integración por partes da

    I_r=exp(-2pi)/(2pi)+(r+3/2)I_(r-1)/(2pi), r>=1.

Expandir H_1J_1 y aplicar esta recurrencia hasta r=5 produce la identidad exacta

    Q_(B,11)(a_0)=(pi²/2)[A I_0-B_0 exp(-2pi)],
    A=(4pi-3)(176pi²-88pi+445)/(128pi⁴)>0,
    B_0=(176pi²-344pi+267)/(64pi⁴).

La convexidad de (1+x)^(3/2) da I_0/exp(-2pi)>=1/(2pi)+3/(8pi²). En consecuencia

    [A I_0-B_0 exp(-2pi)]/exp(-2pi)
      >=(4096pi³+1264pi²+792pi-4005)/(1024pi⁶)
      >120339/1024000.

Aquí bastan 3<pi<22/7 y (22/7)^6<1000. También exp(2pi)<600: las cotas elementales exp(1)<11/4 y

    exp(2/7)<=1+2/7+(2/7)²/[2(1-(2/7)/3)]<4/3

dan exp(2pi)<(11/4)^6(4/3)<600, pues 2pi<44/7. La cota exponencial escrita se deduce de k!>=2*3^(k-2) para k>=2. Se concluye

    Q_(B,11)(a_0)>(9/2)*120339/(1024000*600)>1/1200.
                                                        (POLY-11)

### 19.4. Corrección del parámetro exacto a

Sea delta=a-a_0. La definición mediante S_4/S_2 implica delta<0 y

    |delta|<=(2/pi)sum_(n>=2)n^(-2)exp[-pi(n²-1)]
       <exp(-9)/[6(1-exp(-15))]<1/40000.             (POLY-A)

Se usó n²-1>=3+5(n-2), pi>3 y exp(3)>20. Esta última desigualdad ya resulta de sumar la serie de exp(3) hasta grado8. En particular

    163/100<a<a_0<5/3.

Para TODO parámetro entre a y a_0, los polinomios del primer modo satisfacen, en t>=1,

    |H_1|<=7t³, |J_1|<=4t²,
    |partial_a H_1|<=7t², |partial_a J_1|<=2t.

En efecto partial_a H_1=-(2pi t-3)(t-1)+2t y partial_a J_1=2t-3/pi; las demás cotas siguen directamente de 1<a<2 y 3<pi<22/7. Diferenciar la integral del modo principal, absolutamente convergente, da

    |partial_a Q_(B,11)|
       <=210 integral_1^infinito t^(11/2)exp(-6t)dt
       <210exp(-6)<21/40<1.

Para la desigualdad intermedia, t^(11/2)<=t^6 y la integración por partes finita da

    integral_1^infinito t^6exp(-6t)dt
      =exp(-6)sum_(k=0)^6 6!/[(6-k)!6^(k+1)]<exp(-6).

Por(POLY-A),

    |Q_(B,11)(a)-Q_(B,11)(a_0)|<1/40000.          (POLY-AERR)

### 19.5. Los dos cruces entre los modos 1 y 2

En la tabla siguiente [b_0,...,b_d] significa que el módulo del polinomio en x=t-1>=0 es a lo sumo sum_j b_jx^j. TODAS las cotas son para el parámetro EXACTO a de(POLY-A), no sólo para a_0:

| Polinomio | Coeficientes del mayorante absoluto |
| --- | --- |
| H_1 | [4/3,5,5,44/7] |
| J_1 | [2,1/5,4] |
| H_2 | [4/3,20,5/2,176/7] |
| J_2 | [660,3210,4670,2112] |

Para verificar H_n, con alpha=a-1, sus coeficientes en x son

    [2alpha, -2pi n²alpha+5alpha-4,
                    2pi n²(1-alpha)-7, 2pi n²].

Para J_1 son

    [6/pi-3/pi²+delta(2-3/pi), 12/pi-4+2delta, -4].

Los bounds de(POLY-A), 63/100<alpha<2/3 y 3<pi<22/7 prueban las tres primeras filas. Para la cuarta, D_1(2)=3log2 y D_2(2)=15log2, de modo que

    L_2(t)=(a+1-2t)/pi-1/(4pi²)
                   +24(a+1)log2*t-120log2*t².

Si L_2=l_0+l_1x+l_2x², las desigualdades 2/3<log2<7/10 dan

    37<-l_0<40, 117<-l_1<125, 80<-l_2<84.

Los coeficientes j_k de J_2 son exactamente

    j_0=(8pi-3)l_0-2l_1,
    j_1=8pi l_0+(8pi-5)l_1-4l_2,
    j_2=8pi l_1+(8pi-7)l_2,
    j_3=8pi l_2.

Esos intervalos muestran que todos son negativos y sus módulos son menores que los cuatro números de la tabla.

Denotar por H_i^+,J_i^+ los polinomios de mayorantes de la tabla y poner

    V(x)=[H_1^+(x)J_2^+(x)+4H_2^+(x)J_1^+(x)]
                         *(1+3x/2+3x²/8).

El factor4 es el n² del modo n=2 en TP. La tercera derivada negativa de (1+x)^(3/2) prueba

    (1+x)^(3/2)<=1+3x/2+3x²/8, x>=0.

El producto polinomial racional anterior satisface, exactamente,

    sum_j [x^j]V *j!/15^(j+1)
       =92107822417/664453125<139.

Integrar x^jexp(-15x) da entonces, usando pi²/2<5, 5pi>15 y exp(3)>20,

    |Q_(B,12)+Q_(B,21)|
       <5*139/20^5<1/4500.                         (POLY-12)

No se asigna signo a ninguno de esos cruces; se conserva su coste íntegro.

### 19.6. Resto de la doble serie infinita

De D_j(n)<=n^(2j)log n, a<5/3 y t>=1 se obtienen para n>=2

    |L_n(t)|<=4n^6log(n)t²,
    |L_n'(t)|<=6n^6log(n)t,
    |J_n(t)|<=32n^8log(n)t³.

Por ejemplo, los términos de L_n se acotan por (2/3)t+6n^4log(n)t+2n^6log(n)t²; al dividir por n^6log(n)t², se usa n>=2 y log n>2/3. La derivada se trata igual. Además |R|<=t(t-1), |R'|<=2t y 2pi n²>4 dan |H_n|<=2pi n²t³ para todo n>=1. Por tanto los sumandos F_n de TP y Z_n de TBP satisfacen

    |F_n(t)|<=22n^4t^(17/4)exp(-pi n²t), n>=1,
    |Z_n(t)|<=101n^8log(n)t^(17/4)exp(-pi n²t), n>=2,
    |Z_1(t)|<=13t^(17/4)exp(-pi t).

La última cota usa |J_1|<=4t². Estas son cotas de las series completas, no de un corte elegido numéricamente.

Para N>=2 y d<=9, el cociente entre términos consecutivos de n^dexp(-3n²) es menor que

    (3/2)^9/20^5<1/1000.

Así

    sum_(n>=N)n^dexp(-3n²)
       <(101/100)N^dexp(-3N²).                    (POLY-TAIL)

Para un entero h>=8,

    integral_1^infinito t^(15/2)exp(-pi h t)dt
       <=exp(-pi h)/(pi h-15/2),

por log t<=t-1. El denominador es mayor que22 si h>=10 y mayor que16 si h>=8. Separar ahora los pares restantes de(POLY-QB) en n=1,m>=3; n>=3,m=1; y n,m>=2. Usar log n<=n y(POLY-TAIL), con exp(3)>20. El coste absoluto total es menor o igual que

    (1111/22)(101/100)*3^9/20^10
       +(143/22)(101/100)*3^4/20^10
       +(1111/16)(101/100)²*2^13/20^8
     =11655533623/512000000000000<1/30000.          (POLY-REST)

Los factores1111=22*101/2 y143=22*13/2 incluyen la medida dt/(2t). El último producto incluye TODOS los pares n,m>=2, en particular el par(2,2); no omite cruces entre modos grandes. Las tres clases, junto a(1,1),(1,2),(2,1), particionan toda la doble serie.

### 19.7. Signo y alcance

Combinar(POLY-11), (POLY-AERR), (POLY-12) y(POLY-REST) da

    Q_B(P)>1/1200-1/40000-1/4500-1/30000
            =199/360000>1/2000.

Como Q_log(P)>=0,

    Q(P)>1/2000.                                  (POLY-POS)

Queda firmado ESTE vector primitivo exacto, con todas las contribuciones aritméticas y theta conservadas. El modo principal sólo se utilizó como término de referencia de un bound con cola completa; no se afirmó que fuera un aproximante PSD en todos los órdenes. Las comprobaciones racionales auxiliares de los coeficientes y sumas finitas anteriores fueron reproducidas por el auditor; no interviene una cuadratura decimal en la prueba.

El caso corresponde al primer polinomio ortogonal no constante para w=(t-1)p. No prueba que el resultado se conserve para grados superiores, combinaciones arbitrarias de esos polinomios, ni sus cruces. El cálculo(POLY-POS) tampoco demuestra por sí solo una propiedad de core, una recurrencia, un nuevo menor K de orden fijo, una ventana W/T ni el signo global del Paper47. La propiedad de densidad suficiente se verifica independientemente en§19.8, sin heredar signo en grados superiores. No se ha modificado ningún paper ni creado un archivo de ideas o de cómputo.


### 19.8. Los polinomios por p son un core suficiente; todos sus bloques primitivos equivalen al objetivo global

**PROVED como densidad y alcance, no como signo de la familia.** Construcciones independientes root/fresh_global; auditoría independiente global_restart_checked PASS de la continuación en norma, la corrección primitiva y ambos enlaces físicos. Consultados las reglas del proyecto, los tres índices, [BRIDGE002§3](POWER_BRIDGE_002.md), [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md), [DESCENT_AUDIT016§§8–9](POWER_DESCENT_AUDIT_016.md) y§18. Cotejo dirigido sin esta familia/core literal localizado. Aproximación polinómica y densidad fuerte tienen antecedentes explícitos; cambia el portador a p(t)R(t) con p=P1 exacto y el control simultáneo del grafo(F,G), no sólo una norma física L². No se atribuye prioridad mundial.

**Continuación en B_a² sin separación funcional.** Fijar 0<a<pi y sea V la clausura COMPLEJA de span{p(t)t^j:j>=0} en B_a² de§18.2. Para r=0,1,2, las series theta completas dan |p^(r)(t)|<=C_r exp(-pi t), t>=1: tras retirar exp(-pi t), las sumas restantes se dominan por sum_n n^(2+2r)exp[-pi(n²-1)]. Definir

    H(z)(t)=p(t)exp(zt), Re z<pi-a.

Para un centro z0 de ese semiplano, poner b=pi-a-Re z0>0. Derivando en t hasta orden2, y usando

    sup_(t>=1) exp(-bt)t^j/j! <= b^(-j),

se obtiene para TODOS j>=0

    ||p exp(z0t)t^j/j!||_(a,2)
                         <=C_(z0)(1+b)² b^(-j).

En efecto cada derivada de t^j/j! es t^(j-r)/(j-r)!; los términos con r>j desaparecen. Por tanto la serie Taylor de H en z0 converge en B_a² para |z-z0|<b y coincide con p exp(zt), también tras dos derivadas temporales. En z0=0 sus coeficientes están en V; así H(z) pertenece a V para |z|<pi-a.

Si un intervalo real de parámetros ya tiene H(z) en V, sus derivadas de cualquier orden en un centro interior pertenecen también a V por diferencias finitas y clausura. La serie Taylor en ese centro extiende la pertenencia al disco de radio pi-a-z0. Sucesivos centros reales negativos, separados por (pi-a)/2, dan por discos solapados

    p(t)exp(-nu t) pertenece a V para TODO nu>0.

No se usa Hahn–Banach ni se infiere densidad desde convergencia puntual.

**Compactos y targets declarados.** Para P_c suave de soporte compacto en[1,infinito), poner x=exp(-t) y Q(x)=P_c(t)/(p(t)x). Como p>0 y P_c se anula para t grande, Q es suave en[0,exp(-1)] y cero cerca de0. Aproximar Q en C² por polinomios Q_N. Las funciones p x Q_N(x) son combinaciones finitas de p exp(-nu t), nu enteros positivos, y pertenecen a V. Para derivadas temporales de órdenes0,1,2, el error queda acotado por C eta_N exp[-(pi+1)t], eta_N->0. Así P_c pertenece a V. Cada target finito de§18 tiene sus jets ponderados tendiendo a0 y se aproxima por tales cortes; por clausura pertenece a V y admite aproximantes FINITOS pR en B_a². No se afirma esto para todo B_a²: en particular, no se supone densidad de compactos cuando los jets ponderados no tienden a0.

La continuidad de§18.2 convierte esta aproximación en convergencia simultánea de F=TP y G=.5T LgP-C TP en H_gamma para0<gamma<2a, y por tanto de Q completo.

**Corrección exacta de los dos momentos.** Para un target primitivo P, las condiciones son P(1)=integralP=0 por§18.9. Los aproximantes pR_n tienen errores tendiendo a0 en ambos funcionales continuos de B_a². Corregirlos mediante dos vectores FIJOS p y tp: la matriz de los funcionales(P(1),integralP) tiene determinante

    p(1)[integral_1^infinito t p(t)dt
                              -integral_1^infinito p(t)dt]>0.

Sus coeficientes de corrección tienden a0. Quedan aproximantes primitivos EXACTOS pR_n sin perder la convergencia del grafo. Puesto que p(1)>0, sus polinomios son exactamente

    R_n(t)=(t-1)S_n(t),
    integral_1^infinito w(t)S_n(t)dt=0,
    w(t)=(t-1)p(t)>0 para t>1.

Todos los momentos de w son finitos y su matriz de momentos es definida positiva sobre cada grado. Sean q_j sus polinomios ortogonales mónicos, con q_0=1. Entonces todo S de integral w nula es combinación FINITA de los q_j,j>=1. El portador polinómico primitivo es precisamente span{E_j=p(t)(t-1)q_j(t):j>=1}. El vector de§19.1 es E_1, con q_1=t-a y grado2 de R; el perfil p=P1 de las escalas enteras es otro objeto.

**Equivalencia suficiente y necesaria para todas las ventanas.** Definir la matriz Hermitiana Gamma_ij por polarización de Q(E_i,E_j), con la forma COMPLETA Q, no sólo Q_B. PSD de TODOS los bloques iniciales Gamma_(1..N) equivale a Q>=0 sobre todo el portador polinómico primitivo. A su vez equivale al objetivo lambda_A(T)>=0 para TODO T, como sigue.

Para la suficiencia, tomar un test físico f suave compacto primitivo y trasladarlo a soporte dentro de(0,infinito), conservando Tate y W. Poner F(t)=f(.5log t) y

    P(t)=T^-1F(t)=(1/(2pi))t^(-3/2)
                         integral_t^infinito v^(-3/4)F(v)dv.

Es suave y cero para t suficientemente grande. Además el momento Tate positivo nulo hace P(1)=0; si F se anula cerca de1, también P se anula allí. El otro momento da integralP=0 por§18.9. Así P es un compacto primitivo del dominio anterior. La aproximación polinómica primitiva conserva el grafo completo y da Q(P)>=0 bajo la hipótesis sobre TODOS Gamma. Bajo u=.5log t, Q(P)=W[f], con las constantes y el borde causal verificados en [GLOBAL](POWER_GLOBAL_ROUTE_REVIEW.md), control operativo de§18.5. Por tanto W es no negativa sobre los tests suaves compactos primitivos. Su densidad en el dominio primitivo de cada ventana se obtiene de la densidad del núcleo de forma y corrección de sus dos errores Tate con dos bumps fijos interiores; los momentos son continuos. El paso al límite da lambda_A(T)>=0 para TODO T.

Recíprocamente, si ese objetivo global vale, para cualquier polinomio primitivo P=pR la función física f(u)=(TP)(exp(2u)), u>=0, tiene supercola con todas las derivadas y ambos momentos Tate nulos. Pertenece a H_eta de014 para cualquier eta>1/2. Cortarla sólo en infinito y corregir los momentos con dos bumps físicos fijos produce compactos EXACTAMENTE primitivos convergentes en H_eta. El salto causal en0, si existe, está permitido en el dominio logarítmico; no se impone P'(1)=0. Cada compacto se traslada a alguna ventana y tiene W>=0 por la hipótesis. Continuidad014 da Q(P)=W[f]>=0. Esto firma todos los bloques Gamma y completa la equivalencia.

**Alcance.** Se demuestra que ESTA familia polinómica primitiva es suficiente si se firman TODOS sus grados y cruces; su positividad en todos los tamaños sigue OPEN. El primer vector está certificado en§19.7 y el bloque de dos vectores se certifica separadamente en§19.9. No se hereda signo en el grado siguiente ni en combinaciones a partir de densidad, ortogonalidad de w o de vectores individuales positivos. Tampoco se identifica un mínimo a T fijo ni una nueva ventana W/T. Este puente no incorpora cómputos ni modifica papers.


### 19.9. Bloque primitivo completo de dimensión dos y fallo del signo separado de Q_B

**PROVED mediante certificado racional/Arb con colas analíticas completas, 2026-11-06.** Diseño arithmetic_fresh_candidate/root, revisión matemática previa fresh_global/root; implementación arithmetic_fresh_candidate, auditoría literal del código corregido fresh_global/root y reproducción independiente de root terminada exit0/FULLPASS. Parámetros fijados antes de la ejecución: precisión192 bits,960 paneles iguales de ancho1/64 en[1,16], Taylor de grado40, cuatro modos para encerrar los parámetros y dos modos para las integrales de referencia. No hay búsqueda de parámetros, cuadratura adaptativa ni decisión de signo en coma flotante ordinaria.

Fuentes reproducibles: [verificador](tools/power_thermal_primitive_two_verify.py) y [log](tools/power_thermal_primitive_two_verify.log). SHA256 del verificador CORREGIDO utilizado por constructor y reproducción independiente:

    e589fb2b9d98d76f021418427a903794f17aa629832f400f2154c21add52f170

El certificado mantiene orden41 en cada serie truncada mediante derivadas polinomiales algebraicas exactas y asserts de precisión; no deriva una serie truncada reduciendo su orden. Las cotas siguientes explican todo el presupuesto de error y el alcance del certificado, sin depender sólo de la lectura del log.

**Vectores y parámetros exactos.** Usar x=t-1, p y w=(t-1)p de§19.1. Para j=0,1,2,3,

    mu_j=integral_1^infinito x^j w(t)dt
        =(j+1)! S_(2j+2)/pi^(j+2),
    Delta=mu_2 mu_0-mu_1²>0,
    b=mu_1/mu_0,
    alpha=(mu_3 mu_0-mu_2 mu_1)/Delta,
    beta=(mu_3 mu_1-mu_2²)/Delta.

La estricta positividad de Delta es la varianza no nula del peso positivo w, multiplicada por mu_0². Definir

    R_1=x(x-b),
    R_2=x(x²-alpha x+beta),
    E_1=pR_1,  E_2=pR_2.

El nombre E_i evita confundir estos vectores con el perfil P_1 de las escalas enteras. E_1 coincide con el vector de§19.1, pues a=1+b. Los parámetros de R_2 imponen exactamente

    mu_2-alpha mu_1+beta mu_0=0,
    mu_3-alpha mu_2+beta mu_1=0.

Así E_1,E_2 son los primeros dos vectores de la base primitiva de§19.8, aunque allí se escriban los polinomios ortogonales en t en vez de x. Ambos satisfacen E_i(1)=0 e integral E_i=0. Son linealmente independientes por sus grados2 y3; todo par real no nulo de coeficientes representa una función no nula y exactamente primitiva.

Para encerrar los parámetros se suman los primeros cuatro términos de CADA S_j, j=2,4,6,8. El resto positivo completo satisface

    0<sum_(n>=5)n^(-j)exp(-pi n²)
         <(101/100)5^(-j)20^(-25).

Se usa pi>3, exp(3)>20 y la comparación geométrica de términos consecutivos; el factor101/100 es mayor que1/(1-1/1000). La evaluación con bolas de192 bits, añadiendo ese intervalo positivo ANTES de formar mu,Delta,b,alpha,beta, certifica

    63/100<b<2/3,
    19/10<alpha<48/25,
    3/5<beta<31/50,
    Delta>0.

Toda incertidumbre de estos parámetros permanece dentro de cada coeficiente posterior. No se sustituyen por sus puntos medios.

**Expansión modal y polarización.** Para i=1,2 y n>=1 poner

    L_(i,n)(t)=-sum_(j=1)^3
                  R_i^(j)(t)/[j pi^j n^(2j-2)]
          +2n²sum_(m|n,m>=2)Lambda(m)
                              [R_i(t)-R_i(m²t)],
    H_(i,n)=(2pi n²t-3)R_i-2tR_i',
    J_(i,n)=(2pi n²t-3)L_(i,n)-2tL_(i,n)'.

La suma derivativa termina realmente en el grado de R_i. La identidad Bp=0 y la misma expansión de diferencias de§19.2 dan

    F_i=TE_i=pi t^(5/4)sum_(n>=1)n²exp(-pi n²t)H_(i,n),
    Z_i=TBE_i=pi t^(5/4)sum_(n>=1)exp(-pi n²t)J_(i,n).

La matriz real simétrica completa que se certifica es

    Q_ij=integral_1^infinito
       [log(t)F_i(t)F_j(t)+(F_i(t)Z_j(t)+F_j(t)Z_i(t))/2]
                                                         dt/(2t).
                                                        (BLOCK-Q)

En particular Q(P)=c^t Q c para P=c_1E_1+c_2E_2. Se conserva el promedio simétrico de los cruces; no se sustituye Q_B por una expresión unilateral no simetrizada. Para el diagnóstico de separación se integra además DIRECTAMENTE

    Q_B(E_1+E_2)=integral_1^infinito
                         (F_1+F_2)(Z_1+Z_2)dt/(2t).

**Cotas reales de todos los modos.** Los intervalos de b,alpha,beta prueban para t>=1

    |R_i|<=t³, |R_i'|<=3t², |R_i''|<=6t, |R_i'''|<=6.

Por ejemplo x²-alpha x+beta>=beta-alpha²/4>-1 y su cota superior es menor que x²+1; esto da |R_2|<=t³. Para R_2'=3x²-2alpha x+beta, el término negativo queda acotado por4x<=3t²; las demás derivadas y R_1 satisfacen las cotas escritas directamente.

La parte derivativa de L_(i,n) tiene módulo a lo sumo(38/27)t³. Para n>=2, su derivada tiene módulo a lo sumo(25/12)t². La parte aritmética y su derivada se acotan respectivamente por

    2n²log(n)(1+n^6)t³<=(65/32)n^8log(n)t³,
    6n²log(n)(1+n^6)t²<=(195/32)n^8log(n)t².

Aquí se conservó la diferencia completa R_i(t)-R_i(m²t), usando sum_(m|n)Lambda(m)=log n. Como n^8log n>512/3 para n>=2, se deduce

    |L_(i,n)|<=3n^8log(n)t³,
    |L_(i,n)'|<=7n^8log(n)t²,
    |J_(i,n)|<=23n^10log(n)t^4, n>=2.

Para n=1 bastan |L_(i,1)|<3t²/2 y |L_(i,1)'|<=7t/3. Por las desigualdades racionales verificadas con pi,

    pi(2pi+6)<39, 23pi<73,
    pi(3pi+14/3)<45,

los sumandos modales de F_i,Z_i satisfacen uniformemente para i=1,2

    |F_(i,n)|<=39n^4t^(21/4)exp(-pi n²t), n>=1,
    |Z_(i,1)|<=45t^(21/4)exp(-pi t),
    |Z_(i,n)|<=73n^10log(n)t^(21/4)exp(-pi n²t), n>=2.
                                                        (BLOCK-MODES)

Estas cotas también justifican la convergencia absoluta de las expansiones e integrales de(BLOCK-Q).

**Error por omitir modos n>=3 en la referencia de integración.** Abreviar

    C=101/100,
    T_d(N)=C N^d/20^(N²),
    Sbar_4=1/20+T_4(2).

Para N>=2,d<=11, el cociente entre términos consecutivos de n^dexp(-3n²) es menor que(3/2)^11/20^5<1/1000; por tanto su cola es menor que C N^dexp(-3N²). Todo par omitido tiene h=n²+m²>=10. Las integrales pertinentes satisfacen

    integral_1^infinito t^(19/2)exp(-pi h t)dt
          <=exp(-pi h)/(pi h-19/2)<exp(-3h)/20,
    integral_1^infinito t^(21/2)exp(-pi h t)dt
          <exp(-3h)/19.

Para la segunda se usó log t<=t. Aplicar(BLOCK-MODES) y log n<=n da los presupuestos absolutos, para CADA entrada simetrizada,

    r_B=(39/40)[73 Sbar_4 T_11(3)
                  +45 T_4(3)/20+73 T_4(3)T_11(2)]
       =510613632029241/409600000000000000000
       <1/500000,
    r_log=(1521/19)T_4(3)Sbar_4
       =623421823401/972800000000000000000
       <1/10^9.
                                                        (BLOCK-MODERR)

El primer presupuesto cubre Z de índice>=3 contra todos los F, y F de índice>=3 contra Z de índice1 o>=2. Puede contar dos veces algunos pares, lo cual sólo aumenta el majorante. El promedio de dos términos en Q_B,ij conserva la misma cota r_B. Para la dirección E_1+E_2, el error de Q_B es a lo sumo4r_B. No se elimina ningún par de índices grandes ni un contacto primo-potencia.

**Cola temporal después de16.** Los mismos mayorantes, aún más holgados, dan para cada i

    |F_i(t)|<=663t^(21/4)exp(-pi t),
    |Z_i(t)|<=149549t^(21/4)exp(-pi t).

Se usó Cexp(-9)<1, de modo que las colas relativas se acotan por2^4 y2^11, y 39(1+2^4)=663,45+73*2^11=149549. Estas cotas valen para las series completas y, en particular, para los dos modos retenidos. Para r=10,11,

    integral_16^infinito t^r exp(-6t)dt
       <=16^r exp(-96)/(6-r/16)<16^r/(5*20^32).

Por log t<=t, unos presupuestos válidos para cada entrada son

    e_B=663*149549*16^10/[10*20^32],
    e_log=663²*16^11/[10*20^32],
    e_B+e_log<1/10^20.

Los exponentes enteros10,11 mayoran respectivamente19/2 y21/2 para t>=16. La dirección E_1+E_2 necesita4e_B para su parte Q_B.

**Integración de referencia con resto de Taylor verificado.** Sólo en esta evaluación finita se conservan los modos n=1,2; los errores anteriores pagan todos los demás sobre la semirrecta completa. Para n=2, el único divisor no trivial es2, así que L_(i,2) contiene exactamente8log2[R_i(t)-R_i(4t)]. Su derivada se evalúa algebraicamente como8log2[R_i'(t)-4R_i'(4t)] más la derivada de la parte derivativa. No se reemplaza por diferencias numéricas.

En cada disco complejo de radio1/8 centrado en[1,16] se tienen Re z>7/8, |z|<17, |z-1|<18 y |4z-1|<69. Las ramas principales de log z y z^(5/4) son holomorfas allí. Los intervalos de parámetros anteriores dan

    |R_i(z)|<10^4, |R_i'(z)|<2000,
    |R_i''(z)|<200, |R_i'''(z)|<=6,
    |R_i(4z)|<4*10^5, |R_i'(4z)|<15000.

Denotar por F_i^[2],Z_i^[2] las sumas de referencia con n=1,2 únicamente. Por las fórmulas modales exactas de esos dos modos, usando |exp(-pi n²z)|<1,

    |H_(i,n)|<10^7, |L_(i,n)|<4*10^6,
    |L_(i,n)'|<5*10^5, |J_(i,n)|<3*10^9,
    |F_i^[2](z)|<2*10^11, |Z_i^[2](z)|<10^13.

Además |log z|<4 y |1/(2z)|<1. Por tanto M=10^30 domina el módulo de cada integrando DE REFERENCIA de Q_11,Q_12,Q_22 y del integrando directo de Q_B(E_1+E_2), incluidos sus factores de polarización. Los errores(BLOCK-MODERR) conservan separadamente todos los modos no incluidos en esa referencia. Estos son bounds complejos para los integrandos, no estimaciones reales trasladadas sin prueba.

Los960 paneles tienen ancho1/64 y semiancho1/128. Para el radio de Cauchy1/8, el cociente es1/16. Se integran exactamente los términos pares del polinomio de Taylor de grado40, con aritmética de bolas a192 bits. El error total de truncación queda acotado por

    e_Taylor=15*10^30*(1/16)^41/(1-1/16)<1/10^18.

El verificador construye R_i',R_i'',R_i''' y L_(i,n)' por fórmulas polinomiales exactas. Comprueba explícitamente que los campos F_i,Z_i, los cuatro integrandos y la serie que entra en la integración tienen precisión41 en CADA panel. Así el resto de grado40 corresponde al orden realmente utilizado.

**Inflación y gates finales.** Antes de cualquier comparación de signo se añaden bolas simétricas de radios

    e_Q=r_B+r_log+e_B+e_log+e_Taylor<1/400000,
    e_direction=4r_B+4e_B+e_Taylor.

La incertidumbre de los parámetros ya está incorporada en todos los coeficientes y no se omite de estos intervalos. La ejecución del constructor y la reproducción independiente, con el mismo hash corregido, terminaron exit0/FULLPASS y certificaron

    Q_11>179/100000,
    Q_22>17/10000,
    |Q_12|<79/50000,
    Q_B(E_1+E_2)<-1/20000.

Por aritmética racional exacta,

    det Q> (179/100000)(17/10000)-(79/50000)²
           =2733/5000000000>0.

Luego el bloque COMPLETO Q sobre span{E_1,E_2} es definido positivo: TODA combinación real no nula tiene Q>0. No se restringen los signos de sus dos coeficientes. Al mismo tiempo, E_1+E_2 es exactamente primitivo y tiene Q_B<0. Queda refutada la promoción del signo separado Q_B(E_1)>0 de§19.7 a esta familia bidimensional; la contribución Q_log es necesaria en ese argumento. Esto NO produce un valor negativo de Q ni un contraejemplo al signo del paper.

**Alcance.** Éste es un certificado asistido de un único bloque primitivo2x2 con todos sus cruces y colas completos. Por§19.8, firmar TODOS los bloques de la familia sería suficiente y necesario para el objetivo global; aquí sólo se han firmado dos dimensiones. No hay herencia automática al siguiente grado, recurrencia positiva, nuevo margen uniforme ni nueva ventana W/T. Los polinomios ortogonales de w no diagonalizan por sí solos Q. No se ha modificado ningún paper ni se infiere signo global.


### 19.10. Todos los bloques de cualquier cola fija de grados equivalen al objetivo global

**PROVED como alcance, no como positividad nueva.** Root/joint_sign_fresh_review; auditorías independientes arithmetic_fresh_candidate y fresh_global PASS antes del registro. Consultados las reglas del proyecto, los tres índices,§§18.9,19.8, [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md), [RECIPROCAL_PFAFFIANS083](POWER_RECIPROCAL_PFAFFIANS_083.md) y [GLOBAL, «Comparaciones primitivas»](POWER_GLOBAL_ROUTE_REVIEW.md). Se aplica el lema analítico allí probado, con un número FINITO arbitrario de restricciones, al core térmico ya establecido. No se presenta otra desigualdad positiva ni un nuevo principio de continuación; la diferencia respecto de§19.8 es conservar exactamente los momentos adicionales que eliminan cualquier prefijo fijo de grados.

**Enunciado.** Fijar un entero J>=1 y los E_j=p(t)(t-1)q_j(t) de§19.8. Son equivalentes:

1. Q es no negativa sobre TODA combinación finita de E_j con j>=J, incluidos todos sus cruces; equivalentemente, todos los bloques Gamma_(J..N), N>=J, son PSD.
2. lambda_A(T)>=0 para TODO T>0.

La cola se fija antes de cuantificar los tamaños. No se sustituye1 por signo de las diagonales, de un bloque finito, ni de una unión de paquetes positivos de dimensión creciente.

**Restricciones exactas de la cola.** Por ortogonalidad de q_j para w=(t-1)p, un polinomio P=pR pertenece a span FINITO{E_j:j>=J} exactamente cuando

    P(1)=0,
    integral_1^infinito t^k P(t)dt=0, 0<=k<J.       (TAIL-MOM)

En efecto P(1)=0 equivale a R=(t-1)S; las otras condiciones dicen que S es ortogonal en L²(w dt) a todos los polinomios de grado<J. Su expansión polinómica FINITA en los q_j empieza entonces en J.

Para F=TP y f(r)=F(exp(2r)), r>=0, la identidad de§18.9 da

    ell_sigma(f)=pi P(1)
        +pi(sigma/2-1/4)integral_1^infinito
                                      t^(sigma/2+1/4)P(t)dt.

Por tanto(TAIL-MOM) equivale a ell_sigma(f)=0 para la lista de J+1 números reales DISTINTOS

    Sigma_J={1/2} union {2k-1/2:0<=k<J}.          (TAIL-SIGMA)

Para sigma=1/2 se obtiene pi P(1); para sigma=2k-1/2 el coeficiente de la integral es pi(k-1/2), que no se anula para k entero. No se impone P'(1)=0.

**Extensión finita del lema ya probado en GLOBAL.** Sean sigma_1,...,sigma_m reales distintos, D impar real-analítica en TODA R y K_D(u,v)=(D(u)+D(v))/(u+v), con continuación removible. Si K_D es PSD sobre TODOS los bloques de un intervalo abierto I contenido en(max_l sigma_l,infinito), sujetos a

    sum_i d_i/(u_i-sigma_l)=0, 1<=l<=m,           (CPD-m)

entonces K_D es PSD completo. Para probarlo poner

    V(u)=prod_(l=1)^m(u-sigma_l),
    d_i=V(u_i)b_i,
    L(u,v)=V(u)V(v)K_D(u,v).

Los polinomios V(u)/(u-sigma_l) forman una base de los de grado<=m-1: evaluar en los sigma_l prueba su independencia. Así(CPD-m) equivale a sum_i b_i u_i^k=0, 0<=k<m. Elegir m anclas distintas en I y restar a cada delta_x su interpolante de Lagrange sobre esas anclas. Las medidas E_x resultantes anulan esos m momentos y C(x,y)=L(E_x,E_y) es PSD en I. L y C son conjuntamente real-analíticos en TODA R² porque D es impar. La continuación de§2.2 propaga PSD de C a toda R, exactamente como en el caso m=2 de GLOBAL.

Para cualquier medida finita con esos momentos nulos las correcciones de las anclas se cancelan, de modo que su energía L es no negativa. Las filas L(sigma_l,v) son cero. Dado un vector arbitrario con nodos fuera de los sigma_l, dividir sus coeficientes por V y añadir masas en los m puntos sigma_l para anular los m momentos. La matriz de esa reparación es Vandermonde e invertible; las filas nulas aseguran que la energía no cambia. Resulta PSD completa de K_D fuera de esos puntos y, por continuidad, también en ellos. La recíproca por restricción es inmediata. Sólo se usa un número FINITO fijo de momentos, no una continuación uniforme en m.

**Aproximación térmica con las J+1 restricciones.** Todos los funcionales P(1), integral t^kP, 0<=k<J, son continuos en B_a², 0<a<pi. El core de§19.8 aproxima cualquier P_c suave de soporte compacto en[1,infinito) por pR_n en esa norma y en el grafo completo(F,G). Si P_c satisface(TAIL-MOM), los J+1 errores tienden a cero. Repararlos con los vectores polinómicos FIJOS

    p, (t-1)p, t(t-1)p,...,t^(J-1)(t-1)p.

La fila de borde es(p(1),0,...,0). El bloque restante, sobre los últimos J vectores, es el Hankel

    H_kj=integral_1^infinito t^(k+j)w(t)dt,
    0<=k,j<J,

que es definido positivo porque w>0 para t>1 y todos sus momentos son finitos. La matriz total tiene determinante p(1)det H>0. Sus inversas y los vectores de reparación son FIJOS para este J; sus coeficientes correctores tienden a cero. Los aproximantes corregidos satisfacen(TAIL-MOM) exactamente, pertenecen al span finito de E_j,j>=J y convergen en el grafo. Bajo la hipótesis1, continuidad da Q(P_c)>=0 para todo compacto de este subespacio.

**Corte físico ANTES de aplicar el core.** Para pasar de esos compactos a(CPD-m), tomar la lista(TAIL-SIGMA), elegir U>max(1/2,max_(sigma en Sigma_J)|sigma|), y tasas u_i>U. Sea h(r)=sum_i d_i exp(-u_i r), r>=0, con sum_i d_i/(u_i-sigma)=0 para cada sigma de la lista. Elegir eta con max(1/2,max Sigma_J)<eta<min_i u_i. Entonces h pertenece a H_eta de014 y todos los momentos ell_sigma son continuos allí.

Cortar h suavemente sólo en infinito produce errores de esos momentos tendiendo a cero. Existen J+1 bumps físicos FIJOS con matriz de momentos invertible: tomar psi suave no negativa, soportada dentro de(1,2) y positiva en un intervalo, y los bumps psi(r)exp(sigma_l r). La matriz de momentos es el Gram de las exponenciales exp(sigma_l r) en L²(psi dr), definido positivo por su independencia lineal. Corregir con esos bumps da h_n compactos EXACTAMENTE sujetos a(TAIL-SIGMA), convergentes a h en H_eta. No se exige h_n(0)=0; el posible salto de la extensión causal es permitido en el dominio logarítmico, como en§18.9.

Ahora, y sólo ahora, poner F_n(t)=h_n(.5log t) y P_n=T^-1F_n con la inversa terminal de§17.8. Cada P_n es suave hasta1 y cero para t suficientemente grande. La identidad de momentos da(TAIL-MOM), sin imponer P_n'(1)=0. La aproximación térmica reparada anterior firma Q(P_n)=W[h_n]>=0. Continuidad014 y la identidad exacta de CONE001 dan

    W[h]=sum_ij d_i conjugado(d_j)K_(M_Phi)(u_i,u_j)>=0

en el subespacio(CPD-m) sobre cualquier intervalo abierto contenido en(U,infinito). M_Phi es impar y real-analítica en toda R, por la paridad y positividad real de Z. El lema extendido aplicado a D=M_Phi entrega PSD completa de K_(M_Phi). Los puentes§§2,18.9/BRIDGE002 dan entonces el objetivo2.

Este orden evita aplicar el core B_a² directamente a T^-1 de una mezcla exponencial física no cortada: esa preimagen tiene colas de potencia y NO se ha afirmado que pertenezca a B_a². Las normas de los compactos o sus constantes pueden depender del corte y de J; sólo se requiere convergencia para cada lista fija.

Recíprocamente, el objetivo2 firma todos los bloques primitivos por§19.8 y por tanto su restricción a cualquier cola fija. Esto completa la equivalencia.

**Alcance.** Es una aplicación de los antecedentes de continuación, reparación finita de momentos y core, no una desigualdad positiva nueva. El signo de todos los bloques de cualquiera de estas colas sigue OPEN. El bloque E_1,E_2 de§19.9 no controla automáticamente ninguna cola ni los cruces con ella; tampoco se prueba que ninguna cola pueda firmarse. No se identifica un mínimo a T fijo, no hay uniformidad en J ni nuevo margen, ventana W/T, cómputo o cambio en papers.


### 19.11. La referencia de primer modo no es PSD en el dominio polinómico primitivo exacto

**PROVED como aplicación de un falsificador previo a este dominio.** Construcción root/joint_sign_fresh_review; auditorías de la versión corta joint_sign_fresh_review/fresh_global/arithmetic_fresh_candidate y root PASS. Consultados las reglas del proyecto y los tres índices; antecedentes [PRIME_PATTERN_FALSIFIER008§4](POWER_PRIME_PATTERN_FALSIFIER_008.md), [AUDIT008](POWER_AUDIT_008.md), [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md),§§18.9,19.8 y el control operativo de§18.5 en [GLOBAL](POWER_GLOBAL_ROUTE_REVIEW.md). La necesidad de conservar la aritmética ya estaba registrada en008. Aquí sólo se transporta ese déficit a la referencia de primer modo y a las restricciones EXACTAS de esta familia polinómica, sin calcular otro grado ni otro vector numérico.

Poner p_0(t)=exp(-pi t), p(t)=sum_(n>=1)n²exp(-pi n²t), t>=1, y definir para polinomios reales R

    Q_0(R)=integral_1^infinito
       [log t |T(p_0R)|²
          +Re(T Lg(p_0R) conjugado(T(p_0R)))]dt/(2t).
                                                        (FIRST-REF)

No aparece C en esta referencia: se sustituyen p por p_0 y B por Lg. Se afirma que existe un polinomio real R tal que

    R(1)=0, integral_1^infinito p(t)R(t)dt=0,
    Q_0(R)<0.                                   (FIRST-NEG)

Las dos primeras condiciones hacen que pR, el vector de la familia REAL, sea exactamente primitivo. NO dicen que p_0R tenga ambos momentos Tate nulos.

**Identidad física sin peine.** Para un perfil temporal P suave de soporte compacto o con decaimiento exponencial suficiente, denotar por A_P(P) el lado derecho de(FIRST-REF) con p_0R reemplazado por P. La identidad física ya verificada para el grafo completo en GLOBAL, control operativo de§18.5, al retirar C, da exactamente

    A_P(P)=Arch[f]+2Re(ell_+(f)conjugado(ell_-(f))),
    f(u)=(TP)(exp(2u)), u>=0,
    ell_+(f)=pi P(1), ell_-(f)=pi P(1)-(pi/2)integral P.

El borde causal se conserva. Se utiliza esta identidad solamente sobre compactos suaves y los perfiles exponenciales polinómicos posteriores, donde todas las piezas convergen. A_P es continua en B_a², 0<a<pi, por§18.2 con G=(1/2)T LgP y sin C. Además Q_0(R)=A_P(p_0R).

**Un plano físico negativo de dimensión tres.** El bound de008§4 es

    m(tau)<=-4+17tau²,
    Arch[f]<=-4||f||²+17||f'||²

para tests físicos suaves compactos, por Parseval. Fijar un bump real no nulo phi en C_infinito,c((0,1)), c=||phi'||²/||phi||², y elegir L>0 con L²>17c/4. Los tres vectores

    f_j(u)=L^(-1/2)phi(u/L-3j), j=1,2,3,

tienen soportes disjuntos dentro de la semirrecta y separados de0. En TODO su span real V, tanto las normas como las normas de las derivadas suman sin cruces; así ||f'||²/||f||²=c/L² para cada f no nulo y Arch[f]<0. No se evalúa un nuevo determinante ni se usa signo del peine completo.

**Dos restricciones dejan una dirección negativa.** Para cada f en V, poner F(t)=f(.5log t) y P=T^-1F con la inversa terminal de§17.8. Este mapa es lineal e inyectivo; cada P es suave hasta1 y cero para t suficientemente grande. Definir

    rho(t)=p(t)/p_0(t)
          =sum_(n>=1)n²exp[-pi(n²-1)t].

La función rho es positiva y acotada en[1,infinito). Intersectar en V los dos núcleos reales

    P(1)=0, integral_1^infinito rho(t)P(t)dt=0.

De dimensión tres menos a lo sumo dos restricciones queda algún f no nulo. Para este vector ell_+(f)=0, por lo que el producto polar se anula y A_P(P)=Arch[f]<0. No se necesita ell_-(f)=0 ni se afirma integralP=0. Como F se anula cerca de1, la condición P(1)=0 también hace P cero cerca de1; en particular es un compacto interior admisible para el core.

**Pasar a un polinomio con las restricciones exactas.** El argumento de core de§19.8 se aplica también a p_0: sus primeras dos derivadas son constantes por exp(-pi t), la continuación en B_a² de p_0exp(zt) tiene el mismo semiplano Re z<pi-a, y la aproximación C² de compactos procede exactamente igual. Así existen polinomios reales R_n con p_0R_n->P en B_a². Los errores de P(1) e integral rho P tienden a cero; el segundo funcional es continuo porque rho está acotada y exp(-at) es integrable.

Repararlos con los dos perfiles FIJOS p_0,tp_0. La matriz de estos funcionales tiene determinante

    p_0(1)[integral_1^infinito t p(t)dt
                              -integral_1^infinito p(t)dt]
       =exp(-pi)integral_1^infinito (t-1)p(t)dt>0.

Los coeficientes correctores tienden a cero. Por tanto los perfiles corregidos siguen convergiendo a P en B_a² y son p_0 por polinomios reales, que nuevamente llamamos R_n, con R_n(1)=0 e integral p R_n=0 EXACTOS. Continuidad de A_P conserva la negatividad para algún n finito. Esto prueba(FIRST-NEG), sin calcular el grado ni los coeficientes del polinomio resultante.

**Alcance.** Se refuta únicamente PSD universal de la referencia(FIRST-REF) sobre el dominio primitivo EXACTO definido mediante p. Es una aplicación del déficit arquimediano de008 y del core existente, no un nuevo principio de necesidad aritmética. No es un valor negativo del Q completo, de A o del kernel de una densidad theta truncada; tampoco refuta toda comparación perturbativa ni toda compensación entre modos. Los certificados positivos§§19.7,19.9 permanecen intactos y el signo completo global sigue OPEN. Sin grado nuevo evaluado, campaña, cómputo, archivo auxiliar, ventana W/T o cambio en papers.

### 19.12. Adjunto causal y potencial local: signo negativo a derecha de log2

**PROVED, con cola completa y prueba elemental.** Construcción joint_sign_fresh_review/root; auditoría independiente arithmetic_fresh_candidate FULLPASS de normalizaciones, desigualdades y todas las colas, root PASS previo al registro. Releídos las reglas del proyecto y los tres índices; cotejados§18.5, GLOBAL (control operativo del cambio causal), [106_31](../phase-106-global-modular-star-audit/106_31_FULL_KERNEL_DOOB_VARIANCE_IDENTITY.md) y [ROUND005D](ROUND_005_D.md). Picone/Doob y el killing logarítmico tienen esos antecedentes. La diferencia examinada es el potencial del adjunto CAUSAL de este J exacto, con la métrica dt/(2t), y su signo en un punto de salto concreto. No se encontró este cálculo literal en el cotejo dirigido; no se afirma lectura exhaustiva ni prioridad mundial. La prueba siguiente NO usa la justificación externa de la identidad radical de106_31.

**Identidad del adjunto, conservando el extremo1.** Poner

    p=P_1, Theta(t)=Tp(t)=Phi(.5log t)>0,
    J=TBT^(-1), r=.5log t, dt/(2t)=dr.

La identidad Bp=0 de§18.5 vale para TODO t>0: las series theta y las sumas con logaritmos convergen absolutamente en cada compacto de t>0. En coordenada r, el operador forward completo L_f=logt+J es traslacionalmente invariante, con la renormalización diagonal ya fijada en GLOBAL. Su núcleo fuera de la diagonal, dirigido hacia r+h, es2k(h), donde

    k(h)=2cosh(h/2)-exp(-h/2)/(1-exp(-2h))
                       -sum_(n>=2)Lambda(n)/sqrt(n) delta_(log n)(h), h>0.

El término diagonal se conserva mediante la fórmula de Frullani, no se integra por separado un núcleo singular. De JTheta=0 se obtiene L_f Phi(r)=2rPhi(r) sobre TODA R. Reflejar esta identidad usando Phi par da L_b Phi(r)=-2rPhi(r) para el backward con la misma renormalización. Por tanto su promedio H_full satisface H_full Phi=0, deducido sólo de Bp=0, paridad y las identidades físicas de§18.5/GLOBAL.

Sea H_+ el promedio simétrico sobre r>=0. Para r>0, quitar la parte s<0 del promedio completo deja exactamente

    g(r):=H_+Phi(r)=-integral_0^infinito k(r+s)Phi(s)ds.       (POT-G)

No hay singularidad diagonal en este integral cuando r>0. Como H_+=logt+(J+J*)/2 y JTheta=0,

    (J*Theta)(exp(2r))=2g(r)-4rPhi(r).                       (CAUSAL-ADJ)

Aquí J*Theta se entiende como adjunto débil causal contra tests suaves compactos; no se postula pertenencia a un dominio global del adjunto Hilbertiano. La restricción r>=0 y su borde están incluidos en(POT-G), no se sustituyen por una convolución sin borde.

Para relacionarlo con la propuesta de caminos, definir Q_phys(F):=Q(T^(-1)F), conservando Q(P) como en§19. Escribir F=Theta f y usar la medida FIRMADA fuera de la diagonal

    dnu(t,v)=dt/(2t) [K(t,v)dv
                  -2sum_(m>=2)Lambda(m)/sqrt(m) delta_(m²t)(dv)],

con K de§18.5 y v>t. JTheta=0 y la identidad
Re(conj(a)(b-a))=(|b|²-|a|²-|b-a|²)/2 dan, para f suave de soporte compacto, con las diferencias haciendo integrable el borde diagonal,

    Q_phys(Theta f)=-.5 integral Theta(t)Theta(v)|f(v)-f(t)|² dnu + V(f),
    V(f)=integral_0^infinito Phi(r)g(r)|f(exp(2r))|²dr.      (POT-V)

Equivale a conservar logt Theta²+.5Theta J*Theta en la métrica física. No se supone que la medida física sea estacionaria por tener J un vector nulo a derecha.

**Fórmula explícita y lado derecho del salto.** Para h>0,

    2cosh(h/2)-exp(-h/2)/(1-exp(-2h))
             =exp(h/2)-sum_(j>=1)exp(-(2j+1/2)h).

Con las constantes positivas

    A_+=integral_0^infinito exp(s/2)Phi(s)ds=pi p(1),
    A_0=integral_0^infinito Phi(s)ds,
    A_j=integral_0^infinito exp(-(2j+1/2)s)Phi(s)ds, j>=1,

se obtiene, casi en todas partes para r>0,

    g(r)=sum_(n>exp r)Lambda(n)/sqrt(n) Phi(log n-r)
                    -exp(r/2)A_+
                    +sum_(j>=1)exp(-(2j+1/2)r)A_j.       (POT-EXPLICIT)

La igualdad A_+=pi p(1) es exactamente la identidad del momento positivo de§18.9. Las supercolas de Phi justifican absolutamente las series; la serie prima converge uniformemente en compactos de r alejados de sus puntos de salto. En r=log2 por la DERECHA, el término n2 ha desaparecido. Definir

    P_3=sum_(n>=3)Lambda(n)/sqrt(n) Phi(log(n/2)),
    Gamma=sum_(j>=1)2^(-2j-1/2)A_j.

Entonces g(log2+)=P_3-sqrt(2)A_++Gamma. Como A_j<=A_0<=A_+,

    Gamma<=A_+/(3sqrt(2)),
    g(log2+)<=P_3-[5/(3sqrt(2))]A_+.                     (POT-BUDGET)

**Cota polar generosa.** Las desigualdades pi>3, pi<16/5 y exp(16/5)<25 prueban

    A_+>=pi exp(-pi)>3/25.

Se dan abajo gates de Taylor para las exponenciales. Como sqrt(2)<3/2, la pérdida neta de(POT-BUDGET) es estrictamente mayor que2/15.

**Cola prima/theta COMPLETA.** Para n>=3 la serie positiva exacta es

    Phi(log(n/2))=pi sum_(m>=1)m²(n/2)^(5/2)
              [(pi/2)m²n²-3]exp(-pi m²n²/4).

Multiplicar por Lambda(n)/sqrt(n) y extraer la parte principal deja

    [pi²/(8sqrt(2))] Lambda(n)m^4 n^4
       [1-6/(pi m²n²)]exp(-pi m²n²/4).

Usar pi²<10, sqrt(2)>7/5, Lambda(n)<=log n y log3<9/8. En el ÚNICO par aislado (n,m)=(3,1), conservar el factor entre corchetes, menor que4/5 porque pi<10/3. Como pi>25/8 implica9pi/4>7 y exp7>1000,

    contribucion_(3,1)
      <(25/28)·81·(9/8)·(4/5)/1000=3645/56000.          (POT-FIRST)

Para TODOS los demás pares poner q=mn>=4 y omitir sólo el término negativo -3 en un upper. La identidad de emparejar divisores y las cotas tau(q)<=q, log q<=q/2 para q>=4 dan

    sum_(n|q,n>=3)log n
         <=sum_(n|q)log n=tau(q)log q/2<=q²/4.

El prefactor pi²/(8sqrt(2))<25/28<1 y pi/4>25/32 prueban para el resto completo

    resto<sum_(q>=4)(q^6/4)exp(-25q²/32).

El cociente entre términos consecutivos es a lo sumo

    (5/4)^6 exp(-225/32)<4/1000=1/250.

Con exp(25/2)>250000, sumar esta cola geométrica produce

    resto<1024/249000,
    P_3<3645/56000+1024/249000<7/100.                    (POT-TAIL)

La agrupación incluye todo modo m y todo entero primo-potencia n>=3; no es un truncamiento sin resto ni un cambio de los pesos Lambda.

**Gates elementales suficientes.** Para hacer explícitos los presupuestos exponenciales anteriores, poner S8=sum_(k=0)^8 3^k/k!. Las comparaciones racionales

    S8>20,
    S8+(3^9/9!)/(1-3/10)<81/4

dan20<exp3<81/4; el upper usa el cociente de términos de la cola desde orden9, a lo sumo3/10. Además

    exp(1/5)<6/5+3/140<49/40,
    exp(16/5)<(81/4)(49/40)=3969/160<25,
    exp7=(exp3)² exp1>20²·(8/3)>1000,
    exp(25/2)=(exp3)^4 exp(1/2)>20^4·(13/8)>250000.

El upper exp(1/5) suma desde grado2 con cociente a lo sumo1/15; exp1>8/3 y exp(1/2)>13/8 siguen de sus series positivas. La desigualdad log3<9/8 sigue de sum_(k=0)^4(9/8)^k/k!>3: se usan CINCO términos, grado4. Las cotas de pi anteriores son las racionales elementales usuales; por ejemplo pi>25/8 sigue de pi=4[arctan(1/2)+arctan(1/3)] y

    4[(1/2-1/24+1/160-1/896)+(1/3-1/81)]>25/8,

mediante las sumas alternantes inferiores de arctan. Todos los gates y la comparación racional final(POT-TAIL) fueron comprobados en la auditoría independiente, sin cuadratura ni campaña.

**Signo y alcance.** Combinar(POT-BUDGET) y(POT-TAIL) da estrictamente

    g(log2+)<7/100-2/15=-19/300<-1/20.                  (POT-NEG)

La convergencia uniforme local a derecha de log2, antes del siguiente salto log3, conserva g<0 en algún intervalo abierto I. Puesto que Phi>0, elegir f suave no nula con soporte físico en I hace V(f)<0 en(POT-V). El mismo signo negativo se conserva con primitividad EXACTA: tomar tres bumps reales chi_i suaves, no nulos y de soportes disjuntos dentro de I. En su espacio de dimensión3 los dos funcionales

    b -> integral_I exp(r/2)Phi(r)sum_i b_i chi_i(r)dr,
    b -> integral_I exp(-r/2)Phi(r)sum_i b_i chi_i(r)dr

tienen un núcleo común de dimensión al menos1. Elegir b no cero en él y poner f(exp(2r))=sum_i b_i chi_i(r). El físico F(exp(2r))=Phi(r)sum_i b_i chi_i(r) tiene ambos momentos Tate nulos. Los soportes disjuntos aseguran F no nulo, y Phi g<0 en I da V(f)<0 estrictamente. Su preimagen P=T^(-1)F es suave compacta y satisface P(1)=integralP=0 por§18.9; no se impone P'(1)=0. No se calcula un radio, un grado ni otro test de signo. Por contraste, el borde r hacia0 tiene g(r)=[Phi(0)/2]log(1/r)+O(1): el killing logarítmico favorable conocido en ROUND005D§1 no controla este intervalo interior.

Queda refutada SÓLO la exigencia V(f)>=0 para todos los bumps locales en esta descomposición exacta, INCLUSO restringiendo F a primitividad exacta mediante la combinación de tres bumps. El término de diferencias de(POT-V) conserva signo mixto y puede compensar V<0: NO se demuestra Q negativo, A negativo, negatividad de la forma primitiva completa del Paper47 ni un NO-GO general de caminos, tres puntos o tratamientos conjuntos. Global sigue OPEN; certificados§§19.7,19.9 intactos. Sin archivos nuevos, campaña, nueva ventana W/T ni cambios en papers.
