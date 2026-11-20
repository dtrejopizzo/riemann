# Un solo test compacto para todos los centros del primer filtro

Fijar a>0. Hay fallo del signo global si y sólo si existen un perfil real F∈C_c^∞(0,1), con ∫F dx=∫F dx/x=0, y c>0 tales que

    B∞(Rγ F) ≤ −c/(1+γ²)   para todo γ real,

donde Rγ multiplica la Mellin por 1/(s+a−iγ). Se puede elegir F de norma de energía uno por homogeneidad. F depende de a. La vuelta es inmediata porque cada RγF pertenece a X₀. La ida requiere una aproximación simultánea; la densidad punto a punto de 033 no basta para intercambiar los cuantificadores.

**Prueba.** Si Γ>0, elegir el extremizador real unitario u de 034. Por 036, B∞(Rγu)=−κ I(Rγu) con κ=Γa/(a+1/2). Tomar un mollificador real no negativo de masa uno, suave y compacto en (0,ε), y llamar J a su convolución causal en t=−log x, extendiendo por cero para t<0. Es un promedio de las isometrías S_r de 034, r=exp(−t) para el desplazamiento t. Preserva la media nula y conmuta con Rγ. J y su adjunto en X₀ convergen fuertemente a la identidad: las traslaciones son isometrías fuertemente continuas y ||S_r* v−v||≤||v−S_r v||. Por compacidad del representante A, aproximándolo por operadores de rango finito se obtiene ||J*AJ−A||→0. Fijar ε con error menor que κ/2. Entonces B∞(Rγ Ju)≤−κ I(Rγu)/2 para todos los centros a la vez.

Escribir G para la Fourier de la derivada logarítmica de u. Hay masa positiva de |G|² en algún intervalo acotado. Sobre ese intervalo a²+(t−γ)²≤C(1+γ²), luego I(Rγu)≥c₀/(1+γ²). Por otro lado, para el J ya fijado, con símbolo j(t) de Schwartz, se tiene

    sup_γ (1+γ²)||Rγ J||² ≤ sup_t |j(t)|² [2+(1+2t²)/a²] < ∞

en norma de energía, por Plancherel. Así las formas (1+γ²)B∞(Rγ Jp) son equicontinuas en cada bola de energía: su diferencia entre p y u está acotada por una constante independiente de γ por ||p−u|| (||p||+||u||). Usar la densidad doblemente primitiva de 033 para elegir ahora p real suave compacto de ambos momentos cero con error menor que la mitad del margen. F=Jp es suave compacto en (0,1); cada traslación preserva la anulación de los dos momentos, y lo mismo vale para su promedio. Esto da la desigualdad anunciada.

**Cola con los pesos originales.** Para un test compacto como éste se puede elegir a=1 desde el principio. En general, si supp F⊂[δ,1], w=a−iγ y M_F(s)=∫F(x)x^(s−1)dx, el perfil filtrado v es

    v(x)=x^w ∫ₓ¹ F(y)y^(−w−1)dy,   0<x<1.

Por debajo de δ vale exactamente M_F(−w)x^w. Para n≥1/δ el contacto físico de 032 es por tanto ∫conj(v(y))v(y/n)dy = n^(−w) M_F(−w) conj(M_v(1+conj(w))). Aquí M_v(1+conj(w))=M_F(1+conj(w))/(1+2a). Multiplicando por Λ(n)/n y sumando, toda la cola discreta se evalúa mediante la serie absolutamente convergente ΣΛ(n)n^(−1−w) menos su prefijo. En la forma se resta el doble de la parte real. La identidad calcula la cola y deja por controlar el signo de su suma con el prefijo y la parte arquimediana. Si se usa el híbrido de 032 hay que descontar también la cola continua correspondiente al comparar las dos formas.

**Consecuencia.** Para probar el signo basta encontrar un centro de energía no negativa para cada test inicial doblemente primitivo suave compacto, a un solo ancho fijado. Más débilmente basta excluir un margen estrictamente negativo uniforme tras multiplicar por 1+γ². La construcción no encuentra todavía ese centro. 018 daba recuperación test a test y 033 densidad en norma; el paso adicional es fijar un mollificador antes de la aproximación para controlar la familia no acotada de centros. Prueba y cálculo de cola revisados independientemente.

## Anulación exacta de la cola en una retícula completa

Bajo la misma hipótesis Γ>0, el test puede elegirse de modo que sus primeros filtros sigan siendo negativos en todo centro real y, además, *todos* los filtros de una retícula infinita sean suaves, doblemente primitivos y estén soportados en una misma ventana finita. Esto elimina la cola discreta en esos centros sin estimar la serie de Dirichlet.

Sea F el test anterior, supp F⊂[δ,b]⊂(0,1), y definir F_D=F−e^(−aD) S_{exp(−D)}F, donde S_r F(x)=F(x/r) con extensión por cero. En norma de energía S_r es isométrico y conmuta con Rγ. Por 036 y continuidad a γ finito, H=sup_γ(1+γ²)I(RγF)<∞. El cambio de energía filtrada, multiplicado por 1+γ², tiene valor absoluto a lo sumo ||A|| H(2e^(−aD)+e^(−2aD)). Fijar D suficientemente grande para que este error sea inferior a la mitad del margen inicial. El mismo D sirve para todo γ. Ambas condiciones de momentos pasan a F_D.

En la retícula γ_k=2πk/D, k entero, el numerador de Mellin es 1−exp(−(s+a−iγ_k)D). Por ello hay identidad de perfiles

    R_{γ_k}F_D = T_k F = ∫₀ᴰ exp((−a+iγ_k)t) S_{exp(−t)}F dt.

Cada perfil es suave y sus dos momentos se anulan integrando los de las dilataciones. Su soporte físico queda dentro de [δ exp(−D),b]. Todo contacto con n≥exp(D)/δ desaparece, con el mismo corte para cada k. En esa retícula la forma completa coincide con la energía primitiva de P47 en una ventana logarítmica común. El semiancho necesario es a lo sumo (D+log(b/δ))/2 tras centrar. No hay aquí cota universal para D.

**Comprobación por suma.** Para cualquier F en X₀, Parseval en [0,D] con valores en el espacio de energía da

    Σ_{k∈ℤ} B∞(T_kF) = D [1−exp(−(2a+1)D)]/(2a+1) B∞(F).

En efecto T_kF son los coeficientes de Fourier sin normalizar de exp(−at)S_exp(−t)F; aplicar Parseval polarizado con el operador acotado A. La serie converge absolutamente por |B∞(v)|≤||A|| I(v) y Parseval para I. Finalmente B∞(S_exp(−t)F)=exp(−t)B∞(F). La identidad suma los signos individuales; no asegura el signo de cada término.

Antecedentes: SELECTION_027, P47 rem:Sren y POWER_DESCENT_016 ya recogen el retardo que trunca un promedio exponencial. Aquí una sola perturbación pequeña de F conserva el margen y trunca simultáneamente toda la retícula. La negatividad de estos perfiles individuales no implica negatividad de su espacio generado ni da un test negativo incondicional. Prueba auditada.
