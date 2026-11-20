# Construcción 080 — Corrector aritmético que anula un perfil explícito

Estado: diseño y residuo escritos, pendientes de revisión; signo OPEN.

## Motivo y datos

BUILD079 extrae demasiado incluso en su primer canal. Quitar por proyección ortogonal el perfil g=Q(1_I M), con M=−Φ″+Φ/4 explícito, reduce numéricamente ||WF||² en el test guardado T=0.8 de 0.00829844628 a 0.000190522237; todavía supera su valor de forma 5.2943e−12. El cálculo está en build_079_data/check_extraction.py, órdenes64/96 coincidentes. No es certificado.

Se usa la normalización irrelevante para esa proyección

    Φ(t)=Σ_{n≥1} e^(t/2)(4x_n²−6x_n)e^(−x_n), x_n=πn²e^(2t),
    M(t)=Σ_{n≥1} e^(t/2)(−16x_n⁴+112x_n³−164x_n²+36x_n)e^(−x_n).

Puede evaluarse con t reemplazado por |t| por la paridad del perfil. La implementación diagnóstica trunca en n=12; no usa los autovectores para definir g. Q y K=R−I son exactamente los operadores de BUILD079.

## Operación nueva dentro de este diseño

En lugar de quitar una sola componente por producto interior, se fuerza la cancelación en cada contacto:

    D_g F = g·(KF)−(Kg)·F
          =Σ_n μ(n)/sqrt(n)[g(t)U_log n F(t)−U_log n g(t)F(t)].

Esta fórmula no divide por g y está definida también en sus ceros. En particular D_g g=0 exactamente. No se atribuye signo a g(t)g(t−log n): no se aplica una transformación de estado fundamental con tasas positivas.

Con S=Σ|μ(n)|/sqrt(n),

    ||D_g||≤2S||g||∞,
    α_g=1/[2(1+2S||g||∞)],
    W_g=α_g Q D_g Q,
    V_g F=J W_g F.

Por construcción ||W_g||<1/2 y W_g g=0, porque Qg=g. El corrector usa aritmética y perfil arquimediano en cada sumando, con dos restricciones implementadas por Q. Son hechos de construcción, no una prueba de signo.

## Cuadrado y residuo completos

Poner Z_n^g F=Q[g·U_log n F−(U_log n g)·F], para F∈P_T. Entonces

    ||V_g F||²=α_g² Σ_{m,n≥2} μ(m)μ(n)/sqrt(mn)
                           b(Z_m^g F,Z_n^g F),

    ρ_g(F)=Arch(F)−2Σ_n Λ(n)/sqrt(n) Re<F,U_log n F>
           −α_g²Σ_{m,n} μ(m)μ(n)/sqrt(mn)b(Z_m^g F,Z_n^g F).

Así a_T(F)=||V_gF||²+ρ_g(F), sin términos omitidos. Para F suave del núcleo, g y las funciones resultantes son BV compactas, de modo que pertenecen al dominio de J. La identidad se propone primero en ese núcleo; cualquier extensión requiere continuidad en la norma de forma.

La anulación se conserva en el canal J W_g g. No se invierte aquí el orden de J y W_g: W_gD_u g no tiene por qué ser cero. Ésta es una razón concreta para abandonar la variante V3 de BUILD079.

## Lo que falta

Anular g no anula automáticamente las derivadas del perfil ni los vectores corregidos de toda la escalera. Tampoco firma ρ_g. El diseño debe someterse al test guardado y a los controles cΛ, borrado y Beurling. La anulación algebraica D_g g=0 vale para cualquier K; por tanto no se la presenta por sí sola como el paso que separa falsificadores.

## Revisión y diagnóstico adicional

Las fórmulas de D_g, su norma, la anulación exacta y el residuo fueron revisadas independientemente en el núcleo declarado. La anulación evita el fallo de respuesta local de BUILD079 sobre el perfil límite. No anula toda la escalera.

Corrección de alcance del conmutador: ahora [D_u,M_g]=M_(g−g(·−u))τ_u introduce términos interiores. El conmutador no está localizado exclusivamente en los extremos y en Q, como ocurría en BUILD079.

NUMÉRICO: con el mismo test guardado T=0.8, el script calcula ||W_gF||²=6.2306829896562e−5 en órdenes64 y96. El supremo de g se estimó en una malla de 200001 puntos (16.9460810), dando α_g≈0.0112276223. Ni ese supremo ni el valor guardado de a_T están certificados. El primer canal sigue superando aproximadamente en 1.18e7 el valor guardado 5.2943e−12. Es evidencia contra dominación sobre ese test, aunque D_g g=0 exactamente.

## Corrección de la elección del perfil

Para tratar un test primitivo explícito completo, en lugar de su proyección dura, se puede elegir directamente

    g_T=Mχ_T−a_T^corr u_T,
    a_T^corr=∫Mχ_T cosh(t/2)dt,
    ∫u_T cosh(t/2)dt=1,

con χ_T par suave, compacto dentro de I, y u_T par suave compacto interior. Ambos momentos de g_T son entonces exactamente cero. χ_T y u_T se eligen por fórmulas de bump, independientes de la forma objetivo. La misma construcción D_g anula este test completo, incluida su corrección de momentos; no sólo Mχ_T.

Si se conserva g=Q(Mχ_T), la relación exacta con X_T=Mχ_T−a_T^corr u_T es W_gX_T=−a_T^corr W_gQu_T. No se puede usar esa fórmula sin corregir el término de borde cuando χ_T difiere del corte de g.

La elección directa g_T=X_T elimina exactamente el primer test analítico, pero no modifica la obligación de controlar todos los demás F. No se presenta como solución del diagnóstico numérico anterior, que utilizó el perfil duro Q(1_I M). La siguiente extensión propuesta es una cancelación de dos perfiles mediante cofactores, con revisión separada antes de atribuirle un alcance mayor.
