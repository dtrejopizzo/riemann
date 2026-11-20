# QRH — operador exacto de réplicas y canal coherente

2026-10-19. **PROVED: descomposición, control de varianza y equivalencia
interna de estimaciones. OPEN: estimación selectiva crítica. No signo de D.**

## Corpus y diferencia explícita

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX (L74 y entrada QRH), grid
R162_2300_MASTER_GRID y CROSSWORD-TO-D.md. Punto de partida:
QRH_EXPONENT_MAP.md y OpenAI, PDF de5Oct2026, §§2.2 y3.
La diferencia es calcular el operador de la selección p^6, no volver a
aplicar la criba de toda la familia. No se propone una fuente de signo
nueva ni una construcción de otra familia. Las conclusiones siguientes
son algebraicas y usan sólo conteo elemental de ideales.

## Dominio y réplica exacta

Trabajamos en el campo fijo K=Q(sqrt(-3)) y con los ideales, símbolos y
extensiones por cero del PDF. Fijados el carácter finito ν, el conjunto
finito S y W∈C_c^∞((0,∞)), sean

    A = A_1(D) = Σ_(n,S)=1 μ(n)ν(n)W(Nn/D),
    P_D = {p∉S primo ideal: Y/2<Np≤Y},    Y=sqrt(D),
    J = #P_D.

Para D suficientemente grande J>0 (el argumento publicado incluso usa
J≈Y/log Y); ninguna estimación inferior cuantitativa de J se necesita
para las identidades normalizadas siguientes. Todos los promedios son
uniformes sobre P_D. La identidad del símbolo χ_n(p^6)=1_(p∤n) prueba
exactamente

    A_(p^6)(D) = A − B_p(D),
    B_p(D) = Σ_(n,S)=1,p|n μ(n)ν(n)W(Nn/D)
           = −ν(p) Σ_(m,S)=1,p∤m μ(m)ν(m)W(Np Nm/D).

La última igualdad incluye la condición p∤m: sin ella la fórmula sería
incorrecta para m divisible por p. No se ha estimado una suma firmada.

## Cota uniforme y varianza (PROVED)

Sea supp W⊂[u,v]⊂(0,∞). El conteo de ideales en este campo fijo da
#{m:Nm≤X}≤C_K X para X≥1. En la última suma sólo aparecen ideales con
Nm≤vD/Np≤2v sqrt(D). Como |μν|≤1,

    |B_p(D)| ≤ C_(K,W) sqrt(D).

Las constantes pueden depender del carácter, S y W fijados; son uniformes
en D y p. En particular, escribiendo barB=J^(-1)Σ_p B_p,

    |barB|² ≤ C D,
    Var(B) := J^(-1)Σ_p |B_p−barB|²
            = J^(-1)Σ_p|B_p|²−|barB|² ≤ C D.

Esto controla la varianza a la escala requerida sin criba ni cancelación.

## Descomposición del operador (PROVED)

En C^J con norma cuadrada J^(-1)Σ|z_p|², sea P la proyección ortogonal
sobre el vector constante 1. El vector de réplicas es R=A1−B. Entonces

    PR=(A−barB)1,         (I−P)R=−(B−barB1),
    E_sel(D):=J^(-1)Σ_p |A_(p^6)(D)|²
              = |A−barB|² + Var(B).

El término todavía no controlado es el canal CONSTANTE, no la varianza.
Una cota sobre las diferencias de filas, incluso perfecta, no acota este
canal: sumar z1 a todas las filas deja todas las diferencias invariantes.
Esta observación sólo describe la pérdida algebraica; no es un no-go para
usar estructura aritmética adicional.

## Alcance exacto de la estimación propuesta (PROVED)

Las siguientes dos familias de estimaciones, cada una requerida para
todo ε>0 y permitiendo renombrar ε, son equivalentes:

    (i) E_sel(D) ≪_ε D^(1+ε),
    (ii) |A_1(D)| ≪_ε D^(1/2+ε).

En efecto, punto a punto en D,

    E_sel(D) ≤ 2|A|² + 2 C D,
    |A|² ≤ 2 E_sel(D) + 2 C D.

La segunda desigualdad resulta de A=A_(p^6)+B_p y promediado; la primera
es la desigualdad inversa de igual tipo. Se renombra ε al pasar entre
amplitud y energía. Así, seleccionar las réplicas no transforma la
estimación crítica en un mero control de fluctuaciones entre filas.
Tampoco la hace falsa: ambas estimaciones permanecen OPEN aquí.

## Qué se intentó y qué falta

Se calculó el operador exacto y se controló Var(B) mediante la suma
aritmética explícita para B_p. Esto deja |A−barB|², con |barB|≪sqrt(D).
No se obtuvo una identidad o estimación nueva que controle ese componente
coherente. La cota publicada para TODAS las filas hasta H=D^(1+ϑ) no
cubre las réplicas de altura N(p^6)≈D^3. Aun concediendo la misma cota
DH en H=D^3, dividir por J≈sqrt(D)/log D daría D^(7/2)log D para la
energía media, muy lejos de D^(1+ε).

Por tanto el objetivo selectivo es una formulación exacta del problema
de cancelación de A_1 a esa escala, con una varianza auxiliar ya controlada;
no una prueba nueva de esa cancelación. No se afirma imposibilidad de
mejorarlo ni se invoca ninguna equivalencia externa de D. Sigue pendiente
además una identidad que conecte tal cancelación con el contratermino017.

## Revisión independiente

El revisor verificó la identidad con p∤m, el conteo uniforme, la
descomposición ortogonal y ambas implicaciones. Su precisión sobre
los cuantificadores de ε quedó incorporada: no se afirma equivalencia
con el mismo ε fijo. Revisión favorable con este alcance; el componente
coherente y la estimación sin centrar permanecen OPEN.

## Continuación: ataque directo a la media coherente

Se examina C_D=A_1−barB. Se conserva el
mismo objeto externo, con los mismos W,ν,S fijados; no se relanza una
descomposición genérica de Möbius como si fuera una ruta nueva para D.

Poner a_n=μ(n)ν(n)W(Nn/D) y
r_D(n)=#{p∈P_D:p|n}. Intercambiar las sumas finitas da exactamente

    C_D = Σ_n a_n w_D(n),       w_D(n)=1−r_D(n)/J.

Siempre 0≤w_D≤1. Si D>(8v)², ningún ideal del soporte Nn≤vD puede
ser divisible por tres primos distintos del bloque: su producto tendría
norma mayor que D^(3/2)/8>vD. Así r_D≤2 y w_D≥1−2/J.
La máscara no aporta un nuevo factor oscilante a μ(n)ν(n).

Se obtiene asimismo una fórmula de escalas más cortas con el MISMO W:

    B_p(D)=−ν(p)A_1(D/Np)+O_(K,W)(1).

En efecto, quitar p∤m de la suma exacta agrega sólo m=pℓ con
Nℓ≤vD/(Np)²≤4v, un conjunto acotado independientemente de D,p.
Por tanto

    C_D=A_1(D)+(1/J)Σ_p ν(p)A_1(D/Np)+O(1).

Esta identidad no acota el primer término. Mejorar los sumatorios de
escala D/Np≈√D reduce el error de aproximación a A_1; no demuestra
cancelación nueva del término de escala D.

Finalmente, expandir el cuadrado da

    |C_D|² = Diag_D + Off_D,
    Diag_D=Σ_n |a_n|² w_D(n)² ≪ D,
    Off_D=Σ_(n≠m) a_n conjugate(a_m) w_D(n)w_D(m).

La cota diagonal usa |μν|≤1, W acotado, conteo de ideales y w_D≤1.
Off_D es real por emparejamiento de los índices y Off_D≥−Diag_D.
La cota crítica requeriría Off_D≪_ε D^(1+ε), como cota superior
para todo ε>0, permitiendo renombrarlo al pasar a la amplitud.
**Esa cota de términos cruzados no se ha probado.** El control de la
varianza entre réplicas no la aporta: conserva el mismo canal constante.

Resultado de esta continuación: fórmulas y diagonal verificadas, sin
estimación crítica nueva de C_D. No se declara una imposibilidad general,
un cierre de ruta por mera reformulación ni un avance de signo de D.
