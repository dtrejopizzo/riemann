# POWER_THETA_RATIO_OUTER_077 — Dos signos locales para la Phi real en x>=1

Estado: **PROVED/APROBADO por revisión independiente de root**, prueba leída y verificadorFraction con tresPASS; también comprobación simbólica independiente. Sólo tramo exterior de las hipótesis077. Papers y phase103 intactos.

## 1. Objeto y antecedentes

Consultados las reglas del proyecto, índice/grid/crucigrama y los antecedentes073–076. El tramo exterior10343 controla sólo la tercera logderivada. Aquí se comprueban dos combinaciones locales distintas, con derivadas hasta orden4, que el criterio de cociente de colas077 necesita. No se reetiqueta la positividad de una transformada como signo de un cociente ni se afirma que estas hipótesis estén verificadas cerca del origen.

Sea V=−logPhi y, para x>0,

    p=V′, q=V″, r=V‴, s=V⁗,
    C=p³+xp²q−pq−xpr+xq²,
    C′=4p²q+2xpq²+xp²r−2pr+xqr−xps,
    J=(xq−p)C′−xrC.

Se prueba para TODO x>=1:

    C>3(1+x)y³>0, J>31x²y⁴>0, y=pi exp(2x)>21.       (OUTER)

Por tanto L=(xq−p)/C es positiva y estrictamente decreciente allí, porque L′=−J/C². También L tiende a0. La positividad xq−p>0 proviene de073.

## 2. Primer modo: certificado en una región más grande

Poner b=2y−3. Las cuatro derivadas del potencial del primer modo son

    p0=2y−9/2−6/b,
    q0=4y+24y/b²,
    r0=8y−48y(2y+3)/b³,
    s0=16y+96y(4y²+24y+9)/b⁴.

Definir C0,J0 con esas mismas fórmulas. Se comprueban las identidades racionales y signos

    C0>4(1+x)y³,
    J0>32x²y⁴,                         TODOS x>=1,y>=21. (MODE)

No se necesita usar la relación entrex ey para este paso: es un fortalecimiento válido sobre TODO el cuadrante. La evidencia exacta está en tools/power_theta_ratio_outer_077_verify.py, que usa sólo Fraction y operaciones de polinomios de dos variables.

El script sustituye

    p0=P/(2b), P=8y²−30y+15,
    q0=Q/b², Q=16y³−48y²+60y,
    r0=R/b³, R=8yb³−48y(2y+3),
    s0=S/b⁴, S=16yb⁴+96y(4y²+24y+9).

ParaC usa el denominador positivo8b⁴ y paraJ8b⁷. Tras restar los márgenes deMODE y cambiar x=1+X,y=21+Y, TODOS los coeficientes de ambos numeradores son estrictamente positivos:16 y36 términos no nulos, respectivamente, incluidos sus términos constantes. Las fórmulas deJ se expanden exactamente como

    J=−4p³q+2p²r
       +x(−2p³r+2p²q²+p²s−2pqr)
       +x²(2pq³−pqs+pr²).

Esto certifica MODE para el cuadrante entero, sin muestreo ni elección por autovalores. Si se cancelan factores comunes se recuperan12 y27 coeficientes positivos con denominadores8b² yb⁴, pero esas cancelaciones no son necesarias para el certificado.

## 3. Cola theta completa hasta la cuarta derivada

Escriba Phi=f1(1+Rtheta), y para m>=2 use a=m²−1>=3,z=ay. El bound auditado10343 da

    0<r_m=f_m/f1<=(32/9)a² exp(−ay).

Las tres primeras logderivadas tienen módulos<3z,5z,10z. Para la cuarta, escribir

    B(y)=48y(2y+3)/(2y−3)³,
    DB(y)=−96y(4y²+24y+9)/(2y−3)⁴.

Para y>=21, |DB(y)|<3: basta4+24/y+9/y²<6 y2−3/y>9/5. Por ello |D⁴logr_m|<=16z+6<20z. La fórmula de Bell para la cuarta derivada da

    |D⁴r_m|/r_m
      <=81z⁴+270z³+195z²+20z<100z⁴, z>=63.

El mismo100z⁴ majoriza también los órdenes0,1,2,3. Ampliar los a reales de la suma a TODOS los enteros a>=3 resulta en

    |D^ell Rtheta|
      <=(3200/9)y⁴ sum_(a>=3)a⁶ exp(−ay), 0<=ell<=4.

Exp(3)>16 por una suma Taylor positiva hasta grado7. La razón de términos de la última suma es<=(4/3)^6/16^7<1/2. Además y⁴exp(−3y) decrece para y>=21. Así, simultáneamente,

    |D^ell Rtheta|
      < E=(6400/9)3⁶21⁴/2⁸⁴ <10^−12, 0<=ell<=4.     (TAIL)

La suma es completa, no sólo un prefijo de modos. ComoRtheta>=0, los denominadores de las logderivadas son>=1. Las fórmulas de log(1+Rtheta) hasta orden4 tienen módulos acotados por

    epsilon+7epsilon²+12epsilon³+6epsilon⁴<10^−10,
    epsilon=10^−12.

Por tanto cada una de p,q,r,s difiere de su valor de primer modo en menos de eta=10^−10.

## 4. Pago explícito del error local

En y>=21, el primer modo satisface0<p0<2y,0<q0<5y,0<r0<8y y0<s0<17y. En particular, todos los segmentos entre las cuatro derivadas exactas y sus valores de primer modo están dentro de la caja |p|,|q|,|r|,|s|<=20y.

La suma de los módulos de las tres derivadas parciales deC en esa caja es<=2520xy² para x>=1,y>=21. ParaJ expandido arriba, los monomios de grado4 suman coeficiente absoluto por grado40 y los de grado3 suman21. Por ello la suma de módulos de sus cuatro derivadas parciales es<=328400x²y³. El teorema del valor medio multivariable da

    |C−C0|<=2520xy²eta,
    |J−J0|<=328400x²y³eta.

Como2520eta<21 y328400eta<21, los márgenesMODE prueban exactamenteOUTER. Las comparaciones racionales deTAIL, Bell y estas pérdidas se incluyen en el mismo verificador.

## 5. Bordes y alcance

Para x>=1, la relación real y=pi exp(2x) asegura y>21 por pi>3 y exp2>7. El numerador xq−p es positivo por073 y está acotado, por ejemplo, por20(1+x)y. Junto aOUTER esto da

    0<L(x)<=20/(3y²) ->0.

También p>=y yq<=6y allí; por tanto w=1+xq/p<=1+6x. La cola theta implica wPhi->0 y la integrabilidad de bPhi del criterio077. Esos bordes no se deducen sólo de C>0: se comprueban con la cola REAL específica.

El intervalo0<x<1 no está resuelto por este memo. Sin esa verificación y sin el argumento condicional posterior no se declara G positivo, un kernel Schur positivo ni tres generadores. El resultado es exclusivamente la comprobación analítica uniforme de DOS signos locales en el tramo exterior.
