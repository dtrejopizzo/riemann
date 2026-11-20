# Modelo hiperbólico: Gram de todos los órdenes mediante un Green positivo

Estado: **PROVED para el modelo indicado**, revisión matemática independiente root/casos/invariante_nuevo. **OPEN** cualquier transferencia a la Phi real. No nueva positividad de W, dimensión admisible ni ventana T del Paper47. Papers intactos.

## 1. Objeto y consulta previa

Para a>0 fijo, sea phi_a(t)=exp(-a cosh(2t)), Z_a(u)=integral_R exp(ut)phi_a(t)dt y M_a=Z_a'/Z_a. Aquí a es un parámetro del modelo, no un exponente de un test del Paper47. Se demuestra que

    [(M_a(u_i)+M_a(u_j))/(u_i+u_j)]_ij es PSD

para cualquier número de parámetros positivos u_i. No se identifica phi_a con la theta real.

Consultados ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; búsquedas dirigidas en el corpus y cotejo independiente de mapa. No se encontró un resultado literal para este modelo en las fuentes consultadas. Los Bessel inversos de POWER019 y las menciones a polinomios Macdonald pertenecen a otros objetos. No se afirma novedad bibliográfica mundial.

La diferencia frente a POWER_GRAM_SLICES_OBSTRUCTION es concreta: el modelo tiene supercolas, y su f(t)=(-log phi_a)'=2a sinh(2t) satisface f(t)/t³→infinito. Por la sección5 de aquella nota, algunas de sus capas NO son PSD. La prueba siguiente firma el kernel completo por una ecuación diferencial en la escala, sin exigir signo de cada capa ni extrapolar el modelo cuártico. Frente a083, aquí se construye el Green positivo que proporciona la representación; no se postula una medida Stieltjes.

## 2. Integral y ecuación diferencial

Para x>=0 y r>=0, definir directamente

    y_x(r)=integral_0^infinito exp(-a exp(r) cosh v) cosh(sqrt(x)v)dv.

El integrando y todas las derivadas necesarias son absolutamente integrables, uniformemente en compactos de x,r. En x=0 se interpretan las derivadas mediante la serie de cosh. Cambiar v=2t y usar paridad da EXACTAMENTE

    Z_a(u)=y_(u²/4)(0).

No hay un factor2 pendiente. Con b=a exp(r), la diferencia entre la segunda derivada en r del factor exp(-b cosh v) y su segunda derivada en v es b² exp(-b cosh v). Dos integraciones por partes en v, con derivadas nulas en0 y superdecaimiento en infinito, dan

    y_x''(r)=[a² exp(2r)+x] y_x(r).                    (ODE)

Además y_x>0. Comparar los integrandos para r+h y r prueba

    y_x(r+h)/y_x(r)
      <=exp[-a exp(r)(exp(h)-1)]<=exp[-a exp(r)h].     (RATIO)

Estas desigualdades son válidas para todo h>=0 y x>=0.

## 3. Bordes al diferenciar el parámetro

Poner z_x=partial_x log y_x. La ecuación diferenciada implica

    (y_x² z_x')'=y_x².

Se necesitan ambos bordes, no sólo el decaimiento de y_x. La esperanza bajo la densidad proporcional al integrando cumple, por integrar la derivada de v por esa densidad,

    1=E[b v sinh v-sqrt(x) v tanh(sqrt(x)v)]
      >=(b-x)E[v²], b=a exp(r).

Se usan v sinh v>=v² y tanh w<=w. Por tanto, cuando b>x,

    0<=z_x(r)=E[v tanh(sqrt(x)v)/(2sqrt(x))]
      <=E[v²]/2<=1/[2(b-x)],

con el valor removible en x=0. Por tanto z_x(infinito)=0. El otro borde y_x² z_x'→0 se obtiene directamente de y_x partial_x y_x'-y_x' partial_x y_x. Para b>=1, exp(-b cosh v)<=exp(-b/2)exp(-cosh v/2). Los factores v², cosh v y cosh(sqrt(x)v) son integrables contra el segundo factor. Así y_x, partial_x y_x son O_x(exp(-b/2)), y sus derivadas en r son O_x(b exp(-b/2)); el Wronskiano paramétrico es O_x(b exp(-b)) y tiende a0. No se deriva una notación O sin control. Así

    z_x'(r)=-y_x(r)^(-2) integral_r^infinito y_x(s)²ds,
    z_x(0)=integral_0^infinito y_x(r)^(-2)
                         integral_r^infinito y_x(s)²ds dr. (LOG-DER)

RATIO domina la última integral por integral_0^infinito (2a exp(r))^(-1)dr=1/(2a). En particular todos estos integrales son finitos.

## 4. Green y traza positiva

Sea H=-D_r²+a² exp(2r) sobre la semirrecta con borde Dirichlet en0. Puede definirse mediante la forma integral de |f'|²+a²exp(2r)|f|². Es positiva y H>=a². Su inverso desplazado R_x=(H+x)^(-1) tiene el Green explícito

    G_x(r,s)=y_x(r)y_x(s) integral_0^min(r,s) y_x(t)^(-2)dt.

En efecto se anula en r=0, decae en infinito, cumple la ecuación homogénea fuera de r=s y su derivada tiene el salto -1 requerido por -D². Esta fórmula también factoriza G_x como un Gram continuo: sus factores son y_x(r)/y_x(t) por 1_(t<=r).

Tonelli y LOG-DER dan

    Tr R_x=integral_0^infinito G_x(r,r)dr
          =partial_x log y_x(0)<=1/(2a).              (TRACE)

La traza se justifica sin un determinante: la factorización Gram anterior es producto de un operador Hilbert–Schmidt con su adjunto, pues la integral de su cuadrado es exactamente LOG-DER. Los mismos resultados se obtienen por Green en intervalos finitos y paso al límite de las integrales positivas.

Por la regla de la cadena,

    M_a(u)/u=(1/2)Tr (H+u²/4)^(-1).                  (REP)

Esta es una representación construida, con H positivo independiente de u.

## 5. Suma de cuadrados para cualquier tamaño

Escribir R_i=(H+u_i²/4)^(-1). La identidad de resolventes, o multiplicar los dos denominadores, prueba

    (u_i R_i+u_j R_j)/(u_i+u_j)
       =(H+u_i u_j/4) R_i R_j.

Tomar trazas y usar REP expresa el kernel como

    K_ij=(1/2)Tr(H R_i R_j)+(u_i u_j/8)Tr(R_i R_j).

Todos los productos necesarios tienen traza finita: H R_i²<=R_i y TRACE controla el lado derecho. Para coeficientes reales c_i, poner A=sum_i c_i R_i y B=sum_i c_i u_i R_i. Entonces

    sum_ij c_i c_j K_ij
        =(1/2)||H^(1/2) A||_HS²+(1/8)||B||_HS²>=0.   (GRAM)

Se puede leer GRAM únicamente como integrales de cuadrados. Si F(r,s)=sum_i c_i G_(u_i²/4)(r,s) y B(r,s)=sum_i c_i u_i G_(u_i²/4)(r,s), el lado derecho es

    (1/2) integral integral [|partial_r F|²+a²exp(2r)|F|²]dr ds
      +(1/8) integral integral |B(r,s)|²dr ds.

Las identidades de energía del Green justifican estas integrales; los bordes son Dirichlet en0 y decaimiento en infinito. Esto prueba simultáneamente todos los tamaños, sin una torre de menores.

## 6. Alcance y transferencia pendiente

El modelo muestra de manera positiva que el fallo de capas PSD no impide una prueba uniforme del kernel completo: aquí el mecanismo es el Green de una ODE en la escala. No se ha construido una ODE/Green con la identidad REP para Z de la Phi real. La similitud de las colas no proporciona esa identidad.

Tampoco se transfiere por mezclar densidades positivas: GRAM_SLICES§7 ya muestra que tales mezclas no conservan en general el signo del kernel de la derivada logarítmica. No se propone una campaña de modelos ni se afirma cierre de W. El input que habría que transportar es la representación positiva independiente del parámetro, no sólo una aproximación de phi_a a Phi.

Auditoría: casos e invariante_nuevo verificaron independientemente la normalización Z_a=y_(u²/4)(0), los bordes, el factor1/2 de REP y los coeficientes1/2,1/8 de GRAM; mapa realizó el cotejo dirigido de antecedentes. Sin cómputos numéricos.

## 7. Transferencias positivas directas: el prefactor real impide dos representaciones

**PROVED para las dos clases declaradas; revisión independiente casos/invariante_nuevo y root.** Consulta previa de los tres índices y GRAM_SLICES§7: allí la exclusión cuártica compara órdenes de decaimiento diferentes. Aquí ambos modelos tienen orden doble exponencial; la diferencia decisiva es el prefactor, no sólo ese orden. No se registra una prohibición general de transferencias o de operadores positivos.

La serie theta real de CONE001 da, aislando n=1 y acotando la cola n>=2,

    Phi(t)~2pi² exp(9t/2) exp(-pi exp(2t)), t→infinito. (THETA-TAIL)

En efecto el primer término es pi exp(5t/2)(2pi exp(2t)-3)exp(-pi exp(2t)); los restantes, tras dividir por su término principal, están dominados por una constante por sum_(n>=2) n^4 exp[-pi(n²-1)exp(2t)], que tiende a0 por dominación. Se usan tanto la tasa -log(Phi)/exp(2t)→pi como el prefactor no acotado.

### 7.1 Mezclas positivas puras

No existe una medida positiva mu sobre a>0 tal que

    Phi(t)=integral exp(-a cosh(2t))dmu(a)

para todo t. Se permite mu de masa total infinita; sólo se exige el valor finito en0, integral exp(-a)dmu(a)=Phi(0).

Poner q=cosh(2t) y d sigma=exp(-a)dmu. Sigma es finita. Si tiene masa positiva debajo de 2pi, algún intervalo a<=2pi-epsilon tiene masa positiva y proporciona un minorante constante por exp[-(2pi-epsilon)(q-1)]. Esto contradice THETA-TAIL, pues -log(Phi)/q→2pi. Luego sigma está soportada en [2pi,infinito), de modo que

    Phi(t)<=Phi(0) exp[-2pi(q-1)].

Pero THETA-TAIL da exp(2pi q)Phi(t)~2pi² exp(9t/2)→infinito, contradicción. Amplitudes positivas dependientes de a y normalizaciones de cada modelo se absorben en mu; factores dependientes de t no pertenecen a esta clase.

### 7.2 Convolución con una medida positiva finita

Para cualquier a>0 fijo, no existe una medida positiva finita no nula nu sobre R con Phi=phi_a*nu. No se supone nu par ni compacta.

Poner S=(1/2)log(a/(2pi)). Si nu tiene masa por encima de S, hay un intervalo finito [b,c], b>S, de masa m>0. Para y en ese intervalo,

    a cosh(2(t-y))
       <=(a/2)exp(2t-2b)+(a/2)exp(-2t+2c).

La contribución del intervalo da entonces

    limsup_(t→infinito) -log(Phi(t))/exp(2t)
       <=(a/2)exp(-2b)<pi,

contrario a THETA-TAIL. Por tanto nu está soportada en (-infinito,S]. Para todos esos y,

    phi_a(t-y)<=exp[-(a/2)exp(2t-2y)]
               <=exp[-pi exp(2t)].

Integrar prueba Phi(t)<=nu(R)exp[-pi exp(2t)], de nuevo incompatible con el prefactor de THETA-TAIL. El argumento cubre soporte no acotado antes de deducir su restricción superior.

Estas exclusiones no afectan al teorema del modelo de§5. Tampoco excluyen prefactores temporales, diferenciaciones, combinaciones firmadas u otros potenciales de Green. No dan W negativa ni una desigualdad para el kernel real. Evitan únicamente utilizar las dos representaciones positivas exactas anteriores como puente automático.

## 8. Operación positiva comprobada: prefactor afín y borde Robin

**PROVED para la extensión del modelo; transferencia real OPEN.** Consulta previa de los tres índices y cotejo dirigido de mapa: las apariciones anteriores de Robin/Neumann en014,075,102 y las series Neumann aritméticas no son esta operación sobre la escala del modelo. Revisión independiente casos/invariante_nuevo y root. No se inicia una campaña de prefactores.

Para a>0 y beta>=0 fijos, definir

    phi_(a,beta)(t)=[beta+a cosh(2t)]exp[-a cosh(2t)].

Su transformada bilateral, con las convenciones anteriores, es

    Z_(a,beta)(u)=beta y_x(0)-y_x'(0), x=u²/4,

pues derivar en r el integrando de y introduce -a cosh v en r=0. Los parámetros a,beta permanecen independientes de x.

Sea m_x=-y_x'(0)/y_x(0)>0 y k_x(r)=y_x(r)/y_x(0). El Wronskiano paramétrico de§3 da

    partial_x m_x=integral_0^infinito k_x(r)²dr>0.

El operador H_beta tiene la misma expresión -D²+a²exp(2r), ahora con borde f'(0)=beta f(0). Su forma es

    integral [|f'|²+a²exp(2r)|f|²]dr+beta|f(0)|²,

por lo que H_beta>=a². El signo del término de borde es positivo. Su Green se obtiene explícitamente del Dirichlet:

    R_(beta,x)=R_x+[k_x tensor k_x]/(m_x+beta).       (ROBIN)

Para comprobar el borde, partial_r G_x(0,s)=k_x(s), mientras k_x'(0)=-m_x; por tanto el lado derecho cumple partial_r G_(beta,x)(0,s)=beta G_(beta,x)(0,s). El salto interior y el decaimiento son los mismos. RATIO da integral k_x²<=1/(2a), y -y_x'/y_x>=a en r=0, así la corrección tiene traza finita. En consecuencia,

    Tr R_(beta,x)=Tr R_x+(partial_x m_x)/(m_x+beta)
      =partial_x log[beta y_x(0)-y_x'(0)].           (ROBIN-TRACE)

Por ello M_(a,beta)(u)/u=(1/2)Tr(H_beta+u²/4)^(-1). La prueba GRAM de§5 se aplica sin cambios a cualquier número de parámetros positivos. En la escritura como integrales de cuadrados aparece además el término no negativo

    (beta/2) integral_0^infinito |F(0,s)|²ds.

Beta=0 es el caso Neumann y equivale, salvo el factor positivo a, a derivar la densidad base respecto de -a. Esta es una operación concreta cuya positividad se demuestra mediante el borde, no una afirmación general de que derivar o multiplicar densidades preserve el kernel logarítmico.

El prefactor obtenido crece como exp(2t), mientras el de THETA-TAIL crece como exp(9t/2). La extensión no identifica Z_(a,beta) con Z real, ni proporciona una representación positiva de esta última. No se infiere signo de W ni nueva ventana T. Falta una construcción que reproduzca la theta completa y conserve la representación de traza.

## 9. El flujo de escala del modelo no tiene orden matricial en todos los tamaños

**PROVED, clase y dato auxiliares precisos.** Para cada a>0, K_a es el kernel positivo del modelo de§5. Sin embargo,

    D_a(u,v)=-a partial_a K_a(u,v), u,v>0,

NO es PSD en todos los tamaños. No se afirma esto para el flujo de la theta real. Se prueba para contrastar la propuesta de integrar una derivada matricial positiva desde escalas grandes; la positividad de todos los K_a no autoriza ese paso.

Consulta previa: índices/grid/crucigrama y comparación con POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION,073 y los flujos registrados. SHIFT cambia los exponentes del test; aquí cambia la escala de una densidad auxiliar explícita. La comparación de covarianzas de073 sólo firma cantidades escalares. No se atribuye novedad al cálculo abstracto con momentos. Auditoría matemática independiente casos/invariante_nuevo y root; sin cómputos ni argumentos sobre la función original mediante ceros.

Escribir V_a(r)=a²exp(2r), H=H_a y R_x=(H+x/4)^(-1), donde ahora x=u². Por REP y la identidad de derivación de resolventes,

    P_a(x):=-a partial_a[M_a(sqrt(x))/sqrt(x)]
           =Tr(R_x V_a R_x).                         (SQUARE-RES)

El factor es1, pues a partial_a H=2V_a y REP aporta1/2. La identidad es válida como derivación de formas: 0<V_a<=H y la traza finita de H^(-1) dominan los productos. No se necesita diferenciar valores propios.

El inverso de H es positivo, compacto y de traza finita por§4. En una base ortonormal de sus vectores propios, escribir H psi_j=lambda_j psi_j y v_j=<psi_j,V_a psi_j>. Entonces

    0<v_j<=lambda_j,
    P_a(x)=sum_j v_j/(lambda_j+x/4)²,
    sum_j v_j/lambda_j²<=Tr H^(-1)<infinito.

Esta descomposición sólo concierne al operador positivo explícito del modelo. Agrupar, si fuese necesario, los valores propios repetidos. El menor valor lambda_* tiene multiplicidad finita y está separado del siguiente valor distinto. Para |x|<4lambda_* la serie es absolutamente convergente y

    P_a(x)=sum_(n>=0)(-1)^n A_n x^n,
    A_n=(n+1)sum_j w_j t_j^n,
    w_j=v_j/lambda_j²>0, t_j=1/(4lambda_j).

Poner t_*=max t_j, W_*=sum_(t_j=t_*)w_j>0 y rho=(siguiente t_j)/t_*<1. La masa sum w_j es finita, de modo que

    A_n=(n+1)W_* t_*^n[1+epsilon_n],
    0<=epsilon_n<=C rho^n.

En particular,

    A_n A_(n+2)-A_(n+1)²
      =-W_*² t_*^(2n+2)[1+O(n²rho^n)]<0             (NEG-MOM)

para todo n suficientemente grande. El factor principal negativo procede de (n+1)(n+3)-(n+2)²=-1; la tasa exponencial del error es necesaria para conservarlo.

Por otra parte, D_a(u,v)=[uP_a(u²)+vP_a(v²)]/(u+v). Su coeficiente de u^(2i)v^(2j) en el desarrollo alrededor de(0,0) es (-1)^(i+j)A_(i+j). Si D_a fuera PSD para todos los conjuntos finitos de nodos positivos, sus matrices finitas de coeficientes serían PSD: aproximar cada derivada por diferencias finitas con nodos estrictamente positivos, dividir por los factoriales y pasar al límite. La congruencia diagonal por (-1)^i daría entonces

    [A_(i+j)]_ij PSD.

Su menor con índices k,k+1 exige A_(2k)A_(2k+2)-A_(2k+1)²>=0, contrario a NEG-MOM para k grande. Por continuidad de las diferencias finitas existe un conjunto FINITO de nodos positivos con D_a indefinida; no se calcula su tamaño ni se necesita una campaña de parámetros.

Conclusión restringida: el Gram de§5 permanece válido para cada escala, pero su derivada de escala no conserva PSD en todos los órdenes. Esto excluye deducir una monotonía matricial automática a partir de ese Gram o de covarianzas diagonales positivas. No decide la derivada del flujo theta ni el signo de W, y no excluye una compensación integrada distinta.

## 10. El prefactor fijo no produce un potencial escalar independiente del parámetro

**PROVED, alcance restringido.** Propuesta y revisión independiente invariante_nuevo/root/casos; cotejo dirigido de mapa en índices, grid, crucigrama y fuentes, sin antecedente literal identificado ni afirmación de prioridad mundial. La diferencia respecto de§7 es que aquí se permite un prefactor temporal fijo arbitrario, pero se exige conservar la ecuación escalar en la escala con potencial independiente del parámetro. No se excluyen otras ecuaciones ni operaciones preservantes.

Sea q una función par C², estrictamente positiva, con |q(v)|+|q'(v)|+|q''(v)|<=C exp(C|v|). Para b>0 y nu real definir

    Y_nu(b)=integral_0^infinito exp(-b cosh v)q(v)cosh(nu v)dv.

Con b=a exp(r), dos integraciones por partes dan exactamente

    partial_r² Y_nu=(b²+nu²)Y_nu+F_nu(b),
    F_nu(b)=integral exp(-b cosh v)
              [q''(v)cosh(nu v)+2nu q'(v)sinh(nu v)]dv
           =integral exp(-b cosh v)
              [-q''(v)+2b sinh(v)q'(v)]cosh(nu v)dv.       (FORCE)

Los bordes se anulan porque q'(0)=0 y por el decaimiento doble exponencial. Supongamos que en dos escalas distintas b1,b2 existen números E(bi), independientes de nu, tales que F_nu(bi)=E(bi)Y_nu(bi) para todos los nu de algún intervalo real abierto. Entonces necesariamente q es constante y E(b1)=E(b2)=0.

Prueba: para cada b fijo, la transformada cosh de

    h_b(v)=exp(-b cosh v)[-q''(v)+2b sinh(v)q'(v)-E(b)q(v)]

es entera en nu por las cotas declaradas. Su anulación en un intervalo implica anulación también en nu=i tau. La extensión par de h_b tiene por tanto transformada Fourier nula y es cero. Para explicitar la unicidad usada: convolucionar h_b con cualquier gaussiana escribe esa convolución como la integral de su transformada Fourier nula por otra gaussiana (Fubini es absoluto); al estrechar la gaussiana, la aproximación de la identidad recupera h_b. Por continuidad,

    -q''(v)+2b sinh(v)q'(v)=E(b)q(v)              para todo v>=0.

Restar las identidades de b1,b2 y evaluar en v=0 da [E(b1)-E(b2)]q(0)=0. Puesto que q(0)>0, ambos E coinciden. Para v>0 queda 2(b1-b2)sinh(v)q'(v)=0: q'=0. Sustituir prueba E=0. Basta el intervalo de parámetros del portador; no se supone originalmente la identidad para parámetros imaginarios.

Aplicación a la tentativa real: a=2pi y q(v)=Phi(v/2)exp(2pi cosh v) dan Y_(u/2)(a)=Z_real(u) exactamente. La paridad y suavidad de Phi hacen q par suave. El primer término de la serie theta y sus dos derivadas crecen a lo sumo exponencialmente después de retirar exp(-pi exp(v)); la cola n>=2 y sus derivadas están dominadas por polinomios en exp(v) multiplicados por exp[-pi(n²-1)exp(v)]. Por tanto q satisface las cotas anteriores. Además§7 da q(v)~2pi² exp(9v/4), por lo que no es constante. Esta familia no satisface una ecuación Y''=[b²+nu²+E(b)]Y con E independiente de nu en un intervalo de escalas.

No se refuta un Green diferente, una transformación adicional, un sistema matricial ni un prefactor dependiente de b. En particular Robin§8 usa q_b(v)=beta+b cosh(v), que depende de la escala, y no pertenece a la clase excluida. Tampoco se demuestra signo negativo del kernel real. La compensación de la fuente dependiente de nu sigue sin una estimación firmada uniforme.


### 10.1. Permitir una primera derivada: clasificación completa dentro de esta familia

**PROVED, revisión independiente root/casos; dedup dirigido mapa.** Cambio explícito respecto de§10: se permite ahora un coeficiente arbitrario de la primera derivada en r. Se mantienen el prefactor q fijo, las hipótesis de regularidad y crecimiento de§10, la coordenada b=a exp(r) y el coeficiente UNO de nu². No se reabre la misma clase sin modificar hipótesis.

Supongamos que, para b en un intervalo abierto positivo y nu en un intervalo real abierto,

    Y_rr=A(b)Y_r+[b²+nu²+E(b)]Y,                       (DRIFT)

con A,E independientes de nu. Entonces las únicas posibilidades son

    q(v)=C>0,                  A=0,  E=0;
    q(v)=C cosh(v/2), C>0,     A=-1, E=-b-1/4.

Ambas satisfacen efectivamente DRIFT. No se afirma aquí una representación positiva del segundo caso.

Prueba. Y_r=-b integral exp(-b cosh v)q(v)cosh(v)cosh(nu v)dv. La unicidad ya justificada en§10 transforma DRIFT en

    -q''/q+2b sinh(v)q'/q=-b A(b)cosh(v)+E(b).          (D1)

Restar D1 en dos escalas distintas da constantes alpha,beta tales que

    2sinh(v)q'/q=alpha cosh(v)+beta.

Evaluar en0 fuerza beta=-alpha. Para v>0, q'/q=(alpha/2)tanh(v/2); integrar y usar continuidad en0 da q=C cosh(v/2)^alpha. Por tanto

    q''/q=alpha²/4+(alpha-alpha²)sech²(v/2)/4.

Al sustituir en D1, todos los otros términos están en el espacio generado por1 y cosh(v). La función sech²(v/2) no pertenece a ese espacio: su límite0 en infinito obliga primero a anular el coeficiente de cosh y después la constante. Así alpha-alpha²=0. Sustituir alpha=0 o1 da exactamente los coeficientes anunciados, y verifica también suficiencia.

El prefactor real de§10 crece como exp(9v/4), incompatible tanto con una constante como con cosh(v/2). Queda excluida DRIFT para esa familia real, aun permitiendo primera derivada.

También se excluye una multiplicación escalar no nula g(r), C² e independiente de nu, que convierta esta Y en z=gY con z_rr=[nu²+V(r)]z: al dividir la identidad por g se obtiene DRIFT con A=-2g'/g y E=V-g''/g-b². Esta consecuencia sólo concierne a esa multiplicación y esa coordenada. No excluye cambios de variable, transformaciones integrales, normalizaciones dependientes de nu, prefactores dependientes de b, sistemas matriciales ni otros Green. No es una refutación del signo real ni de la comparación relativa de formas.


**Ampliación para la q real: peso espectral variable y cambio de escala.** Revisión independiente root/casos y cotejo mapa. La reserva anterior sobre cambios de variable se puede retirar para la operación precisa que sigue, no para transformaciones generales. Supóngase ahora Y_rr=A(b)Y_r+[w(b)nu²+B(b)]Y, con coeficientes independientes de nu. Dos integraciones por partes transfieren nu² a la segunda derivada en v de exp(-b cosh v)q(v); la unicidad de§10 da

    (1-w)b²cosh²(v)+[(w-1)+A]b cosh(v)+wb²-B
       -w q''/q+2wb sinh(v)q'/q=0.                    (WEIGHT)

No se comparan formalmente coeficientes de nu entre funciones dependientes de nu. Para q real, su primer modo theta escribe exactamente

    q(v)=2pi² exp(9v/4)exp(pi exp(-v))
          [1-(3/(2pi))exp(-v)+R(v)],

con R y sus primeras dos derivadas superexponencialmente pequeñas: proceden de n>=2 y conservan factores exp[-pi(n²-1)exp(v)] tras derivar. En consecuencia q'/q=9/4+O(exp(-v)) y q''/q=81/16+O(exp(-v)). Dividir WEIGHT por cosh²(v) y enviar v a infinito fuerza w(b)=1 para cada b. La ecuación vuelve a DRIFT con E=B-b², imposible para q real por la clasificación anterior.

En particular, si t=h(r) es C² con h' no nula y z(h(r))=g(r)Y(r), g C² no nula, ambas independientes de nu, la ecuación z_tt=[nu²+V(t)]z implicaría

    w=h'^2, A=h''/h'-2g'/g,
    B=h'^2 V(h(r))-g''/g+(g'/g)(h''/h').

WEIGHT fuerza h'^2=1 y por continuidad h'=1 o -1 en cada intervalo conexo. No hay por tanto reparación mediante este cambio de escala y multiplicación escalar. El resultado no clasifica pesos variables para q arbitraria, ni excluye nuevas familias integrales, transformaciones dependientes del parámetro o sistemas matriciales. No prueba signo de W ni refuta la comparación relativa de formas.

## 11. Transferencia por productos de cosh: representación exacta excluida

**PROVED, alcance restringido.** Revisión matemática independiente root/casos; búsqueda transversal de antecedentes por mapa en índice, grid, crucigrama y fuentes seleccionadas, sin atribución de novedad bibliográfica mundial. La diferencia respecto de§7 es que ahora se permite multiplicar temporalmente el modelo por factores positivos, no mezclarlo ni convolucionarlo. A diferencia de§10, no se exige ninguna ecuación diferencial ni se presupone cómo se demostraría la preservación del signo. Se descarta la representación exacta antes de intentar esa preservación.

No existen C>0, a>0 y una familia finita o numerable de números alpha_j>0, con sum_j alpha_j²<infinito, tales que para todo t real

    Phi(t)=C exp(-a cosh(2t)) prod_j cosh(alpha_j t).   (CP)

El producto vacío también queda excluido. Se trata de factores sin desplazamientos y con exponente unitario; no se incluyen potencias reales, cocientes, sumas o combinaciones firmadas.

### 11.1. La escala y la suma de exponentes quedan forzadas

La desigualdad 0<=log cosh(x)<=x²/2 asegura convergencia del producto en compactos reales y

    0<=sum_j log cosh(alpha_j t)<=t² sum_j alpha_j²/2.

La cola theta conocida da log Phi(t)/exp(2t)->-pi. Dividir el logaritmo de(CP) por exp(2t) fuerza a=2pi. Sea Q(t)=Phi(t)exp(2pi cosh(2t)). Su expansión es

    Q(t)=2pi² exp(9t/2)
          [1+c1 exp(-2t)+O(exp(-4t))],
    c1=pi-3/(2pi),    2<c1<3.                        (TAIL-CP)

Para justificar el resto, el modo n=1 aporta exactamente

    2pi² exp(9t/2) exp(pi exp(-2t))
        [1-(3/(2pi))exp(-2t)].

Los modos n>=2, después de dividir por exp(9t/2), son O(exp(-3pi exp(2t))) para t suficientemente grande: con y=pi exp(2t)>=1, sus valores absolutos se acotan por una constante por sum_(n>=2)(n^4+n²)exp(-(n²-1)y), y se extrae exp(-3y). Por tanto no modifican los dos primeros coeficientes. Las cotas 3<pi<22/7 y la monotonía de x-3/(2x) prueban 2<c1<3 sin cómputo numérico.

Para cada alpha>0, log cosh(alpha t)/t aumenta a alpha cuando t aumenta desde0: el signo de la derivada se reduce a x tanh(x)-log cosh(x)>=0, cuya derivada es x sech²(x)>=0. Convergencia monótona para la serie y(TAIL-CP) dan

    sum_j alpha_j=lim_(t->infinito) log(Q(t)/C)/t=9/2.

### 11.2. Infinitos factores no conservan el coeficiente principal

Si hubiese infinitos factores, la suma anterior permitiría escribir

    exp(-9t/2) prod_j cosh(alpha_j t)
      =prod_j [(1+exp(-2alpha_j t))/2].

Todos los factores pertenecen a(0,1]. Para cada N, el producto completo es menor o igual que el producto de los primeros N factores, cuyo límite es 2^(-N). Al hacer N arbitrariamente grande, el límite del producto completo es0. Esto contradice(TAIL-CP), que exigiría el límite positivo 2pi²/C.

### 11.3. Finitos factores exigen una multiplicidad no entera

Quedan m factores, con suma9/2 y C 2^(-m)=2pi². Sea alpha_* su mínimo y k>=1 su multiplicidad entera. Al dividir por el término principal,

    prod_(j=1)^m(1+exp(-2alpha_j t))
      =1+k exp(-2alpha_* t)+o(exp(-2alpha_* t)).

Comparar con(TAIL-CP) fuerza alpha_*=1 y k=c1. Pero 2<c1<3, imposible para un entero. Esto concluye la exclusión de(CP).

**Decisión y límites.** No se necesita decidir si multiplicar un modelo por cosh preserva su kernel para descartar(CP): ni siquiera una preservación universal daría esa representación de Phi. No se ha demostrado ni refutado tal preservación. Tampoco se excluyen aproximaciones por otras clases, comparaciones relativas de formas, productos con potencias reales o una nueva representación conjunta. No hay signo nuevo de W, ampliación de T ni cambios en papers.


### 11.4. Tampoco hay aproximación uniforme en compactos a escala fija (2026-11-06)

**PROVED, root/casos; auditoría independiente matemática y literal preservador; cotejo dirigido mapa.** Diferencia frente§11: se decide una clase de aproximaciones que el descarte de representaciones exactas no cubría. Consultados los tres índices y antecedentes por mapa; no se halló esta aplicación literal. El lema de compactitud no se presenta como principio nuevo ni como novedad mundial.

No existe una sucesión

    phi_n(t)=C_n exp(-2pi cosh(2t)) prod_(j=1)^(m_n) cosh(alpha_nj t),
    C_n>0, alpha_nj>0,

que converja a Phi uniformemente en cada compacto real. La escala2pi es FIJA; los números de factores y todos sus parámetros pueden variar.

**Lema de clausura.** Si Q_n(t)=prod_j cosh(alpha_nj t) converge localuniformemente a una función Q positiva, entonces

    Q(t)=exp(gamma t²) prod_(j>=1)cosh(alpha_j t),
    gamma>=0, sum_j alpha_j²<infinito.

Se permiten factores nulos, omitidos del producto. En efecto Q_n(0)=Q(0)=1 y log Q_n converge localuniformemente a log Q. Una cota log Q_n(1)<=L da alpha_nj<=A para un A finito. Como logcosh(x)/x² tiene límite1/2 en0 y es positiva en[0,A], existe c>0 con logcosh(x)>=c x² allí. Así sum_j alpha_nj²<=B=L/c.

Ordenar los parámetros en orden decreciente, completar con ceros y extraer una subsucesión diagonal con alpha_nj→alpha_j para cada j y S_n=sum_j alpha_nj²→S. Fatou da sum_j alpha_j²<=S<=B. Además alpha_n,J+1²<=B/(J+1). Para cada T finito, Taylor con resto uniforme en[-AT,AT] da

    |logcosh(alpha t)-alpha²t²/2|<=C_T alpha⁴, |t|<=T.

Por tanto el error de reemplazar la cola j>J por su término cuadrático es como máximo C_T B²/(J+1), uniformemente en n y |t|<=T. Pasar primero n→infinito, después J→infinito, prueba

    log Q(t)=sum_j logcosh(alpha_jt)
             +(t²/2)(S-sum_j alpha_j²).

La serie converge uniformemente en compactos por logcosh(x)<=x²/2. Esto prueba el lema, incluyendo toda la masa cuadrática que pudiera perderse en la extracción.

**Aplicación a Phi.** Si existieran los aproximantes declarados, normalizar en t=0 daría

    Q_n(t)→Q(t)=Phi(t)exp(2pi(cosh(2t)-1))/Phi(0).

Por§11.1, log Q(t)/t→9/2 cuando t→infinito. En la representación del lema todos los sumandos logcosh son no negativos. Por ello gamma>0 es imposible y gamma=0. Se obtiene una representación exacta de Phi como constante positiva por exp(-2pi cosh(2t)) y un producto cosh con sum alpha_j² finita, contradiciendo§11.1–11.3.

**Alcance.** Se excluye sólo esta aproximación localuniforme a escala fija por productos unitarios positivos sin desplazamientos. No se decide preservación abstracta del signo al multiplicar por cosh. No se excluyen escalas variables, potencias reales, sumas, cocientes, otras topologías sin puente demostrado ni comparaciones relativas. El resultado evita intentar transferir positividad mediante esta clausura; no prueba signo negativo de Phi ni positividad nueva de W/T. Papers intactos; sin cómputos.


## 12. Un vector finito de prefactores fijos no absorbe la fuente sin derivada primera (2026-11-06)

**PROVED, root/casos; auditoría independiente matemática y literal preservador; cotejo dirigido mapa.** Diferencia frente§10: se permiten matrices arbitrarias y cualquier número FINITO de componentes, no sólo un potencial escalar. Se conserva una clase precisa: prefactores independientes de b y ningún término matricial multiplicando Y_r. Los sistemas generales permanecen fuera de este descarte.

Sea Q(v) un vector de d funciones pares C², con Q,Q',Q'' de crecimiento a lo sumo exponencial, y Q_1(v)=q_theta(v)=Phi(v/2)exp(2pi cosh v). Definir componente a componente

    Y_nu(b)=integral_0^infinito exp(-b cosh v)Q(v)cosh(nu v)dv,
    b=a exp(r).

No existen dos escalas distintas b1,b2 y matrices E(b1),E(b2), independientes de nu, tales que en ambas escalas, para todo nu de un intervalo real abierto,

    Y_rr=(b²+nu²)Y+E(b)Y.

Prueba. La identidad FORCE de§10 y la unicidad de transformada cosh, componente a componente, obligan a

    -Q''(v)+2b sinh(v)Q'(v)=E(b)Q(v).

Restar las ecuaciones en las dos escalas da

    sinh(v)Q'(v)=B Q(v),
    B=[E(b2)-E(b1)]/[2(b2-b1)],

con B constante. Para v>0 poner w(v)=log tanh(v/2). Se tiene w'(v)=1/sinh(v), luego dQ/dw=BQ y, para cualquier v0>0,

    Q(v)=exp(B[w(v)-w(v0)])Q(v0).

Cuando v tiende a infinito, w(v) tiende a0. La exponencial de una matriz finita es continua, así que Q(v) tiene límite finito. Esto contradice la cola completa q_theta(v)~2pi²exp(9v/4), ya justificada en§10. No se necesita diagonalizar B, suponer independencia de las componentes ni imponer signo a las matrices.

**Alcance.** Este cierre falla antes de preguntar si el potencial matricial sería autoadjunto o positivo. No se descartan términos A(b)Y_r, prefactores que dependan de b, sistemas infinitos, otras transformaciones ni otras realizaciones Green. No demuestra negatividad de K_Phi ni modifica la obligación global. Sin cómputos, nueva positividad W/T ni cambios en papers.


### 12.1. Añadir primera derivada matricial tampoco cierra esta clase (2026-11-06)

**PROVED, root/casos/preservador; dos revisiones matemáticas independientes, auditoría literal casos y cotejo dirigido mapa.** El cotejo de los tres índices y fuentes primarias seleccionadas no localizó antecedente literal anterior, excluyendo esta misma entrada. E101_070§5 trata una jerarquía sin cierre automático de banda finita, no este descarte para matrices arbitrarias mediante un anulador racional. No se afirma novedad mundial ni relectura exhaustiva del corpus. Se permite ahora el término A(b)Y_r expresamente excluido del alcance de§12. Los prefactores Q siguen siendo fijos, la dimensión finita y el coeficiente de nu² la identidad. No se trata de un descarte de sistemas matriciales generales.

Con las hipótesis y definiciones de§12, tampoco existen matrices A(b_i),E(b_i), independientes de nu, en dos escalas distintas, tales que

    Y_rr=(b²+nu²)Y+A(b)Y_r+E(b)Y.

**Reducción a un sistema racional.** Como Y_r es la transformada del vector -b cosh(v)Q(v), FORCE y unicidad dan

    -Q''+2b sinh(v)Q'=-b A(b)cosh(v)Q+E(b)Q.

Restar las dos escalas da sinh(v)Q'=(C cosh(v)+B)Q, donde

    C=-(b2 A(b2)-b1 A(b1))/(2(b2-b1)),
    B=(E(b2)-E(b1))/(2(b2-b1)).

Escribiendo x=exp(v)>1 y Qtilde(x)=Q(log x), resulta

    Qtilde_x=R(x)Qtilde,
    R(x)=[C(x²+1)+2Bx]/[x(x²-1)].

R es una matriz racional regular en x>1; esta ecuación eleva automáticamente la regularidad a C-infinito. Las filas racionales r_0=e_1^t, r_(j+1)=r_j'+r_j R satisfacen (Qtilde_1)^(j)=r_j Qtilde. Las d+1 primeras filas son dependientes sobre el cuerpo R(x). Por tanto un operador diferencial racional escalar no nulo anularía q_theta(log x). No se supone independencia de las componentes.

**La serie completa no admite tal operador.** La fórmula theta exacta da

    q_theta(log x)=h(x)g(x),
    h(x)=pi x^(5/4)exp(pi/x),
    g(x)=sum_(n>=1)n²(2pi n²x-3)exp(-lambda_n x),
    lambda_n=pi(n²-1).

Como h'/h=5/(4x)-pi/x² es racional, conjugar el operador por h y limpiar denominadores daría un operador no nulo

    L=sum_(k=0)^d p_k(x)D_x^k,  p_k polinomios,

que anula g. Sea m el máximo grado de los p_k no nulos. Derivar término a término es legítimo en x>=x0>1: cada orden fijo sólo introduce factores polinómicos en n y x, dominados por las colas exp(-pi n²x). Así

    0=Lg=sum_(n>=1)P_n(x)exp(-lambda_n x),

con deg P_n<=m+1 y coeficientes de crecimiento polinómico en n. Para cada N fijo, la cola n>N es O(x^(m+1)exp(-lambda_(N+1)x)) cuando x>=2; extraer esa exponencial deja una serie convergente de potencias de n por exp(-2(lambda_n-lambda_(N+1))).

Aislar el primer modo prueba P_1=0: un polinomio que decae exponencialmente es nulo. Suprimiéndolo y repitiendo se obtiene P_N=0 para todo N. Sin embargo el coeficiente de x^(m+1) en P_n es

    2pi n^4 sum_(k:deg p_k=m) lead(p_k)(-lambda_n)^k.

El polinomio en lambda de esta expresión no es nulo por definición de m. No puede anularse en las infinitas lambda_n distintas. Contradicción. Se conserva la serie aritmética completa durante toda la prueba; no hay truncación numérica ni argumento sobre ceros de funciones transformadas.

**Alcance.** Queda excluido este cierre finito de prefactores fijos incluso con primera derivada matricial y matrices arbitrarias, sin necesitar autoadjunción o positividad. Permanecen fuera prefactores dependientes de b, dimensión infinita, coeficiente espectral matricial distinto de la identidad y otras representaciones. No negatividad de K_Phi, nueva positividad W/T ni cambios en papers.


### 12.2. Dimensión infinita: rigidez bajo dos operadores simétricos

**PROVED para la clase fuerte declarada, 2026-11-06.** Construcción root; auditorías independientes new_structural_sign y arithmetic_fresh_candidate PASS. Consulta dirigida las reglas del proyecto, los tres índices, §§12–12.1 y E101_070; búsqueda adicional Hankel/Hilbert sin antecedente literal localizado. No se afirma novedad bibliográfica. La diferencia frente§12 es permitir un Hilbert de dimensión infinita y operadores no acotados, a cambio de exigir simetría en un dominio común. La prueba finita por exponencial matricial no decide esta clase.

**Lema.** Sea Q:(0,infinito)->H una función C² en norma de un Hilbert real o complejo. Sean B,C operadores lineales simétricos en un dominio lineal común D que contiene todos los Q(v). Supóngase, como identidades fuertes,

    sinh(v)Q'(v)=B Q(v),       Q''(v)=C Q(v).             (INF-SYM)

Entonces existen constantes A,c>=0 tales que

    ||Q(v)||²=A+c log(cosh v).                           (INF-NORM)

En particular toda observación lineal continua ell satisface |ell(Q(v))|=O(sqrt(1+v)). No se requiere acotación de B o C, autoadjunción, semiboundedness ni Q(v) en Dom(B²).

**Prueba.** Poner w=log(tanh(v/2))<0 y q(w)=Q(v(w)). Como dw/dv=1/sinh(v), se tiene q_w=Bq. Para K(w,z)=<q(w),q(z)>, la simetría de B da K_w=K_z. Cada segmento de suma w+z constante en el cuadrante negativo es conexo; por tanto K(w,z)=F(w+z), con F C² en(-infinito,0). La simetría hermitiana implica que F es real.

La regla de la cadena da

    Q''(v)=a(w) q_ww(w)+b(w) q_w(w),
    a(w)=(cosh(2w)-1)/2,
    b(w)=sinh(2w)/2.

La simetría de C, aplicada a Q(v(w)) y Q(v(z)), produce

    [cosh(2w)-cosh(2z)]F''(w+z)
       +[sinh(2w)-sinh(2z)]F'(w+z)=0.

Para w!=z, dividir por 2sinh(w-z) y poner s=w+z. Todo s<0 admite tal elección; queda

    sinh(s)F''(s)+cosh(s)F'(s)=0.

Así F(s)=A+kappa log|tanh(s/2)|. En la diagonal, tanh(w(v))=-1/cosh(v), por lo que ||Q(v)||²=A-kappa log(cosh v). Su no negatividad para todos v>0 obliga A>=0 y kappa<=0. Poner c=-kappa prueba(INF-NORM). Todas las derivaciones se realizan sobre el kernel C²; nunca se aplica B a Q' ni se intercambia un operador no acotado con una integral.

**Aplicación al cierre fuerte sin primera derivada.** Sean b1!=b2 positivos y E1,E2 simétricos sobre un dominio común D. Si Q es C² en norma, toma valores en D y satisface

    -Q''+2b_i sinh(v)Q'=E_i Q,   i=1,2,                 (INF-FORCE)

entonces B=(E2-E1)/(2(b2-b1)) y C=2b1 B-E1 son simétricos sobre D y cumplen(INF-SYM). Por tanto no puede existir una observación lineal continua ell con

    ell(Q(v))=q_theta(v)=Phi(v/2)exp(2pi cosh v),

pues la cola theta completa de§10 es q_theta(v)~2pi²exp(9v/4), incompatible con(INF-NORM).

**Dominios y alcance.** El resultado excluye(INF-FORCE) en dimensión infinita, incluso con operadores no acotados. Para deducir(INF-FORCE) desde una ecuación integral para Y_nu se debe justificar además el paso del operador por la integral y la unicidad de la transformada; por ejemplo, mediante integrabilidad adecuada en norma de grafo. No se declara ese intercambio automático. No se excluyen sistemas con primera derivada, operadores no simétricos, observaciones no continuas, prefactores dependientes de la escala, métricas variables ni otras realizaciones Green. La clase finita con deriva de§12.1 y esta clase infinita simétrica sin deriva tienen alcances distintos. Esto no refuta K_Phi, no demuestra signo global ni amplía T. Sin cómputos ni cambios en papers.


### 12.3. Deriva escalar constante: kernel forzado por simetría y paridad

**PROVED para la clase fuerte declarada, 2026-11-06.** Construcción root, revisiones independientes new_structural_sign y arithmetic_fresh_candidate PASS; auditoría literal arithmetic_fresh_candidate PASS. Consulta de las reglas del proyecto, los tres índices, §§12–12.2 y las cúspides theta de GLOBAL/GRAM§16. Diferencia frente§12.2: se permite una primera derivada escalar constante de cualquier signo, en dimensión infinita; se exige ahora regularidad par hasta el origen. No se atribuye novedad mundial al método de kernels.

**Hipótesis.** Sea Q:R->H par y C² en norma, con valores en un dominio lineal común D de operadores B,C simétricos. Para algún alpha real fijo supóngase

    sinh(v)Q'(v)+alpha cosh(v)Q(v)=B Q(v),
    Q''(v)=C Q(v).                                      (DRIFT-SYM)

Basta exigirlo para v>=0: la paridad extiende las identidades. No se supone acotación ni autoadjunción de los operadores. Sea A=||Q(0)||².

**Kernel exacto.** Para v,z reales, necesariamente

    <Q(v),Q(z)> = (A/2)[cosh((v+z)/2)^(-2alpha)
                         +cosh((v-z)/2)^(-2alpha)].      (DRIFT-K)

Para probarlo, la simetría de C implica K_vv=K_zz. La condición Q'(0)=0 da K_z(v,0)=0, y d'Alembert con f(v)=<Q(v),Q(0)> proporciona K(v,z)=[f(v+z)+f(v-z)]/2. Además f es par y real: K(v,0)=K(0,v), junto con hermiticidad. La simetría de B da

    sinh(v)K_v-sinh(z)K_z
                    +alpha(cosh(v)-cosh(z))K=0.

Con x=v+z, y=v-z positivos, dividir por sinh(x/2)sinh(y/2) reduce esta igualdad a H(x)+H(y)=0, donde H(x)=coth(x/2)f'(x)+alpha f(x). Para cualesquiera x>y>0 vale esa identidad; por continuidad al hacer y tender a x, H(x)=0. Resolver f'=-alpha tanh(x/2)f con f(0)=A da f=A cosh(x/2)^(-2alpha), probando(DRIFT-K).

**Continuación vectorial, no sólo escalar.** El lado derecho de(DRIFT-K) tiene extensión holomorfa en dos variables al producto de franjas |Im v|,|Im z|<pi/2. Se toman las ramas de logcosh continuadas desde el eje real; no hay ceros de cosh allí. Este kernel analítico obliga a Q a ser analítica en norma. En detalle, los productos internos de los cocientes finitos se calculan con K; las diferencias de cocientes son Cauchy por las derivadas del kernel, proporcionando sucesivamente Q^(n). La estimación de Cauchy en un bidisco de radio R<pi/2 centrado en un punto real r da

    ||Q^(n)(r)/n!|| <= sqrt(M_R) R^(-n),

pues el cuadrado de esa norma es el coeficiente mixto (n,n) del kernel. Las series Taylor Hilbertianas convergen, coinciden con Q sobre el eje real por la identidad de sus productos internos y se pegan en la franja. Polarizar y continuar(DRIFT-K) da, para Z=X+iY, |Y|<pi/2,

    ||Q_hol(Z)||²=(A/2)[cosh(X)^(-2alpha)
                                  +cos(Y)^(-2alpha)].   (DRIFT-HOL)

No se afirma que la fórmula sea un kernel positivo para todo alpha: si existe Q, su positividad y esta identidad son consecuencias necesarias. No se aplica ningún operador no acotado a la continuación compleja.

**Incompatibilidad con la observación theta.** Si alpha>=0, (DRIFT-K) en la diagonal real acota ||Q(v)||² por A. Esto impide ell(Q(v))=q_theta(v) para cualquier funcional lineal continuo ell, porque q_theta(v)~2pi²exp(9v/4).

Si alpha<0, (DRIFT-HOL) permanece acotada con X=log2 y Y tendiendo a pi/2 desde abajo. La observación ell(Q_hol(Z)) también debe permanecer acotada. Pero la igualdad real con q_theta se continúa holomórficamente. Para w=exp(Z)=2i+zeta, el cálculo completo de Poisson en GLOBAL, «La diagonal en las dos cúspides», prueba

    Phi(Z/2)=w^(5/4)[(3i/2)zeta^(-5/2)+E(zeta)],
    |E(zeta)|<=C |zeta|^(-M) exp(-b/|zeta|)

en un sector alrededor del semieje real positivo. El camino Z=log2+iY entra en ese sector, con arg zeta tendiendo a0. El factor exp(2pi cosh Z) tiene límite finito y no nulo. Por tanto |q_theta(Z)| diverge, contradiciendo(DRIFT-HOL). Se usa la cúspide PAR w=2i: la cúspide alternante w=i no sirve, pues allí la theta decae. Así ninguna alpha real permite la observación theta en esta clase.

**Relación con FORCE y límites.** Dos identidades fuertes

    -Q''+2b_i sinh(v)Q'
        =-2alpha b_i cosh(v)Q+E_iQ,   b1!=b2,

con E_i simétricos sobre D producen(DRIFT-SYM), tomando B=(E2-E1)/(2(b2-b1)), C=2b1B-E1. Corresponden al intento Y_rr=(b²+nu²)Y+2alpha Y_r+E(b)Y, sólo cuando se han justificado los intercambios y dominios necesarios para obtener FORCE. No se infiere FORCE formalmente desde esa ecuación integral. El descarte concierne a prefactores fijos pares, deriva escalar CONSTANTE, simetría en dominio común y observación continua. Permanecen fuera deriva dependiente de escala o verdaderamente operatorial, métricas variables, otras representaciones y observaciones no continuas. No se obtiene negatividad de K_Phi ni positividad global; sin cómputos, nueva ventanaT o cambios en papers.


### 12.4. La deriva escalar dependiente de escala queda forzada a ser constante

**PROVED para la clase fuerte declarada, 2026-11-06.** Root; auditorías independientes arithmetic_fresh_candidate y new_structural_sign PASS, incluida revisión literal de este último. Consulta las reglas del proyecto, los tres índices y §§10.1,12–12.3. La clasificación escalar de§10.1 no cubría observaciones de un vector Hilbertiano infinito. Frente§12.3 se permiten ahora valores diferentes del coeficiente de primera derivada en dos escalas; no se modifica la simetría ni el dominio común.

Sea Q:(0,infinito)->H C² en norma, no idénticamente nula, con valores en un dominio lineal común D de E1,E2 simétricos. Sean b1,b2>0 distintos y a1,a2 reales. Supóngase FORCE fuerte:

    -Q''+2b_i sinh(v)Q'=-b_i a_i cosh(v)Q+E_iQ,
    i=1,2.                                             (VAR-FORCE)

Entonces NECESARIAMENTE a1=a2. Para esta conclusión sola no se necesita paridad ni extensión al origen.

**Prueba.** Con Delta=b2-b1, definir

    alpha=(b2 a2-b1 a1)/(2Delta),
    B=(E2-E1)/(2Delta), C=2b1 B-E1,
    beta=b1 b2(a1-a2)/Delta.

B,C son simétricos sobre D. Restar y sustituir(VAR-FORCE) da

    sinh(v)Q'+alpha cosh(v)Q=BQ,
    Q''=CQ+beta cosh(v)Q.                               (VAR-SYS)

Poner w=logtanh(v/2)<0, q(w)=(sinh v)^alpha Q(v). Entonces q_w=Bq. Por simetría de B, como en§12.2, <q(w),q(z)>=F(w+z), con F real C². El cálculo de la segunda derivada es

    Q''/(sinh v)^(-alpha)
       =sinh²(w) q_ww+(2alpha+1)sinh(w)cosh(w) q_w
                       +[alpha(alpha+1)sinh²(w)+alpha²]q.

Como cosh v=-coth w, la simetría de C aplicada a(VAR-SYS), y las identidades de diferencias hiperbólicas, dan para w!=z y s=w+z

    sinh(s)[F''(s)+alpha(alpha+1)F(s)]
       +(2alpha+1)cosh(s)F'(s)
       = beta F(s)/(sinh(w)sinh(z)).                    (VAR-ID)

No se aplica B o C a una derivada de Q; las derivadas se toman sólo en su kernel C². Para s<0 fijo, se puede variar d=w-z con |d|<-s. El denominador es

    sinh(w)sinh(z)=[cosh(s)-cosh(d)]/2>0,

que toma valores distintos para dos d no nulos de distinto valor absoluto. El lado izquierdo de(VAR-ID) depende sólo de s. Por tanto beta F(s)=0 para cada s<0. Como Q no es idénticamente nula, existe w0 con F(2w0)=||q(w0)||²>0. Así beta=0 y a1=a2.

**Consecuencia para theta y alcance.** Si además Q es par C² hasta0 y una observación lineal continua produce q_theta, la igualdad a1=a2 reduce exactamente a§12.3, que da contradicción. Por ello, en esta construcción fuerte simétrica, una deriva escalar arbitraria a(b) tampoco permite la observación theta: ya dos escalas bastan para forzar igualdad de sus valores. No se supone continuidad de a(b).

Como corolario, una multiplicación escalar REAL no nula g(r), C² e independiente de nu, en la MISMA coordenada r=log(b/a), tampoco puede transformar esta Y en Z=gY con Z_rr=[nu²+V(r)]Z y V simétrico en el dominio común: al deshacerla aparecen la deriva escalar -2g'/g y E=V-g''/g-b²I. Este corolario presupone, como las secciones anteriores, la justificación de FORCE desde las integrales; no la obtiene formalmente para operadores no acotados. No excluye deriva verdaderamente operatorial, cambio de coordenada con peso espectral variable, métricas variables, prefactores dependientes de b, observaciones no continuas u otras representaciones. Sin signo global, nueva ventanaT, cómputos o cambios en papers.


**Control del alcance operatorial de§12.4 (2026-11-06).** Construcción new_structural_sign, comprobación algebraica independiente root. Consulta dirigida de los tres índices y§§12.1–12.4. La reducción escalar NO se extiende automáticamente a un operador D simétrico en sinh(v)Q'+cosh(v)DQ=BQ, Q''=CQ. Un ejemplo exacto es

    Q(v)=(1,2cosh v), C=diag(0,1), D=diag(-4,-1),
    B=[[0,-2],[-2,0]].

La primera identidad tiene ambos lados (-4cosh v,-2); la segunda es inmediata. B,C,D son simétricos y [B,D]!=0, con dominios completos en dimensión2. El kernel K=<Q(v),Q(z)> sigue satisfaciendo K_vv=K_zz, pero la otra identidad contiene L=<DQ(v),Q(z)>:

    sinh(v)K_v-sinh(z)K_z+(cosh(v)-cosh(z))L=0.

No se puede sustituir L por alpha K. Este ejemplo no contiene q_theta, de modo que no contradice§12.1 ni prueba una oportunidad positiva para theta. Para Y_rr=(b²+nu²)Y+2DY_r+(-C+2bB)Y, el gauge Z=exp(-rD)Y deja V=b²I+D²+exp(-rD)(-C+2bB)exp(rD). Sus entradas cruzadas son -4b exp(3r) y -4b exp(-3r): el potencial no es simétrico en la métrica usual salvo r=0. Por tanto no se obtiene un Green positivo de este ejemplo. No se descartan otras métricas ni el drift operatorial general; faltan su construcción compatible, semiboundedness y la identidad de traza que represente el núcleo objetivo. Sólo se verifica el alcance del descarte escalar, sin signo global, cómputos o cambios en papers.


**Métrica local para el ejemplo anterior: reparación imposible (2026-11-06).** Root, auditoría independiente new_structural_sign PASS. Cotejo dirigido las reglas del proyecto/tres índices/§12.4: se decide la reparación por métrica para ESE ejemplo, no para otros sistemas. Para L=-partial_r²+2D partial_r+b²I+E(b), con D,E simétricos y D constante, una métrica matricial Hermitiana M(r)>0 de clase C² hace L formalmente simétrico sobre tests compactos si y sólo si

    M'=-DM-MD,             [E(b)+D²,M]=0.

Las condiciones se obtienen comparando los coeficientes de primera derivada y de orden cero tras integrar por partes. La primera fuerza M=exp(-rD)M0 exp(-rD), M0>0 constante. En el gauge Z=exp(-rD)Y la segunda equivale a M0V=V* M0, con V=b²I+D²+exp(-rD)E exp(rD).

Para el ejemplo Q=(1,2coshv), D=diag(-4,-1), C=diag(0,1), B con entradas cruzadas -2, escribir M0=[[a,c],[conj(c),d]]. Aquí V tiene diagonales b²+16,b² y entradas cruzadas -4bexp(3r),-4bexp(-3r). La condición Hermitiana impone c real y

    -4ab exp(3r)+4db exp(-3r)-16c=0.

Como b=a0exp(r), a0>0, las funciones exp(4r), exp(-2r),1 son linealmente independientes en cualquier intervalo abierto. Fuerzan a=d=c=0, incompatible con M0>0. No existe por tanto tal métrica LOCAL matricial positiva para este ejemplo, ni siquiera en un intervalo abierto. No se modifica el coeficiente principal -I ni se añade una conexión nueva. No se excluyen métricas no locales u otros B,C,D; no se infiere semiboundedness o signo global. Sin cómputos ni cambios en papers.


**Actualización de comparación, 2026-11-06.** GLOBAL, «Cierre de la comparación hiperbólica pequeña», refuta K_Phi>=epsilon K_(2pi) para todo epsilon>0 mediante el primer modo de H y una integral theta física certificada. Esto no altera la positividad del modelo probada aquí ni excluye otros modelos; signo global OPEN. Véanse prueba, tres auditorías y certificado reproducible allí.


### 12.5. La deriva operatorial determina también un kernel de ondas

**PROVED en la clase regular declarada, 2026-11-07.** Construcción root, comprobación independiente paired_kernel_fresh, auditoría new_structural_sign PASS. Cotejo dirigido all3 y§12.4: allí consta la ecuación para el kernel con inserción D; aquí se resuelve esa ecuación sin sustituir D por un escalar. Esa es la diferencia explícita frente a los descartes escalares. No se afirma prioridad mundial ni positividad de theta.

Sea Q:R->H par, C4 en norma. Suponer Q(v) en un dominio común de operadores simétricos B,C,D, que v->DQ(v) es continuo en norma, y

    Q''(v)=C Q(v),
    sinh(v)Q'(v)+cosh(v)D Q(v)=B Q(v).

Poner K(v,z)=<Q(v),Q(z)>, F(t)=K(t,0), L(v,z)=<DQ(v),Q(z)>. L es un kernel Hermitiano con inserción de un operador simétrico; NO se presupone PSD de L ni positividad de D.

La simetría de C da K_vv=K_zz y la paridad da K_z(v,0)=0. La fórmula de ondas es

    K(v,z)=[F(v+z)+F(v−z)]/2.

F es par C4. La simetría de B y D da

    (cosh(v)−cosh(z))L(v,z)=sinh(z)K_z(v,z)−sinh(v)K_v(v,z).

Con X=v+z,Y=v−z, el lado derecho es

    −cosh(X/2)sinh(Y/2)F'(X)
    −sinh(X/2)cosh(Y/2)F'(Y).

Dividir por 2sinh(X/2)sinh(Y/2) prueba, fuera de las diagonales,

    L(v,z)=[G(v+z)+G(v−z)]/2,
    G(t)=−coth(t/2)F'(t),   G(0)=−2F''(0).

La singularidad es removible: F'(t)/t=integral_0^1 F''(st)ds, de clase C2, y coth(t/2)−2/t es suave impar cerca0. Por tanto G es par C2. La continuidad de L extiende la identidad a v=±z. En particular

    L_vv=L_zz.

**Lectura operatorial sólo bajo hipótesis adicionales.** Si también Q(v) pertenece a Dom(DC), DQ(v) a Dom(C), y v->Q(v) es C2 en norma de grafo de D (de modo que (DQ)''=DQ''), la igualdad de ondas implica

    <DCQ(v),Q(z)>=<DQ(v),CQ(z)>=<CDQ(v),Q(z)>.

Así <[D,C]Q(v),Q(z)>=0 para todo v,z. Sin densidad del span de Q no se deduce anulación vectorial del conmutador; aun con ella no se deduce conmutación fuerte de operadores no acotados. No se aplican operadores a derivadas sin estas hipótesis.

**Alcance.** El segundo kernel no es un dato libre: queda determinado por F y satisface otra ecuación de ondas. Esto restringe una construcción operatorial compatible, pero NO realiza B,C,D para theta, NO produce una métrica ni un Green positivo y NO firma A. El ejemplo anterior Q=(1,2cosh v) cumple la fórmula: F=1+4cosh v, G=−4(1+cosh v), L=−4−4cosh v cosh z. La posibilidad operatorial general sigue OPEN. Sin web, cómputos numéricos ni modificaciones de papers.


### 12.6. Realización operatorial explícita con observación theta exacta

**PROVED como realización, no como signo, 2026-11-07.** Diseño root/global_constructive_rethink, auditoría independiente new_structural_sign PASS y revisión root. Consultados las reglas del proyecto, all3, §§12.4–12.5 y GLOBAL. Diferencia concreta: §12.5 sólo imponía identidades necesarias a Q,B,C,D; aquí se construyen esos objetos, sus dominios y una observación continua exactamente theta. No se usa deriva escalar; no se atribuye prioridad mundial. La métrica y el Green positivo siguen sin construir.

**Espacio y vectores.** Para omega>=0 poner rho(omega)=sech(pi omega/2), y lambda_j=j+1/4, j=0,1,2. Trabajar en el espacio real

    H=L²((0,infinito),rho(omega)domega) directa R³,
    Q(v)=(cos(omega v), cosh(lambda_0 v),cosh(lambda_1 v),cosh(lambda_2 v)),
    F(t)=sech(t)+sum_(j=0)^2 cosh(lambda_j t).

La fórmula coseno integral_0^infinito rho(omega)cos(omega t)domega=sech(t) tiene normalización integral rho=1. Las identidades de producto dan

    <Q(v),Q(z)>=[F(v+z)+F(v-z)]/2.

Q es par y C^infinito en norma. Definir C como multiplicación por -omega² en el continuo y por lambda_j² en las masas, en su dominio máximo; es autoadjunto y Q''=CQ.

**Construcción de D.** Definir G(t)=-coth(t/2)F'(t), con la singularidad removida. Las identidades

    -coth(t/2)(sech t)'=sech t+sech²t,
    coth(t/2)sinh(t/4)=cosh(t/4)-(1/2)sech(t/4),
    coth(t/2)sinh(5t/4)=cosh(5t/4)+2cosh(t/4)-(1/2)sech(t/4),
    coth(t/2)sinh(9t/4)=cosh(9t/4)+2cosh(5t/4)+2cosh(t/4)-(1/2)sech(t/4)

dan G con masas (-29/4,-23/4,-9/4) y densidad coseno

    sigma(omega)=rho(omega)+omega/sinh(pi omega/2)+(15/2)sech(2pi omega).

Se usan integral_0^infinito [omega/sinh(pi omega/2)]cos(omega t)domega=sech²t y la fórmula escalada de sech. Todas son integrales absolutamente convergentes (también en omega=0 por continuidad).

Por ello definir D en su dominio máximo como el multiplicador

    d(omega)=sigma/rho
      =1+omega coth(pi omega/2)+(15/2)cosh(pi omega/2)/cosh(2pi omega)

junto con las tres masas anteriores. D es autoadjunto, d=O(1+omega), y

    <DQ(v),Q(z)>=[G(v+z)+G(v-z)]/2.

Las colas exponenciales de rho justifican todas las derivadas en las normas de grafo de C,D,CD,DC. En esta realización concreta C y D son multiplicadores simultáneos y DCQ=CDQ; esto no se infiere de una conmutación débil abstracta.

**Construcción y dominio de B.** Sea S=span{Q(v):v>=0}. Definir linealmente

    BQ(v)=sinh(v)Q'(v)+cosh(v)DQ(v).

Está bien definido: para v_i distintos no negativos, una relación finita entre Q(v_i) implicaría sum c_i cos(omega v_i)=0 en un intervalo de omega, y la independencia de exponenciales fuerza c_i=0. Para probar densidad de S, un vector ortogonal a todos Q(v) daría una transformada coseno acotada (Cauchy–Schwarz y integral rho=1) más tres cosh de tasas distintas positivas. El crecimiento cuando v->infinito elimina sucesivamente las tres masas; la unicidad de Fourier elimina el componente continuo.

Las identidades K,L de§12.5, verificadas aquí mediante F,G explícitos, dan

    <BQ(v),Q(z)>=<Q(v),BQ(z)>.

Así B es densamente definido y simétrico sobre S, y por tanto clausurable. No se declara autoadjunto. S está contenido en los dominios de C,D y contiene todos los Q(v); no se supone invariancia de S por C o D.

**Observación exacta, incluyendo toda la cola theta.** Poner

    q_theta(t)=Phi(t/2) exp(2pi cosh t),
    d_(9/4)=2pi², d_(5/4)=2pi³-3pi, d_(1/4)=pi^4-3pi²,
    H_theta(t)=q_theta(t)-2sum_j d_(lambda_j)cosh(lambda_j t).

En cada substrip |Im t|<=b<pi/2, el modo n=1 da, para Re t->infinito,

    q_theta(t)=2pi²exp(9t/4)+(2pi³-3pi)exp(5t/4)
                   +(pi^4-3pi²)exp(t/4)+O_b(exp(-3Re t/4)).

Los modos n>=2 tienen el factor exp(-pi(n²-1)exp(t)) y se acotan uniformemente por una cola superexponencial en esos substrips. La paridad trata el otro extremo. Al restar los cosh se añaden sus ramas decrecientes, por lo que la cota CORRECTA es

    H_theta(t)=O_b(exp(-|Re t|/4)),

no exp(-3|Re t|/4). H_theta es par, real sobre R y holomorfa en |Im t|<pi/2.

Con la convención k(omega)=pi^(-1)integral_R H_theta(t)exp(-i omega t)dt, inversión Fourier da H_theta(v)=integral_0^infinito k(omega)cos(omega v)domega. Desplazar el contorno a Im t=-pi/3 para omega>=0 (las caras verticales desaparecen por la cota anterior) prueba |k(omega)|<=C exp(-pi omega/3). En consecuencia

    integral_0^infinito |k|²/rho < infinito,

pues el integrando es O(exp(-pi omega/6)). El vector h=(k/rho, 2d_(lambda_0),2d_(lambda_1),2d_(lambda_2)) pertenece a H y define una observación continua exacta

    <Q(v),h>=q_theta(v),  v real.

**Alcance estricto.** Se han realizado Q,B,C,D y la observación theta, incluidos los dominios requeridos por§12.5. No se construyó una métrica que haga positiva la energía completa, ni una identidad Green positiva que reproduzca A. La observación escalar no transfiere automáticamente positividad del Gram de Q al kernel objetivo. Global OPEN. Sin web, cómputos numéricos ni cambios en papers.


**Realización integral y ecuación fuerte (mismo resultado, auditoría independiente PASS).** Para b>0, nu real y r=log b, definir

    Y_nu(b)=integral_0^infinito exp(-b cosh v)cosh(nu v)Q(v)dv.

Las normas de Q,Q',CQ,DQ,BQ están acotadas por C exp(13v/4), aumentando C cuando sea necesario. La superamortiguación exp(-b cosh v) permite integrar en los grafos de C,D y de la clausura Bbar; sumas de Riemann en S justifican el paso al grafo cerrado de Bbar. También permite todas las derivadas en b localmente en b>0 y en los grafos requeridos. No se supone que la suma de operadores sea autoadjunta.

Poner w=exp(-b cosh v). Dos integraciones por partes transfieren la segunda derivada de cosh(nu v) a wQ. Los bordes en0 desaparecen porque Q'(0)=w'(0)=(cosh(nu v))'_(v=0)=0, y en infinito por la misma superamortiguación. Así

    nu²Y=CY-2b integral w sinh(v)Q'(v)cosh(nu v)dv
             +integral w[b²sinh²(v)-b cosh(v)]Q(v)cosh(nu v)dv.

Por otro lado Y_rr tiene integrando w[b²cosh²(v)-b cosh(v)]Q(v)cosh(nu v). Sustituir sinh(v)Q'=BQ-cosh(v)DQ prueba la igualdad fuerte

    Y_rr=(b²+nu²)Y+2D Y_r+(-C+2b Bbar)Y.

La observación continua construida arriba cumple exactamente

    <Y_nu(2pi),h>=integral_0^infinito Phi(v/2)cosh(nu v)dv=Z(2nu),
    Z(a)=integral_R exp(at)Phi(t)dt.

Por tanto la realización reproduce el dato theta completo y su ecuación, con dominios e intercambios justificados. Sigue faltando una métrica y una identidad Green POSITIVA que firmen A; esta igualdad no las demuestra. Revisión root y new_structural_sign PASS.


### 12.7. La realización12.6 no admite una métrica local positiva acotada compatible

**PROVED en la clase declarada, 2026-11-07.** Construcciones independientes root/global_constructive_rethink, auditoría new_structural_sign PASS de límites de grafo, coeficientes y alcance. Consultados all3 y§12.4. Allí se descartó una métrica para un ejemplo de dimensión2 sin observación theta; aquí se estudia la realización exacta12.6, en dimensión infinita, y NO se impone diagonalidad de la métrica. El mecanismo de comparar exponentes tiene antecedente12.4; no es una herramienta nueva.

**Clase.** M(r) es un operador autoadjunto acotado estrictamente positivo en H para cada r de un intervalo abierto I, con regularidad local en norma de operador suficiente para las integraciones por partes (C² basta). No se exige inversa acotada ni conmutación con C o D. Se buscan métricas para el operador de12.6, con coeficiente principal -I y sin añadir conexiones, que satisfagan las condiciones necesarias de compatibilidad, en formas sobre S y sus límites de grafo:

    M'=-DM-MD,
    E(r)=-C+D²+2b Bbar es simétrico en el producto M(r),
    b=b_0 exp(r), b_0>0.

La primera igualdad se entiende débilmente: <M' u,v>=-<M Du,v>-<M u,Dv>. La segunda es <M Eu,v>=<M u,Ev>, sin aplicar E a Mu. Estas son las condiciones de§12.4 derivadas por integración por partes, cuando los productos y límites están justificados; la prueba siguiente demuestra directamente que no hay M que las satisfaga. No se extiende el enunciado a métricas no acotadas o no locales en r.

**Dos vectores accesibles en el grafo.** Escribir e_j para los tres vectores discretos. La fórmula explícita de BQ(v) tiene parte continua de norma O(exp v), porque omega y d(omega) pertenecen a L²(rho). Sus tres coordenadas son

    (BQ)_0=-(7/2)cosh(5v/4)-(15/4)cosh(3v/4),
    (BQ)_1=-(9/4)cosh(9v/4)-(7/2)cosh(v/4),
    (BQ)_2=-(9/4)cosh(5v/4).

Dividir Q(v) por cosh(9v/4) y pasar v->infinito prueba en el grafo conjunto de Bbar,C,D² que

    e_2 pertenece a Dom(Bbar), Bbar e_2=-(9/4)e_1.

Después restar cosh(9v/4)e_2 y dividir por cosh(5v/4). La parte continua O(exp v) de BQ desaparece en ese límite; resulta

    e_1 pertenece a Dom(Bbar), Bbar e_1=-(7/2)e_0-(9/4)e_2.

Los vectores que usan e_2 se aproximan desde S mediante selección diagonal en los mismos grafos. Para e_0 sólo se necesita aproximación en el grafo de D, restando ambas masas mayores y dividiendo por cosh(v/4). NO se aplica B a e_0. La acotación de M,M' permite pasar las identidades métricas a esos límites.

**Contradicción sin diagonalizar M.** Los autovalores discretos de D son

    d_0=-29/4, d_1=-23/4, d_2=-9/4.

La ecuación métrica en pares e_i,e_j fuerza, escribiendo M_ij=<M e_i,e_j>,

    M_ij(r)=m_ij exp(-(d_i+d_j)r).

Además (-C+D²)e_1=(63/2)e_1 y (-C+D²)e_2=0. Por tanto

    E e_2=-(9/2)b e_1,
    E e_1=(63/2)e_1-7b e_0-(9/2)b e_2.

La simetría de E aplicada al par e_2,e_1 da exactamente

    b[-9M_11+14M_20+9M_22]-63M_21=0.

Tras sustituir la solución para M_ij, los exponentes de r de los cuatro términos son, respectivamente, 25/2,21/2,11/2,8. Son distintos, de modo que su independencia lineal en cualquier intervalo abierto obliga m_11=m_22=0 (también anula los otros dos coeficientes). Esto contradice <M e_j,e_j>>0. Las entradas que mezclan continuo y masas no se han supuesto nulas: simplemente no intervienen en este par de identidades.

**Alcance.** La realización exacta12.6 sigue siendo válida. Lo que falla es convertir SU ecuación, con el coeficiente principal y la conexión declarados, en una energía simétrica mediante una métrica local positiva acotada de esta clase. No se excluyen métricas no locales, métricas no acotadas con otros dominios, conexiones nuevas ni otras realizaciones. No se obtiene negatividad de A ni signo global. Sin web, cómputos numéricos o cambios en papers.


## 13. Productos cosh desplazados: la cota real fuerza extensión entera

2026-11-07. **PROVED en la clase declarada; auditoría matemática independiente shifted_cosh_gate PASS y revisión root PASS.** Construcción root; filtro previo de novedad por shifted_cosh_gate PASS tras cotejo dirigido de Paper48, los tres índices y primarias. Antecedentes: §§11–11.4 (productos sin desplazamientos) y §12.3 (cúspide par). Permitir c variable elimina el obstáculo de multiplicidad entera de§11.3. La diferencia examinada es la clausura de esta clase ampliada; el argumento siguiente usa normalidad holomorfa en lugar de clasificar todos los productos límite. No se atribuye novedad mundial al principio de compactitud ni a la cúspide.

**Clase.** Para cada n, sea

    Q_n(z)=prod_(j=1..m_n) (cosh(b_nj z)-c_nj)/(1-c_nj),
    b_nj>0, -1<c_nj<1, m_n finito.

Se permiten productos vacíos. Si Q_n converge uniformemente en compactos reales a Q, entonces Q es la restricción de una función entera. En particular no puede ser

    q_theta(t)=Phi(t)/Phi(0) * exp[2pi(cosh(2t)-1)].       (SHIFTED-Q)

**1. Una sola cota real controla todos los factores.** La convergencia implica Q_n(1)<=M para algún M>=1, uniforme en n. Poner

    d_nj=(cosh(b_nj)-1)/(1-c_nj)>=0.

Como prod_j(1+d_nj)>=1+sum_j d_nj, resulta sum_j d_nj<=M-1. Además 1-c_nj<2 implica cosh(b_nj)-1<=2(M-1). Por tanto b_nj<=B:=arcosh(2M-1). Si M=1, todos los productos son vacíos y la conclusión es inmediata.

**2. Cota compleja uniforme.** Para |z|<=R y 0<b<=B, la serie de cosh da

    |cosh(bz)-1| <= (b²R²/2)cosh(BR),
    cosh(b)-1 >= b²/2.

Por consiguiente, con C_R=R²cosh(BR),

    |Q_n(z)| <= prod_j(1+C_R d_nj)
               <= exp[C_R(M-1)].                       (ENTIRE-BOUND)

No se necesita que 1-c_nj esté separado de cero: su efecto ya está incluido en d_nj.

**3. Límite entero e identificación.** La cota en cada disco y las cotas de Cauchy dan una subsucesión que converge uniformemente en todo compacto complejo a una función entera F (extracción diagonal en discos). En el eje real F=Q por la convergencia supuesta. Basta esta subsucesión; no se presume convergencia compleja a partir de convergencia real sin la cota anterior.

**4. Incompatibilidad específica con theta.** SHIFTED-Q es holomorfa en |Im t|<pi/4. Si coincidiera allí con una función entera, el principio de identidad prolongaría la igualdad desde el eje real. Tomar

    Z=log(2)+iY, t=Z/2, Y->pi/2 desde abajo,
    w=exp(Z)=2i+zeta.

La expansión de la cúspide par ya probada en§12.3, con su fuente Poisson en GLOBAL, da

    Phi(Z/2)=w^(5/4)[(3i/2)zeta^(-5/2)+E(zeta)],
    |E(zeta)|<=C |zeta|^(-K) exp(-beta/|zeta|), beta>0,

en el sector que contiene este camino. Su módulo diverge. El factor exp[2pi(cosh Z-1)] tiene límite finito no nulo y Phi(0)>0. Así |q_theta(Z/2)| diverge al acercarse al punto FINITO (log2)/2+i pi/4, lo que contradice que F sea entera.

**Consecuencia para aproximantes del perfil.** No existe sucesión

    phi_n(t)=C_n exp[-2pi cosh(2t)] Q_n(t), C_n>0,

que converja a Phi uniformemente en compactos reales. En efecto phi_n(0)=C_n exp(-2pi) converge a Phi(0)>0; dividir por este valor y retirar la base fija produciría Q_n->q_theta. También quedan excluidos productos infinitos de esta clase definidos como límites localuniformes de sus productos parciales.

**Alcance.** Sólo escala base FIJA 2pi, factores reales con b>0 y -1<c<1, productos finitos o su clausura localuniforme real. No se decide si un factor aislado conserva PSD de A_phi. No se excluyen escalas base variables, otros multiplicadores, sumas, cocientes, potencias reales o comparaciones de formas. Es un descarte de esta aproximación antes de invertir trabajo en conservación de signo; no prueba A negativo, no firma A y no amplía T. Sin cómputos numéricos, web ni cambios en papers.


### 13.1. La escala positiva variable también queda acotada

2026-11-07. **PROVED en la clase declarada; auditoría independiente shifted_cosh_gate PASS y revisión root PASS.** Root; filtro previo shifted_cosh_gate PASS tras cotejo dirigido de all3/Paper48 y primarias. Diferencia frente§13: permitir a_n->infinito destruye su cota inicial Q_n(1). La desigualdad de tres valores siguiente controla ese escape sin presuponer convergencia de derivadas.

**Enunciado.** Tampoco existe aproximación localuniforme real de Phi por

    phi_n(t)=C_n exp[-a_n cosh(2t)] Q_n(t), C_n>0, a_n>0,

con los mismos productos Q_n de§13, aunque a_n varíe sin cota previa.

**1. Concavidad en el cuadrado de la variable.** Para -1<c<1 definir f_c(x)=log[(cosh x-c)/(1-c)]. En x>0,

    x f_c''(x)-f_c'(x)
      =[x-sinh(x)cosh(x)+c(sinh(x)-x cosh(x))]/(cosh(x)-c)².

Como sinh(x)-x cosh(x)<0, el numerador es menor o igual que su valor en c=-1, que es (1+cosh x)(x-sinh x)<0. Por la regla de la cadena, la segunda derivada de f_c(b sqrt(s)) tiene el signo de x f_c''(x)-f_c'(x), x=b sqrt(s), para s>0. En s=0 la extensión es suave por la serie par y 1-c>0. Así s->log Q_n(sqrt(s)) es cóncava en [0,infinito).

**2. Tres valores acotan la escala.** Poner H(s)=cosh(2sqrt(s)) y

    delta=H(0)+H(2)-2H(1)>0.

La positividad estricta sigue de H(s)=sum_(k>=0) 4^k s^k/(2k)!: los términos k=0,1 tienen diferencia cero y los k>=2 tienen diferencia positiva. Con L_n(s)=log phi_n(sqrt(s)), la concavidad anterior da

    L_n(0)+L_n(2)-2L_n(1) <= -a_n delta,
    0<a_n<=[2L_n(1)-L_n(0)-L_n(2)]/delta.              (SCALE-BOUND)

Si phi_n->Phi localuniformemente real, sus valores en 0,1,sqrt(2) convergen a valores positivos. Por tanto el lado derecho permanece acotado y existe A<infinito con 0<a_n<=A para todo n. No se deriva la convergencia de phi_n.

**3. Recuperación de normalidad y contradicción.** Como Q_n(0)=1,

    Q_n(1)=phi_n(1)/phi_n(0) * exp[a_n(cosh2-1)],
    C_n=phi_n(0)exp(a_n).

Ambas sucesiones están acotadas. La cota ENTIRE-BOUND de§13 vuelve a dar acotación local compleja de Q_n. Además, en |z|<=R,

    |exp[-a_n cosh(2z)]|<=exp[A cosh(2R)].

En consecuencia phi_n es una familia entera localmente acotada. Una subsucesión converge en compactos complejos a una función entera que coincide con Phi sobre R. La cúspide par en (log2)/2+i pi/4, usada en§13, contradice esa extensión. Esto prueba el enunciado.

**Alcance actualizado.** Se retira la reserva de§13 únicamente para escalas POSITIVAS a_n variables en la MISMA base cosh(2t), con factores y convergencia declarados. No cubre cambios de frecuencia de esa base, parámetros c fuera de(-1,1), otros factores, sumas, cocientes, potencias reales o comparaciones de formas. No decide conservación de PSD por factores ni signo de A. Sin cómputos numéricos, web, nueva ventanaT ni cambios en papers.
