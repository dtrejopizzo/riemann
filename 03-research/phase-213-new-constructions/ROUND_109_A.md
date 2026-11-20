# Una desigualdad local que sólo hay que probar en centros primos

Poner h=11/25, r=exp(h), C=cosh(h/2). Sea w(t)=t^(−1/2)sinh((h−|log t|)/2) en |log t|≤h y cero fuera. Con V(s)=∫w(t)t^(s−1)dt, el signo global equivale a la siguiente desigualdad para cada primo q suficientemente grande:

    Σ_{q/r≤p≤rq} log p w(p/q) ≤ q V(1).

La banda tiene razón exp(0.88) como en 107. En este criterio tanto el centro como las muestras de la suma son primos. La recuperación de los centros reales es exacta, sin estimaciones de huecos ni tolerancia de interpolación.

**Entre centros primos.** Como función de x, w(p/x) es cero hasta p/r, luego (√r x/p−1/√r)/2 hasta p, luego (√r−x/(p√r))/2 hasta rp, y después cero. Tiene saltos ascendentes de pendiente en los dos extremos y descendente sólo en p. Así E(x)=Σ log p w(p/x)−xV(1) es convexa entre cada par de primos sucesivos. Si E≤0 en ambos extremos, E≤0 en todo el intervalo. En particular un exceso sólo puede ocurrir si al menos uno de los centros primos adyacentes tiene exceso. La verificación continua y la discreta son equivalentes para cualquier cola que comience en un primo.

**Equivalencia continua.** Para z=s−1/2, integrar las dos exponenciales (o usar los tres saltos) da V(s)=[cosh(hz)−C]/(z²−1/4), con singularidades removibles; V(1/2)=4(C−1). Sus posibles ceros tienen Re z=±1/2, de modo que no anula ningún polo de P en 1/2<Re s<1. Landau da la vuelta como en 106–107. Bajo RH, por la misma fórmula explícita ponderada de 107 (peso continuo y segunda derivada logarítmica de variación finita en sentido de medida), E(x)/√x=−V(1/2)/2−Σρ x^(iγ)V(ρ)+o(1). Aquí V(ρ)=(C−cos(hγ))/(γ²+1/4)>0. El certificado que sigue acota Σ V(ρ)/V(1/2) por 0.487, por lo que el techo vale bajo RH con margen eventual ≥0.013 V(1/2)√x.

**Certificado.** Usar Σ1/(γ²+1/4)=D<0.0462 bajo RH y restar sólo las primeras cien parejas del sumando no negativo 1+cos(hγ). Código para python-flint:

    from flint import arb, acb
    h = arb(11)/25
    C = (h/2).cosh()
    gs = [acb.zeta_zero(i).imag for i in range(1,101)]
    bound = ((C+1)*arb('0.0462') -
             sum(2*(1+(h*g).cos())/(g*g+arb(1)/4) for g in gs))/(4*(C-1))
    assert bound < arb('0.487')

**Cotejo.** 044 usa interpolación homogénea en centros prescritos; 094 localiza máximos en cruces de θ y huecos. Aquí la propia suma local es convexa entre primos, aun al atravesar los extremos móviles de otras contribuciones. Esto selecciona directamente los centros q primos sin condición de cruce. Falta demostrar la cota de la suma sobre vecinos de cada q.
