# POWER_CRITICAL_BALANCE_040 — Factor elemental del producto infinito y signos cerca del centro

Estado: **PROVED, núcleo y CONSTANT-CUTOFF aprobados por auditoría independiente**. Ver [POWER_CRITICAL_AUDIT_040.md](POWER_CRITICAL_AUDIT_040.md). Tasa fija u=63/2. Papers intactos.

Resultados: expansión del inverso aritmético COMPLETO con resto explícito O(delta³+N^(-3/2)) y cola exponencial; en delta=N^(-2), signos OPUESTOS uniformes de h_N y K_N cerca del centro energético. No se afirma signo de W.

## 1. Corpus y diferencia precisa

Consultados ROUTES-TRIED-INDEX/README.md, grid maestro y CROSSWORD-TO-D; leídos INVERSE_KERNEL020, UNIFORM_CUTOFF026, SIGNED_MOMENTS038 e INFINITE_SHOULDER039. Las fórmulas de Euler–Maclaurin y el principal de la suma Euler son conocidos; no se presentan como herramientas nuevas.

La diferencia respecto038/039 es conservar el FACTOR elemental del recíproco Euler en sigma=1+delta antes de invertir Fourier. No se centra mediante A_sigma y B_sigma divergentes cuando delta baja a escala1/N. La cota resulta ABSOLUTA para el cociente completo del inverso y es menor que su escala1/N en el régimen analizado, en lugar de un error relativo que no decide el signo. Sólo se usan el integral de la parte fraccionaria y productos absolutamente convergentes en sigma>1.

## 2. Factor local con resto explícito

Para Re z>0,

    zeta(1+z)=1/z+H(z),
    H(z)=1−(1+z)int_1^infty {x}x^(−2−z)dx.

Esta identidad sale de la suma de floor(x) por integración por partes. Además H(0)=gamma: integrar hasta un entero M da int_1^M{x}x^(-2)dx=logM−H_M+1.

Para Re z>=0, |z|<=1/8, el integral tiene módulo<=1 y su diferencia respecto al valor en0 es<=|z|, porque int_1^infty logx x^(-2)dx=1. Por tanto

    |H(z)|<=17/8,
    |H(z)−gamma|<=2|z|,
    |zH(z)|<=17/64<1.

Expandir una fracción geométrica con DENOMINADOR controlado da

    1/zeta(1+z)=z−gamma z²+R3(z),
    |R3(z)|<=9|z|³.                                    (LAURENT)

En efecto R3=−z²(H−gamma)+z³H²/(1+zH), y2+(17/8)²/(1−17/64)<9. No se postula una serie formal sin resto.

## 3. Perfil gamma y razón completa del inverso

Conserve039: d=N−1, c en{1/2,3/2}, rho_N par, q=−rho'/rho para argumento positivo,

    g_c(t)=c rho_N(t)−rho_N'(t),
    v=1/2+delta, a_v=u²−v², t_v=2dv/a_v,
    f(ell)=exp(vell)g_c(t_v+ell)/g_c(t_v).

La extensión izquierda de f no se considera una probabilidad. En sigma=1+delta>1, el inverso COMPLETO correspondiente tiene cociente

    R_c(t_v)=sum_(n>=1)mu(n)n^(−sigma)f(logn).

Para c1/2 éste es h_N(e^t_v)/H_N(e^t_v); para c3/2 es K_N(e^t_v)/G_N(e^t_v), con las normalizaciones039. f(0)=1.

Fourier039 conserva la fórmula exacta y los bounds uniformes, para v en[1/2,2]:

    |fhat(xi)|<=sqrt(N)exp(−Nxi²/1000), |xi|<=1,
    |fhat(xi)|<sqrt(N)/2 ·sqrt(1+xi²)
       [1+beta_v xi²/a_v²+xi^4/a_v²]^(-N/2),
    beta_v=2(u²+v²), beta_v/a_v²>1/500.

La normalización usa la norma del átomo gamma original. El multiplicador infinito es1/zeta(1+delta−i xi); su serie Euler es absoluta porque delta>0. No se descarta ningún entero Möbius.

## 4. Inversión con factor lineal y cuadrático: cota uniforme

Suponga N>=24 y0<delta<=1/16. En |xi|<=1/16, z=delta−i xi pertenece a |z|<=1/8, y LAURENT se aplica. Al invertir los polinomios z,z² aparecen exactamente

    delta f(0)−f'(0),
    delta²f(0)−2delta f'(0)+f''(0).

Se obtiene

    R_c(t_v)=delta−f'(0)
          −gamma[delta²−2delta f'(0)+f''(0)]+E_N,          (EXPANSION)
    |E_N|<=288delta³+9·10^6/N^(3/2)
                  +110000sqrt(N)delta^(-1)exp(−N/10^6). (REMAINDER)

Prueba del centro. La desigualdad |delta−i xi|³<=2(delta³+|xi|³), LAURENT y los integrales gaussianos039 dan

    int_R sqrt(N)exp(−Nxi²/1000)d xi/(2pi)<16,
    int_R sqrt(N)|xi|³exp(−Nxi²/1000)d xi/(2pi)
                                       <500000/N^(3/2).

Multiplicar por18 prueba los dos primeros errores.

Para la cola |xi|>=1/16, la suma Euler absoluta da |1/zeta|<=1+1/delta; el polinomio z−gamma z² se acota junto con ella por(4/delta)(1+xi²). Se separa la potencia gamma en dos mitades y se reserva N/4>=6. La mitad extraída es<=exp(−N/10^6), pues log(1+(1/500)(1/16)²)>1/250000. El integral auxiliar de(1+|xi|)(1+xi²)(1+xi²/500)^(-6) en R es<110000. Sus cuatro monomios se acotan por92,100,46000,62500. Incluir el prefactor sqrt(N)/2 y2pi da el último error de REMAINDER.

Todas las integraciones son absolutas. La cota de cola usa delta>0; no se elimina esa condición por una continuación informal.

## 5. Nueva desigualdad elemental de curvatura gamma

Además de q''<0 ya probado031, se tiene

    −2q'(t)/t<q''(t)<0, t>0.                            (CURVATURE)

Prueba. Con P_N positivo grado d y pesos p_jt^j/P_N(t),

    t²q'=EJ−Var(J)<d.

Defina S=q''+2q'/t. Diferenciar Riccati026 muestra que en cualquier punto S=0,

    S'=2q'[q'−(2d+1)/t²]<0.

Por otro lado P_N da la expansión algebraica

    q=u−d/t+d(d+1)/(2ut²)+O(t^(-3)),
    S=d(d+1)/(ut^4)+O(t^(-5))>0 al infinito.

Si S tuviera algún valor no positivo antes, debería volver a ser positivo, pero en TODO contacto S0 su derivada es negativa; se excluyen también tangencias. Luego S>0. Esto prueba CURVATURE sin una desigualdad especial de Bessel.

Derivar Riccati y combinar sus dos cotas de curvatura da

    d q/[t(qt+d+1)]<q'<d q/[t(qt+d)].                    (SLOPE)

Ésta proporciona una escala inferior efectiva para comparar REMAINDER, no sólo una asintótica formal.

## 6. Derivadas exactas del perfil en el centro inclinado

Escriba q=q_N(t_v), b=q_N'(t_v), epsilon=q−v>0. Riccati se factoriza:

    b=epsilon(q+u²/v),
    eta:=epsilon/b=v/(u²+vq).

Por diferenciación directa,

    f'(0)=b[1/(c+q)−eta],
    f''(0)=−b+q''/(c+q)
                    +b²[eta²−2eta/(c+q)].              (DERIVATIVES)

En el régimen delta=N^(-2), N>=2^80, v<=1, q<2, eta<=1/u² y t_v>=N/(2·992). CURVATURE, b<=M_N<=u²/N y c+q>=1 prueban

    −b(1+3970/N)<f''(0)<−b,
    0<f'(0)<b/(c+1/2),
    f'_(c=1/2)(0)>=b[1−2/N−1/u²].                     (BOUNDS)

Para el lower de b, usar SLOPE, q>=1/2, t_v<=2d/(u²−1)<d/400 y qt_v+d+1<3d. Luego

    b>50/N.                                            (LOWER-b)

Las constantes son deliberadamente holgadas; no se evalúa un N concreto.

## 7. Patrón de signos cerca del centro energético

Con delta=N^(-2), REMAINDER prueba para TODOS N>=2^80

    |E_N|<10^(-4)/N.

El primer término es directo; para el exponencial se usa exp(−x)<=6!x^(-6), de modo que N veces la cola queda acotada por110000·6!·10^36/N^(5/2). Todo se compara racionalmente en el extremo monótono2^80.

Las cotas57/100<gamma<3/5 y BOUNDS/LOWER-b, sustituidas en EXPANSION, dan los signos

    h_N(e^t_v)/H_N(e^t_v)<−1/N,
    K_N(e^t_v)/G_N(e^t_v)>1/N,                           (CENTRAL-SIGNS)
    v=1/2+N^(-2), N>=2^80.

Para c3/2, los términos delta y2gamma delta f' son favorables, −gamma f''>=gamma b y f'<=b/2; el beneficio es al menos(gamma−1/2)b, mayor que los errores. Para c1/2, el upper es

    delta+b{−1+1/u²+2/N+(3/5)(1+3970/N)
                    +(6/5)delta}+|E_N|,

estrictamente menor que−1/N mediante b>50/N y el resto citado. El término−gamma delta² sólo mejora ese upper.

Estos son signos del inverso COMPLETO en un centro que satisface t_v=d/992+O(1/N). No se identifica aún el punto exacto de transición en t ni se afirma un signo de W. Las sumas firmadas se conservan antes del resto; ninguna conclusión procede de una medida firmada tratada como probabilidad.

## 8. Corte uniforme a distancia constante

Para TODOS N>=2^80 y

    2000/N <= delta <= 1000/sqrt(N),

valen v<1, q<2, 0<f'<b y f''<−b por las mismas identidades exactas. Como 0<gamma<1, EXPANSION implica

    R_c(t_v)>=delta−u²/N−delta²−|E_N|.

Las constantes racionales verificadas en el script dan, uniformemente en ese intervalo,

    delta<1/1000,
    288delta³<delta/1000,
    9·10^6/N^(3/2)<1/(10000N),
    110000sqrt(N)delta^(-1)e^(−N/10^6)<1/(10000N).

Para la última desigualdad basta exp(−x)<=6!x^(−6) y delta>=2000/N: N veces el término es a lo sumo 55·6!·10^36/N^(7/2). Luego

    R_c(t_v)> (998/1000)delta−(u²+1/5000)/N>0,

pues delta>=2000/N. Esto cubre ambos c y TODOS los centros t_v de ese intervalo. En el extremo superior enlaza con el teorema039, válido para todos los t posteriores. Por tanto

    h_N(e^t)>0 y K_N(e^t)>0
    para TODO t>= (N−1)/992+5, N>=2^80.             (CONSTANT-CUTOFF)

En efecto, si delta0=2000/N, la diferencia exacta entre el primer centro y d/992 es

    t_(1/2+delta0)−d/992
       =d·delta0·(1985+delta0)/(992·[u²−(1/2+delta0)²])<5,

usando d·delta0<2000, delta0<1 y u²−v²>=u²−1. La conclusión es un corte suficiente, no la ubicación exacta de ninguna transición. Mejora el hombro O(sqrt(N)) de039 para los mismos objetos completos h y K; tampoco decide W.

## 9. Alcance y validación

La prueba controla por primera vez una escala1/N del inverso infinito en el centro, donde039 sólo daba signo en un hombro O(sqrt(N)). CENTRAL-SIGNS y CONSTANT-CUTOFF fueron aprobados independientemente por root y mapa; el verificador exacto reproduce PASS. La región interior integral y el balance con ARCH_sharp siguen pendientes; un h_N negativo localmente no implica W negativo.

No hay campañas de N, m o primos. La prueba usa el factor local explícito, integrales gamma y desigualdades uniformes. La auditoría hostil revisó el resto LAURENT, normalización Fourier, CURVATURE, factores de DERIVATIVES, comparaciones de signos y enlace con039. Papers intactos.
