# POWER_THETA_REMAINDER_077 — Criterio de un valle para el resto Schur real

Estado: **PROVED/APROBADO para la Phi real** por la implicación analítica y las verificaciones locales OUTER/COMPACT077, integradas en POWER_THETA_REMAINDER_AUDIT_077.md. Constructor compacto1589 exit0/PASS; reproducción independiente root36038 terminada exit0/FULL PASS, con hash coincidente. No se afirma positividad del kernel del resto ni de tres generadores. Papers intactos.

## 1. Antecedentes y diferencia

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid maestro R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos THETA_TWO_COPY073, CONTACT_OSCILLATION065, THETA_SCHUR_DENSITY075 y la consulta076 de STATE075.073 prueba una comparación de pares y075 construye Phi_u positiva, pero ninguna de esas positividades ordena Z/H_u.076 identificó el defecto de masa cero y un Wronskiano suficiente aún sin prueba.

El cambio aquí es proponer una hipótesis INDEPENDIENTE del parámetro Schur u, para la densidad original, y demostrar que implica el signo real del resto. No se supone que el forzante tenga un solo cruce: en general tiene DOS. Se conservan sus dos momentos nulos para obtener el signo de Green por interpolación convexa, y se usa sólo el conteo de ceros por Rolle de065, sin una propiedad de positividad total de otros kernels. La sección final da una condición local suficiente para la hipótesis; su verificación real queda separada.

## 2. Datos ya probados y nueva hipótesis precisa

Conservar Phi,Z,M,Phi_u,H_u de075. Para u>0, poner

    c=M(u), a=M'(0), beta=u²a/(ua-c),
    J(x)=int_|x|^infinito y Phi(y)dy,
    tau(x)=J(x)/Phi(x),
    F_u(x)=J(x)-beta Phi_u(x).

075/076 prueban c>0, ua-c>0, Phi_u>0, tau'(x)<0 para x>0 y

    int_R F_u=0,
    Phi_u''-u²Phi_u=cPhi-uJ.

Todas las funciones y derivadas pertinentes decaen más rápido que cualquier exponencial. V=-logPhi es par y suave, con V'>0,V''>0,V'''>0 para x>0 y V'(x)/x->infinito. Estos son los datos específicos usados abajo.

La nueva hipótesis es

    R(x)=[V'(x)+xV''(x)]/[-tau'(x)]
         estrictamente creciente para x>0,
    R(x)->infinito cuando x->infinito.                  (R-HYP)

075 y073 no prueban por sí solos R-HYP. Las verificaciones nuevas y separadas POWER_THETA_RATIO_COMPACT_077 y POWER_THETA_RATIO_OUTER_077 descargan esa hipótesis para la Phi real; abajo se conserva su papel explícito en la demostración de la implicación.

**Conclusión condicional.** Si R-HYP vale para la Phi real, para TODO u>0 la función F_u tiene exactamente UN cero positivo SIMPLE, con signo negativo antes y positivo después. En consecuencia, para TODOS u,z>0,

    T_u(z)>0, G_u(z)>0,                                (REAL-REMAINDER)

con T_u,G_u definidos en076/075. Es un enunciado real; no se extiende automáticamente a una desigualdad de kernels.

## 3. Forzante exacto y dos momentos nulos

Escriba lambda=u²c/(ua-c)>0. Puesto que J'=-xPhi y J''=(xV'-1)Phi, la ecuación de075 da

    f_u:=(D_x²-u²)F_u=Phi(x) B_lambda(x),
    B_lambda(x)=xV'(x)-1+lambda[tau(x)-a].              (FORCING)

Aquí beta c=a lambda y beta u-u²=lambda. Se conservan ambos términos; no se asigna un signo individual al forzante.

Los bordes F_u'(0)=0 y F_u,F_u' superexponencialmente pequeños en infinito dan

    int_0^infinito f_u(x)dx=0,
    int_0^infinito cosh(ux)f_u(x)dx=0.                 (TWO-MOMENTS)

Para el primero, integrar la ecuación y usar int F_u=0 y paridad. Para el segundo, integrar por partes dos veces: la expresión de borde es cosh(ux)F_u'(x)-u sinh(ux)F_u(x), nula en ambos extremos. No hay delta en0, por el resultado075.

## 4. Un valle fuerza el patrón +,-,+ del forzante

Como tau'=V'tau-x y R-HYP,

    B_lambda'(x)=(-tau'(x))[R(x)-lambda].

El factor -tau' es positivo. Por tanto B_lambda primero decrece y después crece, o sólo crece si lambda está por debajo del límite inicial de R. No puede tener más de dos raíces positivas. Además B_lambda(x)->infinito, pues xV'(x)->infinito y tau>=0.

TWO-MOMENTS obliga a al menos DOS cambios de signo en la semirrecta. En efecto, sin cambios contradice el primer momento. Con un único cruce b, el producto[cosh(ux)-cosh(ub)]f_u(x) tendría un signo constante estricto en ambos lados de b; su integral no podría ser cero, contradiciendo los dos momentos. El forzante no es idénticamente nulo porque B_lambda' no puede anularse en todo un intervalo bajo R-HYP.

Por el valle y la cola positiva existen exactamente dos raíces0<b1<b2 y

    f_u>0 en[0,b1), f_u<0 en(b1,b2), f_u>0 en(b2,infinito).

Ambas raíces son simples: están en lados distintos del único mínimo, donde R-lambda no se anula. En particular f_u(0)>0. No se supuso un único cruce del forzante.

## 5. Interpolación convexa: signo de F_u en el origen

Ponga v=cosh(ux), vi=cosh(ubi)>1 y

    H(v)=v-sqrt(v²-1), v>=1.

Se tiene H(cosh(ux))=exp(-ux). Para v>1,

    H''(v)=(v²-1)^(-3/2)>0.

Sea ell(v) la recta que interpola H en v1,v2. La convexidad estricta da H-ell>0 fuera de[v1,v2] y H-ell<0 dentro. El patrón del forzante prueba

    int_0^infinito exp(-ux) f_u(x)dx
      =int_0^infinito [H(cosh(ux))-ell(cosh(ux))]f_u(x)dx>0.

La parte afín de ell se anula por TWO-MOMENTS. Aunque H' sea singular en v=1, no se la integra ni deriva allí; H es continua en ese extremo y vi>1. Todas las integrales son absolutamente convergentes.

El Green del operador D²-u² con los bordes pares y decaimiento lleva signo NEGATIVO:

    F_u(x)=-(1/(2u))int_0^infinito
       [exp(-u|x-y|)+exp(-u(x+y))]f_u(y)dy.

En particular

    F_u(0)=-(1/u)int_0^infinito exp(-uy)f_u(y)dy<0.      (ORIGIN)

## 6. Cola positiva y número exacto de ceros del defecto

La solución superexponencial también tiene la representación anticausal

    F_u(x)=(1/u)int_x^infinito sinh(u(y-x))f_u(y)dy.

Derivarla dos veces verifica la ecuación y los bordes terminales; la diferencia con F_u resolvería la ecuación homogénea y tendría decaimiento superexponencial, por lo que es cero. Para x>=b2, el integrando es positivo salvo en el extremo, así que F_u(x)>0.

Extienda f_u de forma par a toda la recta. Tiene exactamente cuatro ceros simples, en +-b1,+-b2. En toda la recta,

    -F_u=C_1*f_u,
    C_1(x)=exp(-u|x|)/(2u)=e_+*e_-,
    e_+(x)=exp(-ux)1_(x>=0), e_-(x)=exp(ux)1_(x<=0).

El conteo unilateral por Rolle de065, usado sólo en su dirección superior, muestra que esta convolución no puede aumentar el número de ceros CONTADOS CON MULTIPLICIDAD. Para precisar la aplicación: si g=e_+*f, entonces(exp(ux)g)'=exp(ux)f y exp(ux)g tiende a0 al extremo izquierdo. Rolle cuenta un cero entre cada par, las multiplicidades reducidas en los ceros múltiples y un extremo interior antes del primero, como en065. Para e_- se refleja el argumento y se usa el borde derecho. Los datos aquí son suaves y reales analíticos; no hay intervalos nulos ni ceros de orden infinito. Las colas garantizan los bordes, aunque no sean polinomios por exponencial. La anulación de momentos no es necesaria para esta cota superior de ceros.

Por tanto F_u tiene a lo sumo cuatro ceros reales contados con multiplicidad. Es par, F_u(0)<0 y es positiva en la cola. Debe tener un número impar de cambios en la semirrecta positiva. Tres cambios, una tangencia adicional o un único cruce de multiplicidad mayor que1 requerirían al menos seis ceros globales contados con multiplicidad. Se concluye que tiene exactamente UN cero positivo SIMPLE, con signos negativo/positivo. Ésta es una aplicación del mecanismo065 al forzante concreto, no una afirmación genérica de signo del resto.

## 7. Transformada positiva y resto Schur real

Como int_0^infinito F_u=0 y F_u tiene un cruce negativo/positivo en b, para cualquier z>0,

    int_R F_u(x)exp(zx)dx
      =2int_0^infinito [cosh(zx)-cosh(zb)]F_u(x)dx>0.

La identidad de076 es

    t_u=(u/c)F_u,
    T_u(z)=Z(z)-[Z(0)/H_u(0)+z²/c]H_u(z)
          =(u/c)int_R F_u(x)exp(zx)dx,
    G_u(z)=c²T_u(z)/(uzH_u(z)).

075 prueba H_u(z)>0 para z real. Todos los factores son positivos cuando u,z>0, así que se obtiene REAL-REMAINDER.

Esto no identifica G_u con una derivada logarítmica, no prueba la positividad de su kernel de dos nodos y no afirma positividad de tres generadores de la forma original. El contraejemplo genérico074 sigue vigente: no satisface necesariamente la hipótesis adicional R-HYP.

## 8. Criterio local suficiente y aplicación verificada para Phi real

Para x>0, escriba sólo en esta sección

    p=V'(x), q=V''(x), r=V'''(x),
    D=xq-p>0,
    C=p³+xp²q-pq-xpr+xq²,
    L=D/C, w=1+xq/p.

Una condición suficiente concreta para R-HYP es

    C>0,
    L estrictamente decreciente y L(x)->0,
    w(x)Phi(x)->0 cuando x->infinito.                  (LOCAL-HYP)

El último es el borde que debe conservarse al usar la cola theta; no se lo omite en una integración por partes.

Prueba de la implicación: integrar J=int_x^infinito (y/p(y))p(y)Phi(y)dy y usar Phi'=-pPhi da

    J(x)=xPhi(x)/p(x)-int_x^infinito [D(y)/p(y)²]Phi(y)dy.

Además una derivación directa verifica

    -(wPhi)'=C Phi/p².

Por tanto

    R(x)^(-1)
      =[int_x^infinito (D/p²)Phi]/[w(x)Phi(x)]
      =[int_x^infinito L(y)(C/p²)Phi(y)dy]
                    /[int_x^infinito (C/p²)Phi(y)dy].    (TAIL-AVERAGE)

El denominador es positivo por LOCAL-HYP y el borde declarado. Es un promedio de cola de L bajo una densidad positiva. Si L decrece estrictamente, dicho promedio decrece estrictamente al aumentar el extremo inferior: se eliminan valores mayores que los que permanecen. Además0<R^(-1)<L(x)->0. Esto prueba R creciente e infinita.

La verificación separada de C>0 y L decreciente para Phi REAL quedó completada en POWER_THETA_RATIO_COMPACT_077 y POWER_THETA_RATIO_OUTER_077, con los bordes declarados yL->0. El certificado compacto1589 terminóexit0/PASS y fue auditado matemáticamente y a nivel de código; root36038 reprodujo independientemente el certificado y terminó exit0/FULL PASS, con el mismo hash. La prueba exterior fue leída y su verificadorFraction reproducido por root con tresPASS. Así queda descargadaLOCAL-HYP y REAL-REMAINDER es **PROVED** paraTODOSu,z>0. TAIL-AVERAGE por sí sola no era el signo: lo aportan estas desigualdades específicas nuevas. No se deduce positividad del kernel de dos nodos del resto ni de tres generadores.

## 9. Corolario anclado en el nodo auxiliar0

Definir N(u)=M(u)/u y B(u)=[a/N(u)−1]/u², a=M′(0).073 da N′<0 yB>0. Por tanto

    (u²B)′=−aN′/N²>0, es decir 2B+uB′>0.

SustituirM(u)=au/[1+u²B(u)] en la fórmulaSchur075 produce, para el pivotep>0,

    G_p(z)=az[B(p)−B(z)]/[B(p)(z²B(z)−p²B(p))].

El denominador sólo se anula en z=p, pues u²B crece. El valor removible es

    G_p(p)=−aB′(p)/[B(p)(2B(p)+pB′(p))]>0.

REAL-REMAINDER implica B′<0. De aquí−2<uB′/B<0; paraF(u)=uB(u) se obtiene−1<uF′/F<1. El criterio exacto deCONE001 prueba que el kernelK_F(u,v)=[F(u)+F(v)]/(u+v) tiene todos sus pares distintos positivos definidos.

La extensión auxiliar del kernel original tiene K_M(0,0)=a yK_M(0,u)=N(u). Su complemento deSchur es exactamente

    K_M(u,v)−N(u)N(v)/a
      =[uN(u)vN(v)/a]·[uB(u)+vB(v)]/(u+v).

Es una congruencia positiva del kernelK_F. Por tanto la matriz anclada en{0,u,v} es definida positiva para u,v>0 distintos. El nodo0 corresponde al exponente originala_orig=1/2, fuera de la clase de potencias convergentesa_orig>1; NO es un tercer testW admisible. Este corolario no prueba tres nodos positivos arbitrarios ni positividad del kernel deG.
