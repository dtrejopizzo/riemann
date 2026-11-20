# POWER_HIGHPASS_015 — Positividad eventual uniforme de una órbita racional de dimensión fija

Estado: PROVED, revisado independientemente en POWER_HIGHPASS_AUDIT_015.md. No se afirma positividad de los primeros miembros ni uniformidad en la dimensión. Papers intactos.

## 1. Antecedentes y diferencia explícita

Consultados las reglas del proyecto, índice/grid/crucigrama según los puentes previos; entradas high-frequency/exterior A001 y high-prolate ROUND010A; COMMON_TRANSFER010, CONFLUENT_BRIDGE014 y SIGNED_TRANSFER014. La coercividad genérica en frecuencia alta y sus límites sobre bloques prolates ya constan. No se reintenta usarla para declarar positivos todos los tests ni toda una cola de índices prolates.

Aquí el objeto distinto es una órbita racional EXACTA: mantener N y su espacio de numeradores fijos y aplicar repetidamente Q(s)=s/(s+u). Se identifica su escala de norma y frecuencia, se controla TODO el peine por un peso temporal uniforme y se prueba el signo eventual de TODA esa órbita de dimensión N. Ninguna condición de portador arbitrario se deduce de «frecuencias grandes» sin verificarla.

## 2. Teorema

Fije u>1; en esta fase u=63/2. Sea N>=1. Para un polinomio real P no nulo, gradoP<N, defina la función causal f_(k,P) mediante

    F_(k,P)(s)=[s/(s+u)]^k P(s)/(s+u)^N, k=0,1,2,... .

Existe un entero K_N, dependiente de u y N pero NO de P, tal que

    W[f_(k,P)]>0 para todo k>=K_N y todo P!=0,gradoP<N.   (EVENTUAL)

Más precisamente, uniformemente en los numeradores,

    Arch[f_(k,P)]/||f_(k,P)||² >=(1/2)log k−C_N,
    Comb[f_(k,P)]/||f_(k,P)||² ->0,
    Polar[f_(k,P)]/||f_(k,P)||² ->0.                      (U)

Para un P FIJO, si r=N−degP>=1, se obtiene además el valor asintótico completo

    W[f_(k,P)]/||f_(k,P)||²
       =(1/2)log k+log[u/(2pi)]−(1/2)psi(r−1/2)+o(1).    (ASYM)

No se necesita una campaña de certificados ni se ha usado información sobre objetos espectrales externos a la forma.

## 3. Escala de Gram que permite uniformidad en TODOS los numeradores

Escriba P(s)=Σ(j=0..N−1)a_j s^j y, para k>=1, b_j=a_j k^(j/2). Esta transformación diagonal es invertible para cada k; por ello una estimación uniforme en b cubre también numeradores que varían con k.

Para 0<=eta<u/2, ponderar la función por e^(eta y) equivale a evaluar F en s=−eta+i tau. Cambie tau=sqrt(k)x y ponga

    d_eta=u(u−2eta)>0,
    W_(k,eta)(x)=
      [(x²+eta²/k)/(x²+(u−eta)²/k)]^k
      [x²+(u−eta)²/k]^-N,
    B_(k,eta)(x)=Σ_j b_j(ix−eta/sqrt(k))^j.

Parseval da EXACTAMENTE

    k^(N−1/2)||e^(eta y)f_(k,P)||²
       =(1/2pi)∫ W_(k,eta)(x)|B_(k,eta)(x)|²dx.          (GRAM)

Las matrices de esta forma cuadrática convergen, entrada por entrada y en norma, a

    G_eta[b]=(1/2pi)∫ |x|^-2N exp(−d_eta/x²)
                             |Σ_j b_j(ix)^j|²dx.        (LIMIT)

Cada G_eta es definida positiva: su peso es positivo para x!=0 y ningún polinomio no nulo puede anularse casi en todas partes. Como la dimensión N es fija, su menor eigenvalor es estrictamente positivo.

### Dominación necesaria, sin suponer convergencia de densidades

Sea y=x²+(u−eta)²/k. El factor de cociente satisface

    [(x²+eta²/k)/(x²+(u−eta)²/k)]^k
      =[1−d_eta/(ky)]^k<=exp(−d_eta/y).

En |x|<=1, los monomios trasladados son uniformemente acotados y exp(−d_eta/y)y^-N está acotado para y>0. Esto da un majorante constante integrable en ese intervalo. Para |x|>=1, se usa cociente<=1 y la cota C_N|x|^(i+j−2N) para cada entrada i,j; como i,j<=N−1, el exponente es <=−2. Es integrable. Por convergencia dominada se obtiene también convergencia L¹ de CADA densidad matricial, no solo de sus integrales.

En particular, para eta fijo en (1/2,u/2), GRAM/LIMIT y positividad de G_0 dan, uniformemente en P para k suficientemente grande,

    ||e^(eta y)f_(k,P)||² <=C_(N,eta)||f_(k,P)||².        (WT)

Aquí u>1 es exactamente lo que permite elegir ese eta; no se presume esta condición para u meramente mayor que1/2.

## 4. Parte arquimediana: log k más un bloque acotado

El símbolo satisface m(tau)=log(|tau|/(2pi))+o(1) cuando |tau| crece y |m(tau)−log(2+|tau|)|<=C. Para x!=0,

    m(sqrt(k)x)−(1/2)log k ->log(|x|/(2pi)).

Las matrices correspondientes de GRAM, insertando ese multiplicador, también convergen. Para justificarlo cerca de x=0, |m(sqrt(k)x)−(1/2)log k| se acota por C+|log y| con y=x²+u²/k, usando la comparabilidad entre |x|+2/sqrt(k) y sqrt(y). Multiplicar por exp(−u²/y)y^-N conserva un majorante acotado. En |x|>=1 basta C+log|x|, integrable contra |x|^-2.

Así la matriz de Arch menos (1/2)log k veces la matriz de norma converge a la forma logarítmica finita definida por LIMIT. Comparar sus normas con el menor eigenvalor positivo de G_0 prueba la primera desigualdad U, uniformemente en b y por tanto en TODOS los numeradores P.

## 5. Cada contacto desaparece y la cola completa queda dominada

Para t>0 fijo, la correlación es la integral de la densidad matricial no ponderada de §3 contra exp(i sqrt(k)xt). Esa densidad converge en L¹ a la de LIMIT. Por el lema de Riemann–Lebesgue,

    sup_(P!=0) |c_f(k,P)(t)|/||f_(k,P)||² ->0.           (RL)

En detalle, se resta la densidad límite en L¹, y el límite restante es la transformada Fourier de una función L¹ a frecuencia sqrt(k)t; se hace esto para las N² entradas y se compara con G_0. No se aplica RL sin controlar la variación de la densidad con k.

WT y Cauchy–Schwarz desplazado dan simultáneamente

    |c_f(k,P)(log q)|/||f_(k,P)||² <=C_(N,eta)q^-eta.

Como eta>1/2, Σ(q>=2)2Lambda(q)q^(-eta−1/2) converge. Se separa un segmento finito, donde RL es uniforme, y la cola, dominada uniformemente por esta serie. Esto prueba que el peine COMPLETO dividido por la norma tiende a cero uniformemente en P. No se supone signo favorable de ningún contacto.

## 6. El polar decae exponencialmente, incluso uniformemente en P

En los momentos s=±1/2,

    Q(−1/2)Q(1/2)=−1/[4(u²−1/4)].

Por tanto Polar[f_(k,P)]=[−1/(4u²−1)]^k Polar[f_(0,P)]. Para u=63/2 el factor es −1/3968.

En coordenadas b, los coeficientes iniciales son a_j=k^(-j/2)b_j. Las dos evaluaciones de P(±1/2) son funcionales uniformemente acotados en b para k>=1; los denominadores iniciales son constantes. De aquí |Polar[f_(0,P)]|<=C_N||b||². Por §3, ||f_(k,P)||²>=c_N k^(1/2−N)||b||² para k grande. Se obtiene la cota uniforme

    |Polar[f_(k,P)]|/||f_(k,P)||²
       <=C_N k^(N−1/2)(4u²−1)^-k ->0.

Se ha usado u>1, por lo que 4u²−1>1. No se extrapola esa conclusión a tasas pequeñas.

## 7. Constante explícita para P fijo

Sea D=degP, r=N−D y a_D su coeficiente principal. Los términos inferiores desaparecen tras la escala apropiada. La densidad límite normalizada es proporcional a |x|^-2r exp(−u²/x²). Integrar con t=u²/x² da

    ||f_(k,P)||² ~ |a_D|² k^(1/2−r)
                    u^(1−2r)Γ(r−1/2)/(2pi),
    E log|x|=log u−(1/2)psi(r−1/2).

Combinar esto con §§4–6 da ASYM. Para el mismo P, la razón de normas ponderadas tiene además límite

    ||e^(eta y)f_(k,P)||²/||f_(k,P)||²
       ->[u/(u−2eta)]^(r−1/2),

consistente con WT. Son identidades de escala de esta órbita racional, no hipótesis adicionales de regularidad.

## 8. Alcance para la transferencia geométrica

EVENTUAL controla toda la cola k>=K_N para cada dimensión inicial N FIJA, con todos los numeradores y todos los contactos. Esto es un resultado de signo, no solo una identidad de mezcla. Puede servir como condición terminal al estudiar las sumas geométricas de SIGNED/GEOMETRIC_TRANSFER015.

No prueba el signo de los primeros k, ni da K_N uniforme al crecer N, ni demuestra que positividad de la cola implique positividad de la mezcla original. Esa inferencia necesitaría controlar precisamente las contribuciones iniciales y sus pesos. La propiedad es compatible con una forma que tenga direcciones negativas fuera de estas colas; no se presenta como cierre del signo en todos los bloques.
