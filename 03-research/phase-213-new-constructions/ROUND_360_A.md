# Un único promedio lineal a anchura fija para los productos cribados

Sea w el triángulo en [0,2] de altura uno en 1, convolución aditiva de dos indicatrices de [0,1]. Formar con el corte z congelado

    Q_w(x;z)=Σ_{pm sin primos ≤z} (log p)μ(m) w(log(x/(pm))).

Entonces RH equivale al siguiente enunciado escalar: para cada ε>0, uniformemente en x grande y (log x)²≤z≤4(log x)², se tiene |Q_w(x;z)|≪_ε x^(1/2+ε). Es una sola medición con signo a cada x,z: equivale a integrar Q_{z,1}(u) en du/u desde x/e hasta x. No se requieren anchuras tendientes a cero ni un segundo momento. El enunciado conserva todos los centros reales.

**Recuperar el peso logarítmico sin pedir otra medición.** Escribir S_w=Σ μ(n)w(log(x/n)) y P_w para la suma de primos simples antes de la criba. La transformada de Laplace del triángulo es W(s)=(1−e^(−s))²/s². En el semieje positivo tomar la medida firmada ν=2du−2Σ_{k≥1}δ_k. Como su transformada es −W'(s)/W(s)=2/s−2/(e^s−1), resulta u w(u)=(ν*w)(u) por unicidad. Su variación ponderada por e^(−σu) es finita para σ>0. La identidad μ log=−μ*Λ implica por tanto

    (log x) S_w(x) = −P_w(x) − Σ_{p,k≥2}(log p) S_w(x/p^k)
                      + ∫ S_w(x exp(−u)) dν(u).

En el supremo inclinado A(X)=sup_{1≤t≤X}|S_w(t)|/t^σ, σ=1/2+ε, las dos últimas correcciones cuestan O_ε(A(X)x^σ) para x≤X. Se interpreta S_w(t)=0 para t<1.

**Reconstrucción.** Las identidades Q_z=K_z(P−L_z S) y P=L_z S+U_z Q_z de 359 son de coeficientes y valen con w. Bajo RH, M(t)≪_ε t^(1/2+ε) y sumación parcial dan el mismo techo para S_w. La identidad anterior lo da para P_w con un log adicional; K_z y L_z cuestan x^o(1) en un exponente fijo >1/2 y se empieza con una pérdida menor que la solicitada.

Recíprocamente aplicar P=L_z S+U_z Q_z en x con z=(log x)². En unidades de x^σ, L_z S cuesta O_ε((log x)^(1−2ε)A(x)) para 0<ε<1/4. Hasta d≤√x en U_z vale la hipótesis en x/d con pérdida ε/2, por la inclusión en el corredor; la suma cuesta O(x^(−ε/2+o(1))). Para d>√x, usar en el hijo la primera identidad y el techo previo para P_w que proviene de la envolvente A(x); resulta un coste normalizado por el hijo de A(x)x^o(1). La cola del padre es O(x^(−ε/4+o(1))) por el producto de Euler de 359. Los hijos en escalas acotadas satisfacen límites triviales. Así P_w(x)/x^σ cuesta O(1)+o(log x)A(x). Dividir la identidad logarítmica por log x y tomar el supremo, absorbiendo como en 359, da A(X)≪_ε1. La transformada de Mellin de S_w converge entonces en Re s>1/2 y prolonga W(s)/ζ(s); allí W no se anula. Esto demuestra la implicación inversa.

**Alcance.** El uso de anchura fija sin criba ya figura en el tramo inverso de 353. Aquí la medida ν permite cerrar la absorción con la misma única medición lineal después de cribar el producto completo. Falta estimar esta suma firmada a escala de raíz; las medias de sectores de 354 no tienen esa precisión.
