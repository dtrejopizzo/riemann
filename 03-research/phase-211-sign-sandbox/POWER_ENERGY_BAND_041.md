# POWER_ENERGY_BAND_041 — Beneficio firmado en una banda energética móvil

Estado: **PROVED BAND**, revisión independiente aprobada en [POWER_ENERGY_AUDIT_041.md](POWER_ENERGY_AUDIT_041.md). u=63/2 fijo. Papers intactos. No signo W global.

## 1. Corpus y diferencia

Consultados ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos LOW_TABLE018, CELL_BALANCE024, ARCH_CELL026, INTERIOR_SCALE030, GAMMA_WEIGHT031 y CRITICAL_BALANCE040. No se presenta otra integración por partes como signo. Frente024/030/031, la banda crece y se desplaza con N hasta la energía exponencial; se conserva el factor diferencial040 ANTES de tomar módulos. El resto se compara con un beneficio real de la misma escala energética, no con W total.

## 2. Resultado completo y definiciones

Para TODOS N>=2^80, ponga d=N−1, delta=N^(-2), v=1/2+delta,

    T=2dv/(u²−v²), L=sqrt(N)/100,
    g(t)=rho_N(t)/2−rho_N'(t), C_N=exp(T/2)g(T)>0.

Con el inverso Möbius COMPLETO h_N de022 y el MISMO peso celular

    B(x)=log(floor(x)!)−x H_floor(x)+floor(x),

se prueba

    2 int_(exp(T))^(exp(T+L)) h_N(x)B(x)dx
                < −C_N/25600.                        (BAND)

La banda es favorable en la identidad W/norma²=ARCH_sharp−2int hB. No se descarta ni reemplaza ningún salto de B. La contribución de su complemento sigue abierta.

## 3. Expansión040 trasladada sin pérdida de signo

Use el perfil FIJO f(ell)=exp(vell)g(T+ell)/g(T), sobre toda la recta, y

    S(ell)=sum_(n>=1)mu(n)n^(−1−delta)f(ell+logn).

La serie es absoluta. El mismo argumento Fourier040, multiplicando el integrando por exp(i xi ell), da UNIFORMEMENTE en ell

    S=(delta−D)f−gamma(delta−D)²f+r,
    |r|<=E_N<1/(10000N),                              (EXP)

para este delta,N. Esta extensión no cambia ninguna constante de040: el factor añadido tiene módulo1.

Ponga z(ell)=delta f(ell)−f'(ell). Entonces

    int_0^L exp(−delta ell)S(ell)dell
      =1−exp(−delta L)f(L)
         −gamma[z(0)−exp(−delta L)z(L)]
         +int_0^L exp(−delta ell)r(ell)dell.            (ENDS)

Se utiliza sólo un intervalo FINITO; no se integra una serie Euler en el borde crítico ni se supone sumabilidad de sum|mu(n)|/n.

## 4. Beneficio uniforme de bordes para el perfil REAL

Escriba b=q'(T), M=u²/(2N−3). Por040, 50/N<b<M<=u²/N, q(T)−v<=M/u², y por CURV040

    (T/(T+s))² b<q'(T+s)<b.

Las comparaciones racionales del verificador dan L>=8, L<T/4. Por ello q'(T+s)>b/2 para0<=s<=L. Como q(T)>=v,

    log f(L)
      =−int_0^L(q(T+s)−v)ds
           +log[(1/2+q(T+L))/(1/2+q(T))]
      <=−bL²/4+bL<=−bL²/8<=−1/1600.

Así f(L)<=1−1/3200. En toda la banda, log f(s)<=bs<log2, por lo que f<=2. Además

    |f'|<=2M(L+2), |f''|<1.                           (DER)

Para el segundo bound, use directamente

    f''/f=(v−q)²−q'+2(v−q)q'/(1/2+q)+q''/(1/2+q),

|v−q|<=M(L+1), |q''|<2M/T y1/2+q>=1. Las constantes del verificador implican el bound estricto; no se supone una concavidad nueva de f.

En particular |z|<=2delta+2M(L+2). Con0<gamma<1, ENDS y EXP dan

    int_0^L exp(−delta ell)S(ell)dell
       >1/3200−[4delta+4M(L+2)]−E_N L
       >1/12800.                                     (GAIN)

Todas las funciones aquí son las del átomo gamma REAL; no se sustituyen por un perfil elegible.

## 5. B real y su corrección controlada

El estimate elemental

    |B(x)+gamma x|<=logx+1, x>=1                      (B-REAL)

basta en esta banda. Prueba: si n=floorx, theta=x−n, entonces

    B+gamma x=T_n−theta logn−x epsilon_n,
    1<=T_n:=logn!−nlogn+n<=1+logn,
    0<epsilon_n:=H_n−logn−gamma<1/n.

Las primeras cotas proceden de comparar sum logk con el integral monótono; las últimas del integral elemental del residuo armónico. Como x/n<2, la cota inferior es mayor que−1−logx y la superior no supera1+logx. Incluye n1 y los extremos de salto.

Al cambiar x=exp(T+ell), el término principal−gamma x del B EXACTO produce

    −2gamma C_N int_0^L exp(−delta ell)S(ell)dell.

El resto V=B+gamma x conserva toda la aritmética, incluidos saltos. Por EXP/DER, delta<1/1000 yE<1, |S|<8. En consecuencia su contribución absoluta, DIVIDIDA por C_N, es menor que

    16exp(−T)L(T+L+1)
       <32N²exp(−N/1984)<1/25600.                    (V-ERROR)

Aquí N/1984<T<N, L<N, y exp(−x)<=4!x^(-4) permite verificar la última comparación sólo con racionales en N0=2^80. Por gamma>1/2 y GAIN, el principal es menor que−C_N/12800. Sumando V-ERROR se obtiene BAND.

## 6. Alcance y precisión

BAND es una desigualdad firmada sobre una integral REAL, no una identidad etiquetada como positividad. Se ha retenido la derivada total y sus bordes, y sólo después se acotan el resto Fourier y la corrección aritmética. C_N puede ser exponencialmente grande; el signo de la banda se decide porque su beneficio es de esa MISMA escala.

Esto no controla la compensación contra el interior anterior a T ni contra las otras bandas. Un error de esta magnitud tampoco decide W, cuyo residuo total puede ser mucho menor que cada energía. No hay campaña de N, contactos o precisiones. La frontera crítica sum|mu|/n no se usa para negar cancelación firmada: sólo impide un Fubini absoluto global que aquí no se necesita.

## 7. Expansión periódica uniforme de B y error integrado explícito

Complemento auxiliar a BAND, con el B REAL019 completo. La expansión es una aplicación elemental de sumación Euler/Stirling; no se presenta como un principio nuevo de signo. La cota que se registra conserva los saltos exactos y separa la oscilación periódica de un error uniformemente O(1/x), útil para integrar contra el inverso firmado. BAND no depende de esta mejora: su prueba anterior usa una cota más gruesa suficiente.

Ponga n=floorx, theta=x−n, B1(theta)=theta−1/2 y

    kappa=(1/2)log(2pi)−1/2.

Para TODO real x>=1,

    B(x)=−gamma x−B1(theta)logx+kappa+E(x),
    −1/x<E(x)<1/(2x), en particular |E(x)|<=1/x.        (SAWTOOTH)

### 7.1. Dos restos elementales, sin datos numéricos

Para TODO entero n>=1,

    log(n!)=(n+1/2)logn−n+(1/2)log(2pi)+s_n,
                    0<s_n<1/(12n),
    H_n=logn+gamma+1/(2n)+e_n,
                    −1/(12n²)<e_n<0.                  (ELEMENTARY-EM)

Se incluyen pruebas compactas de las cotas y la constante. Sea r=1/(2n+1). La serie absolutamente convergente de atanh da

    a_n=(n+1/2)log(1+1/n)−1
        =sum_(j>=1) r^(2j)/(2j+1),
    0<a_n<r²/[3(1−r²)]=1/[12n(n+1)].

Si Z_n=n!exp(n)/n^(n+1/2), entonces logZ_n−logZ_(n+1)=a_n. Por sumabilidad Z_n converge a una constante positiva C y logZ_n−logC=sum_(k>=n)a_k está entre0 y1/(12n). La constante es C=sqrt(2pi): la recurrencia de los integrales I_j=int_0^(pi/2)sin(t)^jdt y I_(2n+1)<=I_(2n)<=I_(2n−1) dan, con b_n=binom(2n,n)/4^n,

    2/[pi(2n+1)]<=b_n²<=1/(pi n),
    sqrt(n)b_n->1/sqrt(pi).

Pero Z_(2n)/Z_n²=b_n sqrt(n/2)->1/sqrt(2pi), mientras el mismo cociente tiende a1/C. Así C=sqrt(2pi), y queda probada la primera cota de ELEMENTARY-EM.

Para la segunda, defina

    tau_n=1/(2n)+1/[2(n+1)]−log(1+1/n)
       =4sum_(j>=1) [j/(2j+1)]r^(2j+1)>0.

La comparación coeficiente a coeficiente j/(2j+1)<=j/3 prueba

    tau_n<4r³/[3(1−r²)²]
        =(1/12)[1/n²−1/(n+1)²].

La sucesión D_n=H_n−logn−1/(2n)−gamma tiende a0 y D_n−D_(n+1)=−tau_n. Por telescopía, e_n=D_n=−sum_(k>=n)tau_k, que pertenece a(−1/(12n²),0). No se ha citado un resto asintótico sin justificar su signo.

### 7.2. Resto uniforme y saltos en enteros

Sustituir ELEMENTARY-EM en B(x)=log(n!)−xH_n+n da EXACTAMENTE

    E(x)=F(n,theta)+s_n−xe_n,
    F(n,theta)=(theta−1/2)log(1+theta/n)−theta/(2n).

Para0<=theta<=1/2, log(1+theta/n)<=theta/n implica F>=−theta(1−theta)/n>=−1/(4n), y F<=0 es inmediato. Para1/2<=theta<1, log>=0 da F>=−1/(2n), mientras log<=theta/n da F<=theta(theta−1)/n<=0. En conjunto,

    −1/(2n)<=F<=0,
    0<s_n−xe_n<(2n+1)/(12n²)<=1/(4n).

Como x<2n, se concluye SAWTOOTH. En enteros se conserva la convención theta0: B1(0)=−1/2, no su promedio0. El salto de B en un entero m es logm; el de −B1({x})logx es también logm. Por tanto E es CONTINUO en cada entero. No se borran los saltos ni se mezclan sus límites izquierdo y derecho.

### 7.3. Cota integrada periódica con bordes explícitos

Sea

    Q2(x)=(1/2)[{x}²−{x}+1/6]−1/48.

Es una función CONTINUA periódica, incluso en enteros, con derivada B1({x}) casi por todas partes y norma uniforme1/16. Si1<=a<b y h es absolutamente continua en[a,b], defina

    I=int_a^b h(x)[B(x)+gamma x−kappa]dx,
    F_h(x)=h(x)logx.

SAWTOOTH e integración por partes contra la primitiva CONTINUA Q2 dan

    | I+[F_h(x)Q2(x)]_a^b |
      <=(1/16)int_a^b |F_h'(x)|dx
                              +int_a^b |h(x)|/x dx.    (PERIODIC-ERROR)

Equivalente, si se quiere eliminar el borde firmado,

    |I|<=(1/16)[|h(a)|loga+|h(b)|logb
                        +int_a^b |h'(x)logx+h(x)/x|dx]
                        +int_a^b |h(x)|/x dx.

No aparecen términos de salto adicionales: los valores en enteros no cambian la integral y Q2 es continua allí. Para b infinito se puede pasar al límite cuando F_h(b)->0 y los integrales del mayorante convergen; los kernels gamma/inversos de N fijo tienen el decaimiento polinómico requerido.

Esta desigualdad no asigna signo al error ni a h. Retiene la función B completa, el término principal −gamma x y la constante kappa, además de la cancelación periódica antes del módulo. No prueba por sí sola signo W ni domina automáticamente el complemento de la banda. Su papel es cuantificar precisamente qué bordes y qué variación de h harían despreciable esa corrección; el balance real BAND ya demostrado es la aplicación positiva de esta ronda.
