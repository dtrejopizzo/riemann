# POWER_TWO_COPY_SCOPE_074 — La hipótesis fuerte073 no basta para tres generadores

Estado: **PROVED/APROBADO**, auditoría independiente en [POWER_TWO_COPY_SCOPE_AUDIT_074.md](POWER_TWO_COPY_SCOPE_AUDIT_074.md); verificador reproducido por constructor, root y auditor con exit0/PASS. Contraejemplo ANALÍTICO auxiliar dentro de la misma clase de potenciales de073. No es el kernel theta real ni una dirección negativa de W. Papers intactos.

## 1. Consulta y diferencia exacta

Leídos las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid maestro R162_2300_MASTER_GRID y CROSSWORD-TO-D; cotejados SCHUR003 y THETA_TWO_COPY073.003 ya refuta extender monotonías y concavidad a matrices de orden3, pero sus funciones auxiliares no se presentan como medias inclinadas de un potencial par C³ con V'''>0. El ejemplo3+cosh tampoco satisface esas hipótesis.

La diferencia aquí es mantener TODAS las hipótesis fuertes073 y producir una matriz3x3 indefinida. Se estudió primero el jet en0 de la familia prescrita V=x^6; ese jet NO produce el contraejemplo. El contraejemplo definitivo se construye analíticamente mediante un único potencial polinómico explícito y tres inclinaciones fijadas de antemano. No se barre una familia de parámetros ni se evalúan integrales numéricamente.

## 2. Condición del determinante coalescente en el origen

Para cualquier potencial par con los momentos y la regularidad de073, escriba los cumulantes de su ley sin inclinación como kappa2,kappa4,kappa6. Cerca de0,

    M(u)=alpha u+beta u³+gamma u^5+O(u^7),
    alpha=kappa2, beta=kappa4/6, gamma=kappa6/120.

Para nodos distintos xi>0 y ui=epsilon xi, el kernel K(u,v)=(M(u)+M(v))/(u+v) satisface

    det[K(epsilon xi,epsilon xj)]_(i,j=1)^3
      =epsilon^6 prod_(i<j)(xj-xi)²
                       ·(-beta)(alpha gamma-beta²)+O(epsilon^8).

Se verifica expandiendo(u^(2r+1)+v^(2r+1))/(u+v). En las coordenadas monomiales0,1,2 el primer menor de coeficientes es

    [[alpha,0,beta],[0,-beta,0],[beta,0,gamma]],

cuyo determinante es(-beta)(alpha gamma-beta²). Los índices0,1,2 son los de menor suma en tres filas y columnas distintas, por lo que dan el término de orden6. La paridad excluye orden7.

Si kappa4<0, el signo principal de este determinante está determinado por

    3 kappa2 kappa6 - 10 kappa4².                       (JET)

Para V(x)=x^6, los momentos pares son

    m_(2r)=Gamma((2r+1)/6)/Gamma(1/6).

Poniendo a=m2, la reflexión gamma da m4=2a² y m6=1/6. Así

    kappa4=-a², kappa6=1/6,
    JET=a/2-10a^4>0.

Para justificar el último signo sin decimales, basta a<1/3. En efecto

    Gamma(1/6)=6 int_0^infinito exp(-x^6)dx
      >6[1-1/7+1/26-1/114]>3sqrt(pi).

La primera desigualdad usa el polinomio de Taylor inferior1-z+z²/2-z³/6 para exp(-z), integrado en[0,1], y descarta una cola positiva. Si r=1-1/7+1/26-1/114, el verificador comprueba r²>11/14>pi/4 usando pi<22/7. Por tanto a=sqrt(pi)/Gamma(1/6)<1/3 y1/2-10a³>1/2-10/27>0. Este primer test coalescente de x^6 es positivo; no se ofrece como falsificador.

## 3. Potencial explícito que sí da el contraejemplo

Fije exactamente

    p=1000000, A=400000000,
    v(x)=x²/2+x^(2p)/[2p·2^(2p-2)],
    V(x)=A v(x).

Es un potencial par POLINÓMICO, de clase C-infinito, superlineal, y

    v''(x)=1+(2p-1)(x/2)^(2p-2)>=1,
    V'''(x)=A(2p-1)(2p-2)x^(2p-3)/2^(2p-2)>0, x>0.

Por tanto satisface estrictamente TODAS las hipótesis073. Sea M(u) la media de la densidad proporcional a exp[-V(x)+ux], y tome únicamente los tres nodos

    u1=A, u2=2A, u3=3A.

No se modifica el potencial entre los tres nodos.

## 4. Modos: bounds analíticos sin resolver ecuaciones grandes

Para i=1,2,3, sea xi la única solución de v'(xi)=i. Existe y es única por v''>=1 y los límites de v'. Ponga eta=1/20000. Se tiene

    1-eta<x1<1,
    2-eta<x2<2,
    2-eta<x3<2.                                        (MODES)

En efecto v'(x)=x+x(x/2)^(2p-2). Como2p-2>15 y2^15>20000,

    v'(1-eta)<1-eta+2^(-(2p-2))<1<v'(1).

Para el otro extremo,

    v'(2-eta)
      <2-eta+2(1-eta/2)^(2p-2)
      <=2-eta+2exp[-(p-1)eta]<2,

pues(p-1)eta>49 y exp49>49^4/24>40000, de donde2exp(-49)<eta. Por otra parte v'(2)=4>3. La monotonía estricta de v' prueba MODES para ambos índices2,3.

## 5. Modos a medias: error uniforme por convexidad fuerte

En el nodo ui=A i, la densidad es proporcional a exp[-A(v(x)-i x)]. Si Xi tiene esa ley y mi=M(A i), la integración por partes de(x-xi) por la densidad da EXACTAMENTE

    E[(Xi-xi)(v'(Xi)-i)]=1/A.

El término de borde se anula por la caída de una exponencial de un polinomio par. Como v''>=1 y v'(xi)=i,

    (x-xi)(v'(x)-i)>=(x-xi)².

Luego E[(Xi-xi)²]<=1/A y, por Cauchy,

    |mi-xi|<=1/sqrt A=eta.

Combinando con MODES se obtiene

    |m1-1|<1/10000,
    |m2-2|<1/10000,
    |m3-2|<1/10000.                                    (MEANS)

Esta estimación controla las integrales reales completas; no es una aproximación de punto de silla sin resto.

## 6. Vector negativo racional y todos los pares positivos

La matriz rescalada B=A[K(ui,uj)] tiene entradas

    B_(i,j)=(mi+mj)/(i+j).

Por MEANS, cada entrada difiere en menos de delta=1/10000 de la matriz racional

    B0=[[1,1,3/4],[1,1,4/5],[3/4,4/5,2/3]].

Tome c=(40,-40,3). Un cálculo racional exacto da

    c^T B0 c=-6,
    |c^T(B-B0)c|<delta(40+40+3)²=6889/10000<1.

Por tanto

    c^T B c < -53111/10000<0,
    c^T [K(ui,uj)] c < -53111/(10000 A)<0.              (NEGATIVE)

La matriz es indefinida, pues sus diagonales son positivas. Sin embargo, por el teorema general073 aplicado a ESTE V, TODOS sus menores de dos nodos distintos positivos son definidos positivos, no sólo los tres pares elegidos aquí. También M''<0 y M-uM'>0 en toda la semirrecta positiva.

Así el control probabilístico fuerte073 y su concavidad estricta no se preservan automáticamente como un signo de orden3. El contraejemplo es analítico y pertenece exactamente a la clase propuesta, a diferencia de los auxiliares de003.

## 7. Evidencia y alcance

Verificador `tools/power_two_copy_scope_074_verify.py`: aritmética Fraction para MODES, el error de medias, la matriz B0, el vector y las constantes del test x^6. No evalúa la función M ni el potencial de grado enorme; no hay cuadratura ni búsqueda de parámetros. Las desigualdades para las medias y las entradas se prueban analíticamente arriba.

No es el potencial theta REAL y no se afirma una dirección negativa de W. El resultado073 de TODOS los pares reales sigue íntegro. Lo refutado es únicamente la implicación genérica «hipótesis sobre V de073 ⇒ positividad3x3 de K». Para avanzar sobre tres generadores del dato real hará falta una propiedad específica adicional de Phi o una estimación concreta de su cruce. No se excluyen tales propiedades ni se infiere un impedimento global. Papers intactos.
