# Recuperación de la energía completa por dos correctores remotos

**Cotejo.** 012-B evalúa el retorno de una cola a una cabeza de momento inverso nulo. P47 lem:polarelim y rem:polarelim-full explicitan los términos polares. El cotejo con P45, P47, R160 y los correctores de momentos de 211/212 distinguió el alcance de una aproximación test por test. La operación es compensar ambos momentos en extremos opuestos y retener el cruce de los correctores entre sí. La suficiencia global del sector primitivo ya estaba establecida en el corpus.

**Enunciado.** Sea F un test complejo suave compacto en la variable logarítmica t. Escribir A(F)=∫exp(t/2)F(t)dt, B(F)=∫exp(−t/2)F(t)dt, y a para la energía sin polos con todos los contactos visibles en el soporte. Hay tests suaves compactos F_s de momentos A=B=0 tales que ||F_s−F||₂→0 y

    a(F_s) → W(F)=a(F)+2 Re(conjugado(B(F)) A(F)).

Las ventanas de los aproximantes pueden crecer. La convergencia indicada concierne a la distancia L² y a los valores de energía. No se presupone continuidad de la energía completa en L².

**Cálculo de un cruce remoto.** Sean L=Ul y R=Ur dos perfiles suaves compactos en la variable logarítmica, Uf(t)=exp(t/2)f(exp t). Para una distancia s→∞ sólo uno de los dos sentidos del contacto entre L y V_s R puede contribuir. En la energía polarizada, con convención antilineal a la izquierda, el cruce arquimediano es O(1) por Cauchy–Schwarz con peso |m|. Para el peine, al multiplicar el cruce por exp(−s/2) y poner K=exp(s), la expresión que se resta es

    K⁻¹ Σ_n Λ(n) φ(n/K),    φ(v)=∫conjugado(l(x)) r(vx)dx.

En efecto el perfil físico de V_s R es K^(−1/2)r(x/K). La correlación da un factor √n que cancela el denominador del peso. La suma es para un solo sentido en la forma polarizada, con factor dos al tomar el cruce real completo. La función φ es suave con soporte compacto en (0,∞). PNT en forma de cuadratura y Fubini dan ∫φ=conjugado(B(L))A(R). Por tanto

    exp(−s/2) a(L,V_s R) → −conjugado(B(L)) A(R).

**Dos correctores.** Elegir perfiles suaves P,Q con A(P)=−A(F), B(P)=0 y B(Q)=−B(F), A(Q)=0. Existen porque los dos funcionales son independientes sobre los tests suaves compactos (dos traslaciones distintas de un bump positivo dan una matriz de momentos invertible). Tomar

    F_s=F+exp(−s/2)(V_s P+V_(−s) Q).

Las leyes A(V_s P)=exp(s/2)A(P) y B(V_s P)=exp(−s/2)B(P) dan exactamente los dos momentos cero. La distancia L² tiende a cero por la isometría de traslación, y las dos autoenergías añadidas son O(exp(−s)). En orden espacial Q,F,P, las contribuciones mixtas al límite son menos dos veces la parte real de la suma

    conjugado(B(Q)) A(F) + conjugado(B(F)) A(P) + conjugado(B(Q)) A(P).

Para el último término, trasladar conjuntamente por s y aplicar el cálculo anterior con distancia 2s: exp(−s) es precisamente el factor crítico. Al sustituir los momentos de P,Q, la suma equivale a −conjugado(B(F))A(F). Esto prueba la fórmula.

**Consecuencia.** En la unión de ventanas, el ínfimo de W(F)/||F||² sobre los tests suaves compactos no nulos coincide con el de a sobre los tests suaves compactos primitivos con la misma normalización. Una dirección se sigue por inclusión y la otra por la aproximación anterior. Un test con W(F)<0 produciría tests primitivos de energía negativa. El argumento fija cómo se transporta un valor de energía y deja pendiente la desigualdad global que lo firmaría. PROVED tras auditoría matemática independiente.
