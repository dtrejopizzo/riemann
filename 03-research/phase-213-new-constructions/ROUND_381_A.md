# Saldo de todos los sectores de orden fijo y obstrucción al truncamiento

**Estado: PROVED, con revisión independiente de la convolución, su prolongación y el alcance del truncamiento.**

Con la notación de 379–380, para todo entero d≥1 fijo y 0<a<1 fijo,

    S_d ∼ (−1)^d J x P(0)/L · [log(L/b)]^(d−1)/(d−1)! .

Aquí S_d incluye todas las paridades del cofactor formado por primos entre z e y. La densidad de d primos sin ese cofactor ya aparece en 369. La afirmación presente transporta la densidad por la suma firmada de cofactores al corte exacto z=L².

**Sustitución prima.** Se aplican los recortes de 380, escribiendo n=m p₁⋯p_d y dividiendo por d!. Las repeticiones con p_i=p_j cuestan O_d(Y exp(−b)(1+L)^d) para factores ≤exp(2L), por g(log(Y/n'))≪Y/n', Σ_{p>y}p^(−2)≪1/y y la suma recíproca de los otros factores; Y=x/m. En las colas sin truncar, el coeficiente por producto tras ordenar y dividir por d! es ≤1. Reemplazar sucesivamente cada medida prima por dt/log t cuesta O_d(Y(1+L)^d exp(−c√b)): fijar los demás factores, aplicar la integración por partes de 380 y sumar sus recíprocos. Para d fijo los errores sobreviven la suma absoluta de cofactores con ahorro mayor que cualquier potencia de L.

**Densidad y derivadas.** Sea H_d(D) la convolución d veces de 1_{v≥b}/v en la escala logarítmica, dividida por d!. Para d≥2 y D>db, multiplicar por D=Σv_i y usar simetría da

    D H_d(D)=(1/(d−1)!)∫_{v_i≥b, Σv_i≤D−b} ∏_{i=1}^{d−1} dv_i/v_i.

Para D=L, el simplex contiene el cubo [b,(L−b)/(d−1)]^(d−1) y está contenido en [b,L]^(d−1). Integrar en los dos cubos da H_d(L)∼[log(L/b)]^(d−1)/((d−1)! L). Para justificar la suma firmada, cambiar v_i=b+(D−db)u_i: el dominio pasa al simplex fijo u_i≥0, Σu_i≤1. En |D−L|≤L/2, para L grande, Re(D−db)≥L/3; cada factor del integrando en módulo está acotado por C L/(b+Lu_i). Esto da prolongación holomorfa y cota O_d(H_d(L)) integrando en el cubo unidad. Para d=1 se usa H_1(D)=1/D cerca de L.

Luego el argumento de Taylor y los momentos de P de 380 se aplican con esta H_d: grado fijo N elegido para absorber L^C(b/L)^N/P(0), y términos no constantes de tamaño relativo O_{i,d}((b/L)^i). Fuera de |u|≤√L la densidad real se acota por O_d((1+log(D/b))^(d−1)/D) en D≥db, suficiente por decaimiento gaussiano. El término principal tiene signo (−1)^d y es el indicado.

**Consecuencia.** Para cualquier corte fijo d₀≥1, la suma hasta d₀, incluido el sector cero despreciable de 379, es asintótica a S_(d₀). Su complemento es asintótico a −S_(d₀) por el techo de 377. Los equivalentes a orden fijo dejan deliberadamente fuera la suma cuando d₀ crece con x; la razón equivalente entre sectores consecutivos sólo está justificada aquí a d fijo. Así queda descartado atribuir el signo global al predominio de cualquier último sector fijo.

**Registro de revisión.** La identidad D H_d usa d términos simétricos, por lo que el factor resultante es d/d!=1/(d−1)!, sin una multiplicidad adicional. En el cambio al simplex fijo el integrando completo es el producto de (D−db)/(b+(D−db)u_i), con d−1 factores; la cota C_d L/(b+Lu_i) y |D|≥L/2 justifican la holomorfía y el techo O_d(H_d(L)). El cubo interior tiene lado superior (L−b)/(d−1), cuyo logaritmo relativo a b difiere de log(L/b) sólo en O_d(1). Así se obtiene el coeficiente principal exacto antes de aplicar los momentos firmados de380. Las repeticiones, las colas y los d reemplazos PNT se pagan en módulo con un factor polinómico en L para d fijo; los ahorros exp(−b), exp(−c sqrt b) y exp(−cL/b) dominan esos factores para cada a fijo en(0,1). Finalmente el techo de377 es menor que cualquier S_d de orden fijo en módulo, de modo que el complemento cancela su término principal; no determina el signo del residuo ni permite sumar el equivalente uniformemente en d creciente.
