# Corrección de la cancelación residual de L2_BUILD_031

Estado: **PROVED por cálculo exacto; auditorías literales aprobadas.** Sin datos numéricos, con aviso correctivo añadido al histórico031; papers intactos.

## 1. Antecedente y afirmación corregida

Leídos las reglas del proyecto, ROUTES-TRIED-INDEX/README.md y06_OPEN_RESIDUES_DEAD_SUBROUTES.md(R9), grid R162_2300_MASTER_GRID, CROSSWORD-TO-D, P47 problema(S), P48 problema(S), L2_BUILD_030 y N_BUILD_022. El antecedente exacto es

 `03-research/phase-188-closing-D/L2_BUILD_031_RESIDUE_BALANCED_SUBSPACE.md`.

Su sección1 define(B_Q) mediante bloques constantes de longitud múltiplo del módulo. La suma NO PONDERADA de un Ramanujan sobre un bloque completo sí se anula. El paréntesis ya etiqueta ARGUED su extensión al pairing completo y advierte que multiplicar el índice por n sólo transporta balance si p no divide n. Sin embargo la sección3 presenta como identidad la omisión de todas las componentes de módulo p^b<=Q sobre(B_Q). Aquí se refuta esa omisión en el pairing completo definido en030, con una interpolación suave explícitamente admisible. No se refuta el Teorema E ni el signo de la forma real.

## 2. Todos los objetos fijados

Tomar M=Q=2, q_Q=2, I={1,2} y s1=s2=1. Es un único bloque equilibrado(B_Q): una clase par y una impar con el mismo peso. Elegir el perfil de norma1 con

 0<2T0<log(3/2).

Su autocorrelación c0 tiene soporte en[-2T0,2T0] y c0(0)=1. Luego para m=1,2 y TODO entero j>=1,

 W1(m,j)=c0(log(m/j))=delta_mj.

En efecto la distancia logarítmica mínima no nula entre uno de1,2 y otro entero positivo es log(3/2).

Fijar S suave de soporte compacto en(2/3,5/2), con S(1)=S(2)=1. Por ejemplo, si eta(x)=exp(1-1/(1-x^2)) para |x|<1 y0 fuera, tomar

 S(x)=eta(12(x-1))+eta(12(x-2)).

Es C_infinito, vale1 en ambos enteros y vale0 en TODOS los enteros j>=3; interpola así toda la sucesión s, extendida por0 fuera de{1,2}. No se presupone una interpolación en puntos no enteros sin declararla.

## 3. Componente completa de módulo2

En la descomposición Ramanujan030, para j entero positivo definir

 T_q(j)=c_q(j) sum_(n>=1,q|n) (v_n/n)S(j/n),
 v_n=2Lambda(n)/sqrt(n), v1=0.

Esta fórmula viene de la identidad exacta sum_(q|n)c_q(j)=n*1_(n|j). La compactitud de S, alejada de0, hace finita cada suma para j fijo. El pairing de la componente q es

 P_q=sum_(m=1)^2 s_m sum_(j>=1)W1(m,j)T_q(j)
    =T_q(1)+T_q(2).

Para j=1,2 y n>=3 se tiene j/n<=2/3 y S(j/n)=0. Para n=2, S(1/2)=0 y S(2/2)=S(1)=1. Por tanto no existen otras contribuciones a q=2:

 T_2(1)=0,
 T_2(2)=c_2(2)*(v2/2)*S(1)=v2/2,
 P_2=v2/2=log(2)/sqrt(2)>0.

Aquí c2(j)=(-1)^j. El bloque original tiene sum_(k=1)^2 c2(k)=0, pero la multiplicación n=2 da sum_(k=1)^2 c2(2k)=2. El cálculo del pairing anterior es más fuerte que esta observación: fija también S, W1, todos los n y todos los índices que pueden contribuir; no deja una cancelación oculta de otras potencias de2.

Como control, la componente q=1 de estas dos filas también es v2/2; juntas reproducen el término exacto n=2 de V sobre el vector s. El resultado no es una comparación de componentes aisladas con ARCH.

## 4. Corrección y alcance

La identidad de sección3 de031 debe conservar las componentes pequeñas; no puede borrarlas sólo por(B_Q). La misma corrección se aplica a las frases de su sección4 que atribuyen esa cancelación a(B_Q). La prueba del Teorema E por aproximación de configuraciones usa sólo continuidad y bloques cortos en coordenada logarítmica: permanece válida y NO depende de Ramanujan. Tampoco se cambia la cancelación trivial de sumas sobre residuos completos sin los otros pesos.

La interpolación general de030 sección3 ya estaba etiquetada ARGUED; este ejemplo muestra que la elección suave aquí declarada no suministra la cancelación pretendida. No se afirma que toda interpolación imaginable dé el mismo componente individual; justamente una afirmación universal de cancelación necesita hipótesis adicionales. Las identidades totales de030 y el problema(S) no se modifican.

Esta nota no da un valor negativo de W ni un nuevo obstáculo global: corrige un paso algebraico local concreto que no puede usarse para eliminar componentes aritméticas del pairing completo. El histórico031 conserva su texto original y recibe un aviso que remite a esta corrección auditada.


## 5. Reparación universal en soporte rough: sólo el vector cero

**PROVED, alcance restringido; auditorías root/casos/mapa.** Sea Q>=2 y s finito en R_Q, de soporte<=M. Suponga que su componente de módulo2 se anula para TODOS los perfiles permitidos y TODOS los interpolantes suaves compactos S de la sucesión. Elegir 2T0<log((M+1)/M) hace W1(m,j)=delta_mj para m<=M y TODO j>=1. Todos los j del soporte son impares. En el pairingq2, variar S con un bump en el punto no entero x=j/2 aísla el coeficiente -s_j v2/2: una coincidencia j'/2^a=j/2 obligaría j'=2^(a-1)j; como j' es impar, a=1 y j'=j. El bump puede evitar los enteros y las demás razones relevantes (localmente finitas), preservando la interpolación prescrita. La anulación universal fuerza s_j=0 para cada j. Así añadir soporte rough NO repara la cancelación universal salvo en el espacio nulo.

No se extiende este colapso al soporte mixto: las razones j/2^a colisionan dentro de rayas diádicas. Ejemplos para perfiles tan estrechos que W1 sea identidad no deciden la exigencia sobre TODOS los perfiles. En particular, para soporte hasta4 la identidad de todas las columnas necesita anchura<log(5/4), no basta anchura<log2. No se registra aquí un resultado de colapso general. El TeoremaE original sigue intacto; una restricción nueva al núcleo exacto de componentes requeriría una nueva prueba de aproximación.
