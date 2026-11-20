# POWER_GAMMA_BALANCE_030 — Signo del gap integrado para una ley gamma REAL

Estado: PROVED bound constructivo uniforme del gap ARCH_sharp para la ley gamma real; PROVED un gap completo estrictamente negativo para N2,u63/2. Revisión independiente APROBADA y verificador reproducido con PASS. No campaña. Papers intactos.

## Corpus y razón nueva antes de construir

Leídos las reglas del proyecto, INTERIOR_CONSTRAINT027, filas018/028 y los estados vigentes; búsqueda en índice/grid/crucigrama (mezcla gamma/Jensen/gaussiana de igual varianza/gap integrado). La mezcla de calor y la falta de convexidad gaussiana global ya están registradas027 y NO se presentan como novedades.

La diferencia es evaluar el SIGNO del gap contra la ley L_N de un test REAL, en la tasa fija u=63/2. La curvatura negativa en un rango genérico no decidía ese emparejamiento. Se intenta decidir una sola premisa concreta: «la forma completa del test gamma es al menos la de la gaussiana con el mismo segundo momento espectral». No se inferirá W negativo de que esa comparación falle.

La parte constructiva siguiente vale para TODOS N>=2 en la tasa fija. La comparación completa dirigida se fija solo en N=2, donde las fórmulas gamma y la cota favorable del polar gaussiano permiten una demostración elemental con toda la aritmética. No se hacen barridos de N ni otra cuña de u variable.

## 1. Bound CONSTRUCTIVO para TODOS N: coste del gap sharp

Conserve u=63/2, beta=u²/4, b=N−1/2>1, V=beta/G con G~Gamma(b,1), m=EV=beta/(b−1). Como en027,

    rho_N(t)=E e^(-Vt²),
    L_N(a)=E(V−a)_+−(m−a)_+>=0,
    ARCH_sharp[g_N]/||g_N||²=E A_sharp(V).

Se prueba el bound uniforme

    0<A_sharp(m)−ARCH_sharp[g_N]/||g_N||²
       <=(1/2)[psi(b)−log(b−1)]<1/[2(b−1)].             (SHARP-GAP)

Esto repara de manera cuantitativa la dirección desfavorable de Jensen: la gaussiana de igual segundo momento sí produce un LOWER después de pagar un coste explícito O(1/N), sin exigir convexidad falsa.

Prueba. El kernel sharp positivo satisface

    K_sharp(t)=2e^(-5t/2)/(1−e^-2t)
               =2e^(-t/2)/(e^2t−1)<=1/t.

De ahí

    0<−A_sharp''(a)=∫K_sharp(t)t^4e^(-at²)dt<=1/(2a²).

La fórmula de bisagras para la función convexa−log da EXACTAMENTE

    ∫_0^infinito L_N(a)a^-2da
       =log(EV)−ElogV=psi(b)−log(b−1).

Es finita para todos b>1, INCLUSO N2 donde ∫L_N es infinita. Integrar la cota de curvatura contra L_N prueba el primer bound. Finalmente psi(b)<=logb y log[b/(b−1)]<1/(b−1). El signo estricto izquierdo ya fue probado027 mediante la no degeneración de V. No se suma un presupuesto absoluto del peine ni se cambia el portador gamma.

En particular queda una desigualdad inferior válida para la parte sharp:

    ARCH_sharp[g_N]/||g_N||²
       >=A_sharp(m)−(1/2)[psi(N−1/2)−log(N−3/2)].

La fluctuación aritmética firmada ERR sigue necesitando su propia comparación. SHARP-GAP no la reemplaza ni declara signo de W.

## 2. Premisa completa que se decide en una ley real

Sea G_W(v) la forma completa del test gaussiano de norma uno y autocorrelación e^(-vt²). La identidad027 conserva todas las piezas y dice

    W[g_N]/||g_N||²−G_W(m)=∫L_N(a)G_W''(a)da.           (FULL-GAP)

Para la ley REAL N=2,u=63/2, m=u²/2, se prueba

    W[g_2]/||g_2||²<17/20,
    G_W(u²/2)>7/8,
    ∫L_2(a)G_W''(a)da<−1/40.                           (NEG-GAP)

Esto refuta la desigualdad completa «el test gamma domina a la gaussiana de igual segundo momento» para un miembro concreto de la familia original. Es más específico que la falta de convexidad global027: allí no se decidía el emparejamiento contra ninguna ley L_N particular.

## 3. Cota superior gamma con toda la aritmética

La energía arquimediana normalizada de g_2 es

    d−b0=psi(16)−logpi−(63/4)psi'(16)<59/100.

El verificador encierra gamma y logpi con el módulo racional auditado y usa la suma positiva de psi'16 hasta255 más su cola integral inferior. El polar normalizado es

    p20=8/u·[u²/(u²−1/4)]²<13/50.

La autocorrelación C_2(t) es positiva para todos t, así que TODOS los contactos de primos aportan negativamente a W[g_2]. Se conservan con el signo correcto en una cota superior:

    W[g_2]/||g_2||²<59/100+13/50=17/20.

No se toma el peine como cero en una identidad ni se infiere el valor completo desde una suma truncada.

## 4. Lower gaussiano que conserva la ganancia del polar

Sea v=u²/2. Su probabilidad espectral es normal centrada de desviación u, con densidad máxima pmax=1/[u sqrt(2pi)] y

    Elog|tau|=logu−(gamma+log2)/2.

Se necesita una cota de digamma más ajustada que el error constante4 del lower global. Euler–Maclaurin e integrar una vez la función Bernoulli periódica dan, para z=a+it,a>0,

    psi(z)=logz−1/(2z)−1/(12z²)
                    +∫_0^infinito B2({x})(z+x)^-3dx.

Como |B2|<=1/6, el resto tiene módulo <=1/(12a²). Por tanto

    Re psi(a+it)>=log|a+it|−Re[1/(2(a+it))]−1/(6a²).

Aplicar a=5/4 y la recurrencia desde1/4 prueba

    m(tau)>=log(|tau|/(2pi))−8/75
        −(5/4)/[2((5/4)²+tau²/4)]−1/(tau²+1/4).

Los dos kernels recíprocos tienen integrales pi y2pi, respectivamente, por lo que su coste medio es <=3pi pmax=3sqrt(pi/2)/u. El polar gaussiano exacto es

    2sqrt(pi/v)exp(1/(16v))
       >4sqrt(pi/2)/u.

Conservarlo ANTES de redondear cancela tres cuartos de esa pérdida y deja

    ARCH_gauss+Polar_gauss
      >log(u/(2pi))−(gamma+log2)/2−8/75+1/u,            (GP)

usando sqrt(pi/2)>1. Este paso conjunto es un lower real; no se presume convexidad de G_W.

Para el peine gaussiano, logq>=log2>2/3 y u²/3>20 implican v(logq)²>20logq. Así

    |Comb_gauss|<=2Σ(q>=2)q^-19<1/1000,

usando Lambda(q)<=q y relajando una potencia1/2. Es la suma infinita completa, no un segmento.

Finalmente pi<22/7 da u/(2pi)>441/88=4(441/352). Con log2>693/1000 y el primer término atanh,

    log(u/(2pi))>2(693/1000)+178/793.

Junto a gamma<3/5,log2<7/10 y u63/2, el lado de GP menos1/1000 es estrictamente mayor que7/8 por una comparación racional. Esto prueba NEG-GAP.

## 5. Verificación, balance que falta y alcance

El verificador `tools/power_gamma_balance_030_verify.py` comprueba las cotas reales N2, las constantes Euler/Bernoulli y el lower gaussiano completo mediante Fraction. No contiene un recorrido de N ni una cuadratura.

SHARP-GAP sí es una estimación integrada uniforme sobre el peso REAL L_N y da un coste controlado para una componente negativa. NEG-GAP muestra que la comparación completa sin coste no puede sustituirla. Para un lower de W faltaría controlar el cambio FIRMADO de ERR junto a esa pérdida, o el emparejamiento completo L_NG_W'' con su término G_W(m), sin desechar el polar ni convertir el peine en un valor absoluto que reproduzca018.

No se prueba W[g_2]<0: la filaN2 ya tiene signo positivo probado. No se amplía aquí la cobertura de W, no se decide N>=6 y no se afirma signo del FULL-GAP para otros N. La contribución constructiva es SHARP-GAP; el contraejemplo preciso delimita la premisa completa que no puede usarse sin esa nueva compensación aritmética.
