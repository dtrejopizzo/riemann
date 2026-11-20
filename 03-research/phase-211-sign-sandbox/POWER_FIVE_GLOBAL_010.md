# POWER_FIVE_GLOBAL_010 — Signo uniforme para todos los espacios de cinco polos >=63/2

Estado: PROVED, certificado racional exacto ejecutado y revisado independientemente en POWER_FIVE_AUDIT_010.md. Papers intactos.

## 1. Teorema y diferencia respecto de antecedentes

Sean v_1,...,v_5>=u=63/2, con multiplicidades permitidas, y f real no nula de transformada de Laplace P(s)/Π_j(s+v_j), grado P<5. Entonces

    W[f]>(1/100)||f||².                                  (FIVE)

En particular se incluyen mezclas arbitrarias de hasta cinco potencias exteriores X^-a con exponentes a>=32 y todos sus límites confluentes correspondientes. No se exige separación ni cota superior de tasas.

Antecedentes leídos: las reglas del proyecto, índice/grid/crucigrama registrados en POWER_BRIDGE_002; POWER_FOUR_GLOBAL_009 y su auditoría; los certificados confluentes y los falsificadores de monotonía polar. La herramienta de transporte global ya fue inventada y probada en FOUR009: NO se atribuye novedad al principio. La diferencia sustantiva es un NUEVO certificado confluente de dimensión cinco y un cambio de peso en el control all-pass del peine que permite cerrar uniformemente cinco polos. No se extrapola desde puntos ni desde el caso de cuatro.

## 2. Nuevo certificado confluente de dimensión cinco

En la base ortonormal phi_j=sqrt(63)e^-uy L_j(63y), j0..4, la matriz arquimediana es Toeplitz. La diagonal d y las bandas b_k se encierran exactamente mediante

    d=psi16−log pi,
    b_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!.

Las sumas de poligamma son Σ(m>=16)m^(-r-1), con signo (-1)^(r+1), y se acotan sumando m16..255 más colas integrales entre 1/[r·256^r] y 1/[r·255^r]. Para d se usan las mismas cotas racionales de gamma, pi y log que en CONFLUENT_FOUR005. No se necesitan restos de alta precisión.

El centro racional de las cinco bandas arquimedianas es

    (1596/1000,1016/1000,−16/1000,349/1000,−154/10000).

Su error de máxima suma absoluta de fila es <1/200. La polar exacta tiene entradas

    Polar_jk=63(A_j B_k+B_j A_k),
    A_j=(−32)^j/31^(j+1), B_j=(−31)^j/32^(j+1).

El LDL racional de la matriz central más Polar menos (39/200)I tiene cinco pivotes estrictamente positivos, verificados por `tools/power_five_global_010_verify.py`. Por tanto

    AP[f0]:=Arch[f0]+Polar[f0]>(19/100)||f0||²             (BASE5)

para todo numerador confluente de grado<5. Además, con AA=63ΣA_j² y BB=63ΣB_j², el mismo script certifica 4AA BB<1. Por Cauchy–Schwarz,

    |Polar[f0]|<||f0||².                                  (PB5)

No se usa como sustituto de BASE5: PB5 solo controla la pequeña variación del polar bajo el filtro.

## 3. Transporte a cinco tasas arbitrarias

Use el mismo numerador y defina F0(s)=P(s)/(s+u)^5 y F(s)=H(s)F0(s), H(s)=Π_j(s+u)/(s+v_j). Para x=tau², ponga

    R(tau)=|H(i tau)|², R0=Π_j u²/v_j²,
    r0=H(−1/2)H(1/2)=Π_j(u²−1/4)/(v_j²−1/4).

Como v_j>=u,

    1≤R/R0≤(1+x/u²)^5,
    1−5/(4u²)≤r0/R0≤1.

La segunda desigualdad inferior es Bernoulli aplicada a cinco factores. FOUR009 prueba mediante series racionales del símbolo

    m(tau)≥1/10 para tau²≥81,
    tau²(1/10−m(tau))_+<23.

Estas cotas también valen reemplazando 1/10 por c=1/50. Fije K5=[(1+81/u²)^5−1]/81; por convexidad de la expansión polinomial, (R−R0)/R0≤K5 x cuando 0≤x≤81.

La identidad exacta de transporte es

    AP[f]−c||f||²
      =R0(AP[f0]−c||f0||²)
       +(1/2pi)∫(R−R0)(m−c)|F0(i tau)|²d tau
       +(r0−R0)Polar[f0].

Fuera de x≤81 la integral adicional es no negativa. Dentro es >−23K5 R0||f0||². Por PB5, la variación polar es >−5R0||f0||²/(4u²). BASE5 da

    AP[f]−c||f||²
      >R0[19/100−c−23K5−5/(4u²)]||f0||².

El corchete es racional y estrictamente mayor que 3/100, como verifica el script. Por tanto

    AP[f]>(1/50)||f||²                                   (AP5)

uniformemente en todas las tasas. No se afirma monotonía del cociente AP: se transporta solo una cota menor conservando un resto positivo. El término objetivo contiene la norma de f, de modo que R0 pequeño no destruye la uniformidad.

## 4. Nuevo peso all-pass que controla todo el peine

Use sigma=2u/3=21. En una base ortonormal de Malmquist de cinco polos v_j>=u, la primera exponencial normalizada tiene norma al cuadrado ponderada por e^(2sigma y) acotada por v_j/(v_j−sigma)≤3. Cada factor all-pass es la convolución delta−2v_j e^(-v_j y), y su norma L¹ ponderada por e^(sigma y) es ≤1+2v_j/(v_j−sigma)≤7.

Por Young ponderado, el modo j tiene norma al cuadrado ≤3·49^j. Cauchy–Schwarz en los cinco coeficientes de la base da

    ||e^(sigma y)f||²≤B5||f||²,
    B5=3Σ(j=0..4)49^j=(49^5−1)/16.

No se requiere separación de polos ni se pierde el resultado en multiplicidades. Cauchy–Schwarz desplazado da |c_f(t)|≤sqrt(B5)e^(-sigma t)||f||². Así, usando Lambda(q)≤q, sigma+1/2−1=20.5>20 y 2sqrt(B5)<8404,

    |Comb[f]|/||f||²
      ≤8404Σ(q>=2)q^-20
      ≤8404·2^-20(1+2/19)<1/100.

La suma incluye TODOS los contactos y converge absolutamente. Combinando con AP5 se obtiene FIVE.

## 5. Verificación y límites

El script adjunto comprueba BASE5, PB5, las cinco comparaciones escalares del símbolo usadas por FOUR009, el corchete de transporte, B5 y el margen final exclusivamente con Fraction. Resultado ejecutado: PASS.

Cinco polos no son todos los órdenes. El caso de dimensión doce necesita contribución aritmética con signo y no queda cubierto por este transporte de AP. La prueba presente tampoco da una constante uniforme al crecer la dimensión. El siguiente grado exige su propia estimación, no una extrapolación de este teorema.
