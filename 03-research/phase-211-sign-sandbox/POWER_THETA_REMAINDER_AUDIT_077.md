# POWER_THETA_REMAINDER_AUDIT_077

Estado: **APROBADO el ensamblaje para la Phi real**, incluida la verificación local completa. El certificado compacto del constructor1589 terminó exit0/PASS y su código y prueba fueron auditados línea por línea. La reproducción independiente de root36038 terminó exit0/FULL PASS, con el mismo hash del verificador. Papers intactos.

Se cotejaron índice/grid/crucigrama y073–076, incluida la advertencia074 sobre hipótesis genéricas. La implicación auditada es G_u(z)>0 parau,z>0 bajoR-HYP; los dos certificados locales detallados abajo descargan ahora esa hipótesis paraPhi real. No se afirma un kernel positivo de dos nodos paraG ni tres generadores de la forma original.

La ecuación del forzante es exacta: beta c=a lambda, beta u−u²=lambda y J″=(xp−1)Phi dan f=Phi[xp−1+lambda(tau−a)]. Tanto el integral def como el de cosh(ux)f se anulan por las condiciones de borde y la masa cero deF. El segundo conserva el borde Neumann0 y los bordes superexponenciales del infinito; no se omite un término de interfaz.

R-HYP hace que la derivada deB tenga a lo sumo un cambio negativo/positivo. La cola deB es positiva e ilimitada. Los dos momentos nulos excluyen0 o1 cambios de signo: la resta de cosh en el único cruce tendría integral de signo estricto. Por tantoB tiene exactamente dos raíces positivas, ambas simples, con patrón+−+ y B(0)>0. No se presupone un forzante de un solo cruce.

H(v)=v−sqrt(v²−1) es estrictamente convexa parav>1. Su secante en los dos nodos cosh(ub_i) deja el signo de error positivo fuera y negativo dentro; multiplicarlo porf da un integral estrictamente positivo. La secante se elimina con los dos momentos. La singularidad deH′ en1 no interviene: sólo se integraH continua. El signo NEGATIVO del Green deD²−u² está correcto y daF(0)<0.

La representación anticausal tiene signo positivo y satisface la misma ecuación. Su diferencia conF es homogénea y superexponencial, luego nula. AsíF es positiva después de la segunda raíz def. La extensión par def tiene cuatro ceros simples; la doble convolución exponencial no aumenta el número de ceros contados con multiplicidad. En este uso sólo se necesita la cota superior de065. Los intermedios pueden tener ceros múltiples, pero la versión general de Rolle con multiplicidades sigue válida: las soluciones son reales analíticas, sin intervalos nulos ni ceros de orden infinito, y los bordes ponderados se conservan. No se usa indebidamente la preservación de momentos polinómicos de065 para otro dato.

Por tantoF tiene a lo sumo cuatro ceros globales contando multiplicidad. Paridad, F(0)<0 y cola positiva fuerzan exactamente un cero positivo simple: un segundo toque o una multiplicidad impar mayor consumirían al menos seis globales. El integral de cosh contraF, restando su valor en ese cruce y usando masa cero, es estrictamente positivo. Los factores deT_u yG_u son los de076 y son positivos parau,z>0.

También se revisó el criterioLOCAL-HYP: J=xPhi/p−integral bPhi, b=(xq−p)/p², y−(wPhi)′=C Phi/p² son correctos. El bordewPhi->0 convierte el denominador en la masa TOTAL de la cola positiva. AsíR^−1 es el promedio deL=D/C; siL decrece estrictamente hacia0, el promedio también decrece y es menor queL(x), dandoR creciente hacia infinito. Ese borde y la integrabilidad no se deducen sólo deC>0: deben verificarse para laPhi real.

## Verificación exterior y compacta

POWER_THETA_RATIO_OUTER_077 resuelve los signos en TODO x>=1 mediante identidades racionales de primer modo y el pago explícito de TODA la cola theta hasta orden4. Root leyó la prueba independientemente, comprobó los numeradores por expansión simbólica y reprodujo el verificadorFraction con tresPASS. Las expansiones sin cancelar denominadores y las canceladas son consistentes. El borde wPhi->0 y L->0 también se verifica allí con la cola theta real, no sólo con signos locales.

Leídos íntegros POWER_THETA_RATIO_COMPACT_077 y tools/power_theta_local_077_verify.py. En el origen se evita dividir por factoresx³/x⁷: la identidadREG conP=p/x,Q=q,R=r/x,D=(Q−P)/x² yE=C/x³ es exacta. V6<0, paridad, a=V2(0)>0,b=V4(0)>0 yb<2a² implicanV5<0,R′<0,D′<0 yP²+PQ−R>0; por elloE>0 yL′<0 para0<x<=1/16. No se necesita que V4 permanezca positiva en todo ese tramo; R>0 ya viene de073.

El código generaQ0..Q8 exactamente y añade a CADA derivada la cola completa desde m=7. El bound A·3⁹m²⁰2^(−4m²) y su razón<1/2 son correctos. Machin, expTaylor128 con once cuadrados y todos los operadores intervalares redondean hacia fuera. La recurrencia de logjets usa derivadas ordinarias y coeficientes binomiales correctos, sin mezclar jets normalizados por factorial. S.lower>0 se comprueba antes de cada división.

El modeloTaylor2 deV6 usaV6/V7 en el centro yV8 en TODO el panel; [0,h²/2] cubre el resto para ambos signos del desplazamiento. En el resto compacto, la construcción binomial de jetsC hasta orden3 requiereV hasta6, disponible. Las identidadesN′=(xq−p)C″−(r+xV4)C yN″=xrC″+(xq−p)C‴−(2V4+xV5)C−(r+xV4)C′ son exactas. Los modelos deC yN cubren todo cada panel; no se deduce el signo de muestras centrales.

La corrida corregida1589 terminó exit0/PASS en1024 paneles de origen y8192 del resto. Las mallas y dominios se conservaron al sustituir la primera evaluación dependiente insuficiente por el modeloTaylor justificado; losFAIL anteriores no se promovieron como signos falsos deV6. SHA256 verificado del script que terminóPASS:

    896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee.

La reproducción independiente root36038 terminó exit0/FULL PASS en el origen y los8192 paneles restantes; el hash coincide con la versión del constructor. Quedan por tanto dos ejecuciones compactas completas y la auditoría matemática y de código, además de la reproducción independiente de la prueba exterior.

## Conclusión actual y límite

COMPACT yOUTER cubren TODO x>0, danC>0,L′<0,L->0 y los bordes requeridos. Queda descargadaR-HYP para la Phi REAL. En consecuencia, para TODO u>0, F_u=J−betaPhi_u tiene exactamente un cero positivo simple, signo negativo antes y positivo después; para TODOS u,z>0 se obtienen T_u(z)>0 yG_u(z)>0.

Es positividad REAL puntual del resto Schur regularizado, no positividad del kernel de dos nodos deG. No prueba tres generadores, todos los órdenes ni el signo global deW, ni una ventana temporal nueva. La siguiente obligación sigue siendo controlar los términos cruzados de ese kernel o una propiedad adicional que los domine.

## Corolario auxiliar anclado

Revisada la adición de insight/root: N=M/u, B=(a/N−1)/u². N′<0 daB>0 y2B+uB′>0. La sustitución algebraica enG es exacta y su valor removible en el propio pivote es−aB′/[B(2B+uB′)]. ComoG_u(u)>0 por el teorema ya probado, B′<0. AsíF=uB satisface|uF′/F|<1, suficiente para TODOS los pares del kernelK_F; no se requiere queF′ tenga signo fijo.

El complemento deSchur del nodo auxiliar0 es[uN(u)vN(v)/a]K_F(u,v), conK_M(0,0)=a yK_M(0,u)=N(u). Todos los factores de la congruencia son positivos. Esto prueba la matriz anclada{0,u,v}, para positivos distintosu,v, sin contradicción con el alcance declarado:0 corresponde al exponente original1/2 y no es un datoW admisible en la clasea>1. No se obtiene tres generadores positivos arbitrarios ni un kernelG positivo.
