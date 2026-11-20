# Estado038 — Error firmado por Fourier y ventana ampliada de agrupación

Estado: PROVED y auditado. Sustituye STATE037 como resumen de trabajo; conserva su cobertura W. Goal activo, signo global OPEN, papers intactos.

## Desigualdad nueva sobre el mismo perfil real

POWER_SIGNED_MOMENTS_038 conserva el producto Möbius finito en Fourier. Para el perfil gamma real f_N de037 extendido mediante rho par, define M_Q f=U_Q^(-1)sum_(b|Q)mu(b)f(ell+logb)/b, A_Q=sum logp/(p−1), B_Q=sum p(logp)²/(p−1)². Para TODO ell real, N>=16 y B_Q<=N/1000:

    |M_Q f_N(ell)−f_N(ell−A_Q)|
      <=12000 B_Q/N +65 sqrt(N)(V_Q/U_Q+1)exp(−N/2000).

La diferencia respecto037 es sustancial y cuantitativa: V_Q/U_Q desaparece del error central y sólo permanece en una cola exponencialmente pequeña. El principal es una traslación exacta del perfil real, no una constante o una supuesta media positiva. El operador sigue siendo firmado; no se aplica Jensen a sus pesos.

La transformada gamma explícita, un normalizador con densidad auxiliar positiva y una envolvente gaussiana permiten invertir Fourier con errores absolutos controlados. El perfil extendido puede cambiar de signo; sólo la densidad auxiliar empleada para el normalizador es positiva. La comparación entre el modo y el punto central se demuestra mediante Riccati, antes de usar Chebyshev.

## Corolario para la misma agrupación creciente037

Para TODOS N>=2^80, Q=prod_(p<=floor(N^(1/8)))p y

    A_Q <= logm <= A_Q+sqrt(N)/100,

se prueba para el núcleo agrupado REAL

    (4/5)U_Q/m < K_(N,Q)(m) < (6/5)U_Q/m.

El perfil trasladado está en su lado físico positivo, y cada error es menor que1/100. La longitud logarítmica certificada pasa de orden N^(1/4) en037 a orden sqrtN. Son ventanas de validez de un núcleo auxiliar: no son ventanas T del Paper47. No se afirma que el nuevo intervalo contenga m1 ni que su signo controle la suma exterior con coeficientes Möbius.

## Evidencia y obligación pendiente

POWER_SIGNED_AUDIT_038 aprueba teorema y corolario. Root y dos revisores comprobaron Fourier, normalizador, constantes y alcance. Verificador exacto de constantes reproducido por root y auditor: PASS. No se evaluaron nuevos casos W ni listas de Q.

La mejora local no controla aún la suma infinita sobre m coprimo con Q ni su integral en el residuo polar−peine. El error B_Q/N tampoco proporciona por sí solo la precisión necesaria frente a componentes exponenciales. El siguiente paso debe controlar ese complemento firmado sin sumar un mayorante no sumable ni convertir positividad de grupos en positividad de toda la suma.

Sin nueva cobertura positiva de W: se mantienen filas1..17 para todo k>=0 a u31.5 con W>norma²/40, las regiones anteriores y el átomo211,1. No hay nuevas combinaciones arbitrarias ni ampliación de T. El objetivo global sigue abierto.
