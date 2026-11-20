# POWER_WEIGHTED_COEFFICIENT_034 — Oscilación de los prefijos ponderados Erlang

Estado: **PROVED**, revisión hostil independiente aprobada en POWER_COMPARISON_AUDIT_034.md y revisión adicional del constructor principal. Tasa fija u=63/2.

Teorema: los números REALES T_m de033 toman valores estrictamente positivos y estrictamente negativos en índices arbitrariamente grandes. En particular la condición suficiente T_m>=0 para TODO m, y aun su versión salvo finitas excepciones, es falsa. No se afirma W negativa ni un impedimento para controlar la combinación gamma de signos. Papers intactos.

## 1. Corpus y razón nueva

Leídos las reglas del proyecto, COEFFICIENT_BALANCE033 y su auditoría, CONE001§§2,7 (representación REAL cosh positiva del funcional exponencial), TABLE_DESCENT018 (T1 positivo real), y el generador exacto033. Consultados ROUTES-TRIED-INDEX, grid maestro y CROSSWORD-TO-D.md en Pringsheim, series de coeficientes positivos, monotonía absoluta y mezclas Erlang.

El lema clásico de continuación de una serie con coeficientes positivos aparece en antecedentes de colas de fase164; no se presenta como herramienta nueva. La diferencia es el objeto y la hipótesis: se prueba una afirmación sobre la sucesión específica T_m de prefijos ponderados finitos, no sobre la forma W completa. Se usa exclusivamente la representación REAL positiva ya establecida para el funcional exponencial, su paridad y series de coeficientes. El lema de continuación se demuestra abajo, en lugar de invocarlo como una caja opaca.

Frente033, no se agrega otro índice ni una campaña de diagnósticos. La estructura analítica da un patrón UNIFORME y refuta la premisa concreta de signo de todos los T_m. El resultado no se convierte en una conclusión sobre el signo de las combinaciones gamma reales, cuyos coeficientes de Abel positivos aún pueden compensar los signos de T_m.

## 2. Funcional real exponencial y representación cosh positiva

Para v>1/2, el funcional completo normalizado de un exponencial es

    E(v)=psi((v+1/2)/2)−logpi+4v/(v²−1/4)
                        −2sum_(q>=2)Lambda(q)q^(−v−1/2).

Es EXACTAMENTE el E0(v)=2L_power(v+1/2) de033, con todos los términos aritmético y polar. CONE001 establece, mediante la integral theta real y Poisson, que

    E(v)=2Theta'(v)/Theta(v),
    Theta(v)=C int_0^infty Phi(t)cosh(vt)dt, C>0,
    Phi(t)=sum_(n>=1) pi n² e^(5t/2)
             [2pi n² e^(2t)−3]e^(−pi n² e^(2t))>0.

El factor constante no afecta el cociente. La caída doblemente exponencial justifica todas las derivadas y la extensión analítica de esta integral en compactos. Theta es PAR y Theta(v)>0 para TODO v real. En un entorno pequeño de cualquier punto real v0, su parte real sigue siendo estrictamente positiva; allí se define analíticamente logTheta. Por tanto el cociente anterior proporciona una función E real-analítica en TODA la recta real y

    E(−v)=−E(v).                                         (ODD)

Ésta es sólo una propiedad real/analítica de la integral positiva. No se añade ninguna hipótesis sobre el comportamiento fuera de esos entornos de puntos reales.

## 3. Generador correcto y paridad alrededor de1

Con los prefijos exactos033,

    T_m=sum_(j=1)^m j L[S_j],
    S_j(t)=e^(−ut)sum_(r=0)^j(ut)^r/r!,

el generador, convergente inicialmente cerca de z0, es

    F(z):=sum_(m>=1)T_m z^(m−1)
         =[E(v)−vE'(v)]/(1−z)^3, v=u(1−z).             (GEN)

Se ha dividido UNA vez el factor z de la fórmula033. No hay un segundo factor z en GEN.

Por ODD, cerca de v0,

    E(v)=alpha1 v+alpha3 v³+alpha5 v⁵+...,
    E(v)−vE'(v)=−2alpha3 v³−4alpha5 v⁵−... .

Así la aparente división por(1−z)^3 se prolonga analíticamente en z1 y

    F(1+s)=F(1−s),
    F^(q)(1)=0 para TODO entero IMPAR q>=1.              (PARITY)

GEN y la analiticidad real de E muestran además que F admite una prolongación holomorfa local alrededor de CADA punto de la semirrecta real positiva. No se afirma que la serie de Taylor original converja allí sin una hipótesis adicional sobre sus coeficientes.

## 4. Decaimiento real y no trivialidad

Las cotas reales elementales de psi, logx−1/x<=psi(x)<=logx, y psi'(x)<=1/x+1/x², junto con Lambda(q)<=logq, dan para v grande positivo

    E(v)=log(v/(2pi))+O(1/v),
    E'(v)=O(1/v).

Para la serie prima y su derivada basta comparar con sum q^(−v+3/2), que es exponencialmente pequeño; el racional polar y su derivada son O(1/v),O(1/v²). Estas estimaciones usan la expresión explícita real del§2. Por ODD, E' es par y las mismas cotas en módulo valen en el semieje negativo.

Al hacer z real positivo tender a infinito, v=u(1−z) es negativo y de módulo comparable con z. GEN implica

    F(z)=O(logz/z³)->0.                                 (DECAY)

F no es la función nula. Por ejemplo F(0)=T1=L[S1] es precisamente W[g2]/norm², que TABLE_DESCENT018 prueba>1/8 a u63/2. También la no trivialidad se sigue de que E crece como logv y no puede ser una función lineal cv.

## 5. Lema elemental de continuación de una cola positiva

**Lema.** Sea f real-analítica en un entorno de CADA punto x>=0, con un germen de Taylor f(z)=sum c_nz^n en0 de radio positivo. Si c_n>=0 salvo finitos índices, esa serie de Taylor tiene radio infinito.

Prueba. Restar el polinomio de los primeros índices reduce al caso de TODOS los coeficientes no negativos sin cambiar la posibilidad de prolongación local en puntos reales. Suponga radio finito R>0. La prolongación dada por f coincide con el germen inicial a lo largo de(0,R), por unicidad de prolongación analítica.

Elija epsilon>0 pequeño tal que f es holomorfa en|z−R|<epsilon y epsilon<R. Tome a=R−epsilon/4. La serie de Taylor alrededor de a converge, por ejemplo, para h=epsilon/2. Sus coeficientes son

    f^(k)(a)/k!=sum_(n>=k)c_n binom(n,k)a^(n−k)>=0,

porque a<R. Tonelli y el binomio dan

    sum_(k>=0)h^k f^(k)(a)/k!
      =sum_(n>=0)c_n sum_(k=0)^n binom(n,k)a^(n−k)h^k
      =sum_(n>=0)c_n(a+h)^n<infinito.

Pero a+h=R+epsilon/4>R, contradiciendo el radio. Luego no existe radio finito. QED.

El mismo argumento vale para coeficientes eventualmente no positivos aplicándolo a−f. Este lema es la forma elemental de la propiedad clásica de Pringsheim que se necesita; no exige ni proporciona datos externos sobre la función aritmética.

## 6. Teorema de oscilación infinita de T_m

Suponga que T_m>=0 para TODOS m suficientemente grandes. El lema y§3 hacen que la serie de Taylor de F sea entera; su suma coincide con la prolongación real anterior por unicidad a lo largo de la semirrecta positiva. Elija un entero impar q mayor que todos los índices excepcionales (recordando que el coeficiente de z^n es T_(n+1)). Entonces

    0=F^(q)(1)
      =sum_(n>=q) n!/(n−q)! ·T_(n+1).

La derivación término a término y la convergencia absoluta en1 se justifican AHORA por el radio infinito; no se presumieron antes. Todos los sumandos son no negativos. Por tanto TODOS los T_(n+1) con n>=q son nulos y F es un polinomio. DECAY fuerza que ese polinomio sea idénticamente nulo, contradiciendo§4.

Así los T_m NO pueden ser eventualmente no negativos. Aplicar exactamente el argumento a−F prueba que tampoco pueden ser eventualmente no positivos. Puesto que los coeficientes son reales, se concluye

    para TODO M existen m_+>M,m_−>M
       con T_(m_+)>0 y T_(m_−)<0.                       (OSC)

Esto refuta en particular la premisa033 «T_m>=0 para TODOS m». La prueba no localiza el primer índice negativo ni requiere evaluarlo. Tampoco se infiere que la serie sum T_m o sus momentos converjan en1 para el dato real: esas convergencias sólo aparecieron bajo la hipótesis eventualmente positiva que condujo a contradicción.

## 7. Alcance frente a la función gamma real

La identidad exacta033 sigue siendo

    W[g_N]/norm²=sum_(m=1)^(N−1)
                      [v_Nm−v_N,m+1]T_m,
    v_Nm−v_N,m+1>=0.

OSC demuestra que una prueba del signo de estas combinaciones no puede consistir en declarar no negativo cada T_m, ni en corregir sólo un número finito de excepciones. NO dice que la combinación gamma sea negativa: sus pesos reales pueden compensar infinitos cambios de signo en una sucesión de prefijos que no son todos autocorrelaciones admisibles.

El resultado es una refutación del criterio suficiente concreto de033, no un NO-GO global. La continuación constructiva requiere un bound firmado de las contribuciones adversas CONTRA los pesos gamma reales, o una agrupación aritmética diferente que preserve esa compensación. No se abandona la obligación W ni se amplía una campaña de índices.

## 8. Validación

La prueba es analítica y no necesita evaluar nuevos m o N. POWER_COMPARISON_AUDIT_034.md aprueba independientemente la normalización de GEN, representación REAL cosh/ODD, cancelación en z1, lema de continuación, uso condicionado de series en1 y alcance exclusivamente sobre el criterio T_m. El constructor principal leyó y aprobó también esos pasos. Papers intactos.
