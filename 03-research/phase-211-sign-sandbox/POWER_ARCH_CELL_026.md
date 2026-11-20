# POWER_ARCH_CELL_026 — Déficit sharp y kernel conjunto firmado

Estado: **PROVED** déficit no cubierto por el bound ERR025; **PROVED** agrupación conjunta exacta y falsificador de positividad puntual de su kernel. Signo W129 **OPEN**. Revisión independiente por mapa aprobada, incluida la agrupación/Fubini y verificador PASS. Papers intactos.

## 1. Corpus y diferencia precisa

Leídos las reglas del proyecto, LOW_TABLE018, SIGNED_BALANCE020, CONTACT_BALANCE021, CUMULATIVE_INVERSE022, CELL_BALANCE024 y INVERSE_LOGCONCAVITY025. Consultados índice/grid/crucigrama (errores absolutos, límites de component bounds y último balance025). La cancelación polar con el principal es previa018. No se presenta como nueva.

La diferencia frente020 es combinar ARCH_sharp y el emparejamiento celular ANTES de acotar ninguno. Se obtiene un kernel conjunto sobre el inverso compensado K, y se prueba que el lema natural «ese kernel es no negativo» es falso en un punto exacto. Esto no es una razón para abandonar el signo: identifica qué desigualdad pointwise NO aporta la estructura faltante. La restricción de ser el kernel gamma real sigue disponible y no se elimina mediante una clase abstracta.

## 2. Qué déficit queda en el MISMO N129,k0

El símbolo sharp018 se simplifica exactamente por la recurrencia de psi:

    m(tau)+1/(tau²+1/4)=Re psi(5/4+i tau/2)−logpi.

La probabilidad espectral de g_N tiene E(tau/2)²=V_N=u²/[4(2N−3)]. Se usa la misma sumación de Euler compleja y Jensen probadas020, trasladando ahora TRES pasos desde5/4 hasta a=17/4. Con b_j=5/4+j,j0..2,

    ARCH_sharp[g_N]/norm²<=U_N
      =(1/2)log(a²+V_N)−a/[2(a²+V_N)]+1/(2a)
       −sum_(j=0)^2 b_j/(b_j²+V_N)−logpi.

Para N129,u63/2 la comparación racional de logaritmos prueba

    ARCH_sharp[g129]/norm²<−81/100.                       (DEFICIT)

Por025 se tiene ERR129<−33/50, que garantiza un beneficio de al menos.66, NO una cota superior sobre su beneficio real. Sustituir sólo esa garantía deja

    ARCH_sharp[g129]/norm²+33/50<−15/100.

Así el bound probado025 no basta para W>=0. Esta desigualdad NO es W<0: el valor completo de −ERR puede ser mayor que.66. No se confunden las direcciones de las cotas.

## 3. Agrupación conjunta que conserva la cancelación

Con las normalizaciones de022, w_N(x)=x^(−1/2)rho_N(logx), rho_N(0)=1, y

    J_N(x)=x int_x^infty K_N(t)/t²dt,
    w_N(x)=sum_(n>=1)J_N(nx).

La última identidad usa mu*1 y Fubini absoluto, como MASS022. Escriba T(y)=floor(y)[floor(y)+1]/2, incluyendo T(y)=0 si0<=y<1, y

    D(t)=T(t)/t²,
    E_x(t)=T(t/x)/t².

Entonces

    1=int_1^infty K_N(t)D(t)dt,
    rho_N(logx)=x^(3/2)int_1^infty K_N(t)E_x(t)dt.          (RHO)

La representación elemental de psi da, con d_*=psi(5/4)−logpi y k(x)=x^(−7/2)/(1−x^(−2)),

    ARCH_sharp[g_N]/norm²
      =d_*+2int_1^infty k(x)[1−rho_N(logx)]dx.

Se conserva el emparejamiento completo ERR=−2int K_N C_B de022, con TODOS los saltos de B. Sustituir (RHO) y agrupar antes de integrar da

    W[g_N]/norm²=int_1^infty K_N(t)Omega(t)dt,             (JOINT)
    Omega(t)=d_*D(t)+2C_B(t)
       +2int_1^infty k(x)[D(t)−x^(3/2)E_x(t)]dx.          (OMEGA)

Estas identidades no se presentan por sí solas como prueba de signo. Los términos dentro del último corchete deben permanecer JUNTOS cerca de x1.

Justificación de Fubini. Para x cercano a1 se separa T(t)−x^(3/2)T(t/x) en (1−x^(3/2))T(t)+x^(3/2)[T(t)−T(t/x)]. La primera parte es O(x−1) después de integrar contra |K|/t². La segunda sólo cuenta cruces n<=t<nx; su integral absoluta es O(x−1) por el decaimiento suave K(t)=O_N(t^(−32)(1+logt)^(N−1)). Eso cancela la singularidad k(x)=O((x−1)^−1). En x infinito se usa k=O(x^(−7/2)) y el mismo decaimiento. Por tanto la integral doble agrupada es absoluta. En t entero, OMEGA puede tener singularidad logarítmica unilateral; el valor en esos puntos aislados no interviene y las singularidades son integrables contra K. No se exige un kernel acotado punto a punto en los enteros.

## 4. Falsificador exacto del lema pointwise conjunto

En la primera celda1<t<2, D(t)=1/t² y E_x(t)=1/t² para1<=x<=t,0 parax>t. Además C_B(t)=(1−t^(−2))/2. Así

    Omega(t)=1+t^(−2)[log((t+1)/(t−1))−1−gamma−log(4pi)].   (FIRST)

Para verificar la simplificación sin una cuadratura, ponga

    I(t)=int_1^t k(x)(1−x^(3/2))dx+int_t^infty k(x)dx.

Entonces I'(t)=−1/(t²−1), y

    2I(infty)=psi(1/2)−psi(5/4),
    2I(t)=psi(1/2)−psi(5/4)+log((t+1)/(t−1)).

Usar psi(1/2)=−gamma−2log2 prueba FIRST. En t=3/2,

    Omega(3/2)=(4/9)[5/4+log5−gamma−log(4pi)]<−1/10.       (FAIL-OMEGA)

La última comparación se certifica con los intervalos racionales003. No se usa aproximación decimal como prueba.

Por tanto es FALSO el lema concreto «después de agrupar exactamente el principal, ARCH_sharp y todos los saltos celulares, el kernel Omega es no negativo en toda la semirrecta». La agrupación sí conserva la cancelación, pero su kernel sigue firmado.

Esto no falsifica W en el dato real: K_N es el inverso del kernel gamma de autocorrelación, no una función arbitraria elegible para concentrarla en t=3/2. Por ejemplo, tomar un K positivo concentrado dentro de(1,2), normalizado por int KD=1, produciría rho(logx)=x^(3/2)>1 para x apenas mayor que1, violando el bound elemental de una autocorrelación normalizada. La información gamma/positividad definida puede ser esencial para controlar el emparejamiento JOINT, y no se declara inútil porque falle la positividad de Omega.

## 5. Resultado y siguiente obligación concreta

Se probó que el beneficio.66 de025 deja más de.15 de déficit frente al sharp real. También se obtuvo una agrupación verdadera desde el inicio y se refutó con cálculo exacto una desigualdad uniforme natural de su kernel. No se afirma que ninguna agrupación pueda funcionar, que W129 sea negativa ni que la cobertura de la tabla haya retrocedido.

La obligación restante en esta vía es un bound unilateral sobre int K_N Omega que use las restricciones del kernel gamma real y la masa aritmética, sin sustituir K ni Omega por signos supuestos. La identidad JOINT sola no lo aporta; FAIL-OMEGA impide cerrar por positividad puntual universal del nuevo peso.

Verificador exacto: tools/power_arch_cell_026_verify.py, PASS. Sólo N129 para DEFICIT y t3/2 para el falsificador analítico; sin campaña de parámetros ni precisión masiva.
