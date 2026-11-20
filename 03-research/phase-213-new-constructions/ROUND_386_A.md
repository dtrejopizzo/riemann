# Neutralizar la unión de todos los primos grandes: reducción a un producto finito

**Estado: PROVED, con revisión independiente de la precisión aditiva y la localización del corte.**

Sean W(y) el saldo de todos los enteros admisibles con algún primo >y y C(y)=S−W(y). En el corte z=L² existe y tal que

    log(x/y²)= E/2−1/2+o(1),     |W(y)| ≪ √x (log x)^O(1),

con E=∏_{p≤z}(1−1/p)^−1. Se puede escoger el lado W≤0 o el lado W≥0 con esa precisión. Así el criterio unilateral de 372 equivale al mismo techo para C(y), que incluye sólo divisores libres de cuadrados del producto de primos en (z,y]. La selección usa sólo W; no presupone el signo de S. El antecedente 385 neutraliza exactamente un primo grande y deja dos sectores; aquí se neutraliza toda la unión.

**Perfil a precisión aditiva.** Escribir v=log(x/y²)=κ log z. Para κ en cualquier compacto interior de (0,1), el primer marcado T de 385 es JxE/L²+o(x/L²), uniformemente: 384 da los momentos exactos y su resto absoluto O(x L^(−2.7)); los errores por cuadrados y PNT de 385 son menores. Para el sector de dos primos, en |u|≤v/2 la expansión de H(L−u) de 385 tiene error absoluto O(v²/L³), y fuera de esa banda el mayorante 2(v−u)_+/(L−v)² integrado contra la gaussiana tiene cola o(1/L²). El coste de cofactores distintos de uno también es o(x/L²). Como el peso exp(−u)g(u)/J es normal de media −1/2, el sector de dos primos tiene saldo

    2Jx(v+1/2)/L² + o(x/L²).

En la unión, el primer marcado cuenta una vez de más a los semiprimos; tres o más primos tienen masa despreciable. Luego

    W(y)=Jx/L² · [E−2v−1+o(1)].

La constante E se conserva exacta. Sustituirla por su equivalente de Mertens no justificaría el término aditivo −1.

**Elección del corte.** Por Mertens E/(2 log z)→exp(γ)/2<1. Tomar v=E/2−1/2±1; el perfil uniforme da signos opuestos. Al cruzar p sólo varían múltiplos de p y el salto cuesta O(x/p), que en toda esa banda es O(√x (log x)^O(1)). La unión cambia en un conjunto finito de primos para x fijo. Elegir cualquiera de los dos valores que encierran cero en el primer cruce, fijando por ejemplo el lado no positivo (si se alcanza cero, elegir ese valor). El salto acota el módulo, y el propio perfil fuerza v=E/2−1/2+o(1) para ambos lados. La elección es entre valores constantes en los intervalos de corte; no requiere monotonicidad.

La transformada de la suma restante en la escala de evaluación, con ambos extremos congelados, tiene el factor finito ∏_{z<p≤y}(1−p^(−s)). La gaussiana es la misma de 368. La reducción conserva la exigencia O_ε(x^(1/2+ε)) para la parte positiva; no transfiere un signo puntual en márgenes menores que el salto. Sigue abierta una cota unilateral de esa precisión para el producto finito con el corte seleccionado.

**Registro de revisión.** El primer marcado se conserva a error aditivo o(x/L²), no sólo relativo al término que contiene E; el resto O(xL^(−2.7)) de384 basta. En el segundo sector, ∫u exp(−u)g(u)du=−J/2 da exactamente el término v+1/2. Restar una sola copia de ese sector al primer marcado, para formar la unión completa, produce E−2v−1. Como E/(2log z)→exp(γ)/2∈(0,1), los dos valores v=E/2−1/2±1 están en un mismo compacto de κ y tienen signos contrarios con margen2+o(1). El coste de un salto dividido por x/L² tiende a0; el perfil aditivo fuerza por tanto la localización o(1), más precisa que un o(log z). La finitud de estados y la elección de uno de los dos lados no necesitan monotonicidad ni conocimiento del signo deS. El producto finito representa C sólo con sus extremos congelados en la escala de evaluación; no se afirma una única serie de Dirichlet para el corte móvil global.
