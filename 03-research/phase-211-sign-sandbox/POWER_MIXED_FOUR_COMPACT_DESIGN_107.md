# POWER — Diseño compacto del sistema mixto, ronda107

Estado: **DISEÑO AUDITADO; CORRIDA107 INCONCLUSA EN ORIGEN.** Reproducción independiente mapa46719 terminada con el mismo resultado. Este documento conserva los parámetros previos a datos y no afirma el signo compacto.

## 1. Objeto y diferencia respecto del corpus

Se consulta las reglas del proyecto, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID y CROSSWORD-TO-D, y las fuentes103–106. El objetivo es W_t(K,J,Phi,J'')>0 para0<t<64. El origen104 es positivo sin radio y la cola104 cubre t>=64; ninguno cierra el intervalo. Este sistema PAR no es el sistema impar particular093/095. Su positividad, junto al CT3 de103, permitiría el argumento de dos operadores de Rolle para la segunda pareja real de102. No es una consecuencia automática de099 ni un resultado sobre la forma completa.

Escribir a=I2/I0, J(t)=integral_t^infinito s Phi(s)ds y K''=a Phi-J, con K par, positivo y decreciente en la semirrecta. Ij=integral_0^infinito t^j Phi(t)dt. Se usan las fórmulas y normalizaciones103, no nuevos datos de momentos.

## 2. Presupuesto fijado antes de datos

Rama origen: t en[0,1/2], lambda=t^2 en[0,1/4]; precisión1024bits;128 modos; jet t de Phi con cap1025; polinomios lambda de grado512. Partición inicial16 celdas lambda de ancho1/64. Subdivisión interna izquierda primero, profundidad máxima10 y máximo8192 evaluaciones de celdas.

Rama restante: t en[1/2,64]; precisión512bits; jet temporal cap4 para integrales, cap5 para el logaritmo theta local. Gauss–Legendre64 en cada uno de los diez segmentos v con extremos0,1,2,4,8,16,32,64,128,256,512. Partición inicial508 celdas temporales de ancho1/8. Profundidad máxima10 y máximo8192 evaluaciones de celdas, izquierda primero.

Una celda se acepta sólo si el límite inferior del determinante intervalar es positivo en TODA la celda. Si su límite superior es negativo se informa ese intervalo. Si no se decide y se agota profundidad o presupuesto, resultado INCONCLUSO. No se cambian parámetros según signos observados. Sólo una cobertura completa permite afirmar el signo compacto.

## 3. Origen: función holomorfa y colas fijas

Sea phi(lambda)=Phi(sqrt(lambda)); la paridad de Phi define esta función holomorfa en un entorno de |lambda|<=1/2. En ese disco |t|<3/4, Re(pi exp(2t))>3/80 y |pi exp(2t)|<20. Se usan cos(3/2)>1/16, exp(3/2)<5 y exp(15/8)<9. La suma theta absoluta proporciona

 |phi| <=1548 sum_(m>=1) m^4 exp(-3m^2/80)
       <=1548*24*(83/3)^5 <2^40.

Retener modos1..128. Desde m=129 la razón de los mayorantes es menor que1/2, y la cola es menor que2^-583: 129^4<2^29 y 3*129^2/80>624. La extracción de coeficientes PARES del jet t equivale a simetrizar el parcial; no se supone que un parcial theta sea par. Cauchy en lambda radio1/2 da un error de coeficiente <=2^-583*2^k para k0..512. Se añade antes de productos, recurrencias o determinantes.

Para el Taylor completo de grado512, sus restos y derivadas de orden0..4 sobre lambda real[0,1/4] son menores que2^-426. Por ejemplo N=513 y sum_(n>=N) n^4 2^-n<3N^4 2^-N, N^4<2^37; se pagan además2^40 y4^4. No se evalúa una división por t^6 ni por lambda en un intervalo que contenga0.

## 4. Origen: momentos, recurrencias y matriz

Los datos103 se introducen como cajas racionales exactas outward:

 I1=0.02152870762556652324898962 +/-3.96e-27,
 I3=0.00191588830192231322996545 +/-4.90e-27.

Para a se usa exclusivamente un jet PUNTUAL fijo de la función completada E en0 a1024bits, cap3, a=2E[2]/E[0]. E(u)=A[1+(A-1)zeta_deflated(A)] Gamma(A/2) exp(-A log(pi)/2), A=u+1/2. La deflación resta1/(A-1). Se comprueba compatibilidad con el intervalo098 a=0.0462099862308379415778676 +/-3.74e-26; ese intervalo ancho no sustituye al nuevo encierro puntual. Este cálculo es parte del futuro certificado, no se ha ejecutado para107.

Si phi_k son los coeficientes lambda, construir

 J_0=I1, K_0=a I1-I3/2,
 J_k=-phi_(k-1)/(2k),
 K_k=(a phi_(k-1)-J_(k-1))/(2k(2k-1)), k>=1.

Todos los errores de I1,I3,a y phi_k se propagan por aritmética intervalar antes del determinante. Las constantes a,I1,K0<1 se comprueban como assertions.

Para justificar las colas de estas recurrencias, J_lambda'=-phi/2 y

 K(lambda)=K0-I1 lambda/2
 +a lambda integral_0^1 (1-s)phi(s^2 lambda)ds
 +(lambda^2/2) integral_0^1 s(1-s)^2 phi(s^2 lambda)ds.

Esto da |J|,|K|<2^42 en |lambda|<=1/2. Con el mismo cálculo de cola anterior, el error de entradas derivadas hasta4 es menor que2^-420. Se añade conservadoramente una bola2^-400 a CADA entrada de la matriz, después de evaluar los polinomios conocidos. No se rellenan coeficientes desconocidos con ceros sin pagar este error.

La matriz tiene columnas K,J,phi,Q, filas derivadas lambda0..3, donde Q=J''_t=-phi-2lambda phi'. Así Q^(j)=-(2j+1)phi^(j)-2lambda phi^(j+1). Se multiplican coeficientes de jets por factoriales para obtener derivadas. Su determinante es W_lambda; el puente exacto es W_t=64t^6 W_lambda. La matriz se evalúa en la bola de la celda completa.

## 5. Resto: integrales normalizadas directas

Reutilizar el lema106, incluida su sección8, sin propagar datos mediante ODE. Para t en una celda, y=pi exp(2t), r=Log(1+v/y)/2 y

 Theta16(y)=2y-3+sum_(m=2)^16 m^2(2m^2 y-3)exp(-(m^2-1)y),
 A16=exp(-v)/(2y)*(1+v/y)^(1/4)*Theta16(y+v)/Theta16(y).

Integrar juntos los jets de (t+r)A16 y [a r-(t+r)r^2/2]A16. La rama principal es holomorfa por106. Para las evaluaciones reales, comprobar denominador positivo y1+v/y positivo. No se emplea acb.integral ni se omite una condición de rama.

En cada celda fijar Yc=pi exp(2c), constante respecto al jet. Las columnas son Yc^2 kappa,Yc tau,1,X/Yc, X=t p-1, p=-Phi'/Phi. El determinante es Yc^2 W_t/Phi^4. La columna constante permite calcular el menor3x3 de filas derivadas1..3 y columnas primera, segunda y cuarta, con signo positivo. p se obtiene de Theta16 local con cap5, no derivando datos iniciales de una ODE.

## 6. Errores Gauss, modos y dominio

La prueba106 sección8 da, para el coeficiente temporal j, error Gauss <=2^(-83+5j), j0..3. La API arb.legendre_p_root(64,k,weight=True) proporciona nodos y pesos encerrados; su redondeo se propaga además por aritmética intervalar. Verificar positividad de pesos y que su suma encierra2 antes de transformar cada segmento.

El semiancho temporal inicial1/16 es admisible: la unión de discos de radio1/32 alrededor de sus puntos satisface |z-c|<=3/32, Re z>=1/2-3/32>-1/16, |Im z|<=1/32 y |z|<65. Además Yc/Y<exp(3/16)<2 y Yc^2/Y^2<exp(3/8)<2. Por ello siguen válidos los mayorantes4096 exp(-Re v)(1+|v|)^5 y2^34 de106. Las celdas subdivididas sólo reducen estos dominios.

Añadir antes del determinante errores coeficientes2^-81*32^j a ambas columnas integradas, incluyendo Gauss, cola v>512 y modos>16 según106. Para X/Yc usar el error local106 <=2^-687*32^j. Los errores son para coeficientes normalizados; pagar factoriales al convertir a derivadas. No se usa |y+v|>=Y+v, que sería falso para y complejo.

## 7. Implementación prevista y coste

Por celda se pueden precomputar los15 jets exp(-(m^2-1)y) y reutilizar los factores escalares exp(-(m^2-1)v) en los640 nodos. Esto es una identidad exacta que reduce el coste, no cambia regla ni precisión. El máximo resto es8192*640=5242880 evaluaciones vectoriales cap4; puede requerir horas. El diseño no garantiza terminación con signo y no se ejecutará antes de la revisión independiente del literal.

## 8. Pendientes exactos y alcance

Pendiente: auditoría del presente diseño; implementación literal de theta/jet origen y regla Gauss con errores explícitos; revisión independiente del código; ejecución única; reproducción y archivo íntegro de salida/hash si procede. El presupuesto del origen aquí usa la cota robusta2^40, no las cotas más finas discutidas informalmente. Debe revisarse literalmente que la cola de entradas2^-400 cubre la combinación Q, las recurrencias y todos los factoriales; las cajas de momentos se propagan sin absorberse en esa cola.

SIGNO GLOBAL ABIERTO. Una salida INCONCLUSA no refuta el signo. Ninguna parte de este diseño añade cobertura de W, de ventanas T ni de todos los órdenes. La transferencia a la siguiente pareja sólo se invocará después de demostrar el sistema mixto completo.


## 9. Auditoría y salida real de107

Mapa aprobó el diseño completo. El pago de entradas del origen se justifica explícitamente: para J,K, la cota2^42 y el Taylor512 dan, hasta derivada4,

 2^42 * 4^4 * 3 * 513^4 * 2^-513 <2^-424.

Para Phi se tiene2^-426; la combinación Q y sus derivadas hasta3 cuestan menos que8 veces ese error, por tanto menos que2^-423. El pago2^-400 por entrada es holgado. Los errores de modos, momentos y a siguen propagándose antes de los productos; no se consideran correlacionados gratuitamente.

El root ejecutó el literal aprobado: sesión5594, exit2, INCONCLUSIVE en lambda=[0,1/65536], profundidad10,11 evaluaciones,0 celdas aceptadas. La bola del determinante tenía radio aproximado0.00294; esa aproximación sólo describe la salida, no certifica un signo. No se ejecutó la rama restante. No se cambiaron parámetros. La reproducción independiente mapa46719 terminó exit2 con exactamente el mismo resultado; véase sección10.

El fallo es de encierro, no una refutación. Una representación posterior podría formar primero el determinante como polinomio en la MISMA variable lambda y evaluarlo después. Eso requiere pagar explícitamente colas y errores de coeficientes; no se ha probado ni ejecutado todavía aquí.

## 10. Reproducción independiente y alcance final

Root constructor5594 terminó exit2: INCONCLUSIVE por profundidad máxima del origen. Reproducción independiente mapa46719 terminó igualmente exit2. Ambas corridas hicieron11 evaluaciones,0 hojas aceptadas y alcanzaron profundidad10 en lambda[0,1/65536], con determinante impreso[+/−2.94e−3]. Este ball no separa0: no es prueba de signo negativo ni de fallo de la hipótesis. REST NO se ejecutó, según el main auditado.

Logs completos:`tools/power_mixed_four_compact_107_root.log` y `tools/power_mixed_four_compact_107_audit.log`. Hash main:`2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054`; hash origen:`15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553`. Coincidieron en ambas corridas y tras la reproducción. No se editaron scripts ni parámetros para lograr otro resultado.

Sólo se registra insuficiencia del encierro intervalar con ESTE presupuesto; no hay obstrucción matemática, Chebyshev4 decidido, cruce U finito, W negativo ni nueva cobertura. Otro objeto o representación deberá diseñarse y auditarse antes de cualquier nueva ejecución. Los signos locales104 y todas las pruebas analíticas previas permanecen vigentes.
