# POWER_PACKET_SCOPE_AUDIT_009 — Familia Tate racional, paquetes centrales y alcance del puente

Estado: PROVED concentración, identidades y auditoría de puente; OPEN desigualdad aritmética finita. No se modifica ningún paper ni se utiliza una reducción espectral externa.

## 1. Antecedentes concretos, con su alcance

Leídos ROUTES-TRIED-INDEX/06 (R2 y R5), Paper47 lem:wit-conc, prop:wit-Egamma, prop:Egamma-exact y rem:critical; phase188/L2_BUILD_008_GROUND_STATE_AND_T0.md, L2_BUILD_009_ARITHMETIC_INPUT_FOR_T0.md, L2_BUILD_010_REGULARIZED_CENTRE_VALUE.md y N_BUILD_013_E_GAMMA_C_COLLAPSES.md. Se consideran sólo sus formulaciones de forma y fluctuación; no se emplean argumentos de otra naturaleza para desestimar vías.

R2 trabaja con una función compacta clamped por ventana, ground/near-ground de una forma arquimediana. R5 trabaja con paquetes compactos que concentran en una frecuencia. La presente familia f_n=(D²-1/4)y^(n-1)e^(-uy), u31.5 fijo, no es idéntica a ninguna de ellas para n finito: tiene semirrecta exponencial, polos racionales y autocorrelación exponencial por polinomio. Sin embargo su límite central y el umbral de fluctuación son del mismo tipo E0 ya registrado; no aparece una holgura asintótica nueva.

## 2. Concentración central demostrada y umbral coincidente

Su probabilidad espectral p_n es proporcional a (tau²+1/4)^2/(u²+tau²)^n. Las fórmulas beta para la medida base de POWER_PRIME_PATTERN_FALSIFIER_008 muestran, para u fijo y n grande,

    E_n tau² = u²/(2n)(1+O(1/n)),
    E_n tau^4 = O(n^-2).

Se obtiene expandiendo los momentos exactos M2,M4,M6 (y M8 para la segunda línea) en los cocientes de reponderación. En particular p_n converge débilmente a delta0, y

    rho_n(t)=c_fn(t)/||f_n||² ->1

localmente uniformemente: 0<=1-rho_n(t)<=t² E_n tau²/2. La desigualdad global m0<=m(tau)<=m0+17tau² da Arch_n->C0; el multiplicador acotado 1/(tau²+1/4) da e_n->4.

La identidad Tate de eliminación del término principal vale también aquí, porque las integrales exponenciales convergen absolutamente y A=B=0. Si S_n es el peine normalizado y Fcal_n su fluctuación respecto de densidad2e^(t/2), entonces

    S_n=Fcal_n-e_n,
    W_n=Arch_n+e_n-Fcal_n.

Por tanto el umbral del problema límite es C0+4, exactamente el centro E0 de R2/R5. La condición necesaria de signo produce limsup Fcal_n<=C0+4. No se demuestra aquí que esta condición límite baste para los signos finitos, ni que la media aritmética converja. La convergencia local de rho_n a1 no permite intercambiar la suma infinita del peine: sus pesos no son sumables uniformemente en n. Esa es una obligación matemática real, no una razón para abandonar el caso finito.

## 3. Palanca finita distinta: una recurrencia exacta que todavía exige signo

Para n suficientemente grande defina

    J_n(t)=integral_R exp(i tau t)(tau²+1/4)^2/(u²+tau²)^n d tau,
    rho_n(t)=J_n(t)/J_n(0), w(tau)=1/(u²+tau²).

La normalización y derivación bajo la integral dan

    p_(n+1)=w p_n/E_n[w],
    J_(n+1)(t)=-(1/(2nu)) partial_u J_n(t),
    rho_(n+1)(t)-rho_n(t)
        =-partial_u rho_n(t)/[2nu E_n(w)].

El paso de n es por tanto explícito, con constantes de normalización racionales en u gracias a las integrales beta. Para la parte arquimediana,

    Arch_(n+1)-Arch_n=Cov_n(m,w)/E_n(w)<=0,

porque m crece y w decrece en |tau|. Para la forma completa,

    W_(n+1)-W_n
       =Arch_(n+1)-Arch_n
        -sum_(q>=2)2Lambda(q)q^-1/2[rho_(n+1)(logq)-rho_n(logq)].

Cada suma a n finito converge absolutamente por el decaimiento exponencial por polinomio. No tiene signo automático. Una desigualdad unilateral que controle esta diferencia, o una razón renormalizada que preserve no negatividad, sería un avance diferente del mero valor límite E0. No se encontró en las búsquedas dirigidas una prueba previa de ese paso exacto para la familia racional presente. Esta novedad es local y acotada; las identidades de reponderación y covariance son elementales conocidas.

No se propone exigir que W_n sea creciente: el sentido apropiado de una inducción debe ser demostrado y compatible con sus márgenes. Tampoco el signo de esta única cadena controlaría por sí solo todos los numeradores de cada grado.

## 4. Reauditoría del puente: sin defecto encontrado

POWER_BRIDGE_002 se revisó otra vez en sus dos rutas. En la norma B, las traslaciones G(y+logn) son contracciones de la norma intrínseca H^(1/4), y los coeficientes n^-5/4 son sumables. No se deriva Z término a término: se evita la serie potencialmente divergente de derivadas. La extensión por cero para t<1/2 es estándar y controla el salto en el extremo; la constante de Hardy fraccionaria se invoca explícitamente como herramienta conocida.

Para datos PW_N C², dos integraciones por partes en h y xh dan rho,rho'=O(X^-2); el split de diferencias demuestra pertenencia a B sin suponer una tercera derivada. La aproximación C1 tras z=e^-y usa funciones compactas suaves y produce exactamente exponentes32+k; converge fuertemente en B. La continuidad de gamma, peine y momentos se controla por separado.

Para un test F compacto suave arbitrario, trasladarlo a soporte(0,L) conserva la forma completa: la autocorrelación es invariante y los dos momentos se multiplican por factores recíprocos. La inversión u(y)=sum mu(n)n^-1/2 h(y+logn) es FINITA, y al aplicar Z la suma de divisores también es finita, de modo que Zrho=h exactamente. El dato inverso es suave hasta0 y compacto en la semirrecta, así pertenece a B. No se le exige valor cero en0. Todo este paso vale sin suponer el signo buscado.

Así la positividad de TODOS los tamaños de la escalera fija sí sería suficiente para todos los tests compactos y, por núcleo de forma en cada ventana, para el dominio pertinente. Se extiende de tests reales a complejos por separar partes real e imaginaria, ya que la forma tiene núcleo real. El puente no aporta el signo de la escalera, no justifica extrapolar V12 a más modos y no vuelve densa la unión de planos pequeños ya positivos.
