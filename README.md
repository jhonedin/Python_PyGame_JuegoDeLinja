# Python_PyGame_JuegoDeLinja
# El Juego de Linja

![Tablero del Juego](https://github.com/jhonedin/Python_PyGame_JuegoDeLinja/blob/master/imagenes/Tablero.png)

Tablero del Juego

Este fue un proyecto desarrollado como parte del proyecto del curso de la asignatura Inteligencia Artificial del pregrado en Ingeniería de Sistemas, en compañia de otros dos colaboradores relacionados en el archivo del juego.

Se trata del juego Español Llamado Linja donde dos jugadores en este caso humano-maquina deben mover la fichas y ganar el juego conforme a las reglas del mismo.

En este juego se aplico conceptos de Agentes Inteligentes de Inteligencia Artificial. Se aplico el algoritmo MIN-MAX.

El agente que se propone implementar será un agente de software con
características de percepción y de actuación, ya que, tendrá acceso al estado
actual del tablero (percepción) con el fin de tomar acciones de mover el tablero
(actuación) utilizando el algoritmo minimax.
El agente es basado en utilidad, ya que con el algoritmo minimax, se estudian las acciones que permitan llegar a un estado meta, en cada acción posible que pueda realizar, se calculará su utilidad (valor heurístico), con el fin de realizar la jugada MAX, minimizando la pérdida en el juego. Las propiedades del ambiente del juego de Linja, se caracterizan por:

● El ambiente es accesible, ya que el agente tiene acceso al estado total del
juego que se encuentre en un momento dado en el turno.<br>
● Es determinista, ya que cada acción que escoge el agente en la jugada,
afectará la siguiente jugada.<br>
● El juego es no episódico, ya que la calidad del juego es importante a
medida que se avanza.<br>
● Finalmente, el juego es discreto, ya que el agente tiene una cantidad
limitada de percepciones y acciones discernibles.

INSTALACION

1- INSTALAR PYTHON 3: https://www.python.org/downloads/  <br>
2- INSTALAR PYGAME: PIP INSTALL PYGAME <br>
3- SI EL EDITOR DE TEXTO ES VISUAL ESTUDIO CODE NO OLVIDAR ESPECIFICAR LA RUTA DEL INTERPRETE:
File > Preferences > Settings > Workspace > Extensions > Python <br>
4- INSTALAR LA EXTENSION QUE EL EDITOR MISMO VA SUGIRIENDO INSTALAR PARA EVITAR ERRORES.
