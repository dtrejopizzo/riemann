# Transición cuantificada y corte que neutraliza el sector de un primo

**Estado: PROVED, con revisión independiente del perfil, los signos y la selección por saltos.**

Sean L=log x, z=L², v=κ log z, y=exp((L−v)/2), y V(y) el saldo de los enteros con exactamente un primo >y en la criba de 368. Para κ en cualquier compacto de (0,1), uniformemente,

    V(y) = (J x log z/L²) (exp(γ)−4κ+o(1)).

En consecuencia a cada x suficientemente grande se puede elegir un umbral y con κ=exp(γ)/4+o(1) para el cual |V(y)|≤x^(1/2+o(1)). El corte inferior de admisibilidad sigue siendo z. El paso de selección por saltos tiene antecedente en 303 para otra suma; aquí se calcula el perfil de transición en la suma de paridad del corte exacto.

**Primer marcado.** Sea T la suma completa con cada término multiplicado por su número de primos >y. Como en 384 vale T=−Σ_{p>y}f(L−log p) salvo la corrección por p|m al marcar n=mp. Para n≤x² esta corrección en módulo cuesta O(x L Σ_{p>y}1/p²)=O(xL/y), pues g(log(x/n))≪x/n y se suma sobre p²|n. Por encima de x² basta la cola gaussiana con multiplicidad O(log n). La integral y los dos momentos de 384 dan T=(1+o(1))JxE/L²: ahora su extremo L−log y=(L+v)/2 sigue en [0.4L,0.6L]. Todos los costes de 384 son uniformes allí.

**Doble marcado.** Tres primos >y dan n≥y³ y coste O(x exp(−cL²)) aun ponderando por log³ n. Con dos primos grandes y cofactor distinto de uno se tiene n≥y² z=x z^(1−κ); por suma diádica gaussiana sobre todos los enteros el coste es O(x exp(−c(log z)²)), despreciable incluso respecto de x/L². Así el saldo con dos primos grandes es, al orden buscado, la masa positiva de semiprimos pq con p,q>y. Sustituir las dos medidas primas por dt/log t como en 380 cuesta O(x L² exp(−c√L)), y la diagonal O(x/y). Poner b=log y. La densidad continua calculada en 380 es H(D)=log((D−b)/b)/D para D>2b. La masa es

    x ∫_{u<v} exp(−u) g(u) H(L−u) du.

Para |u|≤v/2 se tiene H(L−u)=2(v−u)/L² ·(1+O(v/L)), por 2b=L−v. Para todos los u<v se tiene H(L−u)≤(v−u)/(2b²), por log(1+t)≤t. Las colas gaussianas fuera de |u|≤v/2 son por ello o(v/L²) después de integrar. La integral vale (2J+o(1))v/L². El saldo de exactamente un primo es T menos dos veces este sector, con error despreciable por los tres o más primos. El equivalente de Mertens E∼exp(γ)log z da la fórmula.

**Selección a precisión de raíz.** Al cruzar un solo primo p la indicadora de exactamente un primo grande cambia sólo en múltiplos de p; la variación del saldo es ≤Σ_m g(log(x/(pm)))≪x/p por conteo diádico. Elegir un intervalo fijo [κ₋,κ₊]⊂(0,1) que contenga exp(γ)/4 en su interior. En los extremos hay signos opuestos para todo x grande. Algún par de valores sucesivos del saldo encierra cero (o se alcanza cero); uno tiene módulo O(x/y_min)=O(√x z^(κ₊/2)). Como el perfil es uniforme, cualquier valor así elegido tiene κ=exp(γ)/4+o(1). Borrar ese sector adaptativo conserva los techos unilaterales de potencia 1/2+ε. Aún se necesita la cancelación entre los sectores con cero y dos primos grandes; su suma no queda decidida.

**Registro de revisión.** El primer marcado cuenta S₁+2S₂ salvo los sectores de tres o más primos grandes y la corrección por p|m; esta última es de raíz por xL/y y no exige que2log y exceda L. La aplicación de384 sólo reutiliza sus momentos congelados y su sustitución PNT en el extremo u=(L+v)/2∈[0.4L,0.6L], uniformemente. Para κ en un compacto[κ₋,κ₊]⊂(0,1), las colas con cofactor no trivial tienen separación mínima (1−κ₊)log z y el núcleo semiprimo tiene v≥κ₋log z→∞. Esto justifica ambos recortes gaussianos uniformes. La integral semiprima principal es2Jv/L²; el segundo marcado la resta dos veces y produce exactamente−4κ, mientras Mertens aporta+exp(γ). Al seleccionar el corte no se presupone monotonicidad de V: hay un número finito de estados entre los extremos y algún salto debe cruzar0. Sus dos estados son realizables por umbrales contiguos a p, respetando la desigualdad estricta p>y. El máximo salto es O(√x z^(κ₊/2)), menor que x log z/L² por una potencia de x; por eso el perfil uniforme fuerza κ=exp(γ)/4+o(1). No se obtiene un signo ni un techo de raíz para la suma completa a partir de este corte adaptativo.
