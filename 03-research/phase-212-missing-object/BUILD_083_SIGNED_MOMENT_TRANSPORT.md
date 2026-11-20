# Construcción 083 — Transporte de momentos entre las zonas de signo

Estado: identidades, perfil polinómico, cobertura y test de indefinición cruzada revisados independientemente. No hay prueba del signo de la forma. Se abandona la extracción de un cuadrado que sólo anula perfiles aproximados.

## Perfil y dos medidas balanceadas

Elegir un perfil real g∈C_c∞(I)∩P_T, no nulo, mediante un corte suave par y un corrector central suave par normalizado en cosh(t/2), como en la modificación final de BUILD080 (no mediante Q aplicado al corte duro). No se supone que g sea un autovector ni que A g=0. Escribir g=g+−g−, con ambas partes no negativas y soportes disjuntos.

Para σ=±1 poner

    mσ=∫e^(σt/2)g+(t)dt=∫e^(σt/2)g−(t)dt>0,
    dμσ,±(t)=e^(σt/2)g±(t)dt/mσ.

Son probabilidades. Para F=g h con h suave acotada y F∈P_T,

    ∫h dμσ,+=∫h dμσ,−=:cσ(h).                           (1)

No se considera todavía todo el dominio: este portador de productos puede no ser denso si g se anula en un intervalo. No se omite ese problema de cobertura.

## Identidad exacta de transporte de una diferencia

Si x está en {g>0}, y en {g<0}, definir

    Aσ(x;h)=∫[h(x)−h(z)]dμσ,+(z),
    Bσ(y;h)=∫[h(w)−h(y)]dμσ,−(w).

Por(1), h(x)−h(y)=Aσ(x;h)+Bσ(y;h). Por tanto

    |h(x)−h(y)|²=|Aσ|²+|Bσ|²+2Re(Aσ conjugado(Bσ)).       (2)

La interacción entre signos queda expresada en diferencias internas a cada zona, pero el término mixto se conserva y no tiene signo. No se aplica Jensen ni se descarta ese término.

Se pueden combinar ambas identidades: para cualquier θ(x,y) real,

    h(x)−h(y)=θ(A++B+)+(1−θ)(A−+B−).                    (3)

Ésta es una libertad concreta de diseño basada en AMBAS restricciones. Elegir θ no produce por sí solo positividad; su papel posible sería cancelar cruces con la interacción arquimediana y aritmética completa.

## Forma de energía sin suponer estado fundamental

Para perfiles y tests suaves, la identidad de producto para la forma a_T da

    a_T(g h)=∫g(t)(H_T g)(t)|h(t)|²dt
       +(1/4)∬ K(|t−s|)g(t)g(s)|h(t)−h(s)|²dt ds
       +Σ_n [Λ(n)/sqrt(n)]∫g(t)g(t−log n)|h(t)−h(t−log n)|²dt. (4)

Las funciones se extienden por cero. H_T g denota el operador de la forma completa sobre L²(I), SIN compresión primitiva; no se anula ni se supone que tenga signo. El coeficiente del contacto es v_n/2=Λ(n)/sqrt(n). La identidad se justifica primero con cortes de la singularidad continua y luego por convergencia de las diferencias suaves.

En(4), las interacciones internas a cada signo son positivas y las que cruzan signos son negativas. La propuesta es insertar(3) en TODAS las interacciones negativas, manteniendo las mismas funciones θ y ambos términos de promedio, y comparar los coeficientes resultantes con las interacciones internas. El potencial g H_T g permanece en el cálculo: omitirlo equivaldría a suponer un estado fundamental inexistente en la ventana.

## Primer resultado y obligación restante

Las ecuaciones(1)-(3) dan un transporte exacto, no una cota. El signo requiere construir θ y una identidad conjunta donde el potencial y los términos mixtos queden controlados. Aún no se ha elegido θ con esa propiedad.

El transporte de momentos funciona para cualquier peso y no separa falsificadores. Cualquier selección de θ basada sólo en g y los momentos, sin usar H_Tg y los contactos exactos en la misma cancelación, no explicaría el signo aritmético. El diseño debe resolver también la cobertura del portador, no sólo una subclase de productos.


## Simplificación del parámetro de mezcla

La revisión verifica Aσ(x;h)=h(x)−cσ(h) y Bσ(y;h)=cσ(h)−h(y). En(3), θ sólo reemplaza el centro por cθ=θc++(1−θ)c−. El término mixto permanece. No se afirma que esta libertad ya constituya una operación de signo.

## Perfil polinómico con cobertura densa

Se reemplaza el perfil compacto interior inicial por el siguiente perfil explícito en toda la ventana:

    ψ_T(t)=(T²−t²)² para |t|<T, cero fuera,
    g_T=(1/4−∂²)ψ_T,
    g_T(t)=(T²−t²)²/4+4T²−12t² para |t|<T, cero fuera.  (5)

Como ψ_T y ψ_T′ se anulan en ambos extremos, la derivada segunda distribucional no añade masas. Integrando dos veces por partes se obtiene ∫g_T e^(±t/2)=0 exactamente.

En (0,T), g_T′(t)=−t(T²−t²+24)<0; g_T(0)>0 y g_T(T−)=−8T²<0. Por tanto tiene exactamente dos ceros interiores simples ±r_T, donde

    r_T²=T²+24−sqrt(32T²+576),  0<r_T<T.                 (6)

El signo positivo está en (-r_T,r_T); el negativo en las dos franjas exteriores. Las medidas μσ,± están así completamente especificadas por polinomios y exponenciales. g_T es BV compacto; su transformada es O((1+|τ|)^(-1)), y por ello log(2+|τ|)·ĝ_T∈L². En particular el operador completo H_Tg_T está definido en L²(I). No se comprime ese operador antes de formar el potencial de(4).

Para justificar la cobertura, tomar F suave primitivo y compacto interior. Se eliminan vecindades de radio ε de ±r_T mediante cortes suaves. El error es suma de dos funciones F(t)η((t−r)/ε), cuya norma H^s es O(ε^(1/2−s)) para cualquier 0<s<1/2 (cambio de escala y cotas uniformes de las envolventes suaves). Luego converge a cero también en la norma logarítmica de la forma. Corregir los dos momentos mediante dos bumps fijos soportados lejos de los ceros, con matriz de momentos invertible. Sus coeficientes tienden a cero. Los tests corregidos F_ε son primitivos, se anulan cerca de los ceros y del borde, y convergen a F en norma de forma.

Ahora h_ε=F_ε/g_T es suave compacto, pues la división sólo ocurre lejos de los dos ceros. Así la clase de productos g_T h que son primitivos contiene un núcleo denso de la forma. Esta es una justificación de cobertura, NO de positividad de(4). En esa clase la identidad de producto se obtiene por truncación del núcleo continuo y convergencia de las formas; el potencial H_Tg_T se conserva íntegro.

La verificación independiente confirma(5)-(6), el dominio de operador y la cobertura: PROVED como resultado auxiliar, sin signo global. El perfil polinómico no está elegido por semejanza con un autovector ni por optimización de a_T.


En el subespacio donde los cuatro promedios de h frente a μσ,± son cero, ambos centros cσ son cero. Allí Aσ=h(x), Bσ=−h(y) para ambos signos y θ no modifica el término mixto. Este subespacio debe tratarse directamente con el potencial y las interacciones de(4); ninguna elección de centro lo resuelve automáticamente.


## Cancelación efectiva del primer modo arquimediano entre zonas

Cálculo revisado: PROVED como descomposición auxiliar. Usar tests del núcleo construido que se anulan en vecindades de ±r_T. Escribir F=F_L+F_C+F_R según las tres regiones (-T,-r_T),(-r_T,r_T),(r_T,T). Los soportes de las tres piezas quedan separados. Poner a_j=2j+1/2 y

    A_j^D=∫_D e^(a_j t)F(t)dt,
    B_j^D=∫_D e^(-a_j t)F(t)dt, D=L,C,R.

La parte de la forma que aparea el centro con las dos regiones exteriores es exactamente

    Cross(F)=−2 Re Σ_{j≥0}[A_j^L conjugado(B_j^C)
                                +A_j^C conjugado(B_j^R)]
       −2Σ_n Λ(n)/sqrt(n) Re ∫[F_C(t)conjugado(F_L(t−log n))
                              +F_R(t)conjugado(F_C(t−log n))]dt. (7)

Es una descomposición del apareamiento de F, no sólo de la energía firmada de h; el potencial de(4) no se descarta. La serie continua converge absolutamente por separación de soportes y K(u)=2Σ_j e^(-a_j u). No se incluyen en Cross las interacciones L–R, que pertenecen a las dos zonas de igual signo de g.

En el subespacio ya identificado donde los cuatro promedios de h frente a μσ,± son cero, F_C tiene ambos momentos nulos: A_0^C=B_0^C=0. Por tanto el término j=0 de(7) DESAPARECE exactamente. Esto usa ambos momentos del centro, no sólo los dos momentos globales de F. No se afirma esa desaparición para todo F primitivo.

El resto escrito es

    Cross(F)=−2 Re Σ_{j≥1}[A_j^L conjugado(B_j^C)
                                +A_j^C conjugado(B_j^R)]
              − contactos entre centro y exteriores.                 (8)

Los momentos superiores no se anulan por las restricciones dadas. Tampoco se anulan los contactos. La ecuación(8) localiza qué interacción queda por compensar; no constituye una cota ni una identidad positiva.

Para el portador general hay que conservar además el término j=0 de(7). Una futura construcción no puede promover la cancelación de este subespacio al portador completo sin aportar su correspondiente corrección.

## Test analítico del resto cruzado después de cancelar j=0

Las ecuaciones(7)-(8), su convergencia y alcance fueron revisados independientemente: PROVED como descomposición auxiliar, sin signo global.

Test revisado: PROVED como indefinición del resto cruzado. Elegir dos intervalos pequeños J_L⊂L y J_C⊂C, separados de los ceros y del borde. Pueden elegirse de modo que todas las diferencias t−s con t∈J_C,s∈J_L eviten los finitos log n<2T: basta escoger dos centros cuya diferencia no sea un contacto y reducir los intervalos.

Sean η_L,η_C bumps suaves no negativos, no nulos, soportados en esos intervalos. Definir

    F_D=(1/4−∂²)η_D, D=L,C, y F_R=0.

Cada F_D es primitivo por integración por partes. Los cuatro promedios de h=(F_L+F_C)/g_T se anulan: los del centro por F_C primitivo, los del exterior por F_L primitivo. h es suave compacto lejos de los ceros de g_T.

Para a_j=2j+1/2,

    A_j^L=(1/4−a_j²)∫e^(a_jt)η_L(t)dt,
    B_j^C=(1/4−a_j²)∫e^(-a_jt)η_C(t)dt.

El producto A_j^L B_j^C es estrictamente positivo para todo j≥1. Los contactos cruzados son cero por construcción. Por tanto

    Cross(F_L+F_C)=−2Σ_{j≥1}A_j^L B_j^C<0.

Sustituir F_C por −F_C conserva todos los momentos, soportes y energías individuales, y cambia el signo de Cross. El resto cruzado es por ello indefinido incluso en el subespacio donde θ no actúa y el modo j=0 ya desapareció.

Esto NO refuta a_T≥0: las contribuciones a_T(F_L) y a_T(F_C) permanecen. Sí impide completar el diseño afirmando que el resto cruzado de(8) tiene por sí mismo signo favorable. Una reparación debe conservar y usar esas energías individuales en la misma identidad, con los contactos pertinentes dentro de cada pieza. No se ha obtenido todavía esa identidad.


## Estado constructivo tras la revisión

No se ha construido una elección de θ ni otro operador que compense el resto cruzado con las energías propias. La cobertura y la cancelación parcial están probadas; la dominación global no lo está. El test de indefinición sólo descarta firmar Cross por separado. No excluye una identidad conjunta y no acredita que una tal identidad exista en esta clase.

No se propone un nuevo diseño hasta escribir una operación adicional concreta sobre las energías propias y el apareamiento cruzado. Reformular su dominación como otra norma, discriminante o complemento de Schur no resolvería ese paso.

## Truncación controlada de los acoplamientos arquimedianos separados

Estado: PROVED como estimación auxiliar; ecuaciones (9)-(14), constantes, rango y alcance de densidad revisados independientemente. No es un nuevo mecanismo de signo. Bajo la autorización posterior de resolver subproblemas, se aborda el cálculo infinito de (7), conservando los contactos exactos. Antecedente inmediato: (7)-(8) y su prueba de convergencia; diferencia: se proporciona ahora una cota en norma de operador, uniforme en los tests para huecos fijos, y un criterio suficiente con presupuesto explícito de error. No se atribuye novedad a la estimación geométrica.

Fijar tres subintervalos ordenados I_L,I_C,I_R dentro de las respectivas zonas, con distancias δ_L=inf I_C−sup I_L>0 y δ_R=inf I_R−sup I_C>0. Trabajar con F_D soportado en I_D y F=F_L+F_C+F_R primitivo. No se exige que cada pieza sea primitiva. Poner a_j=2j+1/2. Para J≥0 entero, retener los términos 0≤j<J en la parte arquimediana de (7). El resto es

    R_J(F)=−2 Re Σ_{j≥J}(A_j^L conjugado(B_j^C)
                                   +A_j^C conjugado(B_j^R)).          (9)

Para dos intervalos ordenados I_D,I_E con distancia δ y a>0, el operador de rango uno con núcleo exp(−a(t−s)), s∈I_D,t∈I_E, tiene norma

    ||exp(a·)||_{L²(I_D)} ||exp(−a·)||_{L²(I_E)}
          ≤ exp(−aδ)/(2a).                                         (10)

Prueba: si b=sup I_D y c=inf I_E, las dos integrales de cuadrados están acotadas por exp(2ab)/(2a) y exp(−2ac)/(2a). Esto no depende de las longitudes ni del tamaño de T.

En consecuencia definir

    h_J(δ)=exp(−a_J δ)/[2 a_J(1−exp(−2δ))],
    ε_J=sqrt(h_J(δ_L)²+h_J(δ_R)²).

Sumando (10), usando a_j≥a_J, se obtiene

    |R_J(F)| ≤ 2h_J(δ_L)||F_L||||F_C||
                     +2h_J(δ_R)||F_C||||F_R||
              ≤ ε_J ||F||².                                       (11)

La última desigualdad resulta de Cauchy–Schwarz en las dos componentes exteriores y 2xy≤x²+y². La suma de operadores converge absolutamente en norma. Su forma hermítica tiene, por (11), norma a lo sumo ε_J; no se infiere ningún signo puntual ni operatorial del resto.

Sea a_T^[J] la forma completa a_T en este portador, sustituyendo ÚNICAMENTE el acoplamiento arquimediano L–C y C–R por sus primeros J modos. Permanecen intactos: las tres energías propias, el acoplamiento L–R completo, todos los contactos (incluidos los que cruzan zonas), y los dos momentos globales. Entonces

    a_T^[J](F)−ε_J||F||² ≤ a_T(F)
                             ≤ a_T^[J](F)+ε_J||F||².                (12)

El bloque arquimediano retenido L–C/C–R tiene rango a lo sumo 4J. Esto NO vuelve finito-dimensional a a_T^[J]: los contactos y las energías propias siguen actuando sobre espacios infinitos.

Para δ=min(δ_L,δ_R) y cualquier η>0, una elección suficiente explícita para ε_J≤η es

    J ≥ max(0, ceil(log(sqrt(2)/(η(1−exp(−2δ))))/(2δ))). (13)

En efecto 2a_J≥1 y exp(−a_Jδ)≤exp(−2Jδ). (13) es una elección conservadora, no óptima.

Obligación reducida y alcance: una prueba independiente de a_T^[J](F)≥ε_J||F||² sobre el portador considerado certificaría a_T≥0 allí. No se ha demostrado esa desigualdad. El error puede hacerse tan pequeño como se prescriba con huecos fijos; no se supone que exista un margen positivo que lo absorba. Cuando los huecos tienden a cero, J debe crecer: no hay truncación uniforme acreditada. La densidad ya probada permite pasar al portador original SI se obtiene el signo en toda la familia de portadores separados; la densidad por sí sola no produce esas pruebas.

Esta estimación sólo usa K, por lo que también vale para los falsificadores. Su utilidad es controlar una cola al comprobar futuras compensaciones, no distinguir el peso verdadero ni resolver por sí sola el signo global.

Puede evitarse repartir la misma penalización ε_J entre las tres regiones. Para cualesquiera p_L,p_R>0, (11) y dos cuadrados escalares dan

    |R_J(F)| ≤ p_L||F_L||²+p_R||F_R||²
            +(h_J(δ_L)²/p_L+h_J(δ_R)²/p_R)||F_C||².                 (14)

Así se obtiene otro minorante explícito restando a a_T^[J] las tres penalizaciones de (14). Los parámetros p_L,p_R permiten asignar el coste de cola a las regiones donde una futura prueba disponga de reserva; no se presupone tal reserva. Es una aplicación exacta de Young, no una nueva desigualdad aritmética. Todos los términos retenidos permanecen sin estimar.

## Cierre de los huecos: control relativo a la norma logarítmica

Estado: PROVED como estimación auxiliar, con revisión independiente de (15)-(22), constantes, convergencia y reparación de momentos. Subproblema siguiente de (9)-(14): eliminar la separación positiva entre regiones. Antecedentes: (10)-(12) sólo dan una cota para huecos fijos; el corpus de transmisión logarítmica (fase 121, citado en P124_008 §1) ya contiene operadores de Carleman. No se reclama novedad del ingrediente. Aquí se da una estimación cuantitativa de ESTA cola modal sobre el portador completo, sin huecos ni regularidad Sobolev positiva exigida.

En una frontera b entre dos intervalos adyacentes escribir x=b−s>0, y=t−b>0. El núcleo exacto del operador de cola es, para J≥1,

    H_J(x,y)=Σ_{j≥J}exp(−a_j(x+y))
      =exp(−a_J(x+y))/(1−exp(−2(x+y)))
      =exp(−b_J(x+y))/(2sinh(x+y)), b_J=2J−1/2>0.       (15)

Por sinh u≥u,

    0≤H_J(x,y)≤exp(−b_Jx)exp(−b_Jy)/(2(x+y)).           (16)

El operador de núcleo 1/(x+y) en la semirrecta tiene norma ≤π: el test de Schur con peso x^(−1/2) usa la integral ∫_0^∞ y^(−1/2)/(x+y)dy=π x^(−1/2), obtenida por y=xz². Basta esta cota, no se usa igualdad de norma. De (16), para el término cruzado de una frontera,

    |Cross_J,b(F)|≤π||exp(−b_Jx)F_left|| ||exp(−b_Jy)F_right||
                ≤(π/2)∫exp(−2b_J|t−b|)|F(t)|²dt.      (17)

La integral puede extenderse a toda R. Esta demostración funciona con funciones complejas tomando módulos. También justifica la convergencia del apareamiento modal por dominación, aunque la suma de normas de los rangos uno ya no converja. Para las dos fronteras se suman sus dos cotas (17).

Definir la energía logarítmica positiva, con F extendida por cero,

    L(F)=(1/(2π))∫log(2+|τ|)|Fhat(τ)|²dτ,
    Fhat(τ)=∫F(t)exp(iτt)dt.

Es finita en el dominio de forma declarado, sin suponer signo de a_T. Para cualquier conjunto medible E de longitud |E| y cualquier R>0, separar frecuencias |τ|≤R y |τ|>R. Plancherel y Cauchy–Schwarz dan

    ∫_E|F|² ≤ (2|E|R/π)||F||²+2L(F)/log(2+R).         (18)

En efecto, el trozo de baja frecuencia satisface ||F_low||∞≤sqrt(R/π)||F||; el de alta frecuencia tiene norma cuadrada ≤L(F)/log(2+R). Se usa |u+v|²≤2|u|²+2|v|². No se aplica esta estimación a piezas recortadas; se aplica a la F original.

Para r>0, partir la integral de (17) en |t−b|<r y su complemento. El primer conjunto tiene longitud 2r; en el segundo el peso es ≤exp(−2b_Jr). Sumando ambas fronteras,

    |R_J(F)|≤[4rR+πexp(−2b_Jr)]||F||²
                         +[2π/log(2+R)]L(F).           (19)

Elegir r=J^(−1/2), R=J^(1/4). Se obtiene, uniformemente en T y en la posición de las fronteras,

    |R_J(F)|≤d_J||F||²+e_J L(F),                       (20)
    d_J=4J^(−1/4)+πexp(−(4J−1)/sqrt(J)),
    e_J=2π/log(2+J^(1/4)).

Ambas constantes tienden a cero. Esta es convergencia en la norma de formas relativa a ||F||²+L(F), SIN huecos. Para todo F∈P_T en el dominio de forma, definir a_T^[J]=a_T−R_J, donde el resto cruzado es el operador acotado de (15). Entonces el minorante explícito

    a_T(F)≥a_T^[J](F)−d_J||F||²−e_J L(F)               (21)

vale sobre el portador completo. Se define por sustracción de una forma acotada; no es necesario suponer regularidad adicional de las tres piezas recortadas. Sobre el núcleo suave coincide con sustituir los enlaces arquimedianos adyacentes por los primeros J modos. Contactos, dos momentos, energías propias y enlace L–R permanecen intactos.

### Por qué el cierre de huecos no converge a cero en norma L²

Para un J fijo, en una sola frontera tomar F_ε igual a ε^(−1/2) en ambos intervalos de longitud ε contiguos a b, y cero fuera. Tiene norma cuadrada 2. Reescalando x=εu,y=εv en (15) y usando (16),

    <F_right,H_J F_left> → ∫_0^1∫_0^1[2(u+v)]^(−1)dudv=log 2.

Por tanto Cross_J,b(F_ε)→−2log 2. Para imponer ambos momentos, restar dos bumps fijos con matriz de momentos invertible y soportes alejados de las fronteras. Los momentos de F_ε son O(sqrt(ε)), por lo que el corrector tiene norma O(sqrt(ε)). Como la cola total es acotada en L² por (17), corregir cambia su valor en o(1). La otra frontera no aporta antes de la corrección si ε es pequeño. Los tests corregidos pertenecen al dominio logarítmico (son BV compactos) y son primitivos. Así, para cada J,

    sup_{F∈P_T, F≠0}|R_J(F)|/||F||² ≥ log 2.           (22)

Existe la cota uniforme |R_J(F)|≤π||F||² por (17), pero no una cota c_J||F||² con c_J→0. No hay convergencia uniforme a cero en norma L², ni siquiera después de los dos momentos. Esto no refuta la forma completa: sólo explica por qué el control correcto al cerrar huecos es (20), con energía logarítmica.

### Obligación que permanece

(21) elimina el requisito de huecos y cuantifica el error en todo el dominio; no prueba que el minorante sea positivo. Sigue faltando compensar los contactos y los modos retenidos con suficiente reserva para el coste d_J||F||²+e_J L(F), o hallar una identidad que evite ese coste. La convergencia de (20) no basta para inferir signo: no se intercambia un límite con una supuesta cota inferior positiva. La estimación vale también en los falsificadores, y no constituye una separación aritmética ni una prueba global.

## Pegado exacto en una frontera, sin coste de truncación

Estado: PROVED como descomposición auxiliar; (23)-(29), factores, dominios y paso al límite revisados independientemente. Antecedentes: (15)-(21), la descomposición positiva del núcleo K de P47 y 212-78. No se presenta como nueva fuente de signo ni como una prueba por reflexión de la forma aritmética. La operación adicional consiste en conservar el cuadrado de diferencia de momentos en una frontera y absorber exactamente sus dos términos diagonales en energías reflejadas. A diferencia de (21), no deja una penalización de truncación. El residuo regional completo se escribe, sin suponerlo positivo.

Fijar b∈(−T,T) y definir en x>0, con extensión por cero,

    f_−(x)=F(b−x), f_+(x)=F(b+x),
    α_j(f)=∫_0^∞ exp(−a_jx)f(x)dx, a_j=2j+1/2.

Para a>0 poner

    k_a^N(x,y)=exp(−a|x−y|)+exp(−a(x+y)),
    N_a(f)=(1/2)∫_0^∞∫_0^∞ k_a^N(x,y)|f(x)−f(y)|²dxdy≥0. (23)

La suma de fila de k_a^N es exactamente 2/a. Por tanto

    N_a(f)=(2/a)||f||²−∫∫exp(−a|x−y|)f(x)conjugado(f(y))dxdy
                                      −|α_a(f)|².

El j-ésimo sumando de Arch−C0||F||² es

    E_j(F)=(2/a_j)||F||²−∫_R∫_R exp(−a_j|t−s|)F(t)conjugado(F(s))dtds.

Al separar las dos semirrectas, el término cruzado es −2 Re α_j(f_−)conjugado(α_j(f_+)). Completando el cuadrado se obtiene la identidad EXACTA

    E_j(F)=N_{a_j}(f_−)+N_{a_j}(f_+)
                                 +|α_j(f_−)−α_j(f_+)|².              (24)

Todos los términos de (24) son no negativos. La identidad para sumas finitas pasa al límite por monotonía de los tres términos. Como Σ_jE_j(F)=Arch(F)−C0||F||² es finita en el dominio de forma,

    Arch(F)=C0||F||²+N(f_−)+N(f_+)+||V_b^arch F||²,                 (25)
    N(f)=Σ_{j≥0}N_{a_j}(f),
    V_b^arch F=(α_j(f_−)−α_j(f_+))_{j≥0}.

No se separan diagonales divergentes al sumar. La prueba vale primero para cualquier F∈L² en cada modo y luego para todo F del dominio logarítmico. En particular (25) demuestra finitud de las energías N de las piezas, sin exigir que el corte de F tenga regularidad adicional.

### Contactos en el mismo pegado

Escribir w_n=Λ(n)/sqrt(n), l_n=log n, n<exp(2T). Para f en la semirrecta definir c_f(l)=∫_R f(x)conjugado(f(x−l))dx, con extensión cero. La parte real del contacto se separa como

    Re c_F(l)=Re c_{f_−}(l)+Re c_{f_+}(l)
                    +Re ∫_0^l f_−(x)conjugado(f_+(l−x))dx.          (26)

El último término se incluye en el operador explícito de pegado

    (V_b^prime F)_n(x)=sqrt(w_n)[f_−(x)−f_+(l_n−x)], 0<x<l_n.

Su cuadrado es exactamente la contribución cruzada del peine MÁS las penalizaciones w_n∫_0^{l_n}(|f_−|²+|f_+|²). Definir la forma regional

    q_T(f)=C0||f||²+N(f)−2Σ_n w_n Re c_f(l_n)
                                     −Σ_n w_n∫_0^{l_n}|f(x)|²dx.   (27)

Entonces la forma COMPLETA satisface

    a_T(F)=q_T(f_−)+q_T(f_+)
                     +||V_b^arch F||²+||V_b^prime F||².             (28)

No hay resto omitido ni error numérico: están todos los contactos activos y todas las contribuciones arquimedianas. Las sumas de contactos son finitas. N(f_±) es finita por (25), de modo que (27)-(28) están definidas en el dominio original.

### Los dos momentos y el residuo pendiente

Las condiciones primitivas equivalen, sin importar b, a

    ∫_0^∞ cosh(x/2)(f_−(x)+f_+(x))dx=0,
    ∫_0^∞ sinh(x/2)(f_+(x)−f_−(x))dx=0.                             (29)

Se obtiene (29) multiplicando los momentos originales por exp(∓b/2) y sumando/restando. Las piezas tienen soporte finito. No se impone que cada pieza satisfaga por separado los dos momentos.

El candidato V_b=(V_b^arch,V_b^prime) tiene, por (28), residuo EXACTO q_T(f_−)+q_T(f_+). No se sabe que este residuo sea no negativo, ni se deduce de N≥0: C0<0 y los términos aritméticos de (27) permanecen. Si el residuo resulta negativo, los cuadrados de pegado podrían compensarlo; no se exige su positividad como condición necesaria del objetivo.

Este diseño resuelve sólo el pegado arquimediano y escribe los contactos con sus penalizaciones exactas. Es genérico para pesos no negativos y retardos positivos, también para los falsificadores. No satisface todavía la exigencia final de un mecanismo aritmético no lineal que dé el signo. La próxima obligación concreta es controlar (27) bajo las dos condiciones acopladas (29), conservando los cuadrados de (28); no se declara esa obligación resuelta ni se llama al residuo una energía positiva.


### Diagnóstico del cuadrado de pegado

NUMÉRICO, no certificado: `build_079_data/check_gluing.py` evalúa el canal aritmético con b=0 sobre el vector par guardado T=0.8, reconstruido en su base por tramos y corregido en ambos momentos. Cuadraturas Gauss de órdenes 64 y 96, separadas en todos los puntos de cambio de tramo originales y reflejados, dan norma 1 (error <4e−15), momentos <3e−17 y

    ||V_b^prime F||² ≈ 1.40645379239075,
    canales n=2,3,4: 0.45288941915506, 0.60700843323509, 0.34655594000061.

La energía guardada es 5.29432592315062e−12; no se recalculó ni recertificó aquí. Los valores son evidencia numérica de que el candidato V_b extrae demasiada energía en esta ventana. No se debe proponer q_T(f_−)+q_T(f_+)≥0 como mecanismo a partir de esta descomposición. La identidad exacta sigue válida, pero en este diagnóstico los cuadrados positivos necesitan una cancelación de orden uno con el residuo regional. El avance auxiliar es escribir el pegado sin error de truncación, no haber ganado una reserva positiva para el signo global.

### Diagnóstico del sector negativo regional, T=0.8

NUMÉRICO, sin certificación de índice continuo. `build_079_data/check_regional.py` construye matrices de q_T en polinomios de Legendre ortonormales sobre (0,T), elimina el momento cosh por QR y añade el cuadrado de pegado. La inmersión par isométrica es F(t)=f(|t|)/sqrt(2); en estas coordenadas V_arch=0 y

    A_even=q_T+B,
    B(f)=(1/2)Σ_n w_n∫_0^{l_n}|f(x)−f(l_n−x)|²dx.

Se revisaron independientemente los factores y las fórmulas del script. La energía N se integra usando H0(u)=exp(−u/2)/(1−exp(−2u)) y la cola exacta ∫_u^∞H0=atanh(exp(−u/2))+atan(exp(−u/2)). La cuadratura interna elimina el valor diagonal (su contribución a las diferencias es cero), pero conserva error cerca de esa diagonal y del extremo logarítmico. No es aritmética de intervalos.

| Grado | Orden Gauss | Negativos de la matriz q | Séptimo autovalor de q | Mínimo calculado A_even |
|---|---|---|---|---|
| 16 | 128 | 6 | 0.00300021 | −4.37846e−4 |
| 24 | 256 | 7 | −8.31625e−5 | −1.04833e−4 |
| 24 | 512 | 6 | 0.000233080 | −2.56044e−5 |
| 32 | 512 | 7 | −0.00101102 | −2.56078e−5 |

La comparación de las dos filas de grado24 aísla la variación de cuadratura; las dos de orden512 aíslan la de grado. El séptimo signo NO está resuelto. Los primeros seis autovalores son aproximadamente −1.637, −1.235, −0.632, −0.507, −0.182, −0.070: constituyen una señal negativa robusta a estas variaciones, no una prueba rigurosa de seis direcciones continuas. No se concluye que el índice continuo sea seis ni siete. Los mínimos de A_even son errores/aproximaciones sin signo certificado y son muchísimo mayores que la escala del fondo guardado; no refutan la positividad.

En cada matriz se separaron las direcciones negativas de q y su complemento. Escribir A=q+B por bloques da el Schur exacto de esa matriz

    S=A_--−B_-+ A_++^(-1) B_+-.

Los mínimos calculados de A_++ estuvieron entre0.855 y0.969; residuos de solve <2.1e−16. El bloque A_-- solo tuvo mínimo positivo entre2.87e−4 y8.48e−4, mientras la corrección de Schur tuvo norma entre0.224 y0.245. Por tanto comprobar sólo el bloque negativo original después de añadir B NO justifica el signo de la matriz completa. No se descarta este acoplamiento ni se interpreta la resta de Schur como una energía positiva adicional.

Este cálculo no aporta un mecanismo nuevo: concreta que la compensación regional involucra varias direcciones y su acoplamiento al complemento. Para convertir el diagnóstico en un resultado hace falta certificar una matriz de tests negativos y controlar el resto; no se sustituye esa tarea por el conteo flotante. El signo global y una fórmula aritmética independiente para la transferencia siguen abiertos.

## Tres direcciones regionales negativas con cota analítica e intervalos

Estado: PROVED mediante mayorante analítico y certificado intervalar PASS, revisado y reproducido independientemente; constante 1/600 también revisada. La certificación computacional depende de la implementación de mpmath.iv. Resultado regional, no negatividad de a_T. Antecedente inmediato: diagnóstico anterior de q_T en T=0.8. El cambio consiste en sustituir toda cuadratura singular por un mayorante explícito con integrales elementales y fijar los tests racionalmente antes de certificar. No se necesita conocer autovectores de la forma objetivo.

Fijar T=4/5. Para f(x)=p(x/T) en (0,T), cero fuera, definir en el cuadrado unidad

    I_−(p)=∫∫|p(z)−p(v)|²/|z−v| dzdv,
    I_+(p)=∫∫|p(z)−p(v)|²/(z+v) dzdv.

Con H0(u)=Σ_j exp(−a_j u), para u>0,

    H0(u)=1/(4sinh(u/2))+1/(4cosh(u/2))≤1/(2u)+1/4,
    ∫_u^∞H0(v)dv=atanh(exp(−u/2))+atan(exp(−u/2))
                  ≤(1/2)log(4/u)+u/8+π/4.                         (30)

La segunda cota usa coth(u/4)≤1+4/u y log(1+u/4)≤u/4. Separando el interior (0,T) de su exterior en N, y usando C0=−γ−π/2−3log2−logπ, se obtiene el mayorante cuadrático

    q_T(f)≤U(p),
    U(p)=T cbar∫|p|²−(T/2)∫|p|²log(1−z²)
         +(T/4)(I_−(p)+I_+(p))
         +(T²/2)(∫|p|²−|∫p|²)
         −2Σ_n w_n Re c_f(log n)−Σ_n w_n∫_0^{log n}|f(x)|²dx,
    cbar=−γ−log(2π)+T/4−log T.                                    (31)

Todos los integrales sin límites en z se toman sobre (0,1). En los dos últimos términos f está extendida por cero. Contactos activos: n=2,3,4; sólo log2<T produce contacto interno. Los contactos y penalizaciones de q se conservan exactamente; sólo se acota N por arriba, en la dirección necesaria para certificar negatividad regional.

### Tests explícitos, con momento exacto

Sean P_n los polinomios de Legendre y

    p_n(z)=P_n(2z−1)−[∫_0^1P_n(2u−1)cosh(Tu/2)du]/[∫_0^1cosh(Tu/2)du],
    f_k(x)=Σ_{n=1}^8 V_nk p_n(x/T), k=1,2,3, 0<x<T,
    V=(1/10000) *
      [[−8787, 2039, 1009],
       [ 3613, 8461,  −87],
       [ 3082,−4155, 3429],
       [  −35,−2573,−6207],
       [ −179,  212,−3361],
       [ −294, −504, 5728],
       [ −340,  163, 1716],
       [  −50, −214,−1281]].                                     (32)

Cada f_k tiene exactamente momento cosh nulo. F_k(t)=f_k(|t|)/sqrt2 pertenece a P_T: el segundo momento se reduce al mismo por paridad. Los tests son BV compactos, luego pertenecen al dominio logarítmico. El menor entero de las primeras tres filas de 10000V vale −319025298190≠0; junto a la independencia por grados de p_1,...,p_8, demuestra independencia de f_1,f_2,f_3.

### Evaluación sin cuadratura

`build_079_data/regional_upper.py` evalúa la polarización de (31) mediante integrales de monomios. Para I_− se divide p(z)−p(v) por z−v y se integra por triángulos. Para I_+ se usa

    ∫_0^1∫_0^1 z^u v^vexp/(z+v) dzdv
        =(A_u+A_vexp)/(u+vexp+1),
    A_0=log2, A_k=1/k−A_(k−1).

Aquí vexp denota un exponente entero, no la variable de integración. Los momentos logarítmicos son

    ∫_0^1z^(2m)log(1−z²)dz
       =[2log2−2H_(2m+2)+H_(m+1)]/(2m+1),
    ∫_0^1z^(2m+1)log(1−z²)dz=−H_(m+1)/(2m+2).

Los momentos de cosh se encierran por su serie positiva con 32 términos y cota geométrica de la cola; la corrección de momento del test se define por el cociente EXACTO, no por el punto medio de un intervalo.

`regional_seed.json` fija (32). `certify_regional.py` evalúa la matriz 3×3 de U restringida usando mpmath.iv a 70 dígitos; no usa diagonalización ni cuadratura. Los intervalos de los pivotes LDL de su opuesta están estrictamente dentro de

    (0.22998,0.23000), (0.09419,0.09421), (0.00182,0.00183).

Además comprueba por intervalos que cada margen de dominancia diagonal de esa opuesta es >1/600. La salida completa es `regional_certificate.json`. Esto da, para todo c∈C³,

    q_T(Σ_k c_k f_k)≤U(Σ_k c_k p[f_k])
                                  ≤−(1/600)Σ_k|c_k|²,             (33)

donde p[f_k](z)=f_k(Tz). La constante se refiere a las coordenadas (32), no a una normalización L². Es una prueba asistida por aritmética de intervalos del índice negativo regional ≥3; NO acredita que sea seis o siete ni calcula el índice exacto.

### Consecuencia para el diseño

Una reparación positiva de rango r<3 de q_T sobre el subespacio de momento cosh nulo no puede volverla no negativa: su núcleo intersecta no trivialmente el espacio tridimensional de (32), y (33) sigue siendo estrictamente negativa en esa intersección.                                             (34)

El alcance es esta forma regional y este portador. No excluye toda construcción con correcciones de rango dos en otros objetos. Tampoco refuta a_T≥0: los cuadrados de pegado de (28) se mantienen y pueden compensar q_T. La prueba sólo convierte parte del diagnóstico en una restricción rigurosa sobre reparaciones regionales de rango finito; falta construir la compensación aritmética suficiente.

## Reparación explícita de rango tres sobre el subespacio certificado

Estado: PROVED como reparación sobre E, mediante certificado intervalar PASS revisado y reproducido independientemente (128 modos). Dependencia computacional: mpmath.iv. Se conserva T=4/5 y E=span{f_1,f_2,f_3} de (32), con momento cosh nulo. Antecedente: (33)-(34) prueba que una reparación positiva de rango<3 no alcanza ni siquiera sobre E. La proyección de Gram es un ingrediente estándar ya contemplado en el corpus (RULES_AVOID W2); no se presenta como mecanismo nuevo de signo global. Aquí se construye y verifica una reparación concreta de este subproblema, sin invertir la forma objetivo.

En el sector par, la inmersión F(t)=f(|t|)/sqrt2 da

    a_T(F)=q_T(f)+B(f),
    B(f)=||Lf||²,
    (Lf)_n(x)=sqrt(w_n/2)[f(x)−f(l_n−x)], 0<x<l_n, n=2,3,4.

Definir g_k=Lf_k y su matriz G_ij=<g_i,g_j>. Los g_k son funciones polinómicas por tramos con coeficientes definidos exactamente en (32). Para G>0, poner

    s_k(f)=<g_k,Lf>,
    C_3(f)=s(f)*G^(-1)s(f),
    P_G=proyección ortogonal sobre span{g_1,g_2,g_3},
    W_3f=(I−P_G)Lf.                                                (35)

La convención del producto interior es conjugado-lineal en la primera entrada. También se escriben los funcionales sin operadores abstractos:

    r_k(x)=Σ_n w_n 1_(0,l_n)(x)[f_k(x)−f_k(l_n−x)], 0<x<T,
    s_k(f)=∫_0^T conjugado(r_k(x))f(x)dx.                           (36)

Se usa la extensión cero de f_k. La fórmula proviene de (I−R_l)^2=2(I−R_l) para la reflexión unitaria R_l en L²(0,l). La única inversa en (35) es la de la matriz de Gram 3×3 del pegado, no una inversa ni raíz de a_T.

Por proyección ortogonal,

    0≤C_3≤B,
    B(f)=C_3(f)+||W_3f||²,
    a_T(F)=q_T(f)+C_3(f)+||W_3f||².                               (37)

Si f∈E, entonces W_3f=0 y C_3(f)=B(f). Más aún, B−C_3 tiene apareamiento cero con E frente a cualquier test. G>0 implica que C_3 tiene rango exactamente3 porque s(Σc_kf_k)=Gc. No se reclama positividad de q_T+C_3 fuera de E.

### Certificación por un menorante, sin cuadratura

`build_079_data/compensate_regional.py` calcula G y la restricción a E del menorante

    A_128(f)=C0||f||²+Σ_{j=0}^{127}N_{a_j}(f)
             −2Σ_n w_n Re c_f(l_n)−Σ_n w_n∫_0^{l_n}|f|²+B(f).

Cada modo omitido N_{a_j}≥0, por lo que A_128≤q_T+B exactamente. No se requiere estimar una cola pequeña ni suponer una reserva para absorberla.

Los integrales exponenciales de cada modo se calculan exactamente para polinomios mediante recurrencias. Para β=aT y p en la variable z=x/T,

    h_p(z)=Σ_{r=0}^{deg p}(−1)^r p^(r)(z)/β^(r+1),
    ∫_0^z exp(−β(z−v))p(v)dv=h_p(z)−h_p(0)exp(−βz),
    I_0=(1−exp(−β))/β, I_k=(k I_(k−1)−exp(−β))/β.

Estas identidades evalúan Toeplitz, el término reflejado y todos los contactos, con los momentos exactos encerrados como en el certificado anterior. El código usa mpmath.iv a70dps y verifica LDL de ambas matrices, sin diagonalización ni cuadratura en la ejecución intervalar.

Los intervalos certificados de los pivotes de A_128 son positivos y cercanos a .00750177, .00354991, .02166562; los de G son positivos y cercanos a .38126223, .19452065, .17273963. La ejecución intervalar fue reproducida por el revisor independiente.

### Alcance y próximo residuo

El certificado demuestra que (q_T+C_3)|_E=(q_T+B)|_E>0 y repara explícitamente las tres direcciones antes certificadas negativas, con rango mínimo3 para esa tarea. No se extiende esta conclusión al complemento ni a T distintos de4/5. El nuevo residuo sobre todo el sector par es q_T+C_3; el cuadrado W_3 se anula exactamente en E. Faltan el signo de ese residuo y el control de su acoplamiento con el complemento. El diagnóstico anterior ya advierte que comprobar sólo el bloque E no basta.

La construcción de proyección es genérica y se puede repetir para falsificadores; el resultado local no acredita una separación aritmética global. Este paso realiza una compensación concreta donde antes sólo había una obstrucción de rango, no completa la prueba global.

### Resultado del certificado y diagnóstico fuera de E

La ejecución `python3 compensate_regional.py --interval --modes 128` dio PASS. Los seis pivotes intervalares de A_128 y G son estrictamente positivos; salida completa en `regional_compensation_certificate.json`. La demostración usa sólo el menorante positivo y los contactos exactos, no los autovalores flotantes del diagnóstico anterior.

NUMÉRICO, no certificado: se amplió `check_gluing.py` para evaluar la corrección C_3 y el nuevo cuadrado W_3 sobre el vector par guardado T=.8. Cuadraturas64/96 separadas en cambios de tramo dan

    B(f)≈1.40645379239075,
    C_3(f)≈1.38089100495599,
    ||W_3f||²≈0.025562787434764.

La energía guardada sigue siendo5.29432592315062e−12, no recertificada. La reparación reduce la extracción en ese test, pero el cuadrado restante sigue siendo excesivo según este diagnóstico. No se promueve la reparación local a positividad de q_T+C_3 en todo el portador. La solución del subproblema es estrictamente la compensación de E; aún faltan las otras direcciones y su acoplamiento, con precisión suficiente para el signo global.

## Positividad del complemento regional infinito

Estado: PROVED como cota regional y control del complemento infinito; prueba analítica, constante intervalar y paso a ambas paridades revisados y reproducidos independientemente. Dependencia computacional de la constante en T=4/5: mpmath.iv. Antecedentes: (27), (35)-(37), reducción finita L2 ya existente en P47. No se reclama una nueva equivalencia global ni que el bloque finito restante sea positivo. Se aporta aquí una cota inferior explícita para el complemento infinito de ESTA forma regional, en vez de inferir su signo de matrices finitas.

Trabajar con f soportada en (0,T), con N(f)<∞. No hacen falta restricciones de momentos para la siguiente cota. Definir

    I(u)=∫_u^∞H0(v)dv=atanh(exp(−u/2))+atan(exp(−u/2)),
    s_in(T)=Σ_{log n<T}Λ(n)/sqrt(n),
    s_all(T)=Σ_{log n<2T}Λ(n)/sqrt(n),
    c_T=C0+2I(T)−2s_in(T)−s_all(T),
    κ_T=1 si 0<T≤2; κ_T=exp(−T/2) si T>2.                       (38)

Para 0<u≤T, H0(u)≥κ_T/(2u). La cota exp(−T/2) resulta de 1−exp(−2u)≤2u. Para la mejora κ_T=1 cuando T≤2, poner a=u/2≤1: sinh a≤a cosh a y cosh a≤1+a dan

    H0(u)=1/(4sinh a)+1/(4cosh a)≥(1+a)/(4a cosh a)≥1/(4a).

La cota cosh a≤1+a puede verificarse mediante cosh a≤Σ(a²/2)^k=1/(1−a²/2)≤1+a para 0≤a≤1. Por otra parte I''=−H0'>0. Al separar la energía N en el cuadrado (0,T)² y su exterior, omitir sólo el núcleo reflejado interno positivo y usar convexidad en la cola, se obtiene

    N(f)≥(κ_T/4)∫_0^T∫_0^T |f(x)−f(y)|²/|x−y| dxdy
                                          +2I(T)||f||².

Los contactos internos con log n≥T son cero; los demás satisfacen |c_f(log n)|≤||f||². Cada penalización ∫_0^{log n}|f|²≤||f||². Por tanto

    q_T(f)≥(κ_T/4)∫∫ |f(x)−f(y)|²/|x−y| dxdy+c_T||f||².         (39)

### Diagonalización elemental de la comparación

Sea p_n(x)=sqrt((2n+1)/T)P_n(2x/T−1), base ortonormal de Legendre, y H_n=Σ_{k=1}^n1/k (H_0=0). En el intervalo unidad poner

    (Dp)(z)=∫_0^1[p(z)−p(v)]/|z−v|dv.

Para monomios, división de z^n−v^n e integración en v<z y v>z da

    D(z^n)=2H_n z^n−Σ_{k=0}^{n−1} z^(n−1−k)/(k+1).

Así D preserva los grados y es simétrico en polinomios. La ortogonalidad de Legendre implica D(P_n(2z−1))=2H_nP_n(2z−1). Esto demuestra el valor propio sin una identidad espectral importada.

La forma d(f)=(1/2)∫∫|f(x)−f(y)|²/|x−y| tiene apareamiento d(f,p_n)=2H_n<f,p_n>, con la convención de conjugación ajustada al argumento lineal. Para f de energía finita, la identidad se justifica por Cauchy–Schwarz en la energía y por el núcleo dividido de p_n, acotado. Restar cualquier suma finita de sus coeficientes y usar d≥0 da

    d(f)≥2Σ_{n=1}^M H_n|<p_n,f>|².

No se necesita afirmar que los polinomios sean un núcleo de forma para esta desigualdad. Al pasar M→∞ y usar Parseval, (39) implica

    f⊥span{p_0,...,p_(N−1)} ⇒
    q_T(f)≥(κ_T H_N+c_T)||f||².                                  (40)

La escala T se cancela entre la norma y la energía de comparación; no aparece un factor 1/T en (40).

### Cota explícita y alcance para ambas paridades

Para todo T fijo, H_N→∞. Por ejemplo, para cualquier γ>0 elegir

    N=ceil(exp(max(0,(γ−c_T)/κ_T)))

garantiza κ_T H_N+c_T>γ, pues H_N≥log(N+1). Es una cota conservadora y explícita, no una estimación del índice exacto.

En T=4/5, la evaluación intervalar de (38) da

    c_T≈−5.01972493487543,
    H_96+c_T≈0.127038212680009>1/8.

Así, con la constante certificada y revisada,

    f⊥p_0,...,p_95 ⇒ q_(4/5)(f)≥(1/8)||f||².                   (41)

Código `build_079_data/certify_regional_bulk.py`, salida `regional_bulk_certificate.json`; sólo verifica constantes, mientras (39)-(40) son la prueba del enunciado infinito.

Para el sector par, a_T=q_T+B con B≥0. Para el impar, el mismo pegado da

    a_T(sign(t)f(|t|)/sqrt2)=q_T(f)+2Σ_j|α_j(f)|²
                          +(1/2)Σ_n w_n∫_0^{l_n}|f(x)+f(l_n−x)|²dx.

Por ello (40)-(41) también acotan ambas formas completas en sus respectivos subespacios altos, al imponer además el momento cosh (par) o sinh (impar). Esto NO afirma el signo de sus bloques bajos.

Para mantener exactamente cada momento, sea Q_h la proyección ortogonal a h=cosh(x/2) o h=sinh(x/2), y E_low=span{Q_h p_0,...,Q_h p_95} dentro de h^⊥. Tiene dimensión96: h no es un polinomio y la proyección no anula ninguna combinación polinómica no nula. Su complemento en h^⊥ es ortogonal a los 96 polinomios, de modo que satisface (41). De aquí queda un bloque bajo de dimensión96 por paridad, con complemento infinito coercivo.                                      (42)

Permanecen los términos mixtos entre ese bloque y su complemento. Una prueba de positividad del bloque bajo aislado no basta; tampoco (42) produce una fórmula aritmética para su complemento de Schur. La estimación usa sólo cotas absolutas de los contactos y vale con constantes adaptadas para falsificadores. Su contribución es controlar rigurosamente el sector infinito, no resolver ni reemplazar la obligación global de signo.

Corolario de índice regional: en T=4/5, (33) y (41) dan 3≤n_−(q_T|cosh^⊥)≤96. La cota superior se obtiene por dimensión: un subespacio negativo de dimensión97 intersectaría el complemento coercivo, contradicción. No se identifica el índice exacto ni se convierte el diagnóstico6/7 en teorema.

## Corrección calculable del acoplamiento y residuo a posteriori

Estado: PROVED como identidad y criterio suficiente, revisados independientemente; no se ha evaluado ni certificado la matriz final. Antecedentes explícitos: fórmulas de Feshbach/capa de fase77 y 114_d_207_SCALAR_GAP_SPLIT_INVARIANCE_AND_GREEN_PIVOT, que impide obtener signo simplemente dividiendo una brecha escalar. No se reclama novedad de Schur ni de la identidad residual. El desarrollo aquí especifica un operador finito de corrección dentro del complemento coercivo de (42); usa su matriz de forma, no sólo la constante escalar. La cota escalar se aplica únicamente al residuo que quede tras esa resolución.

Fijar T=4/5 y una paridad. En el Hilbert primitivo h^⊥ de (42), A es el operador de la forma completa de esa paridad. Sean E:C^96→E_low el mapa de columnas e_i=Q_h p_i (i=0,...,95), Π_H la proyección al complemento alto, y

    P=E*AE, C=Π_H AE,
    H=compresión de A al complemento alto, H≥γI, γ=1/8.

La base e_i no se supone ortonormal: P es la matriz de la forma en esas coordenadas, no una matriz de autovalores en norma euclídea. Los e_i son polinomios más múltiplos de h, con extensión compacta suave a trozos. Su transformada es O(1/|τ|); el símbolo arquimediano crece logarítmicamente y los contactos son acotados. Por tanto e_i pertenecen al dominio de operador y C tiene columnas en L². La compresión primitiva no invalida esta conclusión porque los representantes de momento tienen la misma regularidad.

### Un corrector finito con fórmula propia

Para cualquier entero M>96, poner N=96 y

    w_k=p_k−[<h,p_k>/<h,p_N>]p_N, k=N+1,...,M,
    W:C^(M−N)→L²(0,T), columnas w_k.

Los w_k están en el complemento alto y son independientes. El denominador no es cero: por Rodrigues e integración por partes, <h,p_n> es una constante positiva por ∫_0^T h^(n)(x)x^n(T−x)^n dx; las derivadas de cosh(x/2) y sinh(x/2) son estrictamente positivas en (0,T). Esto también especifica exactamente los momentos de los tests altos. No se sustituye un momento pequeño por cero.

Definir las matrices y el operador

    K=W*HW, D=W*C,
    Z=WK^(-1)D, R=C−HZ,
    S_Z=P−D*K^(-1)D.                                             (43)

K≥γW*W>0, así que la inversa finita está justificada sin suponer el signo de A. Los w_k están en el dominio de operador por el mismo argumento que los e_i. H es la compresión autoadjunta definida por la forma; sobre estas columnas HW=Π_H AW y HZ=Π_H AZ. Por tanto R tiene columnas en L² del espacio alto. El operador Z toma coordenadas bajas y devuelve una corrección alta explícita mediante una matriz coerciva. Galerkin da W*R=0, pero esto por sí solo no da una cota pequeña de R.

### Identidad y cota para los términos mixtos

El complemento de Schur exacto es S=P−C*H^(-1)C. Al expandir R y usar Z*HZ=D*K^(-1)D, se obtiene

    S=S_Z−R*H^(-1)R,
    S_Z−8R*R ≤ S ≤ S_Z.                                         (44)

Para F=Ec+y, y en el dominio de forma alto, también se tiene la identidad exacta

    a_T(F)=c*S c+||H^(1/2)(y+Zc+H^(-1)Rc)||².                   (45)

Aquí a_T se lee en la inmersión de paridad correspondiente. La raíz de H es legítima por (42); no se toma una raíz de la forma objetivo sin conocer su signo. La fórmula no sugiere que H^(-1) se haya calculado: desaparece de la condición suficiente verificable

    S_Z−8R*R ≥0.                                                (46)

La matriz R*R es el Gram L² de los residuos de la ecuación alta, no un residuo de cuadratura ni una norma de coeficientes. Sustituirlo por un error flotante de solve no verifica (46). Si R=0, (43) reproduce el Schur exacto; no se afirma que algún M finito tenga R=0 ni que la sucesión de estos residuos converja en L².

### Qué está resuelto y qué no

Las fórmulas especifican qué operador corregir y cómo convertir un control riguroso de su residuo en un control de TODOS los acoplamientos altos. El factor8 está acreditado por (41), no ajustado numéricamente. No se ha calculado una matriz de (46) con signo certificado, ni se supone que la brecha1/8 baste para hacerlo. El cálculo exige P,K,D y los productos L² de R con precisión suficiente; no basta el bloque bajo aislado ni aumentar M sin controlar ese residuo.

Esta es una aplicación del método residual conocido al complemento concreto construido aquí, no una nueva prueba de signo ni una solución global. Una certificación en T=4/5 tampoco sustituiría una construcción válida para todo T. La obligación aritmética global permanece abierta.

## Bases primitivas bien condicionadas para ejecutar el corrector

Estado: PROVED como arreglo de bases y coercividad, con fórmulas, implementación intervalar y constantes revisadas y reproducidas independientemente. Dependencia computacional: mpmath.iv. Antecedente concreto: (42)-(43). Aunque aquellas bases son exactas, la base baja Q_h p_0,...,Q_h p_95 casi pierde una dimensión, y la alta divide por el momento minúsculo <h,p_96>. Se reemplazan ambas para evitar esos problemas, sin redondear momentos a cero. No se reclama una nueva fuente de signo; se hace ejecutable con bases bien condicionadas el corrector ya definido.

Poner N=95, α_n=<p_n,h> (reales positivos),

    h_low=Σ_{n=0}^N α_n p_n, h_tail=h−h_low,
    ε=||h_tail||²/||h||²,
    e_n=p_n−(α_n/α_0)p_0, n=1,...,N.                              (47)

La base baja tiene ahora dimensión95, pertenece a h^⊥ y consiste sólo en polinomios. Su Gram es I+ββ*, β_n=α_n/α_0; por tanto su número de condición espectral es a lo sumo ||h||²/α_0².

En contraste, el Gram de la base anterior Q_h p_0,...,Q_h p_95 es I−aa*/||h||², a=(α_0,...,α_95), con autovalor mínimo ε y número de condición1/ε. La cota que sigue muestra que esa representación exigía conservar una diferencia de más de374 órdenes decimales, aunque el espacio geométrico estuviese bien definido.

### Coercividad del nuevo complemento

Si f∈h^⊥ es ortogonal a los e_n de (47), sus coeficientes bajos son proporcionales a los de h: f_low=t h_low. El momento da t||h_low||²=−<h_tail,f_tail>, y por Cauchy–Schwarz,

    ||f_low||²≤[ε/(1−ε)]||f_tail||²,
    ||f_tail||²≥(1−ε)||f||².

Aplicando (39) y Bessel a los coeficientes de grados≥96,

    q_T(f)≥[κ_T H_96(1−ε)+c_T]||f||².                            (48)

Para T=4/5 se encierra ε por el resto de Taylor de h de grado95:

    ε≤δ_h:=T exp(T)(T/2)^192/[(96!)²||h||²],
    ||cosh(x/2)||²=(sinh T+T)/2,
    ||sinh(x/2)||²=(sinh T−T)/2.                                 (49)

La proyección ortogonal sobre polinomios aproxima al menos tan bien como ese Taylor. La cota uniforme del resto es exp(T/2)(T/2)^96/96!, válida para ambas h; integrar su cuadrado prueba (49).

El certificado verifica δ_h<10^(−374) para ambas paridades y

    H_96(1−δ_h)+c_T>1/8.

Así el nuevo complemento sigue siendo coercivo con1/8. Los dos momentos se imponen exactamente por paridad, no por una tolerancia. La cota del índice regional dentro de cosh^⊥ mejora a3≤n_−≤95; no se afirma índice exacto.

### Base alta sin denominadores pequeños

Definir para k≥96

    w_k=p_k−[α_k/||h_low||²]h_low.                               (50)

Cada w_k está en h^⊥ y es ortogonal a los e_n. Son independientes por sus coeficientes en p_k. Para cualquier colección finita su Gram es

    G_high=I+vv*/||h_low||², v=(α_k),
    cond(G_high)≤1/(1−ε).

No se divide por α_96. En L², todo el complemento nuevo se parametriza así: elegir f_tail arbitraria y corregir su momento con −<h_tail,f_tail>h_low/||h_low||². Esto no afirma por sí solo convergencia en norma de grafo de un algoritmo de Galerkin.

Los momentos se calculan sin restar integrales casi iguales. Rodrigues y la integral beta dan la serie positiva

    α_n=sqrt(T(2n+1))(T/2)^n
        ×Σ_{r≥0, r≡n+σ (mod2)} (T/2)^r (n+r)!/[r!(2n+r+1)!],    (51)

con σ=0 para h=cosh y σ=1 para h=sinh. El cociente entre términos sucesivos de esa paridad es ≤(T/2)²/[(r+1)(r+2)], lo que permite encerrar la cola después de cualquier número prefijado de términos.

`build_079_data/regional_bases.py` implementa (47),(50),(51) en coordenadas de Legendre y devuelve intervalos para sus coeficientes. La certificación usa32 términos positivos por momento, no cuadratura. Verifica mediante intervalos que el Gram bajo tiene condición<27/20 y que el exceso de la cota de condición alta sobre1 es<10^(−370), además de mantener la coercividad1/8. Los chequeos explícitos de ortogonalidad en el script comprueban las95 columnas bajas y cuatro altas; el resultado para toda la familia se prueba algebraicamente arriba, no se infiere de esa muestra.

Las fórmulas (43)-(46) se usan ahora con E:C^95→span{e_1,...,e_95} y W de columnas w_96,...,w_M. El factor8 sigue válido. Esto resuelve el acondicionamiento de los Grams y la imposición de momentos; no evalúa P,K,D ni R*R, no garantiza el acondicionamiento del bloque de signo y no demuestra (46). En particular, no justifica convertir polinomios de grado alto a monomios en precisión ordinaria ni descartar el acoplamiento pendiente.

## Evaluación del bloque y del corrector tras extraer las singularidades

Estado: fórmulas revisadas; evaluación NUMÉRICA, sin cotas intervalares de las matrices ni del residuo funcional. Antecedentes: (43)-(51) y el error de cuadratura detectado en check_regional.py. Se implementa evaluate_blocks.py en coordenadas de Legendre, evitando la cuadratura directa de las singularidades y la conversión de polinomios de grado alto a monomios.

Escribir

    H0(u)=1/(2u)+r(u),
    I(u)=(1/2)log(4/u)+π/4+s(u),
    s(u)=(1/2)log[(u/4)/tanh(u/4)]−atan(tanh(u/4)).                (52)

r es regular en0, con r(0)=1/4; se evalúa por serie cerca de0 para evitar cancelación numérica. El término directo singular aporta la diagonal H_n ya probada. En la cola se extrae exactamente la matriz de log(1−z), con φ_n(z)=sqrt(2n+1)P_n(2z−1):

    L_nn=2H_n−2H_(2n+1)+1/(2n+1),
    L_nm=−sqrt((2n+1)(2m+1))/(|n−m|(n+m+1)), n≠m.              (53)

Una verificación algebraica de (53) usa la recurrencia de multiplicación por2z−1 y la simetría de la integral: la fila0 es ∫P_m(2z−1)log(1−z)=−1/[m(m+1)] para m≥1, por Rodrigues, y vale−1 para m=0. La recurrencia determina las filas restantes; las fórmulas mostradas la satisfacen. Como control adicional de implementación se comparó exactamente por fracciones con integración de polinomios de grados0..4.

El resto de la energía interna se integra en el triángulo x=Tu,y=Tuv, sin |x−y| ni denominadores singulares en los pesos finales. El peso directo regular es Tu r(Tu(1−v)), aplicado a diferencias de φ. El reflejado es1/[2(1+v)]+Tu r(Tu(1+v)), aplicado a diferencias en paridad par y a sumas en paridad impar. La cola suave restante es

    −(1/2)log(1+z)+s(T(1−z))+s(T(1+z)),

y la constante diagonal conjunta es−γ−log(2πT). Los contactos internos llevan−w(C+C*), y la reflexión entre semirrectas−wR para pares,+wR para impares. La revisión independiente confirmó estos factores y la inmersión normalizada.

### Matrices calculadas

En T=.8 se usaron grados0..111:95 columnas bajas de (47) y16 altas de (50). Se calculan P,K,D y la matriz de coeficientes Z_coeff=K^(-1)D; el operador físico es W Z_coeff. El resultado finito S_Z=P−D*Z_coeff se evaluó en órdenes Gauss128 y160.

| Paridad | Orden | Mínimo de P | Mínimo de S_Z | Mínimo de K |
|---|---|---|---|---|
| par |128|5.32560e−12|5.31894e−12|3.25285|
| par |160|5.32231e−12|5.31490e−12|3.25285|
| impar |128|1.130410e−9|1.129509e−9|3.28857|
| impar |160|1.130400e−9|1.129498e−9|3.28857|

Estos son autovalores de matrices en coordenadas de las bases, NO autovalores normalizados por sus Grams ni cotas certificadas de λ_A. La concordancia entre cuadraturas es un diagnóstico. No encierra los errores de la serie de r, cuadratura, aritmética flotante o conversión de momentos a float.

Las matrices y bases de orden160 quedan preservadas en blocks_even_160.npz y blocks_odd_160.npz, junto a blocks_diagnostic.json. En esos archivos la clave Z contiene Z_coeff; W@Z da sus coeficientes en la base Legendre original. El código restringe explícitamente T a.8 porque su lista de contactos es2,3,4.

El S_Z exacto es una cota superior del Schur, pero la matriz flotante no constituye una cota superior certificada. Los residuos de solve fueron <7e−16: sólo verifican la ecuación matricial K Z_coeff≈D y NO el residuo R=C−HZ en L² del complemento infinito. No se han calculado R*R ni una cota inferior certificada S_Z−8R*R. Por tanto, los mínimos positivos de la tabla no prueban (46), ni el signo completo en esta ventana ni para todoT.

## Evaluación del residuo como función

Estado: fórmula del operador y proyección revisadas; resultados NUMÉRICOS sin encerramiento. `build_079_data/evaluate_residual.py` evalúa la acción del operador completo sobre las columnas polinómicas corregidas U=E−WZ_coeff, y luego proyecta al espacio alto. No identifica el residuo de solve con R.

Además de la extracción (52), el término reflejado singular se calcula mediante

    ∫_0^T p_n(y)/(x+y)dy
       =2(−1)^n sqrt((2n+1)/T) Q_n(1+2x/T),                     (54)

donde Q_n(s)=(1/2)∫_(−1)^1P_n(t)/(s−t)dt, s>1. Cambio de variable y paridad prueban (54). Se usa scipy.special.lqmn para la evaluación numérica. El directo singular aporta H_n p_n; los términos regulares se integran separando y<x e y>x. Para σ=+1 par,−1 impar, el operador de contactos es

    −Σ_n w_n[f(x+l_n)+f(x−l_n)+σf(l_n−x)],

con extensión cero. Las fórmulas reflejadas cambian de diferencia a suma en el sector impar, como en (25).

Si A_0 denota el operador de paridad sin compresión de momento, la proyección exacta es

    R= A_0 U−h <h,A_0U>/||h||²
                  −E(E*E)^(-1)E*A_0U.                           (55)

Es válida porque E⊥h y el complemento alto es ortogonal a ambos. El script aproxima el momento de la primera resta mediante la expansión finita de h hasta el grado de U; esa cola no se declara encerrada. El producto E*A_0U se obtiene de las matrices evaluadas anteriormente. Los residuos se evalúan punto a punto antes de formar su Gram, para evitar restar dos Grams grandes casi iguales.

La cuadratura exterior se parte en todos los cambios de contacto:0,T−log2,log3−T,log4−T,log2,T. Incluye aún singularidades logarítmicas cuadradas en los extremos, por lo que su error debe certificarse o eliminarse antes de cualquier conclusión de signo.

### Diagnóstico del corrector con16 modos altos

Con matrices de orden160 y grado111, la cuadratura interior del operador usa160 nodos. Resultados:

| Paridad | Orden exterior | Norma aproximada R*R | Mínimo aproximado de S_Z−8R*R | Error de ortogonalidad bajo muestreada |
|---|---|---|---|---|
| par |128|0.94378|−1.56429|0.02275|
| par |256|0.98984|−1.56877|0.00558|
| impar |128|0.94248|−1.55377|0.04954|
| impar |256|1.06575|−1.56246|0.01227|

Los errores de ortogonalidad son integrales numéricas del residuo frente a E, no errores del solve; su variación evidencia el coste de los extremos logarítmicos. Los mínimos negativos de orden uno son un diagnóstico desfavorable del criterio suficiente para este corrector, no una refutación de a_T≥0 ni un certificado intervalar de fallo. La norma del Gram todavía varía perceptiblemente con la cuadratura.

Sobre el autovector coordenado inferior de S_Z, la penalización8v*R*Rv es aproximadamente8.15e−13 en paridad par y1.21e−10 en impar, por debajo de los respectivos valores positivos de S_Z. Esto tampoco prueba signo: los acoplamientos con otras direcciones permanecen, y la matriz completa del criterio tiene el diagnóstico negativo mostrado.

Los datos basales se conservan en residual_diagnostic.json. Las ejecuciones posteriores parametrizan el orden de las matrices guardadas y usan nombres separados para no confundir correctores de distinta dimensión. No se interpreta ningún error flotante como cota de R*R.

Se amplió el corrector a64 modos altos (grado159, matrices en orden192). Con cuadratura exterior128, los mínimos del criterio escalar S_Z−8R*R fueron aproximadamente−1.14604 y−1.14524 (par/impar), todavía desfavorables. Estos datos están en residual_diagnostic_192.json. Aumentar el tamaño no elimina por sí solo el coste de aplicar la brecha mínima a todo el residuo.

## Mejora modal del control residual

Estado: PROVED como desigualdad auxiliar; argumento y constantes intervalares revisados y reproducidos independientemente. No es un certificado del signo de las matrices calculadas. El cambio respecto de (44) consiste en conservar la comparación modal completa de (39), en vez de reemplazarla por su mínimo1/8. Por eso no es un mero reparto de la brecha escalar excluido en114_d_207: usa información adicional del operador y la ortogonalidad del residuo a los modos resueltos.

Trabajar en T=4/5 con las bases nuevas (47),(50). Sea W_∞:ℓ²({96,97,...})→H_high la parametrización exacta por coeficientes de la cola. Con η=||h_tail||²/||h_low||², (49) acredita η≤ηbar=10^(−370). Se tiene

    ||W_∞||²=1+η≤1+ηbar,
    a_T(W_∞z)≥q_T(W_∞z)≥Σ_{k≥96}d_k|z_k|²,
    d_k=H_k+c_T−|c_T|ηbar.                                      (56)

En efecto, en (39) se conserva la energía de todos los coeficientes altos, se omite únicamente la energía baja no negativa y se acota el término c_T||f_low||² por−|c_T|ηbar||z||². Aquí c_T<0 y d_96>1/8. No se afirma que H≥d_(M+1)I en todo el espacio alto.

Para cualquier fuente r∈H_high, la caracterización variacional del inverso da

    <r,H^(-1)r>
      =sup_y[2 Re<r,y>−a_T(y)]
      ≤Σ_{k≥96}|(W_∞*r)_k|²/d_k.                               (57)

La desigualdad se obtiene aplicando (56) en todo el dominio alto y luego ampliando el supremo al espacio de coeficientes con energía diagonal finita. No requiere una afirmación adicional de núcleo de forma para las aproximaciones de Galerkin.

Para un corrector arbitrario Z=W_M X, donde W_M contiene w_96,...,w_M, definir

    Δ=D−KX=W_M*R,
    R=C−HZ,
    S_X=P−D*X−X*D+X*KX.

Separar en (57) los índices96..M de los posteriores, usar crecimiento de d_k y ||W_∞*r||²≤(1+ηbar)||r||², y polarizar, produce

    R*H^(-1)R ≤[(1+ηbar)/d_(M+1)]R*R
                 +(1/d_96−1/d_(M+1))Δ*Δ,
    S_exact=S_X−R*H^(-1)R.                                     (58)

En Galerkin exacto Δ=0. La fórmula general incluye el defecto del sistema, de modo que un X calculado no tiene que tratarse como una inversa exacta. Todos los productos son en las coordenadas bajas; la base alta no ortonormal ya está contabilizada por ||W_∞||².

`build_079_data/certify_residual_weights.py` encierra las constantes con mpmath.iv y acredita

    M=111: (1+ηbar)/d_112<1783/500=3.566,
    M=159: (1+ηbar)/d_160<1573/1000=1.573,
    0≤1/d_96−1/d_(M+1)<8.

Por tanto una condición suficiente rigurosa, para cada uno de esos tamaños, es

    S_X−ρ_M R*R−8Δ*Δ≥0,                                       (59)

con los respectivos ρ_M racionales. El archivo residual_weights_certificate.json certifica las constantes de esta desigualdad, NO sus matrices.

### Aplicación diagnóstica de la mejora

`check_weighted_residual.py` aplica los pesos certificados a las matrices y Grams todavía flotantes. Resultados aproximados:

| Modos altos | Paridad | Mínimo del diagnóstico de (59) |
|---|---|---|
|16 (M111), exterior256|par|4.80e−12|
|16 (M111), exterior256|impar|1.057e−9|
|64 (M159), exterior128|par|5.19e−12|
|64 (M159), exterior128|impar|1.111e−9|

En los cuatro diagnósticos todos los autovalores calculados fueron positivos. Esto muestra que la mejora modal cambia la viabilidad NUMÉRICA de la condición suficiente; no verifica aún (59). Los Grams del residuo conservan errores de extremos logarítmicos, proyección truncada y aritmética flotante. La salida weighted_residual_diagnostic.json declara expresamente NUMERICAL_ONLY.

La obligación siguiente queda definida: encerrar P,K,D, la acción corregida y R*R con error suficientemente pequeño para probar (59), o modificar de nuevo el corrector si un encerramiento fiable falla. No se sustituye esa tarea por estabilidad numérica ni se extrapola T=.8 a todas las ventanas. El objetivo global permanece abierto.

## Aproximación racional con cancelación exacta de la cola

Estado: PROVED como control auxiliar del error de operador; argumento, signos y traslado revisados independientemente, certificado racional reproducido con resultado PASS. No certifica aún (59). Antecedente inmediato: (52)-(55) extraen la singularidad, pero evalúan el resto sin encerramiento. Este paso completa esa obligación concreta: conserva conjuntamente núcleo y cola y entrega una cota en norma de operador, válida para todas las funciones del dominio, no sólo los polinomios ensayados. No se reclama una nueva fuente de signo ni prioridad sobre la aproximación de Taylor.

En T=4/5 poner r(u)=H0(u)−1/(2u) y s(u)=−∫_0^u r(v)dv. Esta normalización coincide con (52): s(0)=0. La función r es holomorfa en |u|<π, incluida su singularidad removible en cero. En |z|=2, escribir w=z/2=x+iy. Como |w|=1,

    |sinh w|²=sinh²x+sin²y≥(5/6)²(x²+y²),
    |cosh w|²=sinh²x+cos²y≥1/4.

Se usaron |sinh x|≥|x|, |sin y|≥(5/6)|y| y cos y≥1/2 para |y|≤1; las dos últimas siguen de los desarrollos alternados elementales. Por H0(z)=1/(4sinh(z/2))+1/(4cosh(z/2)) se obtiene |r(z)|≤3/10+1/2+1/4=21/20. Cauchy da, para r_K(u)=Σ_{k=0}^K c_k u^k,

    |c_k|≤(21/20)2^(−k),
    sup_[0,8/5]|r−r_K|≤δ_K=(21/4)(4/5)^(K+1),
    s_K(u)=−Σ_{k=0}^K c_k u^(k+1)/(k+1).                     (60)

Todos los c_k son racionales. Una recurrencia exacta, sin evaluar números trascendentes, es

    b_j=(−1)^j 2^(j+1)/(j+1)!,
    c_k=[(−1/2)^(k+1)/(k+1)!−b_(k+1)/2
                  −Σ_{j=1}^k b_j c_(k−j)]/2.                 (61)

Procede de B(u)r(u)=[exp(−u/2)−B(u)/2]/u, con B(u)=(1−exp(−2u))/u. Los primeros coeficientes son 1/4,−1/48,−1/32,7/11520.

Definir A_K por la misma acción de (54), conservando los términos singulares, los logaritmos y los contactos, y reemplazando conjuntamente r,s por r_K,s_K. Sea e=r−r_K, J(u)=∫_0^u e(v)dv y σ=+1 para paridad par, −1 para impar. Las filas diagonales del error directo y reflejado suman

    J(x)+J(T−x)+J(T+x)−J(x)=J(T−x)+J(T+x).

El error de la cola es exactamente el opuesto. Por tanto, en el espacio L²(0,T) antes de imponer el momento,

    ((A−A_K)f)(x)=−∫_0^T[e(|x−y|)+σe(x+y)]f(y)dy,
    ||A−A_K||≤2Tδ_K=ξ_K=(42/5)(4/5)^(K+1).                   (62)

La cota resulta del test de Schur, pues filas y columnas absolutas son ≤2Tδ_K. La diferencia se extiende a un operador acotado autoadjunto; A_K puede definirse como A menos ese operador en el mismo dominio. Las compresiones ortogonales no aumentan la cota. Aproximar s de forma independiente perdería esta cancelación.

### Traslado al criterio finito sin invertir otra matriz

Congelar un mismo X, sin exigir que sea solución exacta de ningún sistema, y poner U=E−WX, G_U=U*U. Los símbolos A,A_K en las siguientes expresiones pueden interpretarse como los operadores completos antes de compresión; las columnas de U son primitivas. Definir

    S_X,K=U*A_K U,
    R_K=Π_high A_K U,
    Δ_K=W*A_K U,
    Γ_K=R_K*R_K.

Las bases E,W y las proyecciones son las exactas de (47)-(51), no sus aproximaciones flotantes. Entonces (62) implica

    S_X≥S_X,K−ξ_K G_U,
    (R−R_K)*(R−R_K)≤ξ_K²G_U,
    (Δ−Δ_K)*(Δ−Δ_K)≤ξ_K²||W||²G_U.

Aplicando Young con cualquier θ>0 y usando ||W||²≤1+ηbar, (59) queda garantizada si

    S_X,K−ρ_M(1+θ)Γ_K−8(1+θ)Δ_K*Δ_K−β_K G_U≥0,
    β_K=ξ_K+(1+1/θ)ξ_K²[ρ_M+8(1+ηbar)].                      (63)

Es una condición suficiente; no se afirma que su matriz sea positiva. El script certify_kernel_polynomial.py construye los385 coeficientes racionales con K=384 y verifica con fracciones exactas ξ_K<10^(−35). Con θ=10^(−20), ηbar=10^(−370) y el mayor peso ρ=1783/500 verifica además β_K<10^(−35), válido por tanto para ambos tamaños de (59). El archivo kernel_polynomial_certificate.json conserva coeficientes, cota racional exacta y alcance del certificado.

La incertidumbre del núcleo regular queda así controlada uniformemente, incluidos todos los modos no calculados. Quedan pendientes las integrales y la aritmética de S_X,K, Γ_K, Δ_K y G_U, con momentos exactos. Sus integrandos contienen ahora polinomios, logaritmos y las funciones de corrección de momentos; no se considera que sean racionales ni que estén certificados automáticamente. En particular, el error de cuadratura exterior y de proyección de (55) no queda resuelto por (62). El signo global continúa OPEN.

## Fuente polinómica con singularidades explícitas

Estado: PROVED como identidad auxiliar, revisada independientemente. Completa la preparación analítica de (63), no su desigualdad matricial. Antecedente (54)-(55): evaluación de Q_n y cuadratura de logaritmos cuadrados sin error certificado. Cambio: expresar la fuente antes de proyección mediante polinomios y tres logaritmos, preservando exactamente sus singularidades. No se presenta como nuevo mecanismo aritmético de signo.

Sea f un polinomio, z=x/T, σ=±1, y definir

    D_T f(x)=∫_0^T(f(x)−f(y))/|x−y|dy,
    Q_f(x)=∫_0^T[f(y)−f(−x)]/(x+y)dy,
    C_T=−γ−log(2πT).

Aquí f(−x) significa continuación del polinomio, NO extensión cero. La división en Q_f es exacta: para f(y)=y^m,

    Q_f(x)=Σ_{j=0}^{m−1}(−x)^j T^(m−j)/(m−j).

El operador D_T también preserva polinomios; para m≥0,

    D_T x^m=2H_m x^m−Σ_{j=0}^{m−1}T^(j+1)x^(m−1−j)/(j+1).

Con C_prime la acción de contactos (positiva en la notación A=Arch−C_prime), la fuente del operador aproximante (62) es exactamente

    A_K f(x)=.5D_T f(x)+C_T f(x)−.5σQ_f(x)
       +.5[σf(−x)−f(x)]log z
       −.5f(x)log(1−z)−.5σf(−x)log(1+z)
       −∫_0^T[r_K(|x−y|)+σr_K(x+y)]f(y)dy
       −C_prime f(x).                                         (64)

Para probarlo, dividir f(y)=f(−x)+(x+y)q(x,y) en la integral reflejada singular. Su parte constante produce f(−x)log((1+z)/z). La fila diagonal reflejada, combinada con −.5f log(1−z²), produce −.5f[log z+log(1−z)]. Las filas regulares cancelan exactamente la cola s_K como en (62). Esto da (64), incluidos todos los signos. Los contactos conservan la extensión cero y son polinómicos en cada intervalo delimitado por sus cambios de soporte. La integral regular es un polinomio, separando y<x de y>x. La identidad vale casi en todas partes; todos sus términos están en L².

La proyección primitiva/alta se aplica DESPUÉS de (64); añade la función h de (55). No se reemplaza esa función por un polinomio sin cota de error.

### Momentos exactos para los extremos

En un intervalo afín x=a+(b−a)t, las singularidades presentes en sus extremos se conservan como log t y log(1−t). Para n≥0, k=n+1, H_k=Σ_{j=1}^k1/j y H_k^(2)=Σ_{j=1}^k1/j²,

    ∫_0^1 t^n dt=1/k,
    ∫_0^1 t^n log t dt=−1/k²,
    ∫_0^1 t^n log(1−t)dt=−H_k/k,
    ∫_0^1 t^n log²t dt=2/k³,
    ∫_0^1 t^n log²(1−t)dt=[H_k²+H_k^(2)]/k,
    ∫_0^1 t^n log t log(1−t)dt
        =H_k/k²+H_k^(2)/k−π²/(6k).                            (65)

Las primeras fórmulas siguen por integración o diferenciación de ∫t^n; las restantes se obtienen diferenciando la integral beta en sus dos exponentes en (k,1), con las identidades finitas de los números armónicos. Las derivadas bajo el integral están justificadas por integrabilidad de logaritmos cuadrados en vecindarios de esos exponentes. Por tanto el Gram de funciones p(t)+q(t)log t+r(t)log(1−t), con coeficientes racionales, se calcula exactamente en Q+π²Q, sin cuadratura exterior. El módulo log_polynomial_moments.py implementa esos seis momentos y la contracción de coeficientes; comprueba, entre otras identidades, ||log t−log(1−t)||²=π²/3.

Los otros logaritmos de (64) son suaves en cada pieza donde no se conservaron como singularidad. Para u∈[a,b] con a>0, c=(a+b)/2, v=(u−c)/c y q=(b−a)/(b+a)<1,

    log u=log c+Σ_{j=1}^L(−1)^(j+1)v^j/j+E_L(u),
    |E_L(u)|≤q^(L+1)/[(L+1)(1−q)].                            (66)

Esto sigue de la serie geométrica integrada. El extremo u=0 nunca se trata con (66): se retiene exactamente por (65). Los puntos de contacto no son racionales y deben encerrarse; tampoco log c es racional. La implementación de (65) es el núcleo algebraico, no un encerramiento automático de esos coeficientes.

Con (64)-(66) queda definida una vía de integración sin singularidades ocultas: conservar los logaritmos de extremo, aproximar sólo los factores suaves con resto explícito y evaluar sus productos por (65). Sigue pendiente ejecutar el ensamblado intervalar completo de (63), incluida la proyección h. No se interpreta la disponibilidad de fórmulas como un certificado de la matriz ni de su signo.

## Sustitución controlada de la proyección hiperbólica

Estado: PROVED como comparación de proyectores, revisada independientemente. Antecedente (55): el evaluador aproximaba el momento de la fuente mediante una expansión truncada de h sin encerrar el error. Ahora se comparan los proyectores completos usando la cota de cola ya probada en (49); no se modifica la base primitiva ni se declara nulo ningún momento pequeño. Esto elimina una integración no polinómica pendiente en (63), sin proporcionar por sí solo el signo.

Sea V_95=span{p_0,...,p_95}, h_low=P_95h y h_tail=h−h_low. El espacio bajo E de (47) es exactamente V_95∩h_low^⊥. Los proyectores ortogonales sobre el complemento alto primitivo y sobre la cola polinómica satisfacen

    Π_high=I−P_E−P_h,
    Π_tail=I−P_95=I−P_E−P_hlow,
    ||Π_high−Π_tail||=sqrt ε<10^(−187),
    ε=||h_tail||²/||h||².                                    (67)

En efecto, ambas proyecciones coinciden fuera del plano generado por h_low,h_tail. En la base ortonormal de ese plano, P_hlow−P_h tiene matriz

    [ ε                  −sqrt(ε(1−ε)) ]
    [ −sqrt(ε(1−ε))      −ε             ],

cuyo cuadrado es εI. Si la cola fuese cero, los proyectores coincidirían. La cota ε<10^(−374) procede de (49) para ambas paridades.

Para la fuente V=A_KU y sus Grams definir

    G_V=V*V,
    B_n=<p_n,V>,
    Γ_tail=G_V−Σ_{n=0}^{95}B_n*B_n.

Entonces Γ_K=V*Π_high V y

    −δG_V≤Γ_K−Γ_tail≤δG_V,  δ=10^(−187).                     (68)

Es una desigualdad de matrices en coordenadas bajas; δ NO es una cota absoluta de error de cada entrada ni de la norma del Gram sin contabilizar G_V. La sustitución en (63) produce el siguiente criterio suficiente, con K=384, θ=10^(−20) y cualquiera de los dos pesos ρ_M certificados:

    S_X,K−ρ_M(1+θ)Γ_tail−8(1+θ)Δ_K*Δ_K
            −10^(−35)G_U−4·10^(−187)G_V ≥0.                  (69)

Se usaron β_K<10^(−35) y ρ_M(1+θ)<4. Todas las matrices de (69) se definen con las bases exactas E,W; sus coeficientes de momentos se encierran por (51). No aparece ninguna integral de h contra la fuente: G_V, B_n, S_X,K y Δ_K requieren sólo integrales de las fuentes de (64) contra sí mismas o contra polinomios. Los coeficientes hiperbólicos de las bases no desaparecen, pero ya cuentan con una serie positiva y cota de cola.

certify_projection_transfer.py reproduce con mpmath.iv70 la cota de Taylor

    ||h_tail||²≤T exp(T)(T/2)^192/(96!)²

y encierra la norma de diferencia de proyectores por 9.20e−189 (par) y 4.03e−188 (impar), ambas menores que δ. Guarda projection_transfer_certificate.json. El certificado acredita únicamente constantes de transferencia, no matrices ni positividad. La resta en Γ_tail sigue requiriendo precisión intervalar suficiente; no se justifica efectuarla en doble precisión ni sustituirla por estabilidad entre cuadraturas.

## Ensamblador de la fuente por momentos y contactos

Estado: identidad auxiliar PROVED y revisada; implementación revisada y comprobación numérica reproducida independientemente con PASS_IMPLEMENTATION_CHECK. Este paso implementa (64), sin introducir una nueva candidata ni un mecanismo adicional de signo. Para k,m enteros no negativos y σ=±1,

    J_(k,m)^σ(x)=∫_0^T[|x−y|^k+σ(x+y)^k]y^m dy
      =(1−(−1)^k) m!k!/(m+k+1)! x^(m+k+1)
       +Σ_{j=0}^k[(−1)^(k−j)+σ] binom(k,j)
                        T^(m+j+1)/(m+j+1) x^(k−j).            (70)

Prueba: reemplazar |x−y|^k por (y−x)^k en todo el intervalo y añadir (1−(−1)^k)(x−y)^k en y<x. La corrección integrada es el término beta de (70). Expandir los dos polinomios restantes da la suma. No hay integración numérica ni singularidad en este paso.

Para f=Σa_m x^m y r_K=Σc_k u^k, precomputar μ_j(f)=Σ_m a_m T^(m+j+1)/(m+j+1). La suma de (70) se contrae con esos momentos, más los términos beta de k impar, en O(K²+K·grado(f)) operaciones por columna. El módulo polynomial_source.py implementa esa contracción, D_T, Q_f, los tres coeficientes logarítmicos de (64) y los contactos. Funciona tanto con mpmath.mp como con mpmath.iv; sólo esta última modalidad encierra los coeficientes y redondeos.

En T=4/5 la partición completa de contactos es

    0, T−log2, log3−T, log4−T, log2, T.

El programa verifica la separación estricta de los intervalos que encierran esos puntos. En cada pieza determina los contactos activos mediante su punto medio; la lista contiene todos los cambios de soporte, por lo que la actividad es constante en el interior. Componer el polinomio con x+log n, x−log n o log n−x implementa cada término activo. Los extremos, de medida cero, no afectan la fuente L². Si la precisión no permite decidir orden o actividad, el ensamblado falla explícitamente.

check_polynomial_source.py compara el ensamblado contra la acción original, integrando por separado incrementos directos, reflejados y cola, para un polinomio de grado4 y r_K de grado8. Recorre ambas paridades y las cinco piezas, con referencia numérica a100dps y coeficientes intervalares a60dps. Esta comprobación es un diagnóstico independiente de implementación, no una prueba mediante cuadratura ni un certificado de signo. El grado8 sirve para probar las operaciones; NO sustituye el grado384 de (69).

El ensamblador conserva las variables físicas x; no evalúa el Gram ni resuelve sus posibles cancelaciones. El trabajo pendiente es transformar cada pieza a (0,1), aplicar (65)-(66) con cotas de resto y ensamblar las matrices de (69) con precisión suficiente.

## Integración intervalar de productos de fuentes

Estado: control analítico e implementación revisados independientemente; ensayo de tres identidades y dos integrales escalares PASS. Las matrices completas de (69) siguen pendientes. El antecedente inmediato es el ensamblador (70): faltaba integrar sus fuentes con un resto explícito. El nuevo módulo interval_source_integrals.py conecta ambos pasos, sin sustituir ningún test de signo por acuerdo numérico.

En cada pieza x=a+d t, d=b−a>0, transformar los cuatro polinomios de (64) por composición afín. Si a=0 se conserva log(x/T)=log(d/T)+log t; si b=T se conserva log(1−x/T)=log(d/T)+log(1−t). La presencia de estos extremos se determina por la partición exacta, no por proximidad numérica. Para los demás factores log(α+βt), el centro c=α+β/2 y q=|β|/(2c)<1 permiten (66). Se exige c>0 y q<1 mediante comparación intervalar estricta.

Sea F la fuente exacta A_Kf en la pieza y Ftilde=p+q_0 log t+r_0 log(1−t) su aproximante, después de sustituir únicamente los logaritmos suaves. Para un polinomio v definir C(v)=Σ|coeficientes(v)|. Si v_j multiplica un logaritmo aproximado con resto uniforme ε_j, entonces

    ||F−Ftilde||_(L²(a,b))≤e_F=sqrt(d)Σ_j ε_j C(v_j),
    ||Ftilde||_(L²(a,b))≤n_F
       =sqrt(d)[C(p)+sqrt(2)(C(q_0)+C(r_0))].                 (71)

La primera cota usa |v_j(t)|≤C(v_j) en [0,1]; la segunda usa ||1||_2=1 y ||log t||_2=||log(1−t)||_2=sqrt2. Para dos fuentes se obtiene por Cauchy–Schwarz

    |<F,G>−<Ftilde,Gtilde>|
       ≤e_F n_G+e_G n_F+e_F e_G.                             (72)

El producto de los aproximantes se integra con (65), incluido el factor d del cambio de variable. Todas las constantes, coeficientes, extremos, logaritmos, π² y redondeos se calculan con mpmath.iv. El programa añade el intervalo simétrico del presupuesto (72). Aunque representa ese presupuesto como intervalo no negativo, multiplicarlo por [−1,1] usa su extremo superior y conserva la cota requerida.

La función source_inner exige una partición compartida del intervalo completo (0,T). Los extremos coincidentes deben representar los mismos puntos exactos, como los construidos por polynomial_source.pieces; la igualdad de intervalos no autoriza identificar dos parámetros exactos desconocidos distintos. El módulo no usa aproximación decimal de los puntos de contacto para elegir el dominio de integración.

La certificación resultante corresponde a A_K y a los coeficientes exactos encerrados por sus intervalos. El error A−A_K continúa cubierto separadamente por (69). Tampoco convierte una entrada encerrada en positividad de la matriz: hace falta ensamblar todas las entradas relevantes y verificar un criterio matricial riguroso.

check_interval_source_integrals.py comprueba tres integrales con valor conocido (log²t, logt·log(1−t), log²(1+t)) y dos normas de fuente A_8f de grado4, una por paridad. En las normas, el encerramiento procede de (71)-(72) y aritmética intervalar; la referencia por cuadratura130dps es sólo una comprobación independiente de implementación. No se ejecuta en este ensayo el Gram95×95 ni se sustituye K384 por K8 en el criterio final.

Resultado del ensayo: los intervalos de las normas cuadradas tienen anchuras menores que 1.946e−39 (par) y 2.154e−38 (impar), con valores aproximadamente1.77351234335 y0.102218493217. Los intervalos y referencias se conservan en interval_source_integrals_check.json. Son integrales de las fuentes de prueba A_8f, no energías del vector del fondo ni entradas certificadas del Gram completo de (69).

## Contracción conjunta de columnas

Estado: reorganización algebraica y código revisados independientemente; ensayos de Grams conocidos PASS. No es un certificado de la matriz de (69). Antecedente (71)-(72): integración pareja por pareja que repetía preparaciones. El módulo interval_source_gram.py prepara cada columna una vez por pieza y comparte las expansiones suaves, sus restos y los momentos intervalares a precisión fija.

Con componentes locales φ_(s,k)(t)=t^k L_s(t), L_0=1, L_1=log t, L_2=log(1−t), y coeficientes C_(s,k),i de cada fuente aproximada, definir

    M_(s,k),(r,l)=∫_0^1 t^(k+l)L_s(t)L_r(t)dt,
    Gtilde=d C^t M C,
    E_ij=e_i n_j+n_i e_j+e_i e_j.                             (73)

Los seis tipos de bloques M son de Hankel y se calculan por (65). El programa aplica M a cada columna y luego contrae con C^t: O(nD²+n²D) operaciones si hay n columnas y D coeficientes totales por fuente, frente a O(n²D²) para repetir las contracciones por parejas. Los intervalos de Gtilde_ij se amplían por [−E_ij,E_ij] y se suman por piezas. La simetría se impone copiando cada entrada superior a su transpuesta, pues ambas encierran el mismo número real exacto; esto no afirma positividad de cualquier matriz seleccionada de los intervalos.

El caché de logaritmos comprueba contexto, precisión, grado y parámetros intervalares antes de reutilizar una expansión. El caché de momentos pertenece a un único contexto a precisión fija. Reasociar los productos puede modificar la anchura intervalar, pero no su validez. No se ha cambiado la cota (72) ni se ha omitido ningún término de error.

check_interval_source_gram.py verifica todas las entradas de los Grams de {1,log t,log(1−t)} y {1,log(1+t),1+log(1+t)}, frente a fórmulas analíticas, con iv80 y grado64 para el logaritmo suave. El segundo ensayo ejercita la reutilización de una misma expansión entre columnas. Estos ensayos no incluyen las95 columnas del corrector ni el núcleoK384; sólo verifican la contracción conjunta y los errores suaves, sin repetir la cuadratura de referencia a130dps.

Queda pendiente medir y ejecutar el ensamblado con las columnas reales de U=E−WX. Los ensayos pequeños no acreditan el coste ni la anchura de los intervalos a esa escala, y el signo global sigue OPEN.

## Corrector congelado y columnas primitivas reales

Estado: procedimiento algebraico y código revisados independientemente; reconstrucción intervalar de95columnas porparidad PASS. Antecedente (73): Grams de prueba, todavía sin las columnas reales del corrector. frozen_corrector.py toma exclusivamente la matriz Z de los archivos blocks_even_160.npz y blocks_odd_160.npz, interpretándola como la matriz X de (58), de16 filas y95 columnas. Cada valor binario finito se convierte mediante as_integer_ratio en un racional exacto. Los archivos frozen_corrector_even_160.json y frozen_corrector_odd_160.json conservan esos racionales y el SHA256 de su fuente. El hash aporta trazabilidad, no una prueba matemática.

T se reconstruye como4/5, no como el racional correspondiente al flotante0.8 guardado. Las bases E,W se reconstruyen desde (47)-(51), sin importar las matrices flotantes A,P,K,D,S. Para el X racional fijado,

    U_i=e_i−Σ_{k=96}^{111}X_(k−96),(i−1) w_k,  i=1,...,95.       (74)

La notación de filas y columnas de X aquí comienza en0; las columnas matemáticas i corresponden al índice de código i−1. Para evitar ambigüedad operacional, el programa recorre la lista e_1,...,e_95 y la lista w_96,...,w_111 en ese orden. No se exige D=KX y el término de defecto de (69) permanece íntegro. La primitividad exacta de U_i sigue de las identidades de las bases; que un intervalo calculado del momento contenga cero es sólo una comprobación de implementación.

Para pasar a potencias físicas se usa la fórmula exacta

    p_n(x)=sqrt((2n+1)/T)
             Σ_{j=0}^n(−1)^(n+j)binom(n,j)binom(n+j,j)(x/T)^j. (75)

La reconstrucción emplea iv400 y160 términos en la serie positiva de momentos de (51), manteniendo su cota explícita de cola. Aumentar sólo dps habría dejado intacto el resto de32 términos; por eso stable_split admite ahora el parámetro terms, cuyo valor por defecto sigue siendo32 para los certificados anteriores.

Los datos congelados definen un corrector exacto reproducible aunque su elección proceda de un cálculo flotante. No certifican que ese corrector sea suficiente, ni trasladan a los nuevos cálculos los signos de matrices numéricas anteriores. Quedan pendientes las fuentes A_384U_i, sus Grams, el defecto Δ y el signo de (69).

Resultado guardado en frozen_corrector_check.json: las190 columnas reconstruidas pasaron los chequeos. Anchura máxima de momentos: <2.887e−400 (par), <1.071e−399 (impar). Anchura máxima de coeficientes físicos: <1.652e−309 (par), <2.347e−309 (impar). Estas cotas corresponden a la reconstrucción de U, no a A_384U ni al Gram. La procedencia racional exacta está conservada en los dosJSON de correctores congelados.

## Norma refinada y primera fuente del corrector real

Estado: refinamiento de la cota de error PROVED y código revisado independientemente; primera fuente real ensamblada con PASS. El antecedente (71) acota la norma del aproximante mediante valores absolutos de coeficientes. A grado alto esa cota puede perder las cancelaciones del polinomio; no es necesario conservarla si el Gram del aproximante ya está disponible.

Calcular primero Gtilde=d C^tMC, SIN añadir restos de Taylor. Como su diagonal encierra exactamente la norma cuadrada de la fuente aproximante en esa pieza,

    n_i,new=min(n_i, sqrt(upper(Gtilde_ii))),                  (76)

donde ambos argumentos del mínimo son cotas superiores y la raíz se redondea hacia arriba, sigue siendo una cota de ||Ftilde_i||_2. El presupuesto (72) se mantiene sustituyendo n_i por n_i,new. No hay circularidad: Gtilde corresponde a funciones explícitas ya integrables por (65), mientras el resto que se añade después corresponde a reemplazar los logaritmos suaves por sus polinomios. Se exige upper(Gtilde_ii)≥0; un intervalo ancho puede dar una cota pobre, pero no inválida.

interval_source_gram.py implementa este orden y conserva la cota anterior si fuese menor. Los dos Grams analíticos de3columnas volvieron a pasar; en el ensayo de logaritmo suave la anchura máxima bajó de3.83e−32 a1.004e−32. Esa comparación sólo describe el ensayo, no una mejora ya medida en las95 columnas.

build_real_source.py reconstruye la columna de índice0 de la paridad par del corrector racional (74), aplica el núcleo de grado384 y ensambla los cinco tramos de A_384U_0 con iv400. Es una columna del objeto real fijado, no un nuevo corrector ni un ensayo de grado reducido. La fuente polinómica tiene grado máximo496, junto con los tres multiplicadores logarítmicos de (64).

Para conservar el cálculo, el programa guarda cada extremo intervalar como su tupla diádica exacta de mpmath (signo, mantisa entera, exponente, longitud binaria), en JSON comprimido. No se convierten los coeficientes a decimales de menor precisión. El formato registra la versión de mpmath y la huella del JSON del corrector. El chequeo de pack/unpack compara todas las tuplas antes de escribirlas; la lectura del archivo persistido se controla separadamente.

Los valores puntuales en los puntos medios de las cinco piezas sirven para medir anchuras y comprobar que la evaluación es finita. No constituyen una prueba de signo de la forma, ni reemplazan la integración del Gram. La siguiente obligación sigue siendo formar las entradas integradas reales de (69).

Resultado de build_real_source.py: PASS para A_384U_0 par, cinco piezas, anchura máxima de coeficientes <2.954e−277; tiempo162.31s incluyendo reconstrucción, ensamblado y escritura. Artefacto real_source_even_0.json.gz, reporte real_source_check.json. Una lectura posterior comprobó sus4175intervalos a50dps: cada tupla diádica coincidió exactamente, con huella del archivo verificada. Esto certifica la persistencia de esos encerramientos, no la integral del Gram. El tiempo observado corresponde a esta columna; no se ha medido todavía el cálculo conjunto de95columnas.

## Primera entrada integrada del Gram de fuente real

Estado: encerramiento obtenido con código y fórmulas revisados y reproducido independientemente con el mismo resultado y huella de entrada. Antecedente (76): fuente real persistida pero sin integral. arb_source_integral.py ejecuta las mismas fórmulas (65),(66),(71),(76) con python-flint0.9.0, usando arb y arb_poly a500dígitos DECIMALES. La composición y multiplicación de polinomios se realizan en código nativo; no se cambia el operador ni se reemplazan las cotas por cuadratura.

Para transferir un intervalo con extremos diádicos a Arb, alinear sus exponentes: extremos L·2^e y H·2^e, enteros L≤H. Usar centro (L+H)·2^(e−1) y radio (H−L)·2^(e−1). El constructor de bola cubre sus redondeos; además se comprueba que la bola contiene ambos extremos exactos, cuya longitud binaria se exige no superior a la precisión de trabajo. La precisión de los radios de Arb puede ampliar el intervalo y queda incluida en las operaciones validadas.

La integral se calcula por piezas, con grado512 para los logaritmos suaves. Los momentos se evalúan mediante recurrencias armónicas en bolas. Primero se calcula la norma cuadrada del aproximante; después se añade el radio 2e nsharp+e². La partición exacta de (0,T) procede del generador del archivo, con huella comprobada; el lector verifica también que los extremos compartidos tienen idénticas representaciones diádicas. La mera contención de T en un intervalo no se presenta como prueba de identidad de extremos.

Resultado para la columna par de índice0 del corrector real:

    (G_V)_(0,0)=||A_384 U_0||²
       ∈ [0.443886963801320938000048529800836280833610634739973860113084376990299605579014185905735369725002044460152144474905033 ±3.97e−118]. (77)

La representación decimal mostrada es conservadora; el radio interno calculado es menor que2.548e−118. Los cinco radios por pieza son, respectivamente, menores que3.476e−288,2.548e−118,9.207e−177,6.725e−238 y2.254e−251. Los extremos, restos y metadatos se conservan en real_source_integral.json. El cálculo tomó40.51s después de cargar la fuente y pasó antes dos comprobaciones de integrales con valor analítico conocido.

Este valor es una entrada de G_V de (69), NO el valor de la forma a_T(U_0), ni una entrada del complemento de Schur, ni un autovalor. Su signo positivo por ser norma cuadrada no resuelve el problema. El avance consiste en disponer del primer producto integrado real con error controlado a los grados previstos. Faltan B_n, las demás entradas de G_V, S_X,K y Δ_K, y la verificación final de (69). Tampoco se extrapola el resultado de T=.8 a otras ventanas.

## Primera diagonal completa del criterio residual

Estado: cálculo intervalar encerrado; código, fórmulas y consecuencia sobre el subespacio infinito revisados, encerramiento reproducido independientemente con el mismo resultado. Antecedente (77): sólo G_V,00. arb_residual_diagonal.py calcula ahora B_n=<p_n,A_384U_0> para n=0,...,111 y completa los términos de la diagonal0 de (69).

Para las piezas disjuntas y los errores e_j de (71), el error de fuente global cumple ||V−Vtilde||²≤Σ_j e_j². Como ||p_n||_(L²(0,T))=1, el error de cada momento satisface

    |B_n−Btilde_n|≤sqrt(Σ_j e_j²).                            (78)

El programa integra los productos de los aproximantes con los polinomios normalizados, incluye los intervalos de coeficientes y añade el resto global de (78). No se usa la suma de valores absolutos de los coeficientes de p_n para esta cota. Con la misma fuente y el mismo corrector, verificados por sus huellas, reconstruye

    Γ_tail,00=G_V,00−Σ_{n=0}^{95}B_n²,
    S_X,K,00=Σ_{n=0}^{111}U_(n,0)B_n,
    Δ_(k,0)=Σ_{n=0}^{111}W_(n,k)B_n,
    G_U,00=Σ_{n=0}^{111}U_(n,0)².

Las dimensiones se fijan explícitamente a N95,M111,112coeficientes y16columnas altas para impedir truncaciones silenciosas de zip o uso de un peso incorrecto. Los coeficientes U,W se reconstruyen con los momentos exactos encerrados; no se importan valores flotantes de S ni de Δ.

El archivo real_residual_diagonal.json encierra:

- G_V,00≈0.443886963801320938;
- Γ_tail,00≈0.0028131096599416285;
- S_X,K,00≈0.261998862294024588;
- ||Δ_(·,0)||²≈2.21470841823e−26;
- G_U,00≈1.00054172185354570.

Incluyendo todos los términos de (69), su diagonal0 queda encerrada en

    M_00∈[0.2519673132466727407969558456690957078273489705956560402666800294610096850934486402921789940958736086707056292619032 ±1.87e−116]
        >1/4.                                                (79)

M aquí designa únicamente la matriz del criterio suficiente (69). No es la matriz completa del operador ni se afirma M≥0 a partir de una diagonal.

### Consecuencia sobre un subespacio infinito

La transferencia ya probada da S_exact,00≥M_00>1/4 para el operador verdadero A, no sólo para A_384. Sea e_1 la primera columna baja, H la compresión alta verdadera y c_1=Π_high A e_1. Para cualquier α complejo y v en el dominio de forma alto,

    a_T(αe_1+v)
      =a_T(v+αH^(−1)c_1)+S_exact,00|α|²
      ≥(1/8)||v+αH^(−1)c_1||²+(1/4)|α|².                    (80)

La fuente c_1 pertenece a L²; por coercividad, H^(−1)c_1 pertenece al dominio del operador y por tanto al de forma. La desigualdad acredita positividad estricta sobre span{e_1}⊕H_high, subespacio de codimensión94 dentro del sector par primitivo. No se interpreta1/8 como cota en la norma original de αe_1+v: el cambio triangular de (80) debe contabilizarse para eso.

Este resultado valida una parte infinita de la construcción en T=4/5, una ventana cuya positividad ya era conocida por otros certificados. No amplía el intervalo probado ni resuelve el signo de las otras94 direcciones bajas y sus acoplamientos. La matriz completa de (69) y el objetivo global siguen OPEN.

## Bloque principal con acoplamientos completos

Estado: formulación y código revisados; bloque8×8 encerrado y certificado positivo por LDL intervalar. Verificación independiente de los ocho menores principales por arb_mat.det: PASS_SYLVESTER, sin reutilizar la recurrencia LDL. Antecedente (79)-(80): una sola dirección baja. arb_residual_block.py selecciona las ocho primeras columnas del MISMO corrector congelado, mantiene las16 columnas altas y el complemento H_high definido por las95 direcciones bajas. No resuelve otro sistema ni modifica el portador al reducir el bloque verificado.

La generación de fuentes reutiliza polynomial_source.pieces y la fórmula (70) mediante un adaptador de contexto Arb. Los intervalos U,W reconstruidos con iv400 se transfieren por contención de extremos a Arb500dps. Las constantes se evalúan en el contexto vigente y las ramas de contactos siguen usando comparaciones certificadas. Todos los coeficientes de la fuente0 nativa se contrastan con los intervalos previamente archivados; el solapamiento es una comprobación de implementación, no el fundamento de la cota.

Por cada pieza se preparan todas las fuentes. Se integran sus productos cruzados y los112 momentos de cada columna. Con errores globales e_i=sqrt(Σ_piezas e_(i,pieza)²) y normas de los aproximantes calculadas antes de los restos, cada entrada del Gram se amplía por e_i n_j+n_i e_j+e_i e_j. Cada B_(n,i) se amplía por e_i, usando ||p_n||=1. Para I={0,...,7},

    Γ_I=G_V,I−B_(0:95,I)^t B_(0:95,I),
    S_I=(U_I^t B_I+B_I^t U_I)/2,
    Δ_I=W^t B_I,  G_U,I=U_I^t U_I.                           (81)

La media de las dos contracciones de S es válida porque A_384 es autoadjunto y ambas encierran la misma entrada exacta. Se forman TODAS las entradas de (69) en I, incluidos los términos mixtos de Γ,Δ^tΔ,G_U,G_V.

La factorización LDL se efectúa con bolas y sin pivotar. Cada pivote debe tener extremo inferior estrictamente positivo antes de utilizarlo como denominador. Si no se puede acreditarlo, la salida es LDL_INDETERMINATE y no se infiere negatividad. La certificación positiva del bloque M_I da, para C_Iα=Π_high AΣ_i α_i e_(i+1),

    a_T(Σ_{i∈I}α_i e_(i+1)+v)
      ≥(1/8)||v+H^(−1)C_Iα||²+α* M_I α.                     (82)

Se obtiene positividad estricta sobre span{e_1,...,e_8}⊕H_high, de codimensión87 dentro del sector par primitivo. Los pivotes de LDL no se interpretan como autovalores ni como cotas en norma L² de ese subespacio. La ejecución está parametrizada en el número de columnas hasta95, pero ejecutar un bloque8 no certifica los demás tamaños.

Para las siguientes ejecuciones se añadió arb_moment_convolution.py: si f_s tiene grado d, la convolución de sus coeficientes invertidos con la tabla μ_(s,0),...,μ_(s,d+111) tiene en la posición d+k el valor Σ_j f_(s,j)μ_(s,j+k). Sumando las tres componentes se obtiene g_k=∫t^k Ftilde; después <p_n,Ftilde> es la contracción de g_k con los coeficientes de p_n local. Se conserva el Jacobiano y los restos. La identidad fue revisada y pasó17 momentos analíticos, incluidos ambos logaritmos, y el caso nulo. La ejecución8×8 ya iniciada sigue con la contracción directa anterior; no se reinició para aplicar esta optimización. Ambas asociaciones encierran la misma integral, aunque sus anchuras puedan variar.

Resultado de la ejecución directa: POSITIVE_PRINCIPAL_BLOCK,451.30s. Los ocho pivotes intervalares son aproximadamente0.2519673132,0.0934374943,0.0447207476,0.00776144705,0.1100067499,0.0667125756,0.0177444232,0.1495851184; todos sus extremos inferiores son positivos. Los radios de los pivotes son menores que8e−108. real_residual_block_even_8.json conserva la matriz completa encerrada, los momentos, Gram, errores y huella del corrector. Esta ejecución usó productos polinómicos directos para los momentos, antes de la optimización por convolución invertida. El bloque8 no cambia la situación de las otras87 direcciones bajas pares ni de las95 impares, y no amplía la ventana T=4/5.

El revisor guardó real_residual_block_even_8_minors.json con huellas de matriz y corrector, simetría verificada y ocho menores positivos. El determinante de orden8 es1.59182184006199695...e−10, con radio<1.74e−117. Esta segunda verificación certifica positividad de la matriz encerrada; no fue una reintegración independiente de las ocho fuentes.

## Contracción matricial nativa y ejecución del sector par completo

Estado: reorganización algebraica y código revisados; ensayo analítico reproducido independientemente. Ejecución95×95 iniciada, sin resultado de signo todavía. arb_native_gram.py extiende la convolución invertida a los tres tipos de test t^k L_s. Para cada fuente j prepara

    Y_(s,k),j=∫_0^1 t^k L_s(t) Ftilde_j(t)dt,
    Gtilde=d C^tY,
    Btilde=P_local Y_(s=0,k≤111).                            (83)

En la última expresión el programa incluye también el factor físico d=b−a. Los coeficientes P_local son los de los polinomios normalizados compuestos con la transformación afín de la pieza. Los momentos de Y requieren sólo los seis productos de logaritmos ya tratados en (65). La cantidad de filas polinómicas se amplía cuando sea necesario para cubrir tanto las fuentes como los tests, incluidas componentes vacías.

Los dos productos matriciales se ejecutan con arb_mat; después se aplican exactamente los mismos presupuestos de error y norma refinada. No se cambia la matriz matemática que debe satisfacer (69). El ensayo del módulo verifica un Gram3×3 de logaritmos y una matriz2×3 de momentos polinómicos frente a valores conocidos, con reproducción independiente.

Se inició arb_residual_block.py --columns95 para las95 direcciones bajas pares del mismo corrector. La ejecución conserva todas las16 direcciones correctoras altas, los112 momentos y el complemento infinito. Si todos los pivotes del criterio resultan positivos, cubrirá el sector par primitivo completo en T=4/5; hasta obtener ese resultado no se da por probado. El sector impar y la positividad para todo T son obligaciones separadas.

El programa contrasta las64 entradas del bloque principal8 con los intervalos previamente certificados y preserva ese archivo al escribir nuevos resultados. Ese solapamiento verifica consistencia entre implementaciones, no reemplaza la prueba LDL de95dimensiones. La ejecución95 sigue activa al registrar este paso.

### Auditoría condicional del cierre del sector par

La revisión independiente comprobó que, SI el bloque M95 de (69) es definido positivo, no queda otra hipótesis de densidad para concluir positividad sobre el sector par primitivo completo. La descomposición E⊕H_high preserva el dominio de forma porque las95 columnas de E pertenecen al dominio del operador. La forma alta es cerrada y H≥1/8; C=Π_high AE tiene columnas L², y L=H^(−1)C es acotado desde el espacio finito de coordenadas bajas.

Además de positividad puntual, se obtendría un fondo uniforme. Con s=λ_min(M95)>0, F=Ex+v y w=v+Lx,

    a_T(F)≥(1/8)||w||²+s||x||²,
    ||F||²≤2||w||²+(||E||²+2||L||²)||x||²,
    λ_par≥min{1/16,s/(||E||²+2||L||²)}>0.                    (84)

Esta consecuencia sigue CONDICIONAL hasta que termine el test95. No proporciona todavía un valor numérico de λ_par, pues requiere encerrar s y las normas indicadas. No prueba el sector impar ni positividad para otras ventanas.

### Preparación del sector impar durante la ejecución par

El verificador admite ahora --parity even/odd, con even como valor por defecto. El ruteo de corrector, huellas, antecedentes y reportes por paridad fue revisado independientemente. La ejecución par ya activa no se reinició ni cambió de código en memoria; todavía no se lanzó la ejecución impar completa.

Para el sector impar, la inmersión F(t)=sgn(t)f(|t|)/sqrt2 es isométrica y la primitividad equivale al momento con sinh(x/2). stable_split reconstruye esas bases mediante la serie certificada y se usa exclusivamente frozen_corrector_odd_160.json. El ensamblador recibe σ=−1: el reflejo arquimediano tiene f(x)+f(y) y el contacto reflejado entra con signo positivo. El término2Σ_j|α_j(f)|² de (29) ya está incorporado en esa acción reflejada; añadirlo separadamente sería contarlo dos veces.

Las constantes de (49),(56),(67),(69) cubren ambas paridades. No se cambia el peso residual ni se reutilizan datos integrados del sector par para el impar. La comparación con real_source_even_0.json.gz se ejecuta sólo en paridad par. Esta preparación no es un certificado numérico impar: falta ejecutarlo y verificar sus pivotes.

## Verificación por congruencia y cota uniforme cuantitativa

Mientras continúa la ejecución95 se preparó una verificación independiente del LDL. verify_residual_congruence.py propone un precondicionador P mediante Cholesky a80dps del punto medio, pero esa etapa es sólo heurística. Congela cada entrada almacenada de P como un diádico exacto, comprueba radio cero en Arb500 y calcula B=PMP^t con intervalos. Si

    δ=min_i{lower(B_ii)−Σ_(j≠i)upper|B_ij|}>0,

Gershgorin acredita B>0. Esto obliga a que P sea invertible y por congruencia acredita M>0, sin exigir que el Cholesky aproximado o su inversa sean exactos. Un fallo heurístico o de dominancia se registra como indeterminación. El reporte conserva P, márgenes y hash de M. El archivo8 pasó esta verificación y el revisor la reprodujo; no se ejecutó todavía sobre95.

La misma congruencia da s=δ/||P||_F²≤λ_min(M). Para un bloque de r direcciones certificadas, escribir X_r para sus columnas, g=tr G_V,r y y=||X_r||_F. Usando E⊥W, ||E||²≤27/20, ||W||²≤1+ηbar, ηbar=10^(−370), y ξ≤10^(−35),

    ||U_r||²≤27/20+(1+ηbar)y²,
    ||H^(−1)C_r||≤ell
      =sqrt(1+ηbar)y
         +8[sqrt(g)+ξ sqrt(27/20+(1+ηbar)y²)],
    a_T(F)≥c_r||F||² sobre span(e_1,...,e_r)⊕H_high,
    c_r=min{1/16,s/(27/20+2ell²)}>0.                         (85)

La cota de ell procede de H^(−1)C_r=WX_r+H^(−1)R_res, con R_res=Π_high A U_r, y ||R_res||≤sqrt(g)+ξ||U_r||. No requiere calcular AW ni construir el inverso infinito. Para r95 cubriría el sector par completo; para r8 sólo cubre el subespacio ya certificado de codimensión87.

certify_uniform_subspace_bound.py reproduce la congruencia usando P guardado y calcula (85) con extremos conservadores, verificando hashes, simetría, tamaños, T4/5 y K384. En el bloque8 obtuvo s>6.42687939e−7, ell<36.086398365 y c_8>2.46636882e−10. Es una cota en la norma L² ORIGINAL sobre ese subespacio restringido; no es una cota de λ_A sobre todo el portador ni debe compararse como tal con el fondo de la forma completa. Los reportes son real_residual_block_even_8_congruence.json y real_residual_block_even_8_uniform_bound.json.

El revisor reprodujo también certify_uniform_subspace_bound.py: PASS_UNIFORM_BOUND, con la misma cota c8 y alcance restringido. No se repitió ni se reinició el cálculo95 activo.

### Ejecuciones completas activas

La ejecución par terminó de ensamblar sus95 fuentes y continúa integrando el bloque completo; aún no produjo resultado LDL95. Tras comprobar disponibilidad de recursos, se inició en paralelo la ejecución impar95 con --parity odd y prioridad de CPU reducida mediante nice. Usa archivos distintos y el corrector impar ya congelado; no modifica ni reinicia la ejecución par. No se declara certificado ninguno de los dos bloques completos mientras sus resultados no existan y se verifiquen.

### Correspondencia con las definiciones vigentes del Paper47

Se cotejaron eq:symbol, eq:form, la definición de lamA y el inciso(o) de thm:parityschur del archivo main.tex vigente, sin modificarlo. El coeficiente de contacto es v_n=2Λ(n)/sqrt(n), las dos restricciones son ∫F exp(±t/2)=0 y la norma de λ_A es la norma L² usada aquí. Las inmersiones con factor1/sqrt2 conservan esa norma.

En (84)-(85), λ_par significa el fondo del sector PRIMITIVO con los primos incluidos, es decir λ_A^par del paper, no el fondo arquimediano sin primos que usa una notación semejante en otra sección. Si ambos certificados completos dan constantes c_even,c_odd>0, la descomposición ortogonal para la norma y la forma da λ_A(4/5)≥min(c_even,c_odd). Sigue siendo una conclusión condicional mientras falte cualquiera de los dos certificados; no afirma positividad de la forma completa W_T fuera del portador primitivo ni para ventanas mayores.


## Ensamblado simultáneo de las fuentes polinómicas

Estado: identidad y código revisados independientemente; comprobaciones de implementación PASS. Es una reorganización de (70), no un mecanismo nuevo para el signo. Para f(x)=Σ_m F_m x^m y r_K(u)=Σ_k c_k u^k, definir

    H_(j,m)=T^(m+j+1)/(m+j+1),
    L_(l,j)=[(-1)^l+σ] c_(l+j) binom(l+j,l), l+j≤K,
    Q_(n,m)=2 c_k m! k!/(m+k+1)!, k=n−m−1 impar, 1≤k≤K.

Las demás entradas son cero. La acción regular de (70) es

    integral_regular(f)=[embed(LH)+Q] F.                    (86)

En la fuente A_K f entra con signo negativo. Se añaden las matrices exactas de D_T, de la división reflejada y de la constante de (64). Cada traslado usa S_(j,m)=binom(m,j) b^(m−j) a^j para f(b+ax), con actividad por pieza certificada y extensión por cero en contactos. Los tres multiplicadores logarítmicos se mantienen separados. Así todas las columnas comparten la matriz arquimediana y las matrices de traslación.

arb_source_batch.py implementa esta asociación con Arb. check_arb_source_batch.py compara la columna real par0, de grado111 y núcleo384, con el archivo preservado:4160 coeficientes compatibles, radio máximo<9.1e−278,17.67s de ensamblado. arb_source_batch_check.json conserva huellas y alcance. El revisor auditó las fórmulas y reprodujo un ensayo de dos columnas, grado4/núcleo8, ambas paridades y cinco piezas:580 comparaciones PASS, radios<1e−65. El solapamiento es un control de implementación; no demuestra igualdad por sí solo ni certifica un nuevo Gram.

Las ejecuciones95 ya activas continúan con su ensamblador original; no se reiniciaron. El nuevo módulo queda disponible para ejecuciones posteriores y no se ha conectado todavía al verificador principal. Al registrar, el par había integrado las piezas0,1,2 y el impar había ensamblado sus95 fuentes e integrado la pieza0. Todavía no hay resultado completo de signo.

La obligación global no se reduce al coste del ensamblado: hace falta construir correctores y demostrar, para cada T, la dominación matricial del residuo en (69), con constantes adaptadas a esa ventana. Las constantes1/8,1783/500 y los grados de este certificado pertenecen a T=4/5; no se trasladan a otras ventanas sin prueba. Esta optimización no cumple esa obligación ni identifica aún la cancelación aritmética requerida.


## Aproximación del núcleo en cualquier ventana finita

Estado: PROVED como lema auxiliar, identidad y cotas revisadas independientemente. Antecedente: (60)-(63) usa un Taylor local para T=4/5. Esta extensión elimina la restricción del radio de ese desarrollo; no constituye una nueva fuente de signo. No se reclama novedad del procedimiento de Bernstein.

Para u≥0 definir, incluyendo las continuaciones en cero,

    B(u)=2∫_0^1 exp(−2ut)dt,
    N(u)=∫_0^1∫_(1/2)^(2t) exp(−us)ds dt,
    r(u)=N(u)/B(u).                                         (87)

La integral interior es orientada cuando 2t<1/2. Para u>0, N=(exp(−u/2)−B/2)/u, de modo que (87) es exactamente H0(u)−1/(2u). En cero, B(0)=2,N(0)=1/2 y r(0)=1/4.

En 0≤u≤2T, los parámetros s de la integral están en[0,2], la longitud de cada intervalo es≤3/2 y

    B≥2exp(−4T), |B'|≤2, |N|≤3/2, |N'|≤3,
    |r'|≤L_T:=(3/2)exp(4T)+(3/4)exp(8T).                    (88)

Las cuatro primeras cotas proceden directamente de las integrales; la última aplica la regla del cociente. Sean n≥1 y q_j aproximaciones a r(2Tj/n) con |q_j−r(2Tj/n)|≤ε. Poner x=u/(2T) y

    r_n(u)=Σ_(j=0)^n q_j binom(n,j)x^j(1−x)^(n−j).

Si J tiene distribución binomial(n,x), la positividad y suma uno de los pesos, Cauchy–Schwarz y Var(J/n)=x(1−x)/n dan

    |r_n(u)−r(u)|≤ε+L_T·2T E|J/n−x|
                  ≤ε+L_T T/√n=:δ_n.                        (89)

Esta es una prueba de la cota, no una hipótesis de convergencia numérica. Los nodos se pueden encerrar mediante exponenciales, usando el valor exacto en cero. Si T es racional y q_j racionales, r_n tiene coeficientes racionales en u. Para T real arbitrario puede elegirse un R racional mayor que T, construir el polinomio en[0,2R] y restringirlo; no se afirma que una normalización por un T irracional conserve coeficientes racionales físicos.

Definir s_n(u)=−∫_0^u r_n(v)dv y sustituir núcleo y cola conjuntamente como en (62). La diferencia entre el operador exacto y el aproximado tiene exclusivamente núcleo

    −[(r−r_n)(|x−y|)+σ(r−r_n)(x+y)],
    ||A_T−A_(T,n)||≤2Tδ_n.                                 (90)

La cota vale en ambas paridades por Schur, pues x,y∈[0,T]. La diferencia es acotada y simétrica y no cambia el dominio del operador singular original. Los contactos aritméticos y los dos momentos no se aproximan en este paso.

Para obtener un error operador≤ζ>0 basta elegir ε≤ζ/(4T) y n≥(4L_T T²/ζ)². Para coeficientes racionales en una ventana real usar R>T y esas mismas elecciones con R, lo que da una cota válida también en T. El coste puede ser enorme: es una construcción explícita de existencia con error controlado, no una recomendación de implementación frente a Taylor por tramos u otras aproximaciones más eficientes.

Consecuencia limitada: el radio de convergencia del Taylor local no impide definir certificados residuales de precisión arbitraria en otras ventanas. Todavía hay que construir un corrector y probar el signo del criterio matricial correspondiente. Hacer δ_n pequeño no prueba esa desigualdad, ni garantiza que un corrector dado la satisfaga; los falsificadores también admiten esta aproximación. No se ha obtenido una ventana positiva nueva ni una prueba global.


### Integración opcional del ensamblador compartido

El verificador acepta ahora --source-method batch; direct sigue siendo el valor predeterminado. Ambas ramas usan las mismas columnas y desembocan en la misma integración y criterio. El ruteo fue revisado independientemente. Los reportes identifican source_method, los archivos batch tienen nombre separado y las nuevas ejecuciones preservan archivos existentes mediante sufijos runN. Los procesos95 ya activos no cambiaron. Se inició una comprobación integral de una columna par con batch, todavía sin resultado al registrar; no se atribuye a esta preparación un certificado nuevo.


La comprobación integral batch de una columna terminó en83.06s: POSITIVE_PRINCIPAL_BLOCK, criterio00=0.2519673132466727407969... con radio<1.91e−116 y extremo inferior>1/4. real_residual_block_even_1_batch.json conserva el resultado. Se comprobaron114 solapamientos con el certificado8 previo:112 momentos, Gram00 y criterio00, con igualdad de la huella del corrector. real_residual_block_even_1_batch_crosscheck.json registra PASS_END_TO_END_CROSSCHECK y ambas huellas. Es una validación de implementación de la misma dirección ya certificada, no un nuevo subespacio ni ventana de positividad.


## Complemento coercivo y pesos residuales para todo T fijo

Estado: PROVED como extensión auxiliar de (38)-(58), revisada independientemente. No es un nuevo mecanismo de signo. Fijar T>0, γ>0 y una paridad, con h=cosh(x/2) o sinh(x/2). Conservar κ_T,c_T de (38), incluidos todos los contactos de esa ventana. Elegir un entero N≥1 que satisfaga

    δ_N=T exp(T)(T/2)^(2N+2)/[((N+1)!)²||h||²]≤1/2,
    κ_T H_(N+1)≥2|c_T|+2γ.                                (91)

La selección termina: para T fijo, δ_N→0 por el factorial y H_(N+1)→∞, mientras κ_T>0 y c_T es finito. Se puede aumentar N hasta verificar ambas desigualdades con cotas conservadoras; no se usa el signo de la forma para escogerlo. Las normas de h son las de (49) y son estrictamente positivas para T>0.

Generalizar (47),(50) a este N: E=span(e_1,...,e_N), h_low=Σ_(0≤n≤N)α_n p_n y w_k=p_k−α_k h_low/||h_low||² para k≥N+1. Como α_0>0 y la aproximación de Taylor da ε≤δ_N, poner eta_bar=δ_N/(1−δ_N)≤1. Entonces

    ||W∞||²≤1+eta_bar≤2,
    a_T(W∞z)≥Σ_(k≥N+1)d_k|z_k|²,
    d_k=κ_T H_k+c_T−|c_T|eta_bar,
    d_(N+1)≥2γ.                                           (92)

La comparación modal procede de (39); el término de norma baja sólo cuesta |c_T|eta_bar. La última desigualdad usa (91) y |c_T|+c_T≥0. Por tanto el operador H de la forma restringida al complemento alto exacto satisface H≥γ en la norma física. Esto conserva exactamente el momento de la paridad y, mediante la inmersión correspondiente, los dos momentos originales.

Para cualquier M≥N+1 y cualquier corrector finito Z=W_M X, definir C=Π_high AE, R=C−HZ, Δ=W_M*R y S_X=P−D*X−X*D+X*KX como antes. La misma prueba variacional de (57)-(58) da

    S_exact=S_X−R*H^(-1)R,
    R*H^(-1)R≤rho R*R+tau Δ*Δ,
    rho=(1+eta_bar)/d_(M+1),
    tau=1/d_(N+1)−1/d_(M+1)≥0.                            (93)

Las columnas polinómicas primitivas están en el dominio del operador por la misma acción con extremos logarítmicos y un número finito de contactos; no aparece una condición espectral nueva. El denominador en (93) es positivo por (92). No se presupone que X sea una solución exacta del sistema finito.

Así el criterio suficiente S_X−rho R*R−tau Δ*Δ≥0 está disponible en cada ventana finita. Junto con (87)-(90), queda resuelta la existencia de una cola coerciva y de una aproximación arbitrariamente precisa del núcleo en cualquier T. No queda resuelto encontrar X y demostrar el signo de ese criterio para cada T. Tampoco se afirma convergencia del residuo al aumentar M, terminación del test de positividad ni una identidad positiva global. Estas herramientas de reducción siguen siendo aplicables a formas falsificadoras con contactos finitos; no aportan por sí mismas la distinción aritmética que falta.


## Certificado completo del sector par en T=4/5

Estado: cálculo intervalar95 terminado, verificado por congruencia y reproducido independientemente en la etapa de certificación matricial y cota uniforme. real_residual_block_even_95.json terminó en3666.00s con95pivotes LDL estrictamente positivos y solapamiento de las64entradas del bloque8 anterior. Su SHA256 es91bc989abd773bdb6b61f8a23ec30730650e2b3e2d938a59d8ed43c87174a7ab. La ejecución comenzó antes de añadirse el campo parity al reporte; la paridad par queda identificada por el corrector congelado y su huella, no por una inferencia del nombre solamente.

verify_residual_congruence.py produjo PASS_CONGRUENCE en dimensión95. El precondicionador diádico exacto y los márgenes de dominancia están en real_residual_block_even_95_congruence.json. certify_uniform_subspace_bound.py reprodujo la congruencia y aplicó(85), dando PASS_UNIFORM_BOUND, scope full parity:

    s>4.79542948e−12,
    ell<284.400740,
    a_(4/5)(F)≥2.96437025e−17 ||F||²
      para todo F del sector par primitivo.                 (94)

La última desigualdad incluye todas las95direcciones bajas y el complemento infinito, mediante(84)-(85); no interpreta los pivotes como autovalores. real_residual_block_even_95_uniform_bound.json conserva las cotas y huellas. El redondeo de(94) es hacia abajo respecto del encerramiento obtenido.

Este resultado completa el certificado residual par en una ventana ya conocida positiva por otras vías. No amplía la ventana probada ni acredita aún el sector impar, cuya ejecución95 sigue activa. No prueba la positividad global ni proporciona la regla aritmética de construcción para todos losT.

El revisor reprodujo PASS_CONGRUENCE y PASS_UNIFORM_BOUND sobre el archivo95, verificó huellas/dimensiones y confirmó el alcance de(94) sobre todo el dominio de forma par primitivo. No reintegró las95fuentes ni modificó reportes o el proceso impar.


## Cierre del certificado local sobre ambas paridades

Estado: ambos bloques95 positivos, verificados por congruencia; revisión independiente de ambos sectores y su combinación completada. La ejecución impar terminó en3661.78s con95pivotes LDL positivos. real_residual_block_odd_95.json tiene SHA256 288085f3be1a57c3b496a5cb27416fb8102b2f101418a61ba32427d9becd0fd7 y huella del corrector impar130a68519fe65899ab5da92d2817de538d8b068ab908a23f25145d63ed1a9d80.

La congruencia y la cota uniforme(85) dieron PASS_CONGRUENCE y PASS_UNIFORM_BOUND:

    s_odd>1.05649760e−9, ell_odd<288.587238,
    a_(4/5)(F_odd)≥6.34279623e−15 ||F_odd||².                (95)

Para F primitivo, F_even y F_odd satisfacen sus respectivos momentos hiperbólicos; la reflexión conmuta con la forma. Por ortogonalidad de norma y forma, (94)-(95) implican

    a_(4/5)(F)≥2.96437025e−17 ||F||²,
    λ_A(4/5)≥2.96437025e−17>0.                              (96)

Se reprodujeron ambas congruencias y cotas antes de guardar real_residual_full_T4_5_certificate.json, PASS_BOTH_PARITIES. El reporte incluye las dos cadenas de huellas, el alcance full parity de cada una y la cota conjunta redondeada hacia abajo. La combinación usa la descomposición analítica anterior, no un test adicional sobre vectores aislados.

Queda cerrado el certificado residual de BUILD083 sobre TODO el dominio primitivo en T=4/5. No se obtuvo una ventana nueva ni se mejoró el fondo conocido: la cota es conservadora. No hay cálculos95 pendientes. La positividad para todoT y el diseño aritmético que fuerce (93) siguen OPEN; (96) no autoriza extrapolar el corrector o sus constantes a ventanas mayores.

El revisor reprodujo la congruencia y cota impar, verificó dimensión/paridad/huellas y confirmó(96) por ortogonalidad de la reflexión. La revisión no fue una reintegración independiente de fuentes.


## Corrector de residuo mínimo y actualización exacta

Estado: PROVED como lema auxiliar de diseño, revisado independientemente. Antecedentes: correctores(43)-(46),(93), sin monotonía del residuoL², y mínimos cuadrados RAT-DD registrados en el índice maestro(líneas25754-55 al consultar). No se atribuye novedad a mínimos cuadrados, ni se presenta como una ruta nueva para el signo. No se ejecutó otra campaña numérica.

Con H≥γ>0 en el complemento alto, W_M las columnas altas independientes y C=Π_high AE, definir

    Y_M=H W_M, G_M=Y_M*Y_M,
    X_M=G_M^(-1)Y_M*C, Z_M=W_M X_M,
    R_M=C−H Z_M=(I−P_range(Y_M))C.                         (97)

Las columnas de W_M están en Dom(H), por lo que Y_M pertenece aL². Además G_M≥γ²W_M*W_M>0, justificando el inverso finito sin usar positividad de la forma completa. Los rangos son anidados y sus proyectores ortogonales satisfacen P_(M+1)≥P_M. De ello resulta

    R_(M+1)*R_(M+1)≤R_M*R_M.                              (98)

La desigualdad vale simultáneamente en todas las direcciones bajas, no sólo para la traza. Existe también una actualización explícita. Poner w=w_(M+1), y=Hw,

    a=G_M^(-1)Y_M*y, q=y−Y_M a,
    Z_(M+1)=Z_M+(w−W_M a)(q*C)/||q||²,
    R_(M+1)=R_M−q(q*R_M)/||q||²,
    R_M*R_M−R_(M+1)*R_(M+1)
       =R_M*q q*R_M/||q||²≥0.                            (99)

Como H es inyectivo y w no pertenece a span(W_M), q≠0. La ortogonalidad q⊥range(Y_M) da q*C=q*R_M y prueba las fórmulas por proyección ortogonal. La elección usa las imágenes del operador alto y un Gram finito; no invierte la forma completa ni supone el signo del Schur.

Lo que se resuelve: al aumentar el espacio corrector, el residuoL² de ESTA elección no crece. Lo que no se resuelve: no hay aquí una prueba de densidad de la unión range(Y_M), ni convergenciaR_M→0, ni control del condicionamiento de G_M. Además Y_M*R_M=0 no equivale a W_M*R_M=0: el defectoΔ de(93) no desaparece como en Galerkin energético. S_X cambia también, por lo que(98) NO implica monotonía ni positividad del criterio completo. Sigue faltando la desigualdad aritmética global. Los correctores congelados del certificado local no se sustituyeron ni se reinterpretaron como soluciones de(97).


## Optimización conjunta del certificado escalar

Estado: PROVED como reparación auxiliar del diseño(97)-(99), revisada independientemente. Antecedente: allí sólo decrece el Gram residual, sin monotonía del criterio completo. Se optimiza ahora el criterio escalar de(46); no se atribuye novedad a la completación de cuadrados ni se afirma una nueva fuente aritmética de signo.

Fijar el portador bajo E, su complemento H≥γ>0 y un número r>1/γ. Para Z=WX, Y=HW, K=W*HW, D=W*C, poner

    R=C−HZ,
    J(X)=S_X−rR*R,
    G=rY*Y−K, B=rY*C−D.                                  (100)

Se tiene Y*Y≥γK y K>0, luego G≥(rγ−1)K>0. Esta desigualdad sólo exige W⊂Dom(H); Y*Y es un GramL² y no requiere que las columnas estén en Dom(H²). La expansión exacta es

    J(X)=P−rC*C+B*X+X*B−X*GX,
    X_opt=G^(-1)B,
    J_opt=P−rC*C+B*G^(-1)B,
    J_opt−J(X)=(X−X_opt)*G(X−X_opt)≥0.                    (101)

El óptimo es simultáneo en orden de Loewner para todas las coordenadas bajas, no sólo un máximo de traza. Si W_M⊂W_(M+1), conservando EL MISMO E,H y r, el corrector anterior se incluye entre los admisibles nuevos y(101) implica

    J_opt,M≤J_opt,M+1≤S_Schur,
    S_Schur−J(X)=R*(rI−H^(-1))R≥0.                        (102)

La última identidad procede de S_Schur=S_X−R*H^(-1)R. H^(-1) aparece sólo en la prueba del error; la fórmula constructiva(101) usa imágenes HW y matrices finitas, sin invertir la forma completa ni suponer su signo.

Esto resuelve la falta de monotonía conjunta del certificado ESCALAR: ampliar el corrector optimizado no empeora su minorante. No demuestra que J_opt alcance cero, que R tienda a cero ni que el límite sea S_Schur. Tampoco permite cambiar N,E o r entre pasos y conservar la monotonía sin nueva prueba. No se compara como superior al criterio MODAL(69), que tiene información adicional y fue el usado en los certificados locales. No se sustituyeron correctores congelados ni se lanzó otra campaña computacional.

Obligación restante explícita: obtener una cota aritmética que fuerce P−rC*C+B*G^(-1)B≥0 para una elección constructiva de espacio corrector en cadaT, o controlar su límite y su signo por otra identidad. La monotonía sola admite límites negativos y también vale para los falsificadores; no cierra el objetivo global.


## Ganancia exacta por dirección correctora

Estado: PROVED, revisado independientemente, como actualización de(101)-(102). Mantener fijos H,C,P,r y el portador bajo. Usar producto interior conjugado-lineal en la primera entrada y la métrica positiva

    g(u,v)=r<Hu,Hv>−<u,Hv>, u,v∈Dom(H).

Sea Z_old el óptimo sobre span(W), G=g(W,W), y elegir w∈Dom(H) fuera de span(W). Definir

    a=G^(-1)g(W,w), q=w−Wa, d=g(q,q)>0,
    b=r(Hq)*C−q*C,
    Z_new=Z_old+q b/d,
    J_new=J_old+b*b/d.                                    (103)

La ortogonalización da g(W,q)=0 y q≠0. Al escribir un corrector en span(W,q), el término cuadrático de(101) queda separado entre ambas componentes; completar el cuadrado en la fila nueva da(103). La nueva elección es el óptimo conjunto, no una heurística que conserva por conveniencia los coeficientes viejos.

Además, R_old=C−HZ_old satisface exactamente

    b=(rHq−q)*R_old,
    x*(J_new−J_old)x=|bx|²/d.                              (104)

La primera identidad usa g(q,Z_old)=0. Así se identifica el detector concreto de una dirección útil: bx≠0 produce mejora estricta del criterio en x. No implica que todas las direcciones bajas mejoren estrictamente con un único q; la ganancia tiene rango a lo sumo uno.

Partiendo de Z_0=0 y ortogonalizando sucesivamente candidatos independientes en g, se obtiene la identidad finita

    J_m=P−rC*C+Σ_(j=1)^m b_j*b_j/d_j.                     (105)

El procedimiento usa Hq, sin aplicar H² a q. No se supone convergencia de la suma infinita. La tarea de diseño aritmético queda expresada como elegir candidatos cuyos aportes conjuntos dominen rC*C−P. Escribir esa obligación no la demuestra: el término inicial puede ser indefinido, los incrementos pueden dejar direcciones sin compensar y los falsificadores admiten las mismas identidades. No se ha encontrado todavía una regla aritmética que asegure esa dominación para todoT. No se alteran los certificados locales ni se reclama novedad del álgebra de Gram.


## Semillas aritméticas con saltos para el corrector

Estado: CANDIDATO INCOMPLETO; dominio y puerta de desarrollo revisados independientemente. Antecedentes: BUILD079, que descarta extraer directamente el cuadrado del operador causal de Möbius, y(103)-(105), que permiten enriquecer un corrector optimizado. El cambio concreto es usar ese operador para producir direcciones de ensayo, sin exigir la dominación del cuadrado descartado. No se presenta como mecanismo de signo ni como prueba de ventaja de Möbius.

Trabajar en I=(-T,T), con extensión por cero. Sea p_j el polinomio de Legendre normalizado en I, U_l f=1_I f(·−l), y definir exactamente como en BUILD079

    E_T=Σ_(2≤n<exp(2T)) Λ(n)/(√n log n) U_log n,
    R_T=exp(−E_T)=Σ_(1≤n<exp(2T)) μ(n)/√n U_log n.          (106)

La exponencial es un polinomio finito por nilpotencia de los retardos. La igualdad de coeficientes procede del producto formal de Euler y no requiere convergencia de una serie infinita. No se confunde R_T con el residuo R de(100).

Para σ=±1, Π_σ f(t)=[f(t)+σf(−t)]/2; tomar h_+=cosh(t/2), h_−=sinh(t/2) en I. Sea E_σ la inmersión isométrica del espacio bajo primitivo previamente construido en esa paridad. El proyector alto exacto, escrito en el espacio completo, es

    Q_high,σ=Π_σ−h_σ(h_σ*·)/||h_σ||²
                   −E_σ(E_σ*E_σ)^(-1)E_σ*,
    w_j=Q_high,σ R_T p_j.                                 (107)

Los dos términos sustraídos son ortogonales porque E_σ es primitivo. La primera resta elimina el momento de la paridad; la otra lo preserva. La condición del otro momento se cumple automáticamente por paridad. Todas las entradas de los proyectores son integrales explícitas de polinomios, exponenciales y funciones a trozos.

Cada R_T p_j es una suma finita de polinomios trasladados con saltos en los puntos −T+log n. Es BV y su acción arquimediana tiene singularidades logarítmicas en un número finito de puntos, que pertenecen aL². Las proyecciones de(107) sólo añaden funciones suaves por tramos, con posibles irregularidades en cero por la inmersión de paridad y cortes en los extremos. Por tanto w_j pertenece aDom(H) del complemento alto correspondiente; no se necesita aplicar H².

La regla constructiva es recorrer j=0,1,..., ortogonalizar w_j contra las direcciones aceptadas en la métrica g de(103) y aceptar sólo si d_j=g(q_j,q_j)>0. Una semilla nula o dependiente se descarta sin dividir por cero. Con cada semilla aceptada se calculan

    b_j=(rHq_j−q_j)*R_old,
    Z_new=Z_old+q_j b_j/d_j,
    J_new=J_old+b_j*b_j/d_j.                              (108)

Si se inicia desde un corrector optimizado no vacío, se conserva ese espacio y se enriquece; si se inicia desde cero, rige el telescopado(105). Los saltos interiores pueden ampliar el espacio polinómico finito previo, pero no se afirma independencia de todas las semillas ni densidad en norma de grafo.

La identificación de coeficientes con μ se pierde para pesos genéricos; esto sólo distingue una identidad aritmética, NO prueba que el resto tenga signo exclusivamente para Λ. La ganancia(108) sigue siendo no negativa para cualquier dirección admisible y cualquier falsificador con complemento coercivo. Falta demostrar que estas semillas produzcan una compensación total de rC*C−P para todoT, o encontrar una modificación que lo haga. No se evaluó todavía b_j para esta familia ni se afirmó que sea distinto de cero. No se reemplazaron los correctores de los certificados locales.


## Densidad L² y primera dirección realmente nueva

Estado: PROVED como propiedades auxiliares de(106)-(108), revisadas independientemente. No son pruebas del signo ni de convergencia en norma de grafo. Los desplazamientos positivos comprimidos satisfacen U_l U_s=U_(l+s), y U_l=0 casi en todas partes si l≥2T. Por μ*1=δ, el inverso explícito finito es

    D_T^arith=Σ_(1≤n<exp(2T))n^(-1/2)U_log n,
    R_T D_T^arith=D_T^arith R_T=I.                         (109)

Sea P_m la proyección L² sobre los primeros m+1 polinomios de Legendre en TODO I. Para f del complemento alto de paridadσ, la combinación finita de semillas

    f_m=Q_high,σ R_T P_m D_T^arith f

satisface

    ||f_m−f||≤||R_T|| ||(I−P_m)D_T^arith f||→0,
    ||R_T||≤Σ_(n<exp(2T))|μ(n)|/√n.                       (110)

La cota sigue de la contracción del proyector alto y la identidad(109); la convergencia usa la completitud L² de Legendre. Así las semillas cubren densamente el complemento alto enL². No se intercambia esta topología por la norma de grafo deH: (110) no controla Hf_m ni prueba que el residuo de(108) tienda a cero.

Hay además una dirección nueva explícita en la ventana ya certificada. Para T=4/5 y p_0=1/√(2T), los únicos saltos aritméticos no triviales de R_Tp_0 son los de n=2,3, pues μ(4)=0. En t_2=log2−T el salto antes de separar paridad es−1/(2√T). Ningún salto reflejado coincide con él: tal coincidencia exigiría nm=exp(2T), imposible porque

    4 < 609427507/123046875 < exp(8/5)
      < 115187041703/23255859375 < 5.

Estas cotas racionales salen de truncar la serie exponencial en grado8 y acotar la cola por su primer término dividido por1−(8/5)/10. Por tanto, en ambas paridades, la semilla w_0 de(107) conserva el salto

    jump_(t_2)(w_0)=−1/(4√T)=−√5/8.                      (111)

Las funciones sustraídas por la proyección alta son suaves CERCA de t_2≠0; no se supone suavidad global de sus extensiones en cero. Ninguna combinación del espacio alto polinómico finito anterior tiene ese salto interior. En consecuencia w_0 no pertenece a ese espacio y su ortogonalización en g tiene d>0. Esto acredita que el enriquecimiento añade una dirección admisible, no que la fila b correspondiente sea no nula ni que su ganancia sea suficiente. El cálculo o signo de esa ganancia y el control en norma de grafo permanecen abiertos.


## Núcleo de operador de las semillas y convergencia del corrector

Estado: PROVED como resultado auxiliar, con revisión independiente de conmutador, dominios, núcleo de operador y convergencia. Antecedentes: transmisión logarítmica por Carleman en P121_DYADIC_RADICAL_BOOTSTRAP, Lema2.2 (índice maestro), estimaciones(15)-(22) y densidadL²(110). No se reclama novedad del ingrediente Carleman. Se resuelve aquí la topología requerida por el corrector, sin usar ni concluir el signo global.

Sea A0 el operador arquimediano autoadjunto en la recta. Por su símbolo explícito, su norma de grafo equivale a

    ||f||_log²=∫[1+log²(2+|ξ|)]|fhat(ξ)|²dξ.              (112)

Para χ=1_I, el bloque cruzado del operador tiene núcleo −H0(|x−y|). Se verifica para u>0

    uH0(u)≤(1/2+u)exp(−u/2)≤1/2+2/e<2.

Cada extremo del intervalo se reduce por traslación/reflexión a un operador dominado por2/(s+t),s,t>0. Schur con peso s^(−1/2), usando ∫_0^∞t^(−1/2)/(s+t)dt=πs^(−1/2), acota su norma por2π. Sumando los dos extremos, el bloque cruzado y el conmutador quedan acotados por4π.

Para f Schwartz, χf esBV compacto y pertenece aH^s para0<s<1/2, luego aDom(A0). La identidad de conmutador calculada por el núcleo da

    ||[A0,χ]f||≤4π||f||.                                 (113)

Extender desde el núcleo Schwartz en norma de grafo y usar que A0 es cerrado prueba χDom(A0)⊂Dom(A0) y la misma identidad en todo el dominio. Para identificar la compresión, restar de A0 el operador autoadjunto acotado formado por sus dos bloques cruzados. El resultado es autoadjunto enDom(A0), conmuta conχ y se descompone en suma directa. Su bloque interior coincide con la compresión de la forma arquimediana. Por tanto el dominio de ese bloque es exactamente las funciones deDom(A0) soportadas en I, con norma de grafo equivalente a(112) aplicada a la extensión por cero. Los contactos son una suma finita de operadores acotados en cadaT y no cambian ese dominio.

Los polinomios en I, extendidos por cero, constituyen un núcleo de operador de esta compresión. Para demostrarlo, contraer primero el soporte de f∈Dom(A0) hacia el interior mediante dilataciones unitarias. Éstas convergen fuertemente en(112): sus normas son uniformemente acotadas para factores cercanos a1, y la convergencia se comprueba primero enSchwartz y se extiende por densidad. Mollificar después con soporte menor que el margen disponible aproxima en(112) por funcionesC∞ compactas en I. Cada función así obtenida se aproxima enC¹ del intervalo cerrado por polinomios (aproximar uniformemente su derivada e integrar). La extensión por cero del error tiene normaH^s,s<1/2, controlada por su normaC¹; esto se obtiene separando el seminorma fraccionario dentro de I y el término de borde, cuya integral d(x,∂I)^(−2s) es finita. Finalmente H^s controla(112). Se trata de existencia de aproximantes polinómicos; NO se afirma convergencia en grafo de las proyecciones ortogonales P_m usadas en(110).

Las traslaciones de la recta conmutan conA0, por lo que U_l=χτ_lχ es acotado en norma de grafo por(113). Las sumas finitas R_T y D_T^arith son entonces operadores inversos acotados en esa norma. Transportar el núcleo polinómico a través de R_T da un núcleo de operador formado por span{R_Tp_j}.

La reflexión preservaDom(A0). Las proyecciones finitas sobre h_σ y E_σ también preservan el dominio, y sus conmutadores con el operador comprimido son acotados: para una columna v∈Dom(A), los coeficientes de los términos cruzados se escriben mediante Av∈L². La misma argumentación por bloques identifica el dominio del operador alto H con la intersección del dominio comprimido y el complemento alto. Aplicar Q_high,σ a los aproximantes anteriores demuestra

    span{w_j:j≥0} es un núcleo de operador de H.            (114)

Así se mejora(110) a densidad en norma de grafo para combinaciones finitas de semillas, sin afirmar tasas ni buena condición numérica. Descartar dependencias exactas mediante(108) no cambia su span.

Para r>1/γ fijo, la métrica usada por el corrector satisface

    (r−1/γ)||Hu||²≤g(u,u)≤r||Hu||².                       (115)

Se usa <u,Hu>≤||Hu||²/γ. Como H≥γ, esta métrica equivale a la norma de grafo. Las columnas Z_*=H^(-1)C pertenecen aDom(H), y(114) permite aproximarlas en g por combinaciones de las semillas. La identidad(101)-(102) identifica el óptimo finito como la proyección de Z_* en esa métrica; por tanto

    ||H(Z_opt,m−Z_*)||→0, ||R_m||→0,
    J_opt,m aumenta hacia S_Schur en norma matricial.      (116)

El número de columnas bajas es finito para cadaT, de modo que la convergencia por columnas implica la de los Grams y de las matrices. No se obtiene una tasa uniforme enT. En particular, SI S_Schur>0 en una ventana, existe un paso finito conJ_opt,m>0. Esa premisa sigue siendo el signo por demostrar; (116) NO permite deducirla. Si el límite tiene una dirección negativa, la monotonía no la repara; si es sólo semidefinido, no se garantiza positividad en ningún paso finito. El diseño global sigue pendiente, ahora sin el hueco analítico de densidad del corrector.

La revisión confirmó la cadena(112)-(116). La existencia condicional de un tamaño finito positivo no acredita por sí sola la terminación de una implementación intervalar concreta: también habría que especificar aproximación e integración verificadas de estas fuentes a trozos y refinamiento de precisión. No se ejecutaron nuevos cálculos ni se cambió el estado OPEN del signo global.


## Auditoría del papel de Euler en la completitud

Estado: identidad PROVED y diagnóstico revisados independientemente. Mantener fijos P,C,H,r. Para cualquier núcleo de operador deH, ortogonalizado en g, (105)-(116) o Parseval en g aplicado aZ_*=H^(-1)C dan

    Σ_j b_j*b_j/d_j = g(Z_*,Z_*)
                    =rC*C−C*H^(-1)C.                    (117)

La convergencia es en norma matricial, pues el número de columnas bajas es finito. El lado derecho no depende del núcleo de operador escogido. Por tanto, reemplazar las semillas de Möbius por otro núcleo completo cambia los parciales y su velocidad de convergencia, pero no el aporte total. No se afirma que dicho total permanezca igual al cambiarΛ o un falsificador: esos cambios alteranP,C,H.

Esto localiza un límite concreto de la candidata(106): usar el producto de Euler solamente para acreditar invertibilidad y completitud de las semillas no proporciona el signo. La suma positiva de(117) existe también con bases sin ese dato aritmético; al combinarla conP−rC*C se recupera exactamente el Schur cuyo signo sigue abierto. Por ello la completitud aritmética sola no cumple las cláusulasO3/O4 deOBJECT_SPEC.

No es un NO-GO para todas las semillas de Möbius ni un descarte de su posible eficacia finita. Una identidad adicional sobreP,C,H, o un control aritmético de parciales suficiente para dominarrC*C−P, podría aportar información nueva. Esa pieza no está construida. Se conserva la candidata como herramienta explícita de aproximación con convergencia probada, sin presentarla como mecanismo global de positividad.


## Acción explícita sobre los escalones de la primera semilla

Estado: fórmula PROVED y revisada; implementación comprobada numéricamente, no intervalar. Para f=1_[a,b] extendida por cero, definir I(d)=atanh(exp(−d/2))+atan(exp(−d/2)), d>0. La acción arquimediana exacta, fuera de los dos extremos, es

    Arch f(x)=C0+I(x−a)+I(b−x),       a<x<b,
             =−I(a−x)+I(b−x),         x<a,
             =−I(x−b)+I(x−a),         x>b.                (118)

Dentro del escalón, el término de diferencias se reduce a las dos colas exteriores. Fuera, queda la integral negativa deH0 sobre[a,b]. En ambos casos I(d)=∫_d^∞H0(u)du da(118). Las singularidades en los extremos son logarítmicas,L²; los valores puntuales no intervienen. Para x∈(-T,T), la acción física completa añade exactamente

    −Σ_(log n<2T)Λ(n)/√n
           [1_[a,b](x+log n)+1_[a,b](x−log n)].           (119)

La combinación lineal de(118)-(119) evalúa A R_Tp_0, pues R_Tp_0 es una suma finita de escalones. La reflexión de paridad conmuta conA. En cambio, para aplicar la proyección alta de(107) hay que conservar A(P_hg) y A(P_Eg):

    H w_0=Q_high A[g−P_hg−P_Eg], g=Π_σR_Tp_0.            (120)

No se reemplaza esta expresión por Q_high Ag, que omitiría los acoplamientos. Esos términos y el Gram de la fuente son necesarios antes de afirmar que se calculó b_0 o su ganancia.

step_source.py implementa(118)-(119) enmpmath y rechaza evaluar el arquimediano exactamente en los extremos singulares. Una comparación independiente por integración directa deH0 en cuatro puntos interiores/exteriores, más reflexión, pasó a70dígitos con discrepancia máxima<3.7e−71; step_source_check.json registra PASS_NUMERICAL_FORMULA_CHECK. Es un control de implementación sin encerramiento intervalar, no una prueba numérica de signo. La fórmula matemática fue revisada independientemente. Todavía no se evaluó la fuente proyectada completa(120) ni la ganancia del candidato.


## Acción sobre las correcciones hiperbólicas de momentos

Estado: fórmula PROVED/revisada; control de implementación NUMÉRICO. Para f_a(x)=exp(ax)1_(-T,T),a=±1/2, y −T<x<T, separar los incrementos a izquierda y derecha da

    Arch f_a(x)=exp(ax)[C0+I(x+T)+I(T−x)
                         +F_(-a)(x+T)+F_a(T−x)],
    F_a(d)=∫_0^d H0(u)(1−exp(au))du.                      (121)

El integrando tiene valor removible−a/2 en cero. Paraq=exp(−d/2), escribir

    A_+(q)=2log q−log(1+q)−(1/2)log(1+q²)−atan q,
    A_−(q)=−log(1+q)+(1/2)log(1+q²)−atan q,
    F_(±1/2)(d)=A_±(q)−A_±(1).                           (122)

La sustitución t=exp(−u/2) reduce los integrandos a2/[t(1+t)(1+t²)] y−2/[(1+t)(1+t²)], respectivamente. Las primitivas anteriores verifican esas derivadas. Sus constantes son A_+(1)=−(3/2)log2−π/4 yA_−(1)=−(1/2)log2−π/4. En particular F_+(0)=F_−(0)=0, F_+(d)≤0 yF_−(d)≥0.

La acción completa resta los contactos de(119) con f_a extendida por cero. Las combinaciones (f_++f_−)/2 y(f_+−f_−)/2 dan cosh ysinh; no se omiten los factores de normalización de la inmersión cuando se pasa al semintervalo. Con(118),(121) y la acción polinómica ya disponible se dispone de las piezas necesarias para escribir la fuente de(120), conservando todas las correcciones. Su ensamblado y Gram todavía están pendientes.

step_source.py incorpora exponential_increment, arch_exponential yphysical_exponential. Se comprobaron seis integrales independientes a70dígitos, los signos deF yla reflexión: error máximo<4.6e−71, exponential_source_check.json PASS_NUMERICAL_FORMULA_CHECK. No es encerramiento intervalar ni evaluación de la ganancia del corrector.


## Coeficientes de la primera semilla proyectada

Estado: identidad de proyección y normalización revisadas; coeficientes calculados NUMÉRICAMENTE a100dígitos, sin encerramiento. En el semintervalo isométrico, la primera semilla sin proyectar es

    g(x)=Σ_(n<exp(2T)) μ(n)/(2√(Tn))
       [1_[max(0,log n−T),T](x)
           +σ1_[0,min(T,T−log n)](x)],                    (123)

omitiendo intervalos vacíos. El término n=1 vale1/√T paraσ=+1 y cero paraσ=−1. Sean v_k=<p_k,g>, α_k=<p_k,h>, h_low=Σ_(0≤k≤N)α_kp_k. Entonces

    t=Σ_(0≤k≤N)α_kv_k/Σ_(0≤k≤N)α_k²,
    c_k=−v_k+tα_k, κ_h=−<h,g>/||h||²,
    w_0=g+Σ_(0≤k≤N)c_kp_k+κ_h h.                         (124)

La fórmula usa Q_high=I−P_V+P_hlow−P_h; no invierte otro sistema mal condicionado. Los v_k se integran mediante la primitiva exacta de Legendre, y<h,g> por primitivas de cosh/sinh sobre cada escalón. Para cada término c1_[a,b] de(123), la fuente de paridad es c[A1_[a,b](x)+σA1_[−b,−a](x)], sin otro factor√2. AñadirΣc_kA_σp_k+κ_hA_σh y proyectar la salida daHw_0.

projected_mobius_seed.py guarda las dos representaciones en projected_mobius_seed.json paraT4/5,N95. Los residuos numéricos del momento y de las95ortogonalidades bajas son<2.7e−102. Se comprobaron además los cuatro primeros momentosv_k mediante cuadratura independiente por piezas, con discrepancia<9e−103. Los coeficientesκ_h son aproximadamente−0.4538580045 enpar y2.4536035273 enimpar. Estos residuos son controles de implementación, no pruebas por tolerancia: la proyección exacta es(124), y los valoresguardados no son intervalos. Falta ensamblar la acción completa y medir la ganancia; no se ha certificado signo nuevo.


## Primer diagnóstico de fuente completa y ganancia

Estado: NUMÉRICO, sin intervalos ni certificado de signo. evaluate_mobius_gain.py ensambla la fuente de(124), incluidas las acciones polinómica e hiperbólica, y aplica Q_high también en la salida usando momentos integrados deh, sin truncarh por su expansión. Usa las16direcciones altas previas, N95 y r=16 en la métrica de(103). La partición contiene seis piezas con todas las singularidades y fronteras de los contactos de los escalones. La acción polinómica reutiliza operator_basis con ordeninterior160.

Se calcularon C=Q_high AE, Y=Q_high AW,y=Q_high Aw_0 por cuadratura, K=W*Y simetrizado,G=16Y*Y−K y a=G^(-1)(16Y*y−W*y). Conq=w_0−Wa,Hq=y−Ya, se evaluaron d=16||Hq||²−<q,Hq>,b=16(Hq)*C−q*C ytraza de ganancia||b||²/d. No se supone que un residuo flotante sea una cota rigurosa.

| Paridad | Orden por pieza | ||Hw_0||² | d | ||b|| | traza de ganancia |
|---|---:|---:|---:|---:|---:|
| par |96|0.00672301415|0.0982195543|0.645151965|4.23765981|
| par |128|0.00673407369|0.0983963592|0.645526034|4.23495203|
| impar |96|0.00685998560|0.0973321791|0.653330066|4.38539628|
| impar |128|0.00687106697|0.0975084935|0.653543089|4.38032169|

La ganancia cambia aproximadamente0.064% enpar y0.116% enimpar entre estos órdenes; no se declara convergida ni encerrada. Las ortogonalidades bajas deentrada/salida son menores que1.4e−14, y los momentos menores que2e−16. mobius_gain_diagnostic.json conserva todos los valores y tamaños. La ganancia es de rango a lo sumo uno enCOORDENADASbajas, no una mejora deλ_A ni un autovalorL².

El ensayo da evidencia numérica de una fila b no nula para la primera semilla, cuyo denominador exacto positivo ya estaba probado por(111). No acredita b≠0 mediante intervalos, ni que la ganancia beneficie la dirección decisiva o vuelva positivo el criterio escalar completo. Ese criterio no se evaluó aquí. La selección deMöbius sigue sin una comparación aritmética global; no se interpreta esta traza como tal.


## Ganancia direccional frente al criterio escalar completo

Estado: diagnóstico NUMÉRICO, código completo auditado independientemente; no certificado de inercia ni signo. Se amplió evaluate_mobius_gain.py para formar el óptimo escalar anterior J_before=P−16C*C+B*G^(-1)B, B=16Y*C−W*C, y J_after=J_before+b*b/d. Se guardan ambas matrices y la ganancia en mobius_directional_{parity}_{order}.npz; mobius_directional_diagnostic.json preserva los controles. El primer reporte de traza no fue sobrescrito.

| Paridad | Orden | mínimo antes | mínimo después | ganancia en el vector mínimo anterior |
|---|---:|---:|---:|---:|
| par |96|−7.7778123|−7.7213228|0.2152956|
| par |128|−8.2139169|−8.1227793|0.2354798|
| impar |96|−7.7996978|−7.7538301|0.1536406|
| impar |128|−8.2248839|−8.1625782|0.1624179|

En los cuatro cálculos, el número flotante de autovalores negativos pasa de23 a22. No es un índice certificado. La ganancia sobre el vector mínimo anterior no coincide con el cambio del mínimo, pues el vector puede cambiar al añadir la matriz de rango uno.

El mínimo cambia alrededor de0.44 al variar la cuadratura; estos valores NO se declaran convergidos. La ortogonalidad métrica g(W,q) muestra residuos entre4.8e−9 y7.1e−8, mayores que los residuos de momentos: el ensamblado de acciones y la simetrización deK siguen sujetos a errores de cuadratura. No se deduce negatividad de la formaA ni siquiera una cota rigurosa del criterioJ de estas matrices flotantes.

Conclusión limitada: el ensayo detecta aporte en una dirección inferior, pero no observa que una sola semilla cierre el criterio escalar. La traza positiva del ensayo previo no justificaba esa conclusión. Sigue pendiente una estimación certificada de la ganancia y, sobre todo, una regla aritmética de compensación suficiente para todoT. No se abre una campaña de aumento mecánico de semillas a partir de estos datos.

La auditoría del código no encontró errores de normalización, signo ni términos omitidos. Identificó que usar K simetrizado enG pero W*Y sin simetrizar en el control contribuye al defecto métrico; ambas coinciden exactamente, no en la cuadratura. Confirmó que el incremento flotante positivo por construcción no certifica su valor exacto ni el signo deJ oA.


## Optimización con pesos modales y refinamiento monótono

Estado: PROVED como desarrollo auxiliar, revisado independientemente. Antecedentes: control modal(57)-(59), optimización escalar(100)-(102) y diagnóstico reciente desfavorable del criterio escalar. El cambio consiste en conservar pesos por modo dentro de la optimización, no en aumentar mecánicamente el número de semillas. No aporta una identidad aritmética de signo nueva.

Fijar T, el portador bajo y su complemento alto, con las bases y números d_k>0 de(92), k>N. Poner c=1+eta_bar y distinguir las columnas modales w_k de las direcciones elegidas para el corrector. La desigualdad dual da

    H^(-1)≤V:=Σ_(k>N)d_k^(-1)w_kw_k*.

Para L≥N+1, definir el operador explícito de rango finito más identidad

    U_L=c/d_(L+1) I
          +Σ_(N<k≤L)(1/d_k−1/d_(L+1))w_kw_k*.             (125)

El control W∞W∞*≤cI y el crecimiento de d_k implican

    V≤U_L,
    U_L−U_(L+1)=(1/d_(L+1)−1/d_(L+2))
                    [cI−Σ_(N<k≤L+1)w_kw_k*]≥0,
    ||U_L−V||≤c/d_(L+1)→0.                              (126)

Para la primera desigualdad, separar la cola deV y acotarla por1/d_(L+1) veces la suma de sus proyectores de rango uno. Para la cota de norma, U_L−V es positivo y está acotado por(c/d_(L+1))I. No se supone que w_k sean ortonormales.

Elegir ε>0 fijo yV_L=U_L+εI. Sea F una familia finita independiente de direcciones correctoras enDom(H), Y=HF,K=F*HF,D=F*C. Entonces

    G_L=Y*V_LY−K≥εY*Y>0,
    B_L=Y*V_LC−D,
    X_opt=G_L^(-1)B_L,
    J_opt=P−C*V_LC+B_L*G_L^(-1)B_L.                      (127)

La expansión deJ_L(X)=S_X−R*V_LR reproduce la completación de cuadrados de(101). En particular J_opt−J_L(X)=(X−X_opt)*G_L(X−X_opt)≥0. No se aplica H² a las columnas: sólo se forman Grams deY y sus momentos modales. El resto exacto es

    S_Schur−J_L(X)=R*(V_L−H^(-1))R≥0.                    (128)

Con el portador bajo y ε fijos, ampliar el espacio corrector no empeora el óptimo. AumentarL tampoco lo empeora, pues V_L disminuye y por tanto J_L(X) aumenta para cada corrector fijo. La regularizaciónε no es gratis: se incluye exactamente comoεR*R y no se omite en un certificado.

La métrica g_L(u,u)=<Hu,V_LHu>−<u,Hu> satisface ε||Hu||²≤g_L(u,u)≤||V_L||||Hu||². Por el núcleo de operador probado en(114), agotar las direcciones correctoras haceJ_opt→S_Schur paraL fijo; también vale al aumentarL conjuntamente, por comparación monótona con cualquierL fijo. AumentarL SOLAMENTE con un espacio corrector fijo no demuestra esa convergencia: V+εI puede superar estrictamenteH^(-1).

Esta construcción evita sustituir toda la distribución modal por la penalización escalarr=16 del ensayo anterior. No se afirma que supere numéricamente(69) con cualquierε ni que el nuevo criterio sea positivo sin evaluarlo. Queda pendiente la compensación aritmética global. No se lanzó un nuevo cómputo ni se alteraron los certificados locales.


## Diagnóstico de la optimización modal con la misma semilla

Estado: NUMÉRICO, código auditado independientemente, sin encerramientos. evaluate_mobius_gain.py --metric modal conserva la semilla, espacio corrector y órdenes96/128, pero usa(125) conL111 yε=1e−12. Incluye todos los pesos individuales1/d_k−1/d_112, no una única cota escalar. La matrizG calculada tiene mínimo≈43.79 enpar y44.95 enimpar, con condición≈4.8; se detendría el solve si ese mínimo flotante no fuese positivo.

| Paridad | Orden | mínimo antes | mínimo después | ganancia sobre el mínimo anterior |
|---|---:|---:|---:|---:|
| par |96|−1.76608e−10|−1.76444e−10|2.46576e−13|
| par |128|−1.36001e−11|−1.33763e−11|3.37375e−13|
| impar |96|1.05704e−9|1.09263e−9|5.30744e−11|
| impar |128|1.05693e−9|1.09256e−9|5.31591e−11|

La traza de la ganancia pasa de0.902918 a0.902353 enpar yde0.933455 a0.932368 enimpar. Se conservan reportes y matrices en mobius_modal_directional_diagnostic.json y losNPZmodales, sin sobrescribir el ensayo escalar.

La mejora diagnóstica respecto del criterio escalar es clara, pero el fondo par no está resuelto por esta cuadratura: cambia a una escala mayor que el fondo positivo local previamente certificado. Tampoco los mínimos impares positivos son certificados. La exactitud del signo local sigue descansando en(96), no en estas cifras. No se obtiene una cota mejorada deλ_A ni una ventana nueva.

La auditoría confirmó c_T, índices96..112, todos los productos de la métrica y nombres separados. El diagnóstico flotante no representa eta_bar=1e−370; una versión intervalar debe restituir c=1+eta_bar y su contribución a d_k. El testG_min>0 es sólo una salvaguarda numérica. No se amplió mecánicamente la campaña de tamaños o cuadraturas. Sigue abierta la prueba aritmética global de compensación.


## Prueba algebraica frente al reescalado1.1Λ

Estado: PROVED y revisado como auditoría de alcance, no como nuevo mecanismo de signo. SustituirΛ porcΛ da E_c=cE yR_c=exp(−cE), con inversaexp(cE). La expansión finita del producto formal de Euler produce

    R_c=Σ_(n<exp(2T)) d_c(n)/√n U_log n,
    d_c(n)=∏_(p^k||n)(−1)^k binom(c,k).                   (129)

Para T=4/5 sólo entran1,2,3,4, y

    R_c=I−c/√2 U_log2−c/√3 U_log3
                       +c(c−1)/4 U_log4.                (130)

En c=1 el último coeficiente es cero; en c=11/10 vale11/400. Se rompe la identificación conμ, pero no la invertibilidad ni la continuidad en norma de grafo: las exponenciales siguen siendo polinomios finitos de operadores de desplazamiento por nilpotencia. Por tanto la propiedad de núcleo de operador de las semillas transportadas sobrevive al reescalado.

Para la forma modificada deben recalcularse el corteN, la coercividadγ y los pesosd_k. En particular NO se trasladan los valoresN95 yγ1/8 del certificado real a1.1Λ. Una vez construido un complemento coercivo apropiado, los lemas de optimización y convergencia conservan su prueba; no usan c=1 para el signo de sus incrementos.

Conclusión de la auditoría: el cambio de coeficientes en(130) no es la ruptura de positividad exigida porO4 deOBJECT_SPEC. Los mecanismos positivos auxiliares sobreviven; lo que aún falta es probar la dominación del término inicial de(105), o su versión modal, mediante una identidad que use específicamente los datos verdaderos. No se afirma invariancia del Schur al cambiarc, ni se descartan posibles usos adicionales de la identidad aritmética. Esta prueba no modifica el certificado local deΛ ni proporciona signo global.


## Identidad exacta de candidato sin inverso del operador alto

Estado: PROVED como identidad y positividad del resto alto, revisado independientemente. Antecedentes: completación(84) usaH^(-1)C; criterio modal(125)-(128) utiliza un mayoranteV=V_L explícito. No es una prueba del signo de la matriz baja.

Fijar V=U_L+εI, ε>0, y un corrector finitoZ. ParaF=Ex+v en el dominio primitivo de forma, poner

    w=v+Zx, R=C−HZ, J=S_Z−R*VR,
    mathcal V(F)=V^(1/2)Rx+V^(-1/2)w.

Entonces la identidad exacta sobre TODO ese dominio es

    a_T(F)=||mathcal V(F)||²+x*Jx
                       +h(w)−<w,V^(-1)w>.                (131)

Aquíh es la forma restringida al complemento alto. La expansión del cuadrado aporta R*VR,2Re<w,Rx> y<w,V^(-1)w>; los dos términos diagonales añadidos se cancelan exactamente conJ y el último término. No hay una desigualdad ni una pérdida de margen en esta identidad.

Por H^(-1)≤V, el orden inverso da V^(-1)≤H en sentido de formas, luego

    h(w)−<w,V^(-1)w>≥0.                                  (132)

El dominio de h se conserva al sumarZx, cuyas columnas pertenecen aDom(H). V es acotado y uniformemente positivo, de modo que ambas raíces son acotadas y no restringen el dominio. La justificación de(132) usa el mayorante modal ya probado; el operador mathcal V no exige calcularH^(-1).

En efecto,V=αI+Σβ_kw_kw_k*,α>0,β_k≥0. EnS=span{w_k:N<k≤L}, una ortonormalización finita y la matriz positiva deV dan sus raíces; enS^⊥ son los escalaresα^(±1/2). Todo el operador candidato queda especificado mediante esas operaciones finitas, el correctorZ y su fuenteR.

La obligación que resta es exactamente J≥0. Si se demuestra, (131)-(132) proporcionan el cuadrado y un resto no negativo de la forma buscada. Mientras no se demuestre para todoT, el término x*Jx sigue firmado y la identidad NO satisface por sí solaOBJECT_SPEC. Tampoco se ha construido aquí una ruptura aritmética para los falsificadores. El resultado convierte el certificado en una identidad exacta utilizable; no cambia el estado globalOPEN ni la ventana local ya acreditada.

## Realización positiva local de la identidad (131)

Estado: PROVED local, código auditado y replay reproducido independientemente. Es cierre de la construcción anterior, no una ruta global nueva. Fijar T=4/5, L=111 y ε=10^(-20), con los correctores racionales congelados de los certificados (94)-(96). La comparación modal ya probada da U_111≤(1783/500)I+8WW*. Por la transferencia del criterio (69), su matriz certificada M satisface

    J=S_Z−R*(U_111+εI)R ≥ M−εR*R
                            ≥ (s−ε B_R)I,                 (133)

donde s es la cota inferior COORDENADA de M, no la cota L² de la forma, y

    B_R=[sqrt(tr G_V)+10^(-35)
                sqrt(27/20+(1+10^(-370))||X||_F²)]².

La cota procede de la norma de la fuente aproximada, de la contracción por la proyección alta y del error de operador; no se supone pequeño el residuo exacto. certify_regularized_identity.py reproduce ambas congruencias con Arb a 500 cifras, verifica las huellas y descuenta ε B_R. Resultado en regularized_identity_T4_5.json:

| Sector | Cota superior conservadora de B_R | Cota inferior de J en coordenadas |
|---|---:|---:|
| par | 1260 | 4.79541688e−12 |
| impar | 1297 | 1.05649759e−9 |

En consecuencia, para estos datos concretos TODOS los términos del lado derecho de (131) son no negativos sobre el portador completo de cada paridad. El término finito puede escribirse ||J^(1/2)x||², con J definida por las fuentes exactas, no por sus aproximaciones flotantes. La suma ortogonal de paridades da la identidad local sobre P_(4/5).

Alcance: la verificación reutiliza las fuentes y sus cotas ya certificadas; no es una reintegración independiente. No amplía la ventana conocida ni mejora la cota (96). Sí elimina el pendiente de que la regularización necesaria para definir V^(-1/2) pudiera consumir el margen local. Para todo T permanece OPEN construir correctores y una dominación aritmética S_Z≥R*V R; ni (133) ni la convergencia de correctores prueban esa dominación global.

## Interpolación obligatoria si el fondo es exactamente nulo

Estado: PROVED como corolario de diseño, revisado independientemente. Antecedentes: (116) advierte que la convergencia no garantiza un certificado finito semidefinido; (128) ya da la identidad de pérdida. No es una identidad nueva, una ruta aritmética ni un resultado de signo para T adicional. El añadido precisa qué debe hacer el corrector en el caso límite que el objetivo ≥0 permite.

Escribir S=P−C*H^(-1)C, B=V−H^(-1), con V=U_L+εI y ε>0. Por (128), J=S−R*BR y B≥εI. Entonces

    J≥0 implica S≥0 y R ker(S)={0}.                       (134)

En efecto S=J+R*BR≥0. Si x pertenece a ker(S),
0≤x*Jx=−<Rx,BRx>≤−ε||Rx||²; por tanto Rx=0. En términos del corrector, esta condición es HZx=Cx exactamente en cada dirección nula. No basta un error positivo pequeño.

Recíprocamente, suponiendo S≥0, poner K=ker(S). Como el espacio bajo es finito, S_perp=S|_(K^perp)>0 cuando K^perp no es trivial. Se tiene el criterio exacto

    J≥0 si y sólo si R|_K=0 y
                  R_perp* B R_perp ≤ S_perp.              (135)

La prueba es la descomposición ortogonal K⊕K^perp: la primera condición anula las filas y columnas cruzadas de R*BR, y S ya tiene esas filas y columnas nulas. Si S=0, el criterio se reduce a R=0. Para una cota suficiente en el complemento puede usarse ||B|| ||R_perp||²≤lambda_min(S_perp); ésta es sólo una herramienta condicional, no una cota disponible del margen verdadero.

La hipótesis B≥εI es relevante. Si únicamente B≥0, lo necesario es B^(1/2)R|_K=0, no necesariamente R|_K=0. El presente corolario no obliga a toda posible identidad positiva a usar interpolación: se refiere a la clase regularizada (131).

Consecuencia operativa: un diseño que pretenda cubrir la meta no estricta mediante (131) necesita reproducir exactamente las posibles direcciones nulas, o demostrar que no existen, o cambiar la penalización y justificar su nuevo resto. El corolario no determina K ni prueba que exista una dirección nula para la forma real. No autoriza usar H^(-1)C como constructor calculable ni suponer S≥0 en la prueba global. La dominación aritmética sigue OPEN.

## Monotonía estricta del fondo de la forma completa

Estado: PROVED, argumento y puerta revisados independientemente. Antecedentes: P47 lem:compact prueba compacidad del resolvente y existencia de minimizador para la forma COMPLETA sobre P_T; lem:strict del paper se refiere al fondo arquimediano. Aquí se combina la compacidad con traslaciones interiores que conservan ambos momentos. Es un lema auxiliar, no un mecanismo aritmético de signo ni una afirmación de prioridad.

Para 0<T_1<T_2 se tiene

    lambda_A(T_2)<lambda_A(T_1).                           (136)

Prueba. La extensión por cero conserva norma, momentos y autocorrelación, por lo que da la desigualdad no estricta. Supongamos igualdad con valor lambda. Sea F un minimizador unitario en P_(T_1), que existe por lem:compact. Para |s|<T_2−T_1, definir F_s(t)=F(t−s). Su soporte permanece en I_(T_2) y

    ∫F_s(t)e^(±t/2)dt=e^(±s/2)∫F(t)e^(±t/2)dt=0.

La traslación conserva la norma de forma arquimediana y todas las autocorrelaciones; los contactos adicionales de la ventana mayor son nulos cuando su desplazamiento excede el ancho del soporte. Por tanto F_s es admisible y a_(T_2)(F_s)=lambda. Como a_(T_2)−lambda||·||² es una forma no negativa, la polarización implica que cada F_s pertenece al autoespacio de H_(T_2) con autovalor lambda. Ese autoespacio es finito dimensional por compacidad del resolvente.

Sin embargo, cualesquiera finitísimas traslaciones distintas de F son linealmente independientes. Para verlo, ordenar s_1<…<s_k y poner alpha=inf ess supp F. En el intervalo (alpha+s_1,alpha+s_2) todas las traslaciones salvo la primera son cero casi por doquier; la primera no es idénticamente cero allí, por la definición de alpha. Toda combinación nula obliga a que su primer coeficiente sea cero. Repetir con las traslaciones restantes; para la última usar F≠0. Así se obtienen familias independientes de tamaño arbitrario dentro de un autoespacio finito, contradicción. Esto prueba (136). No se afirma monotonía estricta de cada sector de paridad por este argumento: las traslaciones no conservan paridad.

En particular,

    [lambda_A(T)≥0 para todo T]
        implica [lambda_A(T)>0 para todo T finito].         (137)

Basta elegir T_2>T_1 en (136). Más localmente, no negatividad en T_2 implica positividad estricta en toda ventana menor. Si lambda_A(T_0)=0, entonces lambda_A(T)<0 para todo T>T_0. Estas consecuencias no prueban la premisa global ni dan una cota cuantitativa del margen.

Aplicación al diseño: bajo la meta global, las matrices de Schur de cada ventana finita son definidas positivas; por tanto el caso nulo de (134) no exige un constructor separado dentro de una eventual prueba global. Esto no permite asumir el signo al construir los correctores. La convergencia de (116)/(128) sólo da existencia de un paso finito positivo CONDICIONAL a esa positividad, sin tasa ni mecanismo aritmético. El lema sobrevive a cualquier peine localmente finito con las mismas propiedades de compacidad y traslación; no distingue falsificadores y no satisface por sí solo O3/O4.
