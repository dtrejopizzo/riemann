# POWER_STATE_065 — Oscilación exacta de la autocorrelación

Estado: **PROVED/APROBADO**. Fuente POWER_CONTACT_OSCILLATION_065.md; auditoría independiente POWER_CONTACT_OSCILLATION_AUDIT_065.md y revisión de root. Prueba analítica, sin campaña numérica. Papers intactos.

## Resultado y alcance

Para TODOS u>0,N>=1,k>=1, la autocorrelación de s^k/(s+u)^(N+k) tiene exactamente k ceros positivos simples, signos alternados desde positivo y última raíz en x=ut estrictamente menor que4k(N+k−1). Para u>1/2, TODA la cola de contactos u logq>=4k(N+k−1) tiene contribución de signo(−1)^(k+1): favorable para k impar, adversa para k par; convergencia absoluta y signo estricto de su suma.

Diferencia frente019: conteo exacto para TODO k, no otra evaluación k=1. Momentos nulos hasta2k−1 más grado resuelven N=1; filtros exponenciales unilaterales y Rolle con borde en infinito preservan ceros simples y propagan en N. La cota019 más fina para k=1 no se reemplaza. No se asume positividad total genérica ni se borra ningún primo. No se controla la magnitud frente al prefijo/ARCH/polar: sin nueva fila W, ventanaT ni signo global. Papers intactos.

## Exploración de monotonía: sin nueva desigualdad interior

La revisión de B_N>=A_N de STATE064 no produjo prueba uniforme ni contraejemplo para la forma completa. Cerca de u=1/2, LOW_TABLE018 cancela exactamente la divergencia polar con el principal continuo del peine: no hay dominancia polar disponible. Para N fijo y u→infinito, el cálculo da sólo B_N−A_N=u∂_uA_N→1 (ganancia ARCH→1; derivadas polar y aritmética→0). Es comparación eventual en tasa variable, no control de u=63/2 con N variable. No se calculó otro N ni se registra como nueva herramienta de descenso.

## Consulta066 — qué falta después de separar los intervalos de signo

Revisión de insight048, casos, mapa y root: el conteo065 no proporciona por sí solo una estimación de compensación. Para K=c_f/||f||², w(x)=x^(-1/2)K(log x), D(x)=psi_Lambda(x)−x+1 y u>1/2, la cancelación completa018 y Abel conservan exactamente

    W[f]/||f||² = ARCH_sharp[f]/||f||² + 2 int_1^infinito D(x)w′(x)dx.

Los nodos X_i=exp(chi_i/u) satisfacen w(X_i)=0. En cada intervalo entre dos nodos, y en el último hasta infinito, int w′=0. Si M=int(w′)_+=int(w′)_->0 y nu_± tienen densidades (w′)_±/M, su contribución es exactamente M(E_(nu_+)D−E_(nu_−)D). La comparación firmada de estas DOS medias sigue pendiente: el signo de w no la decide. El primer intervalo [1,X_1] es distinto, pues w(1)=1 y int w′=−1; no se le atribuyen masas iguales.

Una segunda integración, con E_1(x)=int_1^x D(y)dy, introduce [E_1 w′] en cada intervalo. Como los nodos065 son simples, w′(X_i)≠0: esos bordes no pueden omitirse al acotar intervalos por separado. Sí se cancelan exactamente al recomponer la integral global, por continuidad de E_1 y w′. No se deduce una imposibilidad para otras estimaciones del residuo. Los bordes extremos se controlan con D=O(x log x), E_1=O(x² log x) y el decaimiento racional-temporal para u>1/2.

También se comprobó la propuesta de interpolar pesos suaves en los nodos. Con autocorrelaciones NO normalizadas K_(N,k)=c_(f_(N,k)) y C_N=c_(g_N), la mezcla gaussiana positiva ya usada018/027 y Rodrigues dan, bajo integrabilidad y anulación de los bordes,

    int_0^infinito K_(N,k)(t) phi(t²)dt
      = (−1)^k Gamma(N)/Gamma(N+k)
          int_0^infinito t^(2k) C_N(t) phi^(k)(t²)dt.

Así phi^(k)>=0 da un signo para ese emparejamiento suave sin necesitar el nuevo conteo065. La variante ordinaria con phi(t) y derivada2k ya se obtiene de K_(N,k)=(−1)^k C_(N+k)^(2k) por integración por partes. Ninguna variante permite atribuir esa convexidad al peso completo de W: cerca de un contacto log q>0 éste contiene un átomo no nulo, mientras ARCH y polar son suaves allí. Derivar produce una derivada de delta, que no es una medida positiva; funciones de prueba no negativas, concentradas en ese contacto y con derivada de uno u otro signo, verifican el defecto local. Esto sólo invalida esa hipótesis suficiente, no prueba negatividad de W.

Consulta deduplicada: identidades y condiciones pendientes, sin nueva región W ni nuevo resultado teoremático para los índices. No hubo campaña de casos y los papers permanecen intactos.
