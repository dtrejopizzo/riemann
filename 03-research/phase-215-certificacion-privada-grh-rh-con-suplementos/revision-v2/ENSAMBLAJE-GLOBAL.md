# Ensamblaje global: obligaciones y deducción V2

Fuentes: main.tex de46 en fuentes-v2.json; relectura directa de an:lem-R, an:lem-landau, an:prop-density, an:thm-criterion, au:twistprime, au:Zj, srcC y an:thm-main hasta an:cor-GRH. Esta ficha certifica la implicación indicada, no adelanta la descarga de sus premisas.

## Núcleo lógico suficiente

La conclusión requiere SF, Sp y Cv para los datos producidos por an:thm-data. No requiere los cálculos de ventanas, las comparaciones finitas declaradas sin prueba, las filas43–45 ni una afirmación de novedad. Tampoco basta comprobar únicamente las copias de enunciados en apéndices.

SF recibe seesaw, divisibilidad y kernel de49/50. Sp recibe segundo momento51/52 y las reducciones de46. Cv recibe inj, aux, factor, regular, onelift, hecke y mult de53–56/51. Las dependencias compartidas deben cerrarse una sola vez con sus hipótesis completas. La fase49, exchange53 y el nivel/Higman55 se revisan en los ledgers V2, sin asumir sus conclusiones a partir de este ensamblaje.

## Producto y alturas

En au:twistprime el mismo twist theta_iota sirve a los cambios de base en iota y conjugate(iota): la definición del índice exige una matriz que sirva para todos los twists permitidos en ese primo. El determinante mixto queda integral y cuesta 2 delta. No se supone que un automorfismo complejo conmute con conjugación: sigma'=c sigma c proporciona las dos Gram necesarias; Cauchy–Schwarz exterior seguido de Fischer da la cota archimediana. El multiplicador del principio de alturas es algebraico, pues sus imágenes bajo todos los isomorfismos a Qbar_2 tienen valoración acotada; un trascendente podría enviarse a elementos de valoración arbitraria. El producto de normas racionales da la desigualdad de altura. Esta parte es una prueba, no un postulado de positividad de los lifts.

## Cv desde sus entradas

au:onelift y mult dan Z_j(1)/Z_j(theta^j)=(Delta_j(theta^j)/Delta_j(1))(H_j(1)/H_j(theta^j))^d. Los presupuestos suman d(3A+r bud+10mx1+6k bud-k hdir). Con r<=2k y k bud log b=fa(log b)^4/m basta 3fm²b(log b)²+10m²x1<=fa(log b)³(log b-8), por m²<=4x y a=xb y los tamaños admisibles.

Completar n vectores con n'<=4d/b² auxiliares permite aplicar au:twistprime. Los ratios ramificados cuestan a lo sumo b y el coste archimediano auxiliar es2x1²b². Entonces

0 <= c+2delta+n'(2x1²b²+b)+d(b+fa(log b)^4-hmain).

El término n' es <=db por los tamaños, y2b<=2fa(log b)^4. Resulta Cv exactamente. Cada una de sus entradas todavía debe tener una prueba válida en su instancia; esta aritmética no las reemplaza.

## SF + Sp + Cv

Poner L=fa(log b)^4, E=fa(log b)^3 y d=dim T>0. Sp proporciona una familia de traducciones con coste <=5d log(1+2b²). SF permite elegir una base de su imagen de dimensión n entre(1-4/b²)d y d, con covolumen<=n(hmain-m rem+L) e índice<=10d log(1+2b²)E. Cv implica

n m rem <= d[4L+20log(1+2b²)E],

usando hmain>=0 para n hmain<=d hmain. Si rem<=0 la conclusión es inmediata; en otro caso d<=2n y log(1+2b²)<=3log b. Por log b>=128 se obtiene m rem<=fa(log b)^5. Se conserva el signo de rem; no se divide por una cantidad cuyo signo sea desconocido.

## Del resto a GRH

La identidad exacta an:lem-rem y #Pa/#Pb<=log b dan

R_d,q0(x)<=phi(q0)(log b)^6/m+|R_d,q0(x1)|+log b |R_d,1(x1)|.

Para q0,d fijos, PNT sólo se aplica en x1; sus constantes pueden depender de ellos. Con m>=sqrt(x), log b<=2x^delta y log x1>=x^(delta/6)-1, los dos restos son O(x^-2). Se obtiene R(y)<=y^(-1/2+epsilon), pasando de enteros a reales con coste O(1/x).

La gran criba cuadrática permite escoger d en la clase requerida cuyos twists no tienen ceros en una caja fija que contiene el cero candidato rho y el segmento real pertinente. La demostración de densidad conserva el ahorro theta²/8: el error de truncación ahorra theta(2-theta)/4; la suma sobre productos cuadrados ahorra theta²/4 antes de los epsilon. No se requiere GRH para esta selección.

La transformada de R tiene residuo (n_q(rho)-n_q^K(rho))/(phi(q)rho(1-rho)). La cota unilateral y Landau implican holomorfía en Re(s)>beta salvo un posible polo real de residuo negativo. La selección de d elimina los ceros de twists en el segmento, por lo que los residuos reales son no negativos y esa alternativa es imposible. En rho tampoco hay cancelación por twists: n_q(rho)=0. Con q0=18480q se cubre todo carácter; los factores Euler añadidos sólo tienen ceros en Re(s)=0. La ecuación funcional del carácter primitivo da el otro semiplano.

**Dictamen de este segmento: (a), implicación comprobada de SF/Sp/Cv para los datos construidos a GRH de Dirichlet y RH.** Las condiciones pendientes de SF/Sp/Cv se resuelven en las fichas de especialidad, no se eliminan por llamar certificación a la conclusión.
