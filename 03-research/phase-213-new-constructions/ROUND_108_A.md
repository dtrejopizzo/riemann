# Restricción conjunta de los armónicos del primer cero sobre el techo primo

Con E,V,L,m,γ de 106 se tiene incondicionalmente

    limsup E(x)/√x ≥ 2 cos(π/34) m |V(1/2+iγ)| − V(1/2)/2.

En particular todo peso continuo no negativo no nulo con razón de extremos ≤1.20484 produce excesos positivos de orden raíz en una sucesión. En 106 la obstrucción universal sólo alcanzaba razón aproximadamente 1.160.

**Prueba.** Suponer E(x)≤c√x en una cola y poner g(u)=c−exp(−u/2)E(exp u) en esa cola u≥U. Como en 106 su transformada de Laplace converge para Re s>0 por Landau. Para δ>0 tomar la matriz Gram de las funciones exp(ijγu), 0≤j≤32, con medida positiva δexp(−δu)g(u)du sobre la cola. Cuando δ baja a cero, cada entrada converge al residuo de la transformada en la frecuencia correspondiente. En la diagonal queda c+V(1/2)/2; en las diagonales primeras quedan m V(ρ) y su conjugado. Las restantes son cero: los puntos 1/2+ikγ con 2≤k≤32 no son ceros por el certificado inferior, y ζ(1+2ikγ) tampoco se anula. El límite es semidefinido positivo. Por cambio diagonal unitario se retira la fase de su primera diagonal. Los vectores de componentes sin(jlπ/34), 1≤j≤33, diagonalizan la matriz real tridiagonal; el menor autovalor es c+V(1/2)/2−2m|V(ρ)|cos(π/34). Pasar al limsup como en 106.

Por la proyección de fases de 106, basta L<2 arccos(1/(4 cos(π/34)))/γ para forzar exceso. Certificado reproducible con aritmética de bolas:

    from flint import acb, arb, ctx
    ctx.prec = 100
    g = acb.zeta_zero(1).imag
    values = [abs(acb(arb(1)/2,k*g).zeta()) for k in range(2,33)]
    assert all(v > arb('0.1589') for v in values)
    threshold = (2*(1/(4*(arb.pi()/34).cos())).acos()/g).exp()
    assert threshold > arb('1.20484')

El menor módulo certificado supera 0.1589174. No se presupone independencia racional ni RH. Los 31 puntos certificados son múltiplos de la primera ordenada, no una lista de ceros adicionales. El test ensancha el rango descartado; no aporta el signo para la banda admisible de 107.
