# POWER_PARTICULAR_ORIGIN_DESIGN_093 — Diseño previo y decisión de un único signo particular

**Auditoría independiente:** diseño, literal y fuente final aprobados en `POWER_PARTICULAR_ORIGIN_AUDIT_093.md`; constructor37905 exit0/PASS, reproducción independiente root94506 exit0/FULL PASS128 y hash coincidente.

Estado: **PROVED PUNTUAL por constructor exit0/PASS; auditoría matemática del diseño y literal aprobada antes de la corrida, lectura final pendiente.** Todos los parámetros siguientes fueron fijados antes de ejecutar. Se conservan el diseño previo y sus condiciones; el resultado está en§6. Papers intactos.

## 1. Objeto específico y antecedentes

Consultados las reglas del proyecto, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D, y073/077/078/087/089/090/092.092 descarta una eliminación universal globalmente invertible; no decide el signo para K particular. Aquí se comprueba una condición necesaria de ese signo en UN punto, utilizando la selección global de K por sus dos bordes. No otro pivote, parámetro o malla de signos.

Con w=tPhi,v=−Phi', a=M'(0),c=1/a, K''=v−cw,K(0)=K(infinito)=0, escribir Phi/Phi0=sum a_j t^(2j). Entonces

    W(w,v,w'',K)=64 Phi0^4 t^10[Dpart+O(t²)],
    Dpart=P kappa+Qc+R,
    kappa=K'(0)/Phi0=c tau0−1,
    tau0=I1/Phi0, a=I2/I0, Ir=integral_0^infinito t^r Phi(t)dt.

Las columnas de la matriz que determina Dpart tienen las filas

    [1,−2a1,6a1,kappa],
    [a1,−4a2,20a2,−(2a1+c)/6],
    [2a2,−12a3,84a3,−(4a2+ca1)/10],
    [6a3,−48a4,432a4,−(6a3+ca2)/7].

Se reutilizan los intervalos racionales de a1,...,a4 y Phi0 de087, sin modificar su script. Los coeficientes exactos son

    P=192(6a1a3a4−8a2²a4+3a2a3²),
    Q=(16/35)(126a1³a4−51a1²a2a3+10a1a2³
          −588a1a2a4+210a1a3²+30a2²a3+420a3a4),
    R=−(192/35)(28a1²a2a4−20a1²a3²+2a1a2²a3
          −70a1a3a4+56a2²a4−15a2a3²).

Se decidirá el signo de

    NUM=Q Phi0 I0+P I1 I0+(R−P)Phi0 I2
       =Phi0 I0 a Dpart.

El factor es positivo. El assert final aceptará NUM>0 **o** NUM<0; no se predetermina el signo. Si no separa0, el resultado será inconcluso con estos parámetros, sin ajustes exploratorios.

## 2. Parámetros fijados y bound complejo uniforme

Integrar sólo [0,2] con128paneles de longitud1/64, semiancho h=1/128, centros dyádicos(2j+1)/128,j=0,...,127. Precisión512bits, Taylor grado64, cap65,16modos theta. Radio complejo de Cauchy r=1/32, razón h/r=1/4.

En los discos alrededor de esos centros, usar el recinto mayor

    −1/32<=Re t<=65/32, |Im t|<=1/32, |t|<3.

Con y=pi exp(2t), e<3,pi<4, exp(−1/16)>15/16 y cos(1/16)>511/512:

    Re y>3(15/16)(511/512)>5/2,
    |y|<4 exp(65/16)<4*256=1024,
    |exp(5t/2)|<exp(325/64)<exp(6)<3^6<1024.

Para cada modo theta

    Phi_m=pi exp(5t/2)m²(2m²y−3)exp(−m²y),

queda |Phi_m|<2^24 m^4 8^(−m²), pues exp(5/2)>8 (exp2>7,exp(1/2)>3/2). La suma de m^4 8^(−m²) es menor que1/4: primer término1/8 y todas las razones son menores que1/2. Así |Phi|<2^22 y para r=0,1,2,

    |t^r Phi(t)|<9*2^22<10^8.

La cola COMPLETA de modos m>=17 tiene bound

    EPS=2^25*17^4/8^289,

por razón consecutiva <=(18/17)^4/8^35<1/2. En cada centro se añaden errores outward EPS*32^k a TODOS los coeficientes Phi[k],k=0,...,64, ANTES de multiplicar por t^r.

## 3. Cuadratura Taylor y su error exacto

Se evalúan jets sólo en centros exactos, sin bolas de parámetro. Para cada t^rPhi se integra exactamente el polinomio Taylor grado64 en el panel simétrico: los términos impares se anulan y el término k par aporta2coef[k]h^(k+1)/(k+1). La aritmética arb mantiene todo redondeo outward.

El error puntual de la serie completa en un panel está acotado por10^8(1/4)^65/(1−1/4). Integrando y sumando los paneles, cuya longitud total es2,

    REM=2*10^8*4^(−65)/(1−1/4)<10^(−28).

Este resto se añade simétricamente al momento truncado. Es independiente de los valores observados y de los errores de la cola theta ya incluidos en los coeficientes.

## 4. Cola temporal completa t>2

Para t>=2, pi>3,pi<4 y una suma geométrica de todos los modos dan

    Phi(t)<64 exp(9t/2−3exp(2t)).

En efecto se domina el factor2m²y−3 por8m²exp(2t), y sum m^4 exp(−3m²exp(2t))<2exp(−3exp(2t)). El assert racional Taylor de exp4>54 fija

    Phi(2)<64*3^9*2^(−162)<2^(−140).

La derivada logarítmica del mayorante es9/2−6exp(2t)<−300. Por ello, con s=t−2,

    Phi(2+s)<2^(−140)exp(−300s),
    (2+s)^r<=4exp(2s), r=0,1,2,
    0<integral_2^infinito t^rPhi(t)dt<2^(−140).

Se añade el intervalo positivo[0,2^(−140)] a cada momento; no se aplica el bound042, que requería un rango de N diferente.

## 5. Condiciones de implementación y alcance

ctx.prec=512,ctx.cap=65 explícitos. Exigir Phi.prec>=65 y coeficientes0..64 finitos en todos los centros. Añadir las colas antes de multiplicar t o t². Convertir los intervalos racionales087 a arb usando ambos extremos y redondeo exterior, sin tomar decimales. Verificar I0,I1,I2 y Phi0 estrictamente positivos antes de cualquier cociente opcional. NUM es el test principal y conserva sus factores positivos sin divisiones innecesarias.

El resultado sólo decide el jet de la solución particular real en el origen. Si NUM>0, refuta esa condición suficiente cerca0, no la forma W. Si NUM<0, sólo la verifica cerca0 sin radio certificado; no prueba el signo global de QF ni un nuevo orden de generadores.


## 6. Resultado constructor, reproducción y alcance final

Tras aprobación independiente del diseño y del literal por mapa y root, la ÚNICA corrida constructora37905 terminó exit0/PASS128paneles con los parámetros anteriores, sin modificación durante la corrida. El assert que aceptaba cualquiera de los dos signos obtuvo

    PASS093: particular-origin determinant sign NEGATIVE.

Salida intervalar outward de Arb:

    I0 [0.124280194547078527478193434921 +/- 5.46e-31]
    I1 [0.021528707625566523248989621992 +/- 6.74e-31]
    I2 [0.005742986078786359383812469124 +/- 6.04e-31]
    a [0.04620998623083794157786762086 +/- 2.33e-30]
    tau0 [0.048195336934403062728348027284 +/- 4.42e-31]
    NUM [-55.56138101164184468956750 +/- 9.92e-24]
    Dpart [-21658.19847758362431307814 +/- 2.30e-21].

El signo probado proviene de la comparación estricta intervalar del script, no de sustituir los centros de estos intervalos. Los momentos incluyen tanto los errores de cuadratura como TODAS las colas theta y la cola temporal. El pequeño radio de NUM/Dpart incluye la propagación de los jets racionales087 y las dependencias perdidas conservadoramente; no se excluyen errores comunes por cancelación informal.

Por Dpart<0 y analiticidad,

    W_t(w,v,w'',K)<0 para todo t>0 suficientemente pequeño.

Este resultado **verifica**, y no refuta, la condición local particular requerida en esa vecindad. No proporciona un radio de vecindad, un signo en todo t>0, una invariancia de cono, ni una reparación de la carta Delta de092. Para F=K/w, el signo equivalente de ((F'/B')'/J)' queda verificado localmente por los factores positivos del Wronskiano; no se ha probado globalmente. No cambia la cobertura de W ni el número de generadores; el objetivo global sigue OPEN.

Comando reproducible desde la raíz del repositorio:

    python3 03-research/phase-211-sign-sandbox/tools/power_particular_origin_093_verify.py

SHA256 del script sin cambios durante la corrida:

    57c0656deb1767e00a4de674a0f5f6556886eca06edbc93ae1ef8488b032c67e.

El script087 importado permanece intacto, hash f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7. La reproducción independiente y lectura final se registrarán en la auditoría093.
