# Masa negativa mínima de un certificado truncado del paper 47

Fijar una ventana T>0 y una lista Z finita, simétrica y no vacía de ordenadas reales, con sus multiplicidades. En la notación de finDet y finZ del paper 47 sea g_Z(u)=Σ_{γ∈Z}cos(γu). Para un perfil par real suave, igual a uno en [−2T,2T] y soportado en [−L,L], sea ν la medida con transformada w g_Z, normalizada por ν(ℝ)=|Z|. Su masa negativa es ν⁻(ℝ). Para L suficientemente grande,

    c(Z,T)/L² ≤ inf_w ν⁻(ℝ) ≤ C(Z,T)/L².

El lado inferior vale incluso para toda medida real finita cuya transformada coincida con g_Z en la ventana y se anule para |u|>L. En particular no depende de que la extensión sea un producto.

**Inferior.** Usar el paso a de finDet tal que ra<2T y los r nodos distintos z_j=exp(iγ_j a) estén separados. Sea P(z)=∏(z−z_j). Por los momentos en la ventana, ∫|P(exp(iaτ))|²dν(τ)=0: para la medida discreta de Z la integral vale cero y sólo se usan los momentos |k|≤r. Por tanto ∫|P|²dν⁺=∫|P|²dν⁻≤||P||∞² ν⁻(ℝ).

Tomar n=floor(L/a)+1 y Q_n(z)=∏(z^n−z_j^n). En la circunferencia |Q_n(z)|≤C_Z n|P(z)|, con constante dependiente de los nodos pero no de n. En efecto, escoger el nodo más cercano, usar |z^n−z_j^n|≤n|z−z_j| en ese factor y acotar los restantes por 2. El cociente |P(z)|/min_j|z−z_j| tiene ínfimo positivo por separación y compacidad, extendiendo por continuidad en las raíces. Todos los términos no constantes de |Q_n|² tienen frecuencias múltiplos no nulos de n. Por na>L sus integrales se anulan. El término constante es la suma de los cuadrados de los coeficientes del polinomio en z^n, al menos uno por monicidad. Luego
    |Z| ≤ ∫|Q_n|²dν ≤ ∫|Q_n|²dν⁺ ≤ C_Z² n² ||P||∞² ν⁻(ℝ).
Esto da la cota para cada extensión admisible.

**Superior constructivo.** Tomar b la autocorrelación normalizada de un bump real suave soportado en [−1/2,1/2], de modo que b(0)=1, b'(0)=0, supp b⊂[−1,1] y su densidad de Fourier sea no negativa. Elegir χ par suave de soporte compacto fijo e igual a uno en la ventana. Usar
    w(u)=b(u/L)+χ(u)(1−b(u/L)).
Para L mayor que el radio de soporte de χ, w cumple todas las condiciones. El primer término multiplicado por g_Z tiene densidad no negativa. En el soporte fijo, la corrección e_L=χ(1−b(·/L)) y sus primeras dos derivadas son O_T(L^(−2)) por Taylor y paridad. Por la cota L¹ directa en bajas frecuencias y dos integraciones por partes en altas, la norma L¹ de su densidad de Fourier es O_T(L^(−2)). Multiplicar por g_Z sólo suma traslaciones, con costo ≤|Z|. Esto acota la masa negativa de la medida total.

**Cotejo y alcance.** El antecedente principal es finDet/finZ en el paper 47 y su desarrollo en R155_040/041/043; la sonda G2_B6 ya mostró que una lista finita no certifica el signo. La cota inferior usa el mismo polinomio anulador y añade una comparación con Q_n en la escala donde la transformada ha desaparecido. La superior construye perfiles de orden coincidente. La constante inferior depende de la separación de todos los nodos y no es uniforme al añadir ceros. Se obtiene una tasa para el obstáculo finito; sigue sin justificarse el signo de la cola del espectro real ni de la forma completa.
