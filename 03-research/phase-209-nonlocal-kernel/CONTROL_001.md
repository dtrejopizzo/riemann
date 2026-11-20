# CONTROL_001 — No localidad aparente por compresión

2026-10-18. PROVED, observación elemental; no mecanismo nuevo ni ruta de cierre.

Use Fourier unitaria y dt en frecuencia. Sea P_T la proyección cuya imagen
H_T es la transformada de L²([-T,T]). Su núcleo es

    s_T(t-u)=sin(T(t-u))/(π(t-u)).

Para a real acotada, A=P_T M_a P_T tiene núcleo débil

    K_a(t,t′)=∫ s_T(t-u)a(u)s_T(u-t′) du.

El integral converge por Cauchy–Schwarz. Aunque K_a generalmente depende de
ambas variables, para f,g∈H_T:

    ⟨f,Ag⟩=⟨f,M_a g⟩.

Prueba: P_T es autoadjunta y P_T f=f, P_T g=g. Por tanto escribir K_a no
introduce nueva relación de signo en el dominio efectivo. Con restricción
polar V_T⊂H_T se mantiene la identidad para f,g∈V_T.

La misma cuenta vale para símbolos no acotados cuando la forma multiplicadora
está definida y la compresión se interpreta como restricción de forma; no se
está afirmando una fórmula de integral absolutamente convergente en ese caso.

**Prueba de novedad exigida para O1:** no basta exhibir K(t,t′) ni una
conmutación no nula en L² ambiente. Hay que mostrar que, restringida al dominio
relevante, la forma no es sólo el multiplicador anterior tras compresión.
Esto no excluye todos los operadores no locales ni prueba que la clase O1
esté vacía. Evita confundir la forma del núcleo con un mecanismo adicional.

También conviene separar variables: Toeplitz/Hankel en índices de la base de
Dirichlet, kernel en coordenada x y kernel en altura de Mellin t son tres
representaciones diferentes; traducirlas antes de atribuir una obstrucción.
