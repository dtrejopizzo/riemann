# POWER — Falla de la ordenación PSD por desplazamiento simultáneo

Estado: **PROVED analítico; revisiones matemáticas y literales root/casos/mapa/invariante aprobadas.** Sin nuevos datos, certificados numéricos ni modificaciones de papers. No es un valor negativo de la forma real W.

## 1. Antecedentes, objeto y diferencia

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX01–06 y README, R162_2300_MASTER_GRID y CROSSWORD-TO-D. Cotejados POWER_CONE_001, POWER_COMMON_TRANSFER_010, POWER_RECIPROCAL_PFAFFIANS_083, POWER_BRIDGE_002 y POWER_AUDIT_002.010 transporta cotas bajo hipótesis explícitas, no una ordenación PSD completa bajo desplazamiento común.083 aporta identidades de desplazamiento, no su signo.

Antecedente más cercano: phase188 N_BUILD_007, sección1(iv) y3(b), usa la diferencia entre un átomo en log2 y términos suaves O(epsilon) contra un resolvente causal. Allí la energía arquimediana diagonal log(1/epsilon) impedía inferir un falsificador de la forma completa. Aquí se compara la forma COMPLETA con su modulación e^(-2t); situar el primer paquete cerca de0 añade un factor O(epsilon) en su diagonal y permite pagar esa energía. No se atribuye novedad mundial a paquetes concentrados ni al argumento de continuidad.

Definir, para a,b>1,

 K(a,b)=[L(a)+L(b)]/(a+b-1),
 L(a)=1/a+1/(a-1)-log(pi)/2+psi(a/2)/2+zeta'(a)/zeta(a).

Se refuta la afirmación de que [K(a_i,a_j)-K(a_i+2,a_j+2)] sea PSD para TODOS los conjuntos finitos. Más precisamente falla en algún bloque inicial FINITO de la MISMA escalera a_i=32+i de002. No se especifica su tamaño ni se busca numéricamente.

## 2. Forma completa, continuidad local y parte suave

Se usa la forma causal W de001/002, extendiendo por0 a la recta. Para funciones reales suaves compactas, poner

 C_fg(h)=1/2 integral_R [f(x)g(x+h)+g(x)f(x+h)]dx,
 A(f)=integral f(t)exp(t/2)dt, B(f)=integral f(t)exp(-t/2)dt.

La forma bilineal tiene término arquimediano

 Arch(f,g)=C0 integral fg + integral_0^infinito Karch(h)[integral fg-C_fg(h)]dh,
 Karch(h)=2exp(-h/2)/(1-exp(-2h)),

peine -sum_(n>=2) v_n C_fg(log n), v_n=2Lambda(n)/sqrt(n), y polar A(f)B(g)+A(g)B(f). La fórmula Karch procede de P47main.tex líneas396–418, lema de la densidad de Levy. Es suave en cualquier compacto separado de h=0. La normalización y su identificación con K(a,b) para exponenciales están fijadas en001/002.

En cualquier intervalo compacto fijo I, para cada s>0 existe C_(I,s) tal que

 |W(f,g)|<=C_(I,s)||f||_(H^s(R))||g||_(H^s(R)).       (CONT)

En efecto |m(tau)|<=C_s(1+tau^2)^s controla la integral Fourier por Cauchy–Schwarz ponderado. Hay sólo FINITOS contactos compatibles con I; cada traslación es acotada en L2. Los dos momentos polares son acotados en L2(I). No se sustituye el peine por una envolvente infinita no sumable.

Para T f(t)=exp(-2t)f(t) en la semirrecta causal definir

 D(f,g)=W(f,g)-W(Tf,Tg).                              (DEF)

Es una forma continua en cada dominio local anterior y en H_eta de014, definido de nuevo en§5, con eta=3/4; T es acotado allí. No se supone ningún signo de W o D para deducir esta continuidad.

## 3. Dos paquetes completamente declarados

Elegir UNA función real phi suave, de soporte compacto en(0,1), con norma L2 igual1. Fijar ell=log2 y, para epsilon>0 suficientemente pequeño,

 f_epsilon(t)=epsilon^(-1/2)phi((t-epsilon)/epsilon),
 g_epsilon(t)=f_epsilon(t-ell).

Sus soportes están en(epsilon,2epsilon) y(ell+epsilon,ell+2epsilon). Son causales y contenidos en un intervalo fijo. No se cambian perfiles ni se evalúan puntos: se toma el límite epsilon hacia0 mediante cotas analíticas.

En el contacto h=ell,

 C_(f,g)(ell)=1/2.

La otra orientación no solapa. El soporte de C_(f,g) para h>0 está dentro de[ell-epsilon,ell+epsilon]. Para epsilon suficientemente pequeño ningún otro log n entra allí. Por tanto el peine cruzado es exactamente -v2/2. La parte arquimediana local C0 integral fg es0; su parte integral es O(epsilon), porque Karch está acotada cerca de ell y |C_fg|<=1/2. El polar también es O(epsilon), pues cada momento de cada paquete es O(sqrt(epsilon)). Se sigue

 W(f_epsilon,g_epsilon)=-v2/2+O(epsilon).

Para los paquetes modulados,

 C_(Tf,Tg)(ell)=exp(-2ell)/2 integral exp(-4t)f_epsilon(t)^2dt ->1/8.

Las demás contribuciones cruzadas suaves siguen siendo O(epsilon). Así

 D(f_epsilon,g_epsilon)->-3v2/8
                     =-3log2/(4sqrt2).               (CROSS)

Se ha conservado el contacto EXACTO de2 y todas las contribuciones del polar y del arquimediano; ninguna se omite por una presunta positividad.

## 4. Las diagonales del defecto no pagan ese cruce

Fijar s=1/8, aunque el argumento vale para0<s<1/4. El escalamiento Fourier de un paquete suave da

 ||f_epsilon||Hs+||g_epsilon||Hs=O(epsilon^(-s)).

Como el primer paquete está a distancia O(epsilon) de0,

 ||(1-exp(-2t))f_epsilon||Hs=O(epsilon^(1-s)).

Para justificar la segunda cota sin asumir un multiplicador pequeño sólo en L_infinito, tras cambiar t=epsilon(1+x) la función es epsilon^(1/2) veces

 [(1-exp(-2epsilon(1+x)))/epsilon]phi(x).

Esta familia tiene soporte compacto fijo y todas sus derivadas uniformemente acotadas. Su escalamiento Hs da la cota indicada. También ||Tf_epsilon||Hs=O(epsilon^(-s)).

Escribir h=f_epsilon-Tf_epsilon. Por bilinealidad exacta,

 D(f_epsilon,f_epsilon)=W(h,f_epsilon)+W(Tf_epsilon,h)
                     =O(epsilon^(1-2s)),

usando CONT. Para el paquete desplazado basta CONT y la acotación del multiplicador sobre su soporte fijo:

 D(g_epsilon,g_epsilon)=O(epsilon^(-2s)).

No se afirma que estas diagonales tengan un signo concreto. Su producto es O(epsilon^(1-4s)) y tiende a0. Junto con CROSS,

 det[D(f_i,f_j)]_(f1=f_epsilon,f2=g_epsilon)
       ->-9(log2)^2/32<0.                            (NEGATIVE)

Por tanto para algún epsilon positivo FINITO la forma D tiene un plano indefinido. Esto no es una dirección negativa de W.

## 5. Transferencia a la escalera fija sin confundir coeficientes

Fijar ese epsilon. Los dos paquetes son suaves compactos en(0,infinito). Sea u0=63/2, eta=3/4 y X_eta={f:exp(eta t)f pertenece H1(0,infinito)}, norma usual. Para un paquete h poner x=exp(-t),

 q(x)=x^(-u0)h(-log x).

Es suave de soporte compacto en(0,1). Aproximar q en C1[0,1] por polinomios P: aproximar q' uniformemente por polinomios e integrar ajustando el valor en0. Si ||P-q||C1<=delta, entonces para h_P(t)=exp(-u0t)P(exp(-t)),

 |h_P-h|<=delta exp(-u0t),
 |(h_P-h)'|<=(u0+1)delta exp(-u0t).

Las integrales con peso exp(2eta t) convergen porque u0>eta; así h_P->h en X_eta. Este argumento es la densidad directa de002/014 y mantiene los coeficientes reales.

W es continua en X_eta: el arquimediano por extensión por0 a Hs,0<s<1/2; el peine por |C_f(t)|<=exp(-eta t)||exp(eta t)f||2^2 y sum Lambda(n)n^(-eta-1/2)<infinito; el polar porque eta>1/2. T es acotado en el mismo espacio. Por ello las matrices D de aproximantes de ambos paquetes convergen entrada a entrada y conservan el determinante negativo para aproximantes FINITOS suficientemente próximos.

Cada aproximante pertenece a span{exp(-(u0+j)t):0<=j<=N} para algún N finito común. Para e_j(t)=exp(-(u0+j)t) en t>0,

 W(e_i,e_j)=K(32+i,32+j),
 W(Te_i,Te_j)=K(34+i,34+j).

Los MISMOS coeficientes aproximantes se usan después de T. No se reemplazan por coeficientes de rho ni por coeficientes multiplicados por zeta: aquí son exponenciales causales DIRECTAS. La matriz D sobre su plano es una compresión por congruencia del bloque inicial

 [K(32+i,32+j)-K(34+i,34+j)]_(0<=i,j<=N).

Ese bloque no puede ser PSD. La existencia de N es una conclusión analítica finita de continuidad; no un certificado buscado por barrido.

## 6. Alcance

Queda refutada la ordenación PSD universal K-K_shift con desplazamiento simultáneo2, incluso en la escalera fija suficiente002. La dirección contraria tampoco puede ser PSD universal: por073, M(u)/u decrece estrictamente, así K(a+2,a+2)-K(a,a)<0 para todo a>1. Esta observación escalar no se usa para NEGATIVE.

No se ha probado W negativa, ni una matriz K indefinida, ni el fracaso de otros transportes restringidos. No se descartan normalizaciones diferentes con hipótesis nuevas y prueba propia, otros tamaños de desplazamiento no tratados aquí, ni un control firmado conjunto más fino. No se añade ventana T ni torre finita. El histórico010 y todos los resultados positivos permanecen intactos.


## 7. Resto IMS exacto: ni signo ni desaparición por telescopado

**PROVED analítico; revisiones matemática y literal aprobadas.** Antecedente directo: L2_BUILD004§§1–2 ya da la identidad IMS no local y conserva el peine como acoplamiento. No se presenta esa identidad como un principio nuevo. Aquí se evalúa su resto para el MISMO defecto de modulación de§2 y los MISMOS paquetes de§3, incluyendo el polar.

Poner T(t)=exp(-2t), S(t)=sqrt(1-T(t)^2), t>0, y

 d(t,s)=1-T(t)T(s)-S(t)S(s)
       =.5[(T(t)-T(s))^2+(S(t)-S(s))^2].

Entonces 0<=d(t,s)<=1. Para f real suave de soporte compacto en(0,infinito), definir

 R[f]=D[f]-W[Sf]=W[f]-W[Tf]-W[Sf].

S no es Lipschitz uniforme junto a0; aquí cada soporte es compacto SEPARADO de0 y S es suave en su entorno. No se extiende sin análisis de dominio a funciones arbitrarias no nulas en0. La cancelación T²+S²=1 elimina exactamente el término local C0. Las partes restantes son

 R_arch[f]=-integral_(h>0) Karch(h) integral d(t,t+h)f(t)f(t+h)dt dh,
 R_comb[f]=-sum_(n>=2)v_n integral d(t,t+log n)f(t)f(t+log n)dt,
 R_polar[f]=integral integral 2cosh((t-s)/2)d(t,s)f(t)f(s)dt ds.   (IMS)

Las integrales t,s se restringen a la semirrecta. Cerca de la diagonal d=O(|t-s|²) en cada soporte separado de0, que hace absolutamente convergente la parte arquimediana singular. Sólo hay finitos contactos. El polar y todos sus cruces están incluidos.

Aplicar IMS a f_epsilon,g_epsilon de§3. Sobre t,s en(epsilon,2epsilon), |S'|<=C epsilon^(-1/2), luego d(t,s)<=C|t-s|²/epsilon. Como Karch(h)=O(1/h) cerca de0 y la desigualdad de Cauchy–Schwarz da integral |f(t)f(t+h)|dt<=1, incluso si phi cambia de signo,

 |R_arch[f_epsilon]|<=C/epsilon integral_0^epsilon h dh=O(epsilon).

El peine diagonal es0 por anchura<log2. El polar diagonal es O(epsilon²): d<=C epsilon y ||f||1²=O(epsilon). Por tanto R[f_epsilon]=O(epsilon). Sobre el paquete g, separado de0 por ell, T,S tienen derivadas uniformemente acotadas, d<=C|t-s|² y el mismo argumento da R[g_epsilon]=O(epsilon²).

En el contacto cruzado2, d(t,t+ell)->1-exp(-2ell)=3/4 uniformemente en el primer paquete. Por polarización, el cruce del peine tiende a -3v2/8. Los cruces arquimediano y polar son O(epsilon), pero el error del cruce de contacto puede ser O(sqrt(epsilon)); basta su límite. Así

 R(f_epsilon,g_epsilon)->-3v2/8,
 R[f_epsilon+g_epsilon]->-3v2/4,
 R[f_epsilon-g_epsilon]->+3v2/4.                         (IMS-SIGNS)

El resto IMS es indefinido para paquetes de epsilon finito suficientemente pequeño. Esto no es un signo negativo de W.

Tampoco puede borrarse el resto por una supuesta cancelación automática al iterar. Para cualquier f suave compacto separado de0, la suma de R[T^r f], r>=0, converge absolutamente. En IMS cada producto f(t)f(s) adquiere el factor [T(t)T(s)]^r; sumar da EXACTAMENTE el coeficiente

 d(t,s)/(1-T(t)T(s)).                                  (SUM-IMS)

La convergencia es legítima: el denominador tiene cota inferior positiva sobre el soporte fijo; la anulación cuadrática en la diagonal conserva la integrabilidad arquimediana y el peine es finito. Equivalentemente las normas de forma de T^r f decaen exponencialmente con un factor polinómico en r por derivar T^r.

El coeficiente SUM-IMS está en[0,1], pues d>=0 y d<=1-T(t)T(s). Sin embargo al acercarse (t,s) a(0,log2) desde t,s>0,

 d(t,s)/(1-T(t)T(s))->1,

no0. Esta observación no prueba un signo global de la suma para todo f: conserva un acoplamiento firmado y no demuestra que ningún compensador diferente pueda pagarlo. Un compensador PSD más un coste sumable necesitaría una desigualdad independiente, no sólo esta identidad. No se añade una obstrucción a toda localización o representación de estado fundamental, ni se modifican las conclusiones de§6.
