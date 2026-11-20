# POWER_THREE_SECANTS_079 — Tres generadores desde UNA concavidad adicional

**Actualización080:** el compacto admisible de g quedó certificado en `POWER_THETA_G_COMPACT_080.md`, auditado en `POWER_THETA_G_COMPACT_AUDIT_080.md` y resumido en `POWER_STATE_080.md`: TODOS los triples de potencias ai>1 tienen signo positivo completo. Las menciones siguientes de compacto pendiente describen el estado histórico de esta ronda; h y los órdenes superiores no quedan descargados por080.

Estado: **PROVED como implicación y converso bajo BASE, auditoría independiente aprobada (root, mapa e insight).** Véase `POWER_THREE_SECANTS_AUDIT_079.md`. Para la Phi real, las hipótesis073 están probadas; queda verificar g cóncava en el intervalo donde se quiera aplicar. No se afirma aquí el compacto real pendiente ni tres generadores globales. Papers intactos; sin campañas, nuevas mallas o matrices numéricas.

## 1. Antecedentes y diferencia precisa

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; releídos POWER_SCHUR_003, el jet y el falsificador de clase074, y073–078.003 refuta inferir orden tres desde M creciente, M/u decreciente e incluso M cóncava.074 conserva la hipótesis del potencial de073 y vuelve a refutar esa promoción. Ninguno se retira.

La nueva hipótesis concreta es la concavidad de

    g(x)=x b(x)=a sqrt(x)/M(sqrt(x))−1,
    b(x)=[a sqrt(x)/M(sqrt(x))−1]/x, a=M'(0)>0.

El jet074 identificaba g''<=0 como condición LOCAL necesaria de tres generadores. Aquí se demuestra que, JUNTO con las propiedades reales073, esa misma concavidad basta para TODOS los triples de nodos del intervalo, no sólo un jet confluyente. La prueba es una comparación algebraica de dos cotas de una diferencia de secantes. No exige la concavidad adicional de1/b propuesta078, ni invoca un principio de matrices de orden arbitrario.

## 2. Hipótesis mínimas y enunciado

Conservar la M real de073. Usar las propiedades ya probadas

    M>0, M'>0, M''<0, M(0)=0,
    M/u estrictamente decreciente.                    (BASE)

La última propiedad también se sigue de M estrictamente cóncava y M(0)=0. En particular g=a u/M−1 es positiva y estrictamente creciente en x=u². No se necesita la propiedad adicional b decreciente de077. Sea I un intervalo de nodos positivos. Suponer además que g es cóncava en el intervalo de cuadrados {u²:u∈I}. No se necesita suponer esa concavidad entre0 y el primer nodo.

Entonces, para cualesquiera tres nodos u1,u2,u3 en I, el kernel

    K_ij=[M(ui)+M(uj)]/(ui+uj)

es semidefinido positivo. Si los nodos son distintos y la diferencia de secantes de g definida abajo es estrictamente positiva, K es definida positiva. En particular, si g es estrictamente cóncava en el intervalo, todos sus triples distintos son definidos positivos.

También vale el CONVERSO dentro de BASE: todos los bloques de tres nodos de I son semidefinidos positivos SI Y SÓLO SI g es cóncava en el intervalo de cuadrados. Se prueba directamente en§7, sin un paso límite de jets. Esta equivalencia de un criterio escalar y los bloques3 bajo las hipótesis declaradas no afirma el signo de esa curvatura para la Phi real donde sigue pendiente.

Para exponentes originales ai=ui+1/2>1, este K es exactamente la forma completa de los tres exponenciales, incluyendo ARCH, polar y TODOS los contactos, según CONE001. El mapa exterior sólo introduce una congruencia diagonal positiva. No se sustituye la forma por un componente aislado.

## 3. Secantes y congruencia exacta

Ordenar primero0<u<v<w, y escribir g1=g(u²),g2=g(v²),g3=g(w²). Definir

    beta=(g2−g1)/(v²−u²)>0,
    delta=beta−(g3−g2)/(w²−v²)>=0,
    alpha=1+g1−beta u².

La positividad de beta proviene de g creciente; delta>=0 es exactamente la concavidad entre estos tres cuadrados. El caso débil beta=0 se trata aparte al final.

No se supone aquí alpha>=1. Aunque077 permitiría demostrarlo, es innecesario: M creciente dará directamente alpha>beta uv>0 en§4. Este cuidado permite utilizar sólo la concavidad de g en el intervalo de los tres cuadrados, sin extenderla hasta0 ni introducir una hipótesis adicional de077.

Los valores son

    g1=alpha−1+beta u²,
    g2=alpha−1+beta v²,
    g3=alpha−1+beta w²−delta(w²−v²).

Poner Hi=1+gi>0 y S=diag(H1,H2,H3)/sqrt(a). La congruencia T=SKS tiene entradas

    T_ij=1+[ui gj+uj gi]/(ui+uj).                      (CONGRUENCE)

Una expansión directa de su determinante da la identidad exacta

    det T=delta (u−v)²(v−w)²/(u+w)²
       ·{alpha beta(w²−u²)
                     −delta[alpha w²+beta u²v²]}.       (DET)

No se concluye su signo sólo de delta>=0: el segundo factor es la competencia que debe controlarse.

## 4. La concavidad de M controla la misma diferencia

M(v)>M(u), usando M(ui)=a ui/Hi, implica

    alpha>beta uv.                                    (INC)

En efecto vH1−uH2=(v−u)(alpha−beta uv)>0. Por tanto

    D2=alpha w+beta uv(u+v−w)
      =w(alpha−beta uv)+beta uv(u+v)>0.                 (DEN)

La concavidad de M en los nodos da

    (w−v)M(u)−(w−u)M(v)+(v−u)M(w)<=0.

Tras multiplicar por los denominadores positivos H1H2H3/a, el lado izquierdo es exactamente

    (u−v)(v−w)
      ·{delta(v+w)D2
        −beta(w−u)[alpha(u+v+w)−beta uvw]}.

El prefactor (u−v)(v−w) es positivo. Luego

    delta<=delta_conc
      =beta(w−u)[alpha(u+v+w)−beta uvw]/[(v+w)D2].      (CONC)

Su numerador también es positivo, pues

    alpha(u+v+w)−beta uvw
      =alpha(u+v)+w(alpha−beta uv)>0.

No se cambia la orientación de la desigualdad al despejar delta; DEN comprueba el signo que podría haberse perdido si w>u+v.

## 5. Comparación exacta con el umbral del determinante

El factor entre llaves en DET es positivo si

    delta<delta_crit
      =alpha beta(w²−u²)/[alpha w²+beta u²v²].          (CRIT)

La diferencia de los dos umbrales admite la factorización

    delta_crit−delta_conc
      = beta(w−u)uvw(alpha+beta u²)(alpha+beta v²)
        /{[alpha w²+beta u²v²](v+w)D2}>0.              (GAP)

Para verificar GAP basta multiplicar por los denominadores positivos: la identidad polinómica restante es

    alpha(w+u)(v+w)[alpha w+beta uv(u+v−w)]
      −[alpha(u+v+w)−beta uvw][alpha w²+beta u²v²]
       =uvw(alpha+beta u²)(alpha+beta v²).

Así CONC implica delta<delta_crit. El factor competidor de DET es estrictamente positivo. Si delta>0, det T>0 y por congruencia det K>0. Las diagonales y los menores de dos puntos son positivos por073. El complemento de Schur del primer elemento tiene diagonal positiva y determinante positivo; por tanto es definido positivo y K también. Este último paso es álgebra de una matriz2x2, no una hipótesis de positividad del kernel completo.

## 6. Degeneraciones y nodos coincidentes

Si beta>0 pero delta=0, los datos g son afines en x sobre los tres nodos. CONGRUENCE se reduce exactamente a

    T=alpha·11^t+beta·(u,v,w)^t(u,v,w),

que es semidefinida positiva y tiene rango2 para nodos distintos. No se declara definida positiva en este caso.

Si se permiten las versiones no estrictas de BASE y beta=0, g creciente y cóncava fuerza g1=g2=g3 y delta=0. Entonces T=(1+g1)11^t es semidefinida positiva de rango1. En la aplicación real BASE es estricta y beta=0 no ocurre, pero no se divide por beta para ocultar ese borde.

Si dos o tres nodos coinciden, se combinan sus coeficientes y queda un bloque de uno o dos generadores ya positivo por073. La matriz con columnas repetidas es semidefinida positiva. La energía estricta corresponde a la FUNCIÓN representada no nula, no a cualquier vector de coeficientes no nulo que pueda representar cero.

## 7. Converso: el signo de la diferencia de secantes es necesario

Conservar BASE y tres nodos distintos, pero no suponer delta>=0. La positividad de beta y la desigualdad alpha>beta uv>0 siguen siendo ciertas: sólo usan g creciente y M creciente en los dos primeros nodos. Si delta<0, el factor entre llaves de DET es estrictamente positivo,

    alpha beta(w²−u²)−delta[alpha w²+beta u²v²]>0.

Por tanto det T<0 y det K<0. No puede ser un bloque semidefinido positivo. Así la positividad de TODOS los triples obliga a delta>=0 para todo u<v<w, que es exactamente la concavidad de g en los cuadrados. Junto con la implicación ya demostrada, queda la equivalencia dentro de BASE. Más precisamente, para cada triple el signo del determinante coincide con el de delta; delta=0 es el caso de rango2 descrito arriba.

No se usa una conclusión de mayor orden ni se deduce concavidad de los pares positivos: la nueva obligación es justamente el signo de estas secantes de g.

## 8. Aplicación actual y obligación reducida

Para la Phi real,073 aporta todas las propiedades de BASE.077 motivó las coordenadas de cociente y aporta resultados adicionales válidos, pero su propiedad b decreciente NO es necesaria en la prueba mínima de079. Por tanto la ÚNICA obligación adicional de este criterio para tres generadores es g''<=0 en el intervalo deseado. La concavidad de1/b no es necesaria para esta prueba y queda como propiedad separada, no como requisito pendiente del criterio.

078 ya prueba g''<0 para u>=63/2 mediante la aritmética completa y un margen algebraico explícito. Se obtiene así una demostración analítica de los triples con ui>=63/2. Esa región NO es nueva cobertura:053 ya probó trece polos arbitrarios en ese rango. El resultado nuevo de079 es reducir la obligación GLOBAL de tres generadores a un intervalo acotado de UNA curvatura real. Para los exponentes admisibles ai>1 sólo se necesita 1/2<u<63/2, sin necesitar la segunda concavidad ni una sucesión de matrices finitas.

No se afirma aquí g''<=0 en ese intervalo pendiente, tres generadores para todos ai>1, positividad de cuatro o todos los órdenes, ni una nueva ventana temporal. Las identidades se verificaron simbólicamente como comprobación auxiliar; la prueba está íntegramente dada por las factorizaciones exactas anteriores, sin matrices numéricas o campañas de parámetros.
