# POWER ENERGY AUDIT 041

Estado: ENERGY_BAND041 APROBADO. Papers intactos.

## 1. Corpus y diferencia

Reconsultados índice ROUTES-TRIED-INDEX, grid y crucigrama; contrastados LOW_TABLE018, CELL_BALANCE024, INTERIOR_SCALE030, GAMMA_WEIGHT031 y CRITICAL_BALANCE040. Las representaciones conjuntas y la integración por partes no son nuevas. La diferencia041 es una desigualdad firmada sobre una banda móvil de energía REAL, conservando el factor diferencial antes del error y comparando su resto con un beneficio de la MISMA escalaC_N. No se confunde ese beneficio con W total.

## 2. Expansión trasladada y bordes — APROBADOS

Revisados `POWER_ENERGY_BAND_041.md` y `tools/power_energy_band_041_verify.py`; ejecución independiente PASS. La serieS(ell) es absoluta en sigma1+delta>1. Trasladar el argumento en Fourier añade un factor de módulo1 y mantiene el error uniforme040. Integrar(exp−δell)(δ−D)f y su cuadrado da exactamente ENDS: primer borde1−e^−δLf(L), segundo−γ[z(0)−e^−δLz(L)]. Sólo se usa un intervalo finito; no se intercambia una serie críticaΣ|μ|/n.

CURV040 da q′(T+s)>b(T/(T+s))²>b/2 en0≤s≤L, porqueL<T/4; q″<0 da q′<b. El integral de q−v cuesta al menosbL²/4 y el cociente del factor1/2+q aporta a lo sumobL. ConL≥8 resulta logf(L)<−1/1600 y f(L)≤1−1/3200. En toda la banda f≤2, los bounds directos de f′ y f″ son correctos y sus constantes decrecen conN. Los dos bordes z y el errorE_NL dejan GAIN>1/12800.

## 3. Normalización física y B con saltos — APROBADOS

El cambio x=e^(T+ell) produce exactamente, para el término−γx deB,

−2γC_N∫_0^L e^−δell S(ell)dell.

No falta factor x, e^T o g(T). El resto se divide porC_N como2e^−T e^−(1+delta)ell V(x)S(ell), de donde sale el mayorante16e^−T L(T+L+1).

La identidad B+γx=T_n−theta logn−x epsilon_n es exacta, con1≤T_n≤1+logn y0<epsilon_n<1/n. Da|B+γx|≤logx+1 también n1 y en todos los saltos. No se sustituye el B real por una aproximación continua sin costo.

EXP/DER implican|S|<8 con holgura. T>N/1984,T<N yL+1<N permiten V-ERROR<32N²e^−N/1984; el cuarto término positivo de la exponencial y el extremo monótonoN0 certifican costo<C_N/25600. Comoγ>1/2 y GAIN>1/12800, se obtiene sobre TODA la banda

2∫_(e^T)^(e^(T+L))h_N(x)B(x)dx<−C_N/25600.

## 4. Alcance

El beneficio real es favorable para W=ARCH_sharp−F y uniforme para todos N≥2^80. La banda contiene la energía exponencial y el error se controla relativamente aC_N; no se vende como error pequeño respecto del residuo W. El complemento anterior y posterior, y su balance conARCH_sharp, siguen abiertos. No se suman colas de otra representación sin contabilidad de truncamientos. No hay nuevo signo totalW, fila completa o ventanaT, ni modificación de papers.

## 5. Adición periódica fina de B — APROBADA

Leída§7 final. Los restos de Stirling y del armónico están demostrados, no asumidos asintóticamente: la serie de atanh da a_n>0 y su mayorante telescópico1/[12n(n+1)]; Wallis da las dos cotas de b_n² y su límite, fijandoC=√(2π). El segundo telescopio tiene D_n−D_(n+1)=−T_n y el resto e_n∈(−1/(12n²),0), con el signo correcto.

La sustitución produce E=F(n,theta)+s_n−xe_n exactamente. En ambos rangos theta≤1/2 ytheta≥1/2 las cotas de log(1+theta/n) dejan−1/(2n)≤F≤0;0<s_n−xe_n<1/(4n). Como x<2n se obtiene−1/x<E<1/(2x), incluido n1. Los saltos de−B1({x})logx coinciden conlogm de B, así E es continuo en enteros; se conserva la convención lateraltheta0.

Q2=theta²/2−theta/2+1/16 es continua periódica, con derivadaB1 casi por todas partes y norma1/16. La integración por partes da exactamenteI+[F_hQ2]_a^b=∫F_h′Q2+∫hE. Por tanto PERIODIC-ERROR y su versión con bordes en módulo son correctas, sin términos de salto adicionales. El límite infinito es legítimo bajo los bordes/integrales indicados y para los kernels de N fijo utilizados.

La adición es una expansión clásica con restos uniformes y un presupuesto explícito de variación; no se registra como principio nuevo de signo. No controla por sí sola el complemento ni W. El beneficio BAND está probado autónomamente con una cota más gruesa. Root coincide independientemente en esta revisión final; la ronda queda completa.
