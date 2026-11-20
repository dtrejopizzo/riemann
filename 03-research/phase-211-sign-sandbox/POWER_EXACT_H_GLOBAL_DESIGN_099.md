# POWER_EXACT_H_GLOBAL_DESIGN_099 — Diseño fijo y prueba global de la obligación exacta T_h

**Auditoría independiente:** fuente final, diseño y literal aprobados en `POWER_EXACT_H_GLOBAL_AUDIT_099.md`; constructor98529 FULL PASS2048, reproducción independiente root8310 exit0/FULL PASS2048 y hash coincidente. Aplicación exacta: `POWER_SCHUR_TRIPLES_APPLICATION_099.md`; estado: `POWER_STATE_099.md`.

Estado: **PROVED por constructor y reproducción independiente root8310 exit0/FULL PASS2048; lectura final y auditoría aprobadas, hash coincidente.** Root y mapa aprobaron diseño y literal ANTES de la única corrida. Se conserva el diseño previo y su historial analítico; el resultado está en§8. Papers intactos.

## 1. Objeto, antecedentes y cambio de representación

Consultados las reglas del proyecto, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D, y073/077/078/080/085/089/090/092/093/095/097/098.097 probó la obligación EXACTA T_h>0 para u>=512;098 decidió T_h(0)>0 por seis momentos completos. Las condiciones puntuales de densidades093/095 son más fuertes y no se presuponen globales.090 refuta una herencia genérica de Turán; no se la reintenta.

Este diseño se dirige directamente al compacto restante usando una función ENTERA regularizada. No se certifica una matriz nueva, una condición suficiente de densidades ni sólo muestras de T_h. Se reutiliza el mecanismo de jets centrales y Cauchy080/085, pero se eliminan los denominadores y el cero algebraico u^15 ANTES de fijar el test. La diferencia es esencial para evitar que un bound triangular de variación pierda el signo sólo por ese factor conocido.

Sea E un múltiplo constante positivo de la transformada Z de Phi, M=E'/E,a=M'(0)>0,x=u² y

    N(x)=M(u)/u,
    h(x)=xN(x)/(a−N(x)),
    T_h=2h'h'''−3(h'')²,

con derivadas de h respecto de x. Definir las funciones enteras en x

    U(x)=E'(u)/u,
    V(x)=[aE(u)−U(x)]/u².

Su entiridad proviene de la paridad de E y de aE(0)=E''(0): U=2dE(sqrt x)/dx; el numerador de V tiene término constante cero. No se presupone que h=U/V sea entera ni que V carezca de ceros complejos.

Con derivadas respecto de x, poner Wij=V^(i)U^(j)−V^(j)U^(i). La identidad polinómica exacta es

    NUM_x=−W_x(V,xV,U,xU)
         =2W01W03+6W01W12−3W02².

Es entera sin denominadores. En reales x>0, V>0 por073 y NUM_x=V^4 T_h.

## 2. Polinomios enteros en E y regularización del cero15

Poner ej=E^(j)(u),j=0,...,4, derivadas SIN normalizar por factorial. Definir

    PS=u^4(2e0²e2e4−3e0²e3²−2e0e1²e4+10e0e1e2e3
             −6e0e2³−4e1³e3+3e1²e2²)
       +u³(2e0²e1e4−6e0²e2e3−2e0e1²e3+12e0e1e2²−6e1³e2)
       +u²(6e0²e1e3−9e0²e2²+3e1^4)
       +u(6e0²e1e2−6e0e1³)+3e0²e1²,

    PC=u³(e0e1²e4−6e0e1e2e3+6e0e2³+2e1³e3−3e1²e2²)
       +u²(6e0e1²e3−12e0e1e2²+6e1³e2)
       +u(3e0e1²e2−3e1^4)+3e0e1³,

    Ntilde=a u PS−4PC.

PS=E^4 N_S y PC=E^4 C_h, con N_S,C_h definidos y auditados097. PS tiene18monomios, suma absoluta de coeficientes91 y grado en u<=4; PC tiene11monomios, suma51 y grado<=3. Todos son cuárticos homogéneos en e0,...,e4.

La fórmula DIRECT097 y NUM_x=V^4T_h, primero en u>0 y luego por identidad de funciones enteras, dan

    Ntilde(u)=(16/a)u^15 NUM_x(u²),
    S(u)=Ntilde(u)/u^15=(16/a)NUM_x(u²).          (ENTIRE-S)

Por tanto S es ENTERA y PAR, con la división removible ya justificada. Su valor en0 es S(0)=192E(0)^4H3>0 por098. La entiridad se funda en U,V y ENTIRE-S, **no** en suponer que T_h meromorfa carezca de singularidades complejas.

En reales u>0, S>0 equivale exactamente a T_h>0. La implementación evaluará el cociente en centros estrictamente positivos; no se evalúa0/0. El bound Cauchy siguiente se aplica a la S entera real, no a una familia arbitraria donde se varíe a rompiendo aE0=E''0.

## 3. Bound de crecimiento completo, sin discos libres de ceros

La positividad de Phi y la paridad de E dan, para cada centro real c>=0,|z−c|<=r y cada j>=0,

    |E^(j)(z)|<=2j! E(c+r+1).

Se usa |t|^j<=j!exp(|t|) bajo la integral; todas las colas se conservan. Para c<=512,r=1, la monotonicidad real073 y el ancla gamma/arimética completa garantizan M(t)<3 hasta514. Una comprobación elemental puede usar el ancla A=516: psi(A/2)<=log(A/2), el término primo favorable y pi>3 dan M(515.5)<log86/2+1/516+1/515<3, pues86<(8/3)^5<exp5. La monotonicidad extiende el upper a todo el intervalo requerido.

La cota elemental auditada exp1<87/32 y(87/32)^6<512 dan exp6<512. Así E(c+2)/E(c)<exp6<512 y en el disco de radio1,

    |ej|/E(c)<1024j!<2^15, j<=4,
    |u|<513<2^10, a<8.

La cota a<8 está sobradamente contenida en el intervalo certificado098, y será comprobada también para su refinamiento puntual. Por las sumas de coeficientes de§2,

    |PS|/E(c)^4<2^107,
    |PC|/E(c)^4<2^96,
    |Ntilde|/E(c)^4<2^121.                       (RAW-BOUND)

No se exige que E(z) sea no nula en el disco: no aparecen sus cocientes complejos ni logaritmos en estos polinomios.

## 4. Bound uniforme de S a través del origen removible

Si |z|>=1/4 dentro de un disco anterior, RAW-BOUND implica

    |S(z)|/E(c)^4<2^121*4^15=2^151.

Para |z|<=1/4 usar un círculo centrado en0. Puesto que E(c)>=E(0), la misma desigualdad de derivadas y M<3 dan en |z|=1/4

    |ej|/E(c)<=2j! E(5/4)/E(0)
               <128j!<2^12, j<=4.

Aquí exp(15/4)<64, por log2>56/81. Además |z|<=1 y a|z|<2. Por las sumas91 y51 se obtiene |Ntilde|/E(c)^4<2^57 en ese círculo. ENTIRE-S y el principio del máximo, aplicado a la función ya removida, dan en TODO |z|<=1/4

    |S(z)|/E(c)^4<2^57*4^15=2^87.

Ambos casos prueban en cada disco |z−c|<=1,c en[0,512], el único bound fijo

    |S(z)|/E(c)^4<2^151.                         (CAUCHY-S)

No se resta a ciegas un resto de u^15 en un panel que toca0: el factor fue eliminado algebraicamente en la función que se certifica.

## 5. Parámetros fijados antes de ejecutar

UNA rama, dominio[0,512],2048paneles, semiancho h=1/8, centros

    c_j=(2j+1)/8, j=0,...,2047.

Precisión1024bits, cap de E109, Taylor grado104. Todos los centros son positivos. Radio Cauchy r=1 y razón h/r=1/8. Normalizar la serie entera E por su valor real positivo E(c_j), CONSTANTE respecto de la variable formal; así se certifica S/E(c_j)^4. La incertidumbre del valor normalizador se mantiene outward.

Antes de evaluar centros, la revisión independiente detectó otra pérdida estructural del lower triangular: S conserva el factor E(u)^4. En la cola, su crecimiento lineal en un panel podría consumir el signo aunque S fuese positiva. NO hubo corrida ni signo observado. Se fija por ello el gauge ENTERO por panel

    G_c(u)=exp[−4M(c)(u−c)]S(u)/E(c)^4,
    M(c)=E'(c)/E(c).

El FACTOR EXPONENCIAL es positivo en reales; no se presume el signo de G_c. No se divide por E(u) variable. En el disco de radio1, |M(c)|<3 da un factor máximo exp12<2^18. Por CAUCHY-S,

    |G_c|<2^169,
    REM=2^169*(1/8)^105/(1−1/8)<2^(−145).

La eficacia de quitar ese crecimiento tiene una razón previa analítica:073 da0<M'(u)<=a<1 en u>=0. Para |s|<=h,c+s>=0,

    0<=logE(c+s)−logE(c)−M(c)s<=a s²/2.

Así el factor E(c+s)^4 exp(−4M(c)s)/E(c)^4 pertenece a[1,exp(2ah²)] y es menor que exp(1/32). Esto no garantiza el signo del resto de la función; elimina una pérdida conocida antes de pedirle al certificado que lo decida. Los ajustes Taylor96→104 y cap101→109 pagan exactamente el bound del gauge; no cambian malla, precisión ni centros, y fueron fijados ANTES de evaluar.

Para cada centro, exigir G.prec>=105 y coeficientes0,...,104 finitos. El test continuo de positividad es

    G[0]−sum_(k=1)^104 abs(G[k])*h^k−REM>0.

El test verifica TODO el panel cerrado. No toma muestras como sustituto de un lower continuo. Si falla un encierro, no es por sí mismo un signo negativo y no autoriza ajustar los parámetros para forzar PASS.

## 6. Dato a preciso y evaluación reproducible propuesta

No se utiliza el intervalo ancho de a098 como dato principal para las divisiones por u^15. Antes de recorrer paneles, encerrar nuevamente el MISMO a por la identidad exacta

    a=E''(0)/E(0),

en un único jet central de orden2 y1024bits. Se comprueba que el intervalo nuevo está contenido en el intervalo certificado098

    0.0462099862308379415778676 +/- 3.74e−26.

Se conserva el nuevo encierro estrecho, sin sustituirlo por el intervalo antiguo más ancho. No es un nuevo dato libre; ambos encierran la misma constante y se verifica su consistencia.

Para evaluar E se usa la fórmula entera ya auditada080/085 con A=u+1/2,

    E(u)=A[1+(A−1)zeta_deflated(A)]Gamma(A/2)pi^(−A/2).

zeta_deflated(A)=zeta(A)−1/(A−1), NO(A−1)zeta(A). Definición oficial de la API: https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html . Las evaluaciones son sólo jets en centros exactos, no bolas de parámetro zeta. La identidad con la transformada theta par viene de las definiciones auditadas de CONE001/073; las constantes positivas globales no afectan M,a ni el signo.

E.prec109 deja E^(4).prec105; los productos PS,PC,Ntilde y la división formal por u^15 conservan coeficientes conocidos0,...,104 en cada centro no nulo. No rellenar derivadas desconocidas con ceros. Los ej son derivadas FUNCIONALES obtenidas por derivative(), no coeficientes Taylor sin sus factoriales. Se computan de la serie E original normalizada por la CONSTANTE E(c), NO de una serie ya modificada por el gauge. Primero se evalúan PS,PC,Ntilde/u^15; sólo después se multiplica por exp[−4M(c)(u−c)]. M(c) se encierra desde el mismo jet puntual, sin evaluar M en discos complejos.

La sustitución de una bola estrecha por a en las operaciones encierra el valor real seleccionado. La prueba Cauchy se aplica a ese valor real exacto, cuya relación de momentos asegura ENTIRE-S; no se exige que todas las constantes ajenas contenidas en la bola definan funciones removibles.

## 7. Conclusión prevista por el diseño y límites

Si todos los paneles verifican el lower, el gauge real positivo implica S>0 en[0,512], y por ENTIRE-S se prueba T_h>0 en0<u<=512. Empalmar con097 descarga T_h>0 para TODOu>0.098 da además el valor positivo en0. Esta es la obligación exacta, más débil que el signo temporal de densidades particulares.

El diseño no afirmaba el resultado antes de la corrida;§8 registra su decisión. Aun después de un PASS, no se infiere herencia de Turán del siguiente resto, iteración a todos los órdenes ni signo global de W. Las aplicaciones se formularán y auditarán separadamente; el parámetro u no es una nueva ventana T. No nueva implementación hasta aprobar este diseño independientemente.


## 8. Corrida constructora: obligación exacta global descargada

Después de las aprobaciones matemáticas y literales independientes de root y mapa se ejecutó UNA corrida fija, handle propietario98529. Terminó exit0, sin cambios de parámetros, código o representación durante la ejecución:

    PASS all predeclared Cauchy, Schwarz and gauge bounds
    PASS precise a, certificate098 containment and entire representation
    PASS exact T_h panels128 of2048
    ...
    PASS exact T_h panels2048 of2048
    PASS ALL099: exact T_h positive throughout[0,512].

El refinamiento puntual de a se encerró con radio menor que5.69e−306 y estuvo contenido en el intervalo completo098. Ninguna corrida de momentos previa se importó ni se volvió a ejecutar para la prueba099. La decisión continua usa cada lower de§5, todos los coeficientes hasta104 y el resto EXACTO

    REM=1/78052608194857180995375013954269265270931456.

El signo probado es el del gauge entero positivo por panel, por lo que S>0 en TODO[0,512]. La identidad ENTIRE-S y V>0 en reales positivos prueban

    T_h(u²)>0 para TODO0<u<=512.

Empalmar con la cola analítica completa097 descarga la obligación EXACTA

    T_h(x)=2h'(x)h'''(x)−3h''(x)²>0
    para TODO x>0.

098 da también T_h(0)>0 en su extensión removible. Este resultado se refiere a la MISMA Phi real y conserva la aritmética completa por la representación entera E; no es una herencia genérica desde T_R. Tampoco demuestra que el Wronskiano temporal particular093/095 tenga signo en todo su intervalo intermedio: esa condición era más fuerte y no se usó.

SHA256 del script fijo, sin modificaciones durante la corrida:

    6712eb8542b4d8b7e0836260fba831cd44ccaffb7f1ea321df0a0a32668d51d7.

Comando reproducible desde la raíz:

    python3 03-research/phase-211-sign-sandbox/tools/power_exact_h_global_099_verify.py

No se infiere de este paso una nueva herencia de Turán para el siguiente resto, iteración a todos los órdenes, signo global de W ni una ventana T nueva. Las aplicaciones adicionales deben formularse y auditarse separadamente. La fuente conserva la diferencia entre la variable de inclinación u y la variable temporal t de095. La auditoría099 está aprobada y la reproducción independiente root8310 terminó exit0/FULL PASS2048 con hash y resto exacto coincidentes.
