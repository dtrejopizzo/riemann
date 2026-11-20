# POWER_SCHUR_BASE_AUDIT_081 — Auditoría independiente

Estado: **APROBADO / PROVED en la clase declarada.** Fuente `POWER_SCHUR_BASE_OBSTRUCTION_081.md`, leída íntegra. Revisor mapa; root informado. Papers intactos.

## Objeto y antecedentes

El objeto es el resto exacto G_p de la Phi REAL construido075–077, no el modelo genérico074. Se cotejan003,073–079 y los tres registros obligatorios.079 utiliza BASE073;081 comprueba si esa BASE se hereda literalmente por G_p. El resultado descarta esa herencia particular, no una recursión de Schur más amplia.

## Verificación

La normalización positiva C_p=(p²B(p)²/a)G_p da exactamente C_p=z[B(z)−B(p)]/[1−g(z)/K_p], con g=z²B y K_p=p²B(p). Los límites B(p)→0, K_p→infinito provienen de las cotas reales completas078, por lo que C_p→F=zB=a/M−1/z localmente con derivadas. El argumento límite ya contradice monotonía creciente universal porque F>0 y F→0.

La versión efectiva es correcta. En z*=1024, a>1/25, M(z*)<3 y M'(z*)>1/[3(z*+1/2)] implican a z*²M'/M²>4/3, de donde F'(z*)<−1/(3z*²). Las cotas de psi y series aritméticas conservan el peine completo; no se utiliza un diagnóstico theta nuevo.

Con L=2g*+24a²z*²/c*² y p0=[25(L+2)]², M(p)<sqrt(p) y a>1/25 dan Kp>L para todo p>=p0. Así g*/Kp<1/2. La derivada de NORMAL está correctamente calculada. Su primer término es menor que F'(z*) y el segundo es menor que4a²/(c*²Kp)<1/(6z*²), incluso si su numerador fuera negativo. Resulta G_p'(1024)<0 para todo p>=p0.

Como G_p>0 en toda la semirrecta por077, una derivada negativa impide concavidad global: la recta tangente terminaría siendo negativa. Para cada uno de estos pivotes algún punto posterior tiene G_p''>0.

## Alcance

Se refuta solamente imponer a TODOS los restos reales G_p las condiciones G_p'>0 y G_p''<=0 de BASE073. G_p>0 permanece probado. Los criterios de pares permiten derivadas negativas, y el residuo positivo de Schur no se elimina. No se demuestra un kernel negativo, W negativo, imposibilidad de recursión general ni una obstrucción al objetivo global. La continuación puede cambiar la clase de hipótesis preservadas;082 está separada de esta conclusión.
