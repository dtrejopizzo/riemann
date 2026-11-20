# POWER_RECIPROCAL_PFAFFIANS_083 — Factorización exacta en todos los órdenes

Estado: **PROVED como identidad algebraica, auditoría independiente aprobada.** Véase `POWER_RECIPROCAL_PFAFFIANS_AUDIT_083.md`. Se factoriza el determinante del kernel completo en un producto de dos Pfaffianos, con borde de unos en orden impar. No se afirma signo de esos factores para la Phi real, ni se cierra W. Papers intactos.

## 1. Consulta, atribución y diferencia

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados SCHUR003,074,079,081 y082. La búsqueda Pfaffian/Pfaff y anti-Löwner en los tres índices y SCHUR003 no encontró esta especialización.082 factoriza órdenes dos y tres; aquí se demuestra la fórmula en tamaño arbitrario, no se extrapola un signo desde esos tamaños.

El álgebra de Pfaffianos es clásica, no una herramienta de nueva invención. Primarias consultadas:

* [Okada, Pfaffian Formulas and Schur Q-Function Identities, §2](https://arxiv.org/html/1706.01029): congruencia y expansión de Laplace de Pfaffianos.
* [Knuth, Overlapping Pfaffians, §6](https://lab.cycu.org/downloads/1995_Overlapping_Pfaffians.pdf): antecedentes de Cayley que factorizan determinantes casi antisimétricos en productos de Pfaffianos.
* [Ishikawa–Okada–Tagawa–Zeng, Generalizations of Cauchy's Determinant and Schur's Pfaffian](https://arxiv.org/abs/math/0411280): contexto de las identidades generalizadas de Cauchy y Schur.

No se reclama novedad mundial de la especialización; se registra su ausencia en el corpus consultado y su prueba autocontenida. También se encontró [Audenaert, A Characterisation of Anti-Löwner Functions](https://arxiv.org/html/1008.2943), que estudia exactamente kernels de sumas divididas en todos los órdenes. Su representación integral positiva no se ha demostrado para M real y no se toma como una solución del signo.

## 2. Enunciado y convenciones

Sean u_i>0 y F_i>0, i=1,...,n. No se necesitan monotonía, concavidad, ni una función subyacente diferenciable. Poner

    K_ij=(F_i+F_j)/(u_i+u_j),
    R_i=u_i/F_i, S_i=u_iF_i=u_i²/R_i,
    (A_R)_ij=(R_j−R_i)/(u_i+u_j),
    (A_S)_ij=(S_j−S_i)/(u_i+u_j).

Las diagonales de A_R,A_S son cero. Usar la convención Pf([[0,a],[-a,0]])=a y Pf de la matriz vacía igual a1. Para una matriz antisimétrica A de tamaño n, definir

    P_n(A)=Pf(A),                         n par,
    P_n(A)=Pf([[A,e],[-e^t,0]]),           n impar,

donde e es el vector de n unos y el borde se coloca al FINAL. Entonces, para TODO n>=1,

    det K=P_n(A_R)P_n(A_S)/(producto_i R_i).       (ALL-ORDERS)

El producto y su signo no dependen del orden elegido de los nodos: permutarlos cambia ambos Pfaffianos por el mismo signo. Nodos coincidentes tampoco dañan la identidad algebraica. Para interpretar una aplicación con F como función, naturalmente sus valores coincidentes deben coincidir.

## 3. Dos identidades de desplazamiento

Escribir D=diag(u_i), E=diag(R_i), r=(R_i), u=De, A=A_R y T=EKE. Entrada por entrada se verifican

    T=DA+r e^t,
    E A_S E=DAD+r u^t−u r^t.                     (DISPLACEMENT)

En la primera, (DA+r e^t)_ij=u_i(R_j−R_i)/(u_i+u_j)+R_i=(u_iR_j+u_jR_i)/(u_i+u_j). En la segunda, multiplicar por u_i+u_j reduce la igualdad a

    R_i u_j²−R_j u_i²
      =u_i u_j(R_j−R_i)+(R_i u_j−u_iR_j)(u_i+u_j).

Ambas incluyen correctamente las diagonales. Además det T=(producto R_i)² det K.

## 4. Lemas elementales de Pfaffianos

Se usan Pf(A)²=det A, la congruencia Pf(QAQ^t)=det(Q)Pf(A) y la expansión por una fila. Estas propiedades clásicas también se deducen directamente de la definición por emparejamientos.

### 4.1 Actualización de rango dos

Si V es antisimétrica par e invertible, y a,b son vectores, entonces

    Pf(V+a b^t−b a^t)=Pf(V)[1+b^t V^(-1)a].        (UPDATE)

Una justificación breve que fija el signo: el Pfaffiano de V+t(ab^t−ba^t) es afín en t. En la expansión multilineal, dos copias de la forma descomponible a∧b se anulan. Su valor en0 es Pf(V). Derivar el cuadrado del Pfaffiano en0, usando el determinante, da para su coeficiente lineal

    Pf(V)·tr[V^(-1)(ab^t−ba^t)]/2
       =Pf(V)b^t V^(-1)a.

Esto prueba UPDATE, no sólo su cuadrado.

### 4.2 Cofactores impares

Para A antisimétrica de tamaño impar n, definir

    v_i=(−1)^(i+1)Pf(A con fila y columna i eliminadas).

La expansión de Laplace prueba

    A v=0,
    Pf([[A,b],[-b^t,0]])=b^t v,
    adj(A)=v v^t.                                 (ODD-COFACTORS)

Para la última igualdad, primero considerar rango n−1. El adjunto es simétrico, sus columnas pertenecen al núcleo unidimensional generado por v, y sus diagonales son los cuadrados v_i² por la identidad par. Esto fija adj(A)=vv^t. Si el rango es menor, todos los menores de tamaño n−1 y todos los v_i se anulan. Así la igualdad vale también en ese borde, incluido n=1 con Pf vacía igual a1.

### 4.3 Borde que elimina una actualización

Para cualquier V antisimétrica impar y vectores r,u,

    Pf([[V+r u^t−u r^t,r],[-r^t,0]])
       =Pf([[V,r],[-r^t,0]]).                      (BORDER)

En efecto la matriz de la izquierda es Q[[V,r],[-r^t,0]]Q^t con Q=[[I,u],[0,1]], de determinante1. Esta congruencia fija el signo del borde y no exige ninguna inversa.

## 5. Prueba en orden par

Suponer primero A invertible. La primera identidad DISPLACEMENT y el lema del determinante de rango uno dan

    det T=det D·det A·[1+e^t A^(-1)D^(-1)r].

Poner V=DAD. UPDATE, con a=r,b=u, y la segunda identidad DISPLACEMENT dan

    Pf(E A_S E)
       =Pf(DAD)[1+u^t(DAD)^(-1)r]
       =det D·Pf(A)[1+e^t A^(-1)D^(-1)r].

Como det A=Pf(A)², resulta

    det T=Pf(A)Pf(E A_S E)
         =(producto R_i)Pf(A_R)Pf(A_S).

Dividir por (producto R_i)² prueba ALL-ORDERS en tamaño par.

No se excluyen los datos con A singular. Multiplicar por los denominadores no nulos convierte la identidad en una igualdad polinómica; vale en el conjunto genérico donde A es invertible y por continuidad en todo el dominio. Para nodos positivos distintos, ese conjunto es denso: la elección R_i=u_i da la matriz de Schur, cuyo Pfaffiano es producto_(i<j)(u_j−u_i)/(u_i+u_j), no nulo (fórmula clásica de Schur, Okada citado en§1, Proposición2.2, ecuación(2.7)). Después, nodos coincidentes se obtienen por continuidad. Es un paso algebraico de extensión, no una hipótesis adicional de no degeneración.

## 6. Prueba en orden impar

Ahora det A=0. El lema del determinante de rango uno, válido mediante el adjunto aunque DA sea singular, y ODD-COFACTORS dan

    det T=e^t adj(DA)r
         =det D·e^t adj(A)D^(-1)r
         =det D·(e^t v)(v^t D^(-1)r).              (ODD-DET)

El primer factor escalar es P_n(A_R). Aplicar BORDER a V=DAD y bordear la segunda identidad DISPLACEMENT con r. Se obtiene

    Pf([[E A_S E,r],[-r^t,0]])
       =Pf([[DAD,r],[-r^t,0]]).

La congruencia diag(E,1) en el lado izquierdo y diag(D,1) en el derecho da

    (producto R_i)P_n(A_S)
       =det D·Pf([[A,D^(-1)r],[-r^tD^(-1),0]])
       =det D·v^tD^(-1)r.

Sustituir en ODD-DET produce

    det T=(producto R_i)P_n(A_R)P_n(A_S).

Dividir por (producto R_i)² demuestra ALL-ORDERS impar, incluidos los casos singulares y n=1. No se introducen factores u_i adicionales en la fórmula final.

## 7. Órdenes bajos y obligación de signo

En n=1 ambos Pfaffianos bordeados valen1 y det K=1/R1. En n=2, ALL-ORDERS es exactamente DET2 de082. En n=3, los Pfaffianos bordeados son las combinaciones de tres secantes; al normalizarlos se recupera DET3 de082. Esas comprobaciones no reemplazan las pruebas generales anteriores.

Para F=M real, la forma completa se conserva en K: el cambio de coordenadas sólo ha factorizado su determinante. No se han quitado contactos ni componentes positivos o negativos. La obligación nueva expresada por esta identidad es

    P_n(A_R)P_n(A_S)>=0
    para TODOS los conjuntos de nodos admisibles y TODOS n.

Para concluir PSD de cualquier bloque hay que satisfacer la misma condición para TODOS sus subconjuntos principales; un único determinante no basta. Un signo fijo individual de ambos factores sería suficiente, pero no se ha probado en tamaños arbitrarios. La concavidad de R,S controla exactamente el tamaño tres por082 y no se extrapola a los Pfaffianos superiores.

Así083 aporta una factorización exacta de orden no acotado, no una desigualdad nueva que pague todavía el signo completo. El dato pendiente es una comparación firmada de estos dos Pfaffianos para la Phi específica, o una representación positiva que pruebe sus signos. No hay conclusión de cuatro generadores, todos los órdenes o una nueva ventana temporal en esta fuente. Global OPEN.

## Apéndice — Jerarquía clásica de Rolle y determinantes de Taylor

Estado del apéndice: **identidades y criterio suficiente abstracto PROVED; descarga para R,S reales CONDITIONAL/OPEN; auditoría del apéndice aprobada.** No se presenta una identidad clásica como una nueva desigualdad de signo.

### A. Pfaffianos como determinantes de interpolación

Para 2k nodos positivos distintos ordenados, x_i=u_i² y f_i=f(x_i), la especialización clásica de [Ishikawa–Okada–Tagawa–Zeng, Theorem1.1(b)](https://arxiv.org/html/math/0411280) es

    Pf((f_j−f_i)/(u_i+u_j))
      =sigma_k det[1,x,...,x^(k−1),f,xf,...,x^(k−1)f]
                  /producto_(i<j)(u_i+u_j),
    sigma_k=(−1)^(k(k−1)/2).                         (INTERPOLATION-EVEN)

Se toma p=q=r=s=0 en el teorema, variables x_i=u_i², a_i=f_i y b_i=u_i. El segundo determinante generalizado tiene columnas de potencias pares de u seguidas por las impares; reordenarlas produce sigma_k y la Vandermonde usual. Esta cancela la correspondiente parte de la Vandermonde en u². La fórmula no es nueva.

Para 2k−1 nodos, el borde de unos de083 cumple

    P_(2k−1)(A_f)
      =sigma_k det[1,x,...,x^(k−1),f,xf,...,x^(k−2)f]
                  /producto_(i<j)(u_i+u_j).          (INTERPOLATION-ODD)

En k=1 el bloque con f está vacío. La fórmula impar se deduce de la par añadiendo un último nodo u_2k→infinito y asignando libremente f_2k=u_2k. Las entradas de su última columna antisimétrica tienden a1. En el determinante domina la última columna f x^(k−1), de grado2k−1 en u_2k, exactamente el grado de los nuevos factores del denominador. Su cofactor tiene signo positivo porque ocupa la última fila y columna.

### B. Una jerarquía suficiente, con todas las hipótesis explícitas

Fijar k y un intervalo de cuadrados I. Suponer f∈C^(2k−1)(I). Definir

    H_j(x)=(d/dx)^k[x^j f(x)], j=0,...,k−1,
    D_(k,j)(x)=W(H_0,...,H_(j−1))(x), j=1,...,k.

Aquí W es el Wronskiano con filas de derivadas de orden0,...,j−1. Si TODOS los D_(k,j) son no nulos en I, el sistema H_0,...,H_(k−1) es un sistema de Chebyshev extendido. La justificación es Rolle ponderado: dividir por H_0, que no se anula, y derivar elimina la primera función. Los Wronskianos restantes son los anteriores divididos por potencias no nulas de H_0. Repetir el procedimiento reduce la cota de ceros por uno en cada etapa. Así una combinación no trivial de j funciones iniciales tiene a lo sumo j−1 ceros contados con multiplicidades.

Si P_(k−1)+fQ_(k−1) tuviese2k ceros distintos, derivar k veces daría una combinación de las k funciones H_j con al menos k ceros, contradicción. Si Q fuera cero desde el inicio, el polinomio ya no podría tener tantos ceros. Por tanto el determinante de INTERPOLATION-EVEN no se anula.

Para INTERPOLATION-ODD basta D_(k,j)≠0 para j=1,...,k−1: una combinación P_(k−1)+fQ_(k−2) con2k−1 ceros daría al menos k−1 ceros después de derivar k veces, contra el sistema reducido de dimensión k−1. En k=1 la afirmación impar es directamente P_1=1.

El signo también queda fijado, no sólo la ausencia de ceros. El Wronskiano del sistema original tiene un bloque polinomial triangular, y su determinante es

    [producto_(m=0)^(k−1)m!] D_(k,k),       caso par,
    [producto_(m=0)^(k−1)m!] D_(k,k−1),     caso impar k>=2.

La cámara ordenada de nodos es conexa y el límite confluente divide por una Vandermonde positiva y factoriales positivos. Por tanto el signo del determinante de evaluación es el del D final indicado. En particular,

    sign D_(k,k)=sigma_k y D_(k,j)≠0 TODOS j<=k
       ⇒ Pf(A_f)>0 en TODOS los conjuntos de2k nodos;

    sign D_(k,k−1)=sigma_k y D_(k,j)≠0 TODOS j<k
       ⇒ P_(2k−1)(A_f)>0 en TODOS los conjuntos de2k−1 nodos.

Es un criterio suficiente global en el intervalo: comprobarlo en un punto o para un solo k no prueba los restantes.

### C. Los Wronskianos son Hankel de coeficientes de Taylor normalizados

Trasladar la base x^c a (t−x)^c al evaluar en x es una transformación triangular de determinante1. De Leibniz se obtiene exactamente

    D_(k,j)=det_((l,c)=0,...,j−1)
                [(k+l)!/(k+l−c)! · f^(k+l−c)].

Poner a_m(x)=f^(m)(x)/m!, m>=1. Factorizar (k+l)! de cada fila y revertir las columnas da

    D_(k,j)=(−1)^(j(j−1)/2)
        ·[producto_(l=0)^(j−1)(k+l)!]
        ·det_((l,c)=0,...,j−1)[a_(k−j+1+l+c)(x)].    (TAYLOR-HANKEL)

Por ejemplo,

    D_(2,1)=f'',
    D_(2,2)=3f''²−2f'f'''=−T_f,
    D_(3,2)=4f'''²−3f''f^(4).

Esto recupera el criterio concreto de084 en tamaño cuatro. No extrapola su desigualdad T_f>0 a la siguiente fila de la jerarquía.

Para la jerarquía completa suponer f suave de todos los órdenes. Una condición suficiente más estructurada sería que, para cada x, los números

    mu_m(x)=(−1)^m a_(m+1)(x), m>=0,

fueran momentos de una medida positiva en [0,infinito), con todos sus determinantes de momentos desplazados estrictamente positivos. En tal caso TAYLOR-HANKEL daría

    sign D_(k,j)=(−1)^[jk−j(j+1)/2].

Para j=k y j=k−1 este signo es sigma_k, por lo que ambas paridades quedarían cubiertas. Se declara sólo la suficiencia algebraica; no se afirma que estas secuencias del cociente theta sean momentos positivos.

Antecedente clásico adicional: las matrices de derivadas normalizadas que empiezan en a_1 aparecen en el criterio de Dobsch–Donoghue. Véase [Heinävaara, Local characterizations for the matrix monotonicity and convexity of fixed order](https://arxiv.org/abs/1608.07516). No se presenta la jerarquía Hankel abstracta como un nuevo principio de positividad.

### D. Obligación específica para la Phi real

Las coordenadas reales son cocientes, no transformadas de una única densidad positiva:

    R(x)=u/M(u)=Z(u)/Z_J(u),
    S(x)=uM(u)=u² Z_J(u)/Z(u), x=u²,
    Z_J(u)=Z'(u)/u.

Las densidades positivas J y K de076–078 aportan estructura exacta al denominador y a ciertos defectos. Su positividad NO prueba que los coeficientes normalizados de R o S sean una sucesión de momentos, ni los menores Hankel de TAYLOR-HANKEL. El paso que falta es una representación firmada o una recurrencia que preserve esos menores para AMBOS cocientes y k no acotado.

No se dispone aquí de esa recurrencia para la Phi real. Esta jerarquía explicita el dato que requeriría una inducción, pero no la sustituye; el signo global y los Pfaffianos superiores permanecen OPEN.
