# CONSTRUCTOR_002 — Diseño de covarianza theta normalizada

2026-10-18. Continuación. **WORKING / PARTIAL:** objeto y positividad independientes explícitos; enlace con Q_T **OPEN**. La positividad de una covarianza genérica **no se cuenta como éxito del programa**.

## 0. Corpus y diferencia escrita antes de construir

Se mantienen las lecturas de CONSTRUCTOR_001 y AUDIT_001. Búsqueda adicional en índice README, 04_PHASES, 05_LITERATURE, 05b y 06: covarianza, Fisher, probabilidad, gcd/lcm, log theta, cocientes y divisibilidad. Choques relevantes: SPEC005 Lema H y H.1 (0-homogeneidad de un objeto theta, posibilidad de cocientes); INV_C (formas atómicas y parejas), INV_H/K (divisores usados linealmente), INV_V_002 (transferencia de Chebyshev hermítica), R183_008 (Gram semilocal por gcd), G8D/G8H probabilísticos; P1_BBSTAR.

**Razón para este cálculo, sin reabrir esos programas.** No se intenta igualar Q_T con una forma cuadrática homogénea en coeficientes theta, ni construir un Gram semilocal de Sonin, ni usar Λ*1=log como identidad lineal de transferencia. Se calcula una **covarianza normalizada**, cociente de theta de grado cero, donde la misma ley de probabilidad ve la divisibilidad y cuya dependencia de escala tiene una identidad exacta de Poisson con el término de origen. Esto está permitido por H.1; que no esté excluido literalmente no le da signo para el nodo. El cálculo debe mostrar exactamente qué se pierde si se desnormaliza para leer Mellin. No se afirma originalidad en la teoría general de covarianzas.

## 1. Un único objeto: indicadores de divisibilidad bajo gaussiana discreta

Sea

`θ(y)=Σ_{n∈Z}exp(−πn²y)`, `τ(y)=θ(y)−1`, y>0.

Sobre Z\{0} defino la probabilidad

`P_y(N=n)=exp(−πn²y)/τ(y)`.

Para d≥2, `X_d(N)=1_{d|N}`. Escribo

`q_y(d)=τ(d²y)/τ(y)`, `l=[d,e]=lcm(d,e)`,

`C_y(d,e)=q_y(l)−q_y(d)q_y(e)`.

**Lema 1 (PROVED).** Para cualquier sucesión finita a_d compleja,

`Σ conjugate(a_d)a_e C_y(d,e)=Var_y(Σ a_d X_d)≥0`.

Es covarianza elemental: X_dX_e=X_l. No requiere b=Λ. Por ello es **positividad heredada**, cuyo valor para el programa dependerá enteramente de una identidad específica de enlace.

### Ecuación funcional exacta del mismo objeto

Poisson para la gaussiana da

`τ(y)=y^(−1/2)τ(1/y)+y^(−1/2)−1`,

`q_y(d)=[d^(−1)y^(−1/2)τ(1/(d²y))+d^(−1)y^(−1/2)−1]/[y^(−1/2)τ(1/y)+y^(−1/2)−1]`.

Esta es una identidad exacta, sin fase estacionaria. El origen excluido reaparece como `y^(−1/2)−1`; conductor y escala son los de θ_Z. La dualidad no deja cada indicador de divisibilidad fijo: aparecen las escalas fraccionarias 1/d². Por tanto no se ha obtenido un cierre de la FE en el espacio de indicadores originales.

### Completitud y borrado

Para N≠0:

`Σ_{d|N,d≥2}Λ(d)=log|N|`.

Así el observable infinito definido por la aritmética completa es log|N|. Las sumas tienen convergencia en L²(P_y): su módulo es ≤log|N|, que tiene segundo momento finito por el peso gaussiano. En particular,

`Σ_{d,e≥2}Λ(d)Λ(e) C_y(d,e)=Var_y(log|N|)`

entendido como límite de covarianzas de sumas truncadas en L²; no como intercambio absoluto de cada término firmado sin prueba adicional.

Para b^(p) que borra todas las potencias de p, el observable es

`log|N|−v_p(|N|)log p`.

La identidad con log|N| falla en N=p. Esta es la identidad específica de completitud; la covarianza permanece positiva tras borrar. No se atribuye al fallo de esa identidad el signo de Q_T.

## 2. Mellin positivo hasta el peso ½: no inventar una barrera

Para α>0 y d,e≥2 defino

`I_α(d,e)=∫_0^∞ y^(α−1) C_y(d,e)dy`.

**Lema 2 (PROVED).** La integral converge absolutamente entrada a entrada para todo α>0 y define una forma PSD sobre c_00({2,3,...}). En particular α=1/4 es admisible.

**Prueba.** Cuando y↓0, Poisson implica `q_y(d)=1/d+O_d(√y)`, de modo que

`C_y(d,e)=G_0(d,e)+O_{d,e}(√y)`,

`G_0(d,e)=1/[d,e]−1/(de)=(gcd(d,e)−1)/(de)`.

Cuando y→∞, P_y se concentra en ±1; por ello cada q_y(d) y C_y(d,e) decae exponencialmente (para d≥2, q_y(d)=O_d(exp(−π(d²−1)y))). Convergencia en ambos extremos. Para una suma finita, integrar el Lema 1 contra medida positiva. ∎

Esto no demuestra que I_(1/4) tenga exactamente el peso d^(−1/2) exigido por el nodo. **El parámetro de Mellin 1/4 no sustituye una ley de homogeneidad:** el denominador τ(y) impide extraer una potencia d^(−2α) por cambio de variable. Ésa es una pregunta de enlace y no se da por resuelta.

La familia C_y no es Hankel multiplicativa: para pares (2,6) y (3,4), ambos de producto 12, el límite y↓0 es respectivamente 1/12 y 0. Por tanto no colapsa universalmente a una función del producto de los dos índices. Esto no prueba por sí solo una afirmación de no-Hankel para una única integral I_α a un α concreto.

## 3. Desnormalización: identidad exacta con Mellin clásico y resto

Para recuperar la masa de theta y una ley Mellin de dilataciones, se considera otra forma del **mismo** objeto:

`B_y(d,e)=τ(y)C_y(d,e)=τ(l²y)−τ(d²y)τ(e²y)/τ(y)`.

Para α>1/2 las dos partes son integrables separadamente y

`∫_0^∞ y^(α−1)B_y(d,e)dy`

`=2π^(−α)Γ(α)ζ(2α) l^(−2α) − ∫_0^∞ y^(α−1) τ(d²y)τ(e²y)/τ(y)dy`.

**PROVED** por la transformada de Mellin de τ y un cambio de variable. Cada integral izquierda define un kernel PSD en ese régimen. La resta derecha no convierte por separado sus términos en fuentes de signo.

### Continuación real hasta α=1/4, con contratermino explícito

Se tiene `B_y=y^(−1/2)G_0+O(1)` en 0 y B_y decae exponencialmente en infinito. Para 0<α<1/2 defino

`R_α(d,e)=∫_0^∞ y^(α−1)[B_y(d,e)−y^(−1/2)G_0(d,e)]dy`.

**Lema 3 (PROVED).** R_α converge absolutamente entrada a entrada y es la continuación meromorfa de la integral positiva anterior a través de su polo en α=1/2. Su representación exacta es

`R_α = ∫_0^1 y^(α−1)(B_y−y^(−1/2)G_0)dy`

`      +∫_1^∞ y^(α−1)B_y dy +G_0/(α−1/2)`.

La prueba es dividir la integral en 1; el último término coincide en ambos regímenes por integración elemental. En α=1/4, el contratermino escalar es **−4G_0**. La positividad de I_(1/4) no da la de R_(1/4).

También hay una descomposición exacta, sin continuación en la primera parte:

`R_α=I_α+H_α`,

`H_α=∫_0^∞ y^(α−1)[(τ(y)−1)C_y−y^(−1/2)G_0]dy`.

H_α converge para 0<α<1/2 por las mismas asintóticas; no se le conoce signo. Esta identidad localiza lo que tendría que aportar una segunda desigualdad; no lo oculta como «error pequeño». No se afirma que R_α o H_α sean Q_T.

## 4. Puertas y enlace al nodo: pendientes concretos

- **SOS.** No existe aquí identidad puntual de un símbolo como μ₀−S_T ni arquimediano que paga una constante; thm:sos no se aplica literalmente. Tampoco se ha producido un certificado dual de def:PD.
- **P1.** I_α es una covarianza positiva genérica. Proponer simplemente un mapa U_T con `Q_T=I_(1/4)(U_TF)` trasladaría todo a construir U_T. No se presenta esa existencia como resultado.
- **W₂/BR.** No se han identificado tests y modelo de restos de BR ni un kernel de P36-4. No se reclama evasión de sus paredes.
- **Dominio.** I_α y R_α están definidos sobre sucesiones finitas. No se dispone todavía de un operador no compacto de alturas K(t,t′), ni de un mapa desde todo el dominio continuo de Q_T que verifique las condiciones del README. Una representación de coeficientes por exponentiales no resuelve esto automáticamente.
- **Grado y soporte.** Usar coeficientes `a_d=Λ(d)d^(−1/2)F(log d)` da una forma cuadrática en evaluaciones de F. Usar autocorrelaciones de F como a_d daría grado cuatro y no sirve. La forma del nodo es cuadrática en F y lineal en Λ; no hay identidad entre ella y la primera expresión por mera completitud. Los términos de lcm y cocientes de theta deben tratarse expresamente.
- **Polos.** El término de origen de Poisson está escrito. No se ha probado que corresponda al sector polar de Q_T ni que lo anule la condición ortogonal a cosh(x/2).

## 5. Qué sigue trabajando este diseño

El cálculo evita dos errores: afirmar que una covarianza normalizada no puede existir en parámetro crítico (sí existe), y afirmar que su Mellin ya entrega Γ_R y el peso requerido (no lo hace). La operación exacta que recupera Mellin clásico introduce R_α y el término −4G_0 en α=1/4.

La pregunta siguiente dentro de este único candidato es construir un mapa de tests que convierta la diferencia de desnormalización H_(1/4), junto a las escalas duales de Poisson, en los términos arquimediano y polar con **igualdad de formas**. No hay ese mapa todavía. Si se propone, habrá que verificar los átomos adicionales, no sólo comparar una diagonal o un bloque.

**No se alcanzó el hito del README.** Se obtuvo un objeto normalizado explícito, una identidad FE exacta y el punto exacto donde falta enlace y signo. No se lo declara objeto signo ni progreso demostrado hacia D; se deja como construcción en examen, no como cierre ni como NO-GO universal.

## 6. Origen versus covarianza puncturada: identidad útil para el enlace polar

Para no confundir la asociación theta con un signo útil después de quitar el polo, denoto por `C_y^0` la covarianza en Z **incluyendo 0** y por `C_y^×` la C_y de §§1–5. Sea `p_0=1/θ(y)` y `r_d=τ(d²y)/τ(y)`.

**Lema 4 (PROVED).** Como kernels en d,e,

`C_y^0=(1−p_0)C_y^× + p_0(1−p_0) u_y u_y*`, `u_y(d)=1−r_d`.

**Prueba.** Condicionar en el evento N=0 y su complemento. En N=0 todos los X_d valen 1 y tienen covarianza cero. La fórmula de covarianza total da el primer término como covarianza condicional media y el segundo como covarianza de las medias condicionales 1 y r_d. ∎

Es una descomposición exacta donde el origen aporta rango uno, pero su dirección u_y depende de la escala y del índice. No se identifica aún con cosh(x/2), ni se puede restar sin justificar el mapa de tests.

**Lema 5 (PROVED).** Para d,e≥2 coprimos,

`C_y^×(d,e)=−exp(−π(d²+e²−2)y)(1+o(1))` cuando y→∞.

En efecto, `q_y(k)=exp(−π(k²−1)y)(1+o(1))`, mientras `[d,e]=de` y `d²e²−1>d²+e²−2`. Por tanto la resta del producto domina la probabilidad conjunta.

Consecuencia de diseño: la positividad PSD permanece, pero la positividad **entrada a entrada** no sobrevive a quitar el origen. Cualquier argumento de asociación de la theta completa que pretenda aportar un signo nuevo al sector sin polo debe controlar explícitamente el rango uno del Lema 4. La identidad puede servir para localizar ese enlace; todavía no lo demuestra.

## 7. Primer mapa lineal en Λ: observable logarítmico, con términos exactos

Para acercar el objeto cuadrático a la linealidad del peine del nodo, hay un brazo fijado por completitud. Defino

`L(y)=E_y(log|N|)=−[∂_β log τ_β(y)]_(β=0)`,

`τ_β(y)=Σ_{n≠0}|n|^(−β)exp(−πn²y)`.

Para y>0 fijo, todas las derivadas en β existen y se intercambian con la suma por la cola gaussiana.

**Lema 6 (PROVED).**

`L(y)=Σ_{d≥2}Λ(d)q_y(d)`,

`Cov_y(X_d,log|N|)=q_y(d)[log d+L(d²y)−L(y)]`.

La primera identidad es completitud de divisores y convergencia monótona. La segunda se obtiene condicionando N=dM: dado d|N, M tiene distribución gaussiana discreta puncturada de parámetro d²y y `log|N|=log d+log|M|`.

Por tanto, para a finito,

`Cov_y(Σ a_d X_d,log|N|)=Σ a_d q_y(d)[log d+L(d²y)−L(y)]`.

Si `a_d=Λ(d)v_d`, el brazo móvil es lineal en Λ. El segundo brazo queda fijado por la identidad aritmética completa, que cambia al borrar un primo. Pero es una **covarianza cruzada**, no una varianza: no tiene signo para v arbitrario. Reemplazarla por una varianza introduciría otra vez el brazo cuadrático. No se ha probado que los tests del nodo produzcan un v de signo o monotonicidad adecuados.

La transformada Mellin ponderada de este brazo completo también es exacta para Re s>1:

`∫_0^∞ y^(s/2−1)τ(y)L(y)dy=−2π^(−s/2)Γ(s/2)ζ′(s)`.

Al dividir por `∫ y^(s/2−1)τ(y)dy=2π^(−s/2)Γ(s/2)ζ(s)` se obtiene `−ζ′/ζ(s)`. Éste es un enlace real con el peine, pero **todavía en Re s>1**, y un cociente de Mellin no es la integral de una covarianza positiva. No se transporta ese signo a Re s=1/2 por continuación analítica. Las rutas de transporte y normas Helson ya indexadas no se reabren con esta fórmula.

En este diseño, por consiguiente, ya están escritas las dos pérdidas diferentes que habría que evitar: (a) fijar un brazo logarítmico recupera linealidad en Λ pero pierde la varianza; (b) desnormalizar permite leer Mellin clásico pero introduce el contratermino al cruzar α=1/2. Una identidad nueva de FE que relacione ambos defectos —y el sector polar del test— sería necesaria para pasar de este objeto al nodo. No se ha construido dicha identidad.
