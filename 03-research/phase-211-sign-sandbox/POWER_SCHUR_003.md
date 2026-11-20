# POWER_SCHUR_PRIOR_AUDIT_003 — Antecedentes y primer paso aritmético

Estado: PROVED (álgebra y primer paso real); OPEN (preservación iterada). No modifica papers.

## 1. Restricción de novedad

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX, grid R162_2300_part3/part5, CROSSWORD-TO-D y búsqueda de algoritmo Schur, Cayley, Nevanlinna y recursión en el corpus. Antecedentes concretos:

* 04-papers/36-obstruction-ledger/main.tex:3753–3765: cor:schur-coords y algoritmo escalar Schur–Nevanlinna sobre datos de Pick anidados. El algoritmo general no es nuevo.
* 03-research/phase-61-open-problems/respuestas3.md:110–134: recursión Krein–Langer/Schur para matrices de transferencia ordenadas por primos. Es otro objeto.
* 03-research/phase-104-unconditional-a1-closure/104_16_JORDAN_COCYCLE_ATTACK.md y su README: cociente completado desplazado y jets de Cayley. Otro dato de entrada y otra parametrización.
* 03-research/phase-120-global-polarization/P3_EFFECTIVE_HERGLOTZ_GAMMA_GATE.md:36: Cayley y contractividad de un objeto efectivo.

No se encontró en esas búsquedas el paso exacto para F(z)=L(z+1/2) en los nodos z=31.5+k. La diferencia autorizada es calcular los primeros transformados desde la serie aritmética, demostrar una desigualdad preservada e identificar un falsificador explícito que falle esa desigualdad. No consiste en anunciar el algoritmo conocido ni en usarlo como prueba sin signo.

## 2. Primer transformado exacto

Fije u>=31.5, c=F(u)>0, y defina

    b_u(z)=(z-u)/(z+u),
    r(z)=(F(z)-c)/(F(z)+c),
    q(z)=r(z)/b_u(z),
    F_1(z)=c(1+q(z))/(1-q(z)).

Álgebra directa da

    F_1(z)=c [z F(z)-u c]/[z c-u F(z)].

No se supone contractividad para obtener esta fórmula. La desigualdad ya demostrada en POWER_CONE, F'>=0 y F-zF'>0 para z>=31.5, implica 0<=q(z)<1 para todos los reales z>=31.5, z distinto de u. En efecto r y b tienen el mismo signo por F creciente; q<1 es exactamente la desigualdad de cocientes entre u/z y z/u, demostrada para todos los pares de ese intervalo. El valor removible es

    q(u)=uF'(u)/c <1,
    F_1(u)=c[c+uF'(u)]/[c-uF'(u)]>0.

Por tanto F_1 es real estrictamente positiva en todo ese intervalo. Este resultado verifica un primer paso real; no implica positividad del kernel completo de F_1.

## 3. Falsificador racional del mismo paso

Para H(z)=3+cosh z y F=H'/H, tome u=log2,v=2log2. Entonces c=3/17, F(v)=15/41,

    r(v)=22/63, b_u(v)=1/3,
    q(v)=22/21>1,
    F_1(v)=-43c=-129/17<0.

Así el primer paso real distingue una propiedad probada para el dato aritmético del mero supuesto de representación cosh positiva. No prueba todavía preservación de esa propiedad después del paso.

## 4. La siguiente desigualdad concreta y una advertencia

Ponga d=F'(u), e=F''(u). Derivar la fracción removible en u da

    F_1'(u)=c[d(c-ud)+uc e]/(c-ud)^2.

La condición local necesaria para un siguiente paso es

    |u(cd-u d²+uc e)| <= c²-u²d².

Esta desigualdad usa sólo los jets explícitos de L, y puede atacarse con las series absolutamente convergentes de psi y zeta'/zeta en el rango a>=32. Aún no se ha demostrado aquí, y la preservación global requeriría el correspondiente control para todos los pares del primer transformado y sus iteraciones.

No exigir F_1'>=0 como invariante: ni siquiera el modelo F(z)=c+(1/2)log(z/u), localmente con c>0, lo conserva, pues d=1/(2u),e=-1/(2u²) dan F_1'(u)<0 cuando c>1/2. El invariante apropiado debe permitir ambas señales de la derivada y controlar |zF_j'/F_j|, o directamente la desigualdad de dos puntos de cada transformado. La positividad real del primer transformado por sí sola no es ese invariante.

## 5. Falso lema: todos los pares positivos no preservan el siguiente paso

Falsificador comunicado por el coordinador y verificado con aritmética racional:

    F(z)=(z²-z+10)/10, 1<=z<=3.

Se tiene F>0, F'=(2z-1)/10>0 y

    d/dz[F(z)/z]=1/10-1/z²<0

sobre todo el intervalo. Por el criterio exacto de dos puntos, TODOS los bloques 2x2 del kernel [F(x)+F(y)]/(x+y) son positivos definidos para x distinto de y en [1,3]. Sin embargo para los nodos 1,2,3,

    K=[[1,11/15,13/20],[11/15,3/5,14/25],[13/20,14/25,8/15]],
    det K=-13/270000,
    pivotes LDL=(1,14/225,-13/16800),
    (93,-375,280)K(93,-375,280)^t=-182/3.

El primer transformado, con pivote u=1 y c=1, se simplifica exactamente a

    F_1(z)=(z²+10)/(10-z),
    F_1(2)=7/4, F_1(3)=19/7.

Es positivo en [1,3] y creciente, pero

    F_1(3)/F_1(2)=76/49>3/2,

así pierde la banda de cocientes requerida para el siguiente paso. Incluso el control local de §4 en el pivote inicial pasa: su lado izquierdo es 29/100 y el derecho 99/100. Por tanto verificar únicamente ese jet en el primer pivote tampoco bastaría para controlar los otros nodos.

**Conclusión de alcance exacto:** se refuta la afirmación de preservación del paso Schur basada exclusivamente en F'>=0 y F/z decreciente, aunque ambas propiedades valgan para todos los puntos del intervalo. Esto no refuta el kernel aritmético ni el algoritmo como instrumento constructivo. Obliga a demostrar una propiedad adicional de las series aritméticas y a comprobar su conservación por los transformados. No se afirma NO-GO fuera de esa clase explícita de hipótesis.

## 6. Revisión y estado al registrar

La matriz, determinante, pivotes y vector negativo de §5 fueron recalculados con fracciones racionales exactas; la fórmula de F_1 se verificó por simplificación algebraica. Las demostraciones escalares de §§2–4 no usan ningún signo supuesto del kernel completo. El primer paso real para el dato aritmético permanece PROVED por POWER_CONE; la preservación iterada permanece OPEN, con el falso lema de §5 retirado explícitamente de las posibles justificaciones.

## 7. Añadir concavidad tampoco basta: falsificador continuo por tramos

Dato comunicado por el coordinador y verificado exactamente:

    F(z)=min((2+3z)/5,(14+z)/10), z>=1.

Las dos rectas se cruzan en z=2. La pendiente pasa de 3/5 a 1/10, así F es positiva, creciente y cóncava. En cada rama F(z)/z es decreciente por su intercepto positivo, y es continua en la unión; por tanto decrece en todo [1,infinito). Todos los pares pasan el criterio. Sin embargo F(1)=1,F(2)=8/5,F(3)=17/10 dan det K=-53/270000<0.

Esto refuta, para la clase de funciones continuas por tramos, que agregar concavidad a las dos monotonías garantice el signo de orden tres. No se afirma aquí un falsificador analítico ni se necesita tal afirmación para el alcance declarado. Tampoco se afirma imposibilidad de obtener una desigualdad adicional específica del dato aritmético.
