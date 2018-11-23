## De la politica ficción a la política acción

- No somos expertos.
	- No es una clase magistral sino una exposición de lo aprendido
	- 15M como punto de aprendizaje: economia, politica, organizacion, informatica, derecho
	- Cada uno vuelca lo que sabe y lo contrasta con lo que sabe el otro
- Que os voy a explicar?
	- No como mejorar el sistema electoral -> Como funciona para usarlo o no
	- Yo tengo mis opciones, ojo conmigo
		- Anarquista pero no abstencionista
		- Voto a izquierdas: normalmente ICV
		- Hago campaña por Eb, Pirates, Anticapitalistas, Equo
	- No os voy a decir que hacer el 20N -> Explicar opciones y sus consecuencias
		- Hasta donde se puede llegar con cada opcion?
		- Que masa critica se necesita?
		- Que efectos laterales tiene?
	- A menudo escuchamos historias sobre esto.
	- No siempre estan fundamentadas
	- Muchas veces nos creemos unas o otras
		- segun lo que queremos creer
		- segun las veces que nos lo repiten.
	- Ejemplos:
		- El voto util
		- El voto en blanco que se quedan los mayoritarios
		- El voto en blanco que hacia daño a los minoritarios
		- El voto nulo que no lo hacia
		- El voto a las fuerzas sin representacion que hacia daño a las minoritarias con representación
		- La abstención favoreciendo a las mayorias
		- La ley de Hondt favoreciendo las mayorias
- En Sant Joan, queriamos hacer algo
	- Decidimos no apoyar una opcion concreta, sino informar
	- Pusimos en comun lo que pensabamos que sabiamos
		- Muchas cosas contradictorias
		- Ninguna estaba fundamentada
	- Decidimos:
		- Buscar fuentes primarias sobre la ley
		- Simular los efectos de cada opcion
			- Para ello construimos el simulador
	- Os voy a explicar los resultados de este proceso

- Que opciones de voto consideramos?
	- Voto a candidatura
		- Mayoritarias
			- PP, PSOE, CiU
		- Minoritarias con representación
			- UI/ICV, ERC, UPyD
		- Extraparlamentarias
			- Anticapitalistes (Moviments antiglobalització)
			- PACMA (Animalistas)
			- UCE (Comunistes, Maoistes, Espanyolistes) venen a ser pel PSUC el que era UPyD y C's pel PSC/PSOE
			- PxC (Xenofobs, Extrema dreta) concentra el vot d'extrema dreta (AN, Falanges, E2000...)
		- De castigo o contra sistema:
			- Escons en Blanc: No cogen el escaño ni lo cobran. Consiguieron regidores.
			- Pirata: Democrácia líquida. Derechos humanos, Ideario Pirata, Voto por internet.
			- Hartos (Al final no se presentan): Agrega minoritarios que no han conseguido firmas. (agregados tampoco pudieron)
			- Pato (Al final no se presentan): Ridiculizar la politica. Carmen de Mairena y otros personajes.
	- Voto nulo
		- Cualquier cosa que no sean papeletas a un partido politico
		- Hay gente que hace modelos de papeletas
		- Se dice que la mesa esta obligada a leer lo que hay puesto (no lo hemos podido comprobar en la ley)
		- También se dice que 
	- Voto blanco
		- Sobre vacio. A diferencia del nulo no cuenta para el umbral.
		- A veces afecta, en las generales, en barcelona podria, pero veremos que no.
		- Hay webs que proporcionan modelos de voto nulo
	- Abstención
		- Pasiva: Es la que se hace por vagancia, desidia, desapego, desesperanza...
		- Activa: Quien no quiere legitimar el sistema con su participación y plantea alternativas.
		- No hay forma de diferenciarlas
		- Casi siempre es mayor que el partido mayoritario. Es la opcion mayoritaria.

- Como se agrupan las opciones
	Censo = Abstencion + Participacion
	Participacion = Nulos + Validos
	Validos = Blancos + Candidaturas

- Sistema electoral actual
	- El sistema electoral espanyol funciona per circunscripcions
		- Els vots d'una provincia serveixen nomes per escollir el numero diputats que te assignada aquesta provincia
		- Es fatal per la representativitat perque es perden vots
		- Ens va de conya per analitzar-ho a petita escala a Barcelona
	- El Senat
		- Solo se escoge una parte de los senadores
			- La otra parte la escogen los parlamentos autonomicos
		- Los votos son a la persona y no al partido
		- Cada votante da de 0 a 3 votos
		- De Barcelona salen 4 senadores, los cuatro que tengan mas votos
		- Entonces, según esto...
			- Si voto solo a uno, van los tres votos a el?
				- No, los otros 2 votos los tiras.
			- Si voto solo a uno de los tres de un partido, y le sobran votos, caen en los otros candidatos?
				- No, el voto es a la persona, no al partido.
			- Es bueno repartir el voto en varias formaciones?
				- Depende de lo que pretendas, si otros votantes han hecho lo mismo escogiendo candidatos diferentes de cada lista, no sumaran.
			- Preguntas? Chao senado.
	- El Congres
		- S'escullen 31 de 350
		- Umbral per entrar al recompte: 30% a les generals (canvia a d'altres convocatories, no a Barcelona)
		- Recompte per llei d'Hondt
			- Obtenció dels cocients: dividir els vots de cadascu per 1, 2..
			- Els 31 cocients majors obtenen l'esco
			- Es un algoritme per obtindre-ho pero no il·lustra l'objectiu:
				- Es cerca un preu d'esco mínim
				- Que es reparteixen tots els escons i a ningú li sobra per

- El simulador
	- Esta pensado para simular una sola circunscripción por cada caso
		- Lo que pasa en cada circunscripción es independiente
	- Carga casos reales o hipotéticos
		- Viene con todas las generales y autonómicas en la provincia de Barcelona
		- Viene con algunos casos hipotéticos con candidaturas y censos reales de estas elecciones
		- Viene con diferentes opciones acordes con las ultimas estadisticas del CIS (bastante poco explicitas)
	- Se puede experimentar situaciones alternativas haciendo transferencias de votos entre opciones (incluyendo nulo, abstencion y blanco)
		- Para transferir, basta con:
			- clickar en las tartas con el botón izquierdo el origen
			- clickar en las tartas con el derecho el destino
			- seleccionar el numero de votos
			- clickar en 'Transferir'
	- Las tartas de arriba representan:
		- Las opciones de la totalidad del censo, incluyendo abstencion, nulo y blanco
		- La proporcion de votos a candidaturas
		- El reparto segun la ley electoral actual
		- Un reparto mas proporcional (Metodo Hamilton)
	- La tabla inferior ilustra lo que esta pasando según la ley electoral
		- Las candidaturas que no superan el umbral aparecen en gris
		- Los cocientes que obtienen escaño aparecen con fondo oscuro
		- Los cocientes que estan a punto de pasar a un lado o a otro aparecen en rojo o naranja.
	- En medio hay controles para editar el caso y estadisticas varias


- Rumors i certeses
	- En generales y en Barcelona, el umbral del 3% de los votos válidos no afecta casi nunca porque no hay demasiados escaños (31)
		- El reparto por ley de Hondt se suele quedar por arriba de ese umbral
		- Sí que afecta en las autonómicas porque:
			- reparten mas escaños por provincia (85 en Barcelona)
			- y ademas, en algunas provincias el umbral está más alto (p.e. 5% en valencia)
		- En Generales afectó sólo una vez en Madrid porque tienen más escaños.
		- En el resto de provincias mas pequeñas que Barcelona es imposible en unas Generales el umbral limite
		- Nunca ha pasado en Barcelona pero podría, en ese caso hipotético:
			- afectará solo a un escaño, nunca a tres como pasó en las autonómicas catalanas
			- el escaño anulado no tiene porque ir a un mayoritario
			- aunque la probabilidad de recibirlo si que es proporcional a los votos
		- Además lo que el voto en blanco aporta al monto de votos válidos es ridículo
			- El voto a candidaturas tiene mucho más peso en el umbral (98%) que el blanco
			- Un 2% de voto en blanco, subiría el umbral menos de 1700 votos. (Generales BCN 2008)
			- Si no es testimonial es que el voto en blanco lo ha petado
			- Y si lo peta ya sería una victoria si lo que se quiere es solo mostrar descontento
			- En todo caso, si no te quieres arriesgar a perjudicar a los extraparlamentarios usa otras opciones
			- Por ejemplo, un 3% de voto en blanco se acerca al escaño, si fuera a Escons en Blanc, se computaria como una silla vacía
	- A parte del efecto improbable del umbral, abstenciones, blancos, nulos y candidaturas que no cogieran escaño tienen el mismo efecto
		- No alteran para nada el reparto de Hondt por el hecho de estar ahí
		- Solo afectan en tanto son voto cesante de algún otro partido
			- Un indignado no votaría normalmente a PP, PSOE o CiU
			- Por tanto abstenciones, nulos, blancos... de indignados benefician a estos partidos porque perjudican a alguno del resto.
		- Ni abstención, ni blancos, ni nulos tienen un máximo a partir del qual se anulen las elecciones ni nada por el estilo
			- Existe el mito porque si que lo suele haber en referendum
		- De estos el único que puede alterar los resultados es el voto a candidaturas extraparlamentaria si sube suficiente para obtener el escaño
	- Cuando una candidatura gana un escaño se lo quita a la que tuviera el menor de los cocientes escogidos.
		- Es como decir que se lo quita a la candidatura para la que habían sido más baratos los escaños
		- Ese menor último cociente puede estar tanto en mayoritarios como en minoritarios.
		- Pero la probabilidad de que esté en mayoritarios es mayor.
		- Por eso es falso que si aparece un nuevo minoritario entra en competencia con los otros minoritarios
			- Al menos que compitan por los mismos votantes.
			- Pero si tu alternativa era votar nulo, blanco o abstenerte, no tienes que tener miedo de votar a una opción
	- El poder de unos pocos votos
		- Cuando compiten los últimos divisores
		- Votar en un partido con 0 escaños sube el divisor una unidad
		- Votar en un partido con N escaños tienes que juntar N+1 votos para subir el divisor esa misma unidad unidad
		- Al reves tambien es cierto, si pierdes un voto, es mas grave en los pequeños
	- Si esto es así, votemos siempre a minoritarios y vayamos sumando siempre un escaño
		- Pues no, tampoco es así
		- Cada vez que consigues un escaño el siguiente umbral esta proporcionalmente mas cerca en unidades de cociente
			- Cuando el trasvase de votos es grande acaba compensandose
		- Pero si, de cara a la competencia por los escaños de resto, pocos votos son muy importantes.
	- Voto útil y voto tirado
		- Vende la ilusion de control
		- Éticamente criticable por desincentivar el voto en consciencia
		- Pero es que ademés es totalmente falso
		- La verdad es que todo voto 'es inutil' hasta que se alcanza el siguiente escaño
		- Los escalones para el siguiente escaño, aunque parezcan cada vez mas juntos, son mas o menos iguales porque cada voto vale una enesima parte
		- Para el primer, para el segundo y para el decimo escaño
		- Mientras que haya gente que vote a un partido habra la misma probabilidad de que tenga un resto para llegar al siguiente escaño.
	- Voto dividido
		- Dividir las opciones hace que cada opción tenga su resto
		- Es probable que signifique la perdida de un escaño por cada división

	- En resumen
		- Si quieres votar nulo, abstención o blanco, el unico problema es que, siendo un indignado, es un voto cesante a un partido alternativo
			- Pero no tiene ningún otro efecto lateral!! Hazlo sin miedo de perjudicar a nadie, si es lo que quieres
		- El voto más útil es el que mejor te representa
		- Los minoritarios son más sensibles a perder votos, pero tambien a ganarlos!
		- La division es mala
			- Por desgracia pero para bien hay menos extra parlamentarios
		- Si no te representa ninguno vota formaciones como Escons en Blanc
		- Si no quieres delegar tu poder de decisión por 4 años, los Piratas te dejaran votar por internet en el congreso.
		- El gran poder de la abstención es que es grande
			- Si se puede convertir en otra cosa, se puede cambiar mucho el panorama

- Preguntes de la gent


## Rumorologia

**Rumor: Si la abstención o el voto blanco o nulo supera un límite, pasa algo.**

	No, no pasa nada, ya pueden ser altísimos. Ni se anulan, ni se repiten elecciones.

**Rumor: El umbral del 3% perjudica a los minoritarios**

	Cierto, pero en unas generales en Barcelona nunca ha pasado.
	Hay pocos escaños y cuesta que el reparto llegue a partidos por debajo del umbral.
	Si pasara, como máximo afectaria a un partido con los votos justos para un escaño.
	En ese caso el voto no tiene por que irse a un mayoritario.
	Sí que el mayoritario tiene más números que un minoritario de quedarselo.

**Rumor: El voto en blanco sube el umbral del 3%**

	Cierto, el voto en blanco se considera válido y se usa para calcular el 3%.
	Sin embargo sube en la misma medida que lo subiría un voto a candidatura.
	Por cada 1% mas de voto en blanco, el umbral sube en 700 votos aprox.

**Rumor: El voto blanco, nulo o la abstención favorecen a los mayoritarios.**

	Falso. Si el voto blanco no activa el umbral del 3%,
	el reparto de Hondt es indiferente a la existencia de estas opciones.
	Si que se puede considerar el efecto del voto cesante, si se considera
	que los que han optado por estas opciones hubieran podido votar a minoritarios.

**Rumor: El voto nulo perjudica a mayoritarios**

	Falso. Si optas por nulo porque querias perjudicar a los mayoritarios
	seguramente tampoco ibas a votar mayoritarios, por lo cual no les
	perjudica ni por ser un voto cesante.

**Rumor: La ley de Hondt favorece a los mayoritarios**

	Cierto. Sin embargo mantiene la proporcionalidad de los escaños que se
	obtendrían enteros. La desproporcion viene del reparto de restos.
	En Generales en BCN, el más mayoritario gana como máximo dos escaños por encima de lo proporcional.
	En Generales en BCN, el más minoritario pierde como máximo un escaño respecto a una ley proporcional pura.
	Contra mas desproporción haya en los votos, mas desproporción hay en el reparto de restos.

**Rumor: Se requieren menos votos para un escaño contra más escaños tengas**

	Falso. Los coeficientes están más apretados pero subirlos una unidad 
	cuesta tantos votos como escaños se hayan conseguido.

**Rumor: Es voto útil votar al grande menos malo**

	Falso. Para restarle votos a un partido, puedes sumar votos en cualquiera
	de las otras opciones. Todas tienen la misma probabilidad de que no
	acabes sumando votos para obtener el siguiente escaño.

**Rumor: Es voto tirado votar a candidaturas extraparlamentarias**

	Si, pero es relativo. Si no sumas un escaño, tan tirado es el voto
	en uno que ya tenga escaños y no llegue al siguiente.

**Rumor: Cuando una opción se divide normalmente sale perdiendo**

	Cierto. Si una opción se divide por tres, habrá tres restos de escaño.
	
**Rumor: Cuando un extraparlamentario entra, fastidia al siguiente partido mas pequeño.**

	Es al revés! Entra en competencia con el partido que tenga el último cociente más pequeño.
	Los partidos mayoritarios tienen mas probabilidad de tenerlo.

## Opciones de no-voto

- **Abstención:**

	Generales/BCN: Máxima del 34% en 2000, suele ser primera o segunda opción
	Límite: Los votantes acérrimos de los partidos no dejarían que pasara del 44%
	Por muy alta que sea la abstención no se repiten las elecciones ni nada parecido.
	Efecto en el recuento: Ninguno más allá del voto cesante.
	Hay dos tipos de abstención según los motivos.

	- **Abstención pasiva:**

		**Significa:** No me interesa la política
		Como: Simplemente no ir a votar.
		Representa el aprox 85% de la abstención (según CIS)

	- **Abstención activa:**

		**Significa:** No quiero legitimar el sistema con mi participación
		Es activa si se contribuye a alternativas
		Problema: És difícil diferenciarla de la pasiva
		Sigue siendo una opción ética personal válida

- **Voto nulo (activo):**

	**Significa:** Es un voto de queja
	Como: Poner en el sobre algo que no sea una papeleta de un partido
	Circulan varios modelos de papeleta por internet, pero podemos poner un papel escrito
	Confundible con error, pero no si hay mucho
	Efecto en el recuento: Ninguno más allá del voto cesante.
	Por muy alto que sea el voto nulo no se repiten las elecciones ni nada parecido.
	Mito falso: La mesa no esta obligada a leer lo que diga.

- **Voto blanco:**
	**Significa:** 'no me gusta ninguno'
	Sube el umbral que tienen los partidos minoritarios para entrar.
	En las Generales, es muy improbable que afecte ese umbral.
	En Barcelona, afectaria como máximo a un partido que tenga el primer escaño justito.
	Ese escaño no tiene porque llevarselo un mayoritario, cualquiera con representación tiene igual probabilidad.
	El voto en blanco contribuye poco a subir ese umbral pero contribuye.
	Efecto en el reparto: A parte de subir el umbral, ninguno más allá del voto cesante.
	Si no te quieres arriesgar a perjudicar a minoritarios escoge otra modalidad de voto.











