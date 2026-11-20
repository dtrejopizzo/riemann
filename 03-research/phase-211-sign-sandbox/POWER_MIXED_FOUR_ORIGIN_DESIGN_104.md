# POWER_MIXED_FOUR_ORIGIN_DESIGN_104 — Gate puntual positivo y cola del sistema mixto real

Estado: **PROVED el gate puntual positivo y la cola analítica; lectura final independiente pendiente.** Root y mapa aprobaron diseño y literal ANTES de la corrida. Se conserva el diseño previo; el resultado está en§7. Root autorizó reusar el programa087 INTACTO mediante runpy para recuperar sus intervalos no persistidos. No nuevos modos, precisión, punto o cola theta. Papers intactos.

## 1. Objeto exacto y deduplicación

Consultados las reglas del proyecto, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D, y077/078/087/089/090/093/095/099/102/103. Mantener las densidades PARES

    J(t)=integral_t^infinito sPhi(s)ds,
    K(t)=integral_t^infinito(s−t)[aPhi(s)−J(s)]ds,
    a=M'(0)=I2/I0, Ir=integral_0^infinito t^rPhi(t)dt.

Aquí K es la densidad PAR de078, no la primitiva impar093/095. El sistema mixto propuesto es

    [K,J,Phi,J''].

103§11.4 ya prueba los tres Wronskianos iniciales estrictamente positivos del orden[K,J,Phi,J'']. Por tanto un W4 mixto estrictamente positivo en toda la semirrecta completaría ECT4. Su Chebyshev4 global sería suficiente para el nuevo argumento de cruces localizado por la identidad exacta beta D_p+p²Psi_p=lambda K. No se presupone esa propiedad ni se afirma que sea necesaria para el signo de W o del numerador particular. Este test sólo puede descartar o dejar pasar un gate necesario de ESA propiedad más fuerte.

093 NO decide este origen: si f(lambda)=[K,J,Phi,J'']/Phi(0), lambda=t², entonces

    W_lambda(f')(0)=−a Dpart093/16>0,

pero el objeto de104 es W_lambda(f)(0). Son menores de filas de jets1,...,4 y0,...,3 respectivamente. La identidad se obtiene derivando las cuatro funciones pares: sus derivadas son[−aK_odd,−tPhi,Phi',−(tPhi)''], con las orientaciones de093. El signo de un menor desplazado en un punto no se transmite al anterior; se necesitaría una comparación global que no está probada.099 sólo controla la correspondiente versión transformada por Laplace, no invierte ese transporte para controlar densidades puntuales.

## 2. Matriz regularizada sin cancelaciones t=0

Escribir Phi(t)/Phi0=sum z_j lambda^j,z0=1, y poner

    tau=I1/Phi0,
    kappa=(aI1−I3/2)/Phi0=K(0)/Phi0.

De J'=-tPhi y K''=aPhi−J, las filas de derivadas lambda0,...,3 dan exactamente

    H=[[kappa,tau,1,−1],
       [(a−tau)/2,−1/2,z1,−3z1],
       [(az1+1/2)/6,−z1/2,2z2,−10z2],
       [(az2+z1/4)/5,−z2,6z3,−42z3]].

Los factores k! están incluidos. Con Dmix=detH,

    W_t(K,J,Phi,J'')
      =64Phi0^4 t^6[Dmix+O(t²)].                 (ORIGIN)

El factor t^6 es el cambio de variable de un Wronskiano de CUATRO funciones PARES: (2t)^6. No confundirlo con t^10, que aparece en cuatro funciones impares con un factor t común.

Sólo se precisan Phi0,z1,z2,z3 de087 y I0,I1,I2,I3 de103. Se aceptará cualquiera de ambos signos; un intervalo que no separe0 deja inconcluso este diseño fijo.

## 3. Datos ya certificados y recuperación autorizada

087 usa intervalos racionales outward de escala10^70, pi por Machin128, exponencial Taylor128 y11cuadrados,8modos y TODA la cola m>=9. Recuperar sus variables por runpy reproduce exactamente ESA misma obligación puntual; no se altera el script087. Su hash obligatorio es

    f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7.

Los datos103 se importan como intervalos racionales EXACTOS a partir de sus salidas Arb outward, sin volver a ejecutar su cuadratura:

    I0=0.12428019454707852747819343 +/- 6.89e−27,
    I1=0.02152870762556652324898962 +/- 3.96e−27,
    I2=0.00574298607878635938381247 +/- 2.84e−27,
    I3=0.00191588830192231322996545 +/- 4.90e−27.

Estos balls ya incluyen cola de modos, resto de cuadratura y cola temporal completas. Sus centros decimales se convierten mediante Fraction, y sus radios respectivos son689,396,284,490 divididos por10^29. Se usa la MISMA clase I de087 para formar todos los cocientes y productos, con redondeo exterior a10^70. No se aumenta precisión.

Comprobar Phi0>0,I0>0 y1/25<a<1 antes de los cocientes; la última caja ya está contenida en103 y paga la prueba exterior siguiente. Evaluar detH por sus24permutaciones. El assert acepta Dmix>0 O Dmix<0, sin imponer orientación de antemano. Se imprimirán los intervalos recuperados Phi0,z1,z2,z3 para no perder de nuevo estos datos.

## 4. Orientación exterior con resto holomorfo completo

Se justifica ANTES de datos que el Wronskiano mixto tiene orientación POSITIVA en una cola. Reutilizar COMPLEX de095: para Re z>=3,|Im z|<=1/16,y=pi exp(2z),Y=|y|,

    |p−2y|<6, |p'|<=5Y, Re p>=Y, p=−Phi'/Phi,
    |Phi(z+r)/Phi(z)|<=exp(−Yr), r>=0.

095 prueba estas cotas con TODA la cola theta y discos holomorfos sin ceros; no se borra la corrección de modos. Definir T1=integral_0^infinito rPhi(z+r)dr/Phi(z). Dos integraciones por partes exactas dan

    T1=1/p²−integral_0^infinito [Phi(z+r)/Phi(z)]
                   [2p'(z+r)/p(z+r)^3+r p'(z+r)/p(z+r)^2]dr,
    |T1−1/p²|<=15/Y³.

También J(z)/Phi(z)=z H0(z)/Phi(z)+T1, donde095 da |H0/Phi−1/p|<=5/Y². Por tanto

    |J/Phi−z/p|< (5|z|+2)/Y².

La definición de K es K/Phi=aT1−integral_0^infinito rJ(z+r)dr/Phi(z). Con a<1 y

    |J(z+r)/Phi(z+r)|< (|z|+r)/(Y exp(2r))
                          +1/[Y²exp(4r)],

se obtiene

    |K/Phi−a/p²|< (16+|z|)/Y³.

Todas las integrales horizontales son holomorfas y absolutamente convergentes en compactos del strip. No se diferencia un O real sin resto.

## 5. Modelo exterior y pago del determinante

Fijar t>=4 real,y0=pi exp(2t),P=2y0 y disco|z−t|<=1/32. Comparar las columnas normalizadas

    [K/Phi,J/Phi,1,J''/Phi]
    con [a/P²,t/P,1,tP].

Las primeras fórmulas y |p−2y|<6 implican bounds complejos de errores menores que

    50(1+t)y0^(−3),20(1+t)y0^(−2),0,7(1+t).

Aquí J''/Phi=zp−1 exactamente. Los factores(16/15)^2,(16/15)^3 son menores que2 en los cambios de Y a y0. Cauchy en el disco fijo controla derivadas0,...,3 con el bound común

    Hstar=200*3!*32³=39321600,
    errores de columnas <=Hstar(1+t)[y0^(−3),y0^(−2),0,1].

Las entradas modelo y sus derivadas hasta3 se acotan por

    [16/y0²,16t/y0,1,32t y0].

La identidad algebraica exacta es

    W_t[a/P²,t/P,1,tP]
       =128a(6t²+4t−1)/P²
       >=192a t²/y0²>7t²/y0², t>=4.

Multilinealidad y24términos por determinante dan el error total

    |Wmixed/Phi^4−Wmodelo|
      <=[61440Hstar+6144Hstar²+192Hstar³]t³/y0³
      <Cstar t³/y0³,
    Cstar=10^6(1+Hstar)^3<2^98.

Los coeficientes proceden de los tres errores simples, tres dobles y uno triple; se usan1+t<=2t,y0>=1 y a<1. Es aritmética finita sin evaluar theta. Como y0/t es creciente para t>1/2, y en64 se tiene y0>2^128 y64Cstar<2^104,

    Wmixed(t)/Phi(t)^4>6t²/y0²>0,
    para TODO t>=64.                            (POSITIVE-TAIL)

La orientación positiva es, por tanto, rigurosa y previa al test de origen. t es la variable temporal interna, no una ventana T.

## 6. Lectura predeterminada del gate

- **Dmix<0:** ORIGIN y POSITIVE-TAIL producen determinantes de evaluación con orientaciones opuestas, por confluencia en puntos suficientemente cercanos. Por continuidad en la cámara de cuatro nodos, el sistema mixto NO puede ser Chebyshev4 global. Esto refutaría sólo ESA condición suficiente para la continuación, no el cruce del U particular, la positividad de su primitiva, su kernel, W ni otros mecanismos.
- **Dmix>0:** sólo verifica el signo de origen en una vecindad existente, sin radio. No prueba Chebyshev4 global ni conservación indefinida.
- **Dmix contiene0:** inconcluso con el diseño fijado, sin nuevos parámetros.

La implementación seguirá la aprobación independiente del diseño; no se ejecutará hasta auditar también su literal. Después se permitirá UNA recuperación exacta087 y UNA evaluación de este polinomio, no una campaña de puntos, pivotes o precisiones.


## 7. Resultado de la única recuperación y gate

Tras aprobación matemática y literal independiente por root y mapa, el constructor terminó exit0/PASS con el script fijo. No hubo modificación de parámetros, coeficientes, precisión o entradas después de observar el signo. La decisión fue

    PASS104: mixed-four origin sign POSITIVE.

Los extremos racionales completos son

    lower=20910875038731301173957476100644455719909401587771537215845430471153/
          5000000000000000000000000000000000000000000000000000000000000000000000,

    upper=41821750077462602464978622735022256356361140514400545338810504099651/
          10000000000000000000000000000000000000000000000000000000000000000000000.

Ambos numeradores y denominadores son estrictamente positivos; la cifra aproximada0.00418217500774626 es sólo una lectura, no la prueba. El intervalo se obtiene con la clase racional I70 de087 y las entradas completas103, sin quitar colas ni inferir jets de decimales aproximados.

La salida COMPLETA queda persistida en

    tools/power_mixed_four_origin_104_verify.log.

Ese archivo guarda además los extremos racionales recuperados de Phi0,z1,z2,z3, junto con el hash087 y sus pruebas de cola/paridad. Permite reutilizarlos en el futuro sin volver a ejecutar theta. No se alteró el script087.

SHA256 de104:

    063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105.

Comando desde la raíz:

    python3 03-research/phase-211-sign-sandbox/tools/power_mixed_four_origin_104_verify.py

ORIGIN y Dmix>0 prueban Wmixed>0 en una vecindad existente de0, sin radio certificado. POSITIVE-TAIL prueba el mismo signo para TODOt>=64. **El intervalo intermedio sigue abierto**: no se demuestra Chebyshev4 global, conservación de la pareja, el cruce particular de U ni positividad de una nueva primitiva. No se encontró una refutación de la ruta por este gate. Tampoco se afirma nuevo signo W, generadores, todos los órdenes o ventana T.

Root reprodujo el mismo script con exit0/PASS y el mismo hash063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105. El cierre documental y lectura final se registrarán en la auditoría104. El resultado no autoriza tests adicionales de parámetros o puntos no diseñados.

## Ampliación analítica: conservar potencias del resto reduce la cola a t>=16

**PROVED / revisión independiente root y mapa, sin datos theta nuevos.** En los siete términos multilineales de§5 no es necesario descartar todas las potencias adicionales de y. Conservándolas se obtiene

`error <=61440 Hstar t³/y³+6144 Hstar² t³/y⁴+192 Hstar³ t³/y⁵`.

Los tres términos simples tienen y^-3; los tres dobles tienen y^-4 y el triple y^-5. Se mantienen los mismos mayorantes de entradas y1+t<=2t. Para y>=Hstar, el error es menor que2^17 Hstar t³/y³, pues61440+6144+192=67776<2^17.

Con Hstar=39321600, Taylor positivo hasta grado5 prueba exp2>7; el cálculo entero exacto da

`3*7^16=99698791708803 >16*2^17*Hstar=82463372083200`.

Por tanto y(16)=pi exp32>3*7^16 y, como y/t crece para t>1/2, para TODOt>=16 se tiene y>=Hstar yerror<t²/y². El modelo anterior es mayor que7t²/y², de modo que

`Wmixed(t)/Phi(t)^4>6t²/y²>0 para TODOt>=16`.

Es una mejora del resto104, no una nueva evaluación de theta ni cambio de parámetros de110. La corrida110 se conserva intacta. No se infiere signo del compacto ni cobertura global sin sus pruebas y reproducción correspondientes.
