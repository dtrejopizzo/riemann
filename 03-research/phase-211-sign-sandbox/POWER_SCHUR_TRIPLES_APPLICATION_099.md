# POWER_SCHUR_TRIPLES_APPLICATION_099 — Triples del resto y cinco nodos anclados

Estado: **PROVED usando el constructor099 FULL PASS auditado; reproducción independiente root8310 exit0/FULL PASS2048 y hash coincidente.** Se explicita la aplicación exacta del dato global T_h, sin convertir el nodo auxiliar0 en un test admisible. Papers intactos.

## 1. Entradas y ambas curvaturas

099 certifica T_h>0 en el compacto de inclinación0<u<=512;097 lo prueba para u>=512 y098 añade el valor positivo del origen. La cadena completa da T_h(x)>0 para todo x>0.089 aporta T_R>0 global y086R''<0. Todos los inputs son de la Phi real, no una herencia abstracta refutada090.

Usar a=M'(0)>0, g(x)=aR(x)−1=xb(x), h=1/b.090 ya prueba h'>0, g'>0, T_g=a²T_R>0 y todos los pares distintos delkernelG_p definidos positivos.

Para P=p² y x=z², las identidades exactas de090 son

    R_G(x)=z/G_p(z)=(1/a){(x−P)/[h(x)−h(P)]−Pb(P)},
    S_G(x)=zG_p(z)=a{(x−P)/[g(x)−g(P)]−h(P)}.

El lema de secante recíproca con ancla INTERIOR aplica ahora a f=h y a f=g: ambas derivadas primeras son positivas y ambos T_f estrictamente positivos en toda la semirrecta. Por tanto R_G''<0 y S_G''<0 paraTODOSp,x>0. El puntox=P es removible y el lema da allí H_P''(P)=−T_f(P)/(6f'(P)³)<0. No se omite el ancla.

082, con paresPD y ambas concavidades estrictas, prueba que TODOS los triples de nodos positivos distintos delkernel K_Gp(z,w)=[G_p(z)+G_p(w)]/(z+w) son PD, paraTODOp>0. Nodos repetidos se agrupan. No se requiere G_p creciente;081 sigue válido.

## 2. Congruencia exacta con dos pivotes

Extender analíticamente K_M(u,v)=[M(u)+M(v)]/(u+v) al nodo0:

    K_M(0,0)=a, K_M(0,z)=M(z)/z.

Fijar p>0,c=M(p)>0,delta=a−c/p>0 y definir para z>0,z!=p

    d_p(z)=[zc−pM(z)]/[c(z+p)],
    F1(z)=c[zM(z)−pc]/[zc−pM(z)],
    r_p=c²/delta=pc²/(pa−c)>0.

Las fórmulas075–077 dan F1(z)=r_p/z+G_p(z). M(z)/z estrictamente decreciente implica que d_p(z) tiene signo z−p: es REAL no nulo, pero no siempre positivo. La congruencia sólo necesita ser real invertible.

El complemento deSchur de la diagonalK_M(p,p)=c/p satisface, por álgebra exacta,

    S00=delta,
    S0z=−c d_p(z)/z,
    Suv=d_p(u)d_p(v)[F1(u)+F1(v)]/(u+v).

Quitar además la diagonalS00 produce

    Suv−S0u S0v/delta
       =d_p(u)d_p(v){K_F1(u,v)−r_p/(uv)}
       =d_p(u)d_p(v)K_Gp(u,v).

No se eliminó un término firmado arbitrariamente: r_p/(uv) es exactamente el rango1 pagado por el segundo pivote. Las dos diagonales pivotantesc/p ydelta son positivas.

## 3. Alcance de los cinco nodos

Para p,z1,z2,z3 positivos distintos, el bloque ORIGINAL de nodos{0,p,z1,z2,z3} esPD: sus dos complementos anteriores dejan una congruencia real invertible deltripleG_pPD. Repetidos producen la redundancia habitual y PSD.

El nodo0 corresponde al exponente original1/2 y está FUERA del portador W de exponentes>1. Por tanto esto NO prueba cinco generadores admisibles arbitrarios, ni permite sustituir0 por un nodo positivo libre sin otra prueba. Los cuatro nodos positivos de ese bloque ya estaban cubiertos en su rango admisible por085. El resultado nuevo es control estricto de los triples delresto y de una matriz auxiliar anclada, no nueva coberturaW/T.

No se afirma que T de los datos recíprocos delresto se preserve ni que pueda repetirse el argumento a todos los órdenes. El siguiente nivel requiere un input nuevo y el signo global sigueOPEN. La reproducción independiente root8310 del certificado099 terminó exit0/FULL PASS2048 con hash coincidente.
