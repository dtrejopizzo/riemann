# POWER_MOVING_BALANCE_036 — Ventana de masa y ventana energética real

Estado: **PROVED**, revisión independiente aprobada en POWER_FRONTIER_AUDIT_036.md y verificador PASS reproducido. Tasa FIJA u=63/2. Papers intactos.

Resultado principal a revisar: aunque la ley Abelgamma P_d concentra masa en m~sqrt(N), sus inclinaciones por las contribuciones polar y aritmética COMPLETAS concentran energía en

    m/(N−1)->1/32.

Se dan representaciones positivas exactas y cotas exponenciales uniformes. No se afirma que el funcional FIRMADO t_m tenga esa misma ventana: su cancelación interna puede modificarla. No se afirma signo total de W.

## 1. Corpus y diferencia precisa

Leídos directamente ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md, CROSSWORD-TO-D.md y STATE035; además SIGNED_TRANSFORM035, JOINT_SCALE016, LOW_TABLE018, COEFFICIENT_BALANCE033 y sus auditorías. El fracaso de pesos exponenciales uniformes a tasa fija016 y la insuficiencia de presupuestos absolutos018 son antecedentes, no conclusiones nuevas aquí.

La diferencia es estudiar la ley POSITIVA ESPECÍFICA035 y sus inclinaciones por componentes REALES de la forma, incluido TODO el peine Lambda. Se prueba dónde va su energía, no sólo dónde va la probabilidad de una medida auxiliar. La comparación aritmética inferior es elemental y se demuestra, sin suponer un bound de error fino de psi_Lambda. No se cambia un peso primo ni se hace una campaña de N.

La obstrucción queda limitada al siguiente paso erróneo: «la cola fuera de Csqrt(N) tiene poca probabilidad, luego se pueden omitir por separado las contribuciones polar y prima en ella». Ese paso es falso para los componentes reales. No se descarta una compensación firmada que se haga ANTES de separarlos.

## 2. Ley exacta y componentes positivos

Sea d=N−1>=2. Conserve035:

    a0=a1=1, a_(m+1)/a_m=2(d−m)/(2d−m), a_(d+1)=0,
    delta_v_m=v_m−v_(m+1), v_m=a_m/(2d−m),
    P_d(m)=m(m+1)delta_v_m/2, sum_m P_d(m)=1,
    t_m=T_m/[m(m+1)/2], A_N=W[g_N]/norm²=sum_m P_d(m)t_m.

Para S_j(y)=e^(−uy)sum_(l=0)^j(uy)^l/l!, escriba p_j>0 para su contribución polar lineal y pi_j>0 para el MÓDULO de su peine (su signo en W es negativo). Sean

    p_m^T=[sum_(j=1)^m j p_j]/[m(m+1)/2],
    pi_m^T=[sum_(j=1)^m j pi_j]/[m(m+1)/2].

Son componentes de los mismos perfiles que definen t_m, sin alterar sus contactos. Por linealidad de las mezclas finitas,

    P_N=sum_m P_d(m)p_m^T,
    Pi_N=sum_m P_d(m)pi_m^T,

donde P_N es el polar REAL normalizado de g_N y Pi_N es el módulo de su peine REAL COMPLETO. Defina las inclinaciones EXACTAS

    Q_d^P(m)=P_d(m)p_m^T/P_N,
    Q_d^Pi(m)=P_d(m)pi_m^T/Pi_N.                         (ENERGY)

Ambas son leyes positivas normalizadas. No son la ley de signos del funcional completo.

## 3. Una inclinación base con representación binomial exacta

Ponga

    r=u/(u−1/2)=63/62, s=u/(u+1/2)=63/64,
    A_d(r)=sum_(m=0)^d a_m r^m,
    Qtilde_d(m)=a_m r^m/A_d(r).

El término a0 está INCLUIDO. La integral beta da exactamente

    A_d(r)=(2d+1)int_0^1 q(t)^d dt,
    q(t)=(1−t)[1+(2r−1)t].                              (BETA)

En efecto a_m=(2d+1)binom(d,m)2^m int_0^1 t^m(1−t)^(2d−m)dt; sumar el binomio prueba BETA.

Más precisamente Qtilde es la mezcla de una ley Binomial(d,p(t)) contra la densidad proporcional a q(t)^d en[0,1], donde

    p(t)=2rt/[1+(2r−1)t].                                (BINOMIAL)

Multiplicar la densidad por la probabilidad binomial reconstruye cada a_m r^m. Es una representación POSITIVA exacta, no un argumento formal de punto estacionario.

Para los valores REALES presentes,

    tau=1/64,
    lambda=3969/3968=(1−1/3969)^(-1),
    alpha=(64/63)^2,
    q(t)=lambda[1−alpha(t−tau)^2],
    p(tau)=1/32.                                        (MODE)

El máximo es único. lambda es EXACTAMENTE la base exponencial del polar gamma, no sólo una aproximación gaussiana.

## 4. Localización cuantitativa uniforme de Qtilde

Para d>=4096, el intervalo |t−tau|<=63/(128sqrt(d)) está contenido en(0,1). Allí q(t)^d>=lambda^d(1−1/(4d))^d>=3lambda^d/4. Por tanto

    int_0^1q(t)^d dt>=189lambda^d/[256sqrt(d)].

Fuera de |t−tau|<eta, el numerador se acota por lambda^d exp(−alpha d eta²). Así la mezcla satisface

    Prob(|t−tau|>=eta)
      <=(256/189)sqrt(d)exp(−alpha d eta²).

Además |p'(t)|<=2r<3. Si |t−tau|<epsilon/6, entonces |p(t)−1/32|<epsilon/2. La cota binomial elemental de Chernoff da Prob(|M/d−p(t)|>=epsilon/2)<=2exp(−d epsilon²/2). Se obtiene

    Qtilde_d(|M/d−1/32|>=epsilon)<=B_d(epsilon),
    B_d(epsilon)=(256/189)sqrt(d)
                  exp(−1024d epsilon²/35721)
                       +2exp(−d epsilon²/2),             (CONCENTRATION)

para d>=4096 y0<epsilon<=1/16. Una prueba de la cota binomial usa la segunda derivada del logaritmo de la mgf de Bernoulli, que es una varianza<=1/4, y luego optimiza Chernoff; no necesita aproximación normal.

## 5. La energía POLAR real tiene la misma localización

La contribución polar de S_j es exactamente

    p_j=4[r^(j+1)−s^(j+1)]<=4r^(j+1).

Como delta_v_m<=a_m/d y m<=d,

    P_d(m)p_m^T=delta_v_m sum_(j=1)^m j p_j
      <=C0 a_m r^m,
    C0=4r²/(r−1).

Se usó sum_(j=1)^m j r^(j+1)<=m r^(m+2)/(r−1). Por otro lado, la integral Laplace de rho_N da

    P_N=2A_d(r)/(u−1/2)+2A_d(s)/(u+1/2)
        >=2A_d(r)/31.

Por tanto para CUALQUIER conjunto de índices B,

    Q_d^P(B)<=3969 Qtilde_d(B).                           (POLAR-DOM)

El factor3969 se obtiene exactamente de C0·31/2. Combinado con CONCENTRATION, esto prueba M/d->1/32 bajo la energía polar REAL, sin un cálculo de nuevos N.

La fórmula gamma exacta confirma la escala exponencial:

    P_N=(4sqrt(pi)/u) Gamma(N)/Gamma(N−1/2) lambda^N.

Las cotas Jensen sqrt(N−1)<=Gamma(N)/Gamma(N−1/2)<=sqrt(N−1/2), junto a BETA, dan log(P_N)/N->loglambda y log(A_d(r))/d->loglambda. Sólo se usa una comparación de fase, no una precisión relativa entre prime y polar.

## 6. Cota aritmética inferior ELEMENTAL, demostrada

Sea psi_Lambda(x)=sum_(q<=x)Lambda(q). Para n entero, cada valoración de binom(2n,n) está acotada por el número de potencias de ese primo<=2n, pues cada diferencia de pisos en la fórmula de Legendre es0 o1. Por tanto

    psi_Lambda(2n)>=log binom(2n,n)
                   >=2nlog2−log(2n+1).

La segunda desigualdad usa que el coeficiente central es el máximo entre2n+1 coeficientes cuya suma es4^n. Para real x>=32 tome n=floor(x/2). Así

    psi_Lambda(x)>=(x−2)log2−log(x+1)>=x/2.

La última comparación vale en32 porque30log2−log33>16, y su diferencia respecto a x/2 tiene derivada log2−1/2−1/(x+1)>0 para x>=32. Se puede usar log2>2/3 y log33<4 para verificarlo. Para1<=x<=32, la positividad trivial de psi da, EN TODA la semirrecta,

    psi_Lambda(x)>=x/2−16.                              (CHEB)

No se cita esta cota sin prueba ni se la infiere de una tabla de primos.

Con w_N=x^(-1/2)rho_N(logx), H_N=−w_N'>0 y w_N(1)=1, integración por partes completa da

    Pi_N=2int_1^infty H_N(x)psi_Lambda(x)dx
         >=int_1^infty xH_N(x)dx−32
         =Lplus_N−31,
    Lplus_N=int_0^infty e^(t/2)rho_N(t)dt.

Como P_N=2(Lplus_N+Lminus_N) y Lminus_N<=2 por rho_N<=1,

    Pi_N>=P_N/2−33.                                     (PRIME-LOWER)

Ésta usa la Lambda REAL y TODO su peine. Para TODOS N>=2^20, P_N>132 y, por tanto, Pi_N>=P_N/4. Un mayorante suficiente para el umbral se verifica sin evaluar el dato W: P_N>=(4/u)lambda^N y la expansión positiva lambda^N>=[N(N+1)/(2·3969²)] ya supera132 en el umbral, creciendo después.

## 7. Localización de la energía aritmética COMPLETA

No se precisa una cota superior aritmética fina. La desigualdad trivial psi_Lambda(x)<=xlogx y el carácter decreciente de w_j=x^(-1/2)S_j(logx) prueban

    pi_j=2int w_j dpsi_Lambda
      <=2int_0^infty(t+1)e^(t/2)S_j(t)dt
      <=4[1+(j+1)/31]r^(j+1).

Las integraciones por partes tienen bordes nulos; las últimas integrales son finitas sumas gamma. Así

    P_d(m)pi_m^T<=C0[1+(d+1)/31]a_m r^m.

Para N>=2^20, PRIME-LOWER y P_N>=2A_d(r)/31 implican

    Q_d^Pi(B)
      <=15876[1+(d+1)/31]Qtilde_d(B).                    (PRIME-DOM)

El factor15876 es2·31·C0. CONCENTRATION domina este factor polinomial: M/d->1/32 TAMBIÉN bajo la energía del peine aritmético REAL COMPLETO. No se ha truncado ni modificado Lambda.

Además Pi_N está entre P_N/4 y C0[1+(d+1)/31]A_d(r), por lo que

    log(Pi_N)/N->log(3969/3968).

La fase exponencial de los dos componentes coincide. No se deduce Pi_N/P_N->1 ni una cota del residuo firmado a partir de esta igualdad de fases.

## 8. Obstrucción precisa y retorno a la compensación

Para cualquier C fijo, la ventana M<=Csqrt(d) está fuera de |M/d−1/32|<1/64 cuando d>=(64C)². POLAR-DOM/PRIME-DOM y CONCENTRATION prueban

    Q_d^P(M<=Csqrt(d))->0,
    Q_d^Pi(M<=Csqrt(d))->0.

Por contraste, P_d tiene escala sqrt(d) por035. Por tanto la ley de masa NO permite omitir las colas de estas dos energías después de separarlas: casi toda la energía polar y casi todo el peine real se sitúan en la banda LINEAL m~N/32.

ARCH permanece uniformemente acotada: los perfiles temporales de la mezcla están entre e^(-ut) y1, así que su ARCH está entre m(0) y la energía exponencial a(u). Los dos componentes de fase lambda^N no pueden tratarse como errores pequeños deducidos de la probabilidad de cola de P_d.

Ésta es una obstrucción al procedimiento separado indicado en§1, no al promedio completo t_m. Una cancelación DENTRO de t_m antes de promediar podría recuperar una ventana diferente; eso no se refuta. Si se separan prime y polar, su compensación real debe conservarse en la banda energética m~N/32, con las magnitudes aquí cuantificadas. La identidad previa018 que cancela el principal no se vende como solución nueva: deja un residuo aritmético firmado que aún hay que acotar.

No se afirma W negativa ni positiva para todos N, una nueva región de datos ni cierre del Paper47. No se continúa una campaña de índices. El resultado útil es localizar cuantitativamente dónde falla el descarte probabilístico y dónde se necesita conservar la cancelación.

## 9. Verificación

El script tools/power_moving_balance_036_verify.py compara exactamente las constantes MODE, exponentes, prefactores de dominación, el endpoint CHEB y un umbral monótono suficiente. No calcula W en nuevos N, no enumera primos ni recorre perfiles. Resultado PASS. La localización uniforme y las comparaciones aritméticas se prueban analíticamente arriba. La auditoría independiente confirma las representaciones, constantes, cota aritmética y alcance limitado a componentes. Papers intactos.
