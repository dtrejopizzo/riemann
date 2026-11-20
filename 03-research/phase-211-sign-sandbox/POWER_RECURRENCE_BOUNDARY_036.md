# POWER_RECURRENCE_BOUNDARY_036 — Energía del cono en una frontera infinita

Estado: **PROVED; revisión independiente APROBADA en POWER_FRONTIER_AUDIT_036.md**. A u FIJO63/2, para cualquier entrada inicial N>=18,k>=0, la energía COMPLETA del cono positivo017 en la frontera diagonal de profundidad L tiende a0 con cota explícita O(logL/sqrtL). La energía del complemento tiende EXACTAMENTE a la entrada inicial, sin asumir que el resto desaparece. Una frontera detenida en el primer contacto con ese cono deja además masa normativa positiva explícita. No se prueba signo nuevo W ni un impedimento para otras fronteras.

## 1. Corpus y razón nueva

Leídos primero ROUTES-TRIED-INDEX/README.md, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; consultadas las entradas de descenso/recurrencia/conos, DESCENT016 y su auditoría§7, JOINT_SCALE016, TABLE_DESCENT018 y su falsificador, QUADRATIC_EXPLICIT017, DIVISOR_COMPARISON034 y BOUNDARY_BALANCE035.

La ley beta espectral y la expansión binomial no son nuevas: ya aparecen en016. La identificación como urna es sólo una forma de organizar esa misma ley. La diferencia AQUÍ es controlar la ENERGÍA DE LA FORMA REAL COMPLETA en TODO el subconjunto parabólico creciente k'>=10000N'^2 de cada frontera diagonal, no sólo un borde con N' fijo, ni sólo su probabilidad. Se mantiene el peine infinito y el polar usando sus bounds017. El resto completo tiene un límite exacto identificado; no se lo borra por una consideración de masa.

El resultado035 fue finito y empleó una columna real positiva y un dato terminal. Aquí se estudia qué produce realmente enviar una frontera al infinito con los datos explícitos disponibles, sin reiterar como novedad el contraejemplo abstracto018.

## 2. Pesos exactos, sin límite de martingalas implícito

Sea a_(N,k)=W[f_(N,k)] y n_(N,k)=||f_(N,k)||². Use la recurrencia completa

    a_(N,k)=a_(N,k+1)+u²a_(N+1,k),
    n_(N,k)=u^(1−2N)B(k+1/2,N−1/2)/(2pi).

Ponga A_(N,k)=a_(N,k)/n_(N,k), alpha=k+1/2,beta=N−1/2,S=N+k. Entonces

    A_(N,k)=[alpha/S]A_(N,k+1)+[beta/S]A_(N+1,k).

Iterar L veces da una identidad FINITA para la forma COMPLETA:

    A_(N,k)=sum_(j=0)^L pi_(L,j) A_(N+j,k+L−j),          (FRONT)
    pi_(L,j)=binom(L,j)(beta)_j(alpha)_(L−j)/(S)_L.

Aquí j cuenta incrementos de N. Todos los pi son positivos y su suma es1, por Vandermonde o integrando el binomio contra Beta(alpha,beta). La expansión sin normalizar tiene pesos binom(L,j)u^(2j); la fórmula anterior incluye EXACTAMENTE el cambio de norma. No se ha intercambiado ninguna serie infinita con W.

## 3. Un momento inverso exacto controla TODO el cono creciente

Si J tiene pesos pi_(L,j), la mezcla beta-binomial elemental da

    E[1/(N+J−3/2)]
      =(S−1)/[(N−3/2)(S+L−1)], N>=2.                    (INV)

Prueba: tome Q~Beta(alpha,beta), J|Q~Binomial(L,1−Q). La posterior Q|J es Beta(alpha+L−J,beta+J). Por la integral beta,

    E[(1−Q)^(-1)|J]=(S+L−1)/(beta+J−1),
    E[(1−Q)^(-1)]=(S−1)/(beta−1).

Promediar prueba INV; beta>1 equivale a N>3/2. También se puede verificar multiplicando cada término de FRONT por1/(beta+j−1) y aplicando Vandermonde. No se usa una aproximación asintótica beta.

Sea C=10000 y

    E_L={j: k+L−j>=C(N+j)²},
    s_L=sqrt((k+L)/C),
    M_L=min(1, (s_L−3/2)_+ (S−1)/[(N−3/2)(S+L−1)]).

En E_L se tiene N+j<=s_L, y por tanto 1/(N+j−3/2)>=1/(s_L−3/2), si el conjunto no es vacío. INV prueba

    sum_(j in E_L)pi_(L,j)<=M_L=O_(N,k)(L^(-1/2)).       (MASS)

Si s_L<N, E_L es vacío. El bound escrito con parte positiva sigue siendo válido incluso antes de que exista contacto con el cono.

## 4. Cota superior arquimediana REAL uniforme en la frontera

El símbolo completo es m(tau)=Re psi(1/4+i tau/2)−logpi. La recurrencia de psi resta un recíproco de parte real positiva, de modo que

    m(tau)<=Re psi(5/4+i tau/2)−logpi.

Euler periódico B1 en Re z=5/4 da

    psi(z)=logz−1/(2z)+R(z), |R(z)|<=2/5.

Como Re(1/z)>0 y logpi>0,

    m(tau)<= (1/2)log(25/16+tau²/4)+2/5.                (SYMBOL)

Para la probabilidad espectral del átomo de frontera N'=N+j,k'=k+L−j,

    E tau²=u²(k'+1/2)/(N'−3/2)
                <=u²(k+L+1/2)/(N−3/2).

Jensen para log prueba en TODA la frontera

    ARCH_(N',k')/n_(N',k')<=H_L,
    H_L=(1/2)log[25/16+u²(k+L+1/2)/(4(N−3/2))]+2/5.      (ARCH-UP)

Se necesita N>=2, que se satisface sobradamente en el régimen pendiente N>=18. No se supone que el símbolo sea acotado ni que ARCH converja uniformemente entre todas las celdas.

## 5. ENERGÍA COMPLETA del cono y límite exacto del resto

En CADA celda de E_L, QUADRATIC_EXPLICIT017 prueba para la forma real

    A_(N',k')>49/50,
    |PRIME|/n_(N',k')<1/1000,
    |POLAR|/n_(N',k')<1/1000.

Sus hipótesis son N'>=2,u63/2 y k'>=10000N'^2: exactamente las presentes, sin umbral N adicional. El segundo bound incluye TODOS los contactos y el tercero el polar exacto.

Defina la energía conocida del cono y el resto real

    C_L=sum_(j in E_L)pi_(L,j)A_(N+j,k+L−j),
    R_L=sum_(j notin E_L)pi_(L,j)A_(N+j,k+L−j).

De MASS, ARCH-UP y los bounds completos017,

    0<=C_L<=M_L(H_L+1/500)
               =O_(N,k)(log(L+2)/sqrt(L+1))->0.          (ENERGY)

FRONT implica entonces EXACTAMENTE

    R_L=A_(N,k)−C_L,
    |R_L−A_(N,k)|<=M_L(H_L+1/500)->0.                   (REMAINDER)

Éste es un límite de la ENERGÍA DE W REAL, no sólo una ley de probabilidad. No se ha supuesto integrabilidad uniforme de todos los valores A de la frontera ni se ha separado una compensación infinita de polar y peine. Sólo el subconjunto positivo se domina mediante bounds completos válidos allí; el complemento se conserva como la diferencia FINITA exacta de FRONT.

La región034 a u fijo cubre N'<=17 para k'>=1. Desde una entrada pendiente N>=18 nunca se llega a ella porque N' sólo aumenta. Los datos035 tampoco son alcanzables desde arriba. Por tanto, en esta frontera diagonal, TODO el conjunto positivo explícito017 accesible aporta energía que DESAPARECE, mientras el complemento lleva el valor original completo. No se obtiene una reducción de la obligación interior al cono.

Como ejemplo de resto REAL rigurosamente NO NULO, CONTACT_DECISION032 prueba A_(211,1)>3.4e−15. Para esa entrada ya decidida, REMAINDER da R_L->A_(211,1)>3.4e−15, aunque la energía positiva del cono tienda a0. No es un contraejemplo de signo ni un nuevo cálculo de otro N.

## 6. Frontera detenida: peso exacto y masa superviviente

La conclusión anterior concierne a fronteras DIAGONALES. Para no convertirla en una prohibición sobre todos los esquemas, registre también la detención en el PRIMER contacto con el cono. Suponga que el dato inicial está debajo: k<CN².

Cada camino con r incrementos de k y j incrementos de N tiene probabilidad

    (alpha)_r(beta)_j/(S)_(r+j),

independientemente del orden de sus pasos. Si g_(L,j) cuenta los caminos de longitud L que NO tocaron el cono y terminan con j incrementos de N, el peso EXACTO del resto detenido es

    sigma_(L,j)=g_(L,j)(alpha)_(L−j)(beta)_j/(S)_L.        (STOP-WEIGHT)

Los enteros g se obtienen de Pascal descartando celdas después de su primer contacto. De forma análoga, cada primera celda alcanzada tiene el mismo peso por camino multiplicado por su número de caminos admisibles. Iterar REC sólo en celdas no detenidas da una identidad finita: energía de primeras llegadas hasta L + sum_j sigma_(L,j)A_(N+j,k+L−j)=A_(N,k). Es un peso exacto del resto, no una afirmación de que ese resto converja a0.

Hay masa que NUNCA toca el cono. Condicione la representación beta a Q<=1/3. Los pasos son entonces independientes con probabilidad Q de incrementar k. El proceso 2^(r−j) es una supermartingala no negativa, pues su factor medio es2Q+(1−Q)/2<=1. Al tocar el cono,

    r−j=(k'−N')−(k−N)>=CN²−k,

porque CN'^2−N' crece para N'>=N. La desigualdad maximal elemental (detención finita y luego límite monótono) da

    P(hit|Q<=1/3)<=2^(-(CN²−k)).

Por tanto

    P(nunca hit)>=P_Beta(alpha,beta)(Q<=1/3)
                         ·[1−2^(-(CN²−k))]>0.          (SURVIVAL)

No se infiere de esta masa persistente que el resto de ENERGÍA detenido no pueda desaparecer: faltaría control firmado/integrabilidad de A en esas trayectorias. El resultado exacto ENERGY/REMAINDER es más fuerte para la frontera diagonal concreta; no resuelve esa otra frontera detenida.

## 7. Alcance y obligación cuantitativa que queda

La recurrencia positiva sólo incrementa k y N. Desde k>=1 nunca llega al borde k0; desde N>=18 tampoco alcanza las filas finitas ya cubiertas. La inversión algebraica hacia k0 da diferencias con signos alternos, no una representación positiva autorizada por REC.

La condición suficiente de frontera restante sería una estimación ARITMÉTICA REAL que pruebe R_L>=−epsilon_L con epsilon_L->0; ENERGY la convertiría en A_(N,k)>=0. Los datos de signo del cono por sí solos no proporcionan esa estimación: su energía en la frontera diagonal tiende a0 y R_L converge precisamente al valor cuya decisión estaba pendiente. No se declara esta condición una vía nueva de cierre.

Se registra como resultado nuevo acotado la cota explícita ENERGY para TODO el cono parabólico existente y el límite REMAINDER de la forma completa, más STOP-WEIGHT/SURVIVAL con alcance separado. No se repite como novedad la ley beta016, no se prueba un NO-GO global, y no se elimina la posibilidad de una estimación firmada nueva del interior o de otra frontera con control de energía.
