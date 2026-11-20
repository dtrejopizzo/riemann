# POWER_HIGHPASS_DIAGONAL_DENSITY_094 — Umbral exacto de densidad L² de una unión filtrada

Estado: **PROVED, auditorías independientes aprobadas.** Véase `POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094.md`. Se calcula una distancia L² sin peso y se caracteriza cuándo una UNIÓN diagonal de espacios Q^rV_n es densa. No se afirma densidad de su envolvente lineal, continuidad de W en L² ni positividad de términos cruzados entre espacios distintos. Papers intactos.

## 1. Consulta y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos BRIDGE002, THREE002§8, PACKET_SCOPE009, CONFLUENT_BRIDGE014, HIGHPASS015, JOINT_SCALE016, DESCENT_AUDIT016,053–054 y059–060.

DESCENT_AUDIT016§§2–3 ya impide densidad en L²_eta, eta>0 común: incluso un filtro Q anula un momento continuo, y filtros de orden creciente sólo permiten límite fuerte cero. No se reintenta ese puente fuerte. THREE002§8 prueba una obstrucción L² para otra familia, con tasas que crecen exponencialmente y concentración temporal.

La diferencia aquí es una distancia EXACTA en L² SIN peso, con tasa u FIJA y TODOS los numeradores del bloque. Permite cuantificar el régimen conjunto r²/n, incluso cuando los espacios no están anidados. El determinante binomial y Dodgson son álgebra clásica; no se reclama novedad de esas herramientas.

## 2. Espacios y cambio unitario, con sus constantes

Fijar u>0 y definir, en transformadas de Laplace de funciones causales,

    V_n(u)={P(s)/(s+u)^n: deg P<n}, n>=1,
    Q(s)=s/(s+u), E_(n,r)=Q^r V_n(u), r>=0 entero.

La norma temporal es la L² ordinaria. Plancherel usa

    ||f||²=(1/(2pi))int_R |F(i tau)|²d tau.

Poner z=(s−u)/(s+u). El mapa unitario entre H² del disco y el espacio causal es

    F(s)=sqrt(2u)/(s+u) H((s−u)/(s+u)).             (CAYLEY)

En la frontera, |z|=1 y |dtheta|=2u d tau/(u²+tau²), exactamente el módulo cuadrado del prefactor. Por tanto ||f||²=int|H(e^(itheta))|²dtheta/(2pi). El mapa sobre polinomios da la base ortonormal de Laguerre; su completitud también sigue de la densidad confluente014. Así la isometría se extiende sobre todo L² causal.

CAYLEY lleva V_n sobre los polinomios de grado<n, y Q=(1+z)/2. En consecuencia E_(n,r) corresponde exactamente al subespacio

    S_(n,r)={(1+z)^r P(z): deg P<n} de H².

El factor escalar2^(−r) de Q^r no cambia el subespacio ni las distancias. El vector constante1 corresponde a f_0(t)=sqrt(2u)exp(−ut), que tiene norma1. Todo el argumento vale también en los subespacios reales.

## 3. Distancia exacta al vector base

Para TODO n>=1,r>=0,

    dist_H²(1,S_(n,r))²=1−A(n,r),
    A(n,r)=[(n+r−1)!]²/[(n−1)!(n+2r−1)!].        (EXACT-DISTANCE)

En r=0 el cociente es1 y la distancia es cero. Para probar la fórmula, usar la base b_j=z^j(1+z)^r, j=0,...,n−1. Su Gram es

    G_ij=binom(2r,r+i−j),

con coeficientes binomiales fuera de rango iguales a cero. G es definida positiva por integración de |(1+z)^rP|². Además <1,b_j>=delta_(j,0), pues el término constante de b_j es1 sólo para j=0. La norma cuadrada de la proyección de1 es por tanto

    (G^(-1))_00=det G_(n−1)/det G_n.

El determinante binomial calculado en§4 da exactamente A(n,r).

## 4. Determinante binomial: prueba por Dodgson

Para enteros a,b>=0, definir

    D_n(a,b)=det[binom(a+b,a+i−j)]_(i,j=0,...,n−1), D_0=1.

La identidad es

    D_n(a,b)=producto_(j=0)^(n−1)
                   j!(a+b+j)!/[(a+j)!(b+j)!].       (BINOMIAL-DET)

Los casos n=0,1 son directos. Si a=0 o b=0 la matriz es triangular con diagonal1, igual al producto. Para a,b>=1, la identidad Desnanot–Jacobi aplicada a las cuatro esquinas da

    D_n(a,b)D_(n−2)(a,b)=D_(n−1)(a,b)²
       −D_(n−1)(a−1,b+1)D_(n−1)(a+1,b−1).

Suponer por inducción la fórmula para tamaños menores. El cociente del producto cruzado por D_(n−1)(a,b)² es

    producto_(j=0)^(n−2) [(a+j)(b+j)]/[(a+j+1)(b+j+1)]
       =ab/[(a+n−1)(b+n−1)].

Por tanto el factor de la recurrencia es

    1−ab/[(a+n−1)(b+n−1)]
       =(n−1)(a+b+n−1)/[(a+n−1)(b+n−1)].

Es precisamente el cociente entre los dos últimos factores consecutivos de BINOMIAL-DET. Como D_(n−2)>0 por la fórmula inductiva, se puede dividir y queda probada la identidad. Tomar a=b=r y dividir D_(n−1)/D_n prueba EXACT-DISTANCE, incluyendo n=1 con D_0=1.

## 5. Régimen cuantitativo r²/n

Para r>=1,

    A(n,r)=producto_(j=0)^(r−1)(n+j)/(n+r+j).

Las desigualdades log(1−y)<=−y y log(1−y)>=−y/(1−y),0<y<1, dan

    exp(−r²/n)<=A(n,r)<=exp[−r²/(n+2r−1)].        (TWO-SIDED)

La cota izquierda también vale en r=0. En particular la distancia al vector base tiende a cero a lo largo de dimensiones n→infinito SI Y SÓLO SI r²/n→0. Para la necesidad, si r>=n el exponente de la cota superior es mayor que r/3; si r<n es mayor que r²/(3n). Así no puede tender a cero mientras r²/n esté separado de cero.

También hay una aproximación cuantitativa de cualquier polinomio fijo P(z)=sum_(m=0)^M c_m z^m. Si n>M,

    dist(P,S_(n,r))
       <=sum_(m=0)^M |c_m|sqrt[1−A(n−m,r)]
       <=r sum_(m=0)^M |c_m|/sqrt(n−m).             (POLYNOMIAL-APPROX)

En efecto z^m S_(n−m,r) está contenido en S_(n,r), y multiplicar por z^m preserva la norma H². Aproximar cada monomio y sumar dentro del MISMO espacio lineal da la primera desigualdad. La segunda usa1−exp(−y)<=y. No se están sumando aproximantes pertenecientes a bloques distintos.

## 6. Criterio exacto para la UNIÓN diagonal, sin monotonía de r

Sea r(n) una asignación arbitraria de enteros no negativos, n=1,2,..., sin suponer monotonía. Entonces

    cierre_L²(unión_(n>=1) E_(n,r(n)))=L²(0,infinito)
       SI Y SÓLO SI liminf_(n→infinito) r(n)²/n=0.  (DIAGONAL-DENSITY)

Se trata del cierre de la UNIÓN, no de su envolvente lineal.

Suficiencia: elegir una subsucesión n_k→infinito con r(n_k)²/n_k→0. POLYNOMIAL-APPROX muestra que cada polinomio fijo se aproxima por elementos de S_(n_k,r(n_k)). Los polinomios son densos en H²; aproximar primero el objetivo por un polinomio y después ese polinomio por un único bloque prueba la densidad de la unión. No se usó anidamiento.

Necesidad, incluidos los casos finitos r=0: si el liminf no es cero, existen0<delta<=1 y N tales que r(n)²/n>=delta para todo n>=N. TWO-SIDED y los dos casos r<n/r>=n dan

    dist(1,S_(n,r(n)))>=d=sqrt[1−exp(−delta/3)]>0, n>=N.

Los bloques excepcionales n<N son finitos, aunque algunos tengan r=0 y contengan al vector1. Elegir M mayor que TODOS sus grados máximos n+r(n)−1, y epsilon=d/2. El vector

    H_*=1+epsilon z^M

queda a distancia al menos epsilon de cada bloque excepcional, porque z^M es ortogonal a todos sus polinomios. Para n>=N, la desigualdad triangular da

    dist(H_*,S_(n,r(n)))>=d−epsilon=d/2.

Así H_* tiene distancia positiva a la unión completa. Esto evita suponer que el vector1 sirve como testigo cuando se han añadido finitos bloques sin filtro.

## 7. Obstrucción uniforme para los conos positivos conocidos

Si r>=n>=1, TWO-SIDED implica

    A(n,r)<exp(−1/3)<3/4,
    dist(1,S_(n,r))>1/2.

La segunda comparación usa exp(1/3)>1+1/3=4/3. Por tanto la unión de TODOS los bloques E_(n,r) con r>=n no es densa ni siquiera en L² sin peso, con la distancia uniforme anterior. En particular esto se aplica al cono060

    r>=10^12[n ceil(log_2(n+1))]^3,

que ya exige r>=n. No se vuelve a probar su signo ni se presenta esta obstrucción como un signo W negativo.

Añadir una cantidad finita de bloques confluentes sin filtro a la MISMA tasa tampoco basta. Si sus grados son menores que M, el vector1+z^M/4 tiene distancia al menos1/4 a esos bloques y mayor que1/4 a todo el cono r>=n, por la desigualdad triangular. Su imagen CAYLEY proporciona un testigo causal explícito. La afirmación no incluye otras familias continuas de tasas ni sumas arbitrarias de miembros de bloques distintos.

## 8. Alcance respecto del problema del signo

016 ya descartaba el puente fuerte en una norma ponderada común.094 añade el umbral EXACTO de densidad de la unión diagonal en la topología MÁS DÉBIL L², y una obstrucción cuantitativa para los conos de signo actuales. Si algún futuro cono positivo alcanzara r=o(sqrt n) en una subsucesión, DIAGONAL-DENSITY daría aproximación L²; aun así habría que justificar continuidad de la forma COMPLETA en la topología utilizada. Aquí no se deduce W de esa densidad.

Tampoco se afirma nada sobre densidad de la envolvente lineal de la unión. La positividad de cada bloque no paga automáticamente los cruces entre bloques. Las vías de mezclas o descenso con compensación específica permanecen abiertas. No se modifica ningún paper ni se cierra el objetivo global.
