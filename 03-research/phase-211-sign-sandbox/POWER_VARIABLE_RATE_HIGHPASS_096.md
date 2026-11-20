# POWER_VARIABLE_RATE_HIGHPASS_096 — Proyección uniforme en la tasa

Estado: **PROVED, auditorías independientes aprobadas.** Véase `POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096.md`. Resultado: para r>=10^12n³, la proyección de un exponencial fijo sobre Q_u^rV_n(u) tiene norma cuadrada <=200n/sqrt(r), uniformemente en TODA tasa u>0. No se afirma signo negativo de W, densidad de una envolvente lineal ni continuidad de W en L². Papers intactos; sin campañas.

## 1. Consulta y diferencia

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos015–016,053–054,059–060 y094.016 impide densidad en una norma exponencial ponderada común.094 calcula distancias L² sin peso a tasa fija. Ninguno de esos argumentos uniformiza la comparación con un objetivo fijo al variar u: el vector constante de Cayley también cambia con la tasa.

Aquí se mantiene FIJO f_0(t)=sqrt(2u_0)exp(−u_0t), u_0>0, y se permite cualquier u>0 en el aproximante. El nuevo objeto es la proyección sobre todos los numeradores de Q_u^rV_n(u), no una diagonal escalar ni una norma ponderada. La prueba propuesta separa una región interior real mediante Gegenbauer y la región restante mediante la Gram exacta094.

## 2. Fórmula de proyección y notaciones

Usar el Cayley unitario de094 a tasa u. El objetivo fijo se transforma en

    H_a(z)=sqrt(1−a²)/(1+az), a=(u−u_0)/(u+u_0), −1<a<1.

El espacio filtrado se transforma en S_(n,r)=(1+z)^r P_(n−1), donde el factor2^(−r) no cambia el subespacio. Poner xi=−a. Si G_ij=binom(2r,r+i−j), i,j=0,...,n−1 y v=(1,xi,...,xi^(n−1)), la norma cuadrada de la proyección es

    A_(n,r)(xi)=(1−xi²)(1+xi)^(2r) v^tG^(-1)v.     (PROJECTION)

Equivalentemente,

    A_(n,r)(xi)=(1−xi²)(1+xi)^(2r)
      ·sup_(degP<n) |P(xi)|²/int_T|(1+z)^rP(z)|²dtheta/(2pi).

Esto sigue de <H_a,z^j(1+z)^r>=sqrt(1−a²)(1−a)^r(−a)^j y la fórmula de proyección en una base Gram. Todos los valores xi∈(−1,1) corresponden a una tasa u>0. Los extremos no se incluyen, pero las cotas siguientes son uniformes hasta ellos.

Se prueba la cota

    A_(n,r)(xi)<=200n/sqrt(r),
    TODOS n>=1, r>=10^12n³, −1<xi<1.              (TARGET)

## 3. Lema de Gegenbauer con sus constantes

Para lambda>=1, sea C_k^lambda el polinomio definido por

    C_k^lambda(y)=sum_(j=0)^floor(k/2)
       (−1)^j (lambda)_(k−j)(2y)^(k−2j)/[j!(k−2j)!].

Es ortogonal para el peso(1−y²)^(lambda−1/2), y su norma cuadrada es

    h_k=pi·2^(1−2lambda)Gamma(k+2lambda)
             /[k!(k+lambda)Gamma(lambda)²].

Verificación autónoma: la fórmula de Rodrigues es

    C_k^lambda(y)= (−1)^k(2lambda)_k
       /[2^k k!(lambda+1/2)_k]
       ·(1−y²)^(1/2−lambda) D^k(1−y²)^(k+lambda−1/2).

Comparar coeficientes verifica Rodrigues. Integrar k veces por partes prueba ortogonalidad; todos los bordes se anulan para lambda>=1. Para la norma, D^kC_k=2^k(lambda)_k, y queda

    h_k=(2lambda)_k(lambda)_k/[k!(lambda+1/2)_k]
                  ·B(1/2,k+lambda+1/2),

igual a la fórmula anterior por la duplicación de Gamma. Así no se importa una cota asintótica con constantes implícitas.

Escribir p_k=C_k/sqrt(h_k). Las identidades de Gamma dan

    |p_(2m)(0)|²=(2m+lambda)/pi
       ·Gamma(m+1/2)/Gamma(m+1)
       ·Gamma(m+lambda)/Gamma(m+lambda+1/2),

    |p_(2m+1)'(0)|²=4(2m+1+lambda)/pi
       ·Gamma(m+3/2)/Gamma(m+1)
       ·Gamma(m+lambda+1)/Gamma(m+lambda+1/2).

Para x>1/2,

    sqrt(x−1/2)<=Gamma(x+1/2)/Gamma(x)<=sqrt(x).

La cota superior es Jensen para sqrt(T) bajo una ley Gamma(x); la inferior sigue de Cauchy–Schwarz Gamma(x)²<=Gamma(x−1/2)Gamma(x+1/2), junto con Gamma(x+1/2)=(x−1/2)Gamma(x−1/2). Además Gamma(m+1/2)/Gamma(m+1)<=sqrt(pi), por el producto de los cocientes(j+1/2)/(j+1). Por tanto, si los grados considerados son<n,

    |p_(2m)(0)|²<=4sqrt(lambda+n),
    |p_(2m+1)'(0)|²<=16n(lambda+n)^(3/2).          (BASE-VALUES)

Para s>=0, los coeficientes explícitos también dan

    |p_(2m)(is)|<=|p_(2m)(0)|
             ·exp[2s sqrt(m(lambda+2m))],
    |p_(2m+1)(is)|<=s|p_(2m+1)'(0)|
             ·exp[2s sqrt(m(lambda+2m+1))].        (IMAGINARY)

En efecto, en el caso par el cociente respecto del valor en0 es la suma positiva

    sum_(j=0)^m (lambda+m)_j m_fall_j (2s)^(2j)/(2j)!,

acotada por cosh(2s sqrt(m(lambda+2m))). En el caso impar, después de dividir por s p'(0), aparece la misma suma con(lambda+m+1)_j y(2j+1)!; se acota por sinh(X)/X<=exp(X), incluido X=0 por continuidad. No se pierde una cancelación al evaluar en is: todos los términos tienen la misma fase.

## 4. Polinomio centrado y separación de paridades

Poner d=n−1 y T(theta)=exp(−idtheta/2)P(exp(itheta)). Con y=sin(theta/2), si d es par,

    T=E(y)+i sqrt(1−y²)O(y),

donde E es par de grado<=d y O impar de grado<=d−1. Si d es impar,

    T=sqrt(1−y²)E(y)+iO(y),

con E par de grado<=d−1 y O impar de grado<=d. Son las identidades polinómicas de cos y sin de frecuencias enteras o semienteras; valen también para coeficientes complejos.

La simetría y↔−y elimina el cruce en la norma. Después de extraer4^r de |1+z|^(2r), la norma circular es

    (4^r/pi)(||E||_(lambda_E)²+||O||_(lambda_O)²),

con (lambda_E,lambda_O)=(r,r+1) para d par y(r+1,r) para d impar. Aquí ||.||_lambda usa el peso de§3 y dy, sin factor1/pi. El factor1/pi viene de dtheta=2dy/sqrt(1−y²), sobre theta∈[−pi,pi].

## 5. Región xi=exp(−eta), 0<=eta<=1

Para 0<xi<=1, poner eta=−log xi y s=sinh(eta/2). Evaluar theta=ieta da y=is y

    P(xi)=xi^(d/2)T(ieta).

En esta sección eta<=1, por lo que s<=eta<=1. Usar los polinomios ortonormales pares e impares de§3. Las cotas BASE-VALUES/IMAGINARY, el número de términos<=n y lambda∈{r,r+1} dan, cuando r>=1024n,

    K_E(is)<=8n sqrt(r) exp[8s sqrt(nr)],
    K_O(is)<=96n²r^(3/2)s² exp[8s sqrt(nr)].

K_E,K_O son las sumas de cuadrados de las evaluaciones de sus bases ortonormales; grados ausentes producen suma vacía. Se usó lambda+n<=3r y4sqrt(3)<8. Las dos paridades de§4 y Cauchy–Schwarz dan

    |T(ieta)|²/(||E||²+||O||²)
       <=[16n sqrt(r)+192n²r^(3/2)s²]
                          ·exp[8s sqrt(nr)].       (CENTER-KERNEL)

El factor2 permite tanto K_E+(1+s²)K_O como(1+s²)K_E+K_O. Esto incluye n=1: sólo queda el polinomio constante par.

En PROJECTION, pi<4, xi^d<=1 y1−xi²<=2eta. Además

    ((1+xi)/2)^(2r)
       =exp(−r eta)cosh(eta/2)^(2r)
       <=exp(−3r eta/4),

porque log cosh x<=x²/2 y eta<=1. Finalmente8sqrt(nr)<=r/4 para r>=1024n. CENTER-KERNEL implica

    A_(n,r)(xi)
      <=128n sqrt(r) eta exp(−r eta/2)
          +1536n²r^(3/2)eta³exp(−r eta/2)
      <128n/sqrt(r)+41472n²/r^(3/2)
      <200n/sqrt(r).                              (NEAR)

Se usaron max_(eta>=0)eta exp(−r eta/2)=2/(er)<1/r y max eta³exp(−r eta/2)=(6/(er))³<27/r³, junto con r>=1024n. El límite eta=0 de la cota no se interpreta como un vector Hardy en el extremo; sólo proporciona uniformidad para xi<1.

## 6. Región restante −1<xi<=exp(−1)

Esta región incluye TODOS los xi negativos. Poner C=binom(2r,r). El determinante094 y r>=n dan

    det G>=C^n producto_(j=0)^(n−1) j!/(2r)^j
          >=C^n(2r)^(−n(n−1)/2).

En efecto, cada cociente del factor j respecto de C es j!(2r+1)_j/(r+1)_j²>=j!/(2r)^j. Como tr G=nC,

    lambda_min(G)>=det G/(nC)^(n−1).

Para |xi|<=1 se tiene ||v||²<=n. Además C>=4^r/(2r+1), porque es el mayor de los2r+1 coeficientes de(1+z)^(2r). Como1+exp(−1)<3/2, PROJECTION queda acotada por

    A_(n,r)(xi)
       <=(2r+1)(9/16)^r n^n(2r)^(n(n−1)/2).       (FAR-GRAM)

Para r>=10^12n³, el logaritmo de todos los factores salvo(9/16)^r es menor que r/100. En detalle:

    log(2r+1)<=2sqrt(r)<=r/500000,
    n log n<=n²<=r/10^12,
    [n(n−1)/2]log(2r)<=n²r^(1/3)<=r/10^8.

La última línea usa log(2r)<2r^(1/3), obtenida maximizando log x/x^(1/3), y r^(2/3)>=10^8n². La suma de las tres constantes es menor que1/100. Por e<3 y sqrt(3)<16/9 se tiene log(16/9)>1/2. Así FAR-GRAM implica

    A_(n,r)(xi)<exp(−r/4)<1/sqrt(r)<=200n/sqrt(r).  (FAR)

La comparación final usa exp(r/4)>1+r/4>=sqrt(r). No se utiliza una aproximación asintótica en r o n.

## 7. Consecuencia probada y alcance

NEAR y FAR prueban TARGET para TODO u>0, u_0>0 y r>=10^12n³. Como r>=10^12n³ implica200n/sqrt(r)<=1/5000, la distancia del exponencial FIJO normalizado a la UNIÓN de TODOS esos espacios, permitiendo todas las tasas, es al menos

    sqrt(1−1/5000).

El cono positivo060, r>=10^12[n ceil(log_2(n+1))]^3, está incluido. Esto impide usar variación de la tasa para reparar la densidad L² de su UNIÓN. No trata la adición de otras familias continuas de bloques iniciales, ni sumas con cruces no certificados, ni la envolvente lineal de la unión. Tampoco refuta el signo W de ningún miembro.

Las constantes de Gegenbauer, la separación de paridades, ambos rangos de xi y la interpretación de PROJECTION como NORMA CUADRADA fueron auditados independientemente. No se registra como teorema de signo ni como cierre global.
