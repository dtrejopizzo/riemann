# POWER_INFINITE_SHOULDER_039 — Positividad del inverso COMPLETO en un hombro energético

Estado: **PROVED**, auditoría hostil independiente aprobada en POWER_SHOULDER_AUDIT_039.md y verificador exacto PASS reproducido. Tasa FIJA u=63/2. Papers intactos.

Resultado: para TODOS N>=4,000,000, los inversos aritméticos COMPLETOS h_N y K_N son positivos para TODO x>=exp(T_N), donde

    d=N−1, L=1000,
    v_N=1/2+L/sqrt(N),
    T_N=2d v_N/(u²−v_N²).

El corte es T_N=d/992+O(sqrt(N)) y mejora el corte K026 de escala d/330. No se afirma signo de W ni del resto interior.

## 1. Corpus y diferencia precisa

Consultados ROUTES-TRIED-INDEX/README.md, grid maestro y CROSSWORD-TO-D; leídos INVERSE_KERNEL020, UNIFORM_CUTOFF026, ENERGY_GROUP037 y SIGNED_MOMENTS038. La identidad Euler/Möbius y el centrado del término principal son previos; no se presentan como resultados nuevos de signo.

La diferencia es pasar del grupo FINITO038 al producto aritmético INFINITO conservando su multiplicador firmado. Se trabaja exclusivamente en sigma>1, donde todos los productos, series y momentos utilizados convergen absolutamente. Una inclinación v>1/2 del perfil gamma desplaza el centro al hombro energético; sus momentos se controlan mediante una cota Chebyshev demostrada. Esto controla por primera vez el complemento completo del inverso en esta región, no sólo un Q finito. No hay campaña de N o listas de primos.

Se distinguen dos objetos: h_N es el inverso de H_N; K_N=J_N+xh_N es el inverso compensado de026. Ambos se incluyen abajo para que la comparación con el corte026 se refiera al MISMO K_N.

## 2. Objetos reales y perfil inclinado

Sea rho_N par la autocorrelación gamma normalizada y q_N=−rho_N'/rho_N para argumento positivo. En todo el memo norm²=Gamma(N−1/2)/[2sqrt(pi)Gamma(N)u^(2N−1)] denota la norma del átomo gamma original. Para c en{1/2,3/2}, defina

    g_c(t)=c rho_N(t)−rho_N'(t),
    H_N(x)=x^(-3/2)g_(1/2)(logx),
    G_N(x)=x^(-1/2)g_(3/2)(logx)=w_N−xw_N',
    w_N=x^(-1/2)rho_N(logx).

Los inversos COMPLETOS satisfacen exactamente

    h_N(x)/H_N(x)
      =sum_(n>=1)mu(n)n^(-1/2)
                       g_(1/2)(logx+logn)/g_(1/2)(logx),
    K_N(x)/G_N(x)
      =sum_(n>=1)mu(n)n^(-1/2)
                       g_(3/2)(logx+logn)/g_(3/2)(logx).

Estas fórmulas provienen de019/022, con sus jacobianos. Para N fijo son absolutas.

Para1/2<=v<=2 ponga

    a_v=u²−v², t_v=2dv/a_v, sigma=v+1/2,
    f_(c,v)(ell)=exp(v ell)g_c(t_v+ell)/g_c(t_v).

Se usa la extensión par de rho para Fourier. f_(c,v) puede ser negativa en una parte del semieje izquierdo; no se considera una densidad positiva. En los argumentos físicos t_v+ell>=0 se conserva el perfil real original.

En x=exp(t_v), ambos cocientes de inversos se escriben, para el c correspondiente,

    R_c(t_v)=sum_(n>=1)mu(n)n^(-sigma)f_(c,v)(logn).       (FULL)

## 3. Control elemental de TODOS los momentos aritméticos

Se prueba primero psi_Lambda(x)<=2x para TODO real x>=1. Para entero n,

    psi_Lambda(2n)−psi_Lambda(n)<=log binom(2n,n)<=2nlog2.

Cada potencia prima en(n,2n] contribuye1 en la fórmula de Legendre del binomio, y todas las demás diferencias de pisos son no negativas. Para entero M>=6 tome n=ceil(M/2). Por inducción,

    psi_Lambda(M)<=psi_Lambda(n)+2nlog2
       <=2n(1+log2)<(17/10)(M+1)<=2M.

Los casos1<=M<=5 siguen de psi_Lambda(M)<=MlogM<=Mlog5<2M; no hace falta consultar una tabla de primos. Pasar a floor(x) prueba la cota real.

Para sigma=1+delta>1, integración por partes absoluta da

    A_sigma=sum Lambda(n)n^(-sigma)
      =sigma int_1^infty psi_Lambda(x)x^(-sigma−1)dx
      <=2sigma/delta,
    B_sigma=sum Lambda(n)logn n^(-sigma)
      <=2sigma/delta².                                  (MOMENTS)

En el segundo bound se resta primero el término no positivo de la integración por partes, −int psi_Lambda(x)x^(-sigma−1)dx, y sólo después se aplica psi<=2x al término sigma logx. No se usa psi superior contra un kernel de signo cambiante.

Los productos infinitos son absolutamente convergentes:

    U_sigma=prod_p(1−p^(-sigma))=1/zeta(sigma)>0,
    V_sigma=prod_p(1+p^(-sigma)),
    V_sigma/U_sigma=zeta(sigma)^2/zeta(2sigma)
                    <=(1+1/delta)^2,
    U_sigma>=delta/(1+delta).                            (PRODUCTS)

Sólo se usa la suma Euler absolutamente convergente y zeta(sigma)<=1+1/delta. En1/2<v<=2, sigma<=5/2 y (MOMENTS) da A_sigma<=5/delta,B_sigma<=5/delta².

## 4. Fourier gamma UNIFORME en c y v

El argumento038 se extiende a c en{1/2,3/2}, v en[1/2,2] conservando sus constantes12000 y65. Se detallan los cambios necesarios.

La densidad POSITIVA auxiliar es

    p_v(y)=exp(vy)rho_N(y)/L_v,
    L_v=1/(norm² a_v^N).

Tiene media2Nv/a_v y varianza beta_v N/a_v², donde beta_v=2(u²+v²). Su modo y_* cumple q_N(y_*)=v y, por Riccati026,

    y_*=2dv/[a_v+q_N'(y_*)],
    0<=t_v−y_*<=2dvM_N/a_v²<=4u²/(u²−4)²,
    M_N=u²/(2N−3).

La última cota usa dM_N<=u² y v<=2. El control0<q'<M_N permite comparar p_v(t_v) con su máximo:

    p_v(t_v)>=p_v(y_*)exp[−M_N(t_v−y_*)²/2]
              >p_v(y_*)/2>=3/(32s_v),
    s_v²=beta_v N/a_v².

Chebyshev da la última cota del máximo; la localización y variación del modo justifican evaluarla en t_v. Uniformemente,8u^6/(u²−4)^4<1/100<log2 y s_v<sqrt(N)/22.

El transformado EXACTO es

    fhat_(c,v)(xi)=C_(c,v) exp(i xi t_v)
                (c+v−i xi)(a_v+xi²+2iv xi)^(-N),
    C_(c,v)=exp(−v t_v)/[norm² g_c(t_v)].

Riccati da q_N(t_v)>v, por lo que

    (C_(c,v)a_v^(-N))(c+v)<=32s_v/3<sqrt(N)/2.

Así el factor Fourier se absorbe por

    |c+v−i xi|/(c+v)<=sqrt(1+xi²),

pues c+v>=1. No se pierde una constante al variar v o c. El módulo del denominador al cuadrado es a_v²+beta_v xi²+xi^4.

Con a_v en[3953/4,992], beta_v en[1985,3985/2], las mismas comparaciones038 prueban

    |fhat_(c,v)(xi)|<=sqrt(N)exp(−Nxi²/1000), |xi|<=1,
    int_(|xi|>=1)|fhat_(c,v)(xi)|d xi/(2pi)
                  <65sqrt(N)exp(−N/2000), N>=16.         (GAMMA)

El script comprueba exactamente las cotas extremas: beta_v/(a_v²+beta_v+1)>1/500, beta_v/a_v²>1/500 y s_v<sqrt(N)/22. La prueba de la cola reserva la potencia N/4>=4, como038.

## 5. Producto INFINITO firmado conservado

Defina el operador absolutamente convergente

    M_sigma f(ell)=U_sigma^(-1)sum_(n>=1)mu(n)n^(-sigma)
                                                   f(ell+logn).

Los f_(c,v) son acotados y tienen Fourier integrable; sum n^(-sigma)<infinito justifica Fubini. El multiplicador es el producto Euler infinito Z_sigma(i xi)/U_sigma. Su logaritmo centrado admite la serie ABSOLUTA

    log[Z_sigma(i xi)/U_sigma]+iA_sigma xi
      =−sum_p sum_(k>=1)
        [exp(ik xi logp)−1−ik xi logp]/[k p^(k sigma)].

Por |exp(it)−1−it|<=t²/2 su módulo es <=B_sigma xi²/2. Aplicar exactamente el corte Fourier038 y (GAMMA) prueba

    |M_sigma f_(c,v)(0)−f_(c,v)(−A_sigma)|
      <=12000B_sigma/N
        +65sqrt(N)[(1+1/delta)^2+1]exp(−N/2000),          (INFINITE)

si N>=16 y B_sigma<=N/1000. No hay un grupo Q finito ni una suma exterior coprima omitida en esta desigualdad. No se aplica Jensen a una medida firmada.

## 6. Perfil trasladado en su lado físico

Ponga L=1000 y suponga

    N>=4L²=4,000,000,
    L/sqrt(N)<=delta<=3/2,
    v=1/2+delta.

De(MOMENTS), A:=A_sigma<=5/delta y B_sigma<=5/delta². Además t_v>=d/992>=N/(2·992), mientras A<=5sqrt(N)/L. La desigualdad L²>5·992 prueba t_v>A en todo el rango. El argumento trasladado t_v−A es POSITIVO; no se toma el signo de la extensión izquierda de f.

Riccati, q'>0 y q'<M_N dan

    f_(c,v)(−A)>=(1−M_N A)exp(−M_N A²/2).

En efecto q(t_v)>=v, q(t_v−s)>=v−M_Ns y el cociente(c+q(t_v−A))/(c+q(t_v))>=1−M_NA, porque c+q(t_v)>=1. Con M_N<=u²/N,

    f_(c,v)(−A)>1−15u²/L².

Para el upper, q(t_v)−v<=M_Nv/(u²+v²)<=2M_N/u² y el cociente anterior es<=1. Así

    f_(c,v)(−A)<=exp(5/L²)<=1/(1−5/L²).

## 7. Signo completo del inverso en todos los centros inclinados

En el rango anterior, B_sigma/N<=5/L²<1/1000 y el primer error de(INFINITE) es<=60000/L²=.06. El segundo es<1/200. Para probarlo sin estimación numérica de exponenciales, use delta<=3/2 y delta>=L/sqrt(N):

    [(1+1/delta)^2+1]<=17/(2delta²),
    exp(−N/2000)<=6(2000/N)^3.

En N>=4L² resulta un mayorante3315·10^9/L^5<1/200. Las comparaciones racionales finales dan

    9/10<M_sigma f_(c,v)(0)<11/10.

Por(FULL), para cada v en[1/2+1000/sqrt(N),2] y sigma=1/2+v,

    (9/10)U_sigma<h_N(e^t_v)/H_N(e^t_v)<(11/10)U_sigma,
    (9/10)U_sigma<K_N(e^t_v)/G_N(e^t_v)<(11/10)U_sigma.    (SHOULDER)

Son los inversos COMPLETOS, con todos los enteros Möbius. PRODUCTS da además el lower explícito(9/10)delta/(1+delta)>0. No es un signo de una agrupación truncada.

## 8. Positividad en TODA la cola y comparación correcta con026

La función v->t_v=2dv/(u²−v²) crece estrictamente. Por tanto SHOULDER cubre todos los t entre T_N=t_(1/2+1000/sqrtN) y t_2.

Para t>=t_2, q_N(t)>=2. El cociente de dilatación común a ambos inversos tiene derivada logarítmica

    d/dell log[e^(−ell/2)g_c(t+ell)/g_c(t)]
       =−1/2−q_N(t+ell)+q_N'(t+ell)/(c+q_N(t+ell))<-2,

porque M_N<=u²/N<5/4 y c+q>=5/2. Cada término n>=2 se acota por n^(-2), y la suma absoluta es<3/4. Luego ambos cocientes completos son>1/4 en TODO t>=t_2.

Se concluye para TODOS N>=4,000,000 y TODO x>=exp(T_N):

    h_N(x)>0, K_N(x)>0.                                (TAIL)

Para L fijo,

    T_N=(N−1)/992+(1985L/992²)sqrt(N)+O(1).

Además v_N<=1 en el rango declarado, por lo que T_N<=2d/(u²−1)<d/330. Los dos cortes de K026 son>d/330: t_J directamente y t_R porque Q_d>3/2. Así TAIL mejora legítimamente el corte del MISMO K_N; también mejora el corte previo020 de h_N. No se atribuye a h_N un teorema que026 sólo probaba para K_N.

## 9. Alcance del resultado

La nueva cota controla por primera vez el producto infinito firmado en un hombro energético y la cola posterior. El inverso puede seguir tomando signos en la región interior no cubierta; no se afirma signo en el centro crítico delta0 ni se elimina esa restricción sigma>1.

La representación F_N=2int h_N B conserva una cola favorable al tener B<0, pero no se ha comparado su magnitud con la parte adversa interior o con ARCH_sharp. En particular no se afirma W>=0, nueva fila o nueva ventanaT. La precisión del residuo polar−peine completo sigue siendo una obligación adicional; SHOULDER no se vende como un error relativo suficiente de W.

Verificador: tools/power_infinite_shoulder_039_verify.py, Fraction/intervalos para constantes uniformes, cota aritmética y umbrales; PASS. No evalúa W en nuevos N ni enumera primos. La auditoría independiente confirma c,v, normalización, inversión infinita, condiciones físicas y positividad de toda la cola. Revisión adversarial adicional del constructor paralelo aprobada. Papers intactos.
