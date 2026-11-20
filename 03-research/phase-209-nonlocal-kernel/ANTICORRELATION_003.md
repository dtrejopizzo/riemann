# ANTICORRELATION_003 — Signo cruzado estricto en la gaussiana discreta sin origen

2026-10-18. Constructor principal. Matemática pura. Estado: **PROVED, revisión hostil favorable en AUDIT_003.md**. No se afirma novedad bibliográfica global.
No es una prueba del nodo ni un núcleo O1 identificado con Q_T.

## 0. Corpus check y diferencia escrita

Consultados índice ROUTES-TRIED-INDEX (README, literatura y residuos),
SPEC_SIGN_OBJECT_005, CELL_001, CONSTRUCTOR_002 y POSITIVE_ASSOCIATION_002.
La covarianza PSD por sí sola está cubierta por las objeciones a Gram. Aquí
se prueba **el signo negativo de las entradas cruzadas** para divisores
coprimos, que no vale para una probabilidad arbitraria. Es distinto de la
asociación positiva de theta con origen y de una positividad cuadrática
homogénea en theta: se trabaja con cocientes de grado cero y se elimina el
origen antes de calcular. No se reabre PF del núcleo Xi, ni Bohr/Helson,
ni Perron–Frobenius para la matriz del nodo. Las matrices de esta nota son
covarianzas de divisibilidad; no son la forma de Weil.

La convexidad geométrica de theta CON origen es clásica: Faulhuber y
Steinerberger, arXiv:1601.02972, Thm 2.3,
https://arxiv.org/html/1601.02972 . No se atribuye ese resultado a esta ronda.
La búsqueda dirigida no identificó en el índice la concavidad de theta
MENOS uno usada abajo; eso no prueba prioridad ni exhaustividad literaria.

## 1. Teorema de concavidad geométrica puncturada

Sea

    θ(y)=Σ_{n∈Z}exp(-πyn²),  τ(y)=θ(y)-1>0.

**Teorema 1 (PROVED).** Para todo x∈R,

    d²/dx² log τ(exp x) < 0.

### Prueba: y≥1/2

Considere la probabilidad sobre n≥1 proporcional a exp(-πyn²), y ponga
M=E(n²), V=Var(n²). Con D=y∂y:

    D² log τ(y) = (πy)² V - πy M.

M≥1 y V≤E((n²-1)²). Al dividir por el peso de n=1,

    V ≤ Σ_{n≥2}(n²-1)² exp[-πy(n²-1)].

Cada y exp[-πy(n²-1)] decrece para y≥1/2. Sea q=exp(-π/2)<1/4.
Usando n²-1≥3(n-1) y (n²-1)²≤n⁴≤16^{n-1},

    πy V ≤ (π/2)Σ_{n≥2}(n²-1)²q^{n²-1}
           ≤ (π/2)Σ_{j≥1}(16q³)^j < π/6 < 1 ≤ M.

De ahí D²logτ<0. No se requiere una evaluación numérica de momentos.

### Prueba: 0<y≤1/2

Poisson da

    τ(y)=y^(-1/2) A(y),
    A(y)=1-r+ε(y),  r=√y,
    ε(y)=2Σ_{n≥1}exp(-πn²/y).

A>0. Escribiendo ε₁=Dε y ε₂=D²ε,

    A² D²log A
      = -r/4 +(1-r)ε₂ -rε/4 +rε₁ +εε₂ -ε₁²
      ≤ -r/4 +(1+ε)ε₂ +rε₁.                         (1)

Aquí ε, ε₁, ε₂ son positivos. Las siguientes cotas son uniformes:

    ε < 1/250,  ε₁ < 1/40,  ε₂/r < 11/50.            (2)

Para verificarlas sin numérica de theta, sea q₀=exp(-2π)<1/525.
La desigualdad q₀<1/525 se deduce de π>157/50 y
Σ_{k=0}^{20}(157/25)^k/k! > 525 (aritmética racional).
Las funciones y^{-j}exp(-πn²/y) crecen en 0<y≤1/2 para j=0,1,5/2.
Además n²≥1+3(n-1), n²≤4^{n-1}, n⁴≤16^{n-1}. Por tanto

    ε ≤ 2q₀/(1-q₀³) < 1/250,
    ε₁ ≤ 4πq₀/(1-4q₀³) < 1/40,
    ε₂/r ≤ 8√2 π² q₀/(1-16q₀³) < 11/50.

La última cota usa ε₂≤2π² y^{-2}Σn⁴exp(-πn²/y).
Todas las comparaciones finales se obtienen con π<22/7, √2<99/70
y q₀<1/525 mediante fracciones racionales.
Insertando (2) en (1):

    A²D²log A < r[-1/4+(251/250)(11/50)+1/40]
               = -(103/25000) r <0.

Como logτ=-1/2 log y+log A, se concluye el teorema. ∎

## 2. Anticorrelación exacta de divisores coprimos

En Z\{0}, defina P_y(N=n)=exp(-πyn²)/τ(y) y X_d=1_{d|N}.
Entonces

    r_d(y)=E_y X_d=τ(d²y)/τ(y),
    Cov_y(X_d,X_e)=τ(lcm(d,e)²y)/τ(y)-r_d(y)r_e(y).

**Corolario 2 (PROVED).** Si d,e>1 son coprimos, para todo y>0:

    Cov_y(X_d,X_e)<0,

es decir

    τ(d²y)τ(e²y)-τ(y)τ(d²e²y)>0.                    (3)

Prueba: para f(x)=logτ(exp x), a=2log d>0, b=2log e>0,

    f(x+a+b)+f(x)-f(x+a)-f(x+b)
      =∫₀ᵃ∫₀ᵇ f''(x+u+v) dv du <0.

Exponentiar y usar lcm(d,e)=de. ∎
Esto es un signo cruzado real, no la afirmación genérica Cov≥0 como matriz.

## 3. Un operador matricial positivo con estructura adicional

Sea d₁,…,d_m>1 una familia finita de enteros coprimos dos a dos, y
V_y=(Cov_y(X_di,X_dj)). Entonces:

- V_y es definida positiva: si Σa_iX_di fuera constante casi seguramente,
  N=1 da constante cero y N=d_i da a_i=0.
- Las entradas no diagonales son estrictamente negativas por (3).
- V_y^{-1} tiene todas sus entradas estrictamente positivas.

La tercera conclusión es elemental: tomar s≥λ_max(V_y), B=sI-V_y.
B tiene entradas no negativas, las no diagonales positivas, y radio
espectral s-λ_min(V_y)<s. Así

    V_y^{-1}=s^{-1}Σ_{k≥0}(B/s)^k,

con positividad estricta de toda entrada. Para m=1 la conclusión es obvia.
No se identifica V_y ni su inversa con el nodo de P47.

## 4. Signo entre factores primos completos

Sea Y_p=v_p(|N|)=Σ_{j≥1}X_{p^j}. Como log|N| tiene todos los momentos bajo
P_y, las siguientes series convergen absolutamente con sus pesos:

    log|N|=Σ_p(log p)Y_p,
    Cov_y(Y_p,Y_q)=Σ_{j,k≥1}Cov_y(X_{p^j},X_{q^k})<0,  p≠q.

La integrabilidad que permite los intercambios se obtiene de
Σ_p(log p)Y_p=log|N| punto a punto y
E(log²|N|)+(Elog|N|)²<∞. La fórmula de completitud equivale a
Σ_{d|N}Λ(d)=log|N|; no se usa como certificado de Q_T.

**Corolario 3 (PROVED, desigualdad estricta).** Para todo y>0:

    Var_y(log|N|) < Σ_p(log p)² Var_y(Y_p).           (4)

La diferencia es exactamente

    -2Σ_{p<q}(log p)(log q) Cov_y(Y_p,Y_q)>0.

La suma derecha es finita pues Σ_p(log p)²Y_p²≤log²|N|.
El signo estricto usa, por ejemplo, el par p=2,q=3. A diferencia de PSD de
una covarianza, (4) expresa una cancelación firmada entre factores primos.

## 5. Mellin positivo y límites del resultado

Para familia FINITA de d_i>1 COPRIMOS DOS A DOS y α>0, el kernel

    M_α(d,e)=∫₀∞y^{α-1}Cov_y(X_d,X_e)dy

converge (CONSTRUCTOR_002, lema 2), es definido positivo y tiene entradas
no diagonales negativas cuando los d_i son coprimos. Su inversa finita es
positiva entrada a entrada por el argumento anterior. Esto vale en α=1/4.

**No confundir α=1/4 con haber resuelto el peso crítico del nodo:** la
normalización por τ(y) cambia la transformada; quitarla introduce los
defectos y contraterminos calculados en CONSTRUCTOR_002. No se ha mostrado
que (3) o (4) dominen el déficit gamma.

Tampoco está demostrado que este signo falle al eliminar un primo: el
borrado puede preservar la anticorrelación. Se necesita un enlace específico
que deje de ser válido para el falsificador correspondiente. El resultado
positivo de esta nota es un lema aritmético auxiliar con signo estricto,
no el objeto completo solicitado en O1 ni el cierre de D.

Revisión final AUDIT_003: prueba y constantes aceptadas. La condición de
coprimalidad dos a dos de §5 se ha hecho explícita. No hay enlace Q_T probado.
