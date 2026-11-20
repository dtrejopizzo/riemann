# POWER_AUDIT_002 — Polarización desde cero y puente de aproximación

Estado: PROVED (polarización y puente para datos suaves con decaimiento); OPEN (signo para tres o más potencias). Auditoría independiente. No modifica papers.

Se consultaron las reglas del proyecto, POWER_CONE_001.md, índice README (entrada actual de potencias y antecedentes Pick), grid R162_2300_part3/part5 y CROSSWORD-TO-D.md. Se respeta el problema aislado del signo. La razón nueva es comprobar los cruces de una familia explícita y construir su aproximación en una topología que controla cada término; no se descarta la construcción por etiquetas de reformulación.

## 1. Cruces: no hay defecto polar

Escriba h_u(y)=exp(-uy) para y>0, cero fuera, u=a-1/2. Para v=b-1/2, la autocorrelación bilineal simétrica es

    C_uv(t)=[exp(-ut)+exp(-vt)]/[2(u+v)], t>=0.

Esto sale de integrar cada uno de los dos productos trasladados sobre la semirrecta. Defina

    g(a)=psi(a/2)/2-log(pi)/2+zeta'(a)/zeta(a),
    r(a)=1/a+1/(a-1), L(a)=g(a)+r(a).

Los términos arquimediano y de peine de la polarización son [g(a)+g(b)]/(a+b-1). Los momentos son A_a=1/(a-1), B_a=1/a; por tanto el polar bilineal es

    P_ab=A_a B_b+A_b B_a
        =1/[(a-1)b]+1/[(b-1)a]
        =[r(a)+r(b)]/(a+b-1).

La última identidad se comprueba multiplicando por a(a-1)b(b-1)(a+b-1); también resulta al factorizar su numerador (a+b-1)(2ab-a-b). De aquí

    W(h_u,h_v)=[L(a)+L(b)]/(a+b-1).

Para rho_a(X)=X^-a, Z rho_a= zeta(a) h_u. Por ello los coeficientes correctos son d_i=c_i zeta(a_i), y Q[rho]=sum d_i d_j K_ij tal como declara POWER_CONE. Revisados desde cero el factor 2 del polar, la autocorrelación y el peine: no se requiere corrección. En diagonal Q[rho_a]=zeta(a)^2 L(a)/(a-1/2).

## 2. Resultados conservados y alcance

El criterio de dos puntos, la estimación L-uL'>0 para a>=32 y su consecuencia sobre cada plano de dos potencias sobreviven. En la estimación gamma puede obtenerse primero la cota más precisa .5log(a/(2pi))-.5-7/(4a)+1/(2a^2), que implica la usada. La cota de S resulta de Lambda(n)<=log n<=n. No se infiere signo de orden tres.

El falsificador H=3+cosh tiene, para u=log2,v=2log2,

    (log2)K=[[3/17,126/697],[126/697,15/82]],
    det((log2)K)=-387/971618,
    (42,-41)K(42,-41)^t=-129/(34log2).

Refuta exclusivamente el paso desde una representación cosh positiva al signo de todas las mezclas. No refuta el dato aritmético.

## 3. Puente probado en una norma que controla la forma

Fije 1/2<eta<31.5 y el espacio H_eta de funciones h sobre [0,infinito) tales que exp(eta y)h pertenece a H^1(0,infinito), con su norma habitual. La forma universal W de la extensión por cero es continua en H_eta:

* El término arquimediano está controlado porque la extensión por cero H^1(0,infinito) -> H^s(R) es continua para 0<s<1/2, y |m(tau)|<=C_s(1+tau^2)^s. No se presupone que la extensión por cero sea H^1: puede tener salto en cero.
* Para t>=0, Cauchy--Schwarz da |c_h(t)|<=exp(-eta t)||exp(eta y)h||_2^2. Por polarización se controla también la diferencia de dos formas. La suma del peine converge, pues sum v_n n^-eta=2 sum Lambda(n)n^-(eta+1/2)<infinito.
* A y B son funcionales continuos por Cauchy--Schwarz, ya que eta>1/2.

El span lineal de {exp(-(31.5+k)y): k=0,1,...} es denso en H_eta. Prueba constructiva: las funciones suaves de soporte compacto en [0,infinito) son densas en H_eta (sin imponer valor cero en el extremo). Para una de ellas ponga z=exp(-y), h(y)=z^31.5 f(z). La función f es suave en [0,1], idénticamente cero cerca de cero. Aproxime f y f' uniformemente por un polinomio P y su derivada: aproxime f' por un polinomio y luego integre ajustando f(0). Entonces

    |z^31.5(f-P)| <= epsilon z^31.5,
    |d/dy[z^31.5(f-P)]| <= (31.5+1)epsilon z^31.5.

La integral ponderada converge porque eta<31.5. Esto prueba la aproximación en H_eta. Cada aproximante es imagen Z de una combinación finita de X^-(32+k), dividiendo su coeficiente exponencial por zeta(32+k)>0.

**Consecuencia exacta:** si se prueba positividad de TODAS las matrices finitas de potencias con exponentes 32+k, se obtiene signo de W para todo h en H_eta por continuidad. En particular se transporta a cualquier dato exterior cuyo Zrho pertenezca a H_eta. Para rho suave de decaimiento rápido y derivadas de decaimiento rápido, esto se verifica sumando la serie de Z y su derivada: para todo M>1, son O(exp(-(M-1/2)y)).

Este puente es un resultado positivo de aproximación, no una prueba del signo de las matrices. Los aproximantes pueden requerir arbitrariamente muchos generadores y coeficientes de ambos signos. El resultado existente sobre una unión de planos no autoriza su paso al límite. Tampoco se afirma aquí que todo representante C^2 de PW_N esté en H_eta: deben tratarse su regularidad y decaimiento concretos, o trabajar sobre un núcleo suave y justificar después la clausura pertinente.

## 4. Próxima obligación matemática

El cuello constructivo de esta ruta queda localizado: demostrar el signo de matrices de orden tres y después una estructura para todos los órdenes. El puente de aproximación ya está disponible para datos suaves; no hay que inventarlo de nuevo ni confundirlo con una inferencia desde menores de orden dos. Mantener separados signo universal, restricciones PW_N y coercividad respecto del gauge.

## 5. Ampliación revisada: el puente fraccionario cubre PW_N C²

POWER_BRIDGE_002.md (constructor casos) resuelve la limitación de regularidad de §3. Revisión independiente: APROBADO. Su norma es ||e^(5y/4)rho(e^y)||H^(1/4)(0,infinito). Dos integraciones por partes, tanto para h como para xh, dan rho,rho'=O(X^-2) para el dato PW_N C². Por ello G=e^(5y/4)rho(e^y) satisface |G|<=Ce^(-3y/4), |G'|<=Ce^(y/4). Para 0<delta<1, dividir en R=log(1/delta) da

    integral_0^R |Delta_delta G|² <= C delta² exp(R/2)=C delta^(3/2),
    integral_R^infinito |Delta_delta G|² <= C exp(-3R/2)=C delta^(3/2).

El seminorma H^t es finito para t<3/4; la extensión por cero es continua para t<1/2. Lo crucial es NO derivar la serie Z término a término: rho'=O(X^-2) no daría convergencia absoluta de esa derivada. En su lugar,

    e^(3y/4)Zrho(y)=sum n^(-5/4) G(y+log n)

converge en H^(1/4) por la propiedad de contracción de cada traslación hacia adelante. Esto controla la forma, peine y polos como demuestra B1/B2 del memo. La aproximación polinómica de §3 del mismo memo produce exponentes 33.25+k, todos >=32, y converge en esa norma. Por tanto el puente a TODO PW_N C² queda probado. No afirma todavía signo de las matrices de tamaño arbitrario.

## 6. Puente directo por traslación para el signo de ventanas

Hay también una consecuencia más directa del puente H_eta de §3. Si el kernel es positivo en TODOS los tamaños para exponentes 32+k, W es no negativa en todo H_eta por densidad. Para cualquier F suave de soporte compacto en la recta, trasládelo suficientemente a la derecha para que su soporte esté en (0,infinito). El trasladado pertenece a H_eta. La forma completa es invariante por traslación: archimedeano y peine lo son por autocorrelación, mientras A multiplica por e^(d/2) y B por e^(-d/2), conservando su producto. Así se obtiene W(F)>=0 para cualquier tal F. En cada ventana fija la continuidad en la norma de forma y densidad del núcleo suave extienden esa desigualdad al dominio de la forma; en P_T los momentos se anulan y queda el signo requerido de a_T.

Esta es una implicación constructiva condicional desde TODOS los tamaños del kernel de potencias. No requiere una cota coerciva respecto del gauge ni un margen positivo. La demostración existente de tamaño dos o tres no satisface todavía la hipótesis.

## 7. Auditoría del avance de tres generadores

POWER_THREE_002.md revisado desde sus fórmulas: APROBADO para u>=2^30 y tres tasas en [u,3u]. La base racional ortonormal escrita corresponde a la convención Fourier con exp(-i tau y); el multiplicador m es par y el cálculo es independiente de esa elección. La suma de envolventes de los tres vectores es sqrt(6u)e^(-uy)(3+18uy+18(uy)^2). La constante 327, la cota de cola y la estimación del peine siguen. Para verificar 654sqrt(6)<1602 basta 267²>6*109²; en p=16 su cota del peine es menor que .028. El polar está acotado por 12*366²/u<.1 en el rango. La densidad espectral tiene máximo 3/(pi u), y el principio de llenar primero el intervalo central minimiza integral log|tau|, dando el término log(pi u/6)-1 con el factor dos correcto. La cota arquimediana resultante es >10||f||². Por tanto el margen declarado Q>=9||f||² está justificado.

No requiere separación mínima de tasas. La base all-pass sigue siendo válida para tasas repetidas como base del espacio confluyente de exponenciales por polinomios. Este resultado de orden tres se conserva como avance positivo acotado, sin inferir todos los órdenes.

## 8. Revisión de todos los órdenes con umbral creciente

POWER_THREE_002 §§7–8: APROBADO. La identidad de convoluciones produce exactamente P_n(z)=sum_{k=0}^{n-1} binom(n,k+1)6^k z^k/k!, y z^k/k!<=2^k e^(z/2) da P_n<=13^n e^(z/2). La integración del polinomio antes de aplicar la envolvente da el momento 2sqrt(6)13^n/sqrt(u). Las cotas del polar 48*169^n/u y del peine <15*16^n*2^(-20n-10) son válidas para u>=2^(40n), y cada una es <.1. El argumento espectral da arch>10; el margen W>=9||f||² se conserva para todo n con ese umbral.

La no-densidad declarada también es exacta: toda dirección unitaria de la unión tiene norma sobre [1,infinito) <.01. Para un test unitario sobre [1,2], el producto escalar con cada dirección es <.01; su distancia a cada recta real generada por tal dirección es >=sqrt(1-10^-4). Por tanto la unión con escalares arbitrarios no es densa. Esto no descarta la estrategia general de potencias: localiza la obligación pendiente en una familia común de tasas o en control de cruces entre familias ya positivas.

## 9. Afinamiento a la escalera exacta e inversión finita

POWER_BRIDGE_002 actualizado escoge B=123/4 en su aproximación polinómica, por lo que los exponentes son exactamente 32+k (sustituye el rango auxiliar 33.25+k citado en §5 de esta auditoría). El cambio conserva todas las cotas de densidad porque B>0.

Su nuevo §6, revisado independientemente, proporciona además una realización finita para todo test h suave soportado en (0,L): u(y)=sum mu(n)n^-1/2 h(y+log n), rho(e^y)=e^-y/2 u(y). Al aplicar Z, sólo contribuyen pares kn<=e^L. Reagrupar es finito y la suma de mu sobre divisores da Zrho=h. La pertenencia a B es inmediata porque u es suave hasta cero y compacto en la semirrecta. No hace falta suponer sobreyectividad de un operador infinito.

Queda así una obligación suficiente explícita: probar semidefinitud de K^(m)_ij=[L(32+i)+L(32+j)]/(63+i+j), 0<=i,j<=m, para todos los enteros m. Este paso todavía no está probado. Tanto la aproximación como su enlace con todo test de ventana sí están demostrados, sin exigir un margen positivo ni coercividad sobre gauge.

## 10. Certificado racional de la escalera fija, ronda 003

Revisados tools/power_fixed_grid_003.py y POWER_FIXED_GRID_003.md: APROBADOS. Reejecución independiente de python3 reproduce los seis pivotes positivos y los seis parámetros de Schur del memo, incluyendo el sexto pivote entre 70566563152624/10^30 y 70566563152625/10^30. Las verificaciones de signo operan sólo con Fraction y redondeo dirigido a 10^-60; los float del método __repr__ no intervienen en las verificaciones ni en las salidas certificadas normales.

Detalles auditados: serie atanh de log con primer término omitido de grado 241 y cola geométrica; fórmula Machin y resto alternado positivo tras 100 términos; gamma por Euler–Maclaurin de H_1000 con B_2,...,B_24 y cota siguiente B_26=8553103/6; recurrencias de psi en enteros y semienteros; colas de zeta y de su derivada mediante integrales desde 50, válidas por monotonía en a>=32. En LDL in-place la actualización sólo modifica entradas con índices i,j>k, por lo que la columna k que multiplica cada corrección permanece intacta durante todo ese paso. La recurrencia escalar tampoco modifica su pivote q[r] durante la actualización de los sitios restantes. Las congruencias declaradas del kernel y su complemento son correctas.

El falsificador racional de POWER_FIXED_GRID_003 §4 también se recalculó: det=-332001/391435520 y los tres menores de orden dos coinciden con sus fracciones declaradas. Se conserva el alcance finito: no se extrapolan parámetros alternantes ni una cota uniforme desde seis casos.
