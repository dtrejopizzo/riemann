# POWER_LOGCONVEX_CURVATURE_OBSTRUCTION_101 — Curvatura logconvexa insuficiente

Estado: **PROVED, auditoría independiente aprobada.** Véase `POWER_LOGCONVEX_CURVATURE_AUDIT_101.md`. Falsificador analítico explícito de una clase de potenciales auxiliares. No es la Phi real ni un valor negativo de W. Papers intactos.

## 1. Consulta, hipótesis nueva y alcance

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README.md, el grid R162_2300_MASTER_GRID.md y CROSSWORD-TO-D.md. Cotejados POWER_TWO_COPY_SCOPE_074.md, SCHUR003, 081 y el estado autoritativo099. La búsqueda adicional en el índice y phase211 de logconvexidad de V'', jerarquías de derivadas del potencial y mezclas de cosh no encontró este falsificador.

074 ya demuestra que V par, fuertemente convexo y V'''>0 en la semirrecta no bastan para obtener positividad de triples. Aquí se refuta una hipótesis estrictamente reforzada: además, V'' es estrictamente logconvexa en toda la recta, todas las derivadas pares V^(2j) son estrictamente positivas, y todas las impares V^(2j+1) son estrictamente positivas en t>0. Por tanto V'''/V'' es estrictamente creciente. El potencial polinómico de074 no pertenece a esta clase: en su cola, (log V'')'' es negativo, y sus derivadas suficientemente altas son nulas. Esta diferencia explícita justifica el nuevo test y evita reiterar074 bajo otro nombre.

No se afirma que la Phi real satisfaga todas estas hipótesis, ni que sean necesarias para el signo. Se descarta sólo su suficiencia genérica, incluso antes de intentar conservarlas bajo Schur. No se modifica la cobertura real099 ni se infiere ninguna obstrucción global para W.

## 2. Potencial, ley y nodos completamente fijados

Definir

    v(t)=cosh(t)+10^(-4)cosh(10t), A=10^46,
    V(t)=A v(t), delta=10^(-4), u_i=i delta, U_i=A u_i,
    c=(1,-2,1), i=1,2,3.

Sea M(U) la media de la ley en toda la recta proporcional a exp[-A v(t)+Ut], y

    K_M(U,W)=[M(U)+M(W)]/(U+W).

La caída de exp[-A v(t)+Ut] paga todos los momentos e integraciones por partes siguientes. Se probará

    c^t [K_M(U_i,U_j)] c < -3 delta^4/(2A) < 0.       (NEGATIVE)

El potencial es par y suave, v''>=101/100>1. Todas sus derivadas pares son positivas; todas sus derivadas impares son positivas para t>0. Además

    v''(t)=cosh(t)+10^(-2)cosh(10t)

es una suma positiva de las exponenciales de tasas -10,-1,1,10. Si las cuatro masas normalizadas inclinadas por t son p_r(t), entonces

    (log v'')''=sum_r p_r r^2-(sum_r p_r r)^2 > 0.

La desigualdad es estricta porque las cuatro masas son positivas y las tasas son distintas. Multiplicar por A no cambia esta segunda derivada logarítmica. Quedan verificadas globalmente todas las hipótesis adicionales.

## 3. Aproximación elemental de la función inversa

Sea f=(v')^(-1), bien definida en toda la recta por v''>1. Escribir

    alpha=101/100, beta=1/3, gamma=101/120,
    a=1/alpha, b=-beta/alpha^4,
    d=(3 beta^2-alpha gamma)/alpha^7,
    q(u)=a u+b u^3+d u^5.

Las cancelaciones de coeficientes hasta grado5 en

    alpha q+beta q^3+gamma q^5-u

son directas: alpha a=1, alpha b+beta a^3=0 y alpha d+3 beta a^2 b+gamma a^5=0. Los números racionales satisfacen

    99/100<a<1, -1/3<b<0,
    d=-51675000000000/107213535210701,
    -1<d<-2/5.                                      (COEFF)

Probamos, para 0<=u<=3 delta,

    |f(u)-q(u)| <= 100 u^7.                         (INVERSE)

En u=0 es inmediato. Para u>0 poner w=b u^3+d u^5. Por COEFF, |w|<=2u^3 y 0<q(u)<=u: ambos términos correctores son negativos y q/u>99/100-u^2/3-u^4>0. La expansión cúbica da

    |q^3-a^3u^3-3a^2b u^5|
       <=3u^7+12u^7+8u^9 <16u^7.

El teorema del valor medio aplicado a la quinta potencia, usando 0<q<=a u<=u, da

    |q^5-a^5u^5|<=5u^4 |w|<=10u^7.

También la serie completa de sinh, para 0<=q<=3/10000, da

    0<=v'(q)-alpha q-beta q^3-gamma q^5<3q^7<=3u^7.

En efecto su primer coeficiente omitido es 10001/5040<2, y el cociente de cada término siguiente con el anterior es como máximo (10q)^2/(8*9)<1/7200. La suma geométrica mayorante es menor que3. Combinando estas tres cotas y las cancelaciones exactas,

    |v'(q(u))-u| < (16/3+10+3)u^7 <20u^7.

Como v''>=1 y v'(f(u))=u, el valor medio implica |f(u)-q(u)|<=|u-v'(q(u))|<20u^7<=100u^7. No se evalúan integrales ni se usa un desarrollo asintótico sin resto.

## 4. Un triple negativo para los modos

Definir K_f(u,w)=[f(u)+f(w)]/(u+w). Para el vector c fijado,

    sum_i c_i=0, sum_i c_i u_i=0,
    sum_i c_i u_i^2=2delta^2.

Por las identidades polinomiales (u^3+w^3)/(u+w)=u^2-uw+w^2 y (u^5+w^5)/(u+w)=u^4-u^3w+u^2w^2-uw^3+w^4, las partes lineal y cúbica de q desaparecen en la forma, y

    c^t[K_q(u_i,u_j)]c=4d delta^4<-8delta^4/5.

INVERSE y (u^7+w^7)/(u+w)<=max(u,w)^6 implican

    |(K_f-K_q)(u_i,u_j)|<=100(3delta)^6.

Como sum|c_i|=4, el error de la forma es a lo sumo

    16*100*729 delta^6
      = (729/62500)delta^4 <(3/250)delta^4.

Así

    c^t[K_f(u_i,u_j)]c<-(397/250)delta^4.          (MODE)

## 5. De los modos a las medias, con error explícito

Para cada u_i, la única moda de la ley proporcional a exp[-A(v(t)-u_i t)] es x_i=f(u_i). Sea X_i una variable con esa ley. La integración por partes exacta de (t-x_i) contra la densidad da

    E[(X_i-x_i)(v'(X_i)-u_i)]=1/A.

Por v''>=1 y v'(x_i)=u_i, el integrando es al menos (X_i-x_i)^2. Por tanto

    E[(X_i-x_i)^2]<=1/A,
    |M(Au_i)-f(u_i)|<=1/sqrt(A)=10^(-23).         (MEAN)

Definir B_ij=A K_M(Au_i,Au_j). Entonces

    B_ij=[M(Au_i)+M(Au_j)]/(u_i+u_j).

Como u_i+u_j>=2delta, MEAN implica

    |B_ij-K_f(u_i,u_j)|<=1/[delta sqrt(A)],
    |c^t(B-K_f)c|<=16/[delta sqrt(A)]
       =(2/125)delta^4.

Finalmente MODE da

    c^tBc<-(397/250-4/250)delta^4
          =-(393/250)delta^4 < -3delta^4/2.

Dividir por A prueba NEGATIVE. Las diagonales son positivas porque la paridad y positividad de la densidad implican M(U)>0 para U>0; así este bloque es indefinido.

## 6. Resultado y límites de la conclusión

La clase reforzada de potenciales de§1 no garantiza positividad del kernel completo de tres nodos. El falsificador usa un solo potencial, tres nodos y un vector racional prefijados; no es una campaña numérica. El chequeo racional pequeño de COEFF y de ambos costes de error dio PASS; la demostración anterior es autocontenida y no depende de ese cómputo.

El resultado no concierne al kernel theta real ni produce W negativo. Tampoco refuta una condición más específica de pares J/K, una recurrencia que use más datos que esas desigualdades diferenciales del potencial, ni la recursión general de Schur. Todos los resultados reales hasta099 permanecen vigentes. El signo global sigue OPEN.

En particular este ejemplo NO satisface conjuntamente las comparaciones de077/089/099 que ya pagan los triples reales: su triple negativo impide atribuirle esos inputs. No se ha refutado una clase invariante que los incorpore. La utilidad acotada es evitar sustituir esos datos de pares por la mera jerarquía diferencial del potencial; no es un pivote terminal y no justifica una sucesión de fortalecimientos genéricos de073 que omitan los inputs reales disponibles.
