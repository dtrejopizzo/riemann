# POWER_BOUNDARY_WEDGE_029 — Región uniforme u>=64sqrt(N), incluido k=0

Estado: PROVED región infinita en N,k,u; revisión independiente APROBADA y verificador reproducido con PASS. Papers intactos.

## 1. Corpus, diferencia y teorema

Leídos las reglas del proyecto, INTERIOR017/WRN, JOINT_SCALE016 y sus obstrucciones de pesos, ROW_SPLIT028 y las filas previas; búsquedas dirigidas en índice/grid/crucigrama (pesos bilaterales/escala conjunta/u variable). No se reintenta uniformizar una sola norma temporal a u fijo, que016 refutó.

La diferencia nueva es conservar JUNTOS los pesos opuestos +eta y−eta: sus factores de desplazamiento temporal se cancelan. Se obtiene una constante de correlación controlada por N/u², no por N/u. Esto se combina con un lower global elemental de ARCH que cubre también k0, sin un certificado individual por dimensión.

**Teorema.** Para TODOS enteros N>=1,k>=0 y TODAS tasas reales u>=64sqrt(N), sea f de transformada F(s)=s^k/(s+u)^(N+k). Entonces

    W[f]>(2/5)||f||².                                   (WEDGE)

No se afirma el mismo signo en todo N a una tasa FIJA ni suficiencia de este wedge para el puente a todos los tests.

## 2. Una mejora de WRN por coeficientes, válida en ambas direcciones

El coeficiente de S_N(r) de INTERIOR017 es B_l=(N−1/2)_l/(1/2)_l. Si C_l=(2N−1)_l/l!, entonces B0=C0=1 y para l>=1,

    (l−1/2)(2N+l−2)−l(N+l−3/2)=(N−1)(l−1)>=0.

Por comparación de cocientes, B_l<=C_l y

    S_N(r)<=sum C_lr^l=(1−r)^(-(2N−1)), 0<=r<1.

La expansión beta que prueba WRN utiliza eta² y solamente requiere a=u−eta>0 y eta²/a²<1. Por eso la MISMA prueba vale tanto para eta como para−eta cuando0<eta<u/2, y da

    ||e^(eta y)f||²/||f||²
       <=[(u−eta)/(u−2eta)]^(2N−1),
    ||e^(-eta y)f||²/||f||²
       <=[(u+eta)/(u+2eta)]^(2N−1).

No se fuerza ninguna de esas dos constantes por separado a ser uniforme. Cauchy–Schwarz desplazado conserva su PRODUCTO y da

    |c_f(t)|/||f||²<=e^(-eta|t|)
       ·[(u²−eta²)/(u²−4eta²)]^(N−1/2).                (BILAT)

En efecto, para t>=0 se insertan e^(eta(y+t)) y e^(-eta y) en ∫f(y+t)f(y)dy; queda el factor e^-eta t. La simetría cubre t<0. Éste es el paso que evita la obstrucción de media temporal016.

## 3. Peine completo uniformemente pequeño en el wedge

Elija eta15. Como u²>=4096N, se tiene u>30. Por log(1+x)<=x,

    log([(u²−225)/(u²−900)]^(N−1/2))
       <=675(N−1/2)/(4096N−900)<=675/4096.

La última comparación equivale a2048>=900. Además exp(675/4096)<=4096/3421<6/5. De BILAT se obtiene

    |c_f(t)|/||f||²<(6/5)e^(-15|t|).

Usando Lambda(q)<=q y comparación suma-integral,

    |Comb[f]|/||f||²
      <(12/5)sum_(q>=2)q^-14
      <=(12/5)2^-14(1+2/13)<1/5000.                    (PRIME)

El peine infinito está incluido íntegramente, sin signo supuesto de contactos.

## 4. Lower global de ARCH sin problemas en frecuencia cero

La desigualdad auditada en QUADRATIC017, ApéndiceA, es Re psi(a+it)>=log|a+it|−1/a. Usar la recurrencia una vez desde1/4 hasta5/4 da, para tau!=0,

    m(tau)>=log|tau|−log(2pi)−4/5−1/(tau²+1/4).        (SYMBOL)

El recíproco procede exactamente de Re[1/(1/4+i tau/2)]=1/(tau²+1/4). No se pierde una potencia de2.

La energía arquimediana A_(N,k)(u) crece en k por la covarianza con Z=tau²/(u²+tau²), de modo que basta k0. Su probabilidad espectral tiene densidad máxima

    p_max=1/[uB(1/2,N−1/2)]<=sqrt(N)/(u sqrt(pi)).

La desigualdad beta se demuestra por Jensen para sqrt(X) con X~Gamma(N−1/2,1): Gamma(N)/Gamma(N−1/2)<=sqrt(N−1/2)<sqrtN. Por tanto

    E[1/(tau²+1/4)]<=2pi p_max<4sqrtN/u.                (RECIP)

Por la fórmula beta,

    Elog|tau|=logu+(1/2)psi(1/2)−(1/2)psi(N−1/2)
       >log(u/sqrtN)−1.

Aquí psi(1/2)=−gamma−2log2>−2 usando gamma<3/5,log2<7/10, y psi(x)<=logx. Así SYMBOL/RECIP dan, en el wedge,

    A_(N,k)(u)>log(32/pi)−1−4/5−1/16>9/20.             (ARCH)

La última comparación es elemental: pi<22/7 y

    log(112/11)=3log2+log(14/11)
       >3(693/1000)+6/25=2319/1000.

Se usó el primer término atanh para log(14/11); las cotas de log2 y gamma ya están auditadas y el verificador adjunto las comprueba racionalmente. ARCH cubre TODOS N>=1, no una lista de extremos de N.

## 5. Polar: signo par y pequeño presupuesto impar

Sea a=u²−1/4. Las fórmulas beta dan signo polar (−1)^k y magnitud p_(N,k) de ROW_SPLIT028. La cota beta de§4 y sqrt(pi)<2 implican

    p_(N,0)<=4sqrt(pi)sqrtN/u·(1−1/(4u²))^-N
       <(1/8)·16384/16383<1/4.

Se aplicó Bernoulli (1−z)^N>=1−Nz y N/(4u²)<=1/16384. Además a>=4095N, por lo que

    p_(N,1)=p_(N,0)N/(2a)<1/(4·8190)<1/1000.

Para k>=1, los cocientes sucesivos de magnitudes son

    (k+N)/[(k+1/2)(4u²−1)]
      <=(N+1)/[(3/2)(16384N−1)]<1.

Así todos los polares impares son >−1/1000. En k0 y en todos los k pares el polar es no negativo y se conserva. Combinando con ARCH y PRIME,

    W[f]/||f||²>9/20−1/5000−1/1000>2/5.

Queda probado WEDGE. El límite k0 no necesita un bound singular E tau^-2: RECIP lo reemplazó por una densidad máxima integrable.

## 6. Verificación y alcance

El archivo `tools/power_boundary_wedge_029_verify.py` comprueba las constantes racionales y las cotas elementales de gamma/log sin recorrer N o k. Las desigualdades para todos los parámetros se demuestran en el texto.

Esta es una región REAL de signo completa y uniforme en tres parámetros, e incluye el borde k0. Complementa la región más fuerte de ROW_PATTERN029 para k>=1. No se afirma que uvariable baste para el puente de tasa fija u31.5: para cada N el lower de u crece. POWER_SCALE_BRIDGE_LIMIT_029 demuestra además que las mezclas positivas de las densidades de esta región NO aproximan ciertos átomos concentrados de tasa fija en L¹. No se excluyen otros mecanismos con información adicional. No hay nueva ventana T ni edición de papers.
