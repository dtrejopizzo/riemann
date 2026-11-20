# POWER_POLE_MOVEMENT_004 — Movimiento individual de polos por covarianza

Estado: PROVED (movimiento de polos de la parte arquimediana y control uniforme prime/polar); CITED el certificado racional confluente de POWER_CONFLUENT_004. No modifica papers.

Revisión independiente: se aprobó la covarianza, la identificación común de numeradores y min–max para todas las eigenenergías; aprobó también WT=1302 y reejecutó el certificado confluente (margen 79/700>1/10). Las cotas de esta nota son deliberadamente algo más débiles que las obtenidas en dicha revisión.

## 1. Corpus y diferencia concreta

Búsquedas dirigidas: índice ROUTES-TRIED-INDEX (Takenaka, model space, confluent, pole movement, Müntz), grid maestro/partes, crucigrama, phase211. Antecedentes generales de bases racionales y funciones completamente monótonas no prueban el movimiento. POWER_ARCH_TRIPLE_004 registra explícitamente la conjetura local y un diagnóstico sin prueba. La razón nueva es una comparación EXACTA de cocientes Rayleigh conservando el numerador racional al mover un solo polo; no es dilatación global ni diferenciación de coeficientes fijos en una base móvil.

## 2. Teorema: todas las eigenenergías arquimedianas crecen al aumentar polos

Sean u_1,...,u_n>0, permitiendo multiplicidades; el espacio correspondiente es el span de y^k exp(-u_j y)1_{y>0}, con k menor que cada multiplicidad. Su transformada de Fourier es exactamente

    fhat(tau)=P(i tau)/Π_j(u_j+i tau), deg P<n.

Los coeficientes de P son reales para f real; el mismo argumento admite complejos. Es un espacio de numeradores FIJO, independiente de los polos.

Si v_j>=u_j para cada j, para un mismo numerador P el peso espectral nuevo es el antiguo multiplicado por

    R(tau)=Π_j (u_j²+tau²)/(v_j²+tau²).

R es positiva, acotada y creciente como función de |tau|. El multiplicador m(tau)=Re psi(1/4+i tau/2)-log pi es también creciente en |tau|: cada sumando de su serie

    m(tau)=m(0)+Σ_{k>=0} [(tau/2)²/((k+1/4)((k+1/4)²+(tau/2)²))]

lo es estrictamente. Normalice el peso antiguo a una probabilidad dμ. Entonces

    Rayleigh_v(P)-Rayleigh_u(P)
      =Cov_μ(m,R)/E_μ R >=0.

La desigualdad no requiere ninguna propiedad de P: la covarianza es la mitad de la integral doble de

    [m(tau)-m(sigma)][R(tau)-R(sigma)],

no negativa porque ambos factores tienen el mismo signo al comparar |tau| y |sigma|. La integrabilidad viene de deg P<n y m=O(log(2+|tau|)). Por min–max sobre el mismo espacio de polinomios, TODAS las eigenenergías comprimidas ordenadas son no decrecientes al aumentar individualmente los polos. En particular

    lambda_min_arch(u_1,...,u_n)
        >=lambda_min_arch(u,...,u),  u=min_j u_j.             (PM)

Se permiten polos repetidos desde el principio, sin argumento de estabilidad numérica. La comparación entre espacios usa la correspondencia racional P/D_u -> P/D_v; no sostiene que una función temporal fija conserve sus coeficientes al mover polos.

## 3. Forma diferencial exacta y estrictitud

Al variar sólo u_k y conservar P,

    d Rayleigh/du_k = Cov_μ(m, -2u_k/(u_k²+tau²)) >=0.

Esta segunda función es creciente en |tau|. Se puede diferenciar bajo la integral, pues en compactos u_k>0 el factor logarítmico está acotado y m es integrable contra los pesos racionales. Es una fórmula que incluye la variación del denominador de la norma; omitir ese término daría una derivada incorrecta. Si el polo aumenta estrictamente y P no es nulo, la covarianza es estrictamente positiva, pues la densidad no está concentrada en un único |tau|.

## 4. Peine y polar uniformes sin cota superior de los polos

Esta sección aplica la observación del constructor principal. Para u_j>=u, la base ortonormal racional tiene transformada

    F_j(s)=sqrt(2u_j)/(s+u_j) Π_{k<j}(s-u_k)/(s+u_k).

Cada factor all-pass en tiempo es delta_0-2b exp(-by)1_{y>0}. Multiplicar por exp(uy/2) conjuga la convolución; la norma L1 de cada filtro ponderado es a lo sumo

    1+2b/(b-u/2)<=5.

La exponencial inicial normalizada tiene norma L2 ponderada <=sqrt2. Por Young y Cauchy--Schwarz en los coeficientes ortonormales,

    ||exp(uy/2) f||² <= B_n ||f||²,
    B_n=2Σ_{j=0}^{n-1}25^j=(25^n-1)/12.                     (WT)

Esto implica |c_f(t)|<=sqrt(B_n)exp(-ut/2)||f||². Para n=3 y u>=63/2, B_3=1302 y

    |peine|<=2sqrt1302 Σ_{q>=2}Lambda(q)q^{-(u+1)/2}||f||²
          <=74 Σ_{q>=2}q^-15 ||f||²
          <=74/(28672)||f||² < (3/1000)||f||².

Se usó sqrt1302<37, Lambda(q)<=logq<=q y (u-1)/2>=61/4>15, y Σ_{q>=2}q^-15<=2^-15(1+2/14)=1/28672.

Para el polar, sean A=∫f exp(y/2), B=∫f exp(-y/2). Para reales f,

    2AB=(A+B)²/2-(A-B)²/2 >=-(A-B)²/2.

La integral ponderada exacta es

    ∫_0^∞4sinh²(y/2)exp(-uy)dy=2/[u(u²-1)].

Por (WT) y Cauchy--Schwarz,

    polar >=-1302/[u(u²-1)] ||f||² >-(21/500)||f||²

para u>=63/2, por aritmética racional. Se conserva la cancelación A≈B; la cota grosera por |AB| la destruye.

## 5. Consecuencia para TODAS las ternas de exponentes >=32

POWER_CONFLUENT_004 certifica con aritmética racional lambda_min_arch(63/2,63/2,63/2)>1/10 (input CITED aquí). Por (PM) y §4, para TODAS las ternas de exponentes a_i>=32 y todos los coeficientes reales,

    Q[Σ c_i X^-a_i] >= (1/10-21/500-3/1000)||f||²
                     =11/200 ||f||² >||f||²/20,

con f=Σ c_i zeta(a_i)exp(-(a_i-1/2)y). El mismo razonamiento incluye límites confluentes de tres potencias, interpretados como exponenciales por polinomios.

Este resultado NO se extiende a n arbitrario con u fijo por §4: B_n crece como 25^n, y además la menor eigenenergía confluente disminuye al aumentar n. No se ha demostrado positividad arquimediana uniforme en dimensión. El avance analítico es eliminar por completo la separación y la cota superior de las tres tasas, mediante el nuevo teorema de movimiento individual de polos.
