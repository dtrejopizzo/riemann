# POWER_THETA_TWO_COPY_073 — Concavidad de la media inclinada mediante dos copias

Estado: **PROVED/APROBADO**, incluida la aplicación theta y el corolario de dos generadores; auditoría independiente en [POWER_THETA_AUDIT_073.md](POWER_THETA_AUDIT_073.md). La verificación compacta se incorpora por POWER_THETA_HAZARD_COMPACT_073. Papers intactos. No se afirma signo global de W.

## 1. Corpus y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid maestro R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos CONE001 y `phase-103-direct-a1-closure/103_43_THETA_HAZARD_CONVEXITY_GATE.md`, con sus antecedentes de covarianzas, cumulantes y medidas inclinadas. La positividad de una medida par y su logconvexidad no bastan para el bound superior del criterio de dos generadores: CONE001§4 contiene un contraejemplo concreto.103_43 ya prueba la hipótesis diferencial propuesta para el kernel específico fuera del intervalo compacto; no se presenta esa hipótesis como nueva ni se usa su versión global sin prueba.

La diferencia es probar una consecuencia distinta de esa hipótesis: concavidad estricta de la MEDIA bajo inclinación exponencial, mediante una comparación condicional de DOS copias. No se intenta ordenar los cinco cambios de inclinación polinómica de103_43, ni derivar signo de cumulantes de todos los órdenes. El argumento se demuestra íntegramente abajo mediante cocientes de densidades y covarianzas, sin una desigualdad externa de correlación.

## 2. Hipótesis suficientes y enunciado

Sea V:R->R una función par, de clase C³, tal que

    V'''(x)>0 para todo x>0,
    V(x)/|x| -> +infinito cuando |x|->infinito.           (H)

La segunda condición precisa el decaimiento superexponencial que aquí se necesita. Para u real defina

    Z(u)=int_R exp[-V(x)+ux]dx,
    p_u(x)=exp[-V(x)+ux]/Z(u),
    M(u)=E_u[X]=Z'(u)/Z(u).

Entonces, para todo u>0,

    M''(u)<0,
    M(u)-uM'(u)>0,
    0<uM'(u)<M(u).                                      (RESULT)

Todas las derivadas de Z existen: sobre cualquier compacto de u, una potencia de |x| por exp[-V(x)+ux] queda dominada por una exponencial integrable. En particular M'=Var_u(X)>0 y M'' es el tercer momento centrado. No se necesita suponer que V sea convexa cerca del origen: (H) sólo fuerza que V'' crezca estrictamente con |x|.

## 3. Identidad exacta de dos copias: el factor4

Tome X,Y independientes con densidad p_u y ponga

    S=(X+Y)/2, D=(X-Y)/2.

Por expansión directa,

    E[SD²]=(E[X³]-E[X²]E[X])/4,
    E[D²]=(E[X²]-E[X]²)/2,
    E[S]=E[X].

Así

    4Cov(S,D²)=E[X³]-3E[X²]E[X]+2E[X]³=M''(u).          (TWO-COPY)

La densidad conjunta de S,D es proporcional a

    exp[2us-V(s+d)-V(s-d)].

El jacobiano constante2 no afecta las densidades condicionales. Condicionar S=s elimina la inclinación y da

    q_s(d)=exp[-W_s(d)]/int_R exp[-W_s(v)]dv,
    W_s(d)=V(s+d)+V(s-d).

Ponga g(s)=E[D²|S=s]. Sus valores son finitos y no dependen de u. V par implica q_(-s)=q_s, así que g es par.

## 4. La varianza condicional decrece estrictamente con |S|

Como V es par, V'' es par. De V'''>0 en la semirrecta positiva se sigue que V'' aumenta estrictamente con |x|.

Para 0<=s1<s2, defina Delta(d)=W_s2(d)-W_s1(d). Es par y para d>0 cumple

    Delta'(d)
      =int_(s1)^(s2) [V''(t+d)-V''(t-d)]dt >0.          (ORDER)

En efecto |t+d|>|t-d| para t,d>0. Aunque s1=0, el intervalo(t>0) tiene longitud positiva y la desigualdad integrada es estricta. Por tanto

    q_s2(d)/q_s1(d)=constante·exp[-Delta(d)]

es estrictamente decreciente en |d|. Bajo q_s1, ponga B(d)=exp[-Delta(d)]. Entonces

    g(s2)-g(s1)=Cov_(q_s1)(D²,B(D))/E_(q_s1)B(D)<0.     (g-ORDER)

El signo estricto se prueba con dos copias de |D|: D² crece estrictamente con |D|, B decrece estrictamente y la distribución tiene densidad positiva en toda la recta. Las integrales de B y D²B son finitas por la definición de q_s2 y (H); las de D² bajo q_s1 también. Esto justifica la identidad de covarianza incluso si B no fuera acotada.

Este argumento evita diferenciar integrales que contienen V': no se introduce una hipótesis de crecimiento de sus derivadas escondida en(H). Se ha probado directamente que g(s) es estrictamente decreciente para s>=0, que es la propiedad necesaria en el siguiente paso. No se necesita afirmar una fórmula diferencial de g.

## 5. Signo estricto de la covarianza no condicionada

La densidad marginal de S tiene la forma

    p_S(s)=constante·exp(2us)H(s),
    H(s)=int_R exp[-W_s(d)]dd,

con H par y estrictamente positiva. Ponga R=|S|. Para todo r>0,

    E[S|R=r]=r tanh(2ur)=:a_u(r).

Si u>0, a_u es estrictamente creciente en r>0, pues

    a_u'(r)=tanh(2ur)+2ur sech²(2ur)>0.

Por condicionamiento y porque g es par,

    Cov(S,D²)=Cov(S,g(S))
             =Cov(a_u(R),g(R))<0.                      (NEGATIVE)

La última desigualdad vuelve a ser la identidad elemental de dos copias para funciones de monotonías opuestas. Es estricta porque R tiene densidad positiva en(0,infinito) y ambas funciones son estrictamente monótonas. Los productos son integrables: E[|S|g(S)]=E[|S|D²] es finita por los momentos de orden3 de X,Y. No se ha reemplazado una covarianza mixta por su módulo.

TWO-COPY y NEGATIVE prueban M''(u)<0 para todo u>0.

## 6. Consecuencia para el criterio de dos generadores

La paridad de V da M(0)=0. Para A(u)=M(u)-uM'(u),

    A(0)=0, A'(u)=-uM''(u)>0 para u>0.

Luego A(u)>0. Además M'=Var_u(X)>0, lo que completa RESULT. Integrando la desigualdad0<uM'/M<1 se obtiene, para u>v>0,

    1<M(u)/M(v)<u/v.

Ésta es exactamente la comparación de cocientes que CONE001 necesita para sus menores de dos generadores. Es una consecuencia bajo(H), no una afirmación sobre menores de orden mayor ni sobre la forma completa en una envolvente de familias.

## 7. Aplicación theta: hipótesis verificada y alcance

Para el kernel par positivo Phi de CONE001/103_43, tome

    V(x)=-log Phi(x),
    Z(u)=int_R Phi(x)exp(ux)dx,
    M(u)=Z'(u)/Z(u).

La positividad, paridad, regularidad y decaimiento requerido se comprueban en los antecedentes. La hipótesis adicional necesaria es

    V'''(x)=-(log Phi)'''(x)>0, TODOS x>0.                (THETA-H)

103_43 prueba esa desigualdad para x>=1/4. El compacto0<x<1/4 queda ahora cubierto por [POWER_THETA_HAZARD_COMPACT_073.md](POWER_THETA_HAZARD_COMPACT_073.md): su certificado racional prueba(logPhi)''''<0 en[0,1/4], y la paridad da(logPhi)'''(0)=0. Integrar conserva la desigualdad estricta y completa THETA-H para TODO x>0. Constructor, root y auditor independiente reprodujeron el certificado; la auditoría integrada [POWER_THETA_AUDIT_073.md](POWER_THETA_AUDIT_073.md) aprueba la prueba de dos copias, el compacto y la aplicación. Por tanto la aplicación se promueve a **PROVED/APROBADO**, en lugar de CONDITIONAL. No se deduce de la logconcavidad sola ni se modifica la fuente histórica103_43.

Con M(u)=L(u+1/2) en la normalización de CONE001, RESULT demuestra M-uM'>0 para TODO u>0. Así se supera el dominio previo de la comparación aritmética de CONE001§5, restringido a u+1/2>=32. La comparación de inclinaciones polinómicas más altas de103_43 sigue siendo una obligación distinta.

## 8. Corolario explícito: todos los planos reales de dos generadores

Para a>1 defina, conservando las constantes y la aritmética completas de CONE001,

    L(a)=1/a+1/(a-1)-(log pi)/2+psi(a/2)/2
                         -sum_(m>=2)Lambda(m)m^(-a).

Sean a1=a,a2=b, ambos mayores que1. Si a!=b, la matriz real simétrica

    K_(i,j)=[L(ai)+L(aj)]/(ai+aj-1), i,j=1,2,

es DEFINIDA POSITIVA. En consecuencia, para cualquier par real(c1,c2)!=(0,0),

    W[c1 exp(-(a-1/2)t)1_(t>0)
          +c2 exp(-(b-1/2)t)1_(t>0)] > 0.               (TWO-GENERATORS)

Prueba: por simetría suponga u=a-1/2>v=b-1/2>0. RESULT y§6 dan

    1<L(a)/L(b)<u/v.

Las diagonales de K son positivas, y el criterio exacto de CONE001§3 afirma que el determinante es positivo cuando

    v/u<L(a)/L(b)<u/v.

Ambas desigualdades son estrictas aquí. Sylvester prueba la definitud positiva. La fórmula de polarización de CONE001§1 identifica EXACTAMENTE K como la matriz de W en los dos exponenciales, incluyendo ARCH, polar y TODOS los contactos; no se transfieren sólo las partes individuales.

Para las potencias exteriores rho(X)=c1 X^(-a)+c2 X^(-b), X>1, el mapa Z de CONE001 da los coeficientes d_i=c_i zeta(ai) de esos exponenciales. Como zeta(ai)>0 para ai>1, la matriz de la forma exterior es una congruencia diagonal invertible de K. También es definida positiva para exponentes distintos.

Si a=b, K es sólo semidefinida positiva: los dos generadores coinciden. La función temporal es no nula exactamente cuando c1+c2!=0, y en ese caso su W es estrictamente positiva. El vector de coeficientes no nulo(c1,-c1) representa la función cero y no tiene energía positiva. La misma precisión vale para las potencias exteriores coincidentes.

Este corolario no afirma positividad para tres generadores, todos los órdenes, su envolvente lineal completa ni una nueva ventana T. Es una ampliación demostrada de la comparación real de DOS generadores a todos los exponentes a,b>1. Papers intactos; signo global OPEN.
