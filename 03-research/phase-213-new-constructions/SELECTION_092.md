# Límite de la lectura prima del cosh

El peine cruzado exacto a=1/2 ya está en fase 212-57 C1, con peso (1+1/n)log(x/n). Por tanto calcular otra vez los elementos de la matriz polar no abre una vía.

Una consecuencia para calibrar posibles desigualdades: sea S(x)=Σ_{p≤x}(log p)log(x/p). Entonces el signo global equivale a S(x)≤x para todo x suficientemente grande. En efecto, para x=exp(2T) la fórmula explícita clásica integrada de ψ da

    [x−S(x)]/√x = 2 + J(T) + o(1),

con J de 088 a=1/2. Detalles: integrar ψ(t)/t entre 1 y x (desde 2 para los términos individuales de la fórmula explícita). Los residuos no triviales integrados son −Σ(x^ρ−2^ρ)/ρ²; se obtiene también directamente por Perron con multiplicador 1/s². El polo en 1 aporta x, el origen O(log x), y los ceros triviales O(1) para x≥2. Las potencias cuadradas omitidas pesan 2∫₁^{√x}θ(t)dt/t=(2+o(1))√x por PNT. Las de orden ≥3 cuestan O(x^(1/3)log³x) por conteo trivial.

Bajo RH, |J|≤Σ|ρ|⁻²=Σ1/[ρ(1−ρ)]=2+γ_E−log(4π)<0.047 por la identidad clásica de Hadamard. Luego S(x) queda por debajo de x con margen al menos (1.953−o(1))√x. A la inversa S(x)≤x da J(T)≥−O(1), lo que excluye cualquier polo con Re z>0 por el argumento unilateral de 088. Este criterio pone de manifiesto el sesgo de las potencias cuadradas. La cota S(x)≤x queda abierta; integraciones de Chebyshev y la detección por polos son antecedentes, y no se reivindica prioridad para este corolario.
