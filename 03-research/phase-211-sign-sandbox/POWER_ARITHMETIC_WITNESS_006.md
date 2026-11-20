# POWER_ARITHMETIC_WITNESS_006 — Un test exterior que necesita el peine y es reparado por 2

Estado: PROVED mediante aritmética racional exacta; §§1–3 revisados independientemente en POWER_AUDIT_006. §4 añadido posteriormente, revisado independientemente. Ningún paper modificado.

Antecedentes: POWER_CONFLUENT_FOUR_005 demuestra que la polar puede rescatar ARCH. Aquí se cruza una frontera distinta: ARCH+POLAR es negativa y el peine aritmético es necesario para el signo de este test. Este objeto cambia respecto de las regiones exteriores previamente positivas; no es una afirmación sobre grafos genéricos ni sobre theta positiva. Índice/grid/crucigrama y las reglas del proyecto consultados en POWER_BRIDGE_002.

## 1. Test y resultado concreto

Sea u=63/2, phi_j(y)=sqrt(63)e^-uy L_j(63y)1_(y>0), 0≤j≤11, y h=Σv_j phi_j, donde

    v=(2521,−3701,3730,−3278,2158,−793,
       −793,2158,−3278,3730,−3701,2521),
    ||h||²=N=99993678.

El certificado adjunto prueba las tres afirmaciones

    −2/125 < (Arch[h]+Polar[h])/N < −1/100,                (A)
    cada contacto primo-potencia aporta estrictamente positivo,
    término de n=2 dividido por N >1/25.                  (B)

Por tanto la forma completa satisface W[h]>(1/25−2/125)N>(1/50)N. El peine no es una pequeña perturbación irrelevante: sin él, este test tiene signo negativo. El contacto 2 por sí solo basta para reparar el déficit, y todos los contactos adicionales ayudan sobre este test concreto.

## 2. Autocorrelación y signo de cada contacto

La integral de dos funciones Laguerre desplazadas da

    c_h(t)=e^-ut Q(2ut), t>=0,
    Q(x)=Σ(i<=j)v_i v_j [L_(j-i)(x)−L_(j-i-1)(x)], L_-1=0.

Se verifica integrando polinomios contra e^-63y, o usando la base racional ortonormal y residuos; los términos i>j se anulan. Los coeficientes de Q en orden ascendente son

    [99993678,49185301,13821792,−7615697/2,59520419/12,
     −128178871/60,39362105/72,−4637517/56,7669309/1008,
     −3136561/7560,133613/10800,−6355441/39916800].

La expansión exacta de Q(x+40) tiene TODOS sus coeficientes estrictamente negativos. Luego Q(x)<0 y Q'(x)<0 para x>=40. Como log2>2/3, para todo entero n>=2 se tiene 63log n>42>40. Por ello

    −v_n c_h(log n)=−2Lambda(n)n^-32 Q(63log n)>=0,

estrictamente si Lambda(n)>0. Se entiende «cada término» como cada contacto primo-potencia no nulo. No hace falta estimar una cola para obtener la cota inferior de W.

Para n=2, las monotonías de −Q y log dan la cota racional suficiente

    −2log2·2^-32 Q(63log2)/N
      >−(4/3)2^-32 Q(42)/N >1/25.

La segunda comparación está verificada exactamente. No se usan valores de log2 redondeados.

## 3. Certificado racional de ARCH+POLAR negativa

La matriz arquimediana de orden doce en esta base es Toeplitz. Su diagonal es d=psi16−log pi, y sus bandas, para k>=1, son

    b_k=(1/2)Σ(r=1..k)binom(k−1,r−1)u^r psi^(r)(16)/r!.

Ponga C_k=Σ(i=0..11−k)v_i v_(i+k). Usando psi^(r)(16)=(-1)^(r+1)r!Σ(m>=16)m^(-r-1), se obtiene directamente

    Arch[h]=N d+Σ(r=1..11) T_r Σ(m>=16)m^(-r-1),
    T_r=(-1)^(r+1)u^r Σ(k=r..11)C_k binom(k−1,r−1).

Los T_r son racionales. Se aplican las cotas de d de POWER_CONFLUENT_FOUR_005 y, para cada r, las sumas m16..255 más colas integrales entre 1/[r·256^r] y 1/[r·255^r]. No se restan números flotantes grandes: se mantiene toda la combinación exacta como Fraction.

Los momentos son los mismos de dimensión cuatro:

    Polar[h]=126 [Σv_j(−32)^j/31^(j+1)]
                   [Σv_j(−31)^j/32^(j+1)].

El verificador `tools/power_arithmetic_witness_006_verify.py` prueba (A), el signo de todos los coeficientes trasladados y (B). Los intervalos racionales obtenidos en (A) son aproximadamente (-.01534,-.01054), pero estos decimales no participan en la prueba.

## 4. Retirar solamente el contacto 2 sí cambia el signo

Se puede acotar superiormente TODO el resto sin calcular individualmente otros primos. Escriba Q(x)=Σq_k x^k y r=k+1. Como Lambda(n)≤log n,

    Σ(n>=3) |−2Lambda(n)n^-32 Q(63log n)|/N
      ≤ (2/N)Σ(k=0..11)|q_k|63^k S_(k+1),

donde S_r=Σ(n>=3)(log n)^r n^-32. Para r≤12, la función (log x)^r x^-32 decrece en x≥3. Usando 1<log3<11/10, la comparación por integral y una expansión binomial exacta dan

    S_r ≤3^-32(11/10)^r
          +3^-31 Σ(j=0..r)binom(r,j)(11/10)^(r-j)j!/31^(j+1).

El verificador prueba racionalmente que la suma mayorante completa es <1/500. Las cotas 1<log3<11/10 se obtienen del mismo J/E con argumento 1/2; no se presupone evaluación decimal. Puesto que AP/N<−1/100,

    W_sin_contacto_2[h]/N <−1/100+1/500=−1/125.

Por consiguiente este test distingue realmente el peso del contacto 2: con todos los contactos tiene margen positivo >1/50; retirando solo 2 y conservando TODOS los demás tiene margen negativo <−1/125. No se retiran sus potencias 4,8,...: esas contribuciones forman parte de la cola acotada.

## 5. Alcance

Este test exhibe compensación aritmética concreta fuera de la región ARCH+POLAR positiva. No es un contraejemplo al signo completo ni un certificado sobre todos los vectores de orden doce. El cambio de signo por retirar 2 está demostrado para este test exterior explícito; no se atribuyen consecuencias más amplias sin una construcción adicional.
