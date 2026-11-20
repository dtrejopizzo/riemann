# Una banda prima alrededor de la raíz cúbica

Para cada δ>0 fijo basta controlar una familia de integrales centradas con v exclusivamente en [c X^(1/3), X^(1/3+δ)]. El corte inferior tiene cancelación exacta del núcleo factorial. Se cambia el promedio discreto de 127 por promedios continuos que en conjunto detectan cualquier polo. El término aritmético interno aún contiene coeficientes de Möbius hasta 4X^(2/3).

**Promedios.** Tomar un entero r con (1+2r)δ>1/2 y para n entero positivo usar w_n(t)=(sin⁴ t/t³) sinc(t/n)^(2r), sinc(u)=sin(u)/u, sobre t>0. Es positivo salvo ceros aislados. Su extensión impar a la recta es entera, L¹ y de tipo angular B_n=4+2r/n; por Paley–Wiener tiene Fourier soportada en [−B_n,B_n]. Por la serie de senos de la función periódica {u}−1/2, usando sumación de Abel y convergencia dominada, ∫₀∞ w_n(t)({yt}−1/2)dt=0 para 2πy>B_n. Los valores en los saltos son irrelevantes.

Los momentos G_n(s)=∫w_n(t)t^s dt convergen, al hacer n→∞, para cada 0<Re s<2 al correspondiente momento de sin⁴t/t³. Con α=2−s, éste vale [4·2^α−4^α]π/[16Γ(1+α)sin(πα/2)] por la integral de (1−cos t)t^(−1−α). No se anula en esa franja. En consecuencia cada cero relevante sobrevive para algún n fijo, sin exigir que un n determinado los conserve todos.

**Coste factorial.** Poner D=floor(X^(2/3)) y usar los dos correctores de 130. Escribir K(v)=Σ c_d ∫w_n(t)floor(Xt/(dv))dt, W(v)=∫_{v/X}∞ w_n(t)dt, con dE=dψ−b(v)dv de 129. Para Y=X/d grande se cumple

    ∫ w_n(t) [∫floor(Yt/v)dE(v)]dt = O_n,r(1/Y).

En t≥3/Y usar la expansión calibrada de 129 (aumentar 3 por una constante si hace falta); ∫w_n(t)/t dt es finita. El intervalo pequeño cuesta O(Y⁻²) al acotar la discrepancia factorial original para Yt acotado, pues w_n(t)=O(t). Extender el término de diente de sierra con log(Yt) a ese intervalo cuesta también O(Y⁻²) por cambio u=Yt. La parte con log Y desaparece exactamente por el soporte Fourier. Para la parte con log t integrar por partes contra la primitiva acotada, de tamaño O(1/Y), del diente periódico. La derivada de w_n(t)log t está en L¹, y los bordes se anulan. Así ∫K dE=O(D² log(2D)/X)=o(√X) por la cota ℓ¹ de 130.

**Ambos extremos.** Para v≤cX^(1/3) elegir c>0 tan pequeño que 2πX/(4Dv)>B_n (puede elegirse uniforme en n). La media del suelo es exactamente X/(dv) por el momento ∫tw_n menos (1/2)∫w_n, es decir, una función afín de 1/d. Ambas sumas de coeficientes se anulan, luego K(v)=0. W es acotado y su coste absoluto hasta ese corte es O(X^(1/3)) por Chebyshev. Por encima de X^(1/3+δ), la inversión da W_t=K_t para t≤X^δ/2 y X grande, pues Xt/v<D. Para t>X^δ/2 el coste absoluto sobre todo v de W_t más los suelos con los valores absolutos de los coeficientes es O(Xt log(2+Xt)log(2D)): usar Chebyshev, la identidad factorial y ∫_a∞floor(y/v)dv≪y log(2+y), con Σ|c_d|/d≪log(2D). Integrando w_n(t)≪_{n,r}t^(−3−2r) se obtiene o(√X) por la elección de r. Por Fubini resulta

    ∫ w_n(t)[ψ(Xt)−Xt]dt = ∫_{cX^(1/3)<v≤X^(1/3+δ)} (W−K)dE + o(√X).

El cambio de b a la densidad uno en el término W cuesta O(1).

**Criterio pendiente.** Para cada n bastaría que el lado aritmético derecho estuviera acotado superiormente por O_{n,ε}(X^(1/2+ε)) para todo ε>0. Bajo RH esto se cumple por el PNT con error raíz-log². Recíprocamente aplicar Landau como en 127: truncar ψ(x)−x a x≥1 antes de promediar cuesta O(X⁻²) en X grande; en 1<Re s<2 la Mellin bilateral en X del promedio truncado es G_n(s) veces la Mellin de esa discrepancia. El tramo X<1 del promedio es O_n(X²) por el decaimiento de w_n y Chebyshev, de modo que al retirar dicho tramo se resta una función holomorfa en Re s<2. Todo polo a la derecha de 1/2 sobrevive en algún n, y la transformada es regular en el eje real positivo de la franja. La cota unilateral excluye tal polo. No se ha probado ese techo.

**Cotejo.** R155_005/006 ya emplean sinc⁴ y B-splines; 045 y 047 usan Poisson en cuadraturas. La aplicación adicional es una identidad afín exacta para la media de cada suelo en todo un intervalo, junto con la transferencia Mellin y el corte superior para los mismos promedios. El peso difiere de 127 y el criterio de este memo usa tolerancia.
