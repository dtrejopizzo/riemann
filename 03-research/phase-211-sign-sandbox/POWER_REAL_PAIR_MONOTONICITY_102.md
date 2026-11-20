# POWER_REAL_PAIR_MONOTONICITY_102 — Cocientes temporales reales estrictamente decrecientes

Estado: **PROVED analíticamente usando075/077/078/089; auditorías independientes aprobadas.** Véase `POWER_REAL_PAIR_MONOTONICITY_AUDIT_102.md`. No se requiere un nuevo certificado. Se prueban (K/J)'<0 y (Psi_p/D_p)'<0 para todos p,t>0. No se prueba conservación después de nuevas reducciones, nuevos generadores W ni todos los órdenes. Papers intactos.

## 1. Consulta y diferencia precisa

Leídos las reglas del proyecto, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md y CROSSWORD-TO-D.md; cotejados075/077, el apéndice078 de STATE077, POWER_THETA_DENSITY_TRANSPORT_089.md,099 y100. La búsqueda literal adicional de `Psi_p/D_p`, `Ψ_p/D_p`, `K/J`, `K_even/J`, `K−rJ` y `J,Phi,J` en los tres índices y el corpus POWER de phase211 no encontró este resultado.

075 ya construye el denominador positivo D_p;077 ya controla el cruce del defecto J-beta D_p y paga la positividad del resto. Eso no se presenta nuevamente como avance.100 prueba que eta=-K'/J no es monótona. Aquí los objetos son otros: los cocientes TEMPORALES de dos densidades positivas K/J y Psi_p/D_p. Su monotonía se obtiene de los datos específicos077 y089 mediante Rolle con los bordes; no se infieren propiedades puntuales de densidades desde sus transformadas.

La herramienta específica adicional que se extrae de089 es un sistema Chebyshev de cuatro densidades PARES, derivando hacia el sistema impar ya probado allí. Se conserva íntegra la pareja de075/077 y no se reemplazan sus datos por hipótesis genéricas sobre potenciales como las falsificadas074/101.

## 2. Definiciones, normalizaciones y bordes

Phi es la densidad par positiva real; V=-log Phi y Z(z)=int_R Phi(t)exp(zt)dt. Definir

    M(z)=Z'(z)/Z(z), a=M'(0)>0,
    J(t)=int_|t|^infinito s Phi(s)ds,
    tau(t)=J(t)/Phi(t).

075/077 prueban tau'<0 para t>0. También tau(t)->0: la integración por partes077 da

    J(t)=t Phi(t)/V'(t)
       -int_t^infinito [sV''(s)-V'(s)]Phi(s)/V'(s)^2 ds,

por lo que 0<tau(t)<t/V'(t)->0. Se usan V'>0 y V'(t)/t->infinito.

La densidad PAR K de078/100 es

    K(t)=int_|t|^infinito (s-|t|)[a Phi(s)-J(s)]ds>0,
    K''=a Phi-J, K'(0)=0.

No es la primitiva impar de093/095.

Para cada p>0 fijar

    c=M(p)>0, beta=a p^2/(ap-c)>0,
    lambda=p^2 c/(ap-c)=p beta-p^2>0,
    D_p=Phi_p de075.

075 da D_p>0, par, y la ecuación exacta

    D_p''-p^2D_p=c Phi-pJ.                          (D-EQ)

077 da un único cruce negativo/positivo, masa nula y paridad del defecto

    Q_p=J-beta D_p, int_0^infinito Q_p=0.

Definir

    Psi_p(t)=int_|t|^infinito (s-|t|)Q_p(s)ds.

La integral de cola int_t^infinito Q_p es estrictamente positiva para t>0: después del cruce el integrando es positivo; antes del cruce es -int_0^t Q_p>0. Así Psi_p'<0 en t>0 y Psi_p(infinito)=0 implican Psi_p>0. Además

    Psi_p''=J-beta D_p, Psi_p'(0)=0.                (PSI-EQ)

La extensión par es suave: Q_p es par suave y el primer borde es cero. Las ecuaciones muestran la coincidencia de todas las derivadas en0. Las funciones usadas son reales analíticas; en particular ninguna combinación no nula tiene un intervalo nulo ni raíces de orden infinito.

Todas estas densidades y todas las derivadas empleadas decaen más rápido que cualquier exponencial. Para Phi son las colas theta ya establecidas; para J sigue de J'=-tPhi; para D_p, de075 y D-EQ, que propaga el control a derivadas superiores; para K y Psi_p, de sus integrales de cola y sus ecuaciones de segundo orden. Todos los bordes ponderados por cosh(pt), sinh(pt) que siguen son, por tanto, nulos.

Para fijar la normalización respecto del resto original, si Z_D,Z_Psi denotan las transformadas bilaterales de D_p,Psi_p, entonces

    z^2 Z_Psi(z)=Z_J(z)-beta Z_D(z),
    G_p(z)=c z Z_Psi(z)/Z_D(z).

Son las mismas ecuaciones075/077, sin cambiar el resto G_p ni suprimir un término firmado.

## 3. Lemas de Rolle con multiplicidades y bordes

Los conteos siguientes son en el intervalo ABIERTO (0,infinito). No cuentan la posible raíz en0. Se aplican a funciones analíticas no idénticamente nulas y a cualquier lista finita de sus raíces; por tanto también excluyen infinitas raíces si una cota finita de la derivada lo impide.

**Lema de un extremo.** Si h(infinito)=0 y h tiene m raíces positivas contadas con multiplicidad, entonces h' tiene al menos m raíces positivas, siempre que h no sea idénticamente cero en la cola. En efecto, las multiplicidades en las raíces aportan m-k raíces de h' para k raíces distintas; Rolle entre ellas aporta k-1. Después de la última raíz existe una raíz adicional de h': escoger un punto posterior con h distinto de0 y usar que h vuelve a0 en infinito obliga a un extremo interior. Total m. El argumento puede hacerse en intervalos compactos escogiendo un extremo derecho suficientemente lejano.

**Lema D2.** Si además h'(0)=0 y h'(infinito)=0, entonces h'' tiene al menos m+1 raíces positivas. Aplicar el lema anterior a h da al menos m raíces positivas de h'. Sus multiplicidades y los intervalos entre ellas, incluido el intervalo desde el cero h'(0)=0 hasta la primera, aportan m raíces positivas de h''. El retorno de h' a0 en infinito aporta una más. Para m=0, si se necesita esa versión, los dos bordes h'(0)=h'(infinito)=0 y h' no nula fuerzan igualmente un extremo interior. En nuestras contradicciones se usa m>=2.

**Lema Lp.** Para p>0, sea Lp h=h''-p^2h. Si h es par, todas las funciones relevantes tienen decaimiento superexponencial y h tiene n raíces positivas, entonces Lp h tiene al menos n+1 raíces positivas. Poner

    g=h/cosh(pt), T=cosh(pt)^2 g'
      =cosh(pt)h'-p sinh(pt)h.

g tiene las mismas raíces y multiplicidades que h. El lema de un extremo da al menos n raíces positivas de g' y de T. Por paridad T(0)=0; por los bordes T(infinito)=0. El mismo conteo desde0 y hacia infinito da al menos n+1 raíces positivas de T'. Finalmente

    T'=cosh(pt)[h''-p^2h].

El factor cosh es estrictamente positivo, por lo que no cambia raíces ni multiplicidades. No hay una excepción con g' o T idénticamente nulas: ello daría h constante por cosh(pt), incompatible con el decaimiento salvo h=0.

En particular, si F es par y superexponencial y tiene m>=2 raíces positivas, entonces

    F'' tiene al menos m+1 raíces positivas,
    Lp(F'') tiene al menos m+2 raíces positivas.    (GAIN)

## 4. Cociente K/J: prueba a partir del valle real077

077 prueba para la Phi REAL que

    R(t)=[V'(t)+tV''(t)]/[-tau'(t)]

es estrictamente creciente e infinita. Para contar multiplicidades se puede usar la conclusión más precisa R'(t)>0, que sale de la misma prueba TAIL-AVERAGE077: si R^-1 es el promedio de cola de L bajo la densidad estrictamente positiva w, con L estrictamente decreciente, entonces

    (R^-1)'=w(t)[Avg_tail L-L(t)]/int_t^infinito w<0.

Así R'>0 para t>0 sin nuevo certificado.

Fijar r>0 y H_r=K-rJ. Como J''=(tV'-1)Phi,

    H_r''=-r Phi B_(1/r),
    B_l(t)=tV'(t)-1+l[tau(t)-a],
    B_l'=(-tau')[R-l].                             (VALLEY)

Cada B_l es estrictamente creciente o tiene un único mínimo interior. En un punto crítico, B_l''=(-tau')R'>0. Por ello B_l tiene a lo sumo dos raíces POSITIVAS contadas con multiplicidad: dos simples o una doble en el mínimo, o menos. La posible raíz en0 no se cuenta y no afecta el argumento. B_l no es idénticamente nula, porque R es estrictamente creciente.

Luego H_r'' tiene a lo sumo dos raíces positivas. El lema D2 implica que H_r no puede tener dos raíces positivas contando multiplicidad.

Sea rho=K/J>0. Si rho'(t0)=0 en t0>0, escoger r=rho(t0)>0 daría H_r(t0)=H_r'(t0)=0, es decir una raíz de multiplicidad al menos2. Es imposible por la cota anterior. Por tanto rho' no se anula.

Su dirección se fija por una cota temporal, no por sus transformadas. Escribir A0(t)=int_t^infinito Phi(s)ds. La convexidad de V da, para x>=t y y>=0,

    Phi(x+y)<=exp[-V'(t)y]Phi(x),
    A0(t+y)<=exp[-V'(t)y]A0(t).

Fubini positivo implica

    int_t^infinito(s-t)Phi(s)ds
       =int_0^infinito A0(t+y)dy<=A0(t)/V'(t).

Por la definición de K y positividad de J,

    K(t)<a int_t^infinito(s-t)Phi(s)ds,
    J(t)>t A0(t).

Así

    0<rho(t)<a/[tV'(t)] ->0.                       (K-TAIL)

rho' es continua y nunca cero, por lo que tiene signo constante. La positividad y el límite0 excluyen el signo positivo. Se concluye

    (K/J)'(t)<0 para TODO t>0.                     (K-RATIO)

Esto es compatible con100: eta=-K'/J es otro observable y no es monótono.

## 5. Cuatro densidades pares controladas por089

089 prueba que el sistema impar

    [tPhi,-Phi',(tPhi)'',-Phi''']

es Chebyshev extendido de dimensión4 en (0,infinito): toda combinación no trivial tiene a lo sumo tres raíces contando multiplicidades. Véase el orden [1,B,A,C] y sus cuatro Wronskianos iniciales positivos en POWER_THETA_DENSITY_TRANSPORT_089, sección2. Multiplicar por tPhi>0 conserva los conteos.

Considérese ahora el sistema PAR

    [J,Phi,J'',Phi''].                             (EVEN4)

Su derivada es

    [-tPhi,Phi',-(tPhi)'',Phi'''],

que difiere del sistema impar anterior sólo por factores -1 en las columnas. Una combinación con coeficientes no todos nulos no puede tener derivada idénticamente nula, por la independencia del sistema impar. Tampoco puede ser ella idénticamente nula.

Si tal combinación par tuviese cuatro raíces positivas contando multiplicidades, el lema de un extremo, usando su límite0 en infinito, forzaría al menos cuatro raíces positivas de su derivada. Contradice089. Por tanto toda combinación no trivial de EVEN4 tiene a lo sumo tres raíces positivas contando multiplicidades. No se afirma aquí un signo de determinante innecesario para el argumento.

## 6. Cociente Psi_p/D_p para TODOS los pivotes

Fijar p,r>0 y definir F_r=Psi_p-rD_p. Usando D-EQ y PSI-EQ,

    F_r''=(1+rp)J-rcPhi-(beta+rp^2)D_p.

Aplicar Lp y conservar todas las contribuciones da exactamente

    Lp(F_r'')
      =(1+rp)J''+(p beta-p^2)J-rcPhi''-beta cPhi. (FORCING4)

El coeficiente de J'' es 1+rp>0. Por la independencia de EVEN4, FORCING4 no es idénticamente nula y tiene a lo sumo tres raíces positivas contando multiplicidades. En particular F_r y F_r'' tampoco son idénticamente nulas.

Si F_r tuviese dos raíces positivas contando multiplicidades, GAIN forzaría al menos cuatro de Lp(F_r''), contradicción. Luego F_r tiene a lo sumo una raíz positiva simple.

Definir rho_p=Psi_p/D_p>0. Si rho_p'(t0)=0 en un t0>0, tomar r=rho_p(t0) daría F_r(t0)=F_r'(t0)=0, una raíz doble prohibida. Así rho_p' nunca se anula.

Para determinar el signo fijar p y elegir t suficientemente grande para que tau(t)<=c/(2p). Como tau decrece, en toda la cola s>=t se cumple

    cPhi(s)-pJ(s)>=cPhi(s)/2.

La representación anticausal de075 y sinh(px)/p>=x para x>=0 dan

    D_p(t)=(1/p)int_t^infinito sinh[p(s-t)]
                       [cPhi(s)-pJ(s)]ds
           >=(c/2)I(t),
    I(t)=int_t^infinito(s-t)Phi(s)ds>0.

Por otro lado, usando PSI-EQ y sus bordes,

    Psi_p(t)=int_t^infinito(s-t)[J(s)-beta D_p(s)]ds
             <=int_t^infinito(s-t)J(s)ds
             <=tau(t)I(t).

Así, para cada p fijo,

    0<rho_p(t)<=2tau(t)/c ->0.                     (PAIR-TAIL)

La continuidad y no anulación de rho_p', junto con positividad y límite0, fuerzan el signo negativo. Se concluye

    (Psi_p/D_p)'(t)<0 para TODOS p,t>0.             (PAIR-RATIO)

No se ha tomado un límite en p, intercambiado transformadas ni supuesto una inversión de positividad total. La demostración vale directamente para cada p>0.

## 7. Alcance y conservación todavía pendiente

K-RATIO y PAIR-RATIO son propiedades temporales estrictas de las densidades reales positivas ya construidas; su prueba usa el valle real077 y la cuarta comparación de densidades089. No son una consecuencia de la sola positividad de dos transformadas.

La propiedad PAIR-RATIO controla la pareja obtenida después del primer paso regularizado. El corolario§8 ya construye el denominador positivo de la nueva reducción. Todavía falta el numerador positivo de otra pareja, su monotonía y las comparaciones de cuatro densidades necesarias para repetir el conteo. No se afirma tal cierre, ni que la monotonía por sí sola pague matrices de todos los órdenes.099 permanece vigente; no se obtiene aquí una nueva cobertura W/T, cinco generadores arbitrarios ni el signo global.

Este resultado requiere sólo deducciones analíticas de fuentes ya auditadas. No se ejecutó una cuadratura, campaña o nuevo certificado y no se modificó ningún paper. Las entradas de los tres índices fueron actualizadas tras la auditoría independiente aprobada.

## 8. Corolario: denominador positivo del siguiente paso y obligación exacta restante

Estado de este corolario añadido: **PROVED analítico; auditorías independientes de la ampliación aprobadas.** La coordinación previa con mapa se realizó antes de editar. La búsqueda adicional de `dA-qB`, `d A-q B`, sus variantes con signo menos tipográfico y `ZB/ZA` en los tres índices y el corpus POWER no encontró esta aplicación; sólo102 contiene la pareja nueva. El mecanismo Green con un cruce y balance es el ya probado075, que aquí se aplica a OTRA pareja gracias a PAIR-RATIO. No se presenta el mecanismo abstracto075 como nuevo.

Fijar p>0 y, sólo en esta sección, escribir

    A(t)=D_p(t), B(t)=Psi_p(t), rho(t)=B(t)/A(t),
    ZA(z)=int_R A(t)exp(zt)dt, ZB(z)=int_R B(t)exp(zt)dt,
    F(z)=z ZB(z)/ZA(z)=G_p(z)/c,
    aF=F'(0)=ZB(0)/ZA(0)>0.

Ambas densidades son pares, positivas y superexponenciales; rho'<0 en t>0, rho(infinito)=0. Para z>0, ZB/ZA es el promedio de rho bajo la probabilidad de densidad A(t)cosh(zt) en t>=0. Derivar este promedio da exactamente

    (ZB/ZA)'(z)=Cov_z[rho(T),T tanh(zT)]<0.

La estricta negatividad se demuestra con dos copias independientes: rho decrece estrictamente y t tanh(zt) crece estrictamente; el producto de sus diferencias tiene signo negativo fuera de la diagonal, que tiene probabilidad cero. Los momentos y las derivaciones están pagados por las supercolas. En particular, para cualquier q>0 y d=F(q)>0,

    0<d/q=ZB(q)/ZA(q)<aF,
    q aF-d>0.                                     (F-GAP)

También 0<d/q<rho(0): es un promedio estricto de rho bajo una densidad positiva en toda la semirrecta. Como rho es continua, estrictamente decreciente y tiende a0, existe un único b>0 donde rho(b)=d/q. Por tanto el peso par

    h(t)=d A(t)-q B(t)=q A(t)[d/q-rho(t)]

tiene un único cruce negativo/positivo en la semirrecta. Por la definición de d,

    int_0^infinito cosh(qt)h(t)dt=0.               (BALANCE2)

Definir la nueva densidad par

    E(t)=(1/q)int_|t|^infinito sinh[q(s-|t|)]h(s)ds.

Para t>=0, el peso

    w_t(s)=sinh[q(s-t)]1_(s>=t)/cosh(qs)

es continuo y no decreciente, y es estrictamente creciente en s>t, con derivada q cosh(qt)/cosh(qs)^2. Al multiplicar la medida firmada cosh(qs)h(s)ds por w_t(s)-w_t(b), el integrando es no negativo en ambos lados del único cruce y estrictamente positivo en una cola. BALANCE2 elimina el término constante, exactamente como en075. Así

    E(t)>0 para TODO t real.                      (NEXT-DENSITY)

La diferenciación bajo la integral y BALANCE2 dan

    E''-q^2E=d A-qB, E'(0)=0.

La extensión par es suave, sin delta en0, y E y sus derivadas decaen superexponencialmente. Integrar por partes en toda la recta da la identidad entera

    ZE(z)=[d ZA(z)-q ZB(z)]/(z^2-q^2),
    ZE(0)=[q ZB(0)-d ZA(0)]/q^2>0.                (NEXT-TRANSFORM)

Los valores en z=+-q son removibles por esta identidad. En particular ZE(z)>0 en todo z real. Para el denominador del siguiente Schur,

    z d-q F(z)=z(z^2-q^2)ZE(z)/ZA(z).              (NEXT-DENOM)

No se ha afirmado que E sea una derivada logarítmica ni que la positividad de ZE pruebe el signo del siguiente resto.

Para precisar qué falta, el transformado de Schur de F anclado en q es

    F1(z)=d[zF(z)-qd]/[zd-qF(z)]
         =(d/z)[ZB(z)/ZE(z)-q].

La segunda igualdad usa z^2 ZB-q d ZA=(z^2-q^2)(ZB-q ZE). Su residuo en0 es positivo y exactamente

    r_q=q d^2/(q aF-d)
       =d[ZB(0)/ZE(0)-q]>0.                       (NEXT-RESIDUE)

Al quitar ese polo queda

    R_next(z)=F1(z)-r_q/z
      =(d/z)[ZB(z)/ZE(z)-gamma],
    gamma=ZB(0)/ZE(0)>0.                          (NEXT-REST)

La NUEVA obligación de cruce es la del peso par

    U(t)=B(t)-gamma E(t), int_R U=0.

Si se probase un único cruce negativo/positivo de U, el mismo argumento de cola construiría una densidad positiva Xi con Xi''=U y bordes pares, y entonces R_next(z)=d z ZXi(z)/ZE(z). Ese cruce NO se ha probado aquí. La monotonía ya establecida de B/A no se sustituye por la monotonía todavía desconocida de E/B ni por otra comparación no demostrada.

Finalmente, para conservar la normalización original G_p=cF, si e=G_p(q)=cd, el forzante del denominador es eA-qcB=c h y su densidad positiva es cE. El transformado de Schur original es G1=cF1, su residuo es c r_q y su resto regularizado es c R_next. Todos estos factores son positivos. El argumento de Green de este corolario prueba el siguiente denominador y su residuo, conservando la obligación explícita sobre U. Por sí SOLO no prueba el signo del nuevo resto. El complemento siguiente sí prueba ese signo usando el input ADICIONAL099; no prueba conservación indefinida, nueva cobertura W/T ni todos los órdenes.


### Complemento con099: signo del resto transformado, incluido el punto removible

Estado: **PROVED usando099 además de§8.** No se confunde el signo de una transformada real con una densidad inversa positiva.

Para F=G_p/c,099 prueba paresPD y concavidad estricta en x>0 de los dos datos

    R_F(x)=sqrt(x)/F(sqrt(x)), S_F(x)=sqrt(x)F(sqrt(x)).

F=zZB/ZA es impar analítica en0 y aF=F'(0)=ZB0/ZA0>0. Por tanto R_F y S_F se extienden analíticamente hasta0, con R_F0=1/aF>0,S_F0=0. Sus concavidades estrictas se extienden al intervalo cerrado desde0. Para X,Y>0, las diferencias divididas R_F[0,X,Y],S_F[0,X,Y] son estrictamente negativas. Esto incluye Y=X, porque

    R_F[0,X,X]=[R_F'(X)−(R_F(X)−R_F(0))/X]/X<0,

al ser el promedio de R_F' en[0,X] mayor que R_F'(X); análogamente para S_F. No se deduce una desigualdad estricta de sólo un límite no negativo.

La identidadDET3 de082 extendida por analiticidad al nodo0 da, para q,z>0 distintos,

    det K_F(0,q,z)
      =q²z²(z−q)² R_F[0,q²,z²]S_F[0,q²,z²]
         /[R_F(0)R_F(q²)R_F(z²)]>0.

Además K_F00=aF y el menor(0,q) es (d/q)(aF−d/q)>0 porF-GAP. Así ese bloque esPD. Poner delta=aF−d/q>0 y

    ell(z)=[zd−qF(z)]/[d(z+q)].

La doble identidadSchur ya utilizada099, ahora para F con pivotesq y0, da

    det K_F(0,q,z)=(d/q)delta·ell(z)²·R_next(z)/z.

ell(z) es real no nulo si z!=q, porque F/z decrece estrictamente; por tanto R_next(z)>0 para esos z. En el punto removible,

    ell'(q)=[d−qF'(q)]/(2dq)>0,

pues la desigualdad DIFERENCIAL estricta (ZB/ZA)'(q)<0 de la covarianza implica d−qF'(q)>0.

La fórmulaDET3 tiene término principal (z−q)² con coeficiente

    q^4 R_F[0,q²,q²]S_F[0,q²,q²]
        /[R_F(0)R_F(q²)²]>0.

Dividir por la expansión ell(z)²=ell'(q)²(z−q)²+O((z−q)³) demuestra también R_next(q)>0. F1 tiene un removible simple allí porque d−qF'(q)>0; el resto es analítico. Queda probado

    R_next(z)>0 para TODOS p,q,z>0,

y el resto en la normalización original es cR_next>0.

El cruce de U=B−gammaE y la existencia de una densidadXi positiva SIGUEN OPEN. La positividad real anterior no paga una representación positiva inversa, una monotonía de la nueva pareja ni los cruces de su kernel. Tampoco prueba nuevos generadores W: el nodo0 usado es auxiliar y corresponde al exponente original1/2, fuera del portador admisible. No se declara conservación de todos los órdenes.
