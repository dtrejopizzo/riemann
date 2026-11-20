# POWER_SIGNED_TRANSFORM_035 — Ley positiva específica de la transformación gamma firmada

Estado: **PROVED**, identidades y cotas analíticas aprobadas en revisión independiente POWER_BOUNDARY_AUDIT_035.md; verificador simbólico PASS reproducido. Tasa FIJA u=63/2. No se declara signo de W para todos N. Papers intactos.

Resultados cuantitativos: ley exacta de pesos Abelgamma; cota uniforme O(R^4/N²) de masa inicial; colas explícitas y límite Gamma(shape2) en la escala m²/(4N). Se conserva T_m firmado de034, sin volver a postular su positividad.

## 1. Corpus y razón nueva

Leídos las reglas del proyecto, COEFFICIENT_BALANCE033, WEIGHTED_COEFFICIENT034 y sus auditorías; consultados índice ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D.md en transformaciones positivas, Abel, mezclas, Riesz y coeficientes. No se reabre la premisa T_m>=0, refutada034 con infinitos cambios de signo.

La diferencia es estudiar la transformación POSITIVA y ESPECÍFICA de los pesos gamma, no una clase abstracta de medidas. La paridad analítica034 se pliega mediante una sustitución cuadrática explícita; la transformación tiene una ley combinatoria con cotas uniformes que cuantifican dónde se debe conservar la compensación. Las identidades solas no se promueven a prueba de signo. Las nuevas desigualdades son las cotas de masa y de presupuesto finito de§§4–6, válidas a TODOS N del rango declarado sin campaña.

## 2. Abel real y normalización probabilística exacta

Con d=N−1>=2, conserve033:

    a0=a1=1,
    a_(m+1)/a_m=2(d−m)/(2d−m), a_(d+1)=0,
    v_m=a_m/(2d−m), v_(d+1)=0,
    A_N:=W[g_N]/norm²=sum_(m=1)^d (v_m−v_(m+1))T_m.

Defina h_m=m(m+1)/2 y t_m=T_m/h_m. La normalización

    P_d(m)=h_m(v_m−v_(m+1))
      =a_m m(m−1)(m+1)/[2(2d−m)(2d−m−1)], 1<=m<=d,     (P)

es no negativa (P_d(1)=0) y suma exactamente1. En efecto, sumación por partes da sum h_m(v_m−v_(m+1))=sum m v_m=sum w_m=1. Por tanto

    A_N=sum_(m=1)^d P_d(m)t_m.                           (AVERAGE)

Ésta es una media positiva de valores FIRMADOS. Los perfiles que definen t_m no se suponen autocorrelaciones admisibles. Para d1, A_2=T1 y se trata separadamente como el caso ya probado018.

## 3. Sustitución Catalan que conserva la paridad, sin inferencia de signo

Sea c_d=binom(2d,d)/4^d. La recurrencia por derivación en u² de la forma completa da cerca de z0

    B(z):=sum_(d>=0)c_d A_(d+1)z^d
         =E(u sqrt(1−z))/sqrt(1−z),
    E(v)=L[e^(−vt)].

Para justificarla, escriba f(s)=E(sqrt(s))/(2sqrt(s)). La linealidad de la forma en su densidad racional y su término polar da W[g_(d+1)]=(-1)^d f^(d)(u²)/d!, mientras norm²=c_d/(2u^(2d+1)). Taylor produce la fórmula. Se puede derivar por separado en ARCH, peine y polar para |z| suficientemente pequeño; todos convergen absolutamente allí.

Con F de034 y phi(z)=1−sqrt(1−z),

    B'(z)=(1/2)F(phi(z)),
    F(w)=[E(v)−vE'(v)]/(1−w)^3, v=u(1−w).               (FOLD)

phi tiene coeficientes Catalan positivos y satisface z=phi(2−phi). Para d>=2, inversión formal de Lagrange da

    [z^(d−1)]phi(z)^(m−1)
      =(m−1)/(d−1)·binom(2d−m−2,d−m)·2^(−2d+m+1),
      2<=m<=d.

Dividir por2d c_d reproduce EXACTAMENTE el coeficiente v_m−v_(m+1) de Abel. No se sustituye la transformación real por una mezcla elegida libremente.

Además F(1+s)=F(1−s) implica que F(phi(z)) depende localmente de(1−phi(z))²=1−z: se cancela la ramificación local aparente en z1. Esto conserva una cancelación real de coeficientes. No prueba que los coeficientes de B sean positivos; tampoco se ha probado para B la prolongación en torno a TODO el semieje real positivo que exigía el argumento034. Por tanto OSC034 no se traslada como una conclusión sobre el signo de los A_N.

## 4. Colas EXACTAS de la ley gamma

**Teorema.** Para2<=r<=d,

    P_d(M>=r)
      =a_r[1+r(r−1)/(2(2d−r))].                         (TAIL)

Prueba: sumar P por partes hasta r−1. Se obtiene

    P_d(M<=r−1)=1−a_r−[r(r−1)/2]v_r,

lo que equivale a TAIL. No hay aproximación ni hipótesis sobre T_m.

En particular, para1<=R<=d,

    P_d(M<=R)
      <=min{1,R(R−1)(R+1)(R+2)/[8d(d−1)]}.               (SMALL)

Por(P), a_m<=1 y (2d−m)(2d−m−1)>=d(d−1); sumar m(m²−1) desde1 hasta R da R(R−1)(R+1)(R+2)/4. Esto prueba SMALL.

También, poniendo x_r=r(r−1)/(4d),

    P_d(M>=r)<=min{1,(1+2x_r)e^(−x_r)}.                  (LARGE)

En efecto

    a_r=prod_(j=0)^(r−1)(1−j/d)/(1−j/(2d))
       <=exp(−sum_(j=0)^(r−1)j/(2d))=e^(−x_r),

mientras la corrección de TAIL es <=1+2x_r porque2d−r>=d. Las desigualdades son uniformes en d y no derivan el signo de A_N de una identidad de momentos.

## 5. Escala m~sqrt(N) con resto explícito

Para2<=r<=d/2, expandir log(1−y) en su serie absolutamente convergente da

    −x_r−r³/(3d²)<=log a_r<=−x_r.

El resto se acota por sum_(j<r)(j/d)², ya que para0<=y<=1/2,

    0<=−log(1−y)+log(1−y/2)−y/2
       <=y²/[2(1−y)]<=y².

La corrección exacta en TAIL pertenece a[1+x_r,1+x_r+x_r r/d]. Así

    (1+x_r)e^(−x_r−r³/(3d²))
      <=P_d(M>=r)
      <=(1+x_r+x_r r/d)e^(−x_r).                        (WINDOW)

Por consiguiente M(M−1)/(4d) converge en distribución a la ley Gamma(shape2), cuya supervivencia es(1+x)e^(−x). Para r=O(sqrt(d)), WINDOW exhibe directamente un error que tiende a0. No se afirma convergencia uniforme para r de orden d ni se usa la ley límite para reemplazar el kernel aritmético en una prueba de signo.

La consecuencia estructural es concreta: el transformado gamma no selecciona un índice fijo. Los índices relevantes siguen una ventana MOVIL de orden sqrt(N). Los infinitos cambios de signo034 deben compensarse contra esa ley real.

## 6. Presupuesto firmado real de cualquier prefijo FINITO

Para los t_m aritméticos reales, defina B_R=max_(1<=m<=R)t_m^−. SMALL prueba para TODOS d>=max(2,R)

    sum_(m<=R)P_d(m)t_m
      >=−B_R min{1,R(R−1)(R+1)(R+2)/[8d(d−1)]}.           (BUDGET)

Así cualquier conjunto FIJO de prefijos adversos tiene contribución adversa a la mezcla gamma O(N^(-2)), con constante explícita. No se requiere modificar sus signos ni suponer positivos los demás. Es una desigualdad cuantitativa de la transformación real y no el enunciado W>=0 reescrito.

BUDGET no controla todos los t_m negativos: son infinitos por034 y sus magnitudes pueden crecer. LARGE controla probabilidades de cola, no automáticamente el producto con un funcional aritmético de magnitud desconocida. No se concluye que SMALL/LARGE por sí solos prueben A_N>=0. La obligación que queda vive en la ventana móvil y en sus colas ponderadas por t_m.

## 7. Alcance de una restricción genérica de simetría

Como límite breve, los pesos anteriores y la simetría cosh positiva por sí solos no fuerzan el signo de su promedio. El modelo ya usado en CONE001, escalado a Theta_model(v)=3+cosh(av), a=log2/u, da para el exponencial E_model=2Theta_model'/Theta_model

    A_2,model=E_model(u)−uE_model'(u)
      =2a(51−76log2)/289<0.

Este modelo conserva la representación cosh positiva y la paridad necesarias en034; no es la aritmética real ni se le atribuye el mismo dato prime. El cálculo sólo impide convertir una propiedad genérica de simetría en un argumento de signo para AVERAGE. No es una nueva refutación de W real ni un NO-GO global. La aritmética real necesita aportar la compensación cuantitativa de t_m frente a P_d.

## 8. Evidencia y residuo

El script tools/power_signed_transform_035_verify.py verifica simbólicamente las identidades de masas/CDF, la suma polinomial de SMALL y los cocientes; no evalúa nuevos N ni una lista de m. La prueba de WINDOW y de la escala límite es analítica. El script usa SymPy para identidades formales y los intervalos003 sólo en el chequeo de modelo genérico del§7; PASS.

No se afirma una nueva región W ni ventanaT. El resultado es una representación de promedio específica junto a cotas uniformes y un presupuesto firmado finito. El siguiente paso constructivo debe estimar el promedio aritmético en la escala sqrt(N), no volver a la premisa T_m>=0 refutada ni construir una lista de casos positivos. Papers intactos.
