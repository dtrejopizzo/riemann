# POWER_POLYNOMIAL_003 — Coordenadas polinomiales y dilataciones exactas

Estado: PROVED identidades. OPEN signo uniforme. Certificado de grados 0,1,2 por aritmética racional encargado en paralelo a `signo`; no se duplica aquí. Papers intactos.

Antecedentes: las reglas del proyecto/índice/grid/crucigrama consultados en POWER_BRIDGE_002. La reducción Pick y la eliminación matricial son conocidas. Diferencia explícita: el puente ahora probado permite fijar una sola escalera 32+n; aquí se escribe su forma completa en una base Jacobi con medidas y dilataciones exactas. El objetivo es conservar cancelaciones de polinomios, sin reclamar que coordenadas nuevas impliquen signo.

## 1. Forma exacta sobre polinomios

Sea h(y)=exp(-63y/2)P(exp(-y))1_(y>0), P real. Ponga z=exp(-y) y

    <P,Q>_J=∫_0^1 z^62 P(z)Q(z) dz,
    D_n P(z)=P(z/n).

Entonces ||h||²=<P,P>_J y el peine es exactamente

    Comb[P]=−2 Σ(n>=2)Lambda(n)n^-32 <P,D_nP>_J.             (C)

No se extiende P(z/n) por cero ni se recorta su dominio: para autocorrelación se evalúa h(y+log n), y y>0 ya satisface ambas restricciones. El término polar es exactamente

    Polar[P]=2 (∫_0^1 z^30 P(z)dz)(∫_0^1 z^31 P(z)dz).       (P)

Si P=Σp_i z^i, la parte arquimediana tiene matriz

    A_ij=[psi((32+i)/2)+psi((32+j)/2)−2log pi]/[2(63+i+j)].  (A)

Así C+P+A reproduce el kernel de POWER_CONE_001 en coeficientes de las imágenes h, sin factores zeta. Las imágenes de los datos rho tienen coeficientes p_i=c_i zeta(32+i); la transformación diagonal es invertible y positiva.

## 2. Base Jacobi explícita

Sean q_j los polinomios mónicos ortogonales para z^62 dz. Por Rodrigues,

    q_j(z) = z^-62 /[j! C_j] d^j/dz^j [z^(62+j)(z-1)^j],
    C_j=binom(62+2j,j),
    ||q_j||²_J=1/[(63+2j) C_j²].

Primeros casos:

    q0=1,                         norm²=1/63,
    q1=z−63/64,                  norm²=1/(65·64²),
    q2=z²−64z/33+4032/4290,       norm²=1/(67·2145²).

La base ortonormal es e_j=sqrt(63+2j) C_j q_j. No conviene usar monomios numéricamente: sus casi-cancelaciones cerca de z=1 desaparecen en esta normalización exacta.

Para r>-1, integración por partes en Rodrigues da

    ∫_0^1 z^r q_j(z)dz = (r-62)_(j) /[C_j (r+1)(r+2)...(r+j+1)],

donde (x)_(j)=x(x-1)...(x-j+1). Es aplicable a r=30,31 y da todos los momentos polares por productos racionales. Cada diagonal polar es positiva porque ambos momentos tienen signo (-1)^j; eso no implica positividad de la matriz polar completa.

## 3. Matriz de las dilataciones

En cualquier grado finito d, D_n preserva polinomios de grado ≤d y es triangular en la base q_j, con diagonal n^-j. Si q_j(z)=Σ_l a_jl z^l,

    <q_i,D_n q_j>_J = Σ(k,l) a_ik a_jl n^-l /(63+k+l).       (D)

Todos los factores salvo las sumas aritméticas son racionales. Tras sumar Λ(n)n^-32, cada entrada usa exclusivamente los valores −zeta'(32+l)/zeta(32+l). Por tanto esta coordenatización no crea nueva información aritmética: organiza exactamente la misma matriz.

Primeras imágenes, útiles para verificar implementaciones:

    D_n q0=q0,
    D_n q1=n^-1 q1+(63/64)(n^-1−1)q0.

Aunque los eigenvalores n^-j son positivos y ≤1, D_n no es autoadjunto para z^62dz. No puede sustituirse por una contracción positiva. El término fuera de diagonal de D_n q1 lo demuestra ya en grado uno; diagonalizar dilataciones y olvidar la métrica perdería el signo.

## 4. Ensayo concreto que esta representación permite

Para d=2, forme A por (A), C por (D) y P por los dos vectores racionales de momentos. Conjugue por la matriz de q0,q1,q2 y luego por sus normas exactas. El certificado de signo debe aplicarse a la suma COMPLETA. Ni las diagonales polares positivas ni los eigenvalores de D_n son certificados. Las entradas pueden reducirse a racionales, gamma, log pi, log2 y tres sumas Dirichlet con restos de signo, como está haciendo el cálculo independiente `signo`.

Para grados crecientes, el objetivo falsable adicional es encontrar una estimación de forma en la base e_j que controle los bloques de C+P frente a A sin perder las cancelaciones del término triangular D_n. Aquí no se ha obtenido tal desigualdad. La ventaja demostrada es exactitud de coordenadas y normalización; no se afirma una nueva prueba del signo.
