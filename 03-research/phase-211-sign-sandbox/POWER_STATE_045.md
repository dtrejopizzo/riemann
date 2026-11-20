# Estado 045 — Frontera documental corregida y prueba de un certificado heredado

El signo global permanece OPEN. La ronda no añade una ventana ni una región de positividad de potencias. Papers intactos.

## Corrección importante del estado

No debe confundirse el rango incluido en Paper47 con todo lo certificado previamente en el sandbox. Paper47 contiene la prueba hasta T=log(5)/2. ROUND_026_A, Theorem26A.2, registra una certificación asistida por computadora de lambda_A(T)>=2e-26 para TODOS los tests primitivos normalizados y TODOS 0<T<=207/200=1.035. Esta última sí supera log(5)/2, pero es un resultado anterior, no un avance de las rondas recientes de potencias.

Root y mapa leyeron los logs archivados de ambas paridades a T=1.035, mu=2e-26; ambos registran certified:true. No se reprodujo ahora el cálculo grande. POWER_PRIMAL_AUDIT_045 precisa fuentes, los resúmenes JSON sobrescritos por otros intentos y la distinción entre build y certificado. Para T=1.098 se localizaron matrices y builds, pero no un certificado final: no se promueve ese extremo a resultado probado.

## Qué falla al reutilizar el certificado de Paper47

POWER_CONTACT_FLOOR_045 prueba, con revisión independiente y verificador racional reproducido por root, que al entrar el contacto 5 el piso crudo m(240)-A_T es menor que -1/2. Por ello no sirve mantener simultáneamente el corte240 y ese piso de masa total para obtener un lower no negativo mediante lowercert. No es negatividad de la forma ni imposibilidad de otros certificados. ROUND_026_A ya evita esa restricción usando cotas del símbolo real y otro corte.

La nota escribe también los cruces lineales y cuadráticos y el borde polar que una propuesta basada en ese certificado debe conservar. Son fórmulas del método existente, no una nueva desigualdad de signo.

## Trabajo en la representación L55-B

La construcción de un par positivo explícito sigue OPEN. La auditoría exige igualdad en todo el portador primitivo y coincidencia aritmética en la banda o discrepancia controlada; positividad de medidas aisladas no basta. El intento de imponer masa espectral total finita se retiró por ser una restricción artificial, ajena al candidato general.

POWER_PRIMAL_PAIR_045 estudia el ansatz más preciso de fijar la cola real y reparar sólo un compacto espectral. Para medidas PARES, la identidad en todos los tests primitivos fuerza que esa corrección compacta sea cero: aplicar F=(D²-1/4)phi, polarizar y localizar anula el núcleo en un intervalo; la compacidad anula entonces todos sus momentos. A T=3/5, el símbolo en cero es menor que -15/2. Por ello este ansatz no produce un representante positivo con slack <=15/2, aunque la forma en esa ventana ya es positiva. Root revisó la prueba y reprodujo el verificador de constantes; la auditoría independiente se consigna en POWER_PRIMAL_AUDIT_045.

La paridad es esencial: sin ella sólo se determina la parte par de la corrección. Tampoco se excluyen correcciones no compactas. En el subcaso de una corrección dada por una función continua templada y un resto temporal exterior que es medida finita firmada, el intento vuelve exactamente al dual(D) existente. No se afirma esa identificación para toda medida singular o distribución exterior. No se construyó un nuevo par positivo ni se cerró L55-B.
