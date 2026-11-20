# POWER_ENERGY_GROUP_037 — Dilatación crítica y agrupación firmada en la banda energética

Estado: **PROVED**, revisión independiente aprobada en POWER_GROUP_AUDIT_037.md y verificador PASS reproducido. Tasa FIJA u=63/2. Papers intactos.

Resultados: (i) cotas uniformes de la dilatación gamma real en el centro energético; (ii) falsificador analítico de contracción ABSOLUTA de la inversión Möbius para TODOS N>=2^16; (iii) desigualdad FIRMADA cuantitativa de agrupación por cualquier conjunto FINITO de primos, con error explícito y condición suficiente de signo. No se estima aún el residuo infinito ni se afirma signo de W.

## 1. Corpus y diferencia precisa

Consultados ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md, CROSSWORD-TO-D.md y STATE036; leídos LOW_TABLE018, SIGNED_MEAN019, INVERSE_KERNEL020, UNIFORM_CUTOFF026, GAMMA_WEIGHT031, PRIME_BALANCE033 y MOVING_BALANCE036.

La cancelación principal polar–peine y las identidades de divisores ya pertenecen018/019: no se presentan como desigualdades nuevas. La diferencia aquí es evaluar su recuperación en el MISMO perfil gamma, en la banda ENERGÉTICA real localizada036. Allí la dilatación de la inversión es crítica1/m, a diferencia del régimen contractivo m^(-2) de033. Se prueba ese límite y, después, se agrupa el signo Möbius ANTES del error gamma para obtener una desigualdad local explícita, no sólo otra representación.

La comparación no introduce un error relativo polinomial como si compensara por sí solo la diferencia pequeña entre componentes exponenciales. La precisión necesaria del residuo completo sigue siendo una obligación abierta.

## 2. Perfil gamma real y centro energético

Con d=N−1>=1, conserve rho_N(t)=C_N(t)/C_N(0), q_N=−rho_N'/rho_N y

    H_N(x)=−(d/dx)[x^(-1/2)rho_N(logx)]
          =x^(-3/2)rho_N(logx)[1/2+q_N(logx)]>0.

UNIFORM_CUTOFF026 y GAMMA_WEIGHT031 prueban exactamente

    q'=q²+(2d/t)q−u²,
    0<q'<M_N:=u²/(2N−3), q(0)=0.

Defina

    t_N=d/(u²−1/4)=d/992,
    x_N=e^(t_N).

Es el centro crítico natural de la energía e^(t/2)rho_N(t): la raíz positiva de la ecuación Riccati sin el término q' es1/2 en t_N. En general, para beta>0,

    q_N(d beta)=sqrt(beta^(-2)+u²)−beta^(-1)+O(M_N),

con error acotado por M_N dividido por2sqrt(beta^(-2)+u²), al factorizar el cuadrático. Por tanto el modo de e^(t/2)rho_N(t), donde q=1/2, satisface t/d->1/992. Esto es compatible con m/d->1/32 en036: la integral Laplace positiva condicionada al índice tiene escala temporal m/(u−1/2), y31·32=992. El centro no es un punto elegido mediante una campaña.

Más precisamente, en t_N la Riccati se factoriza:

    q'=(q−1/2)(q+1984+1/2).

Como q'>0 y q>0, se obtiene la cota REAL

    1/2<q_N(t_N)<=1/2+M_N/1985.                          (CENTER)

## 3. Dilatación crítica con resto uniforme

Para m>=1 real, escriba ell=logm y

    D_N(m)=m H_N(mx_N)/H_N(x_N).

La identidad exacta es

    D_N(m)=m^(-1/2)rho_N(t_N+ell)/rho_N(t_N)
                    ·[1/2+q_N(t_N+ell)]/[1/2+q_N(t_N)].

CENTER y0<q'<M_N dan para0<=s<=ell

    1/2<=q_N(t_N+s)<=1/2+M_N(1/1985+s),
    1<=[1/2+q_N(t_N+ell)]/[1/2+q_N(t_N)]<=1+M_Nell.

Integrar el primer bound y combinar ambos prueba

    m^(-1)exp{−M_N[ell/1985+ell²/2]}
      <=D_N(m)<=m^(-1)(1+M_Nell).                        (DILATE)

En particular, para cada m fijo, D_N(m)->1/m cuando N crece. No se toma un valor absoluto del residuo aritmético para deducir un signo.

También, usando exp(−z)>=1−z,

    |D_N(m)−1/m|
       <=(M_N/m)[a ell+ell²/2],
    a=1+1/1985.                                         (ERROR)

Éste es el resto gamma que permite la agrupación firmada del§5.

## 4. Falsificador de la contracción ABSOLUTA propuesta

El inverso completo019 es h_N(x)=sum_(m>=1)mu(m)mH_N(mx), absolutamente convergente para cada N. Un paso suficiente natural sería exigir

    sum_(m>=2)|mu(m)|D_N(m)<1

en el centro energético. Ese paso es FALSO uniformemente para TODOS N>=2^16.

Prueba sin tabla Möbius. Para R ENTERO, la cantidad A(R) de enteros libres de cuadrados<=R satisface A(R)>R/4: los no libres están contenidos en la unión de múltiplos de k²,k>=2, cuyo número es <R sum_(k>=2)k^(-2)<3R/4. Se usó1/4+int_2^infty x^(-2)dx=3/4. Sumación por partes DISCRETA da

    sum_(m=1)^R |mu(m)|/m
      =A(R)/R+sum_(n=1)^(R−1) A(n)/[n(n+1)]
      >H_R/4>logR/4.

Restar el término m1 prueba

    sum_(m=2)^R |mu(m)|/m>(1/4)logR−1.

Fije R=2^18, SIN enumerar sus enteros. Para N>=2^16, el verificador racional prueba

    M_N[(logR)/1985+(logR)²/2]<2/3<log2,
    (1/4)logR−1>2.

Por DILATE, D_N(m)>1/(2m) para TODO2<=m<=R. Por tanto

    sum_(m>=2)|mu(m)|D_N(m)
      >=sum_(m=2)^R |mu(m)|D_N(m)>1.                     (ABS-FAIL)

De hecho esta suma absoluta no admite un bound uniforme en N: para cada R fijo su límite parcial es sum_(m=2)^R|mu(m)|/m y estas sumas crecen sin cota. ABS-FAIL sólo refuta el paso de contracción por valores absolutos en este régimen. No afirma que la suma FIRMADA no contraiga, que h_N sea negativo o que W sea negativo.

## 5. Agrupación aritmética FINITA antes de tomar errores

Sea Q un producto FINITO de primos distintos. Defina sobre el perfil REAL

    K_(N,Q)(m)=sum_(b|Q)mu(b)D_N(mb),
    U_Q=prod_(p|Q)(1−1/p)>0,
    V_Q=prod_(p|Q)(1+1/p),
    mu_Q=sum_(p|Q)logp/(p+1),
    sigma_Q²=sum_(p|Q)p(logp)²/(p+1)².

Aquí mu_Q es un promedio logarítmico, no la función Möbius. ERROR, aplicado DESPUÉS de conservar el signo de la suma principal, prueba

    |K_(N,Q)(m)−U_Q/m|
      <=(M_N V_Q/m) E_Q(logm),                           (SIGNED)
    E_Q(ell)=a(ell+mu_Q)
                    +(1/2)[(ell+mu_Q)²+sigma_Q²].

Prueba. La contribución principal es exactamente sum_(b|Q)mu(b)/(mb)=U_Q/m. Para el resto se suma ERROR con1/b. La probabilidad b|Q con peso(1/b)/V_Q incluye cada primo p independientemente con probabilidad1/(p+1). Sus momentos son Elogb=mu_Q y Var(logb)=sigma_Q²; expandir la cuadrática de ERROR da SIGNED.

Ésta no es sólo la identidad de un producto Euler. Es una desigualdad con un resto gamma UNIFORME en N,m y una condición de signo comprobable:

    M_N V_Q E_Q(logM)<=U_Q/2
      ⇒ U_Q/(2m)<=K_(N,Q)(m)<=3U_Q/(2m), 1<=m<=M.         (WINDOW)

E_Q crece en ell>=0, lo que justifica extender la condición del extremo a todo el intervalo. Para Q fijo, WINDOW permite intervalos logM de orden sqrt(N) con constante suficientemente pequeña. Traducidos a x=x_Nm, son una parte derecha de la banda energética real. No se concluye positividad del inverso completo.

La ganancia concreta es que la constante principal1/m se sustituye por U_Q/m mediante cancelación Möbius exacta, conservando error explícito. El exponente crítico m^(-1) NO cambia. Para Q creciente debe verificarse también la degradación de U_Q/V_Q y del resto; el§8 analiza una elección explícita sin atribuir signo a FULL.

## 6. Dónde permanece el resto infinito

La agrupación completa, todavía con TODOS los enteros aritméticos, es

    h_N(x_N)/H_N(x_N)
      =sum_((m,Q)=1)mu(m)K_(N,Q)(m).                    (FULL)

Cada entero libre de cuadrados se descompone de modo único en un divisor b de Q y un m coprimo con Q. Las series originales son absolutas para N fijo, así que esta reordenación es legítima.

Pero el mayorante de ERROR/SIGNED, de orden(logm)²/m, NO es sumable sobre todo m. Por tanto no puede sumarse hasta infinito ni usarse para borrar el complemento de WINDOW. Tampoco el signo de K_(N,Q) en una ventana hace no negativa la suma exterior de mu(m), que conserva sus signos.

La identidad conocida de018/019 relaciona el residuo conjunto con este inverso y B:

    P_N−Pi_N=2Lminus_N−F_N,
    F_N=2int_1^infty h_N(x)B(x)dx.

SIGNED no se registra como una cota ya obtenida de F_N: falta controlar el complemento aritmético firmado, además de integrar la banda con sus pesos reales. La precisión de la diferencia polar−peine no se deduce de un error relativo polinomial frente a componentes de fase lambda^N.

## 7. Resultado y siguiente obligación

Quedan demostrados dos hechos sustanciales sobre una propuesta concreta: el paso de contracción ABSOLUTA falla en el centro energético real para una familia infinita de N; la agrupación FINITA firmada sí tiene un principal positivo y un error gamma explícito que preserva su signo bajo WINDOW. No se introdujo un modelo ficticio ni se alteró Lambda o mu.

El residuo infinito sigue abierto. La continuación constructiva debe combinar esa cancelación con un bound firmado del complemento, sin sumar un error no sumable ni convertir el signo de un grupo finito en el de FULL. No se afirma signo W, nueva cobertura o cierre global.

Verificador: tools/power_energy_group_037_verify.py; Fraction/intervalos exactos para constantes y umbrales, PASS. Las identidades de divisores y las cotas uniformes están probadas analíticamente. No se evalúa W en ningún N nuevo ni se enumera una campaña Möbius. La revisión independiente confirma el núcleo y la extensión adversarial del§8. Papers intactos.

## 8. Una elección Q creciente: grupos positivos, resto absoluto aún dominante

Revisión adversarial complementaria, sobre la MISMA propuesta SIGNED. Permitir que Q crezca sí preserva una cancelación local para una elección explícita, pero no paga el complemento por triángulo. Este resultado no invalida una agrupación FIRMADA ulterior.

Para TODOS N>=2^80 tome

    K=floor(N^(1/8)), Q=prod_(p<=K)p,
    ell=3N^(1/4), M=exp(ell).

Aquí K>=1024. Las cotas elementales (sin estimaciones asintóticas de primos) son

    U_Q>=prod_(n=2)^K(1−1/n)=1/K,
    V_Q<=prod_(n=2)^K(1+1/n)=(K+1)/2,
    U_Q V_Q=prod_(p<=K)(1−1/p²)<=1,
    U_Q<=1/2,
    logQ<=KlogK<=K²<=N^(1/4),
    mu_Q<=logQ, sigma_Q²<=log²Q.

Por tanto V_Q/U_Q<=K(K+1)/2<=N^(1/4). SIGNED implica, UNIFORMEMENTE en1<=m<=M,

    |K_(N,Q)(m)−U_Q/m|<=epsilon_N U_Q/m,
    epsilon_N<=u²[4a N^(-1/2)+(17/2)N^(-1/4)]<1/100.     (GROW)

En efecto ell+mu_Q<=4N^(1/4), sigma_Q²<=N^(1/2), M_N<=u²/N y a<2. En N>=2^80 basta la comparación racional

    u²[8·2^-40+(17/2)2^-20]<1/100.

Así TODOS los grupos de esa ventana son realmente POSITIVOS. El crecimiento de Q no se invoca sólo formalmente.

Sin embargo,

    sum_((m,Q)=1,m>=2)|mu(m)| |K_(N,Q)(m)| >37/25=1.48,
    0<K_(N,Q)(1)<101/200=.505.                          (GROW-ABS)

La suma de la izquierda conserva TODO el resto infinito; se acota inferiormente por un subconjunto finito positivo de la ventana.

Prueba. Defina las masas armónicas FINITAS

    S(M)=sum_(m<=M,(m,Q)=1)1/m,
    T(M)=sum_(m<=M,(m,Q)=1)mu(m)²/m.

Como M>Q, todos los divisores b de Q satisfacen M/b>=1. Para z>=1,

    H_floor(z)=logz+e(z), 0<=e(z)<=1.

Inclusión–exclusión, ANTES de estimar el error, da

    S(M)=sum_(b|Q)mu(b)H_floor(M/b)/b
         >=U_Q logM−sum_(b|Q)mu(b)logb/b−V_Q
         >=U_Q ell−V_Q.                                (COPRIME)

El término logarítmico que se ha conservado tiene signo favorable exacto:

    sum_(b|Q)mu(b)logb/b
      =−U_Q sum_(p<=K)logp/(p−1)<=0.

Los m coprimos con Q que no son libres de cuadrados son divisibles por p² para algún primo p>K. Dividir por p² preserva la condición de coprimalidad. Por unión de esos sucesos con pesos POSITIVOS,

    S(M)−T(M)
      <=sum_(p>K) p^-2 S(M/p²)
      <=S(M)sum_(n>K)n^-2<=S(M)/K.

Luego T(M)>=(1−1/K)S(M). GROW, aplicado sólo a m<=M, prueba

    sum_((m,Q)=1,m>=2)|mu(m)| |K_(N,Q)(m)|
      >=(1−epsilon_N)U_Q[T(M)−1]
      >=(1−epsilon_N)
           [(1−1/K)(U_Q²ell−U_QV_Q)−U_Q]
      >=(99/100)[2(1−1/1024)−1/2]>37/25.

Se usó U_Q²ell>=3N^(1/4)/K²>=3, U_QV_Q<=1 y U_Q<=1/2. La resta1 dentro de T(M) elimina m1, no un contacto aritmético no contado. Por otro lado GROW en m1 da K_(N,Q)(1)<(101/100)U_Q<=101/200. Esto demuestra GROW-ABS con constantes racionales.

Conclusión específica: ESTA elección creciente de grupos tiene principal positivo y error local controlado, pero la suma de módulos de los grupos restantes es incluso mayor que el grupo principal. Por tanto no permite deducir el signo de FULL por dominación diagonal o por una nueva contracción ABSOLUTA después de agrupar. La suma FIRMADA exterior todavía puede cancelar; no se afirma signo de h_N, F_N o W, ni se excluyen otras elecciones o estimaciones firmadas del complemento.
