# Estado 048 — Nueva región explícita de potencias y un extremo de transporte

El objetivo global sigue OPEN. Esta ronda sí añade una región explícita de positividad de la forma completa, pero no una ventana nueva del Paper47. Papers intactos.

## Forma completa en una región subcuadrática

POWER_SUBQUADRATIC_COROLLARY_048 demuestra, a u=63/2 y para los átomos de transformada s^k/(s+u)^(N+k), que

    N >= exp(10^6),  k >= 2N²/log log N
    => W[f_Nk] > (2/5)log N · ||f_Nk||².

La prueba es simbólica, uniforme en TODOS esos N,k, y conserva el peine infinito completo y el polar. Usa las constantes explícitas de017 con c variable; no es una nueva desigualdad aritmética ni una prueba por casos numéricos. POWER_SUBQUADRATIC_AUDIT_048 aprueba el argumento y root revisó la derivación.

Esto baja la frontera respecto de cada cono cuadrático con coeficiente fijo para N suficientemente grande. El umbral exp(10^6) es conservador. Sigue faltando la banda inferior; la ampliación no elimina el residuo energético036 ni prueba la hipótesis uniforme de046. Las regiones anteriores siguen vigentes.

## Transporte restringido del bloque V12: primer extremo

POWER_R12_ENDPOINT_048 prueba E2[G]>||G||²/50 sobre V13 confluyente con G(0)=0, donde E2 conserva ARCH, POLAR y sólo el contacto2. Es el extremo v=u de R12, no el enunciado uniforme para v>=u. No se confunde con W completo: la cola de los otros contactos requiere su propio control.

La prueba usa una congruencia y LDL racional de doce dimensiones; constructor, auditor y root reprodujeron el verificador PASS. POWER_R12_AUDIT_048 aprueba también la consecuencia local por continuidad y la cota polar de la órbita Q^jV12, de razón <=9/62. Falta un corte arquimediano efectivo y el control de los índices intermedios antes de deducir transporte por la expansión geométrica015. No se hicieron barridos de tasas ni órdenes.

## Estado de las ventanas y del cierre

La corrección documental045 permanece: ROUND_026_A registra una certificación anterior de lambda_A(T)>=2e-26 para todos0<T<=1.035, con logs positivos de ambas paridades revisados documentalmente, sin reproducción larga en estas rondas. Los resultados048 no amplían ese rango.

Las exploraciones046/047 se registraron como deduplicaciones sin nuevo signo. La tabla suficiente completa, su versión primitiva y el objetivo global siguen abiertos. No se marca el goal completo ni bloqueado por dificultad matemática.
