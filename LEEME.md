enVote: Simulador de flujos electorales
=======================================

enVote es un programa de uso y distribución libre
que hemos desarrollado en la acampada indignada de
Sant Joan Despí para poder dar respuesta de forma 
más ágil a las muchas dudas que teníamos sobre el 
funcionamiento del sistema electoral. Las normas 
pueden estar claras, pero a veces deducir los 
efectos de esas normas es complejo.

Funcionalidades

Los puntos fuertes del programa son:

    Tiene en cuenta abstención, voto en blanco y nulo como opciones
    Se pueden manipular los datos haciendo transferencias de una opción a otra
    Viene con casos hechos, reales, encuestas y de exploracion, y es fácil añadir otros.
    Visualiza claramente como se comportan esas transferencias con la Ley de Hondt y el umbral del 3% sobre el voto válido
    Se limita a simular una circunscripción que es donde el voto de cada ciudadano tiene efecto

Descarga
--------

Existe una version versión ya preparada para Windows.
Escoge la version mas alta de los archivos en [este enlace](http://acampadadespi.org/files/envote/)
Es un archivo zip, descomprime todos los ficheros y
ejecuta el ejecutable 'envote.exe'.
Pista: seguramente tu sistema esté configurado para ocultar la extensión .exe del nombre.

Para Linux solo necesitas instalarte python-pyqt4 y
el codigo fuente que está [mantenido en GitHub][enVoteGitHub].

[enVoteGitHub]:(https://github.com/vokimon/envote)

Puedes usar GitHub para colaborar con el proyecto con
código, datos o traducciones.

Uso
---

Casi todos los elementos, tienen una burbuja explicativa
que aparece cuando dejas quieto el puntero del ratón encima.

Las tartas de la parte superior representan, de izquierda a derecha:

* Proporción de cada opción, considerando el censo completo (opciones de voto y no-voto)
* Proporción considerando solo candidaturas
* Reparto de escaños según la ley de Hondt
* Reparto hipotético usando una ley más proporcional (Hamilton)

Abajo hay una tabla que ilustra la ley de Hondt y el umbral del 3% sobre voto válido.

* Los cocientes de las candidaturas fuera del umbral se ven de color gris
* Los cocientes con el fondo azul son los que han obtenido escaño.
* Los cocientes en rojo o naranja son los que están mas cerca de obtener o perder un escaño.

En medio tienes botones de control y algunas estadísticas.

* Para cambiar de caso, usa el desplegable o los botones ‘Anterior’ y ‘Siguiente’.
* Para transferir votos selecciona opciones de origen y destino, fija la cantidad y clicka en ‘Transfiere’
* Otra forma practica de marcar origen y destino es clickar con los botones izquierdo y derecho sobre los sectores de las tartas.


Traducciones
------------

De momento están disponibles las traducciones a ingles,
castellano y catalán. Si quieres contribuir la traducción
a tu idioma, puedes bajarte el [fichero de traducción][TranslationFiles] y 
usar [Qt Linguist][QtLinguist] para rellenarlo.

[TranslationFiles]:(https://github.com/vokimon/envote/tree/master/i18n)
[QtLinguist]:(http://qt-apps.org/content/show.php/Qt+Linguist+Download?content=89360)


