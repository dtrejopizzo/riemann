# POSITIVE_ASSOCIATION_002 — Asociación estricta de divisibilidad bajo theta

2026-10-18. Revisor: prueba independiente para auditar CONSTRUCTOR_002.
**PROVED / herramienta positiva parcial. No signo del nodo demostrado.**

## Corpus y atribución

Búsquedas dirigidas en índice por convexidad geométrica de theta, asociación y correlaciones de divisibilidad no identificaron esta formulación. Proximidades: SPEC005 (C-hom, theta-Bochner genérico), R183_008 (Gram semilocal gcd), R11_2_ORIGIN (polar/origen). La diferencia explícita: no se usa la PSD genérica de una covarianza, sino el signo de cada correlación cruzada; el cociente theta tiene grado cero; el signo puede romperse para la medida correspondiente a un factor Euler eliminado. Esto habilita examinar el corolario, sin reabrir las rutas anteriores como prueba del nodo.

La convexidad theta es clásica, no nueva: fuente primaria comunicada y verificada por el coordinador, Faulhuber–Steinerberger, arXiv:1601.02972, Theorem 2.3, https://arxiv.org/html/1601.02972 . A continuación se da prueba propia elemental para no depender de una cita de memoria. No se afirma novedad del corolario de asociación en la literatura.

## 1. Convexidad geométrica estricta de theta

Sea θ(y)=Σ_{n∈ℤ} exp(−π y n²), y>0; h(x)=log θ(e^x). Entonces h''(x)>0.

Prueba para y=e^x≥1. Bajo la probabilidad gaussiana discreta μ_y(n)=exp(−π y n²)/θ(y), escribir m=E(n²). Derivación absoluta de las series da

    h''(x)=π² y² Var(n²)−π y m.

Se tiene E(n⁴)≥m, luego Var(n²)≥m(1−m). Además θ≥1 y, con q=e^(−π)<1/20,

    0<m≤2 Σ_{n≥1} n² q^(n²)≤2 Σ_{n≥1} n² q^n
       =2q(1+q)/(1−q)³ < 840/6859 < 1/2.

Por tanto h''≥π y m [π y(1−m)−1]>0, ya que π/2>1. Para y≤1, Poisson θ(y)=y^(−1/2)θ(1/y) implica h(x)=−x/2+h(−x), luego h''(x)=h''(−x)>0. ∎

Poisson se usa de modo efectivo para trasladar el signo desde y≥1 hacia y≤1; no se simetriza una norma genérica.

## 2. Correlación de dos divisibilidades

Para enteros d,e≥2, sean I_d(n)=1_{d|n}, tomando d|0. Su probabilidad bajo μ_y es q_d(y)=θ(d²y)/θ(y). Para ℓ=lcm(d,e),

    C_y(d,e)=Cov_μy(I_d,I_e)
       =θ(ℓ²y)/θ(y)−θ(d²y)θ(e²y)/θ(y)² >0.

Prueba. Con x=log y, a=2log d>0 y b=2log e>0,

    h(x+a+b)+h(x)−h(x+a)−h(x+b)
       =∫_0^a ∫_0^b h''(x+u+v) dv du >0.

Exponenciando,

    θ((de)²y)θ(y)>θ(d²y)θ(e²y).

Como ℓ≤de y θ es decreciente, θ(ℓ²y)≥θ((de)²y). La desigualdad estricta anterior prueba C_y(d,e)>0. ∎

El signo no es la PSD de la matriz de covarianzas: PSD vale para toda probabilidad, mientras una covarianza cruzada individual puede ser negativa.

## 3. Un borrado primo rompe el signo cruzado

Sea p primo y μ_y^(p) la probabilidad proporcional a exp(−π y n²) sobre n∈ℤ con p∤n. Su normalización es

    Z_p(y)=θ(y)−θ(p² y)>0.

Para d coprimo con p,

    q_d^(p)(y)=[θ(d²y)−θ(p²d²y)]/Z_p(y).

Sean d,e≥2 coprimos entre sí y con p. Cuando y→∞,

    Z_p(y)=2e^(−π y)(1+o(1)),
    q_d^(p)(y)=e^(−π(d²−1)y)(1+o(1)),
    q_de^(p)(y)=e^(−π((de)²−1)y)(1+o(1)).

Como

    ((de)²−1)−(d²+e²−2)=(d²−1)(e²−1)>0,

resulta

    Cov_μy^(p)(I_d,I_e)
       =−e^(−π(d²+e²−2)y)(1+o(1))<0

para todo y suficientemente grande. Ejemplo explícito: p=5, d=2, e=3. No se requiere umbral numérico para la afirmación asintótica probada.

Este condicionamiento corresponde realmente al factor eliminado: para Re s>1,

    ∫_0^∞ Z_p(y)y^(s/2−1)dy
       =2π^(−s/2)Γ(s/2)ζ(s)(1−p^(−s)).

La identidad sale por integración término a término sobre enteros positivos no divisibles por p. Se ha perdido la masa en cero, pero aquí se prueba que esa pérdida cambia una correlación de signo; no se atribuye ese signo al término polar de Q_T.

## 4. Alcance exacto

Hay un positivo independiente y específico de una distribución aritmética con Poisson: todas las covarianzas cruzadas anteriores son estrictamente positivas y un borrado primo concreto las hace negativas. El objeto no es sólo una norma genérica. Aun así:

- Es una afirmación sobre divisibilidad gaussiana, no todavía sobre los coeficientes Λ del nodo.
- La variable y y los índices d,e no son automáticamente alturas t,t′ de Mellin; la traducción necesita hacerse.
- No se ha demostrado identidad o dominación de Q_T por estas correlaciones. Pesos con signo y derivadas logarítmicas pueden perder la positividad.
- El límite y↓0 es C_y(d,e)→(gcd(d,e)−1)/(de); para d,e coprimos, la estricta positividad queda en una corrección pequeña que no debe descartarse.
- El fallo de signo se probó para un condicionamiento completo y y grande, no para todo p,T ni para toda ventana del nodo.

**Resultado parcial positivo PROVED; enlace con Q_T OPEN.** Esta nota ofrece un signo concreto que auditar, sin declarar cumplido el objetivo de O1 ni el signo final.

## 5. Control hostil del origen: límite decisivo del positivo

**PROVED.** El átomo n=0 explica una contribución positiva de rango uno. Sea p₀=μ_y({0})=1/θ(y), μ_y^*=μ_y condicionada a n≠0, y r_d=E_μy* I_d. La fórmula de covarianza total da exactamente

    C_y(d,e)=(1−p₀) C_y^*(d,e)
       +p₀(1−p₀)(1−r_d)(1−r_e).

El último término es una matriz de rango uno positiva. Sobre coeficientes finitos a_d con Σ_d a_d(1−r_d)=0, su contribución a Σ a_d conjugado(a_e)C_y(d,e) se anula y sólo queda la covarianza condicionada, cuya PSD es genérica.

Para d,e coprimos mayores que 1, también C_y^*(d,e)<0 para y grande: la misma asintótica de §3 vale sin excluir múltiplos de p. Por tanto el cambio de signo del borrado no identifica por sí solo un efecto de Euler completo; quitar únicamente el origen ya destruye la asociación cruzada. La prueba de §2 sigue siendo un positivo exacto, pero no establece que el signo útil sobreviva al eliminar el modo de origen.

**No hay identificación demostrada entre este rango uno y el polar de Q_T.** Hasta construirla, tampoco se puede afirmar que el ortogonal cosh lo mate automáticamente. R11_2_ORIGIN ya obliga a controlar este punto antes de convertir una propiedad del origen theta en mecanismo para el nodo.

Conclusión de alcance corregida: el positivo de asociación existe y es específico de la distribución theta íntegra; la pretensión de que proporcione signo aritmético nuevo para el ortogonal polar queda **OPEN, sin evidencia por ahora**. No usar el fracaso tras borrar p como prueba suficiente de una evasión de la barrera del origen.
