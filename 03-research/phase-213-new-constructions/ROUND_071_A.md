# En la frontera crítica las filas de cada signo exceden el margen raíz

Usamos U_m, y, θ y B de 070. En toda la frontera admisible 1<B≤2, θ=1−B/2, el control O(√x) por módulos falla. Si 1<B<2, para todo x suficientemente grande la masa de filas positivas y el módulo de la masa de filas negativas superan, cada uno,
    
    √x exp(c log x / log log x)

para alguna constante c>0. Si B=2, θ=0, la misma cota se alcanza sobre sucesiones de cuartas potencias para cada signo. Los enunciados se refieren a las filas del sector t_y(m)≤x^θ. No se resta una masa de la otra.

Mantener el intervalo físico [A,C] de 070 sobre el cual k₀ tiene signo constante y |k₀|≥c₀>0. En las familias siguientes los primos del numerador tienden uniformemente a infinito y x/m pertenece a ese intervalo. Por la identidad exacta de 070 cada fila vale μ(m)k₀(x/m).

**Cofactor grande permitido.** Escribir L=log x, l=log L, f=B/2, y=L^B. Formar s con k primos distintos en [y exp(−B),y]. Elegir k de la paridad deseada como el menor con k(B l−B)≥fL+|log A|. Así
    
    k=fL/(B l−B)+O(1),    s≥x^f/A,    log s=fL+O(L/l).

Para cada s tomar todos los primos q en [x/(Cs),x/(As)]. El intervalo tiene razón fija >1, q≤x^θ, y sus extremos son x^(θ+o(1)), uniformemente en s. Como θ>0, por PNT hay ≫x/(s L) primos allí. Son mayores que y y únicos en la factorización de m=sq. Todos los m construidos tienen el mismo signo de Möbius.

Sea H=Σ_{y exp(−B)≤p≤y}1/p=(B+o(1))/log y por PNT y sumación parcial. Al elegir sucesivamente k primos con pesos 1/p, el peso máximo excluido en cualquier paso es k exp(B)/y=o(H). Por tanto la suma de 1/s sobre productos distintos es al menos [H(1−o(1))]^k/k!. Stirling da como cota inferior para el logaritmo del número de filas
    
    L−O(log L)+k[1+log(B/f)−l+o(1)].

En efecto log(H/k)=−l+log(B/f)+o(1). Por la elección de k se tiene k(l−1)=L/2+O(l). La cota inferior resulta L/2+k(log 2+o(1)). Cambiar la paridad de k cambia el signo de la familia; el intervalo de q se eligió después de s, por lo que ambas familias existen al mismo x. Esta elección evita la pérdida subexponencial de un conteo a razón de potencias como el de 070.

**Sólo primos pequeños (B=2).** Aquí no hay primo q de ajuste. Tomar una escala auxiliar X, L=log X, y=L² y k=L/(2 log L)+O(1) de paridad prescrita. Formar productos s de k primos distintos en [y/16,y/2]. Todos satisfacen log s∼L uniformemente. Usar pesos 1/√p. Su suma por PNT es
     
    H∼2(1/√2−1/4) L/log y ∼ 2(1/√2−1/4) k.

El peso excluido en cada paso es a lo sumo 4k/√y=o(H); por tanto Σ_s 1/√s≥[H(1−o(1))]^k/k!≥exp(c₁ k), pues 2e(1/√2−1/4)>1. Partir el rango de s en O(log X) intervalos de razón fija ρ<C/A. En alguno, [M,ρM], la suma de pesos es ≥exp(c₂k) para 0<c₂<c₁ fijo y X grande; esto da al menos √M exp(c₂k) productos. Elegir x=j⁴ en [AρM,CM], como en 070. Entonces (log x)²∼y y todos los primos elegidos están bajo el umbral. El signo se fija por la paridad. El mismo x para las dos paridades no se deduce de este argumento.

**Consecuencia.** Para 1<B≤2 la condición estricta θ<1−B/2 de 070 es exacta para poder retirar todo el sector sumando módulos a coste O(√x). En la igualdad el factor que vence la raíz es subpolinómico, compatible con el exponente limsup 1/2 de 070. El saldo firmado de esas masas y el signo de toda la forma permanecen pendientes.
