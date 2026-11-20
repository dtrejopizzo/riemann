# POWER_MIXED_VOLTERRA_OBSTRUCTION_105 — El kernel Volterra bruto cambia de signo

Estado: **PROVED analítico; auditorías matemática y literal independientes aprobadas.** No se ejecuta ningún certificado. El resultado sólo excluye tratar como positivo el kernel bruto especificado abajo. No refuta otras representaciones Volterra, gauges, compensaciones, el Wronskiano mixto ni W. Papers intactos.

## 1. Consulta y diferencia respecto de rutas registradas

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md y CROSSWORD-TO-D.md; cotejados077/088/091/092/095 y102/103. La búsqueda de Volterra y del kernel R(t)-T(t)tau(s) en esos tres índices y el corpus POWER no encontró esta ecuación de la pareja real. Las referencias Volterra antiguas del grid corresponden a otros objetos.091 estudia Pi(s)/s, un kernel de Peano construido con cofactores de cuatro nodos; aquí no hay tales nodos ni cofactores. El objeto nuevo es un kernel diferencial de las curvaturas temporales reales de103.

La motivación era transportar mediante una ecuación Volterra de kernel positivo la comparación de curvaturas original hasta la comparación mixta pendiente. Se prueba que ESE kernel bruto no es positivo, usando los datos reales y sus colas completas. No se afirma imposibilidad del transporte tras reordenar la ecuación.

## 2. Datos reales y ecuación diferencial exacta

Mantener Phi,J,K de102/103, con K PAR. Para t>0 definir

    V=-logPhi, p=V', q=V'', r=V''',
    tau=J/Phi, kappa=K/Phi,
    E=-tau'>0, X=tp-1, Y=p^2-q,
    R=X'/E, T=Y'/E,
    S=kappa'/tau', w=-S', D=tau S-kappa.

103 sección11.4 prueba S>0 y S'<0; por tanto w>0.102 prueba (kappa/tau)'=(K/J)'<0. Como

    (kappa/tau)'=tau' D/tau^2,

se tiene D>0. También R>0 porque X'=p+tq>0. Los datos son suaves en toda la semirrecta; se conservan las normalizaciones reales de las densidades.

De J'=-tPhi y K''=aPhi-J se obtienen

    tau'=p tau-t,
    kappa''-2p kappa'+Y kappa=a-tau,
    a=M'(0)>0.

Sustituir kappa'=S tau', kappa=tau S-D y w=-S' da exactamente

    E w+X S-Y D=a-tau,
    D'=-tau w, S'=-w.

Al derivar la primera igualdad y usar E'=1-q tau+pE resulta

    E w'+(2-2q tau)w+X'S-Y'D=E.

Dividir por E, que es estrictamente positivo, produce

    w'+B w+R S-T D=1,
    B=(2-2q tau)/E.                               (ODE)

No se asigna un signo supuesto a B ni a la combinación R S-T D.

## 3. Bordes de S,D y representación Volterra

103 ya demuestra que tau,kappa tienden a0. Como S>0 decrece estrictamente, existe ell>=0 con S(t)->ell. Además

    kappa(t)=int_t^infinito S(s)(-tau'(s))ds,
    tau(t)=int_t^infinito(-tau'(s))ds.

La primera identidad usa kappa'=S tau' y el borde kappa(infinito)=0; su integral converge porque vale kappa(t). Por tanto kappa/tau es un promedio de cola de S y está entre ell y S(t).102 prueba kappa/tau=K/J->0, de modo que ell=0. Así

    S(t)->0, 0<D(t)<tau(t)S(t)->0,
    S(t)=int_t^infinito w(s)ds,
    D(t)=int_t^infinito tau(s)w(s)ds.

Insertar estas dos identidades en ODE da la ecuación exacta

    w'(t)+B(t)w(t)
       +int_t^infinito H(t,s)w(s)ds=1,
    H(t,s)=R(t)-T(t)tau(s), s>=t.                 (RAW-VOLTERRA)

La integral es absolutamente convergente para cada t: R(t),T(t) son constantes respecto de s, w es integrable en la cola y tau(s)<=tau(t). El signo w>0 está probado; no se lo obtiene de una supuesta positividad de H.

## 4. Cola real: H(t,t)<0 y H(t,s)>0 para s suficientemente grande

Los bounds completos de los jets theta de088/092 dan, con y=pi exp(2t),

    p=2y+O(1), q=4y+O(1), r=8y+O(1), t->infinito.

Aquí los restos provienen de las cotas ya auditadas para TODA la serie; no se deriva un equivalente real. En particular

    p->infinito, q/p->2, r/p^2->0.

Probamos directamente el único equivalente integral necesario:

    tau(t)p(t)/t ->1.                            (TAU-LIMIT)

En efecto, cambiar s=t+u/p(t) en J(t)/Phi(t) da

    tau(t)p(t)/t
      =int_0^infinito [1+u/(tp(t))]
                       Phi(t+u/p(t))/Phi(t)du.

Para u en cualquier compacto, los bounds de p anteriores implican p(t+u/p(t))/p(t)->1 uniformemente. Por ello

    Phi(t+u/p(t))/Phi(t)
      =exp[-int_0^u p(t+v/p(t))/p(t)dv] -> exp(-u).

Como p es creciente por V''>0, el cociente de densidades es a lo sumo exp(-u). Para t suficientemente grande, tp(t)>=1 y todo el integrando queda dominado por (1+u)exp(-u), integrable. Convergencia dominada prueba TAU-LIMIT sin ningún dato puntual nuevo.

Ahora X'=p+tq e Y'=2pq-r, de modo que

    [X'-tau Y']/(tp)
      =1/t+q/p-[tau p/t][2q/p-r/p^2]
      ->0+2-1*(4-0)=-2.                         (NEGATIVE-TAIL)

Luego X'-tau Y'<0 para todo t suficientemente grande. Como E>0,

    H(t,t)=R(t)-T(t)tau(t)
          =[X'(t)-tau(t)Y'(t)]/E(t)<0.

Para cada uno de esos t fijos, la continuidad en s da también H(t,s)<0 en un intervalo inmediatamente a la derecha de t. En cambio tau(s)->0 y

    H(t,s)->R(t)>0 cuando s->infinito.

Por tanto H(t,s) cambia de signo en la MISMA pareja real para todo t suficientemente grande. No se necesita determinar un umbral óptimo ni evaluar puntos.

## 5. Alcance exacto

RAW-VOLTERRA no es una ecuación con kernel integral punto a punto no negativo. Queda excluido el paso que pretendiera invocar directamente esa positividad para probar una comparación de curvaturas o un cono preservado.

No se afirma que la integral total tenga signo negativo, ni que otra ecuación obtenida mediante gauge, integración por partes, compensación, cambio de incógnita o reordenación carezca de un kernel positivo. El signo del cuarto Wronskiano mixto, el cruce finito de U, la conservación de pares y el signo global de W permanecen abiertos. Todos los resultados reales anteriores permanecen vigentes. No se ejecutó cómputo alguno ni se modificó un paper.
