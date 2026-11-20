# POWER_EXACT_H_ORIGIN_DESIGN_098 — Diseño previo y decisión del jet exacto de T_h

**Actualización099:** la obligación REAL T_h>0 global quedó cerrada en `POWER_EXACT_H_GLOBAL_DESIGN_099.md`, auditada en `POWER_EXACT_H_GLOBAL_AUDIT_099.md` y resumida en `POWER_STATE_099.md`. Se prueban ambas curvaturas y todos los triples del resto G_p; el bloque auxiliar de cinco nodos está anclado en0 y NO son cinco generadores W admisibles. Las menciones de compacto/hipótesis pendiente abajo conservan el estado histórico de esta ronda; la herencia al siguiente nivel sigue abierta.

**Auditoría independiente:** `POWER_EXACT_H_ORIGIN_AUDIT_098.md` aprobada; constructor19778 exit0/FULL PASS, reproducción independiente root57072 exit0/FULL PASS128 y hash coincidente.

Estado: **PROVED PUNTUAL por constructor exit0/FULL PASS; diseño y literal aprobados independientemente ANTES de la corrida.** Lectura final y reproducción independiente pendientes. Se conserva el diseño previo; resultado en§6. Papers intactos.

## 1. Diferencia, antecedentes y objeto

Consultados las reglas del proyecto, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D, y073/077/078/087/090/092/093/095. Las identidades Hankel/Schur abstractas ya están registradas; no prueban por sí mismas un signo.093 verificó un jet de una condición de densidades más fuerte. Aquí se decide la condición EXACTA T_h(0), utilizando sólo seis momentos de la MISMA Phi real. No nuevos pivotes o muestras; no se infiere signo global desde el origen.

Con Z(u)=integral_R exp(ut)Phi(t)dt, M=Z'/Z, x=u² y

    N(x)=M(u)/u=a+b x+c x²+d x³+e x^4+O(x^5),
    h(x)=xN(x)/(a−N(x)),
    T_h=2h'h'''−3(h'')²,

la regularización algebraica exacta da

    T_h(0)=12a H3/b^4,
    H3=det[[a,b,c],[b,c,d],[c,d,e]].

Aquí a=κ2,b=κ4/6,c=κ6/120,d=κ8/5040,e=κ10/362880, con κ los cumulantes de la probabilidad Phi/Z(0).La varianza073 da a>0;086/097 dan R'(0)>0 para R=1/N, y por R'(0)=−b/a² se obtiene b<0. No se deduce esa desigualdad estricta sólo de M''<0 en u>0. El script comprobará además que sus intervalos verifican esas desigualdades antes de la comparación. H3 no se trata como un determinante de momentos positivos genéricos: son coeficientes de cumulantes y su signo es el test solicitado.

Definir Ir=integral_0^infinito t^rPhi(t)dt para r=0,2,4,6,8,10. Los momentos normalizados son mr=Ir/I0. Se forma la serie par Z(u)/Z(0)=sum_(k=0)^5 m_(2k)u^(2k)/(2k)!+O(u^12), con m0=1 exactamente. Derivar su logaritmo hasta grado9 produce a,b,c,d,e sin requerir momentos de orden mayor10. La implementación deberá respetar la precisión formal conocida: Z.prec>=11 y M.prec>=10, sin rellenar coeficientes desconocidos.

## 2. Parámetros previos, idénticos a093

En[0,2],128paneles, centros(2j+1)/128,j=0,...,127, h=1/128. Radio Cauchy r=1/32, razón1/4. Taylor grado64, cap65, precisión512bits, modos theta1,...,16. No ajustar después de observar el signo.

El diseño093 ya auditado prueba en los discos complejos

    −1/32<=Re t<=65/32, |Im t|<=1/32,
    |Phi(t)|<2^22, |t|<3,
    EPS=2^25*17^4/8^289

para la cola COMPLETA de modos m>=17. La única nueva mayoración compleja necesaria es

    |t^(2k)Phi(t)|<3^10*2^22<10^12, k=0,...,5.

Se añaden EPS*32^j a TODOS los coeficientes Phi[j],j=0,...,64, antes de multiplicar por cada t^(2k). No se importa ni ejecuta ninguna malla previa para calcular estos momentos.

## 3. Error de integración fijado

Cada polinomio Taylor grado64 de t^(2k)Phi se integra exactamente en el panel simétrico: términos pares2coef[j]h^(j+1)/(j+1), términos impares0. Los redondeos son intervalares outward.

Con el bound nuevo10^12 y la longitud total2, el error TOTAL del desarrollo completo es

    REM=2*10^12*4^(−65)/(1−1/4)<10^(−24).

Se añade simétricamente a cada momento. Este resto Cauchy se suma a los errores theta ya propagados en los coeficientes; no sustituye la cola theta ni se estima a partir de valores observados.

## 4. Nueva cola temporal, válida hasta orden10

093 ya demostró, conservando todos los modos,

    0<Phi(2+s)<2^(−140)exp(−300s), s>=0.

Para todos los órdenes r=0,2,4,6,8,10,

    (2+s)^r<=2^10 exp(5s),

por log(1+s/2)<=s/2. Luego

    0<integral_2^infinito t^rPhi(t)dt
       <(1024/295)*2^(−140)<2^(−138).

Se fija TAIL=2^(−138) para TODOS los seis momentos y se añade el intervalo positivo[0,TAIL]. No usar el tail2^(−140) de093, que sólo estaba fijado para órdenes0,1,2.

## 5. Test previo y alcance

La implementación verificará la positividad y finitud de los seis momentos, la finitud de las series y las precisiones formales anteriores. H3 se evaluará por la fórmula polinómica exacta

    H3=a*c*e−a*d²−b²*e+2b*c*d−c³.

El assert de decisión acepta H3>0 O H3<0. Si los intervalos no separan0, se informa inconcluso sin modificar parámetros para forzar una respuesta. No se predetermina positividad.

Un signo positivo sólo prueba T_h>0 cerca del origen en una vecindad no cuantificada; un signo negativo refutaría la propiedad global buscada para la Phi real, pero no sería un contraejemplo de W. Ni uno ni otro decide todo el intervalo restante ni todos los órdenes. No nueva ventana T.


## 6. Resultado constructor y alcance exacto

Tras aprobación matemática y literal de mapa y root, la ÚNICA corrida constructora19778 terminó exit0/FULL PASS128paneles, sin cambios de código, precisión, parámetros, modos o restos durante la corrida. El test que aceptaba cualquiera de los dos signos obtuvo

    PASS098: exact T_h(0) sign POSITIVE.

Salida intervalar outward de Arb:

    I0 [0.12428019454707852747819343 +/- 6.89e-27]
    I2 [0.00574298607878635938381247 +/- 2.84e-27]
    I4 [0.00074071210842190804134207 +/- 6.71e-27]
    I6 [0.00014982398664939487296086 +/- 5.39e-27]
    I8 [4.024164363754890272123e-5 +/- 2.69e-27]
    I10 [1.325965856957266369438e-5 +/- 2.26e-27]
    a [0.0462099862308379415778676 +/- 3.74e-26]
    b [-7.434519857053937232973e-5 +/- 5.94e-27]
    c [2.88347862801946559391e-7 +/- 4.83e-28]
    d [-1.3260633605059817397e-9 +/- 5.73e-29]
    e [6.427328301233202432e-12 +/- 4.61e-31]
    H3 [1.73824840842099742e-21 +/- 6.84e-39]
    Th0 [3.1551297417482263e-5 +/- 5.03e-22].

La prueba del signo es la comparación estricta intervalar del script, no la sustitución de los centros de estos intervalos. Se verifican también a>0 y b<0 antes del cociente. Todos los momentos incluyen las colas completas de modos, el resto de cuadratura y la cola temporal hasta orden10. No se usa una positividad abstracta de matrices Hankel para sustituir ese cálculo firmado.

Así **T_h(0)>0 para la Phi REAL**. La regularización de§1 es analítica cerca0 porque b!=0, y por continuidad T_h(x)>0 en una vecindad existente de x=0, sin radio certificado. Se verifica esta premisa local exacta; no se la refuta ni se infiere su signo en todo el intervalo intermedio. El nodo0 es auxiliar para el criterio anclado, no un nuevo exponente admisible de W. No nuevo número de generadores, signo global, todos los órdenes ni ventana T.

Comando desde la raíz del repositorio:

    python3 03-research/phase-211-sign-sandbox/tools/power_exact_h_origin_098_verify.py

SHA256 del script fijo:

    bebcca70c5dd54ba53841e77542aa3e3e2ea059306061dc676e24f88ee5117c9.

El script es autónomo: no importa ni ejecuta las corridas087/093, aunque conserva sus bounds analíticos y esquema de cuadratura ya auditados. La auditoría098 está aprobada y root57072 reprodujo exit0/FULL PASS128 con el mismo hash.
