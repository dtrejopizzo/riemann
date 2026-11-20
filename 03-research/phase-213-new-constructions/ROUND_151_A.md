# Qué parte de la corrección impar escapa a la altura verificada

Usamos el mismo ε y la misma densidad de 150, sin recalibrarlos para un intervalo finito. Sea E(T)=∫yp(y)U(T+y)dy. Para T≥0 vale incondicionalmente

    E(T) = Σ mρ B(ρ) exp((ρ−1/2)T) + b exp(−T/2) + O(exp(−T)),
    b = (ξ'/ξ)(0)/(2ξ(1/2)).

Aquí la suma recorre ceros distintos de ξ. La parte par de F vale a+O(exp(−T/2)). En particular, si H≥2 es una altura hasta la que se conoce RH, entonces

    F(T) ≤ 3a/4 + C exp(−T/2)
                  + C (1+H)^A exp(T/2−πH/4)

con constantes absolutas independientes de T,H y a<0. Se puede usar H=3·10¹² por Z2 del paper 47. No damos un intervalo numérico certificado: las constantes del resto no se han evaluado.

**Prueba.** La transformada de E es B(z)ξ'(z)/ξ(z) en las convenciones de 150. Desplazar hasta Re z=−1/2. Todos los ceros quedan a la derecha de esa recta independientemente de RH. La expansión local de la derivada logarítmica y Stirling dan crecimiento a lo sumo polinómico del factor sin gamma sobre la recta y sobre una sucesión de horizontales que evitan las ordenadas por ≫1/log(|t|+2). El decaimiento gamma permite pasar al límite para cada T fijo. El aparente polo en z=1/2 desaparece por ξ'(1/2)=0. El polo simple de Γ(z/2) en cero tiene residuo 2 y ζ(0)=−1/2, dando b. En la misma tira B(z)cosh(z−1/2) sólo aporta el residuo a en 1/2 y un término O(exp(−T/2)) en cero. Las integrales restantes son O(exp(−T)). En todo 0≤Re z≤1 y para |Im z|≥2, Stirling y el crecimiento polinómico de ζ en tiras fijas dan |B(z)|≤C(1+|Im z|)^A exp(−π|Im z|/4). El conteo por bandas unitarias absorbe un factor logarítmico aumentando A. La serie converge absolutamente para T fijo. Su cola después de H tiene la cota anunciada usando Re ρ≤1. La parte hasta H, multiplicada por ε, cuesta a lo sumo |a|/4 por la elección de 150. Esto prueba la desigualdad.

**Alcance.** Para T≤(π/2−δ)H con δ>0 fijo, la contribución desconocida está acotada por C(1+H)^A exp(−δH/2). El parámetro T de esta cuenta es el logaritmo de la escala de Liouville, distinto del soporte de las pruebas del paper 47. La estimación por altura fija pierde fuerza cuando T crece sin límite. La fórmula localiza exactamente ese fallo aun para ceros múltiples y no proporciona cota global.
