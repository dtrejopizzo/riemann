# POWER_CONFLUENT_BRIDGE_014 — Una sola tasa confluente basta, en norma fuerte

Estado: PROVED. Nueva precisión del puente: no se usa sólo densidad L². Papers intactos.

## 1. Antecedentes y diferencia

Consultados las reglas del proyecto, índice/grid/crucigrama según las auditorías previas; POWER_BRIDGE_002, POWER_PACKET_SCOPE_AUDIT_009, POWER_COMMON_TRANSFER_010 y certificados confluentes004–013. El puente002 demostraba suficiencia de una escalera fija de tasas distintas32+k mediante una norma fraccionaria ponderada. La diferencia aquí es probar densidad fuerte de TODOS los grados con UNA MISMA tasa u fija. No se atribuye signo a esa densidad: la positividad de todos los bloques sigue siendo una obligación aparte.

## 2. Lema elemental: exponenciales por polinomios densas en H¹ de la semirrecta

Para cualquier a>0,

    span{y^k exp(-ay): k=0,1,...}

es denso en H¹(0,infinito), sin condición de valor en0.

Prueba. Basta mostrar que su ortogonal para el producto H¹ es cero. Sea h en ese ortogonal; complejificar si hace falta. Defina para Re z>0 la función analítica bilineal

    J(z)=integral_0^infinito [h(y)e^(-zy)-z h'(y)e^(-zy)]dy.

Todas las derivadas respecto de z convergen localmente por Cauchy--Schwarz y el decaimiento exponencial. La ortogonalidad a y^k e^(-ay) es exactamente J^(k)(a)=0 para todo k, pues derivar también el segundo término reproduce la derivada temporal del test. Por analiticidad, J es idénticamente cero en el semiplano conexo Re z>0.

Escriba H(z)=integral h(y)e^(-zy)dy. Integrar h' por partes da

    integral h'(y)e^(-zy)dy=-h(0)+zH(z),
    J(z)=(1-z²)H(z)+z h(0).

La integración es legítima para H¹: tiene traza en0, y el extremo en infinito se anula contra e^(-zy). Evaluar en z1, donde H es analítica, da h(0)=0. Así (1-z²)H(z)=0 y H es cero en todo Re z>0. La unicidad se puede verificar tomando cualquier vertical Re z=c>0: es la transformada Fourier de la función integrable e^(-cy)h(y) extendida por cero. Por tanto h=0. El teorema de proyección en Hilbert demuestra la densidad anunciada. No se impone una condición de Robin al cierre: el término h(0) fue precisamente necesario para descartarla.

## 3. Norma ponderada que controla toda la forma

Fije u>1/2 y elija eta con1/2<eta<u. Ponga

    H_eta={f: exp(eta y)f(y) pertenece a H¹(0,infinito)},
    ||f||_eta=||exp(eta y)f||H¹.

Multiplicar por exp(eta y) identifica los polinomios por exp(-uy) con los polinomios por exp(-(u-eta)y). El lema§2 se aplica porque u-eta>0. Así

    union_N span{y^k exp(-uy):0<=k<N}

es densa en H_eta.

La forma completa W de la extensión por cero es continua en H_eta, por las estimaciones ya auditadas y que se enumeran para fijar su topología:

* La extensión por cero H¹(0,infinito)->H^s(R) es continua para0<s<1/2, sin exigir f(0)=0. El multiplicador m tiene crecimiento logarítmico y su forma queda controlada por esa norma.
* Con el peso e^(eta y), las correlaciones bilineales desplazadas se acotan por e^(-eta t) veces las dos normas ponderadasL². La suma2sum Lambda(q)q^(-eta-1/2) converge porque eta>1/2, y controla TODO el peine y sus diferencias.
* Ambos momentos polares son continuos por Cauchy--Schwarz, pues e^((1/2-eta)y) es integrable al cuadrado.

Estas cotas son bilineales y prueban continuidad real o Hermitiana de W, no sólo finitud sobre cada miembro de una sucesión. La densidad conseguida es por tanto suficientemente fuerte para pasar una desigualdad de signo al límite.

## 4. Consecuencia suficiente exacta

Si para una SOLA tasa u>1/2 todos los bloques finitos Laguerre

    V_N(u)=span{exp(-uy)L_j(2uy):0<=j<N}

son no negativos para W, entonces W>=0 en todo H_eta por densidad y continuidad. Para un test suave compacto arbitrario en R, trasládelo a soporte dentro de(0,infinito). El trasladado pertenece a H_eta y W es invariante por traslación, incluso en su polar porque los dos momentos se multiplican por factores recíprocos. Se obtiene signo para todos los tests suaves compactos. La densidad del núcleo de forma en cada ventana extiende el signo al dominio correspondiente; en los subespacios primitivos el polar se anula y queda el signo requerido de a_T.

No se necesita un margen uniforme en N: basta semidefinitud de cada bloque y continuidad del límite. Tampoco hace falta probar todos los conjuntos de tasas ni transportar monotonía al variar polos. Para u63/2, éste es un blanco suficiente de UNA sola sucesión de matrices Toeplitz completas.

## 5. Relación con los datos exteriores y límites

En la imagen Z, las derivadas respecto del exponente en a=u+1/2 de X^-a tienen la forma

    partial_a^k[ zeta(a)exp(-(a-1/2)y)]
      =exp(-uy)sum_(j=0)^k binom(k,j)zeta^(k-j)(a)(-y)^j.

La diagonal de esta transformación triangular es(-1)^k zeta(a), distinta de cero para a>1. Por tanto toda confluencia de potencias genera exactamente V_N(u) en su imagen. El puente puede formularse en cualquiera de las dos coordenadas sin suponer una transformación positiva por entradas: se conserva la forma por identificación invertible.

La unión de bloques con todos sus términos cruzados es densa; una sola cadena de vectores f_n, o una unión de espacios de dimensión uniformemente acotada, no hereda esa suficiencia. Los certificados actuales hastaN12 y sus extensiones de tasas no prueban el resto de los bloques. El bloque AP negativo conocido obliga a conservar aritmética cuando se intenta esta dirección a todos los órdenes.


## 6. Tasas móviles: umbral exacto de aproximación fuerte (2026-11-06)

**PROVED como criterio de aproximación; no positividad nueva.** Root; auditorías independientes new_structural_sign y arithmetic_fresh_candidate PASS. Consultados las reglas del proyecto, los tres índices, este puente, THREE002§§7–8 y094/096. La diferencia es permitir tasas u_N que tienden a infinito, sin filtro highpass, y demostrar el umbral en la norma H_eta que controla W. No es el criterio r²/N de094 ni la densidad de una envolvente lineal. No se afirma novedad bibliográfica.

Fijar eta>1/2 y u_N>eta con u_N->infinito. Poner

    V_N(u_N)={exp(-u_N y)P(y):deg P<N},
    L²_eta={f:exp(eta y)f pertenece a L²(0,infinito)},
    ||f||_Heta=||exp(eta y)f||_H1.

Entonces:

1. dist_Heta(f,V_N(u_N))->0 para TODO f en H_eta, a lo largo de todos los N, si y sólo si N/u_N->infinito.
2. La UNION de estos bloques es densa en H_eta si y sólo si limsup_(N->infinito) N/u_N=infinito.

No se caracteriza aquí el cierre de su envolvente lineal.

**Distancia exacta en L²_eta.** Es el caso sin filtro r=0 de la representación por proyección de096§2, aplicado a las tasas desplazadas; no se atribuye novedad a esa fórmula. Para v>eta, normalizar e_v(y)=sqrt(2(v-eta))exp(-vy). La base de Laguerre a tasa a_N=u_N-eta, después de multiplicar por exp(eta y), tiene coeficientes contra e_v proporcionales a ((u_N-v)/(u_N+v-2eta))^j. Sumando la cola geométrica da EXACTAMENTE

    dist_L²eta(e_v,V_N(u_N))²
            =abs((u_N-v)/(u_N+v-2eta))^(2N).            (MOV-DIST)

En efecto el coeficiente de grado j es 2sqrt(a_N(v-eta))/(a_N+v-eta) por ((v-eta-a_N)/(v-eta+a_N))^j; el cuadrado del prefactor es uno menos el cuadrado de la razón. Para u_N->infinito, el logaritmo de(MOV-DIST) es

    -4(v-eta)(N/u_N)(1+o(1)).

Los exponenciales con v>eta son totales en L²_eta por unicidad de Laplace. Las proyecciones ortogonales tienen norma1, de modo que N/u_N->infinito implica aproximación de todo L²_eta a lo largo de N.

**Paso fuerte sin pérdida de grados.** El operador anticausal

    (Jh)(y)=integral_y^infinito h(t)dt

satisface ||Jh||_L²eta<=eta^(-1)||h||_L²eta: después de ponderar, es una integral de traslaciones contra exp(-eta t), de norma L1 igual a1/eta. Si f pertenece a H_eta, entonces f' pertenece a L²_eta, f' es integrable y f tiende a0 en infinito, por lo que f=-Jf'. Aproximar f' por h_N en V_N(u_N) y definir g_N=-Jh_N. Integrar un polinomio por una exponencial NO aumenta su grado; por tanto g_N pertenece al MISMO V_N(u_N) y g_N'=h_N. Así

    ||f-g_N||_Heta
       <=sqrt(eta^(-2)+4) ||f'-h_N||_L²eta ->0.          (MOV-STRONG)

No se necesita una condición adicional N/u_N mucho mayor que log N: esa pérdida aparece si se deriva una proyección L² en lugar de aproximar primero la derivada.

**Necesidad y unión.** Aproximación fuerte implica aproximación L²_eta. (MOV-DIST), con un v>eta fijo, fuerza N/u_N->infinito. Para la unión, si limsup N/u_N=infinito se aplica la suficiencia a una subsucesión. Si limsup es finita, elegir eta<v<min_N u_N; ese mínimo existe y es mayor que eta porque u_N->infinito. Cada distancia de(MOV-DIST) es positiva, y su cola está uniformemente separada de0. Por tanto la unión no aproxima siquiera ese exponencial en L²_eta, ni en H_eta.

**Consecuencia de signo, todavía condicional.** Si se probara W>=0 sobre cada bloque COMPLETO V_N(u_N) de una subsucesión con N/u_N->infinito, continuidad de W en H_eta y traslación, como en§4, darían el objetivo global. Se requieren todos los cruces internos de cada bloque, pero no cruces entre bloques distintos: cada aproximante pertenece a un único bloque positivo. No se ha probado aquí esa hipótesis. Más generalmente basta W[f]>=-epsilon_N||f||² para TODOS f del bloque, con epsilon_N->0 en la subsucesión densa: los aproximantes convergen en H_eta, sus normas L² permanecen acotadas y el error desaparece. La suficiencia de una cota inferior evanescente tiene antecedente en036; no es una nueva desigualdad positiva.

El teorema positivo THREE002§7 exige u_N>=2^(40N), régimen que no satisface el criterio. Además, no se puede conservar su margen fijo W>=9||f||² al pasar a un régimen denso: eso trasladaría el mismo margen a todos los compactos físicos, contradiciendo los cortes suaves de Phi, cuya energía tiende a0 por la identidad física H_full Phi=0 deGRAM19.12, mientras su norma L² tiende a un valor positivo. Esta observación sólo impide preservar coercividad fija; no impide semidefinitud ni márgenes que tiendan a0. No nueva ventanaT, cómputos ni cambios en papers.


**Control de alcance: N/u_N² no suprime el peine completo (2026-11-06).** Root/arithmetic_fresh_candidate, verificación independiente de la aplicación de008. Tomar u_N=N^(3/4) para N suficientemente grande y eta=1. El test exactamente primitivo h de PRIME_PATTERN_FALSIFIER008 pertenece a H_eta y satisface Arch[h]<-3.83||h||², c_h(log2)>||h||²/2. Por este puente, existen aproximantes en V_N(u_N) que convergen a h en H_eta. Pueden hacerse exactamente primitivos: aproximar también dos correctores fijos e^(-2y),e^(-3y) en esos mismos bloques. Su matriz de momentos Tate converge a una matriz invertible; resolver el sistema2x2 elimina los pequeños errores de momentos con coeficientes que tienden a0. Las combinaciones corregidas f_N permanecen en V_N(u_N) y convergen a h en H_eta.

Por continuidad de Arch, de los momentos y de la autocorrelación, eventualmente

    (Arch[f_N]+Polar[f_N])/||f_N||² < -3,
    c_(f_N)(log2)/||f_N||² > 1/3,
    Polar[f_N]=0 exactamente,

mientras N/u_N²=N^(-1/2)->0. Así falla la supresión uniforme del contacto2 como error O(N/u_N²) sobre TODOS los numeradores, y no puede declararse positivo el principal Arch+Polar que elimina la aritmética. Es transporte del falsificador008 al régimen denso, no un principio nuevo sobre necesidad aritmética. No refuta una expansión cuyo principal conserve los contactos y cuya positividad se pruebe independientemente; no afirma W[f_N]<0. No nuevaT ni cómputos.


## 7. Corte aritmético creciente con error uniforme explícito (2026-11-06)

**PROVED como control de cola; signo del bloque retenido OPEN.** Root, auditorías independientes arithmetic_fresh_candidate y new_structural_sign PASS. Consulta las reglas del proyecto, los tres índices, THREE002§7,008 y106_32. Es una aplicación cuantitativa de la cota de cola ya probada, no una nueva estimación de concentración ni positividad. Frente al intento de suprimir contactos bajos, se conserva un corte que crece con N/u.

Para N>=1, u>=2, sea V_N(u)=exp(-uy) polinomios de grado<N y definir

    Q_cut=ceil(exp(40N/u)),
    W_(<=Q_cut)[f]=Arch[f]+Polar[f]
          -2sum_(2<=q<=Q_cut) Lambda(q)/sqrt(q) Re c_f(log q).

Se conserva exactamente la normalización de W y todos los cruces de cada bloque. Entonces

    |W[f]-W_(<=Q_cut)[f]| < exp(-N)||f||²,
    para TODO f en V_N(u).                              (MOV-TAIL)

**Prueba.** La estimación de THREE002§7

    ||f 1_(y>=t)|| <=sqrt6 13^N exp(-ut/2)||f||

usa sólo la base ortonormal y las tasas en[u,3u], no el umbral posterior u>=2^(40N) de positividad. Su límite confluyente conserva la cota para V_N(u). Cauchy–Schwarz para la correlación, seguido de Lambda(q)<=log q, da

    |W-W_(<=Q_cut)|/||f||²
       <=2sqrt6 13^N sum_(q>Q_cut)log(q)q^(-(u+1)/2).

La función log(x)x^(-(u+1)/2) decrece para x>=Q_cut>=2, pues (3/2)log2>1. Comparar cada término con su intervalo precedente e integrar exactamente da

    sum_(q>Q_cut)log(q)q^(-(u+1)/2)
       <=Q_cut^(-(u-1)/2)
                  [2log(Q_cut)/(u-1)+4/(u-1)²].

Como u>=2,

    Q_cut^(-(u-1)/2)<=exp(-10N),
    log Q_cut<=40N/u+1,
    2log(Q_cut)/(u-1)+4/(u-1)²<=40N+6<=46N.

Usando 2sqrt6<5 y13<exp3, la cola es menor que230N exp(-7N). Finalmente N<=exp(N-1) y exp6>400>230 prueban230N exp(-7N)<exp(-N), como se requería.

**Obligación finita que permanece.** Para u_N=N^(3/4), desde N suficientemente grande u_N>=2 y Q_cut,N=ceil(exp(40N^(1/4))). Si se demostrara para TODOS los vectores de cada bloque retenido

    W_(<=Q_cut,N)[f]>=-epsilon_N||f||²,
    epsilon_N->0,

entonces(MOV-TAIL) y§6 darían el objetivo global. No se ha demostrado ese lower ni PSD del bloque retenido. No basta signo de sus diagonales, de algunos vectores o de una cantidad fija de grados. Este corte creciente no contradice la indispensabilidad de átomos para un corte FIJO de106_32. El resultado sólo retira la cola infinita de esta obligación cuantitativa; no decide la compensación aritmética dentro del corte. Sin cómputos, nueva ventanaT o cambios en papers.


## 8. Tamaño necesario del corte en una escala densa (2026-11-06)

**PROVED para el principal truncado; signo completo OPEN.** Constructor fresh_sign_mechanism, auditoría independiente new_structural_sign y comprobación root; deduplicación independiente arithmetic_fresh_candidate. Consulta de los tres índices,007§2 y106_32. La diferencia explícita es cuantitativa: el corte crece con la dimensión, y se obtiene un umbral necesario en la escala u_N=N^(3/4). Las bandas de007 son antecedentes, no una identidad nueva.106_32 trata eliminación de átomos en la energía transformada de diferencias; no se identifica esa truncación con W_(<=Q) aquí.

Para N>=2,u>=1,Q entero>=1, definir la base ortonormal

    phi_j(y)=sqrt(2u)exp(-uy)L_j(2uy), y>=0,
    d=N-1, f=(phi_0-(-1)^d phi_d)/sqrt2.

Entonces ||f||=1 y, con la definición íntegra de W_(<=Q) de§7,

    W_(<=Q)[f] <= 2log u+32+4sqrt(Q)log Q+6/u
                         -(2/u)exp((N-1)/u).             (MOV-NEC)

**Prueba del polar.** Las integrales de phi_j contra exp(±y/2) son sqrt(2u)(-1)^j r^(±j)/(u∓1/2), donde r=(u+1/2)/(u-1/2). Su producto simetrizado da las bandas de007 generalizadas a u: p_d=C_u(-1)^d(r^d+r^(-d)), C_u=2u/(u²-1/4). Por tanto el polar del vector elegido es EXACTAMENTE C_u(2-r^d-r^(-d)). Como 2/u<=C_u<=3/u y log r>=1/u, es <=6/u-(2/u)exp(d/u).

**Prueba arquimediana y aritmética.** El multiplicador m(tau)=Re psi(1/4+i tau/2)-log pi tiene mínimo m(0)>-8. Su media contra la densidad de Fourier de phi_0 es a_0=psi((u+1/2)/2)-log pi<=log u. La última desigualdad usa psi(x)<log x; ésta sigue de Jensen aplicada a log para una variable Gamma(x,1). La cota m(0)>-8 sigue de psi(1/4)=-gamma-pi/2-3log2 y las cotas gamma<1,pi/2<2,3log2<3,log pi<2. En la coordenada de Cayley, las bandas arquimedianas son coeficientes de Fourier de ese multiplicador; cada una tiene módulo <=integral |m|<=a_0+16. Así la contribución de las dos coordenadas es <=2log u+32. Finalmente |c_f(t)|<=||f||²=1, Lambda(q)<=log q y sum_(q=2)^Q q^(-1/2)<=2sqrt Q dan el majorante 4sqrt Q log Q para todos los contactos retenidos. Sumando se obtiene(MOV-NEC).

**Consecuencia móvil.** Fijar 0<delta<2, u_N=N^(3/4). Si log Q_N<=(2-delta)N/u_N, el cociente del majorante aritmético respecto de (2/u_N)exp((N-1)/u_N) es <=2(2-delta)N exp(-delta N^(1/4)/2+1/u_N), que tiende a0. Los términos logarítmicos y 6/u_N también son despreciables. Eventualmente

    W_(<=Q_N)[f_N] <= -exp((N-1)/u_N)/u_N -> -infinito.

En particular, ningún corte polinómico fijo Q_N<=N^k permite una cota inferior -epsilon_N||f||², epsilon_N->0, sobre TODO V_N(u_N). Si existiera tal cota a lo largo de todos los N, necesariamente liminf u_N log Q_N/N>=2: cualquier subsucesión con cociente <=2-delta contradice la cota anterior. No se afirma que el umbral2 sea suficiente ni óptimo. El corte suficiente para ERROR de§7 tiene constante40, de modo que ambas cotas fijan el mismo orden exponencial para esta escala concreta.

**Alcance.** Los vectores no se afirman primitivos. W completa no se ha probado negativa: la cola omitida puede compensar el polar. El umbral no se extiende sin prueba a todas las escalas densas, especialmente si N/u_N crece lentamente. No se firma el principal con corte40, no nueva ventanaT y no cambios en papers.


## 9. Corte insuficiente incluso con ambos momentos nulos (2026-11-06)

**PROVED: falsificador primitivo del principal truncado, no de W completa.** Construcción fresh_sign_mechanism/root y comprobación mutua de constantes; revisión matemática independiente new_structural_sign PASS. Consulta previa de los tres índices,008 y§§6–8; búsqueda dirigida de filtros Dirichlet/Jackson con Laguerre y momentos Tate sin este enunciado localizado. La diferencia nueva es un test explícito en el MISMO bloque móvil con corte creciente. El vector gamma de008 no da esta escala: su ancho es sqrt(N)/u, mientras el filtro siguiente alcanza N/u. No se atribuye novedad al núcleo de Dirichlet ni a las desigualdades de008.

Sea u=N^(3/4), N>=2^60, y Q>=1 entero con

    log Q <= 2^(-12)N/u.

Existe f en V_N(u), real, ||f||=1, con ambos momentos Tate exactamente nulos y f(0)=0, tal que

    W_(<=Q)[f]<-3.                                      (PRIM-CUT)

**Construcción exacta.** Poner M=floor(N/4), r=(u+1/2)/(u-1/2) y definir los coeficientes c_j del polinomio

    C(z)=(1-z)(z+r)(z+r^(-1)) [sum_(j=0)^(M-1)(-z)^j]^4.

Su grado es4M-1<N. Tomar f proporcional a sum_j c_j phi_j, normalizado en L². Las fórmulas de Laplace de§8 evalúan los momentos en z=-r y z=-1/r; por tanto ambos se anulan EXACTAMENTE. Además phi_j(0)=sqrt(2u), así que C(1)=0 implica f(0)=0.

**Segundo momento espectral.** En la coordenada de Cayley z=-exp(2ix), -pi/2<x<pi/2, se tiene |tau|=u|tan x|. La medida espectral de phi_0 se transforma en medida uniforme, que se cancela en la razón normalizada. Escribir a=1/(u²-1/4), S=sin(Mx)/sin x. Entonces |(z+r)(z+1/r)|=a+4sin²x y |1-z|²=4cos²x, de modo que

    E_f tau² = u² integral sin²x(a+4sin²x)²|S|^8 dx
                      / integral cos²x(a+4sin²x)²|S|^8 dx.

Todas las integrales siguientes tienen límites [-pi/2,pi/2]. Para |x|<=1/(2M), M>=2, cos²x>=1/2 y |S|>=M/2. El denominador es >=a²M^7/512. Usar |S|<=min(M,1/|sin x|), |sin x|<=|x| y |sin x|>=|x|/2. Dividir en |x|<=1/M y su complemento da

    I_2=integral sin²x |S|^8 dx
         <=(2/3+128/5)M^5 <27M^5,
    I_6=integral sin^6x |S|^8 dx
         <=(2/7+8)M <9M.

Como (a+4sin²x)²<=2a²+32sin^4x, el numerador es <=u²(2a²I_2+32I_6). Por tanto, para1<=u<=M,

    E_f tau² <=512u²[54/M²+288/(a²M^6)]
              <=175104(u/M)² <2^18(u/M)².                (PRIM-MOM)

Se usó a>=1/u² y u/M<=1. El factor1-z asegura integrabilidad del segundo momento también en los extremos x=±pi/2.

**Signo de cada pieza retenida.** Por008, Arch[f]<-4+17 E_f tau² y c_f(t)>=1-(t²/2)E_f tau². Para N>=2^60, M>=N/8 y u<=M, así E_f tau²<=2^24/sqrt(N)<=1/64. Luego Arch[f]<-3. Si log q<=2^(-12)N/u, entonces log q<=M/(512u), y(PRIM-MOM) implica c_f(log q)>=1/2. Todos los contactos retenidos son no positivos y el polar es cero, lo que demuestra(PRIM-CUT).

**Alcance.** El corte puede crecer exponencialmente en N/u con la pequeña constante2^(-12); todo corte polinómico fijo queda incluido eventualmente. No se transfiere a primitivas el umbral2 de§8, ni se prueba que la constante aquí sea óptima. La cola omitida podría compensar el déficit: W completa y el principal con corte40 de§7 siguen OPEN. La mera eliminación del polar no permite reemplazar ese corte por uno polinómico. Sin cómputos ni nueva ventanaT o cambios en papers.
