# El efecto de tu (no)voto (III): Los números
### 2014-05-25 1:28

Un poco tarde, lo se.
El tema es que hoy he tenido un día ocupadillo y no quería publicar nada sin revisar.

Después de las dos entradas anteriores, el resto de personitas tenemos que hacer números.
Principalmente porque se nos ha bombardeado con un montón de mitos sobre el sistema electoral y las posibilidades del mismo que no son ciertas.
Y también porque lo que es verdad para unas elecciones no tiene que serlo para otras y hay que desaprender algunas cosas.


## La teoría


Primero un poco de teoria básica:
La ley electoral que se aplica a todas las elecciones dice que
el reparto de escaños en una circunscripción se hará repartiéndolos según la regla de Hondt
entre los partidos que superen un determinado porcentaje sobre el voto válido.
El voto válido es el voto a candidaturas más el blanco.


Regla de Hondt:
fija en una especie de subasta un precio mínimo por escaño (P)
de tal manera que se repartan todos los escaños (E) sin que a ningún partido le sobren votos para pillar un escaño más.
En general, los votos totales a candidaturas (V) se repartiran entre los votos asignados P*E (donde E es el número total de escaños) y los votos sobrantes de cada candidatura que sumarán, como máximo (P-1)*C, donde C es el número de candidaturas.
Así, simplificando el -1, tenemos la relacion:
$P*E < V < P*E + P*C$.
Haciendo algebra con esta relacion podemos delimitar el precio del escaño,
expresado en porcentaje del "voto a candidatura": 100/(E+C) % < 100*P/V % < 100/E %.


Esa expresión delimita entre los dos casos extremos e improbables, pero ¿qué es lo más probable?
A los partidos con escaños, hay una probabilidad uniforme de que los votos sobrantes estén en cualquier punto entre un escaño y el siguiente.
Eso implica que el sobrante medio de los partidos con escaños tenderá a ser P/2.
Respecto a los partidos sin escaño, por el comportamiento electoral típico, no sigue esa misma distribución uniforme del voto sobrante sinó que tiende a estar por la parte más baja en la mayoría de ellos.
Voy a hacer una suposición de que solo un cuarto de los partidos extra parlamentarios sigue la distribución uniforme de los partidos con escaño.
El voto sobrante no sería $P*C$ sinó que se aproximaría mejor con $P/2*C/4 = P*C/8$ y el precio del escaño en porcentaje de voto a candidaturas se aproximaría al $100/(E+C/8)%$.
Si mi suposición no os gusta, podéis cambiar los números, pero mucho no cambia.


En resumen, el porcentaje de voto a candidatura necesario para un escaño es:

- Mínimo: 100/(E+C) %
- Típico: 100/(E+C/8) %
- Máximo: 100/E %


## ¿Cuales son los números concretos de estas elecciones?


- Una circunscripción única para toda España

- El umbral para entrar en el reparto es del 0% (¡no hay umbral!)

- 34.420.170 electores

- Hay 54 escaños a repartir
- Hay 39 candidaturas


El precio del escaño en porcentaje de voto a candidatura sería:

- Mínimo: 1,07%, Típico: 1,70%, Máximo: 1'85%

En votos dependiendo de la participación:

- Participación: 100%, Mínimo: 370mil, Típico: 585mil, Máximo: 637mil
- Participación: 50%, Mínimo: 187mil, Típico: 292mil, Máximo: 318mil
- Participación: 40%, Mínimo: 148mil, Típico: 234mil, Máximo: 250mil

**Primera conclusión:** En las elecciones europeas, al no haber umbral de entrada, el voto en blanco no tiene ningún efecto especial respecto al voto nulo o la abstención.
El único efecto de las tres elecciones de no-voto es el efecto del VOTO CESANTE del que hablo más abajo.


**Segunda conclusión:** ¿Es más fácil o más difícil para un partido pequeño conseguir su primer escaño? El precio en las generales ronda los 100mil votos.
Pero en unas generales esos 100mil se tienen que sumar en una sola provincia, y en unas europeas se pueden sumar 300mil en todo el estado.
Los partidos pequeños lo tienen mucho más fácil que en las generales para obtener representación.


**Tercera conclusión:** De como hemos obtenido la fórmula del precio típico se puede deducir que el hecho de que una candidatura extraparlamentaria acumule bastantes votos, aunque no obtenga escaño, sirve para bajar el precio de Hondt, ayudando a otras candidaturas extraparlamentarias a obtener su primer escaño.
Como no hay umbral de entrada, votando a minoritarios, si no se obtiene escaño, ayudas a los otros minoritarios a salir.

**Cuarta conclusión:** En las generales, los partidos locales (nacionalistas, independentistas, regionalistas...) tienen ventaja, respecto a los pequeños de ámbito estatal, por concentrar su voto en ciertas circunscripciones.
Pero en las europeas pierden esa ventaja.
Quizás por eso, los partidos locales se han coaligado con partidos locales de otras autonomías para que su fortaleza en generales no se convierta en debilidad en las europeas.
¿Que posibilidades tienen partidos regionalistas minoritarios que no se han coaligado, como les pasa a los dos que hay de Extremadura? Muy, muy pocas: Solo mirando el censo ves, que si Extremadura tuviera una participación similar a la del resto del estado, dos terceras partes de los votos de Extremadura tendrían ir a una de estas dos opciones para que sacara un solo escaño.

**Falsa conclusión:** Podriamos pensar que contra menos participación, al bajar el precio sería mas fácil entrar para los partidos extraparlamentarios.
Pero la abstención en sí no beneficia directamente a derecha, izquierda, mayoritarios, minoritarios o extraparlamentarios.
Depende del perfil del desmotivado.
Un descontento que no vota es voto cesante de los grandes partidos.
Una persona que vea las elecciones como un pulso entre los mayoritarios que no vota es voto cesante de los grandes.
En la abstención yo creo que hoy en día predomina el primer caso.


## Coaliciones, candidatos ocultos y partidos europeos


Respecto a las candidaturas, coaliciones y demás hay algunas cosas importantes a tener en cuenta:


- Las candidaturas pueden presentarse con una marca autonómica en la papeleta para que los hooligans identifiquemos a nuestro equipo de toda la vida

- En esa papeleta autonómica la lista de candidatos que aparecen puede ocultar los candidatos no locales, aunque el voto vaya a la lista completa estatal.
Si veis una papeleta medio vacía, es el caso.

- Cada partido participante en una coalición puede apoyar a un partido europeo diferente, que tampoco aparece en la papeleta.


Por eso es importante saber que hay una parte de la lista que puede que no veas en la papeleta.
Podría pasar que un votante de Euskadi vote a una lista en la que solo aparece gente del PNV, que apoyan a los Democratas Europeos, pero su voto contribuiría sin saberlo a que entrara un diputado de Unió que apoya a los Populares Europeos.
Puede que le parezca bien o puede que no, pero es importante ser consciente de ello.
Los partidos que forman las coaliciones y a qué partido europeo pertenecen los puedes encontrar en la wikipedia[1], por ejemplo.
Por otro lado, tampoco hay demasiada disciplina de partido europeo en Bruselas así que el partido europeo solo es importante de cara a la elección de los cargos y no en las votaciones concretas.


[1](http://es.wikipedia.org/wiki/Elecciones_al_Parlamento_Europeo_de_2014_%28Espa%C3%B1a%29)


## Teoría de juegos


A partir de aqui, ¿como evalúo el efecto de mi (no)voto? Siguiendo la teoría de juegos, tendríamos que pensar que todo el mundo ha tomado su decisión y faltas tú.
Tendríamos que considerar los posibles escenarios previos a tu decisión, lo que se llama las hipótesis de partida, y la probabilidad de que pasen.
La triste noticia es que tu voto considerado así es muy poco probable que tenga efecto alguno, votes a quien votes.
Es así: ni minoritarios ni mayoritarios tu voto aislado es inútil.
Solo tendría efecto en el caso de que el partido tenga P-1 votos sobrantes y el tuyo sea el que haga P.
Eso pasa con una probabilidad de 1/P, donde P hemos visto que son cientosmiles.


Pos vaya, ¿no? ¿Como lo hacemos entonces? Pues no considerando un voto o no-voto, sino considerando unos cuantos.
Dado un dilema si hacer una cosa o otra, me pregunto: Que efecto tiene que mil, 10mil, 100mil...
en mi misma disyuntiva tome una misma opción y después qué probabilidad hay de que os junteis todos esos en todo el estado.
Todo es un poco difuso pero vereis que nos permitirá hacer algunos razonamientos para entender el efecto de nuestro voto o no voto.
Con ayuda de programas como envote [2] puedes simular esos flujos de personas fácilmente a partir de una situación que pienses que es probable y incluyendo como opciones las de no-voto.


[2] http://acampadadespi.org/blog/?page_id=222


¿Como construimos la situación probable antes de nuestro voto (la hipótesis de partida)? Pues considerando encuestas, elecciones anteriores, los hooligans de cada partido (también llamado suelo electoral), diversas hipotesis de abstención y situación electoral.
También es útil considerar como situación probable de partida situaciones extremas.
Si en condiciones extremas opuestas algo sigue pasando, es que pasará.
Y ojo con nuestro sesgo, no tiene porque pasar lo que queremos nosotros que pase y mola mucho construir situaciones bonitas.


## El voto cesante


Cuando consideramos nuestra opción (y la de los otros ene-mil que ante la misma disyuntiva hacen lo mismo), el otro efecto importante que tiene nuestro voto o no-voto es el de VOTO (O NO-VOTO) CESANTE a cualquier opción que podríamos haber escogido.
El efecto es más importante cuanta mayor hubiera sido probabilidad de escoger la otra opción.
Por ejemplo, si construimos la hipótesis de partida a partir de los resultados de las elecciones anteriores, es importante considerar que habíamos escogido en las elecciones previas y elegir 'grupo con nuestro dilema' entre la gente que había tomado esa opción.
Si hemos construido esa situación probable a partir de encuestas, tenemos que valorar el voto cesante entre las que eran nuestras opciones en el momento de la encuesta.


Por eso decia en la anterior entrada que a los "partidos de gobierno" les interesa que los descontentos no voten a candidaturas.
Si los descontentos escogen opciones de no-voto, el voto cesante se lo llevan sobretodo las otras candidaturas y ellos salen ganando con menos competencia en el reparto de escaños.


## Casos simulados


Como no creo que me de tiempo a la cuarta parte, en la que quería poner algunas conclusiones de casos que he simulado, os resumo un par aquí, uno de aplicacion a los extraparlamentario y otro de aplicación a los que consideráis varias opciones con representación:

Si no-votos se convirtieran en votos al azar a partidos extraparlamentarios no fascistas (20 opciones) dichas opciones suben el doble de lo que pudiera subir el precio por escaño por añadir votos a la cesta.
Si lo concentras en 10 o en 5 opciones, la cosa tiene un efecto mas grande aun.
Además como he dicho arriba, si no consiguen el voto sirve para bajar el precio para que el resto consiga su primer escaño.

Desplazar 100mil de un partido con representacion a otro, implica que con un 30% de posibilidades el emisor pierda el voto, y otro 30% de que el receptor lo gane.
Pero las dos cosas se pueden dar a la vez, por separado o no darse.
Si se da una o otra pero no las dos, implica que tiene un efecto revote en otro partido.
Que partido puede recibir o perder ese voto? Todos tienen posibilidades pero normalmente hay mas probabilidad que lo pierda o lo gane un mayoritario.

En todo caso, coged el enVote y haced vuestra simulacion, oye.
 
Sin más, creo que os he dado herramientas suficientes para que hagáis los experimentos vosotros mismos.
Espero que os sea útil.
Como siempre en estas cosas os recomiendo que voteis a quien penséis que os representa mejor
y si no habéis encontrado ese alguien,
dejadme sugeriros que no os quedéis en casa, que considereis votar aunque sea a **Escaños en Blanco**
que convierten el voto en blanco en escaños vacios para que realmente nadie os represente.
Que conste que no es mi opción, pero la recomendaré siempre como mejor opción que el no-voto.

