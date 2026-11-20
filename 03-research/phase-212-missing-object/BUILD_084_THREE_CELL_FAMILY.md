# Construcción 084 — Familia primitiva de celdas (1,2,k)

## Cotejo y alcance

Antecedente exacto: matrices de celdas de 212-59 y equivalencia de portadores de 212-75. ROUND_018_A de la fase 211 trata tres celdas de una cola transportada, con otras restricciones y ventana fija. Aquí se estudian tres indicadores en la variable física x, con los dos momentos exactos y un índice k arbitrariamente grande. La puerta de selección y la prueba fueron revisadas independientemente.

Estado: PROVED para esta familia, con prueba analítica de la cola y certificado intervalar del tramo finito. No se afirma una nueva representación de la forma, positividad para todos los triples, ni positividad sobre combinaciones de los tests. La diferencia respecto de los certificados locales es que el índice y la ventana no están acotados. El resultado no cumple por sí solo OBJECT_SPEC: no separa los falsificadores.

La operación de signo es conservar el bloque (1,2), descartar únicamente el cruce favorable (2,k) y acotar el retorno adverso (1,k) por divisibilidad del binomial central. Una cota superior de los pesos no puede sustituirse indiscriminadamente en los cruces favorables.

## Familia y teorema

Sean I_j=[j,j+1), k≥3 entero y

    a=log 2, b=log(3/2), c=log(1+1/k), d=a−b,
    f_k=(b−c)1_(I_1)+(c−a)1_(I_2)+d 1_(I_k).             (1)

Se cumplen exactamente ∫f_k=0 y ∫f_k(x)/x dx=0: la segunda igualdad es
a(b−c)+b(c−a)+c(a−b)=0. Por tanto F_k(t)=e^(t/2)f_k(e^t) tiene ambos momentos primitivos nulos. Su soporte está en [0,log(k+1)]; trasladarlo por −log(k+1)/2 lo sitúa en la ventana T_k=log(k+1)/2. Trasladar conserva norma y forma. Los tests pertenecen al dominio de forma por 212-75.

Para cualquier escalar complejo z y cualquier ventana que contenga el test trasladado,

    a_T(zF_k) ≥ (1/1000)||zF_k||².                         (2)

El enunciado concierne a cada recta generada por F_k. No concierne a la envolvente lineal de todas ellas.

## Matriz exacta

Usar h(m)=(m+2)log(m+2)−2(m+1)log(m+1)+m log m, con 0 log0=0, y C=−γ−log(2π). La matriz de 212-59/75 es M=A−C_comb, donde

    A_ii=C+(i+1)log(i+1)−i log i−h(2i)/2,
    A_ij=−[h(i+j)+h(j−i−1)]/2                 (i<j),
    (C_comb)_ij=Σ_(n i≤j<n(i+1), n≥2) Λ(n)/n (i<j),
    (C_comb)_ii=0.                                        (3)

La energía es α* M α para α=(b−c,c−a,d), en las posiciones (1,2,k). El factor dos de cada cruce está incluido. Como h≥0, Λ≥0, c−a<0 y d>0, el cruce (2,k) es no negativo. El bloque (1,2) vale

    q(c)=M11(b−c)²+M22(a−c)²−2M12(b−c)(a−c),
    M12=A12−(log2)/2.                                    (4)

## Retorno adverso: una cota binomial

El retorno es exactamente

    R_k=(C_comb)_1k=Σ_(k/2<n≤k)Λ(n)/n.

Para k=2m, cada potencia prima q en (m,2m] contribuye su logaritmo primo a la valuación del binomial (2m choose m). Las restantes contribuciones a esa valuación son no negativas. Para k=2m+1 sucede lo mismo en (m+1,2m+1]; hay que añadir por separado la posible potencia prima m+1, cuya contribución no excede log k. En ambos casos,

    Σ_(k/2<n≤k) Λ(n) ≤ log(k choose floor(k/2))+log k
                       ≤ k log2+log k.

Como 1/n≤2/k en ese intervalo,

    R_k ≤ 2log2+2log k/k.                                 (5)

No se usó una estimación asintótica de primos ni se omitió el caso impar.

## Cola uniforme k≥256

La identidad h(m)=∫_0^1∫_0^1(m+s+t)^(-1) ds dt da h(m)≤1/m para m>0. Además
(k+1)log(k+1)−k log k=∫_k^(k+1)(log x+1)dx≥log k+1. Por consiguiente,

    A_kk≥log k+C,
    |A_1k|≤[1/(k+1)+1/(k−2)]/2.                          (6)

Para k≥256, 0<c<1/256, b−c≤b y log k/k es decreciente. La aritmética de intervalos sobre TODO c∈[0,1/256] da q(c)>0.15. Conservando el bloque (1,2) y omitiendo sólo el cruce favorable se obtiene

    α*Mα ≥ q(c)+d²(log k+C)
              −2bd(2log2+2log k/k+|A_1k|)
           > 0.08.                                       (7)

El certificado evalúa el segundo miembro con k=256 en todos los términos que empeoran la cota. Su extremo inferior encerrado supera 0.08173135. Así (7) es una cota para infinitos k, no una extrapolación numérica.

## Tramo finito y normalización

build_084_data/certify_three_cells.py calcula las entradas (3) con Arb a 100 cifras y genera Λ exactamente sobre las potencias primas. Verifica α*Mα>1/1000 para cada entero 3≤k≤255. Son 253 verificaciones de fórmulas cerradas; no hay cuadratura ni autovectores aproximados. El archivo three_cell_family_certificate.json conserva cada encerramiento y las constantes de cola. El cálculo fue reproducido independientemente.

Finalmente,

    ||F_k||²=||f_k||²=(b−c)²+(a−c)²+d²
                       ≤b²+a²+d²<1.                      (8)

La última desigualdad se verifica con las mismas constantes intervalares. (7), el tramo finito y (8) prueban (2), también para múltiplos complejos.

## Control de alcance y siguiente problema

La variante del script --scale 11/10 sustituye cada Λ(n) por (11/10)Λ(n), incluido M12, y multiplica la cota (5) por 11/10. También pasa las 253 verificaciones y la cola, cuyo extremo inferior supera 0.06756358. Este control confirma que la familia NO separa ese falsificador; los archivos de ambas ejecuciones están separados. No es una prueba de signo global para ninguno de los dos pesos.

Para pasar de esta familia a un subespacio hace falta controlar a(F_j,F_k), j≠k. La primera parte, (1)-(8), no controla esos emparejamientos; la extensión siguiente trata los cruces G_3k. Para esta afirmación de base se usan los F_k sin centrar individualmente, o todos trasladados por la misma cantidad a una ventana común. De hecho, los F_k forman la base de circuitos con anclas 1 y 2 del subespacio de celdas con ambos momentos nulos: el coeficiente en la celda k de F_k es la constante no nula d. Eliminar las coordenadas k≥3 mediante F_k/d deja un vector en las celdas 1 y 2; sus dos momentos obligan a que sea cero porque a≠b. La independencia se lee en las coordenadas k≥3. La positividad individual sólo firma la diagonal en esa base; no firma su matriz completa. El siguiente problema concreto es una regla para sus cruces que conserve las cancelaciones aritméticas, antes de ampliar certificados o índices.

## Extensión: un cruce completo, uniforme en el índice móvil

Estado: PROVED para cada plano span(F_3,F_k), k≥4, con prueba analítica de cola y certificado intervalar finito reproducido independientemente. Los F_j usan las coordenadas comunes anteriores. No es una prueba para subespacios con varios índices móviles. La operación adicional es controlar el complemento de Schur completo, incluidos los cruces, y no sólo aumentar una tabla de diagonales.

Escribir G_jk=a(F_j,F_k). Para u=(b−c_3,c_3−a,d), c_3=log(4/3), poner

    t_i=Σ_(r=1)^3 u_r M_ri, i=1,2,
    s(c)=(b−c)t_1+(c−a)t_2.

La congruencia directa, sin proyectar oblicuamente el peine, da

    G_3k=s(c)+d Σ_(r=1)^3 u_r M_rk,
    G_kk=q(c)+d²M_kk+2d[(b−c)M_1k+(c−a)M_2k].           (9)

Aquí G_33>0.08381066 está certificado exactamente como en la primera familia. La condición suficiente y necesaria para el plano es

    S_k=G_kk−|G_3k|²/G_33>0.                             (10)

### Cotas de los retornos 2 y 3

Para i=2,3, A=floor(k/(i+1)), B=floor(k/i), k≥12, se tiene B≤2A. Cada potencia prima q con A<q≤B contribuye una unidad a la correspondiente valuación de binom(B,A): q>A y q>B−A. Las demás contribuciones son no negativas. Por tanto

    C_ik ≤ log binom(B,A)/(A+1)
          ≤ B log2/(A+1) < ((i+1)/i)log2.                (11)

Se conserva (5) para i=1. Asimismo, |A_ik|≤[1/(k+i)+1/(k−i−1)]/2 cuando k>i+1.

### Un mayorante de todo el cruce

Fijar N=16384 y definir

    J_i=[1/(N+i)+1/(N−i−1)]/2,
    P_+=(−u_2)[(3/2)log2+J_2],
    P_−=u_1[2log2+2logN/N+J_1]+u_3[(4/3)log2+J_3].

Los signos de u son (+,−,+), mientras M_rk≤0. Para todo k≥N,

    s(c)−dP_− ≤ G_3k ≤ s(c)+dP_+,
    0<c≤1/N.                                             (12)

Evaluar s en todo ese intervalo y tomar el máximo de los valores absolutos de ambos extremos da |G_3k|≤B_*=0.21007079018... (con encerramiento en el certificado). Se incluye el bloque de anclas, los tres retornos y toda la parte arquimediana. No se reemplaza una suma firmada por una suma de valores absolutos de sus seis piezas.

Para la diagonal se conserva la unidad positiva omitida en (6):

    A_kk≥log k+C+1−1/(4k).

Con q_box el intervalo que encierra q(c) para c∈[0,1/N],

    S_k ≥ q_box+d²(logN+C+1−1/(4N))
           −2bd[2log2+2logN/N+J_1]−B_*²/G_33
         >0.00270647>0.002                 (k≥N).         (13)

El uso de N es válido porque log k crece, log k/k decrece, y los J_i y 1/k decrecen. Todos los extremos se redondean hacia fuera.

### Tramo finito e identidad de cuadrados

certify_anchored_planes.py verifica los 16380 enteros 4≤k<16384 mediante (9), usando prefijos intervalares exactos Σ_(n≤x)Λ(n)/n para cada retorno. Obtiene S_k>1/1000; el menor extremo inferior es 0.04520896477..., en k=5. No hay cuadratura ni un solve flotante. Guarda anchored_planes_certificate.json. La prueba de signo de cada plano se expresa como

    a(zF_3+wF_k)=G_33|z+(G_3k/G_33)w|²+S_k|w|²,          (14)

con ambos coeficientes positivos para todo k≥4, y z,w complejos. Esto sí controla el cruce de los dos generadores.

### Cota en la norma original

Los certificados también verifican G_33>0.08 y |G_3k|<1/4 en el tramo finito y la cola. Por (8), ambas normas de los generadores son menores que uno. Con r=G_3k/G_33 y zeta=z+rw, |r|<25/8 y

    ||zF_3+wF_k||²≤2(|z|²+|w|²)
                      ≤4|zeta|²+(657/16)|w|².

Comparando con (14), G_33>0.08 y S_k>0.001 dan

    a(zF_3+wF_k) ≥ (1/50000)||zF_3+wF_k||².              (15)

El uso del Gram de norma queda sustituido aquí por una desigualdad de norma explícita; no se confunden los pivotes coordenados con autovalores L². El límite sigue siendo una familia de planos: faltan los cruces entre dos índices móviles y su efecto conjunto en dimensiones arbitrarias.


### Control escalado de la familia de planos

La variante con (11/10)Λ también certifica (15), recalculando el bloque fijo y todos los retornos. La cota suficiente de cola no pasó con cortes 16384 y 32768; los archivos UNRESOLVED_TAIL_MAJORANT registran sólo esa insuficiencia, no tests negativos. Con corte 65536, la misma desigualdad analítica da Schur>0.03033912. El tramo de 65532 índices restantes pasa con Schur>0.001 (menor extremo>0.04817247, en k=5). G_33>0.08229, el mayorante del cruce de cola es <0.222407 y las cotas de norma siguen siendo válidas.

El código de la variante y su reporte fueron auditados; la ejecución escalada no fue repetida independientemente. El certificado físico original sí fue reproducido. Los archivos escalados están separados. Esto prueba que la positividad de todos estos planos no basta para distinguir el falsificador: no es O4, y no permite inferir positividad sobre su envolvente lineal.

## Control conjunto: una combinación negativa pese a todos los planos positivos

Estado: PROVED mediante un test explícito con certificado intervalar, reproducido independientemente sin autovectores. Se comprueba en el propio falsificador el límite de (2) y (15), en lugar de inferir una obstrucción universal a partir de un ejemplo matricial abstracto.

Se tomó un único bloque N=256 y el peso (11/10)Λ. Un autovector flotante sobre el núcleo de los DOS momentos propuso las coordenadas; ese diagnóstico no interviene en la prueba. Se congelaron los 254 coeficientes de circuitos como

    gamma_k=m_k/2^40, m_k entero, 3≤k≤256,
    F=Σ_(k=3)^256 gamma_k F_k.                            (16)

La lista íntegra de enteros figura en build_084_data/joint_scaled_witness_256.json. La parametrización (16) garantiza los dos momentos exactamente. joint_falsifier_witness.py --verify reconstruye la forma completa con Arb a 100 cifras desde esos enteros, sin ejecutar el solver. Todos los F_k se trasladan por la misma cantidad; basta la ventana T=log(257)/2.

Para el mismo F se certifica

    a_(11Λ/10)(F)/||F||² < −0.09317,
    a_Λ(F)/||F||² > 0.03674.                             (17)

La norma cuadrada encerrada es aproximadamente 1.00000000000040757. El signo no depende del redondeo del autovector: la evaluación intervalar es sobre el test congelado. (17) sólo es un test positivo para Λ, no una cota de todo el bloque para ese peso.

### Localización colectiva del defecto

Sea E_diag=Σ gamma_k²G_kk y E_cross=a(F)−E_diag. El certificado conserva todos los términos y obtiene:

| Peso | E_diag | E_cross | a(F) |
|---|---:|---:|---:|
| Λ | 5.27338761328… | −5.23664241463… | 0.03674519865… |
| (11/10)Λ | 5.50079852782… | −5.59397465926… | −0.09317613144… |

Los valores son encerramientos del reporte, resumidos aquí; el signo no procede de restar decimales redondeados de esta tabla. No se identifica un único par responsable de la diferencia: E_cross es la suma conjunta.

Eliminar exactamente el generador F_3 da

    a(F)=|a(F_3,F)|²/G_33 + R(F),
    R(F)=Σ_(j,k≥4) gamma_j gamma_k
                   [G_jk−G_j3 G_3k/G_33].                (18)

La primera contribución es positiva: aproximadamente 1.03656946e−6 para Λ y 1.54367925e−5 para el peso escalado. El resto vale respectivamente más de 0.03674416 y menos de −0.09319156. Así, la negatividad escalada permanece íntegramente en el acoplamiento de los índices móviles después de extraer el cuadrado ya construido.

### Decisión para el siguiente diseño

El peso (11/10)Λ satisface TODOS los planos de (15) y viola la positividad de una combinación de ellos. Por tanto, no se puede continuar la prueba global simplemente acumulando esos controles de planos. El paso siguiente debe actuar sobre los emparejamientos colectivos del resto de (18), con una ley que use los datos aritméticos verdaderos. (18) es la identidad de Schur ya conocida, ahora acompañada por un control que muestra dónde falla la extensión; no se presenta como nueva equivalencia ni como mecanismo de signo. No se modificó ningún paper ni se declaró una ventana nueva de positividad sobre el portador completo.
