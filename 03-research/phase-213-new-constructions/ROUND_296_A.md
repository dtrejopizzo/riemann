# Dos cortes monótonos y el número de primos que los separa

Para b_t de 292 escribir B=Σ_(n≤x)b_t(n), S(p)=Σ_(n≤x; P⁺(n)≤p)b_t(n) y u_p=1−Re(χ(p)p^(it)). Para todo x suficientemente grande y todo t∈[1,2], S es creciente en sentido no estricto en el tramo I=[√(x/25),√(x/8)]. En los extremos arranca por debajo de min(0,B) y termina por encima de max(0,B). Sean p₀ y p_B los primeros primos del tramo donde respectivamente S≥0 y S≥B. Definir

    W(x,t)=Σ_(p₀<p≤p_B) u_p si p_B>p₀, y cero en otro caso.

El criterio de 292 equivale a ∫₁² W(x,t)dt ≪_ε x^ε para todo ε>0. Los cortes se definen también sin escribir el total B: p_B es el primer primo donde la suma sobre enteros con un factor primo mayor que el corte se hace no positiva. La separación en la orientación opuesta no cuesta nada en este criterio.

**Certificado de pendiente.** En 8≤z≤25 poner J_t(z)=Σ_(m≤z)b_t(m)(1/m−1/z)=z K_t'(z). La función es continua (también en los enteros) y afín en 1/z entre enteros consecutivos. verify_296.py comprueba K_t(8)>1/100, K_t(25)<−1/100 y J_t(j)<−1/100 para cada entero 8≤j≤25 en 1024 celdas intervalares que cubren [1,2]. Por tanto todo el tramo tiene pendiente de ese signo. Los signos de S en los extremos y el hecho de que crucen ambos objetivos se deducen de 295 y de B≪_R x/log^R x de 294.

**El salto discreto tiene el mismo signo.** Para p primo del tramo y z=x/p², los nuevos términos de exponente uno tienen cofactor ≤x/p y todos sus primos estrictamente menores que p. En el sumatorio completo de esos cofactores, un factor q≥p es único y simple (x/p<p² para x grande) y el cofactor restante m≤z≤25. Los de exponente dos en p se añaden por separado. Así

    ΔS = −2u_p [Σ_(k≤x/p)b_t(k) + 2Σ_(m≤z)b_t(m) Σ_(p≤q≤x/(pm); q primo) u_q]
         + u_p² Σ_(m≤z)b_t(m).

Por el PNT en las clases módulo 3, la suma sobre q es (x/(pm)−p)/log p + O(p/log²p), uniforme, incluso con extremos próximos: la aproximación tiene error absoluto y se aplica en [p,25p]. El sumatorio completo en k es O(p/log²p) por 294. Por tanto

    ΔS = −4u_p p z J_t(z)/log p + O(u_p p/log²p).

El factor u_p multiplica también el error; los saltos con u_p pequeño siguen controlados. Hay constantes absolutas c,C>0 tales que c u_p√x/log x ≤ ΔS ≤ C u_p√x/log x en todo I para x grande. Esto prueba la monotonía de los valores efectivos, además de la del perfil principal continuo.

**Medición del saldo.** Con H=√x/log x, al cruzar cada objetivo su exceso está en [0,CH]. Por tanto |max(B,0)−max(S(p_B)−S(p₀),0)|≤CH. Si p_B>p₀, la última diferencia es una suma de saltos entre cHW y CHW. Si p_B≤p₀, W=0 y la parte positiva correspondiente se anula. Integrar da la equivalencia anunciada en las dos direcciones. La elección es medible por desigualdades finitas en t.

**Aproximación incondicional al orden necesario.** Incluso sin conocer el signo de B, la suma de pesos u_p entre los cortes, en cualquiera de los dos órdenes, es ≪1+|B|/H. Por 294 es O_R(√x/log^R x) para todo R fijo. También |p_B−p₀|≪_A √x/log^A x para todo A fijo: si cupiera entre ellos un intervalo de esa longitud, el PNT en clases fijas con resto de cualquier potencia logarítmica daría ≫√x/log^(A+1)x de masa u_p, en contradicción al escoger R>A+1. El control a precisión de toda potencia logarítmica no llega a la cota subpotencial para el número ponderado en la orientación desfavorable. Los dos cortes están definidos mediante sumas diferentes (bloque y complemento), pero medir su separación mediante la identidad de los saltos no da por sí solo la desigualdad pendiente.
