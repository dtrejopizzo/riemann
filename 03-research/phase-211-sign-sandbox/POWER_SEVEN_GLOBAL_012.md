# POWER_SEVEN_GLOBAL_012 — Signo uniforme para todos los espacios de siete polos >=63/2

Estado: PROVED, certificado racional exacto ejecutado y revisado independientemente en POWER_SEVEN_AUDIT_012.md. Papers intactos.

## 1. Teorema y nueva razón respecto de los casos previos

Sean v_1,...,v_7>=u=63/2, permitiendo multiplicidades, y f real no nula de transformada de Laplace P(s)/Π_j(s+v_j), gradoP<7. Entonces

    W[f]>(1/500)||f||².                                  (SEVEN)

Esto incluye mezclas arbitrarias de hasta siete potencias exteriores con exponentes >=32 y todos sus correspondientes límites confluentes. No requiere separación ni cota superior de las tasas.

Se consultan las reglas del proyecto, índice/grid/crucigrama según POWER_BRIDGE_002, los cierres globales de cuatro/cinco/seis polos y POWER_COMMON_TRANSFER_010. No se presenta como nueva la familia semilocal ni el transporte de filtros. La razón nueva es utilizar conjuntamente DOS estimaciones más precisas que las del cierre previo: el déficit del filtro se acota directamente como producto, evitando separar sus máximos, y la norma ponderada se controla por la traza confluente exacta auditada en COMMON_TRANSFER§6. Ambas conservan la holgura necesaria en dimensión siete. El certificado confluente de siete se verifica de nuevo; no se infiere del de seis.

## 2. Certificado confluente exacto

En la base ortonormal phi_j=sqrt(63)e^-uy L_j(63y), j0..6, AP=Arch+Polar es Toeplitz. Sus bandas son

    AP_0=psi16−log pi+4u/(u²−1/4),
    AP_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!
          +[2u/(u²−1/4)](−1)^k[(32/31)^k+(31/32)^k].

El verificador `tools/power_seven_global_012_verify.py` encierra las poligamma mediante las sumas m16..2000 más colas integrales entre 1/[r·2001^r] y 1/[r·2000^r]. Usa el módulo de intervalos racionales con redondeo exterior `power_fixed_grid_003.py` para gamma, pi y log. Todo cálculo se efectúa con Fraction; ninguna función especial flotante interviene.

Los siete pivotes de LDL INTERVALAR de AP−(69/1000)I tienen extremo inferior estrictamente positivo. Así, para todo f0 con transformada P(s)/(s+u)^7,

    AP[f0]>(69/1000)||f0||².                              (BASE7)

Los vectores de momentos tienen normas al cuadrado

    AA=(63/31²)Σ(j=0..6)(32/31)^(2j),
    BB=(63/32²)Σ(j=0..6)(31/32)^(2j).

La comparación racional 4AA BB<1 prueba además |Polar[f0]|<||f0||². Solo se usa esta cota para la variación polar bajo filtro, conservando el signo favorable dentro de BASE7.

## 3. Déficit espectral directo del filtro

La serie positiva de digamma y m(0)>−5373/1000 dan, para x=tau²,

    m(tau)>ell(x):=−5373/1000
             +Σ(k=0..15)x/[a_k(4a_k²+x)], a_k=k+1/4.

La constante m(0) se verifica con los intervalos racionales del mismo módulo. La función ell es creciente y ell(49)>1/20. Fije c=1/100. Para j0..195 y x∈[j/4,(j+1)/4],

    (c−m(sqrt(x)))_+ [(1+x/u²)^7−1]
      ≤(c−ell(j/4))_+ [(1+(j+1)/(4u²))^7−1]
      <57/1000.                                         (DIRECT)

Las 196 últimas comparaciones son racionales exactas, verificadas individualmente. Esto es una partición finita certificada de un intervalo de frecuencia, no un barrido numérico ni una extrapolación entre puntos: cada intervalo queda cubierto por las dos monotonías. Para x>=49, m>c y el déficit es cero.

El paso DIRECT es más preciso que estimar por separado x(c−m)_+ y el cociente del filtro: conserva dónde sus dos factores son simultáneamente grandes.

## 4. Transporte global a tasas arbitrarias

Con el mismo numerador, escriba F0=P/(s+u)^7 y F=HF0, H=Π(s+u)/(s+v_j). Ponga R=|H(i tau)|², R0=Πu²/v_j², r0=H(−1/2)H(1/2). Como v_j>=u,

    1≤R/R0≤(1+x/u²)^7,
    1−7/(4u²)≤r0/R0≤1.

La identidad exacta de COMMON_TRANSFER conserva la norma objetivo nueva:

    AP[f]−c||f||²=R0(AP[f0]−c||f0||²)
       +(1/2pi)∫(R−R0)(m−c)|F0(i tau)|²d tau
       +(r0−R0)Polar[f0].

DIRECT controla la pérdida integral por (57/1000)R0||f0||². La variación polar se pierde a lo sumo 7R0||f0||²/(4u²). BASE7 da

    AP[f]−c||f||²
      >R0[69/1000−1/100−57/1000−7/(4u²)]||f0||²>0.

El corchete es racional estrictamente positivo. Por tanto

    AP[f]>(1/100)||f||²                                 (AP7)

uniformemente para los siete polos arbitrarios. No se afirma monotonía de AP ni se compara indebidamente el polar por su signo.

## 5. Peine completo por la traza ponderada exacta

Use sigma=2u/3=21. El lema auditado de COMMON_TRANSFER§6 prueba que la traza de la Gram ponderada de la base racional es máxima en la confluencia. En consecuencia

    ||e^(sigma y)f||²≤T7||f||²,
    T7=Σ(j=0..6)Σ(k=0..j)binom(j,k)²(2/3)^(2k)/(1/3)^(2j+1)
      =176673441.

Se usa operatornorm≤trace; no se necesita ni se afirma monotonía del eigenvalor máximo ponderado. El valor T7 es racional exacto y 2sqrt(T7)<26600.

Por Cauchy–Schwarz desplazado, |c_f(log q)|≤sqrt(T7)q^-21||f||². Luego, con Lambda(q)≤logq y sqrt(q)>=sqrt2>7/5,

    |Comb[f]|/||f||²
      ≤26600 Σ(q>=2)(log q)q^-21.5
      <26600(5/7)Σ(q>=2)(log q)q^-21.

La función (log x)x^-21 decrece para x>=2. Comparación suma-integral y log2<7/10 dan

    Σ(q>=2)(log q)q^-21
      ≤2^-21[7/10+14/200+2/400]
       =31/(40·2^21).

El producto racional 26600(5/7)31/(40·2^21)<1/125. Combinando con AP7,

    W[f]>(1/100−1/125)||f||²=(1/500)||f||².

Se han incluido TODOS los contactos, no un truncamiento del peine.

## 6. Verificación y alcance

El verificador ejecutado da PASS para los pivotes intervalares, norma polar, 196 paneles, margen de transporte, traza exacta y coste del peine. Reutiliza únicamente el módulo racional explícito de constantes, que también acompaña los certificados anteriores.

Siete polos siguen siendo una clase finita. No se afirma signo en todos los órdenes ni cierre del Paper47. El test Tate de gran orden y el bloque aritmético de dimensión doce mantienen su problema diferente: no quedan resueltos por extrapolar AP7.
