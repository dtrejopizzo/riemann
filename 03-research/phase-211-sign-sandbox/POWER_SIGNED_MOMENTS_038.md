# POWER_SIGNED_MOMENTS_038 — Producto firmado conservado mediante Fourier gamma

Estado: **PROVED**, revisión hostil independiente aprobada en POWER_SIGNED_AUDIT_038.md y verificador exacto PASS reproducido. Tasa fija u=63/2. Papers intactos.

Resultado: el error central de agrupar Möbius se controla por B_Q/N SIN el factor V_Q/U_Q; ese factor permanece sólo en una cola exponencialmente pequeña. No se afirma signo de W ni del residuo infinito.

## 1. Corpus y diferencia precisa

Consultados ROUTES-TRIED-INDEX/README.md, grid maestro y CROSSWORD-TO-D; leídos ENERGY_GROUP037, UNIFORM_CUTOFF026 y MOVING_BALANCE036. Las entradas542/543 del índice tratan cumulantes de un calibrador de grupo de clases y formas completas diferentes. Aquí el objeto es un producto FINITO Möbius sobre divisores de Q aplicado al mismo perfil gamma REAL037. No se usa una desigualdad Jensen para una medida firmada.

La diferencia respecto037 es conservar exactamente el multiplicador firmado en Fourier y estimar el logaritmo de su parte centrada en la banda de frecuencias relevante para gamma. La suma de módulos divisor V_Q/U_Q sólo se usa fuera de esa banda, donde el transformado gamma ya es exponencialmente pequeño. La identidad de momentos sola no se llama una cota de signo.

## 2. Perfil real extendido y operador finito

Ponga d=N−1,a=u²−1/4=992,c_N=d/a y rho=rho_N, extendida de modo PAR a toda R. Defina g(y)=rho(y)/2−rho'(y) y

    f_N(ell)=e^(ell/2)g(c_N+ell)/g(c_N).

Para ell>=0, es precisamente el perfil real r_N de037:

    f_N(ell)=e^ell D_N(e^ell).

Para ell<−c_N el factor g puede ser negativo. NO se considera f_N una densidad positiva en toda R. La densidad positiva usada para normalizar el transformado se introduce separadamente en§4.

Para Q cuadrado libre finito, defina

    U_Q=prod_(p|Q)(1−1/p), V_Q=prod_(p|Q)(1+1/p),
    A_Q=sum_(p|Q)logp/(p−1),
    B_Q=sum_(p|Q)p(logp)²/(p−1)²,
    M_Q f(ell)=U_Q^(-1)sum_(b|Q)mu(b)b^(-1)f(ell+logb).

El kernel agrupado037 satisface K_(N,Q)(m)=(U_Q/m)M_Q f_N(logm). Los parámetros A_Q,B_Q no se interpretan como media/varianza de una probabilidad: los dos primeros cumulantes firmados son−A_Q y−B_Q.

## 3. Producto Fourier exacto y resto centrado

Con Z_Q(z)=prod_(p|Q)(1−p^(z−1)), el multiplicador de M_Q en frecuencia real xi es Z_Q(i xi)/U_Q. La expansión ABSOLUTA

    log[Z_Q(i xi)/U_Q]
      =−sum_(p|Q)sum_(k>=1)[exp(ik xi logp)−1]/(k p^k)

elige la rama continua igual a0 en xi0. Restar el término lineal y usar |exp(it)−1−it|<=t²/2 prueba para TODO xi real

    |log[Z_Q(i xi)/U_Q]+iA_Q xi|<=B_Q xi²/2.

En particular

    |Z_Q(i xi)/U_Q−exp(−iA_Q xi)|
       <=(B_Q xi²/2)exp(B_Q xi²/2).                      (CENTRAL-MULT)

No se asigna signo a un cumulante ni se aplica convexidad firmada. Para la cola basta el bound general

    |Z_Q(i xi)/U_Q−exp(−iA_Q xi)|<=V_Q/U_Q+1.             (TAIL-MULT)

## 4. Transformado gamma exacto y normalización en el centro

Use Fourier con exp(−i xi y). En esta sección norm²=Gamma(N−1/2)/[2sqrt(pi)Gamma(N)u^(2N−1)] es la normalización del átomo gamma original. La autocorrelación normalizada tiene

    rhohat(xi)=1/[norm²(u²+xi²)^N].

El desplazamiento y el peso exponencial dan exactamente

    fhat_N(xi)=C_N exp(i xi c_N)(1−i xi)
                        (a+xi²+i xi)^(-N),
    C_N=exp(−c_N/2)/[norm² g(c_N)]>0.                   (FOURIER)

El factor1−i xi procede de integrar rho' por partes contra exp((1/2−i xi)y). El módulo del denominador al cuadrado es

    |a+xi²+i xi|²=a²+1985xi²+xi^4.

Para controlar C_N sin pérdidas exponenciales, introduzca la probabilidad POSITIVA

    p_N(y)=exp(y/2)rho_N(y)/L_N,
    L_N=int_R exp(y/2)rho_N(y)dy=1/(norm² a^N).

Su media y varianza, por derivar la transformada bilateral positiva, son

    E Y=N/a,
    sigma_N²=1985N/a².

La función p_N es unimodal: en y<0 su derivada logarítmica es1/2+q_N(|y|)>0 y en y>0 es1/2−q_N(y), con q_N estrictamente creciente. Sea y_* su único modo, q_N(y_*)=1/2. Riccati026 da

    y_*=d/[a+q_N'(y_*)],
    0<=c_N−y_*<=dM_N/a²<=u²/a²,
    M_N=u²/(2N−3).

Como0<q_N'<M_N,

    p_N(c_N)>=p_N(y_*)exp[−M_N(c_N−y_*)²/2]
             >p_N(y_*)/2.

La última cota sigue de M_N<=u² y u^6/(2a^4)<log2, una comparación racional elemental. Chebyshev concentra al menos3/4 de la masa en un intervalo de longitud4sigma_N, luego p_N(y_*)>=3/(16sigma_N). Se concluye

    p_N(c_N)>=3/(32sigma_N),
    C_N a^(-N)=1/[(1/2+q_N(c_N))p_N(c_N)]
                <=32sigma_N/3<sqrt(N)/2.                (NORMALIZER)

Aquí se usó q_N(c_N)>1/2 de037. La comparación del modo y el control de variación son esenciales: Chebyshev y unimodalidad por sí solos no darían una cota inferior en un punto arbitrario.

## 5. Envolvente central y cola integrable

Sea c=1985/a². NORMALIZER y FOURIER dan

    |fhat_N(xi)|<sqrt(N)/2 ·sqrt(1+xi²)
                   [1+c xi²+xi^4/a²]^(-N/2).

Para |xi|<=1, log(1+c xi²+xi^4/a²)>=(1985/(a²+1986))xi²>=xi²/500. Así

    |fhat_N(xi)|<=sqrt(N)exp(−Nxi²/1000).                (CENTRAL-GAMMA)

Para |xi|>=1, se separa la potencia de1+c xi² en dos mitades. Si N>=16,

    [1+c xi²]^(-N/2)
      <=(1+c)^(-N/4)[1+c xi²]^(-4).

Como c>1/500 y log(1+c)>=c/(1+c)>1/500, y usando sqrt(1+xi²)<=1+|xi|,

    int_(|xi|>=1)|fhat_N(xi)|d xi/(2pi)
       <65sqrt(N)exp(−N/2000).                          (TAIL-GAMMA)

Un mayorante explícito de la integral racional auxiliar en toda R es260: int_0^infty(1+c xi²)^(-4)d xi<46 e int_0^infty xi(1+c xi²)^(-4)d xi<84. Se conserva2pi en la normalización y sólo se usa pi>1 para el bound65.

## 6. Desigualdad principal

**Teorema.** Si N>=16 y B_Q<=N/1000, entonces para TODO ell real,

    |M_Q f_N(ell)−f_N(ell−A_Q)|
       <=12000 B_Q/N
          +65sqrt(N)(V_Q/U_Q+1)exp(−N/2000).             (SIGNED-FOURIER)

Prueba. Invertir Fourier, conservar el multiplicador firmado y restar la traslación exacta exp(−iA_Q xi). En |xi|<=1, CENTRAL-MULT y CENTRAL-GAMMA se multiplican; B_Q<=N/1000 deja exp(−Nxi²/2000). Ampliar la integral positiva hasta R da

    (B_Q/2)sqrt(N)int_R xi²exp(−Nxi²/2000)d xi/(2pi)
      =2000^(3/2)B_Q/[8sqrt(pi)N]<12000B_Q/N.

En |xi|>=1 se combinan TAIL-MULT y TAIL-GAMMA. Todas las integrales son absolutas, y Q es finito. Esto prueba la desigualdad, sin hacer de Z_Q/U_Q una probabilidad.

El principal es una TRASLACIÓN del perfil gamma real por el primer momento firmado, no simplemente1. El cumulante segundo negativo queda controlado analíticamente por B_Q en el error central; no se usa su signo como si fuera una varianza positiva.

## 7. Corolario: ventana de orden sqrt(N) para la MISMA familia Q037

Para TODOS N>=2^80 conserve exactamente la elección de037:

    K=floor(N^(1/8)), Q=prod_(p<=K)p.

Entonces para TODO m con

    A_Q<=logm<=A_Q+sqrt(N)/100,

el kernel agrupado REAL satisface

    (4/5)U_Q/m<K_(N,Q)(m)<(6/5)U_Q/m.                    (WIDE-WINDOW)

Es una ampliación analítica de la longitud logarítmica, de orden N^(1/4) en037 a orden sqrt(N), sin recorrer nuevos N ni Q. No es una conclusión sobre la suma exterior infinita.

Prueba. Las cotas elementales037 dan A_Q<=logQ<=KlogK<=K²<=N^(1/4) y V_Q/U_Q<=N^(1/4). Además B_Q<=log²Q para esta familia, que contiene2 y3. En efecto p/(p−1)²<=1 para p>=3, el término p2 es2log²2, y el producto cruzado2log2log3 dentro de log²Q domina el log²2 adicional. Por tanto B_Q<=sqrt(N)<=N/1000.

El error central de SIGNED-FOURIER es <=12000/sqrt(N)<1/100. El error de cola también es <1/100: V/U+1<=2N^(1/4) da un prefactor<=130N, y exp(−N/2000)<=2(2000/N)² produce el mayorante1.04·10^9/N.

Escriba s=logm−A_Q en[0,sqrt(N)/100]. El perfil trasladado está en su lado físico positivo. DILATE037 da directamente

    exp{−M_N[s/1985+s²/2]}<=f_N(s)<=1+M_Ns.

Como M_N<=u²/N y N>=2^80, el exponente es <=u²[1/(198500sqrt(N))+1/20000]<1/10, mientras M_Ns<1/100. Luego9/10<f_N(s)<101/100. Restar/sumar los dos errores menores que1/100 prueba

    4/5<M_Q f_N(logm)<6/5.

Multiplicar por U_Q/m prueba WIDE-WINDOW. Todos los extremos y desigualdades monótonas se verifican mediante las constantes racionales del script. La extensión par de f no se interpreta como probabilidad; en este corolario todos sus argumentos físicos son no negativos.

## 8. Alcance y obligación pendiente

SIGNED-FOURIER elimina V_Q/U_Q del error CENTRAL que dominaba037. Ese factor queda sólo multiplicado por una cola exponencial en N. Permite formular condiciones efectivas de signo para un Q creciente si el perfil trasladado es favorable y los dos errores son menores que él; esas condiciones deben probarse antes de concluir un signo.

El teorema no controla todavía la suma exterior sobre m coprimo con Q ni la integral completa del residuo polar−peine. Tampoco el error O(B_Q/N) puede venderse como un error relativo suficiente frente a componentes de fase lambda^N. No se declara W positiva, h_N positivo ni una contracción absoluta del resto.

La extensión par de rho se utiliza sólo para obtener FOURIER. Fuera del lado físico de la traslación, f_N puede tomar signos; no se aplica Jensen ni se le atribuye una ley positiva. La única probabilidad auxiliar usada es p_N en§4, cuyo papel es normalizar y localizar su modo con control explícito.

## 9. Validación

POWER_SIGNED_AUDIT_038.md aprueba independientemente FOURIER/NORMALIZER, constantes centrales y cola, rama del logaritmo del producto finito, normalización2pi y ausencia de interpretaciones probabilísticas para el operador firmado. El corolario WIDE-WINDOW también fue revisado por el constructor principal y el auditor.

Verificador: tools/power_signed_moments_038_verify.py, Fraction/intervalos de constantes; PASS. No evalúa W en nuevos N ni listas de Q: sólo las constantes de las familias analíticas. Papers intactos.
